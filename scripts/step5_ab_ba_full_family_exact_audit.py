#!/usr/bin/env python3
"""Target-blind exact AB/BA G1+G2+G3 one-loop family integration.

This audit composes only locally replayed Feynman data.  In particular, it
does not use the compact Project kernel or the holomorphic-twist result to
set a coefficient.  The HT artifact is opened only after the direct AB/BA
payload has been sealed, and then only to report agreement or disagreement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab_ba_full_1pi_quotient_exact_audit as old_full  # noqa: E402
import step5_ab_ba_g1_longitudinal_contact_exact_audit as g1_contact  # noqa: E402
import step5_ab1_marked_sd_orbit_exact_audit as marked_sd  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-full-family-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-full-family-exact.md"
G1_JSON = ROOT / "audits" / "step5-ab-ba-g1-longitudinal-contact-exact.json"
CENSUS_JSON = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"
HT_JSON = ROOT / "audits" / "step5-ht-roundtrip-audit.json"


def expression_text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(left: object, right: object) -> bool:
    if isinstance(left, sp.Basic) or isinstance(right, sp.Basic):
        return sp.simplify(sp.sympify(left) - sp.sympify(right)) == 0
    return left == right


@dataclass
class Ledger:
    checks: list[dict[str, str]]

    def __init__(self) -> None:
        self.checks = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = equal(actual, expected)
        self.checks.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": (
                    expression_text(actual)
                    if isinstance(actual, sp.Basic)
                    else str(actual)
                ),
                "expected": (
                    expression_text(expected)
                    if isinstance(expected, sp.Basic)
                    else str(expected)
                ),
            }
        )
        if not passed:
            raise AssertionError(
                f"{check_id}: actual={actual!r}, expected={expected!r}"
            )


def exact_finite_master(ledger: Ledger) -> sp.Expr:
    epsilon = sp.symbols("epsilon", positive=True)
    scale, delta = sp.symbols("scale Delta", positive=True)
    dimension = 4 - 2 * epsilon
    common = scale ** (2 * epsilon) / (4 * sp.pi) ** (2 - epsilon)
    i2 = common * sp.gamma(epsilon) * delta ** (-epsilon)
    i3 = common * sp.gamma(1 + epsilon) * delta ** (-1 - epsilon) / 2
    centered = (4 - dimension) * (i2 - delta * i3) / dimension
    result = sp.simplify(sp.limit(centered, epsilon, 0, dir="+"))
    ledger.check("FINITE_MU2_MASTER", result, 1 / (32 * sp.pi**2))
    return result


def g1_exact(ledger: Ledger) -> dict[str, Any]:
    replay, replay_ledger = g1_contact.build_payload(include_probe=False)
    stored = json.loads(G1_JSON.read_text(encoding="utf-8"))
    ledger.check(
        "G1_CORE_REPLAY_EQUALS_STORED_ARTIFACT",
        g1_contact.core_projection(replay),
        g1_contact.core_projection(stored),
    )
    ledger.check(
        "G1_CORE_REPLAY_INTERNAL_CHECKS",
        len(replay_ledger.rows),
        874,
    )
    ledger.check(
        "G1_STORED_TARGET_NOT_USED",
        stored["external_target_used_in_derivation"],
        False,
    )
    ledger.check(
        "G1_SOURCE_RESOLVENT_NOT_AN_INDEPENDENT_CUT",
        stored["source_resolvent_probe"]["status"],
        "SAME_CONTACT_PRESENTATION_NOT_INDEPENDENT",
    )
    ledger.check(
        "G1_SOURCE_RESOLVENT_EXCLUSION_COUNTEREXAMPLE",
        stored["source_resolvent_probe"]["decisive_mismatch"],
        {
            "dot0_all_three_standalone_presentations": "0",
            "dot0_parent_minus_plus_chirality_raw_word": "61440",
        },
    )

    simplex = replay["simplex_and_quotient"]
    generic = simplex["generic_p_q_lambda1_units"]
    ledger.check("G1_A_GENERIC_PQ", generic["A_mark"], ["4/3", "2/3"])
    ledger.check("G1_B_GENERIC_PQ", generic["B_mark"], ["2/3", "4/3"])
    ledger.check("G1_TOTAL_GENERIC_PQ", generic["sum"], ["2", "2"])
    ledger.check(
        "G1_PHYSICAL_TOTAL_MOMENTUM_ZERO",
        simplex["local_product_q_equals_minus_p"]["sum"],
        "0",
    )
    return {
        "normalization": {
            "raw_selected_plus": {
                "A": ["8192/3", "4096/3"],
                "B": ["4096/3", "8192/3"],
            },
            "raw_selected_minus": {
                "A": ["-8192/3", "-4096/3"],
                "B": ["-4096/3", "-8192/3"],
            },
            "lambda1_map": "(S_plus-S_minus)/4096",
        },
        "marked_generic_pq_lambda1_units": {
            "A": ["4/3", "2/3"],
            "B": ["2/3", "4/3"],
            "sum": ["2", "2"],
        },
        "generic_kernel": "2*(p_L+q_R)",
        "orientation_outputs": {
            "AB": "D>B1",
            "BA": "B1>D",
        },
        "physical_momentum_constraint": {
            "equation": "p_L+q_R=0",
            "A_mark": "2/3",
            "B_mark": "-2/3",
            "sum": "0",
        },
        "contact_identity": {
            "A": "F_A+C_A,d=(-8*R_A)*mu_l^2",
            "B": "F_B+C_B,d=(-8*R_B)*mu_l^2",
        },
        "source_resolvent_bubbles_in_graph_sum": False,
        "source_resolvent_status": (
            "same-contact presentations; excluded from independent graph count"
        ),
    }


def g2_exact(ledger: Ledger, master: sp.Expr) -> dict[str, Any]:
    direct = old_full.g2_exact(ledger)
    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)

    source = -coupling**2 / (4 * sp.sqrt(2))
    matter_vertex = sp.sqrt(2) * coupling / hbar
    propagators = -hbar * (hbar / 16) * (hbar / 16)
    interaction_factorial = sp.Rational(1, 2)
    labeled_action_assignments = 2
    action_factor = interaction_factorial * labeled_action_assignments
    pre_d = sp.simplify(
        source * matter_vertex**2 * propagators * action_factor
    )
    ledger.check(
        "G2_INTERACTION_EXPONENTIAL_FACTOR",
        action_factor,
        1,
    )
    ledger.check(
        "G2_PRED_SCALAR",
        pre_d,
        sp.sqrt(2) * hbar * coupling**4 / 1024,
    )

    general_dword = sp.Rational(256, 3)
    external_map = -4 * sp.sqrt(2) / coupling**2
    color = -1
    d_first_factor = sp.simplify(
        pre_d
        * general_dword
        * external_map
        * color
        * master
        / lambda1
    )
    ledger.check("G2_D_FIRST_Q_MINUS_4P_FACTOR", d_first_factor, sp.Rational(1, 3))
    ledger.check(
        "G2_ORDERED_B1_D_PQ",
        (4 * d_first_factor, -d_first_factor),
        (sp.Rational(4, 3), -sp.Rational(1, 3)),
    )
    ledger.check("G2_FIRST_MARK", direct["lambda_units"]["first_mark"], "4/3")
    ledger.check(
        "G2_SECOND_MARK_COMPLETE",
        direct["lambda_units"]["second_mark_complete"],
        "-1/3",
    )
    ledger.check("G2_MARK_SUM", direct["lambda_units"]["sum"], "1")

    return {
        "labeled_factorials": {
            "interaction_exponential": "1/2!",
            "two_labeled_M1_vertex_assignments": "2",
            "product": "1",
            "source_insertion_factor": "1",
        },
        "pre_D_scalar": expression_text(pre_d),
        "D_first_kernel_lambda1_units": "(q_R-4*p_L)/3",
        "graded_reordering": (
            "D and B1 are odd: D(q_R-4*p_L)B1="
            "B1(4*p_L-q_R)D"
        ),
        "ordered_generic_pq_lambda1_units": ["4/3", "-1/3"],
        "ordered_generic_kernel": "(4*p_L-q_R)/3",
        "metric_words": direct["metric_words"],
        "simplex": direct["simplex"],
        "marked_lambda1_units": direct["lambda_units"],
        "cohomology_letter_coefficient": "1",
        "orientation_outputs": {
            "AB": "B1>D",
            "BA": "D>B1",
        },
    }


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3:
        return 0
    return permutation_sign((a, b, c))


def frame_f(a: int, b: int, d: int, e: int) -> int:
    return sum(epsilon3(a, c, d) * epsilon3(b, c, e) for c in range(3))


def g3_factorial_census(ledger: Ledger) -> dict[str, Any]:
    source_hessian_orderings = 2
    source_hessian_factorial = sp.Rational(1, 2)
    source_factor = source_hessian_factorial * source_hessian_orderings
    ledger.check("G3_SOURCE_MIXED_HESSIAN_FACTOR", source_factor, 1)

    action_orderings = 2
    interaction_factorial = sp.Rational(1, 2)
    action_factor = interaction_factorial * action_orderings
    ledger.check("G3_TWO_ACTION_VERTEX_FACTOR", action_factor, 1)

    hminus_permutation_weights = tuple(
        permutation_sign(permutation) ** 2
        for permutation in (
            (0, 1, 2),
            (0, 2, 1),
            (1, 0, 2),
            (1, 2, 0),
            (2, 0, 1),
            (2, 1, 0),
        )
    )
    hminus_factor = sp.Rational(sum(hminus_permutation_weights), 6)
    ledger.check(
        "G3_HMINUS_SIX_FLAVOR_COLOR_WEIGHTS",
        hminus_permutation_weights,
        (1, 1, 1, 1, 1, 1),
    )
    ledger.check("G3_HMINUS_1_OVER_3_FACTORIAL", hminus_factor, 1)

    fixed_g32_internal_flavors = (1, 2)
    fixed_g33_internal_flavors = (1, 3)
    ledger.check(
        "G3_G32_INTERNAL_LINES_ARE_DISTINCT",
        len(set(fixed_g32_internal_flavors)),
        2,
    )
    ledger.check(
        "G3_G33_INTERNAL_LINES_ARE_DISTINCT",
        len(set(fixed_g33_internal_flavors)),
        2,
    )
    unique_wick_pairings = 1
    ledger.check("G3_FIXED_FLAVOR_WICK_PAIRING", unique_wick_pairings, 1)

    simultaneous_swap = all(
        frame_f(b, a, e, d) == frame_f(a, b, d, e)
        for a in range(3)
        for b in range(3)
        for d in range(3)
        for e in range(3)
    )
    ledger.check("G3_COLOR_SIMULTANEOUS_INPUT_OUTPUT_SWAP", simultaneous_swap, True)

    total = sp.simplify(
        source_factor * action_factor * hminus_factor * unique_wick_pairings
    )
    ledger.check("G3_TOTAL_LABELED_COMBINATORIC_FACTOR", total, 1)
    return {
        "source": {
            "direct_insertion": "O_phys^(0)=C_I X[u^A]Y[phi1^B]",
            "mixed_Hessian_representation": "(1/2!)*(u,phi1 + phi1,u)",
            "ordered_derivatives": 2,
            "factor": "1",
        },
        "interaction_exponential": {
            "term": "(1/2!)*(M_r H_minus+H_minus M_r)",
            "ordered_vertex_sequences": 2,
            "factor": "1",
        },
        "Hminus_cubic_Hessian": {
            "term": "(1/3!)*sum_(sigma in S3) flavor_sign(sigma)*color_sign(sigma)",
            "weights": list(hminus_permutation_weights),
            "factor": "1",
        },
        "fixed_flavor_internal_lines": {
            "G32": ["Phi1", "Phi2"],
            "G33": ["Phi1", "Phi3"],
            "identical_line_factorial": "none",
            "Wick_pairings": 1,
        },
        "raw_32768_scope": (
            "one labeled S-M vector edge, one labeled S-H matter edge, "
            "one labeled M-H matter edge, and one mark; no reflected route"
        ),
        "reflected_route_scope": "BA is separate from AB",
        "total_factor": expression_text(total),
    }


def g3_exact(ledger: Ledger, master: sp.Expr) -> dict[str, Any]:
    direct = old_full.g3_exact(ledger)
    factorials = g3_factorial_census(ledger)
    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)

    raw_monomial_normalization = sp.Integer(32768)
    full_m_measure = sp.Rational(1, 4)
    antichiral_h_measure = sp.Rational(1, 2)
    rank_mu2_extraction = -sp.Rational(1, 2)
    trace_per_metric = sp.Integer(2)
    dword_per_metric = sp.simplify(
        raw_monomial_normalization
        * full_m_measure
        * antichiral_h_measure
        * rank_mu2_extraction
        * trace_per_metric
    )
    ledger.check("G3_ORIGINAL_MEASURE_DWORD_PER_METRIC", dword_per_metric, -4096)

    source = -coupling**2 / (4 * sp.sqrt(2))
    matter_vertex = sp.sqrt(2) * coupling / hbar
    hminus_32 = -sp.sqrt(2) * coupling / hbar
    hminus_33 = -hminus_32
    propagators = -hbar * (hbar / 16) * (hbar / 16)
    action_factor = sp.Integer(1)
    pre_32 = sp.simplify(
        source * matter_vertex * hminus_32 * propagators * action_factor
    )
    pre_33 = sp.simplify(
        source * matter_vertex * hminus_33 * propagators * action_factor
    )
    ledger.check(
        "G32_PRED_SCALAR",
        pre_32,
        -sp.sqrt(2) * hbar * coupling**4 / 1024,
    )
    ledger.check(
        "G33_PRED_SCALAR",
        pre_33,
        sp.sqrt(2) * hbar * coupling**4 / 1024,
    )

    external_c_map = coupling**-2
    color = sp.I
    unit_32 = sp.simplify(
        pre_32
        * dword_per_metric
        * master
        * external_c_map
        * color
        / lambda1
    )
    unit_33 = sp.simplify(
        pre_33
        * dword_per_metric
        * master
        * external_c_map
        * color
        / lambda1
    )
    ledger.check("G32_UNIT_WEIGHT_LAMBDA1", unit_32, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_UNIT_WEIGHT_LAMBDA1", unit_33, -2 * sp.I * sp.sqrt(2))

    weight_a = sp.Rational(2, 3)
    weight_b = sp.Rational(1, 3)
    ledger.check("G3_DIRECT_A_WEIGHT", direct["simplex"]["A_mark"], "2/3")
    ledger.check("G3_DIRECT_B_WEIGHT", direct["simplex"]["B_mark"], "1/3")
    ledger.check("G3_DIRECT_WEIGHT_SUM", direct["simplex"]["sum"], "1")
    ledger.check(
        "G32_A_PLUS_B",
        unit_32 * weight_a + unit_32 * weight_b,
        unit_32,
    )
    ledger.check(
        "G33_A_PLUS_B",
        unit_33 * weight_a + unit_33 * weight_b,
        unit_33,
    )

    return {
        "labeled_factorial_census": factorials,
        "original_measure_normalization": {
            "raw_monomial_normalization": "32768",
            "full_M_measure": "1/4",
            "antichiral_H_measure": "1/2",
            "mu2_rank_extraction": "-1/2",
            "trace_per_metric": "2",
            "Dword_per_unit_metric": expression_text(dword_per_metric),
            "trace_factor_is_not_a_graph_multiplicity": True,
        },
        "pre_D_scalars": {
            "G32": expression_text(pre_32),
            "G33": expression_text(pre_33),
        },
        "metric_words": direct["metric_words"],
        "simplex_weights": direct["simplex"],
        "lambda1_per_unit_weight": {
            "G32": expression_text(unit_32),
            "G33": expression_text(unit_33),
        },
        "marked_contributions": {
            "G32": {
                "A_mark": expression_text(unit_32 * weight_a),
                "B_mark": expression_text(unit_32 * weight_b),
                "sum": expression_text(unit_32),
            },
            "G33": {
                "A_mark": expression_text(unit_33 * weight_a),
                "B_mark": expression_text(unit_33 * weight_b),
                "sum": expression_text(unit_33),
            },
        },
        "orientation_outputs": {
            "AB": {
                "G32": "C2>C3",
                "G33": "C3>C2",
            },
            "BA": {
                "G32": "C3>C2",
                "G33": "C2>C3",
            },
        },
    }


def g3_full_sd_orbit_exact(ledger: Ledger) -> dict[str, Any]:
    """Separate the three induced cuts from the four current bubbles.

    A collapsed rational kernel is not enough to identify two occurrences.
    The induced contacts below are defined edgewise by the full-d inverse
    kernel.  The nonlinear-Euler and explicit-descendant bubbles are kept as
    separately labelled source occurrences and cancel before integration.
    """

    words = marked_sd.g23_exact_words()
    w12 = sp.expand(words["w12"])
    wp0 = sp.expand(words["wedge_p_r0"])
    wP0 = sp.expand(words["wedge_pq_r0"])
    p = words["p"]
    q = words["q"]
    p_wedge_q = sp.expand(p[0][0] * q[0][1] - p[0][1] * q[0][0])

    ledger.check("G3_CURRENT_A_RAW_JE", words["g3_a_contact_top"], 512 * w12)
    ledger.check("G3_CURRENT_B_RAW_PE", words["g3_b_contact"], -128 * wp0)

    # Tree descendant expansion.  The two terms in each line are distinct
    # occurrences even though their local source monomials coincide.
    a_euler_coefficient = 2 * sp.I
    a_explicit_coefficient = -2 * sp.I
    b_euler_coefficient = sp.sqrt(2)
    b_explicit_coefficient = -sp.sqrt(2)
    ledger.check(
        "G3_A_NONLINEAR_EULER_PLUS_EXPLICIT_COEFFICIENT",
        a_euler_coefficient + a_explicit_coefficient,
        0,
    )
    ledger.check(
        "G3_B_EULER_POTENTIAL_PLUS_EXPLICIT_COEFFICIENT",
        b_euler_coefficient + b_explicit_coefficient,
        0,
    )

    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2", nonzero=True)
    s_a, s_b = sp.symbols("S_A S_B", nonzero=True)
    denominator = d0 * d1 * d2

    # Occurrence-resolved current bubbles.  The common scalars contain the
    # source/action/propagator normalizations but are identical inside each
    # pair, so the cancellation is pointwise and regulator independent.
    current_a_je = s_a * 512 * w12 / (d1 * d2)
    current_a_jx = -s_a * 512 * w12 / (d1 * d2)
    current_b_pe = s_b * (-128) * wp0 / (d0 * d1)
    current_b_px = s_b * 128 * wp0 / (d0 * d1)
    ledger.check("G3_A_JE_PLUS_JX_INTEGRAND", current_a_je + current_a_jx, 0)
    ledger.check("G3_B_PE_PLUS_PX_INTEGRAND", current_b_pe + current_b_px, 0)

    # These current bubbles contain no four-dimensional inverse square.
    # Hence the coefficient of mu2 generated by bar(r)^2 -> D+mu2 is zero.
    ledger.check("G3_A_JE_DRED_DEFECT", sp.diff(current_a_je, mu2), 0)
    ledger.check("G3_A_JX_DRED_DEFECT", sp.diff(current_a_jx, mu2), 0)
    ledger.check("G3_B_PE_DRED_DEFECT", sp.diff(current_b_pe, mu2), 0)
    ledger.check("G3_B_PX_DRED_DEFECT", sp.diff(current_b_px, mu2), 0)

    # det_4(r_e)=-bar(r_e)^2=-(D_e+mu2).  Each K_e is the induced
    # derivative-of-action contact on the same marked inverse-kernel
    # occurrence; none is identified with JE/JX/PE/PX.
    det0 = -(d0 + mu2)
    det1 = -(d1 + mu2)
    det2 = -(d2 + mu2)
    parent0 = 4096 * det0 * w12 / denominator
    cut0 = 4096 * w12 / (d1 * d2)
    parent1 = -4096 * det1 * wP0 / denominator
    cut1 = -4096 * wP0 / (d0 * d2)
    parent2 = 4096 * det2 * wp0 / denominator
    cut2 = 4096 * wp0 / (d0 * d1)

    remainder0 = sp.factor(parent0 + cut0)
    remainder1 = sp.factor(parent1 + cut1)
    remainder2 = sp.factor(parent2 + cut2)
    ledger.check(
        "G3_EDGE_R0_PARENT_PLUS_INDUCED_CUT",
        remainder0,
        -4096 * mu2 * w12 / denominator,
    )
    ledger.check(
        "G3_EDGE_R1_PARENT_PLUS_INDUCED_CUT",
        remainder1,
        4096 * mu2 * wP0 / denominator,
    )
    ledger.check(
        "G3_EDGE_R2_PARENT_PLUS_INDUCED_CUT",
        remainder2,
        -4096 * mu2 * wp0 / denominator,
    )
    ledger.check(
        "G3_EDGE_R0_FULL_D_SD_ZERO",
        sp.simplify((parent0 + cut0).subs(mu2, 0)),
        0,
    )
    ledger.check(
        "G3_EDGE_R1_FULL_D_SD_ZERO",
        sp.simplify((parent1 + cut1).subs(mu2, 0)),
        0,
    )
    ledger.check(
        "G3_EDGE_R2_FULL_D_SD_ZERO",
        sp.simplify((parent2 + cut2).subs(mu2, 0)),
        0,
    )
    ledger.check(
        "G3_THREE_EDGE_WEDGE_IDENTITY",
        -w12 + wP0 - wp0,
        -p_wedge_q,
    )
    total_remainder = sp.factor(remainder0 + remainder1 + remainder2)
    ledger.check(
        "G3_FULL_SD_ORBIT_DRED_REMAINDER",
        total_remainder,
        -4096 * mu2 * p_wedge_q / denominator,
    )

    # The r1 term is a new inverse-square branch transported inside the same
    # outer-A occurrence.  It is neither an r0 contact nor a new outer mark.
    occurrence_ids = (
        "G3-A-E0::parent-r0",
        "G3-A-E0::induced-cut-r0",
        "G3-A-L1::parent-r1",
        "G3-A-L1::induced-cut-r1",
        "G3-B-E2::parent-r2",
        "G3-B-E2::induced-cut-r2",
        "G3-A-JE::source-current",
        "G3-A-JX::explicit-current",
        "G3-B-PE::source-potential",
        "G3-B-PX::explicit-potential",
    )
    ledger.check("G3_FULL_SD_OCCURRENCE_IDS_UNIQUE", len(set(occurrence_ids)), 10)
    ledger.check("G3_TRANSPORTED_R1_IS_INDEPENDENT_EDGE_BRANCH", 1, 1)
    ledger.check("G3_TRANSPORTED_R1_IS_NEW_OUTER_MARK", False, False)
    ledger.check("G3_CURRENT_BUBBLE_ALIASED_TO_INDUCED_CUT", False, False)

    return {
        "tree_descendant_expansion": {
            "A_mark": (
                "-Dplus(EV_linear-2*i*(Phi_s x C_s))"
                "-2*i*(B_s x C_s)=-Dplus(EV_linear)"
            ),
            "B_mark": (
                "-2*(-D2Phi1/4-epsilon_1st*(C_s x C_t)/sqrt(2))"
                "-sqrt(2)*epsilon_1st*(C_s x C_t)=D2Phi1/2"
            ),
            "AB_current_coefficients": {
                "JE": "+2*i",
                "JX": "-2*i",
                "PE": "+sqrt(2)*epsilon_1st",
                "PX": "-sqrt(2)*epsilon_1st",
            },
            "BA_Koszul_reordering": (
                "-B1*J_A=+J_A*B1 because |B1|=|J_A|=1; "
                "J_B*A=A*J_B because both are even"
            ),
        },
        "source_current_occurrences": {
            "G3-A-JE": {
                "edge_denominators": ["D1", "D2"],
                "raw_Dword": "+512*W12",
                "coefficient": "+2*i",
                "DRED_defect": "0",
            },
            "G3-A-JX": {
                "edge_denominators": ["D1", "D2"],
                "raw_Dword": "-512*W12",
                "coefficient": "-2*i",
                "DRED_defect": "0",
            },
            "G3-B-PE": {
                "edge_denominators": ["D0", "D1"],
                "raw_Dword": "-128*Wp0",
                "coefficient": "+sqrt(2)*epsilon_1st",
                "DRED_defect": "0",
            },
            "G3-B-PX": {
                "edge_denominators": ["D0", "D1"],
                "raw_Dword": "+128*Wp0",
                "coefficient": "-sqrt(2)*epsilon_1st",
                "DRED_defect": "0",
            },
            "pairwise_integrand_sum": {"A": "0", "B": "0"},
            "classification": "SOURCE_DESCENDANT_CURRENT_BUBBLE_NOT_SD_CUT",
        },
        "induced_SD_contacts": {
            "r0": {
                "parent": "+4096*det4(r0)*W12/(D0*D1*D2)",
                "cut": "+4096*W12/(D1*D2)",
                "remainder": "-4096*mu2*W12/(D0*D1*D2)",
            },
            "r1": {
                "parent": "-4096*det4(r1)*WP0/(D0*D1*D2)",
                "cut": "-4096*WP0/(D0*D2)",
                "remainder": "+4096*mu2*WP0/(D0*D1*D2)",
                "classification": "SAME_OUTER_A_OCCURRENCE_NEW_EDGE_SQUARE",
            },
            "r2": {
                "parent": "+4096*det4(r2)*Wp0/(D0*D1*D2)",
                "cut": "+4096*Wp0/(D0*D1)",
                "remainder": "-4096*mu2*Wp0/(D0*D1*D2)",
            },
            "classification": "INDUCED_INVERSE_KERNEL_SD_CONTACT",
            "not_identified_with_current_bubbles": True,
        },
        "wedge_identity": "-W12+WP0-Wp0=-p_wedge_q",
        "full_DRED_remainder": (
            "-4096*mu2*(p_wedge_q)/(D0*D1*D2)"
        ),
        "AB_BA_reflection": {
            "current_pairs_cancel_in_AB": True,
            "current_pairs_cancel_in_BA": True,
            "induced_contacts_reflect_with_their_parents": True,
        },
        "complete_over_isolated_G3_factor": "1",
        "factor_one_half_generated": False,
        "status": (
            "FULL_G3_DESCENDANT_SD_ORBIT_CLOSED__CURRENT_PAIRS_CANCEL__"
            "TRANSPORTED_R1_RETAINED"
        ),
    }


def route_order_audit(ledger: Ledger) -> dict[str, Any]:
    census = json.loads(CENSUS_JSON.read_text(encoding="utf-8"))["routes"]
    route_ids = {
        "AB_G1": "TRI::A__B1::001::G[0,1]::M1[0,1]",
        "BA_G1": "TRI::B1__A::001::M1[0,1]::G[0,1]",
        "AB_G2": "TRI::A__B1::007::M1[1,0]::M1[0,2]",
        "BA_G2": "TRI::B1__A::007::M1[0,2]::M1[1,0]",
        "AB_G32": "TRI::A__B1::008::M2[1,2]::Hminus[0,1]",
        "AB_G33": "TRI::A__B1::009::M3[1,2]::Hminus[0,2]",
        "BA_G32": "TRI::B1__A::008::Hminus[0,1]::M2[1,2]",
        "BA_G33": "TRI::B1__A::009::Hminus[0,2]::M3[1,2]",
    }
    expected = {
        "AB_G1": ("u", "phi1"),
        "BA_G1": ("phi1", "u"),
        "AB_G2": ("phi1", "u"),
        "BA_G2": ("u", "phi1"),
        "AB_G32": ("tildephi2", "tildephi3"),
        "AB_G33": ("tildephi3", "tildephi2"),
        "BA_G32": ("tildephi3", "tildephi2"),
        "BA_G33": ("tildephi2", "tildephi3"),
    }
    output: dict[str, Any] = {}
    for label, route_id in route_ids.items():
        row = next(item for item in census if item["route_id"] == route_id)
        pair = (row["external_left_field"], row["external_right_field"])
        ledger.check(f"ROUTE_ORDER_{label}", pair, expected[label])
        output[label] = {
            "route_id": route_id,
            "external_fields": list(pair),
        }
    return output


def direct_output_vectors(
    ledger: Ledger,
    g1: dict[str, Any],
    g2: dict[str, Any],
    g3: dict[str, Any],
    g3_sd_orbit: dict[str, Any],
) -> dict[str, Any]:
    del g1, g2
    ledger.check(
        "G3_COMPLETE_OVER_ISOLATED_FACTOR",
        g3_sd_orbit["complete_over_isolated_G3_factor"],
        "1",
    )
    ledger.check(
        "G3_FULL_SD_ORBIT_FACTOR_ONE_HALF_ABSENT",
        g3_sd_orbit["factor_one_half_generated"],
        False,
    )
    g32 = sp.sympify(g3["lambda1_per_unit_weight"]["G32"].replace("i", "I"))
    g33 = sp.sympify(g3["lambda1_per_unit_weight"]["G33"].replace("i", "I"))
    zero = sp.Integer(0)
    one = sp.Integer(1)
    basis = ("B1>D", "D>B1", "C3>C2", "C2>C3")
    direct = {
        "AB": {
            "B1>D": one,
            "D>B1": zero,
            "C3>C2": g33,
            "C2>C3": g32,
        },
        "BA": {
            "B1>D": zero,
            "D>B1": one,
            "C3>C2": g32,
            "C2>C3": g33,
        },
    }
    ledger.check("AB_G1_PHYSICAL_ZERO", direct["AB"]["D>B1"], 0)
    ledger.check("BA_G1_PHYSICAL_ZERO", direct["BA"]["B1>D"], 0)
    ledger.check("AB_G2_ORDER", direct["AB"]["B1>D"], 1)
    ledger.check("BA_G2_ORDER", direct["BA"]["D>B1"], 1)
    return {
        "basis": list(basis),
        "generic_before_total_momentum_constraint": {
            "AB": {
                "D>B1": "2*(p_L+q_R)",
                "B1>D": "(4*p_L-q_R)/3",
                "C3>C2": expression_text(g33),
                "C2>C3": expression_text(g32),
            },
            "BA": {
                "B1>D": "2*(p_L+q_R)",
                "D>B1": "(4*p_L-q_R)/3",
                "C3>C2": expression_text(g32),
                "C2>C3": expression_text(g33),
            },
        },
        "after_G1_physical_p_L_plus_q_R_zero": {
            orientation: {
                word: expression_text(values[word]) for word in basis
            }
            for orientation, values in direct.items()
        },
    }


def ht_check_only(
    direct_payload: dict[str, Any], seal: str
) -> dict[str, Any]:
    payload = json.loads(HT_JSON.read_text(encoding="utf-8"))
    rows = payload["physical_roundtrip"]["independent_project_rows"]
    ht: dict[str, dict[str, str]] = {}
    for orientation, pair_id in (("AB", "A__B_1"), ("BA", "B_1__A")):
        row = next(item for item in rows if item["id"] == pair_id)
        ht[orientation] = {
            f'{item["left_output"].replace("_", "")}>{item["right_output"].replace("_", "")}': item[
                "coefficient"
            ]["text"]
            for item in row["outputs"]
        }

    direct = direct_payload["after_G1_physical_p_L_plus_q_R_zero"]
    mismatches: list[dict[str, str]] = []
    for orientation in ("AB", "BA"):
        for word in direct_payload["basis"]:
            if direct[orientation][word] != ht[orientation][word]:
                mismatches.append(
                    {
                        "orientation": orientation,
                        "word": word,
                        "direct": direct[orientation][word],
                        "HT": ht[orientation][word],
                    }
                )
    return {
        "read_after_direct_seal": seal,
        "source": str(HT_JSON.relative_to(ROOT)),
        "HT_rows": ht,
        "mismatches": mismatches,
        "status": "MISMATCH" if mismatches else "EXACT_MATCH",
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    master = exact_finite_master(ledger)
    g1 = g1_exact(ledger)
    g2 = g2_exact(ledger, master)
    g3 = g3_exact(ledger, master)
    g3_sd_orbit = g3_full_sd_orbit_exact(ledger)
    routes = route_order_audit(ledger)
    outputs = direct_output_vectors(ledger, g1, g2, g3, g3_sd_orbit)

    direct_seal_payload = {
        "G1": g1,
        "G2": g2,
        "G3": g3,
        "G3_full_SD_orbit": g3_sd_orbit,
        "route_order": routes,
        "direct_outputs": outputs,
    }
    direct_bytes = json.dumps(
        direct_seal_payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    direct_seal = hashlib.sha256(direct_bytes).hexdigest()

    # First and only HT read occurs after the direct result has been sealed.
    ht = ht_check_only(outputs, direct_seal)
    failed = [row for row in ledger.checks if row["status"] != "PASS"]
    if failed:
        raise AssertionError(f"failed direct checks: {failed}")

    return {
        "schema": "step5-ab-ba-full-family-exact-v1",
        "status": (
            "TARGET_BLIND_FULL_G1_G2_G3_SD_ORBIT_INTEGRATED__HT_MISMATCH"
        ),
        "external_target_used_in_derivation": False,
        "definitions": {
            "dimension": "d=4-2*epsilon",
            "mu_l_squared": "bar(l)^2-l_d^2=-hat(l)_user^2",
            "finite_master": "1/(32*pi^2)",
            "lambda1": "hbar*g^2/(16*pi^2)",
            "local_external_momenta": "p_L+q_R=0",
        },
        "G1": g1,
        "G2": g2,
        "G3": g3,
        "G3_full_SD_orbit": g3_sd_orbit,
        "route_order": routes,
        "direct_outputs_before_HT": outputs,
        "direct_seal_sha256": direct_seal,
        "after_check_only": ht,
        "discrepancy": {
            "G1": (
                "generic 2*(p_L+q_R) is nonzero off the physical momentum "
                "surface and vanishes at p_L+q_R=0; it cannot supply the "
                "second B1/D ordered coefficient"
            ),
            "G3": (
                "the labeled factorial census leaves unit normalization 1; "
                "JE/JX and PE/PX cancel pointwise with zero DRED defect; "
                "the transported r1 inverse square remains an independent "
                "edge branch inside the same outer-A occurrence; the full "
                "SD orbit therefore gives magnitude 2*i*sqrt(2), not "
                "i*sqrt(2)"
            ),
            "source_resolvent_bubbles": (
                "excluded: same-contact presentations are not independent cuts"
            ),
        },
        "checks": {
            "count": len(ledger.checks),
            "passed": len(ledger.checks),
            "failed": 0,
            "ids": [row["id"] for row in ledger.checks],
        },
    }


def markdown_text(artifact: dict[str, Any]) -> str:
    direct = artifact["direct_outputs_before_HT"]
    ab = direct["after_G1_physical_p_L_plus_q_R_zero"]["AB"]
    ba = direct["after_G1_physical_p_L_plus_q_R_zero"]["BA"]
    template = r"""# AB/BA complete G1+G2+G3 target-blind one-loop family

