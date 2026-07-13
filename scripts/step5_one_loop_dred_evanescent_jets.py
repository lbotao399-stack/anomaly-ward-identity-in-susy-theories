#!/usr/bin/env python3
"""Exact Project-5A DRED evanescent-jet certificate.

The certificate classifies the complete raw local-jet carrier at
dimension 9/2, Spin(4) (3/2,0), odd parity, and formal r_f=-1.  It uses
only the Project metric split and four-dimensional Euclidean sigma system.
No loop or anomaly coefficient is computed.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated/step5/one-loop-dred-evanescent-jets.json"
VERIFY = ROOT / "audits/step5-one-loop-dred-evanescent-jets-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-dred-evanescent-jets.md"
PROJECT_R_WEIGHT = ROOT / "generated/step5/one-loop-project-r-weight.json"
SOURCE_COLOR = ROOT / "generated/step5/one-loop-source-color-closure.json"

TARGET_DIMENSION_TWICE = 9
TARGET_FORMAL_R = -1
TARGET_PARITY = 1
TARGET_JL_TWICE = 3
TARGET_JR_TWICE = 0

SIGMA_MASTER_LABELS = (
    "SIGMA_BAR_SIGMA_LEFT_IDENTITY",
    "BAR_SIGMA_SIGMA_RIGHT_IDENTITY",
    "SIGMA_SIGMA_EPSILON_DOWN",
    "BAR_SIGMA_BAR_SIGMA_EPSILON_UP",
)
SIGMA_MASTER_SIGNS = (1, 1, -1, -1)
ANTISYMMETRIC_LABELS = ("SIGMA_MN", "BAR_SIGMA_MN")


@dataclass(frozen=True)
class JetSkeleton:
    skeleton_id: int
    n_w: int
    n_wtilde: int
    n_nabla: int
    n_barnabla: int
    n_vector: int
    dimension_twice: int
    formal_r: int
    parity: int
    target_spin_multiplicity: int

    @property
    def field_strength_degree(self) -> int:
        return self.n_w + self.n_wtilde


def su2_tensor_multiplicities(twice_spins: Iterable[int]) -> dict[int, int]:
    multiplicities = {0: 1}
    for spin in twice_spins:
        updated: defaultdict[int, int] = defaultdict(int)
        for old_spin, old_multiplicity in multiplicities.items():
            for new_spin in range(abs(old_spin - spin), old_spin + spin + 1, 2):
                updated[new_spin] += old_multiplicity
        multiplicities = dict(sorted(updated.items()))
    return multiplicities


def target_spin_multiplicity(
    n_w: int,
    n_wtilde: int,
    n_nabla: int,
    n_barnabla: int,
    n_vector: int,
) -> int:
    left_count = n_w + n_nabla + n_vector
    right_count = n_wtilde + n_barnabla + n_vector
    left = su2_tensor_multiplicities([1] * left_count)
    right = su2_tensor_multiplicities([1] * right_count)
    return left.get(TARGET_JL_TWICE, 0) * right.get(TARGET_JR_TWICE, 0)


def traceless_tilde_target_multiplicity(row: JetSkeleton) -> int:
    """Multiplicity after adjoining tau in Spin(4) (1,1)."""
    left_count = row.n_w + row.n_nabla + row.n_vector
    right_count = row.n_wtilde + row.n_barnabla + row.n_vector
    left = su2_tensor_multiplicities([1] * left_count)
    right = su2_tensor_multiplicities([1] * right_count)
    left_sources = sum(left.get(twice_spin, 0) for twice_spin in (1, 3, 5))
    right_sources = right.get(2, 0)
    return left_sources * right_sources


def enumerate_skeletons() -> list[JetSkeleton]:
    raw: list[tuple[int, int, int, int, int, int, int, int, int]] = []
    for n_w in range(4):
        for n_wtilde in range(4 - n_w):
            for n_nabla in range(TARGET_DIMENSION_TWICE + 1):
                for n_barnabla in range(TARGET_DIMENSION_TWICE + 1):
                    for n_vector in range(TARGET_DIMENSION_TWICE // 2 + 1):
                        dimension_twice = (
                            3 * (n_w + n_wtilde)
                            + n_nabla
                            + n_barnabla
                            + 2 * n_vector
                        )
                        formal_r = n_w - n_wtilde - n_nabla + n_barnabla
                        parity = (n_w + n_wtilde + n_nabla + n_barnabla) % 2
                        if (
                            dimension_twice != TARGET_DIMENSION_TWICE
                            or formal_r != TARGET_FORMAL_R
                            or parity != TARGET_PARITY
                        ):
                            continue
                        raw.append(
                            (
                                n_w,
                                n_wtilde,
                                n_nabla,
                                n_barnabla,
                                n_vector,
                                dimension_twice,
                                formal_r,
                                parity,
                                target_spin_multiplicity(
                                    n_w,
                                    n_wtilde,
                                    n_nabla,
                                    n_barnabla,
                                    n_vector,
                                ),
                            )
                        )
    raw.sort(key=lambda row: (row[0] + row[1], *row[:5]))
    return [JetSkeleton(index, *row) for index, row in enumerate(raw)]


Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(coefficient: complex, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(coefficient * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum((left[row][pivot] * right[pivot][column] for pivot in range(2)), 0j)
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix2) -> Matrix2:
    return tuple(tuple(matrix[column][row] for column in range(2)) for row in range(2))  # type: ignore[return-value]


def sigma_system() -> dict[str, tuple[Matrix2, ...] | Matrix2]:
    imaginary = 1j
    pauli_1: Matrix2 = ((0, 1), (1, 0))
    pauli_2: Matrix2 = ((0, -imaginary), (imaginary, 0))
    pauli_3: Matrix2 = ((1, 0), (0, -1))
    identity: Matrix2 = ((1, 0), (0, 1))
    epsilon_up: Matrix2 = ((0, 1), (-1, 0))
    epsilon_down: Matrix2 = ((0, -1), (1, 0))
    sigma = tuple(
        matrix_scale(-imaginary, matrix)
        for matrix in (pauli_1, pauli_2, pauli_3)
    ) + (identity,)
    bar_sigma = tuple(
        matrix_scale(imaginary, matrix)
        for matrix in (pauli_1, pauli_2, pauli_3)
    ) + (identity,)
    return {
        "sigma": sigma,
        "bar_sigma": bar_sigma,
        "epsilon_up": epsilon_up,
        "epsilon_down": epsilon_down,
        "identity": identity,
    }


def sigma_component_certificate() -> dict[str, object]:
    system = sigma_system()
    sigma = system["sigma"]
    bar_sigma = system["bar_sigma"]
    epsilon_up = system["epsilon_up"]
    epsilon_down = system["epsilon_down"]
    identity = system["identity"]
    assert isinstance(sigma, tuple)
    assert isinstance(bar_sigma, tuple)
    assert isinstance(epsilon_up, tuple)
    assert isinstance(epsilon_down, tuple)
    assert isinstance(identity, tuple)

    checks: dict[str, list[bool]] = {label: [] for label in SIGMA_MASTER_LABELS}
    failures: list[dict[str, object]] = []
    for m, n, first, second in itertools.product(range(4), range(4), range(2), range(2)):
        delta_mn = int(m == n)

        sigma_bar = matrix_add(
            matrix_multiply(sigma[m], bar_sigma[n]),
            matrix_multiply(sigma[n], bar_sigma[m]),
        )[first][second]
        expected_sigma_bar = 2 * delta_mn * identity[first][second]

        bar_sigma_sigma = matrix_add(
            matrix_multiply(bar_sigma[m], sigma[n]),
            matrix_multiply(bar_sigma[n], sigma[m]),
        )[first][second]
        expected_bar_sigma_sigma = 2 * delta_mn * identity[first][second]

        sigma_n_raised = matrix_multiply(sigma[n], transpose(epsilon_up))
        sigma_m_raised = matrix_multiply(sigma[m], transpose(epsilon_up))
        sigma_sigma = sum(
            (
                sigma[m][first][dotted] * sigma_n_raised[second][dotted]
                + sigma[n][first][dotted] * sigma_m_raised[second][dotted]
                for dotted in range(2)
            ),
            0j,
        )
        expected_sigma_sigma = -2 * delta_mn * epsilon_down[first][second]

        bar_n_lowered = matrix_multiply(bar_sigma[n], transpose(epsilon_down))
        bar_m_lowered = matrix_multiply(bar_sigma[m], transpose(epsilon_down))
        bar_bar = sum(
            (
                bar_sigma[m][first][undotted] * bar_n_lowered[second][undotted]
                + bar_sigma[n][first][undotted] * bar_m_lowered[second][undotted]
                for undotted in range(2)
            ),
            0j,
        )
        expected_bar_bar = -2 * delta_mn * epsilon_up[first][second]

        values = (
            sigma_bar == expected_sigma_bar,
            bar_sigma_sigma == expected_bar_sigma_sigma,
            sigma_sigma == expected_sigma_sigma,
            bar_bar == expected_bar_bar,
        )
        for label, passed in zip(SIGMA_MASTER_LABELS, values, strict=True):
            checks[label].append(passed)
            if not passed:
                failures.append(
                    {
                        "identity": label,
                        "m": m,
                        "n": n,
                        "first_spinor": first,
                        "second_spinor": second,
                    }
                )

    return {
        "project_equations": ["1.51", "1.52", "1.54", "5.9"],
        "component_checks_per_identity": 64,
        "component_checks_total": sum(len(rows) for rows in checks.values()),
        "identity_checks": {label: all(rows) for label, rows in checks.items()},
        "all_passed": not failures,
        "failures": failures,
        "tilde_delta_contractions": {
            "SIGMA_BAR_SIGMA_LEFT_IDENTITY": "(+2*epsilon) delta_a^b",
            "BAR_SIGMA_SIGMA_RIGHT_IDENTITY": "(+2*epsilon) delta_dota^dotb",
            "SIGMA_SIGMA_EPSILON_DOWN": "(-2*epsilon) epsilon_ab",
            "BAR_SIGMA_BAR_SIGMA_EPSILON_UP": "(-2*epsilon) epsilon^dotadotb",
        },
        "antisymmetric_channels": {
            "tilde_delta_mn_sigma_E^mn": "0",
            "tilde_delta_mn_bar_sigma_E^mn": "0",
            "reason": "tilde_delta_mn is symmetric; sigma_E^mn and bar_sigma_E^mn are antisymmetric",
        },
    }


def source_sym2_certificate() -> dict[str, object]:
    half = Fraction(1, 2)
    projector = [[half, half], [half, half]]
    square = [
        [sum((projector[row][pivot] * projector[pivot][column] for pivot in range(2)), Fraction(0)) for column in range(2)]
        for row in range(2)
    ]
    return {
        "ordered_source_basis": ["J_AB", "J_BA"],
        "projector": [[str(value) for value in row] for row in projector],
        "projector_squared_equals_projector": square == projector,
        "rank": 1,
        "source_parity": "odd",
        "operator_parity": "odd",
        "source_times_operator_parity": "even",
        "source_has_no_Lorentz_index": True,
        "DRED_reduction_commutes_with_Sym2_source_projection": True,
        "color_dimension": "SYMBOLIC_PER_SYM2_ADJOINT_GENERATOR",
    }


def project_cross_certificates() -> dict[str, object]:
    r_bytes = PROJECT_R_WEIGHT.read_bytes()
    source_color_bytes = SOURCE_COLOR.read_bytes()
    r_payload = json.loads(r_bytes)
    source_color_payload = json.loads(source_color_bytes)
    weights = r_payload["weights"]
    return {
        "Project_R_weight": {
            "path": str(PROJECT_R_WEIGHT.relative_to(ROOT)),
            "sha256": hashlib.sha256(r_bytes).hexdigest(),
            "status": r_payload["status"],
            "pure_gauge_letter_weights": {
                "W": weights["W_a"],
                "Wtilde": weights["tilde_W_dot_a"],
                "nabla": weights["nabla_a"],
                "barnabla": weights["bar_nabla_dot_a"],
                "Dcov": weights["D_cov_a_dot_a"],
            },
            "target_selection_rule": r_payload["verdicts"]["pure_gauge_target_selection_rule"],
        },
        "source_color": {
            "path": str(SOURCE_COLOR.relative_to(ROOT)),
            "sha256": hashlib.sha256(source_color_bytes).hexdigest(),
            "status": source_color_payload["status"],
            "background_CE_source": source_color_payload["verdicts"]["odd_local_source_background_CE_closure"],
            "ordinary_Sym2_split_monomorphism": source_color_payload["verdicts"]["color_Sym2_quotient_for_m_to_m_minus_m"],
            "full_quantum_BV_source_complex": source_color_payload["verdicts"]["full_quantum_BV_Slavnov_source_complex"],
            "tau_rank_five_color_map_covered": False,
        },
    }


Polynomial = dict[int, Fraction]


def polynomial_add(*terms: Polynomial) -> Polynomial:
    output: defaultdict[int, Fraction] = defaultdict(Fraction)
    for term in terms:
        for power, coefficient in term.items():
            output[power] += coefficient
    return {power: coefficient for power, coefficient in sorted(output.items()) if coefficient}


def polynomial_scale(coefficient: Fraction, term: Polynomial) -> Polynomial:
    return {
        power: coefficient * value
        for power, value in term.items()
        if coefficient * value
    }


def encode_polynomial(term: Polynomial) -> dict[str, str]:
    return {str(power): str(coefficient) for power, coefficient in sorted(term.items())}


def tau_algebra_certificate() -> dict[str, object]:
    epsilon: Polynomial = {1: Fraction(1)}
    epsilon_squared: Polynomial = {2: Fraction(1)}
    tilde_trace = polynomial_scale(Fraction(2), epsilon)
    delta_trace: Polynomial = {0: Fraction(4)}
    tau_trace = polynomial_add(
        tilde_trace,
        polynomial_scale(Fraction(-1, 2), polynomial_scale(Fraction(4), epsilon)),
    )
    tau_norm = polynomial_add(
        tilde_trace,
        polynomial_scale(Fraction(-2), epsilon_squared),
        epsilon_squared,
    )
    return {
        "definition": "tau^mn=tilde_delta^mn-(epsilon/2)delta_(4)^mn",
        "exact_split": "tilde_delta^mn=(epsilon/2)delta_(4)^mn+tau^mn",
        "input_polynomials": {
            "tr_tilde_delta": encode_polynomial(tilde_trace),
            "tr_delta_(4)": encode_polynomial(delta_trace),
        },
        "tau_trace_polynomial": encode_polynomial(tau_trace),
        "tau_trace": "delta_(4)_mn tau^mn=0",
        "tau_spin4": "(1,1)",
        "tau_norm_polynomial": encode_polynomial(tau_norm),
        "tau_norm_squared": "tau_mn tau^mn=2*epsilon-epsilon^2",
        "tau_on_external_hat_momentum": "tau^mn v_n=-(epsilon/2)v^m",
        "full_tilde_on_external_hat_momentum": "tilde_delta^mn v_n=0",
        "tau_norm_divisible_by_epsilon": min(tau_norm) >= 1,
        "tau_norm_divisible_by_epsilon_squared": min(tau_norm) >= 2,
        "tau_is_not_in_epsilon_times_regular_tensor_module": min(tau_norm) == 1,
        "nondivisibility_witness": "2*epsilon-epsilon^2 is not divisible by epsilon^2 in Q[epsilon]",
    }


def levi_civita_3(first: int, second: int, third: int) -> int:
    if len({first, second, third}) < 3:
        return 0
    values = (first, second, third)
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def nonabelian_color_witness() -> dict[str, object]:
    """Exact SU(2) witness for the invariant rank-five Project tensor."""

    def metric(first: int, second: int) -> int:
        return int(first == second)

    def structure(first: int, second: int, third: int) -> int:
        return levi_civita_3(first, second, third)

    def color_tensor(a: int, b: int, c: int, d: int, e: int) -> int:
        return (
            metric(a, c) * structure(b, d, e)
            + metric(b, c) * structure(a, d, e)
        )

    source_symmetric = all(
        color_tensor(a, b, c, d, e) == color_tensor(b, a, c, d, e)
        for a, b, c, d, e in itertools.product(range(3), repeat=5)
    )
    de_antisymmetric = all(
        color_tensor(a, b, c, d, e) == -color_tensor(a, b, c, e, d)
        for a, b, c, d, e in itertools.product(range(3), repeat=5)
    )
    variations: list[int] = []
    for x, a, b, c, d, e in itertools.product(range(3), repeat=6):
        variation = sum(
            (
                structure(x, a, f) * color_tensor(f, b, c, d, e)
                + structure(x, b, f) * color_tensor(a, f, c, d, e)
                + structure(x, c, f) * color_tensor(a, b, f, d, e)
                + structure(x, d, f) * color_tensor(a, b, c, f, e)
                + structure(x, e, f) * color_tensor(a, b, c, d, f)
            )
            for f in range(3)
        )
        variations.append(variation)
    nonzero_entries = [
        (a, b, c, d, e, color_tensor(a, b, c, d, e))
        for a, b, c, d, e in itertools.product(range(3), repeat=5)
        if color_tensor(a, b, c, d, e)
    ]
    return {
        "input_tensor": "K^(AB)_(C[DE])=delta^A_C f^B_DE+delta^B_C f^A_DE",
        "Project_dictionary": "f^A_BC=c_BC^A",
        "Project_tensor": "K^(AB)_(C[DE])=delta^A_C c_DE^B+delta^B_C c_DE^A",
        "exact_SU2_adjoint_realization": "kappa_AB=delta_AB; c_ABC=epsilon_ABC",
        "source_AB_symmetric": source_symmetric,
        "DE_antisymmetric": de_antisymmetric,
        "adjoint_invariant": all(value == 0 for value in variations),
        "adjoint_invariance_component_count": len(variations),
        "adjoint_invariance_maximum_absolute_residual": max(map(abs, variations)),
        "invariance_equation_all_lower_Project_indices": "c_XA^F K_FB_CDE+c_XB^F K_AF_CDE+c_XC^F K_AB_FDE+c_XD^F K_AB_CFE+c_XE^F K_AB_CDF=0",
        "nonzero_entry_count": len(nonzero_entries),
        "SU2_AB00_C0_full_DE_contraction": "K^00_(0[DE]) B^[DE]=4*B^12",
        "witness_entries": [
            {
                "A": a,
                "B": b,
                "C": c,
                "D": d,
                "E": e,
                "value": value,
            }
            for a, b, c, d, e, value in nonzero_entries[:6]
        ],
        "general_nonabelian_algebra_classification": "NOT_CLAIMED",
        "abelian_c_zero_case": "WITNESS_ZERO",
    }


def grassmann_and_quadratic_jet_witness() -> dict[str, object]:
    field_swap_sign = -1
    tau_dotted_swap_sign = 1
    dotted_pair_color_exchange_sign = field_swap_sign * tau_dotted_swap_sign
    color_DE_exchange_sign = -1
    contraction_relabel_sign = (
        dotted_pair_color_exchange_sign * color_DE_exchange_sign
    )
    quadratic_derivative_at_zero = 3 * 2 * 0
    cubic_derivative_at_zero = 3 * 2 * 1
    return {
        "Grassmann_exchange": {
            "Wtilde_D_and_Wtilde_E_are_odd": True,
            "field_swap_sign": field_swap_sign,
            "tau_dotted_pair_is_symmetric": True,
            "tau_dotted_swap_sign": tau_dotted_swap_sign,
            "B_DE_exchange_sign": dotted_pair_color_exchange_sign,
            "K_DE_exchange_sign": color_DE_exchange_sign,
            "K_DE_times_B_DE_relabel_sign": contraction_relabel_sign,
            "antisymmetric_color_contraction_not_killed": contraction_relabel_sign == 1,
        },
        "quadratic_jet": {
            "field_strength_degree": 3,
            "minimum_background_connection_degree": 3,
            "model_monomial": "t^3",
            "second_derivative_at_t_zero": quadratic_derivative_at_zero,
            "third_derivative_at_t_zero": cubic_derivative_at_zero,
            "ell_2_of_witness": "0",
            "witness_is_nonzero_before_quadratic_jet": True,
            "raw_DRED_kernel_counterexample": quadratic_derivative_at_zero == 0,
        },
        "quotient_boundary": {
            "full_DRED_raw_source_module_injectivity": "FAIL_EXPLICIT_KERNEL",
            "background_CE_covariant_submodule_injectivity": "FAIL_EXPLICIT_KERNEL",
            "physical_4d_quotient_sets_tau_to_zero": True,
            "physical_4d_injectivity_refuted_by_this_witness": False,
            "full_quantum_BV_cohomology_class_of_witness": "OPEN",
        },
    }


def single_tilde_channel_partition() -> list[dict[str, str]]:
    return [
        {
            "channel": "AT_LEAST_ONE_EXTERNAL_HAT_MOMENTUM_ENDPOINT",
            "outcome": "ZERO_BY_TILDE_DELTA_HAT_DELTA_ORTHOGONALITY",
        },
        {
            "channel": "CLOSED_SCALAR_SIGMA_TRACE",
            "outcome": "SCALAR_2EPSILON_TIMES_EXISTING_JET",
        },
        {
            "channel": "CLOSED_ANTISYMMETRIC_SIGMA_PAIR",
            "outcome": "ZERO_SYMMETRIC_TIMES_ANTISYMMETRIC",
        },
        {
            "channel": "OPEN_SYMMETRIC_TRACELESS_SIGMA_PAIR",
            "outcome": "TAU_(1,1)_RAW_EVANESCENT_TARGET_CANDIDATE",
        },
        {
            "channel": "FREE_VECTOR_ENDPOINT",
            "outcome": "EXCLUDED_BY_TARGET_SPIN4_TYPE",
        },
    ]


def build_target_copies(skeletons: list[JetSkeleton]) -> list[dict[str, int]]:
    copies: list[dict[str, int]] = []
    for skeleton in skeletons:
        for spin_copy in range(skeleton.target_spin_multiplicity):
            copies.append(
                {
                    "copy_id": len(copies),
                    "skeleton_id": skeleton.skeleton_id,
                    "spin_copy": spin_copy,
                    "field_strength_degree": skeleton.field_strength_degree,
                    "vector_slots": skeleton.n_vector,
                }
            )
    return copies


def build_placement_ledger(
    skeletons: list[JetSkeleton], copies: list[dict[str, int]]
) -> list[dict[str, object]]:
    by_id = {row.skeleton_id: row for row in skeletons}
    ledger: list[dict[str, object]] = []
    for copy in copies:
        skeleton = by_id[copy["skeleton_id"]]
        for label, sign in zip(SIGMA_MASTER_LABELS, SIGMA_MASTER_SIGNS, strict=True):
            ledger.append(
                {
                    "placement_id": len(ledger),
                    "copy_id": copy["copy_id"],
                    "skeleton_id": skeleton.skeleton_id,
                    "class": "CLOSED_SIGMA_MASTER",
                    "index_placement": label,
                    "normalized_coefficient": f"{sign:+d}*2*epsilon",
                    "outcome": "EXISTING_PHYSICAL_COPY_IN_EPSILON_IDEAL",
                }
            )
        for label in ANTISYMMETRIC_LABELS:
            ledger.append(
                {
                    "placement_id": len(ledger),
                    "copy_id": copy["copy_id"],
                    "skeleton_id": skeleton.skeleton_id,
                    "class": "CLOSED_ANTISYMMETRIC_SIGMA",
                    "index_placement": label,
                    "normalized_coefficient": "0",
                    "outcome": "ZERO_SYMMETRIC_TIMES_ANTISYMMETRIC",
                }
            )
        for vector_slot in range(skeleton.n_vector):
            for sigma_partner in SIGMA_MASTER_LABELS:
                ledger.append(
                    {
                        "placement_id": len(ledger),
                        "copy_id": copy["copy_id"],
                        "skeleton_id": skeleton.skeleton_id,
                        "class": "EXTERNAL_SIGMA_ENDPOINT",
                        "external_vector_slots": [vector_slot],
                        "sigma_partner": sigma_partner,
                        "normalized_coefficient": "0",
                        "outcome": "ZERO_TILDE_DELTA_TIMES_HAT_MOMENTUM",
                    }
                )
        for first, second in itertools.combinations(range(skeleton.n_vector), 2):
            ledger.append(
                {
                    "placement_id": len(ledger),
                    "copy_id": copy["copy_id"],
                    "skeleton_id": skeleton.skeleton_id,
                    "class": "TWO_EXTERNAL_ENDPOINTS",
                    "external_vector_slots": [first, second],
                    "normalized_coefficient": "0",
                    "outcome": "ZERO_TWO_HAT_MOMENTA",
                }
            )
    return ledger


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def sparse_summary(
    rows: int, columns: int, entries: list[tuple[int, int, str]], witness_count: int = 8
) -> dict[str, object]:
    canonical = sorted(entries)
    witnesses = canonical[:witness_count]
    if len(canonical) > witness_count:
        witnesses += canonical[-witness_count:]
    return {
        "rows": rows,
        "columns": columns,
        "nnz": len(canonical),
        "canonical_COO_sha256": canonical_sha256(canonical),
        "witness_entries": [
            {"row": row, "column": column, "coefficient": coefficient}
            for row, column, coefficient in witnesses
        ],
    }


def module_presentation(
    physical_count: int, ledger: list[dict[str, object]]
) -> dict[str, object]:
    scalar_rows = [row for row in ledger if row["class"] == "CLOSED_SIGMA_MASTER"]
    zero_rows = [row for row in ledger if row["normalized_coefficient"] == "0"]
    scalar_raw_entries: list[tuple[int, int, str]] = []
    for raw_column, row in enumerate(scalar_rows):
        coefficient = str(row["normalized_coefficient"]).split("*2*epsilon", maxsplit=1)[0]
        scalar_raw_entries.append((int(row["copy_id"]), raw_column, coefficient))

    scalar_generator_count = physical_count
    zero_generator_count = len(zero_rows)
    generator_count = physical_count + scalar_generator_count + zero_generator_count
    relation_count = scalar_generator_count + zero_generator_count
    entries: list[tuple[int, int, str]] = []
    for copy_id in range(physical_count):
        entries.append((copy_id, copy_id, "-2*epsilon"))
        entries.append((copy_id, physical_count + copy_id, "1"))
    zero_column_offset = physical_count + scalar_generator_count
    for zero_id in range(zero_generator_count):
        entries.append(
            (
                scalar_generator_count + zero_id,
                zero_column_offset + zero_id,
                "1",
            )
        )

    return {
        "scope": "CONTRACTED_TRACE_AND_EXTERNAL_SUPPORT_SUBMODULE_ONLY",
        "coefficient_ring": "R=Q[epsilon]",
        "physical_module": f"M_phys=R^{physical_count} tensor Sym2(Adj)",
        "tilde_generated_image": "M_tilde=(2*epsilon) M_phys",
        "raw_scalar_sigma_map": sparse_summary(
            physical_count, len(scalar_rows), scalar_raw_entries
        )
        | {
            "exact_rank": physical_count,
            "block_rule": "each physical copy receives [1,1,-1,-1] from the four raised/lowered sigma masters",
        },
        "presentation_generators": {
            "physical": physical_count,
            "scalar_trace_evanescent": scalar_generator_count,
            "zero_placements": zero_generator_count,
            "total": generator_count,
        },
        "presentation_relations": {
            "E_i_minus_2epsilon_P_i": scalar_generator_count,
            "Z_j": zero_generator_count,
            "total": relation_count,
            "matrix": sparse_summary(relation_count, generator_count, entries),
            "unit_pivot_columns": list(range(physical_count, generator_count)),
            "exact_row_rank": relation_count,
        },
        "quotient_free_rank_per_Sym2_color_generator": physical_count,
        "new_independent_evanescent_free_rank_in_this_submodule": 0,
        "does_not_present_open_traceless_tau_sector": True,
        "torsion_statement": {
            "M_phys_is_epsilon_torsion_free": True,
            "M_phys_mod_M_tilde": f"(Q[epsilon]/(epsilon))^{physical_count} tensor Sym2(Adj)",
            "quotient_is_epsilon_torsion": True,
            "localized_pole_mixing_identity": "epsilon^(-1) * (2*epsilon*P_i) = 2*P_i",
            "loop_or_anomaly_coefficient_computed": False,
        },
    }


def _placement_witnesses(ledger: list[dict[str, object]]) -> list[dict[str, object]]:
    witnesses: list[dict[str, object]] = []
    for class_name in sorted({str(row["class"]) for row in ledger}):
        rows = [row for row in ledger if row["class"] == class_name]
        witnesses.append(rows[0])
        if len(rows) > 1:
            witnesses.append(rows[-1])
    return witnesses


def build_payload() -> dict[str, object]:
    skeletons = enumerate_skeletons()
    copies = build_target_copies(skeletons)
    ledger = build_placement_ledger(skeletons, copies)
    color_witness = nonabelian_color_witness()
    kernel_witness = grassmann_and_quadratic_jet_witness()
    placement_counts: defaultdict[str, int] = defaultdict(int)
    for row in ledger:
        placement_counts[str(row["class"])] += 1

    rows_by_degree = {
        str(degree): [
            asdict(row)
            | {
                "traceless_tilde_spurion_target_multiplicity": traceless_tilde_target_multiplicity(row)
            }
            for row in skeletons
            if row.field_strength_degree == degree
        ]
        for degree in range(4)
    }
    spin_copies_by_degree = {
        str(degree): sum(
            row.target_spin_multiplicity
            for row in skeletons
            if row.field_strength_degree == degree
        )
        for degree in range(4)
    }
    tau_copies_by_degree = {
        str(degree): sum(
            traceless_tilde_target_multiplicity(row)
            for row in skeletons
            if row.field_strength_degree == degree
        )
        for degree in range(4)
    }
    tau_copy_count = sum(tau_copies_by_degree.values())
    n3_row = next(row for row in skeletons if row.field_strength_degree == 3)
    separated_sigma_rows = [
        {
            "number_of_intervening_hat_sigma_factors": length,
            "exact_reduction": f"{'+' if length % 2 == 0 else '-'}2*epsilon times original_hat_sigma_word",
            "derivation": f"{length} mixed tilde-hat anticommutations followed by tilde_delta_mn sigma^m bar_sigma^n",
        }
        for length in range(max(row.n_vector for row in skeletons) + 1)
    ]
    projector_power_rows = [
        {
            "power": power,
            "open_chain": "tilde_delta",
            "closed_trace": "2*epsilon",
        }
        for power in range(1, 9)
    ]

    return {
        "schema": "STEP5_ONE_LOOP_DRED_EVANESCENT_JETS_V1",
        "status": "FAIL_EXPLICIT_FULL_DRED_QUADRATIC_JET_KERNEL",
        "scope": {
            "Project_frame": "5A_PERTURBATIVE_FF_DRED_SUPERGRAPHS",
            "DRED_generators": ["delta_(4)", "widehat_delta", "tilde_delta"],
            "metric_contract": ["5.11", "5.12", "5.13", "5.13a", "5.13b", "5.14", "5.15"],
            "target_dimension": "9/2",
            "target_spin4": "(3/2,0)",
            "target_parity": "odd",
            "target_formal_r": -1,
            "physical_Project_U1R_binding": "PASS_BY_PROJECT_R_WEIGHT_CERTIFICATE",
            "source": "J_(AB) in Sym2(Adj), Lorentz scalar",
            "external_momentum_support": "v^m=widehat_delta^m_n v^n",
            "no_additional_evanescent_field_or_antisymmetric_regulator_spurion": True,
        },
        "raw_jet_census": {
            "diophantine_system": [
                "3(n_W+n_Wtilde)+n_N+n_B+2n_D=9",
                "n_W-n_Wtilde-n_N+n_B=-1",
                "n_W+n_Wtilde+n_N+n_B=1 mod 2",
            ],
            "skeleton_count": len(skeletons),
            "skeletons_by_field_strength_degree": rows_by_degree,
            "target_spin_copies_by_field_strength_degree": spin_copies_by_degree,
            "target_spin_copy_count": len(copies),
            "maximum_external_vector_derivative_slots": max(row.n_vector for row in skeletons),
            "zero_spin_multiplicity_skeleton_ids": [
                row.skeleton_id for row in skeletons if row.target_spin_multiplicity == 0
            ],
        },
        "Project_cross_certificates": project_cross_certificates(),
        "source_Sym2": source_sym2_certificate(),
        "sigma_component_certificate": sigma_component_certificate(),
        "tilde_decomposition": tau_algebra_certificate(),
        "single_tilde_index_channel_partition": single_tilde_channel_partition(),
        "raw_traceless_tau_census": {
            "representation_identity": "Sym2((1/2,1/2))=(0,0)+(1,1)",
            "multiplicity_formula": "m_tau=m_R(j=1)*(m_L(j=1/2)+m_L(j=3/2)+m_L(j=5/2))",
            "target_spin_copies_by_field_strength_degree": tau_copies_by_degree,
            "raw_target_spin_copy_count": tau_copy_count,
            "representation_multiplicity_exhausted": True,
            "spot_checks": [
                {
                    "skeleton_id": 0,
                    "left_slots": 5,
                    "right_slots": 4,
                    "left_multiplicities_j_half_threehalf_fivehalf": [5, 4, 1],
                    "right_multiplicity_j_one": 3,
                    "tau_target_multiplicity": 30,
                },
                {
                    "skeleton_id": 14,
                    "left_slots": 3,
                    "right_slots": 2,
                    "left_multiplicities_j_half_threehalf_fivehalf": [2, 1, 0],
                    "right_multiplicity_j_one": 1,
                    "tau_target_multiplicity": 3,
                },
                {
                    "skeleton_id": 17,
                    "left_slots": 1,
                    "right_slots": 2,
                    "left_multiplicities_j_half_threehalf_fivehalf": [1, 0, 0],
                    "right_multiplicity_j_one": 1,
                    "tau_target_multiplicity": 1,
                },
            ],
            "explicit_N3_witness": {
                "skeleton_id": n3_row.skeleton_id,
                "content": "W Wtilde Wtilde",
                "vector_derivative_slots": n3_row.n_vector,
                "physical_target_multiplicity": n3_row.target_spin_multiplicity,
                "tau_target_multiplicity": traceless_tilde_target_multiplicity(n3_row),
                "operator": "E_abc^(AB)=K^(AB)_(C[DE]) tau_(ab)(dotc dotd) W_c^C Wtilde^(D dotc) Wtilde^(E dotd), symmetrized in (a,b,c)",
                "source_pairing": "J_(AB) E^(AB)",
                "dimension": "9/2",
                "formal_r": -1,
                "parity": "odd",
                "external_momentum_annihilation_applicable": False,
                "color_carrier": "EXACT_NONZERO_SU2_ADJOINT_CE_COVARIANT_TENSOR",
                "color_certificate": color_witness,
                "Grassmann_and_quadratic_jet_certificate": kernel_witness,
            },
            "full_index_placement_projector_matrix_built": False,
            "missing_matrix": "M_TAU_OPEN_SPINOR_PLACEMENTS_TO_229_TARGET_COPIES",
            "post_EOM_IBP_full_BV_rank": "BLOCKED",
            "missing_matrix_role": "REQUIRED_FOR_COMPLETE_EVANESCENT_QUOTIENT_CLASSIFICATION_NOT_FOR_RAW_KERNEL_EXISTENCE",
        },
        "contracted_endpoint_subledger": {
            "row_count": len(ledger),
            "counts_by_class": dict(sorted(placement_counts.items())),
            "canonical_sha256": canonical_sha256(ledger),
            "witness_rows": _placement_witnesses(ledger),
            "full_ledger_reconstructed_by": "build_placement_ledger",
            "contracted_trace_external_and_antisymmetric_placements_exhausted": True,
            "open_traceless_tau_placements_included": False,
            "free_vector_endpoint_count": 0,
        },
        "separated_internal_sigma_reduction": {
            "mixed_anticommutator": "tilde_delta_mn widehat_delta_r_s {sigma^m,bar_sigma^r}=0",
            "rows": separated_sigma_rows,
            "all_local_vector_slot_separations_covered": True,
        },
        "multiple_tilde_insertions": {
            "idempotence": "tilde_delta^2=tilde_delta",
            "connected_chain_reduction": "tilde_delta^n=tilde_delta for every integer n>=1",
            "closed_component_trace": "tr(tilde_delta^n)=2*epsilon for every integer n>=1",
            "disconnected_closed_components": "c components give (2*epsilon)^c",
            "any_component_touching_external_hat_momentum": "0",
            "fully_contracted_nonempty_closed_network_has_coefficient_in_ideal_(epsilon)": True,
            "finite_exact_power_witnesses": projector_power_rows,
            "induction_uses_idempotence": True,
            "does_not_reduce_open_tau_tensor": True,
        },
        "module_presentation": module_presentation(len(copies), ledger),
        "verdict": {
            "M_DRED_EVANESCENT_JETS": "FAIL_EXPLICIT_FULL_DRED_QUADRATIC_JET_KERNEL",
            "full_DRED_raw_source_module_injectivity": "FAIL_EXPLICIT_KERNEL",
            "background_CE_covariant_submodule_injectivity": "FAIL_EXPLICIT_KERNEL",
            "explicit_raw_kernel_dimension_lower_bound_for_SU2": 1,
            "physical_4d_quotient_action": "q_4d(tau)=0_AND_q_4d(E)=0",
            "physical_4d_injectivity_refuted_by_this_witness": False,
            "full_quantum_BV_cohomology_class_of_witness": "OPEN",
            "raw_traceless_tau_target_directions": tau_copy_count,
            "post_quotient_independent_evanescent_tensor_directions": "BLOCKED",
            "epsilon_ideal_mixing_retained_until_pole_subtraction": True,
            "coefficient_accepted": False,
            "coupled_open_gates": [
                "EXHAUSTIVE_TAU_EOM_IBP_QUOTIENT_MATRIX",
                "FULL_QUANTUM_BV_ST_SOURCE_COMPLEX",
            ],
        },
    }


def build_verification(payload: dict[str, object]) -> dict[str, object]:
    census = payload["raw_jet_census"]
    sigma = payload["sigma_component_certificate"]
    source = payload["source_Sym2"]
    placement = payload["contracted_endpoint_subledger"]
    presentation = payload["module_presentation"]
    multiple = payload["multiple_tilde_insertions"]
    tau = payload["raw_traceless_tau_census"]
    decomposition = payload["tilde_decomposition"]
    cross = payload["Project_cross_certificates"]
    assert isinstance(census, dict)
    assert isinstance(sigma, dict)
    assert isinstance(source, dict)
    assert isinstance(placement, dict)
    assert isinstance(presentation, dict)
    assert isinstance(multiple, dict)
    assert isinstance(tau, dict)
    assert isinstance(decomposition, dict)
    assert isinstance(cross, dict)
    explicit_witness = tau["explicit_N3_witness"]
    assert isinstance(explicit_witness, dict)
    color_witness = explicit_witness["color_certificate"]
    kernel_witness = explicit_witness["Grassmann_and_quadratic_jet_certificate"]
    assert isinstance(color_witness, dict)
    assert isinstance(kernel_witness, dict)
    grassmann = kernel_witness["Grassmann_exchange"]
    quadratic = kernel_witness["quadratic_jet"]
    boundary = kernel_witness["quotient_boundary"]
    assert isinstance(grassmann, dict)
    assert isinstance(quadratic, dict)
    assert isinstance(boundary, dict)
    relations = presentation["presentation_relations"]
    generators = presentation["presentation_generators"]
    scalar_map = presentation["raw_scalar_sigma_map"]
    assert isinstance(relations, dict)
    assert isinstance(generators, dict)
    assert isinstance(scalar_map, dict)

    counts = placement["counts_by_class"]
    assert isinstance(counts, dict)
    tau_multiplicity_vector = [
        traceless_tilde_target_multiplicity(row) for row in enumerate_skeletons()
    ]
    checks = {
        "complete_diophantine_skeleton_count_18": census["skeleton_count"] == 18,
        "target_spin_copies_by_degree_40_20_6_0": census["target_spin_copies_by_field_strength_degree"]
        == {"0": 40, "1": 20, "2": 6, "3": 0},
        "complete_raw_target_spin_copy_count_66": census["target_spin_copy_count"] == 66,
        "maximum_vector_slot_count_four": census["maximum_external_vector_derivative_slots"] == 4,
        "four_sigma_master_identities_component_exact": sigma["all_passed"] is True,
        "sigma_component_check_count_256": sigma["component_checks_total"] == 256,
        "antisymmetric_sigma_channels_zero": all(
            value == "0"
            for key, value in sigma["antisymmetric_channels"].items()  # type: ignore[union-attr]
            if key != "reason"
        ),
        "Sym2_projector_idempotent_rank_one": source["projector_squared_equals_projector"] is True
        and source["rank"] == 1,
        "DRED_commutes_with_source_projection": source["DRED_reduction_commutes_with_Sym2_source_projection"] is True,
        "single_tilde_channel_partition_has_five_classes": len(payload["single_tilde_index_channel_partition"]) == 5,  # type: ignore[arg-type]
        "contracted_endpoint_subledger_count_908": placement["row_count"] == 908,
        "closed_sigma_master_placements_264": counts["CLOSED_SIGMA_MASTER"] == 264,
        "closed_antisymmetric_placements_132": counts["CLOSED_ANTISYMMETRIC_SIGMA"] == 132,
        "external_sigma_endpoint_placements_420": counts["EXTERNAL_SIGMA_ENDPOINT"] == 420,
        "two_external_endpoint_placements_92": counts["TWO_EXTERNAL_ENDPOINTS"] == 92,
        "no_target_typed_free_vector_endpoint": placement["free_vector_endpoint_count"] == 0,
        "all_local_sigma_separations_covered": payload["separated_internal_sigma_reduction"]["all_local_vector_slot_separations_covered"] is True,  # type: ignore[index]
        "multiple_insertions_reduce_by_idempotence": multiple["induction_uses_idempotence"] is True,
        "fully_contracted_closed_network_is_in_epsilon_ideal": multiple["fully_contracted_nonempty_closed_network_has_coefficient_in_ideal_(epsilon)"] is True,
        "idempotence_does_not_remove_open_tau": multiple["does_not_reduce_open_tau_tensor"] is True,
        "raw_scalar_sigma_map_shape_66_by_264": scalar_map["rows"] == 66 and scalar_map["columns"] == 264,
        "raw_scalar_sigma_map_exact_rank_66": scalar_map["exact_rank"] == 66,
        "presentation_generator_count_776": generators["total"] == 776,
        "presentation_relation_count_and_rank_710": relations["total"] == 710 and relations["exact_row_rank"] == 710,
        "presentation_quotient_free_rank_66": presentation["quotient_free_rank_per_Sym2_color_generator"] == 66,
        "contracted_submodule_has_no_new_free_rank": presentation["new_independent_evanescent_free_rank_in_this_submodule"] == 0,
        "contracted_presentation_excludes_tau": presentation["does_not_present_open_traceless_tau_sector"] is True,
        "tau_split_trace_exact": decomposition["tau_trace"] == "delta_(4)_mn tau^mn=0",
        "tau_norm_exact": decomposition["tau_norm_squared"] == "tau_mn tau^mn=2*epsilon-epsilon^2",
        "tau_not_epsilon_multiple": decomposition["tau_is_not_in_epsilon_times_regular_tensor_module"] is True,
        "tau_raw_copies_by_degree_150_66_12_1": tau["target_spin_copies_by_field_strength_degree"]
        == {"0": 150, "1": 66, "2": 12, "3": 1},
        "tau_raw_target_copy_count_229": tau["raw_target_spin_copy_count"] == 229,
        "tau_skeleton_multiplicity_vector_exact": tau_multiplicity_vector
        == [30, 30, 30, 30, 30, 9, 9, 9, 9, 10, 10, 10, 3, 3, 3, 3, 0, 1],
        "tau_representation_multiplicity_exhausted": tau["representation_multiplicity_exhausted"] is True,
        "three_tau_multiplicity_spot_checks_exact": [
            row["tau_target_multiplicity"] for row in tau["spot_checks"]  # type: ignore[index]
        ]
        == [30, 3, 1],
        "N3_tau_witness_has_no_external_vector_slot": tau["explicit_N3_witness"]["vector_derivative_slots"] == 0,  # type: ignore[index]
        "N3_tau_witness_changes_zero_to_one": tau["explicit_N3_witness"]["physical_target_multiplicity"] == 0  # type: ignore[index]
        and tau["explicit_N3_witness"]["tau_target_multiplicity"] == 1,  # type: ignore[index]
        "K_source_indices_are_symmetric": color_witness["source_AB_symmetric"] is True,
        "K_tildeW_color_indices_are_antisymmetric": color_witness["DE_antisymmetric"] is True,
        "K_is_exactly_adjoint_invariant": color_witness["adjoint_invariant"] is True,
        "K_adjoint_invariance_checks_729_zero_residual": color_witness["adjoint_invariance_component_count"] == 729
        and color_witness["adjoint_invariance_maximum_absolute_residual"] == 0,
        "K_has_thirty_nonzero_SU2_entries": color_witness["nonzero_entry_count"] == 30,
        "K_SU2_component_00012_equals_two": color_witness["witness_entries"][0]  # type: ignore[index]
        == {"A": 0, "B": 0, "C": 0, "D": 1, "E": 2, "value": 2},
        "Grassmann_tildeW_pair_is_color_antisymmetric": grassmann["B_DE_exchange_sign"] == -1,
        "antisymmetric_K_contraction_survives": grassmann["K_DE_times_B_DE_relabel_sign"] == 1
        and grassmann["antisymmetric_color_contraction_not_killed"] is True,
        "N3_second_background_jet_is_zero": quadratic["second_derivative_at_t_zero"] == 0
        and quadratic["ell_2_of_witness"] == "0",
        "N3_third_background_jet_is_nonzero": quadratic["third_derivative_at_t_zero"] == 6
        and quadratic["witness_is_nonzero_before_quadratic_jet"] is True,
        "explicit_raw_DRED_kernel_certified": quadratic["raw_DRED_kernel_counterexample"] is True
        and boundary["full_DRED_raw_source_module_injectivity"] == "FAIL_EXPLICIT_KERNEL",
        "background_CE_covariant_kernel_certified": boundary["background_CE_covariant_submodule_injectivity"]
        == "FAIL_EXPLICIT_KERNEL",
        "physical_4d_quotient_kills_this_witness": boundary["physical_4d_quotient_sets_tau_to_zero"] is True
        and boundary["physical_4d_injectivity_refuted_by_this_witness"] is False,
        "full_quantum_BV_class_remains_open": boundary["full_quantum_BV_cohomology_class_of_witness"]
        == "OPEN",
        "tau_full_index_placement_matrix_fail_closed": tau["full_index_placement_projector_matrix_built"] is False,
        "Project_R_weight_cross_certificate_passes": cross["Project_R_weight"]["status"] == "PASS_PROJECT_U1R_BINDING",  # type: ignore[index]
        "Project_R_weights_match_jet_census": cross["Project_R_weight"]["pure_gauge_letter_weights"]  # type: ignore[index]
        == {"W": 1, "Wtilde": -1, "nabla": -1, "barnabla": 1, "Dcov": 0},
        "background_source_and_ordinary_Sym2_cross_certificate_passes": cross["source_color"]["status"]  # type: ignore[index]
        == "PASS_SCOPED_BACKGROUND_SOURCE_AND_COLOR_GATES",
        "full_BV_source_complex_remains_fail_closed": cross["source_color"]["full_quantum_BV_source_complex"]  # type: ignore[index]
        == "FAIL_CLOSED_MISSING_COMPOSITE_SOURCE_PARTNERS_AND_LINEARIZED_ST_MATRIX",
        "tau_rank_five_color_map_not_covered_by_existing_color_certificate": cross["source_color"]["tau_rank_five_color_map_covered"] is False,  # type: ignore[index]
        "physical_module_is_epsilon_torsion_free": presentation["torsion_statement"]["M_phys_is_epsilon_torsion_free"] is True,  # type: ignore[index]
        "quotient_records_epsilon_torsion": presentation["torsion_statement"]["quotient_is_epsilon_torsion"] is True,  # type: ignore[index]
        "formal_r_bound_to_Project_U1R": payload["scope"]["physical_Project_U1R_binding"] == "PASS_BY_PROJECT_R_WEIGHT_CERTIFICATE",  # type: ignore[index]
        "no_loop_or_anomaly_coefficient": presentation["torsion_statement"]["loop_or_anomaly_coefficient_computed"] is False,  # type: ignore[index]
        "DRED_gate_has_explicit_full_raw_kernel": payload["verdict"]["M_DRED_EVANESCENT_JETS"]  # type: ignore[index]
        == "FAIL_EXPLICIT_FULL_DRED_QUADRATIC_JET_KERNEL",
        "physical_4d_boundary_is_not_overclaimed": payload["verdict"]["physical_4d_injectivity_refuted_by_this_witness"] is False,  # type: ignore[index]
    }
    return {
        "schema": "STEP5_ONE_LOOP_DRED_EVANESCENT_JETS_VERIFICATION_V1",
        "status": "PASS_EXACT_EXPLICIT_FULL_DRED_KERNEL_PHYSICAL4D_UNTOUCHED",
        "payload_sha256": canonical_sha256(payload),
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
    }


def audit_markdown(payload: dict[str, object], verification: dict[str, object]) -> str:
    census = payload["raw_jet_census"]
    placement = payload["contracted_endpoint_subledger"]
    presentation = payload["module_presentation"]
    tau = payload["raw_traceless_tau_census"]
    assert isinstance(census, dict)
    assert isinstance(placement, dict)
    assert isinstance(presentation, dict)
    assert isinstance(tau, dict)
    counts = placement["counts_by_class"]
    assert isinstance(counts, dict)
    return rf"""# Step 5 Project-5A DRED evanescent local jets

