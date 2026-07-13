from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.step5_graph_ir import Statistics, Variance
from scripts.step5_one_loop_n2_physical_hessian_family import (
    AUDIT_JSON,
    AUDIT_MD,
    GENERATED,
    J_WW_FIELD,
    action_hessian_branches,
    build_payload,
    family_graphs,
    fp_quantum_interaction_monomials,
    source_kernel_branches,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_n2_physical_hessian_family.py"


class Step5OneLoopN2PhysicalHessianFamilyTest(unittest.TestCase):
    def test_source_kernel_branch_counts(self) -> None:
        self.assertEqual(
            {order: len(source_kernel_branches(order)) for order in (0, 1, 2)},
            {0: 4, 1: 60, 2: 720},
        )
        self.assertTrue(
            all(
                row["functional_derivative_koszul_sign"] == 1
                for order in (0, 1, 2)
                for row in source_kernel_branches(order)
            )
        )

    def test_action_hessian_block_counts(self) -> None:
        expected = {
            1: {
                "V": 24,
                "PHI_PAIR_1": 2,
                "PHI_PAIR_2": 2,
                "PHI_PAIR_3": 2,
                "FP": 0,
                "NK": 0,
            },
            2: {
                "V": 144,
                "PHI_PAIR_1": 4,
                "PHI_PAIR_2": 4,
                "PHI_PAIR_3": 4,
                "FP": 0,
                "NK": 0,
            },
        }
        for order in (1, 2):
            rows = action_hessian_branches(order)
            self.assertEqual(
                {
                    block: sum(row["block_id"] == block for row in rows)
                    for block in expected[order]
                },
                expected[order],
            )
        payload = build_payload()
        for order in (1, 2):
            diagonal = {
                row["row_block"]: row
                for row in payload["action_hessian_block_matrices"][f"H{order}"]
                if row["row_block"] == row["column_block"]
            }
            for block in ("FP", "NK"):
                self.assertEqual(
                    diagonal[block]["status"], "BLOCKED_MISSING_PROJECT_BLOCK"
                )

    def test_fp_quantum_vertices_are_excluded_from_background_hessian(self) -> None:
        rows = fp_quantum_interaction_monomials()
        self.assertEqual(
            {name: len(entries) for name, entries in rows.items()},
            {"V_QUANTUM_ORDER_1": 4, "V_QUANTUM_ORDER_2": 4},
        )
        self.assertTrue(
            all(
                row["classification"]
                == "QUANTUM_INTERACTION_NOT_BACKGROUND_HESSIAN"
                and row["background_hessian_status"]
                == "BLOCKED_MISSING_PROJECT_BLOCK"
                for entries in rows.values()
                for row in entries
            )
        )

    def test_exact_six_loop_families_plus_ct2(self) -> None:
        graphs = family_graphs()
        self.assertEqual(len(graphs), 7)
        self.assertEqual([graph.cycle_rank() for graph in graphs], [1, 1, 1, 1, 1, 1, 0])
        self.assertTrue(
            all(graph.validate_linear_momentum_routing()["passed"] for graph in graphs)
        )
        self.assertEqual(
            [dict(graph.metadata)["automorphism_order"] for graph in graphs],
            ["1"] * 7,
        )
        self.assertEqual(
            len({dict(graph.metadata)["canonical_key"] for graph in graphs}),
            7,
        )

    def test_source_is_odd_and_old_orientation_sign_is_not_reused(self) -> None:
        payload = build_payload()
        self.assertIs(J_WW_FIELD.statistics, Statistics.FERMION)
        self.assertEqual(
            [index.variance for index in J_WW_FIELD.indices],
            [Variance.DOWN, Variance.DOWN],
        )
        type_audit = payload["source_and_projected_type_audit"]
        self.assertEqual(type_audit["new_family_graphir_source_statistics"], "FERMION")
        self.assertEqual(type_audit["required_tildeW_dotted_variance"], "DOWN")
        self.assertEqual(type_audit["required_fixed_graphir_reflected_sign"], 1)
        self.assertFalse(type_audit["old_orientation_sign_reused"])
        self.assertFalse(type_audit["old_candidate_coefficients_reused"])
        self.assertEqual(type_audit["source_type_verdict"], "REPAIRED")
        self.assertEqual(type_audit["tildeW_variance_verdict"], "REPAIRED")
        self.assertEqual(type_audit["reflected_sign_verdict"], "REPAIRED")
        self.assertIn("PROJECTED_TYPES_REPAIRED", payload["result"])
        self.assertNotIn("MUST_BE_REGENERATED", payload["result"])

    def test_block_path_census_is_fail_closed(self) -> None:
        payload = build_payload()
        paths = payload["block_path_census"]
        self.assertEqual(len(paths), 294)
        survivors = [
            row for row in paths if row["bare_status"] == "SURVIVING_BARE_PROJECT_PATH"
        ]
        self.assertEqual(len(survivors), 4)
        self.assertTrue(
            all(row["node_blocks"] == ["V"] * len(row["node_blocks"]) for row in survivors)
        )
        self.assertTrue(
            any(
                row["source_completed_status"] == "BLOCKED_MISSING_PROJECT_BLOCK"
                for row in paths
            )
        )

    def test_no_pole_or_anomaly_coefficient_is_accepted(self) -> None:
        payload = build_payload()
        boundary = payload["acceptance_boundary"]
        self.assertFalse(boundary["aggregate_contact_pole_accepted"])
        self.assertFalse(boundary["triangle_pole_accepted"])
        self.assertFalse(boundary["anomaly_coefficient_accepted"])
        self.assertTrue(
            all(
                "BLOCKED" in graph["metadata"]["coefficient_status"]
                for graph in payload["physical_family_graphir"]
            )
        )

    def test_artifacts_are_byte_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_generated = GENERATED.read_bytes()
        first_audit = AUDIT_JSON.read_bytes()
        first_markdown = AUDIT_MD.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_generated, GENERATED.read_bytes())
        self.assertEqual(first_audit, AUDIT_JSON.read_bytes())
        self.assertEqual(first_markdown, AUDIT_MD.read_bytes())

        payload = json.loads(first_generated)
        audit = json.loads(first_audit)
        self.assertTrue(payload["status"].startswith("PASS_CENSUS"))
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(audit["totals"]["source_branches"], 784)
        self.assertEqual(audit["totals"]["action_hessian_branches"], 186)
        self.assertEqual(audit["totals"]["block_paths"], 294)
        self.assertEqual(audit["totals"]["family_graphir"], 7)
        self.assertEqual(
            audit["generated_sha256"],
            hashlib.sha256(first_generated).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
