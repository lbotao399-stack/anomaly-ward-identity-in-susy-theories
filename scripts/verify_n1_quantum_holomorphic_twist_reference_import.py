from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "REFERENCE-IMPORT-N1-QUANTUM-HOLOMORPHIC-TWIST-001"
LEDGER_ID = "N1-QUANTUM-HOLOMORPHIC-TWIST-SOURCE-LEDGER"
AUDIT_PATH = ROOT / "audits/n1-quantum-holomorphic-twist-reference-import-verification.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_pages(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise RuntimeError(f"missing PDF page count: {path}")
    return int(match.group(1))


def gzip_original_name(raw: bytes) -> str:
    if raw[:2] != b"\x1f\x8b":
        raise ValueError("not gzip")
    flags = raw[3]
    offset = 10
    if flags & 4:
        extra_length = int.from_bytes(raw[offset : offset + 2], "little")
        offset += 2 + extra_length
    if flags & 8:
        end = raw.index(b"\x00", offset)
        return raw[offset:end].decode("latin-1")
    return ""


checks: list[dict] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    checks.append({"name": name, "result": "PASS" if condition else "FAIL", "detail": detail})


task = load_json(ROOT / "tasks/CURRENT.yaml")
ledger = load_json(ROOT / "references/n1-quantum-holomorphic-twist-source-ledger.json")
manifest = load_json(ROOT / "references/manifest.yaml")
claim_map = load_json(ROOT / "references/claim-map.yaml")
obligations = load_json(ROOT / "ledger/proof_obligations.json")

manifest_by_id = {entry["id"]: entry for entry in manifest["entries"]}
claims_by_id = {entry["id"]: entry for entry in claim_map["claims"]}

check("task-id", task["id"] == TASK_ID)
check("task-type", task["type"] == "REFERENCE_IMPORT")
check("task-status", task["status"] == "SPECIFIED")
check("task-eight-claims", len(task["candidate_claim_ids"]) == 8)
check("task-no-contract-input", all(not item.startswith("contracts/") for item in task["allowed_inputs"]))
check("task-external-count", sum(item.startswith("https://") for item in task["allowed_inputs"]) == 16)
check("task-ledger-id", ledger["task"] == TASK_ID)
check("task-current-obligation", sum(item["task"] == "tasks/CURRENT.yaml" for item in obligations["proof_obligations"]) == 1)
current_obligation = next(item for item in obligations["proof_obligations"] if item["task"] == "tasks/CURRENT.yaml")
check("task-current-obligation-id", current_obligation["id"] == TASK_ID)
check("task-current-hash", current_obligation["task_sha256"] == sha256(ROOT / "tasks/CURRENT.yaml"))

check("ledger-source-count", len(ledger["sources"]) == 8)
check("ledger-core-count", len(ledger["source_tiers"]["core_bv_holomorphic"]) == 4)
check("ledger-diagnostic-count", len(ledger["source_tiers"]["anomaly_and_renormalization_diagnostics"]) == 4)
check("ledger-no-source-execution", ledger["acquisition"]["source_execution_performed"] is False)
check("ledger-no-translation", ledger["acquisition"]["translation_status"] == "NOT_PERFORMED_IN_REFERENCE_IMPORT")
check("ledger-no-adoption", ledger["acquisition"]["project_formula_adoption"] is False)

for source in ledger["sources"]:
    source_id = source["id"]
    check(f"{source_id}-version", bool(re.fullmatch(r"v\d+", source["version"])))
    check(f"{source_id}-title", bool(source["title"].strip()))
    check(f"{source_id}-authors", bool(source["authors"]) and all(author.strip() for author in source["authors"]))
    for kind in ("source", "pdf"):
        artifact = source[kind]
        path = ROOT / artifact["path"]
        artifact_id = f"{source_id}-{kind.upper()}"
        check(f"{artifact_id}-exists", path.is_file())
        check(f"{artifact_id}-bytes", path.stat().st_size == artifact["bytes"])
        check(f"{artifact_id}-sha", sha256(path) == artifact["sha256"])
        check(f"{artifact_id}-manifest", artifact_id in manifest_by_id)
        if artifact_id in manifest_by_id:
            entry = manifest_by_id[artifact_id]
            check(f"{artifact_id}-manifest-path", entry["path"] == artifact["path"])
            check(f"{artifact_id}-manifest-sha", entry["sha256"] == artifact["sha256"])
    pdf_path = ROOT / source["pdf"]["path"]
    check(f"{source_id}-pdf-pages", pdf_pages(pdf_path) == source["pdf"]["pages"])
    source_path = ROOT / source["source"]["path"]
    raw = source_path.read_bytes()
    archive_format = source["source"]["archive_format"]
    if archive_format == "gzip_tar":
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
            actual_members = [member.name for member in archive.getmembers()]
        check(f"{source_id}-archive-members", actual_members == source["source"]["members"])
    elif archive_format == "gzip_single_file":
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
            uncompressed = stream.read()
        expected_member = source["source"]["members"][0]
        check(f"{source_id}-gzip-name", gzip_original_name(raw) == expected_member["name"])
        check(f"{source_id}-gzip-bytes", len(uncompressed) == expected_member["bytes"])
    else:
        check(f"{source_id}-archive-format", False, archive_format)

