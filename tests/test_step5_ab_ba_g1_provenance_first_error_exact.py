from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_ab_ba_g1_provenance_first_error_exact_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location("g1_provenance_audit", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class G1ProvenanceFirstErrorExactTest(unittest.TestCase):
    def test_exact_first_error(self) -> None:
        module = load_module()
        payload = module.build_payload()
        self.assertEqual(payload["checks"]["failed"], 0)
        self.assertEqual(
            payload["status"],
            "PASS_G1_FIRST_ERROR_IS_PURE_DIVERGENCE_MISREPORTED_AS_PHYSICAL_TWO",
        )
        self.assertEqual(
            payload["source_selected_orbit"]["sum_typed"], ["0", "2"]
        )
        self.assertEqual(
            payload["rejected_generic_lift"]["status"],
            "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
        )


if __name__ == "__main__":
    unittest.main()
