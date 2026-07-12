from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5_seed_dalgebra.py"
AUDIT = ROOT / "audits/step5-seed-dalgebra-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
SOURCE_LEDGER = ROOT / "audits/step5-source-translation-ledger.json"


def load_verifier():
    specification = importlib.util.spec_from_file_location("verify_step5_seed_dalgebra", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load seed D-algebra verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5SeedDAlgebraTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_audit_is_byte_reproducible_and_hash_bound(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = AUDIT.read_bytes()
        self.assertEqual(first, second)
        audit = json.loads(first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 42, "failed": 0})
        self.assertEqual(audit["contract_sha256"], hashlib.sha256(CONTRACT.read_bytes()).hexdigest())
        self.assertEqual(
            audit["source_ledger_sha256"],
            hashlib.sha256(SOURCE_LEDGER.read_bytes()).hexdigest(),
        )

    def test_project_normalization_rejects_chat_d_factor(self) -> None:
        checks = self.verifier.project_coefficient_checks()
        self.assertTrue(all(checks.values()), checks)
        audit = self.verifier.run_verification()
        self.assertEqual(audit["derived"]["K_plus"], "-(1/8) D_+ barD^2 D_+")
        self.assertEqual(audit["derived"]["fixed_placement_D_factor"], "-1/2")
        self.assertIn("M3_DALGEBRA_CHAIN", audit["rejected_source_claims"])

    def test_closed_delta_and_mixed_anticommutators_are_exact_matrices(self) -> None:
        self.assertTrue(all(self.verifier.normalization_checks().values()))
        self.assertTrue(all(self.verifier.mixed_anticommutator_checks().values()))

    def test_vertex_momentum_magnitudes_retain_raw_sign(self) -> None:
        checks = self.verifier.routing_checks()
        self.assertTrue(all(checks.values()), checks)
        audit = self.verifier.run_verification()
        self.assertEqual(audit["derived"]["antichiral_raw_vertex_momentum"], "-(2k+q)")
        self.assertEqual(audit["derived"]["chiral_raw_vertex_momentum"], "2k+p+2q")

    def test_endpoint_transfer_keeps_opposite_momentum_labels(self) -> None:
        checks = self.verifier.endpoint_transfer_checks()
        self.assertEqual(len(checks), 12)
        self.assertTrue(all(checks.values()), checks)

    def test_rejected_slice_diagnostic_is_not_an_admitted_amplitude(self) -> None:
        self.assertTrue(all(self.verifier.rejected_slice_diagnostic_checks().values()))
        audit = self.verifier.run_verification()
        self.assertEqual(
            audit["admission_status"],
            "PROJECT_SEED_NORMALIZATION_AUDITED_NO_LOOP_AMPLITUDE_ADMITTED",
        )
        self.assertFalse(audit["anomaly_coefficient_computed"])
        self.assertEqual(audit["derived"]["rejected_slice_coefficient_magnitude"], "g^2/16")


if __name__ == "__main__":
    unittest.main()
