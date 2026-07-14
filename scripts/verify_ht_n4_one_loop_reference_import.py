#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import tarfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "references/vendor/arxiv/2512.07771v2/metadata.json"
LEDGER_PATH = ROOT / "references/ht-n4-one-loop-source-ledger.json"
MANIFEST_PATH = ROOT / "references/manifest.yaml"
CLAIM_MAP_PATH = ROOT / "references/claim-map.yaml"
TASK_PATH = ROOT / "tasks/archive/REFERENCE-IMPORT-HT-N4-ONE-LOOP-001.yaml"
AUDIT_PATH = ROOT / "audits/ht-n4-one-loop-reference-import-verification.json"

TASK_ID = "REFERENCE-IMPORT-HT-N4-ONE-LOOP-001"
SOURCE_ROOT = "references/vendor/arxiv/2512.07771v2/source"
ARCHIVE_PATH = "references/vendor/arxiv/2512.07771v2/2512.07771v2.tar.gz"
MAIN_TEX_PATH = f"{SOURCE_ROOT}/main.tex"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


FILES = [
    ("00README.json", f"{SOURCE_ROOT}/00README.json", 629, "63c8b2f900ebb39ca5d0d9b295ab3668784ecaf54ffcf1edd9fe5f62d1f9429b"),
    ("JHEP.bst", f"{SOURCE_ROOT}/JHEP.bst", 19999, "3a56889d89fdf1f402582b41ee143dfc7986c7d4270adc0e008fb21d6da3a621"),
    ("images/segment.pdf", f"{SOURCE_ROOT}/images/segment.pdf", 2022, "c718bc5845a15e9860febdd7daaf39ea1a72fa1fdd65b4341d4e901b8c15b9b3"),
    ("images/triangle.pdf", f"{SOURCE_ROOT}/images/triangle.pdf", 2130, "c48a34e1a7e5a79538b3f083d1f1168f5ecbfcaca00eb0855e690dd557f94143"),
    ("jheppub.sty", f"{SOURCE_ROOT}/jheppub.sty", 10993, "ed3b8049bb3042bce57ba7ccbefbb2c56159884bb467a0260f27bbb6ef61ed80"),
    ("main.bbl", f"{SOURCE_ROOT}/main.bbl", 19147, "90a84bff4a6aaf6d6f8ffd3c8dee65a351bbd5d9d566f1bd63fa7a47a2748079"),
    ("main.tex", MAIN_TEX_PATH, 107272, "90352c555f69eac3a99b9742c59e63afc785df333399a0730f8ac1ae094d9899"),
    ("mono.bib", f"{SOURCE_ROOT}/mono.bib", 33759, "1500d8e2bca9246f987add2223d040b28b572167029af7bdd5054f38672d5ff9"),
]


