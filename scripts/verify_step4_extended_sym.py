#!/usr/bin/env python3
"""Exact coefficient checks for Step 4 extended super Yang--Mills.

The checker uses the Step-3A exact ring Q(i,sqrt(2)).  Internal-index
packaging checks are formal combinatorial identities; no floating point,
external CAS, textbook rule, or random sampling is used.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from fractions import Fraction

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
AUDIT_PATH = ROOT / "audits" / "step4-extended-sym-verification.json"


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


def matrix_zero():
    return ((ZERO, ZERO), (ZERO, ZERO))


def matrix_add(left, right):
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )


def matrix_equal(left, right) -> bool:
    return all(left[row][column] == right[row][column] for row in range(2) for column in range(2))


def square_zero(size: int):
    return tuple(tuple(ZERO for _ in range(size)) for _ in range(size))


def square_identity(size: int):
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def square_add(left, right):
    size = len(left)
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(size))
        for row in range(size)
    )


def square_scale(matrix, coefficient: Exact):
    size = len(matrix)
    return tuple(
        tuple(coefficient * matrix[row][column] for column in range(size))
        for row in range(size)
    )


def square_multiply(left, right):
    size = len(left)
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(size)),
                ZERO,
            )
            for column in range(size)
        )
        for row in range(size)
    )


def square_equal(left, right) -> bool:
    size = len(left)
    return all(
        left[row][column] == right[row][column]
        for row in range(size)
        for column in range(size)
    )


def square_trace(matrix):
    return sum((matrix[index][index] for index in range(len(matrix))), ZERO)


def epsilon3(i: int, j: int, k: int) -> int:
    if len({i, j, k}) < 3:
        return 0
    values = (i, j, k)
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def epsilon4(i: int, j: int, k: int, l: int) -> int:
    if len({i, j, k, l}) < 4:
        return 0
    values = (i, j, k, l)
    inversions = sum(
        values[left] > values[right]
        for left in range(4)
        for right in range(left + 1, 4)
    )
    return -1 if inversions % 2 else 1


def build_su4_rho_matrices():
    rho = [
        [[ZERO for _ in range(4)] for _ in range(4)]
        for _ in range(6)
    ]
    for r in range(3):
        real_slot = 2 * r
        imaginary_slot = real_slot + 1
        rho[real_slot][r][3] = ONE
        rho[real_slot][3][r] = -ONE
        rho[imaginary_slot][r][3] = I
        rho[imaginary_slot][3][r] = -I
        for s in range(3):
            for t in range(3):
                coefficient = epsilon3(s, t, r)
                if not coefficient:
                    continue
                value = Exact.rational(coefficient)
                rho[real_slot][s][t] = value
                rho[imaginary_slot][s][t] = MINUS_I * value

    rho_tuple = [tuple(tuple(row) for row in matrix) for matrix in rho]
    tilde = []
    for u in range(6):
        matrix = [[ZERO for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                value = ZERO
                for k in range(4):
                    for l in range(4):
                        sign = epsilon4(i, j, k, l)
                        if sign:
                            value = value + Exact.rational(Fraction(sign, 2)) * rho[u][k][l]
                matrix[i][j] = value
        tilde.append(tuple(tuple(row) for row in matrix))
    return rho_tuple, tilde


def check_su4_rho_identities():
    failures: list[str] = []
    checks: dict[str, bool] = {}
    rho, tilde = build_su4_rho_matrices()
    identity4 = square_identity(4)

    for u in range(6):
        for v in range(6):
            clifford = square_add(
                square_multiply(rho[u], tilde[v]),
                square_multiply(rho[v], tilde[u]),
            )
            expected = square_scale(
                identity4,
                Exact.rational(-2 if u == v else 0),
            )
            key = f"rho_clifford_{u}_{v}"
            checks[key] = square_equal(clifford, expected)
            if not checks[key]:
                failures.append(key)

            trace_value = square_trace(square_multiply(rho[u], tilde[v]))
            trace_expected = Exact.rational(-4 if u == v else 0)
            key = f"rho_trace_{u}_{v}"
            checks[key] = trace_value == trace_expected
            if not checks[key]:
                failures.append(key)

    for i, j, k, l in itertools.product(range(4), repeat=4):
        mixed = sum((tilde[u][i][j] * rho[u][k][l] for u in range(6)), ZERO)
        mixed_expected = Exact.rational(
            2 * ((1 if i == k and j == l else 0) - (1 if i == l and j == k else 0))
        )
        key = f"rho_mixed_complete_{i}_{j}_{k}_{l}"
        if mixed != mixed_expected:
            failures.append(key)

        chiral = sum((rho[u][i][j] * rho[u][k][l] for u in range(6)), ZERO)
        chiral_expected = Exact.rational(2 * epsilon4(i, j, k, l))
        key = f"rho_chiral_complete_{i}_{j}_{k}_{l}"
        if chiral != chiral_expected:
            failures.append(key)

    checks["mixed_completeness"] = not any(
        failure.startswith("rho_mixed_complete_") for failure in failures
    )
    checks["chiral_completeness"] = not any(
        failure.startswith("rho_chiral_complete_") for failure in failures
    )
    return failures, checks


def add_coefficient(expression: dict[tuple, int], key: tuple, coefficient: int) -> None:
    if coefficient == 0:
        return
    expression[key] = expression.get(key, 0) + coefficient
    if expression[key] == 0:
        del expression[key]


def scalar_product_key(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def canonical_cross(left: str, right: str) -> tuple[int, tuple[str, str] | None]:
    if left == right:
        return 0, None
    if left < right:
        return 1, (left, right)
    return -1, (right, left)


def canonical_cross_product(
    left: tuple[str, str], right: tuple[str, str]
) -> tuple[tuple[str, str], tuple[str, str]]:
    return tuple(sorted((left, right)))


def normalize_lie_pairing(a: str, b: str, c: str, d: str):
    sign_left, left = canonical_cross(a, b)
    sign_right, right = canonical_cross(c, d)
    if left is None or right is None:
        return 0, None
    return sign_left * sign_right, canonical_cross_product(left, right)


def matrix_rank_fraction(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [list(row) for row in rows]
    row = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next((index for index in range(row, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        pivot_value = matrix[row][column]
        matrix[row] = [entry / pivot_value for entry in matrix[row]]
        for index in range(len(matrix)):
            if index == row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                matrix[index][position] - factor * matrix[row][position]
                for position in range(columns)
            ]
        row += 1
        if row == len(matrix):
            break
    return row


def lie_equivalent_mod_jacobi(left: dict[tuple, int], right: dict[tuple, int]) -> bool:
    difference = dict(left)
    for key, coefficient in right.items():
        difference[key] = difference.get(key, 0) - coefficient
        if difference[key] == 0:
            del difference[key]
    multisets = {
        tuple(sorted(key[0] + key[1]))
        for key in set(left) | set(right)
    }
    for multiset in multisets:
        keys: set[tuple] = set()
        relations: list[dict[tuple, int]] = []
        for permutation in set(itertools.permutations(multiset)):
            a, b, c, d = permutation
            relation: dict[tuple, int] = {}
            # B(a,b;c,d)-B(a,c;b,d)+B(a,d;b,c)=0.
            for coefficient, arguments in (
                (1, (a, b, c, d)),
                (-1, (a, c, b, d)),
                (1, (a, d, b, c)),
            ):
                sign, key = normalize_lie_pairing(*arguments)
                if key is not None:
                    relation[key] = relation.get(key, 0) + coefficient * sign
                    keys.add(key)
            relation = {key: value for key, value in relation.items() if value}
            if relation:
                relations.append(relation)
        local_difference = {
            key: coefficient
            for key, coefficient in difference.items()
            if tuple(sorted(key[0] + key[1])) == multiset
        }
        keys.update(local_difference)
        ordered_keys = sorted(keys)
        relation_rows = [
            [Fraction(relation.get(key, 0)) for key in ordered_keys]
            for relation in relations
        ]
        difference_row = [Fraction(local_difference.get(key, 0)) for key in ordered_keys]
        if matrix_rank_fraction(relation_rows) != matrix_rank_fraction(relation_rows + [difference_row]):
            return False
    return True


def build_su4_scalars():
    varphi: list[list[tuple[int, str] | None]] = [[None for _ in range(4)] for _ in range(4)]
    tilde: list[list[tuple[int, str] | None]] = [[None for _ in range(4)] for _ in range(4)]
    for r in range(3):
        varphi[r][3] = (1, f"p{r}")
        varphi[3][r] = (-1, f"p{r}")
        tilde[r][3] = (1, f"t{r}")
        tilde[3][r] = (-1, f"t{r}")
    for r in range(3):
        for s in range(3):
            for t in range(3):
                coefficient = epsilon3(r, s, t)
                if coefficient:
                    varphi[r][s] = (coefficient, f"t{t}")
                    tilde[r][s] = (coefficient, f"p{t}")
    return varphi, tilde


def check_scalar_duality_and_norm():
    varphi, tilde = build_su4_scalars()
    norm: dict[tuple, int] = {}
    for i in range(4):
        for j in range(4):
            if varphi[i][j] is None or tilde[i][j] is None:
                continue
            c1, s1 = tilde[i][j]
            c2, s2 = varphi[i][j]
            add_coefficient(norm, scalar_product_key(s1, s2), c1 * c2)
    expected = {(f"p{r}", f"t{r}"): 4 for r in range(3)}
    return norm, expected


def canonical_spinor_bilinear(
    first: tuple[str, str], second: tuple[str, str]
) -> tuple[tuple[str, str], tuple[str, str]]:
    # A contracted bilinear of two Grassmann-odd Weyl spinors is symmetric
    # under simultaneous interchange of the two complete field slots.
    return tuple(sorted((first, second)))


def add_uncontracted_yukawa_term(
    expression: dict[tuple, int],
    coefficient: int,
    scalar: str,
    first_species: str,
    first_color: str,
    second_species: str,
    second_color: str,
) -> None:
    key = (
        scalar,
        canonical_spinor_bilinear(
            (first_species, first_color),
            (second_species, second_color),
        ),
    )
    add_coefficient(expression, key, coefficient)


def add_contracted_yukawa_term(
    expression: dict[tuple, int],
    coefficient: int,
    scalar: str,
    first_species: str,
    second_species: str,
) -> None:
    # c_{ABC} changes sign when the B,C fermion color slots are exchanged.
    if first_species <= second_species:
        sign = 1
        pair = (first_species, second_species)
    else:
        sign = -1
        pair = (second_species, first_species)
    add_coefficient(expression, (scalar, pair), sign * coefficient)


def check_su4_yukawa():
    _, tilde = build_su4_scalars()
    fermions = ("psi0", "psi1", "psi2", "lambda")

    uncontracted_actual: dict[tuple, int] = {}
    for i in range(4):
        for j in range(4):
            if tilde[i][j] is None:
                continue
            scalar_coefficient, scalar = tilde[i][j]
            add_uncontracted_yukawa_term(
                uncontracted_actual,
                scalar_coefficient,
                scalar,
                fermions[i],
                "B",
                fermions[j],
                "C",
            )

    uncontracted_expected: dict[tuple, int] = {}
    premature_reduction: dict[tuple, int] = {}
    for r in range(3):
        add_uncontracted_yukawa_term(
            uncontracted_expected, 1, f"t{r}", f"psi{r}", "B", "lambda", "C"
        )
        add_uncontracted_yukawa_term(
            uncontracted_expected, -1, f"t{r}", "lambda", "B", f"psi{r}", "C"
        )
        add_uncontracted_yukawa_term(
            premature_reduction, 2, f"t{r}", f"psi{r}", "B", "lambda", "C"
        )
    for r, s, t in itertools.product(range(3), repeat=3):
        coefficient = epsilon3(r, s, t)
        if not coefficient:
            continue
        for expression in (uncontracted_expected, premature_reduction):
            add_uncontracted_yukawa_term(
                expression,
                coefficient,
                f"p{t}",
                f"psi{r}",
                "B",
                f"psi{s}",
                "C",
            )

    contracted_actual: dict[tuple, int] = {}
    for (scalar, pair), coefficient in uncontracted_actual.items():
        (first_species, first_color), (second_species, second_color) = pair
        if (first_color, second_color) == ("B", "C"):
            color_sign = 1
        elif (first_color, second_color) == ("C", "B"):
            color_sign = -1
        else:
            raise AssertionError("unexpected Yukawa color slots")
        add_contracted_yukawa_term(
            contracted_actual,
            color_sign * coefficient,
            scalar,
            first_species,
            second_species,
        )

    contracted_expected: dict[tuple, int] = {}
    for r in range(3):
        add_contracted_yukawa_term(
            contracted_expected, 2, f"t{r}", f"psi{r}", "lambda"
        )
    for r, s, t in itertools.product(range(3), repeat=3):
        coefficient = epsilon3(r, s, t)
        if coefficient:
            add_contracted_yukawa_term(
                contracted_expected,
                coefficient,
                f"p{t}",
                f"psi{r}",
                f"psi{s}",
            )

    return {
        "uncontracted_actual": uncontracted_actual,
        "uncontracted_expected": uncontracted_expected,
        "premature_uncontracted_reduction": premature_reduction,
        "contracted_actual": contracted_actual,
        "contracted_expected": contracted_expected,
    }


def check_su4_quartic():
    varphi, tilde = build_su4_scalars()
    lhs: dict[tuple, int] = {}
    for i in range(4):
        for j in range(4):
            if varphi[i][j] is None:
                continue
            c1, s1 = varphi[i][j]
            for k in range(4):
                for l in range(4):
                    if varphi[k][l] is None:
                        continue
                    c2, s2 = varphi[k][l]
                    sign_left, cross_left = canonical_cross(s1, s2)
                    if cross_left is None:
                        continue
                    if tilde[i][j] is None or tilde[k][l] is None:
                        continue
                    d1, t1 = tilde[i][j]
                    d2, t2 = tilde[k][l]
                    sign_right, cross_right = canonical_cross(t1, t2)
                    if cross_right is None:
                        continue
                    key = canonical_cross_product(cross_left, cross_right)
                    add_coefficient(lhs, key, c1 * c2 * d1 * d2 * sign_left * sign_right)

    rhs: dict[tuple, int] = {}
    c0_crosses = []
    for r in range(3):
        sign, label = canonical_cross(f"p{r}", f"t{r}")
        assert label is not None
        c0_crosses.append((sign, label))
    for sign_left, left in c0_crosses:
        for sign_right, right in c0_crosses:
            add_coefficient(
                rhs,
                canonical_cross_product(left, right),
                -8 * sign_left * sign_right,
            )
    for r in range(3):
        for s in range(r + 1, 3):
            sign_left, left = canonical_cross(f"p{r}", f"p{s}")
            sign_right, right = canonical_cross(f"t{r}", f"t{s}")
            assert left is not None and right is not None
            add_coefficient(
                rhs,
                canonical_cross_product(left, right),
                32 * sign_left * sign_right,
            )
    return lhs, rhs


def check_su4_quartic_census():
    raw_slots = list(itertools.product(range(4), repeat=4))
    diagonal_zero_slots = [
        slot for slot in raw_slots if slot[0] == slot[1] or slot[2] == slot[3]
    ]
    off_diagonal_slots = [
        slot for slot in raw_slots if slot[0] != slot[1] and slot[2] != slot[3]
    ]

    def reversal_orbit(slot):
        i, j, k, l = slot
        return frozenset(
            (
                (i, j, k, l),
                (j, i, k, l),
                (i, j, l, k),
                (j, i, l, k),
            )
        )

    reversal_orbits = {reversal_orbit(slot) for slot in off_diagonal_slots}
    orbit_size_histogram: dict[int, int] = {}
    for orbit in reversal_orbits:
        orbit_size_histogram[len(orbit)] = orbit_size_histogram.get(len(orbit), 0) + 1

    quartic_lhs, _ = check_su4_quartic()
    orbit_reduction: dict[tuple, int] = {}
    for r in range(3):
        for s in range(3):
            for arguments in (
                (f"p{r}", f"p{s}", f"t{r}", f"t{s}"),
                (f"p{r}", f"t{s}", f"t{r}", f"p{s}"),
            ):
                sign, key = normalize_lie_pairing(*arguments)
                if key is not None:
                    add_coefficient(orbit_reduction, key, 8 * sign)

    canonical_actual: dict[str, int] = {}
    for r in range(3):
        for s in range(3):
            if r != s:
                label = f"A{min(r, s) + 1}{max(r, s) + 1}"
                canonical_actual[label] = canonical_actual.get(label, 0) + 16
            label = f"C{min(r, s) + 1}{max(r, s) + 1}"
            canonical_actual[label] = canonical_actual.get(label, 0) - 8

    canonical_expected = {
        "A12": 32,
        "A13": 32,
        "A23": 32,
        "C11": -8,
        "C22": -8,
        "C33": -8,
        "C12": -16,
        "C13": -16,
        "C23": -16,
    }
    checks = {
        "raw_slot_count": len(raw_slots) == 256,
        "diagonal_zero_slot_count": len(diagonal_zero_slots) == 112,
        "off_diagonal_slot_count": len(off_diagonal_slots) == 144,
        "reversal_orbit_count": len(reversal_orbits) == 36,
        "reversal_orbit_sizes": orbit_size_histogram == {4: 36},
        "orbit_reduction_exact": quartic_lhs == orbit_reduction,
        "canonical_dictionary": canonical_actual == canonical_expected,
    }
    return checks, {
        "raw_slots": len(raw_slots),
        "diagonal_zero_slots": len(diagonal_zero_slots),
        "off_diagonal_slots": len(off_diagonal_slots),
        "reversal_orbits": len(reversal_orbits),
        "orbit_size_histogram": orbit_size_histogram,
        "orbit_reduction": serialize_formal(orbit_reduction),
        "canonical_actual": canonical_actual,
        "canonical_expected": canonical_expected,
    }


def check_su2_auxiliary():
    # Formal coefficients in 1/4 Y^{ij}Y_{ij}.
    expression = {("F", "tF"): 1, ("H", "H"): Fraction(1, 2)}
    expected = {("F", "tF"): 1, ("H", "H"): Fraction(1, 2)}
    return expression, expected


def add_fraction(
    expression: dict[tuple, Fraction], key: tuple, coefficient: Fraction | int
) -> None:
    value = Fraction(coefficient)
    expression[key] = expression.get(key, Fraction(0)) + value
    if expression[key] == 0:
        del expression[key]


def free_boson_pair(
    first_field: str,
    first_color: str,
    second_field: str,
    second_color: str,
) -> tuple[tuple[str, str], tuple[str, str]]:
    return tuple(sorted(((first_field, first_color), (second_field, second_color))))


def add_free_boson_pair(
    expression: dict[tuple, Fraction],
    coefficient: Fraction | int,
    first_field: str,
    first_color: str,
    second_field: str,
    second_color: str,
) -> None:
    add_fraction(
        expression,
        free_boson_pair(first_field, first_color, second_field, second_color),
        coefficient,
    )


def contract_symmetric_kappa(
    expression: dict[tuple, Fraction]
) -> dict[tuple[str, str], Fraction]:
    contracted: dict[tuple[str, str], Fraction] = {}
    for pair, coefficient in expression.items():
        fields = tuple(sorted((pair[0][0], pair[1][0])))
        add_fraction(contracted, fields, coefficient)
    return contracted


def check_n2_contracted_auxiliary_boundary():
    original: dict[tuple, Fraction] = {}
    add_free_boson_pair(original, 1, "tildeF", "A", "F", "B")
    add_free_boson_pair(original, Fraction(1, 2), "D", "A", "D", "B")
    add_free_boson_pair(original, 1, "D", "A", "mu", "B")

    symmetrized: dict[tuple, Fraction] = {}
    add_free_boson_pair(symmetrized, 1, "tildeF", "A", "F", "B")
    add_free_boson_pair(symmetrized, Fraction(1, 2), "D", "A", "D", "B")
    add_free_boson_pair(symmetrized, Fraction(1, 2), "D", "A", "mu", "B")
    add_free_boson_pair(symmetrized, Fraction(1, 2), "mu", "A", "D", "B")

    completed_square: dict[tuple, Fraction] = {}
    add_free_boson_pair(completed_square, 1, "tildeF", "A", "F", "B")
    add_free_boson_pair(completed_square, Fraction(1, 2), "D", "A", "D", "B")
    add_free_boson_pair(completed_square, Fraction(1, 2), "D", "A", "mu", "B")
    add_free_boson_pair(completed_square, Fraction(1, 2), "mu", "A", "D", "B")

    y_free: dict[tuple, Fraction] = {}
    add_free_boson_pair(y_free, Fraction(1, 2), "tildeF", "A", "F", "B")
    add_free_boson_pair(y_free, Fraction(1, 2), "F", "A", "tildeF", "B")
    add_free_boson_pair(y_free, Fraction(1, 2), "H", "A", "H", "B")

    y_short: dict[tuple, Fraction] = {}
    add_free_boson_pair(y_short, 1, "tildeF", "A", "F", "B")
    add_free_boson_pair(y_short, Fraction(1, 2), "H", "A", "H", "B")

    checks = {
        "completion_symmetrized_free_index": symmetrized == completed_square,
        "completion_not_free_index_identity": original != symmetrized,
        "completion_kappa_contracted": (
            contract_symmetric_kappa(original)
            == contract_symmetric_kappa(symmetrized)
        ),
        "triplet_not_free_index_short_identity": y_free != y_short,
        "triplet_kappa_contracted": (
            contract_symmetric_kappa(y_free)
            == contract_symmetric_kappa(y_short)
        ),
    }
    return checks, {
        "completion_original": original,
        "completion_symmetrized": symmetrized,
        "triplet_free_index": y_free,
        "triplet_short_ordered": y_short,
    }


def add_exact(expression: dict[tuple, Exact], key: tuple, coefficient: Exact) -> None:
    expression[key] = expression.get(key, ZERO) + coefficient
    if expression[key].is_zero():
        del expression[key]


def exact_inner_key(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def exact_inner_linear(
    left: dict[str, Exact], right: dict[str, Exact]
) -> dict[tuple[str, str], Exact]:
    expression: dict[tuple[str, str], Exact] = {}
    for left_field, left_coefficient in left.items():
        for right_field, right_coefficient in right.items():
            add_exact(
                expression,
                exact_inner_key(left_field, right_field),
                left_coefficient * right_coefficient,
            )
    return expression


def merge_exact(
    target: dict[tuple, Exact],
    source: dict[tuple, Exact],
    scale: Exact = ONE,
) -> None:
    for key, coefficient in source.items():
        add_exact(target, key, scale * coefficient)


def check_n4_auxiliary_square():
    original: dict[tuple, Exact] = {}
    add_exact(original, exact_inner_key("D", "D"), HALF)
    add_exact(original, exact_inner_key("D", "C0"), I)
    completed: dict[tuple, Exact] = {}
    merge_exact(
        completed,
        exact_inner_linear({"D": ONE, "C0": I}, {"D": ONE, "C0": I}),
        HALF,
    )
    add_exact(completed, exact_inner_key("C0", "C0"), HALF)

    for r in range(3):
        f = f"F{r}"
        tf = f"tildeF{r}"
        q = f"Q{r}"
        tq = f"tildeQ{r}"
        add_exact(original, exact_inner_key(tf, f), ONE)
        add_exact(original, exact_inner_key(f, q), MINUS_ONE)
        add_exact(original, exact_inner_key(tf, tq), MINUS_ONE)
        merge_exact(
            completed,
            exact_inner_linear(
                {tf: ONE, q: MINUS_ONE},
                {f: ONE, tq: MINUS_ONE},
            ),
        )
        add_exact(completed, exact_inner_key(q, tq), MINUS_ONE)

    q_pairing_actual: dict[tuple, Fraction] = {}
    for r, s, t, u, v in itertools.product(range(3), repeat=5):
        left_epsilon = epsilon3(r, s, t)
        right_epsilon = epsilon3(r, u, v)
        if not left_epsilon or not right_epsilon:
            continue
        sign, key = normalize_lie_pairing(f"p{s}", f"p{t}", f"t{u}", f"t{v}")
        if key is not None:
            add_fraction(
                q_pairing_actual,
                key,
                Fraction(left_epsilon * right_epsilon * sign, 2),
            )

    q_pairing_expected: dict[tuple, Fraction] = {}
    for s, t in ((1, 2), (2, 0), (0, 1)):
        sign, key = normalize_lie_pairing(f"p{s}", f"p{t}", f"t{s}", f"t{t}")
        assert key is not None
        add_fraction(q_pairing_expected, key, 2 * sign)

    checks = {
        "complete_square_expansion": original == completed,
        "q_pairing_expansion": q_pairing_actual == q_pairing_expected,
    }
    return checks, {
        "original": original,
        "completed": completed,
        "q_pairing_actual": q_pairing_actual,
        "q_pairing_expected": q_pairing_expected,
    }


def check_n2_current_expansion(euclidean: bool):
    epsilon_lower = ((0, -1), (1, 0))
    chi = (("psi", ONE), ("lambda", -ONE))
    bar_chi = (("tildepsi", ONE), ("tildelambda", -ONE))
    y = (
        (
            {"F": -SQRT_TWO},
            {"H": I},
        ),
        (
            {"H": I},
            {"tildeF": -SQRT_TWO},
        ),
    )
    actual: dict[tuple, Exact] = {}
    for i in range(2):
        physical_sign = ONE if i == 0 else -ONE
        current = "manifest" if i == 0 else "hidden"
        chi_label, chi_sign = chi[i]
        add_exact(
            actual,
            (current, "Dtildephi", chi_label),
            physical_sign * (-SQRT_TWO) * chi_sign,
        )
        for j in range(2):
            bar_label, bar_sign = bar_chi[j]
            epsilon = Exact.rational(epsilon_lower[i][j])
            f_coefficient = epsilon if euclidean else MINUS_I * epsilon
            add_exact(
                actual,
                (current, "Fmunu", bar_label),
                physical_sign * f_coefficient * bar_sign,
            )
            for auxiliary, coefficient in y[i][j].items():
                y_coefficient = coefficient if euclidean else I * coefficient
                add_exact(
                    actual,
                    (current, auxiliary, bar_label),
                    physical_sign * y_coefficient * bar_sign,
                )
            mu_coefficient = I * epsilon if euclidean else -epsilon
            add_exact(
                actual,
                (current, "mu", bar_label),
                physical_sign * mu_coefficient * bar_sign,
            )

    if euclidean:
        expected = {
            ("manifest", "Fmunu", "tildelambda"): ONE,
            ("manifest", "Dtildephi", "psi"): -SQRT_TWO,
            ("manifest", "F", "tildepsi"): -SQRT_TWO,
            ("manifest", "H", "tildelambda"): -I,
            ("manifest", "mu", "tildelambda"): I,
            ("hidden", "Fmunu", "tildepsi"): -ONE,
            ("hidden", "Dtildephi", "lambda"): -SQRT_TWO,
            ("hidden", "H", "tildepsi"): -I,
            ("hidden", "mu", "tildepsi"): -I,
            ("hidden", "tildeF", "tildelambda"): -SQRT_TWO,
        }
    else:
        expected = {
            ("manifest", "Fmunu", "tildelambda"): -I,
            ("manifest", "Dtildephi", "psi"): -SQRT_TWO,
            ("manifest", "F", "tildepsi"): MINUS_I * SQRT_TWO,
            ("manifest", "H", "tildelambda"): ONE,
            ("manifest", "mu", "tildelambda"): -ONE,
            ("hidden", "Fmunu", "tildepsi"): I,
            ("hidden", "Dtildephi", "lambda"): -SQRT_TWO,
            ("hidden", "H", "tildepsi"): ONE,
            ("hidden", "mu", "tildepsi"): ONE,
            ("hidden", "tildeF", "tildelambda"): MINUS_I * SQRT_TWO,
        }
    return actual, expected


def epsilon_lorentz(i: int, j: int, k: int, l: int) -> int:
    return epsilon4(i, j, k, l)


def check_sigma_triple_identity():
    failures: list[str] = []
    metric = (-1, 1, 1, 1)
    for rho, sigma, mu in itertools.product(range(4), repeat=3):
        lhs = matrix_multiply(SIGMA_MUNU_L[rho][sigma], SIGMA_L[mu])
        rhs = matrix_zero()
        if rho == mu:
            rhs = matrix_add(rhs, matrix_scale(SIGMA_L[sigma], Exact.rational(metric[rho])))
        if sigma == mu:
            rhs = matrix_add(rhs, matrix_scale(SIGMA_L[rho], Exact.rational(-metric[sigma])))
        for nu in range(4):
            epsilon = epsilon_lorentz(rho, sigma, mu, nu)
            if not epsilon:
                continue
            sigma_lower = matrix_scale(SIGMA_L[nu], Exact.rational(metric[nu]))
            rhs = matrix_add(rhs, matrix_scale(sigma_lower, MINUS_I * Exact.rational(epsilon)))
        rhs = matrix_scale(rhs, HALF)
        if not matrix_equal(lhs, rhs):
            failures.append(f"sigma_triple_{rho}_{sigma}_{mu}")
    return failures


def check_bar_sigma_triple_identity():
    failures: list[str] = []
    metric = (-1, 1, 1, 1)
    for rho, sigma, mu in itertools.product(range(4), repeat=3):
        lhs = matrix_multiply(BAR_SIGMA_MUNU_L[rho][sigma], BAR_SIGMA_L[mu])
        rhs = matrix_zero()
        if rho == mu:
            rhs = matrix_add(
                rhs,
                matrix_scale(BAR_SIGMA_L[sigma], Exact.rational(metric[rho])),
            )
        if sigma == mu:
            rhs = matrix_add(
                rhs,
                matrix_scale(BAR_SIGMA_L[rho], Exact.rational(-metric[sigma])),
            )
        for nu in range(4):
            epsilon = epsilon_lorentz(rho, sigma, mu, nu)
            if not epsilon:
                continue
            bar_sigma_lower = matrix_scale(
                BAR_SIGMA_L[nu],
                Exact.rational(metric[nu]),
            )
            rhs = matrix_add(
                rhs,
                matrix_scale(bar_sigma_lower, I * Exact.rational(epsilon)),
            )
        rhs = matrix_scale(rhs, HALF)
        if not matrix_equal(lhs, rhs):
            failures.append(f"bar_sigma_triple_{rho}_{sigma}_{mu}")
    return failures


def exterior_multiply(left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int]):
    result: dict[tuple[int, ...], int] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            inversions = sum(
                left_index > right_index
                for left_index in left_monomial
                for right_index in right_monomial
            )
            monomial = tuple(sorted(left_monomial + right_monomial))
            coefficient = left_coefficient * right_coefficient
            if inversions % 2:
                coefficient = -coefficient
            result[monomial] = result.get(monomial, 0) + coefficient
            if result[monomial] == 0:
                del result[monomial]
    return result


def exterior_add(*expressions: dict[tuple[int, ...], int]):
    result: dict[tuple[int, ...], int] = {}
    for expression in expressions:
        for monomial, coefficient in expression.items():
            result[monomial] = result.get(monomial, 0) + coefficient
            if result[monomial] == 0:
                del result[monomial]
    return result


def check_two_spinor_schouten():
    # lower components: chi=(0,1), xi=(2,3), zeta=(4,5).
    spinors = {
        "chi": ({(0,): 1}, {(1,): 1}),
        "xi": ({(2,): 1}, {(3,): 1}),
        "zeta": ({(4,): 1}, {(5,): 1}),
    }
    epsilon_upper = ((0, 1), (-1, 0))

    def contract(left: str, right: str):
        terms = []
        for upper in range(2):
            for lower in range(2):
                coefficient = epsilon_upper[upper][lower]
                if not coefficient:
                    continue
                product = exterior_multiply(
                    spinors[left][lower],
                    spinors[right][upper],
                )
                terms.append(
                    {monomial: coefficient * value for monomial, value in product.items()}
                )
        return exterior_add(*terms)

    failures = []
    for component in range(2):
        expression = exterior_add(
            exterior_multiply(spinors["chi"][component], contract("xi", "zeta")),
            exterior_multiply(spinors["xi"][component], contract("zeta", "chi")),
            exterior_multiply(spinors["zeta"][component], contract("chi", "xi")),
        )
        if expression:
            failures.append(f"two_spinor_schouten_{component}")
    return failures


def check_n4_divergence_wick_coefficients():
    # Each tuple is (Lorentz coefficient, Wick factor inside the term,
    # outer divergence factor, Euclidean coefficient).
    left_terms = {
        "gauge_eom": (MINUS_I, MINUS_I, MINUS_ONE, ONE),
        "scalar_eom": (SQRT_TWO, MINUS_ONE, MINUS_ONE, SQRT_TWO),
        "dual_scalar_eom": (SQRT_TWO * HALF, MINUS_ONE, MINUS_ONE, SQRT_TWO * HALF),
        "sigma_f_fermion_eom": (ONE, MINUS_ONE, MINUS_ONE, ONE),
        "M_fermion_eom": (ONE, ONE, MINUS_ONE, MINUS_ONE),
        "derivative_fermion_eom": (MINUS_I * SQRT_TWO, I, MINUS_ONE, -SQRT_TWO),
    }
    conjugate_terms = {
        "gauge_eom": (MINUS_I, MINUS_I, MINUS_ONE, ONE),
        "scalar_eom": (SQRT_TWO, MINUS_ONE, MINUS_ONE, SQRT_TWO),
        "dual_scalar_eom": (SQRT_TWO * HALF, MINUS_ONE, MINUS_ONE, SQRT_TWO * HALF),
        "bar_sigma_f_fermion_eom": (MINUS_ONE, MINUS_ONE, MINUS_ONE, MINUS_ONE),
        "M_fermion_eom": (MINUS_ONE, ONE, MINUS_ONE, ONE),
        "derivative_fermion_eom": (MINUS_I * SQRT_TWO, I, MINUS_ONE, -SQRT_TWO),
    }
    failures: list[str] = []
    checks: dict[str, bool] = {}
    for family, terms in (("left", left_terms), ("conjugate", conjugate_terms)):
        for term, (lorentz, wick, outer, expected) in terms.items():
            actual = lorentz * wick * outer
            key = f"{family}_{term}"
            checks[key] = actual == expected
            if not checks[key]:
                failures.append(key)
    return failures, checks


def check_n4_fermion_closure_eom_reduction():
    """Check every coefficient pair in (4C.55e)--(4C.57).

    A pair is (coefficient of the covariant derivative term,
    coefficient of the scalar--fermion term).  The left Euler operator
    has pair (-i,sqrt(2)); the right Euler operator has
    (i,sqrt(2)).
    """

    left_euler = (MINUS_I, SQRT_TWO)
    right_euler = (I, SQRT_TWO)

    def scale(pair, coefficient):
        return (coefficient * pair[0], coefficient * pair[1])

    direct_left = {
        "A": (TWO * I, -TWO * SQRT_TWO),
        "A_spinor": (I, -SQRT_TWO),
        "epsilon_barA": (I, -SQRT_TWO),
        "X": (MINUS_I, -SQRT_TWO),
        "T": (TWO * I, TWO * SQRT_TWO),
    }
    eom_left = {
        "A": scale(left_euler, Exact.rational(-2)),
        "A_spinor": scale(left_euler, MINUS_ONE),
        "epsilon_barA": scale(left_euler, MINUS_ONE),
        "X": scale(right_euler, MINUS_ONE),
        "T": scale(right_euler, TWO),
    }

    direct_right = {
        "barA": (-TWO * I, -TWO * SQRT_TWO),
        "barA_spinor": (I, SQRT_TWO),
        "epsilon_A": (MINUS_I, -SQRT_TWO),
        "barX": (I, -SQRT_TWO),
        "barT": (-TWO * I, TWO * SQRT_TWO),
    }
    eom_right = {
        "barA": scale(right_euler, Exact.rational(-2)),
        "barA_spinor": scale(right_euler, ONE),
        "epsilon_A": scale(right_euler, MINUS_ONE),
        "barX": scale(left_euler, MINUS_ONE),
        "barT": scale(left_euler, TWO),
    }

    failures = []
    checks = {}
    for chirality, direct, reduced in (
        ("left", direct_left, eom_left),
        ("right", direct_right, eom_right),
    ):
        for tensor in direct:
            key = f"{chirality}_{tensor}"
            checks[key] = direct[tensor] == reduced[tensor]
            if not checks[key]:
                failures.append(f"n4_fermion_closure_{key}")
    return failures, checks


def check_wick_sigma_f():
    # Euclidean indices 0,1,2,3 mean 1,2,3,4.
    failures = []
    coefficients = {}
    for left in range(4):
        for right in range(left + 1, 4):
            direct = matrix_scale(SIGMA_MN_E[left][right], TWO)
            if right == 3:
                spatial = left
                # F^L_{0i}=iF^E_{4i}=-iF^E_{i4}.
                wick = matrix_scale(SIGMA_MUNU_L[0][spatial + 1], MINUS_I * TWO)
            else:
                wick = matrix_scale(SIGMA_MUNU_L[left + 1][right + 1], TWO)
            expected = matrix_scale(direct, Exact.rational(-1))
            ok = matrix_equal(wick, expected)
            coefficients[f"{left}{right}"] = ok
            if not ok:
                failures.append(f"wick_sigma_f_{left}_{right}")
    return failures, coefficients


def check_wick_sigma_d():
    failures = []
    coefficients = {}
    for euclidean_index in range(4):
        if euclidean_index == 3:
            wick = matrix_scale(SIGMA_L[0], I)
        else:
            wick = SIGMA_L[euclidean_index + 1]
        expected = matrix_scale(SIGMA_E[euclidean_index], I)
        ok = matrix_equal(wick, expected)
        coefficients[str(euclidean_index)] = ok
        if not ok:
            failures.append(f"wick_sigma_d_{euclidean_index}")
    return failures, coefficients


def check_sigma_lorentz_action():
    failures = []
    metric = (-1, 1, 1, 1)
    for mu in range(4):
        for nu in range(4):
            actual = matrix_add(
                matrix_multiply(SIGMA_L[mu], BAR_SIGMA_L[nu]),
                matrix_multiply(SIGMA_L[nu], BAR_SIGMA_L[mu]),
            )
            expected = matrix_scale(
                ((ONE, ZERO), (ZERO, ONE)),
                Exact.rational(-2 * (metric[mu] if mu == nu else 0)),
            )
            if not matrix_equal(actual, expected):
                failures.append(f"lorentz_clifford_{mu}_{nu}")
    return failures


def serialize_formal(expression: dict[tuple, int | Fraction]):
    return {repr(key): str(value) for key, value in sorted(expression.items(), key=lambda item: repr(item[0]))}


def serialize_exact_formal(expression: dict[tuple, Exact]):
    return {
        repr(key): exact_string(value)
        for key, value in sorted(expression.items(), key=lambda item: repr(item[0]))
    }


def run_checks():
    failures: list[str] = []
    checks: dict[str, object] = {}

    clifford_failures = check_sigma_lorentz_action()
    failures.extend(clifford_failures)
    checks["lorentz_clifford"] = {"failures": clifford_failures}

    wick_f_failures, wick_f = check_wick_sigma_f()
    failures.extend(wick_f_failures)
    checks["wick_sigma_f"] = wick_f

    wick_d_failures, wick_d = check_wick_sigma_d()
    failures.extend(wick_d_failures)
    checks["wick_sigma_d"] = wick_d

    scalar_actual, scalar_expected = check_scalar_duality_and_norm()
    if scalar_actual != scalar_expected:
        failures.append("su4_scalar_norm")
    checks["su4_scalar_norm"] = {
        "actual": serialize_formal(scalar_actual),
        "expected": serialize_formal(scalar_expected),
    }

    yukawa = check_su4_yukawa()
    uncontracted_yukawa_ok = (
        yukawa["uncontracted_actual"] == yukawa["uncontracted_expected"]
    )
    premature_reduction_rejected = (
        yukawa["uncontracted_actual"]
        != yukawa["premature_uncontracted_reduction"]
    )
    contracted_yukawa_ok = (
        yukawa["contracted_actual"] == yukawa["contracted_expected"]
    )
    if not uncontracted_yukawa_ok:
        failures.append("su4_yukawa_uncontracted_ordered")
    if not premature_reduction_rejected:
        failures.append("su4_yukawa_premature_reduction_not_rejected")
    if not contracted_yukawa_ok:
        failures.append("su4_yukawa_contracted_reduction")
    checks["su4_yukawa_packaging"] = {
        "uncontracted_actual": serialize_formal(yukawa["uncontracted_actual"]),
        "uncontracted_expected": serialize_formal(yukawa["uncontracted_expected"]),
        "premature_uncontracted_reduction": serialize_formal(
            yukawa["premature_uncontracted_reduction"]
        ),
        "contracted_actual": serialize_formal(yukawa["contracted_actual"]),
        "contracted_expected": serialize_formal(yukawa["contracted_expected"]),
        "uncontracted_ordered_passed": uncontracted_yukawa_ok,
        "premature_uncontracted_reduction_rejected": premature_reduction_rejected,
        "contracted_reduction_passed": contracted_yukawa_ok,
    }

    quartic_actual, quartic_expected = check_su4_quartic()
    quartic_equivalent = lie_equivalent_mod_jacobi(quartic_actual, quartic_expected)
    if not quartic_equivalent:
        failures.append("su4_quartic_packaging")
    checks["su4_quartic_packaging"] = {
        "actual": serialize_formal(quartic_actual),
        "expected": serialize_formal(quartic_expected),
        "equivalent_mod_invariance_and_jacobi": quartic_equivalent,
    }

    quartic_census_checks, quartic_census_data = check_su4_quartic_census()
    for key, passed in quartic_census_checks.items():
        if not passed:
            failures.append(f"su4_quartic_census_{key}")
    checks["su4_quartic_census"] = {
        "checks": quartic_census_checks,
        **quartic_census_data,
    }

    auxiliary_actual, auxiliary_expected = check_su2_auxiliary()
    if auxiliary_actual != auxiliary_expected:
        failures.append("su2_auxiliary_triplet")
    checks["su2_auxiliary_triplet"] = {
        "actual": serialize_formal(auxiliary_actual),
        "expected": serialize_formal(auxiliary_expected),
    }

    n2_boundary_checks, n2_boundary_data = check_n2_contracted_auxiliary_boundary()
    for key, passed in n2_boundary_checks.items():
        if not passed:
            failures.append(f"n2_auxiliary_boundary_{key}")
    checks["n2_contracted_auxiliary_boundary"] = {
        "checks": n2_boundary_checks,
        **{
            key: serialize_formal(value)
            for key, value in n2_boundary_data.items()
        },
    }

    n4_auxiliary_checks, n4_auxiliary_data = check_n4_auxiliary_square()
    for key, passed in n4_auxiliary_checks.items():
        if not passed:
            failures.append(f"n4_auxiliary_{key}")
    checks["n4_auxiliary_square"] = {
        "checks": n4_auxiliary_checks,
        "original": serialize_exact_formal(n4_auxiliary_data["original"]),
        "completed": serialize_exact_formal(n4_auxiliary_data["completed"]),
        "q_pairing_actual": serialize_formal(n4_auxiliary_data["q_pairing_actual"]),
        "q_pairing_expected": serialize_formal(n4_auxiliary_data["q_pairing_expected"]),
    }

    for signature, euclidean in (("lorentz", False), ("euclidean", True)):
        current_actual, current_expected = check_n2_current_expansion(euclidean)
        if current_actual != current_expected:
            failures.append(f"n2_{signature}_current_expansion")
        checks[f"n2_{signature}_current_expansion"] = {
            "actual": {
                repr(key): exact_string(value)
                for key, value in sorted(current_actual.items(), key=lambda item: repr(item[0]))
            },
            "expected": {
                repr(key): exact_string(value)
                for key, value in sorted(current_expected.items(), key=lambda item: repr(item[0]))
            },
        }

    rho_failures, rho_checks = check_su4_rho_identities()
    failures.extend(rho_failures)
    checks["su4_rho_identities"] = {
        "failure_count": len(rho_failures),
        "checks": rho_checks,
    }

    triple_failures = check_sigma_triple_identity()
    failures.extend(triple_failures)
    checks["sigma_triple_identity"] = {
        "failure_count": len(triple_failures),
        "failures": triple_failures,
    }

    bar_triple_failures = check_bar_sigma_triple_identity()
    failures.extend(bar_triple_failures)
    checks["bar_sigma_triple_identity"] = {
        "failure_count": len(bar_triple_failures),
        "failures": bar_triple_failures,
    }

    schouten_failures = check_two_spinor_schouten()
    failures.extend(schouten_failures)
    checks["two_spinor_schouten"] = {
        "failure_count": len(schouten_failures),
        "failures": schouten_failures,
    }

    closure_failures, closure_checks = check_n4_fermion_closure_eom_reduction()
    failures.extend(closure_failures)
    checks["n4_fermion_closure_eom_reduction"] = {
        "failure_count": len(closure_failures),
        "checks": closure_checks,
    }

    divergence_wick_failures, divergence_wick_checks = (
        check_n4_divergence_wick_coefficients()
    )
    failures.extend(divergence_wick_failures)
    checks["n4_divergence_wick_coefficients"] = {
        "failure_count": len(divergence_wick_failures),
        "checks": divergence_wick_checks,
    }

    # Cubic equations: 2 C=sqrt(2), -u/2=C.
    coefficient_c = SQRT_TWO * HALF
    coefficient_u = -SQRT_TWO
    cubic_ok = TWO * coefficient_c == SQRT_TWO and -(coefficient_u * HALF) == coefficient_c
    if not cubic_ok:
        failures.append("n4_cubic_coefficient")
    checks["n4_cubic_coefficient"] = {
        "C": exact_string(coefficient_c),
        "u": exact_string(coefficient_u),
        "passed": cubic_ok,
    }

    return {
        "schema": 1,
        "task": "CONTRACT-STEP-04-EXTENDED-SUPER-YANG-MILLS-001",
        "exact_ring": "Q(i,sqrt(2)) plus integer formal internal-index algebra",
        "failure_count": len(failures),
        "failures": failures,
        "checks": checks,
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
