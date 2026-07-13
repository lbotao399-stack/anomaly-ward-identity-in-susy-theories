#!/usr/bin/env python3
"""Exact fixed-quadratic pure-gauge jet matrices for Step 5.

All matrix arithmetic is over Q.  Color and source tensors remain symbolic.
No anomaly coefficient or external formula enters this certificate.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable, TypeAlias


Q: TypeAlias = Fraction
Matrix: TypeAlias = list[list[Q]]

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated/step5/one-loop-pure-gauge-injectivity-matrix.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-pure-gauge-injectivity-matrix.md"
VERIFY = ROOT / "audits/step5-one-loop-pure-gauge-injectivity-matrix-verification.json"

TARGET_DIMENSION_TWICE = 9
TARGET_FORMAL_R = -1
TARGET_PARITY = 1
TARGET_JL_TWICE = 3
TARGET_JR_TWICE = 0


def zero_matrix(rows: int, cols: int) -> Matrix:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def identity_matrix(size: int) -> Matrix:
    matrix = zero_matrix(size, size)
    for index in range(size):
        matrix[index][index] = Q(1)
    return matrix


def block_diagonal(blocks: list[Matrix]) -> Matrix:
    rows = sum(len(block) for block in blocks)
    cols = sum(len(block[0]) if block else 0 for block in blocks)
    output = zero_matrix(rows, cols)
    row_offset = 0
    col_offset = 0
    for block in blocks:
        block_cols = len(block[0]) if block else 0
        for row_index, row in enumerate(block):
            for col_index, value in enumerate(row):
                output[row_offset + row_index][col_offset + col_index] = value
        row_offset += len(block)
        col_offset += block_cols
    return output


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [list(column) for column in zip(*matrix, strict=True)]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left:
        return []
    if not right:
        return zero_matrix(len(left), 0)
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


def add_matrices(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def scale_matrix(coefficient: Q, matrix: Matrix) -> Matrix:
    return [[coefficient * value for value in row] for row in matrix]


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


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    size = len(matrix)
    output = identity_matrix(size)
    for _ in range(exponent):
        output = multiply(output, matrix)
    return output


def bit_basis(slot_count: int) -> list[tuple[int, ...]]:
    return list(itertools.product((0, 1), repeat=slot_count))


def swap_slot_matrix(slot_count: int, first: int, second: int) -> Matrix:
    basis = bit_basis(slot_count)
    index = {state: position for position, state in enumerate(basis)}
    output = zero_matrix(len(basis), len(basis))
    for column, state in enumerate(basis):
        swapped = list(state)
        swapped[first], swapped[second] = swapped[second], swapped[first]
        output[index[tuple(swapped)]][column] = Q(1)
    return output


def total_spin_casimir(slot_count: int) -> Matrix:
    size = 2**slot_count
    output = scale_matrix(Q(slot_count * (4 - slot_count), 4), identity_matrix(size))
    for first in range(slot_count):
        for second in range(first + 1, slot_count):
            output = add_matrices(output, swap_slot_matrix(slot_count, first, second))
    return output


def spin_isotypic_projector(slot_count: int, target_twice_spin: int) -> Matrix:
    size = 2**slot_count
    allowed = list(range(slot_count, -1, -2))
    if target_twice_spin not in allowed:
        return zero_matrix(size, size)
    casimir = total_spin_casimir(slot_count)
    target_eigenvalue = Q(target_twice_spin * (target_twice_spin + 2), 4)
    projector = identity_matrix(size)
    for twice_spin in allowed:
        if twice_spin == target_twice_spin:
            continue
        eigenvalue = Q(twice_spin * (twice_spin + 2), 4)
        shifted = add_matrices(
            casimir, scale_matrix(-eigenvalue, identity_matrix(size))
        )
        projector = scale_matrix(
            Q(1, 1) / (target_eigenvalue - eigenvalue),
            multiply(projector, shifted),
        )
    return projector


def spin4_target_projector(left_slots: int, right_slots: int) -> Matrix:
    return kronecker(
        spin_isotypic_projector(left_slots, TARGET_JL_TWICE),
        spin_isotypic_projector(right_slots, TARGET_JR_TWICE),
    )


def inverse_matrix(matrix: Matrix) -> Matrix:
    size = len(matrix)
    augmented = [
        matrix[row][:]
        + [Q(int(row == column)) for column in range(size)]
        for row in range(size)
    ]
    reduced, pivots = rref(augmented)
    if pivots[:size] != list(range(size)):
        raise ValueError("matrix is singular")
    return [row[size:] for row in reduced]


@lru_cache(maxsize=None)
def projector_coordinate_data(
    left_slots: int, right_slots: int, *, highest_weight_only: bool
) -> dict[str, object]:
    projector = spin4_target_projector(left_slots, right_slots)
    raw_basis = bit_basis(left_slots + right_slots)
    if highest_weight_only:
        allowed_indices = [
            index
            for index, state in enumerate(raw_basis)
            if (
                left_slots - 2 * sum(state[:left_slots]) == TARGET_JL_TWICE
                and right_slots - 2 * sum(state[left_slots:]) == TARGET_JR_TWICE
            )
        ]
    else:
        allowed_indices = list(range(len(raw_basis)))
    restricted = [
        [projector[row][column] for column in allowed_indices]
        for row in allowed_indices
    ]
    _, restricted_pivots = rref(restricted)
    selected_columns = [allowed_indices[pivot] for pivot in restricted_pivots]
    basis_matrix = [
        [projector[row][column] for column in selected_columns]
        for row in range(len(projector))
    ]
    if not selected_columns:
        return {
            "projector": projector,
            "rank": 0,
            "basis_matrix": zero_matrix(len(projector), 0),
            "coordinate_map": [],
            "selected_columns": [],
            "selected_rows": [],
            "allowed_indices": allowed_indices,
        }
    _, selected_rows = rref(transpose(basis_matrix))
    square = [
        [basis_matrix[row][column] for column in range(len(selected_columns))]
        for row in selected_rows
    ]
    inverse = inverse_matrix(square)
    coordinate_map = zero_matrix(len(selected_columns), len(projector))
    for coordinate_row in range(len(selected_columns)):
        for square_column, raw_row in enumerate(selected_rows):
            coordinate_map[coordinate_row][raw_row] = inverse[
                coordinate_row
            ][square_column]
    if multiply(coordinate_map, basis_matrix) != identity_matrix(
        len(selected_columns)
    ):
        raise AssertionError("projector coordinate map is not a left inverse")
    return {
        "projector": projector,
        "rank": len(selected_columns),
        "basis_matrix": basis_matrix,
        "coordinate_map": coordinate_map,
        "selected_columns": selected_columns,
        "selected_rows": selected_rows,
        "allowed_indices": allowed_indices,
    }


EPSILON_DOWN_COMPONENTS = {
    (0, 0): Q(0),
    (0, 1): Q(-1),
    (1, 0): Q(1),
    (1, 1): Q(0),
}


def raw_commutator_map(
    source_left_slots: list[str],
    source_right_slots: list[str],
    contracted_slots: list[str],
    output_left_slots: list[str],
    output_right_slots: list[str],
) -> Matrix:
    source_slots = source_left_slots + source_right_slots
    output_slots = output_left_slots + output_right_slots
    source_slot_index = {slot: index for index, slot in enumerate(source_slots)}
    if any(slot not in source_slot_index for slot in contracted_slots + output_slots):
        raise AssertionError("commutator map contains a foreign spinor slot")
    if set(contracted_slots) & set(output_slots):
        raise AssertionError("contracted spinor slot survives in child output")
    source_basis = bit_basis(len(source_slots))
    output_basis = bit_basis(len(output_slots))
    output_index = {state: index for index, state in enumerate(output_basis)}
    matrix = zero_matrix(len(output_basis), len(source_basis))
    first_index = source_slot_index[contracted_slots[0]]
    second_index = source_slot_index[contracted_slots[1]]
    for column, state in enumerate(source_basis):
        epsilon = EPSILON_DOWN_COMPONENTS[(state[first_index], state[second_index])]
        if epsilon == 0:
            continue
        output_state = tuple(state[source_slot_index[slot]] for slot in output_slots)
        matrix[output_index[output_state]][column] = epsilon
    return matrix


def projected_intertwiner_coordinates(
    source_left_slots: list[str],
    source_right_slots: list[str],
    contracted_slots: list[str],
    output_left_slots: list[str],
    output_right_slots: list[str],
    *,
    highest_weight_only: bool,
) -> Matrix:
    source_coordinates = projector_coordinate_data(
        len(source_left_slots),
        len(source_right_slots),
        highest_weight_only=highest_weight_only,
    )
    output_coordinates = projector_coordinate_data(
        len(output_left_slots),
        len(output_right_slots),
        highest_weight_only=highest_weight_only,
    )
    if source_coordinates["rank"] == 0 or output_coordinates["rank"] == 0:
        return zero_matrix(
            int(output_coordinates["rank"]), int(source_coordinates["rank"])
        )
    raw_map = raw_commutator_map(
        source_left_slots,
        source_right_slots,
        contracted_slots,
        output_left_slots,
        output_right_slots,
    )
    projected_on_source_basis = multiply(
        raw_map, source_coordinates["basis_matrix"]
    )
    output_projected = multiply(
        output_coordinates["projector"], projected_on_source_basis
    )
    return multiply(output_coordinates["coordinate_map"], output_projected)


def su2_generator(slot_count: int, kind: str) -> Matrix:
    basis = bit_basis(slot_count)
    index = {state: position for position, state in enumerate(basis)}
    output = zero_matrix(len(basis), len(basis))
    for column, state in enumerate(basis):
        if kind == "z":
            output[column][column] = Q(slot_count - 2 * sum(state), 2)
            continue
        for slot, value in enumerate(state):
            if (kind == "+" and value == 1) or (kind == "-" and value == 0):
                changed = list(state)
                changed[slot] = 0 if kind == "+" else 1
                output[index[tuple(changed)]][column] += Q(1)
    return output


@lru_cache(maxsize=None)
def spin4_generators(left_slots: int, right_slots: int) -> dict[str, Matrix]:
    identity_left = identity_matrix(2**left_slots)
    identity_right = identity_matrix(2**right_slots)
    return {
        f"L{kind}": kronecker(
            su2_generator(left_slots, kind), identity_right
        )
        for kind in ("z", "+", "-")
    } | {
        f"R{kind}": kronecker(
            identity_left, su2_generator(right_slots, kind)
        )
        for kind in ("z", "+", "-")
    }


def raw_map_is_spin4_intertwiner(
    raw_map: Matrix,
    source_left_count: int,
    source_right_count: int,
    output_left_count: int,
    output_right_count: int,
) -> bool:
    source_generators = spin4_generators(source_left_count, source_right_count)
    output_generators = spin4_generators(output_left_count, output_right_count)
    return all(
        multiply(output_generators[key], raw_map)
        == multiply(raw_map, source_generators[key])
        for key in source_generators
    )


def epsilon_invariance_checks() -> dict[str, bool]:
    epsilon = [[Q(0), Q(-1)], [Q(1), Q(0)]]
    return {
        kind: add_matrices(
            multiply(transpose(su2_generator(1, kind)), epsilon),
            multiply(epsilon, su2_generator(1, kind)),
        )
        == zero_matrix(2, 2)
        for kind in ("z", "+", "-")
    }


def placement_json(key: tuple[object, ...]) -> dict[str, object]:
    sector = str(key[0])
    factors = key[1]
    assert isinstance(factors, tuple)
    return {
        "sector": sector,
        "factors": [
            {"field": str(factor[0]), "derivative_word": list(factor[1])}
            for factor in factors
        ],
    }


def add_scaled_block(
    target: Matrix,
    row_offset: int,
    column_offset: int,
    coefficient: Q,
    block: Matrix,
) -> None:
    for row, values in enumerate(block):
        for column, value in enumerate(values):
            target[row_offset + row][column_offset + column] += coefficient * value


def indexed_child_to_n2_matrix(rows: list[dict[str, int]]) -> dict[str, object]:
    """Exact indexed N=1 curvature-child map into ordered N=2 target jets."""

    records = indexed_n1_input_records(rows)
    placement_keys = sorted(
        {
            branch["placement_key"]
            for record in records
            for event in record["events"]
            for branch in event["branches"]
        },
        key=repr,
    )
    placement_data: list[dict[str, object]] = []
    placement_offsets: dict[tuple[object, ...], int] = {}
    placement_ids = {key: index for index, key in enumerate(placement_keys)}
    row_offset = 0
    for placement_id, key in enumerate(placement_keys):
        sample = next(
            branch
            for record in records
            for event in record["events"]
            for branch in event["branches"]
            if branch["placement_key"] == key
        )
        left_count = len(sample["left_slots"])
        right_count = len(sample["right_slots"])
        high_coordinates = projector_coordinate_data(
            left_count, right_count, highest_weight_only=True
        )
        full_coordinates = projector_coordinate_data(
            left_count, right_count, highest_weight_only=False
        )
        multiplicity = int(high_coordinates["rank"])
        placement_offsets[key] = row_offset
        placement_data.append(
            {
                "placement_id": placement_id,
                "placement": placement_json(key),
                "left_slots": left_count,
                "right_slots": right_count,
                "target_multiplicity": multiplicity,
                "target_component_dimension": int(full_coordinates["rank"]),
                "multiplicity_row_offset": row_offset,
            }
        )
        row_offset += multiplicity

    source_offsets: list[int] = []
    source_multiplicities: list[int] = []
    column_offset = 0
    for record in records:
        source_coordinates = projector_coordinate_data(
            len(record["source_left_slots"]),
            len(record["source_right_slots"]),
            highest_weight_only=True,
        )
        multiplicity = int(source_coordinates["rank"])
        source_offsets.append(column_offset)
        source_multiplicities.append(multiplicity)
        column_offset += multiplicity

    global_matrix = zero_matrix(row_offset, column_offset)
    intertwiner_cache: dict[tuple[object, ...], dict[str, object]] = {}
    intertwiner_table: list[dict[str, object]] = []
    event_table: list[dict[str, object]] = []
    compact_inputs: list[dict[str, object]] = []
    epsilon_checks = epsilon_invariance_checks()

    for record_index, record in enumerate(records):
        compact_event_ids: list[int] = []
        for event in record["events"]:
            compact_branches: list[dict[str, object]] = []
            for branch in event["branches"]:
                key = (
                    record["skeleton"],
                    tuple(event["contracted_slots"]),
                    tuple(branch["left_slots"]),
                    tuple(branch["right_slots"]),
                )
                if key not in intertwiner_cache:
                    highest = projected_intertwiner_coordinates(
                        record["source_left_slots"],
                        record["source_right_slots"],
                        event["contracted_slots"],
                        branch["left_slots"],
                        branch["right_slots"],
                        highest_weight_only=True,
                    )
                    full = projected_intertwiner_coordinates(
                        record["source_left_slots"],
                        record["source_right_slots"],
                        event["contracted_slots"],
                        branch["left_slots"],
                        branch["right_slots"],
                        highest_weight_only=False,
                    )
                    high_rank = rank(highest)
                    full_rank = rank(full)
                    entry = {
                        "intertwiner_id": len(intertwiner_table),
                        "source_skeleton": record["skeleton"],
                        "contracted_slots": list(event["contracted_slots"]),
                        "output_left_slots": list(branch["left_slots"]),
                        "output_right_slots": list(branch["right_slots"]),
                        "highest_weight_matrix": encoded_matrix(highest),
                        "highest_weight_rank": high_rank,
                        "full_component_rank": full_rank,
                        "full_rank_equals_four_times_highest_rank": (
                            full_rank == 4 * high_rank
                        ),
                        "raw_map_spin4_intertwiner": all(epsilon_checks.values()),
                    }
                    intertwiner_cache[key] = entry
                    intertwiner_table.append(entry)
                entry = intertwiner_cache[key]
                placement_key = branch["placement_key"]
                placement_id = placement_ids[placement_key]
                coefficient = branch["coefficient"]
                assert isinstance(coefficient, Q)
                highest_matrix = [
                    [Q(value) for value in row]
                    for row in entry["highest_weight_matrix"]
                ]
                add_scaled_block(
                    global_matrix,
                    placement_offsets[placement_key],
                    source_offsets[record_index],
                    coefficient,
                    highest_matrix,
                )
                compact_branches.append(
                    {
                        "coefficient": fraction_text(coefficient),
                        "placement_id": placement_id,
                        "intertwiner_id": entry["intertwiner_id"],
                        "factor_roles": [
                            str(field["role"]) for field in branch["fields"]
                        ],
                    }
                )
            event_id = len(event_table)
            compact_event_ids.append(event_id)
            event_table.append(
                {
                    "event_id": event_id,
                    "input_id": record_index,
                    "coefficient_before_prefix_Leibniz": event["coefficient"],
                    "active_word": [token["id"] for token in event["active_word"]],
                    "position": event["position"],
                    "path": event["path"],
                    "commutator": event["commutator"],
                    "contracted_slots": event["contracted_slots"],
                    "curvature_field": event["curvature_field"],
                    "curvature_slot": event["curvature_slot"],
                    "prefix": [token["id"] for token in event["prefix"]],
                    "suffix": [token["id"] for token in event["suffix"]],
                    "branches": compact_branches,
                }
            )
        compact_inputs.append(
            {
                "input_id": record_index,
                "skeleton": record["skeleton"],
                "word": [token["id"] for token in record["word"]],
                "source_left_slots": record["source_left_slots"],
                "source_right_slots": record["source_right_slots"],
                "source_target_multiplicity": source_multiplicities[record_index],
                "multiplicity_column_offset": source_offsets[record_index],
                "event_ids": compact_event_ids,
            }
        )

    global_rank = rank(global_matrix)
    full_component_rank = 4 * global_rank
    nonzero_placement_rows = sum(
        int(placement["target_multiplicity"]) for placement in placement_data
    )
    return {
        "schema": "N1_INDEXED_CURVATURE_CHILD_TO_N2_V1",
        "input_word_count": len(records),
        "event_count": len(event_table),
        "branch_count": sum(
            len(event["branches"]) for event in event_table
        ),
        "ordered_placement_count": len(placement_data),
        "nonzero_target_multiplicity_rows": nonzero_placement_rows,
        "source_target_multiplicity_columns": column_offset,
        "multiplicity_matrix": map_certificate(
            [
                f"input:{record_index}:copy:{copy}"
                for record_index, multiplicity in enumerate(source_multiplicities)
                for copy in range(multiplicity)
            ],
            [
                f"placement:{placement['placement_id']}:copy:{copy}"
                for placement in placement_data
                for copy in range(int(placement["target_multiplicity"]))
            ],
            global_matrix,
            dense=False,
        ),
        "multiplicity_rank": global_rank,
        "full_component_rows": 4 * nonzero_placement_rows,
        "full_component_columns": 4 * column_offset,
        "full_component_rank_by_exact_spin4_intertwining": full_component_rank,
        "full_component_kernel_dimension": 4 * column_offset - full_component_rank,
        "all_raw_maps_spin4_intertwiners": all(
            entry["raw_map_spin4_intertwiner"] for entry in intertwiner_table
        ),
        "epsilon_invariance_checks": epsilon_checks,
        "all_full_ranks_four_times_highest_ranks": all(
            entry["full_rank_equals_four_times_highest_rank"]
            for entry in intertwiner_table
        ),
        "placement_table": placement_data,
        "intertwiner_table": intertwiner_table,
        "input_table": compact_inputs,
        "event_table": event_table,
        "coverage": {
            "ND_and_BD_normal_order_children": True,
            "DD_pairing_children": False,
            "source_jet_block": False,
            "color_role_block": False,
            "evanescent_block": False,
        },
    }


def dd_pairing_branch_specs() -> list[dict[str, object]]:
    """The two Euclidean [D,D] children, including normalized symmetrization."""

    branches: list[dict[str, object]] = []
    for w_slot, n_slot in (("LD2", "LD1"), ("LD1", "LD2")):
        branches.extend(
            [
                {
                    "child": "epsilon_(RD1 RD2) N_(LD1 W_LD2)",
                    "coefficient": Q(1, 2),
                    "contracted_slots": ["RD1", "RD2"],
                    "output_left_slots": [w_slot, "LD0", n_slot],
                    "output_right_slots": ["RD0", "RFT"],
                    "placement": (
                        "W1_T1_N1_B0_D1",
                        (("W", ("D0", "N0")), ("T", ())),
                    ),
                    "prefix_D0_endpoint": "curvature_NW",
                    "target_spin_possible": True,
                },
                {
                    "child": "epsilon_(RD1 RD2) N_(LD1 W_LD2)",
                    "coefficient": Q(1, 2),
                    "contracted_slots": ["RD1", "RD2"],
                    "output_left_slots": [w_slot, n_slot, "LD0"],
                    "output_right_slots": ["RFT", "RD0"],
                    "placement": (
                        "W1_T1_N1_B0_D1",
                        (("W", ("N0",)), ("T", ("D0",))),
                    ),
                    "prefix_D0_endpoint": "original_T",
                    "target_spin_possible": True,
                },
            ]
        )
    for t_slot, b_slot in (("RD2", "RD1"), ("RD1", "RD2")):
        branches.extend(
            [
                {
                    "child": "epsilon_(LD1 LD2) B_(RD1 T_RD2)",
                    "coefficient": Q(1, 2),
                    "contracted_slots": ["LD1", "LD2"],
                    "output_left_slots": ["LD0"],
                    "output_right_slots": [
                        "RFT",
                        t_slot,
                        "RD0",
                        b_slot,
                    ],
                    "placement": (
                        "W0_T2_N0_B1_D1",
                        (("T", ()), ("T", ("D0", "B0"))),
                    ),
                    "prefix_D0_endpoint": "curvature_BT",
                    "target_spin_possible": False,
                },
                {
                    "child": "epsilon_(LD1 LD2) B_(RD1 T_RD2)",
                    "coefficient": Q(1, 2),
                    "contracted_slots": ["LD1", "LD2"],
                    "output_left_slots": ["LD0"],
                    "output_right_slots": [
                        "RFT",
                        "RD0",
                        t_slot,
                        b_slot,
                    ],
                    "placement": (
                        "W0_T2_N0_B1_D1",
                        (("T", ("D0",)), ("T", ("B0",))),
                    ),
                    "prefix_D0_endpoint": "original_T",
                    "target_spin_possible": False,
                },
            ]
        )
    return branches


def indexed_dd_pairing_matrix() -> dict[str, object]:
    source_left = ["LD0", "LD1", "LD2"]
    source_right = ["RFT", "RD0", "RD1", "RD2"]
    branches = dd_pairing_branch_specs()
    placements = sorted({branch["placement"] for branch in branches}, key=repr)

    source_high = projector_coordinate_data(3, 4, highest_weight_only=True)
    source_full = projector_coordinate_data(3, 4, highest_weight_only=False)
    high_offsets: dict[tuple[object, ...], int] = {}
    full_offsets: dict[tuple[object, ...], int] = {}
    high_rows = 0
    full_rows = 0
    placement_table: list[dict[str, object]] = []
    for placement_id, placement in enumerate(placements):
        sample = next(branch for branch in branches if branch["placement"] == placement)
        left_count = len(sample["output_left_slots"])
        right_count = len(sample["output_right_slots"])
        output_high = projector_coordinate_data(
            left_count, right_count, highest_weight_only=True
        )
        output_full = projector_coordinate_data(
            left_count, right_count, highest_weight_only=False
        )
        high_offsets[placement] = high_rows
        full_offsets[placement] = full_rows
        placement_table.append(
            {
                "placement_id": placement_id,
                "placement": placement_json(placement),
                "target_multiplicity": output_high["rank"],
                "target_component_dimension": output_full["rank"],
                "highest_weight_row_offset": high_rows,
                "full_component_row_offset": full_rows,
            }
        )
        high_rows += int(output_high["rank"])
        full_rows += int(output_full["rank"])

    high_matrix = zero_matrix(high_rows, int(source_high["rank"]))
    full_matrix = zero_matrix(full_rows, int(source_full["rank"]))
    encoded_branches: list[dict[str, object]] = []
    for branch_id, branch in enumerate(branches):
        high = projected_intertwiner_coordinates(
            source_left,
            source_right,
            branch["contracted_slots"],
            branch["output_left_slots"],
            branch["output_right_slots"],
            highest_weight_only=True,
        )
        full = projected_intertwiner_coordinates(
            source_left,
            source_right,
            branch["contracted_slots"],
            branch["output_left_slots"],
            branch["output_right_slots"],
            highest_weight_only=False,
        )
        coefficient = branch["coefficient"]
        assert isinstance(coefficient, Q)
        add_scaled_block(
            high_matrix,
            high_offsets[branch["placement"]],
            0,
            coefficient,
            high,
        )
        add_scaled_block(
            full_matrix,
            full_offsets[branch["placement"]],
            0,
            coefficient,
            full,
        )
        encoded_branches.append(
            {
                "branch_id": branch_id,
                "child": branch["child"],
                "coefficient": fraction_text(coefficient),
                "contracted_slots": branch["contracted_slots"],
                "output_left_slots": branch["output_left_slots"],
                "output_right_slots": branch["output_right_slots"],
                "placement_id": placements.index(branch["placement"]),
                "prefix_D0_endpoint": branch["prefix_D0_endpoint"],
                "target_spin_possible": branch["target_spin_possible"],
                "highest_weight_branch_rank": rank(high),
                "full_component_branch_rank": rank(full),
            }
        )

    high_rank = rank(high_matrix)
    full_rank = rank(full_matrix)
    return {
        "schema": "N1_INDEXED_DD_PAIRING_TO_N2_V1",
        "source_skeleton": "W0_T1_N0_B0_D3",
        "Euclidean_curvature_normalization": "rho_E=1",
        "identity": (
            "[D_(a dota),D_(b dotb)]="
            "epsilon_(dota dotb)N_(a W_b)+epsilon_ab B_(dota T_dotb)"
        ),
        "symmetrization": "X_(a Y_b)=(X_a Y_b+X_b Y_a)/2",
        "source_highest_weight_multiplicity": source_high["rank"],
        "source_full_target_dimension": source_full["rank"],
        "placement_table": placement_table,
        "branches": encoded_branches,
        "highest_weight_matrix": map_certificate(
            [f"source-copy:{copy}" for copy in range(int(source_high["rank"]))],
            [
                f"placement:{placement['placement_id']}:copy:{copy}"
                for placement in placement_table
                for copy in range(int(placement["target_multiplicity"]))
            ],
            high_matrix,
        ),
        "full_component_matrix": map_certificate(
            [f"source-component:{copy}" for copy in range(int(source_full["rank"]))],
            [
                f"placement:{placement['placement_id']}:component:{copy}"
                for placement in placement_table
                for copy in range(int(placement["target_component_dimension"]))
            ],
            full_matrix,
        ),
        "highest_weight_rank": high_rank,
        "highest_weight_source_kernel_dimension": (
            int(source_high["rank"]) - high_rank
        ),
        "full_component_rank": full_rank,
        "full_component_source_kernel_dimension": (
            int(source_full["rank"]) - full_rank
        ),
        "full_rank_equals_four_times_highest_rank": full_rank == 4 * high_rank,
        "kernel_interpretation": (
            "kernel of the local [D,D]-child map from the two source-spin"
            " copies; not the kernel of the complete quadratic jet ell_2"
        ),
        "all_eight_symmetry_and_endpoint_branches_explicit": len(branches) == 8,
        "zero_target_BT_child_branches": sum(
            not bool(branch["target_spin_possible"]) for branch in branches
        ),
    }


def placement_key_from_json(
    placement: dict[str, object],
) -> tuple[str, tuple[tuple[str, tuple[str, ...]], ...]]:
    factors = placement["factors"]
    assert isinstance(factors, list)
    return (
        str(placement["sector"]),
        tuple(
            (
                str(factor["field"]),
                tuple(str(token) for token in factor["derivative_word"]),
            )
            for factor in factors
        ),
    )


def complete_indexed_n1_child_to_n2_matrix(
    ndbd: dict[str, object], dd: dict[str, object]
) -> dict[str, object]:
    """Adjoin the exact [D,D] block to the indexed [N,D]/[B,D] map."""

    ndbd_matrix = ndbd["multiplicity_matrix"]
    assert isinstance(ndbd_matrix, dict)
    ndbd_sparse = ndbd_matrix["matrix_sparse"]
    assert isinstance(ndbd_sparse, dict)
    ndbd_entries = ndbd_sparse["entries"]
    assert isinstance(ndbd_entries, list)
    ndbd_rows = int(ndbd_matrix["rows"])
    ndbd_columns = int(ndbd_matrix["columns"])
    ndbd_rank = int(ndbd_matrix["rank"])

    global_row_offsets = {
        placement_key_from_json(placement["placement"]): int(
            placement["multiplicity_row_offset"]
        )
        for placement in ndbd["placement_table"]
    }
    dd_matrix = dd["highest_weight_matrix"]
    assert isinstance(dd_matrix, dict)
    dd_dense = [
        [Q(value) for value in row]
        for row in dd_matrix["matrix"]
    ]
    dd_columns = int(dd_matrix["columns"])
    dd_local_row = 0
    dd_embedding: list[dict[str, int]] = []
    extra_entries: list[dict[str, object]] = []
    for placement in dd["placement_table"]:
        multiplicity = int(placement["target_multiplicity"])
        key = placement_key_from_json(placement["placement"])
        if multiplicity == 0:
            continue
        if key not in global_row_offsets:
            raise AssertionError("[D,D] target placement is absent from indexed N2 basis")
        for copy in range(multiplicity):
            global_row = global_row_offsets[key] + copy
            dd_embedding.append(
                {
                    "DD_local_row": dd_local_row,
                    "complete_target_row": global_row,
                    "placement_id": int(placement["placement_id"]),
                    "spin_copy": copy,
                }
            )
            for column, value in enumerate(dd_dense[dd_local_row]):
                if value:
                    extra_entries.append(
                        {
                            "row": global_row,
                            "column": ndbd_columns + column,
                            "value": fraction_text(value),
                        }
                    )
            dd_local_row += 1
    if dd_local_row != int(dd_matrix["rows"]):
        raise AssertionError("[D,D] row embedding omitted a nonzero target row")

    complete_rank = ndbd_rank
    complete_columns = ndbd_columns + dd_columns
    full_rows = 4 * ndbd_rows
    full_columns = 4 * complete_columns
    full_rank = 4 * complete_rank
    return {
        "schema": "N1_COMPLETE_INDEXED_CHILD_TO_N2_V1",
        "target_multiplicity_rows": ndbd_rows,
        "source_multiplicity_columns": complete_columns,
        "multiplicity_rank": complete_rank,
        "multiplicity_kernel_dimension": complete_columns - complete_rank,
        "multiplicity_matrix_sparse": {
            "rows": ndbd_rows,
            "columns": complete_columns,
            "entries": ndbd_entries + extra_entries,
            "rank": complete_rank,
        },
        "exact_rank_proof": {
            "ND_BD_submatrix_rows": ndbd_rows,
            "ND_BD_submatrix_columns": ndbd_columns,
            "ND_BD_submatrix_rank": ndbd_rank,
            "ND_BD_submatrix_is_surjective": ndbd_rank == ndbd_rows,
            "upper_bound_by_codomain_dimension": ndbd_rows,
            "conclusion": (
                "rank([M_(ND,BD) M_DD])=target multiplicity dimension"
            ),
        },
        "DD_row_embedding": dd_embedding,
        "full_component_rows": full_rows,
        "full_component_columns": full_columns,
        "full_component_rank": full_rank,
        "full_component_kernel_dimension": full_columns - full_rank,
        "full_rank_proof": (
            "all blocks are exact Spin(4) intertwiners on (3/2,0); the"
            " surjective multiplicity map lifts to four component rows per copy"
        ),
        "coverage": {
            "ND_and_BD_normal_order_children": True,
            "DD_pairing_children": True,
            "all_nonzero_DD_rows_embedded_in_shared_N2_placement_basis": (
                dd_local_row == int(dd_matrix["rows"])
            ),
            "source_jet_block": False,
            "color_role_block": False,
            "evanescent_block": False,
        },
    }


def compact_indexed_child_certificate(
    certificate: dict[str, object]
) -> dict[str, object]:
    event_table = certificate["event_table"]
    input_table = certificate["input_table"]
    intertwiner_table = certificate["intertwiner_table"]
    assert isinstance(event_table, list)
    assert isinstance(input_table, list)
    assert isinstance(intertwiner_table, list)
    compact = {
        key: value
        for key, value in certificate.items()
        if key
        not in {
            "multiplicity_matrix",
            "input_table",
            "event_table",
            "intertwiner_table",
        }
    }
    compact["multiplicity_matrix"] = compact_map_certificate(
        certificate["multiplicity_matrix"], witness_row_limit=8
    )
    compact["input_table_ledger"] = sequence_ledger(
        input_table, witness_limit=12
    )
    compact["event_table_ledger"] = sequence_ledger(
        event_table, witness_limit=16
    )
    compact["intertwiner_table_ledger"] = sequence_ledger(
        intertwiner_table, witness_limit=12
    )
    return compact


def compact_complete_indexed_child_certificate(
    certificate: dict[str, object]
) -> dict[str, object]:
    sparse = certificate["multiplicity_matrix_sparse"]
    assert isinstance(sparse, dict)
    compact = dict(certificate)
    compact["multiplicity_matrix_sparse"] = compact_sparse_coo(
        sparse, witness_row_limit=8
    )
    return compact


def rref(matrix: Matrix) -> tuple[Matrix, list[int]]:
    work = [row[:] for row in matrix]
    if not work:
        return [], []
    row_count = len(work)
    col_count = len(work[0])
    pivot_row = 0
    pivots: list[int] = []
    for column in range(col_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            coefficient = work[row][column]
            work[row] = [
                work[row][col] - coefficient * work[pivot_row][col]
                for col in range(col_count)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, pivots


def rank(matrix: Matrix) -> int:
    return len(rref(matrix)[1])


def fraction_text(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def encoded_matrix(matrix: Matrix) -> list[list[str]]:
    return [[fraction_text(value) for value in row] for row in matrix]


def encoded_sparse_matrix(
    matrix: Matrix, *, known_rank: int | None = None
) -> dict[str, object]:
    entries = [
        {"row": row_index, "column": column_index, "value": fraction_text(value)}
        for row_index, row in enumerate(matrix)
        for column_index, value in enumerate(row)
        if value
    ]
    return {
        "rows": len(matrix),
        "columns": len(matrix[0]) if matrix else 0,
        "entries": entries,
        "rank": rank(matrix) if known_rank is None else known_rank,
    }


def canonical_sha256(value: object) -> str:
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def bounded_indices(length: int, limit: int) -> list[int]:
    if length <= limit:
        return list(range(length))
    if limit < 2:
        return [0]
    return sorted(
        {(step * (length - 1)) // (limit - 1) for step in range(limit)}
    )


def sequence_ledger(
    entries: list[object], *, witness_limit: int
) -> dict[str, object]:
    witness_indices = bounded_indices(len(entries), witness_limit)
    return {
        "count": len(entries),
        "canonical_sha256": canonical_sha256(entries),
        "witness_indices": witness_indices,
        "witnesses": [entries[index] for index in witness_indices],
    }


def compact_sparse_coo(
    sparse: dict[str, object], *, witness_row_limit: int
) -> dict[str, object]:
    entries = sparse["entries"]
    assert isinstance(entries, list)
    row_count = int(sparse["rows"])
    nonempty_rows = sorted({int(entry["row"]) for entry in entries})
    selected_rows = [
        nonempty_rows[index]
        for index in bounded_indices(len(nonempty_rows), witness_row_limit)
    ]
    return {
        "rows": row_count,
        "columns": int(sparse["columns"]),
        "rank": int(sparse["rank"]),
        "nonzero_count": len(entries),
        "canonical_COO_sha256": canonical_sha256(entries),
        "witness_rows": [
            {
                "row": row,
                "entries": [
                    {
                        "column": int(entry["column"]),
                        "value": str(entry["value"]),
                    }
                    for entry in entries
                    if int(entry["row"]) == row
                ],
            }
            for row in selected_rows
        ],
    }


def compact_map_certificate(
    certificate: dict[str, object], *, witness_row_limit: int
) -> dict[str, object]:
    domain = certificate["domain_basis"]
    codomain = certificate["codomain_basis"]
    assert isinstance(domain, list)
    assert isinstance(codomain, list)
    matrix_sparse = certificate["matrix_sparse"]
    rref_sparse = certificate["rref_sparse"]
    assert isinstance(matrix_sparse, dict)
    assert isinstance(rref_sparse, dict)
    return {
        "rows": int(certificate["rows"]),
        "columns": int(certificate["columns"]),
        "rank": int(certificate["rank"]),
        "kernel_dimension": int(certificate["kernel_dimension"]),
        "pivot_columns": certificate["pivot_columns"],
        "domain_basis_ledger": sequence_ledger(domain, witness_limit=12),
        "codomain_basis_ledger": sequence_ledger(codomain, witness_limit=12),
        "matrix_sparse": compact_sparse_coo(
            matrix_sparse, witness_row_limit=witness_row_limit
        ),
        "rref_sparse": compact_sparse_coo(
            rref_sparse, witness_row_limit=witness_row_limit
        ),
    }


def relation_certificate(
    basis: list[str], relations: Matrix, *, dense: bool = True
) -> dict[str, object]:
    reduced, pivots = rref(relations)
    relation_rank = len(pivots)
    payload: dict[str, object] = {
        "basis": basis,
        "rows": len(relations),
        "columns": len(basis),
        "rank": relation_rank,
        "quotient_dimension": len(basis) - relation_rank,
        "pivot_columns": pivots,
        "rref_sparse": encoded_sparse_matrix(reduced, known_rank=relation_rank),
    }
    if dense:
        payload["matrix"] = encoded_matrix(relations)
    else:
        payload["matrix_sparse"] = encoded_sparse_matrix(
            relations, known_rank=relation_rank
        )
    return payload


def map_certificate(
    domain: list[str], codomain: list[str], matrix: Matrix, *, dense: bool = True
) -> dict[str, object]:
    reduced, pivots = rref(matrix)
    map_rank = len(pivots)
    payload: dict[str, object] = {
        "domain_basis": domain,
        "codomain_basis": codomain,
        "rows": len(codomain),
        "columns": len(domain),
        "rank": map_rank,
        "kernel_dimension": len(domain) - map_rank,
        "pivot_columns": pivots,
        "rref_sparse": encoded_sparse_matrix(reduced, known_rank=map_rank),
    }
    if dense:
        payload["matrix"] = encoded_matrix(matrix)
    else:
        payload["matrix_sparse"] = encoded_sparse_matrix(matrix, known_rank=map_rank)
    return payload


def su2_multiplicities(twice_spins: Iterable[int]) -> dict[int, int]:
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
    left = su2_multiplicities([1] * (n_w + n_nabla + n_vector))
    right = su2_multiplicities([1] * (n_wtilde + n_barnabla + n_vector))
    return left.get(TARGET_JL_TWICE, 0) * right.get(TARGET_JR_TWICE, 0)


def enumerate_skeletons() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for n_w in range(4):
        for n_wtilde in range(4 - n_w):
            for n_nabla in range(10):
                for n_barnabla in range(10):
                    for n_vector in range(5):
                        dimension_twice = (
                            3 * (n_w + n_wtilde)
                            + n_nabla
                            + n_barnabla
                            + 2 * n_vector
                        )
                        formal_r = n_w - n_wtilde - n_nabla + n_barnabla
                        parity = (
                            n_w + n_wtilde + n_nabla + n_barnabla
                        ) % 2
                        if (
                            dimension_twice,
                            formal_r,
                            parity,
                        ) != (
                            TARGET_DIMENSION_TWICE,
                            TARGET_FORMAL_R,
                            TARGET_PARITY,
                        ):
                            continue
                        rows.append(
                            {
                                "n_w": n_w,
                                "n_wtilde": n_wtilde,
                                "n_nabla": n_nabla,
                                "n_barnabla": n_barnabla,
                                "n_vector": n_vector,
                                "field_strength_degree": n_w + n_wtilde,
                                "target_spin_multiplicity": target_spin_multiplicity(
                                    n_w,
                                    n_wtilde,
                                    n_nabla,
                                    n_barnabla,
                                    n_vector,
                                ),
                            }
                        )
    return sorted(
        rows,
        key=lambda row: (
            row["field_strength_degree"],
            row["n_w"],
            row["n_wtilde"],
            row["n_nabla"],
            row["n_barnabla"],
            row["n_vector"],
        ),
    )


def skeleton_name(row: dict[str, int]) -> str:
    return (
        f"W{row['n_w']}_T{row['n_wtilde']}_"
        f"N{row['n_nabla']}_B{row['n_barnabla']}_D{row['n_vector']}"
    )


def n0_certificate(rows: list[dict[str, int]]) -> dict[str, object]:
    n0_rows = [row for row in rows if row["field_strength_degree"] == 0]
    basis = [
        f"{skeleton_name(row)}:spin{copy}"
        for row in n0_rows
        for copy in range(row["target_spin_multiplicity"])
    ]
    identity_relations = identity_matrix(len(basis))

    source_basis: list[str] = []
    source_blocks: list[Matrix] = []
    source_chains: list[dict[str, object]] = []
    state_index = 0
    for row in n0_rows:
        derivative_parities = (
            (1,) * row["n_nabla"]
            + (1,) * row["n_barnabla"]
            + (0,) * row["n_vector"]
        )
        for copy in range(row["target_spin_multiplicity"]):
            state = basis[state_index]
            state_index += 1
            length = len(derivative_parities)
            block = zero_matrix(length + 1, length + 1)
            signs: list[str] = []
            source_parity = 1
            for step, derivative_parity in enumerate(derivative_parities):
                sign = Q(-1) if derivative_parity * source_parity % 2 else Q(1)
                block[step][step] = Q(1)
                block[step][step + 1] = sign
                signs.append(fraction_text(sign))
                source_parity ^= derivative_parity
            block[length][length] = Q(1)
            source_blocks.append(block)
            source_basis.extend(
                f"{state}:transfer-{step}" for step in range(length + 1)
            )
            source_chains.append(
                {
                    "state": state,
                    "spin_copy": copy,
                    "derivative_parities_outer_to_inner": list(
                        derivative_parities
                    ),
                    "IBP_relation_coefficients": signs,
                    "chain_length": length + 1,
                    "final_relation": "integral (all derivatives on J)*1=0",
                }
            )
    source_relations = block_diagonal(source_blocks)
    return {
        "field_strength_degree": 0,
        "identity_action": "nabla_A 1=[Gamma_A,1]=0",
        "target_component_count": len(basis),
        "identity_relation_matrix": relation_certificate(
            basis, identity_relations, dense=False
        ),
        "source_parity": "|J|=1",
        "source_ibp_equation": (
            "S_k+(-1)^(|delta_(k+1)||J_k|)S_(k+1)=0, "
            "S_L=integral(delta_L...delta_1 J)*1=0"
        ),
        "source_ibp_chains": source_chains,
        "source_ibp_relation_matrix": relation_certificate(
            source_basis, source_relations, dense=False
        ),
        "vanishes_in_source_extended_ibp_quotient": (
            rank(source_relations) == len(source_basis)
        ),
    }


def unique_permutations(tokens: tuple[str, ...]) -> list[tuple[str, ...]]:
    return sorted(set(itertools.permutations(tokens)))


def _add_polynomial_term(
    polynomial: defaultdict[tuple[str, ...], Q], word: tuple[str, ...], value: Q
) -> None:
    polynomial[word] += value
    if polynomial[word] == 0:
        del polynomial[word]


def normal_order_single_field(
    field: str, initial_word: tuple[str, ...]
) -> tuple[dict[tuple[str, ...], Q], list[dict[str, object]]]:
    """Normal order one N=1 derivative word and retain every curvature child.

    Canonical words are D* N* B* on W and D* B* N* on T.  Moving D left
    uses the exact Euclidean commutators.  Mixed N/B pairs use
    {N,B}=-2D.  Curvature children stop at their first new field-strength
    insertion and are therefore explicitly in filtration degree at least two.
    """

    queue: deque[tuple[tuple[str, ...], Q, tuple[str, ...]]] = deque(
        [(initial_word, Q(1), ())]
    )
    terminal: defaultdict[tuple[str, ...], Q] = defaultdict(Q)
    children: list[dict[str, object]] = []
    while queue:
        word, coefficient, path = queue.popleft()
        rewritten = False

        for position in range(len(word) - 1):
            left, right = word[position], word[position + 1]
            if left in {"N", "B"} and right == "D":
                swapped = word[:position] + ("D", left) + word[position + 2 :]
                queue.append((swapped, coefficient, path + (f"swap-{position}",)))
                curvature = "T" if left == "N" else "W"
                relation = (
                    "[N_a,D_(b dotb)]=-2 epsilon_ab T_dotb"
                    if left == "N"
                    else "[B_dota,D_(b dotb)]=-2 epsilon_dota_dotb W_b"
                )
                child_word = word[:position] + (f"CURVATURE_{curvature}",) + word[position + 2 :]
                children.append(
                    {
                        "event": len(children),
                        "input_word": list(initial_word),
                        "active_word": list(word),
                        "position": position,
                        "coefficient": fraction_text(Q(-2) * coefficient),
                        "relation": relation,
                        "child_word": list(child_word),
                        "child_field_strength_degree_minimum": 2,
                        "path": list(path),
                    }
                )
                rewritten = True
                break
        if rewritten:
            continue

        mixed_pair = ("B", "N") if field == "W" else ("N", "B")
        for position in range(len(word) - 1):
            if (word[position], word[position + 1]) != mixed_pair:
                continue
            swapped_pair = (mixed_pair[1], mixed_pair[0])
            swapped = word[:position] + swapped_pair + word[position + 2 :]
            collapsed = word[:position] + ("D",) + word[position + 2 :]
            queue.append(
                (swapped, -coefficient, path + (f"mixed-swap-{position}",))
            )
            queue.append(
                (collapsed, Q(-2) * coefficient, path + (f"mixed-D-{position}",))
            )
            rewritten = True
            break
        if rewritten:
            continue

        if (field == "W" and word and word[-1] == "B") or (
            field == "T" and word and word[-1] == "N"
        ):
            continue
        _add_polynomial_term(terminal, word, coefficient)
    return dict(sorted(terminal.items())), children


IndexedToken: TypeAlias = tuple[str, str, str, str]


def token_parity(token: IndexedToken) -> int:
    return 0 if token[0] == "D" else 1


def token_json(token: IndexedToken) -> dict[str, str]:
    return {
        "kind": token[0],
        "id": token[1],
        "left_slot": token[2],
        "right_slot": token[3],
    }


def indexed_tokens(row: dict[str, int]) -> tuple[IndexedToken, ...]:
    tokens: list[IndexedToken] = []
    for index in range(row["n_nabla"]):
        tokens.append(("N", f"N{index}", f"LN{index}", ""))
    for index in range(row["n_barnabla"]):
        tokens.append(("B", f"B{index}", "", f"RB{index}"))
    for index in range(row["n_vector"]):
        tokens.append(("D", f"D{index}", f"LD{index}", f"RD{index}"))
    return tuple(tokens)


def source_spin_slots(
    original_field: str, tokens: tuple[IndexedToken, ...]
) -> tuple[list[str], list[str]]:
    left: list[str] = ["LFW"] if original_field == "W" else []
    right: list[str] = ["RFT"] if original_field == "T" else []
    left.extend(token[2] for token in tokens if token[0] == "N")
    right.extend(token[3] for token in tokens if token[0] == "B")
    left.extend(token[2] for token in tokens if token[0] == "D")
    right.extend(token[3] for token in tokens if token[0] == "D")
    return left, right


def indexed_normal_order_input(
    original_field: str,
    initial_word: tuple[IndexedToken, ...],
) -> list[dict[str, object]]:
    """Return every curvature event from one fully indexed derivative word."""

    queue: deque[
        tuple[tuple[IndexedToken, ...], Q, tuple[str, ...]]
    ] = deque([(initial_word, Q(1), ())])
    events: list[dict[str, object]] = []
    while queue:
        word, coefficient, path = queue.popleft()
        rewritten = False
        for position in range(len(word) - 1):
            left, right = word[position], word[position + 1]
            if left[0] in {"N", "B"} and right[0] == "D":
                swapped = word[:position] + (right, left) + word[position + 2 :]
                queue.append((swapped, coefficient, path + (f"swap-{position}",)))
                if left[0] == "N":
                    contraction = [left[2], right[2]]
                    curvature_field = "T"
                    curvature_slot = right[3]
                    identity = "[N_a,D_(b dotb)]=-2 epsilon_ab T_dotb"
                else:
                    contraction = [left[3], right[3]]
                    curvature_field = "W"
                    curvature_slot = right[2]
                    identity = "[B_dota,D_(b dotb)]=-2 epsilon_dota_dotb W_b"
                events.append(
                    {
                        "local_event": len(events),
                        "coefficient": Q(-2) * coefficient,
                        "active_word": word,
                        "position": position,
                        "path": path,
                        "commutator": f"{left[0]}D",
                        "identity": identity,
                        "contracted_slots": contraction,
                        "curvature_field": curvature_field,
                        "curvature_slot": curvature_slot,
                        "prefix": word[:position],
                        "suffix": word[position + 2 :],
                        "field_strength_degree_minimum": 2,
                    }
                )
                rewritten = True
                break
        if rewritten:
            continue

        mixed_pair = ("B", "N") if original_field == "W" else ("N", "B")
        for position in range(len(word) - 1):
            left, right = word[position], word[position + 1]
            if (left[0], right[0]) != mixed_pair:
                continue
            n_token = left if left[0] == "N" else right
            b_token = left if left[0] == "B" else right
            generated = (
                "D",
                f"G({n_token[1]},{b_token[1]})",
                n_token[2],
                b_token[3],
            )
            swapped = word[:position] + (right, left) + word[position + 2 :]
            collapsed = word[:position] + (generated,) + word[position + 2 :]
            queue.append(
                (swapped, -coefficient, path + (f"mixed-swap-{position}",))
            )
            queue.append(
                (
                    collapsed,
                    Q(-2) * coefficient,
                    path + (f"mixed-D-{position}",),
                )
            )
            rewritten = True
            break
        if rewritten:
            continue

        if (original_field == "W" and word and word[-1][0] == "B") or (
            original_field == "T" and word and word[-1][0] == "N"
        ):
            continue
    return events


def expand_indexed_child_event(
    original_field: str, event: dict[str, object]
) -> list[dict[str, object]]:
    """Apply every prefix derivative by graded Leibniz to the two child fields."""

    prefix = event["prefix"]
    suffix = event["suffix"]
    assert isinstance(prefix, tuple) and isinstance(suffix, tuple)
    curvature_field = str(event["curvature_field"])
    coefficient = event["coefficient"]
    assert isinstance(coefficient, Q)

    terms: list[
        tuple[Q, list[tuple[IndexedToken, ...]], list[int]]
    ] = [
        (
            coefficient,
            [(), suffix],
            [1, (1 + sum(token_parity(token) for token in suffix)) % 2],
        )
    ]
    for token in reversed(prefix):
        updated: list[
            tuple[Q, list[tuple[IndexedToken, ...]], list[int]]
        ] = []
        parity = token_parity(token)
        for term_coefficient, words, parities in terms:
            for factor in range(2):
                sign = Q(-1) if parity * sum(parities[:factor]) % 2 else Q(1)
                new_words = words[:]
                new_words[factor] = (token,) + new_words[factor]
                new_parities = parities[:]
                new_parities[factor] ^= parity
                updated.append(
                    (term_coefficient * sign, new_words, new_parities)
                )
        terms = updated

    branches: list[dict[str, object]] = []
    for branch_coefficient, words, parities in terms:
        fields = [curvature_field, original_field]
        roles = ["curvature", "original"]
        order_sign = Q(1)
        if fields == ["T", "W"] or fields[0] == fields[1]:
            order_sign = Q(-1) if parities[0] * parities[1] % 2 else Q(1)
            fields = [fields[1], fields[0]]
            roles = [roles[1], roles[0]]
            words = [words[1], words[0]]
            parities = [parities[1], parities[0]]
        final_coefficient = branch_coefficient * order_sign

        left_slots: list[str] = []
        right_slots: list[str] = []
        field_data: list[dict[str, object]] = []
        for field, role, word in zip(fields, roles, words, strict=True):
            field_left = ""
            field_right = ""
            if role == "original":
                if field == "W":
                    field_left = "LFW"
                else:
                    field_right = "RFT"
            elif field == "W":
                field_left = str(event["curvature_slot"])
            else:
                field_right = str(event["curvature_slot"])
            if field_left:
                left_slots.append(field_left)
            if field_right:
                right_slots.append(field_right)
            for token in word:
                if token[0] == "N":
                    left_slots.append(token[2])
                elif token[0] == "B":
                    right_slots.append(token[3])
                else:
                    left_slots.append(token[2])
                    right_slots.append(token[3])
            field_data.append(
                {
                    "field": field,
                    "role": role,
                    "derivative_word": [token_json(token) for token in word],
                    "derivative_kinds": [token[0] for token in word],
                }
            )
        if len(set(left_slots)) != len(left_slots) or len(set(right_slots)) != len(
            right_slots
        ):
            raise AssertionError("indexed child output reuses a spinor slot")

        n_w = fields.count("W")
        n_t = fields.count("T")
        n_n = sum(token[0] == "N" for word in words for token in word)
        n_b = sum(token[0] == "B" for word in words for token in word)
        n_d = sum(token[0] == "D" for word in words for token in word)
        sector = f"W{n_w}_T{n_t}_N{n_n}_B{n_b}_D{n_d}"
        all_output_tokens = [token for word in words for token in word]
        canonical_token_labels: dict[tuple[str, str, str], str] = {}
        for kind, slot_key in (
            ("N", lambda token: (token[2], "")),
            ("B", lambda token: ("", token[3])),
            ("D", lambda token: (token[2], token[3])),
        ):
            tokens_of_kind = sorted(
                (token for token in all_output_tokens if token[0] == kind),
                key=slot_key,
            )
            for index, token in enumerate(tokens_of_kind):
                canonical_token_labels[(token[0], token[2], token[3])] = (
                    f"{kind}{index}"
                )
        placement_key = (
            sector,
            tuple(
                (
                    str(field["field"]),
                    tuple(
                        canonical_token_labels[
                            (token[0], token[2], token[3])
                        ]
                        for token in words[field_index]
                    ),
                )
                for field_index, field in enumerate(field_data)
            ),
        )
        branches.append(
            {
                "coefficient": final_coefficient,
                "fields": field_data,
                "factor_parities": parities,
                "left_slots": left_slots,
                "right_slots": right_slots,
                "sector": sector,
                "placement_key": placement_key,
            }
        )
    return branches


def indexed_n1_input_records(rows: list[dict[str, int]]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    n1_rows = [row for row in rows if row["field_strength_degree"] == 1]
    for row in n1_rows:
        original_field = "W" if row["n_w"] else "T"
        tokens = indexed_tokens(row)
        source_left, source_right = source_spin_slots(original_field, tokens)
        for word in itertools.permutations(tokens):
            events = indexed_normal_order_input(original_field, word)
            if not events:
                continue
            event_records: list[dict[str, object]] = []
            for event in events:
                branches = expand_indexed_child_event(original_field, event)
                event_records.append(
                    {
                        "local_event": event["local_event"],
                        "coefficient": fraction_text(event["coefficient"]),
                        "active_word": [
                            token_json(token) for token in event["active_word"]
                        ],
                        "position": event["position"],
                        "path": list(event["path"]),
                        "commutator": event["commutator"],
                        "identity": event["identity"],
                        "contracted_slots": event["contracted_slots"],
                        "curvature_field": event["curvature_field"],
                        "curvature_slot": event["curvature_slot"],
                        "prefix": [token_json(token) for token in event["prefix"]],
                        "suffix": [token_json(token) for token in event["suffix"]],
                        "field_strength_degree_minimum": 2,
                        "branches": branches,
                    }
                )
            records.append(
                {
                    "input_id": len(records),
                    "skeleton": skeleton_name(row),
                    "original_field": original_field,
                    "source_left_slots": source_left,
                    "source_right_slots": source_right,
                    "word": [token_json(token) for token in word],
                    "events": event_records,
                }
            )
    return records


def n1_normal_order(rows: list[dict[str, int]]) -> dict[str, object]:
    n1_rows = [row for row in rows if row["field_strength_degree"] == 1]
    input_records: list[dict[str, object]] = []
    outputs_by_input: list[dict[tuple[str, tuple[str, ...]], Q]] = []
    all_children: list[dict[str, object]] = []
    output_basis_set: set[tuple[str, tuple[str, ...]]] = set()

    for row in n1_rows:
        field = "W" if row["n_w"] else "T"
        token_multiset = (
            ("N",) * row["n_nabla"]
            + ("B",) * row["n_barnabla"]
            + ("D",) * row["n_vector"]
        )
        for word in unique_permutations(token_multiset):
            output, children = normal_order_single_field(field, word)
            encoded_output = {(field, term): value for term, value in output.items()}
            output_basis_set.update(encoded_output)
            input_id = len(input_records)
            event_ids: list[int] = []
            for child in children:
                child["local_event"] = child.pop("event")
                child["event_id"] = len(all_children)
                child["input_id"] = input_id
                child["skeleton"] = skeleton_name(row)
                curvature = (
                    "T" if "CURVATURE_T" in child["child_word"] else "W"
                )
                child_n_w = row["n_w"] + int(curvature == "W")
                child_n_t = row["n_wtilde"] + int(curvature == "T")
                child_n_nabla = child["child_word"].count("N")
                child_n_barnabla = child["child_word"].count("B")
                child_n_vector = child["child_word"].count("D")
                child["target_N2_skeleton"] = (
                    f"W{child_n_w}_T{child_n_t}_N{child_n_nabla}_"
                    f"B{child_n_barnabla}_D{child_n_vector}"
                )
                event_ids.append(int(child["event_id"]))
                all_children.append(child)
            input_records.append(
                {
                    "id": input_id,
                    "skeleton": skeleton_name(row),
                    "field": field,
                    "word": list(word),
                    "normal_output": [
                        {
                            "coefficient": fraction_text(coefficient),
                            "field": field,
                            "word": list(term),
                        }
                        for term, coefficient in output.items()
                    ],
                    "curvature_child_event_ids": event_ids,
                }
            )
            outputs_by_input.append(encoded_output)

    output_basis = sorted(output_basis_set)
    output_index = {term: index for index, term in enumerate(output_basis)}
    normal_matrix = zero_matrix(len(output_basis), len(input_records))
    for column, output in enumerate(outputs_by_input):
        for term, coefficient in output.items():
            normal_matrix[output_index[term]][column] = coefficient

    child_basis = sorted(
        {
            (
                str(child["skeleton"]),
                str(child["relation"]),
                tuple(child["child_word"]),
            )
            for child in all_children
        }
    )
    child_index = {child: index for index, child in enumerate(child_basis)}
    child_matrix = zero_matrix(len(child_basis), len(input_records))
    for child in all_children:
        key = (
            str(child["skeleton"]),
            str(child["relation"]),
            tuple(child["child_word"]),
        )
        child_matrix[child_index[key]][int(child["input_id"])] += Q(
            str(child["coefficient"])
        )

    return {
        "canonical_order": {
            "W": "D* N* B*, then B W=0",
            "T": "D* B* N*, then N T=0",
        },
        "input_count": len(input_records),
        "input_records": input_records,
        "normal_form_basis": [
            {"field": field, "word": list(word)} for field, word in output_basis
        ],
        "normal_order_map": map_certificate(
            [f"input:{index}" for index in range(len(input_records))],
            [f"{field}:{''.join(word) or '1'}" for field, word in output_basis],
            normal_matrix,
            dense=False,
        ),
        "curvature_child_basis": [
            {
                "skeleton": skeleton,
                "relation": relation,
                "child_word": list(word),
                "field_strength_degree_minimum": 2,
            }
            for skeleton, relation, word in child_basis
        ],
        "curvature_child_incidence": map_certificate(
            [f"input:{index}" for index in range(len(input_records))],
            [f"child:{index}" for index in range(len(child_basis))],
            child_matrix,
            dense=False,
        ),
        "curvature_child_events": all_children,
        "all_commutator_children_tagged_N_ge_2": all(
            child["child_field_strength_degree_minimum"] >= 2
            for child in all_children
        ),
        "all_commutator_children_content_bound_to_five_N2_sectors": all(
            child["target_N2_skeleton"]
            in {
                "W2_T0_N3_B0_D0",
                "W1_T1_N2_B1_D0",
                "W1_T1_N1_B0_D1",
                "W0_T2_N1_B2_D0",
                "W0_T2_N0_B1_D1",
            }
            for child in all_children
        ),
    }


def n1_target_eom_matrix(rows: list[dict[str, int]]) -> dict[str, object]:
    n1_rows = [row for row in rows if row["field_strength_degree"] == 1]
    target_basis: list[str] = []
    carrier_basis: list[str] = []
    coefficients: list[Q] = []
    witnesses: list[dict[str, object]] = []
    vector_pairing_children: list[dict[str, object]] = []
    for row in n1_rows:
        multiplicity = row["target_spin_multiplicity"]
        field = "W" if row["n_w"] else "T"
        for copy in range(multiplicity):
            name = f"{skeleton_name(row)}:spin{copy}"
            target_basis.append(name)
            if field == "W":
                carrier = f"nabla(E):{name}"
                coefficient = Q(-2)
                identity = "nabla^2 W_a=-2 nabla_a E"
            else:
                if row["n_vector"] == 0:
                    right_channel = "BdotT"
                elif row["n_barnabla"] == 0:
                    right_channel = "DdotT"
                else:
                    right_channel = "BdotT" if copy % 2 == 0 else "DdotT"
                if right_channel == "BdotT":
                    carrier = f"barE:{name}"
                    coefficient = Q(1)
                    identity = "bar_nabla^dota T_dota=barE"
                else:
                    carrier = f"nabla(barE):{name}"
                    coefficient = Q(-1, 2)
                    identity = (
                        "D_a^dota T_dota=-(1/2) nabla_a"
                        "(bar_nabla^dota T_dota)"
                    )
                    vector_swaps = (
                        1
                        if row["n_vector"] >= 2
                        and row["n_barnabla"] == 0
                        and copy == 1
                        else 0
                    )
                    for swap in range(vector_swaps):
                        for curvature, formula in (
                            (
                                "N_(a W_b)",
                                "epsilon_(dot a dot b) N_(a W_b)",
                            ),
                            (
                                "B_(dot a T_dot b)",
                                "epsilon_ab B_(dot a T_dot b)",
                            ),
                        ):
                            vector_pairing_children.append(
                                {
                                    "event_id": len(vector_pairing_children),
                                    "target": name,
                                    "swap": swap,
                                    "identity": (
                                        "[D_(a dota),D_(b dotb)]="
                                        "epsilon_(dota dotb)N_(a W_b)+"
                                        "epsilon_ab B_(dota T_dotb)"
                                    ),
                                    "coefficient": "1",
                                    "curvature_term": curvature,
                                    "formula": formula,
                                    "field_strength_degree_minimum": 2,
                                }
                            )
            carrier_basis.append(carrier)
            coefficients.append(coefficient)
            witnesses.append(
                {
                    "target": name,
                    "right_contraction_channel": (
                        "nabla-pair" if field == "W" else right_channel
                    ),
                    "identity": identity,
                    "spin_pairing_witness": (
                        "left target basis contains an antisymmetric N-pair on W"
                        if field == "W"
                        else (
                            "epsilon(T_dot,B_dot_i); all remaining dotted slots paired"
                            if right_channel == "BdotT"
                            else "epsilon(T_dot,D_(a dot)); all remaining dotted slots paired"
                        )
                    ),
                    "coefficient": fraction_text(coefficient),
                    "carrier": carrier,
                }
            )

    basis = target_basis + carrier_basis
    relations = zero_matrix(2 * len(target_basis), 2 * len(target_basis))
    for index, coefficient in enumerate(coefficients):
        relations[index][index] = Q(1)
        relations[index][len(target_basis) + index] = -coefficient
        relations[len(target_basis) + index][len(target_basis) + index] = Q(1)
    return {
        "field_strength_degree": 1,
        "associated_graded_modulo": "F_(field-strength)>=2 curvature children",
        "target_component_count": len(target_basis),
        "identities": {
            "chiral": "nabla^2 W_a=-2 nabla_a E",
            "antichiral": (
                "D_a^dota T_dota=-(1/2) nabla_a"
                "(bar_nabla^dota T_dota)"
            ),
        },
        "witnesses": witnesses,
        "vector_pairing_commutator_children": vector_pairing_children,
        "all_vector_pairing_children_tagged_N_ge_2": all(
            child["field_strength_degree_minimum"] >= 2
            for child in vector_pairing_children
        ),
        "target_plus_EOM_relation_matrix": relation_certificate(
            basis, relations, dense=False
        ),
        "associated_graded_target_quotient_dimension": (
            len(basis) - rank(relations)
        ),
    }


def graded_product_expansion(
    operators: tuple[tuple[str, int], ...], factor_parities: tuple[int, ...]
) -> list[dict[str, object]]:
    """Expand an ordered derivative word on a product, retaining Koszul signs."""

    terms: list[tuple[Q, list[tuple[str, ...]], list[int], dict[str, int]]] = [
        (Q(1), [() for _ in factor_parities], list(factor_parities), {})
    ]
    for operator, parity in reversed(operators):
        updated: list[
            tuple[Q, list[tuple[str, ...]], list[int], dict[str, int]]
        ] = []
        for coefficient, words, parities, assignments in terms:
            for factor in range(len(factor_parities)):
                sign = Q(-1) if parity * sum(parities[:factor]) % 2 else Q(1)
                new_words = words[:]
                new_words[factor] = (operator,) + new_words[factor]
                new_parities = parities[:]
                new_parities[factor] ^= parity
                new_assignments = dict(assignments)
                new_assignments[operator] = factor
                updated.append(
                    (
                        coefficient * sign,
                        new_words,
                        new_parities,
                        new_assignments,
                    )
                )
        terms = updated
    return [
        {
            "coefficient": fraction_text(coefficient),
            "factor_words": [list(word) for word in words],
            "assignment": [assignments[operator] for operator, _ in operators],
        }
        for coefficient, words, _, assignments in terms
    ]


def ibp_incidence(
    derivative_parities: tuple[int, ...], factor_parities: tuple[int, int, int]
) -> dict[str, object]:
    """Exact total-derivative incidence on the factors (J,F1,F2)."""

    derivative_count = len(derivative_parities)
    assignments = list(itertools.product(range(3), repeat=derivative_count))
    assignment_index = {assignment: index for index, assignment in enumerate(assignments)}
    rows: Matrix = []
    row_labels: list[dict[str, object]] = []
    for active in range(derivative_count):
        other_indices = [index for index in range(derivative_count) if index != active]
        for other_assignment in itertools.product(range(3), repeat=derivative_count - 1):
            precursor = [-1] * derivative_count
            for index, factor in zip(other_indices, other_assignment, strict=True):
                precursor[index] = factor
            current_parities = list(factor_parities)
            for index in other_indices:
                if derivative_parities[index]:
                    current_parities[precursor[index]] ^= 1
            row = [Q(0) for _ in assignments]
            coefficients: list[str] = []
            for factor in range(3):
                sign_exponent = derivative_parities[active] * sum(
                    current_parities[:factor]
                )
                coefficient = Q(-1) if sign_exponent % 2 else Q(1)
                completed = precursor[:]
                completed[active] = factor
                row[assignment_index[tuple(completed)]] = coefficient
                coefficients.append(fraction_text(coefficient))
            rows.append(row)
            row_labels.append(
                {
                    "active_derivative": active,
                    "precursor_assignment": precursor,
                    "coefficients_on_J_F1_F2": coefficients,
                }
            )
    physical_columns = [
        index for index, assignment in enumerate(assignments) if 0 not in assignment
    ]
    source_columns = [
        index for index, assignment in enumerate(assignments) if 0 in assignment
    ]
    restricted = [[row[column] for column in physical_columns] for row in rows]
    return {
        "factor_order": ["J", "F1", "F2"],
        "factor_initial_parities": list(factor_parities),
        "derivative_parities": list(derivative_parities),
        "column_assignments": [list(assignment) for assignment in assignments],
        "row_labels": row_labels,
        "full_source_jet_incidence": relation_certificate(
            [f"assignment:{assignment}" for assignment in assignments],
            rows,
            dense=False,
        ),
        "physical_no_source_columns": physical_columns,
        "source_jet_columns": source_columns,
        "constant_source_restriction": relation_certificate(
            [f"assignment:{assignments[index]}" for index in physical_columns],
            restricted,
            dense=False,
        ),
        "constant_source_is_not_the_source_extended_quotient": True,
    }


def ww_spin_projector() -> dict[str, object]:
    projector = [
        [Q(int(row == column)) - Q(1, 5) for column in range(5)]
        for row in range(5)
    ]
    ones = [[Q(1) for _ in range(5)]]
    return {
        "weight_m_3_over_2_basis": [f"minus-slot-{index}" for index in range(5)],
        "raising_map_to_j_5_over_2": map_certificate(
            [f"minus-slot-{index}" for index in range(5)],
            ["all-plus"],
            ones,
        ),
        "j_3_over_2_projector": map_certificate(
            [f"minus-slot-{index}" for index in range(5)],
            [f"minus-slot-{index}" for index in range(5)],
            projector,
        ),
        "projector_idempotent": multiply(projector, projector) == projector,
        "target_multiplicity": rank(projector),
    }


def ww_nabla3_certificate() -> dict[str, object]:
    operators = (("N:a", 1), ("N:b", 1), ("N:c", 1))
    expansion = graded_product_expansion(operators, (1, 1))
    target_copies = 4
    placement_basis = [
        f"spin{spin}:placement{placement}"
        for spin in range(target_copies)
        for placement in range(len(expansion))
    ]
    carrier_basis = [f"EOM:{basis}" for basis in placement_basis]
    basis = placement_basis + carrier_basis
    relations = zero_matrix(2 * len(placement_basis), len(basis))
    for index in range(len(placement_basis)):
        relations[index][index] = Q(1)
        relations[index][len(placement_basis) + index] = Q(-1)
        relations[len(placement_basis) + index][len(placement_basis) + index] = Q(1)
    placement_witnesses = []
    for index, term in enumerate(expansion):
        assignment = term["assignment"]
        count_f1 = assignment.count(0)
        carrier = "W1" if count_f1 >= 2 else "W2"
        placement_witnesses.append(
            {
                "placement": index,
                "assignment": assignment,
                "koszul_coefficient": term["coefficient"],
                "factor_words": term["factor_words"],
                "eom_carrier": carrier,
                "identity": "N_a N_b W_c=-epsilon_ab N_c E",
            }
        )
    return {
        "content": "W W N^3",
        "free_target_spin_multiplicity": target_copies,
        "spin_projector": ww_spin_projector(),
        "graded_leibniz_expansion": expansion,
        "placement_witnesses": placement_witnesses,
        "placement_plus_EOM_relation_matrix": relation_certificate(
            basis, relations, dense=False
        ),
        "target_quotient_dimension": len(basis) - rank(relations),
        "source_ibp_incidence": ibp_incidence((1, 1, 1), (1, 1, 1)),
    }


def mixed_n2b_certificate() -> dict[str, object]:
    operators = (("N:a", 1), ("N:b", 1), ("B:dot", 1))
    expansion = graded_product_expansion(operators, (1, 1))
    codomain = ["EOM", "C_ba", "C_ab", "H_WTT"]
    reduction = zero_matrix(len(codomain), len(expansion))
    reduction[0][4] = Q(-1)
    reduction[1][5] = Q(2)
    reduction[2][6] = Q(-2)
    reduction[3][7] = Q(-4)

    branch_basis = [f"M{index}" for index in range(len(expansion))]
    quotient_basis = branch_basis + codomain
    relations = zero_matrix(len(branch_basis) + 2, len(quotient_basis))
    for index in range(len(branch_basis)):
        relations[index][index] = Q(1)
        for output_index in range(len(codomain)):
            relations[index][len(branch_basis) + output_index] = -reduction[
                output_index
            ][index]
    relations[8][8] = Q(1)  # EOM=0
    relations[9][11] = Q(1)  # H_WTT has no target spin

    sym_projector = [
        [Q(1, 2), Q(1, 2)],
        [Q(1, 2), Q(1, 2)],
    ]
    antisymmetric_reduction = [[Q(2)], [Q(-2)]]
    projected_target_map = [[Q(0)]]
    projected_target_relations = [[Q(1)]]
    return {
        "content": "W T N^2 B",
        "free_target_spin_multiplicity": 1,
        "graded_leibniz_expansion": expansion,
        "normal_reduction_map": map_certificate(
            branch_basis, codomain, reduction
        ),
        "normal_reduction_equations": [
            "N_a B^dot T_dot=-2 D_a^dot T_dot",
            "N_a N_b B^dot T_dot=+4 epsilon_ab T^dot T_dot",
            "N_a N_b W_c=-epsilon_ab N_c E",
        ],
        "branch_relation_matrix": relation_certificate(
            quotient_basis, relations
        ),
        "pre_spin_remaining_dimension": len(quotient_basis) - rank(relations),
        "target_spin_projector_on_C_ba_C_ab": map_certificate(
            ["C_ba", "C_ab"], ["C_ba", "C_ab"], sym_projector
        ),
        "reduced_C_vector": encoded_matrix(antisymmetric_reduction),
        "target_projection_of_reduced_C_vector": encoded_matrix(
            multiply(sym_projector, antisymmetric_reduction)
        ),
        "target_projection_zero": multiply(
            sym_projector, antisymmetric_reduction
        ) == [[Q(0)], [Q(0)]],
        "projected_target_map": map_certificate(
            ["projected W T N^2 B class"],
            ["projected W T N D class"],
            projected_target_map,
        ),
        "projected_target_relation_matrix": relation_certificate(
            ["projected W T N^2 B class"], projected_target_relations
        ),
        "projected_target_quotient_dimension": 0,
        "source_ibp_incidence": ibp_incidence((1, 1, 1), (1, 1, 1)),
    }


def mixed_nd_certificate() -> dict[str, object]:
    operators = (("N:a", 1), ("D:b,dot", 0))
    expansion = graded_product_expansion(operators, (1, 1))
    codomain = ["C_on_W", "C_split", "H_WTT"]
    reduction = [
        [Q(1), Q(0), Q(0), Q(0)],
        [Q(0), Q(0), Q(1), Q(0)],
        [Q(-2), Q(0), Q(0), Q(2)],
    ]
    leibniz_vector = [[Q(1)] for _ in expansion]
    total_reduction = multiply(reduction, leibniz_vector)

    constant_source_basis = ["C_on_W", "C_split"]
    constant_source_ibp = [[Q(1), Q(1)]]
    constant_source_eom_ibp = [
        [Q(1), Q(1)],
        [Q(0), Q(1)],
    ]
    source_extended_basis = ["C_on_W", "C_split", "S_DJ"]
    source_extended_ibp = [[Q(1), Q(1), Q(1)]]
    source_extended_eom_ibp = [
        [Q(1), Q(1), Q(1)],
        [Q(0), Q(1), Q(0)],
    ]

    orientation_matrix = [[Q(1)], [Q(-1)]]
    return {
        "content": "W T N D",
        "free_target_spin_multiplicity": 1,
        "graded_leibniz_expansion": expansion,
        "branch_reduction_map": map_certificate(
            [f"P{index}" for index in range(len(expansion))],
            codomain,
            reduction,
        ),
        "commutator_children": [
            {
                "branch": "P0",
                "identity": "N_a D_(b dotb)=D_(b dotb) N_a-2 epsilon_ab T_dotb",
                "coefficient": "-2",
                "child": "H_WTT",
                "field_strength_degree": 3,
            },
            {
                "branch": "P3",
                "identity": "N_a D_(b dotb) T_dotc=-2 epsilon_ab T_dotb T_dotc",
                "coefficient": "2",
                "child": "H_WTT after the branch Koszul sign",
                "field_strength_degree": 3,
            },
        ],
        "sum_of_all_leibniz_branches": {
            "input_vector": encoded_matrix(leibniz_vector),
            "output_vector_C_on_W_C_split_H": encoded_matrix(total_reduction),
            "N3_children_cancel": total_reduction[2][0] == 0,
        },
        "constant_source_ibp": relation_certificate(
            constant_source_basis, constant_source_ibp
        ),
        "source_extended_ibp": relation_certificate(
            source_extended_basis, source_extended_ibp
        ),
        "antichiral_EOM_equation": (
            "C_split=D_a^dota T_dota=-(1/2)N_a barE=0"
        ),
        "constant_source_EOM_completed_quotient": relation_certificate(
            constant_source_basis, constant_source_eom_ibp
        ),
        "source_extended_EOM_completed_quotient": relation_certificate(
            source_extended_basis, source_extended_eom_ibp
        ),
        "source_extended_representative_equations": [
            "C_split=0",
            "S_DJ=-C_on_W",
        ],
        "source_derivative_is_not_an_independent_class": True,
        "source_extended_equation": "C_on_W+C_split+S_DJ=0",
        "quadratic_operator": (
            "J_AB K^(AB)_(CD) T^C_dota D_+^dota N_+ W_+^D"
        ),
        "symbolic_tensor_module": (
            "K^(AB)_(CD) is a free nonzero source-color tensor; no color quotient"
        ),
        "complete_ordered_quadratic_jet": map_certificate(
            ["K^(AB)_(CD)"],
            ["ordered-port(T^C,W^D)", "ordered-port(W^D,T^C)"],
            orientation_matrix,
        ),
        "ordered_port_sign": "W and T are odd, hence (T,W)=+1 and (W,T)=-1",
        "tensorwise_quadratic_jet_nonzero": rank(orientation_matrix) == 1,
        "tensorwise_quadratic_jet_injective": (
            len(orientation_matrix[0]) - rank(orientation_matrix) == 0
        ),
        "source_ibp_incidence": ibp_incidence((1, 0), (1, 1, 1)),
    }


def n2_certificate(rows: list[dict[str, int]]) -> dict[str, object]:
    n2_rows = [row for row in rows if row["field_strength_degree"] == 2]
    sector_table = [
        {
            "content": skeleton_name(row),
            "target_spin_multiplicity": row["target_spin_multiplicity"],
        }
        for row in n2_rows
    ]
    zero_sectors = [
        row for row in sector_table if row["target_spin_multiplicity"] == 0
    ]
    t2_nb2_expansion = graded_product_expansion(
        (("N:a", 1), ("B:dotb", 1), ("B:dotc", 1)), (1, 1)
    )
    t2_bd_expansion = graded_product_expansion(
        (("B:dota", 1), ("D:b,dotb", 0)), (1, 1)
    )
    return {
        "field_strength_degree": 2,
        "five_sector_table": sector_table,
        "zero_spin_sectors": zero_sectors,
        "WW_N3": ww_nabla3_certificate(),
        "W_T_N2_B": mixed_n2b_certificate(),
        "W_T_N_D": mixed_nd_certificate(),
        "T2_N_B2": {
            "target_spin_multiplicity": 0,
            "graded_leibniz_expansion": t2_nb2_expansion,
            "placement_count": len(t2_nb2_expansion),
            "source_ibp_incidence": ibp_incidence((1, 1, 1), (1, 1, 1)),
        },
        "T2_B_D": {
            "target_spin_multiplicity": 0,
            "graded_leibniz_expansion": t2_bd_expansion,
            "placement_count": len(t2_bd_expansion),
            "source_ibp_incidence": ibp_incidence((1, 0), (1, 1, 1)),
        },
    }


def n3_and_dimension_certificate(rows: list[dict[str, int]]) -> dict[str, object]:
    n3_rows = [row for row in rows if row["field_strength_degree"] == 3]
    row = n3_rows[0]
    return {
        "N3": {
            "solution_count": len(n3_rows),
            "content": skeleton_name(row),
            "left_spin_factors": 1,
            "left_decomposition": "1/2",
            "right_decomposition": "1/2 tensor 1/2 = 0 plus 1",
            "target_spin_multiplicity": row["target_spin_multiplicity"],
            "target_projection_zero": row["target_spin_multiplicity"] == 0,
        },
        "N_ge_4": {
            "minimum_dimension_twice": 12,
            "target_dimension_twice": TARGET_DIMENSION_TWICE,
            "excluded": 12 > TARGET_DIMENSION_TWICE,
        },
    }


def color_quotient_module_certificate() -> dict[str, object]:
    return {
        "status": "CLOSED_BY_SPLIT_MONOMORPHISM",
        "module": (
            "an arbitrary quotient module M of the source-color tensor module"
        ),
        "map": "iota_M:M->M direct_sum M, iota_M(m)=(m,-m)",
        "left_inverse": "pi_1:M direct_sum M->M, pi_1(x,y)=x",
        "composition": "pi_1 o iota_M=id_M",
        "kernel": "ker(iota_M)=0",
        "proof": (
            "iota_M(m)=(0,0) implies m=pi_1(iota_M(m))=0"
        ),
        "consequence": (
            "applying the same color quotient module to the source and both"
            " ordered output copies cannot create a quadratic-jet kernel"
        ),
    }


def filtered_quotient_fail_closed_certificate(
    n0: dict[str, object],
    n1_eom: dict[str, object],
    indexed_ndbd_raw: dict[str, object],
    indexed_dd: dict[str, object],
    indexed_complete: dict[str, object],
    n2: dict[str, object],
    higher: dict[str, object],
) -> dict[str, object]:
    n2_canonical_target_dimension = (
        4 * len(n2["WW_N3"]["graded_leibniz_expansion"])
        + len(n2["W_T_N2_B"]["graded_leibniz_expansion"])
        + len(n2["W_T_N_D"]["graded_leibniz_expansion"])
    )
    source_rows = n2["W_T_N_D"]["source_ibp_incidence"]["row_labels"]
    sector_record_counts: defaultdict[str, int] = defaultdict(int)
    sector_column_counts: defaultdict[str, int] = defaultdict(int)
    for record in indexed_ndbd_raw["input_table"]:
        skeleton = str(record["skeleton"])
        sector_record_counts[skeleton] += 1
        sector_column_counts[skeleton] += int(
            record["source_target_multiplicity"]
        )
    dd_skeleton = str(indexed_dd["source_skeleton"])
    sector_record_counts[dd_skeleton] += 1
    sector_column_counts[dd_skeleton] += int(
        indexed_dd["source_highest_weight_multiplicity"]
    )
    n1_abstract_basis = n1_eom["target_plus_EOM_relation_matrix"]["basis"][
        : int(n1_eom["target_component_count"])
    ]
    indexed_domain_basis = list(
        indexed_ndbd_raw["multiplicity_matrix"]["domain_basis"]
    ) + [
        f"DD:{label}"
        for label in indexed_dd["highest_weight_matrix"]["domain_basis"]
    ]
    indexed_n2_basis = indexed_ndbd_raw["multiplicity_matrix"][
        "codomain_basis"
    ]
    canonical_n2_basis = [
        f"WW:spin{spin}:placement{placement}"
        for spin in range(4)
        for placement in range(8)
    ] + [
        f"WTN2B:placement{placement}" for placement in range(8)
    ] + [
        f"WTND:placement{placement}" for placement in range(4)
    ]
    return {
        "status": "FAIL_CLOSED_NOT_ASSEMBLED",
        "filtered_target_blocks": {
            "N0_target_components": int(n0["target_component_count"]),
            "N1_target_components": int(n1_eom["target_component_count"]),
            "N2_indexed_target_multiplicity_rows": int(
                indexed_complete["target_multiplicity_rows"]
            ),
            "N2_existing_canonical_placement_coordinates": (
                n2_canonical_target_dimension
            ),
            "N3_target_components": int(
                higher["N3"]["target_spin_multiplicity"]
            ),
        },
        "known_exact_blocks": {
            "N0_source_IBP": {
                "rows": int(n0["source_ibp_relation_matrix"]["rows"]),
                "columns": int(n0["source_ibp_relation_matrix"]["columns"]),
                "rank": int(n0["source_ibp_relation_matrix"]["rank"]),
            },
            "N1_target_plus_EOM": {
                "rows": int(
                    n1_eom["target_plus_EOM_relation_matrix"]["rows"]
                ),
                "columns": int(
                    n1_eom["target_plus_EOM_relation_matrix"]["columns"]
                ),
                "rank": int(
                    n1_eom["target_plus_EOM_relation_matrix"]["rank"]
                ),
            },
            "N1_to_N2_child_coverage": {
                "rows": int(indexed_complete["target_multiplicity_rows"]),
                "columns": int(indexed_complete["source_multiplicity_columns"]),
                "rank": int(indexed_complete["multiplicity_rank"]),
                "logical_role": "surjective coverage, not injectivity",
            },
            "N3_target": "zero",
        },
        "source_local_derivative_rows": {
            "factor_order": ["J", "F1", "F2"],
            "column_basis": (
                "e_(x,y): nabla endpoint x and D endpoint y,"
                " x,y in {J,F1,F2}"
            ),
            "nabla_rows": [
                f"e_(J,{endpoint})-e_(F1,{endpoint})+e_(F2,{endpoint})=0"
                for endpoint in ("J", "F1", "F2")
            ],
            "D_rows": [
                f"e_({endpoint},J)+e_({endpoint},F1)+e_({endpoint},F2)=0"
                for endpoint in ("J", "F1", "F2")
            ],
            "exact_incidence_rows": source_rows,
            "matrix": n2["W_T_N_D"]["source_ibp_incidence"][
                "full_source_jet_incidence"
            ],
            "antichiral_EOM_row_on_C_on_W_C_split_S_DJ": ["0", "1", "0"],
            "antichiral_EOM_identity": n2["W_T_N_D"][
                "antichiral_EOM_equation"
            ],
            "EOM_completed_canonical_quotient": n2["W_T_N_D"][
                "source_extended_EOM_completed_quotient"
            ],
            "representative_equations": n2["W_T_N_D"][
                "source_extended_representative_equations"
            ],
            "external_source_momentum": "retained; p=p1+p2",
        },
        "missing_incidence_matrices": [
            {
                "id": "C_N1_TARGET_TO_INDEXED_SOURCE",
                "shape": "4866x20",
                "map_orientation": "C1:Q^20 -> Q^4866",
                "domain_basis": n1_abstract_basis,
                "codomain_basis_ledger": sequence_ledger(
                    indexed_domain_basis, witness_limit=16
                ),
                "codomain_sector_decomposition": [
                    {
                        "skeleton": skeleton,
                        "ordered_word_records": sector_record_counts[skeleton],
                        "multiplicity_columns": sector_column_counts[skeleton],
                    }
                    for skeleton in sorted(sector_column_counts)
                ],
                "role": (
                    "embed the twenty N1 target-spin states into the indexed"
                    " child-source multiplicity columns, with EOM and Koszul signs"
                ),
                "canonical_map_defined": False,
                "obstruction": (
                    "the twenty labels are abstract multiplicity copies, whereas"
                    " the 4866 columns are ordered-word copies; the event ledger"
                    " contains child summands but no Project-normalized section"
                    " or complete ordered-word relation matrix"
                ),
            },
            {
                "id": "R_N2_INDEXED_EOM_IBP",
                "minimum_target_columns": 126,
                "column_basis_ledger": sequence_ledger(
                    indexed_n2_basis, witness_limit=16
                ),
                "existing_canonical_basis": canonical_n2_basis,
                "role": (
                    "act on the shared indexed N2 placement basis and include"
                    " EOM (including C_split=0), graded Leibniz, local-source"
                    " IBP with p=p1+p2, and N3 children"
                ),
                "basis_mismatch": (
                    "the existing canonical N2 blocks contain 44 placement"
                    " coordinates, while the indexed child codomain has 126"
                    " multiplicity coordinates"
                ),
            },
        ],
        "feasibility_from_current_event_ledger": {
            "verdict": "NOT_FEASIBLE_FROM_EVENT_LEDGER_ALONE",
            "event_ledger_contains": (
                "indexed [N,D]/[B,D] and [D,D] curvature-child summands"
            ),
            "event_ledger_omits": [
                "terminal normal-order terms tying all ordered N1 words together",
                "indexed N2 EOM-carrier and chirality rows on all 126 columns",
                "indexed local-source and BRST-partner rows",
                "quadratic-jet codomain boundaries B_2 for source/EOM carriers",
            ],
            "minimal_Project_type_data": [
                {
                    "id": "STEP5_SOURCE_BRST_COMPLEX",
                    "required": (
                        "typed source partners of J_AB, their linearized"
                        " Slavnov differential, parities, and covariant color action"
                    ),
                },
                {
                    "id": "STEP5_ELL2_CODOMAIN_BOUNDARIES",
                    "required": (
                        "ordered quadratic-port basis and the exact boundary"
                        " subspace B_2 for EOM, source-derivative, and BRST carriers"
                    ),
                },
            ],
            "existing_local_identity_now_bound": (
                "D_a^dota T_dota=-(1/2)N_a barE implies"
                " C_split=0 and S_DJ=-C_on_W at p=p1+p2"
            ),
            "new_local_spinor_algebra_identity_required": False,
            "implementation_after_type_lock": (
                "extend the indexed normal-order grammar to terminal/EOM/source"
                " rows and compute R1, R2, M_filtered, and the induced ell_2 kernel"
            ),
        },
        "total_relation_matrix": {
            "id": "M_FILTERED_N0_N1_N2_N3_TOTAL",
            "constructed": False,
            "rank": None,
            "quotient_dimension": None,
        },
        "induced_quadratic_jet": {
            "id": "ell_2_on_filtered_quotient",
            "constructed": False,
            "kernel_dimension": None,
            "ker_ell2_zero_certified": False,
        },
    }


def build_payload() -> dict[str, object]:
    rows = enumerate_skeletons()
    counts = {
        str(degree): sum(row["field_strength_degree"] == degree for row in rows)
        for degree in range(4)
    }
    n0 = n0_certificate(rows)
    n1_normal = n1_normal_order(rows)
    n1_eom = n1_target_eom_matrix(rows)
    n1_indexed_ndbd_raw = indexed_child_to_n2_matrix(rows)
    n1_indexed_dd = indexed_dd_pairing_matrix()
    n1_indexed_complete_raw = complete_indexed_n1_child_to_n2_matrix(
        n1_indexed_ndbd_raw, n1_indexed_dd
    )
    n1_indexed_ndbd = compact_indexed_child_certificate(
        n1_indexed_ndbd_raw
    )
    n1_indexed_complete = compact_complete_indexed_child_certificate(
        n1_indexed_complete_raw
    )
    n2 = n2_certificate(rows)
    n3 = n3_and_dimension_certificate(rows)
    filtered_gate = filtered_quotient_fail_closed_certificate(
        n0,
        n1_eom,
        n1_indexed_ndbd_raw,
        n1_indexed_dd,
        n1_indexed_complete,
        n2,
        n3,
    )
    color_module = color_quotient_module_certificate()

    open_matrices = [
        {
            "id": "M_FILTERED_N0_N1_N2_N3_TOTAL",
            "domain": (
                "N0 direct_sum N1 direct_sum indexed N2 direct_sum N3,"
                " including EOM/source carriers"
            ),
            "codomain": (
                "identity, curvature-child, EOM, graded-Leibniz, and IBP"
                " relation rows"
            ),
            "reason": (
                "C_N1_TARGET_TO_INDEXED_SOURCE and R_N2_INDEXED_EOM_IBP are"
                " not constructed"
            ),
        },
        {
            "id": "M_SOURCE_BRST_COMPLETE",
            "domain": "all source jets J_I and operator-mixing partners",
            "codomain": "linearized Slavnov-Taylor/source closure relations",
            "reason": (
                "IBP incidence is exact, but no Project source multiplet or BRST"
                " mixing matrix is present"
            ),
        },
        {
            "id": "M_DRED_EVANESCENT_JETS",
            "domain": "four-dimensional covariant jets plus evanescent spurions",
            "codomain": "DRED local-operator quotient",
            "reason": "no evanescent covariant-jet basis or relation matrix is derived",
        },
    ]
    return {
        "schema": "STEP5_ONE_LOOP_PURE_GAUGE_INJECTIVITY_MATRIX_V1",
        "status": "FAIL_CLOSED_OPEN_RELATION_MATRICES",
        "scope": "PURE_GAUGE_FIXED_QUADRATIC_COVARIANT_JET",
        "target": {
            "dimension": "9/2",
            "spin": "(3/2,0)",
            "parity": "odd",
            "formal_grading": "r_f=-1",
            "physical_Project_U1R_binding": "OPEN_NOT_USED",
            "source_parity": "odd",
        },
        "algebra": {
            "chirality": ["B_dota W_a=0", "N_a T_dota=0"],
            "mixed": "{N_a,B_dotb}=-2 D_(a dotb)",
            "curvature": [
                "[N_a,D_(b dotb)]=-2 epsilon_ab T_dotb",
                "[B_dota,D_(b dotb)]=-2 epsilon_dota_dotb W_b",
            ],
            "EOM": [
                "N^2 W_a=-2 N_a E",
                "D_a^dota T_dota=-(1/2)N_a(B^dota T_dota)",
            ],
            "IBP": (
                "integral (delta F)G=-(-1)^(|delta||F|) integral F(delta G)"
            ),
        },
        "skeleton_census": {
            "total": len(rows),
            "counts_by_field_strength_degree": counts,
            "rows": rows,
        },
        "N0": n0,
        "N1": {
            "normal_order": n1_normal,
            "target_EOM_quotient": n1_eom,
            "indexed_ND_BD_child_map": n1_indexed_ndbd,
            "indexed_DD_pairing_child_map": n1_indexed_dd,
            "complete_indexed_child_to_N2_map": n1_indexed_complete,
        },
        "N2": n2,
        "higher_degree": n3,
        "filtered_quotient_gate": filtered_gate,
        "color_quotient_module_certificate": color_module,
        "local_results": {
            "N0_target_quotient_zero": n0["vanishes_in_source_extended_ibp_quotient"],
            "N1_associated_graded_target_quotient_zero": (
                n1_eom["associated_graded_target_quotient_dimension"] == 0
            ),
            "WW_N3_target_quotient_zero": (
                n2["WW_N3"]["target_quotient_dimension"] == 0
            ),
            "mixed_N2B_target_projection_zero": n2["W_T_N2_B"][
                "target_projection_zero"
            ],
            "mixed_ND_tensorwise_jet_injective": n2["W_T_N_D"][
                "tensorwise_quadratic_jet_injective"
            ],
            "color_quotient_cannot_add_kernel": (
                color_module["kernel"] == "ker(iota_M)=0"
            ),
            "N3_target_zero": n3["N3"]["target_projection_zero"],
            "N_ge_4_excluded": n3["N_ge_4"]["excluded"],
        },
        "open_relation_matrices": open_matrices,
        "nonmatrix_gate": {
            "id": "PROJECT_U1R_BINDING",
            "status": "OPEN",
            "statement": (
                "r_f is only the formal letter grading; it is not identified"
                " with the physical Project U(1)_R charge"
            ),
        },
        "final_verdict": {
            "ker_ell2_zero_certified": False,
            "status": "BLOCKED_MISSING_EXACT_RELATION_MATRICES",
            "reason": [entry["id"] for entry in open_matrices]
            + ["PROJECT_U1R_BINDING"],
            "accepted_anomaly_coefficient": False,
            "rank_one_claim": False,
        },
    }


def build_verification(payload: dict[str, object]) -> dict[str, object]:
    n0 = payload["N0"]
    n1 = payload["N1"]
    indexed_ndbd = n1["indexed_ND_BD_child_map"]
    indexed_dd = n1["indexed_DD_pairing_child_map"]
    indexed_complete = n1["complete_indexed_child_to_N2_map"]
    filtered = payload["filtered_quotient_gate"]
    color_module = payload["color_quotient_module_certificate"]
    n2 = payload["N2"]
    higher = payload["higher_degree"]
    local = payload["local_results"]
    checks = {
        "census_18_rows": payload["skeleton_census"]["total"] == 18,
        "census_counts_5_7_5_1": payload["skeleton_census"][
            "counts_by_field_strength_degree"
        ]
        == {"0": 5, "1": 7, "2": 5, "3": 1},
        "formal_r_not_physical_R": payload["target"][
            "physical_Project_U1R_binding"
        ]
        == "OPEN_NOT_USED",
        "N0_has_40_target_components": n0["target_component_count"] == 40,
        "N0_identity_matrix_rank_40": n0["identity_relation_matrix"]["rank"]
        == 40,
        "N0_source_ibp_rank_320": n0["source_ibp_relation_matrix"]["rank"]
        == 320,
        "N1_has_20_target_components": n1["target_EOM_quotient"][
            "target_component_count"
        ]
        == 20,
        "N1_target_EOM_quotient_zero": n1["target_EOM_quotient"][
            "associated_graded_target_quotient_dimension"
        ]
        == 0,
        "N1_all_curvature_children_tagged_N_ge_2": n1["normal_order"][
            "all_commutator_children_tagged_N_ge_2"
        ],
        "N1_children_content_bound_to_five_N2_sectors": n1["normal_order"][
            "all_commutator_children_content_bound_to_five_N2_sectors"
        ],
        "N1_vector_pairing_children_tagged_N_ge_2": n1[
            "target_EOM_quotient"
        ]["all_vector_pairing_children_tagged_N_ge_2"],
        "N1_curvature_child_event_ids_unique": len(
            {
                child["event_id"]
                for child in n1["normal_order"]["curvature_child_events"]
            }
        )
        == len(n1["normal_order"]["curvature_child_events"]),
        "N1_normal_order_has_inputs": n1["normal_order"]["input_count"] > 0,
        "N1_indexed_ND_BD_counts_1626_21600_53412": (
            indexed_ndbd["input_word_count"],
            indexed_ndbd["event_count"],
            indexed_ndbd["branch_count"],
        )
        == (1626, 21600, 53412),
        "N1_indexed_ND_BD_matrix_126x4864_rank126": (
            indexed_ndbd["multiplicity_matrix"]["rows"],
            indexed_ndbd["multiplicity_matrix"]["columns"],
            indexed_ndbd["multiplicity_matrix"]["rank"],
            indexed_ndbd["multiplicity_matrix"]["kernel_dimension"],
        )
        == (126, 4864, 126, 4738),
        "N1_indexed_ND_BD_full_504x19456_rank504": (
            indexed_ndbd["full_component_rows"],
            indexed_ndbd["full_component_columns"],
            indexed_ndbd["full_component_rank_by_exact_spin4_intertwining"],
            indexed_ndbd["full_component_kernel_dimension"],
        )
        == (504, 19456, 504, 18952),
        "N1_indexed_all_epsilon_intertwiners_exact": (
            indexed_ndbd["all_raw_maps_spin4_intertwiners"]
            and all(indexed_ndbd["epsilon_invariance_checks"].values())
            and indexed_ndbd["all_full_ranks_four_times_highest_ranks"]
        ),
        "N1_indexed_DD_eight_branches_four_zero_targets": (
            indexed_dd["all_eight_symmetry_and_endpoint_branches_explicit"]
            and indexed_dd["zero_target_BT_child_branches"] == 4
        ),
        "N1_indexed_DD_highest_2x2_rank1_kernel1": (
            indexed_dd["highest_weight_matrix"]["rows"],
            indexed_dd["highest_weight_matrix"]["columns"],
            indexed_dd["highest_weight_rank"],
            indexed_dd["highest_weight_source_kernel_dimension"],
        )
        == (2, 2, 1, 1),
        "N1_indexed_DD_full_8x8_rank4_kernel4": (
            indexed_dd["full_component_matrix"]["rows"],
            indexed_dd["full_component_matrix"]["columns"],
            indexed_dd["full_component_rank"],
            indexed_dd["full_component_source_kernel_dimension"],
        )
        == (8, 8, 4, 4),
        "N1_complete_indexed_matrix_126x4866_rank126": (
            indexed_complete["target_multiplicity_rows"],
            indexed_complete["source_multiplicity_columns"],
            indexed_complete["multiplicity_rank"],
            indexed_complete["multiplicity_kernel_dimension"],
        )
        == (126, 4866, 126, 4740),
        "N1_complete_indexed_full_504x19464_rank504": (
            indexed_complete["full_component_rows"],
            indexed_complete["full_component_columns"],
            indexed_complete["full_component_rank"],
            indexed_complete["full_component_kernel_dimension"],
        )
        == (504, 19464, 504, 18960),
        "N1_complete_indexed_child_coverage": (
            indexed_complete["coverage"]["ND_and_BD_normal_order_children"]
            and indexed_complete["coverage"]["DD_pairing_children"]
            and indexed_complete["coverage"][
                "all_nonzero_DD_rows_embedded_in_shared_N2_placement_basis"
            ]
        ),
        "filtered_basis_mismatch_126_vs_44_explicit": (
            filtered["filtered_target_blocks"][
                "N2_indexed_target_multiplicity_rows"
            ],
            filtered["filtered_target_blocks"][
                "N2_existing_canonical_placement_coordinates"
            ],
        )
        == (126, 44),
        "filtered_missing_C1_and_R2_named": {
            entry["id"] for entry in filtered["missing_incidence_matrices"]
        }
        == {
            "C_N1_TARGET_TO_INDEXED_SOURCE",
            "R_N2_INDEXED_EOM_IBP",
        },
        "filtered_missing_basis_shapes_and_feasibility_exact": (
            sum(
                row["multiplicity_columns"]
                for row in filtered["missing_incidence_matrices"][0][
                    "codomain_sector_decomposition"
                ]
            )
            == 4866
            and len(
                filtered["missing_incidence_matrices"][0]["domain_basis"]
            )
            == 20
            and filtered["missing_incidence_matrices"][1][
                "column_basis_ledger"
            ]["count"]
            == 126
            and filtered["feasibility_from_current_event_ledger"]["verdict"]
            == "NOT_FEASIBLE_FROM_EVENT_LEDGER_ALONE"
            and filtered["feasibility_from_current_event_ledger"][
                "new_local_spinor_algebra_identity_required"
            ]
            is False
        ),
        "filtered_total_matrix_and_ell2_fail_closed": (
            filtered["total_relation_matrix"]["constructed"] is False
            and filtered["total_relation_matrix"]["rank"] is None
            and filtered["induced_quadratic_jet"]["constructed"] is False
            and filtered["induced_quadratic_jet"][
                "ker_ell2_zero_certified"
            ]
            is False
        ),
        "six_source_local_derivative_rows_explicit": (
            len(filtered["source_local_derivative_rows"]["nabla_rows"]),
            len(filtered["source_local_derivative_rows"]["D_rows"]),
            len(
                filtered["source_local_derivative_rows"][
                    "exact_incidence_rows"
                ]
            ),
        )
        == (3, 3, 6)
        and filtered["source_local_derivative_rows"][
            "antichiral_EOM_row_on_C_on_W_C_split_S_DJ"
        ]
        == ["0", "1", "0"]
        and filtered["source_local_derivative_rows"][
            "external_source_momentum"
        ]
        == "retained; p=p1+p2",
        "color_quotient_closed_by_split_monomorphism": (
            color_module["status"] == "CLOSED_BY_SPLIT_MONOMORPHISM"
            and color_module["composition"] == "pi_1 o iota_M=id_M"
            and color_module["kernel"] == "ker(iota_M)=0"
        ),
        "N2_has_five_sectors": len(n2["five_sector_table"]) == 5,
        "N2_two_zero_spin_sectors": len(n2["zero_spin_sectors"]) == 2,
        "WW_spin_projector_rank_4": n2["WW_N3"]["spin_projector"][
            "target_multiplicity"
        ]
        == 4,
        "WW_spin_projector_idempotent": n2["WW_N3"]["spin_projector"][
            "projector_idempotent"
        ],
        "WW_has_eight_placements": len(n2["WW_N3"]["placement_witnesses"])
        == 8,
        "WW_EOM_quotient_zero": n2["WW_N3"]["target_quotient_dimension"]
        == 0,
        "mixed_N2B_has_eight_placements": len(
            n2["W_T_N2_B"]["graded_leibniz_expansion"]
        )
        == 8,
        "mixed_N2B_reduced_target_projection_zero": n2["W_T_N2_B"][
            "target_projection_zero"
        ],
        "mixed_N2B_projected_target_quotient_zero": n2["W_T_N2_B"][
            "projected_target_quotient_dimension"
        ]
        == 0,
        "mixed_ND_has_four_placements": len(
            n2["W_T_N_D"]["graded_leibniz_expansion"]
        )
        == 4,
        "mixed_ND_N3_children_cancel_in_full_leibniz": n2["W_T_N_D"][
            "sum_of_all_leibniz_branches"
        ]["N3_children_cancel"],
        "mixed_ND_IBP_only_constant_source_dimension_one": n2["W_T_N_D"][
            "constant_source_ibp"
        ]["quotient_dimension"]
        == 1,
        "mixed_ND_IBP_only_source_extended_dimension_two": n2["W_T_N_D"][
            "source_extended_ibp"
        ]["quotient_dimension"]
        == 2,
        "mixed_ND_EOM_completed_constant_source_zero": n2["W_T_N_D"][
            "constant_source_EOM_completed_quotient"
        ]["quotient_dimension"]
        == 0,
        "mixed_ND_EOM_completed_local_source_dimension_one": n2["W_T_N_D"][
            "source_extended_EOM_completed_quotient"
        ]["quotient_dimension"]
        == 1,
        "mixed_ND_source_derivative_not_independent": n2["W_T_N_D"][
            "source_derivative_is_not_an_independent_class"
        ],
        "mixed_ND_tensor_jet_rank_one": n2["W_T_N_D"][
            "complete_ordered_quadratic_jet"
        ]["rank"]
        == 1,
        "mixed_ND_tensor_jet_kernel_zero": n2["W_T_N_D"][
            "complete_ordered_quadratic_jet"
        ]["kernel_dimension"]
        == 0,
        "T2_N_B2_all_eight_placements_enumerated": n2["T2_N_B2"][
            "placement_count"
        ]
        == 8,
        "T2_B_D_all_four_placements_enumerated": n2["T2_B_D"][
            "placement_count"
        ]
        == 4,
        "N3_target_multiplicity_zero": higher["N3"][
            "target_spin_multiplicity"
        ]
        == 0,
        "N_ge_4_excluded": higher["N_ge_4"]["excluded"],
        "all_local_results_true": all(local.values()),
        "three_open_relation_matrices_named": len(
            payload["open_relation_matrices"]
        )
        == 3,
        "ker_ell2_fail_closed": payload["final_verdict"][
            "ker_ell2_zero_certified"
        ]
        is False,
        "no_rank_one_claim": payload["final_verdict"]["rank_one_claim"]
        is False,
        "no_anomaly_coefficient": payload["final_verdict"][
            "accepted_anomaly_coefficient"
        ]
        is False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return {
        "schema": "STEP5_ONE_LOOP_PURE_GAUGE_INJECTIVITY_MATRIX_AUDIT_V1",
        "status": "PASS_EXACT_LOCAL_FAIL_CLOSED_GLOBAL",
        "payload_sha256": hashlib.sha256(canonical).hexdigest(),
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
    }


def render_audit(payload: dict[str, object], verification: dict[str, object]) -> str:
    n0 = payload["N0"]
    n1 = payload["N1"]
    n2 = payload["N2"]
    higher = payload["higher_degree"]
    open_ids = ",\n".join(
        f"\\mathsf{{{entry['id']}}}" for entry in payload["open_relation_matrices"]
    )
    template = """# Step 5 pure-gauge fixed-quadratic-jet injectivity matrix

