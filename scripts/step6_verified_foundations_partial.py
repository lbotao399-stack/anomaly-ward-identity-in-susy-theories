#!/usr/bin/env python3
"""Render the bounded, verified Step-6 foundations as a partial mirror.

Only exact facts already present in Project JSON/audit artifacts are admitted.
Every rendered count and status is guarded by a fail-closed equality check.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[1]

SOURCE_PATHS = {
    "valence": Path("generated/step6/two-loop-graphir/valence-families.json"),
    "six_parent": Path("audits/step6-three-parent-completeness-verification.json"),
    "union": Path("audits/step6-union-coefficient-circuit-verification.json"),
    "restricted_three_result": Path(
        "generated/step6/three-parent-sector-sharded-evaluator/results/complete-restricted-three-result.json"
    ),
    "restricted_three_audit": Path(
        "audits/step6-three-parent-sector-sharded-complete-restricted-three-verification.json"
    ),
    "overall_k": Path("generated/step6/overall-k-map/overall-k-map.json"),
    "overall_k_audit": Path("audits/step6-overall-k-map-verification.json"),
    "measure": Path("audits/step6-measure-tagged-delta-convolution-verification.json"),
    "odd_word_sign": Path("audits/step6-odd-word-transfer-sign-verification.json"),
    "contact_provenance": Path(
        "audits/step6-primitive-contact-provenance-audit-verification.json"
    ),
    "physical_sd": Path("audits/step6-physical-sd-full-orbit-verification.json"),
    "descent": Path(
        "audits/step6-three-parent-open-raw-axis-circuit-verification.json"
    ),
    "laurent": Path(
        "generated/step6/connected-scalar-laurent/connected-scalar-laurent.json"
    ),
}

OUTPUT = Path(
    "generated/step6/verified-foundations/step6-verified-foundations-partial.md"
)
AUDIT = Path("audits/step6-verified-foundations-partial-verification.json")

SCHEMA = "step6.verified_foundations_partial.v1"
AUDIT_SCHEMA = "step6.verified_foundations_partial.audit.v1"
DOCUMENT_STATUS = "UNMERGED_PROPOSAL"

EXPECTED_FAMILY_IDS = [
    "I2__S3^4",
    "I2__S3^2__S4^1",
    "I2__S3^1__S5^1",
    "I2__S4^2",
    "I2__S6^1",
    "I3__S3^3",
    "I3__S3^1__S4^1",
    "I3__S5^1",
    "I4__S3^2",
    "I4__S4^1",
    "I5__S3^1",
    "I6__NO_ACTION_VERTEX",
]

ANALYTIC_VALENCE_FAMILIES = [
    r"I_2S_3^4",
    r"I_2S_3^2S_4",
    r"I_2S_3S_5",
    r"I_2S_4^2",
    r"I_2S_6",
    r"I_3S_3^3",
    r"I_3S_3S_4",
    r"I_3S_5",
    r"I_4S_3^2",
    r"I_4S_4",
    r"I_5S_3",
    r"I_6",
]

EXPECTED_K4E_CLASSES = [
    {
        "graph_id": "G6_DIRECT_K4ME_I2_S3SQ_S4",
        "family_id": "I2__S3^2__S4^1",
        "external_hosts": {"p1": "A", "p2": "C"},
        "automorphism_order": 1,
        "weight": {"numerator": -1, "denominator": 1},
    },
    {
        "graph_id": "G6_DIRECT_K4ME_I2_S3SQ_S4_P1S4_P2S3",
        "family_id": "I2__S3^2__S4^1",
        "external_hosts": {"p1": "C", "p2": "A"},
        "automorphism_order": 1,
        "weight": {"numerator": -1, "denominator": 1},
    },
    {
        "graph_id": "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4",
        "family_id": "I2__S3^2__S4^1",
        "external_hosts": {"p1": "C", "p2": "C"},
        "automorphism_order": 2,
        "weight": {"numerator": -1, "denominator": 2},
    },
    {
        "graph_id": "G6_DIRECT_K4ME_I3_S3CUBED",
        "family_id": "I3__S3^3",
        "external_hosts": {"p1": "A", "p2": "B"},
        "automorphism_order": 1,
        "weight": {"numerator": -1, "denominator": 1},
    },
    {
        "graph_id": "G6_DIRECT_K4ME_I3_S3CUBED_P1S3_P2I",
        "family_id": "I3__S3^3",
        "external_hosts": {"p1": "A", "p2": "I"},
        "automorphism_order": 2,
        "weight": {"numerator": -1, "denominator": 2},
    },
    {
        "graph_id": "G6_DIRECT_K4ME_I3_S3CUBED_P1I_P2S3",
        "family_id": "I3__S3^3",
        "external_hosts": {"p1": "I", "p2": "A"},
        "automorphism_order": 2,
        "weight": {"numerator": -1, "denominator": 2},
    },
]

EXPECTED_OLD3 = [
    "G6_DIRECT_K4ME_I2_S3SQ_S4",
    "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4",
    "G6_DIRECT_K4ME_I3_S3CUBED",
]

EXPECTED_NEW3 = [
    "G6_DIRECT_K4ME_I2_S3SQ_S4_P1S4_P2S3",
    "G6_DIRECT_K4ME_I3_S3CUBED_P1S3_P2I",
    "G6_DIRECT_K4ME_I3_S3CUBED_P1I_P2S3",
]


class SourceDriftError(RuntimeError):
    """Raised when a source certificate no longer has the admitted value."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def payload_sha256(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def expect(condition: bool, label: str) -> None:
    if not condition:
        raise SourceDriftError(f"source drift: {label}")


def load_sources(root: Path = ROOT) -> dict[str, Any]:
    return {
        name: json.loads((root / relative).read_text(encoding="utf-8"))
        for name, relative in SOURCE_PATHS.items()
    }


def source_hashes(root: Path = ROOT) -> dict[str, str]:
    return {
        str(relative): file_sha256(root / relative)
        for relative in SOURCE_PATHS.values()
    }