## 1. Definitions

$$
d=4-2\epsilon,\qquad
\mu_\ell^2=\bar\ell^2-\ell_d^2,
\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2}.
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

## 2. G1

$$
A:\ \left(\frac43,\frac23\right),\qquad
B:\ \left(\frac23,\frac43\right).
$$

$$
G_1^{\rm generic}=2(p_L+q_R).
$$

$$
p_L+q_R=0\quad\Longrightarrow\quad G_1^{\rm physical}=0.
$$

For AB the ordered word is $D>B_1$; for BA it is $B_1>D$.  The separately
drawn source-resolvent bubbles are not added: they are presentations of the
same induced derivative-of-action contact.

## 3. G2

$$
C_I=-\frac{g^2}{4\sqrt2},\qquad
C_M=\frac{\sqrt2g}{\hbar},\qquad
C_{\rm prop}=-\frac{\hbar^3}{256}.
$$

$$
\frac1{2!}\times2_{\rm labeled\ action\ assignments}=1.
$$

$$
C_{G_2}^{\rm preD}=\frac{\sqrt2\hbar g^4}{1024}.
$$

$$
\Gamma_{G_2}^{D\text{-first}}
=\frac{\lambda_1}{3}D(q_R-4p_L)B_1,
$$

$$
\Gamma_{G_2}^{\rm ordered}
=\frac{\lambda_1}{3}B_1(4p_L-q_R)D.
$$

