import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_ab_ba_vector_frame_missing_orbit_exact_audit.py"


spec = importlib.util.spec_from_file_location("step5_ab_ba_vector_frame_missing_orbit_exact_audit", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class VectorFrameMissingOrbitExactTest(unittest.TestCase):
    def test_exact_audit(self) -> None:
        artifact = module.build_artifact()
        self.assertEqual(artifact["checks"]["failed"], 0)
        self.assertFalse(
            artifact["requested_delta_test"]["vector_frame_missing_orbit_can_supply_delta"]
        )
        self.assertEqual(artifact["one_loop_missing_orbit"]["cc_support"], [])
        self.assertEqual(
            artifact["bridge_expansion"]["B_ad_E_ad_inverse_B_ad"],
            ["1", "0", "0"],
        )
        self.assertEqual(
            artifact["quotient_layer_audit"]["common_compact_TD_vector"],
            ["0", "1", "-2*i*sqrt(2)", "2*i*sqrt(2)"],
        )
        self.assertFalse(artifact["quotient_layer_audit"]["hybrid_valid"])
        self.assertEqual(
            artifact["project_q_ward_completion"]
            ["topology_limited_missing_graph_hypothesis"]["unique_solution"],
            ["2", "1", "0", "0"],
        )
        self.assertEqual(
            artifact["project_q_ward_completion"]
            ["general_finite_composite_source_counterterm"]["unique_solution"],
            ["1", "0", "i*sqrt(2)", "-i*sqrt(2)"],
        )
        self.assertEqual(
            artifact["project_q_ward_completion"]
            ["general_finite_composite_source_counterterm"]["renormalized_vector"],
            ["1", "1", "-i*sqrt(2)", "i*sqrt(2)"],
        )


if __name__ == "__main__":
    unittest.main()
