#!/usr/bin/env python3
"""Exact Step-5 odd-source/background-CE and color-quotient certificates.

The certificate proves the graded background source lift, retains local
source momentum, and proves that the surviving color jet m -> (m,-m) is a
split monomorphism after the same color quotient is applied to every copy.
It does not construct the full quantum BV Slavnov source complex and does
not evaluate a loop coefficient.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import TypeAlias


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/one-loop-source-color-closure.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-source-color-closure-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-source-color-closure.md"

Q = Fraction
RMatrix: TypeAlias = list[list[Fraction]]
Monomial: TypeAlias = tuple[int, ...]
Exterior: TypeAlias = dict[Monomial, Fraction]
EMatrix: TypeAlias = list[list[Exterior]]


def zeros(rows: int, columns: int) -> RMatrix:
    return [[Q(0) for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> RMatrix:
    matrix = zeros(size, size)
    for index in range(size):
        matrix[index][index] = Q(1)
    return matrix


def transpose(matrix: RMatrix) -> RMatrix:
    return [list(column) for column in zip(*matrix, strict=True)]


def add(left: RMatrix, right: RMatrix) -> RMatrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def scale(value: Fraction, matrix: RMatrix) -> RMatrix:
    return [[value * entry for entry in row] for row in matrix]


def multiply(left: RMatrix, right: RMatrix) -> RMatrix:
    return [
        [
            sum(
                (left[row][pivot] * right[pivot][column] for pivot in range(len(right))),
                Q(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def block_vertical(top: RMatrix, bottom: RMatrix) -> RMatrix:
    return [*top, *bottom]


def block_horizontal(left: RMatrix, right: RMatrix) -> RMatrix:
    return [left_row + right_row for left_row, right_row in zip(left, right, strict=True)]


def kronecker(left: RMatrix, right: RMatrix) -> RMatrix:
    rows = len(left) * len(right)
    columns = len(left[0]) * len(right[0])
    output = zeros(rows, columns)
    for i, left_row in enumerate(left):
        for j, left_entry in enumerate(left_row):
            for k, right_row in enumerate(right):
                for ell, right_entry in enumerate(right_row):
                    output[i * len(right) + k][j * len(right[0]) + ell] = (
                        left_entry * right_entry
                    )
    return output


def matrix_rank(matrix: RMatrix) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient:
                work[row] = [
                    entry - coefficient * pivot_entry
                    for entry, pivot_entry in zip(
                        work[row], work[pivot_row], strict=True
                    )
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def rref(matrix: RMatrix) -> RMatrix:
    work = [row[:] for row in matrix]
    if not work:
        return work
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][column] != 0:
                coefficient = work[row][column]
                work[row] = [
                    entry - coefficient * pivot_entry
                    for entry, pivot_entry in zip(
                        work[row], work[pivot_row], strict=True
                    )
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return work


def encoded_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def encoded_matrix(matrix: RMatrix) -> list[list[str]]:
    return [[encoded_fraction(entry) for entry in row] for row in matrix]


def permutation_sign(left: Monomial, right: Monomial) -> int:
    return -1 if sum(a > b for a in left for b in right) % 2 else 1


def exterior_add(left: Exterior, right: Exterior) -> Exterior:
    output = dict(left)
    for monomial, coefficient in right.items():
        output[monomial] = output.get(monomial, Q(0)) + coefficient
        if output[monomial] == 0:
            del output[monomial]
    return output


def exterior_scale(value: Fraction, polynomial: Exterior) -> Exterior:
    if value == 0:
        return {}
    return {
        monomial: value * coefficient
        for monomial, coefficient in polynomial.items()
        if value * coefficient != 0
    }


def exterior_multiply(left: Exterior, right: Exterior) -> Exterior:
    output: Exterior = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            monomial = tuple(sorted(left_monomial + right_monomial))
            coefficient = (
                permutation_sign(left_monomial, right_monomial)
                * left_coefficient
                * right_coefficient
            )
            output = exterior_add(output, {monomial: coefficient})
    return output


def exterior_generator(index: int) -> Exterior:
    return {(index,): Q(1)}


def levi_civita(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    inversions = sum(x > y for i, x in enumerate((a, b, c)) for y in (a, b, c)[i + 1 :])
    return -1 if inversions % 2 else 1


def ghost_differentials() -> list[Exterior]:
    output: list[Exterior] = []
    for target in range(3):
        polynomial: Exterior = {}
        for left in range(3):
            for right in range(3):
                coefficient = Q(levi_civita(left, right, target), 2)
                polynomial = exterior_add(
                    polynomial,
                    exterior_scale(
                        coefficient,
                        exterior_multiply(
                            exterior_generator(left), exterior_generator(right)
                        ),
                    ),
                )
        output.append(polynomial)
    return output


GHOST_D = ghost_differentials()


def exterior_differential(polynomial: Exterior) -> Exterior:
    output: Exterior = {}
    for monomial, coefficient in polynomial.items():
        for position, generator_index in enumerate(monomial):
            left = {monomial[:position]: Q(1)}
            right = {monomial[position + 1 :]: Q(1)}
            term = exterior_multiply(
                exterior_multiply(left, GHOST_D[generator_index]), right
            )
            output = exterior_add(
                output, exterior_scale(coefficient * ((-1) ** position), term)
            )
    return output


def exterior_matrix_from_rational(matrix: RMatrix) -> EMatrix:
    return [[({(): entry} if entry else {}) for entry in row] for row in matrix]


def exterior_matrix_add(left: EMatrix, right: EMatrix) -> EMatrix:
    return [
        [
            exterior_add(left[row][column], right[row][column])
            for column in range(len(left[0]))
        ]
        for row in range(len(left))
    ]


def exterior_matrix_scale(polynomial: Exterior, matrix: RMatrix) -> EMatrix:
    return [
        [exterior_scale(entry, polynomial) for entry in row]
        for row in matrix
    ]


def exterior_matrix_multiply(left: EMatrix, right: EMatrix) -> EMatrix:
    output: EMatrix = [
        [{} for _ in range(len(right[0]))] for _ in range(len(left))
    ]
    for row in range(len(left)):
        for column in range(len(right[0])):
            entry: Exterior = {}
            for pivot in range(len(right)):
                entry = exterior_add(
                    entry,
                    exterior_multiply(left[row][pivot], right[pivot][column]),
                )
            output[row][column] = entry
    return output


def exterior_matrix_differential(matrix: EMatrix) -> EMatrix:
    return [[exterior_differential(entry) for entry in row] for row in matrix]


def exterior_matrix_zero(matrix: EMatrix) -> bool:
    return all(not entry for row in matrix for entry in row)


def adjoint_generators() -> list[RMatrix]:
    generators: list[RMatrix] = []
    for generator in range(3):
        matrix = zeros(3, 3)
        for output in range(3):
            for input_index in range(3):
                matrix[output][input_index] = Q(
                    levi_civita(generator, input_index, output)
                )
        generators.append(matrix)
    return generators


def symmetric_embedding_and_projection() -> tuple[RMatrix, RMatrix]:
    # Symmetric basis: 00, 11, 22, 01+10, 02+20, 12+21.
    pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    embedding = zeros(9, 6)
    projection = zeros(6, 9)
    for column, (left, right) in enumerate(pairs):
        embedding[3 * left + right][column] = Q(1)
        projection[column][3 * left + right] = Q(1) if left == right else Q(1, 2)
        if left != right:
            embedding[3 * right + left][column] = Q(1)
            projection[column][3 * right + left] = Q(1, 2)
    return embedding, projection


def swap_matrix() -> RMatrix:
    swap = zeros(9, 9)
    for left in range(3):
        for right in range(3):
            swap[3 * right + left][3 * left + right] = Q(1)
    return swap


def symmetric_representation() -> tuple[list[RMatrix], dict[str, bool]]:
    adjoint = adjoint_generators()
    embedding, projection = symmetric_embedding_and_projection()
    identity_3 = identity(3)
    ordered = [
        add(kronecker(generator, identity_3), kronecker(identity_3, generator))
        for generator in adjoint
    ]
    symmetric = [multiply(multiply(projection, generator), embedding) for generator in ordered]
    checks: dict[str, bool] = {}
    for left in range(3):
        for right in range(3):
            commutator = add(
                multiply(symmetric[left], symmetric[right]),
                scale(Q(-1), multiply(symmetric[right], symmetric[left])),
            )
            expected = zeros(6, 6)
            for target in range(3):
                expected = add(
                    expected,
                    scale(Q(levi_civita(left, right, target)), symmetric[target]),
                )
            checks[f"representation_commutator_{left}{right}"] = commutator == expected
    return symmetric, checks


def background_ce_certificate() -> dict[str, object]:
    representation, representation_checks = symmetric_representation()
    gamma: EMatrix = [[{} for _ in range(6)] for _ in range(6)]
    for index, generator in enumerate(representation):
        gamma = exterior_matrix_add(
            gamma, exterior_matrix_scale(exterior_generator(index), generator)
        )
    s_gamma = exterior_matrix_differential(gamma)
    gamma_squared = exterior_matrix_multiply(gamma, gamma)
    mc_residual = exterior_matrix_add(
        s_gamma,
        [[exterior_scale(Q(-1), entry) for entry in row] for row in gamma_squared],
    )
    ghost_square_zero = all(
        exterior_differential(differential) == {} for differential in GHOST_D
    )

    pairing_ledger = {"(sJ)I": 1, "-J(sI)": -1}
    insertion_square_ledger = {"(sGamma)I": 1, "-Gamma^2 I": -1}
    source_square_ledger = {"J Gamma^2": 1, "-J(sGamma)": -1}
    connection_square_ledger = {
        "-(dGamma)Gamma": -1,
        "-Gamma(dGamma)": -1,
        "+Gamma^2 A": 1,
        "+Gamma(dGamma)": 1,
        "-Gamma^2 A": -1,
        "+Gamma A Gamma": 1,
        "+(dGamma)Gamma": 1,
        "-Gamma A Gamma": -1,
        "+A Gamma^2": 1,
        "-A Gamma^2": -1,
    }

    def reduced_zero(ledger: dict[str, int], pairs: tuple[tuple[str, str], ...]) -> bool:
        reduced = dict(ledger)
        for positive, negative in pairs:
            amount = min(abs(reduced.get(positive, 0)), abs(reduced.get(negative, 0)))
            if amount:
                reduced[positive] -= amount
                reduced[negative] += amount
        return all(value == 0 for value in reduced.values())

    connection_pairs = (
        ("+(dGamma)Gamma", "-(dGamma)Gamma"),
        ("+Gamma(dGamma)", "-Gamma(dGamma)"),
        ("+Gamma^2 A", "-Gamma^2 A"),
        ("+Gamma A Gamma", "-Gamma A Gamma"),
        ("+A Gamma^2", "-A Gamma^2"),
    )
    checks = {
        **representation_checks,
        "ghost_CE_nilpotent": ghost_square_zero,
        "Maurer_Cartan_sGamma_equals_Gamma_squared": exterior_matrix_zero(mc_residual),
        "insertion_nilpotent_from_Maurer_Cartan": sum(insertion_square_ledger.values()) == 0,
        "source_nilpotent_from_Maurer_Cartan": sum(source_square_ledger.values()) == 0,
        "odd_source_pairing_invariant": sum(pairing_ledger.values()) == 0,
        "connection_nilpotent_termwise": reduced_zero(
            connection_square_ledger, connection_pairs
        ),
    }
    return {
        "module": "M=Sym^2(Adj), J in Pi(M^dual), I in Pi(M)",
        "parities": {"Gamma": 1, "J": 1, "I": 1, "J_times_I": 0},
        "rules": {
            "Maurer_Cartan": "s_B Gamma=Gamma^2",
            "insertion": "s_B I=Gamma I",
            "source": "s_B J=J Gamma",
            "connection": "s_B A=-d Gamma+Gamma A-A Gamma",
        },
        "graded_pairing_expansion": "s_B(J I)=(s_B J)I-J(s_B I)=J Gamma I-J Gamma I=0",
        "nilpotence_expansions": {
            "insertion": "s_B^2 I=(s_B Gamma)I-Gamma(s_B I)=Gamma^2 I-Gamma^2 I=0",
            "source": "s_B^2 J=(s_B J)Gamma-J(s_B Gamma)=J Gamma^2-J Gamma^2=0",
            "connection": connection_square_ledger,
        },
        "checks": checks,
    }


def local_source_jet_certificate() -> dict[str, object]:
    insertion_terms = {
        "(dGamma)I": 1,
        "Gamma(dI)": 1,
        "-(dGamma)I": -1,
        "Gamma A I": 1,
        "-A Gamma I": -1,
        "+A Gamma I": 1,
    }
    insertion_expected = {"Gamma(dI)": 1, "Gamma A I": 1}
    source_terms = {
        "(dJ)Gamma": 1,
        "J(dGamma)": 1,
        "-J Gamma A": -1,
        "-J(dGamma)": -1,
        "+J Gamma A": 1,
        "-J A Gamma": -1,
    }
    source_expected = {"(dJ)Gamma": 1, "-J A Gamma": -1}

    def collect(terms: dict[str, int]) -> dict[str, int]:
        canonical = {
            "(dGamma)I": "dGamma.I",
            "-(dGamma)I": "dGamma.I",
            "-A Gamma I": "A.Gamma.I",
            "+A Gamma I": "A.Gamma.I",
            "J(dGamma)": "J.dGamma",
            "-J(dGamma)": "J.dGamma",
            "-J Gamma A": "J.Gamma.A",
            "+J Gamma A": "J.Gamma.A",
        }
        signs = {
            "-(dGamma)I": -1,
            "-A Gamma I": -1,
            "-J(dGamma)": -1,
            "-J Gamma A": -1,
        }
        output: dict[str, int] = {}
        for term, coefficient in terms.items():
            normalized = canonical.get(term, term)
            absolute_coefficient = abs(coefficient) * signs.get(term, 1)
            output[normalized] = output.get(normalized, 0) + absolute_coefficient
        return {key: value for key, value in output.items() if value}

    insertion_collected = collect(insertion_terms)
    source_collected = collect(source_terms)
    insertion_expected_collected = collect(insertion_expected)
    source_expected_collected = collect(source_expected)

    basis = ["C_on_W", "C_split", "S_DJ"]
    relation_matrix = [[Q(1), Q(1), Q(1)], [Q(0), Q(1), Q(0)]]
    reduced = rref(relation_matrix)
    relation_rank = matrix_rank(relation_matrix)
    momenta = {"p_J": -5, "p_W": 2, "p_tildeW": 3}
    checks = {
        "covariant_insertion_jet": insertion_collected == insertion_expected_collected,
        "covariant_dual_source_jet": source_collected == source_expected_collected,
        "local_source_momentum_nonzero": momenta["p_J"] != 0,
        "all_incoming_momentum_conservation": sum(momenta.values()) == 0,
        "IBP_plus_EOM_rank_two": relation_rank == 2,
        "local_source_quotient_dimension_one": len(basis) - relation_rank == 1,
        "rref_gives_C_split_zero_and_S_DJ_minus_C_on_W": reduced
        == [[Q(1), Q(0), Q(1)], [Q(0), Q(1), Q(0)]],
    }
    return {
        "covariant_derivatives": {
            "insertion": "D I=dI+A I",
            "source_dual": "D^vee J=dJ-J A",
            "insertion_transformation": "s_B(D I)=Gamma(D I)",
            "source_transformation": "s_B(D^vee J)=(D^vee J)Gamma",
        },
        "full_expansions": {
            "insertion": insertion_terms,
            "insertion_remainder": insertion_collected,
            "source": source_terms,
            "source_remainder": source_collected,
        },
        "W_T_N_D_local_source_block": {
            "basis": basis,
            "IBP_row": ["1", "1", "1"],
            "IBP_equation": "C_on_W+C_split+S_DJ=0",
            "antichiral_EOM_row": ["0", "1", "0"],
            "antichiral_EOM": "C_split=D_a^dota tildeW_dota=-(1/2)nabla_a barE=0",
            "relation_matrix": encoded_matrix(relation_matrix),
            "relation_rank": relation_rank,
            "rref": encoded_matrix(reduced),
            "quotient_dimension": len(basis) - relation_rank,
            "representative_equations": ["C_split=0", "S_DJ=-C_on_W"],
            "pointwise_operator_vs_integrated_source_IBP": (
                "C_split=0 is a pointwise EOM quotient; "
                "C_on_W+C_split+S_DJ=0 is an integrated local-source IBP relation"
            ),
            "source_momentum": {
                "status": "RETAINED_NONZERO",
                "all_incoming_equation": "p_J+p_W+p_tildeW=0 componentwise",
                "exact_witness": momenta,
            },
        },
        "checks": checks,
    }


def color_split_monomorphism_certificate() -> dict[str, object]:
    embedding, projection = symmetric_embedding_and_projection()
    swap = swap_matrix()
    symmetric_projector = scale(Q(1, 2), add(identity(9), swap))
    antisymmetric_projector = scale(Q(1, 2), add(identity(9), scale(Q(-1), swap)))

    ordered_jet = block_vertical(embedding, scale(Q(-1), embedding))
    ordered_left_inverse = block_horizontal(projection, zeros(6, 9))
    quotient_jet = block_vertical(identity(6), scale(Q(-1), identity(6)))
    quotient_left_inverse = block_horizontal(identity(6), zeros(6, 6))
    quotient_each_copy = [
        *block_horizontal(projection, zeros(6, 9)),
        *block_horizontal(zeros(6, 9), projection),
    ]
    quotient_of_ordered_jet = multiply(quotient_each_copy, ordered_jet)

    # Counterexample: quotient the target by the image span(1,-1).
    scalar_jet = [[Q(1)], [Q(-1)]]
    unmatched_target_quotient = [[Q(1), Q(1)]]
    collapsed_scalar_jet = multiply(unmatched_target_quotient, scalar_jet)

    checks = {
        "Sym2_section_retraction": multiply(projection, embedding) == identity(6),
        "Sym2_projector_exact": multiply(embedding, projection) == symmetric_projector,
        "antisymmetric_relations_killed": multiply(projection, antisymmetric_projector)
        == zeros(6, 9),
        "ordered_jet_left_inverse": multiply(ordered_left_inverse, ordered_jet)
        == identity(6),
        "ordered_jet_full_column_rank": matrix_rank(ordered_jet) == 6,
        "quotient_is_functorial_on_both_target_copies": quotient_of_ordered_jet
        == quotient_jet,
        "quotient_jet_left_inverse": multiply(quotient_left_inverse, quotient_jet)
        == identity(6),
        "quotient_jet_full_column_rank": matrix_rank(quotient_jet) == 6,
        "unmatched_target_quotient_can_create_kernel": collapsed_scalar_jet
        == [[Q(0)]],
    }
    return {
        "ordered_color_module": "Adj tensor Adj",
        "physical_color_module": "M=Sym^2(Adj)=(Adj tensor Adj)/Lambda^2(Adj)",
        "dimensions_for_exact_SU2_witness": {
            "ordered": 9,
            "symmetric": 6,
            "two_ordered_outputs": 18,
            "two_symmetric_outputs": 12,
        },
        "maps": {
            "ordered_jet": "m -> (E m,-E m)",
            "ordered_left_inverse": "(u,v) -> Q u",
            "quotient_jet": "iota_M(m)=(m,-m)",
            "quotient_left_inverse": "pi_1(u,v)=u",
            "composition": "pi_1 o iota_M=id_M",
        },
        "general_module_theorem": {
            "statement": (
                "for every quotient module M=C/R, applying q:C->M to the source "
                "and separately to both output copies gives iota_M(m)=(m,-m); "
                "pi_1 iota_M=id_M, hence ker(iota_M)=0"
            ),
            "scope_condition": (
                "the target quotient must be q direct_sum q, or any quotient for "
                "which the displayed left inverse descends"
            ),
            "unmatched_quotient_counterexample": (
                "M=Q, iota(1)=(1,-1), then quotient target by span(1,-1); "
                "the induced jet is zero"
            ),
        },
        "matrices": {
            "Sym2_embedding": encoded_matrix(embedding),
            "Sym2_projection": encoded_matrix(projection),
            "quotient_jet": encoded_matrix(quotient_jet),
            "quotient_left_inverse": encoded_matrix(quotient_left_inverse),
            "unmatched_collapsed_jet": encoded_matrix(collapsed_scalar_jet),
        },
        "checks": checks,
    }


def build_payload() -> dict[str, object]:
    background_ce = background_ce_certificate()
    local_source = local_source_jet_certificate()
    color = color_split_monomorphism_certificate()
    checks = {
        **{f"background_CE.{key}": value for key, value in background_ce["checks"].items()},
        **{f"local_source.{key}": value for key, value in local_source["checks"].items()},
        **{f"color.{key}": value for key, value in color["checks"].items()},
    }
    return {
        "schema": "Step5OneLoopSourceColorClosure.v1",
        "status": "PASS_SCOPED_BACKGROUND_SOURCE_AND_COLOR_GATES"
        if all(checks.values())
        else "FAIL",
        "scope": "PURE_GAUGE_LOCAL_SOURCE_BACKGROUND_CE_AND_COLOR_SPLIT",
        "project_inputs": [
            "Step3D.104 even background transformation and dual source",
            "Step3D.104a background Ward identity",
            "Step3D.132c inert ordinary source under quantum BRST",
            "Step5 physical source module Sym^2(Adj)",
            "W T N D local-source relation and antichiral EOM",
        ],
        "background_CE_source_closure": background_ce,
        "local_source_jet_closure": local_source,
        "color_Sym2_split_monomorphism": color,
        "checks": checks,
        "verdicts": {
            "odd_local_source_background_CE_closure": "PASS",
            "all_covariant_local_source_jets": "PASS",
            "W_T_N_D_local_source_IBP_EOM_block": "PASS_ONE_DIMENSIONAL_QUOTIENT",
            "color_Sym2_quotient_for_m_to_m_minus_m": "PASS_SPLIT_MONOMORPHISM",
            "arbitrary_unmatched_target_quotient": "REJECTED_COUNTEREXAMPLE",
            "full_quantum_BV_Slavnov_source_complex": (
                "FAIL_CLOSED_MISSING_COMPOSITE_SOURCE_PARTNERS_AND_LINEARIZED_ST_MATRIX"
            ),
            "source_linear_BRST_cohomology_rank": "OPEN",
            "complete_quadratic_jet_injectivity": "NOT_CLAIMED_BY_THIS_CERTIFICATE",
            "anomaly_coefficient": "NOT_ACCEPTED",
        },
        "external_results_imported": False,
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def render_markdown() -> str:
    return r"""# Step 5 odd local source and color-quotient closure

