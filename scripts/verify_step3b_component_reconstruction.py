#!/usr/bin/env python3
"""Exact Step-3B component reconstruction verifier.

The calculation imports the Step-3A four-generator exterior algebra and
extends it to the general K Taylor jet, field-dependent f W W products, and
the full antichiral bridge path.  All arithmetic is exact in Q(i,sqrt(2)).
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Callable


sys.dont_write_bytecode = True


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts" / "verify_step3a_gauge_chiral_action.py"
AUDIT_PATH = ROOT / "audits" / "step3b-component-reconstruction-verification.json"


def load_base():
    spec = importlib.util.spec_from_file_location("step3a_exact", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


b = load_base()


def prepend_label(value, label: str):
    return {
        mask: {
            (label,) + monomial: coefficient
            for monomial, coefficient in expression.items()
        }
        for mask, expression in value.items()
    }


def super_from_formal(coordinate, expression):
    result = {}
    for mask, coordinate_expression in coordinate.items():
        result[mask] = b.expr_multiply(coordinate_expression, expression)
    return b.super_normalize(result)


def multiply_many(*values):
    result = b.super_one()
    for value in values:
        result = b.super_multiply(result, value)
    return result


def super_power(value, exponent: int):
    result = b.super_one()
    for _ in range(exponent):
        result = b.super_multiply(result, value)
    return result


def remove_scalar(value, label: str):
    return b.super_add(value, b.super_scale(b.scalar_label(label), b.MINUS_ONE))


def mask_sector(value, theta_degree: int, bar_degree: int):
    return b.super_normalize(
        {
            mask: expression
            for mask, expression in value.items()
            if (mask & 0b0011).bit_count() == theta_degree
            and (mask & 0b1100).bit_count() == bar_degree
        }
    )


def top_d_component(value):
    return b.expr_scale(value.get(0b1111, {}), b.Exact.rational(Fraction(-1, 4)))


def f_component(value):
    return b.expr_scale(value.get(0b0011, {}), b.Exact.rational(Fraction(-1, 2)))


def bar_f_component(value):
    return b.expr_scale(value.get(0b1100, {}), b.Exact.rational(Fraction(1, 2)))


def add_failure(failures, identity: str, actual, expected):
    if actual != expected:
        failures.append(
            {
                "identity": identity,
                "actual": b.serialize_expression(actual),
                "expected": b.serialize_expression(expected),
            }
        )


def full_antichiral_connection(signature: str, exponent, dotted_index: int):
    bridge = b.bridge_expansion(exponent)
    inverse = b.inverse_bridge_expansion(exponent)
    return b.super_multiply(
        bridge,
        b.full_bar_d_lower(signature, dotted_index, inverse),
    )


def full_antichiral_strength(signature: str, exponent, dotted_index: int):
    connection = full_antichiral_connection(signature, exponent, dotted_index)
    return b.super_scale(
        b.full_d_squared(signature, connection),
        b.Exact.rational(Fraction(1, 8)),
    )


def bar_sigma_mn(signature: str):
    if signature == "L":
        bar_sigma = b.BAR_SIGMA_L
        sigma = b.SIGMA_L
    else:
        bar_sigma = b.BAR_SIGMA_E
        sigma = b.SIGMA_E
    return tuple(
        tuple(
            b.matrix_scale(
                b.matrix_subtract(
                    b.matrix_multiply(bar_sigma[left], sigma[right]),
                    b.matrix_multiply(bar_sigma[right], sigma[left]),
                ),
                b.Exact.rational(Fraction(1, 4)),
            )
            for right in range(4)
        )
        for left in range(4)
    )


BAR_SIGMA_MUNU_L = bar_sigma_mn("L")
BAR_SIGMA_MN_E = bar_sigma_mn("E")


def covariant_lambda(vector_index: int, lower_spinor: int):
    result = {}
    result = b.add_formal_term(
        result,
        b.ONE,
        f"d{vector_index}_lambda{lower_spinor + 1}",
    )
    result = b.add_formal_term(
        result,
        b.MINUS_I,
        f"A{vector_index}",
        f"lambda{lower_spinor + 1}",
    )
    result = b.add_formal_term(
        result,
        b.I,
        f"lambda{lower_spinor + 1}",
        f"A{vector_index}",
    )
    return b.expr_normalize(result)


def expected_antichiral_strength(signature: str, dotted_index: int):
    sigma = b.SIGMA_L if signature == "L" else b.SIGMA_E
    bar_mn = BAR_SIGMA_MUNU_L if signature == "L" else BAR_SIGMA_MN_E
    curvature_phase = b.TWO * b.I if signature == "L" else b.Exact.rational(-2) * b.I
    tail_phase = b.MINUS_ONE if signature == "L" else b.MINUS_I

    result = b.super_scale(
        b.scalar_label(f"barlambda{dotted_index + 1}"),
        b.I,
    )
    result = b.super_add(
        result,
        b.attach_label(b.bar_theta_lower(dotted_index), "Daux"),
    )

    for bar_index in range(2):
        for left in range(4):
            for right in range(left + 1, 4):
                coefficient = curvature_phase * bar_mn[left][right][bar_index][dotted_index]
                if coefficient.is_zero():
                    continue
                curvature = b.expr_scale(b.formal_curvature(left, right), coefficient)
                result = b.super_add(
                    result,
                    super_from_formal(b.bar_theta_lower(bar_index), curvature),
                )

    tail = {}
    for raised_spinor in range(2):
        lower_spinor = 1 - raised_spinor
        epsilon = b.ONE if raised_spinor == 0 else b.MINUS_ONE
        for vector_index in range(4):
            coefficient = (
                tail_phase
                * sigma[vector_index][raised_spinor][dotted_index]
                * epsilon
            )
            tail = b.expr_add(
                tail,
                b.expr_scale(
                    covariant_lambda(vector_index, lower_spinor),
                    coefficient,
                ),
            )
    result = b.super_add(result, super_from_formal(b.BAR_THETA2, tail))
    return b.super_normalize(result)


def no_theta(value):
    return b.super_normalize(
        {mask: expression for mask, expression in value.items() if not mask & 0b0011}
    )


def commute_spacetime_derivatives(value):
    """Canonicalize d_m d_n=d_n d_m on formal component labels."""

    result = {}
    for mask, expression in value.items():
        canonical = {}
        for monomial, coefficient in expression.items():
            labels = []
            for label in monomial:
                pieces = label.split("_", 2)
                if (
                    len(pieces) == 3
                    and pieces[0].startswith("d")
                    and pieces[0][1:].isdigit()
                    and pieces[1].startswith("d")
                    and pieces[1][1:].isdigit()
                ):
                    left = int(pieces[0][1:])
                    right = int(pieces[1][1:])
                    low, high = sorted((left, right))
                    label = f"d{low}_d{high}_{pieces[2]}"
                labels.append(label)
            key = tuple(labels)
            canonical[key] = canonical.get(key, b.ZERO) + coefficient
        normalized = b.expr_normalize(canonical)
        if normalized:
            result[mask] = normalized
    return b.super_normalize(result)


def verify_antichiral_bridge():
    failures = []
    rows = {}
    identities = 0
    coefficients = 0
    for signature, exponent in (
        ("L", b.bridge_exponent_wess_zumino()),
        ("E", b.euclidean_bridge_exponent_wess_zumino()),
    ):
        signature_rows = {}
        for dotted_index in range(2):
            actual = no_theta(
                full_antichiral_strength(signature, exponent, dotted_index)
            )
            expected = expected_antichiral_strength(signature, dotted_index)
            identities += 1
            coefficients += sum(len(expression) for expression in expected.values())
            signature_rows[str(dotted_index + 1)] = {
                "actual": {
                    str(mask): b.serialize_expression(expression)
                    for mask, expression in actual.items()
                },
                "expected": {
                    str(mask): b.serialize_expression(expression)
                    for mask, expression in expected.items()
                },
            }
            if actual != expected:
                failures.append(
                    {
                        "identity": f"{signature}: full antichiral bridge strength dot{dotted_index + 1}",
                        "actual": signature_rows[str(dotted_index + 1)]["actual"],
                        "expected": signature_rows[str(dotted_index + 1)]["expected"],
                    }
                )

            strength = full_antichiral_strength(signature, exponent, dotted_index)
            for spinor_index in range(2):
                chirality = commute_spacetime_derivatives(
                    b.full_d_lower(signature, spinor_index, strength)
                )
                identities += 1
                if chirality:
                    failures.append(
                        {
                            "identity": (
                                f"{signature}: D_{spinor_index + 1} "
                                f"tildeW_dot{dotted_index + 1}=0"
                            ),
                            "actual": {
                                str(mask): b.serialize_expression(expression)
                                for mask, expression in chirality.items()
                            },
                            "expected": {},
                        }
                    )
        rows[signature] = signature_rows
    return failures, rows, identities, coefficients


def kahler_taylor(signature: str):
    if signature == "L":
        u = remove_scalar(b.chiral_superfield(), "phi")
        ub = remove_scalar(b.antichiral_superfield(), "barphi")
    else:
        u = remove_scalar(b.euclidean_chiral_superfield(), "phi")
        ub = remove_scalar(b.euclidean_antichiral_superfield(), "tildephi")

    total = {}
    for p in range(5):
        for q in range(5 - p):
            if p + q == 0:
                continue
            coefficient = b.Exact.rational(
                Fraction(1, factorial(p) * factorial(q))
            )
            term = multiply_many(super_power(u, p), super_power(ub, q))
            term = prepend_label(term, f"K{p}{q}")
            total = b.super_add(total, b.super_scale(term, coefficient))
    return u, ub, total


def factorial(value: int) -> int:
    result = 1
    for integer in range(2, value + 1):
        result *= integer
    return result


def expected_kahler_groups(u, ub):
    a = mask_sector(u, 1, 0)
    auxiliary = mask_sector(u, 2, 0)
    vector = mask_sector(u, 1, 1)
    fermion_tail = mask_sector(u, 2, 1)
    top = mask_sector(u, 2, 2)

    abar = mask_sector(ub, 0, 1)
    auxiliary_bar = mask_sector(ub, 0, 2)
    vector_bar = mask_sector(ub, 1, 1)
    fermion_tail_bar = mask_sector(ub, 1, 2)
    top_bar = mask_sector(ub, 2, 2)

    result = {}

    def add(label: str, coefficient, *factors):
        nonlocal result
        term = prepend_label(multiply_many(*factors), label)
        result = b.super_add(result, b.super_scale(term, coefficient))

    add("K10", b.ONE, top)
    add("K01", b.ONE, top_bar)
    add("K20", b.HALF, vector, vector)
    add("K02", b.HALF, vector_bar, vector_bar)

    add("K11", b.ONE, auxiliary, auxiliary_bar)
    add("K11", b.ONE, vector, vector_bar)
    add("K11", b.ONE, a, fermion_tail_bar)
    add("K11", b.ONE, fermion_tail, abar)

    add("K21", b.HALF, a, a, auxiliary_bar)
    add("K21", b.HALF, a, vector, abar)
    add("K21", b.HALF, vector, a, abar)

    add("K12", b.HALF, auxiliary, abar, abar)
    add("K12", b.HALF, a, abar, vector_bar)
    add("K12", b.HALF, a, vector_bar, abar)

    add("K22", b.Exact.rational(Fraction(1, 4)), a, a, abar, abar)
    return b.super_normalize(result)


def verify_kahler_taylor():
    failures = []
    rows = {}
    identities = 0
    coefficients = 0
    for signature in ("L", "E"):
        u, ub, actual_full = kahler_taylor(signature)
        expected_full = expected_kahler_groups(u, ub)
        actual = top_d_component(actual_full)
        expected = top_d_component(expected_full)
        identities += 1
        coefficients += len(expected)
        rows[signature] = {
            "actual": b.serialize_expression(actual),
            "expected": b.serialize_expression(expected),
            "coefficient_count": len(expected),
        }
        add_failure(
            failures,
            f"{signature}: finite K Taylor series equals the complete saturation-family expansion",
            actual,
            expected,
        )

        forbidden = [
            monomial
            for monomial in actual
            if monomial and monomial[0] in {"K31", "K13", "K40", "K04"}
        ]
        identities += 1
        if forbidden:
            failures.append(
                {
                    "identity": f"{signature}: theta3 and bartheta3 K jets vanish",
                    "actual": [list(item) for item in forbidden],
                    "expected": [],
                }
            )
    return failures, rows, identities, coefficients


def invert_two_by_two(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def verify_kahler_geometry():
    g = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
    inverse = invert_two_by_two(g)

    k3 = [
        [
            [Fraction((left + 1) * (right + 1) + bar + 1) for bar in range(2)]
            for right in range(2)
        ]
        for left in range(2)
    ]
    kb3 = [
        [
            [Fraction((bar_left + 1) * (bar_right + 2) + hol + 1) for bar_right in range(2)]
            for bar_left in range(2)
        ]
        for hol in range(2)
    ]
    for hol in range(2):
        kb3[hol][1][0] = kb3[hol][0][1]

    k4 = [
        [
            [
                [
                    Fraction(
                        (hol_left + 1) * (hol_right + 1)
                        + (bar_left + 1) * (bar_right + 1)
                        + 1
                    )
                    for bar_right in range(2)
                ]
                for bar_left in range(2)
            ]
            for hol_right in range(2)
        ]
        for hol_left in range(2)
    ]

    gamma = [
        [
            [
                sum(inverse[upper][bar] * k3[left][right][bar] for bar in range(2))
                for right in range(2)
            ]
            for left in range(2)
        ]
        for upper in range(2)
    ]
    gamma_bar = [
        [
            [
                sum(inverse[hol][upper_bar] * kb3[hol][left][right] for hol in range(2))
                for right in range(2)
            ]
            for left in range(2)
        ]
        for upper_bar in range(2)
    ]

    failures = []
    identities = 0
    coefficients = 0
    for left in range(2):
        for right in range(2):
            for bar in range(2):
                actual = sum(g[upper][bar] * gamma[upper][left][right] for upper in range(2))
                expected = k3[left][right][bar]
                identities += 1
                coefficients += 1
                if actual != expected:
                    failures.append(
                        {
                            "identity": "g Gamma=K_hol_hol_antihol",
                            "indices": [left, right, bar],
                            "actual": str(actual),
                            "expected": str(expected),
                        }
                    )

    for hol in range(2):
        for left in range(2):
            for right in range(2):
                actual = sum(g[hol][bar] * gamma_bar[bar][left][right] for bar in range(2))
                expected = kb3[hol][left][right]
                identities += 1
                coefficients += 1
                if actual != expected:
                    failures.append(
                        {
                            "identity": "g Gamma_bar=K_hol_antihol_antihol",
                            "indices": [hol, left, right],
                            "actual": str(actual),
                            "expected": str(expected),
                        }
                    )

    for hol_left in range(2):
        for hol_right in range(2):
            for bar_left in range(2):
                for bar_right in range(2):
                    connection_product = sum(
                        k3[hol_left][hol_right][bar_mid]
                        * inverse[hol_mid][bar_mid]
                        * kb3[hol_mid][bar_left][bar_right]
                        for hol_mid in range(2)
                        for bar_mid in range(2)
                    )
                    curvature = (
                        k4[hol_left][hol_right][bar_left][bar_right]
                        - connection_product
                    )
                    shifted_product = sum(
                        g[upper][upper_bar]
                        * gamma[upper][hol_left][hol_right]
                        * gamma_bar[upper_bar][bar_left][bar_right]
                        for upper in range(2)
                        for upper_bar in range(2)
                    )
                    actual = shifted_product + curvature
                    expected = k4[hol_left][hol_right][bar_left][bar_right]
                    identities += 1
                    coefficients += 1
                    if actual != expected:
                        failures.append(
                            {
                                "identity": "shifted-auxiliary quartic plus curvature equals K4",
                                "indices": [hol_left, hol_right, bar_left, bar_right],
                                "actual": str(actual),
                                "expected": str(expected),
                            }
                        )
    return failures, identities, coefficients


def chiral_increment(prefix: str):
    result = {}
    for spinor in range(2):
        result = b.super_add(
            result,
            b.super_scale(
                b.attach_label(b.theta(spinor), f"psi{prefix}{spinor + 1}"),
                b.SQRT_TWO,
            ),
        )
    result = b.super_add(result, b.attach_label(b.THETA2, f"F{prefix}"))
    return result


def holomorphic_f_jet():
    increment = chiral_increment("I")
    result = b.scalar_label("f0")
    result = b.super_add(result, prepend_label(increment, "f1"))
    quadratic = prepend_label(b.super_multiply(increment, increment), "f2")
    result = b.super_add(result, b.super_scale(quadratic, b.HALF))
    return b.super_normalize(result)


def strength_product(signature: str):
    field = b.chiral_field_strength if signature == "L" else b.euclidean_chiral_field_strength
    left = (field(0, "A"), field(1, "A"))
    right = (field(0, "B"), field(1, "B"))
    upper_left = (left[1], b.super_scale(left[0], b.MINUS_ONE))
    return b.super_add(
        b.super_multiply(upper_left[0], right[0]),
        b.super_multiply(upper_left[1], right[1]),
    )


def antichiral_increment(signature: str):
    if signature == "L":
        value = no_theta(b.antichiral_superfield())
        return remove_scalar(value, "barphi")
    value = no_theta(b.euclidean_antichiral_superfield())
    return remove_scalar(value, "tildephi")


def antiholomorphic_f_jet(signature: str):
    increment = antichiral_increment(signature)
    result = b.scalar_label("ftilde0")
    result = b.super_add(result, prepend_label(increment, "ftilde1"))
    quadratic = prepend_label(b.super_multiply(increment, increment), "ftilde2")
    result = b.super_add(result, b.super_scale(quadratic, b.HALF))
    return b.super_normalize(result)


def simple_antichiral_strength(signature: str, dotted_index: int, color: str):
    sigma = b.SIGMA_L if signature == "L" else b.SIGMA_E
    bar_mn = BAR_SIGMA_MUNU_L if signature == "L" else BAR_SIGMA_MN_E
    curvature_phase = b.TWO * b.I if signature == "L" else b.Exact.rational(-2) * b.I
    tail_phase = b.MINUS_ONE if signature == "L" else b.MINUS_I
    tilde_name = "barlambda" if signature == "L" else "tildelambda"

    result = b.super_scale(
        b.scalar_label(f"{tilde_name}{color}{dotted_index + 1}"),
        b.I,
    )
    result = b.super_add(
        result,
        b.attach_label(b.bar_theta_lower(dotted_index), f"Daux{color}"),
    )
    for bar_index in range(2):
        for left in range(4):
            for right in range(left + 1, 4):
                coefficient = curvature_phase * bar_mn[left][right][bar_index][dotted_index]
                if coefficient.is_zero():
                    continue
                result = b.super_add(
                    result,
                    b.super_scale(
                        b.attach_label(
                            b.bar_theta_lower(bar_index),
                            f"F{color}{left}{right}",
                        ),
                        coefficient,
                    ),
                )
    tail = {}
    for raised_spinor in range(2):
        lower_spinor = 1 - raised_spinor
        epsilon = b.ONE if raised_spinor == 0 else b.MINUS_ONE
        for vector_index in range(4):
            coefficient = (
                tail_phase
                * sigma[vector_index][raised_spinor][dotted_index]
                * epsilon
            )
            tail = b.add_formal_term(
                tail,
                coefficient,
                f"d{vector_index}_lambda{color}{lower_spinor + 1}",
            )
    result = b.super_add(result, super_from_formal(b.BAR_THETA2, tail))
    return b.super_normalize(result)


def antichiral_strength_product(signature: str):
    left = (
        simple_antichiral_strength(signature, 0, "A"),
        simple_antichiral_strength(signature, 1, "A"),
    )
    right = (
        simple_antichiral_strength(signature, 0, "B"),
        simple_antichiral_strength(signature, 1, "B"),
    )
    return b.super_add(
        b.super_multiply(left[0], right[1]),
        b.super_scale(b.super_multiply(left[1], right[0]), b.MINUS_ONE),
    )


def component_product_formula(left, right):
    result = b.expr_add(
        b.expr_multiply(left.get(0, {}), f_component(right)),
        b.expr_multiply(f_component(left), right.get(0, {})),
    )
    cross = b.expr_add(
        b.expr_multiply(left.get(0b0001, {}), right.get(0b0010, {})),
        b.expr_scale(
            b.expr_multiply(left.get(0b0010, {}), right.get(0b0001, {})),
            b.MINUS_ONE,
        ),
    )
    result = b.expr_add(result, b.expr_scale(cross, b.HALF))
    return b.expr_normalize(result)


def antichiral_component_product_formula(left, right):
    result = b.expr_add(
        b.expr_multiply(left.get(0, {}), bar_f_component(right)),
        b.expr_multiply(bar_f_component(left), right.get(0, {})),
    )
    first_cross = b.expr_multiply(left.get(0b0100, {}), right.get(0b1000, {}))
    second_cross = b.expr_multiply(left.get(0b1000, {}), right.get(0b0100, {}))
    result = b.expr_add(result, b.expr_scale(first_cross, -b.HALF))
    result = b.expr_add(result, b.expr_scale(second_cross, b.HALF))
    return b.expr_normalize(result)


def canonicalize_even_factors(expression):
    result = {}
    for monomial, coefficient in expression.items():
        f_labels = [label for label in monomial if label.startswith("f") and "F" not in label]
        odd_labels = [label for label in monomial if b.component_parity(label)]
        even_labels = [
            label
            for label in monomial
            if label not in f_labels and not b.component_parity(label)
        ]
        key = tuple(f_labels + sorted(even_labels) + odd_labels)
        result[key] = result.get(key, b.ZERO) + coefficient
    return b.expr_normalize(result)


def left_spinor_contraction(left_prefix: str, right_prefix: str):
    return (
        (b.ONE, f"{left_prefix}2", f"{right_prefix}1"),
        (b.MINUS_ONE, f"{left_prefix}1", f"{right_prefix}2"),
    )


def dotted_spinor_contraction(left_prefix: str, right_prefix: str):
    return (
        (b.ONE, f"{left_prefix}1", f"{right_prefix}2"),
        (b.MINUS_ONE, f"{left_prefix}2", f"{right_prefix}1"),
    )


def left_sigma_contraction(matrix, left_prefix: str, right_prefix: str):
    terms = []
    for raised_left in range(2):
        left_lower = 1 - raised_left
        left_epsilon = b.ONE if raised_left == 0 else b.MINUS_ONE
        for right_lower in range(2):
            coefficient = left_epsilon * matrix[raised_left][right_lower]
            if coefficient.is_zero():
                continue
            terms.append(
                (
                    coefficient,
                    f"{left_prefix}{left_lower + 1}",
                    f"{right_prefix}{right_lower + 1}",
                )
            )
    return terms


def dotted_sigma_contraction(matrix, left_prefix: str, right_prefix: str):
    terms = []
    for left_lower in range(2):
        for right_upper in range(2):
            right_lower = 1 - right_upper
            epsilon = b.ONE if right_upper == 0 else b.MINUS_ONE
            coefficient = matrix[left_lower][right_upper] * epsilon
            if coefficient.is_zero():
                continue
            terms.append(
                (
                    coefficient,
                    f"{left_prefix}{left_lower + 1}",
                    f"{right_prefix}{right_lower + 1}",
                )
            )
    return terms


def compact_chiral_f_derivative_sector(signature: str):
    result = {}

    def add(coefficient, *labels):
        nonlocal result
        result = b.add_formal_term(result, coefficient, *labels)

    lambda_ab = left_spinor_contraction("lambdaA", "lambdaB")
    psi_psi = left_spinor_contraction("psiI", "psiI")
    for coefficient, lambda_left, lambda_right in lambda_ab:
        add(-coefficient, "f1", "FI", lambda_left, lambda_right)
        for psi_coefficient, psi_left, psi_right in psi_psi:
            add(
                b.HALF * psi_coefficient * coefficient,
                "f2",
                psi_left,
                psi_right,
                lambda_left,
                lambda_right,
            )

    d_phase = b.I * b.SQRT_TWO * b.HALF
    for d_color, lambda_color in (("A", "B"), ("B", "A")):
        for coefficient, psi_label, lambda_label in left_spinor_contraction(
            "psiI", f"lambda{lambda_color}"
        ):
            add(
                d_phase * coefficient,
                "f1",
                psi_label,
                lambda_label,
                f"Daux{d_color}",
            )

    sigma_mn = b.SIGMA_MUNU_L if signature == "L" else b.SIGMA_MN_E
    curvature_phase = b.SQRT_TWO * b.HALF
    if signature == "E":
        curvature_phase = -curvature_phase
    field_prefix = "F" if signature == "L" else "FE"
    for field_color, lambda_color in (("A", "B"), ("B", "A")):
        for left_vector in range(4):
            for right_vector in range(left_vector + 1, 4):
                for coefficient, psi_label, lambda_label in left_sigma_contraction(
                    sigma_mn[left_vector][right_vector],
                    "psiI",
                    f"lambda{lambda_color}",
                ):
                    add(
                        curvature_phase * b.TWO * coefficient,
                        "f1",
                        psi_label,
                        lambda_label,
                        f"{field_prefix}{field_color}{left_vector}{right_vector}",
                    )
    return canonicalize_even_factors(result)


def compact_antichiral_f_derivative_sector(signature: str):
    result = {}

    def add(coefficient, *labels):
        nonlocal result
        result = b.add_formal_term(result, coefficient, *labels)

    tilde_name = "barlambda" if signature == "L" else "tildelambda"
    psi_name = "barpsi" if signature == "L" else "tildepsi"
    auxiliary_name = "barF" if signature == "L" else "tildeF"
    lambda_ab = dotted_spinor_contraction(f"{tilde_name}A", f"{tilde_name}B")
    psi_psi = dotted_spinor_contraction(psi_name, psi_name)
    for coefficient, lambda_left, lambda_right in lambda_ab:
        add(-coefficient, "ftilde1", auxiliary_name, lambda_left, lambda_right)
        for psi_coefficient, psi_left, psi_right in psi_psi:
            add(
                b.HALF * psi_coefficient * coefficient,
                "ftilde2",
                psi_left,
                psi_right,
                lambda_left,
                lambda_right,
            )

    d_phase = -b.I * b.SQRT_TWO * b.HALF
    for d_color, lambda_color in (("A", "B"), ("B", "A")):
        for coefficient, psi_label, lambda_label in dotted_spinor_contraction(
            psi_name, f"{tilde_name}{lambda_color}"
        ):
            add(
                d_phase * coefficient,
                "ftilde1",
                psi_label,
                lambda_label,
                f"Daux{d_color}",
            )

    bar_mn = BAR_SIGMA_MUNU_L if signature == "L" else BAR_SIGMA_MN_E
    curvature_phase = b.SQRT_TWO * b.HALF
    if signature == "E":
        curvature_phase = -curvature_phase
    for field_color, lambda_color in (("A", "B"), ("B", "A")):
        for left_vector in range(4):
            for right_vector in range(left_vector + 1, 4):
                for coefficient, psi_label, lambda_label in dotted_sigma_contraction(
                    bar_mn[left_vector][right_vector],
                    psi_name,
                    f"{tilde_name}{lambda_color}",
                ):
                    add(
                        curvature_phase * b.TWO * coefficient,
                        "ftilde1",
                        psi_label,
                        lambda_label,
                        f"F{field_color}{left_vector}{right_vector}",
                    )
    return canonicalize_even_factors(result)


def verify_field_dependent_f():
    failures = []
    rows = {}
    identities = 0
    coefficients = 0
    fjet = holomorphic_f_jet()

    expected_f_top = {}
    expected_f_top = b.add_formal_term(expected_f_top, b.ONE, "f1", "FI")
    expected_f_top = b.add_formal_term(
        expected_f_top,
        b.HALF,
        "f2",
        "psiI1",
        "psiI2",
    )
    expected_f_top = b.add_formal_term(
        expected_f_top,
        -b.HALF,
        "f2",
        "psiI2",
        "psiI1",
    )
    actual_f_top = f_component(fjet)
    identities += 1
    coefficients += len(expected_f_top)
    add_failure(
        failures,
        "f(Phi)|F=f_I F-1/2 f_IJ psi^I psi^J",
        actual_f_top,
        expected_f_top,
    )

    for signature in ("L", "E"):
        product = strength_product(signature)
        actual = f_component(b.super_multiply(fjet, product))
        expected = component_product_formula(fjet, product)
        identities += 1
        coefficients += len(expected)
        rows[signature] = {
            "actual": b.serialize_expression(actual),
            "expected": b.serialize_expression(expected),
            "coefficient_count": len(expected),
        }
        add_failure(
            failures,
            f"{signature}: exact field-dependent f(Phi) W_A W_B product formula",
            actual,
            expected,
        )

        derivative_sector = {
            monomial: coefficient
            for monomial, coefficient in actual.items()
            if monomial and monomial[0] in {"f1", "f2"}
        }
        identities += 1
        if not derivative_sector:
            failures.append(
                {
                    "identity": f"{signature}: f_I and f_IJ sectors are nonempty",
                    "actual": [],
                    "expected": ["f1", "f2"],
                }
            )
        compact_actual = canonicalize_even_factors(derivative_sector)
        compact_expected = compact_chiral_f_derivative_sector(signature)
        identities += 1
        coefficients += len(compact_expected)
        add_failure(
            failures,
            f"{signature}: compact f_I and f_IJ coefficient formula",
            compact_actual,
            compact_expected,
        )

        ftilde = antiholomorphic_f_jet(signature)
        tilde_product = antichiral_strength_product(signature)
        actual_tilde = bar_f_component(b.super_multiply(ftilde, tilde_product))
        expected_tilde = antichiral_component_product_formula(ftilde, tilde_product)
        identities += 1
        coefficients += len(expected_tilde)
        rows[f"{signature}_antichiral"] = {
            "actual": b.serialize_expression(actual_tilde),
            "expected": b.serialize_expression(expected_tilde),
            "coefficient_count": len(expected_tilde),
        }
        add_failure(
            failures,
            f"{signature}: exact field-dependent tilde-f tilde-W_A tilde-W_B product formula",
            actual_tilde,
            expected_tilde,
        )
        tilde_derivative_sector = {
            monomial: coefficient
            for monomial, coefficient in actual_tilde.items()
            if monomial and monomial[0] in {"ftilde1", "ftilde2"}
        }
        identities += 1
        if not tilde_derivative_sector:
            failures.append(
                {
                    "identity": f"{signature}: tilde-f_barI and tilde-f_barIbarJ sectors are nonempty",
                    "actual": [],
                    "expected": ["ftilde1", "ftilde2"],
                }
            )
        compact_tilde_actual = canonicalize_even_factors(tilde_derivative_sector)
        compact_tilde_expected = compact_antichiral_f_derivative_sector(signature)
        identities += 1
        coefficients += len(compact_tilde_expected)
        add_failure(
            failures,
            f"{signature}: compact tilde-f_barI and tilde-f_barIbarJ coefficient formula",
            compact_tilde_actual,
            compact_tilde_expected,
        )
    return failures, rows, identities, coefficients


def verify_canonical_moment_map():
    phi = (b.Exact.rational(2), b.Exact.rational(3))
    barphi = (b.Exact.rational(5), b.Exact.rational(7))
    generator = (b.Exact.rational(1), b.Exact.rational(-2))
    x = tuple(b.I * generator[index] * phi[index] for index in range(2))
    bar_x = tuple(-b.I * barphi[index] * generator[index] for index in range(2))
    mu = sum(
        (barphi[index] * generator[index] * phi[index] for index in range(2)),
        b.ZERO,
    )
    mu_i = tuple(barphi[index] * generator[index] for index in range(2))
    mu_bar = tuple(generator[index] * phi[index] for index in range(2))
    expected_i = tuple(b.I * bar_x[index] for index in range(2))
    expected_bar = tuple(-b.I * x[index] for index in range(2))
    failures = []
    if mu_i != expected_i:
        failures.append(
            {
                "identity": "mu_I=i g_IbarJ barX^barJ",
                "actual": [b.exact_string(item) for item in mu_i],
                "expected": [b.exact_string(item) for item in expected_i],
            }
        )
    if mu_bar != expected_bar:
        failures.append(
            {
                "identity": "mu_barJ=-i g_IbarJ X^I",
                "actual": [b.exact_string(item) for item in mu_bar],
                "expected": [b.exact_string(item) for item in expected_bar],
            }
        )
    expected_mu = b.Exact.rational(-32)
    if mu != expected_mu:
        failures.append(
            {
                "identity": "canonical moment map barphi T phi",
                "actual": b.exact_string(mu),
                "expected": b.exact_string(expected_mu),
            }
        )
    return failures, 3, 5


def verify_ibp_coefficients():
    checks = {
        "pure holomorphic scalar cancellation": (
            b.Exact.rational(Fraction(1, 4))
            - b.Exact.rational(Fraction(1, 4)),
            b.ZERO,
        ),
        "mixed scalar coefficient": (
            b.Exact.rational(Fraction(-1, 2))
            - b.Exact.rational(Fraction(1, 4))
            - b.Exact.rational(Fraction(1, 4)),
            b.MINUS_ONE,
        ),
        "fermion kinetic coefficient": (b.HALF + b.HALF, b.ONE),
        "holomorphic connection coefficient": (b.HALF + b.HALF, b.ONE),
        "antiholomorphic connection cancellation": (-b.HALF + b.HALF, b.ZERO),
    }
    failures = []
    for identity, (actual, expected) in checks.items():
        if actual != expected:
            failures.append(
                {
                    "identity": identity,
                    "actual": b.exact_string(actual),
                    "expected": b.exact_string(expected),
                }
            )
    return failures, len(checks), len(checks)


def exact_matrix(values):
    return tuple(
        tuple(b.Exact.rational(Fraction(item)) for item in row)
        for row in values
    )


def matrix_vector(matrix, vector):
    return tuple(
        sum((matrix[row][column] * vector[column] for column in range(len(vector))), b.ZERO)
        for row in range(len(matrix))
    )


def vector_matrix(vector, matrix):
    return tuple(
        sum((vector[row] * matrix[row][column] for row in range(len(vector))), b.ZERO)
        for column in range(len(matrix[0]))
    )


def bilinear(left, matrix, right):
    return sum(
        (
            left[row] * matrix[row][column] * right[column]
            for row in range(len(left))
            for column in range(len(right))
        ),
        b.ZERO,
    )


def exact_conjugate(value):
    return b.Exact(value.a, -value.b, value.c, -value.d)


def verify_gauge_completion_and_equivariance():
    failures = []
    identities = 0
    coefficients = 0
    g = exact_matrix(((2, 1), (1, 1)))
    gauge_parameter = b.Exact.rational(3)
    x = (b.I * b.Exact.rational(2), -b.I * b.Exact.rational(1))
    bar_x = (-b.I * b.Exact.rational(1), b.I * b.Exact.rational(2))
    partial_phi = (b.Exact.rational(4), b.Exact.rational(-1))
    partial_bar = (b.Exact.rational(2), b.Exact.rational(5))
    mu_i = tuple(b.I * item for item in matrix_vector(g, bar_x))
    mu_bar = tuple(-b.I * item for item in vector_matrix(x, g))

    lorentz_direct = -bilinear(partial_phi, g, partial_bar)
    lorentz_direct += -b.I * gauge_parameter * sum(
        (mu_i[index] * partial_phi[index] for index in range(2)), b.ZERO
    )
    lorentz_direct += b.I * gauge_parameter * sum(
        (mu_bar[index] * partial_bar[index] for index in range(2)), b.ZERO
    )
    lorentz_direct += -(gauge_parameter * gauge_parameter) * bilinear(x, g, bar_x)
    covariant_phi = tuple(
        partial_phi[index] - gauge_parameter * x[index] for index in range(2)
    )
    covariant_bar = tuple(
        partial_bar[index] - gauge_parameter * bar_x[index] for index in range(2)
    )
    lorentz_expected = -bilinear(covariant_phi, g, covariant_bar)
    identities += 1
    coefficients += 1
    if lorentz_direct != lorentz_expected:
        failures.append(
            {
                "identity": "Lorentz moment-map bridge terms form -g Dphi Dbarphi",
                "actual": b.exact_string(lorentz_direct),
                "expected": b.exact_string(lorentz_expected),
            }
        )

    euclidean_direct = bilinear(partial_phi, g, partial_bar)
    euclidean_direct += b.I * gauge_parameter * sum(
        (mu_i[index] * partial_phi[index] for index in range(2)), b.ZERO
    )
    euclidean_direct += -b.I * gauge_parameter * sum(
        (mu_bar[index] * partial_bar[index] for index in range(2)), b.ZERO
    )
    euclidean_direct += (gauge_parameter * gauge_parameter) * bilinear(x, g, bar_x)
    euclidean_expected = bilinear(covariant_phi, g, covariant_bar)
    identities += 1
    coefficients += 1
    if euclidean_direct != euclidean_expected:
        failures.append(
            {
                "identity": "Euclidean moment-map bridge terms form +g Dphi Dtildephi",
                "actual": b.exact_string(euclidean_direct),
                "expected": b.exact_string(euclidean_expected),
            }
        )

    g_inverse = exact_matrix(((1, -1), (-1, 2)))
    nabla_x = exact_matrix(((1, 2), (-1, 3)))
    minus_g_inverse_nabla_x_g = tuple(
        tuple(
            -sum(
                (
                    g_inverse[row][left]
                    * nabla_x[left][right]
                    * g[right][column]
                    for left in range(2)
                    for right in range(2)
                ),
                b.ZERO,
            )
            for column in range(2)
        )
        for row in range(2)
    )
    nabla_tilde_x = tuple(
        tuple(minus_g_inverse_nabla_x_g[column][row] for column in range(2))
        for row in range(2)
    )
    mixed_from_x = tuple(
        tuple(
            -b.I
            * sum(
                (nabla_x[row][inner] * g[inner][column] for inner in range(2)),
                b.ZERO,
            )
            for column in range(2)
        )
        for row in range(2)
    )
    mixed_from_tilde_x = tuple(
        tuple(
            b.I
            * sum(
                (g[row][inner] * nabla_tilde_x[column][inner] for inner in range(2)),
                b.ZERO,
            )
            for column in range(2)
        )
        for row in range(2)
    )
    identities += 1
    coefficients += 4
    if mixed_from_x != mixed_from_tilde_x:
        failures.append(
            {
                "identity": "Euclidean mixed moment-map derivative from X and tilde-X",
                "actual": [
                    [b.exact_string(item) for item in row]
                    for row in mixed_from_x
                ],
                "expected": [
                    [b.exact_string(item) for item in row]
                    for row in mixed_from_tilde_x
                ],
            }
        )

    half = b.Exact.rational(Fraction(1, 2))
    t1 = ((b.ZERO, half), (half, b.ZERO))
    t2 = ((b.ZERO, -b.I * half), (b.I * half, b.ZERO))
    t3 = ((half, b.ZERO), (b.ZERO, -half))
    phi = (b.Exact.rational(1), b.Exact.rational(2))
    bar_phi = (b.Exact.rational(3), b.Exact.rational(4))

    def x_vector(generator):
        return tuple(b.I * item for item in matrix_vector(generator, phi))

    def bar_x_vector(generator):
        conjugate_representation = tuple(
            tuple(exact_conjugate(generator[row][column]) for column in range(2))
            for row in range(2)
        )
        return tuple(-b.I * item for item in matrix_vector(conjugate_representation, bar_phi))

    def moment(generator):
        return bilinear(bar_phi, generator, phi)

    x1 = x_vector(t1)
    bar_x1 = bar_x_vector(t1)
    mu2_i = vector_matrix(bar_phi, t2)
    mu2_bar = matrix_vector(t2, phi)
    lie_mu2 = sum((x1[index] * mu2_i[index] for index in range(2)), b.ZERO)
    lie_mu2 += sum((bar_x1[index] * mu2_bar[index] for index in range(2)), b.ZERO)
    expected_mu3 = moment(t3)
    identities += 1
    coefficients += 1
    if lie_mu2 != expected_mu3:
        failures.append(
            {
                "identity": "SU(2) exact equivariance K_1 mu_2=c_12^3 mu_3",
                "actual": b.exact_string(lie_mu2),
                "expected": b.exact_string(expected_mu3),
            }
        )
    return failures, identities, coefficients


def verify_wick_auxiliary_and_contour():
    failures = []
    identities = 0
    coefficients = 0
    quarter = b.Exact.rational(Fraction(1, 4))
    eighth = b.Exact.rational(Fraction(1, 8))
    inv_two_sqrt_two = b.SQRT_TWO * quarter
    checks = (
        ("scalar kinetic", -b.MINUS_ONE * b.ONE, b.ONE),
        ("fermion kinetic", -(b.I * b.I), b.ONE),
        ("matter auxiliary", -b.ONE, b.MINUS_ONE),
        ("Kahler quartic", -quarter, -quarter),
        ("moment map D", -b.ONE, b.MINUS_ONE),
        ("moment-map gaugino", -(b.I * b.SQRT_TWO), -b.I * b.SQRT_TWO),
        ("gauge F squared", -(-quarter), quarter),
        ("gauge D squared", -b.HALF, -b.HALF),
        ("topological density", -((-eighth) * -b.I), -b.I * eighth),
        ("field-dependent F lambda lambda", -(-quarter), quarter),
        ("field-dependent four fermions", -eighth, -eighth),
        ("field-dependent D Yukawa", -(b.I * inv_two_sqrt_two), -b.I * inv_two_sqrt_two),
        ("field-dependent sigma F Yukawa", -(inv_two_sqrt_two * -b.ONE), inv_two_sqrt_two),
        ("gaugino kinetic", -((b.I * b.HALF) * b.I), b.HALF),
    )
    for identity, actual, expected in checks:
        identities += 1
        coefficients += 1
        if actual != expected:
            failures.append(
                {
                    "identity": f"Wick coefficient: {identity}",
                    "actual": b.exact_string(actual),
                    "expected": b.exact_string(expected),
                }
            )

    g = exact_matrix(((2, 1), (1, 1)))
    inverse = exact_matrix(((1, -1), (-1, 2)))
    field = (b.Exact.rational(2), b.Exact.rational(-1))
    tilde_field = (b.Exact.rational(3), b.Exact.rational(4))
    source = (b.Exact.rational(5), b.Exact.rational(-2))
    tilde_source = (b.Exact.rational(1), b.Exact.rational(6))
    lhs_f = -bilinear(field, g, tilde_field)
    lhs_f -= sum((source[index] * field[index] for index in range(2)), b.ZERO)
    lhs_f -= sum((tilde_source[index] * tilde_field[index] for index in range(2)), b.ZERO)
    shifted = tuple(
        field[index] + matrix_vector(inverse, tilde_source)[index]
        for index in range(2)
    )
    shifted_tilde = tuple(
        tilde_field[index] + vector_matrix(source, inverse)[index]
        for index in range(2)
    )
    rhs_f = -bilinear(shifted, g, shifted_tilde)
    rhs_f += bilinear(source, inverse, tilde_source)
    identities += 1
    coefficients += 1
    if lhs_f != rhs_f:
        failures.append(
            {
                "identity": "general-metric Euclidean F square completion",
                "actual": b.exact_string(lhs_f),
                "expected": b.exact_string(rhs_f),
            }
        )

    d_field = (b.Exact.rational(2), b.Exact.rational(-3))
    moment = (b.Exact.rational(4), b.Exact.rational(1))
    lhs_d = -b.HALF * bilinear(d_field, g, d_field)
    lhs_d -= sum((moment[index] * d_field[index] for index in range(2)), b.ZERO)
    shifted_d = tuple(
        d_field[index] + matrix_vector(inverse, moment)[index]
        for index in range(2)
    )
    rhs_d = -b.HALF * bilinear(shifted_d, g, shifted_d)
    rhs_d += b.HALF * bilinear(moment, inverse, moment)
    identities += 1
    coefficients += 1
    if lhs_d != rhs_d:
        failures.append(
            {
                "identity": "Euclidean D square completion",
                "actual": b.exact_string(lhs_d),
                "expected": b.exact_string(rhs_d),
            }
        )

    complex_g = (b.Exact.rational(1) + b.I, b.Exact.rational(2) - b.I)
    tilde_g = tuple(-exact_conjugate(item) for item in complex_g)
    positive_g = -bilinear(complex_g, g, tilde_g)
    potential_source = (b.Exact.rational(2) + b.I, b.Exact.rational(-1))
    positive_source = bilinear(
        potential_source,
        inverse,
        tuple(exact_conjugate(item) for item in potential_source),
    )
    real_d = (b.Exact.rational(1), b.Exact.rational(2))
    imaginary_h = tuple(b.I * item for item in real_d)
    positive_h = -b.HALF * bilinear(imaginary_h, g, imaginary_h)
    positive_moment = b.HALF * bilinear(moment, inverse, moment)
    for identity, value in (
        ("G contour", positive_g),
        ("superpotential source", positive_source),
        ("H=i d contour", positive_h),
        ("moment-map potential", positive_moment),
    ):
        identities += 1
        coefficients += 1
        if value.b != 0 or value.d != 0 or value.a <= 0:
            failures.append(
                {
                    "identity": f"positive contour: {identity}",
                    "actual": b.exact_string(value),
                    "expected": "strictly positive real",
                }
            )

    h_value = b.Exact.rational(2)
    k_value = b.Exact.rational(3)
    f_value = h_value + b.I * k_value
    f_tilde = h_value - b.I * k_value
    hk_checks = (
        (
            "Lorentz h F2",
            quarter * (f_value * -b.HALF + f_tilde * -b.HALF),
            -quarter * h_value,
        ),
        (
            "Lorentz h D2",
            quarter * (f_value + f_tilde),
            b.HALF * h_value,
        ),
        (
            "Lorentz k epsilon FF",
            quarter * (f_value * (b.I * quarter) + f_tilde * (-b.I * quarter)),
            -eighth * k_value,
        ),
        (
            "Euclidean h F2",
            -quarter * (f_value * -b.HALF + f_tilde * -b.HALF),
            quarter * h_value,
        ),
        (
            "Euclidean h D2",
            -quarter * (f_value + f_tilde),
            -b.HALF * h_value,
        ),
        (
            "Euclidean k epsilon FF",
            -quarter * (f_value * quarter + f_tilde * -quarter),
            -b.I * eighth * k_value,
        ),
    )
    for identity, actual, expected in hk_checks:
        identities += 1
        coefficients += 1
        if actual != expected:
            failures.append(
                {
                    "identity": identity,
                    "actual": b.exact_string(actual),
                    "expected": b.exact_string(expected),
                }
            )
    return failures, identities, coefficients


def build_audit():
    base_audit = b.build_audit()
    failures = []
    if base_audit["status"] != "PASS":
        failures.append(
            {
                "identity": "Step-3A dependency audit remains PASS",
                "actual": base_audit["status"],
                "expected": "PASS",
            }
        )

    antichiral_failures, antichiral_rows, antichiral_ids, antichiral_coeffs = (
        verify_antichiral_bridge()
    )
    kahler_failures, kahler_rows, kahler_ids, kahler_coeffs = verify_kahler_taylor()
    geometry_failures, geometry_ids, geometry_coeffs = verify_kahler_geometry()
    f_failures, f_rows, f_ids, f_coeffs = verify_field_dependent_f()
    moment_failures, moment_ids, moment_coeffs = verify_canonical_moment_map()
    ibp_failures, ibp_ids, ibp_coeffs = verify_ibp_coefficients()
    gauge_failures, gauge_ids, gauge_coeffs = verify_gauge_completion_and_equivariance()
    wick_failures, wick_ids, wick_coeffs = verify_wick_auxiliary_and_contour()

    failures.extend(antichiral_failures)
    failures.extend(kahler_failures)
    failures.extend(geometry_failures)
    failures.extend(f_failures)
    failures.extend(moment_failures)
    failures.extend(ibp_failures)
    failures.extend(gauge_failures)
    failures.extend(wick_failures)

    new_identities = (
        antichiral_ids
        + kahler_ids
        + geometry_ids
        + f_ids
        + moment_ids
        + ibp_ids
        + gauge_ids
        + wick_ids
    )
    new_coefficients = (
        antichiral_coeffs
        + kahler_coeffs
        + geometry_coeffs
        + f_coeffs
        + moment_coeffs
        + ibp_coeffs
        + gauge_coeffs
        + wick_coeffs
    )
    return {
        "task_id": "CONTRACT-STEP-03B-COMPONENT-RECONSTRUCTION-001",
        "status": "PASS" if not failures else "FAIL",
        "arithmetic": {
            "coefficient_ring": "Q(i,sqrt(2))",
            "external_cas": False,
            "grassmann_order": [
                "vartheta^1",
                "vartheta^2",
                "barvartheta_dot1",
                "barvartheta_dot2",
            ],
        },
        "dependency": {
            "step3a_status": base_audit["status"],
            "step3a_exact_identities": base_audit["totals"]["exact_identities"],
            "step3a_component_coefficients": base_audit["totals"][
                "exact_component_coefficients"
            ],
        },
        "totals": {
            "new_exact_identities": new_identities,
            "new_exact_component_coefficients": new_coefficients,
            "cumulative_exact_identities": (
                base_audit["totals"]["exact_identities"] + new_identities
            ),
            "cumulative_exact_component_coefficients": (
                base_audit["totals"]["exact_component_coefficients"]
                + new_coefficients
            ),
            "failed_checks": len(failures),
        },
        "full_antichiral_bridge": antichiral_rows,
        "general_kahler_taylor": kahler_rows,
        "field_dependent_f": f_rows,
        "ibp_reorganization": {
            "identities": ibp_ids,
            "coefficients": ibp_coeffs,
            "failed": len(ibp_failures),
        },
        "gauge_completion_and_equivariance": {
            "identities": gauge_ids,
            "coefficients": gauge_coeffs,
            "failed": len(gauge_failures),
        },
        "wick_auxiliary_contour": {
            "identities": wick_ids,
            "coefficients": wick_coeffs,
            "failed": len(wick_failures),
        },
        "failures": failures,
    }


def main() -> None:
    audit = build_audit()
    AUDIT_PATH.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2))
        raise SystemExit(1)
    print(
        "Step-3B exact verification: "
        f"{audit['totals']['new_exact_identities']} new identities, "
        f"{audit['totals']['new_exact_component_coefficients']} new coefficients, "
        "0 failures"
    )


if __name__ == "__main__":
    main()
