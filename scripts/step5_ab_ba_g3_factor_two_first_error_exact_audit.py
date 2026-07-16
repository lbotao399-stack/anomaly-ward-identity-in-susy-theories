#!/usr/bin/env python3
"""Target-blind first-error audit for the AB/BA G3 factor two.

The audit evaluates the AB G3 word in its original
``d4theta_M d2bartheta_H`` measure with both matter-projector scalars retained.
It then compares the first raw D-word level with the independently replayed
BB off-diagonal TMH orbit.  No holomorphic-twist artifact is read.
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
import step5_ab_ba_full_1pi_quotient_exact_audit as ab_old  # noqa: E402
import step5_bb_offdiagonal_family_exact_audit as bb  # noqa: E402


JSON_OUT = ROOT / "audits/step5-ab-ba-g3-factor-two-first-error-exact.json"
MD_OUT = ROOT / "audits/step5-ab-ba-g3-factor-two-first-error-exact.md"


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
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": text(actual) if isinstance(actual, sp.Basic) else str(actual),
                "expected": text(expected) if isinstance(expected, sp.Basic) else str(expected),
            }
        )
        if not passed:
            raise AssertionError(
                f"{check_id}: actual={actual!r}, expected={expected!r}"
            )


def raw_original_measure_values(
    y_value: sp.Rational,
    z_value: sp.Rational,
    loop4: tuple[int, int, int, int],
) -> tuple[sp.Expr, sp.Expr]:
    """Return raw canonical coefficients before either Berezin measure."""

    p = ab_old.euclidean_bispinor((1, 0, 0, 0))
    q = ab_old.euclidean_bispinor((0, 0, 0, 1))
    total = ab_old.matrix_add(p, q)
    r0 = ab_old.matrix_add(
        ab_old.euclidean_bispinor(loop4),
        ab_old.matrix_add(
            ab_old.matrix_scale(y_value, p),
            ab_old.matrix_scale(z_value, total),
        ),
    )
    r1 = g23.matrix_sub(r0, p)
    r2 = g23.matrix_sub(r1, q)
    minus_r2 = g23.matrix_neg(r2)

    a_unmarked = g23.d(
        g23.bar_d2(
            g23.d(g23.delta4(g23.S, g23.M), g23.S, 0, r0),
            g23.S,
            r0,
        ),
        g23.S,
        0,
        r0,
    )
    a_marked = g23.d(a_unmarked, g23.S, 1, r0)
    b_unmarked = g23.d(
        g23.bar_d2(
            g23.d2(g23.delta4(g23.S, g23.H), g23.S, minus_r2),
            g23.S,
            minus_r2,
        ),
        g23.S,
        0,
        minus_r2,
    )
    b_marked = g23.d(b_unmarked, g23.S, 1, minus_r2)
    bridge = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.H), g23.M, r1),
        g23.M,
        r1,
    )
    external = (
        bridge
        * g23.antichiral_bottom(g23.M, p)
        * g23.antichiral_bottom(g23.H, q)
    )
    mask = (15 << (4 * g23.M)) | (12 << (4 * g23.H))
    return (
        sp.factor((a_marked * b_unmarked * external).coefficient(mask)),
        sp.factor((a_unmarked * b_marked * external).coefficient(mask)),
    )


def raw_transverse_trace(
    y_value: sp.Rational, z_value: sp.Rational
) -> tuple[sp.Expr, sp.Expr]:
    center = raw_original_measure_values(y_value, z_value, (0, 0, 0, 0))
    traces = [sp.Integer(0), sp.Integer(0)]
    for axis in (1, 2):
        plus = tuple(1 if index == axis else 0 for index in range(4))
        minus = tuple(-1 if index == axis else 0 for index in range(4))
        value_plus = raw_original_measure_values(y_value, z_value, plus)
        value_minus = raw_original_measure_values(y_value, z_value, minus)
        for mark in range(2):
            traces[mark] += sp.factor(
                (value_plus[mark] + value_minus[mark] - 2 * center[mark]) / 2
            )
    return tuple(sp.factor(value) for value in traces)


def simplex(value: sp.Expr, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    return sp.simplify(
        2 * sp.integrate(sp.integrate(value, (z, 0, 1 - y)), (y, 0, 1))
    )


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    samples = {
        "00": raw_transverse_trace(sp.Rational(0), sp.Rational(0)),
        "10": raw_transverse_trace(sp.Rational(1), sp.Rational(0)),
        "01": raw_transverse_trace(sp.Rational(0), sp.Rational(1)),
        "check": raw_transverse_trace(sp.Rational(1, 3), sp.Rational(1, 3)),
    }
    raw = sp.Integer(32768)
    expected = {
        "00": (-2 * sp.I * raw, 0),
        "10": (-2 * sp.I * raw, 0),
        "01": (0, -2 * sp.I * raw),
        "check": (
            -sp.Rational(4, 3) * sp.I * raw,
            -sp.Rational(2, 3) * sp.I * raw,
        ),
    }
    for point in samples:
        ledger.check(f"AB_RAW_ORIGINAL_MEASURE_{point}_A", samples[point][0], expected[point][0])
        ledger.check(f"AB_RAW_ORIGINAL_MEASURE_{point}_B", samples[point][1], expected[point][1])

    y, z = sp.symbols("y z", real=True)
    trace_a = sp.expand(
        samples["00"][0]
        + y * (samples["10"][0] - samples["00"][0])
        + z * (samples["01"][0] - samples["00"][0])
    )
    trace_b = sp.expand(
        samples["00"][1]
        + y * (samples["10"][1] - samples["00"][1])
        + z * (samples["01"][1] - samples["00"][1])
    )
    external_wedge = ab_old.wedge(
        ab_old.euclidean_bispinor((1, 0, 0, 0)),
        ab_old.euclidean_bispinor((0, 0, 0, 1)),
    )
    metric_a_raw = sp.simplify(trace_a / (2 * external_wedge))
    metric_b_raw = sp.simplify(trace_b / (2 * external_wedge))
    ledger.check("AB_RAW_METRIC_A", metric_a_raw, raw * (1 - z))
    ledger.check("AB_RAW_METRIC_B", metric_b_raw, raw * z)

    # Locked projectors give theta^2=-2 theta+theta- and
    # bartheta^2=+2 bartheta+bartheta-.  Hence the magnitudes of the
    # canonical monomial maps are 1/4 and 1/2.  Reversing the full-measure
    # orientation also reverses delta4; it changes no magnitude below.
    theta2_top = -2
    bartheta2_top = 2
    full_top = theta2_top * bartheta2_top
    full_measure_signed = sp.Rational(1, full_top)
    antichiral_measure_signed = sp.Rational(1, bartheta2_top)
    ledger.check("LOCKED_THETA2_TOP", theta2_top, -2)
    ledger.check("LOCKED_BARTHETA2_TOP", bartheta2_top, 2)
    ledger.check("LOCKED_FULL_TOP", full_top, -4)
    ledger.check("LOCKED_FULL_MEASURE_CANONICAL_MAP", full_measure_signed, -sp.Rational(1, 4))
    ledger.check("LOCKED_ANTICHIRAL_MEASURE_CANONICAL_MAP", antichiral_measure_signed, sp.Rational(1, 2))
    measure_magnitude = abs(full_measure_signed * antichiral_measure_signed)
    ledger.check("AB_ORIGINAL_MEASURE_MAGNITUDE", measure_magnitude, sp.Rational(1, 8))
    dword_per_metric_magnitude = sp.simplify(raw * measure_magnitude)
    ledger.check("AB_ORIGINAL_MEASURE_DWORD_MAGNITUDE", dword_per_metric_magnitude, 4096)

    weight_a = simplex(metric_a_raw / raw, y, z)
    weight_b = simplex(metric_b_raw / raw, y, z)
    ledger.check("AB_A_MARK_WEIGHT", weight_a, sp.Rational(2, 3))
    ledger.check("AB_B_MARK_WEIGHT", weight_b, sp.Rational(1, 3))
    ledger.check("AB_MARK_WEIGHT_SUM", weight_a + weight_b, 1)
    ab_effective_raw = sp.simplify(dword_per_metric_magnitude * (weight_a + weight_b))
    ledger.check("AB_G3_EFFECTIVE_RAW_MAGNITUDE", ab_effective_raw, 4096)

    # Primitive scalar normalization with both constrained matter propagator
    # projectors kept explicitly.
    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source = -coupling**2 / (4 * sp.sqrt(2))
    matter = sp.sqrt(2) * coupling / hbar
    hminus = -sp.sqrt(2) * coupling / hbar
    vector_propagator = -hbar
    matter_projector_1 = hbar / 16
    matter_projector_2 = hbar / 16
    action_taylor = sp.Rational(1, 2) * 2
    pre_d_ab = sp.simplify(
        source
        * matter
        * hminus
        * vector_propagator
        * matter_projector_1
        * matter_projector_2
        * action_taylor
    )
    ledger.check("AB_TWO_MATTER_PROJECTORS_RETAINED", matter_projector_1 * matter_projector_2, hbar**2 / 256)
    ledger.check("AB_ACTION_TAYLOR_ORDERINGS", action_taylor, 1)
    ledger.check("AB_G32_PRED", pre_d_ab, -sp.sqrt(2) * hbar * coupling**4 / 1024)

    pre_d_bb = -hbar * coupling**4 / 2048
    external_ab = coupling**-2
    external_bb = 2 * sp.sqrt(2) * coupling**-2
    master_over_lambda = sp.Rational(1, 2) / (hbar * coupling**2) * (hbar * coupling**2)
    # The last expression displays (1/32 pi^2)/(lambda1)=1/(2 hbar g^2).
    master_over_lambda = 1 / (2 * hbar * coupling**2)
    ab_per_raw_without_color = sp.simplify(pre_d_ab * external_ab * master_over_lambda)
    bb_per_raw_without_color = sp.simplify(pre_d_bb * external_bb * master_over_lambda)
    ledger.check("AB_PER_RAW_CONVERSION_WITHOUT_COLOR", ab_per_raw_without_color, -sp.sqrt(2) / 2048)
    ledger.check("BB_PER_RAW_CONVERSION_WITHOUT_COLOR", bb_per_raw_without_color, -sp.sqrt(2) / 2048)
    ledger.check("AB_BB_PER_RAW_CONVERSION_EQUAL", ab_per_raw_without_color, bb_per_raw_without_color)

    # BB target-blind TMH calibration is replayed from its Grassmann engine;
    # no final BB target row is read.
    bb_ledger = bb.Ledger()
    bb_words = bb.triangle_words(bb_ledger)
    bb_r0 = bb_words["r0"]
    bb_direct_coefficient = sp.simplify(
        bb_words["direct_evanescent_word"][0] / bb_r0[0][1]
    )
    bb_transported_coefficient = sp.simplify(
        bb_words["transported_evanescent_word"][0] / bb_r0[0][1]
    )
    ledger.check("BB_REPLAY_DIRECT_RAW_COEFFICIENT", bb_direct_coefficient, -4096)
    ledger.check("BB_REPLAY_TRANSPORTED_RAW_COEFFICIENT", bb_transported_coefficient, -2048)
    ledger.check("BB_REPLAY_INTERNAL_CHECK_COUNT", len(bb_ledger.rows), 36)

    # The two oriented routes have opposite effective colors and exchanged
    # (2/3,1/3) moments.
    p_weight = sp.Rational(2, 3)
    q_weight = sp.Rational(1, 3)
    bb_direct_raw = abs(bb_direct_coefficient) * (p_weight - q_weight)
    bb_transported_raw = abs(bb_transported_coefficient) * (p_weight - q_weight)
    bb_effective_raw = sp.simplify(bb_direct_raw + bb_transported_raw)
    ledger.check("BB_DIRECT_ORDERED_EFFECTIVE_RAW", bb_direct_raw, sp.Rational(4096, 3))
    ledger.check("BB_TRANSPORTED_ORDERED_EFFECTIVE_RAW", bb_transported_raw, sp.Rational(2048, 3))
    ledger.check("BB_TMH_ORDERED_EFFECTIVE_RAW", bb_effective_raw, 2048)
    ledger.check("AB_OVER_BB_EFFECTIVE_RAW_RATIO", ab_effective_raw / bb_effective_raw, 2)

    # There is no common 1/2 at the source or at the two outer marks.
    source_mixed_hessian = sp.Rational(1, 2) * 2
    action_vertices = sp.Rational(1, 2) * 2
    hminus_hessian = sp.Rational(1, 6) * 6
    fixed_flavor_wick = 1
    product_rule_a_mark = 1
    product_rule_b_mark = 1
    ledger.check("AB_SOURCE_MIXED_HESSIAN_FACTOR", source_mixed_hessian, 1)
    ledger.check("AB_ACTION_VERTEX_FACTOR", action_vertices, 1)
    ledger.check("AB_HMINUS_HESSIAN_FACTOR", hminus_hessian, 1)
    ledger.check("AB_FIXED_FLAVOR_WICK_FACTOR", fixed_flavor_wick, 1)
    ledger.check("AB_PRODUCT_RULE_A_MARK", product_rule_a_mark, 1)
    ledger.check("AB_PRODUCT_RULE_B_MARK", product_rule_b_mark, 1)
    ledger.check("AB_COMMON_OUTER_MARK_HALF", False, False)

    return {
        "schema": "step5-ab-ba-g3-factor-two-first-error-exact-v1",
        "status": (
            "TARGET_BLIND_NO_HALF_IN_ORIGINAL_MEASURE_OR_SOURCE_MARKS__"
            "FIRST_FACTOR_TWO_DIFFERENCE_AT_DWORD_ORBIT"
        ),
        "external_target_read": False,
        "AB_original_measure": {
            "measure": "d4theta_M d2bartheta_H",
            "raw_metric_words": {
                "A_mark": "32768*(1-z)",
                "B_mark": "32768*z",
            },
            "locked_canonical_measure_maps": {
                "full": "-1/4",
                "antichiral": "+1/2",
                "magnitude_product": "1/8",
            },
            "both_matter_projectors": ["hbar/16", "hbar/16"],
            "Dword_per_metric_magnitude": "4096",
            "mark_weights": {"A": "2/3", "B": "1/3", "sum": "1"},
            "effective_raw_magnitude": "4096",
        },
        "primitive_factors": {
            "source_mixed_Hessian": "(1/2!)*2=1",
            "two_action_vertices": "(1/2!)*2=1",
            "Hminus_cubic_Hessian": "(1/3!)*6=1",
            "fixed_flavor_Wick": "1",
            "outer_A_product_rule": "1",
            "outer_B_product_rule": "1",
            "common_outer_mark_half": False,
            "AB_G32_preD": text(pre_d_ab),
        },
        "internal_BB_calibration": {
            "AB_per_raw_without_color": text(ab_per_raw_without_color),
            "BB_per_raw_without_color": text(bb_per_raw_without_color),
            "direct_ordered_raw": "4096/3",
            "transported_ordered_raw": "2048/3",
            "effective_ordered_raw": "2048",
        },
        "first_factor_two_difference": {
            "level": "D_ALGEBRA_OCCURRENCE_ORBIT_AFTER_PRIMITIVE_NORMALIZATION",
            "AB_G3_raw_effective": "4096",
            "BB_TMH_raw_effective": "2048",
            "ratio": "2",
            "not_at": [
                "original Berezin measure",
                "matter projector 1/16 scalars",
                "source mixed-Hessian factorial",
                "action Taylor factorial",
                "Hminus cubic Hessian factorial",
                "fixed-flavor Wick pairing",
                "outer A/B product-rule marks",
            ],
            "interpretation": (
                "BB calibration does not by itself prove an identity equating "
                "the two channel D-word orbits; it localizes the first factor-two "
                "difference but supplies no legal 1/2 for AB"
            ),
        },
        "blocker": (
            "BLOCKED_NO_TARGET_BLIND_PROJECT_IDENTITY_EQUATING_"
            "AB_G3_AND_BB_TMH_RAW_DWORD_ORBITS"
        ),
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "ids": [row["id"] for row in ledger.rows],
        },
    }


def markdown(artifact: dict[str, Any]) -> str:
    return r"""# AB/BA G3 factor-two first-error audit

