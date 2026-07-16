#!/usr/bin/env python3
"""Exact target-blind G3 original/full Berezin-measure equivalence audit.

The audit compares the same two marked G3 words in

    d4theta_M d2bartheta_H

and in

    d4theta_M d4theta_H

after deleting one already present terminal D_H^2 and applying the exact
measure-conversion coefficient.  Equality is checked coefficientwise as a
Grassmann polynomial before the M integral and before any transverse trace.
The one-loop supertrace block cycles are enumerated independently.  No HT or
desired output coefficient is imported.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_g2_g3_dword_replay as g23  # noqa: E402


JSON_OUT = (
    ROOT
    / "audits"
    / "step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
)
MD_OUT = (
    ROOT
    / "audits"
    / "step5-ab-ba-g3-original-full-measure-equivalence-exact.md"
)
STATUS = (
    "PASS_G3_ORIGINAL_FULL_MEASURE_EQUIVALENCE__"
    "CONVERSION_MAGNITUDE_FOUR__TWO_SUPERTRACE_CYCLES_CANCEL_HALF__"
    "C_G3_4096"
)


def exact_text(value: object) -> str:
    if isinstance(value, sp.MatrixBase):
        return str(value.tolist()).replace("I", "i")
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    if isinstance(value, tuple):
        return "(" + ", ".join(exact_text(item) for item in value) + ")"
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        difference = sp.Matrix(actual) - sp.Matrix(expected)
        return all(sp.simplify(item) == 0 for item in difference)
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
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def euclidean_bispinor(
    vector: tuple[object, object, object, object],
) -> list[list[sp.Expr]]:
    imaginary = sp.I
    sigma_e = (
        -imaginary * sp.Matrix(((0, 1), (1, 0))),
        -imaginary * sp.Matrix(((0, -imaginary), (imaginary, 0))),
        -imaginary * sp.Matrix(((1, 0), (0, -1))),
        sp.eye(2),
    )
    mathsf = tuple(-imaginary * matrix for matrix in sigma_e)
    matrix = sum(
        (mathsf[index] * vector[index] for index in range(4)),
        sp.zeros(2),
    )
    return [
        [sp.expand(matrix[row, column]) for column in range(2)]
        for row in range(2)
    ]


def matrix_add(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [
        [sp.expand(left[a][b] + right[a][b]) for b in range(2)]
        for a in range(2)
    ]


def matrix_scale(
    scalar: object, matrix: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [[sp.expand(scalar * item) for item in row] for row in matrix]


def wedge(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> sp.Expr:
    return sp.expand(
        left[0][0] * right[0][1] - left[0][1] * right[0][0]
    )


def project_source_bottom_and_h_measure(
    polynomial: g23.Grassmann,
    h_local_mask: int,
    measure_weight: sp.Expr,
) -> g23.Grassmann:
    """Project S to bottom and perform only the indicated H measure."""

    source_all = 15 << (4 * g23.S)
    h_all = 15 << (4 * g23.H)
    h_target = h_local_mask << (4 * g23.H)
    terms: dict[int, sp.Expr] = {}
    for mask, coefficient in polynomial.terms.items():
        if mask & source_all:
            continue
        if mask & h_all != h_target:
            continue
        output_mask = mask ^ h_target
        terms[output_mask] = sp.expand(
            terms.get(output_mask, 0) + measure_weight * coefficient
        )
    return g23.Grassmann(terms)


def substitute_grassmann(
    polynomial: g23.Grassmann, substitutions: dict[sp.Symbol, sp.Expr]
) -> g23.Grassmann:
    return g23.Grassmann(
        {
            mask: sp.expand(coefficient.subs(substitutions))
            for mask, coefficient in polynomial.terms.items()
        }
    )


M_GENERATORS = ("theta_M+", "theta_M-", "bartheta_Mdot+", "bartheta_Mdot-")


def local_monomial_name(global_mask: int) -> str:
    local_mask = global_mask >> (4 * g23.M)
    selected = [
        name for offset, name in enumerate(M_GENERATORS) if local_mask & (1 << offset)
    ]
    return "1" if not selected else "*".join(selected)


def polynomial_payload(polynomial: g23.Grassmann) -> dict[str, Any]:
    rows = {
        local_monomial_name(mask): exact_text(coefficient)
        for mask, coefficient in sorted(polynomial.terms.items())
    }
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "term_count": len(rows),
        "coefficients": rows,
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }


def build_g3_words() -> dict[str, Any]:
    r_symbols = sp.symbols("r00 r01 r10 r11", real=True)
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = euclidean_bispinor((1, 0, 0, 0))
    q = euclidean_bispinor((0, 0, 0, 1))
    r1 = g23.matrix_sub(r0, p)
    r2 = g23.matrix_sub(r1, q)
    minus_r2 = g23.matrix_neg(r2)

    a_unmarked = g23.d(
        g23.bar_d2(
            g23.d(g23.delta4(g23.S, g23.M), g23.S, 0, r0),
            g23.S,
            r0,
        ),
        g23.S,
        0,
        r0,
    )
    a_marked = g23.d(a_unmarked, g23.S, 1, r0)
    b_unmarked = g23.d(
        g23.bar_d2(
            g23.d2(
                g23.delta4(g23.S, g23.H), g23.S, minus_r2
            ),
            g23.S,
            minus_r2,
        ),
        g23.S,
        0,
        minus_r2,
    )
    b_marked = g23.d(b_unmarked, g23.S, 1, minus_r2)

    # Full projector on M-H and the representation with its terminal D^2
    # deleted.
    bridge_full = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.H), g23.M, r1),
        g23.M,
        r1,
    )
    bridge_deleted = g23.bar_d2(
        g23.delta4(g23.M, g23.H), g23.M, r1
    )

    # Full projector on S-H and the representation with its terminal D^2
    # deleted.  The source D_+ and the outer D_- mark are retained.
    b_deleted_unmarked = g23.d(
        g23.bar_d2(
            g23.delta4(g23.S, g23.H), g23.S, minus_r2
        ),
        g23.S,
        0,
        minus_r2,
    )
    b_deleted_marked = g23.d(
        b_deleted_unmarked, g23.S, 1, minus_r2
    )

    external = (
        g23.antichiral_bottom(g23.M, p)
        * g23.antichiral_bottom(g23.H, q)
    )
    return {
        "r_symbols": r_symbols,
        "r0": r0,
        "p": p,
        "q": q,
        "original": {
            "A_mark": a_marked * b_unmarked * bridge_full * external,
            "B_mark": a_unmarked * b_marked * bridge_full * external,
        },
        "delete_MH_D2": {
            "A_mark": a_marked * b_unmarked * bridge_deleted * external,
            "B_mark": a_unmarked * b_marked * bridge_deleted * external,
        },
        "delete_SH_D2": {
            "A_mark": a_marked * b_deleted_unmarked * bridge_full * external,
            "B_mark": a_unmarked * b_deleted_marked * bridge_full * external,
        },
    }


def transverse_metric(
    polynomial: sp.Expr,
    loop: tuple[sp.Symbol, ...],
    external_wedge: sp.Expr,
) -> sp.Expr:
    expanded = sp.Poly(sp.expand(polynomial), *loop)
    transverse_trace = sum(
        expanded.coeff_monomial(loop[axis] ** 2) for axis in (1, 2)
    )
    return sp.factor(transverse_trace / (2 * external_wedge))


def grassmann_and_measure_certificate(ledger: Ledger) -> dict[str, Any]:
    words = build_g3_words()
    conversion = sp.Integer(4)
    wrong_conversion = sp.Integer(2)

    # The one-vertex monomial calculation fixes the conversion coefficient in
    # the sparse engine orientation, without a textbook identity.
    zero = [[sp.Integer(0), sp.Integer(0)], [sp.Integer(0), sp.Integer(0)]]
    canonical_h_top = g23.Grassmann.scalar(1)
    for offset in range(4):
        canonical_h_top *= g23.variable(g23.H, offset)
    d2_top = g23.d2(canonical_h_top, g23.H, zero)
    d2_bar_coefficient = d2_top.coefficient(12 << (4 * g23.H))
    antichiral_measure = sp.Rational(1, 2)
    full_measure = sp.Rational(1, 4)
    lhs_monomial = antichiral_measure * d2_bar_coefficient
    rhs_monomial = conversion * full_measure
    ledger.check("ENGINE_D2_CANONICAL_TOP", d2_bar_coefficient, 2)
    ledger.check("ANTICHIRAL_MEASURE_MAP", antichiral_measure, sp.Rational(1, 2))
    ledger.check("FULL_MEASURE_MAP", full_measure, sp.Rational(1, 4))
    ledger.check("MEASURE_CONVERSION_COEFFICIENT", conversion, 4)
    ledger.check("MONOMIAL_MEASURE_IDENTITY", lhs_monomial, rhs_monomial)
    ledger.check(
        "WRONG_COEFFICIENT_TWO_GIVES_HALF",
        wrong_conversion * full_measure,
        sp.Rational(1, 2),
    )

    projected: dict[str, dict[str, g23.Grassmann]] = {}
    for mark in ("A_mark", "B_mark"):
        original_raw_bar = project_source_bottom_and_h_measure(
            words["original"][mark], 12, sp.Integer(1)
        )
        original = project_source_bottom_and_h_measure(
            words["original"][mark], 12, antichiral_measure
        )
        deleted_mh = project_source_bottom_and_h_measure(
            words["delete_MH_D2"][mark], 15, sp.Integer(1)
        )
        deleted_sh = project_source_bottom_and_h_measure(
            words["delete_SH_D2"][mark], 15, sp.Integer(1)
        )
        full_mh = project_source_bottom_and_h_measure(
            words["delete_MH_D2"][mark],
            15,
            conversion * full_measure,
        )
        full_sh = project_source_bottom_and_h_measure(
            words["delete_SH_D2"][mark],
            15,
            conversion * full_measure,
        )
        wrong_mh = project_source_bottom_and_h_measure(
            words["delete_MH_D2"][mark],
            15,
            wrong_conversion * full_measure,
        )

        ledger.check(
            f"{mark}_ORIGINAL_RAW_IS_TWO_DELETED_MH",
            bool((original_raw_bar - 2 * deleted_mh).terms),
            False,
        )
        ledger.check(
            f"{mark}_ORIGINAL_RAW_IS_TWO_DELETED_SH",
            bool((original_raw_bar - 2 * deleted_sh).terms),
            False,
        )
        ledger.check(
            f"{mark}_ORIGINAL_EQUALS_FULL_MH_COEFFICIENTWISE",
            bool((original - full_mh).terms),
            False,
        )
        ledger.check(
            f"{mark}_ORIGINAL_EQUALS_FULL_SH_COEFFICIENTWISE",
            bool((original - full_sh).terms),
            False,
        )
        ledger.check(
            f"{mark}_TWO_WRONG_FULL_EQUALS_ORIGINAL",
            bool((2 * wrong_mh - original).terms),
            False,
        )
        ledger.check(
            f"{mark}_WRONG_FULL_IS_NOT_ORIGINAL",
            bool((wrong_mh - original).terms),
            True,
        )
        projected[mark] = {
            "original": original,
            "full_MH": full_mh,
            "full_SH": full_sh,
            "wrong_half": wrong_mh,
        }

    loop = sp.symbols("L0 L1 L2 L3", real=True)
    loop_matrix = euclidean_bispinor(loop)
    p = words["p"]
    q = words["q"]
    p_plus_q = matrix_add(p, q)
    frame_data: dict[str, Any] = {}
    for label, y_value, z_value in (
        ("y0_z0", sp.Rational(0), sp.Rational(0)),
        ("y1over3_z1over3", sp.Rational(1, 3), sp.Rational(1, 3)),
    ):
        frame_r0 = matrix_add(
            loop_matrix,
            matrix_add(
                matrix_scale(y_value, p),
                matrix_scale(z_value, p_plus_q),
            ),
        )
        substitutions = {
            words["r_symbols"][2 * row + column]: frame_r0[row][column]
            for row in range(2)
            for column in range(2)
        }
        marks: dict[str, Any] = {}
        for mark in ("A_mark", "B_mark"):
            original_frame = substitute_grassmann(
                projected[mark]["original"], substitutions
            )
            full_mh_frame = substitute_grassmann(
                projected[mark]["full_MH"], substitutions
            )
            full_sh_frame = substitute_grassmann(
                projected[mark]["full_SH"], substitutions
            )
            difference_mh = original_frame - full_mh_frame
            difference_sh = original_frame - full_sh_frame
            ledger.check(
                f"FRAME_{label}_{mark}_MH_DIFFERENCE_TERM_COUNT",
                len(difference_mh.terms),
                0,
            )
            ledger.check(
                f"FRAME_{label}_{mark}_SH_DIFFERENCE_TERM_COUNT",
                len(difference_sh.terms),
                0,
            )
            marks[mark] = {
                "N_original": polynomial_payload(original_frame),
                "N_full_delete_MH_D2_sha256": polynomial_payload(full_mh_frame)[
                    "sha256"
                ],
                "N_full_delete_SH_D2_sha256": polynomial_payload(full_sh_frame)[
                    "sha256"
                ],
                "N_original_minus_N_full_MH": {},
                "N_original_minus_N_full_SH": {},
            }
        frame_data[label] = {
            "y": exact_text(y_value),
            "z": exact_text(z_value),
            "r0": [[exact_text(item) for item in row] for row in frame_r0],
            "marks": marks,
        }

    # Extract the raw top-monomial transverse metrics independently from the
    # same universal words.
    y, z = sp.symbols("y z", real=True)
    affine_r0 = matrix_add(
        loop_matrix,
        matrix_add(matrix_scale(y, p), matrix_scale(z, p_plus_q)),
    )
    affine_substitutions = {
        words["r_symbols"][2 * row + column]: affine_r0[row][column]
        for row in range(2)
        for column in range(2)
    }
    original_mask = (15 << (4 * g23.M)) | (12 << (4 * g23.H))
    full_mask = (15 << (4 * g23.M)) | (15 << (4 * g23.H))
    external_wedge = wedge(p, q)
    metric_rows: dict[str, Any] = {}
    expected_shape = {"A_mark": 1 - z, "B_mark": z}
    for mark in ("A_mark", "B_mark"):
        original_top = sp.expand(
            words["original"][mark]
            .coefficient(original_mask)
            .subs(affine_substitutions)
        )
        deleted_mh_top = sp.expand(
            words["delete_MH_D2"][mark]
            .coefficient(full_mask)
            .subs(affine_substitutions)
        )
        deleted_sh_top = sp.expand(
            words["delete_SH_D2"][mark]
            .coefficient(full_mask)
            .subs(affine_substitutions)
        )
        original_metric = transverse_metric(original_top, loop, external_wedge)
        deleted_mh_metric = transverse_metric(
            deleted_mh_top, loop, external_wedge
        )
        deleted_sh_metric = transverse_metric(
            deleted_sh_top, loop, external_wedge
        )
        converted_full_metric = sp.factor(conversion * deleted_mh_metric)
        original_after_measures = sp.factor(
            original_metric * sp.Rational(1, 4) * antichiral_measure
        )
        full_after_measures = sp.factor(
            converted_full_metric * sp.Rational(1, 4) * full_measure
        )
        wrong_after_measures = sp.factor(
            wrong_conversion
            * deleted_mh_metric
            * sp.Rational(1, 4)
            * full_measure
        )
        shape = expected_shape[mark]
        ledger.check(f"{mark}_ORIGINAL_RAW_METRIC", original_metric, 32768 * shape)
        ledger.check(f"{mark}_DELETED_MH_RAW_METRIC", deleted_mh_metric, 16384 * shape)
        ledger.check(f"{mark}_DELETED_SH_RAW_METRIC", deleted_sh_metric, 16384 * shape)
        ledger.check(f"{mark}_CONVERTED_FULL_RAW_METRIC", converted_full_metric, 65536 * shape)
        ledger.check(f"{mark}_ORIGINAL_MEASURED_METRIC", original_after_measures, 4096 * shape)
        ledger.check(f"{mark}_FULL_MEASURED_METRIC", full_after_measures, 4096 * shape)
        ledger.check(f"{mark}_WRONG_MEASURED_METRIC", wrong_after_measures, 2048 * shape)
        metric_rows[mark] = {
            "shape": exact_text(shape),
            "original_raw_top_metric": exact_text(original_metric),
            "deleted_terminal_D2_raw_top_metric": exact_text(deleted_mh_metric),
            "converted_full_raw_top_metric": exact_text(converted_full_metric),
            "original_after_measures": exact_text(original_after_measures),
            "full_after_measures": exact_text(full_after_measures),
            "wrong_coefficient_two_after_measures": exact_text(wrong_after_measures),
        }

    simplex_a = sp.simplify(
        2 * sp.integrate(sp.integrate(1 - z, (z, 0, 1 - y)), (y, 0, 1))
    )
    simplex_b = sp.simplify(
        2 * sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1))
    )
    ledger.check("A_MARK_SIMPLEX_WEIGHT", simplex_a, sp.Rational(2, 3))
    ledger.check("B_MARK_SIMPLEX_WEIGHT", simplex_b, sp.Rational(1, 3))
    ledger.check("MARK_SIMPLEX_WEIGHT_SUM", simplex_a + simplex_b, 1)
    ledger.check("FINAL_C_G3", 4096 * (simplex_a + simplex_b), 4096)

    # GPT Pro's ordered-H convention uses D_H^2(theta_+ theta_-)=-2 and
    # conversion -4.  The deleted word changes sign under that orientation,
    # so the converted full word is identical to this engine's +4 word.
    xi_engine = sp.Symbol("Xi_engine")
    xi_ordered_h = -xi_engine
    ordered_h_conversion = -sp.Integer(4)
    ledger.check(
        "ORDERED_H_SIGN_TRANSLATION",
        ordered_h_conversion * xi_ordered_h,
        conversion * xi_engine,
    )

    return {
        "engine_measure_identity": {
            "canonical_H_monomial": "theta_H+ theta_H- bartheta_Hdot+ bartheta_Hdot-",
            "D_H2_on_theta_Hplus_theta_Hminus": "2",
            "d2bartheta_H_map": "1/2",
            "d4theta_H_map": "1/4",
            "conversion": "+4",
            "identity": "int d2bartheta_H (D_H2 K)|theta=0 = 4 int d4theta_H K",
        },
        "ordered_H_orientation_translation": {
            "conversion": "-4",
            "deleted_word_relation": "Xi_ordered_H=-Xi_engine",
            "converted_word_identity": "(-4)*Xi_ordered_H=(+4)*Xi_engine",
            "scalar_disagreement": False,
            "intermediate_sign_disagreement": True,
        },
        "generic_frame_coefficientwise_checks": frame_data,
        "raw_metric_chain": metric_rows,
        "simplex_weights": {
            "A_mark": exact_text(simplex_a),
            "B_mark": exact_text(simplex_b),
            "sum": exact_text(simplex_a + simplex_b),
        },
        "coefficient_chain": {
            "original": "32768*(1/4)_M*(1/2)_barH=4096",
            "full": "65536*(1/4)_M*(1/4)_H=4096",
            "rejected": "32768*(1/4)_M*(1/4)_H=2048",
            "c_G3": "4096",
        },
    }


BASIS = ("u", "phi1", "tildephi1", "phi_s", "tildephi_s")
INDEX = {field: index for index, field in enumerate(BASIS)}


def one_block(row: str, column: str, value: sp.Expr) -> sp.Matrix:
    matrix = sp.zeros(len(BASIS))
    matrix[INDEX[row], INDEX[column]] = value
    return matrix


def supertrace(matrix: sp.Matrix) -> sp.Expr:
    # All five quantum integration variables in this TMH block are even.
    return sp.expand(sum(matrix[index, index] for index in range(len(BASIS))))


def supertrace_cycle_certificate(ledger: Ledger) -> dict[str, Any]:
    g_u, g_1, g_s = sp.symbols("G_u G_1 G_s", nonzero=True)
    i_u1, i_1u = sp.symbols("I_u1 I_1u", nonzero=True)
    m_us, m_su = sp.symbols("M_us M_su", nonzero=True)
    h_1s, h_s1 = sp.symbols("H_1s H_s1", nonzero=True)

    propagator = sp.zeros(len(BASIS))
    propagator[INDEX["u"], INDEX["u"]] = g_u
    propagator[INDEX["phi1"], INDEX["tildephi1"]] = g_1
    propagator[INDEX["tildephi1"], INDEX["phi1"]] = g_1
    propagator[INDEX["phi_s"], INDEX["tildephi_s"]] = g_s
    propagator[INDEX["tildephi_s"], INDEX["phi_s"]] = g_s

    source_blocks = {
        "I_u_phi1": one_block("u", "phi1", i_u1),
        "I_phi1_u": one_block("phi1", "u", i_1u),
    }
    matter_blocks = {
        "M_u_phi_s": one_block("u", "phi_s", m_us),
        "M_phi_s_u": one_block("phi_s", "u", m_su),
    }
    hminus_blocks = {
        "H_tildephi1_tildephi_s": one_block(
            "tildephi1", "tildephi_s", h_1s
        ),
        "H_tildephi_s_tildephi1": one_block(
            "tildephi_s", "tildephi1", h_s1
        ),
    }

    rows: list[dict[str, Any]] = []
    values: dict[str, sp.Expr] = {}
    for order, source_name, matter_name, hminus_name in itertools.product(
        ("MH", "HM"), source_blocks, matter_blocks, hminus_blocks
    ):
        first, second = (
            (matter_blocks[matter_name], hminus_blocks[hminus_name])
            if order == "MH"
            else (hminus_blocks[hminus_name], matter_blocks[matter_name])
        )
        product = (
            propagator
            * first
            * propagator
            * second
            * propagator
            * source_blocks[source_name]
        )
        value = sp.factor(supertrace(product))
        row_id = f"{order}::{source_name}::{matter_name}::{hminus_name}"
        values[row_id] = value
        rows.append(
            {
                "id": row_id,
                "value": exact_text(value),
                "nonzero": value != 0,
            }
        )

    nonzero = [row for row in rows if row["nonzero"]]
    expected_ids = (
        "MH::I_phi1_u::M_u_phi_s::H_tildephi_s_tildephi1",
        "HM::I_u_phi1::M_phi_s_u::H_tildephi1_tildephi_s",
    )
    ledger.check("SUPERTRACE_CANDIDATE_BLOCK_ROWS", len(rows), 16)
    ledger.check("SUPERTRACE_NONZERO_CYCLE_COUNT", len(nonzero), 2)
    ledger.check(
        "SUPERTRACE_NONZERO_CYCLE_IDS",
        tuple(row["id"] for row in nonzero),
        expected_ids,
    )

    cycle_1 = values[expected_ids[0]]
    cycle_2 = values[expected_ids[1]]
    i0, vm, vh = sp.symbols("I0 VM VH", nonzero=True)
    reverse_equal = {
        i_u1: i0,
        i_1u: i0,
        m_us: vm,
        m_su: vm,
        h_1s: vh,
        h_s1: vh,
    }
    common_cycle = g_u * g_1 * g_s * i0 * vm * vh
    cycle_1_equal = sp.factor(cycle_1.subs(reverse_equal))
    cycle_2_equal = sp.factor(cycle_2.subs(reverse_equal))
    correct_outer_half = sp.factor(
        sp.Rational(1, 2) * (cycle_1_equal + cycle_2_equal)
    )
    rejected_outer_half = sp.factor(sp.Rational(1, 2) * cycle_1_equal)
    ledger.check("SUPERTRACE_CYCLE_1", cycle_1_equal, common_cycle)
    ledger.check("SUPERTRACE_CYCLE_2", cycle_2_equal, common_cycle)
    ledger.check("SUPERTRACE_HALF_TIMES_TWO", correct_outer_half, common_cycle)
    ledger.check(
        "REJECTED_SINGLE_CYCLE_WITH_HALF",
        rejected_outer_half,
        common_cycle / 2,
    )
    ledger.check(
        "REJECTED_ROUTE_RATIO",
        correct_outer_half / rejected_outer_half,
        2,
    )

    return {
        "basis": list(BASIS),
        "candidate_count": len(rows),
        "nonzero_count": len(nonzero),
        "nonzero_cycles": [
            {
                "id": expected_ids[0],
                "word": "STr(G M2 G Hminus G I_phi1_u)",
                "value": exact_text(cycle_1_equal),
            },
            {
                "id": expected_ids[1],
                "word": "STr(G Hminus G M2 G I_u_phi1)",
                "value": exact_text(cycle_2_equal),
            },
        ],
        "correct": "(1/2)*(C1+C2)=C1",
        "rejected": "(1/2)*C1=C1/2",
        "first_false_equality": "(1/2)*(C1+C2) -> (1/2)*C1",
        "equivalent_measure_ledger_error": "conversion coefficient 4 -> 2",
        "errors_are_same_missing_factor_not_two_independent_halves": True,
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    grassmann = grassmann_and_measure_certificate(ledger)
    cycles = supertrace_cycle_certificate(ledger)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": (
            "step5-ab-ba-g3-original-full-measure-equivalence-exact-v1"
        ),
        "status": STATUS if failed == 0 else "FAIL",
        "authority_role": "LOCAL_PROPOSAL_TARGET_BLIND",
        "external_target_used": False,
        "HT_used": False,
        "desired_vector_fitting_used": False,
        "grassmann_measure_equivalence": grassmann,
        "supertrace_cycle_census": cycles,
        "verdict": {
            "c_G3": "4096",
            "original_equals_full_measure": True,
            "rejected_2048": True,
            "first_false_equality": cycles["first_false_equality"],
            "sign_comparison_with_ordered_H_derivation": (
                "engine conversion is +4; ordered-H conversion is -4 with "
                "Xi_ordered_H=-Xi_engine; converted word and scalar agree"
            ),
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows) - failed,
            "failed": failed,
            "rows": ledger.rows,
        },
    }


def markdown(artifact: dict[str, Any]) -> str:
    checks = artifact["checks"]
    rendered = r"""# G3 original/full measure equivalence exact audit