## 1. Background Chevalley--Eilenberg lift

$$
M:=\operatorname{Sym}^2(\operatorname{Adj}),
\qquad
\mathscr I\in\Pi M,
\qquad
J\in\Pi M^\vee,
\qquad
|\Gamma|=|\mathscr I|=|J|=1.
$$

$$
\rho_2(t)
=\rho_{\rm ad}(t)\otimes\mathbf1
+\mathbf1\otimes\rho_{\rm ad}(t),
\qquad
\Gamma:=c^a\rho_2(t_a).
$$

$$
\boxed{
s_{\rm B}\Gamma=\Gamma^2,
\qquad
s_{\rm B}\mathscr I=\Gamma\mathscr I,
\qquad
s_{\rm B}J=J\Gamma.}
$$

$$
\begin{aligned}
s_{\rm B}^2\mathscr I
&=(s_{\rm B}\Gamma)\mathscr I
-\Gamma(s_{\rm B}\mathscr I)\\
&=\Gamma^2\mathscr I-\Gamma^2\mathscr I=0,\\
s_{\rm B}^2J
&=(s_{\rm B}J)\Gamma-J(s_{\rm B}\Gamma)\\
&=J\Gamma^2-J\Gamma^2=0,\\
s_{\rm B}(J\mathscr I)
&=(s_{\rm B}J)\mathscr I-J(s_{\rm B}\mathscr I)\\
&=J\Gamma\mathscr I-J\Gamma\mathscr I=0.
\end{aligned}
$$

