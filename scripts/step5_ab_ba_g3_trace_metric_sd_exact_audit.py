#!/usr/bin/env python3
"""Exact target-blind G3 trace/metric and occurrence-resolved SD audit.

The audit distinguishes the kinetic Schwinger cuts K0,K1,K2 from the
zero-square nonlinear-current rows JE/JX/PE/PX.  The former fix the metric
reconstruction factor chi from full-d cancellation; the latter cancel as
equal local words with opposite coefficients and carry no DRED remainder.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_g2_g3_dword_replay as g23  # noqa: E402
import step5_ab1_marked_sd_orbit_exact_audit as marked  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g3-trace-metric-sd-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-trace-metric-sd-exact.md"


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
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
        row = {
            "id": check_id,
            "status": "PASS" if passed else "FAIL",
            "actual": text(actual) if isinstance(actual, sp.Basic) else str(actual),
            "expected": text(expected) if isinstance(expected, sp.Basic) else str(expected),
        }
        self.rows.append(row)
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    words = marked.g23_exact_words()

    w0 = sp.expand(words["w12"])
    w1 = sp.expand(words["wedge_pq_r0"])
    w2 = sp.expand(words["wedge_p_r0"])
    ledger.check("RAW_W2_EQUALS_W01", w2, words["w01"])
    ledger.check(
        "RAW_A_PARENT_REPLAY",
        words["g3_a_full"],
        -1024 * words["det_r0"] * w0 + 1024 * words["det_r1"] * w1,
    )
    ledger.check(
        "RAW_B_PARENT_REPLAY",
        words["g3_b_parent_raw"],
        -1024 * words["det_r2"] * w2,
    )
    ledger.check("RAW_K0_CORE", words["g3_a_contact_top"], 512 * w0)
    ledger.check("RAW_K1_CORE", words["g3_transported_contact_core"], -128 * w1)
    ledger.check("RAW_K2_CORE", words["g3_b_contact"], -128 * w2)

    zero_momentum = [[0, 0], [0, 0]]
    theta_square = -2 * g23.variable(g23.S, 0) * g23.variable(g23.S, 1)
    bartheta_square = 2 * g23.variable(g23.S, 2) * g23.variable(g23.S, 3)
    d2_theta_square = g23.d2(theta_square, g23.S, zero_momentum).coefficient(0)
    minus_bard2_bartheta_square = -g23.bar_d2(
        bartheta_square, g23.S, zero_momentum
    ).coefficient(0)
    ledger.check("LOCKED_D2_THETA2_SATURATION", d2_theta_square, -4)
    ledger.check(
        "LOCKED_MINUS_BARD2_BARTHETA2_SATURATION",
        minus_bard2_bartheta_square,
        4,
    )

    # Common occurrence normalization: one quarter of the final physical
    # D-word.  In this normalization the three kinetic cuts are exactly
    # +512 W0, -512 W1, +512 W2 on the three distinct collapsed edges.
    k0_core = sp.expand(words["g3_a_contact_top"])
    k1_core = sp.expand(minus_bard2_bartheta_square * words["g3_transported_contact_core"])
    k2_core = sp.expand(d2_theta_square * words["g3_b_contact"])
    ledger.check("KINETIC_K0_CORE", k0_core, 512 * w0)
    ledger.check("KINETIC_K1_CORE", k1_core, -512 * w1)
    ledger.check("KINETIC_K2_CORE", k2_core, 512 * w2)

    chi, d0, d1, d2, mu2 = sp.symbols("chi D0 D1 D2 mu2")
    rw0, rw1, rw2 = sp.symbols("RW0 RW1 RW2")
    denominator = d0 * d1 * d2

    p0 = -512 * chi * (d0 + mu2) * rw0 / denominator
    p1 = 512 * chi * (d1 + mu2) * rw1 / denominator
    p2 = -512 * chi * (d2 + mu2) * rw2 / denominator
    k0 = 512 * rw0 / (d1 * d2)
    k1 = -512 * rw1 / (d0 * d2)
    k2 = 512 * rw2 / (d0 * d1)

    orbit_a = sp.factor(p0 + p1 + k0 + k1)
    expected_a = sp.factor(
        512
        * ((1 - chi) * d0 * rw0 + (chi - 1) * d1 * rw1 + chi * mu2 * (-rw0 + rw1))
        / denominator
    )
    ledger.check("A_ORBIT_COMMON_DENOMINATOR", orbit_a, expected_a)

    full_d_a_numerator = sp.expand((orbit_a * denominator / 512).subs(mu2, 0))
    polynomial_a = sp.Poly(full_d_a_numerator, d0, d1, rw0, rw1)
    equations = [
        sp.Eq(polynomial_a.coeff_monomial(d0 * rw0), 0),
        sp.Eq(polynomial_a.coeff_monomial(d1 * rw1), 0),
    ]
    chi_solutions = sp.solve(equations, chi, dict=True)
    ledger.check("FULL_D_SD_UNIQUE_CHI", chi_solutions, [{chi: 1}])
    ledger.check("A_FULL_D_ZERO_AT_CHI1", orbit_a.subs({chi: 1, mu2: 0}), 0)
    ledger.check(
        "A_OLD_CHI2_NONZERO",
        sp.factor(orbit_a.subs({chi: 2, mu2: 0})),
        512 * (-d0 * rw0 + d1 * rw1) / denominator,
    )
    ledger.check(
        "A_DRED_REMAINDER_CHI1",
        orbit_a.subs(chi, 1),
        512 * mu2 * (-rw0 + rw1) / denominator,
    )

    orbit_b = sp.factor(p2 + k2)
    ledger.check("B_FULL_D_ZERO_AT_CHI1", orbit_b.subs({chi: 1, mu2: 0}), 0)
    ledger.check(
        "B_DRED_REMAINDER_CHI1",
        orbit_b.subs(chi, 1),
        -512 * mu2 * rw2 / denominator,
    )

    # Zero-square nonlinear rows are a different occurrence class.  Their
    # edge tags and routed words coincide pairwise, while coefficients are
    # opposite.  They neither replace nor duplicate K_e.
    je = 512 * rw0 / (d1 * d2)
    jx = -512 * rw0 / (d1 * d2)
    pe = -128 * rw2 / (d0 * d1)
    px = 128 * rw2 / (d0 * d1)
    ledger.check("ZERO_SQUARE_JE_JX_LOCAL_WORD", je + jx, 0)
    ledger.check("ZERO_SQUARE_PE_PX_LOCAL_WORD", pe + px, 0)
    ledger.check("ZERO_SQUARE_JE_JX_MU2_DEFECT", sp.diff(je + jx, mu2), 0)
    ledger.check("ZERO_SQUARE_PE_PX_MU2_DEFECT", sp.diff(pe + px, mu2), 0)

    # Componentwise epsilon contraction has no additional factor two, but
    # the locked Fourier phase exp(i p x) gives P -> i p on each slot.
    # Consequently the momentum-space raw wedge is minus the typed pairing.
    x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
    epsilon_up = sp.Matrix(((0, 1), (-1, 0)))
    x = sp.Matrix((x1, x2))
    y = sp.Matrix((y1, y2))
    raised_y = epsilon_up * y
    pairing = sp.expand((x.T * raised_y)[0])
    raw_wedge = sp.expand(x1 * y2 - x2 * y1)
    ledger.check("TYPED_PAIRING_EQUALS_RAW_WEDGE", pairing, raw_wedge)
    fourier_pairing = sp.expand(
        ((sp.I * x).T * epsilon_up * (sp.I * y))[0]
    )
    ledger.check("FOURIER_TYPED_PAIRING_EQUALS_MINUS_RAW_WEDGE", fourier_pairing, -raw_wedge)

    raw_metric = sp.Integer(32768)
    full_measure = sp.Rational(1, 4)
    antichiral_measure = sp.Rational(1, 2)
    rank_projector = -sp.Rational(1, 2)
    corrected_dword = sp.simplify(
        raw_metric * full_measure * antichiral_measure * rank_projector
    )
    old_dword = sp.simplify(2 * corrected_dword)
    ledger.check("CORRECTED_DWORD_CHI1", corrected_dword, -2048)
    ledger.check("OLD_DWORD_CHI2", old_dword, -4096)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    pred32 = -sp.sqrt(2) * hbar * coupling**4 / 1024
    pred33 = -pred32
    master = 1 / (32 * sp.pi**2)
    external_c_map = coupling**-2
    color = sp.I
    branch32 = sp.simplify(
        pred32
        * corrected_dword
        * sp.Rational(1, 3)
        * master
        * external_c_map
        * color
        / lambda1
    )
    branch33 = sp.simplify(
        pred33
        * corrected_dword
        * sp.Rational(1, 3)
        * master
        * external_c_map
        * color
        / lambda1
    )
    ledger.check("G32_SINGLE_BRANCH_LAMBDA1", branch32, sp.I * sp.sqrt(2) / 3)
    ledger.check("G33_SINGLE_BRANCH_LAMBDA1", branch33, -sp.I * sp.sqrt(2) / 3)
    ledger.check("G32_THREE_BRANCHES_LAMBDA1", 3 * branch32, sp.I * sp.sqrt(2))
    ledger.check("G33_THREE_BRANCHES_LAMBDA1", 3 * branch33, -sp.I * sp.sqrt(2))
    typed32 = -3 * branch32
    typed33 = -3 * branch33
    ledger.check("G32_TYPED_AFTER_FOURIER", typed32, -sp.I * sp.sqrt(2))
    ledger.check("G33_TYPED_AFTER_FOURIER", typed33, sp.I * sp.sqrt(2))

    return {
        "schema": "step5-ab-ba-g3-trace-metric-sd-exact-v1",
        "status": "REJECTED_CONDITIONAL_CONTACT_NORMALIZATION__CHI_ONE_NOT_DERIVED",
        "external_target_used": False,
        "pro_adjudication": {
            "conditional_only": (
                "if K0,K1,K2 have common-unit coefficients +512,-512,+512, "
                "then the full-d equations fix chi=1"
            ),
            "rejected": (
                "the absolute K Hessian/Taylor/Wick multiplicities were not "
                "derived in the same units as the two-axis parent trace"
            ),
            "corrected_naming": (
                "K0,K1,K2 are kinetic derivative-of-action cuts; "
                "JE/JX/PE/PX are separate zero-square nonlinear rows"
            ),
            "delta_B": "NOT_CLOSED_UNTIL_RAW_K_MULTIPLICITY_REPLAY",
        },
        "raw_replay": {
            "W0": "W12",
            "W1": "W(P0)",
            "W2": "W(p0)=W01",
            "A_parent_chi2": "-1024*det4(r0)*W0+1024*det4(r1)*W1",
            "B_parent_chi2": "-1024*det4(r2)*W2",
            "K_cores": {"K0": "+512*W0", "K1": "-512*W1", "K2": "+512*W2"},
        },
        "occurrence_denominators": {
            "K0": ["D1", "D2"],
            "K1": ["D0", "D2"],
            "K2": ["D0", "D1"],
            "JE_JX": {"collapsed_edge": "e0", "sum": "0"},
            "PE_PX": {"collapsed_edge": "e2", "sum": "0"},
        },
        "chi_equation": {
            "A_full_d_coefficients": ["1-chi", "chi-1"],
            "unique_solution": "chi=1",
            "old_chi2_residual": "512*(-D0*RW0+D1*RW1)/(D0*D1*D2)",
        },
        "dred_remainders_common_units": {
            "A": "+512*mu2*(-RW0+RW1)/(D0*D1*D2)",
            "B": "-512*mu2*RW2/(D0*D1*D2)",
            "sum": "+512*mu2*(-RW0+RW1-RW2)/(D0*D1*D2)",
        },
        "normalization": {
            "Dword": "32768*(1/4)*(1/2)*(-1/2)=-2048",
            "epsilon_contraction_factor": "1",
            "fourier_raw_wedge_to_typed_pairing": "-1",
            "conditional_chi1_raw_wedge": {
                "G32": "+i*sqrt(2)",
                "G33": "-i*sqrt(2)"
            },
            "conditional_chi1_typed": {
                "G32_C2_gt_C3": "-i*sqrt(2)",
                "G33_C3_gt_C2": "+i*sqrt(2)"
            },
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    return r"""# AB/BA G3 trace/metric and full-d SD audit

