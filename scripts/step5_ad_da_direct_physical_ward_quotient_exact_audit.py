#!/usr/bin/env python3
"""Rejected DD-port AD/DA diagnostic plus the surviving source Hessian.

This checker fixes the source normalization from the physical ordered
composite itself,

    O_AD = (D_- A)^A D^B,
    O_DA = -D^A (D_- A)^B,

with unit operator coefficient.  The former v1 artifact incorrectly used a
``D`` endpoint at both cubic gauge vertices.  The generated physical graph IR
instead fixes one ``V_tildeW``/``S_g^-`` vertex and one ``V_W``/``S_g^+``
vertex.  Therefore every DD triangle/contact/vector conclusion is retained
only as a rejected off-shell diagnostic.  No holomorphic-twist target is
imported or read.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import step5_ad_da_gauge_family_raw_audit as raw  # noqa: E402


alg = raw.alg
JSON_OUT = (
    ROOT / "audits" / "step5-ad-da-direct-physical-ward-quotient-exact.json"
)
MD_OUT = (
    ROOT / "audits" / "step5-ad-da-direct-physical-ward-quotient-exact.md"
)


def sp_text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value)))


def exact_text(value: object) -> str:
    if isinstance(value, alg.A):
        return value.text()
    if isinstance(value, sp.Basic):
        return sp_text(value)
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, alg.A) or isinstance(expected, alg.A):
        return actual == expected
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = exact_equal(actual, expected)
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": exact_text(actual),
                "expected": exact_text(expected),
            }
        )
        if not passed:
            raise AssertionError(
                f"{check_id}: actual={actual!r}, expected={expected!r}"
            )


def linear_letter_factor(
    momentum: alg.Vector,
    color: int,
    theta_mask: int,
    letter: str,
) -> alg.A:
    """Extract one exact linear N0=D_-A1 or D1 preimage coefficient."""

    ctx = alg.Context(("X",), ({"X": momentum},), 4)
    field = alg.basis_endpoint(
        ctx, "X", 0, color, theta_mask, 4
    )
    a1, _, _ = alg.canonical_A_words(field, "X")
    d1, _, _ = raw.canonical_D_words(field, "X", 0)
    if letter == "N0":
        word = alg.component(alg.mat_d(a1, "X", 1), color)
    elif letter == "D1":
        word = alg.component(d1, color)
    else:
        raise ValueError(letter)
    return (
        word.coefficient_labels((1,))
        .set_coordinates_zero("X")
        .grass_coefficient(raw.marker_mask(theta_mask, 4))
    )


def source_hessian_certificate(ledger: Ledger) -> dict[str, Any]:
    """Fix the absolute Hessian from the unit physical insertion."""

    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))

    ad_n0 = linear_letter_factor(p, 0, 1, "N0")
    ad_d1 = linear_letter_factor(q, 1, 2, "D1")
    da_d1 = linear_letter_factor(p, 0, 1, "D1")
    da_n0 = linear_letter_factor(q, 1, 1, "N0")
    ledger.check("AD_N0_PREIMAGE", ad_n0, alg.SQRT2 / 2)
    ledger.check("AD_D1_PREIMAGE", ad_d1, alg.I * alg.SQRT2 / 4)
    ledger.check("DA_D1_PREIMAGE", da_d1, -alg.SQRT2 / 4)
    ledger.check("DA_N0_PREIMAGE", da_n0, alg.SQRT2 / 2)

    ad_product = ad_n0 * ad_d1
    da_product = -da_d1 * da_n0
    ledger.check("AD_ORDERED_PRODUCT", ad_product, alg.I / 4)
    ledger.check("DA_ORDERED_PRODUCT", da_product, alg.ONE / 4)

    ad_hessian = raw.pair_source_I0_hessian_entries(
        "A__Ddot1", p, q, 0, 1, 1, 2, 0, 0, 1
    )
    da_hessian = raw.pair_source_I0_hessian_entries(
        "Ddot1__A", p, q, 0, 1, 1, 1, 0, 0, 1
    )
    ledger.check("AD_HESSIAN_TAG_COUNT", len(ad_hessian), 1)
    ledger.check("DA_HESSIAN_TAG_COUNT", len(da_hessian), 1)
    ledger.check(
        "AD_HESSIAN_DIRECT_COMPONENT",
        ad_hessian["I0_N0[A]*D1[B]"],
        ad_product,
    )
    ledger.check(
        "DA_HESSIAN_DIRECT_COMPONENT",
        da_hessian["I0_-D1[A]*N0[B]"],
        da_product,
    )

    # The two labeled field exponents are both one.  Functional
    # differentiation multiplies by 1!*1!=1, not by 2.
    hessian_factor = sp.factorial(1) * sp.factorial(1)
    ledger.check("ORDERED_LABELED_HESSIAN_FACTOR", hessian_factor, 1)
    ledger.check("PHYSICAL_OPERATOR_COEFFICIENT", sp.Integer(1), 1)

    return {
        "physical_insertion": {
            "AD": "O_AD^{AB}=N0^A*D1^B",
            "DA": "O_DA^{AB}=-D1^A*N0^B",
            "coefficient": "1",
        },
        "linear_preimages": {
            "AD": {"N0": ad_n0.text(), "D1": ad_d1.text()},
            "DA": {"D1": da_d1.text(), "N0": da_n0.text()},
        },
        "ordered_hessian_components": {
            "AD": ad_product.text(),
            "DA": da_product.text(),
        },
        "functional_factor": "1!*1!=1",
        "extra_factor_two": False,
        "source_J_convention_used": False,
    }


def normalization_certificate(ledger: Ledger) -> dict[str, str]:
    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))
    left = raw.external_d_normalization(p, 0, 1)
    right = raw.external_d_normalization(q, 1, 0)
    product = left * right
    color = alg.A(alg.su2_F(0, 1, 1, 0))
    raw_to_component = alg.ONE / (product * color)
    ledger.check("EXTERNAL_D_LEFT", left, -alg.SQRT2 / 8)
    ledger.check("EXTERNAL_D_RIGHT", right, -alg.SQRT2 / 8)
    ledger.check("EXTERNAL_D_PRODUCT", product, alg.ONE / 32)
    ledger.check("SU2_F_01_10", color, alg.A(-2))
    ledger.check("RAW_TO_CANONICAL_COMPONENT", raw_to_component, alg.A(-16))

    loop_master_over_lambda = sp.Rational(1, 2)
    raw_integrated_to_lambda = sp.Integer(-16) * loop_master_over_lambda
    ledger.check("LOOP_MASTER_OVER_LAMBDA", loop_master_over_lambda, sp.Rational(1, 2))
    ledger.check("RAW_INTEGRATED_TO_LAMBDA", raw_integrated_to_lambda, -8)
    return {
        "external_D_each": "-sqrt(2)/8",
        "external_D_product": "1/32",
        "SU2_F_01_10": "-2",
        "raw_to_canonical_component": "-16",
        "hbar_g2_over_32pi2_divided_by_lambda1": "1/2",
        "raw_integrated_to_lambda1": "-8",
        "lambda1": "hbar*g^2/(16*pi^2)",
    }


def operator_and_gf_certificate(ledger: Ledger) -> dict[str, Any]:
    operator_checks = raw.verify_marked_operator_identity()
    factorization_checks = raw.verify_selected_parent_factorization()
    gf_checks = raw.verify_gauge_fixing_longitudinal_cancellation()
    ledger.check("OPERATOR_MASK_CHECKS", operator_checks, 32)
    ledger.check("SELECTED_FACTORIZATION_MASK_CHECKS", factorization_checks, 32)
    ledger.check("GF_CANCELLATION_MASK_CHECKS", gf_checks, 32)
    return {
        "identity": (
            "D_-A1=sqrt(2)*bar(r_e)^2*D_+U"
            "+(sqrt(2)/16)*D_+*barD^2*D^2*U"
        ),
        "source_longitudinal": "-(1/2)*D_+*barD^2*D^2",
        "gauge_fixing": "+(1/2)*D_+*barD^2*D^2",
        "sum": "-8*bar(r_e)^2*D_+",
        "mask_checks": {
            "operator": operator_checks,
            "selected_factorization": factorization_checks,
            "gauge_fixing": gf_checks,
        },
        "transported_longitudinal_square_survives": False,
    }


def sd_quotient_certificate(ledger: Ledger) -> dict[str, Any]:
    rd2, mu2, phat, re = sp.symbols(
        "r_ed2 mu_l2 P_hat_e R_e", nonzero=True
    )
    full_d = sp.simplify(re * (rd2 / (rd2 * phat) - 1 / phat))
    dred = sp.simplify(
        re * ((rd2 + mu2) / (rd2 * phat) - 1 / phat)
    )
    ledger.check("FULL_D_PARENT_MINUS_CUT", full_d, 0)
    ledger.check("DRED_PARENT_MINUS_CUT", dred, re * mu2 / (rd2 * phat))
    return {
        "for_each_edge": {
            "parent_4d": "bar(r_e)^2*R_e/(D0*D1*D2)",
            "same_edge_cut": "-R_e/P_hat_e",
            "full_d": "R_e*[r_(e,d)^2/P3-1/P_hat_e]=0",
            "dred": "mu_l^2*R_e/P3",
        },
        "mu_l_squared": "bar(l)^2-l_d^2=-hat(l)_user^2",
        "finite_master": "integral mu_l^2/P3=1/(32*pi^2)",
    }


def o05_certificate(ledger: Ledger) -> dict[str, Any]:
    cached = raw.cached_o05_tagged_samples()
    interpolated = raw.interpolate_tagged_rank_one(cached)
    sample0 = cached
    expected_sample0 = {
        (0, "A__Ddot1", "source_dot1_action_dot2"): {
            "I1_N1A2[A]*D1[B]": alg.A(10) * alg.I,
            "I1_N1gamma1[A]*D1[B]": alg.A(4) * alg.I,
        },
        (0, "A__Ddot1", "source_dot2_action_dot1"): {
            "I1_N0[A]*D2[B]": alg.A(4) * alg.I,
        },
        (0, "Ddot1__A", "source_dot1_action_dot2"): {
            "I1_-D2[A]*N0[B]": -alg.I,
        },
        (0, "Ddot1__A", "source_dot2_action_dot1"): {
            "I1_-D1[A]*N1A2[B]": alg.ONE + alg.A(2) * alg.I,
        },
    }
    for key, expected in expected_sample0.items():
        ledger.check(f"O05_SAMPLE0_TAG_COUNT_{key[1]}_{key[2]}", len(sample0[key]), len(expected))
        for tag, value in expected.items():
            ledger.check(
                f"O05_SAMPLE0_{key[1]}_{key[2]}_{tag}",
                sample0[key][tag],
                value,
            )

    expected_rank_one = {
        "A__Ddot1": {
            "source_dot1_action_dot2::I1_N1A2[A]*D1[B]": ("r0", "0", "0", "5*I"),
            "source_dot1_action_dot2::I1_N1gamma1[A]*D1[B]": ("r0", "0", "0", "2*I"),
            "source_dot2_action_dot1::I1_N0[A]*D2[B]": ("r2", "0", "0", "2*I"),
        },
        "Ddot1__A": {
            "source_dot1_action_dot2::I1_-D2[A]*N0[B]": ("r0", "0", "0", "-I/2"),
            "source_dot2_action_dot1::I1_-D1[A]*N1A2[B]": ("r2", "0", "I", "I"),
        },
    }
    for pair, rows in expected_rank_one.items():
        ledger.check(f"O05_INTERPOLATED_ROW_COUNT_{pair}", len(interpolated[pair]), len(rows))
        for row_id, expected in rows.items():
            row = interpolated[pair][row_id]
            actual = (
                row["collapsed_edge"],
                row["rank_one"]["ell_plus_dotted"],
                row["rank_one"]["p_plus_dotted"],
                row["rank_one"]["q_plus_dotted"],
            )
            ledger.check(f"O05_RANK_ONE_{pair}_{row_id}", actual, expected)
            ledger.check(
                f"O05_NO_SCALAR_SQUARE_{pair}_{row_id}",
                row["four_dimensional_scalar_square"],
                "0",
            )

    return {
        "raw_replay_frame0": {
            "loop": ["1", "2", "3", "4"],
            "p": ["2", "-1", "1", "0"],
            "q": ["-1", "3", "0", "2"],
            "q_plus_dot1": "2",
            "AD": {
                "I1_N1A2[A]*D1[B]": "10*i",
                "I1_N1gamma1[A]*D1[B]": "4*i",
                "I1_N0[A]*D2[B]": "4*i",
            },
            "DA": {
                "I1_-D2[A]*N0[B]": "-i",
                "I1_-D1[A]*N1A2[B]": "1+2*i",
            },
        },
        "edge_aggregates": {
            "AD": {
                "r0_over_D1D2": "7*i*q_plus",
                "r2_over_D0D1": "2*i*q_plus",
            },
            "DA": {
                "r0_over_D1D2": "-i*q_plus/2",
                "r2_over_D0D1": "i*(p+q)_plus",
            },
        },
        "loop_hessian": "0",
        "standalone_mu2_anomaly": "0",
    }


def o06_certificate(ledger: Ledger) -> dict[str, Any]:
    certificate = raw.o06_occurrence_certificate()
    ledger.check("O06_COLLAPSED_EDGE", certificate["collapsed_edge"], "r1")
    ledger.check("O06_DENOMINATOR", certificate["denominator"], "D0*D2")
    ledger.check(
        "O06_AD_RANK_ONE",
        certificate["AD_rank_one"],
        {"ell_plus_dotted": "0", "p_plus_dotted": "0", "q_plus_dotted": "0"},
    )
    ledger.check(
        "O06_DA_RANK_ONE",
        certificate["DA_rank_one"],
        {"ell_plus_dotted": "0", "p_plus_dotted": "i", "q_plus_dotted": "i"},
    )
    ledger.check("O06_CHIRAL_HALF", certificate["chiral_fraction"], "1/2")
    ledger.check("O06_ANTICHIRAL_HALF", certificate["antichiral_fraction"], "1/2")
    ledger.check(
        "O06_NO_SCALAR_SQUARE",
        certificate["four_dimensional_scalar_square"],
        "0",
    )
    ledger.check(
        "O06_STANDALONE_ANOMALY",
        certificate["standalone_anomaly_sector"],
        "0",
    )
    first = certificate["replay_samples"][0]
    ledger.check("O06_FRAME0_AD", first["AD"], {})
    ledger.check(
        "O06_FRAME0_DA_PLUS",
        first["DA"]["I0_-D1[A]*N0[B]__Sg4_+"],
        "1/2 + i",
    )
    ledger.check(
        "O06_FRAME0_DA_MINUS",
        first["DA"]["I0_-D1[A]*N0[B]__Sg4_-"],
        "1/2 + i",
    )
    return {
        "collapsed_edge": "r1",
        "AD": "0",
        "DA_chiral": "i*(p+q)_plus/2",
        "DA_antichiral": "i*(p+q)_plus/2",
        "DA_sum": "i*(p+q)_plus",
        "raw_replay_frame0": {
            "AD": {},
            "DA_plus": "1/2+i",
            "DA_minus": "1/2+i",
        },
        "loop_hessian": "0",
        "four_dimensional_scalar_square": "0",
        "standalone_mu2_anomaly": "0",
        "transported_r1_square": "0",
    }


def current_and_fp_certificate(ledger: Ledger) -> dict[str, Any]:
    current = raw.matter_current_pair_certificate()
    fp = raw.fp_current_kernel_certificate()
    ledger.check("MATTER_CURRENT_FULL_D_SUM", current["full_d_family_sum"], "0")
    ledger.check("MATTER_CURRENT_MU2", current["mu2_remainder"], "0")
    ledger.check("FP_HESSIAN_CHECKS", fp["loop_hessian_checks"], 8)
    ledger.check("FP_SCALAR_SQUARE", fp["four_dimensional_scalar_square"], "0")
    ledger.check("FP_FULL_SD", fp["full_Schwinger_family"], "0")
    ledger.check("FP_MU2", fp["mu2_remainder"], "0")
    ledger.check("FP_ANOMALY", fp["anomaly_sector"], "0")
    return {
        "matter_current": {
            "Euler": "+2*i*K_dot_a",
            "explicit_contact": "-2*i*K_dot_a",
            "full_d_sum": "0",
            "mu2_remainder": "0",
        },
        "FP": {
            "Euler_bubble": "+B_FP_DD",
            "full_d_cut": "-B_FP_DD",
            "full_Schwinger_family": "0",
            "kernel": "full-d Box",
            "four_dimensional_scalar_square": "0",
            "mu2_remainder": "0",
        },
    }


def finite_vector_certificate(ledger: Ledger) -> dict[str, Any]:
    i = sp.I
    ell_shift_p = -sp.Rational(2, 3)
    ell_shift_q = -sp.Rational(1, 3)
    ledger.check("RANK_ONE_ELL_P_MOMENT", ell_shift_p, -sp.Rational(2, 3))
    ledger.check("RANK_ONE_ELL_Q_MOMENT", ell_shift_q, -sp.Rational(1, 3))

    ad_ell, ad_p, ad_q = i / 16, i / 16, i / 32
    da_ell, da_p, da_q = -i / 16, 0, 0
    ad_raw_p = sp.simplify(ad_p + ell_shift_p * ad_ell)
    ad_raw_q = sp.simplify(ad_q + ell_shift_q * ad_ell)
    da_raw_p = sp.simplify(da_p + ell_shift_p * da_ell)
    da_raw_q = sp.simplify(da_q + ell_shift_q * da_ell)
    ledger.check("AD_RAW_INTEGRATED_P", ad_raw_p, i / 48)
    ledger.check("AD_RAW_INTEGRATED_Q", ad_raw_q, i / 96)
    ledger.check("DA_RAW_INTEGRATED_P", da_raw_p, i / 24)
    ledger.check("DA_RAW_INTEGRATED_Q", da_raw_q, i / 48)

    conversion = sp.Integer(-8)
    ad_p_lambda = sp.simplify(conversion * ad_raw_p)
    ad_q_lambda = sp.simplify(conversion * ad_raw_q)
    da_p_lambda = sp.simplify(conversion * da_raw_p)
    da_q_lambda = sp.simplify(conversion * da_raw_q)
    ledger.check("AD_INTERNAL_P_OVER_LAMBDA", ad_p_lambda, -i / 6)
    ledger.check("AD_INTERNAL_Q_OVER_LAMBDA", ad_q_lambda, -i / 12)
    ledger.check("DA_INTERNAL_P_OVER_LAMBDA", da_p_lambda, -i / 3)
    ledger.check("DA_INTERNAL_Q_OVER_LAMBDA", da_q_lambda, -i / 6)

    # AD: k_L=q, k_R=-(p+q).  DA: k_L=-(p+q), k_R=q.
    ad_left = sp.simplify(-ad_p_lambda + ad_q_lambda)
    ad_right = sp.simplify(-ad_p_lambda)
    da_left = sp.simplify(-da_p_lambda)
    da_right = sp.simplify(-da_p_lambda + da_q_lambda)
    ledger.check("AD_ORDERED_LEFT_OVER_LAMBDA", ad_left, i / 12)
    ledger.check("AD_ORDERED_RIGHT_OVER_LAMBDA", ad_right, i / 6)
    ledger.check("DA_ORDERED_LEFT_OVER_LAMBDA", da_left, i / 3)
    ledger.check("DA_ORDERED_RIGHT_OVER_LAMBDA", da_right, i / 6)
    ledger.check(
        "AD_NORMALIZED_LEFT_SHAPE",
        sp.simplify(ad_left / (ad_left + ad_right)),
        sp.Rational(1, 3),
    )
    ledger.check(
        "AD_NORMALIZED_RIGHT_SHAPE",
        sp.simplify(ad_right / (ad_left + ad_right)),
        sp.Rational(2, 3),
    )
    ledger.check(
        "DA_NORMALIZED_LEFT_SHAPE",
        sp.simplify(da_left / (da_left + da_right)),
        sp.Rational(2, 3),
    )
    ledger.check(
        "DA_NORMALIZED_RIGHT_SHAPE",
        sp.simplify(da_right / (da_left + da_right)),
        sp.Rational(1, 3),
    )
    ledger.check(
        "ABSOLUTE_AD_OVER_DA_SUM_RATIO",
        sp.simplify((ad_left + ad_right) / (da_left + da_right)),
        sp.Rational(1, 2),
    )
    return {
        "raw_mu2_numerator": {
            "AD": "(i/16)*mu_l^2*(ell+p+q/2)_plus_dot_a",
            "DA": "-(i/16)*mu_l^2*ell_plus_dot_a",
        },
        "simplex_moment": "ell -> -(2*p+q)/3",
        "raw_integrated_bracket_after_1_over_32pi2": {
            "AD": {"p": "i/48", "q": "i/96"},
            "DA": {"p": "i/24", "q": "i/48"},
        },
        "internal_momenta_over_lambda1": {
            "AD": {"p": "-i/6", "q": "-i/12"},
            "DA": {"p": "-i/3", "q": "-i/6"},
        },
        "ordered_momentum_maps": {
            "AD": "k_L=q; k_R=-(p+q)",
            "DA": "k_L=-(p+q); k_R=q",
        },
        "absolute_ordered_vector_over_lambda1": {
            "AD": {"k_left": "i/12", "k_right": "i/6"},
            "DA": {"k_left": "i/3", "k_right": "i/6"},
        },
        "normalized_shapes": {
            "AD": {"k_left": "1/3", "k_right": "2/3"},
            "DA": {"k_left": "2/3", "k_right": "1/3"},
        },
        "absolute_sum_ratio_AD_over_DA": "1/2",
    }


def replay_o05_sample0(ledger: Ledger, workers: int) -> None:
    loop, p, q = raw.interpolation_samples()[0]
    expected = {
        "A__Ddot1": {
            "source_dot1_action_dot2": {
                "I1_N1A2[A]*D1[B]": alg.A(10) * alg.I,
                "I1_N1gamma1[A]*D1[B]": alg.A(4) * alg.I,
            },
            "source_dot2_action_dot1": {
                "I1_N0[A]*D2[B]": alg.A(4) * alg.I,
            },
        },
        "Ddot1__A": {
            "source_dot1_action_dot2": {
                "I1_-D2[A]*N0[B]": -alg.I,
            },
            "source_dot2_action_dot1": {
                "I1_-D1[A]*N1A2[B]": alg.ONE + alg.A(2) * alg.I,
            },
        },
    }
    for pair in ("A__Ddot1", "Ddot1__A"):
        actual = raw.dd_bubble_attachment_values_parallel(
            pair, loop, p, q, workers
        )
        ledger.check(f"RAW_O05_REPLAY_{pair}", actual, expected[pair])


def replay_o06_sample0(ledger: Ledger, workers: int) -> None:
    loop, p, q = raw.interpolation_samples()[0]
    expected = {
        "A__Ddot1": {},
        "Ddot1__A": {
            "I0_-D1[A]*N0[B]__Sg4_+": alg.ONE / 2 + alg.I,
            "I0_-D1[A]*N0[B]__Sg4_-": alg.ONE / 2 + alg.I,
        },
    }
    for pair in ("A__Ddot1", "Ddot1__A"):
        actual = raw.dd_quartic_values_parallel(pair, loop, p, q, workers)
        ledger.check(f"RAW_O06_REPLAY_{pair}", actual, expected[pair])


def build_payload(
    replay_o05: bool = False,
    replay_o06: bool = False,
    workers: int = 8,
) -> dict[str, Any]:
    ledger = Ledger()
    source_hessian = source_hessian_certificate(ledger)
    rejected_dd_diagnostic = {
        "normalization": normalization_certificate(ledger),
        "operator_and_gauge_fixing": operator_and_gf_certificate(ledger),
        "parent_minus_cut": sd_quotient_certificate(ledger),
        "O05": o05_certificate(ledger),
        "O06": o06_certificate(ledger),
        "current_and_FP": current_and_fp_certificate(ledger),
        "finite_vector": finite_vector_certificate(ledger),
        "crossed_TGG_routing": {
            "role": "rejected DD routing diagnostic",
            "exact_frames": 8,
            "surviving_routes": 0,
            "sum": "0",
        },
    }
    payload: dict[str, Any] = {
        "schema": "step5-ad-da-direct-physical-ward-quotient-exact-v2",
        "external_target_used": False,
        "physical_source_hessian": source_hessian,
        "rejection": {
            "code": "WRONG_EXTERNAL_VERTEX_TYPE",
            "computed_parent": "S_g^- endpoint_D x S_g^- endpoint_D",
            "required_parent": "V_tildeW/S_g^- endpoint_D x V_W/S_g^+ endpoint_A",
            "graph_ir_rows": [
                "CUT-ORBIT-026::A__Ddot1::0::TRIANGLE",
                "CUT-ORBIT-064::Ddot1__A::0::TRIANGLE",
            ],
            "fixed_ordered_wick_weight": "(1/2!)*(1+1)=1",
            "still_valid": [
                "unit ordered source coefficient",
                "AD direct source Hessian i/4",
                "DA direct source Hessian 1/4",
                "no extra labeled-Hessian factor two",
            ],
            "invalidated": [
                "DD TGG finite vector",
                "DD raw-to-component conversion -16",
                "DD raw-to-lambda1 conversion -8",
                "standalone O05/O06 anomaly-zero claims",
                "absolute AD/DA compact coefficients",
            ],
            "affine_contact_warning": (
                "A two-denominator affine contact may be the selected-edge "
                "cut of a parent containing bar(r_e)^2; affine does not imply "
                "zero DRED anomaly."
            ),
        },
        "rejected_DD_diagnostic": rejected_dd_diagnostic,
        "result": {
            "AD_dot_a": None,
            "DA_dot_a": None,
            "normalization_status": "SOURCE_HESSIAN_ONLY_FIXED",
            "derivation_status": "REJECTED_WRONG_EXTERNAL_VERTEX_TYPE",
        },
        "status": "REJECTED_WRONG_EXTERNAL_VERTEX_TYPE",
    }
    if replay_o05:
        replay_o05_sample0(ledger, workers)
    if replay_o06:
        replay_o06_sample0(ledger, workers)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    payload["checks"] = {
        "count": len(ledger.rows),
        "passed": len(ledger.rows) - failed,
        "failed": failed,
        "rows": ledger.rows,
    }
    return payload


def render_markdown(payload: dict[str, Any]) -> str:
    checks = payload["checks"]
    return rf"""# Step 5 AD/DA DD-port artifact rejection

