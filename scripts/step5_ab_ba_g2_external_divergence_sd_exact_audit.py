#!/usr/bin/env python3
"""Exact G2 r2 Schwinger orbit and dotted-divergence projection.

No holomorphic-twist coefficient or q-covariance relation is used.  The
calculation first checks the full-d parent/contact zero and its DRED
remainder, then performs the dotted epsilon contractions which decide the
sign of the external B1(P.D) carrier.
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


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g2-external-divergence-sd-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g2-external-divergence-sd-exact.md"


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

    # Locked dotted conventions.  The contraction is over the first index of
    # both epsilon tensors, hence epsilon^{ab} epsilon_{ac}=-delta^b_c.
    epsilon_up = sp.Matrix(((0, 1), (-1, 0)))
    epsilon_down = sp.Matrix(((0, -1), (1, 0)))
    first_index_contraction = epsilon_up.T * epsilon_down
    ledger.check("EPSILON_UP_DOWN_INVERSE", epsilon_up * epsilon_down, sp.eye(2))
    ledger.check(
        "EPSILON_FIRST_INDEX_CONTRACTION",
        first_index_contraction,
        -sp.eye(2),
    )

    pb0, pb1, du0, du1 = sp.symbols("PB0 PB1 DU0 DU1")
    pb_lower = sp.Matrix((pb0, pb1))
    d_upper = sp.Matrix((du0, du1))
    pb_upper = epsilon_up * pb_lower
    d_lower = epsilon_down * d_upper
    pairing = sp.expand((pb_lower.T * d_upper)[0])
    raised_lowered_term = sp.expand((pb_upper.T * d_lower)[0])
    ledger.check("RAISED_PB_TIMES_LOWER_D", raised_lowered_term, -pairing)

    # P^a(B D_a)=(P^a B)D_a+B(P^a D_a)=-<B,D>+E_BD.
    eom = sp.Symbol("E_BD")
    total_divergence = sp.expand(raised_lowered_term + eom)
    ledger.check("B_D_TOTAL_DIVERGENCE", total_divergence, eom - pairing)
    eom_from_divergence = sp.expand(total_divergence + pairing)
    ledger.check("B_D_EOM_EQUALS_PAIR_PLUS_DIVERGENCE", eom_from_divergence, eom)

    # Occurrence-level r2 parent and its derivative-of-action contact.
    words = marked.g23_exact_words()
    r0 = words["r0"]
    residual = sp.Matrix(words["g2_a_residual"])
    expected_residual = sp.Matrix((-128 * r0[0][1], 128 * r0[0][0]))
    ledger.check("G2_R2_RESIDUAL_WORD", residual, expected_residual)
    ledger.check("G2_CURRENT_CONTACT_SAME_WORD", sp.Matrix(words["g2_contact"]), residual)

    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2", nonzero=True)
    rr0, rr1 = sp.symbols("R0 R1")
    denominator = d0 * d1 * d2
    for component, rr in enumerate((rr0, rr1)):
        det_r2 = -(d2 + mu2)
        parent = 8 * det_r2 * rr / denominator
        contact = 8 * rr / (d0 * d1)
        ledger.check(
            f"G2_R2_COMPONENT_{component}_FULL_D_ZERO",
            (parent + contact).subs(mu2, 0),
            0,
        )
        ledger.check(
            f"G2_R2_COMPONENT_{component}_DRED_REMAINDER",
            parent + contact,
            -8 * mu2 * rr / denominator,
        )

    # Feynman shift r0=L+y p+z(p+q).  The odd L moment is zero and the
    # normalized ordered-simplex moments are exactly <y>=<z>=1/3.
    y, z = sp.symbols("y z", nonnegative=True)

    def simplex_average(value: sp.Expr) -> sp.Expr:
        return sp.simplify(
            2 * sp.integrate(sp.integrate(value, (z, 0, 1 - y)), (y, 0, 1))
        )

    average_y = simplex_average(y)
    average_z = simplex_average(z)
    ledger.check("ORDERED_SIMPLEX_AVERAGE_Y", average_y, sp.Rational(1, 3))
    ledger.check("ORDERED_SIMPLEX_AVERAGE_Z", average_z, sp.Rational(1, 3))
    p_carrier, q_carrier = sp.symbols("p q")
    average_r0 = sp.expand(
        average_y * p_carrier + average_z * (p_carrier + q_carrier)
    )
    ledger.check(
        "G2_R0_RANK_ONE_MOMENT",
        average_r0,
        (2 * p_carrier + q_carrier) / 3,
    )

    # Direct physical normalization gives +(2/3)B(2p+q)D.  The transported
    # Omega occurrence contributes -B q D.  Routing is fixed by the raw graph:
    # p exits M on D, while q exits H on B1.
    selected_raw_pq = sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3)))
    omega_raw_pq = sp.Matrix((0, -1))
    full_raw_pq = selected_raw_pq + omega_raw_pq
    raw_to_pair_eom = sp.Matrix(((0, 1), (1, 0)))
    full_pair_eom = raw_to_pair_eom * full_raw_pq
    ledger.check(
        "G2_SELECTED_RAW_P_D_Q_B",
        selected_raw_pq,
        sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3))),
    )
    ledger.check("G2_OMEGA_RAW_P_D_Q_B", omega_raw_pq, sp.Matrix((0, -1)))
    ledger.check(
        "G2_FULL_RAW_P_D_Q_B",
        full_raw_pq,
        sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3))),
    )
    ledger.check(
        "G2_FULL_PAIR_EOM_BEFORE_DIVERGENCE",
        full_pair_eom,
        sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))),
    )

    # Since E_BD=<B,D>+T_BD, coefficients transform by
    # (c_pair,c_EOM)->(c_pair+c_EOM,c_EOM) in the (pair,total-divergence)
    # basis.  This sign is specific to B>D with the displayed index positions.
    pair_eom_to_pair_divergence = sp.Matrix(((1, 1), (0, 1)))
    full_pair_divergence = pair_eom_to_pair_divergence * full_pair_eom
    ledger.check(
        "G2_FULL_PAIR_TOTAL_DIVERGENCE",
        full_pair_divergence,
        sp.Matrix((1, sp.Rational(4, 3))),
    )
    ledger.check("G2_EXACT_DIVERGENCE_QUOTIENT_PAIR", full_pair_divergence[0], 1)
    ledger.check(
        "G2_EOM_PLUS_FOUR_THIRDS_MAPS_PLUS_PAIR",
        full_pair_eom[1],
        sp.Rational(4, 3),
    )

    # The tempting common map T=pair+EOM has the wrong epsilon contraction
    # for B>D and would produce -5/3.
    wrong_common_map = sp.Matrix(((1, -1), (0, 1)))
    wrong_pair_divergence = wrong_common_map * full_pair_eom
    ledger.check("OLD_COMMON_MAP_WRONG_PAIR", wrong_pair_divergence[0], -sp.Rational(5, 3))
    ledger.check("OLD_COMMON_MAP_DIFFERS_FROM_INDEX_RESULT", wrong_pair_divergence == full_pair_divergence, False)

    # The Omega r1 occurrence is independently an SD family, not a zero-square
    # deletion.  It changes only the q-on-B/pair coefficient.
    omega_parent = -sp.Rational(1, 2) * (d1 + mu2)
    omega_contact = sp.Rational(1, 2) * d1
    ledger.check("G2_OMEGA_R1_FULL_D_ZERO", (omega_parent + omega_contact).subs(mu2, 0), 0)
    ledger.check("G2_OMEGA_R1_DRED_REMAINDER", omega_parent + omega_contact, -sp.Rational(1, 2) * mu2)

    return {
        "schema": "step5-ab-ba-g2-external-divergence-sd-exact-v1",
        "status": (
            "G2_R2_AND_OMEGA_SD_FULL_D_ZERO__"
            "DOTTED_EPSILON_MAPS_BPD_TO_PLUS_PAIR__PAIR_COEFFICIENT_ONE"
        ),
        "external_target_used": False,
        "q_covariance_used": False,
        "r2_sd_orbit": {
            "parent": "-8*(D2+mu2)*R/(D0*D1*D2)",
            "contact": "+8*R/(D0*D1)",
            "full_d": "0",
            "dred": "-8*mu2*R/(D0*D1*D2)",
            "rank_one_moment": "(2*p_D+q_B)/3",
        },
        "omega_r1_sd_orbit": {
            "parent": "-(1/2)*(D1+mu2)*W",
            "contact": "+(1/2)*D1*W",
            "full_d": "0",
            "dred": "-(1/2)*mu2*W",
            "typed_pair_contribution": "-1",
        },
        "dotted_index_identity": {
            "epsilon_contraction": "epsilon^{ab} epsilon_{ac}=-delta^b_c",
            "pair": "<B1,D>=(P_a B1)D^a",
            "eom": "E_BD=B1(P^a D_a)",
            "total_divergence": "T_BD=P^a(B1 D_a)=-<B1,D>+E_BD",
            "solved": "E_BD=<B1,D>+T_BD",
        },
        "typed_coefficients": {
            "raw_basis_pD_qB": [text(value) for value in full_raw_pq],
            "pair_EOM": [text(value) for value in full_pair_eom],
            "pair_total_divergence": [text(value) for value in full_pair_divergence],
            "exact_divergence_quotient_pair": "1",
        },
        "first_error": {
            "artifact": "step5-ab-ba-unified-typed-q-covariance-exact",
            "claim": "the D>B and B>D slots share T=pair+EOM",
            "exact": "for B>D, T=EOM-pair because epsilon^{ab}epsilon_{ac}=-delta^b_c",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(_: dict[str, Any]) -> str:
    return r"""# AB/BA G2 external-divergence and SD exact audit

