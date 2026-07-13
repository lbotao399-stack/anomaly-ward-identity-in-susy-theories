from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ww_contact_replay.py"
OUTPUT = ROOT / "generated/step5/contact-replay/ww-contact-replay.json"
AUDIT_JSON = ROOT / "audits/step5-ww-contact-replay-verification.json"
AUDIT_MD = ROOT / "audits/step5-ww-contact-replay.md"


class Step5WWContactReplayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        cls.payload = json.loads(OUTPUT.read_text())

    def test_Qphys_contains_Hessian_cut_and_counterterm_families(self) -> None:
        family = self.payload["complete_Q_contact"]
        self.assertEqual(
            set(family["Q_Hess"]["terms"]),
            {
                "minus_I0_G0_H2_G0",
                "minus_I1_p1_G0_H1_p2_G0",
                "minus_I1_p2_G0_H1_p1_G0",
                "plus_I2_G0",
            },
        )
        self.assertEqual(
            family["Q_phys"]["definition"],
            "Q_phys^(2)=Q_Hess^(2)+Q_cut^(2)+CT2",
        )
        self.assertEqual(
            family["Q_phys"]["role"],
            "REGROUPED_CONTACT_CUT_FAMILY_NOT_ADDED_TO_BARE_TRIANGLE",
        )
        self.assertEqual(
            family["Q_phys"]["full_quadratic_identity"],
            "Gamma_2=Q_triangle^irr+Q_phys^(2)",
        )
        self.assertEqual(
            family["Q_phys"]["R_cut_status"],
            "NOT_CONSTRUCTED_COEFFICIENT_TRANSPORT_OPEN",
        )
        cut = family["Q_cut"]
        self.assertEqual(len(cut["records"]), 48)
        self.assertEqual(len(cut["unique_children"]), 6)
        self.assertEqual(
            len({row["child_graph_sha256"] for row in cut["records"]}),
            6,
        )
        self.assertTrue(all(row["coefficient"] == "OPEN" for row in cut["records"]))
        self.assertEqual(family["CT2"]["coefficient"], "OPEN")
        self.assertEqual(
            family["Q_phys"]["local_UV_pole"],
            "FAIL_CLOSED_NOT_COMPUTED",
        )

    def test_branch_numbers_are_literals_and_never_graph_counts(self) -> None:
        terms = self.payload["complete_Q_contact"]["Q_Hess"]["terms"]
        order = (
            "minus_I0_G0_H2_G0",
            "minus_I1_p1_G0_H1_p2_G0",
            "minus_I1_p2_G0_H1_p1_G0",
            "plus_I2_G0",
        )
        self.assertEqual([terms[key]["branch_path_literal"] for key in order], [576, 1440, 1440, 720])
        for key in order:
            self.assertEqual(
                terms[key]["branch_path_literal_status"],
                "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
            )
            self.assertNotIn("ordered_vector_branch_paths", terms[key])
            self.assertFalse(any("graph_count" in field for field in terms[key]))
        h2 = self.payload["complete_quadratic_family"]["I0_H2"]
        self.assertEqual(h2["branch_path_literal"], 576)
        self.assertEqual(
            h2["branch_path_literal_status"],
            "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
        )

    def test_Wick_and_Hessian_minus_signs_are_alternative_representations(self) -> None:
        projection = self.payload["bubble_projection_and_coefficient"]
        transport = projection["single_sign_transport_obligation"]
        self.assertEqual(transport["status"], "FAIL_CLOSED_NOT_DERIVED")
        self.assertIn("never multiply the two", transport["rule"])
        self.assertEqual(
            projection["euclidean_action_expansion"]["representation"],
            "WICK_EXPANSION_ONLY",
        )
        self.assertTrue(
            all(
                row["scalar_coefficient"]["coefficient_usage"]
                == "WICK_REPRESENTATION_ONLY_DO_NOT_MULTIPLY_BY_HESSIAN_NEUMANN_SIGN"
                for row in projection["records"]
            )
        )
        hessian_terms = self.payload["complete_Q_contact"]["Q_Hess"]["terms"].values()
        self.assertTrue(
            all(row["sign_usage"] == "HESSIAN_REPRESENTATION_ONLY" for row in hessian_terms)
        )
        serialized = json.dumps(self.payload["complete_Q_contact"], sort_keys=True)
        self.assertNotIn("combined_sign", serialized)
        self.assertNotIn("total_sign", serialized)

    def test_color_certificate_is_index_incidence_only(self) -> None:
        color = self.payload["color_AST"]
        projection = self.payload["bubble_projection_and_coefficient"]
        tadpoles = self.payload["I4_tadpoles"]
        self.assertEqual(
            color["status"],
            "INDEX_INCIDENCE_ONLY_PHYSICAL_COLOR_REDUCTION_OPEN",
        )
        self.assertEqual(color["physical_color_reduction"], "FAIL_CLOSED_NOT_COMPUTED")
        self.assertEqual(color["counts"]["total"], 540)
        self.assertEqual(
            sorted(row["labeled_graph_id"] for row in color["bubble_tensors"]),
            sorted(row["labeled_graph_id"] for row in projection["records"]),
        )
        self.assertEqual(
            sorted(row["labeled_graph_id"] for row in color["tadpole_tensors"]),
            sorted(row["labeled_graph_id"] for row in tadpoles["records"]),
        )
        rows = color["bubble_tensors"] + color["tadpole_tensors"]
        self.assertTrue(all(all(row["tensor"]["checks"].values()) for row in rows))

    def test_projector_scope_counts_are_reconstructed_from_rows(self) -> None:
        projection = self.payload["bubble_projection_and_coefficient"]
        records = projection["records"]
        self.assertEqual(len(records), 360)
        self.assertEqual(
            projection["counts"]["both_exact_local"],
            sum(row["both_external_projectors_local"] for row in records),
        )
        self.assertEqual(
            projection["counts"]["requires_shared_scope_D_algebra"],
            sum(not row["both_external_projectors_local"] for row in records),
        )
        self.assertEqual(
            projection["wick_scalar_histogram_after_hg2"],
            {"-1/8192*g^2": 216, "1/16384*g^2": 144},
        )
        self.assertEqual(
            projection["local_scalar_histogram_after_extraction"],
            {"-1/128*g^2": 24, "1/256*g^2": 8},
        )

    def test_I4_DRED_zero_is_conditional_on_edge_tagged_proof(self) -> None:
        tadpoles = self.payload["I4_tadpoles"]
        self.assertEqual(
            tadpoles["normal_order_policy"]["status"],
            "FAIL_CLOSED_BARE_COMPOSITE_RENORMALIZATION_PRESCRIPTION_OPEN",
        )
        self.assertEqual(
            tadpoles["counts"],
            {
                "admitted_self_contractions": 180,
                "conditional_DRED_zero": 180,
                "certified_DRED_zero": 0,
                "projection_pending": 180,
            },
        )
        self.assertTrue(
            all(
                row["DRED_value"] == "CONDITIONAL_ZERO_PROOF_OBLIGATION_OPEN"
                and row["missing_edge_tagged_locality_to_polynomial_proof"]
                for row in tadpoles["records"]
            )
        )
        i2 = self.payload["complete_Q_contact"]["Q_Hess"]["terms"]["plus_I2_G0"]
        self.assertEqual(
            i2["DRED_scaleless_value"],
            "CONDITIONAL_ZERO_LOCALITY_TO_POLYNOMIAL_OPEN",
        )
        self.assertEqual(
            i2["ordinary_UV_pole"],
            "NOT_SEPARATED_FROM_SCALELESS_UV_IR_PAIR",
        )

    def test_automorphism_is_assigned_audit_only(self) -> None:
        certificate = self.payload["typed_automorphisms"]
        self.assertEqual(
            certificate["status"],
            "ASSIGNED_ORDER_ONE_AUDIT_ONLY_PHYSICAL_STABILIZER_OPEN",
        )
        self.assertEqual(certificate["contact_typed_automorphism_order_literal"], 1)
        self.assertEqual(certificate["physical_stabilizers"], "FAIL_CLOSED_NOT_COMPUTED")
        self.assertEqual(
            certificate["Taylor_Wick_factorial_matching"],
            "FAIL_CLOSED_NOT_COMPUTED",
        )
        self.assertFalse(certificate["automorphism_division_applied"])

    def test_all_physical_coefficient_boundaries_remain_fail_closed(self) -> None:
        obligations = self.payload["proof_obligations"]
        self.assertEqual(len(obligations), 10)
        self.assertTrue(
            all(row["severity"] != "CLOSED" and row.get("missing") for row in obligations)
        )
        self.assertEqual(
            self.payload["open_proof_obligation_ids"],
            [row["id"] for row in obligations],
        )
        self.assertEqual(
            self.payload["pole_boundary"]["anomaly_coefficient"],
            "NOT_ACCEPTED",
        )
        self.assertFalse(
            self.payload["pole_boundary"]["invalidated_coefficient_reused"]
        )
        self.assertFalse(self.payload["external_results_imported"])

    def test_artifacts_are_byte_reproducible_and_fail_closed(self) -> None:
        paths = (OUTPUT, AUDIT_JSON, AUDIT_MD)
        before = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
        }
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        after = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths
        }
        self.assertEqual(before, after)
        audit = json.loads(AUDIT_JSON.read_text())
        self.assertEqual(
            audit["status"],
            "FAIL_CLOSED_PHYSICAL_CONTACT_FAMILY_WITH_SCHEMA_INVARIANTS",
        )
        self.assertEqual(audit["resolved_gates"], [])
        self.assertEqual(
            audit["fail_closed_gates"],
            [row["id"] for row in self.payload["proof_obligations"]],
        )
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertGreater(audit["totals"]["schema_invariants"], 10)


if __name__ == "__main__":
    unittest.main()