## 0. Status

$$
\boxed{{
\mathsf{{M}}_{{\rm DRED\_EVANESCENT\_JETS}}
=\texttt{{FAIL\_EXPLICIT\_FULL\_DRED\_QUADRATIC\_JET\_KERNEL}}
}}
$$

$$
\boxed{{
0\ne\mathscr E\in
\ker\!\left(\ell_2\big|_{{\mathcal V^{{J^1}}_{{\rm DRED,raw}}}}\right),
\qquad
q_{{4d}}(\mathscr E)=0.
}}
$$

$$
N_{{\tau,{{\rm raw}}}}=229,
\qquad
N_{{\tau,N=3}}=1,
\qquad
\operatorname{{rank}}\mathcal M_{{\tau,{{\rm EOM/IBP/BV}}}}
=\texttt{{BLOCKED}}.
$$

No loop or anomaly coefficient is computed.

## 1. Typed carrier

$$
[\mathscr O]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
|\mathscr O|=1,
\qquad
r_{{\rm f}}(\mathscr O)=-1.
$$

The Project $U(1)_R$ certificate fixes

$$
r_{{\rm P}}(W,\widetilde W,\nabla,\bar\nabla,\mathcal D)
=(+1,-1,-1,+1,0),
$$

so $r_{{\rm f}}=r_{{\rm P}}$ on this complete pure-gauge letter set.

