#!/usr/bin/env python3
"""Exact verification of the Step-4D Majorana spinor system.

The coefficient ring is Q(i,sqrt(2)).  Spinor components, supersymmetry
parameters, and jets are formal anticommuting generators; bosonic labels
are formal commuting generators.  Every check is an exact identity over
this ring; no floating point and no external computer-algebra package
are used.

The ten checks anchor the memo equations of
contracts/foundations/step-04d-majorana-spinor-system.md, per its
table (4D.74):

  1  gamma_clifford_chirality_traces   (4D.3)-(4D.14), (4D.17)-(4D.19)
  2  beta_hermiticity                  (4D.20)-(4D.22)
  3  charge_conjugation_majorana       (4D.23)-(4D.30)
  4  bilinear_dictionary               (4D.34)
  5  majorana_flips                    (4D.35)-(4D.36)
  6  majorana_fierz                    (4D.37)
  7  kinetic_equivalence               (4D.38)-(4D.41)
  8  susy_algebra_superspace           (4D.43), (4D.46), (4D.48)-(4D.53)
  9  n4_action_fermion_sector          (4D.60)-(4D.63)
 10  n4_sixteen_transformations        (4D.56), (4D.64)-(4D.66), (4D.68)-(4D.69)
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from verify_step3a_gauge_chiral_action import (
    BAR_SIGMA_E,
    BAR_SIGMA_L,
    Exact,
    HALF,
    I,
    MINUS_I,
    MINUS_ONE,
    ONE,
    SIGMA_E,
    SIGMA_L,
    SQRT_TWO,
    TWO,
    ZERO,
    matrix_multiply,
    matrix_scale,
    matrix_subtract,
)

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "audits" / "step4d-majorana-verification.json"

QUARTER = Exact.rational(Fraction(1, 4))
MINUS_TWO = Exact.rational(-2)
FOUR = Exact.rational(4)
MINUS_FOUR = Exact.rational(-4)

# ----------------------------------------------------------------------
# Spinor epsilon matrices: eps^{12}=+1, eps_{12}=-1 (contract (1.3)-(1.4)).
# EPS_UP[a][b] = eps^{ab}, EPS_DN[a][b] = eps_{ab}; identical for dotted.
# ----------------------------------------------------------------------

EPS_UP = ((ZERO, ONE), (MINUS_ONE, ZERO))
EPS_DN = ((ZERO, MINUS_ONE), (ONE, ZERO))

ETA = (MINUS_ONE, ONE, ONE, ONE)  # eta_{mu mu}, diagonal


def sigma_bar_mu_nu(sigma, bar_sigma):
    return tuple(
        tuple(
            matrix_scale(
                matrix_subtract(
                    matrix_multiply(sigma[mu], bar_sigma[nu]),
                    matrix_multiply(sigma[nu], bar_sigma[mu]),
                ),
                QUARTER,
            )
            for nu in range(4)
        )
        for mu in range(4)
    )


def bar_sigma_mu_nu(sigma, bar_sigma):
    return tuple(
        tuple(
            matrix_scale(
                matrix_subtract(
                    matrix_multiply(bar_sigma[mu], sigma[nu]),
                    matrix_multiply(bar_sigma[nu], sigma[mu]),
                ),
                QUARTER,
            )
            for nu in range(4)
        )
        for mu in range(4)
    )


SIGMA_MUNU = sigma_bar_mu_nu(SIGMA_L, BAR_SIGMA_L)
BAR_SIGMA_MUNU = bar_sigma_mu_nu(SIGMA_L, BAR_SIGMA_L)
SIGMA_MN_EU = sigma_bar_mu_nu(SIGMA_E, BAR_SIGMA_E)
BAR_SIGMA_MN_EU = bar_sigma_mu_nu(SIGMA_E, BAR_SIGMA_E)

# ----------------------------------------------------------------------
# 4x4 matrices over Exact.
# Slot layout: rows/columns 0,1 = lower undotted a=1,2;
#              rows/columns 2,3 = upper dotted adot=1,2.
# ----------------------------------------------------------------------


def mat4_zero():
    return tuple(tuple(ZERO for _ in range(4)) for _ in range(4))


def mat4_identity():
    return tuple(tuple(ONE if r == c else ZERO for c in range(4)) for r in range(4))


def mat4_from_blocks(upper_left, upper_right, lower_left, lower_right):
    rows = []
    for r in range(2):
        rows.append(tuple(upper_left[r]) + tuple(upper_right[r]))
    for r in range(2):
        rows.append(tuple(lower_left[r]) + tuple(lower_right[r]))
    return tuple(rows)


ZERO2 = ((ZERO, ZERO), (ZERO, ZERO))
ID2 = ((ONE, ZERO), (ZERO, ONE))


def mat4_mul(left, right):
    return tuple(
        tuple(
            sum((left[r][k] * right[k][c] for k in range(4)), ZERO)
            for c in range(4)
        )
        for r in range(4)
    )


def mat4_add(left, right):
    return tuple(tuple(left[r][c] + right[r][c] for c in range(4)) for r in range(4))


def mat4_sub(left, right):
    return tuple(tuple(left[r][c] - right[r][c] for c in range(4)) for r in range(4))


def mat4_scale(matrix, coefficient):
    return tuple(tuple(coefficient * matrix[r][c] for c in range(4)) for r in range(4))


def mat4_eq(left, right):
    return all((left[r][c] - right[r][c]).is_zero() for r in range(4) for c in range(4))


def mat4_transpose(matrix):
    return tuple(tuple(matrix[c][r] for c in range(4)) for r in range(4))


def exact_conjugate(value: Exact) -> Exact:
    return Exact(value.a, -value.b, value.c, -value.d)


def mat4_dagger(matrix):
    return tuple(tuple(exact_conjugate(matrix[c][r]) for c in range(4)) for r in range(4))


def mat4_trace(matrix):
    return sum((matrix[r][r] for r in range(4)), ZERO)


def gamma_from_sigma(sigma, bar_sigma):
    return tuple(
        mat4_from_blocks(ZERO2, sigma[mu], bar_sigma[mu], ZERO2) for mu in range(4)
    )


GAMMA_L = gamma_from_sigma(SIGMA_L, BAR_SIGMA_L)
GAMMA_E = gamma_from_sigma(SIGMA_E, BAR_SIGMA_E)

# gamma5 = i gamma^0 gamma^1 gamma^2 gamma^3  (Lorentzian, Srednicki sign)
GAMMA5 = mat4_scale(
    mat4_mul(mat4_mul(GAMMA_L[0], GAMMA_L[1]), mat4_mul(GAMMA_L[2], GAMMA_L[3])), I
)
# gamma5E = - gammaE^1 gammaE^2 gammaE^3 gammaE^4
GAMMA5_E = mat4_scale(
    mat4_mul(mat4_mul(GAMMA_E[0], GAMMA_E[1]), mat4_mul(GAMMA_E[2], GAMMA_E[3])),
    MINUS_ONE,
)

P_L = mat4_scale(mat4_sub(mat4_identity(), GAMMA5), HALF)
P_R = mat4_scale(mat4_add(mat4_identity(), GAMMA5), HALF)

BETA = mat4_from_blocks(ZERO2, ID2, ID2, ZERO2)
CC = mat4_from_blocks(EPS_DN, ZERO2, ZERO2, EPS_UP)


def gamma_munu(gammas):
    return tuple(
        tuple(
            mat4_scale(
                mat4_sub(mat4_mul(gammas[mu], gammas[nu]), mat4_mul(gammas[nu], gammas[mu])),
                HALF,
            )
            for nu in range(4)
        )
        for mu in range(4)
    )


GAMMA_MUNU_L = gamma_munu(GAMMA_L)
GAMMA_MN_E = gamma_munu(GAMMA_E)


def epsilon_sign(indices):
    order = list(indices)
    if len(set(order)) != len(order):
        return 0
    sign = 1
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if order[i] > order[j]:
                sign = -sign
    return sign


# ----------------------------------------------------------------------
# Formal Grassmann polynomial algebra.
# Monomial = (odd generator tuple sorted, even generator tuple sorted).
# Generators are tuples starting with a string tag.
# ----------------------------------------------------------------------

Poly = dict


def poly_zero() -> Poly:
    return {}


def poly_scalar(coefficient: Exact) -> Poly:
    if coefficient.is_zero():
        return {}
    return {((), ()): coefficient}


def odd_gen(*key) -> Poly:
    return {((tuple(key),), ()): ONE}


def even_gen(*key) -> Poly:
    return {((), (tuple(key),)): ONE}


def poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        total = result.get(monomial, ZERO) + coefficient
        if total.is_zero():
            result.pop(monomial, None)
        else:
            result[monomial] = total
    return result


def poly_scale(value: Poly, coefficient: Exact) -> Poly:
    if coefficient.is_zero():
        return {}
    return {monomial: coefficient * term for monomial, term in value.items()}


def poly_sub(left: Poly, right: Poly) -> Poly:
    return poly_add(left, poly_scale(right, MINUS_ONE))


def odd_merge(left: tuple, right: tuple):
    """Merge two sorted odd tuples; return (sign, merged) or None if repeated."""
    merged = []
    sign = 1
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            return None
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            # right[j] passes the remaining len(left)-i odd generators
            if (len(left) - i) % 2:
                sign = -sign
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return sign, tuple(merged)


def poly_mul(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (lodd, leven), lcoef in left.items():
        for (rodd, reven), rcoef in right.items():
            merged = odd_merge(lodd, rodd)
            if merged is None:
                continue
            sign, odd_part = merged
            even_part = tuple(sorted(leven + reven))
            coefficient = lcoef * rcoef
            if sign < 0:
                coefficient = -coefficient
            monomial = (odd_part, even_part)
            total = result.get(monomial, ZERO) + coefficient
            if total.is_zero():
                result.pop(monomial, None)
            else:
                result[monomial] = total
    return result


def poly_is_zero(value: Poly) -> bool:
    return all(coefficient.is_zero() for coefficient in value.values())


def poly_eq(left: Poly, right: Poly) -> bool:
    return poly_is_zero(poly_sub(left, right))


# Vectors of polynomials -------------------------------------------------


def vec_zero(size: int):
    return [poly_zero() for _ in range(size)]


def vec_add(left, right):
    return [poly_add(l, r) for l, r in zip(left, right)]


def vec_scale(vector, coefficient: Exact):
    return [poly_scale(entry, coefficient) for entry in vector]


def vec_scale_poly(vector, poly: Poly):
    return [poly_mul(poly, entry) for entry in vector]


def mat4_vec(matrix, vector):
    return [
        poly_add(
            poly_add(poly_scale(vector[0], matrix[r][0]), poly_scale(vector[1], matrix[r][1])),
            poly_add(poly_scale(vector[2], matrix[r][2]), poly_scale(vector[3], matrix[r][3])),
        )
        for r in range(4)
    ]


def vec_transpose_mat4(vector, matrix):
    """Row vector v^T M, preserving Grassmann order (v entries first)."""
    return [
        poly_add(
            poly_add(poly_scale(vector[0], matrix[0][c]), poly_scale(vector[1], matrix[1][c])),
            poly_add(poly_scale(vector[2], matrix[2][c]), poly_scale(vector[3], matrix[3][c])),
        )
        for c in range(4)
    ]


def row_dot_col(row, col) -> Poly:
    result = poly_zero()
    for r, c in zip(row, col):
        result = poly_add(result, poly_mul(r, c))
    return result


def mat2_vec(matrix, vector):
    return [
        poly_add(poly_scale(vector[0], matrix[r][0]), poly_scale(vector[1], matrix[r][1]))
        for r in range(2)
    ]


# Two-component helpers --------------------------------------------------


def raise_spinor(lower):
    """psi^a = eps^{ab} psi_b (same numerics for dotted)."""
    return mat2_vec(EPS_UP, lower)


def lower_spinor(upper):
    return mat2_vec(EPS_DN, upper)


def contract_uu(upper, lower) -> Poly:
    """xi chi := xi^a chi_a."""
    return poly_add(poly_mul(upper[0], lower[0]), poly_mul(upper[1], lower[1]))


def contract_bar(lower, upper) -> Poly:
    """bar-xi bar-chi := bar-xi_adot bar-chi^adot."""
    return poly_add(poly_mul(lower[0], upper[0]), poly_mul(lower[1], upper[1]))


def sigma_contract(upper, sigma_matrix, bar_upper) -> Poly:
    """chi sigma^mu bar-psi := chi^a (sigma^mu)_{a bdot} bar-psi^bdot."""
    result = poly_zero()
    for a in range(2):
        for b in range(2):
            result = poly_add(
                result, poly_scale(poly_mul(upper[a], bar_upper[b]), sigma_matrix[a][b])
            )
    return result


def bar_sigma_contract(bar_lower, bar_sigma_matrix, lower) -> Poly:
    """bar-chi bar-sigma^mu psi := bar-chi_adot (bar-sigma^mu)^{adot b} psi_b."""
    result = poly_zero()
    for a in range(2):
        for b in range(2):
            result = poly_add(
                result, poly_scale(poly_mul(bar_lower[a], lower[b]), bar_sigma_matrix[a][b])
            )
    return result


def sigma_munu_contract(upper, matrix, lower) -> Poly:
    """chi sigma^{mu nu} psi := chi^a (sigma^{mu nu})_a{}^b psi_b."""
    result = poly_zero()
    for a in range(2):
        for b in range(2):
            result = poly_add(result, poly_scale(poly_mul(upper[a], lower[b]), matrix[a][b]))
    return result


def bar_sigma_munu_contract(bar_lower, matrix, bar_upper) -> Poly:
    """bar-chi bar-sigma^{mu nu} bar-psi := bar-chi_adot (bar-sigma^{mu nu})^adot{}_bdot bar-psi^bdot."""
    result = poly_zero()
    for a in range(2):
        for b in range(2):
            result = poly_add(
                result, poly_scale(poly_mul(bar_lower[a], bar_upper[b]), matrix[a][b])
            )
    return result


# Majorana packaging -----------------------------------------------------


def weyl_pair(tag: str):
    """Independent Weyl pair: psi_a (lower) and bar-psi_adot (lower)."""
    lower = [odd_gen(tag, "L", a) for a in range(2)]
    bar_lower = [odd_gen(tag, "B", a) for a in range(2)]
    return lower, bar_lower


def majorana_package(lower, bar_lower):
    """Psi = (psi_a, bar-psi^adot)^T."""
    bar_upper = raise_spinor(bar_lower)
    return [lower[0], lower[1], bar_upper[0], bar_upper[1]]


def bar_via_C(column):
    """barPsi := Psi^T C."""
    return vec_transpose_mat4(column, CC)


def conj_single(poly: Poly, conj_gen) -> Poly:
    """Dagger of a degree<=1 polynomial: conjugate coefficients, map generators."""
    result: Poly = {}
    for (odd_part, even_part), coefficient in poly.items():
        if even_part or len(odd_part) > 1:
            raise ValueError("conj_single expects degree <= 1 odd polynomials")
        new_odd = tuple(conj_gen(g) for g in odd_part)
        monomial = (new_odd, even_part)
        result[monomial] = result.get(monomial, ZERO) + exact_conjugate(coefficient)
    return result


def bar_via_beta(column, conj_gen):
    """barPsi := Psi^dagger beta."""
    dagger_row = [conj_single(entry, conj_gen) for entry in column]
    return vec_transpose_mat4(dagger_row, BETA)


# Derivative (jet) operator ---------------------------------------------


def jet_of(generator: tuple, mu: int) -> tuple:
    return ("d",) + (mu,) + generator


def sort_odd_with_sign(generators):
    items = list(generators)
    sign = 1
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                if items[j] == items[j + 1]:
                    return 0, ()
                items[j], items[j + 1] = items[j + 1], items[j]
                sign = -sign
    if len(set(items)) != len(items):
        return 0, ()
    return sign, tuple(items)


def poly_derivative(value: Poly, mu: int) -> Poly:
    """Even derivative acting by the Leibniz rule on odd generators."""
    result: Poly = {}
    for (odd_part, even_part), coefficient in value.items():
        for position, generator in enumerate(odd_part):
            replaced = list(odd_part)
            replaced[position] = jet_of(generator, mu)
            sign, sorted_odd = sort_odd_with_sign(replaced)
            if sign == 0:
                continue
            monomial = (sorted_odd, even_part)
            term = coefficient if sign > 0 else -coefficient
            total = result.get(monomial, ZERO) + term
            if total.is_zero():
                result.pop(monomial, None)
            else:
                result[monomial] = total
    return result


def jet_column(lower_tag_column, mu: int):
    return [poly_derivative(entry, mu) for entry in lower_tag_column]


# ----------------------------------------------------------------------
# Check 1: Clifford algebra, chirality, Wick relations, gamma technology.
# ----------------------------------------------------------------------


def check_gamma_clifford_chirality_traces():
    failures = []

    identity = mat4_identity()
    for mu in range(4):
        for nu in range(4):
            anticom = mat4_add(
                mat4_mul(GAMMA_L[mu], GAMMA_L[nu]), mat4_mul(GAMMA_L[nu], GAMMA_L[mu])
            )
            eta = ETA[mu] if mu == nu else ZERO
            if not mat4_eq(anticom, mat4_scale(identity, MINUS_TWO * eta if mu == nu else ZERO)):
                failures.append(f"lorentz clifford {mu}{nu}")
            anticom_e = mat4_add(
                mat4_mul(GAMMA_E[mu], GAMMA_E[nu]), mat4_mul(GAMMA_E[nu], GAMMA_E[mu])
            )
            delta = TWO if mu == nu else ZERO
            if not mat4_eq(anticom_e, mat4_scale(identity, delta)):
                failures.append(f"euclid clifford {mu}{nu}")

    expected_g5 = mat4_from_blocks(
        matrix_scale(ID2, MINUS_ONE), ZERO2, ZERO2, ID2
    )
    if not mat4_eq(GAMMA5, expected_g5):
        failures.append("gamma5 block value")
    if not mat4_eq(GAMMA5_E, expected_g5):
        failures.append("euclidean gamma5 equals lorentzian gamma5")
    if not mat4_eq(mat4_mul(GAMMA5, GAMMA5), identity):
        failures.append("gamma5 squared")
    for mu in range(4):
        if not mat4_eq(
            mat4_add(mat4_mul(GAMMA5, GAMMA_L[mu]), mat4_mul(GAMMA_L[mu], GAMMA5)),
            mat4_zero(),
        ):
            failures.append(f"gamma5 anticommute {mu}")

    for name, proj in (("PL", P_L), ("PR", P_R)):
        if not mat4_eq(mat4_mul(proj, proj), proj):
            failures.append(f"{name} idempotent")
    if not mat4_eq(mat4_mul(P_L, P_R), mat4_zero()):
        failures.append("PL PR orthogonal")
    if not mat4_eq(mat4_add(P_L, P_R), identity):
        failures.append("PL + PR complete")

    # Wick relations gammaE^j = -i gammaL^j, gammaE^4 = gammaL^0.
    for j in range(3):
        if not mat4_eq(GAMMA_E[j], mat4_scale(GAMMA_L[j + 1], MINUS_I)):
            failures.append(f"wick gamma {j+1}")
    if not mat4_eq(GAMMA_E[3], GAMMA_L[0]):
        failures.append("wick gamma 4")

    # Gamma^{mu nu} block value.
    for mu in range(4):
        for nu in range(4):
            expected = mat4_from_blocks(
                matrix_scale(SIGMA_MUNU[mu][nu], TWO),
                ZERO2,
                ZERO2,
                matrix_scale(BAR_SIGMA_MUNU[mu][nu], TWO),
            )
            if not mat4_eq(GAMMA_MUNU_L[mu][nu], expected):
                failures.append(f"Gamma^munu block {mu}{nu}")
            expected_e = mat4_from_blocks(
                matrix_scale(SIGMA_MN_EU[mu][nu], TWO),
                ZERO2,
                ZERO2,
                matrix_scale(BAR_SIGMA_MN_EU[mu][nu], TWO),
            )
            if not mat4_eq(GAMMA_MN_E[mu][nu], expected_e):
                failures.append(f"euclid Gamma^mn block {mu}{nu}")

    # Contractions with kappa = -1 at d = 4.
    total = mat4_zero()
    for mu in range(4):
        lowered = mat4_scale(GAMMA_L[mu], ETA[mu])
        total = mat4_add(total, mat4_mul(GAMMA_L[mu], lowered))
    if not mat4_eq(total, mat4_scale(identity, MINUS_FOUR)):
        failures.append("gamma^mu gamma_mu = -4")

    for nu in range(4):
        total = mat4_zero()
        for mu in range(4):
            lowered = mat4_scale(GAMMA_L[mu], ETA[mu])
            total = mat4_add(total, mat4_mul(mat4_mul(GAMMA_L[mu], GAMMA_L[nu]), lowered))
        if not mat4_eq(total, mat4_scale(GAMMA_L[nu], TWO)):
            failures.append(f"gamma gamma^nu gamma = 2 gamma^nu ({nu})")

    for nu in range(4):
        for rho in range(4):
            total = mat4_zero()
            for mu in range(4):
                lowered = mat4_scale(GAMMA_L[mu], ETA[mu])
                total = mat4_add(
                    total,
                    mat4_mul(
                        mat4_mul(mat4_mul(GAMMA_L[mu], GAMMA_L[nu]), GAMMA_L[rho]), lowered
                    ),
                )
            eta = ETA[nu] if nu == rho else ZERO
            if not mat4_eq(total, mat4_scale(identity, FOUR * eta if nu == rho else ZERO)):
                failures.append(f"triple contraction {nu}{rho}")

    # Traces.
    for mu in range(4):
        for nu in range(4):
            trace = mat4_trace(mat4_mul(GAMMA_L[mu], GAMMA_L[nu]))
            eta = ETA[mu] if mu == nu else ZERO
            if not (trace - MINUS_FOUR * eta if mu == nu else trace).is_zero():
                failures.append(f"trace gamma pair {mu}{nu}")
            trace_e = mat4_trace(mat4_mul(GAMMA_E[mu], GAMMA_E[nu]))
            delta = FOUR if mu == nu else ZERO
            if not (trace_e - delta).is_zero():
                failures.append(f"euclid trace gamma pair {mu}{nu}")
    for mu in range(4):
        if not mat4_trace(GAMMA_L[mu]).is_zero():
            failures.append(f"trace gamma {mu}")
        if not mat4_trace(mat4_mul(GAMMA5, GAMMA_L[mu])).is_zero():
            failures.append(f"trace gamma5 gamma {mu}")
    if not mat4_trace(GAMMA5).is_zero():
        failures.append("trace gamma5")

    import itertools

    for mu, nu, rho, sigma in itertools.product(range(4), repeat=4):
        product = mat4_mul(
            mat4_mul(GAMMA_L[mu], GAMMA_L[nu]), mat4_mul(GAMMA_L[rho], GAMMA_L[sigma])
        )
        trace = mat4_trace(product)
        eta = lambda m, n: (ETA[m] if m == n else ZERO)
        expected = FOUR * (
            eta(mu, nu) * eta(rho, sigma)
            - eta(mu, rho) * eta(nu, sigma)
            + eta(mu, sigma) * eta(nu, rho)
        )
        if not (trace - expected).is_zero():
            failures.append(f"trace four gammas {mu}{nu}{rho}{sigma}")
        trace5 = mat4_trace(mat4_mul(GAMMA5, product))
        expected5 = MINUS_FOUR * I * Exact.rational(epsilon_sign((mu, nu, rho, sigma)))
        if not (trace5 - expected5).is_zero():
            failures.append(f"trace gamma5 four gammas {mu}{nu}{rho}{sigma}")

    # Duality identities: Gamma^{mu nu rho} = i eps^{mu nu rho sigma} gamma5 gamma_sigma,
    # Gamma^{mu nu rho sigma} = -i eps^{mu nu rho sigma} gamma5  (kappa = -1).
    def normalized_antisym(indices):
        total = mat4_zero()
        count = 0
        import itertools as it

        for perm in it.permutations(range(len(indices))):
            sign = epsilon_sign(perm)
            product = mat4_identity()
            for p in perm:
                product = mat4_mul(product, GAMMA_L[indices[p]])
            total = mat4_add(total, mat4_scale(product, Exact.rational(sign)))
            count += 1
        return mat4_scale(total, Exact.rational(Fraction(1, count)))

    for mu, nu, rho in itertools.product(range(4), repeat=3):
        lhs = normalized_antisym((mu, nu, rho))
        rhs = mat4_zero()
        for sigma in range(4):
            sign = epsilon_sign((mu, nu, rho, sigma))
            if sign == 0:
                continue
            lowered = mat4_scale(mat4_mul(GAMMA5, GAMMA_L[sigma]), ETA[sigma])
            rhs = mat4_add(rhs, mat4_scale(lowered, I * Exact.rational(sign)))
        if not mat4_eq(lhs, rhs):
            failures.append(f"Gamma^mnr duality {mu}{nu}{rho}")

    for mu, nu, rho, sigma in itertools.product(range(4), repeat=4):
        lhs = normalized_antisym((mu, nu, rho, sigma))
        rhs = mat4_scale(GAMMA5, MINUS_I * Exact.rational(epsilon_sign((mu, nu, rho, sigma))))
        if not mat4_eq(lhs, rhs):
            failures.append(f"Gamma^mnrs duality {mu}{nu}{rho}{sigma}")

    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 2: beta and hermiticity (kappa_C = -1 branch).
# ----------------------------------------------------------------------


def check_beta_hermiticity():
    failures = []
    identity = mat4_identity()
    if not mat4_eq(mat4_mul(BETA, BETA), identity):
        failures.append("beta squared")
    if not mat4_eq(mat4_dagger(BETA), BETA):
        failures.append("beta hermitian")
    if not mat4_eq(BETA, GAMMA_L[0]):
        failures.append("beta equals gamma^0 numerically")
    for mu in range(4):
        lhs = mat4_dagger(GAMMA_L[mu])
        rhs = mat4_mul(mat4_mul(BETA, GAMMA_L[mu]), BETA)
        if not mat4_eq(lhs, rhs):
            failures.append(f"gamma dagger {mu}")
        if not mat4_eq(mat4_dagger(GAMMA_E[mu]), GAMMA_E[mu]):
            failures.append(f"euclid gamma hermitian {mu}")
    if not mat4_eq(mat4_dagger(GAMMA5), GAMMA5):
        failures.append("gamma5 hermitian")
    # gamma5^dagger = gamma5 = - beta gamma5 beta^{-1}.
    if not mat4_eq(
        mat4_dagger(GAMMA5), mat4_scale(mat4_mul(mat4_mul(BETA, GAMMA5), BETA), MINUS_ONE)
    ):
        failures.append("gamma5 beta conjugation")
    for mu in range(4):
        lhs = mat4_dagger(mat4_mul(GAMMA5, GAMMA_L[mu]))
        rhs = mat4_mul(mat4_mul(BETA, mat4_mul(GAMMA5, GAMMA_L[mu])), BETA)
        if not mat4_eq(lhs, rhs):
            failures.append(f"gamma5 gamma dagger {mu}")
    for mu in range(4):
        for nu in range(4):
            lhs = mat4_dagger(GAMMA_MUNU_L[mu][nu])
            rhs = mat4_scale(
                mat4_mul(mat4_mul(BETA, GAMMA_MUNU_L[mu][nu]), BETA), MINUS_ONE
            )
            if not mat4_eq(lhs, rhs):
                failures.append(f"Gamma^munu dagger {mu}{nu}")
    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 3: charge conjugation matrix and the Majorana condition.
# ----------------------------------------------------------------------


def conj_gen_default(generator):
    tag, kind, index = generator
    return (tag, "L" if kind == "B" else "B", index)


def check_charge_conjugation_majorana():
    failures = []
    identity = mat4_identity()

    if not mat4_eq(mat4_transpose(CC), mat4_scale(CC, MINUS_ONE)):
        failures.append("C transpose")
    if not mat4_eq(mat4_dagger(CC), mat4_scale(CC, MINUS_ONE)):
        failures.append("C dagger")
    if not mat4_eq(mat4_mul(CC, CC), mat4_scale(identity, MINUS_ONE)):
        failures.append("C squared")
    c_inverse = mat4_scale(CC, MINUS_ONE)

    transpose_signs = []
    for name, matrix, expected_sign in (
        ("identity", identity, ONE),
        ("gamma5", GAMMA5, ONE),
    ):
        lhs = mat4_mul(mat4_mul(c_inverse, matrix), CC)
        if not mat4_eq(lhs, mat4_scale(mat4_transpose(matrix), expected_sign)):
            failures.append(f"C conjugation {name}")
        transpose_signs.append((name, "+1" if expected_sign == ONE else "-1"))
    for mu in range(4):
        for name, matrix, expected_sign in (
            (f"gamma^{mu}", GAMMA_L[mu], MINUS_ONE),
            (f"gamma5 gamma^{mu}", mat4_mul(GAMMA5, GAMMA_L[mu]), ONE),
            (f"gammaE^{mu}", GAMMA_E[mu], MINUS_ONE),
            (f"gamma5 gammaE^{mu}", mat4_mul(GAMMA5, GAMMA_E[mu]), ONE),
        ):
            lhs = mat4_mul(mat4_mul(c_inverse, matrix), CC)
            if not mat4_eq(lhs, mat4_scale(mat4_transpose(matrix), expected_sign)):
                failures.append(f"C conjugation {name}")
    for mu in range(4):
        for nu in range(4):
            for name, matrix in (
                (f"Gamma^{mu}{nu}", GAMMA_MUNU_L[mu][nu]),
                (f"GammaE^{mu}{nu}", GAMMA_MN_E[mu][nu]),
            ):
                lhs = mat4_mul(mat4_mul(c_inverse, matrix), CC)
                if not mat4_eq(lhs, mat4_scale(mat4_transpose(matrix), MINUS_ONE)):
                    failures.append(f"C conjugation {name}")

    # Majorana packaging: barPsi via beta equals barPsi via C; Psi^* = -beta C Psi.
    lower, bar_lower = weyl_pair("psi")
    psi4 = majorana_package(lower, bar_lower)
    bar_c = bar_via_C(psi4)
    bar_b = bar_via_beta(psi4, conj_gen_default)
    for slot in range(4):
        if not poly_eq(bar_c[slot], bar_b[slot]):
            failures.append(f"majorana bar condition slot {slot}")

    conj_column = [conj_single(entry, conj_gen_default) for entry in psi4]
    minus_beta_c = mat4_scale(mat4_mul(BETA, CC), MINUS_ONE)
    reality = mat4_vec(minus_beta_c, psi4)
    for slot in range(4):
        if not poly_eq(conj_column[slot], reality[slot]):
            failures.append(f"majorana reality slot {slot}")

    # Explicit two-component content of barPsi: (psi^a, bar-psi_adot).
    upper = raise_spinor(lower)
    expected_bar = [upper[0], upper[1], bar_lower[0], bar_lower[1]]
    for slot in range(4):
        if not poly_eq(bar_c[slot], expected_bar[slot]):
            failures.append(f"barPsi content slot {slot}")

    return {
        "failure_count": len(failures),
        "failures": failures,
        "transpose_signs": {
            "identity": "+1",
            "gamma5": "+1",
            "gamma5 gamma^mu": "+1",
            "gamma^mu": "-1",
            "Gamma^munu": "-1",
        },
    }


# ----------------------------------------------------------------------
# Check 4: complete bilinear dictionary (Lorentzian and Euclidean).
# ----------------------------------------------------------------------


def check_bilinear_dictionary():
    failures = []

    lower1, bar1 = weyl_pair("chi")
    lower2, bar2 = weyl_pair("psi")
    psi1 = majorana_package(lower1, bar1)
    psi2 = majorana_package(lower2, bar2)
    bar_psi1 = bar_via_C(psi1)
    upper1 = raise_spinor(lower1)
    bar_upper2 = raise_spinor(bar2)
    upper2 = raise_spinor(lower2)

    # scalar
    lhs = row_dot_col(bar_psi1, psi2)
    rhs = poly_add(contract_uu(upper1, lower2), contract_bar(bar1, bar_upper2))
    if not poly_eq(lhs, rhs):
        failures.append("scalar bilinear")
    # pseudoscalar
    lhs = row_dot_col(bar_psi1, mat4_vec(GAMMA5, psi2))
    rhs = poly_add(
        poly_scale(contract_uu(upper1, lower2), MINUS_ONE),
        contract_bar(bar1, bar_upper2),
    )
    if not poly_eq(lhs, rhs):
        failures.append("pseudoscalar bilinear")
    # vector and axial vector
    for mu in range(4):
        lhs = row_dot_col(bar_psi1, mat4_vec(GAMMA_L[mu], psi2))
        rhs = poly_add(
            sigma_contract(upper1, SIGMA_L[mu], bar_upper2),
            bar_sigma_contract(bar1, BAR_SIGMA_L[mu], lower2),
        )
        if not poly_eq(lhs, rhs):
            failures.append(f"vector bilinear {mu}")
        lhs = row_dot_col(bar_psi1, mat4_vec(mat4_mul(GAMMA_L[mu], GAMMA5), psi2))
        rhs = poly_sub(
            sigma_contract(upper1, SIGMA_L[mu], bar_upper2),
            bar_sigma_contract(bar1, BAR_SIGMA_L[mu], lower2),
        )
        if not poly_eq(lhs, rhs):
            failures.append(f"axial bilinear {mu}")
    # tensor
    for mu in range(4):
        for nu in range(4):
            lhs = row_dot_col(bar_psi1, mat4_vec(GAMMA_MUNU_L[mu][nu], psi2))
            rhs = poly_add(
                poly_scale(sigma_munu_contract(upper1, SIGMA_MUNU[mu][nu], lower2), TWO),
                poly_scale(
                    bar_sigma_munu_contract(bar1, BAR_SIGMA_MUNU[mu][nu], bar_upper2), TWO
                ),
            )
            if not poly_eq(lhs, rhs):
                failures.append(f"tensor bilinear {mu}{nu}")

    # Euclidean: independent tilde pair, bar defined through C only.
    for mu in range(4):
        lhs = row_dot_col(bar_psi1, mat4_vec(GAMMA_E[mu], psi2))
        rhs = poly_add(
            sigma_contract(upper1, SIGMA_E[mu], bar_upper2),
            bar_sigma_contract(bar1, BAR_SIGMA_E[mu], lower2),
        )
        if not poly_eq(lhs, rhs):
            failures.append(f"euclid vector bilinear {mu}")

    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 5: Majorana flip signs.
# ----------------------------------------------------------------------


def check_majorana_flips():
    failures = []
    lower1, bar1 = weyl_pair("chi")
    lower2, bar2 = weyl_pair("psi")
    psi1 = majorana_package(lower1, bar1)
    psi2 = majorana_package(lower2, bar2)
    bar_psi1 = bar_via_C(psi1)
    bar_psi2 = bar_via_C(psi2)

    matrices = [("identity", mat4_identity(), ONE), ("gamma5", GAMMA5, ONE)]
    for mu in range(4):
        matrices.append((f"gamma5 gamma^{mu}", mat4_mul(GAMMA5, GAMMA_L[mu]), ONE))
        matrices.append((f"gamma^{mu}", GAMMA_L[mu], MINUS_ONE))
        matrices.append((f"gammaE^{mu}", GAMMA_E[mu], MINUS_ONE))
    for mu in range(4):
        for nu in range(4):
            matrices.append((f"Gamma^{mu}{nu}", GAMMA_MUNU_L[mu][nu], MINUS_ONE))

    for name, matrix, sign in matrices:
        lhs = row_dot_col(bar_psi1, mat4_vec(matrix, psi2))
        rhs = poly_scale(row_dot_col(bar_psi2, mat4_vec(matrix, psi1)), sign)
        if not poly_eq(lhs, rhs):
            failures.append(f"flip {name}")
    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 6: Majorana Fierz identity (Project/Srednicki branch).
# ----------------------------------------------------------------------


def check_majorana_fierz():
    failures = []
    lower, bar_lower = weyl_pair("s")
    s4 = majorana_package(lower, bar_lower)
    bar_s = bar_via_C(s4)

    scalar = row_dot_col(bar_s, s4)
    pseudo = row_dot_col(bar_s, mat4_vec(GAMMA5, s4))
    axial = [
        row_dot_col(bar_s, mat4_vec(mat4_mul(GAMMA5, GAMMA_L[mu]), s4)) for mu in range(4)
    ]

    for alpha in range(4):
        for beta in range(4):
            lhs = poly_mul(s4[alpha], s4[beta])
            rhs = poly_scale(poly_scale(scalar, CC[alpha][beta]), QUARTER)
            g5c = mat4_mul(GAMMA5, CC)
            rhs = poly_add(rhs, poly_scale(poly_scale(pseudo, g5c[alpha][beta]), QUARTER))
            for mu in range(4):
                g5gmuc = mat4_mul(mat4_mul(GAMMA5, mat4_scale(GAMMA_L[mu], ETA[mu])), CC)
                rhs = poly_add(
                    rhs, poly_scale(poly_scale(axial[mu], g5gmuc[alpha][beta]), QUARTER)
                )
            if not poly_eq(lhs, rhs):
                failures.append(f"fierz slot {alpha}{beta}")
    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 7: kinetic and mass equivalence (Lorentzian and Euclidean).
# ----------------------------------------------------------------------


def check_kinetic_equivalence():
    failures = []

    lower, bar_lower = weyl_pair("lam")
    psi4 = majorana_package(lower, bar_lower)
    bar_psi = bar_via_C(psi4)
    upper = raise_spinor(lower)
    bar_upper = raise_spinor(bar_lower)

    # Lorentzian: i bar-lambda bar-sigma^mu d_mu lambda
    #   = (i/2) barPsi gamma^mu d_mu Psi - (i/4) d_mu (barPsi gamma^mu gamma5 Psi).
    lhs = poly_zero()
    for mu in range(4):
        d_lower = [poly_derivative(entry, mu) for entry in lower]
        lhs = poly_add(lhs, poly_scale(bar_sigma_contract(bar_lower, BAR_SIGMA_L[mu], d_lower), I))

    rhs = poly_zero()
    for mu in range(4):
        d_psi = jet_column(psi4, mu)
        rhs = poly_add(
            rhs, poly_scale(row_dot_col(bar_psi, mat4_vec(GAMMA_L[mu], d_psi)), I * HALF)
        )
        axial = row_dot_col(bar_psi, mat4_vec(mat4_mul(GAMMA_L[mu], GAMMA5), psi4))
        rhs = poly_sub(rhs, poly_scale(poly_derivative(axial, mu), I * QUARTER))
    if not poly_eq(lhs, rhs):
        failures.append("lorentzian kinetic equivalence")

    # Single-Majorana vector bilinear vanishes; axial equals -2 bar-lambda bar-sigma lambda.
    for mu in range(4):
        vector = row_dot_col(bar_psi, mat4_vec(GAMMA_L[mu], psi4))
        if not poly_is_zero(vector):
            failures.append(f"majorana vector vanishing {mu}")
        axial = row_dot_col(bar_psi, mat4_vec(mat4_mul(GAMMA_L[mu], GAMMA5), psi4))
        rhs = poly_scale(bar_sigma_contract(bar_lower, BAR_SIGMA_L[mu], lower), MINUS_TWO)
        if not poly_eq(axial, rhs):
            failures.append(f"axial two-component value {mu}")

    # Mass bilinears.
    mass = row_dot_col(bar_psi, psi4)
    expected = poly_add(contract_uu(upper, lower), contract_bar(bar_lower, bar_upper))
    if not poly_eq(mass, expected):
        failures.append("mass bilinear")

    # Euclidean: tilde-lambda bar-sigmaE^m d_m lambda
    #   = (1/2) barPsi gammaE^m d_m Psi - (1/4) d_m (barPsi gammaE^m gamma5 Psi).
    lhs = poly_zero()
    for m in range(4):
        d_lower = [poly_derivative(entry, m) for entry in lower]
        lhs = poly_add(lhs, bar_sigma_contract(bar_lower, BAR_SIGMA_E[m], d_lower))
    rhs = poly_zero()
    for m in range(4):
        d_psi = jet_column(psi4, m)
        rhs = poly_add(rhs, poly_scale(row_dot_col(bar_psi, mat4_vec(GAMMA_E[m], d_psi)), HALF))
        axial = row_dot_col(bar_psi, mat4_vec(mat4_mul(GAMMA_E[m], GAMMA5), psi4))
        rhs = poly_sub(rhs, poly_scale(poly_derivative(axial, m), QUARTER))
    if not poly_eq(lhs, rhs):
        failures.append("euclidean kinetic equivalence")

    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 8: Majorana supersymmetry algebra and superspace monomials.
# ----------------------------------------------------------------------


def check_susy_algebra_superspace():
    failures = []

    # (a) Anticommutator assembly.  Blocks from (1.39): {Q_a, barQ_bdot} =
    # -2 sigma^mu_{a bdot} P_mu; barQ^adot and Q^a raised with eps.
    # Assembled statement: {Q_alpha, barQ^beta} = -2 (gamma^mu)_alpha{}^beta P_mu.
    def q_assembly(sigma, bar_sigma, coefficient):
        # barQ = Q^T C = (Q^a, barQ_adot).  Row index alpha runs over
        # (Q_a, barQ^adot); column index beta over (Q^b, barQ_bdot).
        result = [[poly_zero() for _ in range(4)] for _ in range(4)]
        for mu in range(4):
            p_mu = even_gen("P", mu)
            for a in range(2):
                for b in range(2):
                    result[a][2 + b] = poly_add(
                        result[a][2 + b],
                        poly_scale(p_mu, coefficient * sigma[mu][a][b]),
                    )
            # {barQ^adot, Q^b} = eps^{adot cdot} eps^{b d} {barQ_cdot, Q_d}
            for a in range(2):
                for b in range(2):
                    total = ZERO
                    for c in range(2):
                        for d in range(2):
                            total = total + EPS_UP[a][c] * EPS_UP[b][d] * (
                                coefficient * sigma[mu][d][c]
                            )
                    result[2 + a][b] = poly_add(result[2 + a][b], poly_scale(p_mu, total))
        return result

    for tag, sigma, bar_sigma in (("L", SIGMA_L, BAR_SIGMA_L), ("E", SIGMA_E, BAR_SIGMA_E)):
        gammas = GAMMA_L if tag == "L" else GAMMA_E
        # {Q, barQ} blocks carry -2 sigma (1.39)/(1.68); the covariant
        # derivatives carry +2i sigma in L (2A.29) and -2 sigmaE in E
        # (from (D.5.2)); each assembles to the same gamma statement.
        for coefficient in (MINUS_TWO, TWO * I if tag == "L" else MINUS_TWO):
            assembled = q_assembly(sigma, bar_sigma, coefficient)
            for alpha in range(4):
                for beta in range(4):
                    expected = poly_zero()
                    for mu in range(4):
                        expected = poly_add(
                            expected,
                            poly_scale(
                                even_gen("P", mu), coefficient * gammas[mu][alpha][beta]
                            ),
                        )
                    if not poly_eq(assembled[alpha][beta], expected):
                        failures.append(f"{tag} QQbar assembly {alpha}{beta}")

    # (b) Superspace monomial dictionary.
    theta_upper = [odd_gen("th", "U", a) for a in range(2)]
    theta_lower = lower_spinor(theta_upper)
    bar_theta_lower = [odd_gen("th", "D", a) for a in range(2)]
    bar_theta_upper = raise_spinor(bar_theta_lower)

    big_theta = [theta_lower[0], theta_lower[1], bar_theta_upper[0], bar_theta_upper[1]]
    bar_big_theta = bar_via_C(big_theta)

    expected_bar = [theta_upper[0], theta_upper[1], bar_theta_lower[0], bar_theta_lower[1]]
    for slot in range(4):
        if not poly_eq(bar_big_theta[slot], expected_bar[slot]):
            failures.append(f"barTheta content slot {slot}")

    theta_sq = contract_uu(theta_upper, theta_lower)
    bar_theta_sq = contract_bar(bar_theta_lower, bar_theta_upper)

    if not poly_eq(row_dot_col(bar_big_theta, mat4_vec(P_L, big_theta)), theta_sq):
        failures.append("Theta PL Theta")
    if not poly_eq(row_dot_col(bar_big_theta, mat4_vec(P_R, big_theta)), bar_theta_sq):
        failures.append("Theta PR Theta")
    g5_bilinear = row_dot_col(bar_big_theta, mat4_vec(GAMMA5, big_theta))
    if not poly_eq(g5_bilinear, poly_sub(bar_theta_sq, theta_sq)):
        failures.append("Theta gamma5 Theta")
    if not poly_eq(
        poly_mul(g5_bilinear, g5_bilinear),
        poly_scale(poly_mul(theta_sq, bar_theta_sq), MINUS_TWO),
    ):
        failures.append("(Theta gamma5 Theta)^2")
    if not poly_eq(
        poly_mul(
            row_dot_col(bar_big_theta, mat4_vec(P_L, big_theta)),
            row_dot_col(bar_big_theta, mat4_vec(P_R, big_theta)),
        ),
        poly_mul(theta_sq, bar_theta_sq),
    ):
        failures.append("(Theta PL Theta)(Theta PR Theta)")

    for tag, sigma, gammas in (("L", SIGMA_L, GAMMA_L), ("E", SIGMA_E, GAMMA_E)):
        for mu in range(4):
            lhs = row_dot_col(
                bar_big_theta, mat4_vec(mat4_mul(GAMMA5, gammas[mu]), big_theta)
            )
            b_mu = sigma_contract(theta_upper, sigma[mu], bar_theta_upper)
            if not poly_eq(lhs, poly_scale(b_mu, MINUS_TWO)):
                failures.append(f"{tag} Theta gamma5 gamma Theta {mu}")

    # (c) Chiral/vector superfield monomials with a Majorana fermion package.
    lam_lower, lam_bar_lower = weyl_pair("lam")
    lam4 = majorana_package(lam_lower, lam_bar_lower)
    lam_bar_upper = raise_spinor(lam_bar_lower)

    lhs = row_dot_col(bar_big_theta, mat4_vec(P_L, lam4))
    rhs = contract_uu(theta_upper, lam_lower)
    if not poly_eq(lhs, rhs):
        failures.append("Theta PL Psi")
    lhs = row_dot_col(bar_big_theta, mat4_vec(P_R, lam4))
    rhs = contract_bar(bar_theta_lower, lam_bar_upper)
    if not poly_eq(lhs, rhs):
        failures.append("Theta PR Psi")

    wz_weyl = poly_add(
        poly_scale(poly_mul(theta_sq, contract_bar(bar_theta_lower, lam_bar_upper)), TWO * I),
        poly_scale(poly_mul(bar_theta_sq, contract_uu(theta_upper, lam_lower)), MINUS_TWO * I),
    )
    wz_majorana = poly_add(
        poly_scale(
            poly_mul(theta_sq, row_dot_col(bar_big_theta, mat4_vec(P_R, lam4))), TWO * I
        ),
        poly_scale(
            poly_mul(bar_theta_sq, row_dot_col(bar_big_theta, mat4_vec(P_L, lam4))),
            MINUS_TWO * I,
        ),
    )
    if not poly_eq(wz_weyl, wz_majorana):
        failures.append("Wess-Zumino fermion tail")

    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# N=4 helpers: flavor-indexed packages.
# ----------------------------------------------------------------------


def n4_fields():
    lam_lower = {}
    lamt_lower = {}
    for flavor in range(1, 5):
        lam_lower[flavor] = [odd_gen("Lam", flavor, a) for a in range(2)]
        lamt_lower[flavor] = [odd_gen("Lat", flavor, a) for a in range(2)]
    return lam_lower, lamt_lower


def chiral_left(lam_lower, flavor):
    return [lam_lower[flavor][0], lam_lower[flavor][1], poly_zero(), poly_zero()]


def chiral_right(lamt_lower, flavor):
    upper = raise_spinor(lamt_lower[flavor])
    return [poly_zero(), poly_zero(), upper[0], upper[1]]


def n4_parameters():
    eps_lower = {}
    epst_lower = {}
    for flavor in range(1, 5):
        eps_lower[flavor] = [odd_gen("eps", flavor, a) for a in range(2)]
        epst_lower[flavor] = [odd_gen("ept", flavor, a) for a in range(2)]
    return eps_lower, epst_lower


def f_label(mu, nu) -> Poly:
    if mu == nu:
        return poly_zero()
    if mu < nu:
        return even_gen("F", mu, nu)
    return poly_scale(even_gen("F", nu, mu), MINUS_ONE)


def dphi_label(mu, i, j) -> Poly:
    if i == j:
        return poly_zero()
    if i < j:
        return even_gen("Dp", mu, i, j)
    return poly_scale(even_gen("Dp", mu, j, i), MINUS_ONE)


def dphi_tilde_label(mu, i, j) -> Poly:
    result = poly_zero()
    for k in range(1, 5):
        for l in range(1, 5):
            sign = epsilon_sign((i - 1, j - 1, k - 1, l - 1))
            if sign == 0:
                continue
            result = poly_add(result, poly_scale(dphi_label(mu, k, l), HALF * Exact.rational(sign)))
    return result


def m_label(i, k) -> Poly:
    return even_gen("M", i, k)


def m_tilde_label(i, k) -> Poly:
    """tilde-M_I{}^K := tilde-phi_{IJ} x phi^{JK} = -M^K{}_I  (4C.55)."""
    return poly_scale(m_label(k, i), MINUS_ONE)


# ----------------------------------------------------------------------
# Check 9: N=4 fermion sector of the action.
# ----------------------------------------------------------------------


def check_n4_action_fermion_sector():
    failures = []
    lam_lower, lamt_lower = n4_fields()

    # (a) Yukawa bilinears, all ordered flavor slots.
    for i in range(1, 5):
        for j in range(1, 5):
            left_i = chiral_left(lam_lower, i)
            left_j = chiral_left(lam_lower, j)
            right_i = chiral_right(lamt_lower, i)
            right_j = chiral_right(lamt_lower, j)

            bar_left_i = bar_via_C(left_i)
            bar_right_i = bar_via_C(right_i)

            lhs = row_dot_col(bar_left_i, left_j)
            rhs = contract_uu(raise_spinor(lam_lower[i]), lam_lower[j])
            if not poly_eq(lhs, rhs):
                failures.append(f"yukawa left {i}{j}")

            lhs = row_dot_col(bar_right_i, right_j)
            rhs = contract_bar(lamt_lower[i], raise_spinor(lamt_lower[j]))
            if not poly_eq(lhs, rhs):
                failures.append(f"yukawa right {i}{j}")

            if not poly_is_zero(row_dot_col(bar_left_i, right_j)):
                failures.append(f"chirality orthogonality LR {i}{j}")
            if not poly_is_zero(row_dot_col(bar_right_i, left_j)):
                failures.append(f"chirality orthogonality RL {i}{j}")

    # (b) Kinetic sector, summed over flavors, Lorentzian and Euclidean.
    lhs_l = poly_zero()
    rhs_l = poly_zero()
    lhs_e = poly_zero()
    rhs_e = poly_zero()
    for flavor in range(1, 5):
        lower = lam_lower[flavor]
        bar_lower = lamt_lower[flavor]
        psi4 = majorana_package(lower, bar_lower)
        bar_psi = bar_via_C(psi4)
        for mu in range(4):
            d_lower = [poly_derivative(entry, mu) for entry in lower]
            lhs_l = poly_add(
                lhs_l, poly_scale(bar_sigma_contract(bar_lower, BAR_SIGMA_L[mu], d_lower), I)
            )
            lhs_e = poly_add(lhs_e, bar_sigma_contract(bar_lower, BAR_SIGMA_E[mu], d_lower))
            d_psi = jet_column(psi4, mu)
            rhs_l = poly_add(
                rhs_l, poly_scale(row_dot_col(bar_psi, mat4_vec(GAMMA_L[mu], d_psi)), I * HALF)
            )
            axial_l = row_dot_col(bar_psi, mat4_vec(mat4_mul(GAMMA_L[mu], GAMMA5), psi4))
            rhs_l = poly_sub(rhs_l, poly_scale(poly_derivative(axial_l, mu), I * QUARTER))
            rhs_e = poly_add(
                rhs_e, poly_scale(row_dot_col(bar_psi, mat4_vec(GAMMA_E[mu], d_psi)), HALF)
            )
            axial_e = row_dot_col(bar_psi, mat4_vec(mat4_mul(GAMMA_E[mu], GAMMA5), psi4))
            rhs_e = poly_sub(rhs_e, poly_scale(poly_derivative(axial_e, mu), QUARTER))
    if not poly_eq(lhs_l, rhs_l):
        failures.append("n4 lorentzian kinetic")
    if not poly_eq(lhs_e, rhs_e):
        failures.append("n4 euclidean kinetic")

    return {"failure_count": len(failures), "failures": failures}


# ----------------------------------------------------------------------
# Check 10: the sixteen transformations in Majorana form.
# ----------------------------------------------------------------------


def check_n4_sixteen_transformations():
    failures = []
    lam_lower, lamt_lower = n4_fields()
    eps_lower, epst_lower = n4_parameters()

    def eps_left(flavor):
        return [eps_lower[flavor][0], eps_lower[flavor][1], poly_zero(), poly_zero()]

    def eps_right(flavor):
        upper = raise_spinor(epst_lower[flavor])
        return [poly_zero(), poly_zero(), upper[0], upper[1]]

    for tag in ("L", "E"):
        sigma = SIGMA_L if tag == "L" else SIGMA_E
        bar_sigma = BAR_SIGMA_L if tag == "L" else BAR_SIGMA_E
        smunu = SIGMA_MUNU if tag == "L" else SIGMA_MN_EU
        bar_smunu = BAR_SIGMA_MUNU if tag == "L" else BAR_SIGMA_MN_EU
        gammas = GAMMA_L if tag == "L" else GAMMA_E
        gmunu = GAMMA_MUNU_L if tag == "L" else GAMMA_MN_E
        eta = ETA if tag == "L" else (ONE, ONE, ONE, ONE)

        # Coefficients distinguishing the two signatures:
        #   delta A:      L: -i (4C.24)         E: +1 (4C.44)
        #   delta Psi F:  L: +1/2 Gamma (4C.26) E: -1/2 Gamma (4C.46)
        #   delta Psi D:  L: +i sqrt2 (4C.26)   E: -sqrt2 (4C.46)
        a_coef = MINUS_I if tag == "L" else ONE
        f_coef = HALF if tag == "L" else -HALF
        d_coef = I * SQRT_TWO if tag == "L" else -SQRT_TWO

        # ---- delta A_mu ----
        for mu in range(4):
            sigma_lowered = matrix_scale(sigma[mu], eta[mu])
            bar_sigma_lowered = matrix_scale(bar_sigma[mu], eta[mu])
            weyl = poly_zero()
            for flavor in range(1, 5):
                weyl = poly_add(
                    weyl,
                    poly_scale(
                        sigma_contract(
                            raise_spinor(eps_lower[flavor]),
                            sigma_lowered,
                            raise_spinor(lamt_lower[flavor]),
                        ),
                        a_coef,
                    ),
                )
                weyl = poly_add(
                    weyl,
                    poly_scale(
                        bar_sigma_contract(
                            epst_lower[flavor], bar_sigma_lowered, lam_lower[flavor]
                        ),
                        a_coef,
                    ),
                )
            gamma_lowered = mat4_scale(gammas[mu], eta[mu])
            majorana = poly_zero()
            for flavor in range(1, 5):
                e_l = eps_left(flavor)
                e_r = eps_right(flavor)
                lam_l = chiral_left(lam_lower, flavor)
                lam_r = chiral_right(lamt_lower, flavor)
                majorana = poly_add(
                    majorana,
                    poly_scale(
                        row_dot_col(bar_via_C(e_l), mat4_vec(gamma_lowered, lam_r)), a_coef
                    ),
                )
                majorana = poly_add(
                    majorana,
                    poly_scale(
                        row_dot_col(bar_via_C(e_r), mat4_vec(gamma_lowered, lam_l)), a_coef
                    ),
                )
            if not poly_eq(weyl, majorana):
                failures.append(f"{tag} delta A {mu}")

        # ---- delta phi^{IJ} ----
        for i in range(1, 5):
            for j in range(1, 5):
                weyl = poly_scale(
                    poly_sub(
                        contract_uu(raise_spinor(eps_lower[i]), lam_lower[j]),
                        contract_uu(raise_spinor(eps_lower[j]), lam_lower[i]),
                    ),
                    SQRT_TWO,
                )
                for k in range(1, 5):
                    for l in range(1, 5):
                        sign = epsilon_sign((i - 1, j - 1, k - 1, l - 1))
                        if sign == 0:
                            continue
                        weyl = poly_add(
                            weyl,
                            poly_scale(
                                contract_bar(epst_lower[k], raise_spinor(lamt_lower[l])),
                                SQRT_TWO * Exact.rational(sign),
                            ),
                        )
                majorana = poly_scale(
                    poly_sub(
                        row_dot_col(bar_via_C(eps_left(i)), chiral_left(lam_lower, j)),
                        row_dot_col(bar_via_C(eps_left(j)), chiral_left(lam_lower, i)),
                    ),
                    SQRT_TWO,
                )
                for k in range(1, 5):
                    for l in range(1, 5):
                        sign = epsilon_sign((i - 1, j - 1, k - 1, l - 1))
                        if sign == 0:
                            continue
                        majorana = poly_add(
                            majorana,
                            poly_scale(
                                row_dot_col(
                                    bar_via_C(eps_right(k)), chiral_right(lamt_lower, l)
                                ),
                                SQRT_TWO * Exact.rational(sign),
                            ),
                        )
                if not poly_eq(weyl, majorana):
                    failures.append(f"{tag} delta phi {i}{j}")

        # ---- delta Psi^I: Majorana column ----
        for i in range(1, 5):
            majorana = vec_zero(4)
            for mu in range(4):
                for nu in range(4):
                    term = mat4_vec(
                        gmunu[mu][nu], vec_add(eps_left(i), eps_right(i))
                    )
                    term = [poly_mul(f_label(mu, nu), entry) for entry in term]
                    majorana = vec_add(majorana, vec_scale(term, f_coef))
            for mu in range(4):
                inner = vec_zero(4)
                for j in range(1, 5):
                    inner = vec_add(
                        inner, vec_scale_poly(eps_right(j), dphi_label(mu, i, j))
                    )
                    inner = vec_add(
                        inner, vec_scale_poly(eps_left(j), dphi_tilde_label(mu, i, j))
                    )
                majorana = vec_add(majorana, vec_scale(mat4_vec(gammas[mu], inner), d_coef))
            for k in range(1, 5):
                majorana = vec_add(majorana, vec_scale_poly(eps_left(k), m_label(i, k)))
                majorana = vec_add(majorana, vec_scale_poly(eps_right(k), m_tilde_label(i, k)))

            # Weyl left half: (4C.26) / (4C.46).
            for a in range(2):
                weyl = poly_zero()
                for mu in range(4):
                    for nu in range(4):
                        coefficient = poly_zero()
                        for b in range(2):
                            coefficient = poly_add(
                                coefficient,
                                poly_scale(eps_lower[i][b], smunu[mu][nu][a][b]),
                            )
                        sign = ONE if tag == "L" else MINUS_ONE
                        weyl = poly_add(
                            weyl, poly_scale(poly_mul(f_label(mu, nu), coefficient), sign)
                        )
                for mu in range(4):
                    for j in range(1, 5):
                        coefficient = poly_zero()
                        epst_upper = raise_spinor(epst_lower[j])
                        for b in range(2):
                            coefficient = poly_add(
                                coefficient, poly_scale(epst_upper[b], sigma[mu][a][b])
                            )
                        weyl = poly_add(
                            weyl,
                            poly_scale(poly_mul(dphi_label(mu, i, j), coefficient), d_coef),
                        )
                for k in range(1, 5):
                    weyl = poly_add(weyl, poly_mul(m_label(i, k), eps_lower[k][a]))
                if not poly_eq(weyl, majorana[a]):
                    failures.append(f"{tag} delta Psi left {i} slot {a}")

            # Weyl right half: raised (4C.27) / (4C.47).
            lowered_pair = [
                build_lowered(i, 0, tag, sigma, bar_smunu, eps_lower, epst_lower),
                build_lowered(i, 1, tag, sigma, bar_smunu, eps_lower, epst_lower),
            ]
            for adot in range(2):
                if not poly_eq(raise_component(lowered_pair, adot), majorana[2 + adot]):
                    failures.append(f"{tag} delta Psi right {i} slot {adot}")

        # ---- supersymmetry-current packaging: (4C.59)+(4C.64b) [L],
        #      (4C.66c3 primitive)+(4C.67b2 primitive) [E]. ----
        def matrix2_poly_contract(matrix, spinor, row):
            result = poly_zero()
            for b in range(2):
                result = poly_add(result, poly_scale(spinor[b], matrix[row][b]))
            return result

        f_cur = MINUS_I if tag == "L" else ONE  # left-half F coefficient
        s_cur = SQRT_TWO
        m_cur = I if tag == "L" else ONE
        for i in range(1, 5):
            lam_l = chiral_left(lam_lower, i)
            for mu in range(4):
                # Majorana column.
                col = vec_zero(4)
                psi_i = vec_add(chiral_left(lam_lower, i), chiral_right(lamt_lower, i))
                g5psi = mat4_vec(GAMMA5, psi_i)
                for rho in range(4):
                    for sg in range(4):
                        term = mat4_vec(
                            mat4_mul(gmunu[rho][sg], gammas[mu]), g5psi
                        )
                        term = [poly_mul(f_label(rho, sg), entry) for entry in term]
                        col = vec_add(col, vec_scale(term, f_cur * HALF))
                for nu in range(4):
                    inner = vec_zero(4)
                    for j in range(1, 5):
                        inner = vec_add(
                            inner,
                            vec_scale_poly(
                                chiral_left(lam_lower, j), dphi_tilde_label(nu, i, j)
                            ),
                        )
                        inner = vec_add(
                            inner,
                            vec_scale_poly(
                                chiral_right(lamt_lower, j), dphi_label(nu, i, j)
                            ),
                        )
                    col = vec_add(
                        col,
                        vec_scale(mat4_vec(mat4_mul(gammas[nu], gammas[mu]), inner), s_cur),
                    )
                inner = vec_zero(4)
                for j in range(1, 5):
                    inner = vec_add(
                        inner, vec_scale_poly(chiral_right(lamt_lower, j), m_label(j, i))
                    )
                    inner = vec_add(
                        inner, vec_scale_poly(chiral_left(lam_lower, j), m_label(i, j))
                    )
                col = vec_add(col, vec_scale(mat4_vec(gammas[mu], inner), m_cur))

                # Weyl left half.
                for a in range(2):
                    weyl = poly_zero()
                    for rho in range(4):
                        for sg in range(4):
                            matrix = matrix_multiply(smunu[rho][sg], sigma[mu])
                            weyl = poly_add(
                                weyl,
                                poly_scale(
                                    poly_mul(
                                        f_label(rho, sg),
                                        matrix2_poly_contract(
                                            matrix, raise_spinor(lamt_lower[i]), a
                                        ),
                                    ),
                                    f_cur,
                                ),
                            )
                    for nu in range(4):
                        matrix = matrix_multiply(sigma[nu], bar_sigma[mu])
                        for j in range(1, 5):
                            weyl = poly_add(
                                weyl,
                                poly_scale(
                                    poly_mul(
                                        dphi_tilde_label(nu, i, j),
                                        matrix2_poly_contract(matrix, lam_lower[j], a),
                                    ),
                                    s_cur,
                                ),
                            )
                    for j in range(1, 5):
                        weyl = poly_add(
                            weyl,
                            poly_scale(
                                poly_mul(
                                    m_label(j, i),
                                    matrix2_poly_contract(
                                        sigma[mu], raise_spinor(lamt_lower[j]), a
                                    ),
                                ),
                                m_cur,
                            ),
                        )
                    if not poly_eq(weyl, col[a]):
                        failures.append(f"{tag} current left {i} mu {mu} slot {a}")

                # Weyl right half; the F coefficient is +i in (4C.64b)
                # and -1 in the (4C.67b2) primitive.
                f_bar_cur = I if tag == "L" else MINUS_ONE
                for adot in range(2):
                    weyl = poly_zero()
                    for rho in range(4):
                        for sg in range(4):
                            matrix = matrix_multiply(bar_smunu[rho][sg], bar_sigma[mu])
                            weyl = poly_add(
                                weyl,
                                poly_scale(
                                    poly_mul(
                                        f_label(rho, sg),
                                        matrix2_poly_contract(matrix, lam_lower[i], adot),
                                    ),
                                    f_bar_cur,
                                ),
                            )
                    for nu in range(4):
                        matrix = matrix_multiply(bar_sigma[nu], sigma[mu])
                        for j in range(1, 5):
                            weyl = poly_add(
                                weyl,
                                poly_scale(
                                    poly_mul(
                                        dphi_label(nu, i, j),
                                        matrix2_poly_contract(
                                            matrix, raise_spinor(lamt_lower[j]), adot
                                        ),
                                    ),
                                    s_cur,
                                ),
                            )
                    for j in range(1, 5):
                        weyl = poly_add(
                            weyl,
                            poly_scale(
                                poly_mul(
                                    m_label(i, j),
                                    matrix2_poly_contract(bar_sigma[mu], lam_lower[j], adot),
                                ),
                                m_cur,
                            ),
                        )
                    if not poly_eq(weyl, col[2 + adot]):
                        failures.append(f"{tag} current right {i} mu {mu} slot {adot}")

    return {"failure_count": len(failures), "failures": failures}


def build_lowered(i, adot, tag, sigma, bar_smunu, eps_lower, epst_lower):
    """delta tilde-Lambda_{adot I} from (4C.27) [L] or (4C.47) [E]."""
    lowered = poly_zero()
    for mu in range(4):
        for nu in range(4):
            coefficient = poly_zero()
            for b in range(2):
                coefficient = poly_add(
                    coefficient, poly_scale(epst_lower[i][b], bar_smunu[mu][nu][b][adot])
                )
            sign = MINUS_ONE if tag == "L" else ONE
            lowered = poly_add(lowered, poly_scale(poly_mul(f_label(mu, nu), coefficient), sign))
    for mu in range(4):
        for j in range(1, 5):
            coefficient = poly_zero()
            eps_upper = raise_spinor(eps_lower[j])
            for b in range(2):
                coefficient = poly_add(coefficient, poly_scale(eps_upper[b], sigma[mu][b][adot]))
            sign = MINUS_I * SQRT_TWO if tag == "L" else SQRT_TWO
            lowered = poly_add(
                lowered, poly_scale(poly_mul(dphi_tilde_label(mu, i, j), coefficient), sign)
            )
    for k in range(1, 5):
        lowered = poly_add(lowered, poly_mul(m_tilde_label(i, k), epst_lower[k][adot]))
    return lowered


def raise_component(lowered_pair, adot):
    """X^adot = eps^{adot bdot} X_bdot."""
    result = poly_zero()
    for bdot in range(2):
        result = poly_add(result, poly_scale(lowered_pair[bdot], EPS_UP[adot][bdot]))
    return result


def build_audit():
    checks = {
        "gamma_clifford_chirality_traces": check_gamma_clifford_chirality_traces(),
        "beta_hermiticity": check_beta_hermiticity(),
        "charge_conjugation_majorana": check_charge_conjugation_majorana(),
        "bilinear_dictionary": check_bilinear_dictionary(),
        "majorana_flips": check_majorana_flips(),
        "majorana_fierz": check_majorana_fierz(),
        "kinetic_equivalence": check_kinetic_equivalence(),
        "susy_algebra_superspace": check_susy_algebra_superspace(),
        "n4_action_fermion_sector": check_n4_action_fermion_sector(),
        "n4_sixteen_transformations": check_n4_sixteen_transformations(),
    }
    failure_count = sum(entry["failure_count"] for entry in checks.values())
    return {
        "task": "CONTRACT-STEP-04D-MAJORANA-SPINOR-SYSTEM-001",
        "contract": "contracts/foundations/step-04d-majorana-spinor-system.md",
        "ring": "Q(i,sqrt(2)) with formal anticommuting generators",
        "checks": checks,
        "failure_count": failure_count,
        "status": "PASS" if failure_count == 0 else "FAIL",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-audit", action="store_true", help="write the audit JSON"
    )
    arguments = parser.parse_args()
    audit = build_audit()
    serialized = json.dumps(audit, indent=1, sort_keys=True) + "\n"
    if arguments.write_audit:
        AUDIT_PATH.write_text(serialized, encoding="utf-8")
    print(f"status: {audit['status']}  failures: {audit['failure_count']}")
    for name, entry in audit["checks"].items():
        print(f"  {name}: {entry['failure_count']}")
        for failure in entry["failures"][:8]:
            print(f"    FAIL {failure}")


if __name__ == "__main__":
    main()
