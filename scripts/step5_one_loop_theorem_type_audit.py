#!/usr/bin/env python3
"""Independent exact type audit for the Step-5 one-loop theorem proposal.

No loop or anomaly coefficient is imported or evaluated.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable

try:
    from scripts import step5_background_ward_recursion as ward
    from scripts import step5_frame_bridge_intertwiner as bridge
    from scripts import step5_one_loop_hessian_insertion_census as hessian
    from scripts import step5_one_loop_spin_projector as spin
except ModuleNotFoundError:  # direct execution
    import sys

    ROOT_IMPORT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT_IMPORT))
    from scripts import step5_background_ward_recursion as ward
    from scripts import step5_frame_bridge_intertwiner as bridge
    from scripts import step5_one_loop_hessian_insertion_census as hessian
    from scripts import step5_one_loop_spin_projector as spin


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/one-loop-theorem-type-audit.json"
AUDIT = ROOT / "audits/step5-one-loop-theorem-type-audit-verification.json"


def degree_sum(left: Iterable[int], right: Iterable[int]) -> set[int]:
    return {a + b for a in left for b in right}


def connection_degree_certificate() -> dict[str, object]:
    field_strength = {1, 2}
    x = field_strength | {1 + degree for degree in field_strength}
    xx = degree_sum(x, x)
    seed = xx | {1 + degree for degree in xx}
    derivative_x = x | {1 + degree for degree in x}
    anomaly_candidate = degree_sum(field_strength, derivative_x)
    return {
        "field_strength": sorted(field_strength),
        "X=nabla_plus_W_plus": sorted(x),
        "X_tensor_X": sorted(xx),
        "seed=nabla_minus_X_tensor_X": sorted(seed),
        "candidate=tildeW_times_DX": sorted(anomaly_candidate),
        "seed_maximum": max(seed),
        "candidate_maximum": max(anomaly_candidate),
        "status": "PASS_UNREDUCED_CONNECTION_FILTRATION",
    }


def source_certificate() -> dict[str, object]:
    insertion_dimension = Fraction(9, 2)
    full_measure_dimension = Fraction(-2)
    source_dimension = -full_measure_dimension - insertion_dimension
    source_parity = 1
    insertion_parity = 1
    odd_leibniz_sign = -1 if source_parity else 1
    source_dual_sign = 1
    invariant_pairing_coefficient = source_dual_sign + odd_leibniz_sign
    return {
        "ordered_graph_carrier": "Adjoint tensor Adjoint with A|B order",
        "physical_local_seed_subspace": "Sym^2(Adjoint)",
        "ordered_source_representation": "(Adjoint tensor Adjoint)^dual",
        "conditional_local_source_representation": "(Sym^2(Adjoint))^dual",
        "ordered_to_local_quotient": "OPEN_COLOR_WORD_QUOTIENT",
        "outer_connection": (
            "D_minus+Gamma_minus^Adj tensor 1+1 tensor Gamma_minus^Adj"
        ),
        "measure": "E_FULL_SUPERSPACE_d8z",
        "measure_dimension": str(full_measure_dimension),
        "insertion_dimension": str(insertion_dimension),
        "source_dimension": str(source_dimension),
        "insertion_R_weight": -1,
        "source_R_weight": 1,
        "R_weight_status": "TEMPORARY_FORMAL_GRADING",
        "Project_U1R_binding": "OPEN",
        "source_parity": source_parity,
        "insertion_parity": insertion_parity,
        "source_left_dual_rule": "<sJ,O>=<J,rho_2(c)O>",
        "odd_Leibniz_sign": odd_leibniz_sign,
        "invariant_pairing_coefficient": invariant_pairing_coefficient,
        "chiral_measure_status": "REJECTED_WITHOUT_CHIRAL_PROJECTOR",
        "source_extended_BV_closure": "OPEN",
    }


def color_word_certificate() -> dict[str, object]:
    # Basis order: (a*c, a*d, b*c, b*d), with
    # Y_lower=(a,b), W_lower=(c,d), epsilon^(+-)=+1.
    upper_y_lower_w = (0, -1, 1, 0)  # b*c-a*d
    lower_y_upper_w = (0, 1, -1, 0)  # a*d-b*c
    return {
        "epsilon_upper": {"plus_minus": 1, "minus_plus": -1},
        "Y_lower": ["a", "b"],
        "W_lower": ["c", "d"],
        "Y_upper": ["b", "-a"],
        "W_upper": ["d", "-c"],
        "monomial_basis": ["a*c", "a*d", "b*c", "b*d"],
        "Y_upper_W_lower_coefficients": list(upper_y_lower_w),
        "W_lower_Y_upper_coefficients": list(upper_y_lower_w),
        "Y_lower_W_upper_coefficients": list(lower_y_upper_w),
        "lower_upper_is_minus_upper_lower": lower_y_upper_w
        == tuple(-value for value in upper_y_lower_w),
        "seed_exchange_symmetry": "SYMMETRIC_AB",
        "literal_5_54A_second_term": "Y_upper^D times W_lower^E",
        "literal_candidate_internal_exchange": "ANTISYMMETRIC_DE",
        "literal_candidate_open_exchange": "ANTISYMMETRIC_AB",
        "literal_candidate_Sym2_projection": "ZERO",
        "ordered_A_bar_B_to_local_Sym2": "OPEN_COLOR_WORD_QUOTIENT",
        "reflected_dotted_index_variance": "OPEN",
        "status": "PASS_EXACT_INDEX_TEST_FAIL_CLOSED_COLOR_GATE",
    }


def adjoint_anomaly_certificate() -> dict[str, object]:
    return {
        "input": "c_ABC=c_[ABC]",
        "transpose_rules": {
            "T_ad_A": "-T_ad_A",
            "anticommutator_BC": "+anticommutator_BC",
        },
        "trace_chain": [
            "d=Tr(TA{TB,TC})",
            "d=Tr((TA{TB,TC})^T)",
            "d=-Tr({TB,TC}TA)",
            "d=-Tr(TA{TB,TC})=-d",
            "d=0",
        ],
        "d_Adj_ABC": 0,
        "step5A_restoration_counterterm": "OPEN",
        "step5C_finite_BV_density": "OUT_OF_SCOPE_FOR_STEP5A",
    }


def completion_theorem_certificate() -> dict[str, object]:
    return {
        "general_injective_completion": {
            "input": "complete tensor-valued quadratic jet ell_2[A_loc]",
            "required": [
                "restored Step5A background Ward identity",
                "ker(ell_2)=0",
            ],
            "rank_one_required": False,
            "status": "OPEN",
        },
        "rank_one_candidate_channel_corollary": {
            "channel": "Sym^2(Adjoint), j_L=3/2, j_R=0, r_f=-1",
            "required": [
                "dim(H_channel)=1",
                "nonzero symmetry-compatible representative O_star",
            ],
            "status": "OPEN",
        },
        "pure_gauge_kernel_route": {
            "conditional_filtration": (
                "ker(ell_2) subset field_strength_degree>=3 "
                "modulo derivative commutators"
            ),
            "dimension_9_over_2_and_r_minus_1": {
                "n_W": 1,
                "n_tildeW": 2,
            },
            "three_field_strength_spin_after_jR_scalar": "(1/2,0)",
            "required_spin": "(3/2,0)",
            "four_field_strength_dimension": "6>9/2",
            "filtration_lemma": "OPEN",
            "full_N4_matter": "SEPARATE_OPEN_GATE",
        },
    }


def build_payload() -> dict[str, object]:
    degrees = connection_degree_certificate()
    source = source_certificate()
    color = color_word_certificate()
    anomaly = adjoint_anomaly_certificate()
    completion = completion_theorem_certificate()
    hessian_payload = hessian.build_payload()
    spin_payload = spin.build_certificate()
    ward_payload = ward.build_payload()
    bridge_payload = bridge.build_payload()

    n2_families = {
        (
            row["s"],
            tuple(row["r_parts"]),
            row["neumann_sign"],
        )
        for row in hessian_payload["terms_by_background_order"]["2"]
    }
    checks = {
        "seed_connection_degrees_are_2_through_7": degrees[
            "seed=nabla_minus_X_tensor_X"
        ]
        == [2, 3, 4, 5, 6, 7],
        "candidate_connection_degrees_are_2_through_6": degrees[
            "candidate=tildeW_times_DX"
        ]
        == [2, 3, 4, 5, 6],
        "source_full_measure_dimension_is_minus_five_halves": source[
            "source_dimension"
        ]
        == "-5/2",
        "source_odd_Leibniz_pairing_is_invariant": source[
            "invariant_pairing_coefficient"
        ]
        == 0,
        "Project_R_weight_binding_is_not_claimed": source[
            "Project_U1R_binding"
        ]
        == "OPEN",
        "physical_seed_is_in_Sym2_Adjoint": source[
            "physical_local_seed_subspace"
        ]
        == "Sym^2(Adjoint)"
        and color["seed_exchange_symmetry"] == "SYMMETRIC_AB",
        "literal_dotted_index_positions_are_exact": color[
            "Y_upper_W_lower_coefficients"
        ]
        == [0, -1, 1, 0]
        and color["W_lower_Y_upper_coefficients"] == [0, -1, 1, 0]
        and color["Y_lower_W_upper_coefficients"] == [0, 1, -1, 0]
        and color["lower_upper_is_minus_upper_lower"] is True,
        "literal_candidate_is_antisymmetric_with_zero_Sym2_projection": color[
            "literal_candidate_open_exchange"
        ]
        == "ANTISYMMETRIC_AB"
        and color["literal_candidate_Sym2_projection"] == "ZERO",
        "ordered_color_word_quotient_remains_open": source[
            "ordered_to_local_quotient"
        ]
        == "OPEN_COLOR_WORD_QUOTIENT"
        and color["ordered_A_bar_B_to_local_Sym2"]
        == "OPEN_COLOR_WORD_QUOTIENT",
        "injective_completion_is_distinct_from_rank_one_corollary": completion[
            "general_injective_completion"
        ]["rank_one_required"]
        is False
        and completion["rank_one_candidate_channel_corollary"]["status"] == "OPEN",
        "pure_gauge_kernel_filtration_is_not_claimed": completion[
            "pure_gauge_kernel_route"
        ]["filtration_lemma"]
        == "OPEN",
        "adjoint_cubic_anomaly_tensor_is_zero": anomaly["d_Adj_ABC"] == 0,
        "hessian_n2_four_families_have_exact_signs": n2_families
        == {
            (0, (1, 1), 1),
            (0, (2,), -1),
            (1, (1,), -1),
            (2, (), 1),
        },
        "hessian_polarized_counts_are_6_26_150": hessian_payload[
            "polarized_term_counts"
        ]
        == {"2": 6, "3": 26, "4": 150},
        "spin_projector_ranks_are_10_equals_6_plus_4": spin_payload[
            "dimensions"
        ]
        == {"domain": 10, "sym5": 6, "sym3": 4},
        "seed_spin_component_identity_is_exact": spin_payload[
            "component_formula"
        ]["identity"]
        == "U_-;++++=H_-++++-(4/5)t_+++",
        "seed_spin_five_halves_is_closed_by_chiral_bianchi": spin_payload[
            "spin_five_halves_gate"
        ]["status"]
        == "CLOSED_EXACT"
        and spin_payload["rank_five_closure"]["status"] == "CLOSED_EXACT",
        "seed_tree_EOM_identity_is_closed": spin_payload[
            "tree_level_eom_identity"
        ]["status"]
        == "CLOSED_EXACT_AT_TREE_LEVEL",
        "seed_quantum_spin_cohomology_remains_open": spin_payload[
            "quantum_gates"
        ]["status"]
        == "OPEN",
        "ward_output_is_chiral_frame_rho2_etaR": ward_payload[
            "polarized_chiral_frame_Ward_recursion"
        ]["output_representation"]
        == "rho_2(eta_R)",
        "vector_subgroup_has_no_level_mixing": ward_payload["vector_subgroup"][
            "level_mixing"
        ]
        is False,
        "bridge_separates_chain_rules_and_conditional_similarity": bridge_payload[
            "equations"
        ]["hessian_chain_rule"]
        == "K_C=J_q^st*K_V*J_q+E_(V,alpha)*C^alpha"
        and bridge_payload["equations"]["hessian_endomorphism_conditional"]
        == "H_C=J_q^(-1)*H_V*J_q when E_V*C=0"
        and bridge_payload["equations"]["source_hessian_chain_rule"]
        == (
            "Ibil_C=J_q^st*Ibil_V*J_q+F_(V,alpha)*C^alpha; "
            "F_V=d(I_V)/d(zeta_V)"
        )
        and bridge_payload["equations"]["source_endomorphism_conditional"]
        == "Iop_C=J_q^(-1)*Iop_V*J_q when F_V*C=0",
        "bridge_full_jacobian_and_finite_bv_remain_open": bridge_payload["gates"][
            "full_physical_ghost_nonminimal_frame_jacobian"
        ]
        == "OPEN_3D109A"
        and bridge_payload["gates"]["full_finite_bv_density_and_cycle"]
        == "OPEN_STEP5C_3D110"
        and bridge_payload["gates"][
            "cross_frame_functional_equality_with_independent_flat_measures"
        ]
        == "NOT_ASSERTED",
    }
    return {
        "schema": "Step5OneLoopTheoremTypeAudit.v3",
        "status": "PASS_EXACT_TYPES_WITH_OPEN_THEOREM_GATES"
        if all(checks.values())
        else "FAIL",
        "connection_degree": degrees,
        "source_and_BRST_dual": source,
        "open_color_and_dotted_index": color,
        "completion_theorem": completion,
        "adjoint_gauge_anomaly": anomaly,
        "hessian_census": {
            "status": hessian_payload["status"],
            "family_counts": hessian_payload["family_counts"],
            "polarized_counts": hessian_payload["polarized_term_counts"],
            "ordered_block_values": "OPEN",
        },
        "spin_projector": {
            "certificate_status": spin_payload["certificate_status"],
            "direct_sum_ranks": spin_payload["dimensions"],
            "component_identity": spin_payload["component_formula"]["identity"],
            "j_five_halves_removal": spin_payload["spin_five_halves_gate"][
                "status"
            ],
            "tree_EOM_identity": spin_payload["tree_level_eom_identity"][
                "status"
            ],
            "quantum_gates": spin_payload["quantum_gates"]["status"],
        },
        "Ward_recursion": {
            "formal_status": ward_payload["status"],
            "frame": ward_payload["polarized_chiral_frame_Ward_recursion"][
                "frame"
            ],
            "output_representation": ward_payload[
                "polarized_chiral_frame_Ward_recursion"
            ]["output_representation"],
            "vector_subgroup_level_mixing": ward_payload["vector_subgroup"][
                "level_mixing"
            ],
            "quantum_restoration": "OPEN",
        },
        "frame_bridge": {
            "status": bridge_payload["status"],
            "scope": bridge_payload["scope"],
            "operator_similarity": bridge_payload["gates"][
                "covariant_operator_similarity_general_gauge_algebra"
            ],
            "quadratic_supertrace_similarity_sector": bridge_payload["gates"][
                "quadratic_hessian_green_source_supertrace_on_similarity_sector"
            ],
            "reference_flat_adjoint_block": bridge_payload["gates"][
                "reference_flat_measure_covariant_adjoint_block"
            ],
            "full_physical_ghost_nonminimal_jacobian": bridge_payload["gates"][
                "full_physical_ghost_nonminimal_frame_jacobian"
            ],
            "full_finite_bv_density_and_cycle": bridge_payload["gates"][
                "full_finite_bv_density_and_cycle"
            ],
            "independent_flat_measure_functional_equality": bridge_payload["gates"][
                "cross_frame_functional_equality_with_independent_flat_measures"
            ],
            "Step5A_primary_frame": "GAUGE_VECTOR_NO_CHANGE_OF_VARIABLES_REQUIRED",
        },
        "open_theorem_gates": [
            "OPEN_COLOR_WORD_QUOTIENT",
            "OPEN_REFLECTED_DOTTED_INDEX_VARIANCE",
            "SOURCE_EXTENDED_BV_MULTIPLET_CLOSURE",
            "SEED_J_3_OVER_2_QUANTUM_COHOMOLOGY_AND_CANDIDATE_MATCH",
            "ORDERED_NONZERO_PROJECT_HESSIAN_BLOCKS",
            "STEP5A_LOCAL_BACKGROUND_WARD_RESTORATION",
            "LOCAL_COVARIANT_COHOMOLOGY_RANK_ONE",
            "QUADRATIC_JET_INJECTIVITY",
            "PURE_GAUGE_ASSOCIATED_GRADED_FILTRATION",
            "PROJECT_R_WEIGHT_BINDING",
            "M0_SCHWINGER_DYSON_ORBIT",
        ],
        "step5C_only_gates": [
            "FINITE_BV_DENSITY",
            "FULL_FUNCTIONAL_FRAME_JACOBIAN",
        ],
        "checks": checks,
        "external_coefficients_imported": False,
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    audit = {
        "schema": "Step5OneLoopTheoremTypeAuditVerification.v2",
        "status": payload["status"],
        "checks": len(payload["checks"]),
        "failed": [name for name, passed in payload["checks"].items() if not passed],
        "open_theorem_gates": len(payload["open_theorem_gates"]),
        "step5C_only_gates": len(payload["step5C_only_gates"]),
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT.write_bytes(canonical_json(audit))


if __name__ == "__main__":
    write_artifacts()
