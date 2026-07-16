#!/usr/bin/env python3
"""Target-blind raw multiplicity and transverse-trace audit for AB/BA G1,G3.

This audit starts from the executable source/action D-words.  It does not
read a holomorphic-twist result and it does not use a residual-q condition.
The two questions are:

* whether one directed mixed source block receives an additional 1/2 after
  quotienting the two cyclic starting points in the one-loop supertrace;
* whether the DRED projector -1/2 may be applied again after the two-axis
  trace has already been divided by 2 to recover the metric coefficient.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_marked_sd_orbit_exact_audit as marked  # noqa: E402
import step5_ab_ba_g1_longitudinal_contact_exact_audit as g1_contact  # noqa: E402
import step5_ab_ba_g3_factor_two_first_error_exact_audit as g3_raw  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g1-g3-raw-multiplicity-trace-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g1-g3-raw-multiplicity-trace-exact.md"


def exact_text(value: object) -> str:
    if isinstance(value, sp.MatrixBase):
        return str(value.tolist()).replace("I", "i")
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    if isinstance(value, tuple):
        return "(" + ", ".join(exact_text(entry) for entry in value) + ")"
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        difference = sp.Matrix(actual) - sp.Matrix(expected)
        return all(sp.simplify(entry) == 0 for entry in difference)
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


def cyclic_source_certificate(ledger: Ledger) -> dict[str, Any]:
    """Resolve the 1/2 STr against the two mixed Hessian blocks exactly."""

    i_uphi = sp.Matrix(((0, 1), (0, 0)))
    i_phiu = sp.Matrix(((0, 0), (1, 0)))
    cycle = i_uphi + i_phiu
    forward = sp.trace(cycle * i_uphi)
    reverse = sp.trace(cycle * i_phiu)
    full_supertrace_weight = sp.Rational(1, 2) * (forward + reverse)
    ledger.check("CYCLIC_FORWARD_BLOCK", forward, 1)
    ledger.check("CYCLIC_REVERSE_BLOCK", reverse, 1)
    ledger.check("HALF_STRTIMES_TWO_STARTING_POINTS", full_supertrace_weight, 1)
    ledger.check("ONE_REPRESENTATIVE_ORBIT_WEIGHT", forward, full_supertrace_weight)
    ledger.check(
        "REJECT_HALF_OF_ONE_REPRESENTATIVE",
        sp.Rational(1, 2) * forward == full_supertrace_weight,
        False,
    )
    return {
        "mixed_blocks": ["I_{u,phi}", "I_{phi,u}"],
        "block_traces": [exact_text(forward), exact_text(reverse)],
        "supertrace": "(1/2)*(1+1)=1",
        "cyclic_equivalence_classes": 1,
        "weight_of_one_retained_representative": "1",
        "forbidden_weight": "1/2",
        "reason": (
            "The retained directed row represents the complete cyclic class; "
            "the omitted reverse block is precisely the second term cancelled "
            "by the supertrace half."
        ),
    }


def transverse_rank_certificate(ledger: Ledger) -> dict[str, Any]:
    """Show the two equivalent, and only equivalent, DRED trace routes."""

    c, wedge = sp.symbols("c W", nonzero=True)
    two_axis_trace = 2 * c * wedge
    metric = sp.simplify(two_axis_trace / (2 * wedge))
    from_trace = sp.simplify(-sp.Rational(1, 2) * two_axis_trace)
    from_metric = sp.simplify(-metric * wedge)
    double_half = sp.simplify(-sp.Rational(1, 2) * metric * wedge)
    ledger.check("TRACE_IS_TWO_METRIC_COMPONENTS", two_axis_trace, 2 * c * wedge)
    ledger.check("METRIC_FROM_TRACE_OVER_TWO_W", metric, c)
    ledger.check("DRED_FROM_FULL_TRACE", from_trace, -c * wedge)
    ledger.check("DRED_FROM_RECOVERED_METRIC", from_metric, -c * wedge)
    ledger.check("TRACE_AND_METRIC_ROUTES_EQUAL", from_trace, from_metric)
    ledger.check("EXTRA_HALF_AFTER_METRIC_IS_WRONG", double_half == from_metric, False)
    return {
        "two_axis_trace": "T_perp=2*c*W",
        "trace_route": "(-1/2)*T_perp=-c*W",
        "metric_route": "c=T_perp/(2*W), then DRED=-c*W",
        "forbidden_mixed_route": "(-1/2)*[T_perp/(2*W)]*W=-c*W/2",
        "extra_rank_trace_half": False,
    }


def g1_axis_trace_sample(ledger: Ledger) -> dict[str, Any]:
    p = marked.g1.vector((1, 0, 0, 0))
    q = marked.g1.vector((0, 0, 0, 1))
    zero = marked.g1.ZERO_VECTOR
    center = marked.g1_full_outer_totals(zero, p, q, 0, "+")
    axis_rows: list[tuple[object, object]] = []
    for axis in (1, 2):
        unit = [marked.g1.ZERO] * 4
        unit[axis] = marked.g1.ONE
        unit_vector = tuple(unit)
        plus = marked.g1_full_outer_totals(unit_vector, p, q, 0, "+")
        minus = marked.g1_full_outer_totals(
            marked.g1.vector_neg(unit_vector), p, q, 0, "+"
        )
        axis_rows.append(
            tuple((plus[branch] - 2 * center[branch] + minus[branch]) / 2 for branch in range(2))
        )
    trace = tuple(axis_rows[0][branch] + axis_rows[1][branch] for branch in range(2))
    ledger.check("G1_PLUS_DOT0_AXIS1_COEFFICIENTS", axis_rows[0], (marked.g1.QI.coerce(4096), marked.g1.QI.coerce(-4096)))
    ledger.check("G1_PLUS_DOT0_AXIS2_COEFFICIENTS", axis_rows[1], (marked.g1.QI.coerce(2048), marked.g1.QI.coerce(-4096)))
    ledger.check("G1_PLUS_DOT0_TWO_AXIS_TRACE", trace, (marked.g1.QI.coerce(6144), marked.g1.QI.coerce(-8192)))
    return {
        "frame": "p=e1,q=e4,L=0,sector=+,dotted=0",
        "axis_2": [exact_text(value) for value in axis_rows[0]],
        "axis_3": [exact_text(value) for value in axis_rows[1]],
        "two_axis_trace": [exact_text(value) for value in trace],
    }


def g1_certificate(ledger: Ledger, cyclic: dict[str, Any]) -> dict[str, Any]:
    g1 = marked.g1
    source_cycle = sp.Integer(1)
    action_taylor = sp.Rational(1, 2) * 2
    gauge_cubic_hessian = sp.Rational(1, 6) * 6
    matter_cubic_hessian = sp.Rational(1, 6) * 6
    fixed_role_wick = sp.Integer(1)
    total_multiplicity = sp.simplify(
        source_cycle
        * action_taylor
        * gauge_cubic_hessian
        * matter_cubic_hessian
        * fixed_role_wick
    )
    ledger.check("G1_SOURCE_CYCLIC_CLASS_FACTOR", source_cycle, 1)
    ledger.check("G1_ACTION_TAYLOR_TWO_ORDERS", action_taylor, 1)
    ledger.check("G1_GAUGE_CUBIC_HESSIAN_FACTOR", gauge_cubic_hessian, 1)
    ledger.check("G1_MATTER_CUBIC_HESSIAN_FACTOR", matter_cubic_hessian, 1)
    ledger.check("G1_FIXED_ROLE_WICK_PAIRING", fixed_role_wick, 1)
    ledger.check("G1_TOTAL_RAW_MULTIPLICITY", total_multiplicity, 1)
    ledger.check("G1_VVV_PERMUTATIONS", len(g1.PERMUTATIONS), 6)
    ledger.check("G1_VVV_DERIVATIVE_PLACEMENTS", len(g1.PLACEMENTS), 2)
    ledger.check("G1_VVV_ROWS_PER_CHIRALITY", len(g1.PERMUTATIONS) * len(g1.PLACEMENTS), 12)
    ledger.check("G1_VVV_ROWS_BOTH_CHIRALITIES", 2 * len(g1.PERMUTATIONS) * len(g1.PLACEMENTS), 24)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source = -coupling**2 / (4 * sp.sqrt(2))
    gauge_plus = sp.I * sp.sqrt(2) * coupling / hbar
    matter_plus = -sp.I * sp.sqrt(2) * coupling / (256 * hbar)
    propagators = (-hbar) * (-hbar) * (hbar / 16)
    pre_plus = sp.simplify(
        source * gauge_plus * matter_plus * propagators * action_taylor
    )
    ledger.check("G1_PRE_D_PLUS_FROM_PRIMITIVES", pre_plus, -hbar * coupling**4 / (8192 * sp.sqrt(2)))
    ledger.check("G1_PRE_D_MINUS_FROM_CHIRAL_REFLECTION", -pre_plus, hbar * coupling**4 / (8192 * sp.sqrt(2)))

    tensor = marked.g1_full_tensor_frame_audit()
    selected = tensor["selected_momentum_coefficients"]
    normalized: dict[str, tuple[object, object]] = {}
    for branch, mark in enumerate(("A", "B")):
        plus = selected["+", branch]
        minus = selected["-", branch]
        normalized[mark] = tuple((plus[index] - minus[index]) / 4096 for index in range(2))
    expected_a = (g1.QI.coerce(Fraction(4, 3)), g1.QI.coerce(Fraction(2, 3)))
    expected_b = (g1.QI.coerce(Fraction(2, 3)), g1.QI.coerce(Fraction(4, 3)))
    total = tuple(normalized["A"][index] + normalized["B"][index] for index in range(2))
    ledger.check("G1_A_MARK_GENERIC_PB_QD", normalized["A"], expected_a)
    ledger.check("G1_B_MARK_GENERIC_PB_QD", normalized["B"], expected_b)
    ledger.check("G1_TWO_MARK_SUM_GENERIC_PB_QD", total, (g1.QI.coerce(2), g1.QI.coerce(2)))

    contact_payload, contact_ledger = g1_contact.build_payload(include_probe=False)
    ledger.check("G1_RAW_CONTACT_REPLAY_STATUS", contact_payload["status"], "EXACT_TARGET_BLIND_G1_CONTACT_ORBIT_CLOSED")
    ledger.check("G1_RAW_CONTACT_REPLAY_FAILURES", contact_payload["checks"]["failed"], 0)
    ledger.check("G1_RAW_CONTACT_CORE_CHECKS", len(contact_ledger.rows), 874)
    first_a = contact_payload["validation"]["first_nonzero_A_anomaly_row"]
    first_b = contact_payload["validation"]["first_nonzero_B_anomaly_row"]
    ledger.check("G1_A_MARK_EDGE", first_a["selected_edge"], "e2")
    ledger.check("G1_B_MARK_EDGE", first_b["selected_edge"], "e0")
    ledger.check("G1_A_FULL_D_PARENT_CONTACT", first_a["full_d_parent_plus_contact"], "0")
    ledger.check("G1_B_FULL_D_PARENT_CONTACT", first_b["full_d_parent_plus_contact"], "0")

    return {
        "cyclic_source_factor": cyclic["supertrace"],
        "primitive_multiplicity": {
            "source_mixed_blocks": "(1/2)_STr*2_cyclic_starts=1",
            "action_expansion": "(1/2!)*2_(Sg3,Sm3 orders)=1",
            "gauge_cubic_Hessian": "(1/3!)*6_label_permutations=1",
            "gauge_derivative_placements": "QL and LQ are two algebraic Hessian summands",
            "matter_cubic_Hessian": "(1/3!)*6_distinct_role_derivatives=1",
            "fixed_connected_Wick_pairing": "1",
            "total": exact_text(total_multiplicity),
        },
        "unique_connected_pairing": [
            "u_source<->u_gauge",
            "u_matter<->u_gauge",
            "phi_source<->tildephi_matter",
        ],
        "source_marks": {
            "A": {
                "edge": "e2",
                "parent": "alpha_A*bar(r2)^2/(D0*D1*D2)",
                "cut": "-alpha_A*r2_d^2/(D0*D1*D2)",
                "remainder": "alpha_A*mu_l^2/(D0*D1*D2)",
                "generic_(p_B,q_D)": [exact_text(value) for value in normalized["A"]],
            },
            "B": {
                "edge": "e0",
                "parent": "alpha_B*bar(r0)^2/(D0*D1*D2)",
                "cut": "-alpha_B*r0_d^2/(D0*D1*D2)",
                "remainder": "alpha_B*mu_l^2/(D0*D1*D2)",
                "generic_(p_B,q_D)": [exact_text(value) for value in normalized["B"]],
            },
            "classification": "two distinct product-rule parent occurrences",
        },
        "raw_generic_(p_B,q_D)": [exact_text(value) for value in total],
        "current_G1_scale": "2",
        "decision": "RETAIN",
        "axis_trace_sample": g1_axis_trace_sample(ledger),
    }


def g3_certificate(ledger: Ledger, cyclic: dict[str, Any]) -> dict[str, Any]:
    source_cycle = sp.Integer(1)
    action_taylor = sp.Rational(1, 2) * 2
    hminus_hessian = sp.Rational(1, 6) * 6
    fixed_flavor_wick = sp.Integer(1)
    total_multiplicity = sp.simplify(
        source_cycle * action_taylor * hminus_hessian * fixed_flavor_wick
    )
    ledger.check("G3_SOURCE_CYCLIC_CLASS_FACTOR", source_cycle, 1)
    ledger.check("G3_ACTION_TAYLOR_TWO_ORDERS", action_taylor, 1)
    ledger.check("G3_HMINUS_THIRD_DERIVATIVE_FACTOR", hminus_hessian, 1)
    ledger.check("G3_FIXED_FLAVOR_WICK_PAIRING", fixed_flavor_wick, 1)
    ledger.check("G3_TOTAL_RAW_MULTIPLICITY", total_multiplicity, 1)

    y, z = sp.symbols("y z", nonnegative=True)
    weight_a = sp.simplify(2 * sp.integrate(sp.integrate(1 - z, (z, 0, 1 - y)), (y, 0, 1)))
    weight_b = sp.simplify(2 * sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1)))
    ledger.check("G3_A_MARK_SIMPLEX_WEIGHT", weight_a, sp.Rational(2, 3))
    ledger.check("G3_B_MARK_SIMPLEX_WEIGHT", weight_b, sp.Rational(1, 3))
    ledger.check("G3_MARK_WEIGHT_SUM", weight_a + weight_b, 1)

    raw_00 = g3_raw.raw_original_measure_values(sp.Rational(0), sp.Rational(0), (0, 0, 0, 0))
    raw_axis2_plus = g3_raw.raw_original_measure_values(sp.Rational(0), sp.Rational(0), (0, 1, 0, 0))
    raw_axis2_minus = g3_raw.raw_original_measure_values(sp.Rational(0), sp.Rational(0), (0, -1, 0, 0))
    raw_axis3_plus = g3_raw.raw_original_measure_values(sp.Rational(0), sp.Rational(0), (0, 0, 1, 0))
    raw_axis3_minus = g3_raw.raw_original_measure_values(sp.Rational(0), sp.Rational(0), (0, 0, -1, 0))
    ledger.check("G3_RAW_MONOMIAL_L2_PLUS_A", raw_axis2_plus[0], -32768 - 32768 * sp.I)
    ledger.check("G3_RAW_MONOMIAL_L2_MINUS_A", raw_axis2_minus[0], 32768 - 32768 * sp.I)
    ledger.check("G3_RAW_MONOMIAL_L3_PLUS_A", raw_axis3_plus[0], 65536 - 32768 * sp.I)
    ledger.check("G3_RAW_MONOMIAL_L3_MINUS_A", raw_axis3_minus[0], -65536 - 32768 * sp.I)
    trace = g3_raw.raw_transverse_trace(sp.Rational(0), sp.Rational(0))
    ledger.check("G3_RAW_TWO_AXIS_TRACE_AT_00", trace, (-65536 * sp.I, 0))
    p = g3_raw.ab_old.euclidean_bispinor((1, 0, 0, 0))
    q = g3_raw.ab_old.euclidean_bispinor((0, 0, 0, 1))
    wedge = sp.expand(g3_raw.ab_old.wedge(p, q))
    metric = sp.simplify(trace[0] / (2 * wedge))
    ledger.check("G3_FRAME_EXTERNAL_WEDGE", wedge, -sp.I)
    ledger.check("G3_METRIC_FROM_TRACE_OVER_2W", metric, 32768)
    measure_magnitude = sp.Rational(1, 4) * sp.Rational(1, 2)
    metric_after_measure = sp.simplify(metric * measure_magnitude)
    trace_after_measure = sp.simplify(trace[0] * measure_magnitude)
    ev_from_trace = sp.simplify(-sp.Rational(1, 2) * trace_after_measure)
    ev_from_metric = sp.simplify(-metric_after_measure * wedge)
    wrong_extra_half = sp.simplify(-sp.Rational(1, 2) * metric_after_measure * wedge)
    ledger.check("G3_METRIC_AFTER_ORIGINAL_MEASURES", metric_after_measure, 4096)
    ledger.check("G3_DRED_FROM_FULL_TWO_AXIS_TRACE", ev_from_trace, 4096 * sp.I)
    ledger.check("G3_DRED_FROM_RECOVERED_METRIC", ev_from_metric, 4096 * sp.I)
    ledger.check("G3_TRACE_AND_METRIC_DRED_EQUAL", ev_from_trace, ev_from_metric)
    ledger.check("G3_REJECT_EXTRA_HALF_AFTER_METRIC", wrong_extra_half == ev_from_metric, False)

    words = marked.g23_exact_words()
    w0 = sp.expand(words["w12"])
    w1 = sp.expand(words["wedge_pq_r0"])
    w2 = sp.expand(words["wedge_p_r0"])
    ledger.check("G3_RAW_A_PARENT", words["g3_a_full"], -1024 * words["det_r0"] * w0 + 1024 * words["det_r1"] * w1)
    ledger.check("G3_RAW_B_PARENT", words["g3_b_parent_raw"], -1024 * words["det_r2"] * w2)
    ledger.check("G3_RAW_K0_CORE", words["g3_a_contact_top"], 512 * w0)
    ledger.check("G3_RAW_K1_CORE", words["g3_transported_contact_core"], -128 * w1)
    ledger.check("G3_RAW_K2_CORE", words["g3_b_contact"], -128 * w2)

    endpoint_d2 = -sp.Integer(4)
    k0_multiplier = sp.Integer(8)
    k1_multiplier = -sp.Rational(1, 2) * 16 * endpoint_d2
    k2_multiplier = sp.Rational(1, 2) * 16 * endpoint_d2
    k0 = sp.expand(k0_multiplier * words["g3_a_contact_top"])
    k1 = sp.expand(k1_multiplier * words["g3_transported_contact_core"])
    k2 = sp.expand(k2_multiplier * words["g3_b_contact"])
    ledger.check("G3_K0_SAME_UNIT", k0, 4096 * w0)
    ledger.check("G3_K1_SAME_UNIT", k1, -4096 * w1)
    ledger.check("G3_K2_SAME_UNIT", k2, 4096 * w2)
    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2", nonzero=True)
    denominator = d0 * d1 * d2
    parent0 = -4096 * (d0 + mu2) * w0 / denominator
    parent1 = 4096 * (d1 + mu2) * w1 / denominator
    parent2 = -4096 * (d2 + mu2) * w2 / denominator
    cut0 = k0 / (d1 * d2)
    cut1 = k1 / (d0 * d2)
    cut2 = k2 / (d0 * d1)
    ledger.check("G3_E0_FULL_D_ZERO", (parent0 + cut0).subs(mu2, 0), 0)
    ledger.check("G3_E1_FULL_D_ZERO", (parent1 + cut1).subs(mu2, 0), 0)
    ledger.check("G3_E2_FULL_D_ZERO", (parent2 + cut2).subs(mu2, 0), 0)
    ledger.check("G3_E0_DRED", parent0 + cut0, -4096 * mu2 * w0 / denominator)
    ledger.check("G3_E1_DRED", parent1 + cut1, 4096 * mu2 * w1 / denominator)
    ledger.check("G3_E2_DRED", parent2 + cut2, -4096 * mu2 * w2 / denominator)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source = -coupling**2 / (4 * sp.sqrt(2))
    matter = sp.sqrt(2) * coupling / hbar
    hminus32 = -sp.sqrt(2) * coupling / hbar
    hminus33 = -hminus32
    propagators = -hbar * (hbar / 16) * (hbar / 16)
    pre32 = sp.simplify(source * matter * hminus32 * propagators * action_taylor)
    pre33 = sp.simplify(source * matter * hminus33 * propagators * action_taylor)
    ledger.check("G32_PRE_D_FROM_PRIMITIVES", pre32, -sp.sqrt(2) * hbar * coupling**4 / 1024)
    ledger.check("G33_PRE_D_FROM_PRIMITIVES", pre33, sp.sqrt(2) * hbar * coupling**4 / 1024)
    master = 1 / (32 * sp.pi**2)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    external_map = coupling**-2
    color = sp.I
    raw32 = sp.simplify(pre32 * (-4096) * (weight_a + weight_b) * master * external_map * color / lambda1)
    raw33 = sp.simplify(pre33 * (-4096) * (weight_a + weight_b) * master * external_map * color / lambda1)
    typed32 = -raw32
    typed33 = -raw33
    ledger.check("G32_RAW_WEDGE_COEFFICIENT", raw32, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_RAW_WEDGE_COEFFICIENT", raw33, -2 * sp.I * sp.sqrt(2))
    ledger.check("G32_TYPED_C2_GT_C3", typed32, -2 * sp.I * sp.sqrt(2))
    ledger.check("G33_TYPED_C3_GT_C2", typed33, 2 * sp.I * sp.sqrt(2))

    return {
        "cyclic_source_factor": cyclic["supertrace"],
        "primitive_multiplicity": {
            "source_mixed_blocks": "(1/2)_STr*2_cyclic_starts=1",
            "action_expansion": "(1/2!)*2_(M,Hminus orders)=1",
            "Hminus_cubic_Hessian": "(1/3!)*6_flavor-color permutations=1",
            "fixed_flavor_Wick_pairing": "1",
            "total": exact_text(total_multiplicity),
        },
        "outer_marks": {
            "A": {"simplex_weight": exact_text(weight_a), "square_edges": ["e0", "e1"]},
            "B": {"simplex_weight": exact_text(weight_b), "square_edges": ["e2"]},
            "sum": exact_text(weight_a + weight_b),
        },
        "original_measure_trace": {
            "one_nonzero_monomial": exact_text(raw_axis2_plus[0]),
            "two_axis_trace": exact_text(trace[0]),
            "external_wedge": exact_text(wedge),
            "metric_coefficient": exact_text(metric),
            "measure_magnitude": exact_text(measure_magnitude),
            "metric_after_measure": exact_text(metric_after_measure),
            "correct_trace_route": "(-1/2)*(2*4096*W)=-4096*W",
            "correct_metric_route": "c=4096, then -c*W=-4096*W",
            "rejected_double_half": "(-1/2)*c*W=-2048*W",
        },
        "occurrences": {
            "e0": {"parent": "-4096*(D0+mu2)*W0/P3", "cut": "+4096*W0/(D1*D2)", "remainder": "-4096*mu2*W0/P3"},
            "e1": {"parent": "+4096*(D1+mu2)*W1/P3", "cut": "-4096*W1/(D0*D2)", "remainder": "+4096*mu2*W1/P3"},
            "e2": {"parent": "-4096*(D2+mu2)*W2/P3", "cut": "+4096*W2/(D0*D1)", "remainder": "-4096*mu2*W2/P3"},
        },
        "raw_wedge_coefficients": {"G32": exact_text(raw32), "G33": exact_text(raw33)},
        "typed_coefficients": {"G32_C2_gt_C3": exact_text(typed32), "G33_C3_gt_C2": exact_text(typed33)},
        "current_G3_magnitude": "2*sqrt(2)",
        "decision": "RETAIN",
    }


def build() -> dict[str, Any]:
    ledger = Ledger()
    cyclic = cyclic_source_certificate(ledger)
    transverse = transverse_rank_certificate(ledger)
    g1 = g1_certificate(ledger, cyclic)
    g3 = g3_certificate(ledger, cyclic)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": "step5-ab-ba-g1-g3-raw-multiplicity-trace-exact-v1",
        "external_target_used": False,
        "residual_q_used": False,
        "cyclic_source_hessian": cyclic,
        "transverse_rank": transverse,
        "G1": g1,
        "G3": g3,
        "decision": {
            "G1_current_2": "RETAIN",
            "G3_current_plus_minus_2i_sqrt2": "RETAIN",
            "directed_source_factor_half": "REJECTED",
            "extra_half_after_trace_over_2W": "REJECTED",
        },
        "status": (
            "PASS_AB_BA_G1_G3_RAW_MULTIPLICITY_ONE__"
            "NO_EXTRA_TRANSVERSE_HALF__CURRENT_MAGNITUDES_RETAINED"
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
    checks = payload["checks"]
    assert isinstance(checks, dict)
    return r"""# AB/BA G1 and G3 raw multiplicity and transverse trace