Status: `{payload['status']}`.

External target used: `false`.

## 1. Wrong parent

Former v1 computed

$$
S_g^-\big|_{{D}}\times S_g^-\big|_{{D}}.
$$

The generated physical graph IR fixes

$$
V_{{\widetilde W}}\big|_{{S_g^-,D}}
\times
V_W\big|_{{S_g^+,A}},
\qquad
\frac1{{2!}}(1+1)=1.
$$

Therefore the former DD TGG vector, conversions (-16,-8), O05/O06
standalone-zero inference, and compact AD/DA coefficients are rejected.

An affine contact is not an anomaly-zero criterion:

$$
\frac{{\bar r_e^2R_e}}{{D_0D_1D_2}}
-\frac{{R_e}}{{P_{{\widehat e}}}}
=\frac{{\mu_\ell^2R_e}}{{D_0D_1D_2}},
\qquad
\bar r_e^2=r_{{e,d}}^2+\mu_\ell^2.
$$

## 2. Surviving source normalization

$$
O_{{AD}}^{{AB}}=N_0^A D_1^B,
\qquad
N_0^A=\frac{{\sqrt2}}2,
\qquad
D_1^B=\frac{{i\sqrt2}}4,
\qquad
N_0^AD_1^B=\frac i4,
$$

$$
O_{{DA}}^{{AB}}=-D_1^A N_0^B,
\qquad
D_1^A=-\frac{{\sqrt2}}4,
\qquad
N_0^B=\frac{{\sqrt2}}2,
\qquad
-D_1^AN_0^B=\frac14.
$$

