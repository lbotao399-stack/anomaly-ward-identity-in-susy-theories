#!/usr/bin/env python3
"""Exact arithmetic checker for the ordered-AA gauge normalization ledger."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-gauge-canonical-normalization-ledger.md"


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
    imaginary = sp.I

    h = g**-2
    v_to_u = sp.sqrt(2) * g
    gamma_linear = v_to_u
    w_linear = -gamma_linear / 8
    a_c_linear = sp.simplify(w_linear / g)
    k_coefficient = -1 / (4 * sp.sqrt(2))

    d_square_conversion = sp.Rational(1, 2)
    marked_k_coefficient = sp.simplify(k_coefficient * d_square_conversion)
    two_source_coefficient = sp.simplify(marked_k_coefficient * k_coefficient)
    closed_d_loop = 16
    mixed_left = 2
    mixed_right = 2
    source_d_weight = sp.simplify(
        two_source_coefficient * closed_d_loop * mixed_left * mixed_right
    )

    source_order_factor = 1
    source_half_factor = 1
    interaction_factor = sp.Rational(1, 2) * 2
    wick_factor = 1

    action_hessian_w = imaginary * g / 4
    action_hessian_w_tilde = -imaginary * g / 4
    tau_e = -1 / hbar
    exponent_w = sp.simplify(tau_e * action_hessian_w)
    exponent_w_tilde = sp.simplify(tau_e * action_hessian_w_tilde)
    vector_propagator = -hbar
    three_propagators = vector_propagator**3
    vertex_propagator_product = sp.simplify(
        exponent_w * exponent_w_tilde * three_propagators
    )
    odd_source_ibp = -1
    parent_prefactor = sp.simplify(
        source_d_weight
        * source_order_factor
        * source_half_factor
        * interaction_factor
        * wick_factor
        * vertex_propagator_product
        * odd_source_ibp
    )

    simplex_area = sp.Rational(1, 2)
    feynman_factor = 2
    selected_square = -4
    evanescent_master = 1 / (32 * sp.pi**2)
    directed = sp.simplify(
        parent_prefactor
        * feynman_factor
        * simplex_area
        * selected_square
        * evanescent_master
    )
    lambda_1 = hbar * g**2 / (16 * sp.pi**2)

    old_coordinate_propagator = sp.Rational(1, 2) * vector_propagator
    three_line_old_ratio = sp.simplify(
        old_coordinate_propagator**3 / vector_propagator**3
    )
    erroneous_unit_over_correct_old = sp.simplify(1 / abs(three_line_old_ratio))

    physical_source_scale = g**2
    physical_output_scale = g * g

    checks = [
        Check("h_equals_g_minus_two", h, g**-2),
        Check("V_to_u_scale", v_to_u, sp.sqrt(2) * g),
        Check("Gamma_linear_coefficient", gamma_linear, sp.sqrt(2) * g),
        Check("W_linear_coefficient", w_linear, -sp.sqrt(2) * g / 8),
        Check("A_c_linear_coefficient", a_c_linear, -sp.sqrt(2) / 8),
        Check("K_coefficient", k_coefficient, -1 / (4 * sp.sqrt(2))),
        Check("Dminus_K_coefficient", marked_k_coefficient, -1 / (8 * sp.sqrt(2))),
        Check("two_source_coefficient", two_source_coefficient, sp.Rational(1, 64)),
        Check("closed_D_loop", closed_d_loop, 16),
        Check("left_mixed_anticommutator", mixed_left, 2),
        Check("right_mixed_anticommutator", mixed_right, 2),
        Check("source_D_weight", source_d_weight, 1),
        Check("ordered_source_no_half", source_half_factor, 1),
        Check("interaction_half_times_two_orders", interaction_factor, 1),
        Check("fixed_directed_Wick_factor", wick_factor, 1),
        Check("action_H_W", action_hessian_w, imaginary * g / 4),
        Check("action_H_Wtilde", action_hessian_w_tilde, -imaginary * g / 4),
        Check("exponent_vertex_W", exponent_w, -imaginary * g / (4 * hbar)),
        Check("exponent_vertex_Wtilde", exponent_w_tilde, imaginary * g / (4 * hbar)),
        Check("three_vector_propagators", three_propagators, -hbar**3),
        Check(
            "vertex_propagator_product",
            vertex_propagator_product,
            -hbar * g**2 / 16,
        ),
        Check("odd_source_IBP", odd_source_ibp, -1),
        Check("parent_prefactor", parent_prefactor, hbar * g**2 / 16),
        Check("feynman_factor_times_simplex_area", feynman_factor * simplex_area, 1),
        Check("selected_square", selected_square, -4),
        Check("evanescent_master", evanescent_master, 1 / (32 * sp.pi**2)),
        Check("directed_coefficient", directed, -lambda_1 / 8),
        Check("old_coordinate_one_line_ratio", old_coordinate_propagator / vector_propagator, sp.Rational(1, 2)),
        Check("old_coordinate_three_line_ratio", three_line_old_ratio, sp.Rational(1, 8)),
        Check("erroneous_unit_factor", erroneous_unit_over_correct_old, 8),
        Check("physical_source_output_scale_cancel", physical_source_scale / physical_output_scale, 1),
    ]

    text = AUDIT.read_text(encoding="utf-8")
    anchors = {
        "linear_letter": r"A_c^{(1)}",
        "source_sixty_four": r"\boxed{\frac1{64}}",
        "hessian_w": r"H_W",
        "hessian_wtilde": r"H_{\widetilde W}",
        "propagator": r"\langle u^A",
        "source_no_half": "There is no $1/2$ in $S_J$",
        "action_factorial": r"\frac1{2!}",
        "selected_square": r"-4(\bar L^2-L_d^2)",
        "coefficient": r"-\frac{\lambda_1}{8}",
        "old_factor_eight": r"2^3=8",
        "target_blind": "No previous $AA$ coefficient",
    }
    checks.extend(Check(f"audit_anchor_{key}", value in text, True) for key, value in anchors.items())

    failed = [check for check in checks if not check.passed]
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"{status} {check.name}: {check.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
