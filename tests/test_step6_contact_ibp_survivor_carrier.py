from __future__ import annotations

import gzip
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step6_contact_ibp_survivor_carrier as carrier  # noqa: E402


class ContactIBPSurvivorCarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = carrier.build_payload()
        cls.checks = carrier.exact_checks(cls.payload)
        cls.carriers = cls.payload["carriers"]
        cls.branches = [
            branch for row in cls.carriers for branch in row["coproduct_branches"]
        ]

    def test_all_exact_checks_pass(self) -> None:
        self.assertTrue(all(self.checks.values()), self.checks)

    def test_source_is_the_frozen_bcdfe0c_replay(self) -> None:
        self.assertEqual(self.payload["source_commit"], "bcdfe0c")
        self.assertEqual(
            self.payload["input_provenance"]["source_replay_payload_sha256"],
            carrier.EXPECTED_REPLAY_PAYLOAD_SHA256,
        )
        self.assertEqual(
            self.payload["input_provenance"]["file_sha256"],
            carrier.EXPECTED_INPUT_FILE_SHA256,
        )

    def test_contact_and_residual_token_census(self) -> None:
        self.assertEqual(len(self.carriers), 608)
        self.assertEqual(
            self.payload["token_word_census"],
            {
                "D_plus": 192,
                "barD_dotminus|D_plus": 160,
                "barD_dotplus|D_plus": 160,
                "barD_dotplus|barD_dotminus|D_plus": 96,
            },
        )

    def test_two_A_local_slots_and_theta_I_barrier(self) -> None:
        for row in self.carriers:
            self.assertEqual(
                {slot["edge_id"] for slot in row["A_local_slots"]},
                {"e_BA", "e_CA"},
            )
            self.assertTrue(
                all(slot["theta_A_IBP_eligible"] for slot in row["A_local_slots"])
            )
            self.assertEqual(row["protected_I_local_slot"]["edge_id"], "e_IB")
            self.assertFalse(row["protected_I_local_slot"]["theta_A_IBP_eligible"])

    def test_complete_two_factor_graded_coproduct(self) -> None:
        self.assertEqual(len(self.branches), 2432)
        for row in self.carriers:
            n_tokens = len(row["residual_e_AI_word_outer_to_inner"])
            self.assertEqual(row["coproduct_branch_count"], 2**n_tokens)

    def test_every_ibp_event_reconstructs_its_step_sign(self) -> None:
        for branch in self.branches:
            sign = 1
            for event in branch["ibp_event_ledger"]:
                expected_ibp = -1 if event["ibp_sign_exponent_mod_2"] else 1
                expected_leibniz = (
                    -1 if event["graded_leibniz_sign_exponent_mod_2"] else 1
                )
                self.assertEqual(event["ibp_sign"], expected_ibp)
                self.assertEqual(event["graded_leibniz_sign"], expected_leibniz)
                self.assertEqual(event["step_sign"], expected_ibp * expected_leibniz)
                sign *= event["step_sign"]
            self.assertEqual(branch["ibp_branch_sign"], sign)

    def test_boundary_tokens_are_never_dropped(self) -> None:
        total_events = 0
        for branch in self.branches:
            self.assertTrue(branch["token_conservation"]["counts_equal"])
            self.assertEqual(
                branch["protected_I_local_survivor"][
                    "received_theta_A_IBP_token_count"
                ],
                0,
            )
            for event in branch["ibp_event_ledger"]:
                total_events += 1
                token = event["boundary_token"]
                self.assertEqual(token["disposition"], "RETAIN_UNTIL_ENDPOINT_BINDING")
                self.assertIn("NEVER_DELETE", token["if_external"])
                self.assertIn("EXPLICIT_MOMENTUM_LABELS", token["if_internal"])
        self.assertEqual(total_events, 5248)

    def test_I3_interface_is_exactly_three_port_and_fail_closed(self) -> None:
        self.assertEqual(len(self.payload["I3_target_basis"]), 10)
        self.assertTrue(
            all(
                len(target["port_words"]) == 3
                for target in self.payload["I3_target_basis"]
            )
        )
        self.assertEqual(self.payload["counts"]["raw_port_degree_prefilter_rows"], 1600)
        self.assertEqual(
            self.payload["counts"]["raw_port_degree_no_candidate_rows"], 832
        )
        self.assertEqual(self.payload["counts"]["raw_ordered_I3_word_matches"], 0)
        self.assertEqual(self.payload["counts"]["raw_permutation_I3_word_matches"], 0)
        self.assertIsNone(self.payload["comparison_frontier"]["comparison_matrix"])
        self.assertIsNone(
            self.payload["comparison_frontier"]["object_level_I3_equality"]
        )

    def test_open_types_are_exact_and_no_coefficient_is_claimed(self) -> None:
        self.assertEqual(
            self.payload["original_missing_type_status"],
            "PARTIALLY_RESOLVED_EVENT_CARRIER_ONLY",
        )
        self.assertEqual(
            self.payload["open_missing_type_ids"], list(carrier.OPEN_TYPE_IDS)
        )
        self.assertIsNone(self.payload["anomaly_coefficient"])
        self.assertTrue(
            all(
                branch["anomaly_coefficient_contribution"] is None
                for branch in self.branches
            )
        )

    def test_written_artifact_and_audit_round_trip(self) -> None:
        carrier.write_outputs(self.payload)
        compressed_once = carrier.GENERATED.read_bytes()
        written = json.loads(gzip.decompress(compressed_once).decode("utf-8"))
        carrier.write_outputs(self.payload)
        compressed_twice = carrier.GENERATED.read_bytes()
        audit = json.loads(carrier.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(compressed_once, compressed_twice)
        self.assertEqual(int.from_bytes(compressed_once[4:8], "little"), 0)
        self.assertEqual(written["payload_sha256"], self.payload["payload_sha256"])
        self.assertTrue(audit["all_checks_passed"], audit["checks"])
        self.assertEqual(audit["anomaly_coefficient"], None)
        self.assertEqual(audit["artifact_storage"]["gzip_mtime"], 0)
        self.assertTrue(audit["artifact_storage"]["round_trip_payload_hash_valid"])
        self.assertEqual(
            audit["artifact_storage"]["round_trip_payload_sha256"],
            self.payload["payload_sha256"],
        )
        self.assertEqual(
            audit["artifact_storage"]["compressed_size_bytes"], len(compressed_once)
        )


if __name__ == "__main__":
    unittest.main()