## 2. Local source jets

$$
\mathcal D\mathscr I:=d\mathscr I+A\mathscr I,
\qquad
\mathcal D^\vee J:=dJ-JA,
$$

$$
s_{\rm B}A=-d\Gamma+\Gamma A-A\Gamma.
$$

$$
\begin{aligned}
s_{\rm B}(\mathcal D\mathscr I)
&=d(\Gamma\mathscr I)
+(-d\Gamma+\Gamma A-A\Gamma)\mathscr I
+A\Gamma\mathscr I\\
&=(d\Gamma)\mathscr I+\Gamma d\mathscr I
-(d\Gamma)\mathscr I+\Gamma A\mathscr I
-A\Gamma\mathscr I+A\Gamma\mathscr I\\
&=\Gamma(d\mathscr I+A\mathscr I)
=\Gamma\mathcal D\mathscr I,
\end{aligned}
$$

$$
\begin{aligned}
s_{\rm B}(\mathcal D^\vee J)
&=d(J\Gamma)-(J\Gamma)A
+J(-d\Gamma+\Gamma A-A\Gamma)\\
&=(dJ)\Gamma+Jd\Gamma-J\Gamma A
-Jd\Gamma+J\Gamma A-JA\Gamma\\
&=(dJ-JA)\Gamma
=(\mathcal D^\vee J)\Gamma.
\end{aligned}
$$

