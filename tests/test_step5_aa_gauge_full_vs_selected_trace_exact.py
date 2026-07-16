from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_aa_gauge_full_vs_selected_trace_exact_audit.py"


class AAGaugeFullVsSelectedTraceExactTest(unittest.TestCase):
    def test_exact_trace_audit(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("SUMMARY 15/15 PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
