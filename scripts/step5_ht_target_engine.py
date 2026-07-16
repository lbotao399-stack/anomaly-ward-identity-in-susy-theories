#!/usr/bin/env python3
"""Generate the admitted holomorphic-twist N=4 one-loop target in source notation.

This module is deliberately independent of the Project-side loop calculation.  It
encodes only the EXTERNAL_TARGET_ONLY statements admitted by tasks/CURRENT.yaml,
keeps both source normalization conflicts unresolved, and uses exact rational
arithmetic throughout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "generated/step5"
SOURCE_PATH = "references/vendor/arxiv/2512.07771v2/source/main.tex"
SOURCE_SHA256 = "90352c555f69eac3a99b9742c59e63afc785df333399a0730f8ac1ae094d9899"


def fraction_payload(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}",
    }


def canonical_json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode(
        "utf-8"
    )


def write_json(path: Path, payload: Any) -> str:
    data = canonical_json_bytes(payload)
    path.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def popcount(value: int) -> int:
    return value.bit_count()


def exterior_product(left: int, right: int) -> tuple[int, int] | None:
    """Return (canonical mask, sign) for two ordered exterior monomials."""
    if left & right:
        return None
    inversions = 0
    cursor = left
    while cursor:
        lowest = cursor & -cursor
        index = lowest.bit_length() - 1
        inversions += popcount(right & ((1 << index) - 1))
        cursor ^= lowest
    return left | right, -1 if inversions % 2 else 1


def epsilon3(i: int, j: int, k: int) -> int:
    if len({i, j, k}) < 3:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


def t_mn_terms(m: int, n: int) -> list[dict[str, Any]]:
    """Exact terms of the source kernel T_{m,n}, valid for arbitrary m,n >= 0."""
    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")
    rows: list[dict[str, Any]] = []
    for k in range(m + 1):
        for ell in range(n + 1):
            coefficient = Fraction(comb(m, k) * comb(n, ell), (m + n + 2) * (k + ell + 1))
            rows.append(
                {
                    "k": k,
                    "ell": ell,
                    "coefficient": fraction_payload(coefficient),
                    "left_output_derivative": [k, ell],
                    "right_output_derivative": [m - k, n - ell],
                }
            )
    return rows


@dataclass(frozen=True)
class Letter:
    id: str
    family: str
    source_field: str
    parity: int
    component: str | int | None
    inherent_derivative: tuple[int, int]
    project_expression: str
    dictionary_scale: str

    def payload(self, ordinal: int) -> dict[str, Any]:
        return {
            "ordinal": ordinal,
            "id": self.id,
            "family": self.family,
            "source_field": self.source_field,
            "parity": self.parity,
            "component": self.component,
            "inherent_source_derivative": list(self.inherent_derivative),
            "project_expression": self.project_expression,
            "dictionary_scale_symbol": self.dictionary_scale,
        }


LETTERS = (
    Letter("B", "B", "b", 0, None, (0, 0), "nabla_+ W_+", "s_b"),
    Letter("P1", "P", "beta", 1, 1, (0, 0), "nabla_+ Phi_1", "s_beta"),
    Letter("P2", "P", "beta", 1, 2, (0, 0), "nabla_+ Phi_2", "s_beta"),
    Letter("P3", "P", "beta", 1, 3, (0, 0), "nabla_+ Phi_3", "s_beta"),
    Letter("G1", "G", "gamma", 0, 1, (0, 0), "tilde_Phi_1", "s_gamma"),
    Letter("G2", "G", "gamma", 0, 2, (0, 0), "tilde_Phi_2", "s_gamma"),
    Letter("G3", "G", "gamma", 0, 3, (0, 0), "tilde_Phi_3", "s_gamma"),
    Letter("Hdot1", "H", "c", 1, "dot1", (1, 0), "tilde_W_dot1", "s_c"),
    Letter("Hdot2", "H", "c", 1, "dot2", (0, 1), "tilde_W_dot2", "s_c"),
)


RULES: dict[tuple[str, str], dict[str, Any]] = {
    ("b", "c"): {"id": "HT-RULE-BC", "classification": "NONZERO"},
    ("b", "b"): {"id": "HT-RULE-BB", "classification": "NONZERO"},
    ("beta", "gamma"): {"id": "HT-RULE-BETA-GAMMA", "classification": "NONZERO"},
    ("beta", "beta"): {"id": "HT-RULE-BETA-BETA", "classification": "NONZERO"},
    ("b", "gamma"): {"id": "HT-RULE-B-GAMMA", "classification": "NONZERO"},
    ("beta", "b"): {"id": "HT-RULE-BETA-B", "classification": "NONZERO"},
    ("c", "c"): {"id": "HT-ZERO-CC", "classification": "ZERO"},
    ("gamma", "gamma"): {"id": "HT-ZERO-GAMMA-GAMMA", "classification": "ZERO"},
    ("gamma", "c"): {"id": "HT-ZERO-GAMMA-C", "classification": "ZERO"},
    ("beta", "c"): {"id": "HT-ZERO-BETA-C", "classification": "ZERO"},
}


def output_term(coefficient: int, left: str, right: str) -> dict[str, Any]:
    return {
        "coefficient": coefficient,
        "left_output": left,
        "right_output": right,
        "kernel": "T_mn",
    }


def instantiate_rule_terms(
    rule_id: str, left_component: str | int | None, right_component: str | int | None
) -> list[dict[str, Any]]:
    if rule_id == "HT-RULE-BC":
        return [output_term(1, "c", "c")]
    if rule_id == "HT-RULE-BB":
        rows = [
            output_term(1, "c", "b"),
            output_term(-1, "b", "c"),
        ]
        for flavor in range(1, 4):
            rows.append(output_term(1, f"beta_{flavor}", f"gamma_{flavor}"))
            rows.append(output_term(-1, f"gamma_{flavor}", f"beta_{flavor}"))
        return rows
    if rule_id == "HT-RULE-BETA-GAMMA":
        if left_component != right_component:
            return []
        return [output_term(1, "c", "c")]
    if rule_id == "HT-RULE-BETA-BETA":
        assert isinstance(left_component, int) and isinstance(right_component, int)
        rows: list[dict[str, Any]] = []
        for flavor in range(1, 4):
            sign = epsilon3(left_component, right_component, flavor)
            if sign:
                rows.append(output_term(sign, "c", f"gamma_{flavor}"))
                rows.append(output_term(-sign, f"gamma_{flavor}", "c"))
        return rows
    if rule_id == "HT-RULE-B-GAMMA":
        assert isinstance(right_component, int)
        return [
            output_term(1, "c", f"gamma_{right_component}"),
            output_term(-1, f"gamma_{right_component}", "c"),
        ]
    if rule_id == "HT-RULE-BETA-B":
        assert isinstance(left_component, int)
        rows = [
            output_term(1, f"beta_{left_component}", "c"),
            output_term(1, "c", f"beta_{left_component}"),
        ]
        for first in range(1, 4):
            for second in range(1, 4):
                sign = epsilon3(left_component, first, second)
                if sign:
                    rows.append(output_term(sign, f"gamma_{first}", f"gamma_{second}"))
        return rows
    if rule_id.startswith("HT-ZERO-"):
        return []
    raise KeyError(rule_id)


def canonicalize_pair(left: Letter, right: Letter) -> dict[str, Any]:
    direct_key = (left.source_field, right.source_field)
    if direct_key in RULES:
        rule = RULES[direct_key]
        canonical_left = left
        canonical_right = right
        reversed_pair = False
        koszul_sign = 1
        color_order = ["A", "B"]
    else:
        reverse_key = (right.source_field, left.source_field)
        if reverse_key not in RULES:
            raise AssertionError(f"missing canonical rule for {left.id},{right.id}")
        rule = RULES[reverse_key]
        canonical_left = right
        canonical_right = left
        reversed_pair = True
        koszul_sign = -1 if left.parity * right.parity % 2 else 1
        color_order = ["B", "A"]

    terms = instantiate_rule_terms(
        rule["id"], canonical_left.component, canonical_right.component
    )
    for term in terms:
        term["coefficient"] *= koszul_sign

    exact_zero = not terms
    if rule["classification"] == "ZERO":
        zero_reason = "SOURCE_ZERO_RULE"
    elif exact_zero:
        zero_reason = "FLAVOR_TENSOR_ZERO"
    else:
        zero_reason = None

    return {
        "rule_id": rule["id"],
        "rule_classification": rule["classification"],
        "reversed_to_canonical": reversed_pair,
        "koszul_sign": koszul_sign,
        "canonical_source_fields": [canonical_left.source_field, canonical_right.source_field],
        "canonical_source_components": [canonical_left.component, canonical_right.component],
        "canonical_input_derivatives": [
            list(canonical_left.inherent_derivative),
            list(canonical_right.inherent_derivative),
        ],
        "canonical_color_order": color_order,
        "color_tensor": f"f_{{{color_order[0]} C D}} f_{{{color_order[1]} C E}}",
        "overall_source_coefficient": "kappa_H^2",
        "output_terms": terms,
        "exact_zero": exact_zero,
        "zero_reason": zero_reason,
        "source_branch": "DERIVATIVE_TOWER_BRANCH",
    }


def build_alphabet() -> dict[str, Any]:
    return {
        "schema": 1,
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "source": {
            "path": SOURCE_PATH,
            "sha256": SOURCE_SHA256,
            "anchors": [
                "HT-TWISTED-ACTION-FIELDS",
                "HT-N4-SETUP-SUPERFIELD",
                "HT-N4-DERIVATIVE-COMPONENT-PAIR-RESULTS",
            ],
        },
        "family_sizes": {"B": 1, "P": 3, "G": 3, "H": 2},
        "letter_count": len(LETTERS),
        "ordered_pair_count": len(LETTERS) ** 2,
        "letters": [letter.payload(index) for index, letter in enumerate(LETTERS)],
        "parity_identity": {
            "B": "|nabla_+|+|W_+|=1+1=0 mod 2",
            "P": "|nabla_+|+|Phi_r|=1+0=1 mod 2",
            "G": "|tilde_Phi_r|=0",
            "H": "|tilde_W_dot_a|=1",
        },
    }


def build_rule_catalog() -> list[dict[str, Any]]:
    anchors = {
        "HT-RULE-BC": [1041, 1042, 1227, 1228, 1367, 1369],
        "HT-RULE-BB": [1044, 1046, 1230, 1232, 1371, 1374],
        "HT-RULE-BETA-GAMMA": [1048, 1049, 1234, 1235, 1377, 1379],
        "HT-RULE-BETA-BETA": [1068, 1069, 1236, 1237, 1382, 1384],
        "HT-RULE-B-GAMMA": [1055, 1056, 1238, 1239, 1387, 1388],
        "HT-RULE-BETA-B": [1070, 1072, 1241, 1243, 1390, 1393],
        "HT-ZERO-CC": [729, 731],
        "HT-ZERO-GAMMA-GAMMA": [729, 731],
        "HT-ZERO-GAMMA-C": [729, 731],
        "HT-ZERO-BETA-C": [729, 731],
    }
    rows = []
    for (left, right), rule in RULES.items():
        rows.append(
            {
                "id": rule["id"],
                "classification": rule["classification"],
                "canonical_source_fields": [left, right],
                "source_path": SOURCE_PATH,
                "source_line_span_union": anchors[rule["id"]],
            }
        )
    return rows


def build_pairs() -> dict[str, Any]:
    pairs: list[dict[str, Any]] = []
    for left_index, left in enumerate(LETTERS):
        for right_index, right in enumerate(LETTERS):
            resolution = canonicalize_pair(left, right)
            pairs.append(
                {
                    "ordinal": left_index * len(LETTERS) + right_index,
                    "id": f"{left.id}__{right.id}",
                    "left": left.id,
                    "right": right.id,
                    "input_parities": [left.parity, right.parity],
                    "input_source_fields": [left.source_field, right.source_field],
                    "input_source_components": [left.component, right.component],
                    "input_inherent_derivatives": [
                        list(left.inherent_derivative),
                        list(right.inherent_derivative),
                    ],
                    **resolution,
                }
            )

    reversed_count = sum(bool(pair["reversed_to_canonical"]) for pair in pairs)
    exact_zero_count = sum(bool(pair["exact_zero"]) for pair in pairs)
    return {
        "schema": 1,
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "rule_catalog": build_rule_catalog(),
        "family_order": ["B", "P", "G", "H"],
        "ordered_family_component_counts": [
            [1, 3, 3, 2],
            [3, 9, 9, 6],
            [3, 9, 9, 6],
            [2, 6, 6, 4],
        ],
        "pair_count": len(pairs),
        "direct_canonical_count": len(pairs) - reversed_count,
        "reversed_canonical_count": reversed_count,
        "exact_zero_count": exact_zero_count,
        "exact_nonzero_count": len(pairs) - exact_zero_count,
        "reversal_contract": {
            "formula": "Q1(X^A Y^B)=(-1)^(|X||Y|) Q1(Y^B X^A)",
            "color_rule": "A,B are swapped before the canonical source rule is instantiated",
            "forbidden_reduction": "f_{B C D} f_{A C E} must not be replaced by f_{A C D} f_{B C E} without a separate proof",
        },
        "pairs": pairs,
    }


def build_derivative_kernel(max_audit_index: int) -> dict[str, Any]:
    samples = []
    for m in range(max_audit_index + 1):
        for n in range(max_audit_index + 1):
            samples.append(
                {
                    "m": m,
                    "n": n,
                    "term_count": (m + 1) * (n + 1),
                    "terms": t_mn_terms(m, n),
                }
            )
    return {
        "schema": 1,
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "source": {
            "path": SOURCE_PATH,
            "anchor": "HT-N4-DERIVATIVE-COMPONENT-PAIR-RESULTS",
            "lines": [1339, 1395],
            "equation_labels": ["eq:rec", "eq:Cmn"],
        },
        "kernel": {
            "id": "T_mn",
            "domain": "m,n,k,ell are nonnegative integers with 0<=k<=m and 0<=ell<=n",
            "coefficient": "binom(m,k) binom(n,ell) / ((m+n+2)(k+ell+1))",
            "left_factor": "partial_1^k partial_2^ell partial_dot_alpha f",
            "right_factor": "partial_1^(m-k) partial_2^(n-ell) partial^dot_alpha g",
        },
        "first_input_lift": {
            "formula": "Q1((partial^u f)(partial^v g))=sum_{r<=u} (-1)^|r| binom(u,r) partial^(u-r) Q1(f partial^(v+r) g)",
            "multiindex_binomial": "binom(u,r)=binom(u1,r1)binom(u2,r2)",
            "validity": "all u,v in N^2",
        },
        "zero_shift": {
            "T_0_0_coefficient": fraction_payload(Fraction(1, 2)),
            "formula": "T_0_0(f,g)=(1/2) partial_dot_alpha f partial^dot_alpha g",
        },
        "audit_rectangle": {
            "max_m": max_audit_index,
            "max_n": max_audit_index,
            "sample_count": len(samples),
            "samples": samples,
        },
    }


@dataclass(frozen=True)
class CComponent:
    id: str
    theta_mask: int
    theta_coefficient: int
    parity: int


C_COMPONENTS = (
    CComponent("c", 0b000, 1, 1),
    CComponent("gamma_1", 0b001, 1, 0),
    CComponent("gamma_2", 0b010, 1, 0),
    CComponent("gamma_3", 0b100, 1, 0),
    CComponent("beta_1", 0b110, 1, 1),
    CComponent("beta_2", 0b101, -1, 1),
    CComponent("beta_3", 0b011, 1, 1),
    CComponent("b", 0b111, 1, 0),
)


def delta_theta_polynomial() -> dict[int, Fraction]:
    polynomial = {0: Fraction(1)}
    for index in range(3):
        factor = {1 << index: Fraction(1), 1 << (index + 3): Fraction(-1)}
        updated: dict[int, Fraction] = {}
        for left_mask, left_value in polynomial.items():
            for right_mask, right_value in factor.items():
                product = exterior_product(left_mask, right_mask)
                if product is None:
                    continue
                mask, sign = product
                updated[mask] = updated.get(mask, Fraction(0)) + left_value * right_value * sign
        polynomial = {mask: value for mask, value in updated.items() if value}
    return polynomial


def c_product_term(first: CComponent, second: CComponent) -> tuple[int, Fraction]:
    first_mask = first.theta_mask
    second_mask = second.theta_mask << 3
    product = exterior_product(first_mask, second_mask)
    assert product is not None
    mask, exterior_sign = product
    field_theta_sign = -1 if first.parity * popcount(second.theta_mask) % 2 else 1
    coefficient = Fraction(
        first.theta_coefficient * second.theta_coefficient * exterior_sign * field_theta_sign
    )
    return mask, coefficient


def c_component_source_data(component_id: str) -> tuple[str, int | None]:
    if component_id in {"b", "c"}:
        return component_id, None
    family, raw_component = component_id.split("_", 1)
    if family not in {"beta", "gamma"}:
        raise ValueError(component_id)
    return family, int(raw_component)


def compact_normalized_actions() -> list[dict[str, Any]]:
    prefix = delta_theta_polynomial()
    rhs_by_mask: dict[int, dict[tuple[str, str], Fraction]] = {}
    for first in C_COMPONENTS:
        for second in C_COMPONENTS:
            component_mask, component_coefficient = c_product_term(first, second)
            for prefix_mask, prefix_coefficient in prefix.items():
                product = exterior_product(prefix_mask, component_mask)
                if product is None:
                    continue
                final_mask, exterior_sign = product
                # The compact source formula has an overall minus sign.
                coefficient = -prefix_coefficient * component_coefficient * exterior_sign
                key = (first.id, second.id)
                bucket = rhs_by_mask.setdefault(final_mask, {})
                bucket[key] = bucket.get(key, Fraction(0)) + coefficient

    rows: list[dict[str, Any]] = []
    for first in C_COMPONENTS:
        for second in C_COMPONENTS:
            input_mask, lhs_product_coefficient = c_product_term(first, second)
            # Q1 is odd.  After all six bookkeeping theta variables have been
            # moved to the left, extracting Q1 of the component pair contributes
            # (-1)^(total theta degree).
            q1_theta_sign = -1 if popcount(input_mask) % 2 else 1
            lhs_coefficient = lhs_product_coefficient * q1_theta_sign
            outputs = []
            actual_terms: list[tuple[Fraction, str, str]] = []
            for (left_output, right_output), value in sorted(
                rhs_by_mask.get(input_mask, {}).items()
            ):
                normalized = value / lhs_coefficient
                if normalized:
                    actual_terms.append((normalized, left_output, right_output))
                    outputs.append(
                        {
                            "coefficient": fraction_payload(normalized),
                            "left_output": left_output,
                            "right_output": right_output,
                            "bilinear": "partial_dot_alpha(left_D) partial^dot_alpha(right_E)",
                        }
                    )
            first_family, first_component = c_component_source_data(first.id)
            second_family, second_component = c_component_source_data(second.id)
            direct_rule = RULES.get((first_family, second_family))
            if direct_rule is None:
                canonical_rule_audit = {
                    "status": "NOT_APPLICABLE_REVERSED_COLOR_ORDER_RETAINED",
                    "detail": "The ordered-pair target engine performs the Koszul and A<->B color swap without reducing the color tensor.",
                }
            else:
                expected_rows = instantiate_rule_terms(
                    direct_rule["id"], first_component, second_component
                )
                expected_terms = sorted(
                    (Fraction(row["coefficient"]), row["left_output"], row["right_output"])
                    for row in expected_rows
                )
                canonical_rule_audit = {
                    "status": "PASS" if sorted(actual_terms) == expected_terms else "FAIL",
                    "rule_id": direct_rule["id"],
                    "expected_term_count": len(expected_terms),
                    "actual_term_count": len(actual_terms),
                }
            rows.append(
                {
                    "id": f"{first.id}__{second.id}",
                    "left_input": first.id,
                    "right_input": second.id,
                    "theta_mask": f"{input_mask:06b}",
                    "lhs_product_theta_coefficient": fraction_payload(lhs_product_coefficient),
                    "q1_theta_extraction_sign": q1_theta_sign,
                    "lhs_theta_coefficient": fraction_payload(lhs_coefficient),
                    "normalized_compact_outputs": outputs,
                    "exact_zero": not outputs,
                    "canonical_rule_audit": canonical_rule_audit,
                }
            )
    return rows


def build_compact_audit() -> dict[str, Any]:
    actions = compact_normalized_actions()
    nonzero_count = sum(not row["exact_zero"] for row in actions)
    canonical_audits = [
        row["canonical_rule_audit"]
        for row in actions
        if row["canonical_rule_audit"]["status"] != "NOT_APPLICABLE_REVERSED_COLOR_ORDER_RETAINED"
    ]
    prefix = delta_theta_polynomial()
    return {
        "schema": 1,
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "source": {
            "path": SOURCE_PATH,
            "superfield_anchor": "HT-N4-SETUP-SUPERFIELD",
            "compact_anchors": ["HT-INTRO-N4-COMPACT-Q1", "HT-N4-COMPACT-SUPERFIELD-RESULT"],
        },
        "grassmann_order": ["theta_1", "theta_2", "theta_3", "theta_prime_1", "theta_prime_2", "theta_prime_3"],
        "sign_conventions": [
            "All theta monomials are canonicalized to the displayed grassmann_order.",
            "Moving the first component field through the primed theta monomial contributes its Koszul sign.",
            "Extracting the odd Q1 through the complete theta monomial contributes (-1)^(total theta degree).",
        ],
        "epsilon_orientation_for_expansion": "epsilon^123=+1",
        "superfield_components": [
            {
                "id": component.id,
                "theta_mask_unprimed": f"{component.theta_mask:03b}",
                "theta_coefficient": component.theta_coefficient,
                "parity": component.parity,
            }
            for component in C_COMPONENTS
        ],
        "delta_theta_product": [
            {"theta_mask": f"{mask:06b}", "coefficient": fraction_payload(value)}
            for mask, value in sorted(prefix.items())
        ],
        "normalized_formula": "-prod_I(theta_I-theta_prime_I) partial C^D(theta) partial C^E(theta_prime)",
        "branches": [
            {
                "id": "COMPACT_INTRO_BRANCH",
                "overall_coefficient": "1/4",
                "source_lines": [200, 206],
                "equation_label": "eq:Q1C",
            },
            {
                "id": "COMPACT_MAIN_BRANCH",
                "overall_coefficient": "kappa_H^2",
                "source_lines": [1248, 1252],
                "equation_label": "eq:Q1N4",
            },
        ],
        "component_pair_count": len(actions),
        "exact_nonzero_count": nonzero_count,
        "exact_zero_count": len(actions) - nonzero_count,
        "canonical_rule_audit_count": len(canonical_audits),
        "canonical_rule_audit_passed": sum(row["status"] == "PASS" for row in canonical_audits),
        "canonical_rule_audit_failed": sum(row["status"] == "FAIL" for row in canonical_audits),
        "component_actions": actions,
        "audit_statement": "Both compact branches have the identical normalized 64-component Grassmann expansion; only their unresolved overall coefficients differ.",
    }


def build_conflicts() -> dict[str, Any]:
    return {
        "schema": 1,
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "resolution_status": "UNRESOLVED_PROJECT_DERIVATION_REQUIRED",
        "conflicts": [
            {
                "id": "HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT",
                "status": "UNRESOLVED_IN_SOURCE",
                "branches": [
                    {"id": "COMPACT_INTRO_BRANCH", "coefficient": "-1/4"},
                    {"id": "COMPACT_MAIN_BRANCH", "coefficient": "-kappa_H^2"},
                ],
                "algebraic_compatibility_condition": "kappa_H^2=1/4",
                "source_anchors": ["HT-INTRO-N4-COMPACT-Q1", "HT-N4-COMPACT-SUPERFIELD-RESULT", "HT-LIE-NORMALIZATION"],
                "project_selection": None,
            },
            {
                "id": "HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO",
                "status": "UNRESOLVED_IN_SOURCE",
                "branches": [
                    {"id": "PRINTED_ZERO_COMPONENT_BRANCH", "bilinear_coefficient": "kappa_H^2"},
                    {"id": "SHIFTED_DTRI_ZERO_BRANCH", "bilinear_coefficient": "kappa_H^2/2"},
                    {"id": "DERIVATIVE_TOWER_M0_N0_BRANCH", "bilinear_coefficient": "kappa_H^2/2"},
                ],
                "algebraic_discrepancy": "kappa_H^2-kappa_H^2/2=kappa_H^2/2",
                "source_anchors": ["HT-PAIR-RULE-AND-DTRI-KERNEL", "HT-N4-COMPONENT-PAIR-RESULTS", "HT-N4-DERIVATIVE-COMPONENT-PAIR-RESULTS"],
                "project_selection": None,
            },
        ],
    }


def build_dictionary() -> dict[str, Any]:
    rows = [
        {
            "source": "b^A",
            "project": "B^P=(nabla_+ W_+)^P",
            "forward": "iota(b^A)=s_b R_A^P B^P",
            "inverse": "iota^-1(B^P)=s_b^-1 (R^-1)_P^A b^A",
            "scale_symbol": "s_b",
            "scale_constraint": "s_b!=0",
        },
        {
            "source": "beta_I^A",
            "project": "P_r^P=(nabla_+ Phi_r)^P",
            "forward": "iota(beta_I^A)=s_beta R_A^P U_I^r P_r^P",
            "inverse": "iota^-1(P_r^P)=s_beta^-1 (R^-1)_P^A (U^-1)_r^I beta_I^A",
            "scale_symbol": "s_beta",
            "scale_constraint": "s_beta!=0",
        },
        {
            "source": "gamma^{I A}",
            "project": "G_r^P=tilde_Phi_r^P",
            "forward": "iota(gamma^{I A})=s_gamma R_A^P (U^-1)_r^I G_r^P",
            "inverse": "iota^-1(G_r^P)=s_gamma^-1 (R^-1)_P^A U_I^r gamma^{I A}",
            "scale_symbol": "s_gamma",
            "scale_constraint": "s_gamma!=0",
        },
        {
            "source": "partial_dot_a c^A",
            "project": "H_dot_b^P=tilde_W_dot_b^P",
            "forward": "iota(partial_dot_a c^A)=s_c R_A^P S_dot_a^dot_b H_dot_b^P",
            "inverse": "iota^-1(H_dot_b^P)=s_c^-1 (R^-1)_P^A (S^-1)_dot_b^dot_a partial_dot_a c^A",
            "scale_symbol": "s_c",
            "scale_constraint": "s_c!=0",
        },
    ]
    return {
        "schema": 1,
        "status": "CONDITIONAL_PLACEHOLDER_NOT_A_PROJECT_FORMULA",
        "maps": rows,
        "invertibility_assumptions": [
            "s_b!=0",
            "s_beta!=0",
            "s_gamma!=0",
            "s_c!=0",
            "s_Q!=0",
            "tau!=0",
            "R in GL(dim(g))",
            "U in GL(3)",
            "S in GL(2)",
        ],
        "operator_normalization": {
            "formula": "iota o Q1_HT o iota^-1=s_Q Q1_Project",
            "scale_symbol": "s_Q",
            "scale_constraint": "s_Q!=0",
            "status": "UNRESOLVED_PROJECT_DERIVATION_REQUIRED",
        },
        "round_trip_audits": [
            {
                "source": row["source"],
                "forward_then_inverse": "IDENTITY_UNDER_DECLARED_INVERTIBILITY_ASSUMPTIONS",
                "project": row["project"],
                "inverse_then_forward": "IDENTITY_UNDER_DECLARED_INVERTIBILITY_ASSUMPTIONS",
            }
            for row in rows
        ],
        "color_basis_contract": {
            "formula": "f_AB^C R_C^R=i R_A^P R_B^Q c_PQ^R",
            "trace_formula": "kappa_H delta_AB=tau R_A^P R_B^Q kappa_Project_PQ",
            "nonzero_symbols": ["tau"],
            "forbidden_shortcut": "f_ABC=c_ABC",
        },
        "unresolved_typed_gates": [
            {
                "id": "CONDITIONAL_SU4_HODGE_MAP",
                "detail": "The source gamma-to-Phi^{4r} convention must be translated to the Project tilde_Phi_r convention by an explicit Hodge/index map.",
            },
            {
                "id": "CONDITIONAL_PLUS_MINUS_SPIN_FRAME",
                "detail": "The exact coefficient between b and nabla_+ W_+ is not fixed before the Step-5 plus/minus spin-frame ledger.",
            },
            {
                "id": "CONDITIONAL_HOLOMORPHIC_DERIVATIVE_MAP",
                "detail": "The commuting source partial_1,partial_2 tower is not identified with ordered Project gauge-covariant derivatives before a Project derivation.",
            },
            {
                "id": "CONDITIONAL_LOOP_NORMALIZATION",
                "detail": "The admitted source anchors contain no explicit g_YM normalization to identify with the Project absorbed-coupling convention.",
            },
        ],
    }


def perform_checks(
    alphabet: dict[str, Any],
    pairs: dict[str, Any],
    derivative: dict[str, Any],
    compact: dict[str, Any],
    conflicts: dict[str, Any],
    dictionary: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        checks.append(
            {
                "id": check_id,
                "status": "PASS" if condition else "FAIL",
                "detail": detail,
            }
        )

    pair_rows = pairs["pairs"]
    rule_rows = pairs["rule_catalog"]
    check("alphabet.count", alphabet["letter_count"] == 9, str(alphabet["letter_count"]))
    check(
        "source.sha256",
        hashlib.sha256((ROOT / SOURCE_PATH).read_bytes()).hexdigest() == SOURCE_SHA256,
        SOURCE_SHA256,
    )
    check("alphabet.unique_ids", len({row["id"] for row in alphabet["letters"]}) == 9, "nine unique ids")
    check("pairs.count", len(pair_rows) == 81, str(len(pair_rows)))
    check("pairs.unique_ids", len({row["id"] for row in pair_rows}) == 81, "eighty-one unique ids")
    check("pairs.ordinals", [row["ordinal"] for row in pair_rows] == list(range(81)), "ordinals 0..80")
    check("rules.nonzero_count", sum(row["classification"] == "NONZERO" for row in rule_rows) == 6, "six")
    check("rules.zero_count", sum(row["classification"] == "ZERO" for row in rule_rows) == 4, "four")
    check("pairs.direct_count", pairs["direct_canonical_count"] == 52, str(pairs["direct_canonical_count"]))
    check("pairs.reversed_count", pairs["reversed_canonical_count"] == 29, str(pairs["reversed_canonical_count"]))
    check("pairs.zero_count", pairs["exact_zero_count"] == 52, str(pairs["exact_zero_count"]))
    check("pairs.nonzero_count", pairs["exact_nonzero_count"] == 29, str(pairs["exact_nonzero_count"]))
    check(
        "pairs.reversed_color_order",
        all(
            row["canonical_color_order"] == (["B", "A"] if row["reversed_to_canonical"] else ["A", "B"])
            for row in pair_rows
        ),
        "color order follows canonical reversal",
    )
    check(
        "derivative.T00",
        derivative["zero_shift"]["T_0_0_coefficient"] == fraction_payload(Fraction(1, 2)),
        "1/2",
    )
    check(
        "derivative.exact_coefficients",
        all(
            row["coefficient"]["denominator"] > 0
            for sample in derivative["audit_rectangle"]["samples"]
            for row in sample["terms"]
        ),
        "all denominators positive",
    )
    check("compact.component_count", compact["component_pair_count"] == 64, str(compact["component_pair_count"]))
    check("compact.branch_count", len(compact["branches"]) == 2, str(len(compact["branches"])))
    check("compact.delta_term_count", len(compact["delta_theta_product"]) == 8, str(len(compact["delta_theta_product"])))
    check("compact.canonical_audit_count", compact["canonical_rule_audit_count"] == 42, str(compact["canonical_rule_audit_count"]))
    check("compact.canonical_audit_passed", compact["canonical_rule_audit_passed"] == 42, str(compact["canonical_rule_audit_passed"]))
    check("compact.canonical_audit_failed", compact["canonical_rule_audit_failed"] == 0, str(compact["canonical_rule_audit_failed"]))
    check("conflicts.count", len(conflicts["conflicts"]) == 2, str(len(conflicts["conflicts"])))
    check(
        "conflicts.ids",
        {row["id"] for row in conflicts["conflicts"]}
        == {
            "HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT",
            "HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO",
        },
        "both named conflicts",
    )
    check("dictionary.map_count", len(dictionary["maps"]) == 4, str(len(dictionary["maps"])))
    check(
        "dictionary.nonzero_scales",
        {row["scale_constraint"] for row in dictionary["maps"]}
        == {"s_b!=0", "s_beta!=0", "s_gamma!=0", "s_c!=0"},
        "all four field scales explicitly nonzero",
    )
    return checks


def generate(output_dir: Path, max_derivative_audit: int) -> dict[str, Any]:
    if max_derivative_audit < 0:
        raise ValueError("max_derivative_audit must be nonnegative")
    output_dir.mkdir(parents=True, exist_ok=True)

    alphabet = build_alphabet()
    pairs = build_pairs()
    derivative = build_derivative_kernel(max_derivative_audit)
    compact = build_compact_audit()
    conflicts = build_conflicts()
    dictionary = build_dictionary()
    checks = perform_checks(alphabet, pairs, derivative, compact, conflicts, dictionary)
    failed = [row for row in checks if row["status"] != "PASS"]
    if failed:
        raise AssertionError(f"generation checks failed: {failed}")

    payloads = {
        "ht_typed_alphabet.json": alphabet,
        "ht_ordered_pair_targets.json": pairs,
        "ht_derivative_kernel.json": derivative,
        "ht_compact_grassmann_audit.json": compact,
        "ht_source_conflicts.json": conflicts,
        "ht_typed_dictionary.json": dictionary,
    }
    hashes = {
        filename: write_json(output_dir / filename, payload)
        for filename, payload in payloads.items()
    }
    summary = {
        "schema": 1,
        "generator": "scripts/step5_ht_target_engine.py",
        "authority_role": "EXTERNAL_TARGET_ONLY",
        "output_directory": str(output_dir.relative_to(ROOT)),
        "counts": {
            "letters": alphabet["letter_count"],
            "ordered_pairs": pairs["pair_count"],
            "exact_nonzero_pairs": pairs["exact_nonzero_count"],
            "exact_zero_pairs": pairs["exact_zero_count"],
            "canonical_nonzero_rules": 6,
            "canonical_zero_rules": 4,
            "compact_component_pairs": compact["component_pair_count"],
            "source_conflicts": len(conflicts["conflicts"]),
            "checks": len(checks),
            "checks_passed": len(checks),
            "checks_failed": 0,
        },
        "checks": checks,
        "artifact_sha256": hashes,
        "determinism_contract": "sorted JSON keys, UTF-8, two-space indentation, trailing newline, no timestamp",
    }
    summary_filename = "ht_generation_summary.json"
    summary_hash = write_json(output_dir / summary_filename, summary)
    return {
        "summary": summary,
        "summary_sha256": summary_hash,
        "artifacts": [*payloads, summary_filename],
    }


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory (default: generated/step5)",
    )
    parser.add_argument(
        "--max-derivative-audit",
        type=int,
        default=4,
        help="Largest m and n included in the exact-rational audit rectangle",
    )
    parser.add_argument(
        "--print-t",
        nargs=2,
        type=int,
        metavar=("M", "N"),
        help="Print exact T_{m,n} terms and exit without generating artifacts",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if args.print_t is not None:
        m, n = args.print_t
        print(canonical_json_bytes({"m": m, "n": n, "terms": t_mn_terms(m, n)}).decode(), end="")
        return 0
    result = generate(args.output_dir.resolve(), args.max_derivative_audit)
    counts = result["summary"]["counts"]
    print(
        "STEP5_HT_TARGET_ENGINE_OK "
        f"letters={counts['letters']} pairs={counts['ordered_pairs']} "
        f"nonzero={counts['exact_nonzero_pairs']} zero={counts['exact_zero_pairs']} "
        f"checks={counts['checks_passed']}/{counts['checks']} "
        f"summary_sha256={result['summary_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
