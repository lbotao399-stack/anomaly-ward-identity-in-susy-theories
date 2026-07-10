from __future__ import annotations

import hashlib
import json
import re
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

    def test_notion_is_output_only(self) -> None:
        page_map = json.loads((ROOT / "mirror/page_map.yaml").read_text(encoding="utf-8"))
        self.assertEqual(page_map["direction"], "GIT_TO_NOTION_ONLY")
        self.assertEqual(page_map["notion_content_read_policy"], "FORBIDDEN")
        receipt = json.loads((ROOT / "audits/notion_write_receipt.json").read_text(encoding="utf-8"))
        self.assertFalse(receipt["content_readback_performed"])

    def test_authority_repair_is_accepted(self) -> None:
        task = json.loads((ROOT / "tasks/CURRENT.yaml").read_text(encoding="utf-8"))
        quarantine = json.loads((ROOT / "audits/legacy_quarantine.json").read_text(encoding="utf-8"))
        protection = json.loads((ROOT / "audits/branch_protection.json").read_text(encoding="utf-8"))
        self.assertEqual(task["id"], "AUTHORITY-REPAIR-001")
        self.assertEqual(task["status"], "ACCEPTED")
        self.assertEqual(quarantine["action"], "ARCHIVE_NOT_DELETE")
        self.assertFalse(quarantine["content_imported"])
        self.assertEqual(len(quarantine["repositories"]), 4)
        self.assertTrue(all(item["archived"] for item in quarantine["repositories"]))
        self.assertEqual(protection["blocker"], "BLOCKED_GITHUB_PLAN_BRANCH_PROTECTION")
        self.assertEqual(protection["replacement_gate"], "origin/main commit plus successful verify workflow")

    def test_step_1_formula_surface(self) -> None:
        text = (ROOT / "contracts/foundations/step-01-supersymmetry-commutator.md").read_text(encoding="utf-8")
        tags = {int(value) for value in re.findall(r"\\tag\{1\.(\d+)\}", text)}
        self.assertEqual(tags, set(range(1, 69)))
        self.assertIn(r"\{Q^L_a,\bar Q^L_{\dot b}\}", text)
        self.assertIn(r"Q^E_a=-iQ^L_a", text)
        self.assertIn(r"\{Q^E_a,\bar Q^E_{\dot b}\}", text)
        self.assertNotIn(r"\sim", text)
        self.assertNotIn(r"\approx", text)

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
