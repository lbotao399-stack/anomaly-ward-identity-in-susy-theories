from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class G3Gate7NormalizationFirstErrorExactTest(unittest.TestCase):
    def test_artifact_is_exact_and_current(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_g3_gate7_normalization_first_error_exact_audit.py"
        subprocess.run([sys.executable, str(script), "--check"], cwd=ROOT, check=True)
        payload = json.loads(
            (
                ROOT
                / "audits"
                / "step5-ab-ba-g3-gate7-normalization-first-error-exact.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["first_error"]["section"], "4.2 PX routing")
        self.assertEqual(
            payload["same_unit_sd_orbit"]["kinetic_cuts"]["K2"],
            "+4096*W2/(D0*D1)",
        )
        self.assertEqual(
            payload["corrected_coefficients_lambda1"]["G32_typed_C2_gt_C3"],
            "-2*sqrt(2)*i",
        )
        self.assertEqual(payload["q_covariance"]["common_G1_G3_scale"], "2")
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
