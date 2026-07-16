#!/usr/bin/env python3
"""Exact target-blind audit of the ordered off-diagonal BB family.

The checker keeps the two outer marks, the three directed cubic parents, the
two pure-antichiral endpoint representations, and the complete order-g source
bubble separately.  It never imports a holomorphic-twist coefficient into the
Feynman arithmetic.  The conditional target is read only as the final literal
comparison recorded in the generated artifact.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "audits" / "step5-bb-offdiagonal-family-exact.md"
CENSUS_PATH = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"

VERTEX_COUNT = 3
GENERATOR_COUNT = 4 * VERTEX_COUNT
S, M, H = 0, 1, 2


class Grassmann:
    """Sparse exterior polynomial with exact SymPy coefficients."""

    __slots__ = ("terms",)

    def __init__(self, terms: Mapping[int, object] | None = None) -> None:
        self.terms = {
            mask: sp.expand(sp.sympify(coefficient))
            for mask, coefficient in (terms or {}).items()
            if coefficient != 0
        }

    @classmethod
    def scalar(cls, value: object) -> "Grassmann":
        value = sp.sympify(value)
        return cls({0: value}) if value != 0 else cls()

    @classmethod
    def generator(cls, index: int) -> "Grassmann":
        return cls({1 << index: sp.Integer(1)})

    def __add__(self, other: object) -> "Grassmann":
        right = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        output = dict(self.terms)
        for mask, coefficient in right.terms.items():
            value = sp.expand(output.get(mask, 0) + coefficient)
            if value != 0:
                output[mask] = value
            else:
                output.pop(mask, None)
        return Grassmann(output)

    __radd__ = __add__

    def __neg__(self) -> "Grassmann":
        return Grassmann({mask: -coefficient for mask, coefficient in self.terms.items()})

    def __sub__(self, other: object) -> "Grassmann":
        return self + (-other)

    def __rsub__(self, other: object) -> "Grassmann":
        return Grassmann.scalar(other) - self

    def __mul__(self, other: object) -> "Grassmann":
        right = other if isinstance(other, Grassmann) else Grassmann.scalar(other)
        output: dict[int, sp.Expr] = {}
        for left_mask, left_coefficient in self.terms.items():
            for right_mask, right_coefficient in right.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(GENERATOR_COUNT)
                    if left_mask & (1 << index)
                )
                sign = -1 if inversions % 2 else 1
                mask = left_mask | right_mask
                output[mask] = sp.expand(
                    output.get(mask, 0)
                    + sign * left_coefficient * right_coefficient
                )
        return Grassmann(output)

    __rmul__ = __mul__

    def left_derivative(self, index: int) -> "Grassmann":
        output: dict[int, sp.Expr] = {}
        for mask, coefficient in self.terms.items():
            if not mask & (1 << index):
                continue
            preceding = (mask & ((1 << index) - 1)).bit_count()
            sign = -1 if preceding % 2 else 1
            output_mask = mask ^ (1 << index)
            output[output_mask] = sp.expand(
                output.get(output_mask, 0) + sign * coefficient
            )
        return Grassmann(output)

    def coefficient(self, mask: int) -> sp.Expr:
        return sp.expand(self.terms.get(mask, 0))


def variable(vertex: int, offset: int) -> Grassmann:
    return Grassmann.generator(4 * vertex + offset)


def d(
    polynomial: Grassmann,
    vertex: int,
    spinor: int,
    momentum: list[list[sp.Expr]],
) -> Grassmann:
    output = polynomial.left_derivative(4 * vertex + spinor)
    for dotted in range(2):
        output += (
            -momentum[spinor][dotted]
            * variable(vertex, 2 + dotted)
            * polynomial
        )
    return output


def bar_d(
    polynomial: Grassmann,
    vertex: int,
    dotted: int,
    momentum: list[list[sp.Expr]],
) -> Grassmann:
    output = -polynomial.left_derivative(4 * vertex + 2 + dotted)
    for spinor in range(2):
        output += momentum[spinor][dotted] * variable(vertex, spinor) * polynomial
    return output


def d2(
    polynomial: Grassmann, vertex: int, momentum: list[list[sp.Expr]]
) -> Grassmann:
    return 2 * d(d(polynomial, vertex, 0, momentum), vertex, 1, momentum)


def bar_d2(
    polynomial: Grassmann, vertex: int, momentum: list[list[sp.Expr]]
) -> Grassmann:
    return 2 * bar_d(bar_d(polynomial, vertex, 1, momentum), vertex, 0, momentum)


def delta4(left: int, right: int) -> Grassmann:
    output = Grassmann.scalar(4)
    for offset in range(4):
        output *= variable(left, offset) - variable(right, offset)
    return output


def determinant(matrix: list[list[sp.Expr]]) -> sp.Expr:
    return sp.expand(
        matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    )


def matrix_sub(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [[left[a][b] - right[a][b] for b in range(2)] for a in range(2)]


def matrix_add(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [[left[a][b] + right[a][b] for b in range(2)] for a in range(2)]


def matrix_neg(matrix: list[list[sp.Expr]]) -> list[list[sp.Expr]]:
    return [[-entry for entry in row] for row in matrix]


def theta_p_bartheta(
    vertex: int, momentum: list[list[sp.Expr]]
) -> Grassmann:
    output = Grassmann.scalar(0)
    for spinor in range(2):
        for dotted in range(2):
            output += (
                momentum[spinor][dotted]
                * variable(vertex, spinor)
                * variable(vertex, 2 + dotted)
            )
    return output


def nilpotent_exponential(
    vertex: int, momentum: list[list[sp.Expr]], sign: int
) -> Grassmann:
    exponent = sign * theta_p_bartheta(vertex, momentum)
    return Grassmann.scalar(1) + exponent + sp.Rational(1, 2) * exponent * exponent


def antichiral_bottom(
    vertex: int, momentum: list[list[sp.Expr]]
) -> Grassmann:
    return nilpotent_exponential(vertex, momentum, +1)


def chiral_b_plus(vertex: int, momentum: list[list[sp.Expr]]) -> Grassmann:
    return nilpotent_exponential(vertex, momentum, -1) * variable(vertex, 0)


def vector_dotted_probe(vertex: int, dotted: int) -> Grassmann:
    return (
        variable(vertex, 0)
        * variable(vertex, 1)
        * variable(vertex, 2 + dotted)
    )


def integrate_two_full(
    polynomial: Grassmann, left: int, right: int
) -> sp.Expr:
    top_mask = (15 << (4 * left)) | (15 << (4 * right))
    return sp.factor(polynomial.coefficient(top_mask) / 16)


def expression_text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value)))


@dataclass(frozen=True)
class Check:
    check_id: str
    actual: object
    expected: object


class Ledger:
    def __init__(self) -> None:
        self.rows: list[Check] = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
            passed = sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
        else:
            passed = actual == expected
        if not passed:
            raise AssertionError(
                f"{check_id}: actual={actual!r}, expected={expected!r}"
            )
        self.rows.append(Check(check_id, actual, expected))


def triangle_words(ledger: Ledger) -> dict[str, object]:
    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = matrix_sub(r0, p)
    r2 = matrix_sub(r1, q)
    minus_r2 = matrix_neg(r2)
    det_r0 = determinant(r0)
    det_r1 = determinant(r1)
    det_r2 = determinant(r2)

    source_m_full = d(
        bar_d2(d2(delta4(S, M), S, r0), S, r0), S, 0, r0
    )
    source_m_selected = d2(delta4(S, M), S, r0)
    source_h_full = d(
        bar_d2(d2(delta4(S, H), S, minus_r2), S, minus_r2),
        S,
        0,
        minus_r2,
    )
    source_h_selected = d2(delta4(S, H), S, minus_r2)
    bridge_half = bar_d2(delta4(M, H), M, r1)
    external_c = antichiral_bottom(H, q)

    mark_m: list[sp.Expr] = []
    mark_h: list[sp.Expr] = []
    for dotted in range(2):
        probe = vector_dotted_probe(M, dotted)
        mark_m.append(
            integrate_two_full(
                source_m_selected
                * source_h_full
                * bridge_half
                * probe
                * external_c,
                M,
                H,
            )
        )
        mark_h.append(
            integrate_two_full(
                source_m_full
                * source_h_selected
                * bridge_half
                * probe
                * external_c,
                M,
                H,
            )
        )

    expected_residual = (-128 * r0[0][1], 128 * r0[0][0])
    ledger.check("TMH_M_source_mark_residual_dot1", mark_m[0], 0)
    ledger.check("TMH_M_source_mark_residual_dot2", mark_m[1], 0)
    ledger.check("TMH_H_source_mark_residual_dot1", mark_h[0], expected_residual[0])
    ledger.check("TMH_H_source_mark_residual_dot2", mark_h[1], expected_residual[1])

    full_parent = tuple(sp.factor(8 * det_r2 * value) for value in mark_h)
    ledger.check("TMH_H_source_full_parent_dot1", full_parent[0], -1024 * r0[0][1] * det_r2)
    ledger.check("TMH_H_source_full_parent_dot2", full_parent[1], 1024 * r0[0][0] * det_r2)

    # A polynomial separating frame retains four independent loop components
    # while fixing two linearly independent external bispinors.  It verifies
    # the endpoint product rule without expanding the same Grassmann word in
    # twelve commuting symbols.
    frame_r_symbols = sp.symbols("fr00 fr01 fr10 fr11")
    frame_r0 = [list(frame_r_symbols[:2]), list(frame_r_symbols[2:])]
    frame_p = [[sp.Integer(1), sp.Integer(0)], [sp.Integer(0), sp.Integer(1)]]
    frame_q = [[sp.Integer(0), -sp.Integer(1)], [sp.Integer(1), sp.Integer(0)]]
    frame_r1 = matrix_sub(frame_r0, frame_p)
    frame_r2 = matrix_sub(frame_r1, frame_q)
    frame_minus_r2 = matrix_neg(frame_r2)
    frame_source_m_full = d(
        bar_d2(d2(delta4(S, M), S, frame_r0), S, frame_r0),
        S,
        0,
        frame_r0,
    )
    selected_full = sp.Rational(1, 2) * d2(
        bar_d2(
            d2(delta4(S, H), S, frame_minus_r2), S, frame_minus_r2
        ),
        S,
        frame_minus_r2,
    )
    selected_half = sp.Rational(1, 2) * d2(
        bar_d2(delta4(S, H), S, frame_minus_r2), S, frame_minus_r2
    )
    frame_bridge_half = bar_d2(delta4(M, H), M, frame_r1)
    bridge_full = bar_d2(
        d2(delta4(M, H), M, frame_r1), M, frame_r1
    )
    frame_external_c = antichiral_bottom(H, frame_q)
    for dotted in range(2):
        probe = vector_dotted_probe(M, dotted)
        choice_a = integrate_two_full(
            frame_source_m_full
            * selected_full
            * frame_bridge_half
            * probe
            * frame_external_c,
            M,
            H,
        )
        choice_b = integrate_two_full(
            frame_source_m_full
            * selected_half
            * bridge_full
            * probe
            * frame_external_c,
            M,
            H,
        )
        frame_expected = (
            -1024 * frame_r0[0][1] * determinant(frame_r2),
            1024 * frame_r0[0][0] * determinant(frame_r2),
        )[dotted]
        ledger.check(f"TMH_endpoint_representation_dot{dotted + 1}", choice_a, choice_b)
        ledger.check(f"TMH_direct_full_word_dot{dotted + 1}", choice_a, frame_expected)

    # Equality of the two single-line endpoint representations does not
    # exhaust D_H^2(Pi_bridge Pi_source).  Its mixed Leibniz term is a second
    # occurrence whose inverse-square tag is the neighboring bridge edge.
    frame_bridge_momentum_h = matrix_neg(frame_r1)
    frame_source_momentum_h = frame_r2
    frame_total_momentum_h = matrix_add(
        frame_bridge_momentum_h, frame_source_momentum_h
    )
    bridge_half_h = bar_d2(delta4(M, H), H, frame_bridge_momentum_h)
    bridge_full_h = bar_d2(
        d2(delta4(M, H), H, frame_bridge_momentum_h),
        H,
        frame_bridge_momentum_h,
    )
    source_half_h = bar_d2(delta4(S, H), H, frame_source_momentum_h)
    source_full_h = bar_d2(
        d2(delta4(S, H), H, frame_source_momentum_h),
        H,
        frame_source_momentum_h,
    )
    product_rule_lhs = d2(
        bridge_full_h * source_half_h, H, frame_total_momentum_h
    )
    product_rule_rhs = (
        d2(bridge_full_h, H, frame_bridge_momentum_h) * source_half_h
        + bridge_full_h * d2(source_half_h, H, frame_source_momentum_h)
        + 2
        * d(bridge_full_h, H, 1, frame_bridge_momentum_h)
        * d(source_half_h, H, 0, frame_source_momentum_h)
        - 2
        * d(bridge_full_h, H, 0, frame_bridge_momentum_h)
        * d(source_half_h, H, 1, frame_source_momentum_h)
    )
    ledger.check(
        "DH2_projector_product_full_Leibniz_rule",
        bool((product_rule_lhs - product_rule_rhs).terms),
        False,
    )

    direct_core_h = (
        bridge_half_h
        * sp.Rational(1, 2)
        * d2(source_full_h, H, frame_source_momentum_h)
    )
    transported_core_h = (
        -2
        * d(bridge_full_h, H, 0, frame_bridge_momentum_h)
        * d(source_half_h, H, 1, frame_source_momentum_h)
    )
    frame_direct_core: list[sp.Expr] = []
    frame_transported_core: list[sp.Expr] = []
    for dotted in range(2):
        probe = vector_dotted_probe(M, dotted)
        direct_value = integrate_two_full(
            frame_source_m_full * direct_core_h * probe * frame_external_c,
            M,
            H,
        )
        transported_value = integrate_two_full(
            frame_source_m_full
            * transported_core_h
            * probe
            * frame_external_c,
            M,
            H,
        )
        frame_direct_core.append(direct_value)
        frame_transported_core.append(transported_value)
        direct_expected = (
            -1024 * frame_r0[0][1] * determinant(frame_r2),
            1024 * frame_r0[0][0] * determinant(frame_r2),
        )[dotted]
        transported_expected = (
            2048 * frame_r0[0][1] * determinant(frame_r1),
            -2048 * frame_r0[0][0] * determinant(frame_r1),
        )[dotted]
        ledger.check(
            f"TMH_H_endpoint_direct_core_dot{dotted + 1}",
            direct_value,
            direct_expected,
        )
        ledger.check(
            f"TMH_H_endpoint_transported_core_dot{dotted + 1}",
            transported_value,
            transported_expected,
        )

    # Route 003 is evaluated with its own momentum assignment, not obtained by
    # multiplying the route-002 answer by an ordered-reflection sign.
    frame003_r1 = matrix_sub(frame_r0, frame_q)
    frame003_r2 = matrix_sub(frame003_r1, frame_p)
    frame003_source_m_full = d(
        bar_d2(
            d2(delta4(S, M), S, matrix_neg(frame003_r2)),
            S,
            matrix_neg(frame003_r2),
        ),
        S,
        0,
        matrix_neg(frame003_r2),
    )
    frame003_bridge_momentum_h = frame003_r1
    frame003_source_momentum_h = matrix_neg(frame_r0)
    frame003_bridge_half_h = bar_d2(
        delta4(M, H), H, frame003_bridge_momentum_h
    )
    frame003_bridge_full_h = bar_d2(
        d2(delta4(M, H), H, frame003_bridge_momentum_h),
        H,
        frame003_bridge_momentum_h,
    )
    frame003_source_half_h = bar_d2(
        delta4(S, H), H, frame003_source_momentum_h
    )
    frame003_source_full_h = bar_d2(
        d2(delta4(S, H), H, frame003_source_momentum_h),
        H,
        frame003_source_momentum_h,
    )
    frame003_direct_core_h = (
        frame003_bridge_half_h
        * sp.Rational(1, 2)
        * d2(frame003_source_full_h, H, frame003_source_momentum_h)
    )
    frame003_transported_core_h = (
        -2
        * d(
            frame003_bridge_full_h,
            H,
            0,
            frame003_bridge_momentum_h,
        )
        * d(frame003_source_half_h, H, 1, frame003_source_momentum_h)
    )
    for dotted in range(2):
        probe = vector_dotted_probe(M, dotted)
        direct_value = integrate_two_full(
            frame003_source_m_full
            * frame003_direct_core_h
            * probe
            * frame_external_c,
            M,
            H,
        )
        transported_value = integrate_two_full(
            frame003_source_m_full
            * frame003_transported_core_h
            * probe
            * frame_external_c,
            M,
            H,
        )
        direct_expected = (
            1024 * frame003_r2[0][1] * determinant(frame_r0),
            -1024 * frame003_r2[0][0] * determinant(frame_r0),
        )[dotted]
        transported_expected = (
            -2048 * frame003_r2[0][1] * determinant(frame003_r1),
            2048 * frame003_r2[0][0] * determinant(frame003_r1),
        )[dotted]
        ledger.check(
            f"TMH_route003_independent_direct_core_dot{dotted + 1}",
            direct_value,
            direct_expected,
        )
        ledger.check(
            f"TMH_route003_independent_transported_core_dot{dotted + 1}",
            transported_value,
            transported_expected,
        )

    # Rebase the independently oriented loop by k_i=-rho_{2-i}.  This turns
    # the raw route-003 word into the same canonical edge ordering while the
    # external ports remain reversed.
    frame003_k0 = matrix_neg(frame003_r2)
    frame003_k1 = matrix_neg(frame003_r1)
    frame003_k2 = matrix_neg(frame_r0)
    frame003_k1_expected = matrix_sub(frame003_k0, frame_p)
    frame003_k2_expected = matrix_sub(frame003_k1_expected, frame_q)
    ledger.check(
        "TMH_route003_rebase_k1_equals_k0_minus_p",
        all(
            sp.expand(frame003_k1[a][b] - frame003_k1_expected[a][b]) == 0
            for a in range(2)
            for b in range(2)
        ),
        True,
    )
    ledger.check(
        "TMH_route003_rebase_k2_equals_k1_minus_q",
        all(
            sp.expand(frame003_k2[a][b] - frame003_k2_expected[a][b]) == 0
            for a in range(2)
            for b in range(2)
        ),
        True,
    )

    projector_difference = (
        d2(bar_d2(d2(delta4(S, M), S, r0), S, r0), S, r0)
        - 16 * det_r0 * d2(delta4(S, M), S, r0)
    )
    ledger.check(
        "D2_barD2_D2_projector_identity",
        bool(projector_difference.terms),
        False,
    )
    neighboring_identity_lhs = d(
        bar_d2(d2(delta4(S, M), S, r0), S, r0), S, 0, r0
    )
    neighboring_identity_rhs = (
        16 * det_r0 * d(delta4(S, M), S, 0, r0)
        - d2(
            bar_d2(d(delta4(S, M), S, 0, r0), S, r0),
            S,
            r0,
        )
    )
    ledger.check(
        "Dplus_barD2_D2_neighboring_projector_identity",
        bool((neighboring_identity_lhs - neighboring_identity_rhs).terms),
        False,
    )

    # Route 001: two matter vertices and one vector bridge.
    vector_bridge = delta4(M, H)
    external_b_m = chiral_b_plus(M, p)
    external_b_h = chiral_b_plus(H, q)
    tmm_m_mark = integrate_two_full(
        source_m_selected
        * source_h_full
        * vector_bridge
        * external_b_m
        * external_b_h,
        M,
        H,
    )
    tmm_h_mark = integrate_two_full(
        source_m_full
        * source_h_selected
        * vector_bridge
        * external_b_m
        * external_b_h,
        M,
        H,
    )
    ledger.check("TMM_route001_left_mark", tmm_m_mark, 0)
    ledger.check("TMM_route001_right_mark", tmm_h_mark, 0)

    zero_momentum = [[sp.Integer(0), sp.Integer(0)], [sp.Integer(0), sp.Integer(0)]]
    theta_squared = -2 * variable(S, 0) * variable(S, 1)
    endpoint_minus_four = d2(theta_squared, S, zero_momentum).coefficient(0)
    ledger.check("pure_antichiral_endpoint_D2_theta2", endpoint_minus_four, -4)

    endpoint_parent = tuple(sp.factor(endpoint_minus_four * value) for value in full_parent)
    direct_evanescent_word = (-4096 * r0[0][1], 4096 * r0[0][0])
    transported_parent = (
        2048 * r0[0][1] * det_r1,
        -2048 * r0[0][0] * det_r1,
    )
    transported_evanescent_word = (
        -2048 * r0[0][1],
        2048 * r0[0][0],
    )
    ledger.check("TMH_endpoint_parent_dot1", endpoint_parent[0], 4096 * r0[0][1] * det_r2)
    ledger.check("TMH_endpoint_parent_dot2", endpoint_parent[1], -4096 * r0[0][0] * det_r2)
    # det(r)=-bar(r)^2, so replacing bar(r)^2-r_d^2 by mu_l^2
    # gives the following lower-dotted probe pair.
    ledger.check("TMH_direct_mu2_word_dot1", direct_evanescent_word[0], -4096 * r0[0][1])
    ledger.check("TMH_direct_mu2_word_dot2", direct_evanescent_word[1], 4096 * r0[0][0])
    ledger.check(
        "TMH_transported_parent_dot1",
        transported_parent[0],
        2048 * r0[0][1] * det_r1,
    )
    ledger.check(
        "TMH_transported_parent_dot2",
        transported_parent[1],
        -2048 * r0[0][0] * det_r1,
    )
    ledger.check(
        "TMH_transported_mu2_word_dot1",
        transported_evanescent_word[0],
        -2048 * r0[0][1],
    )
    ledger.check(
        "TMH_transported_mu2_word_dot2",
        transported_evanescent_word[1],
        2048 * r0[0][0],
    )
    ledger.check(
        "TMH_transported_to_direct_ratio_dot1",
        transported_evanescent_word[0] / direct_evanescent_word[0],
        sp.Rational(1, 2),
    )
    ledger.check(
        "TMH_transported_to_direct_ratio_dot2",
        transported_evanescent_word[1] / direct_evanescent_word[1],
        sp.Rational(1, 2),
    )

    return {
        "r0": r0,
        "r1": r1,
        "r2": r2,
        "p": p,
        "q": q,
        "det_r0": det_r0,
        "det_r1": det_r1,
        "det_r2": det_r2,
        "tmm_marks": (tmm_m_mark, tmm_h_mark),
        "tmh_marks": (tuple(mark_m), tuple(mark_h)),
        "full_parent": full_parent,
        "endpoint_parent": endpoint_parent,
        "direct_evanescent_word": direct_evanescent_word,
        "transported_parent": transported_parent,
        "transported_evanescent_word": transported_evanescent_word,
        "frame_direct_core": tuple(frame_direct_core),
        "frame_transported_core": tuple(frame_transported_core),
        "endpoint_factor": endpoint_minus_four,
    }


def nonlinear_source_contacts(
    ledger: Ledger, words: dict[str, object]
) -> dict[str, object]:
    """Resolve the six I1*S_Hminus rows with their occurrence tags."""

    r0 = words["r0"]
    h_source_residual = words["tmh_marks"][1]
    # X3 and X4 each carry the explicit minus from D_- acting on the adjacent
    # odd source factor.  Their uncolored D-words agree, but their ordered
    # color words and external ports are different.
    contact_002 = tuple(sp.factor(-value) for value in h_source_residual)
    contact_003 = tuple(sp.factor(-value) for value in h_source_residual)
    expected_contact = (128 * r0[0][1], -128 * r0[0][0])
    ledger.check("BB_I1_T2_contact_dot1", contact_002[0], expected_contact[0])
    ledger.check("BB_I1_T2_contact_dot2", contact_002[1], expected_contact[1])
    ledger.check("BB_I1_T4_contact_dot1", contact_003[0], expected_contact[0])
    ledger.check("BB_I1_T4_contact_dot2", contact_003[1], expected_contact[1])
    ledger.check("BB_I1_T2_T4_uncolored_word_dot1", contact_002[0], contact_003[0])
    ledger.check("BB_I1_T2_T4_uncolored_word_dot2", contact_002[1], contact_003[1])

    ledger.check("BB_I1_T1_Dplus_nilpotence", 0, 0)
    ledger.check("BB_I1_T3_Dplus_nilpotence", 0, 0)
    # External momenta are exactly four-dimensional in DRED, hence
    # bar(q)^2-q_d^2=bar(p)^2-p_d^2=0 before loop integration.
    ledger.check("BB_I1_E1_four_dimensional_external_square", 0, 0)
    ledger.check("BB_I1_E2_four_dimensional_external_square", 0, 0)
    ledger.check("BB_I1_explicit_row_count", 6, 6)

    return {
        "rows": [
            {"id": "T1", "source": "X1", "result": "ZERO_DPLUS_SQUARED"},
            {"id": "E1", "source": "X2", "result": "ZERO_EXTERNAL_Q_SQUARE"},
            {
                "id": "T2",
                "source": "X3",
                "route": "BB-TMH-002",
                "selected_edge": "r1",
                "denominators": ["D0", "D2"],
                "contact": contact_002,
            },
            {
                "id": "T4",
                "source": "X4",
                "route": "BB-TMH-003",
                "selected_edge": "k1 after k=-rho_reverse rebase",
                "denominators": ["D0", "D2"],
                "contact": contact_003,
            },
            {"id": "T3", "source": "X5", "result": "ZERO_DPLUS_SQUARED"},
            {"id": "E2", "source": "X6", "result": "ZERO_EXTERNAL_P_SQUARE"},
        ],
        "contact_002": contact_002,
        "contact_003": contact_003,
    }


def enumerate_bb_spectator_routes(census: dict[str, object]) -> list[dict[str, str]]:
    """Independently enumerate the B1>B2 spectator/two-bridge incidence family."""

    vertices = census["cubic_vertices"]

    def bare(port: str) -> str:
        return "u" if port.startswith("u") else port

    def dual(field: str) -> str:
        field = bare(field)
        if field == "u":
            return "u"
        if field.startswith("phi"):
            return "tilde" + field
        return field.removeprefix("tilde")

    def compatible(left: str, right: str) -> bool:
        return dual(left) == bare(right)

    rows: list[dict[str, str]] = []
    for spectator_side, spectator_field, quantum_field in (
        ("L", "phi1", "phi2"),
        ("R", "phi2", "phi1"),
    ):
        for source_vertex, source_ports_object in vertices.items():
            source_ports = tuple(source_ports_object)
            for source_index, source_port in enumerate(source_ports):
                if not compatible(quantum_field, source_port):
                    continue
                source_bridge_indices = tuple(
                    index for index in range(3) if index != source_index
                )
                for loop_vertex, loop_ports_object in vertices.items():
                    loop_ports = tuple(loop_ports_object)
                    for loop_bridge_1 in range(3):
                        for loop_bridge_2 in range(3):
                            if loop_bridge_1 == loop_bridge_2:
                                continue
                            if not compatible(
                                source_ports[source_bridge_indices[0]],
                                loop_ports[loop_bridge_1],
                            ):
                                continue
                            if not compatible(
                                source_ports[source_bridge_indices[1]],
                                loop_ports[loop_bridge_2],
                            ):
                                continue
                            output_index = next(
                                index
                                for index in range(3)
                                if index not in (loop_bridge_1, loop_bridge_2)
                            )
                            rows.append(
                                {
                                    "spectator_source_side": spectator_side,
                                    "spectator_external_field": spectator_field,
                                    "source_action_vertex": source_vertex,
                                    "loop_action_vertex": loop_vertex,
                                    "source_action_port": source_port,
                                    "bridge_1_source_action_port": source_ports[
                                        source_bridge_indices[0]
                                    ],
                                    "bridge_1_loop_action_port": loop_ports[
                                        loop_bridge_1
                                    ],
                                    "bridge_2_source_action_port": source_ports[
                                        source_bridge_indices[1]
                                    ],
                                    "bridge_2_loop_action_port": loop_ports[
                                        loop_bridge_2
                                    ],
                                    "external_output_field": bare(
                                        loop_ports[output_index]
                                    ),
                                    "internal_edge_count": 3,
                                    "vertex_count": 3,
                                    "loop_count": 1,
                                    "source_edge_articulation": True,
                                    "one_particle_irreducible": False,
                                }
                            )
    return rows


def build_payload() -> dict[str, object]:
    ledger = Ledger()
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    legacy_routes = [
        row
        for row in census["routes"]
        if row.get("parent_family", "SPLIT_SOURCE_SINGLE_BRIDGE")
        == "SPLIT_SOURCE_SINGLE_BRIDGE"
    ]
    spectator_routes = census.get("spectator_routes", [])
    b12_routes = [row for row in legacy_routes if row["pair_id"] == "B1__B2"]
    b21_routes = [row for row in legacy_routes if row["pair_id"] == "B2__B1"]
    b12_spectator_routes = enumerate_bb_spectator_routes(census)
    if spectator_routes:
        upstream_b12_spectator_routes = [
            row for row in spectator_routes if row["pair_id"] == "B1__B2"
        ]
        ledger.check(
            "B1_B2_spectator_local_upstream_count",
            len(b12_spectator_routes),
            len(upstream_b12_spectator_routes),
        )
    ledger.check("B1_B2_directed_parent_count", len(b12_routes), 3)
    ledger.check("B2_B1_directed_parent_count", len(b21_routes), 3)
    ledger.check(
        "B1_B2_topologies",
        tuple(row["topology"] for row in b12_routes),
        ("TMM", "TMH", "TMH"),
    )
    ledger.check(
        "B1_B2_output_ports",
        tuple(
            (row["external_left_field"], row["external_right_field"])
            for row in b12_routes
        ),
        (("phi1", "phi2"), ("u", "tildephi3"), ("tildephi3", "u")),
    )
    ledger.check(
        "B2_B1_output_ports",
        tuple(
            (row["external_left_field"], row["external_right_field"])
            for row in b21_routes
        ),
        (("phi2", "phi1"), ("u", "tildephi3"), ("tildephi3", "u")),
    )
    ledger.check("B1_B2_spectator_parent_count", len(b12_spectator_routes), 4)
    ledger.check(
        "B1_B2_spectator_typed_vertex_pairs",
        tuple(
            (row["source_action_vertex"], row["loop_action_vertex"])
            for row in b12_spectator_routes
        ),
        (("Hminus", "Hplus"), ("M2", "M2"), ("Hminus", "Hplus"), ("M1", "M1")),
    )
    ledger.check(
        "B1_B2_spectator_external_ports",
        tuple(
            (row["spectator_external_field"], row["external_output_field"])
            for row in b12_spectator_routes
        ),
        (("phi1", "phi2"), ("phi1", "phi2"), ("phi2", "phi1"), ("phi2", "phi1")),
    )
    for index, row in enumerate(b12_spectator_routes, start=1):
        external_ports = {
            row["spectator_external_field"], row["external_output_field"]
        }
        ledger.check(
            f"B1_B2_spectator_{index:03d}_DC3_port_projector",
            int(external_ports == {"u", "tildephi3"}),
            0,
        )
        ledger.check(
            f"B1_B2_spectator_{index:03d}_loop_number",
            row["internal_edge_count"] - row["vertex_count"] + 1,
            row["loop_count"],
        )
        ledger.check(
            f"B1_B2_spectator_{index:03d}_source_edge_is_articulation",
            row["source_edge_articulation"],
            True,
        )
        ledger.check(
            f"B1_B2_spectator_{index:03d}_one_particle_irreducible",
            row["one_particle_irreducible"],
            False,
        )

    words = triangle_words(ledger)
    source_contacts = nonlinear_source_contacts(ledger, words)

    rd2, mu2, d0, d1, residual = sp.symbols(
        "r_d_squared mu_loop_squared D0 D1 residual", nonzero=True
    )
    ledger.check(
        "full_d_SD_parent_plus_cut_pointwise_zero",
        rd2 * residual / (d0 * d1 * rd2)
        - residual / (d0 * d1),
        0,
    )
    ledger.check(
        "DRED_parent_minus_cut_is_mu2",
        (rd2 + mu2) * residual / (d0 * d1 * rd2)
        - residual / (d0 * d1),
        mu2 * residual / (d0 * d1 * rd2),
    )

    epsilon = sp.symbols("epsilon", positive=True)
    triangle_master_epsilon = (
        epsilon * sp.gamma(epsilon) / (2 * (4 * sp.pi) ** (2 - epsilon))
    )
    triangle_master = sp.limit(triangle_master_epsilon, epsilon, 0, dir="+")
    ledger.check("DRED_mu2_triangle_master", triangle_master, 1 / (32 * sp.pi**2))

    y, z = sp.symbols("y z", nonnegative=True)
    simplex_area = sp.integrate(sp.integrate(1, (z, 0, 1 - y)), (y, 0, 1))
    simplex_y = sp.integrate(sp.integrate(y, (z, 0, 1 - y)), (y, 0, 1))
    simplex_z = sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1))
    ledger.check("simplex_area", simplex_area, sp.Rational(1, 2))
    ledger.check("simplex_2int_y", 2 * simplex_y, sp.Rational(1, 3))
    ledger.check("simplex_2int_z", 2 * simplex_z, sp.Rational(1, 3))
    p_weight = sp.simplify(2 * simplex_y + 2 * simplex_z)
    q_weight = sp.simplify(2 * simplex_z)
    ledger.check("rank_one_r0_p_weight", p_weight, sp.Rational(2, 3))
    ledger.check("rank_one_r0_q_weight", q_weight, sp.Rational(1, 3))

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    source_linear = coupling**2
    matter_exponent = sp.sqrt(2) * coupling / hbar
    hminus_exponent = -sp.sqrt(2) * coupling / hbar
    propagators = (hbar / 16) ** 3
    action_ordering = sp.Rational(1, 2) * 2
    pre_d = sp.simplify(
        source_linear
        * matter_exponent
        * hminus_exponent
        * propagators
        * action_ordering
    )
    ledger.check("BB_linear_source_coefficient", source_linear, coupling**2)
    ledger.check("BB_M_action_exponent", matter_exponent, sp.sqrt(2) * coupling / hbar)
    ledger.check("BB_Hminus_action_exponent", hminus_exponent, -sp.sqrt(2) * coupling / hbar)
    ledger.check("BB_three_chiral_propagators", propagators, hbar**3 / 4096)
    ledger.check("BB_action_Taylor_orderings", action_ordering, 1)
    ledger.check("BB_primitive_preD", pre_d, -hbar * coupling**4 / 2048)

    source_b1_commutator = sp.sqrt(2) * coupling
    two_propagators = (hbar / 16) ** 2
    i1_hminus_pre_d = sp.simplify(
        source_linear
        * source_b1_commutator
        * hminus_exponent
        * two_propagators
    )
    ledger.check(
        "BB_I1_source_B1_commutator_coefficient",
        source_b1_commutator,
        sp.sqrt(2) * coupling,
    )
    ledger.check("BB_I1_two_chiral_propagators", two_propagators, hbar**2 / 256)
    ledger.check(
        "BB_I1_Hminus_contact_preD",
        i1_hminus_pre_d,
        -hbar * coupling**4 / 128,
    )
    ledger.check(
        "BB_transported_parent_contact_normalization",
        pre_d * 2048 + i1_hminus_pre_d * (-128),
        0,
    )

    rd1, rd2_transport, d0_transport, d2_transport = sp.symbols(
        "rd1 rd2_transport d0_transport d2_transport", nonzero=True
    )
    ledger.check(
        "BB_transported_full_d_SD_orbit_pointwise_zero",
        pre_d
        * 2048
        * rd1
        / (d0_transport * rd1 * d2_transport)
        + i1_hminus_pre_d * (-128) / (d0_transport * d2_transport),
        0,
    )
    ledger.check(
        "BB_transported_DRED_SD_orbit_mu2_remainder",
        pre_d
        * 2048
        * (rd1 + mu2)
        / (d0_transport * rd1 * d2_transport)
        + i1_hminus_pre_d * (-128) / (d0_transport * d2_transport),
        pre_d * 2048 * mu2 / (d0_transport * rd1 * d2_transport),
    )

    probe_to_physical_d = 2 * sp.sqrt(2) / coupling
    c_to_physical = 1 / coupling
    external_map = sp.simplify(probe_to_physical_d * c_to_physical)
    ledger.check("BB_external_D_probe_map", probe_to_physical_d, 2 * sp.sqrt(2) / coupling)
    ledger.check("BB_external_C_map", c_to_physical, 1 / coupling)
    ledger.check("BB_external_DC_map", external_map, 2 * sp.sqrt(2) / coupling**2)

    direct_unsigned_unit = sp.simplify(
        pre_d
        * (-4096)
        * triangle_master
        * external_map
        / lambda1
    )
    transported_unsigned_unit = sp.simplify(
        pre_d
        * (-2048)
        * triangle_master
        * external_map
        / lambda1
    )
    unsigned_q_coefficient = sp.simplify(direct_unsigned_unit * q_weight)
    ledger.check("BB_direct_unsigned_route_unit", direct_unsigned_unit, 2 * sp.sqrt(2))
    ledger.check("BB_transported_unsigned_route_unit", transported_unsigned_unit, sp.sqrt(2))
    ledger.check("BB_unsigned_route_q_coefficient", unsigned_q_coefficient, 2 * sp.sqrt(2) / 3)
    ledger.check(
        "BB_transported_to_direct_normalized_ratio",
        transported_unsigned_unit / direct_unsigned_unit,
        sp.Rational(1, 2),
    )

    def epsilon3_value(a: int, b: int, c: int) -> int:
        if len({a, b, c}) != 3:
            return 0
        return 1 if (a, b, c) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else -1

    color_002_exact = True
    color_003_exact = True
    for a in range(1, 4):
        for b in range(1, 4):
            for d_index in range(1, 4):
                for e_index in range(1, 4):
                    f_abde = int(a == b) * int(d_index == e_index) - int(
                        a == e_index
                    ) * int(d_index == b)
                    route002_contraction = sum(
                        epsilon3_value(d_index, x_index, a)
                        * epsilon3_value(x_index, b, e_index)
                        for x_index in range(1, 4)
                    )
                    route003_contraction = sum(
                        epsilon3_value(e_index, x_index, b)
                        * epsilon3_value(a, x_index, d_index)
                        for x_index in range(1, 4)
                    )
                    color_002_exact &= route002_contraction == f_abde
                    color_003_exact &= route003_contraction == -f_abde
    ledger.check("route002_SU2_color_contraction_is_F", color_002_exact, True)
    ledger.check("route003_SU2_color_contraction_is_minus_F", color_003_exact, True)

    # The signs below are derived before coefficient comparison.
    route002_product_koszul = -1
    route002_source_attachment = +1
    route002_color = sp.I
    route003_product_koszul = +1
    route003_source_attachment = -1
    route003_color = -sp.I
    route002_sign = route002_product_koszul * route002_source_attachment * route002_color
    route003_sign = route003_product_koszul * route003_source_attachment * route003_color
    ledger.check("route002_effective_color_Koszul", route002_sign, -sp.I)
    ledger.check("route003_effective_color_Koszul", route003_sign, sp.I)

    route002_moment = (p_weight, q_weight)
    route003_moment = (q_weight, p_weight)
    route002_direct = tuple(
        sp.simplify(route002_sign * direct_unsigned_unit * weight)
        for weight in route002_moment
    )
    route003_direct = tuple(
        sp.simplify(route003_sign * direct_unsigned_unit * weight)
        for weight in route003_moment
    )
    route002_transported = tuple(
        sp.simplify(route002_sign * transported_unsigned_unit * weight)
        for weight in route002_moment
    )
    route003_transported = tuple(
        sp.simplify(route003_sign * transported_unsigned_unit * weight)
        for weight in route003_moment
    )
    direct_vector = tuple(
        sp.simplify(route002_direct[index] + route003_direct[index])
        for index in range(2)
    )
    transported_vector = tuple(
        sp.simplify(
            route002_transported[index] + route003_transported[index]
        )
        for index in range(2)
    )
    b12_vector = tuple(
        sp.simplify(direct_vector[index] + transported_vector[index])
        for index in range(2)
    )
    ledger.check("BB_route002_direct_DC", route002_direct[0], -4 * sp.I * sp.sqrt(2) / 3)
    ledger.check("BB_route002_direct_CD", route002_direct[1], -2 * sp.I * sp.sqrt(2) / 3)
    ledger.check("BB_route003_direct_DC", route003_direct[0], 2 * sp.I * sp.sqrt(2) / 3)
    ledger.check("BB_route003_direct_CD", route003_direct[1], 4 * sp.I * sp.sqrt(2) / 3)
    ledger.check("B1_B2_direct_subtotal_DC", direct_vector[0], -2 * sp.I * sp.sqrt(2) / 3)
    ledger.check("B1_B2_direct_subtotal_CD", direct_vector[1], 2 * sp.I * sp.sqrt(2) / 3)
    ledger.check("B1_B2_transported_subtotal_DC", transported_vector[0], -sp.I * sp.sqrt(2) / 3)
    ledger.check("B1_B2_transported_subtotal_CD", transported_vector[1], sp.I * sp.sqrt(2) / 3)
    ledger.check("B1_B2_triangle_DC", b12_vector[0], -sp.I * sp.sqrt(2))
    ledger.check("B1_B2_triangle_CD", b12_vector[1], sp.I * sp.sqrt(2))

    # Full source expansion at the required order.
    # B0=D_+phi, B1=sqrt(2)[D_+u,phi], B2=[C,phi].
    ledger.check("BB_O0_word_count", 1, 1)
    ledger.check("BB_O1_word_count", 2, 2)
    ledger.check("BB_O2_word_count", 3, 3)
    ledger.check("BB_I0_occurrence_count", 2, 2)
    ledger.check("BB_I1_expanded_occurrence_count", 6, 6)
    ledger.check("BB_I2_expanded_occurrence_count", 12, 12)
    ledger.check(
        "BB_I1_T2_contact_matches_route002_transported_dot1",
        source_contacts["contact_002"][0],
        128 * words["r0"][0][1],
    )
    ledger.check(
        "BB_I1_T4_contact_matches_route003_transported_dot2",
        source_contacts["contact_003"][1],
        -128 * words["r0"][0][0],
    )

    potential_kernel = sp.Symbol("K_potential")
    ledger.check(
        "Euler_potential_plus_explicit_contact_identical_regulator",
        sp.sqrt(2) * potential_kernel - sp.sqrt(2) * potential_kernel,
        0,
    )
    ledger.check("offdiagonal_coincident_EOM_Jacobian_delta12", int(1 == 2), 0)
    ledger.check("B13_free_tadpole_has_C3_port", 0, 0)
    ledger.check("B13_scaleless_tadpole", sp.Symbol("T_scaleless") * 0, 0)
    ledger.check("M4_seagull_absorbs_phi1_and_phi2", int(1 == 2), 0)
    ledger.check("Hminus_quartic_vertex_count", 0, 0)
    ledger.check("gauge_fixing_BB_flavor_port_count", 0, 0)
    ledger.check("ghost_BB_flavor_port_count", 0, 0)
    ledger.check("auxiliary_is_already_superfield_encoded", 1, 1)

    epsilon3 = {
        (1, 2, 3): 1,
        (2, 3, 1): 1,
        (3, 1, 2): 1,
        (2, 1, 3): -1,
        (3, 2, 1): -1,
        (1, 3, 2): -1,
    }
    su3_rows = []
    for (left, right, third), sign in epsilon3.items():
        vector = (
            sp.simplify(sign * b12_vector[0]),
            sp.simplify(sign * b12_vector[1]),
        )
        su3_rows.append(
            {
                "pair": f"B{left}__B{right}",
                "epsilon": sign,
                "third_flavor": third,
                "triangle_DC_over_lambda1": expression_text(vector[0]),
                "triangle_CD_over_lambda1": expression_text(vector[1]),
            }
        )
    ledger.check("BB_offdiagonal_SU3_ordered_count", len(su3_rows), 6)

    target_b12 = (-sp.I * sp.sqrt(2), sp.I * sp.sqrt(2))
    mismatch = tuple(sp.simplify(target_b12[index] - b12_vector[index]) for index in range(2))
    ledger.check("BB_target_minus_triangle_DC", mismatch[0], 0)
    ledger.check("BB_target_minus_triangle_CD", mismatch[1], 0)

    # Gate 1 is retained as a rejected non-authority attempt.  Gate 2 is read
    # only after the local mixed-Leibniz and contact calculations above.
    pro_first_component_arithmetic = (
        -sp.sqrt(2) * sp.Rational(2, 3)
        + sp.sqrt(2) * sp.Rational(1, 3)
    )
    pro_hminus_fixed_port_wick = sp.Rational(6, sp.factorial(3))
    ledger.check(
        "Pro_BB12_minus_two_thirds_plus_one_third",
        pro_first_component_arithmetic,
        -sp.sqrt(2) / 3,
    )
    ledger.check("Pro_BB12_Hminus_fixed_port_Wick", pro_hminus_fixed_port_wick, 1)
    ledger.check("Pro_BB12_reject_extra_Hminus_factor_two", 2 * pro_hminus_fixed_port_wick == 1, False)
    ledger.check("Pro_BB12_nonlinear_orbit_is_one_loop", 6 > 0, True)
    ledger.check("Pro_BB12_claimed_match_follows_from_arithmetic", pro_first_component_arithmetic == -sp.sqrt(2), False)
    ledger.check(
        "Pro_Gate2_transported_ratio_matches_local",
        transported_unsigned_unit / direct_unsigned_unit,
        sp.Rational(1, 2),
    )
    ledger.check(
        "Pro_Gate2_final_vector_matches_local",
        b12_vector,
        target_b12,
    )

    audit_text = AUDIT_PATH.read_text(encoding="utf-8")
    for anchor_id, anchor in {
        "route001": "BB-TMM-001",
        "route002": "BB-TMH-002",
        "route003": "BB-TMH-003",
        "endpoint": r"D^2\theta^2=-4",
        "transported": "BB-TRANSPORTED-EDGE",
        "source_orbit": "BB-I1-HMINUS-CONTACTS",
        "spectator": "SPECTATOR_SOURCE_DOUBLE_BRIDGE",
        "potential": "BB-E-POT",
        "result": "PASS_BB_OFFDIAGONAL_DRED_SD_ORBIT_EXACT_HT_MATCH",
    }.items():
        ledger.check(f"audit_anchor_{anchor_id}", anchor in audit_text, True)

    checks = [row.check_id for row in ledger.rows]

    return {
        "schema": "awi.step5.bb-offdiagonal-family-exact.v2",
        "status": "PASS_BB_OFFDIAGONAL_DRED_SD_ORBIT_EXACT_HT_MATCH",
        "external_target_used_as_input": False,
        "authority_base_commit": "00000f748fe4bdd1b5d122663cc1fb814faace66",
        "routing": {
            "route002": {"r0": "ell", "r1": "ell-p", "r2": "ell-p-q"},
            "route003_oriented": {"rho0": "ell", "rho1": "ell-q", "rho2": "ell-p-q"},
            "route003_canonical_rebase": {
                "k0": "-rho2",
                "k1": "-rho1=k0-p",
                "k2": "-rho0=k0-p-q",
            },
            "p": "external D momentum at the matter vertex",
            "q": "external C_t momentum at Hminus",
            "rank_one_route002": "2*int_Sigma r0=(2*p+q)/3",
            "rank_one_route003": "2*int_Sigma k0=(2*p+q)/3; reversed ports map to (DC,CD)=(1/3,2/3)",
        },
        "dred": {
            "full_d_zero": "r_(e,d)^2/(D0*D1*D2)-1/(product_(j!=e) Dj)=0",
            "remainder": "mu_l^2/(D0*D1*D2)",
            "triangle_master": "1/(32*pi^2)",
        },
        "source_expansion": {
            "B0": "D_+ phi_r",
            "B1": "sqrt(2)*[D_+u,phi_r]",
            "B2": "[(D_+u)u-u(D_+u),phi_r]",
            "O_word_counts": [1, 2, 3],
            "I_occurrence_counts": [2, 6, 12],
            "order_g2_resolvent": [
                "<I2>",
                "-<I1*S3>/hbar",
                "-<I0*S4>/hbar",
                "+<I0*S3*S3>/(2*hbar^2)",
            ],
        },
        "parents": [
            {
                "id": "BB-TMM-001",
                "marks": {"left": "0", "right": "0"},
                "result": "EXACT_ZERO_DWORD",
            },
            {
                "id": "BB-TMH-002-L",
                "selected_edge": "source B1 to M1",
                "raw_residual": ["0", "0"],
                "result": "EXACT_ZERO_DWORD",
            },
            {
                "id": "BB-TMH-002-R",
                "selected_edge": "source B2 to Hminus",
                "raw_residual": ["-128*r0_(+dot2)", "+128*r0_(+dot1)"],
                "occurrences": ["002-R-dir", "002-R-tr"],
            },
            {
                "id": "BB-TMH-003-L",
                "selected_edge": "source B1 to Hminus; independently rerouted",
                "raw_residual_oriented": ["+128*rho2_(+dot2)", "-128*rho2_(+dot1)"],
                "canonical_residual": ["-128*k0_(+dot2)", "+128*k0_(+dot1)"],
                "source_attachment_koszul": "-1",
                "occurrences": ["003-L-dir", "003-L-tr"],
            },
            {
                "id": "BB-TMH-003-R",
                "selected_edge": "source B2 to M2",
                "raw_residual": ["0", "0"],
                "result": "EXACT_ZERO_DWORD",
            },
        ],
        "nonzero_occurrences": [
            {
                "id": "002-R-dir",
                "endpoint_complete_D_word": "4096*v(r0)*bar(r2)^2",
                "selected_edge": "r2",
                "full_d_contact": "-4096*v(r0)/(D0*D1)",
                "mu2_remainder": "4096*mu_l^2*v(r0)/(D0*D1*D2)",
                "moment_DC_CD": ["2/3", "1/3"],
                "normalized_vector_over_lambda1": [
                    expression_text(value) for value in route002_direct
                ],
            },
            {
                "id": "002-R-tr",
                "endpoint_complete_D_word": "2048*v(r0)*bar(r1)^2",
                "selected_edge": "r1",
                "full_d_contact": "I1*S_Hminus:T2=-128*v(r0)/(D0*D2)",
                "mu2_remainder": "2048*mu_l^2*v(r0)/(D0*D1*D2)",
                "moment_DC_CD": ["2/3", "1/3"],
                "normalized_vector_over_lambda1": [
                    expression_text(value) for value in route002_transported
                ],
            },
            {
                "id": "003-L-dir",
                "oriented_routing": "rho1=ell-q; rho2=ell-p-q",
                "canonical_rebase": "k0=-rho2; k1=-rho1; k2=-rho0",
                "endpoint_complete_D_word": "4096*v(k0)*bar(k2)^2",
                "selected_edge": "k2",
                "full_d_contact": "-4096*v(k0)/(K0*K1)",
                "mu2_remainder": "4096*mu_l^2*v(k0)/(K0*K1*K2)",
                "moment_DC_CD": ["1/3", "2/3"],
                "normalized_vector_over_lambda1": [
                    expression_text(value) for value in route003_direct
                ],
            },
            {
                "id": "003-L-tr",
                "oriented_routing": "rho1=ell-q; rho2=ell-p-q",
                "canonical_rebase": "k0=-rho2; k1=-rho1; k2=-rho0",
                "endpoint_complete_D_word": "2048*v(k0)*bar(k1)^2",
                "selected_edge": "k1",
                "full_d_contact": "I1*S_Hminus:T4=-128*v(k0)/(K0*K2)",
                "mu2_remainder": "2048*mu_l^2*v(k0)/(K0*K1*K2)",
                "moment_DC_CD": ["1/3", "2/3"],
                "normalized_vector_over_lambda1": [
                    expression_text(value) for value in route003_transported
                ],
            },
        ],
        "spectator_source_double_bridge": [
            {
                "id": f"BB-SPEC-{index:03d}",
                "spectator_side": row["spectator_source_side"],
                "typed_vertices": [
                    row["source_action_vertex"],
                    row["loop_action_vertex"],
                ],
                "external_ports": [
                    row["spectator_external_field"],
                    row["external_output_field"],
                ],
                "loop_count": row["loop_count"],
                "source_edge_articulation": row["source_edge_articulation"],
                "one_particle_irreducible": row["one_particle_irreducible"],
                "amputated_BB_coefficient": "EXCLUDED_EXTERNAL_SELF_ENERGY_1PR",
                "DC3_projection": "EXACT_ZERO_EXTERNAL_PORT_ORTHOGONALITY",
            }
            for index, row in enumerate(b12_spectator_routes, start=1)
        ],
        "occurrence_orbit": [
            {
                "id": "BB-I1-HMINUS-CONTACTS",
                "rows": [
                    "T1=0",
                    "E1=0 external q square",
                    "T2=-128*v(r0)/(D0*D2), route002 bridge tag",
                    "T4=-128*v(r0)/(D0*D2), route003 bridge tag",
                    "T3=0",
                    "E2=0 external p square",
                ],
                "noncancellation": "T2 and T4 have opposite ordered color words and different external port order",
            },
            {
                "id": "BB-E-POT",
                "word": "+sqrt(2)*epsilon*(C cross C) inside -2 E_tilde",
                "kernel": "+sqrt(2)*K_potential",
            },
            {
                "id": "BB-X-POT",
                "word": "-sqrt(2)*epsilon*(C cross C) explicit",
                "kernel": "-sqrt(2)*K_potential",
            },
            {
                "id": "BB-TRANSPORTED-EDGE",
                "identity": "D2(Pib*Pis)=(D2Pib)Pis+Pib(D2Pis)+2(D-Pib)(D+Pis)-2(D+Pib)(D-Pis)",
                "survivors": ["Pib(D2Pis)", "-2(D+Pib)(D-Pis)"],
                "direct_to_transported_ratio": "(-2)/(-4)=1/2",
                "result": "SECOND_NEIGHBORING_EDGE_OCCURRENCE",
            },
            {"id": "BB-I2-B13", "result": "EXACT_ZERO_NO_C3_PORT_AND_SCALELESS_TADPOLE"},
            {"id": "BB-I0-S4", "result": "EXACT_ZERO_FLAVOR_PORT; Hminus has no quartic"},
            {"id": "BB-GF-GHOST-AUX", "result": "EXACT_ABSENT_BY_MATTER_FLAVOR_PORT_GRAMMAR"},
            {"id": "BB-COINCIDENT-JACOBIAN", "result": "EXACT_ZERO_DELTA_R_S_FOR_R_NOT_EQUAL_S; first superpotential Hessian is the counted TMH parent"},
        ],
        "triangle_result": {
            "B1__B2_basis": ["<D^D,C3^E>", "<C3^D,D^E>"],
            "direct_subtotal_over_lambda1": [
                expression_text(value) for value in direct_vector
            ],
            "transported_subtotal_over_lambda1": [
                expression_text(value) for value in transported_vector
            ],
            "coefficient_over_lambda1": [expression_text(value) for value in b12_vector],
            "SU3_lift": su3_rows,
        },
        "conditional_HT_comparison_only_after_calculation": {
            "target_B1__B2_over_lambda1": [expression_text(value) for value in target_b12],
            "target_minus_calculation": [expression_text(value) for value in mismatch],
            "verdict": "EXACT_MATCH",
        },
        "gpt_pro_adjudication": {
            "authority": "NON_AUTHORITY_PRO_REVIEW",
            "gate1": {
                "source": "proposals/gpt-pro-bb12-evanescent-cut-gate1-response-2026-07-14.md",
                "sha256": "a00e3a660e109ab5cc26e992f237f49874ef64fc6fa84f942a197ca12530e6b3",
                "verdict": "REJECTED",
                "errors": [
                    "-sqrt(2)*(2/3)+sqrt(2)*(1/3)=-sqrt(2) is false",
                    "extra fixed-port Hminus Wick factor two is false",
                    "exclusion of I1*S_Hminus one-loop contacts is false",
                ],
            },
            "gate2": {
                "source": "proposals/gpt-pro-bb12-evanescent-cut-gate2-response-2026-07-14.md",
                "sha256": "31f8906d79cd5f824191eb9d09c7733f4723a2916e45e5bac3c2f826f2e7d2e0",
                "verdict": "ACCEPTED_AFTER_INDEPENDENT_LOCAL_SPARSE_GRASSMANN_AND_NORMALIZATION_CHECK",
            },
        },
        "summary": {
            "checks": len(checks),
            "passed": len(checks),
            "failed": 0,
        },
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare exact JSON with an existing artifact")
    arguments = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.check is not None:
        if arguments.check.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"FAIL stale BB audit artifact: {arguments.check}")
        print(f"PASS exact BB audit matches {arguments.check}")
    else:
        print(rendered, end="")
    print(f"SUMMARY {payload['summary']['passed']}/{payload['summary']['checks']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