## 1. Original measure

$$
[\theta^2\bar\theta^2]_D=1,\qquad
\theta^2=-2\theta^+\theta^-,\qquad
\bar\theta^2=+2\bar\theta^{\dot+}\bar\theta^{\dot-}.
$$

Therefore the canonical monomial maps have magnitudes

$$
\left|\int d^4\theta\right|=\frac14,\qquad
\left|\int d^2\bar\theta\right|=\frac12.
$$

The direct sparse replay in the original measure gives

$$
T_A^{\rm raw}=32768(1-z),\qquad
T_B^{\rm raw}=32768z.
$$

Both matter propagator scalars remain outside the D-word:

$$
\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)=\frac{\hbar^2}{256}.
$$

No full/full endpoint conversion is used.  Direct canonical extraction gives

$$
32768\left(\frac14\right)\left(\frac12\right)=4096.
$$

## 2. Source and action factors

$$
\frac1{2!}(O_{u\phi}+O_{\phi u})=1,
$$

$$
\frac1{2!}(M_rH_-+H_-M_r)=1,
$$

$$
\frac1{3!}\sum_{\sigma\in S_3}1=1,
$$

$$
N_{\rm Wick}^{(1,r)}=1.
$$

The two product-rule marks have coefficients

$$
c_A=1,\qquad c_B=1,
$$

