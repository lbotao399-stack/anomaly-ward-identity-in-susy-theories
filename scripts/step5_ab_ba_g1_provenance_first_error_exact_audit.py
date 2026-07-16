#!/usr/bin/env python3
"""Exact provenance audit for the AB/BA G1 coefficient.

This audit is target-blind.  It distinguishes the source-selected DRED
subtotal from the rejected generic-(p,q) lift and from the residual-q
completion.  In particular it prevents the pure total-divergence vector
(2,2) from being reported as a physical coefficient two.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
G1_IN = ROOT / "audits" / "step5-ab-ba-g1-longitudinal-contact-exact.json"
FULL_1PI_IN = ROOT / "audits" / "step5-ab-ba-full-1pi-quotient-exact.json"
UNIFIED_IN = ROOT / "audits" / "step5-ab-ba-unified-typed-q-covariance-exact.json"
DEFAULT_JSON = ROOT / "audits" / "step5-ab-ba-g1-provenance-first-error-exact.json"
DEFAULT_MD = ROOT / "audits" / "step5-ab-ba-g1-provenance-first-error-exact.md"


def parse_exact(value: str) -> sp.Expr:
    return sp.sympify(value, locals={"i": sp.I, "sqrt": sp.sqrt})


class Ledger:
    def __init__(self) -> None:
        self.rows: list[dict[str, str]] = []

    def check(self, check_id: str, actual: Any, expected: Any) -> None:
        if isinstance(actual, bool) or isinstance(expected, bool):
            passed = actual is expected
        elif isinstance(actual, (sp.Basic, int)) or isinstance(expected, (sp.Basic, int)):
            passed = sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
        else:
            passed = actual == expected
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": str(actual),
                "expected": str(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def build_payload() -> dict[str, Any]:
    ledger = Ledger()
    g1 = json.loads(G1_IN.read_text(encoding="utf-8"))
    full_1pi = json.loads(FULL_1PI_IN.read_text(encoding="utf-8"))
    unified = json.loads(UNIFIED_IN.read_text(encoding="utf-8"))

    selected = g1["simplex_and_quotient"]["generic_p_q_lambda1_units"]
    a = sp.Matrix(tuple(parse_exact(x) for x in selected["A_mark"]))
    b = sp.Matrix(tuple(parse_exact(x) for x in selected["B_mark"]))
    source_selected = a + b
    ledger.check("SOURCE_SELECTED_A", a, sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3))))
    ledger.check("SOURCE_SELECTED_B", b, sp.Matrix((sp.Rational(2, 3), sp.Rational(4, 3))))
    ledger.check("SOURCE_SELECTED_SUM", source_selected, sp.Matrix((2, 2)))

    # Let X=<D,B1> carry the B1 momentum p and let
    # Y=B1(P.D) carry the D momentum q.  The exact dotted Leibniz identity is
    # T_DB=P(DB1)=X+Y, so a X+b Y=(a-b)X+b T_DB.
    raw_to_pair_total_derivative = sp.Matrix(((1, -1), (0, 1)))
    selected_pair_td = raw_to_pair_total_derivative * source_selected
    ledger.check("D_GT_B1_PAIR_TOTAL_DERIVATIVE_MAP", selected_pair_td, sp.Matrix((0, 2)))
    ledger.check("SOURCE_SELECTED_PHYSICAL_MOD_TOTAL_DERIVATIVE", selected_pair_td[0], 0)
    ledger.check("SOURCE_SELECTED_IS_TWO_T_DB", selected_pair_td[1], 2)

    local_a = a[0] - a[1]
    local_b = b[0] - b[1]
    ledger.check("SOURCE_SELECTED_A_Q_EQUALS_MINUS_P", local_a, sp.Rational(2, 3))
    ledger.check("SOURCE_SELECTED_B_Q_EQUALS_MINUS_P", local_b, -sp.Rational(2, 3))
    ledger.check("SOURCE_SELECTED_LOCAL_SUM", local_a + local_b, 0)
    ledger.check("G1_ARTIFACT_DERIVED_AB", g1["derived_before_HT"]["AB"]["D>B1"], "0")

    # The later generic-(p,q) full-word reconstruction is a different object.
    # Its own locked boundary rejects it because restriction to q=-p does not
    # agree with the direct one-variable replay.
    rejected_generic = sp.Matrix((-sp.Rational(7, 6), -sp.Rational(4, 3)))
    rejected_q_minus_p = rejected_generic[0] - rejected_generic[1]
    direct_q_minus_p = -sp.Rational(3, 2) + 1
    ledger.check("REJECTED_GENERIC_Q_EQUALS_MINUS_P", rejected_q_minus_p, sp.Rational(1, 6))
    ledger.check("DIRECT_ONE_VARIABLE_Q_EQUALS_MINUS_P", direct_q_minus_p, -sp.Rational(1, 2))
    ledger.check("GENERIC_SPECIALIZATION_MISMATCH", rejected_q_minus_p - direct_q_minus_p, sp.Rational(2, 3))
    ledger.check(
        "FULL_1PI_RAW_G1_STATUS",
        full_1pi["raw_G1_boundary"]["status"],
        "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
    )
    ledger.check(
        "FULL_1PI_REJECTS_GENERIC_LIFT",
        full_1pi["raw_G1_boundary"]["generic_pq_occurrence_result_is_not_used"],
        True,
    )

    # Locate the first invalid inference in the unified status.  Its own
    # arithmetic obtains (0,2) in the (pair,total derivative) basis, while its
    # final status nevertheless groups G1 with G3 as a physical factor two.
    checks = {
        row["id"]: row for row in unified["checks"]["rows"]
    }
    ledger.check(
        "UNIFIED_STORED_G1_PAIR_TD",
        checks["G1_TYPED_PAIR_TOTAL_DERIVATIVE"]["actual"],
        "Matrix([[0], [2]])",
    )
    ledger.check(
        "UNIFIED_STATUS_CONTAINS_G1_FACTOR_TWO",
        "G1_G3_COMMON_FACTOR_TWO_REMAINS" in unified["status"],
        True,
    )

    return {
        "schema": "step5-ab-ba-g1-provenance-first-error-exact-v1",
        "status": "PASS_G1_FIRST_ERROR_IS_PURE_DIVERGENCE_MISREPORTED_AS_PHYSICAL_TWO",
        "external_target_used": False,
        "basis": {
            "raw": ["p_on_B1", "q_on_D"],
            "typed": ["pair_<D,B1>", "total_derivative_T_DB"],
            "identity": "a*X+b*Y=(a-b)*X+b*T_DB; T_DB=X+Y",
            "matrix": [["1", "-1"], ["0", "1"]],
        },
        "source_selected_orbit": {
            "A": [str(x) for x in a],
            "B": [str(x) for x in b],
            "sum_raw": [str(x) for x in source_selected],
            "sum_typed": [str(x) for x in selected_pair_td],
            "physical_mod_total_derivative": "0",
        },
        "rejected_generic_lift": {
            "raw_p_q": [str(x) for x in rejected_generic],
            "q_equals_minus_p": str(rejected_q_minus_p),
            "direct_one_variable": str(direct_q_minus_p),
            "difference": str(rejected_q_minus_p - direct_q_minus_p),
            "status": "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
        },
        "first_error": {
            "location": "unified G1 status after G1_TYPED_PAIR_TOTAL_DERIVATIVE",
            "invalid_step": "(2,2) in raw (p,q) basis was called a physical factor two",
            "exact_correction": "(2,2)=2*T_DB maps to (pair,total derivative)=(0,2)",
            "consequence": "G1 cannot be grouped with G3 as a common physical factor-two mismatch",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def render_md(payload: dict[str, Any]) -> str:
    return r"""# AB/BA G1 provenance first-error exact audit

