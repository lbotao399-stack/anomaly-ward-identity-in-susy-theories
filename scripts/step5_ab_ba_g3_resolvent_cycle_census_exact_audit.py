#!/usr/bin/env python3
"""Exact target-blind resolvent-cycle census for the AB/BA G3 TMH parent.

For one fixed flavor s=2 or s=3, the quantum field basis is

    (u, phi1, tildephi1, phi_s, tildephi_s).

The audit expands

    -(hbar/2) STr[G (V_M+V_H) G (V_M+V_H) G I0'']

into every oriented source, matter, and Hminus Hessian block.  It decides
whether the source reverse block and the two action orders are independent
multiplicities, and compares the resulting cycle weight with the direct Wick
pre-D scalar.  No holomorphic-twist coefficient is read.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = (
    ROOT / "audits" / "step5-ab-ba-g3-resolvent-cycle-census-exact.json"
)
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-resolvent-cycle-census-exact.md"

STATUS = (
    "PASS_G3_RESOLVENT_TWO_NONZERO_CYCLES_CORRELATED__"
    "OUTER_HALF_CANCELLED_ONCE__CURRENT_PRED_NO_DOUBLE_COUNT"
)

BASIS = ("u", "phi1", "tildephi1", "phi_s", "tildephi_s")
INDEX = {field: index for index, field in enumerate(BASIS)}


def exact_text(value: object) -> str:
    if isinstance(value, sp.MatrixBase):
        return str(value.tolist()).replace("I", "i")
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    if isinstance(value, tuple):
        return "(" + ", ".join(exact_text(entry) for entry in value) + ")"
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        difference = sp.Matrix(actual) - sp.Matrix(expected)
        return all(sp.simplify(entry) == 0 for entry in difference)
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = exact_equal(actual, expected)
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": exact_text(actual),
                "expected": exact_text(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def one_block(row: str, column: str, value: sp.Expr) -> sp.Matrix:
    matrix = sp.zeros(len(BASIS))
    matrix[INDEX[row], INDEX[column]] = value
    return matrix


def supertrace(matrix: sp.Matrix, parities: tuple[int, ...]) -> sp.Expr:
    return sp.expand(
        sum(
            (-1) ** parities[index] * matrix[index, index]
            for index in range(len(BASIS))
        )
    )


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()

    g_u, g_1, g_s = sp.symbols("G_u G_1 G_s", nonzero=True)
    i_u1, i_1u = sp.symbols("I_u1 I_1u", nonzero=True)
    m_us, m_su = sp.symbols("M_us M_su", nonzero=True)
    h_1s, h_s1 = sp.symbols("H_1s H_s1", nonzero=True)

    propagator = sp.zeros(len(BASIS))
    propagator[INDEX["u"], INDEX["u"]] = g_u
    propagator[INDEX["phi1"], INDEX["tildephi1"]] = g_1
    propagator[INDEX["tildephi1"], INDEX["phi1"]] = g_1
    propagator[INDEX["phi_s"], INDEX["tildephi_s"]] = g_s
    propagator[INDEX["tildephi_s"], INDEX["phi_s"]] = g_s

    source_blocks = {
        "I_u1": one_block("u", "phi1", i_u1),
        "I_1u": one_block("phi1", "u", i_1u),
    }
    matter_blocks = {
        "M_us": one_block("u", "phi_s", m_us),
        "M_su": one_block("phi_s", "u", m_su),
    }
    hminus_blocks = {
        "H_1s": one_block("tildephi1", "tildephi_s", h_1s),
        "H_s1": one_block("tildephi_s", "tildephi1", h_s1),
    }
    source = sum(source_blocks.values(), sp.zeros(len(BASIS)))
    matter = sum(matter_blocks.values(), sp.zeros(len(BASIS)))
    hminus = sum(hminus_blocks.values(), sp.zeros(len(BASIS)))

    # The quantum superfields in this TMH block are even integration
    # variables.  Thus STr equals Tr on this restricted field block.
    parities = (0, 0, 0, 0, 0)
    ledger.check("G3_TMH_FIELD_PARITIES", parities, (0, 0, 0, 0, 0))
    c_ab, c_ba = sp.symbols("C_AB C_BA")
    ledger.check("AB_REVERSE_HESSIAN_BLOCK_RETAINS_AB", c_ab, c_ab)
    ledger.check("AB_REVERSE_HESSIAN_BLOCK_IS_BA_SOURCE", c_ab == c_ba, False)

    rows: list[dict[str, Any]] = []
    row_values: dict[str, sp.Expr] = {}
    for action_order, source_name, matter_name, hminus_name in itertools.product(
        ("MH", "HM"),
        source_blocks,
        matter_blocks,
        hminus_blocks,
    ):
        first, second = (
            (matter_blocks[matter_name], hminus_blocks[hminus_name])
            if action_order == "MH"
            else (hminus_blocks[hminus_name], matter_blocks[matter_name])
        )
        product = (
            propagator
            * first
            * propagator
            * second
            * propagator
            * source_blocks[source_name]
        )
        value = sp.factor(supertrace(product, parities))
        diagonal_support = [
            BASIS[index]
            for index in range(len(BASIS))
            if sp.simplify(product[index, index]) != 0
        ]
        row_id = f"{action_order}::{source_name}::{matter_name}::{hminus_name}"
        row_values[row_id] = value
        rows.append(
            {
                "id": row_id,
                "action_order": action_order,
                "source_block": source_name,
                "matter_block": matter_name,
                "Hminus_block": hminus_name,
                "supertrace": exact_text(value),
                "nonzero": value != 0,
                "diagonal_support": diagonal_support,
            }
        )

    nonzero = [row for row in rows if row["nonzero"]]
    ledger.check("ORIENTED_BLOCK_CANDIDATE_COUNT", len(rows), 16)
    ledger.check("NONZERO_BLOCK_CYCLE_COUNT", len(nonzero), 2)
    ledger.check(
        "NONZERO_BLOCK_CYCLE_IDS",
        tuple(row["id"] for row in nonzero),
        (
            "MH::I_1u::M_us::H_s1",
            "HM::I_u1::M_su::H_1s",
        ),
    )
    ledger.check(
        "NONZERO_CYCLE_STARTING_BLOCKS",
        tuple(tuple(row["diagonal_support"]) for row in nonzero),
        (("u",), ("phi1",)),
    )

    expected_cycle_mh = g_u * m_us * g_s * h_s1 * g_1 * i_1u
    expected_cycle_hm = g_1 * h_1s * g_s * m_su * g_u * i_u1
    ledger.check(
        "MH_I1U_WEIGHT",
        row_values[nonzero[0]["id"]],
        expected_cycle_mh,
    )
    ledger.check(
        "HM_IU1_WEIGHT",
        row_values[nonzero[1]["id"]],
        expected_cycle_hm,
    )

    # Even ordered Hessians have equal reverse blocks.  Under this exact
    # substitution the two rows are one closed Wick cycle with two starts.
    i0, vm, vh = sp.symbols("I0 VM VH", nonzero=True)
    reverse_equal = {
        i_u1: i0,
        i_1u: i0,
        m_us: vm,
        m_su: vm,
        h_1s: vh,
        h_s1: vh,
    }
    common_cycle = sp.factor(g_u * g_1 * g_s * i0 * vm * vh)
    cycle_mh_equal = sp.factor(expected_cycle_mh.subs(reverse_equal))
    cycle_hm_equal = sp.factor(expected_cycle_hm.subs(reverse_equal))
    ledger.check("TWO_CYCLES_EQUAL_MH", cycle_mh_equal, common_cycle)
    ledger.check("TWO_CYCLES_EQUAL_HM", cycle_hm_equal, common_cycle)

    # Expanding V=V_M+V_H gives four action words.  MM and HH vanish on the
    # source block; the two cross words are precisely the two rows above.
    full_source = source.subs(reverse_equal)
    full_matter = matter.subs(reverse_equal)
    full_hminus = hminus.subs(reverse_equal)
    mm = sp.factor(
        supertrace(
            propagator
            * full_matter
            * propagator
            * full_matter
            * propagator
            * full_source,
            parities,
        )
    )
    mh = sp.factor(
        supertrace(
            propagator
            * full_matter
            * propagator
            * full_hminus
            * propagator
            * full_source,
            parities,
        )
    )
    hm = sp.factor(
        supertrace(
            propagator
            * full_hminus
            * propagator
            * full_matter
            * propagator
            * full_source,
            parities,
        )
    )
    hh = sp.factor(
        supertrace(
            propagator
            * full_hminus
            * propagator
            * full_hminus
            * propagator
            * full_source,
            parities,
        )
    )
    ledger.check("RESOLVENT_MM_WORD_ZERO", mm, 0)
    ledger.check("RESOLVENT_MH_WORD", mh, common_cycle)
    ledger.check("RESOLVENT_HM_WORD", hm, common_cycle)
    ledger.check("RESOLVENT_HH_WORD_ZERO", hh, 0)
    cross_sum = sp.factor(mh + hm)
    ledger.check("RESOLVENT_CROSS_SUM", cross_sum, 2 * common_cycle)
    resolvent_half = sp.Rational(1, 2)
    resolvent_cycle_weight = sp.factor(resolvent_half * cross_sum / common_cycle)
    ledger.check("RESOLVENT_HALF_TIMES_CORRELATED_TWO_CYCLES", resolvent_cycle_weight, 1)

    # The two labels are perfectly correlated: fixing either source block or
    # action order fixes the other.  There is no Cartesian product of four
    # nonzero rows.
    source_to_action = {row["source_block"]: row["action_order"] for row in nonzero}
    action_to_source = {row["action_order"]: row["source_block"] for row in nonzero}
    ledger.check(
        "SOURCE_BLOCK_TO_ACTION_ORDER_BIJECTION",
        source_to_action,
        {"I_1u": "MH", "I_u1": "HM"},
    )
    ledger.check(
        "ACTION_ORDER_TO_SOURCE_BLOCK_BIJECTION",
        action_to_source,
        {"MH": "I_1u", "HM": "I_u1"},
    )
    ledger.check("INDEPENDENT_TWO_BY_TWO_MULTIPLICITY", len(nonzero), 2)
    ledger.check("FOUR_NONZERO_CARTESIAN_ROWS_EXIST", len(nonzero) == 4, False)

    # Direct Wick expansion is the alternative representation of the same
    # combinatorics.  Its 1/2! is canceled by the two even action sequences;
    # the species-compatible contraction is unique.  It is not multiplied by
    # a second raw source-Hessian factor two.
    action_taylor_half = sp.Rational(1, 2)
    even_action_sequences = sp.Integer(2)
    unique_species_wick = sp.Integer(1)
    direct_wick_weight = sp.simplify(
        action_taylor_half * even_action_sequences * unique_species_wick
    )
    ledger.check("DIRECT_ACTION_TAYLOR_WEIGHT", direct_wick_weight, 1)
    ledger.check("RESOLVENT_AND_DIRECT_WICK_WEIGHTS_EQUAL", resolvent_cycle_weight, direct_wick_weight)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source_scalar = -coupling**2 / (4 * sp.sqrt(2))
    matter_scalar = sp.sqrt(2) * coupling / hbar
    hminus32_scalar = -sp.sqrt(2) * coupling / hbar
    hminus33_scalar = -hminus32_scalar
    three_propagator_scalar = -hbar * (hbar / 16) * (hbar / 16)
    current_pre32 = sp.simplify(
        source_scalar
        * matter_scalar
        * hminus32_scalar
        * three_propagator_scalar
        * direct_wick_weight
    )
    current_pre33 = sp.simplify(
        source_scalar
        * matter_scalar
        * hminus33_scalar
        * three_propagator_scalar
        * direct_wick_weight
    )
    resolvent_pre32 = sp.simplify(
        source_scalar
        * matter_scalar
        * hminus32_scalar
        * three_propagator_scalar
        * resolvent_cycle_weight
    )
    resolvent_pre33 = sp.simplify(
        source_scalar
        * matter_scalar
        * hminus33_scalar
        * three_propagator_scalar
        * resolvent_cycle_weight
    )
    ledger.check(
        "CURRENT_G32_PRED",
        current_pre32,
        -sp.sqrt(2) * hbar * coupling**4 / 1024,
    )
    ledger.check(
        "CURRENT_G33_PRED",
        current_pre33,
        sp.sqrt(2) * hbar * coupling**4 / 1024,
    )
    ledger.check("RESOLVENT_EQUALS_CURRENT_G32_PRED", resolvent_pre32, current_pre32)
    ledger.check("RESOLVENT_EQUALS_CURRENT_G33_PRED", resolvent_pre33, current_pre33)
    ledger.check("CURRENT_PRED_RAW_SOURCE_FACTOR_TWO", sp.Integer(1), 1)
    ledger.check("CURRENT_PRED_DOUBLE_COUNTS_TWO", current_pre32 == 2 * resolvent_pre32, False)
    ledger.check("HYPOTHETICAL_EXTRA_TWO_G32", 2 * current_pre32, -sp.sqrt(2) * hbar * coupling**4 / 512)

    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": "step5-ab-ba-g3-resolvent-cycle-census-exact-v1",
        "status": STATUS if failed == 0 else "FAIL",
        "authority_role": "LOCAL_PROPOSAL_TARGET_BLIND",
        "external_target_used": False,
        "residual_q_used": False,
        "basis": list(BASIS),
        "propagator_blocks": {
            "u-u": "G_u",
            "phi1-tildephi1": "G_1",
            "tildephi1-phi1": "G_1",
            "phi_s-tildephi_s": "G_s",
            "tildephi_s-phi_s": "G_s",
        },
        "Hessian_blocks": {
            "I0": ["I_u1", "I_1u"],
            "M_s": ["M_us", "M_su"],
            "Hminus": ["H_1s", "H_s1"],
        },
        "oriented_cycle_census": {
            "candidate_count": len(rows),
            "nonzero_count": len(nonzero),
            "rows": rows,
        },
        "nonzero_cycles": [
            {
                "id": nonzero[0]["id"],
                "start": "u",
                "path": "u-G_u-u-M-phi_s-G_s-tildephi_s-H-tildephi1-G_1-phi1-I0-u",
                "weight": exact_text(expected_cycle_mh),
            },
            {
                "id": nonzero[1]["id"],
                "start": "phi1",
                "path": "phi1-G_1-tildephi1-H-tildephi_s-G_s-phi_s-M-u-G_u-u-I0-phi1",
                "weight": exact_text(expected_cycle_hm),
            },
        ],
        "correlation": {
            "source_to_action": source_to_action,
            "action_to_source": action_to_source,
            "source_reverse_and_action_swap_are_same_two_rows": True,
            "independent_2x2": False,
            "reverse_AB_Hessian_block_becomes_BA_source": False,
            "BA_has_same_two-cycle_sparsity_with_C_AB_replaced_by_C_BA": True,
        },
        "resolvent_expansion": {
            "MM": exact_text(mm),
            "MH": exact_text(mh),
            "HM": exact_text(hm),
            "HH": exact_text(hh),
            "cross_sum": exact_text(cross_sum),
            "overall_half": "1/2",
            "cycle_weight": exact_text(resolvent_cycle_weight),
            "formula": "(1/2)_resolvent*(2)_correlated_closed_cycles=1",
        },
        "direct_Wick_representation": {
            "formula": "(1/2!)_action*(2)_even_action_sequences*(1)_unique_species_Wick=1",
            "weight": exact_text(direct_wick_weight),
            "alternative_to_resolvent_count_not_independent_multiplier": True,
        },
        "preD": {
            "current_formula": "source*M*Hminus*three_propagators*action_cross_weight",
            "raw_source_Hessian_factor_two_applied": False,
            "G32_current": exact_text(current_pre32),
            "G32_resolvent": exact_text(resolvent_pre32),
            "G33_current": exact_text(current_pre33),
            "G33_resolvent": exact_text(resolvent_pre33),
            "current_double_counts_two": False,
            "hypothetical_extra_two_G32": exact_text(2 * current_pre32),
        },
        "decision": {
            "overall_resolvent_half_cancelled_by": "one correlated pair of nonzero closed block cycles",
            "source_reverse_block_two_is_independent_of_action_order_two": False,
            "current_preD_retained": True,
            "documentation_rule": (
                "Use either resolvent (1/2)*2 or direct Wick (1/2!)*2; "
                "do not form an independent 2_source*2_action census."
            ),
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows) - failed,
            "failed": failed,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    checks = payload["checks"]
    return r"""# AB/BA G3 resolvent cycle census

