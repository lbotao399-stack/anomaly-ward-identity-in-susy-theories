import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "audits" / "step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json"


class G1ActualResolventContactOrbitExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(ARTIFACT.read_text())

    def test_all_checks_pass(self) -> None:
        checks = self.payload["checks"]
        self.assertGreaterEqual(checks["count"], 35)
        self.assertEqual(checks["failed"], 0)
        self.assertEqual(checks["passed"], checks["count"])

    def test_vector_frame_source_is_complete_through_i2(self) -> None:
        source = self.payload["vector_frame_source"]
        self.assertEqual(len(source["I1_order_three"]), 4)
        self.assertEqual(len(source["I1_exact_ten_descendant_words_AB"]), 10)
        self.assertEqual(len(source["I2_order_four"]), 10)

    def test_only_ordinary_r2_gauge_bubble_survives(self) -> None:
        bubble = self.payload["R2_gauge_bubble"]
        for orientation in ("AB", "BA"):
            for dotted in ("0", "1"):
                row = bubble[orientation][dotted]
                self.assertFalse(row["four_dimensional_inverse_square"])
                self.assertEqual(row["DRED_anomaly_sector"], "0")

    def test_other_lower_resolvents_are_zero(self) -> None:
        self.assertEqual(self.payload["R1"]["DRED_anomaly_sector"], "0")
        zero = self.payload["R2_R3_symbolic_zero_bubbles"]
        for family in ("R2_M", "R3_M4"):
            for dotted in ("0", "1"):
                self.assertEqual(zero[family][dotted]["AB"], {})
                self.assertEqual(zero[family][dotted]["DRED_anomaly_sector"], "0")

    def test_ordinary_longitudinal_term_is_outside_anomaly_sector(self) -> None:
        boundary = self.payload["longitudinal_boundary"][
            "ordinary_no_inverse_square_term"
        ]
        self.assertFalse(boundary["anomaly_sector"])
        self.assertEqual(
            boundary["raw_Ward_contact_completion"],
            "SEPARATE_IDENTITY_NOT_CLAIMED_COMPLETE",
        )

    def test_common_layer(self) -> None:
        common = self.payload["common_layer"]
        self.assertEqual(common["new_R1_R2_R3_anomaly_raw_p_q"], ["0", "0"])
        self.assertEqual(common["G1_raw_p_q"], ["2", "2"])
        self.assertEqual(common["G1_pair_total_derivative"], ["0", "2"])
        self.assertEqual(common["G1_after_total_derivative_quotient"], "0")
        self.assertFalse(common["missing_terms_supply_minus_one_D_gt_B1"])
        self.assertEqual(common["common_layer_closure_verdict"], "NO_COMMON_LAYER_CLOSURE")


if __name__ == "__main__":
    unittest.main()
