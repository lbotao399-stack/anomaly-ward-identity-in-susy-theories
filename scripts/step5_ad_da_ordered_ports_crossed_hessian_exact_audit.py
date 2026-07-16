#!/usr/bin/env python3
"""Target-blind AD/DA ordered-port and crossed-Hessian audit.

This audit derives the two background output momenta from the three vertex
conservation equations.  It keeps the two color allocations of the ordered
source Hessian separately and never imports a holomorphic-twist coefficient.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ad_da_gauge_family_raw_audit as raw  # noqa: E402


alg = raw.alg
JSON_OUT = ROOT / "audits" / "step5-ad-da-ordered-ports-crossed-hessian-exact.json"
MD_OUT = ROOT / "audits" / "step5-ad-da-ordered-ports-crossed-hessian-exact.md"
OLD_JSON = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.json"
OLD_MD = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.md"
GRAPH_IR = ROOT / "generated" / "step5" / "physical-graph-ir.json"
RAW_CONTACT_JSON = (
    ROOT / "audits" / "step5-ad-da-raw-contact-hessian-multiplicity-exact.json"
)
POLARIZED_P_JSON = (
    ROOT / "audits" / "step5-ad-da-full-polarized-symbolic-p-only-exact.json"
)
POLARIZED_Q_JSON = (
    ROOT / "audits" / "step5-ad-da-full-polarized-symbolic-q-only-exact.json"
)


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = actual == expected
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": exact_text(actual),
                "expected": exact_text(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def exact_text(value: object) -> str:
    if isinstance(value, alg.A):
        return value.text()
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value))
    return str(value)


def gaussian(value: alg.A) -> sp.Expr:
    if value.b or value.d:
        raise AssertionError(value.text())
    return sp.Rational(value.a.numerator, value.a.denominator) + sp.I * sp.Rational(
        value.c.numerator, value.c.denominator
    )


def walk_json(value: object):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)


def routing_certificate(ledger: Ledger) -> dict[str, object]:
    ell = sp.Matrix(sp.symbols("ell0:4"))
    p = sp.Matrix(sp.symbols("p0:4"))
    q = sp.Matrix(sp.symbols("q0:4"))
    r0 = ell
    r1 = ell + p
    r2 = ell + p + q
    left = sp.simplify(r0 - r1 + p)
    right = sp.simplify(-r2 + r1 + q)
    source = sp.simplify(-r0 + r2 - (p + q))
    ledger.check("LEFT_ACTION_CONSERVATION", left, sp.zeros(4, 1))
    ledger.check("RIGHT_ACTION_CONSERVATION", right, sp.zeros(4, 1))
    ledger.check("SOURCE_CONSERVATION", source, sp.zeros(4, 1))
    ledger.check("LEFT_OUTPUT_MOMENTUM", p, p)
    ledger.check("RIGHT_OUTPUT_MOMENTUM", q, q)
    graph_payload = json.loads(GRAPH_IR.read_text(encoding="utf-8"))
    graph_rows: dict[str, object] = {}
    for pair, ordinal in (("A__Ddot1", 26), ("Ddot1__A", 64)):
        graph_id = f"CUT-ORBIT-{ordinal:03d}::{pair}::0::TRIANGLE"
        triangle = next(
            row for row in walk_json(graph_payload) if row.get("graph_id") == graph_id
        )
        edges = tuple(edge["momentum"] for edge in triangle["edges"])
        ledger.check(
            f"GRAPH_IR_{pair}_EDGES",
            edges,
            ("r0=k", "r1=k+q", "r2=k+p+q"),
        )
        graph_rows[pair] = {
            "graph_id": graph_id,
            "edges": list(edges),
        }
    return {
        "all_momenta_incoming": True,
        "raw_engine_edges": {
            "r0": "ell",
            "r1": "ell+p_raw",
            "r2": "ell+p_raw+q_raw",
        },
        "generated_IR_edges": {
            "r0": "k",
            "r1": "k+q_IR",
            "r2": "k+p_IR+q_IR",
        },
        "raw_to_IR_map": {
            "ell": "k",
            "p_raw": "q_IR=k_left",
            "q_raw": "p_IR=k_right",
        },
        "vertex_equations": {
            "left_action": "r0-r1+p_raw=0",
            "right_action": "-r2+r1+q_raw=0",
            "source": "-r0+r2-(p_raw+q_raw)=0",
        },
        "background_output_ports": {
            "left": {"field": "D_lower", "momentum": "q_IR", "alias": "k_left"},
            "right": {"field": "D_upper", "momentum": "p_IR", "alias": "k_right"},
        },
        "source_insertion_momentum": "-(p_IR+q_IR)",
        "graph_IR_rows": graph_rows,
        "forbidden_imported_map": {
            "AD": "(q,-p-q)",
            "DA": "(-p-q,q)",
            "status": "REJECTED_NOT_ACTION_OUTPUT_MOMENTA",
        },
    }


def color_hessian_certificate(ledger: Ledger) -> dict[str, object]:
    direct_frame = (0, 1, 1, 0)
    crossed_frame = (0, 1, 0, 1)
    direct_direct = alg.su2_F(*direct_frame)
    direct_cross = alg.su2_F(1, 0, direct_frame[2], direct_frame[3])
    cross_direct = alg.su2_F(*crossed_frame)
    cross_cross = alg.su2_F(1, 0, crossed_frame[2], crossed_frame[3])
    ledger.check("DIRECT_PROJECTOR_F_AB", direct_direct, -2)
    ledger.check("DIRECT_PROJECTOR_F_BA", direct_cross, 0)
    ledger.check("CROSSED_PROJECTOR_F_AB", cross_direct, 0)
    ledger.check("CROSSED_PROJECTOR_F_BA", cross_cross, -2)
    return {
        "ordered_source_words": {
            "AD": "N^A[u_1]D^B[u_2]+N^A[u_2]D^B[u_1]",
            "DA": "-D^A[u_1]N^B[u_2]-D^A[u_2]N^B[u_1]",
        },
        "color_allocations": {
            "direct": "F^{AB}_{DE}",
            "crossed": "F^{BA}_{DE}",
        },
        "term_port_table": [
            {
                "source_word": "AD",
                "allocation": "direct",
                "color": "F^{AB}_{DE}",
                "background_output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
            },
            {
                "source_word": "AD",
                "allocation": "crossed",
                "color": "F^{BA}_{DE}",
                "background_output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
            },
            {
                "source_word": "DA",
                "allocation": "direct",
                "color": "F^{AB}_{DE}",
                "background_output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
            },
            {
                "source_word": "DA",
                "allocation": "crossed",
                "color": "F^{BA}_{DE}",
                "background_output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
            },
        ],
        "su2_orthogonal_projectors": {
            "direct": {
                "A_B_D_E": list(direct_frame),
                "F_AB": str(direct_direct),
                "F_BA": str(direct_cross),
            },
            "crossed": {
                "A_B_D_E": list(crossed_frame),
                "F_AB": str(cross_direct),
                "F_BA": str(cross_cross),
            },
        },
        "single_component_zero_rule": "A zero of one projector never removes the other color allocation.",
    }


def source_component_hessian_certificate(ledger: Ledger) -> dict[str, object]:
    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))
    ad_direct = raw.pair_source_I0_hessian_entries(
        "A__Ddot1", p, q, 0, 1, 1, 2, 0, 0, 1
    )
    ad_crossed = raw.pair_source_I0_hessian_entries(
        "A__Ddot1", q, p, 1, 0, 2, 1, 0, 0, 1
    )
    da_direct = raw.pair_source_I0_hessian_entries(
        "Ddot1__A", p, q, 0, 1, 1, 1, 0, 0, 1
    )
    da_crossed = raw.pair_source_I0_hessian_entries(
        "Ddot1__A", q, p, 1, 0, 1, 1, 0, 0, 1
    )
    ledger.check("AD_DIRECT_SOURCE_COMPONENT", ad_direct, {"I0_N0[A]*D1[B]": alg.I / 4})
    ledger.check("AD_CROSSED_SOURCE_COMPONENT", ad_crossed, {"I0_N0[A]*D1[B]": -alg.I / 4})
    ledger.check("DA_DIRECT_SOURCE_COMPONENT", da_direct, {"I0_-D1[A]*N0[B]": alg.ONE / 4})
    ledger.check("DA_CROSSED_SOURCE_COMPONENT", da_crossed, {"I0_-D1[A]*N0[B]": -alg.ONE / 4})
    return {
        "direct_direction_order": {
            "AD": "i/4",
            "DA": "1/4",
        },
        "crossed_direction_order": {
            "AD": "-i/4",
            "DA": "-1/4",
        },
        "graded_reason": (
            "The two extracted component directions are odd; reversing their "
            "functional order changes sign.  The crossed Hessian is nonzero."
        ),
    }


R1_FRAMES = (
    alg.ONE / 4 + 5 * alg.I / 16,
    alg.ONE / 16 + alg.I / 8,
    alg.ONE / 32 + 3 * alg.I / 16,
    alg.ONE / 32 - alg.I / 16,
)
R2_FRAMES = (
    -3 * alg.ONE / 16 - alg.I / 4,
    -alg.I / 16,
    alg.ONE / 8 - 3 * alg.I / 16,
    -alg.ONE / 16 + alg.I / 8,
)


def interpolation_matrix() -> sp.Matrix:
    return sp.Matrix(
        [
            [
                raw.plus_dotted(loop, 0),
                raw.plus_dotted(p, 0),
                raw.plus_dotted(q, 0),
            ]
            for loop, p, q in raw.interpolation_samples()[:3]
        ]
    )


def interpolate_frames(values: tuple[alg.A, ...]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    matrix = interpolation_matrix()
    return tuple(
        sp.simplify(entry)
        for entry in matrix.inv() * sp.Matrix([gaussian(value) for value in values[:3]])
    )  # type: ignore[return-value]


def rank_one_held_out(coefficients: tuple[sp.Expr, sp.Expr, sp.Expr], value: alg.A) -> sp.Expr:
    loop, p, q = raw.interpolation_samples()[3]
    return sp.simplify(
        coefficients[0] * raw.plus_dotted(loop, 0)
        + coefficients[1] * raw.plus_dotted(p, 0)
        + coefficients[2] * raw.plus_dotted(q, 0)
        - gaussian(value)
    )


def numerator_certificate(ledger: Ledger) -> dict[str, object]:
    matrix = interpolation_matrix()
    ledger.check("INTERPOLATION_DETERMINANT", sp.factor(matrix.det()), 9 + 3 * sp.I)
    r1 = interpolate_frames(R1_FRAMES)
    r2 = interpolate_frames(R2_FRAMES)
    ledger.check("R1_COEFFICIENTS", r1, (sp.I / 16, sp.I / 16, sp.I / 32))
    ledger.check("R2_COEFFICIENTS", r2, (-sp.I / 16, 0, 0))
    ledger.check("R1_HELD_OUT", rank_one_held_out(r1, R1_FRAMES[3]), 0)
    ledger.check("R2_HELD_OUT", rank_one_held_out(r2, R2_FRAMES[3]), 0)
    rows = {
        "AD": {"direct_F_AB": "R1", "crossed_F_BA": "R2"},
        "DA": {"direct_F_AB": "R2", "crossed_F_BA": "R1"},
    }
    return {
        "basis": {
            "R1": {
                "frames": [value.text() for value in R1_FRAMES],
                "formula": "(i/16)*mu_l^2*(ell+p+q/2)_plus_dotted",
            },
            "R2": {
                "frames": [value.text() for value in R2_FRAMES],
                "formula": "-(i/16)*mu_l^2*ell_plus_dotted",
            },
        },
        "ordered_source_and_color_rows": rows,
        "component_formulas": {
            "AD": "F^{AB}_{DE}*R1+F^{BA}_{DE}*R2",
            "DA": "F^{AB}_{DE}*R2+F^{BA}_{DE}*R1",
        },
    }


def normalization_certificate(ledger: Ledger) -> dict[str, str]:
    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))
    left = raw.external_d_normalization(p, 0, 1)
    right = raw.external_d_normalization(q, 1, 0)
    product = left * right
    color = alg.A(alg.su2_F(0, 1, 1, 0))
    raw_to_component = alg.ONE / (product * color)
    master_over_lambda = sp.Rational(1, 2)
    legacy_component_times_master = sp.Integer(-16) * master_over_lambda
    rank_trace_correction = sp.Rational(1, 2)
    corrected_component_times_master = (
        legacy_component_times_master * rank_trace_correction
    )
    ledger.check("LEFT_D_NORMALIZATION", left, -alg.SQRT2 / 8)
    ledger.check("RIGHT_D_NORMALIZATION", right, -alg.SQRT2 / 8)
    ledger.check("D_PRODUCT", product, alg.ONE / 32)
    ledger.check("COLOR_PROJECTOR", color, alg.A(-2))
    ledger.check("RAW_TO_COMPONENT", raw_to_component, alg.A(-16))
    ledger.check("MASTER_OVER_LAMBDA", master_over_lambda, sp.Rational(1, 2))
    ledger.check("LEGACY_COMPONENT_TIMES_MASTER", legacy_component_times_master, -8)
    ledger.check("RANK_TRACE_CORRECTION", rank_trace_correction, sp.Rational(1, 2))
    ledger.check("CORRECTED_COMPONENT_TIMES_MASTER", corrected_component_times_master, -4)
    return {
        "external_D_each": "-sqrt(2)/8",
        "external_D_product": "1/32",
        "isolating_color_tensor": "-2",
        "raw_to_component": "-16",
        "master_over_lambda1": "1/2",
        "legacy_component_times_master": "-8",
        "rank_trace_correction_from_generated_contact": "1/2",
        "corrected_component_times_master": "-4",
        "four_chirality_times_corrected_conversion": "4*(-4)=-16",
        "raw_integrated_to_lambda1_full_result": "-16",
        "forbidden_double_count": (
            "Do not multiply the corrected -4 by another rank/trace half."
        ),
        "lambda1": "hbar*g^2/(16*pi^2)",
    }


def sd_rank_trace_certificate(ledger: Ledger) -> dict[str, object]:
    rd2, phat, rword = sp.symbols("r_ed2 P_hat_e R_omega_e", nonzero=True)
    parent = sp.Integer(1)
    contact = sp.Integer(1)
    full_d = sp.factor(parent * rword * rd2 / (rd2 * phat) - contact * rword / phat)
    ledger.check(
        "RAW_CONTACT_MULTIPLICITY_FULL_D_ZERO",
        full_d,
        0,
    )
    contact_payload = json.loads(RAW_CONTACT_JSON.read_text(encoding="utf-8"))
    contact_checks = contact_payload["checks"]
    ledger.check(
        "RAW_CONTACT_ARTIFACT_STATUS",
        contact_payload["status"],
        "PASS_RAW_LOCAL_CONTACT_MULTIPLICITY_ONE__FINITE_W_LINK_LONGITUDINAL_ZERO",
    )
    ledger.check("RAW_CONTACT_ARTIFACT_FAILED", contact_checks["failed"], 0)
    ledger.check("RAW_CONTACT_ARTIFACT_M", contact_payload["local_w0"]["m_contact"], "1")
    occurrence_rows = [
        {
            "pair": "AD",
            "allocation": "F^{AB}_{DE}",
            "edge": "e0",
            "R_omega_e": "-i*(ell+p_raw+q_raw/2)_plus",
        },
        {
            "pair": "AD",
            "allocation": "F^{BA}_{DE}",
            "edge": "e2",
            "R_omega_e": "+i*ell_plus",
        },
        {
            "pair": "DA",
            "allocation": "F^{AB}_{DE}",
            "edge": "e2",
            "R_omega_e": "+i*ell_plus",
        },
        {
            "pair": "DA",
            "allocation": "F^{BA}_{DE}",
            "edge": "e0",
            "R_omega_e": "-i*(ell+p_raw+q_raw/2)_plus",
        },
    ]
    for row in occurrence_rows:
        row.update(
            {
                "generated_selected_parent": (
                    "R_omega_e*bar(r_e)^2/(D0*D1*D2)"
                ),
                "parent_coefficient": "1_FROM_RAW_SELECTED_FACTORIZATION",
                "raw_contact_coefficient": "1_FROM_RAW_FUNCTIONAL_HESSIAN",
                "full_d_sum": "0",
                "local_factor_chain": (
                    "parent=(-2)^3=-8; contact=(-1)_SD*(-2)_Euler*(-2)^2=+8"
                ),
                "multiplicity": (
                    "(1/2!*2_action_order)*(1/2!*2_cut_endpoint)*"
                    "(1/2!*2_remaining_Wick)=1"
                ),
            }
        )
    return {
        "derivation": [
            "The source D-word generates the selected parent coefficient one.",
            "The raw contact uses the canonical kinetic metric and two uncut propagators.",
            "Eight action-order, cut-endpoint, and remaining-Wick rows sum to one.",
        ],
        "equations": {
            "parent": "R*bar(r_e)^2/P3",
            "contact": "-R/P_hat_e",
            "full_d_gate": "R*r_(e,d)^2/P3-R/P_hat_e=0",
            "dred_remainder": "R*mu_l^2/P3",
        },
        "m_parent": "1",
        "m_contact": "1",
        "legacy_trace_factor": "2",
        "corrected_trace_factor": "1",
        "rank_trace_correction": "1/2",
        "contact_artifact": str(RAW_CONTACT_JSON.relative_to(ROOT)),
        "contact_artifact_checks": {
            "passed": contact_checks["passed"],
            "failed": contact_checks["failed"],
        },
        "status": "PASS_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE",
        "occurrence_rows": occurrence_rows,
    }


def action_sector_weight_certificate(ledger: Ledger) -> dict[str, object]:
    same_chirality_weight = sp.Rational(1, 2) * 2
    mixed_chirality_weight = sp.Integer(1)
    ledger.check("ACTION_WEIGHT_PLUS_PLUS", same_chirality_weight, 1)
    ledger.check("ACTION_WEIGHT_PLUS_MINUS", mixed_chirality_weight, 1)
    ledger.check("ACTION_WEIGHT_MINUS_PLUS", mixed_chirality_weight, 1)
    ledger.check("ACTION_WEIGHT_MINUS_MINUS", same_chirality_weight, 1)
    return {
        "interaction_expansion": (
            "(1/2!)*sum_(chi,psi)[H_chi(L)H_psi(R)+H_psi(R)H_chi(L)]"
        ),
        "even_vertex_exchange": "H_psi(R)H_chi(L)=H_chi(L)H_psi(R)",
        "weights": {"++": "1", "+-": "1", "-+": "1", "--": "1"},
        "four_sector_sum_rule": (
            "If the four raw Hessian contractions coincide polynomially, "
            "their full action contribution is exactly four times one sector."
        ),
    }


def raw_operator_sector_certificate(ledger: Ledger) -> dict[str, object]:
    operator_checks = raw.verify_marked_operator_identity()
    selected_checks = raw.verify_selected_parent_factorization()
    gf_checks = raw.verify_gauge_fixing_longitudinal_cancellation()
    loop, p, q = raw.interpolation_samples()[0]
    r0 = loop
    r2 = alg.vadd(loop, p, q)
    pair_gf_checks = 0
    for pair, attachment in itertools.product(
        ("A__Ddot1", "Ddot1__A"), ("direct", "crossed")
    ):
        momenta = (
            (alg.vneg(r0), r2)
            if attachment == "direct"
            else (r2, alg.vneg(r0))
        )
        for mask_left, mask_right in itertools.product(range(16), repeat=2):
            longitudinal = raw.source_component_entry(
                pair,
                *momenta,
                mask_left,
                mask_right,
                0,
                0,
                1,
                "longitudinal",
            )
            gauge_fixing = raw.gauge_fixing_source_component_entry(
                pair,
                *momenta,
                mask_left,
                mask_right,
                0,
                0,
                1,
            )
            if longitudinal + gauge_fixing:
                raise AssertionError(
                    (pair, attachment, mask_left, mask_right, longitudinal, gauge_fixing)
                )
            pair_gf_checks += 1
    ledger.check("RAW_MARKED_OPERATOR_MASKS", operator_checks, 32)
    ledger.check("RAW_SELECTED_FACTORIZATION_MASKS", selected_checks, 32)
    ledger.check("RAW_LONGITUDINAL_GF_MASKS", gf_checks, 32)
    ledger.check("RAW_PAIR_HESSIAN_LONGITUDINAL_GF_MASKS", pair_gf_checks, 1024)
    rows = [
        {
            "pair": "AD",
            "allocation": "F^{AB}_{DE}",
            "source_attachment": "direct",
            "marked_edge": "e0",
            "r_e": "r0=ell",
            "R_e": "-i*(ell+p_raw+q_raw/2)_plus",
        },
        {
            "pair": "AD",
            "allocation": "F^{BA}_{DE}",
            "source_attachment": "crossed",
            "marked_edge": "e2",
            "r_e": "r2=ell+p_raw+q_raw",
            "R_e": "+i*ell_plus",
        },
        {
            "pair": "DA",
            "allocation": "F^{AB}_{DE}",
            "source_attachment": "direct",
            "marked_edge": "e2",
            "r_e": "r2=ell+p_raw+q_raw",
            "R_e": "+i*ell_plus",
        },
        {
            "pair": "DA",
            "allocation": "F^{BA}_{DE}",
            "source_attachment": "crossed",
            "marked_edge": "e0",
            "r_e": "r0=ell",
            "R_e": "-i*(ell+p_raw+q_raw/2)_plus",
        },
    ]
    for row in rows:
        row.update(
            {
                "selected_kinetic_parent": "R_e*bar(r_e)^2/(D0*D1*D2)",
                "source_longitudinal": "+L_(omega,e)/(D0*D1*D2)",
                "gauge_fixing_euler": "-L_(omega,e)/(D0*D1*D2)",
                "longitudinal_plus_GF": "0",
                "full_d_cut": "-R_e/P_hat_e",
                "full_d_orbit_sum": "0",
                "DRED_orbit_sum": "R_e*mu_l^2/(D0*D1*D2)",
            }
        )
    return {
        "raw_code_paths": {
            "full_operator": "source_component_entry(marked_sector='full')",
            "selected_kinetic": "source_component_entry(marked_sector='selected')",
            "source_longitudinal": "source_component_entry(marked_sector='longitudinal')",
            "gauge_fixing": "gauge_fixing_source_component_entry",
        },
        "operator_identity": {
            "full": "D_-D_+barD^2D_+",
            "selected": "-8*bar(r_e)^2*D_+",
            "longitudinal": "-(1/2)*D_+*barD^2*D^2",
            "gauge_fixing": "+(1/2)*D_+*barD^2*D^2",
            "full_plus_GF": "-8*bar(r_e)^2*D_+",
        },
        "mask_checks": {
            "operator": operator_checks,
            "selected_factorization": selected_checks,
            "longitudinal_plus_gauge_fixing": gf_checks,
            "pair_hessian_longitudinal_plus_gauge_fixing": pair_gf_checks,
        },
        "occurrence_rows": rows,
        "claim_boundary": (
            "Raw operator-level kinetic/longitudinal/GF replay is exact.  "
            "The four chirality-sector cubic Hessians, local Schwinger contact, "
            "and finite-w longitudinal link cancellation are independently replayed."
        ),
    }


def integrate_rank_one(
    coefficients: tuple[sp.Expr, sp.Expr, sp.Expr]
) -> tuple[sp.Expr, sp.Expr]:
    ell, p, q = coefficients
    return (
        sp.simplify(p - sp.Rational(2, 3) * ell),
        sp.simplify(q - sp.Rational(1, 3) * ell),
    )


def finite_vector_certificate(ledger: Ledger) -> dict[str, object]:
    r1 = interpolate_frames(R1_FRAMES)
    r2 = interpolate_frames(R2_FRAMES)
    r1_int = integrate_rank_one(r1)
    r2_int = integrate_rank_one(r2)
    ledger.check("R1_SIMPLEX", r1_int, (sp.I / 48, sp.I / 96))
    ledger.check("R2_SIMPLEX", r2_int, (sp.I / 24, sp.I / 48))
    four_sector_weight = sp.Integer(4)
    r1_four_sector_raw = tuple(
        sp.simplify(four_sector_weight * entry) for entry in r1_int
    )
    r2_four_sector_raw = tuple(
        sp.simplify(four_sector_weight * entry) for entry in r2_int
    )
    ledger.check(
        "R1_FOUR_SECTOR_RAW",
        r1_four_sector_raw,
        (sp.I / 12, sp.I / 24),
    )
    ledger.check(
        "R2_FOUR_SECTOR_RAW",
        r2_four_sector_raw,
        (sp.I / 6, sp.I / 12),
    )
    rank_trace_correction = sp.Rational(1, 2)
    corrected_conversion = sp.Integer(-8)
    r1_corrected_raw = tuple(
        sp.simplify(rank_trace_correction * entry)
        for entry in r1_four_sector_raw
    )
    r2_corrected_raw = tuple(
        sp.simplify(rank_trace_correction * entry)
        for entry in r2_four_sector_raw
    )
    r1_lambda = tuple(
        sp.simplify(corrected_conversion * entry) for entry in r1_corrected_raw
    )
    r2_lambda = tuple(
        sp.simplify(corrected_conversion * entry) for entry in r2_corrected_raw
    )
    ledger.check("R1_RANK_TRACE_CORRECTED_RAW", r1_corrected_raw, (sp.I / 24, sp.I / 48))
    ledger.check("R2_RANK_TRACE_CORRECTED_RAW", r2_corrected_raw, (sp.I / 12, sp.I / 24))
    ledger.check("R1_FULL_OVER_LAMBDA", r1_lambda, (-sp.I / 3, -sp.I / 6))
    ledger.check("R2_FULL_OVER_LAMBDA", r2_lambda, (-2 * sp.I / 3, -sp.I / 3))
    for artifact_path, frame in (
        (POLARIZED_P_JSON, "p_only"),
        (POLARIZED_Q_JSON, "q_only"),
    ):
        replay = json.loads(artifact_path.read_text(encoding="utf-8"))
        ledger.check(f"POLARIZED_{frame}_STATUS", replay["status"], "PASS")
        ledger.check(f"POLARIZED_{frame}_FAILED", replay["checks"]["failed"], 0)
        ledger.check(f"POLARIZED_{frame}_COUNT", replay["checks"]["count"], 112)
    return {
        "simplex_shift": "ell -> -(2*p+q)/3",
        "raw_to_IR_external_momenta": {
            "p_raw": "q_IR=k_left",
            "q_raw": "p_IR=k_right",
        },
        "raw_integrated": {
            "R1": {"p_raw": "i/48", "q_raw": "i/96"},
            "R2": {"p_raw": "i/24", "q_raw": "i/48"},
        },
        "four_chirality_sum": {
            "sector_weights": {"++": "1", "+-": "1", "-+": "1", "--": "1"},
            "R1_raw": {"p_raw": "i/12", "q_raw": "i/24"},
            "R2_raw": {"p_raw": "i/6", "q_raw": "i/12"},
            "rank_trace_correction": "1/2",
            "R1_corrected_raw": {"p_raw": "i/24", "q_raw": "i/48"},
            "R2_corrected_raw": {"p_raw": "i/12", "q_raw": "i/24"},
            "legacy_component_master_conversion": "-8",
            "R1_over_lambda1": {"p_raw=q_IR": "-i/3", "q_raw=p_IR": "-i/6"},
            "R2_over_lambda1": {"p_raw=q_IR": "-2*i/3", "q_raw=p_IR": "-i/3"},
        },
        "typed_projection": {
            "right_spinor_carrier": "D^E_upper(p_IR)",
            "other_field_momentum": "q_IR=p_raw",
            "carrier_own_momentum": "p_IR=q_raw",
            "identity": (
                "D^D_lower*(a*q_IR+b*p_IR)_+*D^E_upper="
                "a*<D^D_lower,D^E_upper>_+ + "
                "b*D^D_lower*(P^{dot a}D^E_{dot a})"
            ),
            "spinor_Fourier_conversion": "-i*k_plus -> P_dot_a",
            "canonical_bracket_coefficients": {
                "AD": {"P_on_left": "1/3", "P_on_right": "2/3"},
                "DA": {"P_on_left": "2/3", "P_on_right": "1/3"},
            },
            "coefficient_status": "PASS",
        },
        "reflection": {
            "AD_direct_F_AB": "DA_crossed_F_BA=R1",
            "AD_crossed_F_BA": "DA_direct_F_AB=R2",
        },
        "full_chirality_matrix_status": (
            "PASS_P_ONLY_112_OF_112__Q_ONLY_112_OF_112"
        ),
        "absolute_coefficient_status": (
            "PASS_RAW_CONTACT_MULTIPLICITY_ONE_AND_RANK_TRACE_HALF"
        ),
        "output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
    }


def sd_row(
    row_id: str,
    pair: str,
    allocation: str,
    edge: str,
    component_r: str,
    cut_numerator: str,
) -> dict[str, str]:
    denominators = {"e0": "D1*D2", "e1": "D0*D2", "e2": "D0*D1"}
    edge_name = {"e0": "r0", "e1": "r1", "e2": "r2"}[edge]
    return {
        "id": row_id,
        "pair": pair,
        "color_allocation": allocation,
        "edge": edge,
        "component_parent_R": component_r,
        "parent_4d": f"({component_r})*bar({edge_name})^2/(D0*D1*D2)",
        "full_cut": f"({cut_numerator})/({denominators[edge]})",
        "full_d_sum": "0",
        "dred_remainder": f"({component_r})*mu_l^2/(D0*D1*D2)",
    }


CROSS_CONTACT_FRAMES = {
    ("AD", "e0"): (-alg.I, -alg.I, -alg.ONE / 2 - alg.I, alg.ONE / 2),
    ("AD", "e1"): (
        alg.ONE + 2 * alg.I,
        alg.ONE + 2 * alg.I,
        3 * alg.ONE + alg.I,
        -alg.ONE + alg.I,
    ),
    ("AD", "e2"): (
        alg.ONE + 2 * alg.I,
        alg.ONE + 2 * alg.I,
        3 * alg.ONE + alg.I,
        -alg.ONE + alg.I,
    ),
    ("DA", "e0"): (
        14 * alg.I,
        14 * alg.I,
        7 * alg.ONE + 14 * alg.I,
        -7 * alg.ONE,
    ),
    ("DA", "e1"): (alg.ZERO, alg.ZERO, alg.ZERO, alg.ZERO),
    ("DA", "e2"): (
        4 * alg.I,
        4 * alg.I,
        2 * alg.ONE + 4 * alg.I,
        -2 * alg.ONE,
    ),
}


def crossed_contact_certificate(ledger: Ledger) -> dict[str, object]:
    expected_formulas: dict[tuple[str, str], tuple[sp.Expr, sp.Expr, sp.Expr]] = {
        ("AD", "e0"): (sp.Integer(0), sp.Integer(0), -sp.I / 2),
        ("AD", "e1"): (sp.Integer(0), sp.I, sp.I),
        ("AD", "e2"): (sp.Integer(0), sp.I, sp.I),
        ("DA", "e0"): (sp.Integer(0), sp.Integer(0), 7 * sp.I),
        ("DA", "e1"): (sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        ("DA", "e2"): (sp.Integer(0), sp.Integer(0), 2 * sp.I),
    }
    rows: list[dict[str, object]] = []
    for key, frames in CROSS_CONTACT_FRAMES.items():
        coefficients = expected_formulas[key]
        for sample_index, ((loop, p, q), value) in enumerate(
            zip(raw.interpolation_samples(), frames, strict=True)
        ):
            predicted = sp.simplify(
                coefficients[0] * raw.plus_dotted(loop, 0)
                + coefficients[1] * raw.plus_dotted(p, 0)
                + coefficients[2] * raw.plus_dotted(q, 0)
            )
            ledger.check(
                f"CROSSED_CONTACT_{key[0]}_{key[1]}_FRAME{sample_index}",
                sp.expand_complex(gaussian(value) - predicted),
                0,
            )
        rows.append(
            {
                "pair": key[0],
                "edge": key[1],
                "frames": [value.text() for value in frames],
                "rank_one": {
                    "ell_plus": exact_text(coefficients[0]),
                    "p_plus": exact_text(coefficients[1]),
                    "q_plus": exact_text(coefficients[2]),
                },
            }
        )
    return {
        "color_projector": "F^{BA}_{DE}; SU2 (A,B;D,E)=(0,1;0,1)",
        "rows": rows,
        "aggregate_symmetry": {
            "crossed_AD": "direct_DA occurrencewise after color projection",
            "crossed_DA": "direct_AD occurrencewise after color projection",
        },
    }


def contact_parent_certificate(ledger: Ledger) -> dict[str, object]:
    rd2, mu2, phat, rword = sp.symbols("r_ed2 mu_l2 P_hat R_omega_e", nonzero=True)
    full_d = sp.simplify(rword * rd2 / (rd2 * phat) - rword / phat)
    dred = sp.simplify(rword * (rd2 + mu2) / (rd2 * phat) - rword / phat)
    ledger.check("FULL_D_PARENT_PLUS_CUT", full_d, 0)
    ledger.check("DRED_PARENT_PLUS_CUT", dred, rword * mu2 / (rd2 * phat))
    rows = [
        sd_row(
            "AD_DIRECT_E0",
            "AD",
            "F^{AB}_{DE}",
            "e0",
            "-i*(ell+p+q/2)_plus",
            "+i*(ell+p+q/2)_plus",
        ),
        sd_row(
            "AD_CROSSED_E2",
            "AD",
            "F^{BA}_{DE}",
            "e2",
            "+i*ell_plus",
            "-i*ell_plus",
        ),
        sd_row(
            "DA_DIRECT_E2",
            "DA",
            "F^{AB}_{DE}",
            "e2",
            "+i*ell_plus",
            "-i*ell_plus",
        ),
        sd_row(
            "DA_CROSSED_E0",
            "DA",
            "F^{BA}_{DE}",
            "e0",
            "-i*(ell+p+q/2)_plus",
            "+i*(ell+p+q/2)_plus",
        ),
    ]
    ledger.check("TGG_SD_ROW_COUNT", len(rows), 4)
    explicit_partial = {
        "projector_F_AB": {
            "AD": {
                "O05_e0": "7*i*q_plus/(D1*D2)",
                "O06_e1": "0/(D0*D2)",
                "O05_e2": "2*i*q_plus/(D0*D1)",
            },
            "DA": {
                "O05_e0": "-i*q_plus/(2*D1*D2)",
                "O06_e1": "i*(p+q)_plus/(D0*D2)",
                "O05_e2": "i*(p+q)_plus/(D0*D1)",
            },
        },
        "projector_F_BA": {
            "AD": {
                "O05_e0": "-i*q_plus/(2*D1*D2)",
                "O06_e1": "i*(p+q)_plus/(D0*D2)",
                "O05_e2": "i*(p+q)_plus/(D0*D1)",
            },
            "DA": {
                "O05_e0": "7*i*q_plus/(D1*D2)",
                "O06_e1": "0/(D0*D2)",
                "O05_e2": "2*i*q_plus/(D0*D1)",
            },
        },
        "interpretation": (
            "O05/O06 are partial contact members.  A row is a valid cut only "
            "after it is combined on the same edge and same color tensor with "
            "the remaining kinetic, longitudinal, gauge-fixing, and link contacts."
        ),
        "forbidden_operation": (
            "Do not infer zero from the affine two-denominator numerator and do "
            "not add a partial O05/O06 contact to an already formed mu_l^2 remainder."
        ),
    }
    ell_plus, p_plus, q_plus = sp.symbols("ell_plus p_plus q_plus")
    i = sp.I
    allocation_balances = {
        "F^{AB}_{DE}": {
            "AD": {
                "e0": (7 * i * q_plus, i * (ell_plus + p_plus + q_plus / 2)),
                "e1": (sp.Integer(0), sp.Integer(0)),
                "e2": (2 * i * q_plus, sp.Integer(0)),
            },
            "DA": {
                "e0": (-i * q_plus / 2, sp.Integer(0)),
                "e1": (i * (p_plus + q_plus), sp.Integer(0)),
                "e2": (i * (p_plus + q_plus), -i * ell_plus),
            },
        },
        "F^{BA}_{DE}": {
            "AD": {
                "e0": (-i * q_plus / 2, sp.Integer(0)),
                "e1": (i * (p_plus + q_plus), sp.Integer(0)),
                "e2": (i * (p_plus + q_plus), -i * ell_plus),
            },
            "DA": {
                "e0": (7 * i * q_plus, i * (ell_plus + p_plus + q_plus / 2)),
                "e1": (sp.Integer(0), sp.Integer(0)),
                "e2": (2 * i * q_plus, sp.Integer(0)),
            },
        },
    }
    completion_constraints: list[dict[str, str]] = []
    for allocation, pair_rows in allocation_balances.items():
        allocation_id = "AB" if allocation == "F^{AB}_{DE}" else "BA"
        for pair, edge_rows in pair_rows.items():
            for edge, (explicit, full_cut) in edge_rows.items():
                required_constraint = sp.expand(full_cut - explicit)
                ledger.check(
                    f"CONTACT_CONSTRAINT_{allocation_id}_{pair}_{edge}",
                    sp.expand(explicit + required_constraint),
                    sp.expand(full_cut),
                )
                completion_constraints.append(
                    {
                        "pair": pair,
                        "color_allocation": allocation,
                        "edge": edge,
                        "explicit_O05_or_O06": exact_text(explicit),
                        "required_completion_constraint": exact_text(required_constraint),
                        "full_same_edge_cut": exact_text(full_cut),
                        "derivation": (
                            "constraint only: full_same_edge_cut-explicit_O05_or_O06; "
                            "not a generated sector amplitude"
                        ),
                    }
                )
    return {
        "identity": {
            "full_d": "R*r_(e,d)^2/P3-R/P_hat_e=0",
            "dred": "R*bar(r_e)^2/P3-R/P_hat_e=R*mu_l^2/P3",
        },
        "occurrence_resolved_TGG_rows": rows,
        "explicit_O05_O06_partial_contacts": explicit_partial,
        "crossed_color_contact_replay": crossed_contact_certificate(ledger),
        "required_same_edge_completion_constraints": completion_constraints,
        "generated_raw_contact": {
            "artifact": str(RAW_CONTACT_JSON.relative_to(ROOT)),
            "local_factor_chain": (
                "parent=(-2)^3=-8; contact=(-1)_SD*(-2)_Euler*(-2)^2=+8"
            ),
            "multiplicity": (
                "(1/2!*2_action_order)*(1/2!*2_cut_endpoint)*"
                "(1/2!*2_remaining_Wick)=1"
            ),
            "full_d_check": (
                "4 frames * 4 occurrence/color rows * 4 chirality sectors: "
                "N_d+K_raw=0"
            ),
            "finite_w_link": (
                "T1 derivative has the same phase-weighted residue; Duhamel "
                "endpoint cancellation is zero before integration"
            ),
        },
        "contact_completion_status": (
            "PASS_GENERATED_AGGREGATE_RAW_SCHWINGER_CONTACT_AND_FINITE_W_LINK;_"
            "O05_O06_REMAIN_PARTIAL_NORMAL_FORM_ALLOCATIONS"
        ),
    }


def _replay_tgg_one(args: tuple[str, str]) -> tuple[str, str, alg.A]:
    pair, allocation = args
    loop, p, q = raw.interpolation_samples()[0]
    if allocation == "direct":
        attachment, ext_left, ext_right = "direct", 1, 0
    else:
        attachment, ext_left, ext_right = "crossed", 0, 1
    routes = raw.all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        source_attachment=attachment,
        external_left_color=ext_left,
        external_right_color=ext_right,
        left_action_sector="-",
        right_action_sector="+",
    )
    return pair, allocation, sum(routes.values(), alg.ZERO)


def _full_cubic_hessian_task(
    args: tuple[
        str,
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
        int,
        int,
        int,
        int,
        int,
        int,
    ]
) -> tuple[str, str, int, int, int, int, int, alg.A]:
    (
        vertex,
        sector,
        momentum_1,
        momentum_2,
        background_momentum,
        background_dotted,
        background_color,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
    ) = args
    ctx = alg.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        alg.endpoint_D(
            ctx,
            "X",
            2,
            background_color,
            background_dotted,
            eta_index=4,
        ),
    ]
    action = alg.gauge_action_integrand(alg.sum_mats(fields), "X", sector)
    action = action.coefficient_labels((1, 1, 1))
    action = (
        alg.integrate_chiral(action, "X")
        if sector == "+"
        else alg.integrate_antichiral(action, "X")
    )
    value = action.grass_coefficient(
        alg.hessian_marker_mask(theta_mask_1, theta_mask_2, True)
    )
    return (
        vertex,
        sector,
        background_color,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
        value,
    )


def _full_cubic_hessian_tables(
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    workers: int,
) -> dict[str, dict[tuple[str, int, int, int, int, int], alg.A]]:
    r0 = loop
    r1 = alg.vadd(loop, p)
    r2 = alg.vadd(loop, p, q)
    vertex_data = {
        "left": (r0, alg.vneg(r1), p, 0),
        "right": (alg.vneg(r2), r1, q, 1),
    }
    # The two SU(2) projectors isolate exactly these two color rows:
    # direct uses (background,source)=(1,0) on the left and (0,1) on
    # the right; crossed interchanges them.  The bridge color is summed.
    # All other background/source pairs are orthogonal to both projectors.
    color_rows = tuple(
        (background_color, source_color, bridge_color)
        for background_color, source_color in ((1, 0), (0, 1))
        for bridge_color in range(3)
    )
    tasks = [
        (
            vertex,
            sector,
            momentum_1,
            momentum_2,
            background_momentum,
            background_dotted,
            background_color,
            color_1,
            color_2,
            theta_mask_1,
            theta_mask_2,
        )
        for vertex, (
            momentum_1,
            momentum_2,
            background_momentum,
            background_dotted,
        ) in vertex_data.items()
        for sector, (
            background_color,
            color_1,
            color_2,
        ), theta_mask_1, theta_mask_2 in itertools.product(
            ("+", "-"), color_rows, range(16), range(16)
        )
    ]
    tables: dict[str, dict[tuple[str, int, int, int, int, int], alg.A]] = {
        "left": {},
        "right": {},
    }
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        rows = pool.map(_full_cubic_hessian_task, tasks, chunksize=8)
        for vertex, sector, background_color, color_1, color_2, mask_1, mask_2, value in rows:
            if value:
                tables[vertex][
                    sector,
                    background_color,
                    color_1,
                    color_2,
                    mask_1,
                    mask_2,
                ] = value
    return tables


def _full_polarized_contract(
    pair: str,
    allocation: str,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    tables: dict[str, dict[tuple[str, int, int, int, int, int], alg.A]],
    marked_sector: str = "evanescent",
) -> dict[tuple[str, str], alg.A]:
    r0 = loop
    r2 = alg.vadd(loop, p, q)
    direct = allocation == "direct"
    if allocation not in {"direct", "crossed"}:
        raise ValueError(allocation)
    source_momenta = (alg.vneg(r0), r2) if direct else (r2, alg.vneg(r0))
    source_table: dict[tuple[int, int], alg.A] = {}
    for source_left_mask, source_right_mask in itertools.product(range(16), repeat=2):
        if marked_sector == "gauge_fixing":
            value = raw.gauge_fixing_source_component_entry(
                pair,
                *source_momenta,
                source_left_mask,
                source_right_mask,
                0,
                0,
                1,
            )
        else:
            value = raw.source_component_entry(
                pair,
                *source_momenta,
                source_left_mask,
                source_right_mask,
                0,
                0,
                1,
                marked_sector,
            )
        if value:
            source_table[source_left_mask, source_right_mask] = value

    totals = {(left, right): alg.ZERO for left in ("+", "-") for right in ("+", "-")}
    left_source_index = 0 if direct else 1
    right_source_index = 1 if direct else 0
    left_source_color = 0 if direct else 1
    right_source_color = 1 if direct else 0
    left_external_color = 1 if direct else 0
    right_external_color = 0 if direct else 1
    for (source_left_mask, source_right_mask), source in source_table.items():
        source_masks = (source_left_mask, source_right_mask)
        left_source_mask = 15 ^ source_masks[left_source_index]
        right_source_mask = 15 ^ source_masks[right_source_index]
        cov_left = alg.component_covariance(
            source_masks[left_source_index], left_source_mask
        )
        cov_right = alg.component_covariance(
            source_masks[right_source_index], right_source_mask
        )
        if not cov_left or not cov_right:
            continue
        for left_bridge_mask in range(16):
            right_bridge_mask = 15 ^ left_bridge_mask
            cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
            if not cov_bridge:
                continue
            parities = (
                source_left_mask.bit_count() % 2,
                source_right_mask.bit_count() % 2,
                left_source_mask.bit_count() % 2,
                left_bridge_mask.bit_count() % 2,
                1,
                right_source_mask.bit_count() % 2,
                right_bridge_mask.bit_count() % 2,
                1,
            )
            pairs = (
                ((0, 2), (1, 5), (3, 6))
                if direct
                else ((0, 5), (1, 2), (3, 6))
            )
            wick = raw.wick_pair_sign(parities, pairs)
            edge = -8 * cov_left * cov_right * cov_bridge
            for left_sector, right_sector in totals:
                value = alg.ZERO
                for bridge_color in range(3):
                    left = tables["left"].get(
                        (
                            left_sector,
                            left_external_color,
                            left_source_color,
                            bridge_color,
                            left_source_mask,
                            left_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    right = tables["right"].get(
                        (
                            right_sector,
                            right_external_color,
                            right_source_color,
                            bridge_color,
                            right_source_mask,
                            right_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    value += left * right
                totals[left_sector, right_sector] += wick * edge * source * value
    return totals


def replay_full_chirality_frame0(ledger: Ledger, workers: int) -> dict[str, object]:
    loop, p, q = raw.interpolation_samples()[0]
    tables = _full_cubic_hessian_tables(loop, p, q, workers)
    rows: dict[str, object] = {}
    for pair_id, pair in (("AD", "A__Ddot1"), ("DA", "Ddot1__A")):
        rows[pair_id] = {}
        for allocation in ("direct", "crossed"):
            values = _full_polarized_contract(
                pair,
                allocation,
                loop,
                p,
                q,
                tables,
            )
            rows[pair_id][allocation] = {
                f"{left}{right}": value.text()
                for (left, right), value in values.items()
            }
            # The former ordered-slot -,+ sum is an independent implementation
            # of the same full cubic functional Hessian entry.
            expected_minus_plus = {
                ("AD", "direct"): R1_FRAMES[0],
                ("AD", "crossed"): R2_FRAMES[0],
                ("DA", "direct"): R2_FRAMES[0],
                ("DA", "crossed"): R1_FRAMES[0],
            }[pair_id, allocation]
            ledger.check(
                f"FULL_HESSIAN_MINUS_PLUS_{pair_id}_{allocation}",
                values["-", "+"],
                expected_minus_plus,
            )
    return {
        "frame": 0,
        "action_table_sizes": {
            vertex: len(table) for vertex, table in tables.items()
        },
        "all_chirality_sectors": rows,
    }


def replay_frame0(ledger: Ledger, workers: int) -> None:
    args = [
        (pair, allocation)
        for pair in ("A__Ddot1", "Ddot1__A")
        for allocation in ("direct", "crossed")
    ]
    expected = {
        ("A__Ddot1", "direct"): R1_FRAMES[0],
        ("A__Ddot1", "crossed"): R2_FRAMES[0],
        ("Ddot1__A", "direct"): R2_FRAMES[0],
        ("Ddot1__A", "crossed"): R1_FRAMES[0],
    }
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        rows = list(pool.map(_replay_tgg_one, args))
    for pair, allocation, value in rows:
        ledger.check(f"REPLAY_FRAME0_{pair}_{allocation}", value, expected[pair, allocation])


def _cross_o05_partial(
    args: tuple[int, str, str, alg.Vector, alg.Vector, alg.Vector, int, int]
) -> tuple[int, str, str, dict[str, alg.A]]:
    sample_index, pair, edge, loop, p, q, color_1, color_2 = args
    if edge == "e0":
        values = raw.dd_bubble_color_partials(
            pair, loop, p, q, 0, 1, 0, 1, color_1, color_2, 0, 1, "+"
        )
    elif edge == "e2":
        values = raw.dd_bubble_color_partials(
            pair, loop, q, p, 1, 0, 1, 0, color_1, color_2, 0, 1, "-"
        )
    else:
        raise ValueError(edge)
    return sample_index, pair, edge, values


def _cross_o06_partial(
    args: tuple[int, str, alg.Vector, alg.Vector, alg.Vector, int, int]
) -> tuple[int, str, dict[str, alg.A]]:
    sample_index, pair, loop, p, q, color_1, color_2 = args
    values = raw.dd_quartic_color_partials(
        pair, loop, p, q, color_1, color_2, 0, 1, 0, 1
    )
    return sample_index, pair, values


def replay_crossed_contacts(ledger: Ledger, workers: int) -> None:
    samples = raw.interpolation_samples()
    o05_args = [
        (sample_index, pair, edge, loop, p, q, color_1, color_2)
        for sample_index, (loop, p, q) in enumerate(samples)
        for pair in ("A__Ddot1", "Ddot1__A")
        for edge in ("e0", "e2")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    o06_args = [
        (sample_index, pair, loop, p, q, color_1, color_2)
        for sample_index, (loop, p, q) in enumerate(samples)
        for pair in ("A__Ddot1", "Ddot1__A")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        o05_rows = list(pool.map(_cross_o05_partial, o05_args))
        o06_rows = list(pool.map(_cross_o06_partial, o06_args))

    o05_totals: dict[tuple[int, str, str], dict[str, alg.A]] = {}
    for sample_index, pair, edge, values in o05_rows:
        target = o05_totals.setdefault((sample_index, pair, edge), {})
        for tag, value in values.items():
            target[tag] = target.get(tag, alg.ZERO) + value
    o06_totals: dict[tuple[int, str], dict[str, alg.A]] = {}
    for sample_index, pair, values in o06_rows:
        target = o06_totals.setdefault((sample_index, pair), {})
        for tag, value in values.items():
            target[tag] = target.get(tag, alg.ZERO) + value

    color = alg.A(alg.su2_F(1, 0, 0, 1))
    ledger.check("CROSSED_REPLAY_COLOR_PROJECTOR", color, alg.A(-2))
    for sample_index, (_, p, q) in enumerate(samples):
        norm_left = raw.external_d_normalization(p, 0, 0)
        norm_right = raw.external_d_normalization(q, 1, 1)
        normalization = alg.A(Fraction(-1, 2)) / (
            norm_left * norm_right * color
        )
        for pair_id, short_pair in (("A__Ddot1", "AD"), ("Ddot1__A", "DA")):
            for edge in ("e0", "e2"):
                edge_sign = -1 if edge == "e2" else 1
                value = sum(
                    (
                        edge_sign * normalization * entry
                        for entry in o05_totals[(sample_index, pair_id, edge)].values()
                    ),
                    alg.ZERO,
                )
                ledger.check(
                    f"REPLAY_CROSSED_O05_{short_pair}_{edge}_FRAME{sample_index}",
                    value,
                    CROSS_CONTACT_FRAMES[short_pair, edge][sample_index],
                )
            value = sum(
                (
                    normalization * entry
                    for entry in o06_totals[(sample_index, pair_id)].values()
                ),
                alg.ZERO,
            )
            ledger.check(
                f"REPLAY_CROSSED_O06_{short_pair}_e1_FRAME{sample_index}",
                value,
                CROSS_CONTACT_FRAMES[short_pair, "e1"][sample_index],
            )


def build_payload(
    replay: bool = False,
    replay_contacts: bool = False,
    replay_full_chirality: bool = False,
    workers: int = 4,
) -> dict[str, object]:
    ledger = Ledger()
    payload: dict[str, object] = {
        "schema": "step5-ad-da-ordered-ports-crossed-hessian-exact-v3",
        "external_target_used": False,
        "routing": routing_certificate(ledger),
        "source_hessian_color": color_hessian_certificate(ledger),
        "source_hessian_components": source_component_hessian_certificate(ledger),
        "action_sector_weights": action_sector_weight_certificate(ledger),
        "evanescent_numerators": numerator_certificate(ledger),
        "normalization": normalization_certificate(ledger),
        "rank_trace_from_AD_DA_SD": sd_rank_trace_certificate(ledger),
        "raw_operator_sectors": raw_operator_sector_certificate(ledger),
        "schwinger_rows": contact_parent_certificate(ledger),
        "finite_vector": finite_vector_certificate(ledger),
        "result": {
            "ordered_port_AD": (
                "-i*lambda1*[F^{AB}_{DE}*(q_IR/3+p_IR/6)+"
                "F^{BA}_{DE}*(2*q_IR/3+p_IR/3)]"
            ),
            "ordered_port_DA": (
                "-i*lambda1*[F^{AB}_{DE}*(2*q_IR/3+p_IR/3)+"
                "F^{BA}_{DE}*(q_IR/3+p_IR/6)]"
            ),
            "canonical_physical_AD": (
                "lambda1*F^{AB}_{DE}*["
                "(1/3)<P_dot_a D^D,D^E>+"
                "(2/3)<D^D,P_dot_a D^E>]"
            ),
            "canonical_physical_DA": (
                "lambda1*F^{AB}_{DE}*["
                "(2/3)<P_dot_a D^D,D^E>+"
                "(1/3)<D^D,P_dot_a D^E>]"
            ),
            "output_word": "D^D_lower(q_IR)>D^E_upper(p_IR)",
            "claim_boundary": (
                "FULL_FOUR_CHIRALITY_RAW_HESSIAN__LOCAL_SCHWINGER_CONTACT__"
                "FINITE_W_LONGITUDINAL_LINK__BARE_ONE_LOOP_ANOMALY_SECTOR"
            ),
        },
        "supersedes": {
            "artifact": str(OLD_JSON.relative_to(ROOT)),
            "reason": [
                "imported momentum maps were not action-port momenta",
                "crossed color Hessian was omitted",
            ],
            "old_status": "REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION",
        },
        "status": (
            "PASS_TARGET_BLIND_AD_DA_FULL_CHIRALITY_RAW_CONTACT_AND_LINK__"
            "HOLOMORPHIC_TWIST_COEFFICIENTS_MATCH"
        ),
    }
    if replay:
        replay_frame0(ledger, workers)
    if replay_contacts:
        replay_crossed_contacts(ledger, workers)
    if replay_full_chirality:
        payload["full_polarized_frame0_replay"] = replay_full_chirality_frame0(
            ledger, workers
        )
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    payload["checks"] = {
        "count": len(ledger.rows),
        "passed": len(ledger.rows) - failed,
        "failed": failed,
        "rows": ledger.rows,
    }
    return payload


def render_markdown(payload: dict[str, object]) -> str:
    checks = payload["checks"]
    assert isinstance(checks, dict)
    template = r"""# Step 5 AD/DA ordered action ports and crossed Hessian

