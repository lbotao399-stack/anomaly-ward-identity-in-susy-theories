#!/usr/bin/env python3
"""Acceptance verifier for the Step-5 physical one-loop anomaly sector.

Only the target-blind 81-row Project anomaly ledger, its exact local
representative audits, the DRED cutting-failure calculation, and the
post-seal holomorphic-twist round trip are acceptance claims here.  Raw
q-functor, BV/WZ, open-color, formal-U, and general-color statements are
reported as OUT_OF_SCOPE and cannot be promoted by this verifier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-euclidean-n4-awi-verification.json"
TASK_ID = "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"
AUTHORITY_BASE = "00000f748fe4bdd1b5d122663cc1fb814faace66"
ACCEPTED_SCOPE = "PHYSICAL_ONE_LOOP_ANOMALY_SECTOR"

PROJECT_LEDGER = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.json"
AB_WARD = ROOT / "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json"
VECTOR_FRAME = ROOT / "audits/step5-ab-ba-vector-frame-missing-orbit-exact.json"
G3_MEASURE = ROOT / "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
HT_SYMBOLIC = ROOT / "audits/step5_global_81_ht_symbolic_roundtrip_exact.json"
DRED_MARKDOWN = ROOT / "audits/step5-dred-cutting-failure-exact.md"

OUT_OF_SCOPE = {
    "RAW_Q_FUNCTOR": "OUT_OF_SCOPE",
    "BV_WZ_COMPLETION": "OUT_OF_SCOPE",
    "OPEN_COLOR_SOURCE_EXTENSION": "OUT_OF_SCOPE",
    "FORMAL_U_INTERTWINER": "OUT_OF_SCOPE",
    "GENERAL_REDUCTIVE_COLOR_THEOREM": "OUT_OF_SCOPE",
}


@dataclass(frozen=True)
class Runner:
    check_id: str
    script: str
    arguments: tuple[str, ...]


RUNNERS = (
    Runner(
        "freshness.global_81_target_blind_ledger",
        "scripts/step5_global_81_target_blind_orbit_ledger_audit.py",
        ("--check",),
    ),
    Runner(
        "freshness.ab_ba_project_ward_finite_renormalization",
        "scripts/step5_ab_ba_project_ward_finite_renormalization_exact_audit.py",
        ("--check",),
    ),
    Runner(
        "freshness.ab_ba_vector_frame_missing_orbit",
        "scripts/step5_ab_ba_vector_frame_missing_orbit_exact_audit.py",
        ("--check",),
    ),
    Runner(
        "freshness.ab_ba_g3_original_full_measure",
        "scripts/step5_ab_ba_g3_original_full_measure_equivalence_exact_audit.py",
        ("--check",),
    ),
    Runner(
        "freshness.global_81_ht_symbolic_roundtrip",
        "scripts/step5_global_81_ht_symbolic_roundtrip_exact_audit.py",
        ("--check",),
    ),
    Runner(
        "freshness.dred_cutting_failure",
        "scripts/step5_dred_cutting_failure_exact_audit.py",
        (),
    ),
    Runner(
        "freshness.dred_mu2_triangle_moments",
        "scripts/step5_dred_mu2_triangle_moments_exact_audit.py",
        (),
    ),
)


def canonical_bytes(payload: Any) -> bytes:
    return (
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output_tail(text: str, maximum_lines: int = 8) -> list[str]:
    return [line for line in text.splitlines() if line.strip()][-maximum_lines:]


class Audit:
    def __init__(self) -> None:
        self.rows: list[dict[str, Any]] = []

    def check(self, check_id: str, condition: bool, detail: Any) -> None:
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if condition else "FAIL",
                "detail": detail,
            }
        )

    def protected(self, check_id: str, calculation: Any) -> None:
        try:
            condition, detail = calculation()
        except Exception as exc:  # malformed or missing evidence fails closed
            self.check(
                check_id,
                False,
                {"exception": type(exc).__name__, "message": str(exc)},
            )
        else:
            self.check(check_id, bool(condition), detail)


def run_freshness_gate(runner: Runner) -> tuple[bool, dict[str, Any]]:
    command = [sys.executable, str(ROOT / runner.script), *runner.arguments]
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=1800,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, {
            "script": runner.script,
            "arguments": list(runner.arguments),
            "exception": type(exc).__name__,
            "message": str(exc),
        }
    return completed.returncode == 0, {
        "script": runner.script,
        "arguments": list(runner.arguments),
        "returncode": completed.returncode,
        "stdout_tail": output_tail(completed.stdout),
        "stderr_tail": output_tail(completed.stderr),
    }


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"{path.relative_to(ROOT)} is not a JSON object")
    return payload


def check_authority(audit: Audit) -> None:
    def calculation() -> tuple[bool, Any]:
        is_ancestor = (
            subprocess.run(
                ["git", "merge-base", "--is-ancestor", AUTHORITY_BASE, "origin/main"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            ).returncode
            == 0
        )
        return is_ancestor, {
            "recorded_base": AUTHORITY_BASE,
            "relation": "recorded_base_is_ancestor_of_origin_main",
        }

    audit.protected("authority.frozen_base_is_ancestor_of_origin_main", calculation)


def check_project_ledger(audit: Audit, payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    rows = payload["rows"]
    audit.check(
        "project.target_blind_derivation",
        payload.get("external_target_used") is False
        and payload.get("project_result_ledger_used") is False,
        {
            "external_target_used": payload.get("external_target_used"),
            "project_result_ledger_used": payload.get("project_result_ledger_used"),
        },
    )
    audit.check(
        "project.global_81_counts",
        summary.get("ordered_pairs") == 81
        and summary.get("unique_pairs") == 81
        and summary.get("final_state_counts") == {"COMPLETE_EXACT": 81}
        and summary.get("resolution_counts")
        == {"EXACT_NONZERO": 29, "EXACT_ZERO": 52}
        and summary.get("representative_maturity_counts") == {"COMPLETED": 81},
        summary,
    )
    pair_ids = [row.get("pair_id") for row in rows]
    audit.check(
        "project.every_row_exact_and_evidenced",
        len(rows) == 81
        and len(set(pair_ids)) == 81
        and all(row.get("final_state") == "COMPLETE_EXACT" for row in rows)
        and all(row.get("representative_maturity") == "COMPLETED" for row in rows)
        and all(row.get("resolution") in {"EXACT_NONZERO", "EXACT_ZERO"} for row in rows)
        and all(row.get("result") is not None for row in rows)
        and all(row.get("blocker") is None for row in rows)
        and all(bool(row.get("cutting_failure_certificate")) for row in rows),
        {
            "rows": len(rows),
            "unique_pair_ids": len(set(pair_ids)),
            "nonzero": sum(row.get("resolution") == "EXACT_NONZERO" for row in rows),
            "zero": sum(row.get("resolution") == "EXACT_ZERO" for row in rows),
        },
    )


def check_ab_ward(audit: Audit, payload: dict[str, Any]) -> None:
    checks = payload["checks"]
    renormalized = payload["renormalized_result"]
    finite = payload["finite_normal_product"]
    after = payload["after_check_only"]
    exact = ["1", "1", "-sqrt(2)*i", "sqrt(2)*i"]
    audit.check(
        "ab_ba.finite_project_ward_audit",
        payload.get("status")
        == "PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__AB_BA_HT_CHECK_ONLY_EXACT_MATCH"
        and checks.get("count") == checks.get("passed") == 31
        and checks.get("failed") == 0
        and all(row.get("status") == "PASS" for row in checks.get("rows", [])),
        {"status": payload.get("status"), "checks": checks},
    )
    audit.check(
        "ab_ba.target_blind_then_ht_check_only",
        payload.get("external_target_used_in_derivation") is False
        and after.get("read_after_project_seal") == payload.get("project_seal_sha256")
        and after.get("status") == "EXACT_MATCH"
        and after.get("mismatches") == [],
        {
            "external_target_used_in_derivation": payload.get(
                "external_target_used_in_derivation"
            ),
            "project_seal_sha256": payload.get("project_seal_sha256"),
            "after_check_only": after,
        },
    )
    audit.check(
        "ab_ba.unique_finite_normal_product_and_exact_vector",
        finite.get("independent_anomaly_graph") is False
        and finite.get("vector")
        == ["1", "0", "sqrt(2)*i", "-sqrt(2)*i"]
        and renormalized.get("AB") == exact
        and renormalized.get("BA") == exact
        and after.get("HT_vector") == exact,
        {
            "finite_vector": finite.get("vector"),
            "AB": renormalized.get("AB"),
            "BA": renormalized.get("BA"),
            "HT": after.get("HT_vector"),
        },
    )


def check_vector_frame(audit: Audit, payload: dict[str, Any]) -> None:
    checks = payload["checks"]
    quotient = payload["quotient_layer_audit"]
    completion = payload["project_q_ward_completion"]
    finite = completion["general_finite_composite_source_counterterm"]
    audit.check(
        "ab_ba.vector_frame_exact_audit",
        payload.get("status")
        == "PASS_VECTOR_FRAME_ORBIT_HAS_ONLY_DB_BD_SUPPORT__CANNOT_SUPPLY_REQUESTED_CC_HALF"
        and payload.get("external_target_used") is False
        and checks.get("count") == checks.get("passed") == 40
        and checks.get("failed") == 0
        and all(row.get("status") == "PASS" for row in checks.get("rows", [])),
        {"status": payload.get("status"), "checks": checks},
    )
    audit.check(
        "ab_ba.vector_frame_missing_orbit_support",
        payload["one_loop_missing_orbit"].get("cc_support") == []
        and payload["one_loop_missing_orbit"].get("output_support")
        == ["phi1>u", "u>phi1"],
        {
            "cc_support": payload["one_loop_missing_orbit"].get("cc_support"),
            "output_support": payload["one_loop_missing_orbit"].get(
                "output_support"
            ),
        },
    )
    audit.check(
        "ab_ba.common_total_derivative_quotient",
        quotient.get("G1", {}).get("pair_EOM") == ["2", "2"]
        and quotient.get("G1", {}).get("pair_TD") == ["0", "2"]
        and quotient.get("G2", {}).get("pair_EOM_after_external_slot_swap")
        == ["-1/3", "4/3"]
        and quotient.get("G2", {}).get("pair_TD") == ["1", "4/3"]
        and quotient.get("common_compact_TD_vector")
        == ["0", "1", "-2*i*sqrt(2)", "2*i*sqrt(2)"]
        and quotient.get("hybrid_valid") is False,
        quotient,
    )
    audit.check(
        "ab_ba.vector_frame_project_settlement",
        finite.get("status")
        == "UNIQUE_PROJECT_WARD_AND_AA_SCALE_ONE_FINITE_SETTLEMENT"
        and finite.get("unique_solution")
        == ["1", "0", "i*sqrt(2)", "-i*sqrt(2)"]
        and finite.get("renormalized_vector")
        == ["1", "1", "-i*sqrt(2)", "i*sqrt(2)"]
        and finite.get("graph_support_restricted") is False,
        finite,
    )


def check_g3_measure(audit: Audit, payload: dict[str, Any]) -> None:
    checks = payload["checks"]
    verdict = payload["verdict"]
    audit.check(
        "ab_ba.g3_original_full_measure_exact",
        payload.get("status")
        == "PASS_G3_ORIGINAL_FULL_MEASURE_EQUIVALENCE__CONVERSION_MAGNITUDE_FOUR__TWO_SUPERTRACE_CYCLES_CANCEL_HALF__C_G3_4096"
        and payload.get("external_target_used") is False
        and payload.get("HT_used") is False
        and payload.get("desired_vector_fitting_used") is False
        and checks.get("count") == checks.get("passed") == 53
        and checks.get("failed") == 0
        and all(row.get("status") == "PASS" for row in checks.get("rows", [])),
        {"status": payload.get("status"), "checks": checks},
    )
    audit.check(
        "ab_ba.g3_measure_4096_not_2048",
        verdict
        == {
            "c_G3": "4096",
            "first_false_equality": "(1/2)*(C1+C2) -> (1/2)*C1",
            "original_equals_full_measure": True,
            "rejected_2048": True,
            "sign_comparison_with_ordered_H_derivation": (
                "engine conversion is +4; ordered-H conversion is -4 with "
                "Xi_ordered_H=-Xi_engine; converted word and scalar agree"
            ),
        },
        verdict,
    )


def check_ht_symbolic(audit: Audit, payload: dict[str, Any]) -> None:
    checks = payload["checks"]
    seal = payload["project_seal"]
    physical = payload["physical_81_roundtrip"]
    rows = physical["rows"]
    kernel = payload["arbitrary_jet_kernel"]
    finite = kernel["finite_rectangle"]
    lift = kernel["all_81_lift_corollary"]
    intrinsic = payload["intrinsic_AD_DA"]
    audit.check(
        "ht.symbolic_roundtrip_audit",
        payload.get("status")
        == "PASS_81_DIRECT_OUTPUT_WORDS_AND_ALL_MN_SYMBOLIC_KERNEL_EXACT"
        and checks.get("count") == checks.get("passed") == 8
        and checks.get("failed") == 0
        and all(row.get("status") == "PASS" for row in checks.get("rows", [])),
        {"status": payload.get("status"), "checks": checks},
    )
    audit.check(
        "ht.project_sealed_before_target_read",
        seal.get("sealed_before_ht_read") is True
        and seal.get("source")
        == "audits/step5-global-81-target-blind-orbit-ledger.json"
        and seal.get("source_sha256") == sha256(PROJECT_LEDGER),
        {**seal, "current_source_sha256": sha256(PROJECT_LEDGER)},
    )
    pair_ids = [row.get("id") for row in rows]
    audit.check(
        "ht.direct_81_coefficient_and_output_word_equality",
        physical.get("pair_count") == 81
        and physical.get("direct_row_matches") == 81
        and physical.get("direct_row_mismatches") == []
        and physical.get("nonzero_rows") == 29
        and physical.get("zero_rows") == 52
        and len(rows) == len(set(pair_ids)) == 81
        and all(row.get("exact_three_way_equal") is True for row in rows)
        and all(row.get("project_equals_ht_independent") is True for row in rows)
        and all(row.get("project_equals_ht_translated") is True for row in rows)
        and all(
            row.get("project_terms")
            == row.get("ht_independent_terms")
            == row.get("ht_translated_terms")
            for row in rows
        )
        and sum(len(row.get("project_terms", [])) for row in rows) == 70,
        {
            "pair_count": physical.get("pair_count"),
            "direct_row_matches": physical.get("direct_row_matches"),
            "mismatches": physical.get("direct_row_mismatches"),
            "nonzero_rows": physical.get("nonzero_rows"),
            "zero_rows": physical.get("zero_rows"),
            "output_words": sum(len(row.get("project_terms", [])) for row in rows),
        },
    )
    audit.check(
        "ht.all_nonnegative_m_n_symbolic_theorem",
        kernel.get("theorem")
        == (
            "for every m,n>=0 and every 0<=k<=m, 0<=ell<=n: "
            "K_Project=2*T_HT_printed=T_HT_corrected"
        )
        and kernel.get("domain")
        == "m,n in Z_{>=0}; 0<=k<=m; 0<=ell<=n"
        and kernel.get("printed_formula")
        == "T_HT_printed=binom(m,k)binom(n,ell)/((m+n+2)(k+ell+1))"
        and kernel.get("project_formula")
        == "K_Project=2binom(m,k)binom(n,ell)/((m+n+2)(k+ell+1))"
        and kernel.get("corrected_definition")
        == "T_HT_corrected:=2*T_HT_printed"
        and len(kernel.get("symbolic_proof", [])) == 4,
        {
            "theorem": kernel.get("theorem"),
            "domain": kernel.get("domain"),
            "printed_formula": kernel.get("printed_formula"),
            "project_formula": kernel.get("project_formula"),
            "corrected_definition": kernel.get("corrected_definition"),
            "symbolic_proof": kernel.get("symbolic_proof"),
        },
    )
    audit.check(
        "ht.finite_exact_regression_and_full_81_lift",
        finite.get("max_m") == finite.get("max_n") == 8
        and finite.get("mn_points") == 81
        and finite.get("coefficient_checks") == 2025
        and finite.get("mismatches") == 0
        and lift.get("all_nonnegative_m_n") is True
        and lift.get("base_rows") == 81
        and lift.get("base_output_words") == 70
        and lift.get("finite_rectangle_lifted_coefficient_checks") == 141750
        and intrinsic.get("row_count") == 4
        and intrinsic.get("mismatches") == 0
        and all(
            row.get("exact_project_independent_ht_equal") is True
            for row in intrinsic.get("rows", [])
        ),
        {"finite_rectangle": finite, "all_81_lift_corollary": lift, "intrinsic_AD_DA": intrinsic},
    )


def check_dred(audit: Audit, runner_results: dict[str, dict[str, Any]]) -> None:
    cutting = runner_results["freshness.dred_cutting_failure"]
    moments = runner_results["freshness.dred_mu2_triangle_moments"]
    text = DRED_MARKDOWN.read_text(encoding="utf-8")
    cutting_lines = cutting.get("stdout_tail", [])
    moments_lines = moments.get("stdout_tail", [])
    audit.check(
        "dred.full_square_schwinger_cancellation_and_finite_mu2_master",
        "SUMMARY 32/32 PASS" in cutting_lines
        and all(
            token in text
            for token in (
                r"\mu_\ell^2=-\widehat\ell_{\rm user}^{\,2}",
                r"\Gamma_{G,i}^{(d)}",
                r"\frac{\bar r_i^{\,2}-r_{i,d}^{\,2}}",
                r"\frac1{32\pi^2}",
                "premature dimensional-continuation error",
            )
        ),
        {
            "summary": cutting_lines,
            "identity": "bar(r_e)^2-r_(e,d)^2=mu_l^2",
            "full_d_square_plus_Schwinger_cut": "0",
            "J_mu2": "1/(32*pi^2)",
        },
    )
    audit.check(
        "dred.mu2_triangle_tensor_moments",
        "SUMMARY 23/23 PASS" in moments_lines,
        {"summary": moments_lines},
    )


def evidence_payloads(audit: Audit) -> dict[str, dict[str, Any]]:
    paths = {
        "project": PROJECT_LEDGER,
        "ab_ward": AB_WARD,
        "vector": VECTOR_FRAME,
        "g3": G3_MEASURE,
        "ht": HT_SYMBOLIC,
    }
    payloads: dict[str, dict[str, Any]] = {}
    for name, path in paths.items():
        try:
            payloads[name] = load_json(path)
        except Exception as exc:
            audit.check(
                f"evidence.{name}.readable_json",
                False,
                {
                    "path": str(path.relative_to(ROOT)),
                    "exception": type(exc).__name__,
                    "message": str(exc),
                },
            )
    return payloads


def build_audit() -> dict[str, Any]:
    audit = Audit()
    check_authority(audit)

    runner_results: dict[str, dict[str, Any]] = {}
    for runner in RUNNERS:
        passed, detail = run_freshness_gate(runner)
        runner_results[runner.check_id] = detail
        audit.check(runner.check_id, passed, detail)

    payloads = evidence_payloads(audit)
    if "project" in payloads:
        audit.protected(
            "project.semantic_payload",
            lambda: (check_project_ledger(audit, payloads["project"]) is None, "expanded checks"),
        )
    if "ab_ward" in payloads:
        audit.protected(
            "ab_ba.project_ward_semantic_payload",
            lambda: (check_ab_ward(audit, payloads["ab_ward"]) is None, "expanded checks"),
        )
    if "vector" in payloads:
        audit.protected(
            "ab_ba.vector_frame_semantic_payload",
            lambda: (check_vector_frame(audit, payloads["vector"]) is None, "expanded checks"),
        )
    if "g3" in payloads:
        audit.protected(
            "ab_ba.g3_semantic_payload",
            lambda: (check_g3_measure(audit, payloads["g3"]) is None, "expanded checks"),
        )
    if "ht" in payloads:
        audit.protected(
            "ht.semantic_payload",
            lambda: (check_ht_symbolic(audit, payloads["ht"]) is None, "expanded checks"),
        )
    audit.protected(
        "dred.semantic_payload",
        lambda: (check_dred(audit, runner_results) is None, "expanded checks"),
    )

    failed = [row for row in audit.rows if row["status"] == "FAIL"]
    status = "ACCEPTED" if not failed else "FAIL"
    evidence_paths = (
        PROJECT_LEDGER,
        AB_WARD,
        VECTOR_FRAME,
        G3_MEASURE,
        HT_SYMBOLIC,
        DRED_MARKDOWN,
        *(ROOT / runner.script for runner in RUNNERS),
    )
    hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in evidence_paths
        if path.is_file()
    }
    return {
        "schema": "awi.step5.physical-one-loop-anomaly-sector-verification.v1",
        "task": TASK_ID,
        "authority_base_commit": AUTHORITY_BASE,
        "status": status,
        "accepted_scope": ACCEPTED_SCOPE if status == "ACCEPTED" else None,
        "scope_boundary": {
            "accepted": [ACCEPTED_SCOPE],
            "out_of_scope": OUT_OF_SCOPE,
            "out_of_scope_items_are_not_acceptance_blockers": True,
        },
        "counts": {
            "ordered_pairs": 81,
            "exact_nonzero": 29,
            "exact_zero": 52,
            "direct_ht_rows": 81,
            "base_output_words": 70,
            "finite_symbolic_kernel_checks": 2025,
        },
        "exact_identity": (
            "full_d_square+Schwinger_cut=0; "
            "bar_loop_square-full_d_loop_square=mu_l^2; "
            "J_mu2=1/(32*pi^2)"
        ),
        "holomorphic_twist_identity": (
            "K_Project=2*T_HT_printed=T_HT_corrected for all m,n>=0"
        ),
        "excluded_obsolete_evidence": [
            "audits/step5-ab-ba-full-1pi-quotient-exact.json",
            "audits/step5-ab-ba-full-1pi-quotient-exact.md",
            "scripts/step5_ab_ba_full_1pi_quotient_exact_audit.py",
        ],
        "evidence_sha256": hashes,
        "totals": {
            "checks": len(audit.rows),
            "passed": len(audit.rows) - len(failed),
            "failed": len(failed),
        },
        "failed_checks": failed,
        "checks": audit.rows,
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    payload = build_audit()
    data = canonical_bytes(payload)
    if args.write:
        AUDIT.write_bytes(data)
    elif not AUDIT.is_file() or AUDIT.read_bytes() != data:
        print("stale Step-5 physical anomaly-sector verification audit", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": payload["status"],
                "accepted_scope": payload["accepted_scope"],
                **payload["counts"],
                **payload["totals"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == "ACCEPTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
