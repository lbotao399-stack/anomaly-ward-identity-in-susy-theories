from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_global_81_target_blind_orbit_ledger_audit.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("step5_global_81_target_blind_orbit_ledger_audit", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Step5Global81TargetBlindOrbitLedgerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = load_audit_module()
        cls.payload = cls.audit.build_payload()
        cls.rows = cls.payload["rows"]

    def test_cartesian_exhaustion_and_complete_counts(self) -> None:
        self.assertEqual(len(self.rows), 81)
        self.assertEqual(len({row["pair_id"] for row in self.rows}), 81)
        expected = {
            f"{left}__{right}"
            for left in self.audit.LETTERS
            for right in self.audit.LETTERS
        }
        self.assertEqual({row["pair_id"] for row in self.rows}, expected)
        self.assertEqual(
            Counter(row["final_state"] for row in self.rows),
            Counter({"COMPLETE_EXACT": 81}),
        )
        self.assertEqual(
            Counter(row["resolution"] for row in self.rows),
            Counter({"EXACT_NONZERO": 29, "EXACT_ZERO": 52}),
        )
        self.assertEqual(
            Counter(row["representative_maturity"] for row in self.rows),
            Counter({"COMPLETED": 81}),
        )
        self.assertTrue(all(row["result"] is not None and row["blocker"] is None for row in self.rows))

    def test_target_blind_input_boundary_and_artifact_readback(self) -> None:
        evidence_paths = set(self.payload["evidence_inputs"])
        self.assertNotIn("generated/step5/project-result-ledger.json", evidence_paths)
        self.assertNotIn("generated/step5/ht_ordered_pair_targets.json", evidence_paths)
        self.assertNotIn("audits/step5-ht-roundtrip-audit.json", evidence_paths)
        self.assertNotIn("audits/step5-ab1-standard-feynman-strictification.md", evidence_paths)
        self.assertNotIn("audits/step5-ab1-marked-sd-orbit-exact.md", evidence_paths)
        self.assertIn("audits/step5-ab-ba-project-ward-finite-renormalization-exact.json", evidence_paths)
        self.assertIn("audits/step5-ab-ba-vector-frame-missing-orbit-exact.json", evidence_paths)
        self.assertIn("audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json", evidence_paths)
        self.assertIn("audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json", evidence_paths)
        self.assertIn("audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json", evidence_paths)
        self.assertFalse(self.payload["external_target_used"])
        self.assertFalse(self.payload["project_result_ledger_used"])

        json_path = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.json"
        md_path = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.md"
        self.assertEqual(json_path.read_text(encoding="utf-8"), self.audit.render_json(self.payload))
        self.assertEqual(md_path.read_text(encoding="utf-8"), self.audit.render_markdown(self.payload))
        self.assertEqual(json.loads(json_path.read_text(encoding="utf-8")), self.payload)

    def test_explicit_flavor_koszul_color_transport(self) -> None:
        by_pair = {row["pair_id"]: row for row in self.rows}

        bb12 = by_pair["B1__B2"]
        bb21 = by_pair["B2__B1"]
        self.assertEqual(bb12["result"]["coefficients_over_lambda1"], ["-sqrt(2)*I", "sqrt(2)*I"])
        self.assertEqual(bb21["result"]["coefficients_over_lambda1"], ["sqrt(2)*I", "-sqrt(2)*I"])
        self.assertIn("epsilon_123=1", bb12["transport"]["coefficient_sign"])
        self.assertIn("epsilon_213=-1", bb21["transport"]["coefficient_sign"])
        self.assertEqual(bb12["transport"]["source_slot_map"], "L->L;R->R;ORDER_REVERSAL_NOT_USED")
        self.assertEqual(bb12["transport"]["color_map"], "(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged")

        self.assertEqual(by_pair["B1__B1"]["marked_terms"], [
            {"side": "L", "letter": "B1", "leibniz_sign": 1},
            {"side": "R", "letter": "B1", "leibniz_sign": -1},
        ])
        self.assertEqual(by_pair["B1__B1"]["resolution"], "EXACT_ZERO")
        self.assertEqual(by_pair["B1__Ddot1"]["resolution"], "EXACT_ZERO")
        self.assertEqual(by_pair["Ddot1__B1"]["resolution"], "EXACT_ZERO")
        self.assertEqual(by_pair["C1__B1"]["marked_terms"], [
            {"side": "R", "letter": "B1", "leibniz_sign": 1},
        ])
        self.assertEqual(
            self.payload["symmetry_maps"]["ORDER_REBASE_RECORDED_BUT_NOT_USED"]["color"],
            "(A,B,D,E)->(B,A,E,D)",
        )

    def test_aa_ab_ba_and_ad_da_completed_exact_vectors(self) -> None:
        by_pair = {row["pair_id"]: row for row in self.rows}

        aa = by_pair["A__A"]
        self.assertEqual(aa["final_state"], "COMPLETE_EXACT")
        self.assertEqual(aa["resolution"], "EXACT_NONZERO")
        self.assertEqual(
            aa["result"]["coefficients_over_lambda1"],
            ["1", "-1", "1", "-1", "1", "-1", "1", "-1"],
        )
        self.assertIn("Q_e*mu_l^2", aa["cutting_failure_certificate"])

        for dot in (1, 2):
            ad = by_pair[f"A__Ddot{dot}"]
            da = by_pair[f"Ddot{dot}__A"]
            self.assertEqual(ad["final_state"], "COMPLETE_EXACT")
            self.assertEqual(da["final_state"], "COMPLETE_EXACT")
            self.assertEqual(ad["result"]["coefficients_over_lambda1"], ["1/3", "2/3"])
            self.assertEqual(da["result"]["coefficients_over_lambda1"], ["2/3", "1/3"])
            self.assertIn("m_parent=m_contact=1", ad["cutting_failure_certificate"])
            self.assertIn("m_parent=m_contact=1", da["cutting_failure_certificate"])

        cyclic = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
        for r, (s, t) in cyclic.items():
            for pair_id in (f"A__B{r}", f"B{r}__A"):
                row = by_pair[pair_id]
                self.assertEqual(row["final_state"], "COMPLETE_EXACT")
                self.assertEqual(row["resolution"], "EXACT_NONZERO")
                self.assertEqual(
                    row["result"]["basis"],
                    [f"<D^D,B{r}^E>", f"<B{r}^D,D^E>", f"<C{s}^D,C{t}^E>", f"<C{t}^D,C{s}^E>"],
                )
                self.assertEqual(
                    row["result"]["coefficients_over_lambda1"],
                    ["1", "1", "-sqrt(2)*I", "sqrt(2)*I"],
                )
                self.assertIn("not an independent anomaly graph", row["cutting_failure_certificate"])


if __name__ == "__main__":
    unittest.main()