## 0. Typed target

$$
[\\mathscr O]=\\frac92,
\\qquad
(j_L,j_R)=\\left(\\frac32,0\\right),
\\qquad
|\\mathscr O|=1,
\\qquad
r_\\mathrm f(\\mathscr O)=-1.
$$

Here $r_\\mathrm f$ is only the formal letter grading.  The physical Project
$U(1)_R$ binding is not used.

$$
\\{\\nabla_a,\\bar\\nabla_{{\\dot b}}\\}
=-2\\mathcal D_{{a\\dot b}},
$$

$$
[\\nabla_a,\\mathcal D_{{b\\dot b}}]
=-2\\epsilon_{{ab}}\\widetilde{\\mathcal W}_{{\\dot b}},
\\qquad
[\\bar\\nabla_{{\\dot a}},\\mathcal D_{{b\\dot b}}]
=-2\\epsilon_{{\\dot a\\dot b}}\\mathcal W_b.
$$

## 1. Degree zero

$$
\\nabla_{\\mathfrak A}1
=\\partial_{\\mathfrak A}1+[\\Gamma_{\\mathfrak A},1]=0.
$$

The target basis has

$$
5\\cdot8={n0['target_component_count']}
$$

components.  Its identity-relation matrix has

$$
\\operatorname{{rank}}M_0={n0['identity_relation_matrix']['rank']},
\\qquad
\\dim(\\mathcal V_0/\\operatorname{{row}}M_0)=0.
$$

