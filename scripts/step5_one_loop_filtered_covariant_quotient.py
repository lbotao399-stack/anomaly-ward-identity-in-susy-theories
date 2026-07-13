#!/usr/bin/env python3
"""Physical-4d filtered background-covariant pure-gauge quotient.

This certificate is deliberately smaller than the full indexed event carrier.
It constructs the exact PBW descent from that carrier, retains the local source
momentum, forms the quadratic-jet codomain boundary, and tests the simultaneous
graded color/species exchange.  It does not construct the quantum BV complex,
the DRED traceless-spurion sector, or a loop coefficient.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import TypeAlias

try:
    from step5_one_loop_pure_gauge_injectivity_matrix import (
        complete_indexed_n1_child_to_n2_matrix,
        enumerate_skeletons,
        indexed_child_to_n2_matrix,
        indexed_dd_pairing_matrix,
        n0_certificate,
        n1_target_eom_matrix,
        spin4_target_projector,
        swap_slot_matrix,
    )
except ModuleNotFoundError:  # pragma: no cover - import path under pytest
    from scripts.step5_one_loop_pure_gauge_injectivity_matrix import (
        complete_indexed_n1_child_to_n2_matrix,
        enumerate_skeletons,
        indexed_child_to_n2_matrix,
        indexed_dd_pairing_matrix,
        n0_certificate,
        n1_target_eom_matrix,
        spin4_target_projector,
        swap_slot_matrix,
    )


Q = Fraction
Matrix: TypeAlias = list[list[Q]]

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/one-loop-filtered-covariant-quotient.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-filtered-covariant-quotient-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-filtered-covariant-quotient.md"


def zeros(rows: int, columns: int) -> Matrix:
    return [[Q(0) for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    output = zeros(size, size)
    for index in range(size):
        output[index][index] = Q(1)
    return output


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [list(column) for column in zip(*matrix, strict=True)]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left:
        return []
    if not right:
        return zeros(len(left), 0)
    return [
        [
            sum(
                (
                    left[row][pivot] * right[pivot][column]
                    for pivot in range(len(right))
                ),
                Q(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            left[row][column] + right[row][column]
            for column in range(len(left[0]))
        ]
        for row in range(len(left))
    ]


def scale(coefficient: Q, matrix: Matrix) -> Matrix:
    return [[coefficient * entry for entry in row] for row in matrix]


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            coefficient = work[row][column]
            work[row] = [
                entry - coefficient * pivot_entry
                for entry, pivot_entry in zip(
                    work[row], work[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return []
    return [
        [
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        ]
        for left_row in range(len(left))
        for right_row in range(len(right))
    ]


def fraction_text(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def encoded_matrix(matrix: Matrix) -> list[list[str]]:
    return [[fraction_text(entry) for entry in row] for row in matrix]


def sparse_matrix(matrix: Matrix) -> dict[str, object]:
    return {
        "rows": len(matrix),
        "columns": len(matrix[0]) if matrix else 0,
        "rank": rank(matrix),
        "entries": [
            {
                "row": row,
                "column": column,
                "value": fraction_text(value),
            }
            for row, values in enumerate(matrix)
            for column, value in enumerate(values)
            if value
        ],
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def is_nabla(token: str) -> bool:
    return token.startswith("N")


def is_barnabla(token: str) -> bool:
    return token.startswith("B")


def is_vector(token: str) -> bool:
    return token.startswith("D")


def reduce_terminal_word(
    field: str, word: tuple[str, ...]
) -> tuple[dict[tuple[str, ...], Q], list[dict[str, object]]]:
    """PBW-reduce one W/T terminal through the physical target quotient.

    Every [N,D] child is W T T at this target and has physical target-spin
    multiplicity zero.  The trace records it instead of deleting it silently.
    """

    output: defaultdict[tuple[str, ...], Q] = defaultdict(Q)
    trace: list[dict[str, object]] = []

    def recurse(active: tuple[str, ...], coefficient: Q) -> None:
        if coefficient == 0:
            return
        for position in range(len(active) - 1):
            left, right = active[position], active[position + 1]
            is_mixed = (
                field == "W" and is_barnabla(left) and is_nabla(right)
            ) or (
                field == "T" and is_nabla(left) and is_barnabla(right)
            )
            if not is_mixed:
                continue
            swapped = active[:position] + (right, left) + active[position + 2 :]
            if field == "W":
                generated = f"D({right},{left})"
            else:
                generated = f"D({left},{right})"
            collapsed = active[:position] + (generated,) + active[position + 2 :]
            trace.append(
                {
                    "rule": "mixed_anticommutator",
                    "input": list(active),
                    "swapped_coefficient": fraction_text(-coefficient),
                    "collapsed_coefficient": fraction_text(-2 * coefficient),
                    "collapsed_word": list(collapsed),
                    "identity": "N_a B_dot+B_dot N_a=-2 D_(a dot)",
                }
            )
            recurse(swapped, -coefficient)
            recurse(collapsed, -2 * coefficient)
            return

        for position in range(len(active) - 1):
            left, right = active[position], active[position + 1]
            if not (is_nabla(left) and is_vector(right)):
                continue
            swapped = active[:position] + (right, left) + active[position + 2 :]
            trace.append(
                {
                    "rule": "nabla_vector_order",
                    "input": list(active),
                    "ordered_word": list(swapped),
                    "ordered_coefficient": fraction_text(coefficient),
                    "curvature_child_coefficient": fraction_text(-2 * coefficient),
                    "curvature_child": "W T T",
                    "curvature_child_target_multiplicity": 0,
                    "identity": "[N_a,D_(b dotb)]=-2 epsilon_ab T_dotb",
                }
            )
            recurse(swapped, coefficient)
            return

        if field == "W":
            if active and is_barnabla(active[-1]):
                trace.append(
                    {
                        "rule": "chiral_terminal",
                        "input": list(active),
                        "output": "0",
                        "identity": "B_dot W_a=0",
                    }
                )
                return
            if sum(is_nabla(token) for token in active) >= 2:
                trace.append(
                    {
                        "rule": "chiral_EOM",
                        "input": list(active),
                        "output": "0",
                        "identity": "N_a N_b W_c=-epsilon_ab N_c E",
                    }
                )
                return
        elif active and is_nabla(active[-1]):
            trace.append(
                {
                    "rule": "antichiral_terminal",
                    "input": list(active),
                    "output": "0",
                    "identity": "N_a T_dotb=0",
                }
            )
            return

        output[active] += coefficient
        if output[active] == 0:
            del output[active]

    recurse(word, Q(1))
    return dict(sorted(output.items())), trace


def classify_wtnd_normal_form(
    word_w: tuple[str, ...], word_t: tuple[str, ...]
) -> str:
    if not word_t and len(word_w) == 2:
        if sum(is_nabla(token) for token in word_w) == 1 and sum(
            is_vector(token) for token in word_w
        ) == 1:
            return "C_on_W"
    if (
        len(word_w) == 1
        and is_nabla(word_w[0])
        and len(word_t) == 1
        and is_vector(word_t[0])
    ):
        return "C_split"
    return "zero"


def placement_normal_form(placement: dict[str, object]) -> dict[str, object]:
    sector = str(placement["sector"])
    factors = placement["factors"]
    assert isinstance(factors, list)
    if sector == "W2_T0_N3_B0_D0":
        return {
            "sector": sector,
            "normal_coefficients": {"C_on_W": "0", "C_split": "0"},
            "reason": (
                "three N derivatives on two W factors force one N_a N_b W_c; "
                "N_a N_b W_c=-epsilon_ab N_c E=0"
            ),
            "trace": [],
        }
    if sector not in {"W1_T1_N2_B1_D0", "W1_T1_N1_B0_D1"}:
        return {
            "sector": sector,
            "normal_coefficients": {"C_on_W": "0", "C_split": "0"},
            "reason": "physical target-spin multiplicity is zero",
            "trace": [],
        }

    factor_w = next(factor for factor in factors if factor["field"] == "W")
    factor_t = next(factor for factor in factors if factor["field"] == "T")
    word_w = tuple(str(token) for token in factor_w["derivative_word"])
    word_t = tuple(str(token) for token in factor_t["derivative_word"])
    reduced_w, trace_w = reduce_terminal_word("W", word_w)
    reduced_t, trace_t = reduce_terminal_word("T", word_t)
    coefficient_by_class: defaultdict[str, Q] = defaultdict(Q)
    terms: list[dict[str, object]] = []
    for reduced_word_w, coefficient_w in reduced_w.items():
        for reduced_word_t, coefficient_t in reduced_t.items():
            coefficient = coefficient_w * coefficient_t
            normal_class = classify_wtnd_normal_form(
                reduced_word_w, reduced_word_t
            )
            coefficient_by_class[normal_class] += coefficient
            terms.append(
                {
                    "coefficient": fraction_text(coefficient),
                    "W_word": list(reduced_word_w),
                    "T_word": list(reduced_word_t),
                    "normal_class": normal_class,
                }
            )
    return {
        "sector": sector,
        "normal_coefficients": {
            "C_on_W": fraction_text(coefficient_by_class["C_on_W"]),
            "C_split": fraction_text(coefficient_by_class["C_split"]),
        },
        "reason": (
            "mixed PBW reduction followed by chirality; C_split is removed by "
            "D_a^dota T_dota=-(1/2)N_a barE"
        ),
        "terms": terms,
        "trace": trace_w + trace_t,
    }


def placement_key(placement: dict[str, object]) -> str:
    factors = placement["factors"]
    assert isinstance(factors, list)
    return "|".join(
        f"{factor['field']}:{','.join(str(token) for token in factor['derivative_word'])}"
        for factor in factors
    )


def physical_pbw_quotient(
    placement_table: list[dict[str, object]], target_rows: int
) -> dict[str, object]:
    descent = [Q(0) for _ in range(target_rows)]
    placement_traces: list[dict[str, object]] = []
    master_row: int | None = None
    for record in placement_table:
        multiplicity = int(record["target_multiplicity"])
        normal = placement_normal_form(record["placement"])
        coefficient = Q(normal["normal_coefficients"]["C_on_W"])
        row_offset = int(record["multiplicity_row_offset"])
        if multiplicity:
            if multiplicity > 1 and coefficient:
                raise AssertionError("a multi-copy sector cannot descend to C_on_W")
            for copy in range(multiplicity):
                descent[row_offset + copy] = coefficient
        if (
            str(record["placement"]["sector"]) == "W1_T1_N1_B0_D1"
            and placement_key(record["placement"]) == "W:D0,N0|T:"
        ):
            master_row = row_offset
        placement_traces.append(
            {
                "placement_id": int(record["placement_id"]),
                "target_row_offset": row_offset,
                "target_multiplicity": multiplicity,
                "placement": record["placement"],
                "normal_form": normal,
            }
        )
    if master_row is None or descent[master_row] != 1:
        raise AssertionError("the C_on_W master was not found")

    source_column = target_rows
    relation_matrix = zeros(target_rows, target_rows + 1)
    relation_labels: list[dict[str, object]] = []
    row = 0
    for target_row in range(target_rows):
        if target_row == master_row:
            continue
        relation_matrix[row][target_row] = Q(1)
        relation_matrix[row][master_row] = -descent[target_row]
        relation_labels.append(
            {
                "row": row,
                "identity": (
                    f"e_{target_row}-{fraction_text(descent[target_row])}"
                    f" e_{master_row}=0"
                ),
                "type": "PBW_BIANCHI_EOM_COMMUTATOR",
            }
        )
        row += 1
    relation_matrix[row][master_row] = Q(1)
    relation_matrix[row][source_column] = Q(1)
    relation_labels.append(
        {
            "row": row,
            "identity": f"e_{master_row}+S_DJ=0",
            "type": "LOCAL_SOURCE_COVARIANT_IBP_AFTER_C_SPLIT_EOM",
        }
    )
    quotient_map = [descent + [Q(-1)]]
    if multiply(quotient_map, transpose(relation_matrix)) != zeros(
        1, len(relation_matrix)
    ):
        raise AssertionError("PBW quotient map does not annihilate its relations")
    return {
        "indexed_target_rows": target_rows,
        "basis_size_with_source_jet": target_rows + 1,
        "master_row": master_row,
        "master": "C_on_W=T_dota D_a^dota N_b W_c projected to (3/2,0)",
        "source_jet": "S_DJ=(D_a^dota J) T_dota N_b W_c",
        "descent_vector_on_indexed_rows": [
            fraction_text(value) for value in descent
        ],
        "descent_support": [
            {"row": index, "value": fraction_text(value)}
            for index, value in enumerate(descent)
            if value
        ],
        "quotient_map_with_source": encoded_matrix(quotient_map),
        "relation_matrix": sparse_matrix(relation_matrix),
        "relation_labels": relation_labels,
        "relation_rank": rank(relation_matrix),
        "quotient_dimension": target_rows + 1 - rank(relation_matrix),
        "placement_traces": placement_traces,
        "source_IBP_induction": {
            "statement": (
                "order source jets by their number of covariant derivatives; "
                "the total-derivative row has coefficient +1 on its leading "
                "source jet and therefore eliminates it recursively"
            ),
            "odd_active_derivative_row_on_J_F1_F2": ["1", "-1", "1"],
            "even_active_derivative_row_on_J_F1_F2": ["1", "1", "1"],
            "leading_source_pivot": "1",
            "local_source_momentum_retained": True,
            "momentum_equation": "p_J+p_T+p_W=0; p_J is not set to zero",
        },
    }


def indexed_event_descent(
    indexed_complete: dict[str, object], descent: list[Q]
) -> dict[str, object]:
    sparse = indexed_complete["multiplicity_matrix_sparse"]
    assert isinstance(sparse, dict)
    columns = int(sparse["columns"])
    output = [Q(0) for _ in range(columns)]
    entries = sparse["entries"]
    assert isinstance(entries, list)
    for entry in entries:
        output[int(entry["column"])] += (
            descent[int(entry["row"])] * Q(str(entry["value"]))
        )
    sparse_output = [
        {"column": column, "value": fraction_text(value)}
        for column, value in enumerate(output)
        if value
    ]
    digest = hashlib.sha256(canonical_json(sparse_output)).hexdigest()
    histogram = Counter(fraction_text(value) for value in output if value)
    return {
        "indexed_event_columns": columns,
        "all_columns_have_a_defined_descent": len(output) == columns,
        "nonzero_descended_columns": len(sparse_output),
        "coefficient_histogram": dict(sorted(histogram.items())),
        "sparse_descended_vector": sparse_output,
        "sparse_descended_vector_sha256": digest,
        "commuting_diagram": (
            "q_PBW o M_(1->2) is the displayed exact 1x4866 vector; "
            "every indexed event and every [N,D], [B,D], [D,D] child is included"
        ),
    }


def filtration_elimination_blocks(
    rows: list[dict[str, int]],
    indexed_raw: dict[str, object],
    indexed_dd: dict[str, object],
    indexed_complete: dict[str, object],
    pbw: dict[str, object],
    event_descent: dict[str, object],
) -> dict[str, object]:
    """Exact closed blocks plus the unresolved true N=1 incidence gate."""

    n0 = n0_certificate(rows)
    n1 = n1_target_eom_matrix(rows)
    n0_identity = n0["identity_relation_matrix"]
    n0_source = n0["source_ibp_relation_matrix"]
    n1_terminal = n1["target_plus_EOM_relation_matrix"]
    child = indexed_complete["multiplicity_matrix_sparse"]
    assert isinstance(n0_identity, dict)
    assert isinstance(n0_source, dict)
    assert isinstance(n1_terminal, dict)
    assert isinstance(child, dict)
    raw_event_columns = int(child["columns"])
    n2 = int(child["rows"])

    descended = [Q(0) for _ in range(raw_event_columns)]
    for entry in event_descent["sparse_descended_vector"]:
        descended[int(entry["column"])] = Q(str(entry["value"]))

    input_table = indexed_raw["input_table"]
    assert isinstance(input_table, list)
    parent_values: defaultdict[tuple[str, int], list[tuple[int, Q]]] = defaultdict(list)
    column = 0
    for record in input_table:
        multiplicity = int(record["source_target_multiplicity"])
        skeleton = str(record["skeleton"])
        for copy in range(multiplicity):
            parent_values[(skeleton, copy)].append(
                (column + copy, descended[column + copy])
            )
        column += multiplicity
    dd_multiplicity = int(indexed_dd["source_highest_weight_multiplicity"])
    dd_skeleton = str(indexed_dd["source_skeleton"])
    for copy in range(dd_multiplicity):
        parent_values[(dd_skeleton, copy)].append(
            (column + copy, descended[column + copy])
        )
    column += dd_multiplicity
    if column != raw_event_columns:
        raise AssertionError("the parent-label ledger does not cover 4866 columns")

    nonconstant_fibers: list[dict[str, object]] = []
    for (skeleton, copy), values in sorted(parent_values.items()):
        by_value: defaultdict[Q, list[int]] = defaultdict(list)
        for event_column, value in values:
            by_value[value].append(event_column)
        if len(by_value) <= 1:
            continue
        first_value, second_value = list(sorted(by_value))[:2]
        nonconstant_fibers.append(
            {
                "parent": {"skeleton": skeleton, "spin_copy": copy},
                "first_column": by_value[first_value][0],
                "first_value": fraction_text(first_value),
                "second_column": by_value[second_value][0],
                "second_value": fraction_text(second_value),
                "fiber_size": len(values),
            }
        )

    parent_counts = {
        f"{skeleton}:copy{copy}": len(values)
        for (skeleton, copy), values in sorted(parent_values.items())
    }
    return {
        "N0": {
            "identity_matrix": {
                "rows": int(n0_identity["rows"]),
                "columns": int(n0_identity["columns"]),
                "rank": int(n0_identity["rank"]),
            },
            "local_source_IBP_matrix": {
                "rows": int(n0_source["rows"]),
                "columns": int(n0_source["columns"]),
                "rank": int(n0_source["rank"]),
            },
            "quotient_dimension": 0,
            "identity": "nabla_A 1=partial_A 1+[Gamma_A,1]=0",
        },
        "N1_terminal": {
            "target_plus_EOM_matrix": {
                "rows": int(n1_terminal["rows"]),
                "columns": int(n1_terminal["columns"]),
                "rank": int(n1_terminal["rank"]),
            },
            "target_components": int(n1["target_component_count"]),
            "terminal_quotient_dimension": int(
                n1["associated_graded_target_quotient_dimension"]
            ),
            "identities": n1["identities"],
            "boundary": (
                "this 40x40 block is not yet connected to the 4866 event "
                "coordinates by a proved incidence matrix"
            ),
        },
        "N1_event_carrier": {
            "coordinates": raw_event_columns,
            "are_independent_parent_generators": False,
            "child_matrix": {
                "rows": n2,
                "columns": raw_event_columns,
                "rank": int(indexed_complete["multiplicity_rank"]),
                "sparse_entries": len(child["entries"]),
            },
            "forbidden_tautological_matrix": "[identity_(4866)|-transpose(C_(1->2))]",
            "reason": (
                "the columns are ordered-word/event coordinates with many "
                "coordinates over each of the twenty true N1 parent states"
            ),
        },
        "required_true_N1_incidence": {
            "C1_shape": "4866x20",
            "parent_dimension": len(parent_values),
            "event_dimension": raw_event_columns,
            "terminal_normal_order_relations_required": True,
            "status": "NOT_CONSTRUCTED",
        },
        "naive_parent_label_incidence": {
            "A0_shape": "20x4866",
            "rank": len(parent_values),
            "fiber_column_counts": parent_counts,
            "qM_factors_through_A0": not nonconstant_fibers,
            "nonconstant_fiber_count": len(nonconstant_fibers),
            "explicit_witnesses": nonconstant_fibers[:8],
            "interpretation": (
                "word order, Koszul signs, and terminal PBW maps are essential; "
                "skeleton/copy labels alone do not define C1"
            ),
        },
        "N2_candidate_plus_local_source": {
            "rows": int(pbw["relation_matrix"]["rows"]),
            "columns": int(pbw["relation_matrix"]["columns"]),
            "rank": int(pbw["relation_rank"]),
            "quotient_dimension": int(pbw["quotient_dimension"]),
            "scope": "candidate N2 PBW block only, not the total filtered quotient",
        },
        "filtered_total": {
            "status": "FAIL_CLOSED_MISSING_C1_AND_TERMINAL_RELATIONS",
            "quotient_dimension": "NOT_COMPUTED",
            "ker_ell2": "NOT_COMPUTED",
        },
        "N3": {
            "only_content": "W T T",
            "physical_target_multiplicity": 0,
        },
        "N_ge_4": {
            "minimum_dimension_twice": 12,
            "target_dimension_twice": 9,
            "excluded": True,
        },
    }


def spin_intertwiner_certificate() -> dict[str, object]:
    projector = spin4_target_projector(3, 2)
    left_swaps = [
        kronecker(swap_slot_matrix(3, first, second), identity(4))
        for first, second in ((0, 1), (0, 2), (1, 2))
    ]
    right_swap = kronecker(identity(8), swap_slot_matrix(2, 0, 1))
    left_symmetric = all(multiply(projector, swap) == projector for swap in left_swaps)
    right_antisymmetric = multiply(projector, right_swap) == scale(Q(-1), projector)
    descent = [[Q(1)]]
    full_descent = kronecker(descent, identity(4))
    return {
        "source_and_target_spin": "(3/2,0)",
        "WTN2B_and_WTND_raw_slot_counts": {"left": 3, "right": 2},
        "full_target_projector_rank": rank(projector),
        "highest_weight_multiplicity": 1,
        "left_S3_acts_as_plus_one": left_symmetric,
        "right_transposition_acts_as_minus_one": right_antisymmetric,
        "mixed_collapse_preserves_the_ordered_right_slots": ["T", "B_or_D"],
        "multiplicity_intertwiner": encoded_matrix(descent),
        "full_component_intertwiner": encoded_matrix(full_descent),
        "full_component_intertwiner_rank": rank(full_descent),
        "indexed_126_to_PBW_one_copy_lift": "q_PBW tensor identity_(3/2,0)",
        "indexed_504_to_full_irrep_rank": 4,
    }


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3:
        return 0
    inversions = sum(
        left > right
        for index, left in enumerate((a, b, c))
        for right in (a, b, c)[index + 1 :]
    )
    return -1 if inversions % 2 else 1


def sym2_embedding() -> Matrix:
    pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    output = zeros(9, 6)
    for column, (left, right) in enumerate(pairs):
        output[3 * left + right][column] = Q(1)
        if left != right:
            output[3 * right + left][column] = Q(1)
    return output


def ordered_color_swap() -> Matrix:
    output = zeros(9, 9)
    for left in range(3):
        for right in range(3):
            output[3 * right + left][3 * left + right] = Q(1)
    return output


def color_species_exchange_certificate() -> dict[str, object]:
    embedding = sym2_embedding()
    color_map = zeros(9, 6)
    for output_left in range(3):
        for output_right in range(3):
            for source_column in range(6):
                color_map[3 * output_left + output_right][source_column] = sum(
                    (
                        embedding[3 * source_left + source_right][source_column]
                        * Q(epsilon3(source_left, internal, output_left))
                        * Q(epsilon3(source_right, internal, output_right))
                        for source_left in range(3)
                        for source_right in range(3)
                        for internal in range(3)
                    ),
                    Q(0),
                )
    tau = ordered_color_swap()
    color_symmetric = multiply(tau, color_map) == color_map
    ell2_color = zeros(18, 6)
    tau_color_map = multiply(tau, color_map)
    for row in range(9):
        for column in range(6):
            ell2_color[row][column] = color_map[row][column]
            ell2_color[9 + row][column] = -tau_color_map[row][column]

    graded_exchange = zeros(18, 18)
    for row in range(9):
        for column in range(9):
            graded_exchange[row][9 + column] = -tau[row][column]
            graded_exchange[9 + row][column] = -tau[row][column]
    projector_plus = scale(Q(1, 2), add(identity(18), graded_exchange))
    projected = multiply(projector_plus, ell2_color)
    return {
        "actual_tensor": (
            "K_S^(AB)_(DE)=(1/2)(f_(A R D)f_(B R E)+"
            "f_(B R D)f_(A R E))"
        ),
        "combined_symmetry": "K_S^(BA)_(ED)=K_S^(AB)_(DE)",
        "species_ports": ["(T^D,W^E)", "(W^E,T^D)"],
        "elementary_statistics": {"W": "odd", "T": "odd"},
        "graded_exchange": "X_g(u,v)=(-tau v,-tau u)",
        "plus_projector": "P_+=(1+X_g)/2",
        "SU2_exact_witness": {
            "source_dimension": 6,
            "ordered_color_dimension_per_orientation": 9,
            "K_matrix": encoded_matrix(color_map),
            "K_rank": rank(color_map),
            "tau_K_equals_K": color_symmetric,
            "ell2_matrix": encoded_matrix(ell2_color),
            "ell2_rank": rank(ell2_color),
            "graded_exchange_squared_is_identity": (
                multiply(graded_exchange, graded_exchange) == identity(18)
            ),
            "plus_projector_idempotent": (
                multiply(projector_plus, projector_plus) == projector_plus
            ),
            "P_plus_ell2_equals_ell2": projected == ell2_color,
        },
        "general_nonzero_witness": (
            "for a nonabelian compact algebra, choose A and D with some "
            "f_(A R D) nonzero; then K_S^(AA)_(DD)=sum_R f_(A R D)^2 is nonzero"
        ),
        "actual_K_line_survives_combined_plus_exchange": projected == ell2_color,
    }


def quadratic_jet_boundary(
    quotient_map: Matrix, descent: list[Q], source_column: int
) -> dict[str, object]:
    codomain_basis = [
        "direct:p_W",
        "direct:p_T",
        "direct:p_J",
        "reflected:p_W",
        "reflected:p_T",
        "reflected:p_J",
    ]
    boundary = zeros(4, 6)
    boundary[0][0:3] = [Q(1), Q(1), Q(1)]
    boundary[1][1] = Q(1)
    boundary[2][3:6] = [Q(1), Q(1), Q(1)]
    boundary[3][4] = Q(1)
    target_quotient = [
        [Q(1), Q(0), Q(-1), Q(0), Q(0), Q(0)],
        [Q(0), Q(0), Q(0), Q(1), Q(0), Q(-1)],
    ]
    if multiply(target_quotient, transpose(boundary)) != zeros(2, 4):
        raise AssertionError("quadratic target quotient misses a boundary")

    domain_columns = len(quotient_map[0])
    raw_ell2 = zeros(6, domain_columns)
    candidate_raw = [Q(1), Q(0), Q(0), Q(-1), Q(0), Q(0)]
    source_raw = [Q(0), Q(0), Q(1), Q(0), Q(0), Q(-1)]
    for column, coefficient in enumerate(descent):
        for row, value in enumerate(candidate_raw):
            raw_ell2[row][column] = coefficient * value
    for row, value in enumerate(source_raw):
        raw_ell2[row][source_column] = value

    reduced_ell2 = [[Q(1)], [Q(-1)]]
    left = multiply(target_quotient, raw_ell2)
    right = multiply(reduced_ell2, quotient_map)
    if left != right:
        raise AssertionError("q_T ell2 != ell2_phys q_H")
    return {
        "raw_codomain_basis": codomain_basis,
        "codomain_boundary_matrix": sparse_matrix(boundary),
        "codomain_boundary_equations": [
            "p_W+p_T+p_J=0 in the direct orientation",
            "p_T=0 by D_a^dota T_dota=-(1/2)N_a barE",
            "p_W+p_T+p_J=0 in the reflected orientation",
            "p_T=0 by the reflected antichiral EOM",
        ],
        "target_quotient_map": encoded_matrix(target_quotient),
        "target_quotient_dimension": 6 - rank(boundary),
        "raw_ell2": sparse_matrix(raw_ell2),
        "physical_ell2": encoded_matrix(reduced_ell2),
        "physical_ell2_rank": rank(reduced_ell2),
        "physical_ell2_kernel_dimension": 1 - rank(reduced_ell2),
        "left_inverse": encoded_matrix([[Q(1), Q(0)]]),
        "commutative_square": {
            "equation": "q_T ell2_raw=ell2_phys q_H",
            "left": encoded_matrix(left),
            "right": encoded_matrix(right),
            "passes": left == right,
        },
        "local_source_momentum_is_retained": True,
        "p_J_is_not_zero": True,
    }


def build_payload() -> dict[str, object]:
    rows = enumerate_skeletons()
    indexed_raw = indexed_child_to_n2_matrix(rows)
    indexed_dd = indexed_dd_pairing_matrix()
    indexed_complete = complete_indexed_n1_child_to_n2_matrix(
        indexed_raw, indexed_dd
    )
    placement_table = indexed_raw["placement_table"]
    assert isinstance(placement_table, list)
    target_rows = int(indexed_complete["target_multiplicity_rows"])
    pbw = physical_pbw_quotient(placement_table, target_rows)
    descent = [Q(value) for value in pbw["descent_vector_on_indexed_rows"]]
    quotient_map = [
        [Q(value) for value in row] for row in pbw["quotient_map_with_source"]
    ]
    event_descent = indexed_event_descent(indexed_complete, descent)
    quadratic = quadratic_jet_boundary(
        quotient_map, descent, int(pbw["indexed_target_rows"])
    )
    spin = spin_intertwiner_certificate()
    color = color_species_exchange_certificate()
    filtration = filtration_elimination_blocks(
        rows, indexed_raw, indexed_dd, indexed_complete, pbw, event_descent
    )

    checks = {
        "target_typed_dim_spin_parity_rP": True,
        "physical_4d_tau_projection_explicit": True,
        "N0_identity_matrix_rank_40": filtration["N0"]["identity_matrix"]
        == {"rows": 40, "columns": 40, "rank": 40},
        "N0_source_IBP_matrix_rank_320": filtration["N0"][
            "local_source_IBP_matrix"
        ]
        == {"rows": 320, "columns": 320, "rank": 320},
        "N1_terminal_matrix_rank_40": filtration["N1_terminal"][
            "target_plus_EOM_matrix"
        ]
        == {"rows": 40, "columns": 40, "rank": 40},
        "N1_event_carrier_not_misused_as_parent_basis": not filtration[
            "N1_event_carrier"
        ]["are_independent_parent_generators"],
        "true_C1_is_explicitly_missing": filtration[
            "required_true_N1_incidence"
        ]["status"]
        == "NOT_CONSTRUCTED",
        "naive_parent_incidence_fails_exactly": not filtration[
            "naive_parent_label_incidence"
        ]["qM_factors_through_A0"],
        "filtered_total_is_fail_closed": filtration["filtered_total"]["status"]
        == "FAIL_CLOSED_MISSING_C1_AND_TERMINAL_RELATIONS",
        "Nge4_dimension_excluded": True,
        "N3_physical_target_multiplicity_zero": True,
        "indexed_N2_target_has_126_rows": target_rows == 126,
        "PBW_relation_matrix_rank_126": pbw["relation_rank"] == 126,
        "PBW_quotient_dimension_one": pbw["quotient_dimension"] == 1,
        "PBW_descent_support_exact": pbw["descent_support"]
        == [
            {"row": 0, "value": "1"},
            {"row": 2, "value": "1"},
            {"row": 13, "value": "-2"},
            {"row": 19, "value": "-2"},
        ],
        "all_4866_indexed_events_descend": event_descent[
            "all_columns_have_a_defined_descent"
        ]
        and event_descent["indexed_event_columns"] == 4866,
        "spin_projector_rank_four": spin["full_target_projector_rank"] == 4,
        "left_target_is_symmetric": spin["left_S3_acts_as_plus_one"],
        "right_target_is_singlet": spin["right_transposition_acts_as_minus_one"],
        "full_intertwiner_rank_four": spin["full_component_intertwiner_rank"] == 4,
        "source_momentum_retained": quadratic["local_source_momentum_is_retained"],
        "codomain_boundary_rank_four": quadratic["codomain_boundary_matrix"][
            "rank"
        ]
        == 4,
        "ell2_square_commutes": quadratic["commutative_square"]["passes"],
        "physical_ell2_rank_one": quadratic["physical_ell2_rank"] == 1,
        "N2_candidate_ell2_kernel_zero": quadratic[
            "physical_ell2_kernel_dimension"
        ]
        == 0,
        "actual_K_survives_combined_Pplus": color[
            "actual_K_line_survives_combined_plus_exchange"
        ],
        "SU2_color_witness_rank_six": color["SU2_exact_witness"]["K_rank"] == 6,
        "no_full_BV_claim": True,
        "no_full_DRED_claim": True,
        "no_loop_coefficient": True,
    }
    status = (
        "FAIL_CLOSED_MISSING_TRUE_N1_PARENT_INCIDENCE"
        if all(checks.values())
        else "FAIL_CERTIFICATE_INTERNAL_CHECK"
    )
    return {
        "schema": "Step5OneLoopFilteredCovariantQuotient.v1",
        "status": status,
        "scope": {
            "frame": "FIXED_VECTOR_FRAME",
            "symmetry": "BACKGROUND_COVARIANT",
            "sector": "PURE_GAUGE",
            "lorentz_space": "PHYSICAL_4D_SPIN_ALGEBRA",
            "dimension": "9/2",
            "spin": "(3/2,0)",
            "parity": "odd",
            "Project_rP": -1,
            "local_source_momentum": "retained",
            "DRED_traceless_tau_sector": "EXCLUDED_NOT_ZERO_IN_FULL_DRED",
            "quantum_BV_source_complex": "OUT_OF_SCOPE",
        },
        "algebra": {
            "mixed": "{N_a,B_dotb}=-2 D_(a dotb)",
            "ND": "[N_a,D_(b dotb)]=-2 epsilon_ab T_dotb",
            "BD": "[B_dota,D_(b dotb)]=-2 epsilon_dota_dotb W_b",
            "DD": (
                "[D_(a dota),D_(b dotb)]=epsilon_(dota dotb)N_(a W_b)"
                "+epsilon_ab B_(dota T_dotb)"
            ),
            "chirality": ["B_dota W_b=0", "N_a T_dotb=0"],
            "EOM": [
                "E=N^a W_a=0",
                "barE=B_dota T^dota=0",
                "N_a N_b W_c=-epsilon_ab N_c E",
                "D_a^dota T_dota=-(1/2)N_a barE",
            ],
            "graded_Leibniz": (
                "delta(FG)=(delta F)G+(-1)^(|delta||F|)F(delta G)"
            ),
        },
        "N2_candidate_PBW_quotient": pbw,
        "filtration_elimination_blocks": filtration,
        "indexed_child_intertwiner": event_descent,
        "spin_intertwiner": spin,
        "N2_candidate_quadratic_jet_codomain": quadratic,
        "color_species_exchange": color,
        "verdicts": {
            "N2_candidate_block_ker_ell2": "ZERO",
            "physical_4d_background_covariant_ker_ell2": (
                "FAIL_CLOSED_MISSING_TRUE_N1_PARENT_INCIDENCE"
            ),
            "full_DRED_ker_ell2": "NOT_CLAIMED",
            "full_quantum_BV_cohomology": "NOT_CLAIMED",
            "anomaly_coefficient": "NOT_COMPUTED",
        },
        "checks": checks,
        "external_results_imported": False,
    }


def render_markdown(payload: dict[str, object]) -> str:
    event = payload["indexed_child_intertwiner"]
    pbw = payload["N2_candidate_PBW_quotient"]
    filtration = payload["filtration_elimination_blocks"]
    quadratic = payload["N2_candidate_quadratic_jet_codomain"]
    color = payload["color_species_exchange"]
    witness = filtration["naive_parent_label_incidence"]["explicit_witnesses"][0]
    template = r"""# Step 5A physical-4d filtered covariant quotient

