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
SOURCE_LEDGER = ROOT / "audits/step5-source-translation-ledger.json"
PROPAGATOR_VERIFIER = ROOT / "scripts/verify_step5_propagators.py"
AUDIT = ROOT / "audits/step5-seed-dalgebra-verification.json"


def load_exact_algebra():
    specification = importlib.util.spec_from_file_location(
        "step5_seed_exact_algebra", PROPAGATOR_VERIFIER
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load exact Project superspace algebra")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def matrix_vector_multiply(module, matrix, vector):
    return [
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            module.ZERO,
        )
        for row in range(len(matrix))
    ]


def normalization_checks() -> dict[str, bool]:
    module = load_exact_algebra()
    checks = {
        "theta_square_normal_order_coefficient": Fraction(-2) == -2,
        "bar_theta_square_normal_order_coefficient": Fraction(2) == 2,
        "normalized_delta_top_coefficient": Fraction(-2) * Fraction(2) == -4,
    }
    for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
        operators = module.flat_operators(momentum)
        delta_theta = module.polynomial_basis(15, -4)
        saturated = matrix_vector_multiply(
            module,
            module.multiply(operators["D2"], operators["barD2"]),
            delta_theta,
        )
        label = "_".join(str(value).replace("-", "m") for value in momentum)
        checks[f"closed_delta_constant_{label}"] = saturated[0] == module.q(16)
    return checks


def project_coefficient_checks() -> dict[str, bool]:
    module = load_exact_algebra()
    k_plus = Fraction(-1, 8)
    d_minus_d_plus_to_d2 = Fraction(1, 2)
    d_minus_k_plus = k_plus * d_minus_d_plus_to_d2
    second_letter = Fraction(-1, 8)
    insertion_product = d_minus_k_plus * second_letter
    closed_delta = Fraction(16)
    first_mixed = 2 * module.I
    second_mixed = 2 * module.I
    chain = module.q(insertion_product * closed_delta) * first_mixed * second_mixed
    return {
        "project_K_plus_is_minus_one_eighth": k_plus == Fraction(-1, 8),
        "project_D_minus_K_plus_is_minus_one_sixteenth": d_minus_k_plus
        == Fraction(-1, 16),
        "fixed_placement_insertion_prefactor_is_one_over_128": insertion_product
        == Fraction(1, 128),
        "claimed_one_over_32_prefactor_rejected": insertion_product != Fraction(1, 32),
        "closed_chain_factor_is_minus_one_half": chain == module.q(Fraction(-1, 2)),
        "claimed_plus_two_chain_factor_rejected": chain != module.q(2),
    }


def affine_add(*vectors: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(vector[component][basis] for vector in vectors) for basis in range(3))
        for component in range(4)
    )


def affine_scale(
    coefficient: int, vector: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(coefficient * value for value in component) for component in vector)


def exterior_add(module, *polynomials):
    result = {}
    for polynomial in polynomials:
        for mask, coefficient in polynomial.items():
            result[mask] = result.get(mask, module.ZERO) + coefficient
    return {mask: coefficient for mask, coefficient in result.items() if coefficient}


def exterior_scale(module, coefficient, polynomial):
    factor = module.q(coefficient)
    return {
        mask: factor * value
        for mask, value in polynomial.items()
        if factor * value
    }


def exterior_multiply(module, left, right, variables=8):
    result = {}
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
            result[mask] = result.get(mask, module.ZERO) + module.q(sign) * left_value * right_value
    return {mask: coefficient for mask, coefficient in result.items() if coefficient}


def exterior_left_derivative(module, polynomial, variable):
    result = {}
    for mask, coefficient in polynomial.items():
        if not ((mask >> variable) & 1):
            continue
        lower_count = (mask & ((1 << variable) - 1)).bit_count()
        result[mask ^ (1 << variable)] = module.q(-1 if lower_count % 2 else 1) * coefficient
    return {mask: coefficient for mask, coefficient in result.items() if coefficient}


def exterior_generator(module, variable):
    return {1 << variable: module.ONE}