def _validate_valence(source: Mapping[str, Any]) -> list[str]:
    expect(
        source.get("schema_version") == "step6.two_loop_graphir.v1", "valence schema"
    )
    families = source.get("families")
    expect(isinstance(families, list), "valence families type")
    expect(len(families) == 12, "valence family count")
    expect(
        [row.get("family_id") for row in families] == EXPECTED_FAMILY_IDS,
        "valence family ids",
    )
    for row in families:
        identity = row.get("identity", {})
        expect(
            row.get("classification") == "VALENCE_NOT_GRAPH",
            f"{row.get('family_id')} classification",
        )
        expect(row.get("graph_ir") is None, f"{row.get('family_id')} graph_ir")
        expect(identity.get("L") == 2, f"{row.get('family_id')} loop count")
        expect(identity.get("lhs") == 4, f"{row.get('family_id')} lhs")
        expect(identity.get("rhs") == 4, f"{row.get('family_id')} rhs")
        expect(
            identity.get("required_value") == 4,
            f"{row.get('family_id')} required value",
        )
    return list(EXPECTED_FAMILY_IDS)


def _validate_six_parent(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.six_parent_k4e_completeness.audit.v2",
        "six-parent schema",
    )
    expect(
        source.get("status") == "PASS_EXACT_SIX_PARENT_K4E_CLOSURE_AUDIT",
        "six-parent status",
    )
    expect(
        source.get("authority_role") == "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "six-parent authority role",
    )
    expect(
        source.get("authority", {}).get("step6_task_authorized") is False,
        "Step-6 authority boundary",
    )
    expect(source.get("Q2_bb_result") is None, "six-parent Q2 result")
    expect(source.get("coefficient_claim") is None, "six-parent coefficient claim")

    source_valence = source.get("source_valence", {})
    expect(source_valence.get("reduced_family_count") == 12, "reduced family count")
    expect(
        source_valence.get("K4e_capable_family_ids") == ["I2__S3^2__S4^1", "I3__S3^3"],
        "K4e capable families",
    )

    census = source.get("K4e_background_labeled_census", {})
    expect(census.get("all_class_count") == 6, "K4e class count")
    expect(census.get("literal_GraphIR_count") == 6, "literal K4e GraphIR count")
    expect(
        census.get("missing_literal_GraphIR_count") == 0,
        "missing literal K4e GraphIR count",
    )
    actual_classes = []
    for row in census.get("classes", []):
        ids = row.get("literal_graphir_ids", [])
        expect(len(ids) == 1, "one literal GraphIR per K4e class")
        expect(
            row.get("literal_graphir_instantiated") is True, f"{ids[0]} instantiated"
        )
        actual_classes.append(
            {
                "graph_id": ids[0],
                "family_id": row.get("raw_valence_family_id"),
                "external_hosts": row.get("external_hosts"),
                "automorphism_order": row.get(
                    "background_source_labeled_automorphism_order"
                ),
                "weight": row.get("decorated_occurrence_orbit_weight"),
            }
        )
    expect(actual_classes == EXPECTED_K4E_CLASSES, "six exact K4e classes and weights")

    boundaries = source.get("full_boundaries", {})
    expected_boundaries = {
        "pure_vector_reduced_gate_graph_count": 273,
        "pure_vector_self_loop_graph_count": 178,
        "FP_admitted_candidate_count": 10,
        "matter_admitted_candidate_count": 12,
        "NK_classification": "PROVED_ABSENT_AT_THIS_ORDER",
    }
    expect(boundaries == expected_boundaries, "full gate counts")

    implication = source.get("implication_boundary", {})
    not_implied = implication.get("not_implied", {})
    expected_not_implied = {
        "FP_fixed_gauge_completion_is_zero",
        "N4_matter_completion_is_zero",
        "SD_contact_counterterm_orbit_is_zero",
        "complete_273_graph_pure_vector_gate_is_zero",
        "covariant_X_tensor_X_amplitude_is_zero",
        "renormalized_Q2_bb_is_zero",
    }
    expect(set(not_implied) == expected_not_implied, "full-gate implication keys")
    expect(all(not_implied.values()), "full-gate implications remain open")
    expect(
        implication.get("witnesses", {}).get(
            "non_K4e_or_additional_pure_vector_graph_classes"
        )
        == 267,
        "additional pure-vector graph count",
    )
    return {
        "classes": actual_classes,
        "full_boundaries": boundaries,
        "additional_vector": 267,
    }


def _validate_union(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.union_coefficient_circuit.audit.v1",
        "union schema",
    )
    expect(source.get("status") == "PASS", "union audit status")
    expect(source.get("failed") == 0, "union failed count")
    expect(
        source.get("execution", {}).get("production_evaluation")
        == "FAIL_CLOSED_NEW3_DALGEBRA_OPEN_AXIS_EVALUATOR_ABSENT",
        "union production evaluation",
    )
    payload = source.get("payload", {})
    counts = payload.get("counts", {})
    expected_counts = {
        "parent_factor_graph_count": 6,
        "structurally_compiled_parent_count": 3,
        "fail_closed_parent_count": 3,
        "bounded_materialized_parent_tuple_count": 3,
    }
    for key, expected in expected_counts.items():
        expect(counts.get(key) == expected, f"union {key}")
    partition = payload.get("compatibility_partition", {})
    expect(partition.get("old3_parent_ids") == EXPECTED_OLD3, "union old3 ids")
    expect(partition.get("new3_parent_ids") == EXPECTED_NEW3, "union new3 ids")
    expect(
        partition.get("old3_status")
        == "STRUCTURALLY_COMPILED_WITH_LEGACY_CERTIFIED_OPEN_AXIS_RECORDS",
        "union old3 status",
    )
    expect(
        partition.get("new3_status")
        == "FAIL_CLOSED_NO_CERTIFIED_DALGEBRA_OPEN_AXIS_EVALUATOR",
        "union new3 status",
    )
    expect(
        payload.get("boundary", {}).get("new3_D_algebra_open_axis_evaluation")
        == "BLOCKED_NO_CERTIFIED_EVALUATOR",
        "union open-axis boundary",
    )
    return {
        "counts": expected_counts,
        "old3": list(EXPECTED_OLD3),
        "new3": list(EXPECTED_NEW3),
    }


