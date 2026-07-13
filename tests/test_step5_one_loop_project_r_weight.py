from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts import step5_one_loop_project_r_weight as module


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_project_r_weight.py"


class Step5OneLoopProjectRWeightTest(unittest.TestCase):
    def test_exact_Project_weight_chain(self) -> None:
        payload = module.build_payload()
        self.assertEqual(payload["status"], "PASS_PROJECT_U1R_BINDING")
        self.assertTrue(all(payload["checks"].values()))
        self.assertEqual(payload["weights"]["W_a"], 1)
        self.assertEqual(payload["weights"]["tilde_W_dot_a"], -1)
        self.assertEqual(payload["weights"]["X=nabla_plus_W_plus"], 0)
        self.assertEqual(payload["weights"]["I=nabla_minus_X_X"], -1)
        self.assertEqual(payload["weights"]["O_star=tildeW_Dcov_X"], -1)
        self.assertFalse(payload["external_results_imported"])

    def test_artifacts_are_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_generated = module.GENERATED.read_bytes()
        first_audit = module.AUDIT_JSON.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_generated, module.GENERATED.read_bytes())
        self.assertEqual(first_audit, module.AUDIT_JSON.read_bytes())
        audit = json.loads(first_audit)
        self.assertEqual(audit["status"], "PASS_PROJECT_U1R_BINDING")
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(first_generated).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
