from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG3ResolventCycleCensusExactTest(unittest.TestCase):
    def test_artifact_is_exact_target_blind_and_current(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ab_ba_g3_resolvent_cycle_census_exact_audit.py"
        )
        artifact = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-resolvent-cycle-census-exact.json"
        )
        note = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-resolvent-cycle-census-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_G3_RESOLVENT_TWO_NONZERO_CYCLES_CORRELATED__"
            "OUTER_HALF_CANCELLED_ONCE__CURRENT_PRED_NO_DOUBLE_COUNT",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["residual_q_used"])
        self.assertEqual(payload["oriented_cycle_census"]["candidate_count"], 16)
        self.assertEqual(payload["oriented_cycle_census"]["nonzero_count"], 2)
        nonzero_ids = [
            row["id"]
            for row in payload["oriented_cycle_census"]["rows"]
            if row["nonzero"]
        ]
        self.assertEqual(
            nonzero_ids,
            [
                "MH::I_1u::M_us::H_s1",
                "HM::I_u1::M_su::H_1s",
            ],
        )
        self.assertTrue(
            payload["correlation"][
                "source_reverse_and_action_swap_are_same_two_rows"
            ]
        )
        self.assertFalse(payload["correlation"]["independent_2x2"])
        self.assertEqual(payload["resolvent_expansion"]["cycle_weight"], "1")
        self.assertEqual(payload["direct_Wick_representation"]["weight"], "1")
        self.assertFalse(payload["preD"]["raw_source_Hessian_factor_two_applied"])
        self.assertFalse(payload["preD"]["current_double_counts_two"])
        self.assertEqual(
            payload["preD"]["G32_current"],
            "-sqrt(2)*g**4*hbar/1024",
        )
        self.assertEqual(payload["preD"]["G32_resolvent"], payload["preD"]["G32_current"])
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "PASS G3 resolvent 16 oriented candidates and 2 nonzero cycles",
            completed.stdout,
        )
        self.assertIn(
            "PASS G3 current pre-D scalar has no extra factor two",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