def _validate_restricted_three(
    result: Mapping[str, Any], audit: Mapping[str, Any]
) -> dict[str, Any]:
    expect(
        result.get("schema") == "step6.three_parent_sector_sharded_evaluator.result.v1",
        "restricted-three result schema",
    )
    expect(
        result.get("status") == "PASS_SECTOR_SHARDED_RESTRICTED_THREE_EVALUATION",
        "restricted-three result status",
    )
    expect(result.get("label") == "complete-restricted-three", "restricted-three label")
    scope = result.get("scope", {})
    expected_scope = {
        "evaluated_parent_class_count": 3,
        "all_host_literal_K4_minus_e_parent_class_count": 6,
        "strict_subset": True,
        "can_imply_full_K4_minus_e_result": False,
        "can_imply_Q2_bb": False,
    }
    expect(scope == expected_scope, "restricted-three scope")
    expect(
        result.get("requested_sector_count") == 40, "restricted-three requested sectors"
    )
    expect(
        result.get("complete_restricted_three_sector_count") == 40,
        "restricted-three completed sectors",
    )
    expect(
        result.get("is_complete_restricted_three_run") is True,
        "restricted-three completion flag",
    )
    expect(len(result.get("shards", [])) == 40, "restricted-three shard count")

    merge = result.get("merge_manifest", {})
    expect(
        merge.get("input_sparse_row_count") == 351_069, "restricted-three input rows"
    )
    expect(
        merge.get("output_sparse_row_count") == 55_518, "restricted-three output rows"
    )
    expect(merge.get("output_term_count") == 350_945, "restricted-three output terms")
    expect(
        merge.get("global_DAG_registry_constructed") is False,
        "restricted-three global DAG",
    )
    semantic = merge.get("semantic_expansion_gate", {})
    expect(
        semantic.get("status") == "NOT_RUN_SEPARATE_GATE",
        "restricted-three semantic gate",
    )
    expect(
        semantic.get("Poly_Exterior_distribution_performed") is False,
        "restricted-three Poly/Exterior expansion",
    )
    validation = result.get("merge_validation", {})
    expect(
        validation.get("status") == "VALIDATED_DISK_STREAMED_EXACT_SPARSE_MERGE",
        "restricted-three merge validation",
    )
    expect(
        validation.get("output_sparse_row_count") == 55_518,
        "restricted-three validated output rows",
    )
    expect(
        validation.get("output_term_count") == 350_945,
        "restricted-three validated output terms",
    )
    expect(
        validation.get("global_DAG_registry_constructed") is False,
        "restricted-three validated DAG",
    )
    expect(
        validation.get("semantic_expansion_performed") is False,
        "restricted-three validated semantic expansion",
    )
    boundary = result.get("boundary", {})
    expect(
        boundary.get("can_imply_full_K4_minus_e_result") is False,
        "restricted-three full K4-e boundary",
    )
    expect(
        boundary.get("covariant_projection_performed") is False,
        "restricted-three covariant projection",
    )
    expect(
        boundary.get("automatic_Project_X_source_map_descent_proved") is False,
        "restricted-three source-map descent",
    )
    expect(boundary.get("Q2_bb_result") is None, "restricted-three Q2 boundary")

    expect(
        audit.get("schema") == "step6.three_parent_sector_sharded_evaluator.audit.v1",
        "restricted-three audit schema",
    )
    expect(audit.get("status") == "PASS", "restricted-three audit status")
    expect(audit.get("passed") == 6, "restricted-three audit passed count")
    expect(audit.get("failed") == 0, "restricted-three audit failed count")
    expect(all(audit.get("checks", {}).values()), "restricted-three audit checks")
    expect(
        audit.get("checks", {}).get("no_global_DAG_or_semantic_expansion") is True,
        "restricted-three no global semantic expansion audit",
    )
    expect(
        audit.get("checks", {}).get("strict_three_of_six_scope_no_Q2") is True,
        "restricted-three scope audit",
    )
    return {
        "evaluated_parents": 3,
        "all_parents": 6,
        "completed_sectors": 40,
        "requested_sectors": 40,
        "input_sparse_rows": 351_069,
        "output_sparse_rows": 55_518,
        "output_terms": 350_945,
        "global_DAG_registry_constructed": False,
        "semantic_expansion_performed": False,
        "can_imply_full_K4_minus_e_result": False,
        "can_imply_Q2_bb": False,
    }


