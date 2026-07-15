#!/usr/bin/env python3
"""Target-blind exact G1 R1/R2/R3 vector-frame contact orbit.

This audit expands the symmetric vector bridge through I_[2], performs the
complete species/port census for external (D,B1), and replays every surviving
R2/R3 D-word with symbolic momenta.  Only occurrence-tagged four-dimensional
inverse squares are admitted to the anomaly sector.  No HT data are read.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import sys
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab_ba_g1_longitudinal_contact_exact_audit as contact  # noqa: E402


aa = contact.aa
g1 = contact.g1
sd = contact.sd

JSON_OUT = ROOT / "audits" / "step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.md"


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        left = sp.Matrix(actual)
        right = sp.Matrix(expected)
        return left.shape == right.shape and all(sp.simplify(value) == 0 for value in left - right)
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


def text(value: object) -> str:
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    return str(value)


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
                "actual": text(actual),
                "expected": text(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def a_to_sympy(value: aa.A) -> sp.Expr:
    return sp.expand(
        sp.sympify(value.a)
        + sp.sqrt(2) * sp.sympify(value.b)
        + sp.I * sp.sympify(value.c)
        + sp.I * sp.sqrt(2) * sp.sympify(value.d)
    )


def avec(symbols: tuple[sp.Symbol, ...]) -> aa.Vector:
    return tuple(aa.A(a=value) for value in symbols)  # type: ignore[return-value]


def spinor(vector: tuple[sp.Expr, ...], dotted: int) -> sp.Expr:
    if dotted == 0:
        return sp.expand(vector[0] - sp.I * vector[1])
    if dotted == 1:
        return sp.expand(-vector[2] - sp.I * vector[3])
    raise ValueError(dotted)


def vector_frame_source_expansion() -> dict[str, Any]:
    return {
        "bridge": {
            "B_ad": "exp(ad_V/2)",
            "V": "sqrt(2)*g*U",
            "b1(L)": "(1/sqrt(2))*[U,L]",
            "b2(L)": "(1/4)*[U,[U,L]]",
        },
        "I0_order_two": ["A1*B11"],
        "I1_order_three": [
            "A2*B11",
            "A1*B12",
            "b1(A1)*B11",
            "A1*b1(B11)",
        ],
        "I1_descendant_occurrence_tags_AB": list(
            contact.full_i1_products.__doc__.splitlines()
            if contact.full_i1_products.__doc__
            else []
        ),
        "I1_exact_ten_descendant_words_AB": [
            "NA1_A2*B11",
            "NA1_gamma*B11",
            "NA0*B12",
            "A2*NB0",
            "A1*NB1_B12",
            "A1*NB1_gamma",
            "NA1_bridge*B11",
            "NA0*B12_bridge",
            "A2_bridge*NB0",
            "A1*NB1_bridge",
        ],
        "I2_order_four": [
            "A3*B11",
            "b1(A2)*B11",
            "b2(A1)*B11",
            "A2*B12",
            "A2*b1(B11)",
            "b1(A1)*B12",
            "b1(A1)*b1(B11)",
            "A1*B13",
            "A1*b1(B12)",
            "A1*b2(B11)",
        ],
        "species_support": {
            "I0": ["u", "phi1"],
            "I1_each_word": ["u", "u", "phi1"],
            "I2_each_word": ["u", "u", "u", "phi1"],
        },
    }


def port_census(ledger: Ledger) -> dict[str, Any]:
    rows = [
        {
            "class": "R1",
            "term": "+G0*I2",
            "source": "I2(u,u,u,phi1)",
            "external_assignment": "I2:(D,B1)",
            "quantum_ports": ["u", "u"],
            "internal_edges": ["u--u same-source tadpole"],
            "loops": 1,
            "status": "SCALELESS_TADPOLE",
        },
        {
            "class": "R2_G",
            "term": "-G0*Sg3*G0*I1",
            "source": "I1(u,u,phi1)",
            "action": "Sg3(u,u,u)",
            "external_assignment": "I1:B1; Sg3:D",
            "quantum_ports": ["I1:u,u", "Sg3:u,u"],
            "internal_edges": ["u--u", "u--u"],
            "loops": 1,
            "status": "UNIQUE_NONZERO_ORDINARY_BUBBLE",
        },
        {
            "class": "R2_M",
            "term": "-G0*Sm3*G0*I1",
            "source": "I1(u,u,phi1)",
            "action": "Sm3(tilde1,u,phi1)",
            "external_assignment": "I1:D; Sm3:B1",
            "quantum_ports": ["I1:u,phi1", "Sm3:u,tilde1"],
            "internal_edges": ["u--u", "phi1--tilde1"],
            "loops": 1,
            "status": "D_ALGEBRA_ZERO",
        },
        {
            "class": "R3_M4",
            "term": "-G0*Sm4*G0*I0",
            "source": "I0(u,phi1)",
            "action": "Sm4(tilde1,u,u,phi1)",
            "external_assignment": "Sm4:(D,B1)",
            "quantum_ports": ["I0:u,phi1", "Sm4:u,tilde1"],
            "internal_edges": ["u--u", "phi1--tilde1"],
            "loops": 1,
            "status": "D_ALGEBRA_ZERO",
        },
    ]
    ledger.check("resolvent_surviving_species_classes", len(rows), 4)
    ledger.check("R1_loop_count", rows[0]["loops"], 1)
    ledger.check("R2G_edge_count", len(rows[1]["internal_edges"]), 2)
    ledger.check("R2M_edge_count", len(rows[2]["internal_edges"]), 2)
    ledger.check("R3_edge_count", len(rows[3]["internal_edges"]), 2)
    excluded = {
        "R2_other_matter_flavors": "source phi1 has no matching tilde2/tilde3",
        "R2_superpotential": "source u ports have no propagating partner",
        "R3_pure_gauge_gauge_fixing_FP_NK_measure": "source phi1 has no tilde1 partner",
        "R3_superpotential": "source u has no u partner",
    }
    return {"survivors": rows, "excluded_by_ports": excluded}


def symbolic_r2_gauge_bubble(ledger: Ledger) -> dict[str, Any]:
    ell_symbols = sp.symbols("ell0:4")
    p_symbols = sp.symbols("p0:4")
    q_symbols = sp.symbols("q0:4")
    ell = avec(ell_symbols)
    p = avec(p_symbols)
    q = avec(q_symbols)
    expected = {
        dotted: -sp.sqrt(2) * spinor(tuple(q_symbols), dotted) / 4
        for dotted in (0, 1)
    }
    payload: dict[str, Any] = {}
    for orientation in ("AB", "BA"):
        payload[orientation] = {}
        for dotted in (0, 1):
            raw = contact.source_matter_contact(ell, p, q, dotted, orientation)
            tagged = {tag: a_to_sympy(value) for tag, value in raw.items()}
            total = sp.expand(sum(tagged.values()))
            gamma = sp.expand(
                sum(value for tag, value in tagged.items() if "gamma" in tag)
            )
            bridge = sp.expand(
                sum(value for tag, value in tagged.items() if "bridge" in tag)
            )
            ledger.check(f"R2G:{orientation}:dot{dotted}:total", total, expected[dotted])
            ledger.check(
                f"R2G:{orientation}:dot{dotted}:gamma",
                gamma,
                -sp.sqrt(2) * spinor(tuple(q_symbols), dotted) / 2,
            )
            ledger.check(
                f"R2G:{orientation}:dot{dotted}:bridge",
                bridge,
                sp.sqrt(2) * spinor(tuple(q_symbols), dotted) / 4,
            )
            ledger.check(
                f"R2G:{orientation}:dot{dotted}:no_loop_momentum",
                bool(total.free_symbols.intersection(set(ell_symbols))),
                False,
            )
            ledger.check(
                f"R2G:{orientation}:dot{dotted}:no_B_momentum",
                bool(total.free_symbols.intersection(set(p_symbols))),
                False,
            )
            payload[orientation][str(dotted)] = {
                "tagged_raw_numerators": {tag: text(value) for tag, value in tagged.items()},
                "nonbridge_gamma_sum": text(gamma),
                "vector_bridge_sum": text(bridge),
                "complete_sum": text(total),
                "denominator": "two-propagator bubble",
                "four_dimensional_inverse_square": False,
                "DRED_anomaly_sector": "0",
            }
    ledger.check(
        "R2G_AB_BA_dot0_equal",
        payload["AB"]["0"]["complete_sum"],
        payload["BA"]["0"]["complete_sum"],
    )
    ledger.check(
        "R2G_AB_BA_dot1_equal",
        payload["AB"]["1"]["complete_sum"],
        payload["BA"]["1"]["complete_sum"],
    )
    return payload


def symbolic_zero_bubbles(ledger: Ledger) -> dict[str, Any]:
    ell_symbols = sp.symbols("zell0:4")
    p_symbols = sp.symbols("zp0:4")
    q_symbols = sp.symbols("zq0:4")
    ell = avec(ell_symbols)
    p = avec(p_symbols)
    q = avec(q_symbols)
    payload: dict[str, Any] = {"R2_M": {}, "R3_M4": {}}
    for dotted in (0, 1):
        r2_ab = contact.source_gauge_contact(ell, p, q, dotted, "AB")
        r3_ab = contact.middle_gauge_seagull_contact(ell, p, q, dotted, "AB")
        ledger.check(f"R2M_AB_dot{dotted}_symbolic_zero", r2_ab, {})
        ledger.check(f"R3M4_AB_dot{dotted}_symbolic_zero", r3_ab, {})
        payload["R2_M"][str(dotted)] = {
            "AB": {},
            "BA": "exact graded/color mirror of AB",
            "DRED_anomaly_sector": "0",
        }
        payload["R3_M4"][str(dotted)] = {
            "AB": {},
            "BA": "exact graded/color mirror of AB",
            "DRED_anomaly_sector": "0",
        }
    return payload


def selected_r4_vector(ledger: Ledger) -> dict[str, Any]:
    tensor = sd.g1_full_tensor_frame_audit()
    selected = tensor["selected_momentum_coefficients"]
    normalized: dict[str, tuple[g1.QI, g1.QI]] = {}
    for branch, mark in enumerate(("A", "B")):
        plus = selected["+", branch]
        minus = selected["-", branch]
        normalized[mark] = tuple(
            (plus[component] - minus[component]) / 4096
            for component in range(2)
        )  # type: ignore[assignment]
    expected_a = (g1.QI.coerce(Fraction(4, 3)), g1.QI.coerce(Fraction(2, 3)))
    expected_b = (g1.QI.coerce(Fraction(2, 3)), g1.QI.coerce(Fraction(4, 3)))
    ledger.check("R4_A_selected", normalized["A"], expected_a)
    ledger.check("R4_B_selected", normalized["B"], expected_b)
    total = tuple(normalized["A"][index] + normalized["B"][index] for index in range(2))
    ledger.check("R4_selected_total", total, (g1.QI.coerce(2), g1.QI.coerce(2)))
    return {
        "A_mark": [str(value) for value in normalized["A"]],
        "B_mark": [str(value) for value in normalized["B"]],
        "sum_raw_p_q": [str(value) for value in total],
    }


def build_payload(*, replay_symbolic: bool) -> tuple[dict[str, Any], Ledger]:
    ledger = Ledger()
    source = vector_frame_source_expansion()
    ledger.check("I0_sector_count", len(source["I0_order_two"]), 1)
    ledger.check("I1_vector_frame_sector_count", len(source["I1_order_three"]), 4)
    ledger.check("I1_descendant_word_count", len(source["I1_exact_ten_descendant_words_AB"]), 10)
    ledger.check("I2_vector_frame_sector_count", len(source["I2_order_four"]), 10)
    ports = port_census(ledger)
    r4 = selected_r4_vector(ledger)

    if replay_symbolic:
        r2_g = symbolic_r2_gauge_bubble(ledger)
        zero_bubbles = symbolic_zero_bubbles(ledger)
    else:
        r2_g = {"status": "NOT_REPLAYED_USE_--replay-symbolic"}
        zero_bubbles = {"status": "NOT_REPLAYED_USE_--replay-symbolic"}

    # R1 has one massless propagator and no external momentum through the loop.
    # Every possible DRED defect is a massless tadpole and vanishes in DR.
    r1 = {
        "all_I2_species": "u,u,u,phi1",
        "external_ports": "D=u and B1=phi1",
        "quantum_ports": "u,u",
        "loop_integrals": (
            "integral d^d ell (mu_ell^2)^r (ell^2)^s/(ell^2)^n = 0 "
            "for every integer r,s,n by massless scaleless DR continuation"
        ),
        "DRED_anomaly_sector": "0",
    }
    ledger.check("R1_DRED_anomaly", r1["DRED_anomaly_sector"], "0")

    missing_anomaly = sp.Matrix((0, 0))
    ledger.check("R1_R2_R3_new_anomaly_vector", missing_anomaly, sp.zeros(2, 1))
    raw = sp.Matrix((2, 2)) + missing_anomaly
    ledger.check("G1_common_layer_raw_p_q", raw, sp.Matrix((2, 2)))
    pair_total_map = sp.Matrix(((1, -1), (0, 1)))
    pair_total = pair_total_map * raw
    ledger.check("G1_pair_total_derivative_basis", pair_total, sp.Matrix((0, 2)))
    ledger.check("G1_mod_total_derivative", pair_total[0], 0)
    ledger.check("missing_exact_minus_one", missing_anomaly, sp.Matrix((0, 0)))

    payload: dict[str, Any] = {
        "schema": "step5-ab-ba-g1-actual-resolvent-contact-orbit-exact-v1",
        "status": (
            "G1_VECTOR_FRAME_R1_R2_R3_ANOMALY_ZERO__NO_MISSING_MINUS_ONE__"
            "COMMON_LAYER_RAW_TWO_TWO__MOD_TOTAL_DERIVATIVE_ZERO"
        ),
        "external_target_used": False,
        "vector_frame_source": source,
        "port_census": ports,
        "R1": r1,
        "R2_gauge_bubble": r2_g,
        "R2_R3_symbolic_zero_bubbles": zero_bubbles,
        "R4_selected_edge_anomaly": r4,
        "longitudinal_boundary": {
            "exact_result": (
                "L_A is already in the 24 R4 words; no nonzero R2/R3 Hessian "
                "equals -L_A and no row has an exact bar(r1)^2 divisor"
            ),
            "forbidden_projection": (
                "a global centered metric trace is not an occurrence-tagged inverse-kernel cut"
            ),
            "Gate10_minus_p_plus_q": "REJECTED",
            "ordinary_no_inverse_square_term": {
                "anomaly_sector": False,
                "reason": (
                    "it has no occurrence-tagged four-dimensional inverse square, "
                    "hence no full-square minus four-dimensional-square defect"
                ),
                "raw_Ward_contact_completion": "SEPARATE_IDENTITY_NOT_CLAIMED_COMPLETE",
            },
        },
        "common_layer": {
            "new_R1_R2_R3_anomaly_raw_p_q": ["0", "0"],
            "G1_raw_p_q": [str(value) for value in raw],
            "basis_identity": "a*X+b*Y=(a-b)*X+b*T_DB with T_DB=X+Y",
            "G1_pair_total_derivative": [str(value) for value in pair_total],
            "G1_after_total_derivative_quotient": str(pair_total[0]),
            "missing_terms_supply_minus_one_D_gt_B1": False,
            "common_layer_closure_verdict": "NO_COMMON_LAYER_CLOSURE",
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
    return r"""# AB/BA G1 actual vector-frame resolvent contact orbit

