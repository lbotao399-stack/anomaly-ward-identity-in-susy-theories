from __future__ import annotations

import ast
import json
from pathlib import Path
import tempfile
import unittest

from scripts.step6_external_target_firewall import (
    DENIED_ROOTS,
    STATUS,
    artifact_violations,
    build_firewall,
    digest,
    review_ledger,
    sha256_bytes,
    source_violations,
)


ROOT = Path(__file__).resolve().parents[1]


class Step6ExternalTargetFirewallTest(unittest.TestCase):
    def test_live_firewall_passes(self) -> None:
        payload = build_firewall(ROOT)
        self.assertEqual(payload["status"], STATUS)
        self.assertEqual(payload["violations"], [])
        self.assertTrue(payload["denied_input_ledger"])
        self.assertTrue(all(payload["checks"].values()))
        self.assertIsNone(payload["calculation_result"])
        self.assertIsNone(payload["anomaly_coefficient"])

    def test_review_ledger_hashes_every_denied_file_exactly(self) -> None:
        records = review_ledger(ROOT)
        paths = {record["path"] for record in records}
        expected = {
            path.relative_to(ROOT).as_posix()
            for denied_root in DENIED_ROOTS
            for path in (ROOT / denied_root).rglob("*")
            if path.is_file()
        }
        self.assertEqual(paths, expected)
        for record in records:
            payload = (ROOT / record["path"]).read_bytes()
            self.assertEqual(record["sha256"], sha256_bytes(payload))
            self.assertEqual(record["byte_count"], len(payload))

    def test_derivation_sources_do_not_name_review_paths_or_target_ids(self) -> None:
        self.assertEqual(source_violations(ROOT), [])

    def test_artifacts_do_not_copy_or_declare_review_hashes(self) -> None:
        reviews = review_ledger(ROOT)
        self.assertEqual(artifact_violations(ROOT, reviews), [])

    def test_artifact_copy_and_declared_hash_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            review = root / "tasks" / "reviews" / "target.md"
            review.parent.mkdir(parents=True)
            review.write_text("private-target-payload", encoding="utf-8")
            generated = root / "generated" / "step6" / "two-loop-graphir"
            generated.mkdir(parents=True)
            copied = generated / "copied.json"
            copied.write_bytes(review.read_bytes())
            declared = generated / "declared.json"
            review_hash = sha256_bytes(review.read_bytes())
            declared.write_text(json.dumps({"dependency": review_hash}), encoding="utf-8")
            failures = artifact_violations(root, review_ledger(root))
            self.assertIn("EXACT_DENIED_FILE_HASH", {item["token"] for item in failures})
            self.assertIn(
                "DECLARED_DENIED_DEPENDENCY_HASH",
                {item["token"] for item in failures},
            )

    def test_python_ast_parser_covers_concatenated_literals(self) -> None:
        tree = ast.parse("value = 'tasks/' 'reviews'\n")
        constants = [
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        ]
        self.assertEqual(constants, ["tasks/reviews"])

    def test_firewall_hash_is_recomputable(self) -> None:
        payload = build_firewall(ROOT)
        stored = payload.pop("firewall_hash")
        self.assertEqual(stored, digest(payload))

    def test_external_target_is_hashed_and_comparison_only(self) -> None:
        manifest = json.loads((ROOT / "references/manifest.yaml").read_text())
        entries = {entry["id"]: entry for entry in manifest["entries"]}
        target = entries["STEP6-HOLOMORPHIC-Q2-TARGET-LEDGER"]
        target_path = ROOT / target["path"]
        self.assertEqual(
            target["classification"],
            "EXTERNAL_TARGET_COMPARISON_ONLY_NOT_DERIVATION",
        )
        self.assertEqual(target["sha256"], sha256_bytes(target_path.read_bytes()))

        claim_map = json.loads((ROOT / "references/claim-map.yaml").read_text())
        claims = {claim["id"]: claim for claim in claim_map["claims"]}
        claim = claims["STEP6-HOLOMORPHIC-Q2-EXTERNAL-TARGET"]
        self.assertEqual(claim["sources"], ["STEP6-HOLOMORPHIC-Q2-TARGET-LEDGER"])
        self.assertIn("after", claim["allowed_use"].casefold())
        self.assertIn("frozen", claim["allowed_use"].casefold())
        for stage in ("wick", "d-algebra", "r-operation", "ibp"):
            self.assertIn(stage, claim["forbidden_use"].casefold())


if __name__ == "__main__":
    unittest.main()
