from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5DREDIntegralTest(unittest.TestCase):
    def test_exact_dred_integral_audit_is_reproducible(self) -> None:
        script = ROOT / "scripts/verify_step5_dred_integrals.py"
        audit_path = ROOT / "audits/step5-dred-integrals-verification.json"
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(
            audit["totals"],
            {"exact_checks": 47, "failed_checks": 0},
        )
        self.assertEqual(
            audit["feynman_parameter_shift"]["bare_numerator_check_classification"],
            "CONVENTION_TEMPLATE_ONLY",
        )
        self.assertEqual(
            audit["integrals"]["metric_split_of_rank_two_pole"]["classification"],
            "KINEMATIC_PROJECTOR_TRACE_ONLY_NOT_AN_ANOMALY_COEFFICIENT",
        )


if __name__ == "__main__":
    unittest.main()
