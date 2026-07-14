from __future__ import annotations

import json
import unittest

from scripts import step6_independent_selected_edge_word_dalgebra_gate as gate


class Step6IndependentSelectedEdgeWordDAlgebraGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = gate.build_payload()
        cls.audit = gate.build_audit(cls.payload)

    def test_frozen_seed_word_coproduct_selects_exact_domain(self) -> None:
        selection = self.payload["selection"]
        self.assertEqual(selection["raw_parent_pair_count"], 768)
        self.assertEqual(selection["measure_expanded_raw_pair_occurrence_count"], 13824)
        self.assertEqual(selection["selected_unique_edge_word_pair_count"], 142)
        self.assertEqual(
            selection["selected_word_pairs_sha256"],
            "68fb00bee6917d76dabe58a5eafed6afb16ed061c86b52d8871d9949d4c468a5",
        )
        self.assertEqual(
            selection["selection_engine"],
            "INDEPENDENT_SEED_WORD_COPRODUCT_NO_DWORD_EXECUTION",
        )

    def test_local_exterior_algebra_is_exact(self) -> None:
        algebra = self.payload["local_exterior_algebra"]
        self.assertTrue(algebra["all_same_chirality_anticommutators_zero"])
        self.assertTrue(algebra["all_mixed_anticommutators_equal_minus_2_i_p"])
        self.assertEqual(len(algebra["same_chirality_anticommutator_cases"]), 8)
        self.assertEqual(len(algebra["mixed_anticommutator_cases"]), 4)

    def test_exact_142_by_16_gate(self) -> None:
        comparison = self.payload["comparison"]
        self.assertEqual(comparison["selected_word_pair_count"], 142)
        self.assertEqual(comparison["coefficient_basis_dimension"], 16)
        self.assertEqual(comparison["exact_basis_case_count"], 2272)
        self.assertEqual(comparison["basis_mismatch_count"], 0)
        self.assertTrue(comparison["all_operator_matrices_equal"])
        self.assertTrue(comparison["all_basis_outputs_equal"])
        self.assertEqual(
            comparison["pair_rows_sha256"],
            "1a071a308cde13dfcdcbefcf292a234fdcc79671d1535288a963097348e82fa5",
        )

    def test_every_pair_retains_all_basis_cases(self) -> None:
        rows = self.payload["comparison"]["pair_rows"]
        self.assertEqual(len(rows), 142)
        self.assertEqual(len({row["pair_id"] for row in rows}), 142)
        for row in rows:
            self.assertTrue(row["operator_matrices_equal"])
            self.assertTrue(row["all_16_basis_outputs_equal"])
            self.assertEqual(
                [case["basis_mask"] for case in row["basis_cases"]], list(range(16))
            )
            self.assertTrue(all(case["outputs_equal"] for case in row["basis_cases"]))

    def test_independent_side_does_not_use_shared_primitive_engine(self) -> None:
        contract = self.payload["independence_contract"]
        self.assertEqual(contract["imported_project_modules"], ["step6_two_loop_dword"])
        self.assertTrue(contract["only_existing_dwordnf_imported"])
        self.assertEqual(contract["independent_evaluator_forbidden_token_hits"], [])
        self.assertFalse(contract["independent_evaluator_uses_existing_dword_module"])
        self.assertEqual(contract["selector_forbidden_token_hits"], [])
        self.assertFalse(contract["selector_uses_preaggregation_replay"])
        self.assertTrue(contract["independent_ring_and_matrix_classes_are_local"])

    def test_existing_engine_audit_excludes_shared_replay_evaluator(self) -> None:
        engine = self.payload["existing_engine_audit"]
        self.assertTrue(
            all(engine["existing_DWordNF"]["required_definition_hits"].values())
        )
        replay = engine["preaggregation_replay"]
        self.assertTrue(replay["declares_shared_primitive_oracle_role"])
        self.assertTrue(replay["imports_shared_coefficient_tensor"])
        self.assertTrue(replay["imports_existing_DWordNF"])
        self.assertFalse(replay["admissible_as_independent_side"])
        self.assertEqual(replay["gap_id"], "G1[G-SCOPE]")
        self.assertFalse(replay["used_to_select_142_pairs"])
        self.assertFalse(replay["used_by_independent_side"])

    def test_convention_bridge_is_explicit(self) -> None:
        bridge = self.payload["convention_bridge"]
        self.assertEqual(bridge["word_order"]["matrix"], "M(P_1)...M(P_n)")
        self.assertEqual(bridge["delta_endpoint_transfer"]["total_transfer_factor"], -1)
        self.assertEqual(
            bridge["delta_endpoint_transfer"]["raw_matrix_formula"],
            "(-1)^len(I)*M(A)*M(I)",
        )
        self.assertEqual(set(bridge["primitive_token_bridge"]), set(gate.PRIMITIVES))
        self.assertEqual(
            bridge["momentum_bridge"]["local_polynomial_variables"],
            list(gate.MOMENTUM_VARIABLES),
        )

    def test_wrong_delta_transfer_sign_is_detected(self) -> None:
        evaluator = gate.LocalExteriorEvaluator()
        pairs, _ = gate.selected_word_pairs()
        witness = next(
            (action, insertion)
            for action, insertion in pairs
            if evaluator.raw_delta_matrix(action, insertion).entries
        )
        action, insertion = witness
        correct = evaluator.raw_delta_matrix(action, insertion)
        wrong = evaluator.word_matrix(action) @ evaluator.word_matrix(insertion)
        self.assertEqual(len(insertion) & 1, 1)
        self.assertNotEqual(correct, wrong)

    def test_dropped_dword_normal_term_is_detected(self) -> None:
        evaluator = gate.LocalExteriorEvaluator()
        pairs, _ = gate.selected_word_pairs()
        for action, insertion in pairs:
            normal, _ = gate.dword_normal_form(action, insertion)
            if normal:
                raw = evaluator.raw_delta_matrix(action, insertion)
                dropped = gate._normal_form_matrix(evaluator, normal[1:])
                if raw != dropped:
                    break
        else:
            self.fail("no nontrivial corruption witness was found")
        self.assertNotEqual(raw, dropped)

    def test_open_boundaries_remain_explicit(self) -> None:
        self.assertEqual(
            self.payload["open_missing_type_ids"], list(gate.OPEN_MISSING_TYPE_IDS)
        )
        excluded = self.payload["excluded_claims"]
        self.assertIsNone(excluded["aggregated_remainder_object_equality"])
        self.assertIsNone(excluded["residual_contact_ibp"])
        self.assertFalse(excluded["DRED_performed"])
        self.assertIsNone(excluded["UV_pole"])
        self.assertIsNone(excluded["two_loop_AWI_coefficient"])
        self.assertEqual(excluded["two_loop_AWI_coefficient_status"], "UNCOMPUTED")

    def test_audit_and_payload_hashes_pass(self) -> None:
        self.assertTrue(self.audit["all_checks_passed"])
        self.assertTrue(all(self.audit["checks"].values()))
        self.assertEqual(self.audit["counts"]["selected_word_pairs"], 142)
        self.assertEqual(self.audit["counts"]["exact_basis_cases"], 2272)
        self.assertEqual(self.audit["counts"]["basis_mismatches"], 0)
        self.assertEqual(
            self.payload["payload_sha256"],
            gate.digest(
                {
                    key: value
                    for key, value in self.payload.items()
                    if key != "payload_sha256"
                }
            ),
        )

    def test_generated_readback_is_exact(self) -> None:
        generated = json.loads(gate.GENERATED.read_text(encoding="utf-8"))
        audit = json.loads(gate.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(generated, self.payload)
        self.assertEqual(audit, self.audit)


if __name__ == "__main__":
    unittest.main()