def _validate_overall_k(
    source: Mapping[str, Any], audit: Mapping[str, Any]
) -> dict[str, Any]:
    expect(source.get("schema") == "step6.overall_k_map.v1", "overall-K schema")
    expect(
        source.get("status") == "PASS_EXACT_OVERALL_K_RPRIME_DIRECT_B2_RAW_PARENT",
        "overall-K status",
    )
    expect(
        source.get("authority_role") == "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "overall-K authority",
    )
    scope = source.get("scope", {})
    expect(
        scope.get("graph_id") == "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4", "overall-K graph"
    )
    expect(scope.get("orientation") == "direct", "overall-K orientation")
    expect(scope.get("parent") == "completed_direct_B2_raw_parent", "overall-K parent")
    expect(scope.get("operation") == "K R'(G)", "overall-K operation")
    expect(scope.get("parent_union_included") is False, "overall-K parent union")

    contract = source.get("momentum_and_DRED_contract", {})
    expect(
        contract.get("all_incoming_relation") == "P+p1+p2=0",
        "overall-K momentum relation",
    )
    expect(
        contract.get("substitution_applied") == "P=-p1-p2",
        "overall-K momentum substitution",
    )
    expect(contract.get("external_scale") == "s12=(p1+p2)^2", "overall-K scale")
    expect(
        contract.get("logarithm") == "L_12=log(4*pi*mu^2/s12)-gamma_E",
        "overall-K logarithm",
    )

    result = source.get("overall_K_Rprime", {})
    expect(
        result.get("status") == "COMPLETE_EXACT_TWO_CHANNEL_LAURENT_MODULE",
        "overall-K result status",
    )
    expect(
        result.get("normalization") == "source_Qi*A0^2*h^3", "overall-K normalization"
    )
    counts = {
        "epsilon_minus_2_constant": result.get("epsilon_minus_2", {}).get(
            "term_instances_after_rowwise_collection"
        ),
        "epsilon_minus_1_log": result.get("epsilon_minus_1", {})
        .get("L_12", {})
        .get("term_instances_after_rowwise_collection"),
        "epsilon_minus_1_constant": result.get("epsilon_minus_1", {})
        .get("constant", {})
        .get("term_instances_after_rowwise_collection"),
    }
    expect(
        counts
        == {
            "epsilon_minus_2_constant": 3_035_883,
            "epsilon_minus_1_log": 0,
            "epsilon_minus_1_constant": 5_334_947,
        },
        "overall-K Laurent-channel counts",
    )
    expect(
        all(value == 0 for value in source.get("unresolved", {}).values()),
        "overall-K unresolved counts",
    )
    boundary = source.get("acceptance_boundary", {})
    expect(boundary.get("overall_K_operation_executed") is True, "overall-K executed")
    expect(
        boundary.get("R_operation_completed") is False, "R operation remains incomplete"
    )
    expect(
        boundary.get("parent_union_included") is False,
        "overall-K union remains incomplete",
    )
    expect(
        boundary.get("two_loop_AWI_coefficient_claimed") is False,
        "no two-loop AWI claim",
    )
    expect(
        source.get("comparison_target_used") is False,
        "no comparison target in overall-K",
    )

    expect(
        audit.get("schema") == "step6.overall_k_map.audit.v1", "overall-K audit schema"
    )
    expect(audit.get("status") == "PASS", "overall-K audit status")
    expect(audit.get("passed") == 14, "overall-K audit passed count")
    expect(audit.get("failed") == 0, "overall-K audit failed count")
    expect(all(audit.get("checks", {}).values()), "overall-K checks")
    expect(
        audit.get("external_or_holomorphic_input_used") is False,
        "overall-K external input boundary",
    )
    expected_audit_counts = {
        "source_rows": 483_685,
        "forest_events": 1_206_389,
        "forest_templates": 320_327,
        "unique_overall_K_templates": 583,
        "combined_normalized_term_instances": 8_370_830,
        "unresolved_tensor_count": 0,
        "unresolved_integral_count": 0,
    }
    expect(audit.get("counts") == expected_audit_counts, "overall-K audit counts")
    return {
        "graph_id": scope["graph_id"],
        "counts": counts,
        "audit_counts": expected_audit_counts,
    }


def _validate_measure(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.preaggregation_raw_replay_seed.audit.v2",
        "measure schema",
    )
    expect(
        source.get("status")
        == "PASS_PREAGGREGATION_REPLAY_SEED__MEASURE_TAGGED_CONVOLUTION_OPEN",
        "measure status",
    )
    expect(source.get("all_checks_passed") is True, "measure all checks")
    expect(all(source.get("checks", {}).values()), "measure checks")
    expect(
        source.get("open_missing_type_id")
        == "MISSING_TYPE::MeasureTaggedDeltaConvolutionBeforeContactAggregation",
        "measure open missing type",
    )
    expect(
        source.get("resolved_seed_type_id")
        == "TYPE::PreAggregationRawReplaySeedWithBareDeltaIdentity",
        "measure resolved replay seed type",
    )
    expected_counts = {
        "delta_entries_per_order": 256,
        "raw_histories": 216,
        "source_rows": 6,
        "unaggregated_pairs": 768,
    }
    expect(source.get("counts") == expected_counts, "measure counts")
    return {
        "counts": expected_counts,
        "resolved_seed": "PreAggregationRawReplaySeedWithBareDeltaIdentity",
        "open_missing_type": "MeasureTaggedDeltaConvolutionBeforeContactAggregation",
    }


def _validate_odd_word_sign(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.odd_word_transfer_sign.audit.v2",
        "odd-word sign schema",
    )
    expect(
        source.get("status") == "PASS_EXACT_ARBITRARY_ODD_WORD_EVENT_LEDGER",
        "odd-word sign status",
    )
    expect(source.get("all_checks_passed") is True, "odd-word sign all checks")
    checks = source.get("checks", {})
    expect(all(checks.values()), "odd-word sign checks")
    expect(
        checks.get("all_five_event_categories_separate") is True,
        "odd-word five sign categories",
    )
    expect(
        checks.get("exhaustive_sign_replay_exact") is True, "odd-word exhaustive replay"
    )
    expect(
        checks.get("ibp_reversal_payload_boundary_derived") is True,
        "odd-word boundary derivation",
    )
    expected_counts = {
        "boundary_payload_cases": 34,
        "exhaustive_cases": 10_922,
        "maximum_exhaustive_word_length": 6,
    }
    expect(source.get("counts") == expected_counts, "odd-word sign counts")
    return {
        "exhaustive_cases": 10_922,
        "maximum_exhaustive_word_length": 6,
        "boundary_payload_cases": 34,
        "maximum_boundary_word_length": 16,
        "payload_parities": [0, 1],
    }


def _validate_contact_provenance(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.primitive_contact_provenance_audit.audit.v1",
        "contact-provenance schema",
    )
    expect(
        source.get("status") == "FAIL_CLOSED_608_PRE_DISTRIBUTION_PROVENANCE_ABSENT",
        "contact-provenance status",
    )
    expect(source.get("all_checks_passed") is True, "contact-provenance all checks")
    checks = source.get("checks", {})
    expect(all(checks.values()), "contact-provenance checks")
    expect(
        checks.get("contact_catalog_is_postaggregation_shape") is True,
        "contact postaggregation shape",
    )
    expect(
        checks.get("required_pre_distribution_provenance_absent") is True,
        "contact missing provenance",
    )
    expect(
        checks.get("no_608_mapping_invented") is True, "contact no invented 608 mapping"
    )
    expect(checks.get("missing_type_remains_open") is True, "contact missing type open")
    expected_counts = {
        "contacts_with_complete_pre_distribution_provenance": 0,
        "earliest_raw_histories": 216,
        "earliest_unaggregated_pairs": 768,
        "stored_contacts": 608,
    }
    expect(source.get("counts") == expected_counts, "contact-provenance counts")
    expect(
        source.get("earliest_exact_type_id")
        == "TYPE::PreAggregationRawReplaySeedWithBareDeltaIdentity",
        "contact earliest exact type",
    )
    expect(
        source.get("open_missing_type_id")
        == "MISSING_TYPE::MeasureTaggedDeltaConvolutionBeforeContactAggregation",
        "contact open missing type",
    )
    return {
        "stored_contacts": 608,
        "complete_pre_distribution_provenance": 0,
        "unaggregated_pairs": 768,
        "mapping_status": "FAIL_CLOSED",
    }


