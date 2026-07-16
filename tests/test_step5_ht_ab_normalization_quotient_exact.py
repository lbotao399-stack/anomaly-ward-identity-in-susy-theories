from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ht_ab_normalization_quotient_exact_audit.py"
SPEC = importlib.util.spec_from_file_location("ht_ab_normalization", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HTABNormalizationQuotientExactTest(unittest.TestCase):
    def test_exact_normalization_and_layer_boundary(self) -> None:
        payload = MODULE.build_artifact()
        self.assertEqual(payload["ab_translation"]["verdict"], "SCALE_ONE")
        self.assertEqual(
            payload["ab_translation"]["HT_zero_component_main_compact_vector"],
            ["1", "1", "-sqrt(2)*i", "sqrt(2)*i"],
        )
        self.assertEqual(
            payload["raw_and_quotient_layers"]["hybrid_over_HT_scale_candidates"],
            ["2", "1", "2", "2"],
        )
        self.assertEqual(payload["raw_and_quotient_layers"]["global_normalization_solution"], [])
        self.assertEqual(payload["aa_q_covariance"]["unique_scale"], "t=1")
        self.assertEqual(payload["first_error_equality"]["raw_local_invalid_step"], "T_BD=0")
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
