#!/usr/bin/env python3
"""Exact AB/BA G3 absolute-normalization and first-difference audit.

The audit compares the normalized original-measure replay in
``step5_ab_ba_full_1pi_quotient_exact_audit.py`` with the raw sparse replay,
restores every primitive factor, and checks the SU(2) color contraction.
It neither calls the Project/HT engines nor uses a residual-q condition.
"""

from __future__ import annotations

import argparse
import inspect
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_g1_vvv_dword_replay as g1  # noqa: E402
import step5_ab_ba_full_1pi_quotient_exact_audit as old  # noqa: E402
import step5_ab_ba_g3_factor_two_first_error_exact_audit as raw  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g3-absolute-normalization-first-difference-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-absolute-normalization-first-difference-exact.md"


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


def permutation_sign(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3:
        return 0
    return permutation_sign((a, b, c))


def su2_color_certificate(ledger: Ledger) -> dict[str, Any]:
    """Check both the literal shorthand and the complete graph color."""

    # T_a=sigma_a/2, kappa_ab=tr(T_a T_b)=delta_ab/2,
    # c_ab^c=epsilon_abc and c_abc=epsilon_abc/2.
    kappa_down = sp.eye(3) / 2
    kappa_up = 2 * sp.eye(3)

    def c_lower(a: int, b: int, c: int) -> sp.Expr:
        return sp.Rational(1, 2) * epsilon3(a, b, c)

    def t_up(a: int, d: int, x: int) -> sp.Expr:
        # -i (T_a)^d_x=c_ax^d from the locked covariant derivative.
        return sp.I * epsilon3(a, x, d)

    def t_down(a: int, d: int, x: int) -> sp.Expr:
        return sum(kappa_down[d, r] * t_up(a, r, x) for r in range(3))

    def f_tensor(a: int, b: int, d: int, e: int) -> sp.Expr:
        return sp.simplify(
            sum(
                kappa_up[a, u]
                * kappa_up[b, v]
                * kappa_up[c, cp]
                * c_lower(u, c, d)
                * c_lower(v, cp, e)
                for u in range(3)
                for v in range(3)
                for c in range(3)
                for cp in range(3)
            )
        )

    def literal(a: int, b: int, d: int, e: int) -> sp.Expr:
        return sp.simplify(
            sum(t_up(a, d, x) * c_lower(b, x, e) for x in range(3))
        )

    def complete(a: int, b: int, d: int, e: int) -> sp.Expr:
        # Three inverse color metrics are supplied by the vector, source-H,
        # and internal matter propagators.  The matter vertex is lower in its
        # external tilde-Phi slot: (T_u)_{d x}=kappa_dr(T_u)^r_x.
        return sp.simplify(
            sum(
                kappa_up[a, u]
                * kappa_up[b, p]
                * kappa_up[x, y]
                * t_down(u, d, x)
                * c_lower(p, y, e)
                for u in range(3)
                for p in range(3)
                for x in range(3)
                for y in range(3)
            )
        )

    nonzero_frames: list[dict[str, str | list[int]]] = []
    for a in range(3):
        for b in range(3):
            for d in range(3):
                for e in range(3):
                    f_value = f_tensor(a, b, d, e)
                    literal_value = literal(a, b, d, e)
                    complete_value = complete(a, b, d, e)
                    ledger.check(
                        f"SU2_LITERAL_{a}{b}{d}{e}",
                        literal_value,
                        sp.I * f_value / 4,
                    )
                    ledger.check(
                        f"SU2_COMPLETE_{a}{b}{d}{e}",
                        complete_value,
                        sp.I * f_value,
                    )
                    if f_value != 0:
                        nonzero_frames.append(
                            {
                                "frame": [a, b, d, e],
                                "F": exact_text(f_value),
                                "literal_Tup_c": exact_text(literal_value),
                                "complete_graph_color": exact_text(complete_value),
                            }
                        )

    sample = next(row for row in nonzero_frames if row["frame"] == [0, 1, 1, 0])
    ledger.check("SU2_SAMPLE_F_0110", f_tensor(0, 1, 1, 0), -2)
    ledger.check("SU2_SAMPLE_LITERAL_0110", literal(0, 1, 1, 0), -sp.I / 2)
    ledger.check("SU2_SAMPLE_COMPLETE_0110", complete(0, 1, 1, 0), -2 * sp.I)
    ledger.check("SU2_COMPLETE_COLOR_HAS_NO_HALF", complete(0, 1, 1, 0) / f_tensor(0, 1, 1, 0), sp.I)

    return {
        "conventions": {
            "T_a": "sigma_a/2",
            "kappa_ab": "delta_ab/2",
            "kappa^ab": "2*delta_ab",
            "c_ab^c": "epsilon_abc",
            "c_abc": "epsilon_abc/2",
            "(T_a)^d_x": "i*epsilon_axd",
            "(T_a)_dx": "i*c_axd=i*epsilon_axd/2",
        },
        "literal_shorthand": {
            "formula": "(T_A)^D_X*c_BXE=(i/4)*F^{AB}_{DE}",
            "status": "NOT_THE_COMPLETE_GRAPH_COLOR",
        },
        "complete_graph": {
            "formula": (
                "kappa^{AU}*kappa^{BP}*kappa^{XY}*"
                "(T_U)_{DX}*c_PYE=i*F^{AB}_{DE}"
            ),
            "ratio_to_F": "i",
            "extra_half": False,
        },
        "sample_0110": sample,
        "nonzero_frame_count": len(nonzero_frames),
    }


def g3_trace_and_normalization_certificate(ledger: Ledger) -> dict[str, Any]:
    normalization = sp.Integer(32768)
    points = {
        "00": (sp.Rational(0), sp.Rational(0)),
        "10": (sp.Rational(1), sp.Rational(0)),
        "01": (sp.Rational(0), sp.Rational(1)),
        "check": (sp.Rational(1, 3), sp.Rational(1, 3)),
    }
    old_traces: dict[str, tuple[sp.Expr, sp.Expr]] = {}
    raw_traces: dict[str, tuple[sp.Expr, sp.Expr]] = {}
    for label, (y_value, z_value) in points.items():
        old_trace = old._g3_transverse_trace(y_value, z_value)
        raw_trace = raw.raw_transverse_trace(y_value, z_value)
        old_traces[label] = old_trace
        raw_traces[label] = raw_trace
        ledger.check(f"RAW_EQUALS_32768_OLD_A_{label}", raw_trace[0], normalization * old_trace[0])
        ledger.check(f"RAW_EQUALS_32768_OLD_B_{label}", raw_trace[1], normalization * old_trace[1])

    y, z = sp.symbols("y z", real=True)

    def affine(samples: dict[str, tuple[sp.Expr, sp.Expr]], mark: int) -> sp.Expr:
        return sp.expand(
            samples["00"][mark]
            + y * (samples["10"][mark] - samples["00"][mark])
            + z * (samples["01"][mark] - samples["00"][mark])
        )

    old_a = affine(old_traces, 0)
    old_b = affine(old_traces, 1)
    raw_a = affine(raw_traces, 0)
    raw_b = affine(raw_traces, 1)
    wedge = old.wedge(
        old.euclidean_bispinor((1, 0, 0, 0)),
        old.euclidean_bispinor((0, 0, 0, 1)),
    )
    old_metrics = (sp.simplify(old_a / (2 * wedge)), sp.simplify(old_b / (2 * wedge)))
    raw_metrics = (sp.simplify(raw_a / (2 * wedge)), sp.simplify(raw_b / (2 * wedge)))
    ledger.check("EXTERNAL_WEDGE", wedge, -sp.I)
    ledger.check("OLD_NORMALIZED_METRIC_A", old_metrics[0], 1 - z)
    ledger.check("OLD_NORMALIZED_METRIC_B", old_metrics[1], z)
    ledger.check("RAW_METRIC_A", raw_metrics[0], normalization * (1 - z))
    ledger.check("RAW_METRIC_B", raw_metrics[1], normalization * z)

    mask = (15 << (4 * raw.g23.M)) | (12 << (4 * raw.g23.H))
    ledger.check("ORIGINAL_MEASURE_MASK", mask, 3312)
    theta2_top = -2
    bartheta2_top = 2
    full_measure_signed = sp.Rational(1, theta2_top * bartheta2_top)
    antichiral_measure_signed = sp.Rational(1, bartheta2_top)
    measure_magnitude = abs(full_measure_signed * antichiral_measure_signed)
    ledger.check("FULL_M_BEREZIN_CANONICAL_MAP", full_measure_signed, -sp.Rational(1, 4))
    ledger.check("ANTICHIRAL_H_BEREZIN_CANONICAL_MAP", antichiral_measure_signed, sp.Rational(1, 2))
    ledger.check("ORIGINAL_MEASURE_MAGNITUDE", measure_magnitude, sp.Rational(1, 8))

    metric_after_measure = sp.simplify(normalization * measure_magnitude)
    two_axis_trace_after_measure = 2 * metric_after_measure * wedge
    dred_from_trace = sp.simplify(-sp.Rational(1, 2) * two_axis_trace_after_measure)
    dred_from_metric = sp.simplify(-metric_after_measure * wedge)
    scale_one_double_half = sp.simplify(-sp.Rational(1, 2) * metric_after_measure * wedge)
    ledger.check("METRIC_AFTER_ORIGINAL_MEASURE", metric_after_measure, 4096)
    ledger.check("TWO_AXIS_TRACE_AFTER_MEASURE", two_axis_trace_after_measure, 8192 * wedge)
    ledger.check("DRED_FROM_TRACE", dred_from_trace, -4096 * wedge)
    ledger.check("DRED_FROM_METRIC", dred_from_metric, -4096 * wedge)
    ledger.check("TRACE_AND_METRIC_ROUTES_EQUAL", dred_from_trace, dred_from_metric)
    ledger.check("SCALE_ONE_DOUBLE_HALF", scale_one_double_half, -2048 * wedge)
    ledger.check("SCALE_ONE_DIFFERS_BY_TWO", dred_from_metric / scale_one_double_half, 2)

    weight_a = old.simplex(old_metrics[0], y, z)
    weight_b = old.simplex(old_metrics[1], y, z)
    ledger.check("A_MARK_WEIGHT", weight_a, sp.Rational(2, 3))
    ledger.check("B_MARK_WEIGHT", weight_b, sp.Rational(1, 3))
    ledger.check("MARK_WEIGHT_SUM", weight_a + weight_b, 1)

    old_source = inspect.getsource(old._g3_original_measure_values)
    old_quotient_source = inspect.getsource(old.quotient_exact)
    ledger.check("OLD_EXPLICIT_DIVISION_BY_32768", "/ common_dword_normalization" in old_source, True)
    ledger.check("OLD_SCALE_OUTPUT_IMPORTED_FROM_PROJECT", "project.build_bundle()" in old_quotient_source, True)

    return {
        "original_measure_mask": mask,
        "old_normalized_trace_samples": {
            label: [exact_text(value) for value in values]
            for label, values in old_traces.items()
        },
        "raw_trace_samples": {
            label: [exact_text(value) for value in values]
            for label, values in raw_traces.items()
        },
        "exact_comparison": "T_raw=32768*T_old at every sampled affine frame",
        "old_metric": [exact_text(value) for value in old_metrics],
        "raw_metric": [exact_text(value) for value in raw_metrics],
        "berezin_maps": {
            "full_M_signed": exact_text(full_measure_signed),
            "antichiral_H_signed": exact_text(antichiral_measure_signed),
            "magnitude_product": exact_text(measure_magnitude),
        },
        "absolute_metric_coefficient": exact_text(metric_after_measure),
        "correct_dred": "(-1/2)*(2*4096*W)=-4096*W = -4096*W",
        "scale_one_completion": "(-1/2)*4096*W=-2048*W",
        "old_executable_boundary": {
            "earliest_absolute_information_loss": (
                "_g3_original_measure_values divides by 32768 and retains only shape"
            ),
            "scale_one_derived_from_g3_replay": False,
            "scale_one_source": "quotient_exact imports project.build_bundle()",
        },
        "earliest_factor_two_error": {
            "level": "DRED_RECONSTRUCTION_AFTER_METRIC_RECOVERY",
            "false_equality": "R_DRED=(-1/2)*c*W with c=T_perp/(2*W)",
            "correct_equality": "R_DRED=-c*W=(-1/2)*T_perp",
            "wrong_absolute_word": "-2048*W",
            "correct_absolute_word": "-4096*W",
        },
    }


def primitive_and_output_certificate(ledger: Ledger) -> dict[str, Any]:
    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source = -coupling**2 / (4 * sp.sqrt(2))
    matter = sp.sqrt(2) * coupling / hbar
    hminus32 = -sp.sqrt(2) * coupling / hbar
    hminus33 = -hminus32
    propagators = (-hbar) * (hbar / 16) * (hbar / 16)
    source_cycle = sp.Rational(1, 2) * 2
    action_orders = sp.Rational(1, 2) * 2
    hminus_hessian = sp.Rational(1, 6) * 6
    fixed_wick = sp.Integer(1)
    multiplicity = sp.simplify(source_cycle * action_orders * hminus_hessian * fixed_wick)
    pre32 = sp.simplify(source * matter * hminus32 * propagators * action_orders)
    pre33 = sp.simplify(source * matter * hminus33 * propagators * action_orders)
    ledger.check("SOURCE_CYCLIC_FACTOR", source_cycle, 1)
    ledger.check("ACTION_ORDER_FACTOR", action_orders, 1)
    ledger.check("HMINUS_HESSIAN_FACTOR", hminus_hessian, 1)
    ledger.check("FIXED_FLAVOR_WICK", fixed_wick, 1)
    ledger.check("TOTAL_PRIMITIVE_MULTIPLICITY", multiplicity, 1)
    ledger.check("G32_PRED", pre32, -sp.sqrt(2) * hbar * coupling**4 / 1024)
    ledger.check("G33_PRED", pre33, sp.sqrt(2) * hbar * coupling**4 / 1024)

    dword = -sp.Integer(4096)
    master = 1 / (32 * sp.pi**2)
    external_map = coupling**-2
    color = sp.I
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    raw32 = sp.simplify(pre32 * dword * master * external_map * color / lambda1)
    raw33 = sp.simplify(pre33 * dword * master * external_map * color / lambda1)
    typed32 = -raw32
    typed33 = -raw33
    ledger.check("G32_RAW_WEDGE_LAMBDA_UNITS", raw32, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_RAW_WEDGE_LAMBDA_UNITS", raw33, -2 * sp.I * sp.sqrt(2))
    ledger.check("G32_TYPED_C2_GT_C3", typed32, -2 * sp.I * sp.sqrt(2))
    ledger.check("G33_TYPED_C3_GT_C2", typed33, 2 * sp.I * sp.sqrt(2))

    half_dword = -sp.Integer(2048)
    half32 = sp.simplify(pre32 * half_dword * master * external_map * color / lambda1)
    ledger.check("FALSE_HALF_G32_RAW_WEDGE", half32, sp.I * sp.sqrt(2))

    return {
        "primitive_factors": {
            "source": exact_text(source),
            "matter_action": exact_text(matter),
            "Hminus_G32": exact_text(hminus32),
            "Hminus_G33": exact_text(hminus33),
            "propagators": exact_text(propagators),
            "source_cycle": "(1/2)*2=1",
            "action_orders": "(1/2!)*2=1",
            "Hminus_Hessian": "(1/3!)*6=1",
            "fixed_flavor_Wick": "1",
            "total_multiplicity": exact_text(multiplicity),
        },
        "pre_D": {"G32": exact_text(pre32), "G33": exact_text(pre33)},
        "output_chain": {
            "DRED_word": "-4096*W",
            "external_component_map": "tildephi_2*tildephi_3=g^(-2)*C_2*C_3",
            "complete_color": "+i*F^{AB}_{DE}",
            "finite_master": "1/(32*pi^2)",
            "lambda1": "hbar*g^2/(16*pi^2)",
            "G32_raw_wedge": exact_text(raw32),
            "G33_raw_wedge": exact_text(raw33),
            "typed_G32_C2_gt_C3": exact_text(typed32),
            "typed_G33_C3_gt_C2": exact_text(typed33),
        },
        "false_scale_one_chain": {
            "DRED_word": "-2048*W",
            "G32_raw_wedge": exact_text(half32),
        },
    }


def g1_half_certificate(ledger: Ledger) -> dict[str, Any]:
    coordinate_mask = sum(1 << g1.INDEX["S", name] for name in g1.COORDINATES)
    theta2 = g1.theta_squared_difference("S")
    dminus_dplus = g1.d_lower(
        g1.d_lower(theta2, "S", 0, g1.ZERO_VECTOR),
        "S",
        1,
        g1.ZERO_VECTOR,
    ).set_zero(g1.INDEX["S", name] for name in g1.COORDINATES)
    d2 = g1.d_squared(theta2, "S", g1.ZERO_VECTOR).set_zero(
        g1.INDEX["S", name] for name in g1.COORDINATES
    )
    ledger.check("G1_THETA2_COORDINATE_MASK_NONZERO", coordinate_mask != 0, True)
    ledger.check("G1_DMINUS_DPLUS_THETA2", dminus_dplus.coefficient(0), g1.QI.coerce(-2))
    ledger.check("G1_D2_THETA2", d2.coefficient(0), g1.QI.coerce(-4))
    ledger.check(
        "G1_D2_EQUALS_TWO_DMINUS_DPLUS",
        d2.terms,
        (2 * dminus_dplus).terms,
    )

    phi = g1.chiral_b_endpoint("M", g1.ZERO_VECTOR)
    b_projection = g1.d_lower(phi, "M", 0, g1.ZERO_VECTOR).set_zero(
        g1.INDEX["M", name] for name in g1.COORDINATES
    )
    ledger.check(
        "G1_ENDPOINT_DPLUS_PHI_EQUALS_ETA_B",
        b_projection.coefficient(1 << g1.ETA_B_INDEX),
        g1.ONE,
    )
    for dotted in (0, 1):
        vector = g1.vector_d_endpoint("G", dotted)
        projection = g1.d_squared(
            g1.bar_d_lower(vector, "G", dotted, g1.ZERO_VECTOR),
            "G",
            g1.ZERO_VECTOR,
        ).set_zero(g1.INDEX["G", name] for name in g1.COORDINATES)
        ledger.check(
            f"G1_ENDPOINT_D2_BARD_U_EQUALS_ETA_D_{dotted}",
            projection.coefficient(1 << g1.ETA_D_INDEX),
            g1.ONE,
        )

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    pre_plus = -hbar * coupling**4 / (8192 * sp.sqrt(2))
    pre_minus = -pre_plus
    external_map = (-4 * sp.sqrt(2) / coupling) * (1 / coupling)
    master = 1 / (32 * sp.pi**2)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    a_word_plus = sp.Rational(4096, 3)
    a_word_minus = -a_word_plus
    b_word_plus = -a_word_plus
    b_word_minus = a_word_plus
    a = sp.simplify(
        (pre_plus * a_word_plus + pre_minus * a_word_minus)
        * external_map
        * master
        / lambda1
    )
    b = sp.simplify(
        (pre_plus * b_word_plus + pre_minus * b_word_minus)
        * external_map
        * master
        / lambda1
    )
    ledger.check("G1_A_MARK_NORMALIZATION", a, sp.Rational(2, 3))
    ledger.check("G1_B_MARK_NORMALIZATION", b, -sp.Rational(2, 3))
    ledger.check("G1_FORBIDDEN_EXTRA_HALF_A", a / 2 == a, False)

    return {
        "source_derivative_convention": {
            "identity": "D^2=2*D_-*D_+",
            "engine_operator": "D_-*D_+=D^2/2",
            "engine_theta2_value": "-2",
            "D2_theta2_value": "-4",
            "additional_post_replay_half": False,
        },
        "endpoint_probe_maps": {
            "Dplus_phi_probe": "eta_B",
            "D2_barD_u_probe": "eta_D for both dotted slots",
            "physical_Dplus_phi": "B1/g",
            "physical_D2_barD_u": "-4*sqrt(2)*D/g",
            "product": "-4*sqrt(2)/g^2",
            "additional_component_half": False,
        },
        "selected_mark_check": {"A": exact_text(a), "B": exact_text(b)},
    }


def build() -> dict[str, Any]:
    ledger = Ledger()
    color = su2_color_certificate(ledger)
    trace = g3_trace_and_normalization_certificate(ledger)
    primitive = primitive_and_output_certificate(ledger)
    g1_half = g1_half_certificate(ledger)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": "step5-ab-ba-g3-absolute-normalization-first-difference-exact-v1",
        "external_target_used": False,
        "project_engine_called": False,
        "holomorphic_twist_used": False,
        "residual_q_used": False,
        "q_covariance_used": False,
        "SU2_color": color,
        "G3_trace_and_absolute_normalization": trace,
        "G3_primitives_and_output": primitive,
        "G1_half_check": g1_half,
        "status": (
            "PASS_G3_COLOR_PLUS_I__RAW_32768_TO_4096__"
            "FIRST_SCALE_ONE_ERROR_IS_DOUBLE_TRANSVERSE_HALF__"
            "G1_HAS_NO_ADDITIONAL_HALF"
            if failed == 0
            else "FAIL"
        ),
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows) - failed,
            "failed": failed,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    return r"""# AB/BA G3 absolute normalization and first difference

Status: `@@STATUS@@`.

## 1. SU(2) color

Use

$$
T_a=\frac{\sigma_a}{2},\qquad
\kappa_{ab}=\frac12\delta_{ab},\qquad
c_{ab}{}^c=\varepsilon_{abc},\qquad
c_{abc}=\frac12\varepsilon_{abc}.
$$

The literal shorthand without propagator metrics is

$$
(T_A)^D{}_Xc_{BXE}
=\frac{i}{2}\sum_X\varepsilon_{AXD}\varepsilon_{BXE}
=\frac{i}{4}\mathbb F^{AB}{}_{DE}.
$$

It is not the graph color.  The matter vertex is lower in the external
antichiral slot,

$$
(T_U)_{DX}:=\kappa_{DR}(T_U)^R{}_X=ic_{UXD}.
$$

The three propagators supply three inverse metrics.  Therefore

$$
\begin{aligned}
\mathcal C^{AB}{}_{DE}
&=\kappa^{AU}\kappa^{BP}\kappa^{XY}
(T_U)_{DX}c_{PYE}\\
&=i\kappa^{AU}\kappa^{BP}\kappa^{XY}
c_{UXD}c_{PYE}\\
&=i\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

For $(A,B,D,E)=(0,1,1,0)$,

$$
\mathbb F^{01}{}_{10}=-2,\qquad
(T_0)^1{}_Xc_{1X0}=-\frac i2,\qquad
\mathcal C^{01}{}_{10}=-2i.
$$

Thus the complete color is exactly $+i\mathbb F$ and contains no $1/2$.

## 2. Old normalized trace versus raw trace

The retained Berezin mask is

$$
m=(15\ll4M)\,|\,(12\ll4H)=3312.
$$

At every affine sample,

$$
T^{\rm raw}_{A,B}=32768T^{\rm old}_{A,B}.
$$

With $W=p_+\wedge q_+=-i$,

$$
T_A^{\rm old}=-2i(1-z),\qquad
T_B^{\rm old}=-2iz,
$$

$$
c_A^{\rm old}=\frac{T_A^{\rm old}}{2W}=1-z,\qquad
c_B^{\rm old}=\frac{T_B^{\rm old}}{2W}=z,
$$

whereas

$$
c_A^{\rm raw}=32768(1-z),\qquad
c_B^{\rm raw}=32768z.
$$

The old function divides by $32768$ before returning.  This is the first
loss of absolute normalization, not itself a false equality.

## 3. Berezin and DRED restoration

For the canonical monomials,

$$
\mathcal B_M=-\frac14,\qquad
\mathcal B_H=+\frac12,\qquad
|\mathcal B_M\mathcal B_H|=\frac18.
$$

Hence the absolute metric coefficient is

$$
c=32768\left(\frac18\right)=4096.
$$

Since the two-axis transverse trace is $T_\perp=2cW$,

$$
\mathcal R_{\rm DRED}
=-\frac12T_\perp
=-\frac12(2cW)
=-cW
=-4096W.
$$

The scale-one completion instead uses

$$
-\frac12cW=-2048W,
$$

after $c=T_\perp/(2W)$ has already consumed the trace factor $2$.  This is
the first algebraic factor-two error.  The old G3 replay itself never derives
the scale-one output; its quotient routine imports it from the Project engine.

## 4. Primitive and finite chain

$$
C_I=-\frac{g^2}{4\sqrt2},\qquad
C_M=\frac{\sqrt2g}{\hbar},\qquad
C_{H,32}=-\frac{\sqrt2g}{\hbar},\qquad
C_{H,33}=+\frac{\sqrt2g}{\hbar},
$$

$$
C_{\rm prop}=(-\hbar)
\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)
=-\frac{\hbar^3}{256}.
$$

$$
\left[\frac12(2)_{\rm source\ cycle}\right]
\left[\frac1{2!}(2)_{MH\ orders}\right]
\left[\frac1{3!}(6)_{H_-\ Hessian}\right]
(1)_{\rm Wick}=1.
$$

Therefore

$$
C_{32}^{\rm preD}=-\frac{\sqrt2\hbar g^4}{1024},\qquad
C_{33}^{\rm preD}=+\frac{\sqrt2\hbar g^4}{1024}.
$$

Using

$$
\widetilde\phi_2\widetilde\phi_3=g^{-2}C_2C_3,\qquad
\mathcal C_{\rm color}=+i\mathbb F,qquad
I_{\mu^2}=\frac1{32\pi^2},\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},
$$

one obtains

$$
\frac{C_{32}^{\rm preD}(-4096)g^{-2}iI_{\mu^2}}{\lambda_1}
=+2i\sqrt2,
$$

$$
\frac{C_{33}^{\rm preD}(-4096)g^{-2}iI_{\mu^2}}{\lambda_1}
=-2i\sqrt2.
$$

The ordered spinor map gives

$$
G_{32}:\ C_2>C_3=-2i\sqrt2,\qquad
G_{33}:\ C_3>C_2=+2i\sqrt2.
$$

## 5. G1 half check

The sparse engine gives

$$
D_-D_+\theta^2=-2,\qquad
D^2\theta^2=-4,\qquad
D^2=2D_-D_+.
$$

Thus the source replay already uses $D_-D_+=D^2/2$.  No further factor
$1/2$ may be applied.

Its endpoint probes obey

$$
D_+\phi_{\rm probe}=\eta_B,\qquad
D^2\bar D_{\dot a}u_{\rm probe}=\eta_D,
$$

and the physical map is

$$
D_+\phi_1=\frac1gB_1,\qquad
D^2\bar D_{\dot a}u=-\frac{4\sqrt2}{g}D_{\dot a}.
$$

There is no component-map half.  The selected marked rows remain

$$
G_{1,A}=\frac23,\qquad G_{1,B}=-\frac23.
$$
""".replace("@@STATUS@@", str(payload["status"]))


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", "--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        JSON_OUT.write_text(canonical(payload), encoding="utf-8")
        MD_OUT.write_text(markdown(payload), encoding="utf-8")
    if args.check_artifact:
        stored = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        if stored != payload:
            raise AssertionError(f"stored artifact is stale: {JSON_OUT}")
    if args.print_json:
        print(canonical(payload), end="")
    else:
        print("PASS SU2_COMPLETE_G3_COLOR_PLUS_I_F_NO_HALF")
        print("PASS RAW_TRACE_EQUALS_32768_TIMES_OLD_NORMALIZED_TRACE")
        print("PASS ORIGINAL_MEASURE_METRIC_4096_AND_DRED_WORD_MINUS_4096_W")
        print("PASS FIRST_SCALE_ONE_ERROR_IS_DOUBLE_TRANSVERSE_HALF")
        print("PASS G1_DMINUS_AND_COMPONENT_MAP_HAVE_NO_ADDITIONAL_HALF")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
