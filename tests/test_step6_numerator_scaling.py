from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import step6_numerator_scaling as scaling
from scripts import step6_two_loop_forest as forest
from scripts import step6_two_loop_graphir as graphir
from scripts import step6_two_loop_integrals as integrals


class Step6NumeratorScalingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.audit = scaling.write_outputs()
        cls.graphs = graphir.build_bundle()["literal_direct_graphs"]

    def test_audit_passes(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["totals"]["failed"], 0)
        self.assertGreaterEqual(self.audit["totals"]["checks"], 13)

    def test_every_repository_direct_parent_is_discovered_dynamically(self):
        self.assertEqual(
            self.payload["repository_direct_parent_count_discovered"], len(self.graphs)
        )
        self.assertEqual(
            set(self.payload["repository_direct_parent_ids"]),
            {graph["graph_id"] for graph in self.graphs},
        )

    def test_each_parent_has_every_named_cycle_and_full_graph(self):
        by_id = {
            row["graph_id"]: row
            for row in self.payload["graph_fixture_certificates"]
        }
        for graph in self.graphs:
            expected = {
                cycle["cycle_id"]
                for cycle in graph["simple_one_loop_cycles"]["cycles"]
            } | {"full"}
            actual = {
                row["subgraph_id"]
                for row in by_id[graph["graph_id"]]["subgraph_certificates"]
            }
            self.assertEqual(actual, expected)

    def test_adapted_map_is_derived_from_outside_routed_rows(self):
        for graph in self.graphs:
            for subgraph in scaling.graph_subgraph_records(graph):
                adapted = scaling.derive_scaling_map(graph, subgraph)
                B = adapted.basis_matrix
                for row in adapted.outside_loop_rows:
                    for column in range(adapted.subgraph_loop_count):
                        self.assertEqual(
                            sum(Fraction(row[i]) * B[i][column] for i in range(2)),
                            0,
                        )
                self.assertNotEqual(scaling.determinant_2(B), 0)

    def test_outside_edges_fixed_and_inside_edges_vary(self):
        for graph in self.payload["graph_fixture_certificates"]:
            for row in graph["subgraph_certificates"]:
                self.assertTrue(row["outside_edges_fixed"])
                self.assertTrue(row["every_inside_edge_varies"])

    def test_scalar_leading_quadratic_cancellation_gives_rho_zero(self):
        fixture = self.payload["manual_cancellation_and_basis_fixtures"]["fixtures"][
            "SCALAR_K_PLUS_L_SQUARED"
        ]
        result = fixture["canonical_basis_result"]
        self.assertEqual(result["highest_surviving_t_degree"], 0)
        self.assertEqual(
            result["expanded_terms"],
            [
                {
                    "coefficient": {"numerator": 4, "denominator": 1},
                    "t_degree": 0,
                    "scalar_monomial": [
                        {"generator": "dot(c0,c0)", "power": 1}
                    ],
                    "tensor_word": [],
                }
            ],
        )

    def test_scalar_partial_cancellation_gives_rho_one(self):
        fixture = self.payload["manual_cancellation_and_basis_fixtures"]["fixtures"][
            "SCALAR_K2_MINUS_L2"
        ]
        result = fixture["canonical_basis_result"]
        self.assertEqual(result["highest_surviving_t_degree"], 1)
        self.assertEqual(len(result["expanded_terms"]), 1)
        self.assertEqual(result["expanded_terms"][0]["coefficient"]["numerator"], 4)
        self.assertEqual(result["expanded_terms"][0]["t_degree"], 1)

    def test_tensor_vector_cancellation_includes_tensor_rank_exactly(self):
        fixture = self.payload["manual_cancellation_and_basis_fixtures"]["fixtures"][
            "TENSOR_K_PLUS_L"
        ]
        result = fixture["canonical_basis_result"]
        self.assertEqual(result["highest_surviving_t_degree"], 0)
        self.assertEqual(result["free_indices"], ["m"])
        self.assertEqual(
            result["expanded_terms"][0]["tensor_word"],
            [{"adapted_vector": "c0", "free_index": "m"}],
        )
        self.assertEqual(result["expanded_terms"][0]["coefficient"]["numerator"], 2)

    def test_rho_is_invariant_under_adapted_basis_change(self):
        fixtures = self.payload["manual_cancellation_and_basis_fixtures"]["fixtures"]
        self.assertTrue(all(row["basis_change_invariant"] for row in fixtures.values()))
        for graph in self.payload["graph_fixture_certificates"]:
            self.assertTrue(all(row["invariant"] for row in graph["basis_change_invariance"]))

    def test_true_substitution_not_edge_or_free_index_heuristic(self):
        self.assertFalse(self.payload["algorithm"]["edge_or_free_index_heuristic_used"])
        fixtures = self.payload["manual_cancellation_and_basis_fixtures"]["fixtures"]
        self.assertTrue(
            all(row["leading_degree_cancellation_observed"] for row in fixtures.values())
        )

    def test_complete_fixture_certificate_is_consumed_by_forest_API(self):
        for graph in self.payload["graph_fixture_certificates"]:
            power = graph["forest_API_result"]["power_counting"]
            self.assertEqual(power["unknown_subgraph_ids"], [])
            self.assertEqual(power["certificate"]["graph_hash"], graph["graph_hash"])
            self.assertEqual(
                power["status"], "POWER_COUNTING_CERTIFIED_KUV_STILL_UNEVALUATED"
            )

    def test_wrong_graph_hash_remains_rejected_by_forest_API(self):
        graph = self.graphs[0]
        records = forest.enumerate_connected_edge_subgraphs(graph)
        certificate = forest.NumeratorScalingCertificate(
            "wrong-hash",
            {record["subgraph_id"]: 0 for record in records if record["one_particle_irreducible"] and record["counts"]["L"] > 0},
        )
        with self.assertRaises(ValueError):
            forest.power_counting_analysis(graph, records, certificate)

    def test_malformed_or_regulator_polynomial_fails_closed(self):
        bad = dict(integrals.constant_polynomial(1))
        bad["coefficient_domain"] = "Q_WITH_EPSILON"
        with self.assertRaises(scaling.NumeratorSubstitutionError):
            scaling.substitute_numerator(bad, scaling.manual_fixture_map())

    def test_zero_numerator_has_no_fabricated_nonnegative_rho(self):
        result = scaling.substitute_numerator(
            integrals.zero_polynomial(), scaling.manual_fixture_map()
        )
        self.assertIsNone(result["highest_surviving_t_degree"])
        self.assertEqual(result["rho"], "ZERO_NUMERATOR")
        self.assertEqual(result["certificate_status"], "IDENTICALLY_ZERO_AFTER_EXACT_SUBSTITUTION")

    def test_physical_numerator_and_physics_results_remain_blocked(self):
        self.assertIsNone(
            self.payload["physical_numerator_status"]["compiled_Dalgebra_numerator"]
        )
        for key in (
            "physical_rho_by_subgraph",
            "physical_divergent_forest",
            "master_integral",
            "UV_pole",
            "renormalized_coefficient",
        ):
            self.assertIsNone(self.payload["terminal_blocks"][key])

    def test_no_regulator_or_comparison_data_enters_calculation(self):
        self.assertFalse(self.payload["algorithm"]["regulator_inserted_into_numerator"])
        self.assertFalse(self.payload["input_provenance"]["comparison_data_read"])
        for graph in self.payload["graph_fixture_certificates"]:
            for row in graph["subgraph_certificates"]:
                self.assertEqual(
                    row["scaled_numerator"]["coefficient_domain"], "Q_NO_EPSILON"
                )


if __name__ == "__main__":
    unittest.main()
