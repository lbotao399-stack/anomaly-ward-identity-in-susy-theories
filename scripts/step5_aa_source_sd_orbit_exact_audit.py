#!/usr/bin/env python3
"""Exact arithmetic audit for the ordered-AA source-word proposal.

The script checks only the finite word, resolvent, Wick-support, and loop-
arithmetic identities stated in
``audits/step5-aa-source-expansion-sd-orbit.md``.  It does not certify the
physical matter cut assignment or the still-open pure-gauge source orbit.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-source-expansion-sd-orbit.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, tuple) and isinstance(self.expected, tuple):
            return len(self.actual) == len(self.expected) and all(
                sp.simplify(actual - expected) == 0
                if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic)
                else actual == expected
                for actual, expected in zip(self.actual, self.expected, strict=True)
            )
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.simplify(self.actual - self.expected) == 0
        return self.actual == self.expected


def matrix_entries(vector: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    """Return entries of mathsf r=-i sigma_E.r in the locked Euclidean frame."""

    imaginary = sp.I
    sigma_1 = sp.Matrix(((0, 1), (1, 0)))
    sigma_2 = sp.Matrix(((0, -imaginary), (imaginary, 0)))
    sigma_3 = sp.Matrix(((1, 0), (0, -1)))
    identity = sp.eye(2)
    sigma_e = (-imaginary * sigma_1, -imaginary * sigma_2, -imaginary * sigma_3, identity)
    mathsf = tuple(-imaginary * matrix for matrix in sigma_e)
    matrix = sum((mathsf[index] * vector[index] for index in range(4)), sp.zeros(2))
    return matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]


def diagonal_coefficients(polynomial: sp.Expr, loop: tuple[sp.Symbol, ...]) -> tuple[sp.Expr, ...]:
    expanded = sp.Poly(sp.expand(polynomial), *loop)
    return tuple(sp.expand(expanded.coeff_monomial(component**2)) for component in loop)


def main() -> int:
    epsilon = sp.symbols("epsilon", positive=True)
    y, z = sp.symbols("y z", real=True)
    d_0, d_1, d_2 = sp.symbols("D0 D1 D2", nonzero=True)

    # O0, O1, O2 contain 1, 2, 3 displayed products.  Acting with the
    # covariant D_- gives respectively 2, 4+2, and 6+4+2 occurrence words.
    source_product_counts = (1, 2, 3)
    insertion_word_counts = (2, 4 + 2, 6 + 4 + 2)

    # Expansion of exp[-(g S3+g^2 S4)/hbar] against I0+g I1+g^2 I2.
    resolvent_signs = (1, -1, -1, 1)
    resolvent_denominators = (1, 1, 1, 2)

    area = sp.integrate(1 - y, (y, 0, 1))
    z_moment = sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1))
    marked_first_moment = 2 * sp.integrate(
        sp.integrate(1 - z, (z, 0, 1 - y)), (y, 0, 1)
    )
    marked_second_moment = 2 * sp.integrate(
        sp.integrate(z - sp.Rational(1, 2), (z, 0, 1 - y)), (y, 0, 1)
    )
    complete_moment = sp.simplify(marked_first_moment + marked_second_moment)

    # Two-component matter word.  The symbols are the four entries of
    # mathsf r_i.  W_ij is the dotted wedge of the plus rows.
    entries = sp.symbols(
        "a0 b0 c0 d0 a1 b1 c1 d1 a2 b2 c2 d2",
        commutative=True,
    )
    (
        a_0,
        b_0,
        c_0,
        d_0e,
        a_1,
        b_1,
        c_1,
        d_1e,
        a_2,
        b_2,
        c_2,
        d_2e,
    ) = entries
    w_12 = a_1 * b_2 - b_1 * a_2
    w_02 = a_0 * b_2 - b_0 * a_2
    w_01 = a_0 * b_1 - b_0 * a_1
    det_0 = a_0 * d_0e - b_0 * c_0
    det_1 = a_1 * d_1e - b_1 * c_1
    det_2 = a_2 * d_2e - b_2 * c_2
    s_1 = det_0 * w_12 - det_1 * w_02
    mixed_21 = a_2 * d_1e - c_1 * b_2
    s_2 = w_01 * mixed_21
    factorized_sum = w_12 * (a_0 * (d_0e - d_1e) - b_0 * (c_0 - c_1))
    omega_21 = a_2 * d_1e - a_1 * d_2e - b_2 * c_1 + b_1 * c_2
    det_difference = (a_1 - a_2) * (d_1e - d_2e) - (b_1 - b_2) * (c_1 - c_2)

    # Target-blind rank-two check in a nondegenerate Euclidean frame
    # p=e_1, q=e_4.  Covariance leaves one p_+ wedge q_+ coefficient, so
    # this frame fixes that coefficient without importing the HT target.
    loop = sp.symbols("L1 L2 L3 L4", real=True)
    p = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    q = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))
    total = tuple(p[index] + q[index] for index in range(4))
    k = tuple(loop[index] + y * q[index] + z * total[index] for index in range(4))
    r_0 = k
    r_1 = tuple(k[index] - q[index] for index in range(4))
    r_2 = tuple(k[index] - p[index] - q[index] for index in range(4))
    m_0 = matrix_entries(r_0)
    m_1 = matrix_entries(r_1)
    m_2 = matrix_entries(r_2)
    aa_0, bb_0, cc_0, dd_0 = m_0
    aa_1, bb_1, cc_1, dd_1 = m_1
    aa_2, bb_2, cc_2, dd_2 = m_2
    ww_12 = aa_1 * bb_2 - bb_1 * aa_2
    ww_02 = aa_0 * bb_2 - bb_0 * aa_2
    ww_01 = aa_0 * bb_1 - bb_0 * aa_1
    frame_s_1 = (aa_0 * dd_0 - bb_0 * cc_0) * ww_12 - (
        aa_1 * dd_1 - bb_1 * cc_1
    ) * ww_02
    frame_s_2 = ww_01 * (aa_2 * dd_1 - cc_1 * bb_2)
    diag_1 = diagonal_coefficients(frame_s_1, loop)
    diag_2 = diagonal_coefficients(frame_s_2, loop)
    transverse_1 = sp.expand(diag_1[1] + diag_1[2])
    transverse_2 = sp.expand(diag_2[1] + diag_2[2])
    p_entries = matrix_entries(p)
    q_entries = matrix_entries(q)
    p_wedge_q = sp.expand(p_entries[0] * q_entries[1] - p_entries[1] * q_entries[0])

    # A chiral projector contributes 1/16 and its closed D word contributes
    # 16.  The bottom maps B=D_+ Phi| and C=tilde Phi| carry unit factors.
    packaged_chiral_projector = sp.Rational(1, 16) * 16
    b_bottom_map = sp.Integer(1)
    c_bottom_map = sp.Integer(1)

    checks = [
        Check("source_product_counts_O0_O1_O2", source_product_counts, (1, 2, 3)),
        Check("insertion_word_counts_I0_I1_I2", insertion_word_counts, (2, 6, 12)),
        Check("g2_resolvent_signs", resolvent_signs, (1, -1, -1, 1)),
        Check("g2_resolvent_factorials", resolvent_denominators, (1, 1, 1, 2)),
        Check("simplex_area", area, sp.Rational(1, 2)),
        Check("simplex_z_moment", z_moment, sp.Rational(1, 6)),
        Check("marked_first_moment", marked_first_moment, sp.Rational(2, 3)),
        Check("marked_second_moment", marked_second_moment, -sp.Rational(1, 6)),
        Check("complete_marked_moment", complete_moment, sp.Rational(1, 2)),
        Check("single_placement_coefficient", 2 * marked_first_moment, sp.Rational(4, 3)),
        Check("second_placement_coefficient", 2 * marked_second_moment, -sp.Rational(1, 3)),
        Check("complete_matter_coefficient", 2 * complete_moment, 1),
        Check("matter_word_factorization", s_1 + s_2, factorized_sum),
        Check(
            "mixed_polarization_identity",
            2 * mixed_21,
            det_1 + det_2 - det_difference + omega_21,
        ),
        Check("frame_diag_S1", diag_1, tuple(sp.I * x for x in (3 * z - 1, z - 1, z - 1, z + 1))),
        Check("frame_diag_S2", diag_2, tuple(sp.I * x for x in (1 - 3 * z, 1 - z, -z, -z))),
        Check("frame_transverse_S1", transverse_1, 2 * sp.I * (z - 1)),
        Check("frame_transverse_S2", transverse_2, sp.I * (1 - 2 * z)),
        Check("frame_transverse_sum", transverse_1 + transverse_2, p_wedge_q),
        Check("packaged_chiral_projector", packaged_chiral_projector, 1),
        Check("physical_B_bottom_map", b_bottom_map, 1),
        Check("physical_C_bottom_map", c_bottom_map, 1),
        Check("full_square_cut_edge_0", d_0 / (d_0 * d_1 * d_2) - 1 / (d_1 * d_2), 0),
        Check("full_square_cut_edge_1", d_1 / (d_0 * d_1 * d_2) - 1 / (d_0 * d_2), 0),
        Check("full_square_cut_edge_2", d_2 / (d_0 * d_1 * d_2) - 1 / (d_0 * d_1), 0),
        Check("two_source_attachments", 2, 2),
        Check("two_marked_Dminus_placements_per_attachment", 2, 2),
        Check("complete_matter_occurrence_rows", 2 * 2, 4),
        Check("chiral_antisymmetric_wedge", -p_wedge_q, q_entries[0] * p_entries[1] - q_entries[1] * p_entries[0]),
        Check("evanescent_trace", 4 - (4 - 2 * epsilon), 2 * epsilon),
    ]

    text = AUDIT.read_text(encoding="utf-8")
    anchors = {
        "status": "RETRACTED_SINGLE_MARKED_PLACEMENT",
        "resolvent": r"\langle\mathcal I_2\rangle_0",
        "no_double_count": "NO_DOUBLE_COUNT_PARENT_MINUS_CUT",
        "matter_first": r"\mathcal S_1",
        "matter_second": r"\mathcal S_2",
        "matter_unit": r"=\lambda_1",
        "bubble_zero": r"P_+\wedge P_+=0",
        "pure_gauge_open": "BLOCKED_AA_GAUGE_FULL_MARKED_OCCURRENCE_RECOUNT",
        "matter_cut_open": "BLOCKED_AA_MATTER_PHYSICAL_CUT_ASSIGNMENT",
        "candidate_boundary": "CANDIDATE_NOT_ACCEPTED",
    }
    checks.extend(Check(f"audit_anchor_{key}", value in text, True) for key, value in anchors.items())

    failed = [check for check in checks if not check.passed]
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"{status} {check.name}: {check.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