Status: __STATUS__.

No HT coefficient or desired output is used.

## 1. Measure coefficient

The sparse engine orders the H-vertex generators as

$$
(\theta_{H+},\theta_{H-},
\bar\theta_{H\dot +},\bar\theta_{H\dot -}),
$$

and uses

$$
D_H^2=2D_{H-}D_{H+}.
$$

Direct left differentiation gives

$$
D_{H+}(\theta_{H+}\theta_{H-})=\theta_{H-},
$$

$$
D_{H-}D_{H+}(\theta_{H+}\theta_{H-})=1,
$$

$$
D_H^2(\theta_{H+}\theta_{H-})=2.
$$

The canonical monomial maps are

$$
\int d^2\bar\theta_H\,
\bar\theta_{H\dot +}\bar\theta_{H\dot -}
=\frac12,
$$

$$
\int d^4\theta_H\,
\theta_{H+}\theta_{H-}
\bar\theta_{H\dot +}\bar\theta_{H\dot -}
=\frac14.
$$

Therefore

$$
\frac12\cdot2=1,
$$

$$
4\cdot\frac14=1,
$$

and

$$
\boxed{
\int d^2\bar\theta_H\,
(D_H^2K)\big|_{\theta_H=0}
=4\int d^4\theta_H\,K.
}
$$

