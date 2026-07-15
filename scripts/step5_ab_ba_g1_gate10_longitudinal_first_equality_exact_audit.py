#!/usr/bin/env python3
"""Exact Gate-10 first-equality audit for the AB/BA G1 longitudinal word.

The claimed extra family

    P_L = -bar(r1)^2 (r0-r2)

is compared directly with the complete 24-word longitudinal D-algebra

    L_A = -(1/2) D_+ barD^2 D^2

already present in every A-mark row.  Loop components are SymPy indeterminates
inside the repository's finite Grassmann engine; hence the comparison is a
polynomial identity test, not numerical sampling.  No HT coefficient is read.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab_ba_g1_longitudinal_contact_exact_audit as longitudinal  # noqa: E402


g1 = longitudinal.g1
aa = longitudinal.aa

JSON_OUT = ROOT / "audits" / "step5-ab-ba-g1-gate10-longitudinal-first-equality-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g1-gate10-longitudinal-first-equality-exact.md"

ELL = sp.symbols("ell0:4")
ELL_SQUARE = sum(component**2 for component in ELL)


def qtext(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value)).replace("I", "i")


def qi_to_sympy(value: g1.QI) -> sp.Expr:
    return sp.expand(sp.sympify(value.re) + sp.I * sp.sympify(value.im))


def symbolic_vector(values: tuple[object, object, object, object]) -> g1.Vector:
    return tuple(g1.QI(re=sp.sympify(value)) for value in values)  # type: ignore[return-value]


def spinor_component(vector: tuple[sp.Expr, ...], dotted: int) -> sp.Expr:
    if dotted == 0:
        return sp.expand(vector[0] - sp.I * vector[1])
    if dotted == 1:
        return sp.expand(-vector[2] - sp.I * vector[3])
    raise ValueError(dotted)


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
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


def homogeneous_part(poly: sp.Expr, degree: int) -> sp.Expr:
    parameter = sp.symbols("t")
    scaled = sp.expand(poly.subs({ELL[index]: parameter * ELL[index] for index in range(4)}))
    return sp.expand(scaled.coeff(parameter, degree))


def third_forward_difference(poly: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    base = {component: 0 for component in ELL}
    values = []
    for step in range(4):
        point = dict(base)
        point[variable] = step
        values.append(sp.expand(poly.subs(point)))
    return sp.expand(values[3] - 3 * values[2] + 3 * values[1] - values[0])


def exact_longitudinal_rows(
    p_values: tuple[int, int, int, int],
    q_values: tuple[int, int, int, int],
    dotted: int,
) -> tuple[dict[tuple[str, object], sp.Expr], sp.Expr]:
    loop = symbolic_vector(ELL)
    p = g1.vector(p_values)
    q = g1.vector(q_values)
    rows: dict[tuple[str, object], sp.Expr] = {}
    sector_totals: dict[str, sp.Expr] = {}
    for sector in ("+", "-"):
        exact = longitudinal.g1_longitudinal_outer_a_rows(loop, p, q, dotted, sector)
        for key, value in exact.items():
            rows[sector, key] = qi_to_sympy(value)
        sector_totals[sector] = sp.expand(sum(rows[sector, key] for key in exact))
    # This is the same chirality combination used by selected_simplex_audit.
    return rows, sp.expand(sector_totals["+"] - sector_totals["-"])


def normalized_simplex_metric_projection(
    poly: sp.Expr,
    p_values: tuple[int, int, int, int],
    q_values: tuple[int, int, int, int],
) -> sp.Expr:
    """Extract the centered log-metric coefficient by exact finite differences.

    For D0=ell^2, D1=(ell-p)^2, D2=(ell-p-q)^2 the Feynman shift is

        ell = L + y p + z (p+q).

    The Laplacian of the cubic raw word is affine, so normalized simplex
    integration is exactly the average over the three vertices 0,p,p+q.
    """

    laplacian = sp.expand(sum(sp.diff(poly, component, 2) for component in ELL))
    p = tuple(sp.Integer(value) for value in p_values)
    total = tuple(sp.Integer(p_values[index] + q_values[index]) for index in range(4))
    vertices = ((sp.Integer(0),) * 4, p, total)
    values = [
        sp.expand(laplacian.subs(dict(zip(ELL, vertex))) / 8)
        for vertex in vertices
    ]
    return sp.simplify(sum(values) / 3 / 4096)


def row_divisibility(
    rows: dict[tuple[str, object], sp.Expr],
    aggregate: sp.Expr,
    p_values: tuple[int, int, int, int],
) -> dict[str, Any]:
    r1_square = sp.expand(
        sum((ELL[index] - p_values[index]) ** 2 for index in range(4))
    )
    nonzero = {key: value for key, value in rows.items() if sp.expand(value) != 0}
    divisible: list[str] = []
    for key, value in nonzero.items():
        _, remainder = sp.div(value, r1_square, *ELL)
        if sp.expand(remainder) == 0:
            divisible.append(str(key))
    quotient, remainder = sp.div(aggregate, r1_square, *ELL)
    return {
        "r1_square": qtext(r1_square),
        "nonzero_rows": len(nonzero),
        "individually_r1_square_divisible_rows": divisible,
        "aggregate_r1_square_divisible": sp.expand(remainder) == 0,
        "aggregate_division_quotient": qtext(quotient),
        "aggregate_division_remainder": qtext(remainder),
    }


def symbolic_source_gauge_contact_zero(
    dotted: int,
) -> dict[str, Any]:
    """Replay the complete I1--S_m3 bubble at symbolic AB momenta."""

    l_symbols = sp.symbols("cl0:4")
    p_symbols = sp.symbols("cp0:4")
    q_symbols = sp.symbols("cq0:4")

    def avec(values: tuple[sp.Symbol, ...]) -> aa.Vector:
        return tuple(aa.A(a=value) for value in values)  # type: ignore[return-value]

    result = longitudinal.source_gauge_contact(
        avec(l_symbols), avec(p_symbols), avec(q_symbols), dotted, "AB"
    )
    return {
        "orientation": "AB",
        "dotted": dotted,
        "complete_I1_terms": list(longitudinal.source_word_orbit()["AB"]["e2_A_mark"].values()),
        "nonzero_output": {key: value.text() for key, value in result.items()},
        "is_exact_zero": result == {},
        "BA_follows_from_exact_graded_mirror": (
            "-B1(D_-A)=+(D_-A)B1 with the corresponding SU(2) color relabeling"
        ),
    }


FRAMES = (
    {
        "id": "generic_1",
        "p": (1, 2, -1, 1),
        "q": (-2, 1, 3, 0),
    },
    {
        "id": "generic_2",
        "p": (0, 1, 1, 0),
        "q": (1, 0, 0, -1),
    },
)


def build_payload(*, replay_contact: bool) -> tuple[dict[str, Any], Ledger]:
    ledger = Ledger()
    expected_cubic = {
        0: -4096 * (ELL[0] - sp.I * ELL[1]) * ELL_SQUARE,
        1: 4096 * (ELL[2] + sp.I * ELL[3]) * ELL_SQUARE,
    }
    finite_difference_expected = {
        (0, 0): -24576,
        (0, 1): 24576 * sp.I,
        (1, 2): 24576,
        (1, 3): 24576 * sp.I,
    }

    frame_payloads: list[dict[str, Any]] = []
    for frame in FRAMES:
        p_values = frame["p"]
        q_values = frame["q"]
        total = tuple(p_values[index] + q_values[index] for index in range(4))
        dotted_payload: dict[str, Any] = {}
        metric_components: list[sp.Expr] = []
        for dotted in (0, 1):
            rows, aggregate = exact_longitudinal_rows(p_values, q_values, dotted)
            degree = sp.Poly(aggregate, *ELL).total_degree()
            cubic = homogeneous_part(aggregate, 3)
            ledger.check(f"{frame['id']}:dot{dotted}:degree", degree, 3)
            ledger.check(
                f"{frame['id']}:dot{dotted}:universal_cubic",
                cubic,
                expected_cubic[dotted],
            )
            divisibility = row_divisibility(rows, aggregate, p_values)
            ledger.check(
                f"{frame['id']}:dot{dotted}:nonzero_rows",
                divisibility["nonzero_rows"],
                12,
            )
            ledger.check(
                f"{frame['id']}:dot{dotted}:no_individual_r1_square",
                len(divisibility["individually_r1_square_divisible_rows"]),
                0,
            )
            ledger.check(
                f"{frame['id']}:dot{dotted}:aggregate_not_r1_square",
                divisibility["aggregate_r1_square_divisible"],
                False,
            )
            relevant_differences: dict[str, str] = {}
            for coordinate in range(4):
                difference = third_forward_difference(aggregate, ELL[coordinate])
                if difference:
                    relevant_differences[f"Delta_ell{coordinate}^3"] = qtext(difference)
                expected = finite_difference_expected.get((dotted, coordinate), sp.Integer(0))
                ledger.check(
                    f"{frame['id']}:dot{dotted}:third_difference_ell{coordinate}",
                    difference,
                    expected,
                )
            metric = normalized_simplex_metric_projection(
                aggregate, p_values, q_values
            )
            metric_components.append(metric)
            q_half = tuple(sp.Rational(value, 2) for value in q_values)
            ledger.check(
                f"{frame['id']}:dot{dotted}:metric_projection_q_over_2",
                metric,
                spinor_component(q_half, dotted),
            )
            dotted_payload[str(dotted)] = {
                "full_raw_polynomial": qtext(aggregate),
                "total_degree": degree,
                "homogeneous_cubic": qtext(cubic),
                "third_forward_differences": relevant_differences,
                "r1_square_test": divisibility,
                "normalized_centered_metric_projection": qtext(metric),
                "Gate10_claimed_projection_minus_p_plus_q": qtext(
                    -spinor_component(tuple(map(sp.Integer, total)), dotted)
                ),
            }

        q_half_spinor = tuple(
            spinor_component(tuple(sp.Rational(value, 2) for value in q_values), dotted)
            for dotted in (0, 1)
        )
        gate10_spinor = tuple(
            -spinor_component(tuple(map(sp.Integer, total)), dotted)
            for dotted in (0, 1)
        )
        ledger.check(
            f"{frame['id']}:metric_pair",
            sp.Matrix(metric_components),
            sp.Matrix(q_half_spinor),
        )
        ledger.check(
            f"{frame['id']}:metric_pair_not_gate10",
            sp.Matrix(metric_components) == sp.Matrix(gate10_spinor),
            False,
        )
        frame_payloads.append(
            {
                "id": frame["id"],
                "p": list(p_values),
                "q": list(q_values),
                "p_plus_q": list(total),
                "dotted": dotted_payload,
                "finite_difference_metric_pair": [qtext(value) for value in metric_components],
                "exact_pair": [qtext(value) for value in q_half_spinor],
                "Gate10_pair": [qtext(value) for value in gate10_spinor],
            }
        )

    contacts = (
        [symbolic_source_gauge_contact_zero(dotted) for dotted in (0, 1)]
        if replay_contact
        else {"status": "NOT_REPLAYED_USE_--replay-contact"}
    )
    if replay_contact:
        for row in contacts:
            ledger.check(
                f"symbolic_I1Sm3_AB_dot{row['dotted']}_zero",
                row["is_exact_zero"],
                True,
            )

    payload: dict[str, Any] = {
        "schema": "step5-ab-ba-g1-gate10-longitudinal-first-equality-exact-v1",
        "status": (
            "GATE10_FIRST_EQUALITY_REJECTED__EXACT_LA_ALREADY_INCLUDED__"
            "NO_R1_SQUARE_DIVISOR__METRIC_PROJECTION_IS_Q_OVER_2_NOT_MINUS_P_PLUS_Q"
        ),
        "external_target_used": False,
        "definitions": {
            "routing": "r0=ell, r1=ell-p, r2=ell-p-q",
            "exact_longitudinal_operator": "L_A=-(1/2) D_+ barD^2 D^2",
            "chirality_combination": "L_A=L_{A,+}-L_{A,-}",
            "Gate10_claim": "P_L=-bar(r1)^2*(r0-r2)",
            "spinor_map": {
                "dot0": "S(v)^dot0=v0-i*v1",
                "dot1": "S(v)^dot1=-(v2+i*v3)",
            },
        },
        "first_equality": {
            "claimed": "L_A == -bar(r1)^2*(r0-r2)",
            "exact_cubic_dot0": qtext(expected_cubic[0]),
            "exact_cubic_dot1": qtext(expected_cubic[1]),
            "claimed_total_degree": 2,
            "exact_total_degree": 3,
            "verdict": "FALSE_BEFORE_ANY_SIMPLEX_INTEGRAL_OR_QUOTIENT",
        },
        "frames": frame_payloads,
        "source_resolvent_R2_middle_edge": {
            "claimed_cut": "+D0*D2*(r0-r2)",
            "exact_complete_I1_Sm3_symbolic_replay": contacts,
            "classification": (
                "Gate10 reuses the already enumerated L_A occurrence but does not "
                "supply a nonzero matching R2 Hessian.  Its added N_L is not an "
                "independent graph."
            ),
        },
        "adjudication": {
            "new_independent_N_L": False,
            "hidden_exact_bar_r1_square": False,
            "centered_metric_trace_exists": True,
            "centered_metric_trace": "S(q/2), diagnostic only; it is not an exact selected-edge cut",
            "current_contact_warning": (
                "The old formal replacement C_L=-L_A is not promoted here to a raw "
                "R2 graph identity; the complete I1-Sm3 replay is zero.  G1 raw "
                "contact closure therefore remains open, but Gate10's -(p+q) "
                "correction is exactly rejected."
            ),
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": sum(row["status"] == "PASS" for row in ledger.rows),
            "failed": sum(row["status"] == "FAIL" for row in ledger.rows),
            "rows": ledger.rows,
        },
    }
    return payload, ledger


def markdown(payload: dict[str, Any]) -> str:
    frame_sections: list[str] = []
    for frame in payload["frames"]:
        lines = [
            f"### {frame['id']}",
            "",
            "$$",
            f"p={tuple(frame['p'])},\\qquad q={tuple(frame['q'])},\\qquad P={tuple(frame['p_plus_q'])}.",
            "$$",
            "",
        ]
        for dotted in ("0", "1"):
            row = frame["dotted"][dotted]
            lines.extend(
                [
                    "$$",
                    f"L^{{\\dot {dotted}}}(\\ell)={row['full_raw_polynomial']}.",
                    "$$",
                    "",
                    "$$",
                    f"[L^{{\\dot {dotted}}}]_3={row['homogeneous_cubic']}.",
                    "$$",
                    "",
                    f"Nonzero rows: `{row['r1_square_test']['nonzero_rows']}`; "
                    f"rows divisible by $\\bar r_1^2$: "
                    f"`{len(row['r1_square_test']['individually_r1_square_divisible_rows'])}`; "
                    f"aggregate divisible: `{row['r1_square_test']['aggregate_r1_square_divisible']}`.",
                    "",
                    "$$",
                    f"\\mathscr M[L^{{\\dot {dotted}}}]={row['normalized_centered_metric_projection']},\\qquad "
                    f"-S(P)^{{\\dot {dotted}}}={row['Gate10_claimed_projection_minus_p_plus_q']}.",
                    "$$",
                    "",
                ]
            )
        frame_sections.append("\n".join(lines))

    return r"""# AB/BA G1 Gate10 longitudinal first-equality exact audit