$$
D_e=r_{e,d}^2,\qquad \bar r_e^2=D_e+\mu_\ell^2,\qquad
P_D=D_0D_1D_2.
$$

$$
W_0=W_{12},\qquad W_1=W_{P0},\qquad W_2=W_{p0}=W_{01}.
$$

The kinetic cuts and zero-square currents are different occurrences:

$$
K_0=\frac{512W_0}{D_1D_2},\qquad
K_1=-\frac{512W_1}{D_0D_2},\qquad
K_2=\frac{512W_2}{D_0D_1}.
$$

$$
JE+JX=0,\qquad PE+PX=0,
$$

and the latter pair has no independent $\mu_\ell^2$ remainder.

With an unfixed trace/metric factor $\chi$,

$$
\begin{aligned}
\mathfrak O_A(\chi)
=\frac{512}{P_D}\big[&(1-\chi)D_0W_0
+(\chi-1)D_1W_1\\
&+\chi\mu_\ell^2(-W_0+W_1)\big].
\end{aligned}
$$

The two routed words are independent before integration.  At
$\mu_\ell^2=0$,

$$
1-\chi=0,\qquad \chi-1=0,
$$

so

$$
\boxed{\chi=1.}
$$

The $B$ occurrence closes independently:

$$
-512\frac{(D_2+\mu_\ell^2)W_2}{P_D}
+\frac{512W_2}{D_0D_1}
=-512\frac{\mu_\ell^2W_2}{P_D}.
$$

