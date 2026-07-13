#!/usr/bin/env python3
"""Machine firewall between Step-6 derivation artifacts and review/target files.

The check is deliberately syntactic.  It certifies that the executable Step-6
source and generated derivation artifacts do not name, import, or byte-copy the
denied review/target inputs.  It does not claim anything about a human author's
memory or about the correctness of the independent calculation.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


SCHEMA = "step6.external_target_firewall.v1"
STATUS = "PASS_SYNTACTIC_DERIVATION_INPUT_ISOLATION"
DENIED_ROOTS = ("tasks/reviews", "references/external-targets")
DENIED_SEMANTIC_TOKENS = (
    "EXTERNAL_TARGET_NOT_DERIVATION",
    "2207.14321",
    "2306.01039",
    "2512.07771",
    "holomorphic-twist target",
    "holomorphic twist target",
)
DERIVATION_GENERATED_DIRS = (
    "generated/step6/two-loop-graphir",
    "generated/step6/two-loop-grammar",
    "generated/step6/two-loop-forest",
    "generated/step6/two-loop-wick",
    "generated/step6/two-loop-ghost-census",
    "generated/step6/two-loop-dword",
    "generated/step6/external-projection",
    "generated/step6/two-loop-integrals",
    "generated/step6/two-loop-amplitude-ir",
    "generated/step6/symbolic-grassmann-oracle",
    "generated/step6/coefficient-tensor",
    "generated/step6/two-loop-color-tensor",
    "generated/step6/global-supertensor",
    "generated/step6/sd-orbit",
    "generated/step6/dred-reducer",
    "generated/step6/bitriangle-master",
    "generated/step6/full-supertensor",
    "generated/step6/global-dword-adapter",
    "generated/step6/color-jacobi",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256_bytes(canonical_json(value).encode("utf-8"))


def relative_files(root: Path, relative_root: str) -> list[Path]:
    directory = root / relative_root
    if not directory.exists():
        return []
    return sorted(path for path in directory.rglob("*") if path.is_file())


def review_ledger(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for denied_root in DENIED_ROOTS:
        for path in relative_files(root, denied_root):
            payload = path.read_bytes()
            records.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "sha256": sha256_bytes(payload),
                    "byte_count": len(payload),
                    "role": "DENIED_DERIVATION_INPUT_GAP_REVIEW_ONLY",
                }
            )
    return records


def step6_source_files(root: Path) -> list[Path]:
    files = sorted((root / "scripts").glob("step6_*.py"))
    return [path for path in files if path.name != Path(__file__).name]


def string_literals(path: Path) -> Iterable[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            yield node.value


def source_violations(root: Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    forbidden = DENIED_ROOTS + DENIED_SEMANTIC_TOKENS
    for path in step6_source_files(root):
        for literal in string_literals(path):
            for token in forbidden:
                if token.casefold() in literal.casefold():
                    violations.append(
                        {
                            "path": path.relative_to(root).as_posix(),
                            "token": token,
                            "literal_sha256": sha256_bytes(literal.encode("utf-8")),
                        }
                    )
    return violations


def derivation_artifact_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for relative_root in DERIVATION_GENERATED_DIRS:
        files.extend(relative_files(root, relative_root))
    return sorted(set(files))


def artifact_violations(
    root: Path, review_records: list[dict[str, Any]]
) -> list[dict[str, str]]:
    denied_hashes = {str(record["sha256"]) for record in review_records}
    violations: list[dict[str, str]] = []
    for path in derivation_artifact_files(root):
        payload = path.read_bytes()
        text = payload.decode("utf-8", errors="replace")
        relative = path.relative_to(root).as_posix()
        artifact_hash = sha256_bytes(payload)
        if artifact_hash in denied_hashes:
            violations.append(
                {
                    "path": relative,
                    "token": "EXACT_DENIED_FILE_HASH",
                    "evidence_sha256": artifact_hash,
                }
            )
        for denied_root in DENIED_ROOTS:
            if denied_root.casefold() in text.casefold():
                violations.append(
                    {
                        "path": relative,
                        "token": denied_root,
                        "evidence_sha256": artifact_hash,
                    }
                )
        for token in DENIED_SEMANTIC_TOKENS:
            if token.casefold() in text.casefold():
                violations.append(
                    {
                        "path": relative,
                        "token": token,
                        "evidence_sha256": artifact_hash,
                    }
                )
        for denied_hash in denied_hashes:
            if denied_hash in text:
                violations.append(
                    {
                        "path": relative,
                        "token": "DECLARED_DENIED_DEPENDENCY_HASH",
                        "evidence_sha256": denied_hash,
                    }
                )
    return violations


def build_firewall(root: Path) -> dict[str, Any]:
    reviews = review_ledger(root)
    source_files = step6_source_files(root)
    artifact_files = derivation_artifact_files(root)
    source_failures = source_violations(root)
    artifact_failures = artifact_violations(root, reviews)
    failures = source_failures + artifact_failures
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS if not failures else "FAIL_DERIVATION_INPUT_ISOLATION",
        "claim_scope": "SYNTACTIC_FILE_AND_DECLARED_HASH_ISOLATION_ONLY",
        "non_claims": [
            "NO_HUMAN_MEMORY_ISOLATION_CLAIM",
            "NO_PHYSICAL_CORRECTNESS_CLAIM",
            "NO_TWO_LOOP_COEFFICIENT_CLAIM",
        ],
        "denied_roots": list(DENIED_ROOTS),
        "denied_semantic_tokens": list(DENIED_SEMANTIC_TOKENS),
        "denied_input_ledger": reviews,
        "derivation_source_files": [
            path.relative_to(root).as_posix() for path in source_files
        ],
        "derivation_artifact_files": [
            path.relative_to(root).as_posix() for path in artifact_files
        ],
        "checks": {
            "source_string_literals_do_not_name_denied_inputs": not source_failures,
            "artifacts_do_not_copy_denied_files": not any(
                item["token"] == "EXACT_DENIED_FILE_HASH" for item in artifact_failures
            ),
            "artifacts_do_not_declare_denied_dependency_hashes": not any(
                item["token"] == "DECLARED_DENIED_DEPENDENCY_HASH"
                for item in artifact_failures
            ),
            "artifacts_do_not_contain_denied_paths_or_target_tokens": not any(
                item["token"]
                not in {"EXACT_DENIED_FILE_HASH", "DECLARED_DENIED_DEPENDENCY_HASH"}
                for item in artifact_failures
            ),
        },
        "violations": failures,
        "calculation_result": None,
        "anomaly_coefficient": None,
    }
    payload["firewall_hash"] = digest(payload)
    return payload


def write_outputs(root: Path) -> dict[str, Any]:
    payload = build_firewall(root)
    generated = root / "generated" / "step6" / "external-target-firewall"
    generated.mkdir(parents=True, exist_ok=True)
    target = generated / "external-target-firewall.json"
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    audit = {
        "schema": "step6.external_target_firewall.audit.v1",
        "status": "PASS" if payload["status"] == STATUS else "FAIL",
        "firewall_hash": payload["firewall_hash"],
        "check_count": len(payload["checks"]),
        "failure_count": len(payload["violations"]),
        "checks": payload["checks"],
    }
    audit_path = root / "audits" / "step6-external-target-firewall-verification.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    audit = write_outputs(root)
    print(json.dumps(audit, sort_keys=True))
    if args.check and audit["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