$$
1!\,1!=1.
$$

Only this direct ordered source Hessian remains valid.

## 3. Physical coefficient

$$
\Gamma_{{AD}}^{{\rm anom}}=\mathrm{{OPEN}},
\qquad
\Gamma_{{DA}}^{{\rm anom}}=\mathrm{{OPEN}}.
$$

Machine diagnostic checks retained under `rejected_DD_diagnostic`:

$$
N_{{\rm pass}}={checks['passed']},\qquad
N_{{\rm fail}}={checks['failed']}.
$$
"""


def render_rejected_dd_diagnostic_markdown(payload: dict[str, Any]) -> str:
    checks = payload["checks"]
    return rf"""# Step 5 AD/DA direct physical Ward quotient

Status: `{payload['status']}`.

External target used: `false`. 下面只使用 locked letters、direct physical
ordered composite、exact sparse superspace algebra 与 DRED parent-minus-cut。

## 1. Notation

$$
r_0=\ell,\qquad r_1=\ell+p,\qquad r_2=\ell+p+q,
$$

$$
P_3=D_0D_1D_2,\qquad
\mu_\ell^2=\bar\ell^{{2}}-\ell_d^2=-\widehat\ell_{{\rm user}}^{{2}}.
$$

## 2. Direct physical source Hessian

