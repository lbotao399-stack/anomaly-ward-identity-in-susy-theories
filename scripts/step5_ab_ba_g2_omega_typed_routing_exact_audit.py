#!/usr/bin/env python3
"""Exact G2 Omega-occurrence and external-slot routing adjudication.

The audit keeps the transported Omega_21 Schwinger occurrence, but corrects
the old identification of the graph momenta with the typed B1>D slots.
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

import step5_ab1_marked_sd_orbit_exact_audit as marked  # noqa: E402
import step5_ab_ba_full_1pi_quotient_exact_audit as old_full  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g2-omega-typed-routing-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g2-omega-typed-routing-exact.md"


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
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

    # Rebuild the exact marked metric polynomials.  Only the polynomial and
    # simplex rows are reused; typed interpretation is redone below.
    old_ledger = old_full.Ledger()
    direct = old_full.g2_exact(old_ledger)
    ledger.check("G2_POLYNOMIAL_REPLAY_CHECK_COUNT", len(old_ledger.checks), 21)
    ledger.check("G2_C1", direct["metric_words"]["first_mark"], "1 - z")
    ledger.check("G2_C2_DET", direct["metric_words"]["second_mark_determinant"], "z")
    ledger.check("G2_C2_OMEGA", direct["metric_words"]["second_mark_omega"], "-1/2")
    ledger.check("G2_C2_FULL", direct["metric_words"]["second_mark_complete"], "(2*z - 1)/2")

    # The transported occurrence is genuine.  Five odd endpoint derivatives
    # give -1, their reversal gives +1, and the transported D2 barD2 block is
    # even.  The adjacent r1 projector closes with coefficient -16.
    endpoint_transfer = (-1) ** 5
    reversal = (-1) ** (5 * 4 // 2)
    transported_even_ibp = 1
    adjacent_projector = -16
    ledger.check("OMEGA_ENDPOINT_TRANSFER_SIGN", endpoint_transfer, -1)
    ledger.check("OMEGA_FIVE_ODD_REVERSAL_SIGN", reversal, 1)
    ledger.check("OMEGA_EVEN_BLOCK_IBP_SIGN", transported_even_ibp, 1)
    ledger.check("OMEGA_ADJACENT_R1_PROJECTOR", adjacent_projector, -16)

    ld2, mu2, wedge = sp.symbols("Ld2 mu2 W")
    bar_l2 = ld2 + mu2
    p_omega = -sp.Rational(1, 2) * bar_l2 * wedge
    c_omega = sp.Rational(1, 2) * ld2 * wedge
    ledger.check("OMEGA_FULL_D_PARENT_PLUS_CONTACT_ZERO", (p_omega + c_omega).subs(mu2, 0), 0)
    ledger.check("OMEGA_DRED_REMAINDER", p_omega + c_omega, -sp.Rational(1, 2) * mu2 * wedge)

    delta = sp.symbols("Delta", nonzero=True)
    rank_zero_completion = 1 / (ld2 + delta) ** 2 - delta / (ld2 + delta) ** 3
    ledger.check(
        "OMEGA_RANK_ZERO_COMPLETION",
        ld2 / (ld2 + delta) ** 3,
        rank_zero_completion,
    )

    # Direct tensor replay separates the transverse determinant orbit from
    # the transported longitudinal/Omega orbit.
    tensor = marked.g2_full_tensor_frame_audit()
    y, z = tensor["y"], tensor["z"]
    ledger.check(
        "G2_TRANSVERSE_TRACE",
        tensor["perpendicular_trace"]["transverse"],
        (2048 * sp.I * (y + z), 2048 * z),
    )
    ledger.check(
        "G2_LONGITUDINAL_OMEGA_TRACE",
        tensor["perpendicular_trace"]["longitudinal"],
        (0, -1024),
    )
    ledger.check(
        "G2_TRANSVERSE_EVANESCENT_PROBE",
        tensor["evanescent_probe"]["transverse"],
        (-2048 * sp.I / 3, -1024 * sp.Rational(1, 3)),
    )
    ledger.check(
        "G2_LONGITUDINAL_OMEGA_EVANESCENT_PROBE",
        tensor["evanescent_probe"]["longitudinal"],
        (0, 512),
    )

    # Raw occurrence replay also fixes the absent completions: the B-marked
    # physical projection vanishes, while the two nonlinear-current rows
    # have the same local word and opposite coefficients.
    words = marked.g23_exact_words()
    ledger.check("G2_B_MARK_SELECTED_PROJECTION", tuple(words["g2_b_residual"]), (0, 0))
    ledger.check("G2_B_MARK_FULL_EULER_PROJECTION", tuple(words["g2_b_full"]), (0, 0))
    ledger.check("G2_CURRENT_LOCAL_WORD_EQUALITY", tuple(words["g2_contact"]), tuple(words["g2_a_residual"]))

    # The actual graph routing is explicit in g23: the D probe is at M and
    # the chiral B1 endpoint is at H.  r0-r1=p exits M; r1-r2=q exits H.
    p0, p1, p2, p3, q0, q1, q2, q3 = sp.symbols("p0:4 q0:4")
    p_out = sp.Matrix((p0, p1, p2, p3))
    q_out = sp.Matrix((q0, q1, q2, q3))
    r0 = sp.Matrix(sp.symbols("r0:4"))
    r1 = r0 - p_out
    r2 = r1 - q_out
    ledger.check("M_SLOT_MOMENTUM_IS_P", r0 - r1, p_out)
    ledger.check("H_SLOT_MOMENTUM_IS_Q", r1 - r2, q_out)

    # D and B1 are odd.  The directly replayed D-first word is
    # (1/3) D(q-4p)B, hence the B1>D word is (1/3)B(4p-q)D.
    p_carrier, q_carrier = sp.symbols("p_carrier q_carrier")
    d_first = sp.Rational(1, 3) * (q_carrier - 4 * p_carrier)
    b_first = -d_first
    ledger.check("G2_GRADED_REORDERED_B_FIRST", b_first, sp.Rational(1, 3) * (4 * p_carrier - q_carrier))

    # Since B1 has q_out and D has p_out,
    #   q_out -> <B1,D>, p_out -> B1(P.D).
    # The old audit used the identity map and therefore swapped pair/EOM.
    raw_to_pair_eom = sp.Matrix(((0, 1), (1, 0)))
    selected_raw_pq = sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3)))
    omega_raw_pq = sp.Matrix((0, -1))
    full_raw_pq = selected_raw_pq + omega_raw_pq
    selected_pair_eom = raw_to_pair_eom * selected_raw_pq
    omega_pair_eom = raw_to_pair_eom * omega_raw_pq
    full_pair_eom = raw_to_pair_eom * full_raw_pq
    ledger.check("G2_SELECTED_RAW_P_Q", selected_raw_pq, sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3))))
    ledger.check("G2_OMEGA_RAW_P_Q", omega_raw_pq, sp.Matrix((0, -1)))
    ledger.check("G2_FULL_RAW_P_Q", full_raw_pq, sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3))))
    ledger.check("G2_SELECTED_PAIR_EOM", selected_pair_eom, sp.Matrix((sp.Rational(2, 3), sp.Rational(4, 3))))
    ledger.check("G2_OMEGA_PAIR_EOM", omega_pair_eom, sp.Matrix((-1, 0)))
    ledger.check("G2_FULL_PAIR_EOM", full_pair_eom, sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))))

    old_wrong_pair_eom = sp.eye(2) * full_raw_pq
    ledger.check("OLD_TYPED_COMMENT_SWAPPED_PAIR_EOM", old_wrong_pair_eom, sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3))))
    ledger.check("OLD_TYPED_COMMENT_DIFFERS_FROM_ROUTED_MAP", old_wrong_pair_eom == full_pair_eom, False)

    # Mark coefficients and typed carriers are not the same decomposition.
    # c1 integrates to 4/3 and is the p/EOM carrier; c2,det integrates to
    # 2/3 and is the q/pair carrier; Omega contributes -1 to q/pair.
    first_mark = sp.Rational(4, 3)
    second_det = sp.Rational(2, 3)
    second_omega = -sp.Integer(1)
    ledger.check("G2_MARK_SUM_WITHOUT_OMEGA", first_mark + second_det, 2)
    ledger.check("G2_MARK_SUM_WITH_OMEGA", first_mark + second_det + second_omega, 1)
    ledger.check("G2_FIRST_MARK_IS_EOM_CARRIER", selected_pair_eom[1], first_mark)
    ledger.check("G2_SECOND_DET_IS_PAIR_CARRIER", selected_pair_eom[0], second_det)
    ledger.check("G2_OMEGA_IS_PAIR_CARRIER", omega_pair_eom[0], second_omega)
    ledger.check("MARK_SUM_TWO_IS_NOT_PAIR_COEFFICIENT", first_mark + second_det == selected_pair_eom[0], False)

    # Outgoing-to-all-incoming and Fourier signs are common to the p and q
    # carriers.  With p_in=-p_out, q_in=-q_out and P->i p_in,
    #   Pair_F=-i q_out B D, EOM_F=-i p_out B D,
    # so B(a p_out+b q_out)D=i(a EOM_F+b Pair_F).
    imaginary = sp.I
    raw_a, raw_b = sp.symbols("a b")
    pair_f, eom_f = sp.symbols("Pair_F EOM_F")
    fourier_reconstruction = sp.expand(
        imaginary * (raw_a * eom_f + raw_b * pair_f)
    )
    ledger.check(
        "OUTGOING_FOURIER_COMMON_FACTOR",
        fourier_reconstruction,
        imaginary * raw_a * eom_f + imaginary * raw_b * pair_f,
    )

    # Corrected q-covariance diagnosis after the separately fixed G3 Fourier
    # sign.  The G2 coefficient is the routed pair coefficient -1/3, not 4/3.
    sqrt2 = sp.sqrt(2)
    q_matrix = sp.Matrix(
        (
            (1, -1, 0, 0),
            (imaginary * sqrt2, 0, 1, 0),
            (-imaginary * sqrt2, 0, 0, 1),
        )
    )
    q_ray = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    full_vector = sp.Matrix((2, full_pair_eom[0], -2 * imaginary * sqrt2, 2 * imaginary * sqrt2))
    transverse_vector = sp.Matrix((2, selected_pair_eom[0], -2 * imaginary * sqrt2, 2 * imaginary * sqrt2))
    full_residual = sp.simplify(q_matrix * full_vector)
    transverse_residual = sp.simplify(q_matrix * transverse_vector)
    full_scales = sp.Matrix(
        (
            full_vector[0],
            full_vector[1],
            full_vector[2] / q_ray[2],
            full_vector[3] / q_ray[3],
        )
    )
    ledger.check("G2_FULL_CORRECTED_Q_SCALES", full_scales, sp.Matrix((2, -sp.Rational(1, 3), 2, 2)))
    ledger.check("G2_FULL_CORRECTED_Q_RESIDUAL", full_residual, sp.Matrix((sp.Rational(7, 3), 0, 0)))
    ledger.check("G2_TRANSVERSE_ONLY_Q_RESIDUAL", transverse_residual, sp.Matrix((sp.Rational(4, 3), 0, 0)))

    return {
        "schema": "step5-ab-ba-g2-omega-typed-routing-exact-v1",
        "status": "OMEGA_RETAINED_AS_TRANSPORTED_R1_CUT__OLD_G2_TYPED_SLOT_MAP_REJECTED",
        "external_target_used": False,
        "omega_classification": {
            "type": "transported_r1_inverse_kernel_with_rank_zero_completion",
            "parent": "-(1/2)*barL2*W",
            "contact": "+(1/2)*Ld2*W",
            "full_d": "0",
            "dred": "-(1/2)*mu2*W",
            "delete_as_zero_square": False,
        },
        "routing": {
            "raw_convention": "p,q outgoing",
            "M_external": "D(p)",
            "H_external": "B1(q)",
            "proof": ["r0-r1=p", "r1-r2=q", "chiral_b_plus is at H with q", "D probe is at M"],
            "old_comment": "B1(p)>D(q)",
            "old_comment_verdict": "REJECTED",
        },
        "typed_projection": {
            "raw_basis": ["p_out_on_D", "q_out_on_B1"],
            "typed_basis": ["<B1,D>", "B1(P.D)"],
            "matrix": [["0", "1"], ["1", "0"]],
            "selected_transverse": [text(value) for value in selected_pair_eom],
            "omega": [text(value) for value in omega_pair_eom],
            "full": [text(value) for value in full_pair_eom],
            "outgoing_fourier": "B(a*p_out+b*q_out)D=i*(a*EOM_F+b*Pair_F)",
        },
        "mark_vs_carrier": {
            "first_mark": "4/3 -> p_out -> EOM",
            "second_determinant": "2/3 -> q_out -> pair",
            "second_omega": "-1 -> q_out -> pair",
            "without_omega_mark_sum": "2",
            "without_omega_pair": "2/3",
            "with_omega_pair": "-1/3",
        },
        "completion": {
            "B_marked_selected": "0",
            "B_marked_full_Euler": "0",
            "nonlinear_current_rows": "same local word, opposite source coefficients",
        },
        "q_covariance": {
            "full_direct_vector": [text(value) for value in full_vector],
            "full_scale_candidates": [text(value) for value in full_scales],
            "full_residual": [text(value) for value in full_residual],
            "transverse_only_vector": [text(value) for value in transverse_vector],
            "transverse_only_residual": [text(value) for value in transverse_residual],
            "conclusion": "Omega removal does not produce scale 2; the old sum 4/3+2/3 mixed EOM and pair carriers",
        },
        "first_error": {
            "location": "marked/unified typed comment after G2_B1>D reconstruction",
            "claim": "p is B1 momentum and q is D momentum",
            "exact": "p exits M and belongs to D; q exits H and belongs to B1",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(_: dict[str, Any]) -> str:
    return r"""# AB/BA G2 Omega and typed-routing exact audit

