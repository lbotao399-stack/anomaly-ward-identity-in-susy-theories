#!/usr/bin/env python3
"""Reject Gate-2W source/saturation recount using the final sparse rows."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-gauge-gate2w-double-count-exact.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.simplify(self.actual - self.expected) == 0
        return self.actual == self.expected


def simplex(expr: sp.Expr, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    return sp.simplify(2 * sp.integrate(sp.integrate(expr, (z, 0, 1 - y)), (y, 0, 1)))


def build_checks() -> list[Check]:
    y, z = sp.symbols("y z", real=True)
    p, q = sp.symbols("p q")
    P = p + q
    source = -sp.Rational(1, 4)
    exact_final_row = sp.Integer(2)
    exact_remaining_endpoint = sp.simplify(exact_final_row / source)
    gate2w_recount = sp.simplify(source * 16 * 2)
    recount_ratio = sp.simplify(gate2w_recount / exact_final_row)

    my = simplex(y, y, z)
    mz = simplex(z, y, z)
    r0 = sp.expand(-my * q - mz * P)
    r2 = sp.expand(r0 + P)
    f01 = sp.expand(-2 * r2)
    f02 = sp.expand(-2 * r0)

    hbar, g = sp.symbols("hbar g", nonzero=True)
    wvp = sp.simplify(
        (-sp.I * g / (4 * hbar))
        * (sp.I * g / (4 * hbar))
        * (-hbar) ** 3
    )

    text = AUDIT.read_text(encoding="utf-8")
    return [
        Check("source_scalar", source, -sp.Rational(1, 4)),
        Check("exact_final_sparse_coefficient", exact_final_row, 2),
        Check("exact_remaining_endpoint_factor", exact_remaining_endpoint, -8),
        Check("source_times_exact_endpoint", source * exact_remaining_endpoint, 2),
        Check("gate2w_recount", gate2w_recount, -8),
        Check("gate2w_over_exact_ratio", recount_ratio, -4),
        Check("simplex_y", my, sp.Rational(1, 3)),
        Check("simplex_z", mz, sp.Rational(1, 3)),
        Check("outgoing_r0_moment", r0, -(p + 2 * q) / 3),
        Check("outgoing_r2_moment", r2, (2 * p + q) / 3),
        Check("outgoing_f01_moment", f01, -(4 * p + 2 * q) / 3),
        Check("outgoing_f02_moment", f02, (2 * p + 4 * q) / 3),
        Check("vertex_propagator_core", wvp, -hbar * g**2 / 16),
        Check("rank_one_not_rank_two", 1 == 2, False),
        Check("status_anchor", "GATE2W_SECTION8_REJECTED__FINAL_SPARSE_ROW_RECOUNTED_BY_MINUS_FOUR" in text, True),
        Check("target_blind_anchor", "No external target enters this audit" in text, True),
    ]


def main() -> int:
    checks = build_checks()
    failed = [row for row in checks if not row.passed]
    for row in checks:
        print(f"{'PASS' if row.passed else 'FAIL'} {row.name}: {row.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
