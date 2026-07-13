from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import unittest

from scripts.step6_two_loop_forest import (
    NumeratorScalingCertificate,
    build_audit,
    build_forest_bundle,
    build_graph_forest_record,
    connected_census,
    enumerate_connected_edge_subgraphs,
    evanescent_finite_remainder,
    rank2_coefficient,
    rank4_coefficients,
    subgraphs_compatible,
)
from scripts.step6_two_loop_graphir import (
    build_direct_i2_s3_squared_s4,
    build_direct_i2_s3_squared_s4_double_background_s4,
    build_direct_i3_s3_cubed,
    build_raw_marked_k23_theta_lift,
)


ROOT = Path(__file__).resolve().parents[1]


class Step6TwoLoopForestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.direct_i3 = build_direct_i3_s3_cubed()
        self.direct_i2 = build_direct_i2_s3_squared_s4()
        self.direct_i2_s4_b2 = build_direct_i2_s3_squared_s4_double_background_s4()
        self.raw = build_raw_marked_k23_theta_lift()
        self.graphs = [self.direct_i3, self.direct_i2, self.direct_i2_s4_b2, self.raw]
        self.bundle = build_forest_bundle()

    def test_generic_connected_subgraph_enumerator_counts_every_nonempty_edge_subset(self) -> None:
        for graph, expected in (
            (self.direct_i3, 29),
            (self.direct_i2, 29),
            (self.direct_i2_s4_b2, 29),
            (self.raw, 51),
        ):
            records = enumerate_connected_edge_subgraphs(graph)
            self.assertEqual(len(records), expected)
            self.assertEqual(len({record["subgraph_hash"] for record in records}), expected)
            for record in records:
                counts = record["counts"]
                self.assertEqual(counts["L"], counts["I"] - counts["V"] + 1)
                self.assertTrue(record["connected"])

    def test_literal_and_raw_census_classes_are_exact(self) -> None:
        direct_census = connected_census(enumerate_connected_edge_subgraphs(self.direct_i3))
        self.assertEqual(
            {
                (
                    item["L"],
                    item["I"],
                    item["V"],
                    item["one_particle_irreducible"],
                ): item["count"]
                for item in direct_census
            },
            {
                (0, 1, 2, False): 5,
                (0, 2, 3, False): 8,
                (0, 3, 4, False): 8,
                (1, 3, 3, True): 2,
                (1, 4, 4, False): 4,
                (1, 4, 4, True): 1,
                (2, 5, 4, True): 1,
            },
        )
        raw_census = connected_census(enumerate_connected_edge_subgraphs(self.raw))
        self.assertEqual(
            {
                (
                    item["L"],
                    item["I"],
                    item["V"],
                    item["one_particle_irreducible"],
                ): item["count"]
                for item in raw_census
            },
            {
                (0, 1, 2, False): 6,
                (0, 2, 3, False): 9,
                (0, 3, 4, False): 14,
                (0, 4, 5, False): 12,
                (1, 4, 4, True): 3,
                (1, 5, 5, False): 6,
                (2, 6, 5, True): 1,
            },
        )

    def test_left_right_outer_are_the_only_proper_one_loop_1pi_subgraphs(self) -> None:
        expected_edges = {
            self.direct_i3["graph_id"]: {
                "left": {"e_CI", "e_CA", "e_AI"},
                "right": {"e_CI", "e_CB", "e_BI"},
                "outer": {"e_CA", "e_AI", "e_CB", "e_BI"},
            },
            self.direct_i2["graph_id"]: {
                "left": {"e_BI", "e_IC", "e_BC"},
                "right": {"e_BA", "e_AC", "e_BC"},
                "outer": {"e_BI", "e_IC", "e_BA", "e_AC"},
            },
            self.direct_i2_s4_b2["graph_id"]: {
                "left": {"e_AI", "e_IB", "e_BA"},
                "right": {"e_CA", "e_BC", "e_BA"},
                "outer": {"e_AI", "e_IB", "e_CA", "e_BC"},
            },
            self.raw["graph_id"]: {
                "left": {"e_CI", "e_ID", "e_CA", "e_AD"},
                "right": {"e_CI", "e_ID", "e_CB", "e_BD"},
                "outer": {"e_CA", "e_AD", "e_CB", "e_BD"},
            },
        }
        for graph in self.graphs:
            records = enumerate_connected_edge_subgraphs(graph)
            proper = {
                record["subgraph_id"]: set(record["edge_ids"])
                for record in records
                if record["proper"]
                and record["one_particle_irreducible"]
                and record["counts"]["L"] > 0
            }
            self.assertEqual(proper, expected_edges[graph["graph_id"]])

    def test_pairwise_overlap_forbids_every_two_cycle_forest(self) -> None:
        for graph_record in self.bundle["graph_records"]:
            forests = graph_record["forests"]
            self.assertEqual(
                [forest["subgraph_ids"] for forest in forests["structurally_compatible_forests"]],
                [[], ["left"], ["outer"], ["right"]],
            )
            self.assertEqual(forests["current_graph_maximum_structural_forest_cardinality"], 1)
            for relation in forests["pair_relations"]:
                self.assertFalse(relation["compatible"])
                self.assertEqual(relation["relation"], "OVERLAP_NON_NESTED")
                self.assertTrue(relation["intersection_edge_ids"])

        records = enumerate_connected_edge_subgraphs(self.direct_i3)
        by_id = {record["subgraph_id"]: record for record in records}
        self.assertFalse(subgraphs_compatible(by_id["left"], by_id["right"]))
        self.assertFalse(subgraphs_compatible(by_id["left"], by_id["outer"]))
        self.assertFalse(subgraphs_compatible(by_id["right"], by_id["outer"]))

    def test_unknown_rho_blocks_every_power_counting_forest(self) -> None:
        for graph_record in self.bundle["graph_records"]:
            power = graph_record["power_counting"]
            self.assertEqual(power["status"], "BLOCKED_RHO_UNKNOWN_FAIL_CLOSED")
            self.assertIsNone(graph_record["forests"]["power_counting_forests"])
            for entry in power["entries"]:
                self.assertEqual(entry["rho"], "UNKNOWN")
                self.assertEqual(entry["omega4"], "UNKNOWN")
                self.assertIsNone(entry["superficially_divergent_candidate"])
                self.assertIsNone(entry["actual_uv_pole"])

    def test_explicit_rho_certificate_controls_only_superficial_candidates(self) -> None:
        graph = self.direct_i3
        certificate = NumeratorScalingCertificate(
            graph_hash=graph["graph_hash"],
            rho_by_subgraph={
                "left": 2,
                "right": 1,
                "outer": 4,
                "full": 2,
            },
            source_status="UNIT_TEST_EXPLICIT_RHO_FIXTURE",
            adapted_basis_status="UNIT_TEST_ADAPTED_BASIS_FIXTURE",
        )
        record = build_graph_forest_record(graph, certificate)
        entries = {entry["subgraph_id"]: entry for entry in record["power_counting"]["entries"]}
        self.assertEqual(entries["left"]["omega4"], 0)
        self.assertTrue(entries["left"]["superficially_divergent_candidate"])
        self.assertEqual(entries["right"]["omega4"], -1)
        self.assertFalse(entries["right"]["superficially_divergent_candidate"])
        self.assertEqual(entries["outer"]["omega4"], 0)
        self.assertTrue(entries["outer"]["superficially_divergent_candidate"])
        self.assertEqual(entries["full"]["omega4"], 0)
        self.assertTrue(entries["full"]["superficially_divergent_candidate"])
        self.assertEqual(
            [forest["subgraph_ids"] for forest in record["forests"]["power_counting_forests"]],
            [[], ["left"], ["outer"]],
        )
        for entry in entries.values():
            self.assertIsNone(entry["actual_uv_pole"])
        self.assertIsNone(record["renormalization_ast"]["uv_pole"])
        self.assertIsNone(record["renormalization_ast"]["renormalized_coefficient"])

    def test_certificate_rejects_wrong_graph_hash_and_invalid_rho(self) -> None:
        with self.assertRaises(ValueError):
            NumeratorScalingCertificate(
                graph_hash=self.direct_i3["graph_hash"],
                rho_by_subgraph={"left": -1},
            )
        wrong = NumeratorScalingCertificate(
            graph_hash="wrong-hash",
            rho_by_subgraph={"left": None, "right": None, "outer": None, "full": None},
        )
        with self.assertRaises(ValueError):
            build_graph_forest_record(self.direct_i3, wrong)

    def test_contracted_cograph_counts_and_topologies_are_exact(self) -> None:
        by_graph = {record["source_graph_id"]: record for record in self.bundle["graph_records"]}
        for graph in (self.direct_i3, self.direct_i2, self.direct_i2_s4_b2):
            cographs = {
                item["subgraph_id"]: item
                for item in by_graph[graph["graph_id"]]["contractions"]["cographs"]
            }
            for name in ("left", "right"):
                self.assertEqual(cographs[name]["counts"], {"L": 1, "I": 2, "V": 2})
                self.assertEqual(cographs[name]["reduced_topology"], "TWO_EDGE_ONE_LOOP_BUBBLE")
            self.assertEqual(cographs["outer"]["counts"], {"L": 1, "I": 1, "V": 1})
            self.assertEqual(cographs["outer"]["reduced_topology"], "ONE_EDGE_SELF_LOOP_TADPOLE")
            self.assertEqual(
                cographs["outer"]["scaleless_status"],
                "NOT_EVALUATED_REQUIRES_CONTRACTED_NUMERATOR_AND_EXTERNAL_INJECTION",
            )
        raw_record = by_graph[self.raw["graph_id"]]
        for cograph in raw_record["contractions"]["cographs"]:
            self.assertEqual(cograph["counts"], {"L": 1, "I": 2, "V": 2})
            self.assertEqual(cograph["reduced_topology"], "TWO_EDGE_ONE_LOOP_BUBBLE")

    def test_rprime_counterterm_and_R_are_symbolic_and_use_distinct_KUV(self) -> None:
        for record in self.bundle["graph_records"]:
            ast = record["renormalization_ast"]
            self.assertEqual(ast["uv_projector"]["symbol"], "K_UV")
            self.assertTrue(ast["uv_projector"]["distinct_from_superspace_projector"])
            self.assertIn("K_+=", ast["uv_projector"]["superspace_projector"])
            self.assertEqual(ast["rprime"]["op"], "SUM")
            self.assertEqual(len(ast["rprime"]["terms"]), 4)
            self.assertEqual(ast["overall_counterterm"]["op"], "NEGATIVE_UV_POLE_PROJECTOR")
            self.assertEqual(ast["renormalized"]["op"], "ONE_MINUS_UV_POLE_PROJECTOR")
            self.assertEqual(ast["status"], "BLOCKED_NUMERATOR_SCALING_CERTIFICATE")
            self.assertIsNone(ast["uv_pole"])

    def test_two_loop_measure_and_metric_types_are_locked_without_bare_epsilon(self) -> None:
        dred = self.bundle["dred_architecture"]
        self.assertEqual(dred["dimension"], "d=4-2*epsilon")
        self.assertEqual(dred["measure"]["mu_power"], "mu^(4*epsilon)")
        self.assertEqual(
            dred["measure"]["two_loop"],
            "mu^(4*epsilon) d^d k/(2*pi)^d d^d l/(2*pi)^d",
        )
        self.assertEqual(dred["metric_types"]["spin_dalgebra_metric"], "delta_(4)")
        self.assertEqual(dred["metric_types"]["loop_tensor_metric"], "hat_delta")
        self.assertEqual(dred["metric_types"]["bare_numerator_epsilon_status"], "FORBIDDEN")

    def test_rank_two_and_rank_four_rational_functions_are_exact(self) -> None:
        self.assertEqual(rank2_coefficient(Fraction(4)), Fraction(1, 4))
        d = Fraction(7, 2)
        X, Y, Z = Fraction(3), Fraction(5), Fraction(11)
        A, B, C = rank4_coefficients(d, X, Y, Z)
        self.assertEqual(d * d * A + d * B + d * C, X)
        self.assertEqual(d * A + d * d * B + d * C, Y)
        self.assertEqual(d * A + d * B + d * d * C, Z)
        identical = rank4_coefficients(d, Fraction(13), Fraction(13), Fraction(13))
        expected = Fraction(13) / (d * (d + 2))
        self.assertEqual(identical, (expected, expected, expected))
        with self.assertRaises(ZeroDivisionError):
            rank2_coefficient(Fraction(0))
        for singular in (Fraction(0), Fraction(1), Fraction(-2)):
            with self.assertRaises(ZeroDivisionError):
                rank4_coefficients(singular, X, Y, Z)

    def test_laurent_valuation_rule_through_double_pole_is_exact(self) -> None:
        self.assertEqual(
            evanescent_finite_remainder(
                {1: Fraction(3), 2: Fraction(5)},
                {1: Fraction(2), 2: Fraction(7)},
            ),
            Fraction(41),
        )
        self.assertEqual(
            evanescent_finite_remainder(
                {1: Fraction(3), 2: Fraction(5)},
                {1: Fraction(2), 2: Fraction(7)},
                pole_order=1,
            ),
            Fraction(6),
        )
        with self.assertRaises(ValueError):
            evanescent_finite_remainder({}, {}, pole_order=3)

    def test_generated_bundle_is_exactly_reproducible(self) -> None:
        path = ROOT / "generated" / "step6" / "two-loop-forest" / "two-loop-forest.json"
        self.assertTrue(path.exists())
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), self.bundle)

    def test_checked_in_audit_passes_independent_reconstruction(self) -> None:
        path = ROOT / "audits" / "step6-two-loop-forest-verification.json"
        checked_in = json.loads(path.read_text(encoding="utf-8"))
        reconstructed = build_audit(self.bundle)
        self.assertEqual(checked_in["status"], "PASS")
        self.assertEqual(checked_in["failure_count"], 0)
        self.assertEqual(
            [(check["id"], check["passed"]) for check in checked_in["checks"]],
            [(check["id"], check["passed"]) for check in reconstructed["checks"]],
        )
        self.assertEqual(len(checked_in["artifact_sha256"]), 4)
        for artifact_hash in checked_in["artifact_sha256"].values():
            self.assertEqual(len(artifact_hash), 64)


if __name__ == "__main__":
    unittest.main()
