#!/usr/bin/env python3
"""Exact Step-3A gauge--chiral component verification.

The coefficient ring is Q(i,sqrt(2)); the odd-coordinate algebra is the
four-generator exterior algebra ordered as

    vartheta^1 < vartheta^2 < barvartheta_dot1 < barvartheta_dot2.

Component coefficients remain ordered formal monomials.  No floating point
and no external computer-algebra package are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "audits" / "step3a-gauge-chiral-verification.json"


@dataclass(frozen=True)
class Exact:
    """a + b i + c sqrt(2) + d i sqrt(2), with rational coefficients."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @staticmethod
    def rational(value: int | Fraction) -> "Exact":
        return Exact(Fraction(value))

    def __add__(self, other: "Exact") -> "Exact":
        return Exact(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __neg__(self) -> "Exact":
        return Exact(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: "Exact") -> "Exact":
        return self + (-other)

    def __mul__(self, other: "Exact") -> "Exact":
        # (z0 + z1 s)(w0 + w1 s), s^2=2; each z is Gaussian rational.
        z0w0_r = self.a * other.a - self.b * other.b
        z0w0_i = self.a * other.b + self.b * other.a
        z1w1_r = self.c * other.c - self.d * other.d
        z1w1_i = self.c * other.d + self.d * other.c
        cross_r = (
            self.a * other.c - self.b * other.d
            + self.c * other.a - self.d * other.b
        )
        cross_i = (
            self.a * other.d + self.b * other.c
            + self.c * other.b + self.d * other.a
        )
        return Exact(z0w0_r + 2 * z1w1_r, z0w0_i + 2 * z1w1_i, cross_r, cross_i)

    def is_zero(self) -> bool:
        return self.a == self.b == self.c == self.d == 0


ZERO = Exact()
ONE = Exact.rational(1)
MINUS_ONE = Exact.rational(-1)
TWO = Exact.rational(2)
HALF = Exact.rational(Fraction(1, 2))
I = Exact(Fraction(0), Fraction(1))
MINUS_I = -I
SQRT_TWO = Exact(Fraction(0), Fraction(0), Fraction(1))


def exact_string(value: Exact) -> str:
    pieces: list[str] = []
    for coefficient, basis in (
        (value.a, ""),
        (value.b, "i"),
        (value.c, "sqrt(2)"),
        (value.d, "i sqrt(2)"),
    ):
        if coefficient == 0:
            continue
        sign = "+" if coefficient > 0 and pieces else ""
        if basis and abs(coefficient) == 1:
            number = "-" if coefficient < 0 else ""
        else:
            number = str(coefficient)
        pieces.append(f"{sign}{number}{basis}")
    return "0" if not pieces else "".join(pieces)


FormalMonomial = tuple[str, ...]
FormalExpression = dict[FormalMonomial, Exact]
SuperExpression = dict[int, FormalExpression]


def component_parity(label: str) -> int:
    return int("psi" in label or "lambda" in label)


def monomial_parity(monomial: FormalMonomial) -> int:
    return sum(component_parity(label) for label in monomial) % 2


def expr_normalize(value: FormalExpression) -> FormalExpression:
    return {monomial: coefficient for monomial, coefficient in value.items() if not coefficient.is_zero()}


def expr_add(left: FormalExpression, right: FormalExpression) -> FormalExpression:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, ZERO) + coefficient
    return expr_normalize(result)


def expr_scale(value: FormalExpression, coefficient: Exact) -> FormalExpression:
    return expr_normalize({monomial: coefficient * term for monomial, term in value.items()})


def expr_multiply(left: FormalExpression, right: FormalExpression) -> FormalExpression:
    result: FormalExpression = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = left_monomial + right_monomial
            coefficient = left_coefficient * right_coefficient
            result[monomial] = result.get(monomial, ZERO) + coefficient
    return expr_normalize(result)


def super_normalize(value: SuperExpression) -> SuperExpression:
    return {mask: expr_normalize(expression) for mask, expression in value.items() if expr_normalize(expression)}


def super_add(left: SuperExpression, right: SuperExpression) -> SuperExpression:
    result = {mask: dict(expression) for mask, expression in left.items()}
    for mask, expression in right.items():
        result[mask] = expr_add(result.get(mask, {}), expression)
    return super_normalize(result)


def super_scale(value: SuperExpression, coefficient: Exact) -> SuperExpression:
    return super_normalize({mask: expr_scale(expression, coefficient) for mask, expression in value.items()})


def wedge_sign(left_mask: int, right_mask: int) -> int:
    inversions = 0
    for left_index in range(4):
        if not left_mask & (1 << left_index):
            continue
        for right_index in range(4):
            if right_mask & (1 << right_index) and left_index > right_index:
                inversions += 1
    return -1 if inversions % 2 else 1


def super_multiply(left: SuperExpression, right: SuperExpression) -> SuperExpression:
    result: SuperExpression = {}
    for left_mask, left_expression in left.items():
        for right_mask, right_expression in right.items():
            if left_mask & right_mask:
                continue
            new_mask = left_mask | right_mask
            degree_right = right_mask.bit_count()
            wedge = wedge_sign(left_mask, right_mask)
            term: FormalExpression = {}
            for left_monomial, left_coefficient in left_expression.items():
                crossing = -1 if monomial_parity(left_monomial) * degree_right % 2 else 1
                for right_monomial, right_coefficient in right_expression.items():
                    monomial = left_monomial + right_monomial
                    coefficient = left_coefficient * right_coefficient
                    if wedge * crossing == -1:
                        coefficient = -coefficient
                    term[monomial] = term.get(monomial, ZERO) + coefficient
            result[new_mask] = expr_add(result.get(new_mask, {}), term)
    return super_normalize(result)


def super_left_derivative(index: int, value: SuperExpression) -> SuperExpression:
    result: SuperExpression = {}
    bit = 1 << index
    lower_bits = bit - 1
    for mask, expression in value.items():
        if not mask & bit:
            continue
        sign = -1 if (mask & lower_bits).bit_count() % 2 else 1
        term = expression if sign == 1 else expr_scale(expression, MINUS_ONE)
        new_mask = mask ^ bit
        result[new_mask] = expr_add(result.get(new_mask, {}), term)
    return super_normalize(result)


def theta_d_squared(value: SuperExpression) -> SuperExpression:
    # D^a D_a=2 partial_2 partial_1 at vartheta=barvartheta=0.
    return super_scale(super_left_derivative(1, super_left_derivative(0, value)), TWO)


def bar_d_squared(value: SuperExpression) -> SuperExpression:
    # barD_dot a barD^dot a=2 partial_bar1 partial_bar2 at the origin.
    return super_scale(super_left_derivative(2, super_left_derivative(3, value)), TWO)


def super_one() -> SuperExpression:
    return {0: {(): ONE}}


def coordinate(index: int, coefficient: Exact = ONE) -> SuperExpression:
    return {1 << index: {(): coefficient}}


def attach_label(value: SuperExpression, label: str) -> SuperExpression:
    return {
        mask: {monomial + (label,): coefficient for monomial, coefficient in expression.items()}
        for mask, expression in value.items()
    }


def scalar_label(label: str) -> SuperExpression:
    return {0: {(label,): ONE}}


def theta(index: int) -> SuperExpression:
    return coordinate(index)


def bar_theta_lower(index: int) -> SuperExpression:
    return coordinate(2 + index)


def bar_theta_upper(index: int) -> SuperExpression:
    if index == 0:
        return coordinate(3)
    if index == 1:
        return coordinate(2, MINUS_ONE)
    raise IndexError(index)


THETA2 = {0b0011: {(): Exact.rational(-2)}}
BAR_THETA2 = {0b1100: {(): Exact.rational(2)}}
TOP = super_multiply(THETA2, BAR_THETA2)


SIGMA_0 = ((ONE, ZERO), (ZERO, ONE))
SIGMA_1 = ((ZERO, ONE), (ONE, ZERO))
SIGMA_2 = ((ZERO, MINUS_I), (I, ZERO))
SIGMA_3 = ((ONE, ZERO), (ZERO, MINUS_ONE))
SIGMA_L = (SIGMA_0, SIGMA_1, SIGMA_2, SIGMA_3)


