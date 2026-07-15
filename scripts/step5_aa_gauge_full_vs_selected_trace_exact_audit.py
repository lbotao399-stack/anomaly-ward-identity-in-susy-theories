#!/usr/bin/env python3
"""Exact harmonic trace audit for the corrected-index AA gauge parent."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-aa-gauge-full-vs-selected-trace-exact.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.expand(self.actual - self.expected) == 0
        return self.actual == self.expected


def entries(vector: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    i = sp.I
    sigma_1 = sp.Matrix(((0, 1), (1, 0)))
    sigma_2 = sp.Matrix(((0, -i), (i, 0)))
    sigma_3 = sp.Matrix(((1, 0), (0, -1)))
    matrices = (-sigma_1, -sigma_2, -sigma_3, -i * sp.eye(2))
    matrix = sum(
        (matrices[index] * vector[index] for index in range(4)),
        sp.zeros(2),
    )
    return matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]


def homogeneous(polynomial: sp.Expr, loop: tuple[sp.Symbol, ...], degree: int) -> sp.Expr:
    poly = sp.Poly(sp.expand(polynomial), *loop)
    answer = sp.Integer(0)
    for powers, coefficient in poly.terms():
        if sum(powers) == degree:
            answer += coefficient * sp.prod(
                loop[index] ** powers[index] for index in range(4)
            )
    return sp.expand(answer)


def laplacian(polynomial: sp.Expr, loop: tuple[sp.Symbol, ...]) -> sp.Expr:
    return sp.expand(sum(sp.diff(polynomial, component, 2) for component in loop))


def main() -> int:
    loop = sp.symbols("l0:4")
    external = sp.symbols("P0:4")
    a, b, c, d = entries(loop)
    cap_a, cap_b, cap_c, cap_d = entries(external)
    a2, b2, c2, d2 = (
        a + cap_a,
        b + cap_b,
        c + cap_c,
        d + cap_d,
    )
    ell_sq = sum(component**2 for component in loop)
    ell_dot_p = sum(loop[index] * external[index] for index in range(4))
    p_sq = sum(component**2 for component in external)

    det0 = sp.expand(a * d - b * c)
    det2 = sp.expand(a2 * d2 - b2 * c2)
    wedge02 = sp.expand(a * b2 - b * a2)

    selected01 = sp.expand(2 * b2 * det0)
    selected02 = sp.expand(2 * b * det2)
    longitudinal01 = sp.expand(-2 * d * wedge02)
    longitudinal02 = sp.Integer(0)
    selected = sp.expand(selected01 + selected02)
    longitudinal = sp.expand(longitudinal01 + longitudinal02)
    full = sp.expand(selected + longitudinal)

    full_closed = sp.expand(2 * b * (a2 * (d + d2) - b2 * (c + c2)))
    selected_closed = sp.expand(
        -2 * (b + cap_b) * ell_sq
        - 2 * b * (ell_sq + 2 * ell_dot_p + p_sq)
    )

    selected3 = homogeneous(selected, loop, 3)
    selected2 = homogeneous(selected, loop, 2)
    full3 = homogeneous(full, loop, 3)
    full2 = homogeneous(full, loop, 2)
    long3 = homogeneous(longitudinal, loop, 3)
    long2 = homogeneous(longitudinal, loop, 2)

    selected_scalar3 = sp.expand(ell_sq * laplacian(selected3, loop) / 12)
    selected_scalar2 = sp.expand(ell_sq * laplacian(selected2, loop) / 8)
    full_scalar3 = sp.expand(ell_sq * laplacian(full3, loop) / 12)
    full_scalar2 = sp.expand(ell_sq * laplacian(full2, loop) / 8)
    long_scalar3 = sp.expand(ell_sq * laplacian(long3, loop) / 12)
    long_scalar2 = sp.expand(ell_sq * laplacian(long2, loop) / 8)

    checks = [
        Check("det_r0", det0, -ell_sq),
        Check("det_r2", det2, -(ell_sq + 2 * ell_dot_p + p_sq)),
        Check("selected_closed_form", selected, selected_closed),
        Check("full_closed_form", full, full_closed),
        Check("selected_cubic_scalar", selected_scalar3, -4 * b * ell_sq),
        Check("selected_quadratic_scalar", selected_scalar2, -3 * cap_b * ell_sq),
        Check("full_cubic_scalar", full_scalar3, -4 * b * ell_sq),
        Check("full_quadratic_scalar", full_scalar2, -2 * cap_b * ell_sq),
        Check("longitudinal_cubic_scalar", long_scalar3, 0),
        Check("longitudinal_quadratic_scalar", long_scalar2, cap_b * ell_sq),
        Check(
            "occurrence_tagged_selected_defect",
            -2 * (b2 + b),
            -2 * (2 * b + cap_b),
        ),
    ]

    text = AUDIT.read_text(encoding="utf-8")
    for anchor in (
        "AA_GAUGE_GLOBAL_TRACE_NOT_EQUAL_TO_EDGE_TAGGED_CUT",
        r"\Pi_{\mathrm{sc}}G_{\mathcal S}^{(2)}",
        r"\Pi_{\mathrm{sc}}G_{\mathcal L}^{(2)}",
        "MISSING_ROWWISE_LONGITUDINAL_TO_CONTACT_EDGE_MAP",
    ):
        checks.append(Check(f"audit_anchor::{anchor}", anchor in text, True))

    failed = [row for row in checks if not row.passed]
    for row in checks:
        print(f"{'PASS' if row.passed else 'FAIL'} {row.name}: {row.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
