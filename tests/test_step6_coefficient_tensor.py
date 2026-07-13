import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step6_coefficient_tensor.py"
SPEC = importlib.util.spec_from_file_location("step6_coefficient_tensor_tested", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Step6CoefficientTensorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = MODULE.build_bundle()
        cls.audit = MODULE.audit_bundle(cls.bundle)

    def test_full_measure_pairing_inverse_is_two_sided(self):
        metric = MODULE.coefficient_pairing_matrix()
        inverse = MODULE.invert_fraction_matrix(metric)
        identity = MODULE.identity_fraction_matrix()
        self.assertEqual(MODULE.multiply_fraction_matrices(metric, inverse), identity)
        self.assertEqual(MODULE.multiply_fraction_matrices(inverse, metric), identity)
        self.assertEqual(sum(value != 0 for row in metric for value in row), 16)
        self.assertEqual(sum(value != 0 for row in inverse for value in row), 16)

    def test_normalized_difference_delta_is_metric_inverse(self):
        metric = MODULE.coefficient_pairing_matrix()
        inverse = MODULE.invert_fraction_matrix(metric)
        delta = MODULE.normalized_difference_delta_coefficients()
        self.assertEqual(delta, inverse)
        self.assertEqual(delta[0][15], Fraction(-4))
        self.assertEqual(delta[1][14], Fraction(4))

    def test_left_ordered_hessian_inverse_and_delta_reconstruction(self):
        metric = MODULE.coefficient_pairing_matrix()
        metric_inverse = MODULE.invert_fraction_matrix(metric)
        hessian = MODULE.left_ordered_coefficient_hessian(metric)
        hessian_inverse = MODULE.invert_fraction_matrix(hessian)
        expected = MODULE.left_ordered_covariance_core(metric_inverse)
        identity = MODULE.identity_fraction_matrix()
        self.assertEqual(hessian_inverse, expected)
        self.assertEqual(MODULE.multiply_fraction_matrices(hessian, hessian_inverse), identity)
        self.assertEqual(MODULE.multiply_fraction_matrices(hessian_inverse, hessian), identity)
        reconstructed = MODULE.reconstruct_delta_from_left_ordered_covariance(hessian_inverse)
        self.assertEqual(reconstructed, MODULE.normalized_difference_delta_coefficients())

    def test_operator_identity_is_not_coefficient_covariance(self):
        metric = MODULE.coefficient_pairing_matrix()
        inverse = MODULE.invert_fraction_matrix(metric)
        self.assertNotEqual(inverse, MODULE.identity_fraction_matrix())
        with self.assertRaisesRegex(ValueError, "operator identity"):
            MODULE.edge_covariance_entry(0, 15, inverse, coefficient_kernel="identity_16")
        with self.assertRaisesRegex(ValueError, "ordering sign"):
            MODULE.edge_covariance_entry(0, 15, inverse, coefficient_kernel="M_inverse")

    def test_typed_edge_covariance_rule_and_parities(self):
        inverse = MODULE.invert_fraction_matrix(MODULE.coefficient_pairing_matrix())
        entry = MODULE.edge_covariance_entry(1, 14, inverse)
        self.assertEqual(entry["left_ordered_H_inverse_entry"], "-4")
        self.assertEqual(entry["ordinary_kernel_coefficient"], "8")
        self.assertEqual(entry["ordered_endpoint_coefficient_parities"], [1, 1])
        self.assertTrue(entry["entry_even_when_nonzero"])
        self.assertIn("(-1)^(|s||t|)", entry["coefficient_supertranspose_convention"])
        self.assertEqual(
            entry["global_koszul_wick_permutation"],
            "BLOCKED_NOT_DERIVED_AT_THIS_LAYER",
        )
        templates = self.bundle["edge_covariance"]["per_oriented_parent_edge_templates"]
        self.assertEqual(len(templates), 30)
        for template in templates:
            self.assertEqual(
                tuple(template["target_all_incoming_vector"]),
                tuple(-value for value in template["source_all_incoming_vector"]),
            )
            self.assertEqual(template["coefficient_kernel"], "LEFT_ORDERED_H_INVERSE")

    def test_local_coefficient_exterior_cross_sign_is_included(self):
        zero = MODULE.momentum_from_vector((0, 0, 0, 0, 0))
        left = MODULE.oracle.LabeledLeaf("left", zero, 0, MODULE.oracle.Exterior.basis(1))
        right = MODULE.oracle.LabeledLeaf("right", zero, 0, MODULE.oracle.Exterior.basis(2))
        terms = (MODULE.oracle.ProductTerm(MODULE.oracle.ONE, (left, right)),)
        value = MODULE.evaluate_product_terms(terms, {"left": 1, "right": 1})
        self.assertEqual(value, MODULE.oracle.Exterior.basis(3, -1))

    def test_selected_grammar_and_all_local_options_compile(self):
        programs = self.bundle["tensor_programs"]
        self.assertEqual(programs["compiled_term_count"], 22)
        self.assertEqual(programs["parent_count"], 6)
        self.assertEqual(programs["local_option_program_count"], 1048)
        self.assertTrue(all(parent["all_local_options_compiled"] for parent in programs["parents"]))

    def test_full_ast_hash_ports_measure_and_conservation(self):
        programs = self.bundle["tensor_programs"]
        for program in programs["option_programs"].values():
            term = programs["compiled_terms"][program["term_id"]]
            self.assertEqual(program["expression_ast_sha256"], term["expression_ast_sha256"])
            self.assertEqual(program["color_ast_sha256"], term["color_ast_sha256"])
            self.assertEqual(program["measure"], term["measure"])
            self.assertEqual(
                sorted(binding["grammar_port_id"] for binding in program["bindings"]),
                sorted(term["port_order"]),
            )
            self.assertTrue(program["vertex_conservation"]["passed"])

    def test_signed_incidence_has_source_plus_target_minus(self):
        programs = self.bundle["tensor_programs"]["option_programs"]
        seen = set()
        for program in programs.values():
            for binding in program["bindings"]:
                if binding["role"] != "QUANTUM_EDGE_ENDPOINT":
                    continue
                routing = tuple(binding["edge_routing_vector"])
                incoming = tuple(binding["all_incoming_leaf_momentum_vector"])
                expected = routing if binding["orientation_endpoint"] == "source" else tuple(-x for x in routing)
                self.assertEqual(incoming, expected)
                seen.add(binding["orientation_endpoint"])
        self.assertEqual(seen, {"source", "target"})

    def test_recursive_and_independent_expanded_fixtures_agree(self):
        fixtures = self.bundle["fixtures"]
        self.assertEqual([item["family"] for item in fixtures], ["I2", "S3_PLUS", "S3_MINUS", "S4_PLUS"])
        self.assertTrue(all(item["recursive_expanded_equal"] for item in fixtures))
        self.assertTrue(all(item["value_is_nonzero"] for item in fixtures))
        self.assertEqual(fixtures[0]["value"]["type"], "Exterior")
        self.assertTrue(all(item["value"]["type"] == "Poly" for item in fixtures[1:]))

    def test_requested_entry_cache_is_exact(self):
        term, program = MODULE._first_program(self.bundle, "S3_PLUS")
        masks = MODULE.fixture_indices("S3_PLUS")
        first = MODULE.evaluate_tensor_entry(term, program, masks, engine="recursive")
        second = MODULE.evaluate_tensor_entry(term, program, masks, engine="recursive")
        self.assertIs(first, second)
        self.assertEqual(first["entry_sha256"], second["entry_sha256"])

    def test_component_bracket_is_one_ordered_product(self):
        regression = self.bundle["component_bracket_regression"]
        self.assertTrue(all(regression["checks"].values()))
        self.assertEqual(
            regression["superspace_interpretation"],
            "ONE_ORDERED_PRODUCT_NO_FORWARD_MINUS_REVERSE",
        )

    def test_fail_closed_boundary(self):
        blocked = self.bundle["fail_closed"]
        self.assertEqual(blocked["five_edge_global_tensor_contraction"], "BLOCKED_NOT_PERFORMED")
        self.assertEqual(blocked["global_coefficient_koszul_sign"], "BLOCKED_NOT_DERIVED")
        self.assertEqual(blocked["DRED"], "BLOCKED_NOT_PERFORMED")
        self.assertEqual(blocked["IBP"], "BLOCKED_NOT_PERFORMED")
        self.assertEqual(blocked["UV_pole"], "BLOCKED_NOT_PERFORMED")
        self.assertIsNone(blocked["renormalized_two_loop_coefficient"])

    def test_audit_passes(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["passed_count"], self.audit["check_count"])


if __name__ == "__main__":
    unittest.main()