def matrix_multiply(
    left: tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
    right: tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
) -> tuple[tuple[Exact, Exact], tuple[Exact, Exact]]:
    return tuple(
        tuple(
            left[row][0] * right[0][column] + left[row][1] * right[1][column]
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(
    value: tuple[tuple[Exact, Exact], tuple[Exact, Exact]], coefficient: Exact
) -> tuple[tuple[Exact, Exact], tuple[Exact, Exact]]:
    return tuple(tuple(coefficient * entry for entry in row) for row in value)  # type: ignore[return-value]


def matrix_subtract(
    left: tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
    right: tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
) -> tuple[tuple[Exact, Exact], tuple[Exact, Exact]]:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def theta_sigma_bar_theta(vector_index: int) -> SuperExpression:
    result: SuperExpression = {}
    for spinor_index in range(2):
        for dotted_index in range(2):
            term = super_multiply(theta(spinor_index), bar_theta_upper(dotted_index))
            result = super_add(result, super_scale(term, SIGMA_L[vector_index][spinor_index][dotted_index]))
    return result


B_L = tuple(theta_sigma_bar_theta(vector_index) for vector_index in range(4))

SIGMA_E = (
    matrix_scale(SIGMA_1, MINUS_I),
    matrix_scale(SIGMA_2, MINUS_I),
    matrix_scale(SIGMA_3, MINUS_I),
    SIGMA_0,
)
BAR_SIGMA_E = (
    matrix_scale(SIGMA_1, I),
    matrix_scale(SIGMA_2, I),
    matrix_scale(SIGMA_3, I),
    SIGMA_0,
)


def theta_sigma_bar_theta_with_sigma(
    sigma: tuple[
        tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
        tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
        tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
        tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
    ],
    vector_index: int,
) -> SuperExpression:
    result: SuperExpression = {}
    for spinor_index in range(2):
        for dotted_index in range(2):
            term = super_multiply(theta(spinor_index), bar_theta_upper(dotted_index))
            result = super_add(result, super_scale(term, sigma[vector_index][spinor_index][dotted_index]))
    return result


B_E = tuple(theta_sigma_bar_theta_with_sigma(SIGMA_E, vector_index) for vector_index in range(4))


def upper_dotted_label(prefix: str, dotted_index: int, derivative: int | None = None) -> tuple[str, Exact]:
    # xi^dot1=xi_dot2, xi^dot2=-xi_dot1.
    lower_index = 1 - dotted_index
    coefficient = ONE if dotted_index == 0 else MINUS_ONE
    stem = f"{prefix}{lower_index + 1}"
    if derivative is not None:
        stem = f"d{derivative}_{stem}"
    return stem, coefficient


def chiral_superfield() -> SuperExpression:
    result = scalar_label("phi")
    for mu in range(4):
        result = super_add(result, super_scale(attach_label(B_L[mu], f"d{mu}_phi"), MINUS_I))
    for mu in range(4):
        for nu in range(4):
            term = super_multiply(B_L[mu], B_L[nu])
            result = super_add(
                result,
                super_scale(attach_label(term, f"dd{mu}{nu}_phi"), -HALF),
            )
    for spinor_index in range(2):
        result = super_add(
            result,
            super_scale(attach_label(theta(spinor_index), f"psi{spinor_index + 1}"), SQRT_TWO),
        )
        for mu in range(4):
            term = super_multiply(theta(spinor_index), B_L[mu])
            result = super_add(
                result,
                super_scale(
                    attach_label(term, f"d{mu}_psi{spinor_index + 1}"),
                    MINUS_I * SQRT_TWO,
                ),
            )
    result = super_add(result, attach_label(THETA2, "F"))
    return super_normalize(result)


def antichiral_superfield() -> SuperExpression:
    result = scalar_label("barphi")
    for mu in range(4):
        result = super_add(result, super_scale(attach_label(B_L[mu], f"d{mu}_barphi"), I))
    for mu in range(4):
        for nu in range(4):
            term = super_multiply(B_L[mu], B_L[nu])
            result = super_add(
                result,
                super_scale(attach_label(term, f"dd{mu}{nu}_barphi"), -HALF),
            )
    for dotted_index in range(2):
        label, epsilon = upper_dotted_label("barpsi", dotted_index)
        result = super_add(
            result,
            super_scale(attach_label(bar_theta_lower(dotted_index), label), epsilon * SQRT_TWO),
        )
        for mu in range(4):
            derivative_label, derivative_epsilon = upper_dotted_label("barpsi", dotted_index, mu)
            term = super_multiply(bar_theta_lower(dotted_index), B_L[mu])
            result = super_add(
                result,
                super_scale(
                    attach_label(term, derivative_label),
                    I * SQRT_TWO * derivative_epsilon,
                ),
            )
    result = super_add(result, attach_label(BAR_THETA2, "barF"))
    return super_normalize(result)


def euclidean_chiral_superfield() -> SuperExpression:
    result = scalar_label("phi")
    for vector_index in range(4):
        result = super_add(result, attach_label(B_E[vector_index], f"d{vector_index}_phi"))
    for left_vector in range(4):
        for right_vector in range(4):
            term = super_multiply(B_E[left_vector], B_E[right_vector])
            result = super_add(
                result,
                super_scale(attach_label(term, f"dd{left_vector}{right_vector}_phi"), HALF),
            )
    for spinor_index in range(2):
        result = super_add(
            result,
            super_scale(attach_label(theta(spinor_index), f"psi{spinor_index + 1}"), SQRT_TWO),
        )
        for vector_index in range(4):
            term = super_multiply(theta(spinor_index), B_E[vector_index])
            result = super_add(
                result,
                super_scale(
                    attach_label(term, f"d{vector_index}_psi{spinor_index + 1}"),
                    SQRT_TWO,
                ),
            )
    result = super_add(result, attach_label(THETA2, "F"))
    return super_normalize(result)


def euclidean_antichiral_superfield() -> SuperExpression:
    result = scalar_label("tildephi")
    for vector_index in range(4):
        result = super_add(
            result,
            super_scale(attach_label(B_E[vector_index], f"d{vector_index}_tildephi"), MINUS_ONE),
        )
    for left_vector in range(4):
        for right_vector in range(4):
            term = super_multiply(B_E[left_vector], B_E[right_vector])
            result = super_add(
                result,
                super_scale(attach_label(term, f"dd{left_vector}{right_vector}_tildephi"), HALF),
            )
    for dotted_index in range(2):
        label, epsilon = upper_dotted_label("tildepsi", dotted_index)
        result = super_add(
            result,
            super_scale(attach_label(bar_theta_lower(dotted_index), label), epsilon * SQRT_TWO),
        )
        for vector_index in range(4):
            derivative_label, derivative_epsilon = upper_dotted_label(
                "tildepsi", dotted_index, vector_index
            )
            term = super_multiply(bar_theta_lower(dotted_index), B_E[vector_index])
            result = super_add(
                result,
                super_scale(
                    attach_label(term, derivative_label),
                    -SQRT_TWO * derivative_epsilon,
                ),
            )
    result = super_add(result, attach_label(BAR_THETA2, "tildeF"))
    return super_normalize(result)


def bridge_exponent_wess_zumino() -> SuperExpression:
    result: SuperExpression = {}
    for mu in range(4):
        result = super_add(result, super_scale(attach_label(B_L[mu], f"A{mu}"), Exact.rational(-2)))
    for dotted_index in range(2):
        label, epsilon = upper_dotted_label("barlambda", dotted_index)
        term = super_multiply(THETA2, bar_theta_lower(dotted_index))
        result = super_add(result, super_scale(attach_label(term, label), TWO * I * epsilon))
    for spinor_index in range(2):
        term = super_multiply(BAR_THETA2, theta(spinor_index))
        result = super_add(
            result,
            super_scale(attach_label(term, f"lambda{spinor_index + 1}"), Exact.rational(-2) * I),
        )
    result = super_add(
        result,
        attach_label(super_multiply(THETA2, BAR_THETA2), "Daux"),
    )
    return super_normalize(result)


def euclidean_bridge_exponent_wess_zumino() -> SuperExpression:
    result: SuperExpression = {}
    for vector_index in range(4):
        result = super_add(
            result,
            super_scale(
                attach_label(B_E[vector_index], f"A{vector_index}"),
                Exact.rational(-2) * I,
            ),
        )
    for dotted_index in range(2):
        label, epsilon = upper_dotted_label("barlambda", dotted_index)
        term = super_multiply(THETA2, bar_theta_lower(dotted_index))
        result = super_add(result, super_scale(attach_label(term, label), TWO * I * epsilon))
    for spinor_index in range(2):
        term = super_multiply(BAR_THETA2, theta(spinor_index))
        result = super_add(
            result,
            super_scale(attach_label(term, f"lambda{spinor_index + 1}"), Exact.rational(-2) * I),
        )
    result = super_add(
        result,
        attach_label(super_multiply(THETA2, BAR_THETA2), "Daux"),
    )
    return super_normalize(result)


def bridge_expansion(exponent: SuperExpression) -> SuperExpression:
    return super_add(
        super_one(),
        super_add(exponent, super_scale(super_multiply(exponent, exponent), HALF)),
    )


def inverse_bridge_expansion(exponent: SuperExpression) -> SuperExpression:
    return super_add(
        super_one(),
        super_add(
            super_scale(exponent, MINUS_ONE),
            super_scale(super_multiply(exponent, exponent), HALF),
        ),
    )


def select_component_labels(
    value: SuperExpression,
    predicate,
) -> SuperExpression:
    return super_normalize(
        {
            mask: {
                monomial: coefficient
                for monomial, coefficient in expression.items()
                if all(predicate(label) for label in monomial)
            }
            for mask, expression in value.items()
        }
    )


def bar_d_lower(dotted_index: int, value: SuperExpression) -> SuperExpression:
    # barD_dot1=-partial/barvartheta_dot2,
    # barD_dot2=+partial/barvartheta_dot1 at x-independent input.
    if dotted_index == 0:
        return super_scale(super_left_derivative(3, value), MINUS_ONE)
    if dotted_index == 1:
        return super_left_derivative(2, value)
    raise IndexError(dotted_index)


def chiral_connection_from_bridge(
    exponent: SuperExpression,
    spinor_index: int,
) -> SuperExpression:
    bridge = bridge_expansion(exponent)
    inverse = inverse_bridge_expansion(exponent)
    return super_multiply(inverse, super_left_derivative(spinor_index, bridge))


def antichiral_connection_from_bridge(
    exponent: SuperExpression,
    dotted_index: int,
) -> SuperExpression:
    bridge = bridge_expansion(exponent)
    inverse = inverse_bridge_expansion(exponent)
    return super_multiply(bridge, bar_d_lower(dotted_index, inverse))


def chiral_strength_from_bridge(
    exponent: SuperExpression,
    spinor_index: int,
) -> SuperExpression:
    connection = chiral_connection_from_bridge(exponent, spinor_index)
    return super_scale(bar_d_squared(connection), Exact.rational(Fraction(-1, 8)))


def antichiral_strength_from_bridge(
    exponent: SuperExpression,
    dotted_index: int,
) -> SuperExpression:
    connection = antichiral_connection_from_bridge(exponent, dotted_index)
    return super_scale(theta_d_squared(connection), Exact.rational(Fraction(1, 8)))


def space_derivative_expression(
    value: FormalExpression,
    vector_index: int,
) -> FormalExpression:
    result: FormalExpression = {}
    for monomial, coefficient in value.items():
        for position, label in enumerate(monomial):
            differentiated = (
                monomial[:position]
                + (f"d{vector_index}_{label}",)
                + monomial[position + 1 :]
            )
            result[differentiated] = result.get(differentiated, ZERO) + coefficient
    return expr_normalize(result)


def space_derivative_super(
    value: SuperExpression,
    vector_index: int,
) -> SuperExpression:
    return super_normalize(
        {
            mask: space_derivative_expression(expression, vector_index)
            for mask, expression in value.items()
        }
    )


def full_d_lower(
    signature: str,
    spinor_index: int,
    value: SuperExpression,
) -> SuperExpression:
    result = super_left_derivative(spinor_index, value)
    sigma = SIGMA_L if signature == "L" else SIGMA_E
    phase = MINUS_I if signature == "L" else ONE
    for vector_index in range(4):
        derivative = space_derivative_super(value, vector_index)
        for dotted_index in range(2):
            term = super_multiply(bar_theta_upper(dotted_index), derivative)
            result = super_add(
                result,
                super_scale(
                    term,
                    phase
                    * sigma[vector_index][spinor_index][dotted_index],
                ),
            )
    return super_normalize(result)


def full_bar_d_lower(
    signature: str,
    dotted_index: int,
    value: SuperExpression,
) -> SuperExpression:
    result = bar_d_lower(dotted_index, value)
    sigma = SIGMA_L if signature == "L" else SIGMA_E
    phase = I if signature == "L" else MINUS_ONE
    for vector_index in range(4):
        derivative = space_derivative_super(value, vector_index)
        for spinor_index in range(2):
            term = super_multiply(theta(spinor_index), derivative)
            result = super_add(
                result,
                super_scale(
                    term,
                    phase
                    * sigma[vector_index][spinor_index][dotted_index],
                ),
            )
    return super_normalize(result)


def full_d_squared(signature: str, value: SuperExpression) -> SuperExpression:
    return super_scale(
        full_d_lower(signature, 1, full_d_lower(signature, 0, value)),
        TWO,
    )


def full_bar_d_squared(signature: str, value: SuperExpression) -> SuperExpression:
    return super_scale(
        full_bar_d_lower(
            signature,
            0,
            full_bar_d_lower(signature, 1, value),
        ),
        TWO,
    )


def full_chiral_connection_from_bridge(
    signature: str,
    exponent: SuperExpression,
    spinor_index: int,
) -> SuperExpression:
    bridge = bridge_expansion(exponent)
    inverse = inverse_bridge_expansion(exponent)
    return super_multiply(
        inverse,
        full_d_lower(signature, spinor_index, bridge),
    )


def full_chiral_strength_from_bridge(
    signature: str,
    exponent: SuperExpression,
    spinor_index: int,
) -> SuperExpression:
    connection = full_chiral_connection_from_bridge(
        signature,
        exponent,
        spinor_index,
    )
    return super_scale(
        full_bar_d_squared(signature, connection),
        Exact.rational(Fraction(-1, 8)),
    )


def serialize_expression(expression: FormalExpression) -> list[dict[str, object]]:
    return [
        {"coefficient": exact_string(coefficient), "ordered_factors": list(monomial)}
        for monomial, coefficient in sorted(expression.items())
    ]


def add_formal_term(
    expression: FormalExpression,
    coefficient: Exact,
    *labels: str,
) -> FormalExpression:
    return expr_add(expression, {tuple(labels): coefficient})


def integrate_by_parts(expression: FormalExpression) -> FormalExpression:
    """Canonicalize the quadratic total derivatives used by the D-term check."""

    result: FormalExpression = {}
    for monomial, coefficient in expression.items():
        if len(monomial) == 2 and monomial[0] == "barphi" and monomial[1].startswith("dd"):
            indices = monomial[1][2:4]
            if len(indices) == 2 and indices[0] == indices[1]:
                mu = indices[0]
                result = add_formal_term(result, -coefficient, f"d{mu}_barphi", f"d{mu}_phi")
                continue
        if len(monomial) == 2 and monomial[0].startswith("dd") and monomial[1] == "phi":
            indices = monomial[0][2:4]
            if len(indices) == 2 and indices[0] == indices[1]:
                mu = indices[0]
                result = add_formal_term(result, -coefficient, f"d{mu}_barphi", f"d{mu}_phi")
                continue
        if (
            len(monomial) == 2
            and monomial[0].startswith("d")
            and "_barpsi" in monomial[0]
            and monomial[1].startswith("psi")
        ):
            derivative, bar_label = monomial[0].split("_", 1)
            mu = derivative[1:]
            result = add_formal_term(result, -coefficient, bar_label, f"d{mu}_{monomial[1]}")
            continue
        result = add_formal_term(result, coefficient, *monomial)
    return expr_normalize(result)


def integrate_by_parts_euclidean(expression: FormalExpression) -> FormalExpression:
    result: FormalExpression = {}
    for monomial, coefficient in expression.items():
        if len(monomial) == 2 and monomial[0] == "tildephi" and monomial[1].startswith("dd"):
            indices = monomial[1][2:4]
            if len(indices) == 2 and indices[0] == indices[1]:
                vector_index = indices[0]
                result = add_formal_term(
                    result,
                    -coefficient,
                    f"d{vector_index}_tildephi",
                    f"d{vector_index}_phi",
                )
                continue
        if len(monomial) == 2 and monomial[0].startswith("dd") and monomial[1] == "phi":
            indices = monomial[0][2:4]
            if len(indices) == 2 and indices[0] == indices[1]:
                vector_index = indices[0]
                result = add_formal_term(
                    result,
                    -coefficient,
                    f"d{vector_index}_tildephi",
                    f"d{vector_index}_phi",
                )
                continue
        if (
            len(monomial) == 2
            and monomial[0].startswith("d")
            and "_tildepsi" in monomial[0]
            and monomial[1].startswith("psi")
        ):
            derivative, tilde_label = monomial[0].split("_", 1)
            vector_index = derivative[1:]
            result = add_formal_term(
                result,
                -coefficient,
                tilde_label,
                f"d{vector_index}_{monomial[1]}",
            )
            continue
        result = add_formal_term(result, coefficient, *monomial)
    return expr_normalize(result)


BAR_SIGMA_L = (
    SIGMA_0,
    tuple(tuple(-entry for entry in row) for row in SIGMA_1),
    tuple(tuple(-entry for entry in row) for row in SIGMA_2),
    tuple(tuple(-entry for entry in row) for row in SIGMA_3),
)


SIGMA_MUNU_L = tuple(
    tuple(
        matrix_scale(
            matrix_subtract(
                matrix_multiply(SIGMA_L[mu], BAR_SIGMA_L[nu]),
                matrix_multiply(SIGMA_L[nu], BAR_SIGMA_L[mu]),
            ),
            Exact.rational(Fraction(1, 4)),
        )
        for nu in range(4)
    )
    for mu in range(4)
)

SIGMA_MN_E = tuple(
    tuple(
        matrix_scale(
            matrix_subtract(
                matrix_multiply(SIGMA_E[left_vector], BAR_SIGMA_E[right_vector]),
                matrix_multiply(SIGMA_E[right_vector], BAR_SIGMA_E[left_vector]),
            ),
            Exact.rational(Fraction(1, 4)),
        )
        for right_vector in range(4)
    )
    for left_vector in range(4)
)


def expected_canonical_matter() -> FormalExpression:
    result: FormalExpression = {}
    result = add_formal_term(result, ONE, "barF", "F")
    result = add_formal_term(result, ONE, "barphi", "Daux", "phi")

    metric = (-1, 1, 1, 1)
    for mu, metric_entry in enumerate(metric):
        g = Exact.rational(metric_entry)
        result = add_formal_term(result, -g, f"d{mu}_barphi", f"d{mu}_phi")
        result = add_formal_term(result, I * g, f"d{mu}_barphi", f"A{mu}", "phi")
        result = add_formal_term(result, -I * g, "barphi", f"A{mu}", f"d{mu}_phi")
        result = add_formal_term(result, -g, "barphi", f"A{mu}", f"A{mu}", "phi")

        for dotted_index in range(2):
            for spinor_index in range(2):
                matrix_entry = BAR_SIGMA_L[mu][dotted_index][spinor_index]
                if matrix_entry.is_zero():
                    continue
                result = add_formal_term(
                    result,
                    I * matrix_entry,
                    f"barpsi{dotted_index + 1}",
                    f"d{mu}_psi{spinor_index + 1}",
                )
                result = add_formal_term(
                    result,
                    matrix_entry,
                    f"barpsi{dotted_index + 1}",
                    f"A{mu}",
                    f"psi{spinor_index + 1}",
                )

    # +i sqrt(2) barphi lambda^a psi_a.
    result = add_formal_term(result, I * SQRT_TWO, "barphi", "lambda2", "psi1")
    result = add_formal_term(result, -I * SQRT_TWO, "barphi", "lambda1", "psi2")
    # -i sqrt(2) barpsi_dot a barlambda^dot a phi.
    result = add_formal_term(result, -I * SQRT_TWO, "barpsi1", "barlambda2", "phi")
    result = add_formal_term(result, I * SQRT_TWO, "barpsi2", "barlambda1", "phi")
    return expr_normalize(result)


def expected_euclidean_matter_density() -> FormalExpression:
    """Direct Wick image of the Lorentzian D-density, before the S_E overall minus."""

    result: FormalExpression = {}
    result = add_formal_term(result, ONE, "tildeF", "F")
    result = add_formal_term(result, ONE, "tildephi", "Daux", "phi")

    for vector_index in range(4):
        result = add_formal_term(
            result,
            MINUS_ONE,
            f"d{vector_index}_tildephi",
            f"d{vector_index}_phi",
        )
        result = add_formal_term(
            result,
            I,
            f"d{vector_index}_tildephi",
            f"A{vector_index}",
            "phi",
        )
        result = add_formal_term(
            result,
            MINUS_I,
            "tildephi",
            f"A{vector_index}",
            f"d{vector_index}_phi",
        )
        result = add_formal_term(
            result,
            MINUS_ONE,
            "tildephi",
            f"A{vector_index}",
            f"A{vector_index}",
            "phi",
        )

        for dotted_index in range(2):
            for spinor_index in range(2):
                matrix_entry = BAR_SIGMA_E[vector_index][dotted_index][spinor_index]
                if matrix_entry.is_zero():
                    continue
                result = add_formal_term(
                    result,
                    -matrix_entry,
                    f"tildepsi{dotted_index + 1}",
                    f"d{vector_index}_psi{spinor_index + 1}",
                )
                result = add_formal_term(
                    result,
                    I * matrix_entry,
                    f"tildepsi{dotted_index + 1}",
                    f"A{vector_index}",
                    f"psi{spinor_index + 1}",
                )

    result = add_formal_term(result, I * SQRT_TWO, "tildephi", "lambda2", "psi1")
    result = add_formal_term(result, -I * SQRT_TWO, "tildephi", "lambda1", "psi2")
    result = add_formal_term(result, -I * SQRT_TWO, "tildepsi1", "barlambda2", "phi")
    result = add_formal_term(result, I * SQRT_TWO, "tildepsi2", "barlambda1", "phi")
    return expr_normalize(result)


def theta_lower(index: int) -> SuperExpression:
    if index == 0:
        return super_scale(theta(1), MINUS_ONE)
    if index == 1:
        return theta(0)
    raise IndexError(index)


def theta_psi(prefix: str) -> SuperExpression:
    result: SuperExpression = {}
    for index in range(2):
        result = super_add(result, attach_label(theta(index), f"{prefix}{index + 1}"))
    return result


def chiral_field_strength(spinor_index: int, color: str = "") -> SuperExpression:
    result = scalar_label(f"lambda{color}{spinor_index + 1}")
    result = super_scale(result, MINUS_I)
    result = super_add(
        result,
        attach_label(theta_lower(spinor_index), f"Daux{color}"),
    )

    # +i sigma_L^{mu nu} theta F_mu nu, with the Einstein sum reduced to mu<nu.
    for mu in range(4):
        for nu in range(mu + 1, 4):
            for raised_spinor in range(2):
                matrix_entry = SIGMA_MUNU_L[mu][nu][spinor_index][raised_spinor]
                if matrix_entry.is_zero():
                    continue
                term = theta_lower(raised_spinor)
                result = super_add(
                    result,
                    super_scale(
                        attach_label(term, f"F{color}{mu}{nu}"),
                        Exact.rational(2) * I * matrix_entry,
                    ),
                )

    # -theta^2 sigma_L^mu D_mu barlambda^dot a.
    for mu in range(4):
        for dotted_index in range(2):
            label, epsilon = upper_dotted_label(
                f"barlambda{color}", dotted_index, mu
            )
            coefficient = -SIGMA_L[mu][spinor_index][dotted_index] * epsilon
            result = super_add(result, super_scale(attach_label(THETA2, label), coefficient))
    return super_normalize(result)


def chiral_field_strength_square(
    left_color: str = "",
    right_color: str | None = None,
) -> FormalExpression:
    if right_color is None:
        right_color = left_color
    lower_left = (
        chiral_field_strength(0, left_color),
        chiral_field_strength(1, left_color),
    )
    lower_right = (
        chiral_field_strength(0, right_color),
        chiral_field_strength(1, right_color),
    )
    upper_left = (
        lower_left[1],
        super_scale(lower_left[0], MINUS_ONE),
    )
    product: SuperExpression = {}
    for index in range(2):
        product = super_add(
            product,
            super_multiply(upper_left[index], lower_right[index]),
        )
    # theta^2=-2 theta^1 theta^2.
    return expr_scale(product.get(0b0011, {}), Exact.rational(Fraction(-1, 2)))


def euclidean_chiral_field_strength(
    spinor_index: int,
    color: str = "",
) -> SuperExpression:
    result = super_scale(
        scalar_label(f"lambda{color}{spinor_index + 1}"),
        MINUS_I,
    )
    result = super_add(
        result,
        attach_label(theta_lower(spinor_index), f"Daux{color}"),
    )

    # -i sigma_E^{mn} theta F_mn, with the Einstein sum reduced to m<n.
    for left_vector in range(4):
        for right_vector in range(left_vector + 1, 4):
            for raised_spinor in range(2):
                matrix_entry = SIGMA_MN_E[left_vector][right_vector][spinor_index][raised_spinor]
                if matrix_entry.is_zero():
                    continue
                result = super_add(
                    result,
                    super_scale(
                        attach_label(
                            theta_lower(raised_spinor),
                            f"FE{color}{left_vector}{right_vector}",
                        ),
                        Exact.rational(-2) * I * matrix_entry,
                    ),
                )

    # -i theta^2 sigma_E^m D_m barlambda^dot a.
    for vector_index in range(4):
        for dotted_index in range(2):
            label, epsilon = upper_dotted_label(
                f"barlambda{color}", dotted_index, vector_index
            )
            coefficient = -I * SIGMA_E[vector_index][spinor_index][dotted_index] * epsilon
            result = super_add(result, super_scale(attach_label(THETA2, label), coefficient))
    return super_normalize(result)


def euclidean_chiral_field_strength_square(
    left_color: str = "",
    right_color: str | None = None,
) -> FormalExpression:
    if right_color is None:
        right_color = left_color
    lower_left = (
        euclidean_chiral_field_strength(0, left_color),
        euclidean_chiral_field_strength(1, left_color),
    )
    lower_right = (
        euclidean_chiral_field_strength(0, right_color),
        euclidean_chiral_field_strength(1, right_color),
    )
    upper_left = (
        lower_left[1],
        super_scale(lower_left[0], MINUS_ONE),
    )
    product: SuperExpression = {}
    for index in range(2):
        product = super_add(
            product,
            super_multiply(upper_left[index], lower_right[index]),
        )
    return expr_scale(product.get(0b0011, {}), Exact.rational(Fraction(-1, 2)))


def canonicalize_gauge_expression(expression: FormalExpression) -> FormalExpression:
    result: FormalExpression = {}
    for monomial, coefficient in expression.items():
        factors = list(monomial)
        if len(factors) == 2 and factors[0].startswith("F") and factors[1].startswith("F"):
            factors.sort()
        if (
            len(factors) == 2
            and "barlambda" in factors[0]
            and factors[1].startswith("lambda")
        ):
            factors = [factors[1], factors[0]]
            coefficient = -coefficient
        result = add_formal_term(result, coefficient, *factors)
    return expr_normalize(result)


def epsilon_four(indices: tuple[int, int, int, int]) -> int:
    if len(set(indices)) != 4:
        return 0
    inversions = sum(
        1
        for left in range(4)
        for right in range(left + 1, 4)
        if indices[left] > indices[right]
    )
    return -1 if inversions % 2 else 1


def field_strength_label(mu: int, nu: int) -> tuple[str, int]:
    if mu < nu:
        return f"F{mu}{nu}", 1
    if nu < mu:
        return f"F{nu}{mu}", -1
    raise ValueError((mu, nu))


def expected_field_strength_square(
    left_color: str = "",
    right_color: str | None = None,
) -> FormalExpression:
    if right_color is None:
        right_color = left_color
    result: FormalExpression = {}
    metric = (-1, 1, 1, 1)
    result = add_formal_term(
        result,
        ONE,
        f"Daux{left_color}",
        f"Daux{right_color}",
    )

    # -1/2 F_mu_nu F^mu_nu = -sum_(mu<nu) eta_mu eta_nu F_mu_nu^2.
    for mu in range(4):
        for nu in range(mu + 1, 4):
            result = add_formal_term(
                result,
                Exact.rational(-metric[mu] * metric[nu]),
                f"F{left_color}{mu}{nu}",
                f"F{right_color}{mu}{nu}",
            )

    # +(i/4) epsilon^(mu nu rho sigma) F_mu_nu F_rho_sigma.
    quarter_i = I * Exact.rational(Fraction(1, 4))
    for mu in range(4):
        for nu in range(4):
            if mu == nu:
                continue
            first_uncolored, first_sign = field_strength_label(mu, nu)
            first = f"F{left_color}{first_uncolored[1:]}"
            for rho in range(4):
                for sigma in range(4):
                    if rho == sigma:
                        continue
                    epsilon = epsilon_four((mu, nu, rho, sigma))
                    if epsilon == 0:
                        continue
                    second_uncolored, second_sign = field_strength_label(rho, sigma)
                    second = f"F{right_color}{second_uncolored[1:]}"
                    labels = tuple(sorted((first, second)))
                    coefficient = quarter_i * Exact.rational(epsilon * first_sign * second_sign)
                    result = add_formal_term(result, coefficient, *labels)

    # +i lambda_A sigma D barlambda_B +i lambda_B sigma D barlambda_A.
    for lambda_color, barlambda_color in (
        (left_color, right_color),
        (right_color, left_color),
    ):
        for raised_spinor in range(2):
            lower_lambda = 1 - raised_spinor
            lambda_epsilon = ONE if raised_spinor == 0 else MINUS_ONE
            for mu in range(4):
                for dotted_index in range(2):
                    bar_label, bar_epsilon = upper_dotted_label(
                        f"barlambda{barlambda_color}",
                        dotted_index,
                        mu,
                    )
                    coefficient = (
                        I
                        * lambda_epsilon
                        * SIGMA_L[mu][raised_spinor][dotted_index]
                        * bar_epsilon
                    )
                    if coefficient.is_zero():
                        continue
                    result = add_formal_term(
                        result,
                        coefficient,
                        f"lambda{lambda_color}{lower_lambda + 1}",
                        bar_label,
                    )
    return expr_normalize(result)


def epsilon_euclidean(indices: tuple[int, int, int, int]) -> int:
    # Stored vector order is (1,2,3,4); epsilon_E^(1 2 3 4)=+1.
    return epsilon_four(indices)


def euclidean_field_strength_label(left_vector: int, right_vector: int) -> tuple[str, int]:
    if left_vector < right_vector:
        return f"FE{left_vector}{right_vector}", 1
    if right_vector < left_vector:
        return f"FE{right_vector}{left_vector}", -1
    raise ValueError((left_vector, right_vector))


def expected_euclidean_field_strength_square(
    left_color: str = "",
    right_color: str | None = None,
) -> FormalExpression:
    if right_color is None:
        right_color = left_color
    result: FormalExpression = {}
    result = add_formal_term(
        result,
        ONE,
        f"Daux{left_color}",
        f"Daux{right_color}",
    )
    for left_vector in range(4):
        for right_vector in range(left_vector + 1, 4):
            result = add_formal_term(
                result,
                MINUS_ONE,
                f"FE{left_color}{left_vector}{right_vector}",
                f"FE{right_color}{left_vector}{right_vector}",
            )

    # +(1/4) epsilon_E^(mnrs) F_mn F_rs, epsilon_E^(1 2 3 4)=+1.
    quarter = Exact.rational(Fraction(1, 4))
    for left_vector in range(4):
        for right_vector in range(4):
            if left_vector == right_vector:
                continue
            first_uncolored, first_sign = euclidean_field_strength_label(
                left_vector, right_vector
            )
            first = f"FE{left_color}{first_uncolored[2:]}"
            for third_vector in range(4):
                for fourth_vector in range(4):
                    if third_vector == fourth_vector:
                        continue
                    epsilon = epsilon_euclidean(
                        (left_vector, right_vector, third_vector, fourth_vector)
                    )
                    if epsilon == 0:
                        continue
                    second_uncolored, second_sign = euclidean_field_strength_label(
                        third_vector, fourth_vector
                    )
                    second = f"FE{right_color}{second_uncolored[2:]}"
                    labels = tuple(sorted((first, second)))
                    result = add_formal_term(
                        result,
                        quarter * Exact.rational(epsilon * first_sign * second_sign),
                        *labels,
                    )

    # -lambda_A sigma_E D barlambda_B -lambda_B sigma_E D barlambda_A.
    for lambda_color, barlambda_color in (
        (left_color, right_color),
        (right_color, left_color),
    ):
        for raised_spinor in range(2):
            lower_lambda = 1 - raised_spinor
            lambda_epsilon = ONE if raised_spinor == 0 else MINUS_ONE
            for vector_index in range(4):
                for dotted_index in range(2):
                    bar_label, bar_epsilon = upper_dotted_label(
                        f"barlambda{barlambda_color}",
                        dotted_index,
                        vector_index,
                    )
                    coefficient = (
                        MINUS_ONE
                        * lambda_epsilon
                        * SIGMA_E[vector_index][raised_spinor][dotted_index]
                        * bar_epsilon
                    )
                    if coefficient.is_zero():
                        continue
                    result = add_formal_term(
                        result,
                        coefficient,
                        f"lambda{lambda_color}{lower_lambda + 1}",
                        bar_label,
                    )
    return expr_normalize(result)


def check_bilinears() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    metric = (-1, 1, 1, 1)
    for mu in range(4):
        for nu in range(4):
            value = super_multiply(B_L[mu], B_L[nu])
            expected = (
                super_scale(TOP, Exact.rational(Fraction(-metric[mu], 2)))
                if mu == nu
                else {}
            )
            if value != expected:
                failures.append(
                    {
                        "identity": f"B^{mu} B^{nu}=-1/2 eta^({mu}{nu}) theta^2 bartheta^2",
                        "actual": serialize_expression(value.get(15, {})),
                        "expected": serialize_expression(expected.get(15, {})),
                    }
                )
    return failures


def check_euclidean_bilinears() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    for left_vector in range(4):
        for right_vector in range(4):
            value = super_multiply(B_E[left_vector], B_E[right_vector])
            expected = super_scale(TOP, HALF) if left_vector == right_vector else {}
            if value != expected:
                failures.append(
                    {
                        "identity": (
                            f"B_E^{left_vector + 1} B_E^{right_vector + 1}="
                            "+1/2 delta theta^2 bartheta^2"
                        ),
                        "actual": serialize_expression(value.get(15, {})),
                        "expected": serialize_expression(expected.get(15, {})),
                    }
                )
    return failures


def check_measures() -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    checks = (
        ("-1/4 D^2 theta^2=1", super_scale(theta_d_squared(THETA2), Exact.rational(Fraction(-1, 4)))),
        (
            "-1/4 barD^2 bartheta^2=1",
            super_scale(bar_d_squared(BAR_THETA2), Exact.rational(Fraction(-1, 4))),
        ),
        (
            "+1/16 D^2 barD^2(theta^2 bartheta^2)=1",
            super_scale(theta_d_squared(bar_d_squared(TOP)), Exact.rational(Fraction(1, 16))),
        ),
    )
    for identity, value in checks:
        if value != super_one():
            failures.append(
                {
                    "identity": identity,
                    "actual": serialize_expression(value.get(0, {})),
                    "expected": serialize_expression(super_one()[0]),
                }
            )
    return failures


def formal_from_terms(terms: list[tuple[Exact, str]]) -> FormalExpression:
    result: FormalExpression = {}
    for coefficient, label in terms:
        if not coefficient.is_zero():
            result = add_formal_term(result, coefficient, label)
    return expr_normalize(result)


def check_bridge_projection_chain() -> tuple[
    list[dict[str, object]],
    dict[str, object],
    int,
    int,
]:
    failures: list[dict[str, object]] = []
    results: dict[str, object] = {}
    identities = 0
    coefficients = 0

    exponents = {
        "L": bridge_exponent_wess_zumino(),
        "E": euclidean_bridge_exponent_wess_zumino(),
    }
    sigmas = {"L": SIGMA_L, "E": SIGMA_E}
    barsigmas = {"L": BAR_SIGMA_L, "E": BAR_SIGMA_E}

    for signature in ("L", "E"):
        exponent = exponents[signature]
        vector_exponent = select_component_labels(
            exponent, lambda label: label.startswith("A")
        )
        connections = tuple(
            chiral_connection_from_bridge(vector_exponent, spinor_index)
            for spinor_index in range(2)
        )

        connection_rows: dict[str, object] = {}
        for spinor_index in range(2):
            for dotted_index in range(2):
                actual = bar_d_lower(dotted_index, connections[spinor_index]).get(0, {})
                phase = TWO if signature == "L" else TWO * I
                expected = formal_from_terms(
                    [
                        (
                            phase
                            * sigmas[signature][vector_index][spinor_index][dotted_index],
                            f"A{vector_index}",
                        )
                        for vector_index in range(4)
                    ]
                )
                identity = (
                    f"{signature}: barD_dot{dotted_index + 1} Gamma_{spinor_index + 1}| "
                    f"equals normalized sigma.A"
                )
                identities += 1
                coefficients += len(expected)
                connection_rows[f"{spinor_index + 1}{dotted_index + 1}"] = {
                    "actual": serialize_expression(actual),
                    "expected": serialize_expression(expected),
                }
                if actual != expected:
                    failures.append(
                        {
                            "identity": identity,
                            "actual": serialize_expression(actual),
                            "expected": serialize_expression(expected),
                        }
                    )
        results[f"{signature}_connection_A_projection"] = connection_rows

        vector_rows: dict[str, object] = {}
        metric = (-1, 1, 1, 1)
        for output_vector in range(4):
            reconstructed: SuperExpression = {}
            for spinor_index in range(2):
                for dotted_index in range(2):
                    first = super_left_derivative(
                        spinor_index,
                        bar_d_lower(dotted_index, vector_exponent),
                    )
                    second = bar_d_lower(
                        dotted_index,
                        super_left_derivative(spinor_index, vector_exponent),
                    )
                    ordinary_commutator = super_add(first, super_scale(second, MINUS_ONE))
                    barsigma = barsigmas[signature][output_vector][dotted_index][spinor_index]
                    if signature == "L":
                        barsigma = Exact.rational(metric[output_vector]) * barsigma
                    reconstructed = super_add(
                        reconstructed,
                        super_scale(ordinary_commutator, barsigma),
                    )
            projector = Exact.rational(Fraction(1, 8))
            if signature == "E":
                projector = I * projector
            actual = super_scale(reconstructed, projector).get(0, {})
            expected = formal_from_terms([(ONE, f"A{output_vector}")])
            identity = f"{signature}: ordinary-commutator vector projection A{output_vector}"
            identities += 1
            coefficients += 1
            vector_rows[str(output_vector)] = {
                "actual": serialize_expression(actual),
                "expected": serialize_expression(expected),
            }
            if actual != expected:
                failures.append(
                    {
                        "identity": identity,
                        "actual": serialize_expression(actual),
                        "expected": serialize_expression(expected),
                    }
                )
        results[f"{signature}_vector_projection"] = vector_rows

        lambda_exponent = select_component_labels(
            exponent, lambda label: label.startswith("lambda")
        )
        barlambda_exponent = select_component_labels(
            exponent, lambda label: label.startswith("barlambda")
        )
        auxiliary_exponent = select_component_labels(
            exponent, lambda label: label == "Daux"
        )

        lambda_rows: dict[str, object] = {}
        barlambda_rows: dict[str, object] = {}
        chiral_strengths = tuple(
            chiral_strength_from_bridge(lambda_exponent, spinor_index)
            for spinor_index in range(2)
        )
        antichiral_strengths = tuple(
            antichiral_strength_from_bridge(barlambda_exponent, dotted_index)
            for dotted_index in range(2)
        )
        for spinor_index, strength in enumerate(chiral_strengths):
            actual = expr_scale(strength.get(0, {}), I)
            expected = formal_from_terms(
                [(ONE, f"lambda{spinor_index + 1}")]
            )
            identities += 1
            coefficients += 1
            lambda_rows[str(spinor_index + 1)] = {
                "actual": serialize_expression(actual),
                "expected": serialize_expression(expected),
            }
            if actual != expected:
                failures.append(
                    {
                        "identity": f"{signature}: i W_{spinor_index + 1}|=lambda",
                        "actual": serialize_expression(actual),
                        "expected": serialize_expression(expected),
                    }
                )
        for dotted_index, strength in enumerate(antichiral_strengths):
            actual = expr_scale(strength.get(0, {}), MINUS_I)
            expected = formal_from_terms(
                [(ONE, f"barlambda{dotted_index + 1}")]
            )
            identities += 1
            coefficients += 1
            barlambda_rows[str(dotted_index + 1)] = {
                "actual": serialize_expression(actual),
                "expected": serialize_expression(expected),
            }
            if actual != expected:
                failures.append(
                    {
                        "identity": (
                            f"{signature}: -i tildeW_dot{dotted_index + 1}|=barlambda"
                        ),
                        "actual": serialize_expression(actual),
                        "expected": serialize_expression(expected),
                    }
                )
        results[f"{signature}_lambda_projection"] = lambda_rows
        results[f"{signature}_barlambda_projection"] = barlambda_rows

        auxiliary_chiral = tuple(
            chiral_strength_from_bridge(auxiliary_exponent, spinor_index)
            for spinor_index in range(2)
        )
        d_contraction = super_add(
            super_left_derivative(1, auxiliary_chiral[0]),
            super_scale(
                super_left_derivative(0, auxiliary_chiral[1]),
                MINUS_ONE,
            ),
        )
        actual_d = super_scale(d_contraction, -HALF).get(0, {})
        expected_d = formal_from_terms([(ONE, "Daux")])
        identities += 1
        coefficients += 1
        if actual_d != expected_d:
            failures.append(
                {
                    "identity": f"{signature}: -1/2 D^a W_a|=Daux",
                    "actual": serialize_expression(actual_d),
                    "expected": serialize_expression(expected_d),
                }
            )

        auxiliary_antichiral = tuple(
            antichiral_strength_from_bridge(auxiliary_exponent, dotted_index)
            for dotted_index in range(2)
        )
        bard_contraction = super_add(
            super_left_derivative(2, auxiliary_antichiral[0]),
            super_left_derivative(3, auxiliary_antichiral[1]),
        )
        actual_bard = super_scale(bard_contraction, HALF).get(0, {})
        identities += 1
        coefficients += 1
        if actual_bard != expected_d:
            failures.append(
                {
                    "identity": f"{signature}: +1/2 barD^dot a tildeW_dot a|=Daux",
                    "actual": serialize_expression(actual_bard),
                    "expected": serialize_expression(expected_d),
                }
            )
        results[f"{signature}_auxiliary_projections"] = {
            "chiral": serialize_expression(actual_d),
            "antichiral": serialize_expression(actual_bard),
            "expected": serialize_expression(expected_d),
        }

        full_algebraic_exponent = select_component_labels(
            exponent,
            lambda label: (
                label.startswith("lambda")
                or label.startswith("barlambda")
                or label == "Daux"
            ),
        )
        chirality_rows: dict[str, object] = {}
        for spinor_index in range(2):
            strength = chiral_strength_from_bridge(
                full_algebraic_exponent, spinor_index
            )
            for dotted_index in range(2):
                actual = bar_d_lower(dotted_index, strength)
                identities += 1
                chirality_rows[f"{spinor_index + 1}{dotted_index + 1}"] = {
                    "actual": serialize_expression(actual.get(0, {})),
                    "expected": [],
                }
                if actual:
                    failures.append(
                        {
                            "identity": (
                                f"{signature}: barD_dot{dotted_index + 1} "
                                f"W_{spinor_index + 1}=0"
                            ),
                            "actual": {
                                str(mask): serialize_expression(expression)
                                for mask, expression in actual.items()
                            },
                            "expected": {},
                        }
                    )
        results[f"{signature}_chiral_strength_chirality"] = chirality_rows

    return failures, results, identities, coefficients


EPSILON_LOWER = (
    (ZERO, MINUS_ONE),
    (ONE, ZERO),
)


def lower_second_spinor_index(
    matrix: tuple[tuple[Exact, Exact], tuple[Exact, Exact]],
    first_index: int,
    second_index: int,
) -> Exact:
    return (
        matrix[first_index][0] * EPSILON_LOWER[0][second_index]
        + matrix[first_index][1] * EPSILON_LOWER[1][second_index]
    )


def formal_curvature(
    left_vector: int,
    right_vector: int,
) -> FormalExpression:
    result: FormalExpression = {}
    result = add_formal_term(
        result,
        ONE,
        f"d{left_vector}_A{right_vector}",
    )
    result = add_formal_term(
        result,
        MINUS_ONE,
        f"d{right_vector}_A{left_vector}",
    )
    result = add_formal_term(
        result,
        MINUS_I,
        f"A{left_vector}",
        f"A{right_vector}",
    )
    result = add_formal_term(
        result,
        I,
        f"A{right_vector}",
        f"A{left_vector}",
    )
    return expr_normalize(result)


def check_curvature_projection_chain() -> tuple[
    list[dict[str, object]],
    dict[str, object],
    int,
    int,
]:
    failures: list[dict[str, object]] = []
    results: dict[str, object] = {}
    identities = 0
    coefficients = 0

    for signature, exponent, sigma_mn in (
        (
            "L",
            bridge_exponent_wess_zumino(),
            SIGMA_MUNU_L,
        ),
        (
            "E",
            euclidean_bridge_exponent_wess_zumino(),
            SIGMA_MN_E,
        ),
    ):
        vector_exponent = select_component_labels(
            exponent,
            lambda label: label.startswith("A"),
        )
        strengths = tuple(
            full_chiral_strength_from_bridge(
                signature,
                vector_exponent,
                spinor_index,
            )
            for spinor_index in range(2)
        )
        signature_rows: dict[str, object] = {}
        for first_spinor in range(2):
            for second_spinor in range(first_spinor, 2):
                first_term = full_d_lower(
                    signature,
                    first_spinor,
                    strengths[second_spinor],
                )
                second_term = full_d_lower(
                    signature,
                    second_spinor,
                    strengths[first_spinor],
                )
                actual = super_scale(
                    super_add(first_term, second_term),
                    HALF,
                ).get(0, {})

                expected: FormalExpression = {}
                phase = TWO * I if signature == "L" else Exact.rational(-2) * I
                for left_vector in range(4):
                    for right_vector in range(left_vector + 1, 4):
                        sigma_lower = lower_second_spinor_index(
                            sigma_mn[left_vector][right_vector],
                            first_spinor,
                            second_spinor,
                        )
                        expected = expr_add(
                            expected,
                            expr_scale(
                                formal_curvature(left_vector, right_vector),
                                phase * sigma_lower,
                            ),
                        )
                expected = expr_normalize(expected)
                identities += 1
                coefficients += len(expected)
                key = f"{first_spinor + 1}{second_spinor + 1}"
                signature_rows[key] = {
                    "actual": serialize_expression(actual),
                    "expected": serialize_expression(expected),
                }
                if actual != expected:
                    failures.append(
                        {
                            "identity": (
                                f"{signature}: D_({first_spinor + 1} "
                                f"W_{second_spinor + 1})| exact nonabelian curvature"
                            ),
                            "actual": serialize_expression(actual),
                            "expected": serialize_expression(expected),
                        }
                    )
        results[signature] = signature_rows
    return failures, results, identities, coefficients


def check_gaugino_tail_projection() -> tuple[
    list[dict[str, object]],
    dict[str, object],
    int,
    int,
]:
    failures: list[dict[str, object]] = []
    results: dict[str, object] = {}
    identities = 0
    coefficients = 0

    for signature, exponent, sigma in (
        ("L", bridge_exponent_wess_zumino(), SIGMA_L),
        ("E", euclidean_bridge_exponent_wess_zumino(), SIGMA_E),
    ):
        selected_exponent = select_component_labels(
            exponent,
            lambda label: (
                label.startswith("A")
                or label.startswith("barlambda")
            ),
        )
        phase = MINUS_ONE if signature == "L" else MINUS_I
        signature_rows: dict[str, object] = {}
        for spinor_index in range(2):
            strength = full_chiral_strength_from_bridge(
                signature,
                selected_exponent,
                spinor_index,
            )
            actual = expr_scale(strength.get(0b0011, {}), -HALF)
            expected: FormalExpression = {}
            for vector_index in range(4):
                for dotted_index in range(2):
                    bar_label, epsilon = upper_dotted_label(
                        "barlambda",
                        dotted_index,
                    )
                    sigma_entry = sigma[vector_index][spinor_index][dotted_index]
                    coefficient = phase * sigma_entry * epsilon
                    expected = add_formal_term(
                        expected,
                        coefficient,
                        f"d{vector_index}_{bar_label}",
                    )
                    expected = add_formal_term(
                        expected,
                        coefficient * MINUS_I,
                        f"A{vector_index}",
                        bar_label,
                    )
                    expected = add_formal_term(
                        expected,
                        coefficient * I,
                        bar_label,
                        f"A{vector_index}",
                    )
            expected = expr_normalize(expected)
            identities += 1
            coefficients += len(expected)
            signature_rows[str(spinor_index + 1)] = {
                "actual": serialize_expression(actual),
                "expected": serialize_expression(expected),
            }
            if actual != expected:
                failures.append(
                    {
                        "identity": (
                            f"{signature}: theta2 W_{spinor_index + 1} "
                            "equals the adjoint covariant gaugino derivative"
                        ),
                        "actual": serialize_expression(actual),
                        "expected": serialize_expression(expected),
                    }
                )
        results[signature] = signature_rows
    return failures, results, identities, coefficients


def check_superpotential_product() -> tuple[list[dict[str, object]], FormalExpression]:
    product = super_multiply(theta_psi("psiI"), theta_psi("psiJ"))
    actual = expr_scale(product.get(0b0011, {}), Exact.rational(Fraction(-1, 2)))
    expected: FormalExpression = {}
    expected = add_formal_term(expected, HALF, "psiI1", "psiJ2")
    expected = add_formal_term(expected, -HALF, "psiI2", "psiJ1")
    failures: list[dict[str, object]] = []
    if actual != expected:
        failures.append(
            {
                "identity": "(vartheta psi^I)(vartheta psi^J)=-1/2 vartheta^2 psi^I psi^J",
                "actual": serialize_expression(actual),
                "expected": serialize_expression(expected),
            }
        )
    return failures, actual


def build_audit() -> dict[str, object]:
    phi = chiral_superfield()
    bar_phi = antichiral_superfield()
    exponent = bridge_exponent_wess_zumino()
    bridge = bridge_expansion(exponent)
    canonical = super_multiply(super_multiply(bar_phi, bridge), phi)
    measure_failures = check_measures()
    lorentz_bilinear_failures = check_bilinears()
    euclidean_bilinear_failures = check_euclidean_bilinears()
    (
        bridge_projection_failures,
        bridge_projection_results,
        bridge_projection_identities,
        bridge_projection_coefficients,
    ) = check_bridge_projection_chain()
    (
        curvature_projection_failures,
        curvature_projection_results,
        curvature_projection_identities,
        curvature_projection_coefficients,
    ) = check_curvature_projection_chain()
    (
        gaugino_tail_failures,
        gaugino_tail_results,
        gaugino_tail_identities,
        gaugino_tail_coefficients,
    ) = check_gaugino_tail_projection()
    projection_chain_identities = (
        bridge_projection_identities
        + curvature_projection_identities
        + gaugino_tail_identities
    )
    projection_chain_coefficients = (
        bridge_projection_coefficients
        + curvature_projection_coefficients
        + gaugino_tail_coefficients
    )
    failures = (
        measure_failures
        + lorentz_bilinear_failures
        + euclidean_bilinear_failures
        + bridge_projection_failures
        + curvature_projection_failures
        + gaugino_tail_failures
    )
    top_component = expr_scale(canonical.get(15, {}), Exact.rational(Fraction(-1, 4)))
    integrated_component = integrate_by_parts(top_component)
    expected_component = expected_canonical_matter()
    if integrated_component != expected_component:
        failures.append(
            {
                "identity": "integral d4theta barPhi exp(V) Phi equals the canonical gauge-covariant matter action",
                "actual": serialize_expression(integrated_component),
                "expected": serialize_expression(expected_component),
            }
        )

    euclidean_phi = euclidean_chiral_superfield()
    euclidean_tilde_phi = euclidean_antichiral_superfield()
    euclidean_bridge = bridge_expansion(euclidean_bridge_exponent_wess_zumino())
    euclidean_canonical = super_multiply(
        super_multiply(euclidean_tilde_phi, euclidean_bridge), euclidean_phi
    )
    euclidean_top = expr_scale(
        euclidean_canonical.get(15, {}), Exact.rational(Fraction(-1, 4))
    )
    euclidean_integrated = integrate_by_parts_euclidean(euclidean_top)
    euclidean_expected = expected_euclidean_matter_density()
    if euclidean_integrated != euclidean_expected:
        failures.append(
            {
                "identity": (
                    "Euclidean direct-Wick D-density equals the canonical gauge-covariant "
                    "matter density before the S_E overall minus"
                ),
                "actual": serialize_expression(euclidean_integrated),
                "expected": serialize_expression(euclidean_expected),
            }
        )

    superpotential_failures, superpotential_product = check_superpotential_product()
    failures.extend(superpotential_failures)

    gauge_square = canonicalize_gauge_expression(chiral_field_strength_square())
    expected_gauge_square = canonicalize_gauge_expression(expected_field_strength_square())
    if gauge_square != expected_gauge_square:
        failures.append(
            {
                "identity": "[W^a W_a]_theta2 exact gauge kinetic component",
                "actual": serialize_expression(gauge_square),
                "expected": serialize_expression(expected_gauge_square),
            }
        )

    euclidean_gauge_square = canonicalize_gauge_expression(
        euclidean_chiral_field_strength_square()
    )
    expected_euclidean_gauge_square = canonicalize_gauge_expression(
        expected_euclidean_field_strength_square()
    )
    if euclidean_gauge_square != expected_euclidean_gauge_square:
        failures.append(
            {
                "identity": "[W_E^a W_Ea]_theta2 exact Euclidean gauge kinetic component",
                "actual": serialize_expression(euclidean_gauge_square),
                "expected": serialize_expression(expected_euclidean_gauge_square),
            }
        )

    cross_gauge_square = canonicalize_gauge_expression(
        chiral_field_strength_square("A", "B")
    )
    expected_cross_gauge_square = canonicalize_gauge_expression(
        expected_field_strength_square("A", "B")
    )
    if cross_gauge_square != expected_cross_gauge_square:
        failures.append(
            {
                "identity": "[W_A^a W_Ba]_theta2 exact cross-color Lorentz component",
                "actual": serialize_expression(cross_gauge_square),
                "expected": serialize_expression(expected_cross_gauge_square),
            }
        )

    euclidean_cross_gauge_square = canonicalize_gauge_expression(
        euclidean_chiral_field_strength_square("A", "B")
    )
    expected_euclidean_cross_gauge_square = canonicalize_gauge_expression(
        expected_euclidean_field_strength_square("A", "B")
    )
    if euclidean_cross_gauge_square != expected_euclidean_cross_gauge_square:
        failures.append(
            {
                "identity": "[W_EA^a W_EBa]_theta2 exact cross-color Euclidean component",
                "actual": serialize_expression(euclidean_cross_gauge_square),
                "expected": serialize_expression(
                    expected_euclidean_cross_gauge_square
                ),
            }
        )
    return {
        "task_id": "CONTRACT-STEP-03A-GAUGE-CHIRAL-ACTION-001",
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
        "projection_checks": {
            "theta_squared": "-2 vartheta^1 vartheta^2",
            "bartheta_squared": "+2 barvartheta_dot1 barvartheta_dot2",
            "theta2_bartheta2_top_coefficient": exact_string(TOP[15][()]),
            "lorentz_bilinear_identities": 16,
            "euclidean_bilinear_identities": 16,
            "measure_failures": len(measure_failures),
            "lorentz_bilinear_failures": len(lorentz_bilinear_failures),
            "euclidean_bilinear_failures": len(euclidean_bilinear_failures),
            "bridge_projection_identities": bridge_projection_identities,
            "curvature_projection_identities": curvature_projection_identities,
            "gaugino_tail_identities": gaugino_tail_identities,
            "projection_chain_coefficients": projection_chain_coefficients,
            "projection_chain_failures": (
                len(bridge_projection_failures)
                + len(curvature_projection_failures)
                + len(gaugino_tail_failures)
            ),
        },
        "totals": {
            "exact_identities": 42 + projection_chain_identities,
            "exact_component_coefficients": (
                len(integrated_component)
                + len(euclidean_integrated)
                + len(superpotential_product)
                + len(gauge_square)
                + len(euclidean_gauge_square)
                + len(cross_gauge_square)
                + len(euclidean_cross_gauge_square)
                + projection_chain_coefficients
            ),
            "failed_checks": len(failures),
        },
        "bridge_projection_chain": {
            "algebraic_components": bridge_projection_results,
            "nonabelian_curvature": curvature_projection_results,
            "covariant_gaugino_tail": gaugino_tail_results,
        },
        "canonical_matter_top_component": serialize_expression(top_component),
        "canonical_matter_after_integration_by_parts": serialize_expression(integrated_component),
        "canonical_matter_expected": serialize_expression(expected_component),
        "euclidean_matter_top_component": serialize_expression(euclidean_top),
        "euclidean_matter_after_integration_by_parts": serialize_expression(euclidean_integrated),
        "euclidean_matter_expected": serialize_expression(euclidean_expected),
        "superpotential_fermion_product": serialize_expression(superpotential_product),
        "gauge_field_strength_square": serialize_expression(gauge_square),
        "gauge_field_strength_square_expected": serialize_expression(expected_gauge_square),
        "euclidean_gauge_field_strength_square": serialize_expression(euclidean_gauge_square),
        "euclidean_gauge_field_strength_square_expected": serialize_expression(
            expected_euclidean_gauge_square
        ),
        "cross_color_gauge_field_strength_square": serialize_expression(
            cross_gauge_square
        ),
        "cross_color_gauge_field_strength_square_expected": serialize_expression(
            expected_cross_gauge_square
        ),
        "euclidean_cross_color_gauge_field_strength_square": serialize_expression(
            euclidean_cross_gauge_square
        ),
        "euclidean_cross_color_gauge_field_strength_square_expected": serialize_expression(
            expected_euclidean_cross_gauge_square
        ),
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", action="store_true")
    args = parser.parse_args()
    audit = build_audit()
    if args.dump:
        print(json.dumps(audit["canonical_matter_top_component"], indent=2))
        return
    AUDIT_PATH.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