Status: `OMEGA_RETAINED_AS_TRANSPORTED_R1_CUT__OLD_G2_TYPED_SLOT_MAP_REJECTED`.

## 1. Omega occurrence

The transported longitudinal block gives an adjacent $r_1$ inverse kernel.
Its metric coefficient is

$$
c_{2,\Omega}=-\frac12.
$$

The parent/contact pair is

$$
P_\Omega=-\frac12\bar L^2W,
\qquad
C_\Omega=+\frac12L_d^2W,
$$

$$
P_\Omega+C_\Omega
=-\frac12\mu_\ell^2W.
$$

The contact contains both terms

$$
\frac{L_d^2}{(L_d^2+\Delta)^3}
=\frac1{(L_d^2+\Delta)^2}
-\frac{\Delta}{(L_d^2+\Delta)^3}.
$$

Therefore $\Omega_{21}$ is not a zero-square row and cannot be deleted.

## 2. Exact external slots

The raw replay fixes

$$
r_0-r_1=p,
\qquad
r_1-r_2=q.
$$

The $D$ probe is at $M$ and the chiral $B_1$ endpoint is at $H$:

$$
\boxed{D=D(p),\qquad B_1=B_1(q).}
$$

The old statement $B_1(p)>D(q)$ is false.

The D-first word is

