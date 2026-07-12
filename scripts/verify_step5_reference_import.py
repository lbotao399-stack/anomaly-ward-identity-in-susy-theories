#!/usr/bin/env python3
"""Exact verifier for the scoped Step-5 chat and Weinberg Chapter-30 import."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "REFERENCE-IMPORT-STEP5-CHAT-WEINBERG30-001"
BASE = ROOT / "references/vendor/chatgpt/6a53ea95-9138-83e8-9761-2e85a29c3970"
AUTH = BASE / "authenticated-visible.json"
SHARE = BASE / "share-visible.json"
TRANSCRIPT = BASE / "authenticated-visible.md"
COMPARISON = BASE / "comparison.json"
NOTION = ROOT / "references/vendor/notion/weinberg/chapter-30"
LEDGER = ROOT / "references/step5-chat-weinberg30-source-ledger.json"
MANIFEST = ROOT / "references/manifest.yaml"
CLAIM_MAP = ROOT / "references/claim-map.yaml"
TASK = ROOT / "tasks/CURRENT.yaml"
AUDIT = ROOT / "audits/step5-reference-import-verification.json"

AUTH_SHA = "0eba2b4e454b9ffe97f139b28bd94efc01643f55460dde6792fd05e2fcbcac7f"
SHARE_SHA = "987adb876381e5126682dab4c31f1de0cc9a511b6743b5d36f59102acce0a3fa"
TRANSCRIPT_SHA = "369c29f0092310d16a8392f23223de9cf0c9c8102c42e9a298f6dad2519aa7ce"
COMPARISON_SHA = "fcf34b7b96231ba8c7deefefac818d271a5bc0e9aad3d4db6db67f324344a321"
AUTH_TRANSCRIPT_SHA = "761d93838766f6b1502136f680615f8f26ec9eeba33d81fed44cc3bf7c6c6ff2"
SHARE_TRANSCRIPT_SHA = "1e9c4ca047b8af9e3359578631295c1b6844b500c833ce346881a5ae410b5dce"

AUTH_IDS = [
    "0b973267-f5e1-4a08-bd5c-548b91c646ea",
    "7af98f88-eda4-426f-b85d-eece9477a4af",
    "85f1987d-2b98-4202-b4ad-c35ae39a41ee",
    "1064c3f5-5760-4e0a-b400-311a968dd191",
    "d54b7adf-15f1-472b-9518-6347ee4b77aa",
    "0f6acae0-bd68-4fa5-874c-60dc2fb5fdbb",
    "e0aef8be-dd6b-4be5-88c4-113bb38fe8d8",
]
AUTH_ROLES = ["user", "assistant", "assistant", "user", "assistant", "user", "assistant"]
AUTH_TURNS = [1, 2, 8, 9, 10, 11, 12]
AUTH_FORMULAS = [0, 95, 173, 0, 186, 0, 19]
AUTH_MESSAGE_HASHES = [
    "400bb28a1be446bfddbb0dd98152929941114f7dc4b22488fb734840dfb75552",
    "4f7427e3ec0a5a54043dd5ebe59c5a75360c7c63d4b04f4ab3443ac8435984e7",
    "ad87f512c7e0f641080741184cded79843671c63ef3ed54f5f7fd0fbfbf5f565",
    "1364ad81082719121ad58afa0799b295e6a109849f25caea1bba2a88ced0363b",
    "8351d68bf40b88c34a7aa465df8c2533a7c87fca1b86f500d10f29b3af61b31a",
    "5e4190dba1473b13fec8dbbca339931d2eebe4676eafe7ea123604e6d03c236d",
    "1a960b1a88dd85ba8ea26ee428b00873861e94459732be6a5c53a379b978f002",
]

NOTION_PAGES = [
    {
        "id": "WEINBERG-NOTION-CHAPTER-30-INDEX",
        "page_id": "34cee2b74b3f81239f12c44eda7b664f",
        "title": "第 30 章 超图",
        "parent": "310ee2b74b3f8065a3acdbdac27f3b2b",
        "path": "chapter-30-index-34cee2b74b3f81239f12c44eda7b664f.md",
        "bytes": 1014,
        "lines": 20,
        "sha256": "bd4e5c578fa157daf4b5e41dfe482280bd059b359374fdaaaa405daf0a525405",
    },
    {
        "id": "WEINBERG-NOTION-30-01-POTENTIAL-SUPERFIELDS",
        "page_id": "34cee2b74b3f8182a114ff6b4b910489",
        "title": "30.1 势超场",
        "parent": "34cee2b74b3f81239f12c44eda7b664f",
        "path": "30-01-potential-superfields-34cee2b74b3f8182a114ff6b4b910489.md",
        "bytes": 9123,
        "lines": 149,
        "sha256": "c1bec1b653e08ae194d8d00a8f46cc1bedb8520347a57e64a7b0a19a2ce526fe",
    },
    {
        "id": "WEINBERG-NOTION-30-02-SUPERPROPAGATORS",
        "page_id": "34cee2b74b3f81359cb6e2419fe2f5f0",
        "title": "30.2 超传播子",
        "parent": "34cee2b74b3f81239f12c44eda7b664f",
        "path": "30-02-superpropagators-34cee2b74b3f81359cb6e2419fe2f5f0.md",
        "bytes": 17206,
        "lines": 265,
        "sha256": "a9d4eebc2397b5230329f9a19a1d59e2bad7f8fff6143d1c68840d0b149dee7e",
    },
    {
        "id": "WEINBERG-NOTION-30-03-CALCULATIONS-WITH-SUPERGRAPHS",
        "page_id": "34cee2b74b3f817499daf036a9bdca44",
        "title": "30.3 用超图进行计算",
        "parent": "34cee2b74b3f81239f12c44eda7b664f",
        "path": "30-03-calculations-with-supergraphs-34cee2b74b3f817499daf036a9bdca44.md",
        "bytes": 12982,
        "lines": 131,
        "sha256": "732ec39d572eec6037ade1dc8e319bd540a7ba5b868dbc980f240e9508d1357d",
    },
]

CLAIM_IDS = [
    "CHATGPT-STEP5-TRIANGLE-CALCULATION-CANDIDATE",
    "CHATGPT-STEP5-DRAW-MAP-DALGEBRA-WORKFLOW-CANDIDATE",
    "WEINBERG-CH30-SUPERGRAPH-STRUCTURE-CANDIDATE",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def content_fingerprint(message: dict[str, Any]) -> str:
    clean = copy.deepcopy(message)
    clean.pop("order", None)
    clean.pop("canonical_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[str] = []

    def check(self, name: str, actual: Any, expected: Any, category: str) -> None:
        passed = actual == expected
        self.checks.append({
            "name": name,
            "category": category,
            "passed": passed,
            "actual": actual,
            "expected": expected,
        })
        if not passed:
            self.failures.append(name)


def build_audit() -> dict[str, Any]:
    r = Recorder()
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    share = json.loads(SHARE.read_text(encoding="utf-8"))
    comparison = json.loads(COMPARISON.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    claim_map = json.loads(CLAIM_MAP.read_text(encoding="utf-8"))
    task = json.loads(TASK.read_text(encoding="utf-8"))

    for name, path, digest in (
        ("authenticated capture", AUTH, AUTH_SHA),
        ("share capture", SHARE, SHARE_SHA),
        ("mechanical transcript", TRANSCRIPT, TRANSCRIPT_SHA),
        ("dual-capture comparison", COMPARISON, COMPARISON_SHA),
    ):
        r.check(f"{name} sha256", sha256(path), digest, "chat_identity")

    am = auth["messages"]
    sm = share["messages"]
    r.check("authenticated declared message count", auth["message_count"], 7, "chat_structure")
    r.check("authenticated parsed message count", len(am), 7, "chat_structure")
    r.check("authenticated message ids", [m["message_id"] for m in am], AUTH_IDS, "chat_structure")
    r.check("authenticated roles", [m["role"] for m in am], AUTH_ROLES, "chat_structure")
    r.check(
        "authenticated turns",
        [int(m["conversation_turn"].removeprefix("conversation-turn-")) for m in am],
        AUTH_TURNS,
        "chat_structure",
    )
    r.check("authenticated order", [m["order"] for m in am], list(range(7)), "chat_structure")
    r.check("authenticated formula counts", [len(m["formulas"]) for m in am], AUTH_FORMULAS, "chat_structure")
    r.check("authenticated canonical hashes", [m["canonical_sha256"] for m in am], AUTH_MESSAGE_HASHES, "chat_structure")
    r.check("authenticated declared hash sequence", auth["message_hash_sequence"], AUTH_MESSAGE_HASHES, "chat_structure")
    r.check("authenticated transcript hash", auth["normalized_transcript_sha256"], AUTH_TRANSCRIPT_SHA, "chat_identity")
    r.check("share declared message count", share["message_count"], 5, "chat_structure")
    r.check("share parsed message count", len(sm), 5, "chat_structure")
    r.check("share ids are authenticated suffix", [m["message_id"] for m in sm], AUTH_IDS[2:], "chat_comparison")
    r.check("share roles are authenticated suffix", [m["role"] for m in sm], AUTH_ROLES[2:], "chat_comparison")
    r.check("share transcript hash", share["normalized_transcript_sha256"], SHARE_TRANSCRIPT_SHA, "chat_identity")
    r.check(
        "shared message content exact excluding capture order",
        [content_fingerprint(a) == content_fingerprint(s) for a, s in zip(am[2:], sm)],
        [True] * 5,
        "chat_comparison",
    )
    r.check(
        "comparison shared fingerprints",
        [row["content_sha256_without_capture_order"] for row in comparison["shared_messages"]],
        [content_fingerprint(m) for m in am[2:]],
        "chat_comparison",
    )
    r.check("comparison missing authenticated prefix", [x["message_id"] for x in comparison["missing_from_share"]], AUTH_IDS[:2], "chat_comparison")
    r.check("comparison verdict", comparison["cross_capture_checks"]["verdict"], "SHARED_CONTENT_IDENTICAL_SHARE_OMITS_AUTHENTICATED_PREFIX_2", "chat_comparison")

    transcript = TRANSCRIPT.read_text(encoding="utf-8")
    bodies = re.findall(
        r"<!-- BEGIN EXACT text_with_tex -->\n\n(.*?)\n\n<!-- END EXACT text_with_tex -->",
        transcript,
        flags=re.DOTALL,
    )
    r.check("transcript exact body count", len(bodies), 7, "chat_transcript")
    r.check("transcript exact body sequence", bodies, [m["text_with_tex"] for m in am], "chat_transcript")

    notion_text: dict[str, str] = {}
    for row in NOTION_PAGES:
        path = NOTION / row["path"]
        text = path.read_text(encoding="utf-8")
        notion_text[row["page_id"]] = text
        r.check(f"Notion {row['page_id']} sha256", sha256(path), row["sha256"], "notion_identity")
        r.check(f"Notion {row['page_id']} bytes", len(path.read_bytes()), row["bytes"], "notion_identity")
        r.check(f"Notion {row['page_id']} lines", len(text.splitlines()), row["lines"], "notion_identity")
        r.check(f"Notion {row['page_id']} page URL", f'/p/{row["page_id"]}' in text, True, "notion_structure")
        r.check(f"Notion {row['page_id']} title", f'{{"title":"{row["title"]}"}}' in text, True, "notion_structure")
        r.check(f"Notion {row['page_id']} parent", f'/p/{row["parent"]}' in text, True, "notion_structure")

    index_content = notion_text[NOTION_PAGES[0]["page_id"]].split("<content>", 1)[1].split("</content>", 1)[0]
    child_order = re.findall(r'<page url="https://app\.notion\.com/p/([0-9a-f]{32})">', index_content)
    expected_child_order = [
        "34cee2b74b3f8182a114ff6b4b910489",
        "34cee2b74b3f81359cb6e2419fe2f5f0",
        "34cee2b74b3f817499daf036a9bdca44",
        "34cee2b74b3f819e9687dfd81389b4c2",
    ]
    r.check("Chapter 30 child order", child_order, expected_child_order, "notion_structure")

    search_specs = [
        ("Weinberg Chapter 30", NOTION / "search/weinberg-chapter-30.json", "53eeaaaabc6a6d2cab838e6f08d52d21cf3ef775c165e6cba8df784f399a7e44", False),
        ("30 Supergraphs", NOTION / "search/30-supergraphs.json", "ae75f72f653fa313a2a86d4b546366b6c4eff1065eb875e694e9c17511315f71", True),
    ]
    for query, path, digest, expected_present in search_specs:
        data = json.loads(path.read_text(encoding="utf-8"))
        r.check(f"search {query} sha256", sha256(path), digest, "notion_search")
        r.check(f"search {query} exact query", data["query"], query, "notion_search")
        r.check(f"search {query} page scope", data["page_url"], "310ee2b74b3f8065a3acdbdac27f3b2b", "notion_search")
        ids = [x["id"].replace("-", "") for x in data["response"]["results"]]
        r.check(f"search {query} Chapter 30 presence", "34cee2b74b3f81239f12c44eda7b664f" in ids, expected_present, "notion_search")

    r.check("task id", task["id"], TASK_ID, "task")
    r.check("task type", task["type"], "REFERENCE_IMPORT", "task")
    r.check("task status", task["status"], "ACCEPTED", "task")
    r.check("chat translation deferred", task["chat_reference_exception"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT", "boundary")
    r.check("Notion translation deferred", task["notion_reference_exception"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT", "boundary")
    r.check("ledger task", ledger["task"], TASK_ID, "ledger")
    r.check("ledger translation deferred", ledger["admissibility"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT", "boundary")
    r.check("ledger Project adoption false", ledger["admissibility"]["project_formula_adoption"], False, "boundary")
    r.check("ledger contract modification false", ledger["admissibility"]["project_contract_modified"], False, "boundary")
    r.check("ledger message ids", [x["message_id"] for x in ledger["chat"]["message_ledger"]], AUTH_IDS, "ledger")
    r.check("ledger formulas not adopted", [x["adoption_status"] for x in ledger["chat"]["message_ledger"]], ["NOT_ADOPTED_IN_REFERENCE_IMPORT"] * 7, "boundary")
    r.check("ledger candidate claim ids", [x["id"] for x in ledger["candidate_claims"]], CLAIM_IDS, "ledger")
    r.check("ledger candidates not adopted", [x["adoption_status"] for x in ledger["candidate_claims"]], ["NOT_ADOPTED_IN_REFERENCE_IMPORT"] * 3, "boundary")
    r.check(
        "ledger per-page fetch timestamps",
        [x["fetched_at"] for x in ledger["weinberg_chapter_30"]["fetched_pages"]],
        ["2026-07-12T20:13:10Z"] * 4,
        "ledger",
    )

    entries = {x["id"]: x for x in manifest["entries"]}
    expected_sources = {
        "CHATGPT-STEP5-AUTHENTICATED-VISIBLE": AUTH,
        "CHATGPT-STEP5-SHARE-VISIBLE": SHARE,
        "CHATGPT-STEP5-AUTHENTICATED-TRANSCRIPT": TRANSCRIPT,
        "CHATGPT-STEP5-DUAL-CAPTURE-COMPARISON": COMPARISON,
        "WEINBERG-NOTION-CHAPTER-30-SEARCH-WEINBERG": NOTION / "search/weinberg-chapter-30.json",
        "WEINBERG-NOTION-CHAPTER-30-SEARCH-SUPERGRAPHS": NOTION / "search/30-supergraphs.json",
        **{row["id"]: NOTION / row["path"] for row in NOTION_PAGES},
        "STEP5-CHAT-WEINBERG30-SOURCE-LEDGER": LEDGER,
    }
    r.check("manifest Step5 source ids present", [x in entries for x in expected_sources], [True] * len(expected_sources), "manifest")
    r.check("manifest Step5 hashes", [entries[x]["sha256"] for x in expected_sources], [sha256(p) for p in expected_sources.values()], "manifest")

    claims = {x["id"]: x for x in claim_map["claims"]}
    r.check("claim-map Step5 ids present", [x in claims for x in CLAIM_IDS], [True] * 3, "claims")
    r.check("task candidate claim ids", task["candidate_claim_ids"], CLAIM_IDS, "claims")
    r.check(
        "claim-map Step5 source ids registered",
        [all(source in expected_sources for source in claims[cid]["sources"]) for cid in CLAIM_IDS],
        [True] * 3,
        "claims",
    )

    categories: dict[str, dict[str, int]] = {}
    for check in r.checks:
        row = categories.setdefault(check["category"], {"checks": 0, "failed": 0})
        row["checks"] += 1
        row["failed"] += int(not check["passed"])
    return {
        "schema": 1,
        "task": TASK_ID,
        "status": "PASS" if not r.failures else "FAIL",
        "categories": categories,
        "totals": {"checks": len(r.checks), "failed": len(r.failures)},
        "checks": r.checks,
        "failures": r.failures,
    }


def main() -> None:
    audit = build_audit()
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2, ensure_ascii=False))
        raise SystemExit(1)
    print(f"Step5 reference import: {audit['totals']['checks']} checks, 0 failures")


if __name__ == "__main__":
    main()
