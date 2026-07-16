from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG1G3RawMultiplicityTraceExactTest(unittest.TestCase):
    def test_artifact(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_g1_g3_raw_multiplicity_trace_exact_audit.py"
        artifact = ROOT / "audits" / "step5-ab-ba-g1-g3-raw-multiplicity-trace-exact.json"
        note = ROOT / "audits" / "step5-ab-ba-g1-g3-raw-multiplicity-trace-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_AB_BA_G1_G3_RAW_MULTIPLICITY_ONE__"
            "NO_EXTRA_TRANSVERSE_HALF__CURRENT_MAGNITUDES_RETAINED",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["residual_q_used"])
        self.assertEqual(payload["cyclic_source_hessian"]["supertrace"], "(1/2)*(1+1)=1")
        self.assertEqual(payload["G1"]["primitive_multiplicity"]["total"], "1")
        self.assertEqual(payload["G1"]["raw_generic_(p_B,q_D)"], ["2", "2"])
        self.assertEqual(payload["G1"]["decision"], "RETAIN")
        self.assertEqual(payload["G3"]["primitive_multiplicity"]["total"], "1")
        self.assertEqual(
            payload["G3"]["typed_coefficients"],
            {
                "G32_C2_gt_C3": "-2*sqrt(2)*i",
                "G33_C3_gt_C2": "2*sqrt(2)*i",
            },
        )
        self.assertEqual(payload["G3"]["decision"], "RETAIN")
        self.assertFalse(payload["transverse_rank"]["extra_rank_trace_half"])
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS AB_BA_SOURCE_CYCLIC_HALF_TIMES_TWO_EQUALS_ONE", completed.stdout)
        self.assertIn("PASS AB_BA_G1_RAW_MULTIPLICITY_ONE_AND_SCALE_TWO", completed.stdout)
        self.assertIn("PASS AB_BA_G3_RAW_MULTIPLICITY_ONE_AND_SCALE_TWO", completed.stdout)
        self.assertIn("PASS AB_BA_TRANSVERSE_TRACE_NO_EXTRA_HALF", completed.stdout)


if __name__ == "__main__":
    unittest.main()
