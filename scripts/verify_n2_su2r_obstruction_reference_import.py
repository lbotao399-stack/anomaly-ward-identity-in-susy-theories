#!/usr/bin/env python3
"""Exact verifier for the scoped N=2 SU(2)_R obstruction-note import."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references/vendor/local/N2_SYM_offshell_SU2R_obstruction_lecture_note.tex"
LEDGER = ROOT / "references/n2-su2r-obstruction-note-source-ledger.json"
MANIFEST = ROOT / "references/manifest.yaml"
CLAIM_MAP = ROOT / "references/claim-map.yaml"
TASK_CANDIDATES = (
    ROOT / "tasks/CURRENT.yaml",
    ROOT / "tasks/archive/REFERENCE-IMPORT-N2-SU2R-OBSTRUCTION-NOTE-001.yaml",
)
AUDIT = ROOT / "audits/n2-su2r-obstruction-reference-import-verification.json"

TASK_ID = "REFERENCE-IMPORT-N2-SU2R-OBSTRUCTION-NOTE-001"
SOURCE_ID = "N2-SU2R-OBSTRUCTION-LECTURE-NOTE-TEX"
SOURCE_SHA256 = "cc5abc773174305472acfe06b14f3d63229ffcfba9ed70f55ff3d3b534be26e6"
SOURCE_LOCATOR = (
    "attachment://N2_SYM_offshell_SU2R_obstruction_lecture_note.tex"
    "#sha256=" + SOURCE_SHA256
)
CLAIM_IDS = (
    "N2-SU2R-GRADED-ORDERING-CANDIDATE",
    "N2-SU2R-CANONICAL-PACKAGE-CANDIDATE",
    "N2-SU2R-PATCH-CHECKLIST-CANDIDATE",
    "N2-SU2R-EMBEDDED-EXTERNAL-CONTEXT",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[str] = []

    def check(self, name: str, actual: Any, expected: Any, category: str) -> None:
        passed = actual == expected
        self.checks.append(
            {
                "name": name,
                "category": category,
                "passed": passed,
                "actual": actual,
                "expected": expected,
            }
        )
        if not passed:
            self.failures.append(name)


def build_audit() -> dict[str, Any]:
    recorder = Recorder()
    source_bytes = SOURCE.read_bytes()
    source_text = source_bytes.decode("utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    claim_map = json.loads(CLAIM_MAP.read_text(encoding="utf-8"))
    task_path = next(
        path
        for path in TASK_CANDIDATES
        if path.exists() and json.loads(path.read_text(encoding="utf-8"))["id"] == TASK_ID
    )
    task = json.loads(task_path.read_text(encoding="utf-8"))

    recorder.check("source sha256", sha256(SOURCE), SOURCE_SHA256, "identity")
    recorder.check("source byte count", len(source_bytes), 32358, "identity")
    recorder.check("source line count", len(source_text.splitlines()), 1054, "identity")
    recorder.check("task id", task["id"], TASK_ID, "task")
    recorder.check("task type", task["type"], "REFERENCE_IMPORT", "task")
    recorder.check("task status", task["status"], "ACCEPTED", "task")
    exception = task["local_reference_exception"]
    recorder.check("user authorization", exception["user_authorized"], True, "task")
    recorder.check("source locator", exception["resolved_locator"], SOURCE_LOCATOR, "task")
    recorder.check("source locator hash", exception["resolved_sha256"], SOURCE_SHA256, "task")
    recorder.check(
        "write-only boundary restored",
        exception["default_boundary_after_task"],
        "GIT_TO_NOTION_ONLY",
        "task",
    )
    external_inputs = [item for item in task["allowed_inputs"] if "://" in item]
    recorder.check("single external handle", external_inputs, [SOURCE_LOCATOR], "task")
    recorder.check("Notion content forbidden", "Notion content" in task["forbidden_inputs"], True, "task")

    source = ledger["source"]
    recorder.check("ledger task", ledger["task"], TASK_ID, "ledger")
    recorder.check("ledger source hash", source["sha256"], SOURCE_SHA256, "ledger")
    recorder.check("ledger source bytes", source["bytes"], 32358, "ledger")
    recorder.check("ledger source lines", source["lines"], 1054, "ledger")
    recorder.check("ledger exact identity", source["identity_check"], "EXACT_BYTE_IDENTITY", "ledger")
    recorder.check(
        "translation not performed",
        ledger["source_scope"]["translation_status"],
        "NOT_PERFORMED_IN_REFERENCE_IMPORT",
        "boundary",
    )
    recorder.check("project formula not adopted", ledger["source_scope"]["project_formula_adoption"], False, "boundary")
    recorder.check("Step4 contract untouched", ledger["source_scope"]["step4_contract_modified"], False, "boundary")
    recorder.check("Step4 verifier untouched", ledger["source_scope"]["step4_verifier_modified"], False, "boundary")
    recorder.check("Notion not read", ledger["source_scope"]["notion_read_performed"], False, "boundary")
    recorder.check("web not read", ledger["source_scope"]["web_read_performed"], False, "boundary")
    recorder.check("candidate claim ids", tuple(item["id"] for item in ledger["candidate_claims"]), CLAIM_IDS, "claims")
    recorder.check(
        "candidate claims not adopted",
        [item["adoption_status"] for item in ledger["candidate_claims"][:3]],
        ["NOT_ADOPTED_IN_REFERENCE_IMPORT"] * 3,
        "claims",
    )
    recorder.check(
        "external context forbidden",
        ledger["candidate_claims"][3]["adoption_status"],
        "FORBIDDEN_UNTIL_SEPARATE_REFERENCE_IMPORT",
        "claims",
    )
    recorder.check(
        "embedded references not imported",
        [item["imported"] for item in ledger["embedded_external_references"]],
        [False, False, False],
        "boundary",
    )

    manifest_by_id = {item["id"]: item for item in manifest["entries"]}
    recorder.check("source registered", SOURCE_ID in manifest_by_id, True, "manifest")
    recorder.check("source manifest hash", manifest_by_id[SOURCE_ID]["sha256"], SOURCE_SHA256, "manifest")
    recorder.check(
        "ledger manifest hash",
        manifest_by_id["N2-SU2R-OBSTRUCTION-NOTE-SOURCE-LEDGER"]["sha256"],
        sha256(LEDGER),
        "manifest",
    )
    recorder.check(
        "claim-map manifest hash",
        manifest_by_id["REFERENCE-CLAIM-MAP"]["sha256"],
        sha256(CLAIM_MAP),
        "manifest",
    )
    claim_by_id = {item["id"]: item for item in claim_map["claims"]}
    recorder.check("claim-map ids present", [item in claim_by_id for item in CLAIM_IDS], [True] * 4, "claims")
    recorder.check(
        "claim-map source boundary",
        [claim_by_id[item]["sources"] for item in CLAIM_IDS],
        [[SOURCE_ID]] * 4,
        "claims",
    )

    markers = (
        "Removing the Off-Shell $SU(2)_R$ Pseudo-Obstruction",
        "Scope: PR \\#27, commit \\texttt{e814615}",
        "This note diagnoses and specifies a patch.",
        "\\section{Correct derivation in parameter-left order}",
        "\\section{Equivalent derivation in field-left order}",
        "\\section{Concrete verifier repair}",
        "\\section{Suggested patch checklist by file}",
        "\\bibitem{VanProeyen1995}",
        "\\bibitem{MartinPrimer}",
        "\\bibitem{ProjectPR}",
    )
    recorder.check("source markers exact", [marker in source_text for marker in markers], [True] * len(markers), "source")
    recorder.check(
        "import task excludes Step4 contract",
        [item for item in task["allowed_inputs"] if item.startswith("contracts/foundations/step-04")],
        [],
        "boundary",
    )
    recorder.check(
        "import task excludes Step4 verifier",
        "scripts/verify_step4_n2_closure.py" in task["allowed_inputs"],
        False,
        "boundary",
    )
    recorder.check(
        "import task forbids translation",
        any("translation of a candidate sign" in item for item in task["forbidden_inputs"]),
        True,
        "lifecycle",
    )

    categories: dict[str, dict[str, int]] = {}
    for check in recorder.checks:
        row = categories.setdefault(check["category"], {"checks": 0, "failed": 0})
        row["checks"] += 1
        if not check["passed"]:
            row["failed"] += 1
    return {
        "schema": 1,
        "task": TASK_ID,
        "status": "PASS" if not recorder.failures else "FAIL",
        "source": {
            "path": str(SOURCE.relative_to(ROOT)),
            "sha256": SOURCE_SHA256,
            "bytes": 32358,
            "lines": 1054,
        },
        "categories": categories,
        "totals": {"checks": len(recorder.checks), "failed": len(recorder.failures)},
        "checks": recorder.checks,
        "failures": recorder.failures,
    }


def main() -> None:
    audit = build_audit()
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2, ensure_ascii=False))
        raise SystemExit(1)
    print(f"N2 SU2R reference import: {audit['totals']['checks']} checks, 0 failures")


if __name__ == "__main__":
    main()
