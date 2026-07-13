from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

from scripts import step6_global_supertensor as global_tensor


ROOT = Path(__file__).resolve().parents[1]


class Step6GlobalSupertensorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = global_tensor.build_payload()
        cls.audit = global_tensor.build_audit(cls.payload)

    def test_audit_passes(self) -> None:
        self.assertEqual(self.audit["status"], "PASS")
        self.assertTrue(all(self.audit["checks"].values()))

    def test_exact_graph_weights_and_orientation_policy(self) -> None:
        certificate = self.payload["graph_weight_certificate"]
        self.assertEqual(certificate["formula"], "-1/(hbar^3*Aut_bg)")
        self.assertEqual(
            [row["hbar_stripped_graph_weight"] for row in certificate["rows"]],
            ["-1", "-1", "-1/2"],
        )
        self.assertTrue(certificate["direct_only_is_physical"])
        self.assertEqual(
            certificate["reflected_role"],
            "ROUTING_COVARIANCE_ONLY_NOT_ADDED",
        )

    def test_global_and_recursive_signs_agree_exhaustively(self) -> None:
        fixture = self.payload["graded_sign"]["exhaustive_fixture"]
        self.assertEqual(fixture["checked_cases"], 11520)
        self.assertTrue(
            fixture[
                "direct_weighted_permutation_equals_recursive_target_removal"
            ]
        )

    def test_direct_superfield_delta_reconstruction(self) -> None:
        fixture = self.payload["graded_sign"][
            "direct_superfield_delta_fixture"
        ]
        self.assertTrue(
            fixture[
                "left_H_inverse_crossed_back_to_exterior_order_equals_delta"
            ]
        )
        self.assertEqual(
            fixture["nonzero_support"],
            [[source, 15 ^ source] for source in range(16)],
        )

    def test_joint_option_tuple_never_multiplies_marginals(self) -> None:
        plan = self.payload["factorized_complete_sum_plan"]
        self.assertTrue(plan["aggregation_before_network_contraction"])
        self.assertEqual(
            plan["local_object"],
            "JOINT_COEFFICIENT_X_COLOR_TENSOR_ON_TOPOLOGY_PORTS",
        )
        self.assertEqual(len(plan["parents"]), 6)
        for parent in plan["parents"]:
            self.assertTrue(
                parent[
                    "same_ordered_local_option_tuple_for_coefficient_and_color"
                ]
            )
            self.assertEqual(
                parent["independent_coefficient_color_marginal_product"],
                "REJECTED",
            )
            self.assertEqual(
                parent["raw_cartesian_cardinality"],
                global_tensor.prod(parent["raw_option_counts"].values()),
            )

    def test_one_exact_direct_row_keeps_all_five_edge_joins(self) -> None:
        row = self.payload["exact_row"]
        self.assertEqual(row["graph_id"], global_tensor.PHYSICAL_GRAPH_ID)
        self.assertEqual(row["orientation"], "direct")
        self.assertEqual(row["amplitude_rank"], 0)
        self.assertEqual(len(row["edge_order"]), 5)
        self.assertEqual(row["external_coefficient_slice"], {"p1": 0, "p2": 0})
        self.assertTrue(row["external_coefficient_indices_retained_not_contracted"])
        self.assertTrue(row["open_insertion_exterior_basis_retained"])
        self.assertGreater(row["candidate_assignments_after_local_sparsity"], 0)
        self.assertGreater(row["nonzero_global_edge_assignments"], 0)
        self.assertTrue(row["coefficient_result_is_nonzero"])

    def test_exact_row_polynomial_regression(self) -> None:
        row = self.payload["exact_row"]
        encoded = json.dumps(
            row["coefficient_exterior_momentum_polynomial"],
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
        self.assertEqual(
            hashlib.sha256(encoded).hexdigest(),
            "ec0463f61f4d7b79ed9ccb4886ba7ff3abba72e53cb3cce29435e45680bac081",
        )
        self.assertEqual(
            [
                item["mask"]
                for item in row["coefficient_exterior_momentum_polynomial"][
                    "terms"
                ]
            ],
            [4, 8, 13, 14],
        )

    def test_raw_qi_edge_kernel_and_orbit_ownership_are_once(self) -> None:
        row = self.payload["exact_row"]
        self.assertEqual(
            row["edge_covariance_ownership"],
            "EACH_EDGE_USES_MINUS_2_TIMES_H_INVERSE_EXACTLY_ONCE",
        )
        self.assertEqual(
            row["raw_local_Qi_ownership"],
            "LOCAL_TENSOR_EVALUATOR_EXACTLY_ONCE",
        )
        self.assertEqual(row["Aut_bg"], 2)
        self.assertEqual(
            row["Aut_bg_certificate_sha256"],
            "312dc8d5bc9008e1e1f636ce0455b2433db42f7ed81b4324f8b38dac1762e824",
        )
        self.assertEqual(row["hbar_stripped_graph_weight"], "-1/2")
        self.assertEqual(row["formal_hbar_power_before_strip"], 2)
        self.assertEqual(row["formal_coupling_rewrite"], "(g^2)^5*h^3=g^4")

    def test_color_network_keeps_ABRS_and_no_extra_i(self) -> None:
        color = self.payload["exact_row"]["color"]
        self.assertEqual(color["free_index_order"], ["A", "B", "R", "S"])
        self.assertEqual(color["external_background_colors"], {"p1": "R", "p2": "S"})
        self.assertTrue(color["no_extra_bracket_i"])
        self.assertEqual(
            color["canonical_reduced_network"]["signature_sha256"],
            "b5243c5758e3a533c11a3b4a8c835847c8184bf53474578d31d4a6ea9d3224c4",
        )

    def test_downstream_physical_claims_fail_closed(self) -> None:
        blocked = self.payload["global_fail_closed"]
        self.assertEqual(
            blocked["complete_two_loop_numerator"],
            "BLOCKED_INCOMPLETE_PAIRING_AND_EXTERNAL_SLICE_SUM",
        )
        self.assertIsNone(blocked["renormalized_two_loop_coefficient"])
        self.assertEqual(
            self.payload["exact_row"]["fail_closed"]["reflected_physical_addition"],
            "REJECTED_ROUTING_CHECK_ONLY",
        )

    def test_generated_payload_and_audit_are_exact_readbacks(self) -> None:
        generated = json.loads(global_tensor.OUTPUT_JSON.read_text(encoding="utf-8"))
        audit = json.loads(global_tensor.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(generated, self.payload)
        self.assertEqual(audit, self.audit)


if __name__ == "__main__":
    unittest.main()
