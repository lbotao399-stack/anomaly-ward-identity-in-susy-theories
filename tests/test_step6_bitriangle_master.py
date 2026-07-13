from fractions import Fraction
import unittest

from scripts import step6_bitriangle_master as master


class Step6BitriangleMasterTests(unittest.TestCase):
    def test_elementary_integrals(self) -> None:
        self.assertEqual(master.integral_zero_one_power(5), Fraction(1, 6))
        self.assertEqual(
            master.integral_one_infinity_inverse_power(7), Fraction(1, 6)
        )
        self.assertEqual(
            master.integral_one_infinity_log_inverse_power(7), Fraction(1, 36)
        )

    def test_elementary_integral_domains_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            master.integral_zero_one_power(-1)
        with self.assertRaises(ValueError):
            master.integral_one_infinity_inverse_power(1)
        with self.assertRaises(ValueError):
            master.integral_one_infinity_log_inverse_power(1)

    def test_radial_mode_formula(self) -> None:
        for n in range(12):
            row = master.radial_mode(n)
            self.assertEqual(row["R_n"], str(Fraction(3, 2 * (n + 1) ** 2)))

    def test_mode_coefficient(self) -> None:
        for n in range(12):
            row = master.mode_contribution(n)
            self.assertEqual(
                row["coefficient_of_pi4"], str(Fraction(6, (n + 1) ** 3))
            )

    def test_source_graph_and_routing(self) -> None:
        graph = master.source_graph()
        self.assertEqual(graph["graph_id"], master.GRAPH_ID)
        self.assertEqual(
            graph["denominator_ast"]["rendered"],
            "k^2 (k-P)^2 l^2 (l-P)^2 (k-l)^2",
        )

    def test_payload_exact_result_and_boundary(self) -> None:
        payload = master.build_payload()
        self.assertEqual(
            payload["normalized_result"], "6*zeta(3)/((4*pi)^4*P^2)"
        )
        self.assertFalse(payload["external_result_used_as_input"])
        self.assertIsNone(payload["fail_closed"]["two_loop_anomaly_coefficient"])

    def test_audit(self) -> None:
        payload = master.build_payload()
        audit = master.build_audit(payload)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["passed"], audit["total"])


if __name__ == "__main__":
    unittest.main()