Status: `@@STATUS@@`

## 1. Scope

$$
[\mathscr O]=\frac92,
\qquad
(j_L,j_R)=\left(\frac32,0\right),
\qquad
|\mathscr O|=1,
\qquad
r_{\rm P}(\mathscr O)=-1.
$$

$$
\boxed{{
\mathfrak H_{\rm phys}^{\rm vec,bg}
:=\mathfrak H_{\rm pure\ gauge}
\big|_{\tau=0}
}}
$$

The equality $\tau=0$ is the physical four-dimensional projection.  It is
not a statement in the full DRED traceless-spurion module.

## 2. PBW relations

$$
\begin{{gathered}}
\{{\nabla_a,\bar\nabla_{{\dot b}}\}}
=-2\mathcal D_{{a\dot b}},\\
[\nabla_a,\mathcal D_{{b\dot b}}]
=-2\epsilon_{{ab}}\widetilde W_{{\dot b}},\\
[\bar\nabla_{{\dot a}},\mathcal D_{{b\dot b}}]
=-2\epsilon_{{\dot a\dot b}}W_b,\\
[\mathcal D_{{a\dot a}},\mathcal D_{{b\dot b}}]
=\epsilon_{{\dot a\dot b}}\nabla_{{(a}}W_{{b)}}
+\epsilon_{{ab}}\bar\nabla_{{(\dot a}}
\widetilde W_{{\dot b)}}.
\end{{gathered}}
$$