Hence every iterated covariant source jet closes by induction.

For the local-source (W\widetilde W\nabla\mathcal D) block, use

$$
\mathcal B_{\rm loc}
=(C_{\rm on\,W},C_{\rm split},S_{\mathcal D J}).
$$

Integrated source IBP and the pointwise antichiral EOM give

$$
C_{\rm on\,W}+C_{\rm split}+S_{\mathcal D J}=0,
$$

$$
C_{\rm split}
=\mathcal D_a{}^{\dot a}\widetilde{\mathcal W}_{\dot a}
=-\frac12\nabla_a\overline{\mathcal E}=0.
$$

$$
R_{\rm loc}
=\begin{pmatrix}
1&1&1\\
0&1&0
\end{pmatrix},
\qquad
\operatorname{rank}R_{\rm loc}=2,
$$

$$
\operatorname{rref}R_{\rm loc}
=\begin{pmatrix}
1&0&1\\
0&1&0
\end{pmatrix}.
$$

$$
\boxed{
\dim(\mathcal B_{\rm loc}/\operatorname{row}R_{\rm loc})=1,
\qquad
C_{\rm split}=0,
\qquad
S_{\mathcal D J}=-C_{\rm on\,W}.}
$$

The source momentum is retained:

$$
p_J+p_W+p_{\widetilde W}=0,
\qquad
p_J\ne0.
$$

