from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/one-loop-filtered-covariant-quotient.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-filtered-covariant-quotient-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-filtered-covariant-quotient.md"


class Step5OneLoopFilteredCovariantQuotientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.generated_bytes = GENERATED.read_bytes()
        cls.payload = json.loads(cls.generated_bytes)
        cls.audit = json.loads(AUDIT_JSON.read_bytes())

    def test_scope_is_physical_4d_background_covariant_only(self) -> None:
        scope = self.payload["scope"]
        self.assertEqual(scope["frame"], "FIXED_VECTOR_FRAME")
        self.assertEqual(scope["symmetry"], "BACKGROUND_COVARIANT")
        self.assertEqual(scope["lorentz_space"], "PHYSICAL_4D_SPIN_ALGEBRA")
        self.assertEqual(
            scope["DRED_traceless_tau_sector"],
            "EXCLUDED_NOT_ZERO_IN_FULL_DRED",
        )
        self.assertEqual(scope["quantum_BV_source_complex"], "OUT_OF_SCOPE")

    def test_N0_is_closed_and_N1_true_parent_incidence_is_fail_closed(self) -> None:
        filtration = self.payload["filtration_elimination_blocks"]
        self.assertEqual(
            filtration["N0"]["identity_matrix"],
            {"rows": 40, "columns": 40, "rank": 40},
        )
        self.assertEqual(
            filtration["N0"]["local_source_IBP_matrix"],
            {"rows": 320, "columns": 320, "rank": 320},
        )
        self.assertEqual(
            filtration["N1_terminal"]["target_plus_EOM_matrix"],
            {"rows": 40, "columns": 40, "rank": 40},
        )
        event = filtration["N1_event_carrier"]
        self.assertEqual(event["coordinates"], 4866)
        self.assertFalse(event["are_independent_parent_generators"])
        self.assertEqual(
            event["forbidden_tautological_matrix"],
            "[identity_(4866)|-transpose(C_(1->2))]",
        )
        required = filtration["required_true_N1_incidence"]
        self.assertEqual(required["C1_shape"], "4866x20")
        self.assertEqual(required["status"], "NOT_CONSTRUCTED")
        naive = filtration["naive_parent_label_incidence"]
        self.assertFalse(naive["qM_factors_through_A0"])
        self.assertGreater(naive["nonconstant_fiber_count"], 0)
        self.assertEqual(
            naive["explicit_witnesses"][0],
            {
                "parent": {"skeleton": "W0_T1_N1_B1_D2", "spin_copy": 0},
                "first_column": 0,
                "first_value": "-2",
                "second_column": 6,
                "second_value": "0",
                "fiber_size": 20,
            },
        )

    def test_N2_relation_matrix_has_one_physical_class(self) -> None:
        pbw = self.payload["N2_candidate_PBW_quotient"]
        matrix = pbw["relation_matrix"]
        self.assertEqual(
            (matrix["rows"], matrix["columns"], matrix["rank"]),
            (126, 127, 126),
        )
        self.assertEqual(pbw["quotient_dimension"], 1)
        self.assertEqual(
            pbw["descent_support"],
            [
                {"row": 0, "value": "1"},
                {"row": 2, "value": "1"},
                {"row": 13, "value": "-2"},
                {"row": 19, "value": "-2"},
            ],
        )
        total = self.payload["filtration_elimination_blocks"]["filtered_total"]
        self.assertEqual(total["quotient_dimension"], "NOT_COMPUTED")
        self.assertEqual(total["ker_ell2"], "NOT_COMPUTED")

    def test_every_indexed_commutator_child_descends(self) -> None:
        descent = self.payload["indexed_child_intertwiner"]
        self.assertTrue(descent["all_columns_have_a_defined_descent"])
        self.assertEqual(descent["indexed_event_columns"], 4866)
        self.assertEqual(descent["nonzero_descended_columns"], 190)
        self.assertEqual(len(descent["sparse_descended_vector_sha256"]), 64)

    def test_spin_intertwiner_lifts_the_multiplicity_normal_form(self) -> None:
        spin = self.payload["spin_intertwiner"]
        self.assertTrue(spin["left_S3_acts_as_plus_one"])
        self.assertTrue(spin["right_transposition_acts_as_minus_one"])
        self.assertEqual(spin["full_target_projector_rank"], 4)
        self.assertEqual(spin["full_component_intertwiner_rank"], 4)

    def test_local_source_codomain_boundary_and_ell2_square(self) -> None:
        quadratic = self.payload["N2_candidate_quadratic_jet_codomain"]
        self.assertEqual(
            (
                quadratic["codomain_boundary_matrix"]["rows"],
                quadratic["codomain_boundary_matrix"]["columns"],
                quadratic["codomain_boundary_matrix"]["rank"],
            ),
            (4, 6, 4),
        )
        self.assertTrue(quadratic["local_source_momentum_is_retained"])
        self.assertTrue(quadratic["p_J_is_not_zero"])
        self.assertTrue(quadratic["commutative_square"]["passes"])
        self.assertEqual(quadratic["physical_ell2"], [["1"], ["-1"]])
        self.assertEqual(quadratic["physical_ell2_kernel_dimension"], 0)

    def test_combined_color_species_plus_exchange_preserves_actual_K(self) -> None:
        color = self.payload["color_species_exchange"]
        witness = color["SU2_exact_witness"]
        self.assertEqual(witness["K_rank"], 6)
        self.assertEqual(witness["ell2_rank"], 6)
        self.assertTrue(witness["tau_K_equals_K"])
        self.assertTrue(witness["graded_exchange_squared_is_identity"])
        self.assertTrue(witness["plus_projector_idempotent"])
        self.assertTrue(witness["P_plus_ell2_equals_ell2"])
        self.assertTrue(color["actual_K_line_survives_combined_plus_exchange"])

    def test_verdict_is_fail_closed_outside_physical_local_quotient(self) -> None:
        verdicts = self.payload["verdicts"]
        self.assertEqual(verdicts["N2_candidate_block_ker_ell2"], "ZERO")
        self.assertEqual(
            verdicts["physical_4d_background_covariant_ker_ell2"],
            "FAIL_CLOSED_MISSING_TRUE_N1_PARENT_INCIDENCE",
        )
        self.assertEqual(verdicts["full_DRED_ker_ell2"], "NOT_CLAIMED")
        self.assertEqual(verdicts["full_quantum_BV_cohomology"], "NOT_CLAIMED")
        self.assertEqual(verdicts["anomaly_coefficient"], "NOT_COMPUTED")

    def test_artifact_hash_and_markdown(self) -> None:
        self.assertEqual(self.audit["failed"], [])
        self.assertEqual(self.audit["passed"], self.audit["total"])
        self.assertEqual(
            self.audit["generated_sha256"],
            hashlib.sha256(self.generated_bytes).hexdigest(),
        )
        markdown = AUDIT_MD.read_text(encoding="utf-8")
        self.assertIn("q_T\\ell_2^{(N=2),{\\rm raw}}", markdown)
        self.assertIn("P_+L_K=L_K\\ne0", markdown)
        self.assertIn("FAIL\\_CLOSED\\_MISSING\\_C1", markdown)
        self.assertIn("full DRED traceless-", markdown)


if __name__ == "__main__":
    unittest.main()
