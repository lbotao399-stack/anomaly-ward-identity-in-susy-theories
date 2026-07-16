from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AdDaDirectPhysicalWardQuotientExactTest(unittest.TestCase):
    def test_exact_artifact_and_replay(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ad_da_direct_physical_ward_quotient_exact_audit.py"
        )
        artifact_path = (
            ROOT
            / "audits"
            / "step5-ad-da-direct-physical-ward-quotient-exact.json"
        )
        markdown_path = (
            ROOT
            / "audits"
            / "step5-ad-da-direct-physical-ward-quotient-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["schema"],
            "step5-ad-da-direct-physical-ward-quotient-exact-v2",
        )
        self.assertEqual(
            artifact["status"], "REJECTED_WRONG_EXTERNAL_VERTEX_TYPE"
        )
        self.assertFalse(artifact["external_target_used"])
        self.assertEqual(
            artifact["physical_source_hessian"]["physical_insertion"][
                "coefficient"
            ],
            "1",
        )
        self.assertFalse(
            artifact["physical_source_hessian"]["extra_factor_two"]
        )
        self.assertEqual(
            artifact["physical_source_hessian"][
                "ordered_hessian_components"
            ],
            {"AD": "1/4*i", "DA": "1/4"},
        )
        self.assertEqual(
            artifact["rejection"]["computed_parent"],
            "S_g^- endpoint_D x S_g^- endpoint_D",
        )
        self.assertIn(
            "DD raw-to-lambda1 conversion -8",
            artifact["rejection"]["invalidated"],
        )
        self.assertIsNone(artifact["result"]["AD_dot_a"])
        self.assertIsNone(artifact["result"]["DA_dot_a"])
        self.assertEqual(
            artifact["result"]["normalization_status"],
            "SOURCE_HESSIAN_ONLY_FIXED",
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
        self.assertIn(
            "PASS AD_DA_DIRECT_PHYSICAL_HESSIAN_FACTOR_ONE",
            completed.stdout,
        )
        self.assertIn(
            "REJECTED AD_DA_DD_PARENT_WRONG_EXTERNAL_VERTEX_TYPE",
            completed.stdout,
        )
        self.assertIn("SUMMARY 82/82 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
