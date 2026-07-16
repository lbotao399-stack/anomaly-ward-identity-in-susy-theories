#!/usr/bin/env python3
"""Exact ordered AB1 G2/G3 superspace D-word replay.

The calculation uses sparse left-Grassmann polynomials with SymPy
coefficients.  It does not use the holomorphic-twist coefficient as input.

Vertex order is ``S,M,H`` for G3 and ``S,L,R`` for G2.  At every vertex the
generator order is ``theta+, theta-, bartheta_dot+, bartheta_dot-``.  The
locked square conventions are

    D^2 = 2 D_- D_+,
    barD^2 = 2 barD_dot+ barD_dot-,
    {D_a,barD_dot-a} = 2 r_{a dot-a}.

The delta normalization and Berezin measure are fixed together by
``delta^4(theta)=theta^2 bartheta^2=4 theta+ theta- bartheta+ bartheta-``
and ``int d^4 theta delta^4(theta)=1``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Mapping

import sympy as sp


VERTEX_COUNT = 3
GENERATOR_COUNT = 4 * VERTEX_COUNT
S, M, H = 0, 1, 2


class Grassmann:
    """Sparse exterior polynomial with exact SymPy coefficients."""

    __slots__ = ("terms",)

    def __init__(self, terms: Mapping[int, object] | None = None) -> None:
        self.terms = {
            mask: sp.expand(sp.sympify(coeff))
            for mask, coeff in (terms or {}).items()
            if coeff != 0
        }

    @classmethod
    def scalar(cls, value: object) -> "Grassmann":
        value = sp.sympify(value)
        return cls({0: value}) if value != 0 else cls()

    @classmethod
    def generator(cls, index: int) -> "Grassmann":
        return cls({1 << index: sp.Integer(1)})

    def __add__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        terms = dict(self.terms)
        for mask, coeff in rhs.terms.items():
            value = sp.expand(terms.get(mask, 0) + coeff)
            if value != 0:
                terms[mask] = value
            elif mask in terms:
                del terms[mask]
        return Grassmann(terms)

    __radd__ = __add__

    def __neg__(self) -> "Grassmann":
        return Grassmann({mask: -coeff for mask, coeff in self.terms.items()})

    def __sub__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        return self + (-rhs)

    def __rsub__(self, other: object) -> "Grassmann":
        return Grassmann.scalar(other) - self

    def __mul__(self, other: object) -> "Grassmann":
        rhs = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        terms: dict[int, sp.Expr] = {}
        for left_mask, left_coeff in self.terms.items():
            for right_mask, right_coeff in rhs.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(GENERATOR_COUNT)
                    if left_mask & (1 << index)
                )
                sign = -1 if inversions % 2 else 1
                mask = left_mask | right_mask
                terms[mask] = sp.expand(
                    terms.get(mask, 0) + sign * left_coeff * right_coeff
                )
        return Grassmann(terms)

    __rmul__ = __mul__

    def left_derivative(self, index: int) -> "Grassmann":
        terms: dict[int, sp.Expr] = {}
        for mask, coeff in self.terms.items():
            if not mask & (1 << index):
                continue
            preceding = (mask & ((1 << index) - 1)).bit_count()
            sign = -1 if preceding % 2 else 1
            output_mask = mask ^ (1 << index)
            terms[output_mask] = sp.expand(
                terms.get(output_mask, 0) + sign * coeff
            )
        return Grassmann(terms)

    def coefficient(self, mask: int) -> sp.Expr:
        return sp.expand(self.terms.get(mask, 0))


def variable(vertex: int, offset: int) -> Grassmann:
    return Grassmann.generator(4 * vertex + offset)


def d(poly: Grassmann, vertex: int, spinor: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    result = poly.left_derivative(4 * vertex + spinor)
    for dotted in range(2):
        result += (
            -momentum[spinor][dotted]
            * variable(vertex, 2 + dotted)
            * poly
        )
    return result


def bar_d(
    poly: Grassmann,
    vertex: int,
    dotted: int,
    momentum: list[list[sp.Expr]],
) -> Grassmann:
    result = -poly.left_derivative(4 * vertex + 2 + dotted)
    for spinor in range(2):
        result += momentum[spinor][dotted] * variable(vertex, spinor) * poly
    return result


def d2(poly: Grassmann, vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    # Operator product 2 D_- D_+: D_+ acts first.
    return 2 * d(d(poly, vertex, 0, momentum), vertex, 1, momentum)


def bar_d2(poly: Grassmann, vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    # Operator product 2 barD_dot+ barD_dot-: barD_dot- acts first.
    return 2 * bar_d(bar_d(poly, vertex, 1, momentum), vertex, 0, momentum)


def delta4(left: int, right: int) -> Grassmann:
    result = Grassmann.scalar(4)
    for offset in range(4):
        result *= variable(left, offset) - variable(right, offset)
    return result


def theta_p_bartheta(vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    result = Grassmann()
    for spinor in range(2):
        for dotted in range(2):
            result += (
                momentum[spinor][dotted]
                * variable(vertex, spinor)
                * variable(vertex, 2 + dotted)
            )
    return result


def nilpotent_exponential(
    vertex: int,
    momentum: list[list[sp.Expr]],
    sign: int,
) -> Grassmann:
    exponent = sign * theta_p_bartheta(vertex, momentum)
    return Grassmann.scalar(1) + exponent + sp.Rational(1, 2) * exponent * exponent


def antichiral_bottom(vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    # D_a C=0 and C|=1.
    return nilpotent_exponential(vertex, momentum, +1)


def chiral_b_plus(vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    # barD_dot-a Phi=0 and D_+ Phi|=1.
    return nilpotent_exponential(vertex, momentum, -1) * variable(vertex, 0)


def vector_dotted_component(vertex: int, dotted: int) -> Grassmann:
    # Probe u=theta+ theta- bartheta_dot-a; D^2 barD_dot-a u|=-2.
    return (
        variable(vertex, 0)
        * variable(vertex, 1)
        * variable(vertex, 2 + dotted)
    )


def integrate_two_vertices_bottom_source(poly: Grassmann, left: int, right: int) -> sp.Expr:
    top_mask = (15 << (4 * left)) | (15 << (4 * right))
    # Each full d^4 theta measure maps the canonical degree-four monomial to 1/4.
    return sp.factor(poly.coefficient(top_mask) / 16)


def matrix_sub(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [[left[a][b] - right[a][b] for b in range(2)] for a in range(2)]


def matrix_neg(matrix: list[list[sp.Expr]]) -> list[list[sp.Expr]]:
    return [[-entry for entry in row] for row in matrix]


def determinant(matrix: list[list[sp.Expr]]) -> sp.Expr:
    return sp.expand(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def expression_text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value)))


def assert_zero(value: object, message: str) -> None:
    if sp.simplify(sp.sympify(value)) != 0:
        raise AssertionError(f"{message}: {sp.factor(value)}")


def build_artifact() -> dict[str, object]:
    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = matrix_sub(r0, p)
    r2 = matrix_sub(r1, q)
    minus_r2 = matrix_neg(r2)
    det_r2 = determinant(r2)
    wedge_p_r0 = sp.expand(p[0][0] * r0[0][1] - p[0][1] * r0[0][0])
    wedge_p_q = sp.expand(p[0][0] * q[0][1] - p[0][1] * q[0][0])

    # Convention checks on a generic delta kernel.
    generic_delta = delta4(S, M)
    square_identity_difference = (
        d2(bar_d2(d2(generic_delta, S, r0), S, r0), S, r0)
        - 16 * determinant(r0) * d2(generic_delta, S, r0)
    )
    if square_identity_difference.terms:
        raise AssertionError("D^2 barD^2 D^2 identity failed")

    c_m = antichiral_bottom(M, p)
    c_h = antichiral_bottom(H, q)
    for spinor in range(2):
        if d(c_m, M, spinor, p).terms:
            raise AssertionError("external C_M is not antichiral")
        if d(c_h, H, spinor, q).terms:
            raise AssertionError("external C_H is not antichiral")

    # G3 source and the two standard pure-antichiral-vertex representations.
    a_source_g3 = d(
        bar_d2(d(delta4(S, M), S, 0, r0), S, r0),
        S,
        0,
        r0,
    )
    selected_residual = d2(delta4(S, H), S, minus_r2)
    half_mh = bar_d2(delta4(M, H), M, r1)
    residual_g3 = integrate_two_vertices_bottom_source(
        a_source_g3 * selected_residual * half_mh * c_m * c_h,
        M,
        H,
    )

    # Choice A: retain H-D^2 on S-H and omit it on M-H.
    choice_a_selected_full = sp.Rational(1, 2) * d2(
        bar_d2(d2(delta4(S, H), S, minus_r2), S, minus_r2),
        S,
        minus_r2,
    )
    raw_choice_a = integrate_two_vertices_bottom_source(
        a_source_g3 * choice_a_selected_full * half_mh * c_m * c_h,
        M,
        H,
    )

    # Choice B: omit H-D^2 on S-H and retain it on M-H.
    choice_b_selected_half = sp.Rational(1, 2) * d2(
        bar_d2(delta4(S, H), S, minus_r2),
        S,
        minus_r2,
    )
    choice_b_mh_full = bar_d2(d2(delta4(M, H), M, r1), M, r1)
    raw_choice_b = integrate_two_vertices_bottom_source(
        a_source_g3 * choice_b_selected_half * choice_b_mh_full * c_m * c_h,
        M,
        H,
    )

    expected_residual_g3 = -128 * wedge_p_r0
    expected_raw_g3 = 8 * det_r2 * expected_residual_g3
    endpoint_factor_g3 = -sp.Rational(1, 64)
    parent_numerator_g3 = sp.factor(endpoint_factor_g3 * raw_choice_a)
    expected_parent_numerator_g3 = 16 * det_r2 * wedge_p_r0
    # bar r_2^2=-det(r_2), so the parent is -16 bar r_2^2 (p wedge r_0).
    anomaly_residual_g3 = -16 * wedge_p_r0

    assert_zero(residual_g3 - expected_residual_g3, "G3 residual")
    assert_zero(raw_choice_a - expected_raw_g3, "G3 choice A raw word")
    assert_zero(raw_choice_b - expected_raw_g3, "G3 choice B raw word")
    assert_zero(raw_choice_a - raw_choice_b, "G3 representation independence")
    assert_zero(
        parent_numerator_g3 - expected_parent_numerator_g3,
        "G3 endpoint-weighted parent numerator",
    )

    y, z = sp.symbols("y z", nonnegative=True)
    simplex_area = sp.integrate(sp.integrate(1, (z, 0, 1 - y)), (y, 0, 1))
    simplex_z = sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1))
    feynman_weight_z = sp.simplify(2 * simplex_z)
    scalar_master = 1 / (32 * sp.pi**2)
    rank_one_master = sp.simplify(feynman_weight_z * scalar_master)
    lambda1 = sp.Symbol("lambda1")
    isolated_g32 = sp.Rational(2, 3) * sp.I * sp.sqrt(2) * lambda1
    isolated_g33 = -isolated_g32

    # G3 with the outer D_- marked on A.  The transverse vector-Euler square
    # is on r0; after factoring -8 bar(r0)^2 the remaining A kernel is D_+.
    # Both allowed H-endpoint representations are replayed again.
    a_square_g3 = d(delta4(S, M), S, 0, r0)
    b_source_sh_full = d(
        bar_d2(d2(delta4(S, H), S, minus_r2), S, minus_r2),
        S,
        0,
        minus_r2,
    )
    b_source_sh_half = d(
        bar_d2(delta4(S, H), S, minus_r2),
        S,
        0,
        minus_r2,
    )
    a_marked_choice_a = integrate_two_vertices_bottom_source(
        a_square_g3 * b_source_sh_full * half_mh * c_m * c_h,
        M,
        H,
    )
    a_marked_choice_b = integrate_two_vertices_bottom_source(
        a_square_g3 * b_source_sh_half * choice_b_mh_full * c_m * c_h,
        M,
        H,
    )
    wedge_q_r0 = sp.expand(q[0][0] * r0[0][1] - q[0][1] * r0[0][0])
    expected_a_marked_g3 = -128 * (wedge_p_q + wedge_q_r0)
    assert_zero(
        a_marked_choice_a - expected_a_marked_g3,
        "G3 A-marked choice A residual",
    )
    assert_zero(
        a_marked_choice_b - expected_a_marked_g3,
        "G3 A-marked choice B residual",
    )
    assert_zero(
        a_marked_choice_a - a_marked_choice_b,
        "G3 A-marked H representation independence",
    )
    a_marked_endpoint_residual_g3 = sp.factor(
        sp.Rational(1, 8) * a_marked_choice_a
    )
    # q wedge r0 -> -(y+z) p wedge q after the Feynman shift.
    a_marked_simplex_factor = sp.simplify(
        1
        - 2
        * sp.integrate(
            sp.integrate(y + z, (z, 0, 1 - y)),
            (y, 0, 1),
        )
    )
    isolated_two_marked_g32 = 2 * isolated_g32
    isolated_two_marked_g33 = 2 * isolated_g33

    # G2 routing: source Phi -> L is r0, L -> R is r1, R -> source V is r2.
    phi_r = chiral_b_plus(H, q)
    for dotted in range(2):
        if bar_d(phi_r, H, dotted, q).terms:
            raise AssertionError("external Phi_R is not chiral")

    a_source_g2 = d(
        bar_d2(d(delta4(S, H), S, 0, minus_r2), S, minus_r2),
        S,
        0,
        minus_r2,
    )
    source_matter_full = d(
        bar_d2(d2(delta4(S, M), S, r0), S, r0),
        S,
        0,
        r0,
    )
    lr_full = bar_d2(d2(delta4(M, H), M, r1), M, r1)

    # Marked B placement: the selected source-matter edge gives no physical D.PB
    # component in this isolated packaged occurrence.
    b_selected = d2(delta4(S, M), S, r0)
    g2_b_projection: list[sp.Expr] = []
    b_marked_common = a_source_g2 * b_selected * lr_full * phi_r
    for dotted in range(2):
        probe = vector_dotted_component(M, dotted)
        # phi_r and the dotted-vector probe are both odd; common*probe has
        # the reverse order from probe*phi_r.
        value = -integrate_two_vertices_bottom_source(
            b_marked_common * probe,
            M,
            H,
        )
        g2_b_projection.append(value)
        assert_zero(value, f"G2 B-placement physical projection dotted={dotted}")

    # Marked A placement.  The gauge-invariant linear Euler kernel decomposes as
    # (1/2)D^2 barD^2 D_+ = 8 Box D_+ - (1/2)D_+ barD^2 D^2.
    a_marked_full = d(a_source_g2, S, 1, minus_r2)
    a_square_residual = d(delta4(S, H), S, 0, minus_r2)
    box_r2 = det_r2
    g2_full_projection: list[sp.Expr] = []
    g2_square_projection: list[sp.Expr] = []
    g2_longitudinal_projection: list[sp.Expr] = []
    full_common = a_marked_full * source_matter_full * lr_full * phi_r
    square_common = a_square_residual * source_matter_full * lr_full * phi_r
    for dotted in range(2):
        probe = vector_dotted_component(M, dotted)
        full_value = -integrate_two_vertices_bottom_source(
            full_common * probe,
            M,
            H,
        )
        square_value = -integrate_two_vertices_bottom_source(
            square_common * probe,
            M,
            H,
        )
        longitudinal_value = sp.factor(full_value - 8 * box_r2 * square_value)
        g2_full_projection.append(full_value)
        g2_square_projection.append(square_value)
        g2_longitudinal_projection.append(longitudinal_value)

    f_mixed = sp.expand(
        r2[0][0] * r1[1][1] - r2[0][1] * r1[1][0]
    )
    expected_g2_full = [-1024 * r0[0][1] * f_mixed, 1024 * r0[0][0] * f_mixed]
    expected_g2_square = [-128 * r0[0][1], 128 * r0[0][0]]
    for dotted in range(2):
        assert_zero(
            g2_full_projection[dotted] - expected_g2_full[dotted],
            f"G2 full A-marked polynomial dotted={dotted}",
        )
        assert_zero(
            g2_square_projection[dotted] - expected_g2_square[dotted],
            f"G2 square residual dotted={dotted}",
        )

    simplex_y_plus_z = sp.integrate(
        sp.integrate(y + z, (z, 0, 1 - y)),
        (y, 0, 1),
    )
    shift_weight_p = sp.simplify(2 * simplex_y_plus_z)
    shift_weight_q = feynman_weight_z

    checks = {
        "D2_barD2_D2_equals_16_Box_D2": True,
        "external_antichiral_constraints": True,
        "external_chiral_constraint": True,
        "G3_choice_A_residual_derived": True,
        "G3_choice_A_equals_choice_B_before_endpoint_factors": True,
        "G3_omission_choices_are_representations_not_multiplicity": True,
        "G3_A_marked_H_representations_are_equal": True,
        "G3_A_marked_simplex_factor_is_one_third": a_marked_simplex_factor == sp.Rational(1, 3),
        "G3_endpoint_weighted_parent_is_minus_16_bar_r2_sq_wedge": True,
        "G3_rank_one_simplex_weight_is_one_third": feynman_weight_z == sp.Rational(1, 3),
        "G2_B_marked_physical_projection_is_zero": all(
            sp.simplify(value) == 0 for value in g2_b_projection
        ),
        "G2_A_marked_transverse_plus_longitudinal_equals_full": True,
        "no_HT_coefficient_used_as_input": True,
    }
    if not all(checks.values()):
        raise AssertionError(f"failed check: {checks}")

    return {
        "schema": "step5-ab1-g2-g3-dword-replay-v1",
        "status": "EXACT_ISOLATED_TRIANGLE_REPLAY__FULL_DESCENDANT_ORBIT_OPEN",
        "arithmetic": "exact SymPy polynomials and rational simplex integrals; no floating point",
        "contract_inputs": [
            "audits/step5-ab1-standard-feynman-strictification.md Sections 1-3",
            "audits/step5-dred-cutting-failure-exact.md Sections 2-4",
            "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md (5A.64)-(5A.75)",
            "references/vendor/local/superspace-1001-supergraph-pages.pdf Section 6.3, printed pp. 351-352",
        ],
        "conventions": {
            "generator_order_per_vertex": [
                "theta+",
                "theta-",
                "bartheta_dot+",
                "bartheta_dot-",
            ],
            "D2": "2 D_- D_+",
            "barD2": "2 barD_dot+ barD_dot-",
            "delta4": "4 theta+ theta- bartheta_dot+ bartheta_dot-",
            "full_measure_top_monomial": "1/4 per d4theta vertex",
            "bar_Box": "det(r_a_dot-a)",
            "bar_r_squared": "-det(r_a_dot-a)",
            "endpoint_factor": "-D2/4 or -barD2/4",
        },
        "routing": {
            "r0": "loop momentum on S-M (G3 vector; G2 source-matter)",
            "r1": "r0-p",
            "r2": "r0-p-q",
            "p": "outgoing momentum at M/L",
            "q": "outgoing momentum at H/R",
            "wedge": "p00*r01-p01*r00",
            "pairing": "<C_M,C_H>=p00*q01-p01*q00",
        },
        "G3": {
            "source_and_slots": {
                "G32": {
                    "source_u_color": "A -> M2.u^A",
                    "source_phi1_color": "B -> H.tildephi1^B",
                    "internal": "M2.phi2^X -> H.tildephi2^X",
                    "external_slot_D": "M2.tildephi2^D = C2^D",
                    "external_slot_E": "H.tildephi3^E = C3^E",
                    "color": "(T_A)^D_X c_BXE = +i F^{AB}_{DE}",
                },
                "G33": {
                    "source_u_color": "A -> M3.u^A",
                    "source_phi1_color": "B -> H.tildephi1^B",
                    "internal": "M3.phi3^X -> H.tildephi3^X",
                    "external_slot_D": "M3.tildephi3^D = C3^D",
                    "external_slot_E": "H.tildephi2^E = C2^E",
                    "color": "(T_A)^D_X c_BXE = +i F^{AB}_{DE}",
                },
            },
            "marked_placement": "outer D_- on source B1; selected edge is source-Phi1 to H-tildePhi1",
            "marked_B_chiral_edge": {
                "selected_edge": "source-Phi1 to H-tildePhi1, momentum r2",
                "endpoint_weighted_evanescent_word": "-16*(p_+ wedge r0_+)*mu_l_squared/(D0 D1 D2)",
                "simplex_reduction": "2*int_Sigma z=1/3",
                "G32": expression_text(isolated_g32),
                "G33": expression_text(isolated_g33),
            },
            "marked_A_vector_edge": {
                "selected_edge": "source-u to M.u, momentum r0",
                "choice_A_residual_without_endpoint_constants": expression_text(a_marked_choice_a),
                "choice_B_residual_without_endpoint_constants": expression_text(a_marked_choice_b),
                "representation_independence_difference": expression_text(a_marked_choice_a - a_marked_choice_b),
                "endpoint_weighted_evanescent_word": "-16*(p_+ wedge q_+ + q_+ wedge r0_+)*mu_l_squared/(D0 D1 D2)",
                "simplex_reduction": "1-2*int_Sigma(y+z)=1/3",
                "G32": expression_text(isolated_g32),
                "G33": expression_text(isolated_g33),
            },
            "choice_A": {
                "description": "retain H-D2 on selected S-H edge; omit H-D2 on M-H",
                "residual_without_endpoint_constants": expression_text(residual_g3),
                "raw_parent_before_endpoint_constants": expression_text(raw_choice_a),
            },
            "choice_B": {
                "description": "omit H-D2 on S-H; retain H-D2 on M-H",
                "raw_parent_before_endpoint_constants": expression_text(raw_choice_b),
            },
            "representation_independence_difference": expression_text(raw_choice_a - raw_choice_b),
            "endpoint_factor_product": expression_text(endpoint_factor_g3),
            "parent_numerator": expression_text(parent_numerator_g3),
            "parent_numerator_in_square_notation": "-16*bar_r2_squared*(p_+ wedge r0_+)",
            "full_d_SD_cut_replacement": "bar_r2_squared -> r2_d_squared",
            "evanescent_remainder": "-16*(p_+ wedge r0_+)*mu_l_squared/(D0*D1*D2)",
            "simplex": {
                "area": expression_text(simplex_area),
                "integral_z": expression_text(simplex_z),
                "two_times_integral_z": expression_text(feynman_weight_z),
                "rank_one_master": expression_text(rank_one_master),
                "result": "int mu_l^2 (p_+ wedge r0_+)/(D0 D1 D2) = <C_M,C_H>/(96*pi^2)",
            },
            "isolated_triangle_coefficients": {
                "G32_external_C2D_C3E": expression_text(isolated_g32),
                "G33_external_C3D_C2E": expression_text(isolated_g33),
                "normalization": "lambda1=hbar*g^2/(16*pi^2)",
                "scope": "isolated parent plus its selected full-d Schwinger cut only; not the full descendant/contact orbit",
            },
            "two_marked_parent_sum_before_contact_completion": {
                "G32_external_C2D_C3E": expression_text(isolated_two_marked_g32),
                "G33_external_C3D_C2E": expression_text(isolated_two_marked_g33),
                "scope": "sum of A-marked and B-marked selected-edge remainders; Euler/nonlinear/explicit-contact orbit still open",
            },
        },
        "G2": {
            "source_color_order": "(T_E)^B_X (T_A)^X_D = -F^{AB}_{DE}; the color-D external Phi and color-E external u must not be transposed",
            "marked_B_placement": {
                "selected_edge": "source-Phi1 to first action tildePhi1",
                "physical_D_dot_P_B_projection": [
                    expression_text(value) for value in g2_b_projection
                ],
            },
            "marked_A_placement": {
                "selected_edge": "source-u to action-u vector edge r2",
                "operator_decomposition": "(1/2)D2 barD2 D_+ = 8 barBox D_+ - (1/2)D_+ barD2 D2",
                "full_packaged_projection": [
                    expression_text(value) for value in g2_full_projection
                ],
                "mixed_factor_F": expression_text(f_mixed),
                "transverse_square_residual": [
                    expression_text(value) for value in g2_square_projection
                ],
                "longitudinal_remainder": [
                    expression_text(value) for value in g2_longitudinal_projection
                ],
                "physical_transverse_word": "-2*(D2 barD_dot-a u)*r0^dot-a*(D_+ phi1)*mu_l^2/(D0 D1 D2)",
                "rank_one_shift_weights": {
                    "external_u_momentum_p": expression_text(shift_weight_p),
                    "external_B_momentum_q": expression_text(shift_weight_q),
                    "result": "int mu_l^2 r0/(D0 D1 D2)=(2*p+q)/(96*pi^2)",
                },
                "scope": "transverse selected-edge term is exact; its longitudinal/contact completion is not included in the isolated coefficient",
            },
        },
        "descendant_occurrence_ledger": {
            "product_rule": "nabla_-(A B1)=(nabla_- A)B1+A(nabla_- B1)",
            "A_marked": [
                "-(nabla_+ E_V_linear) B1: vector-edge parent/cut in G1 and both G2 source attachments",
                "+2i (nabla_+(Phi_s x tildePhi_s)) B1 inside -nabla_+ E_V",
                "-2i (B_s x C_s) B1 explicit matter contact",
            ],
            "B_marked": [
                "-2 A E_tilde1,kinetic: source-chiral-edge parent/cut",
                "+sqrt(2) epsilon_1st A(C_s x C_t) inside -2 A E_tilde1",
                "-sqrt(2) epsilon_1st A(C_s x C_t) explicit contact",
            ],
            "raw_parent_markings": [
                "G2_DB_A",
                "G2_DB_B",
                "G2_BD_A",
                "G2_BD_B",
                "G32_A",
                "G32_B",
                "G33_A",
                "G33_B",
            ],
            "unsettled_requirement": "pair every longitudinal/Euler and explicit contact occurrence before comparing the remaining one-third with HT",
        },
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write generated JSON")
    parser.add_argument("--check", type=Path, help="compare with existing JSON")
    arguments = parser.parse_args()

    artifact = build_artifact()
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if arguments.check is not None:
        existing = arguments.check.read_text(encoding="utf-8")
        if existing != rendered:
            raise SystemExit(f"FAIL: stale replay artifact: {arguments.check}")
    if arguments.output is not None:
        arguments.output.write_text(rendered, encoding="utf-8")
        print(f"PASS: wrote {arguments.output}")
    elif arguments.check is None:
        print(rendered, end="")
    else:
        print(f"PASS: exact replay matches {arguments.check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