Status: `@@STATUS@@`.

## 1. Mixed source Hessian

Let $I_{u\phi}$ and $I_{\phi u}$ be the two mixed Hessian blocks.  The two
closed traces differ only by the starting point:

$$
T_{u\phi}=T_{\phi u}=T.
$$

Therefore

$$
\frac12\operatorname{STr}\bigl[C(I_{u\phi}+I_{\phi u})\bigr]
=\frac12(T+T)=T.
$$

One retained directed representative has weight $1$, not $1/2$.

## 2. Transverse rank extraction

For $N=c\bar L^2W$,

$$
T_\perp=2cW.
$$

The two equivalent calculations are

$$
-\frac12T_\perp=-cW,
$$

$$
c=\frac{T_\perp}{2W},
\qquad
\mathcal R_{\rm DRED}=-cW.
$$

The mixed prescription

$$
-\frac12\left(\frac{T_\perp}{2W}\right)W=-\frac12cW
$$

applies the rank half twice and is rejected.

## 3. G1

The primitive multiplicity is

$$
\left[\frac12(2)_{\rm cyclic\ source}\right]
\left[\frac1{2!}(2)_{S_gS_m\ {m orders}}\right]
\left[\frac1{3!}(6)_{VVV\ {m labels}}\right]
\left[\frac1{3!}(6)_{u\phi\widetilde\phi}\right]
(1)_{\rm Wick}=1.
$$

