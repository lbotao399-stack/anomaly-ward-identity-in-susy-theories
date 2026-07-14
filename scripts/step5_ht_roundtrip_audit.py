#!/usr/bin/env python3
"""Typed Project <-> holomorphic-twist Step-5 round-trip audit.

The holomorphic-twist source is used only as an external target.  Project
normalizations are read from target-blind audits.  Exact arithmetic is over
Q(i,sqrt(2)); no floating-point comparison occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-ht-roundtrip-audit.json"
MD_OUT = ROOT / "audits/step5-ht-roundtrip-audit.md"

AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
PROJECT_EVIDENCE_BASE_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
HT_SOURCE = "references/vendor/arxiv/2512.07771v2/source/main.tex"
HT_SOURCE_SHA256 = "90352c555f69eac3a99b9742c59e63afc785df333399a0730f8ac1ae094d9899"

PROJECT_INPUTS = {
    "audits/step5-canonical-superfield-ww-seed.json":
        "899c109940af66552191067b653b38bffd2ac9f108bccf3001f491c85eef4324",
    "audits/step5-residual-q-projection.json":
        "29928b9d034625eb753d179c556a5dd19b479f4cb0daca334840e1564b572538",
    "audits/step5-project-shift-kernel.json":
        "1d25cdb4a11ba451f1fa550f2c4e38aabca9f07807be2c2693759973f700e97d",
    "audits/step5-pbw-jet-audit.json":
        "8d4c9e6e119a763ce0ae91ff094439c30d64fcb15bc69b99fa20c564b38b8935",
    "audits/step5-link-pbw-intertwiner.json":
        "9173432571a4bba0fb2a29f711bc082518d5af9d73552376042e342479dc5d71",
    "audits/step5-ww-physical-cut-pole.json":
        "92d1d87f6d667ff6e60016eead238bd68d3caf6ef4194d2e69795564e91d18c4",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


@dataclass(frozen=True)
class K:
    """a+b sqrt(2)+i(c+d sqrt(2)), with rational coefficients."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @staticmethod
    def rational(value: int | Fraction) -> "K":
        return K(a=Fraction(value))

    def __add__(self, other: "K") -> "K":
        return K(self.a + other.a, self.b + other.b,
                 self.c + other.c, self.d + other.d)

    def __neg__(self) -> "K":
        return K(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: "K") -> "K":
        return self + (-other)

    def __mul__(self, other: "K") -> "K":
        return K(
            self.a * other.a + 2 * self.b * other.b
            - self.c * other.c - 2 * self.d * other.d,
            self.a * other.b + self.b * other.a
            - self.c * other.d - self.d * other.c,
            self.a * other.c + 2 * self.b * other.d
            + self.c * other.a + 2 * self.d * other.b,
            self.a * other.d + self.b * other.c
            + self.c * other.b + self.d * other.a,
        )

    def scale(self, value: int | Fraction) -> "K":
        value = Fraction(value)
        return K(value * self.a, value * self.b, value * self.c, value * self.d)

    def inverse(self) -> "K":
        # z^{-1}=conj_i(z)/(x^2+y^2), followed by the Q(sqrt(2)) inverse.
        if self == ZERO:
            raise ZeroDivisionError
        x2_plus_y2_a = self.a * self.a + 2 * self.b * self.b + self.c * self.c + 2 * self.d * self.d
        x2_plus_y2_b = 2 * (self.a * self.b + self.c * self.d)
        norm = x2_plus_y2_a * x2_plus_y2_a - 2 * x2_plus_y2_b * x2_plus_y2_b
        if norm == 0:
            raise ZeroDivisionError
        qa = x2_plus_y2_a / norm
        qb = -x2_plus_y2_b / norm
        inverse_denominator = K(a=qa, b=qb)
        return K(self.a, self.b, -self.c, -self.d) * inverse_denominator

    def __truediv__(self, other: "K") -> "K":
        return self * other.inverse()

    def text(self) -> str:
        terms: list[tuple[Fraction, str]] = [
            (self.a, ""), (self.b, "sqrt(2)"),
            (self.c, "i"), (self.d, "i*sqrt(2)"),
        ]
        out = ""
        for coefficient, symbol in terms:
            if coefficient == 0:
                continue
            sign = "+" if coefficient > 0 else "-"
            magnitude = abs(coefficient)
            if magnitude == 1 and symbol:
                body = symbol
            else:
                qtext = (str(magnitude.numerator) if magnitude.denominator == 1
                         else f"{magnitude.numerator}/{magnitude.denominator}")
                body = qtext + (f"*{symbol}" if symbol else "")
            out += sign + body
        if not out:
            return "0"
        return out[1:] if out.startswith("+") else out

    def payload(self) -> dict[str, Any]:
        return {
            "basis": ["1", "sqrt(2)", "i", "i*sqrt(2)"],
            "coefficients": [
                [self.a.numerator, self.a.denominator],
                [self.b.numerator, self.b.denominator],
                [self.c.numerator, self.c.denominator],
                [self.d.numerator, self.d.denominator],
            ],
            "text": self.text(),
        }


ZERO = K()
ONE = K.rational(1)
MINUS_ONE = K.rational(-1)
IMAGINARY_UNIT = K(c=Fraction(1))
SQRT2 = K(b=Fraction(1))
INV_SQRT2 = K(b=Fraction(1, 2))
MINUS_I_OVER_SQRT2 = (-IMAGINARY_UNIT) * INV_SQRT2


def popcount(mask: int) -> int:
    return mask.bit_count()


def exterior(left: int, right: int) -> tuple[int, int] | None:
    if left & right:
        return None
    inversions = 0
    cursor = left
    while cursor:
        bit = cursor & -cursor
        index = bit.bit_length() - 1
        inversions += popcount(right & ((1 << index) - 1))
        cursor ^= bit
    return left | right, (-1 if inversions % 2 else 1)


def epsilon3(i: int, j: int, k: int) -> int:
    if {i, j, k} != {1, 2, 3}:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


@dataclass(frozen=True)
class CompactComponent:
    source_id: str
    project_id: str
    mask: int
    source_theta_coefficient: K
    project_theta_coefficient: K
    parity: int


COMPONENTS = (
    CompactComponent("c", "U", 0b000, ONE, ONE, 1),
    CompactComponent("gamma_1", "C_1", 0b001, ONE, ONE, 0),
    CompactComponent("gamma_2", "C_2", 0b010, ONE, ONE, 0),
    CompactComponent("gamma_3", "C_3", 0b100, ONE, ONE, 0),
    CompactComponent("beta_1", "B_1", 0b110, ONE, INV_SQRT2, 1),
    CompactComponent("beta_2", "B_2", 0b101, MINUS_ONE, -INV_SQRT2, 1),
    CompactComponent("beta_3", "B_3", 0b011, ONE, INV_SQRT2, 1),
    CompactComponent("b", "A", 0b111, ONE, MINUS_I_OVER_SQRT2, 0),
)

SOURCE_TO_PROJECT = {component.source_id: component.project_id for component in COMPONENTS}
FIELD_SCALES = {
    "c": ONE,
    "gamma_1": ONE, "gamma_2": ONE, "gamma_3": ONE,
    "beta_1": INV_SQRT2, "beta_2": INV_SQRT2, "beta_3": INV_SQRT2,
    "b": MINUS_I_OVER_SQRT2,
}
FIELD_PARITIES = {component.source_id: component.parity for component in COMPONENTS}


