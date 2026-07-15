from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Step5AdDaOrderedPortsCrossedHessianExactTest(unittest.TestCase):
    def test_artifact(self) -> None:
        script = ROOT / "scripts" / "step5_ad_da_ordered_ports_crossed_hessian_exact_audit.py"
        artifact = ROOT / "audits" / "step5-ad-da-ordered-ports-crossed-hessian-exact.json"
        note = ROOT / "audits" / "step5-ad-da-ordered-ports-crossed-hessian-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        self.assertTrue(note.is_file())
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_TARGET_BLIND_AD_DA_FULL_CHIRALITY_RAW_CONTACT_AND_LINK__"
            "HOLOMORPHIC_TWIST_COEFFICIENTS_MATCH",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(
            payload["routing"]["background_output_ports"],
            {
                "left": {"field": "D_lower", "momentum": "q_IR", "alias": "k_left"},
                "right": {"field": "D_upper", "momentum": "p_IR", "alias": "k_right"},
            },
        )
        self.assertEqual(
            payload["source_hessian_color"]["su2_orthogonal_projectors"],
            {
                "direct": {
                    "A_B_D_E": [0, 1, 1, 0],
                    "F_AB": "-2",
                    "F_BA": "0",
                },
                "crossed": {
                    "A_B_D_E": [0, 1, 0, 1],
                    "F_AB": "0",
                    "F_BA": "-2",
                },
            },
        )
        self.assertEqual(
            payload["finite_vector"]["four_chirality_sum"],
            {
                "sector_weights": {"++": "1", "+-": "1", "-+": "1", "--": "1"},
                "R1_raw": {"p_raw": "i/12", "q_raw": "i/24"},
                "R2_raw": {"p_raw": "i/6", "q_raw": "i/12"},
                "rank_trace_correction": "1/2",
                "R1_corrected_raw": {"p_raw": "i/24", "q_raw": "i/48"},
                "R2_corrected_raw": {"p_raw": "i/12", "q_raw": "i/24"},
                "legacy_component_master_conversion": "-8",
                "R1_over_lambda1": {
                    "p_raw=q_IR": "-i/3",
                    "q_raw=p_IR": "-i/6",
                },
                "R2_over_lambda1": {
                    "p_raw=q_IR": "-2*i/3",
                    "q_raw=p_IR": "-i/3",
                },
            },
        )
        self.assertEqual(
            payload["finite_vector"]["typed_projection"]
            ["canonical_bracket_coefficients"],
            {
                "AD": {"P_on_left": "1/3", "P_on_right": "2/3"},
                "DA": {"P_on_left": "2/3", "P_on_right": "1/3"},
            },
        )
        self.assertEqual(
            payload["normalization"]["four_chirality_times_corrected_conversion"],
            "4*(-4)=-16",
        )
        self.assertEqual(payload["rank_trace_from_AD_DA_SD"]["m_contact"], "1")
        self.assertEqual(
            payload["schwinger_rows"]["generated_raw_contact"]["full_d_check"],
            "4 frames * 4 occurrence/color rows * 4 chirality sectors: "
            "N_d+K_raw=0",
        )
        self.assertEqual(
            payload["finite_vector"]["full_chirality_matrix_status"],
            "PASS_P_ONLY_112_OF_112__Q_ONLY_112_OF_112",
        )
        self.assertEqual(payload["checks"]["failed"], 0)
        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS AD_DA_ACTION_PORT_MOMENTA_P_Q", completed.stdout)
        self.assertIn("PASS AD_DA_FULL_CHIRALITY_P_Q_SYMBOLIC", completed.stdout)
        self.assertIn("PASS AD_DA_RAW_CONTACT_MULTIPLICITY_ONE", completed.stdout)
        self.assertIn("PASS AD_DA_FINITE_W_LINK_LONGITUDINAL_ZERO", completed.stdout)
        self.assertIn("PASS AD_DA_HOLOMORPHIC_TWIST_COEFFICIENTS", completed.stdout)
        self.assertIn("REJECTED AD_DA_IMPORTED_PRO_MOMENTUM_MAP", completed.stdout)


if __name__ == "__main__":
    unittest.main()
