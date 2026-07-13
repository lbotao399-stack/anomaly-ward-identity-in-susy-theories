from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts import verify_step5_full_n4_one_loop_status_ledger as module


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5_full_n4_one_loop_status_ledger.py"


class Step5FullN4OneLoopStatusLedgerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.build_payload()

    def test_authority_columns_are_disjoint(self) -> None:
        authority = self.payload["authority_columns"]
        accepted = authority["accepted_origin_main"]
        proposal = authority["draft_pr46_proposal"]
        self.assertEqual(accepted["commit"], module.ACCEPTED_MAIN)
        self.assertEqual(accepted["result"], "EMPTY")
        self.assertEqual(accepted["accepted_full_n4_one_loop_results"], [])
        self.assertEqual(accepted["accepted_anomaly_coefficients"], [])
        self.assertEqual(proposal["commit"], module.PR46_PROPOSAL)
        self.assertEqual(proposal["authority"], "PROPOSAL_ONLY_NOT_ACCEPTED")
        self.assertEqual(proposal["exact_renormalized_channel_results"], [])
        self.assertEqual(proposal["accepted_anomaly_coefficients"], [])
        extension = authority["draft_worktree_extension"]
        self.assertEqual(extension["authority"], "UNCOMMITTED_PROJECT_ONLY_PROPOSAL")
        self.assertEqual(extension["exact_renormalized_channel_results"], [])
        self.assertEqual(extension["accepted_anomaly_coefficients"], [])

    def test_exact_channel_census(self) -> None:
        counts = self.payload["counts"]
        self.assertEqual(counts["ordered_families"], 16)
        self.assertEqual(counts["component_channels"], 81)
        self.assertEqual(counts["partial_seed_families"], 1)
        self.assertEqual(counts["unimplemented_families"], 15)
        self.assertEqual(counts["unimplemented_component_channels"], 80)
        self.assertEqual(counts["tree_zero_families"], 4)
        self.assertEqual(counts["tree_zero_components"], 25)
        self.assertEqual(counts["nonzero_unimplemented_families"], 11)
        self.assertEqual(counts["nonzero_unimplemented_components"], 55)
        self.assertEqual(counts["exact_renormalized_families"], 0)
        self.assertEqual(counts["renormalized_open_families"], 16)
        self.assertEqual(counts["renormalized_open_component_channels"], 81)
        self.assertEqual(counts["ww_mixed_matter_yz_graph_families"], 2)
        self.assertEqual(counts["ww_mixed_matter_yz_connected_labeled_rows"], 8)
        self.assertEqual(counts["ww_mixed_matter_yz_disconnected_typed_matchings"], 2)
        self.assertEqual(counts["ww_mixed_matter_yz_open_obligations"], 4)

    def test_all_sixteen_channels_have_no_renormalized_result(self) -> None:
        channels = self.payload["ordered_channels"]
        self.assertEqual(len(channels), 16)
        self.assertTrue(all(not item["exact_renormalized_result"] for item in channels))
        self.assertTrue(all(item["accepted_coefficient"] is None for item in channels))
        ww = next(item for item in channels if item["channel_id"] == "W__W")
        self.assertEqual(
            ww["one_loop_status"],
            "PARTIAL_EXACT_ISOLATED_VECTOR_TRIANGLE_ONLY__CONTACT_MATTER_QUOTIENT_OPEN",
        )
        zeros = {
            item["channel_id"]
            for item in channels
            if item["tree_status"] == "EXACT_ALL_VALENCE_TREE_ZERO"
        }
        self.assertEqual(
            zeros,
            {
                "TildePhi__TildePhi",
                "TildePhi__TildeW",
                "TildeW__TildePhi",
                "TildeW__TildeW",
            },
        )

    def test_ww_isolated_triangle_intermediate_is_exact(self) -> None:
        ww = self.payload["exact_proposal_intermediates"]["ww_isolated_triangle"]
        self.assertEqual(ww["graph_count"], 2)
        self.assertEqual(
            ww["d_algebra_rows_per_orientation"], {"DIRECT": 8, "REFLECTED": 8}
        )
        self.assertEqual(ww["graph_prefactor_before_d_chain"], "-g^2/8")
        self.assertEqual(ww["closed_d_chain_factor"], "-1/2")
        self.assertEqual(ww["row_prefactor"], "+g^2/16")
        self.assertEqual(
            ww["row_aggregation_semantics"],
            "ADDITIVE_ENDPOINT_ASSIGNMENT_BRANCHES_WITH_DISTINCT_NUMERATORS__NOT_EIGHT_IDENTICAL_AMPLITUDES",
        )
        self.assertEqual(
            ww["four_endpoint_numerator_identity_per_d_minus_placement"],
            "r0*p*r1+r0*p*r2+r1*p*r1+r1*p*r2=(r0+r1)*p*(r1+r2)=L1*p*L2",
        )
        self.assertEqual(
            ww["four_endpoint_factorized_coefficient_per_placement"], "+g^2/16"
        )
        self.assertEqual(ww["two_placement_factorized_coefficient"], "+g^2/8")
        self.assertEqual(
            ww["row_uv_pole"],
            "+g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)",
        )
        self.assertEqual(
            ww["pole_aggregation_per_orientation"],
            "8*(1/1024)*g^2/(pi^2*epsilon)=1/128*g^2/(pi^2*epsilon)",
        )
        self.assertEqual(ww["row_to_orientation_aggregation_status"], "PROVED_EXACT")
        self.assertEqual(ww["renormalized_ward_result"], "OPEN")
        self.assertIsNone(ww["accepted_anomaly_coefficient"])

    def test_stale_aggregate_candidate_is_invalidated(self) -> None:
        boundary = self.payload["coefficient_boundary"]
        self.assertEqual(boundary["accepted_coefficients"], [])
        self.assertEqual(boundary["accepted_full_n4_result_count"], 0)
        self.assertEqual(boundary["full_n4_coefficient"]["status"], "NOT_ESTABLISHED")
        stale = boundary["stale_aggregate_candidate"]
        self.assertEqual(stale["value"], "g^2/(64*pi^2)")
        self.assertEqual(
            stale["ledger_status"],
            "INVALIDATED_STALE_AGGREGATE_SD_CANDIDATE__NO_COEFFICIENT_PROPAGATION",
        )
        self.assertFalse(stale["accepted"])
        self.assertFalse(stale["usable_as_full_n4_result"])
        self.assertFalse(stale["usable_as_ward_coefficient"])

    def test_ww_mixed_matter_yz_census_is_exact_but_not_renormalized(self) -> None:
        matter = self.payload["exact_proposal_intermediates"][
            "ww_mixed_matter_yz_census"
        ]
        self.assertEqual(
            matter["status"],
            "PASS_EXACT_PROJECT_GRAPH_CENSUS__AMPLITUDES_FAIL_CLOSED",
        )
        self.assertEqual(
            matter["triangle_I2_S3m_S3m"]["connected_labeled_row_count"], 4
        )
        self.assertEqual(matter["seagull_I2_S4m"]["connected_labeled_row_count"], 4)
        self.assertEqual(
            matter["open_obligation_ids"],
            [
                "MATTER_SUPERPROPAGATOR_NORMALIZATION",
                "EXTERNAL_Y_DALGEBRA_PROJECTION",
                "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
                "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            ],
        )
        self.assertFalse(any(matter["acceptance_boundary"].values()))
        self.assertEqual(matter["renormalized_ward_result"], "OPEN")
        self.assertIsNone(matter["accepted_anomaly_coefficient"])

    def test_row_to_orientation_aggregation_does_not_multiply_identical_amplitudes(
        self,
    ) -> None:
        checks = self.payload["checks"]
        self.assertTrue(checks["ww_row_to_orientation_pole_aggregation_is_exact"])
        self.assertTrue(
            checks["ww_endpoint_branch_numerator_factorization_is_recorded"]
        )

    def test_contact_matter_quotient_and_step5c_gates_are_open(self) -> None:
        gates = self.payload["open_gates"]
        by_category = {
            category: {item["code"] for item in gates if item["category"] == category}
            for category in {
                "contact",
                "matter_and_channels",
                "quotient_and_scheme",
                "step5c",
            }
        }
        self.assertIn("WW_PHYSICAL_CONTACT_FAMILY", by_category["contact"])
        self.assertIn("CONTACT_HESSIAN_COEFFICIENT", by_category["contact"])
        self.assertIn("ANOMALY_COEFFICIENT", by_category["contact"])
        self.assertIn(
            "FULL_N4_FLUCTUATING_SECTOR_TRACE", by_category["matter_and_channels"]
        )
        self.assertIn(
            "FULL_N4_MATTER_SOURCE_COLOR_COHOMOLOGY",
            by_category["matter_and_channels"],
        )
        self.assertIn(
            "MATTER_SUPERPROPAGATOR_NORMALIZATION",
            by_category["matter_and_channels"],
        )
        self.assertIn(
            "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            by_category["matter_and_channels"],
        )
        self.assertIn(
            "PHYSICAL4D_TOTAL_FILTERED_INJECTIVITY",
            by_category["quotient_and_scheme"],
        )
        self.assertIn(
            "FINITE_COEFFICIENT_SPACE_DENSITY_AND_BEREZINIAN",
            by_category["step5c"],
        )
        self.assertTrue(all(item["status"] == "OPEN" for item in gates))

    def test_no_external_or_ht_target_input(self) -> None:
        scope = self.payload["scope"]
        self.assertTrue(scope["internal_project_artifacts_only"])
        self.assertEqual(scope["holomorphic_twist_input_count"], 0)
        self.assertEqual(scope["external_target_input_count"], 0)
        self.assertEqual(scope["external_coefficient_input_count"], 0)
        self.assertEqual(scope["notion_input_count"], 0)

    def test_all_exact_checks_pass_and_artifacts_are_reproducible(self) -> None:
        self.assertTrue(all(self.payload["checks"].values()))
        self.assertEqual(
            self.payload["status"],
            "PASS_INTERNAL_STATUS_LEDGER__NO_ACCEPTED_FULL_N4_ONE_LOOP_COEFFICIENT",
        )
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        ledger_first = module.OUT.read_bytes()
        audit_first = module.AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(ledger_first, module.OUT.read_bytes())
        self.assertEqual(audit_first, module.AUDIT.read_bytes())
        self.assertEqual(json.loads(ledger_first), self.payload)
        audit = json.loads(audit_first)
        self.assertEqual(audit["failed"], [])
        self.assertEqual(audit["accepted_coefficient_count"], 0)
        self.assertEqual(audit["external_target_input_count"], 0)
        self.assertEqual(audit["holomorphic_twist_input_count"], 0)
        self.assertEqual(
            audit["ledger_sha256"], hashlib.sha256(ledger_first).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