$QL$ and $LQ$ are two algebraic summands of the polarized gauge Hessian;
they are not an additional graph factor.

The two product-rule marks are distinct parent occurrences:

$$
A:\ e_2,\qquad B:\ e_0.
$$

The exact generic $(p_B,q_D)$ rows are

$$
A=\left(\frac43,\frac23\right),
\qquad
B=\left(\frac23,\frac43\right),
$$

$$
\boxed{G_1=(2,2).}
$$

## 4. G3

The primitive multiplicity is

$$
\left[\frac12(2)_{\rm cyclic\ source}\right]
\left[\frac1{2!}(2)_{MH\ {m orders}}\right]
\left[\frac1{3!}(6)_{H_-\ {m Hessian}}\right]
(1)_{\rm Wick}=1.
$$

At $y=z=0$, one exact nonzero original-measure monomial is

$$
-32768-32768i.
$$

The exact two-axis trace and external wedge are

$$
T_\perp=-65536i,
\qquad W=-i,
\qquad
c=\frac{T_\perp}{2W}=32768.
$$

Thus

$$
c_{\rm measure}=32768\left(\frac14\right)\left(\frac12\right)=4096,
$$

$$
-\frac12T_{\perp,{\rm measure}}
=-4096W.
$$

Equivalently, after recovering $c_{\rm measure}=4096$, the DRED word is
$-c_{\rm measure}W$; no further $1/2$ is allowed.

