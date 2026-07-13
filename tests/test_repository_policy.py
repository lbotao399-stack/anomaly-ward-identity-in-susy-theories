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
        self.assertEqual(task["status"], "SPECIFIED")
        self.assertTrue(task["reference_admission"]["source_translation_required_before_formula_adoption"])
        self.assertEqual(len(task["acceptance"]), 23)
        self.assertTrue(any("5A PERTURBATIVE_FF_DRED_SUPERGRAPHS" in item for item in task["acceptance"]))
        self.assertTrue(any("primitive WW" in item for item in task["acceptance"]))
        self.assertTrue(any("external-leg" in item for item in task["acceptance"]))
        self.assertTrue(any("Q(i,sqrt2)" in item for item in task["acceptance"]))
        self.assertTrue(any("automorphism order is an audit" in item for item in task["acceptance"]))
        self.assertTrue(any("finite critical-pair suite" in item for item in task["acceptance"]))
        self.assertTrue(any("isolated triangle" in item for item in task["forbidden_inputs"]))

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
        self.assertIn(r"\mathsf V:=\text{gauge-vector frame}", text)
        self.assertIn(r"\mathsf C:=\text{gauge-chiral frame}", text)
        self.assertIn(r"\mathsf A:=\text{gauge-antichiral frame}", text)
        self.assertIn(r"\rho_R:=\frac4{\kappa_R^2}", text)
        self.assertIn(r"\xi_Ac_{BC}{}^A=0", text)
        self.assertIn(r"\widetilde{\mathcal B}_R\mathcal B_R", text)
        self.assertIn(r"\boldsymbol\nabla_R^{\mathsf V a}", text)
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
        self.assertEqual(audit["totals"]["exact_checks"], 106)
        self.assertEqual(audit["totals"]["failed_checks"], 0)
        self.assertTrue(all(item["failed"] == 0 for item in audit["categories"].values()))

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
            (ROOT / "tasks/archive/MIRROR-STEP-03C-NOTION-001.yaml").read_text(encoding="utf-8")
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
        self.assertEqual(page["source_commit"], "fe4b80a9478a4ad0bdd63c614c0d1a1f4b1cd5f0")
        self.assertEqual(page["source_sha256"], "90e5211557e0a12e444ee91a174beaf7ddea9039e6f9b987eb0861f0a9ef2461")
        self.assertEqual(page["notion_page_id"], "39aee2b7-4b3f-8161-b3dd-fbb0d0c97f7d")
        self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertEqual(mirror_task["id"], "MIRROR-STEP-03C-NOTION-001")
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
                "3fcf7e242928d3512c02059d8c28d9551b5cb86156f9d6259cd2bba713211d27",
                "39bee2b7-4b3f-8173-949c-dead35930a41",
            ),
            "FOUNDATION-N1-SUPER-YANG-MILLS-004A": (
                "contracts/foundations/step-04a-n1-super-yang-mills.md",
                "b2495f6a98c8cffe21ab2583b1955c81f5bb06af9b0edfb677fc0a3a3ee1fbc1",
                "39bee2b7-4b3f-8102-8acd-c94d11c92963",
            ),
            "FOUNDATION-N2-SUPER-YANG-MILLS-004B": (
                "contracts/foundations/step-04b-n2-super-yang-mills.md",
                "c8c46744d2c41880bf145d8d6c90af25555276650cc036ded8ddbda9071870d3",
                "39bee2b7-4b3f-8188-bfb0-f7bb9f1d6d0f",
            ),
            "FOUNDATION-N4-SUPER-YANG-MILLS-004C": (
                "contracts/foundations/step-04c-n4-super-yang-mills.md",
                "9fb057d14ee438b31d3f38836e8ca848dfee74b1ea363716222264c96405e5db",
                "39bee2b7-4b3f-81ee-ad8d-ec5b838fa90d",
            ),
            "CONTRACT-STEP-04-EXTENDED-SYM-DICTIONARY-001": (
                "contracts/dictionaries/step-04-extended-sym-weinberg-srednicki-dictionary.md",
                "0909093c4afa22d5d8ae9c540880a524e57353c573795bf1937de1cfdcdd0a7b",
                "39bee2b7-4b3f-8150-a227-dd76caa48008",
            ),
        }
        for page_id, (source, digest, notion_page_id) in expected.items():
            page = next(item for item in page_map["pages"] if item["id"] == page_id)
            write = next(item for item in receipt["pages"] if item["id"] == page_id)
            self.assertEqual(page["source"], source)
            self.assertEqual(page["source_commit"], "a3d7791c0469051f21471f5f5c40c97f6aef1cff")
            self.assertEqual(page["source_sha256"], digest)
            self.assertEqual(page["notion_page_id"], notion_page_id)
            self.assertEqual(write["page_id"], notion_page_id)
            self.assertEqual(write["write_response"], "succeeded")
        self.assertFalse(receipt["content_readback_performed"])
        self.assertEqual(mirror_task["id"], "MIRROR-STEP-04-NOTION-001")
        self.assertEqual(mirror_task["status"], "ACCEPTED")

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