ledger_claim_ids = [claim["id"] for claim in ledger["candidate_claims"]]
check("claim-task-ledger-id-set", set(task["candidate_claim_ids"]) == set(ledger_claim_ids))
check("claim-distinct-counterterm", "QHT-REF-HOLOMORPHIC-COUNTERTERM" in ledger_claim_ids)
check("claim-distinct-qme", "QHT-REF-HOLOMORPHIC-QME-ANOMALY" in ledger_claim_ids)

for candidate in ledger["candidate_claims"]:
    claim_id = candidate["id"]
    check(f"{claim_id}-claim-map", claim_id in claims_by_id)
    check(f"{claim_id}-locator", bool(candidate["locator"].strip()))
    check(f"{claim_id}-scope", bool(candidate["scope_limitation"].strip()))
    check(f"{claim_id}-not-adopted", candidate["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT")
    if claim_id in claims_by_id:
        mapped = claims_by_id[claim_id]
        check(f"{claim_id}-sources", mapped["sources"] == candidate["sources"])
        check(f"{claim_id}-allowed-use", bool(mapped["allowed_use"].strip()))
        check(f"{claim_id}-forbidden-use", bool(mapped["forbidden_use"].strip()))
        for artifact_id in mapped["sources"]:
            check(f"{claim_id}-{artifact_id}-hashed", artifact_id in manifest_by_id and bool(re.fullmatch(r"[0-9a-f]{64}", manifest_by_id[artifact_id]["sha256"])))

claim_map_entry = manifest_by_id["REFERENCE-CLAIM-MAP"]
check("claim-map-manifest-path", claim_map_entry["path"] == "references/claim-map.yaml")
check("claim-map-manifest-sha", claim_map_entry["sha256"] == sha256(ROOT / "references/claim-map.yaml"))
ledger_entry = manifest_by_id[LEDGER_ID]
check("ledger-manifest-path", ledger_entry["path"] == "references/n1-quantum-holomorphic-twist-source-ledger.json")
check("ledger-manifest-sha", ledger_entry["sha256"] == sha256(ROOT / ledger_entry["path"]))

visual_checks = ledger["visual_verification"]["checks"]
check("visual-source-count", len(visual_checks) == 8)
check("visual-result", ledger["visual_verification"]["result"] == "PASS")
source_by_id = {source["id"]: source for source in ledger["sources"]}
for visual in visual_checks:
    check(f"{visual['source']}-visual-source", visual["source"] in source_by_id)
    check(f"{visual['source']}-visual-pass", visual["result"] == "PASS")
    if visual["source"] in source_by_id:
        page_count = source_by_id[visual["source"]]["pdf"]["pages"]
        check(f"{visual['source']}-visual-pages", all(1 <= page <= page_count for page in visual["pdf_pages"]))

admissibility = ledger["admissibility"]
check("admissibility-reference-only", admissibility["classification"] == "REFERENCE_EVIDENCE_ONLY")
check("admissibility-no-translation", admissibility["translation_status"] == "NOT_PERFORMED_IN_REFERENCE_IMPORT")
check("admissibility-no-adoption", admissibility["project_formula_adoption"] is False)
check("admissibility-no-contract-change", admissibility["project_contract_modified"] is False)
check("admissibility-no-notion-read", admissibility["notion_read_performed"] is False)
check("admissibility-no-chat", admissibility["chat_or_pro_output_used"] is False)

failed = [item for item in checks if item["result"] != "PASS"]
audit = {
    "schema": 1,
    "task": TASK_ID,
    "status": "PASS" if not failed else "FAIL",
    "totals": {"checks": len(checks), "failed": len(failed), "sources": len(ledger["sources"]), "claims": len(ledger["candidate_claims"])},
    "checks": checks,
}
AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
AUDIT_PATH.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if failed:
    for failure in failed:
        print(json.dumps(failure, ensure_ascii=False))
    raise SystemExit(1)

print(json.dumps(audit["totals"], sort_keys=True))