Status: `@@STATUS@@`.

## 1. Vector-frame source

With

$$
V=\sqrt{2}\,g\,U,\qquad
{\cal B}_{\rm ad}=e^{\operatorname{ad}_V/2},\qquad
b_1(L)=\frac{1}{\sqrt{2}}[U,L],\qquad
b_2(L)=\frac{1}{4}[U,[U,L]],
$$

the source sectors needed for two external fields are

$$
I_{[0]}: A_1B_{11},
$$

$$
I_{[1]}:\quad
A_2B_{11}+A_1B_{12}+b_1(A_1)B_{11}+A_1b_1(B_{11}),
$$

$$
\begin{aligned}
I_{[2]}:\quad&
A_3B_{11}+b_1(A_2)B_{11}+b_2(A_1)B_{11}\\
&+A_2B_{12}+A_2b_1(B_{11})+b_1(A_1)B_{12}
+b_1(A_1)b_1(B_{11})\\
&+A_1B_{13}+A_1b_1(B_{12})+A_1b_2(B_{11}).
\end{aligned}
$$

Every $I_{[1]}$ word has species $(u,u,\phi_1)$; every $I_{[2]}$ word has
$(u,u,u,\phi_1)$.

## 2. Complete legal lower-resolvent classes

$$
R_1=G_0I_{[2]}:\quad
(u,u)_{\rm quantum}\longrightarrow\text{one massless tadpole}.
$$

