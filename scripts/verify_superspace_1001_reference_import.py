from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references/vendor/hep-th-0108200v1.pdf"
SUBSET = ROOT / "references/vendor/local/superspace-1001-gauge-representations-pages.pdf"
LEDGER = ROOT / "references/superspace-1001-gauge-representation-source-ledger.json"
MANIFEST = ROOT / "references/manifest.yaml"
CLAIM_MAP = ROOT / "references/claim-map.yaml"
TASK = ROOT / "tasks/archive/REFERENCE-IMPORT-SUPERSPACE-1001-VECTOR-REPRESENTATION-001.yaml"
OBLIGATIONS = ROOT / "ledger/proof_obligations.json"
AUDIT = ROOT / "audits/superspace-1001-reference-import-verification.json"

SOURCE_SHA = "3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99"
SUBSET_SHA = "57d71bcf95fb84dabb4f5e85cfb9290ba52031e031a062cf7b0e5dad93a2d87e"
STEP4_SHA = "f76e1975617e6a703efda4413a67760bf55d84e22fb3a7a6289d3b890ff3eb6e"

PAGE_MAP = [
    (1, 1),
    (2, 5),
    (3, 177),
    (4, 178),
    (5, 179),
    (6, 180),
    (7, 182),
    (8, 183),
    (9, 184),
    (10, 185),
    (11, 186),
    (12, 187),
    (13, 188),
    (14, 190),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_page_count(path: Path) -> int:
    return len(re.findall(rb"/Type\s*/Page\b", path.read_bytes()))


def page_text(path: Path, page: int) -> bytes:
    completed = subprocess.run(
        [
            "pdftotext",
            "-f",
            str(page),
            "-l",
            str(page),
            "-layout",
            str(path),
            "-",
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.replace(b"\x0c", b"").rstrip()


def main() -> int:
    if shutil.which("pdftotext") is None:
        raise SystemExit("pdftotext is required for page-correspondence verification")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    claim_map = json.loads(CLAIM_MAP.read_text(encoding="utf-8"))
    task = json.loads(TASK.read_text(encoding="utf-8"))
    obligations = json.loads(OBLIGATIONS.read_text(encoding="utf-8"))
    entries = {entry["id"]: entry for entry in manifest["entries"]}

    checks: list[dict[str, object]] = []

    def check(name: str, left: object, right: object) -> None:
        checks.append(
            {
                "name": name,
                "left": left,
                "right": right,
                "passed": left == right,
            }
        )

    check("source_sha", sha256(SOURCE), SOURCE_SHA)
    check("subset_sha", sha256(SUBSET), SUBSET_SHA)
    check("source_page_count", pdf_page_count(SOURCE), 568)
    check("subset_page_count", pdf_page_count(SUBSET), 14)

    source_entry = entries["ARXIV-HEP-TH-0108200-V1"]
    subset_entry = entries["SUPERSPACE-1001-GAUGE-REPRESENTATIONS-PAGES"]
    check("manifest_source_path", source_entry["path"], str(SOURCE.relative_to(ROOT)))
    check("manifest_source_sha", source_entry["sha256"], SOURCE_SHA)
    check("manifest_subset_path", subset_entry["path"], str(SUBSET.relative_to(ROOT)))
    check("manifest_subset_sha", subset_entry["sha256"], SUBSET_SHA)

    source = ledger["source"]
    scoped = ledger["scoped_artifact"]
    check("ledger_local_source_sha", source["local_sha256"], SOURCE_SHA)
    check("ledger_vendor_source_sha", source["identical_existing_vendor_artifact"]["sha256"], SOURCE_SHA)
    check("ledger_subset_sha", scoped["sha256"], SUBSET_SHA)
    check("ledger_subset_pages", scoped["pages"], 14)
    check("discovery_filename_candidates", ledger["discovery"]["filename_candidate_count"], 5)
    check("discovery_opened_candidates", ledger["discovery"]["opened_candidate_count"], 1)
    check("discovery_exact_title_matches", ledger["discovery"]["rendered_title_page_exact_match_count"], 1)
    check("temporary_full_text_retained", ledger["locator_index_pass"]["temporary_full_text_retained"], False)
    visual = ledger["visual_verification"]
    manual_checks = visual["manual_visual_checks"]
    check("manual_visual_check_count", len(manual_checks), 6)
    check("manual_visual_check_pages_unique", len({item["subset_page"] for item in manual_checks}), 6)
    check(
        "independent_manual_raster_comparisons",
        visual["independent_page_comparison"]["independent_manual_raster_comparisons"],
        14,
    )

    for subset_page, source_page in PAGE_MAP:
        subset_text = page_text(SUBSET, subset_page)
        source_text = page_text(SOURCE, source_page)
        check(
            f"page_text_{subset_page}_from_{source_page}",
            hashlib.sha256(subset_text).hexdigest(),
            hashlib.sha256(source_text).hexdigest(),
        )

    title_text = page_text(SUBSET, 1).decode("utf-8", errors="replace")
    check("title_marker", "SUPERSPACE" in title_text, True)
    check("subtitle_marker", "One thousand and one" in title_text, True)
    check("author_marker", "S. James Gates, Jr." in title_text, True)

    claim_ids = {claim["id"] for claim in claim_map["claims"]}
    for claim_id in (
        "SUPERSPACE-1001-GAUGE-CHIRAL-REPRESENTATION-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-BRIDGE-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-BIANCHI-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-ACTION-COMPARISON-EVIDENCE",
    ):
        check(f"claim_{claim_id}", claim_id in claim_ids, True)

    resolved_locator = (
        "icloud-file://01_物理科研/CMC材料/CMC课题/SUPERSPACE.pdf"
        "#sha256=3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99"
    )
    check("task_resolved_locator", task["local_reference_exception"]["resolved_locator"], resolved_locator)
    check("task_resolved_sha", task["local_reference_exception"]["resolved_sha256"], SOURCE_SHA)
    check("task_vendor_source_allowed", "references/vendor/hep-th-0108200v1.pdf" in task["allowed_inputs"], True)

    step4 = next(
        item
        for item in obligations["proof_obligations"]
        if item["id"] == "CONTRACT-STEP-04-EXTENDED-SUPER-YANG-MILLS-001"
    )
    step4_path = ROOT / step4["task"]
    check("step4_recorded_sha", step4["task_sha256"], STEP4_SHA)
    check("step4_file_sha", sha256(step4_path), STEP4_SHA)
    check(
        "one_current_obligation",
        sum(item["task"] == "tasks/CURRENT.yaml" for item in obligations["proof_obligations"]),
        1,
    )

    failures = [item["name"] for item in checks if not item["passed"]]
    audit = {
        "schema": 1,
        "task": "REFERENCE-IMPORT-SUPERSPACE-1001-VECTOR-REPRESENTATION-001",
        "status": "PASS" if not failures else "FAIL",
        "page_map": [
            {"subset_page": subset_page, "source_pdf_page": source_page}
            for subset_page, source_page in PAGE_MAP
        ],
        "checks": checks,
        "totals": {
            "checks": len(checks),
            "failed": len(failures),
            "page_text_comparisons": len(PAGE_MAP),
        },
        "failures": failures,
    }
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