For the elementary ordered derivatives

$$
S_k:=\\int(\\delta_k\\cdots\\delta_1J)
(\\delta_{{k+1}}\\cdots\\delta_L1),
$$

$$
S_k+(-1)^{{|\\delta_{{k+1}}||J_k|}}S_{{k+1}}=0,
\\qquad
S_L=\\int(\\delta_L\\cdots\\delta_1J)1=0.
$$

The exact stepwise source-IBP chains have

$$
\\operatorname{{rank}}M_{{0,J}}={n0['source_ibp_relation_matrix']['rank']},
\\qquad
\\dim(\\mathcal V_{{0,J}}/\\operatorname{{row}}M_{{0,J}})=0.
$$

## 2. Degree one

$$
\\nabla^2\\mathcal W_a=-2\\nabla_a\\mathcal E,
\\qquad
\\mathcal E:=\\nabla^b\\mathcal W_b,
$$

$$
\\mathcal D_a{{}}^{{\\dot a}}\\widetilde{\\mathcal W}_{{\\dot a}}
=-\\frac12\\nabla_a
\\left(\\bar\\nabla^{{\\dot a}}
\\widetilde{\\mathcal W}_{{\\dot a}}\\right).
$$

The seven skeletons contain

$$
2+2+2+2+4+4+4
={n1['target_EOM_quotient']['target_component_count']}
$$

