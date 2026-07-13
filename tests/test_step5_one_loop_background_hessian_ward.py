from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_one_loop_background_hessian_ward import (
    AUDIT_JSON,
    AUDIT_MD,
    GENERATED,
    build_payload,
    covariance_witness,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_background_hessian_ward.py"


class Step5OneLoopBackgroundHessianWardTest(unittest.TestCase):
    def test_raw_hessian_and_endomorphism_tensor_types_are_distinct(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["equations"]["raw_hessian"], "K'=R^(-st) K R^(-1)")
        self.assertEqual(payload["equations"]["endomorphism"], "H'=R H R^(-1); H=Omega^(-1) K")

    def test_exact_nonorthogonal_covariance_witness(self) -> None:
        witness = covariance_witness()
        self.assertTrue(all(witness["checks"].values()), witness)

    def test_functional_pass_does_not_claim_graphir_or_frame_measure_pass(self) -> None:
        payload = build_payload()
        self.assertEqual(
            payload["verdicts"]["functional_background_hessian_covariance"], "PASS"
        )
        self.assertEqual(
            payload["verdicts"]["vertex_by_vertex_graphir_intertwining"],
            "OPEN_COMPILER_REPLAY",
        )
        self.assertEqual(
            payload["verdicts"]["full_chiral_vector_measure_bridge"], "OPEN"
        )
        self.assertEqual(payload["verdicts"]["anomaly_coefficient"], "NOT_ACCEPTED")

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_generated = GENERATED.read_bytes()
        first_audit = AUDIT_JSON.read_bytes()
        first_markdown = AUDIT_MD.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_generated, GENERATED.read_bytes())
        self.assertEqual(first_audit, AUDIT_JSON.read_bytes())
        self.assertEqual(first_markdown, AUDIT_MD.read_bytes())
        audit = json.loads(first_audit)
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(first_generated).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
