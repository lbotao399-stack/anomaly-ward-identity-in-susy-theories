from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references/vendor/hep-th-0108200v1.pdf"
SUBSET = ROOT / "references/vendor/local/superspace-1001-supergraph-pages.pdf"
LEDGER = ROOT / "references/superspace-1001-supergraph-source-ledger.json"
MANIFEST = ROOT / "references/manifest.yaml"
CLAIM_MAP = ROOT / "references/claim-map.yaml"
TASK_CANDIDATES = (
    ROOT / "tasks/CURRENT.yaml",
    ROOT / "tasks/archive/REFERENCE-IMPORT-SUPERSPACE-1001-SUPERGRAPH-001.yaml",
)
OBLIGATIONS = ROOT / "ledger/proof_obligations.json"
AUDIT = ROOT / "audits/superspace-1001-supergraph-reference-import-verification.json"

SOURCE_SHA = "3669da125d970d5db9f247b580da3e89f76a9363235910e7f94509eff097ea99"
SUBSET_SHA = "1cb68ae63aa5c8d8a3e2150b769ba2bfb56f245c91204bafceaa5793f969ccb8"
LEDGER_SHA = "fefb51c998872d6bee6a4bcfb21a56d75b121a294d22abd189b1da8d80d4a5f3"
CLAIM_MAP_SHA = "26b8106d7c5b5cf08904a34d17ae1a280a1df3166929ca4081859ef9a2e11bad"

CLAIM_IDS = [
    "SUPERSPACE-1001-GAUSSIAN-SUPERFIELD-EVIDENCE",
    "SUPERSPACE-1001-DELTA-PROJECTOR-EVIDENCE",
    "SUPERSPACE-1001-CHIRAL-PROPAGATOR-EVIDENCE",
    "SUPERSPACE-1001-VECTOR-GAUGE-FIXING-EVIDENCE",
    "SUPERSPACE-1001-FP-NK-GHOST-EVIDENCE",
    "SUPERSPACE-1001-ORDERED-SUPERGRAPH-VERTEX-EVIDENCE",
    "SUPERSPACE-1001-D-ALGEBRA-EVIDENCE",
]

SOURCE_PAGES = [1, 5, 6, *range(353, 380), *range(389, 405)]
PAGE_MAP = list(enumerate(SOURCE_PAGES, start=1))


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


def page_raster_sha(path: Path, page: int, directory: Path, stem: str) -> str:
    prefix = directory / stem
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-png",
            "-r",
            "72",
            str(path),
            str(prefix),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return sha256(prefix.with_suffix(".png"))