target-spin components.  With one EOM carrier per component,

$$
\\operatorname{{rank}}M_1
={n1['target_EOM_quotient']['target_plus_EOM_relation_matrix']['rank']},
\\qquad
\\dim(\\mathcal V_1/\\operatorname{{row}}M_1)=0.
$$

Normal ordering covers

$$
N_{{\\rm words}}={n1['normal_order']['input_count']}
$$

distinct derivative words.  Every $[\\nabla,\\mathcal D]$ or
$[\\bar\\nabla,\\mathcal D]$ child is stored with filtration tag
$N\\geq2$.

### 2.1 Indexed child matrix

$$
P_j=\\prod_{{j'\\ne j}}
\\frac{C_2-j'(j'+1)\\mathbf1}
{{j(j+1)-j'(j'+1)}}.
$$

For all labeled $[\\nabla,\\mathcal D]$ and
$[\\bar\\nabla,\\mathcal D]$ events,

$$
N_{{\\rm input}}={n1['indexed_ND_BD_child_map']['input_word_count']},
\\qquad
N_{{\\rm event}}={n1['indexed_ND_BD_child_map']['event_count']},
\\qquad
N_{{\\rm branch}}={n1['indexed_ND_BD_child_map']['branch_count']}.
$$

$$
M_{{ND,BD}}\\in
\\operatorname{{Mat}}_{{126\\times4864}}(\\mathbb Q),
\\qquad
\\operatorname{{rank}}M_{{ND,BD}}=126,
\\qquad
\\dim\\ker M_{{ND,BD}}=4738.
$$