ANCHORS = [
    ("HT-TITLE-ABSTRACT", 111, 126, 1235, "a5416babfe591e14658adaf5144a9b35344142ad7198adc0b2e65c6b14c3abcd"),
    ("HT-INTRO-N4-COMPACT-Q1", 198, 206, 1356, "6548bf5c794c3f38e47b0ea462444531e9ff9d89c3dd0a57bec867713825a900"),
    ("HT-HIGHER-LOOP-BOUNDARY", 218, 222, 926, "e2a209f3c5797836ed7f674eeeaa997dfc1b150fe23c7cc336adabfb6684b849"),
    ("HT-Q1-BRACKET-DEFINITION", 386, 400, 2200, "261f51ca39ae337fae29ca78a190d1740c7537a37eeaa047e70aa5d53f579c9c"),
    ("HT-NORMAL-ORDERING-PARITY", 438, 451, 2283, "5940ab15d2473a3ded0f381508923ed898accb48b44073ca0793ff41e703d0de"),
    ("HT-MASTER-INTEGRAL-DEFINITION-LAMAN", 485, 499, 2485, "081dba027a9296dc4c51a82064eddcc8d8225e5d5c937eb8bf6be1b3009b951d"),
    ("HT-MASTER-INTEGRAL-CLOSED-FORM", 652, 668, 1537, "8e23f1907a2ae6d5205905f2975d0651b6dd33a05f84d9f157fd6bd641d80189"),
    ("HT-TWISTED-ACTION-FIELDS", 675, 705, 2181, "2277b8d7ed32708a54b9339a159ba69f4cece8ce81e7e0ff3f3ab5360b376e01"),
    ("HT-PAIR-RULE-AND-DTRI-KERNEL", 709, 732, 2510, "0c20b367363886ef1220ba26067f85f7defc86305ed9fe07d287e55988bfee49"),
    ("HT-LIE-NORMALIZATION", 736, 744, 682, "8213f1680ed884d3c0d9e570cf8b7ddcb03f63899c461bb9713ec5f3ba4ebd16"),
    ("HT-GENERIC-ADJOINT-SHIFTED-PAIRS", 1038, 1073, 2618, "8d8664edc81e68044492f9a3d90f7f08008b2c642c0a243cae17be4028bcf7d5"),
    ("HT-N4-SETUP-SUPERFIELD", 1149, 1184, 1992, "a16da6c67d43fdfa90a0f50334936f5cb378a512d72e8996a99322c5d579b0c8"),
    ("HT-N4-COMPONENT-PAIR-RESULTS", 1212, 1246, 2258, "c6ac381fac5f1566b9290b64850381027000d03166374e3b73df0b51956a6ae7"),
    ("HT-N4-COMPACT-SUPERFIELD-RESULT", 1248, 1252, 405, "6e82c7f07ce4c72fab77f4c104465e9c27d3d4f470338810582f2ab50d393b8f"),
    ("HT-MASTER-INTEGRAL-DERIVATION", 1272, 1334, 4522, "1ecf734ea4d421c18b4c705815eaa7a3ce29ac621ed41be85584999f4687667e"),
    ("HT-N4-DERIVATIVE-COMPONENT-PAIR-RESULTS", 1339, 1395, 5171, "9e008678d0073e6a3d8d2899d262d5773e4ff7c7d156a2701691384d03bad832"),
]


CLAIM_SOURCES = [
    "ARXIV-2512.07771V2-SOURCE-MAIN-TEX",
    "HT-N4-ONE-LOOP-SOURCE-LEDGER",
]


EXPECTED_CLAIMS = {
    "HT-N4-ONE-LOOP-COMPLETE-SUPERFIELD-CANDIDATE": {
        "id": "HT-N4-ONE-LOOP-COMPLETE-SUPERFIELD-CANDIDATE",
        "sources": CLAIM_SOURCES,
        "classification": "EXTERNAL_TARGET_ONLY",
        "translation_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "comparison_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "allowed_use": "A later registered CONTRACT_CHANGE may construct an explicit source-to-Project dictionary and independently test the source's compact N=4 one-loop superfield target, while retaining every source-internal normalization and ordering conflict.",
        "forbidden_use": "Importing the source superfield, coefficient, color normalization, derivative convention, completeness claim, or higher-loop statement as a Project formula during this reference import.",
    },
    "HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE": {
        "id": "HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE",
        "sources": CLAIM_SOURCES,
        "classification": "EXTERNAL_TARGET_ONLY",
        "translation_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "comparison_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "allowed_use": "A later registered CONTRACT_CHANGE may translate and independently rederive the source's N=4 pair formulas, zero pairs, and arbitrary-holomorphic-derivative formulas after fixing the source ordering and normalization ambiguities.",
        "forbidden_use": "Treating any printed pair formula, zero, derivative-distribution coefficient, parity sign, or ordering as a Project result without an independent Project derivation.",
    },
    "HT-ONE-LOOP-MASTER-INTEGRAL-CANDIDATE": {
        "id": "HT-ONE-LOOP-MASTER-INTEGRAL-CANDIDATE",
        "sources": CLAIM_SOURCES,
        "classification": "EXTERNAL_TARGET_ONLY",
        "translation_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "comparison_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "allowed_use": "A later registered CONTRACT_CHANGE may reconstruct the source's holomorphic-twist triangle master integral in source notation and compare it only after deriving the Project-side regulated integral independently.",
        "forbidden_use": "Using the holomorphic-twist master integral, Laman-graph statement, zero-shift value, measure, regulator, or derivative kernel as a Project Feynman integral or graph census.",
    },
}