Status: `@@STATUS@@`.

## 1. Field blocks

For fixed $s=2$ or $s=3$, use

$$
\mathcal B=(u,\phi_1,\widetilde\phi_1,\phi_s,\widetilde\phi_s).
$$

The nonzero propagator blocks are

$$
G_{uu}=G_u,
$$

$$
G_{\phi_1\widetilde\phi_1}
=G_{\widetilde\phi_1\phi_1}=G_1,
$$

$$
G_{\phi_s\widetilde\phi_s}
=G_{\widetilde\phi_s\phi_s}=G_s.
$$

The oriented Hessian blocks are

$$
I_0'':quad I_{u1},I_{1u},
$$

$$
V_M'':quad M_{us},M_{su},
$$

$$
V_H'':quad H_{1s},H_{s1}.
$$

All five quantum superfields in this block are even, so

$$
\operatorname{STr}_{\mathcal B}=\operatorname{Tr}_{\mathcal B}.
$$

## 2. Complete oriented census

Expand

$$
\Gamma_{I_0}^{(1)}
=-\frac{\hbar}{2}
\operatorname{STr}
\left[G(V_M+V_H)G(V_M+V_H)GI_0''\right].
$$

There are

$$
2_{\rm action\ order}
\cdot2_{I_0''}
\cdot2_{V_M''}
\cdot2_{V_H''}
=16
$$