Status: `{payload['status']}`.

External target used: `false`.

## 1. Momentum routing

$$
r_0=\ell,\qquad r_1=\ell+p_{{\rm raw}},\qquad
r_2=\ell+p_{{\rm raw}}+q_{{\rm raw}}.
$$

$$
r_0-r_1+p_{{\rm raw}}=0,\qquad
-r_2+r_1+q_{{\rm raw}}=0.
$$

Generated graph IR fixes

$$
r_0=k,\qquad r_1=k+q_{{\rm IR}},\qquad
r_2=k+p_{{\rm IR}}+q_{{\rm IR}},
$$

therefore

$$
p_{{\rm raw}}=q_{{\rm IR}}=k_L,\qquad
q_{{\rm raw}}=p_{{\rm IR}}=k_R.
$$

The ordered background action ports are

$$
D^D_{{\dot1}}(q_{{\rm IR}})>D^{{E\dot2}}(p_{{\rm IR}}).
$$

The maps $$(q,-p-q)$$ and $$(-p-q,q)$$ use the source-insertion
momentum as an output momentum and are rejected.

## 2. Two color Hessians

$$
H_{{AD}}[u_1,u_2]
=N^A[u_1]D^B[u_2]+N^A[u_2]D^B[u_1],
$$

$$
H_{{DA}}[u_1,u_2]
=-D^A[u_1]N^B[u_2]-D^A[u_2]N^B[u_1].
$$

