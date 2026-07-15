#!/usr/bin/env python3
"""Exact target-blind AA raw gauge-convolution and SD-cut audit.

The checker starts at Step 5A (5A.52), enumerates the four cubic words and
all six labeled source/bridge/external slot assignments in each chirality,
locks the canonical Hessians without a route-count multiplier, and replays
both DA and independently reflected AD corrected-index exterior-algebra
words.  The Schwinger contact is retained occurrence by occurrence; no
holomorphic-twist or Project coefficient is read.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_gauge_marked_occurrence_exact_audit as aa  # noqa: E402


DEFAULT_JSON = ROOT / "audits/step5-aa-gauge-raw-convolution-hessian-exact.json"
AUDIT = ROOT / "audits/step5-aa-gauge-raw-convolution-hessian-exact.md"
CONTRACT = ROOT / "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
CENSUS = ROOT / "audits/step5-all-triangle-parent-port-census.json"


RAW_WORDS = {
    "+": (
        {
            "id": "1000",
            "pqrs": (1, 0, 0, 0),
            "sign": 1,
            "left": "barD2(V_X D^a V_Y)",
            "right": "barD2(D_a V_Z)",
            "color": "K(X,Y;Z)",
            "linear_slot": "Z",
        },
        {
            "id": "0100",
            "pqrs": (0, 1, 0, 0),
            "sign": -1,
            "left": "barD2(D^a V_X V_Y)",
            "right": "barD2(D_a V_Z)",
            "color": "K(X,Y;Z)",
            "linear_slot": "Z",
        },
        {
            "id": "0010",
            "pqrs": (0, 0, 1, 0),
            "sign": 1,
            "left": "barD2(D^a V_X)",
            "right": "barD2(V_Y D_a V_Z)",
            "color": "K(Y,Z;X)",
            "linear_slot": "X",
        },
        {
            "id": "0001",
            "pqrs": (0, 0, 0, 1),
            "sign": -1,
            "left": "barD2(D^a V_X)",
            "right": "barD2(D_a V_Y V_Z)",
            "color": "K(Y,Z;X)",
            "linear_slot": "X",
        },
    ),
    "-": (
        {
            "id": "1000",
            "pqrs": (1, 0, 0, 0),
            "sign": -1,
            "left": "D2(V_X barD_dot_a V_Y)",
            "right": "D2(barD^dot_a V_Z)",
            "color": "K(X,Y;Z)",
            "linear_slot": "Z",
        },
        {
            "id": "0100",
            "pqrs": (0, 1, 0, 0),
            "sign": 1,
            "left": "D2(barD_dot_a V_X V_Y)",
            "right": "D2(barD^dot_a V_Z)",
            "color": "K(X,Y;Z)",
            "linear_slot": "Z",
        },
        {
            "id": "0010",
            "pqrs": (0, 0, 1, 0),
            "sign": -1,
            "left": "D2(barD_dot_a V_X)",
            "right": "D2(V_Y barD^dot_a V_Z)",
            "color": "K(Y,Z;X)",
            "linear_slot": "X",
        },
        {
            "id": "0001",
            "pqrs": (0, 0, 0, 1),
            "sign": 1,
            "left": "D2(barD_dot_a V_X)",
            "right": "D2(barD^dot_a V_Y V_Z)",
            "color": "K(Y,Z;X)",
            "linear_slot": "X",
        },
    ),
}


def expr(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value))


def substitute_labels(text: str, assignment: dict[str, str]) -> str:
    answer = text
    for slot in ("X", "Y", "Z"):
        answer = answer.replace(slot, assignment[slot])
    return answer


def raw_port_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for chirality, words in RAW_WORDS.items():
        for word in words:
            for permutation in itertools.permutations(("S", "B", "E")):
                assignment = dict(zip(("X", "Y", "Z"), permutation, strict=True))
                sign = int(word["sign"])
                rows.append(
                    {
                        "id": f"{chirality}:{word['id']}:{''.join(permutation)}",
                        "chirality": chirality,
                        "pqrs": list(word["pqrs"]),
                        "assignment": assignment,
                        "coefficient_original_V": f"{sign:+d}*h/512",
                        "coefficient_canonical_u": f"{sign:+d}*sqrt(2)*g/256",
                        "left_word": substitute_labels(str(word["left"]), assignment),
                        "right_word": substitute_labels(str(word["right"]), assignment),
                        "ordered_color_word": substitute_labels(str(word["color"]), assignment),
                        "external_is_linear_field_strength_slot": assignment[str(word["linear_slot"])] == "E",
                    }
                )
    return rows


def longitudinal_mark(word: aa.Grassmann, point: int, momentum: tuple[sp.Expr, ...]) -> aa.Grassmann:
    return (
        sp.sqrt(2)
        / 16
        * aa.d_operator(
            aa.bar_d_square(aa.d_square(word, point, momentum), point, momentum),
            point,
            0,
            momentum,
        )
    )


def direct_rows(
    source_01: aa.Grassmann,
    source_02: aa.Grassmann,
    external_d: aa.Grassmann,
    external_w: aa.Grassmann,
    middle: aa.Grassmann,
    r0: tuple[sp.Expr, ...],
    r1: tuple[sp.Expr, ...],
    r2: tuple[sp.Expr, ...],
    *,
    spinor: int = 1,
) -> tuple[sp.Expr, ...]:
    bar_01 = lambda word: aa.bar_d_upper(word, 1, 0, aa.negative(r0))
    bar_12 = lambda word: aa.bar_d_upper(word, 1, 0, r1)
    # W^gamma D_gamma|W_plus=-W_plus D_minus.  The common raised-field
    # sign is included before expanding the two endpoint differences.
    d_02 = lambda word: -aa.d_operator(word, 2, spinor, r2)
    d_12 = lambda word: -aa.d_operator(word, 2, spinor, aa.negative(r1))
    words = (
        source_01 * bar_12(middle) * d_02(source_02),
        -source_01 * d_12(bar_12(middle)) * source_02,
        -bar_01(source_01) * middle * d_02(source_02),
        bar_01(source_01) * d_12(middle) * source_02,
    )
    integrated_mask = sum(1 << index for index in range(4, 13))
    return tuple(
        sp.factor((external_d * external_w * word).terms.get(integrated_mask, 0))
        for word in words
    )


def reflected_rows(
    source_01: aa.Grassmann,
    source_02: aa.Grassmann,
    external_w: aa.Grassmann,
    external_d: aa.Grassmann,
    middle: aa.Grassmann,
    r0: tuple[sp.Expr, ...],
    r1: tuple[sp.Expr, ...],
    r2: tuple[sp.Expr, ...],
    *,
    spinor: int = 1,
) -> tuple[sp.Expr, ...]:
    # Independent reflected trace: W sits at point 1 and tilde-W at point 2.
    # The chiral endpoint is D_e0-D_e1 after W^-=-W_+; the antichiral
    # endpoint is barD_e1-barD_e2.  W is kept to the left of D.
    d_01 = lambda word: aa.d_operator(word, 1, spinor, aa.negative(r0))
    d_12 = lambda word: aa.d_operator(word, 1, spinor, r1)
    bar_12 = lambda word: aa.bar_d_upper(word, 2, 0, aa.negative(r1))
    bar_02 = lambda word: aa.bar_d_upper(word, 2, 0, r2)
    words = (
        d_01(source_01) * bar_12(middle) * source_02,
        -d_01(source_01) * middle * bar_02(source_02),
        -source_01 * bar_12(d_12(middle)) * source_02,
        source_01 * d_12(middle) * bar_02(source_02),
    )
    integrated_mask = sum(1 << index for index in range(4, 13))
    return tuple(
        sp.factor((external_w * external_d * word).terms.get(integrated_mask, 0))
        for word in words
    )


def dword_payload() -> dict[str, object]:
    momenta = [sp.symbols(f"a{i} b{i} c{i} d{i}") for i in range(3)]
    r0, r1, r2 = momenta
    q = tuple(r0[index] - r1[index] for index in range(4))
    p = tuple(r1[index] - r2[index] for index in range(4))

    middle = aa.theta_delta(1, 2)
    delta_01 = aa.theta_delta(0, 1)
    delta_02 = aa.theta_delta(0, 2)
    unmarked_01 = aa.source_bottom(aa.source_k(delta_01, 0, r0))
    unmarked_02 = aa.source_bottom(aa.source_k(delta_02, 0, aa.negative(r2)))
    full_01 = aa.source_bottom(aa.marked_source_k(delta_01, 0, r0))
    full_02 = aa.source_bottom(aa.marked_source_k(delta_02, 0, aa.negative(r2)))
    long_01 = aa.source_bottom(longitudinal_mark(delta_01, 0, r0))
    long_02 = aa.source_bottom(longitudinal_mark(delta_02, 0, aa.negative(r2)))
    selected_01 = full_01 - long_01
    selected_02 = full_02 - long_02

    direct_d = aa.grassmann_exponential(aa.plane_wave_bilinear(1, q)) * aa.variable(12)
    direct_w = (
        aa.grassmann_exponential(-aa.plane_wave_bilinear(2, p))
        * aa.variable(aa.coordinate(2, 0))
    )
    reflected_w = (
        aa.grassmann_exponential(aa.plane_wave_bilinear(1, q))
        * aa.variable(aa.coordinate(1, 0))
    )
    reflected_d = aa.grassmann_exponential(-aa.plane_wave_bilinear(2, p)) * aa.variable(12)

    direct = {
        "mark01_selected": direct_rows(selected_01, unmarked_02, direct_d, direct_w, middle, r0, r1, r2),
        "mark01_longitudinal": direct_rows(long_01, unmarked_02, direct_d, direct_w, middle, r0, r1, r2),
        "mark01_full": direct_rows(full_01, unmarked_02, direct_d, direct_w, middle, r0, r1, r2),
        "mark02_selected": direct_rows(unmarked_01, selected_02, direct_d, direct_w, middle, r0, r1, r2),
        "mark02_longitudinal": direct_rows(unmarked_01, long_02, direct_d, direct_w, middle, r0, r1, r2),
        "mark02_full": direct_rows(unmarked_01, full_02, direct_d, direct_w, middle, r0, r1, r2),
    }
    reflected = {
        "mark01_selected": reflected_rows(selected_01, unmarked_02, reflected_w, reflected_d, middle, r0, r1, r2),
        "mark01_longitudinal": reflected_rows(long_01, unmarked_02, reflected_w, reflected_d, middle, r0, r1, r2),
        "mark01_full": reflected_rows(full_01, unmarked_02, reflected_w, reflected_d, middle, r0, r1, r2),
        "mark02_selected": reflected_rows(unmarked_01, selected_02, reflected_w, reflected_d, middle, r0, r1, r2),
        "mark02_longitudinal": reflected_rows(unmarked_01, long_02, reflected_w, reflected_d, middle, r0, r1, r2),
        "mark02_full": reflected_rows(unmarked_01, full_02, reflected_w, reflected_d, middle, r0, r1, r2),
    }
    wrong_reflected = {
        "mark01": reflected_rows(selected_01, unmarked_02, reflected_w, reflected_d, middle, r0, r1, r2, spinor=0),
        "mark02": reflected_rows(unmarked_01, selected_02, reflected_w, reflected_d, middle, r0, r1, r2, spinor=0),
    }

    a0, b0, c0, d0 = r0
    a2, b2, c2, d2 = r2
    det0 = a0 * d0 - b0 * c0
    det2 = a2 * d2 - b2 * c2
    expected = {
        "direct_mark01": (-b2 * det0, b2 * det0, b2 * det0, b2 * det0),
        "direct_mark02": (b0 * det2, -b0 * det2, b0 * det2, b0 * det2),
        "reflected_mark01": (-b2 * det0, -b2 * det0, -b2 * det0, b2 * det0),
        "reflected_mark02": (-b0 * det2, -b0 * det2, b0 * det2, -b0 * det2),
    }
    actual = {
        "direct_mark01": direct["mark01_selected"],
        "direct_mark02": direct["mark02_selected"],
        "reflected_mark01": reflected["mark01_selected"],
        "reflected_mark02": reflected["mark02_selected"],
    }
    assert all(
        sp.simplify(actual[key][index] - expected[key][index]) == 0
        for key in expected
        for index in range(4)
    )
    assert all(
        sp.simplify(
            sectors[f"mark{mark}_full"][index]
            - sectors[f"mark{mark}_selected"][index]
            - sectors[f"mark{mark}_longitudinal"][index]
        )
        == 0
        for sectors in (direct, reflected)
        for mark in ("01", "02")
        for index in range(4)
    )
    assert all(value == 0 for values in wrong_reflected.values() for value in values)

    bar_coefficients = {
        "DA": {
            "mark01": (b2, -b2, -b2, -b2),
            "mark02": (-b0, b0, -b0, -b0),
        },
        "AD": {
            "mark01": (b2, b2, b2, -b2),
            "mark02": (b0, b0, -b0, b0),
        },
    }
    contact_rows: list[dict[str, object]] = []
    for orientation, sectors in (("DA", direct), ("AD", reflected)):
        for mark, edge in (("01", 0), ("02", 2)):
            longitudinal = sectors[f"mark{mark}_longitudinal"]
            for index, coefficient in enumerate(bar_coefficients[orientation][f"mark{mark}"], start=1):
                # C_d=-L-alpha*r_ed^2 preserves the occurrence and edge.
                bar_square, d_square, mu_square = sp.symbols(
                    f"bar_r{edge}_sq r{edge}_d_sq mu_sq"
                )
                parent = coefficient * bar_square + longitudinal[index - 1]
                contact = -longitudinal[index - 1] - coefficient * d_square
                remainder = coefficient * mu_square
                assert sp.expand(
                    (parent + contact).subs(bar_square, d_square + mu_square)
                    - remainder
                ) == 0
                contact_rows.append(
                    {
                        "id": f"{orientation}:{mark}.{index}",
                        "orientation": orientation,
                        "mark": mark,
                        "row": index,
                        "selected_edge": f"e{edge}",
                        "selected_bar_square_coefficient": expr(coefficient),
                        "longitudinal_parent": expr(longitudinal[index - 1]),
                        "full_d_contact": expr(contact),
                        "sole_dred_remainder": expr(remainder),
                        "same_occurrence": True,
                        "same_edge": True,
                    }
                )

    return {
        "direct": {name: [expr(value) for value in values] for name, values in direct.items()},
        "reflected": {name: [expr(value) for value in values] for name, values in reflected.items()},
        "wrong_reflected_Dplus": {
            name: [expr(value) for value in values] for name, values in wrong_reflected.items()
        },
        "contact_rows": contact_rows,
        "bar_coefficient_sums": {
            orientation: {
                mark: expr(sum(values))
                for mark, values in marks.items()
            }
            for orientation, marks in bar_coefficients.items()
        },
    }


def build_payload() -> dict[str, object]:
    contract_text = CONTRACT.read_text(encoding="utf-8")
    if r"\tag{5A.52}" not in contract_text:
        raise AssertionError("authority equation (5A.52) missing")
    if r"u=\frac{V}{\sqrt2g}" not in (ROOT / "audits/step5-aa-gauge-field-normalization-factor8-exact.md").read_text(encoding="utf-8"):
        raise AssertionError("canonical V=sqrt(2)g u anchor missing")

    raw_rows = raw_port_rows()
    plus_rows = [row for row in raw_rows if row["chirality"] == "+"]
    minus_rows = [row for row in raw_rows if row["chirality"] == "-"]
    assert len(plus_rows) == len(minus_rows) == 24
    assert {tuple(row["pqrs"]) for row in plus_rows} == {
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    }
    assert all(sum(row["pqrs"]) == 1 for row in raw_rows)
    eta_e = -1
    for chirality, words in RAW_WORDS.items():
        for word in words:
            p_index, q_index, r_index, s_index = word["pqrs"]
            exponent = p_index + r_index if chirality == "+" else q_index + s_index
            authority_sign = eta_e * (-1) ** exponent
            authority_denominator = (
                256
                * sp.factorial(p_index)
                * sp.factorial(q_index)
                * sp.factorial(r_index)
                * sp.factorial(s_index)
                * (p_index + q_index + 1)
                * (r_index + s_index + 1)
            )
            assert int(word["sign"]) == authority_sign
            assert authority_denominator == 512

    g, hbar = sp.symbols("g hbar", nonzero=True)
    h = g**-2
    raw_original = h / 512
    canonical_raw = sp.simplify(raw_original * (sp.sqrt(2) * g) ** 3)
    external_linear_to_canonical = -4 * sp.sqrt(2)
    chiral_measure_and_odd_order = -4
    reduced_one_word = sp.simplify(
        canonical_raw * external_linear_to_canonical * chiral_measure_and_odd_order
    )
    plus_group = -reduced_one_word
    minus_group = reduced_one_word
    plus_action = 2 * plus_group
    minus_action = 2 * minus_group
    plus_hessian = sp.I * g / 4
    minus_hessian = -sp.I * g / 4
    tau_e = -1 / hbar

    assert canonical_raw == sp.sqrt(2) * g / 256
    assert reduced_one_word == g / 8
    assert plus_group == -g / 8
    assert minus_group == g / 8
    assert plus_action == -g / 4
    assert minus_action == g / 4

    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    aa_tgg = [
        row
        for row in census["legacy_routes"]
        if row["pair_id"] == "A__A" and row["topology"] == "TGG"
    ]
    aa_tgg_marks = sum(len(row["marked_occurrences"]) for row in aa_tgg)
    assert len(aa_tgg) == 36
    assert aa_tgg_marks == 72
    slot_assignments = len(tuple(itertools.permutations(range(3), 2)))
    slot_pairs = slot_assignments**2
    chirality_refined_rows = 2 * slot_pairs
    action_order_weight = sp.Rational(1, 2) * 2
    assert slot_assignments == 6
    assert slot_pairs == 36
    assert chirality_refined_rows == 72
    assert action_order_weight == 1

    dwords = dword_payload()

    p, q = sp.symbols("p q")
    y, z = sp.symbols("y z")
    simplex_one = sp.integrate(sp.integrate(2, (z, 0, 1 - y)), (y, 0, 1))
    simplex_y = sp.integrate(sp.integrate(2 * y, (z, 0, 1 - y)), (y, 0, 1))
    simplex_z = sp.integrate(sp.integrate(2 * z, (z, 0, 1 - y)), (y, 0, 1))
    r0_mean = -simplex_y * q - simplex_z * (p + q)
    r2_mean = r0_mean + p + q
    direct_rank_one = sp.expand(-2 * r2_mean - 2 * r0_mean)
    # Reflected engine variables are q_engine=p_A and p_engine=q_D.
    reflected_r0 = -simplex_y * p - simplex_z * (q + p)
    reflected_r2 = reflected_r0 + q + p
    reflected_rank_one = sp.expand(2 * reflected_r2 + 2 * reflected_r0)
    assert simplex_one == 1
    assert simplex_y == simplex_z == sp.Rational(1, 3)
    assert direct_rank_one == -sp.Rational(2, 3) * (p - q)
    assert reflected_rank_one == -sp.Rational(2, 3) * (p - q)

    common_prefactor = -hbar * g**2 / 16
    mu2_master = 1 / (32 * sp.pi**2)
    lambda1 = hbar * g**2 / (16 * sp.pi**2)
    component_coefficient = sp.simplify(
        common_prefactor * (-sp.Rational(2, 3)) * mu2_master / lambda1
    )
    assert component_coefficient == sp.Rational(1, 48)
    typed_vector = (
        component_coefficient,
        -component_coefficient,
        -component_coefficient,
        component_coefficient,
    )

    payload = {
        "schema": "awi.step5.aa-gauge-raw-convolution-hessian-exact.v1",
        "status": "REJECTED_FIXED_FIELD_STRENGTH_SLOT_ONLY__SUPERSEDED_BY_FULL_POLARIZED_SYMBOLIC_AUDIT",
        "scope": "FIXED_EXTERNAL_LINEAR_FIELD_STRENGTH_SLOT_ONLY",
        "rejection": {
            "reason": "The compact Hessian fixes the external background in the linear field-strength slot and omits the differentiated and undifferentiated commutator slots.",
            "counterexample": "At ell=(2,-1,1,3), N_full=6-19*i/2 while N_fixed_strength=-5.",
            "superseding_artifact": "audits/step5-aa-full-polarized-symbolic-exact.json",
        },
        "authority_equation": "Step 5A (5A.52)",
        "external_target_used": False,
        "raw_cubic_words": {
            "plus_signs": [word["sign"] for word in RAW_WORDS["+"]],
            "minus_signs": [word["sign"] for word in RAW_WORDS["-"]],
            "rows": raw_rows,
            "rows_per_chirality": 24,
            "all_rows": 48,
        },
        "canonical_reduction": {
            "h": "g^(-2)",
            "V": "sqrt(2)*g*u",
            "one_raw_word_original_V_magnitude": expr(raw_original),
            "one_raw_word_canonical_u_magnitude": expr(canonical_raw),
            "linear_field_strength_conversion": expr(external_linear_to_canonical),
            "chiral_measure_and_odd_order": expr(chiral_measure_and_odd_order),
            "one_reduced_word_magnitude": expr(reduced_one_word),
            "plus_two_cross_term_groups": [expr(plus_group), expr(plus_group)],
            "minus_two_cross_term_groups": [expr(minus_group), expr(minus_group)],
            "canonical_actions": {
                "plus": "-(g/4) int W_c^a [D_a u,u]",
                "minus": "+(g/4) int Wtilde_c_dot_a [barD^dot_a u,u]",
            },
            "action_hessians": {
                "plus": expr(plus_hessian) + "*c_UCE*W_c^E*(D_C-D_U)",
                "minus": expr(minus_hessian) + "*c_UCD*Wtilde_c^D*(barD_C-barD_U)",
            },
            "exponent_hessians": {
                "plus": expr(tau_e * plus_hessian),
                "minus": expr(tau_e * minus_hessian),
            },
        },
        "route_collapse": {
            "authority_structural_TGG_routes": len(aa_tgg),
            "authority_marked_occurrences": aa_tgg_marks,
            "slot_assignments_per_vertex": slot_assignments,
            "slot_pairs": slot_pairs,
            "chirality_refined_action_rows": chirality_refined_rows,
            "interaction_factor": expr(action_order_weight),
            "identity": "(1/2!)*(sum_rho Vplus_rho*sum_sigma Vminus_sigma + sum_sigma Vminus_sigma*sum_rho Vplus_rho)=Hplus*Hminus",
            "post_hessian_route_multiplier": 1,
            "post_hessian_mark_multiplier": 1,
        },
        "d_algebra": dwords,
        "simplex": {
            "2int_1": expr(simplex_one),
            "2int_y": expr(simplex_y),
            "2int_z": expr(simplex_z),
            "mean_r0": expr(r0_mean),
            "mean_r2": expr(r2_mean),
            "direct_DA_raw_rank_one": expr(direct_rank_one),
            "reflected_AD_raw_rank_one_after_pq_relabel": expr(reflected_rank_one),
        },
        "normalization": {
            "common_vertex_propagator_prefactor": expr(common_prefactor),
            "mu2_triangle_master": expr(mu2_master),
            "lambda1": expr(lambda1),
            "raw_component_coefficient_over_lambda1": expr(component_coefficient),
        },
        "target_blind_ordered_result": {
            "physical_status": "REJECTED_AS_FULL_AA_RESULT",
            "basis": ["DA_p", "DA_q", "AD_p", "AD_q"],
            "vector_in_lambda1_units": [expr(value) for value in typed_vector],
            "formula": "lambda1*F*[ (DA_p-DA_q)/48-(AD_p-AD_q)/48 ]",
            "epsilon_identity": "p_dot_a*A*D^dot_a=-D_dot_a*p^dot_a*A",
            "compact_DA_AD_vector": ["UNDEFINED", "UNDEFINED"],
            "first_missing_equality": "No target-blind quotient identifies or removes the independent q-derivative structures DA_q and AD_q.",
        },
        "checks": [
            "four_raw_words_per_chirality",
            "5A52_sign_and_denominator_recomputed_8_of_8",
            "six_labeled_slot_assignments_per_raw_word",
            "canonical_raw_coefficient_sqrt2_g_over_256",
            "compact_hessians_from_two_cross_term_groups",
            "36_structural_routes_and_72_marked_occurrences_not_multipliers",
            "corrected_Dminus_direct_rows_exact",
            "wrong_Dplus_reflected_rows_zero_8_of_8",
            "independent_reflected_AD_rows_exact",
            "full_equals_selected_plus_longitudinal_16_of_16",
            "occurrence_and_edge_preserving_SD_contacts_16_of_16",
            "rank_one_simplex_moments_exact",
            "extended_ordered_vector_target_blind",
            "fixed_slot_scope_rejected_as_full_polarization",
        ],
    }
    return payload


def validate(payload: dict[str, object]) -> tuple[int, int]:
    audit_text = AUDIT.read_text(encoding="utf-8")
    assertions = (
        payload["schema"] == "awi.step5.aa-gauge-raw-convolution-hessian-exact.v1",
        payload["status"]
        == "REJECTED_FIXED_FIELD_STRENGTH_SLOT_ONLY__SUPERSEDED_BY_FULL_POLARIZED_SYMBOLIC_AUDIT",
        payload["scope"] == "FIXED_EXTERNAL_LINEAR_FIELD_STRENGTH_SLOT_ONLY",
        payload["external_target_used"] is False,
        payload["raw_cubic_words"]["all_rows"] == 48,
        payload["route_collapse"]["authority_structural_TGG_routes"] == 36,
        payload["route_collapse"]["authority_marked_occurrences"] == 72,
        payload["route_collapse"]["post_hessian_route_multiplier"] == 1,
        len(payload["d_algebra"]["contact_rows"]) == 16,
        payload["target_blind_ordered_result"]["vector_in_lambda1_units"]
        == ["1/48", "-1/48", "-1/48", "1/48"],
        payload["target_blind_ordered_result"]["compact_DA_AD_vector"]
        == ["UNDEFINED", "UNDEFINED"],
        payload["target_blind_ordered_result"]["physical_status"]
        == "REJECTED_AS_FULL_AA_RESULT",
        len(payload["checks"]) == 14,
        "REJECTED_FIXED_FIELD_STRENGTH_SLOT_ONLY" in audit_text,
        r"(c_{DA,p},c_{DA,q},c_{AD,p},c_{AD,q})" in audit_text,
        "NO_ROUTE_COUNT_MULTIPLIER" in audit_text,
    )
    return sum(assertions), len(assertions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    passed, total = validate(payload)
    if args.check:
        for check in payload["checks"]:
            print(f"PASS {check}")
        print(f"SUMMARY {passed}/{total} PASS")
        return 0 if passed == total else 1
    if passed != total:
        raise AssertionError(f"validation {passed}/{total}")
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = args.output or DEFAULT_JSON
    output.write_text(rendered, encoding="utf-8")
    print(f"PASS wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