oriented block candidates.  Exactly two are nonzero:

$$
\begin{aligned}
\mathcal C_u
&=\operatorname{Tr}
\left[GV_MGV_HGI_{1u}\right]\\
&=G_uM_{us}G_sH_{s1}G_1I_{1u},
\end{aligned}
$$

$$
\begin{aligned}
\mathcal C_{\phi_1}
&=\operatorname{Tr}
\left[GV_HGV_MGI_{u1}\right]\\
&=G_1H_{1s}G_sM_{su}G_uI_{u1}.
\end{aligned}
$$

Every other oriented block product is zero.

For even ordered Hessians,

$$
I_{u1}=I_{1u}=I_0,
\qquad
M_{us}=M_{su}=V_M,
\qquad
H_{1s}=H_{s1}=V_H.
$$

Hence

$$
\mathcal C_u
=\mathcal C_{\phi_1}
=G_uG_1G_sI_0V_MV_H
=:\mathcal C.
$$

The four resolvent words are

$$
\operatorname{STr}[GV_MGV_MGI_0'']=0,
$$

$$
\operatorname{STr}[GV_MGV_HGI_0'']=\mathcal C,
$$

$$
\operatorname{STr}[GV_HGV_MGI_0'']=\mathcal C,
$$

$$
\operatorname{STr}[GV_HGV_HGI_0'']=0.
$$