def _validate_physical_sd(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.physical_sd_full_orbit.v1.audit",
        "physical-SD schema",
    )
    expect(
        source.get("verification_status") == "PASS", "physical-SD verification status"
    )
    expect(
        source.get("physics_status") == "BLOCKED_TYPED_LOCAL_AST_CLOSURE",
        "physical-SD physics status",
    )
    expect(source.get("failed") == 0, "physical-SD failed count")
    census = source.get("census", {})
    expect(census.get("oriented_columns") == 96, "physical-SD oriented columns")
    expect(
        census.get("physical_local_coefficient_resolved_columns") == 0,
        "physical-SD resolved columns",
    )
    matrices = source.get("physical_coefficient_matrices", {})
    expect(
        matrices.get("status") == "BLOCKED_TYPED_LOCAL_AST_CLOSURE",
        "physical-SD matrix status",
    )
    expect(matrices.get("shape") == [22, 134], "physical-SD matrix shape")
    expect(matrices.get("M_C_sparse_entries") is None, "physical-SD M_C")
    expect(matrices.get("M_E_sparse_entries") is None, "physical-SD M_E")
    expect(matrices.get("equality") is None, "physical-SD equality")
    expect(matrices.get("rank") is None, "physical-SD rank")
    expected_types = [
        "MISSING_TYPE::EdgeCollapsedProjectKernelNormalForm",
        "MISSING_TYPE::GroupedEVIntoI2I3OrderedPortNormalForm",
        "MISSING_TYPE::HigherValenceOrderedEulerOccurrenceNormalForm",
        "MISSING_TYPE::InheritedContactVertexAST",
    ]
    expect(
        [
            row.get("type_id")
            for row in source.get("smallest_required_types_in_order", [])
        ]
        == expected_types,
        "physical-SD missing types",
    )
    return {
        "oriented_columns": 96,
        "resolved_columns": 0,
        "shape": [22, 134],
        "missing_types": expected_types,
    }


def _validate_descent(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.three_parent_open_raw_axis_circuit.audit.v1",
        "descent schema",
    )
    expect(
        source.get("status") == "PASS_THREE_PARENT_ALL_PARITY_OPEN_RAW_AXIS_CIRCUIT_IR",
        "descent status",
    )
    boundary = source.get("interpretation_boundary", {})
    expect(
        boundary.get("three_parent_raw_axis_polynomial_evaluated") is False,
        "raw-axis evaluation",
    )
    expect(
        boundary.get("three_parent_raw_axis_sum_identically_zero") is None,
        "raw-axis zero test",
    )
    expect(
        boundary.get("automatic_source_map_descent_proved") is False,
        "source-map descent",
    )
    expect(
        boundary.get("covariant_projection_performed") is False, "covariant projection"
    )
    expect(
        boundary.get("covariant_X_tensor_X_inferred") is False,
        "covariant X tensor X inference",
    )
    expect(boundary.get("Q2_bb_result") is None, "descent Q2 result")
    return {
        "automatic_source_map_descent_proved": False,
        "covariant_projection_performed": False,
    }


def _validate_laurent(source: Mapping[str, Any]) -> dict[str, Any]:
    expect(
        source.get("schema") == "step6.connected_scalar_laurent.v1", "Laurent schema"
    )
    expect(
        source.get("status")
        == "PASS_EXACT_ALL_92_CONNECTED_PINCHED_NUMERATOR_LAURENT_TARGETS",
        "Laurent status",
    )
    expect(
        source.get("external_result_used_as_input") is False,
        "Laurent external-result boundary",
    )
    expect(source.get("comparison_target_used") is False, "Laurent comparison boundary")
    fail_closed = source.get("fail_closed", {})
    expect(
        fail_closed.get("forest_combination") == "UNCOMPUTED",
        "forest combination status",
    )
    expect(fail_closed.get("KUV") == "UNCOMPUTED", "KUV status")
    expect(
        fail_closed.get("renormalized_two_loop_coefficient") == "UNCOMPUTED",
        "renormalized coefficient",
    )
    expect(fail_closed.get("AWI_coefficient") == "UNCOMPUTED", "AWI coefficient")
    return {"AWI_coefficient": "UNCOMPUTED"}


def validate_sources(sources: Mapping[str, Any]) -> dict[str, Any]:
    expect(set(sources) == set(SOURCE_PATHS), "source set")
    return {
        "schema": SCHEMA,
        "document_status": DOCUMENT_STATUS,
        "valence_families": _validate_valence(sources["valence"]),
        "six_parent": _validate_six_parent(sources["six_parent"]),
        "union": _validate_union(sources["union"]),
        "restricted_three": _validate_restricted_three(
            sources["restricted_three_result"], sources["restricted_three_audit"]
        ),
        "overall_k": _validate_overall_k(
            sources["overall_k"], sources["overall_k_audit"]
        ),
        "measure": _validate_measure(sources["measure"]),
        "odd_word_sign": _validate_odd_word_sign(sources["odd_word_sign"]),
        "contact_provenance": _validate_contact_provenance(
            sources["contact_provenance"]
        ),
        "physical_sd": _validate_physical_sd(sources["physical_sd"]),
        "descent": _validate_descent(sources["descent"]),
        "laurent": _validate_laurent(sources["laurent"]),
    }


def _tex_id(value: str) -> str:
    return r"\texttt{" + value.replace("_", r"\_") + "}"