Status: `@@STATUS@@`.

## 1. Definitions

$$
r_0=\ell,\qquad r_1=\ell-p,\qquad r_2=\ell-p-q,
$$

$$
L_A=-\frac12D_+\bar D^2D^2,
\qquad L_A=L_{A,+}-L_{A,-}.
$$

Gate10 claims

$$
L_A\stackrel{?}{=}-\bar r_1^2(r_0-r_2)^{\dot a}
=-\bar r_1^2(p+q)^{\dot a}.
$$

## 2. First equality

The complete 24-word exact exterior-algebra replay gives, in both generic
external frames,

$$
[L_A^{\dot0}]_3=-4096(\ell_0-i\ell_1)\bar\ell^2,
$$

$$
[L_A^{\dot1}]_3=+4096(\ell_2+i\ell_3)\bar\ell^2.
$$

Therefore

$$
\deg_\ell L_A=3,
\qquad
\deg_\ell\left[-\bar r_1^2(p+q)^{\dot a}\right]=2,
$$

$$
\boxed{L_A\ne-\bar r_1^2(p+q)^{\dot a}.}
$$

Equivalently,

$$
\Delta_{\ell_0}^3L_A^{\dot0}=-24576,
\qquad
\Delta_{\ell_1}^3L_A^{\dot0}=24576i,
$$

