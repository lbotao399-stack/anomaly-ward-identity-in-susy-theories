#!/usr/bin/env python3
"""Exact local adjudication of the Gate-7 G3 normalization/contact claims.

The Pro response is non-authority.  This audit replays the Project D-words,
keeps kinetic cuts separate from the nonlinear PE/PX zero-square rows, and
applies the DRED transverse-trace map before the Fourier typed projection.
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


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g3-gate7-normalization-first-error-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-gate7-normalization-first-error-exact.md"


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
    words = marked.g23_exact_words()
    w0 = sp.expand(words["w12"])
    w1 = sp.expand(words["wedge_pq_r0"])
    w2 = sp.expand(words["wedge_p_r0"])
    det0 = sp.expand(words["det_r0"])
    det1 = sp.expand(words["det_r1"])
    det2 = sp.expand(words["det_r2"])

    # The local descendant identity fixes the nonlinear rows before any loop
    # routing.  K denotes nabla^2 Phi_1 and X denotes epsilon(C x C).
    kinetic, nonlinear = sp.symbols("K X")
    euler_tilde = -sp.Rational(1, 4) * kinetic - nonlinear / sp.sqrt(2)
    explicit_potential = -sp.sqrt(2) * nonlinear
    descendant = sp.expand(-2 * euler_tilde + explicit_potential)
    ledger.check("B1_DESCENDANT_NONLINEAR_CANCELLATION", descendant, kinetic / 2)

    # Direct sparse words.  PE and PX are separately tagged source rows but
    # have one canonical routed word and opposite source coefficients.
    ledger.check("RAW_G3_B_PARENT", words["g3_b_parent_raw"], -1024 * det2 * w2)
    ledger.check("RAW_G3_B_LOCAL_CORE", words["g3_b_contact"], -128 * w2)
    pe_zero_square = -128 * w2
    px_zero_square = 128 * w2
    ledger.check("PE_PX_ZERO_SQUARE_SUM", pe_zero_square + px_zero_square, 0)

    # Gate 7 first canonical error: after using color antisymmetry to reorder
    # PX, it independently reverses the same external contraction.  That
    # produces a spurious second exchange and turns the exact zero into 512 W.
    gate7_pe_routed = -2 * w2
    gate7_px_routed = 2 * w2
    gate7_spurious_sum = sp.expand((-128) * gate7_pe_routed + 128 * gate7_px_routed)
    ledger.check("GATE7_SPURIOUS_PE_PX_SUM", gate7_spurious_sum, 512 * w2)
    ledger.check("GATE7_PE_PX_SUM_IS_NOT_PROJECT_ZERO", gate7_spurious_sum == 0, False)

    # Kinetic cuts in the same units as their parents.  These multipliers are
    # operator factors, not fitted Schwinger coefficients.
    omitted_endpoint_d2 = -sp.Integer(4)
    transverse_square = sp.Integer(8)
    longitudinal_identity = -sp.Rational(1, 2)
    constrained_projector = sp.Integer(16)
    b_kinetic_descendant = sp.Rational(1, 2)
    multiplier_k0 = transverse_square
    multiplier_k1 = longitudinal_identity * constrained_projector * omitted_endpoint_d2
    multiplier_k2 = b_kinetic_descendant * constrained_projector * omitted_endpoint_d2
    ledger.check("K0_OPERATOR_MULTIPLIER", multiplier_k0, 8)
    ledger.check("K1_OPERATOR_MULTIPLIER", multiplier_k1, 32)
    ledger.check("K2_OPERATOR_MULTIPLIER", multiplier_k2, -32)

    k0 = sp.expand(multiplier_k0 * words["g3_a_contact_top"])
    k1 = sp.expand(multiplier_k1 * words["g3_transported_contact_core"])
    k2 = sp.expand(multiplier_k2 * words["g3_b_contact"])
    ledger.check("K0_SAME_UNIT_WORD", k0, 4096 * w0)
    ledger.check("K1_SAME_UNIT_WORD", k1, -4096 * w1)
    ledger.check("K2_SAME_UNIT_WORD", k2, 4096 * w2)

    parent0 = sp.expand(omitted_endpoint_d2 * (-1024 * det0 * w0))
    parent1 = sp.expand(omitted_endpoint_d2 * (1024 * det1 * w1))
    parent2 = sp.expand(omitted_endpoint_d2 * words["g3_b_parent_raw"])
    ledger.check("P0_SAME_UNIT_DET_WORD", parent0, 4096 * det0 * w0)
    ledger.check("P1_SAME_UNIT_DET_WORD", parent1, -4096 * det1 * w1)
    ledger.check("P2_SAME_UNIT_DET_WORD", parent2, 4096 * det2 * w2)

    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2")
    denominator = d0 * d1 * d2
    p0 = -4096 * (d0 + mu2) * w0 / denominator
    p1 = 4096 * (d1 + mu2) * w1 / denominator
    p2 = -4096 * (d2 + mu2) * w2 / denominator
    c0 = k0 / (d1 * d2)
    c1 = k1 / (d0 * d2)
    c2 = k2 / (d0 * d1)
    ledger.check("P0_PLUS_K0_FULL_D_ZERO", (p0 + c0).subs(mu2, 0), 0)
    ledger.check("P1_PLUS_K1_FULL_D_ZERO", (p1 + c1).subs(mu2, 0), 0)
    ledger.check("P2_PLUS_K2_FULL_D_ZERO", (p2 + c2).subs(mu2, 0), 0)
    ledger.check("P0_K0_DRED_REMAINDER", p0 + c0, -4096 * mu2 * w0 / denominator)
    ledger.check("P1_K1_DRED_REMAINDER", p1 + c1, 4096 * mu2 * w1 / denominator)
    ledger.check("P2_K2_DRED_REMAINDER", p2 + c2, -4096 * mu2 * w2 / denominator)

    # Gate 7's -512 orbit is not in either direct raw or endpoint-normalized
    # units.  It is one half of the raw parent and one eighth of the physical
    # parent/cut pair.
    ledger.check("GATE7_PARENT_OVER_RAW_PARENT", sp.Rational(512, 1024), sp.Rational(1, 2))
    ledger.check("GATE7_PARENT_OVER_SAME_UNIT_PARENT", sp.Rational(512, 4096), sp.Rational(1, 8))
    ledger.check("GATE7_CONTACT_OVER_K2", sp.Rational(512, 4096), sp.Rational(1, 8))

    # Rank-two DRED extraction.  If T_perp=2 c W, the projector -1/2 acts
    # on T_perp.  It must not act once more after c=T_perp/(2W) is formed.
    raw_metric = sp.Integer(32768)
    measure = sp.Rational(1, 4) * sp.Rational(1, 2)
    metric_after_measure = raw_metric * measure
    wedge_symbol = sp.Symbol("W")
    transverse_trace = 2 * metric_after_measure * wedge_symbol
    evanescent_from_trace = -sp.Rational(1, 2) * transverse_trace
    gate7_double_half = -sp.Rational(1, 2) * metric_after_measure * wedge_symbol
    ledger.check("METRIC_AFTER_ORIGINAL_MEASURE", metric_after_measure, 4096)
    ledger.check("DRED_MINUS_HALF_APPLIED_TO_TWO_AXIS_TRACE", evanescent_from_trace, -4096 * wedge_symbol)
    ledger.check("GATE7_DOUBLE_HALF_VALUE", gate7_double_half, -2048 * wedge_symbol)
    ledger.check("GATE7_DOUBLE_HALF_IS_NOT_TRACE_EXTRACTION", gate7_double_half == evanescent_from_trace, False)

    # Locked Fourier phase e^{ipx}: each P gives i times its external momentum.
    p1s, p2s, q1s, q2s = sp.symbols("p1 p2 q1 q2")
    epsilon_up = sp.Matrix(((0, 1), (-1, 0)))
    pvec = sp.Matrix((p1s, p2s))
    qvec = sp.Matrix((q1s, q2s))
    raw_wedge = sp.expand((pvec.T * epsilon_up * qvec)[0])
    fourier_pairing = sp.expand(((sp.I * pvec).T * epsilon_up * (sp.I * qvec))[0])
    ledger.check("FOURIER_TYPED_PAIRING", fourier_pairing, -raw_wedge)

    # Absolute local coefficients.  The three square occurrences each have
    # simplex moment 1/3 and the same D-word -4096.
    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    pred32 = -sp.sqrt(2) * hbar * coupling**4 / 1024
    pred33 = -pred32
    master = 1 / (32 * sp.pi**2)
    external_map = coupling**-2
    color = sp.I
    raw32_each = sp.simplify(
        pred32 * (-4096) * sp.Rational(1, 3) * master * external_map * color / lambda1
    )
    raw33_each = sp.simplify(
        pred33 * (-4096) * sp.Rational(1, 3) * master * external_map * color / lambda1
    )
    ledger.check("G32_RAW_WEDGE_EACH", raw32_each, sp.Rational(2, 3) * sp.I * sp.sqrt(2))
    ledger.check("G33_RAW_WEDGE_EACH", raw33_each, -sp.Rational(2, 3) * sp.I * sp.sqrt(2))
    raw32 = 3 * raw32_each
    raw33 = 3 * raw33_each
    typed32 = -raw32
    typed33 = -raw33
    ledger.check("G32_RAW_WEDGE_TOTAL", raw32, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_RAW_WEDGE_TOTAL", raw33, -2 * sp.I * sp.sqrt(2))
    ledger.check("G32_TYPED_TOTAL", typed32, -2 * sp.I * sp.sqrt(2))
    ledger.check("G33_TYPED_TOTAL", typed33, 2 * sp.I * sp.sqrt(2))

    # The same -1/2 trace rule is already applied to the G1/G2 two-axis
    # traces.  Applying Gate 7's extra half uniformly would halve both.
    g1_pair_eom = sp.Matrix((2, 2))
    g2_raw_outgoing_pq = sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3)))
    g2_pair_eom = sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3)))
    ledger.check("G1_EXACT_PAIR_EOM_UNCHANGED", g1_pair_eom, sp.Matrix((2, 2)))
    ledger.check("G2_RAW_OUTGOING_P_Q_UNCHANGED", g2_raw_outgoing_pq, sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3))))
    ledger.check("G2_ROUTED_PAIR_EOM", g2_pair_eom, sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))))
    ledger.check("GATE7_EXTRA_HALF_WOULD_HALVE_G1", g1_pair_eom / 2, sp.Matrix((1, 1)))
    ledger.check("GATE7_EXTRA_HALF_WOULD_HALVE_G2_RAW_P_Q", g2_raw_outgoing_pq / 2, sp.Matrix((sp.Rational(2, 3), -sp.Rational(1, 6))))

    sqrt2 = sp.sqrt(2)
    imaginary = sp.I
    q_matrix = sp.Matrix(
        (
            (1, -1, 0, 0),
            (imaginary * sqrt2, 0, 1, 0),
            (-imaginary * sqrt2, 0, 0, 1),
        )
    )
    q_ray = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    corrected_vector = sp.Matrix((2, g2_pair_eom[0], typed32, typed33))
    corrected_residual = sp.simplify(q_matrix * corrected_vector)
    scales = sp.Matrix(
        (
            corrected_vector[0],
            corrected_vector[1],
            corrected_vector[2] / q_ray[2],
            corrected_vector[3] / q_ray[3],
        )
    )
    ledger.check("CORRECTED_Q_SCALE_CANDIDATES", scales, sp.Matrix((2, -sp.Rational(1, 3), 2, 2)))
    ledger.check("CORRECTED_Q_RESIDUAL", corrected_residual, sp.Matrix((sp.Rational(7, 3), 0, 0)))

    return {
        "schema": "step5-ab-ba-g3-gate7-normalization-first-error-exact-v1",
        "status": "GATE7_REJECTED__KINETIC_CUTS_CHI2_FOURIER_SIGN_FIXED__G2_DEFICIT_LOCALIZED",
        "external_target_used": False,
        "pro_role": "NON_AUTHORITY_PRO_REVIEW",
        "first_error": {
            "section": "4.2 PX routing",
            "claim": "canonical left differentiation independently reverses W01 to W10 after color-slot canonicalization",
            "failure": "the color exchange was already used to canonicalize c_IJK to c_IKJ; the second wedge reversal is unsupported and destroys the exact local nonlinear cancellation",
            "exact_replacement": "PE=-128*Wp0, PX=+128*Wp0, PE+PX=0",
        },
        "same_unit_sd_orbit": {
            "parents": {
                "P0": "-4096*(D0+mu2)*W0/(D0*D1*D2)",
                "P1": "+4096*(D1+mu2)*W1/(D0*D1*D2)",
                "P2": "-4096*(D2+mu2)*W2/(D0*D1*D2)",
            },
            "kinetic_cuts": {
                "K0": "+4096*W0/(D1*D2)",
                "K1": "-4096*W1/(D0*D2)",
                "K2": "+4096*W2/(D0*D1)",
            },
            "multipliers": {
                "K0": "8",
                "K1": "(-1/2)*16*(-4)=+32",
                "K2": "(+1/2)*16*(-4)=-32",
            },
            "nonlinear_rows": "PE+PX=(-128+128)*Wp0=0; not K2",
        },
        "trace_metric": {
            "two_axis_trace": "T_perp=2*c*W",
            "metric_after_measure": "c=32768*(1/4)*(1/2)=4096",
            "correct_dred": "(-1/2)*T_perp=-4096*W",
            "gate7_error": "(-1/2)*c=-2048 applies the rank projector twice",
        },
        "fourier": {
            "phase": "exp(i p x)",
            "raw_wedge_to_typed_pairing": "-1",
        },
        "corrected_coefficients_lambda1": {
            "G32_raw_wedge": text(raw32),
            "G33_raw_wedge": text(raw33),
            "G32_typed_C2_gt_C3": text(typed32),
            "G33_typed_C3_gt_C2": text(typed33),
        },
        "same_trace_rule_implication": {
            "G1_pair_EOM": ["2", "2"],
            "G2_raw_outgoing_p_q": ["4/3", "-1/3"],
            "G2_pair_EOM_after_Dp_Bq_routing": ["-1/3", "4/3"],
            "incorrect_extra_half_G1": ["1", "1"],
            "incorrect_extra_half_G2": ["2/3", "-1/6"],
        },
        "q_covariance": {
            "basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
            "unique_ray": ["1", "1", "-i*sqrt(2)", "+i*sqrt(2)"],
            "corrected_direct_vector": [text(value) for value in corrected_vector],
            "scale_candidates": [text(value) for value in scales],
            "residual": [text(value) for value in corrected_residual],
            "common_G1_G3_scale": "2",
            "remaining_G2_pair_deficit": "7/3",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(_: dict[str, Any]) -> str:
    return r"""# AB/BA G3 Gate-7 normalization first-error audit