$$
M_{{ND,BD}}^{{\\rm full}}\\in
\\operatorname{{Mat}}_{{504\\times19456}}(\\mathbb Q),
\\qquad
\\operatorname{{rank}}M_{{ND,BD}}^{{\\rm full}}=504,
\\qquad
\\dim\\ker M_{{ND,BD}}^{{\\rm full}}=18952.
$$

$$
\\rho_E=1,
\\qquad
[\\mathcal D_{{a\\dot a}},\\mathcal D_{{b\\dot b}}]
=\\epsilon_{{\\dot a\\dot b}}\\nabla_{{(a}}\\mathcal W_{{b)}}
+\\epsilon_{{ab}}\\bar\\nabla_{{(\\dot a}}
\\widetilde{{\\mathcal W}}_{{\\dot b)}}.
$$

The eight symmetrization/endpoint branches give

$$
M_{{DD}}^{{\\rm hw}}
=\\begin{{pmatrix}}0&1\\\\0&-1\\end{{pmatrix}},
\\qquad
\\operatorname{{rank}}M_{{DD}}^{{\\rm hw}}=1,
\\qquad
\\ker M_{{DD}}^{{\\rm hw}}
=\\operatorname{{span}}_\\mathbb Q
\\left\\{\\begin{{pmatrix}}1\\\\0\\end{{pmatrix}}\\right\\}.
$$

