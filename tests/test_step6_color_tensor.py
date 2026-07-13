from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import step6_color_tensor as color
from scripts import step6_two_loop_amplitude_ir as amplitude


def v_nodes(expression):
    rows = []

    def visit(node):
        if node["op"] == "V":
            rows.append(node)
        for argument in node.get("args", ()):
            visit(argument)

    visit(expression)
    return rows


class Step6ColorTensorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.audit = color.write_outputs()
        _, cls.runtime_parents, _ = amplitude.build_runtime()

    def test_audit_and_exact_cardinality(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["totals"]["failed"], 0)
        self.assertEqual(self.payload["parent_count"], 6)
        self.assertEqual(self.payload["exact_total_labeled_amplitudes"], 2_985_984)
        self.assertEqual(
            sum(
                parent["factorized_histogram_multiplicity"]
                for parent in self.payload["parents"]
            ),
            2_985_984,
        )

    def test_gamma2_w2_emit_one_ordered_c_without_extra_i(self):
        regression = color.gamma2_w2_regression()
        for label in ("Gamma2", "W2"):
            row = regression[label]
            self.assertTrue(row["one_ordered_c"])
            self.assertEqual(row["source_coefficient_Qi"]["i_power_reduced"], 1)
            self.assertEqual(row["extra_i"], 0)
            self.assertFalse(row["reverse_bracket_term"])
            node = row["ordered_c_node"]
            self.assertEqual(node["component_rule"], color.COMPONENT_RULE)
            self.assertEqual(node["emission_policy"], color.ORDERED_C_POLICY)
            self.assertEqual(node["ordered_leg_roles"], [
                "left_input",
                "right_input",
                "bracket_output",
            ])

    def test_extra_i_is_rejected(self):
        node = deepcopy(color.gamma2_w2_regression()["Gamma2"]["ordered_c_node"])
        node["extra_i_power"] = 1
        with self.assertRaises(color.OrderedBracketError):
            color.validate_ordered_c_node(node)

    def test_reverse_bracket_is_rejected(self):
        node = deepcopy(color.gamma2_w2_regression()["W2"]["ordered_c_node"])
        node["reverse_bracket_term_emitted"] = True
        with self.assertRaises(color.OrderedBracketError):
            color.validate_ordered_c_node(node)

    def test_deleted_port_is_rejected(self):
        parent = self.runtime_parents[0]
        vertex_id = parent.vertex_order[0]
        vertex = next(v for v in parent.graph["vertices"] if v["vertex_id"] == vertex_id)
        option = parent.local_options[vertex_id][0]
        term = parent.term_dictionary[option["source_term_id"]]
        bindings, _ = color.local_option_port_bindings(parent, option)
        bindings.pop(next(iter(bindings)))
        with self.assertRaises(color.PortSaturationError):
            color.compile_root_color_ast(
                term["expression_ast"],
                vertex_id=vertex_id,
                source_term_id=term["term_id"],
                topology_role=vertex["role"],
                port_bindings=bindings,
            )

    def test_duplicated_source_port_is_rejected(self):
        parent = self.runtime_parents[0]
        vertex_id = parent.vertex_order[0]
        vertex = next(v for v in parent.graph["vertices"] if v["vertex_id"] == vertex_id)
        option = parent.local_options[vertex_id][0]
        term = parent.term_dictionary[option["source_term_id"]]
        expression = deepcopy(term["expression_ast"])
        leaves = v_nodes(expression)
        self.assertGreaterEqual(len(leaves), 2)
        leaves[1]["attrs"]["port_id"] = leaves[0]["attrs"]["port_id"]
        bindings, _ = color.local_option_port_bindings(parent, option)
        with self.assertRaises(color.PortSaturationError):
            color.compile_root_color_ast(
                expression,
                vertex_id=vertex_id,
                source_term_id=term["term_id"],
                topology_role=vertex["role"],
                port_bindings=bindings,
            )

    def test_missing_or_extra_free_index_is_rejected(self):
        invalid = [
            {
                "kind": "c",
                "ordered_indices": ["A", "B", "R"],
                "component_rule": color.COMPONENT_RULE,
                "extra_i_power": 0,
                "reverse_bracket_term_emitted": False,
            },
            {
                "kind": "kappa_inverse",
                "indices": ["T", "d0"],
                "variance": "upper",
            },
            {
                "kind": "kappa",
                "indices": ["d0", "d1"],
                "variance": "lower",
            },
        ]
        with self.assertRaises(color.FreeIndexError):
            color.validate_free_indices(invalid)

    def test_exact_antisymmetry_sign(self):
        tensor = {
            "kind": "c",
            "ordered_indices": ["B", "A", "R"],
            "component_rule": color.COMPONENT_RULE,
            "extra_i_power": 0,
            "reverse_bracket_term_emitted": False,
        }
        canonical = color.canonicalize_network([tensor], antisymmetry=True)
        self.assertEqual(canonical["overall_antisymmetry_sign"], -1)
        self.assertFalse(canonical["zero_by_antisymmetry"])
        self.assertEqual(
            canonical["canonical_tensors"][0]["canonical_indices"],
            ["A", "B", "R"],
        )

    def test_repeated_c_index_is_exact_zero(self):
        tensor = {
            "kind": "c",
            "ordered_indices": ["A", "A", "R"],
            "component_rule": color.COMPONENT_RULE,
            "extra_i_power": 0,
            "reverse_bracket_term_emitted": False,
        }
        canonical = color.canonicalize_network([tensor], antisymmetry=True)
        self.assertTrue(canonical["zero_by_antisymmetry"])
        self.assertEqual(canonical["overall_antisymmetry_sign"], 0)

    def test_kappa_inverse_contraction_is_exact(self):
        network = [
            {"kind": "kappa", "indices": ["x", "y"], "variance": "lower"},
            {
                "kind": "kappa_inverse",
                "indices": ["x", "z"],
                "variance": "upper",
            },
            {
                "kind": "c",
                "ordered_indices": ["y", "A", "B"],
                "component_rule": color.COMPONENT_RULE,
                "extra_i_power": 0,
                "reverse_bracket_term_emitted": False,
            },
            {
                "kind": "c",
                "ordered_indices": ["z", "R", "S"],
                "component_rule": color.COMPONENT_RULE,
                "extra_i_power": 0,
                "reverse_bracket_term_emitted": False,
            },
        ]
        reduced = color.reduce_metrics_exact(network)
        self.assertEqual(reduced["rewrite_count"], 1)
        self.assertFalse(any(t["kind"].startswith("kappa") for t in reduced["tensors"]))
        self.assertTrue(reduced["all_rewrite_paths_same_terminal"])

    def test_every_quantum_leaf_joins_one_of_five_metrics(self):
        for parent, payload_parent in zip(
            self.runtime_parents, self.payload["parents"], strict=True
        ):
            rows = [
                payload_parent["local_color_option_catalog"][vertex][0]
                for vertex in parent.vertex_order
            ]
            _, propagators = color.attach_propagator_color_metrics(parent, rows)
            self.assertEqual(len(propagators), 5)
            endpoints = [
                port
                for propagator in propagators
                for port in (
                    propagator["source_topology_port"],
                    propagator["target_topology_port"],
                )
            ]
            self.assertEqual(len(endpoints), len(set(endpoints)))
            self.assertEqual(len(endpoints), 10)

    def test_source_qi_owns_bracket_i_parity(self):
        for parent in self.payload["parents"]:
            for rows in parent["local_color_option_catalog"].values():
                for row in rows:
                    self.assertEqual(
                        row["source_coefficient_i_power"],
                        row["ordered_c_node_count"] % 2,
                    )
                    self.assertEqual(row["color_i_factor_added_by_compiler"], 0)

    def test_orientation_and_external_permutation_ledgers_are_separate(self):
        orientations = {(p["graph_id"], p["orientation"]) for p in self.payload["parents"]}
        graph_ids = {p["graph_id"] for p in self.payload["parents"]}
        self.assertEqual(
            orientations,
            {(graph_id, orientation) for graph_id in graph_ids for orientation in ("direct", "reflected")},
        )
        for parent in self.payload["parents"]:
            for row in parent["factorized_signature_histogram"]:
                self.assertEqual(row["bosonic_external_permutation_sign"], 1)
                self.assertFalse(row["fermion_sign_inferred"])

    def test_color_marginal_preserves_exact_option_join_factorization(self):
        for parent in self.payload["parents"]:
            groups_by_vertex = {
                vertex: {
                    group["local_color_signature_sha256"]: group
                    for group in groups
                }
                for vertex, groups in parent[
                    "factorized_local_color_catalog"
                ].items()
            }
            for row in parent["factorized_signature_histogram"]:
                factors = row["ordered_local_color_group_ids_in_vertex_order"]
                self.assertEqual(len(factors), 4)
                self.assertEqual(
                    row["multiplicity"],
                    __import__("math").prod(
                        groups_by_vertex[vertex][factor]["multiplicity"]
                        for vertex, factor in zip(
                            parent["vertex_order"], factors, strict=True
                        )
                    ),
                )
                for vertex, factor in zip(parent["vertex_order"], factors, strict=True):
                    group = groups_by_vertex[vertex][factor]
                    self.assertEqual(
                        group["multiplicity"], len(group["local_amplitude_option_ids"])
                    )
                self.assertTrue(parent["factorized_histogram_policy"]["color_histogram_is_a_marginal_not_a_downstream_product"])
                self.assertTrue(parent["factorized_histogram_policy"]["independent_marginal_multiplication_forbidden"])

    def test_jacobi_is_not_applied(self):
        self.assertEqual(self.payload["Jacobi_equivalence_status"], color.JACOBI_STATUS)
        for parent in self.payload["parents"]:
            self.assertFalse(parent["jacobi_policy"]["rewrite_implemented"])
            self.assertTrue(parent["jacobi_policy"]["histogram_is_not_Jacobi_quotiented"])

    def test_firewall_and_downstream_absence(self):
        self.assertFalse(self.payload["input_firewall"]["review_or_external_target_reads"])
        self.assertEqual(
            set(self.payload["input_firewall"]["allowed_modules"]),
            {
                "scripts/step6_two_loop_grammar.py",
                "scripts/step6_two_loop_graphir.py",
                "scripts/step6_two_loop_wick.py",
                "scripts/step6_two_loop_amplitude_ir.py",
            },
        )
        for value in self.payload["global_downstream_fail_closed"].values():
            self.assertIsNone(value["value"])


if __name__ == "__main__":
    unittest.main()
