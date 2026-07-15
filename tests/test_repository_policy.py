from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryPolicyTest(unittest.TestCase):
    def test_required_authority_files_exist(self) -> None:
        for relative in (
            "AUTHORITY.md",
            "AGENTS.md",
            "tasks/CURRENT.yaml",
            "contracts/manifest.yaml",
            "mirror/page_map.yaml",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_legacy_directory_or_symlink(self) -> None:
        self.assertFalse((ROOT / "legacy").exists())
        for path in ROOT.rglob("*"):
            if ".git" in path.parts:
                continue
            self.assertFalse(path.is_symlink(), str(path))

    def test_contract_hashes(self) -> None:
        manifest = json.loads((ROOT / "contracts/manifest.yaml").read_text(encoding="utf-8"))
        for entry in manifest["contracts"]:
            path = (ROOT / entry["path"]).resolve()
            path.relative_to(ROOT)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertRegex(entry["sha256"] or "", r"^[0-9a-f]{64}$")
            self.assertEqual(entry["sha256"], digest)

    def test_reference_hashes(self) -> None:
        manifest = json.loads((ROOT / "references/manifest.yaml").read_text(encoding="utf-8"))
        for entry in manifest["entries"]:
            path = (ROOT / entry["path"]).resolve()
            path.relative_to(ROOT)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(entry["sha256"], digest)

    def test_claim_map_resolves_to_hashed_artifacts(self) -> None:
        manifest = json.loads((ROOT / "references/manifest.yaml").read_text(encoding="utf-8"))
        claim_map_path = ROOT / "references/claim-map.yaml"
        if not claim_map_path.exists():
            self.skipTest("no claim map registered")
        claim_map = json.loads(claim_map_path.read_text(encoding="utf-8"))
        artifacts = {entry["id"]: entry for entry in manifest["entries"]}
        for claim in claim_map["claims"]:
            for source_id in claim["sources"]:
                self.assertIn(source_id, artifacts)
                self.assertRegex(artifacts[source_id]["sha256"] or "", r"^[0-9a-f]{64}$")

    def test_weinberg_srednicki_reference_import(self) -> None:
        ledger_path = ROOT / "references/weinberg-srednicki-notation-source-ledger.json"
        if not ledger_path.exists():
            self.skipTest("Weinberg-Srednicki reference import is not registered")
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        pages = ledger["notion_pages"]
        self.assertEqual(ledger["task"], "REFERENCE-IMPORT-WEINBERG-SREDNICKI-NOTATION-001")
        self.assertEqual(ledger["draft"]["role"], "UNVERIFIED_CANDIDATE_DICTIONARY")
        self.assertEqual(ledger["draft"]["byte_fidelity"], "BYTE_FOR_BYTE_COPY_OF_USER_ATTACHMENT")
        self.assertEqual(len(pages), 32)
        self.assertEqual(sum(page["source"] == "WEINBERG" for page in pages), 20)
        self.assertEqual(sum(page["source"] == "SREDNICKI" for page in pages), 12)
        for page in pages:
            self.assertEqual(page["role"], "REFERENCE_EVIDENCE_ONLY")
            self.assertRegex(page["page_id"], r"^[0-9a-f]{32}$")
            self.assertEqual(page["url"], f"https://app.notion.com/p/{page['page_id']}")
            snapshot = ROOT / page["snapshot_path"]
            self.assertTrue(snapshot.is_file(), page["snapshot_path"])
            self.assertEqual(hashlib.sha256(snapshot.read_bytes()).hexdigest(), page["sha256"])

    def test_superspace_1001_gauge_representation_reference_import(self) -> None:
        ledger_path = ROOT / "references/superspace-1001-gauge-representation-source-ledger.json"
        if not ledger_path.exists():
            self.skipTest("Superspace 1001 gauge-representation reference import is not registered")
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(
            ledger["task"],
            "REFERENCE-IMPORT-SUPERSPACE-1001-VECTOR-REPRESENTATION-001",
        )
        source = ledger["source"]
        discovery = ledger["discovery"]
        locator = ledger["locator_index_pass"]
        scoped = ledger["scoped_artifact"]
        self.assertEqual(source["identity_check"], "EXACT_BYTE_IDENTITY")
        self.assertEqual(
            source["local_sha256"],
            source["identical_existing_vendor_artifact"]["sha256"],
        )
        self.assertEqual(scoped["pages"], 14)
        self.assertEqual(discovery["filename_candidate_count"], 5)
        self.assertEqual(discovery["opened_candidate_count"], 1)
        self.assertEqual(discovery["rendered_title_page_exact_match_count"], 1)
        self.assertFalse(locator["temporary_full_text_retained"])
        self.assertEqual(scoped["page_selection"][2]["source_pdf_pages"], "177-180")
        self.assertEqual(scoped["page_selection"][3]["source_pdf_pages"], "182-188")
        self.assertEqual(scoped["page_selection"][4]["source_pdf_pages"], "190")
        artifact = ROOT / scoped["path"]
        self.assertTrue(artifact.is_file())
        self.assertEqual(hashlib.sha256(artifact.read_bytes()).hexdigest(), scoped["sha256"])
        self.assertEqual(ledger["source_scope"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
        visual_checks = ledger["visual_verification"]["manual_visual_checks"]
        self.assertEqual(len(visual_checks), 6)
        self.assertEqual(len({item["subset_page"] for item in visual_checks}), 6)
        self.assertTrue(all({"subset_page", "source_pdf_page", "role"} == set(item) for item in visual_checks))
        self.assertEqual(ledger["visual_verification"]["result"], "PASS")

    def test_superspace_1001_reference_import_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_superspace_1001_reference_import.py"
        audit_path = ROOT / "audits/superspace-1001-reference-import-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Superspace 1001 reference-import verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 47, "failed": 0, "page_text_comparisons": 14})

    def test_n2_su2r_obstruction_note_reference_import(self) -> None:
        ledger_path = ROOT / "references/n2-su2r-obstruction-note-source-ledger.json"
        source_path = ROOT / "references/vendor/local/N2_SYM_offshell_SU2R_obstruction_lecture_note.tex"
        self.assertTrue(ledger_path.is_file())
        self.assertTrue(source_path.is_file())
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(ledger["task"], "REFERENCE-IMPORT-N2-SU2R-OBSTRUCTION-NOTE-001")
        self.assertEqual(ledger["source"]["identity_check"], "EXACT_BYTE_IDENTITY")
        self.assertEqual(
            hashlib.sha256(source_path.read_bytes()).hexdigest(),
            "cc5abc773174305472acfe06b14f3d63229ffcfba9ed70f55ff3d3b534be26e6",
        )
        self.assertEqual(ledger["source_scope"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
        self.assertFalse(ledger["source_scope"]["project_formula_adoption"])
        self.assertFalse(ledger["source_scope"]["notion_read_performed"])
        self.assertTrue(all(not item["imported"] for item in ledger["embedded_external_references"]))

    def test_n2_su2r_obstruction_reference_import_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_n2_su2r_obstruction_reference_import.py"
        audit_path = ROOT / "audits/n2-su2r-obstruction-reference-import-verification.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 37, "failed": 0})

    def test_n2_general_lie_closure_instructor_reference_import(self) -> None:
        ledger_path = ROOT / "references/n2-general-lie-closure-instructor-source-ledger.json"
        source_path = ROOT / "references/vendor/local/N2_SYM_general_Lie_closure_instructor_2026-07-12.md"
        self.assertTrue(ledger_path.is_file())
        self.assertTrue(source_path.is_file())
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(ledger["task"], "REFERENCE-IMPORT-N2-GENERAL-LIE-CLOSURE-INSTRUCTOR-001")
        self.assertEqual(ledger["source"]["identity_check"], "EXACT_BYTE_IDENTITY")
        self.assertEqual(
            hashlib.sha256(source_path.read_bytes()).hexdigest(),
            "392c9e59ee038d7ac19f390acf9f18111f1a1fc880cd7fed9c09a21f42a166ec",
        )
        self.assertEqual(ledger["source_scope"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
        self.assertFalse(ledger["source_scope"]["project_formula_adoption"])
        self.assertFalse(ledger["source_scope"]["notion_read_performed"])
        self.assertEqual(ledger["embedded_external_references"], [])
        self.assertTrue(
            all(item["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT" for item in ledger["candidate_claims"])
        )

    def test_n2_general_lie_closure_instructor_import_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_n2_general_lie_closure_instructor_import.py"
        audit_path = ROOT / "audits/n2-general-lie-closure-instructor-import-verification.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 41, "failed": 0})

    def test_notion_is_output_only(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        self.assertEqual(page_map["direction"], "GIT_TO_NOTION_ONLY")
        self.assertEqual(page_map["notion_content_read_policy"], "FORBIDDEN")
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        self.assertFalse(receipt["content_readback_performed"])

    def test_authority_repair_is_accepted(self) -> None:
        obligations = json.loads((ROOT / "ledger/proof_obligations.json").read_text(encoding="utf-8"))
        quarantine = json.loads((ROOT / "audits/legacy_quarantine.json").read_text(encoding="utf-8"))
        protection = json.loads((ROOT / "audits/branch_protection.json").read_text(encoding="utf-8"))
        authority = next(item for item in obligations["proof_obligations"] if item["id"] == "AUTHORITY-REPAIR-001")
        self.assertEqual(authority["state"], "ACCEPTED")
        self.assertEqual(quarantine["action"], "ARCHIVE_NOT_DELETE")
        self.assertFalse(quarantine["content_imported"])
        self.assertEqual(len(quarantine["repositories"]), 4)
        self.assertTrue(all(item["archived"] for item in quarantine["repositories"]))
        self.assertEqual(protection["blocker"], "BLOCKED_GITHUB_PLAN_BRANCH_PROTECTION")
        self.assertEqual(protection["replacement_gate"], "origin/main commit plus successful verify workflow")

    def test_current_task_is_registered(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        obligations = json.loads((ROOT / "ledger/proof_obligations.json").read_text(encoding="utf-8"))
        ids = {item["id"] for item in obligations["proof_obligations"]}
        self.assertIn(task["id"], ids)
        self.assertIn(task["type"], {"AUTHORITY_REPAIR", "REFERENCE_IMPORT", "CONTRACT_CHANGE"})
        current = [item for item in obligations["proof_obligations"] if item["task"] == "tasks/CURRENT.yaml"]
        self.assertEqual(len(current), 1)
        self.assertEqual(current[0]["id"], task["id"])
        for obligation in obligations["proof_obligations"]:
            packet = json.loads((ROOT / obligation["task"]).read_text(encoding="utf-8"))
            self.assertEqual(packet["id"], obligation["id"])
            if "task_sha256" in obligation:
                digest = hashlib.sha256((ROOT / obligation["task"]).read_bytes()).hexdigest()
                self.assertEqual(digest, obligation["task_sha256"])

    def test_step5_aa_standard_feynman_strictification(self) -> None:
        script = ROOT / "scripts/step5_aa_standard_feynman_strict_audit.py"
        audit = ROOT / "audits/step5-aa-standard-feynman-strictification.md"
        pro_review = ROOT / "proposals/gpt-pro-aa-standard-feynman-2026-07-14.md"
        pro_correction = ROOT / "proposals/gpt-pro-aa-derivation-correction-2026-07-14.md"
        pro_final = ROOT / "proposals/gpt-pro-aa-final-settlement-2026-07-14.md"
        second_mark_sd = ROOT / "audits/step5-aa-matter-second-mark-full-sd-independent.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        self.assertTrue(pro_review.is_file())
        self.assertTrue(pro_correction.is_file())
        self.assertTrue(pro_final.is_file())
        self.assertTrue(second_mark_sd.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["summary"]["status"], "PASS")
        self.assertEqual(result["summary"]["failed"], 0)
        self.assertGreater(result["summary"]["passed"], 200)
        self.assertEqual(
            result["scope"],
            "FULL_AA_ONE_LOOP_ANOMALY_SECTOR_TARGET_BLIND_EXACT",
        )
        self.assertEqual(
            result["summary"]["scope"],
            "FULL_AA_ONE_LOOP_ANOMALY_SECTOR_TARGET_BLIND_EXACT",
        )
        self.assertEqual(
            result["claim_boundary"],
            "AA_SECTOR_ONLY__DOES_NOT_CERTIFY_GLOBAL_81_LEDGER",
        )
        self.assertTrue(result["certifies_full_diagram_derivation"])
        self.assertEqual(
            result["full_diagram_derivation"]["status"],
            "ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH",
        )
        self.assertTrue(
            result["full_diagram_derivation"][
                "pass_from_this_script_implies_completion"
            ]
        )
        self.assertEqual(result["full_diagram_derivation"]["required_blockers"], [])
        checks = {row["id"]: row for row in result["checks"]}
        self.assertEqual(checks["gauge_signed_hessian_propagator_weight"]["status"], "PASS")
        self.assertEqual(checks["gauge_signed_hessian_propagator_weight"]["actual"], "-1/16")
        final_check_ids = {
            "aa_final_external_target_absent_from_derivation",
            "aa_final_exact_artifact_status",
            "aa_final_raw_hessian_group_count",
            "aa_final_raw_hessian_endpoint_row_count",
            "aa_final_raw_contact_multiplicity",
            "aa_final_raw_full_d_edge_cancellations",
            "aa_final_exhaustive_component_replay",
            "aa_final_gauge_ordered_vector",
            "aa_final_matter_ordered_vector",
            "aa_ht_check_only_unique_target_row",
            "aa_ht_check_only_color_tensor_dictionary",
            "aa_ht_check_only_exact_ordered_vector_match",
        }
        self.assertTrue(final_check_ids.issubset(checks))
        self.assertTrue(
            all(
                checks[check_id]["scope"]
                == "FULL_AA_ONE_LOOP_ANOMALY_SECTOR_TARGET_BLIND_EXACT"
                and checks[check_id]["certifies_full_diagram_derivation"]
                and checks[check_id]["status"] == "PASS"
                for check_id in final_check_ids
            )
        )
        conditional_matter_arithmetic_checks = {
            "matter_naive_2x2_bispinor_matrix",
            "matter_naive_2x2_bispinor_determinant",
            "matter_cut_e0_vector_bubble_zero",
            "matter_cut_e1_vector_bubble_zero",
            "matter_cut_seagull_vector_bubble_zero",
            "matter_cut_J_C_vector_bubble_zero",
            "matter_cut_J_B_vector_bubble_zero",
            "matter_rank_two_parent_ell_1_squared_coefficient",
            "matter_rank_two_parent_ell_2_squared_coefficient",
            "matter_rank_two_parent_ell_3_squared_coefficient",
            "matter_rank_two_parent_ell_4_squared_coefficient",
            "matter_rank_two_simplex_projection_factor",
            "matter_rank_two_forward_simplex_ratios",
            "matter_rank_two_reflected_simplex_ratios",
            "matter_rank_two_derived_symmetric_diagonal_weights",
            "matter_rank_two_H_displayed_ratio",
            "matter_rank_two_H_delta4_zero",
            "matter_rank_two_H_locked_trace_constraint",
            "matter_rank_two_H_epsilon_ratio",
            "matter_second_marked_mixed21_det_omega_identity",
            "matter_second_marked_longitudinal_posttransport_identity",
            "matter_second_marked_posttransport_r1_inverse_kernel_coefficient",
            "matter_second_marked_operator_transport_ledger",
            "matter_second_marked_determinant_simplex",
            "matter_second_marked_omega_simplex",
            "matter_second_marked_full_simplex",
            "matter_second_marked_full_lambda1_units_from_simplex",
        }
        self.assertTrue(conditional_matter_arithmetic_checks.issubset(checks))
        self.assertTrue(
            all(checks[check_id]["status"] == "PASS" for check_id in conditional_matter_arithmetic_checks)
        )
        self.assertEqual(checks["matter_first_marked_placement_magnitude_in_lambda1_units"]["actual"], "4/3")
        self.assertEqual(checks["matter_second_marked_placement_in_lambda1_units"]["actual"], "-1/3")
        self.assertEqual(checks["matter_complete_marked_orbit_magnitude_in_lambda1_units"]["actual"], "1")
        self.assertEqual(checks["matter_to_gauge_selected_orbit_magnitude_ratio"]["actual"], "8")
        self.assertEqual(
            result["second_mark_full_sd_artifact"],
            "audits/step5-aa-matter-second-mark-full-sd-independent.md",
        )
        text = audit.read_text(encoding="utf-8")
        missing_derivation_blockers = {
            "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION",
            "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
            "BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE",
            "BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR",
            "BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER",
            "BLOCKED_COMPLETE_AA_GRAPH_CENSUS",
            "AA_MATTER_UNIT_MAGNITUDE_REPRODUCED__GLOBAL_ORIENTATION_SIGN_OPEN",
        }
        self.assertEqual(
            set(
                result["full_diagram_derivation"][
                    "legacy_blockers_superseded_for_AA_sector"
                ]
            ),
            missing_derivation_blockers,
        )
        for blocker in missing_derivation_blockers:
            self.assertIn(blocker, text)
        self.assertIn("CONDITIONAL_DOWNSTREAM_ARITHMETIC_ONLY", text)
        self.assertIn("These are occurrence-resolved $D$-word results, not ansaetze.", text)
        self.assertIn("AA_MATTER_UNIT_MAGNITUDE_REPRODUCED__GLOBAL_ORIENTATION_SIGN_OPEN", text)
        self.assertIn(r"\mathcal S_2", text)
        self.assertIn(r"\Omega_{21}", text)
        self.assertIn(r"\left(z-\frac12\right)", text)
        second_mark_text = second_mark_sd.read_text(encoding="utf-8")
        self.assertIn(
            "SECOND_MARK_FULL_SD_REPAIRED__DISCARDED_LONGITUDINAL_RESIDUAL_WAS_THE_ERROR__TARGET_BLIND_UNIT_MAGNITUDE",
            second_mark_text,
        )
        self.assertIn(r"D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)", second_mark_text)
        self.assertIn("42/42 PASS", second_mark_text)
        self.assertIn(r"N_{\rm parent}-N_{\rm cut}", text)
        self.assertIn("REJECTED_PROPAGATOR_NORMALIZATION", text)
        self.assertIn("REJECTED_BY_EVIDENCE__EXACT_FACTOR_8", text)
        self.assertIn("NON_AUTHORITY_PRO_REVIEW", pro_review.read_text(encoding="utf-8"))
        correction_text = pro_correction.read_text(encoding="utf-8")
        self.assertIn("NON_AUTHORITY_PRO_REVIEW", correction_text)
        self.assertIn("# CORRECTED_G_RESULT", correction_text)
        final_text = pro_final.read_text(encoding="utf-8")
        self.assertIn("NON_AUTHORITY_PRO_REVIEW", final_text)
        self.assertIn("1efd04011130a3f64f4e57e42bc58fc1d0aa576af8bc8e7eb68b7f0eaab1f90b", final_text)
        self.assertIn("BLOCKED_UNREDUCED_Q4S_MATTER_WORD", final_text)
        self.assertIn("BLOCKED_PROJECT_HT_COMPONENT_INTERTWINER", final_text)
        self.assertIn("GRAPH_CENSUS", final_text)
        self.assertIn("FULL_AA_MATCH", final_text)
        acceptance = result["aa_final_acceptance"]
        self.assertEqual(
            acceptance["status"],
            "ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH",
        )
        self.assertFalse(acceptance["global_81_ledger_modified"])
        self.assertEqual(
            acceptance["derived_before_HT"],
            {
                "D>A": "1",
                "A>D": "-1",
                "B_1>C_1": "1",
                "C_1>B_1": "-1",
                "B_2>C_2": "1",
                "C_2>B_2": "-1",
                "B_3>C_3": "1",
                "C_3>B_3": "-1",
            },
        )
        self.assertEqual(
            acceptance["raw_multiplicity_ledger"]["verified_multiplicity"],
            {"m0": "1", "m2": "1"},
        )
        self.assertTrue(acceptance["HT_check_only"]["exact_match"])
        self.assertFalse(
            acceptance["HT_check_only"][
                "target_used_to_determine_coefficient"
            ]
        )
        self.assertEqual(
            acceptance["HT_check_only"]["seal"],
            "AA_HT_CHECK_ONLY_SEAL__DERIVATION_TARGET_BLIND__EXACT_MATCH",
        )
        self.assertIn(
            "ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH",
            text,
        )
        self.assertIn(
            "AA_HT_CHECK_ONLY_SEAL__DERIVATION_TARGET_BLIND__EXACT_MATCH",
            text,
        )
        self.assertIn(r"\boxed{m_0=m_2=1}", text)
        self.assertIn(r"\Gamma_{AA}^{(1)}", text)

    def test_step5_aa_source_sd_orbit_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_source_sd_orbit_exact_audit.py"
        audit = ROOT / "audits/step5-aa-source-expansion-sd-orbit.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 40/40 PASS", completed.stdout)
        text = audit.read_text(encoding="utf-8")
        self.assertIn("RETRACTED_SINGLE_MARKED_PLACEMENT", text)
        self.assertIn("NO_DOUBLE_COUNT_PARENT_MINUS_CUT", text)
        self.assertIn("BLOCKED_AA_GAUGE_FULL_MARKED_OCCURRENCE_RECOUNT", text)
        self.assertIn("BLOCKED_AA_MATTER_PHYSICAL_CUT_ASSIGNMENT", text)
        self.assertIn("CANDIDATE_NOT_ACCEPTED", text)

    def test_step5_aa_matter_full_placements_independent_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_matter_full_placements_independent_audit.py"
        audit = ROOT / "audits/step5-aa-matter-full-placements-independent.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("40/40 PASS", completed.stdout)
        text = audit.read_text(encoding="utf-8")
        self.assertIn(
            "SECOND_MARK_FULL_SD_REPAIRED__FOUR_OCCURRENCES_TARGET_BLIND_UNIT_MAGNITUDE",
            text,
        )
        self.assertIn(r"\mathcal C_0^{\mathrm{raw}}=-1024W_{02}", text)
        self.assertIn(r"\mathcal C_2^{\mathrm{raw}}=+1024W_{02}", text)
        self.assertIn(r"\Delta_2^{\mathrm{full}}", text)
        self.assertIn(r"\left(\frac12-z\right)", text)
        self.assertIn(r"\Omega_{21}", text)

    def test_step5_aa_matter_second_mark_full_sd_independent_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_matter_second_mark_full_sd_independent_audit.py"
        audit = ROOT / "audits/step5-aa-matter-second-mark-full-sd-independent.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn("PASS SECOND_SOURCE_TRANSVERSE_PLUS_LONGITUDINAL", completed.stdout)
        self.assertIn("PASS LONGITUDINAL_ENDPOINT_ORDER_REVERSAL", completed.stdout)
        self.assertIn("PASS POST_TRANSPORT_R1_D2_BARD2_D2_COLLAPSE", completed.stdout)
        self.assertIn("PASS DRED_FULL_S2_DEFECT", completed.stdout)
        self.assertIn("PASS SECOND_MARKED_LAMBDA_UNITS", completed.stdout)
        self.assertIn("42/42 PASS", completed.stdout)
        text = audit.read_text(encoding="utf-8")
        self.assertIn(r"\Omega_{21}", text)
        self.assertIn(r"\mathcal R_2^{\mathrm{full}}", text)
        self.assertIn(r"-\frac13\lambda_1", text)

    def test_step5_aa_gauge_marked_occurrence_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_gauge_marked_occurrence_exact_audit.py"
        audit = ROOT / "audits/step5-aa-gauge-marked-occurrence-recount.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 23/23 PASS", completed.stdout)
        text = audit.read_text(encoding="utf-8")
        self.assertIn("NO_RANK_TWO_DRED_DEFECT", text)
        self.assertIn("NO_EXTRA_POLARIZATION_MULTIPLICITY", text)
        self.assertIn(r"-\frac{\lambda_1}{8}", text)

    def test_step5_aa_gauge_canonical_normalization_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_gauge_canonical_normalization_audit.py"
        audit = ROOT / "audits/step5-aa-gauge-canonical-normalization-ledger.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 42/42 PASS", completed.stdout)
        text = audit.read_text(encoding="utf-8")
        self.assertIn("AA_GAUGE_CANONICAL_NORMALIZATION_REDERIVED_TARGET_BLIND", text)
        self.assertIn(r"-4(\bar L^2-L_d^2)", text)
        self.assertIn(r"2^3=8", text)

    def test_step5_aa_gauge_full_source_sd_orbit_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_gauge_full_source_sd_orbit_exact_audit.py"
        audit = ROOT / "audits/step5-aa-gauge-full-source-sd-orbit-exact.md"
        artifact_path = ROOT / "audits/step5-aa-gauge-full-source-sd-orbit-exact.json"
        for path in (script, audit, artifact_path):
            self.assertTrue(path.is_file(), path)
        completed = subprocess.run(
            [sys.executable, str(script), "--check-artifact", str(artifact_path)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 24/24 PASS", completed.stdout)
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(artifact["route_coverage"]["AA_directed_parents"], 42)
        self.assertEqual(artifact["route_coverage"]["AA_gauge_gauge_routes"], 36)
        self.assertEqual(
            artifact["I1_Sg3_bubbles"]["attachment_quadratic_numerator_sum"],
            "0",
        )
        self.assertEqual(
            artifact["I1_Sg3_bubbles"]["source_A_four_dimensional_trace"]["text"],
            "0",
        )
        self.assertEqual(
            artifact["I1_Sg3_bubbles"]["source_D_four_dimensional_trace"]["text"],
            "0",
        )
        self.assertEqual(artifact["I0_Sg4_bubble"]["four_dimensional_trace"]["text"], "0")
        self.assertEqual(artifact["full_gauge_source_orbit"]["coefficient_in_lambda1_units"], "-1/8")
        text = audit.read_text(encoding="utf-8")
        self.assertIn("GAUGE_SOURCE_ORBIT_ZERO", text)
        self.assertIn(r"H_{A|D}+H_{D|A}=0", text)
        self.assertIn(r"C_{AA,\mathrm{gauge}}^{\mathrm{full}}", text)

    def test_step5_aa_gauge_bc_current_orbit_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_aa_gauge_bc_current_orbit_exact_audit.py"
        audit = ROOT / "audits/step5-aa-gauge-bc-current-orbit-exact.md"
        artifact_path = ROOT / "audits/step5-aa-gauge-bc-current-orbit-exact.json"
        for path in (script, audit, artifact_path):
            self.assertTrue(path.is_file(), path)
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 12/12 PASS", completed.stdout)
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(artifact["pointwise_sum"], "0")
        self.assertEqual(artifact["anomaly_coefficient_in_lambda1_units"], "0")
        self.assertFalse(artifact["omega21_boundary"]["included_here"])
        text = audit.read_text(encoding="utf-8")
        self.assertIn("NO_MINUS_ONE_THIRD_FROM_GAUGE_BC_CURRENT", text)
        self.assertIn(r"\delta^2S_{\mathrm{gf}}", text)
        self.assertIn(r"2i-2i", text)

    def test_step5_ad_da_gauge_family_raw_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_ad_da_gauge_family_raw_audit.py"
        audit = ROOT / "audits/step5-ad-da-gauge-family-raw-exact.md"
        artifact = ROOT / "audits/step5-ad-da-gauge-family-raw-exact.json"
        for path in (script, audit, artifact):
            self.assertTrue(path.is_file(), path)
        completed = subprocess.run(
            [sys.executable, str(script), "--check", "--workers", "8"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=240,
        )
        self.assertIn("SUMMARY 9/9 PASS", completed.stdout)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertFalse(payload["external_target_used"])
        self.assertFalse(payload["full_pair_result_claimed"])
        self.assertTrue(payload["conditional_ff_anomaly_sector_claimed"])
        self.assertEqual(
            payload["route_counts"],
            {
                "amputated_1PI_legacy": {
                    "A__Ddot1": 42,
                    "Ddot1__A": 42,
                },
                "connected_1PR_spectator": {
                    "A__Ddot1": 42,
                    "Ddot1__A": 42,
                },
                "connected_total": {
                    "A__Ddot1": 84,
                    "Ddot1__A": 84,
                },
            },
        )
        self.assertEqual(
            payload["topology_counts"],
            {
                "A__Ddot1": {"TGG": 36, "TMM": 6},
                "Ddot1__A": {"TGG": 36, "TMM": 6},
            },
        )
        for pair in ("A__Ddot1", "Ddot1__A", "A__Ddot2", "Ddot2__A"):
            self.assertEqual(len(payload["pairs"][pair]), 42)
        self.assertEqual(
            payload["aggregates"]["A__Ddot1"]["loop_routing_distribution"],
            {
                "derivation": "ell -> -(2*p+q)/3 from the exact rank-one triangle simplex moment",
                "p": "2/3",
                "q": "1/3",
            },
        )
        self.assertEqual(
            payload["aggregates"]["Ddot1__A"]["loop_routing_distribution"]["p"],
            "2/3",
        )
        self.assertEqual(
            payload["aggregates"]["Ddot1__A"]["loop_routing_distribution"]["q"],
            "1/3",
        )
        self.assertEqual(
            payload["target_blind_ordered_external_vector"]["AD_shape"],
            {"k_left": "1/3", "k_right": "2/3"},
        )
        self.assertEqual(
            payload["target_blind_ordered_external_vector"]["DA_shape"],
            {"k_left": "2/3", "k_right": "1/3"},
        )
        self.assertEqual(len(payload["conditional_ff_occurrence_census"]), 15)
        fp = next(
            row
            for row in payload["conditional_ff_occurrence_census"]
            if row["id"] == "ADDA-O09-FP-EULER-BUBBLE"
        )
        self.assertTrue(fp["DD_reachable"])
        self.assertEqual(fp["loop_number"], 1)
        self.assertEqual(fp["status"], "EVALUATED_NONZERO_EULER_BUBBLE__FULL_D_CUT_REQUIRED")
        self.assertTrue(
            payload["gauge_fixing_ghost_nk"]["fp_full_schwinger_family_zero"]
        )
        self.assertIn(
            "BLOCKED_AD_DA_AUTHORITY_ORDERED_SOURCE_HESSIAN_NORMALIZATION",
            payload["gauge_fixing_ghost_nk"]["blockers"],
        )
        text = audit.read_text(encoding="utf-8")
        self.assertIn(r"AD:\left(\frac13,\frac23\right)", text)
        self.assertIn(r"DA:\left(\frac23,\frac13\right)", text)
        self.assertIn("FP Euler bubble", text)
        self.assertIn("Nielsen--Kallosh", text)

    def test_step5_no_descendant_pairs_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_no_descendant_pairs_exact_audit.py"
        audit = ROOT / "audits/step5-no-descendant-pairs-exact.md"
        artifact = ROOT / "audits/step5-no-descendant-pairs-exact.json"
        for path in (script, audit, artifact):
            self.assertTrue(path.is_file(), path)
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("SUMMARY 11/11 PASS", completed.stdout)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(payload["ordered_pair_count"], 25)
        self.assertTrue(all(row["anomaly_sector"] == "0" for row in payload["rows"]))
        text = audit.read_text(encoding="utf-8")
        self.assertIn("NO_OUTER_DESCENDANT__NO_CUTTING_FAILURE_WORD", text)
        self.assertIn(r"N_{\mathrm{marked\ inverse\ kernels}}", text)

    def test_step5_bc_full_family_raw_projection_exact_audit(self) -> None:
        script = ROOT / "scripts/step5_bc_full_family_raw_projection_audit.py"
        audit = ROOT / "audits/step5-bc-full-family-raw-projection-exact.md"
        artifact = ROOT / "audits/step5-bc-full-family-raw-projection-exact.json"
        for path in (script, audit, artifact):
            self.assertTrue(path.is_file(), path)
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn("84/84 PASS", completed.stdout)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "PASS_BC_CB_REGULATED_SD_KONISHI_EXACT",
        )
        self.assertFalse(payload["external_target_used"])
        self.assertEqual(payload["summary"], {"checks": 84, "passed": 84, "failed": 0})
        self.assertEqual(payload["blockers"], [])
        self.assertEqual(payload["color"]["actual_coefficient_over_lambda1"], "delta_rs")
        self.assertEqual(
            payload["ordered_results"]["r_neq_s_DD_port"],
            "EXACT_ZERO_ANTICHIRAL_FUNCTIONAL_DERIVATIVE_DELTA_RS",
        )
        self.assertEqual(
            payload["ordered_results"]["r_eq_s_DD_port"],
            "NONZERO_REGULATED_ANTICHIRAL_DENSITY_DIVERGENCE",
        )
        self.assertEqual(
            payload["ordered_results"]["B_r>C_s"],
            "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
        )
        self.assertEqual(
            payload["ordered_results"]["C_s>B_r"],
            "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
        )
        self.assertEqual(
            payload["cutting_failure"],
            {
                "DRED_difference": "bar(r_e)^2-r_(e,d)^2=mu_loop^2",
                "full_d_zero": "r_(e,d)^2/(D0*D1*D2)-1/(D1*D2)=0",
                "master": "1/(32*pi^2)",
                "regulated_kernel": "mu_loop^2/(D0*D1*D2)",
            },
        )
        self.assertEqual(
            payload["regulated_eom_jacobian"]["coefficient"],
            "2*hbar*g^2*(1/(32*pi^2))=lambda1",
        )
        self.assertEqual(
            payload["regulated_eom_jacobian"]["support"],
            "tildePhi block only; vector, FP, NK, and non-minimal components are zero",
        )
        check_ids = {row["id"] for row in payload["checks"]}
        self.assertIn("complete_outer_B_word", check_ids)
        self.assertIn("TMM_BC_kernel_nonzero_control", check_ids)
        self.assertIn("TMM_CB_kernel_nonzero_control", check_ids)
        self.assertIn("nonlinear_contact_BC_CCB", check_ids)
        self.assertIn("component_D_vertex_coefficient", check_ids)
        self.assertIn("component_same_flavor_DD_closed_routes", check_ids)
        self.assertIn("component_mixed_flavor_DD_closed_routes", check_ids)
        self.assertIn("regulated_BC_coefficient", check_ids)
        self.assertIn("BC_flavor_diagonal_density_divergence", check_ids)
        self.assertIn("CB_flavor_diagonal_density_divergence", check_ids)
        self.assertTrue(all(row["status"] == "PASS" for row in payload["checks"]))
        component = payload["independent_component_wick_audit"]
        self.assertEqual(
            component["verdict"],
            "NO_ORDINARY_COMPONENT_DD_TMM_TRIANGLE; NOT_A_TEST_OF_THE_REGULATED_EOM_JACOBIAN",
        )
        self.assertTrue(all(not row["closed_triangle"] for row in component["r_eq_s_routes"]))
        self.assertTrue(all(not row["closed_triangle"] for row in component["r_neq_s_routes"]))
        text = audit.read_text(encoding="utf-8")
        self.assertIn("PASS_BC_CB_REGULATED_SD_KONISHI_EXACT", text)
        self.assertIn(r"\bar r_e^2=r_{e,d}^2+\mu_\ell^2", text)
        self.assertIn(r"\delta_{rs}\lambda_1", text)
        self.assertIn("regulated Schwinger orbit", text)

    def test_step5_ab1_standard_feynman_strictification(self) -> None:
        script = ROOT / "scripts/step5_ab1_standard_feynman_strict_audit.py"
        audit = ROOT / "audits/step5-ab1-standard-feynman-strictification.md"
        pro_initial = ROOT / "proposals/gpt-pro-ab1-standard-feynman-2026-07-14.md"
        pro_derivation = ROOT / "proposals/gpt-pro-ab1-derivation-correction-2026-07-14.md"
        pro_final = ROOT / "proposals/gpt-pro-ab1-final-settlement-2026-07-14.md"
        for path in (script, audit, pro_initial, pro_derivation, pro_final):
            self.assertTrue(path.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["summary"]["status"], "PASS")
        self.assertEqual(result["summary"]["failed"], 0)
        self.assertGreater(result["summary"]["passed"], 80)
        self.assertEqual(result["scope"], "CONDITIONAL_FF_Q4S_AB1_ARITHMETIC_ONLY")
        self.assertEqual(
            result["claim_boundary"],
            "PASS_DOES_NOT_CERTIFY_AB1_OCCURRENCE_CENSUS_DWORD_CUT_COMPLETION_OR_RENORMALIZED_MATCH",
        )
        self.assertFalse(result["certifies_full_diagram_derivation"])
        self.assertEqual(
            result["authority"],
            {
                "commit": "00000f748fe4bdd1b5d122663cc1fb814faace66",
                "origin_main_at_check": "00000f748fe4bdd1b5d122663cc1fb814faace66",
                "verify_run": 29306335742,
                "verify_run_receipt_kind": "RECORDED_METADATA_NOT_LIVE_GITHUB_QUERY",
                "foundation_reads": "PINNED_GIT_OBJECTS_ONLY",
            },
        )
        self.assertEqual(
            result["full_diagram_derivation"]["status"],
            "BLOCKED_NO_ADMITTED_AB1_TREE_GRAPH_DRED_RESULT",
        )
        self.assertFalse(result["full_diagram_derivation"]["pass_from_this_script_implies_completion"])
        self.assertNotIn("source_hessian_census", result)
        self.assertEqual(
            result["coarse_port_pair_count"],
            {
                "status": "COARSE_ORDERED_PORT_PAIR_COUNT_ONLY__NOT_SOURCE_HESSIAN_CENSUS",
                "count_kind": "ORDERED_DISTINCT_COARSE_PORT_PAIRS",
                "certifies_source_hessian_census": False,
                "I0": 2,
                "I1": 18,
                "I2": 72,
                "total": 92,
                "nonlink": 50,
                "link_dependent": 42,
            },
        )
        checks = {row["id"]: row for row in result["checks"]}
        self.assertEqual(checks["rescaled_vector_propagator_sign"]["actual"], "-1")
        self.assertEqual(checks["rescaled_matter_propagator_sign"]["actual"], "1/16")
        self.assertEqual(checks["authority_exact_vector_momentum_rule"]["status"], "PASS")
        self.assertEqual(checks["authority_exact_matter_momentum_rule"]["status"], "PASS")
        self.assertEqual(checks["authority_origin_main_pin"]["status"], "PASS")
        self.assertEqual(checks["authority_step5a_receipt_status"]["status"], "PASS")
        self.assertEqual(checks["audit_authority_workflow_receipt_metadata"]["status"], "PASS")
        self.assertEqual(checks["audit_exact_rescaled_vector_rule"]["status"], "PASS")
        self.assertEqual(checks["audit_exact_rescaled_matter_rule"]["status"], "PASS")
        self.assertEqual(checks["degree_two_resolvent_neumann_words"]["status"], "PASS")
        self.assertEqual(checks["conditional_Q4S_trace_unit"]["actual"], "1/32")
        self.assertEqual(checks["evanescent_edge_square_unit"]["actual"], "1/32")
        self.assertEqual(checks["full_inverse_square_cut_edge_0"]["status"], "PASS")
        self.assertEqual(checks["full_inverse_square_cut_edge_1"]["status"], "PASS")
        self.assertEqual(checks["full_inverse_square_cut_edge_2"]["status"], "PASS")
        self.assertEqual(checks["g1_replay_plus_total"]["actual"], "1024")
        self.assertEqual(checks["g1_replay_minus_total"]["actual"], "-1024")
        self.assertEqual(checks["g1_a_marked_parent_DB_in_lambda1_units"]["actual"], "-3/2")
        self.assertEqual(checks["g1_b_marked_parent_DB_in_lambda1_units"]["actual"], "1")
        self.assertEqual(checks["g1_combined_parent_DB_in_lambda1_units"]["actual"], "-1/2")
        self.assertEqual(checks["g1_replay_internal_checks"]["status"], "PASS")
        self.assertEqual(checks["coarse_ordered_port_pair_total"]["actual"], "92")
        self.assertEqual(
            result["evanescent_cut_mechanism"],
            {
                "status": "REPRODUCED",
                "d_algebra_square": "four_dimensional",
                "schwinger_inverse_square": "full_d_dimensional",
                "anomaly_numerator": "mu_l^2=bar_l^2-l_d^2",
                "finite_triangle_unit": "1/(32*pi^2)",
            },
        )
        self.assertNotIn("BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES", result["blockers"])
        self.assertNotIn("BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION", result["blockers"])
        self.assertTrue(
            all(
                row["scope"] == "CONDITIONAL_FF_Q4S_AB1_ARITHMETIC_ONLY"
                and not row["certifies_full_diagram_derivation"]
                for row in result["checks"]
            )
        )
        audit_text = audit.read_text(encoding="utf-8")
        independently_required_blockers = {
            "BLOCKED_CHIRAL_TO_VECTOR_FRAME_SOURCE_BRIDGE",
            "BLOCKED_TYPED_ORIENTED_EDGE_KERNEL_ASSIGNMENT",
            "BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED",
            "BLOCKED_AB1_G1_EDGE_TAGGED_SD_CONTACT_PAIRING",
        }
        self.assertTrue(independently_required_blockers.issubset(set(result["blockers"])))
        for blocker in independently_required_blockers:
            self.assertIn(blocker, audit_text)
        for blocker in result["blockers"]:
            self.assertIn(blocker, audit_text)
        self.assertNotIn("BLOCKED_AB1_SOURCE_OVERALL_G_NORMALIZATION", result["blockers"])
        self.assertNotIn("BLOCKED_SOURCE_COUPLING_INSERTION_SIGN", result["blockers"])
        self.assertNotIn("BLOCKED_VVV_ORDERED_HESSIAN", result["blockers"])

        for label in ("initial_pro", "derivation_pro", "final_pro"):
            self.assertEqual(checks[f"{label}_archive_exists"]["status"], "PASS")
            self.assertEqual(checks[f"{label}_archive_non_authority_status"]["status"], "PASS")
            self.assertEqual(checks[f"{label}_archive_prompt_hash_declared"]["status"], "PASS")
            body_hash_id = f"{label}_archive_body_hash"
            if body_hash_id in checks:
                self.assertEqual(checks[body_hash_id]["status"], "PASS")
        self.assertEqual(
            checks["initial_pro_archive_prompt_hash"]["actual"],
            "2f8307295b028b317ca07ae29696eca93a8c3850f0c4fe3005584439add1b658",
        )
        self.assertEqual(
            checks["derivation_pro_archive_prompt_hash"]["actual"],
            "059d7aa7bef7ac723ec8969ef1af172a983c2073233fe75dab32c198be45b3fd",
        )
        self.assertEqual(
            checks["final_pro_archive_prompt_hash"]["actual"],
            "d179b8b7b80d902b7789cab3d7cfed13a6e96ef2ee152c82028883e57c88853c",
        )

    def test_step5_ab1_g1_vvv_dword_replay(self) -> None:
        script = ROOT / "scripts/step5_ab1_g1_vvv_dword_replay.py"
        artifact = ROOT / "audits/step5-ab1-g1-vvv-dword-replay.json"
        self.assertTrue(script.is_file())
        self.assertTrue(artifact.is_file())
        completed = subprocess.run(
            [sys.executable, str(script), "--check", str(artifact)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn("PASS: exact replay matches", completed.stdout)
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(payload["generated_tables"]["plus_total"]["integer"], 1024)
        self.assertEqual(payload["generated_tables"]["minus_total"]["integer"], -1024)
        self.assertTrue(all(payload["checks"].values()))

    def test_step5_dred_cutting_failure_exact(self) -> None:
        script = ROOT / "scripts/step5_dred_cutting_failure_exact_audit.py"
        audit = ROOT / "audits/step5-dred-cutting-failure-exact.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS full_square_cut_edge_0", completed.stdout)
        self.assertIn("PASS full_square_cut_edge_1", completed.stdout)
        self.assertIn("PASS full_square_cut_edge_2", completed.stdout)
        self.assertIn("PASS finite_triangle", completed.stdout)
        self.assertIn("PASS AB1_G2_direct_Wick_preD", completed.stdout)
        self.assertIn("PASS AB1_G32_direct_Wick_preD", completed.stdout)
        self.assertIn("PASS AB1_G33_direct_Wick_preD", completed.stdout)
        self.assertIn("PASS AB1_G1_plus_per_word_preD", completed.stdout)
        self.assertIn("SUMMARY 32/32 PASS", completed.stdout)

    def test_step5_dred_mu2_triangle_moments_exact(self) -> None:
        script = ROOT / "scripts/step5_dred_mu2_triangle_moments_exact_audit.py"
        self.assertTrue(script.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS centered_scalar_limit", completed.stdout)
        self.assertIn("PASS centered_rank_two_limit", completed.stdout)
        self.assertIn("PASS rank_one_p", completed.stdout)
        self.assertIn("PASS rank_two_metric_q2", completed.stdout)
        self.assertIn("SUMMARY 23/23 PASS", completed.stdout)

    def test_step5_all_letter_pairs_triangle_census(self) -> None:
        script = ROOT / "scripts/step5_all_letter_pairs_triangle_census_audit.py"
        audit = ROOT / "audits/step5-all-letter-pairs-triangle-census.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS ordered_pair_count=81", completed.stdout)
        self.assertIn("PASS nonzero_count=29", completed.stdout)
        self.assertIn("PASS zero_count=52", completed.stdout)
        self.assertIn("PASS marked_occurrence_count=72", completed.stdout)
        self.assertIn("PASS project_exact_zero_classification_crosscheck=81", completed.stdout)
        self.assertIn("PASS ht_exact_zero_classification_crosscheck=81", completed.stdout)
        self.assertIn("PASS classification_crosscheck_uses_coefficients=false", completed.stdout)
        self.assertIn(
            "PASS status=BLOCKED_RAW_ALL_PAIR_TRIANGLE_AND_DESCENDANT_ORBITS",
            completed.stdout,
        )

    def test_step5_all_triangle_parent_port_census(self) -> None:
        script = ROOT / "scripts/step5_all_triangle_parent_port_census_audit.py"
        audit = ROOT / "audits/step5-all-triangle-parent-port-census.md"
        artifact = ROOT / "audits/step5-all-triangle-parent-port-census.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        self.assertTrue(artifact.is_file())
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS external_target_used: False", completed.stdout)
        self.assertIn("PASS ordered_pair_count: 81", completed.stdout)
        self.assertIn("PASS marked_pair_count: 56", completed.stdout)
        self.assertIn("PASS directed_parent_route_count: 1365", completed.stdout)
        self.assertIn(
            "PASS legacy_directed_parent_route_count: 495",
            completed.stdout,
        )
        self.assertIn(
            "PASS spectator_directed_parent_route_count: 870",
            completed.stdout,
        )
        self.assertIn(
            "PASS marked_inverse_edge_occurrence_count: 1098",
            completed.stdout,
        )
        self.assertIn("PASS route_ids_unique: 1365", completed.stdout)
        self.assertIn(
            "PASS spectator_connected_but_1pr: 870",
            completed.stdout,
        )
        self.assertIn("PASS no_coefficient_claim: True", completed.stdout)
        self.assertIn("SUMMARY 16/16 PASS", completed.stdout)

    def test_step5_aa_matter_order_g2_support_independent(self) -> None:
        script = ROOT / "scripts/step5_aa_matter_order_g2_support_independent_audit.py"
        audit = ROOT / "audits/step5-aa-matter-order-g2-support-independent.md"
        self.assertTrue(script.is_file())
        self.assertTrue(audit.is_file())
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn("PASS MATTER_PARENT_ROUTE_COUNT", completed.stdout)
        self.assertIn("PASS MATTER_MARKED_OCCURRENCE_COUNT", completed.stdout)
        self.assertIn("PASS I0_SM4_SHIFTED_WEDGE", completed.stdout)
        self.assertIn("PASS PROJECT_ORDER_G2_TOTAL_MAGNITUDE", completed.stdout)
        self.assertIn("PASS AFTER_CHECK_CONDITIONAL_HT_MISMATCH", completed.stdout)
        self.assertIn("68/68 PASS", completed.stdout)

    def test_reference_import_has_narrow_acquisition_scope(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["type"] != "REFERENCE_IMPORT":
            self.skipTest("current task is not a reference import")
        if task["id"] == "REFERENCE-IMPORT-SUPERSPACE-001":
            urls = [item for item in task["allowed_inputs"] if item.startswith("https://")]
            self.assertEqual(
                urls,
                [
                    "https://arxiv.org/abs/hep-th/0108200",
                    "https://arxiv.org/abs/hep-th/9808041",
                    "https://arxiv.org/abs/hep-th/9903230",
                ],
            )
            return
        if task["id"] == "REFERENCE-IMPORT-WEINBERG-SREDNICKI-NOTATION-001":
            exception = task["notion_reference_exception"]
            self.assertTrue(exception["user_authorized"])
            self.assertEqual(
                exception["search_queries"],
                [
                    "Weinberg supersymmetry",
                    "The Quantum Theory of Fields Volume III Weinberg",
                    "25.2 Supersymmetry Algebra",
                    "Srednicki supersymmetry",
                ],
            )
            self.assertEqual(exception["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if "://" in item]
            self.assertEqual(
                external,
                [
                    "attachment://weinberg-srednicki-dictionary-draft",
                    "notion-search://Weinberg supersymmetry",
                    "notion-search://The Quantum Theory of Fields Volume III Weinberg",
                    "notion-search://25.2 Supersymmetry Algebra",
                    "notion-search://Srednicki supersymmetry",
                ],
            )
            return
        if task["id"] == "REFERENCE-IMPORT-SUPERSPACE-1001-VECTOR-REPRESENTATION-001":
            exception = task["local_reference_exception"]
            search_locator = "icloud-title-search://Superspace, or One Thousand and One Lessons in Supersymmetry"
            resolved_locator = "icloud-file://01_物理科研/CMC材料/CMC课题/SUPERSPACE.pdf#sha256=3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99"
            self.assertTrue(exception["user_authorized"])
            self.assertEqual(exception["search_locator"], search_locator)
            self.assertEqual(exception["resolved_locator"], resolved_locator)
            self.assertEqual(exception["resolved_sha256"], "3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99")
            self.assertEqual(exception["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if "://" in item]
            self.assertEqual(external, [search_locator, resolved_locator])
            self.assertIn("references/vendor/hep-th-0108200v1.pdf", task["allowed_inputs"])
            return
        if task["id"] == "REFERENCE-IMPORT-N2-SU2R-OBSTRUCTION-NOTE-001":
            exception = task["local_reference_exception"]
            locator = (
                "attachment://N2_SYM_offshell_SU2R_obstruction_lecture_note.tex"
                "#sha256=cc5abc773174305472acfe06b14f3d63229ffcfba9ed70f55ff3d3b534be26e6"
            )
            self.assertTrue(exception["user_authorized"])
            self.assertEqual(exception["resolved_locator"], locator)
            self.assertEqual(
                exception["resolved_sha256"],
                "cc5abc773174305472acfe06b14f3d63229ffcfba9ed70f55ff3d3b534be26e6",
            )
            self.assertEqual(exception["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if "://" in item]
            self.assertEqual(external, [locator])
            self.assertIn(
                "references/vendor/local/N2_SYM_offshell_SU2R_obstruction_lecture_note.tex",
                task["allowed_inputs"],
            )
            return
        if task["id"] == "REFERENCE-IMPORT-N2-GENERAL-LIE-CLOSURE-INSTRUCTOR-001":
            exception = task["local_reference_exception"]
            locator = (
                "attachment://N2_SYM_general_Lie_closure_instructor_2026-07-12.md"
                "#sha256=392c9e59ee038d7ac19f390acf9f18111f1a1fc880cd7fed9c09a21f42a166ec"
            )
            self.assertTrue(exception["user_authorized"])
            self.assertEqual(exception["resolved_locator"], locator)
            self.assertEqual(
                exception["resolved_sha256"],
                "392c9e59ee038d7ac19f390acf9f18111f1a1fc880cd7fed9c09a21f42a166ec",
            )
            self.assertEqual(exception["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if "://" in item]
            self.assertEqual(external, [locator])
            self.assertIn(
                "references/vendor/local/N2_SYM_general_Lie_closure_instructor_2026-07-12.md",
                task["allowed_inputs"],
            )
            return
        if task["id"] == "REFERENCE-IMPORT-SUPERSPACE-1001-SUPERGRAPH-001":
            scope = task["source_scope"]
            self.assertTrue(scope["user_authorized"])
            self.assertEqual(scope["source_id"], "ARXIV-HEP-TH-0108200-V1")
            self.assertEqual(scope["vendored_path"], "references/vendor/hep-th-0108200v1.pdf")
            self.assertEqual(
                scope["sha256"],
                "3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99",
            )
            self.assertEqual(scope["pdf_pages"], 568)
            self.assertEqual(scope["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
            self.assertEqual(scope["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            self.assertFalse(any("://" in item for item in task["allowed_inputs"]))
            self.assertIn("references/vendor/hep-th-0108200v1.pdf", task["allowed_inputs"])
            self.assertEqual(len(task["candidate_claim_ids"]), 7)
            return
        if task["id"] == "REFERENCE-IMPORT-STEP5-CHAT-WEINBERG30-001":
            chat = task["chat_reference_exception"]
            notion = task["notion_reference_exception"]
            self.assertTrue(chat["user_authorized"])
            self.assertEqual(chat["conversation_title"], "1-loop result in SYM")
            self.assertEqual(
                chat["conversation_url"],
                "https://chatgpt.com/c/6a51b2b1-5870-83e8-ad8f-b1f8496be0fc",
            )
            self.assertEqual(
                chat["share_url"],
                "https://chatgpt.com/share/6a53ea95-9138-83e8-9761-2e85a29c3970",
            )
            self.assertEqual(chat["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
            self.assertTrue(notion["user_authorized"])
            self.assertEqual(notion["book_root_page_id"], "310ee2b74b3f8065a3acdbdac27f3b2b")
            self.assertEqual(
                notion["search_queries"],
                ["Weinberg Chapter 30", "30 Supergraphs"],
            )
            self.assertEqual(notion["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
            self.assertEqual(chat["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            self.assertEqual(notion["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if "://" in item]
            self.assertEqual(
                external,
                [
                    "https://chatgpt.com/c/6a51b2b1-5870-83e8-ad8f-b1f8496be0fc",
                    "https://chatgpt.com/share/6a53ea95-9138-83e8-9761-2e85a29c3970",
                    "notion-search://Weinberg Chapter 30",
                    "notion-search://30 Supergraphs",
                ],
            )
            self.assertEqual(len(task["candidate_claim_ids"]), 3)
            return
        if task["id"] == "REFERENCE-IMPORT-HT-N4-ONE-LOOP-001":
            exception = task["reference_exception"]
            self.assertTrue(exception["user_authorized"])
            self.assertEqual(exception["source"], "arXiv:2512.07771v2")
            self.assertEqual(exception["role"], "EXTERNAL_TARGET_ONLY")
            self.assertEqual(exception["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
            self.assertEqual(exception["comparison_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
            self.assertEqual(exception["default_boundary_after_task"], "GIT_TO_NOTION_ONLY")
            external = [item for item in task["allowed_inputs"] if item.startswith("https://")]
            self.assertEqual(
                external,
                [
                    "https://arxiv.org/abs/2512.07771v2",
                    "https://arxiv.org/html/2512.07771v2",
                    "https://arxiv.org/pdf/2512.07771v2",
                    "https://export.arxiv.org/e-print/2512.07771v2",
                ],
            )
            self.assertIn(
                "references/vendor/arxiv/2512.07771v2/2512.07771v2.pdf",
                task["allowed_inputs"],
            )
            self.assertIn(
                "references/vendor/arxiv/2512.07771v2/2512.07771v2.tar.gz",
                task["allowed_inputs"],
            )
            self.assertEqual(len(task["candidate_claim_ids"]), 3)
            return
        self.fail(f"unreviewed reference-import task: {task['id']}")

    def test_superspace_1001_supergraph_reference_import(self) -> None:
        audit_path = ROOT / "audits/superspace-1001-supergraph-reference-import-verification.json"
        ledger_path = ROOT / "references/superspace-1001-supergraph-source-ledger.json"
        subset_path = ROOT / "references/vendor/local/superspace-1001-supergraph-pages.pdf"
        self.assertTrue(audit_path.exists())
        self.assertTrue(ledger_path.exists())
        self.assertTrue(subset_path.exists())
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["checks"], 149)
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(audit["totals"]["page_text_comparisons"], 46)
        self.assertEqual(audit["totals"]["page_raster_comparisons"], 46)
        self.assertEqual(ledger["scoped_artifact"]["pages"], 46)
        self.assertEqual(
            ledger["scoped_artifact"]["sha256"],
            "1cb68ae63aa5c8d8a3e2150b769ba2bfb56f245c91204bafceaa5793f969ccb8",
        )
        self.assertEqual(ledger["admissibility"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
        self.assertTrue(
            all(
                item["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT"
                for item in ledger["candidate_claims"]
            )
        )

    def test_step5_chat_weinberg30_reference_import(self) -> None:
        script = ROOT / "scripts/verify_step5_reference_import.py"
        audit_path = ROOT / "audits/step5-reference-import-verification.json"
        ledger_path = ROOT / "references/step5-chat-weinberg30-source-ledger.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        self.assertTrue(ledger_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 77, "failed": 0})
        self.assertEqual(ledger["task"], "REFERENCE-IMPORT-STEP5-CHAT-WEINBERG30-001")
        self.assertEqual(
            ledger["admissibility"]["translation_status"],
            "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        )
        self.assertFalse(ledger["admissibility"]["project_formula_adoption"])
        self.assertFalse(ledger["admissibility"]["project_contract_modified"])
        self.assertTrue(
            all(
                item["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT"
                for item in ledger["candidate_claims"]
            )
        )
        self.assertTrue(ledger["chat"]["dual_capture_result"]["share_is_exact_authenticated_suffix_by_message_id_and_content"])
        self.assertEqual(len(ledger["weinberg_chapter_30"]["fetched_pages"]), 4)

    def test_ht_n4_one_loop_reference_import(self) -> None:
        script = ROOT / "scripts/verify_ht_n4_one_loop_reference_import.py"
        audit_path = ROOT / "audits/ht-n4-one-loop-reference-import-verification.json"
        ledger_path = ROOT / "references/ht-n4-one-loop-source-ledger.json"
        metadata_path = ROOT / "references/vendor/arxiv/2512.07771v2/metadata.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        self.assertTrue(ledger_path.is_file())
        self.assertTrue(metadata_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(audit["totals"]["archive_regular_files"], 8)
        self.assertEqual(audit["totals"]["source_anchors"], 16)
        self.assertEqual(audit["totals"]["candidate_claims"], 3)
        self.assertEqual(audit["totals"]["source_internal_normalization_conflicts"], 2)
        self.assertEqual(audit["totals"]["source_internal_ordering_audits"], 1)
        self.assertEqual(ledger["admissibility"]["role"], "EXTERNAL_TARGET_ONLY")
        self.assertEqual(
            ledger["admissibility"]["translation_status"],
            "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        )
        self.assertEqual(
            ledger["admissibility"]["comparison_status"],
            "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        )
        self.assertEqual(
            ledger["source_internal_ordering_audits"][0]["status"],
            "PASS",
        )

    def test_contract_change_has_no_network_inputs(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["type"] != "CONTRACT_CHANGE":
            self.skipTest("current task is not a contract change")
        self.assertFalse(any(item.startswith("http://") or item.startswith("https://") for item in task["allowed_inputs"]))
        for item in task["allowed_inputs"]:
            self.assertTrue((ROOT / item).exists(), item)
        if "reference_admission" in task:
            claim_map = json.loads((ROOT / "references/claim-map.yaml").read_text(encoding="utf-8"))
            registered_claims = {item["id"] for item in claim_map["claims"]}
            self.assertTrue(set(task["reference_admission"]["admitted_claim_ids"]) <= registered_claims)

    def test_step5_contract_registration(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["id"] != "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001":
            self.skipTest("Step-5 Euclidean N=4 AWI task is not current")
        self.assertEqual(task["type"], "CONTRACT_CHANGE")
        self.assertEqual(task["status"], "ACCEPTED")
        self.assertEqual(task["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR")
        self.assertTrue(task["reference_admission"]["source_translation_required_before_formula_adoption"])
        self.assertTrue(task["reference_admission"]["independent_project_derivation_required_before_target_comparison"])
        self.assertEqual(len(task["acceptance"]), 16)
        external_target_ids = task["reference_admission"]["external_target_only_claim_ids"]
        self.assertEqual(
            external_target_ids,
            [
                "HT-N4-ONE-LOOP-COMPLETE-SUPERFIELD-CANDIDATE",
                "HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE",
                "HT-ONE-LOOP-MASTER-INTEGRAL-CANDIDATE",
            ],
        )
        self.assertTrue(set(external_target_ids) <= set(task["reference_admission"]["admitted_claim_ids"]))
        claim_map = json.loads((ROOT / "references/claim-map.yaml").read_text(encoding="utf-8"))
        classifications = {item["id"]: item.get("classification") for item in claim_map["claims"]}
        self.assertTrue(all(classifications[claim_id] == "EXTERNAL_TARGET_ONLY" for claim_id in external_target_ids))
        self.assertTrue(any("sixteen channel classes" in item for item in task["acceptance"]))
        self.assertTrue(any("exactly eighty-one ordered component pairs" in item for item in task["acceptance"]))
        self.assertTrue(any("arbitrary holomorphic-derivative tower" in item for item in task["acceptance"]))
        self.assertTrue(any("HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT" in item for item in task["acceptance"]))
        self.assertTrue(any("HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO" in item for item in task["acceptance"]))
        self.assertTrue(any("forward and inverse maps compose to the identity" in item for item in task["acceptance"]))
        self.assertTrue(any("holomorphic-twist round-trip audit" in item for item in task["acceptance"]))
        self.assertTrue(any("external leg" in item for item in task["acceptance"]))
        self.assertTrue(any("isolated triangle" in item for item in task["forbidden_inputs"]))
        evidence = set(task["acceptance_evidence"])
        self.assertTrue(
            {
                "contracts/foundations/step-05-euclidean-n4-awi-one-loop.md",
                "audits/step5-euclidean-n4-awi-verification.json",
                "audits/step5-global-81-target-blind-orbit-ledger.json",
                "audits/step5_global_81_ht_symbolic_roundtrip_exact.json",
                "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json",
                "audits/step5-aa-external-slot-decomposition-exact.json",
            }
            <= evidence
        )
        self.assertTrue(all((ROOT / relative).is_file() for relative in evidence))
        obsolete = set(task["excluded_obsolete_acceptance_evidence"])
        self.assertEqual(
            obsolete,
            {
                "audits/step5-ab-ba-full-1pi-quotient-exact.json",
                "audits/step5-ab-ba-full-1pi-quotient-exact.md",
                "scripts/step5_ab_ba_full_1pi_quotient_exact_audit.py",
            },
        )
        self.assertTrue(evidence.isdisjoint(obsolete))
        self.assertTrue(
            all(item.startswith("OUT_OF_SCOPE_") for item in task["out_of_scope_nonblocking"])
        )

    def test_step5_physical_settlement_contract(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["id"] != "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001":
            self.skipTest("Step-5 Euclidean N=4 AWI task is not current")

        relative = "contracts/foundations/step-05-euclidean-n4-awi-one-loop.md"
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest = json.loads((ROOT / "contracts/manifest.yaml").read_text(encoding="utf-8"))
        entries = [
            entry
            for entry in manifest["contracts"]
            if entry["id"] == "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"
        ]
        self.assertEqual(manifest["state"], "ACCEPTED")
        self.assertEqual(manifest["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["path"], relative)
        self.assertEqual(entries[0]["status"], "DERIVED_UNFROZEN")
        self.assertEqual(entries[0]["sha256"], digest)
        self.assertIn(
            "Status: `ACCEPTED_PHYSICAL_ONE_LOOP_ANOMALY_SECTOR__81_COMPLETE_EXACT__HT_CORRECTED_ROUNDTRIP_EXACT`",
            text,
        )
        self.assertEqual(text.count("$$") % 2, 0)
        for token in (r"\sim", r"\approx", r"\propto"):
            self.assertNotIn(token, text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\t")

        self.assertEqual(task["status"], "ACCEPTED")
        self.assertEqual(task["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR")
        self.assertNotIn(relative, task["allowed_inputs"])
        self.assertIn(relative, task["acceptance_evidence"])
        proof_ledger = json.loads(
            (ROOT / "ledger/proof_obligations.json").read_text(encoding="utf-8")
        )
        obligation = next(
            row
            for row in proof_ledger["proof_obligations"]
            if row["id"] == task["id"]
        )
        self.assertEqual(obligation["state"], "ACCEPTED")
        self.assertIsNone(obligation["blocking_reason"])
        self.assertEqual(
            obligation["task_sha256"],
            hashlib.sha256((ROOT / obligation["task"]).read_bytes()).hexdigest(),
        )
        self.assertNotIn(
            "STEP5_ONE_LOOP_FAIL_CLOSED_CHECKPOINT",
            obligation["checked_scope"],
        )
        settlement = obligation["checked_scope"]["STEP5_PHYSICAL_ONE_LOOP_ANOMALY_SETTLEMENT"]
        self.assertEqual(
            settlement["result"],
            "ACCEPTED_PHYSICAL_ONE_LOOP_ANOMALY_SECTOR__81_COMPLETE_EXACT__HT_CORRECTED_ROUNDTRIP_EXACT",
        )
        self.assertEqual(settlement["verification_status"], "ACCEPTED")
        self.assertEqual(settlement["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR")
        self.assertEqual(settlement["contract_sha256"], digest)
        self.assertEqual(settlement["verifier_totals"], {"checks": 33, "passed": 33, "failed": 0})
        self.assertEqual(
            settlement["global_81_ledger"],
            {
                "audit": "audits/step5-global-81-target-blind-orbit-ledger.json",
                "final_state_counts": {"COMPLETE_EXACT": 81},
                "ordered_pairs": 81,
                "exact_nonzero": 29,
                "exact_zero": 52,
                "unresolved": 0,
            },
        )
        self.assertEqual(settlement["holomorphic_twist_roundtrip"]["direct_rows"], 81)
        self.assertEqual(settlement["holomorphic_twist_roundtrip"]["output_words"], 70)
        self.assertEqual(settlement["holomorphic_twist_roundtrip"]["finite_kernel_checks"], 2025)
        self.assertEqual(
            settlement["bc_cb_regulated_sd_konishi"],
            {
                "audit": "audits/step5-bc-full-family-raw-projection-exact.json",
                "status": "PASS_BC_CB_REGULATED_SD_KONISHI_EXACT",
                "checks": 84,
                "failed": 0,
            },
        )
        self.assertTrue(
            all(item.startswith("OUT_OF_SCOPE_") for item in settlement["out_of_scope_nonblocking"])
        )
        self.assertTrue(
            set(settlement["excluded_obsolete_acceptance_evidence"]).isdisjoint(
                task["acceptance_evidence"]
            )
        )
        step5a = obligation["checked_scope"]["STEP5A_COMPONENT_BV_BRST_PRIMITIVE_GRAMMAR"]
        self.assertEqual(
            step5a["acceptance_relation"],
            "OUT_OF_SCOPE_FOR_PHYSICAL_ONE_LOOP_ANOMALY_SECTOR",
        )
        self.assertTrue(
            all(item.startswith("OUT_OF_SCOPE_") for item in step5a["out_of_scope_limits"])
        )
        unescaped_text = text.replace(r"\_", "_")
        for boundary in (
            "OUT_OF_SCOPE_RAW_GRAPH_Q_EQUIVARIANT_FUNCTOR",
            "OUT_OF_SCOPE_GENERAL_BV_WZ_REDUCTION",
            "OUT_OF_SCOPE_OPEN_COLOR_SOURCE_BV_EXTENSION",
            "OUT_OF_SCOPE_FORMAL_U_Q0_ABSOLUTE_INTERTWINER",
            "OUT_OF_SCOPE_GENERAL_REDUCTIVE_COLOR_FRAME",
        ):
            self.assertIn(boundary, unescaped_text)

    def test_step5_physical_settlement_verifier(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["id"] != "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001":
            self.skipTest("Step-5 Euclidean N=4 AWI task is not current")
        script = ROOT / "scripts/verify_step5_euclidean_n4_awi.py"
        audit_path = ROOT / "audits/step5-euclidean-n4-awi-verification.json"
        expected = audit_path.read_bytes()
        completed = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(audit_path.read_bytes(), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "ACCEPTED")
        self.assertEqual(audit["accepted_scope"], "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR")
        self.assertEqual(audit["failed_checks"], [])
        self.assertEqual(audit["totals"], {"checks": 33, "passed": 33, "failed": 0})
        self.assertEqual(
            audit["counts"],
            {
                "ordered_pairs": 81,
                "exact_nonzero": 29,
                "exact_zero": 52,
                "direct_ht_rows": 81,
                "base_output_words": 70,
                "finite_symbolic_kernel_checks": 2025,
            },
        )
        self.assertEqual(
            audit["scope_boundary"],
            {
                "accepted": ["PHYSICAL_ONE_LOOP_ANOMALY_SECTOR"],
                "out_of_scope": {
                    "RAW_Q_FUNCTOR": "OUT_OF_SCOPE",
                    "BV_WZ_COMPLETION": "OUT_OF_SCOPE",
                    "OPEN_COLOR_SOURCE_EXTENSION": "OUT_OF_SCOPE",
                    "FORMAL_U_INTERTWINER": "OUT_OF_SCOPE",
                    "GENERAL_REDUCTIVE_COLOR_THEOREM": "OUT_OF_SCOPE",
                },
                "out_of_scope_items_are_not_acceptance_blockers": True,
            },
        )
        self.assertEqual(
            audit["exact_identity"],
            "full_d_square+Schwinger_cut=0; bar_loop_square-full_d_loop_square=mu_l^2; J_mu2=1/(32*pi^2)",
        )
        self.assertEqual(
            audit["holomorphic_twist_identity"],
            "K_Project=2*T_HT_printed=T_HT_corrected for all m,n>=0",
        )
        self.assertTrue(all(row["status"] == "PASS" for row in audit["checks"]))
        freshness_ids = {
            row["id"] for row in audit["checks"] if row["id"].startswith("freshness.")
        }
        self.assertEqual(
            freshness_ids,
            {
                "freshness.global_81_target_blind_ledger",
                "freshness.ab_ba_project_ward_finite_renormalization",
                "freshness.ab_ba_vector_frame_missing_orbit",
                "freshness.ab_ba_g3_original_full_measure",
                "freshness.global_81_ht_symbolic_roundtrip",
                "freshness.dred_cutting_failure",
                "freshness.dred_mu2_triangle_moments",
            },
        )
        authority_gate = next(
            row
            for row in audit["checks"]
            if row["id"] == "authority.origin_main_matches_frozen_base"
        )
        self.assertEqual(authority_gate["status"], "PASS")
        for relative, expected_digest in audit["evidence_sha256"].items():
            self.assertEqual(
                hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(),
                expected_digest,
            )
        self.assertEqual(
            set(audit["excluded_obsolete_evidence"]),
            set(task["excluded_obsolete_acceptance_evidence"]),
        )
        self.assertTrue(
            set(audit["evidence_sha256"]).isdisjoint(audit["excluded_obsolete_evidence"])
        )

    def test_step5a_component_bv_brst_primitive_grammar(self) -> None:
        relative = "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        tags = re.findall(r"\\tag\{(5A\.[^}]+)\}", text)
        self.assertEqual(len(tags), len(set(tags)))
        self.assertEqual(
            {tag for tag in tags if tag[3:].isdigit()},
            {f"5A.{number}" for number in range(1, 82)},
        )
        self.assertIn("5A.53a", tags)
        self.assertEqual(text.count("$$") % 2, 0)
        for token in (r"\sim", r"\approx", r"\propto"):
            self.assertNotIn(token, text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\t")
        self.assertEqual(
            [
                line_number
                for line_number, line in enumerate(text.splitlines(), start=1)
                if re.search(r"(?<!\\)qquad", line)
            ],
            [],
        )
        self.assertNotIn(r"\Delta_{R,\nu}^2=0", text)

        blockers = (
            "BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED",
            "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
            "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
            "BLOCKED_STEP3D_LC_VECTOR_CYCLE",
        )
        for blocker in blockers:
            self.assertEqual(text.count(blocker), 1)
        for required in (
            r"f_{AB}=h\kappa_{AB}+i\mathfrak k_{AB}",
            r"\mathcal V_R\ne\mathcal V_R^{\mathrm{WZ}}",
            r"\mathfrak R_{R,\nu}^{\mathsf i}",
            r"\mathfrak O^{\mathrm{BV}}_{E,\nu}[W]",
            r"\mathfrak M^\Delta_{R,\nu}[F]",
            r"&:=\Delta_{R,\nu}^2F",
            r"\widehat{\boldsymbol\varpi}_{R,\nu}\ \text{BV-compatible}",
            r"\mathfrak M^\Delta_{R,\nu}[F]=0\quad\text{for every }F",
            r"a_{pq}:=\frac{(-1)^p}{p!q!(p+q+1)}",
            r"\widetilde a_{pq}:=\frac{(-1)^{q+1}}{p!q!(p+q+1)}",
            r"\right|_{V=0}",
            r"(-\tau_R^{-1})^{|E(G)|}",
            r"-\tau_L^{-1}=i\hbar",
            r"-\tau_E^{-1}=\hbar",
            r"\mathcal Y_{E,\mathrm{FF}}\text{ is nonlocal}",
            "complete accepted Feynman rules are not claimed",
        ):
            self.assertIn(required, text)

        manifest = json.loads((ROOT / "contracts/manifest.yaml").read_text(encoding="utf-8"))
        entry = next(
            item
            for item in manifest["contracts"]
            if item["id"] == "FOUNDATION-COMPONENT-BV-BRST-PRIMITIVE-SUPERGRAPH-GRAMMAR-005A"
        )
        self.assertEqual(entry["path"], relative)
        self.assertEqual(entry["status"], "DERIVED_UNFROZEN")
        self.assertEqual(entry["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        self.assertIn(relative, task["allowed_inputs"])
        ledger = json.loads((ROOT / "ledger/proof_obligations.json").read_text(encoding="utf-8"))
        obligation = next(
            item
            for item in ledger["proof_obligations"]
            if item["id"] == "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"
        )
        self.assertEqual(obligation["state"], "ACCEPTED")
        checked = obligation["checked_scope"]["STEP5A_COMPONENT_BV_BRST_PRIMITIVE_GRAMMAR"]
        self.assertEqual(checked["result"], "PASS_EXACT_PARTIAL_SCOPE")
        self.assertEqual(
            checked["acceptance_relation"],
            "OUT_OF_SCOPE_FOR_PHYSICAL_ONE_LOOP_ANOMALY_SECTOR",
        )
        self.assertEqual(checked["contract_sha256"], entry["sha256"])
        self.assertEqual(
            checked["out_of_scope_limits"],
            [
                "OUT_OF_SCOPE_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE",
                "OUT_OF_SCOPE_STEP5A_NK_BRANCH",
                "OUT_OF_SCOPE_STEP5A_GENERAL_MOMENTUM_RULES_FOURIER_DRED_LEDGER",
                "OUT_OF_SCOPE_STEP3D_LORENTZIAN_VECTOR_CYCLE",
            ],
        )

    def test_step5a_exact_verifier_and_audits(self) -> None:
        script = ROOT / "scripts/verify_step5a_component_bv_brst_grammar.py"
        audit_path = ROOT / "audits/step5a-component-bv-brst-grammar-verification.json"
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS_EXACT_PARTIAL_SCOPE")
        self.assertEqual(audit["totals"]["failed_check_families"], 0)
        self.assertGreaterEqual(audit["totals"]["exact_check_families"], 42)
        self.assertTrue(all(item["passed"] for item in audit["checks"]))
        for relative in (
            "audits/step5a-notation-ledger.json",
            "audits/step5a-gap-audit.json",
            "audits/step5a-independent-review.json",
        ):
            manual = json.loads((ROOT / relative).read_text(encoding="utf-8"))
            self.assertEqual(manual["result"], "PASS_EXACT_PARTIAL_SCOPE")
            self.assertEqual(manual["post_resolution"], {"P0": [], "P1": []})

    def test_step_1_formula_surface(self) -> None:
        text = (ROOT / "contracts/foundations/step-01-supersymmetry-commutator.md").read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{1\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 69)))
        self.assertIn(r"\{Q^L_a,\bar Q^L_{\dot b}\}", text)
        self.assertIn(r"Q^E_a=-iQ^L_a", text)
        self.assertIn(r"\{Q^E_a,\bar Q^E_{\dot b}\}", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)

    def test_step_2a_formula_surface(self) -> None:
        path = ROOT / "contracts/foundations/step-02a-flat-superspace.md"
        if not path.exists():
            self.skipTest("Step 2A contract is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{2A\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 54)))
        for subtag in ("15a", "20a", "20b", "20c", "20d", "50a"):
            self.assertIn(rf"\tag{{2A.{subtag}}}", text)
        self.assertIn(r"\mathsf P^L_\mu=-i\partial_\mu^L", text)
        self.assertIn(r"\mathsf P_m^E=-\partial_m^E", text)
        self.assertIn(r"\pi_m^E:=i\mathsf P_m^E=-i\partial_m^E", text)
        self.assertIn(r"\{\bar\partial_{\dot a},\bar\vartheta^{\dot b}\}", text)
        self.assertIn("Intrinsic Euclidean superspace imposes no relation", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)

    def test_step_2a_notation_audit(self) -> None:
        path = ROOT / "audits/step2a-notation-ledger.json"
        if not path.exists():
            self.skipTest("Step 2A notation audit is not registered")
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["result"], "PASS")
        self.assertEqual(audit["findings"]["P0"], [])
        self.assertEqual(audit["findings"]["P1"], [])
        self.assertTrue(all(item["result"] == "PASS" for item in audit["checks"]))

    def test_step_2a_exact_symbolic_verifier(self) -> None:
        script = ROOT / "scripts/verify_step2a_flat_superspace.py"
        audit_path = ROOT / "audits/step2a-symbolic-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 2A symbolic verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["operator_identities"], 244)
        self.assertEqual(audit["totals"]["input_cases"], 3184)
        self.assertEqual(audit["totals"]["failed_cases"], 0)

    def test_step_2a_independent_review(self) -> None:
        path = ROOT / "audits/step2a-independent-review.json"
        if not path.exists():
            self.skipTest("Step 2A independent review is not registered")
        review = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(review["result"], "PASS")
        self.assertEqual(review["post_resolution"]["P0"], [])
        self.assertEqual(review["post_resolution"]["P1"], [])
        self.assertTrue(all(item["status"] == "RESOLVED" for item in review["findings"]))

    def test_step_2b_formula_surface(self) -> None:
        path = ROOT / "contracts/foundations/step-02b-superconformal-superspace.md"
        if not path.exists():
            self.skipTest("Step 2B contract is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{2B\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 79)))
        for subtag in (
            "31a",
            "31b",
            "33b",
            "34bb",
            "35a",
            "35fa",
            "35h",
            "35i",
            "35k",
            "58b",
            "58g",
            "60c",
            "61c",
            "63c",
            "76b",
        ):
            self.assertIn(rf"\tag{{2B.{subtag}}}", text)
        self.assertIn(r"\bar y^\mu-y^\mu", text)
        self.assertIn(r"\mathcal I_{s,L}^*:\mathscr F_{\rm ch}\longleftrightarrow", text)
        self.assertIn(r"\mathsf K_\mu^L", text)
        self.assertIn(r"\mathsf S_L^a", text)
        self.assertIn(r"\bar{\mathsf S}_L^{\dot a}", text)
        self.assertIn(r"\boxed{r=-\frac23\Delta.}", text)
        self.assertIn(r"\mathsf P_m^E&=-\partial_m^E", text)
        self.assertIn(r"\mathsf R_E&=-iN_\vartheta", text)
        self.assertIn("Intrinsic Euclidean superspace imposes no adjoint relation", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)

    def test_step_2b_notation_audit(self) -> None:
        path = ROOT / "audits/step2b-notation-ledger.json"
        if not path.exists():
            self.skipTest("Step 2B notation audit is not registered")
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["result"], "PASS")
        self.assertEqual(audit["findings"]["P0"], [])
        self.assertEqual(audit["findings"]["P1"], [])
        self.assertTrue(all(item["result"] == "PASS" for item in audit["checks"]))

    def test_step_2b_lorentz_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step2b_chiral_superconformal.py"
        audit_path = ROOT / "audits/step2b-lorentzian-superconformal-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 2B Lorentz verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["operator_identities"], 905)
        self.assertEqual(audit["input_cases"], 54300)
        self.assertEqual(audit["failed_cases"], 0)

    def test_step_2b_euclidean_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step2b_euclidean_superconformal.py"
        audit_path = ROOT / "audits/step2b-euclidean-superconformal-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 2B Euclidean verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["operator_identities"], 763)
        self.assertEqual(audit["input_cases"], 45780)
        self.assertEqual(audit["failed_cases"], 0)

    def test_step_2b_independent_review(self) -> None:
        path = ROOT / "audits/step2b-independent-review.json"
        if not path.exists():
            self.skipTest("Step 2B independent review is not registered")
        review = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(review["result"], "PASS")
        self.assertEqual(review["post_resolution"]["P0"], [])
        self.assertEqual(review["post_resolution"]["P1"], [])
        self.assertTrue(all(item["status"] == "RESOLVED" for item in review["findings"]))

    def test_step_2c_formula_surface(self) -> None:
        path = ROOT / "contracts/foundations/step-02c-complete-superconformal-covariance.md"
        if not path.exists():
            self.skipTest("Step 2C contract is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{2C\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 63)))
        for subtag in (
            "3a",
            "5a",
            "12a",
            "12b",
            "12c",
            "12d",
            "29a",
            "29ba",
            "29e",
            "30a",
            "43a",
            "46a",
            "47a",
            "49b",
            "58c",
        ):
            self.assertIn(rf"\tag{{2C.{subtag}}}", text)
        self.assertIn(r"\boxed{\mathsf P_\mu^L=-i\partial_\mu.}", text)
        self.assertIn(r"\widetilde{\bar\partial}_{\dot a}", text)
        self.assertIn(r"\mathsf K_\mu^L", text)
        self.assertIn(r"\mathsf S_L^a", text)
        self.assertIn(r"\bar{\mathsf S}_L^{\dot a}", text)
        self.assertIn(r"\boldsymbol{\mathsf G}_A^L", text)
        self.assertIn(r"M_{\Phi_{\lambda'\leftarrow\lambda}}", text)
        self.assertIn(r"\mathsf K_m^E", text)
        self.assertIn(r"\mathsf S_E^a", text)
        self.assertIn(r"\bar{\mathsf S}_E^{\dot a}", text)
        self.assertIn(r"N_L", text)
        self.assertIn(r"N_E=62{,}704", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)

    def test_step_2c_notation_audit(self) -> None:
        path = ROOT / "audits/step2c-notation-ledger.json"
        if not path.exists():
            self.skipTest("Step 2C notation audit is not registered")
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["result"], "PASS")
        self.assertEqual(audit["findings"]["P0"], [])
        self.assertEqual(audit["findings"]["P1"], [])
        self.assertTrue(all(item["result"] == "PASS" for item in audit["checks"]))

    def test_step_2c_lorentz_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step2c_full_lorentz_superconformal.py"
        audit_path = ROOT / "audits/step2c-full-lorentz-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 2C Lorentz verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["basis"]["grassmann_monomials"], 16)
        self.assertEqual(audit["coverage"]["total_exact_cases"], 58896)
        self.assertEqual(audit["failed_cases"], 0)

    def test_step_2c_euclidean_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step2c_full_euclidean_superconformal.py"
        audit_path = ROOT / "audits/step2c-full-euclidean-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 2C Euclidean verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["basis"]["grassmann_monomials"], 16)
        self.assertEqual(audit["operator_identities"], 1163)
        self.assertEqual(audit["input_cases"], 62704)
        self.assertEqual(audit["failed_cases"], 0)

    def test_step_2c_independent_review(self) -> None:
        path = ROOT / "audits/step2c-independent-review.json"
        if not path.exists():
            self.skipTest("Step 2C independent review is not registered")
        review = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(review["result"], "PASS")
        self.assertEqual(review["post_resolution"], {"P0": [], "P1": []})
        self.assertTrue(all(item["status"] == "RESOLVED" for item in review["resolved_findings"]))
        self.assertEqual(review["exact_verification"]["lorentz_total_cases"], 58896)
        self.assertEqual(review["exact_verification"]["euclidean_total_cases"], 62704)
        self.assertEqual(review["exact_verification"]["failed_cases"], 0)

    def test_step_3a_formula_surface(self) -> None:
        path = ROOT / "contracts/foundations/step-03a-gauge-chiral-action.md"
        if not path.exists():
            self.skipTest("Step 3A contract is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{3A\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 107)))
        for subtag in (
            "34a",
            "34b",
            "50a",
            "50b",
            "50c",
            "50d",
            "53a",
            "54a",
            "65a",
            "65b",
            "66a",
            "84a",
            "104a",
        ):
            self.assertIn(rf"\tag{{3A.{subtag}}}", text)
        self.assertIn(r"\psi_{Ra}^I:=\frac1{\sqrt2}D_{Ra}\Phi_R^I\Big|", text)
        self.assertIn(r"\boxed{\mathcal D_\mu=\partial_\mu-iA_\mu.}", text)
        self.assertIn(r"\mathcal W_{Ra}", text)
        self.assertIn(r"[T_A,T_B]=ic_{AB}{}^CT_C", text)
        self.assertIn(r"f_{AB}(\Phi)=f_{BA}(\Phi)", text)
        self.assertIn(r"N_{\rm identities}=88", text)
        self.assertIn(r"N_{\rm component\ coefficients}=336", text)
        d_density = text.split(
            "### 3A.8 Canonical matter $D$-density from covariant $D$-algebra",
            maxsplit=1,
        )[1].split("For the superpotential", maxsplit=1)[0]
        self.assertNotIn(r"\vartheta", d_density)
        self.assertNotIn("direct multiplication", d_density.lower())
        self.assertIn(r"\nabla_R^{\leftarrow2}A_R", d_density)
        self.assertIn(r"\mathcal K_R^{\rm ord}", d_density)
        self.assertIn(r"\partial_{RM}J_R^M", d_density)
        self.assertIn(
            r"\int d^4x_L\,[\bar\Phi\mathcal E_L\Phi]_D",
            d_density,
        )
        self.assertNotIn("Direct Euclidean multiplication", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\r\t")

    def test_step_3a_notation_audit(self) -> None:
        path = ROOT / "audits/step3a-notation-ledger.json"
        if not path.exists():
            self.skipTest("Step 3A notation audit is not registered")
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["result"], "PASS")
        self.assertEqual(audit["findings"]["P0"], [])
        self.assertEqual(audit["findings"]["P1"], [])
        self.assertTrue(all(item["result"] == "PASS" for item in audit["checks"]))

    def test_step_3a_exact_component_verifier(self) -> None:
        script = ROOT / "scripts/verify_step3a_gauge_chiral_action.py"
        audit_path = ROOT / "audits/step3a-gauge-chiral-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 3A exact verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["exact_identities"], 88)
        self.assertEqual(audit["totals"]["exact_component_coefficients"], 336)
        self.assertEqual(audit["totals"]["failed_checks"], 0)
        self.assertEqual(audit["projection_checks"]["projection_chain_failures"], 0)
        self.assertEqual(
            audit["projection_checks"]["projection_chain_coefficients"],
            164,
        )

    def test_step_3a_independent_review(self) -> None:
        path = ROOT / "audits/step3a-independent-review.json"
        if not path.exists():
            self.skipTest("Step 3A independent review is not registered")
        review = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(review["result"], "PASS")
        self.assertEqual(review["post_resolution"], {"P0": [], "P1": []})
        self.assertTrue(
            all(item["status"] == "RESOLVED" for item in review["resolved_findings"])
        )
        self.assertEqual(
            review["exact_verification"],
            {
                "identities": 88,
                "component_coefficients": 336,
                "failed": 0,
                "status": "PASS",
            },
        )

    def test_weinberg_srednicki_dictionary_surface(self) -> None:
        path = ROOT / "contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md"
        if not path.exists():
            self.skipTest("Weinberg-Srednicki-project dictionary is not registered")
        text = path.read_text(encoding="utf-8")
        tags = re.findall(r"\\tag\{(D\.[^}]+)\}", text)
        self.assertGreaterEqual(len(tags), 130)
        self.assertEqual(len(tags), len(set(tags)))
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        self.assertNotIn(",qquad", text)
        self.assertNotIn("Pending integrated fields", text)
        self.assertIn(r"\Theta_W=-i\Theta_S^{(4)}", text)
        self.assertIn(r"[X]^S_D=\frac12[X]^W_D+\frac14\Box C_X", text)
        self.assertIn(r"\int d^4x\,[X]^S_D", text)
        self.assertIn(r"V_c^A=V_S^A", text)
        self.assertIn(r"\widehat V^A=gV_S^A", text)
        self.assertNotIn("PROJECT_UNFIXED", text)
        self.assertIn("Verified Step 3A equations", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\r\t")

    def test_step_3b_component_reconstruction_contract(self) -> None:
        path = ROOT / "contracts/foundations/step-03b-component-reconstruction.md"
        if not path.exists():
            self.skipTest("Step 3B component reconstruction is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{3B\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 118)))
        self.assertIn(r"\tag{3B.63a}", text)
        self.assertIn(r"\widetilde\nabla_{\dot a}^{\,\mathrm{row}}X", text)
        self.assertIn(r"\mathcal L_{K,L}^{\rm raw}", text)
        self.assertIn(r"\mathcal C_{L,f}", text)
        self.assertIn(r"\widetilde{\mathcal C}_{E,\widetilde f}", text)
        self.assertIn(r"N_{\rm failures}=0", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\r\t")

    def test_step_3b_exact_component_verifier(self) -> None:
        script = ROOT / "scripts/verify_step3b_component_reconstruction.py"
        audit_path = ROOT / "audits/step3b-component-reconstruction-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 3B exact verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["new_exact_identities"], 99)
        self.assertEqual(audit["totals"]["new_exact_component_coefficients"], 772)
        self.assertEqual(audit["totals"]["cumulative_exact_identities"], 187)
        self.assertEqual(audit["totals"]["cumulative_exact_component_coefficients"], 1108)
        self.assertEqual(audit["totals"]["failed_checks"], 0)

    def test_step_3b_audits(self) -> None:
        for relative in (
            "audits/step3b-gap-audit.json",
            "audits/step3b-notation-ledger.json",
            "audits/step3b-independent-review.json",
        ):
            path = ROOT / relative
            if not path.exists():
                self.skipTest(f"{relative} is not registered")
            audit = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(audit["result"], "PASS")
            self.assertEqual(audit["post_resolution"]["P0"], [])
            self.assertEqual(audit["post_resolution"]["P1"], [])

    def test_step_3c_gauge_vector_representation_contract(self) -> None:
        path = ROOT / "contracts/foundations/step-03c-gauge-vector-representation.md"
        if not path.exists():
            self.skipTest("Step 3C gauge-vector representation is not registered")
        text = path.read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{3C\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 82)))
        self.assertIn(r"\tag{3C.39a}", text)
        self.assertIn(r"\tag{3C.60a}", text)
        for letter in "abcdefghijklmnop":
            self.assertIn(rf"\tag{{3C.72{letter}}}", text)
        self.assertIn(r"\mathsf V:=\text{gauge-vector frame}", text)
        self.assertIn(r"\mathsf C:=\text{gauge-chiral frame}", text)
        self.assertIn(r"\mathsf A:=\text{gauge-antichiral frame}", text)
        self.assertIn(r"\rho_R:=\frac4{\kappa_R^2}", text)
        self.assertIn(r"\xi_Ac_{BC}{}^A=0", text)
        self.assertIn(r"\widetilde{\mathcal B}_R\mathcal B_R", text)
        self.assertIn(r"\boldsymbol\nabla_R^{\mathsf V a}", text)
        self.assertIn("#### 3C.6.1 Canonical matter density", text)
        self.assertIn("#### 3C.6.2 Chiral and gauge densities", text)
        self.assertIn(r"\partial_{RM}J_R^M", text)
        self.assertIn(r"\mathfrak C_R^{AB}", text)
        self.assertIn(r"\mathcal L_{L,\mathrm{can}}", text)
        self.assertIn(r"\mathcal L_{E,\mathrm{can}}", text)
        density_segment = text[
            text.index("#### 3C.6.1 Canonical matter density") : text.index(
                "### 3C.7 Wick transport"
            )
        ]
        self.assertNotIn(r"\vartheta", density_segment)
        self.assertNotRegex(text, r"\^\{V(?:A|B|a|\\dot)")
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\r\t")

    def test_step_3c_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step3c_gauge_vector_representation.py"
        audit_path = ROOT / "audits/step3c-vector-representation-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 3C exact verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["exact_checks"], 206)
        self.assertEqual(audit["totals"]["failed_checks"], 0)
        self.assertTrue(all(item["failed"] == 0 for item in audit["categories"].values()))
        self.assertEqual(audit["categories"]["component_density_binding"]["failed"], 0)
        self.assertEqual(audit["categories"]["mutation"]["failed"], 0)

    def test_step_3c_audits(self) -> None:
        for relative in (
            "audits/step3c-gap-audit.json",
            "audits/step3c-notation-ledger.json",
            "audits/step3c-independent-review.json",
        ):
            path = ROOT / relative
            if not path.exists():
                self.skipTest(f"{relative} is not registered")
            audit = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(audit["result"], "PASS")
            if "post_resolution" in audit:
                self.assertEqual(audit["post_resolution"]["P0"], [])
                self.assertEqual(audit["post_resolution"]["P1"], [])
            else:
                self.assertEqual(audit["verification"]["post_resolution_P0"], [])
                self.assertEqual(audit["verification"]["post_resolution_P1"], [])

    def test_step_3c_write_only_mirror_receipt(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        mirror_task = json.loads(
            (ROOT / "tasks/archive/MIRROR-STEP-03C-DALGEBRA-NOTION-001.yaml").read_text(encoding="utf-8")
        )
        page = next(
            item
            for item in page_map["pages"]
            if item["id"] == "FOUNDATION-GAUGE-VECTOR-REPRESENTATION-003C"
        )
        write = next(
            item
            for item in receipt["pages"]
            if item["id"] == "FOUNDATION-GAUGE-VECTOR-REPRESENTATION-003C"
        )
        self.assertEqual(page["source_commit"], "f340e44d233881a7133a8ca11624ac47fc6070ec")
        self.assertEqual(page["source_sha256"], "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1")
        self.assertEqual(page["notion_page_id"], "39aee2b7-4b3f-8161-b3dd-fbb0d0c97f7d")
        self.assertEqual(write["source_commit"], "f340e44d233881a7133a8ca11624ac47fc6070ec")
        self.assertEqual(write["source_sha256"], "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1")
        self.assertEqual(write["mutation"], "replace_page_content")
        self.assertTrue(write["preserve_child_pages"])
        self.assertEqual(write["archived_top_level_blocks"], 192)
        self.assertEqual(write["appended_blocks"], 235)
        self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertEqual(mirror_task["id"], "MIRROR-STEP-03C-DALGEBRA-NOTION-001")
        self.assertEqual(mirror_task["status"], "ACCEPTED")

    def test_step_3d_write_only_mirror_receipt(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        mirror_task = json.loads(
            (ROOT / "tasks/archive/MIRROR-STEP-03D-NOTION-001.yaml").read_text(encoding="utf-8")
        )
        page = next(
            item
            for item in page_map["pages"]
            if item["id"] == "FOUNDATION-N1-SUPERFIELD-PATH-INTEGRAL-BV-BRST-003D"
        )
        write = next(
            item
            for item in receipt["pages"]
            if item["id"] == "FOUNDATION-N1-SUPERFIELD-PATH-INTEGRAL-BV-BRST-003D"
        )
        self.assertEqual(page["source_commit"], "218c043b7d0a10b54464d46a42d4732d6ab6b8ac")
        self.assertEqual(page["source_sha256"], "109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538")
        self.assertEqual(page["notion_page_id"], "39aee2b7-4b3f-8126-881c-ec4d32b780de")
        self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertEqual(mirror_task["id"], "MIRROR-STEP-03D-NOTION-001")
        self.assertEqual(mirror_task["status"], "ACCEPTED")

    def test_step_4_write_only_mirror_receipt(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        mirror_task = json.loads(
            (ROOT / "tasks/archive/MIRROR-STEP-04-NOTION-001.yaml").read_text(
                encoding="utf-8"
            )
        )
        expected = {
            "FOUNDATION-EXTENDED-SYM-NOTATION-004": (
                "contracts/foundations/step-04-extended-sym-notation.md",
                "a3d7791c0469051f21471f5f5c40c97f6aef1cff",
                "3fcf7e242928d3512c02059d8c28d9551b5cb86156f9d6259cd2bba713211d27",
                "39bee2b7-4b3f-8173-949c-dead35930a41",
            ),
            "FOUNDATION-N1-SUPER-YANG-MILLS-004A": (
                "contracts/foundations/step-04a-n1-super-yang-mills.md",
                "a3d7791c0469051f21471f5f5c40c97f6aef1cff",
                "b2495f6a98c8cffe21ab2583b1955c81f5bb06af9b0edfb677fc0a3a3ee1fbc1",
                "39bee2b7-4b3f-8102-8acd-c94d11c92963",
            ),
            "FOUNDATION-N2-SUPER-YANG-MILLS-004B": (
                "contracts/foundations/step-04b-n2-super-yang-mills.md",
                "ee5cf4ef77757c2ab44cfe4a95528b88b12bc1cd",
                "590bff04a31f2790ec97226570df189647f822b69c53ee9b141f5c1a0c98c860",
                "39bee2b7-4b3f-8188-bfb0-f7bb9f1d6d0f",
            ),
            "FOUNDATION-N4-SUPER-YANG-MILLS-004C": (
                "contracts/foundations/step-04c-n4-super-yang-mills.md",
                "ee5cf4ef77757c2ab44cfe4a95528b88b12bc1cd",
                "fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f",
                "39bee2b7-4b3f-81ee-ad8d-ec5b838fa90d",
            ),
            "CONTRACT-STEP-04-EXTENDED-SYM-DICTIONARY-001": (
                "contracts/dictionaries/step-04-extended-sym-weinberg-srednicki-dictionary.md",
                "a3d7791c0469051f21471f5f5c40c97f6aef1cff",
                "0909093c4afa22d5d8ae9c540880a524e57353c573795bf1937de1cfdcdd0a7b",
                "39bee2b7-4b3f-8150-a227-dd76caa48008",
            ),
        }
        for page_id, (source, commit, digest, notion_page_id) in expected.items():
            page = next(item for item in page_map["pages"] if item["id"] == page_id)
            write = next(item for item in receipt["pages"] if item["id"] == page_id)
            self.assertEqual(page["source"], source)
            self.assertEqual(page["source_commit"], commit)
            self.assertEqual(page["source_sha256"], digest)
            self.assertEqual(page["notion_page_id"], notion_page_id)
            self.assertEqual(write["source_commit"], commit)
            self.assertEqual(write["source_sha256"], digest)
            self.assertEqual(write["page_id"], notion_page_id)
            self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertEqual(mirror_task["id"], "MIRROR-STEP-04-NOTION-001")
        self.assertEqual(mirror_task["status"], "ACCEPTED")

    def test_step5a_write_only_mirror_receipt(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        task_path = ROOT / "tasks/archive/MIRROR-STEP-05A-NOTION-001.yaml"
        mirror_task = json.loads(task_path.read_text(encoding="utf-8"))
        ledger = json.loads((ROOT / "ledger/proof_obligations.json").read_text(encoding="utf-8"))

        page_id = "FOUNDATION-COMPONENT-BV-BRST-PRIMITIVE-SUPERGRAPH-GRAMMAR-005A"
        page = next(item for item in page_map["pages"] if item["id"] == page_id)
        write = next(item for item in receipt["pages"] if item["id"] == page_id)
        self.assertEqual(
            page["source"],
            "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md",
        )
        self.assertEqual(page["source_commit"], "ee5cf4ef77757c2ab44cfe4a95528b88b12bc1cd")
        self.assertEqual(
            page["source_sha256"],
            "300d55a07534a312bfad582c6702ba1991ef7e439a3b999c4c228c1329ca05bc",
        )
        self.assertEqual(page["notion_page_id"], "39dee2b7-4b3f-8113-8e71-ee71eeeef23b")
        self.assertEqual(write["page_id"], page["notion_page_id"])
        self.assertEqual(write["mutation"], "create_pages_then_replace_page_content")
        self.assertEqual(write["appended_blocks"], 197)
        self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertFalse(receipt["central_log_write"]["content_readback_performed"])
        self.assertEqual(receipt["central_log_write"]["write_response"], "succeeded")

        self.assertEqual(mirror_task["id"], "MIRROR-STEP-05A-NOTION-001")
        self.assertEqual(mirror_task["status"], "ACCEPTED")
        obligation = next(
            item
            for item in ledger["proof_obligations"]
            if item["id"] == "MIRROR-STEP-05A-NOTION-001"
        )
        self.assertEqual(obligation["state"], "ACCEPTED")
        self.assertEqual(
            obligation["task_sha256"],
            hashlib.sha256(task_path.read_bytes()).hexdigest(),
        )

    def test_step_3d_path_integral_bv_brst_contract(self) -> None:
        path = ROOT / "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md"
        if not path.exists():
            self.skipTest("Step 3D path-integral/BV-BRST contract is not registered")
        text = path.read_text(encoding="utf-8")
        tags = re.findall(r"\\tag\{3D\.([^}]+)\}", text)
        self.assertEqual(len(tags), 222)
        self.assertEqual(len(tags), len(set(tags)))
        self.assertEqual({tag for tag in tags if tag.isdigit()}, {str(value) for value in range(1, 135)})
        self.assertEqual(sum(not tag.isdigit() for tag in tags), 88)
        self.assertEqual(len(re.findall(r"\$\$\n.*?\n\$\$", text, re.DOTALL)), 222)
        self.assertIn(
            re.sub(r"\s+", "", r"\mathbf s_R F=(S_{\min,R},F)_R"),
            re.sub(r"\s+", "", text),
        )
        self.assertIn(r"X^\star_{\rmBV}=X^{\star{\rmext}}-", re.sub(r"\s+", "", text))
        self.assertIn(r"\widehat{\boldsymbol\varpi}_{\rmext,R,\nu}^{\,1/2}", re.sub(r"\s+", "", text))
        self.assertIn(r"(F,G)_{\rm1PI,int,R,\nu}", re.sub(r"\s+", "", text))
        self.assertIn(r"\mathfrakO_{R,\nu}^{\rm1PI,u}", re.sub(r"\s+", "", text))
        self.assertIn(r"M_{\nu,\rmint}^{\rmW,\perp}", re.sub(r"\s+", "", text))
        self.assertNotIn(r"\Gamma", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\t")

    def test_step_3d_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step3d_path_integral_bv_brst.py"
        audit_path = ROOT / "audits/step3d-path-integral-bv-brst-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Step 3D exact verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"exact_checks": 183, "failed_checks": 0})
        self.assertTrue(all(item["failed"] == 0 for item in audit["categories"].values()))

    def test_step_3d_audits(self) -> None:
        for relative in (
            "audits/step3d-gap-audit.json",
            "audits/step3d-notation-ledger.json",
            "audits/step3d-independent-review.json",
        ):
            path = ROOT / relative
            if not path.exists():
                self.skipTest(f"{relative} is not registered")
            audit = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(audit["result"], "PASS")
            self.assertEqual(audit["post_resolution"]["P0"], [])
            self.assertEqual(audit["post_resolution"]["P1"], [])

    def test_step_4_formula_surfaces(self) -> None:
        surfaces = {
            "contracts/foundations/step-04-extended-sym-notation.md": (
                "4.",
                52,
                (
                    r"[T_A,T_B]=ic_{AB}{}^CT_C",
                    r"\llbracket X,Y\rrbracket^A&:=ic_{BC}{}^AX^BY^C",
                    r"Y_{11}:=-\sqrt2F",
                    r"\varphi^{r4}:=\phi_r",
                    r"\mathsf N_{\rm PL}",
                    r"\mathcal R_{{\rm PR},\mathsf s}^{\Xi}",
                    r"\mathcal A_{\rm univ}^{R}",
                    r"\iota_R\!\left(\llbracket U,V\rrbracket\right)",
                    r"\mathcal D_{[M}F_{NP]}&=0",
                ),
            ),
            "contracts/foundations/step-04a-n1-super-yang-mills.md": (
                "4A.",
                57,
                (
                    r"S_L^{(1)}",
                    r"S_E^{(1)}",
                    r"\mathcal L_{L,{\rm compact}}^{(1)}",
                    r"\partial_\mu j_{L,a}^\mu",
                ),
            ),
            "contracts/foundations/step-04b-n2-super-yang-mills.md": (
                "4B.",
                112,
                (
                    r"S_L^{(2)}",
                    r"S_E^{(2)}",
                    r"Y_{ij}",
                    r"j_{L,ia}^{\mu}",
                    r"\mathsf A_{\rm PL}",
                    r"(-\sqrt2,-\sqrt2,i,-1,1,-i,-2i,+2i)",
                    r"\mathscr S_{\rm free}^{L,E}",
                    r"\mathscr S_{\rm int}^{L}",
                    r"\mathscr R_R[\mathcal D_MX]",
                    r"N_{\rm free\text{-}bind}^{L+E}&=1156",
                    r"A_r^{\rm internal}=A_{E,r+1}",
                    r"\operatorname{ev}_{\mathfrak g}",
                    r"PASS\_EXACT\_GENERAL\_LIE\_CLOSURE",
                ),
            ),
            "contracts/foundations/step-04c-n4-super-yang-mills.md": (
                "4C.",
                111,
                (
                    r"S_L^{(4)}",
                    r"S_E^{(4)}",
                    r"\boxed{u=-\sqrt2.}",
                    r"j_{L,a\mathcal I}^{\mu}",
                    r"-i\bar\varepsilon_{\mathcal I}\bar\sigma_{L,\mu}",
                    r"+\widetilde\varepsilon_{\mathcal I}\bar\sigma_{E,m}",
                ),
            ),
        }
        all_tags: list[str] = []
        for relative, (prefix, minimum_tags, required) in surfaces.items():
            path = ROOT / relative
            self.assertTrue(path.is_file(), relative)
            text = path.read_text(encoding="utf-8")
            tags = re.findall(r"\\tag\{([^}]+)\}", text)
            self.assertGreaterEqual(len(tags), minimum_tags, relative)
            self.assertEqual(len(tags), len(set(tags)), relative)
            self.assertTrue(all(tag.startswith(prefix) for tag in tags), relative)
            all_tags.extend(tags)
            for formula in required:
                self.assertIn(formula, text, f"{relative}: {formula}")
            self.assertEqual(text.count("$$") % 2, 0, relative)
            self.assertNotIn(r"\sim", text, relative)
            self.assertNotIn(r"\approx", text, relative)
            self.assertNotIn(r"\propto", text, relative)
            for character in text:
                self.assertFalse(
                    ord(character) < 32 and character not in "\n\t",
                    relative,
                )
        self.assertEqual(len(all_tags), len(set(all_tags)))

    def test_step_4_extended_sym_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_step4_extended_sym.py"
        audit_path = ROOT / "audits/step4-extended-sym-verification.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script), "--write-audit"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["failure_count"], 0)
        self.assertEqual(audit["failures"], [])
        self.assertEqual(audit["checks"]["lorentz_clifford"]["failures"], [])
        self.assertEqual(audit["checks"]["sigma_triple_identity"]["failure_count"], 0)
        self.assertEqual(audit["checks"]["bar_sigma_triple_identity"]["failure_count"], 0)
        self.assertEqual(audit["checks"]["two_spinor_schouten"]["failure_count"], 0)
        self.assertEqual(audit["checks"]["su4_rho_identities"]["failure_count"], 0)
        self.assertEqual(audit["checks"]["n4_divergence_wick_coefficients"]["failure_count"], 0)
        self.assertEqual(
            audit["checks"]["n4_fermion_closure_eom_reduction"]["failure_count"],
            0,
        )

    def test_step_4_n2_closure_verifier(self) -> None:
        script = ROOT / "scripts/verify_step4_n2_closure.py"
        audit_path = ROOT / "audits/step4-n2-closure-verification.json"
        self.assertTrue(script.is_file())
        self.assertTrue(audit_path.is_file())
        expected = audit_path.read_text(encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(script), "--write-audit"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        task = json.loads(
            (
                ROOT
                / "tasks/archive/CONTRACT-STEP-04-EXTENDED-SUPER-YANG-MILLS-001.yaml"
            ).read_text(encoding="utf-8")
        )
        admission = task["general_lie_reference_admission"]
        self.assertEqual(admission["source_id"], "N2-GENERAL-LIE-CLOSURE-INSTRUCTOR-MD")
        self.assertEqual(
            admission["admitted_claim_ids"],
            [
                "N2-GENERAL-LIE-PRIMITIVE-CLOSURE-CANDIDATE",
                "N2-GENERAL-LIE-FUNCTORIAL-LIFT-CANDIDATE",
                "N2-GENERAL-LIE-VERIFIER-DESIGN-CANDIDATE",
            ],
        )
        self.assertEqual(
            admission["rejected_claim_id"],
            "N2-GENERAL-LIE-COMPLETENESS-CANDIDATE",
        )
        self.assertEqual(
            admission["rejection"],
            "CIRCULAR_UNTIL_ALL_PRIMITIVE_RESIDUALS_ARE_DIRECTLY_ZERO",
        )
        self.assertEqual(audit["status"], "PASS_EXACT_GENERAL_LIE_CLOSURE")
        self.assertEqual(audit["failure_count"], 0)
        self.assertEqual(audit["failures"], [])
        self.assertTrue(audit["nonabelian_full_covariant_closure_claimed"])
        self.assertTrue(
            audit[
                "complete_checked_scope_offshell_su2_r_intertwiner_claimed"
            ]
        )
        for name in (
            "lorentz_free_all_field_closure",
            "euclidean_free_all_field_closure",
            "constant_su2_nonabelian_interaction_closure",
            "simultaneous_nonlinear_coefficient_solution",
            "omega_sign_and_normalization_solution",
            "graded_normal_ordering_identity",
            "offshell_su2_r_lie_free_lorentz_intertwiner",
            "offshell_su2_r_lie_free_euclidean_intertwiner",
            "offshell_su2_r_lie_interaction_intertwiner",
            "offshell_su2_r_triplet_gate",
            "offshell_su2_r_quarter_turn_free_lorentz_regression",
            "offshell_su2_r_quarter_turn_free_euclidean_regression",
            "offshell_su2_r_quarter_turn_interaction_regression",
        ):
            check = audit["checks"][name]
            self.assertTrue(check["passed"], name)
            self.assertEqual(check["residual_count"], 0, name)

        normal_order = audit["checks"]["graded_normal_ordering_identity"]
        self.assertEqual(normal_order["checked_components"], 32)
        self.assertEqual(
            normal_order["identity"],
            "barepsilon barsigma^M psi=-(psi sigma^M barepsilon)",
        )

        gate = audit["checks"]["offshell_su2_r_triplet_gate"]
        self.assertEqual(
            gate["derived_exact_coefficients"]["residual_coefficient_of_s"],
            "0",
        )
        self.assertEqual(
            gate["derived_exact_coefficients"]["order_covariance_residual"],
            "0",
        )
        self.assertEqual(
            gate["derived_exact_coefficients"]["gamma_c_over_s_parameter_left"],
            "-i",
        )
        self.assertEqual(
            gate["derived_exact_coefficients"]["gamma_c_over_s_field_left"],
            "-i",
        )
        self.assertEqual(gate["conclusion"], "dual-order manifest-slot compatibility")

        generator_basis = [
            "t1=i*sigma1/2",
            "t2=i*sigma2/2",
            "t3=i*sigma3/2",
        ]
        for signature in ("lorentz", "euclidean"):
            lie = audit["checks"][
                f"offshell_su2_r_lie_free_{signature}_intertwiner"
            ]
            self.assertEqual(lie["generator_basis"], generator_basis)
            self.assertEqual(lie["parameter_copies"], [1, 2])
            self.assertEqual(lie["checked_matrix_cells"], 1734)
            self.assertEqual(lie["residual_monomial_count"], 0)

        interaction = audit["checks"][
            "offshell_su2_r_lie_interaction_intertwiner"
        ]
        self.assertEqual(interaction["generator_basis"], generator_basis)
        self.assertEqual(interaction["parameter_copies"], [1, 2])
        self.assertEqual(interaction["checked_object_color_slots"], 396)
        self.assertEqual(interaction["checked_triplet_reconstruction_slots"], 27)
        self.assertEqual(interaction["residual_monomial_count"], 0)
        for output in (
            "lambda0",
            "tlambda0",
            "psi0",
            "tpsi0",
            "Y11",
            "Y22",
            "Y12",
        ):
            self.assertIn(output, interaction["checked_outputs"])

        for signature in ("lorentz", "euclidean"):
            binding = audit["checks"][f"universal_abelian_roundtrip_{signature}"]
            self.assertTrue(binding["passed"])
            self.assertEqual(binding["checked_cell_bindings"], 578)
            self.assertEqual(binding["nonzero_source_cells"], 224)
            self.assertEqual(binding["nonzero_roundtrip_cells"], 224)
            self.assertEqual(binding["residual_count"], 0)

            direct = audit["checks"][f"universal_direct_general_lie_closure_{signature}"]
            self.assertTrue(direct["passed"])
            self.assertEqual(direct["primitive_residual_objects_checked"], 17)
            self.assertEqual(direct["derived_residual_objects_checked"], 5)
            self.assertEqual(direct["total_residual_objects_checked"], 22)
            self.assertEqual(direct["residual_object_count"], 0)
            self.assertEqual(direct["residual_monomial_count"], 0)
            self.assertEqual(direct["maximum_actual_term_count"], 392)
            self.assertEqual(direct["maximum_expected_term_count"], 392)
            self.assertEqual(direct["maximum_composed_word_length"], 3)
            self.assertEqual(direct["maximum_composed_jet_order"], 1)
            self.assertTrue(direct["direct_composition_used_for_every_object"])
            self.assertFalse(direct["recursion_used_to_infer_primitive_closure"])
            self.assertFalse(direct["finite_color_projection"])
            self.assertFalse(direct["structure_constants_instantiated"])
            self.assertIsNone(direct["truncation"])
            self.assertFalse(direct["pbw_word_order_reordered"])

        structural = audit["checks"]["universal_structural_identities"]
        self.assertTrue(structural["passed"])
        self.assertEqual(structural["checked_identity_count"], 284)
        self.assertEqual(
            structural["category_counts"],
            {
                "commuting_partial_jets": 12,
                "graded_jacobi": 8,
                "covariant_derivative_curvature": 12,
                "bianchi": 4,
                "variation_covariant_derivative_recursion": 208,
                "variation_curvature_recursion": 24,
                "variation_bracket_recursion": 16,
            },
        )
        self.assertTrue(all(value == 0 for value in structural["category_residual_counts"].values()))
        self.assertEqual(structural["residual_count"], 0)
        self.assertFalse(structural["finite_color_projection"])
        self.assertFalse(structural["structure_constants_instantiated"])
        self.assertIsNone(structural["truncation"])
        self.assertFalse(structural["pbw_word_order_reordered"])
        exact_counts = audit["checks"]["universal_gate_exact_counts"]
        self.assertTrue(exact_counts["passed"])
        self.assertEqual(exact_counts["abelian_roundtrip_bindings"], 1156)
        self.assertEqual(exact_counts["direct_object_residuals"], 44)
        universal_surface = json.dumps(
            {
                "lorentz": audit["checks"]["universal_direct_general_lie_closure_lorentz"],
                "euclidean": audit["checks"]["universal_direct_general_lie_closure_euclidean"],
                "structural": structural,
            },
            sort_keys=True,
        )
        self.assertNotIn("epsilon_AB", universal_surface)
        self.assertNotIn("fixed three-color", universal_surface)

    def test_step_4_dictionary_surface(self) -> None:
        path = ROOT / "contracts/dictionaries/step-04-extended-sym-weinberg-srednicki-dictionary.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        tags = re.findall(r"\\tag\{(D4\.[^}]+)\}", text)
        self.assertGreaterEqual(len(tags), 12)
        self.assertEqual(len(tags), len(set(tags)))
        self.assertIn("Project--Srednicki--Weinberg", text)
        self.assertIn("SOURCE_INSUFFICIENT", text)
        self.assertIn("NOT_DEFINED_IN_SOURCE", text)
        self.assertIn("PASS_EXACT_GENERAL_LIE_CLOSURE", text)
        self.assertNotIn("UNVERIFIED_GENERAL_LIE_CLOSURE", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)
        self.assertNotIn(r"\propto", text)
        for character in text:
            self.assertFalse(ord(character) < 32 and character not in "\n\r\t")

    def test_step_4_audits(self) -> None:
        expected = {
            "audits/step4-gap-audit.json": ("PASS", []),
            "audits/step4-independent-review.json": ("PASS", []),
            "audits/step4-notation-ledger.json": ("PASS", []),
            "audits/step4-dictionary-review.json": ("PASS", []),
        }
        for relative, (result, p1_findings) in expected.items():
            path = ROOT / relative
            self.assertTrue(path.is_file(), relative)
            audit = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(audit["result"], result, relative)
            self.assertEqual(audit["post_resolution"]["P0"], [], relative)
            self.assertEqual(
                audit["post_resolution"]["P1"],
                p1_findings,
                relative,
            )

    def test_weinberg_srednicki_section_verdicts(self) -> None:
        path = ROOT / "audits/ws-dictionary/draft-section-verdicts.json"
        if not path.exists():
            self.skipTest("Weinberg-Srednicki section audit is not registered")
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["result"], "PASS")
        self.assertEqual(audit["section_range"], {"first": 0, "last": 54, "count": 55})
        self.assertEqual([item["section"] for item in audit["sections"]], list(range(55)))
        allowed = {"VERIFIED", "CORRECTED", "FALSE", "NOT_IN_SCOPE", "SOURCE_INSUFFICIENT"}
        self.assertTrue(all(item["status"] in allowed for item in audit["sections"]))
        self.assertTrue(all(item["citations"] for item in audit["sections"]))
        for source in audit["source_registry"].values():
            self.assertTrue((ROOT / source["path"]).is_file(), source["path"])
            if source["source"] in {"WEINBERG", "SREDNICKI"}:
                self.assertEqual(source["url"], f"https://app.notion.com/p/{source['page_id']}")

    def test_weinberg_srednicki_exact_verifier(self) -> None:
        script = ROOT / "scripts/verify_ws_notation_dictionary.py"
        audit_path = ROOT / "audits/ws-dictionary/exact-verification.json"
        if not script.exists() or not audit_path.exists():
            self.skipTest("Weinberg-Srednicki exact verifier is not registered")
        expected = audit_path.read_text(encoding="utf-8")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        self.assertEqual(audit_path.read_text(encoding="utf-8"), expected)
        audit = json.loads(expected)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["checks"], 1953)
        self.assertEqual(audit["totals"]["failed"], 0)
        for name in (
            "gamma5_phase",
            "weinberg_fierz_0_0",
            "srednicki_fierz_3_3",
            "exterior_covariant_D_identity_0",
            "exterior_srednicki_Q_bracket_1_1",
            "exterior_chiral_coordinate_3_1",
            "superspace_chiral_coordinate_bridge_3",
            "superspace_D_grassmann_factor",
            "superspace_chiral_fermion_contraction",
        ):
            self.assertTrue(audit["checks"][name], name)

    def test_weinberg_srednicki_independent_review(self) -> None:
        path = ROOT / "audits/ws-dictionary/independent-review.json"
        if not path.exists():
            self.skipTest("Weinberg-Srednicki independent review is not registered")
        review = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(review["result"], "PASS")
        self.assertEqual(review["post_resolution"], {"P0": [], "P1": []})
        self.assertTrue(all(item["status"] == "RESOLVED" for item in review["resolved_findings"]))
        self.assertEqual(review["exact_verification"], {"checks": 1953, "failed": 0, "status": "PASS"})
        self.assertEqual(
            review["section_verdicts"],
            {"first": 0, "last": 54, "count": 55, "status": "PASS"},
        )

    def test_no_absolute_user_paths_in_authority_surface(self) -> None:
        roots = [
            ROOT / "AUTHORITY.md",
            ROOT / "AGENTS.md",
            ROOT / "contracts",
            ROOT / "channels",
            ROOT / "tasks",
            ROOT / "ledger",
            ROOT / "mirror",
            ROOT / "scripts",
        ]
        for root in roots:
            paths = (
                [root]
                if root.is_file()
                else [
                    path
                    for path in root.rglob("*")
                    if path.is_file()
                    and "__pycache__" not in path.parts
                    and path.suffix != ".pyc"
                ]
            )
            for path in paths:
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("/Users/", text, str(path))

    def test_channel_sources_do_not_cross_read(self) -> None:
        channels = ("ec", "es", "lc", "ls")
        for channel in channels:
            base = ROOT / "channels" / channel
            for path in list((base / "src").rglob("*")) + list((base / "tests").rglob("*")):
                if not path.is_file():
                    continue
                text = path.read_text(encoding="utf-8")
                for other in channels:
                    if other != channel:
                        self.assertNotIn(f"channels/{other}", text, str(path))


if __name__ == "__main__":
    unittest.main()
