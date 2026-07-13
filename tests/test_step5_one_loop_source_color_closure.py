from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_one_loop_source_color_closure import (
    AUDIT_JSON,
    AUDIT_MD,
    GENERATED,
    background_ce_certificate,
    build_payload,
    color_split_monomorphism_certificate,
    local_source_jet_certificate,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_source_color_closure.py"


class Step5OneLoopSourceColorClosureTest(unittest.TestCase):
    def test_background_ce_closes_odd_source_and_pairing(self) -> None:
        certificate = background_ce_certificate()
        self.assertTrue(all(certificate["checks"].values()), certificate)
        self.assertEqual(certificate["rules"]["source"], "s_B J=J Gamma")
        self.assertEqual(certificate["parities"]["J_times_I"], 0)

    def test_local_source_momentum_and_covariant_source_jet_are_retained(self) -> None:
        certificate = local_source_jet_certificate()
        self.assertTrue(all(certificate["checks"].values()), certificate)
        block = certificate["W_T_N_D_local_source_block"]
        self.assertEqual(block["source_momentum"]["status"], "RETAINED_NONZERO")
        self.assertNotEqual(block["source_momentum"]["exact_witness"]["p_J"], 0)
        self.assertEqual(block["relation_rank"], 2)
        self.assertEqual(block["quotient_dimension"], 1)
        self.assertEqual(
            block["representative_equations"],
            ["C_split=0", "S_DJ=-C_on_W"],
        )

    def test_color_sym2_quotient_is_split_but_unmatched_quotient_is_not(self) -> None:
        certificate = color_split_monomorphism_certificate()
        self.assertTrue(all(certificate["checks"].values()), certificate)
        self.assertEqual(
            certificate["maps"]["composition"], "pi_1 o iota_M=id_M"
        )
        self.assertEqual(
            certificate["matrices"]["unmatched_collapsed_jet"], [["0"]]
        )

    def test_scope_does_not_conflate_background_ce_with_full_bv_slavnov(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["verdicts"]["odd_local_source_background_CE_closure"], "PASS")
        self.assertEqual(
            payload["verdicts"]["full_quantum_BV_Slavnov_source_complex"],
            "FAIL_CLOSED_MISSING_COMPOSITE_SOURCE_PARTNERS_AND_LINEARIZED_ST_MATRIX",
        )
        self.assertEqual(
            payload["verdicts"]["complete_quadratic_jet_injectivity"],
            "NOT_CLAIMED_BY_THIS_CERTIFICATE",
        )
        self.assertEqual(payload["verdicts"]["anomaly_coefficient"], "NOT_ACCEPTED")

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