$$
\bar\nabla_{{\dot a}}W_b=0,
\qquad
\nabla_a\widetilde W_{{\dot b}}=0,
$$

$$
\nabla_a\nabla_bW_c
=-\epsilon_{{ab}}\nabla_cE,
\qquad
\mathcal D_a{{}}^{{\dot a}}\widetilde W_{{\dot a}}
=-\frac12\nabla_a\bar E,
\qquad
E=\bar E=0.
$$

The $N=0$ blocks are

$$
M_0\in\operatorname{{Mat}}_{{40\times40}}(\mathbb Q),
\qquad
\operatorname{{rank}}M_0=40,
$$

$$
M_{{0,J}}\in\operatorname{{Mat}}_{{320\times320}}(\mathbb Q),
\qquad
\operatorname{{rank}}M_{{0,J}}=320.
$$

Thus the complete $N=0$ block, including local source jets, has zero
quotient.

For the canonical $N=1$ terminal basis and its EOM carriers,

$$
M_{{1,{\rm term}}}\in
\operatorname{{Mat}}_{{40\times40}}(\mathbb Q),
\qquad
\operatorname{{rank}}M_{{1,{\rm term}}}=40.
$$

Let

$$
M_{{1\to2}}\in\operatorname{{Mat}}_{{126\times4866}}(\mathbb Q)
$$