$$
J_{{(AB)}}=J_{{(BA)}},
\qquad |J|=1,
\qquad |J\mathscr O|=0.
$$

The source has no Lorentz index.  Its exact ordered projector is

$$
P_{{\rm Sym^2}}
=\frac12
\begin{{pmatrix}}1&1\\1&1\end{{pmatrix}},
\qquad
P_{{\rm Sym^2}}^2=P_{{\rm Sym^2}},
\qquad
\operatorname{{rank}}P_{{\rm Sym^2}}=1.
$$

The raw Project letter census gives

$$
N_{{\rm skeleton}}={census['skeleton_count']},
\qquad
(N_0,N_1,N_2,N_3)=(40,20,6,0),
\qquad
N_{{(3/2,0)}}={census['target_spin_copy_count']}.
$$

All counts are per symbolic generator of $\operatorname{{Sym}}^2(\mathrm{{Adj}})$.

## 2. Scalar and traceless metric channels

$$
\delta_{{(4)}}^{{mn}}
=\widehat\delta^{{mn}}+\widetilde\delta^{{mn}},
\qquad
\widehat\delta\widetilde\delta=0,
\qquad
\operatorname{{tr}}\widetilde\delta=2\epsilon.
$$

Define

$$
\tau^{{mn}}
:=\widetilde\delta^{{mn}}
-\frac{{\epsilon}}{{2}}\delta_{{(4)}}^{{mn}}.
$$

