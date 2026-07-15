from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_aa_gauge_raw_convolution_hessian_exact_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location("aa_raw_convolution", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load AA raw-convolution audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AAGaugeRawConvolutionHessianExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_raw_word_and_route_counts(self) -> None:
        self.assertEqual(
            self.payload["status"],
            "REJECTED_FIXED_FIELD_STRENGTH_SLOT_ONLY__SUPERSEDED_BY_FULL_POLARIZED_SYMBOLIC_AUDIT",
        )
        self.assertEqual(
            self.payload["target_blind_ordered_result"]["physical_status"],
            "REJECTED_AS_FULL_AA_RESULT",
        )
        self.assertEqual(self.payload["raw_cubic_words"]["rows_per_chirality"], 24)
        self.assertEqual(self.payload["raw_cubic_words"]["all_rows"], 48)
        self.assertEqual(self.payload["route_collapse"]["authority_structural_TGG_routes"], 36)
        self.assertEqual(self.payload["route_collapse"]["authority_marked_occurrences"], 72)
        self.assertEqual(self.payload["route_collapse"]["post_hessian_route_multiplier"], 1)

    def test_occurrence_sd_map_and_extended_vector(self) -> None:
        rows = self.payload["d_algebra"]["contact_rows"]
        self.assertEqual(len(rows), 16)
        self.assertTrue(all(row["same_occurrence"] and row["same_edge"] for row in rows))
        self.assertEqual(
            self.payload["target_blind_ordered_result"]["vector_in_lambda1_units"],
            ["1/48", "-1/48", "-1/48", "1/48"],
        )
        self.assertEqual(
            self.payload["target_blind_ordered_result"]["compact_DA_AD_vector"],
            ["UNDEFINED", "UNDEFINED"],
        )

    def test_cli_check(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("SUMMARY 16/16 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
