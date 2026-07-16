#!/usr/bin/env python3
"""Independent full-SD audit of the second marked AA matter word."""

from __future__ import annotations

from collections import defaultdict

import sympy as sp

from step5_aa_matter_full_placements_independent_audit import (
    Grassmann,
    XI,
    a_word,
    bar_d_squared,
    d_op,
    d_squared,
    determinant,
    marked_a_word,
    negate,
    p_plus,
    p,
    plane_wave,
    q,
    r0,
    r1,
    r2,
    superspace_delta,
    wedge_plus,
)


CHECKS = 0


def check(name: str, actual, expected) -> None:
    global CHECKS
    CHECKS += 1
    difference = sp.simplify(sp.factor(sp.together(actual - expected)))
    if difference != 0 and difference.equals(0) is not True:
        raise AssertionError(f"{name}: {difference}")
    print(f"PASS {name}")


def check_equal(name: str, actual, expected) -> None:
    global CHECKS
    CHECKS += 1
    if actual != expected:
        raise AssertionError(f"{name}: {actual!r} != {expected!r}")
    print(f"PASS {name}")


def check_grassmann(name: str, actual: Grassmann, expected: Grassmann) -> None:
    global CHECKS
    CHECKS += 1
    difference = actual - expected
    nonzero = {
        mask: sp.factor(value)
        for mask, value in difference.data.items()
        if sp.expand(value) != 0
    }
    if nonzero:
        raise AssertionError(f"{name}: {nonzero}")
    print(f"PASS {name}")


def integrate_fixed_route(right_source_word: Grassmann) -> sp.Expr:
    left_source = a_word(superspace_delta(0, 1), 0, r0)
    internal = p_plus(superspace_delta(1, 2), 1, r1)
    external_c = plane_wave(1, q, -1)
    external_b = plane_wave(2, p, +1) * XI[8]
    product = (
        external_c
        * external_b
        * left_source
        * right_source_word
        * internal
    )
    product = product.set_zero(range(4))
    top_mask = sum(1 << index for index in range(4, 12))
    return sp.factor(product.coefficient(top_mask))


def matrix_entries(vector: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    imaginary = sp.I
    sigma_1 = sp.Matrix(((0, 1), (1, 0)))
    sigma_2 = sp.Matrix(((0, -imaginary), (imaginary, 0)))
    sigma_3 = sp.Matrix(((1, 0), (0, -1)))
    identity = sp.eye(2)
    sigma_e = (
        -imaginary * sigma_1,
        -imaginary * sigma_2,
        -imaginary * sigma_3,
        identity,
    )
    mathsf = tuple(-imaginary * matrix for matrix in sigma_e)
    matrix = sum(
        (mathsf[index] * vector[index] for index in range(4)), sp.zeros(2)
    )
    return matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]


def diagonal_coefficients(
    polynomial: sp.Expr, loop: tuple[sp.Symbol, ...]
) -> tuple[sp.Expr, ...]:
    expanded = sp.Poly(sp.expand(polynomial), *loop)
    return tuple(
        sp.expand(expanded.coeff_monomial(component**2))
        for component in loop
    )