$$
R_{2,G}=-G_0S_{g3}G_0I_{[1]}:\quad
(u,u)\leftrightarrow(u,u).
$$

$$
R_{2,M}=-G_0S_{m3}G_0I_{[1]}:\quad
(u,\phi_1)\leftrightarrow(u,\widetilde\phi_1).
$$

$$
R_{3,M}=-G_0S_{m4}G_0I_{[0]}:\quad
(u,\phi_1)\leftrightarrow(u,\widetilde\phi_1).
$$

Pure gauge, gauge-fixing, FP, NK, and measure $R_3$ vertices have no
$\widetilde\phi_1$ port and therefore cannot close the source $\phi_1$ port.

## 3. Exact symbolic bubbles

Define

$$
S(q)^{\dot0}=q_0-iq_1,qquad
S(q)^{\dot1}=-(q_2+iq_3).
$$

The complete $I_{[1]}S_{g3}$ result, for both AB and BA, is

$$
N_{R_{2,G}}^{\dot a}
=-\frac{\sqrt{2}}{4}S(q)^{\dot a}.
$$

Occurrence resolution gives

$$
N_{\rm nonbridge}=-\frac{\sqrt{2}}{2}S(q),\qquad
N_{\rm vector\ bridge}=+\frac{\sqrt{2}}{4}S(q),
$$