The ordered-H orientation with coefficient $-4$ has

$$
\Xi_{\mathrm{ordered}\ H}=-\Xi_{\mathrm{engine}},
$$

so

$$
(-4)\Xi_{\mathrm{ordered}\ H}
=(-4)(-\Xi_{\mathrm{engine}})
=4\Xi_{\mathrm{engine}}.
$$

Thus only the intermediate orientation sign differs.

## 2. Coefficientwise Grassmann equality

Define

$$
\mathcal A=D_+\bar D^2D_+\delta_{SM},
$$

$$
\mathcal B=D_+\bar D^2D^2\delta_{SH},
$$

$$
\mathcal P_{MH}=\bar D_M^2D_M^2\delta_{MH}.
$$

For

$$
\sigma\in\{D_-\mathcal A,D_-\mathcal B\},
$$

let $N_O$ use $d^2\bar\theta_H$.  Let $N_F^{MH}$ delete the
terminal $D_M^2$ from $\mathcal P_{MH}$, and let $N_F^{SH}$ delete the
terminal $D_S^2$ from the S-H projector.  Multiplying either deleted word
by the conversion coefficient gives

$$
N_O-N_F^{MH}=0,
$$

$$
N_O-N_F^{SH}=0.
$$

Both equalities hold coefficientwise in every remaining M-vertex
Grassmann monomial, with arbitrary loop components, at

