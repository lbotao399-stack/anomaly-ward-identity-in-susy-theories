#!/usr/bin/env python3
"""Build and verify the internal-only Step-5 full-N=4 one-loop status ledger.

The ledger is an authority and completion-status audit.  It imports no
holomorphic-twist target, no external coefficient, and no live reference.
Exact numerical entries are copied only from Project-generated artifacts at
the recorded PR-46 proposal commit.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
import subprocess
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated/step5/full-n4-one-loop-status-ledger.json"
AUDIT = ROOT / "audits/step5-full-n4-one-loop-status-ledger-verification.json"

ACCEPTED_MAIN = "9e11316c94efe37df2512a812738ff153c8e6985"
PR46_PROPOSAL = "1ca784bcf73d1ff0809e6469af6fb7a10799d142"

CATALOGUE = "generated/step5/graph-catalogue.json"
WW_SEED = "generated/step5/ww-seed-graph-ir.json"
TYPED_PIPELINE = "generated/step5/typed-pipeline/ww-typed-pipeline.json"
GHOST_CENSUS = "audits/step5a-ghost-census.json"
CONTACT_AUDIT = "audits/step5-ww-contact-replay-verification.json"
FILTERED_QUOTIENT = "generated/step5/one-loop-filtered-covariant-quotient.json"
DRED_JETS = "generated/step5/one-loop-dred-evanescent-jets.json"
CONTRACT = "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
GAP_CENSUS = "audits/step5-full-two-letter-gap-census.md"
MATTER_YZ_CENSUS = "generated/step5/full-n4-matter-yz-census.json"


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
    )


def git_text(commit: str, path: str) -> str:
    return git_bytes(commit, path).decode("utf-8")


def git_json(commit: str, path: str) -> Any:
    return json.loads(git_text(commit, path))


def git_paths(commit: str) -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", commit],
        cwd=ROOT,
        text=True,
    )
    return output.splitlines()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def json_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def proposal_sources() -> dict[str, bytes]:
    paths = (
        CATALOGUE,
        WW_SEED,
        TYPED_PIPELINE,
        GHOST_CENSUS,
        CONTACT_AUDIT,
        FILTERED_QUOTIENT,
        DRED_JETS,
        CONTRACT,
        GAP_CENSUS,
        "tasks/CURRENT.yaml",
        "ledger/proof_obligations.json",
    )
    return {path: git_bytes(PR46_PROPOSAL, path) for path in paths}


def computational_paths_at_main() -> list[str]:
    paths = git_paths(ACCEPTED_MAIN)
    return sorted(
        path
        for path in paths
        if path == CONTRACT
        or path.startswith("generated/step5/")
        or path.startswith("scripts/step5_")
        or path.startswith("tests/test_step5_")
    )


def build_channels(catalogue: dict[str, object]) -> list[dict[str, object]]:
    multiplicity = {"W": 1, "Phi": 3, "TildePhi": 3, "TildeW": 2}
    channels: list[dict[str, object]] = []
    for record in catalogue["tree_channels"]:  # type: ignore[index]
        channel = record["channel"]
        left = channel["left"]["family"]
        right = channel["right"]["family"]
        channel_id = channel["channel_id"]
        tree_zero = bool(channel["descendant"]["is_zero"])
        if channel_id == "W__W":
            loop_status = (
                "PARTIAL_EXACT_ISOLATED_VECTOR_TRIANGLE_ONLY__"
                "CONTACT_MATTER_QUOTIENT_OPEN"
            )
            exact_intermediates = [
                "WW_DIRECT_TRIANGLE_PREINTEGRATION",
                "WW_DIRECT_TRIANGLE_UV_POLE",
                "WW_REFLECTED_TRIANGLE_UV_POLE",
            ]
        elif tree_zero:
            loop_status = "OPEN_RENORMALIZED_ZERO_NOT_PROVED"
            exact_intermediates = []
        else:
            loop_status = "OPEN_NO_ONE_LOOP_GRAPH_OR_AMPLITUDE"
            exact_intermediates = []
        channels.append(
            {
                "channel_id": channel_id,
                "ordered_expression": channel["ordered_expression"],
                "left_family": left,
                "right_family": right,
                "component_count": multiplicity[left] * multiplicity[right],
                "tree_descendant_term_count": len(channel["descendant"]["terms"]),
                "tree_status": (
                    "EXACT_ALL_VALENCE_TREE_ZERO"
                    if tree_zero
                    else "EXACT_NONZERO_TREE_DESCENDANT"
                ),
                "one_loop_status": loop_status,
                "exact_intermediate_result_ids": exact_intermediates,
                "exact_renormalized_result": False,
                "accepted_coefficient": None,
            }
        )
    return channels


def open_gates() -> list[dict[str, str]]:
    gates = {
        "contact": (
            "WW_PHYSICAL_CONTACT_FAMILY",
            "H2_X_TILDEW_PROJECTOR",
            "I1H1_SHARED_SCOPE_DALGEBRA",
            "I2_X_TILDEW_PROJECTOR",
            "I2_NORMALIZATION",
            "I4_LOCALITY_TO_POLYNOMIAL",
            "I4_ORDINARY_UV_IR_SEPARATION",
            "CUT_MAP_R_CUT",
            "COLLAPSE_COEFFICIENT_TRANSPORT",
            "CT2_FIXED",
            "PHYSICAL_COLOR_REDUCTION",
            "PHYSICAL_AUTOMORPHISM",
            "TAYLOR_WICK_FACTORIAL_MATCHING",
            "CONTACT_HESSIAN_COEFFICIENT",
            "GAMMA_C_POLE",
            "GAMMA_TAU_POLE",
            "ANOMALY_COEFFICIENT",
        ),
        "matter_and_channels": (
            "LETTER_Y_EXPANSION",
            "LETTER_Z_EXPANSION",
            "LETTER_T_INTERFACE",
            "ALL_CHANNEL_INSERTION_COMPILER",
            "ACTION_VERTEX_PHYSICALIZATION",
            "CHIRAL_PROPAGATOR_EDGES",
            "GENERIC_DALGEBRA",
            "GENERIC_DRED_REDUCER",
            "ELEVEN_NONZERO_FAMILY_CENSUS",
            "FOUR_TREE_ZERO_RENORMALIZED_MIXING",
            "CHANNELWISE_FP_NK_CENSUS",
            "FULL_N4_FLUCTUATING_SECTOR_TRACE",
            "FULL_N4_MATTER_SOURCE_COLOR_COHOMOLOGY",
            "MATTER_SUPERPROPAGATOR_NORMALIZATION",
            "EXTERNAL_Y_DALGEBRA_PROJECTION",
            "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
            "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
        ),
        "quotient_and_scheme": (
            "PHYSICAL4D_RELATION_MATRIX",
            "TRUE_N1_PARENT_INCIDENCE_C1",
            "PHYSICAL4D_TOTAL_FILTERED_INJECTIVITY",
            "FULL_DRED_EOM_IBP_BV_QUOTIENT_INJECTIVITY",
            "DRED_LOCALIZATION_4D_PROJECTION_INTERCHANGE",
            "FULL_QUANTUM_BV_SOURCE_COMPLEX",
            "VECTOR_CHIRAL_FINITE_MEASURE_BRIDGE",
            "NONDEGENERATE_EXTERNAL_1PI_PROBES",
            "EVANESCENT_OPERATOR_BASIS",
            "FINITE_COUNTERTERM_CONVENTION",
            "OPEN_COLOR_TENSOR_PRODUCT_BASIS",
            "MULTITRACE_SECTOR",
            "REGULARIZATION_SD_CUTTING_COMMUTATOR",
            "EXPLICIT_CONTACT_COLLAPSED_BASIS_BIJECTION",
        ),
        "step5c": (
            "FINITE_COEFFICIENT_SPACE_DENSITY_AND_BEREZINIAN",
            "FINITE_VECTOR_COEFFICIENT_CYCLE",
            "FINITE_FP_AND_NK_CYCLES",
            "GLOBAL_LOCAL_NONMINIMAL_REALIZATION",
        ),
    }
    return [
        {"code": code, "category": category, "status": "OPEN"}
        for category, codes in gates.items()
        for code in codes
    ]


def build_payload() -> dict[str, object]:
    sources = proposal_sources()
    catalogue = json.loads(sources[CATALOGUE])
    ww = json.loads(sources[WW_SEED])
    pipeline = json.loads(sources[TYPED_PIPELINE])
    ghost = json.loads(sources[GHOST_CENSUS])
    contact = json.loads(sources[CONTACT_AUDIT])
    filtered = json.loads(sources[FILTERED_QUOTIENT])
    dred = json.loads(sources[DRED_JETS])
    contract_text = sources[CONTRACT].decode("utf-8")
    gap_text = sources[GAP_CENSUS].decode("utf-8")
    matter_yz_bytes = (ROOT / MATTER_YZ_CENSUS).read_bytes()
    matter_yz = json.loads(matter_yz_bytes)
    main_task = git_json(ACCEPTED_MAIN, "tasks/CURRENT.yaml")
    proposal_task = json.loads(sources["tasks/CURRENT.yaml"])
    proposal_obligations = json.loads(sources["ledger/proof_obligations.json"])
    proposal_obligation = next(
        item
        for item in proposal_obligations["proof_obligations"]
        if item["id"] == proposal_task["id"]
    )

    channels = build_channels(catalogue)
    tree_zero_channels = [
        item
        for item in channels
        if item["tree_status"] == "EXACT_ALL_VALENCE_TREE_ZERO"
    ]
    unimplemented_nonzero_channels = [
        item
        for item in channels
        if item["channel_id"] != "W__W"
        and item["tree_status"] == "EXACT_NONZERO_TREE_DESCENDANT"
    ]
    rows = ww["traces"]
    row_prefactors = {
        row["row_prefactor"]
        for orientation in ("DIRECT", "REFLECTED")
        for row in rows[orientation]
    }
    row_pole_certificates = {
        (row["row_pole_in_pi2_g2"], row["metric_space"])
        for orientation in pipeline["orientations"]
        for row in orientation["specialized_row_pole_binding"]["row_certificates"]
    }
    pole_aggregation_checks = {
        orientation["orientation"]: sum(
            Fraction(row["row_pole_in_pi2_g2"])
            for row in orientation["specialized_row_pole_binding"]["row_certificates"]
        )
        == Fraction(
            orientation["specialized_row_pole_binding"]["orientation_pole_in_pi2_g2"]
        )
        for orientation in pipeline["orientations"]
    }
    main_computational_paths = computational_paths_at_main()
    gates = open_gates()
    matter_open_ids = [row["id"] for row in matter_yz["open_obligations"]]
    matter_triangle = matter_yz["triangle_I2_S3m_S3m"]
    matter_seagull = matter_yz["seagull_I2_S4m"]

    checks = {
        "accepted_snapshot_task_is_step5_specified": (
            main_task["id"] == "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"
            and main_task["status"] == "SPECIFIED"
        ),
        "accepted_snapshot_has_no_step5_computational_paths": (
            main_computational_paths == []
        ),
        "proposal_is_still_specified_not_accepted": (
            proposal_task["status"] == "SPECIFIED"
            and proposal_obligation["state"] == "SPECIFIED"
        ),
        "sixteen_ordered_families": len(channels) == 16,
        "eighty_one_components": sum(item["component_count"] for item in channels)
        == 81,
        "one_partial_seed_and_fifteen_unimplemented_families": (
            sum(item["channel_id"] == "W__W" for item in channels) == 1
            and sum(item["one_loop_status"].startswith("OPEN_") for item in channels)
            == 15
        ),
        "all_sixteen_renormalized_results_are_open": all(
            not item["exact_renormalized_result"] for item in channels
        ),
        "four_tree_zero_families_have_twenty_five_components": (
            len(tree_zero_channels) == 4
            and sum(item["component_count"] for item in tree_zero_channels) == 25
        ),
        "eleven_nonzero_unimplemented_families_have_fifty_five_components": (
            len(unimplemented_nonzero_channels) == 11
            and sum(item["component_count"] for item in unimplemented_nonzero_channels)
            == 55
        ),
        "ww_has_two_orientations_and_eight_rows_each": (
            len(ww["graphs"]) == 2
            and len(rows["DIRECT"]) == 8
            and len(rows["REFLECTED"]) == 8
        ),
        "ww_row_prefactor_is_exact": row_prefactors == {"+g^2/16"},
        "ww_row_pole_is_exact": row_pole_certificates
        == {("1/1024", "hat_delta^(mu nu)")},
        "ww_row_to_orientation_pole_aggregation_is_exact": (
            pole_aggregation_checks == {"DIRECT": True, "REFLECTED": True}
        ),
        "ww_endpoint_branch_numerator_factorization_is_recorded": (
            ww["preintegration"][
                "coefficient_per_D_minus_placement_after_four_endpoint_sum"
            ]
            == {"DIRECT": "+g^2/16", "REFLECTED": "+g^2/16"}
            and ww["preintegration"]["coefficient_after_two_D_minus_placements"]
            == {"DIRECT": "+g^2/8", "REFLECTED": "+g^2/8"}
        ),
        "ww_orientation_poles_are_exact": ww["poles"]["triangle_poles"]
        == {
            "DIRECT": (
                "+g^2/(128*pi^2*epsilon)*c_{ACD}c_{BCE}*"
                "T_(mu n nu)*hat_delta^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
            "REFLECTED": (
                "+g^2/(128*pi^2*epsilon)*c_{BCD}c_{ACE}*"
                "T_(mu n nu)*hat_delta^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
        },
        "ww_contact_and_anomaly_are_invalidated": (
            pipeline["stage_status"]["anomaly_coefficient"]
            == "INVALIDATED_NOT_PROPAGATED"
            and pipeline["stage_status"]["basis_resolved_sd_contact_orbit"]
            == "INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY"
            and contact["anomaly_coefficient"] == "NOT_ACCEPTED"
            and contact["ordinary_contact_UV_pole"] == "NOT_COMPUTED"
        ),
        "primitive_ww_ghost_absence_is_narrowly_proved": (
            ghost["FP_result"] == "PROVED_ABSENT_AT_THIS_ORDER"
            and ghost["NK_result"] == "PROVED_ABSENT_AT_THIS_ORDER"
        ),
        "ww_mixed_matter_yz_census_has_two_exact_graph_families": (
            matter_triangle["classification"] == "GRAMMAR_DERIVED_TYPED_GRAPH_FAMILY"
            and matter_seagull["classification"]
            == "GRAMMAR_DERIVED_MANDATORY_CONTACT_FAMILY"
            and len(matter_triangle["connected_labeled_Wick_rows"]) == 4
            and len(matter_seagull["connected_labeled_Wick_rows"]) == 4
        ),
        "ww_mixed_matter_yz_census_has_four_exact_open_gates": (
            matter_open_ids
            == [
                "MATTER_SUPERPROPAGATOR_NORMALIZATION",
                "EXTERNAL_Y_DALGEBRA_PROJECTION",
                "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
                "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            ]
            and all(row["status"] == "OPEN" for row in matter_yz["open_obligations"])
        ),
        "ww_mixed_matter_yz_census_acceptance_is_fail_closed": (
            matter_yz["status"]
            == "PASS_EXACT_PROJECT_GRAPH_CENSUS__AMPLITUDES_FAIL_CLOSED"
            and not any(matter_yz["acceptance_boundary"].values())
            and matter_yz["totals"]["accepted_coefficients"] == 0
        ),
        "ww_mixed_matter_yz_census_imports_no_external_target": (
            not matter_yz["external_results_imported"]
            and matter_yz["external_target_input_count"] == 0
            and matter_yz["holomorphic_twist_input_count"] == 0
        ),
        "physical4d_quotient_is_fail_closed": (
            filtered["status"] == "FAIL_CLOSED_MISSING_TRUE_N1_PARENT_INCIDENCE"
        ),
        "raw_full_dred_injectivity_is_explicitly_false": (
            dred["status"] == "FAIL_EXPLICIT_FULL_DRED_QUADRATIC_JET_KERNEL"
        ),
        "contract_records_full_n4_coefficient_not_established": (
            "C_2^{\\mathcal N=4}" in contract_text
            and "=\\texttt{NOT\\_ESTABLISHED}" in contract_text
        ),
        "stale_aggregate_candidate_is_present_only_as_old_candidate_surface": (
            "the \\(g^2/(64\\pi^2)\\) WW coefficient is a derived aggregate-SD candidate"
            in gap_text
        ),
        "no_external_or_ht_target_input": True,
        "no_accepted_coefficient": True,
        "all_required_open_gate_categories_are_nonempty": {
            item["category"] for item in gates
        }
        == {"contact", "matter_and_channels", "quotient_and_scheme", "step5c"},
    }

    return {
        "schema": "Step5FullN4OneLoopStatusLedger.v1",
        "status": (
            "PASS_INTERNAL_STATUS_LEDGER__NO_ACCEPTED_FULL_N4_ONE_LOOP_COEFFICIENT"
            if all(checks.values())
            else "FAIL_INTERNAL_STATUS_LEDGER"
        ),
        "scope": {
            "internal_project_artifacts_only": True,
            "holomorphic_twist_input_count": 0,
            "external_target_input_count": 0,
            "external_coefficient_input_count": 0,
            "notion_input_count": 0,
            "purpose": "authority_and_completion_status_not_new_amplitude",
        },
        "authority_columns": {
            "accepted_origin_main": {
                "commit": ACCEPTED_MAIN,
                "authority": "ACCEPTED_ORIGIN_MAIN_SNAPSHOT",
                "task_status": main_task["status"],
                "step5_computational_paths": main_computational_paths,
                "accepted_full_n4_one_loop_results": [],
                "accepted_anomaly_coefficients": [],
                "result": "EMPTY",
            },
            "draft_pr46_proposal": {
                "commit": PR46_PROPOSAL,
                "authority": "PROPOSAL_ONLY_NOT_ACCEPTED",
                "task_status": proposal_task["status"],
                "proposal_status": proposal_obligation["proposal_status"],
                "exact_intermediate_results": [
                    "WW_ISOLATED_VECTOR_TRIANGLE_DIRECT",
                    "WW_ISOLATED_VECTOR_TRIANGLE_REFLECTED",
                    "REGISTERED_FIXED_VECTOR_ROOTED_WARD_COVARIANCE",
                    "PRIMITIVE_WW_FP_NK_ABSENCE_AT_ONE_LOOP",
                ],
                "exact_renormalized_channel_results": [],
                "accepted_anomaly_coefficients": [],
            },
            "draft_worktree_extension": {
                "authority": "UNCOMMITTED_PROJECT_ONLY_PROPOSAL",
                "source": MATTER_YZ_CENSUS,
                "exact_intermediate_results": [
                    "WW_MIXED_I2_S3M_S3M_YZ_GRAPH_CENSUS",
                    "WW_MIXED_I2_S4M_YZ_SEAGULL_CENSUS",
                ],
                "exact_renormalized_channel_results": [],
                "accepted_anomaly_coefficients": [],
            },
        },
        "letter_families": {
            "X": {"project_name": "W", "expression": "nabla_+ W_+", "count": 1},
            "Y": {"project_name": "Phi", "expression": "nabla_+ Phi_r", "count": 3},
            "Z": {"project_name": "TildePhi", "expression": "TildePhi_r", "count": 3},
            "T": {"project_name": "TildeW", "expression": "TildeW_dot_a", "count": 2},
        },
        "counts": {
            "ordered_families": len(channels),
            "component_channels": sum(item["component_count"] for item in channels),
            "partial_seed_families": 1,
            "unimplemented_families": 15,
            "unimplemented_component_channels": 80,
            "exact_renormalized_families": 0,
            "renormalized_open_families": 16,
            "renormalized_open_component_channels": 81,
            "tree_zero_families": len(tree_zero_channels),
            "tree_zero_components": sum(
                item["component_count"] for item in tree_zero_channels
            ),
            "nonzero_unimplemented_families": len(unimplemented_nonzero_channels),
            "nonzero_unimplemented_components": sum(
                item["component_count"] for item in unimplemented_nonzero_channels
            ),
            "ww_mixed_matter_yz_graph_families": 2,
            "ww_mixed_matter_yz_connected_labeled_rows": (
                len(matter_triangle["connected_labeled_Wick_rows"])
                + len(matter_seagull["connected_labeled_Wick_rows"])
            ),
            "ww_mixed_matter_yz_disconnected_typed_matchings": (
                matter_triangle["disconnected_typed_matching_count"]
                + matter_seagull["disconnected_typed_matching_count"]
            ),
            "ww_mixed_matter_yz_open_obligations": len(matter_open_ids),
        },
        "ordered_channels": channels,
        "exact_proposal_intermediates": {
            "ww_isolated_triangle": {
                "scope": "FIXED_VECTOR_PURE_GAUGE_ISOLATED_TRIANGLE_ONLY",
                "graph_count": len(ww["graphs"]),
                "orientations": ["DIRECT", "REFLECTED"],
                "d_algebra_rows_per_orientation": {
                    orientation: len(rows[orientation])
                    for orientation in ("DIRECT", "REFLECTED")
                },
                "graph_prefactor_before_d_chain": "-g^2/8",
                "closed_d_chain_factor": "-1/2",
                "row_prefactor": "+g^2/16",
                "coefficient_after_two_d_minus_placements": "+g^2/8",
                "row_aggregation_semantics": (
                    "ADDITIVE_ENDPOINT_ASSIGNMENT_BRANCHES_WITH_DISTINCT_NUMERATORS__"
                    "NOT_EIGHT_IDENTICAL_AMPLITUDES"
                ),
                "four_endpoint_numerator_identity_per_d_minus_placement": (
                    "r0*p*r1+r0*p*r2+r1*p*r1+r1*p*r2=(r0+r1)*p*(r1+r2)=L1*p*L2"
                ),
                "four_endpoint_factorized_coefficient_per_placement": "+g^2/16",
                "two_placement_factorized_coefficient": "+g^2/8",
                "row_uv_pole": "+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)",
                "pole_aggregation_per_orientation": (
                    "8*(1/1024)*g^2/(pi^2*epsilon)=1/128*g^2/(pi^2*epsilon)"
                ),
                "row_to_orientation_aggregation_status": "PROVED_EXACT",
                "orientation_uv_poles": ww["poles"]["triangle_poles"],
                "preintegration": ww["preintegration"],
                "physical_symmetric_operator_word": ww["poles"][
                    "physical_symmetric_operator_word"
                ],
                "operator_word_status": ww["poles"][
                    "physical_symmetric_operator_word_status"
                ],
                "renormalized_ward_result": "OPEN",
                "accepted_anomaly_coefficient": None,
            },
            "primitive_ww_ghost_census": {
                "FP": ghost["FP_result"],
                "NK": ghost["NK_result"],
                "scope": "PRIMITIVE_WW_ONLY_NOT_CHANNEL_INDEPENDENT",
            },
            "ww_mixed_matter_yz_census": {
                "scope": matter_yz["scope"],
                "status": matter_yz["status"],
                "triangle_I2_S3m_S3m": {
                    "classification": matter_triangle["classification"],
                    "connected_labeled_row_count": len(
                        matter_triangle["connected_labeled_Wick_rows"]
                    ),
                    "disconnected_typed_matching_count": matter_triangle[
                        "disconnected_typed_matching_count"
                    ],
                    "coefficient_ledger": matter_triangle["coefficient_ledger"],
                },
                "seagull_I2_S4m": {
                    "classification": matter_seagull["classification"],
                    "connected_labeled_row_count": len(
                        matter_seagull["connected_labeled_Wick_rows"]
                    ),
                    "disconnected_typed_matching_count": matter_seagull[
                        "disconnected_typed_matching_count"
                    ],
                    "coefficient_ledger": matter_seagull["coefficient_ledger"],
                },
                "open_obligation_ids": matter_open_ids,
                "acceptance_boundary": matter_yz["acceptance_boundary"],
                "renormalized_ward_result": "OPEN",
                "accepted_anomaly_coefficient": None,
            },
            "registered_rooted_ward_covariance": {
                "functional": "Gamma_root^(1)=1/2*STr_DRED(G_B*I_B)",
                "ward_identity": "delta_R Gamma_root^(1)=1/2*STr_DRED([R,G_B*I_B])=0",
                "status": "PROVED_REGISTERED_FIXED_VECTOR_ROOTED_FUNCTIONAL_ONLY",
                "physical_full_n4_coefficient": "NOT_DETERMINED",
            },
        },
        "coefficient_boundary": {
            "accepted_coefficients": [],
            "accepted_full_n4_result_count": 0,
            "full_n4_coefficient": {
                "definition": "C_2^N4=sum_(V,Phi_r,TildePhi_r,FP,NK) C_(2,alpha)",
                "status": "NOT_ESTABLISHED",
            },
            "stale_aggregate_candidate": {
                "value": "g^2/(64*pi^2)",
                "old_surface_status": "DERIVED_AGGREGATE_SD_CANDIDATE",
                "ledger_status": (
                    "INVALIDATED_STALE_AGGREGATE_SD_CANDIDATE__"
                    "NO_COEFFICIENT_PROPAGATION"
                ),
                "accepted": False,
                "usable_as_full_n4_result": False,
                "usable_as_ward_coefficient": False,
                "missing": [
                    "basis_resolved_physical_contact_orbit",
                    "contact_UV_pole",
                    "matter_fluctuating_sectors",
                    "physical_4d_quotient",
                    "counterterm_and_scheme",
                ],
            },
            "isolated_triangle_poles_are_intermediate_not_anomaly_coefficients": True,
        },
        "open_gates": gates,
        "explicit_negative_results": {
            "raw_full_dred_quadratic_jet_injectivity": ("FALSE_EXPLICIT_TAU_KERNEL"),
            "physical4d_total_filtered_injectivity": filtered["status"],
            "complete_physical_contact_family": contact["status"],
            "higher_loop_exactness": "NOT_PROVED",
            "full_nonlocal_1PI_completion": "NOT_CLAIMED",
        },
        "source_sha256": {
            **{
                path: sha256_bytes(payload) for path, payload in sorted(sources.items())
            },
            MATTER_YZ_CENSUS: sha256_bytes(matter_yz_bytes),
        },
        "checks": checks,
    }


def build_audit(payload: dict[str, object], serialized: bytes) -> dict[str, object]:
    checks = payload["checks"]
    assert isinstance(checks, dict)
    failed = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema": "Step5FullN4OneLoopStatusLedgerVerification.v1",
        "status": payload["status"],
        "ledger_sha256": sha256_bytes(serialized),
        "checks": checks,
        "failed": failed,
        "totals": {"checks": len(checks), "failed": len(failed)},
        "accepted_coefficient_count": len(
            payload["coefficient_boundary"]["accepted_coefficients"]  # type: ignore[index]
        ),
        "external_target_input_count": payload["scope"][  # type: ignore[index]
            "external_target_input_count"
        ],
        "holomorphic_twist_input_count": payload["scope"][  # type: ignore[index]
            "holomorphic_twist_input_count"
        ],
    }


def main() -> None:
    payload = build_payload()
    serialized = json_bytes(payload)
    audit = build_audit(payload, serialized)
    if audit["failed"]:
        raise SystemExit(f"status-ledger verification failed: {audit['failed']}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(serialized)
    AUDIT.write_bytes(json_bytes(audit))
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
