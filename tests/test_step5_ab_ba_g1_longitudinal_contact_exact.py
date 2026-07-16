from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG1LongitudinalContactExactTest(unittest.TestCase):
    def test_exact_artifact_and_core_replay(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ab_ba_g1_longitudinal_contact_exact_audit.py"
        )
        artifact_path = (
            ROOT
            / "audits"
            / "step5-ab-ba-g1-longitudinal-contact-exact.json"
        )
        markdown_path = (
            ROOT
            / "audits"
            / "step5-ab-ba-g1-longitudinal-contact-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["schema"],
            "step5-ab-ba-g1-longitudinal-contact-exact-v1",
        )
        self.assertEqual(
            artifact["status"],
            "EXACT_TARGET_BLIND_G1_CONTACT_ORBIT_CLOSED",
        )
        self.assertFalse(artifact["external_target_used_in_derivation"])
        self.assertEqual(
            artifact["definitions"]["finite_master"], "1/(32*pi^2)"
        )
        self.assertEqual(artifact["raw_VVV_orbit"]["raw_words"], 24)
        self.assertEqual(artifact["raw_VVV_orbit"]["AB_BA_rows"], 192)

        rows = artifact["validation"]["all_primary_AB_BA_rows"]
        self.assertEqual(len(rows), 192)
        self.assertTrue(
            all(row["full_d_parent_plus_contact"] == "0" for row in rows)
        )
        self.assertTrue(
            all(row["DRED_parent_plus_contact"].endswith("*mu_l^2") for row in rows)
        )
        self.assertEqual(
            artifact["validation"]["first_nonzero_longitudinal_row"]["L"],
            "-1024-2048*i",
        )
        self.assertEqual(
            artifact["validation"]["first_nonzero_A_anomaly_row"]["alpha_minus_8R"],
            "-2048+1024*i",
        )
        self.assertEqual(
            artifact["validation"]["first_nonzero_B_anomaly_row"]["alpha_minus_8R"],
            "1024-1024*i",
        )

        simplex = artifact["simplex_and_quotient"]
        self.assertEqual(
            simplex["generic_p_q_lambda1_units"],
            {
                "A_mark": ["4/3", "2/3"],
                "B_mark": ["2/3", "4/3"],
                "sum": ["2", "2"],
                "sum_word": "2*(p+q)",
            },
        )
        self.assertEqual(
            simplex["local_product_q_equals_minus_p"],
            {"A_mark": "2/3", "B_mark": "-2/3", "sum": "0"},
        )
        self.assertEqual(
            artifact["source_resolvent_probe"]["status"],
            "SAME_CONTACT_PRESENTATION_NOT_INDEPENDENT",
        )
        self.assertEqual(
            artifact["source_resolvent_probe"]["decisive_mismatch"],
            {
                "dot0_all_three_standalone_presentations": "0",
                "dot0_parent_minus_plus_chirality_raw_word": "61440",
            },
        )
        self.assertEqual(
            artifact["derived_before_HT"],
            {
                "AB": {"D>B1": "0"},
                "BA": {"B1>D": "0"},
                "reason": "A_mark+B_mark=2/3-2/3=0 at q=-p",
            },
        )
        self.assertEqual(artifact["checks"]["failed"], 0)
        self.assertEqual(
            artifact["checks"]["passed"], artifact["checks"]["count"]
        )

        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS all 192 AB/BA occurrence rows", completed.stdout)
        self.assertIn("PASS G1 A+B=2/3-2/3=0", completed.stdout)
        self.assertIn("SUMMARY 874/874 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