def render_markdown(snapshot: Mapping[str, Any]) -> str:
    family_tex = r",\;".join(ANALYTIC_VALENCE_FAMILIES)
    class_rows = []
    for index, row in enumerate(snapshot["six_parent"]["classes"], start=1):
        hosts = row["external_hosts"]
        weight = row["weight"]
        weight_tex = (
            str(weight["numerator"])
            if weight["denominator"] == 1
            else rf"-\frac{{1}}{{{weight['denominator']}}}"
        )
        class_rows.append(
            rf"G_{{{index}}}&={_tex_id(row['graph_id'])},&"
            rf"(H_1,H_2)&=({hosts['p1']},{hosts['p2']}),&"
            rf"|\operatorname{{Aut}}G_{{{index}}}|&={row['automorphism_order']},&"
            rf"w_{{{index}}}&={weight_tex}"
        )
    class_table = (r" \\" + "\n").join(class_rows)

    old3 = r",\;".join(_tex_id(value) for value in snapshot["union"]["old3"])
    new3 = r",\;".join(_tex_id(value) for value in snapshot["union"]["new3"])
    missing_sd = (r" \\" + "\n").join(
        rf"\tau_{{{index}}}&={_tex_id(type_id)}"
        for index, type_id in enumerate(
            snapshot["physical_sd"]["missing_types"], start=1
        )
    )

    return rf"""# Step 6 — verified foundations: partial mirror

$$
\mathrm{{DocumentStatus}}=\texttt{{UNMERGED\_PROPOSAL}}.
$$

## 1. Notation

$$
I_m:=\text{{insertion of total valence }}m,
\qquad
S_r:=\text{{action vertex of valence }}r,
\qquad
n_r:=N(S_r).
$$

$$
n_I:=\text{{insertion valence}},
\qquad
N_{{\mathrm{{int}}}}:=\text{{number of internal edges}},
\qquad
E:=2,
\qquad
V:=1+\sum_{{r\geq3}}n_r.
$$

$$
K:=\text{{UV-pole projector}},
\qquad
R'(G):=\Phi(G)+\sum_{{\gamma\subsetneq G}}C(\gamma)\Phi(G/\gamma),
\qquad
L_P:=\log\frac{{4\pi\mu^2}}{{(p_1+p_2)^2}}-\gamma_E.
$$

$$
\Phi(G):=\text{{bare amplitude of }}G,
\qquad
C(\gamma):=\text{{local counterterm of }}\gamma,
\qquad
w_j:=\frac{{\text{{signed decorated occurrence}}}}{{|\operatorname{{Aut}}G_j|}}.
$$

$$
m:=|\mathcal W_D|,
\qquad
|F|\in\{{0,1\}}:=\text{{payload parity}},
\qquad
N_{{\mathrm{{coeff}}}}:=\text{{odd-coefficient crossings}},
\qquad
N_{{\mathrm{{endpoint}}}}:=\text{{endpoint transfers}}.
$$

## 2. Two-loop valence closure

$$
n_I+\sum_{{r\geq3}}rn_r=2N_{{\mathrm{{int}}}}+E
=2N_{{\mathrm{{int}}}}+2.
$$

$$
L=N_{{\mathrm{{int}}}}-V+1=2
\quad\Longrightarrow\quad
N_{{\mathrm{{int}}}}=2+\sum_{{r\geq3}}n_r.
$$

$$
n_I+\sum_{{r\geq3}}rn_r
=2\left(2+\sum_{{r\geq3}}n_r\right)+2
\quad\Longrightarrow\quad
\boxed{{(n_I-2)+\sum_{{r\geq3}}(r-2)n_r=4}}.
$$

$$
\mathcal F_{{L=2}}=\left\{{{family_tex}\right\}},
\qquad
|\mathcal F_{{L=2}}|=12.
$$

$$
\forall F\in\mathcal F_{{L=2}}:\qquad
F=\texttt{{VALENCE\_NOT\_GRAPH}},
\qquad
F\notin\mathrm{{GraphIR}}.
$$

$$
F=\texttt{{VALENCE\_NOT\_GRAPH}}
\quad\not\Longrightarrow\quad
N_{{\mathrm{{instantiated\ GraphIR}}}}(F)=0.
$$

## 3. Background-labelled K4-e parents

$$
\begin{{aligned}}
{class_table}
\end{{aligned}}
$$

$$
N_{{K_4-e}}=6,
\qquad
(w_1,w_2,w_3,w_4,w_5,w_6)=\left(-1,-1,-\frac12,-1,-\frac12,-\frac12\right).
$$

## 4. Restricted-three evaluator; six-parent boundary

$$
\mathcal U_6:=\bigoplus_{{j=1}}^6\mathfrak A(G_j),
\qquad
N_{{\mathrm{{structural}}}}=3,
\qquad
N_{{\mathrm{{fail\mbox{{-}}closed}}}}=3,
\qquad
N_{{\mathrm{{bounded\ materialized}}}}=3.
$$

$$
\mathcal U_{{\mathrm{{old}}}}=\left\{{{old3}\right\}},
\qquad
\mathcal U_{{\mathrm{{new}}}}=\left\{{{new3}\right\}}.
$$

$$
\mathrm{{Parents}}_{{\mathrm{{evaluated}}}}=\frac36,
\qquad
\mathrm{{Sectors}}_{{\mathrm{{completed}}}}=\frac{{40}}{{40}},
\qquad
\mathrm{{Status}}_{{\mathrm{{restricted\ three}}}}
=\texttt{{PASS\_SECTOR\_SHARDED\_RESTRICTED\_THREE\_EVALUATION}}.
$$

$$
N_{{\mathrm{{input\ sparse\ rows}}}}=351\,069,
\qquad
N_{{\mathrm{{output\ sparse\ rows}}}}=55\,518,
\qquad
N_{{\mathrm{{output\ terms}}}}=350\,945.
$$

$$
\mathrm{{GlobalDAGRegistryConstructed}}=\texttt{{FALSE}},
\qquad
\mathrm{{PolyExteriorSemanticExpansion}}=\texttt{{NOT\_RUN}}.
$$

$$
\mathrm{{RestrictedThreeResult}}
\not\Longrightarrow
\mathrm{{Full}}\;K_4-e,
\qquad
\mathrm{{RestrictedThreeResult}}
\not\Longrightarrow
Q_2(bb).
$$

$$
\mathrm{{SixParentSemanticUnion}}
=\texttt{{OPEN: FAIL\_CLOSED\_NEW3\_DALGEBRA\_OPEN\_AXIS\_EVALUATOR\_ABSENT}}.
$$

## 5. Direct B2 overall-K certificate

$$
G_{{B_2}}={_tex_id(snapshot["overall_k"]["graph_id"])},
\qquad
P+p_1+p_2=0,
\qquad
P=-p_1-p_2.
$$

$$
K R'(G_{{B_2}})
\in
\bigl(\mathrm{{source}}_{{Q(i)}}A_0^2h^3\bigr)
\left[
\epsilon^{{-2}}\mathcal M_{{-2,0}}
+\epsilon^{{-1}}L_P\mathcal M_{{-1,1}}
+\epsilon^{{-1}}\mathcal M_{{-1,0}}
\right].
$$

$$
N(\mathcal M_{{-2,0}})=3\,035\,883,
\qquad
N(\mathcal M_{{-1,1}})=0,
\qquad
N(\mathcal M_{{-1,0}})=5\,334\,947.
$$

$$
\boxed{{\left[K R'(G_{{B_2}})\right]_{{\epsilon^{{-1}}L_P}}=0}}.
$$

$$
N_{{\mathrm{{source\ rows}}}}=483\,685,
\quad
N_{{\mathrm{{forest\ events}}}}=1\,206\,389,
\quad
N_{{\mathrm{{forest\ templates}}}}=320\,327,
\quad
N_{{\mathrm{{overall\mbox{{-}}K\ templates}}}}=583.
$$

## 6. Full gate census

$$
N_V=273,
\qquad
N_{{V,\mathrm{{self\mbox{{-}}loop}}}}=178,
\qquad
N_{{V\setminus K_4-e}}=267,
\qquad
N_{{\mathrm{{FP}}}}=10,
\qquad
N_{{\mathrm{{matter}}}}=12.
$$

$$
\left.\mathrm{{NK}}\right|_{{\mathrm{{reference\mbox{{-}}flat\ fixed\ gauge}}}}
=\texttt{{PROVED\_ABSENT\_AT\_THIS\_ORDER}},
\qquad
\mathrm{{FullVector+FP+MatterCompletion}}=\texttt{{OPEN}}.
$$

## 7. Measure-tagged convolution

$$
N_{{\Delta/\mathrm{{order}}}}=256,
\qquad
N_{{\mathrm{{raw\ histories}}}}=216,
\qquad
N_{{\mathrm{{source\ rows}}}}=6,
\qquad
N_{{\mathrm{{unaggregated\ pairs}}}}=768.
$$

$$
\mathrm{{PreAggregationRawReplaySeedWithBareDeltaIdentity}}
=\texttt{{RESOLVED: PASS\_EXACT\_REPLAY\_SEED}}.
$$

$$
\mathrm{{MeasureTaggedDeltaConvolutionBeforeContactAggregation}}
=\texttt{{OPEN: MISSING\_TYPE}}.
$$

## 8. Primitive-contact provenance

$$
N_{{\mathrm{{stored\ contacts}}}}=608,
\qquad
N_{{\mathrm{{complete\ pre\mbox{{-}}distribution\ provenance}}}}=0,
\qquad
N_{{\mathrm{{unaggregated\ pairs}}}}=768.
$$

$$
\mathrm{{ProvenanceMap}}_{{768\to608}}=\texttt{{FAIL\_CLOSED}},
\qquad
\mathrm{{MeasureTaggedDeltaConvolutionBeforeContactAggregation}}
=\texttt{{OPEN: MISSING\_TYPE}}.
$$

## 9. Odd-word transfer sign

$$
N=m+\binom{{m}}{{2}}+m|F|+N_{{\mathrm{{coeff}}}}+N_{{\mathrm{{endpoint}}}},
\qquad
\boxed{{s=(-1)^N}}.
$$

$$
|F|\in\{{0,1\}},
\qquad
0\leq m\leq6,
\qquad
N_{{\mathrm{{exhaustive}}}}=10\,922,
\qquad
\mathrm{{Status}}=\texttt{{PASS}}.
$$

$$
|F|\in\{{0,1\}},
\qquad
0\leq m\leq16,
\qquad
N_{{\mathrm{{boundary}}}}=2(17)=34.
$$

## 10. Frozen full-orbit Schwinger–Dyson snapshot

$$
\mathrm{{Snapshot}}=\texttt{{FROZEN\_FULL\_ORBIT\_AUDIT}},
\qquad
\mathrm{{NewestPerCutFrontier}}=\texttt{{NOT\_REPRESENTED\_HERE}}.
$$

$$
N_{{\mathrm{{oriented\ columns}}}}=96,
\qquad
N_{{\mathrm{{resolved\ physical\ coefficients}}}}=0,
\qquad
\dim M_C=\dim M_E=22\times134.
$$

$$
\mathrm{{PhysicalSDCoefficients}}=\texttt{{OPEN: BLOCKED\_TYPED\_LOCAL\_AST\_CLOSURE}}.
$$

$$
\begin{{aligned}}
{missing_sd}
\end{{aligned}}
$$

## 11. Covariant descent and coefficient boundary

$$
\mathrm{{AutomaticSourceMapDescent}}=\texttt{{OPEN}},
\qquad
\mathrm{{CovariantProjection}}=\texttt{{OPEN}},
\qquad
\mathrm{{Covariant}}\;X\otimes X=\texttt{{NOT\_INFERRED}}.
$$

$$
R=\texttt{{INCOMPLETE}},
\qquad
\mathrm{{ParentUnion}}=\texttt{{INCOMPLETE}},
\qquad
\boxed{{C_{{\mathrm{{AWI}}}}^{{(2)}}=\texttt{{UNCOMPUTED}}}}.
$$
"""


