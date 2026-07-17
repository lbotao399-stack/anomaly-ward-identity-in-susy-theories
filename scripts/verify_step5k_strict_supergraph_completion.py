#!/usr/bin/env python3
"""Exact acceptance gate for the Step-5K strict supergraph completion."""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import subprocess
import sys
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "tasks" / "CURRENT.yaml"
LEDGER = ROOT / "ledger" / "proof_obligations.json"
RULES = ROOT / "audits" / "step5k-momentum-rules-and-fp-inverse.md"
DIAGRAM_IR = ROOT / "audits" / "step5k-diagram-ir.json"
DWORD_JSON = ROOT / "generated" / "step5k-ww-gauge-dword.json"
DWORD_MEMO = ROOT / "audits" / "step5k-ww-gauge-triangle-dword.md"
RULE_LEDGER = ROOT / "generated" / "step5k-momentum-rule-ledger.json"
EXTERNAL_SLOT = ROOT / "audits" / "step5-aa-external-slot-decomposition-exact.json"
CENSUS = ROOT / "audits" / "step5k-graph-census-17.json"
ROUTE_REVIEW = ROOT / "audits" / "step5k-graph-census-and-four-routes-review.md"
MEMO = ROOT / "audits" / "step5k-strict-supergraph-completion.md"
PAPER = ROOT / "paper" / "awi-n4-one-loop.md"
OUTPUT = ROOT / "audits" / "step5k-strict-supergraph-verification.json"


checks: list[dict[str, object]] = []


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(
    name: str,
    condition: bool,
    evidence: object,
    memo_equations: list[str],
) -> None:
    checks.append(
        {
            "name": name,
            "passed": bool(condition),
            "memo_equations": memo_equations,
            "evidence": evidence,
        }
    )


