from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5_euclidean_n4_awi.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location(
        "verify_step5_euclidean_n4_awi_acceptance", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Step5PhysicalAnomalySectorAcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_current_exact_evidence_accepts_only_physical_sector(self) -> None:
        payload = self.verifier.build_audit()
        self.assertEqual(payload["status"], "ACCEPTED", payload["failed_checks"])
        self.assertEqual(
            payload["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR"
        )
        self.assertEqual(payload["totals"]["failed"], 0)
        self.assertEqual(payload["counts"]["ordered_pairs"], 81)
        self.assertEqual(payload["counts"]["exact_nonzero"], 29)
        self.assertEqual(payload["counts"]["exact_zero"], 52)

    def test_broader_claims_remain_out_of_scope(self) -> None:
        payload = self.verifier.build_audit()
        self.assertTrue(
            payload["scope_boundary"]["out_of_scope_items_are_not_acceptance_blockers"]
        )
        self.assertEqual(
            payload["scope_boundary"]["out_of_scope"],
            {
                "RAW_Q_FUNCTOR": "OUT_OF_SCOPE",
                "BV_WZ_COMPLETION": "OUT_OF_SCOPE",
                "OPEN_COLOR_SOURCE_EXTENSION": "OUT_OF_SCOPE",
                "FORMAL_U_INTERTWINER": "OUT_OF_SCOPE",
                "GENERAL_REDUCTIVE_COLOR_THEOREM": "OUT_OF_SCOPE",
            },
        )

    def test_project_seal_tampering_fails_exact_ht_gate(self) -> None:
        payload = copy.deepcopy(self.verifier.load_json(self.verifier.HT_SYMBOLIC))
        payload["project_seal"]["source_sha256"] = "0" * 64
        audit = self.verifier.Audit()
        self.verifier.check_ht_symbolic(audit, payload)
        by_id = {row["id"]: row for row in audit.rows}
        self.assertEqual(
            by_id["ht.project_sealed_before_target_read"]["status"], "FAIL"
        )

    def test_obsolete_hybrid_quotient_is_not_an_acceptance_runner(self) -> None:
        scripts = {runner.script for runner in self.verifier.RUNNERS}
        self.assertNotIn(
            "scripts/step5_ab_ba_full_1pi_quotient_exact_audit.py", scripts
        )


if __name__ == "__main__":
    unittest.main()
