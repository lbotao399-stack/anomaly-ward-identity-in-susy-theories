from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5_propagators.py"
AUDIT = ROOT / "audits/step5-propagator-verification.json"


def load_verifier():
    specification = importlib.util.spec_from_file_location("verify_step5_propagators", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load Step-5 propagator verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5PropagatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_exact_verifier_is_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first = AUDIT.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = AUDIT.read_text(encoding="utf-8")
        self.assertEqual(first, second)
        audit = json.loads(first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["arithmetic"], "EXACT_Q_I_NO_FLOATING_POINT")
        self.assertEqual(audit["totals"], {"checks": 87, "failed": 0})

    def test_equations_5_37_through_5_40_at_three_exact_momenta(self) -> None:
        for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
            checks = self.verifier.operator_checks(momentum)
            self.assertTrue(all(checks.values()), (momentum, checks))
            operators = self.verifier.flat_operators(momentum)
            self.assertEqual(len(operators["identity"]), 16)
            self.assertEqual(len(operators["identity"][0]), 16)

    def test_vector_physical_hessian_and_step5a_fixed_gauge_inverse(self) -> None:
        for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
            checks = self.verifier.vector_checks(momentum)
            self.assertTrue(checks["physical_5_43"], momentum)
            self.assertTrue(checks["step5a_total_5_45"], momentum)
            self.assertTrue(checks["step5a_inverse_5_46_left"], momentum)
            self.assertTrue(checks["step5a_inverse_5_46_right"], momentum)

    def test_constrained_chiral_hessian_and_lowest_components(self) -> None:
        for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
            checks = self.verifier.chiral_checks(momentum)
            self.assertTrue(checks["chiral_embedding_annihilated_by_barD"], momentum)
            self.assertTrue(checks["antichiral_embedding_at_minus_p_annihilated_by_D"], momentum)
            self.assertTrue(checks["hessian_inverse_left"], momentum)
            self.assertTrue(checks["hessian_inverse_right"], momentum)
            self.assertTrue(checks["scalar_green_kernel"], momentum)
            self.assertTrue(checks["fermion_green_kernel"], momentum)
            self.assertTrue(checks["auxiliary_green_kernel"], momentum)

    def test_koszul_sign_is_part_of_the_fermion_check(self) -> None:
        momentum = (1, 2, 3, 4)
        pairing = self.verifier.chiral_pairing(momentum)
        hessian_inverse = self.verifier.inverse(self.verifier.scale(-1, pairing))
        epsilon_down = [[0, -1], [1, 0]]
        fermion_kernel = self.verifier.zeros(2, 2)
        for undotted in range(2):
            for dotted_lower in range(2):
                fermion_kernel[undotted][dotted_lower] = self.verifier.Fraction(1, 2) * sum(
                    (
                        hessian_inverse[1 + undotted][1 + dotted_upper]
                        * epsilon_down[dotted_lower][dotted_upper]
                        for dotted_upper in range(2)
                    ),
                    self.verifier.ZERO,
                )
        expected = self.verifier.scale(
            -self.verifier.I / self.verifier.momentum_square(momentum),
            self.verifier.sigma_e(momentum),
        )
        self.assertEqual(fermion_kernel, expected)

    def test_source_order_and_step5c_obligations_are_scoped(self) -> None:
        audit = self.verifier.run_verification()
        self.assertEqual(
            audit["admission_status"],
            "PHYSICAL_HESSIANS_AND_STEP5A_VECTOR_GREEN_VERIFIED",
        )
        self.assertIn(
            "J_Phi then tildeJ_Phi",
            audit["derived_rules"]["source_order"],
        )
        self.assertEqual(audit["typed_blockers"], [])
        blocker_ids = {entry["id"] for entry in audit["step5c_obligations"]}
        self.assertEqual(
            blocker_ids,
            {
                "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
                "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
                "BLOCKED_FP_GHOST_CYCLE_UNDECLARED",
                "BLOCKED_NK_BRANCH_AND_KERNEL_UNFIXED",
            },
        )
        self.assertTrue(all(self.verifier.fp_checks((1, 2, 3, 4)).values()))

    def test_no_external_propagator_or_anomaly_coefficient_is_adopted(self) -> None:
        audit = self.verifier.run_verification()
        boundary = audit["source_boundary"]
        self.assertFalse(boundary["weinberg_coefficients_used"])
        self.assertFalse(boundary["superspace_1001_coefficients_used"])
        self.assertFalse(boundary["anomaly_coefficient_computed"])


if __name__ == "__main__":
    unittest.main()