def build_audit(
    snapshot: Mapping[str, Any], markdown: str, hashes: Mapping[str, str]
) -> dict[str, Any]:
    checks = {
        "document_marked_unmerged_proposal": "UNMERGED\\_PROPOSAL" in markdown,
        "half_edge_and_euler_derivation_rendered": "n_I+\\sum_{r\\geq3}rn_r=2N_{\\mathrm{int}}+E"
        in markdown
        and "L=N_{\\mathrm{int}}-V+1=2" in markdown,
        "exact_two_loop_valence_identity_rendered": "(n_I-2)+\\sum_{r\\geq3}(r-2)n_r=4"
        in markdown,
        "all_twelve_analytic_valence_families_rendered": all(
            value in markdown for value in ANALYTIC_VALENCE_FAMILIES
        ),
        "valence_family_not_misidentified_as_empty_GraphIR": "\\mathfrak G(F)=\\varnothing"
        not in markdown
        and "\\not\\Longrightarrow" in markdown,
        "six_exact_K4e_weights_rendered": "\\left(-1,-1,-\\frac12,-1,-\\frac12,-\\frac12\\right)"
        in markdown,
        "restricted_three_of_six_boundary_rendered": "N_{\\mathrm{structural}}=3"
        in markdown
        and "N_{\\mathrm{fail\\mbox{-}closed}}=3" in markdown,
        "restricted_three_exact_evaluator_evidence_rendered": "\\frac36" in markdown
        and "\\frac{40}{40}" in markdown
        and "351\\,069" in markdown
        and "55\\,518" in markdown
        and "350\\,945" in markdown,
        "restricted_three_global_semantic_gate_not_run": "GlobalDAGRegistryConstructed"
        in markdown
        and "PolyExteriorSemanticExpansion" in markdown,
        "direct_B2_overall_K_log_pole_zero_rendered": "[K R'(G_{B_2})\\right]_{\\epsilon^{-1}L_P}=0"
        in markdown,
        "full_gate_counts_rendered": "N_V=273" in markdown
        and "N_{\\mathrm{FP}}=10" in markdown
        and "N_{\\mathrm{matter}}=12" in markdown,
        "preaggregation_replay_seed_resolved_convolution_open": "PreAggregationRawReplaySeedWithBareDeltaIdentity"
        in markdown
        and "MeasureTaggedDeltaConvolutionBeforeContactAggregation" in markdown
        and "OPEN: MISSING\\_TYPE" in markdown,
        "primitive_contact_provenance_fail_closed": "N_{\\mathrm{stored\\ contacts}}=608"
        in markdown
        and "N_{\\mathrm{complete\\ pre\\mbox{-}distribution\\ provenance}}=0"
        in markdown
        and "\\mathrm{ProvenanceMap}_{768\\to608}=\\texttt{FAIL\\_CLOSED}" in markdown,
        "odd_word_sign_formula_exact": "N=m+\\binom{m}{2}+m|F|+N_{\\mathrm{coeff}}+N_{\\mathrm{endpoint}}"
        in markdown
        and "s=(-1)^N" in markdown,
        "odd_word_exhaustive_and_boundary_counts_exact": "N_{\\mathrm{exhaustive}}=10\\,922"
        in markdown
        and "N_{\\mathrm{boundary}}=2(17)=34" in markdown,
        "physical_SD_coefficients_open": "PhysicalSDCoefficients" in markdown
        and "BLOCKED\\_TYPED\\_LOCAL\\_AST\\_CLOSURE" in markdown,
        "physical_SD_snapshot_scoped_as_frozen": "FROZEN\\_FULL\\_ORBIT\\_AUDIT"
        in markdown
        and "NewestPerCutFrontier" in markdown,
        "NK_absence_scoped_to_reference_flat_fixed_gauge": "reference\\mbox{-}flat\\ fixed\\ gauge"
        in markdown,
        "covariant_descent_open": "AutomaticSourceMapDescent" in markdown
        and "CovariantProjection" in markdown,
        "AWI_coefficient_uncomputed": "C_{\\mathrm{AWI}}^{(2)}=\\texttt{UNCOMPUTED}"
        in markdown,
        "headings_contain_no_inline_TeX": all(
            "$" not in line for line in markdown.splitlines() if line.startswith("#")
        ),
        "no_external_result_or_comparison_content": all(
            token not in markdown for token in ("GPT", "arXiv", "comparison target")
        ),
    }
    expect(all(checks.values()), "rendered partial-mirror checks")
    audit: dict[str, Any] = {
        "schema": AUDIT_SCHEMA,
        "status": "PASS",
        "authority_role": DOCUMENT_STATUS,
        "checks": checks,
        "passed": len(checks),
        "failed": 0,
        "source_sha256": dict(hashes),
        "snapshot_sha256": payload_sha256(snapshot),
        "output": str(OUTPUT),
        "output_sha256": sha256(markdown.encode("utf-8")).hexdigest(),
        "counts": {
            "valence_families": 12,
            "K4e_parents": 6,
            "structurally_compiled_parents": 3,
            "fail_closed_parents": 3,
            "restricted_three_completed_sectors": 40,
            "restricted_three_input_sparse_rows": 351_069,
            "restricted_three_output_sparse_rows": 55_518,
            "restricted_three_output_terms": 350_945,
            "odd_word_exhaustive_cases": 10_922,
            "odd_word_boundary_cases": 34,
            "stored_contacts": 608,
            "contacts_with_complete_pre_distribution_provenance": 0,
            "pure_vector_gate_graphs": 273,
            "FP_candidates": 10,
            "matter_candidates": 12,
            "physical_SD_resolved_coefficients": 0,
        },
        "external_result_used_as_input": False,
        "comparison_target_used": False,
    }
    audit["audit_sha256"] = payload_sha256(audit)
    return audit


def generate(root: Path = ROOT, write: bool = True) -> tuple[str, dict[str, Any]]:
    sources = load_sources(root)
    snapshot = validate_sources(sources)
    markdown = render_markdown(snapshot)
    hashes = source_hashes(root)
    audit = build_audit(snapshot, markdown, hashes)
    if write:
        output_path = root / OUTPUT
        audit_path = root / AUDIT
        output_path.parent.mkdir(parents=True, exist_ok=True)
        audit_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        audit_path.write_text(
            json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return markdown, audit


if __name__ == "__main__":
    generate()