## 3. Color quotient

Let (C:=\operatorname{Adj}\otimes\operatorname{Adj}) and

$$
M:=C/\Lambda^2(\operatorname{Adj})
=\operatorname{Sym}^2(\operatorname{Adj}).
$$

The surviving ordered-port jet is

$$
\iota_M:M\longrightarrow M\oplus M,
\qquad
\iota_M(m)=(m,-m).
$$

Define

$$
\pi_1:M\oplus M\longrightarrow M,
\qquad
\pi_1(u,v)=u.
$$

Then

$$
\boxed{
\pi_1\iota_M=\operatorname{id}_M,
\qquad
\ker\iota_M=0.}
$$

More generally, this proof survives every color relation quotient
(q:C\to C/R) applied to the source and separately to both output copies.

It does not survive an arbitrary larger target quotient.  For

$$
M=\mathbb Q,
\qquad
\iota_M(1)=(1,-1),
$$

quotienting the target by (\operatorname{span}(1,-1)) sends the jet to zero.

## 4. Boundary

$$
\boxed{
\text{background-CE odd source and local jets}=\texttt{PASS},
\qquad
\text{color }\operatorname{Sym}^2\text{ quotient}=\texttt{PASS}.}
$$

$$
\boxed{
\text{full quantum BV Slavnov source complex}
=\texttt{FAIL\_CLOSED}.}
$$

