from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ht_ab_epsilon_canonicalization_exact_audit.py"
SPEC = importlib.util.spec_from_file_location("ht_ab_epsilon_canonicalization", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HTABEpsilonCanonicalizationExactTest(unittest.TestCase):
    def test_common_basis_ratio_and_hessian(self) -> None:
        payload = MODULE.build_artifact()
        self.assertEqual(payload["ordered_basis"]["HT"], ["-sqrt(2)*i", "sqrt(2)*i"])
        self.assertEqual(payload["ordered_basis"]["raw"], ["-2*sqrt(2)*i", "2*sqrt(2)*i"])
        self.assertEqual(
            payload["canonical_two_tensor_basis"]["HT"],
            ["-sqrt(2)*i", "-sqrt(2)*i"],
        )
        self.assertEqual(
            payload["canonical_two_tensor_basis"]["raw"],
            ["-2*sqrt(2)*i", "-2*sqrt(2)*i"],
        )
        self.assertEqual(payload["canonical_single_monomial_bases"]["ratio_in_either_basis"], "2")
        self.assertEqual(payload["hessian_factor"]["exact_result"], "(1/2!)*(1+1)=1")
        self.assertEqual(
            payload["first_false_equality"]["correct"],
            "F^{AB}_{ED}=F^{BA}_{DE}",
        )
        self.assertIn("STILL_TWICE_HT", payload["verdict"])
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
