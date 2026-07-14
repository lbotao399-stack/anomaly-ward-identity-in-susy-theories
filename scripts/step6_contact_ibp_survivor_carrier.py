#!/usr/bin/env python3
"""Build the fail-closed residual-contact IBP carrier.

The input is the frozen ``bcdfe0c`` preaggregation replay.  This compiler
moves the residual ``e_AI`` spinor word from the integrated ``theta_A``
delta endpoint onto the two ordered A-local factors.  It does not identify
those factors with I3 grammar ports and it does not run post-IBP primitive
normal ordering, chirality, or color reduction.
"""

from __future__ import annotations

import hashlib
import gzip
import io
import json
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

import step6_preaggregation_measure_delta_replay as preaggregation


ROOT = Path(__file__).resolve().parents[1]
GENERATED = (
    ROOT
    / "generated/step6/contact-ibp-survivor-carrier/contact-ibp-survivor-carrier.json.gz"
)
AUDIT = ROOT / "audits/step6-contact-ibp-survivor-carrier-verification.json"
TEST_PATH = ROOT / "tests/test_step6_contact_ibp_survivor_carrier.py"
REPLAY_SCRIPT = ROOT / "scripts/step6_preaggregation_measure_delta_replay.py"
REPLAY_FIXTURE = (
    ROOT
    / "generated/step6/measure-tagged-delta-convolution/measure-tagged-delta-convolution.json"
)
REPLAY_SUMMARY = (
    ROOT / "generated/step6/preaggregation-measure-delta-replay/"
    "preaggregation-measure-delta-replay-summary.json"
)
REPLAY_AUDIT = (
    ROOT / "audits/step6-preaggregation-measure-delta-replay-verification.json"
)
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
I3_BASIS = ROOT / "generated/step6/coefficient-tensor/coefficient-tensor-programs.json"

SCHEMA = "step6.contact_ibp_survivor_carrier.v1"
STATUS = "PASS_TYPED_IBP_EVENT_CARRIER__I3_LOCAL_SURVIVOR_COMPARISON_OPEN"
RESOLVED_TYPE_ID = "TYPE::EdgeTaggedContactIBPEventCarrier"
ORIGINAL_MISSING_TYPE_ID = "MISSING_TYPE::EdgeTaggedContactIBPToALocalSurvivors"
OPEN_TYPE_IDS = (
    "MISSING_TYPE::CollapsedContactEndpointColorAndI3PortBinding",
    "MISSING_TYPE::PostIBPPrimitiveNormalForm",
    "MISSING_TYPE::I3LocalSurvivorComparisonMatrix",
)
SOURCE_COMMIT = "bcdfe0c"
EXPECTED_REPLAY_PAYLOAD_SHA256 = (
    "fa7118bb2f672f12e372db16e752b388eee6b24459b6326edf7f434def9e2508"
)
EXPECTED_REPLAY_AGGREGATE_ROWS_SHA256 = (
    "6f3f81d50dae92e9b28788b299c2d7e6bdbf6b06256af3dd6805bf05d39e0f77"
)
EXPECTED_REPLAY_CONTACT_CATALOG_SHA256 = (
    "1918745eafd2970e942209ff312efb2bd342b745d2cf1ace3d9fe3d06fa2de0a"
)
EXPECTED_INPUT_FILE_SHA256 = {
    "scripts/step6_preaggregation_measure_delta_replay.py": (
        "cab350456eb126fd517c4aada40a28dba2405e0aa1f4d539959517d7ee54af4d"
    ),
    "generated/step6/measure-tagged-delta-convolution/"
    "measure-tagged-delta-convolution.json": (
        "b5ecf1ac6a471f7a6d75158d502ec6a869fe5d0bce6599343f285b7cf404a940"
    ),
    "generated/step6/preaggregation-measure-delta-replay/"
    "preaggregation-measure-delta-replay-summary.json": (
        "5e6e345c76619952e1c6efebba04c2892bb3ae55c378f61bd418a7ce8377f442"
    ),
    "audits/step6-preaggregation-measure-delta-replay-verification.json": (
        "616fe3e5ece0a9baa5886cdf472880dcf6d49cb6c14af3da3db9219c39ae9bc2"
    ),
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md": (
        "5b24afd355ef0d471e859c37a24a15632fcebdcad3aa654d30dc098647939ab5"
    ),
    "generated/step6/coefficient-tensor/coefficient-tensor-programs.json": (
        "1d5fd2c13e30f0dc315d819d2c3c8f4213d832e386c72aee32be77843548f126"
    ),
}
INPUT_PATHS = {
    "scripts/step6_preaggregation_measure_delta_replay.py": REPLAY_SCRIPT,
    "generated/step6/measure-tagged-delta-convolution/"
    "measure-tagged-delta-convolution.json": REPLAY_FIXTURE,
    "generated/step6/preaggregation-measure-delta-replay/"
    "preaggregation-measure-delta-replay-summary.json": REPLAY_SUMMARY,
    "audits/step6-preaggregation-measure-delta-replay-verification.json": (
        REPLAY_AUDIT
    ),
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md": CONTRACT,
    "generated/step6/coefficient-tensor/coefficient-tensor-programs.json": I3_BASIS,
}

