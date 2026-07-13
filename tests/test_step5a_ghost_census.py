from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_step5a_ghost_census.py"
AUDIT = ROOT / "audits/step5a-ghost-census.json"


def load_verifier():
    specification = importlib.util.spec_from_file_location("verify_step5a_ghost_census", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load Step-5A ghost census verifier")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5AGhostCensusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_verifier_is_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first = AUDIT.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = AUDIT.read_text(encoding="utf-8")
        self.assertEqual(first, second)
        audit = json.loads(first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["FP_result"], "PROVED_ABSENT_AT_THIS_ORDER")
        self.assertEqual(audit["NK_result"], "PROVED_ABSENT_AT_THIS_ORDER")

    def test_exact_project_FP_port_signatures_are_censused(self) -> None:
        signatures = self.verifier.fp_signatures()
        self.assertEqual(len(signatures), 10)
        by_valence = {
            valence: [entry for entry in signatures if entry["V_valence"] == valence]
            for valence in (0, 1, 2)
        }
        self.assertEqual({key: len(value) for key, value in by_valence.items()}, {0: 2, 1: 4, 2: 4})
        self.assertTrue(all(entry["ghost_valence"] == 2 for entry in signatures))

    def test_absence_is_graph_theoretic_not_a_cycle_blocker(self) -> None:
        audit = self.verifier.run_verification()
        proof = audit["graph_theoretic_proof"]
        self.assertEqual(len(audit["external_background_ports"]), 2)
        self.assertEqual(len(audit["I2_quantum_Wick_ports"]), 2)
        self.assertFalse(proof["connected_one_loop_families"])
        self.assertTrue(proof["first_connected_two_loop_families"])
        self.assertTrue(
            all(
                family["loop_number_E_minus_V_plus_1"] == 2
                for family in proof["first_connected_two_loop_families"]
            )
        )
        self.assertNotIn("BLOCKED", audit["FP_result"])
        self.assertNotIn("BLOCKED", audit["NK_result"])
        self.assertIn("Step-5C", audit["finite_cycle_statement"])

    def test_minimal_connected_FP_families_start_at_two_loops(self) -> None:
        families = self.verifier.enumerate_fp_families()
        one_quartic = next(
            family
            for family in families
            if (family["m0_V^0_cprime_c"], family["m1_V^1_cprime_c"], family["m2_V^2_cprime_c"])
            == (0, 0, 1)
        )
        two_cubics = next(
            family
            for family in families
            if (family["m0_V^0_cprime_c"], family["m1_V^1_cprime_c"], family["m2_V^2_cprime_c"])
            == (0, 2, 0)
        )
        self.assertEqual(one_quartic["internal_edges"], 3)
        self.assertEqual(one_quartic["vertices"], 2)
        self.assertEqual(one_quartic["loop_number_E_minus_V_plus_1"], 2)
        self.assertEqual(two_cubics["internal_edges"], 4)
        self.assertEqual(two_cubics["vertices"], 3)
        self.assertEqual(two_cubics["loop_number_E_minus_V_plus_1"], 2)

    def test_all_one_loop_FP_multisets_fail_connectivity_or_saturation(self) -> None:
        families = self.verifier.enumerate_fp_families()
        connected_one_loop = [
            family
            for family in families
            if family["connected"] and family["loop_number_E_minus_V_plus_1"] == 1
        ]
        self.assertEqual(connected_one_loop, [])
        m0_only = [
            family
            for family in families
            if family["m1_V^1_cprime_c"] == family["m2_V^2_cprime_c"] == 0
        ]
        self.assertTrue(m0_only)
        self.assertTrue(
            all(family["classification"] == "DISCONNECTED_GHOST_VACUUM_COMPONENT" for family in m0_only)
        )


if __name__ == "__main__":
    unittest.main()
