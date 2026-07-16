from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ABBASourceCycleSupertraceExactTest(unittest.TestCase):
    def test_source_cycle_artifact(self) -> None:
        script = ROOT / "scripts" / "step5_ab_ba_source_cycle_supertrace_exact_audit.py"
        subprocess.run([sys.executable, str(script), "--write"], cwd=ROOT, check=True)
        payload = json.loads(
            (ROOT / "audits" / "step5-ab-ba-source-cycle-supertrace-exact.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(payload["source_hessian"]["canonical_cycle_weight"], "1")
        self.assertEqual(payload["conclusion"]["G1_source_action_half"], "REJECTED")
        self.assertEqual(payload["conclusion"]["G3_source_action_half"], "REJECTED")
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
