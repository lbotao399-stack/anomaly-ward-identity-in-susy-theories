from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AcCaFamilyExactTest(unittest.TestCase):
    def test_generated_artifact_and_validator(self) -> None:
        script = ROOT / "scripts/step5_ac_ca_family_exact_audit.py"
        artifact_path = ROOT / "audits/step5-ac-ca-family-exact.json"
        markdown_path = ROOT / "audits/step5-ac-ca-family-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertFalse(artifact["external_target_used_in_derivation"])
        self.assertEqual(artifact["schema"], "step5-ac-ca-family-exact-v2")
        self.assertEqual(
            artifact["status"],
            "TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH",
        )
        self.assertEqual(artifact["TGM"]["route_count"], 6)
        self.assertEqual(artifact["TGM"]["lambda_sum"], "-2")
        self.assertEqual(
            artifact["A__C_r_matter"]["tmm"]["evanescent_probe"],
            ["-1024*p01", "1024*p00"],
        )
        self.assertEqual(
            artifact["C_r__A_matter"]["tmm"][
                "evanescent_probe_after_simplex"
            ],
            ["-1024*q01", "1024*q00"],
        )
        orbit = artifact["full_order_g2_orbit"]
        self.assertEqual(orbit["exact_color"]["identity"], "C_full=F^{AB}_{DE}")
        self.assertEqual(
            orbit["metric_poles"]["TMM_sum"],
            "2-8/d=-2*(4-d)/d=-2*J_mu2/J2",
        )
        self.assertEqual(
            orbit["metric_poles"]["TGM_sum"],
            "8/d-2=+2*(4-d)/d=+2*J_mu2/J2",
        )
        self.assertEqual(
            orbit["first_invalid_old_line"]["classification"],
            "OCCURRENCE_DECOMPOSITION_DOUBLE_COUNT",
        )
        self.assertEqual(
            artifact["ordered_results"]["A__C_r"],
            {"C_r^D>D^E": "-1", "D^D>C_r^E": "+1"},
        )
        self.assertEqual(
            artifact["ordered_results"]["C_r__A"],
            {"C_r^D>D^E": "-1", "D^D>C_r^E": "+1"},
        )
        self.assertEqual(artifact["after_check_only"]["status"], "EXACT_MATCH")

        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS TGM 6/6", completed.stdout)
        self.assertIn("PASS TMM", completed.stdout)
        self.assertIn("PASS full I2-I1S3-I0S4+I0S3S3/2 metric orbit", completed.stdout)
        self.assertIn("SUMMARY 7/7 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
