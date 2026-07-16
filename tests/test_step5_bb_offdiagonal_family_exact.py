from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_bb_offdiagonal_family_exact_audit.py"
ARTIFACT = ROOT / "audits" / "step5-bb-offdiagonal-family-exact.json"


class Step5BBOffdiagonalFamilyExactTest(unittest.TestCase):
    def test_exact_audit_is_fresh(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--check", str(ARTIFACT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 149/149 PASS", completed.stdout)

    def test_exact_ht_match_and_pro_adjudication(self) -> None:
        payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_BB_OFFDIAGONAL_DRED_SD_ORBIT_EXACT_HT_MATCH",
        )
        self.assertFalse(payload["external_target_used_as_input"])
        self.assertEqual(payload["summary"], {"checks": 149, "failed": 0, "passed": 149})
        self.assertEqual(
            payload["triangle_result"]["coefficient_over_lambda1"],
            ["-sqrt(2)*I", "sqrt(2)*I"],
        )
        self.assertEqual(
            payload["conditional_HT_comparison_only_after_calculation"][
                "target_minus_calculation"
            ],
            ["0", "0"],
        )
        self.assertEqual(
            payload["triangle_result"]["transported_subtotal_over_lambda1"],
            ["-sqrt(2)*I/3", "sqrt(2)*I/3"],
        )
        self.assertEqual(payload["gpt_pro_adjudication"]["gate1"]["verdict"], "REJECTED")
        self.assertEqual(
            payload["gpt_pro_adjudication"]["gate2"]["sha256"],
            "31f8906d79cd5f824191eb9d09c7733f4723a2916e45e5bac3c2f826f2e7d2e0",
        )
        self.assertEqual(len(payload["spectator_source_double_bridge"]), 4)
        self.assertTrue(
            all(
                row["one_particle_irreducible"] is False
                and row["source_edge_articulation"] is True
                and row["DC3_projection"]
                == "EXACT_ZERO_EXTERNAL_PORT_ORTHOGONALITY"
                for row in payload["spectator_source_double_bridge"]
            )
        )


if __name__ == "__main__":
    unittest.main()
