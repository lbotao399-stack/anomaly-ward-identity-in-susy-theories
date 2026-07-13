from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5CoreTest(unittest.TestCase):
    def test_exact_core_verifier_is_reproducible(self) -> None:
        script = ROOT / "scripts/verify_step5_core.py"
        audit_path = ROOT / "audits/step5-core-verification.json"
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["stage"], "REGISTERED_FIXED_VECTOR_WARD_PROVED")
        self.assertEqual(
            audit["stage_qualifier"],
            "WW_CONTACT_AND_INJECTIVITY_OPEN",
        )
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(len(audit["channel_ledger"]), 16)
        ww = next(item for item in audit["channel_ledger"] if item["id"] == "W__W")
        self.assertEqual(
            ww["one_loop_seed_state"],
            "ISOLATED_TRIANGLE_DERIVED__ANOMALY_INVALIDATED_NOT_PROPAGATED",
        )
        self.assertNotIn("DERIVED_WW_SEED_G2_OVER_64PI2", expected)


if __name__ == "__main__":
    unittest.main()
