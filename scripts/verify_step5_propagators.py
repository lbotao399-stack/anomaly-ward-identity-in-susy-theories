#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-propagator-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"


@dataclass(frozen=True)
class QComplex:
    """Exact element of Q(i); no floating-point arithmetic is admitted."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QComplex":
        rhs = q(other)
        return QComplex(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "QComplex":
        return QComplex(-self.re, -self.im)

    def __sub__(self, other: object) -> "QComplex":
        return self + (-q(other))

    def __rsub__(self, other: object) -> "QComplex":
        return q(other) - self

    def __mul__(self, other: object) -> "QComplex":
        rhs = q(other)
        return QComplex(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "QComplex":
        rhs = q(other)
        denominator = rhs.re * rhs.re + rhs.im * rhs.im
        if denominator == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return QComplex(
            (self.re * rhs.re + self.im * rhs.im) / denominator,
            (self.im * rhs.re - self.re * rhs.im) / denominator,
        )

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def to_json(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im)}


def q(value: object) -> QComplex:
    if isinstance(value, QComplex):
        return value
    if isinstance(value, Fraction):
        return QComplex(value)
    if isinstance(value, int):
        return QComplex(Fraction(value))
    raise TypeError(f"unsupported exact scalar: {value!r}")


ZERO = QComplex()
ONE = q(1)
I = QComplex(Fraction(0), Fraction(1))

Matrix = list[list[QComplex]]
Polynomial = list[QComplex]


def zeros(rows: int, columns: int) -> Matrix:
    return [[ZERO for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    result = zeros(size, size)
    for index in range(size):
        result[index][index] = ONE
    return result


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def scale(coefficient: object, matrix: Matrix) -> Matrix:
    factor = q(coefficient)
    return [[factor * value for value in row] for row in matrix]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    result = zeros(len(left), len(right[0]))
    for row in range(len(left)):
        for pivot in range(len(right)):
            if not left[row][pivot]:
                continue
            for column in range(len(right[0])):
                if right[pivot][column]:
                    result[row][column] = (
                        result[row][column]
                        + left[row][pivot] * right[pivot][column]
                    )
    return result


def matrix_vector(matrix: Matrix, vector: Polynomial) -> Polynomial:
    return [
        sum((matrix[row][column] * vector[column] for column in range(len(vector))), ZERO)
        for row in range(len(matrix))
    ]


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("inverse requires a square matrix")
    augmented = [
        list(row) + [ONE if row_index == column else ZERO for column in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise ValueError("singular exact matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column or not augmented[row][column]:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                augmented[row][entry] - factor * augmented[column][entry]
                for entry in range(2 * size)
            ]
    return [row[size:] for row in augmented]


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left) * len(right)
    columns = len(left[0]) * len(right[0])
    result = zeros(rows, columns)
    for left_row in range(len(left)):
        for left_column in range(len(left[0])):
            for right_row in range(len(right)):
                for right_column in range(len(right[0])):
                    result[left_row * len(right) + right_row][
                        left_column * len(right[0]) + right_column
                    ] = left[left_row][left_column] * right[right_row][right_column]
    return result


def left_multiply(variable: int) -> Matrix:
    result = zeros(16, 16)
    for monomial in range(16):
        if (monomial >> variable) & 1:
            continue
        lower_count = (monomial & ((1 << variable) - 1)).bit_count()
        result[monomial | (1 << variable)][monomial] = q(-1 if lower_count % 2 else 1)
    return result


def left_derivative(variable: int) -> Matrix:
    result = zeros(16, 16)
    for monomial in range(16):
        if not ((monomial >> variable) & 1):
            continue
        lower_count = (monomial & ((1 << variable) - 1)).bit_count()
        result[monomial ^ (1 << variable)][monomial] = q(-1 if lower_count % 2 else 1)
    return result


def polynomial_basis(mask: int, coefficient: object = 1) -> Polynomial:
    result = [ZERO for _ in range(16)]
    result[mask] = q(coefficient)
    return result


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    return [lhs + rhs for lhs, rhs in zip(left, right)]


def polynomial_scale(coefficient: object, polynomial: Polynomial) -> Polynomial:
    factor = q(coefficient)
    return [factor * value for value in polynomial]


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [ZERO for _ in range(16)]
    for left_mask, left_value in enumerate(left):
        if not left_value:
            continue
        for right_mask, right_value in enumerate(right):
            if not right_value or left_mask & right_mask:
                continue
            inversions = sum(
                1
                for left_index in range(4)
                if (left_mask >> left_index) & 1
                for right_index in range(4)
                if (right_mask >> right_index) & 1 and left_index > right_index
            )
            sign = -1 if inversions % 2 else 1
            result[left_mask | right_mask] = (
                result[left_mask | right_mask]
                + q(sign) * left_value * right_value
            )
    return result


def sigma_e(momentum: tuple[int, int, int, int]) -> Matrix:
    p1, p2, p3, p4 = (Fraction(value) for value in momentum)
    # sigma_E.p = -i p_i sigma_i + p_4 1.
    return [
        [q(p4) - I * p3, -I * p1 - q(p2)],
        [-I * p1 + q(p2), q(p4) + I * p3],
    ]


def bar_sigma_e(momentum: tuple[int, int, int, int]) -> Matrix:
    p1, p2, p3, p4 = (Fraction(value) for value in momentum)
    # bar_sigma_E.p = +i p_i sigma_i + p_4 1.
    return [
        [q(p4) + I * p3, I * p1 + q(p2)],
        [I * p1 - q(p2), q(p4) - I * p3],
    ]


def momentum_square(momentum: tuple[int, int, int, int]) -> Fraction:
    return sum((Fraction(value) ** 2 for value in momentum), Fraction(0))


def flat_operators(momentum: tuple[int, int, int, int]) -> dict[str, Matrix]:
    theta = [left_multiply(0), left_multiply(1)]
    bar_theta_lower = [left_multiply(2), left_multiply(3)]
    derivative = [left_derivative(index) for index in range(4)]
    epsilon_up = [[0, 1], [-1, 0]]
    epsilon_down = [[0, -1], [1, 0]]
    bar_theta_upper = [bar_theta_lower[1], scale(-1, bar_theta_lower[0])]
    bar_derivative_lower = [scale(-1, derivative[3]), derivative[2]]

    sigma_p = sigma_e(momentum)
    i_sigma_p = scale(I, sigma_p)
    d_lower: list[Matrix] = []
    bar_d_lower: list[Matrix] = []
    for undotted in range(2):
        operator = derivative[undotted]
        for dotted in range(2):
            operator = add(
                operator,
                scale(i_sigma_p[undotted][dotted], bar_theta_upper[dotted]),
            )
        d_lower.append(operator)
    for dotted in range(2):
        operator = bar_derivative_lower[dotted]
        for undotted in range(2):
            operator = add(
                operator,
                scale(-i_sigma_p[undotted][dotted], theta[undotted]),
            )
        bar_d_lower.append(operator)

    d_upper = [d_lower[1], scale(-1, d_lower[0])]
    bar_d_upper = [bar_d_lower[1], scale(-1, bar_d_lower[0])]
    d_square = add(
        multiply(d_upper[0], d_lower[0]),
        multiply(d_upper[1], d_lower[1]),
    )
    bar_d_square = add(
        multiply(bar_d_lower[0], bar_d_upper[0]),
        multiply(bar_d_lower[1], bar_d_upper[1]),
    )
    d_bar_d_d = add(
        multiply(multiply(d_upper[0], bar_d_square), d_lower[0]),
        multiply(multiply(d_upper[1], bar_d_square), d_lower[1]),
    )
    square_sum = add(
        multiply(d_square, bar_d_square),
        multiply(bar_d_square, d_square),
    )
    p_squared = momentum_square(momentum)
    if not p_squared:
        raise ValueError("the Step-5 residual-free operator algebra requires p_(4)^2 != 0")
    pi_half = scale(Fraction(1, 8) / p_squared, d_bar_d_d)
    pi_zero = scale(Fraction(-1, 16) / p_squared, square_sum)
    return {
        "D_plus": d_lower[0],
        "D_minus": d_lower[1],
        "barD_plus": bar_d_lower[0],
        "barD_minus": bar_d_lower[1],
        "D2": d_square,
        "barD2": bar_d_square,
        "DbarD2D": d_bar_d_d,
        "square_sum": square_sum,
        "Pi_half": pi_half,
        "Pi_zero": pi_zero,
        "identity": identity(16),
        "zero": zeros(16, 16),
    }


def operator_checks(momentum: tuple[int, int, int, int]) -> dict[str, bool]:
    operators = flat_operators(momentum)
    p_squared = momentum_square(momentum)
    d_square = operators["D2"]
    bar_d_square = operators["barD2"]
    d_bar_d_d = operators["DbarD2D"]
    square_sum = operators["square_sum"]
    pi_half = operators["Pi_half"]
    pi_zero = operators["Pi_zero"]
    unit = operators["identity"]
    zero = operators["zero"]
    return {
        "identity_5_37": d_bar_d_d
        == add(scale(8 * p_squared, unit), scale(Fraction(1, 2), square_sum)),
        "identity_5_38_D": multiply(multiply(d_square, bar_d_square), d_square)
        == scale(-16 * p_squared, d_square),
        "identity_5_38_barD": multiply(multiply(bar_d_square, d_square), bar_d_square)
        == scale(-16 * p_squared, bar_d_square),
        "Pi_half_idempotent": multiply(pi_half, pi_half) == pi_half,
        "Pi_zero_idempotent": multiply(pi_zero, pi_zero) == pi_zero,
        "Pi_left_orthogonal": multiply(pi_half, pi_zero) == zero,
        "Pi_right_orthogonal": multiply(pi_zero, pi_half) == zero,
        "Pi_complete": add(pi_half, pi_zero) == unit,
    }


def vector_checks(momentum: tuple[int, int, int, int]) -> dict[str, bool]:
    operators = flat_operators(momentum)
    p_squared = momentum_square(momentum)
    h = Fraction(3, 2)
    g_squared = Fraction(2, 3)
    kappa = [[q(2), q(1)], [q(1), q(1)]]
    kappa_inverse = [[q(1), q(-1)], [q(-1), q(2)]]
    pi_half = operators["Pi_half"]
    pi_zero = operators["Pi_zero"]
    unit16 = operators["identity"]
    physical_from_derivatives = scale(Fraction(-1, 16) * h, operators["DbarD2D"])
    physical_from_projector = scale(Fraction(-1, 2) * h * p_squared, pi_half)
    gauge_fixing = scale(Fraction(-1, 2) * h * p_squared, pi_zero)
    total_operator = add(physical_from_derivatives, gauge_fixing)
    expected_total_operator = scale(Fraction(-1, 2) * h * p_squared, unit16)
    inverse_operator = scale(-2 * g_squared / p_squared, unit16)

    full_kernel = kronecker(kappa, total_operator)
    full_inverse = kronecker(kappa_inverse, inverse_operator)
    unit32 = identity(32)
    return {
        "physical_5_43": physical_from_derivatives == physical_from_projector,
        "step5a_total_5_45": total_operator == expected_total_operator,
        "h_times_g_squared_is_one": h * g_squared == 1,
        "kappa_left_inverse": multiply(kappa, kappa_inverse) == identity(2),
        "kappa_right_inverse": multiply(kappa_inverse, kappa) == identity(2),
        "step5a_inverse_5_46_left": multiply(full_kernel, full_inverse) == unit32,
        "step5a_inverse_5_46_right": multiply(full_inverse, full_kernel) == unit32,
    }


def b_polynomial(momentum: tuple[int, int, int, int]) -> Polynomial:
    sigma_p = sigma_e(momentum)
    theta = [polynomial_basis(1), polynomial_basis(2)]
    bar_theta_upper = [polynomial_basis(8), polynomial_scale(-1, polynomial_basis(4))]
    result = polynomial_basis(0, 0)
    for undotted in range(2):
        for dotted in range(2):
            result = polynomial_add(
                result,
                polynomial_scale(
                    sigma_p[undotted][dotted],
                    polynomial_multiply(theta[undotted], bar_theta_upper[dotted]),
                ),
            )
    return result


def chiral_embeddings(momentum: tuple[int, int, int, int]) -> tuple[list[Polynomial], list[Polynomial]]:
    # Phi(p)=exp(+i p.B)(phi + theta^a chi_a + theta^2 F), chi=sqrt(2) psi.
    # tildePhi(-p)=exp(+i p.B)(tildephi + bartheta_dot-a tildechi^dot-a
    #                                      + bartheta^2 tildeF).
    b_value = b_polynomial(momentum)
    exponential = polynomial_add(
        polynomial_add(polynomial_basis(0), polynomial_scale(I, b_value)),
        polynomial_scale(Fraction(-1, 2), polynomial_multiply(b_value, b_value)),
    )
    chiral_bases = [
        polynomial_basis(0),
        polynomial_basis(1),
        polynomial_basis(2),
        polynomial_basis(3, -2),  # theta^2=-2 theta^+ theta^-
    ]
    antichiral_bases = [
        polynomial_basis(0),
        polynomial_basis(4),
        polynomial_basis(8),
        polynomial_basis(12, 2),  # bartheta^2=2 bartheta_dot+ bartheta_dot-
    ]
    return (
        [polynomial_multiply(exponential, basis) for basis in chiral_bases],
        [polynomial_multiply(exponential, basis) for basis in antichiral_bases],
    )


def d_integral(polynomial: Polynomial) -> QComplex:
    # theta^2 bartheta^2=-4 theta+ theta- bartheta_dot+ bartheta_dot-.
    return q(Fraction(-1, 4)) * polynomial[15]


def chiral_pairing(momentum: tuple[int, int, int, int]) -> Matrix:
    chiral, antichiral = chiral_embeddings(momentum)
    component_parities = [0, 1, 1, 0]
    result = zeros(4, 4)
    for anti_index, anti_polynomial in enumerate(antichiral):
        for chiral_index, chiral_polynomial in enumerate(chiral):
            # Components are displayed to the right of their theta monomials.  Moving the
            # odd antichiral coefficient through the odd chiral monomial supplies this
            # Koszul sign; omitting it reverses the fermion kinetic operator.
            koszul = -1 if component_parities[anti_index] * component_parities[chiral_index] else 1
            result[anti_index][chiral_index] = q(koszul) * d_integral(
                polynomial_multiply(anti_polynomial, chiral_polynomial)
            )
    return result


def chiral_checks(momentum: tuple[int, int, int, int]) -> dict[str, bool]:
    p_squared = momentum_square(momentum)
    chiral, antichiral = chiral_embeddings(momentum)
    operators_p = flat_operators(momentum)
    operators_minus_p = flat_operators(tuple(-entry for entry in momentum))

    pairing = chiral_pairing(momentum)
    hessian = scale(-1, pairing)  # S_E,2=-h kappa [tildePhi Phi]_D; h=kappa=1 here.
    hessian_inverse = inverse(hessian)
    unit4 = identity(4)

    epsilon_down = [[0, -1], [1, 0]]
    fermion_kernel = zeros(2, 2)
    for undotted in range(2):
        for dotted_lower in range(2):
            fermion_kernel[undotted][dotted_lower] = Fraction(1, 2) * sum(
                (
                    hessian_inverse[1 + undotted][1 + dotted_upper]
                    * epsilon_down[dotted_lower][dotted_upper]
                    for dotted_upper in range(2)
                ),
                ZERO,
            )
    expected_fermion = scale(-I / p_squared, sigma_e(momentum))

    chiral_constraint = all(
        matrix_vector(operators_p[name], column) == [ZERO for _ in range(16)]
        for name in ("barD_plus", "barD_minus")
        for column in chiral
    )
    antichiral_constraint = all(
        matrix_vector(operators_minus_p[name], column) == [ZERO for _ in range(16)]
        for name in ("D_plus", "D_minus")
        for column in antichiral
    )
    fermion_only_block = all(
        pairing[row][column] == ZERO
        for row in range(4)
        for column in range(4)
        if (row in (1, 2)) != (column in (1, 2))
    )
    return {
        "chiral_embedding_annihilated_by_barD": chiral_constraint,
        "antichiral_embedding_at_minus_p_annihilated_by_D": antichiral_constraint,
        "pairing_scalar_block": pairing[0][0] == q(-p_squared),
        "pairing_auxiliary_block": pairing[3][3] == ONE,
        "pairing_no_boson_fermion_mix": fermion_only_block,
        "hessian_inverse_left": multiply(hessian, hessian_inverse) == unit4,
        "hessian_inverse_right": multiply(hessian_inverse, hessian) == unit4,
        "scalar_green_kernel": hessian_inverse[0][0] == q(Fraction(1, 1) / p_squared),
        "fermion_green_kernel": fermion_kernel == expected_fermion,
        "auxiliary_green_kernel": hessian_inverse[3][3] == q(-1),
    }


def fp_checks(momentum: tuple[int, int, int, int]) -> dict[str, bool]:
    operators = flat_operators(momentum)
    zero = operators["zero"]
    # From (3D.84), sV|_{V=0}=i(tilde c-c).  Equations (3D.86),(3D.91) give
    # M_+(tilde c)=-(i/4) barD^2 tilde c and M_-(c)=+(i/4) D^2 c.
    m_plus_tilde = scale(-I / 4, operators["barD2"])
    m_minus_chiral = scale(I / 4, operators["D2"])
    return {
        "M_plus_is_chiral_plus": multiply(operators["barD_plus"], m_plus_tilde) == zero,
        "M_plus_is_chiral_minus": multiply(operators["barD_minus"], m_plus_tilde) == zero,
        "M_minus_is_antichiral_plus": multiply(operators["D_plus"], m_minus_chiral) == zero,
        "M_minus_is_antichiral_minus": multiply(operators["D_minus"], m_minus_chiral) == zero,
    }


def flatten_checks(grouped: dict[str, dict[str, bool]]) -> list[dict[str, object]]:
    return [
        {"id": f"{group}.{name}", "passed": passed}
        for group, checks in grouped.items()
        for name, passed in checks.items()
    ]


def run_verification() -> dict[str, object]:
    momenta = [(0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)]
    grouped: dict[str, dict[str, bool]] = {}
    for momentum in momenta:
        label = "p_" + "_".join(str(entry).replace("-", "m") for entry in momentum)
        grouped[f"operator.{label}"] = operator_checks(momentum)
        grouped[f"vector.{label}"] = vector_checks(momentum)
        grouped[f"chiral.{label}"] = chiral_checks(momentum)
        grouped[f"fp.{label}"] = fp_checks(momentum)
    checks = flatten_checks(grouped)
    failed = [check for check in checks if not check["passed"]]
    contract_sha256 = hashlib.sha256(CONTRACT.read_bytes()).hexdigest()
    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "contract": str(CONTRACT.relative_to(ROOT)),
        "contract_sha256": contract_sha256,
        "arithmetic": "EXACT_Q_I_NO_FLOATING_POINT",
        "status": "PASS" if not failed else "FAIL",
        "admission_status": (
            "PHYSICAL_HESSIANS_AND_STEP5A_VECTOR_GREEN_VERIFIED"
            if not failed
            else "CONTRACT_OPERATOR_MISMATCH"
        ),
        "momenta": [list(momentum) for momentum in momenta],
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "derived_rules": {
            "vector_hessian": "K_V,AB^phys=-(h/2) kappa_AB p_(4)^2 Pi_1/2",
            "step5a_vector_green_kernel": "G_V^{AB}=-(2 g^2/p_(4)^2) kappa^{AB} 1_16",
            "chiral_hessian": "K_(tilde q q),AB=-h kappa_AB B_component(p)",
            "scalar_green_kernel": "G_(phi tildephi)^{AB}=g^2 kappa^{AB}/p_(4)^2",
            "fermion_green_kernel": "G_(psi_a tildepsi_dotb)^{AB}=-i g^2 kappa^{AB} p_(a dotb)/p_(4)^2",
            "auxiliary_green_kernel": "G_(F tildeF)^{AB}=-g^2 kappa^{AB}",
            "gaussian_wick_factor_if_admitted": "hbar times the ordered Green kernel",
            "source_order": "int_(E,+) J_Phi Phi + int_(E,-) tildePhi tildeJ_Phi; forward derivative order is J_Phi then tildeJ_Phi",
            "reverse_fermion_order": "G_(tildepsi_dotb psi_a)(-p,p)=-G_(psi_a tildepsi_dotb)(p,-p)",
        },
        "typed_blockers": [],
        "step5c_obligations": [
            {
                "id": "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
                "scope": "equivalence of the admitted Step-5A vector kernel to a global local non-minimal coefficient integral",
                "reason": "The fixed-gauge Step-5A Gaussian is admitted independently; only its global local-Y realization remains a Step-5C obligation.",
            },
            {
                "id": "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
                "scope": "finite coefficient-space reconstruction of the Step-5A vector Wick contraction",
                "reason": "The complete (A_T,lambda,tilde-lambda,d) finite cycle and Berezinian remain Step 5C; they do not alter the reference-flat Step-5A inversion.",
            },
            {
                "id": "BLOCKED_FP_GHOST_CYCLE_UNDECLARED",
                "scope": "finite FP coefficient-space cycle",
                "reason": "The primitive connected one-loop FP graph is separately proved absent; the global finite cycle remains Step 5C.",
            },
            {
                "id": "BLOCKED_NK_BRANCH_AND_KERNEL_UNFIXED",
                "scope": "finite Nielsen-Kallosh coefficient-space cycle",
                "reason": "The primitive connected one-loop NK graph is separately proved absent; the global finite cycle remains Step 5C.",
            },
        ],
        "source_boundary": {
            "project_equations_used": ["2A.41", "3A.9-3A.16", "3D.84-3D.94", "4C.4", "5.37-5.46"],
            "weinberg_coefficients_used": False,
            "superspace_1001_coefficients_used": False,
            "anomaly_coefficient_computed": False,
        },
    }


def main() -> int:
    result = run_verification()
    AUDIT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["totals"], sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