$$
\Delta_{\ell_2}^3L_A^{\dot1}=24576,
\qquad
\Delta_{\ell_3}^3L_A^{\dot1}=24576i,
$$

while all third differences of the Gate10 polynomial vanish.

## 3. Two generic full-polynomial frames

@@FRAMES@@

The exact centered metric diagnostic is

$$
\mathscr M[L]^{\dot a}
:=\frac{2}{4096}\int_{y,z\ge0\atop y+z\le1}dy\,dz\,
\frac18\Delta_\ell L^{\dot a}
\left(yp+z(p+q)\right)
=S\!\left(\frac q2\right)^{\dot a},
$$

not $-S(p+q)^{\dot a}$.  This metric projection is not an exact
$\bar r_1^2$ divisor: every frame has twelve nonzero longitudinal rows per
dotted component, zero of which is divisible by $\bar r_1^2$, and their sum
is also not divisible.

## 4. Matching source-resolvent cut

The complete symbolic $I_{[1]}S_{m3}$ replay contains the $A_2B_{11}$,
$A_1B_{12}$, outer-connection, and vector-frame bridge terms.  It gives

$$
K_{L,R_2}^{AB}=0,
$$

with BA obtained by the exact graded mirror
$-B_1(D_-A)=+(D_-A)B_1$.  Thus the claimed

