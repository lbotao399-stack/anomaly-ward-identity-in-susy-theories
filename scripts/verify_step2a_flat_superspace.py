#!/usr/bin/env python3
"""Exact Step-2A flat-superspace operator verification.

The coefficient ring is Z[i][k_0,k_1,k_2,k_3].  The odd algebra is the
four-generator exterior algebra ordered as

    vartheta^1 < vartheta^2 < barvartheta_dot1 < barvartheta_dot2.

No floating-point or computer-algebra dependency is used.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Callable, Iterable


N_BOSONIC = 4
N_GRASSMANN = 4
Exponent = tuple[int, int, int, int]


@dataclass(frozen=True)
class GaussianInteger:
    real: int = 0
    imag: int = 0

    def __add__(self, other: "GaussianInteger") -> "GaussianInteger":
        return GaussianInteger(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "GaussianInteger":
        return GaussianInteger(-self.real, -self.imag)

    def __sub__(self, other: "GaussianInteger") -> "GaussianInteger":
        return self + (-other)

    def __mul__(self, other: "GaussianInteger") -> "GaussianInteger":
        return GaussianInteger(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def is_zero(self) -> bool:
        return self.real == 0 and self.imag == 0

    def conjugate(self) -> "GaussianInteger":
        return GaussianInteger(self.real, -self.imag)


ZERO = GaussianInteger()
ONE = GaussianInteger(1, 0)
MINUS_ONE = GaussianInteger(-1, 0)
I = GaussianInteger(0, 1)
MINUS_I = GaussianInteger(0, -1)
TWO = GaussianInteger(2, 0)
MINUS_TWO = GaussianInteger(-2, 0)
ZERO_EXPONENT: Exponent = (0, 0, 0, 0)

Polynomial = dict[Exponent, GaussianInteger]
SuperPolynomial = dict[int, Polynomial]
Operator = Callable[[SuperPolynomial], SuperPolynomial]
FormalFactor = tuple[str, int]
FormalMonomial = tuple[FormalFactor, ...]
FormalExpression = dict[FormalMonomial, GaussianInteger]


def gaussian_power_i(power: int) -> GaussianInteger:
    return (ONE, I, MINUS_ONE, MINUS_I)[power % 4]


def polynomial_normalize(polynomial: Polynomial) -> Polynomial:
    return {exponent: coefficient for exponent, coefficient in polynomial.items() if not coefficient.is_zero()}


def polynomial_constant(coefficient: GaussianInteger) -> Polynomial:
    if coefficient.is_zero():
        return {}
    return {ZERO_EXPONENT: coefficient}


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, ZERO) + coefficient
    return polynomial_normalize(result)


def polynomial_scale(polynomial: Polynomial, coefficient: GaussianInteger) -> Polynomial:
    if coefficient.is_zero():
        return {}
    return polynomial_normalize(
        {exponent: coefficient * value for exponent, value in polynomial.items()}
    )


def polynomial_multiply_variable(polynomial: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        shifted = list(exponent)
        shifted[variable] += 1
        shifted_exponent = tuple(shifted)
        result[shifted_exponent] = result.get(shifted_exponent, ZERO) + coefficient
    return polynomial_normalize(result)


def polynomial_derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[variable]
        if power == 0:
            continue
        shifted = list(exponent)
        shifted[variable] -= 1
        shifted_exponent = tuple(shifted)
        derivative_coefficient = GaussianInteger(power, 0) * coefficient
        result[shifted_exponent] = result.get(shifted_exponent, ZERO) + derivative_coefficient
    return polynomial_normalize(result)


def super_normalize(super_polynomial: SuperPolynomial) -> SuperPolynomial:
    result: SuperPolynomial = {}
    for mask, polynomial in super_polynomial.items():
        normalized = polynomial_normalize(polynomial)
        if normalized:
            result[mask] = normalized
    return result


def super_add(left: SuperPolynomial, right: SuperPolynomial) -> SuperPolynomial:
    result = {mask: dict(polynomial) for mask, polynomial in left.items()}
    for mask, polynomial in right.items():
        result[mask] = polynomial_add(result.get(mask, {}), polynomial)
    return super_normalize(result)


def super_scale(super_polynomial: SuperPolynomial, coefficient: GaussianInteger) -> SuperPolynomial:
    return super_normalize(
        {mask: polynomial_scale(polynomial, coefficient) for mask, polynomial in super_polynomial.items()}
    )


def super_wedge_left(variable: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    """Left multiplication by one primitive odd coordinate."""

    result: SuperPolynomial = {}
    variable_bit = 1 << variable
    lower_bits = variable_bit - 1
    for mask, polynomial in super_polynomial.items():
        if mask & variable_bit:
            continue
        swaps = (mask & lower_bits).bit_count()
        coefficient = MINUS_ONE if swaps % 2 else ONE
        new_mask = mask | variable_bit
        term = polynomial_scale(polynomial, coefficient)
        result[new_mask] = polynomial_add(result.get(new_mask, {}), term)
    return super_normalize(result)


def super_left_derivative(variable: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    """Left derivative by one primitive odd coordinate."""

    result: SuperPolynomial = {}
    variable_bit = 1 << variable
    lower_bits = variable_bit - 1
    for mask, polynomial in super_polynomial.items():
        if not mask & variable_bit:
            continue
        position = (mask & lower_bits).bit_count()
        coefficient = MINUS_ONE if position % 2 else ONE
        new_mask = mask ^ variable_bit
        term = polynomial_scale(polynomial, coefficient)
        result[new_mask] = polynomial_add(result.get(new_mask, {}), term)
    return super_normalize(result)


def super_bosonic_momentum(variable: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    return super_normalize(
        {
            mask: polynomial_multiply_variable(polynomial, variable)
            for mask, polynomial in super_polynomial.items()
        }
    )


def super_bosonic_derivative(variable: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    return super_normalize(
        {
            mask: polynomial_derivative(polynomial, variable)
            for mask, polynomial in super_polynomial.items()
        }
    )


def super_basis(mask: int) -> SuperPolynomial:
    return {mask: polynomial_constant(ONE)}


def super_one() -> SuperPolynomial:
    return super_basis(0)


def super_bosonic_coordinate(variable: int) -> SuperPolynomial:
    exponent = [0, 0, 0, 0]
    exponent[variable] = 1
    return {0: {tuple(exponent): ONE}}


def theta_multiply(index: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    return super_wedge_left(index, super_polynomial)


def theta_derivative(index: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    return super_left_derivative(index, super_polynomial)


def raised_bar_theta_multiply(index: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    """barvartheta^dot a = epsilon^(dot a dot b) barvartheta_dot b."""

    if index == 0:
        return super_wedge_left(3, super_polynomial)
    if index == 1:
        return super_scale(super_wedge_left(2, super_polynomial), MINUS_ONE)
    raise IndexError(index)


def lower_bar_derivative(index: int, super_polynomial: SuperPolynomial) -> SuperPolynomial:
    """barpartial_dot a = epsilon_(dot a dot b) d^L/d barvartheta_dot b."""

    if index == 0:
        return super_scale(super_left_derivative(3, super_polynomial), MINUS_ONE)
    if index == 1:
        return super_left_derivative(2, super_polynomial)
    raise IndexError(index)


def matrix_scale(
    matrix: tuple[tuple[GaussianInteger, GaussianInteger], tuple[GaussianInteger, GaussianInteger]],
    coefficient: GaussianInteger,
) -> tuple[tuple[GaussianInteger, GaussianInteger], tuple[GaussianInteger, GaussianInteger]]:
    return tuple(
        tuple(coefficient * entry for entry in row) for row in matrix
    )  # type: ignore[return-value]


SIGMA_IDENTITY = ((ONE, ZERO), (ZERO, ONE))
SIGMA_1 = ((ZERO, ONE), (ONE, ZERO))
SIGMA_2 = ((ZERO, MINUS_I), (I, ZERO))
SIGMA_3 = ((ONE, ZERO), (ZERO, MINUS_ONE))
SIGMA_LORENTZ = (SIGMA_IDENTITY, SIGMA_1, SIGMA_2, SIGMA_3)
SIGMA_EUCLIDEAN = (
    matrix_scale(SIGMA_1, MINUS_I),
    matrix_scale(SIGMA_2, MINUS_I),
    matrix_scale(SIGMA_3, MINUS_I),
    SIGMA_IDENTITY,
)


@dataclass(frozen=True)
class FlatOperators:
    signature: str
    sigma: tuple[
        tuple[tuple[GaussianInteger, GaussianInteger], tuple[GaussianInteger, GaussianInteger]], ...
    ]
    p: tuple[Operator, Operator, Operator, Operator]
    q: tuple[Operator, Operator]
    bar_q: tuple[Operator, Operator]
    d: tuple[Operator, Operator]
    bar_d: tuple[Operator, Operator]


def operator_sum(*terms: SuperPolynomial) -> SuperPolynomial:
    result: SuperPolynomial = {}
    for term in terms:
        result = super_add(result, term)
    return result


def make_flat_operators(signature: str, bosonic_derivative: Callable[[int, SuperPolynomial], SuperPolynomial]) -> FlatOperators:
    if signature == "Lorentzian":
        sigma = SIGMA_LORENTZ
        q_derivative_coefficient = MINUS_I
        p_coefficient = MINUS_I
        d_derivative_coefficient = ONE
        d_tail_coefficient = MINUS_I
        bar_d_tail_coefficient = I
    elif signature == "Euclidean":
        sigma = SIGMA_EUCLIDEAN
        q_derivative_coefficient = MINUS_ONE
        p_coefficient = MINUS_ONE
        d_derivative_coefficient = ONE
        d_tail_coefficient = ONE
        bar_d_tail_coefficient = MINUS_ONE
    else:
        raise ValueError(signature)

    p_operators: list[Operator] = []
    for vector_index in range(4):
        p_operators.append(
            lambda value, vector_index=vector_index: super_scale(
                bosonic_derivative(vector_index, value), p_coefficient
            )
        )

    q_operators: list[Operator] = []
    bar_q_operators: list[Operator] = []
    d_operators: list[Operator] = []
    bar_d_operators: list[Operator] = []

    for spinor_index in range(2):
        def q(value: SuperPolynomial, spinor_index: int = spinor_index) -> SuperPolynomial:
            result = super_scale(theta_derivative(spinor_index, value), q_derivative_coefficient)
            for vector_index in range(4):
                differentiated = bosonic_derivative(vector_index, value)
                for dotted_index in range(2):
                    term = raised_bar_theta_multiply(dotted_index, differentiated)
                    result = super_add(
                        result,
                        super_scale(term, sigma[vector_index][spinor_index][dotted_index]),
                    )
            return super_normalize(result)

        def d(value: SuperPolynomial, spinor_index: int = spinor_index) -> SuperPolynomial:
            result = super_scale(theta_derivative(spinor_index, value), d_derivative_coefficient)
            for vector_index in range(4):
                differentiated = bosonic_derivative(vector_index, value)
                for dotted_index in range(2):
                    term = raised_bar_theta_multiply(dotted_index, differentiated)
                    result = super_add(
                        result,
                        super_scale(
                            term,
                            d_tail_coefficient * sigma[vector_index][spinor_index][dotted_index],
                        ),
                    )
            return super_normalize(result)

        q_operators.append(q)
        d_operators.append(d)

    for dotted_index in range(2):
        def bar_q(value: SuperPolynomial, dotted_index: int = dotted_index) -> SuperPolynomial:
            result = super_scale(lower_bar_derivative(dotted_index, value), q_derivative_coefficient)
            for vector_index in range(4):
                differentiated = bosonic_derivative(vector_index, value)
                for spinor_index in range(2):
                    term = theta_multiply(spinor_index, differentiated)
                    result = super_add(
                        result,
                        super_scale(term, -sigma[vector_index][spinor_index][dotted_index]),
                    )
            return super_normalize(result)

        def bar_d(value: SuperPolynomial, dotted_index: int = dotted_index) -> SuperPolynomial:
            result = super_scale(lower_bar_derivative(dotted_index, value), d_derivative_coefficient)
            for vector_index in range(4):
                differentiated = bosonic_derivative(vector_index, value)
                for spinor_index in range(2):
                    term = theta_multiply(spinor_index, differentiated)
                    result = super_add(
                        result,
                        super_scale(
                            term,
                            bar_d_tail_coefficient * sigma[vector_index][spinor_index][dotted_index],
                        ),
                    )
            return super_normalize(result)

        bar_q_operators.append(bar_q)
        bar_d_operators.append(bar_d)

    return FlatOperators(
        signature=signature,
        sigma=sigma,
        p=tuple(p_operators),  # type: ignore[arg-type]
        q=tuple(q_operators),  # type: ignore[arg-type]
        bar_q=tuple(bar_q_operators),  # type: ignore[arg-type]
        d=tuple(d_operators),  # type: ignore[arg-type]
        bar_d=tuple(bar_d_operators),  # type: ignore[arg-type]
    )


def operator_anticommutator(left: Operator, right: Operator) -> Operator:
    return lambda value: super_add(left(right(value)), right(left(value)))


def operator_commutator(left: Operator, right: Operator) -> Operator:
    return lambda value: super_add(left(right(value)), super_scale(right(left(value)), MINUS_ONE))


def zero_operator(_: SuperPolynomial) -> SuperPolynomial:
    return {}


def identity_operator(value: SuperPolynomial) -> SuperPolynomial:
    return value


def linear_combination(operators: Iterable[tuple[GaussianInteger, Operator]]) -> Operator:
    terms = tuple(operators)

    def result(value: SuperPolynomial) -> SuperPolynomial:
        output: SuperPolynomial = {}
        for coefficient, operator in terms:
            output = super_add(output, super_scale(operator(value), coefficient))
        return output

    return result


def gaussian_string(value: GaussianInteger) -> str:
    if value.imag == 0:
        return str(value.real)
    if value.real == 0:
        if value.imag == 1:
            return "i"
        if value.imag == -1:
            return "-i"
        return f"{value.imag}i"
    sign = "+" if value.imag > 0 else "-"
    magnitude = abs(value.imag)
    imaginary = "i" if magnitude == 1 else f"{magnitude}i"
    return f"{value.real}{sign}{imaginary}"


def super_serializable(value: SuperPolynomial, bosonic_names: tuple[str, str, str, str]) -> list[dict[str, object]]:
    terms: list[dict[str, object]] = []
    for mask in sorted(value):
        for exponent in sorted(value[mask]):
            coefficient = value[mask][exponent]
            bosonic = [
                {"name": bosonic_names[index], "power": power}
                for index, power in enumerate(exponent)
                if power
            ]
            grassmann = [index for index in range(N_GRASSMANN) if mask & (1 << index)]
            terms.append(
                {
                    "coefficient": gaussian_string(coefficient),
                    "bosonic": bosonic,
                    "grassmann_generator_indices": grassmann,
                }
            )
    return terms


class VerificationRecorder:
    def __init__(self) -> None:
        self.families: dict[str, dict[str, int]] = {}
        self.failures: list[dict[str, object]] = []

    def check_operator_identity(
        self,
        family: str,
        identity: str,
        left: Operator,
        right: Operator,
        inputs: Iterable[SuperPolynomial],
        bosonic_names: tuple[str, str, str, str],
    ) -> None:
        input_values = tuple(inputs)
        record = self.families.setdefault(
            family,
            {"operator_identities": 0, "input_cases": 0, "passed_cases": 0, "failed_cases": 0},
        )
        record["operator_identities"] += 1
        record["input_cases"] += len(input_values)
        for case_index, input_value in enumerate(input_values):
            left_value = super_normalize(left(input_value))
            right_value = super_normalize(right(input_value))
            if left_value == right_value:
                record["passed_cases"] += 1
                continue
            record["failed_cases"] += 1
            if len(self.failures) < 20:
                self.failures.append(
                    {
                        "family": family,
                        "identity": identity,
                        "case_index": case_index,
                        "left": super_serializable(left_value, bosonic_names),
                        "right": super_serializable(right_value, bosonic_names),
                    }
                )

    def check_exact_value(self, family: str, identity: str, passed: bool) -> None:
        record = self.families.setdefault(
            family,
            {"operator_identities": 0, "input_cases": 0, "passed_cases": 0, "failed_cases": 0},
        )
        record["operator_identities"] += 1
        record["input_cases"] += 1
        if passed:
            record["passed_cases"] += 1
        else:
            record["failed_cases"] += 1
            if len(self.failures) < 20:
                self.failures.append({"family": family, "identity": identity})


def check_grassmann_calculus(recorder: VerificationRecorder, basis: tuple[SuperPolynomial, ...]) -> None:
    names = ("k0", "k1", "k2", "k3")
    for left_index in range(2):
        for right_index in range(2):
            theta_left = lambda value, left_index=left_index: theta_derivative(left_index, value)
            theta_right = lambda value, right_index=right_index: theta_multiply(right_index, value)
            coefficient = ONE if left_index == right_index else ZERO
            recorder.check_operator_identity(
                "grassmann_calculus",
                f"{{partial_{left_index + 1},vartheta^{right_index + 1}}}=delta",
                operator_anticommutator(theta_left, theta_right),
                linear_combination(((coefficient, identity_operator),)),
                basis,
                names,
            )

            bar_left = lambda value, left_index=left_index: lower_bar_derivative(left_index, value)
            bar_right = lambda value, right_index=right_index: raised_bar_theta_multiply(right_index, value)
            bar_coefficient = MINUS_ONE if left_index == right_index else ZERO
            recorder.check_operator_identity(
                "grassmann_calculus",
                f"{{barpartial_dot{left_index + 1},barvartheta^dot{right_index + 1}}}=-delta",
                operator_anticommutator(bar_left, bar_right),
                linear_combination(((bar_coefficient, identity_operator),)),
                basis,
                names,
            )


def check_flat_algebra(
    recorder: VerificationRecorder,
    operators: FlatOperators,
    basis: tuple[SuperPolynomial, ...],
    bosonic_names: tuple[str, str, str, str],
) -> None:
    prefix = operators.signature.lower()

    for left_index in range(2):
        for right_index in range(2):
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                f"{{Q_{left_index + 1},Q_{right_index + 1}}}=0",
                operator_anticommutator(operators.q[left_index], operators.q[right_index]),
                zero_operator,
                basis,
                bosonic_names,
            )
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                f"{{barQ_dot{left_index + 1},barQ_dot{right_index + 1}}}=0",
                operator_anticommutator(operators.bar_q[left_index], operators.bar_q[right_index]),
                zero_operator,
                basis,
                bosonic_names,
            )
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                f"{{D_{left_index + 1},D_{right_index + 1}}}=0",
                operator_anticommutator(operators.d[left_index], operators.d[right_index]),
                zero_operator,
                basis,
                bosonic_names,
            )
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                f"{{barD_dot{left_index + 1},barD_dot{right_index + 1}}}=0",
                operator_anticommutator(operators.bar_d[left_index], operators.bar_d[right_index]),
                zero_operator,
                basis,
                bosonic_names,
            )

            q_rhs = linear_combination(
                (
                    (MINUS_TWO * operators.sigma[vector_index][left_index][right_index], operators.p[vector_index])
                    for vector_index in range(4)
                )
            )
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                f"{{Q_{left_index + 1},barQ_dot{right_index + 1}}}=-2 sigma.P",
                operator_anticommutator(operators.q[left_index], operators.bar_q[right_index]),
                q_rhs,
                basis,
                bosonic_names,
            )

            d_bracket_coefficient = MINUS_TWO if operators.signature == "Lorentzian" else TWO
            d_rhs = linear_combination(
                (
                    (
                        d_bracket_coefficient * operators.sigma[vector_index][left_index][right_index],
                        operators.p[vector_index],
                    )
                    for vector_index in range(4)
                )
            )
            recorder.check_operator_identity(
                f"{prefix}_graded_algebra",
                (
                    f"{{D_{left_index + 1},barD_dot{right_index + 1}}}="
                    f"{'-2' if operators.signature == 'Lorentzian' else '+2'} sigma.P"
                ),
                operator_anticommutator(operators.d[left_index], operators.bar_d[right_index]),
                d_rhs,
                basis,
                bosonic_names,
            )

            mixed_pairs = (
                (operators.q[left_index], operators.d[right_index], "Q,D"),
                (operators.q[left_index], operators.bar_d[right_index], "Q,barD"),
                (operators.bar_q[left_index], operators.d[right_index], "barQ,D"),
                (operators.bar_q[left_index], operators.bar_d[right_index], "barQ,barD"),
            )
            for left, right, label in mixed_pairs:
                recorder.check_operator_identity(
                    f"{prefix}_mixed_q_d",
                    f"{{{label}}}=0[{left_index + 1},{right_index + 1}]",
                    operator_anticommutator(left, right),
                    zero_operator,
                    basis,
                    bosonic_names,
                )

    odd_operators = (
        *(operator for operator in operators.q),
        *(operator for operator in operators.bar_q),
        *(operator for operator in operators.d),
        *(operator for operator in operators.bar_d),
    )
    odd_labels = ("Q_1", "Q_2", "barQ_dot1", "barQ_dot2", "D_1", "D_2", "barD_dot1", "barD_dot2")
    for vector_index in range(4):
        for odd_operator, label in zip(odd_operators, odd_labels, strict=True):
            recorder.check_operator_identity(
                f"{prefix}_translation_commutators",
                f"[P_{vector_index},{label}]=0",
                operator_commutator(operators.p[vector_index], odd_operator),
                zero_operator,
                basis,
                bosonic_names,
            )
        for second_vector_index in range(4):
            recorder.check_operator_identity(
                f"{prefix}_translation_commutators",
                f"[P_{vector_index},P_{second_vector_index}]=0",
                operator_commutator(operators.p[vector_index], operators.p[second_vector_index]),
                zero_operator,
                basis,
                bosonic_names,
            )


def wick_substitute_lorentz_to_euclidean(value: SuperPolynomial) -> SuperPolynomial:
    """k_L^0 -> i k_E^4 and k_L^j -> k_E^j."""

    result: SuperPolynomial = {}
    for mask, polynomial in value.items():
        transformed: Polynomial = {}
        for exponent, coefficient in polynomial.items():
            euclidean_exponent: Exponent = (exponent[1], exponent[2], exponent[3], exponent[0])
            euclidean_coefficient = coefficient * gaussian_power_i(exponent[0])
            transformed[euclidean_exponent] = transformed.get(euclidean_exponent, ZERO) + euclidean_coefficient
        result[mask] = polynomial_normalize(transformed)
    return super_normalize(result)


def wick_transformed(operator: Operator, coefficient: GaussianInteger) -> Operator:
    return lambda value: super_scale(wick_substitute_lorentz_to_euclidean(operator(value)), coefficient)


def check_wick_relations(
    recorder: VerificationRecorder,
    lorentz: FlatOperators,
    euclidean: FlatOperators,
    basis: tuple[SuperPolynomial, ...],
) -> None:
    names = ("kE1", "kE2", "kE3", "kE4")
    for spatial_index in range(3):
        recorder.check_operator_identity(
            "wick_relations",
            f"P_E{spatial_index + 1}=-i Wick(P_L{spatial_index + 1})",
            euclidean.p[spatial_index],
            wick_transformed(lorentz.p[spatial_index + 1], MINUS_I),
            basis,
            names,
        )
    recorder.check_operator_identity(
        "wick_relations",
        "P_E4=-Wick(P_L0)",
        euclidean.p[3],
        wick_transformed(lorentz.p[0], MINUS_ONE),
        basis,
        names,
    )

    for spinor_index in range(2):
        for label, lorentz_pair, euclidean_pair, coefficient in (
            ("Q", lorentz.q, euclidean.q, MINUS_I),
            ("barQ", lorentz.bar_q, euclidean.bar_q, MINUS_I),
            ("D", lorentz.d, euclidean.d, ONE),
            ("barD", lorentz.bar_d, euclidean.bar_d, ONE),
        ):
            recorder.check_operator_identity(
                "wick_relations",
                (
                    f"{label}_E{spinor_index + 1}="
                    f"{'-i ' if coefficient == MINUS_I else ''}Wick({label}_L{spinor_index + 1})"
                ),
                euclidean_pair[spinor_index],
                wick_transformed(lorentz_pair[spinor_index], coefficient),
                basis,
                names,
            )

    for spatial_index in range(3):
        recorder.check_exact_value(
            "wick_relations",
            f"sigma_E^{spatial_index + 1}=-i sigma_L^{spatial_index + 1}",
            SIGMA_EUCLIDEAN[spatial_index] == matrix_scale(SIGMA_LORENTZ[spatial_index + 1], MINUS_I),
        )
    recorder.check_exact_value(
        "wick_relations",
        "sigma_E^4=sigma_L^0",
        SIGMA_EUCLIDEAN[3] == SIGMA_LORENTZ[0],
    )


def theta_sigma_bar_theta(
    sigma: tuple[
        tuple[tuple[GaussianInteger, GaussianInteger], tuple[GaussianInteger, GaussianInteger]], ...
    ],
    vector_index: int,
) -> SuperPolynomial:
    result: SuperPolynomial = {}
    for spinor_index in range(2):
        for dotted_index in range(2):
            term = raised_bar_theta_multiply(dotted_index, super_one())
            term = theta_multiply(spinor_index, term)
            result = super_add(
                result,
                super_scale(term, sigma[vector_index][spinor_index][dotted_index]),
            )
    return super_normalize(result)


def check_chiral_coordinates(recorder: VerificationRecorder) -> None:
    lorentz = make_flat_operators("Lorentzian", super_bosonic_derivative)
    euclidean = make_flat_operators("Euclidean", super_bosonic_derivative)
    lorentz_names = ("xL0", "xL1", "xL2", "xL3")
    euclidean_names = ("xE1", "xE2", "xE3", "xE4")

    for vector_index in range(4):
        bilinear = theta_sigma_bar_theta(SIGMA_LORENTZ, vector_index)
        y = super_add(super_bosonic_coordinate(vector_index), super_scale(bilinear, MINUS_I))
        bar_y = super_add(super_bosonic_coordinate(vector_index), super_scale(bilinear, I))
        for dotted_index in range(2):
            recorder.check_operator_identity(
                "lorentzian_chiral_coordinates",
                f"barD_dot{dotted_index + 1} y_L^{vector_index}=0",
                lorentz.bar_d[dotted_index],
                zero_operator,
                (y,),
                lorentz_names,
            )
        for spinor_index in range(2):
            recorder.check_operator_identity(
                "lorentzian_chiral_coordinates",
                f"D_{spinor_index + 1} bary_L^{vector_index}=0",
                lorentz.d[spinor_index],
                zero_operator,
                (bar_y,),
                lorentz_names,
            )

    for vector_index in range(4):
        bilinear = theta_sigma_bar_theta(SIGMA_EUCLIDEAN, vector_index)
        y = super_add(super_bosonic_coordinate(vector_index), bilinear)
        bar_y = super_add(super_bosonic_coordinate(vector_index), super_scale(bilinear, MINUS_ONE))
        for dotted_index in range(2):
            recorder.check_operator_identity(
                "euclidean_chiral_coordinates",
                f"barD_dot{dotted_index + 1} y_E^{vector_index + 1}=0",
                euclidean.bar_d[dotted_index],
                zero_operator,
                (y,),
                euclidean_names,
            )
        for spinor_index in range(2):
            recorder.check_operator_identity(
                "euclidean_chiral_coordinates",
                f"D_{spinor_index + 1} bary_E^{vector_index + 1}=0",
                euclidean.d[spinor_index],
                zero_operator,
                (bar_y,),
                euclidean_names,
            )


def formal_normalize(expression: FormalExpression) -> FormalExpression:
    return {monomial: coefficient for monomial, coefficient in expression.items() if not coefficient.is_zero()}


def formal_add_term(
    expression: FormalExpression,
    coefficient: GaussianInteger,
    *factors: FormalFactor,
) -> None:
    expression[factors] = expression.get(factors, ZERO) + coefficient
    if expression[factors].is_zero():
        del expression[factors]


def formal_canonicalize_factors(factors: tuple[FormalFactor, ...]) -> FormalMonomial:
    """Move the even x/dx factors past odd factors; no odd-odd swap is made."""

    odd = tuple(factor for factor in factors if factor[0] not in {"x", "dx"})
    even = tuple(factor for factor in factors if factor[0] in {"x", "dx"})
    return odd + even


def formal_dagger(expression: FormalExpression) -> FormalExpression:
    """Anti-linear, order-reversing Lorentz coordinate formal involution."""

    factor_dagger: dict[str, tuple[str, GaussianInteger]] = {
        "x": ("x", ONE),
        "dx": ("dx", MINUS_ONE),
        "theta": ("bartheta", ONE),
        "bartheta": ("theta", ONE),
        "dtheta": ("bard", MINUS_ONE),
        "bard": ("dtheta", MINUS_ONE),
    }
    result: FormalExpression = {}
    for monomial, coefficient in expression.items():
        dagger_coefficient = coefficient.conjugate()
        dagger_factors: list[FormalFactor] = []
        for kind, index in reversed(monomial):
            dagger_kind, rule_coefficient = factor_dagger[kind]
            dagger_coefficient = dagger_coefficient * rule_coefficient
            dagger_factors.append((dagger_kind, index))
        canonical_monomial = formal_canonicalize_factors(tuple(dagger_factors))
        result[canonical_monomial] = result.get(canonical_monomial, ZERO) + dagger_coefficient
    return formal_normalize(result)


def formal_p(vector_index: int) -> FormalExpression:
    return {(('dx', vector_index),): MINUS_I}


def formal_q(spinor_index: int) -> FormalExpression:
    result: FormalExpression = {}
    formal_add_term(result, MINUS_I, ("dtheta", spinor_index))
    for vector_index in range(4):
        for dotted_index in range(2):
            formal_add_term(
                result,
                SIGMA_LORENTZ[vector_index][spinor_index][dotted_index],
                ("bartheta", dotted_index),
                ("dx", vector_index),
            )
    return formal_normalize(result)


def formal_bar_q(dotted_index: int) -> FormalExpression:
    result: FormalExpression = {}
    formal_add_term(result, MINUS_I, ("bard", dotted_index))
    for vector_index in range(4):
        for spinor_index in range(2):
            formal_add_term(
                result,
                -SIGMA_LORENTZ[vector_index][spinor_index][dotted_index],
                ("theta", spinor_index),
                ("dx", vector_index),
            )
    return formal_normalize(result)


def formal_d(spinor_index: int) -> FormalExpression:
    result: FormalExpression = {}
    formal_add_term(result, ONE, ("dtheta", spinor_index))
    for vector_index in range(4):
        for dotted_index in range(2):
            formal_add_term(
                result,
                MINUS_I * SIGMA_LORENTZ[vector_index][spinor_index][dotted_index],
                ("bartheta", dotted_index),
                ("dx", vector_index),
            )
    return formal_normalize(result)


def formal_bar_d(dotted_index: int) -> FormalExpression:
    result: FormalExpression = {}
    formal_add_term(result, ONE, ("bard", dotted_index))
    for vector_index in range(4):
        for spinor_index in range(2):
            formal_add_term(
                result,
                I * SIGMA_LORENTZ[vector_index][spinor_index][dotted_index],
                ("theta", spinor_index),
                ("dx", vector_index),
            )
    return formal_normalize(result)


def formal_chiral_coordinate(vector_index: int, bilinear_coefficient: GaussianInteger) -> FormalExpression:
    result: FormalExpression = {(('x', vector_index),): ONE}
    for spinor_index in range(2):
        for dotted_index in range(2):
            formal_add_term(
                result,
                bilinear_coefficient * SIGMA_LORENTZ[vector_index][spinor_index][dotted_index],
                ("theta", spinor_index),
                ("bartheta", dotted_index),
            )
    return formal_normalize(result)


def check_lorentzian_formal_adjoint(recorder: VerificationRecorder) -> None:
    for vector_index in range(4):
        recorder.check_exact_value(
            "lorentzian_coordinate_formal_adjoint",
            f"(P_C,L_{vector_index})^dagger=P_C,L_{vector_index}",
            formal_dagger(formal_p(vector_index)) == formal_p(vector_index),
        )
    for spinor_index in range(2):
        recorder.check_exact_value(
            "lorentzian_coordinate_formal_adjoint",
            f"(Q_C,L_{spinor_index + 1})^dagger=barQ_C,L_dot{spinor_index + 1}",
            formal_dagger(formal_q(spinor_index)) == formal_bar_q(spinor_index),
        )
        recorder.check_exact_value(
            "lorentzian_coordinate_formal_adjoint",
            f"(D_L_{spinor_index + 1})^dagger=-barD_L_dot{spinor_index + 1}",
            formal_dagger(formal_d(spinor_index))
            == {monomial: -coefficient for monomial, coefficient in formal_bar_d(spinor_index).items()},
        )
    for vector_index in range(4):
        y = formal_chiral_coordinate(vector_index, MINUS_I)
        bar_y = formal_chiral_coordinate(vector_index, I)
        recorder.check_exact_value(
            "lorentzian_coordinate_formal_adjoint",
            f"(y_L^{vector_index})^dagger=bary_L^{vector_index}",
            formal_dagger(y) == bar_y,
        )


def build_audit() -> dict[str, object]:
    basis = tuple(super_basis(mask) for mask in range(1 << N_GRASSMANN))
    recorder = VerificationRecorder()

    check_grassmann_calculus(recorder, basis)

    lorentz = make_flat_operators("Lorentzian", super_bosonic_momentum)
    euclidean = make_flat_operators("Euclidean", super_bosonic_momentum)
    check_flat_algebra(recorder, lorentz, basis, ("kL0", "kL1", "kL2", "kL3"))
    check_flat_algebra(recorder, euclidean, basis, ("kE1", "kE2", "kE3", "kE4"))
    check_wick_relations(recorder, lorentz, euclidean, basis)
    check_chiral_coordinates(recorder)
    check_lorentzian_formal_adjoint(recorder)

    total_identities = sum(record["operator_identities"] for record in recorder.families.values())
    total_cases = sum(record["input_cases"] for record in recorder.families.values())
    total_passed = sum(record["passed_cases"] for record in recorder.families.values())
    total_failed = sum(record["failed_cases"] for record in recorder.families.values())

    return {
        "task_id": "CONTRACT-STEP-02A-FLAT-SUPERSPACE-001",
        "status": "PASS" if total_failed == 0 else "FAIL",
        "arithmetic": {
            "coefficient_ring": "Z[i][k_0,k_1,k_2,k_3]",
            "implementation": "exact integer pairs; no floating point; no external CAS",
        },
        "grassmann_basis": {
            "ordered_primitive_generators": [
                "vartheta^1",
                "vartheta^2",
                "barvartheta_dot1",
                "barvartheta_dot2",
            ],
            "basis_monomials": len(basis),
            "raised_bar_rule": "barvartheta^dot a=epsilon^(dot a dot b)barvartheta_dot b",
            "lower_bar_derivative_rule": "barpartial_dot a=epsilon_(dot a dot b)d^L/dbarvartheta_dot b",
            "derived_bracket": "{barpartial_dot a,barvartheta^dot b}=-delta_dot a^dot b",
        },
        "bosonic_symbols": {
            "Lorentzian": ["kL0", "kL1", "kL2", "kL3"],
            "Euclidean": ["kE1", "kE2", "kE3", "kE4"],
            "independence": "four commuting algebraically independent indeterminates per signature",
        },
        "operator_definitions": {
            "Lorentzian": {
                "P": "-i partial_L",
                "Q": "-i partial_a + sigma_L barvartheta partial_L",
                "barQ": "-i barpartial_dot - vartheta sigma_L partial_L",
                "D": "partial_a - i sigma_L barvartheta partial_L",
                "barD": "barpartial_dot + i vartheta sigma_L partial_L",
                "Q_barQ": "-2 sigma_L.P",
                "D_barD": "-2 sigma_L.P",
            },
            "Euclidean": {
                "P": "-partial_E",
                "Q": "-partial_a + sigma_E barvartheta partial_E",
                "barQ": "-barpartial_dot - vartheta sigma_E partial_E",
                "D": "partial_a + sigma_E barvartheta partial_E",
                "barD": "barpartial_dot - vartheta sigma_E partial_E",
                "Q_barQ": "-2 sigma_E.P",
                "D_barD": "+2 sigma_E.P",
            },
        },
        "lorentzian_coordinate_formal_adjoint": {
            "rules": [
                "x^dagger=x",
                "partial_mu^dagger=-partial_mu",
                "(vartheta^a)^dagger=barvartheta^dot a",
                "(partial_a)^dagger=-barpartial_dot a",
                "(A B)^dagger=B^dagger A^dagger",
            ],
            "scope": "exact symbolic coordinate differential-operator involution; not a Euclidean or Berezin L2 spinor adjoint",
        },
        "families": recorder.families,
        "totals": {
            "operator_identities": total_identities,
            "input_cases": total_cases,
            "passed_cases": total_passed,
            "failed_cases": total_failed,
        },
        "failures": recorder.failures,
    }


def main() -> int:
    audit = build_audit()
    repository_root = Path(__file__).resolve().parents[1]
    audit_path = repository_root / "audits" / "step2a-symbolic-verification.json"
    rendered = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    audit_path.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