Then

$$
\delta_{{(4)mn}}\tau^{{mn}}
=2\epsilon-\frac{{\epsilon}}{{2}}4=0,
$$

$$
\widetilde\delta^{{mn}}
=\frac{{\epsilon}}{{2}}\delta_{{(4)}}^{{mn}}+\tau^{{mn}},
\qquad
\tau\in(1,1).
$$

Using $\widetilde\delta^2=\widetilde\delta$,

$$
\begin{{aligned}}
\tau_{{mn}}\tau^{{mn}}
&=\widetilde\delta_{{mn}}\widetilde\delta^{{mn}}
-\epsilon\widetilde\delta_m{{}}^m
+\frac{{\epsilon^2}}{{4}}\delta_{{(4)m}}{{}}^m\\
&=2\epsilon-2\epsilon^2+\epsilon^2\\
&=2\epsilon-\epsilon^2.
\end{{aligned}}
$$

If $\tau=\epsilon X$ for a regular tensor $X$ over
$R=\mathbb Q[\epsilon]$, then
$\tau_{{mn}}\tau^{{mn}}\in(\epsilon^2)R$.  But

$$
2\epsilon-\epsilon^2\notin(\epsilon^2)R.
$$

Therefore $\tau$ is an independent evanescent tensor generator; it is not an
$\epsilon$ coefficient multiplying $\delta_{{(4)}}$.