$$
K_L=+D_0D_2(r_0-r_2)
$$

is not a raw Hessian result.

## 5. Adjudication

$$
\boxed{
N_L\text{ is not a new graph, no exact hidden }\bar r_1^2\text{ factor exists,}
}
$$

$$
\boxed{
(2,2)\longrightarrow(1,1)\text{ is rejected at the first parent equality.}
}
$$

The earlier formal contact $C_L=-L_A$ is not thereby proved as a raw
$R_2$ Hessian: the complete $I_{[1]}S_{m3}$ word is zero.  Hence the G1 raw
contact closure remains open, while the Gate10 $-(p+q)$ correction is closed.
""".replace("@@STATUS@@", payload["status"]).replace(
        "@@FRAMES@@", "\n\n".join(frame_sections)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replay-contact",
        action="store_true",
        help="also run the slower fully symbolic I1-Sm3 contact replay",
    )
    parser.add_argument("--json-out", type=Path, default=JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=MD_OUT)
    args = parser.parse_args()

    payload, _ = build_payload(replay_contact=args.replay_contact)
    args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    args.md_out.write_text(markdown(payload))
    print(
        json.dumps(
            {
                "status": payload["status"],
                "checks": payload["checks"],
                "json": str(args.json_out),
                "markdown": str(args.md_out),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