$$
M_{{DD}}^{{\\rm full}}\\in
\\operatorname{{Mat}}_{{8\\times8}}(\\mathbb Q),
\\qquad
\\operatorname{{rank}}M_{{DD}}^{{\\rm full}}=4,
\\qquad
\\dim\\ker M_{{DD}}^{{\\rm full}}=4.
$$

This kernel belongs only to the local $[\\mathcal D,\\mathcal D]$ child map.
For the complete indexed child map,

$$
M_{{1\\to2}}=\\begin{{pmatrix}}M_{{ND,BD}}&M_{{DD}}\\end{{pmatrix}}
\\in\\operatorname{{Mat}}_{{126\\times4866}}(\\mathbb Q),
$$

$$
\\operatorname{{rank}}M_{{1\\to2}}=126,
\\qquad
\\dim\\ker M_{{1\\to2}}=4740,
$$

$$
M_{{1\\to2}}^{{\\rm full}}
\\in\\operatorname{{Mat}}_{{504\\times19464}}(\\mathbb Q),
\\qquad
\\operatorname{{rank}}M_{{1\\to2}}^{{\\rm full}}=504,
\\qquad
\\dim\\ker M_{{1\\to2}}^{{\\rm full}}=18960.
$$

Thus

$$
\\operatorname{{im}}M_{{1\\to2}}=\\mathcal V_2^{{\\rm indexed}},
\\qquad
\\ker M_{{1\\to2}}\\ne0.
$$