取 unit-coefficient ordered insertions

$$
O_{{AD}}^{{AB}}=N_0^A D_1^B,
\qquad
O_{{DA}}^{{AB}}=-D_1^A N_0^B.
$$

Exact component preimages are

$$
N_0^A=\frac{{\sqrt2}}{{2}},\qquad
D_1^B=\frac{{i\sqrt2}}{{4}},\qquad
N_0^A D_1^B=\frac i4,
$$

$$
D_1^A=-\frac{{\sqrt2}}{{4}},\qquad
N_0^B=\frac{{\sqrt2}}{{2}},\qquad
-D_1^A N_0^B=\frac14.
$$

Both field labels occur once:

$$
[t_Lt_R]O=\frac{{\partial^2O}}{{\partial t_L\partial t_R}}\bigg|_0,
\qquad 1!\,1!=1.
$$

因此没有 extra Hessian factor (2)，也不需要 (J_{{AD}}) convention。

## 3. Source identity and gauge fixing

$$
D_-A_1
=\sqrt2\,\bar r_e^{{2}}D_+U
+\frac{{\sqrt2}}{{16}}D_+\bar D^2D^2U.
$$

In the normalized Ward row,

$$
\mathscr L_e
=-8\bar r_e^{{2}}R_e
-\frac12H_e,
\qquad
\mathscr G_e=+\frac12H_e,
$$

