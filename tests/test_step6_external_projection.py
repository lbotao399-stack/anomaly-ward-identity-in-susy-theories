import copy
import json
from pathlib import Path
import unittest

from scripts import step6_external_projection as projection


ROOT = Path(__file__).resolve().parents[1]


class Step6ExternalProjectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload, cls.runtime = projection.build_payload()
        cls.by_id = {item.graph["graph_id"]: item for item in cls.runtime}

    def test_all_exact_checks_pass(self) -> None:
        checks = projection.exact_checks(self.payload, self.runtime)
        self.assertEqual(sum(not value for value in checks.values()), 0, checks)
        self.assertEqual(len(checks), 23)

    def test_ordered_v_background_quantum_split_has_unit_multiplicity(self) -> None:
        certificate = projection.ordered_split_certificate()
        for degree in certificate["degrees"]:
            t = degree["ordered_degree"]
            self.assertEqual(degree["role_word_count"], 2**t)
            self.assertEqual(degree["unique_role_word_count"], 2**t)
            self.assertEqual(
                degree["fixed_background_distribution"],
                {str(b): projection.comb(t, b) for b in range(t + 1)},
            )
            self.assertEqual(degree["coefficient_of_every_labeled_role_word"]["rendered"], "1")
            self.assertEqual(degree["multiplicity_of_every_labeled_role_word"], 1)

    def test_linear_project_maps_are_derived_from_grammar_ast(self) -> None:
        maps = projection.linear_map_certificate()["maps"]
        self.assertEqual(maps["Gamma_(1)+"]["coefficient"]["rendered"], "1")
        self.assertEqual(
            maps["Gamma_(1)+"]["derivative_word_outer_to_inner"], ["D_+"]
        )
        self.assertEqual(maps["W_(1)+"]["coefficient"]["rendered"], "-1/8")
        self.assertEqual(
            maps["W_(1)+"]["derivative_word_outer_to_inner"],
            ["barD^2", "D_+"],
        )
        self.assertEqual(maps["X_(1)"]["coefficient"]["rendered"], "-1/8")
        self.assertEqual(
            maps["X_(1)"]["derivative_word_outer_to_inner"],
            ["D_+", "barD^2", "D_+"],
        )
        self.assertEqual(maps["X_(1)"]["connection_sum_at_degree_one"], [])
        self.assertEqual(
            maps["TildeGamma_(1)dot_a"]["coefficient"]["rendered"], "-1"
        )
        self.assertEqual(
            maps["TildeW_(1)dot_a"]["coefficient"]["rendered"], "-1/8"
        )
        self.assertEqual(
            maps["TildeW_(1)dot_a"]["derivative_word_outer_to_inner"],
            ["D^2", "barD_dot_a"],
        )

    def test_all_three_decorated_k4_minus_edge_graphs_are_present(self) -> None:
        self.assertEqual(tuple(self.by_id), projection.SUPPORTED_GRAPH_IDS)
        self.assertTrue(
            all(item.graph["topology"] == "K4_MINUS_ONE_EDGE" for item in self.runtime)
        )

    def test_exact_factorized_projection_cardinalities(self) -> None:
        expected = {
            "G6_DIRECT_K4ME_I3_S3CUBED": ((12, 12), 144),
            "G6_DIRECT_K4ME_I2_S3SQ_S4": ((12, 24), 288),
            "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": ((72,), 72),
        }
        for graph_id, (radices, cardinality) in expected.items():
            runtime = self.by_id[graph_id]
            self.assertEqual(runtime.radices, radices)
            self.assertEqual(runtime.cardinality, cardinality)
        self.assertEqual(self.payload["exact_total_graph_projection_candidates"], 504)

    def test_double_background_s4_keeps_both_ordered_external_permutations(self) -> None:
        runtime = self.by_id["G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"]
        rows = runtime.local_candidates["C"]
        self.assertEqual(len(rows), 72)
        self.assertEqual(sum(row["external_permutation"] == ["p1", "p2"] for row in rows), 36)
        self.assertEqual(sum(row["external_permutation"] == ["p2", "p1"] for row in rows), 36)
        self.assertTrue(
            all(len(row["background_port_projections"]) == 2 for row in rows)
        )

    def test_every_materialized_graph_projection_has_exact_external_momenta(self) -> None:
        for runtime in self.runtime:
            for row in projection.iter_materialized(runtime):
                self.assertEqual(row["external_momentum_multiset"], ["p1", "p2"])
                self.assertEqual(len(row["background_port_projections"]), 2)
                self.assertEqual(row["valid_orientations"], ["direct", "reflected"])

    def test_every_port_retains_derivative_measure_spinor_color_and_source_coefficient(self) -> None:
        for runtime in self.runtime:
            for vertex_id in runtime.background_vertex_order:
                for candidate in runtime.local_candidates[vertex_id]:
                    self.assertIn(
                        candidate["measure_chirality"]["chirality"],
                        ("CHIRAL", "ANTICHIRAL"),
                    )
                    self.assertEqual(candidate["source_term_coefficient_raw"]["field"], "Q(i)")
                    self.assertIsNone(candidate["assembled_vertex_coefficient"])
                    for port in candidate["background_port_projections"]:
                        self.assertTrue(port["derivative_word_outer_to_inner"])
                        slots = port["spinor_and_color_slots"]
                        self.assertIn(
                            slots["spinor_slot"],
                            ("a_up", "a_down", "dot_a_up", "dot_a_down"),
                        )
                        self.assertIn(slots["factor_output_color_slot"], ("A", "B"))
                        self.assertEqual(slots["gauge_color_pairing"], "kappa[A,B]")
                        self.assertEqual(port["ordered_split_coefficient"]["rendered"], "1")
                        self.assertEqual(port["ordered_split_multiplicity"], 1)

    def test_only_degree_one_factor_is_named_as_linear_field_strength(self) -> None:
        saw_linear = False
        saw_nonlinear = False
        for runtime in self.runtime:
            for vertex_id in runtime.background_vertex_order:
                for candidate in runtime.local_candidates[vertex_id]:
                    for port in candidate["background_port_projections"]:
                        degree = port["spinor_and_color_slots"]["field_strength_degree"]
                        supply = port["source_supply"]
                        if degree == 1:
                            saw_linear = True
                            self.assertIn(
                                supply["status"],
                                (
                                    "EXACT_LINEAR_PROJECT_FIELD_STRENGTH",
                                    "EXACT_LINEAR_PROJECT_TILDE_FIELD_STRENGTH",
                                ),
                            )
                            self.assertIsNotNone(supply["standalone_linear_projector"])
                        else:
                            saw_nonlinear = True
                            self.assertEqual(
                                supply["status"], "EXACT_NONLINEAR_SOURCE_FACTOR_RETAINED"
                            )
                            self.assertIsNone(supply["standalone_linear_projector"])
        self.assertTrue(saw_linear)
        self.assertTrue(saw_nonlinear)

    def test_factor_group_classifies_pure_and_mixed_nonlinear_backgrounds(self) -> None:
        runtime = self.by_id["G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"]
        classes = {
            group["classification"]
            for row in runtime.local_candidates["C"]
            for group in row["factor_groups"]
        }
        self.assertIn("LINEAR_PURE_BACKGROUND_FACTOR", classes)
        self.assertIn("NONLINEAR_PURE_BACKGROUND_FACTOR", classes)
        self.assertIn("NONLINEAR_MIXED_BACKGROUND_QUANTUM_FACTOR", classes)

    def test_unsupported_background_source_fails_closed(self) -> None:
        graph = copy.deepcopy(self.runtime[0].graph)
        insertion = next(vertex for vertex in graph["vertices"] if vertex["vertex_id"] == "I")
        insertion["background_valence"] = 1
        insertion["background_ports"] = [
            {"port_id": "I.b0", "kind": "BACKGROUND_EXTERNAL", "momentum": "p1"}
        ]
        with self.assertRaises(projection.ProjectionSourceBlocked):
            projection.vertex_projection_candidates(graph, insertion)

    def test_no_downstream_stage_or_graph_coefficient_is_claimed(self) -> None:
        self.assertIsNone(self.payload["coefficient_policy"]["assembled_vertex_coefficient"])
        self.assertIsNone(self.payload["coefficient_policy"]["assembled_graph_coefficient"])
        self.assertEqual(
            set(self.payload["forbidden_stages"]),
            {
                "QUANTUM_PORT_TO_EDGE_JOIN",
                "PROPAGATOR",
                "WICK_CONTRACTION",
                "D_ALGEBRA",
                "AMPLITUDE",
                "GRAPH_COEFFICIENT",
                "SUBTRACTION",
            },
        )
        for runtime in self.runtime:
            for row in projection.iter_materialized(runtime):
                self.assertIsNone(row["propagator"])
                self.assertIsNone(row["wick_contraction"])
                self.assertIsNone(row["d_algebra"])
                self.assertIsNone(row["amplitude"])
                self.assertIsNone(row["assembled_graph_coefficient"])

    def test_generated_payload_and_audit_are_reproducible(self) -> None:
        generated = json.loads(
            (ROOT / "generated/step6/external-projection/external-projection-certificate.json").read_text()
        )
        audit = json.loads(
            (ROOT / "audits/step6-external-projection-verification.json").read_text()
        )
        self.assertEqual(generated, self.payload)
        self.assertEqual(audit, projection.build_audit(self.payload, self.runtime))
        self.assertEqual(audit["summary"], {"passed": 23, "failed": 0, "total": 23})


if __name__ == "__main__":
    unittest.main()
