from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_global_81_ht_symbolic_roundtrip_exact_audit.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "step5_global_81_ht_symbolic_roundtrip_exact_audit", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class Step5Global81HTSymbolicRoundtripExactTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = load_module()
        cls.payload = cls.audit.build_payload()

    def test_project_is_sealed_before_ht_read(self) -> None:
        payload = self.payload
        self.assertFalse(payload["scope"]["external_target_used_in_derivation"])
        self.assertEqual(payload["read_order"][3], "4_SHA256_SEAL_PROJECT_PAYLOAD")
        self.assertEqual(payload["read_order"][4], "5_READ_HT_AUDIT_WITH_PROJECT_SEAL_CAPABILITY")
        project_hash = payload["project_seal"]["semantic_sha256"]
        self.assertEqual(len(project_hash), 64)
        self.assertEqual(payload["ht_check"]["read_after_project_semantic_sha256"], project_hash)
        self.assertEqual(
            hashlib.sha256((ROOT / payload["project_seal"]["source"]).read_bytes()).hexdigest(),
            payload["project_seal"]["source_sha256"],
        )

    def test_all_81_direct_coefficients_and_output_words_equal(self) -> None:
        physical = self.payload["physical_81_roundtrip"]
        self.assertEqual(physical["pair_count"], 81)
        self.assertEqual(physical["direct_row_matches"], 81)
        self.assertEqual(physical["direct_row_mismatches"], [])
        self.assertEqual((physical["nonzero_rows"], physical["zero_rows"]), (29, 52))
        for row in physical["rows"]:
            self.assertTrue(row["exact_three_way_equal"], row["id"])
            self.assertEqual(row["project_terms"], row["ht_independent_terms"], row["id"])
            self.assertEqual(row["project_terms"], row["ht_translated_terms"], row["id"])
            self.assertEqual(
                len(row["project_source_basis"]),
                len(row["project_source_coefficients_over_lambda1"]),
                row["id"],
            )

        by_id = {row["id"]: row for row in physical["rows"]}
        self.assertEqual(
            [term["coefficient"]["text"] for term in by_id["A__B_1"]["project_terms"]],
            ["1", "-i*sqrt(2)", "i*sqrt(2)", "1"],
        )
        self.assertEqual(
            [
                (term["left_output"], term["right_output"])
                for term in by_id["A__B_1"]["project_terms"]
            ],
            [("B_1", "D"), ("C_2", "C_3"), ("C_3", "C_2"), ("D", "B_1")],
        )

    def test_finite_rectangle_and_symbolic_all_mn_identity(self) -> None:
        kernel = self.payload["arbitrary_jet_kernel"]
        finite = kernel["finite_rectangle"]
        self.assertEqual((finite["max_m"], finite["max_n"]), (8, 8))
        self.assertEqual(finite["mn_points"], 81)
        self.assertEqual(finite["coefficient_checks"], 2025)
        self.assertEqual(finite["mismatches"], 0)
        counted = 0
        for row in finite["rows"]:
            m, n = row["m"], row["n"]
            self.assertEqual(row["term_count"], (m + 1) * (n + 1))
            for k, ell, p_num, p_den, c_num, c_den in row["terms"]:
                printed = Fraction(p_num, p_den)
                corrected = Fraction(c_num, c_den)
                self.assertEqual(corrected, 2 * printed)
                self.assertEqual(corrected, self.audit.kernel_fraction(m, n, k, ell, 2))
                counted += 1
        self.assertEqual(counted, 2025)
        self.assertTrue(kernel["all_81_lift_corollary"]["all_nonnegative_m_n"])
        self.assertEqual(kernel["all_81_lift_corollary"]["base_output_words"], 70)
        self.assertEqual(
            kernel["all_81_lift_corollary"]["finite_rectangle_lifted_coefficient_checks"],
            70 * 2025,
        )

    def test_intrinsic_ad_da_distributions(self) -> None:
        intrinsic = self.payload["intrinsic_AD_DA"]
        self.assertEqual(intrinsic["mismatches"], 0)
        self.assertEqual(intrinsic["row_count"], 4)
        by_id = {row["id"]: row for row in intrinsic["rows"]}
        self.assertEqual(
            [term["coefficient"]["text"] for term in by_id["A__D_dot1"]["terms"]],
            ["2/3", "1/3"],
        )
        self.assertEqual(
            [term["coefficient"]["text"] for term in by_id["D_dot1__A"]["terms"]],
            ["1/3", "2/3"],
        )
        self.assertEqual(
            [term["coefficient"]["text"] for term in by_id["A__D_dot2"]["terms"]],
            ["2/3", "1/3"],
        )
        self.assertEqual(
            [term["coefficient"]["text"] for term in by_id["D_dot2__A"]["terms"]],
            ["1/3", "2/3"],
        )

    def test_artifacts_are_exact_readback(self) -> None:
        json_path = ROOT / "audits/step5_global_81_ht_symbolic_roundtrip_exact.json"
        md_path = ROOT / "audits/step5_global_81_ht_symbolic_roundtrip_exact.md"
        self.assertEqual(json_path.read_text(encoding="utf-8"), self.audit.render_json(self.payload))
        self.assertEqual(md_path.read_text(encoding="utf-8"), self.audit.render_markdown(self.payload))
        self.assertEqual(json.loads(json_path.read_text(encoding="utf-8")), self.payload)


if __name__ == "__main__":
    unittest.main()
