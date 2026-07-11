#!/usr/bin/env python3
"""Exact checked-scope off-shell closure gates for Step 4B N=2 SYM.

The first two gates are the free Abelian specializations of the displayed
Lorentzian and Euclidean component rules.  The interaction gate is an exact
constant-background SU(2) covariant-jet calculation.  In particular, it does
not make the invalid replacement delta(D_mu X)=0 when D_mu X=0; it retains
delta(D_mu X)|_{A=partial X=0}=(delta A_mu) cross X.  All spinor matrices and
coefficients lie in Q(i,sqrt(2)); momenta are formal commuting indeterminates
and supersymmetry parameters form an exact exterior algebra.  No random
evaluation or external formula is used.

If a checked gate fails, the script records the exact residual and does not
claim the corresponding closure result.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path

from verify_step3a_gauge_chiral_action import (
    BAR_SIGMA_E,
    BAR_SIGMA_L,
    EPSILON_LOWER,
    Exact,
    I,
    MINUS_I,
    MINUS_ONE,
    ONE,
    SIGMA_E,
    SIGMA_L,
    SIGMA_MN_E,
    SIGMA_MUNU_L,
    SQRT_TWO,
    TWO,
    ZERO,
    exact_string,
    matrix_multiply,
    matrix_scale,
    matrix_subtract,
)


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "audits" / "step4-n2-closure-verification.json"

EPSILON_UPPER = ((ZERO, ONE), (MINUS_ONE, ZERO))
METRIC_L = (-1, 1, 1, 1)

BAR_SIGMA_MUNU_L = tuple(
    tuple(
        matrix_scale(
            matrix_subtract(
                matrix_multiply(BAR_SIGMA_L[mu], SIGMA_L[nu]),
                matrix_multiply(BAR_SIGMA_L[nu], SIGMA_L[mu]),
            ),
            Exact.rational(Fraction(1, 4)),
        )
        for nu in range(4)
    )
    for mu in range(4)
)

BAR_SIGMA_MN_E = tuple(
    tuple(
        matrix_scale(
            matrix_subtract(
                matrix_multiply(BAR_SIGMA_E[m], SIGMA_E[n]),
                matrix_multiply(BAR_SIGMA_E[n], SIGMA_E[m]),
            ),
            Exact.rational(Fraction(1, 4)),
        )
        for n in range(4)
    )
    for m in range(4)
)


# A momentum polynomial is a finite Q(i,sqrt(2))-linear combination of
# p_0^e0 ... p_3^e3.
MomentumMonomial = tuple[int, int, int, int]
Poly = dict[MomentumMonomial, Exact]
ExteriorMonomial = tuple[str, ...]
Entry = dict[ExteriorMonomial, Poly]


def poly_normalize(value: Poly) -> Poly:
    return {key: coefficient for key, coefficient in value.items() if not coefficient.is_zero()}


def poly_constant(value: Exact) -> Poly:
    return {} if value.is_zero() else {(0, 0, 0, 0): value}


def poly_momentum(index: int) -> Poly:
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): ONE}


def poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, ZERO) + coefficient
    return poly_normalize(result)


def poly_scale(value: Poly, coefficient: Exact) -> Poly:
    return poly_normalize({key: coefficient * term for key, term in value.items()})


def poly_multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for left_power, left_coefficient in left.items():
        for right_power, right_coefficient in right.items():
            power = tuple(left_power[index] + right_power[index] for index in range(4))
            result[power] = result.get(power, ZERO) + left_coefficient * right_coefficient
    return poly_normalize(result)


def exterior_product(left: ExteriorMonomial, right: ExteriorMonomial):
    if set(left) & set(right):
        return 0, ()
    concatenated = list(left + right)
    inversions = sum(
        concatenated[i] > concatenated[j]
        for i in range(len(concatenated))
        for j in range(i + 1, len(concatenated))
    )
    return (-1 if inversions % 2 else 1), tuple(sorted(concatenated))


def entry_normalize(value: Entry) -> Entry:
    return {key: poly_normalize(poly) for key, poly in value.items() if poly_normalize(poly)}


def entry_add(left: Entry, right: Entry) -> Entry:
    result = {key: dict(poly) for key, poly in left.items()}
    for monomial, poly in right.items():
        result[monomial] = poly_add(result.get(monomial, {}), poly)
    return entry_normalize(result)


def entry_scale(value: Entry, coefficient: Exact) -> Entry:
    return entry_normalize({key: poly_scale(poly, coefficient) for key, poly in value.items()})


def entry_multiply(left: Entry, right: Entry) -> Entry:
    result: Entry = {}
    for left_odd, left_poly in left.items():
        for right_odd, right_poly in right.items():
            sign, odd = exterior_product(left_odd, right_odd)
            if sign == 0:
                continue
            poly = poly_multiply(left_poly, right_poly)
            if sign == -1:
                poly = poly_scale(poly, MINUS_ONE)
            result[odd] = poly_add(result.get(odd, {}), poly)
    return entry_normalize(result)


def parameter(name: str, coefficient: Exact = ONE) -> Entry:
    return {(name,): poly_constant(coefficient)}


def entry_with_poly(value: Entry, poly: Poly) -> Entry:
    return entry_normalize({key: poly_multiply(term, poly) for key, term in value.items()})


def entry_equal(left: Entry, right: Entry) -> bool:
    return entry_normalize(left) == entry_normalize(right)


FIELDS = (
    *(f"A{mu}" for mu in range(4)),
    "phi",
    "tphi",
    "lambda0",
    "lambda1",
    "tlambda0",
    "tlambda1",
    "psi0",
    "psi1",
    "tpsi0",
    "tpsi1",
    "F",
    "tF",
    "D",
)
FIELD_INDEX = {field: index for index, field in enumerate(FIELDS)}


def zero_matrix():
    return [[{} for _ in FIELDS] for _ in FIELDS]


def matrix_add_term(matrix, row: str, column: str, value: Entry) -> None:
    i = FIELD_INDEX[row]
    j = FIELD_INDEX[column]
    matrix[i][j] = entry_add(matrix[i][j], value)


def matrix_multiply_entries(left, right):
    size = len(FIELDS)
    result = zero_matrix()
    for row in range(size):
        for middle in range(size):
            if not left[row][middle]:
                continue
            for column in range(size):
                if not right[middle][column]:
                    continue
                result[row][column] = entry_add(
                    result[row][column],
                    entry_multiply(left[row][middle], right[middle][column]),
                )
    return result


def matrix_subtract_entries(left, right):
    size = len(FIELDS)
    return [
        [entry_add(left[row][column], entry_scale(right[row][column], MINUS_ONE)) for column in range(size)]
        for row in range(size)
    ]


def p_lower(index: int) -> Poly:
    return poly_momentum(index)


def p_upper_lorentz(index: int) -> Poly:
    return poly_scale(poly_momentum(index), Exact.rational(METRIC_L[index]))


def sigma_lower_lorentz(mu: int):
    return tuple(
        tuple(Exact.rational(METRIC_L[mu]) * SIGMA_L[mu][a][dot] for dot in range(2))
        for a in range(2)
    )


def bar_sigma_lower_lorentz(mu: int):
    return tuple(
        tuple(Exact.rational(METRIC_L[mu]) * BAR_SIGMA_L[mu][dot][a] for a in range(2))
        for dot in range(2)
    )


def parameter_component(kind: str, set_index: int, component: int, raised: bool = False) -> Entry:
    # kind is e, be, n, or bn.  Stored components are lower.
    prefix = {"e": "e", "be": "b", "n": "n", "bn": "m"}[kind]
    if not raised:
        return parameter(f"{set_index}{prefix}{component}")
    result: Entry = {}
    for lower in range(2):
        coefficient = EPSILON_UPPER[component][lower]
        if coefficient.is_zero():
            continue
        result = entry_add(result, parameter(f"{set_index}{prefix}{lower}", coefficient))
    return result


def multiply_parameter_forms(left: Entry, right: Entry, coefficient: Exact = ONE) -> Entry:
    return entry_scale(entry_multiply(left, right), coefficient)


def add_spinor_curvature(
    matrix,
    row_prefix: str,
    parameter_kind: str,
    set_index: int,
    sigma_mn,
    coefficient: Exact,
) -> None:
    for spinor in range(2):
        row = f"{row_prefix}{spinor}"
        for raised_spinor in range(2):
            eta = parameter_component(parameter_kind, set_index, raised_spinor, raised=False)
            for mu in range(4):
                for nu in range(4):
                    sigma = sigma_mn[mu][nu][spinor][raised_spinor]
                    if sigma.is_zero():
                        continue
                    # F_mn = p_m A_n - p_n A_m.
                    matrix_add_term(
                        matrix,
                        row,
                        f"A{nu}",
                        entry_with_poly(entry_scale(eta, coefficient * sigma), p_lower(mu)),
                    )
                    matrix_add_term(
                        matrix,
                        row,
                        f"A{mu}",
                        entry_with_poly(entry_scale(eta, -(coefficient * sigma)), p_lower(nu)),
                    )


def add_bar_spinor_curvature(
    matrix,
    row_prefix: str,
    parameter_kind: str,
    set_index: int,
    bar_sigma_mn,
    coefficient: Exact,
) -> None:
    for dotted in range(2):
        row = f"{row_prefix}{dotted}"
        for contracted in range(2):
            bareta = parameter_component(parameter_kind, set_index, contracted, raised=False)
            for mu in range(4):
                for nu in range(4):
                    sigma = bar_sigma_mn[mu][nu][contracted][dotted]
                    if sigma.is_zero():
                        continue
                    matrix_add_term(
                        matrix,
                        row,
                        f"A{nu}",
                        entry_with_poly(entry_scale(bareta, coefficient * sigma), p_lower(mu)),
                    )
                    matrix_add_term(
                        matrix,
                        row,
                        f"A{mu}",
                        entry_with_poly(entry_scale(bareta, -(coefficient * sigma)), p_lower(nu)),
                    )


def build_lorentz_transform(set_index: int, *, corrected_tilde_f_sign: bool = True):
    matrix = zero_matrix()

    # Scalars.
    for a in range(2):
        for b in range(2):
            matrix_add_term(
                matrix,
                "phi",
                f"psi{b}",
                entry_scale(parameter_component("e", set_index, a, raised=True), -SQRT_TWO if a == b else ZERO),
            )
            matrix_add_term(
                matrix,
                "phi",
                f"lambda{b}",
                entry_scale(parameter_component("n", set_index, a, raised=True), -SQRT_TWO if a == b else ZERO),
            )
            # barred contraction uses lower parameter and raised field.
            coefficient = EPSILON_UPPER[a][b]
            if not coefficient.is_zero():
                matrix_add_term(matrix, "tphi", f"tpsi{b}", entry_scale(parameter_component("be", set_index, a), -SQRT_TWO * coefficient))
                matrix_add_term(matrix, "tphi", f"tlambda{b}", entry_scale(parameter_component("bn", set_index, a), -SQRT_TWO * coefficient))

    # Gauge potential: manifest plus hidden.
    for mu in range(4):
        sigma_down = sigma_lower_lorentz(mu)
        bar_sigma_down = bar_sigma_lower_lorentz(mu)
        for a in range(2):
            eps_up = parameter_component("e", set_index, a, raised=True)
            eta_up = parameter_component("n", set_index, a, raised=True)
            for dot in range(2):
                for lower_dot in range(2):
                    raise_field = EPSILON_UPPER[dot][lower_dot]
                    if not raise_field.is_zero():
                        matrix_add_term(matrix, f"A{mu}", f"tlambda{lower_dot}", entry_scale(eps_up, MINUS_I * sigma_down[a][dot] * raise_field))
                        matrix_add_term(matrix, f"A{mu}", f"tpsi{lower_dot}", entry_scale(eta_up, I * sigma_down[a][dot] * raise_field))
        for dot in range(2):
            bareps = parameter_component("be", set_index, dot)
            for a in range(2):
                matrix_add_term(matrix, f"A{mu}", f"lambda{a}", entry_scale(bareps, MINUS_I * bar_sigma_down[dot][a]))
        # -i psi^a sigma_a dot bar_eta^dot; parameter-first adds one odd swap.
        for dot in range(2):
            bareta_up = parameter_component("bn", set_index, dot, raised=True)
            for a in range(2):
                for lower_a in range(2):
                    raise_field = EPSILON_UPPER[a][lower_a]
                    if not raise_field.is_zero():
                        matrix_add_term(matrix, f"A{mu}", f"psi{lower_a}", entry_scale(bareta_up, I * sigma_down[a][dot] * raise_field))

    # Manifest vector fermions.
    add_spinor_curvature(matrix, "lambda", "e", set_index, SIGMA_MUNU_L, ONE)
    add_bar_spinor_curvature(matrix, "tlambda", "be", set_index, BAR_SIGMA_MUNU_L, MINUS_ONE)
    for a in range(2):
        matrix_add_term(matrix, f"lambda{a}", "D", entry_scale(parameter_component("e", set_index, a), MINUS_I))
        matrix_add_term(matrix, f"tlambda{a}", "D", entry_scale(parameter_component("be", set_index, a), I))

    # Manifest adjoint chiral fermions.
    for a in range(2):
        matrix_add_term(matrix, f"psi{a}", "F", entry_scale(parameter_component("e", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"tpsi{a}", "tF", entry_scale(parameter_component("be", set_index, a), -SQRT_TWO))
        for dot in range(2):
            bareps_up = parameter_component("be", set_index, dot, raised=True)
            for mu in range(4):
                matrix_add_term(matrix, f"psi{a}", "phi", entry_with_poly(entry_scale(bareps_up, I * SQRT_TWO * SIGMA_L[mu][a][dot]), p_lower(mu)))
        for up in range(2):
            eps_up = parameter_component("e", set_index, up, raised=True)
            for mu in range(4):
                matrix_add_term(matrix, f"tpsi{a}", "tphi", entry_with_poly(entry_scale(eps_up, -I * SQRT_TWO * SIGMA_L[mu][up][a]), p_lower(mu)))

    # Hidden fermions.
    for a in range(2):
        matrix_add_term(matrix, f"lambda{a}", "tF", entry_scale(parameter_component("n", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"psi{a}", "D", entry_scale(parameter_component("n", set_index, a), MINUS_I))
        matrix_add_term(matrix, f"tlambda{a}", "F", entry_scale(parameter_component("bn", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"tpsi{a}", "D", entry_scale(parameter_component("bn", set_index, a), I))
        for dot in range(2):
            bareta_up = parameter_component("bn", set_index, dot, raised=True)
            for mu in range(4):
                matrix_add_term(matrix, f"lambda{a}", "phi", entry_with_poly(entry_scale(bareta_up, I * SQRT_TWO * SIGMA_L[mu][a][dot]), p_lower(mu)))
        for up in range(2):
            eta_up = parameter_component("n", set_index, up, raised=True)
            for mu in range(4):
                matrix_add_term(matrix, f"tlambda{a}", "tphi", entry_with_poly(entry_scale(eta_up, -I * SQRT_TWO * SIGMA_L[mu][up][a]), p_lower(mu)))
    add_spinor_curvature(matrix, "psi", "n", set_index, SIGMA_MUNU_L, MINUS_ONE)
    add_bar_spinor_curvature(matrix, "tpsi", "bn", set_index, BAR_SIGMA_MUNU_L, ONE)

    # Manifest F, tF and D.  Parameter-first ordering is explicit.
    for dot in range(2):
        bareps_up = parameter_component("be", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_psi = EPSILON_UPPER[up][lower]
                if raise_psi.is_zero():
                    continue
                for mu in range(4):
                    # Step 4A (4A.15): the ordered coefficient is
                    # +i sqrt(2) (sigma^mu)^a_dot b bar-epsilon^dot b d_mu psi_a.
                    matrix_add_term(matrix, "F", f"psi{lower}", entry_with_poly(entry_scale(bareps_up, I * SQRT_TWO * SIGMA_L[mu][up][dot] * raise_psi), p_lower(mu)))
    for up in range(2):
        eps_up = parameter_component("e", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tpsi = EPSILON_UPPER[dot][lower_dot]
                if raise_tpsi.is_zero():
                    continue
                for mu in range(4):
                    tilde_f_coefficient = I if corrected_tilde_f_sign else MINUS_I
                    matrix_add_term(matrix, "tF", f"tpsi{lower_dot}", entry_with_poly(entry_scale(eps_up, tilde_f_coefficient * SQRT_TWO * SIGMA_L[mu][up][dot] * raise_tpsi), p_lower(mu)))
    for up in range(2):
        eps_up = parameter_component("e", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tlambda = EPSILON_UPPER[dot][lower_dot]
                if raise_tlambda.is_zero():
                    continue
                for mu in range(4):
                    matrix_add_term(matrix, "D", f"tlambda{lower_dot}", entry_with_poly(entry_scale(eps_up, -SIGMA_L[mu][up][dot] * raise_tlambda), p_lower(mu)))
    for dot in range(2):
        bareps = parameter_component("be", set_index, dot)
        for a in range(2):
            for mu in range(4):
                matrix_add_term(matrix, "D", f"lambda{a}", entry_with_poly(entry_scale(bareps, BAR_SIGMA_L[mu][dot][a]), p_lower(mu)))

    # Hidden F, tF and D.
    for up in range(2):
        eta_up = parameter_component("n", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tlambda = EPSILON_UPPER[dot][lower_dot]
                if raise_tlambda.is_zero():
                    continue
                for mu in range(4):
                    matrix_add_term(matrix, "F", f"tlambda{lower_dot}", entry_with_poly(entry_scale(eta_up, I * SQRT_TWO * SIGMA_L[mu][up][dot] * raise_tlambda), p_lower(mu)))
    for dot in range(2):
        bareta_up = parameter_component("bn", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_lambda = EPSILON_UPPER[up][lower]
                if raise_lambda.is_zero():
                    continue
                for mu in range(4):
                    # -(D lambda) sigma bar_eta; one odd swap makes +.
                    matrix_add_term(matrix, "tF", f"lambda{lower}", entry_with_poly(entry_scale(bareta_up, I * SQRT_TWO * SIGMA_L[mu][up][dot] * raise_lambda), p_lower(mu)))
    for up in range(2):
        eta_up = parameter_component("n", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tpsi = EPSILON_UPPER[dot][lower_dot]
                if raise_tpsi.is_zero():
                    continue
                for mu in range(4):
                    matrix_add_term(matrix, "D", f"tpsi{lower_dot}", entry_with_poly(entry_scale(eta_up, -SIGMA_L[mu][up][dot] * raise_tpsi), p_lower(mu)))
    for dot in range(2):
        bareta_up = parameter_component("bn", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_psi = EPSILON_UPPER[up][lower]
                if raise_psi.is_zero():
                    continue
                for mu in range(4):
                    # -(D psi) sigma bar_eta; parameter-first adds a minus.
                    matrix_add_term(matrix, "D", f"psi{lower}", entry_with_poly(entry_scale(bareta_up, SIGMA_L[mu][up][dot] * raise_psi), p_lower(mu)))

    return matrix


def build_euclidean_transform(set_index: int):
    """The corrected direct Euclidean rules (4B.33b)--(4B.35)."""

    matrix = zero_matrix()

    # Scalars.
    for a in range(2):
        for b in range(2):
            diagonal = ONE if a == b else ZERO
            matrix_add_term(matrix, "phi", f"psi{b}", entry_scale(parameter_component("e", set_index, a, raised=True), -SQRT_TWO * diagonal))
            matrix_add_term(matrix, "phi", f"lambda{b}", entry_scale(parameter_component("n", set_index, a, raised=True), -SQRT_TWO * diagonal))
            coefficient = EPSILON_UPPER[a][b]
            if not coefficient.is_zero():
                matrix_add_term(matrix, "tphi", f"tpsi{b}", entry_scale(parameter_component("be", set_index, a), -SQRT_TWO * coefficient))
                matrix_add_term(matrix, "tphi", f"tlambda{b}", entry_scale(parameter_component("bn", set_index, a), -SQRT_TWO * coefficient))

    # Gauge potential.
    for m in range(4):
        for a in range(2):
            eps_up = parameter_component("e", set_index, a, raised=True)
            eta_up = parameter_component("n", set_index, a, raised=True)
            for dot in range(2):
                for lower_dot in range(2):
                    raise_field = EPSILON_UPPER[dot][lower_dot]
                    if raise_field.is_zero():
                        continue
                    matrix_add_term(matrix, f"A{m}", f"tlambda{lower_dot}", entry_scale(eps_up, SIGMA_E[m][a][dot] * raise_field))
                    matrix_add_term(matrix, f"A{m}", f"tpsi{lower_dot}", entry_scale(eta_up, -SIGMA_E[m][a][dot] * raise_field))
        for dot in range(2):
            bareps = parameter_component("be", set_index, dot)
            for a in range(2):
                matrix_add_term(matrix, f"A{m}", f"lambda{a}", entry_scale(bareps, BAR_SIGMA_E[m][dot][a]))
        # +psi sigma_m bar-eta becomes -bar-eta psi in parameter-first order.
        for dot in range(2):
            bareta_up = parameter_component("bn", set_index, dot, raised=True)
            for a in range(2):
                for lower_a in range(2):
                    raise_field = EPSILON_UPPER[a][lower_a]
                    if raise_field.is_zero():
                        continue
                    matrix_add_term(matrix, f"A{m}", f"psi{lower_a}", entry_scale(bareta_up, -SIGMA_E[m][a][dot] * raise_field))

    # Manifest vector and matter fermions.
    add_spinor_curvature(matrix, "lambda", "e", set_index, SIGMA_MN_E, MINUS_ONE)
    add_bar_spinor_curvature(matrix, "tlambda", "be", set_index, BAR_SIGMA_MN_E, ONE)
    for a in range(2):
        matrix_add_term(matrix, f"lambda{a}", "D", entry_scale(parameter_component("e", set_index, a), MINUS_I))
        matrix_add_term(matrix, f"tlambda{a}", "D", entry_scale(parameter_component("be", set_index, a), I))
        matrix_add_term(matrix, f"psi{a}", "F", entry_scale(parameter_component("e", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"tpsi{a}", "tF", entry_scale(parameter_component("be", set_index, a), -SQRT_TWO))
        for dot in range(2):
            bareps_up = parameter_component("be", set_index, dot, raised=True)
            for m in range(4):
                matrix_add_term(matrix, f"psi{a}", "phi", entry_with_poly(entry_scale(bareps_up, -SQRT_TWO * SIGMA_E[m][a][dot]), p_lower(m)))
        for up in range(2):
            eps_up = parameter_component("e", set_index, up, raised=True)
            for m in range(4):
                matrix_add_term(matrix, f"tpsi{a}", "tphi", entry_with_poly(entry_scale(eps_up, SQRT_TWO * SIGMA_E[m][up][a]), p_lower(m)))

    # Hidden fermions.
    for a in range(2):
        matrix_add_term(matrix, f"lambda{a}", "tF", entry_scale(parameter_component("n", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"psi{a}", "D", entry_scale(parameter_component("n", set_index, a), MINUS_I))
        matrix_add_term(matrix, f"tlambda{a}", "F", entry_scale(parameter_component("bn", set_index, a), -SQRT_TWO))
        matrix_add_term(matrix, f"tpsi{a}", "D", entry_scale(parameter_component("bn", set_index, a), I))
        for dot in range(2):
            bareta_up = parameter_component("bn", set_index, dot, raised=True)
            for m in range(4):
                matrix_add_term(matrix, f"lambda{a}", "phi", entry_with_poly(entry_scale(bareta_up, -SQRT_TWO * SIGMA_E[m][a][dot]), p_lower(m)))
        for up in range(2):
            eta_up = parameter_component("n", set_index, up, raised=True)
            for m in range(4):
                matrix_add_term(matrix, f"tlambda{a}", "tphi", entry_with_poly(entry_scale(eta_up, SQRT_TWO * SIGMA_E[m][up][a]), p_lower(m)))
    add_spinor_curvature(matrix, "psi", "n", set_index, SIGMA_MN_E, ONE)
    add_bar_spinor_curvature(matrix, "tpsi", "bn", set_index, BAR_SIGMA_MN_E, MINUS_ONE)

    # Manifest top slots.  The accepted Wick partner of +i sqrt(2) in
    # Lorentzian signature is -sqrt(2) here.
    for dot in range(2):
        bareps_up = parameter_component("be", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_psi = EPSILON_UPPER[up][lower]
                if raise_psi.is_zero():
                    continue
                for m in range(4):
                    matrix_add_term(matrix, "F", f"psi{lower}", entry_with_poly(entry_scale(bareps_up, -SQRT_TWO * SIGMA_E[m][up][dot] * raise_psi), p_lower(m)))
    for up in range(2):
        eps_up = parameter_component("e", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tpsi = EPSILON_UPPER[dot][lower_dot]
                if raise_tpsi.is_zero():
                    continue
                for m in range(4):
                    matrix_add_term(matrix, "tF", f"tpsi{lower_dot}", entry_with_poly(entry_scale(eps_up, -SQRT_TWO * SIGMA_E[m][up][dot] * raise_tpsi), p_lower(m)))
    for up in range(2):
        eps_up = parameter_component("e", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tlambda = EPSILON_UPPER[dot][lower_dot]
                if raise_tlambda.is_zero():
                    continue
                for m in range(4):
                    matrix_add_term(matrix, "D", f"tlambda{lower_dot}", entry_with_poly(entry_scale(eps_up, -I * SIGMA_E[m][up][dot] * raise_tlambda), p_lower(m)))
    for dot in range(2):
        bareps = parameter_component("be", set_index, dot)
        for a in range(2):
            for m in range(4):
                matrix_add_term(matrix, "D", f"lambda{a}", entry_with_poly(entry_scale(bareps, I * BAR_SIGMA_E[m][dot][a]), p_lower(m)))

    # Hidden top slots.
    for up in range(2):
        eta_up = parameter_component("n", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tlambda = EPSILON_UPPER[dot][lower_dot]
                if raise_tlambda.is_zero():
                    continue
                for m in range(4):
                    matrix_add_term(matrix, "F", f"tlambda{lower_dot}", entry_with_poly(entry_scale(eta_up, -SQRT_TWO * SIGMA_E[m][up][dot] * raise_tlambda), p_lower(m)))
    for dot in range(2):
        bareta_up = parameter_component("bn", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_lambda = EPSILON_UPPER[up][lower]
                if raise_lambda.is_zero():
                    continue
                for m in range(4):
                    # +(D lambda) sigma bar-eta becomes -bar-eta sigma D lambda.
                    matrix_add_term(matrix, "tF", f"lambda{lower}", entry_with_poly(entry_scale(bareta_up, -SQRT_TWO * SIGMA_E[m][up][dot] * raise_lambda), p_lower(m)))
    for up in range(2):
        eta_up = parameter_component("n", set_index, up, raised=True)
        for dot in range(2):
            for lower_dot in range(2):
                raise_tpsi = EPSILON_UPPER[dot][lower_dot]
                if raise_tpsi.is_zero():
                    continue
                for m in range(4):
                    matrix_add_term(matrix, "D", f"tpsi{lower_dot}", entry_with_poly(entry_scale(eta_up, -I * SIGMA_E[m][up][dot] * raise_tpsi), p_lower(m)))
    for dot in range(2):
        bareta_up = parameter_component("bn", set_index, dot, raised=True)
        for up in range(2):
            for lower in range(2):
                raise_psi = EPSILON_UPPER[up][lower]
                if raise_psi.is_zero():
                    continue
                for m in range(4):
                    # -i(D psi)sigma bar-eta becomes +i bar-eta sigma D psi.
                    matrix_add_term(matrix, "D", f"psi{lower}", entry_with_poly(entry_scale(bareta_up, I * SIGMA_E[m][up][dot] * raise_psi), p_lower(m)))

    return matrix


def bilinear(
    left_kind: str,
    left_set: int,
    matrix,
    right_kind: str,
    right_set: int,
    coefficient: Exact = ONE,
) -> Entry:
    result: Entry = {}
    for a in range(2):
        left = parameter_component(left_kind, left_set, a, raised=True)
        for dot in range(2):
            right = parameter_component(right_kind, right_set, dot, raised=True)
            result = entry_add(
                result,
                multiply_parameter_forms(left, right, coefficient * matrix[a][dot]),
            )
    return result


def spinor_contraction(left_kind: str, left_set: int, right_kind: str, right_set: int) -> Entry:
    result: Entry = {}
    for a in range(2):
        result = entry_add(
            result,
            multiply_parameter_forms(
                parameter_component(left_kind, left_set, a, raised=True),
                parameter_component(right_kind, right_set, a, raised=False),
            ),
        )
    return result


def barred_contraction(left_kind: str, left_set: int, right_kind: str, right_set: int) -> Entry:
    result: Entry = {}
    for dot in range(2):
        result = entry_add(
            result,
            multiply_parameter_forms(
                parameter_component(left_kind, left_set, dot, raised=False),
                parameter_component(right_kind, right_set, dot, raised=True),
            ),
        )
    return result


def expected_lorentz_closure():
    expected = zero_matrix()
    velocity: list[Entry] = []
    for mu in range(4):
        value = entry_add(
            bilinear("e", 1, SIGMA_L[mu], "be", 2, TWO * I),
            bilinear("e", 2, SIGMA_L[mu], "be", 1, -TWO * I),
        )
        value = entry_add(value, bilinear("n", 1, SIGMA_L[mu], "bn", 2, TWO * I))
        value = entry_add(value, bilinear("n", 2, SIGMA_L[mu], "bn", 1, -TWO * I))
        velocity.append(value)

    omega_tphi = entry_add(
        spinor_contraction("e", 1, "n", 2),
        entry_scale(spinor_contraction("e", 2, "n", 1), MINUS_ONE),
    )
    omega_tphi = entry_scale(omega_tphi, TWO * SQRT_TWO)
    omega_phi = entry_add(
        barred_contraction("be", 1, "bn", 2),
        entry_scale(barred_contraction("be", 2, "bn", 1), MINUS_ONE),
    )
    omega_phi = entry_scale(omega_phi, TWO * SQRT_TWO)

    for field in FIELDS:
        if field.startswith("A"):
            continue
        diagonal: Entry = {}
        for mu in range(4):
            diagonal = entry_add(diagonal, entry_with_poly(velocity[mu], p_lower(mu)))
        matrix_add_term(expected, field, field, diagonal)

    for mu in range(4):
        # v^nu (p_nu A_mu - p_mu A_nu).
        for nu in range(4):
            matrix_add_term(expected, f"A{mu}", f"A{mu}", entry_with_poly(velocity[nu], p_lower(nu)))
            matrix_add_term(expected, f"A{mu}", f"A{nu}", entry_with_poly(entry_scale(velocity[nu], MINUS_ONE), p_lower(mu)))
        matrix_add_term(expected, f"A{mu}", "tphi", entry_with_poly(omega_tphi, p_lower(mu)))
        matrix_add_term(expected, f"A{mu}", "phi", entry_with_poly(omega_phi, p_lower(mu)))
    return expected


def expected_euclidean_closure():
    expected = zero_matrix()
    velocity: list[Entry] = []
    for m in range(4):
        value = entry_add(
            bilinear("e", 1, SIGMA_E[m], "be", 2, -TWO),
            bilinear("e", 2, SIGMA_E[m], "be", 1, TWO),
        )
        value = entry_add(value, bilinear("n", 1, SIGMA_E[m], "bn", 2, -TWO))
        value = entry_add(value, bilinear("n", 2, SIGMA_E[m], "bn", 1, TWO))
        velocity.append(value)

    omega_tphi = entry_add(
        spinor_contraction("e", 1, "n", 2),
        entry_scale(spinor_contraction("e", 2, "n", 1), MINUS_ONE),
    )
    omega_tphi = entry_scale(omega_tphi, TWO * SQRT_TWO)
    omega_phi = entry_add(
        barred_contraction("be", 1, "bn", 2),
        entry_scale(barred_contraction("be", 2, "bn", 1), MINUS_ONE),
    )
    omega_phi = entry_scale(omega_phi, TWO * SQRT_TWO)

    for field in FIELDS:
        if field.startswith("A"):
            continue
        diagonal: Entry = {}
        for m in range(4):
            diagonal = entry_add(diagonal, entry_with_poly(velocity[m], p_lower(m)))
        matrix_add_term(expected, field, field, diagonal)

    for m in range(4):
        for n in range(4):
            matrix_add_term(expected, f"A{m}", f"A{m}", entry_with_poly(velocity[n], p_lower(n)))
            matrix_add_term(expected, f"A{m}", f"A{n}", entry_with_poly(entry_scale(velocity[n], MINUS_ONE), p_lower(m)))
        matrix_add_term(expected, f"A{m}", "tphi", entry_with_poly(omega_tphi, p_lower(m)))
        matrix_add_term(expected, f"A{m}", "phi", entry_with_poly(omega_phi, p_lower(m)))
    return expected


def serialize_poly(poly: Poly) -> dict[str, str]:
    return {
        "p" + "".join(str(power) for power in monomial): exact_string(coefficient)
        for monomial, coefficient in sorted(poly.items())
    }


def serialize_entry(entry: Entry) -> dict[str, dict[str, str]]:
    return {" ".join(monomial): serialize_poly(poly) for monomial, poly in sorted(entry.items())}


def matrix_residual(actual, expected):
    failures = []
    residual_rows = []
    difference = matrix_subtract_entries(actual, expected)
    for row, row_field in enumerate(FIELDS):
        for column, column_field in enumerate(FIELDS):
            if difference[row][column]:
                failures.append(f"{row_field}<-{column_field}")
                if len(residual_rows) < 24:
                    residual_rows.append(
                        {
                            "output": row_field,
                            "input": column_field,
                            "residual": serialize_entry(difference[row][column]),
                        }
                    )
    return failures, residual_rows


# ---------------------------------------------------------------------------
# Constant non-Abelian interaction gate.
#
# The free matrix checker proves every derivative/sigma coefficient.  The
# following independent exact supercommutative polynomial calculation sets
# spacetime derivatives and F_mn to zero and uses c_AB^C=epsilon_AB^C.  It
# checks all scalar, fermion, auxiliary, H, and Y interaction terms against
# the claimed field-dependent gauge transformation.  This is an exact
# necessary Lie/Jacobi witness, not a proof for every Lie algebra.

GMonomial = tuple[str, ...]
GExpression = dict[GMonomial, Exact]


def generator_parity(name: str) -> int:
    if name[0] in {"e", "b", "n", "m"} and name[1:].isdigit():
        return 1
    # Covariant first jets have names such as dpsi0m2c1.  A spacetime
    # derivative is even, hence the jet has the parity of its base field.
    base_name = name[1:] if name.startswith("d") else name
    return int(base_name.startswith(("lambda", "tlambda", "psi", "tpsi")))


def g_normalize(value: GExpression) -> GExpression:
    return {key: coefficient for key, coefficient in value.items() if not coefficient.is_zero()}


def g_add(left: GExpression, right: GExpression) -> GExpression:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, ZERO) + coefficient
    return g_normalize(result)


def g_scale(value: GExpression, coefficient: Exact) -> GExpression:
    return g_normalize({key: coefficient * term for key, term in value.items()})


def g_monomial_multiply(left: GMonomial, right: GMonomial):
    combined = list(left + right)
    odd = [name for name in combined if generator_parity(name)]
    if len(set(odd)) != len(odd):
        return 0, ()
    inversions = sum(
        generator_parity(combined[i])
        and generator_parity(combined[j])
        and combined[i] > combined[j]
        for i in range(len(combined))
        for j in range(i + 1, len(combined))
    )
    return (-1 if inversions % 2 else 1), tuple(sorted(combined))


def g_multiply(left: GExpression, right: GExpression) -> GExpression:
    result: GExpression = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            sign, monomial = g_monomial_multiply(left_monomial, right_monomial)
            if sign == 0:
                continue
            coefficient = left_coefficient * right_coefficient
            if sign == -1:
                coefficient = -coefficient
            result[monomial] = result.get(monomial, ZERO) + coefficient
    return g_normalize(result)


def g_generator(name: str, coefficient: Exact = ONE) -> GExpression:
    return {(name,): coefficient}


def epsilon3_value(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    values = (a, b, c)
    inversions = sum(values[i] > values[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def g_cross(left: list[GExpression], right: list[GExpression]) -> list[GExpression]:
    result = [{}, {}, {}]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                sign = epsilon3_value(b, c, a)
                if sign:
                    result[a] = g_add(
                        result[a],
                        g_scale(g_multiply(left[b], right[c]), Exact.rational(sign)),
                    )
    return result


def g_bracket(left: list[GExpression], right: list[GExpression]) -> list[GExpression]:
    return [g_scale(value, I) for value in g_cross(left, right)]


def g_vector(prefix: str, spinor: int | None = None) -> list[GExpression]:
    suffix = "" if spinor is None else str(spinor)
    return [g_generator(f"{prefix}{suffix}c{color}") for color in range(3)]


def g_parameter(kind: str, set_index: int, component: int, raised: bool = False) -> GExpression:
    prefix = {"e": "e", "be": "b", "n": "n", "bn": "m"}[kind]
    if not raised:
        return g_generator(f"{prefix}{set_index}{component}")
    result: GExpression = {}
    for lower in range(2):
        coefficient = EPSILON_UPPER[component][lower]
        if not coefficient.is_zero():
            result = g_add(result, g_generator(f"{prefix}{set_index}{lower}", coefficient))
    return result


def g_contract_parameter_fermion(kind: str, set_index: int, prefix: str):
    result = [{}, {}, {}]
    for spinor in range(2):
        parameter_value = g_parameter(kind, set_index, spinor, raised=True)
        field = g_vector(prefix, spinor)
        for color in range(3):
            result[color] = g_add(result[color], g_multiply(parameter_value, field[color]))
    return result


def g_bar_contract_parameter_fermion(kind: str, set_index: int, prefix: str):
    result = [{}, {}, {}]
    for dotted in range(2):
        parameter_value = g_parameter(kind, set_index, dotted, raised=False)
        for raised_dot in range(2):
            coefficient = EPSILON_UPPER[dotted][raised_dot]
            if coefficient.is_zero():
                continue
            field = g_vector(prefix, raised_dot)
            for color in range(3):
                result[color] = g_add(
                    result[color],
                    g_scale(g_multiply(parameter_value, field[color]), coefficient),
                )
    return result


NONABELIAN_FIELDS = (
    "phi",
    "tphi",
    "lambda0",
    "lambda1",
    "tlambda0",
    "tlambda1",
    "psi0",
    "psi1",
    "tpsi0",
    "tpsi1",
    "F",
    "tF",
    "D",
)


def displayed_nonlinear_coefficients():
    return {
        "psi_mu": Exact.rational(-2) * I,
        "tpsi_mu": Exact.rational(2) * I,
        "manifest_F": Exact.rational(-2) * I,
        "manifest_tF": Exact.rational(-2) * I,
        "hidden_F": Exact.rational(2) * I,
        "hidden_tF": Exact.rational(2) * I,
        "hidden_D_left": TWO * SQRT_TWO,
        "hidden_D_right": TWO * SQRT_TWO,
    }


def build_constant_nonabelian_variations(set_index: int, coefficients=None):
    """Deprecated non-covariant truncation retained only as a diagnostic."""

    coefficients = coefficients or displayed_nonlinear_coefficients()
    variations: dict[str, list[GExpression]] = {
        field: [{}, {}, {}] for field in NONABELIAN_FIELDS
    }
    phi = g_vector("phi")
    tphi = g_vector("tphi")
    mu = g_bracket(phi, tphi)

    eps_psi = g_contract_parameter_fermion("e", set_index, "psi")
    eta_lambda = g_contract_parameter_fermion("n", set_index, "lambda")
    beps_tpsi = g_bar_contract_parameter_fermion("be", set_index, "tpsi")
    beta_tlambda = g_bar_contract_parameter_fermion("bn", set_index, "tlambda")
    for color in range(3):
        variations["phi"][color] = g_scale(g_add(eps_psi[color], eta_lambda[color]), -SQRT_TWO)
        variations["tphi"][color] = g_scale(g_add(beps_tpsi[color], beta_tlambda[color]), -SQRT_TWO)

    # Fermions at D_mu=F_mu_nu=0.
    for spinor in range(2):
        eps = g_parameter("e", set_index, spinor)
        eta = g_parameter("n", set_index, spinor)
        beps = g_parameter("be", set_index, spinor)
        beta = g_parameter("bn", set_index, spinor)
        Fv, tFv, Dv = g_vector("F"), g_vector("tF"), g_vector("D")
        for color in range(3):
            variations[f"psi{spinor}"][color] = g_add(
                g_scale(g_multiply(eps, Fv[color]), -SQRT_TWO),
                g_add(
                    g_scale(g_multiply(eta, Dv[color]), MINUS_I),
                    g_scale(g_multiply(eta, mu[color]), coefficients["psi_mu"]),
                ),
            )
            variations[f"lambda{spinor}"][color] = g_add(
                g_scale(g_multiply(eps, Dv[color]), MINUS_I),
                g_scale(g_multiply(eta, tFv[color]), -SQRT_TWO),
            )
            variations[f"tpsi{spinor}"][color] = g_add(
                g_scale(g_multiply(beps, tFv[color]), -SQRT_TWO),
                g_add(
                    g_scale(g_multiply(beta, Dv[color]), I),
                    g_scale(g_multiply(beta, mu[color]), coefficients["tpsi_mu"]),
                ),
            )
            variations[f"tlambda{spinor}"][color] = g_add(
                g_scale(g_multiply(beps, Dv[color]), I),
                g_scale(g_multiply(beta, Fv[color]), -SQRT_TWO),
            )

    # Top slots.  Every double bracket is i times the SU(2) cross product.
    beps_tlambda = g_bar_contract_parameter_fermion("be", set_index, "tlambda")
    eps_lambda = g_contract_parameter_fermion("e", set_index, "lambda")
    eta_psi = g_contract_parameter_fermion("n", set_index, "psi")
    beta_tpsi = g_bar_contract_parameter_fermion("bn", set_index, "tpsi")
    manifest_F = g_bracket(beps_tlambda, phi)
    manifest_tF = g_bracket(eps_lambda, tphi)
    hidden_F = g_bracket(eta_psi, tphi)
    hidden_tF = g_bracket(beta_tpsi, phi)
    hidden_D_left = g_bracket(eta_lambda, tphi)
    hidden_D_right = g_bracket(phi, beta_tlambda)
    for color in range(3):
        variations["F"][color] = g_add(
            g_scale(manifest_F[color], coefficients["manifest_F"]),
            g_scale(hidden_F[color], coefficients["hidden_F"]),
        )
        variations["tF"][color] = g_add(
            g_scale(manifest_tF[color], coefficients["manifest_tF"]),
            g_scale(hidden_tF[color], coefficients["hidden_tF"]),
        )
        variations["D"][color] = g_add(
            g_scale(hidden_D_left[color], coefficients["hidden_D_left"]),
            g_scale(hidden_D_right[color], coefficients["hidden_D_right"]),
        )
    return variations


def g_parameter_from_entry_name(name: str) -> GExpression:
    """Translate free-check names such as 1e0 into interaction names e10."""

    if len(name) != 3 or name[0] not in "12" or name[1] not in "ebnm" or name[2] not in "01":
        raise ValueError(f"unexpected supersymmetry parameter generator: {name}")
    return g_generator(f"{name[1]}{name[0]}{name[2]}")


def build_covariant_constant_nonabelian_variations(
    set_index: int,
    coefficients=None,
    *,
    corrected_tilde_f_sign: bool = True,
):
    """Transformations on the A=partial(field)=0 covariant first-jet fiber.

    A covariant derivative vanishes at the selected background, but its
    variation does not:

        delta(D_mu X) = D_mu(delta X) + (delta A_mu) cross X
                      = (delta A_mu) cross X.

    The linear rules are translated directly from the exact free Lorentzian
    transformation matrix, so this gate uses precisely the already-verified
    sigma/index coefficients.  The displayed nonlinear brackets are then
    added without re-entering any linear rule by hand.
    """

    coefficients = coefficients or displayed_nonlinear_coefficients()
    linear = build_lorentz_transform(
        set_index,
        corrected_tilde_f_sign=corrected_tilde_f_sign,
    )
    all_base_fields = tuple(FIELDS)
    variations: dict[str, list[GExpression]] = {
        field: [{}, {}, {}] for field in all_base_fields
    }
    derivative_keys: set[tuple[str, int]] = set()

    for row, output in enumerate(FIELDS):
        for column, input_field in enumerate(FIELDS):
            entry = linear[row][column]
            for odd_monomial, polynomial in entry.items():
                parameter_value: GExpression = {(): ONE}
                for parameter_name in odd_monomial:
                    parameter_value = g_multiply(
                        parameter_value,
                        g_parameter_from_entry_name(parameter_name),
                    )
                for momentum_power, coefficient in polynomial.items():
                    degree = sum(momentum_power)
                    if degree == 0:
                        source_name = input_field
                    elif degree == 1:
                        mu = next(index for index, power in enumerate(momentum_power) if power)
                        # At A=partial(field)=0, delta(partial_mu A_nu)=0 for
                        # constant component fields.  Covariant derivatives of
                        # every adjoint tensor field require the connection
                        # variation and are retained as first-jet generators.
                        if input_field.startswith("A"):
                            continue
                        derivative_keys.add((input_field, mu))
                        source_name = f"d{input_field}m{mu}"
                        variations.setdefault(source_name, [{}, {}, {}])
                    else:
                        raise ValueError(
                            f"nonlinear momentum monomial in first-order transformation: {momentum_power}"
                        )
                    source = g_vector(source_name)
                    for color in range(3):
                        variations[output][color] = g_add(
                            variations[output][color],
                            g_scale(g_multiply(parameter_value, source[color]), coefficient),
                        )

    phi = g_vector("phi")
    tphi = g_vector("tphi")
    mu_value = g_bracket(phi, tphi)

    # Displayed nonlinear terms in (4B.20)--(4B.21a).
    for spinor in range(2):
        eta = g_parameter("n", set_index, spinor)
        beta = g_parameter("bn", set_index, spinor)
        for color in range(3):
            variations[f"psi{spinor}"][color] = g_add(
                variations[f"psi{spinor}"][color],
                g_scale(g_multiply(eta, mu_value[color]), coefficients["psi_mu"]),
            )
            variations[f"tpsi{spinor}"][color] = g_add(
                variations[f"tpsi{spinor}"][color],
                g_scale(g_multiply(beta, mu_value[color]), coefficients["tpsi_mu"]),
            )

    beps_tlambda = g_bar_contract_parameter_fermion("be", set_index, "tlambda")
    eps_lambda = g_contract_parameter_fermion("e", set_index, "lambda")
    eta_psi = g_contract_parameter_fermion("n", set_index, "psi")
    beta_tpsi = g_bar_contract_parameter_fermion("bn", set_index, "tpsi")
    eta_lambda = g_contract_parameter_fermion("n", set_index, "lambda")
    beta_tlambda = g_bar_contract_parameter_fermion("bn", set_index, "tlambda")
    nonlinear_terms = {
        "F": (
            (coefficients["manifest_F"], g_bracket(beps_tlambda, phi)),
            (coefficients["hidden_F"], g_bracket(eta_psi, tphi)),
        ),
        "tF": (
            (coefficients["manifest_tF"], g_bracket(eps_lambda, tphi)),
            (coefficients["hidden_tF"], g_bracket(beta_tpsi, phi)),
        ),
        "D": (
            (coefficients["hidden_D_left"], g_bracket(eta_lambda, tphi)),
            (coefficients["hidden_D_right"], g_bracket(phi, beta_tlambda)),
        ),
    }
    for output, terms in nonlinear_terms.items():
        for coefficient, vector in terms:
            for color in range(3):
                variations[output][color] = g_add(
                    variations[output][color],
                    g_scale(vector[color], coefficient),
                )

    # Covariant-jet transformation at the selected background.
    for field, mu_index in derivative_keys:
        derivative_name = f"d{field}m{mu_index}"
        variations[derivative_name] = g_cross(
            variations[f"A{mu_index}"],
            g_vector(field),
        )
    return variations


def g_apply_variation(
    expression: GExpression,
    variations,
    *,
    incorrectly_treat_delta_as_odd: bool = False,
) -> GExpression:
    """Apply the parameter-included, hence even, supersymmetry variation.

    ``incorrectly_treat_delta_as_odd`` is exposed only for the audit's
    rejected-convention diagnostic.
    """

    result: GExpression = {}
    for monomial, coefficient in expression.items():
        for position, generator in enumerate(monomial):
            if "c" not in generator:
                continue
            prefix, color_text = generator.rsplit("c", 1)
            if prefix not in variations or not color_text.isdigit():
                continue
            replacement = variations[prefix][int(color_text)]
            if not replacement:
                continue
            left = {monomial[:position]: ONE}
            right = {monomial[position + 1 :]: ONE}
            term = g_multiply(g_multiply(left, replacement), right)
            if incorrectly_treat_delta_as_odd and sum(
                generator_parity(item) for item in monomial[:position]
            ) % 2:
                term = g_scale(term, MINUS_ONE)
            result = g_add(result, g_scale(term, coefficient))
    return result


def g_full_parameter_contraction(left_kind: str, left_set: int, right_kind: str, right_set: int):
    result: GExpression = {}
    for spinor in range(2):
        result = g_add(
            result,
            g_multiply(
                g_parameter(left_kind, left_set, spinor, raised=True),
                g_parameter(right_kind, right_set, spinor, raised=False),
            ),
        )
    return result


def g_full_barred_contraction(left_kind: str, left_set: int, right_kind: str, right_set: int):
    result: GExpression = {}
    for dotted in range(2):
        result = g_add(
            result,
            g_multiply(
                g_parameter(left_kind, left_set, dotted, raised=False),
                g_parameter(right_kind, right_set, dotted, raised=True),
            ),
        )
    return result


def constant_nonabelian_omega(
    undotted_scale: Exact = ONE,
    dotted_scale: Exact = ONE,
):
    undotted = g_add(
        g_full_parameter_contraction("e", 1, "n", 2),
        g_scale(g_full_parameter_contraction("e", 2, "n", 1), MINUS_ONE),
    )
    dotted = g_add(
        g_full_barred_contraction("be", 1, "bn", 2),
        g_scale(g_full_barred_contraction("be", 2, "bn", 1), MINUS_ONE),
    )
    phi, tphi = g_vector("phi"), g_vector("tphi")
    return [
        g_scale(
            g_add(
                g_scale(g_multiply(undotted, tphi[color]), undotted_scale),
                g_scale(g_multiply(dotted, phi[color]), dotted_scale),
            ),
            TWO * SQRT_TWO,
        )
        for color in range(3)
    ]


def serialize_gexpression(expression: GExpression):
    return {" ".join(monomial): exact_string(coefficient) for monomial, coefficient in sorted(expression.items())}


def project_constant_background(expression: GExpression) -> GExpression:
    """Set A_mu and all covariant first jets to zero after composition."""

    return {
        monomial: coefficient
        for monomial, coefficient in expression.items()
        if not any(
            generator.startswith("d")
            or (generator.startswith("A") and "c" in generator)
            for generator in monomial
        )
    }


def constant_nonabelian_objects():
    objects: dict[str, list[GExpression]] = {
        field: g_vector(field) for field in (*FIELDS,)
    }
    phi, tphi = objects["phi"], objects["tphi"]
    mu = g_bracket(phi, tphi)
    objects["mu"] = mu
    objects["H"] = [g_add(objects["D"][color], mu[color]) for color in range(3)]
    objects["Y11"] = [g_scale(objects["F"][color], -SQRT_TWO) for color in range(3)]
    objects["Y22"] = [g_scale(objects["tF"][color], -SQRT_TWO) for color in range(3)]
    objects["Y12"] = [g_scale(objects["H"][color], I) for color in range(3)]
    return objects


def constant_covariant_residual_map(
    coefficients=None,
    *,
    corrected_tilde_f_sign: bool = True,
    object_names=None,
    undotted_omega_scale: Exact = ONE,
    dotted_omega_scale: Exact = ONE,
    incorrectly_treat_delta_as_odd: bool = False,
):
    first = build_covariant_constant_nonabelian_variations(
        1,
        coefficients,
        corrected_tilde_f_sign=corrected_tilde_f_sign,
    )
    second = build_covariant_constant_nonabelian_variations(
        2,
        coefficients,
        corrected_tilde_f_sign=corrected_tilde_f_sign,
    )
    omega = constant_nonabelian_omega(
        undotted_omega_scale,
        dotted_omega_scale,
    )
    objects = constant_nonabelian_objects()
    if object_names is None:
        object_names = tuple(objects)
    residual_map: dict[tuple[str, int], GExpression] = {}

    for name in object_names:
        vector = objects[name]
        for color in range(3):
            delta2 = g_apply_variation(
                vector[color],
                second,
                incorrectly_treat_delta_as_odd=incorrectly_treat_delta_as_odd,
            )
            delta1 = g_apply_variation(
                vector[color],
                first,
                incorrectly_treat_delta_as_odd=incorrectly_treat_delta_as_odd,
            )
            actual = project_constant_background(
                g_add(
                    g_apply_variation(
                        delta2,
                        first,
                        incorrectly_treat_delta_as_odd=incorrectly_treat_delta_as_odd,
                    ),
                    g_scale(
                        g_apply_variation(
                            delta1,
                            second,
                            incorrectly_treat_delta_as_odd=incorrectly_treat_delta_as_odd,
                        ),
                        MINUS_ONE,
                    ),
                )
            )
            expected = (
                {}
                if name.startswith("A")
                else g_scale(g_cross(omega, vector)[color], MINUS_ONE)
            )
            residual = g_add(actual, g_scale(expected, MINUS_ONE))
            if residual:
                residual_map[(name, color)] = residual
    return residual_map


def parameter_sector(monomial: GMonomial) -> str:
    parameters = sorted(
        generator[0] + generator[1]
        for generator in monomial
        if len(generator) == 3
        and generator[0] in "ebnm"
        and generator[1:].isdigit()
    )
    return "*".join(parameters)


def classify_g_residuals(residual_map):
    by_object: dict[str, int] = {}
    by_parameter_sector: dict[str, int] = {}
    monomial_count = 0
    for (name, _color), residual in residual_map.items():
        by_object[name] = by_object.get(name, 0) + 1
        for monomial in residual:
            monomial_count += 1
            sector = parameter_sector(monomial)
            by_parameter_sector[sector] = by_parameter_sector.get(sector, 0) + 1
    return {
        "failed_color_entries_by_object": dict(sorted(by_object.items())),
        "parameter_monomials_by_sector": dict(sorted(by_parameter_sector.items())),
        "residual_monomial_count": monomial_count,
    }


def check_constant_nonabelian_interactions(
    coefficients=None,
    *,
    corrected_tilde_f_sign: bool = True,
    incorrectly_treat_delta_as_odd: bool = False,
):
    residual_map = constant_covariant_residual_map(
        coefficients,
        corrected_tilde_f_sign=corrected_tilde_f_sign,
        incorrectly_treat_delta_as_odd=incorrectly_treat_delta_as_odd,
    )
    failures = [f"{name}[{color}]" for name, color in residual_map]
    residuals = [
        {
            "object": name,
            "color": color,
            "residual": serialize_gexpression(residual),
        }
        for (name, color), residual in list(residual_map.items())[:24]
    ]
    return failures, residuals, classify_g_residuals(residual_map)


NORMALIZED_NONLINEAR_NAMES = (
    "psi_mu_over_i",
    "tpsi_mu_over_i",
    "manifest_F_over_i",
    "manifest_tF_over_i",
    "hidden_F_over_i",
    "hidden_tF_over_i",
    "hidden_D_left_over_sqrt2",
    "hidden_D_right_over_sqrt2",
)


def coefficients_from_normalized(values):
    values = tuple(Fraction(value) for value in values)
    if len(values) != 8:
        raise ValueError("eight normalized nonlinear coefficients are required")
    return {
        "psi_mu": I * Exact.rational(values[0]),
        "tpsi_mu": I * Exact.rational(values[1]),
        "manifest_F": I * Exact.rational(values[2]),
        "manifest_tF": I * Exact.rational(values[3]),
        "hidden_F": I * Exact.rational(values[4]),
        "hidden_tF": I * Exact.rational(values[5]),
        "hidden_D_left": SQRT_TWO * Exact.rational(values[6]),
        "hidden_D_right": SQRT_TWO * Exact.rational(values[7]),
    }


def flatten_g_residual_map(residual_map):
    result: dict[tuple[str, int, GMonomial], Exact] = {}
    for (name, color), expression in residual_map.items():
        for monomial, coefficient in expression.items():
            result[(name, color, monomial)] = coefficient
    return result


def rational_rref(rows, variable_count: int):
    matrix = [list(row) for row in rows]
    rank = 0
    pivot_columns: list[int] = []
    for column in range(variable_count):
        pivot = next(
            (
                row
                for row in range(rank, len(matrix))
                if matrix[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or matrix[row][column] == 0:
                continue
            multiplier = matrix[row][column]
            matrix[row] = [
                matrix[row][index] - multiplier * matrix[rank][index]
                for index in range(variable_count + 1)
            ]
        pivot_columns.append(column)
        rank += 1
    inconsistent = any(
        not any(row[:variable_count]) and row[variable_count] != 0
        for row in matrix
    )
    return matrix, pivot_columns, inconsistent


def solve_nonlinear_coefficients_from_fermion_closure():
    """Exact simultaneous solution of all eight displayed nonlinear slots.

    Closure on the eight fermion components is affine in these coefficients.
    Its solution set contains every solution of the full constant-jet system,
    so a full-rank fermion subsystem followed by a full-field check determines
    all branches exactly.
    """

    fermion_objects = (
        "lambda0",
        "lambda1",
        "tlambda0",
        "tlambda1",
        "psi0",
        "psi1",
        "tpsi0",
        "tpsi1",
    )
    zero_values = (Fraction(0),) * 8
    base = flatten_g_residual_map(
        constant_covariant_residual_map(
            coefficients_from_normalized(zero_values),
            object_names=fermion_objects,
        )
    )
    unit_samples = []
    for index in range(8):
        values = list(zero_values)
        values[index] = Fraction(1)
        unit_samples.append(
            flatten_g_residual_map(
                constant_covariant_residual_map(
                    coefficients_from_normalized(values),
                    object_names=fermion_objects,
                )
            )
        )

    keys = set(base)
    for sample in unit_samples:
        keys.update(sample)
    rows = set()
    for key in keys:
        constant = base.get(key, ZERO)
        sensitivities = [
            sample.get(key, ZERO) - constant for sample in unit_samples
        ]
        for basis_name in ("a", "b", "c", "d"):
            row = tuple(
                getattr(sensitivity, basis_name)
                for sensitivity in sensitivities
            ) + (-getattr(constant, basis_name),)
            if any(row):
                rows.add(row)

    reduced, pivots, inconsistent = rational_rref(sorted(rows), 8)
    solution = [None] * 8
    if not inconsistent:
        for row_index, column in enumerate(pivots):
            solution[column] = reduced[row_index][8]
    unique = not inconsistent and len(pivots) == 8

    full_candidate_residual = {}
    if unique:
        full_candidate_residual = constant_covariant_residual_map(
            coefficients_from_normalized(solution)
        )
    return {
        "equation_count_after_exact_deduplication": len(rows),
        "rank": len(pivots),
        "inconsistent": inconsistent,
        "solution_branch_count": 1 if unique and not full_candidate_residual else 0,
        "all_solution_branches": (
            [
                {
                    name: str(solution[index])
                    for index, name in enumerate(NORMALIZED_NONLINEAR_NAMES)
                }
            ]
            if unique and not full_candidate_residual
            else []
        ),
        "full_field_candidate_residual_count": len(full_candidate_residual),
        "interpretation": (
            "The fermion subsystem has full rank eight.  Its unique candidate is "
            "the displayed coefficient vector, and that candidate has zero residual "
            "on A_mu, scalars, all fermions, F, tildeF, D, mu, H, and Y_ij."
        ),
    }


def solve_omega_scales_from_scalar_closure():
    """Solve separate multipliers of the undotted and dotted Omega terms."""

    scalar_objects = ("phi", "tphi")
    samples = []
    for undotted, dotted in ((ZERO, ZERO), (ONE, ZERO), (ZERO, ONE)):
        samples.append(
            flatten_g_residual_map(
                constant_covariant_residual_map(
                    object_names=scalar_objects,
                    undotted_omega_scale=undotted,
                    dotted_omega_scale=dotted,
                )
            )
        )
    base, unit_undotted, unit_dotted = samples
    keys = set(base) | set(unit_undotted) | set(unit_dotted)
    rows = set()
    for key in keys:
        constant = base.get(key, ZERO)
        sensitivities = (
            unit_undotted.get(key, ZERO) - constant,
            unit_dotted.get(key, ZERO) - constant,
        )
        for basis_name in ("a", "b", "c", "d"):
            row = tuple(
                getattr(sensitivity, basis_name)
                for sensitivity in sensitivities
            ) + (-getattr(constant, basis_name),)
            if any(row):
                rows.add(row)
    reduced, pivots, inconsistent = rational_rref(sorted(rows), 2)
    solution = [None, None]
    if not inconsistent:
        for row_index, column in enumerate(pivots):
            solution[column] = reduced[row_index][2]
    return {
        "rank": len(pivots),
        "inconsistent": inconsistent,
        "solution_branch_count": int(not inconsistent and len(pivots) == 2),
        "all_solution_branches": (
            [
                {
                    "undotted_term_multiplier": str(solution[0]),
                    "dotted_term_multiplier": str(solution[1]),
                }
            ]
            if not inconsistent and len(pivots) == 2
            else []
        ),
        "interpretation": (
            "Scalar closure independently fixes both terms of Omega_12 to their "
            "displayed sign and normalization."
        ),
    }


def rejected_noncovariant_quotient_diagnostic():
    """Reproduce the false obstruction from setting D_mu X to zero too early."""

    first = build_constant_nonabelian_variations(1)
    second = build_constant_nonabelian_variations(2)
    omega = constant_nonabelian_omega()
    objects = constant_nonabelian_objects()
    names = (
        *NONABELIAN_FIELDS,
        "mu",
        "H",
        "Y11",
        "Y22",
        "Y12",
    )
    residual_map = {}
    for name in names:
        vector = objects[name]
        for color in range(3):
            delta2 = g_apply_variation(vector[color], second)
            delta1 = g_apply_variation(vector[color], first)
            actual = g_add(
                g_apply_variation(delta2, first),
                g_scale(g_apply_variation(delta1, second), MINUS_ONE),
            )
            expected = g_scale(g_cross(omega, vector)[color], MINUS_ONE)
            residual = g_add(actual, g_scale(expected, MINUS_ONE))
            if residual:
                residual_map[(name, color)] = residual
    return {
        "rejected": True,
        "failed_color_entry_count": len(residual_map),
        "classification": classify_g_residuals(residual_map),
        "reason": (
            "The quotient D_mu X=0 is not invariant under supersymmetry: "
            "delta(D_mu X)=(delta A_mu) cross X remains nonzero.  These residuals "
            "are therefore not closure obstructions."
        ),
    }


def check_lorentz_free_closure(*, corrected_tilde_f_sign: bool = True):
    first = build_lorentz_transform(1, corrected_tilde_f_sign=corrected_tilde_f_sign)
    second = build_lorentz_transform(2, corrected_tilde_f_sign=corrected_tilde_f_sign)
    # delta_1 delta_2 X = M_2 M_1 X for row-vector transformation data.
    actual = matrix_subtract_entries(
        matrix_multiply_entries(second, first),
        matrix_multiply_entries(first, second),
    )
    expected = expected_lorentz_closure()
    return matrix_residual(actual, expected)


def check_euclidean_free_closure():
    first = build_euclidean_transform(1)
    second = build_euclidean_transform(2)
    actual = matrix_subtract_entries(
        matrix_multiply_entries(second, first),
        matrix_multiply_entries(first, second),
    )
    return matrix_residual(actual, expected_euclidean_closure())


def check_offshell_su2_triplet_gate():
    """Exact manifest-slot no-go for an invertible auxiliary triplet map."""

    transform = build_lorentz_transform(1, corrected_tilde_f_sign=True)

    def selected_coefficient(row, column, parameter_name, momentum_power):
        entry = transform[FIELD_INDEX[row]][FIELD_INDEX[column]]
        coefficient = entry.get((parameter_name,), {}).get(momentum_power, ZERO)
        if coefficient.is_zero():
            raise AssertionError(
                f"missing manifest slot {row}<-{column}, "
                f"{parameter_name}, {momentum_power}"
            )
        return coefficient

    p_zero = (0, 0, 0, 0)
    p_time = (1, 0, 0, 0)
    gamma_times_a = selected_coefficient("psi0", "F", "1e0", p_zero)
    gamma_c_over_s_from_gaugino = selected_coefficient(
        "lambda0", "D", "1e0", p_zero
    )
    a_to_derivative_A = selected_coefficient("F", "psi0", "1b0", p_time)
    d_barepsilon_barsigma_dlambda = selected_coefficient(
        "D", "lambda0", "1b0", p_time
    )

    expected_handles = {
        "psi0<-F": -SQRT_TWO,
        "lambda0<-D": MINUS_I,
        "F<-p0 psi0": I * SQRT_TWO,
        "D<-p0 lambda0": ONE,
    }
    extracted_handles = {
        "psi0<-F": gamma_times_a,
        "lambda0<-D": gamma_c_over_s_from_gaugino,
        "F<-p0 psi0": a_to_derivative_A,
        "D<-p0 lambda0": d_barepsilon_barsigma_dlambda,
    }
    if extracted_handles != expected_handles:
        raise AssertionError(
            "manifest slot extraction drift: "
            + str(
                {
                    key: exact_string(value)
                    for key, value in extracted_handles.items()
                }
            )
        )

    # bar-epsilon bar-sigma D lambda = -(D lambda) sigma bar-epsilon.
    field_first_dlambda = -d_barepsilon_barsigma_dlambda
    c_over_A_s_from_symmetric_slot = (
        Exact.rational(Fraction(1, 2)) * field_first_dlambda
    )

    # A=a i sqrt(2), A s/2=-c, gamma a=-sqrt(2).
    gamma_c_over_s_from_triplet = (
        gamma_times_a
        * a_to_derivative_A
        * c_over_A_s_from_symmetric_slot
    )
    residual_coefficient_of_s = (
        gamma_c_over_s_from_triplet - gamma_c_over_s_from_gaugino
    )
    passed = residual_coefficient_of_s.is_zero()

    return {
        "passed": passed,
        "residual_count": 0 if passed else 1,
        "ansatz": {
            "doublet": "chi_1=psi, chi_2=s lambda, zeta^1=epsilon, zeta^2=s^(-1) eta",
            "auxiliary": "Y_11=a F, Y_22=b tildeF, Y_12=c H",
            "invertibility": "s != 0 and a b c != 0",
        },
        "extracted_exact_slot_coefficients": {
            "gamma_times_a": exact_string(gamma_times_a),
            "gamma_c_over_s_from_gaugino": exact_string(
                gamma_c_over_s_from_gaugino
            ),
            "A_over_a_from_delta_F": exact_string(a_to_derivative_A),
            "c_over_A_s_from_symmetric_Y12": exact_string(
                c_over_A_s_from_symmetric_slot
            ),
            "Dlambda_parameter_first": exact_string(
                d_barepsilon_barsigma_dlambda
            ),
            "Dlambda_field_first": exact_string(field_first_dlambda),
        },
        "extraction_handles": {
            "psi0_from_F": "1e0,p0000",
            "lambda0_from_D": "1e0,p0000",
            "F_from_psi0": "1b0,p1000",
            "D_from_lambda0": "1b0,p1000",
        },
        "derived_exact_coefficients": {
            "gamma_c_over_s_from_triplet": exact_string(
                gamma_c_over_s_from_triplet
            ),
            "residual_coefficient_of_s": exact_string(
                residual_coefficient_of_s
            ),
        },
        "equations": {
            "gaugino": (
                "gamma*c/s="
                + exact_string(gamma_c_over_s_from_gaugino)
            ),
            "symmetric_triplet": (
                "gamma*c/s="
                + exact_string(gamma_c_over_s_from_triplet)
            ),
        },
        "conclusion": (
            "residual*s=0 contradicts s!=0"
            if not passed
            else "no manifest-slot obstruction"
        ),
        "on_shell_boundary": (
            "After F=tildeF=H=0 the displayed physical-field rules admit a "
            "componentwise SU(2)_R-covariant rewriting.  On-shell algebra closure "
            "was not machine-checked and is not claimed."
        ),
        "scope_boundary": (
            "This gate excludes only the declared linear invertible doublet/triplet "
            "packaging.  It does not exclude nonlinear or field-dependent alternatives."
        ),
    }


def run_checks():
    lorentz_failures, lorentz_residuals = check_lorentz_free_closure()
    euclidean_failures, euclidean_residuals = check_euclidean_free_closure()
    (
        nonabelian_failures,
        nonabelian_residuals,
        nonabelian_classification,
    ) = check_constant_nonabelian_interactions()
    legacy_failures, legacy_residuals = check_lorentz_free_closure(
        corrected_tilde_f_sign=False
    )
    (
        legacy_interaction_failures,
        legacy_interaction_residuals,
        legacy_interaction_classification,
    ) = check_constant_nonabelian_interactions(
        corrected_tilde_f_sign=False
    )
    (
        graded_failures,
        _graded_residuals,
        graded_classification,
    ) = check_constant_nonabelian_interactions(
        incorrectly_treat_delta_as_odd=True
    )
    nonlinear_solution = solve_nonlinear_coefficients_from_fermion_closure()
    omega_solution = solve_omega_scales_from_scalar_closure()
    rejected_quotient = rejected_noncovariant_quotient_diagnostic()
    su2_triplet_gate = check_offshell_su2_triplet_gate()
    all_failures = [f"lorentz_free:{failure}" for failure in lorentz_failures]
    all_failures.extend(f"euclidean_free:{failure}" for failure in euclidean_failures)
    all_failures.extend(f"constant_su2:{failure}" for failure in nonabelian_failures)
    if nonlinear_solution["solution_branch_count"] != 1:
        all_failures.append("nonlinear_coefficient_system:not_unique_or_not_closed")
    if omega_solution["solution_branch_count"] != 1:
        all_failures.append("omega_coefficient_system:not_unique")
    if not su2_triplet_gate["passed"]:
        all_failures.append("offshell_su2_r_triplet:manifest_slot_no_go")
    status = (
        "PASS_EXACT_CHECKED_SCOPE"
        if not all_failures
        else "BLOCKED_OFFSHELL_SU2_R_PACKAGING"
    )
    return {
        "schema": 2,
        "task": "CONTRACT-STEP-04-EXTENDED-SUPER-YANG-MILLS-001",
        "scope": (
            "Exact free all-field Lorentzian/Euclidean closure plus exact Lorentzian "
            "constant-background SU(2) covariant-first-jet interaction closure."
        ),
        "exact_rings": {
            "free": "Q(i,sqrt(2))[p0,p1,p2,p3] tensor exterior(parameters)",
            "interaction": (
                "Q(i,sqrt(2))[commuting adjoint bosons] tensor "
                "exterior(parameters, adjoint fermions)"
            ),
        },
        "status": status,
        "nonabelian_full_covariant_closure_claimed": False,
        "constant_su2_interaction_closure_claimed": not nonabelian_failures,
        "euclidean_free_closure_claimed": not euclidean_failures,
        "failure_count": len(all_failures),
        "failures": all_failures,
        "checks": {
            "lorentz_free_all_field_closure": {
                "passed": not lorentz_failures,
                "residual_count": len(lorentz_failures),
                "residuals": lorentz_residuals,
            },
            "euclidean_free_all_field_closure": {
                "passed": not euclidean_failures,
                "residual_count": len(euclidean_failures),
                "residuals": euclidean_residuals,
            },
            "constant_su2_nonabelian_interaction_closure": {
                "passed": not nonabelian_failures,
                "residual_count": len(nonabelian_failures),
                "residuals": nonabelian_residuals,
                "residual_classification": nonabelian_classification,
                "scope": (
                    "Exact c_AB^C=epsilon_AB^C, A_mu=partial_mu(field)=0 covariant-jet "
                    "gate.  It retains delta(D_mu X)=(delta A_mu) cross X and checks "
                    "A_mu, phi, tildephi, all fermions, F, tildeF, D, mu, H, and Y_ij."
                ),
            },
            "simultaneous_nonlinear_coefficient_solution": {
                "passed": nonlinear_solution["solution_branch_count"] == 1,
                "residual_count": nonlinear_solution[
                    "full_field_candidate_residual_count"
                ],
                **nonlinear_solution,
            },
            "omega_sign_and_normalization_solution": {
                "passed": omega_solution["solution_branch_count"] == 1,
                "residual_count": 0,
                **omega_solution,
            },
            "offshell_su2_r_triplet_gate": su2_triplet_gate,
        },
        "diagnostics": {
            "rejected_old_sign": {
                "replacement": (
                    "restore the rejected old coefficient delta_1 tildeF = "
                    "-i sqrt(2) epsilon sigma_L^mu D_mu tildepsi"
                ),
                "passed": not legacy_failures,
                "residual_count": len(legacy_failures),
                "residuals": legacy_residuals,
                "constant_covariant_interaction_residual_count": len(
                    legacy_interaction_failures
                ),
                "constant_covariant_interaction_residuals": legacy_interaction_residuals,
                "constant_covariant_interaction_classification": (
                    legacy_interaction_classification
                ),
                "interpretation": (
                    "The accepted correction is required: restoring the old sign reproduces "
                    "both the exact free-closure obstruction and a tildeF/Y22 interaction "
                    "obstruction."
                ),
            },
            "rejected_odd_leibniz_rule": {
                "rejected": True,
                "failed_color_entry_count": len(graded_failures),
                "classification": graded_classification,
                "reason": (
                    "The component transformation already includes its Grassmann-odd "
                    "parameter and is therefore even.  Ordinary Leibniz is required; "
                    "adding an odd-derivation sign destroys scalar and fermion closure."
                ),
            },
            "rejected_noncovariant_constant_quotient": rejected_quotient,
            "parameter_gauge_covariance": {
                "supersymmetry_parameters_are_gauge_singlets": True,
                "additional_compensator_action_on_parameters": "rejected",
                "reason": (
                    "The exact rank-eight solution already fixes the Wess-Zumino "
                    "compensator-induced nonlinear coefficients; a gauge action on the "
                    "constant supersymmetry parameters would violate their singlet type."
                ),
            },
        },
        "unchecked_scope": (
            "General-Lie-algebra non-Abelian closure with simultaneous covariant derivatives, "
            "field strength, and Jacobi reductions is not claimed by this verifier."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-audit", action="store_true")
    args = parser.parse_args()
    result = run_checks()
    if args.write_audit:
        AUDIT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["failure_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
