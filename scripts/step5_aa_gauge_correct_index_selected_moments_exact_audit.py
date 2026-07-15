#!/usr/bin/env python3
"""Exact simplex moments for the corrected two-edge AA gauge numerator."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-gauge-correct-index-selected-moments-exact.md"


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

    m0 = simplex(sp.Integer(1), y, z)
    my = simplex(y, y, z)
    mz = simplex(z, y, z)
    r0 = sp.expand(my * q + mz * P)
    r2 = sp.expand(r0 - P)
    s01 = sp.expand(-2 * r2)
    s02 = sp.expand(-2 * r0)

    bar_r, rd_r, mu2, denom, other = sp.symbols(
        "bar_r rd_r mu2 denom other", nonzero=True
    )
    full_d_zero = sp.simplify(rd_r / denom - other)
    four_d_remainder = sp.simplify(bar_r / denom - other)
    cut_substitution = {other: rd_r / denom, bar_r: rd_r + mu2}

    text = AUDIT.read_text(encoding="utf-8")
    return [
        Check("simplex_unit", m0, 1),
        Check("simplex_y", my, sp.Rational(1, 3)),
        Check("simplex_z", mz, sp.Rational(1, 3)),
        Check("r0_moment", r0, (p + 2 * q) / 3),
        Check("r2_moment", r2, -(2 * p + q) / 3),
        Check("selected_mark01", s01, (4 * p + 2 * q) / 3),
        Check("selected_mark02", s02, -(2 * p + 4 * q) / 3),
        Check("selected_sum", sp.expand(s01 + s02), 2 * (p - q) / 3),
        Check("full_d_parent_minus_cut", full_d_zero.subs(cut_substitution), 0),
        Check(
            "four_d_parent_minus_cut",
            four_d_remainder.subs(cut_substitution),
            mu2 / denom,
        ),
        Check("status_anchor", "AA_GAUGE_TWO_SELECTED_EDGES_EXACT__LONGITUDINAL_QUOTIENT_PENDING" in text, True),
        Check("no_final_coefficient", "No signed AA gauge coefficient is assigned here" in text, True),
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
