from __future__ import annotations

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import unittest

from scripts import step6_coefficient_tensor as coefficient
from scripts import step6_full_supertensor as full
from scripts import step6_global_supertensor as global_tensor
from scripts import step6_two_loop_amplitude_ir as amplitude


ROOT = Path(__file__).resolve().parents[1]


class Step6FullSupertensorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = coefficient.build_bundle()
        _, parents = amplitude.build_payload()
        cls.parent = next(
            row
            for row in parents
            if row.graph["graph_id"] == full.GRAPH_ID
            and row.orientation == "direct"
        )

    def test_generic_I2_translation_equals_direct_option_evaluation(self) -> None:
        programs = global_tensor.option_program_index(self.bundle)
        terms = self.bundle["tensor_programs"]["compiled_terms"]
        option = self.parent.local_options["I"][0]
        program = programs[option["local_amplitude_option_id"]]
        term = terms[program["term_id"]]
        generic = full.generic_local_tensor(term, ())
        translated = full.transform_generic_option(
            self.parent, "I", program, generic
        )
        direct = global_tensor.local_sparse_tensor(
            term, program, full.EXTERNAL_SLICE
        )
        self.assertEqual(full.tensor_content_hash(translated), full.tensor_content_hash(direct))
        self.assertEqual(set(translated), set(direct))

    def test_option_dependent_local_sign_composes_with_common_sign(self) -> None:
        fixture = full.port_permutation_fixture(self.parent, self.bundle)
        self.assertEqual(
            fixture["unique_local_word_patterns"],
            {"I": 2, "A": 6, "B": 6, "C": 24},
        )
        self.assertEqual(fixture["checked_pattern_parity_cases"], 55296)
        self.assertTrue(
            fixture[
                "actual_to_edge_equals_local_to_common_times_common_to_edge"
            ]
        )

    def test_common_sign_polynomial_stages_cover_all_edge_masks(self) -> None:
        record = full.sign_polynomial(self.parent, self.bundle)
        self.assertEqual(record["checked_edge_parity_cases"], 32)
        self.assertEqual(record["all_16_pow_5_mask_assignments_checked"], 16**5)
        self.assertTrue(record["common_word_sign_equals_staged_sign"])

    def test_variable_elimination_equals_one_explicit_sparse_assignment(self) -> None:
        metric_inverse = [
            [Fraction(value) for value in row]
            for row in self.bundle["coefficient_metric"]["M_inverse"]
        ]
        sign_record = full.sign_polynomial(self.parent, self.bundle)
        stages = {
            name: {
                "linear": row["linear"],
                "quadratic": [tuple(pair) for pair in row["quadratic"]],
            }
            for name, row in sign_record["stages"].items()
        }
        masks = dict(zip(full.EDGE_VARIABLES, (1, 3, 4, 6, 7), strict=True))
        insertion = {
            (masks["e_AI"], masks["e_IB"]): coefficient.oracle.Exterior.basis(
                2, coefficient.oracle.Poly.variable("u")
            )
        }
        action_a = {
            (masks["e_AI"], masks["e_CA"], masks["e_BA"]): coefficient.oracle.Poly.variable(
                "a"
            )
        }
        action_b = {
            (masks["e_IB"], masks["e_BC"], masks["e_BA"]): coefficient.oracle.Poly.variable(
                "b"
            )
        }
        action_c = {
            (masks["e_CA"], masks["e_BC"]): coefficient.oracle.Poly.variable(
                "c"
            )
        }
        counts: dict[str, int] = {"IA_multiply_adds": 0, "IAB_multiply_adds": 0, "IABC_multiply_adds": 0}
        ia = full.contract_ia(
            insertion, action_a, metric_inverse, stages["IA"], counts
        )
        iab = full.contract_iab(
            ia, action_b, metric_inverse, stages["IAB"], counts
        )
        eliminated = full.contract_iabc(
            iab, action_c, metric_inverse, stages["IABC"], counts
        )
        scalar = Fraction(1)
        for edge in full.EDGE_VARIABLES:
            scalar *= full.edge_kernel(masks[edge], metric_inverse)
        common_sign = global_tensor.weighted_permutation_sign(
            full.common_global_word(self.parent, self.bundle, masks),
            full.edge_canonical_labels(self.parent),
        )
        explicit = coefficient.oracle.Exterior.basis(
            2,
            coefficient.oracle.Poly.variable("u")
            * coefficient.oracle.Poly.variable("a")
            * coefficient.oracle.Poly.variable("b")
            * coefficient.oracle.Poly.variable("c")
            * scalar
            * common_sign,
        )
        self.assertEqual(eliminated, explicit)
        self.assertEqual(counts, {"IA_multiply_adds": 1, "IAB_multiply_adds": 1, "IABC_multiply_adds": 1})

    def test_generated_full_parent_readback(self) -> None:
        if not full.OUTPUT_JSON.is_file():
            self.skipTest(
                "the exact 4032-tuple artifact has not been generated in this checkout"
            )
        payload = json.loads(full.OUTPUT_JSON.read_text(encoding="utf-8"))
        audit = json.loads(full.AUDIT.read_text(encoding="utf-8"))
        if not payload["contraction"]["complete"]:
            self.skipTest(
                "the exact 4032-tuple artifact is still running; bounded output is not a result"
            )
        self.assertEqual(audit["status"], "PASS")
        self.assertTrue(all(audit["checks"].values()))
        self.assertEqual(payload["scope"]["graph_id"], full.GRAPH_ID)
        self.assertEqual(
            {vertex: len(rows) for vertex, rows in payload["joint_local_color_groups"].items()},
            {"I": 2, "A": 6, "B": 6, "C": 56},
        )
        self.assertEqual(
            payload["contraction"]["expected_joint_group_tuples"], 4032
        )
        self.assertTrue(payload["contraction"]["complete"])
        self.assertEqual(
            payload["contraction"]["contracted_joint_group_tuples"], 4032
        )
        self.assertEqual(
            payload["variable_elimination"]["coefficient_color_marginal_product"],
            "REJECTED",
        )
        self.assertIsNone(
            payload["fail_closed"]["renormalized_two_loop_coefficient"]
        )
        for row in payload["contraction"]["final_canonical_color_coefficients"]:
            artifact = row["coefficient_exterior_polynomial_artifact"]
            compressed = (ROOT / artifact["path"]).read_bytes()
            self.assertEqual(
                hashlib.sha256(compressed).hexdigest(),
                artifact["compressed_sha256"],
            )
            encoded = gzip.decompress(compressed)
            self.assertEqual(
                hashlib.sha256(encoded).hexdigest(),
                artifact["uncompressed_sha256"],
            )
            value = full.deserialize_value(json.loads(encoded))
            self.assertTrue(value)

    def test_firewall_source_contains_no_comparison_identifiers(self) -> None:
        source = (ROOT / "scripts/step6_full_supertensor.py").read_text(encoding="utf-8")
        for token in ("2207.14321", "2306.01039", "EXTERNAL_TARGET_NOT_DERIVATION"):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