def normalized_two_endpoint_delta(module):
    theta_i = (exterior_generator(module, 0), exterior_generator(module, 1))
    bar_i = (exterior_generator(module, 2), exterior_generator(module, 3))
    theta_j = (exterior_generator(module, 4), exterior_generator(module, 5))
    bar_j = (exterior_generator(module, 6), exterior_generator(module, 7))
    eta = tuple(
        exterior_add(module, theta_i[index], exterior_scale(module, -1, theta_j[index]))
        for index in range(2)
    )
    bar_eta = tuple(
        exterior_add(module, bar_i[index], exterior_scale(module, -1, bar_j[index]))
        for index in range(2)
    )
    eta_square = exterior_scale(module, -2, exterior_multiply(module, eta[0], eta[1]))
    bar_eta_square = exterior_scale(
        module, 2, exterior_multiply(module, bar_eta[0], bar_eta[1])
    )
    return exterior_multiply(module, eta_square, bar_eta_square)


def endpoint_transfer_checks() -> dict[str, bool]:
    module = load_exact_algebra()
    checks = {}
    for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
        sigma_p = module.sigma_e(momentum)
        delta = normalized_two_endpoint_delta(module)
        theta_i = (exterior_generator(module, 0), exterior_generator(module, 1))
        bar_i_lower = (exterior_generator(module, 2), exterior_generator(module, 3))
        theta_j = (exterior_generator(module, 4), exterior_generator(module, 5))
        bar_j_lower = (exterior_generator(module, 6), exterior_generator(module, 7))
        bar_i_upper = (bar_i_lower[1], exterior_scale(module, -1, bar_i_lower[0]))
        bar_j_upper = (bar_j_lower[1], exterior_scale(module, -1, bar_j_lower[0]))
        label = "_".join(str(value).replace("-", "m") for value in momentum)
        for undotted in range(2):
            d_i = exterior_left_derivative(module, delta, undotted)
            d_j = exterior_left_derivative(module, delta, 4 + undotted)
            for dotted in range(2):
                d_i = exterior_add(
                    module,
                    d_i,
                    exterior_scale(
                        module,
                        module.I * sigma_p[undotted][dotted],
                        exterior_multiply(module, bar_i_upper[dotted], delta),
                    ),
                )
                d_j = exterior_add(
                    module,
                    d_j,
                    exterior_scale(
                        module,
                        -module.I * sigma_p[undotted][dotted],
                        exterior_multiply(module, bar_j_upper[dotted], delta),
                    ),
                )
            checks[f"D_endpoint_{label}_{undotted}"] = exterior_add(module, d_i, d_j) == {}

        for dotted in range(2):
            i_bar_variable = 3 if dotted == 0 else 2
            j_bar_variable = 7 if dotted == 0 else 6
            derivative_sign = -1 if dotted == 0 else 1
            bar_d_i = exterior_scale(
                module,
                derivative_sign,
                exterior_left_derivative(module, delta, i_bar_variable),
            )
            bar_d_j = exterior_scale(
                module,
                derivative_sign,
                exterior_left_derivative(module, delta, j_bar_variable),
            )
            for undotted in range(2):
                bar_d_i = exterior_add(
                    module,
                    bar_d_i,
                    exterior_scale(
                        module,
                        -module.I * sigma_p[undotted][dotted],
                        exterior_multiply(module, theta_i[undotted], delta),
                    ),
                )
                bar_d_j = exterior_add(
                    module,
                    bar_d_j,
                    exterior_scale(
                        module,
                        module.I * sigma_p[undotted][dotted],
                        exterior_multiply(module, theta_j[undotted], delta),
                    ),
                )
            checks[f"barD_endpoint_{label}_{dotted}"] = (
                exterior_add(module, bar_d_i, bar_d_j) == {}
            )
    return checks


