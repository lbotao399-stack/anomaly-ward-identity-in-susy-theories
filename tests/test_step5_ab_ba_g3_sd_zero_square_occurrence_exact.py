from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG3SdZeroSquareOccurrenceExactTest(unittest.TestCase):
    def test_artifact_is_target_blind_exact_and_current(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ab_ba_g3_sd_zero_square_occurrence_exact_audit.py"
        )
        artifact = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-sd-zero-square-occurrence-exact.json"
        )
        note = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-sd-zero-square-occurrence-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_G3_THREE_SD_CUTS_AND_ZERO_SQUARE_I1_I2_FAMILIES_EXHAUSTED__"
            "NO_NET_CC_EXTERNAL_PORT_CORRECTION__PRECOHOMOLOGY_MAGNITUDE_TWO_RETAINED",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["residual_q_used"])
        self.assertFalse(payload["total_divergence_used"])
        self.assertFalse(payload["cohomology_projection_used"])
        self.assertEqual(
            set(payload["three_SD_rows"]),
            {"e0", "e1", "e2"},
        )
        self.assertTrue(
            all(row["full_d_sum"] == "0" for row in payload["three_SD_rows"].values())
        )
        self.assertEqual(payload["zero_square_descendants"]["I1"]["sum"], "0")
        self.assertEqual(payload["zero_square_descendants"]["I2"]["sum"], "0")
        self.assertEqual(
            payload["zero_square_descendants"]["net_CC_external_port_correction"],
            "0",
        )
        self.assertFalse(
            payload["occurrence_exhaustion"]["omitted_independent_I1_I2_contact_family"]
        )
        self.assertEqual(payload["occurrence_exhaustion"]["unaccounted"], [])
        self.assertEqual(
            payload["precohomology_coefficients_lambda1"][
                "AB_typed_basis_(C2>C3,C3>C2)"
            ],
            ["-2*sqrt(2)*i", "2*sqrt(2)*i"],
        )
        self.assertEqual(
            payload["precohomology_coefficients_lambda1"][
                "BA_typed_basis_(C2>C3,C3>C2)"
            ],
            ["2*sqrt(2)*i", "-2*sqrt(2)*i"],
        )
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "PASS G3 three edgewise full-d Schwinger cancellations",
            completed.stdout,
        )
        self.assertIn(
            "PASS G3 no net I1/I2 CC external-port correction",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
