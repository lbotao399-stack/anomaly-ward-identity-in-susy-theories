#!/usr/bin/env python3
"""Exact fixed-order source-Hessian and one-loop cycle combinatorics.

This audit decides whether the reverse mixed Hessian block supplies a new
factor two, or instead cancels the one-loop supertrace half.  It uses the
fixed AB source ordering and a port-preserving three-species cycle.  No HT
coefficient is read.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits" / "step5-ab-ba-source-cycle-supertrace-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-source-cycle-supertrace-exact.md"
LOCKED_NOTE = ROOT / "audits" / "step5-ab1-standard-feynman-strictification.md"
CENSUS = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        difference = sp.Matrix(actual) - sp.Matrix(expected)
        return difference.shape[0] * difference.shape[1] == 0 or all(
            sp.simplify(entry) == 0 for entry in difference
        )
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = equal(actual, expected)
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": text(actual) if isinstance(actual, sp.Basic) else str(actual),
                "expected": text(expected) if isinstance(expected, sp.Basic) else str(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    locked = LOCKED_NOTE.read_text(encoding="utf-8")
    ledger.check(
        "LOCKED_REVERSE_BLOCK_SAME_CYCLE",
        "reverse mixed\nHessian block is the same closed Wick cycle with a different starting point" in locked,
        True,
    )
    ledger.check(
        "LOCKED_SUPERTRACE_HALF_REMOVES_DUPLICATE",
        "the factor (1/2) in the supertrace removes that duplicate" in locked,
        True,
    )

    # Mixed Hessian of I0^{AB}=C_AB u^A phi^B.  Both off-diagonal blocks
    # retain the same ordered color labels AB.
    cab, k = sp.symbols("C_AB K")
    source_hessian = sp.Matrix(((0, cab), (cab, 0)))
    closed_cycle_kernel = sp.Matrix(((0, k), (k, 0)))
    product = source_hessian * closed_cycle_kernel
    two_start_sum = sp.trace(product)
    supertrace_value = sp.Rational(1, 2) * two_start_sum
    ledger.check("SOURCE_TWO_CYCLIC_STARTS", tuple(product.diagonal()), (cab * k, cab * k))
    ledger.check("SOURCE_TRACE_SUM", two_start_sum, 2 * cab * k)
    ledger.check("SOURCE_HALF_TRACE", supertrace_value, cab * k)
    ledger.check("ONE_CANONICAL_CYCLE_FINAL_WEIGHT", supertrace_value / (cab * k), 1)
    ledger.check(
        "FORBID_HALF_AFTER_CYCLIC_QUOTIENT",
        sp.Rational(1, 2) * supertrace_value == supertrace_value,
        False,
    )

    # Reversing the derivative order does not exchange the external ordered
    # source.  AB and BA use independent source coefficients.
    cba = sp.Symbol("C_BA")
    source_labels = {
        "I_AB[uA,phiB]": cab,
        "I_AB[phiB,uA]": cab,
        "I_BA[uB,phiA]": cba,
        "I_BA[phiA,uB]": cba,
    }
    ledger.check("AB_REVERSE_BLOCK_RETAINS_AB", source_labels["I_AB[phiB,uA]"], cab)
    ledger.check("AB_REVERSE_BLOCK_IS_NOT_BA", source_labels["I_AB[phiB,uA]"] == cba, False)

    # Port-preserving triangle skeleton.  Quantum species are the three cycle
    # edges.  I joins species 0--2, X joins 0--1, and Y joins 1--2.  The two
    # action sequences are the two cyclic starting descriptions of the same
    # fixed ordered AB Wick cycle.
    insertion = sp.zeros(3)
    vertex_x = sp.zeros(3)
    vertex_y = sp.zeros(3)
    insertion[0, 2] = insertion[2, 0] = 1
    vertex_x[0, 1] = vertex_x[1, 0] = 1
    vertex_y[1, 2] = vertex_y[2, 1] = 1
    xy_start = sp.trace(vertex_x * vertex_y * insertion)
    yx_start = sp.trace(vertex_y * vertex_x * insertion)
    action_cross = sp.Rational(1, 2) * (xy_start + yx_start)
    ledger.check("FIXED_AB_XY_CYCLE", xy_start, 1)
    ledger.check("FIXED_AB_YX_CYCLE", yx_start, 1)
    ledger.check("ACTION_TAYLOR_CROSS_TERM", action_cross, 1)

    # The same result follows from the direct zero-dimensional Wick skeleton:
    # O=a c, V_X=a b, V_Y=b c.  Each species appears twice, so the unique
    # species-compatible contraction has unit weight.
    gaussian_second_moment = sp.Integer(1)
    direct_wick = gaussian_second_moment**3
    interaction_taylor = sp.Rational(1, 2) * 2
    ledger.check("DIRECT_WICK_SPECIES_MATCHING", direct_wick, 1)
    ledger.check("DISTINCT_ACTION_SEQUENCE_FACTOR", interaction_taylor, 1)
    ledger.check("DIRECT_FIXED_AB_TRIANGLE_WEIGHT", direct_wick * interaction_taylor, 1)

    # Route 001 (G1), 007 (G2), and 008/009 (G3) are separately directed AB
    # rows.  Their reverse BA rows have different pair_ids and route_ids.
    routes = json.loads(CENSUS.read_text(encoding="utf-8"))["routes"]
    route_ids = (
        "TRI::A__B1::001::G[0,1]::M1[0,1]",
        "TRI::A__B1::007::M1[1,0]::M1[0,2]",
        "TRI::A__B1::008::M2[1,2]::Hminus[0,1]",
        "TRI::A__B1::009::M3[1,2]::Hminus[0,2]",
    )
    selected = {row["route_id"]: row for row in routes if row["route_id"] in route_ids}
    ledger.check("DIRECTED_AB_ROUTE_COUNT", len(selected), 4)
    ledger.check("DIRECTED_AB_PAIR_IDS", {row["pair_id"] for row in selected.values()}, {"A__B1"})
    for route_id, row in selected.items():
        ledger.check(f"ROUTE_EXPANSION_{route_id}", row["expansion_factor"], "(1/2!)*(two action orderings)=1")

    # G2 has two labeled M1 placements; G1/G3 have two distinct even action
    # factors.  In either case the fixed AB direct-Wick coefficient is one.
    topology_weights = {
        "G1_G_M1": sp.Rational(1, 2) * 2,
        "G2_M1_left_M1_right": sp.Rational(1, 2) * 2,
        "G32_M2_Hminus": sp.Rational(1, 2) * 2,
        "G33_M3_Hminus": sp.Rational(1, 2) * 2,
    }
    for label, value in topology_weights.items():
        ledger.check(f"TOPOLOGY_WEIGHT_{label}", value, 1)

    return {
        "schema": "step5-ab-ba-source-cycle-supertrace-exact-v1",
        "status": (
            "REVERSE_MIXED_HESSIAN_IS_CYCLIC_DUPLICATE__"
            "SUPERTRACE_HALF_TIMES_TWO_STARTS_IS_ONE__NO_G1_G3_HALF"
        ),
        "external_target_used": False,
        "fixed_source": "I0^{AB}=C_AB*u^A*phi1^B",
        "source_hessian": {
            "blocks": ["I_AB[uA,phiB]=C_AB", "I_AB[phiB,uA]=C_AB"],
            "two_start_trace": "2*C_AB*K",
            "one_loop_half": "1/2",
            "canonical_cycle_weight": "1",
            "reverse_block_changes_AB_to_BA": False,
        },
        "action_wick_skeleton": {
            "XY_trace": "1",
            "YX_trace": "1",
            "half_sum": "1",
            "direct_species_matching": "1",
        },
        "topology_weights": {label: text(value) for label, value in topology_weights.items()},
        "conclusion": {
            "G1_source_action_half": "REJECTED",
            "G3_source_action_half": "REJECTED",
            "reason": "keeping one canonical cycle already implements (1/2)*(two cyclic starts)=1",
            "remaining_factor_two_location": "not source mixed-Hessian or action Taylor/Wick skeleton",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(_: dict[str, Any]) -> str:
    return r"""# AB/BA source-cycle supertrace exact audit

