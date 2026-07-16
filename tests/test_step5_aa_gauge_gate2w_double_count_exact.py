from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_aa_gauge_gate2w_double_count_exact_audit.py"
AUDIT = ROOT / "audits" / "step5-aa-gauge-gate2w-double-count-exact.md"


class AAGaugeGate2WDoubleCountExactTest(unittest.TestCase):
    def test_exact_rejection_audit(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 16/16 PASS", completed.stdout)

    def test_boundaries_are_explicit(self) -> None:
        text = AUDIT.read_text(encoding="utf-8")
        self.assertIn(r"\frac{w_D^{2W}}{sE_{\rm exact}}", text)
        self.assertIn("rank-one momentum moment", text)
        self.assertIn("Gate-2W final vector is not derived", text)


if __name__ == "__main__":
    unittest.main()
