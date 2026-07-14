from __future__ import annotations

from copy import deepcopy
import subprocess
import unittest

from scripts import step6_independent_remainder_object_comparator as module


class Step6IndependentRemainderObjectComparatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.build_payload()

    def test_all_exact_checks(self) -> None:
        self.assertTrue(all(module.exact_checks(self.payload).values()))

    def test_1568_objectwise_equalities(self) -> None:
        comparison = self.payload["objectwise_comparison"]
        self.assertEqual(comparison["left_count"], 1568)
        self.assertEqual(comparison["right_count"], 1568)
        self.assertTrue(comparison["key_sets_equal"])
        self.assertTrue(comparison["all_polynomials_equal"])
        self.assertTrue(comparison["all_incidence_multiplicities_exact"])
        self.assertTrue(comparison["all_parent_incidence_equal"])

    def test_forbidden_left_imports_absent(self) -> None:
        self.assertTrue(module.exact_checks(self.payload)["clean_left_import_boundary"])

    def test_exact_input_hash_closure(self) -> None:
        checks = module.exact_checks(self.payload)
        self.assertTrue(checks["frozen_seed_exact"])
        self.assertTrue(checks["committed_gate_source_exact"])
        self.assertTrue(checks["replay_source_exact"])
        self.assertTrue(checks["replay_payload_exact"])
        self.assertTrue(checks["replay_dependency_manifest_exact"])
        self.assertTrue(checks["replay_internal_checks_pass"])

    def test_runtime_dependency_paths_are_tracked(self) -> None:
        paths = self.payload["replay_runtime_closure"]["dependency_paths"]
        self.assertTrue(all((module.ROOT / path).is_file() for path in paths))
        if (module.ROOT / ".git").exists():
            completed = subprocess.run(
                ["git", "ls-files", "--error-unmatch", *paths],
                cwd=module.ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_replay_dependency_manifest_corruption_fails(self) -> None:
        corrupted = deepcopy(self.payload)
        corrupted["replay_runtime_closure"]["dependency_manifest_sha256"] = "0" * 64
        self.assertFalse(
            module.exact_checks(corrupted)["replay_dependency_manifest_exact"]
        )

    def test_polynomial_corruption_fails(self) -> None:
        left = module._independent_objects()
        right = deepcopy(module._replay_objects())
        key = sorted(right)[0]
        right[key]["exact_polynomial"][0]["coefficient"]["re"] = "999"
        self.assertFalse(module.compare_maps(left, right)["all_polynomials_equal"])

    def test_parent_incidence_corruption_fails(self) -> None:
        left = module._independent_objects()
        right = deepcopy(module._replay_objects())
        key = next(key for key in sorted(right) if right[key]["parent_incidence"])
        right[key]["parent_incidence"][0]["parent_pair_id"] = "CORRUPTED"
        self.assertFalse(module.compare_maps(left, right)["all_parent_incidence_equal"])

    def test_duplicate_parent_incidence_corruption_fails(self) -> None:
        left = module._independent_objects()
        right = deepcopy(module._replay_objects())
        key = next(key for key in sorted(right) if right[key]["parent_incidence"])
        right[key]["parent_incidence"].append(
            deepcopy(right[key]["parent_incidence"][0])
        )
        comparison = module.compare_maps(left, right)
        self.assertFalse(comparison["all_incidence_multiplicities_exact"])
        self.assertFalse(comparison["all_parent_incidence_equal"])

    def test_write_outputs(self) -> None:
        module.write_outputs(self.payload)
        self.assertTrue(module.GENERATED.is_file())
        self.assertTrue(module.AUDIT.is_file())


if __name__ == "__main__":
    unittest.main()
