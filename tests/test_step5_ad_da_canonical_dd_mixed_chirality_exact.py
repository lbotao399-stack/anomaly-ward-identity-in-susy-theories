from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AdDaCanonicalDdMixedChiralityExactTest(unittest.TestCase):
    def test_artifact(self) -> None:
        script = ROOT / "scripts" / "step5_ad_da_canonical_dd_mixed_chirality_exact_audit.py"
        artifact = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.json"
        note = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(
            payload["source_hessian"]["direct_components"],
            {"AD": "i/4", "DA": "1/4"},
        )
        self.assertFalse(payload["source_hessian"]["extra_factor_two"])
        for pair in ("A__Ddot1", "Ddot1__A"):
            self.assertEqual(
                payload["graph_ir"][pair]["canonical_component_parent"],
                "S_g^-|D x S_g^+|D",
            )
            self.assertEqual(
                payload["graph_ir"][pair]["physical_outputs"],
                ["D>D", "D>D"],
            )
        self.assertEqual(payload["normalization"]["raw_integrated_to_lambda1"], "-8")
        self.assertIsNone(payload["result"]["AD_dot_a"])
        self.assertIsNone(payload["result"]["DA_dot_a"])
        self.assertEqual(
            payload["rejection"]["omitted_source_hessian"],
            "crossed F^{BA}_{DE}",
        )
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("REJECTED AD_DA_IMPORTED_OUTPUT_ROUTING", completed.stdout)


if __name__ == "__main__":
    unittest.main()