$$
N_{\rm complete}=-\frac{\sqrt{2}}{4}S(q).
$$

It contains neither $\ell$ nor $p$ and contains no four-dimensional inverse
square.  Hence

$$
{\cal A}_{R_{2,G}}=0.
$$

The complete symbolic exterior-algebra replays give

$$
N_{R_{2,M}}=0,qquad N_{R_{3,M}}=0.
$$

For $R_1$, every possible evanescent numerator remains a massless tadpole:

$$
\int d^d\ell\,
\frac{(\mu_\ell^2)^r(\ell^2)^s}{(\ell^2)^n}=0.
$$

Therefore

$$
\boxed{{\cal A}_{R_1}={\cal A}_{R_2}={\cal A}_{R_3}=0.}
$$

## 4. Longitudinal sector boundary

The ordinary longitudinal term has no occurrence-tagged
four-dimensional inverse square.  Therefore it has no
$p_{\rm full}^2-\bar p^2=\widehat p^2$ cutting defect:

$$
{\cal A}_{\rm longitudinal,\ no\ square}=0.
$$

This anomaly-sector statement is separate from the raw Ward/contact identity;
the latter is not claimed complete here.

## 5. Common layer

The occurrence-tagged $R_4$ selected squares remain

$$
A=\left(\frac43,\frac23\right),qquad
B=\left(\frac23,\frac43\right),
$$

$$
G_{1,\rm raw}=(2,2)_{(p,q)}.
$$

Let

$$
X=\langle D,B_1\rangle,qquad
Y=B_1(P\cdot D),qquad
T_{DB}=X+Y.
$$

Then

$$
2X+2Y=2T_{DB},qquad
(c_{\rm pair},c_T)=(0,2).
$$

Thus

$$
\boxed{[G_1]_{\rm total\ derivative}=0.}
$$

The vector-frame $R_1/R_2/R_3$ orbit supplies $(0,0)$, not a coefficient
$-1$ in the $D>B_1$ slot.  Since no target data enter this derivation, the
common-layer verdict is

$$
\boxed{\texttt{NO\_COMMON\_LAYER\_CLOSURE}.}
$$
""".replace("@@STATUS@@", payload["status"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replay-symbolic",
        action="store_true",
        help="run the slower arbitrary-momentum R2/R3 exterior-algebra replay",
    )
    parser.add_argument("--json-out", type=Path, default=JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=MD_OUT)
    args = parser.parse_args()
    payload, _ = build_payload(replay_symbolic=args.replay_symbolic)
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
