from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_ab_ba_g3_full_resolvent_census_exact_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location("g3_full_resolvent", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class G3FullResolventCensusExactTest(unittest.TestCase):
    def test_full_resolvent(self) -> None:
        module = load_module()
        ledger = module.Ledger()
        census = module.resolvent_census(ledger)
        sd = module.sd_and_normalization(ledger)
        payload = json.loads(module.JSON_OUT.read_text(encoding="utf-8"))
        self.assertEqual(payload["checks"]["failed"], 0)
        self.assertTrue(all(row["status"] == "PASS" for row in ledger.rows))
        self.assertEqual(
            payload["status"],
            "PASS_FULL_RESOLVENT_CENSUS__NO_MISSING_1PI_C2C3_FAMILY__G3_SCALE_TWO_REMAINS",
        )
        self.assertEqual(
            len(census["I0S3S3"]["one_loop_1PI"]), 2
        )
        self.assertEqual(payload["conclusion"]["missing_net_correction"], "0")
        self.assertEqual(sd["G32_typed"], "-2*sqrt(2)*i")


if __name__ == "__main__":
    unittest.main()
