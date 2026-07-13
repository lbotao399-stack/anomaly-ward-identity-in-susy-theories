from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_one_loop_ghost_background_census import (
    AUDIT,
    GENERATED,
    attachment_census,
    build_payload,
    joined_cycle_rank,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_ghost_background_census.py"


class Step5OneLoopGhostBackgroundCensusTest(unittest.TestCase):
    def test_joined_cycle_rank_identity(self) -> None:
        for physical_loops in range(5):
            for attachments in range(1, 8):
                self.assertEqual(
                    joined_cycle_rank(physical_loops, 1, attachments),
                    physical_loops + attachments,
                )

    def test_single_attachment_is_1pr_and_two_attachments_start_at_two_loops(self) -> None:
        rows = attachment_census(max_background_order=12)
        self.assertTrue(
            all(
                not row["one_particle_irreducible"]
                for row in rows
                if row["attachment_edges"] == 1
            )
        )
        self.assertTrue(
            all(
                row["loop_number"] >= 2
                for row in rows
                if row["one_particle_irreducible"]
            )
        )

    def test_background_order_never_changes_cycle_rank(self) -> None:
        rows = attachment_census(max_background_order=12)
        grouped: dict[tuple[int, int], set[int]] = {}
        for row in rows:
            key = (row["physical_loops"], row["attachment_edges"])
            grouped.setdefault(key, set()).add(row["loop_number"])
        self.assertTrue(all(len(loop_numbers) == 1 for loop_numbers in grouped.values()))

    def test_all_background_result_is_scoped_to_step5a_1pi(self) -> None:
        payload = build_payload(max_background_order=12)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["scope"], "STEP5A_ONE_LOOP_1PI_ALL_BACKGROUND_ORDERS")
        self.assertEqual(
            payload["result"],
            "PROVED_ABSENT_AT_ONE_LOOP_1PI_ALL_BACKGROUND_ORDERS",
        )
        self.assertEqual(payload["finite_BV_cycle_statement"], "NOT_USED; STEP5C_OBLIGATION")

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())
        payload = json.loads(generated_first)
        audit = json.loads(audit_first)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 5, "failed": 0, "rows": 108})
        self.assertEqual(
            audit["generated_sha256"],
            hashlib.sha256(generated_first).hexdigest(),
        )
        self.assertFalse(payload["external_results_imported"])


if __name__ == "__main__":
    unittest.main()