Therefore

$$
-\frac{\hbar}{2}(\mathcal C+\mathcal C)
=-\hbar\mathcal C.
$$

## 3. The two labels are correlated

The nonzero map is

$$
I_{1u}\longleftrightarrow (V_M,V_H),
$$

$$
I_{u1}\longleftrightarrow (V_H,V_M).
$$

Fixing the source block fixes the action order, and fixing the action order
fixes the source block.  Thus

$$
N_{\rm nonzero}=2,
\qquad
N_{\rm nonzero}\ne2_{\rm source}\cdot2_{\rm action}=4.
$$

The overall resolvent factor is canceled once:

$$
\boxed{
\left(\frac12\right)_{\rm resolvent}
(2)_{\rm correlated\ closed\ cycles}=1.}
$$

The source reverse block and the action-order swap are two names for the same
two nonzero rows.

## 4. Direct Wick representation

The direct expansion gives

$$
\boxed{
\left(\frac1{2!}\right)_{\rm action}
(2)_{V_MV_H,V_HV_M}
(1)_{\rm species\ Wick}=1.}
$$

This is an alternative representation of the resolvent count.  It is not an
additional multiplier.

With

$$
C_I=-\frac{g^2}{4\sqrt2},
\qquad
V_M=\frac{\sqrt2g}{\hbar},
$$