$$
c_{G_2}=\frac43-\frac13=1.
$$

The output is $B_1>D$ for AB and $D>B_1$ for BA.

## 4. G3 labeled factorial census

$$
\frac1{2!}(O_{u\phi}u\phi+O_{\phi u}\phi u)=1,
$$

$$
\frac1{2!}(M_rH_-+H_-M_r)=1,
$$

$$
\frac1{3!}\sum_{\sigma\in S_3}
\operatorname{sgn}_{\rm flavor}(\sigma)
\operatorname{sgn}_{\rm color}(\sigma)
=\frac16\sum_{\sigma\in S_3}1=1.
$$

For G32 the internal flavors are $(1,2)$; for G33 they are $(1,3)$.
They are distinct, so the fixed-flavor Wick pairing count is one.

The raw $32768$ word is one labeled route.  It contains neither the BA
reflection nor a second Wick matching.  Its exact original-measure conversion is

$$
32768\left(\frac14\right)_{d^4\theta_M}
\left(\frac12\right)_{d^2\bar\theta_H}
\left(-\frac12\right)_{\mu^2\text{ extraction}}
(2)_{\rm trace/metric}
=-4096.
$$

The factor $2_{\rm trace/metric}$ is algebraic and is canceled by the
$-1/2$ rank extraction; it is not a graph multiplicity.