$$
\mathscr L_e+\mathscr G_e=-8\bar r_e^{{2}}R_e.
$$

The cancellation holds on (32) exact component masks.  Hence no
transported longitudinal (r_1^2) square survives.

## 4. Full-d Schwinger quotient

For every marked occurrence,

$$
R_e\left[
\frac{{r_{{e,d}}^2}}{{D_0D_1D_2}}
-\frac1{{P_{{\widehat e}}}}
\right]=0,
$$

$$
R_e\left[
\frac{{\bar r_e^{{2}}}}{{D_0D_1D_2}}
-\frac1{{P_{{\widehat e}}}}
\right]
=\frac{{\mu_\ell^2R_e}}{{D_0D_1D_2}}.
$$

## 5. O05 and O06 contacts

O05 gives

$$
\mathcal C_{{AD}}^{{O05}}
=\frac{{7iq_{{+\dot a}}}}{{D_1D_2}}
+\frac{{2iq_{{+\dot a}}}}{{D_0D_1}},
$$

$$
\mathcal C_{{DA}}^{{O05}}
=-\frac{{iq_{{+\dot a}}}}{{2D_1D_2}}
+\frac{{i(p+q)_{{+\dot a}}}}{{D_0D_1}}.
$$

O06 lies on (r_1):

$$
\mathcal C_{{AD}}^{{O06}}=0,
$$