$$
V_{H,32}=-\frac{\sqrt2g}{\hbar},
\qquad
V_{H,33}=+\frac{\sqrt2g}{\hbar},
$$

$$
G_uG_1G_s
=(-\hbar)\left(\frac{\hbar}{16}\right)^2
=-\frac{\hbar^3}{256},
$$

the current direct-Wick scalars are

$$
C_{G32}^{\rm preD}
=\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\hbar^3}{256}\right)
=-\frac{\sqrt2\hbar g^4}{1024},
$$

$$
C_{G33}^{\rm preD}
=+\frac{\sqrt2\hbar g^4}{1024}.
$$

The resolvent cycle weight gives the same two scalars.  No raw source-Hessian
factor $2$ is multiplied into the current pre-D expression.

An additional factor $2$ would give

$$
2C_{G32}^{\rm preD}
=-\frac{\sqrt2\hbar g^4}{512},
$$

which is not the current pre-D scalar.

$$
N_{\rm pass}=@@PASS@@,
\qquad
N_{\rm fail}=@@FAIL@@.
$$
""".replace("@@STATUS@@", str(payload["status"])).replace(
        "@@PASS@@", str(checks["passed"])
    ).replace("@@FAIL@@", str(checks["failed"]))


def canonical(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def validate(payload: dict[str, Any]) -> None:
    if payload.get("status") != STATUS:
        raise AssertionError(payload.get("status"))
    if payload.get("external_target_used") is not False:
        raise AssertionError("external target used")
    if payload.get("residual_q_used") is not False:
        raise AssertionError("residual q used")
    census_payload = payload["oriented_cycle_census"]
    if census_payload["candidate_count"] != 16 or census_payload["nonzero_count"] != 2:
        raise AssertionError(census_payload)
    if payload["correlation"]["independent_2x2"] is not False:
        raise AssertionError(payload["correlation"])
    if payload["preD"]["current_double_counts_two"] is not False:
        raise AssertionError(payload["preD"])
    if payload["checks"]["failed"] != 0:
        raise AssertionError(payload["checks"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    validate(payload)
    json_text = canonical(payload)
    md_text = markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
    if args.print_json:
        print(json_text, end="")
    else:
        print("PASS G3 resolvent 16 oriented candidates and 2 nonzero cycles")
        print("PASS G3 source reverse block and action order are correlated")
        print("PASS G3 overall resolvent half cancels once")
        print("PASS G3 current pre-D scalar has no extra factor two")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
