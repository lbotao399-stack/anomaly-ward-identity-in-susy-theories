from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class G2OmegaTypedRoutingExactTest(unittest.TestCase):
    def test_artifact_is_exact_and_current(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_g2_omega_typed_routing_exact_audit.py"
        subprocess.run([sys.executable, str(script), "--check"], cwd=ROOT, check=True)
        payload = json.loads(
            (
                ROOT / "audits" / "step5-ab-ba-g2-omega-typed-routing-exact.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["routing"]["M_external"], "D(p)")
        self.assertEqual(payload["routing"]["H_external"], "B1(q)")
        self.assertEqual(payload["typed_projection"]["full"], ["-1/3", "4/3"])
        self.assertFalse(payload["omega_classification"]["delete_as_zero_square"])
        self.assertEqual(payload["q_covariance"]["full_residual"], ["7/3", "0", "0"])
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
