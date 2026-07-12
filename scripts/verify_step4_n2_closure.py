#!/usr/bin/env python3
"""Exact off-shell closure gates for Step 4B N=2 SYM.

The decisive gate directly composes every displayed nonlinear Lorentzian and
Euclidean transformation in a free differential associative superalgebra over
Q(i,sqrt(2)).  SUSY parameters form a parameter-left exterior algebra;
ordinary jets have commuting sorted derivative labels; matrix words remain
ordered and untruncated.  The older free and constant-background SU(2) gates
remain independent regressions.  No random evaluation or external formula is
used, and every failure is emitted as an exact normal-form residual.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import re

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

EXACT_HALF = Exact.rational(Fraction(1, 2))
SU2_R_LIE_GENERATORS = {
    "t1=i*sigma1/2": (
        (ZERO, I * EXACT_HALF),
        (I * EXACT_HALF, ZERO),
    ),
    "t2=i*sigma2/2": (
        (ZERO, EXACT_HALF),
        (-EXACT_HALF, ZERO),
    ),
    "t3=i*sigma3/2": (
        (I * EXACT_HALF, ZERO),
        (ZERO, -I * EXACT_HALF),
    ),
}


def su2_r_lie_blocks(generator):
    """Raw-field, raw-parameter, and auxiliary generators.

    With S=diag(1,-1), chi=S(psi,lambda), bar-chi=S(tpsi,tlambda),
    zeta=S(epsilon,eta), and bar-zeta=S(bar-epsilon,bar-eta), the raw
    lower and upper doublet generators are

        ell=S t S,        ellbar=-S t^T S.

    The final triple is (x,y,z) for t=((x,y),(z,-x)).
    """

    x, y = generator[0]
    z, minus_x = generator[1]
    if minus_x != -x:
        raise AssertionError("SU(2)_R generator must be traceless")
    ell = ((x, -y), (-z, -x))
    ellbar = ((-x, z), (y, x))
    return ell, ellbar, (x, y, z)

SU2_R_QUARTER_TURN_FIELDS = {field: (field, ONE) for field in FIELDS}
for _spinor_index in range(2):
    SU2_R_QUARTER_TURN_FIELDS[f"psi{_spinor_index}"] = (
        f"lambda{_spinor_index}",
        MINUS_ONE,
    )
    SU2_R_QUARTER_TURN_FIELDS[f"lambda{_spinor_index}"] = (
        f"psi{_spinor_index}",
        ONE,
    )
    SU2_R_QUARTER_TURN_FIELDS[f"tpsi{_spinor_index}"] = (
        f"tlambda{_spinor_index}",
        MINUS_ONE,
    )
    SU2_R_QUARTER_TURN_FIELDS[f"tlambda{_spinor_index}"] = (
        f"tpsi{_spinor_index}",
        ONE,
    )
SU2_R_QUARTER_TURN_FIELDS["F"] = ("tF", ONE)
SU2_R_QUARTER_TURN_FIELDS["tF"] = ("F", ONE)
SU2_R_QUARTER_TURN_FIELDS["D"] = ("D", MINUS_ONE)


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


def check_graded_normal_ordering_identity():
    """Check the PL/FL spinor identity from the locked epsilon tensors.

    For every matrix component this verifies

        barepsilon_{dot a} barsigma^{M dot a a} psi_a
        = -(psi^a sigma^M_{a dot a} barepsilon^{dot a}).

    The right-hand side is first moved to parameter-left order and then
    compared componentwise.  No shorthand spinor identity is assumed.
    """

    failures = []
    residuals = []
    checked_components = 0
    for signature, sigma, bar_sigma in (
        ("L", SIGMA_L, BAR_SIGMA_L),
        ("E", SIGMA_E, BAR_SIGMA_E),
    ):
        for spacetime in range(4):
            for dotted_lower in range(2):
                for field_lower in range(2):
                    field_left_in_parameter_order = ZERO
                    for field_raised in range(2):
                        for dotted_raised in range(2):
                            field_left_in_parameter_order += (
                                MINUS_ONE
                                * EPSILON_UPPER[field_raised][field_lower]
                                * EPSILON_UPPER[dotted_raised][dotted_lower]
                                * sigma[spacetime][field_raised][dotted_raised]
                            )
                    residual = (
                        bar_sigma[spacetime][dotted_lower][field_lower]
                        + field_left_in_parameter_order
                    )
                    checked_components += 1
                    if not residual.is_zero():
                        label = (
                            f"{signature}:M{spacetime}:"
                            f"dot{dotted_lower}:a{field_lower}"
                        )
                        failures.append(label)
                        residuals.append(
                            {"component": label, "residual": exact_string(residual)}
                        )
    return {
        "passed": not failures,
        "checked_components": checked_components,
        "residual_count": len(failures),
        "identity": (
            "barepsilon barsigma^M psi="
            "-(psi sigma^M barepsilon)"
        ),
        "failures": failures,
        "residuals": residuals,
    }


def free_su2_r_matrix():
    result = [[ZERO for _ in FIELDS] for _ in FIELDS]
    for output, (source, coefficient) in SU2_R_QUARTER_TURN_FIELDS.items():
        result[FIELD_INDEX[output]][FIELD_INDEX[source]] = coefficient
    return result


def matrix_left_exact(left, right):
    result = zero_matrix()
    for row in range(len(FIELDS)):
        for middle in range(len(FIELDS)):
            coefficient = left[row][middle]
            if coefficient.is_zero():
                continue
            for column in range(len(FIELDS)):
                if right[middle][column]:
                    result[row][column] = entry_add(
                        result[row][column],
                        entry_scale(right[middle][column], coefficient),
                    )
    return result


def matrix_right_exact(left, right):
    result = zero_matrix()
    for row in range(len(FIELDS)):
        for middle in range(len(FIELDS)):
            if not left[row][middle]:
                continue
            for column in range(len(FIELDS)):
                coefficient = right[middle][column]
                if not coefficient.is_zero():
                    result[row][column] = entry_add(
                        result[row][column],
                        entry_scale(left[row][middle], coefficient),
                    )
    return result


def free_su2_r_parameter_image(name: str) -> tuple[str, Exact]:
    if len(name) != 3 or name[0] not in "12" or name[1] not in "ebnm" or name[2] not in "01":
        raise ValueError(f"unexpected free supersymmetry parameter: {name}")
    kind, coefficient = {
        "e": ("n", MINUS_ONE),
        "n": ("e", ONE),
        "b": ("m", MINUS_ONE),
        "m": ("b", ONE),
    }[name[1]]
    return name[0] + kind + name[2], coefficient


def free_su2_r_parameter_substitution(value: Entry) -> Entry:
    result: Entry = {}
    for monomial, polynomial in value.items():
        transformed: Entry = {(): poly_constant(ONE)}
        for name in monomial:
            image, coefficient = free_su2_r_parameter_image(name)
            transformed = entry_multiply(
                transformed,
                parameter(image, coefficient),
            )
        for transformed_monomial, transformed_polynomial in transformed.items():
            result[transformed_monomial] = poly_add(
                result.get(transformed_monomial, {}),
                poly_multiply(transformed_polynomial, polynomial),
            )
    return entry_normalize(result)


def check_free_su2_r_intertwiner(signature: str):
    if signature == "L":
        transform = build_lorentz_transform(1, corrected_tilde_f_sign=True)
    elif signature == "E":
        transform = build_euclidean_transform(1)
    else:
        raise ValueError(signature)
    rotation = free_su2_r_matrix()
    transformed_parameters = [
        [free_su2_r_parameter_substitution(entry) for entry in row]
        for row in transform
    ]
    left = matrix_left_exact(rotation, transform)
    right = matrix_right_exact(transformed_parameters, rotation)
    failures, residuals = matrix_residual(left, right)
    return {
        "passed": not failures,
        "residual_count": len(failures),
        "signature": signature,
        "matrix_equation": "R_fields T(parameters)=T(R_parameters parameters) R_fields",
        "parameter_quarter_turn": "epsilon->-eta, eta->epsilon, barepsilon->-bareta, bareta->barepsilon",
        "field_quarter_turn": {
            "psi": "-lambda",
            "lambda": "psi",
            "tildepsi": "-tildelambda",
            "tildelambda": "tildepsi",
            "F": "tildeF",
            "tildeF": "F",
            "D_free": "-D_free",
        },
        "failures": failures,
        "residuals": residuals,
    }


def free_su2_r_lie_field_matrix(generator):
    ell, ellbar, (x, y, z) = su2_r_lie_blocks(generator)
    result = [[ZERO for _ in FIELDS] for _ in FIELDS]

    for spinor in range(2):
        for row, output in enumerate((f"psi{spinor}", f"lambda{spinor}")):
            for column, source in enumerate((f"psi{spinor}", f"lambda{spinor}")):
                result[FIELD_INDEX[output]][FIELD_INDEX[source]] = ell[row][column]
        for row, output in enumerate((f"tpsi{spinor}", f"tlambda{spinor}")):
            for column, source in enumerate((f"tpsi{spinor}", f"tlambda{spinor}")):
                result[FIELD_INDEX[output]][FIELD_INDEX[source]] = ellbar[row][column]

    auxiliary = (
        (TWO * x, ZERO, -I * SQRT_TWO * y),
        (ZERO, -TWO * x, -I * SQRT_TWO * z),
        (I * SQRT_TWO * z, I * SQRT_TWO * y, ZERO),
    )
    for row, output in enumerate(("F", "tF", "D")):
        for column, source in enumerate(("F", "tF", "D")):
            result[FIELD_INDEX[output]][FIELD_INDEX[source]] = auxiliary[row][column]
    return result


def free_su2_r_lie_parameter_image(name: str, generator) -> Entry:
    if len(name) != 3 or name[0] not in "12" or name[1] not in "ebnm" or name[2] not in "01":
        raise ValueError(f"unexpected free supersymmetry parameter: {name}")
    ell, ellbar, _ = su2_r_lie_blocks(generator)
    pair = ("e", "n") if name[1] in "en" else ("b", "m")
    matrix = ellbar if name[1] in "en" else ell
    row = pair.index(name[1])
    result: Entry = {}
    for column, kind in enumerate(pair):
        coefficient = matrix[row][column]
        if not coefficient.is_zero():
            result = entry_add(
                result,
                parameter(name[0] + kind + name[2], coefficient),
            )
    return result


def free_su2_r_lie_parameter_derivation(value: Entry, generator) -> Entry:
    """Even Lie-algebra derivation on the exterior parameter algebra."""

    result: Entry = {}
    for monomial, polynomial in value.items():
        for position, name in enumerate(monomial):
            left: Entry = {monomial[:position]: poly_constant(ONE)}
            right: Entry = {monomial[position + 1 :]: poly_constant(ONE)}
            term = entry_multiply(
                entry_multiply(
                    left,
                    free_su2_r_lie_parameter_image(name, generator),
                ),
                right,
            )
            result = entry_add(result, entry_with_poly(term, polynomial))
    return result


def matrix_entry_term_count(matrix) -> int:
    return sum(
        len(polynomial)
        for row in matrix
        for entry in row
        for polynomial in entry.values()
    )


def check_free_su2_r_lie_intertwiner(signature: str):
    """Full su(2)_R Lie-algebra intertwiner on every free matrix slot."""

    if signature not in {"L", "E"}:
        raise ValueError(signature)
    failures = []
    residual_rows = []
    residual_monomial_count = 0
    results = {}
    for set_index in (1, 2):
        transform = (
            build_lorentz_transform(set_index, corrected_tilde_f_sign=True)
            if signature == "L"
            else build_euclidean_transform(set_index)
        )
        for generator_name, generator in SU2_R_LIE_GENERATORS.items():
            field_generator = free_su2_r_lie_field_matrix(generator)
            parameter_derivative = [
                [
                    free_su2_r_lie_parameter_derivation(entry, generator)
                    for entry in row
                ]
                for row in transform
            ]
            commutator = matrix_subtract_entries(
                matrix_left_exact(field_generator, transform),
                matrix_right_exact(transform, field_generator),
            )
            case_failures, case_residuals = matrix_residual(
                commutator,
                parameter_derivative,
            )
            difference = matrix_subtract_entries(commutator, parameter_derivative)
            case_monomials = matrix_entry_term_count(difference)
            case_key = f"set{set_index}:{generator_name}"
            results[case_key] = {
                "passed": not case_failures,
                "residual_cell_count": len(case_failures),
                "residual_monomial_count": case_monomials,
                "residuals": case_residuals,
            }
            failures.extend(
                f"{case_key}:{failure}" for failure in case_failures
            )
            residual_monomial_count += case_monomials
            if len(residual_rows) < 24:
                residual_rows.extend(
                    {"case": case_key, **row}
                    for row in case_residuals[: 24 - len(residual_rows)]
                )
    checked_matrix_cells = (
        2 * len(SU2_R_LIE_GENERATORS) * len(FIELDS) * len(FIELDS)
    )
    return {
        "passed": not failures,
        "signature": signature,
        "generator_basis": list(SU2_R_LIE_GENERATORS),
        "parameter_copies": [1, 2],
        "checked_outputs": list(FIELDS),
        "checked_matrix_cells": checked_matrix_cells,
        "residual_count": len(failures),
        "residual_monomial_count": residual_monomial_count,
        "matrix_equation": "r_X M(Pi)-M(Pi) r_X-M(r_Pi Pi)=0",
        "failures": failures,
        "residuals": residual_rows,
        "results": results,
    }


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


def interaction_su2_r_parameter_image(name: str) -> GExpression:
    if len(name) != 3 or name[0] not in "ebnm" or not name[1:].isdigit():
        raise ValueError(f"unexpected interaction supersymmetry parameter: {name}")
    kind, coefficient = {
        "e": ("n", MINUS_ONE),
        "n": ("e", ONE),
        "b": ("m", MINUS_ONE),
        "m": ("b", ONE),
    }[name[0]]
    return g_generator(kind + name[1:], coefficient)


def interaction_su2_r_field_name(name: str) -> tuple[str, Exact]:
    derivative = re.fullmatch(r"d(.+)m([0-3])", name)
    if derivative:
        base, mu_index = derivative.groups()
        source, coefficient = SU2_R_QUARTER_TURN_FIELDS[base]
        return f"d{source}m{mu_index}", coefficient
    return SU2_R_QUARTER_TURN_FIELDS[name]


def interaction_mu_expression():
    return g_bracket(g_vector("phi"), g_vector("tphi"))


def interaction_mu_jet_expression(mu_index: int):
    return [
        g_add(
            g_bracket(g_vector(f"dphim{mu_index}"), g_vector("tphi"))[color],
            g_bracket(g_vector("phi"), g_vector(f"dtphim{mu_index}"))[color],
        )
        for color in range(3)
    ]


def interaction_su2_r_generator_image(generator: str) -> GExpression:
    if len(generator) == 3 and generator[0] in "ebnm" and generator[1:].isdigit():
        return interaction_su2_r_parameter_image(generator)
    if "c" not in generator:
        return g_generator(generator)
    field_name, color_text = generator.rsplit("c", 1)
    if not color_text.isdigit():
        raise ValueError(generator)
    color = int(color_text)
    if field_name == "D":
        return g_add(
            g_generator(generator, MINUS_ONE),
            g_scale(interaction_mu_expression()[color], Exact.rational(-2)),
        )
    derivative = re.fullmatch(r"dDm([0-3])", field_name)
    if derivative:
        mu_index = int(derivative.group(1))
        return g_add(
            g_generator(generator, MINUS_ONE),
            g_scale(
                interaction_mu_jet_expression(mu_index)[color],
                Exact.rational(-2),
            ),
        )
    source, coefficient = interaction_su2_r_field_name(field_name)
    return g_generator(source + "c" + color_text, coefficient)


def interaction_su2_r_substitution(expression: GExpression) -> GExpression:
    result: GExpression = {}
    for monomial, coefficient in expression.items():
        transformed: GExpression = {(): coefficient}
        for generator in monomial:
            transformed = g_multiply(
                transformed,
                interaction_su2_r_generator_image(generator),
            )
        result = g_add(result, transformed)
    return result


def check_nonabelian_su2_r_intertwiner():
    variations = build_covariant_constant_nonabelian_variations(1)
    mu = interaction_mu_expression()
    failures = []
    residuals = []
    for output in variations:
        for color in range(3):
            if output == "D":
                left = g_add(
                    g_scale(variations["D"][color], MINUS_ONE),
                    g_scale(
                        g_apply_variation(mu[color], variations),
                        Exact.rational(-2),
                    ),
                )
            else:
                derivative = re.fullmatch(r"dDm([0-3])", output)
                if derivative:
                    mu_index = int(derivative.group(1))
                    left = g_add(
                        g_scale(variations[output][color], MINUS_ONE),
                        g_scale(
                            g_apply_variation(
                                interaction_mu_jet_expression(mu_index)[color],
                                variations,
                            ),
                            Exact.rational(-2),
                        ),
                    )
                else:
                    source, coefficient = interaction_su2_r_field_name(output)
                    left = g_scale(variations[source][color], coefficient)
            right = interaction_su2_r_substitution(variations[output][color])
            residual = g_add(left, g_scale(right, MINUS_ONE))
            if residual:
                failures.append(f"{output}[{color}]")
                if len(residuals) < 24:
                    residuals.append(
                        {
                            "output": output,
                            "color": color,
                            "residual": serialize_gexpression(residual),
                        }
                    )
    return {
        "passed": not failures,
        "residual_count": len(failures),
        "matrix_equation": "R_* delta(parameters,fields)=delta(R parameters,R fields)",
        "affine_auxiliary_map": "D->-D-2 mu, equivalently H=D+mu->-H",
        "checked_output_slots": len(variations) * 3,
        "failures": failures,
        "residuals": residuals,
    }


def interaction_su2_r_lie_parameter_image(name: str, generator) -> GExpression:
    match = re.fullmatch(r"([ebnm])([12])([01])", name)
    if match is None:
        raise ValueError(f"unexpected interaction supersymmetry parameter: {name}")
    kind, set_index, component = match.groups()
    ell, ellbar, _ = su2_r_lie_blocks(generator)
    pair = ("e", "n") if kind in "en" else ("b", "m")
    matrix = ellbar if kind in "en" else ell
    row = pair.index(kind)
    result: GExpression = {}
    for column, target_kind in enumerate(pair):
        coefficient = matrix[row][column]
        if not coefficient.is_zero():
            result = g_add(
                result,
                g_generator(target_kind + set_index + component, coefficient),
            )
    return result


def interaction_su2_r_lie_linear_combination(terms) -> GExpression:
    result: GExpression = {}
    for coefficient, expression in terms:
        if not coefficient.is_zero():
            result = g_add(result, g_scale(expression, coefficient))
    return result


def interaction_su2_r_lie_generator_image(
    generator_name: str,
    generator,
) -> GExpression:
    if re.fullmatch(r"[ebnm][12][01]", generator_name):
        return interaction_su2_r_lie_parameter_image(generator_name, generator)
    if "c" not in generator_name:
        raise ValueError(f"untyped interaction generator: {generator_name}")
    field_name, color_text = generator_name.rsplit("c", 1)
    if not color_text.isdigit():
        raise ValueError(generator_name)
    color = int(color_text)
    ell, ellbar, (x, y, z) = su2_r_lie_blocks(generator)

    derivative = re.fullmatch(r"d(.+)m([0-3])", field_name)
    if derivative is not None:
        base, mu_index = derivative.groups()
        if base in {"phi", "tphi"} or base.startswith("A"):
            return {}
        for pair, matrix in (
            (("psi0", "lambda0"), ell),
            (("psi1", "lambda1"), ell),
            (("tpsi0", "tlambda0"), ellbar),
            (("tpsi1", "tlambda1"), ellbar),
        ):
            if base in pair:
                row = pair.index(base)
                return interaction_su2_r_lie_linear_combination(
                    (
                        (
                            matrix[row][column],
                            g_generator(
                                f"d{target}m{mu_index}c{color_text}"
                            ),
                        )
                        for column, target in enumerate(pair)
                    )
                )
        raise ValueError(f"untyped covariant jet for SU(2)_R: {field_name}")

    if field_name in {"phi", "tphi"} or field_name.startswith("A"):
        return {}
    for pair, matrix in (
        (("psi0", "lambda0"), ell),
        (("psi1", "lambda1"), ell),
        (("tpsi0", "tlambda0"), ellbar),
        (("tpsi1", "tlambda1"), ellbar),
    ):
        if field_name in pair:
            row = pair.index(field_name)
            return interaction_su2_r_lie_linear_combination(
                (
                    (
                        matrix[row][column],
                        g_generator(target + "c" + color_text),
                    )
                    for column, target in enumerate(pair)
                )
            )

    F_value = g_vector("F")[color]
    tilde_F_value = g_vector("tF")[color]
    D_value = g_vector("D")[color]
    mu_value = interaction_mu_expression()[color]
    H_value = g_add(D_value, mu_value)
    if field_name == "F":
        return interaction_su2_r_lie_linear_combination(
            (
                (TWO * x, F_value),
                (-I * SQRT_TWO * y, H_value),
            )
        )
    if field_name == "tF":
        return interaction_su2_r_lie_linear_combination(
            (
                (-TWO * x, tilde_F_value),
                (-I * SQRT_TWO * z, H_value),
            )
        )
    if field_name == "D":
        return interaction_su2_r_lie_linear_combination(
            (
                (I * SQRT_TWO * z, F_value),
                (I * SQRT_TWO * y, tilde_F_value),
            )
        )
    raise ValueError(f"untyped component field for SU(2)_R: {field_name}")


def interaction_su2_r_lie_derivation(
    expression: GExpression,
    generator,
) -> GExpression:
    """Even su(2)_R derivation on fields, jets, and parameters."""

    result: GExpression = {}
    for monomial, coefficient in expression.items():
        for position, generator_name in enumerate(monomial):
            image = interaction_su2_r_lie_generator_image(
                generator_name,
                generator,
            )
            if not image:
                continue
            term = g_multiply(
                g_multiply({monomial[:position]: ONE}, image),
                {monomial[position + 1 :]: ONE},
            )
            result = g_add(result, g_scale(term, coefficient))
    return result


def check_interaction_su2_r_lie_intertwiner():
    """Full Lorentzian covariant-jet intertwiner for all off-shell objects."""

    objects = constant_nonabelian_objects()
    checked_outputs = tuple(objects)
    failures = []
    residual_rows = []
    residual_monomial_count = 0
    results = {}
    for set_index in (1, 2):
        variations = build_covariant_constant_nonabelian_variations(set_index)
        for generator_name, generator in SU2_R_LIE_GENERATORS.items():
            case_key = f"set{set_index}:{generator_name}"
            case_failures = []
            case_monomials = 0
            case_residuals = []
            for output, vector in objects.items():
                for color, value in enumerate(vector):
                    delta_value = g_apply_variation(value, variations)
                    transformed_delta = interaction_su2_r_lie_derivation(
                        delta_value,
                        generator,
                    )
                    transformed_value = interaction_su2_r_lie_derivation(
                        value,
                        generator,
                    )
                    delta_transformed_value = g_apply_variation(
                        transformed_value,
                        variations,
                    )
                    residual = g_add(
                        transformed_delta,
                        g_scale(delta_transformed_value, MINUS_ONE),
                    )
                    if residual:
                        failure = f"{output}[{color}]"
                        case_failures.append(failure)
                        case_monomials += len(residual)
                        if len(case_residuals) < 24:
                            case_residuals.append(
                                {
                                    "output": output,
                                    "color": color,
                                    "residual": serialize_gexpression(residual),
                                }
                            )
            results[case_key] = {
                "passed": not case_failures,
                "residual_object_color_count": len(case_failures),
                "residual_monomial_count": case_monomials,
                "residuals": case_residuals,
            }
            failures.extend(
                f"{case_key}:{failure}" for failure in case_failures
            )
            residual_monomial_count += case_monomials
            if len(residual_rows) < 24:
                residual_rows.extend(
                    {"case": case_key, **row}
                    for row in case_residuals[: 24 - len(residual_rows)]
                )

    triplet_failures = []
    triplet_residuals = []
    for generator_name, generator in SU2_R_LIE_GENERATORS.items():
        _, _, (x, y, z) = su2_r_lie_blocks(generator)
        for color in range(3):
            Y11 = objects["Y11"][color]
            Y22 = objects["Y22"][color]
            Y12 = objects["Y12"][color]
            expected = {
                "Y11": interaction_su2_r_lie_linear_combination(
                    ((TWO * x, Y11), (TWO * y, Y12))
                ),
                "Y22": interaction_su2_r_lie_linear_combination(
                    ((TWO * z, Y12), (-TWO * x, Y22))
                ),
                "Y12": interaction_su2_r_lie_linear_combination(
                    ((z, Y11), (y, Y22))
                ),
            }
            for component, value in (
                ("Y11", Y11),
                ("Y22", Y22),
                ("Y12", Y12),
            ):
                actual = interaction_su2_r_lie_derivation(value, generator)
                residual = g_add(actual, g_scale(expected[component], MINUS_ONE))
                if residual:
                    failure = f"{generator_name}:{component}[{color}]"
                    triplet_failures.append(failure)
                    residual_monomial_count += len(residual)
                    if len(triplet_residuals) < 24:
                        triplet_residuals.append(
                            {
                                "generator": generator_name,
                                "component": component,
                                "color": color,
                                "residual": serialize_gexpression(residual),
                            }
                        )
    failures.extend(f"triplet:{failure}" for failure in triplet_failures)
    checked_object_color_slots = (
        2 * len(SU2_R_LIE_GENERATORS) * len(checked_outputs) * 3
    )
    checked_triplet_reconstruction_slots = len(SU2_R_LIE_GENERATORS) * 3 * 3
    return {
        "passed": not failures,
        "generator_basis": list(SU2_R_LIE_GENERATORS),
        "parameter_copies": [1, 2],
        "checked_outputs": list(checked_outputs),
        "checked_object_color_slots": checked_object_color_slots,
        "checked_triplet_reconstruction_slots": checked_triplet_reconstruction_slots,
        "residual_count": len(failures),
        "residual_monomial_count": residual_monomial_count,
        "matrix_equation": "r_total(delta_Pi X)-delta_Pi(r_fields X)=0",
        "triplet_equation": "rY=tY+Yt^T with H=D+mu",
        "failures": failures,
        "residuals": residual_rows,
        "triplet_residuals": triplet_residuals,
        "results": results,
    }


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
    """Dual-normal-order coefficient gate for the invertible triplet map."""

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
    delta_f_parameter_left = selected_coefficient("F", "psi0", "1b0", p_time)
    delta_d_parameter_left = selected_coefficient(
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
        "F<-p0 psi0": delta_f_parameter_left,
        "D<-p0 lambda0": delta_d_parameter_left,
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

    half = Exact.rational(Fraction(1, 2))
    A_left_over_a = delta_f_parameter_left
    c_over_A_left_s = half * delta_d_parameter_left
    A_right_over_a = -A_left_over_a
    c_over_A_right_s = -c_over_A_left_s

    gamma_c_over_s_parameter_left = (
        gamma_times_a
        * A_left_over_a
        * c_over_A_left_s
    )
    gamma_c_over_s_field_left = (
        gamma_times_a
        * A_right_over_a
        * c_over_A_right_s
    )
    residual_coefficient_of_s = (
        gamma_c_over_s_parameter_left - gamma_c_over_s_from_gaugino
    )
    order_covariance_residual = (
        gamma_c_over_s_parameter_left - gamma_c_over_s_field_left
    )
    passed = (
        residual_coefficient_of_s.is_zero()
        and order_covariance_residual.is_zero()
    )

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
            "deltaF_parameter_left": exact_string(delta_f_parameter_left),
            "deltaD_parameter_left": exact_string(delta_d_parameter_left),
            "A_left_over_a": exact_string(A_left_over_a),
            "c_over_A_left_s": exact_string(c_over_A_left_s),
            "A_right_over_a": exact_string(A_right_over_a),
            "c_over_A_right_s": exact_string(c_over_A_right_s),
        },
        "extraction_handles": {
            "psi0_from_F": "1e0,p0000",
            "lambda0_from_D": "1e0,p0000",
            "F_from_psi0": "1b0,p1000",
            "D_from_lambda0": "1b0,p1000",
        },
        "derived_exact_coefficients": {
            "gamma_c_over_s_parameter_left": exact_string(
                gamma_c_over_s_parameter_left
            ),
            "gamma_c_over_s_field_left": exact_string(
                gamma_c_over_s_field_left
            ),
            "residual_coefficient_of_s": exact_string(
                residual_coefficient_of_s
            ),
            "order_covariance_residual": exact_string(
                order_covariance_residual
            ),
        },
        "equations": {
            "gaugino": (
                "gamma*c/s="
                + exact_string(gamma_c_over_s_from_gaugino)
            ),
            "symmetric_triplet_parameter_left": (
                "gamma*c/s="
                + exact_string(gamma_c_over_s_parameter_left)
            ),
            "symmetric_triplet_field_left": (
                "gamma*c/s="
                + exact_string(gamma_c_over_s_field_left)
            ),
        },
        "conclusion": "dual-order manifest-slot compatibility" if passed else "graded-order mismatch",
        "on_shell_boundary": (
            "After F=tildeF=H=0 the displayed physical-field rules admit a "
            "componentwise SU(2)_R-covariant rewriting.  On-shell algebra closure "
            "was not machine-checked and is not claimed."
        ),
        "scope_boundary": (
            "This gate proves the derivative and auxiliary coefficient compatibility only.  "
            "Off-shell SU(2)_R covariance within the declared free Lorentzian, free "
            "Euclidean, and SU(2)-color covariant-jet scope is checked by the "
            "independent intertwiner gates."
        ),
    }


# ---------------------------------------------------------------------------
# Universal arbitrary-Lie closure gate.
#
# The coefficient ring is K=Q(i,sqrt(2)).  Supersymmetry parameters are kept
# in parameter-left exterior order.  Component fields are matrix-valued free
# differential-superalgebra generators: ordinary jets commute only at the
# derivative-label level, while matrix words are never reordered or
# truncated.  Therefore equality of the resulting PBW words is an identity
# for every associative matrix realization, hence for every Lie algebra in
# the declared representation convention.


@dataclass(frozen=True, order=True)
class UniversalJet:
    field: str
    derivatives: tuple[int, ...] = ()


UniversalWord = tuple[UniversalJet, ...]
UniversalKey = tuple[ExteriorMonomial, UniversalWord]
UniversalExpression = dict[UniversalKey, Exact]


def universal_field_parity(field: str) -> int:
    return int(field.startswith(("lambda", "tlambda", "psi", "tpsi")))


def universal_word_parity(word: UniversalWord) -> int:
    return sum(universal_field_parity(jet.field) for jet in word) % 2


def universal_normalize(value: UniversalExpression) -> UniversalExpression:
    return {
        key: coefficient
        for key, coefficient in value.items()
        if not coefficient.is_zero()
    }


def universal_add(
    left: UniversalExpression,
    right: UniversalExpression,
) -> UniversalExpression:
    result = dict(left)
    for key, coefficient in right.items():
        result[key] = result.get(key, ZERO) + coefficient
    return universal_normalize(result)


def universal_scale(
    value: UniversalExpression,
    coefficient: Exact,
) -> UniversalExpression:
    if coefficient.is_zero():
        return {}
    return universal_normalize(
        {key: coefficient * term for key, term in value.items()}
    )


def universal_multiply(
    left: UniversalExpression,
    right: UniversalExpression,
) -> UniversalExpression:
    result: UniversalExpression = {}
    for (left_parameters, left_word), left_coefficient in left.items():
        for (right_parameters, right_word), right_coefficient in right.items():
            parameter_sign, parameters = exterior_product(
                left_parameters,
                right_parameters,
            )
            if parameter_sign == 0:
                continue
            koszul_sign = -1 if (
                universal_word_parity(left_word)
                and len(right_parameters) % 2
            ) else 1
            coefficient = left_coefficient * right_coefficient
            if parameter_sign * koszul_sign == -1:
                coefficient = -coefficient
            key = (parameters, left_word + right_word)
            result[key] = result.get(key, ZERO) + coefficient
    return universal_normalize(result)


def universal_one(coefficient: Exact = ONE) -> UniversalExpression:
    return {} if coefficient.is_zero() else {((), ()): coefficient}


def universal_parameter(name: str, coefficient: Exact = ONE) -> UniversalExpression:
    return {} if coefficient.is_zero() else {((name,), ()): coefficient}


def universal_parameter_monomial(
    names: ExteriorMonomial,
    coefficient: Exact = ONE,
) -> UniversalExpression:
    return {} if coefficient.is_zero() else {(names, ()): coefficient}


def universal_jet(
    field: str,
    derivatives: tuple[int, ...] = (),
    coefficient: Exact = ONE,
) -> UniversalExpression:
    if coefficient.is_zero():
        return {}
    if field not in FIELD_INDEX:
        raise ValueError(f"unknown universal component field: {field}")
    return {
        ((), (UniversalJet(field, tuple(sorted(derivatives))),)): coefficient
    }


def universal_expression_parity(value: UniversalExpression) -> int:
    parities = {
        (len(parameters) + universal_word_parity(word)) % 2
        for parameters, word in value
    }
    if len(parities) != 1:
        raise ValueError(f"expression is not homogeneous: parities={sorted(parities)}")
    return next(iter(parities))


def universal_bracket(
    left: UniversalExpression,
    right: UniversalExpression,
) -> UniversalExpression:
    if not left or not right:
        return {}
    sign = -1 if (
        universal_expression_parity(left)
        * universal_expression_parity(right)
    ) % 2 else 1
    reverse = universal_multiply(right, left)
    if sign == 1:
        reverse = universal_scale(reverse, MINUS_ONE)
    return universal_add(universal_multiply(left, right), reverse)


def universal_partial(
    value: UniversalExpression,
    spacetime_index: int,
) -> UniversalExpression:
    result: UniversalExpression = {}
    for (parameters, word), coefficient in value.items():
        for position, jet in enumerate(word):
            differentiated = UniversalJet(
                jet.field,
                tuple(sorted(jet.derivatives + (spacetime_index,))),
            )
            new_word = word[:position] + (differentiated,) + word[position + 1 :]
            key = (parameters, new_word)
            result[key] = result.get(key, ZERO) + coefficient
    return universal_normalize(result)


def universal_partial_multi(
    value: UniversalExpression,
    derivatives: tuple[int, ...],
) -> UniversalExpression:
    result = value
    for spacetime_index in derivatives:
        result = universal_partial(result, spacetime_index)
    return result


def universal_covariant_expression(
    value: UniversalExpression,
    spacetime_index: int,
) -> UniversalExpression:
    return universal_add(
        universal_partial(value, spacetime_index),
        universal_scale(
            universal_bracket(
                universal_jet(f"A{spacetime_index}"),
                value,
            ),
            MINUS_I,
        ),
    )


def universal_covariant_field(
    field: str,
    spacetime_index: int,
) -> UniversalExpression:
    return universal_covariant_expression(
        universal_jet(field),
        spacetime_index,
    )


def universal_curvature(mu: int, nu: int) -> UniversalExpression:
    return universal_add(
        universal_add(
            universal_jet(f"A{nu}", (mu,)),
            universal_scale(universal_jet(f"A{mu}", (nu,)), MINUS_ONE),
        ),
        universal_scale(
            universal_bracket(
                universal_jet(f"A{mu}"),
                universal_jet(f"A{nu}"),
            ),
            MINUS_I,
        ),
    )


def universal_parameter_component(
    kind: str,
    set_index: int,
    component: int,
    raised: bool = False,
) -> UniversalExpression:
    prefix = {"e": "e", "be": "b", "n": "n", "bn": "m"}[kind]
    if not raised:
        return universal_parameter(f"{set_index}{prefix}{component}")
    result: UniversalExpression = {}
    for lower in range(2):
        coefficient = EPSILON_UPPER[component][lower]
        if not coefficient.is_zero():
            result = universal_add(
                result,
                universal_parameter(f"{set_index}{prefix}{lower}", coefficient),
            )
    return result


def universal_contract_parameter_fermion(
    kind: str,
    set_index: int,
    field_prefix: str,
) -> UniversalExpression:
    result: UniversalExpression = {}
    for spinor in range(2):
        result = universal_add(
            result,
            universal_multiply(
                universal_parameter_component(
                    kind,
                    set_index,
                    spinor,
                    raised=True,
                ),
                universal_jet(f"{field_prefix}{spinor}"),
            ),
        )
    return result


def universal_bar_contract_parameter_fermion(
    kind: str,
    set_index: int,
    field_prefix: str,
) -> UniversalExpression:
    result: UniversalExpression = {}
    for dotted in range(2):
        parameter_value = universal_parameter_component(
            kind,
            set_index,
            dotted,
            raised=False,
        )
        for raised_dotted in range(2):
            coefficient = EPSILON_UPPER[dotted][raised_dotted]
            if coefficient.is_zero():
                continue
            result = universal_add(
                result,
                universal_scale(
                    universal_multiply(
                        parameter_value,
                        universal_jet(f"{field_prefix}{raised_dotted}"),
                    ),
                    coefficient,
                ),
            )
    return result


def build_universal_transform(
    signature: str,
    set_index: int,
) -> dict[str, UniversalExpression]:
    if signature == "L":
        linear = build_lorentz_transform(
            set_index,
            corrected_tilde_f_sign=True,
        )
    elif signature == "E":
        linear = build_euclidean_transform(set_index)
    else:
        raise ValueError(signature)

    variations = {field: {} for field in FIELDS}
    for row, output in enumerate(FIELDS):
        for column, input_field in enumerate(FIELDS):
            for parameter_names, polynomial in linear[row][column].items():
                parameter_value = universal_parameter_monomial(parameter_names)
                for momentum_power, coefficient in polynomial.items():
                    degree = sum(momentum_power)
                    if degree == 0:
                        source = universal_jet(input_field)
                    elif degree == 1:
                        spacetime_index = next(
                            index
                            for index, power in enumerate(momentum_power)
                            if power
                        )
                        if input_field.startswith("A"):
                            gauge_index = int(input_field[1:])
                            source = universal_scale(
                                universal_curvature(
                                    spacetime_index,
                                    gauge_index,
                                ),
                                EXACT_HALF,
                            )
                        else:
                            source = universal_covariant_field(
                                input_field,
                                spacetime_index,
                            )
                    else:
                        raise ValueError(
                            "full nonlinear rule builder received a higher "
                            f"momentum monomial: {momentum_power}"
                        )
                    variations[output] = universal_add(
                        variations[output],
                        universal_scale(
                            universal_multiply(parameter_value, source),
                            coefficient,
                        ),
                    )

    coefficients = displayed_nonlinear_coefficients()
    phi = universal_jet("phi")
    tilde_phi = universal_jet("tphi")
    moment_map = universal_bracket(phi, tilde_phi)
    for spinor in range(2):
        variations[f"psi{spinor}"] = universal_add(
            variations[f"psi{spinor}"],
            universal_scale(
                universal_multiply(
                    universal_parameter_component(
                        "n", set_index, spinor, raised=False
                    ),
                    moment_map,
                ),
                coefficients["psi_mu"],
            ),
        )
        variations[f"tpsi{spinor}"] = universal_add(
            variations[f"tpsi{spinor}"],
            universal_scale(
                universal_multiply(
                    universal_parameter_component(
                        "bn", set_index, spinor, raised=False
                    ),
                    moment_map,
                ),
                coefficients["tpsi_mu"],
            ),
        )

    barred_epsilon_tilde_lambda = universal_bar_contract_parameter_fermion(
        "be", set_index, "tlambda"
    )
    epsilon_lambda = universal_contract_parameter_fermion(
        "e", set_index, "lambda"
    )
    eta_psi = universal_contract_parameter_fermion(
        "n", set_index, "psi"
    )
    barred_eta_tilde_psi = universal_bar_contract_parameter_fermion(
        "bn", set_index, "tpsi"
    )
    eta_lambda = universal_contract_parameter_fermion(
        "n", set_index, "lambda"
    )
    barred_eta_tilde_lambda = universal_bar_contract_parameter_fermion(
        "bn", set_index, "tlambda"
    )
    nonlinear_terms = {
        "F": (
            (
                coefficients["manifest_F"],
                universal_bracket(barred_epsilon_tilde_lambda, phi),
            ),
            (
                coefficients["hidden_F"],
                universal_bracket(eta_psi, tilde_phi),
            ),
        ),
        "tF": (
            (
                coefficients["manifest_tF"],
                universal_bracket(epsilon_lambda, tilde_phi),
            ),
            (
                coefficients["hidden_tF"],
                universal_bracket(barred_eta_tilde_psi, phi),
            ),
        ),
        "D": (
            (
                coefficients["hidden_D_left"],
                universal_bracket(eta_lambda, tilde_phi),
            ),
            (
                coefficients["hidden_D_right"],
                universal_bracket(phi, barred_eta_tilde_lambda),
            ),
        ),
    }
    for output, terms in nonlinear_terms.items():
        for coefficient, value in terms:
            variations[output] = universal_add(
                variations[output],
                universal_scale(value, coefficient),
            )
    return variations


def universal_abelian_matrix(
    variations: dict[str, UniversalExpression],
):
    result = zero_matrix()
    for output, value in variations.items():
        for (parameters, word), coefficient in value.items():
            if len(word) != 1:
                continue
            jet = word[0]
            if len(jet.derivatives) > 1:
                raise ValueError(
                    f"nonlinear transform contains unexpected jet {jet}"
                )
            momentum_power = [0, 0, 0, 0]
            if jet.derivatives:
                momentum_power[jet.derivatives[0]] = 1
            entry = {
                parameters: {
                    tuple(momentum_power): coefficient,
                }
            }
            matrix_add_term(result, output, jet.field, entry)
    return result


def check_universal_abelian_roundtrip(signature: str):
    failures = []
    residuals = []
    checked_cells = 0
    nonzero_source_cells = 0
    nonzero_roundtrip_cells = 0
    for set_index in (1, 2):
        source = (
            build_lorentz_transform(set_index, corrected_tilde_f_sign=True)
            if signature == "L"
            else build_euclidean_transform(set_index)
        )
        roundtrip = universal_abelian_matrix(
            build_universal_transform(signature, set_index)
        )
        difference = matrix_subtract_entries(roundtrip, source)
        for row, output in enumerate(FIELDS):
            for column, input_field in enumerate(FIELDS):
                checked_cells += 1
                nonzero_source_cells += int(bool(source[row][column]))
                nonzero_roundtrip_cells += int(bool(roundtrip[row][column]))
                if difference[row][column]:
                    failure = f"set{set_index}:{output}<-{input_field}"
                    failures.append(failure)
                    if len(residuals) < 24:
                        residuals.append(
                            {
                                "binding": failure,
                                "residual": serialize_entry(
                                    difference[row][column]
                                ),
                            }
                        )
    return {
        "passed": not failures,
        "signature": signature,
        "parameter_copies": [1, 2],
        "matrix_shape": [len(FIELDS), len(FIELDS)],
        "checked_cell_bindings": checked_cells,
        "nonzero_source_cells": nonzero_source_cells,
        "nonzero_roundtrip_cells": nonzero_roundtrip_cells,
        "residual_count": len(failures),
        "failures": failures,
        "residuals": residuals,
        "map": (
            "p_mu X -> D_mu X; antisymmetric p_mu A_nu sector "
            "-> F_mu_nu/2; displayed nonlinear coefficients appended"
        ),
    }


def universal_jet_label(jet: UniversalJet) -> str:
    if not jet.derivatives:
        return jet.field
    return "d" + "".join(str(index) for index in jet.derivatives) + jet.field


def serialize_universal_expression(value: UniversalExpression):
    return {
        (
            (" ".join(parameters) if parameters else "1")
            + " | "
            + (" ".join(universal_jet_label(jet) for jet in word) if word else "1")
        ): exact_string(coefficient)
        for (parameters, word), coefficient in sorted(value.items())
    }


def universal_expression_metrics(value: UniversalExpression):
    return {
        "term_count": len(value),
        "maximum_word_length": max((len(word) for _, word in value), default=0),
        "maximum_jet_order": max(
            (
                len(jet.derivatives)
                for _, word in value
                for jet in word
            ),
            default=0,
        ),
        "maximum_parameter_degree": max(
            (len(parameters) for parameters, _ in value),
            default=0,
        ),
    }


def universal_apply_variation(
    value: UniversalExpression,
    variations: dict[str, UniversalExpression],
) -> UniversalExpression:
    """Apply the parameter-included, even transformation without truncation."""

    jet_cache: dict[UniversalJet, UniversalExpression] = {}

    def jet_variation(jet: UniversalJet) -> UniversalExpression:
        if jet not in jet_cache:
            jet_cache[jet] = universal_partial_multi(
                variations[jet.field],
                jet.derivatives,
            )
        return jet_cache[jet]

    result: UniversalExpression = {}
    for (parameters, word), coefficient in value.items():
        for position, jet in enumerate(word):
            left = {
                (parameters, word[:position]): coefficient,
            }
            right = universal_one()
            if position + 1 < len(word):
                right = {((), word[position + 1 :]): ONE}
            term = universal_multiply(
                universal_multiply(left, jet_variation(jet)),
                right,
            )
            result = universal_add(result, term)
    return result


def universal_entry_parameter_expression(value: Entry) -> UniversalExpression:
    result: UniversalExpression = {}
    for parameters, polynomial in value.items():
        for momentum_power, coefficient in polynomial.items():
            if momentum_power != (0, 0, 0, 0):
                raise ValueError(
                    "closure parameter unexpectedly depends on momentum: "
                    f"{momentum_power}"
                )
            result = universal_add(
                result,
                universal_parameter_monomial(parameters, coefficient),
            )
    return result


def universal_closure_parameters(signature: str):
    if signature == "L":
        sigma = SIGMA_L
        velocity_coefficient = TWO * I
    elif signature == "E":
        sigma = SIGMA_E
        velocity_coefficient = -TWO
    else:
        raise ValueError(signature)

    velocities = []
    for spacetime_index in range(4):
        value = entry_add(
            bilinear(
                "e", 1, sigma[spacetime_index], "be", 2,
                velocity_coefficient,
            ),
            bilinear(
                "e", 2, sigma[spacetime_index], "be", 1,
                -velocity_coefficient,
            ),
        )
        value = entry_add(
            value,
            bilinear(
                "n", 1, sigma[spacetime_index], "bn", 2,
                velocity_coefficient,
            ),
        )
        value = entry_add(
            value,
            bilinear(
                "n", 2, sigma[spacetime_index], "bn", 1,
                -velocity_coefficient,
            ),
        )
        velocities.append(universal_entry_parameter_expression(value))

    omega_tilde_phi = entry_add(
        spinor_contraction("e", 1, "n", 2),
        entry_scale(spinor_contraction("e", 2, "n", 1), MINUS_ONE),
    )
    omega_tilde_phi = entry_scale(omega_tilde_phi, TWO * SQRT_TWO)
    omega_phi = entry_add(
        barred_contraction("be", 1, "bn", 2),
        entry_scale(barred_contraction("be", 2, "bn", 1), MINUS_ONE),
    )
    omega_phi = entry_scale(omega_phi, TWO * SQRT_TWO)
    omega = universal_add(
        universal_multiply(
            universal_entry_parameter_expression(omega_tilde_phi),
            universal_jet("tphi"),
        ),
        universal_multiply(
            universal_entry_parameter_expression(omega_phi),
            universal_jet("phi"),
        ),
    )
    return velocities, omega


UNIVERSAL_DERIVED_FIELDS = ("mu", "H", "Y11", "Y22", "Y12")


def universal_closure_objects():
    objects = {field: universal_jet(field) for field in FIELDS}
    objects["mu"] = universal_bracket(objects["phi"], objects["tphi"])
    objects["H"] = universal_add(objects["D"], objects["mu"])
    objects["Y11"] = universal_scale(objects["F"], -SQRT_TWO)
    objects["Y22"] = universal_scale(objects["tF"], -SQRT_TWO)
    objects["Y12"] = universal_scale(objects["H"], I)
    return objects


def universal_expected_closure(
    name: str,
    value: UniversalExpression,
    velocities: list[UniversalExpression],
    omega: UniversalExpression,
) -> UniversalExpression:
    if name.startswith("A") and name in FIELD_INDEX:
        mu = int(name[1:])
        result: UniversalExpression = {}
        for nu in range(4):
            result = universal_add(
                result,
                universal_multiply(
                    velocities[nu],
                    universal_curvature(nu, mu),
                ),
            )
        return universal_add(
            result,
            universal_covariant_expression(omega, mu),
        )

    result: UniversalExpression = {}
    for mu in range(4):
        result = universal_add(
            result,
            universal_multiply(
                velocities[mu],
                universal_covariant_expression(value, mu),
            ),
        )
    return universal_add(
        result,
        universal_scale(universal_bracket(omega, value), I),
    )


def check_universal_direct_closure(signature: str):
    first = build_universal_transform(signature, 1)
    second = build_universal_transform(signature, 2)
    velocities, omega = universal_closure_parameters(signature)
    objects = universal_closure_objects()
    failures = []
    residual_rows = []
    residual_monomial_count = 0
    maximum_actual_terms = 0
    maximum_expected_terms = 0
    maximum_composed_word_length = 0
    maximum_composed_jet_order = 0
    per_object = {}

    for name, value in objects.items():
        delta_two = universal_apply_variation(value, second)
        delta_one = universal_apply_variation(value, first)
        actual = universal_add(
            universal_apply_variation(delta_two, first),
            universal_scale(
                universal_apply_variation(delta_one, second),
                MINUS_ONE,
            ),
        )
        expected = universal_expected_closure(
            name,
            value,
            velocities,
            omega,
        )
        residual = universal_add(
            actual,
            universal_scale(expected, MINUS_ONE),
        )
        actual_metrics = universal_expression_metrics(actual)
        expected_metrics = universal_expression_metrics(expected)
        residual_metrics = universal_expression_metrics(residual)
        maximum_actual_terms = max(
            maximum_actual_terms,
            actual_metrics["term_count"],
        )
        maximum_expected_terms = max(
            maximum_expected_terms,
            expected_metrics["term_count"],
        )
        maximum_composed_word_length = max(
            maximum_composed_word_length,
            actual_metrics["maximum_word_length"],
            expected_metrics["maximum_word_length"],
        )
        maximum_composed_jet_order = max(
            maximum_composed_jet_order,
            actual_metrics["maximum_jet_order"],
            expected_metrics["maximum_jet_order"],
        )
        per_object[name] = {
            "passed": not residual,
            "actual_term_count": actual_metrics["term_count"],
            "expected_term_count": expected_metrics["term_count"],
            "residual_monomial_count": residual_metrics["term_count"],
        }
        if residual:
            failures.append(name)
            residual_monomial_count += len(residual)
            if len(residual_rows) < 22:
                residual_rows.append(
                    {
                        "object": name,
                        "residual": serialize_universal_expression(residual),
                    }
                )

    primitive_objects = tuple(FIELDS)
    derived_objects = UNIVERSAL_DERIVED_FIELDS
    return {
        "passed": not failures,
        "signature": signature,
        "finite_color_projection": False,
        "structure_constants_instantiated": False,
        "truncation": None,
        "pbw_word_order_reordered": False,
        "primitive_objects": list(primitive_objects),
        "derived_objects": list(derived_objects),
        "primitive_residual_objects_checked": len(primitive_objects),
        "derived_residual_objects_checked": len(derived_objects),
        "total_residual_objects_checked": len(objects),
        "direct_composition_used_for_every_object": True,
        "recursion_used_to_infer_primitive_closure": False,
        "residual_object_count": len(failures),
        "residual_monomial_count": residual_monomial_count,
        "maximum_actual_term_count": maximum_actual_terms,
        "maximum_expected_term_count": maximum_expected_terms,
        "maximum_composed_word_length": maximum_composed_word_length,
        "maximum_composed_jet_order": maximum_composed_jet_order,
        "failures": failures,
        "residuals": residual_rows,
        "per_object": per_object,
    }


def check_universal_structural_identities():
    failures = []
    residual_rows = []
    category_counts = {
        "commuting_partial_jets": 0,
        "graded_jacobi": 0,
        "covariant_derivative_curvature": 0,
        "bianchi": 0,
        "variation_covariant_derivative_recursion": 0,
        "variation_curvature_recursion": 0,
        "variation_bracket_recursion": 0,
    }
    category_residual_counts = {key: 0 for key in category_counts}

    def record(category: str, label: str, residual: UniversalExpression):
        category_counts[category] += 1
        if not residual:
            return
        failures.append(f"{category}:{label}")
        category_residual_counts[category] += 1
        if len(residual_rows) < 24:
            residual_rows.append(
                {
                    "identity": f"{category}:{label}",
                    "residual": serialize_universal_expression(residual),
                }
            )

    for field in ("phi", "lambda0"):
        value = universal_jet(field)
        for mu in range(4):
            for nu in range(mu + 1, 4):
                residual = universal_add(
                    universal_partial(
                        universal_partial(value, nu),
                        mu,
                    ),
                    universal_scale(
                        universal_partial(
                            universal_partial(value, mu),
                            nu,
                        ),
                        MINUS_ONE,
                    ),
                )
                record(
                    "commuting_partial_jets",
                    f"{field}:d{mu}d{nu}",
                    residual,
                )

    parity_representatives = {
        0: ("phi", "tphi", "D"),
        1: ("lambda0", "psi0", "tlambda0"),
    }
    for px in (0, 1):
        for py in (0, 1):
            for pz in (0, 1):
                x = universal_jet(parity_representatives[px][0])
                y = universal_jet(parity_representatives[py][1])
                z = universal_jet(parity_representatives[pz][2])
                first = universal_bracket(x, universal_bracket(y, z))
                second = universal_bracket(y, universal_bracket(z, x))
                third = universal_bracket(z, universal_bracket(x, y))
                if px * pz % 2:
                    first = universal_scale(first, MINUS_ONE)
                if py * px % 2:
                    second = universal_scale(second, MINUS_ONE)
                if pz * py % 2:
                    third = universal_scale(third, MINUS_ONE)
                residual = universal_add(universal_add(first, second), third)
                record(
                    "graded_jacobi",
                    f"parities={px}{py}{pz}",
                    residual,
                )

    for field in ("phi", "lambda0"):
        value = universal_jet(field)
        for mu in range(4):
            for nu in range(mu + 1, 4):
                commutator = universal_add(
                    universal_covariant_expression(
                        universal_covariant_expression(value, nu),
                        mu,
                    ),
                    universal_scale(
                        universal_covariant_expression(
                            universal_covariant_expression(value, mu),
                            nu,
                        ),
                        MINUS_ONE,
                    ),
                )
                residual = universal_add(
                    commutator,
                    universal_scale(
                        universal_bracket(universal_curvature(mu, nu), value),
                        I,
                    ),
                )
                record(
                    "covariant_derivative_curvature",
                    f"{field}:m{mu}n{nu}",
                    residual,
                )

    for mu in range(4):
        for nu in range(mu + 1, 4):
            for rho in range(nu + 1, 4):
                residual = universal_add(
                    universal_add(
                        universal_covariant_expression(
                            universal_curvature(nu, rho),
                            mu,
                        ),
                        universal_covariant_expression(
                            universal_curvature(rho, mu),
                            nu,
                        ),
                    ),
                    universal_covariant_expression(
                        universal_curvature(mu, nu),
                        rho,
                    ),
                )
                record(
                    "bianchi",
                    f"m{mu}n{nu}r{rho}",
                    residual,
                )

    tensor_fields = tuple(
        field for field in FIELDS if not field.startswith("A")
    )
    bracket_pairs = (
        ("phi", "tphi"),
        ("phi", "lambda0"),
        ("lambda0", "phi"),
        ("lambda0", "psi0"),
    )
    for signature in ("L", "E"):
        for set_index in (1, 2):
            variations = build_universal_transform(signature, set_index)
            for field in tensor_fields:
                value = universal_jet(field)
                for mu in range(4):
                    left = universal_apply_variation(
                        universal_covariant_expression(value, mu),
                        variations,
                    )
                    right = universal_add(
                        universal_covariant_expression(
                            variations[field],
                            mu,
                        ),
                        universal_scale(
                            universal_bracket(
                                variations[f"A{mu}"],
                                value,
                            ),
                            MINUS_I,
                        ),
                    )
                    residual = universal_add(
                        left,
                        universal_scale(right, MINUS_ONE),
                    )
                    record(
                        "variation_covariant_derivative_recursion",
                        f"{signature}:set{set_index}:{field}:m{mu}",
                        residual,
                    )
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    left = universal_apply_variation(
                        universal_curvature(mu, nu),
                        variations,
                    )
                    right = universal_add(
                        universal_covariant_expression(
                            variations[f"A{nu}"],
                            mu,
                        ),
                        universal_scale(
                            universal_covariant_expression(
                                variations[f"A{mu}"],
                                nu,
                            ),
                            MINUS_ONE,
                        ),
                    )
                    residual = universal_add(
                        left,
                        universal_scale(right, MINUS_ONE),
                    )
                    record(
                        "variation_curvature_recursion",
                        f"{signature}:set{set_index}:m{mu}n{nu}",
                        residual,
                    )
            for left_field, right_field in bracket_pairs:
                left_value = universal_jet(left_field)
                right_value = universal_jet(right_field)
                left = universal_apply_variation(
                    universal_bracket(left_value, right_value),
                    variations,
                )
                right = universal_add(
                    universal_bracket(
                        variations[left_field],
                        right_value,
                    ),
                    universal_bracket(
                        left_value,
                        variations[right_field],
                    ),
                )
                residual = universal_add(
                    left,
                    universal_scale(right, MINUS_ONE),
                )
                record(
                    "variation_bracket_recursion",
                    (
                        f"{signature}:set{set_index}:"
                        f"[{left_field},{right_field}]"
                    ),
                    residual,
                )

    return {
        "passed": not failures,
        "finite_color_projection": False,
        "structure_constants_instantiated": False,
        "truncation": None,
        "pbw_word_order_reordered": False,
        "normal_form": (
            "free differential associative superalgebra with sorted "
            "ordinary-jet derivative tuples and unreordered PBW words"
        ),
        "checked_identity_count": sum(category_counts.values()),
        "category_counts": category_counts,
        "category_residual_counts": category_residual_counts,
        "residual_count": len(failures),
        "failures": failures,
        "residuals": residual_rows,
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
    normal_order_identity = check_graded_normal_ordering_identity()
    su2_triplet_gate = check_offshell_su2_triplet_gate()
    su2_lie_free_lorentz = check_free_su2_r_lie_intertwiner("L")
    su2_lie_free_euclidean = check_free_su2_r_lie_intertwiner("E")
    su2_lie_interaction = check_interaction_su2_r_lie_intertwiner()
    su2_quarter_turn_lorentz = check_free_su2_r_intertwiner("L")
    su2_quarter_turn_euclidean = check_free_su2_r_intertwiner("E")
    su2_quarter_turn_interaction = check_nonabelian_su2_r_intertwiner()
    universal_roundtrip_lorentz = check_universal_abelian_roundtrip("L")
    universal_roundtrip_euclidean = check_universal_abelian_roundtrip("E")
    universal_closure_lorentz = check_universal_direct_closure("L")
    universal_closure_euclidean = check_universal_direct_closure("E")
    universal_structural = check_universal_structural_identities()
    all_failures = [f"lorentz_free:{failure}" for failure in lorentz_failures]
    all_failures.extend(f"euclidean_free:{failure}" for failure in euclidean_failures)
    all_failures.extend(f"constant_su2:{failure}" for failure in nonabelian_failures)
    if nonlinear_solution["solution_branch_count"] != 1:
        all_failures.append("nonlinear_coefficient_system:not_unique_or_not_closed")
    if omega_solution["solution_branch_count"] != 1:
        all_failures.append("omega_coefficient_system:not_unique")
    if not normal_order_identity["passed"]:
        all_failures.extend(
            f"graded_normal_order:{failure}"
            for failure in normal_order_identity["failures"]
        )
    if not su2_triplet_gate["passed"]:
        all_failures.append("offshell_su2_r_normal_order:manifest_slot_mismatch")
    for label, gate in (
        ("offshell_su2_r_lie_free_lorentz", su2_lie_free_lorentz),
        ("offshell_su2_r_lie_free_euclidean", su2_lie_free_euclidean),
        ("offshell_su2_r_lie_interaction", su2_lie_interaction),
        ("offshell_su2_r_quarter_turn_free_lorentz", su2_quarter_turn_lorentz),
        ("offshell_su2_r_quarter_turn_free_euclidean", su2_quarter_turn_euclidean),
        ("offshell_su2_r_quarter_turn_interaction", su2_quarter_turn_interaction),
    ):
        all_failures.extend(f"{label}:{failure}" for failure in gate["failures"])
    for label, gate in (
        ("universal_abelian_roundtrip_lorentz", universal_roundtrip_lorentz),
        ("universal_abelian_roundtrip_euclidean", universal_roundtrip_euclidean),
        ("universal_direct_closure_lorentz", universal_closure_lorentz),
        ("universal_direct_closure_euclidean", universal_closure_euclidean),
        ("universal_structural", universal_structural),
    ):
        all_failures.extend(f"{label}:{failure}" for failure in gate["failures"])

    universal_binding_count = (
        universal_roundtrip_lorentz["checked_cell_bindings"]
        + universal_roundtrip_euclidean["checked_cell_bindings"]
    )
    universal_object_residual_count = (
        universal_closure_lorentz["total_residual_objects_checked"]
        + universal_closure_euclidean["total_residual_objects_checked"]
    )
    if universal_binding_count != 1156:
        all_failures.append(
            f"universal_binding_count:{universal_binding_count}!=1156"
        )
    if universal_object_residual_count != 44:
        all_failures.append(
            "universal_object_residual_count:"
            f"{universal_object_residual_count}!=44"
        )
    status = (
        "PASS_EXACT_GENERAL_LIE_CLOSURE"
        if not all_failures
        else "FAILED_EXACT_GENERAL_LIE_CLOSURE"
    )
    return {
        "schema": 3,
        "task": "CONTRACT-STEP-04-EXTENDED-SUPER-YANG-MILLS-001",
        "scope": (
            "Exact direct off-shell N=2 closure for the displayed Lorentzian and "
            "Euclidean component rules in the free differential associative "
            "superalgebra, together with all previous regression gates."
        ),
        "exact_rings": {
            "free": "Q(i,sqrt(2))[p0,p1,p2,p3] tensor exterior(parameters)",
            "interaction": (
                "Q(i,sqrt(2))[commuting adjoint bosons] tensor "
                "exterior(parameters, adjoint fermions)"
            ),
            "universal": (
                "Q(i,sqrt(2)) tensor exterior(parameter-left SUSY parameters) "
                "tensor ordered noncommutative ordinary-jet PBW words"
            ),
        },
        "status": status,
        "nonabelian_full_covariant_closure_claimed": not all_failures,
        "constant_su2_interaction_closure_claimed": not nonabelian_failures,
        "euclidean_free_closure_claimed": not euclidean_failures,
        "complete_checked_scope_offshell_su2_r_intertwiner_claimed": (
            su2_lie_free_lorentz["passed"]
            and su2_lie_free_euclidean["passed"]
            and su2_lie_interaction["passed"]
        ),
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
            "graded_normal_ordering_identity": normal_order_identity,
            "offshell_su2_r_lie_free_lorentz_intertwiner": su2_lie_free_lorentz,
            "offshell_su2_r_lie_free_euclidean_intertwiner": su2_lie_free_euclidean,
            "offshell_su2_r_lie_interaction_intertwiner": su2_lie_interaction,
            "offshell_su2_r_triplet_gate": su2_triplet_gate,
            "offshell_su2_r_quarter_turn_free_lorentz_regression": su2_quarter_turn_lorentz,
            "offshell_su2_r_quarter_turn_free_euclidean_regression": su2_quarter_turn_euclidean,
            "offshell_su2_r_quarter_turn_interaction_regression": su2_quarter_turn_interaction,
            "universal_abelian_roundtrip_lorentz": universal_roundtrip_lorentz,
            "universal_abelian_roundtrip_euclidean": universal_roundtrip_euclidean,
            "universal_direct_general_lie_closure_lorentz": universal_closure_lorentz,
            "universal_direct_general_lie_closure_euclidean": universal_closure_euclidean,
            "universal_structural_identities": universal_structural,
            "universal_gate_exact_counts": {
                "passed": (
                    universal_binding_count == 1156
                    and universal_object_residual_count == 44
                ),
                "residual_count": int(universal_binding_count != 1156)
                + int(universal_object_residual_count != 44),
                "abelian_roundtrip_bindings": universal_binding_count,
                "direct_object_residuals": universal_object_residual_count,
                "required_abelian_roundtrip_bindings": 1156,
                "required_direct_object_residuals": 44,
            },
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
        "unchecked_scope": [],
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
