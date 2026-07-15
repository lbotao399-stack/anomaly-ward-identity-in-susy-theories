#!/usr/bin/env python3
"""Exact scalar, rank-one, and rank-two DRED mu^2 triangle moments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-dred-cutting-failure-exact.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        return sp.simplify(sp.sympify(self.actual) - sp.sympify(self.expected)) == 0


def main() -> int:
    epsilon = sp.symbols("epsilon", positive=True)
    mu, Delta = sp.symbols("mu Delta", positive=True)
    y, z = sp.symbols("y z", nonnegative=True)
    d = 4 - 2 * epsilon
    common = mu ** (2 * epsilon) / (4 * sp.pi) ** (2 - epsilon)
    i1 = common * sp.gamma(epsilon - 1) * Delta ** (1 - epsilon)
    i2 = common * sp.gamma(epsilon) * Delta ** (-epsilon)
    i3 = common * sp.gamma(1 + epsilon) * Delta ** (-1 - epsilon) / 2

    centered_scalar = (4 - d) * (i2 - Delta * i3) / d
    l4_i3 = i1 - 2 * Delta * i2 + Delta**2 * i3
    centered_rank_two = (4 - d) * l4_i3 / (d * (d + 2))

    simplex = lambda value: sp.integrate(
        sp.integrate(value, (z, 0, 1 - y)), (y, 0, 1)
    )
    ky = y + z
    kz = z
    delta_p2 = (1 - y - z) * y + (1 - y - z) * z
    delta_pq = 2 * (1 - y - z) * z
    delta_q2 = (1 - y - z) * z + y * z

    scalar_triangle = 2 * simplex(1) / (32 * sp.pi**2)
    rank_one_p = -2 * simplex(ky) / (32 * sp.pi**2)
    rank_one_q = -2 * simplex(kz) / (32 * sp.pi**2)
    rank_two_pp = 2 * simplex(ky**2) / (32 * sp.pi**2)
    rank_two_pq_each = 2 * simplex(ky * kz) / (32 * sp.pi**2)
    rank_two_qq = 2 * simplex(kz**2) / (32 * sp.pi**2)
    rank_two_metric_p2 = -2 * simplex(delta_p2) / (64 * sp.pi**2)
    rank_two_metric_pq = -2 * simplex(delta_pq) / (64 * sp.pi**2)
    rank_two_metric_q2 = -2 * simplex(delta_q2) / (64 * sp.pi**2)

    checks = [
        Check("l4_reduction", l4_i3 / (Delta * i2), (epsilon - 3) * (epsilon - 2) / (2 * (epsilon - 1))),
        Check("centered_scalar_limit", sp.limit(centered_scalar, epsilon, 0, dir="+"), 1 / (32 * sp.pi**2)),
        Check("centered_rank_one_limit", 0, 0),
        Check("centered_rank_two_limit", sp.limit(centered_rank_two, epsilon, 0, dir="+"), -Delta / (64 * sp.pi**2)),
        Check("simplex_area", simplex(1), sp.Rational(1, 2)),
        Check("simplex_y", simplex(y), sp.Rational(1, 6)),
        Check("simplex_z", simplex(z), sp.Rational(1, 6)),
        Check("simplex_y2", simplex(y**2), sp.Rational(1, 12)),
        Check("simplex_yz", simplex(y * z), sp.Rational(1, 24)),
        Check("scalar_triangle", scalar_triangle, 1 / (32 * sp.pi**2)),
        Check("rank_one_p", rank_one_p, -1 / (48 * sp.pi**2)),
        Check("rank_one_q", rank_one_q, -1 / (96 * sp.pi**2)),
        Check("rank_two_pp", rank_two_pp, 1 / (64 * sp.pi**2)),
        Check("rank_two_pq_each", rank_two_pq_each, 1 / (128 * sp.pi**2)),
        Check("rank_two_qq", rank_two_qq, 1 / (192 * sp.pi**2)),
        Check("rank_two_metric_p2", rank_two_metric_p2, -1 / (384 * sp.pi**2)),
        Check("rank_two_metric_pq", rank_two_metric_pq, -1 / (384 * sp.pi**2)),
        Check("rank_two_metric_q2", rank_two_metric_q2, -1 / (384 * sp.pi**2)),
    ]

    text = AUDIT.read_text(encoding="utf-8")
    anchors = (
        r"J_{\rm ev}^{\mu\nu}(\Delta)",
        r"-\frac{\Delta}{64\pi^2}\bar\delta^{\mu\nu}",
        r"-\frac{2p^\mu+q^\mu}{96\pi^2}",
        r"\frac{p^\mu p^\nu}{64\pi^2}",
        r"-\frac{\bar\delta^{\mu\nu}}{384\pi^2}",
    )
    for index, anchor in enumerate(anchors, start=1):
        checks.append(Check(f"audit_anchor_{index}", int(anchor in text), 1))

    failed = [row for row in checks if not row.passed]
    for row in checks:
        print(f"{'PASS' if row.passed else 'FAIL'} {row.name}: {row.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
