from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from math import factorial, prod
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import step6_sd_orbit as sd
from scripts import step6_two_loop_graphir as graphir


class Step6SDOrbitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.audit = sd.write_outputs()
        cls.graphs = graphir.build_bundle()["literal_direct_graphs"]

    def test_audit_and_global_census(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["totals"]["failed"], 0)
        self.assertEqual(self.payload["orbit_count"], 6)
        self.assertEqual(
            self.payload["global_census"],
            {
                "rooted_open_cut_count": 60,
                "rooted_contact_child_count": 60,
                "rooted_bubble_derivation_path_count": 216,
            },
        )

    def test_direct_and_reflected_orbits_remain_separate(self):
        pairs = {
            (orbit["parent_graph_id"], orbit["orientation"])
            for orbit in self.payload["orbits"]
        }
        graph_ids = {graph["graph_id"] for graph in self.graphs}
        self.assertEqual(
            pairs,
            {
                (graph_id, orientation)
                for graph_id in graph_ids
                for orientation in ("direct", "reflected")
            },
        )

    def test_each_parent_has_ten_rooted_cuts_contacts_and_36_bubbles(self):
        for orbit in self.payload["orbits"]:
            self.assertEqual(len(orbit["rooted_open_cuts"]), 10)
            self.assertEqual(len(orbit["rooted_contact_children"]), 10)
            self.assertEqual(len(orbit["rooted_bubble_derivation_paths"]), 36)
            self.assertEqual(
                orbit["census"]["cycle_length_histogram_for_rooted_cuts"],
                {3: 8, 4: 2},
            )
            self.assertEqual(
                sum(orbit["census"]["bubble_family_signature_histogram"].values()),
                36,
            )

    def test_every_parent_edge_has_both_endpoint_roots(self):
        graph_by_id = {graph["graph_id"]: graph for graph in self.graphs}
        for orbit in self.payload["orbits"]:
            graph = graph_by_id[orbit["parent_graph_id"]]
            roots_by_edge = {}
            for cut in orbit["rooted_open_cuts"]:
                roots_by_edge.setdefault(cut["cut_edge_id"], set()).add(
                    cut["root_vertex"]
                )
            self.assertEqual(set(roots_by_edge), {edge["edge_id"] for edge in graph["internal_edges"]})
            for edge in graph["internal_edges"]:
                self.assertEqual(
                    roots_by_edge[edge["edge_id"]],
                    {edge["source"], edge["target"]},
                )

    def test_open_cut_incidence_and_denominator(self):
        for orbit in self.payload["orbits"]:
            for cut in orbit["rooted_open_cuts"]:
                self.assertEqual(cut["counts"], {"V": 4, "I_propagator": 4, "L": 1})
                self.assertEqual(len(cut["open_cut_endpoints"]), 2)
                self.assertEqual(
                    {row["rooted_functional_derivative_endpoint"] for row in cut["open_cut_endpoints"]},
                    {False, True},
                )
                self.assertEqual(len(cut["denominator_ast"]["factors"]), 4)
                self.assertNotIn(
                    cut["cut_edge_id"],
                    {factor["edge_id"] for factor in cut["denominator_ast"]["factors"]},
                )

    def test_contact_children_have_exact_fused_valence(self):
        for orbit in self.payload["orbits"]:
            for child in orbit["rooted_contact_children"]:
                self.assertEqual(child["counts"], {"V": 3, "I_propagator": 4, "L": 2})
                merged = child["merged_vertex"]
                origins = [
                    domain
                    for domain in child["source_occurrence_product_preserved"]
                ]
                self.assertEqual(len(origins), 2)
                self.assertEqual(
                    merged["total_valence"],
                    sum(int(domain["family"][1:]) for domain in origins) - 2,
                )
                self.assertEqual(
                    merged["quantum_valence"],
                    sum(
                        1
                        for edge in child["remaining_propagator_edges"]
                        for endpoint in (edge["source"], edge["target"])
                        if endpoint == merged["vertex_id"]
                    ),
                )

    def test_i3_s3_cubed_contacts_are_all_quartic(self):
        for orbit in self.payload["orbits"]:
            if orbit["parent_graph_id"] != "G6_DIRECT_K4ME_I3_S3CUBED":
                continue
            classes = {
                child["contact_classification"]
                for child in orbit["rooted_contact_children"]
            }
            self.assertEqual(
                classes,
                {"QUARTIC_INSERTION_CONTACT", "QUARTIC_ACTION_CONTACT"},
            )
            self.assertEqual(
                {child["merged_vertex"]["family"] for child in orbit["rooted_contact_children"]},
                {"I4", "S4"},
            )

    def test_contact_candidate_never_imports_candidate_coefficient(self):
        for orbit in self.payload["orbits"]:
            for child in orbit["rooted_contact_children"]:
                candidate = child["contact_grammar_candidate_domain"]
                self.assertIn("BLOCKED_ORDERED_FUNCTIONAL_DERIVATIVE", candidate["coefficient_status"])
                if candidate["merged_role"] == "COMPOSITE_INSERTION":
                    self.assertIsNone(candidate["coefficient_equality_to_candidate"])
                else:
                    self.assertTrue(
                        all(
                            row["coefficient_equality_to_candidate"] is None
                            for row in candidate["sector_compatibility"]
                        )
                    )

    def test_every_bubble_is_two_parallel_propagators(self):
        for orbit in self.payload["orbits"]:
            for bubble in orbit["rooted_bubble_derivation_paths"]:
                self.assertEqual(bubble["counts"], {"V": 2, "I_propagator": 2, "L": 1})
                self.assertEqual(len(bubble["supervertices"]), 2)
                endpoints = {
                    tuple(sorted((edge["source"], edge["target"])))
                    for edge in bubble["propagator_edges"]
                }
                self.assertEqual(len(endpoints), 1)
                self.assertEqual(
                    [factor["edge_id"] for factor in bubble["denominator_ast"]["factors"]],
                    bubble["retained_propagator_edge_ids"],
                )
                self.assertEqual(
                    bubble["automorphisms"]["parallel_edge_permutation_order"], 2
                )
                self.assertEqual(
                    bubble["bubble_family_signature_sha256"],
                    sd.digest(bubble["bubble_family_signature_record"]),
                )

    def test_bubble_path_count_formula(self):
        for orbit in self.payload["orbits"]:
            count = sum(
                len(list(__import__("itertools").combinations(cut["unique_cycle_edge_ids"], 2)))
                for cut in orbit["rooted_open_cuts"]
            )
            self.assertEqual(count, 36)

    def test_exact_functional_and_KG_signs(self):
        self.assertEqual(self.payload["Schwinger_Dyson_identity"]["delta_F_sign"], 1)
        self.assertEqual(self.payload["Schwinger_Dyson_identity"]["minus_F_delta_S_sign"], -1)
        self.assertEqual(self.payload["fixed_kernel_identity"]["K_times_G"], 1)
        self.assertEqual(self.payload["fixed_kernel_identity"]["G_times_K"], 1)
        for orbit in self.payload["orbits"]:
            for child in [
                *orbit["rooted_open_cuts"],
                *orbit["rooted_contact_children"],
                *orbit["rooted_bubble_derivation_paths"],
            ]:
                expected = (
                    1
                    if child["SD_functional_channel"]["channel"] == "DELTA_F_INSERTION"
                    else -1
                )
                self.assertEqual(
                    child["SD_functional_channel"]["SD_zero_sum_sign"], expected
                )

    def test_action_expansion_factor_is_exact_for_all_sector_assignments(self):
        for orbit in self.payload["orbits"]:
            table = orbit["source_action_sector_expansion_table"]
            self.assertEqual(len(table), 8)
            for row in table:
                multiplicities = row["family_sector_multiplicities"]
                denominator = prod(factorial(value) for value in multiplicities.values())
                expected = Fraction(-1, denominator)
                rational = row["exponential_factor"]["rational"]
                actual = Fraction(rational["numerator"], rational["denominator"])
                self.assertEqual(actual, expected)
                self.assertEqual(row["exponential_factor"]["N"], 3)
                self.assertEqual(row["exponential_factor"]["hbar_power"], -3)

    def test_automorphisms_are_never_divided_again(self):
        for orbit in self.payload["orbits"]:
            for child in [
                *orbit["rooted_open_cuts"],
                *orbit["rooted_contact_children"],
                *orbit["rooted_bubble_derivation_paths"],
            ]:
                auto = child["automorphisms"]
                self.assertGreaterEqual(auto["full_multigraph_order_typed"], 1)
                self.assertGreaterEqual(
                    auto["full_multigraph_order_background_source_labeled"], 1
                )
                self.assertIsNone(auto["automorphism_denominator_applied"])

    def test_orbit_links_are_exact_and_unique(self):
        for orbit in self.payload["orbits"]:
            cut_ids = {row["cut_descendant_id"] for row in orbit["rooted_open_cuts"]}
            contact_ids = {
                row["contact_child_id"] for row in orbit["rooted_contact_children"]
            }
            bubble_ids = {
                row["bubble_child_id"]
                for row in orbit["rooted_bubble_derivation_paths"]
            }
            self.assertEqual(len(orbit["orbit_links"]), 10)
            for link in orbit["orbit_links"]:
                self.assertIn(link["cut_descendant_id"], cut_ids)
                self.assertIn(link["contact_child_id"], contact_ids)
                self.assertTrue(set(link["bubble_child_ids"]) <= bubble_ids)

    def test_duplicate_parent_edge_is_rejected(self):
        graph = deepcopy(self.graphs[0])
        graph["internal_edges"][1]["edge_id"] = graph["internal_edges"][0]["edge_id"]
        with self.assertRaises(sd.ParentGraphError):
            sd.validate_parent(graph)

    def test_missing_cut_edge_and_invalid_bubble_pair_are_rejected(self):
        graph = self.graphs[0]
        with self.assertRaises(sd.CutError):
            sd.build_cut_descendant(graph, "direct", "missing", "I")
        edge = graph["internal_edges"][0]
        cut = sd.build_cut_descendant(graph, "direct", edge["edge_id"], edge["source"])
        with self.assertRaises(sd.BubbleError):
            sd.build_bubble_child(graph, cut, cut["unique_cycle_edge_ids"][:1])

    def test_nonanomalous_cancellation_is_explicitly_Dalgebra_blocked(self):
        for orbit in self.payload["orbits"]:
            gate = orbit["cancellation_gate"]
            self.assertEqual(gate["status"], sd.DALGEBRA_BLOCK)
            self.assertIsNone(gate["ordinary_nonanomalous_numerator_terms"])
            self.assertIsNone(gate["bubble_contact_parent_pairing"])
            self.assertIsNone(gate["anomaly_coefficient"])
        for gate in self.payload["global_cancellation_gate"].values():
            self.assertIsNone(gate["value"])

    def test_input_firewall(self):
        self.assertFalse(self.payload["external_result_used_as_calculation_input"])
        self.assertFalse(self.payload["input_firewall"]["external_target_or_review_read"])
        source = (ROOT / "scripts/step6_sd_orbit.py").read_text(encoding="utf-8")
        self.assertNotIn("tasks/reviews", source)
        self.assertNotIn("references/external-targets", source)


if __name__ == "__main__":
    unittest.main()
