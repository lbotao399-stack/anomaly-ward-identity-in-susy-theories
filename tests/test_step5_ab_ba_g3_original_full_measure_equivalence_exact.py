from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG3OriginalFullMeasureEquivalenceExactTest(unittest.TestCase):
    def test_exact_artifact(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ab_ba_g3_original_full_measure_equivalence_exact_audit.py"
        )
        artifact = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
        )
        note = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-original-full-measure-equivalence-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())

        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_G3_ORIGINAL_FULL_MEASURE_EQUIVALENCE__"
            "CONVERSION_MAGNITUDE_FOUR__TWO_SUPERTRACE_CYCLES_CANCEL_HALF__"
            "C_G3_4096",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["HT_used"])
        self.assertFalse(payload["desired_vector_fitting_used"])
        self.assertEqual(payload["checks"]["count"], 53)
        self.assertEqual(payload["checks"]["passed"], 53)
        self.assertEqual(payload["checks"]["failed"], 0)

        measure = payload["grassmann_measure_equivalence"]
        self.assertEqual(measure["engine_measure_identity"]["conversion"], "+4")
        sign = measure["ordered_H_orientation_translation"]
        self.assertTrue(sign["intermediate_sign_disagreement"])
        self.assertFalse(sign["scalar_disagreement"])
        self.assertEqual(measure["coefficient_chain"]["c_G3"], "4096")

        for frame in measure["generic_frame_coefficientwise_checks"].values():
            for mark in frame["marks"].values():
                self.assertEqual(mark["N_original_minus_N_full_MH"], {})
                self.assertEqual(mark["N_original_minus_N_full_SH"], {})
                self.assertEqual(
                    mark["N_original"]["sha256"],
                    mark["N_full_delete_MH_D2_sha256"],
                )
                self.assertEqual(
                    mark["N_original"]["sha256"],
                    mark["N_full_delete_SH_D2_sha256"],
                )

        cycles = payload["supertrace_cycle_census"]
        self.assertEqual(cycles["candidate_count"], 16)
        self.assertEqual(cycles["nonzero_count"], 2)
        self.assertEqual(cycles["correct"], "(1/2)*(C1+C2)=C1")
        self.assertEqual(cycles["rejected"], "(1/2)*C1=C1/2")
        self.assertEqual(
            cycles["first_false_equality"],
            "(1/2)*(C1+C2) -> (1/2)*C1",
        )
        self.assertTrue(
            cycles["errors_are_same_missing_factor_not_two_independent_halves"]
        )

        forbidden_controls = [
            byte
            for byte in note.read_bytes()
            if byte <= 8 or byte in (11, 12, 127) or 14 <= byte <= 31
        ]
        self.assertEqual(forbidden_controls, [])

        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS 53/53 checks", completed.stdout)
        self.assertIn("PASS c_G3=4096; rejected c_G3=2048", completed.stdout)


if __name__ == "__main__":
    unittest.main()
