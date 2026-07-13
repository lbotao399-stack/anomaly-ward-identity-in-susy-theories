from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_spin_projector.py"
SPEC = importlib.util.spec_from_file_location("step5_one_loop_spin_projector", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Step5OneLoopSpinProjectorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.certificate = MODULE.build_certificate()

    def test_epsilon_contractions_are_exact(self) -> None:
        checks = self.certificate["checks"]
        self.assertTrue(checks["epsilon_up_down_is_identity"])
        self.assertTrue(checks["epsilon_down_up_is_identity"])
        self.assertTrue(checks["epsilon_first_slot_is_minus_identity"])
        self.assertTrue(checks["epsilon_ab_epsilon_ab_is_minus_two"])
        self.assertEqual(
            self.certificate["eom_trace_separation"]["direct_epsilon_trace"],
            "epsilon^{ab}M_ab=-E",
        )

    def test_trace_embedding_is_a_right_inverse(self) -> None:
        trace = MODULE.trace_matrix()
        embedding = MODULE.trace_embedding_matrix()
        self.assertEqual(
            MODULE.matrix_multiply(trace, embedding), MODULE.identity_matrix(4)
        )
        self.assertEqual(MODULE.matrix_rank(trace), 4)
        self.assertEqual(MODULE.matrix_rank(embedding), 4)

    def test_exact_direct_sum_projectors(self) -> None:
        trace = MODULE.trace_matrix()
        embedding = MODULE.trace_embedding_matrix()
        p_three = MODULE.matrix_multiply(embedding, trace)
        p_five = MODULE.matrix_add(
            MODULE.identity_matrix(10), MODULE.matrix_scale(Fraction(-1), p_three)
        )
        self.assertEqual(MODULE.matrix_rank(p_five), 6)
        self.assertEqual(MODULE.matrix_rank(p_three), 4)
        self.assertEqual(MODULE.matrix_add(p_five, p_three), MODULE.identity_matrix(10))
        self.assertEqual(
            MODULE.matrix_multiply(p_five, p_three), MODULE.zero_matrix(10, 10)
        )
        self.assertEqual(
            MODULE.matrix_multiply(p_three, p_five), MODULE.zero_matrix(10, 10)
        )

    def test_trace_free_projector_is_total_symmetrization(self) -> None:
        trace = MODULE.trace_matrix()
        embedding = MODULE.trace_embedding_matrix()
        p_five = MODULE.matrix_add(
            MODULE.identity_matrix(10),
            MODULE.matrix_scale(Fraction(-1), MODULE.matrix_multiply(embedding, trace)),
        )
        self.assertEqual(p_five, MODULE.full_symmetrizer_matrix())
        self.assertEqual(
            MODULE.matrix_multiply(trace, p_five), MODULE.zero_matrix(4, 10)
        )

    def test_minus_plus4_component_formula(self) -> None:
        component = self.certificate["component_formula"]
        self.assertEqual(component["t_+++"], "B-A")
        self.assertEqual(component["H_-++++"], "(1/5)A+(4/5)B")
        self.assertEqual(component["identity"], "U_-;++++=H_-++++-(4/5)t_+++")
        self.assertEqual(component["chiral_closure"], "H_-++++=0")
        self.assertEqual(component["closed_identity"], "U_-;++++=-(4/5)t_+++")
        self.assertTrue(self.certificate["checks"]["u_minus_plus4_reconstruction"])

    def test_seed_is_reducible_at_weight_three_halves(self) -> None:
        component = self.certificate["component_formula"]
        self.assertEqual(component["left_weight"], "3/2")
        self.assertEqual(
            {entry["j_L"] for entry in component["irreducible_content"]},
            {"5/2", "3/2"},
        )

    def test_candidate_is_sym3_highest_component(self) -> None:
        candidate = self.certificate["anomaly_candidate_spin_type"]
        self.assertEqual(candidate["representation"], "Sym^3 S_L")
        self.assertEqual(candidate["j_L"], "3/2")
        self.assertEqual(
            candidate["highest_component"],
            "C_+++=tildeW_dotalpha D_+^dotalpha X_++",
        )
        self.assertEqual(candidate["highest_weight"], "3/2")

    def test_chiral_bianchi_identity_is_six_term_exact_zero(self) -> None:
        polynomial, raw_count = MODULE.chiral_bianchi_polynomial()
        self.assertEqual(raw_count, 6)
        self.assertEqual(polynomial, {})
        self.assertTrue(self.certificate["checks"]["chiral_bianchi_reduces_to_zero"])

    def test_nested_and_direct_symmetrizers_are_identical(self) -> None:
        direct = MODULE.direct_five_symmetrizer_polynomial()
        nested = MODULE.nested_four_then_five_symmetrizer_polynomial()
        self.assertEqual(nested, direct)
        self.assertEqual(sum(direct.values(), Fraction(0)), Fraction(1))

    def test_rank_five_tensor_vanishes_with_open_color_order(self) -> None:
        derivative_on_a, derivative_on_b, raw_count, order_preserved = (
            MODULE.h_leibniz_polynomials()
        )
        self.assertEqual(raw_count, 480)
        self.assertEqual(derivative_on_a, {})
        self.assertEqual(derivative_on_b, {})
        self.assertTrue(order_preserved)
        self.assertEqual(
            self.certificate["rank_five_closure"]["status"], "CLOSED_EXACT"
        )

    def test_spin_five_halves_gate_is_closed_exactly(self) -> None:
        gate = self.certificate["spin_five_halves_gate"]
        self.assertEqual(gate["status"], "CLOSED_EXACT")
        self.assertEqual(gate["identity"], "H_abcde=0")
        self.assertEqual(gate["seed_consequence"], "H_-++++=0")
        self.assertEqual(self.certificate["certificate_status"], "PASS")

    def test_project_eom_derivative_rewrite_is_exact(self) -> None:
        left, right = MODULE.project_eom_derivative_polynomial()
        self.assertEqual(left, right)
        identity = self.certificate["tree_level_eom_identity"]
        self.assertEqual(identity["status"], "CLOSED_EXACT_AT_TREE_LEVEL")
        self.assertEqual(
            identity["derivation"][-1],
            "nabla_+E=-nabla_-nabla_+W_+=-nabla_-X_++",
        )

    def test_tree_eom_insertion_rewrite_preserves_open_order(self) -> None:
        raw, rewritten, stated = MODULE.tree_eom_insertion_polynomials()
        self.assertEqual(
            raw,
            {
                ("A:nabla_-X", "B:X"): Fraction(1),
                ("A:X", "B:nabla_-X"): Fraction(1),
            },
        )
        self.assertEqual(rewritten, stated)
        self.assertEqual(
            self.certificate["tree_level_eom_identity"]["closed_identity"],
            "I^AB=-(nabla_+E^A)X^B-X^A(nabla_+E^B)",
        )
        self.assertTrue(
            self.certificate["checks"][
                "tree_eom_insertion_preserves_open_a_before_b_order"
            ]
        )

    def test_quantum_contact_and_cohomology_gates_remain_open(self) -> None:
        gates = self.certificate["quantum_gates"]
        self.assertEqual(gates["status"], "OPEN")
        self.assertEqual(gates["t_cohomology_triviality"], "OPEN_NOT_DERIVED")
        self.assertEqual(gates["full_n4_eom_ideal_membership"], "OPEN_NOT_DERIVED")
        self.assertEqual(
            gates["renormalized_contact_anomaly_coefficient"], "OPEN_NOT_COMPUTED"
        )

    def test_artifact_and_audit_round_trip(self) -> None:
        artifact, audit = MODULE.write_outputs(ROOT)
        artifact_payload = json.loads(artifact.read_text())
        audit_payload = json.loads(audit.read_text())
        self.assertEqual(artifact_payload["certificate_status"], "PASS")
        self.assertEqual(
            audit_payload["overall_status"], "PASS_WITH_OPEN_QUANTUM_GATES"
        )
        self.assertEqual(audit_payload["spin_five_halves_gate_status"], "CLOSED_EXACT")
        self.assertEqual(
            audit_payload["tree_level_eom_identity_status"],
            "CLOSED_EXACT_AT_TREE_LEVEL",
        )
        self.assertEqual(audit_payload["quantum_gate_status"], "OPEN")
        self.assertEqual(
            audit_payload["passed_check_count"], audit_payload["check_count"]
        )


if __name__ == "__main__":
    unittest.main()