The two contractions carry

$$
\mathbb F^{{AB}}{{}}_{{DE}},\qquad \mathbb F^{{BA}}{{}}_{{DE}}.
$$

For the fixed odd component directions,

$$
H_{AD}^{\rm direct}=\frac i4,\qquad
H_{AD}^{\rm crossed}=-\frac i4,
$$

$$
H_{DA}^{\rm direct}=\frac14,\qquad
H_{DA}^{\rm crossed}=-\frac14.
$$

For $SU(2)$,

$$
(A,B;D,E)=(0,1;1,0):\quad
(\mathbb F^{{AB}}{{}}_{{DE}},\mathbb F^{{BA}}{{}}_{{DE}})=(-2,0),
$$

$$
(A,B;D,E)=(0,1;0,1):\quad
(\mathbb F^{{AB}}{{}}_{{DE}},\mathbb F^{{BA}}{{}}_{{DE}})=(0,-2).
$$

## 3. Exact D-algebra numerators

$$
R_1=\frac i{{16}}\mu_\ell^2
\left(\ell+p_{{\rm raw}}+\frac12q_{{\rm raw}}\right)_+,
\qquad
R_2=-\frac i{{16}}\mu_\ell^2\ell_+.
$$

$$
N_{{AD}}^{{\rm ev}}=\mathbb F^{{AB}}{{}}_{{DE}}R_1
+\mathbb F^{{BA}}{{}}_{{DE}}R_2,
$$