def main() -> int:
    for executable in ("pdftotext", "pdftoppm"):
        if shutil.which(executable) is None:
            raise SystemExit(f"{executable} is required")

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    claim_map = json.loads(CLAIM_MAP.read_text(encoding="utf-8"))
    task_path = next(
        path
        for path in TASK_CANDIDATES
        if path.exists()
        and json.loads(path.read_text(encoding="utf-8"))["id"]
        == "REFERENCE-IMPORT-SUPERSPACE-1001-SUPERGRAPH-001"
    )
    task = json.loads(task_path.read_text(encoding="utf-8"))
    obligations = json.loads(OBLIGATIONS.read_text(encoding="utf-8"))
    entries = {entry["id"]: entry for entry in manifest["entries"]}
    claims = {claim["id"]: claim for claim in claim_map["claims"]}

    checks: list[dict[str, object]] = []

    def check(name: str, left: object, right: object) -> None:
        checks.append({"name": name, "left": left, "right": right, "passed": left == right})

    check("source_sha", sha256(SOURCE), SOURCE_SHA)
    check("subset_sha", sha256(SUBSET), SUBSET_SHA)
    check("ledger_sha", sha256(LEDGER), LEDGER_SHA)
    check("claim_map_sha", sha256(CLAIM_MAP), CLAIM_MAP_SHA)
    check("source_page_count", pdf_page_count(SOURCE), 568)
    check("subset_page_count", pdf_page_count(SUBSET), 46)

    source_entry = entries["ARXIV-HEP-TH-0108200-V1"]
    subset_entry = entries["SUPERSPACE-1001-SUPERGRAPH-PAGES"]
    ledger_entry = entries["SUPERSPACE-1001-SUPERGRAPH-SOURCE-LEDGER"]
    claim_entry = entries["REFERENCE-CLAIM-MAP"]
    check("manifest_source_sha", source_entry["sha256"], SOURCE_SHA)
    check("manifest_subset_path", subset_entry["path"], str(SUBSET.relative_to(ROOT)))
    check("manifest_subset_sha", subset_entry["sha256"], SUBSET_SHA)
    check("manifest_ledger_path", ledger_entry["path"], str(LEDGER.relative_to(ROOT)))
    check("manifest_ledger_sha", ledger_entry["sha256"], LEDGER_SHA)
    check("manifest_claim_map_sha", claim_entry["sha256"], CLAIM_MAP_SHA)

    check("task_id", task["id"], "REFERENCE-IMPORT-SUPERSPACE-1001-SUPERGRAPH-001")
    check("task_type", task["type"], "REFERENCE_IMPORT")
    check("task_source_sha", task["source_scope"]["sha256"], SOURCE_SHA)
    check("task_source_pages", task["source_scope"]["pdf_pages"], 568)
    check("task_translation_status", task["source_scope"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
    check("task_claim_ids", task["candidate_claim_ids"], CLAIM_IDS)

    check("ledger_source_sha", ledger["source"]["sha256"], SOURCE_SHA)
    check("ledger_subset_sha", ledger["scoped_artifact"]["sha256"], SUBSET_SHA)
    check("ledger_subset_pages", ledger["scoped_artifact"]["pages"], 46)
    check("ledger_translation_status", ledger["admissibility"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
    check("ledger_candidate_claim_ids", [item["id"] for item in ledger["candidate_claims"]], CLAIM_IDS)
    check(
        "ledger_claims_not_adopted",
        all(item["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT" for item in ledger["candidate_claims"]),
        True,
    )

    for claim_id in CLAIM_IDS:
        check(f"claim_present_{claim_id}", claim_id in claims, True)
        check(f"claim_source_{claim_id}", claims[claim_id]["sources"], ["SUPERSPACE-1001-SUPERGRAPH-PAGES"])

    text_mismatches = 0
    raster_mismatches = 0
    with tempfile.TemporaryDirectory(prefix="awi-supergraph-import-") as temporary:
        temp = Path(temporary)
        for subset_page, source_page in PAGE_MAP:
            subset_text_sha = hashlib.sha256(page_text(SUBSET, subset_page)).hexdigest()
            source_text_sha = hashlib.sha256(page_text(SOURCE, source_page)).hexdigest()
            if subset_text_sha != source_text_sha:
                text_mismatches += 1
            check(f"page_text_{subset_page}_from_{source_page}", subset_text_sha, source_text_sha)

            subset_raster_sha = page_raster_sha(SUBSET, subset_page, temp, f"subset-{subset_page}")
            source_raster_sha = page_raster_sha(SOURCE, source_page, temp, f"source-{source_page}")
            if subset_raster_sha != source_raster_sha:
                raster_mismatches += 1
            check(f"page_raster_{subset_page}_from_{source_page}", subset_raster_sha, source_raster_sha)

    check("page_text_mismatch_count", text_mismatches, 0)
    check("page_raster_mismatch_count", raster_mismatches, 0)

    title = page_text(SUBSET, 1).decode("utf-8", errors="replace")
    contents = (
        page_text(SUBSET, 3)
        .decode("utf-8", errors="replace")
        .replace("ﬁ", "fi")
        .replace("ﬀ", "ff")
    )
    gauge = page_text(SUBSET, 10).decode("utf-8", errors="replace")
    rules = page_text(SUBSET, 15).decode("utf-8", errors="replace")
    dalgebra = page_text(SUBSET, 27).decode("utf-8", errors="replace")
    nk = page_text(SUBSET, 34).decode("utf-8", errors="replace")
    covariant = page_text(SUBSET, 40).decode("utf-8", errors="replace")
    for name, marker, text in (
        ("title", "SUPERSPACE", title),
        ("contents_supergraphs", "6.1. Introduction to supergraphs", contents),
        ("contents_gauge_fixing", "6.2. Gauge fixing and ghosts", contents),
        ("contents_rules", "6.3. Supergraph rules", contents),
        ("contents_background", "6.5. The background field method", contents),
        ("gauge_section", "b. Supersymmetric Yang-Mills theory", gauge),
        ("rules_section", "a. Derivation of Feynman rules", rules),
        ("dalgebra_section", "e. D-algebra", dalgebra),
        ("nk_marker", "Nielsen-Kallosh ghost", nk),
        ("covariant_marker", "c. Covariant Feynman rules", covariant),
    ):
        check(name, marker in text, True)

    task_obligations = [item for item in obligations["proof_obligations"] if item["id"] == task["id"]]
    check("one_current_obligation", len(task_obligations), 1)
    check("current_obligation_id", task_obligations[0]["id"], task["id"])

    visual = ledger["visual_verification"]
    check("manual_contact_sheets", visual["manual_contact_sheets"], 8)
    check("manual_pages", visual["manually_inspected_subset_pages"], 46)
    check("manual_mismatches", visual["manual_visual_mismatches"], 0)
    check("ledger_text_comparisons", visual["independent_page_comparison"]["machine_text_comparisons"], 46)
    check("ledger_raster_comparisons", visual["independent_page_comparison"]["independent_raster_comparisons"], 46)

    failures = [item["name"] for item in checks if not item["passed"]]
    audit = {
        "schema": 1,
        "task": task["id"],
        "status": "PASS" if not failures else "FAIL",
        "arithmetic": {
            "hash": "SHA-256",
            "page_text": "exact pdftotext -layout bytes after form-feed removal",
            "page_raster": "exact 72-dpi pdftoppm PNG bytes",
        },
        "page_map": [
            {"subset_page": subset_page, "source_pdf_page": source_page}
            for subset_page, source_page in PAGE_MAP
        ],
        "checks": checks,
        "totals": {
            "checks": len(checks),
            "failed": len(failures),
            "page_text_comparisons": len(PAGE_MAP),
            "page_raster_comparisons": len(PAGE_MAP),
        },
        "failures": failures,
    }
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
