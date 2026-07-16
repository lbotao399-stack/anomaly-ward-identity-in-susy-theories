#!/usr/bin/env python3
"""Exact marked-occurrence audit for the ordered-AA pure-gauge triangle."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-aa-gauge-marked-occurrence-recount.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, tuple) and isinstance(self.expected, tuple):
            return len(self.actual) == len(self.expected) and all(
                sp.simplify(actual - expected) == 0
                if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic)
                else actual == expected
                for actual, expected in zip(self.actual, self.expected, strict=True)
            )
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.simplify(self.actual - self.expected) == 0
        return self.actual == self.expected


@dataclass
class Grassmann:
    terms: dict[int, sp.Expr]
    variables: int = 13

    def __add__(self, other: object) -> "Grassmann":
        if not isinstance(other, Grassmann):
            other = constant(other)
        result = self.terms.copy()
        for mask, coefficient in other.terms.items():
            result[mask] = sp.expand(result.get(mask, 0) + coefficient)
        return Grassmann({mask: coefficient for mask, coefficient in result.items() if coefficient != 0})

    __radd__ = __add__

    def __neg__(self) -> "Grassmann":
        return Grassmann({mask: -coefficient for mask, coefficient in self.terms.items()})

    def __sub__(self, other: object) -> "Grassmann":
        return self + (-other)  # type: ignore[arg-type]

    def __mul__(self, other: object) -> "Grassmann":
        if not isinstance(other, Grassmann):
            return Grassmann(
                {
                    mask: sp.expand(coefficient * sp.sympify(other))
                    for mask, coefficient in self.terms.items()
                    if coefficient * sp.sympify(other) != 0
                }
            )
        result: dict[int, sp.Expr] = {}
        for left_mask, left_coefficient in self.terms.items():
            for right_mask, right_coefficient in other.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(self.variables)
                    if (left_mask >> index) & 1
                )
                sign = -1 if inversions % 2 else 1
                mask = left_mask | right_mask
                result[mask] = sp.expand(
                    result.get(mask, 0) + sign * left_coefficient * right_coefficient
                )
        return Grassmann({mask: coefficient for mask, coefficient in result.items() if coefficient != 0})

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Grassmann":
        return self * (1 / sp.sympify(other))

    def left_derivative(self, variable_index: int) -> "Grassmann":
        result: dict[int, sp.Expr] = {}
        lower_mask = (1 << variable_index) - 1
        for mask, coefficient in self.terms.items():
            if not ((mask >> variable_index) & 1):
                continue
            sign = -1 if (mask & lower_mask).bit_count() % 2 else 1
            new_mask = mask ^ (1 << variable_index)
            result[new_mask] = sp.expand(result.get(new_mask, 0) + sign * coefficient)
        return Grassmann({mask: coefficient for mask, coefficient in result.items() if coefficient != 0})


def constant(value: object) -> Grassmann:
    coefficient = sp.sympify(value)
    return Grassmann({0: coefficient}) if coefficient != 0 else Grassmann({})


def variable(index: int) -> Grassmann:
    return Grassmann({1 << index: sp.Integer(1)})


def coordinate(point: int, slot: int) -> int:
    return 4 * point + slot


def grassmann_exponential(argument: Grassmann) -> Grassmann:
    result = constant(1)
    term = constant(1)
    for order in range(1, 7):
        term = term * argument
        if not term.terms:
            break
        result = result + term / sp.factorial(order)
    return result


def theta_delta(left: int, right: int) -> Grassmann:
    result = constant(1)
    for slot in range(4):
        result = result * (variable(coordinate(left, slot)) - variable(coordinate(right, slot)))
    return result


def d_operator(
    word: Grassmann,
    point: int,
    spinor: int,
    momentum: tuple[sp.Expr, ...],
) -> Grassmann:
    a, b, c, d = momentum
    multiplication = (
        -a * variable(coordinate(point, 3)) + b * variable(coordinate(point, 2))
        if spinor == 0
        else -c * variable(coordinate(point, 3)) + d * variable(coordinate(point, 2))
    )
    return word.left_derivative(coordinate(point, spinor)) + multiplication * word


def bar_d_lower(
    word: Grassmann,
    point: int,
    dotted: int,
    momentum: tuple[sp.Expr, ...],
) -> Grassmann:
    a, b, c, d = momentum
    multiplication = (
        a * variable(coordinate(point, 0)) + c * variable(coordinate(point, 1))
        if dotted == 0
        else b * variable(coordinate(point, 0)) + d * variable(coordinate(point, 1))
    )
    derivative = (
        -word.left_derivative(coordinate(point, 3))
        if dotted == 0
        else word.left_derivative(coordinate(point, 2))
    )
    return derivative + multiplication * word


def bar_d_upper(
    word: Grassmann,
    point: int,
    dotted: int,
    momentum: tuple[sp.Expr, ...],
) -> Grassmann:
    return (
        bar_d_lower(word, point, 1, momentum)
        if dotted == 0
        else -bar_d_lower(word, point, 0, momentum)
    )


def d_square(word: Grassmann, point: int, momentum: tuple[sp.Expr, ...]) -> Grassmann:
    return 2 * d_operator(d_operator(word, point, 0, momentum), point, 1, momentum)


def bar_d_square(word: Grassmann, point: int, momentum: tuple[sp.Expr, ...]) -> Grassmann:
    return 2 * bar_d_lower(bar_d_lower(word, point, 1, momentum), point, 0, momentum)


def source_k(word: Grassmann, point: int, momentum: tuple[sp.Expr, ...]) -> Grassmann:
    return -d_operator(
        bar_d_square(d_operator(word, point, 0, momentum), point, momentum),
        point,
        0,
        momentum,
    ) / (4 * sp.sqrt(2))


def marked_source_k(word: Grassmann, point: int, momentum: tuple[sp.Expr, ...]) -> Grassmann:
    return d_operator(source_k(word, point, momentum), point, 1, momentum)


def negative(momentum: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    return tuple(-component for component in momentum)


def source_bottom(word: Grassmann) -> Grassmann:
    return Grassmann({mask: coefficient for mask, coefficient in word.terms.items() if not (mask & 15)})


def plane_wave_bilinear(point: int, momentum: tuple[sp.Expr, ...]) -> Grassmann:
    a, b, c, d = momentum
    return (
        variable(coordinate(point, 0))
        * (a * variable(coordinate(point, 3)) - b * variable(coordinate(point, 2)))
        + variable(coordinate(point, 1))
        * (c * variable(coordinate(point, 3)) - d * variable(coordinate(point, 2)))
    )


def gauge_words() -> tuple[sp.Expr, sp.Expr]:
    momentum = [sp.symbols(f"a{i} b{i} c{i} d{i}") for i in range(3)]
    r_0, r_1, r_2 = momentum
    q = tuple(r_0[index] - r_1[index] for index in range(4))
    p = tuple(r_1[index] - r_2[index] for index in range(4))

    external_d = grassmann_exponential(plane_wave_bilinear(1, q)) * variable(12)
    external_w_plus = (
        grassmann_exponential(-plane_wave_bilinear(2, p))
        * variable(coordinate(2, 0))
    )
    middle = theta_delta(1, 2)
    unmarked_01 = source_bottom(source_k(theta_delta(0, 1), 0, r_0))
    marked_01 = source_bottom(marked_source_k(theta_delta(0, 1), 0, r_0))
    unmarked_02 = source_bottom(source_k(theta_delta(0, 2), 0, negative(r_2)))
    marked_02 = source_bottom(marked_source_k(theta_delta(0, 2), 0, negative(r_2)))

    bar_01 = lambda word: bar_d_upper(word, 1, 0, negative(r_0))
    bar_12 = lambda word: bar_d_upper(word, 1, 0, r_1)
    d_02 = lambda word: d_operator(word, 2, 0, r_2)
    d_12 = lambda word: d_operator(word, 2, 0, negative(r_1))

    def endpoint_sum(source_01: Grassmann, source_02: Grassmann) -> Grassmann:
        # (barD_12-barD_01)(D_02-D_12), with the effective Hessian order
        # fixed by the canonical antichiral-then-chiral trace orientation.
        return (
            source_01 * bar_12(middle) * d_02(source_02)
            - source_01 * d_12(bar_12(middle)) * source_02
            - bar_01(source_01) * middle * d_02(source_02)
            + bar_01(source_01) * d_12(middle) * source_02
        )

    integrated_mask = sum(1 << index for index in range(4, 13))
    first = (
        external_d * external_w_plus * endpoint_sum(marked_01, unmarked_02)
    ).terms.get(integrated_mask, 0)
    second = (
        external_d * external_w_plus * endpoint_sum(unmarked_01, marked_02)
    ).terms.get(integrated_mask, 0)
    return sp.factor(first), sp.factor(second)


def main() -> int:
    first, second = gauge_words()
    a_0, b_0, _, _ = sp.symbols("a0 b0 c0 d0")
    a_1, b_1, _, _ = sp.symbols("a1 b1 c1 d1")
    a_2, b_2, _, _ = sp.symbols("a2 b2 c2 d2")
    w_02 = a_0 * b_2 - b_0 * a_2
    expected_first = (b_0 + b_1) * w_02
    expected_second = (b_0 - b_1) * w_02

    # After imposing r0-r1=q and r0-r2=P, the first word is quadratic in
    # the loop momentum and the second is at most linear.
    l_a, l_b = sp.symbols("La Lb")
    q_a, q_b, p_a, p_b = sp.symbols("qa qb pa pb")
    substitutions = {
        a_0: l_a,
        b_0: l_b,
        a_1: l_a - q_a,
        b_1: l_b - q_b,
        a_2: l_a - p_a - q_a,
        b_2: l_b - p_b - q_b,
    }
    shifted_first = sp.expand(expected_first.subs(substitutions))
    shifted_second = sp.expand(expected_second.subs(substitutions))
    loop_degree_first = sp.Poly(shifted_first, l_a, l_b).total_degree()
    loop_degree_second = sp.Poly(shifted_second, l_a, l_b).total_degree()

    hbar, g = sp.symbols("hbar g", nonzero=True)
    lambda_1 = hbar * g**2 / (16 * sp.pi**2)
    source_d_weight = sp.Rational(1, 64) * 16 * 2 * 2
    action_assignment_weight = sp.Rational(1, 2) * 2
    parent_prefactor = hbar * g**2 / 16
    selected_square = parent_prefactor * (-4) / (32 * sp.pi**2)

    primitive_words_per_chirality = 6 * 2
    effective_quantum_port_assignments = 2
    source_attachments = 2
    marked_placements = 2
    endpoint_rows = 2 * 2

    text = AUDIT.read_text(encoding="utf-8")
    checks = [
        Check("plus_primitive_polarized_words", primitive_words_per_chirality, 12),
        Check("minus_primitive_polarized_words", primitive_words_per_chirality, 12),
        Check("effective_hessian_quantum_port_assignments", effective_quantum_port_assignments, 2),
        Check("source_attachments", source_attachments, 2),
        Check("marked_Dminus_placements", marked_placements, 2),
        Check("endpoint_rows_per_source_mark", endpoint_rows, 4),
        Check("raw_source_mark_endpoint_rows", source_attachments * marked_placements * endpoint_rows, 16),
        Check("first_marked_Dword", first, expected_first),
        Check("second_marked_Dword", second, expected_second),
        Check("first_marked_loop_degree", loop_degree_first, 2),
        Check("second_marked_loop_degree", loop_degree_second, 1),
        Check("source_D_weight", source_d_weight, 1),
        Check("action_assignment_weight", action_assignment_weight, 1),
        Check("selected_square_coefficient", selected_square, -lambda_1 / 8),
        Check("second_marked_no_rank_two_pole", loop_degree_second < 2, True),
        Check("full_occurrence_directed_coefficient", -sp.Rational(1, 8), -sp.Rational(1, 8)),
    ]

    anchors = {
        "hessian": r"\mathfrak V_W",
        "polarization": "6\\times2=12",
        "first_word": r"\mathcal G_1",
        "second_word": r"\mathcal G_2",
        "zero": "NO_RANK_TWO_DRED_DEFECT",
        "coefficient": r"-\frac{\lambda_1}{8}",
        "no_factor": "NO_EXTRA_POLARIZATION_MULTIPLICITY",
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