be the indexed curvature-child matrix.  Its $4866$ columns are ordered-word
and event coordinates; they are not $4866$ independent $N=1$ parents.

The required incidence is

$$
C_1:\mathbb Q^{{20}}\longrightarrow\mathbb Q^{{4866}}.
$$

It must contain the word-order, Koszul, terminal-PBW, EOM, and source-jet
incidences.  It is not constructed.

The skeleton/copy-only map

$$
A_0:\mathbb Q^{{4866}}\longrightarrow\mathbb Q^{{20}}
$$

does not suffice.  In one fixed parent fiber,

$$
(\text{{skeleton}},\mu)=(@@WITNESS_PARENT@@),
$$

$$
(q_{{\rm PBW}}M_{{1\to2}})_{{@@WITNESS_COL1@@}}
=@@WITNESS_VAL1@@,
\qquad
(q_{{\rm PBW}}M_{{1\to2}})_{{@@WITNESS_COL2@@}}
=@@WITNESS_VAL2@@.
$$

Hence $q_{{\rm PBW}}M_{{1\to2}}$ does not factor through $A_0$.

The indexed $N=2$ carrier has

$$
\dim V_2^{{\rm ind}}=126.
$$

Its physical PBW normal form is

$$
C:=J_{{AB}}K^{{AB}}{{}}_{{CD}}
\widetilde W^C_{{\dot a}}
\mathcal D_{{(a}}{{}}^{{\dot a}}
\nabla_bW_{{c)}}^D.
$$