MANIFEST_ROWS_FIXED = [
    ("ARXIV-2512.07771V2-PDF", "references/vendor/arxiv/2512.07771v2/2512.07771v2.pdf", "PRIMARY_REFERENCE_EXTERNAL_TARGET_ONLY", "cb2a6f53c97dd0f706685fd123ef6eb6a909344b78b02769af78e90ccfcf1e35"),
    ("ARXIV-2512.07771V2-SOURCE-ARCHIVE", ARCHIVE_PATH, "PRIMARY_REFERENCE_SOURCE_ARCHIVE_EXTERNAL_TARGET_ONLY", "27d9eefd23fef109bb65be780c72a360d0df9ba90c5db1bc07ecf0b248a63632"),
    ("ARXIV-2512.07771V2-SOURCE-00README-JSON", f"{SOURCE_ROOT}/00README.json", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "63c8b2f900ebb39ca5d0d9b295ab3668784ecaf54ffcf1edd9fe5f62d1f9429b"),
    ("ARXIV-2512.07771V2-SOURCE-JHEP-BST", f"{SOURCE_ROOT}/JHEP.bst", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "3a56889d89fdf1f402582b41ee143dfc7986c7d4270adc0e008fb21d6da3a621"),
    ("ARXIV-2512.07771V2-SOURCE-SEGMENT-PDF", f"{SOURCE_ROOT}/images/segment.pdf", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "c718bc5845a15e9860febdd7daaf39ea1a72fa1fdd65b4341d4e901b8c15b9b3"),
    ("ARXIV-2512.07771V2-SOURCE-TRIANGLE-PDF", f"{SOURCE_ROOT}/images/triangle.pdf", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "c48a34e1a7e5a79538b3f083d1f1168f5ecbfcaca00eb0855e690dd557f94143"),
    ("ARXIV-2512.07771V2-SOURCE-JHEPPUB-STY", f"{SOURCE_ROOT}/jheppub.sty", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "ed3b8049bb3042bce57ba7ccbefbb2c56159884bb467a0260f27bbb6ef61ed80"),
    ("ARXIV-2512.07771V2-SOURCE-MAIN-BBL", f"{SOURCE_ROOT}/main.bbl", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "90a84bff4a6aaf6d6f8ffd3c8dee65a351bbd5d9d566f1bd63fa7a47a2748079"),
    ("ARXIV-2512.07771V2-SOURCE-MAIN-TEX", MAIN_TEX_PATH, "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "90352c555f69eac3a99b9742c59e63afc785df333399a0730f8ac1ae094d9899"),
    ("ARXIV-2512.07771V2-SOURCE-MONO-BIB", f"{SOURCE_ROOT}/mono.bib", "PRIMARY_REFERENCE_EXTRACTED_SOURCE_EXTERNAL_TARGET_ONLY", "1500d8e2bca9246f987add2223d040b28b572167029af7bdd5054f38672d5ff9"),
]


checks: list[dict[str, Any]] = []


def check(check_id: str, condition: bool, detail: str = "") -> None:
    row: dict[str, Any] = {"id": check_id, "status": "PASS" if condition else "FAIL"}
    if not condition:
        row["detail"] = detail
    checks.append(row)


def equal(check_id: str, actual: Any, expected: Any) -> None:
    check(check_id, actual == expected, f"expected={expected!r}; actual={actual!r}")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    metadata = load_json(METADATA_PATH)
    ledger = load_json(LEDGER_PATH)
    manifest = load_json(MANIFEST_PATH)
    claim_map = load_json(CLAIM_MAP_PATH)
    task = load_json(TASK_PATH)

    equal("metadata.task", metadata["task"], TASK_ID)
    equal("metadata.versioned_id", metadata["source_identity"]["versioned_id"], "2512.07771v2")
    equal("metadata.title", metadata["source_identity"]["title"], "Loop Corrected Supercharges from Holomorphic Anomalies")
    equal("metadata.authors", metadata["source_identity"]["authors"], ["Kasia Budzik", "Justin Kulp"])
    equal("metadata.v2_revision", metadata["source_identity"]["submission_history"][1], {"version": "v2", "timestamp_utc": "2026-03-19T17:24:36Z"})
    equal(
        "metadata.urls",
        metadata["urls"],
        {
            "abstract": "https://arxiv.org/abs/2512.07771v2",
            "html": "https://arxiv.org/html/2512.07771v2",
            "pdf": "https://arxiv.org/pdf/2512.07771v2",
            "source_archive": "https://export.arxiv.org/e-print/2512.07771v2",
        },
    )
    equal(
        "metadata.boundary",
        metadata["admissibility"],
        {
            "role": "EXTERNAL_TARGET_ONLY",
            "translation_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
            "comparison_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
            "project_formula_adoption": False,
            "project_contract_modified": False,
            "notion_read_performed": False,
        },
    )

    artifact_expected = [
        ("VERSIONED_PDF", "references/vendor/arxiv/2512.07771v2/2512.07771v2.pdf", 625721, "cb2a6f53c97dd0f706685fd123ef6eb6a909344b78b02769af78e90ccfcf1e35"),
        ("VERSIONED_TEX_SOURCE_ARCHIVE", ARCHIVE_PATH, 52452, "27d9eefd23fef109bb65be780c72a360d0df9ba90c5db1bc07ecf0b248a63632"),
    ]
    equal(
        "metadata.artifacts",
        [(x["role"], x["path"], x["byte_size"], x["sha256"]) for x in metadata["artifacts"]],
        artifact_expected,
    )
    for role, relative, size, digest in artifact_expected:
        path = ROOT / relative
        check(f"artifact.exists.{role}", path.is_file(), relative)
        equal(f"artifact.size.{role}", path.stat().st_size, size)
        equal(f"artifact.sha256.{role}", sha256_path(path), digest)

    metadata_files = [
        (x["archive_member_path"], x["extracted_path"], x["byte_size"], x["sha256"])
        for x in metadata["extraction"]["files"]
    ]
    equal("extraction.file_order", metadata_files, FILES)
    equal("extraction.regular_file_count", metadata["extraction"]["regular_file_count"], len(FILES))
    equal("extraction.directory_members", metadata["extraction"]["archive_directory_members"], ["images"])
    equal("extraction.ordering", metadata["extraction"]["ordering"], "LEXICOGRAPHIC_BY_ARCHIVE_MEMBER_PATH")

    extracted_actual = sorted(
        str(path.relative_to(ROOT))
        for path in (ROOT / SOURCE_ROOT).rglob("*")
        if path.is_file()
    )
    equal("extraction.no_omitted_or_extra_files", extracted_actual, [item[1] for item in FILES])
    for member, relative, size, digest in FILES:
        path = ROOT / relative
        check(f"source.exists.{member}", path.is_file(), relative)
        equal(f"source.size.{member}", path.stat().st_size, size)
        equal(f"source.sha256.{member}", sha256_path(path), digest)

    archive = ROOT / ARCHIVE_PATH
    with tarfile.open(archive, mode="r:gz") as tar:
        regular = sorted(member.name for member in tar.getmembers() if member.isfile())
        directories = sorted(member.name.rstrip("/") for member in tar.getmembers() if member.isdir())
        equal("archive.regular_members", regular, [item[0] for item in FILES])
        equal("archive.directory_members", directories, ["images"])
        check(
            "archive.safe_member_paths",
            all(not Path(member.name).is_absolute() and ".." not in Path(member.name).parts for member in tar.getmembers()),
            "absolute or parent-traversal member",
        )
        for member, relative, size, digest in FILES:
            handle = tar.extractfile(member)
            check(f"archive.readable.{member}", handle is not None, member)
            data = b"" if handle is None else handle.read()
            equal(f"archive.size.{member}", len(data), size)
            equal(f"archive.sha256.{member}", sha256_bytes(data), digest)
            equal(f"archive.extracted_byte_identity.{member}", data, (ROOT / relative).read_bytes())

    equal("ledger.task", ledger["task"], TASK_ID)
    equal("ledger.source.versioned_id", ledger["source"]["versioned_id"], "arXiv:2512.07771v2")
    equal("ledger.source.primary_tex", ledger["source"]["primary_tex_path"], MAIN_TEX_PATH)
    equal("ledger.source.primary_tex_sha256", ledger["source"]["primary_tex_sha256"], FILES[6][3])
    equal(
        "ledger.boundary",
        ledger["admissibility"],
        {
            "role": "EXTERNAL_TARGET_ONLY",
            "translation_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
            "comparison_status": "NOT_PERFORMED_IN_REFERENCE_IMPORT",
            "project_formula_adoption": False,
            "project_notation_used": False,
            "project_contract_modified": False,
            "normalization_conflicts_resolved": False,
        },
    )

    anchors = ledger["anchors"]
    equal("ledger.anchor_order", [row["id"] for row in anchors], [row[0] for row in ANCHORS])
    tex_lines = (ROOT / MAIN_TEX_PATH).read_bytes().splitlines(keepends=True)
    for row, (anchor_id, start, end, size, digest) in zip(anchors, ANCHORS, strict=True):
        equal(f"anchor.path.{anchor_id}", row["path"], MAIN_TEX_PATH)
        equal(f"anchor.start.{anchor_id}", row["start_line"], start)
        equal(f"anchor.end.{anchor_id}", row["end_line"], end)
        span = b"".join(tex_lines[start - 1 : end])
        equal(f"anchor.size.{anchor_id}", len(span), size)
        equal(f"anchor.recorded_size.{anchor_id}", row["byte_size"], size)
        equal(f"anchor.sha256.{anchor_id}", sha256_bytes(span), digest)
        equal(f"anchor.recorded_sha256.{anchor_id}", row["sha256"], digest)
        for label in row.get("equation_labels", []):
            check(f"anchor.label.{anchor_id}.{label}", f"\\label{{{label}}}".encode() in span, label)

    conflicts = ledger["source_internal_normalization_conflicts"]
    equal(
        "ledger.normalization_conflict_ids",
        [row["id"] for row in conflicts],
        ["HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT", "HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO"],
    )
    check("ledger.normalization_conflicts_unresolved", all(row["status"] == "UNRESOLVED_IN_SOURCE" for row in conflicts))
    equal("ledger.compact_compatibility_condition", conflicts[0]["algebraic_compatibility_condition_in_source_symbols"], "kappa^2=1/4")
    equal("ledger.zero_shift_discrepancy", conflicts[1]["algebraic_discrepancy_in_source_symbols"], "(kappa^2)-(kappa^2/2)=kappa^2/2")
    check("ledger.normalization_conflicts_not_translated", all("PROJECT_TRANSLATION" in row["resolution"] for row in conflicts))

    ordering = ledger["source_internal_ordering_audits"]
    equal("ledger.ordering_audit_count", len(ordering), 1)
    equal("ledger.ordering_audit_id", ordering[0]["id"], "HT-ORDERING-AUDIT-BB-VECTOR-TERM-SYMMETRY")
    equal("ledger.ordering_audit_status", ordering[0]["status"], "PASS")
    equal(
        "ledger.ordering_exact_chain",
        ordering[0]["source_internal_calculation"],
        [
            "P^D_(dot alpha)Lambda^(E dot alpha)=epsilon^(dot alpha dot beta)P^D_(dot alpha)Lambda^E_(dot beta).",
            "Because P is even, this equals epsilon^(dot alpha dot beta)Lambda^E_(dot beta)P^D_(dot alpha).",
            "Exchanging the dummy dotted indices gives epsilon^(dot beta dot alpha)Lambda^E_(dot alpha)P^D_(dot beta)=-S_ED.",
            "The vector term printed in equation (3.64) is therefore R_AB=kappa^2 F_ABDE(S_DE+S_ED).",
            "F_BADE=f_BCD f_ACE=f_ACE f_BCD=F_ABED.",
            "R_BA=kappa^2 F_ABED(S_DE+S_ED)=kappa^2 F_ABDE(S_ED+S_DE)=R_AB after D<->E relabelling.",
            "Thus the displayed vector output is symmetric under A<->B, consistent with b^A b^B=b^B b^A.",
        ],
    )
    equal("ledger.ordering_result", ordering[0]["result"], "SOURCE_INTERNAL_GRADED_SYMMETRY_VERIFIED")
    equal("ledger.ordering_not_translated", ordering[0]["project_translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")

    expected_claim_ids = list(EXPECTED_CLAIMS)
    equal("ledger.candidate_claim_ids", [row["id"] for row in ledger["candidate_claims"]], expected_claim_ids)
    check("ledger.claims_external_target_only", all(row["classification"] == "EXTERNAL_TARGET_ONLY" for row in ledger["candidate_claims"]))
    check("ledger.claims_not_adopted", all(row["adoption_status"] == "NOT_ADOPTED_IN_REFERENCE_IMPORT" for row in ledger["candidate_claims"]))

    metadata_digest = sha256_path(METADATA_PATH)
    ledger_digest = sha256_path(LEDGER_PATH)
    expected_manifest_rows = MANIFEST_ROWS_FIXED + [
        ("ARXIV-2512.07771V2-METADATA", str(METADATA_PATH.relative_to(ROOT)), "REFERENCE_ACQUISITION_METADATA_EXTERNAL_TARGET_ONLY", metadata_digest),
        ("HT-N4-ONE-LOOP-SOURCE-LEDGER", str(LEDGER_PATH.relative_to(ROOT)), "REFERENCE_SOURCE_LEDGER_EXTERNAL_TARGET_ONLY", ledger_digest),
    ]
    entries_by_id: dict[str, list[dict[str, Any]]] = {}
    for entry in manifest["entries"]:
        entries_by_id.setdefault(entry["id"], []).append(entry)
    for entry_id, relative, classification, digest in expected_manifest_rows:
        equal(f"manifest.unique.{entry_id}", len(entries_by_id.get(entry_id, [])), 1)
        if len(entries_by_id.get(entry_id, [])) == 1:
            equal(
                f"manifest.row.{entry_id}",
                entries_by_id[entry_id][0],
                {"id": entry_id, "path": relative, "classification": classification, "sha256": digest},
            )
    ht_manifest_ids = [entry["id"] for entry in manifest["entries"] if entry["id"].startswith("ARXIV-2512.07771V2-") or entry["id"] == "HT-N4-ONE-LOOP-SOURCE-LEDGER"]
    equal("manifest.exact_import_id_set", ht_manifest_ids, [row[0] for row in expected_manifest_rows])
    claim_map_entry = entries_by_id["REFERENCE-CLAIM-MAP"][0]
    equal("manifest.claim_map_hash", claim_map_entry["sha256"], sha256_path(CLAIM_MAP_PATH))

    mapped_by_id: dict[str, list[dict[str, Any]]] = {}
    for claim in claim_map["claims"]:
        mapped_by_id.setdefault(claim["id"], []).append(claim)
    for claim_id, expected in EXPECTED_CLAIMS.items():
        equal(f"claim_map.unique.{claim_id}", len(mapped_by_id.get(claim_id, [])), 1)
        if len(mapped_by_id.get(claim_id, [])) == 1:
            equal(f"claim_map.row.{claim_id}", mapped_by_id[claim_id][0], expected)
    ht_claim_ids = [claim["id"] for claim in claim_map["claims"] if claim["id"] in EXPECTED_CLAIMS]
    equal("claim_map.exact_candidate_ids", ht_claim_ids, expected_claim_ids)

    equal("task.id", task["id"], TASK_ID)
    equal("task.type", task["type"], "REFERENCE_IMPORT")
    check("task.status", task["status"] in {"SPECIFIED", "ACCEPTED"}, task["status"])
    equal("task.candidate_claim_ids", task["candidate_claim_ids"], expected_claim_ids)
    equal("task.reference_role", task["reference_exception"]["role"], "EXTERNAL_TARGET_ONLY")
    equal("task.translation_status", task["reference_exception"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
    equal("task.comparison_status", task["reference_exception"]["comparison_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT")
    equal(
        "task.external_urls",
        [item for item in task["allowed_inputs"] if item.startswith("https://")],
        list(metadata["urls"].values()),
    )

    failed = sum(row["status"] == "FAIL" for row in checks)
    audit = {
        "schema": 1,
        "task": TASK_ID,
        "status": "PASS" if failed == 0 else "FAIL",
        "totals": {
            "checks": len(checks),
            "failed": failed,
            "archive_regular_files": len(FILES),
            "source_anchors": len(ANCHORS),
            "candidate_claims": len(EXPECTED_CLAIMS),
            "source_internal_normalization_conflicts": len(conflicts),
            "source_internal_ordering_audits": len(ordering),
        },
        "checks": checks,
    }
    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit["totals"], sort_keys=True))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
