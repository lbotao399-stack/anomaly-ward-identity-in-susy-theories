from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
import unittest

from scripts.step6_two_loop_graphir import (
    MOMENTUM_BASIS,
    build_audit,
    build_bundle,
    build_direct_i2_s3_squared_s4,
    build_direct_i2_s3_squared_s4_double_background_s4,
    build_direct_i3_s3_cubed,
    build_raw_marked_k23_theta_lift,
    digest,
    enumerate_valence_families,
)


ROOT = Path(__file__).resolve().parents[1]


class Step6TwoLoopGraphIRTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bundle = build_bundle()
        self.direct_i3 = build_direct_i3_s3_cubed()
        self.direct_i2 = build_direct_i2_s3_squared_s4()
        self.direct_i2_s4_b2 = build_direct_i2_s3_squared_s4_double_background_s4()
        self.raw = build_raw_marked_k23_theta_lift()
        self.graphs = [self.direct_i3, self.direct_i2, self.direct_i2_s4_b2, self.raw]

    def test_exactly_twelve_valence_families_are_not_graphs(self) -> None:
        families = enumerate_valence_families()
        self.assertEqual(len(families), 12)
        self.assertEqual(
            {family["family_id"] for family in families},
            {
                "I2__S3^4",
                "I2__S3^2__S4^1",
                "I2__S3^1__S5^1",
                "I2__S4^2",
                "I2__S6^1",
                "I3__S3^3",
                "I3__S3^1__S4^1",
                "I3__S5^1",
                "I4__S3^2",
                "I4__S4^1",
                "I5__S3^1",
                "I6__NO_ACTION_VERTEX",
            },
        )
        for family in families:
            self.assertEqual(family["classification"], "VALENCE_NOT_GRAPH")
            self.assertIsNone(family["graph_ir"])
            self.assertEqual(family["typed_valence_totals"]["background_distribution"], "UNRESOLVED")
            identity = family["identity"]
            self.assertEqual(identity["lhs"], 4)
            self.assertEqual(identity["rhs"], 4)
            self.assertEqual(identity["L"], 2)
            self.assertEqual(
                family["typed_valence_totals"]["total_valence"],
                family["typed_valence_totals"]["quantum_valence"] + 2,
            )

    def test_constructed_graphs_satisfy_both_exact_two_loop_identities(self) -> None:
        for graph in self.graphs:
            self.assertEqual(
                graph["graph_kind"],
                "TOPOLOGY_GRAPHIR_NO_FIELD_OR_WICK_ASSIGNMENT",
            )
            self.assertEqual(graph["sector"], "EUCLIDEAN_N4_SYM_PURE_GAUGE")
            self.assertEqual(
                graph["operator_seed"],
                "nabla_-[(nabla_+W_+)^A (nabla_+W_+)^B]",
            )
            identities = graph["identities"]
            self.assertTrue(identities["connected"])
            self.assertEqual(identities["L"], 2)
            self.assertEqual(
                identities["L"],
                identities["I"] - identities["V"] + 1,
            )
            self.assertEqual(identities["valence_identity"]["lhs"], 4)
            self.assertEqual(identities["valence_identity"]["rhs"], 4)
            self.assertTrue(identities["total_half_edge_identity"]["passed"])
            self.assertTrue(identities["background_valence_identity"]["passed"])
            self.assertTrue(identities["quantum_valence_identity"]["passed"])

    def test_typed_vertices_separate_total_background_and_quantum_valence(self) -> None:
        for graph in self.graphs:
            self.assertEqual(sum(vertex["background_valence"] for vertex in graph["vertices"]), 2)
            self.assertEqual(
                sum(vertex["quantum_valence"] for vertex in graph["vertices"]),
                2 * len(graph["internal_edges"]),
            )
            for vertex in graph["vertices"]:
                self.assertEqual(
                    vertex["total_valence"],
                    vertex["background_valence"] + vertex["quantum_valence"],
                )
                if vertex["role"] == "COMPOSITE_INSERTION":
                    self.assertEqual(vertex["background_valence"], 0)
                    source = [
                        injection
                        for injection in vertex["momentum_injections"]
                        if injection["kind"] == "COMPOSITE_SOURCE_MOMENTUM"
                    ]
                    self.assertEqual(len(source), 1)
                    self.assertFalse(source[0]["counts_toward_background_valence"])
            certificate = graph["typed_port_saturation"]
            self.assertTrue(certificate["each_quantum_port_used_once"])
            self.assertEqual(
                certificate["all_quantum_ports"],
                certificate["edge_endpoint_ports"],
            )

    def test_two_direct_families_are_literal_k4_minus_one_edge(self) -> None:
        for graph in (self.direct_i3, self.direct_i2, self.direct_i2_s4_b2):
            vertices = {vertex["vertex_id"] for vertex in graph["vertices"]}
            all_pairs = {frozenset(pair) for pair in combinations(vertices, 2)}
            graph_pairs = {
                frozenset((edge["source"], edge["target"]))
                for edge in graph["internal_edges"]
            }
            self.assertEqual(len(vertices), 4)
            self.assertEqual(len(graph_pairs), 5)
            self.assertEqual(len(all_pairs - graph_pairs), 1)
            self.assertEqual(graph["topology"], "K4_MINUS_ONE_EDGE")
            self.assertEqual(graph["classification"], "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT")
        self.assertEqual(self.direct_i3["valence_family_id"], "I3__S3^3")
        self.assertEqual(self.direct_i2["valence_family_id"], "I2__S3^2__S4^1")
        self.assertEqual(self.direct_i2_s4_b2["valence_family_id"], "I2__S3^2__S4^1")
        self.assertEqual(
            [vertex["background_valence"] for vertex in self.direct_i2_s4_b2["vertices"]],
            [0, 0, 0, 2],
        )

    def test_raw_marked_graph_is_literal_k23_and_not_a_five_edge_graph(self) -> None:
        self.assertEqual(self.raw["valence_family_id"], "I2__S3^4")
        self.assertEqual(self.raw["identities"]["V"], 5)
        self.assertEqual(self.raw["identities"]["I"], 6)
        self.assertEqual(self.raw["identities"]["L"], 2)
        self.assertEqual(
            {
                frozenset((edge["source"], edge["target"]))
                for edge in self.raw["internal_edges"]
            },
            {
                frozenset((high, low))
                for high in ("C", "D")
                for low in ("I", "A", "B")
            },
        )
        suppression = self.raw["homeomorphic_suppression"]
        self.assertEqual(
            suppression["status"],
            "BLOCKED_NO_TYPED_DALGEBRA_PROPAGATOR_COLLAPSE_CERTIFICATE",
        )
        self.assertFalse(suppression["raw_graph_is_literal_k4_minus_edge"])
        self.assertEqual(
            suppression["forbidden_inference"],
            "DO_NOT_IDENTIFY_RAW_SIX_EDGE_GRAPH_WITH_FIVE_EDGE_BITRIANGLE",
        )

    def test_raw_routing_and_six_denominator_ast_are_exact(self) -> None:
        self.assertEqual(tuple(self.raw["momentum_contract"]["basis"]), MOMENTUM_BASIS)
        self.assertEqual(
            [edge["momentum"] for edge in self.raw["internal_edges"]],
            ["k", "k-P", "l", "l-p1", "-k-l", "-k-l-p2"],
        )
        self.assertEqual(
            self.raw["denominator_ast"]["rendered"],
            "k^2 (k-P)^2 l^2 (l-p1)^2 (k+l)^2 (k+l+p2)^2",
        )
        self.assertEqual(self.raw["denominator_ast"]["op"], "product")
        self.assertEqual(len(self.raw["denominator_ast"]["factors"]), 6)
        for factor in self.raw["denominator_ast"]["factors"]:
            self.assertEqual(factor["base"]["op"], "square")
            self.assertEqual(
                factor["base"]["space"],
                "PROJECT_EUCLIDEAN_DRED_HAT_MOMENTUM_SUBSPACE",
            )
            self.assertEqual(factor["base"]["bilinear_form"], "POSITIVE_EUCLIDEAN")

    def test_incidence_conservation_is_exact_for_both_orientations(self) -> None:
        for graph in self.graphs:
            for orientation in ("direct", "reflected"):
                certificate = graph["incidence_routing"][orientation]
                self.assertTrue(certificate["passed"])
                self.assertEqual(
                    certificate["rank"],
                    certificate["expected_connected_rank"],
                )
                self.assertTrue(certificate["each_column_has_one_source_and_one_target"])
                for balance in certificate["vertex_conservation"].values():
                    self.assertTrue(balance["passed"])
                    self.assertEqual(balance["reduced_balance"], [0, 0, 0, 0])
                    self.assertIn(balance["relation_multiple"], (0, 1))

    def test_all_simple_one_loop_cycles_include_left_right_and_outer(self) -> None:
        for graph in self.graphs:
            cycle_ir = graph["simple_one_loop_cycles"]
            self.assertEqual(
                [cycle["cycle_id"] for cycle in cycle_ir["cycles"]],
                ["left", "right", "outer"],
            )
            self.assertTrue(cycle_ir["gf2_relation"]["passed"])
            self.assertEqual(cycle_ir["gf2_relation"]["residual_edge_ids"], [])
            self.assertEqual(len(cycle_ir["overlap_relations"]), 3)
            for relation in cycle_ir["overlap_relations"]:
                self.assertEqual(relation["relation"], "OVERLAP_NON_NESTED")
                self.assertFalse(relation["edge_disjoint"])
                self.assertFalse(relation["left_subset_right"])
                self.assertFalse(relation["right_subset_left"])
                self.assertIn(relation["symmetric_difference_cycle"], ("left", "right", "outer"))
        raw_by_name = {
            cycle["cycle_id"]: set(cycle["edge_ids"])
            for cycle in self.raw["simple_one_loop_cycles"]["cycles"]
        }
        self.assertEqual(raw_by_name["left"], {"e_CI", "e_ID", "e_CA", "e_AD"})
        self.assertEqual(raw_by_name["right"], {"e_CI", "e_ID", "e_CB", "e_BD"})
        self.assertEqual(raw_by_name["outer"], {"e_CA", "e_AD", "e_CB", "e_BD"})

    def test_automorphism_and_orientation_hashes_are_recomputable(self) -> None:
        expected_orders = {
            self.direct_i3["graph_id"]: (2, 1),
            self.direct_i2["graph_id"]: (1, 1),
            self.direct_i2_s4_b2["graph_id"]: (2, 2),
            self.raw["graph_id"]: (4, 2),
        }
        for graph in self.graphs:
            self.assertEqual(
                (
                    graph["automorphisms"]["typed_external_unlabeled"]["order"],
                    graph["automorphisms"]["background_source_labeled"]["order"],
                ),
                expected_orders[graph["graph_id"]],
            )
            for kind in ("typed_external_unlabeled", "background_source_labeled"):
                record = graph["automorphisms"][kind]
                payload = {key: value for key, value in record.items() if key != "automorphism_hash"}
                self.assertEqual(record["automorphism_hash"], digest(payload))
            direct = graph["orientations"]["direct"]
            reflected = graph["orientations"]["reflected"]
            self.assertEqual(
                graph["orientations"]["semantics"],
                "EDGE_DIRECTION_AND_MOMENTUM_SIGN_ONLY_NOT_A_WICK_OR_FIELD_ORIENTATION",
            )
            self.assertNotEqual(direct["orientation_hash"], reflected["orientation_hash"])
            for record in (direct, reflected):
                payload = {key: value for key, value in record.items() if key != "orientation_hash"}
                self.assertEqual(record["orientation_hash"], digest(payload))
            direct_by_edge = {edge["edge_id"]: edge for edge in direct["edges"]}
            reflected_by_edge = {edge["edge_id"]: edge for edge in reflected["edges"]}
            for edge_id, direct_edge in direct_by_edge.items():
                reflected_edge = reflected_by_edge[edge_id]
                self.assertEqual(reflected_edge["source"], direct_edge["target"])
                self.assertEqual(reflected_edge["target"], direct_edge["source"])
                self.assertEqual(
                    reflected_edge["momentum_vector"],
                    [-coefficient for coefficient in direct_edge["momentum_vector"]],
                )

    def test_every_downstream_computational_stage_fails_closed(self) -> None:
        for graph in self.graphs:
            for stage in graph["downstream_fail_closed"].values():
                self.assertTrue(stage["status"].startswith("BLOCKED_"))
                self.assertIsNone(stage["value"])
            for edge in graph["internal_edges"]:
                self.assertIsNone(edge["propagator"])
                self.assertTrue(edge["propagator_status"].startswith("BLOCKED_"))
        for stage in self.bundle["downstream_fail_closed"].values():
            self.assertTrue(stage["status"].startswith("BLOCKED_"))
            self.assertIsNone(stage["value"])

    def test_generated_master_is_exactly_reproducible(self) -> None:
        generated = ROOT / "generated" / "step6" / "two-loop-graphir" / "two-loop-graphir.json"
        self.assertTrue(generated.exists())
        self.assertEqual(json.loads(generated.read_text(encoding="utf-8")), self.bundle)

    def test_checked_in_audit_passes_independent_reconstruction(self) -> None:
        audit_path = ROOT / "audits" / "step6-two-loop-graphir-verification.json"
        checked_in = json.loads(audit_path.read_text(encoding="utf-8"))
        reconstructed = build_audit(self.bundle)
        self.assertEqual(checked_in["status"], "PASS")
        self.assertEqual(checked_in["failure_count"], 0)
        self.assertEqual(
            [(check["id"], check["passed"]) for check in checked_in["checks"]],
            [(check["id"], check["passed"]) for check in reconstructed["checks"]],
        )
        self.assertTrue(checked_in["artifact_sha256"])


if __name__ == "__main__":
    unittest.main()
