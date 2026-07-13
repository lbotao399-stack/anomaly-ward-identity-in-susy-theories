from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_one_loop_hessian_insertion_census import (
    AUDIT,
    GENERATED,
    build_payload,
    hessian_compositions,
    labeled_term_rows,
    ordered_set_partitions,
    positive_compositions,
    source_block_support,
    typed_path_templates,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_hessian_insertion_census.py"


class Step5OneLoopHessianInsertionCensusTest(unittest.TestCase):
    def test_positive_compositions(self) -> None:
        self.assertEqual(list(positive_compositions(0, 0)), [()])
        self.assertEqual(list(positive_compositions(3, 2)), [(1, 2), (2, 1)])
        self.assertEqual(list(positive_compositions(4, 3)), [(1, 1, 2), (1, 2, 1), (2, 1, 1)])

    def test_family_counts(self) -> None:
        self.assertEqual(
            {n: len(hessian_compositions(n)) for n in (2, 3, 4)},
            {2: 4, 3: 8, 4: 16},
        )

    def test_ordered_labeled_partition_count(self) -> None:
        partitions = list(ordered_set_partitions((1, 2, 3, 4), (1, 1, 2)))
        self.assertEqual(len(partitions), 12)
        for blocks in partitions:
            flattened = [label for block in blocks for label in block]
            self.assertEqual(sorted(flattened), [1, 2, 3, 4])

    def test_n2_exhaustive_four_families_and_six_polarizations(self) -> None:
        rows = labeled_term_rows(2)
        self.assertEqual(len(rows), 6)
        families = {
            (row["s"], tuple(row["r_parts"]), row["neumann_sign"])
            for row in rows
        }
        self.assertEqual(
            families,
            {
                (0, (1, 1), 1),
                (0, (2,), -1),
                (1, (1,), -1),
                (2, (), 1),
            },
        )
        multiplicities = {
            family: sum(
                (row["s"], tuple(row["r_parts"]), row["neumann_sign"])
                == family
                for row in rows
            )
            for family in families
        }
        self.assertEqual(
            multiplicities,
            {
                (0, (1, 1), 1): 2,
                (0, (2,), -1): 1,
                (1, (1,), -1): 2,
                (2, (), 1): 1,
            },
        )

    def test_reflection_is_an_involution(self) -> None:
        for n in (2, 3, 4):
            rows = labeled_term_rows(n)
            rows_by_id = {row["term_id"]: row for row in rows}
            self.assertEqual(len(rows_by_id), len(rows))
            for row in rows:
                reflected = rows_by_id[row["reflection"]["term_id"]]
                self.assertEqual(reflected["reflection"]["term_id"], row["term_id"])
                self.assertEqual(reflected["neumann_sign"], row["neumann_sign"])

    def test_source_absence_is_derived_only_from_free_field_support(self) -> None:
        rows = source_block_support()
        admitted = [row for row in rows if row["status"].startswith("FORMALLY_ADMITTED")]
        absent = [row for row in rows if row["status"].startswith("PROVED_ZERO")]
        self.assertEqual(admitted, [
            {
                "row_block": "V",
                "column_block": "V",
                "status": "FORMALLY_ADMITTED_I_s_BLOCK_VALUE_NOT_DERIVED",
                "proof": "both quantum derivatives are with respect to V",
            }
        ])
        self.assertEqual(len(absent), 35)
        self.assertTrue(all("outside {V}" in row["proof"] for row in absent))

    def test_typed_path_counts_and_graded_rejection(self) -> None:
        paths = typed_path_templates(max_k=4)
        self.assertEqual(
            {key: len(rows) for key, rows in paths.items()},
            {"K0": 1, "K1": 1, "K2": 6, "K3": 36, "K4": 216},
        )
        self.assertEqual(
            sum(row["valid_under_even_hessian_parity"] for row in paths["K4"]),
            125,
        )
        fp_paths = [
            row
            for row in paths["K4"]
            if "FP" in row["hessian_block_path"]
        ]
        self.assertTrue(fp_paths)
        self.assertTrue(
            all(not row["valid_under_even_hessian_parity"] for row in fp_paths)
        )

    def test_payload_is_fail_closed(self) -> None:
        payload = build_payload()
        self.assertEqual(payload["status"], "PASS_COMBINATORICS_FAIL_CLOSED_PHYSICS")
        self.assertEqual(
            payload["polarized_term_counts"],
            {"2": 6, "3": 26, "4": 150},
        )
        self.assertEqual(
            [row["counterterm_id"] for row in payload["counterterms"]],
            ["CT_2", "CT_3", "CT_4"],
        )
        obligation_ids = {row["id"] for row in payload["unresolved_obligations"]}
        self.assertTrue(
            {
                "SOURCE_PARTNER_AND_MEASURE",
                "GRADED_CYCLIC_SOURCE_SIGN",
                "FUNCTIONAL_HESSIAN_JACOBIAN",
            }.issubset(obligation_ids)
        )
        self.assertFalse(payload["external_results_imported"])

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())

        payload = json.loads(generated_first)
        audit = json.loads(audit_first)
        self.assertEqual(payload["status"], "PASS_COMBINATORICS_FAIL_CLOSED_PHYSICS")
        self.assertEqual(audit["status"], "PASS_COMBINATORICS_FAIL_CLOSED_PHYSICS")
        self.assertEqual(
            audit["totals"],
            {
                "checks": 10,
                "counterterms": 3,
                "failed": 0,
                "families": 28,
                "polarized_terms": 182,
                "source_block_rows": 36,
                "typed_path_templates": 260,
                "unresolved_obligations": 5,
            },
        )
        self.assertEqual(
            audit["generated_sha256"],
            hashlib.sha256(generated_first).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
