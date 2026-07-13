from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5a_fixed_kernel.py"
AUDIT = ROOT / "audits/step5a-fixed-kernel.json"


def load_verifier():
    specification = importlib.util.spec_from_file_location("verify_step5a_fixed_kernel", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load Step-5A fixed-kernel verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5AFixedKernelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_verifier_is_exact_and_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first = AUDIT.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = AUDIT.read_text(encoding="utf-8")
        self.assertEqual(first, second)
        audit = json.loads(first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["admission_status"], "STEP5A_WICK_KERNEL_ADMITTED")
        self.assertEqual(audit["arithmetic"], "EXACT_Q_I_NO_FLOATING_POINT")
        self.assertEqual(audit["totals"], {"checks": 36, "failed": 0})

    def test_two_sided_16_by_16_and_color_inverses(self) -> None:
        for momentum in self.verifier.MOMENTA:
            checks = self.verifier.fixed_kernel_checks(momentum)
            self.assertTrue(all(checks.values()), (momentum, checks))
            matrices = self.verifier.fixed_kernel(momentum)
            self.assertEqual(matrices["K_G"], self.verifier.identity(16))
            self.assertEqual(matrices["G_K"], self.verifier.identity(16))

    def test_reference_flat_measure_is_scoped_only_to_5A(self) -> None:
        audit = self.verifier.run_verification()
        measure = audit["perturbative_measure"]
        self.assertEqual(measure["value"], "0")
        self.assertEqual(measure["scope"], "REFERENCE_FLAT_STEP5A_ONLY")
        self.assertIn("NOT_CLAIMED", measure["finite_BV_density_equality"])


if __name__ == "__main__":
    unittest.main()