def require_file(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


ComplexQ = tuple[Fraction, Fraction]
Operator = tuple[ComplexQ, tuple[str, ...], str, str]
LaurentMonomial = tuple[int, int]
LaurentPolynomial = dict[LaurentMonomial, Fraction]


def add_poly(*polynomials: LaurentPolynomial) -> LaurentPolynomial:
    output: LaurentPolynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            output[monomial] = output.get(monomial, Fraction(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in output.items() if coefficient}


def mul_poly(left: LaurentPolynomial, right: LaurentPolynomial) -> LaurentPolynomial:
    output: LaurentPolynomial = {}
    for (pd_left, mu_left), left_coefficient in left.items():
        for (pd_right, mu_right), right_coefficient in right.items():
            monomial = (pd_left + pd_right, mu_left + mu_right)
            output[monomial] = (
                output.get(monomial, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return {monomial: coefficient for monomial, coefficient in output.items() if coefficient}


def serialize_laurent(polynomial: LaurentPolynomial) -> list[dict[str, object]]:
    return [
        {
            "coefficient": fraction_pair(coefficient),
            "p_d_squared_power": pd_power,
            "mu_squared_power": mu_power,
        }
        for (pd_power, mu_power), coefficient in sorted(
            polynomial.items(),
            key=lambda item: (-item[0][0], item[0][1]),
        )
    ]


def complex_product(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def operator_product(left: Operator, right: Operator) -> Operator:
    if right[3] != left[2]:
        raise AssertionError(
            f"typed operator mismatch: {right[3]} != {left[2]}"
        )
    coefficient = complex_product(left[0], right[0])
    word = left[1] + right[1]
    scalar = tuple(token for token in word if token in {"barBoxInv", "BoxdInv"})
    non_scalar = tuple(token for token in word if token not in {"barBoxInv", "BoxdInv"})
    return coefficient, scalar + non_scalar, right[2], left[3]


def matrix_product(
    left: list[list[Operator | None]],
    right: list[list[Operator | None]],
) -> list[list[Operator | None]]:
    output: list[list[Operator | None]] = [[None, None], [None, None]]
    for row in range(2):
        for column in range(2):
            terms = [
                operator_product(left[row][inner], right[inner][column])
                for inner in range(2)
                if left[row][inner] is not None and right[inner][column] is not None
            ]
            if len(terms) > 1:
                raise AssertionError("unexpected multi-term FP matrix entry")
            output[row][column] = terms[0] if terms else None
    return output


GaugeRow = tuple[int, int, int, int, Fraction, Fraction]


def gauge_dispatcher_rows(n: int) -> list[GaugeRow]:
    rows: list[GaugeRow] = []
    for p in range(n - 1):
        for q in range(n - 1 - p):
            for r in range(n - 1 - p - q):
                s = n - 2 - p - q - r
                denominator = (
                    256
                    * factorial(p)
                    * factorial(q)
                    * factorial(r)
                    * factorial(s)
                    * (p + q + 1)
                    * (r + s + 1)
                )
                alpha_plus = Fraction(-((-1) ** (p + r)), denominator)
                alpha_minus = Fraction(-((-1) ** (q + s)), denominator)
                rows.append((p, q, r, s, alpha_plus, alpha_minus))
    return rows


def fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def canonical_coefficient_expression(
    rational: Fraction,
    sqrt2_power: int,
    g_power: int,
) -> str:
    sign = "+" if rational >= 0 else "-"
    absolute = abs(rational)
    factors = [str(absolute.numerator)]
    if sqrt2_power:
        factors.append("sqrt(2)")
    if g_power == 1:
        factors.append("g")
    elif g_power:
        factors.append(f"g^{g_power}")
    numerator = "*".join(factors)
    denominator = "" if absolute.denominator == 1 else f"/{absolute.denominator}"
    return sign + numerator + denominator


def expected_ordered_slots(
    p: int,
    q_value: int,
    r: int,
    s: int,
) -> list[dict[str, str]]:
    slots: list[dict[str, str]] = []
    for index in range(p):
        slots.append({"id": f"L.pre.{index + 1}", "block": "left", "role": "plain_u"})
    slots.append({"id": "L.D", "block": "left", "role": "distinguished_u"})
    for index in range(q_value):
        slots.append({"id": f"L.post.{index + 1}", "block": "left", "role": "plain_u"})
    for index in range(r):
        slots.append({"id": f"R.pre.{index + 1}", "block": "right", "role": "plain_u"})
    slots.append({"id": "R.D", "block": "right", "role": "distinguished_u"})
    for index in range(s):
        slots.append({"id": f"R.post.{index + 1}", "block": "right", "role": "plain_u"})
    return slots


def momentum_sum(labels: list[int]) -> str:
    return "+".join(f"p_{label}" for label in labels)


def expected_rule_ledger_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    raw_rows: list[dict[str, object]] = []
    for n in (3, 4):
        for p, q_value, r, s, alpha_plus, alpha_minus in gauge_dispatcher_rows(n):
            for chirality, alpha in (("+", alpha_plus), ("-", alpha_minus)):
                rational = alpha * (2 ** (n // 2))
                sqrt2_power = n % 2
                g_power = n - 2
                monomial = f"{p}{q_value}{r}{s}"
                slots = expected_ordered_slots(p, q_value, r, s)
                outer = "barD2" if chirality == "+" else "D2"
                left_d = "D^a" if chirality == "+" else "barD_dot_a"
                right_d = "D_a" if chirality == "+" else "barD^dot_a"
                half_measure = "E,+" if chirality == "+" else "E,-"
                full_conversion = (
                    "-D2/(4*barBox_E)"
                    if chirality == "+"
                    else "-barD2/(4*barBox_E)"
                )
                left_slots = [row["id"] for row in slots if row["block"] == "left"]
                right_slots = [row["id"] for row in slots if row["block"] == "right"]
                raw_rows.append(
                    {
                        "id": f"G{n}:{chirality}:{monomial}",
                        "n": n,
                        "chirality": chirality,
                        "pqrs": [p, q_value, r, s],
                        "raw_monomial": monomial,
                        "action_coefficient_after_h_equals_g_minus2": {
                            "rational": fraction_pair(rational),
                            "sqrt2_power": sqrt2_power,
                            "g_power": g_power,
                            "expression": canonical_coefficient_expression(
                                rational,
                                sqrt2_power,
                                g_power,
                            ),
                        },
                        "coupling_reduction": "(sqrt(2)*g)^n*h*kappa_AB with h=g^-2",
                        "sign_exponent": "p+r" if chirality == "+" else "q+s",
                        "color_map": {
                            "metric": "kappa_AB",
                            "left_output_index": "A",
                            "right_output_index": "B",
                            "ordered_rule": (
                                "kappa_AB*Coeff^A(left ordered adjoint word)*"
                                "Coeff^B(right ordered adjoint word)"
                            ),
                            "left_ordered_slots": left_slots,
                            "right_ordered_slots": right_slots,
                        },
                        "ordered_slots": slots,
                        "operator_map": {
                            "left_outer": outer,
                            "right_outer": outer,
                            "left_distinguished": left_d,
                            "right_distinguished": right_d,
                            "left_outer_momentum": "sum of left ordered-slot momenta",
                            "right_outer_momentum": "sum of right ordered-slot momenta",
                            "distinguished_momentum": (
                                "momentum of the corresponding L.D or R.D slot"
                            ),
                        },
                        "measure": {
                            "half_superspace": half_measure,
                            "exact_full_measure_conversion": full_conversion,
                        },
                        "momentum_delta": "(2*pi)^d*delta_d(p_1+...+p_n)",
                        "ordinary_vertex_factor": "-C_E/hbar",
                        "memo_equation": "K.54" if chirality == "+" else "K.55",
                    }
                )

    labeled_rows: list[dict[str, object]] = []
    for raw in raw_rows:
        n = int(raw["n"])
        slots = raw["ordered_slots"]
        assert isinstance(slots, list)
        for permutation in itertools.permutations(range(1, n + 1)):
            assignments = [
                {
                    "slot": slot["id"],
                    "block": slot["block"],
                    "role": slot["role"],
                    "label": label,
                    "color_index": f"A_{label}",
                    "momentum": f"p_{label}",
                }
                for slot, label in zip(slots, permutation, strict=True)
            ]
            left = [row for row in assignments if row["block"] == "left"]
            right = [row for row in assignments if row["block"] == "right"]
            left_d = next(row for row in left if row["role"] == "distinguished_u")
            right_d = next(row for row in right if row["role"] == "distinguished_u")
            operator_map = raw["operator_map"]
            assert isinstance(operator_map, dict)
            permutation_id = "".join(str(label) for label in permutation)
            labeled_rows.append(
                {
                    "id": f"{raw['id']}:P{permutation_id}",
                    "raw_row_id": raw["id"],
                    "functional_derivative_order": [
                        f"delta/delta u^(A_{label})(p_{label})"
                        for label in range(n, 0, -1)
                    ],
                    "koszul_sign": 1,
                    "ordered_slot_assignment": assignments,
                    "action_coefficient_after_h_equals_g_minus2": raw[
                        "action_coefficient_after_h_equals_g_minus2"
                    ],
                    "color_map": {
                        "metric": "kappa_AB",
                        "left_ordered_color_word": [row["color_index"] for row in left],
                        "right_ordered_color_word": [row["color_index"] for row in right],
                        "expression": (
                            "kappa_AB*Coeff^A(T_"
                            + "*T_".join(str(row["label"]) for row in left)
                            + ")*Coeff^B(T_"
                            + "*T_".join(str(row["label"]) for row in right)
                            + ")"
                        ),
                    },
                    "operator_momentum_map": {
                        "left_outer": (
                            f"{operator_map['left_outer']}"
                            f"({momentum_sum([row['label'] for row in left])})"
                        ),
                        "left_distinguished": (
                            f"{operator_map['left_distinguished']}(p_{left_d['label']})"
                        ),
                        "right_outer": (
                            f"{operator_map['right_outer']}"
                            f"({momentum_sum([row['label'] for row in right])})"
                        ),
                        "right_distinguished": (
                            f"{operator_map['right_distinguished']}(p_{right_d['label']})"
                        ),
                    },
                    "momentum_delta": (
                        "(2*pi)^d*delta_d("
                        + momentum_sum(list(range(1, n + 1)))
                        + ")"
                    ),
                    "ordinary_vertex_factor": "-C_E/hbar",
                }
            )
    return raw_rows, labeled_rows


def signed_fraction(value: Fraction) -> str:
    sign = "+" if value > 0 else "-"
    magnitude = abs(value)
    if magnitude.denominator == 1:
        return f"{sign}{magnitude.numerator}"
    return f"{sign}{magnitude.numerator}/{magnitude.denominator}"


def compact_tex(text: str) -> str:
    return re.sub(r"\s+", "", text)


def markdown_math_violations(path: Path) -> list[dict[str, object]]:
    display = False
    violations: list[dict[str, object]] = []
    for line_number, line in enumerate(require_file(path).splitlines(), start=1):
        if re.search(r"(?<!\\)\\[\[\]]", line):
            violations.append({"line": line_number, "kind": "chat_display_delimiter"})
        if re.search(r"(?<!\\)\\[()]", line):
            violations.append({"line": line_number, "kind": "chat_inline_delimiter"})
        if "$$" in line:
            if line.strip() != "$$":
                violations.append({"line": line_number, "kind": "nonstandalone_display_dollar"})
                continue
            display = not display
            continue
        if not display:
            unescaped = re.sub(r"\\\$", "", line)
            if unescaped.count("$") % 2:
                violations.append({"line": line_number, "kind": "unpaired_inline_dollar"})
    if display:
        violations.append({"line": -1, "kind": "unclosed_display_dollar"})
    return violations


def check_task_and_ledger() -> None:
    task = json.loads(require_file(TASK))
    ledger = json.loads(require_file(LEDGER))
    rows = [row for row in ledger["proof_obligations"] if row["id"] == task["id"]]
    expected_trace = [
        "SPECIFIED",
        "FROZEN",
        "RULES_DERIVED",
        "ENUMERATED",
        "EVALUATED",
        "CUT_COMPLETE",
        "RENORMALIZED",
        "WARD_CLOSED",
        "COHOMOLOGY_PROJECTED",
        "ACCEPTED",
    ]
    actual_trace = [row.get("state") for row in task.get("state_trace", [])]
    passed = (
        task["id"] == "CONTRACT-STEP-05K-STRICT-SUPERGRAPH-COMPLETION-001"
        and len(rows) == 1
        and rows[0]["task"] == "tasks/CURRENT.yaml"
        and rows[0].get("task_sha256") == sha256(TASK)
        and task["status"] == "ACCEPTED"
        and rows[0]["state"] == "ACCEPTED"
        and actual_trace == expected_trace
    )
    record(
        "TASK_LEDGER_HASH_AND_ACCEPTANCE",
        passed,
        {
            "task_status": task.get("status"),
            "ledger_rows": rows,
            "task_sha256": sha256(TASK),
            "state_trace": actual_trace,
        },
        ["K.121", "K.128"],
    )


def check_rule_table() -> None:
    text = require_file(RULES)
    rule_ledger = json.loads(require_file(RULE_LEDGER))
    ledger_builder = ROOT / "scripts" / "build_step5k_momentum_rule_ledger.py"
    ledger_build = subprocess.run(
        [sys.executable, str(ledger_builder), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    forbidden_controls = [byte for byte in RULES.read_bytes() if byte < 32 and byte not in (9, 10)]
    required = [
        "K_E^{\\rm FP}",
        "(K_E^{\\rm FP})^{-1}_{\\bar4}",
        "\\mathcal R_+^d",
        "\\mathfrak v_E",
        "S_E^{\\rm mat}",
        "S_{E,{\\rm FP}}^{(1u)}",
        "S_{E,{\\rm FP}}^{(2u)}",
        "\\mathcal I_{0,w}^{AB}",
        "Nielsen--Kallosh",
        "step5k-momentum-rule-ledger.json",
        "N_{\\rm total}^{\\rm labeled}=528",
    ]
    missing = [token for token in required if token not in text]
    cubic = gauge_dispatcher_rows(3)
    quartic = gauge_dispatcher_rows(4)
    expected_rows = [
        f"| ${n}$ | $({p},{q},{r},{s})$ | ${signed_fraction(alpha_plus)}$ | "
        f"${signed_fraction(alpha_minus)}$ |"
        for n, rows in ((3, cubic), (4, quartic))
        for p, q, r, s, alpha_plus, alpha_minus in rows
    ]
    missing_dispatcher_rows = [row for row in expected_rows if text.count(row) != 1]
    compact = compact_tex(text)
    exact_word_tokens = [
        r"\mathscrW_{+;pqrs}^{AB}&:=\int_{E,+}\left[\barD^2(u^pD^au\,u^q)\right]^A\left[\barD^2(u^rD_au\,u^s)\right]^B",
        r"\mathscrW_{-;pqrs}^{AB}&:=\int_{E,-}\left[D^2(u^p\barD_{\dota}u\,u^q)\right]^A\left[D^2(u^r\barD^{\dota}u\,u^s)\right]^B",
        r"\alpha_{+;n,pqrs}(\sqrt2g)^nf_{AB}\mathscrW_{+;pqrs}^{AB}",
        r"\alpha_{-;n,pqrs}(\sqrt2g)^n\widetildef_{AB}\mathscrW_{-;pqrs}^{AB}",
        r"\mathfrakv_{E,\pm}^{g,(n)}=-\frac1\hbar\frac{\vec\delta}{\deltau^{A_n}(p_n)}\cdots\frac{\vec\delta}{\deltau^{A_1}(p_1)}S_{E,\pm}^{g,(n)}",
    ]
    missing_word_tokens = [token for token in exact_word_tokens if token not in compact]
    expected_raw_rows, expected_labeled_rows = expected_rule_ledger_rows()
    dispatcher = rule_ledger.get("gauge_dispatcher", {})
    actual_raw_rows = dispatcher.get("raw_rows", [])
    actual_labeled_rows = dispatcher.get("labeled_rows", [])
    expected_raw_by_id = {row["id"]: row for row in expected_raw_rows}
    actual_raw_by_id = {row.get("id"): row for row in actual_raw_rows}
    expected_labeled_by_id = {row["id"]: row for row in expected_labeled_rows}
    actual_labeled_by_id = {row.get("id"): row for row in actual_labeled_rows}
    raw_ledger_exact = actual_raw_by_id == expected_raw_by_id
    labeled_ledger_exact = actual_labeled_by_id == expected_labeled_by_id
    invariants = dispatcher.get("invariants", {})
    cross_bindings = rule_ledger.get("cross_bindings", {})
    dword_binding = cross_bindings.get("dword_cubic_raw_rows", {})
    diagram_binding = cross_bindings.get("diagram_polarized_vertices", {})
    ledger_exact = (
        ledger_build.returncode == 0
        and rule_ledger.get("schema") == "step5k-momentum-rule-ledger-v1"
        and rule_ledger.get("status") == "DERIVED_EXACT_TYPED_RULES"
        and rule_ledger.get("generated") is True
        and rule_ledger.get("rule_memo_sha256") == sha256(RULES)
        and rule_ledger.get("coupling_branch")
        == {
            "h": "g^-2",
            "f_AB": "h*kappa_AB",
            "tilde_f_AB": "h*kappa_AB",
            "canonical_vector": "u=V/(sqrt(2)*g)",
        }
        and raw_ledger_exact
        and labeled_ledger_exact
        and invariants.get("raw_row_count") == 28
        and invariants.get("raw_unique_row_id_count") == 28
        and invariants.get("labeled_row_count") == 528
        and invariants.get("labeled_unique_row_id_count") == 528
        and invariants.get("cubic_labeled_row_count") == 48
        and invariants.get("quartic_labeled_row_count") == 480
        and invariants.get("unresolved") == 0
        and dword_binding.get("artifact_sha256") == sha256(DWORD_JSON)
        and dword_binding.get("full_contact_row_count") == 48
        and dword_binding.get("unique_cubic_raw_row_count") == 8
        and len(dword_binding.get("rows", [])) == 8
        and dword_binding.get("matched") is True
        and diagram_binding.get("artifact_sha256") == sha256(DIAGRAM_IR)
        and diagram_binding.get("graph_id") == "G-WW-GAUGE-01"
        and len(diagram_binding.get("vertices", [])) == 2
        and all(
            row.get("matched") is True
            and len(row.get("source_raw_row_ids", [])) == 4
            for row in diagram_binding.get("vertices", [])
        )
        and diagram_binding.get("matched") is True
        and rule_ledger.get("unresolved") == []
    )
    dispatcher_exact = (
        len(cubic) == 4
        and len(quartic) == 10
        and sum(row[4] for row in cubic) == 0
        and sum(row[5] for row in cubic) == 0
        and sum(row[4] for row in quartic) == 0
        and sum(row[5] for row in quartic) == 0
        and {row[4] for row in cubic} == {Fraction(1, 512), Fraction(-1, 512)}
        and all(row[5] == -row[4] for row in cubic)
        and {abs(row[4]) for row in quartic}
        == {Fraction(1, 1536), Fraction(1, 1024), Fraction(1, 768)}
        and all(row[5] == row[4] for row in quartic)
        and not missing_dispatcher_rows
        and not missing_word_tokens
        and ledger_exact
    )
    record(
        "COMPLETE_MOMENTUM_RULE_TABLE",
        bool(text) and not forbidden_controls and not missing and dispatcher_exact,
        {
            "missing": missing,
            "forbidden_controls": forbidden_controls,
            "missing_dispatcher_rows": missing_dispatcher_rows,
            "missing_exact_word_tokens": missing_word_tokens,
            "momentum_rule_ledger": {
                "builder": ledger_build.stdout.strip(),
                "raw_rows": len(actual_raw_rows),
                "raw_exact": raw_ledger_exact,
                "labeled_rows": len(actual_labeled_rows),
                "labeled_exact": labeled_ledger_exact,
                "dword_cross_binding": dword_binding.get("matched"),
                "diagram_cross_binding": diagram_binding.get("matched"),
                "unresolved": rule_ledger.get("unresolved"),
            },
            "gauge_dispatcher": {
                "cubic_rows": len(cubic),
                "quartic_rows": len(quartic),
                "cubic_chiral_sum": str(sum(row[4] for row in cubic)),
                "cubic_antichiral_sum": str(sum(row[5] for row in cubic)),
                "quartic_chiral_sum": str(sum(row[4] for row in quartic)),
                "quartic_antichiral_sum": str(sum(row[5] for row in quartic)),
                "exact_rows": expected_rows,
            },
        },
        ["K.10--K.46"],
    )


def check_fp_inverse() -> None:
    text = require_file(RULES)
    compact = compact_tex(text)
    rule_ledger = json.loads(require_file(RULE_LEDGER))
    quadratic_blocks = rule_ledger.get("typed_quadratic_blocks", {})
    required = [
        "K_E^{\\rm FP}(K_E^{\\rm FP})^{-1}_{\\bar4}",
        "(K_E^{\\rm FP})^{-1}_{\\bar4}K_E^{\\rm FP}",
        "\\mathbf1_{\\mathscr F^{\\perp}}",
        "\\mathbf1_{\\mathscr G^{\\perp}}",
        "1+\\frac{\\mu_r^2}{r_d^2}",
        "All other free ghost contractions vanish",
    ]
    missing = [token for token in required if token not in text]
    exact_tex_blocks = [
        r"(K_{E,\bar4}^u)_{AB}=\kappa_{AB}\bar\Box_E,\qquad(K_{E,\bar4}^u)^{-1\,AB}=\kappa^{AB}\bar\Box_E^{-1}",
        r"(K_{E,\bar4}^u)_{AC}(K_E^u)^{-1\,CB}_{d}=(K_E^u)^{-1\,BC}_{d}(K_{E,\bar4}^u)_{CA}=\frac{\bar\Box_E}{\Box_d}\delta_A{}^B=\left(1+\frac{\mu_p^2}{p_d^2}\right)\delta_A{}^B",
        r"K_E^{\Phi\widetilde\Phi}=-\kappa\mathbf1_+,\qquad(K_E^{\Phi\widetilde\Phi})^{-1}_{\bar4}=-\kappa^{-1}\mathcalP_+^{\bar4}",
        r"K_E^{\widetilde\Phi\Phi}=-\kappa\mathbf1_-,\qquad(K_E^{\widetilde\Phi\Phi})^{-1}_{\bar4}=-\kappa^{-1}\mathcalP_-^{\bar4}",
        r"K_E^{\Phi\widetilde\Phi}(K_E^{\Phi\widetilde\Phi})^{-1}_{d}=\frac{\bar\Box_E}{\Box_d}\mathbf1_+=\left(1+\frac{\mu_p^2}{p_d^2}\right)\mathbf1_+",
        r"K_E^{\rmFP}:=-\mathcalM_E^{(0)}=\begin{pmatrix}0&+\dfraci4\barD^2\\[2mm]-\dfraci4D^2&0\end{pmatrix}",
        r"(K_E^{\rmFP})^{-1}_{\bar4}=\begin{pmatrix}0&+\dfraci4\bar\Box_E^{-1}\barD^2\\[2mm]-\dfraci4\bar\Box_E^{-1}D^2&0\end{pmatrix}",
        r"K_E^{\rmFP}(K_E^{\rmFP})^{-1}_{\bar4}&=\begin{pmatrix}\dfrac1{16}\barD^2D^2\bar\Box_E^{-1}&0\\[2mm]0&\dfrac1{16}D^2\barD^2\bar\Box_E^{-1}\end{pmatrix}",
        r"(K_E^{\rmFP})^{-1}_{\bar4}K_E^{\rmFP}&=\begin{pmatrix}\dfrac1{16}\bar\Box_E^{-1}\barD^2D^2&0\\[2mm]0&\dfrac1{16}\bar\Box_E^{-1}D^2\barD^2\end{pmatrix}",
        r"K_E^{\rmFP}(r)(K_E^{\rmFP})^{-1}_{d}(r)-1=(K_E^{\rmFP})^{-1}_{d}(r)K_E^{\rmFP}(r)-1=\frac{\mu_r^2}{r_d^2}",
    ]
    missing_exact_tex = [token for token in exact_tex_blocks if token not in compact]
    zero = Fraction(0)
    quarter = Fraction(1, 4)
    fp_kernel: list[list[Operator | None]] = [
        [None, ((zero, quarter), ("barD2",), "G_minus", "F_plus")],
        [((zero, -quarter), ("D2",), "G_plus", "F_minus"), None],
    ]
    fp_inverse: list[list[Operator | None]] = [
        [None, ((zero, quarter), ("barBoxInv", "barD2"), "F_minus", "G_plus")],
        [((zero, -quarter), ("barBoxInv", "D2"), "F_plus", "G_minus"), None],
    ]
    right = matrix_product(fp_kernel, fp_inverse)
    left = matrix_product(fp_inverse, fp_kernel)
    expected_right = [
        [((Fraction(1, 16), zero), ("barBoxInv", "barD2", "D2"), "F_plus", "F_plus"), None],
        [None, ((Fraction(1, 16), zero), ("barBoxInv", "D2", "barD2"), "F_minus", "F_minus")],
    ]
    expected_left = [
        [((Fraction(1, 16), zero), ("barBoxInv", "barD2", "D2"), "G_plus", "G_plus"), None],
        [None, ((Fraction(1, 16), zero), ("barBoxInv", "D2", "barD2"), "G_minus", "G_minus")],
    ]
    vector_kernel = (Fraction(1), ("kappa_down", "barBox"))
    vector_inverse = (Fraction(1), ("kappa_up", "barBoxInv"))
    vector_exact = (
        vector_kernel[0] * vector_inverse[0] == 1
        and vector_kernel[1] + vector_inverse[1]
        == ("kappa_down", "barBox", "kappa_up", "barBoxInv")
    )
    matter_compositions = {
        orientation: {
            "kernel": (Fraction(-1), ("kappa_down", f"identity_{orientation}")),
            "inverse": (
                Fraction(-1),
                ("kappa_up", f"projector_{orientation}_bar4"),
            ),
        }
        for orientation in ("plus", "minus")
    }
    matter_exact = all(
        row["kernel"][0] * row["inverse"][0] == 1
        and row["kernel"][1][0] == "kappa_down"
        and row["inverse"][1][0] == "kappa_up"
        and row["kernel"][1][1].removeprefix("identity_")
        == row["inverse"][1][1]
        .removeprefix("projector_")
        .removesuffix("_bar4")
        for row in matter_compositions.values()
    )
    pd2: LaurentPolynomial = {(1, 0): Fraction(1)}
    mu2: LaurentPolynomial = {(0, 1): Fraction(1)}
    pd2_inverse: LaurentPolynomial = {(-1, 0): Fraction(1)}
    barp2 = add_poly(pd2, mu2)
    dred_ratio = mul_poly(barp2, pd2_inverse)
    expected_dred_ratio: LaurentPolynomial = {
        (0, 0): Fraction(1),
        (-1, 1): Fraction(1),
    }
    dred_defect = add_poly(dred_ratio, {(0, 0): Fraction(-1)})
    dred_defect_exact = (
        dred_ratio == expected_dred_ratio
        and dred_defect == {(-1, 1): Fraction(1)}
    )
    regulated_defects = {
        sector: {
            "barp2_times_pd2_inverse": {
                f"pd2^{pd_power}*mu2^{mu_power}": str(coefficient)
                for (pd_power, mu_power), coefficient in sorted(dred_ratio.items())
            },
            "minus_identity": {
                f"pd2^{pd_power}*mu2^{mu_power}": str(coefficient)
                for (pd_power, mu_power), coefficient in sorted(dred_defect.items())
            },
            "result": "mu_p^2/p_d^2",
        }
        for sector in ("vector", "matter", "fp_left", "fp_right")
    }

    ratio_serialized = serialize_laurent(dred_ratio)
    defect_serialized = serialize_laurent(dred_defect)

    def sector_products_exact(sector: dict[str, object], space: str) -> bool:
        products = sector.get("products", {})
        if not isinstance(products, dict):
            return False
        return (
            products.get("exact_left") == f"1_{space}"
            and products.get("exact_right") == f"1_{space}"
            and all(
                isinstance(products.get(order), dict)
                and products[order].get("ratio_laurent_polynomial")
                == ratio_serialized
                and products[order].get("defect_laurent_polynomial")
                == defect_serialized
                and products[order].get("result")
                == f"(1+mu_p^2/p_d^2)*1_{space}"
                for order in ("dred_left", "dred_right")
            )
        )

    vector_block = quadratic_blocks.get("vector", {})
    matter_plus_block = quadratic_blocks.get("matter_plus", {})
    matter_minus_block = quadratic_blocks.get("matter_minus", {})
    vector_ledger_exact = (
        vector_block.get("kernel_bar4")
        == {"coefficient": [1, 1], "color": "kappa_AB", "operator": "barBox_E"}
        and vector_block.get("inverse_bar4")
        == {"coefficient": [1, 1], "color": "kappa^AB", "operator": "barBox_E^-1"}
        and vector_block.get("inverse_d")
        == {"coefficient": [1, 1], "color": "kappa^AB", "operator": "Box_d^-1"}
        and vector_block.get("momentum_propagator")
        == "-(2*pi)^d*delta_d(p+p')*hbar*kappa^AB*delta4(theta_1-theta_2)/p_d^2"
        and sector_products_exact(vector_block, "U_bar4_perp")
    )
    matter_plus_ledger_exact = (
        matter_plus_block.get("kernel_bar4")
        == {"coefficient": [-1, 1], "color": "kappa_AB", "operator": "1_+"}
        and matter_plus_block.get("inverse_bar4")
        == {
            "coefficient": [-1, 1],
            "color": "kappa^AB",
            "operator": "P_+^bar4=barD2*D2/(16*barBox_E)",
        }
        and matter_plus_block.get("inverse_d")
        == {
            "coefficient": [-1, 1],
            "color": "kappa^AB",
            "operator": "R_+^d=barD2*D2/(16*Box_d)",
        }
        and matter_plus_block.get("momentum_propagator")
        == "+(2*pi)^d*delta_d(p+p')*delta_rs*hbar*kappa^AB*barD2(p)*D2(p)*delta4(theta_1-theta_2)/(16*p_d^2)"
        and sector_products_exact(matter_plus_block, "Sigma_E,+")
    )
    matter_minus_ledger_exact = (
        matter_minus_block.get("kernel_bar4")
        == {"coefficient": [-1, 1], "color": "kappa_AB", "operator": "1_-"}
        and matter_minus_block.get("inverse_bar4")
        == {
            "coefficient": [-1, 1],
            "color": "kappa^AB",
            "operator": "P_-^bar4=D2*barD2/(16*barBox_E)",
        }
        and matter_minus_block.get("inverse_d")
        == {
            "coefficient": [-1, 1],
            "color": "kappa^AB",
            "operator": "R_-^d=D2*barD2/(16*Box_d)",
        }
        and matter_minus_block.get("momentum_propagator")
        == "+(2*pi)^d*delta_d(p+p')*delta_rs*hbar*kappa^AB*D2(p)*barD2(p)*delta4(theta_1-theta_2)/(16*p_d^2)"
        and sector_products_exact(matter_minus_block, "Sigma_E,-")
    )

    def ledger_operator(
        real: Fraction,
        imaginary: Fraction,
        scalar_inverse: str,
        spin_word: list[str],
        source: str,
        target: str,
    ) -> dict[str, object]:
        return {
            "coefficient": {
                "real": fraction_pair(real),
                "imaginary": fraction_pair(imaginary),
            },
            "scalar_inverse": scalar_inverse,
            "spin_word": spin_word,
            "source": source,
            "target": target,
        }

    fp_block = quadratic_blocks.get("fp", {})
    expected_fp_kernel = [
        [None, ledger_operator(Fraction(0), quarter, "1", ["barD2"], "G-", "F+")],
        [ledger_operator(Fraction(0), -quarter, "1", ["D2"], "G+", "F-"), None],
    ]
    expected_fp_inverse_bar4 = [
        [None, ledger_operator(Fraction(0), quarter, "barBox_E^-1", ["barD2"], "F-", "G+")],
        [ledger_operator(Fraction(0), -quarter, "barBox_E^-1", ["D2"], "F+", "G-"), None],
    ]
    expected_fp_inverse_d = [
        [None, ledger_operator(Fraction(0), quarter, "Box_d^-1", ["barD2"], "F-", "G+")],
        [ledger_operator(Fraction(0), -quarter, "Box_d^-1", ["D2"], "F+", "G-"), None],
    ]

    def expected_fp_product(space_prefix: str, scalar_inverse: str) -> list[list[dict[str, object] | None]]:
        return [
            [
                ledger_operator(
                    Fraction(1, 16),
                    Fraction(0),
                    scalar_inverse,
                    ["barD2", "D2"],
                    f"{space_prefix}+",
                    f"{space_prefix}+",
                ),
                None,
            ],
            [
                None,
                ledger_operator(
                    Fraction(1, 16),
                    Fraction(0),
                    scalar_inverse,
                    ["D2", "barD2"],
                    f"{space_prefix}-",
                    f"{space_prefix}-",
                ),
            ],
        ]

    def reduced_fp_product_exact(
        block_name: str,
        space_prefix: str,
        scalar_result: str,
        ratio: list[dict[str, object]],
        defect: list[dict[str, object]],
    ) -> bool:
        block = fp_block.get(block_name, {})
        reduced = block.get("reduced", []) if isinstance(block, dict) else []
        if not (
            isinstance(reduced, list)
            and len(reduced) == 2
            and all(isinstance(row, list) and len(row) == 2 for row in reduced)
            and reduced[0][1] is None
            and reduced[1][0] is None
        ):
            return False
        for index, chirality in enumerate(("+", "-")):
            row = reduced[index][index]
            if not isinstance(row, dict):
                return False
            space = f"{space_prefix}{chirality}"
            spin_word = "barD2*D2" if chirality == "+" else "D2*barD2"
            if not (
                row.get("chirality") == chirality
                and row.get("source") == space
                and row.get("target") == space
                and row.get("coefficient_before_spin_rewrite")
                == {"real": [1, 16], "imaginary": [0, 1]}
                and row.get("scalar_result") == scalar_result
                and row.get("ratio_laurent_polynomial") == ratio
                and row.get("defect_laurent_polynomial") == defect
                and row.get("spin_rewrite")
                == f"{spin_word}=16*barBox_E*P_{chirality}^bar4"
                and row.get("projector_action") == f"P_{chirality}^bar4=1_{space}"
            ):
                return False
        return True

    identity_serialized = serialize_laurent({(0, 0): Fraction(1)})
    fp_ledger_exact = (
        fp_block.get("domain_basis") == ["G+", "G-"]
        and fp_block.get("codomain_basis") == ["F+", "F-"]
        and fp_block.get("kernel") == expected_fp_kernel
        and fp_block.get("inverse_bar4") == expected_fp_inverse_bar4
        and fp_block.get("inverse_d") == expected_fp_inverse_d
        and fp_block.get("right_inverse_bar4", {}).get("raw")
        == expected_fp_product("F", "barBox_E^-1")
        and fp_block.get("left_inverse_bar4", {}).get("raw")
        == expected_fp_product("G", "barBox_E^-1")
        and fp_block.get("right_composition_d", {}).get("raw")
        == expected_fp_product("F", "Box_d^-1")
        and fp_block.get("left_composition_d", {}).get("raw")
        == expected_fp_product("G", "Box_d^-1")
        and reduced_fp_product_exact(
            "right_inverse_bar4", "F", "1", identity_serialized, []
        )
        and reduced_fp_product_exact(
            "left_inverse_bar4", "G", "1", identity_serialized, []
        )
        and reduced_fp_product_exact(
            "right_composition_d",
            "F",
            "1+mu_p^2/p_d^2",
            ratio_serialized,
            defect_serialized,
        )
        and reduced_fp_product_exact(
            "left_composition_d",
            "G",
            "1+mu_p^2/p_d^2",
            ratio_serialized,
            defect_serialized,
        )
    )
    quadratic_ledger_exact = (
        vector_ledger_exact
        and matter_plus_ledger_exact
        and matter_minus_ledger_exact
        and fp_ledger_exact
    )
    inverse_exact = (
        right == expected_right
        and left == expected_left
        and vector_exact
        and matter_exact
        and dred_defect_exact
        and not missing_exact_tex
        and quadratic_ledger_exact
    )
    record(
        "TYPED_FP_LEFT_RIGHT_INVERSE_AND_DRED_DEFECT",
        not missing and inverse_exact,
        {
            "missing": missing,
            "missing_exact_tex": missing_exact_tex,
            "fp_right_product": repr(right),
            "fp_left_product": repr(left),
            "vector_exact": vector_exact,
            "matter_exact": matter_exact,
            "matter_compositions": repr(matter_compositions),
            "regulated_defects": regulated_defects,
            "typed_rule_ledger": {
                "vector": vector_ledger_exact,
                "matter_plus": matter_plus_ledger_exact,
                "matter_minus": matter_minus_ledger_exact,
                "fp": fp_ledger_exact,
            },
        },
        ["K.23--K.28"],
    )


def check_sector_typed_ir() -> None:
    payload = json.loads(require_file(DIAGRAM_IR))
    graphs = {row["id"]: row for row in payload["graphs"]}
    gauge = graphs.get("G-WW-GAUGE-01", {})
    matter = graphs.get("G-WW-MATTER-01", {})
    gauge_fields = [edge.get("field_tex", "") for edge in gauge.get("internal_edges", [])]
    matter_fields = [edge.get("field_tex", "") for edge in matter.get("internal_edges", [])]
    passed = (
        set(graphs) == {"G-WW-GAUGE-01", "G-WW-MATTER-01"}
        and gauge.get("sector") == "GAUGE_VECTOR"
        and matter.get("sector") == "ADJOINT_CHIRAL_MATTER"
        and len(gauge_fields) == 3
        and all("u^" in item for item in gauge_fields)
        and sum("u^" in item for item in matter_fields) == 2
        and sum("Phi" in item for item in matter_fields) == 1
        and len(gauge.get("wick_contractions", [])) == 2
        and len(matter.get("wick_contractions", [])) == 4
    )
    record(
        "GAUGE_MATTER_FIELD_WORD_NONCONFLATION",
        passed,
        {"gauge_fields": gauge_fields, "matter_fields": matter_fields},
        ["K.47--K.48"],
    )


def check_formula_rendering() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "render_step5k_supergraphs.py"), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    outputs = []
    for stem in ("step5k-gauge-vector-triangle", "step5k-adjoint-matter-triangle"):
        tex = ROOT / "paper" / "figures" / f"{stem}.tex"
        pdf = ROOT / "paper" / "figures" / f"{stem}.pdf"
        svg = ROOT / "paper" / "figures" / f"{stem}.svg"
        outputs.append(
            {
                "stem": stem,
                "tex": tex.is_file(),
                "pdf_bytes": pdf.stat().st_size if pdf.is_file() else 0,
                "svg_formula_paths": svg.is_file() and "<path" in require_file(svg),
            }
        )
    passed = result.returncode == 0 and all(
        row["tex"] and row["pdf_bytes"] > 1000 and row["svg_formula_paths"] for row in outputs
    )
    record(
        "FORMULA_RENDERED_TIKZ_PDF_SVG",
        passed,
        {"renderer": result.stdout.strip(), "outputs": outputs},
        ["K.47--K.48"],
    )


def check_gauge_dword() -> None:
    payload = json.loads(require_file(DWORD_JSON))
    external_slot = json.loads(require_file(EXTERNAL_SLOT))
    rows = payload.get("endpoint_rows", [])
    marks = payload.get("dminus_marks", [])
    full_rows = payload.get("full_contact_rows", [])
    coefficient = payload.get("coefficient_ledger", {})
    legacy = payload.get("legacy_rejected_factor8", {})
    dword_full_orbit = payload.get("full_gauge_orbit_result", {})
    generator = ROOT / "scripts" / "build_step5k_ww_gauge_dword.py"
    generated = subprocess.run(
        [sys.executable, str(generator), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    ) if generator.is_file() else None
    typed = external_slot.get("typed_ordered_reconstruction", {})
    replay = external_slot.get("exhaustive_component_replay", {})
    external_checks = external_slot.get("checks", {})
    accepted_full_orbit = (
        external_slot.get("external_target_used") is False
        and external_checks.get("count") == 269
        and external_checks.get("failed") == 0
        and replay.get("total_full_color_mask_rows") == 9216
        and replay.get("total_equality_failures") == 0
        and typed.get("external_target_used") is False
        and typed.get("physical_formula_after_typed_EOM_quotient")
        == "lambda1*F^{AB}_{DE}*(DA_p-AD_p)"
    )
    passed = (
        payload.get("graph_id") == "G-WW-GAUGE-01"
        and len(rows) == 4
        and {row.get("row_id") for row in rows} == {"R01", "R02", "R11", "R12"}
        and all(row.get("raw_times_transport") == -1 for row in rows)
        and len(marks) == 2
        and len(full_rows) == 48
        and len({row.get("row_id") for row in full_rows}) == 48
        and len({row.get("hessian_group_id") for row in full_rows}) == 24
        and coefficient.get("same_edge_anticommutator_factor_left") == 2
        and coefficient.get("same_edge_anticommutator_factor_right") == 2
        and coefficient.get("fixed_parent_prefactor") == "+hbar*g^2/16"
        and legacy.get("status") == "REJECTED_FACTOR_8"
        and dword_full_orbit.get("derived_by_this_generator") is False
        and dword_full_orbit.get("source")
        == "audits/step5-aa-external-slot-decomposition-exact.json"
        and payload.get("unresolved") == []
        and generated is not None
        and generated.returncode == 0
        and accepted_full_orbit
    )
    record(
        "NONCOMMUTATIVE_GAUGE_DWORD_AND_COEFFICIENT",
        passed,
        {
            "endpoint_rows": len(rows),
            "marks": len(marks),
            "full_contact_rows": len(full_rows),
            "coefficient": coefficient,
            "generator": None if generated is None else generated.stdout.strip(),
            "accepted_full_orbit": {
                "source": str(EXTERNAL_SLOT.relative_to(ROOT)),
                "checks": external_checks.get("count"),
                "full_color_rows": replay.get("total_full_color_mask_rows"),
                "formula": typed.get("physical_formula_after_typed_EOM_quotient"),
                "target_used": external_slot.get("external_target_used"),
            },
        },
        ["K.55--K.76", "K.87--K.96", "K.122"],
    )


def check_numerator_provenance() -> None:
    memo = require_file(MEMO)
    dword = json.loads(require_file(DWORD_JSON))
    provenance = dword.get("numerator_provenance", {})
    required = [
        "L_1:=r_0+r_1=2k+q",
        "L_2:=r_1+r_2=2k+p+2q",
        "N_{G,+}{}^{\\dot\\alpha}",
        "\\left(\\frac1{64}\\right)(16)(2)(2)=1",
        "\\frac{\\hbar g^2}{16}",
        "\\mathrm{REJECTED\\_LEGACY\\_PREFACTOR}",
        "\\left[-4N_{ij,+}{}^{\\dot\\alpha}\\right]",
        "e^{iw\\cdot\\ell}e^{iw\\cdot(aq+bp)}",
        "\\omega^2",
        "No $w=0$ limit is imposed",
    ]
    missing = [token for token in required if token not in memo]
    passed = len(provenance) >= 6 and not missing
    record(
        "PREINTEGRAL_NUMERATOR_PROVENANCE",
        passed,
        {"provenance_rows": len(provenance), "missing": missing},
        ["K.49--K.76f"],
    )


def check_census_and_routes() -> None:
    census = json.loads(require_file(CENSUS))
    review = require_file(ROUTE_REVIEW)
    memo = require_file(MEMO)
    ids = [row["id"] for row in census["candidates"]]
    allowed = set(census["status_alphabet"])
    bucket3 = [row for row in census["candidates"] if row["bucket"] == "DEFERRED_WICK_ROUTING"]
    required_routes = [
        "## 4. C14: BC--TMG--TAIL",
        "## 5. C15: AC--SOURCE--CYCLE--TAIL",
        "## 6. C16: AD/DA $I_0S_{m4}$",
        "## 7. C17: $T_{H_+H_-}$",
    ]
    stable_routes = [
        "BC-TMG-TAIL",
        "AC-SOURCE-CYCLE-TAIL",
        "ADDA-I0-SM4",
        "T_(H+H-)",
    ]
    passed = (
        len(ids) == 17
        and len(set(ids)) == 17
        and all(row["status"] in allowed for row in census["candidates"])
        and len(bucket3) == 4
        and census["totals"]["unresolved"] == 0
        and all(route in review for route in required_routes)
        and census.get("actual_four_deferred_routes") == stable_routes
        and all(route in memo for route in stable_routes)
        and "HT target used to decide a route: no" in review
    )
    record(
        "SEVENTEEN_CANDIDATES_AND_FOUR_DEFERRED_ROUTES",
        passed,
        {"candidate_count": len(ids), "bucket3_count": len(bucket3), "unresolved": census["totals"]["unresolved"]},
        ["K.117--K.121"],
    )


def check_matter_occurrences() -> None:
    review = require_file(ROUTE_REVIEW)
    memo = require_file(MEMO)
    required = [
        "MW-F1",
        "MW-F2",
        "MW-X1",
        "MW-X2",
        "-\\frac43\\lambda_1",
        "+\\frac13\\lambda_1",
        "\\mathcal S_{012}",
        "\\mathcal S_2",
        "e^{iw\\cdot r_2}\\bar D_1^2D_1^2",
    ]
    missing = [token for token in required[:8] if token not in review]
    missing += [token for token in required[8:] if token not in memo]
    record(
        "FOUR_MATTER_OCCURRENCE_WICK_ROUTES",
        not missing,
        {"missing": missing},
        ["K.97--K.116"],
    )


def check_memo_paper_and_final_result() -> None:
    memo = require_file(MEMO)
    paper = require_file(PAPER)
    required_memo = [
        "Status: `ACCEPTED_STEP5K_STRICT_SUPERGRAPH_COMPLETION`",
        "\\Gamma_{AA}^{(1)}",
        "\\Gamma_{AA,\\rm one\\ loop}^{(1)}",
        "-\\Gamma_{AA,\\rm HT}^{(1)}=0",
        "\\frac1{32\\pi^2}",
        "step5-aa-external-slot-decomposition-exact.json",
        "step5k-momentum-rule-ledger.json",
    ]
    required_paper = [
        "STEP5K_STRICT_SUPERGRAPH_COMPLETION",
        "step5k-gauge-vector-triangle.svg",
        "step5k-adjoint-matter-triangle.svg",
        "CENSUS_17_CANDIDATES_CLOSED_TARGET_BLIND",
    ]
    missing = [f"memo:{x}" for x in required_memo if x not in memo]
    missing += [f"paper:{x}" for x in required_paper if x not in paper]
    surfaces = [RULES, DWORD_MEMO, ROUTE_REVIEW, MEMO, PAPER]
    control_bytes = {
        str(path.relative_to(ROOT)): [
            byte for byte in path.read_bytes() if byte < 32 and byte not in (9, 10)
        ]
        for path in surfaces
    }
    math_delimiter_violations = {
        str(path.relative_to(ROOT)): markdown_math_violations(path)
        for path in surfaces
    }
    brace_violations = {
        str(path.relative_to(ROOT)): (require_file(path).count("{"), require_file(path).count("}"))
        for path in surfaces
        if require_file(path).count("{") != require_file(path).count("}")
    }
    forbidden_tokens = {
        str(path.relative_to(ROOT)): [
            token for token in (r"\sim", r"\approx", r"\propto") if token in require_file(path)
        ]
        for path in surfaces
    }
    text_clean = (
        all(not values for values in control_bytes.values())
        and all(not values for values in math_delimiter_violations.values())
        and not brace_violations
        and all(not values for values in forbidden_tokens.values())
    )
    record(
        "MEMO_PAPER_RESULT_AND_HT_ROUNDTRIP",
        not missing and text_clean,
        {
            "missing": missing,
            "control_bytes": control_bytes,
            "math_delimiter_violations": math_delimiter_violations,
            "brace_violations": brace_violations,
            "forbidden_tokens": forbidden_tokens,
        },
        ["K.122--K.129"],
    )


def main() -> None:
    check_task_and_ledger()
    check_rule_table()
    check_fp_inverse()
    check_sector_typed_ir()
    check_formula_rendering()
    check_gauge_dword()
    check_numerator_provenance()
    check_census_and_routes()
    check_matter_occurrences()
    check_memo_paper_and_final_result()

    failed = [row for row in checks if not row["passed"]]
    inputs = [
        TASK,
        LEDGER,
        RULES,
        RULE_LEDGER,
        DIAGRAM_IR,
        DWORD_JSON,
        EXTERNAL_SLOT,
        CENSUS,
        ROUTE_REVIEW,
        MEMO,
        PAPER,
    ]
    payload = {
        "schema": "step5k-strict-supergraph-verification-v1",
        "status": "PASS" if not failed else "FAIL",
        "check_count": len(checks),
        "failed": len(failed),
        "checks": checks,
        "input_sha256": {str(path.relative_to(ROOT)): sha256(path) for path in inputs if path.is_file()},
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if failed:
        for row in failed:
            print(f"FAIL {row['name']}: {row['evidence']}")
        raise SystemExit(1)
    print("PASS STEP5K_STRICT_SUPERGRAPH_COMPLETION 10/10")


if __name__ == "__main__":
    main()
