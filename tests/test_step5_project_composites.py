from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_project_composites import (
    ExactScalar,
    antichiral_gauge_s3_terms,
    build_payload,
    component_transport_coefficients,
    e_xi_terms,
    gamma_terms,
    gauge_s4_terms,
    insertion_terms_at_valence,
    matrix_transport_coefficients,
    operator_names,
    seed_port_assignment_payload,
    series_sign_audit,
    transport_e_xi_terms,
    tilde_gamma_terms,
    tilde_w_terms,
    v_slots,
    w_terms,
    x_terms_at_degree,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_project_composites.py"
GENERATED = ROOT / "generated/step5/project-composites.json"
AUDIT = ROOT / "audits/step5-project-composites-verification.json"


class Step5ProjectCompositesTest(unittest.TestCase):
    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_generated = GENERATED.read_bytes()
        first_audit = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_generated, GENERATED.read_bytes())
        self.assertEqual(first_audit, AUDIT.read_bytes())
        audit = json.loads(first_audit)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 34, "failed": 0})
        self.assertEqual(audit["physical_euler_transport_series"], "project_functional_euler")
        self.assertEqual(
            audit["user_requested_seed_transport_status"],
            "REJECTED_BY_5_28_TRANSPOSITION",
        )
        self.assertEqual(audit["generated_sha256"], hashlib.sha256(first_generated).hexdigest())

    def test_gamma_w_x_are_project_bch_series_not_exp_2gv_imports(self) -> None:
        self.assertEqual(
            [term.coefficient for term in gamma_terms()],
            [
                ExactScalar(1),
                ExactScalar(Fraction(-1, 2), i_power=1),
                ExactScalar(Fraction(1, 6), i_power=2),
            ],
        )
        self.assertEqual(
            [term.coefficient for term in w_terms()],
            [
                ExactScalar(Fraction(-1, 8)),
                ExactScalar(Fraction(1, 16), i_power=1),
                ExactScalar(Fraction(1, 48)),
            ],
        )
        self.assertEqual(
            [term.coefficient.render() for term in tilde_gamma_terms()],
            ["-1", "-1/2*i", "1/6"],
        )
        self.assertTrue(all(
            "FlatBarD" in operator_names(term.expression)
            and "FlatD" not in operator_names(term.expression)
            for term in tilde_gamma_terms()
        ))
        self.assertEqual(
            [term.coefficient.render() for term in tilde_w_terms()],
            ["-1/8", "-1/16*i", "1/48"],
        )
        self.assertEqual(
            [[term.coefficient.render() for term in x_terms_at_degree(degree)] for degree in (1, 2, 3)],
            [
                ["-1/8"],
                ["1/16*i", "-1/8*i"],
                ["1/48", "-1/16", "-1/16"],
            ],
        )
        payload = build_payload()
        self.assertFalse(payload["canonical_exp_2gV_coefficients_imported"])
        self.assertEqual(payload["external_imports"], [])

    def test_e_xi_core_is_concrete_through_required_order(self) -> None:
        terms = e_xi_terms()
        self.assertEqual(len(terms), 13)
        self.assertEqual(
            [term.v_degree for term in terms],
            [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 0],
        )
        self.assertEqual(
            [term.origin for term in terms[:2]],
            ["D_- W_+", "D_+ W_-"],
        )
        self.assertEqual(
            [term.coefficient.render() for term in terms[:2]],
            ["-1/16*h*kappa[A,B]", "1/16*h*kappa[A,B]"],
        )
        matter = terms[-1]
        self.assertEqual(matter.origin, "-i (Phi_r x TildePhi_r)")
        self.assertEqual(matter.matter_degree, 2)
        self.assertEqual(
            matter.coefficient,
            ExactScalar(-1, i_power=1, symbols=("h", "kappa[A,B]")),
        )
        self.assertTrue(all(len(v_slots(term.expression)) == term.v_degree for term in terms))

    def test_functional_euler_and_requested_transport_are_not_silently_identified(self) -> None:
        self.assertEqual(
            matrix_transport_coefficients("project_functional_euler"),
            (Fraction(1), Fraction(1, 2), Fraction(1, 6), Fraction(1, 24)),
        )
        self.assertEqual(
            matrix_transport_coefficients("user_requested_seed_transport"),
            (Fraction(1), Fraction(-1, 2), Fraction(-1, 6), Fraction(-1, 24)),
        )
        self.assertEqual(
            component_transport_coefficients("project_functional_euler"),
            (
                ExactScalar(1),
                ExactScalar(Fraction(1, 2), i_power=1),
                ExactScalar(Fraction(1, 6), i_power=2),
                ExactScalar(Fraction(1, 24), i_power=3),
            ),
        )
        audit = series_sign_audit()
        self.assertTrue(audit["project_equals_direct_transposition"])
        self.assertFalse(audit["requested_equals_direct_transposition"])
        self.assertEqual(audit["conflict_degrees"], [1, 2, 3])
        self.assertEqual(len(transport_e_xi_terms("project_functional_euler")), 24)
        self.assertEqual(len(transport_e_xi_terms("user_requested_seed_transport")), 24)
        payload = build_payload()
        self.assertEqual(payload["E_V"]["physical_SD_uses"], "project_functional_euler")
        self.assertEqual(
            payload["E_V"]["user_requested_seed_transport_status"],
            "REJECTED_BY_5_28_TRANSPOSITION",
        )

    def test_I2_I3_I4_keep_direct_and_outer_connection_terms(self) -> None:
        i2, i3, i4 = (insertion_terms_at_valence(valence) for valence in (2, 3, 4))
        self.assertEqual([len(i2), len(i3), len(i4)], [2, 10, 30])
        self.assertEqual(
            {tag for term in i2 for tag in term.tags if tag.startswith("D_MINUS_")},
            {"D_MINUS_LEFT", "D_MINUS_RIGHT"},
        )
        self.assertFalse(any("OUTER_NABLA_MINUS_CONNECTION" in term.tags for term in i2))
        self.assertEqual(
            sum("OUTER_NABLA_MINUS_CONNECTION" in term.tags for term in i3),
            2,
        )
        self.assertEqual(
            sum("OUTER_NABLA_MINUS_CONNECTION" in term.tags for term in i4),
            10,
        )
        self.assertTrue(all(term.parity == 1 for term in i2 + i3 + i4))
        self.assertTrue(all("QUARTIC_CONTACT" in term.tags for term in i4))
        for term in i2 + i3 + i4:
            slots = v_slots(term.expression)
            self.assertEqual(len(slots), term.v_degree)
            self.assertEqual(len(slots), len(set(slots)))

    def test_gauge_s4_and_ordered_background_quantum_ports_are_exact(self) -> None:
        s4 = gauge_s4_terms()
        self.assertEqual(
            [term.coefficient.render() for term in s4],
            [
                "1/1536*h",
                "1/1024*h",
                "1/1536*h",
                "1/1536*h",
                "1/1024*h",
                "1/1536*h",
            ],
        )
        self.assertEqual(
            [term.coefficient.render() for term in antichiral_gauge_s3_terms()],
            ["-1/512*i*h", "-1/512*i*h"],
        )
        port_payload = seed_port_assignment_payload()
        self.assertEqual(
            port_payload["counts"],
            {
                "I3_all": 80,
                "I4_all": 480,
                "S4_all": 96,
                "S3_antichiral_all": 16,
                "I3_one_background_two_quantum_projected": 30,
                "S3_antichiral_one_background_two_quantum_projected": 6,
                "I4_two_background_two_quantum_tadpole": 180,
                "S4_mixed_X_TildeW": 0,
            },
        )
        for family, assignments in port_payload["all_ordered_assignments"].items():
            for assignment in assignments:
                self.assertEqual(assignment["ordered_assignment_multiplicity"], 1)
                self.assertFalse(assignment["coefficient_changed_by_split"])
                port_ids = [port["port_id"] for port in assignment["ordered_ports"]]
                self.assertEqual(len(port_ids), len(set(port_ids)), family)
                self.assertTrue(all("derivative_word_outer_to_inner" in port for port in assignment["ordered_ports"]))
                self.assertIn("color_bracket_word", assignment)

        i3_selected = port_payload["selected_for_seed"]["I3_one_background_two_quantum"]
        s3_selected = port_payload["selected_for_seed"]["S3_antichiral_one_background_two_quantum"]
        self.assertTrue(
            all(len(item["external_projections"]) == 1 and len(item["quantum_ports"]) == 2 for item in i3_selected)
        )
        self.assertTrue(all(
            item["external_projections"][0]["target"] == "TILDE_W_EXTERNAL_AFTER_PROJECTOR"
            and len(item["quantum_ports"]) == 2
            for item in s3_selected
        ))
        mixed_s4 = port_payload["selected_for_seed"]["S4_mixed_X_TildeW"]
        self.assertEqual(
            mixed_s4["status"],
            "PROVED_ABSENT_BY_INTRINSIC_EUCLIDEAN_CHIRAL_SECTOR",
        )
        self.assertEqual(mixed_s4["graphir_rows"], [])
        tadpoles = port_payload["selected_for_seed"]["I4_two_background_two_quantum_tadpole"]
        self.assertEqual(len(tadpoles), 180)
        self.assertTrue(all(
            item["classification"] == "SCALELESS_IF_SOLE_LOOP_HAS_NO_EXTERNAL_MOMENTUM"
            for item in tadpoles
        ))


if __name__ == "__main__":
    unittest.main()