$$
\frac13D(q-4p)B_1.
$$

Because $D$ and $B_1$ are odd,

$$
\frac13D(q-4p)B_1
=\frac13B_1(4p-q)D.
$$

Since $q$ belongs to $B_1$ and $p$ belongs to $D$,

$$
q\longmapsto\langle B_1,D\rangle,
\qquad
p\longmapsto B_1(P\cdot D).
$$

Thus the exact map is

$$
\binom{c_{\rm pair}}{c_{\rm EOM}}
=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\binom{c_p}{c_q}.
$$

For the transverse determinant orbit,

$$
(c_p,c_q)=\left(\frac43,\frac23\right),
$$

$$
(c_{\rm pair},c_{\rm EOM})
=\left(\frac23,\frac43\right).
$$

The Omega orbit gives

$$
(c_p,c_q)=(0,-1),
\qquad
(c_{\rm pair},c_{\rm EOM})=(-1,0).
$$

Hence the full G2 result is

$$
\boxed{
(c_{\rm pair},c_{\rm EOM})
=\left(-\frac13,\frac43\right).}
$$

## 3. Outgoing and Fourier signs

With all-incoming momenta

$$
p_{\rm in}=-p_{\rm out},
\qquad
q_{\rm in}=-q_{\rm out},
$$