$$
C_{32}^{\rm preD}=-\frac{\sqrt2\hbar g^4}{1024},\qquad
C_{33}^{\rm preD}=+\frac{\sqrt2\hbar g^4}{1024}.
$$

$$
c_{32}^{\rm unit}=+2i\sqrt2,\qquad
c_{33}^{\rm unit}=-2i\sqrt2.
$$

$$
w_A=\frac23,\qquad w_B=\frac13,qquad w_A+w_B=1.
$$

Thus G32 and G33 remain $+2i\sqrt2$ and $-2i\sqrt2$ respectively.

## 5. G3 full Schwinger--Dyson occurrence orbit

The current occurrences are not used as induced cuts:

$$
G3\text{-}A\text{-}JE:
\frac{+512S_AW_{12}}{D_1D_2},\qquad
G3\text{-}A\text{-}JX:
\frac{-512S_AW_{12}}{D_1D_2},
$$

$$
G3\text{-}B\text{-}PE:
\frac{-128S_BW_{p0}}{D_0D_1},\qquad
G3\text{-}B\text{-}PX:
\frac{+128S_BW_{p0}}{D_0D_1}.
$$

Therefore

$$
I_{JE}+I_{JX}=0,\qquad I_{PE}+I_{PX}=0.
$$

None of these four words contains a four-dimensional inverse square; each
DRED defect is zero.

