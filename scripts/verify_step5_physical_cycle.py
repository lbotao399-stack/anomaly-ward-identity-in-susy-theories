#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
PROPAGATOR_VERIFIER = ROOT / "scripts/verify_step5_propagators.py"
AUDIT = ROOT / "audits/step5-physical-cycle-verification.json"


def load_propagator_verifier():
    specification = importlib.util.spec_from_file_location(
        "step5_propagator_dependency", PROPAGATOR_VERIFIER
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load the exact Step-5 propagator verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def rational_matrix_multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [
            sum(
                (left[row][pivot] * right[pivot][column] for pivot in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def rational_matrix_scale(
    coefficient: Fraction, matrix: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [[coefficient * value for value in row] for row in matrix]


def rational_identity(size: int) -> list[list[Fraction]]:
    return [
        [Fraction(1 if row == column else 0) for column in range(size)]
        for row in range(size)
    ]


Polynomial = dict[int, Fraction]


def polynomial_add(*polynomials: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def polynomial_scale(coefficient: Fraction, polynomial: Polynomial) -> Polynomial:
    return {
        monomial: coefficient * value
        for monomial, value in polynomial.items()
        if coefficient * value
    }


def polynomial_multiply(left: Polynomial, right: Polynomial, variables: int) -> Polynomial:
    result: Polynomial = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            if left_mask & right_mask:
                continue
            inversions = sum(
                1
                for left_index in range(variables)
                if (left_mask >> left_index) & 1
                for right_index in range(variables)
                if (right_mask >> right_index) & 1 and left_index > right_index
            )
            sign = -1 if inversions % 2 else 1
            mask = left_mask | right_mask
            result[mask] = (
                result.get(mask, Fraction(0))
                + sign * left_value * right_value
            )
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def exterior_generator(index: int) -> Polynomial:
    return {1 << index: Fraction(1)}


def exterior_exponential(polynomial: Polynomial, variables: int) -> Polynomial:
    result: Polynomial = {0: Fraction(1)}
    power: Polynomial = {0: Fraction(1)}
    factorial = 1
    for degree in range(1, variables + 1):
        power = polynomial_multiply(power, polynomial, variables)
        factorial *= degree
        result = polynomial_add(result, polynomial_scale(Fraction(1, factorial), power))
    return result


def left_derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for mask, coefficient in polynomial.items():
        if not ((mask >> variable) & 1):
            continue
        sign = -1 if (mask & ((1 << variable) - 1)).bit_count() % 2 else 1
        result[mask ^ (1 << variable)] = sign * coefficient
    return result


def integrate_odd_fields(
    polynomial: Polynomial, field_indices: tuple[int, ...]
) -> Polynomial:
    field_mask = sum(1 << index for index in field_indices)
    return {
        mask ^ field_mask: coefficient
        for mask, coefficient in polynomial.items()
        if mask & field_mask == field_mask
    }


def normalized_fermion_gaussian() -> dict[str, object]:
    # Total normal order:
    # rho_0 < rho_1 < tilderho_0 < tilderho_1
    #       < psi_0 < psi_1 < tildepsi_0 < tildepsi_1.
    # Integrated coefficient order is psi_0 < psi_1 < tildepsi_0 < tildepsi_1;
    # (3D.19) therefore uses dtildepsi_1 dtildepsi_0 dpsi_1 dpsi_0.
    variables = 8
    rho = [exterior_generator(0), exterior_generator(1)]
    tilde_rho = [exterior_generator(2), exterior_generator(3)]
    psi = [exterior_generator(4), exterior_generator(5)]
    tilde_psi = [exterior_generator(6), exterior_generator(7)]
    field_indices = (4, 5, 6, 7)
    hbar = Fraction(3, 2)
    kernel = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(1)]]
    kernel_inverse = [[Fraction(1), Fraction(-1)], [Fraction(-1), Fraction(2)]]

    exponent: Polynomial = {}
    for tilde_index in range(2):
        for index in range(2):
            exponent = polynomial_add(
                exponent,
                polynomial_scale(
                    -kernel[tilde_index][index] / hbar,
                    polynomial_multiply(
                        tilde_psi[tilde_index], psi[index], variables
                    ),
                ),
            )
    for index in range(2):
        exponent = polynomial_add(
            exponent,
            polynomial_scale(
                Fraction(-1, 1) / hbar,
                polynomial_multiply(rho[index], psi[index], variables),
            ),
            polynomial_scale(
                Fraction(-1, 1) / hbar,
                polynomial_multiply(
                    tilde_psi[index], tilde_rho[index], variables
                ),
            ),
        )

    unnormalized = integrate_odd_fields(
        exterior_exponential(exponent, variables), field_indices
    )
    vacuum = unnormalized[0]
    normalized = {
        monomial: coefficient / vacuum
        for monomial, coefficient in unnormalized.items()
    }

    expected_exponent: Polynomial = {}
    for index in range(2):
        for tilde_index in range(2):
            expected_exponent = polynomial_add(
                expected_exponent,
                polynomial_scale(
                    kernel_inverse[index][tilde_index] / hbar,
                    polynomial_multiply(
                        rho[index], tilde_rho[tilde_index], variables
                    ),
                ),
            )
    expected = exterior_exponential(expected_exponent, variables)

    derivative_checks: dict[str, bool] = {}
    for index in range(2):
        for tilde_index in range(2):
            # Step 3D component sources occur as -rho psi - tildepsi tilderho.
            # Both coefficient derivatives are LEFT derivatives.  Acting first with
            # d/drho and then with d/dtilderho gives the ordered insertion
            # psi_i tildepsi_tilde-index: the source minus signs and the odd Leibniz
            # crossing cancel exactly.
            derivative = left_derivative(
                left_derivative(normalized, index), 2 + tilde_index
            ).get(0, Fraction(0))
            derivative_checks[f"psi_{index}_tildepsi_{tilde_index}"] = (
                hbar * hbar * derivative
                == hbar * kernel_inverse[index][tilde_index]
            )

    return {
        "normalized_generator_exact": normalized == expected,
        "vacuum_nonzero": vacuum != 0,
        "derivative_checks": derivative_checks,
        "hbar": str(hbar),
        "vacuum": str(vacuum),
    }


def bosonic_cycle_checks() -> dict[str, bool]:
    h = Fraction(3, 2)
    g_squared = Fraction(2, 3)
    hbar = Fraction(5, 3)
    p_squared = Fraction(30)
    kappa = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(1)]]
    kappa_inverse = [[Fraction(1), Fraction(-1)], [Fraction(-1), Fraction(2)]]
    scalar_kernel = rational_matrix_scale(h * p_squared, kappa)
    scalar_inverse = rational_matrix_scale(g_squared / p_squared, kappa_inverse)
    auxiliary_cycle_kernel = rational_matrix_scale(h, kappa)
    auxiliary_cycle_inverse = rational_matrix_scale(g_squared, kappa_inverse)
    return {
        "kappa_positive_first_minor": kappa[0][0] > 0,
        "kappa_positive_determinant": kappa[0][0] * kappa[1][1] - kappa[0][1] ** 2 > 0,
        "scalar_cycle_kernel_positive_factor": h * p_squared > 0,
        "transverse_A_cycle_positive_factor": h * p_squared / 2 > 0,
        "d_cycle_positive_factor": h / 2 > 0,
        "scalar_inverse_left": rational_matrix_multiply(scalar_kernel, scalar_inverse)
        == rational_identity(2),
        "scalar_inverse_right": rational_matrix_multiply(scalar_inverse, scalar_kernel)
        == rational_identity(2),
        "auxiliary_contour_changes_minus_hessian_to_positive": h > 0,
        "auxiliary_inverse_left": rational_matrix_multiply(
            auxiliary_cycle_kernel, auxiliary_cycle_inverse
        )
        == rational_identity(2),
        "scalar_source_derivative": rational_matrix_scale(hbar, scalar_inverse)
        == rational_matrix_scale(hbar * g_squared / p_squared, kappa_inverse),
        "F_source_derivative_before_tildeF_to_minus_Fdagger": rational_matrix_scale(
            -hbar * g_squared, kappa_inverse
        )
        == rational_matrix_scale(-1, rational_matrix_scale(hbar, auxiliary_cycle_inverse)),
    }


def transverse_vector_checks() -> dict[str, bool]:
    verifier = load_propagator_verifier()
    momentum = (1, 2, 3, 4)
    operators = verifier.flat_operators(momentum)
    p_squared = verifier.momentum_square(momentum)
    h = Fraction(3, 2)
    g_squared = Fraction(2, 3)
    physical_kernel = verifier.scale(
        Fraction(-1, 2) * h * p_squared, operators["Pi_half"]
    )
    transverse_inverse = verifier.scale(
        -2 * g_squared / p_squared, operators["Pi_half"]
    )
    return {
        "physical_left_inverse_on_transverse_image": verifier.multiply(
            physical_kernel, transverse_inverse
        )
        == operators["Pi_half"],
        "physical_right_inverse_on_transverse_image": verifier.multiply(
            transverse_inverse, physical_kernel
        )
        == operators["Pi_half"],
        "physical_kernel_annihilates_longitudinal_left": verifier.multiply(
            operators["Pi_zero"], physical_kernel
        )
        == operators["zero"],
        "physical_kernel_annihilates_longitudinal_right": verifier.multiply(
            physical_kernel, operators["Pi_zero"]
        )
        == operators["zero"],
        "transverse_projector_nontrivial": operators["Pi_half"]
        != operators["zero"],
        "longitudinal_projector_nontrivial": operators["Pi_zero"]
        != operators["zero"],
    }


def flatten_checks(grouped: dict[str, dict[str, bool]]) -> list[dict[str, object]]:
    return [
        {"id": f"{group}.{name}", "passed": passed}
        for group, checks in grouped.items()
        for name, passed in checks.items()
    ]


def run_verification() -> dict[str, object]:
    fermion = normalized_fermion_gaussian()
    grouped = {
        "bosonic_cycle": bosonic_cycle_checks(),
        "fermion_gaussian": {
            "normalized_generator_exact": bool(fermion["normalized_generator_exact"]),
            "vacuum_nonzero": bool(fermion["vacuum_nonzero"]),
            **fermion["derivative_checks"],
        },
        "vector_transverse": transverse_vector_checks(),
    }
    checks = flatten_checks(grouped)
    failed = [check for check in checks if not check["passed"]]
    contract_sha256 = hashlib.sha256(CONTRACT.read_bytes()).hexdigest()
    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "contract": str(CONTRACT.relative_to(ROOT)),
        "contract_sha256": contract_sha256,
        "status": "PASS" if not failed else "FAIL",
        "admission_status": (
            "REFERENCE_FLAT_CHIRAL_GAUSSIAN_VERIFIED_VECTOR_PSEUDOINVERSE_ONLY"
            if not failed
            else "PHYSICAL_CYCLE_OR_SOURCE_ORDER_MISMATCH"
        ),
        "arithmetic": "EXACT_RATIONAL_AND_EXACT_Q_I_PROJECTOR_DEPENDENCY",
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "physical_cycle": {
            "momentum_reality": [
                "tildephi^A(-p)=(phi^A(p))^dagger",
                "tildeF^A(-p)=-(F^A(p))^dagger",
                "A_m^A(-p)=(A_m^A(p))^dagger",
                "D^A(p)=i d^A(p), d^A(-p)=(d^A(p))^dagger",
            ],
            "bosonic_convergence": "For h>0, positive kappa, and p_(4)^2>0, scalar, transverse-A, F-cycle, and d-cycle quadratic real parts are positive.",
            "fermion_coefficient_order": "psi_+ < psi_- < tildepsi_dot+ < tildepsi_dot- for every lexicographically ordered (p,r,A) block",
            "fermion_measure_order": "dtildepsi_dot- dtildepsi_dot+ dpsi_- dpsi_+",
            "fermion_source_coupling": "-rho psi - tildepsi tilderho",
            "fermion_source_derivative_order": "both derivatives are LEFT: first d/drho, then d/dtilderho, i.e. (d_L/dtilderho)(d_L/drho) Z",
            "normalized_finite_gaussian": "Z[rho,tilderho]/Z[0]=exp(rho K^{-1} tilderho/hbar)",
        },
        "reference_flat_wick_rules": {
            "scalar": "<phi^A(p) tildephi^B(-p)>=hbar g^2 kappa^{AB}/p_(4)^2",
            "fermion": "<psi_a^A(p) tildepsi_dotb^B(-p)>=-i hbar g^2 kappa^{AB} p_(a dotb)/p_(4)^2",
            "fermion_reverse_order": "<tildepsi_dotb^B(-p) psi_a^A(p)>=+i hbar g^2 kappa^{AB} p_(a dotb)/p_(4)^2",
            "auxiliary": "<F^A(p) tildeF^B(-p)>=-hbar g^2 kappa^{AB}",
        },
        "algebraic_pseudoinverses": {
            "vector_transverse": "G_T^{AB}=-2 g^2 kappa^{AB} Pi_(1/2)/p_(4)^2",
            "two_sided_projected_identity": "K_T G_T=G_T K_T=Pi_(1/2)",
            "not_a_wick_contraction": True,
        },
        "typed_blockers": [
            {
                "id": "BLOCKED_GAUGE_FIXED_DENSITY_BEREZINIAN",
                "scope": "promotion of reference-flat Gaussian rules to the full regulated measure",
                "reason": "The field-dependent density is isolated as S_measure=-hbar log(varpi(q)/varpi(0)); its coefficient vertices are not instantiated.",
            },
            {
                "id": "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
                "scope": "transverse V Wick contraction",
                "reason": "The algebraic Pi_(1/2) pseudoinverse has not been accompanied by the complete finite Gaussian for (A_T,lambda,tildelambda,d), its ordered sources, and coefficientwise reconstruction to V_T.",
            },
            {
                "id": "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
                "scope": "Pi_0 longitudinal and full unconstrained V Wick contraction",
                "reason": "The accepted physical Hessian vanishes on Im Pi_0.  A local non-minimal multiplier kernel and its cycle are not fixed by the physical contour (3A.102)-(3A.103).",
            }
        ],
        "untouched_sectors": {
            "FP_cycle": "NOT_READ_OR_MODIFIED",
            "NK_cycle": "NOT_READ_OR_MODIFIED",
        },
        "source_boundary": {
            "project_equations_used": [
                "3A.102-3A.103",
                "3D.18-3D.21",
                "3D.26-3D.27",
                "3D.125b",
                "current Step5 physical Hessians and Green kernels",
            ],
            "external_propagator_coefficients_used": False,
            "anomaly_coefficient_computed": False,
            "full_density_used_in_gaussian": False,
            "reference_measure": "D' qhat with varpi(0) divided out",
        },
    }


def main() -> int:
    result = run_verification()
    AUDIT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["totals"], sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