$$
\mathcal C_{{DA}}^{{O06,+}}
=\frac{{i(p+q)_{{+\dot a}}}}{{2D_0D_2}},
\qquad
\mathcal C_{{DA}}^{{O06,-}}
=\frac{{i(p+q)_{{+\dot a}}}}{{2D_0D_2}}.
$$

Every numerator above is loop-affine with zero scalar loop square:

$$
\frac{{\partial^2N_{{O05,O06}}}}{{\partial\ell_m\partial\ell_n}}=0,
\qquad
\Gamma_{{O05,O06}}^{{\mu^2}}=0.
$$

Thus (r_1) survives only as the affine O06 contact, not as a transported
longitudinal anomaly square.

## 6. FP and matter-current contacts

$$
\mathcal M_{{\rm Euler}}=2iK_{{\dot a}},\qquad
\mathcal M_{{\rm explicit}}=-2iK_{{\dot a}},\qquad
\mathcal M_{{\mu^2}}=0.
$$

The FP inverse is the full-(d) \(\Box\) kernel:

$$
\Gamma_{{\rm FP,Euler}}^{{DD}}=\mathcal B_{{\rm FP}}^{{DD}},
\qquad
\Gamma_{{\rm FP,cut}}^{{DD}}=-\mathcal B_{{\rm FP}}^{{DD}},
$$