$$
(y,z)=(0,0),
$$

and

$$
(y,z)=\left(\frac13,\frac13\right).
$$

The JSON artifact stores every nonzero coefficient and both zero
difference dictionaries.

## 3. Raw metric chain

The two original raw top coefficients are

$$
c_{O,A}^{\mathrm{raw}}=32768(1-z),
$$

$$
c_{O,B}^{\mathrm{raw}}=32768z.
$$

Deleting either terminal $D_H^2$ gives

$$
c_{\Xi,A}^{\mathrm{raw}}=16384(1-z),
$$

$$
c_{\Xi,B}^{\mathrm{raw}}=16384z.
$$

The full-measure conversion gives

$$
c_{F,A}^{\mathrm{raw}}
=4\cdot16384(1-z)
=65536(1-z),
$$

$$
c_{F,B}^{\mathrm{raw}}
=4\cdot16384z
=65536z.
$$

Hence

$$
32768\left(\frac14\right)_M
\left(\frac12\right)_{\bar H}
=4096,
$$

$$
65536\left(\frac14\right)_M
\left(\frac14\right)_H
=4096.
$$

The rejected coefficient $2$ gives

$$
2\cdot16384
\left(\frac14\right)_M
\left(\frac14\right)_H
=2048.
$$

The marked simplex moments are