This cancellation is conditional on the displayed $K_2$ normalization.  Its
raw Hessian/Taylor/Wick multiplicity has not yet been derived in the same unit
as the parent trace, so $\Delta_B$ is not closed by this artifact.

The algebraic component contraction is

$$
(P_{\dot1}C_2)(P^{\dot1}C_3)
+(P_{\dot2}C_2)(P^{\dot2}C_3)
=(P_{\dot1}C_2)(P_{\dot2}C_3)
-(P_{\dot2}C_2)(P_{\dot1}C_3),
$$

With Fourier phase $e^{ipx}$,

$$
P_{\dot a}\longmapsto ip_{\dot a},\qquad
\langle C_2,C_3\rangle_{\rm Fourier}
=-(p_{\dot1}q_{\dot2}-p_{\dot2}q_{\dot1})C_2C_3.
$$

Thus raw momentum wedge to typed pairing carries factor $-1$.

$$
32768\left(\frac14\right)\left(\frac12\right)
\left(-\frac12\right)=-2048.
$$

For each simplex branch,

$$
G_{32}^{(e)}=\frac{i\sqrt2}{3}\lambda_1,qquad
G_{33}^{(e)}=-\frac{i\sqrt2}{3}\lambda_1.
$$

Conditionally at $\chi=1$, the raw-wedge coefficients are opposite to the
typed coefficients.  Therefore

$$
\boxed{G_{32}^{\rm typed}=-i\sqrt2\lambda_1,\qquad
G_{33}^{\rm typed}=+i\sqrt2\lambda_1.}
$$

The $\chi=1$ inference itself is rejected until the raw $K_e$ multiplicities
are replayed without fitting them to the SD equation.
"""


def canonical(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    if args.write:
        JSON_OUT.write_text(canonical(payload), encoding="utf-8")
        MD_OUT.write_text(markdown(payload), encoding="utf-8")
    if args.check:
        if json.loads(JSON_OUT.read_text(encoding="utf-8")) != payload:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != markdown(payload):
            raise AssertionError(f"stale artifact: {MD_OUT}")
    if args.print_json:
        print(canonical(payload), end="")
    else:
        print("PASS conditional chi=1 algebra under assumed K normalization")
        print("PASS K0/K1/K2 distinct from zero-square current pairs")
        print("REJECT chi=1 until raw K multiplicities are derived")
        print("PASS Fourier raw-wedge to typed-pairing sign -1")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
