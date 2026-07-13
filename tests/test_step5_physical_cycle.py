from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5_physical_cycle.py"
AUDIT = ROOT / "audits/step5-physical-cycle-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"


def load_verifier():
    specification = importlib.util.spec_from_file_location("verify_step5_physical_cycle", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load physical-cycle verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5PhysicalCycleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_exact_audit_is_reproducible_and_hash_bound(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first = AUDIT.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = AUDIT.read_text(encoding="utf-8")
        self.assertEqual(first, second)
        audit = json.loads(first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 23, "failed": 0})
        self.assertEqual(
            audit["contract_sha256"],
            hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        )

    def test_bosonic_cycle_has_positive_convergent_quadratic_forms(self) -> None:
        checks = self.verifier.bosonic_cycle_checks()
        self.assertTrue(all(checks.values()), checks)
        audit = self.verifier.run_verification()
        reality = audit["physical_cycle"]["momentum_reality"]
        self.assertIn("tildephi^A(-p)=(phi^A(p))^dagger", reality)
        self.assertIn("tildeF^A(-p)=-(F^A(p))^dagger", reality)
        self.assertIn("A_m^A(-p)=(A_m^A(p))^dagger", reality)
        self.assertIn("D^A(p)=i d^A(p), d^A(-p)=(d^A(p))^dagger", reality)

    def test_finite_berezin_gaussian_fixes_source_order_and_signs(self) -> None:
        result = self.verifier.normalized_fermion_gaussian()
        self.assertTrue(result["normalized_generator_exact"])
        self.assertTrue(result["vacuum_nonzero"])
        self.assertTrue(all(result["derivative_checks"].values()))
        audit = self.verifier.run_verification()
        cycle = audit["physical_cycle"]
        self.assertEqual(
            cycle["fermion_measure_order"],
            "dtildepsi_dot- dtildepsi_dot+ dpsi_- dpsi_+",
        )
        self.assertEqual(
            cycle["fermion_source_coupling"],
            "-rho psi - tildepsi tilderho",
        )
        self.assertIn("both derivatives are LEFT", cycle["fermion_source_derivative_order"])
        self.assertIn("first d/drho", cycle["fermion_source_derivative_order"])

    def test_chiral_green_kernels_are_reference_flat_wick_rules(self) -> None:
        audit = self.verifier.run_verification()
        self.assertEqual(
            audit["admission_status"],
            "REFERENCE_FLAT_CHIRAL_AND_STEP5A_VECTOR_GAUSSIAN_VERIFIED",
        )
        contractions = audit["reference_flat_wick_rules"]
        self.assertEqual(
            contractions["scalar"],
            "<phi^A(p) tildephi^B(-p)>=hbar g^2 kappa^{AB}/p_(4)^2",
        )
        self.assertEqual(
            contractions["fermion"],
            "<psi_a^A(p) tildepsi_dotb^B(-p)>=-i hbar g^2 kappa^{AB} p_(a dotb)/p_(4)^2",
        )
        self.assertEqual(
            contractions["auxiliary"],
            "<F^A(p) tildeF^B(-p)>=-hbar g^2 kappa^{AB}",
        )
        self.assertTrue(contractions["fermion_reverse_order"].startswith("<tildepsi"))

    def test_vector_transverse_and_full_step5a_wick_rule_are_separated_from_step5c(self) -> None:
        checks = self.verifier.transverse_vector_checks()
        self.assertTrue(all(checks.values()), checks)
        audit = self.verifier.run_verification()
        self.assertIn("vector", audit["reference_flat_wick_rules"])
        pseudoinverse = audit["algebraic_pseudoinverses"]
        self.assertIn("Pi_(1/2)", pseudoinverse["vector_transverse"])
        self.assertTrue(pseudoinverse["not_a_finite_cycle_reconstruction"])
        self.assertEqual(audit["typed_blockers"], [])
        self.assertEqual(
            [entry["id"] for entry in audit["step5c_obligations"]],
            [
                "BLOCKED_GAUGE_FIXED_DENSITY_BEREZINIAN",
                "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
                "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
            ],
        )

    def test_fp_nk_and_anomaly_sectors_are_untouched(self) -> None:
        audit = self.verifier.run_verification()
        self.assertEqual(
            audit["untouched_sectors"],
            {"FP_cycle": "NOT_READ_OR_MODIFIED", "NK_cycle": "NOT_READ_OR_MODIFIED"},
        )
        self.assertFalse(audit["source_boundary"]["external_propagator_coefficients_used"])
        self.assertFalse(audit["source_boundary"]["anomaly_coefficient_computed"])
        self.assertFalse(audit["source_boundary"]["full_density_used_in_gaussian"])


if __name__ == "__main__":
    unittest.main()