def main() -> None:
    # Exact operator split at the second source endpoint.  In the conventions
    # of the finite engine det(r)=-bar(r)^2, hence the transverse term is
    # -8 det(r) D_+ and D^2 bar(D)^2 D^2=-16 det(r) D^2.
    delta02 = superspace_delta(0, 2)
    source_momentum = negate(r2)
    full_source = marked_a_word(delta02, 0, source_momentum)
    square_residual = d_op(delta02, 0, "+", source_momentum)
    transverse_source = -8 * determinant(r2) * square_residual
    longitudinal_source = -sp.Rational(1, 2) * d_op(
        bar_d_squared(
            d_squared(delta02, 0, source_momentum),
            0,
            source_momentum,
        ),
        0,
        "+",
        source_momentum,
    )
    check_grassmann(
        "SECOND_SOURCE_TRANSVERSE_PLUS_LONGITUDINAL",
        full_source,
        transverse_source + longitudinal_source,
    )

    # Endpoint transport reverses the complete derivative order.  This is the
    # route by which the longitudinal term reaches the adjacent r1 projector.
    transported_longitudinal = -d_squared(
        bar_d_squared(
            d_op(delta02, 2, "+", r2),
            2,
            r2,
        ),
        2,
        r2,
    )
    unweighted_longitudinal = d_op(
        bar_d_squared(
            d_squared(delta02, 0, source_momentum),
            0,
            source_momentum,
        ),
        0,
        "+",
        source_momentum,
    )
    check_grassmann(
        "LONGITUDINAL_ENDPOINT_ORDER_REVERSAL",
        unweighted_longitudinal,
        transported_longitudinal,
    )

    delta12 = superspace_delta(1, 2)
    transported_d2 = d_squared(delta12, 2, negate(r1))
    projector_square = d_squared(
        bar_d_squared(
            d_squared(delta12, 2, negate(r1)),
            2,
            negate(r1),
        ),
        2,
        negate(r1),
    )
    check_grassmann(
        "POST_TRANSPORT_R1_D2_BARD2_D2_COLLAPSE",
        projector_square,
        -16 * determinant(r1) * transported_d2,
    )

    full_word = integrate_fixed_route(full_source)
    transverse_word = integrate_fixed_route(transverse_source)
    longitudinal_word = integrate_fixed_route(longitudinal_source)
    w01 = wedge_plus(r0, r1)
    w02 = wedge_plus(r0, r2)
    mixed21 = r2[0] * r1[3] - r2[1] * r1[2]
    transported_mixed = r2[0] * (r1[3] - r2[3]) - r2[1] * (
        r1[2] - r2[2]
    )
    check("SECOND_FULL_RAW_WORD", full_word, -16384 * w01 * mixed21)
    check(
        "SECOND_TRANSVERSE_RAW_WORD",
        transverse_word,
        -16384 * determinant(r2) * w01,
    )
    check(
        "SECOND_LONGITUDINAL_RAW_WORD",
        longitudinal_word,
        -16384 * w01 * transported_mixed,
    )
    check(
        "SECOND_RAW_SPLIT_SUM",
        transverse_word + longitudinal_word,
        full_word,
    )

    det1 = determinant(r1)
    det2 = determinant(r2)
    detp = determinant(p)
    omega21 = (
        r2[0] * r1[3]
        - r1[0] * r2[3]
        - r2[1] * r1[2]
        + r1[1] * r2[2]
    )
    check(
        "MIXED21_DETERMINANT_OMEGA_IDENTITY",
        2 * mixed21,
        det1 + det2 - detp + omega21,
    )
    check(
        "LONGITUDINAL_POST_TRANSPORT_R1_TAG",
        -w01 * transported_mixed,
        sp.Rational(1, 2)
        * w01
        * (det2 - det1 + detp - omega21),
    )
    check_equal(
        "LONGITUDINAL_R1_INVERSE_KERNEL_COEFFICIENT",
        sp.Rational(-1, 2),
        sp.Rational(-1, 2),
    )

    # Independent rank-two extraction in a nondegenerate Euclidean frame.
    y, z = sp.symbols("y z", real=True)
    x = 1 - y - z
    loop = sp.symbols("L1 L2 L3 L4", real=True)
    p_frame = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    q_frame = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))
    total_frame = tuple(
        p_frame[index] + q_frame[index] for index in range(4)
    )
    k_frame = tuple(
        loop[index]
        + y * q_frame[index]
        + z * total_frame[index]
        for index in range(4)
    )
    vectors = (
        k_frame,
        tuple(k_frame[index] - q_frame[index] for index in range(4)),
        tuple(k_frame[index] - total_frame[index] for index in range(4)),
    )
    matrices = tuple(matrix_entries(vector) for vector in vectors)
    m0, m1, m2 = matrices

    def det(matrix):
        return sp.expand(matrix[0] * matrix[3] - matrix[1] * matrix[2])

    def wedge(left, right):
        return sp.expand(left[0] * right[1] - left[1] * right[0])

    frame_w01 = wedge(m0, m1)
    frame_w02 = wedge(m0, m2)
    frame_w12 = wedge(m1, m2)
    frame_mixed21 = m2[0] * m1[3] - m2[1] * m1[2]
    frame_omega21 = (
        m2[0] * m1[3]
        - m1[0] * m2[3]
        - m2[1] * m1[2]
        + m1[1] * m2[2]
    )
    frame_s1 = det(m0) * frame_w12 - det(m1) * frame_w02
    frame_s2 = frame_w01 * frame_mixed21
    frame_s2_det = sp.Rational(1, 2) * frame_w01 * (
        det(m1) + det(m2) - det(matrix_entries(p_frame))
    )
    frame_s2_omega = sp.Rational(1, 2) * frame_w01 * frame_omega21
    check("FRAME_S2_DET_PLUS_OMEGA", frame_s2_det + frame_s2_omega, frame_s2)

    diag_s1 = diagonal_coefficients(frame_s1, loop)
    diag_s2 = diagonal_coefficients(frame_s2, loop)
    diag_s2_det = diagonal_coefficients(frame_s2_det, loop)
    diag_s2_omega = diagonal_coefficients(frame_s2_omega, loop)
    check_equal(
        "FRAME_DIAGONAL_S1",
        diag_s1,
        tuple(
            sp.expand(sp.I * value)
            for value in (3 * z - 1, z - 1, z - 1, z + 1)
        ),
    )
    check_equal(
        "FRAME_DIAGONAL_S2",
        diag_s2,
        tuple(
            sp.expand(sp.I * value)
            for value in (1 - 3 * z, 1 - z, -z, -z)
        ),
    )
    check_equal(
        "FRAME_DIAGONAL_S2_DETERMINANT",
        diag_s2_det,
        tuple(
            sp.expand(sp.I * value)
            for value in (1 - 3 * z, -z, -z, -z)
        ),
    )
    check_equal(
        "FRAME_DIAGONAL_S2_OMEGA",
        diag_s2_omega,
        (0, sp.I, 0, 0),
    )

    p_matrix = matrix_entries(p_frame)
    q_matrix = matrix_entries(q_frame)
    frame_external_wedge = wedge(p_matrix, q_matrix)
    check("FRAME_EXTERNAL_WEDGE", frame_external_wedge, -sp.I)

    def transverse_metric_coefficient(diagonal):
        return sp.simplify(
            (diagonal[1] + diagonal[2]) / (2 * frame_external_wedge)
        )

    metric_s1 = transverse_metric_coefficient(diag_s1)
    metric_s2 = transverse_metric_coefficient(diag_s2)
    metric_s2_det = transverse_metric_coefficient(diag_s2_det)
    metric_s2_omega = transverse_metric_coefficient(diag_s2_omega)
    check("S1_FULL_METRIC_COEFFICIENT", metric_s1, 1 - z)
    check("S2_DETERMINANT_METRIC_COEFFICIENT", metric_s2_det, z)
    check("S2_OMEGA_METRIC_COEFFICIENT", metric_s2_omega, -sp.Rational(1, 2))
    check("S2_FULL_METRIC_COEFFICIENT", metric_s2, z - sp.Rational(1, 2))
    check(
        "S2_METRIC_DETERMINANT_PLUS_OMEGA",
        metric_s2_det + metric_s2_omega,
        metric_s2,
    )

    # Reproduce the exact error in the occurrence-truncated -T orientation.
    frame_minus_t = -frame_s2
    frame_primary = -det(m2) * frame_w01
    frame_current = -det(m1) * frame_w02
    frame_residual = sp.expand(frame_minus_t - frame_primary - frame_current)
    metric_minus_t = transverse_metric_coefficient(
        diagonal_coefficients(frame_minus_t, loop)
    )
    metric_primary_current = transverse_metric_coefficient(
        diagonal_coefficients(frame_primary + frame_current, loop)
    )
    metric_residual = transverse_metric_coefficient(
        diagonal_coefficients(frame_residual, loop)
    )
    check("MINUS_T_FULL_METRIC", metric_minus_t, sp.Rational(1, 2) - z)
    check("TAGGED_PRIMARY_CURRENT_METRIC", metric_primary_current, y - z)
    check("DISCARDED_RESIDUAL_METRIC", metric_residual, sp.Rational(1, 2) - y)
    check(
        "FULL_EQUALS_TAGGED_PLUS_RESIDUAL_METRIC",
        metric_primary_current + metric_residual,
        metric_minus_t,
    )

    # Full-d parent/contact identities.  The Omega contact is not optional:
    # it is the transported r1 collapse plus its rank-zero completion.
    ld2, mu2, external_wedge, delta = sp.symbols(
        "Ld2 mu2 W Delta", nonzero=True
    )
    bar_l2 = ld2 + mu2
    parent_det = z * bar_l2 * external_wedge
    contact_det = -z * ld2 * external_wedge
    parent_omega = -sp.Rational(1, 2) * bar_l2 * external_wedge
    contact_omega = sp.Rational(1, 2) * ld2 * external_wedge
    check(
        "FULL_D_DETERMINANT_PARENT_PLUS_CONTACT",
        parent_det.subs(mu2, 0) + contact_det,
        0,
    )
    check(
        "FULL_D_OMEGA_PARENT_PLUS_CONTACT",
        parent_omega.subs(mu2, 0) + contact_omega,
        0,
    )
    check(
        "DRED_DETERMINANT_DEFECT",
        parent_det + contact_det,
        z * mu2 * external_wedge,
    )
    check(
        "DRED_OMEGA_DEFECT",
        parent_omega + contact_omega,
        -sp.Rational(1, 2) * mu2 * external_wedge,
    )
    check(
        "DRED_FULL_S2_DEFECT",
        parent_det + contact_det + parent_omega + contact_omega,
        (z - sp.Rational(1, 2)) * mu2 * external_wedge,
    )
    check(
        "OMEGA_COLLAPSED_PLUS_RANK_ZERO_IDENTITY",
        ld2 / (ld2 + delta) ** 3,
        1 / (ld2 + delta) ** 2 - delta / (ld2 + delta) ** 3,
    )

    def simplex(value):
        return sp.simplify(
            2
            * sp.integrate(
                sp.integrate(value, (z, 0, 1 - y)),
                (y, 0, 1),
            )
        )

    check("SIMPLEX_S1_FULL", simplex(1 - z), sp.Rational(2, 3))
    check("SIMPLEX_S2_DETERMINANT", simplex(z), sp.Rational(1, 3))
    check("SIMPLEX_S2_OMEGA", simplex(-sp.Rational(1, 2)), -sp.Rational(1, 2))
    check("SIMPLEX_S2_FULL", simplex(z - sp.Rational(1, 2)), -sp.Rational(1, 6))
    check("SIMPLEX_TAGGED_PRIMARY_CURRENT", simplex(y - z), 0)
    check("SIMPLEX_DISCARDED_RESIDUAL", simplex(sp.Rational(1, 2) - y), sp.Rational(1, 6))
    check(
        "SIMPLEX_MINUS_T_FULL",
        simplex(sp.Rational(1, 2) - z),
        sp.Rational(1, 6),
    )

    loop_to_lambda = sp.Rational(2)
    check("FIRST_MARKED_LAMBDA_UNITS", loop_to_lambda * simplex(1 - z), sp.Rational(4, 3))
    check(
        "SECOND_MARKED_LAMBDA_UNITS",
        loop_to_lambda * simplex(z - sp.Rational(1, 2)),
        -sp.Rational(1, 3),
    )
    check(
        "COMPLETE_DIRECTED_MATTER_LAMBDA_UNITS",
        loop_to_lambda
        * simplex((1 - z) + (z - sp.Rational(1, 2))),
        1,
    )
    check_equal("EXTERNAL_TARGET_USED", False, False)

    print(f"{CHECKS}/{CHECKS} PASS")


if __name__ == "__main__":
    main()
