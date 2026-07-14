from __future__ import annotations

from copy import deepcopy
import json
import unittest

from scripts import step6_verified_foundations_partial as partial


class Step6VerifiedFoundationsPartialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.markdown, cls.audit = partial.generate(write=True)

    def test_exact_bounded_snapshot(self) -> None:
        snapshot = partial.validate_sources(partial.load_sources())
        self.assertEqual(snapshot["document_status"], "UNMERGED_PROPOSAL")
        self.assertEqual(len(snapshot["valence_families"]), 12)
        self.assertEqual(len(snapshot["six_parent"]["classes"]), 6)
        self.assertEqual(
            snapshot["union"]["counts"]["structurally_compiled_parent_count"], 3
        )
        self.assertEqual(snapshot["union"]["counts"]["fail_closed_parent_count"], 3)
        self.assertEqual(snapshot["restricted_three"]["completed_sectors"], 40)
        self.assertEqual(snapshot["restricted_three"]["input_sparse_rows"], 351_069)
        self.assertEqual(snapshot["restricted_three"]["output_sparse_rows"], 55_518)
        self.assertEqual(snapshot["restricted_three"]["output_terms"], 350_945)
        self.assertFalse(
            snapshot["restricted_three"]["global_DAG_registry_constructed"]
        )
        self.assertFalse(snapshot["restricted_three"]["semantic_expansion_performed"])
        self.assertFalse(
            snapshot["restricted_three"]["can_imply_full_K4_minus_e_result"]
        )
        self.assertFalse(snapshot["restricted_three"]["can_imply_Q2_bb"])
        self.assertEqual(snapshot["overall_k"]["counts"]["epsilon_minus_1_log"], 0)
        self.assertEqual(
            snapshot["six_parent"]["full_boundaries"][
                "pure_vector_reduced_gate_graph_count"
            ],
            273,
        )
        self.assertEqual(snapshot["physical_sd"]["resolved_columns"], 0)
        self.assertEqual(snapshot["odd_word_sign"]["exhaustive_cases"], 10_922)
        self.assertEqual(snapshot["odd_word_sign"]["boundary_payload_cases"], 34)
        self.assertEqual(snapshot["contact_provenance"]["stored_contacts"], 608)
        self.assertEqual(
            snapshot["contact_provenance"][
                "legacy_catalog_rows_with_embedded_pre_distribution_provenance"
            ],
            0,
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["resolved_type"],
            "MeasureTaggedDeltaConvolutionReplayUnderSharedPrimitiveDAlgebraOracle",
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["replay_role"],
            "NON_INDEPENDENT_SHARED_ORACLE_RECONSTRUCTION",
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["independent_remainder_object_equality"],
            "OPEN",
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["next_missing_type"],
            "EdgeTaggedContactIBPToALocalSurvivors",
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["counts"],
            partial.EXPECTED_MEASURE_DELTA_REPLAY_COUNTS,
        )
        self.assertEqual(
            snapshot["measure_delta_replay"]["hashes"],
            partial.EXPECTED_MEASURE_DELTA_REPLAY_HASHES,
        )
        self.assertEqual(snapshot["laurent"]["AWI_coefficient"], "UNCOMPUTED")

    def test_formula_first_markdown_contains_exact_boundaries(self) -> None:
        self.assertIn("n_I+\\sum_{r\\geq3}rn_r=2N_{\\mathrm{int}}+E", self.markdown)
        self.assertIn("L=N_{\\mathrm{int}}-V+1=2", self.markdown)
        self.assertIn("(n_I-2)+\\sum_{r\\geq3}(r-2)n_r=4", self.markdown)
        for family in partial.ANALYTIC_VALENCE_FAMILIES:
            self.assertIn(family, self.markdown)
        self.assertNotIn("\\mathfrak G(F)=\\varnothing", self.markdown)
        self.assertIn(
            "\\left(-1,-1,-\\frac12,-1,-\\frac12,-\\frac12\\right)", self.markdown
        )
        self.assertIn("N_{\\mathrm{structural}}=3", self.markdown)
        self.assertIn("N_{\\mathrm{fail\\mbox{-}closed}}=3", self.markdown)
        self.assertIn("\\frac{40}{40}", self.markdown)
        self.assertIn("351\\,069", self.markdown)
        self.assertIn("55\\,518", self.markdown)
        self.assertIn("350\\,945", self.markdown)
        self.assertIn("GlobalDAGRegistryConstructed", self.markdown)
        self.assertIn("PolyExteriorSemanticExpansion", self.markdown)
        self.assertIn("[K R'(G_{B_2})\\right]_{\\epsilon^{-1}L_P}=0", self.markdown)
        self.assertIn(
            "MeasureTaggedDeltaConvolutionReplayUnderSharedPrimitiveDAlgebraOracle",
            self.markdown,
        )
        self.assertIn("PreAggregationRawReplaySeedWithBareDeltaIdentity", self.markdown)
        self.assertIn("PASS\\_TYPED\\_REPLAY", self.markdown)
        self.assertIn("SHARED\\_PRIMITIVE\\_D\\mbox{-}ALGEBRA\\_ORACLE", self.markdown)
        self.assertIn("IndependentRemainderObjectEquality", self.markdown)
        self.assertIn("PREAGGREGATION\\_MEASURE\\_DELTA\\_REPLAY\\_ONLY", self.markdown)
        self.assertIn("StandaloneReplayCertificate", self.markdown)
        self.assertIn(
            "N_{\\mathrm{measure\\mbox{-}pair\\ histories}}=13\\,824", self.markdown
        )
        self.assertIn("N_{\\mathrm{normal\\ contributions}}=13\\,568", self.markdown)
        self.assertIn("N_{\\mathrm{nilpotent\\ zeros}}=36\\,096", self.markdown)
        self.assertIn(
            "N_{\\mathrm{sparse\\ parent\\ incidence}}=6\\,080", self.markdown
        )
        self.assertIn("EdgeTaggedContactIBPToALocalSurvivors", self.markdown)
        self.assertIn("OPEN: MISSING\\_TYPE", self.markdown)
        self.assertNotIn(
            "DeferredMeasureDeltaDWordExecutionToALocalContact", self.markdown
        )
        self.assertIn("N_{\\mathrm{stored\\ contacts}}=608", self.markdown)
        self.assertIn(
            "N_{\\mathrm{legacy\\ catalog\\ rows\\ with\\ embedded\\ provenance}}=0",
            self.markdown,
        )
        self.assertIn(
            "\\mathrm{ParentIncidence}_{768\\to(608+1\\,568)}",
            self.markdown,
        )
        self.assertIn("PASS\\_COMPUTED\\_OBJECT\\_RECONSTRUCTION", self.markdown)
        self.assertNotIn(
            "MeasureTaggedDeltaConvolutionBeforeContactAggregation}}\n=\\texttt{{OPEN",
            self.markdown,
        )
        self.assertNotIn("PASS\\_EXACT\\_PREAGGREGATION\\_REPLAY", self.markdown)
        self.assertNotIn("PASS\\_EXACT\\_PARENT\\_INCIDENCE", self.markdown)
        self.assertNotIn("ProvenanceMap}_{768\\to608}", self.markdown)
        for value in partial.EXPECTED_MEASURE_DELTA_REPLAY_HASHES.values():
            if value in {
                partial.EXPECTED_MEASURE_DELTA_REPLAY_HASHES["contact_catalog_sha256"],
                partial.EXPECTED_MEASURE_DELTA_REPLAY_HASHES[
                    "remainder_catalog_sha256"
                ],
            }:
                self.assertIn(value, self.markdown)
        self.assertIn(
            "N=m+\\binom{m}{2}+m|F|+N_{\\mathrm{coeff}}+N_{\\mathrm{endpoint}}",
            self.markdown,
        )
        self.assertIn("s=(-1)^N", self.markdown)
        self.assertIn("N_{\\mathrm{exhaustive}}=10\\,922", self.markdown)
        self.assertIn("N_{\\mathrm{boundary}}=2(17)=34", self.markdown)
        self.assertTrue(
            all(
                "$" not in line
                for line in self.markdown.splitlines()
                if line.startswith("#")
            )
        )
        self.assertIn("reference\\mbox{-}flat\\ fixed\\ gauge", self.markdown)
        self.assertIn("FROZEN\\_FULL\\_ORBIT\\_AUDIT", self.markdown)
        self.assertIn("C_{\\mathrm{AWI}}^{(2)}=\\texttt{UNCOMPUTED}", self.markdown)
        self.assertNotIn("GPT", self.markdown)
        self.assertNotIn("arXiv", self.markdown)

    def test_audit_is_self_consistent_and_written_exactly(self) -> None:
        output_path = partial.ROOT / partial.OUTPUT
        audit_path = partial.ROOT / partial.AUDIT
        self.assertEqual(output_path.read_text(encoding="utf-8"), self.markdown)
        readback = json.loads(audit_path.read_text(encoding="utf-8"))
        self.assertEqual(readback, self.audit)
        self.assertEqual(readback["status"], "PASS")
        self.assertEqual(readback["failed"], 0)
        self.assertTrue(all(readback["checks"].values()))
        unhashed = dict(readback)
        audit_hash = unhashed.pop("audit_sha256")
        self.assertEqual(audit_hash, partial.payload_sha256(unhashed))

    def test_source_status_drift_fails_closed(self) -> None:
        sources = deepcopy(partial.load_sources())
        sources["measure"]["status"] = "DRIFTED"
        with self.assertRaisesRegex(partial.SourceDriftError, "measure status"):
            partial.validate_sources(sources)

    def test_source_count_drift_fails_closed(self) -> None:
        sources = deepcopy(partial.load_sources())
        sources["six_parent"]["full_boundaries"][
            "pure_vector_reduced_gate_graph_count"
        ] = 272
        with self.assertRaisesRegex(partial.SourceDriftError, "full gate counts"):
            partial.validate_sources(sources)

    def test_measure_replay_hash_drift_fails_closed(self) -> None:
        sources = deepcopy(partial.load_sources())
        sources["measure_delta_replay"]["contact_catalog_sha256"] = "0" * 64
        with self.assertRaisesRegex(
            partial.SourceDriftError, "measure-delta contact_catalog_sha256"
        ):
            partial.validate_sources(sources)


if __name__ == "__main__":
    unittest.main()