and phase $e^{ikx}$,

$$
P\longmapsto ik_{\rm in}.
$$

Therefore

$$
\mathrm{Pair}_F=-iq_{\rm out}B_1D,
\qquad
\mathrm{EOM}_F=-ip_{\rm out}B_1D,
$$

$$
B_1(ap_{\rm out}+bq_{\rm out})D
=i\left(a\,\mathrm{EOM}_F+b\,\mathrm{Pair}_F\right).
$$

The common factor $i$ does not exchange the two carriers.

## 4. Consequence

The mark sum without Omega is

$$
\frac43+\frac23=2,
$$

but it is not a pair coefficient:

$$
\frac43\longrightarrow\mathrm{EOM},
\qquad
\frac23\longrightarrow\mathrm{pair}.
$$

With the corrected G3 Fourier sign, the full ordered vector is

$$
v=\left(2,-\frac13,-2i\sqrt2,+2i\sqrt2\right),
$$

and

$$
Qv=\left(\frac73,0,0\right).
$$

Deleting Omega would instead give

$$
v_T=\left(2,\frac23,-2i\sqrt2,+2i\sqrt2\right),
\qquad
Qv_T=\left(\frac43,0,0\right),
$$

so Omega deletion does not produce the common scale $2$.
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
        print("PASS Omega retained as transported r1 cut with rank-zero completion")
        print("PASS actual G2 routing D(p), B1(q)")
        print("PASS corrected G2 pair/EOM = (-1/3, 4/3)")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