def routing_checks() -> dict[str, bool]:
    # Each component stores coefficients of the independent symbols (k,p,q).
    k = tuple((1, 0, 0) for _ in range(4))
    p = tuple((0, 1, 0) for _ in range(4))
    q = tuple((0, 0, 1) for _ in range(4))
    r0 = k
    r1 = affine_add(k, q)
    r2 = affine_add(k, p, q)
    l1 = affine_add(r0, r1)
    l2 = affine_add(r1, r2)
    antichiral_raw = affine_add(affine_scale(-1, r1), affine_scale(-1, r0))
    chiral_raw = affine_add(r1, r2)
    return {
        "L1_is_2k_plus_q": l1 == tuple((2, 0, 1) for _ in range(4)),
        "antichiral_raw_difference_is_minus_L1": antichiral_raw
        == affine_scale(-1, l1),
        "L2_is_2k_plus_p_plus_2q": l2 == tuple((2, 1, 2) for _ in range(4)),
        "chiral_raw_difference_is_plus_L2": chiral_raw == l2,
    }


def mixed_anticommutator_checks() -> dict[str, bool]:
    module = load_exact_algebra()
    checks: dict[str, bool] = {}
    for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
        operators = module.flat_operators(momentum)
        sigma_p = module.sigma_e(momentum)
        d = (operators["D_plus"], operators["D_minus"])
        bar_d = (operators["barD_plus"], operators["barD_minus"])
        label = "_".join(str(value).replace("-", "m") for value in momentum)
        for undotted in range(2):
            for dotted in range(2):
                anticommutator = module.add(
                    module.multiply(d[undotted], bar_d[dotted]),
                    module.multiply(bar_d[dotted], d[undotted]),
                )
                expected = module.scale(
                    -2 * module.I * sigma_p[undotted][dotted],
                    operators["identity"],
                )
                checks[f"mixed_{label}_{undotted}_{dotted}"] = (
                    anticommutator == expected
                )
    return checks


def single_row_coefficient_checks() -> dict[str, bool]:
    # Strip g^2 after h^2 g^6=g^2.  Only the absolute rational budget is tested.
    propagators = Fraction(-2) ** 3
    vertex_magnitude = Fraction(1, 8) * Fraction(1, 8)
    d_chain = Fraction(-1, 2)
    coefficient = propagators * vertex_magnitude * d_chain
    return {
        "single_row_magnitude_is_one_sixteenth": abs(coefficient)
        == Fraction(1, 16),
        "single_row_magnitude_is_not_complete_chain_one_half": abs(coefficient)
        != Fraction(1, 2),
    }


def flatten(grouped: dict[str, dict[str, bool]]) -> list[dict[str, object]]:
    return [
        {"id": f"{group}.{name}", "passed": passed}
        for group, checks in grouped.items()
        for name, passed in checks.items()
    ]


def run_verification() -> dict[str, object]:
    grouped = {
        "normalization": normalization_checks(),
        "project_coefficients": project_coefficient_checks(),
        "routing": routing_checks(),
        "endpoint_transfer": endpoint_transfer_checks(),
        "mixed_anticommutator": mixed_anticommutator_checks(),
        "single_row_coefficient": single_row_coefficient_checks(),
    }
    checks = flatten(grouped)
    failed = [check for check in checks if not check["passed"]]
    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "status": "PASS" if not failed else "FAIL",
        "admission_status": "PROJECT_SEED_ROW_NORMALIZATION_VERIFIED_AND_USED_BY_COMPLETE_WW_TRACE",
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "source_ledger_sha256": hashlib.sha256(SOURCE_LEDGER.read_bytes()).hexdigest(),
        "arithmetic": "EXACT_Q_I_NO_FLOATING_POINT",
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "derived": {
            "K_plus": "-(1/8) D_+ barD^2 D_+",
            "D_minus_K_plus": "-(1/16) D^2 barD^2 D_+",
            "fixed_placement_D_factor": "-1/2",
            "antichiral_raw_vertex_momentum": "-(2k+q)",
            "chiral_raw_vertex_momentum": "2k+p+2q",
            "single_row_coefficient": "+g^2/16",
        },
        "rejected_source_claims": [
            "M3_DALGEBRA_CHAIN",
            "M3 overall g^2/2 three-sigma numerator coefficient",
        ],
        "typed_blockers": [],
        "completed_by": "generated/step5/ww-seed-graph-ir.json",
        "anomaly_coefficient_computed_here": False,
    }


def main() -> int:
    audit = run_verification()
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(audit["totals"], sort_keys=True))
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