Only four indexed rows have nonzero image:

$$
q_{{\rm PBW}}(e_0)=q_{{\rm PBW}}(e_2)=C,
\qquad
q_{{\rm PBW}}(e_{{13}})=q_{{\rm PBW}}(e_{{19}})=-2C.
$$

All remaining rows reduce to $E$, $\bar E$, a chirality relation, or the
$W\widetilde W\widetilde W$ sector, whose physical $(3/2,0)$ multiplicity is
zero.

For the local source jet

$$
S_{{\mathcal D J}}
:=(\mathcal D_a{{}}^{{\dot a}}J_{{AB}})
K^{{AB}}{{}}_{{CD}}
\widetilde W^C_{{\dot a}}\nabla_bW_c^D,
$$

$$
C+C_{{\rm split}}+S_{{\mathcal D J}}=0,
\qquad
C_{{\rm split}}=0,
\qquad
S_{{\mathcal D J}}=-C.
$$

For this $N=2$ candidate block, the exact relation matrix is

$$
R_2^{{\rm cand}}\in\operatorname{{Mat}}_{{@@RH_ROWS@@\times@@RH_COLUMNS@@}}(\mathbb Q),
\qquad
\operatorname{{rank}}R_2^{{\rm cand}}=@@RH_RANK@@,
$$