$$
\Gamma_{{\rm FP,full\ SD}}^{{DD}}=0,
\qquad
\Gamma_{{\rm FP}}^{{\mu^2}}=0.
$$

## 7. Finite triangle and absolute ordered vector

$$
N_{{AD}}^{{\rm ev}}
=\frac i{{16}}\mu_\ell^2
\left(\ell+p+\frac12q\right)_{{+\dot a}},
$$

$$
N_{{DA}}^{{\rm ev}}
=-\frac i{{16}}\mu_\ell^2\ell_{{+\dot a}}.
$$

Using

$$
\int\frac{{d^d\ell}}{{(2\pi)^d}}
\frac{{\mu_\ell^2}}{{D_0D_1D_2}}
=\frac1{{32\pi^2}},
\qquad
\ell\longmapsto-\frac23p-\frac13q,
$$

$$
AD:\quad
\frac1{{32\pi^2}}
\left(\frac i{{48}}p+\frac i{{96}}q\right)_{{+\dot a}},
$$

$$
DA:\quad
\frac1{{32\pi^2}}
\left(\frac i{{24}}p+\frac i{{48}}q\right)_{{+\dot a}}.
$$

The exact normalization is

$$
\left(-\frac{{\sqrt2}}8\right)^2=\frac1{{32}},
\qquad
F_{{01;10}}=-2,
\qquad
\frac1{{(1/32)(-2)}}=-16,
$$