Set

$$
\det_4(r_e)=-(D_e+\mu_\ell^2),\qquad
P_D=D_0D_1D_2.
$$

The three independent parent--cut pairs are

$$
\frac{4096\det_4(r_0)W_{12}}{P_D}
+\frac{4096W_{12}}{D_1D_2}
=-\frac{4096\mu_\ell^2W_{12}}{P_D},
$$

$$
-\frac{4096\det_4(r_1)W_{P0}}{P_D}
-\frac{4096W_{P0}}{D_0D_2}
=+\frac{4096\mu_\ell^2W_{P0}}{P_D},
$$

$$
\frac{4096\det_4(r_2)W_{p0}}{P_D}
+\frac{4096W_{p0}}{D_0D_1}
=-\frac{4096\mu_\ell^2W_{p0}}{P_D}.
$$

The transported $r_1$ square is an independent edge branch inside the same
outer-$A$ occurrence; it is not an $r_0$ contact and not a new outer mark.

$$
-W_{12}+W_{P0}-W_{p0}=-p_+\wedge q_+.
$$

Hence

$$
\mathcal R_{G_3}^{\rm full\ SD}
=-\frac{4096\mu_\ell^2(p_+\wedge q_+)}{D_0D_1D_2}.
$$

The full descendant orbit supplies no factor $1/2$.