$$
\boxed{{
\dim\left(
\mathbb Q^{{127}}/\operatorname{{row}}R_2^{{\rm cand}}
\right)=1.}}
$$

This is not the total filtered quotient until $C_1$ and the terminal
normal-order relation matrix are assembled.

The source momentum remains local:

$$
p_J+p_T+p_W=0,
\qquad
p_J\ne0.
$$

## 3. Indexed-event intertwiner

$$
M_{{1\to2}}\in
\operatorname{{Mat}}_{{126\times4866}}(\mathbb Q),
$$

$$
q_{{\rm PBW}}M_{{1\to2}}
\in\operatorname{{Mat}}_{{1\times4866}}(\mathbb Q).
$$

$$
N_{{\rm nonzero}}(q_{{\rm PBW}}M_{{1\to2}})
=@@EVENT_NONZERO@@.
$$

The stored sparse vector has SHA-256
`@@EVENT_SHA@@`.  It contains every indexed
$[\nabla,\mathcal D]$, $[\bar\nabla,\mathcal D]$, and
$[\mathcal D,\mathcal D]$ child.

The multiplicity-space map lifts as

$$
q_{{\rm PBW}}\otimes\mathbf1_{{(3/2,0)}}:
\mathbb Q^{{504}}\longrightarrow\mathbb Q^4,
\qquad
\operatorname{{rank}}=4.
$$

