#!/usr/bin/env python3

from __future__ import annotations

from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/step6_two_loop_grammar.py"
SPEC = importlib.util.spec_from_file_location("step6_two_loop_grammar", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
grammar = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = grammar
SPEC.loader.exec_module(grammar)


class Step6TwoLoopGrammarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = grammar.build_payload()
        cls.checks = grammar.exact_checks(cls.payload)

    def test_all_internal_checks_pass(self) -> None:
        self.assertTrue(all(self.checks.values()), [name for name, value in self.checks.items() if not value])

    def test_exact_qi_coefficients_through_v5(self) -> None:
        gamma = [term.coefficient.render() for term in grammar.gamma_terms()]
        w = [term.coefficient.render() for term in grammar.w_terms()]
        tilde_gamma = [term.coefficient.render() for term in grammar.tilde_gamma_terms()]
        tilde_w = [term.coefficient.render() for term in grammar.tilde_w_terms()]
        self.assertEqual(gamma, ["1", "-1/2*i", "-1/6", "1/24*i", "1/120"])
        self.assertEqual(w, ["-1/8", "1/16*i", "1/48", "-1/192*i", "-1/960"])
        self.assertEqual(tilde_gamma, ["-1", "-1/2*i", "1/6", "1/24*i", "-1/120"])
        self.assertEqual(tilde_w, ["-1/8", "-1/16*i", "1/48", "1/192*i", "-1/960"])
        for degree, term in enumerate(grammar.gamma_terms(), start=1):
            self.assertEqual(
                term.coefficient,
                grammar.QI(Fraction((-1) ** (degree - 1), grammar.factorial(degree)), degree - 1),
            )

    def test_x_counts_are_generated_by_flat_plus_ordered_connections(self) -> None:
        expected_coefficients = {
            1: ["-1/8"],
            2: ["1/16*i", "-1/8*i"],
            3: ["1/48", "-1/16", "-1/16"],
            4: ["-1/192*i", "1/48*i", "1/32*i", "1/48*i"],
            5: ["-1/960", "1/192", "1/96", "1/96", "1/192"],
        }
        for degree in range(1, 6):
            terms = grammar.x_terms_at_degree(degree)
            self.assertEqual(len(terms), 1 + len(range(1, degree)))
            self.assertEqual(sum("FLAT_DERIVATIVE" in term.tags for term in terms), 1)
            self.assertEqual(sum("COVARIANT_CONNECTION" in term.tags for term in terms), degree - 1)
            self.assertEqual(
                [term.coefficient.render() for term in terms],
                expected_coefficients[degree],
            )

    def test_insertion_counts_are_derived_from_compositions(self) -> None:
        derived: list[int] = []
        actual: list[int] = []
        for valence in range(2, 7):
            x_count = {degree: len(grammar.x_terms_at_degree(degree)) for degree in range(1, 6)}
            direct = sum(
                2 * x_count[left] * x_count[valence - left]
                for left in range(1, valence)
                if left in x_count and valence - left in x_count
            )
            outer = sum(
                2 * x_count[left] * x_count[valence - gamma_degree - left]
                for gamma_degree in range(1, valence - 1)
                for left in range(1, valence - gamma_degree)
                if gamma_degree <= 5
                and left in x_count
                and valence - gamma_degree - left in x_count
            )
            derived.append(direct + outer)
            terms = grammar.insertion_terms_at_valence(valence)
            actual.append(len(terms))
            direct_terms = [term for term in terms if "DIRECT_D_MINUS" in term.tags]
            outer_terms = [term for term in terms if "OUTER_NABLA_MINUS_CONNECTION" in term.tags]
            self.assertEqual(len(direct_terms), direct)
            self.assertEqual(len(outer_terms), outer)
        self.assertEqual(derived, [2, 10, 30, 70, 140])
        self.assertEqual(actual, derived)

    def test_both_dminus_and_outer_connection_placements(self) -> None:
        for valence in range(2, 7):
            terms = grammar.insertion_terms_at_valence(valence)
            direct_placements = {
                placement
                for placement in ("D_MINUS_LEFT", "D_MINUS_RIGHT")
                if any(placement in term.tags for term in terms)
            }
            self.assertEqual(direct_placements, {"D_MINUS_LEFT", "D_MINUS_RIGHT"})
            if valence >= 3:
                connection_placements = {
                    placement
                    for placement in ("OUTER_CONNECTION_LEFT", "OUTER_CONNECTION_RIGHT")
                    if any(placement in term.tags for term in terms)
                }
                self.assertEqual(
                    connection_placements,
                    {"OUTER_CONNECTION_LEFT", "OUTER_CONNECTION_RIGHT"},
                )

    def test_s3_through_s6_parallel_ordered_splits(self) -> None:
        actions = grammar.action_terms()
        for valence in range(3, 7):
            plus = actions[f"S{valence}_PLUS"]
            minus = actions[f"S{valence}_MINUS"]
            expected_splits = [(left, valence - left) for left in range(1, valence)]
            self.assertEqual(len(plus), len(expected_splits))
            self.assertEqual(len(minus), len(expected_splits))
            self.assertEqual(
                [term.term_id for term in plus],
                [f"S{valence}_PLUS_{left}_{right}" for left, right in expected_splits],
            )
            self.assertEqual(
                [term.term_id for term in minus],
                [f"S{valence}_MINUS_{left}_{right}" for left, right in expected_splits],
            )
            self.assertTrue(all(term.measure == "E_PLUS_CHIRAL" for term in plus))
            self.assertTrue(all(term.measure == "E_MINUS_ANTICHIRAL" for term in minus))

    def test_euler_counts_are_derived(self) -> None:
        e_xi = grammar.e_xi_gauge_terms()
        e_xi_by_degree = {
            degree: sum(term.total_v_degree == degree for term in e_xi)
            for degree in range(1, 6)
        }
        for degree in range(1, 6):
            self.assertEqual(e_xi_by_degree[degree], 2 * len(grammar.x_terms_at_degree(degree)))
        derived_e_xi = sum(e_xi_by_degree.values())
        self.assertEqual(derived_e_xi, 30)
        e_v = grammar.e_v_project_terms()
        derived_e_v = sum(e_xi_by_degree[degree] * (6 - degree) for degree in range(1, 6))
        self.assertEqual(derived_e_v, 70)
        self.assertEqual(len(e_v), derived_e_v)

    def test_term_metadata_contains_typed_ports_and_provenance(self) -> None:
        groups = (
            grammar.gamma_terms(),
            grammar.w_terms(),
            grammar.tilde_gamma_terms(),
            grammar.tilde_w_terms(),
            grammar.x_terms(),
            *(grammar.insertion_terms_at_valence(n) for n in range(2, 7)),
            *(grammar.action_terms_at_valence(n, sector) for n in range(3, 7) for sector in ("PLUS", "MINUS")),
            grammar.e_xi_gauge_terms(),
            grammar.e_v_project_terms(),
        )
        for term in grammar.flatten_term_groups(groups):
            row = term.as_json()
            self.assertEqual(row["status"], grammar.STATUS)
            self.assertEqual(row["coefficient"]["field"], "Q(i)")
            self.assertEqual(len(row["ports"]), row["degree"]["total_v"])
            self.assertIn(row["parity"], (0, 1))
            self.assertTrue(row["measure"])
            self.assertTrue(row["color_ast"])
            self.assertTrue(row["source_equations"])

    def test_background_quantum_assignment_exposes_t_b_q(self) -> None:
        term = grammar.insertion_terms_at_valence(6)[0]
        assignments = grammar.background_quantum_assignments(term)
        self.assertEqual(len(assignments), 2**6)
        observed = set()
        for row in assignments:
            degree = row["degree"]
            self.assertEqual(degree["total_v"], degree["background_v"] + degree["quantum_v"])
            self.assertTrue(degree["identity_check"])
            observed.add((degree["total_v"], degree["background_v"], degree["quantum_v"]))
            self.assertEqual(row["external_projection"], grammar.EXTERNAL_PROJECTION_STATUS)
        self.assertEqual(observed, {(6, background, 6 - background) for background in range(7)})

    def test_external_projection_fails_closed(self) -> None:
        assignment = grammar.background_quantum_assignments(grammar.gamma_terms(1)[0])[0]
        with self.assertRaisesRegex(
            grammar.ExternalProjectionBlocked,
            grammar.EXTERNAL_PROJECTION_STATUS,
        ):
            grammar.project_external_assignment(assignment, ("X_EXTERNAL",))

    def test_generated_outputs_match_proposal_gate(self) -> None:
        payload_path = ROOT / "generated/step6/two-loop-grammar/project-two-loop-grammar.json"
        audit_path = ROOT / "audits/step6-two-loop-grammar-verification.json"
        payload = json.loads(payload_path.read_text())
        audit = json.loads(audit_path.read_text())
        self.assertEqual(payload["status"], grammar.STATUS)
        self.assertEqual(payload["result_products"], [])
        self.assertEqual(audit["status"], grammar.STATUS)
        self.assertEqual(audit["failed"], 0)
        self.assertEqual(audit["passed"], len(audit["checks"]))


if __name__ == "__main__":
    unittest.main()