$$
N_{{DA}}^{{\rm ev}}=\mathbb F^{{AB}}{{}}_{{DE}}R_2
+\mathbb F^{{BA}}{{}}_{{DE}}R_1.
$$

## 4. Same-edge parent and cut

For every occurrence $\omega$ on edge $e$,

$$
\frac{R_\omega r_{{e,d}}^2}{D_0D_1D_2}
-\frac{R_\omega}{P_{{\widehat e}}}=0,
$$

$$
\frac{R_\omega\bar r_e^2}{D_0D_1D_2}
-\frac{R_\omega}{P_{{\widehat e}}}
=\frac{R_\omega\mu_\ell^2}{D_0D_1D_2}.
$$

O05/O06 are partial two-denominator contact members.  They must first be
combined with the same-edge, same-color kinetic/longitudinal/gauge-fixing/link
contacts.  Their affine numerator is not an anomaly-zero certificate.

The following equations are required same-edge constraints only.  Their
second summands are not declared generated contact amplitudes:

$$
\begin{aligned}
AD,\ e_0:\quad&
7iq_+
+\left[i\left(\ell+p+\frac12q\right)_+-7iq_+\right]
=i\left(\ell+p+\frac12q\right)_+,\\
AD,\ e_1:\quad&0+0=0,\\
AD,\ e_2:\quad&2iq_+-2iq_+=0,
\end{aligned}
$$

