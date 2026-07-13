from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_frame_bridge_intertwiner import (
    AUDIT,
    AUDIT_MD,
    GENERATED,
    adjoint_bridge_full,
    abstract_similarity_checks,
    background_ward_intertwiner_witness,
    build_payload,
    frame_witness,
    nonlinear_tangent_hessian_witness,
    project_adjoint_bridge_checks,
)
from scripts.verify_step5a_fixed_kernel import MOMENTA


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_frame_bridge_intertwiner.py"


class Step5FrameBridgeIntertwinerTest(unittest.TestCase):
    def test_general_adjoint_similarity_is_order_exact(self) -> None:
        checks = abstract_similarity_checks()
        self.assertTrue(all(checks.values()), checks)

    def test_exact_project_adjoint_bridge(self) -> None:
        checks = project_adjoint_bridge_checks()
        self.assertTrue(all(checks.values()), checks)

    def test_background_dependent_full_coefficient_map(self) -> None:
        frame, frame_inverse, parities = adjoint_bridge_full()
        self.assertEqual(len(frame), 48)
        self.assertEqual(len(frame_inverse), 48)
        self.assertEqual(parities.count(0), 24)
        self.assertEqual(parities.count(1), 24)

    def test_all_exact_quadratic_witnesses_pass(self) -> None:
        for momentum in MOMENTA:
            witness = frame_witness(momentum)
            self.assertEqual(witness["dimension"], 48)
            self.assertEqual(witness["even_dimension"], 24)
            self.assertEqual(witness["odd_dimension"], 24)
            self.assertTrue(all(witness["checks"].values()), witness)

    def test_nonlinear_tangent_connection_is_retained(self) -> None:
        witness = nonlinear_tangent_hessian_witness()
        self.assertTrue(all(witness["checks"].values()), witness)
        self.assertEqual(
            witness["coordinate_map"], "y1=x1; y2=x2+(1/2)*x1^2"
        )

    def test_background_ward_recursion_transports(self) -> None:
        witness = background_ward_intertwiner_witness()
        self.assertTrue(all(witness["checks"].values()), witness)

    def test_scope_distinguishes_similarity_tangent_and_density(self) -> None:
        payload = build_payload()
        self.assertEqual(
            payload["scope"],
            "COVARIANT_ADJOINT_SIMILARITY_AND_TANGENT_CHAIN_RULE",
        )
        gates = payload["gates"]
        self.assertEqual(
            gates["covariant_operator_similarity_general_gauge_algebra"],
            "PASS",
        )
        self.assertEqual(
            gates["nonlinear_quantum_tangent_hessian"],
            "CONDITIONAL_E_V_C_EQUALS_ZERO",
        )
        self.assertEqual(
            gates["nonlinear_source_hessian_insertion"],
            "CONDITIONAL_F_V_C_EQUALS_ZERO",
        )
        self.assertEqual(
            gates["full_finite_bv_density_and_cycle"], "OPEN_STEP5C_3D110"
        )
        self.assertEqual(
            gates["cross_frame_functional_equality_with_independent_flat_measures"],
            "NOT_ASSERTED",
        )
        self.assertEqual(gates["anomaly_coefficient"], "NOT_COMPUTED")
        self.assertEqual(payload["checked_equation_groups"], 8)
        self.assertEqual(len(payload["gap_ledger"]), 6)
        required_gap_keys = {
            "id",
            "type",
            "location",
            "claim",
            "missing",
            "minimal_repair",
            "severity",
            "status",
        }
        for gap in payload["gap_ledger"]:
            self.assertEqual(set(gap), required_gap_keys)

    def test_former_toy_gl_witness_is_removed(self) -> None:
        payload = build_payload()
        self.assertIn("arbitrary 2x2 GL witness is removed", payload["frame_matrix_deprecation"])
        self.assertNotIn("frame", payload["witnesses"][0])

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        audit_markdown_first = AUDIT_MD.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())
        self.assertEqual(audit_markdown_first, AUDIT_MD.read_bytes())
        self.assertNotIn(b"{{", audit_markdown_first)
        payload = json.loads(generated_first)
        audit = json.loads(audit_first)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertGreater(audit["totals"]["checks"], 80)
        self.assertEqual(
            audit["generated_sha256"],
            hashlib.sha256(generated_first).hexdigest(),
        )
        self.assertEqual(
            audit["audit_markdown_sha256"],
            hashlib.sha256(audit_markdown_first).hexdigest(),
        )
        self.assertFalse(payload["external_results_imported"])


if __name__ == "__main__":
    unittest.main()
