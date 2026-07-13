from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
import unittest

from scripts import step6_two_loop_wick as wick


ROOT = Path(__file__).resolve().parents[1]


class Step6TwoLoopWickJoinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload, cls.joins = wick.build_payload()
        cls.checks = wick.exact_checks(cls.payload, cls.joins)
        cls.by_key = {
            (join.graph["graph_id"], join.orientation): join
            for join in cls.joins
        }

    def test_all_exact_checks_pass(self) -> None:
        self.assertTrue(
            all(self.checks.values()),
            [name for name, passed in self.checks.items() if not passed],
        )

    def test_scope_contains_only_two_literal_k4_minus_edge_parents(self) -> None:
        self.assertEqual(
            set(self.payload["supported_valence_families"]),
            {"I3__S3^3", "I2__S3^2__S4^1"},
        )
        self.assertEqual(len(self.joins), 6)
        self.assertEqual(
            {join.graph["graph_id"] for join in self.joins},
            {
                "G6_DIRECT_K4ME_I3_S3CUBED",
                "G6_DIRECT_K4ME_I2_S3SQ_S4",
                "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4",
            },
        )
        for join in self.joins:
            self.assertEqual(join.graph["topology"], "K4_MINUS_ONE_EDGE")
            self.assertEqual(join.graph["identities"]["I"], 5)
            self.assertEqual(join.graph["identities"]["L"], 2)

    def test_exact_background_quantum_assignment_counts(self) -> None:
        expected = {
            "G6_DIRECT_K4ME_I3_S3CUBED": {"I": 10, "A": 12, "B": 12, "C": 4},
            "G6_DIRECT_K4ME_I2_S3SQ_S4": {"I": 2, "A": 12, "B": 4, "C": 24},
            "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": {"I": 2, "A": 4, "B": 4, "C": 72},
        }
        for (graph_id, _), join in self.by_key.items():
            self.assertEqual(
                {vertex: len(rows) for vertex, rows in join.assignment_catalog.items()},
                expected[graph_id],
            )
            for rows in join.assignment_catalog.values():
                for assignment in rows:
                    self.assertEqual(
                        assignment["t"], assignment["b"] + assignment["q"]
                    )
                    self.assertEqual(
                        assignment["external_projection"],
                        wick.EXTERNAL_PROJECTION_STATUS,
                    )

    def test_double_background_s4_enumerates_both_labeled_bijections(self) -> None:
        join = self.by_key[
            ("G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4", "direct")
        ]
        groups: dict[tuple[str, tuple[str, ...]], set[tuple[str, ...]]] = defaultdict(set)
        for assignment in join.assignment_catalog["C"]:
            grammar_subset = tuple(
                port["port_id"] for port in assignment["background_grammar_ports"]
            )
            bijection = assignment["background_projection_join"]
            self.assertEqual(bijection["status"], wick.EXTERNAL_PROJECTION_STATUS)
            self.assertIsNone(bijection["value"])
            target_order = tuple(
                row["topology_background_port_id"]
                for row in bijection["labeled_background_port_bijection"]
            )
            groups[(assignment["source_term_id"], grammar_subset)].add(target_order)
        self.assertEqual(len(groups), 36)
        self.assertTrue(
            all(target_orders == {("C.b0", "C.b1"), ("C.b1", "C.b0")}
                for target_orders in groups.values())
        )
    def test_exact_local_and_global_wick_counts(self) -> None:
        expected_local = {
            "G6_DIRECT_K4ME_I3_S3CUBED": {"I": 60, "A": 24, "B": 24, "C": 24},
            "G6_DIRECT_K4ME_I2_S3SQ_S4": {"I": 4, "A": 24, "B": 24, "C": 144},
            "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": {"I": 4, "A": 24, "B": 24, "C": 144},
        }
        expected_global = {
            "G6_DIRECT_K4ME_I3_S3CUBED": 829_440,
            "G6_DIRECT_K4ME_I2_S3SQ_S4": 331_776,
            "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": 331_776,
        }
        for (graph_id, _), join in self.by_key.items():
            self.assertEqual(
                {vertex: len(rows) for vertex, rows in join.local_options.items()},
                expected_local[graph_id],
            )
            self.assertEqual(join.cardinality, expected_global[graph_id])
        self.assertEqual(self.payload["exact_total_labeled_pairings"], 2_985_984)

    def test_serialized_ir_is_factorized_and_does_not_materialize_global_rows(self) -> None:
        self.assertEqual(len(self.payload["term_dictionary"]), 22)
        self.assertEqual(
            len(self.payload["decorated_graph_background_quantum_assignment_catalog"]),
            3,
        )
        for row in self.payload["joins"]:
            self.assertNotIn("local_wick_option_catalog", row)
            local_product = 1
            for factor in row["local_wick_factor_catalog"].values():
                self.assertEqual(
                    factor["local_option_count"],
                    factor["assignment_count"] * factor["permutation_count"],
                )
                local_product *= factor["local_option_count"]
            self.assertEqual(
                local_product,
                row["global_pairing_enumeration"]["cardinality"],
            )
            self.assertEqual(
                set(row["samples_only_not_full_materialization"]),
                {"first", "middle", "last"},
            )

    def test_rank_unrank_and_edge_materialization(self) -> None:
        for join in self.joins:
            for rank in (0, 1, join.cardinality // 2, join.cardinality - 1):
                options = join.unrank(rank)
                self.assertEqual(join.rank(options), rank)
                pairing = join.materialize(rank)
                self.assertEqual(pairing["pairing_id"], join.pairing_id(rank))
                self.assertEqual(len(pairing["edges"]), 5)
                grammar_ports = [
                    endpoint["grammar_port_occurrence_id"]
                    for edge in pairing["edges"]
                    for endpoint in (edge["source"], edge["target"])
                ]
                self.assertEqual(len(grammar_ports), 10)
                self.assertEqual(len(set(grammar_ports)), 10)
                self.assertTrue(
                    all(
                        edge["propagator"] is None
                        and edge["propagator_status"] == wick.PROPAGATOR_STATUS
                        for edge in pairing["edges"]
                    )
                )

    def test_term_metadata_and_asts_are_preserved(self) -> None:
        for join in self.joins:
            for term_id, term in join.term_dictionary.items():
                self.assertEqual(term["term_id"], term_id)
                self.assertIn(term["grassmann_parity"], (0, 1))
                self.assertTrue(term["measure"])
                self.assertTrue(term["chirality"]["class"])
                self.assertEqual(
                    wick.digest(term["color_ast"]), term["color_ast_sha256"]
                )
                self.assertEqual(
                    wick.digest(term["expression_ast"]),
                    term["expression_ast_sha256"],
                )

    def test_raw_sector_factor_and_decorated_occurrence_orbit_are_separate(self) -> None:
        for row in self.payload["joins"]:
            self.assertEqual(
                sum(item["labeled_pairing_count"] for item in row["sector_histogram"]),
                row["global_pairing_enumeration"]["cardinality"],
            )
            for item in row["sector_histogram"]:
                rational = item["exponential_expansion_factor"]["rational"]
                denominator = 1
                for multiplicity in item["family_sector_multiplicities"].values():
                    denominator *= wick.factorial(multiplicity)
                self.assertEqual(
                    (rational["numerator"], rational["denominator"]),
                    (-1, denominator),
                )
                self.assertEqual(
                    item["exponential_expansion_factor"]["hbar_power"], -3
                )
            for sample in row["samples_only_not_full_materialization"].values():
                factors = sample["coefficient_factorization"]
                orbit = factors["decorated_occurrence_orbit_factor"]
                self.assertEqual(
                    factors["automorphism_denominator"],
                    orbit["background_source_labeled_automorphism_order"],
                )
                self.assertEqual(
                    (
                        orbit["combined_rational"]["numerator"],
                        orbit["combined_rational"]["denominator"],
                    ),
                    (-1, factors["automorphism_denominator"]),
                )
                self.assertEqual(
                    factors["automorphism_policy"],
                    "DIVIDE_ONCE_AFTER_OCCURRENCE_TO_DECORATED_ROLE_EMBEDDINGS",
                )
                self.assertIsNone(factors["assembled_numeric_coefficient"])

    def test_direct_is_physical_and_reflected_is_routing_only(self) -> None:
        self.assertEqual(
            self.payload[
                "exact_total_physical_representative_pairings_before_automorphism_weight"
            ],
            1_492_992,
        )
        for row in self.payload["joins"]:
            self.assertEqual(
                row["orientation_role"],
                "PHYSICAL_SUM_REPRESENTATIVE"
                if row["orientation"] == "direct"
                else "ROUTING_COVARIANCE_CHECK_ONLY_NOT_ADDED_TO_PHYSICAL_SUM",
            )

    def test_family_sector_factorials_distinguish_s3_squared_s4(self) -> None:
        i3_all_plus = wick.expansion_factor({"S3_PLUS": 3})
        self.assertEqual(
            (i3_all_plus["rational"]["numerator"], i3_all_plus["rational"]["denominator"]),
            (-1, 6),
        )
        i2_all_plus = wick.expansion_factor({"S3_PLUS": 2, "S4_PLUS": 1})
        self.assertEqual(
            (i2_all_plus["rational"]["numerator"], i2_all_plus["rational"]["denominator"]),
            (-1, 2),
        )
        i2_split = wick.expansion_factor(
            {"S3_PLUS": 1, "S3_MINUS": 1, "S4_MINUS": 1}
        )
        self.assertEqual(
            (i2_split["rational"]["numerator"], i2_split["rational"]["denominator"]),
            (-1, 1),
        )

    def test_source_ast_has_no_duplicate_literal_dictionary_keys(self) -> None:
        self.assertEqual(
            wick.duplicate_literal_dict_keys(ROOT / "scripts/step6_two_loop_wick.py"),
            [],
        )

    def test_symbolic_coupling_grade_is_exactly_g4(self) -> None:
        for row in self.payload["joins"]:
            grade = row["coupling_grade"]
            self.assertEqual(grade["propagator_count"], 5)
            self.assertEqual(grade["action_vertex_count"], 3)
            self.assertEqual(grade["exact_chain"], [
                "(g^2)^5*h^3",
                "(g^2)^5*(g^2)^(-3)",
                "(g^2)^2",
                "g^4",
            ])
            self.assertEqual(grade["derived_g2_power"], 2)
            self.assertEqual(grade["derived_g_power"], 4)
            self.assertTrue(grade["kept_separate_from_numeric_action_and_wick_factors"])

    def test_no_chirality_zero_and_all_downstream_stages_fail_closed(self) -> None:
        self.assertEqual(
            self.payload["global_chirality_policy"],
            {
                "status": wick.CHIRALITY_ZERO_STATUS,
                "discarded_assignment_count": 0,
            },
        )
        for row in self.payload["joins"]:
            self.assertEqual(row["chirality_policy"]["discarded_assignment_count"], 0)
            self.assertEqual(
                row["external_projection"],
                {"status": wick.EXTERNAL_PROJECTION_STATUS, "value": None},
            )
            for stage in row["downstream_fail_closed"].values():
                self.assertIsNone(stage["value"])
                self.assertTrue(stage["status"].startswith("BLOCKED_"))

    def test_generated_outputs_match_runtime(self) -> None:
        payload = json.loads(
            (ROOT / "generated/step6/two-loop-wick/typed-wick-join.json").read_text()
        )
        audit = json.loads(
            (ROOT / "audits/step6-two-loop-wick-verification.json").read_text()
        )
        self.assertEqual(payload["payload_sha256"], self.payload["payload_sha256"])
        self.assertEqual(payload["status"], wick.STATUS)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["failed"], 0)
        self.assertEqual(audit["passed"], len(audit["checks"]))


if __name__ == "__main__":
    unittest.main()