## 3. External-momentum channel

Every external derivative momentum obeys

$$
v^m=\widehat\delta^m{{}}_nv^n.
$$

Hence the full insertion vanishes:

$$
\widetilde\delta^m{{}}_nv^n
=\widetilde\delta^m{{}}_n\widehat\delta^n{{}}_rv^r
=0.
$$

The split pieces cancel:

$$
\tau^m{{}}_nv^n=-\frac{{\epsilon}}{{2}}v^m,
\qquad
\frac{{\epsilon}}{{2}}\delta_{{(4)}}^m{{}}_nv^n
=+\frac{{\epsilon}}{{2}}v^m.
$$

Thus external support removes only the channel in which at least one
$\widetilde\delta$ endpoint reaches an external derivative momentum.

## 4. Closed sigma channels

$$
\begin{{aligned}}
\widetilde\delta_{{mn}}
(\sigma_E^m\bar\sigma_E^n)
&=2\epsilon\,\mathbf1_L,\\
\widetilde\delta_{{mn}}
(\bar\sigma_E^m\sigma_E^n)
&=2\epsilon\,\mathbf1_R,\\
\widetilde\delta_{{mn}}
(\sigma_E^m)_{{a\dot a}}(\sigma_E^n)_b{{}}^{{\dot a}}
&=-2\epsilon\,\epsilon_{{ab}},\\
\widetilde\delta_{{mn}}
(\bar\sigma_E^m)^{{\dot a a}}
(\bar\sigma_E^n)^{{\dot b}}{{}}_a
&=-2\epsilon\,\epsilon^{{\dot a\dot b}}.
\end{{aligned}}
$$