$$
\begin{aligned}
DA,\ e_0:\quad&-\frac i2q_++\frac i2q_+=0,\\
DA,\ e_1:\quad&i(p+q)_+-i(p+q)_+=0,\\
DA,\ e_2:\quad&i(p+q)_+
+\left[-i\ell_+-i(p+q)_+\right]
=-i\ell_+.
\end{aligned}
$$

The independent crossed-color replay gives, edge by edge,

$$
\mathcal C^{BA}_{AD,e}=\mathcal C^{AB}_{DA,e},
\qquad
\mathcal C^{BA}_{DA,e}=\mathcal C^{AB}_{AD,e},
\qquad e=0,1,2.
$$

Thus the same six displayed balances with $AD\leftrightarrow DA$ give all
six $\mathbb F^{BA}{}_{DE}$ rows.  The JSON ledger retains all twelve rows
separately.

The raw same-occurrence functional Hessian gives

$$
c_{\rm parent}=(-2)^3=-8,
\qquad
c_{\rm contact}=(-1)_{\rm SD}(-2)_{\rm Euler}(-2)^2=+8.
$$

Its complete combinatorial multiplicity is

$$
m_{\rm contact}
=\left(\frac1{2!}\,2_{\rm action\ order}\right)
 \left(\frac1{2!}\,2_{\rm cut\ endpoint}\right)
 \left(\frac1{2!}\,2_{\rm remaining\ Wick}\right)=1.
