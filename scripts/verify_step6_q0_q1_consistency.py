#!/usr/bin/env python3
"""Exact Phase-0 input-boundary audit for the Step-6 consistency condition.

The locked color product is

    (X cross Y)^A = c_(FG)^A X^F Y^G,

one ordered color monomial.  It is not a graded commutator.  The checker
loads the sealed 81-row target-blind ledger and checks whether the locked
inputs define both sides of (T.9).  They do not: the Euler-descendant Delta
maps, [nabla_minus,P_dot], and the nonlinear-word extension of Delta are not
locked.  It therefore seals a blocker, not a P0 against the ledger.

For diagnosis only, the checker also evaluates A__C1 after imposing three
explicit extra assumptions.  That conditional calculation is kept separate
from the contract-grade verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import product
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.json"
COVARIANCE_PATH = ROOT / "audits/step5-project-covariance-kernel.json"
AUDIT_PATH = ROOT / "audits/step6-q0-q1-consistency.json"
TRACE_PATH = ROOT / "generated/step6/q0-q1-consistency.json"

LETTERS = ("A", "B1", "B2", "B3", "C1", "C2", "C3", "Ddot1", "Ddot2")
PARITY = {
    "A": 0,
    "B1": 1,
    "B2": 1,
    "B3": 1,
    "C1": 0,
    "C2": 0,
    "C3": 0,
    "Ddot1": 1,
    "Ddot2": 1,
}


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def epsilon3(i: int, j: int, k: int) -> int:
    if {i, j, k} != {1, 2, 3}:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


def verify_epsilon_lie_model() -> dict[str, Any]:
    """Verify, rather than import, the exact three-color witness."""

    for i, j, k in product(range(1, 4), repeat=3):
        value = epsilon3(i, j, k)
        if value != -epsilon3(j, i, k):
            raise ValueError("epsilon witness fails antisymmetry in slots 1,2")
        if value != -epsilon3(i, k, j):
            raise ValueError("epsilon witness fails antisymmetry in slots 2,3")

    for a, b, c, d in product(range(1, 4), repeat=4):
        jacobi = sum(
            epsilon3(a, b, h) * epsilon3(h, c, d)
            + epsilon3(b, c, h) * epsilon3(h, a, d)
            + epsilon3(c, a, h) * epsilon3(h, b, d)
            for h in range(1, 4)
        )
        if jacobi != 0:
            raise ValueError(f"epsilon witness fails Jacobi at {(a, b, c, d)}")

    def color_f(first: int, second: int, lower_d: int, lower_e: int) -> int:
        return sum(
            epsilon3(first, h, lower_d) * epsilon3(second, h, lower_e)
            for h in range(1, 4)
        )

    # T^(AB)_(GDE) = sum_F c^A_(FG) F^(FB)_(DE).
    external = {"A": 1, "B": 2, "G": 3, "D": 1, "E": 1}
    terms = []
    tensor_component = 0
    for f in range(1, 4):
        c_value = epsilon3(f, external["G"], external["A"])
        f_value = color_f(f, external["B"], external["D"], external["E"])
        contribution = c_value * f_value
        terms.append(
            {
                "F": f,
                "c^A_(F G)": c_value,
                "F^(F B)_(D E)": f_value,
                "product": contribution,
            }
        )
        tensor_component += contribution
    if tensor_component != 1:
        raise ValueError(f"nonzero color witness drift: {tensor_component}")

    return {
        "definition": "kappa_ab=delta_ab; c_abc=epsilon_abc for a,b,c in {1,2,3}",
        "verification": {
            "antisymmetry_exhaustive": True,
            "jacobi_exhaustive": True,
            "status": "PASS",
        },
        "component": external,
        "contraction": "T^(AB)_(GDE)=sum_F c^A_(FG) F^(FB)_(DE)",
        "summands": terms,
        "value": tensor_component,
    }


def load_ledger() -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    payload = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 81:
        raise ValueError("sealed ledger is not a complete 81-row list")

    expected = [(left, right) for left in LETTERS for right in LETTERS]
    observed = [(row.get("left"), row.get("right")) for row in rows]
    if observed != expected:
        raise ValueError("sealed ledger row order is not the canonical 9x9 product")

    by_id: dict[str, dict[str, Any]] = {}
    for ordinal, row in enumerate(rows, start=1):
        left, right = observed[ordinal - 1]
        pair_id = f"{left}__{right}"
        if row.get("ordinal") != ordinal or row.get("pair_id") != pair_id:
            raise ValueError(f"occurrence identity drift at ordinal {ordinal}")
        if row.get("parities") != [PARITY[left], PARITY[right]]:
            raise ValueError(f"parity drift at {pair_id}")
        by_id[pair_id] = row
    return payload, by_id


def coefficient(row: dict[str, Any], basis: str) -> sp.Expr:
    result = row.get("result", {})
    bases = result.get("basis", [])
    coefficients = result.get("coefficients_over_lambda1", [])
    if len(bases) != len(coefficients):
        raise ValueError(f"basis/coefficient drift at {row['pair_id']}")
    try:
        position = bases.index(basis)
    except ValueError as exc:
        raise ValueError(f"missing basis {basis!r} at {row['pair_id']}") from exc
    return sp.sympify(coefficients[position], locals={"I": sp.I})


def assert_zero_row(row: dict[str, Any]) -> None:
    result = row.get("result", {})
    values = [sp.sympify(item, locals={"I": sp.I}) for item in result.get("coefficients_over_lambda1", [])]
    if row.get("resolution") != "EXACT_ZERO" or any(value != 0 for value in values):
        raise ValueError(f"expected exact-zero row drift at {row['pair_id']}")


def locked_input_boundary() -> dict[str, Any]:
    covariance = json.loads(COVARIANCE_PATH.read_text(encoding="utf-8"))
    blocker_ids = {item["id"] for item in covariance.get("blockers", [])}
    required = {
        "BLOCKED_TREE_EULER_TO_COMPACT_DESCENDANT_MAP",
        "BLOCKED_LOCAL_COHOMOLOGY_COMPLEX_NOT_LOCKED",
    }
    if not required.issubset(blocker_ids):
        raise ValueError("locked covariance-boundary audit drift")
    conditional = covariance.get("conditional_intertwiner", {})
    assumptions = conditional.get("conditional_zero_if", [])
    if "[q_r,P]=0" not in assumptions:
        raise ValueError("locked conditional translation assumption drift")

    return {
        "status": "BLOCKED_PHASE0_CHAIN_MAP_ACTION_NOT_LOCKED",
        "missing_rules": [
            {
                "id": "MISSING_DELTA_ON_EULER_DESCENDANTS",
                "required": [
                    "Delta(nabla_plus(E_V),L)",
                    "Delta(L,nabla_plus(E_V))",
                    "Delta(E_tilde_r,L)",
                    "Delta(L,E_tilde_r)",
                ],
                "reason": "the work order retains the full tree descendants, but the 81-row ledger has only bottom-letter inputs",
            },
            {
                "id": "MISSING_NABLA_MINUS_TRANSLATION_COMMUTATOR",
                "required": "[nabla_minus,P_dot] on every translated output letter",
                "reason": "the locked covariance audit treats even [q_r,P]=0 as a conditional assumption; no nabla-minus analogue is fixed",
            },
            {
                "id": "MISSING_NONLINEAR_DELTA_EXTENSION",
                "required": "Delta(X_1...X_m,Y_1...Y_n) from the bilinear 81-row map",
                "reason": "(5A.61)-(5A.62) define ordered functional differentiation and leg permutation, not a Q1 biderivation",
            },
            {
                "id": "MISSING_Q1_STABLE_EOM_QUOTIENT",
                "required": "a declared BRST/EOM quotient stable under Q0 and Q1",
                "reason": "the locked covariance audit explicitly leaves the BRST/EOM quotient unspecified",
            },
        ],
        "locked_blocker_ids_used": sorted(required),
        "covariance_boundary_sha256": sha256_bytes(COVARIANCE_PATH.read_bytes()),
    }


def build_trace() -> dict[str, Any]:
    ledger, by_id = load_ledger()
    boundary = locked_input_boundary()

    passive_letters = ("C1", "C2", "C3", "Ddot1", "Ddot2")
    defined_pair_ids: list[str] = []
    for left in passive_letters:
        for right in passive_letters:
            pair_id = f"{left}__{right}"
            assert_zero_row(by_id[pair_id])
            defined_pair_ids.append(pair_id)
    if len(defined_pair_ids) != 25:
        raise ValueError("defined passive-row count drift")

    ac = by_id["A__C1"]
    if ac.get("resolution") != "EXACT_NONZERO":
        raise ValueError("A__C1 row is no longer exact-nonzero")
    if coefficient(ac, "(P_dot C_r)^D D^(E dot)") != -1:
        raise ValueError("A__C1 first coefficient drift")
    if coefficient(ac, "D_dot^D (P^dot C_r)^E") != 1:
        raise ValueError("A__C1 second coefficient drift")

    for flavor in range(1, 4):
        bc = by_id[f"B{flavor}__C1"]
        if flavor == 1:
            if coefficient(bc, "<D^D,D^E>") != 1:
                raise ValueError("B1__C1 coefficient drift")
        else:
            assert_zero_row(bc)
        assert_zero_row(by_id[f"C{flavor}__C1"])

    # Locked descendant in the physical Euler-operator quotient:
    # d A^A = -2 i sum_s c^A_(F G) B_s^F C_s^G.
    # The cross product is one ordered monomial.  In Delta(dA,C1), only the
    # B1 occurrence survives; every Delta(C_s,C1) and B_{2,3} row is zero.
    delta_d_coefficient = sp.expand(-2 * sp.I * coefficient(by_id["B1__C1"], "<D^D,D^E>"))
    d_delta_coefficient = sp.Integer(0)
    residual_coefficient = sp.expand(d_delta_coefficient - delta_d_coefficient)
    if delta_d_coefficient != -2 * sp.I or residual_coefficient != 2 * sp.I:
        raise ValueError("A__C1 residual coefficient drift")

    witness = verify_epsilon_lie_model()
    if residual_coefficient * witness["value"] == 0:
        raise ValueError("A__C1 residual witness unexpectedly vanishes")

    return {
        "schema": "awi.step6.q0-q1-phase0-blocker-trace.v3",
        "generated": True,
        "checked_equations": ["(T.9)", "(5A.2)", "(5A.61)-(5A.62)", "(6.1)-(6.6)"],
        "identity": "d Delta(A^A,C1^B) - Delta(d(A^A C1^B))_Koszul",
        "scope": "locked-input definability of the full Phase-0 chain-map identity",
        "sources": {
            "sealed_rows": str(LEDGER_PATH.relative_to(ROOT)),
            "sealed_rows_sha256": sha256_bytes(LEDGER_PATH.read_bytes()),
            "covariance_boundary": str(COVARIANCE_PATH.relative_to(ROOT)),
            "covariance_boundary_sha256": sha256_bytes(COVARIANCE_PATH.read_bytes()),
            "project_result_ledger_used": False,
        },
        "ledger_census": {
            "loaded_rows": len(ledger["rows"]),
            "canonical_order_verified": True,
        },
        "phase0_gate": {
            "status": boundary["status"],
            "contract_grade_evaluated_rows": 25,
            "contract_grade_passed_rows": 25,
            "contract_grade_blocked_rows": 56,
            "defined_pair_ids": defined_pair_ids,
            "downstream_phases": "NOT_RUN_AFTER_PHASE0_BLOCKER",
            "reason": "the C/C, C/D, D/C, and D/D zero rows are defined; every row containing A or B_r requires missing chain-map action",
        },
        "locked_input_boundary": boundary,
        "locked_color_semantics": {
            "cross_product": "(X cross Y)^A=c^A_(F G) X^F Y^G",
            "cross_is_single_ordered_monomial": True,
            "graded_commutator_used": False,
            "symbolic_tensor": "T^(AB)_(GDE)=sum_F c^A_(F G) F^(F B)_(D E)",
        },
        "conditional_diagnostic": {
            "status": "CONDITIONAL_NONZERO_NOT_A_P0",
            "pair_id": "A__C1",
            "ordinal": ac["ordinal"],
            "extra_assumptions": [
                "set E_V=E_tilde_r=0 in a Q1-stable quotient",
                "[nabla_minus,P_dot]=0",
                "extend Delta to composite words by literal occurrence replacement using (5A.61)",
            ],
            "dA_EOM_quotient": "-2*i*sum_(s,F,G) c^A_(F G) B_s^F C_s^G",
            "dC1": "0",
            "d_Delta": {
                "coefficient_over_lambda1_times_T": sp.sstr(d_delta_coefficient),
                "terms": [],
                "reason": "Delta(A,C1) contains only D, C1, and even translations; dD=dC1=0",
            },
            "Delta_d_Koszul": {
                "coefficient_over_lambda1_times_T": sp.sstr(delta_d_coefficient),
                "terms": [
                    {
                        "coefficient_over_lambda1_times_T": sp.sstr(delta_d_coefficient),
                        "left_word": ["D_dot^D", "C1^G"],
                        "right_word": ["D^(E dot)"],
                        "source_occurrence": "B1^F in B1^F C1^G",
                        "functional_derivative_sign_5A61": 1,
                    }
                ],
                "zero_occurrences": [
                    "Delta(B2,C1)=0",
                    "Delta(B3,C1)=0",
                    "Delta(C_s,C1)=0 for s=1,2,3",
                ],
            },
            "residual_dDelta_minus_Deltad": {
                "coefficient_over_lambda1_times_T": sp.sstr(residual_coefficient),
                "formula": "+2*i*lambda1*T^(AB)_(GDE)*(D_dot^D C1^G) D^(E dot)",
                "conditionally_nonzero": True,
            },
            "exact_color_witness": witness,
            "acceptance_use": False,
        },
        "residual_q": {
            "status": "NOT_RUN_AFTER_PHASE0_BLOCKER",
            "additional_missing_domain": "Delta(P_dot C_r,L) and Delta(L,P_dot C_r) for rows containing D_dot",
        },
        "target_blindness": {
            "memo_prediction_used": False,
            "holomorphic_twist_used": False,
            "literature_coefficient_used": False,
        },
    }


def build_summary(trace: dict[str, Any], trace_data: bytes) -> dict[str, Any]:
    return {
        "schema": "awi.step6.q0-q1-phase0-blocker-summary.v3",
        "generated": False,
        "checked_equations": trace["checked_equations"],
        "overall_status": trace["phase0_gate"]["status"],
        "scope": trace["scope"],
        "ledger_census": trace["ledger_census"],
        "phase0_gate": trace["phase0_gate"],
        "locked_input_boundary": trace["locked_input_boundary"],
        "locked_color_semantics": trace["locked_color_semantics"],
        "conditional_diagnostic": trace["conditional_diagnostic"],
        "residual_q": trace["residual_q"],
        "target_blindness": trace["target_blindness"],
        "sources": trace["sources"],
        "hashes": {
            "checker_sha256": sha256_bytes(Path(__file__).read_bytes()),
            "generated_trace_sha256": sha256_bytes(trace_data),
            "sealed_step5_ledger_sha256": trace["sources"]["sealed_rows_sha256"],
        },
        "generated_trace": {
            "path": str(TRACE_PATH.relative_to(ROOT)),
            "schema": trace["schema"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--require-pass", action="store_true")
    args = parser.parse_args()

    try:
        trace = build_trace()
        trace_data = canonical_bytes(trace)
        summary = build_summary(trace, trace_data)
        audit_data = canonical_bytes(summary)
    except Exception as exc:
        print(f"Phase-0 checker error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    if args.write:
        TRACE_PATH.parent.mkdir(parents=True, exist_ok=True)
        TRACE_PATH.write_bytes(trace_data)
        AUDIT_PATH.write_bytes(audit_data)
    else:
        if not TRACE_PATH.is_file() or TRACE_PATH.read_bytes() != trace_data:
            print(f"Phase-0: stale or missing {TRACE_PATH.relative_to(ROOT)}", file=sys.stderr)
            return 1
        if not AUDIT_PATH.is_file() or AUDIT_PATH.read_bytes() != audit_data:
            print(f"Phase-0: stale or missing {AUDIT_PATH.relative_to(ROOT)}", file=sys.stderr)
            return 1

    gate = trace["phase0_gate"]
    print(
        f"{gate['status']}: contract_grade_evaluated={gate['contract_grade_evaluated_rows']} "
        f"passed={gate['contract_grade_passed_rows']} blocked={gate['contract_grade_blocked_rows']} "
        f"conditional_A__C1_color_witness={trace['conditional_diagnostic']['exact_color_witness']['value']}"
    )
    return 1 if args.require_pass else 0


if __name__ == "__main__":
    raise SystemExit(main())