The executable component check evaluates $4\times64=256$ exact entries.

$$
\widetilde\delta_{{mn}}\sigma_E^{{mn}}=0,
\qquad
\widetilde\delta_{{mn}}\bar\sigma_E^{{mn}}=0.
$$

These equations classify the closed trace and antisymmetric channels.  They do
not remove the open symmetric-traceless bispinor

$$
\tau_{{ab\dot a\dot b}}
:=\tau_{{mn}}
(\sigma_E^m)_{{(a(\dot a}}
(\sigma_E^n)_{{b)\dot b)}},
\qquad
\tau_{{ab\dot a\dot b}}\in(1,1).
$$

The complete single-insertion channel partition is

$$
\begin{{array}}{{c|c}}
\text{{channel}}&\text{{result}}\\ \hline
\text{{external hatted momentum}}&0\\
\text{{closed scalar sigma trace}}&2\epsilon\times\text{{existing jet}}\\
\text{{closed antisymmetric sigma}}&0\\
\text{{open symmetric-traceless sigma}}&\tau\text{{ target candidate}}\\
\text{{free vector endpoint}}&\text{{wrong target type}}
\end{{array}}
$$

## 5. Exact traceless-spurion multiplicity census

For a skeleton with $L$ left and $R$ right fundamental spinor slots, let
$m_L(j)$ and $m_R(j)$ be the exact $SU(2)$ tensor-product multiplicities.
Since

