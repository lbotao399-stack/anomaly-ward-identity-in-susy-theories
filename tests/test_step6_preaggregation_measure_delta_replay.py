from copy import deepcopy
import json
from pathlib import Path
import subprocess
import unittest

from scripts import step6_preaggregation_measure_delta_replay as module


class Step6PreaggregationMeasureDeltaReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.build_payload()
        cls.checks = module.exact_checks(cls.payload)
        cls.replay = cls.payload["measure_tagged_delta_convolution_replay"]
        cls.seed = module._load_seed_fixture()

    def _computed(self) -> dict[str, bool]:
        return module._computed_provenance_predicates(self.replay, self.seed)

    def test_all_exact_checks_pass_with_honest_status(self) -> None:
        self.assertTrue(
            all(self.checks.values()),
            [name for name, passed in self.checks.items() if not passed],
        )
        self.assertEqual(self.payload["status"], module.STATUS)
        self.assertEqual(self.payload["resolved_type_id"], module.RESOLVED_TYPE_ID)
        self.assertEqual(
            self.payload["open_missing_type_ids"],
            [
                module.REMAINDER_COMPARATOR_MISSING_TYPE_ID,
                module.RESIDUAL_IBP_MISSING_TYPE_ID,
            ],
        )
        self.assertNotIn("independent_replay_equality", self.replay)
        self.assertFalse(self.payload["external_result_used_as_input"])

    def test_exact_scope_maps_are_executed_branchwise(self) -> None:
        expected_measure = module._validated_measure_scope_map(
            self.seed["measure_tagged_raw_replay"]["measure_scopes"][0]
        )
        expected_delta = module._validated_delta_scope(
            self.seed["finite_delta_convolution"]["delta_scope"]
        )
        self.assertEqual(self.replay["measure_scope_map"], expected_measure)
        self.assertEqual(self.replay["delta_scope_binding"], expected_delta)
        computed = self._computed()
        self.assertTrue(computed["measure_scope_map_exact"])
        self.assertTrue(computed["measure_normalization_applied_once"])
        self.assertTrue(computed["delta_scope_binding_exact"])
        self.assertTrue(computed["delta_scope_consumed_branchwise"])
        self.assertTrue(computed["scope_execution_order_recomputed"])

    def test_replay_cardinalities_and_shared_oracle_digest_regression(self) -> None:
        counts = self.replay["counts"]
        self.assertEqual(
            counts,
            {
                "source_rows": 6,
                "raw_histories": 216,
                "raw_parent_pairs": 768,
                "measure_distributed_action_histories": 3456,
                "measure_pair_histories": 13824,
                "primitive_normal_contributions": 13568,
                "primitive_zero_branches": 36096,
                "nonzero_aggregate_groups": 2176,
                "edge_square_contact_groups": 608,
                "remainder_groups": 1568,
                "sparse_parent_incidence_entries": 6080,
                "contact_parent_pairs": 128,
                "remainder_parent_pairs": 256,
            },
        )
        regression = self.replay["shared_primitive_oracle_regression"]
        self.assertEqual(
            regression["role"],
            "NON_INDEPENDENT_SHARED_ORACLE_RECONSTRUCTION",
        )
        self.assertTrue(regression["contact_hash_agrees"])
        self.assertTrue(regression["remainder_hash_agrees"])
        self.assertIsNone(regression["contact_object_equality"])
        self.assertIsNone(regression["remainder_object_equality"])
        self.assertEqual(
            regression["remainder_object_equality_status"],
            "UNPROVED_NO_OBJECT_LEVEL_COMPARATOR",
        )

    def test_parent_incidence_is_object_level_exact(self) -> None:
        self.assertTrue(
            self.replay["provenance_checks"][
                "all_parent_incidence_reconstructs_aggregate"
            ]
        )
        for row in self.replay["aggregate_rows"]:
            aggregate = module._exact_polynomial_from_json(row["exact_polynomial"])
            parent_sum = module.dword.POLY_ZERO
            for parent in row["parent_incidence"]:
                parent_sum += module._exact_polynomial_from_json(
                    parent["exact_polynomial"]
                )
            self.assertEqual(parent_sum, aggregate)

    def test_residual_contact_ibp_is_explicitly_open(self) -> None:
        open_record = self.replay["residual_contact_IBP"]
        self.assertEqual(
            open_record["missing_type_id"], module.RESIDUAL_IBP_MISSING_TYPE_ID
        )
        self.assertEqual(open_record["execution_state"], "OPEN_NOT_EXECUTED")
        self.assertIsNone(open_record["bound_I3_comparison_matrix"])
        self.assertIsNone(open_record["anomaly_coefficient"])
        self.assertTrue(
            self.replay["provenance_checks"]["residual_contact_IBP_explicitly_open"]
        )

    def test_measure_sign_corruption_is_detected(self) -> None:
        row = self.replay["measure_distributed_action_histories"][0]
        saved = deepcopy(row)
        try:
            row["measure_primitive_hits"][0]["koszul_sign"] *= -1
            row["record_sha256"] = module.digest(
                {key: value for key, value in row.items() if key != "record_sha256"}
            )
            self.assertFalse(self._computed()["measure_koszul_signs_recomputed"])
        finally:
            row.clear()
            row.update(saved)

    def test_original_order_corruption_is_detected(self) -> None:
        row = self.replay["primitive_normal_contributions"][0]
        saved = deepcopy(row)
        try:
            row["original_factor_order"] = list(reversed(row["original_factor_order"]))
            row["record_sha256"] = module.digest(
                {key: value for key, value in row.items() if key != "record_sha256"}
            )
            self.assertFalse(self._computed()["original_factor_order_recomputed"])
        finally:
            row.clear()
            row.update(saved)

    def test_delta_scope_corruption_is_detected(self) -> None:
        row = self.replay["primitive_normal_contributions"][0]
        saved = deepcopy(row)
        try:
            consumption = row["delta_scope_consumption"]
            consumption["delta_scope_id"] = "DELTA::CORRUPTED"
            consumption["record_sha256"] = module.digest(
                {
                    key: value
                    for key, value in consumption.items()
                    if key != "record_sha256"
                }
            )
            row["record_sha256"] = module.digest(
                {key: value for key, value in row.items() if key != "record_sha256"}
            )
            self.assertFalse(self._computed()["delta_scope_consumed_branchwise"])
        finally:
            row.clear()
            row.update(saved)

    def test_residual_ibp_corruption_is_detected(self) -> None:
        row = self.replay["primitive_normal_contributions"][0]
        saved = deepcopy(row)
        try:
            row["residual_IBP_performed"] = True
            row["record_sha256"] = module.digest(
                {key: value for key, value in row.items() if key != "record_sha256"}
            )
            self.assertFalse(self._computed()["residual_contact_IBP_explicitly_open"])
        finally:
            row.clear()
            row.update(saved)

    def test_dependency_closure_is_hash_bound_and_tracked(self) -> None:
        self.assertTrue(module._input_hashes_valid(self.payload))
        provenance = self.payload["input_provenance"]
        self.assertEqual(
            set(provenance["direct_import_paths"]),
            {
                "scripts/step6_coefficient_tensor.py",
                "scripts/step6_two_loop_dword.py",
                "scripts/step6_global_dword_adapter.py",
            },
        )
        self.assertEqual(
            set(provenance["transitive_import_paths"]),
            {
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
            },
        )
        self.assertEqual(
            provenance["explicitly_not_imported"][
                "scripts/step6_ordered_sector_euler_normal_form.py"
            ],
            "REMOVED_FROM_DIRECT_DEPENDENCY",
        )
        fixture = str(module.SEED_FIXTURE.relative_to(module.ROOT))
        required = [
            fixture,
            *provenance["direct_import_paths"],
            *provenance["transitive_import_paths"],
        ]
        for path in required:
            result = subprocess.run(
                ["git", "ls-files", "--error-unmatch", path],
                cwd=module.ROOT,
                capture_output=True,
                check=False,
                text=True,
            )
            self.assertEqual(result.returncode, 0, (path, result.stderr))
            self.assertTrue((module.ROOT / Path(path)).is_file())

    def test_frozen_outputs_match_fresh_payload(self) -> None:
        summary = json.loads(module.GENERATED.read_text(encoding="utf-8"))
        audit = json.loads(module.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(summary, module.build_summary(self.payload))
        self.assertEqual(audit, module.build_audit(self.payload))
        self.assertTrue(audit["all_checks_passed"])
        self.assertIsNone(audit["remainder_object_equality"])
        self.assertTrue(summary["reconstruction_requires_fresh_compiler"])
        self.assertFalse(summary["standalone_replay_certificate"])
        self.assertEqual(summary["semantic_scope"], module.SEMANTIC_SCOPE)
        self.assertTrue(audit["reconstruction_requires_fresh_compiler"])
        self.assertFalse(audit["standalone_replay_certificate"])
        self.assertEqual(audit["semantic_scope"], module.SEMANTIC_SCOPE)


if __name__ == "__main__":
    unittest.main()
