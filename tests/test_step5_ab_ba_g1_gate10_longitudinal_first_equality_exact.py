import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "audits" / "step5-ab-ba-g1-gate10-longitudinal-first-equality-exact.json"


class G1Gate10LongitudinalFirstEqualityExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(ARTIFACT.read_text())

    def test_all_checks_pass(self) -> None:
        self.assertGreaterEqual(self.payload["checks"]["count"], 40)
        self.assertEqual(self.payload["checks"]["failed"], 0)
        self.assertEqual(
            self.payload["checks"]["passed"], self.payload["checks"]["count"]
        )

    def test_first_equality_is_rejected_before_integration(self) -> None:
        first = self.payload["first_equality"]
        self.assertEqual(first["claimed_total_degree"], 2)
        self.assertEqual(first["exact_total_degree"], 3)
        self.assertEqual(
            first["verdict"], "FALSE_BEFORE_ANY_SIMPLEX_INTEGRAL_OR_QUOTIENT"
        )

    def test_no_row_has_the_claimed_r1_square(self) -> None:
        for frame in self.payload["frames"]:
            for dotted in ("0", "1"):
                test = frame["dotted"][dotted]["r1_square_test"]
                self.assertEqual(test["nonzero_rows"], 12)
                self.assertEqual(test["individually_r1_square_divisible_rows"], [])
                self.assertFalse(test["aggregate_r1_square_divisible"])

    def test_metric_projection_is_q_over_two_not_gate10(self) -> None:
        for frame in self.payload["frames"]:
            self.assertEqual(frame["finite_difference_metric_pair"], frame["exact_pair"])
            self.assertNotEqual(frame["finite_difference_metric_pair"], frame["Gate10_pair"])

    def test_symbolic_source_contact_is_zero(self) -> None:
        contacts = self.payload["source_resolvent_R2_middle_edge"][
            "exact_complete_I1_Sm3_symbolic_replay"
        ]
        self.assertIsInstance(contacts, list)
        self.assertEqual(len(contacts), 2)
        self.assertTrue(all(row["is_exact_zero"] for row in contacts))
        self.assertTrue(all(row["nonzero_output"] == {} for row in contacts))


if __name__ == "__main__":
    unittest.main()
