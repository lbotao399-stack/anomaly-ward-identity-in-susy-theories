from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5SpectatorSourceSelfEnergyOrbitExactTest(unittest.TestCase):
    def test_exact_artifact_and_validator(self) -> None:
        script = ROOT / "scripts/step5_spectator_source_self_energy_orbit_exact_audit.py"
        artifact_path = ROOT / "audits/step5-spectator-source-self-energy-orbit-exact.json"
        markdown_path = ROOT / "audits/step5-spectator-source-self-energy-orbit-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact_path.is_file())
        self.assertTrue(markdown_path.is_file())

        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["schema"],
            "step5-spectator-source-self-energy-orbit-exact-v1",
        )
        self.assertFalse(artifact["external_target_used"])
        self.assertFalse(artifact["holomorphic_twist_target_read"])
        global_ledger = artifact["global_family_ledger"]
        self.assertEqual(global_ledger["route_count"], 870)
        self.assertEqual(
            global_ledger["topology_counts"],
            {"TGG": 612, "THH": 78, "TMM": 180},
        )
        self.assertEqual(global_ledger["connected_route_count"], 870)
        self.assertEqual(global_ledger["one_particle_irreducible_route_count"], 0)
        self.assertEqual(global_ledger["source_action_cut_edge_count"], 870)
        self.assertEqual(global_ledger["quantum_cut_edge_mark_occurrences"], 486)
        self.assertEqual(global_ledger["external_spectator_mark_occurrences"], 600)
        self.assertEqual(global_ledger["marked_loop_cycle_edge_occurrences"], 0)
        self.assertEqual(artifact["graph_cut_identity"]["P_1PI"], "0")
        self.assertEqual(
            artifact["DRED_projector_identity"]["P_anomaly_P_1PI"],
            "0",
        )
        self.assertEqual(
            artifact["D_word_controls"]["TMM_samples"]["q1200_loop3500"]
            ["one_delta_collapsed_word"],
            "1280",
        )
        self.assertEqual(
            artifact["ordered_pair_ledgers"]["A__C1"]["topology_counts"],
            {"TGG": 18, "THH": 1, "TMM": 4},
        )
        self.assertEqual(
            artifact["ordered_pair_ledgers"]["B1__C1"]["topology_counts"],
            {"THH": 2, "TMM": 2},
        )
        settlement = artifact["coefficient_settlement"]
        self.assertEqual(
            settlement["A__C_r"]["amputated_1PI_result"],
            ["-1", "+1"],
        )
        self.assertEqual(
            settlement["B_r__C_s"]["amputated_1PI_result"],
            "+delta_rs",
        )

        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS spectator_route_count: 870", completed.stdout)
        self.assertIn(
            "PASS one_particle_irreducible_route_count: 0",
            completed.stdout,
        )
        self.assertIn(
            "PASS marked_loop_cycle_edge_occurrences: 0",
            completed.stdout,
        )
        self.assertIn("PASS AC_CA_coefficients_unchanged", completed.stdout)
        self.assertIn("PASS BC_CB_Konishi_unchanged", completed.stdout)
        self.assertIn("SUMMARY 19/19 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