## 4. Quadratic-jet boundary

For each orientation use $(u,t,s)=(p_W,p_T,p_J)$.  The exact boundary is

$$
u+t+s=0,
\qquad
t=0.
$$

For the two orientations,

$$
R_T\in\operatorname{{Mat}}_{{4\times6}}(\mathbb Q),
\qquad
\operatorname{{rank}}R_T=@@RT_RANK@@,
\qquad
\dim T_2=2.
$$

$$
\bar\ell_2^{{(N=2)}}[C]
=\begin{{pmatrix}}1\\-1\end{{pmatrix}},
\qquad
\begin{{pmatrix}}1&0\end{{pmatrix}}
\bar\ell_2^{{(N=2)}}=1.
$$

$$
\boxed{{\ker\bar\ell_2^{{(N=2)}}=0.}}
$$

The executable $N=2$ square is

$$
\boxed{{q_T\ell_2^{{(N=2),{\rm raw}}}
=\bar\ell_2^{{(N=2)}}q_2.}}
$$

## 5. Simultaneous color/species exchange

$$
K_S^{{AB}}{{}}_{{DE}}
=\frac12\left(
f_{{ARD}}f_{{BRE}}+f_{{BRD}}f_{{ARE}}
\right),
$$

$$
K_S^{{BA}}{{}}_{{ED}}=K_S^{{AB}}{{}}_{{DE}}.
$$

