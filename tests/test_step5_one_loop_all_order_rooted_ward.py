from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_one_loop_all_order_rooted_ward import (
    AUDIT_JSON,
    AUDIT_MD,
    GENERATED,
    MAX_CHECKED_ORDER,
    build_payload,
    canonical_trace_word,
    inverse_variation_certificate,
    order_certificate,
    polarized_count_formula,
    ward_variation_terms,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_all_order_rooted_ward.py"


class Step5OneLoopAllOrderRootedWardTest(unittest.TestCase):
    def test_exact_family_and_polarized_counts(self) -> None:
        expected_polarized = [1, 2, 6, 26, 150, 1082, 9366]
        self.assertEqual(
            [polarized_count_formula(n) for n in range(MAX_CHECKED_ORDER + 1)],
            expected_polarized,
        )
        for n in range(MAX_CHECKED_ORDER + 1):
            row = order_certificate(n)
            self.assertEqual(row["family_count_enumerated"], 2**n)
            self.assertEqual(
                row["polarized_count_enumerated"], expected_polarized[n]
            )
            self.assertTrue(all(row["checks"].values()))

    def test_even_similarity_variation_telescopes_in_trace(self) -> None:
        words = [
            ("I", "G"),
            ("I", "G", "H1", "G"),
            ("I", "G", "H1", "G", "H2", "G"),
            ("I", "G", "H1", "G", "H2", "G", "H3", "G"),
        ]
        for word in words:
            self.assertEqual(ward_variation_terms(word), {})
        self.assertEqual(canonical_trace_word(("B", "C", "A")), ("A", "B", "C"))

    def test_inverse_variation_is_exact_commutator(self) -> None:
        certificate = inverse_variation_certificate()
        self.assertTrue(certificate["passed"])
        self.assertEqual(
            certificate["reduced"],
            [
                {"word": ["G", "R"], "coefficient": "-1"},
                {"word": ["R", "G"], "coefficient": "1"},
            ],
        )

    def test_scope_remains_fail_closed(self) -> None:
        payload = build_payload()
        self.assertTrue(
            payload["acceptance_boundary"]["all_order_rooted_one_loop_census_accepted"]
        )
        self.assertFalse(
            payload["acceptance_boundary"][
                "all_order_background_covariant_completion_accepted"
            ]
        )
        self.assertFalse(
            payload["acceptance_boundary"][
                "triangle_determines_every_local_dressing_accepted"
            ]
        )
        self.assertEqual(
            payload["project_gates"]["quadratic_jet_injectivity"],
            "OPEN_RELATION_MATRIX",
        )
        self.assertEqual(
            payload["project_gates"]["dred_regulated_supertrace_cyclicity"],
            "PASS_PROJECT_TEST_DOMAIN_5.19A",
        )
        self.assertEqual(
            payload["project_gates"]["dred_loop_translation_invariance"],
            "PASS_PROJECT_MOMENTUM_SUBSPACE_5.13A",
        )
        self.assertFalse(payload["external_results_imported"])

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_generated = GENERATED.read_bytes()
        first_audit = AUDIT_JSON.read_bytes()
        first_markdown = AUDIT_MD.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_generated, GENERATED.read_bytes())
        self.assertEqual(first_audit, AUDIT_JSON.read_bytes())
        self.assertEqual(first_markdown, AUDIT_MD.read_bytes())
        audit = json.loads(first_audit)
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(first_generated).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
