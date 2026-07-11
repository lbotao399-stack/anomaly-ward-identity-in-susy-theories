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
        for obligation in obligations["proof_obligations"]:
            packet = json.loads((ROOT / obligation["task"]).read_text(encoding="utf-8"))
            self.assertEqual(packet["id"], obligation["id"])

    def test_reference_import_has_narrow_acquisition_scope(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        if task["type"] != "REFERENCE_IMPORT":
            self.skipTest("current task is not a reference import")
        urls = [item for item in task["allowed_inputs"] if item.startswith("https://")]
        self.assertEqual(
            urls,
            [
                "https://arxiv.org/abs/hep-th/0108200",
                "https://arxiv.org/abs/hep-th/9808041",
                "https://arxiv.org/abs/hep-th/9903230",
            ],
        )

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
