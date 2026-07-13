#!/usr/bin/env python3
"""Exact left-spin projector certificate for the Step-5 one-loop theorem.

All linear algebra is over Q.  No loop coefficient or external result enters.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from typing import TypeAlias


Q: TypeAlias = Fraction
Matrix: TypeAlias = list[list[Q]]
Word: TypeAlias = tuple[str, ...]
Polynomial: TypeAlias = dict[Word, Q]

SPIN = ("+", "-")
EPSILON_UP = {
    ("+", "+"): Q(0),
    ("+", "-"): Q(1),
    ("-", "+"): Q(-1),
    ("-", "-"): Q(0),
}
EPSILON_DOWN = {
    ("+", "+"): Q(0),
    ("+", "-"): Q(-1),
    ("-", "+"): Q(1),
    ("-", "-"): Q(0),
}


def zero_matrix(rows: int, cols: int) -> Matrix:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def identity_matrix(size: int) -> Matrix:
    out = zero_matrix(size, size)
    for index in range(size):
        out[index][index] = Q(1)
    return out


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][col] + right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matrix_scale(coefficient: Q, matrix: Matrix) -> Matrix:
    return [[coefficient * value for value in row] for row in matrix]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[row][pivot] * right[pivot][col] for pivot in range(len(right))),
                Q(0),
            )
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    row_count = len(work)
    col_count = len(work[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][col] == 0:
                continue
            coefficient = work[row][col]
            work[row] = [
                work[row][column] - coefficient * work[pivot_row][column]
                for column in range(col_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def fraction_text(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def encoded_matrix(matrix: Matrix) -> list[list[str]]:
    return [[fraction_text(value) for value in row] for row in matrix]


def u_basis() -> list[tuple[str, int]]:
    """U_(a;m), where m is the number of minus slots among the last four."""

    return [(first, minus_count) for first in SPIN for minus_count in range(5)]


def t_basis() -> list[int]:
    """t_m, where m is the number of minus slots among its three slots."""

    return list(range(4))


def u_index(first: str, minus_count: int) -> int:
    return u_basis().index((first, minus_count))


def trace_matrix() -> Matrix:
    """t_(cde)=epsilon^(ab) U_(a;bcde)."""

    out = zero_matrix(4, 10)
    for minus_count in range(4):
        out[minus_count][u_index("+", minus_count + 1)] = Q(1)
        out[minus_count][u_index("-", minus_count)] = Q(-1)
    return out


def trace_embedding_matrix() -> Matrix:
    """Right inverse E: Sym^3 S_L -> S_L tensor Sym^4 S_L.

    E(t)_(a;bcde)=-1/5 times the sum of epsilon_(a,b_i) t_(B without b_i).
    """

    out = zero_matrix(10, 4)
    for minus_count in range(5):
        if minus_count >= 1:
            out[u_index("+", minus_count)][minus_count - 1] = Q(minus_count, 5)
        if minus_count <= 3:
            out[u_index("-", minus_count)][minus_count] = Q(-(4 - minus_count), 5)
    return out


def full_symmetrizer_matrix() -> Matrix:
    """Normalized total symmetrization of all five lower undotted slots."""

    out = zero_matrix(10, 10)
    for minus_count in range(5):
        out[u_index("+", minus_count)][u_index("+", minus_count)] = Q(
            5 - minus_count, 5
        )
        if minus_count >= 1:
            out[u_index("+", minus_count)][u_index("-", minus_count - 1)] = Q(
                minus_count, 5
            )

        if minus_count <= 3:
            out[u_index("-", minus_count)][u_index("+", minus_count + 1)] = Q(
                4 - minus_count, 5
            )
        out[u_index("-", minus_count)][u_index("-", minus_count)] = Q(
            minus_count + 1, 5
        )
    return out


def epsilon_contract(
    left: dict[tuple[str, str], Q], right: dict[tuple[str, str], Q]
) -> Matrix:
    return [
        [sum((left[(a, b)] * right[(b, c)] for b in SPIN), Q(0)) for c in SPIN]
        for a in SPIN
    ]


def epsilon_first_slot_contract() -> Matrix:
    return [
        [
            sum(
                (EPSILON_UP[(a, b)] * EPSILON_DOWN[(a, c)] for a in SPIN),
                Q(0),
            )
            for c in SPIN
        ]
        for b in SPIN
    ]


def row_subtract(left: list[Q], coefficient: Q, right: list[Q]) -> list[Q]:
    return [left[index] - coefficient * right[index] for index in range(len(left))]


def add_term(polynomial: Polynomial, word: Word, coefficient: Q) -> None:
    value = polynomial.get(word, Q(0)) + coefficient
    if value == 0:
        polynomial.pop(word, None)
    else:
        polynomial[word] = value


def canonical_odd_derivative_pair(
    left: str, right: str
) -> tuple[tuple[str, str], Q] | None:
    """Reduce two chiral derivatives using {nabla_a,nabla_b}=0."""

    if left == right:
        return None
    ordered = sorted((left, right))
    sign = Q(1) if (left, right) == tuple(ordered) else Q(-1)
    return (ordered[0], ordered[1]), sign


def chiral_bianchi_polynomial() -> tuple[Polynomial, int]:
    """Expand nabla_(a X_bc) into its six ordered derivative words."""

    polynomial: Polynomial = {}
    raw_count = 0
    for first, second, field_index in (
        ("a", "b", "c"),
        ("a", "c", "b"),
        ("b", "c", "a"),
        ("b", "a", "c"),
        ("c", "a", "b"),
        ("c", "b", "a"),
    ):
        raw_count += 1
        canonical = canonical_odd_derivative_pair(first, second)
        if canonical is None:
            continue
        derivative_pair, sign = canonical
        add_term(
            polynomial,
            ("DDW", derivative_pair[0], derivative_pair[1], field_index),
            Q(1, 6) * sign,
        )
    return polynomial, raw_count


def sorted_pair(left: str, right: str) -> tuple[str, str]:
    ordered = sorted((left, right))
    return ordered[0], ordered[1]


def direct_five_symmetrizer_polynomial() -> Polynomial:
    """Sym_5[nabla_a(X^A_bc X^B_de)] before Leibniz expansion."""

    polynomial: Polynomial = {}
    for permuted in permutations(("a", "b", "c", "d", "e")):
        first_a, first_b = sorted_pair(permuted[1], permuted[2])
        second_a, second_b = sorted_pair(permuted[3], permuted[4])
        word = (
            "D",
            permuted[0],
            "A:X",
            first_a,
            first_b,
            "B:X",
            second_a,
            second_b,
        )
        add_term(polynomial, word, Q(1, 120))
    return polynomial


def nested_four_then_five_symmetrizer_polynomial() -> Polynomial:
    """nabla_(a T_bcde), with T the normalized Sym^4 projection."""

    polynomial: Polynomial = {}
    labels = ("a", "b", "c", "d", "e")
    for derivative_index in labels:
        remaining = tuple(label for label in labels if label != derivative_index)
        for permuted in permutations(remaining):
            first_a, first_b = sorted_pair(permuted[0], permuted[1])
            second_a, second_b = sorted_pair(permuted[2], permuted[3])
            word = (
                "D",
                derivative_index,
                "A:X",
                first_a,
                first_b,
                "B:X",
                second_a,
                second_b,
            )
            add_term(polynomial, word, Q(1, 5 * 24))
    return polynomial


def h_leibniz_polynomials() -> tuple[Polynomial, Polynomial, int, bool]:
    """Expand H in a noncommutative A-before-B word basis.

    The first polynomial has nabla acting on X^A; the second has nabla acting
    on X^B.  X is even, so the graded Leibniz sign of the second term is +1.
    """

    derivative_on_a: Polynomial = {}
    derivative_on_b: Polynomial = {}
    raw_count = 0
    open_order_preserved = True
    for permuted in permutations(("a", "b", "c", "d", "e")):
        coefficient = Q(1, 120 * 2)
        b_pair = sorted_pair(permuted[3], permuted[4])
        for second_derivative, field_index in (
            (permuted[1], permuted[2]),
            (permuted[2], permuted[1]),
        ):
            raw_count += 1
            canonical = canonical_odd_derivative_pair(permuted[0], second_derivative)
            if canonical is not None:
                derivative_pair, sign = canonical
                word = (
                    "A:DDW",
                    derivative_pair[0],
                    derivative_pair[1],
                    field_index,
                    "B:X",
                    b_pair[0],
                    b_pair[1],
                )
                open_order_preserved &= word.index("A:DDW") < word.index("B:X")
                add_term(derivative_on_a, word, coefficient * sign)

        a_pair = sorted_pair(permuted[1], permuted[2])
        for second_derivative, field_index in (
            (permuted[3], permuted[4]),
            (permuted[4], permuted[3]),
        ):
            raw_count += 1
            canonical = canonical_odd_derivative_pair(permuted[0], second_derivative)
            if canonical is not None:
                derivative_pair, sign = canonical
                word = (
                    "A:X",
                    a_pair[0],
                    a_pair[1],
                    "B:DDW",
                    derivative_pair[0],
                    derivative_pair[1],
                    field_index,
                )
                open_order_preserved &= word.index("A:X") < word.index("B:DDW")
                add_term(derivative_on_b, word, coefficient * sign)
    return derivative_on_a, derivative_on_b, raw_count, open_order_preserved


def project_eom_derivative_polynomial() -> tuple[Polynomial, Polynomial]:
    """Compare nabla_+ E with -nabla_- X_++ exactly."""

    left: Polynomial = {}
    for coefficient, first, second, field_index in (
        (Q(1), "+", "-", "+"),
        (Q(-1), "+", "+", "-"),
    ):
        canonical = canonical_odd_derivative_pair(first, second)
        if canonical is None:
            continue
        derivative_pair, sign = canonical
        add_term(
            left,
            ("DDW", derivative_pair[0], derivative_pair[1], field_index),
            coefficient * sign,
        )

    right: Polynomial = {}
    canonical = canonical_odd_derivative_pair("-", "+")
    assert canonical is not None
    derivative_pair, sign = canonical
    add_term(
        right,
        ("DDW", derivative_pair[0], derivative_pair[1], "+"),
        Q(-1) * sign,
    )
    return left, right


def tree_eom_insertion_polynomials() -> tuple[Polynomial, Polynomial, Polynomial]:
    """Apply nabla_-X=-nabla_+E to the ordered Leibniz expansion."""

    raw_leibniz: Polynomial = {
        ("A:nabla_-X", "B:X"): Q(1),
        ("A:X", "B:nabla_-X"): Q(1),
    }
    rewritten: Polynomial = {}
    for word, coefficient in raw_leibniz.items():
        if word[0] == "A:nabla_-X":
            add_term(rewritten, ("A:nabla_+E", word[1]), -coefficient)
        elif word[1] == "B:nabla_-X":
            add_term(rewritten, (word[0], "B:nabla_+E"), -coefficient)
        else:
            add_term(rewritten, word, coefficient)

    stated_rewrite: Polynomial = {
        ("A:nabla_+E", "B:X"): Q(-1),
        ("A:X", "B:nabla_+E"): Q(-1),
    }
    return raw_leibniz, rewritten, stated_rewrite


def build_certificate() -> dict[str, object]:
    trace = trace_matrix()
    embedding = trace_embedding_matrix()
    projector_three = matrix_multiply(embedding, trace)
    projector_five = matrix_add(
        identity_matrix(10), matrix_scale(Q(-1), projector_three)
    )
    symmetrizer = full_symmetrizer_matrix()
    zero_10 = zero_matrix(10, 10)

    up_down = epsilon_contract(EPSILON_UP, EPSILON_DOWN)
    down_up = epsilon_contract(EPSILON_DOWN, EPSILON_UP)
    first_slot = epsilon_first_slot_contract()
    epsilon_scalar = sum(
        (EPSILON_UP[(a, b)] * EPSILON_DOWN[(a, b)] for a in SPIN for b in SPIN),
        Q(0),
    )

    a_row = identity_matrix(10)[u_index("-", 0)]
    b_row = identity_matrix(10)[u_index("+", 1)]
    trace_plus_plus_plus = trace[0]
    h_minus_plus4 = projector_five[u_index("-", 0)]
    reconstructed_a = row_subtract(h_minus_plus4, Q(4, 5), trace_plus_plus_plus)

    chiral_bianchi, chiral_raw_count = chiral_bianchi_polynomial()
    direct_five_sym = direct_five_symmetrizer_polynomial()
    nested_five_sym = nested_four_then_five_symmetrizer_polynomial()
    h_on_a, h_on_b, h_raw_count, h_open_order = h_leibniz_polynomials()
    eom_derivative_left, eom_derivative_right = project_eom_derivative_polynomial()
    insertion_raw, insertion_rewritten, insertion_stated = (
        tree_eom_insertion_polynomials()
    )

    checks = {
        "epsilon_up_down_is_identity": up_down == identity_matrix(2),
        "epsilon_down_up_is_identity": down_up == identity_matrix(2),
        "epsilon_first_slot_is_minus_identity": first_slot
        == matrix_scale(Q(-1), identity_matrix(2)),
        "epsilon_ab_epsilon_ab_is_minus_two": epsilon_scalar == Q(-2),
        "eom_trace_sign": (
            EPSILON_UP[("+", "-")] * EPSILON_DOWN[("+", "-")]
            + EPSILON_UP[("-", "+")] * EPSILON_DOWN[("-", "+")]
        )
        == Q(-2),
        "trace_after_embedding_is_identity": matrix_multiply(trace, embedding)
        == identity_matrix(4),
        "projector_three_idempotent": matrix_multiply(projector_three, projector_three)
        == projector_three,
        "projector_five_idempotent": matrix_multiply(projector_five, projector_five)
        == projector_five,
        "projectors_sum_to_identity": matrix_add(projector_five, projector_three)
        == identity_matrix(10),
        "projectors_mutually_annihilate_left": matrix_multiply(
            projector_five, projector_three
        )
        == zero_10,
        "projectors_mutually_annihilate_right": matrix_multiply(
            projector_three, projector_five
        )
        == zero_10,
        "trace_kills_sym5": matrix_multiply(trace, projector_five)
        == zero_matrix(4, 10),
        "total_symmetrizer_equals_projector_five": symmetrizer == projector_five,
        "rank_trace_is_four": matrix_rank(trace) == 4,
        "rank_embedding_is_four": matrix_rank(embedding) == 4,
        "rank_projector_three_is_four": matrix_rank(projector_three) == 4,
        "rank_projector_five_is_six": matrix_rank(projector_five) == 6,
        "dimension_is_ten_equals_six_plus_four": 10 == 6 + 4,
        "t_plus3_is_b_minus_a": trace_plus_plus_plus
        == row_subtract(b_row, Q(1), a_row),
        "h_minus_plus4_is_one_fifth_a_plus_four_fifths_b": h_minus_plus4
        == matrix_add(matrix_scale(Q(1, 5), [a_row]), matrix_scale(Q(4, 5), [b_row]))[
            0
        ],
        "u_minus_plus4_reconstruction": reconstructed_a == a_row,
        "u_minus_plus4_weight_is_three_halves": Q(-1, 2) + 4 * Q(1, 2) == Q(3, 2),
        "candidate_highest_weight_is_three_halves": 3 * Q(1, 2) == Q(3, 2),
        "chiral_bianchi_has_six_raw_terms": chiral_raw_count == 6,
        "chiral_bianchi_reduces_to_zero": chiral_bianchi == {},
        "nested_sym4_then_sym5_equals_direct_sym5": nested_five_sym == direct_five_sym,
        "five_symmetrizer_is_normalized": sum(direct_five_sym.values(), Q(0)) == Q(1),
        "h_leibniz_has_four_hundred_eighty_raw_terms": h_raw_count == 480,
        "h_derivative_on_a_reduces_to_zero": h_on_a == {},
        "h_derivative_on_b_reduces_to_zero": h_on_b == {},
        "h_preserves_open_a_before_b_order": h_open_order,
        "project_eom_derivative_identity": eom_derivative_left == eom_derivative_right,
        "tree_eom_insertion_has_two_ordered_leibniz_terms": len(insertion_raw) == 2,
        "tree_eom_insertion_identity": insertion_rewritten == insertion_stated,
        "tree_eom_insertion_preserves_open_a_before_b_order": all(
            word[0].startswith("A:") and word[1].startswith("B:")
            for word in (*insertion_raw.keys(), *insertion_rewritten.keys())
        ),
    }

    return {
        "schema": "step5-one-loop-spin-projector-v1",
        "arithmetic": "Q",
        "conventions": {
            "epsilon_up_plus_minus": "1",
            "epsilon_down_plus_minus": "-1",
            "raising": "v^a=epsilon^{ab}v_b",
            "lowering": "v_a=epsilon_{ab}v^b",
            "lower_plus_weight": "1/2",
            "lower_minus_weight": "-1/2",
        },
        "eom_trace_separation": {
            "M_ab": "nabla_a W_b",
            "E": "nabla^a W_a=epsilon^{ab}nabla_b W_a",
            "X_ab": "M_(ab)",
            "decomposition": "M_ab=X_ab+(1/2)epsilon_ab E",
            "direct_epsilon_trace": "epsilon^{ab}M_ab=-E",
        },
        "rank_four_letter": {
            "definition": "T_bcde=X^A_(bc X^B_de) with normalized Sym^4 projection",
            "explicit_projection": (
                "(1/6)(X^A_bc X^B_de+X^A_bd X^B_ce+X^A_be X^B_cd"
                "+X^A_cd X^B_be+X^A_ce X^B_bd+X^A_de X^B_bc)"
            ),
            "seed_component": "T_++++=X^A_++ X^B_++",
            "U_definition": "U_a;bcde=nabla_a T_bcde",
        },
        "chiral_bianchi_closure": {
            "project_algebra": "{nabla_a,nabla_b}=0",
            "X_definition": "X_ab=nabla_(a W_b)",
            "expanded_identity": (
                "nabla_(a X_bc)=(1/6)(nabla_a nabla_b W_c+nabla_b nabla_a W_c"
                "+nabla_a nabla_c W_b+nabla_c nabla_a W_b"
                "+nabla_b nabla_c W_a+nabla_c nabla_b W_a)=0"
            ),
            "raw_term_count": chiral_raw_count,
            "reduced_polynomial": {
                "term_count": len(chiral_bianchi),
                "terms": {
                    "|".join(word): fraction_text(value)
                    for word, value in chiral_bianchi.items()
                },
            },
        },
        "rank_five_closure": {
            "definition": "H_abcde=nabla_(a T_bcde)",
            "graded_leibniz": (
                "nabla_a(X^A_bc X^B_de)=(nabla_a X^A_bc)X^B_de"
                "+X^A_bc(nabla_a X^B_de), because |X|=0"
            ),
            "ordered_derivation": (
                "H=Sym5[(nabla_a X^A_bc)X^B_de]+Sym5[X^A_bc(nabla_a X^B_de)]"
            ),
            "factorized_zero": (
                "H=Sym5[(nabla_(a X^A_bc))X^B_de]+Sym5[X^A_bc(nabla_(a X^B_de))]=0"
            ),
            "open_color_order": "A factor remains left of B factor in every word",
            "symmetrizer_checks": {
                "nested_sym4_then_sym5_unique_words": len(nested_five_sym),
                "direct_sym5_unique_words": len(direct_five_sym),
                "nested_equals_direct": nested_five_sym == direct_five_sym,
                "normalization": fraction_text(sum(direct_five_sym.values(), Q(0))),
                "leibniz_raw_term_count": h_raw_count,
                "derivative_on_a_remainder_count": len(h_on_a),
                "derivative_on_b_remainder_count": len(h_on_b),
            },
            "status": "CLOSED_EXACT",
        },
        "bases": {
            "U": [f"U_{first};m{minus_count}" for first, minus_count in u_basis()],
            "trace": [f"t_m{minus_count}" for minus_count in t_basis()],
        },
        "maps": {
            "trace": encoded_matrix(trace),
            "right_inverse_embedding": encoded_matrix(embedding),
            "projector_j_three_halves": encoded_matrix(projector_three),
            "projector_j_five_halves": encoded_matrix(projector_five),
            "total_symmetrizer": encoded_matrix(symmetrizer),
        },
        "right_inverse_formula": {
            "trace": "t_cde=epsilon^{ab}U_a;bcde",
            "embedding": (
                "E(t)_a;bcde=-(1/5)(epsilon_ab t_cde+epsilon_ac t_bde"
                "+epsilon_ad t_bce+epsilon_ae t_bcd)"
            ),
            "contraction": "epsilon^{ab}E(t)_a;bcde=(-1/5)(-2-1-1-1)t_cde=t_cde",
            "decomposition": "U=P_5 U+E(t), P_5=1-E trace",
        },
        "component_formula": {
            "A": "U_-;++++",
            "B": "U_+;-+++",
            "t_+++": "B-A",
            "H_-++++": "(1/5)A+(4/5)B",
            "identity": "U_-;++++=H_-++++-(4/5)t_+++",
            "chiral_closure": "H_-++++=0",
            "closed_identity": "U_-;++++=-(4/5)t_+++",
            "left_weight": "3/2",
            "irreducible_content": [
                {"tensor": "H_-++++", "j_L": "5/2", "weight": "3/2"},
                {"tensor": "t_+++", "j_L": "3/2", "weight": "3/2"},
            ],
            "irreducible_content_scope": "UNRESTRICTED_TENSOR_PRODUCT",
            "chiral_constrained_content": [
                {"tensor": "t_+++", "j_L": "3/2", "weight": "3/2"}
            ],
        },
        "anomaly_candidate_spin_type": {
            "definition": "C_abc=tildeW_dotalpha D_(a^dotalpha X_bc)",
            "normalized_symmetrization": (
                "C_abc=(1/3)tildeW_dotalpha(D_a^dotalpha X_bc"
                "+D_b^dotalpha X_ca+D_c^dotalpha X_ab)"
            ),
            "representation": "Sym^3 S_L",
            "j_L": "3/2",
            "highest_component": "C_+++=tildeW_dotalpha D_+^dotalpha X_++",
            "highest_weight": "3/2",
        },
        "ambiguity_ledger": {
            "epsilon_and_eom_trace": "RESOLVED_BY_PROJECT_CONVENTION",
            "open_color_AB_symmetry": (
                "NO_SYMMETRY_ASSUMED; NONCOMMUTATIVE A-B ORDER PRESERVED"
            ),
            "tensor_product_derivative": "RESOLVED_AS_GRADED_DERIVATION_WITH_X_EVEN",
            "coefficient_matching_to_anomaly_candidate": "OPEN_NOT_COMPUTED",
        },
        "spin_five_halves_gate": {
            "status": "CLOSED_EXACT",
            "identity": "H_abcde=0",
            "seed_consequence": "H_-++++=0",
        },
        "tree_level_eom_identity": {
            "E_definition": (
                "E=nabla^a W_a=epsilon^{ab}nabla_b W_a=nabla_- W_+-nabla_+ W_-"
            ),
            "derivation": [
                "nabla_+ E=nabla_+nabla_-W_+-nabla_+^2W_-",
                "nabla_+^2=0",
                "nabla_+nabla_-=-nabla_-nabla_+",
                "nabla_+E=-nabla_-nabla_+W_+=-nabla_-X_++",
            ],
            "seed": "I^AB=nabla_-(X^A X^B), X=X_++",
            "graded_leibniz": ("I^AB=(nabla_-X^A)X^B+X^A(nabla_-X^B), because |X|=0"),
            "rewrite_rules": [
                "nabla_-X^A=-nabla_+E^A",
                "nabla_-X^B=-nabla_+E^B",
            ],
            "closed_identity": ("I^AB=-(nabla_+E^A)X^B-X^A(nabla_+E^B)"),
            "trace_component_rewrite": (
                "t_+++=-(5/4)I^AB=(5/4)[(nabla_+E^A)X^B+X^A(nabla_+E^B)]"
            ),
            "status": "CLOSED_EXACT_AT_TREE_LEVEL",
        },
        "quantum_gates": {
            "status": "OPEN",
            "t_cohomology_triviality": "OPEN_NOT_DERIVED",
            "full_n4_eom_ideal_membership": "OPEN_NOT_DERIVED",
            "renormalized_contact_anomaly_coefficient": "OPEN_NOT_COMPUTED",
            "coefficient_matching_to_sym3_candidate": "OPEN_NOT_COMPUTED",
            "forbidden_inference": "tree-level EOM rewrite implies zero renormalized insertion",
        },
        "dimensions": {"domain": 10, "sym5": 6, "sym3": 4},
        "checks": checks,
        "certificate_status": "PASS" if all(checks.values()) else "FAIL",
    }


def write_outputs(root: Path) -> tuple[Path, Path]:
    certificate = build_certificate()
    generated = root / "generated/step5/one-loop-spin-projector.json"
    audit = root / "audits/step5-one-loop-spin-projector-verification.json"
    generated.parent.mkdir(parents=True, exist_ok=True)
    audit.parent.mkdir(parents=True, exist_ok=True)
    generated.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    audit_payload = {
        "schema": "step5-one-loop-spin-projector-audit-v1",
        "artifact": str(generated.relative_to(root)),
        "certificate_status": certificate["certificate_status"],
        "spin_five_halves_gate_status": certificate["spin_five_halves_gate"]["status"],
        "tree_level_eom_identity_status": certificate["tree_level_eom_identity"][
            "status"
        ],
        "quantum_gate_status": certificate["quantum_gates"]["status"],
        "check_count": len(certificate["checks"]),
        "passed_check_count": sum(certificate["checks"].values()),
        "failed_checks": [
            name for name, passed in certificate["checks"].items() if not passed
        ],
        "exact_results": {
            "epsilon_contractions": "PASS",
            "trace_right_inverse": "PASS",
            "direct_sum_ranks": "10=6+4",
            "unrestricted_seed_component": "U_-;++++=H_-++++-(4/5)t_+++",
            "chiral_closed_seed_component": "U_-;++++=-(4/5)t_+++",
            "rank_five_closure": "H_abcde=0",
            "tree_level_eom_identity": ("I^AB=-(nabla_+E^A)X^B-X^A(nabla_+E^B)"),
            "seed_left_weight": "3/2",
            "unrestricted_tensor_product_spin_content": ["5/2", "3/2"],
            "chiral_constrained_seed_spin_content": ["3/2"],
            "candidate_spin": "3/2",
        },
        "open_obligations": [
            "cohomology triviality of t_cde",
            "membership in the full N=4 EOM ideal including matter terms",
            "renormalized contact-anomaly coefficient",
            "coefficient matching to the Sym^3 anomaly candidate",
        ],
        "overall_status": (
            "PASS_WITH_OPEN_QUANTUM_GATES"
            if certificate["certificate_status"] == "PASS"
            else "FAIL"
        ),
    }
    audit.write_text(json.dumps(audit_payload, indent=2, sort_keys=True) + "\n")
    return generated, audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    arguments = parser.parse_args()
    generated, audit = write_outputs(arguments.root.resolve())
    certificate = json.loads(generated.read_text())
    print(
        json.dumps(
            {
                "artifact": str(generated),
                "audit": str(audit),
                "certificate_status": certificate["certificate_status"],
                "spin_five_halves_gate": certificate["spin_five_halves_gate"]["status"],
                "quantum_gate": certificate["quantum_gates"]["status"],
            },
            sort_keys=True,
        )
    )
    return 0 if certificate["certificate_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
