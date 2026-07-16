from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class G3TraceMetricSDExactTest(unittest.TestCase):
    def test_artifact_is_exact_and_current(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_g3_trace_metric_sd_exact_audit.py"
        subprocess.run([sys.executable, str(script), "--check"], cwd=ROOT, check=True)
        payload = json.loads(
            (ROOT / "audits" / "step5-ab-ba-g3-trace-metric-sd-exact.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload["chi_equation"]["unique_solution"], "chi=1")
        self.assertEqual(
            payload["pro_adjudication"]["delta_B"],
            "NOT_CLOSED_UNTIL_RAW_K_MULTIPLICITY_REPLAY",
        )
        self.assertEqual(
            payload["normalization"]["fourier_raw_wedge_to_typed_pairing"],
            "-1",
        )
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