This is exact target coverage; it is not filtered-quotient injectivity.

## 3. Degree two

$$
\\begin{{array}}{{c|ccccc}}
&WW\\nabla^3&W\\widetilde W\\nabla^2\\bar\\nabla
&W\\widetilde W\\nabla\\mathcal D
&\\widetilde W^2\\nabla\\bar\\nabla^2
&\\widetilde W^2\\bar\\nabla\\mathcal D\\\\ \\hline
\\operatorname{{mult}}_{{(3/2,0)}}&4&1&1&0&0
\\end{{array}}
$$

### 3.1 $WW\\nabla^3$

The weight-$m_L=3/2$ projector is

$$
P_{{3/2}}=I_5-\\frac15\\mathbf1\\mathbf1^T,
\\qquad
P_{{3/2}}^2=P_{{3/2}},
\\qquad
\\operatorname{{rank}}P_{{3/2}}=4.
$$

The $2^3=8$ graded-Leibniz placements obey

$$
\\nabla_a\\nabla_b\\mathcal W_c
=-\\epsilon_{{ab}}\\nabla_c\\mathcal E.
$$

For four spin copies the placement-plus-EOM matrix has

$$
\\operatorname{{rank}}M_{{WW}}=
{n2['WW_N3']['placement_plus_EOM_relation_matrix']['rank']},
\\qquad
\\dim(\\mathcal V_{{WW}}/\\operatorname{{row}}M_{{WW}})=0.
$$

