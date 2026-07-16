from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_aa_gauge_longitudinal_first_error_exact_audit.py"
ARTIFACT = ROOT / "audits/step5-aa-gauge-longitudinal-first-error-exact.json"


class Step5AAGaugeLongitudinalFirstErrorExactTest(unittest.TestCase):
    def test_wrong_chiral_index_and_correct_determinants(self) -> None:
        payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(
            payload["status"],
            "AA_GAUGE_WRONG_CHIRAL_INDEX_PROVED__FULL_EDGE_ORBIT_PENDING",
        )
        self.assertEqual(
            payload["wrong_Dplus_control"]["mark01_selected"], ["0"] * 4
        )
        self.assertEqual(
            payload["wrong_Dplus_control"]["mark02_selected"], ["0"] * 4
        )
        self.assertEqual(
            payload["row_sums"]["mark01_selected"],
            "2*b2*(a0*d0 - b0*c0)",
        )
        self.assertEqual(
            payload["row_sums"]["mark02_selected"],
            "2*b0*(a2*d2 - b2*c2)",
        )
        self.assertEqual(payload["row_sums"]["mark02_longitudinal"], "0")

    def test_exact_replay(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "audit.json"
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--output", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("SUMMARY 7/7 PASS", completed.stdout)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")),
                json.loads(ARTIFACT.read_text(encoding="utf-8")),
            )


if __name__ == "__main__":
    unittest.main()