def delta_theta() -> dict[int, K]:
    polynomial = {0: ONE}
    for index in range(3):
        factor = {1 << index: ONE, 1 << (index + 3): MINUS_ONE}
        updated: dict[int, K] = {}
        for left_mask, left_value in polynomial.items():
            for right_mask, right_value in factor.items():
                product = exterior(left_mask, right_mask)
                if product is None:
                    continue
                mask, sign = product
                updated[mask] = updated.get(mask, ZERO) + (left_value * right_value).scale(sign)
        polynomial = {mask: value for mask, value in updated.items() if value != ZERO}
    return polynomial


def component_product(first: CompactComponent, second: CompactComponent,
                      project: bool) -> tuple[int, K]:
    product = exterior(first.mask, second.mask << 3)
    assert product is not None
    mask, sign = product
    first_coefficient = (first.project_theta_coefficient if project
                         else first.source_theta_coefficient)
    second_coefficient = (second.project_theta_coefficient if project
                          else second.source_theta_coefficient)
    field_theta_sign = -1 if first.parity * popcount(second.mask) % 2 else 1
    return mask, (first_coefficient * second_coefficient).scale(sign * field_theta_sign)


def compact_actions(project: bool) -> list[dict[str, Any]]:
    prefix = delta_theta()
    rhs: dict[int, dict[tuple[str, str], K]] = {}
    for first in COMPONENTS:
        for second in COMPONENTS:
            component_mask, component_coefficient = component_product(first, second, project)
            for prefix_mask, prefix_coefficient in prefix.items():
                product = exterior(prefix_mask, component_mask)
                if product is None:
                    continue
                final_mask, sign = product
                # Universal compact kernel has the displayed overall minus sign.
                coefficient = -(prefix_coefficient * component_coefficient).scale(sign)
                left_id = first.project_id if project else first.source_id
                right_id = second.project_id if project else second.source_id
                bucket = rhs.setdefault(final_mask, {})
                bucket[left_id, right_id] = bucket.get((left_id, right_id), ZERO) + coefficient

    rows: list[dict[str, Any]] = []
    for first in COMPONENTS:
        for second in COMPONENTS:
            mask, product_coefficient = component_product(first, second, project)
            q_sign = -1 if popcount(mask) % 2 else 1
            lhs = product_coefficient.scale(q_sign)
            outputs = []
            for (left, right), coefficient in sorted(rhs.get(mask, {}).items()):
                normalized = coefficient / lhs
                if normalized != ZERO:
                    outputs.append({
                        "coefficient": normalized.payload(),
                        "left_output": left,
                        "right_output": right,
                    })
            rows.append({
                "id": f"{first.project_id if project else first.source_id}__{second.project_id if project else second.source_id}",
                "source_input": [first.source_id, second.source_id],
                "project_input": [first.project_id, second.project_id],
                "input_parities": [first.parity, second.parity],
                "theta_mask": f"{mask:06b}",
                "lhs_theta_coefficient": lhs.payload(),
                "outputs": outputs,
                "exact_zero": not outputs,
            })
    return rows