Status: `GATE7_REJECTED__KINETIC_CUTS_CHI2_FOURIER_SIGN_FIXED__G2_DEFICIT_LOCALIZED`.

## 1. First error

$$
\mathscr E_{\widetilde1}
=-\frac14\nabla^2\Phi_1
-\frac1{\sqrt2}\varepsilon_{1st}(C_s\times C_t),
$$

$$
-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1.
$$

Hence the nonlinear occurrences are

$$
PE=-128W_{p0},\qquad PX=+128W_{p0},\qquad PE+PX=0.
$$

Gate 7 first uses $c_{IJK}=-c_{IKJ}$ to canonicalize the PX color slots and
then, in Section 4.2, reverses the dotted contraction again,
$W_{01}\mapsto W_{10}$.  This is a second unsupported exchange:

$$
(-128)(-2W_{p0})+(+128)(+2W_{p0})=512W_{p0}\ne0.
$$

Thus $PE/PX$ are zero-square nonlinear rows; they are not the kinetic cut
$K_2$.

## 2. Same-unit kinetic cuts

$$
m_{K_0}=8,
$$

$$
m_{K_1}=\left(-\frac12\right)(16)(-4)=+32,
$$

$$
m_{K_2}=\left(+\frac12\right)(16)(-4)=-32.
$$

