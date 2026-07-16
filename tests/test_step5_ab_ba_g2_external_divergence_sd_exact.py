import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_ab_ba_g2_external_divergence_sd_exact_audit.py"


class Step5ABBAG2ExternalDivergenceSDExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("g2_external_divergence_sd", SCRIPT)
        cls.module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        sys.modules[spec.name] = cls.module
        spec.loader.exec_module(cls.module)
        cls.artifact = cls.module.build_artifact()

    def test_all_exact_checks_pass(self):
        checks = self.artifact["checks"]
        self.assertEqual(checks["failed"], 0)
        self.assertEqual(checks["passed"], checks["count"])

    def test_no_target_or_q_input(self):
        self.assertFalse(self.artifact["external_target_used"])
        self.assertFalse(self.artifact["q_covariance_used"])

    def test_full_d_sd_and_physical_pair(self):
        self.assertEqual(self.artifact["r2_sd_orbit"]["full_d"], "0")
        self.assertEqual(
            self.artifact["typed_coefficients"]["pair_EOM"],
            ["-1/3", "4/3"],
        )
        self.assertEqual(
            self.artifact["typed_coefficients"]["exact_divergence_quotient_pair"],
            "1",
        )


if __name__ == "__main__":
    unittest.main()
