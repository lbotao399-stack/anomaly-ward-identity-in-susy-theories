#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts import step6_global_supertensor as global_tensor
from scripts import step6_two_loop_dword as dword
from scripts.step6_global_dword_adapter import (
    AUDIT,
    FIXED_FIELD,
    FROZEN_SOURCE_MASKS,
    OUTPUT_JSON,
    OUTPUT_MD,
    OUTPUT_PROGRAM,
    OUTPUT_RESULT,
    PHYSICAL_GRAPH_ID,
    STATUS,
    build_audit,
    build_payload,
    digest,
    exact_checks,
)


ROOT = Path(__file__).resolve().parents[1]


def contains_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(contains_float(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_float(item) for item in value)
    return False


class Step6GlobalDWordAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_payload()
        cls.audit = build_audit(cls.payload)

    def test_direct_rank_zero_parent_and_exact_local_option_tuple(self) -> None:
        parent = self.payload["physical_parent"]
        self.assertEqual(parent["graph_id"], PHYSICAL_GRAPH_ID)
        self.assertEqual(parent["orientation"], "direct")
        self.assertEqual(parent["amplitude_rank"], 0)
        self.assertEqual(parent["vertex_order"], ["I", "A", "B", "C"])
        self.assertEqual(
            parent["edge_order"], ["e_AI", "e_IB", "e_CA", "e_BC", "e_BA"]
        )
        self.assertEqual(
            parent["selected_local_amplitude_option_ids"],
            {
                "I": "direct::I::I2_direct_001::BQ001::P001",
                "A": "direct::A::S3_MINUS_1_2::BQ001::P001",
                "B": "direct::B::S3_MINUS_1_2::BQ001::P001",
                "C": "direct::C::S4_MINUS_1_3::BQ001::P001",
            },
        )

    def test_frozen_edge_masks_are_one_exact_surviving_assignment(self) -> None:
        assignment = self.payload["fixed_assignment"]
        self.assertEqual(
            FROZEN_SOURCE_MASKS,
            {"e_AI": 0, "e_IB": 0, "e_CA": 4, "e_BC": 4, "e_BA": 11},
        )
        self.assertEqual(assignment["source_masks_in_graph_edge_order"], [0, 0, 4, 4, 11])
        self.assertTrue(assignment["survives"])
        self.assertTrue(global_tensor.deserialize_value(assignment["local_product"]))
        self.assertTrue(
            global_tensor.deserialize_value(
                assignment["assignment_contribution_before_graph_weight"]
            )
        )
        self.assertEqual(assignment["graded_wick_sign"], assignment["recursive_graded_wick_sign"])

    def test_port_ledger_preserves_every_grammar_word_and_all_incoming_momentum(self) -> None:
        rows = self.payload["port_ledger"]
        self.assertEqual(len(rows), 12)
        self.assertEqual(
            sum(row["role"] == "QUANTUM_EDGE_ENDPOINT" for row in rows), 10
        )
        self.assertEqual(
            sum(row["role"] == "BACKGROUND_EXTERNAL_ENDPOINT" for row in rows), 2
        )
        self.assertEqual(len({row["coefficient_id"] for row in rows}), 12)
        self.assertTrue(all(row["grammar_derivative_word_outer_to_inner"] for row in rows))
        right_insertion = next(
            row
            for row in rows
            if row["coefficient_id"] == "I::I2.R.1.flat.W_1.Gamma_1.v1"
        )
        self.assertEqual(right_insertion["edge_id"], "e_IB")
        self.assertEqual(right_insertion["orientation_endpoint"], "source")
        self.assertEqual(right_insertion["all_incoming_leaf_momentum_vector"], [1, 0, -1, 0, 0])
        self.assertEqual(
            right_insertion["grammar_derivative_word_outer_to_inner"],
            ["D_+", "barD^2", "D_+"],
        )

    def test_global_join_key_has_ten_left_slots_and_five_exact_pairings(self) -> None:
        join_key = self.payload["global_join_key"]
        normalized = dword.validate_global_join_key(join_key)
        self.assertEqual(len(normalized["global_left_coefficient_word"]), 10)
        self.assertEqual(len(normalized["fixed_edge_pairing_order"]), 5)
        word_ids = {
            row["coefficient_id"] for row in normalized["global_left_coefficient_word"]
        }
        paired_ids = {
            coefficient_id
            for row in normalized["fixed_edge_pairing_order"]
            for coefficient_id in (
                row["source_coefficient_id"],
                row["target_coefficient_id"],
            )
        }
        self.assertEqual(word_ids, paired_ids)
        for row in normalized["global_left_coefficient_word"]:
            self.assertEqual(row["parity"], row["basis_index"].bit_count() & 1)

    def test_external_p1_p2_and_composite_source_endpoints_are_retained(self) -> None:
        endpoints = self.payload["physical_dword_program"]["endpoints"]
        external = [row for row in endpoints if row["endpoint_kind"] == "EXTERNAL_BACKGROUND"]
        composite = [row for row in endpoints if row["endpoint_kind"] == "COMPOSITE_SOURCE"]
        self.assertEqual(len(external), 2)
        self.assertEqual(
            {tuple(row["momentum"]["coefficients"]) for row in external},
            {(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)},
        )
        self.assertEqual(len(composite), 1)
        self.assertEqual(composite[0]["momentum"]["coefficients"], [0, 0, 1, 0, 0])
        self.assertEqual(composite[0]["equation_class"], "EOM")

    def test_all_incoming_vertex_momenta_close_with_declared_relation(self) -> None:
        record = self.payload["momentum_conservation"]
        self.assertEqual(record["I_plus_composite_source_P"], [0, 0, 0, 0, 0])
        self.assertEqual(record["A"], [0, 0, 0, 0, 0])
        self.assertEqual(record["B"], [0, 0, 0, 0, 0])
        self.assertTrue(record["C_equals_declared_external_relation"])
        self.assertEqual(record["declared_relation"], "P+p1+p2=0")

    def test_scope_expansion_cardinality_is_factorized_not_materialized(self) -> None:
        scope = self.payload["scope_expansion"]
        self.assertEqual(scope["factorized_global_branch_counts"], [4, 288, 288, 960])
        self.assertEqual(scope["factorized_global_cartesian_cardinality"], 318_504_960)
        self.assertFalse(scope["full_cartesian_materialization_performed"])
        for vertex in ["I", "A", "B", "C"]:
            record = scope["per_vertex"][vertex]
            self.assertTrue(record["branch_ledger_regenerated_from_exact_expression_ast"])
            self.assertFalse(record["branch_ledger_persisted_in_prior_global_row"])
            self.assertEqual(len(record["complete_branch_ledger_sha256"]), 64)

    def test_one_complete_actual_insertion_port_word_executes(self) -> None:
        metadata = self.payload["physical_dword_projection"]
        program = self.payload["physical_dword_program"]
        self.assertEqual(metadata["execution_scope"], "ONE_COMPLETE_ACTUAL_GRAMMAR_PORT_WORD")
        self.assertTrue(metadata["not_the_complete_global_numerator"])
        self.assertEqual(metadata["edge_id"], "e_IB")
        self.assertEqual(metadata["orientation_endpoint"], "source")
        self.assertEqual(metadata["basis_index"], 0)
        self.assertEqual(
            metadata["derivative_word_outer_to_inner"],
            ["D_plus", "barD_dotplus", "barD_dotminus", "D_plus"],
        )
        self.assertEqual(program["program_kind"], "GLOBAL_NUMERATOR")
        self.assertEqual(program["branches"][0]["coefficient"], {"domain": "Q(i)", "re": "1/64", "im": "0"})
        self.assertEqual(program["branches"][0]["denominator_edges"], ["e_AI", "e_IB", "e_CA", "e_BC", "e_BA"])
        self.assertEqual(dword.execute_edge_tagged_dalgebra(program), self.payload["physical_dword_result"])

    def test_dword_result_contains_exact_mixed_momenta_and_nilpotent_child(self) -> None:
        result = self.payload["physical_dword_result"]
        self.assertEqual(len(result["terms"]), 2)
        self.assertEqual(len(result["zero_terms"]), 1)
        self.assertEqual(result["zero_terms"][0]["classification"], "NILPOTENT_ZERO")
        ledger_kinds = {
            ledger["kind"]
            for term in result["terms"]
            for provenance in term["provenance"]
            for ledger in provenance["ledger"]
        }
        self.assertIn("MIXED_ANTICOMMUTATOR", ledger_kinds)
        self.assertIn("PRIMITIVE_REORDER", ledger_kinds)
        self.assertTrue(
            all(
                term["remaining_denominator_edges"]
                == ["e_AI", "e_BA", "e_BC", "e_CA", "e_IB"]
                for term in result["terms"]
            )
        )

    def test_independent_16_by_16_oracle_matches_same_assignment(self) -> None:
        comparison = self.payload["independent_oracle_comparison"]
        self.assertEqual(comparison["same_edge_id"], "e_IB")
        self.assertEqual(comparison["same_orientation_endpoint"], "source")
        self.assertEqual(comparison["same_all_incoming_momentum_vector"], [1, 0, -1, 0, 0])
        self.assertEqual(comparison["same_basis_index"], 0)
        self.assertTrue(comparison["operator_matrices_equal"])
        self.assertTrue(comparison["assigned_basis_outputs_equal"])
        self.assertTrue(comparison["assigned_basis_output_nonzero"])
        self.assertEqual(
            comparison["original_operator_sha256"],
            comparison["dword_reconstructed_operator_sha256"],
        )
        self.assertFalse(comparison["numerical_sampling_used"])

    def test_action_measure_scope_identity_uses_coefficient_parity(self) -> None:
        comparison = self.payload["measure_scope_comparison"]
        self.assertEqual([row["vertex_id"] for row in comparison["rows"]], ["A", "B", "C"])
        for row in comparison["rows"]:
            direct = global_tensor.deserialize_value(row["apply_measure_after_left_collection"])
            distributed = global_tensor.deserialize_value(row["distributed_measure_before_left_collection"])
            self.assertEqual(distributed, direct)
            self.assertTrue(row["distributed_equals_direct"])
        fixed = comparison["derivative_fix"]
        self.assertEqual(fixed["field_name"], FIXED_FIELD)
        self.assertTrue(fixed["replacement_preserves_field"])
        self.assertEqual(fixed["status"], "PASS")

    def test_complete_global_equality_fails_closed_without_result_claims(self) -> None:
        boundary = self.payload["acceptance_boundary"]
        self.assertEqual(self.payload["status"], STATUS)
        self.assertEqual(
            boundary["complete_global_dword_equality"],
            "BLOCKED_FULL_GLOBAL_DWORD_CONTRACTION_NOT_PERFORMED",
        )
        self.assertEqual(boundary["coefficient_left_derivative_fix"], "PASS")
        self.assertFalse(boundary["global_numerator_claimed"])
        self.assertFalse(boundary["integral_reduction_performed"])
        self.assertFalse(boundary["pole_claimed"])
        self.assertFalse(boundary["two_loop_coefficient_claimed"])
        self.assertFalse(self.payload["external_result_used_as_calculation_input"])

    def test_exact_domain_contains_no_float(self) -> None:
        self.assertFalse(contains_float(self.payload))

    def test_all_exact_checks_and_audit_pass(self) -> None:
        checks = exact_checks(self.payload)
        self.assertTrue(all(checks.values()), [key for key, value in checks.items() if not value])
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["failed"], 0)
        self.assertEqual(self.audit["passed"], len(self.audit["checks"]))
        self.assertEqual(self.audit["payload_sha256"], self.payload["payload_sha256"])

    def test_generated_artifacts_are_exact_reproducible_readbacks(self) -> None:
        for path in (OUTPUT_JSON, OUTPUT_PROGRAM, OUTPUT_RESULT, OUTPUT_MD, AUDIT):
            self.assertTrue(path.is_file(), path)
        generated = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        program = json.loads(OUTPUT_PROGRAM.read_text(encoding="utf-8"))
        result = json.loads(OUTPUT_RESULT.read_text(encoding="utf-8"))
        audit = json.loads(AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(generated, self.payload)
        self.assertEqual(program, self.payload["physical_dword_program"])
        self.assertEqual(result, self.payload["physical_dword_result"])
        self.assertEqual(audit, self.audit)
        self.assertEqual(
            generated["payload_sha256"],
            digest({key: value for key, value in generated.items() if key != "payload_sha256"}),
        )
        markdown = OUTPUT_MD.read_text(encoding="utf-8")
        self.assertIn("LabeledLeaf.coefficient_parity", markdown)
        self.assertNotIn("coefficient_order_measure_scope_sign", markdown)


if __name__ == "__main__":
    unittest.main()