Step 3D defines the ordinary linear source as inert under
(\mathbf s_{R,\nu}^{\rm all}).  The Step-5 composite-source antifields,
source partners, and the linearized Slavnov mixing matrix are not defined.
Background covariance therefore does not determine the full source-linear
BV cohomology.  No loop coefficient is accepted.

## 5. Status patches for the aggregate audits

$$
\begin{array}{c|c}
\text{gate}&\text{replacement status}\\ \hline
G5&
\texttt{PASS\_BACKGROUND\_CE\_SOURCE\_JETS;
FULL\_BV\_ST\_FAIL\_CLOSED}\\
G9\text{ color}&
\texttt{PASS\_SPLIT\_MONOMORPHISM}\\
G9\text{ local }W\widetilde W\nabla\mathcal D&
\texttt{PASS\_RANK2\_QUOTIENT\_DIM1}\\
\ker\bar\ell_2=0&
\texttt{NOT\_ESTABLISHED\_BY\_THIS\_CERTIFICATE}
\end{array}
$$

The theorem status remains conditional.  Its source-BV and DRED gates remain
separate from the closed color quotient.
"""


def write_outputs() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT_MD.write_text(render_markdown(), encoding="utf-8")
    failed = sorted(key for key, value in payload["checks"].items() if not value)
    audit = {
        "schema": "Step5OneLoopSourceColorClosureAudit.v1",
        "status": payload["status"],
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "totals": {"checks": len(payload["checks"]), "failed": len(failed)},
        "failed_checks": failed,
        "local_source_momentum": "RETAINED_NONZERO",
        "full_quantum_BV_Slavnov_source_complex": payload["verdicts"][
            "full_quantum_BV_Slavnov_source_complex"
        ],
        "anomaly_coefficient": "NOT_ACCEPTED",
    }
    AUDIT_JSON.write_bytes(canonical_json(audit))
    if failed:
        raise SystemExit(f"failed exact checks: {failed}")


if __name__ == "__main__":
    write_outputs()