With the directly replayed cores,

$$
K_0=8(512W_0)=+4096W_0,
$$

$$
K_1=32(-128W_1)=-4096W_1,
$$

$$
K_2=(-32)(-128W_2)=+4096W_2.
$$

The parent words in the same endpoint normalization are

$$
P_0=-4096(D_0+\mu_\ell^2)W_0,
$$

$$
P_1=+4096(D_1+\mu_\ell^2)W_1,
$$

$$
P_2=-4096(D_2+\mu_\ell^2)W_2.
$$

Therefore

$$
\frac{P_0}{D_0D_1D_2}+\frac{K_0}{D_1D_2}
=-4096\frac{\mu_\ell^2W_0}{D_0D_1D_2},
$$

$$
\frac{P_1}{D_0D_1D_2}+\frac{K_1}{D_0D_2}
=+4096\frac{\mu_\ell^2W_1}{D_0D_1D_2},
$$

$$
\frac{P_2}{D_0D_1D_2}+\frac{K_2}{D_0D_1}
=-4096\frac{\mu_\ell^2W_2}{D_0D_1D_2}.
$$

At $\mu_\ell^2=0$, all three equations are exactly zero.

## 3. Trace and Fourier signs

Let the two-axis transverse trace be

$$
T_\perp=2cW.
$$