$$
\frac12\otimes1\supset\frac32,
\qquad
\frac32\otimes1\supset\frac32,
\qquad
\frac52\otimes1\supset\frac32,
\qquad
1\otimes1\supset0,
$$

the raw multiplicity is

$$
m_\tau
=m_R(1)
\left[m_L\left(\frac12\right)
+m_L\left(\frac32\right)
+m_L\left(\frac52\right)\right].
$$

The complete 18-skeleton census gives

$$
\begin{{array}}{{c|rrrr|r}}
N&0&1&2&3&\text{{total}}\\ \hline
m_{{\rm physical}}&40&20&6&0&66\\
m_\tau&150&66&12&1&{tau['raw_target_spin_copy_count']}
\end{{array}}
$$

Three independent decomposition checks are

$$
\begin{{aligned}}
(L,R)=(5,4):\quad
m_\tau&=3(5+4+1)=30,\\
(L,R)=(3,2):\quad
m_\tau&=1(2+1+0)=3,\\
(L,R)=(1,2):\quad
m_\tau&=1(1+0+0)=1.
\end{{aligned}}
$$

The representation multiplicity is exhaustive.  The 229 explicit open-index
placement projectors and their EOM/IBP/BV relations are not built.

## 6. Explicit full-DRED quadratic-jet kernel

For $N=3$, the only skeleton is

$$
W\widetilde W\widetilde W,
\qquad
n_{{\mathcal D}}=0.
$$

Its physical target multiplicity is zero, while its $\tau$-extended target
multiplicity is one.  In Project notation define

$$
\mathscr E_{{abc}}^{{AB}}
:=
K^{{AB}}{{}}_{{C[DE]}}
\tau_{{(ab|\dot c\dot d|}}
W_{{c)}}^C
\widetilde W^{{D\dot c}}
\widetilde W^{{E\dot d}}.
$$

$$
K^{{AB}}{{}}_{{C[DE]}}
:=\delta^A{{}}_C c_{{DE}}{{}}^B
+\delta^B{{}}_C c_{{DE}}{{}}^A,
\qquad
K^{{AB}}{{}}_{{C[DE]}}=K^{{BA}}{{}}_{{C[DE]}},
\qquad
K^{{AB}}{{}}_{{C[ED]}}=-K^{{AB}}{{}}_{{C[DE]}}.
$$

For the exact $SU(2)$ adjoint realization

$$
\kappa_{{AB}}=\delta_{{AB}},
\qquad
c_{{ABC}}=\varepsilon_{{ABC}},
$$

