#!/usr/bin/env python3
"""Replay measure distribution and delta D-algebra before contact aggregation.

The replay starts from the frozen six first-cut rows, their 216 raw expression
histories, and the 768 unaggregated action--insertion history pairs.  Every
measure hit, graded Leibniz sign, delta-endpoint transfer, primitive swap, and
mixed anticommutator is retained before the exact EdgeSquare/remainder split.

The executor uses the same primitive D-algebra oracle as the earlier grouped
classifier.  Its output is therefore a provenance-preserving reconstruction,
not an independent calculation.  No legacy aggregate row is used to assign a
raw parent.  Object-level remainder equality is left open.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_two_loop_dword as dword
    from scripts import step6_global_dword_adapter as dword_adapter
except ModuleNotFoundError:  # direct execution
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_two_loop_dword as dword
    from scripts import step6_global_dword_adapter as dword_adapter


ROOT = Path(__file__).resolve().parents[1]
GENERATED = (
    ROOT / "generated/step6/preaggregation-measure-delta-replay/"
    "preaggregation-measure-delta-replay-summary.json"
)
AUDIT = ROOT / "audits/step6-preaggregation-measure-delta-replay-verification.json"
TEST_PATH = ROOT / "tests/test_step6_preaggregation_measure_delta_replay.py"
SEED_FIXTURE = (
    ROOT / "generated/step6/measure-tagged-delta-convolution/"
    "measure-tagged-delta-convolution.json"
)

SCHEMA = "step6.preaggregation_measure_delta_replay.v2"
STATUS = (
    "PASS_TYPED_REPLAY_UNDER_SHARED_PRIMITIVE_DALGEBRA_ORACLE__"
    "REMAINDER_OBJECT_EQUALITY_OPEN"
)
RESOLVED_TYPE_ID = (
    "TYPE::MeasureTaggedDeltaConvolutionReplayUnderSharedPrimitiveDAlgebraOracle"
)
REMAINDER_COMPARATOR_MISSING_TYPE_ID = (
    "MISSING_TYPE::IndependentRemainderObjectComparator"
)
RESIDUAL_IBP_MISSING_TYPE_ID = "MISSING_TYPE::EdgeTaggedContactIBPToALocalSurvivors"
SEMANTIC_SCOPE = "PREAGGREGATION_MEASURE_DELTA_REPLAY_ONLY"
EXPECTED_SEED_FILE_SHA256 = (
    "b5ecf1ac6a471f7a6d75158d502ec6a869fe5d0bce6599343f285b7cf404a940"
)
EXPECTED_SEED_PAYLOAD_SHA256 = (
    "f10375c672a750baeeb81151ee4379a9052ff43d45bc8c9b1911e69849b65450"
)
SHARED_ORACLE_CONTACT_HASH = (
    "1918745eafd2970e942209ff312efb2bd342b745d2cf1ace3d9fe3d06fa2de0a"
)
SHARED_ORACLE_REMAINDER_HASH = (
    "6dc51612772cdd485b0ba0b85a22fa79b4b930d37f6cfe54c821f90521579351"
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qi_json(value: Any) -> dict[str, str]:
    return {"field": "Q(i)", "re": str(value.re), "im": str(value.im)}


def oracle_qi_from_json(value: Mapping[str, Any]) -> Any:
    return coefficient.oracle.Gaussian(
        Fraction(str(value["re"])), Fraction(str(value["im"]))
    )


def dword_qi_json(value: Any) -> dict[str, str]:
    return {"domain": dword.QI_DOMAIN, "re": str(value.re), "im": str(value.im)}


def constant_gaussian_from_poly_json(value: Sequence[Mapping[str, Any]]) -> Any:
    if len(value) != 1 or value[0].get("monomial") != []:
        raise ValueError("raw history coefficient is not a Q(i) constant")
    return oracle_qi_from_json(value[0]["coefficient"])


def to_dword_gaussian(value: Any) -> Any:
    return dword.GaussianRational(value.re, value.im)


def coefficient_reordering_sign(
    order: Sequence[str], target: Sequence[str], parities: Mapping[str, int]
) -> int:
    if len(order) != len(target) or set(order) != set(target):
        raise ValueError("coefficient permutations require identical distinct labels")
    rank = {label: position for position, label in enumerate(target)}
    exponent = 0
    for left in range(len(order)):
        for right in range(left + 1, len(order)):
            if rank[order[left]] > rank[order[right]]:
                exponent ^= parities[order[left]] * parities[order[right]]
    return -1 if exponent else 1


def _validated_measure_scope_map(source: Mapping[str, Any]) -> dict[str, Any]:
    expected = {
        "type_id": "TYPE::MeasureScope",
        "scope_id": "MEASURE::S3_MINUS_1_2::DEFERRED",
        "measure_kind": "E_MINUS_ANTICHIRAL",
        "word_outer_to_inner": ["barD2"],
        "normalization": {"field": "Q(i)", "re": "-1/4", "im": "0"},
        "execution_state": "DEFERRED_AT_RAW_EXPRESSION_TRACE",
        "distribution_performed": False,
    }
    if dict(source) != expected:
        raise AssertionError("deferred MeasureScope record changed")
    expansions = [
        {
            "expansion_index": index,
            "coefficient": qi_json(expansion_coefficient),
            "primitive_word_outer_to_inner": list(primitive_word),
        }
        for index, (expansion_coefficient, primitive_word) in enumerate(
            coefficient._explicit_word_expansion(tuple(source["word_outer_to_inner"]))
        )
    ]
    expected_expansions = [
        {
            "expansion_index": 0,
            "coefficient": {"field": "Q(i)", "re": "1", "im": "0"},
            "primitive_word_outer_to_inner": ["barD_dotplus", "barD_dotminus"],
        },
        {
            "expansion_index": 1,
            "coefficient": {"field": "Q(i)", "re": "-1", "im": "0"},
            "primitive_word_outer_to_inner": ["barD_dotminus", "barD_dotplus"],
        },
    ]
    if expansions != expected_expansions:
        raise AssertionError("E_MINUS_ANTICHIRAL measure expansion changed")
    core = {
        "type_id": "TYPE::DeferredToExecutedMeasureScopeMap",
        "source_scope_id": str(source["scope_id"]),
        "source_scope_record_sha256": digest(source),
        "source_measure_kind": str(source["measure_kind"]),
        "source_word_outer_to_inner": list(source["word_outer_to_inner"]),
        "source_normalization": dict(source["normalization"]),
        "target_scope_id": "MEASURE::S3_MINUS_1_2::EXECUTED",
        "target_execution_state": "EXECUTED_BEFORE_CONTACT_AGGREGATION",
        "word_expansions": expansions,
        "normalization_application_count": 1,
    }
    record = {"measure_scope_map_id": f"MEASURE_MAP::{digest(core)[:24]}", **core}
    record["record_sha256"] = digest(record)
    return record


def _execute_measure_scope(
    parent_history: Mapping[str, Any],
    scope_map: Mapping[str, Any],
) -> list[dict[str, Any]]:
    if parent_history.get("side") != "action":
        raise ValueError("only an action raw history carries the deferred measure")
    raw_factors = parent_history["factors_in_raw_AST_order"]
    raw_scalar = constant_gaussian_from_poly_json(parent_history["coefficient"])
    output = []
    for expansion in scope_map["word_expansions"]:
        expansion_scalar = oracle_qi_from_json(expansion["coefficient"])
        states = [
            {
                "relative_scalar": expansion_scalar,
                "factors": deepcopy(raw_factors),
                "hits": [],
            }
        ]
        primitive_word = expansion["primitive_word_outer_to_inner"]
        for application_index, primitive in enumerate(reversed(primitive_word)):
            emitted = []
            for state in states:
                prefix_parity = 0
                prefix_factor_parities = []
                for position, factor in enumerate(state["factors"]):
                    coefficient_parity = int(factor["coefficient_parity"])
                    sign_exponent = prefix_parity ^ coefficient_parity
                    sign = -1 if sign_exponent else 1
                    factors = deepcopy(state["factors"])
                    before_parity = int(factor["derived_factor_parity"])
                    factors[position]["derived_factor_parity"] = before_parity ^ 1
                    factors[position]["derivative_word_outer_to_inner"] = [
                        primitive,
                        *factor["derivative_word_outer_to_inner"],
                    ]
                    hit = {
                        "sequence_index": len(state["hits"]),
                        "scope_map_id": scope_map["measure_scope_map_id"],
                        "source_scope_id": scope_map["source_scope_id"],
                        "executed_scope_id": scope_map["target_scope_id"],
                        "scope_expansion_index": int(expansion["expansion_index"]),
                        "scope_primitive_word_outer_to_inner": list(primitive_word),
                        "primitive_application_index_inner_to_outer": application_index,
                        "primitive": primitive,
                        "hit_factor_position": position,
                        "grammar_port_id": str(factor["grammar_port_id"]),
                        "topology_port_id": str(factor["topology_port_id"]),
                        "endpoint_class": str(factor["role"]),
                        "edge_id": factor["edge_id"],
                        "orientation_endpoint": str(factor["orientation_endpoint"]),
                        "prefix_factor_parities": list(prefix_factor_parities),
                        "prefix_parity": prefix_parity,
                        "hit_leaf_coefficient_parity": coefficient_parity,
                        "sign_exponent_mod_2": sign_exponent,
                        "koszul_sign": sign,
                        "derived_factor_parity_before": before_parity,
                        "derived_factor_parity_after": before_parity ^ 1,
                    }
                    emitted.append(
                        {
                            "relative_scalar": state["relative_scalar"] * sign,
                            "factors": factors,
                            "hits": [*state["hits"], hit],
                        }
                    )
                    prefix_factor_parities.append(before_parity)
                    prefix_parity ^= before_parity
            states = emitted

        normalization = oracle_qi_from_json(scope_map["source_normalization"])
        for state in states:
            relative_scalar = state["relative_scalar"] * normalization
            core = {
                "type_id": "TYPE::MeasureDistributedRawActionHistory",
                "parent_action_raw_trace_history_id": str(parent_history["history_id"]),
                "measure_child_ordinal": len(output),
                "measure_scope_map_id": scope_map["measure_scope_map_id"],
                "source_deferred_measure_scope_id": scope_map["source_scope_id"],
                "executed_measure_scope_id": scope_map["target_scope_id"],
                "measure_normalization": dict(scope_map["source_normalization"]),
                "normalization_application_count": 1,
                "measure_relative_scalar": qi_json(relative_scalar),
                "coefficient_after_measure": qi_json(raw_scalar * relative_scalar),
                "factors_in_original_AST_order_after_measure": state["factors"],
                "measure_primitive_hits": state["hits"],
                "measure_structural_choice": dict(expansion),
                "raw_primitive_hits_preserved_by_parent_reference": len(
                    parent_history["primitive_hits"]
                ),
                "raw_structural_choices_preserved_by_parent_reference": len(
                    parent_history["structural_choices"]
                ),
            }
            branch_id = (
                f"MEASURE_CHILD::{parent_history['history_id']}::{len(output)}::"
                f"{digest(core)[:20]}"
            )
            record = {"measure_branch_id": branch_id, **core}
            record["record_sha256"] = digest(record)
            output.append(record)
    return output


def _validated_delta_scope(source: Mapping[str, Any]) -> dict[str, Any]:
    expected = {
        "type_id": "TYPE::DeltaScope",
        "scope_id": "DELTA::e_AI::A_TO_I",
        "edge_id": "e_AI",
        "integrated_coordinate": "theta_A",
        "unintegrated_coordinate": "theta_I",
        "coefficient_kernel": "LEFT_ORDERED_H_INVERSE",
        "normalized_delta": "-4*product_gamma(theta_A^gamma-theta_I^gamma)",
        "generator_order": list(coefficient.oracle.GENERATOR_ORDER),
        "execution_state": "ATTACHED_BEFORE_CONTACT_AGGREGATION",
    }
    if dict(source) != expected:
        raise AssertionError("DeltaScope record changed")
    core = {
        "type_id": "TYPE::ValidatedDeltaScopeBinding",
        "scope_id": str(source["scope_id"]),
        "delta_scope_record_sha256": digest(source),
        "edge_id": str(source["edge_id"]),
        "source_endpoint_id": "delta.theta_A.source",
        "target_endpoint_id": "delta.theta_I.target",
        "integrated_coordinate": str(source["integrated_coordinate"]),
        "unintegrated_coordinate": str(source["unintegrated_coordinate"]),
        "coefficient_kernel": str(source["coefficient_kernel"]),
    }
    record = {"delta_binding_id": f"DELTA_BINDING::{digest(core)[:24]}", **core}
    record["record_sha256"] = digest(record)
    return record


def _edge_endpoints(
    delta_binding: Mapping[str, Any],
) -> dict[str, dword.ExecutorEndpoint]:
    source_id = str(delta_binding["source_endpoint_id"])
    target_id = str(delta_binding["target_endpoint_id"])
    edge_id = str(delta_binding["edge_id"])
    source = dword.ExecutorEndpoint(
        source_id,
        "INTERNAL_SOURCE",
        0,
        "NONE",
        "ORDINARY",
        tuple(coefficient.MOMENTUM_BASIS),
        (1, 0, 0, 0, 0),
        edge_id,
        target_id,
    )
    target = dword.ExecutorEndpoint(
        target_id,
        "INTERNAL_TARGET",
        0,
        "NONE",
        "ORDINARY",
        tuple(coefficient.MOMENTUM_BASIS),
        (-1, 0, 0, 0, 0),
        edge_id,
        source_id,
    )
    return {source.endpoint_id: source, target.endpoint_id: target}


def _edge_word_replay(
    action_word: Sequence[str],
    insertion_word: Sequence[str],
    branch_id: str,
    delta_scope_id: str,
    delta_binding: Mapping[str, Any],
    action_factor: Mapping[str, Any],
    insertion_factor: Mapping[str, Any],
) -> tuple[list[dword.ExecutorTerm], list[dict[str, object]], dict[str, Any]]:
    if delta_scope_id != delta_binding["scope_id"]:
        raise AssertionError("parent pair DeltaScope id does not resolve")
    expected_endpoints = (
        (action_factor, "e_AI_source", "source", "k"),
        (insertion_factor, "e_AI_target", "target", "-k"),
    )
    endpoint_validation_evidence = []
    for factor, topology, orientation, momentum in expected_endpoints:
        valid = (
            factor["topology_port_id"] == topology
            and factor["edge_id"] == delta_binding["edge_id"]
            and factor["orientation_endpoint"] == orientation
            and factor["momentum_label"] == momentum
        )
        endpoint_validation_evidence.append(
            {
                "grammar_port_id": str(factor["grammar_port_id"]),
                "topology_port_id": str(factor["topology_port_id"]),
                "edge_id": str(factor["edge_id"]),
                "orientation_endpoint": str(factor["orientation_endpoint"]),
                "momentum_label": str(factor["momentum_label"]),
                "validated": valid,
            }
        )
        if not valid:
            raise AssertionError("contracted factor disagrees with DeltaScope")
    endpoints = _edge_endpoints(delta_binding)
    source_id = str(delta_binding["source_endpoint_id"])
    target_id = str(delta_binding["target_endpoint_id"])
    tokens: list[dword.ExecutorToken] = []
    for side, word, endpoint in (
        ("A", action_word, source_id),
        ("I", insertion_word, target_id),
    ):
        for position, primitive in enumerate(word):
            kind, component = dword_adapter.PRIMITIVE_TOKEN[str(primitive)]
            tokens.append(
                dword.ExecutorToken(
                    f"{branch_id}:{side}:{position}",
                    kind,
                    component,
                    endpoint,
                    "PROPAGATOR_DELTA",
                )
            )
    initial = dword.ExecutorTerm(
        branch_id,
        dword.ExactPolynomial.constant(dword.ONE),
        tuple(tokens),
        (str(delta_binding["edge_id"]),),
    )
    transferred = dword._canonicalize_delta_endpoints(initial, endpoints)
    normal, zeros = dword._normal_order_terms([transferred], endpoints)
    consumption = {
        "type_id": "TYPE::DeltaScopeConsumption",
        "delta_binding_id": delta_binding["delta_binding_id"],
        "delta_scope_id": delta_binding["scope_id"],
        "delta_scope_record_sha256": delta_binding["delta_scope_record_sha256"],
        "parent_scope_id_resolved": delta_scope_id == delta_binding["scope_id"],
        "contracted_endpoint_validation_evidence": endpoint_validation_evidence,
        "contracted_endpoint_records_validated": all(
            row["validated"] for row in endpoint_validation_evidence
        ),
        "execution_phase": "BEFORE_CONTACT_AGGREGATION",
    }
    consumption["record_sha256"] = digest(consumption)
    return normal, zeros, consumption


def _history_lookup(
    replay: Mapping[str, Any],
) -> dict[tuple[str, str, int], Mapping[str, Any]]:
    result = {}
    for record in replay["raw_histories"]:
        key = (str(record["row_id"]), str(record["side"]), int(record["raw_ordinal"]))
        if key in result:
            raise AssertionError("raw-history ordinal key collision")
        result[key] = record
    return result


def _pair_lookup(replay: Mapping[str, Any]) -> dict[tuple[str, str], Mapping[str, Any]]:
    result = {}
    for record in replay["unaggregated_contact_provenance"]:
        key = (
            str(record["action_raw_trace_history_id"]),
            str(record["insertion_raw_trace_history_id"]),
        )
        if key in result:
            raise AssertionError("raw-history pair key collision")
        result[key] = record
    return result


def _compact_parent_pair(record: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "provenance_id",
        "row_id",
        "action_raw_trace_history_id",
        "insertion_raw_trace_history_id",
        "measure_scope_id",
        "delta_scope_id",
        "contracted_action_port",
        "contracted_insertion_port",
        "contracted_action_word_outer_to_inner",
        "contracted_insertion_word_outer_to_inner",
        "factor_order_ledger",
        "preaggregation_Koszul_ledger",
        "exact_factor_ledger",
        "preaggregation_exact_coefficient_before_measure",
        "record_sha256",
    )
    return {key: record[key] for key in keys}


def _survivor_signature(
    factors: Sequence[Mapping[str, Any]],
    contracted_ports: set[str],
) -> tuple[tuple[str, tuple[str, ...]], ...]:
    return tuple(
        (
            str(factor["topology_port_id"]),
            tuple(str(token) for token in factor["derivative_word_outer_to_inner"]),
        )
        for factor in factors
        if str(factor["grammar_port_id"]) not in contracted_ports
    )


def _survivor_json(
    signature: Sequence[tuple[str, Sequence[str]]],
) -> list[dict[str, Any]]:
    return [
        {"edge_id": edge, "word_outer_to_inner": list(word)} for edge, word in signature
    ]


def _edge_tokens_json(
    tokens: Sequence[dword.ExecutorToken],
) -> list[dict[str, str]]:
    return [
        {
            "derivative_kind": token.derivative_kind,
            "spinor_component": token.spinor_component,
        }
        for token in tokens
    ]


def _event_count(ledger: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    return dict(sorted(Counter(str(event["kind"]) for event in ledger).items()))


def _parent_incidence_json(
    incidence: Mapping[str, dword.ExactPolynomial],
) -> list[dict[str, Any]]:
    rows = []
    for pair_id, polynomial in sorted(incidence.items()):
        if not polynomial:
            continue
        encoded = polynomial.to_json()
        rows.append(
            {
                "parent_pair_id": pair_id,
                "exact_polynomial": encoded,
                "polynomial_sha256": digest(encoded),
            }
        )
    return rows


def _exact_polynomial_from_json(
    rows: Sequence[Mapping[str, Any]],
) -> dword.ExactPolynomial:
    terms: dict[dword.Monomial, dword.GaussianRational] = {}
    for row in rows:
        monomial = tuple(
            (str(factor["symbol"]), int(factor["exponent"]))
            for factor in row["monomial"]
        )
        terms[monomial] = dword.GaussianRational.from_json(row["factor"])
    return dword.ExactPolynomial.from_terms(terms)


def _record_hash_valid(record: Mapping[str, Any]) -> bool:
    return bool(record.get("record_sha256")) and record["record_sha256"] == digest(
        {key: value for key, value in record.items() if key != "record_sha256"}
    )


def _load_seed_fixture() -> dict[str, Any]:
    if file_sha256(SEED_FIXTURE) != EXPECTED_SEED_FILE_SHA256:
        raise AssertionError("frozen preaggregation seed file hash changed")
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    if payload.get("schema") != "step6.preaggregation_raw_replay_seed.v2":
        raise AssertionError("frozen preaggregation seed schema changed")
    if (
        payload.get("status")
        != "PASS_PREAGGREGATION_REPLAY_SEED__MEASURE_TAGGED_CONVOLUTION_OPEN"
    ):
        raise AssertionError("frozen preaggregation seed status changed")
    if payload.get("external_result_used_as_input") is not False:
        raise AssertionError("seed unexpectedly imports an external result")
    payload_hash = payload.get("payload_sha256")
    if payload_hash != EXPECTED_SEED_PAYLOAD_SHA256:
        raise AssertionError("frozen preaggregation seed payload hash changed")
    if payload_hash != digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    ):
        raise AssertionError("frozen preaggregation seed self-hash fails")
    replay = payload["measure_tagged_raw_replay"]
    if digest(replay["raw_histories"]) != replay["raw_histories_sha256"]:
        raise AssertionError("frozen raw-history table hash fails")
    if (
        digest(replay["unaggregated_contact_provenance"])
        != replay["unaggregated_pairs_sha256"]
    ):
        raise AssertionError("frozen unaggregated-pair table hash fails")
    if not all(_record_hash_valid(row) for row in replay["raw_histories"]):
        raise AssertionError("a frozen raw-history record hash fails")
    if not all(
        _record_hash_valid(row) for row in replay["unaggregated_contact_provenance"]
    ):
        raise AssertionError("a frozen parent-pair record hash fails")
    return payload


def _pair_preaggregation_coefficient_exact(
    parent: Mapping[str, Any],
    action_history: Mapping[str, Any],
    insertion_history: Mapping[str, Any],
) -> Any:
    ledger = parent["exact_factor_ledger"]
    scalar = constant_gaussian_from_poly_json(action_history["coefficient"])
    scalar *= constant_gaussian_from_poly_json(insertion_history["coefficient"])
    for key in ("action_Project_scalar", "insertion_Project_scalar"):
        scalar *= oracle_qi_from_json(ledger[key])
    for key in (
        "edge_join_integer",
        "ordered_euler_sector_conversion",
        "action_color_permutation_sign",
        "coefficient_reordering_sign",
        "derivative_extraction_sign",
    ):
        scalar *= int(ledger[key])
    return scalar


def _derivative_extraction_sign(
    factors: Sequence[Mapping[str, Any]], contracted_ports: set[str]
) -> int:
    edge_flags = [
        str(factor["grammar_port_id"]) in contracted_ports
        for factor in factors
        for _ in factor["derivative_word_outer_to_inner"]
    ]
    inversions = sum(
        1
        for position, is_edge in enumerate(edge_flags)
        if is_edge
        for earlier in edge_flags[:position]
        if not earlier
    )
    return -1 if inversions & 1 else 1


def _replay() -> dict[str, Any]:
    seed_payload = _load_seed_fixture()
    seed_replay = seed_payload["measure_tagged_raw_replay"]
    raw_histories = seed_replay["raw_histories"]
    parent_pairs = seed_replay["unaggregated_contact_provenance"]
    histories_by_id = {str(row["history_id"]): row for row in raw_histories}
    if len(histories_by_id) != len(raw_histories):
        raise AssertionError("raw-history ids are not unique")
    pair_ids = {str(row["provenance_id"]) for row in parent_pairs}
    if len(pair_ids) != len(parent_pairs):
        raise AssertionError("parent-pair ids are not unique")

    measure_scope = seed_replay["measure_scopes"][0]
    measure_scope_map = _validated_measure_scope_map(measure_scope)
    delta_scope = seed_payload["finite_delta_convolution"]["delta_scope"]
    delta_binding = _validated_delta_scope(delta_scope)

    action_ids = sorted(
        {str(row["action_raw_trace_history_id"]) for row in parent_pairs}
    )
    measure_by_action: dict[str, list[dict[str, Any]]] = {}
    measure_branches: list[dict[str, Any]] = []
    action_measure_child_counts: Counter[int] = Counter()
    for action_id in action_ids:
        children = _execute_measure_scope(histories_by_id[action_id], measure_scope_map)
        measure_by_action[action_id] = children
        measure_branches.extend(children)
        action_measure_child_counts[len(children)] += 1

    contributions: list[dict[str, Any]] = []
    zero_branches: list[dict[str, Any]] = []
    aggregate_polynomials: dict[tuple[Any, ...], dword.ExactPolynomial] = {}
    aggregate_incidence: dict[tuple[Any, ...], dict[str, dword.ExactPolynomial]] = (
        defaultdict(dict)
    )
    aggregate_contribution_ids: dict[tuple[Any, ...], list[str]] = defaultdict(list)
    measure_pair_history_count = 0

    for parent in parent_pairs:
        pair_id = str(parent["provenance_id"])
        action_history = histories_by_id[str(parent["action_raw_trace_history_id"])]
        insertion_history = histories_by_id[
            str(parent["insertion_raw_trace_history_id"])
        ]
        if (
            action_history["side"] != "action"
            or insertion_history["side"] != "insertion"
            or action_history["row_id"] != parent["row_id"]
            or insertion_history["row_id"] != parent["row_id"]
        ):
            raise AssertionError("parent pair does not resolve to its typed histories")
        if parent["measure_scope_id"] != measure_scope_map["source_scope_id"]:
            raise AssertionError(
                "parent pair does not resolve to deferred MeasureScope"
            )
        if parent["delta_scope_id"] != delta_binding["scope_id"]:
            raise AssertionError("parent pair does not resolve to DeltaScope")

        action_port = str(parent["contracted_action_port"])
        insertion_port = str(parent["contracted_insertion_port"])
        insertion_factor_by_port = {
            str(row["grammar_port_id"]): row
            for row in insertion_history["factors_in_raw_AST_order"]
        }
        insertion_factor = insertion_factor_by_port[insertion_port]
        contracted_ports = {action_port, insertion_port}
        canonical_ports = list(
            parent["factor_order_ledger"]["canonical_preaggregation_order"]
        )
        original_raw_order = [
            str(row["grammar_port_id"])
            for row in (
                *action_history["factors_in_raw_AST_order"],
                *insertion_history["factors_in_raw_AST_order"],
            )
        ]
        if original_raw_order != parent["factor_order_ledger"]["raw_AST_order"]:
            raise AssertionError("parent raw factor order changed")
        parent_pre = _pair_preaggregation_coefficient_exact(
            parent, action_history, insertion_history
        )
        expected_parent_pre = oracle_qi_from_json(
            parent["preaggregation_exact_coefficient_before_measure"]
        )
        if parent_pre != expected_parent_pre:
            raise AssertionError("parent exact-factor ledger does not reconstruct")

        old_reorder = int(
            parent["preaggregation_Koszul_ledger"]["coefficient_reordering_sign"]
        )
        old_extraction = int(
            parent["preaggregation_Koszul_ledger"]["derivative_extraction_sign"]
        )

        for measure_record in measure_by_action[str(action_history["history_id"])]:
            action_factors = measure_record[
                "factors_in_original_AST_order_after_measure"
            ]
            action_factor_by_port = {
                str(row["grammar_port_id"]): row for row in action_factors
            }
            action_factor = action_factor_by_port[action_port]
            factors = [*action_factors, *insertion_history["factors_in_raw_AST_order"]]
            factor_order = [str(row["grammar_port_id"]) for row in factors]
            parities = {
                str(row["grammar_port_id"]): int(row["coefficient_parity"])
                for row in factors
            }
            reorder_sign = coefficient_reordering_sign(
                factor_order, canonical_ports, parities
            )
            extraction_sign = _derivative_extraction_sign(factors, contracted_ports)
            relative = oracle_qi_from_json(measure_record["measure_relative_scalar"])
            scalar = (
                parent_pre
                * relative
                * reorder_sign
                * old_reorder
                * extraction_sign
                * old_extraction
            )
            action_word = tuple(
                str(token) for token in action_factor["derivative_word_outer_to_inner"]
            )
            insertion_word = tuple(
                str(token)
                for token in insertion_factor["derivative_word_outer_to_inner"]
            )
            if (
                list(insertion_word)
                != parent["contracted_insertion_word_outer_to_inner"]
            ):
                raise AssertionError("contracted insertion word changed")
            signature = _survivor_signature(factors, contracted_ports)
            branch_id = f"DELTA::{pair_id}::{measure_record['measure_branch_id']}"
            normal, zeros, delta_consumption = _edge_word_replay(
                action_word,
                insertion_word,
                branch_id,
                str(parent["delta_scope_id"]),
                delta_binding,
                action_factor,
                insertion_factor,
            )
            measure_pair_history_count += 1
            execution_order = [
                measure_scope_map["target_scope_id"],
                delta_binding["scope_id"],
                "PRIMITIVE_DALGEBRA_SHARED_ORACLE",
                "CONTACT_AGGREGATION_NOT_YET_EXECUTED",
            ]

            for zero_ordinal, zero in enumerate(zeros):
                zero_core = {
                    "type_id": "TYPE::PreAggregationDeltaZeroBranch",
                    "parent_pair_id": pair_id,
                    "action_raw_trace_history_id": str(action_history["history_id"]),
                    "insertion_raw_trace_history_id": str(
                        insertion_history["history_id"]
                    ),
                    "measure_branch_id": measure_record["measure_branch_id"],
                    "measure_scope_map_id": measure_scope_map["measure_scope_map_id"],
                    "source_measure_scope_id": measure_scope_map["source_scope_id"],
                    "executed_measure_scope_id": measure_scope_map["target_scope_id"],
                    "delta_scope_id": delta_binding["scope_id"],
                    "delta_scope_consumption": deepcopy(delta_consumption),
                    "scope_execution_order": execution_order,
                    "zero_ordinal": zero_ordinal,
                    "original_factor_order": factor_order,
                    "canonical_preaggregation_order": canonical_ports,
                    "contracted_action_word_outer_to_inner": list(action_word),
                    "contracted_insertion_word_outer_to_inner": list(insertion_word),
                    "classification": zero["classification"],
                    "rule": zero["rule"],
                    "token_ids": list(zero["token_ids"]),
                    "delta_and_odd_word_ledger": list(zero["ledger"]),
                    "event_counts": _event_count(zero["ledger"]),
                    "residual_IBP_events": [],
                    "residual_IBP_performed": False,
                }
                zero_record = {
                    "zero_branch_id": f"ZERO::{digest(zero_core)[:28]}",
                    **zero_core,
                }
                zero_record["record_sha256"] = digest(zero_record)
                zero_branches.append(zero_record)

            for normal_ordinal, normal_term in enumerate(normal):
                polynomial = normal_term.polynomial.scale(to_dword_gaussian(scalar))
                edge_key = tuple(
                    (
                        token.derivative_kind,
                        token.spinor_component,
                    )
                    for token in normal_term.ordered_tokens
                )
                key = signature, edge_key
                group_key_sha = digest(
                    {
                        "survivor_signature": _survivor_json(signature),
                        "remaining_e_AI_tokens": _edge_tokens_json(
                            normal_term.ordered_tokens
                        ),
                    }
                )
                contribution_core = {
                    "type_id": "TYPE::PreAggregationDeltaNormalBranch",
                    "parent_pair_id": pair_id,
                    "action_raw_trace_history_id": str(action_history["history_id"]),
                    "insertion_raw_trace_history_id": str(
                        insertion_history["history_id"]
                    ),
                    "measure_branch_id": measure_record["measure_branch_id"],
                    "measure_scope_map_id": measure_scope_map["measure_scope_map_id"],
                    "source_measure_scope_id": measure_scope_map["source_scope_id"],
                    "executed_measure_scope_id": measure_scope_map["target_scope_id"],
                    "delta_scope_id": delta_binding["scope_id"],
                    "delta_scope_consumption": deepcopy(delta_consumption),
                    "scope_execution_order": execution_order,
                    "normal_ordinal": normal_ordinal,
                    "original_factor_order": factor_order,
                    "canonical_preaggregation_order": canonical_ports,
                    "contracted_action_word_outer_to_inner": list(action_word),
                    "contracted_insertion_word_outer_to_inner": list(insertion_word),
                    "survivor_signature": _survivor_json(signature),
                    "remaining_e_AI_tokens": _edge_tokens_json(
                        normal_term.ordered_tokens
                    ),
                    "exact_scalar_before_delta_word": qi_json(scalar),
                    "coefficient_reordering_sign": reorder_sign,
                    "derivative_extraction_sign": extraction_sign,
                    "delta_and_odd_word_ledger": list(normal_term.ledger),
                    "event_counts": _event_count(normal_term.ledger),
                    "residual_IBP_events": [],
                    "residual_IBP_performed": False,
                    "exact_polynomial": polynomial.to_json(),
                    "aggregate_group_key_sha256": group_key_sha,
                }
                contribution_id = f"CONTRIB::{digest(contribution_core)[:28]}"
                contribution = {
                    "contribution_id": contribution_id,
                    **contribution_core,
                }
                contribution["record_sha256"] = digest(contribution)
                contributions.append(contribution)
                aggregate_polynomials[key] = (
                    aggregate_polynomials.get(key, dword.POLY_ZERO) + polynomial
                )
                parent_polynomial = aggregate_incidence[key].get(
                    pair_id, dword.POLY_ZERO
                )
                aggregate_incidence[key][pair_id] = parent_polynomial + polynomial
                aggregate_contribution_ids[key].append(contribution_id)

    aggregate_polynomials = {
        key: polynomial
        for key, polynomial in aggregate_polynomials.items()
        if polynomial
    }
    source_endpoint = _edge_endpoints(delta_binding)[
        str(delta_binding["source_endpoint_id"])
    ]
    edge_square = dword.endpoint_square_polynomial(source_endpoint)
    aggregate_rows: list[dict[str, Any]] = []
    contact_catalog: list[dict[str, Any]] = []
    remainder_catalog: list[dict[str, Any]] = []
    contact_parent_pairs: set[str] = set()
    remainder_parent_pairs: set[str] = set()
    incidence_nonzero_count = 0
    token_counts: Counter[int] = Counter()

    for (signature, edge_key), polynomial in sorted(aggregate_polynomials.items()):
        tokens_json = [
            {"derivative_kind": kind, "spinor_component": component}
            for kind, component in edge_key
        ]
        catalog_record = {
            "survivor_signature": _survivor_json(signature),
            "remaining_e_AI_tokens": tokens_json,
            "polynomial_sha256": digest(polynomial.to_json()),
        }
        quotient = polynomial.scalar_multiple_of(edge_square)
        classification = "EDGE_SQUARE_CONTACT" if quotient is not None else "REMAINDER"
        if quotient is not None:
            catalog_record["edge_square_quotient"] = dword_qi_json(quotient)
            contact_catalog.append(catalog_record)
            token_counts[len(edge_key)] += 1
        else:
            remainder_catalog.append(catalog_record)
        raw_parent_incidence = aggregate_incidence[(signature, edge_key)]
        parent_rows = _parent_incidence_json(raw_parent_incidence)
        parent_sum = dword.POLY_ZERO
        for parent_polynomial in raw_parent_incidence.values():
            parent_sum = parent_sum + parent_polynomial
        parent_ids = {str(row["parent_pair_id"]) for row in parent_rows}
        if quotient is not None:
            contact_parent_pairs.update(parent_ids)
        else:
            remainder_parent_pairs.update(parent_ids)
        group_id = f"PREAGG::{classification}::{digest(catalog_record)[:28]}"
        aggregate_rows.append(
            {
                "aggregate_group_id": group_id,
                "classification": classification,
                **catalog_record,
                "exact_polynomial": polynomial.to_json(),
                "primitive_contribution_ids": sorted(
                    aggregate_contribution_ids[(signature, edge_key)]
                ),
                "primitive_contribution_count": len(
                    aggregate_contribution_ids[(signature, edge_key)]
                ),
                "parent_incidence": parent_rows,
                "parent_incidence_count": len(parent_rows),
                "parent_incidence_reconstructs_aggregate": (parent_sum == polynomial),
            }
        )
        incidence_nonzero_count += len(parent_rows)

    contact_hash = digest(contact_catalog)
    remainder_hash = digest(remainder_catalog)
    seed_pair_ids = {str(record["provenance_id"]) for record in parent_pairs}
    referenced_pair_ids = {
        str(record["parent_pair_id"]) for record in contributions
    } | {str(record["parent_pair_id"]) for record in zero_branches}
    replay = {
        "source_group_join_id": seed_replay["source_group_join_id"],
        "resolved_type_id": RESOLVED_TYPE_ID,
        "seed_binding": {
            "resolved_seed_type_id": seed_payload["resolved_seed_type_id"],
            "seed_file_sha256": EXPECTED_SEED_FILE_SHA256,
            "seed_payload_sha256": seed_payload["payload_sha256"],
            "source_row_count": seed_replay["source_row_count"],
            "raw_history_count": seed_replay["raw_history_count"],
            "raw_histories_sha256": seed_replay["raw_histories_sha256"],
            "unaggregated_pair_count": seed_replay["unaggregated_pair_count"],
            "unaggregated_pairs_sha256": seed_replay["unaggregated_pairs_sha256"],
        },
        "deferred_measure_scope": measure_scope,
        "measure_scope_map": measure_scope_map,
        "delta_scope": delta_scope,
        "delta_scope_binding": delta_binding,
        "parent_pair_contracts": [
            _compact_parent_pair(record) for record in parent_pairs
        ],
        "measure_distributed_action_histories": measure_branches,
        "primitive_normal_contributions": contributions,
        "primitive_zero_branches": zero_branches,
        "aggregate_rows": aggregate_rows,
        "contact_catalog": contact_catalog,
        "remainder_catalog": remainder_catalog,
        "counts": {
            "source_rows": seed_replay["source_row_count"],
            "raw_histories": len(raw_histories),
            "raw_parent_pairs": len(parent_pairs),
            "measure_distributed_action_histories": len(measure_branches),
            "measure_pair_histories": measure_pair_history_count,
            "primitive_normal_contributions": len(contributions),
            "primitive_zero_branches": len(zero_branches),
            "nonzero_aggregate_groups": len(aggregate_rows),
            "edge_square_contact_groups": len(contact_catalog),
            "remainder_groups": len(remainder_catalog),
            "sparse_parent_incidence_entries": incidence_nonzero_count,
            "contact_parent_pairs": len(contact_parent_pairs),
            "remainder_parent_pairs": len(remainder_parent_pairs),
        },
        "measure_children_per_raw_action_history": {
            str(key): value
            for key, value in sorted(action_measure_child_counts.items())
        },
        "contact_remaining_edge_token_counts": {
            str(key): value for key, value in sorted(token_counts.items())
        },
        "parent_pair_reference_coverage": {
            "seed_parent_pair_ids_sha256": digest(sorted(seed_pair_ids)),
            "referenced_parent_pair_ids_sha256": digest(sorted(referenced_pair_ids)),
            "sets_equal": referenced_pair_ids == seed_pair_ids,
        },
        "shared_primitive_oracle_regression": {
            "role": "NON_INDEPENDENT_SHARED_ORACLE_RECONSTRUCTION",
            "contact_catalog_sha256": contact_hash,
            "shared_oracle_contact_catalog_sha256": (SHARED_ORACLE_CONTACT_HASH),
            "contact_hash_agrees": (contact_hash == SHARED_ORACLE_CONTACT_HASH),
            "remainder_catalog_sha256": remainder_hash,
            "shared_oracle_remainder_catalog_sha256": (SHARED_ORACLE_REMAINDER_HASH),
            "remainder_hash_agrees": (remainder_hash == SHARED_ORACLE_REMAINDER_HASH),
            "contact_object_equality": None,
            "remainder_object_equality": None,
            "remainder_object_equality_status": ("UNPROVED_NO_OBJECT_LEVEL_COMPARATOR"),
        },
        "residual_contact_IBP": {
            "missing_type_id": RESIDUAL_IBP_MISSING_TYPE_ID,
            "execution_state": "OPEN_NOT_EXECUTED",
            "input_domain": (
                "608 EdgeSquare contact aggregates with 1--3 residual e_AI tokens"
            ),
            "codomain": ("graded coproduct over ordered A-local survivors (A.q1,A.q2)"),
            "primitive_contact_count": len(contact_catalog),
            "parent_incidence_is_available": bool(aggregate_rows),
            "bound_I3_comparison_matrix": None,
            "anomaly_coefficient": None,
        },
        "remainder_object_comparison": {
            "missing_type_id": REMAINDER_COMPARATOR_MISSING_TYPE_ID,
            "execution_state": "OPEN_NOT_EXECUTED",
            "object_level_equality": None,
        },
    }
    replay["provenance_checks"] = _computed_provenance_predicates(replay, seed_payload)
    return replay


def _computed_provenance_predicates(
    replay: Mapping[str, Any], seed_payload: Mapping[str, Any]
) -> dict[str, bool]:
    seed_replay = seed_payload["measure_tagged_raw_replay"]
    histories = {str(row["history_id"]): row for row in seed_replay["raw_histories"]}
    pairs = {
        str(row["provenance_id"]): row
        for row in seed_replay["unaggregated_contact_provenance"]
    }
    scope_map = replay["measure_scope_map"]
    expected_scope_map = _validated_measure_scope_map(seed_replay["measure_scopes"][0])
    delta_binding = replay["delta_scope_binding"]
    expected_delta_binding = _validated_delta_scope(
        seed_payload["finite_delta_convolution"]["delta_scope"]
    )

    measure_by_id = {
        str(row["measure_branch_id"]): row
        for row in replay["measure_distributed_action_histories"]
    }
    measure_records_valid = len(measure_by_id) == len(
        replay["measure_distributed_action_histories"]
    )
    measure_signs_valid = True
    measure_orders_valid = True
    measure_normalizations_valid = True
    for row in measure_by_id.values():
        parent = histories.get(str(row["parent_action_raw_trace_history_id"]))
        measure_records_valid &= _record_hash_valid(row) and parent is not None
        if parent is None:
            measure_orders_valid = False
            measure_normalizations_valid = False
            continue
        parent_order = [
            str(factor["grammar_port_id"])
            for factor in parent["factors_in_raw_AST_order"]
        ]
        child_order = [
            str(factor["grammar_port_id"])
            for factor in row["factors_in_original_AST_order_after_measure"]
        ]
        measure_orders_valid &= parent_order == child_order
        expected_after = constant_gaussian_from_poly_json(
            parent["coefficient"]
        ) * oracle_qi_from_json(row["measure_relative_scalar"])
        measure_normalizations_valid &= (
            row["measure_scope_map_id"] == scope_map["measure_scope_map_id"]
            and row["source_deferred_measure_scope_id"] == scope_map["source_scope_id"]
            and row["executed_measure_scope_id"] == scope_map["target_scope_id"]
            and row["normalization_application_count"]
            == scope_map["normalization_application_count"]
            == 1
            and row["measure_normalization"] == scope_map["source_normalization"]
            and oracle_qi_from_json(row["coefficient_after_measure"]) == expected_after
        )
        for hit in row["measure_primitive_hits"]:
            prefix = 0
            for parity in hit["prefix_factor_parities"]:
                prefix ^= int(parity)
            expected_exponent = prefix ^ int(hit["hit_leaf_coefficient_parity"])
            expected_sign = -1 if expected_exponent else 1
            measure_signs_valid &= (
                hit["scope_map_id"] == scope_map["measure_scope_map_id"]
                and hit["source_scope_id"] == scope_map["source_scope_id"]
                and hit["executed_scope_id"] == scope_map["target_scope_id"]
                and int(hit["prefix_parity"]) == prefix
                and int(hit["sign_exponent_mod_2"]) == expected_exponent
                and int(hit["koszul_sign"]) == expected_sign
            )

    branch_rows = [
        *replay["primitive_normal_contributions"],
        *replay["primitive_zero_branches"],
    ]
    branch_records_valid = True
    original_orders_valid = True
    delta_consumption_valid = True
    execution_order_valid = True
    residual_ibp_open = True
    for row in branch_rows:
        pair = pairs.get(str(row["parent_pair_id"]))
        measure = measure_by_id.get(str(row["measure_branch_id"]))
        branch_records_valid &= (
            _record_hash_valid(row) and pair is not None and measure is not None
        )
        if pair is None or measure is None:
            original_orders_valid = False
            delta_consumption_valid = False
            execution_order_valid = False
            residual_ibp_open = False
            continue
        insertion = histories[str(pair["insertion_raw_trace_history_id"])]
        expected_order = [
            str(factor["grammar_port_id"])
            for factor in (
                *measure["factors_in_original_AST_order_after_measure"],
                *insertion["factors_in_raw_AST_order"],
            )
        ]
        original_orders_valid &= (
            row["original_factor_order"] == expected_order
            and row["canonical_preaggregation_order"]
            == pair["factor_order_ledger"]["canonical_preaggregation_order"]
        )
        consumption = row["delta_scope_consumption"]
        endpoint_evidence = consumption["contracted_endpoint_validation_evidence"]
        delta_consumption_valid &= (
            _record_hash_valid(consumption)
            and consumption["delta_binding_id"] == delta_binding["delta_binding_id"]
            and consumption["delta_scope_id"] == delta_binding["scope_id"]
            and consumption["delta_scope_record_sha256"]
            == delta_binding["delta_scope_record_sha256"]
            and consumption["parent_scope_id_resolved"] is True
            and consumption["contracted_endpoint_records_validated"]
            == all(evidence["validated"] for evidence in endpoint_evidence)
            and len(endpoint_evidence) == 2
            and all(evidence["validated"] for evidence in endpoint_evidence)
            and sum(
                1
                for event in row["delta_and_odd_word_ledger"]
                if event["kind"] == "ENDPOINT_TRANSFER"
            )
            == len(row["contracted_insertion_word_outer_to_inner"])
        )
        execution_order_valid &= row["scope_execution_order"] == [
            scope_map["target_scope_id"],
            delta_binding["scope_id"],
            "PRIMITIVE_DALGEBRA_SHARED_ORACLE",
            "CONTACT_AGGREGATION_NOT_YET_EXECUTED",
        ]
        residual_ibp_open &= (
            row["residual_IBP_events"] == []
            and row["residual_IBP_performed"] is False
            and all(
                event.get("phase") != "PIVOTED_IBP"
                for event in row["delta_and_odd_word_ledger"]
            )
        )
        if "event_counts" in row:
            branch_records_valid &= row["event_counts"] == _event_count(
                row["delta_and_odd_word_ledger"]
            )

    incidence_exact = True
    for aggregate in replay["aggregate_rows"]:
        aggregate_polynomial = _exact_polynomial_from_json(
            aggregate["exact_polynomial"]
        )
        parent_sum = dword.POLY_ZERO
        for parent_row in aggregate["parent_incidence"]:
            parent_polynomial = _exact_polynomial_from_json(
                parent_row["exact_polynomial"]
            )
            incidence_exact &= parent_row["polynomial_sha256"] == digest(
                parent_row["exact_polynomial"]
            )
            parent_sum = parent_sum + parent_polynomial
        incidence_exact &= (
            parent_sum == aggregate_polynomial
            and aggregate["polynomial_sha256"] == digest(aggregate["exact_polynomial"])
            and aggregate["parent_incidence_reconstructs_aggregate"]
            == (parent_sum == aggregate_polynomial)
            and aggregate["parent_incidence_count"]
            == len(aggregate["parent_incidence"])
        )

    seed_pair_ids = set(pairs)
    referenced_pair_ids = {str(row["parent_pair_id"]) for row in branch_rows}
    pair_coefficients_exact = all(
        _pair_preaggregation_coefficient_exact(
            pair,
            histories[str(pair["action_raw_trace_history_id"])],
            histories[str(pair["insertion_raw_trace_history_id"])],
        )
        == oracle_qi_from_json(pair["preaggregation_exact_coefficient_before_measure"])
        for pair in pairs.values()
    )
    return {
        "seed_fixture_self_hash_valid": (
            seed_payload["payload_sha256"]
            == digest(
                {
                    key: value
                    for key, value in seed_payload.items()
                    if key != "payload_sha256"
                }
            )
        ),
        "parent_pair_exact_factor_ledgers_reconstruct": (pair_coefficients_exact),
        "measure_scope_map_exact": scope_map == expected_scope_map,
        "measure_branch_record_hashes_valid": measure_records_valid,
        "measure_normalization_applied_once": measure_normalizations_valid,
        "measure_koszul_signs_recomputed": measure_signs_valid,
        "original_factor_order_recomputed": (
            measure_orders_valid and original_orders_valid
        ),
        "delta_scope_binding_exact": delta_binding == expected_delta_binding,
        "delta_scope_consumed_branchwise": delta_consumption_valid,
        "scope_execution_order_recomputed": execution_order_valid,
        "branch_record_hashes_valid": branch_records_valid,
        "all_seed_parent_pairs_referenced": (referenced_pair_ids == seed_pair_ids),
        "all_parent_incidence_reconstructs_aggregate": incidence_exact,
        "residual_contact_IBP_explicitly_open": (
            residual_ibp_open
            and replay["residual_contact_IBP"]["execution_state"] == "OPEN_NOT_EXECUTED"
            and replay["residual_contact_IBP"]["anomaly_coefficient"] is None
        ),
    }


DIRECT_IMPORT_PATHS = (
    "scripts/step6_coefficient_tensor.py",
    "scripts/step6_two_loop_dword.py",
    "scripts/step6_global_dword_adapter.py",
)
TRANSITIVE_IMPORT_PATHS = (
    "scripts/step6_symbolic_grassmann_oracle.py",
    "scripts/step6_two_loop_graphir.py",
    "scripts/step6_global_supertensor.py",
    "scripts/step6_two_loop_amplitude_ir.py",
    "scripts/step6_color_tensor.py",
    "scripts/step6_external_projection.py",
    "scripts/step6_two_loop_grammar.py",
    "scripts/step6_two_loop_wick.py",
    "scripts/verify_step5a_fixed_kernel.py",
    "scripts/verify_step5_propagators.py",
)
CONTRACT_PATH = "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"


@lru_cache(maxsize=1)
def build_payload() -> dict[str, Any]:
    replay = _replay()
    input_paths = (
        str(SEED_FIXTURE.relative_to(ROOT)),
        *DIRECT_IMPORT_PATHS,
        *TRANSITIVE_IMPORT_PATHS,
        CONTRACT_PATH,
    )
    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "resolved_type_id": RESOLVED_TYPE_ID,
        "open_missing_type_ids": [
            REMAINDER_COMPARATOR_MISSING_TYPE_ID,
            RESIDUAL_IBP_MISSING_TYPE_ID,
        ],
        "external_result_used_as_input": False,
        "measure_tagged_delta_convolution_replay": replay,
        "input_provenance": {
            "frozen_seed_role": (
                "BOUNDED_COHERENT_INPUT_FIXTURE_NOT_AN_INDEPENDENT_ORACLE"
            ),
            "direct_import_paths": list(DIRECT_IMPORT_PATHS),
            "transitive_import_paths": list(TRANSITIVE_IMPORT_PATHS),
            "file_sha256": {path: file_sha256(ROOT / path) for path in input_paths},
            "explicitly_not_imported": {
                "scripts/step6_ordered_sector_euler_normal_form.py": (
                    "REMOVED_FROM_DIRECT_DEPENDENCY"
                ),
                "scripts/step6_full_dword_bridge.py": (
                    "REMOVED_FROM_DIRECT_DEPENDENCY"
                ),
                "scripts/step6_grouped_e_v_i2_i3_ordered_port_normal_form.py": (
                    "REMOVED_FROM_DIRECT_DEPENDENCY"
                ),
                "scripts/step6_measure_tagged_delta_convolution.py": (
                    "REPLACED_BY_FROZEN_HASHED_FIXTURE"
                ),
            },
        },
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def _input_hashes_valid(payload: Mapping[str, Any]) -> bool:
    hashes = payload["input_provenance"]["file_sha256"]
    return all(
        (ROOT / path).is_file() and file_sha256(ROOT / path) == expected
        for path, expected in hashes.items()
    )


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    replay = payload["measure_tagged_delta_convolution_replay"]
    counts = replay["counts"]
    computed = _computed_provenance_predicates(replay, _load_seed_fixture())
    regression = replay["shared_primitive_oracle_regression"]
    return {
        "schema_and_status_exact": (
            payload["schema"] == SCHEMA
            and payload["status"] == STATUS
            and payload["resolved_type_id"] == RESOLVED_TYPE_ID
        ),
        "frozen_seed_cardinalities": (
            counts["source_rows"] == 6
            and counts["raw_histories"] == 216
            and counts["raw_parent_pairs"] == 768
        ),
        "measure_distribution_exact": (
            replay["measure_children_per_raw_action_history"] == {"18": 192}
            and counts["measure_distributed_action_histories"] == 3456
            and counts["measure_pair_histories"] == 13824
        ),
        "computed_branch_provenance_predicates": (
            all(computed.values()) and replay["provenance_checks"] == computed
        ),
        "aggregate_cardinalities_exact": (
            counts["primitive_normal_contributions"] == 13568
            and counts["primitive_zero_branches"] == 36096
            and counts["nonzero_aggregate_groups"] == 2176
            and counts["edge_square_contact_groups"] == 608
            and counts["remainder_groups"] == 1568
        ),
        "contact_token_counts_exact": (
            replay["contact_remaining_edge_token_counts"]
            == {"1": 192, "2": 320, "3": 96}
        ),
        "shared_oracle_digest_regression": (
            regression["role"] == "NON_INDEPENDENT_SHARED_ORACLE_RECONSTRUCTION"
            and regression["contact_hash_agrees"]
            and regression["remainder_hash_agrees"]
            and regression["contact_catalog_sha256"] == SHARED_ORACLE_CONTACT_HASH
            and regression["remainder_catalog_sha256"] == SHARED_ORACLE_REMAINDER_HASH
        ),
        "object_level_remainder_equality_explicitly_unproved": (
            regression["remainder_object_equality"] is None
            and regression["remainder_object_equality_status"]
            == "UNPROVED_NO_OBJECT_LEVEL_COMPARATOR"
            and replay["remainder_object_comparison"]["object_level_equality"] is None
            and replay["remainder_object_comparison"]["execution_state"]
            == "OPEN_NOT_EXECUTED"
        ),
        "residual_contact_ibp_explicitly_open": (
            replay["residual_contact_IBP"]["missing_type_id"]
            == RESIDUAL_IBP_MISSING_TYPE_ID
            and replay["residual_contact_IBP"]["execution_state"] == "OPEN_NOT_EXECUTED"
            and replay["residual_contact_IBP"]["bound_I3_comparison_matrix"] is None
            and replay["residual_contact_IBP"]["anomaly_coefficient"] is None
        ),
        "input_hash_closure_valid": _input_hashes_valid(payload),
        "no_external_result": (payload["external_result_used_as_input"] is False),
        "payload_hash_valid": (
            payload["payload_sha256"]
            == digest(
                {
                    key: value
                    for key, value in payload.items()
                    if key != "payload_sha256"
                }
            )
        ),
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    replay = payload["measure_tagged_delta_convolution_replay"]
    regression = replay["shared_primitive_oracle_regression"]
    return {
        "schema": "step6.preaggregation_measure_delta_replay.audit.v2",
        "status": payload["status"],
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "counts": replay["counts"],
        "contact_remaining_edge_token_counts": replay[
            "contact_remaining_edge_token_counts"
        ],
        "contact_catalog_sha256": regression["contact_catalog_sha256"],
        "remainder_catalog_sha256": regression["remainder_catalog_sha256"],
        "remainder_object_equality": None,
        "reconstruction_requires_fresh_compiler": True,
        "standalone_replay_certificate": False,
        "semantic_scope": SEMANTIC_SCOPE,
        "aggregate_rows_with_parent_incidence_sha256": digest(replay["aggregate_rows"]),
        "resolved_type_id": RESOLVED_TYPE_ID,
        "open_missing_type_ids": payload["open_missing_type_ids"],
        "input_provenance": payload["input_provenance"],
        "payload_sha256": payload["payload_sha256"],
        "script_sha256": file_sha256(Path(__file__)),
        "test_sha256": file_sha256(TEST_PATH),
    }


def build_summary(payload: Mapping[str, Any]) -> dict[str, Any]:
    replay = payload["measure_tagged_delta_convolution_replay"]
    regression = replay["shared_primitive_oracle_regression"]
    measure_hits = Counter(
        int(hit["koszul_sign"])
        for row in replay["measure_distributed_action_histories"]
        for hit in row["measure_primitive_hits"]
    )
    normal_events = Counter(
        str(event["kind"])
        for row in replay["primitive_normal_contributions"]
        for event in row["delta_and_odd_word_ledger"]
    )
    zero_events = Counter(
        str(event["kind"])
        for row in replay["primitive_zero_branches"]
        for event in row["delta_and_odd_word_ledger"]
    )
    zero_classes = Counter(
        str(row["classification"]) for row in replay["primitive_zero_branches"]
    )
    summary = {
        "schema": "step6.preaggregation_measure_delta_replay.summary.v2",
        "status": payload["status"],
        "resolved_type_id": payload["resolved_type_id"],
        "open_missing_type_ids": payload["open_missing_type_ids"],
        "input_provenance": payload["input_provenance"],
        "payload_sha256": payload["payload_sha256"],
        "counts": replay["counts"],
        "measure_children_per_raw_action_history": replay[
            "measure_children_per_raw_action_history"
        ],
        "contact_remaining_edge_token_counts": replay[
            "contact_remaining_edge_token_counts"
        ],
        "shared_primitive_oracle_regression": regression,
        "provenance_checks": replay["provenance_checks"],
        "event_counts": {
            "measure_hit_koszul_sign": {
                str(key): value for key, value in sorted(measure_hits.items())
            },
            "normal_delta_and_odd_word": dict(sorted(normal_events.items())),
            "zero_delta_and_odd_word": dict(sorted(zero_events.items())),
            "zero_classifications": dict(sorted(zero_classes.items())),
        },
        "factorized_table_sha256": {
            "parent_pair_contracts": digest(replay["parent_pair_contracts"]),
            "measure_distributed_action_histories": digest(
                replay["measure_distributed_action_histories"]
            ),
            "primitive_normal_contributions": digest(
                replay["primitive_normal_contributions"]
            ),
            "primitive_zero_branches": digest(replay["primitive_zero_branches"]),
            "aggregate_rows_with_parent_incidence": digest(replay["aggregate_rows"]),
        },
        "full_event_payload_materialized": False,
        "fresh_compiler_reconstructs_full_event_payload": True,
        "reconstruction_requires_fresh_compiler": True,
        "standalone_replay_certificate": False,
        "semantic_scope": SEMANTIC_SCOPE,
        "independent_remainder_object_comparison_performed": False,
        "residual_contact_ibp_performed": False,
        "all_exact_checks_pass": all(exact_checks(payload).values()),
    }
    summary["summary_sha256"] = digest(summary)
    return summary


def write_outputs(payload: Mapping[str, Any]) -> None:
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_text(
        json.dumps(build_summary(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    AUDIT.write_text(
        json.dumps(build_audit(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    payload = build_payload()
    audit = build_audit(payload)
    if not audit["all_checks_passed"]:
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise SystemExit(f"exact checks failed: {failed}")
    write_outputs(payload)
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
