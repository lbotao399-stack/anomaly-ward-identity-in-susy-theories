from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_aa_gauge_field_normalization_factor8_exact_audit.py"
AUDIT = ROOT / "audits" / "step5-aa-gauge-field-normalization-factor8-exact.md"


class Step5AAGaugeFieldNormalizationFactor8ExactTest(unittest.TestCase):
    def test_exact_normalization_audit(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 49/49 PASS", completed.stdout)

    def test_factor_eight_and_index_boundaries_are_explicit(self) -> None:
        text = AUDIT.read_text(encoding="utf-8")
        self.assertIn("first wrong numerical step is Step-5 WW line 464", text)
        self.assertIn(r"\boxed{2\cdot4\cdot\frac18=1.}", text)
        self.assertIn(r"W^-=-W_+", text)
        self.assertIn("It fixes neither the final magnitude nor the directed sign", text)
        self.assertIn("No full AA gauge coefficient is assigned", text)


if __name__ == "__main__":
    unittest.main()