Status: `PASS_G1_FIRST_ERROR_IS_PURE_DIVERGENCE_MISREPORTED_AS_PHYSICAL_TWO`.

## 1. Source-selected DRED orbit

Let

$$
X=\langle D,B_1\rangle,
\qquad
Y=B_1(P^{\dot a}D_{\dot a}),
\qquad
T_{DB}=P^{\dot a}(D_{\dot a}B_1)=X+Y.
$$

The exact selected rows are

$$
A=\frac43p+\frac23q,
\qquad
B=\frac23p+\frac43q,
$$

therefore

$$
A+B=2p+2q=2X+2Y=2T_{DB}.
$$

For a general raw vector $(a,b)$,

$$
aX+bY=(a-b)X+bT_{DB},
$$

so

$$
\begin{pmatrix}c_{\rm pair}\\c_{T}\end{pmatrix}
=
\begin{pmatrix}1&-1\\0&1\end{pmatrix}
\begin{pmatrix}2\\2\end{pmatrix}
=
\begin{pmatrix}0\\2\end{pmatrix}.
$$

Hence

$$
\boxed{(2,2)_{(p,q)}=2T_{DB},\qquad c_{\rm pair}=0.}
$$

The same result follows at $q=-p$:

$$
A=\frac43-\frac23=\frac23,
\qquad
B=\frac23-\frac43=-\frac23,
\qquad
A+B=0.
$$

## 2. Rejected generic lift

The later full-word reconstruction gives

$$
F_{\rm generic}=-\frac76p-\frac43q.
$$

Its restriction is

$$
F_{\rm generic}\big|_{q=-p}
=-\frac76+\frac43
=\frac{-7+8}{6}
=\frac16.
$$

The direct one-variable replay gives

$$
F_{\rm direct}=-\frac32+1=-\frac12.
$$

Thus

$$
\frac16-\left(-\frac12\right)
=\frac16+\frac36
=\frac46
=\frac23\ne0.
$$

This lift remains `BLOCKED_RAW_GRAPH_Q_DATA_MISSING` and cannot replace the
selected orbit.

## 3. First error

The unified audit itself records

$$
(2,2)_{(p,q)}\longmapsto(0,2)_{({\rm pair},T_{DB})},
$$

but its final status calls the same row a physical G1 factor two.  The first
invalid step is therefore

$$
\boxed{2T_{DB}\not\longrightarrow 2\langle D,B_1\rangle.}
$$

G1 and G3 do not form a common physical factor-two mismatch.
"""


def canonical(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    payload = build_payload()
    json_text = canonical(payload)
    md_text = render_md(payload)
    if args.check:
        if args.json.read_text(encoding="utf-8") != json_text:
            raise SystemExit(f"stale artifact: {args.json}")
        if args.md.read_text(encoding="utf-8") != md_text:
            raise SystemExit(f"stale artifact: {args.md}")
    else:
        args.json.write_text(json_text, encoding="utf-8")
        args.md.write_text(md_text, encoding="utf-8")
    print(f"PASS {payload['checks']['passed']}/{payload['checks']['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
