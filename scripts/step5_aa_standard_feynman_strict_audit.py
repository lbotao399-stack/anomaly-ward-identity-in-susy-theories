#!/usr/bin/env python3
"""Fail-closed conditional arithmetic checks for the ordered-AA audit.

A PASS from this script certifies only the explicitly encoded downstream
arithmetic identities and archive/blocker presence.  It never certifies an
occurrence-resolved superspace D-word or a complete one-loop diagram.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import TypeAlias


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-aa-standard-feynman-strictification.md"
PRO_REVIEW = ROOT / "proposals/gpt-pro-aa-standard-feynman-2026-07-14.md"
PRO_CORRECTION = ROOT / "proposals/gpt-pro-aa-derivation-correction-2026-07-14.md"
PRO_FINAL = ROOT / "proposals/gpt-pro-aa-final-settlement-2026-07-14.md"
STEP5A = ROOT / "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"

CONDITIONAL_SCOPE = "CONDITIONAL_DOWNSTREAM_ARITHMETIC_ONLY"
CLAIM_BOUNDARY = "PASS_DOES_NOT_CERTIFY_FULL_DIAGRAM_DERIVATION"
FULL_DERIVATION_STATUS = "BLOCKED_MISSING_OCCURRENCE_RESOLVED_D_WORD_TRACES"

MISSING_DERIVATION_BLOCKERS = (
    "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION",
    "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
    "BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE",
    "BLOCKED_LOCKED_STEP5_DRED_CONTRACT",
    "BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR",
    "BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES",
    "BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION",
    "BLOCKED_AA_MATTER_DWORD_SIGN_NORMALIZATION",
    "BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER",
)


Monomial: TypeAlias = tuple[int, ...]
Polynomial: TypeAlias = dict[Monomial, Fraction]
GaussianPolynomial: TypeAlias = tuple[Polynomial, Polynomial]
Spinor2: TypeAlias = tuple[Polynomial, Polynomial]


def polynomial_constant(value: int | Fraction, variables: int) -> Polynomial:
    coefficient = Fraction(value)
    return {} if coefficient == 0 else {(0,) * variables: coefficient}


def polynomial_variable(index: int, variables: int) -> Polynomial:
    powers = [0] * variables
    powers[index] = 1
    return {tuple(powers): Fraction(1)}


def polynomial_add(*terms: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for term in terms:
        for monomial, coefficient in term.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
            if result[monomial] == 0:
                del result[monomial]
    return result


def polynomial_scale(coefficient: int | Fraction, term: Polynomial) -> Polynomial:
    coefficient = Fraction(coefficient)
    if coefficient == 0:
        return {}
    return {monomial: coefficient * value for monomial, value in term.items()}


def polynomial_negate(term: Polynomial) -> Polynomial:
    return polynomial_scale(-1, term)


def polynomial_subtract(left: Polynomial, right: Polynomial) -> Polynomial:
    return polynomial_add(left, polynomial_negate(right))


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_power + right_power
                for left_power, right_power in zip(left_monomial, right_monomial, strict=True)
            )
            result[monomial] = result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            if result[monomial] == 0:
                del result[monomial]
    return result


def gaussian_constant(real: int, imaginary: int, variables: int) -> GaussianPolynomial:
    return (
        polynomial_constant(real, variables),
        polynomial_constant(imaginary, variables),
    )


def gaussian_add(*terms: GaussianPolynomial) -> GaussianPolynomial:
    return (
        polynomial_add(*(term[0] for term in terms)),
        polynomial_add(*(term[1] for term in terms)),
    )


def gaussian_negate(term: GaussianPolynomial) -> GaussianPolynomial:
    return polynomial_negate(term[0]), polynomial_negate(term[1])


def gaussian_subtract(left: GaussianPolynomial, right: GaussianPolynomial) -> GaussianPolynomial:
    return gaussian_add(left, gaussian_negate(right))


def gaussian_multiply(left: GaussianPolynomial, right: GaussianPolynomial) -> GaussianPolynomial:
    return (
        polynomial_subtract(
            polynomial_multiply(left[0], right[0]),
            polynomial_multiply(left[1], right[1]),
        ),
        polynomial_add(
            polynomial_multiply(left[0], right[1]),
            polynomial_multiply(left[1], right[0]),
        ),
    )


def gaussian_multiply_real(term: GaussianPolynomial, factor: Polynomial) -> GaussianPolynomial:
    return polynomial_multiply(term[0], factor), polynomial_multiply(term[1], factor)


def matrix_scale_gaussian(
    scalar: GaussianPolynomial,
    matrix: tuple[tuple[GaussianPolynomial, GaussianPolynomial], tuple[GaussianPolynomial, GaussianPolynomial]],
) -> tuple[tuple[GaussianPolynomial, GaussianPolynomial], tuple[GaussianPolynomial, GaussianPolynomial]]:
    return tuple(
        tuple(gaussian_multiply(scalar, entry) for entry in row)
        for row in matrix
    )  # type: ignore[return-value]


def wedge(left: Spinor2, right: Spinor2) -> Polynomial:
    return polynomial_subtract(
        polynomial_multiply(left[0], right[1]),
        polynomial_multiply(left[1], right[0]),
    )


def spinor_add(left: Spinor2, right: Spinor2) -> Spinor2:
    return polynomial_add(left[0], right[0]), polynomial_add(left[1], right[1])


def spinor_scale(coefficient: int | Fraction, spinor: Spinor2) -> Spinor2:
    return polynomial_scale(coefficient, spinor[0]), polynomial_scale(coefficient, spinor[1])


def simplex_moment(a: int, b: int) -> Fraction:
    return Fraction(factorial(a) * factorial(b), factorial(a + b + 2))


def ht_derivative_coefficient(m: int, n: int, k: int, ell: int) -> Fraction:
    return Fraction(comb(m, k) * comb(n, ell), (m + n + 2) * (k + ell + 1))


def check(name: str, condition: bool, actual: object, expected: object) -> dict[str, object]:
    return {
        "id": name,
        "status": "PASS" if condition else "FAIL",
        "actual": str(actual),
        "expected": str(expected),
        "scope": CONDITIONAL_SCOPE,
        "certifies_full_diagram_derivation": False,
    }


def conditional_matter_arithmetic_checks() -> list[dict[str, object]]:
    """Check consequences of the recorded finite parent, not its D-word origin."""
    rows: list[dict[str, object]] = []

    def literal_sigma_e_matrices(variable_count: int):
        sigma_zero = gaussian_constant(0, 0, variable_count)
        sigma_one = gaussian_constant(1, 0, variable_count)
        sigma_i = gaussian_constant(0, 1, variable_count)
        sigma_minus_i = gaussian_constant(0, -1, variable_count)
        sigma_minus_one = gaussian_constant(-1, 0, variable_count)
        sigma_1 = ((sigma_zero, sigma_one), (sigma_one, sigma_zero))
        sigma_2 = ((sigma_zero, gaussian_negate(sigma_i)), (sigma_i, sigma_zero))
        sigma_3 = ((sigma_one, sigma_zero), (sigma_zero, sigma_minus_one))
        sigma_identity = ((sigma_one, sigma_zero), (sigma_zero, sigma_one))
        return (
            matrix_scale_gaussian(sigma_minus_i, sigma_1),
            matrix_scale_gaussian(sigma_minus_i, sigma_2),
            matrix_scale_gaussian(sigma_minus_i, sigma_3),
            sigma_identity,
        )

    def sigma_contraction(
        sigma_e,
        vector: tuple[Polynomial, Polynomial, Polynomial, Polynomial],
    ):
        return tuple(
            tuple(
                gaussian_add(
                    *(
                        gaussian_multiply_real(sigma_e[index][row][column], vector[index])
                        for index in range(4)
                    )
                )
                for column in range(2)
            )
            for row in range(2)
        )

    def gaussian_determinant(matrix) -> GaussianPolynomial:
        return gaussian_subtract(
            gaussian_multiply(matrix[0][0], matrix[1][1]),
            gaussian_multiply(matrix[0][1], matrix[1][0]),
        )

    # Literal Step-1 Euclidean matrices:
    # sigma_E^m=(-i sigma^1,-i sigma^2,-i sigma^3,1),
    # mathsf r=-i sigma_E^m r_m.
    variables = 4
    minus_imaginary_unit = gaussian_constant(0, -1, variables)
    sigma_e = literal_sigma_e_matrices(variables)

    momentum = tuple(polynomial_variable(index, variables) for index in range(variables))
    sigma_dot_momentum = sigma_contraction(sigma_e, momentum)
    bispinor = matrix_scale_gaussian(
        minus_imaginary_unit,
        sigma_dot_momentum,
    )

    r_1, r_2, r_3, r_4 = momentum
    expected_bispinor = (
        (
            (polynomial_negate(r_3), polynomial_negate(r_4)),
            (polynomial_negate(r_1), r_2),
        ),
        (
            (polynomial_negate(r_1), polynomial_negate(r_2)),
            (r_3, polynomial_negate(r_4)),
        ),
    )
    rows.append(
        check(
            "matter_naive_2x2_bispinor_matrix",
            bispinor == expected_bispinor,
            bispinor,
            expected_bispinor,
        )
    )

    determinant = gaussian_determinant(bispinor)
    euclidean_norm_squared = polynomial_add(
        *(polynomial_multiply(component, component) for component in momentum)
    )
    expected_determinant = polynomial_negate(euclidean_norm_squared), {}
    rows.append(
        check(
            "matter_naive_2x2_bispinor_determinant",
            determinant == expected_determinant,
            determinant,
            expected_determinant,
        )
    )

    # Conditional vector-bubble arithmetic: given the recorded finite parent,
    # integral k_+ -> Q_+/2 makes each listed residue a rational multiple of
    # Q_+ wedge Q_+.  This does not derive the parent from a superspace D-word.
    bubble_variables = 4
    p_plus: Spinor2 = (
        polynomial_variable(0, bubble_variables),
        polynomial_variable(1, bubble_variables),
    )
    q_plus: Spinor2 = (
        polynomial_variable(2, bubble_variables),
        polynomial_variable(3, bubble_variables),
    )
    total_plus = spinor_add(p_plus, q_plus)

    bubble_residues = {
        "matter_cut_e0_vector_bubble_zero": polynomial_scale(
            -1, wedge(spinor_scale(Fraction(1, 2), p_plus), p_plus)
        ),
        "matter_cut_e1_vector_bubble_zero": wedge(
            spinor_scale(Fraction(1, 2), total_plus), total_plus
        ),
        "matter_cut_seagull_vector_bubble_zero": polynomial_scale(
            -4, wedge(spinor_scale(Fraction(1, 2), total_plus), total_plus)
        ),
        "matter_cut_J_C_vector_bubble_zero": polynomial_scale(
            -2, wedge(spinor_scale(Fraction(1, 2), p_plus), p_plus)
        ),
        "matter_cut_J_B_vector_bubble_zero": polynomial_scale(
            -2, wedge(spinor_scale(Fraction(1, 2), q_plus), q_plus)
        ),
    }
    for name, residue in bubble_residues.items():
        rows.append(check(name, residue == {}, residue, {}))

    # Derive a rank-two arithmetic consequence from the displayed candidate
    # parent itself.  The parent-to-D-word implication is deliberately absent. With
    # ell=k-yq-z(p+q), substitute k=ell+yq+z(p+q), extract every ell_i^2
    # coefficient, and apply 2*(1/4)*integral_Delta exactly.
    rank_variables = 6  # ell_1,...,ell_4,y,z
    rank_sigma_e = literal_sigma_e_matrices(rank_variables)
    rank_zero = polynomial_constant(0, rank_variables)
    rank_one = polynomial_constant(1, rank_variables)
    ell_vector = tuple(polynomial_variable(index, rank_variables) for index in range(4))
    y_parameter = polynomial_variable(4, rank_variables)
    z_parameter = polynomial_variable(5, rank_variables)

    def rank_parent_diagonal(p_axis: int, q_axis: int):
        p_vector = tuple(rank_one if index == p_axis else rank_zero for index in range(4))
        q_vector = tuple(rank_one if index == q_axis else rank_zero for index in range(4))
        total_vector = tuple(polynomial_add(p_vector[index], q_vector[index]) for index in range(4))
        k_vector = tuple(
            polynomial_add(
                ell_vector[index],
                polynomial_multiply(y_parameter, q_vector[index]),
                polynomial_multiply(z_parameter, total_vector[index]),
            )
            for index in range(4)
        )
        r_0 = k_vector
        r_1 = tuple(polynomial_subtract(k_vector[index], q_vector[index]) for index in range(4))
        r_2 = tuple(polynomial_subtract(k_vector[index], total_vector[index]) for index in range(4))

        sigma_r_0 = sigma_contraction(rank_sigma_e, r_0)
        sigma_r_1 = sigma_contraction(rank_sigma_e, r_1)
        sigma_r_2 = sigma_contraction(rank_sigma_e, r_2)

        def gaussian_wedge(left, right) -> GaussianPolynomial:
            return gaussian_subtract(
                gaussian_multiply(left[0], right[1]),
                gaussian_multiply(left[1], right[0]),
            )

        parent = gaussian_subtract(
            gaussian_multiply(
                gaussian_determinant(sigma_r_0),
                gaussian_wedge(sigma_r_1[0], sigma_r_2[0]),
            ),
            gaussian_multiply(
                gaussian_determinant(sigma_r_1),
                gaussian_wedge(sigma_r_0[0], sigma_r_2[0]),
            ),
        )
        parent = polynomial_scale(4, parent[0]), polynomial_scale(4, parent[1])

        def extract_loop_square(term: Polynomial, loop_axis: int) -> Polynomial:
            coefficient: Polynomial = {}
            for monomial, value in term.items():
                if monomial[loop_axis] != 2:
                    continue
                if any(monomial[index] != 0 for index in range(4) if index != loop_axis):
                    continue
                parameter_monomial = monomial[4], monomial[5]
                coefficient[parameter_monomial] = coefficient.get(parameter_monomial, Fraction(0)) + value
                if coefficient[parameter_monomial] == 0:
                    del coefficient[parameter_monomial]
            return coefficient

        diagonal_coefficients = tuple(
            (
                extract_loop_square(parent[0], loop_axis),
                extract_loop_square(parent[1], loop_axis),
            )
            for loop_axis in range(4)
        )

        def integrate_simplex(term: Polynomial) -> Fraction:
            return sum(
                (
                    value * simplex_moment(monomial[0], monomial[1])
                    for monomial, value in term.items()
                ),
                Fraction(0),
            )

        projection_factor = Fraction(2, 1) * Fraction(1, 4)
        projected_coefficients = tuple(
            (
                projection_factor * integrate_simplex(coefficient[0]),
                projection_factor * integrate_simplex(coefficient[1]),
            )
            for coefficient in diagonal_coefficients
        )

        sigma_p = sigma_contraction(rank_sigma_e, p_vector)[0]
        sigma_q = sigma_contraction(rank_sigma_e, q_vector)[0]
        external_wedge = gaussian_wedge(sigma_p, sigma_q)
        constant_monomial = (0,) * rank_variables
        wedge_constant = (
            external_wedge[0].get(constant_monomial, Fraction(0)),
            external_wedge[1].get(constant_monomial, Fraction(0)),
        )
        wedge_norm = wedge_constant[0] ** 2 + wedge_constant[1] ** 2

        normalized_coefficients = tuple(
            (
                (coefficient[0] * wedge_constant[0] + coefficient[1] * wedge_constant[1])
                / wedge_norm,
                (coefficient[1] * wedge_constant[0] - coefficient[0] * wedge_constant[1])
                / wedge_norm,
            )
            for coefficient in projected_coefficients
        )
        return diagonal_coefficients, normalized_coefficients

    forward_coefficients, forward_ratios = rank_parent_diagonal(0, 3)
    parameter_constant = polynomial_constant(1, 2)
    parameter_z = polynomial_variable(1, 2)
    expected_forward_coefficients = (
        ({}, polynomial_add(polynomial_scale(12, parameter_z), polynomial_scale(-4, parameter_constant))),
        ({}, polynomial_add(polynomial_scale(4, parameter_z), polynomial_scale(-4, parameter_constant))),
        ({}, polynomial_add(polynomial_scale(4, parameter_z), polynomial_scale(-4, parameter_constant))),
        ({}, polynomial_add(polynomial_scale(4, parameter_z), polynomial_scale(4, parameter_constant))),
    )
    for index, (coefficient, expected) in enumerate(
        zip(forward_coefficients, expected_forward_coefficients, strict=True),
        start=1,
    ):
        rows.append(
            check(
                f"matter_rank_two_parent_ell_{index}_squared_coefficient",
                coefficient == expected,
                coefficient,
                expected,
            )
        )

    rows.append(
        check(
            "matter_rank_two_simplex_projection_factor",
            Fraction(2, 1) * Fraction(1, 4) == Fraction(1, 2),
            Fraction(2, 1) * Fraction(1, 4),
            Fraction(1, 2),
        )
    )
    expected_forward_ratios = (
        (Fraction(0), Fraction(0)),
        (-Fraction(2, 3), Fraction(0)),
        (-Fraction(2, 3), Fraction(0)),
        (Fraction(4, 3), Fraction(0)),
    )
    rows.append(
        check(
            "matter_rank_two_forward_simplex_ratios",
            forward_ratios == expected_forward_ratios,
            forward_ratios,
            expected_forward_ratios,
        )
    )

    # The candidate reflected arithmetic exchanges p and q.  Its arithmetic
    # mean is the p<->q-symmetric diagonal representative of this candidate.
    _, reflected_ratios = rank_parent_diagonal(3, 0)
    expected_reflected_ratios = (
        (Fraction(4, 3), Fraction(0)),
        (-Fraction(2, 3), Fraction(0)),
        (-Fraction(2, 3), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    rows.append(
        check(
            "matter_rank_two_reflected_simplex_ratios",
            reflected_ratios == expected_reflected_ratios,
            reflected_ratios,
            expected_reflected_ratios,
        )
    )
    projection_weights = tuple(
        (forward_ratios[index][0] + reflected_ratios[index][0]) / 2
        for index in range(4)
    )
    expected_projection_weights = (
        Fraction(2, 3),
        -Fraction(2, 3),
        -Fraction(2, 3),
        Fraction(2, 3),
    )
    rows.append(
        check(
            "matter_rank_two_derived_symmetric_diagonal_weights",
            projection_weights == expected_projection_weights,
            projection_weights,
            expected_projection_weights,
        )
    )

    # Contract the candidate-parent weights with H=diag(1,h2,h3,1), then impose
    # h2+h3=2-2 epsilon exactly.
    h_variables = 3
    h_2 = polynomial_variable(0, h_variables)
    h_3 = polynomial_variable(1, h_variables)
    epsilon = polynomial_variable(2, h_variables)
    h_one = polynomial_constant(1, h_variables)
    h_two = polynomial_constant(2, h_variables)
    def contract_diagonal(diagonal: tuple[Polynomial, Polynomial, Polynomial, Polynomial]) -> Polynomial:
        return polynomial_add(
            *(
                polynomial_scale(weight, component)
                for weight, component in zip(projection_weights, diagonal, strict=True)
            )
        )

    h_diagonal = (h_one, h_2, h_3, h_one)
    rank_two_ratio = contract_diagonal(h_diagonal)
    displayed_ratio = polynomial_scale(
        -Fraction(2, 3),
        polynomial_subtract(polynomial_add(h_2, h_3), h_two),
    )
    rows.append(
        check(
            "matter_rank_two_H_displayed_ratio",
            rank_two_ratio == displayed_ratio,
            rank_two_ratio,
            displayed_ratio,
        )
    )

    delta_4_ratio = contract_diagonal((h_one, h_one, h_one, h_one))
    rows.append(check("matter_rank_two_H_delta4_zero", delta_4_ratio == {}, delta_4_ratio, {}))

    h_3_locked = polynomial_subtract(
        polynomial_subtract(h_two, polynomial_scale(2, epsilon)),
        h_2,
    )
    locked_constraint = polynomial_add(
        h_2,
        h_3_locked,
        polynomial_negate(h_two),
        polynomial_scale(2, epsilon),
    )
    rows.append(
        check(
            "matter_rank_two_H_locked_trace_constraint",
            locked_constraint == {},
            locked_constraint,
            {},
        )
    )

    locked_ratio = contract_diagonal((h_one, h_2, h_3_locked, h_one))
    expected_locked_ratio = polynomial_scale(Fraction(4, 3), epsilon)
    rows.append(
        check(
            "matter_rank_two_H_epsilon_ratio",
            locked_ratio == expected_locked_ratio,
            locked_ratio,
            expected_locked_ratio,
        )
    )

    return rows


def main() -> int:
    audit = AUDIT.read_text()
    pro_review = PRO_REVIEW.read_text()
    pro_correction = PRO_CORRECTION.read_text()
    pro_final = PRO_FINAL.read_text()
    step5a = STEP5A.read_text()

    rows: list[dict[str, object]] = []

    old_v_propagator = Fraction(2, 4)
    rows.append(check("old_v_propagator_magnitude", old_v_propagator == Fraction(1, 2), old_v_propagator, Fraction(1, 2)))

    old_three_line_error = Fraction(1, 1) / old_v_propagator**3
    rows.append(check("old_three_line_overcount", old_three_line_error == 8, old_three_line_error, 8))

    # These gauge rows reproduce only the unsigned arithmetic recorded in the
    # audit.  The missing odd-D transport signs are guarded by blocker checks
    # below; no row here is a signed D-algebra derivation.
    gauge_d_weight = Fraction(1, 64) * 16 * 2 * 2
    rows.append(check("gauge_closed_D_weight", gauge_d_weight == 1, gauge_d_weight, 1))

    gauge_signed_hessian_propagator_weight = -Fraction(1, 16)
    rows.append(
        check(
            "gauge_signed_hessian_propagator_weight",
            gauge_signed_hessian_propagator_weight == -Fraction(1, 16),
            gauge_signed_hessian_propagator_weight,
            -Fraction(1, 16),
        )
    )

    # -1 is a recorded odd-D transport primitive, not a result of this
    # commutative arithmetic checker.  The audit must retain the corresponding
    # missing-D-word blocker before this conditional product may be displayed.
    recorded_odd_d_transport_sign = -1
    gauge_preintegral = (
        gauge_signed_hessian_propagator_weight
        * gauge_d_weight
        * recorded_odd_d_transport_sign
    )
    rows.append(check("gauge_preintegral", gauge_preintegral == Fraction(1, 16), gauge_preintegral, Fraction(1, 16)))

    triangle_pole = gauge_preintegral * Fraction(1, 16)
    rows.append(check("gauge_triangle_pole_in_pi2_units", triangle_pole == Fraction(1, 256), triangle_pole, Fraction(1, 256)))

    gauge_defect = triangle_pole * 2
    rows.append(check("gauge_defect_in_pi2_units", gauge_defect == Fraction(1, 128), gauge_defect, Fraction(1, 128)))

    gauge_in_lambda1_units = gauge_defect * 16
    rows.append(check("gauge_defect_in_lambda1_units", gauge_in_lambda1_units == Fraction(1, 8), gauge_in_lambda1_units, Fraction(1, 8)))

    rows.extend(conditional_matter_arithmetic_checks())

    rows.append(check("matter_to_gauge_trial_ratio", Fraction(4, 3) / Fraction(1, 8) == Fraction(32, 3), Fraction(4, 3) / Fraction(1, 8), Fraction(32, 3)))

    for m in range(5):
        for n in range(5):
            for k in range(m + 1):
                for ell in range(n + 1):
                    direct = Fraction(comb(m, k) * comb(n, ell), 1)
                    direct *= Fraction(1, (k + ell + 1) * (m + n + 2))
                    formula = ht_derivative_coefficient(m, n, k, ell)
                    rows.append(check(f"ht_derivative_{m}_{n}_{k}_{ell}", direct == formula, direct, formula))

    rows.append(check("simplex_area", simplex_moment(0, 0) == Fraction(1, 2), simplex_moment(0, 0), Fraction(1, 2)))
    rows.append(check("project_zero_shift_kernel", 2 * ht_derivative_coefficient(0, 0, 0, 0) == 1, 2 * ht_derivative_coefficient(0, 0, 0, 0), 1))

    required_audit_fragments = [
        CONDITIONAL_SCOPE,
        "UNVERIFIED_DWORD_ANSATZ",
        "CONDITIONAL_PARENT_DEFINITION",
        *MISSING_DERIVATION_BLOCKERS,
        "REJECTED_PROPAGATOR_NORMALIZATION",
        r"\frac{\lambda_1}{8}",
        r"\frac{4\lambda_1}{3}",
        "NAIVE_FINITE_2X2",
        "Q4S_NO_FIERZ",
    ]
    for fragment in required_audit_fragments:
        rows.append(check(f"audit_fragment::{fragment}", fragment in audit, fragment in audit, True))

    required_pro_review_fragments = [
        "NON_AUTHORITY_PRO_REVIEW",
        "48314dda34aaba5c2afd433c3dc2e31b5f8fd8f41e3266fef7f4659dd2531977",
        r"\boxed{\chi_G=1.}",
        r"\boxed{\chi_M=1,}",
    ]
    for fragment in required_pro_review_fragments:
        rows.append(check(f"pro_review_fragment::{fragment}", fragment in pro_review, fragment in pro_review, True))

    required_pro_correction_fragments = [
        "NON_AUTHORITY_PRO_REVIEW",
        "0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33",
        "# CORRECTED_G_RESULT",
        r"\frac{\lambda_1}{8}",
        r"\Gamma_{AA,M}^{B,\mathrm{full}}",
        r"\frac{32}{3}",
    ]
    for fragment in required_pro_correction_fragments:
        rows.append(
            check(
                f"pro_correction_fragment::{fragment}",
                fragment in pro_correction,
                fragment in pro_correction,
                True,
            )
        )

    required_pro_final_fragments = [
        "NON_AUTHORITY_PRO_REVIEW",
        "1efd04011130a3f64f4e57e42bc58fc1d0aa576af8bc8e7eb68b7f0eaab1f90b",
        "BLOCKED_UNREDUCED_Q4S_MATTER_WORD",
        "BLOCKED_PROJECT_HT_COMPONENT_INTERTWINER",
        "GRAPH_CENSUS",
        "FULL_AA_MATCH",
    ]
    for fragment in required_pro_final_fragments:
        rows.append(
            check(
                f"pro_final_fragment::{fragment}",
                fragment in pro_final,
                fragment in pro_final,
                True,
            )
        )

    required_step5a_fragments = [
        r"K_{E,AB}^V=\frac h2\kappa_{AB}\Box_E",
        r"=2\hbar g^2\kappa^{-1}\Box_E^{-1}",
        r"\frac{\hbar g^2\kappa^{AB}}{16p^2}",
    ]
    for fragment in required_step5a_fragments:
        rows.append(check(f"locked_fragment::{fragment}", fragment in step5a, fragment in step5a, True))

    failed = [row for row in rows if row["status"] != "PASS"]
    result = {
        "audit": str(AUDIT.relative_to(ROOT)),
        "scope": CONDITIONAL_SCOPE,
        "claim_boundary": CLAIM_BOUNDARY,
        "certifies_full_diagram_derivation": False,
        "full_diagram_derivation": {
            "status": FULL_DERIVATION_STATUS,
            "pass_from_this_script_implies_completion": False,
            "required_blockers": list(MISSING_DERIVATION_BLOCKERS),
        },
        "checks": rows,
        "summary": {
            "passed": len(rows) - len(failed),
            "failed": len(failed),
            "status": "PASS" if not failed else "FAIL",
            "scope": CONDITIONAL_SCOPE,
            "claim_boundary": CLAIM_BOUNDARY,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