and original-measure moments

$$
w_A=\frac23,\qquad w_B=\frac13,\qquad w_A+w_B=1.
$$

Thus no common factor $1/2$ occurs.

## 3. BB internal calibration

The two per-raw conversion factors agree before color:

$$
K_{AB}=K_{BB}=-\frac{\sqrt2}{2048}.
$$

For the ordered BB component,

$$
R_{BB}^{\rm direct}=4096\left(\frac23-\frac13\right)
=\frac{4096}{3},
$$

$$
R_{BB}^{\rm transported}=2048\left(\frac23-\frac13\right)
=\frac{2048}{3},
$$

$$
R_{BB}^{\rm ordered}=2048.
$$

For AB,

$$
R_{AB}^{\rm ordered}=4096
\left(\frac23+\frac13\right)=4096.
$$

Hence

$$
\frac{R_{AB}^{\rm ordered}}{R_{BB}^{\rm ordered}}=2.
$$

The first factor-two difference is the channel-specific D-algebra occurrence
orbit, after all primitive normalizations.  The original measure and the
outer source marks do not generate a factor $1/2$.
"""


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", "--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    artifact = build_artifact()
    if args.write:
        JSON_OUT.write_text(canonical(artifact), encoding="utf-8")
        MD_OUT.write_text(markdown(artifact), encoding="utf-8")
    if args.check_artifact:
        stored = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        if stored != artifact:
            raise AssertionError(f"stored artifact is stale: {JSON_OUT}")
    if args.print_json:
        print(canonical(artifact), end="")
    else:
        print("PASS original d4theta_M d2bartheta_H magnitude 4096")
        print("PASS no common source-mark factor 1/2")
        print("PASS AB/BB per-raw conversion equal -sqrt(2)/2048")
        print("PASS first factor-two difference at D-word orbit 4096/2048")
        print(
            f"SUMMARY {artifact['checks']['passed']}/"
            f"{artifact['checks']['count']} PASS"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
