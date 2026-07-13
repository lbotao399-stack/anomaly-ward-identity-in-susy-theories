from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_background_ward_recursion import (
    add_series,
    build_payload,
    dexp_series,
    exact_checks,
    exponential_series,
    inverse_series,
    multiply_series,
    vector_subgroup_profile,
    variation_coefficients,
    ward_subset_profile,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_background_ward_recursion.py"
GENERATED = ROOT / "generated/step5/background-ward-recursion.json"
AUDIT = ROOT / "audits/step5-background-ward-recursion-verification.json"


class Step5BackgroundWardRecursionTest(unittest.TestCase):
    def test_dexp_inverse_is_exact_over_q(self) -> None:
        for order in range(0, 13):
            dexp = dexp_series(order)
            inverse = inverse_series(dexp, order)
            self.assertEqual(
                multiply_series(dexp, inverse, order),
                (Fraction(1),) + (Fraction(),) * order,
            )

    def test_left_and_right_coefficients_solve_group_equation(self) -> None:
        for order in range(1, 13):
            self.assertTrue(all(exact_checks(order).values()))

    def test_first_bernoulli_coefficients_are_project_ordered(self) -> None:
        coefficients = variation_coefficients(6)
        self.assertEqual(
            coefficients["eta_left"],
            (
                Fraction(1),
                Fraction(-1, 2),
                Fraction(1, 12),
                Fraction(),
                Fraction(-1, 720),
                Fraction(),
                Fraction(1, 30240),
            ),
        )
        self.assertEqual(
            coefficients["eta_right"],
            (
                Fraction(-1),
                Fraction(-1, 2),
                Fraction(-1, 12),
                Fraction(),
                Fraction(1, 720),
                Fraction(),
                Fraction(-1, 30240),
            ),
        )

    def test_vector_subgroup_collapses_to_one_commutator(self) -> None:
        coefficients = variation_coefficients(12)
        vector = add_series(coefficients["eta_left"], coefficients["eta_right"])
        self.assertEqual(
            vector,
            (Fraction(), Fraction(-1)) + (Fraction(),) * 11,
        )

    def test_rhs_reconstruction_is_eta_l_minus_exp_eta_r(self) -> None:
        order = 10
        coefficients = variation_coefficients(order)
        self.assertEqual(
            multiply_series(dexp_series(order), coefficients["eta_left"], order),
            (Fraction(1),) + (Fraction(),) * order,
        )
        self.assertEqual(
            multiply_series(dexp_series(order), coefficients["eta_right"], order),
            tuple(-coefficient for coefficient in exponential_series(order)),
        )

    def test_polarized_ward_recursion_has_all_subsets_once(self) -> None:
        for level in range(9):
            profile = ward_subset_profile(level)
            self.assertEqual(profile["term_count"], 2**level)
            self.assertEqual(profile["expected_term_count"], 2**level)
            self.assertEqual(
                sum(profile["by_nonlinear_order"].values()),
                2**level,
            )
            self.assertEqual(
                len({tuple(subset) for subset in profile["subsets"]}),
                2**level,
            )
            self.assertEqual(
                profile["seagull_contact_count"],
                max(0, 2**level - level - 1),
            )

    def test_chiral_frame_and_vector_subgroup_scopes_do_not_mix(self) -> None:
        payload = build_payload()
        chiral = payload["polarized_chiral_frame_Ward_recursion"]
        self.assertEqual(chiral["frame"], "GAUGE_CHIRAL")
        self.assertEqual(chiral["output_representation"], "rho_2(eta_R)")
        self.assertIn("eta_L,eta_R", chiral["identity"])
        self.assertIn("FAIL_CLOSED", chiral["quantum_insertion_status"])

        vector = payload["vector_subgroup"]
        self.assertFalse(vector["level_mixing"])
        self.assertEqual(
            vector["Taylor_maps"],
            {"R_0": "0", "R_1": "[eta,V]", "R_r_ge_2": "0"},
        )
        for level in range(7):
            profile = vector_subgroup_profile(level)
            self.assertEqual(profile["same_level_commutator_terms"], level)
            self.assertEqual(profile["higher_level_terms"], 0)

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())
        payload = json.loads(generated_first)
        audit = json.loads(audit_first)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 3, "failed": 0})
        self.assertEqual(
            audit["generated_sha256"],
            hashlib.sha256(generated_first).hexdigest(),
        )
        self.assertFalse(payload["external_results_imported"])
        self.assertFalse(payload["graph_coefficients_present"])
        self.assertFalse(payload["anomaly_coefficients_present"])

    def test_payload_does_not_claim_graph_acceptance(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["schema"], "Step5BackgroundWardRecursion.v2")
        self.assertEqual(payload["vector_subgroup"]["result"], "delta_V=-ad_V(eta)")


if __name__ == "__main__":
    unittest.main()
