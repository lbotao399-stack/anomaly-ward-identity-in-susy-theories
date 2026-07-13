import unittest

from scripts import step6_measure_scope_sign_audit as audit


class Step6MeasureScopeSignAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = audit.build_payload()

    def test_single_leaf_coefficient_left_rule(self):
        self.assertTrue(self.payload["single_leaf"]["passed"])

    def test_vertex_sign_is_not_global(self):
        self.assertEqual(
            [row["basis_masks"] for row in self.payload["counterexamples"]],
            [[0, 0, 0], [0, 1, 4]],
        )
        self.assertTrue(
            all(
                row["vertex"] == "A" and row["term_id"] == "S3_MINUS_1_2"
                for row in self.payload["counterexamples"]
            )
        )
        self.assertEqual(
            [row["legacy_relation"] for row in self.payload["counterexamples"]],
            ["EQUAL", "MINUS"],
        )
        self.assertTrue(
            all(row["active_scope_identity"] for row in self.payload["counterexamples"])
        )

    def test_active_scope_identity(self):
        self.assertTrue(
            all(
                row["active_scope_identity"]
                for row in self.payload["counterexamples"]
                + self.payload["frozen_action_vertices"]
            )
        )

    def test_global_measure_sign_rejected(self):
        self.assertEqual(
            self.payload["rejected_global_sign_field"]["field_name"],
            "coefficient_order_measure_scope_sign",
        )
        self.assertEqual(
            self.payload["rejected_global_sign_field"]["status"],
            "REJECTED_NOT_A_CANDIDATE",
        )
        self.assertEqual(
            self.payload["required_minimal_field"],
            "LabeledLeaf.coefficient_parity",
        )
        self.assertEqual(self.payload["status"], "PASS_BUG_FIXED_GLOBAL_SIGN_REJECTED")


if __name__ == "__main__":
    unittest.main()