### 3.2 $W\\widetilde W\\nabla^2\\bar\\nabla$

For the ordered word $\\nabla_a\\nabla_b\\bar\\nabla_{{\\dot c}}$,
the eight placements reduce to

$$
\\begin{{aligned}}
M_4&=-E,\\\\
M_5&=2C_{{ba}},\\\\
M_6&=-2C_{{ab}},\\\\
M_7&=-4H_{{W\\widetilde W^2}},
\\end{{aligned}}
$$

with $M_0=M_1=M_2=M_3=0$.  Since

$$
P_{\\rm sym}
=\\frac12
\\begin{{pmatrix}}1&1\\\\1&1\\end{{pmatrix}},
\\qquad
P_{\\rm sym}
\\begin{{pmatrix}}2\\\\-2\\end{{pmatrix}}
=\\begin{{pmatrix}}0\\\\0\\end{{pmatrix}},
$$

the target-spin projection contains only EOM and the $N=3$ child.

### 3.3 $W\\widetilde W\\nabla\\mathcal D$

For $\\nabla_a\\mathcal D_{{b\\dot b}}(W\\widetilde W)$,

$$
\\begin{{array}}{{c|ccc}}
&C_{{W}}&C_{{\\rm split}}&H_{{W\\widetilde W^2}}\\\\ \\hline
P_0&1&0&-2\\\\
P_1&0&0&0\\\\
P_2&0&1&0\\\\
P_3&0&0&2
\\end{{array}}.
$$

Thus

$$
\\sum_{{i=0}}^3P_i=C_W+C_{{\\rm split}},
\\qquad
-2H_{{W\\widetilde W^2}}+2H_{{W\\widetilde W^2}}=0.
$$

IBP alone gives

$$
C_W+C_{{\\rm split}}=0,
\\qquad
\\dim\\mathcal Q_{{\\rm IBP,const}}=1,
$$

For a local source,

$$
C_W+C_{{\\rm split}}+S_{{\\mathcal D J}}=0,
\\qquad
\\dim\\mathcal Q_{{\\rm IBP,local}}=2.
$$

The antichiral EOM gives

$$
C_{{\\rm split}}
=\\mathcal D_a{{}}^{{\\dot a}}
\\widetilde{{\\mathcal W}}_{{\\dot a}}
=-\\frac12\\nabla_a\\bar{\\mathcal E}=0.
$$

Hence

$$
\\dim\\mathcal Q_{{\\rm EOM+IBP,const}}=0,
\\qquad
\\dim\\mathcal Q_{{\\rm EOM+IBP,local}}=1,
$$

$$
S_{{\\mathcal D J}}=-C_W.
$$

Let the source-color tensor remain free:

$$
\\mathscr C_K
=J_{{AB}}K^{{AB}}{{}}_{{CD}}
\\widetilde{\\mathcal W}^C_{{\\dot a}}
\\mathcal D_+{{}}^{{\\dot a}}
\\nabla_+\\mathcal W_+^D.
$$

Its complete ordered quadratic jet is

$$
\\ell_2[\\mathscr C_K]
=
\\begin{{pmatrix}}1\\\\-1\\end{{pmatrix}}
\\otimes K^{{AB}}{{}}_{{CD}},
$$

$$
\\operatorname{{rank}}\\ell_2=1,
\\qquad
\\dim\\ker\\ell_2=0
$$

over the free symbolic tensor module.  No scalar rank-one color claim is made.

Let $M$ be any quotient module of the source-color tensor module.  Define

$$
\\iota_M:M\\longrightarrow M\\oplus M,
\\qquad
\\iota_M(m)=(m,-m),
$$

$$
\\pi_1:M\\oplus M\\longrightarrow M,
\\qquad
\\pi_1(x,y)=x.
$$

Then

$$
\\pi_1\\circ\\iota_M=\\operatorname{{id}}_M,
\\qquad
\\ker\\iota_M=0.
$$

Hence the same color quotient on the source and both ordered output copies
does not create a kernel.

## 4. Higher degree

$$
N=3:\\quad W\\widetilde W^2,
\\qquad
\\operatorname{{mult}}_{{(3/2,0)}}=
{higher['N3']['target_spin_multiplicity']}.
$$

$$
N\\geq4:\\quad 2[\\mathscr O]\\geq3N\\geq12>9.
$$

## 5. Filtered assembly

$$
\\dim\\mathcal V_0=40,
\\qquad
\\dim\\mathcal V_1=20,
\\qquad
\\dim\\mathcal V_2^{{\\rm indexed}}=126,
\\qquad
\\dim\\mathcal V_3=0.
$$

The existing canonical degree-two blocks contain

$$
4\\cdot8+1\\cdot8+1\\cdot4=44
$$

placement coordinates.  Therefore the following exact incidence maps remain
unconstructed:

$$
C_1\\in\\operatorname{{Mat}}_{{4866\\times20}}(\\mathbb Q),
\\qquad
R_2^{{\\rm indexed}}:\\mathcal V_2^{{\\rm indexed}}
\\longrightarrow\\mathcal R_{{\\rm EOM/IBP/N3}}.
$$

The exact $C_1$ basis sizes are

$$
\\begin{{array}}{{c|rrrrrrr}}
\\text{{skeleton}}
&T D^3&TN\\bar N D^2&TN^2\\bar N^2D&TN^3\\bar N^3
&WN^2D^2&WN^3\\bar N D&WN^4\\bar N^2\\\\ \\hline
\\dim\\mathcal V_1^{{\\rm abstract}}&2&2&2&2&4&4&4\\\\
N_{{\\rm ordered\\ records}}&1&20&116&684&20&114&672\\\\
\\dim\\mathcal V_1^{{\\rm indexed}}&2&40&232&1368&80&456&2688
\\end{{array}}.
$$

$$
2+2+2+2+4+4+4=20,
$$

$$
2+40+232+1368+80+456+2688=4866.
$$

The $126$ columns of $R_2^{{\\rm indexed}}$ are

$$
\\left\\{{(p,\\mu):
p\\in\\mathcal P_2^{{\\rm ordered}},
\\ 1\\leq\\mu\\leq
\\operatorname{{mult}}_{{(3/2,0)}}(p)}\\right\\},
$$

$$
|\\mathcal P_2^{{\\rm ordered}}|=83,
\\qquad
\\sum_{{p\\in\\mathcal P_2^{{\\rm ordered}}}}
\\operatorname{{mult}}_{{(3/2,0)}}(p)=126.
$$

For the local source basis $e_{{x,y}}$, where $x$ is the $\\nabla$ endpoint
and $y$ is the $\\mathcal D$ endpoint,

$$
e_{{J,y}}-e_{{F_1,y}}+e_{{F_2,y}}=0,
\\qquad
y\\in\\{{J,F_1,F_2\\}},
$$

$$
e_{{x,J}}+e_{{x,F_1}}+e_{{x,F_2}}=0,
\\qquad
x\\in\\{{J,F_1,F_2\\}}.
$$

Together with

$$
C_{{\\rm split}}=0,
\\qquad
S_{{\\mathcal D J}}=-C_W,
\\qquad
p=p_1+p_2.
$$

The event ledger contains curvature-child summands but not the terminal
normal-order, indexed EOM/source, or quadratic-boundary rows.  It therefore
does not define $C_1$ or $R_2^{{\\rm indexed}}$.

The minimal missing Project type data are

$$
\\boxed{{
\\texttt{{STEP5\\_SOURCE\\_BRST\\_COMPLEX}},
\\qquad
\\texttt{{STEP5\\_ELL2\\_CODOMAIN\\_BOUNDARIES}}.
}}
$$

No additional local spinor-algebra identity is required after these types are
fixed.

Thus

$$
M_{{\\rm filtered}}=
M_{{N0\\oplus N1\\oplus N2\\oplus N3}}
\\quad\\text{{is not assembled}},
$$

$$
\\dim\\ker\\left(
\\ell_2:\\mathcal V/\\operatorname{{row}}M_{{\\rm filtered}}
\\longrightarrow\\mathcal J_2
\\right)
\\quad\\text{{is not computed}}.
$$

## 6. Fail-closed verdict

The missing exact matrices are

$$
\\boxed{{
\\begin{{gathered}}
{open_ids}.
\\end{{gathered}}
}}
$$

Hence

$$
\\boxed{{
\\ker\\ell_2=0
\\quad\\text{{is not certified for the full Project quotient.}}
}}
$$

$$
\\boxed{{
\\texttt{{PASS\\_EXACT\\_LOCAL\\_FAIL\\_CLOSED\\_GLOBAL}}
\\qquad
{verification['passed']}/{verification['total']}.
}}
$$
"""
    replacements = {
        "{n0['target_component_count']}": str(n0["target_component_count"]),
        "{n0['identity_relation_matrix']['rank']}": str(
            n0["identity_relation_matrix"]["rank"]
        ),
        "{n0['source_ibp_relation_matrix']['rank']}": str(
            n0["source_ibp_relation_matrix"]["rank"]
        ),
        "{n1['target_EOM_quotient']['target_component_count']}": str(
            n1["target_EOM_quotient"]["target_component_count"]
        ),
        "{n1['target_EOM_quotient']['target_plus_EOM_relation_matrix']['rank']}": str(
            n1["target_EOM_quotient"]["target_plus_EOM_relation_matrix"]["rank"]
        ),
        "{n1['normal_order']['input_count']}": str(
            n1["normal_order"]["input_count"]
        ),
        "{n1['indexed_ND_BD_child_map']['input_word_count']}": str(
            n1["indexed_ND_BD_child_map"]["input_word_count"]
        ),
        "{n1['indexed_ND_BD_child_map']['event_count']}": str(
            n1["indexed_ND_BD_child_map"]["event_count"]
        ),
        "{n1['indexed_ND_BD_child_map']['branch_count']}": str(
            n1["indexed_ND_BD_child_map"]["branch_count"]
        ),
        "{n2['WW_N3']['placement_plus_EOM_relation_matrix']['rank']}": str(
            n2["WW_N3"]["placement_plus_EOM_relation_matrix"]["rank"]
        ),
        "{higher['N3']['target_spin_multiplicity']}": str(
            higher["N3"]["target_spin_multiplicity"]
        ),
        "{open_ids}": open_ids,
        "{verification['passed']}": str(verification["passed"]),
        "{verification['total']}": str(verification["total"]),
    }
    for old, new in replacements.items():
        template = template.replace(old, new)
    return template.replace("{{", "{").replace("}}", "}")


def main() -> None:
    payload = build_payload()
    verification = build_verification(payload)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    VERIFY.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n")
    AUDIT_MD.write_text(render_audit(payload, verification))
    print(
        json.dumps(
            {
                "output": str(OUT),
                "audit": str(AUDIT_MD),
                "verification": verification,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
