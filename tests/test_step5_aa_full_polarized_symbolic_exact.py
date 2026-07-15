import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "audits" / "step5-aa-full-polarized-symbolic-exact.json"


class FullPolarizedAASymbolicAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_all_exact_checks_pass(self):
        self.assertEqual(self.artifact["status"], "PASS")
        self.assertEqual(len(self.artifact["checks"]), 15)
        self.assertTrue(all(self.artifact["checks"].values()))

    def test_full_vertex_is_not_fixed_strength_vertex(self):
        full = self.artifact["full_polarization"]
        self.assertNotEqual(
            full["full_numerator"],
            full["fixed_field_strength_numerator"],
        )
        self.assertNotEqual(full["full_minus_fixed"], "0")

    def test_selected_edges_divide_exactly(self):
        selected = self.artifact["selected"]
        self.assertEqual(selected["e0_remainder"], "0")
        self.assertEqual(selected["e2_remainder"], "0")
        self.assertEqual(selected["quadratic_trace_e0"], "0")
        self.assertEqual(selected["quadratic_trace_e2"], "0")
        self.assertEqual(
            selected["e0_quotient"],
            "-l0**2/2 + I*l0*l1 + 3*l0/2 - I*l0 + l1**2/2 - l1 - 3*I*l1/2 - 1/2 + 3*I/2",
        )
        self.assertEqual(
            selected["e2_quotient"],
            "-l0**2/2 + I*l0*l1 - l0/2 + l1**2/2 + I*l1/2",
        )

    def test_contacts_leave_only_mu_squared(self):
        contact = self.artifact["induced_contact"]
        self.assertEqual(contact["identity_e0_remainder"], "0")
        self.assertEqual(contact["identity_e2_remainder"], "0")

    def test_finite_simplex_average(self):
        simplex = self.artifact["finite_simplex"]
        self.assertEqual(simplex["average_q0"], "-1/2 + 5*I/12")
        self.assertEqual(simplex["average_q2"], "7*I/12")
        self.assertEqual(simplex["average_sum"], "-1/2 + I")


if __name__ == "__main__":
    unittest.main()
