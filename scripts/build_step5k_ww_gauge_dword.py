#!/usr/bin/env python3
"""Build and verify the Step-5K WW gauge D-word contact rows."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "generated" / "step5k-ww-gauge-dword.json"
MEMO_EQUATIONS = ("K.55--K.64", "K.65--K.76f", "K.87--K.96", "K.122")

CHIRALITIES = ("+", "-")
RAW_MONOMIALS = ("0001", "0010", "0100", "1000")
PLACEMENTS = (
    "derivative_commutator",
    "linear_field_strength",
    "plain_commutator",
)
ENDPOINT_ORDERS = ("BS", "SB")

EXTERNAL_SLOT = {
    "0001": {
        "derivative_commutator": "Y",
        "linear_field_strength": "X",
        "plain_commutator": "Z",
    },
    "0010": {
        "derivative_commutator": "Z",
        "linear_field_strength": "X",
        "plain_commutator": "Y",
    },
    "0100": {
        "derivative_commutator": "X",
        "linear_field_strength": "Z",
        "plain_commutator": "Y",
    },
    "1000": {
        "derivative_commutator": "Y",
        "linear_field_strength": "Z",
        "plain_commutator": "X",
    },
}

PLUS_RAW_SIGN = {
    "0001": -1,
    "0010": +1,
    "0100": -1,
    "1000": +1,
}

CANONICAL_LEDGER = {
    "canonical_source_marked_times_unmarked":
        "(-1/(8*sqrt(2)))*(-1/(4*sqrt(2)))=1/64",
    "closed_delta": 16,
    "same_edge_anticommutator_factor_left": 2,
    "same_edge_anticommutator_factor_right": 2,
    "D_weight": "(1/64)*16*2*2=1",
    "action_order_factor":
        "(1/2!)*(S_plus*S_minus+S_minus*S_plus)=1",
    "port_preserving_wick_factor": 1,
    "exponent_vertex_W": "-i*g/(4*hbar)",
    "exponent_vertex_barW": "+i*g/(4*hbar)",
    "three_canonical_vector_propagators": "(-hbar)^3",
    "vertices_times_propagators":
        "(-i*g/(4*hbar))*(+i*g/(4*hbar))*(-hbar)^3=-hbar*g^2/16",
    "global_odd_source_loop_IBP_sign": -1,
    "fixed_parent_prefactor": "+hbar*g^2/16",
    "selected_square_minus_cut":
        "-4*(bar(L)^2-L_d^2)*sigma.p=-4*mu_L^2*sigma.p",
    "simplex_factor": "2*int_Sigma2(1)=1",
    "evanescent_master":
        "int d^dL/(2*pi)^d mu_L^2/(L^2+Delta)^3=1/(32*pi^2)",
    "isolated_directed_result":
        "-hbar*g^2/(128*pi^2)=-lambda1/8",
}

FP_BLOCK = {
    "kernel_K_E_FP": [
        ["0", "+(i/4)*barD^2"],
        ["-(i/4)*D^2", "0"],
    ],
    "inverse_bar4": [
        ["0", "+(i/4)*barBox_E^-1*barD^2"],
        ["-(i/4)*barBox_E^-1*D^2", "0"],
    ],
    "inverse_d": [
        ["0", "+(i/4)*Box_d^-1*barD^2"],
        ["-(i/4)*Box_d^-1*D^2", "0"],
    ],
    "right_inverse_check":
        "K_E^FP*inverse_bar4=diag(P_+^bar4,P_-^bar4)=1_Fperp",
    "left_inverse_check":
        "inverse_bar4*K_E^FP=diag(P_+^bar4,P_-^bar4)=1_Gperp",
    "regulated_right_defect": "mu_r^2/r_d^2",
    "regulated_left_defect": "mu_r^2/r_d^2",
    "cubic_vertex":
        "(i*g/(4*sqrt(2)))*[int_+ c'_+*barD^2[tilde(c)+c,u]"
        "+int_- tilde(c)'_-*D^2[tilde(c)+c,u]]",
    "one_loop_candidate":
        "I1_source*S_FP3 with one vector edge and one same-vertex ghost edge",
    "candidate_verdict": "EXACT_ZERO",
    "zero_reason":
        "delta4(Q) for generic Q; at Q=0 every remaining DRED integral is scaleless",
    "two_cubic_vertex_graph_loop_number": "I-V+1=4-3+1=2",
}


def assignment_for(
    raw_monomial: str,
    placement: str,
    endpoint_order: str,
) -> tuple[dict[str, str], str, str]:
    external_slot = EXTERNAL_SLOT[raw_monomial][placement]
    quantum_slots = "".join(slot for slot in "XYZ" if slot != external_slot)
    assignment = {external_slot: "E"}
    assignment[quantum_slots[0]] = endpoint_order[0]
    assignment[quantum_slots[1]] = endpoint_order[1]
    assignment = {slot: assignment[slot] for slot in "XYZ"}
    return assignment, external_slot, quantum_slots


def raw_sign(chirality: str, raw_monomial: str) -> int:
    sign = PLUS_RAW_SIGN[raw_monomial]
    return sign if chirality == "+" else -sign


def build_row(
    chirality: str,
    raw_monomial: str,
    placement: str,
    endpoint_order: str,
) -> dict[str, Any]:
    assignment, external_slot, quantum_slots = assignment_for(
        raw_monomial,
        placement,
        endpoint_order,
    )
    row_suffix = "".join(assignment[slot] for slot in "XYZ")
    row_id = f"{chirality}:{raw_monomial}:{row_suffix}"
    sign = raw_sign(chirality, raw_monomial)
    signed_coefficient = "+" if sign == 1 else "-"

    if endpoint_order == "SB":
        edge_tags = {"T0": ["e0", "e1"], "T2": ["e2", "e1"]}
        endpoint_rule = "KEEP_SB"
    else:
        edge_tags = {"T0": ["e1", "e0"], "T2": ["e1", "e2"]}
        endpoint_rule = "EVEN_SWAP_BS_TO_SB"

    assignment_json = json.dumps(
        assignment,
        separators=(",", ":"),
        sort_keys=False,
    )

    return {
        "row_id": row_id,
        "hessian_group_id":
            f"{chirality}:{raw_monomial}:{placement}",
        "chirality": chirality,
        "raw_monomial": raw_monomial,
        "external_placement": placement,
        "input_word": (
            f"c_{chirality}*Tr(W_{chirality}^(1)(X={assignment['X']})"
            f"*[mathscrD_{chirality}(Y={assignment['Y']}),"
            f"Z={assignment['Z']}])::{raw_monomial}"
        ),
        "coefficient_canonical_u":
            f"{signed_coefficient}1*sqrt(2)*g/256",
        "quantum_slots": quantum_slots,
        "ordered_quantum_roles": endpoint_order,
        "edge_tags": edge_tags,
        "raw_sign": sign,
        "ordered_transfers": [
            {
                "rule": "POLARIZED_SLOT_TO_ROLE",
                "sign": 1,
                "before": f"XYZ={assignment_json}",
                "after":
                    f"external={external_slot},quantum={quantum_slots}",
            },
            {
                "rule": endpoint_rule,
                "sign": 1,
                "before": endpoint_order,
                "after": "SB",
            },
            {
                "rule": "SOURCE_ROLE_TO_MARKED_EDGE",
                "sign": 1,
                "before": "S",
                "after": "T0:e0,T2:e2",
            },
            {
                "rule": "GAUSSIAN_SD_SAME_EDGE",
                "sign": -1,
                "before": "N_d,rho",
                "after": "K_raw,rho=-N_d,rho",
            },
        ],
        "transport_sign": 1,
        "sd_contact_sign": -1,
        "delta_saturation": {
            "rule": "CLOSED_GRASSMANN_LOOP",
            "factor": 16,
            "before": "delta4(theta)*D^2*barD^2*delta4(theta)",
            "after": "16*delta4(theta)",
        },
        "local_output": {
            "parent": "N_d,rho=L_rho+Q_rho*r_(e,d)^2",
            "contact": "K_raw,rho=-L_rho-Q_rho*r_(e,d)^2",
            "full_d_sum": "N_d,rho+K_raw,rho=0",
            "dred_sum":
                "N_full,rho+K_raw,rho=Q_rho*mu_ell^2",
        },
        "terminal_class": {
            "contact": "PAIRED_CONTACT",
            "eom": "EOM_IF_Q_CARRIER",
            "anomaly": "ANOMALY_CANDIDATE_QRHO_MU2",
            "verdict": "PAIRED_CONTACT",
        },
    }


def build_rows() -> list[dict[str, Any]]:
    return [
        build_row(chirality, raw_monomial, placement, endpoint_order)
        for chirality in CHIRALITIES
        for raw_monomial in RAW_MONOMIALS
        for placement in PLACEMENTS
        for endpoint_order in ENDPOINT_ORDERS
    ]


def validate_rows(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    row_ids = [row["row_id"] for row in rows]
    group_ids = [row["hessian_group_id"] for row in rows]
    group_counts = Counter(group_ids)

    if len(rows) != 48:
        errors.append(f"row count {len(rows)} != 48")
    if len(set(row_ids)) != 48:
        errors.append(f"unique row-id count {len(set(row_ids))} != 48")
    if len(set(group_ids)) != 24:
        errors.append(f"group count {len(set(group_ids))} != 24")
    if set(group_counts.values()) != {2}:
        errors.append(
            "endpoint/group multiplicities are "
            f"{sorted(group_counts.values())}, expected only 2"
        )
    return errors


def compare_rows(
    expected: list[dict[str, Any]],
    actual: list[dict[str, Any]],
) -> list[str]:
    if expected == actual:
        return []
    errors = ["full_contact_rows differs from deterministic build"]
    for index, (expected_row, actual_row) in enumerate(
        zip(expected, actual, strict=False)
    ):
        if expected_row != actual_row:
            errors.append(
                f"first mismatch at index {index}: "
                f"expected {expected_row.get('row_id')}, "
                f"actual {actual_row.get('row_id')}"
            )
            break
    if len(expected) != len(actual):
        errors.append(
            f"expected {len(expected)} rows, actual {len(actual)}"
        )
    return errors


def check_document(document: dict[str, Any]) -> list[str]:
    expected_rows = build_rows()
    actual_rows = document.get("full_contact_rows", [])
    errors = validate_rows(expected_rows)
    errors.extend(compare_rows(expected_rows, actual_rows))

    if document.get("graph_id") != "G-WW-GAUGE-01":
        errors.append("graph_id != G-WW-GAUGE-01")
    if document.get("generated") is not True:
        errors.append("generated marker is not true")
    if document.get("coefficient_ledger") != CANONICAL_LEDGER:
        errors.append("canonical coefficient ledger mismatch")
    if document.get("fp_block") != FP_BLOCK:
        errors.append("typed FP block mismatch")
    if document.get("unresolved") != []:
        errors.append("unresolved must be []")
    if tuple(document.get("memo_equations", [])) != MEMO_EQUATIONS:
        errors.append("memo equation map mismatch")

    local_algebra = document.get("fourier_and_local_algebra", {})
    if (
        local_algebra.get("same_edge_anticommutator")
        != "{D_alpha(r_i),barD_dotbeta(r_i)}=-2*i*r_i_(alpha,dotbeta)"
    ):
        errors.append("same-edge anticommutator normalization mismatch")
    rewrites = {
        row.get("rewrite_id"): row
        for row in document.get("ordered_local_rewrites", [])
    }
    left = rewrites.get("W1_LEFT_SAME_EDGE_ROW_SUM", {})
    right = rewrites.get("W2_RIGHT_SAME_EDGE_ROW_SUM", {})
    endpoint_sum = rewrites.get("W4_FOUR_ENDPOINT_ROW_SUM", {})
    if (
        left.get("common_factor") != 2
        or left.get("row_rewrites")
        != [
            "{D_+(r0),barD_dotbeta(r0)}=-2*i*r0_(+,dotbeta)",
            "{D_+(r1),barD_dotbeta(r1)}=-2*i*r1_(+,dotbeta)",
        ]
        or left.get("after")
        != "-2*i*(r0+r1)_(+,dotbeta)=-2*i*L1_(+,dotbeta)"
    ):
        errors.append("left same-edge endpoint row sum mismatch")
    if (
        right.get("common_factor") != 2
        or right.get("row_rewrites")
        != [
            "{D_gamma(r1),barD^dotalpha(r1)}=-2*i*r1_gamma^dotalpha",
            "{D_gamma(r2),barD^dotalpha(r2)}=-2*i*r2_gamma^dotalpha",
        ]
        or right.get("after")
        != "-2*i*(r1+r2)_gamma^dotalpha=-2*i*L2_gamma^dotalpha"
    ):
        errors.append("right same-edge endpoint row sum mismatch")
    if (
        endpoint_sum.get("row_numerators")
        != [
            "R01:(-1)*[-4*N_01]=+4*N_01",
            "R02:(-1)*[-4*N_02]=+4*N_02",
            "R11:(-1)*[-4*N_11]=+4*N_11",
            "R12:(-1)*[-4*N_12]=+4*N_12",
        ]
        or endpoint_sum.get("after")
        != "4*sum_(i=0,1;j=1,2)N_ij=4*(r0+r1)*(i*p)*(r1+r2)=4*N_T"
    ):
        errors.append("four endpoint selected-row sum mismatch")

    invariants = document.get("invariants", {})
    required_invariants = {
        "full_contact_row_count": 48,
        "full_contact_unique_row_id_count": 48,
        "full_hessian_group_count": 24,
        "endpoints_per_hessian_group": 2,
        "source_mark_count": 2,
        "unresolved_count": 0,
    }
    for key, expected_value in required_invariants.items():
        if invariants.get(key) != expected_value:
            errors.append(
                f"invariant {key}={invariants.get(key)!r}, "
                f"expected {expected_value!r}"
            )

    isolated = document.get("isolated_directed_result", {})
    if isolated.get("value") != "-lambda1/8":
        errors.append("isolated directed result != -lambda1/8")
    full_orbit = document.get("full_gauge_orbit_result", {})
    if (
        full_orbit.get("not_equal_to_single_triangle_integral") is not True
        or full_orbit.get("derived_by_this_generator") is not False
        or full_orbit.get("source")
        != "audits/step5-aa-external-slot-decomposition-exact.json"
    ):
        errors.append("isolated/full-orbit scope split is not locked")
    return errors


def write_document(document: dict[str, Any]) -> None:
    rows = build_rows()
    document["full_contact_rows"] = rows
    document["coefficient_ledger"] = CANONICAL_LEDGER
    document["fp_block"] = FP_BLOCK
    document["unresolved"] = []
    document["memo_equations"] = list(MEMO_EQUATIONS)
    invariants = document.setdefault("invariants", {})
    invariants.update({
        "full_contact_row_count": 48,
        "full_contact_unique_row_id_count": 48,
        "full_hessian_group_count": 24,
        "endpoints_per_hessian_group": 2,
        "source_mark_count": 2,
        "unresolved_count": 0,
    })
    TARGET.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if args.write:
        document = json.loads(TARGET.read_text(encoding="utf-8"))
        write_document(document)
        print(f"WROTE {TARGET}")
        return 0

    if not args.check:
        print(json.dumps(build_rows(), indent=2, ensure_ascii=False))
        return 0

    document = json.loads(TARGET.read_text(encoding="utf-8"))
    errors = check_document(document)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(
        "PASS G-WW-GAUGE-01: "
        "48 rows, 48 unique IDs, 24 groups, 2 endpoints/group, "
        "canonical ledger, unresolved=[], memo equations K.55--K.122"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