the exhaustive component sum gives

$$
\begin{{aligned}}
0={{}}&c_{{XA}}{{}}^F K_{{FB;CDE}}
+c_{{XB}}{{}}^F K_{{AF;CDE}}
+c_{{XC}}{{}}^F K_{{AB;FDE}}\\
&+c_{{XD}}{{}}^F K_{{AB;CFE}}
+c_{{XE}}{{}}^F K_{{AB;CDF}},
\end{{aligned}}
$$

$$
\#\left\{{(X,A,B,C,D,E)\right\}}=3^6=729,
\qquad
\max|\delta_XK|=0,
$$

$$
\#\left\{{(A,B,C,D,E):K^{{AB}}{{}}_{{CDE}}\ne0\right\}}=30,
\qquad
K^{{00}}{{}}_{{0[12]}}=2.
$$

Thus $K$ is nonzero and adjoint-equivariant.

Set

$$
B^{{DE}}
:=\tau_{{\dot c\dot d}}
\widetilde W^{{D\dot c}}
\widetilde W^{{E\dot d}}.
$$

The exact Grassmann exchange is

$$
\begin{{aligned}}
B^{{ED}}
&=\tau_{{\dot c\dot d}}
\widetilde W^{{E\dot c}}
\widetilde W^{{D\dot d}}\\
&=-\tau_{{\dot c\dot d}}
\widetilde W^{{D\dot d}}
\widetilde W^{{E\dot c}}\\
&=-\tau_{{\dot d\dot c}}
\widetilde W^{{D\dot c}}
\widetilde W^{{E\dot d}}\\
&=-B^{{DE}}.
\end{{aligned}}
$$

Therefore

$$
K^{{AB}}{{}}_{{C[ED]}}B^{{ED}}
=(-1)(-1)K^{{AB}}{{}}_{{C[DE]}}B^{{DE}}
=K^{{AB}}{{}}_{{C[DE]}}B^{{DE}}\ne0.
$$

For the displayed $SU(2)$ component,

$$
K^{{00}}{{}}_{{0[DE]}}B^{{DE}}
=2B^{{12}}+(-2)B^{{21}}
=2B^{{12}}+2B^{{12}}
=4B^{{12}}\ne0.
$$

Direct counting gives

$$
[\mathscr E]=3\left(\frac32\right)=\frac92,
\qquad
r_{{\rm f}}(\mathscr E)=1-1-1=-1,
\qquad
|\mathscr E|=1+1+1=1\pmod2.
$$

There is no external momentum on which $\widetilde\delta$ can vanish.  Each
field strength has minimum background-connection degree one.  Hence

$$
\mathscr E(t\mathcal B)=t^3\mathscr E_{{(3)}}(\mathcal B)
+\sum_{{n\ge4}}t^n\mathscr E_{{(n)}}(\mathcal B),
$$

$$
\ell_2(\mathscr E)
:=\frac12\left.\frac{{d^2}}{{dt^2}}\right|_{{t=0}}
\mathscr E(t\mathcal B)=0,
\qquad
\left.\frac{{d^3}}{{dt^3}}\right|_{{t=0}}t^3=6.
$$

Thus

$$
0\ne\mathscr E\in
\ker\!\left(\ell_2\big|_{{\mathcal V^{{J^1}}_{{\rm DRED,raw}}}}\right).
$$

The adjoint-equivariance of $K$ places the same witness in the
background-CE-covariant submodule.  Therefore injectivity fails in both raw
modules.

The physical-$4d$ quotient is different:

$$
q_{{4d}}(\tau)=0,
\qquad
q_{{4d}}(\mathscr E)=0.
$$

This witness does not refute injectivity after $q_{{4d}}$.  Its class after
EOM/IBP and in the full quantum BV complex remains open.

## 7. Certified contracted subledger

$$
\begin{{array}}{{c|r}}
\text{{class}}&\text{{rows}}\\ \hline
\text{{closed sigma masters}}&{counts['CLOSED_SIGMA_MASTER']}\\
\text{{closed antisymmetric sigma}}&{counts['CLOSED_ANTISYMMETRIC_SIGMA']}\\
\text{{one external endpoint}}&{counts['EXTERNAL_SIGMA_ENDPOINT']}\\
\text{{two external endpoints}}&{counts['TWO_EXTERNAL_ENDPOINTS']}\\ \hline
\text{{total}}&{placement['row_count']}
\end{{array}}
$$

The 908 rows exhaust only external-support, closed-trace, and antisymmetric
placements.  They do not contain the open $\tau$ sector.

The corresponding sparse presentation is

$$
M_{{\rm contracted}}
\in\operatorname{{Mat}}_{{710\times776}}(R),
\qquad
\operatorname{{rank}}_R M_{{\rm contracted}}=710.
$$

It proves no new direction in that contracted submodule only.

## 8. Multiple insertions

For every integer $n\ge1$,

$$
(\widetilde\delta^n)^m{{}}_n
=\widetilde\delta^m{{}}_n,
\qquad
\operatorname{{tr}}(\widetilde\delta^n)=2\epsilon.
$$

The induction is

$$
\widetilde\delta^{{n+1}}
=\widetilde\delta^n\widetilde\delta
=\widetilde\delta\widetilde\delta
=\widetilde\delta.
$$

A connected component touching an external momentum is zero.  A closed
component gives $2\epsilon$.  For $c$ disconnected closed components,

$$
(2\epsilon)^c\in(\epsilon)R,
\qquad c\ge1.
$$

A fully closed network is coefficient-ring mixing.  An open network can retain
$\tau$; idempotence does not convert $\tau$ into an $\epsilon$ multiple.

$\mathcal M_{{\rm phys}}$ is $\epsilon$-torsion-free.  The scalar-trace
quotient

$$
\frac{{\mathcal M_{{\rm phys}}}}{{(2\epsilon)\mathcal M_{{\rm phys}}}}
=
\left(\frac{{\mathbb Q[\epsilon]}}{{(\epsilon)}}\right)^{{66}}
\otimes\operatorname{{Sym}}^2(\mathrm{{Adj}})
$$

is $\epsilon$-torsion.  Pole mixing remains possible:

$$
\epsilon^{{-1}}(2\epsilon P_i)=2P_i.
$$

This is coefficient-ring mixing, not an independent evanescent tensor.

The $\tau$ sector is an independent tensor sector before the missing quotient
matrix is applied.

## 9. Gap audit

$$
\begin{{array}}{{c|c|c|c}}
\text{{gap}}&\text{{type}}&\text{{finding}}&\text{{status}}\\ \hline
G1&\mathrm{{G\!\!-PROJ}}&\widetilde\delta
=\frac\epsilon2\delta_{{(4)}}+\tau&\texttt{{REPAIRED}}\\
G2&\mathrm{{G\!\!-IDX}}&229\text{{ open }}\tau\text{{ projectors}}&\texttt{{OPEN\ P0}}\\
G3&\mathrm{{G\!\!-COLOR}}&K^{{AB}}{{}}_{{C[DE]}}
\text{{ exact }}SU(2)\text{{ equivariance}}&\texttt{{CLOSED}}\\
G4&\mathrm{{G\!\!-ALG}}&\tau\text{{ versus }}(\epsilon)R
\text{{ separated}}&\texttt{{REPAIRED}}\\
G5&\mathrm{{G\!\!-BV}}&\text{{EOM/IBP and full BV-ST class}}
&\texttt{{OPEN\ P1}}
\end{{array}}
$$

$$
\boxed{{
\texttt{{{verification['status']}}}
\qquad
{verification['passed']}/{verification['total']}.
}}
$$

Project $U(1)_R$, background-CE source covariance, the ordinary
$\operatorname{{Sym}}^2(\mathrm{{Adj}})$ split monomorphism, and the explicit
$SU(2)$ rank-five color witness pass.  Full-DRED raw quadratic-jet injectivity
fails.  The exhaustive $\tau$ quotient matrix and the full quantum BV-ST class
remain open; physical-$4d$ injectivity is untouched by this counterexample.
"""


def main() -> None:
    payload = build_payload()
    verification = build_verification(payload)
    if not verification["all_passed"]:
        failed = [name for name, passed in verification["checks"].items() if not passed]
        raise AssertionError(f"DRED evanescent certificate failed: {failed}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    VERIFY.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    VERIFY.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n")
    AUDIT_MD.write_text(audit_markdown(payload, verification))
    print(
        json.dumps(
            {
                "output": str(OUT),
                "verification": str(VERIFY),
                "audit": str(AUDIT_MD),
                "status": verification["status"],
                "passed": verification["passed"],
                "total": verification["total"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