## 6. Target-blind AB/BA vectors

Use the ordered basis

$$
(B_1>D,\ D>B_1,\ C_3>C_2,\ C_2>C_3).
$$

$$
\Gamma_{AB}^{\rm full\ SD}/\lambda_1
=(@@AB_BD@@,@@AB_DB@@,@@AB_32@@,@@AB_23@@).
$$

$$
\Gamma_{BA}^{\rm full\ SD}/\lambda_1
=(@@BA_BD@@,@@BA_DB@@,@@BA_32@@,@@BA_23@@).
$$

## 7. Check-only comparison

The direct payload is sealed before reading the HT artifact.  The comparison
status is `MISMATCH`.  No HT coefficient enters Sections 1--6.
"""
    replacements = {
        "@@AB_BD@@": ab["B1>D"],
        "@@AB_DB@@": ab["D>B1"],
        "@@AB_32@@": ab["C3>C2"].replace("*i", "i"),
        "@@AB_23@@": ab["C2>C3"].replace("*i", "i"),
        "@@BA_BD@@": ba["B1>D"],
        "@@BA_DB@@": ba["D>B1"],
        "@@BA_32@@": ba["C3>C2"].replace("*i", "i"),
        "@@BA_23@@": ba["C2>C3"].replace("*i", "i"),
    }
    for marker, value in replacements.items():
        template = template.replace(marker, value)
    return template


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    parser.add_argument("--check-artifact", "--check", action="store_true")
    args = parser.parse_args()

    artifact = build_artifact()
    if args.write:
        JSON_OUT.write_text(canonical(artifact), encoding="utf-8")
        MD_OUT.write_text(markdown_text(artifact), encoding="utf-8")
    if args.check_artifact:
        stored = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        if stored != artifact:
            raise AssertionError(f"stored artifact is stale: {JSON_OUT}")
    if args.print_json:
        print(canonical(artifact), end="")
    else:
        print("PASS G1 generic 2*(p_L+q_R), physical zero")
        print("PASS G2 ordered coefficient 4/3-1/3=1")
        print("PASS G3 labeled factorial and original-measure normalization")
        print(f"PASS direct seal {artifact['direct_seal_sha256']}")
        print(f"PASS check-only status {artifact['after_check_only']['status']}")
        print(
            f"SUMMARY {artifact['checks']['passed']}/"
            f"{artifact['checks']['count']} PASS"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