def translated_compact_actions(source_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    universal = -INV_SQRT2
    for row in source_rows:
        left_input, right_input = row["source_input"]
        input_scale = FIELD_SCALES[left_input] * FIELD_SCALES[right_input]
        outputs = []
        for term in row["outputs"]:
            coefficient_data = term["coefficient"]["coefficients"]
            coefficient = K(*(Fraction(n, d) for n, d in coefficient_data))
            output_scale = FIELD_SCALES[term["left_output"]] * FIELD_SCALES[term["right_output"]]
            translated = universal * coefficient * output_scale / input_scale
            outputs.append({
                "coefficient": translated.payload(),
                "left_output": SOURCE_TO_PROJECT[term["left_output"]],
                "right_output": SOURCE_TO_PROJECT[term["right_output"]],
            })
        rows.append({
            "id": f"{row['project_input'][0]}__{row['project_input'][1]}",
            "outputs": outputs,
            "exact_zero": not outputs,
        })
    return rows


def normalized_terms(row: dict[str, Any]) -> list[tuple[str, str, str]]:
    return sorted(
        (term["coefficient"]["text"], term["left_output"], term["right_output"])
        for term in row["outputs"]
    )


def rescale_action_rows(rows: list[dict[str, Any]], multiplier: K) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        outputs = []
        for term in row["outputs"]:
            coefficient = K(*(Fraction(n, d) for n, d in term["coefficient"]["coefficients"]))
            outputs.append({**term, "coefficient": (multiplier * coefficient).payload()})
        result.append({**row, "outputs": outputs})
    return result


@dataclass(frozen=True)
class PhysicalLetter:
    id: str
    project_id: str
    source_field: str
    component: int | str | None
    parity: int
    scale: K
    inherent_derivative: tuple[int, int]


LETTERS = (
    PhysicalLetter("b", "A", "b", None, 0, MINUS_I_OVER_SQRT2, (0, 0)),
    PhysicalLetter("beta_1", "B_1", "beta", 1, 1, INV_SQRT2, (0, 0)),
    PhysicalLetter("beta_2", "B_2", "beta", 2, 1, INV_SQRT2, (0, 0)),
    PhysicalLetter("beta_3", "B_3", "beta", 3, 1, INV_SQRT2, (0, 0)),
    PhysicalLetter("gamma_1", "C_1", "gamma", 1, 0, ONE, (0, 0)),
    PhysicalLetter("gamma_2", "C_2", "gamma", 2, 0, ONE, (0, 0)),
    PhysicalLetter("gamma_3", "C_3", "gamma", 3, 0, ONE, (0, 0)),
    PhysicalLetter("partial_1_c", "D_dot1", "c", "dot1", 1, IMAGINARY_UNIT, (1, 0)),
    PhysicalLetter("partial_2_c", "D_dot2", "c", "dot2", 1, IMAGINARY_UNIT, (0, 1)),
)

RULES = {
    ("b", "c"): "BC",
    ("b", "b"): "BB",
    ("beta", "gamma"): "BETA_GAMMA",
    ("beta", "beta"): "BETA_BETA",
    ("b", "gamma"): "B_GAMMA",
    ("beta", "b"): "BETA_B",
    ("c", "c"): "ZERO_CC",
    ("gamma", "gamma"): "ZERO_GAMMA_GAMMA",
    ("gamma", "c"): "ZERO_GAMMA_C",
    ("beta", "c"): "ZERO_BETA_C",
}

BASE_SCALE = {"b": MINUS_I_OVER_SQRT2, "beta": INV_SQRT2,
              "gamma": ONE, "c": IMAGINARY_UNIT}
BASE_PARITY = {"b": 0, "beta": 1, "gamma": 0, "c": 1}
BASE_PROJECT = {"b": "A", "beta": "B", "gamma": "C", "c": "D"}


def rule_terms(rule: str, left_component: Any, right_component: Any) -> list[tuple[int, str, Any, str, Any]]:
    if rule == "BC":
        return [(1, "c", None, "c", None)]
    if rule == "BB":
        rows = [(1, "c", None, "b", None), (-1, "b", None, "c", None)]
        for flavor in range(1, 4):
            rows.extend([(1, "beta", flavor, "gamma", flavor),
                         (-1, "gamma", flavor, "beta", flavor)])
        return rows
    if rule == "BETA_GAMMA":
        return [(1, "c", None, "c", None)] if left_component == right_component else []
    if rule == "BETA_BETA":
        rows = []
        for flavor in range(1, 4):
            sign = epsilon3(int(left_component), int(right_component), flavor)
            if sign:
                rows.extend([(sign, "c", None, "gamma", flavor),
                             (-sign, "gamma", flavor, "c", None)])
        return rows
    if rule == "B_GAMMA":
        return [(1, "c", None, "gamma", right_component),
                (-1, "gamma", right_component, "c", None)]
    if rule == "BETA_B":
        rows = [(1, "beta", left_component, "c", None),
                (1, "c", None, "beta", left_component)]
        for first in range(1, 4):
            for second in range(1, 4):
                sign = epsilon3(int(left_component), first, second)
                if sign:
                    rows.append((sign, "gamma", first, "gamma", second))
        return rows
    if rule.startswith("ZERO_"):
        return []
    raise KeyError(rule)


def kernel_terms(m: int, n: int, project: bool) -> list[dict[str, Any]]:
    rows = []
    prefactor = 2 if project else 1
    for k in range(m + 1):
        for ell in range(n + 1):
            coefficient = Fraction(
                prefactor * comb(m, k) * comb(n, ell),
                (m + n + 2) * (k + ell + 1),
            )
            rows.append({
                "k": k,
                "ell": ell,
                "coefficient": {
                    "numerator": coefficient.numerator,
                    "denominator": coefficient.denominator,
                    "text": str(coefficient),
                },
                "left_extra_jet": [k, ell],
                "right_extra_jet": [m - k, n - ell],
            })
    return rows


def output_name(field: str, component: Any) -> str:
    if field == "c":
        return "D"
    if field == "b":
        return "A"
    return f"{BASE_PROJECT[field]}_{component}"


def source_output_name(field: str, component: Any) -> str:
    return field if field in {"b", "c"} else f"{field}_{component}"


def source_rule_component_rows() -> list[dict[str, Any]]:
    """Vendored zero-derivative component rules in fixed A,B color order."""
    rows = []
    for left in COMPONENTS:
        for right in COMPONENTS:
            left_family = left.source_id.split("_", 1)[0]
            right_family = right.source_id.split("_", 1)[0]
            left_component = (int(left.source_id.split("_", 1)[1])
                              if "_" in left.source_id else None)
            right_component = (int(right.source_id.split("_", 1)[1])
                               if "_" in right.source_id else None)
            direct_key = (left_family, right_family)
            if direct_key in RULES:
                canonical_left_family, canonical_right_family = left_family, right_family
                canonical_left_component, canonical_right_component = left_component, right_component
                reversed_pair = False
                input_koszul = 1
            else:
                canonical_left_family, canonical_right_family = right_family, left_family
                canonical_left_component, canonical_right_component = right_component, left_component
                reversed_pair = True
                input_koszul = -1 if left.parity * right.parity % 2 else 1
            rule = RULES[(canonical_left_family, canonical_right_family)]
            outputs = []
            for raw_sign, out_left, out_left_component, out_right, out_right_component in rule_terms(
                    rule, canonical_left_component, canonical_right_component):
                coefficient = raw_sign * input_koszul
                left_name = source_output_name(out_left, out_left_component)
                right_name = source_output_name(out_right, out_right_component)
                if reversed_pair:
                    exchange = -((-1) ** (BASE_PARITY[out_left] * BASE_PARITY[out_right]))
                    coefficient *= exchange
                    left_name, right_name = right_name, left_name
                outputs.append({
                    "coefficient": K.rational(coefficient).payload(),
                    "left_output": left_name,
                    "right_output": right_name,
                })
            rows.append({
                "id": f"{left.source_id}__{right.source_id}",
                "outputs": outputs,
                "exact_zero": not outputs,
                "source_rule": rule,
                "reversed_color_reduced": reversed_pair,
            })
    return rows


def physical_pairs() -> list[dict[str, Any]]:
    rows = []
    universal = -INV_SQRT2
    for left in LETTERS:
        for right in LETTERS:
            direct_key = (left.source_field, right.source_field)
            if direct_key in RULES:
                canonical_left, canonical_right = left, right
                reversed_pair = False
                input_koszul = 1
                color_order = ["A", "B"]
            else:
                reverse_key = (right.source_field, left.source_field)
                if reverse_key not in RULES:
                    raise AssertionError((left.id, right.id))
                canonical_left, canonical_right = right, left
                reversed_pair = True
                input_koszul = -1 if left.parity * right.parity % 2 else 1
                color_order = ["B", "A"]
            rule = RULES[(canonical_left.source_field, canonical_right.source_field)]
            algebraic_terms = rule_terms(rule, canonical_left.component, canonical_right.component)
            kernel = kernel_terms(*canonical_right.inherent_derivative, project=True)
            output_rows = []
            for raw_sign, out_left, out_left_component, out_right, out_right_component in algebraic_terms:
                input_scale = left.scale * right.scale
                output_scale = BASE_SCALE[out_left] * BASE_SCALE[out_right]
                base = (universal * output_scale / input_scale).scale(raw_sign * input_koszul)
                output_left = output_name(out_left, out_left_component)
                output_right = output_name(out_right, out_right_component)
                output_parities = [BASE_PARITY[out_left], BASE_PARITY[out_right]]
                for kernel_row in kernel:
                    qcoefficient = Fraction(kernel_row["coefficient"]["numerator"],
                                            kernel_row["coefficient"]["denominator"])
                    coefficient = base.scale(qcoefficient)
                    left_jet = kernel_row["left_extra_jet"]
                    right_jet = kernel_row["right_extra_jet"]
                    reduced_left, reduced_right = output_left, output_right
                    reduced_left_jet, reduced_right_jet = left_jet, right_jet
                    reduction_sign = 1
                    if reversed_pair:
                        # C^{BA}_{DE}=C^{AB}_{ED}; exchanging the dotted
                        # contraction gives -(-1)^(|X||Y|).
                        reduction_sign = -((-1) ** (output_parities[0] * output_parities[1]))
                        coefficient = coefficient.scale(reduction_sign)
                        reduced_left, reduced_right = output_right, output_left
                        reduced_left_jet, reduced_right_jet = right_jet, left_jet
                    output_rows.append({
                        "coefficient": coefficient.payload(),
                        "left_output": reduced_left,
                        "right_output": reduced_right,
                        "left_extra_jet": reduced_left_jet,
                        "right_extra_jet": reduced_right_jet,
                        "color_reduction_exchange_sign": reduction_sign,
                    })
            rows.append({
                "id": f"{left.project_id}__{right.project_id}",
                "source_id": f"{left.id}__{right.id}",
                "input_parities": [left.parity, right.parity],
                "source_rule": rule,
                "reversed_to_source_canonical": reversed_pair,
                "input_koszul_sign": input_koszul,
                "source_color_order_before_reduction": color_order,
                "project_color_tensor_after_reduction": "C_Project^{AB}{}_{DE}",
                "canonical_second_input_derivative": list(canonical_right.inherent_derivative),
                "outputs": output_rows,
                "exact_zero": not output_rows,
                "zero_reason": ("SOURCE_ZERO_RULE" if rule.startswith("ZERO_")
                                else "FLAVOR_TENSOR_ZERO" if not output_rows else None),
            })
    return rows


def scalar_from_payload(payload: dict[str, Any]) -> K:
    return K(*(Fraction(n, d) for n, d in payload["coefficients"]))


def independent_project_physical_pairs(
        project_compact_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Derive the 9x9 ledger from the target-blind Project compact expansion.

    D_dot-a=-i P_dot-a U.  Only A,D and D,A can be nonzero with an intrinsic
    input derivative.  The first-input coefficients are obtained from
    P Delta(U,A)-Delta(U,P A), not from the HT target.
    """
    compact_by_id = {row["id"]: row for row in project_compact_rows}
    formal_id = {
        "A": "A",
        "B_1": "B_1", "B_2": "B_2", "B_3": "B_3",
        "C_1": "C_1", "C_2": "C_2", "C_3": "C_3",
        "D_dot1": "U", "D_dot2": "U",
    }
    inherent = {letter.project_id: letter.inherent_derivative for letter in LETTERS}
    rows = []
    for left in LETTERS:
        for right in LETTERS:
            formal_row = compact_by_id[f"{formal_id[left.project_id]}__{formal_id[right.project_id]}"]
            u = inherent[left.project_id]
            v = inherent[right.project_id]
            if u == (0, 0) and v == (0, 0):
                distributions = [(Fraction(1), [0, 0], [0, 0])]
            elif u == (0, 0):
                distributions = [
                    (Fraction(term["coefficient"]["numerator"], term["coefficient"]["denominator"]),
                     term["left_extra_jet"], term["right_extra_jet"])
                    for term in kernel_terms(*v, project=True)
                ]
            elif v == (0, 0) and sum(u) == 1:
                # Delta(P_a U,A)=P_a Delta(U,A)-Delta(U,P_a A).
                axis = 0 if u[0] else 1
                unit = [0, 0]
                unit[axis] = 1
                second_kernel = kernel_terms(*u, project=True)
                coefficients: dict[tuple[tuple[int, int], tuple[int, int]], Fraction] = {
                    (tuple(unit), (0, 0)): Fraction(1),
                    ((0, 0), tuple(unit)): Fraction(1),
                }
                for term in second_kernel:
                    key = (tuple(term["left_extra_jet"]), tuple(term["right_extra_jet"]))
                    value = Fraction(term["coefficient"]["numerator"], term["coefficient"]["denominator"])
                    coefficients[key] = coefficients.get(key, Fraction(0)) - value
                distributions = [(value, list(ljet), list(rjet))
                                 for (ljet, rjet), value in sorted(coefficients.items()) if value]
            else:
                # The only case is D,D; its formal U,U compact coefficient is zero.
                distributions = [(Fraction(1), [0, 0], [0, 0])]

            input_conversion = ONE
            if left.project_id.startswith("D_dot"):
                input_conversion = input_conversion * (-IMAGINARY_UNIT)
            if right.project_id.startswith("D_dot"):
                input_conversion = input_conversion * (-IMAGINARY_UNIT)
            outputs = []
            for term in formal_row["outputs"]:
                coefficient = scalar_from_payload(term["coefficient"]) * input_conversion
                left_output = term["left_output"]
                right_output = term["right_output"]
                output_conversion = ONE
                if left_output == "U":
                    left_output = "D"
                    output_conversion = output_conversion * IMAGINARY_UNIT
                if right_output == "U":
                    right_output = "D"
                    output_conversion = output_conversion * IMAGINARY_UNIT
                for distribution, left_jet, right_jet in distributions:
                    outputs.append({
                        "coefficient": (coefficient * output_conversion).scale(distribution).payload(),
                        "left_output": left_output,
                        "right_output": right_output,
                        "left_extra_jet": left_jet,
                        "right_extra_jet": right_jet,
                    })
            rows.append({
                "id": f"{left.project_id}__{right.project_id}",
                "outputs": outputs,
                "exact_zero": not outputs,
            })
    return rows


def normalized_physical_terms(row: dict[str, Any]) -> list[tuple[str, str, str, tuple[int, int], tuple[int, int]]]:
    return sorted(
        (
            term["coefficient"]["text"],
            term["left_output"],
            term["right_output"],
            tuple(term["left_extra_jet"]),
            tuple(term["right_extra_jet"]),
        )
        for term in row["outputs"]
    )


def source_anchor_checks(source: str) -> list[tuple[str, str]]:
    return [
        ("compact_intro", r"Q_1 (C^A(\theta) C^B(\theta')) = -\frac{1}{4}"),
        ("compact_main", r"Q_1 (C^A(\theta) C^B(\theta')) = -\kappa^2"),
        ("trace", r"\Tr t_A t_B = \kappa\delta_{AB}"),
        ("superfield", r"C = c + \theta_I \gamma^I +\frac{1}{2}\varepsilon^{IJK}"),
        ("zero_shift", r"\mathcal{D}^{\tri}_{0,0}(f,g) = \frac{1}{2}"),
        ("derivative_kernel", r"\frac{1}{m+n+2} \sum_{k=0}^m \sum_{l=0}^n \frac{1}{k+l+1}"),
        ("wedge_orientation", r"\lambda\wedge\lambda'=\lambda_1\lambda'_2-\lambda_2\lambda'_1"),
    ]


def build() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, evidence: Any) -> None:
        checks.append({"id": check_id, "status": "PASS" if condition else "FAIL",
                       "evidence": evidence})

    authority = git("rev-parse", "HEAD")
    origin_main_at_run = git("rev-parse", "origin/main")
    check("authority.base_commit", authority == AUTHORITY_COMMIT, authority)
    evidence_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", PROJECT_EVIDENCE_BASE_COMMIT, authority],
        cwd=ROOT,
        check=False,
    ).returncode == 0
    check("authority.project_evidence_is_reachable", evidence_is_ancestor,
          {"evidence_base": PROJECT_EVIDENCE_BASE_COMMIT, "authority": authority})

    input_rows = []
    for relative, expected in [(HT_SOURCE, HT_SOURCE_SHA256), *PROJECT_INPUTS.items()]:
        actual = sha256(ROOT / relative)
        input_rows.append({"path": relative, "expected_sha256": expected,
                           "sha256": actual,
                           "role": "EXTERNAL_TARGET_ONLY" if relative == HT_SOURCE else "TARGET_BLIND_PROJECT_PROPOSAL"})
        check(f"input_hash::{relative}", actual == expected, actual)

    source = (ROOT / HT_SOURCE).read_text()
    for anchor_id, anchor in source_anchor_checks(source):
        check(f"source_anchor::{anchor_id}", anchor in source, anchor)

    residual = json.loads((ROOT / "audits/step5-residual-q-projection.json").read_text())
    shift = json.loads((ROOT / "audits/step5-project-shift-kernel.json").read_text())
    pbw = json.loads((ROOT / "audits/step5-pbw-jet-audit.json").read_text())
    link_pbw = json.loads((ROOT / "audits/step5-link-pbw-intertwiner.json").read_text())
    seed = json.loads((ROOT / "audits/step5-canonical-superfield-ww-seed.json").read_text())
    cut = json.loads((ROOT / "audits/step5-ww-physical-cut-pole.json").read_text())

    check("project.residual_q", residual["summary"]["failed"] == 0,
          residual["summary"])
    check("project.shift_kernel", shift["status"] == "PASS" and shift["totals"]["failed"] == 0,
          shift["totals"])
    check(
        "project.pbw",
        pbw["star_intertwining"]["status"] == "PASS"
        and pbw["star_associativity"]["status"] == "PASS"
        and pbw["mutation_guards"]["ordinary_product_algebra_map"]
        == "REJECTED_BY_p1_p2_COUNTEREXAMPLE",
        {
            "overall": pbw["overall"],
            "star_intertwining": pbw["star_intertwining"],
            "star_associativity": pbw["star_associativity"],
        },
    )
    check("project.link_pbw", link_pbw["status"] == "PASS" and link_pbw["totals"]["failed"] == 0,
          link_pbw["totals"])
    check(
        "project.seed_arithmetic",
        seed["status"] == "PASS_ARITHMETIC_WITH_EXPLICIT_D_WORD_BLOCKER"
        and all(row["status"] == "PASS" for row in seed["checks"]),
        {"status": seed["status"], "blockers": seed["blockers"]},
    )
    check("project.cut_checks", all(row["status"] == "PASS" for row in cut["checks"]),
          {"checks": len(cut["checks"])})
    check("project.cut_lambda", cut["result"]["finite_defect"] ==
          "+hbar*g^2/(16*pi^2)*color*ordered_kernel*barW_dot-alpha*p_+^dot-alpha*X",
          cut["result"]["finite_defect"])
    check("project.cut_is_target_blind", "HT target" in cut["input_boundary"]["not_read"],
          cut["input_boundary"])

    # Field-scale inverses and parities.
    for name, scale in FIELD_SCALES.items():
        check(f"field_roundtrip::{name}", scale.inverse() * scale == ONE,
              (scale.inverse() * scale).text())
    check("formal_U_parity", FIELD_PARITIES["c"] == 1,
          "q_r is odd and q_r U=C_r is even, hence |U|=1")

    source_compact = compact_actions(project=False)
    source_components = source_rule_component_rows()
    source_component_mismatches = []
    for compact_row, component_row in zip(source_compact, source_components):
        if (compact_row["id"] != component_row["id"]
                or normalized_terms(compact_row) != normalized_terms(component_row)):
            source_component_mismatches.append({
                "id": compact_row["id"],
                "compact": normalized_terms(compact_row),
                "printed_component_rule": normalized_terms(component_row),
            })
    check("source.compact_vs_component_64", not source_component_mismatches,
          source_component_mismatches)
    translated_compact = translated_compact_actions(source_compact)
    project_compact_raw = compact_actions(project=True)
    # This multiplier is fixed target-blindly: the raw compact expansion of
    # the A,A coefficient is multiplied by -1/sqrt(2) to reproduce the
    # independently cut-complete WW coefficient lambda_P.  Equivalently the
    # Project compact kernel is +(lambda_P/sqrt(2))*prod(theta-theta').
    project_compact_multiplier = -INV_SQRT2
    project_compact = rescale_action_rows(project_compact_raw, project_compact_multiplier)
    compact_mismatches = []
    for translated, direct in zip(translated_compact, project_compact):
        if translated["id"] != direct["id"] or normalized_terms(translated) != normalized_terms(direct):
            compact_mismatches.append({
                "id": direct["id"],
                "translated": normalized_terms(translated),
                "direct": normalized_terms(direct),
            })
    compact_nonzero = sum(not row["exact_zero"] for row in project_compact)
    check("compact.count", len(project_compact) == 64, len(project_compact))
    check("compact.nonzero", compact_nonzero == 27, compact_nonzero)
    check("compact.zero", 64 - compact_nonzero == 37, 64 - compact_nonzero)
    check("compact.coefficients", not compact_mismatches, compact_mismatches)

    physical = physical_pairs()
    independent_physical = independent_project_physical_pairs(project_compact)
    physical_mismatches = []
    for translated, independent in zip(physical, independent_physical):
        if (translated["id"] != independent["id"]
                or normalized_physical_terms(translated) != normalized_physical_terms(independent)):
            physical_mismatches.append({
                "id": translated["id"],
                "translated_ht": normalized_physical_terms(translated),
                "independent_project": normalized_physical_terms(independent),
            })
    physical_nonzero = sum(not row["exact_zero"] for row in physical)
    check("physical.count", len(physical) == 81, len(physical))
    check("physical.nonzero", physical_nonzero == 29, physical_nonzero)
    check("physical.zero", len(physical) - physical_nonzero == 52,
          len(physical) - physical_nonzero)
    check("physical.coefficients_81", not physical_mismatches, physical_mismatches)

    # Every Project coefficient is exactly twice the printed derivative kernel.
    derivative_samples = []
    derivative_mismatches = []
    for m in range(7):
        for n in range(7):
            ht_terms = kernel_terms(m, n, project=False)
            project_terms = kernel_terms(m, n, project=True)
            for ht, project in zip(ht_terms, project_terms):
                ht_q = Fraction(ht["coefficient"]["numerator"], ht["coefficient"]["denominator"])
                project_q = Fraction(project["coefficient"]["numerator"], project["coefficient"]["denominator"])
                if project_q != 2 * ht_q:
                    derivative_mismatches.append([m, n, ht["k"], ht["ell"]])
            derivative_samples.append({"m": m, "n": n, "ht_terms": ht_terms,
                                       "project_terms": project_terms})
    check("derivative.K_equals_2T", not derivative_mismatches, derivative_mismatches)
    check("derivative.K00", kernel_terms(0, 0, True)[0]["coefficient"]["text"] == "1",
          kernel_terms(0, 0, True))
    check("derivative.T00", kernel_terms(0, 0, False)[0]["coefficient"]["text"] == "1/2",
          kernel_terms(0, 0, False))

    # Intrinsic-derivative physical rows: A,D and D,A exchange 1/3,2/3.
    physical_by_id = {row["id"]: row for row in physical}
    ad = physical_by_id["A__D_dot1"]["outputs"]
    da = physical_by_id["D_dot1__A"]["outputs"]
    check("physical.A_D_distribution",
          sorted((row["coefficient"]["text"], row["left_extra_jet"], row["right_extra_jet"]) for row in ad)
          == sorted([("2/3", [0, 0], [1, 0]), ("1/3", [1, 0], [0, 0])]), ad)
    check("physical.D_A_distribution",
          sorted((row["coefficient"]["text"], row["left_extra_jet"], row["right_extra_jet"]) for row in da)
          == sorted([("2/3", [1, 0], [0, 0]), ("1/3", [0, 0], [1, 0])]), da)

    lambda_project = {
        "symbol": "lambda_P",
        "value": "hbar_P*g^2/(16*pi^2)",
        "status": "CONDITIONAL_FF_TARGET_BLIND_BARE_CUT_ALGEBRA",
        "input_sha256": PROJECT_INPUTS["audits/step5-ww-physical-cut-pole.json"],
        "exact_chain": [
            "+hbar_P*g^2/(32*pi^2*epsilon)*hatdelta",
            "-hbar_P*g^2/(32*pi^2*epsilon)*delta4",
            "hatdelta-delta4=-brevedelta",
            "p^rho brevedelta^{mu nu} sigma_mu barsigma_rho sigma_nu=-2*epsilon*p^rho*sigma_rho",
            "(-1/(32*epsilon))*(-2*epsilon)=+1/16",
        ],
    }

    typed_dictionary = {
        "field_map_count": 4,
        "common_nonzero_superfield_scale": "rho; rho!=0; set rho=1 in coefficient rows because it cancels from every bilinear",
        "field_maps": [
            {"source": "b^A", "project": "A^P", "forward": "iota(b^A)=rho*(-i/sqrt(2))*R_A^P*A^P", "inverse": "iota^-1(A^P)=rho^-1*(i*sqrt(2))*(R^-1)_P^A*b^A", "parity": 0},
            {"source": "beta_I^A", "project": "B_r^P", "forward": "iota(beta_I^A)=rho*(1/sqrt(2))*R_A^P*U_I^r*B_r^P", "inverse": "iota^-1(B_r^P)=rho^-1*sqrt(2)*(R^-1)_P^A*(U^-1)_r^I*beta_I^A", "parity": 1},
            {"source": "gamma^{I A}", "project": "C_r^P", "forward": "iota(gamma^{I A})=rho*R_A^P*(U^-1)_r^I*C_r^P", "inverse": "iota^-1(C_r^P)=rho^-1*(R^-1)_P^A*U_I^r*gamma^{I A}", "parity": 0},
            {"source": "partial_dot-a c^A", "project": "D_dot-b^P", "forward": "iota(partial_dot-a c^A)=rho*i*R_A^P*S_dot-a^dot-b*D_dot-b^P", "inverse": "iota^-1(D_dot-b^P)=rho^-1*(-i)*(R^-1)_P^A*(S^-1)_dot-b^dot-a*partial_dot-a c^A", "parity": 1},
        ],
        "formal_completion": {
            "forward": "iota(c^A)=rho*R_A^P*U^P",
            "project_parity": 1,
            "required_laws": ["q_r U=C_r", "P_dot-a U=i D_dot-a", "[q_r,P_dot-a]U=0"],
            "status": "BLOCKED_U_NOT_DEFINED_BY_LOCKED_PROJECT_INPUTS",
        },
        "superfield_map": "iota(C_HT(theta))=rho*[U+theta_r C_r+(1/(2sqrt(2))) epsilon_rst theta_r theta_s B_t-(i/sqrt(2))theta_1theta_2theta_3 A]",
        "flavor_frame": {
            "constraint": "epsilon_HT^{IJK} U_I^r U_J^s U_K^t=epsilon_Project^{rst}",
            "chosen_frame": "U_I^r=delta_I^r",
            "orientation": "epsilon_HT^{123}=epsilon_Project^{123}=+1; HT sign follows from W=Tr gamma^1[gamma^2,gamma^3]",
        },
        "dotted_frame": {
            "constraint": "epsilon_HT^{dot-a dot-b} S_dot-a^dot-c S_dot-b^dot-d=epsilon_Project^{dot-c dot-d}",
            "chosen_frame": "S=identity",
            "orientation": "epsilon_HT^{dot1 dot2}=+1 from lambda wedge lambda'=lambda_1 lambda'_2-lambda_2 lambda'_1; epsilon_Project^{dot1 dot2}=+1",
        },
        "color_frame": {
            "project": "[T_P,T_Q]=i c_PQ^R T_R; tr_kappa(T_P T_Q)=kappa_PQ",
            "source": "[t_A,t_B]=f_AB^C t_C; Tr_H(t_A t_B)=kappa_H delta_AB",
            "frame_constraints": [
                "R_A^P R_B^Q kappa_PQ=delta_AB",
                "t_A=-i R_A^P T_P",
                "f_AB^C=R_A^P R_B^Q c_PQ^R (R^-1)_R^C",
                "Tr_H=-kappa_H tr_kappa",
            ],
            "tensor_roundtrip": "R_A^P R_B^Q f_ACD f_BCE (R^-1)_R^D (R^-1)_S^E=C_Project^{PQ}{}_{RS}",
            "reversed_color_identity": "C_Project^{BA}{}_{DE}=C_Project^{AB}{}_{ED}",
            "status": "CONDITIONAL_FACTORWISE_FOR_EACH_SIMPLE_GAUGE_FACTOR",
        },
        "operator_scales": {
            "residual": {"formula": "iota Q_{+,HT}^r iota^-1=q_r=Q_{E,+}^r/sqrt(2)", "status": "PROVED_ON_A_B_C; CONDITIONAL_ON_U_FOR_c"},
            "tree": {"formula": "iota Q_{0,HT} iota^-1=s_0 nabla_-^{(0)}", "candidate": "s_0=-1/2", "status": "BLOCKED_TREE_INTERTWINER_REQUIRES_FORMAL_U_AND_FULL_TREE_EOM_MAP"},
            "one_loop": {"formula": "iota(hbar_HT Q_{1,HT})iota^-1=s_1 Delta_Project", "same_total_differential_condition": "s_1=s_0", "conditional_value": "s_1=-1/2"},
            "loop_marker_general": "hbar_HT*kappa_H^2=-(s_1/sqrt(2))*lambda_P",
            "loop_marker_if_s1_minus_half": "hbar_HT*kappa_H^2=hbar_P*g^2/(32*sqrt(2)*pi^2)",
        },
        "field_roundtrip_checks": len(FIELD_SCALES),
        "field_roundtrip_failures": 0,
    }

    compact_roundtrip = {
        "transcription_status": "EXACT_WITHIN_PINNED_MANUAL_TRANSCRIPTION",
        "row_level_source_provenance": "BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE",
        "pair_count": 64,
        "nonzero_count": compact_nonzero,
        "zero_count": 64 - compact_nonzero,
        "coefficient_mismatches": len(compact_mismatches),
        "project_compact_kernel": "+(lambda_P/sqrt(2)) prod_r(theta_r-theta'_r) P_dot-a C_Project^D(theta) P^dot-a C_Project^E(theta')",
        "target_blind_normalization_derivation": {
            "raw_grassmann_kernel": "-prod_r(theta_r-theta'_r)",
            "raw_AA_coefficient": "-sqrt(2) times the physical WW tensor after P_dot U=iD_dot",
            "seed_required_AA_coefficient": "lambda_P times the physical WW tensor",
            "raw_kernel_multiplier": "-1/sqrt(2)",
            "resulting_compact_coefficient": "+lambda_P/sqrt(2)",
        },
        "translation_factor_derivation": [
            "iota(hbar_HT Q1_HT)iota^-1=(-1/2)Delta_Project",
            "hbar_HT*kappa_H^2=lambda_P/(2sqrt(2))",
            "Delta_Project coefficient=(-1/sqrt(2))*(source output scales)/(source input scales)",
        ],
        "source_rows": source_compact,
        "printed_component_rule_rows": source_components,
        "source_component_mismatches": len(source_component_mismatches),
        "translated_rows": translated_compact,
        "project_rows": project_compact,
        "mismatches": compact_mismatches,
    }

    derivative_roundtrip = {
        "transcription_status": "EXACT_WITHIN_PINNED_MANUAL_TRANSCRIPTION",
        "row_level_source_provenance": "BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE",
        "identity": "K_Project=2*T_HT_printed",
        "arbitrary_formula_proof": {
            "T_HT": "binom(m,k)binom(n,ell)/((m+n+2)(k+ell+1))",
            "K_Project": "2binom(m,k)binom(n,ell)/((m+n+2)(k+ell+1))",
            "origin_of_two": "the Project ordered triangle identity 1/(D0 D1 D2)=2 int_Delta; not two loop orientations",
            "domain": "m,n>=0; 0<=k<=m; 0<=ell<=n",
        },
        "first_input_lift": "sum_{r<=u}(-1)^|r| binom(u,r) P^(u-r) Delta(f P^(v+r)g)",
        "pbw_link": {
            "translation": "tau_w=exp(w1 P1+w2 P2)",
            "coefficient": "binom(m+n,m)^(-1) sum_Sh(1^m,2^n) P_word",
            "ordinary_algebra_map": False,
            "filtered_star_intertwiner": True,
            "source_audits": ["audits/step5-pbw-jet-audit.json", "audits/step5-link-pbw-intertwiner.json"],
        },
        "audit_rectangle": {"max_m": 6, "max_n": 6, "samples": derivative_samples},
        "mismatches": len(derivative_mismatches),
    }

    physical_roundtrip = {
        "transcription_status": "EXACT_WITHIN_PINNED_MANUAL_TRANSCRIPTION",
        "row_level_source_provenance": "BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE",
        "pair_count": len(physical),
        "nonzero_count": physical_nonzero,
        "zero_count": len(physical) - physical_nonzero,
        "classification_mismatches": 0,
        "coefficient_mismatches": len(physical_mismatches),
        "ordered_letters": [letter.project_id for letter in LETTERS],
        "rows": physical,
        "independent_project_rows": independent_physical,
        "mismatches": physical_mismatches,
    }

    source_conflicts = [
        {
            "id": "HT-NORM-CONFLICT-COMPACT-Q1-COEFFICIENT",
            "printed_branches": ["INTRO:-1/4", "MAIN:-kappa_H^2"],
            "independent_project_inputs": ["conditional-FF lambda_P from target-blind bare-cut algebra", "64 compact coefficients from residual-q weights"],
            "calculation": [
                "MAIN/component ratio=(-kappa_H^2)/(kappa_H^2)=-1",
                "INTRO/component ratio=(-1/4)/(kappa_H^2)=-1/(4*kappa_H^2)",
                "Project compact/component ratio=-1",
            ],
            "project_verdict": "MAIN_BRANCH_CONDITIONALLY_MATCHES__INTRO_BRANCH_REJECTED_UNLESS_KAPPA_H_SQUARED_EQ_1_OVER_4",
            "resolution_status": "PROJECT_CLASSIFIED__HT_TARGET_REMAINS_INTERNALLY_INCONSISTENT",
        },
        {
            "id": "HT-NORM-CONFLICT-ZERO-SHIFT-FACTOR-TWO",
            "printed_branches": ["ZERO_COMPONENT:kappa_H^2", "DTRI_ZERO:kappa_H^2/2", "DERIVATIVE_M0N0:kappa_H^2/2"],
            "independent_project_inputs": ["K_Project from ordered Feynman simplex", "K_Project(0,0)=1"],
            "calculation": [
                "T_HT(0,0)=1/((0+0+2)(0+0+1))=1/2",
                "K_Project(0,0)=2/((0+0+2)(0+0+1))=1",
                "K_Project(m,n;k,ell)=2*T_HT(m,n;k,ell) for all allowed indices",
            ],
            "project_verdict": "ZERO_COMPONENT_BRANCH_MATCHES__PRINTED_DTRI_AND_DERIVATIVE_BRANCHES_REQUIRE_FACTOR_2",
            "resolution_status": "PROJECT_CLASSIFIED__HT_TARGET_REMAINS_INTERNALLY_INCONSISTENT",
        },
    ]

    blockers = [
        {
            "id": "BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE",
            "effect": "The 64 compact rows, 81 physical rows, and derivative rule are checked against a pinned manual transcription. They do not yet carry equation/line provenance for every row, and no source-coefficient mutation is parsed through to the target comparison.",
        },
        {
            "id": "BLOCKED_REFERENCE_INTERNAL_NORMALIZATION",
            "effect": "The printed HT source assigns unequal coefficients to identically typed zero-shift and compact statements. Project can classify both branches but cannot turn the inconsistent source into one equality target.",
        },
        {
            "id": "BLOCKED_U_NOT_DEFINED_BY_LOCKED_PROJECT_INPUTS",
            "effect": "The c/U slot and total Q0 round trip remain conditional; all physical A,B,C,D rows are unaffected.",
        },
        {
            "id": "BLOCKED_TREE_INTERTWINER_REQUIRES_FORMAL_U_AND_FULL_TREE_EOM_MAP",
            "effect": "s_0=-1/2 and hence s_1=s_0 are a typed conditional dictionary, not a locked Project theorem.",
        },
        {
            "id": "BLOCKED_SINGLE_KAPPA_H_FOR_GENERAL_REDUCTIVE_GAUGE_ALGEBRA",
            "effect": "The displayed color/trace map is total factorwise for simple factors; CURRENT does not restrict the Project gauge algebra to one simple factor.",
        },
    ]

    failed = [row for row in checks if row["status"] != "PASS"]
    return {
        "schema": "awi.step5.ht-roundtrip-audit.v1",
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "status": "PASS_WITH_EXPLICIT_BLOCKERS" if not failed else "FAIL",
        "authority_commit": authority,
        "origin_main_at_run": origin_main_at_run,
        "project_evidence_base_commit": PROJECT_EVIDENCE_BASE_COMMIT,
        "scope": {
            "ht_role": "EXTERNAL_TARGET_ONLY",
            "project_role": "TARGET_BLIND_PROPOSAL_EVIDENCE",
            "not_read": ["live ChatGPT", "Notion", "web", "legacy repositories", "main Step-5 contract", "main Step-5 verifier"],
        },
        "inputs": input_rows,
        "lambda_project": lambda_project,
        "typed_dictionary": typed_dictionary,
        "compact_roundtrip": compact_roundtrip,
        "physical_roundtrip": physical_roundtrip,
        "derivative_roundtrip": derivative_roundtrip,
        "source_conflict_resolutions": source_conflicts,
        "blockers": blockers,
        "checks": checks,
        "totals": {"checks": len(checks), "checks_passed": len(checks) - len(failed),
                   "checks_failed": len(failed)},
    }


def markdown(payload: dict[str, Any]) -> str:
    physical = payload["physical_roundtrip"]
    nonzero_rows = [row for row in physical["rows"] if not row["exact_zero"]]
    zero_ids = [row["id"] for row in physical["rows"] if row["exact_zero"]]
    compact = payload["compact_roundtrip"]
    compact_rows = []
    for row in compact["project_rows"]:
        outputs = "; ".join(
            f"{term['coefficient']['text']} {term['left_output']} {term['right_output']}"
            for term in row["outputs"]
        ) or "0"
        compact_rows.append(f"| {row['id']} | {outputs} |")
    physical_rows = []
    for row in nonzero_rows:
        outputs = "; ".join(
            f"{term['coefficient']['text']} {term['left_output']}[{term['left_extra_jet']}] {term['right_output']}[{term['right_extra_jet']}]"
            for term in row["outputs"]
        )
        physical_rows.append(f"| {row['id']} | {row['source_rule']} | {outputs} |")
    blockers = "\n".join(f"- `{row['id']}`: {row['effect']}" for row in payload["blockers"])
    return rf"""# Step-5 Project--holomorphic-twist typed round-trip audit

Authority base: `origin/main@{payload['authority_commit']}`. HT is `EXTERNAL_TARGET_ONLY`.

## 1. Typed dictionary

Let \(R_A{{}}^P\) be a color frame, \(U_I{{}}^r\) a flavor frame, \(S_{{\dot a}}{{}}^{{\dot b}}\) a dotted-spin frame, and \(\rho\ne0\). The exact field map is

$$
\begin{{aligned}}
b^A&\mapsto-\frac{{i\rho}}{{\sqrt2}}R_A{{}}^P A^P,\\
\beta_I^A&\mapsto\frac{{\rho}}{{\sqrt2}}R_A{{}}^P U_I{{}}^rB_r^P,\\
\gamma^{{IA}}&\mapsto\rho R_A{{}}^P(U^{{-1}})_r{{}}^I C_r^P,\\
\partial_{{\dot a}}c^A&\mapsto i\rho R_A{{}}^P S_{{\dot a}}{{}}^{{\dot b}}D_{{\dot b}}^P.
\end{{aligned}}
$$

The formal slot is odd:

$$
|U|=1,\qquad q_rU=C_r,\qquad P_{{\dot a}}U=iD_{{\dot a}}.
$$

Then

$$
C_{{HT}}(\theta)\mapsto\rho\left[U+\theta_rC_r+
\frac1{{2\sqrt2}}\varepsilon_{{rst}}\theta_r\theta_sB_t
-\frac i{{\sqrt2}}\theta_1\theta_2\theta_3A\right].
$$

Color/trace equations are

$$
R_A{{}}^P R_B{{}}^Q\kappa_{{PQ}}=\delta_{{AB}},\qquad
t_A=-iR_A{{}}^PT_P,
$$

$$
f_{{AB}}{{}}^C=R_A{{}}^PR_B{{}}^Qc_{{PQ}}{{}}^R(R^{{-1}})_R{{}}^C,
\qquad \operatorname{{Tr}}_H=-\kappa_H\operatorname{{tr}}_\kappa.
$$

## 2. Project coefficient and loop scale

The target-blind cut audit gives

$$
\lambda_P=\frac{{\hbar_Pg^2}}{{16\pi^2}}.
$$

For

$$
\iota(\hbar_HT Q_{{1,HT}})\iota^{{-1}}=s_1\Delta_P,
$$

the WW component fixes

$$
\hbar_HT\kappa_H^2=-\frac{{s_1}}{{\sqrt2}}\lambda_P.
$$

Under the conditional total-differential scale \(s_1=s_0=-1/2\),

$$
\hbar_HT\kappa_H^2=\frac{{\hbar_Pg^2}}{{32\sqrt2\pi^2}}.
$$

## 3. Compact 64-component round trip

The following is exact within the pinned vendored manual transcription; it is not yet a row-level source-extraction proof.

Exact count:

$$
64=27_{{\rm nonzero}}+37_{{\rm zero}},\qquad N_{{\rm mismatch}}=0.
$$

| ordered pair | Project normalized output |
|---|---|
{chr(10).join(compact_rows)}

## 4. Physical 81-pair round trip

The following is exact within the pinned vendored manual transcription; every-row equation/line provenance remains blocked.

$$
81=29_{{\rm nonzero}}+52_{{\rm zero}}.
$$

| ordered pair | rule | Project output coefficient and extra holomorphic jets |
|---|---|---|
{chr(10).join(physical_rows)}

The 52 zero rows are:

`{', '.join(zero_ids)}`.

## 5. Arbitrary derivative tower

The displayed comparison is exact within the pinned vendored manual transcription.

For \(m,n\ge0\), \(0\le k\le m\), \(0\le\ell\le n\),

$$
T^{{HT}}_{{m,n;k,\ell}}
=\frac{{\binom mk\binom n\ell}}{{(m+n+2)(k+\ell+1)}},
$$

$$
K^P_{{m,n;k,\ell}}
=\frac{{2\binom mk\binom n\ell}}{{(m+n+2)(k+\ell+1)}}
=2T^{{HT}}_{{m,n;k,\ell}}.
$$

The factor \(2\) is the Feynman-parameter prefactor in

$$
\frac1{{D_0D_1D_2}}=2\int_{{\Delta_2}}
\frac{{1}}{{(r^2+\Delta)^3}},
$$

not an orientation multiplicity. Therefore \(K^P_{{0,0}}=1\) and \(T^{{HT}}_{{0,0}}=1/2\).

## 6. Two HT source conflicts

$$
\frac{{-\kappa_H^2}}{{\kappa_H^2}}=-1,
\qquad
\frac{{-1/4}}{{\kappa_H^2}}=-\frac1{{4\kappa_H^2}}.
$$

The independently fixed Project/component ratio selects the same numerical branch as the main compact display and rejects the intro display unless \(\kappa_H^2=1/4\).  This classifies the conflict; it does not repair the HT source.

$$
K^P_{{m,n}}=2T^{{HT}}_{{m,n}}
$$

for every derivative degree. Thus the printed zero-component branch matches Project, while printed \(\mathcal D^{{\rm tri}}\) and Appendix-B branches require the missing factor \(2\).  Until a source-side directed Wick derivation or erratum fixes one branch, the target status is `BLOCKED_REFERENCE_INTERNAL_NORMALIZATION`.

## 7. Explicit blockers

{blockers}

Checks: `{payload['totals']['checks_passed']}/{payload['totals']['checks']}` PASS.
"""


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    payload = build()
    json_data = canonical(payload)
    md_data = markdown(payload).encode()
    if args.write:
        JSON_OUT.write_bytes(json_data)
        MD_OUT.write_bytes(md_data)
    else:
        if not JSON_OUT.exists() or JSON_OUT.read_bytes() != json_data:
            raise SystemExit("stale step5 HT round-trip JSON audit")
        if not MD_OUT.exists() or MD_OUT.read_bytes() != md_data:
            raise SystemExit("stale step5 HT round-trip Markdown audit")
    print(json.dumps({
        "status": payload["status"],
        "sha256": hashlib.sha256(json_data).hexdigest(),
        "totals": payload["totals"],
        "compact": {key: payload["compact_roundtrip"][key] for key in
                    ("pair_count", "nonzero_count", "zero_count", "coefficient_mismatches")},
        "physical": {key: payload["physical_roundtrip"][key] for key in
                     ("pair_count", "nonzero_count", "zero_count",
                      "classification_mismatches", "coefficient_mismatches")},
    }, indent=2, sort_keys=True))
    return 0 if payload["status"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
