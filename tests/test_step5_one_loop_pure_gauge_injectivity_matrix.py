from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/step5_one_loop_pure_gauge_injectivity_matrix.py"
SPEC = importlib.util.spec_from_file_location("step5_injectivity_matrix", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PureGaugeInjectivityMatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.verification = MODULE.build_verification(cls.payload)

    def test_exact_census(self) -> None:
        rows = MODULE.enumerate_skeletons()
        self.assertEqual(len(rows), 18)
        self.assertEqual(
            {
                degree: sum(row["field_strength_degree"] == degree for row in rows)
                for degree in range(4)
            },
            {0: 5, 1: 7, 2: 5, 3: 1},
        )

    def test_formal_grading_is_not_physical_R(self) -> None:
        self.assertEqual(
            self.payload["target"]["physical_Project_U1R_binding"],
            "OPEN_NOT_USED",
        )
        self.assertEqual(
            self.payload["nonmatrix_gate"]["id"], "PROJECT_U1R_BINDING"
        )

    def test_rref_is_exact_over_Q(self) -> None:
        matrix = [
            [Fraction(1), Fraction(2), Fraction(3)],
            [Fraction(2), Fraction(4), Fraction(6)],
            [Fraction(0), Fraction(1), Fraction(1)],
        ]
        reduced, pivots = MODULE.rref(matrix)
        self.assertEqual(pivots, [0, 1])
        self.assertEqual(
            reduced,
            [
                [Fraction(1), Fraction(0), Fraction(1)],
                [Fraction(0), Fraction(1), Fraction(1)],
                [Fraction(0), Fraction(0), Fraction(0)],
            ],
        )

    def test_N0_identity_and_source_ibp_blocks_are_full_rank(self) -> None:
        n0 = self.payload["N0"]
        self.assertEqual(n0["target_component_count"], 40)
        self.assertEqual(n0["identity_relation_matrix"]["rank"], 40)
        self.assertEqual(n0["identity_relation_matrix"]["quotient_dimension"], 0)
        self.assertEqual(n0["source_ibp_relation_matrix"]["rank"], 320)
        self.assertEqual(n0["source_ibp_relation_matrix"]["quotient_dimension"], 0)

    def test_single_field_mixed_normal_order(self) -> None:
        chiral, _ = MODULE.normal_order_single_field("W", ("B", "N"))
        antichiral, _ = MODULE.normal_order_single_field("T", ("N", "B"))
        self.assertEqual(chiral, {("D",): Fraction(-2)})
        self.assertEqual(antichiral, {("D",): Fraction(-2)})
        self.assertEqual(MODULE.normal_order_single_field("W", ("B",))[0], {})
        self.assertEqual(MODULE.normal_order_single_field("T", ("N",))[0], {})

    def test_every_N1_curvature_child_has_unique_explicit_tag(self) -> None:
        normal = self.payload["N1"]["normal_order"]
        events = normal["curvature_child_events"]
        self.assertGreater(len(events), 0)
        self.assertEqual(
            {event["event_id"] for event in events}, set(range(len(events)))
        )
        self.assertTrue(
            all(event["child_field_strength_degree_minimum"] >= 2 for event in events)
        )
        self.assertTrue(
            normal["all_commutator_children_content_bound_to_five_N2_sectors"]
        )
        self.assertTrue(
            all(
                event["relation"].startswith("[N_a,D")
                or event["relation"].startswith("[B_dota,D")
                for event in events
            )
        )

    def test_N1_target_EOM_matrix_kills_all_twenty_components(self) -> None:
        quotient = self.payload["N1"]["target_EOM_quotient"]
        self.assertEqual(quotient["target_component_count"], 20)
        matrix = quotient["target_plus_EOM_relation_matrix"]
        self.assertEqual((matrix["rows"], matrix["columns"], matrix["rank"]), (40, 40, 40))
        self.assertEqual(matrix["quotient_dimension"], 0)
        self.assertTrue(
            any(
                witness["identity"]
                == "D_a^dota T_dota=-(1/2) nabla_a(bar_nabla^dota T_dota)"
                for witness in quotient["witnesses"]
            )
        )
        vector_children = quotient["vector_pairing_commutator_children"]
        self.assertEqual(len(vector_children), 2)
        self.assertTrue(
            all(child["field_strength_degree_minimum"] >= 2 for child in vector_children)
        )

    def test_indexed_ND_BD_child_matrix_is_exact_and_surjective(self) -> None:
        indexed = self.payload["N1"]["indexed_ND_BD_child_map"]
        self.assertEqual(
            (
                indexed["input_word_count"],
                indexed["event_count"],
                indexed["branch_count"],
                indexed["ordered_placement_count"],
            ),
            (1626, 21600, 53412, 83),
        )
        matrix = indexed["multiplicity_matrix"]
        self.assertEqual(
            (matrix["rows"], matrix["columns"], matrix["rank"], matrix["kernel_dimension"]),
            (126, 4864, 126, 4738),
        )
        self.assertEqual(
            (
                indexed["full_component_rows"],
                indexed["full_component_columns"],
                indexed["full_component_rank_by_exact_spin4_intertwining"],
                indexed["full_component_kernel_dimension"],
            ),
            (504, 19456, 504, 18952),
        )
        self.assertTrue(all(indexed["epsilon_invariance_checks"].values()))
        self.assertTrue(indexed["all_raw_maps_spin4_intertwiners"])
        self.assertTrue(indexed["all_full_ranks_four_times_highest_ranks"])
        event_ledger = indexed["event_table_ledger"]
        self.assertEqual(event_ledger["count"], 21600)
        self.assertLessEqual(len(event_ledger["witnesses"]), 16)
        self.assertEqual(
            [event["event_id"] for event in event_ledger["witnesses"]],
            event_ledger["witness_indices"],
        )
        for key in ("matrix_sparse", "rref_sparse"):
            sparse = matrix[key]
            self.assertEqual(len(sparse["canonical_COO_sha256"]), 64)
            self.assertLessEqual(len(sparse["witness_rows"]), 8)
            self.assertNotIn("entries", sparse)

    def test_indexed_DD_pairing_has_local_source_kernel(self) -> None:
        dd = self.payload["N1"]["indexed_DD_pairing_child_map"]
        self.assertEqual(dd["Euclidean_curvature_normalization"], "rho_E=1")
        self.assertEqual(len(dd["branches"]), 8)
        self.assertEqual(dd["zero_target_BT_child_branches"], 4)
        self.assertEqual(dd["highest_weight_matrix"]["matrix"], [["0", "1"], ["0", "-1"]])
        self.assertEqual(
            (
                dd["highest_weight_matrix"]["rows"],
                dd["highest_weight_matrix"]["columns"],
                dd["highest_weight_rank"],
                dd["highest_weight_source_kernel_dimension"],
            ),
            (2, 2, 1, 1),
        )
        self.assertEqual(
            (
                dd["full_component_matrix"]["rows"],
                dd["full_component_matrix"]["columns"],
                dd["full_component_rank"],
                dd["full_component_source_kernel_dimension"],
            ),
            (8, 8, 4, 4),
        )
        self.assertIn("not the kernel", dd["kernel_interpretation"])

    def test_complete_indexed_child_matrix_closes_only_the_N1_child_block(self) -> None:
        complete = self.payload["N1"]["complete_indexed_child_to_N2_map"]
        self.assertEqual(
            (
                complete["target_multiplicity_rows"],
                complete["source_multiplicity_columns"],
                complete["multiplicity_rank"],
                complete["multiplicity_kernel_dimension"],
            ),
            (126, 4866, 126, 4740),
        )
        self.assertEqual(
            (
                complete["full_component_rows"],
                complete["full_component_columns"],
                complete["full_component_rank"],
                complete["full_component_kernel_dimension"],
            ),
            (504, 19464, 504, 18960),
        )
        self.assertTrue(
            complete["exact_rank_proof"]["ND_BD_submatrix_is_surjective"]
        )
        self.assertTrue(all(complete["coverage"][key] for key in (
            "ND_and_BD_normal_order_children",
            "DD_pairing_children",
            "all_nonzero_DD_rows_embedded_in_shared_N2_placement_basis",
        )))

    def test_filtered_total_relation_matrix_fails_closed_on_two_incidence_maps(self) -> None:
        gate = self.payload["filtered_quotient_gate"]
        self.assertEqual(
            (
                gate["filtered_target_blocks"]["N0_target_components"],
                gate["filtered_target_blocks"]["N1_target_components"],
                gate["filtered_target_blocks"][
                    "N2_indexed_target_multiplicity_rows"
                ],
                gate["filtered_target_blocks"][
                    "N2_existing_canonical_placement_coordinates"
                ],
                gate["filtered_target_blocks"]["N3_target_components"],
            ),
            (40, 20, 126, 44, 0),
        )
        self.assertEqual(
            {entry["id"] for entry in gate["missing_incidence_matrices"]},
            {
                "C_N1_TARGET_TO_INDEXED_SOURCE",
                "R_N2_INDEXED_EOM_IBP",
            },
        )
        c1, r2 = gate["missing_incidence_matrices"]
        self.assertEqual(c1["shape"], "4866x20")
        self.assertEqual(len(c1["domain_basis"]), 20)
        self.assertEqual(
            [
                (
                    row["skeleton"],
                    row["ordered_word_records"],
                    row["multiplicity_columns"],
                )
                for row in c1["codomain_sector_decomposition"]
            ],
            [
                ("W0_T1_N0_B0_D3", 1, 2),
                ("W0_T1_N1_B1_D2", 20, 40),
                ("W0_T1_N2_B2_D1", 116, 232),
                ("W0_T1_N3_B3_D0", 684, 1368),
                ("W1_T0_N2_B0_D2", 20, 80),
                ("W1_T0_N3_B1_D1", 114, 456),
                ("W1_T0_N4_B2_D0", 672, 2688),
            ],
        )
        self.assertEqual(r2["column_basis_ledger"]["count"], 126)
        self.assertEqual(len(r2["existing_canonical_basis"]), 44)
        feasibility = gate["feasibility_from_current_event_ledger"]
        self.assertEqual(
            feasibility["verdict"], "NOT_FEASIBLE_FROM_EVENT_LEDGER_ALONE"
        )
        self.assertFalse(
            feasibility["new_local_spinor_algebra_identity_required"]
        )
        self.assertEqual(
            {entry["id"] for entry in feasibility["minimal_Project_type_data"]},
            {
                "STEP5_SOURCE_BRST_COMPLEX",
                "STEP5_ELL2_CODOMAIN_BOUNDARIES",
            },
        )
        self.assertFalse(gate["total_relation_matrix"]["constructed"])
        self.assertIsNone(gate["total_relation_matrix"]["rank"])
        self.assertFalse(gate["induced_quadratic_jet"]["constructed"])
        self.assertFalse(
            gate["induced_quadratic_jet"]["ker_ell2_zero_certified"]
        )
        source = gate["source_local_derivative_rows"]
        self.assertEqual(
            source["nabla_rows"],
            [
                "e_(J,J)-e_(F1,J)+e_(F2,J)=0",
                "e_(J,F1)-e_(F1,F1)+e_(F2,F1)=0",
                "e_(J,F2)-e_(F1,F2)+e_(F2,F2)=0",
            ],
        )
        self.assertEqual(len(source["D_rows"]), 3)
        self.assertEqual(len(source["exact_incidence_rows"]), 6)
        self.assertEqual(
            source["antichiral_EOM_row_on_C_on_W_C_split_S_DJ"],
            ["0", "1", "0"],
        )
        self.assertEqual(
            source["representative_equations"],
            ["C_split=0", "S_DJ=-C_on_W"],
        )
        self.assertEqual(source["external_source_momentum"], "retained; p=p1+p2")

    def test_color_quotient_cannot_create_a_kernel(self) -> None:
        color = self.payload["color_quotient_module_certificate"]
        self.assertEqual(color["status"], "CLOSED_BY_SPLIT_MONOMORPHISM")
        self.assertEqual(color["composition"], "pi_1 o iota_M=id_M")
        self.assertEqual(color["kernel"], "ker(iota_M)=0")
        self.assertIn("arbitrary quotient module", color["module"])

    def test_WW_spin_projector_is_idempotent_rank_four(self) -> None:
        projector = self.payload["N2"]["WW_N3"]["spin_projector"]
        self.assertTrue(projector["projector_idempotent"])
        self.assertEqual(projector["target_multiplicity"], 4)
        self.assertEqual(projector["j_3_over_2_projector"]["rank"], 4)

    def test_WW_all_placements_have_EOM_carrier(self) -> None:
        ww = self.payload["N2"]["WW_N3"]
        self.assertEqual(len(ww["graded_leibniz_expansion"]), 8)
        self.assertEqual(len(ww["placement_witnesses"]), 8)
        self.assertTrue(all(row["eom_carrier"] in {"W1", "W2"} for row in ww["placement_witnesses"]))
        self.assertEqual(ww["placement_plus_EOM_relation_matrix"]["rank"], 64)
        self.assertEqual(ww["target_quotient_dimension"], 0)

    def test_mixed_N2B_reduction_and_spin_projection(self) -> None:
        mixed = self.payload["N2"]["W_T_N2_B"]
        self.assertEqual(len(mixed["graded_leibniz_expansion"]), 8)
        matrix = mixed["normal_reduction_map"]["matrix"]
        self.assertEqual(matrix[0][4], "-1")
        self.assertEqual(matrix[1][5], "2")
        self.assertEqual(matrix[2][6], "-2")
        self.assertEqual(matrix[3][7], "-4")
        self.assertEqual(
            mixed["target_projection_of_reduced_C_vector"], [["0"], ["0"]]
        )
        self.assertEqual(mixed["projected_target_quotient_dimension"], 0)

    def test_mixed_ND_children_cancel_only_after_full_leibniz_sum(self) -> None:
        mixed = self.payload["N2"]["W_T_N_D"]
        self.assertEqual(len(mixed["graded_leibniz_expansion"]), 4)
        self.assertEqual(
            mixed["sum_of_all_leibniz_branches"][
                "output_vector_C_on_W_C_split_H"
            ],
            [["1"], ["1"], ["0"]],
        )
        self.assertEqual(
            [child["coefficient"] for child in mixed["commutator_children"]],
            ["-2", "2"],
        )

    def test_local_source_EOM_identifies_source_derivative_with_physical_class(self) -> None:
        mixed = self.payload["N2"]["W_T_N_D"]
        self.assertEqual(mixed["constant_source_ibp"]["quotient_dimension"], 1)
        self.assertEqual(mixed["source_extended_ibp"]["quotient_dimension"], 2)
        self.assertEqual(
            mixed["constant_source_EOM_completed_quotient"][
                "quotient_dimension"
            ],
            0,
        )
        self.assertEqual(
            mixed["source_extended_EOM_completed_quotient"][
                "quotient_dimension"
            ],
            1,
        )
        self.assertEqual(
            mixed["source_extended_equation"], "C_on_W+C_split+S_DJ=0"
        )
        self.assertEqual(
            mixed["source_extended_representative_equations"],
            ["C_split=0", "S_DJ=-C_on_W"],
        )
        self.assertTrue(mixed["source_derivative_is_not_an_independent_class"])
        self.assertTrue(
            mixed["source_ibp_incidence"][
                "constant_source_is_not_the_source_extended_quotient"
            ]
        )

    def test_complete_tensor_valued_quadratic_jet_is_injective(self) -> None:
        jet = self.payload["N2"]["W_T_N_D"]["complete_ordered_quadratic_jet"]
        self.assertEqual(jet["matrix"], [["1"], ["-1"]])
        self.assertEqual(jet["rank"], 1)
        self.assertEqual(jet["kernel_dimension"], 0)
        self.assertIn("free nonzero source-color tensor", self.payload["N2"]["W_T_N_D"]["symbolic_tensor_module"])

    def test_all_five_N2_sector_placements_are_enumerated(self) -> None:
        n2 = self.payload["N2"]
        self.assertEqual(len(n2["WW_N3"]["graded_leibniz_expansion"]), 8)
        self.assertEqual(len(n2["W_T_N2_B"]["graded_leibniz_expansion"]), 8)
        self.assertEqual(len(n2["W_T_N_D"]["graded_leibniz_expansion"]), 4)
        self.assertEqual(n2["T2_N_B2"]["placement_count"], 8)
        self.assertEqual(n2["T2_B_D"]["placement_count"], 4)

    def test_N3_and_N_ge_4_are_exactly_excluded(self) -> None:
        higher = self.payload["higher_degree"]
        self.assertEqual(higher["N3"]["target_spin_multiplicity"], 0)
        self.assertTrue(higher["N3"]["target_projection_zero"])
        self.assertEqual(higher["N_ge_4"]["minimum_dimension_twice"], 12)
        self.assertTrue(higher["N_ge_4"]["excluded"])

    def test_global_injectivity_fails_closed_on_named_matrices(self) -> None:
        self.assertEqual(
            {entry["id"] for entry in self.payload["open_relation_matrices"]},
            {
                "M_FILTERED_N0_N1_N2_N3_TOTAL",
                "M_SOURCE_BRST_COMPLETE",
                "M_DRED_EVANESCENT_JETS",
            },
        )
        verdict = self.payload["final_verdict"]
        self.assertFalse(verdict["ker_ell2_zero_certified"])
        self.assertFalse(verdict["rank_one_claim"])
        self.assertFalse(verdict["accepted_anomaly_coefficient"])

    def test_generated_artifacts_match_builders(self) -> None:
        on_disk_payload = json.loads(MODULE.OUT.read_text())
        on_disk_verification = json.loads(MODULE.VERIFY.read_text())
        self.assertEqual(on_disk_payload, self.payload)
        self.assertEqual(on_disk_verification, self.verification)
        self.assertTrue(on_disk_verification["all_passed"])
        self.assertEqual(
            (on_disk_verification["passed"], on_disk_verification["total"]),
            (56, 56),
        )
        self.assertEqual(
            MODULE.AUDIT_MD.read_text(),
            MODULE.render_audit(self.payload, self.verification),
        )


if __name__ == "__main__":
    unittest.main()
