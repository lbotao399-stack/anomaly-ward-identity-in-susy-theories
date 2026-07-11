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
        self.assertEqual(audit["totals"], {"checks": 46, "failed": 0, "page_text_comparisons": 14})

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
        self.fail(f"unreviewed reference-import task: {task['id']}")

    def test_contract_change_has_no_network_inputs(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["type"] != "CONTRACT_CHANGE":
            self.skipTest("current task is not a contract change")
        self.assertFalse(any(item.startswith("http://") or item.startswith("https://") for item in task["allowed_inputs"]))
        for item in task["allowed_inputs"]:
            self.assertTrue((ROOT / item).exists(), item)

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
            paths = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file()]
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
