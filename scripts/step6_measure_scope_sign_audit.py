#!/usr/bin/env python3
"""Exact audit of the Step-6 coefficient-left derivative sign.

The active tensor compiler carries coefficient parity on every expanded leaf.
The local legacy engine below omits only that sign and is retained solely to
reproduce the assignment-dependent failure.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_global_dword_adapter as adapter
    from scripts import step6_global_supertensor as global_tensor
except ModuleNotFoundError:
    import step6_coefficient_tensor as coefficient
    import step6_global_dword_adapter as adapter
    import step6_global_supertensor as global_tensor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "generated/step6/measure-scope-sign/measure-scope-sign.json"
AUDIT = ROOT / "audits/step6-measure-scope-sign-verification.json"

SCHEMA = "step6.measure_scope_sign_audit.v1"
REJECTED_FIELD = "coefficient_order_measure_scope_sign"
REQUIRED_FIELD = "LabeledLeaf.coefficient_parity"


class LegacyMissingLeafSignEngine:
    """Forensic engine reproducing the removed hit-leaf-sign omission."""

    def __init__(self) -> None:
        self.operators: dict[Any, Mapping[str, Any]] = {}

    def primitive(self, terms: Sequence[Any], primitive: str) -> tuple[Any, ...]:
        emitted: list[Any] = []
        for term in terms:
            prefix_factor_parity = 0
            for position, factor in enumerate(term.factors):
                operators = self.operators.setdefault(
                    factor.momentum,
                    coefficient.oracle.flat_operators(factor.momentum),
                )
                differentiated = operators[primitive].apply(factor.value)
                if differentiated:
                    replacement = coefficient.oracle.LabeledLeaf(
                        factor.label,
                        factor.momentum,
                        factor.parity ^ 1,
                        differentiated,
                        (primitive,) + factor.derivative_word,
                        factor.coefficient_parity,
                    )
                    emitted.append(
                        coefficient.oracle.ProductTerm(
                            term.coefficient * (-1 if prefix_factor_parity else 1),
                            term.factors[:position]
                            + (replacement,)
                            + term.factors[position + 1 :],
                        )
                    )
                prefix_factor_parity ^= factor.parity
        return coefficient._canonical_product_terms(emitted)

    def __call__(
        self, terms: Sequence[Any], tokens: Sequence[str]
    ) -> tuple[Any, ...]:
        emitted: list[Any] = []
        for branch_coefficient, primitive_word in coefficient._explicit_word_expansion(
            tokens
        ):
            branch = coefficient.scale_terms(
                terms, coefficient.oracle.Poly.constant(branch_coefficient)
            )
            for primitive in reversed(primitive_word):
                branch = self.primitive(branch, primitive)
            emitted.extend(branch)
        return coefficient._canonical_product_terms(emitted)


def _program(vertex: str) -> tuple[Any, Mapping[str, Any], Mapping[str, Any]]:
    context = adapter.selected_context()
    option = context.selected[vertex]
    program = context.programs[str(option["local_amplitude_option_id"])]
    term = context.terms[str(program["term_id"])]
    return context, program, term


def _parities(program: Mapping[str, Any], masks: Sequence[int]) -> dict[str, int]:
    return {
        str(port): coefficient.coefficient_parity(int(mask))
        for port, mask in zip(program["port_order"], masks, strict=True)
    }


def _measure_token(measure: str) -> str:
    if measure == "E_MINUS_ANTICHIRAL":
        return "barD2"
    if measure == "E_PLUS_CHIRAL":
        return "D2"
    raise ValueError(measure)


def _distributed_constant(
    terms: Sequence[Any], parities: Mapping[str, int], measure: str, engine: Any
) -> Any:
    expanded = engine(terms, (_measure_token(measure),))
    exterior = coefficient.evaluate_product_terms(expanded, parities)
    return exterior.coefficient(0).divide_scalar(-4)


def compare_assignment(
    vertex: str, masks: Sequence[int]
) -> dict[str, Any]:
    _, program, term = _program(vertex)
    masks = tuple(int(mask) for mask in masks)
    parities = _parities(program, masks)
    leaves = coefficient._program_leaves(program, masks)

    legacy_engine = LegacyMissingLeafSignEngine()
    legacy_inner = coefficient._evaluate_ast_terms(
        term["expression_ast"], leaves, {}, legacy_engine
    )
    legacy_direct = coefficient.apply_measure(
        coefficient.evaluate_product_terms(legacy_inner, parities), term["measure"]
    )
    legacy_distributed = _distributed_constant(
        legacy_inner, parities, term["measure"], legacy_engine
    )

    active_engine = global_tensor.CachedDerivativeEngine()
    active_inner = coefficient._evaluate_ast_terms(
        term["expression_ast"], leaves, {}, active_engine
    )
    active_direct = coefficient.apply_measure(
        coefficient.evaluate_product_terms(active_inner, parities), term["measure"]
    )
    active_distributed = _distributed_constant(
        active_inner, parities, term["measure"], active_engine
    )

    return {
        "vertex": vertex,
        "term_id": term["term_id"],
        "basis_masks": list(masks),
        "coefficient_parities": [parities[port] for port in program["port_order"]],
        "coefficient_word_parity": sum(parities.values()) & 1,
        "legacy_relation": (
            "EQUAL"
            if legacy_distributed == legacy_direct
            else "MINUS"
            if legacy_distributed == -legacy_direct
            else "NEITHER"
        ),
        "legacy_direct": coefficient.serialize_evaluation(legacy_direct),
        "legacy_distributed": coefficient.serialize_evaluation(legacy_distributed),
        "active_direct": coefficient.serialize_evaluation(active_direct),
        "active_distributed": coefficient.serialize_evaluation(active_distributed),
        "active_scope_identity": active_direct == active_distributed,
    }


def single_leaf_checks() -> dict[str, Any]:
    oracle = coefficient.oracle
    zero = oracle.BispinorMomentum(
        "0", ((oracle.ZERO, oracle.ZERO), (oracle.ZERO, oracle.ZERO))
    )
    cases = 0
    nonzero = 0
    passed = True
    for mask in range(16):
        parity = coefficient.coefficient_parity(mask)
        label = "v"
        leaf = oracle.LabeledLeaf(
            label,
            zero,
            0,
            oracle.Exterior.basis(mask),
            coefficient_parity=parity,
        )
        terms = (oracle.ProductTerm(oracle.ONE, (leaf,)),)
        for primitive in oracle.PRIMITIVE_DERIVATIVES:
            cases += 1
            legacy = LegacyMissingLeafSignEngine().primitive(terms, primitive)
            active = global_tensor.CachedDerivativeEngine().primitive(terms, primitive)
            if legacy:
                nonzero += 1
                expected = coefficient.scale_terms(
                    legacy, oracle.Poly.constant(-1 if parity else 1)
                )
                passed &= active == expected
            else:
                passed &= not active
    return {
        "cases": cases,
        "nonzero_cases": nonzero,
        "identity": "d(v_s e_s)=(-1)^|s| v_s d(e_s)",
        "passed": bool(passed),
    }


def build_payload() -> dict[str, Any]:
    context = adapter.selected_context()
    frozen = {
        vertex: [
            adapter.local_basis_by_port(
                context.programs[
                    str(context.selected[vertex]["local_amplitude_option_id"])
                ]
            )[port]
            for port in context.programs[
                str(context.selected[vertex]["local_amplitude_option_id"])
            ]["port_order"]
        ]
        for vertex in ("A", "B", "C")
    }
    counterexamples = [
        compare_assignment("A", (0, 0, 0)),
        compare_assignment("A", (0, 1, 4)),
    ]
    frozen_rows = [compare_assignment(vertex, frozen[vertex]) for vertex in ("A", "B", "C")]
    single = single_leaf_checks()
    checks = {
        "single_leaf_left_rule": single["passed"],
        "legacy_sign_is_assignment_dependent": [
            row["legacy_relation"] for row in counterexamples
        ]
        == ["EQUAL", "MINUS"],
        "active_counterexamples_close": all(
            row["active_scope_identity"] for row in counterexamples
        ),
        "active_frozen_rows_close": all(
            row["active_scope_identity"] for row in frozen_rows
        ),
        "legacy_frozen_accidental_minus_reproduced": all(
            row["legacy_relation"] == "MINUS" for row in frozen_rows
        ),
        "frozen_words_are_even": all(
            row["coefficient_word_parity"] == 0 for row in frozen_rows
        ),
    }
    payload = {
        "schema": SCHEMA,
        "status": "PASS_BUG_FIXED_GLOBAL_SIGN_REJECTED",
        "source_equations": {
            "left_leibniz": "2A.5",
            "coefficient_left_expansion": "3D.14",
            "coefficient_parity": "3D.15",
            "measure_projector": "3A.13",
        },
        "derivation": {
            "leaf": "V_s=v_s*e_s, |v_s|=|e_s|=p_s",
            "primitive": "d(v_s*e_s)=(-1)^p_s*v_s*d(e_s)",
            "branch_missing_sign": "(-1)^(sum_r p_(j_r)) for derivative hits j_1,...,j_m",
            "even_measure_after_left": "(-1)^(2*|v_1...v_n|)=+1",
        },
        "rejected_global_sign_field": {
            "field_name": REJECTED_FIELD,
            "status": "REJECTED_NOT_A_CANDIDATE",
        },
        "required_minimal_field": REQUIRED_FIELD,
        "single_leaf": single,
        "counterexamples": counterexamples,
        "frozen_action_vertices": frozen_rows,
        "fixed_locations": [
            "scripts/step6_symbolic_grassmann_oracle.py:LabeledLeaf",
            "scripts/step6_symbolic_grassmann_oracle.py:apply_primitive_graded_leibniz",
            "scripts/step6_coefficient_tensor.py:_program_leaves",
            "scripts/step6_coefficient_tensor.py:_explicit_apply_primitive",
            "scripts/step6_global_supertensor.py:CachedDerivativeEngine.primitive",
            "scripts/step6_full_supertensor.py:generic_local_tensor",
            "scripts/step6_global_dword_adapter.py:ScopeOnlyDerivativeEngine.primitive",
        ],
        "checks": checks,
    }
    payload["passed"] = sum(checks.values())
    payload["failed"] = len(checks) - payload["passed"]
    return payload


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = {
        "schema": "step6.measure_scope_sign_audit.verification.v1",
        "status": "PASS" if payload["failed"] == 0 else "FAIL",
        "checks": payload["checks"],
        "passed": payload["passed"],
        "failed": payload["failed"],
    }
    if audit["status"] != "PASS":
        raise AssertionError(audit)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(json.dumps({"status": payload["status"], "audit": audit["status"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