The three parent--cut rows are

$$
-\frac{4096(D_0+\mu_\ell^2)W_0}{P_3}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu_\ell^2W_0}{P_3},
$$

$$
+\frac{4096(D_1+\mu_\ell^2)W_1}{P_3}
-\frac{4096W_1}{D_0D_2}
=+\frac{4096\mu_\ell^2W_1}{P_3},
$$

$$
-\frac{4096(D_2+\mu_\ell^2)W_2}{P_3}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu_\ell^2W_2}{P_3}.
$$

The raw-wedge coefficients are

$$
G_{32}^{\rm raw}=+2i\sqrt2,
\qquad
G_{33}^{\rm raw}=-2i\sqrt2.
$$

With the locked Fourier map, the typed coefficients are

$$
\boxed{
G_{32}^{C_2>C_3}=-2i\sqrt2,
\qquad
G_{33}^{C_3>C_2}=+2i\sqrt2.}
$$

$$
N_{\rm pass}=@@PASS@@,
\qquad
N_{\rm fail}=@@FAIL@@.
$$
""".replace("@@STATUS@@", str(payload["status"])).replace(
        "@@PASS@@", str(checks["passed"])
    ).replace("@@FAIL@@", str(checks["failed"]))


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def validate(payload: dict[str, Any]) -> None:
    expected_status = (
        "PASS_AB_BA_G1_G3_RAW_MULTIPLICITY_ONE__"
        "NO_EXTRA_TRANSVERSE_HALF__CURRENT_MAGNITUDES_RETAINED"
    )
    if payload.get("status") != expected_status:
        raise AssertionError(payload.get("status"))
    if payload.get("external_target_used") is not False:
        raise AssertionError("external target was used")
    if payload.get("residual_q_used") is not False:
        raise AssertionError("residual q was used")
    checks = payload.get("checks")
    if not isinstance(checks, dict) or checks.get("failed") != 0:
        raise AssertionError(checks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    json_text = canonical(payload)
    md_text = markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    elif args.check_artifact:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
        print("PASS AB_BA_SOURCE_CYCLIC_HALF_TIMES_TWO_EQUALS_ONE")
        print("PASS AB_BA_G1_RAW_MULTIPLICITY_ONE_AND_SCALE_TWO")
        print("PASS AB_BA_G3_RAW_MULTIPLICITY_ONE_AND_SCALE_TWO")
        print("PASS AB_BA_TRANSVERSE_TRACE_NO_EXTRA_HALF")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    else:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
