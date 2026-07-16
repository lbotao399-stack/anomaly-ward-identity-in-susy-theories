from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaG3AbsoluteNormalizationFirstDifferenceExactTest(unittest.TestCase):
    def test_artifact(self) -> None:
        script = (
            ROOT
            / "scripts"
            / "step5_ab_ba_g3_absolute_normalization_first_difference_exact_audit.py"
        )
        artifact = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-absolute-normalization-first-difference-exact.json"
        )
        note = (
            ROOT
            / "audits"
            / "step5-ab-ba-g3-absolute-normalization-first-difference-exact.md"
        )
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())

        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_G3_COLOR_PLUS_I__RAW_32768_TO_4096__"
            "FIRST_SCALE_ONE_ERROR_IS_DOUBLE_TRANSVERSE_HALF__"
            "G1_HAS_NO_ADDITIONAL_HALF",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["project_engine_called"])
        self.assertFalse(payload["holomorphic_twist_used"])
        self.assertFalse(payload["residual_q_used"])
        self.assertFalse(payload["q_covariance_used"])

        color = payload["SU2_color"]
        self.assertEqual(
            color["literal_shorthand"]["formula"],
            "(T_A)^D_X*c_BXE=(i/4)*F^{AB}_{DE}",
        )
        self.assertEqual(color["complete_graph"]["ratio_to_F"], "i")
        self.assertFalse(color["complete_graph"]["extra_half"])
        self.assertEqual(
            color["sample_0110"],
            {
                "frame": [0, 1, 1, 0],
                "F": "-2",
                "literal_Tup_c": "-i/2",
                "complete_graph_color": "-2*i",
            },
        )

        trace = payload["G3_trace_and_absolute_normalization"]
        self.assertEqual(trace["original_measure_mask"], 3312)
        self.assertEqual(trace["absolute_metric_coefficient"], "4096")
        self.assertEqual(trace["earliest_factor_two_error"]["wrong_absolute_word"], "-2048*W")
        self.assertEqual(trace["earliest_factor_two_error"]["correct_absolute_word"], "-4096*W")
        self.assertFalse(
            trace["old_executable_boundary"]["scale_one_derived_from_g3_replay"]
        )

        output = payload["G3_primitives_and_output"]["output_chain"]
        self.assertEqual(output["typed_G32_C2_gt_C3"], "-2*sqrt(2)*i")
        self.assertEqual(output["typed_G33_C3_gt_C2"], "2*sqrt(2)*i")

        g1 = payload["G1_half_check"]
        self.assertFalse(
            g1["source_derivative_convention"]["additional_post_replay_half"]
        )
        self.assertFalse(
            g1["endpoint_probe_maps"]["additional_component_half"]
        )
        self.assertEqual(g1["selected_mark_check"], {"A": "2/3", "B": "-2/3"})
        self.assertEqual(payload["checks"]["failed"], 0)

        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS SU2_COMPLETE_G3_COLOR_PLUS_I_F_NO_HALF", completed.stdout)
        self.assertIn(
            "PASS RAW_TRACE_EQUALS_32768_TIMES_OLD_NORMALIZED_TRACE",
            completed.stdout,
        )
        self.assertIn(
            "PASS FIRST_SCALE_ONE_ERROR_IS_DOUBLE_TRANSVERSE_HALF",
            completed.stdout,
        )
        self.assertIn(
            "PASS G1_DMINUS_AND_COMPONENT_MAP_HAVE_NO_ADDITIONAL_HALF",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
