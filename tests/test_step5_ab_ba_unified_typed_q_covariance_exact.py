from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class UnifiedTypedQCovarianceExactTest(unittest.TestCase):
    def test_artifact_is_exact_and_current(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_unified_typed_q_covariance_exact_audit.py"
        subprocess.run([sys.executable, str(script), "--check"], cwd=ROOT, check=True)
        payload = json.loads(
            (ROOT / "audits" / "step5-ab-ba-unified-typed-q-covariance-exact.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload["G1"]["pair_EOM"], ["2", "2"])
        self.assertEqual(payload["G2"]["pair_EOM"], ["-1/3", "4/3"])
        self.assertEqual(payload["G2"]["exact_divergence_quotient_pair"], "1")
        self.assertEqual(payload["q_covariance"]["scale_candidates"], ["2", "1", "2", "2"])
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