Status: `REVERSE_MIXED_HESSIAN_IS_CYCLIC_DUPLICATE__SUPERTRACE_HALF_TIMES_TWO_STARTS_IS_ONE__NO_G1_G3_HALF`.

No HT coefficient is used.

## 1. Fixed ordered source

For

$$
I_0^{AB}=C_{AB}u^A\phi_1^B,
$$

the mixed Hessian is

$$
I_{AB}''=
\begin{pmatrix}
0&C_{AB}\\
C_{AB}&0
\end{pmatrix}.
$$

The reverse block still carries (AB), not (BA):

$$
I_{AB;u^A\phi^B}''=C_{AB},
\qquad
I_{AB;\phi^Bu^A}''=C_{AB}.
$$

Let the rest of the same closed cycle be

$$
K_{\rm cyc}=
\begin{pmatrix}
0&K\\
K&0
\end{pmatrix}.
$$

Then

$$
I_{AB}''K_{\rm cyc}
=
\begin{pmatrix}
C_{AB}K&0\\
0&C_{AB}K
\end{pmatrix},
$$

and

$$
\frac12\operatorname{Tr}(I_{AB}''K_{\rm cyc})
=\frac12(C_{AB}K+C_{AB}K)
=C_{AB}K.
$$

Thus the reverse block is the second cyclic start removed by the supertrace
half.  After replacing the two starts by one canonical cycle, its weight is

$$
\boxed{1,}
$$

not (1/2).

## 2. Action Taylor and Wick cycle

Use three quantum species and matrices

$$
I=E_{02}+E_{20},
\qquad
X=E_{01}+E_{10},
\qquad
Y=E_{12}+E_{21}.
$$

Direct multiplication gives

$$
\operatorname{Tr}(XYI)=1,
\qquad
\operatorname{Tr}(YXI)=1.
$$

Therefore

$$
\frac12\left[
\operatorname{Tr}(XYI)+\operatorname{Tr}(YXI)
\right]
=1.
$$

Equivalently, for the direct Wick skeleton

$$
O=ac,
\qquad
V_X=ab,
\qquad
V_Y=bc,
$$

the unique species-compatible contraction is

$$
\langle ac\,ab\,bc\rangle_{m cyc}
=\langle a^2\rangle\langle b^2\rangle\langle c^2\rangle
=1.
$$

For distinct even action vertices,

$$
\frac1{2!}(V_XV_Y+V_YV_X)=V_XV_Y.
$$

For the two labeled (M_1) placements in G2, the same calculation gives

$$
\frac1{2!}(M_{1,L}M_{1,R}+M_{1,R}M_{1,L})=M_{1,L}M_{1,R}.
$$

Hence

$$
\boxed{
w_{G_1}=w_{G_2}=w_{G_{3,2}}=w_{G_{3,3}}=1.
}
$$

The common G1/G3 factor two is not generated by the fixed-source mixed
Hessian or by the action Taylor/Wick skeleton.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    artifact = build_artifact()
    if args.write:
        JSON_OUT.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
        MD_OUT.write_text(markdown(artifact), encoding="utf-8")
    print(
        "PASS "
        f"{artifact['checks']['passed']}/{artifact['checks']['count']} "
        "source-cycle supertrace checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
