from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AbBaFullOneLoopQuotientRetractionExactTest(unittest.TestCase):
    def test_historical_retraction_and_exact_source_bindings(self) -> None:
        script = ROOT / "scripts/step5_ab_ba_full_1pi_quotient_exact_audit.py"
        artifact_path = ROOT / "audits/step5-ab-ba-full-1pi-quotient-exact.json"
        markdown_path = ROOT / "audits/step5-ab-ba-full-1pi-quotient-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["schema"],
            "step5-ab-ba-full-1pi-quotient-historical-retraction-exact-v2",
        )
        self.assertEqual(artifact["artifact_role"], "HISTORICAL_RETRACTION_REGRESSION")
        self.assertFalse(artifact["accepted_as_positive_derivation"])
        self.assertFalse(artifact["external_target_used_in_derivation"])
        self.assertFalse(artifact["holomorphic_twist_read"])
        self.assertFalse(artifact["project_result_engine_read"])

        sources = artifact["derivation_sources"]
        self.assertEqual(
            [item["path"] for item in sources],
            [
                "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json",
                "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json",
            ],
        )
        for source in sources:
            source_path = ROOT / source["path"]
            self.assertEqual(
                source["sha256"],
                hashlib.sha256(source_path.read_bytes()).hexdigest(),
            )

        retraction = artifact["historical_retraction"]
        self.assertEqual(retraction["original_full_measure_coefficient"], "4096")
        self.assertEqual(retraction["rejected_single_cycle_coefficient"], "2048")
        self.assertEqual(retraction["raw_multiplicity_scale"], "2")
        self.assertEqual(retraction["simplex_shape_sum"], "1")
        self.assertEqual(retraction["nonzero_supertrace_cycles"], 2)
        self.assertEqual(
            retraction["first_false_equality"],
            "(1/2)*(C1+C2) -> (1/2)*C1",
        )
        self.assertEqual(retraction["verdict"], "RETRACTED_FALSE_SCALE_ONE_NORMALIZATION")

        carrier = artifact["carrier_rebasing_and_finite_settlement"]
        self.assertEqual(
            carrier["raw_vector"],
            ["2", "2", "-1/3", "4/3", "-2*sqrt(2)*i", "2*sqrt(2)*i"],
        )
        self.assertEqual(
            carrier["rebased_vector"],
            ["0", "2", "1", "4/3", "-2*sqrt(2)*i", "2*sqrt(2)*i"],
        )
        self.assertEqual(
            carrier["common_TD_vector"],
            ["0", "1", "-2*sqrt(2)*i", "2*sqrt(2)*i"],
        )
        self.assertEqual(
            carrier["finite_normal_product_vector"],
            ["1", "0", "sqrt(2)*i", "-sqrt(2)*i"],
        )
        self.assertEqual(
            carrier["renormalized_vector"],
            ["1", "1", "-sqrt(2)*i", "sqrt(2)*i"],
        )
        self.assertEqual(carrier["renormalized_q_Ward"], ["0", "0", "0"])

        self.assertEqual(artifact["definitions"]["finite_master"], "1/(32*pi**2)")
        self.assertEqual(
            artifact["DRED_cutting_failure"]["four_d_square_plus_cut"],
            "(D_e+mu_l^2)/(D0*D1*D2)-1/prod_{j!=e}(D_j)=mu_l^2/(D0*D1*D2)",
        )
        self.assertEqual(artifact["checks"]["failed"], 0)
        self.assertEqual(artifact["checks"]["passed"], artifact["checks"]["count"])

        script_text = script.read_text(encoding="utf-8")
        self.assertNotIn("step5_project_anomaly_engine", script_text)
        self.assertNotIn("step5-ht-roundtrip-audit", script_text)

        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS HISTORICAL_RETRACTION", completed.stdout)
        self.assertIn(
            "PASS first false equality (1/2)*(C1+C2) -> (1/2)*C1",
            completed.stdout,
        )
        self.assertIn("PASS vraw -> vTD -> vren", completed.stdout)


if __name__ == "__main__":
    unittest.main()
