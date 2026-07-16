from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_bbdiagonal_bd_db_exact_zero_audit.py"
ARTIFACT = ROOT / "audits/step5-bbdiagonal-bd-db-exact-zero.json"


def load_module():
    spec = importlib.util.spec_from_file_location("step5_bbdiagonal_bd_db_exact_zero_audit_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Step5BBDiagonalBDDBExactZeroTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = load_module()
        cls.payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_all_fifteen_pairs_and_all_399_routes_are_closed(self) -> None:
        self.assertEqual(self.payload["summary"], {
            "all_routes": 399,
            "alternative_rows": 102,
            "exact_zero_pairs": 15,
            "ordered_pairs": 15,
            "spectator_routes": 288,
            "split_routes": 111,
            "symbolic_dword_checks": 117,
        })
        self.assertEqual(
            {row["pair_id"] for row in self.payload["pair_results"]},
            set(self.audit.TARGET_PAIRS),
        )
        self.assertTrue(all(row["result"] == "0" for row in self.payload["pair_results"]))
        self.assertEqual(
            Counter(row["classification"] for row in self.payload["route_rows"]),
            Counter({"EXACT_ZERO_1PR_EXCLUDED": 288, "EXACT_ZERO_PROJECTED_DWORD": 111}),
        )
        census = json.loads(self.audit.CENSUS_PATH.read_text(encoding="utf-8"))
        regenerated = self.audit.build_route_rows(census)
        self.assertEqual(regenerated, self.payload["route_rows"])

    def test_symbolic_words_flavor_rows_and_koszul_transport(self) -> None:
        symbolic = self.payload["symbolic_dword"]
        self.assertEqual(symbolic["check_count"], 117)
        self.assertTrue(all(row["passed"] and row["actual"] == "0" for row in symbolic["checks"]))
        self.assertEqual(symbolic["TGM"]["symbolic_projection_count"], 96)
        self.assertEqual(symbolic["TMM"]["symbolic_projection_count"], 4)
        self.assertEqual(symbolic["TMH"]["symbolic_projection_count"], 4)
        self.assertEqual(symbolic["matter_quartic"]["symbolic_projection_count"], 4)
        self.assertEqual(symbolic["BB_diagonal"]["TMM"]["graded_leibniz_signs"], [1, -1])
        self.assertEqual(
            {row["tensor"] for row in symbolic["BB_diagonal"]["H_Yukawa_flavor_rows"]},
            {"epsilon_rtu*delta_rt=epsilon_rru", "epsilon_rtu*delta_ru=epsilon_rtr"},
        )
        by_pair = {row["pair_id"]: row for row in self.payload["pair_results"]}
        self.assertEqual(by_pair["B1__Ddot1"]["transport"]["marked_signs"], ["L:+1"])
        self.assertEqual(by_pair["Ddot1__B1"]["transport"]["marked_signs"], ["R:-1"])

    def test_target_and_project_result_ledgers_are_absent(self) -> None:
        self.assertFalse(self.payload["external_target_used"])
        self.assertFalse(self.payload["project_result_ledger_used"])
        inputs = set(self.payload["inputs"])
        self.assertNotIn("generated/step5/project-result-ledger.json", inputs)
        self.assertNotIn("generated/step5/ht_ordered_pair_targets.json", inputs)


if __name__ == "__main__":
    unittest.main()
