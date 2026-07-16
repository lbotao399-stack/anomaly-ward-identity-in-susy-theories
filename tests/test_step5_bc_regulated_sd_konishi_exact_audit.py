from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5BcRegulatedSdKonishiExactTest(unittest.TestCase):
    def test_generated_artifact_and_validator(self) -> None:
        script = ROOT / "scripts/step5_bc_full_family_raw_projection_audit.py"
        artifact_path = ROOT / "audits/step5-bc-full-family-raw-projection-exact.json"
        markdown_path = ROOT / "audits/step5-bc-full-family-raw-projection-exact.md"

        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["status"],
            "PASS_BC_CB_REGULATED_SD_KONISHI_EXACT",
        )
        self.assertFalse(artifact["external_target_used"])
        self.assertEqual(
            artifact["cutting_failure"]["full_d_zero"],
            "r_(e,d)^2/(D0*D1*D2)-1/(D1*D2)=0",
        )
        self.assertEqual(
            artifact["cutting_failure"]["regulated_kernel"],
            "mu_loop^2/(D0*D1*D2)",
        )
        self.assertEqual(
            artifact["cutting_failure"]["master"],
            "1/(32*pi^2)",
        )
        self.assertEqual(
            artifact["ordered_results"]["B_r>C_s"],
            "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
        )
        self.assertEqual(
            artifact["ordered_results"]["C_s>B_r"],
            "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
        )
        self.assertEqual(artifact["blockers"], [])
        self.assertEqual(artifact["summary"], {"checks": 84, "failed": 0, "passed": 84})
        self.assertEqual(
            artifact["covariant_source_expansion"]["order_V2_orbit"],
            [
                "I0 with (1/2!)*M1*M1: triangle parent",
                "I1 with M1: nonlinear-source/collapsed contact",
                "I0 with M2: matter seagull",
                "I2: source seagull/tadpole contact",
            ],
        )
        self.assertEqual(
            artifact["normalization_trace"]["final"],
            "+2*hbar*g^2*(1/(32*pi^2))=+lambda1",
        )

        occurrence_ids = [row["id"] for row in artifact["occurrence_orbit"]]
        self.assertEqual(
            occurrence_ids,
            [
                "BC-E-KIN",
                "BC-E-POT",
                "BC-X-POT",
                "CB-E-KIN",
                "CB-E-POT",
                "CB-X-POT",
            ],
        )
        self.assertIn(
            "no mixed boson-fermion propagator occurs in the Jacobian orbit",
            artifact["why_old_component_zero_does_not_apply"],
        )

        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("84/84 PASS", completed.stdout)
        self.assertIn("PASS_BC_CB_REGULATED_SD_KONISHI_EXACT", completed.stdout)


if __name__ == "__main__":
    unittest.main()