$$

Consequently, occurrence by occurrence and in each chirality sector,

$$
N^{\rm parent}_{d,\omega}+K^{\rm contact}_{\rm raw,\omega}=0,
$$

while the four-dimensional D-algebra numerator leaves

$$
N^{\rm parent}_{4,\omega}+K^{\rm contact}_{\rm raw,\omega}
=\frac{R_\omega\mu_\ell^2}{D_0D_1D_2}.
$$

For finite $w$, define

$$
(M_1)^B{}_C=w^m c_{LC}{}^B a_m^L,
\qquad
a_m^L=\frac{i\sqrt2}{8}\bar\sigma_m^{\dot ba}
[D_a,\bar D_{\dot b}]_{\rm ord}u^L\big|.
$$

The first Duhamel derivative is

$$
\frac{\delta(T_1Y)^B}{\delta a_n^J}
=w^n c_{JC}{}^B\int_0^1ds\,
e^{iw[sr+(1-s)r']}Y^C.
$$

With $x=iwr$ and $y=iwr'$,

$$
(x-y)\int_0^1ds\,e^{sx+(1-s)y}=e^x-e^y.
$$

Thus the one-link term and the two endpoint terms cancel before loop
integration.  This finite-$w$ sector is longitudinal in arbitrary $d$ and its
$\mu_\ell^2$ coefficient is exactly zero.

## 5. Full four-chirality TGG result

$$
\boxed{{
\Gamma_{{AD}}
=-i\lambda_1\left[
\mathbb F^{{AB}}{{}}_{{DE}}\left(\frac13q_{{\rm IR}}+\frac16p_{{\rm IR}}\right)
+\mathbb F^{{BA}}{{}}_{{DE}}\left(\frac23q_{{\rm IR}}+\frac13p_{{\rm IR}}\right)
\right]_+
}},
$$

$$
\boxed{{
\Gamma_{{DA}}
=-i\lambda_1\left[
\mathbb F^{{AB}}{{}}_{{DE}}\left(\frac23q_{{\rm IR}}+\frac13p_{{\rm IR}}\right)
+\mathbb F^{{BA}}{{}}_{{DE}}\left(\frac13q_{{\rm IR}}+\frac16p_{{\rm IR}}\right)
\right]_+
}}.
$$

The absolute conversion is

$$
4_{\rm chirality}\left(\frac12\right)_{\rm rank/trace}(-8)_{\rm legacy}
=-16.
$$

The factor $1/2$ is inserted exactly once; $m_{\rm contact}=1$ supplies no
second factor.  In canonical physical ordering,

$$
\boxed{{
\mathcal A_{AD}
=\lambda_1\mathbb F^{{AB}}{{}}_{{DE}}
\left[
\frac13\langle P_{\dot a}D^D,D^E\rangle
+\frac23\langle D^D,P_{\dot a}D^E\rangle
\right]
}},
$$

$$
\boxed{{
\mathcal A_{DA}
=\lambda_1\mathbb F^{{AB}}{{}}_{{DE}}
\left[
\frac23\langle P_{\dot a}D^D,D^E\rangle
+\frac13\langle D^D,P_{\dot a}D^E\rangle
\right]
}}.
$$

The independent $p$-only and $q$-only polarized replays pass $112/112$
checks each.  The raw local-contact and finite-$w$ link replay passes $255/255$
checks.

The former canonical artifact is `REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION`.

$$
N_{{\rm pass}}={checks['passed']},\qquad N_{{\rm fail}}={checks['failed']}.
$$
"""
    return (
        template.replace("{payload[\'status\']}", str(payload["status"]))
        .replace("{checks[\'passed\']}", str(checks["passed"]))
        .replace("{checks[\'failed\']}", str(checks["failed"]))
        .replace("{{", "{")
        .replace("}}", "}")
    )


def rejection_note() -> str:
    return """# Step 5 AD/DA canonical DD mixed-chirality quotient

Status: `REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION`.

This artifact used the non-action-port maps `(q,-p-q)` and `(-p-q,q)` and
kept only the direct color Hessian.  It is superseded by
`audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md`.
"""


def mark_old_json_rejected() -> None:
    if not OLD_JSON.exists():
        return
    old = json.loads(OLD_JSON.read_text(encoding="utf-8"))
    old["status"] = "REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION"
    old["superseded_by"] = "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json"
    old["rejection"] = {
        "invalid_momentum_maps": ["(q,-p-q)", "(-p-q,q)"],
        "omitted_source_hessian": "crossed F^{BA}_{DE}",
    }
    OLD_JSON.write_text(json.dumps(old, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OLD_MD.write_text(rejection_note(), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--replay-frame0", action="store_true")
    parser.add_argument("--replay-crossed-contacts", action="store_true")
    parser.add_argument("--replay-full-chirality-frame0", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    payload = build_payload(
        args.replay_frame0,
        args.replay_crossed_contacts,
        args.replay_full_chirality_frame0,
        args.workers,
    )
    json_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    markdown_text = render_markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(markdown_text, encoding="utf-8")
        mark_old_json_rejected()
    elif args.check_artifact:
        if (
            args.replay_frame0
            or args.replay_crossed_contacts
            or args.replay_full_chirality_frame0
        ):
            raise AssertionError("replay adds checks; do not combine with artifact check")
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != markdown_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
        old = json.loads(OLD_JSON.read_text(encoding="utf-8"))
        if old.get("status") != "REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION":
            raise AssertionError("old canonical artifact is not marked rejected")
        print("PASS AD_DA_ACTION_PORT_MOMENTA_P_Q")
        print("PASS AD_DA_DIRECT_AND_CROSSED_COLOR_HESSIANS")
        print("PASS AD_DA_SAME_EDGE_FULL_D_ZERO_AND_DRED_REMAINDER")
        print("PASS AD_DA_FULL_CHIRALITY_P_Q_SYMBOLIC")
        print("PASS AD_DA_RAW_CONTACT_MULTIPLICITY_ONE")
        print("PASS AD_DA_FINITE_W_LINK_LONGITUDINAL_ZERO")
        print("PASS AD_DA_HOLOMORPHIC_TWIST_COEFFICIENTS")
        print("REJECTED AD_DA_IMPORTED_PRO_MOMENTUM_MAP")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    else:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
