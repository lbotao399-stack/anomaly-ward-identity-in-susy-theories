from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ab_ba_project_ward_finite_renormalization_exact_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location("step5_ab_ba_project_ward_finite_renormalization_exact_audit", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Step5ABBAProjectWardFiniteRenormalizationExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = load_module()
        cls.payload = cls.audit.build_artifact()

    def test_all_exact_checks_pass(self) -> None:
        checks = self.payload["checks"]
        self.assertEqual(checks["failed"], 0)
        self.assertEqual(checks["passed"], checks["count"])

    def test_quotient_layers_are_not_mixed(self) -> None:
        project = self.payload["project_derivation"]
        self.assertEqual(project["common_compact_TD_vector"], ["0", "1", "-2*sqrt(2)*i", "2*sqrt(2)*i"])
        self.assertEqual(project["hybrid_vector_rejected"], ["2", "1", "-2*sqrt(2)*i", "2*sqrt(2)*i"])

    def test_finite_project_ward_solution(self) -> None:
        project = self.payload["project_derivation"]
        self.assertEqual(project["finite_counterterm"], ["1", "0", "sqrt(2)*i", "-sqrt(2)*i"])
        self.assertEqual(project["renormalized_vector"], ["1", "1", "-sqrt(2)*i", "sqrt(2)*i"])
        self.assertEqual(
            self.payload["topology_limited_candidate"]["verdict"],
            "REJECTED_SCALE_TWO_CONFLICTS_WITH_TARGET_BLIND_AA_WARD_NORMALIZATION",
        )

    def test_ht_is_check_only_and_exact(self) -> None:
        self.assertFalse(self.payload["external_target_used_in_derivation"])
        self.assertEqual(self.payload["after_check_only"]["status"], "EXACT_MATCH")
        self.assertEqual(
            self.payload["after_check_only"]["read_after_project_seal"],
            self.payload["project_seal_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
