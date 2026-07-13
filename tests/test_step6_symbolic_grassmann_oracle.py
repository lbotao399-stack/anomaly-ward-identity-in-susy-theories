from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step6_symbolic_grassmann_oracle.py"


def load_oracle():
    specification = importlib.util.spec_from_file_location(
        "step6_symbolic_grassmann_oracle_under_test", SCRIPT
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load Step-6 symbolic Grassmann oracle")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


oracle = load_oracle()


class Step6SymbolicGrassmannOracleTests(unittest.TestCase):
    def test_sparse_q_i_polynomial_is_canonical_and_exact(self):
        p = oracle.Poly.variable("p_pp")
        q = oracle.Poly.variable("q_mm")
        self.assertEqual((p + q) * (p - q), p**2 - q**2)
        self.assertEqual(p - p, oracle.ZERO)
        self.assertTrue(
            all(
                isinstance(number, Fraction)
                for _, coefficient in ((p + oracle.I * q) ** 2).terms
                for number in (coefficient.re, coefficient.im)
            )
        )

    def test_source_has_no_float_literals(self):
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        float_literals = [
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        self.assertEqual(float_literals, [])

    def test_exterior_order_and_left_derivative(self):
        generators = [oracle.Exterior.basis(1 << index) for index in range(4)]
        self.assertEqual(generators[1] * generators[0], (generators[0] * generators[1]).scale(-1))
        top = generators[0] * generators[1] * generators[2] * generators[3]
        self.assertEqual(top, oracle.Exterior.basis(15))
        self.assertEqual(top.left_derivative(1), oracle.Exterior.basis(13, -1))

    def test_symbolic_defining_anticommutators(self):
        checks = oracle.exact_identity_checks()
        selected = {
            key: value
            for key, value in checks.items()
            if key.startswith(("D_D_", "barD_barD_", "D_barD_"))
        }
        self.assertEqual(len(selected), 12)
        self.assertTrue(all(selected.values()), selected)

    def test_symbolic_projector_identities_are_polynomial(self):
        checks = oracle.exact_identity_checks()
        self.assertTrue(checks["D2_barD2_D2"])
        self.assertTrue(checks["barD2_D2_barD2"])

    def test_all_three_measures_have_locked_normalization(self):
        checks = oracle.exact_identity_checks()
        self.assertTrue(checks["theta2_chiral_measure_1"])
        self.assertTrue(checks["bartheta2_antichiral_measure_1"])
        self.assertTrue(checks["normalized_delta_full_measure_1"])
        self.assertTrue(checks["normalized_delta_closed_constant_16"])

    def test_scalar_vector_kernel_cancels_exactly(self):
        checks = oracle.exact_identity_checks()
        self.assertTrue(checks["K_V_G_V_scalar_left"])
        self.assertTrue(checks["G_V_K_V_scalar_right"])

    def test_translation_matches_verified_project_matrices(self):
        checks = oracle.translation_checks()
        self.assertEqual(len(checks), 21)
        self.assertTrue(all(checks.values()), checks)

    def test_w1_and_x1_words_equal_direct_matrix_composition(self):
        checks = oracle.word_and_leibniz_checks()
        self.assertTrue(checks["W1_compiled_equals_direct"])
        self.assertTrue(checks["X1_compiled_equals_K_plus"])

    def test_labeled_graded_leibniz_matches_total_momentum_matrix(self):
        checks = oracle.word_and_leibniz_checks()
        self.assertTrue(checks["odd_even_graded_Leibniz_equals_total_momentum_matrix"])
        self.assertTrue(checks["labeled_leaf_histories_retained"])

    def test_generic_graded_bracket_outer_bard2_is_one_full_ast_scope(self):
        regression = oracle.generic_graded_bracket_scope_fixture()
        checks = regression["checks"]
        self.assertTrue(all(checks.values()), regression)
        self.assertEqual(
            regression["certifies"],
            "OUTER_SCOPE_DISTRIBUTION_ONLY_NOT_COMPONENT_ADJOINT_GRAMMAR",
        )
        self.assertEqual(
            regression["correct_bar_allocations"],
            [[0, 2], [1, 1], [2, 0]],
        )
        self.assertEqual(regression["wrong_bar_allocations"], [[2, 2]])
        self.assertNotEqual(
            regression["formula"], regression["rejected_formula"]
        )

    def test_component_adjoint_is_one_ordered_product_without_second_i(self):
        fixture = oracle.component_adjoint_ordered_product_fixture()
        self.assertTrue(all(fixture["checks"].values()), fixture)
        self.assertEqual(
            fixture["generator_commutator"],
            "[T_A,T_B]=i*c[A,B,C]*T_C",
        )
        self.assertEqual(fixture["grammar_component_node"], "c[A,B,C]*Y^A*Z^B")
        self.assertTrue(fixture["grammar_QI_is_after_commutator_expansion"])
        self.assertFalse(fixture["reverse_component_term"])
        self.assertEqual(fixture["adjoint_QI_prefactor"], "1")
        self.assertEqual(fixture["Gamma2_component_prefactor"], "-i/2")
        self.assertEqual(fixture["W2_component_prefactor"], "i/16")

    def test_unknown_derivative_token_fails_closed(self):
        with self.assertRaises(KeyError):
            oracle.expand_derivative_word(("UNDECLARED_D",))

    def test_build_result_is_bounded_and_passes(self):
        result = oracle.build_result()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["totals"]["failed"], 0)
        self.assertEqual(
            result["remaining_interface"]["status"],
            "BLOCKED_GRAPH_TENSOR_CONTRACTION_INTERFACE_NOT_IMPLEMENTED",
        )
        self.assertFalse(any(result["negative_claims"].values()))

    def test_provenance_hashes_are_exact(self):
        result = oracle.build_result()
        for relative_path, digest in result["provenance"].items():
            path = ROOT / relative_path
            self.assertTrue(path.is_file())
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)

    def test_generator_writes_readable_and_machine_outputs(self):
        self.assertEqual(oracle.main(), 0)
        result = json.loads(oracle.OUTPUT_JSON.read_text(encoding="utf-8"))
        audit = json.loads(oracle.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(audit["status"], "PASS")
        self.assertIn("NO_GRAPH_CONTRACTION", oracle.OUTPUT_MD.read_text(encoding="utf-8"))
        for relative_path, digest in audit["generated_sha256"].items():
            self.assertEqual(hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest(), digest)

    def test_forbidden_input_roots_and_target_markers_are_absent(self):
        source = SCRIPT.read_text(encoding="utf-8")
        for forbidden in (
            "tasks/reviews",
            "references/external-targets",
            "Q_2(b",
            "holomorphic twist",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
