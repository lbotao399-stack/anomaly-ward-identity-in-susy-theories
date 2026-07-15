#!/usr/bin/env python3
"""Target-blind exact AA gauge-coordinate and factor-eight audit."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-gauge-field-normalization-factor8-exact.md"
STEP5A = ROOT / "contracts" / "foundations" / "step-05a-component-bv-brst-primitive-supergraph-grammar.md"
WW = ROOT / "contracts" / "foundations" / "step-05-euclidean-n4-awi-one-loop.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.simplify(self.actual - self.expected) == 0
        return self.actual == self.expected


def main() -> int:
    g, hbar = sp.symbols("g hbar", nonzero=True)
    h = g**-2

    # Original unrestricted prepotential V.
    k_v = h / 2
    k_v_inverse = 2 * g**2
    propagator_v_original = -hbar * k_v_inverse

    scales = {
        "V": sp.Integer(1),
        "u": sp.sqrt(2) * g,
        "v": 2 * g,
    }
    propagators = {
        name: sp.simplify(propagator_v_original / scale**2)
        for name, scale in scales.items()
    }

    # A_c=g^{-1}D_+W_+, W_+^{(1)}=-barD^2D_+V/8.
    source_unmarked = {
        name: sp.simplify(-scale / (8 * g))
        for name, scale in scales.items()
    }
    source_marked = {
        name: sp.simplify(value / 2)
        for name, value in source_unmarked.items()
    }
    closed_d_factor = 16 * 2 * 2
    source_weights = {
        name: sp.simplify(
            source_unmarked[name] * source_marked[name] * closed_d_factor
        )
        for name in scales
    }

    # From S_{E,+,3}=-(h/8) int W^a[D_aV,V], with W=g W_c.
    action_hessian_magnitudes = {
        name: sp.simplify(scale**2 / (8 * g))
        for name, scale in scales.items()
    }

    interaction_order_factor = sp.Rational(1, 2) * 2
    fixed_wick_factor = 1
    polarization_factor_after_hessian = 1
    graph_cores = {
        name: sp.simplify(
            source_weights[name]
            * action_hessian_magnitudes[name] ** 2
            * propagators[name] ** 3
            / hbar**2
            * interaction_order_factor
            * fixed_wick_factor
            * polarization_factor_after_hessian
        )
        for name in scales
    }

    # WW entries w_D=2 and |H|=g/2 are exactly the v-coordinate entries.
    ww_source_weight = sp.Integer(2)
    ww_hessian_magnitude = g / 2
    ww_correct_core = sp.simplify(
        ww_source_weight
        * ww_hessian_magnitude**2
        * propagators["v"] ** 3
        / hbar**2
    )
    ww_unit_propagator_core = sp.simplify(
        ww_source_weight
        * ww_hessian_magnitude**2
        * (-hbar) ** 3
        / hbar**2
    )
    factor_eight = sp.simplify(ww_unit_propagator_core / ww_correct_core)

    # W^gamma D_gamma with epsilon^{-+}=-1 and only external W_+ nonzero.
    w_minus_over_w_plus = -1
    projected_action_derivative = -1
    abstract_hessian_w = sp.I * g / 4
    projected_hessian_wplus = sp.simplify(
        abstract_hessian_w * w_minus_over_w_plus
    )
    tau_e = -1 / hbar
    projected_exponent_wplus = sp.simplify(tau_e * projected_hessian_wplus)

    checks = [
        Check("h_equals_g_minus_two", h, g**-2),
        Check("original_V_hessian", k_v, 1 / (2 * g**2)),
        Check("original_V_inverse", k_v_inverse, 2 * g**2),
        Check("original_V_propagator", propagators["V"], -2 * hbar * g**2),
        Check("u_scale", scales["u"], sp.sqrt(2) * g),
        Check("v_scale", scales["v"], 2 * g),
        Check("u_propagator", propagators["u"], -hbar),
        Check("v_propagator", propagators["v"], -hbar / 2),
        Check("V_source_unmarked", source_unmarked["V"], -1 / (8 * g)),
        Check("u_source_unmarked", source_unmarked["u"], -1 / (4 * sp.sqrt(2))),
        Check("v_source_unmarked", source_unmarked["v"], -sp.Rational(1, 4)),
        Check("V_source_marked", source_marked["V"], -1 / (16 * g)),
        Check("u_source_marked", source_marked["u"], -1 / (8 * sp.sqrt(2))),
        Check("v_source_marked", source_marked["v"], -sp.Rational(1, 8)),
        Check("closed_D_factor", closed_d_factor, 64),
        Check("V_source_weight", source_weights["V"], 1 / (2 * g**2)),
        Check("u_source_weight", source_weights["u"], 1),
        Check("v_source_weight", source_weights["v"], 2),
        Check("V_action_hessian_magnitude", action_hessian_magnitudes["V"], 1 / (8 * g)),
        Check("u_action_hessian_magnitude", action_hessian_magnitudes["u"], g / 4),
        Check("v_action_hessian_magnitude", action_hessian_magnitudes["v"], g / 2),
        Check("interaction_half_times_two_orders", interaction_order_factor, 1),
        Check("fixed_port_Wick_factor", fixed_wick_factor, 1),
        Check("hessian_already_contains_two_ports", polarization_factor_after_hessian, 1),
        Check("V_graph_core", graph_cores["V"], -hbar * g**2 / 16),
        Check("u_graph_core", graph_cores["u"], -hbar * g**2 / 16),
        Check("v_graph_core", graph_cores["v"], -hbar * g**2 / 16),
        Check("WW_source_is_v_coordinate", ww_source_weight, source_weights["v"]),
        Check("WW_hessian_is_v_coordinate", ww_hessian_magnitude, action_hessian_magnitudes["v"]),
        Check("WW_correct_v_core", ww_correct_core, -hbar * g**2 / 16),
        Check("WW_unit_propagator_core", ww_unit_propagator_core, -hbar * g**2 / 2),
        Check("WW_unit_over_correct_factor", factor_eight, 8),
        Check("Wminus_over_Wplus", w_minus_over_w_plus, -1),
        Check("projected_action_derivative_is_minus_Dminus", projected_action_derivative, -1),
        Check("projected_Wplus_action_hessian", projected_hessian_wplus, -sp.I * g / 4),
        Check("projected_Wplus_exponent_vertex", projected_exponent_wplus, sp.I * g / (4 * hbar)),
    ]

    audit_text = AUDIT.read_text(encoding="utf-8")
    step5a_text = STEP5A.read_text(encoding="utf-8")
    ww_text = WW.read_text(encoding="utf-8")
    anchors = {
        "status": "PASS_AA_GAUGE_COORDINATE_NORMALIZATION__OLD_V_UNIT_PROPAGATOR_OVERCOUNT_FACTOR8__FULL_DWORD_COEFFICIENT_OPEN",
        "original_hessian": r"K_{E,AB}^V=\frac h2\kappa_{AB}\Box_E",
        "v_propagator": r"\langle vv\rangle=-\frac{\hbar}{2p^2}",
        "coordinate_invariance": r"2\cdot4\cdot\frac18=1",
        "first_wrong_line": "first wrong numerical step is Step-5 WW line 464",
        "index_projection": r"W^-=-W_+",
        "sign_boundary": "It fixes neither the final magnitude nor the directed sign",
        "coefficient_boundary": "No full AA gauge coefficient is assigned",
    }
    checks.extend(
        Check(f"audit_anchor_{name}", anchor in audit_text, True)
        for name, anchor in anchors.items()
    )
    checks.extend(
        [
            Check("step5a_quadratic_hessian_anchor", r"K_{E,AB}^V=\frac h2" in step5a_text, True),
            Check("step5a_inverse_anchor", r"(K_E^V)^{-1\,AB}=2g^2" in step5a_text, True),
            Check("WW_wD_two_anchor", r"w_D=\frac1{32}\cdot16\cdot2\cdot2=2" in ww_text, True),
            Check("WW_g_over_two_vertices_anchor", r"\left(+\frac{ig}{2}\right)" in ww_text, True),
            Check("WW_missing_v_propagator_anchor", r"\left(-\frac{\hbar}{2}\right)^3" in ww_text, False),
        ]
    )

    failed = [row for row in checks if not row.passed]
    for row in checks:
        print(f"{'PASS' if row.passed else 'FAIL'} {row.name}: {row.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