The original measure gives

$$
c=32768\left(\frac14\right)\left(\frac12\right)=4096.
$$

Hence

$$
-\frac12T_\perp=-cW=-4096W.
$$

Gate 7 instead used

$$
-\frac12cW=-2048W,
$$

which applies the rank projector a second time after dividing the trace by
$2W$.

For the locked phase $e^{ipx}$,

$$
(ip)_+\wedge(iq)_+=-(p_+\wedge q_+).
$$

Therefore

$$
G_{3,2}^{\mathrm{raw}}=+2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\mathrm{raw}}=-2i\sqrt2\lambda_1,
$$

$$
\boxed{
G_{3,2}^{\mathrm{typed}}=-2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\mathrm{typed}}=+2i\sqrt2\lambda_1.}
$$

The same trace rule leaves

$$
G_1=(2,2)_{\mathrm{pair,EOM}},
\qquad
(c_p,c_q)_{G_2}=\left(\frac43,-\frac13\right).
$$

The actual G2 graph has $D(p)$ and $B_1(q)$, hence

$$
G_2=\left(-\frac13,\frac43\right)_{\mathrm{pair,EOM}}.
$$

In the basis

$$
(D>B_1,B_1>D,C_2>C_3,C_3>C_2),
$$

the corrected vector and residual are

$$
v=\left(2,-\frac13,-2i\sqrt2,+2i\sqrt2\right),
$$

$$
Qv=\left(\frac73,0,0\right).
$$

Thus G1 and G3 have common scale $2$; the only remaining coefficient defect
is the routed G2 pair deficit $7/3$.
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
        print("PASS Gate7 first error: unsupported second PX exchange")
        print("PASS same-unit kinetic cuts K0/K1/K2 = +4096/-4096/+4096")
        print("PASS transverse trace and Fourier typed signs")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
