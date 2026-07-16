from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AaExternalSlotDecompositionExactTest(unittest.TestCase):
    def test_artifact(self) -> None:
        script = ROOT / "scripts" / "step5_aa_external_slot_decomposition_exact_audit.py"
        artifact = ROOT / "audits" / "step5-aa-external-slot-decomposition-exact.json"
        note = ROOT / "audits" / "step5-aa-external-slot-decomposition-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(
            payload["formal_polarization"]["identity"],
            "H_full=H_linear_field_strength+H_derivative_commutator+H_plain_commutator",
        )
        self.assertEqual(
            payload["raw_port_partition"]["counts"],
            {
                "+": {
                    "linear_field_strength": 8,
                    "derivative_commutator": 8,
                    "plain_commutator": 8,
                },
                "-": {
                    "linear_field_strength": 8,
                    "derivative_commutator": 8,
                    "plain_commutator": 8,
                },
            },
        )
        self.assertEqual(payload["raw_port_partition"]["old_fixed_omitted_rows"], 32)
        for row in payload["sample_component_replay"]:
            self.assertEqual(row["placement_sum"], row["full_action_hessian"])
        quotient = payload["source_edge_quotient"]
        self.assertEqual(
            quotient["aggregate_edge_divisibility"]["division_remainders"],
            {"T0": "0", "T2": "0"},
        )
        self.assertFalse(
            quotient["aggregate_edge_divisibility"]["affine_fit_valid"]
        )
        self.assertTrue(
            quotient["aggregate_edge_divisibility"]["held_out"][
                "replayed_from_full_probe"
            ]
        )
        self.assertEqual(
            quotient["combined_raw_row_edge_table"],
            "CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA",
        )
        occurrence = payload["occurrence_edge_structural_lemma"]
        self.assertEqual(
            occurrence["unique_surviving_color_chain"],
            [0, 2, 1],
        )
        self.assertFalse(occurrence["reflection_changes_physical_source_edge"])
        self.assertEqual(len(occurrence["placement_reflection_rows"]), 18)
        self.assertEqual(
            occurrence["combined_raw_row_edge_status"],
            "CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA",
        )
        raw_contact = occurrence[
            "raw_schwinger_contact_hessian_certificate"
        ]
        self.assertEqual(
            raw_contact["status"],
            "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE",
        )
        self.assertEqual(
            raw_contact["verified_multiplicity"],
            {"m0": "1", "m2": "1"},
        )
        self.assertEqual(raw_contact["raw_Hessian_group_count"], 24)
        self.assertEqual(raw_contact["raw_Hessian_endpoint_row_count"], 48)
        self.assertTrue(
            all(
                row["N_d_plus_K_raw"] == "0"
                for row in raw_contact["polynomial_cancellations"]
            )
        )
        exhaustive = payload["exhaustive_component_replay"]
        if "total_equality_failures" in exhaustive:
            self.assertEqual(exhaustive["total_equality_failures"], 0)
        self.assertTrue(
            payload["sector_pair_interaction"]["held_out_probe"][
                "replayed_from_full_probe"
            ]
        )
        typed = payload["typed_ordered_reconstruction"]
        self.assertEqual(
            typed["typed_projector_matrix"]["matrix"],
            [["-I", "-1"], ["-1", "-I"]],
        )
        self.assertEqual(typed["typed_projector_matrix"]["determinant"], "-2")
        self.assertEqual(
            typed["scalar_coefficients_before_global_normalization"],
            {"p": "-I/2", "q": "-I"},
        )
        self.assertEqual(
            typed["ordered_vector_over_lambda1_times_F"],
            ["I", "2*I", "-I", "-2*I"],
        )
        self.assertEqual(
            typed["fourier_and_physical_quotient"][
                "post_fourier_extended_vector_over_lambda1_times_F"
            ],
            ["1", "2", "-1", "-2"],
        )
        self.assertEqual(
            typed["fourier_and_physical_quotient"][
                "physical_ordered_p_vector_over_lambda1_times_F"
            ],
            ["1", "-1"],
        )
        self.assertEqual(
            typed["fourier_and_physical_quotient"]["physical_status"],
            "ACCEPTED_RAW_SCHWINGER_CONTACT_MULTIPLICITY_ONE_VERIFIED",
        )
        self.assertEqual(
            typed["contact_only_frames"]["p_transverse"],
            "REJECTED_OPPOSITE_UNDOTTED_CONTAMINATION_FOR_TYPED_SOLVE",
        )
        self.assertEqual(
            payload["matter_primitive_sign"][
                "ordered_vector_over_lambda1_times_F"
            ],
            ["1", "-1"],
        )
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS AA_EXTERNAL_SLOT_SUM_EQUALS_FULL_HESSIAN", completed.stdout)


if __name__ == "__main__":
    unittest.main()
