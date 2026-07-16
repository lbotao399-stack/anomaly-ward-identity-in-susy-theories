from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_aa_gauge_correct_index_selected_moments_exact_audit.py"


class CorrectedAAGaugeSelectedMomentsTest(unittest.TestCase):
    def test_all_exact_checks_pass(self) -> None:
        spec = importlib.util.spec_from_file_location("aa_selected_moments", SCRIPT)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        checks = module.build_checks()
        self.assertTrue(checks)
        self.assertTrue(all(row.passed for row in checks))


if __name__ == "__main__":
    unittest.main()
