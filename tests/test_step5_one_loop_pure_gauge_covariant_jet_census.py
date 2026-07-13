from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/step5_one_loop_pure_gauge_covariant_jet_census.py"
SPEC = importlib.util.spec_from_file_location("step5_pure_gauge_jet", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PureGaugeCovariantJetCensusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.audit = MODULE.build_audit(cls.payload)
        cls.rows = MODULE.enumerate_jets()

    def test_diophantine_census_is_complete(self) -> None:
        self.assertEqual(len(self.rows), 18)
        self.assertEqual(
            {
                degree: sum(row.field_strength_degree == degree for row in self.rows)
                for degree in range(4)
            },
            {0: 5, 1: 7, 2: 5, 3: 1},
        )

    def test_every_row_has_locked_quantum_numbers(self) -> None:
        for row in self.rows:
            self.assertEqual(row.dimension_twice, 9)
            self.assertEqual(row.r_charge, -1)
            self.assertEqual(row.parity, 1)

    def test_N_ge_four_is_dimensionally_impossible(self) -> None:
        self.assertGreater(3 * 4, MODULE.TARGET_DIMENSION_TWICE)

    def test_N3_is_unique_and_has_no_target_spin(self) -> None:
        rows = [row for row in self.rows if row.field_strength_degree == 3]
        self.assertEqual(len(rows), 1)
        self.assertEqual((rows[0].n_w, rows[0].n_wtilde), (1, 2))
        self.assertEqual(rows[0].target_spin_multiplicity_free_ordered, 0)

    def test_N2_multisets_and_raw_spin_multiplicities(self) -> None:
        actual = {
            (row.n_w, row.n_wtilde, row.n_nabla, row.n_barnabla, row.n_vector): row.target_spin_multiplicity_free_ordered
            for row in self.rows
            if row.field_strength_degree == 2
        }
        self.assertEqual(
            actual,
            {
                (2, 0, 3, 0, 0): 4,
                (1, 1, 2, 1, 0): 1,
                (1, 1, 1, 0, 1): 1,
                (0, 2, 1, 2, 0): 0,
                (0, 2, 0, 1, 1): 0,
            },
        )

    def test_candidate_spin_multiplicity_is_one(self) -> None:
        self.assertEqual(MODULE.su2_tensor_multiplicities([1, 1, 1]), {1: 2, 3: 1})
        self.assertEqual(MODULE.su2_tensor_multiplicities([1, 1]), {0: 1, 2: 1})
        self.assertEqual(MODULE.target_spin_multiplicity(1, 1, 1, 0, 1), 1)

    def test_chiral_mixed_word_reduction(self) -> None:
        self.assertEqual(
            MODULE._reduce_chiral_word(("B:dot", "N:a", "N:b")),
            {
                ("D:a,dot", "N:b"): -2,
                ("N:a", "D:b,dot"): 2,
            },
        )
        self.assertEqual(MODULE._reduce_chiral_word(("N:a", "N:b", "B:dot")), {})

    def test_antichiral_mixed_word_reduction(self) -> None:
        self.assertEqual(
            MODULE._reduce_antichiral_word(("N:a", "N:b", "B:dot")),
            {("N:a", "D:b,dot"): -2},
        )
        self.assertEqual(MODULE._reduce_antichiral_word(("B:dot", "N:a", "N:b")), {})

    def test_pigeonhole_covers_all_labeled_distributions(self) -> None:
        rows = MODULE.eom_pigeonhole_rows()
        self.assertEqual(len(rows), 8)
        self.assertEqual({tuple(row["assignment"]) for row in rows}, set(__import__("itertools").product((1, 2), repeat=3)))
        self.assertTrue(all(row["local_differential_E_ideal_membership"] for row in rows))
        self.assertTrue(all(not row["full_ordered_product_coefficient_certified"] for row in rows))

    def test_fail_closed_gates_remain_explicit(self) -> None:
        self.assertFalse(self.payload["rank_statement"]["conditional_rank_one_theorem_certified"])
        self.assertFalse(self.payload["rank_statement"]["full_local_cohomology_rank_one_certified"])
        self.assertFalse(self.payload["r_grading"]["project_U1R_binding_certified"])
        self.assertEqual(
            set(self.payload["open_gates"]),
            {
                "DERIVATIVE_PLACEMENT_AND_GRADED_LEIBNIZ",
                "COVARIANT_IBP_WITH_OPERATOR_ORDER",
                "DERIVATIVE_COMMUTATOR_CURVATURE_CHILDREN",
                "ORDERED_ADJ_AB_COLOR_RELATIONS",
                "DRED_EVANESCENT_OPERATORS",
                "SOURCE_PARTNER_AND_BRST_RELATIONS",
                "PROJECT_R_WEIGHT_BINDING",
            },
        )

    def test_generated_artifacts_match_builder(self) -> None:
        on_disk_payload = json.loads(MODULE.OUT.read_text())
        on_disk_audit = json.loads(MODULE.AUDIT.read_text())
        self.assertEqual(on_disk_payload, self.payload)
        self.assertEqual(on_disk_audit, self.audit)
        self.assertTrue(on_disk_audit["all_passed"])
        self.assertEqual((on_disk_audit["passed"], on_disk_audit["total"]), (11, 11))


if __name__ == "__main__":
    unittest.main()