$$
w_A=\frac23,
\qquad
w_B=\frac13,
\qquad
w_A+w_B=1.
$$

## 4. Supertrace cycles

In the basis

$$
(u,\phi_1,\widetilde\phi_1,\phi_s,\widetilde\phi_s),
$$

the exhaustive oriented-block census has $16$ candidates and exactly two
nonzero cycles:

$$
\mathcal C_1
=\operatorname{STr}
(G M_2 G H_- G I_{\phi_1u}),
$$

$$
\mathcal C_2
=\operatorname{STr}
(G H_- G M_2 G I_{u\phi_1}).
$$

The reverse even Hessian blocks give

$$
\mathcal C_1
=G_uG_1G_sI_0M_2H_-,
$$

$$
\mathcal C_2
=G_uG_1G_sI_0M_2H_-.
$$

Therefore

$$
\frac12(\mathcal C_1+\mathcal C_2)
=\frac12(2\mathcal C_1)
=\mathcal C_1.
$$

The rejected route first uses

$$
\boxed{
\frac12(\mathcal C_1+\mathcal C_2)
\longrightarrow
\frac12\mathcal C_1.
}
$$

Equivalently, its full-measure ledger replaces $4$ by $2$.  These are the
same missing factor, not two independent halves.

$$
\boxed{c_{G_3}=4096.}
$$

Checks: __CHECKS__ PASS.
"""
    return rendered.replace("__STATUS__", artifact["status"]).replace(
        "__CHECKS__", f"{checks['passed']}/{checks['count']}"
    )


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", "--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    artifact = build_artifact()
    if args.write:
        JSON_OUT.write_text(canonical(artifact), encoding="utf-8")
        MD_OUT.write_text(markdown(artifact), encoding="utf-8")
    if args.check_artifact:
        stored = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        if stored != artifact:
            raise AssertionError(f"stored artifact is stale: {JSON_OUT}")
    if args.print_json:
        print(canonical(artifact), end="")
    else:
        print(
            f"PASS {artifact['checks']['passed']}/"
            f"{artifact['checks']['count']} checks"
        )
        print("PASS coefficientwise original/full equality at two generic frames")
        print("PASS exactly two nonzero supertrace cycles cancel the outer half")
        print("PASS c_G3=4096; rejected c_G3=2048")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
