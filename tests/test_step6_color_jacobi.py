from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import step6_color_jacobi as jacobi
from scripts import step6_color_tensor as color


class Step6ColorJacobiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.audit = jacobi.write_outputs()

    def test_audit_passes(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["totals"]["failed"], 0)
        self.assertGreaterEqual(self.audit["totals"]["checks"], 10)

    def test_jacobi_three_term_fixture_reduces_exactly_to_zero(self):
        result = jacobi.canonicalize_expression(jacobi.jacobi_three_term_fixture())
        self.assertTrue(result["zero_in_jacobi_quotient"])
        self.assertEqual(result["normal_form"], [])
        self.assertEqual(result["orbit"]["basis_network_count"], 3)
        self.assertEqual(result["orbit"]["relation_count"], 1)
        self.assertEqual(result["relation_matrix_rank"], 1)

    def test_metric_bridged_jacobi_reduces_exactly_to_zero(self):
        result = jacobi.canonicalize_expression(
            jacobi.metric_bridged_jacobi_fixture()
        )
        self.assertTrue(result["zero_in_jacobi_quotient"])
        self.assertEqual(result["normal_form"], [])
        self.assertTrue(
            any(
                relation["bridge_metric_positions"]
                for relation in result["orbit"]["relations"]
            )
        )

    def test_oriented_rewrite_strictly_decreases_basis_key(self):
        result = jacobi.canonicalize_expression(jacobi.jacobi_three_term_fixture()[:1])
        for rule in result["rewrite_rules"]:
            pivot = rule["pivot_canonical_graph_serialization"]
            self.assertTrue(
                all(
                    term["canonical_graph_serialization"] < pivot
                    for term in rule[
                        "replacement_canonical_graph_serializations"
                    ]
                )
            )
            self.assertTrue(rule["all_replacement_keys_strictly_smaller"])

    def test_each_IHX_relation_has_exact_integer_coefficients(self):
        result = jacobi.canonicalize_expression(jacobi.jacobi_three_term_fixture()[:1])
        relation = result["orbit"]["relations"][0]["canonical_relation"]
        self.assertEqual(len(relation), 3)
        self.assertTrue(
            all(term["coefficient"]["denominator"] == 1 for term in relation)
        )
        self.assertEqual(
            {abs(term["coefficient"]["numerator"]) for term in relation}, {1}
        )

    def test_antisymmetry_sign_is_preserved_before_jacobi(self):
        original = {"coefficient": 1, "network": [jacobi.c("A", "B", "x"), jacobi.c("x", "R", "S")]}
        swapped = {"coefficient": 1, "network": [jacobi.c("B", "A", "x"), jacobi.c("x", "R", "S")]}
        left = jacobi.canonicalize_expression([original])
        right = jacobi.canonicalize_expression([swapped])
        self.assertEqual(
            [
                (term["basis_key"], term["coefficient"]["numerator"], term["coefficient"]["denominator"])
                for term in left["normal_form"]
            ],
            [
                (term["basis_key"], -term["coefficient"]["numerator"], term["coefficient"]["denominator"])
                for term in right["normal_form"]
            ],
        )

    def test_metric_contraction_occurs_before_jacobi(self):
        normalized = jacobi.normalize_network(jacobi.metric_contraction_fixture())
        self.assertEqual(normalized.metric_rewrite_count, 1)
        self.assertIsNotNone(normalized.basis)
        assert normalized.basis is not None
        self.assertFalse(
            any(tensor["kind"].startswith("kappa") for tensor in normalized.basis.tensors)
        )

    def test_full_color_compiler_canonical_schema_is_accepted(self):
        raw = [jacobi.c("A", "B", "x"), jacobi.c("x", "R", "S")]
        upstream = color.canonicalize_network(
            raw,
            fixed_indices=jacobi.FREE_INDEX_ORDER,
            antisymmetry=True,
        )
        adapted = jacobi.normalize_network(upstream)
        direct = jacobi.normalize_network(raw)
        self.assertEqual(adapted.coefficient, direct.coefficient)
        self.assertIsNotNone(adapted.basis)
        self.assertIsNotNone(direct.basis)
        assert adapted.basis is not None and direct.basis is not None
        self.assertEqual(adapted.basis.key, direct.basis.key)
        self.assertEqual(
            adapted.input_adapter["schema"],
            "STEP6_COLOR_COMPILER_CANONICAL_NETWORK",
        )

        metric_raw = jacobi.metric_bridged_jacobi_fixture()[0]["network"]
        metric_upstream = color.canonicalize_network(
            metric_raw,
            fixed_indices=jacobi.FREE_INDEX_ORDER,
            antisymmetry=True,
        )
        metric_adapted = jacobi.normalize_network(metric_upstream)
        self.assertIsNotNone(metric_adapted.basis)
        assert metric_adapted.basis is not None
        edges = jacobi.internal_c_edges(metric_adapted.basis)
        self.assertEqual(len(edges), 1)
        self.assertEqual(len(edges[0]["bridge_metric_positions"]), 1)

    def test_square_graph_critical_pairs_all_join(self):
        rows = jacobi.critical_pair_certificates(jacobi.square_critical_fixture())
        self.assertGreaterEqual(len(rows), 4)
        for row in rows:
            self.assertTrue(row["joinable"])
            self.assertEqual(row["left_normal_form"], row["right_normal_form"])
            self.assertEqual(row["left_normal_form"], row["source_normal_form"])

    def test_rref_normal_form_is_idempotent(self):
        terms = jacobi.jacobi_three_term_fixture()[:1]
        result = jacobi.canonicalize_expression(terms)
        orbit_networks = {
            row["basis_key"]: row for row in result["orbit"]["basis_networks"]
        }
        reconstructed = [
            {
                "coefficient": term["coefficient"],
                "network": {
                    "canonical_tensors": orbit_networks[term["basis_key"]]["canonical_tensors"],
                    "overall_antisymmetry_sign": 1,
                    "zero_by_antisymmetry": False,
                },
            }
            for term in result["normal_form"]
        ]
        second = jacobi.canonicalize_expression(reconstructed)
        self.assertEqual(second["normal_form"], result["normal_form"])

    def test_exact_fraction_parser_rejects_float_and_symbolic_atoms(self):
        with self.assertRaises(jacobi.ColorInputError):
            jacobi.parse_fraction(0.5)
        with self.assertRaises(jacobi.ColorInputError):
            jacobi.parse_fraction(
                {
                    "sign": 1,
                    "rational": {"numerator": 1, "denominator": 2},
                    "atoms": [{"name": "C_A"}],
                }
            )
        self.assertEqual(
            jacobi.parse_fraction({"numerator": -3, "denominator": 7}),
            Fraction(-3, 7),
        )

    def test_unknown_tensor_and_wrong_metric_variance_fail_closed(self):
        with self.assertRaises(jacobi.ColorInputError):
            jacobi.normalize_network(
                [
                    jacobi.c("A", "B", "x"),
                    jacobi.c("x", "R", "S"),
                    {"kind": "trace", "indices": ["u", "v"]},
                ]
            )
        with self.assertRaises(jacobi.ColorInputError):
            jacobi.validate_and_project_tensor(
                {"kind": "kappa", "indices": ["u", "v"], "variance": "upper"}
            )

    def test_illegal_free_index_incidence_fails_closed(self):
        with self.assertRaises(jacobi.ColorInputError):
            jacobi.normalize_network(
                [jacobi.c("A", "B", "x"), jacobi.c("x", "R", "T")]
            )

    def test_orbit_bound_fails_closed(self):
        normalized = jacobi.normalize_network(jacobi.square_critical_fixture())
        self.assertIsNotNone(normalized.basis)
        assert normalized.basis is not None
        with self.assertRaises(jacobi.OrbitLimitError):
            jacobi.build_jacobi_orbit([normalized.basis], max_orbit_size=1)

    def test_component_oracle_checks_all_81_assignments(self):
        oracle = jacobi.su2_jacobi_component_oracle()
        self.assertTrue(oracle["passed"])
        self.assertEqual(oracle["component_assignments_checked"], 81)
        self.assertEqual(oracle["failures"], [])

    def test_adjoint_casimir_is_not_applied(self):
        contract = self.payload["algebra_contract"]["adjoint_Casimir"]
        self.assertEqual(contract["status"], jacobi.ADJOINT_CASIMIR_STATUS)
        self.assertFalse(contract["rewrite_applied"])

    def test_no_numerator_integral_or_coefficient_claim(self):
        terminal = self.payload["terminal_blocks"]
        for key in (
            "numerator",
            "integral",
            "UV_pole",
            "anomaly_coefficient",
            "external_target_comparison",
        ):
            self.assertIsNone(terminal[key])


if __name__ == "__main__":
    unittest.main()
