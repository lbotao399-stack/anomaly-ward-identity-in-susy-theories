from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HTZeroShiftFactorTwoTest(unittest.TestCase):
    def test_generated_artifacts_are_current(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/step5_ht_zero_shift_factor_two_adjudication.py"),
                "--check",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 13/13 PASS", result.stdout)
        artifact = json.loads(
            (
                ROOT
                / "audits/step5-ht-zero-shift-factor-two-adjudication.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            artifact["status"],
            "SOURCE_INTERNAL_FACTOR_TWO_PROVED__PROJECT_FEYNMAN_AND_COMPONENT_BRANCH_SELECTED",
        )
        self.assertEqual(
            artifact["adjudication"]["project_kernel_prefactor"],
            "retain the leading factor 2 in K^P_mn",
        )


if __name__ == "__main__":
    unittest.main()