TOKEN_TO_PRIMITIVE = {
    ("D", "+"): "D_plus",
    ("BAR_D", "dot+"): "barD_dotplus",
    ("BAR_D", "dot-"): "barD_dotminus",
}
EXPECTED_TOKEN_WORD_CENSUS = {
    ("D_plus",): 192,
    ("barD_dotplus", "D_plus"): 160,
    ("barD_dotminus", "D_plus"): 160,
    ("barD_dotplus", "barD_dotminus", "D_plus"): 96,
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _payload_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _payload_gzip_bytes(payload: Mapping[str, Any]) -> bytes:
    source = _payload_json_bytes(payload)
    output = io.BytesIO()
    with gzip.GzipFile(
        filename="",
        mode="wb",
        compresslevel=9,
        fileobj=output,
        mtime=0,
    ) as stream:
        stream.write(source)
    return output.getvalue()


def _record_with_hash(core: Mapping[str, Any]) -> dict[str, Any]:
    record = dict(core)
    record["record_sha256"] = digest(record)
    return record


def _record_hash_valid(record: Mapping[str, Any]) -> bool:
    return bool(record.get("record_sha256")) and record["record_sha256"] == digest(
        {key: value for key, value in record.items() if key != "record_sha256"}
    )


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _input_hashes() -> dict[str, str]:
    return {name: file_sha256(path) for name, path in INPUT_PATHS.items()}


def _primitive(token: Mapping[str, Any]) -> str:
    key = (str(token["derivative_kind"]), str(token["spinor_component"]))
    if key not in TOKEN_TO_PRIMITIVE:
        raise AssertionError(f"unregistered residual token: {key}")
    return TOKEN_TO_PRIMITIVE[key]


def _signed_qi(value: Mapping[str, Any], sign: int) -> dict[str, str]:
    if sign not in (-1, 1):
        raise AssertionError("IBP sign is not binary")
    return {
        "domain": "Q(i)",
        "re": str(Fraction(str(value["re"])) * sign),
        "im": str(Fraction(str(value["im"])) * sign),
    }


def _normalize_ast_primitive(token: str) -> str:
    table = {
        "D_plus": "D_plus",
        "D_minus": "D_minus",
        "barD_dot_plus": "barD_dotplus",
        "barD_dot_minus": "barD_dotminus",
    }
    if token not in table:
        raise AssertionError(f"unregistered AST primitive: {token}")
    return table[token]


def _i3_port_words(
    node: Mapping[str, Any],
    outer_word: tuple[str, ...] = (),
) -> list[tuple[str, tuple[str, ...]]]:
    op = str(node["op"])
    args = list(node.get("args", []))
    word = outer_word
    if op == "FlatD":
        word += ({"+": "D_plus", "-": "D_minus"}[str(node["attrs"]["index"])],)
    elif op == "FlatBarD":
        index = str(node["attrs"]["index"])
        if index != "dot_a":
            raise AssertionError("I3 FlatBarD has an unregistered concrete index")
        word += ("barD_dot_a",)
    elif op in {"D2", "BarD2"}:
        ordered = tuple(
            _normalize_ast_primitive(str(token))
            for token in node["attrs"]["ordered_word"]
        )
        word += ordered
    if op == "V":
        return [(str(node["attrs"]["port_id"]), word)]
    output: list[tuple[str, tuple[str, ...]]] = []
    for child in args:
        output.extend(_i3_port_words(child, word))
    return output


def _load_i3_target_basis() -> list[dict[str, Any]]:
    payload = _load_json(I3_BASIS)
    if payload["schema"] != "step6.coefficient_tensor_program_ir.v1":
        raise AssertionError("I3 target basis schema changed")
    terms = payload["tensor_programs"]["compiled_terms"]
    result = []
    for term_id, term in sorted(terms.items()):
        if term["family"] != "I3":
            continue
        words = _i3_port_words(term["expression_ast"])
        if len(words) != 3 or set(port for port, _ in words) != set(term["port_order"]):
            raise AssertionError("I3 target term is not a typed three-port object")
        word_rows = [
            {"grammar_port_id": port, "word_outer_to_inner": list(word)}
            for port, word in words
        ]
        result.append(
            {
                "term_id": str(term_id),
                "coefficient_raw": deepcopy(term["coefficient_raw"]),
                "port_order": list(term["port_order"]),
                "port_words": word_rows,
                "ordered_word_signature_sha256": digest(word_rows),
                "sorted_port_degrees": sorted(len(word) for _, word in words),
                "total_spinor_derivative_degree": sum(len(word) for _, word in words),
                "expression_ast_sha256": str(term["expression_ast_sha256"]),
                "color_ast_sha256": str(term["color_ast_sha256"]),
            }
        )
    if len(result) != 10:
        raise AssertionError("I3 target basis no longer has ten terms")
    return result


def _local_slots(
    contact: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    signature = list(contact["survivor_signature"])
    if len(signature) != 3:
        raise AssertionError("contact does not have three survivors")
    if {str(row["edge_id"]) for row in signature[:2]} != {"e_BA", "e_CA"}:
        raise AssertionError("the first two survivors are not A-local")
    if str(signature[2]["edge_id"]) != "e_IB":
        raise AssertionError("the protected survivor is not I-local")
    local = []
    for ordinal, survivor in enumerate(signature[:2], start=1):
        word = [str(token) for token in survivor["word_outer_to_inner"]]
        local.append(
            {
                "local_slot_id": f"A.q{ordinal}",
                "local_slot_namespace": "COLLAPSED_CONTACT_LOCAL_ORDER",
                "edge_id": str(survivor["edge_id"]),
                "coordinate": "theta_A",
                "base_word_outer_to_inner": word,
                "base_parity": len(word) % 2,
                "theta_A_IBP_eligible": True,
                "endpoint_class": "BOUNDARY_UNRESOLVED_OUTGOING_PORT",
            }
        )
    protected_word = [str(token) for token in signature[2]["word_outer_to_inner"]]
    protected = {
        "local_slot_id": "I.q1",
        "local_slot_namespace": "COLLAPSED_CONTACT_LOCAL_ORDER",
        "edge_id": "e_IB",
        "coordinate": "theta_I",
        "base_word_outer_to_inner": protected_word,
        "base_parity": len(protected_word) % 2,
        "theta_A_IBP_eligible": False,
        "endpoint_class": "BOUNDARY_UNRESOLVED_OUTGOING_PORT",
        "exclusion_rule_id": "R-IBP-THETA-I-BARRIER",
    }
    return local, protected


def _ibp_branches(
    contact: Mapping[str, Any],
    local_slots: Sequence[Mapping[str, Any]],
    protected_slot: Mapping[str, Any],
    i3_targets: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    residual = [_primitive(token) for token in contact["remaining_e_AI_tokens"]]
    states: list[dict[str, Any]] = [
        {
            "sign": 1,
            "assignment": [],
            "slot_words": [
                list(local_slots[0]["base_word_outer_to_inner"]),
                list(local_slots[1]["base_word_outer_to_inner"]),
            ],
            "slot_parities": [
                int(local_slots[0]["base_parity"]),
                int(local_slots[1]["base_parity"]),
            ],
            "events": [],
        }
    ]
    for ordinal, primitive in enumerate(residual):
        next_states: list[dict[str, Any]] = []
        for state in states:
            total_parity = sum(state["slot_parities"]) % 2
            ibp_exponent = (1 + total_parity) % 2
            ibp_sign = -1 if ibp_exponent else 1
            for target_index in (0, 1):
                target = local_slots[target_index]
                leibniz_exponent = (
                    int(state["slot_parities"][0]) if target_index == 1 else 0
                )
                leibniz_sign = -1 if leibniz_exponent else 1
                step_sign = ibp_sign * leibniz_sign
                slot_words = deepcopy(state["slot_words"])
                slot_parities = list(state["slot_parities"])
                word_before = list(slot_words[target_index])
                slot_words[target_index] = [primitive, *word_before]
                slot_parities[target_index] ^= 1
                event_core = {
                    "type_id": "TYPE::EdgeTaggedContactIBPEvent",
                    "rule_id": "R-SUPERSPACE-IBP-5.53",
                    "source_contact_group_id": str(contact["aggregate_group_id"]),
                    "event_ordinal": ordinal,
                    "derivative_primitive": primitive,
                    "derivative_parity": 1,
                    "source_delta_endpoint": "delta.theta_A.source",
                    "integrated_coordinate": "theta_A",
                    "unintegrated_coordinate": "theta_I",
                    "target_local_slot_id": str(target["local_slot_id"]),
                    "target_edge_id": str(target["edge_id"]),
                    "product_factor_parities_before": list(state["slot_parities"]),
                    "total_product_parity_before": total_parity,
                    "ibp_sign_exponent_mod_2": ibp_exponent,
                    "ibp_sign": ibp_sign,
                    "graded_leibniz_sign_exponent_mod_2": leibniz_exponent,
                    "graded_leibniz_sign": leibniz_sign,
                    "step_sign": step_sign,
                    "target_word_before": word_before,
                    "target_word_after": list(slot_words[target_index]),
                    "active_delta_word_before": residual[ordinal:],
                    "active_delta_word_after": residual[ordinal + 1 :],
                    "boundary_token": {
                        "type_id": "TYPE::EdgeTaggedBoundaryDerivativeToken",
                        "primitive": primitive,
                        "edge_id": str(target["edge_id"]),
                        "endpoint_binding": None,
                        "disposition": "RETAIN_UNTIL_ENDPOINT_BINDING",
                        "if_external": (
                            "RETYPE_AS_TYPE::ExternalLegDerivativeToken_AND_NEVER_DELETE"
                        ),
                        "if_internal": (
                            "REQUIRE_RULE_5.53c_WITH_EXPLICIT_MOMENTUM_LABELS"
                        ),
                    },
                    "invariants": {
                        "theta_I_slot_not_hit": True,
                        "one_delta_token_removed": True,
                        "one_boundary_token_emitted": True,
                        "operator_adjoint_order_reversed_by_prepend": True,
                    },
                }
                event = _record_with_hash(event_core)
                next_states.append(
                    {
                        "sign": int(state["sign"]) * step_sign,
                        "assignment": [
                            *state["assignment"],
                            str(target["local_slot_id"]),
                        ],
                        "slot_words": slot_words,
                        "slot_parities": slot_parities,
                        "events": [*state["events"], event],
                    }
                )
        states = next_states

    branches = []
    target_by_degree = {
        str(target["term_id"]): tuple(target["sorted_port_degrees"])
        for target in i3_targets
    }
    target_word_signatures = {
        str(target["term_id"]): tuple(
            tuple(row["word_outer_to_inner"]) for row in target["port_words"]
        )
        for target in i3_targets
    }
    for state in states:
        ordered_words = (
            tuple(state["slot_words"][0]),
            tuple(state["slot_words"][1]),
            tuple(protected_slot["base_word_outer_to_inner"]),
        )
        sorted_degrees = tuple(sorted(len(word) for word in ordered_words))
        degree_candidates = sorted(
            term_id
            for term_id, degrees in target_by_degree.items()
            if degrees == sorted_degrees
        )
        ordered_matches = sorted(
            term_id
            for term_id, signature in target_word_signatures.items()
            if signature == ordered_words
        )
        permutation_matches = sorted(
            term_id
            for term_id, signature in target_word_signatures.items()
            if sorted(signature) == sorted(ordered_words)
        )
        branch_core = {
            "type_id": "TYPE::ALocalIBPCoproductBranch",
            "source_contact_group_id": str(contact["aggregate_group_id"]),
            "assignment_outer_to_inner_transfer_order": list(state["assignment"]),
            "ibp_branch_sign": int(state["sign"]),
            "edge_square_quotient_before_ibp": deepcopy(
                contact["edge_square_quotient"]
            ),
            "exact_coefficient_after_ibp": _signed_qi(
                contact["edge_square_quotient"], int(state["sign"])
            ),
            "A_local_survivors": [
                {
                    "local_slot_id": "A.q1",
                    "edge_id": str(local_slots[0]["edge_id"]),
                    "word_outer_to_inner": list(state["slot_words"][0]),
                    "parity": int(state["slot_parities"][0]),
                },
                {
                    "local_slot_id": "A.q2",
                    "edge_id": str(local_slots[1]["edge_id"]),
                    "word_outer_to_inner": list(state["slot_words"][1]),
                    "parity": int(state["slot_parities"][1]),
                },
            ],
            "protected_I_local_survivor": {
                "local_slot_id": "I.q1",
                "edge_id": "e_IB",
                "word_outer_to_inner": list(protected_slot["base_word_outer_to_inner"]),
                "parity": int(protected_slot["base_parity"]),
                "received_theta_A_IBP_token_count": 0,
            },
            "ibp_event_ledger": list(state["events"]),
            "token_conservation": {
                "input_residual_token_count": len(residual),
                "emitted_boundary_token_count": len(state["events"]),
                "counts_equal": len(residual) == len(state["events"]),
            },
            "I3_comparison_interface": {
                "candidate_port_order": ["A.q1", "A.q2", "I.q1"],
                "candidate_ordered_word_signature": [
                    list(word) for word in ordered_words
                ],
                "candidate_sorted_port_degrees": list(sorted_degrees),
                "degree_prefilter_target_term_ids": degree_candidates,
                "raw_ordered_word_match_term_ids": ordered_matches,
                "raw_permutation_word_match_term_ids": permutation_matches,
                "comparison_status": (
                    "OPEN_MISSING_ENDPOINT_COLOR_PORT_BINDING_AND_POST_IBP_NORMAL_FORM"
                ),
                "comparison_matrix_row": None,
            },
            "post_IBP_reductions_performed": [],
            "anomaly_coefficient_contribution": None,
        }
        branch_id = f"IBP::{digest(branch_core)[:28]}"
        branches.append(_record_with_hash({"branch_id": branch_id, **branch_core}))
    if len(branches) != 2 ** len(residual):
        raise AssertionError("graded two-factor coproduct is incomplete")
    return branches


def _legal_boundary_rules() -> list[dict[str, Any]]:
    return [
        {
            "rule_id": "R-SUPERSPACE-IBP-5.53",
            "formula": "int (D F) G = -(-1)^(|D||F|) int F (D G)",
            "conditions": ["|D|=1", "integrated_coordinate=theta_A"],
            "execution": "BRANCHWISE_EXECUTED",
        },
        {
            "rule_id": "R-GRADED-LEIBNIZ-TWO-A-LOCAL-FACTORS",
            "formula": "D(F1 F2)=(D F1)F2+(-1)^|F1| F1(D F2)",
            "conditions": ["ordered_factors=(A.q1,A.q2)", "|D|=1"],
            "execution": "BRANCHWISE_EXECUTED",
        },
        {
            "rule_id": "R-IBP-THETA-I-BARRIER",
            "formula": "partial_theta_A F(theta_I)=0 before endpoint identification",
            "conditions": ["theta_I is unintegrated", "slot=I.q1"],
            "execution": "BRANCHWISE_ENFORCED",
        },
        {
            "rule_id": "R-EXTERNAL-TOKEN-NEVER-DROP-5.53",
            "formula": "external hit -> TYPE::ExternalLegDerivativeToken",
            "conditions": ["later endpoint binding classifies port as external"],
            "execution": "DEFERRED_ENDPOINT_BINDING_REQUIRED",
        },
        {
            "rule_id": "R-INTERNAL-ENDPOINT-TRANSFER-5.53c",
            "formula": "D_i(r) Delta_ij(r)=-D_j(-r) Delta_ij(r)",
            "conditions": ["later endpoint binding classifies port as internal"],
            "execution": "DEFERRED_EXPLICIT_MOMENTUM_BINDING_REQUIRED",
        },
    ]


def build_payload() -> dict[str, Any]:
    input_hashes = _input_hashes()
    if input_hashes != EXPECTED_INPUT_FILE_SHA256:
        raise AssertionError("the committed bcdfe0c input closure changed")
    replay_audit = _load_json(REPLAY_AUDIT)
    if not replay_audit["all_checks_passed"]:
        raise AssertionError("the source replay audit is not PASS")
    replay = preaggregation._replay()
    replay_aggregate_rows_sha256 = digest(replay["aggregate_rows"])
    replay_contact_catalog_sha256 = replay["shared_primitive_oracle_regression"][
        "contact_catalog_sha256"
    ]
    if replay_aggregate_rows_sha256 != EXPECTED_REPLAY_AGGREGATE_ROWS_SHA256:
        raise AssertionError("the reconstructed replay aggregate object changed")
    if replay_contact_catalog_sha256 != EXPECTED_REPLAY_CONTACT_CATALOG_SHA256:
        raise AssertionError("the reconstructed replay contact catalog changed")
    contacts = [
        row
        for row in replay["aggregate_rows"]
        if row["classification"] == "EDGE_SQUARE_CONTACT"
    ]
    if len(contacts) != 608:
        raise AssertionError("the source replay does not contain 608 contacts")
    i3_targets = _load_i3_target_basis()
    carriers = []
    for contact in contacts:
        local_slots, protected_slot = _local_slots(contact)
        branches = _ibp_branches(contact, local_slots, protected_slot, i3_targets)
        parent_incidence = [
            {
                "parent_pair_id": str(row["parent_pair_id"]),
                "polynomial_sha256": str(row["polynomial_sha256"]),
            }
            for row in contact["parent_incidence"]
        ]
        carrier_core = {
            "type_id": "TYPE::EdgeTaggedContactIBPCarrierRow",
            "source_contact_group_id": str(contact["aggregate_group_id"]),
            "source_contact_polynomial_sha256": str(contact["polynomial_sha256"]),
            "edge_square_quotient": deepcopy(contact["edge_square_quotient"]),
            "collapsed_edge_id": "e_AI",
            "delta_scope_id": "DELTA::e_AI::A_TO_I",
            "integrated_coordinate": "theta_A",
            "unintegrated_coordinate": "theta_I",
            "residual_e_AI_word_outer_to_inner": [
                _primitive(token) for token in contact["remaining_e_AI_tokens"]
            ],
            "A_local_slots": local_slots,
            "protected_I_local_slot": protected_slot,
            "parent_incidence": parent_incidence,
            "parent_incidence_count": len(parent_incidence),
            "primitive_contribution_count": int(
                contact["primitive_contribution_count"]
            ),
            "coproduct_branch_count": len(branches),
            "coproduct_branches": branches,
        }
        carriers.append(_record_with_hash(carrier_core))

    token_word_census = Counter(
        tuple(row["residual_e_AI_word_outer_to_inner"]) for row in carriers
    )
    local_order_census = Counter(
        tuple(slot["edge_id"] for slot in row["A_local_slots"]) for row in carriers
    )
    branches = [branch for row in carriers for branch in row["coproduct_branches"]]
    events = [event for branch in branches for event in branch["ibp_event_ledger"]]
    degree_prefilter = Counter(
        "HAS_RAW_PORT_DEGREE_CANDIDATE"
        if branch["I3_comparison_interface"]["degree_prefilter_target_term_ids"]
        else "NO_RAW_PORT_DEGREE_CANDIDATE"
        for branch in branches
    )
    raw_ordered_matches = sum(
        bool(branch["I3_comparison_interface"]["raw_ordered_word_match_term_ids"])
        for branch in branches
    )
    raw_permutation_matches = sum(
        bool(branch["I3_comparison_interface"]["raw_permutation_word_match_term_ids"])
        for branch in branches
    )
    counts = {
        "source_contact_aggregates": len(carriers),
        "one_token_contacts": sum(
            len(word) == 1 for word in token_word_census.elements()
        ),
        "two_token_contacts": sum(
            len(word) == 2 for word in token_word_census.elements()
        ),
        "three_token_contacts": sum(
            len(word) == 3 for word in token_word_census.elements()
        ),
        "A_local_slots": 2 * len(carriers),
        "protected_I_local_slots": len(carriers),
        "coproduct_branches": len(branches),
        "ibp_events": len(events),
        "retained_edge_tagged_boundary_tokens": len(events),
        "I3_target_terms": len(i3_targets),
        "I3_comparison_interface_rows": len(branches),
        "raw_ordered_I3_word_matches": raw_ordered_matches,
        "raw_permutation_I3_word_matches": raw_permutation_matches,
        "raw_port_degree_prefilter_rows": degree_prefilter[
            "HAS_RAW_PORT_DEGREE_CANDIDATE"
        ],
        "raw_port_degree_no_candidate_rows": degree_prefilter[
            "NO_RAW_PORT_DEGREE_CANDIDATE"
        ],
    }
    core = {
        "schema": SCHEMA,
        "status": STATUS,
        "source_commit": SOURCE_COMMIT,
        "resolved_type_id": RESOLVED_TYPE_ID,
        "original_missing_type_id": ORIGINAL_MISSING_TYPE_ID,
        "original_missing_type_status": "PARTIALLY_RESOLVED_EVENT_CARRIER_ONLY",
        "open_missing_type_ids": list(OPEN_TYPE_IDS),
        "semantic_scope": "RESIDUAL_E_AI_IBP_EVENT_CARRIER_ONLY",
        "input_provenance": {
            "source_replay_payload_sha256": EXPECTED_REPLAY_PAYLOAD_SHA256,
            "source_contact_catalog_sha256": replay_contact_catalog_sha256,
            "source_aggregate_rows_sha256": replay_aggregate_rows_sha256,
            "runtime_reconstruction_object_hash_matches_bcdfe0c": True,
            "runtime_reconstruction_role": (
                "MECHANISM_ONLY_EXACT_OBJECT_HASH_GATED_NOT_SEPARATE_AUTHORITY"
            ),
            "file_sha256": input_hashes,
            "external_result_used_as_input": False,
        },
        "legal_boundary_rules": _legal_boundary_rules(),
        "local_slot_definition": {
            "A.q1": "first theta_A survivor in replay survivor_signature order",
            "A.q2": "second theta_A survivor in replay survivor_signature order",
            "I.q1": "theta_I survivor e_IB; excluded from theta_A IBP",
            "namespace": "COLLAPSED_CONTACT_LOCAL_ORDER",
            "not_parent_GraphIR_topology_port_namespace": True,
        },
        "counts": counts,
        "token_word_census": {
            "|".join(key): value for key, value in sorted(token_word_census.items())
        },
        "A_local_edge_order_census": {
            "|".join(key): value for key, value in sorted(local_order_census.items())
        },
        "I3_target_basis": i3_targets,
        "carriers": carriers,
        "comparison_frontier": {
            "status": "OPEN_FAIL_CLOSED",
            "raw_word_equality_is_not_a_post_IBP_normal_form_proof": True,
            "raw_ordered_word_match_count": raw_ordered_matches,
            "raw_permutation_word_match_count": raw_permutation_matches,
            "missing_rule_data": [
                {
                    "missing_type_id": OPEN_TYPE_IDS[0],
                    "required_record": (
                        "for each collapsed contact: edge -> endpoint class, momentum, "
                        "color slot, and ordered I3 grammar-port bijection"
                    ),
                },
                {
                    "missing_type_id": OPEN_TYPE_IDS[1],
                    "required_record": (
                        "edge-tagged primitive normal ordering, mixed anticommutator, "
                        "chirality, and nilpotence ledger after the IBP carrier"
                    ),
                },
                {
                    "missing_type_id": OPEN_TYPE_IDS[2],
                    "required_record": (
                        "object-level exact Q(i) matrix from normalized local branches "
                        "to the ten I3 target terms, including color and port order"
                    ),
                },
            ],
            "comparison_matrix": None,
            "object_level_I3_equality": None,
        },
        "anomaly_coefficient": None,
    }
    payload = dict(core)
    payload["payload_sha256"] = digest(payload)
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    counts = payload["counts"]
    carriers = payload["carriers"]
    branches = [branch for row in carriers for branch in row["coproduct_branches"]]
    events = [event for branch in branches for event in branch["ibp_event_ledger"]]
    return {
        "input_hash_closure_exact": payload["input_provenance"]["file_sha256"]
        == EXPECTED_INPUT_FILE_SHA256,
        "source_replay_payload_exact": payload["input_provenance"][
            "source_replay_payload_sha256"
        ]
        == EXPECTED_REPLAY_PAYLOAD_SHA256
        and payload["input_provenance"]["source_aggregate_rows_sha256"]
        == EXPECTED_REPLAY_AGGREGATE_ROWS_SHA256
        and payload["input_provenance"]["source_contact_catalog_sha256"]
        == EXPECTED_REPLAY_CONTACT_CATALOG_SHA256
        and payload["input_provenance"][
            "runtime_reconstruction_object_hash_matches_bcdfe0c"
        ],
        "contact_and_token_census_exact": counts["source_contact_aggregates"] == 608
        and counts["one_token_contacts"] == 192
        and counts["two_token_contacts"] == 320
        and counts["three_token_contacts"] == 96,
        "local_partition_exact": counts["A_local_slots"] == 1216
        and counts["protected_I_local_slots"] == 608
        and all(
            {slot["edge_id"] for slot in row["A_local_slots"]} == {"e_BA", "e_CA"}
            and row["protected_I_local_slot"]["edge_id"] == "e_IB"
            for row in carriers
        ),
        "token_word_census_exact": {
            tuple(key.split("|")): value
            for key, value in payload["token_word_census"].items()
        }
        == EXPECTED_TOKEN_WORD_CENSUS,
        "graded_coproduct_cardinality_exact": counts["coproduct_branches"] == 2432
        and counts["ibp_events"] == 5248,
        "all_event_and_branch_hashes_valid": all(
            _record_hash_valid(event) for event in events
        )
        and all(_record_hash_valid(branch) for branch in branches)
        and all(_record_hash_valid(row) for row in carriers),
        "branch_signs_and_token_conservation_exact": all(
            branch["ibp_branch_sign"] in (-1, 1)
            and branch["token_conservation"]["counts_equal"]
            and len(branch["ibp_event_ledger"])
            == len(branch["assignment_outer_to_inner_transfer_order"])
            for branch in branches
        ),
        "theta_I_barrier_and_boundary_retention_exact": all(
            branch["protected_I_local_survivor"]["received_theta_A_IBP_token_count"]
            == 0
            and all(
                event["boundary_token"]["disposition"]
                == "RETAIN_UNTIL_ENDPOINT_BINDING"
                for event in branch["ibp_event_ledger"]
            )
            for branch in branches
        )
        and counts["retained_edge_tagged_boundary_tokens"] == 5248,
        "I3_target_interface_exact": counts["I3_target_terms"] == 10
        and counts["I3_comparison_interface_rows"] == 2432
        and counts["raw_port_degree_prefilter_rows"] == 1600
        and counts["raw_port_degree_no_candidate_rows"] == 832,
        "raw_word_match_is_honestly_nonaccepting": counts["raw_ordered_I3_word_matches"]
        == 0
        and counts["raw_permutation_I3_word_matches"] == 0
        and payload["comparison_frontier"][
            "raw_word_equality_is_not_a_post_IBP_normal_form_proof"
        ],
        "comparison_fail_closed": payload["comparison_frontier"]["comparison_matrix"]
        is None
        and payload["comparison_frontier"]["object_level_I3_equality"] is None
        and payload["open_missing_type_ids"] == list(OPEN_TYPE_IDS),
        "no_coefficient_claim": payload["anomaly_coefficient"] is None
        and all(
            branch["anomaly_coefficient_contribution"] is None for branch in branches
        ),
        "no_external_result": payload["input_provenance"][
            "external_result_used_as_input"
        ]
        is False,
        "payload_hash_valid": payload["payload_sha256"]
        == digest(
            {key: value for key, value in payload.items() if key != "payload_sha256"}
        ),
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    uncompressed = _payload_json_bytes(payload)
    compressed = _payload_gzip_bytes(payload)
    return {
        "schema": "step6.contact_ibp_survivor_carrier.audit.v1",
        "status": payload["status"],
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "counts": payload["counts"],
        "token_word_census": payload["token_word_census"],
        "A_local_edge_order_census": payload["A_local_edge_order_census"],
        "resolved_type_id": payload["resolved_type_id"],
        "original_missing_type_status": payload["original_missing_type_status"],
        "open_missing_type_ids": payload["open_missing_type_ids"],
        "comparison_frontier": payload["comparison_frontier"],
        "carrier_rows_sha256": digest(payload["carriers"]),
        "I3_target_basis_sha256": digest(payload["I3_target_basis"]),
        "input_provenance": payload["input_provenance"],
        "payload_sha256": payload["payload_sha256"],
        "artifact_storage": {
            "encoding": "JSON_UTF8_GZIP",
            "compression_level": 9,
            "gzip_mtime": 0,
            "uncompressed_size_bytes": len(uncompressed),
            "uncompressed_file_sha256": hashlib.sha256(uncompressed).hexdigest(),
            "compressed_size_bytes": len(compressed),
            "compressed_file_sha256": hashlib.sha256(compressed).hexdigest(),
            "round_trip_payload_sha256": json.loads(gzip.decompress(compressed))[
                "payload_sha256"
            ],
            "round_trip_payload_hash_valid": json.loads(gzip.decompress(compressed))[
                "payload_sha256"
            ]
            == payload["payload_sha256"],
        },
        "script_sha256": file_sha256(Path(__file__)),
        "test_sha256": file_sha256(TEST_PATH),
        "anomaly_coefficient": None,
    }


def write_outputs(payload: Mapping[str, Any]) -> None:
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(_payload_gzip_bytes(payload))
    AUDIT.write_text(
        json.dumps(build_audit(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    payload = build_payload()
    checks = exact_checks(payload)
    if not all(checks.values()):
        failed = [key for key, value in checks.items() if not value]
        raise AssertionError(f"contact IBP carrier checks failed: {failed}")
    write_outputs(payload)
    print(json.dumps(build_audit(payload), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
