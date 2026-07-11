#!/usr/bin/env python3
"""Exact algebraic checks for the Weinberg--Srednicki--project dictionary.

The coefficient field is Q(i).  No floating point or external CAS is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import verify_step2a_flat_superspace as flat


@dataclass(frozen=True)
class C:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "C") -> "C":
        return C(self.re + other.re, self.im + other.im)

    def __neg__(self) -> "C":
        return C(-self.re, -self.im)

    def __sub__(self, other: "C") -> "C":
        return self + (-other)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conjugate(self) -> "C":
        return C(self.re, -self.im)


Z = C()
O = C(Fraction(1))
M = C(Fraction(-1))
I = C(Fraction(0), Fraction(1))
MI = C(Fraction(0), Fraction(-1))
H = C(Fraction(1, 2))
IH = C(Fraction(0), Fraction(1, 2))

Matrix = tuple[tuple[C, ...], ...]


def mat(rows: list[list[C]]) -> Matrix:
    return tuple(tuple(row) for row in rows)


def zeros(n: int, m: int) -> Matrix:
    return tuple(tuple(Z for _ in range(m)) for _ in range(n))


def eye(n: int) -> Matrix:
    return tuple(tuple(O if i == j else Z for j in range(n)) for i in range(n))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def sub(a: Matrix, b: Matrix) -> Matrix:
    return add(a, scale(b, M))


def scale(a: Matrix, c: C) -> Matrix:
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Z)
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(mul(a, b), mul(b, a))


def anticomm(a: Matrix, b: Matrix) -> Matrix:
    return add(mul(a, b), mul(b, a))


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def dagger(a: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j].conjugate() for i in range(len(a)))
        for j in range(len(a[0]))
    )


def trace(a: Matrix) -> C:
    return sum((a[i][i] for i in range(len(a))), Z)


def block(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    top = tuple(tuple(a[i]) + tuple(b[i]) for i in range(len(a)))
    bottom = tuple(tuple(c[i]) + tuple(d[i]) for i in range(len(c)))
    return top + bottom


def product(*matrices: Matrix) -> Matrix:
    result = eye(len(matrices[0]))
    for matrix in matrices:
        result = mul(result, matrix)
    return result


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def antisymmetrized(gamma: tuple[Matrix, ...], indices: tuple[int, ...]) -> Matrix:
    result = zeros(len(gamma[0]), len(gamma[0]))
    factorial = 1
    for n in range(2, len(indices) + 1):
        factorial *= n
    for order in permutations(range(len(indices))):
        term = product(*(gamma[indices[position]] for position in order))
        result = add(result, scale(term, C(Fraction(permutation_sign(order)))))
    return scale(result, C(Fraction(1, factorial)))


def epsilon4(a: int, b: int, c: int, d: int) -> int:
    values = (a, b, c, d)
    if len(set(values)) != 4:
        return 0
    return permutation_sign(values)


GrassmannQuadratic = dict[tuple[int, int], C]


def grassmann_pair(i: int, j: int) -> GrassmannQuadratic:
    if i == j:
        return {}
    if i < j:
        return {(i, j): O}
    return {(j, i): M}


def poly_add(a: GrassmannQuadratic, b: GrassmannQuadratic) -> GrassmannQuadratic:
    result = dict(a)
    for key, value in b.items():
        total = result.get(key, Z) + value
        if total == Z:
            result.pop(key, None)
        else:
            result[key] = total
    return result


def poly_scale(a: GrassmannQuadratic, coefficient: C) -> GrassmannQuadratic:
    return {key: coefficient * value for key, value in a.items() if coefficient * value != Z}


def grassmann_bilinear(a: Matrix) -> GrassmannQuadratic:
    result: GrassmannQuadratic = {}
    for i in range(len(a)):
        for j in range(len(a)):
            result = poly_add(result, poly_scale(grassmann_pair(i, j), a[i][j]))
    return result


def grassmann_cross_bilinear(a: Matrix, right_offset: int) -> GrassmannQuadratic:
    result: GrassmannQuadratic = {}
    for i in range(len(a)):
        for j in range(len(a)):
            result = poly_add(
                result,
                poly_scale(grassmann_pair(i, right_offset + j), a[i][j]),
            )
    return result


def exterior_multiply(
    left: dict[tuple[int, ...], C],
    right: dict[tuple[int, ...], C],
) -> dict[tuple[int, ...], C]:
    result: dict[tuple[int, ...], C] = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            if set(left_key) & set(right_key):
                continue
            inversions = sum(a > b for a in left_key for b in right_key)
            coefficient = left_value * right_value
            if inversions % 2:
                coefficient = M * coefficient
            key = tuple(sorted(left_key + right_key))
            total = result.get(key, Z) + coefficient
            if total == Z:
                result.pop(key, None)
            else:
                result[key] = total
    return result


def main() -> None:
    one2 = eye(2)
    zero2 = zeros(2, 2)
    pauli = (
        mat([[Z, O], [O, Z]]),
        mat([[Z, MI], [I, Z]]),
        mat([[O, Z], [Z, M]]),
    )
    sigma = (one2,) + pauli
    barsigma = (one2,) + tuple(scale(s, M) for s in pauli)
    eta = (-1, 1, 1, 1)

    checks: dict[str, bool] = {}
    for mu in range(4):
        for nu in range(4):
            rhs = scale(one2, C(Fraction(-2 * eta[mu] if mu == nu else 0)))
            checks[f"sigma_clifford_{mu}_{nu}"] = (
                add(mul(sigma[mu], barsigma[nu]), mul(sigma[nu], barsigma[mu])) == rhs
            )

    gamma_s = tuple(block(zero2, sigma[mu], barsigma[mu], zero2) for mu in range(4))
    gamma_w = tuple(scale(gamma, MI) for gamma in gamma_s)
    one4 = eye(4)
    for mu in range(4):
        for nu in range(4):
            rhs_s = scale(one4, C(Fraction(-2 * eta[mu] if mu == nu else 0)))
            rhs_w = scale(one4, C(Fraction(+2 * eta[mu] if mu == nu else 0)))
            checks[f"srednicki_clifford_{mu}_{nu}"] = anticomm(gamma_s[mu], gamma_s[nu]) == rhs_s
            checks[f"weinberg_clifford_{mu}_{nu}"] = anticomm(gamma_w[mu], gamma_w[nu]) == rhs_w

    gamma5_s = scale(product(*gamma_s), I)
    gamma5_w = scale(product(*gamma_w), MI)
    checks["gamma5_phase"] = gamma5_w == scale(gamma5_s, M)
    checks["gamma5_s_square"] = mul(gamma5_s, gamma5_s) == one4
    checks["gamma5_w_square"] = mul(gamma5_w, gamma5_w) == one4

    beta_s = gamma_s[0]
    beta_w = scale(gamma_w[0], I)
    checks["beta_identity"] = beta_w == beta_s

    c_matrix = block(scale(pauli[1], MI), zero2, zero2, scale(pauli[1], I))
    c_inverse = scale(c_matrix, M)
    checks["charge_conjugation_transpose"] = transpose(c_matrix) == scale(c_matrix, M)
    checks["charge_conjugation_dagger"] = dagger(c_matrix) == scale(c_matrix, M)
    checks["charge_conjugation_square"] = mul(c_matrix, c_matrix) == scale(one4, M)
    for label, gamma, beta, kappa in (
        ("srednicki", gamma_s, beta_s, -1),
        ("weinberg", gamma_w, beta_w, +1),
    ):
        for mu in range(4):
            hermitian_rhs = scale(mul(mul(beta, gamma[mu]), beta), C(Fraction(-kappa)))
            checks[f"{label}_gamma_hermiticity_{mu}"] = dagger(gamma[mu]) == hermitian_rhs
            checks[f"{label}_charge_conjugation_{mu}"] = (
                mul(mul(c_inverse, gamma[mu]), c_matrix) == scale(transpose(gamma[mu]), M)
            )

    for mu in range(4):
        for nu in range(4):
            generator_s = scale(comm(gamma_s[mu], gamma_s[nu]), C(Fraction(0), Fraction(1, 4)))
            generator_w = scale(comm(gamma_w[mu], gamma_w[nu]), C(Fraction(0), Fraction(-1, 4)))
            checks[f"lorentz_generator_{mu}_{nu}"] = generator_w == generator_s

    projector_w_plus = scale(add(one4, gamma5_w), H)
    projector_w_minus = scale(sub(one4, gamma5_w), H)
    projector_s_left = scale(sub(one4, gamma5_s), H)
    projector_s_right = scale(add(one4, gamma5_s), H)
    checks["projector_plus_left"] = projector_w_plus == projector_s_left
    checks["projector_minus_right"] = projector_w_minus == projector_s_right

    # Project sigma^{mu nu}=1/4(sigma^mu barsigma^nu-sigma^nu barsigma^mu).
    # Srednicki S_L^{mu nu}=i times this matrix.
    for mu in range(4):
        for nu in range(4):
            project_sigma = scale(sub(mul(sigma[mu], barsigma[nu]), mul(sigma[nu], barsigma[mu])), C(Fraction(1, 4)))
            srednicki_sl = scale(sub(mul(sigma[mu], barsigma[nu]), mul(sigma[nu], barsigma[mu])), C(Fraction(0), Fraction(1, 4)))
            checks[f"project_srednicki_spin_generator_{mu}_{nu}"] = srednicki_sl == scale(project_sigma, I)

    # Coefficients in X=A d_theta+B sigma bartheta d_x and
    # Xbar=C d_bartheta+D theta sigma d_x; {X,Xbar}=(AD-BC)sigma d_x.
    q_s = (O, I, O, MI)
    q_project = (MI, O, MI, M)
    d_s = (O, MI, O, I)
    d_project = (O, MI, O, I)

    def bracket_coefficient(coefficients: tuple[C, C, C, C]) -> C:
        a, b, c, d = coefficients
        return a * d - b * c

    checks["coordinate_Q_phase_all_terms"] = q_project == tuple(MI * value for value in q_s)
    checks["coordinate_Q_srednicki_bracket"] = bracket_coefficient(q_s) == C(Fraction(0), Fraction(-2))
    checks["coordinate_Q_project_bracket"] = bracket_coefficient(q_project) == C(Fraction(0), Fraction(2))
    checks["covariant_D_identity_all_terms"] = d_project == d_s
    checks["covariant_D_bracket"] = bracket_coefficient(d_project) == C(Fraction(0), Fraction(2))

    # Independent exterior-algebra realization of Srednicki's operators in the
    # project's primitive (theta^a, bartheta_dot a) basis.
    flat_basis = tuple(flat.super_basis(mask) for mask in range(1 << flat.N_GRASSMANN))

    def flat_operator_equal(left: flat.Operator, right: flat.Operator) -> bool:
        return all(
            flat.super_normalize(left(value)) == flat.super_normalize(right(value))
            for value in flat_basis
        )

    def flat_scaled(operator: flat.Operator, coefficient: flat.GaussianInteger) -> flat.Operator:
        return lambda value: flat.super_scale(operator(value), coefficient)

    def make_srednicki_operators(
        bosonic_derivative: callable,
    ) -> tuple[tuple[flat.Operator, ...], tuple[flat.Operator, ...], tuple[flat.Operator, ...], tuple[flat.Operator, ...]]:
        q_ops: list[flat.Operator] = []
        bar_q_ops: list[flat.Operator] = []
        d_ops: list[flat.Operator] = []
        bar_d_ops: list[flat.Operator] = []

        for a in range(2):
            def q_sred(value: flat.SuperPolynomial, a: int = a) -> flat.SuperPolynomial:
                result = flat.theta_derivative(a, value)
                for mu in range(4):
                    differentiated = bosonic_derivative(mu, value)
                    for dotted in range(2):
                        term = flat.raised_bar_theta_multiply(dotted, differentiated)
                        coefficient = flat.I * flat.SIGMA_LORENTZ[mu][a][dotted]
                        result = flat.super_add(result, flat.super_scale(term, coefficient))
                return flat.super_normalize(result)

            def d_sred(value: flat.SuperPolynomial, a: int = a) -> flat.SuperPolynomial:
                result = flat.theta_derivative(a, value)
                for mu in range(4):
                    differentiated = bosonic_derivative(mu, value)
                    for dotted in range(2):
                        term = flat.raised_bar_theta_multiply(dotted, differentiated)
                        coefficient = flat.MINUS_I * flat.SIGMA_LORENTZ[mu][a][dotted]
                        result = flat.super_add(result, flat.super_scale(term, coefficient))
                return flat.super_normalize(result)

            q_ops.append(q_sred)
            d_ops.append(d_sred)

        for dotted in range(2):
            def bar_q_sred(value: flat.SuperPolynomial, dotted: int = dotted) -> flat.SuperPolynomial:
                result = flat.lower_bar_derivative(dotted, value)
                for mu in range(4):
                    differentiated = bosonic_derivative(mu, value)
                    for a in range(2):
                        term = flat.theta_multiply(a, differentiated)
                        coefficient = flat.MINUS_I * flat.SIGMA_LORENTZ[mu][a][dotted]
                        result = flat.super_add(result, flat.super_scale(term, coefficient))
                return flat.super_normalize(result)

            def bar_d_sred(value: flat.SuperPolynomial, dotted: int = dotted) -> flat.SuperPolynomial:
                result = flat.lower_bar_derivative(dotted, value)
                for mu in range(4):
                    differentiated = bosonic_derivative(mu, value)
                    for a in range(2):
                        term = flat.theta_multiply(a, differentiated)
                        coefficient = flat.I * flat.SIGMA_LORENTZ[mu][a][dotted]
                        result = flat.super_add(result, flat.super_scale(term, coefficient))
                return flat.super_normalize(result)

            bar_q_ops.append(bar_q_sred)
            bar_d_ops.append(bar_d_sred)

        return tuple(q_ops), tuple(bar_q_ops), tuple(d_ops), tuple(bar_d_ops)

    project_momentum_ops = flat.make_flat_operators("Lorentzian", flat.super_bosonic_momentum)
    q_s_ops, bar_q_s_ops, d_s_ops, bar_d_s_ops = make_srednicki_operators(flat.super_bosonic_momentum)
    for a in range(2):
        checks[f"exterior_coordinate_Q_phase_{a}"] = flat_operator_equal(
            project_momentum_ops.q[a], flat_scaled(q_s_ops[a], flat.MINUS_I)
        )
        checks[f"exterior_covariant_D_identity_{a}"] = flat_operator_equal(
            project_momentum_ops.d[a], d_s_ops[a]
        )
        checks[f"exterior_bar_coordinate_Q_phase_{a}"] = flat_operator_equal(
            project_momentum_ops.bar_q[a], flat_scaled(bar_q_s_ops[a], flat.MINUS_I)
        )
        checks[f"exterior_bar_covariant_D_identity_{a}"] = flat_operator_equal(
            project_momentum_ops.bar_d[a], bar_d_s_ops[a]
        )

    dx_ops: tuple[flat.Operator, ...] = tuple(
        (lambda value, mu=mu: flat.super_bosonic_momentum(mu, value))
        for mu in range(4)
    )
    for a in range(2):
        for dotted in range(2):
            sred_q_rhs = flat.linear_combination(
                (
                    (
                        flat.MINUS_TWO * flat.I * flat.SIGMA_LORENTZ[mu][a][dotted],
                        dx_ops[mu],
                    )
                    for mu in range(4)
                )
            )
            project_q_rhs = flat.linear_combination(
                (
                    (
                        flat.TWO * flat.I * flat.SIGMA_LORENTZ[mu][a][dotted],
                        dx_ops[mu],
                    )
                    for mu in range(4)
                )
            )
            d_rhs = flat.linear_combination(
                (
                    (
                        flat.TWO * flat.I * flat.SIGMA_LORENTZ[mu][a][dotted],
                        dx_ops[mu],
                    )
                    for mu in range(4)
                )
            )
            checks[f"exterior_srednicki_Q_bracket_{a}_{dotted}"] = flat_operator_equal(
                flat.operator_anticommutator(q_s_ops[a], bar_q_s_ops[dotted]),
                sred_q_rhs,
            )
            checks[f"exterior_project_Q_bracket_{a}_{dotted}"] = flat_operator_equal(
                flat.operator_anticommutator(
                    project_momentum_ops.q[a], project_momentum_ops.bar_q[dotted]
                ),
                project_q_rhs,
            )
            checks[f"exterior_covariant_D_bracket_{a}_{dotted}"] = flat_operator_equal(
                flat.operator_anticommutator(d_s_ops[a], bar_d_s_ops[dotted]),
                d_rhs,
            )

    project_coordinate_ops = flat.make_flat_operators("Lorentzian", flat.super_bosonic_derivative)
    for mu in range(4):
        y_mu = flat.super_bosonic_coordinate(mu)
        for a in range(2):
            for dotted in range(2):
                monomial = flat.theta_multiply(
                    a,
                    flat.raised_bar_theta_multiply(dotted, flat.super_one()),
                )
                coefficient = flat.MINUS_I * flat.SIGMA_LORENTZ[mu][a][dotted]
                y_mu = flat.super_add(y_mu, flat.super_scale(monomial, coefficient))
        for dotted in range(2):
            checks[f"exterior_chiral_coordinate_{mu}_{dotted}"] = (
                project_coordinate_ops.bar_d[dotted](y_mu) == {}
            )

    # Normalized antisymmetric products, contractions, traces, and dualities.
    for label, gamma, gamma5, kappa in (
        ("srednicki", gamma_s, gamma5_s, -1),
        ("weinberg", gamma_w, gamma5_w, +1),
    ):
        lowered = tuple(scale(gamma[mu], C(Fraction(eta[mu]))) for mu in range(4))
        contracted_one = zeros(4, 4)
        for mu in range(4):
            contracted_one = add(contracted_one, mul(gamma[mu], lowered[mu]))
        checks[f"{label}_contract_one"] = contracted_one == scale(one4, C(Fraction(4 * kappa)))

        for nu in range(4):
            contracted_three = zeros(4, 4)
            for mu in range(4):
                contracted_three = add(
                    contracted_three,
                    product(gamma[mu], gamma[nu], lowered[mu]),
                )
            checks[f"{label}_contract_three_{nu}"] = (
                contracted_three == scale(gamma[nu], C(Fraction(-2 * kappa)))
            )

            for rho in range(4):
                contracted_four = zeros(4, 4)
                for mu in range(4):
                    contracted_four = add(
                        contracted_four,
                        product(gamma[mu], gamma[nu], gamma[rho], lowered[mu]),
                    )
                rhs = scale(one4, C(Fraction(4 * eta[nu] if nu == rho else 0)))
                checks[f"{label}_contract_four_{nu}_{rho}"] = contracted_four == rhs

        for mu in range(4):
            for nu in range(4):
                expected_two_trace = C(Fraction(4 * kappa * eta[mu] if mu == nu else 0))
                checks[f"{label}_trace_two_{mu}_{nu}"] = trace(mul(gamma[mu], gamma[nu])) == expected_two_trace
                gamma_two = antisymmetrized(gamma, (mu, nu))
                dual_two_rhs = zeros(4, 4)
                for rho in range(4):
                    for sigma_index in range(4):
                        eps = epsilon4(mu, nu, rho, sigma_index)
                        if not eps:
                            continue
                        gamma_two_lower = scale(
                            antisymmetrized(gamma, (rho, sigma_index)),
                            C(Fraction(eta[rho] * eta[sigma_index])),
                        )
                        dual_two_rhs = add(
                            dual_two_rhs,
                            scale(gamma_two_lower, C(Fraction(0), Fraction(-kappa * eps, 2))),
                        )
                checks[f"{label}_dual_two_{mu}_{nu}"] = mul(gamma5, gamma_two) == dual_two_rhs

                for rho in range(4):
                    gamma_three = antisymmetrized(gamma, (mu, nu, rho))
                    dual_three_rhs = zeros(4, 4)
                    for sigma_index in range(4):
                        eps = epsilon4(mu, nu, rho, sigma_index)
                        if eps:
                            dual_three_rhs = add(
                                dual_three_rhs,
                                scale(mul(gamma5, lowered[sigma_index]), C(Fraction(0), Fraction(eps))),
                            )
                    checks[f"{label}_dual_three_{mu}_{nu}_{rho}"] = gamma_three == dual_three_rhs

                    for sigma_index in range(4):
                        four_trace = trace(product(gamma[mu], gamma[nu], gamma[rho], gamma[sigma_index]))
                        expected_four_trace = C(
                            Fraction(
                                4
                                * (
                                    (eta[mu] if mu == nu else 0) * (eta[rho] if rho == sigma_index else 0)
                                    - (eta[mu] if mu == rho else 0) * (eta[nu] if nu == sigma_index else 0)
                                    + (eta[mu] if mu == sigma_index else 0) * (eta[nu] if nu == rho else 0)
                                )
                            )
                        )
                        checks[f"{label}_trace_four_{mu}_{nu}_{rho}_{sigma_index}"] = (
                            four_trace == expected_four_trace
                        )
                        gamma5_trace = trace(product(gamma5, gamma[mu], gamma[nu], gamma[rho], gamma[sigma_index]))
                        checks[f"{label}_trace_gamma5_{mu}_{nu}_{rho}_{sigma_index}"] = (
                            gamma5_trace == C(Fraction(0), Fraction(4 * kappa * epsilon4(mu, nu, rho, sigma_index)))
                        )
                        gamma_four = antisymmetrized(gamma, (mu, nu, rho, sigma_index))
                        dual_four_rhs = scale(
                            gamma5,
                            C(Fraction(0), Fraction(kappa * epsilon4(mu, nu, rho, sigma_index))),
                        )
                        checks[f"{label}_dual_four_{mu}_{nu}_{rho}_{sigma_index}"] = gamma_four == dual_four_rhs

    # W/S Majorana reality, adjoint phase, kinetic factors, and indexed Fierz identities.
    reality_s = scale(mul(beta_s, c_matrix), M)
    reality_w = mul(beta_w, c_matrix)
    checks["majorana_reality_phase_branch"] = scale(reality_s, MI) == scale(reality_w, I)
    checks["majorana_bar_phase_branch"] = scale(c_matrix, M * I) == scale(c_matrix, MI)
    checks["majorana_kinetic_phase"] = M * MI * MI * I == I
    checks["majorana_mass_phase"] = MI * I == O

    quarter = C(Fraction(1, 4))
    for label, gamma, gamma5, bar_sign, channel_signs in (
        ("weinberg", gamma_w, gamma5_w, M, (M, M, O)),
        ("srednicki", gamma_s, gamma5_s, O, (O, O, O)),
    ):
        gamma_lower = tuple(scale(gamma[mu], C(Fraction(eta[mu]))) for mu in range(4))

        def barred_bilinear(operator: Matrix) -> GrassmannQuadratic:
            return poly_scale(grassmann_bilinear(mul(c_matrix, operator)), bar_sign)

        scalar = barred_bilinear(one4)
        pseudoscalar = barred_bilinear(gamma5)
        axial = tuple(barred_bilinear(mul(gamma5, gamma[mu])) for mu in range(4))
        scalar_sign, pseudoscalar_sign, axial_sign = channel_signs

        for alpha in range(4):
            for beta_index in range(4):
                lhs = grassmann_pair(alpha, beta_index)
                rhs: GrassmannQuadratic = {}
                rhs = poly_add(
                    rhs,
                    poly_scale(
                        scalar,
                        quarter * scalar_sign * c_matrix[alpha][beta_index],
                    ),
                )
                gamma5_c = mul(gamma5, c_matrix)
                rhs = poly_add(
                    rhs,
                    poly_scale(
                        pseudoscalar,
                        quarter * pseudoscalar_sign * gamma5_c[alpha][beta_index],
                    ),
                )
                for mu in range(4):
                    gamma5_gamma_c = product(gamma5, gamma_lower[mu], c_matrix)
                    rhs = poly_add(
                        rhs,
                        poly_scale(
                            axial[mu],
                            quarter * axial_sign * gamma5_gamma_c[alpha][beta_index],
                        ),
                    )
                checks[f"{label}_fierz_{alpha}_{beta_index}"] = lhs == rhs

    # Four-component superspace-coordinate bridge for the declared branch
    # Theta_W=-i Theta_S, with Theta_S=(theta_a, theta*^dot a)^T.
    epsilon_spinor_w = block(scale(pauli[1], I), zero2, zero2, scale(pauli[1], I))
    theta_square: GrassmannQuadratic = {(0, 1): C(Fraction(-2))}
    bar_theta_square: GrassmannQuadratic = {(2, 3): C(Fraction(2))}
    theta_minus_bar = poly_add(theta_square, poly_scale(bar_theta_square, M))

    theta_w_bar_gamma5_theta_w = poly_scale(
        grassmann_bilinear(product(gamma5_w, epsilon_spinor_w, gamma5_w)),
        M,
    )
    checks["superspace_barTheta_gamma5_Theta"] = theta_w_bar_gamma5_theta_w == theta_minus_bar

    theta_w_left_square = poly_scale(
        grassmann_bilinear(product(gamma5_w, epsilon_spinor_w, projector_w_plus)),
        M,
    )
    checks["superspace_left_quadratic"] = theta_w_left_square == theta_square

    theta_psi_matrix = product(transpose(projector_w_plus), epsilon_spinor_w, projector_w_plus)
    minus_theta_w_psi_w = poly_scale(grassmann_cross_bilinear(theta_psi_matrix, 4), M)
    theta_psi_expected: GrassmannQuadratic = {(1, 4): O, (0, 5): M}
    checks["superspace_chiral_fermion_contraction"] = minus_theta_w_psi_w == theta_psi_expected

    bilinear_square = exterior_multiply(theta_w_bar_gamma5_theta_w, theta_w_bar_gamma5_theta_w)
    theta_bar_product = exterior_multiply(theta_square, bar_theta_square)
    checks["superspace_D_quartic_bridge"] = bilinear_square == poly_scale(theta_bar_product, C(Fraction(-2)))
    checks["superspace_D_grassmann_factor"] = (
        poly_scale(bilinear_square, C(Fraction(-1, 4)))
        == poly_scale(theta_bar_product, C(Fraction(1, 2)))
    )

    for mu in range(4):
        theta_sigma_bar: GrassmannQuadratic = {}
        for dotted in range(2):
            theta_sigma_bar = poly_add(
                theta_sigma_bar,
                {(1, 2 + dotted): sigma[mu][0][dotted]},
            )
            theta_sigma_bar = poly_add(
                theta_sigma_bar,
                {(0, 2 + dotted): M * sigma[mu][1][dotted]},
            )
        x_shift_w = poly_scale(
            grassmann_bilinear(
                product(gamma5_w, epsilon_spinor_w, gamma5_w, gamma_w[mu])
            ),
            M,
        )
        checks[f"superspace_chiral_coordinate_bridge_{mu}"] = (
            x_shift_w == poly_scale(theta_sigma_bar, C(Fraction(0), Fraction(-2)))
        )

    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": 1,
        "task": "CONTRACT-WEINBERG-SREDNICKI-CODEX-DICTIONARY-001",
        "coefficient_field": "Q(i)",
        "checks": checks,
        "totals": {"checks": len(checks), "failed": len(failed)},
        "failed_checks": failed,
        "status": "PASS" if not failed else "FAIL",
    }
    output = Path(__file__).resolve().parents[1] / "audits/ws-dictionary/exact-verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))
    print(json.dumps(result["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
