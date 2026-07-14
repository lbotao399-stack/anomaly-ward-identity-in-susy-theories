#!/usr/bin/env python3
"""Fail-closed verifier for the proposed Euclidean N=4 Step-5 AWI contract.

The verifier distinguishes three outcomes.

PASS
    Every algebraic check passes and every acceptance gate is closed.
BLOCKED
    Algebraic checks pass, but at least one declared proof obligation remains.
FAIL
    A deterministic artifact, count, coefficient, type map, or mutation check fails.

Holomorphic-twist data are read only through the admitted external-target
engine.  They are never used to determine a Project coefficient.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5"
AUDIT = ROOT / "audits/step5-euclidean-n4-awi-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-one-loop.md"
TASK_ID = "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"
AUTHORITY_BASE = "00000f748fe4bdd1b5d122663cc1fb814faace66"


def load_module(name: str, relative: str, *, optional: bool = False) -> Any | None:
    path = ROOT / relative
    if optional and not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PROJECT = load_module("step5_project_verify", "scripts/step5_project_anomaly_engine.py")
PHYSICAL = load_module("step5_physical_verify", "scripts/step5_physical_graph_engine.py")
STRUCTURAL = load_module("step5_structural_verify", "scripts/step5_graph_cut_engine.py")
HT = load_module("step5_ht_target_verify", "scripts/step5_ht_target_engine.py")
SEED = load_module("step5_seed_verify", "scripts/step5_canonical_superfield_ww_seed.py")
SHIFT = load_module("step5_shift_verify", "scripts/step5_project_shift_kernel_audit.py")
LINK_PBW = load_module("step5_link_pbw_verify", "scripts/step5_link_pbw_intertwiner_audit.py")
RESIDUAL_Q = load_module(
    "step5_residual_q_verify", "scripts/step5_residual_q_projection_audit.py"
)
COVARIANCE = load_module(
    "step5_covariance_verify", "scripts/step5_project_covariance_audit.py"
)
BRST = load_module("step5_brst_clean_verify", "scripts/step5_brst_clean_review.py")
MIXING = load_module("step5_mixing_verify", "scripts/step5_local_operator_mixing_audit.py")
EVANESCENT = load_module(
    "step5_evanescent_verify", "scripts/step5_evanescent_closure_review.py"
)
WW_POLE = load_module("step5_ww_pole_verify", "scripts/step5_ww_physical_cut_pole_audit.py")
TOPOLOGY = load_module(
    "step5_topology_verify", "scripts/step5_ww_topology_allocation_invariance_audit.py"
)
HT_ROUNDTRIP = load_module(
    "step5_ht_roundtrip_verify", "scripts/step5_ht_roundtrip_audit.py", optional=True
)
SLICE_NO_GO = load_module(
    "step5_slice_no_go_verify", "scripts/step5a_local_slice_dred_no_go_audit.py"
)
WZ_GATE = load_module(
    "step5_wz_gate_verify", "scripts/step5a_wz_component_bv_gate_audit.py"
)
Q_GRAPH_LIFT = load_module(
    "step5_q_graph_lift_verify", "scripts/step5_q_equivariant_graph_lift_audit.py"
)
EPSILON_MIXING = load_module(
    "step5_epsilon_mixing_verify", "scripts/step5_dred_epsilon_scalar_mixing_audit.py"
)


def canonical_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction(payload: Any) -> Fraction:
    if isinstance(payload, dict):
        return Fraction(int(payload["numerator"]), int(payload["denominator"]))
    return Fraction(payload)


class Audit:
    VALID = {"PASS", "BLOCKED", "FAIL"}

    def __init__(self) -> None:
        self.rows: list[dict[str, Any]] = []

    def add(self, check_id: str, status: str, detail: Any) -> None:
        if status not in self.VALID:
            raise ValueError(status)
        self.rows.append({"id": check_id, "status": status, "detail": detail})

    def check(self, check_id: str, condition: bool, detail: Any) -> None:
        self.add(check_id, "PASS" if condition else "FAIL", detail)

    def gate(self, check_id: str, closed: bool, detail: Any) -> None:
        self.add(check_id, "PASS" if closed else "BLOCKED", detail)

    def section(self, prefix: str) -> dict[str, int]:
        rows = [row for row in self.rows if row["id"].startswith(prefix)]
        return {
            "checks": len(rows),
            "passed": sum(row["status"] == "PASS" for row in rows),
            "blocked": sum(row["status"] == "BLOCKED" for row in rows),
            "failed": sum(row["status"] == "FAIL" for row in rows),
        }


def check_authority(audit: Audit) -> None:
    origin_main = subprocess.run(
        ["git", "rev-parse", "origin/main"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    audit.gate(
        "authority.origin_main_matches_recorded_base",
        origin_main == AUTHORITY_BASE,
        {"recorded_base": AUTHORITY_BASE, "origin_main": origin_main},
    )


def json_matches(path: Path, payload: Any) -> bool:
    return path.is_file() and path.read_bytes() == canonical_bytes(payload)


def check_contract(audit: Audit) -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    control = sorted({ord(ch) for ch in text if ord(ch) < 32 and ch not in "\n\t"})
    audit.check("contract.no_control_characters", not control, control)
    forbidden = ("\\sim", "\\approx", "After substitution", "after substitution")
    audit.check(
        "contract.no_forbidden_shortcuts",
        not any(token in text for token in forbidden),
        list(forbidden),
    )
    anchors = (
        "Status: `CONDITIONAL_WW_ARITHMETIC_CHECKED__EXPLICIT_D_WORD_RAW_ALL_CHANNEL_AND_RENORMALIZATION_BLOCKED`",
        "## 1. Notation and DRED",
        "## 4. Canonical WW seed",
        "## 7. Ordered component ledger",
        "## 9. Renormalization obstruction",
        "BLOCKED\\_STEP5A\\_LOCAL\\_FERMI\\_FEYNMAN\\_PROPER\\_SLICE",
        "BLOCKED\\_STEP5A\\_WZ\\_BV\\_REDUCTION\\_UNDEFINED",
        "BLOCKED\\_RAW\\_GRAPH\\_Q\\_EQUIVARIANT\\_LIFT",
        "BLOCKED\\_FINITE\\_MIXED\\_PRIMITIVE\\_RESIDUES",
        "BLOCKED\\_REFERENCE\\_INTERNAL\\_NORMALIZATION",
        "HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT",
        "HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO",
    )
    audit.check(
        "contract.required_fail_closed_anchors",
        all(token in text for token in anchors),
        list(anchors),
    )
    overclaims = (
        "Status: `ACCEPTED`",
        "Status: `RENORMALIZED`",
        "Status: `WARD_CLOSED`",
        "the complete one-loop answer is",
        "every printed zero-derivative component formula map exactly",
        "\\mathcal A_{ij}^{(1),\\rm noncut}=0",
    )
    audit.check(
        "contract.no_renormalized_overclaim",
        not any(token in text for token in overclaims),
        list(overclaims),
    )
    exact_snippets = (
        "\\mathcal K^P_{1,0}\n=\\frac13\\langle P_1f,g\\rangle",
        "\\mathcal K^P_{2,0}\n=\\frac16\\langle P_1^2f,g\\rangle",
        "\\mathcal K^P_{1,1}={}&\n\\frac16\\langle P_1P_2f,g\\rangle",
        "\\mathfrak p_{\\dot\\alpha}X",
    )
    audit.check(
        "contract.exact_typed_endpoint_weights",
        all(snippet in text for snippet in exact_snippets),
        list(exact_snippets),
    )


def check_project(audit: Audit) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    bundle = PROJECT.build_bundle()
    verification = bundle["project-verification.json"]
    ledger = bundle["project-result-ledger.json"]
    pairs = ledger["pairs"]
    audit.check(
        "project.authority_base",
        PROJECT.AUTHORITY_BASE_COMMIT == AUTHORITY_BASE,
        PROJECT.AUTHORITY_BASE_COMMIT,
    )
    audit.check("project.engine_status", verification["status"] == "PASS", verification["totals"])
    audit.check(
        "project.target_blind",
        all(payload.get("external_target_used") is not True for payload in bundle.values()),
        {name: payload.get("external_target_used") for name, payload in bundle.items()},
    )
    counts = (
        ledger["ordered_pair_count"],
        ledger["nonzero_count"],
        ledger["zero_count"],
    )
    audit.check("project.ordered_pair_counts", counts == (81, 29, 52), counts)
    audit.check(
        "project.pair_ids_unique",
        len(pairs) == len({row["id"] for row in pairs}) == 81,
        len({row["id"] for row in pairs}),
    )
    audit.check(
        "project.every_nonzero_has_physical_output",
        all(row["physical_outputs"] for row in pairs if not row["exact_zero"]),
        sum(bool(row["physical_outputs"]) for row in pairs),
    )
    audit.check(
        "project.every_zero_has_certificate",
        all(row["zero_certificate"] for row in pairs if row["exact_zero"]),
        sum(bool(row["zero_certificate"]) for row in pairs),
    )
    return bundle, pairs


def structural_signatures(structural: dict[str, Any]) -> Counter[tuple[str, str]]:
    return Counter(
        (row["pair_id"], row["compact_output"])
        for row in structural["cut-orbits.json"]["orbits"]
    )


def physical_signatures(ir: dict[str, Any]) -> Counter[tuple[str, str]]:
    out: Counter[tuple[str, str]] = Counter()
    for orbit in ir["orbits"]:
        kernel = orbit["members"][0]["compact_output_kernel"]
        out[(orbit["pair_id"], f"{kernel['left_output']}>{kernel['right_output']}")] += 1
    return out


def check_graphs(audit: Audit) -> tuple[dict[str, Any], dict[str, Any]]:
    structural = STRUCTURAL.build_outputs()
    structural_verification = structural["structural-graph-verification.json"]
    ir = PHYSICAL.build_ir()
    physical_verification = PHYSICAL.verify(ir)
    audit.check(
        "graph.structural_status",
        structural_verification["status"] == "PASS",
        structural_verification["counts"],
    )
    audit.check(
        "graph.structural_counts",
        structural_verification["counts"]
        == {
            "pairs": 81,
            "nonzero_pairs": 29,
            "zero_pairs": 52,
            "kernels": 66,
            "cut_orbits": 66,
            "graphs": 132,
        }
        and structural["graph-census.json"]["ordered_family_channels"] == 16,
        {
            "counts": structural_verification["counts"],
            "ordered_family_channels": structural["graph-census.json"][
                "ordered_family_channels"
            ],
        },
    )
    audit.check(
        "graph.structural_mutations",
        len(structural_verification["mutation_tests"]) == 4
        and all(row["status"] == "PASS" for row in structural_verification["mutation_tests"]),
        structural_verification["mutation_tests"],
    )
    audit.check(
        "graph.physical_structural_status",
        physical_verification["structural_status"] == "PASS",
        physical_verification["totals"],
    )
    physical_counts = (
        ir["ordered_pair_count"],
        ir["nonzero_pair_count"],
        ir["zero_pair_count"],
        ir["ordered_kernel_count"],
        ir["cut_orbit_count"],
        ir["graph_object_count"],
        ir["orientation_multiplicity"],
    )
    audit.check(
        "graph.physical_counts_no_orientation_double",
        physical_counts == (81, 29, 52, 66, 66, 132, 1),
        physical_counts,
    )
    audit.check(
        "graph.independent_census_equal",
        structural_signatures(structural) == physical_signatures(ir),
        {
            "structural": sum(structural_signatures(structural).values()),
            "physical": sum(physical_signatures(ir).values()),
        },
    )
    audit.check(
        "graph.cut_involution",
        all(
            orbit["cut_involution"][orbit["cut_involution"][member["graph_id"]]]
            == member["graph_id"]
            for orbit in ir["orbits"]
            for member in orbit["members"]
        ),
        "C_cut^2=1 on all 132 graph objects",
    )
    audit.gate(
        "graph.renormalized_completion",
        ir["status"] == "RENORMALIZED_COMPLETE",
        {"status": ir["status"], "completion_sectors": ir["completion_sectors"]},
    )
    return structural, ir


def check_slice_and_q_lift(audit: Audit) -> None:
    slice_no_go = SLICE_NO_GO.build()
    audit.check(
        "slice.local_completion_no_go_algebra",
        all(slice_no_go["checks"].values()),
        slice_no_go["checks"],
    )
    audit.check(
        "slice.local_completion_no_go_determinism",
        json_matches(ROOT / "audits/step5a-local-slice-dred-no-go.json", slice_no_go),
        "audits/step5a-local-slice-dred-no-go.json",
    )
    audit.gate(
        "slice.admissible_fermi_feynman_proper_completion",
        slice_no_go["result"] == "ADMISSIBLE_LOCAL_PROPER_FERMI_FEYNMAN_SLICE",
        {"result": slice_no_go["result"], "blocker": slice_no_go["blocker"]},
    )

    wz = WZ_GATE.build()
    audit.check("slice.wz_bv_gate_algebra", all(wz["checks"].values()), wz["checks"])
    audit.check(
        "slice.wz_bv_gate_determinism",
        json_matches(ROOT / "audits/step5a-wz-component-bv-gate.json", wz),
        "audits/step5a-wz-component-bv-gate.json",
    )
    audit.gate(
        "slice.wz_component_bv_reduction",
        wz["result"] == "ADMISSIBLE_WZ_COMPONENT_BV_REDUCTION",
        {"result": wz["result"], "blockers": wz["blockers"]},
    )

    q_lift = Q_GRAPH_LIFT.build_audit()
    audit.check(
        "graph.q_equivariant_lift_structural_audit",
        q_lift["structural_audit_status"] == "PASS"
        and not q_lift["baseline_failures"]
        and all(row["status"] == "PASS" for row in q_lift["mutation_tests"]),
        {
            "structural_status": q_lift["structural_audit_status"],
            "baseline_failures": q_lift["baseline_failures"],
            "mutations": q_lift["mutation_tests"],
        },
    )
    audit.check(
        "graph.q_equivariant_lift_determinism",
        json_matches(ROOT / "audits/step5-q-equivariant-graph-lift.json", q_lift),
        "audits/step5-q-equivariant-graph-lift.json",
    )
    audit.gate(
        "graph.raw_q_equivariant_lift",
        q_lift["status"] == "PASS_RAW_GRAPH_Q_EQUIVARIANT_LIFT",
        {
            "status": q_lift["status"],
            "verdict": q_lift["verdict"],
            "missing_raw_graph_words": q_lift["missing_raw_graph_words"],
        },
    )


def check_q_and_brst(audit: Audit) -> None:
    residual = RESIDUAL_Q.build_result()
    audit.check(
        "q.residual_projection_checks",
        residual["summary"]["failed"] == 0 and residual["summary"]["passed"] == 22,
        residual["summary"],
    )
    audit.check(
        "q.residual_projection_determinism",
        json_matches(ROOT / "audits/step5-residual-q-projection.json", residual),
        "audits/step5-residual-q-projection.json",
    )
    covariance = COVARIANCE.build_audit()
    audit.check(
        "q.covariance_kernel_checks",
        covariance["test_summary"] == {"passed": 12, "total": 12},
        covariance["test_summary"],
    )
    audit.check(
        "q.covariance_kernel_determinism",
        json_matches(ROOT / "audits/step5-project-covariance-kernel.json", covariance),
        "audits/step5-project-covariance-kernel.json",
    )

    actual_hashes = {
        relative: sha256(ROOT / relative) for relative in BRST.EXPECTED_INPUTS
    }
    brst_checks = {
        "input_hashes": actual_hashes == dict(BRST.EXPECTED_INPUTS),
        "link_endpoint_nilpotent": BRST.brst(BRST.brst(BRST.NCExpr.atom("U"))).terms == {},
        "dual_source_nilpotent": BRST.brst(BRST.brst(BRST.NCExpr.atom("J"))).terms == {},
        "first_jet_pairing": BRST.first_jet_pairing_check(),
        "second_jet_pairing": BRST.second_jet_pairing_check(),
        "path_derivative_symmetry": BRST.second_path_derivative_symmetry_check(),
        "adjoint_symmetric_trace": BRST.adjoint_symmetric_trace_check(),
        "evanescent_finite_part": BRST.laurent_finite_part_check(),
    }
    audit.check("brst.clean_algebra", all(brst_checks.values()), brst_checks)


def check_seed_and_cut(audit: Audit) -> None:
    seed = SEED.build_audit()
    audit.check(
        "dred.canonical_seed_arithmetic",
        seed["status"] == "PASS_ARITHMETIC_WITH_EXPLICIT_D_WORD_BLOCKER"
        and all(row["status"] == "PASS" for row in seed["checks"]),
        {"status": seed["status"], "checks": seed["checks"]},
    )
    seed_blockers = {row["id"] for row in seed["blockers"]}
    audit.gate(
        "dred.explicit_ww_d_algebra_word_derivation",
        "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION" not in seed_blockers,
        seed["blockers"],
    )
    audit.check(
        "dred.canonical_seed_determinism",
        json_matches(ROOT / "audits/step5-canonical-superfield-ww-seed.json", seed),
        "audits/step5-canonical-superfield-ww-seed.json",
    )
    pole = WW_POLE.build()
    audit.check(
        "dred.ww_pole_checks",
        all(row["status"] == "PASS" for row in pole["checks"]),
        {"status": pole["overall_status"], "checks": len(pole["checks"])},
    )
    audit.check(
        "dred.ww_pole_determinism",
        json_matches(ROOT / "audits/step5-ww-physical-cut-pole.json", pole),
        "audits/step5-ww-physical-cut-pole.json",
    )
    result = pole["result"]
    audit.check(
        "dred.metric_defect",
        result["metric_sum"].startswith("-hbar*g^2/(32*pi^2*epsilon)")
        and result["breve_contraction"]
        == "brevedelta^mu nu*T_mu rho nu*p^rho=-2*epsilon*sigma_rho*p^rho"
        and result["finite_defect"].startswith("+hbar*g^2/(16*pi^2)"),
        result,
    )
    topology = TOPOLOGY.build()
    audit.check(
        "dred.topology_allocation_checks",
        all(row["status"] == "PASS" for row in topology["checks"]),
        {"status": topology["overall_status"], "checks": len(topology["checks"])},
    )
    audit.check(
        "dred.topology_allocation_determinism",
        json_matches(ROOT / "audits/step5-ww-topology-allocation-invariance.json", topology),
        "audits/step5-ww-topology-allocation-invariance.json",
    )
    audit.gate(
        "dred.named_topology_numerical_table",
        topology["exact_blocker"]["id"]
        != "BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE",
        {"status": topology["overall_status"], "blocker": topology["exact_blocker"]},
    )


def check_shift_and_pbw(audit: Audit) -> None:
    shift = SHIFT.build()
    audit.check("jet.shift_kernel_status", shift["status"] == "PASS", shift["totals"])
    audit.check(
        "jet.shift_kernel_determinism",
        json_matches(ROOT / "audits/step5-project-shift-kernel.json", shift),
        "audits/step5-project-shift-kernel.json",
    )
    link = LINK_PBW.build()
    audit.check("jet.link_pbw_status", link["status"] == "PASS", link["totals"])
    audit.check(
        "jet.link_pbw_determinism",
        json_matches(ROOT / "audits/step5-link-pbw-intertwiner.json", link),
        "audits/step5-link-pbw-intertwiner.json",
    )
    pbw_path = ROOT / "audits/step5-pbw-jet-audit.json"
    pbw = json.loads(pbw_path.read_text(encoding="utf-8"))
    audit.check(
        "jet.pbw_linear_isomorphism_degree_0_4",
        pbw["authority_base"] == AUTHORITY_BASE
        and all(
            row["word_dimension"] == row["symmetric_dimension"] == 2**degree
            and row["forward_inverse"] == row["inverse_forward"] == "PASS"
            for degree, row in ((int(key), value) for key, value in pbw["degree_audit"].items())
        ),
        pbw["degree_audit"],
    )
    audit.check(
        "jet.pbw_star_checks",
        pbw["star_intertwining"] == {
            "status": "PASS",
            "exact_rational": True,
            "maximum_total_degree": 4,
            "pairs_checked": 129,
        }
        and pbw["star_associativity"] == {
            "status": "PASS",
            "exact_rational": True,
            "maximum_total_degree": 4,
            "triples_checked": 351,
        },
        {
            "intertwining": pbw["star_intertwining"],
            "associativity": pbw["star_associativity"],
        },
    )


def compact_ht_roundtrip(audit: Audit) -> None:
    project_actions = {row["id"]: row for row in PROJECT.compact_actions()}
    source_actions = HT.compact_normalized_actions()
    mapping: dict[str, tuple[str, Any]] = {
        "c": ("U", PROJECT.ONE),
        "b": ("A", -PROJECT.IMAGINARY_UNIT * PROJECT.INV_SQRT2),
    }
    for flavor in range(1, 4):
        mapping[f"gamma_{flavor}"] = (f"C{flavor}", PROJECT.ONE)
        mapping[f"beta_{flavor}"] = (f"B{flavor}", PROJECT.INV_SQRT2)
    coefficient_map = -PROJECT.INV_SQRT2
    mismatches: list[dict[str, Any]] = []
    for source in source_actions:
        left_input, left_scale = mapping[source["left_input"]]
        right_input, right_scale = mapping[source["right_input"]]
        project = project_actions[f"{left_input}__{right_input}"]
        predicted = []
        for output in source["normalized_compact_outputs"]:
            left_output, left_output_scale = mapping[output["left_output"]]
            right_output, right_output_scale = mapping[output["right_output"]]
            source_coefficient = PROJECT.rational(fraction(output["coefficient"]))
            coefficient = (
                coefficient_map
                * source_coefficient
                * left_output_scale
                * right_output_scale
                / (left_scale * right_scale)
            )
            predicted.append((left_output, right_output, PROJECT.exact_text(coefficient)))
        actual = [
            (row["left_output"], row["right_output"], row["coefficient_over_lambda"]["text"])
            for row in project["outputs"]
        ]
        if sorted(predicted) != sorted(actual):
            mismatches.append(
                {"pair": source["id"], "predicted": sorted(predicted), "actual": sorted(actual)}
            )
    audit.check(
        "ht.compact_roundtrip_64",
        len(source_actions) == 64 and not mismatches,
        {"pairs": len(source_actions), "mismatches": mismatches},
    )


def ordered_pair_ht_classification(audit: Audit, project_pairs: list[dict[str, Any]]) -> None:
    source_pairs = HT.build_pairs()["pairs"]
    project_by_id = {row["id"]: row for row in project_pairs}
    letter_map = {
        "B": "A",
        "P1": "B1",
        "P2": "B2",
        "P3": "B3",
        "G1": "C1",
        "G2": "C2",
        "G3": "C3",
        "Hdot1": "Ddot1",
        "Hdot2": "Ddot2",
    }
    mismatches = []
    for source in source_pairs:
        project_id = f"{letter_map[source['left']]}__{letter_map[source['right']]}"
        project = project_by_id[project_id]
        if source["exact_zero"] != project["exact_zero"]:
            mismatches.append((source["id"], project_id))
    audit.check(
        "ht.ordered_pair_classification_81",
        len(source_pairs) == 81 and not mismatches,
        {"pairs": len(source_pairs), "mismatches": mismatches},
    )


def derivative_ht_roundtrip(audit: Audit, maximum: int = 12) -> None:
    mismatches = []
    terms = 0
    for m in range(maximum + 1):
        for n in range(maximum + 1):
            source = HT.t_mn_terms(m, n)
            project = PROJECT.ordered_project_kernel_terms(m, n)
            if len(source) != len(project):
                mismatches.append({"m": m, "n": n, "reason": "term_count"})
                continue
            for source_term, project_term in zip(source, project, strict=True):
                terms += 1
                source_coefficient = fraction(source_term["coefficient"])
                project_coefficient = Fraction(project_term["coefficient"])
                if (
                    project_term["k"] != source_term["k"]
                    or project_term["ell"] != source_term["ell"]
                    or project_coefficient != 2 * source_coefficient
                ):
                    mismatches.append(
                        {
                            "m": m,
                            "n": n,
                            "source": str(source_coefficient),
                            "project": str(project_coefficient),
                        }
                    )
    audit.check(
        "ht.derivative_kernel_project_equals_two_printed_target",
        not mismatches,
        {
            "rectangle": [0, maximum, 0, maximum],
            "terms": terms,
            "identity": "K_Project=2*T_HT_printed",
            "mismatches": mismatches,
        },
    )


def check_ht(audit: Audit, project_pairs: list[dict[str, Any]]) -> None:
    with tempfile.TemporaryDirectory(dir=ROOT) as first, tempfile.TemporaryDirectory(
        dir=ROOT
    ) as second:
        first_root = Path(first)
        second_root = Path(second)
        HT.generate(first_root, 4)
        HT.generate(second_root, 4)
        names = sorted(path.name for path in first_root.iterdir())
        deterministic = names == sorted(path.name for path in second_root.iterdir())
        generated_equal = True
        for name in names:
            if name == "ht_generation_summary.json":
                left = json.loads((first_root / name).read_text())
                right = json.loads((second_root / name).read_text())
                left["output_directory"] = "<OUTPUT_DIRECTORY>"
                right["output_directory"] = "<OUTPUT_DIRECTORY>"
                deterministic = deterministic and left == right
                generated_path = GENERATED / name
                if generated_path.is_file():
                    generated = json.loads(generated_path.read_text())
                    generated["output_directory"] = "<OUTPUT_DIRECTORY>"
                    generated_equal = generated_equal and left == generated
                else:
                    generated_equal = False
            else:
                deterministic = deterministic and (first_root / name).read_bytes() == (
                    second_root / name
                ).read_bytes()
                generated_equal = generated_equal and (GENERATED / name).is_file()
                generated_equal = generated_equal and (GENERATED / name).read_bytes() == (
                    first_root / name
                ).read_bytes()
    audit.check("ht.external_target_engine_deterministic", deterministic, names)
    audit.check("ht.generated_target_artifacts_current", generated_equal, names)
    audit.check(
        "ht.external_target_role",
        HT.build_pairs()["authority_role"] == "EXTERNAL_TARGET_ONLY"
        and HT.build_conflicts()["authority_role"] == "EXTERNAL_TARGET_ONLY",
        "EXTERNAL_TARGET_ONLY",
    )
    compact_ht_roundtrip(audit)
    ordered_pair_ht_classification(audit, project_pairs)
    derivative_ht_roundtrip(audit)

    if HT_ROUNDTRIP is None:
        audit.gate(
            "ht.total_typed_roundtrip",
            False,
            "BLOCKED_STEP5_HT_ROUNDTRIP_AUDIT_MISSING",
        )
        return
    try:
        roundtrip = HT_ROUNDTRIP.build()
    except Exception as exc:  # fail closed on a present but non-runnable audit
        audit.add(
            "ht.roundtrip_audit_algebra",
            "FAIL",
            {"exception": type(exc).__name__, "message": str(exc)},
        )
        audit.gate(
            "ht.total_typed_roundtrip",
            False,
            "BLOCKED_STEP5_HT_ROUNDTRIP_AUDIT_NOT_RUNNABLE",
        )
        return
    checks_failed = roundtrip.get("totals", {}).get("checks_failed")
    audit.check(
        "ht.roundtrip_audit_algebra",
        checks_failed == 0,
        roundtrip.get("totals"),
    )
    audit.check(
        "ht.roundtrip_audit_determinism",
        json_matches(ROOT / "audits/step5-ht-roundtrip-audit.json", roundtrip),
        "audits/step5-ht-roundtrip-audit.json",
    )
    blockers = roundtrip.get("blockers", [])
    audit.gate(
        "ht.total_typed_roundtrip",
        roundtrip.get("status") == "PASS" and not blockers,
        {"status": roundtrip.get("status"), "blockers": blockers},
    )


def check_mixing(audit: Audit) -> None:
    mixing = MIXING.build_audit()
    audit.check(
        "mixing.algebra_tests",
        all(row["pass"] for row in mixing["tests"]),
        {"tests": len(mixing["tests"]), "status": mixing["status"]},
    )
    audit.check(
        "mixing.audit_determinism",
        json_matches(ROOT / "audits/step5-local-operator-mixing.json", mixing),
        "audits/step5-local-operator-mixing.json",
    )
    audit.check(
        "mixing.unique_physical_q_cocycle",
        mixing["dimension_9_over_2_block"]["joint_q_kernel_dimension"] == 1
        and mixing["counterterm_primitive_block"]["exact_covariance"]
        == "q_s Y_r=i delta_sr Z",
        {
            "kernel_dimension": mixing["dimension_9_over_2_block"][
                "joint_q_kernel_dimension"
            ],
            "primitive": mixing["counterterm_primitive_block"]["exact_covariance"],
        },
    )
    closure = EVANESCENT.build()
    audit.check(
        "mixing.evanescent_cross_review_tests",
        all(row["pass"] for row in closure["checks"]),
        {"checks": len(closure["checks"]), "status": closure["status"]},
    )
    audit.check(
        "mixing.evanescent_cross_review_determinism",
        json_matches(ROOT / "audits/step5-evanescent-closure-review.json", closure),
        "audits/step5-evanescent-closure-review.json",
    )
    gate_closed = (
        mixing["status"] == "PASS"
        and closure["verdict"]["renormalized_all_channel"] == "PROVED"
        and closure["verdict"]["z_EO"] == "PROVED_ZERO"
    )
    audit.gate(
        "mixing.renormalized_evanescent_closure",
        gate_closed,
        {
            "mixing_status": mixing["status"],
            "computed_verdict": mixing["one_loop_mixing"]["computed_verdict"],
            "numerical_status": mixing["minimal_dred_ms_insertion_block"][
                "numerical_status"
            ],
            "closure_status": closure["status"],
            "closure_verdict": closure["verdict"],
            "unexcluded_operator": closure["explicit_unexcluded_genuine_row"]["operator"],
        },
    )
    audit.gate(
        "mixing.mixed_projector_census",
        closure["not_proved_scope"].get("local_evanescent_kernel") == "PROVED",
        {
            "status": "BLOCKED_MIXED_PROJECTOR_CENSUS",
            "local_evanescent_kernel": closure["not_proved_scope"].get(
                "local_evanescent_kernel"
            ),
            "witness": closure["explicit_unexcluded_genuine_row"],
        },
    )
    blocker_ids = {row["id"] for row in mixing["blockers"]}
    audit.gate(
        "brst.open_color_source_bv_completion",
        "BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION" not in blocker_ids,
        next(
            (
                row
                for row in mixing["blockers"]
                if row["id"] == "BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION"
            ),
            "PROVED",
        ),
    )

    epsilon_mixing = EPSILON_MIXING.build()
    audit.check(
        "mixing.epsilon_scalar_projector_tests",
        all(row["pass"] for row in epsilon_mixing["tests"]),
        {
            "status": epsilon_mixing["status"],
            "tests": len(epsilon_mixing["tests"]),
        },
    )
    audit.check(
        "mixing.epsilon_scalar_projector_determinism",
        json_matches(
            ROOT / "audits/step5-dred-epsilon-scalar-mixing.json",
            epsilon_mixing,
        ),
        "audits/step5-dred-epsilon-scalar-mixing.json",
    )
    rows = epsilon_mixing["minimal_projector_split"]["rows"]
    audit.check(
        "mixing.minimal_projector_split_5_plus_3",
        len(rows) == 8
        and sum(row["family"] == "DA" for row in rows) == 5
        and sum(row["family"] == "BC" for row in rows) == 3,
        epsilon_mixing["minimal_projector_split"],
    )
    audit.check(
        "mixing.double_breve_enumerated_delta_classes_zero",
        set(epsilon_mixing["A_bb_enumerated_delta_zero"]["scope"])
        == {
            "CHI_TADPOLE",
            "A_HAT_CHICHI_DIRECT",
            "A_HAT_CHICHI_EXCHANGE",
        }
        and epsilon_mixing["A_bb_enumerated_delta_zero"]["direct"]
        == "Sigma^ij delta_ik delta_jl delta_kl=Sigma^ij delta_ij=0"
        and epsilon_mixing["A_bb_enumerated_delta_zero"]["exchange"]
        == "Sigma^ij delta_il delta_jk delta_kl=Sigma^ij delta_ij=0"
        and epsilon_mixing["A_bb_enumerated_delta_zero"]["contact_tadpole"]
        == "Sigma^ij delta_ij=0"
        and epsilon_mixing["A_bb_enumerated_delta_zero"]["full_row_conclusion"]
        == "NOT_PROVED"
        and epsilon_mixing["A_bb_enumerated_delta_zero"]["full_row_status"]
        == "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES",
        epsilon_mixing["A_bb_enumerated_delta_zero"],
    )
    epsilon_blockers = {row["id"] for row in epsilon_mixing["blockers"]}
    audit.gate(
        "mixing.complete_bv_dred_evanescent_basis",
        "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS" not in epsilon_blockers,
        epsilon_mixing["blockers"],
    )
    audit.gate(
        "mixing.finite_mixed_primitive_residues",
        "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES" not in epsilon_blockers,
        {
            "blockers": epsilon_mixing["blockers"],
            "conditional_pole_statement": epsilon_mixing["one_loop_pole_vs_finite"],
            "no_double_count_boundary": epsilon_mixing["no_double_count"],
        },
    )


def check_generated_determinism(
    audit: Audit,
    project_bundle: dict[str, Any],
    structural: dict[str, Any],
    ir: dict[str, Any],
) -> None:
    for name, payload in project_bundle.items():
        audit.check(
            f"determinism.project.{name}",
            json_matches(GENERATED / name, payload),
            str((GENERATED / name).relative_to(ROOT)),
        )
    for name, payload in structural.items():
        audit.check(
            f"determinism.structural.{name}",
            json_matches(GENERATED / name, payload),
            str((GENERATED / name).relative_to(ROOT)),
        )
    physical_payloads = {
        "physical-graph-ir.json": canonical_bytes(ir),
        "physical-graph-verification.json": canonical_bytes(PHYSICAL.verify(ir)),
        "physical-graph-atlas.md": PHYSICAL.atlas(ir).encode(),
    }
    for name, data in physical_payloads.items():
        path = GENERATED / name
        audit.check(
            f"determinism.physical.{name}",
            path.is_file() and path.read_bytes() == data,
            str(path.relative_to(ROOT)),
        )


def build_audit() -> dict[str, Any]:
    audit = Audit()
    check_authority(audit)
    check_contract(audit)
    project_bundle, project_pairs = check_project(audit)
    check_q_and_brst(audit)
    structural, ir = check_graphs(audit)
    check_slice_and_q_lift(audit)
    check_seed_and_cut(audit)
    check_shift_and_pbw(audit)
    check_ht(audit, project_pairs)
    check_mixing(audit)
    check_generated_determinism(audit, project_bundle, structural, ir)

    failed = [row for row in audit.rows if row["status"] == "FAIL"]
    blocked = [row for row in audit.rows if row["status"] == "BLOCKED"]
    status = "FAIL" if failed else "BLOCKED" if blocked else "PASS"
    prefixes = (
        "authority.",
        "contract.",
        "project.",
        "q.",
        "brst.",
        "graph.",
        "dred.",
        "jet.",
        "ht.",
        "mixing.",
        "determinism.",
    )
    return {
        "schema": 2,
        "task": TASK_ID,
        "authority_base_commit": AUTHORITY_BASE,
        "status": status,
        "contract": {
            "path": str(CONTRACT.relative_to(ROOT)),
            "sha256": sha256(CONTRACT),
        },
        "engines": {
            path.name: sha256(path)
            for path in sorted((ROOT / "scripts").glob("step5_*.py"))
            if path.name
            not in {
                "step5_brst_counterterm_closure_audit.py",
                "step5_cut_exhaustion_audit.py",
                "step5_ww_seed_engine.py",
            }
        },
        "excluded_obsolete_or_contaminated_engines": [
            "scripts/step5_brst_counterterm_closure_audit.py",
            "scripts/step5_cut_exhaustion_audit.py",
            "scripts/step5_ww_seed_engine.py",
        ],
        "totals": {
            "checks": len(audit.rows),
            "passed": len(audit.rows) - len(failed) - len(blocked),
            "blocked": len(blocked),
            "failed": len(failed),
            "ordered_family_channels": 16,
            "ordered_pairs": 81,
            "nonzero_pairs": 29,
            "zero_pairs": 52,
            "compact_ordered_kernels": 66,
            "compact_cut_representatives": 66,
            "compact_representative_graph_objects": 132,
        },
        "blocking_gates": [row for row in blocked],
        "failed_checks": [row for row in failed],
        "audit_sections": {prefix: audit.section(prefix) for prefix in prefixes},
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
        print("stale Step-5 verification audit", file=sys.stderr)
        return 1

    print(json.dumps({"status": payload["status"], **payload["totals"]}, indent=2, sort_keys=True))
    if payload["status"] == "PASS":
        return 0
    if payload["status"] == "BLOCKED":
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