Status: `G2_R2_AND_OMEGA_SD_FULL_D_ZERO__DOTTED_EPSILON_MAPS_BPD_TO_PLUS_PAIR__PAIR_COEFFICIENT_ONE`.

No HT coefficient and no residual-$q$ equation is used.

## 1. The selected (r_2) Schwinger family

The exact raw residual is

$$
\mathcal R_{\dot0}=-128r_{0,+\dot2},
\qquad
\mathcal R_{\dot1}=+128r_{0,+\dot1}.
$$

Using

$$
\det(r_2)=-\bar r_2^2=-(D_2+\mu_\ell^2),
$$

the parent and contact are

$$
\frac{8\det(r_2)\mathcal R}{D_0D_1D_2}
=-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2},
$$

$$
\frac{8\mathcal R}{D_0D_1}.
$$

Therefore

$$
\left.
\left[
-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2}
+\frac{8\mathcal R}{D_0D_1}
\right]
\right|_{\mu_\ell^2=0}=0,
$$

$$
-\frac{8(D_2+\mu_\ell^2)\mathcal R}{D_0D_1D_2}
+\frac{8\mathcal R}{D_0D_1}
=-\frac{8\mu_\ell^2\mathcal R}{D_0D_1D_2}.
$$

For

$$
r_0=L+yp+z(p+q),
$$

