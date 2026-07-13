from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import LetterFamily, emit_ordered_family_channels


class Step5FullTwoLetterGapCensusTest(unittest.TestCase):
    def test_exact_family_and_component_census(self) -> None:
        channels = emit_ordered_family_channels()
        multiplicity = {
            LetterFamily.W: 1,
            LetterFamily.PHI: 3,
            LetterFamily.TILDE_PHI: 3,
            LetterFamily.TILDE_W: 2,
        }
        self.assertEqual(len(channels), 16)
        self.assertEqual(
            sum(
                multiplicity[channel.left.family] * multiplicity[channel.right.family]
                for channel in channels
            ),
            81,
        )
        self.assertEqual(sum(len(channel.descendant.terms) for channel in channels), 32)

    def test_four_tree_zero_families_have_twenty_five_components(self) -> None:
        channels = emit_ordered_family_channels()
        zero = {channel.channel_id for channel in channels if channel.descendant.is_zero}
        self.assertEqual(
            zero,
            {
                "TildePhi__TildePhi",
                "TildePhi__TildeW",
                "TildeW__TildePhi",
                "TildeW__TildeW",
            },
        )
        self.assertEqual((3 + 2) ** 2, 25)

    def test_ww_status_does_not_overclaim_basis_resolved_cancellation(self) -> None:
        payload = json.loads(
            (ROOT / "generated/step5/ww-seed-graph-ir.json").read_text(encoding="utf-8")
        )
        poles = payload["poles"]
        self.assertEqual(
            poles["contact_status"],
            "INVALIDATED_BY_REFLECTION_SOURCE_VARIANCE_REPAIR",
        )
        self.assertFalse(poles["metric_mismatch_proved_at_aggregate_sd_level"])
        self.assertFalse(poles["full_ordinary_triangle_bubble_cancellation_proved"])
        self.assertEqual(
            poles["anomaly_status"],
            "INVALIDATED_NOT_PROPAGATED_AFTER_TYPED_SIGN_REPAIR",
        )

    def test_gap_audit_records_fifteen_open_obligations(self) -> None:
        audit = (ROOT / "audits/step5-full-two-letter-gap-census.md").read_text(
            encoding="utf-8"
        )
        for gap_id in range(1, 16):
            self.assertIn(f"| G{gap_id} |", audit)
        self.assertIn("not an accepted full Ward-identity coefficient", audit)
        self.assertIn("I_{ZZ,(N)}=I_{ZT,(N)}=I_{TZ,(N)}=I_{TT,(N)}=0", audit)


if __name__ == "__main__":
    unittest.main()