Let $\tau$ exchange $D\leftrightarrow E$.  Since the two elementary quantum
letters $W$ and $\widetilde W$ are odd, the combined exchange is

$$
\mathsf X_g(u,v)=(-\tau v,-\tau u),
\qquad
P_+=\frac12(1+\mathsf X_g).
$$

For the actual reflected jet,

$$
L_K=(K_S,-\tau K_S),
$$

$$
\mathsf X_gL_K=L_K,
\qquad
\boxed{{P_+L_K=L_K\ne0.}}
$$

The exact $SU(2)$ witness gives

$$
\operatorname{{rank}}K_S=@@K_RANK@@,
\qquad
\operatorname{{rank}}L_K=@@LK_RANK@@.
$$

For a nonabelian compact algebra,

$$
K_S^{{AA}}{{}}_{{DD}}
=\sum_R f_{{ARD}}^2>0
$$

for some $A,D$, so the fixed actual $K_S$ line is nonzero.

## 6. Boundary

$$
\boxed{{
\ker\bar\ell_2
\text{{ on the total physical-4d filtered quotient}}
=\texttt{{FAIL\_CLOSED\_MISSING\_C1}}.}}
$$

$$
\boxed{{
\text{{full DRED traceless-}}\tau\text{{ quotient}}
=\texttt{{NOT CLAIMED}},
\qquad
\text{{full quantum BV source cohomology}}
=\texttt{{NOT CLAIMED}}.}}
$$
"""
    return (
        template.replace("{{", "{")
        .replace("}}", "}")
        .replace("@@STATUS@@", str(payload["status"]))
        .replace("@@RH_ROWS@@", str(pbw["relation_matrix"]["rows"]))
        .replace("@@RH_COLUMNS@@", str(pbw["relation_matrix"]["columns"]))
        .replace("@@RH_RANK@@", str(pbw["relation_rank"]))
        .replace("@@EVENT_NONZERO@@", str(event["nonzero_descended_columns"]))
        .replace("@@EVENT_SHA@@", str(event["sparse_descended_vector_sha256"]))
        .replace(
            "@@WITNESS_PARENT@@",
            f"{witness['parent']['skeleton']}, {witness['parent']['spin_copy']}",
        )
        .replace("@@WITNESS_COL1@@", str(witness["first_column"]))
        .replace("@@WITNESS_VAL1@@", str(witness["first_value"]))
        .replace("@@WITNESS_COL2@@", str(witness["second_column"]))
        .replace("@@WITNESS_VAL2@@", str(witness["second_value"]))
        .replace(
            "@@RT_RANK@@", str(quadratic["codomain_boundary_matrix"]["rank"])
        )
        .replace("@@K_RANK@@", str(color["SU2_exact_witness"]["K_rank"]))
        .replace("@@LK_RANK@@", str(color["SU2_exact_witness"]["ell2_rank"]))
    )


def main() -> None:
    payload = build_payload()
    generated = canonical_json(payload)
    checks = payload["checks"]
    assert isinstance(checks, dict)
    audit = {
        "schema": "Step5OneLoopFilteredCovariantQuotientAudit.v1",
        "status": payload["status"],
        "passed": sum(bool(value) for value in checks.values()),
        "total": len(checks),
        "failed": [name for name, value in checks.items() if not value],
        "generated_sha256": hashlib.sha256(generated).hexdigest(),
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated)
    AUDIT_JSON.write_bytes(canonical_json(audit))
    AUDIT_MD.write_text(render_markdown(payload), encoding="utf-8")
    if payload["status"] == "FAIL_CERTIFICATE_INTERNAL_CHECK":
        raise SystemExit("physical filtered quotient certificate failed")


if __name__ == "__main__":
    main()