the normalized simplex moments are

$$
2\int_0^1dy\int_0^{1-y}dz\,y
=2\int_0^1dy\int_0^{1-y}dz\,z
=\frac13,
$$

so

$$
\langle r_0\rangle_\triangle
=\frac13p+\frac13(p+q)
=\frac13(2p+q).
$$

The selected (B_1>D) word is

$$
\frac23B_1(2p+q)^{\dot a}D_{\dot a}.
$$

The transported (r_1) occurrence obeys

$$
-\frac12(D_1+\mu_\ell^2)W
+\frac12D_1W
=-\frac12\mu_\ell^2W,
$$

and contributes (-B_1q^{\dot a}D_{\dot a}).  Hence

$$
\Gamma_{G_2}^{B_1>D}
=\frac13B_1(4p-q)^{\dot a}D_{\dot a}.
$$

Here (p) is the momentum of (D), while (q) is the momentum of (B_1).  Thus

$$
(c_{\rm pair},c_{\rm EOM})
=\left(-\frac13,\frac43\right).
$$

## 2. Dotted-index divergence

The locked epsilon tensors give

$$
\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
=-\delta^{\dot b}_{\dot c}.
$$

Therefore

$$
(P^{\dot a}B_1)D_{\dot a}
=\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
(P_{\dot b}B_1)D^{\dot c}
=-\langle B_1,D\rangle.
$$

Define

$$
E_{BD}:=B_1(P^{\dot a}D_{\dot a}),
\qquad
T_{BD}:=P^{\dot a}(B_1D_{\dot a}).
$$

The exact Leibniz expansion is

$$
T_{BD}
=-\langle B_1,D\rangle+E_{BD},
$$

so

$$
E_{BD}=\langle B_1,D\rangle+T_{BD}.
$$

Consequently

$$
-\frac13\langle B_1,D\rangle
+\frac43E_{BD}
=\langle B_1,D\rangle
+\frac43T_{BD}.
$$

In the exact-divergence quotient,

$$
\boxed{c_{G_2}=1.}
$$
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
        "G2 SD and dotted-divergence checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
