from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts import step6_two_loop_amplitude_ir as amplitude
from scripts import step6_external_projection as projection


ROOT = Path(__file__).resolve().parents[1]


class Step6TwoLoopAmplitudeIRTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload, cls.parents = amplitude.build_payload()
        cls.checks = amplitude.exact_checks(cls.payload, cls.parents)
        cls.by_key = {
            (parent.graph["graph_id"], parent.orientation): parent
            for parent in cls.parents
        }

    def test_all_exact_checks_pass(self) -> None:
        self.assertTrue(
            all(self.checks.values()),
            [name for name, passed in self.checks.items() if not passed],
        )
        self.assertEqual(len(self.checks), 22)

    def test_exact_factorized_cardinality_and_rank_unrank(self) -> None:
        expected = {
            "G6_DIRECT_K4ME_I3_S3CUBED": 829_440,
            "G6_DIRECT_K4ME_I2_S3SQ_S4": 331_776,
            "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": 331_776,
        }
        self.assertEqual(self.payload["exact_total_labeled_amplitudes"], 2_985_984)
        self.assertEqual(
            self.payload[
                "exact_total_physical_representative_amplitudes_before_automorphism_weight"
            ],
            1_492_992,
        )
        for (graph_id, _), parent in self.by_key.items():
            self.assertEqual(parent.cardinality, expected[graph_id])
            self.assertEqual(parent.radices, parent.wick_join.radices)
            for rank in (0, 1, parent.cardinality // 2, parent.cardinality - 1):
                self.assertEqual(parent.rank(parent.unrank(rank)), rank)

    def test_local_projection_join_is_exact_and_bijective(self) -> None:
        projection_ids = set(self.payload["projection_candidate_dictionary"])
        used = set()
        for parent in self.parents:
            for vertex_id in parent.vertex_order:
                vertex = next(
                    item for item in parent.graph["vertices"] if item["vertex_id"] == vertex_id
                )
                for option in parent.local_options[vertex_id]:
                    ref = option["background_projection"]
                    if vertex["background_valence"] == 0:
                        self.assertEqual(ref["status"], "NOT_APPLICABLE_EXACT_B0_VERTEX")
                        self.assertIsNone(ref["projection_candidate_id"])
                    else:
                        self.assertEqual(
                            ref["status"], "EXACT_BIJECTIVE_PROJECT_BACKGROUND_JOIN"
                        )
                        self.assertFalse(
                            ref["external_projector_coefficient_applied_separately"]
                        )
                        used.add(ref["projection_candidate_id"])
        self.assertEqual(used, projection_ids)

    def test_double_background_projection_preserves_both_source_orders(self) -> None:
        parent = self.by_key[
            ("G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4", "direct")
        ]
        source_orders = set()
        for option in parent.local_options["C"]:
            candidate_id = option["background_projection"]["projection_candidate_id"]
            candidate = self.payload["projection_candidate_dictionary"][candidate_id]
            source_orders.add(tuple(candidate["external_permutation"]))
        self.assertEqual(source_orders, {("p1", "p2"), ("p2", "p1")})
        for rank in (0, parent.cardinality // 2, parent.cardinality - 1):
            row = parent.materialize(rank)
            self.assertEqual(
                [
                    item["external_momentum"]
                    for item in row["external_background_projection"][
                        "topology_background_port_order"
                    ]
                ],
                ["p1", "p2"],
            )

    def test_every_sample_has_five_exact_Project_propagators(self) -> None:
        for parent in self.parents:
            for rank in (0, parent.cardinality // 2, parent.cardinality - 1):
                row = parent.materialize(rank)
                self.assertEqual(len(row["edges"]), 5)
                self.assertEqual(row["denominator_product"], parent.graph["denominator_ast"])
                for edge in row["edges"]:
                    propagator = edge["propagator"]
                    self.assertEqual(propagator["coefficient"]["rendered"], "-2*g^2")
                    self.assertEqual(propagator["inverse_Hessian_kernel"], "G_V")
                    self.assertEqual(propagator["Wick_contraction"], "hbar*G_V")
                    self.assertEqual(propagator["Wick_hbar_factor"]["power"], 1)
                    self.assertEqual(propagator["grassmann_operator"], "identity_16")
                    self.assertEqual(propagator["grassmann_delta_ast"]["degree"], 4)
                    self.assertEqual(propagator["momentum"], edge["momentum"])
                    self.assertEqual(propagator["momentum_vector"], edge["momentum_vector"])
                    self.assertEqual(
                        propagator["denominator"]["edge_id"], edge["edge_id"]
                    )

    def test_orientation_reverses_edges_but_not_squared_denominators(self) -> None:
        for graph_id in projection.SUPPORTED_GRAPH_IDS:
            direct = self.by_key[(graph_id, "direct")].materialize(0)
            reflected = self.by_key[(graph_id, "reflected")].materialize(0)
            self.assertEqual(direct["denominator_product"], reflected["denominator_product"])
            direct_edges = {edge["edge_id"]: edge for edge in direct["edges"]}
            reflected_edges = {edge["edge_id"]: edge for edge in reflected["edges"]}
            for edge_id in direct_edges:
                left = direct_edges[edge_id]
                right = reflected_edges[edge_id]
                self.assertEqual(left["source"]["vertex_id"], right["target"]["vertex_id"])
                self.assertEqual(left["target"]["vertex_id"], right["source"]["vertex_id"])
                self.assertEqual(
                    left["momentum_vector"], [-value for value in right["momentum_vector"]]
                )

    def test_endpoint_D_words_color_AST_refs_measures_and_theta_vertices_survive(self) -> None:
        for parent in self.parents:
            row = parent.materialize(parent.cardinality // 2)
            self.assertEqual(len(row["theta_vertices"]), 4)
            for theta_vertex in row["theta_vertices"]:
                term = self.payload["term_dictionary"][theta_vertex["source_term_id"]]
                self.assertEqual(theta_vertex["measure"], term["measure"])
                self.assertEqual(theta_vertex["color_ast_sha256"], term["color_ast_sha256"])
                self.assertEqual(
                    theta_vertex["expression_ast_sha256"], term["expression_ast_sha256"]
                )
            for edge in row["edges"]:
                for endpoint in (edge["source"], edge["target"]):
                    self.assertEqual(
                        endpoint["grammar_derivative_word_outer_to_inner"],
                        endpoint["grammar_port_record"]["derivative_word_outer_to_inner"],
                    )
                    self.assertIn(endpoint["source_color_ast_ref"], self.payload["term_dictionary"])

    def test_exact_coefficient_factorization_is_1_times_3_times_5(self) -> None:
        for parent in self.parents:
            for rank in (0, parent.cardinality // 2, parent.cardinality - 1):
                factors = parent.materialize(rank)["coefficient_factorization"]
                self.assertEqual(len(factors["ordered_action_raw_Qi"]), 3)
                self.assertEqual(len(factors["ordered_vector_Wick_factors"]), 5)
                self.assertTrue(
                    all(
                        item["inverse_Hessian_GV_coefficient"]["rendered"]
                        == "-2*g^2"
                        and item["Wick_hbar_factor"]["power"] == 1
                        for item in factors["ordered_vector_Wick_factors"]
                    )
                )
                orbit = factors["decorated_occurrence_orbit_factor"]
                self.assertEqual(orbit["N"], 3)
                self.assertEqual(orbit["combined_hbar_power"], -3)
                self.assertEqual(
                    (
                        orbit["combined_rational"]["numerator"],
                        orbit["combined_rational"]["denominator"],
                    ),
                    (-1, orbit["background_source_labeled_automorphism_order"]),
                )
                self.assertEqual(factors["bosonic_wick_sign"]["value"], 1)
                self.assertIsNone(factors["external_projector_coefficient_factor"])
                self.assertEqual(
                    factors["exact_product_before_h_rewrite"]["normalization_exponents"],
                    {"g^2": 5, "h": 3, "hbar": 2},
                )
                self.assertEqual(
                    factors["exact_product_before_h_rewrite"]["hbar_power_certificate"],
                    {
                        "action_occurrence_orbit_power": -3,
                        "five_Wick_edge_power": 5,
                        "identity": "-3+5=2",
                    },
                )
                self.assertEqual(
                    factors["h_equals_inverse_g_squared_rewrite_certificate"]["output"],
                    "g^4*hbar^2",
                )
                self.assertEqual(
                    factors["exact_product_after_h_rewrite"]["coupling_grade"], "g^4"
                )
                self.assertEqual(
                    factors["exact_product_after_h_rewrite"]["loop_grade"], "hbar^2"
                )

    def test_histogram_is_exact_without_global_row_materialization(self) -> None:
        for parent_row in self.payload["parents"]:
            self.assertNotIn("amplitude_rows", parent_row)
            self.assertEqual(
                sum(
                    item["labeled_pairing_count"]
                    for item in parent_row["coefficient_signature_histogram"]
                ),
                parent_row["global_amplitude_enumeration"]["cardinality"],
            )
            self.assertEqual(
                set(parent_row["samples_only_not_full_materialization"]),
                {"first", "middle", "last"},
            )

    def test_optional_integral_link_has_no_numerator_or_reduction(self) -> None:
        for row in self.payload["parents"]:
            link = row["integral_family_interface"]
            if link is None:
                continue
            self.assertEqual(link["status"], "OPTIONAL_INTERFACE_LINKED_NOT_A_DEPENDENCY")
            self.assertIsNone(link["physical_numerator"])
            self.assertEqual(
                link["edge_order"],
                [factor["edge_id"] for factor in row["denominator_product"]["factors"]],
            )

    def test_all_downstream_quantities_fail_closed(self) -> None:
        for row in self.payload["parents"]:
            for stage in row["downstream_fail_closed"].values():
                self.assertIsNone(stage["value"])
                self.assertTrue(stage["status"].startswith("BLOCKED_"))
            for sample in row["samples_only_not_full_materialization"].values():
                self.assertIsNone(
                    sample["coefficient_factorization"]["pairing_sum"]
                )
                self.assertIsNone(
                    sample["downstream_fail_closed"]["renormalized_coefficient"][
                        "value"
                    ]
                )

    def test_missing_projection_candidate_is_rejected(self) -> None:
        parent = self.parents[0]
        vertex = next(item for item in parent.graph["vertices"] if item["vertex_id"] == "A")
        option = parent.wick_join.local_options["A"][0]
        assignment = next(
            item
            for item in parent.wick_join.assignment_catalog["A"]
            if item["assignment_id"] == option["assignment_id"]
        )
        with self.assertRaises(amplitude.ProjectionJoinError):
            amplitude.join_local_option(
                parent.wick_join, vertex, option, assignment, {}
            )

    def test_duplicate_port_mismatch_and_double_coefficient_are_rejected(self) -> None:
        parent = self.by_key[
            ("G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4", "direct")
        ]
        vertex = next(item for item in parent.graph["vertices"] if item["vertex_id"] == "C")
        option = parent.wick_join.local_options["C"][0]
        assignment = next(
            item
            for item in parent.wick_join.assignment_catalog["C"]
            if item["assignment_id"] == option["assignment_id"]
        )
        ref = parent.local_options["C"][0]["background_projection"]
        candidate = deepcopy(
            self.payload["projection_candidate_dictionary"][ref["projection_candidate_id"]]
        )
        duplicate = deepcopy(candidate)
        duplicate["background_port_projections"][1]["topology_port_id"] = duplicate[
            "background_port_projections"
        ][0]["topology_port_id"]
        with self.assertRaises(amplitude.ProjectionJoinError):
            amplitude.validate_projection_candidate(
                parent.wick_join, vertex, option, assignment, duplicate
            )
        double = deepcopy(candidate)
        double["assembled_vertex_coefficient"] = {"rendered": "1"}
        with self.assertRaises(amplitude.CoefficientApplicationError):
            amplitude.validate_projection_candidate(
                parent.wick_join, vertex, option, assignment, double
            )

    def test_non_Project_propagator_is_rejected(self) -> None:
        parent = self.parents[0]
        source = parent.wick_join.materialize(0)["edges"][0]
        bad_kernel = deepcopy(parent.kernel_certificate)
        bad_kernel["derived_equations"]["G_V"] = "+2*g^2/p^2"
        with self.assertRaises(amplitude.PropagatorContractError):
            amplitude.attach_vector_propagator(
                parent.graph, parent.orientation, source, bad_kernel
            )

    def test_generated_outputs_and_audit_are_reproducible(self) -> None:
        generated = json.loads(
            (ROOT / "generated/step6/two-loop-amplitude-ir/pre-dalgebra-amplitude-ir.json").read_text()
        )
        audit = json.loads(
            (ROOT / "audits/step6-two-loop-amplitude-ir-verification.json").read_text()
        )
        self.assertEqual(generated, self.payload)
        rebuilt = amplitude.build_audit(
            self.payload,
            self.parents,
            audit["artifact_sha256"],
        )
        self.assertEqual(audit, rebuilt)
        self.assertEqual(audit["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