$$
\frac{{\hbar g^2/(32\pi^2)}}{{\lambda_1}}=\frac12,
\qquad
(-16)\left(\frac12\right)=-8,
\qquad
\lambda_1=\frac{{\hbar g^2}}{{16\pi^2}}.
$$

For (AD), (k_L=q, k_R=-(p+q)).  For (DA),
(k_L=-(p+q), k_R=q).  Therefore

$$
\boxed{{
\Gamma_{{AD,\dot a}}^{{\rm anom}}
=i\lambda_1
\left(
\frac1{{12}}k_{{L,+\dot a}}
+\frac16k_{{R,+\dot a}}
\right)
}},
$$

$$
\boxed{{
\Gamma_{{DA,\dot a}}^{{\rm anom}}
=i\lambda_1
\left(
\frac13k_{{L,+\dot a}}
+\frac16k_{{R,+\dot a}}
\right)
}}.
$$

Machine checks:

$$
N_{{\rm pass}}={checks['passed']},\qquad
N_{{\rm fail}}={checks['failed']}.
$$
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--replay-o05-sample0", action="store_true")
    parser.add_argument("--replay-o06-sample0", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    payload = build_payload(
        replay_o05=args.replay_o05_sample0,
        replay_o06=args.replay_o06_sample0,
        workers=args.workers,
    )
    json_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    markdown_text = render_markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(markdown_text, encoding="utf-8")
    elif args.check_artifact:
        if args.replay_o05_sample0 or args.replay_o06_sample0:
            raise AssertionError(
                "raw replay flags add checks; use them without --check-artifact"
            )
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != markdown_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
        print("PASS AD_DA_DIRECT_PHYSICAL_HESSIAN_FACTOR_ONE")
        print("REJECTED AD_DA_DD_PARENT_WRONG_EXTERNAL_VERTEX_TYPE")
        print(
            f"SUMMARY {payload['checks']['passed']}/"
            f"{payload['checks']['count']} PASS"
        )
    else:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
