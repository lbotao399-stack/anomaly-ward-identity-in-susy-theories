from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaFullFamilyExactTest(unittest.TestCase):
    def test_target_blind_full_sd_orbit(self) -> None:
        script = ROOT / "scripts/step5_ab_ba_full_family_exact_audit.py"
        artifact_path = ROOT / "audits/step5-ab-ba-full-family-exact.json"
        markdown_path = ROOT / "audits/step5-ab-ba-full-family-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["schema"], "step5-ab-ba-full-family-exact-v1"
        )
        self.assertEqual(
            artifact["status"],
            "TARGET_BLIND_FULL_G1_G2_G3_SD_ORBIT_INTEGRATED__HT_MISMATCH",
        )
        self.assertFalse(artifact["external_target_used_in_derivation"])

        self.assertEqual(
            artifact["G1"]["marked_generic_pq_lambda1_units"]["sum"],
            ["2", "2"],
        )
        self.assertEqual(
            artifact["G1"]["physical_momentum_constraint"]["sum"], "0"
        )
        self.assertFalse(artifact["G1"]["source_resolvent_bubbles_in_graph_sum"])
        self.assertEqual(
            artifact["G2"]["ordered_generic_pq_lambda1_units"],
            ["4/3", "-1/3"],
        )

        g3 = artifact["G3"]
        self.assertEqual(g3["labeled_factorial_census"]["total_factor"], "1")
        self.assertEqual(
            g3["original_measure_normalization"]["Dword_per_unit_metric"],
            "-4096",
        )
        self.assertEqual(
            g3["lambda1_per_unit_weight"],
            {"G32": "2*sqrt(2)*i", "G33": "-2*sqrt(2)*i"},
        )

        orbit = artifact["G3_full_SD_orbit"]
        self.assertEqual(
            orbit["source_current_occurrences"]["pairwise_integrand_sum"],
            {"A": "0", "B": "0"},
        )
        for occurrence_id in ("G3-A-JE", "G3-A-JX", "G3-B-PE", "G3-B-PX"):
            self.assertEqual(
                orbit["source_current_occurrences"][occurrence_id]["DRED_defect"],
                "0",
            )
        self.assertTrue(
            orbit["induced_SD_contacts"]["not_identified_with_current_bubbles"]
        )
        self.assertEqual(
            orbit["induced_SD_contacts"]["r1"]["classification"],
            "SAME_OUTER_A_OCCURRENCE_NEW_EDGE_SQUARE",
        )
        self.assertEqual(
            orbit["full_DRED_remainder"],
            "-4096*mu2*(p_wedge_q)/(D0*D1*D2)",
        )
        self.assertEqual(orbit["complete_over_isolated_G3_factor"], "1")
        self.assertFalse(orbit["factor_one_half_generated"])

        outputs = artifact["direct_outputs_before_HT"][
            "after_G1_physical_p_L_plus_q_R_zero"
        ]
        self.assertEqual(
            outputs["AB"],
            {
                "B1>D": "1",
                "D>B1": "0",
                "C3>C2": "-2*sqrt(2)*i",
                "C2>C3": "2*sqrt(2)*i",
            },
        )
        self.assertEqual(
            outputs["BA"],
            {
                "B1>D": "0",
                "D>B1": "1",
                "C3>C2": "2*sqrt(2)*i",
                "C2>C3": "-2*sqrt(2)*i",
            },
        )
        self.assertEqual(artifact["after_check_only"]["status"], "MISMATCH")
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
            timeout=600,
        )
        self.assertIn(
            "PASS G3 labeled factorial and original-measure normalization",
            completed.stdout,
        )
        self.assertIn("PASS check-only status MISMATCH", completed.stdout)
        self.assertIn("SUMMARY 112/112 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
