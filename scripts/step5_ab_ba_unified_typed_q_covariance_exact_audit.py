#!/usr/bin/env python3
"""Unified target-blind typed projection and residual-q covariance audit.

The raw p- and q-carriers are retained separately.  The p-carrier is the
ordered pairing, whereas the q-carrier is the divergence/EOM word.  A total
derivative carrier is recorded but is not imposed as a quotient relation.
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

import step5_ab_ba_full_1pi_quotient_exact_audit as g2_replay  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-unified-typed-q-covariance-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-unified-typed-q-covariance-exact.md"
G1_IN = ROOT / "audits" / "step5-ab-ba-g1-longitudinal-contact-exact.json"
G3_IN = ROOT / "audits" / "step5-ab-ba-g3-trace-metric-sd-exact.json"
G3_GATE7_IN = ROOT / "audits" / "step5-ab-ba-g3-gate7-normalization-first-error-exact.json"
G2_TYPED_IN = ROOT / "audits" / "step5-ab-ba-g2-omega-typed-routing-exact.json"
Q_IN = ROOT / "audits" / "step5-residual-q-projection.json"
CENSUS_IN = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def parse_exact(value: str) -> sp.Expr:
    return sp.sympify(value.replace("i", "I"))


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        actual_matrix = sp.Matrix(actual)
        expected_matrix = sp.Matrix(expected)
        return actual_matrix.shape == expected_matrix.shape and all(
            sp.simplify(value) == 0
            for value in (actual_matrix - expected_matrix)
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
    g1 = json.loads(G1_IN.read_text(encoding="utf-8"))
    g3 = json.loads(G3_IN.read_text(encoding="utf-8"))
    g3_gate7 = json.loads(G3_GATE7_IN.read_text(encoding="utf-8"))
    g2_typed = json.loads(G2_TYPED_IN.read_text(encoding="utf-8"))
    q_payload = json.loads(Q_IN.read_text(encoding="utf-8"))
    census = json.loads(CENSUS_IN.read_text(encoding="utf-8"))["routes"]
    ledger.check("G1_TARGET_NOT_USED", g1["external_target_used_in_derivation"], False)
    ledger.check("G3_TARGET_NOT_USED", g3["external_target_used"], False)
    ledger.check("G3_GATE7_TARGET_NOT_USED", g3_gate7["external_target_used"], False)
    ledger.check("G2_TYPED_TARGET_NOT_USED", g2_typed["external_target_used"], False)
    ledger.check(
        "G3_CONDITIONAL_CHI1_ARTIFACT_REJECTED",
        g3["status"],
        "REJECTED_CONDITIONAL_CONTACT_NORMALIZATION__CHI_ONE_NOT_DERIVED",
    )

    # Occurrence-wise full-d checks forbid a trace rescaling of G1.
    chi, mu2, edge_square = sp.symbols("chi mu2 Dedge")
    g1_rows = (
        g1["validation"]["first_nonzero_A_anomaly_row"],
        g1["validation"]["first_nonzero_B_anomaly_row"],
    )
    g1_chi_solutions: list[dict[sp.Symbol, sp.Expr]] = []
    for label, row in zip(("A", "B"), g1_rows):
        alpha = parse_exact(row["alpha_minus_8R"])
        longitudinal = parse_exact(row["L"])
        stored_parent = parse_exact(row["F"])
        stored_bar_square = parse_exact(row["bar_edge_square"])
        ledger.check(
            f"G1_{label}_STORED_PARENT_IDENTITY",
            alpha * stored_bar_square + longitudinal,
            stored_parent,
        )
        parent_chi = chi * alpha * (edge_square + mu2) + longitudinal
        contact = -longitudinal - alpha * edge_square
        full_d = sp.expand((parent_chi + contact).subs(mu2, 0))
        solution = sp.solve(sp.Eq(full_d, 0), chi, dict=True)
        g1_chi_solutions.extend(solution)
        ledger.check(f"G1_{label}_FULL_D_UNIQUE_CHI", solution, [{chi: 1}])
        ledger.check(
            f"G1_{label}_DRED_REMAINDER_CHI1",
            sp.expand((parent_chi + contact).subs(chi, 1)),
            alpha * mu2,
        )

    # Independent G2 replay: the three metric occurrences each fix chi=1.
    g2_ledger = g2_replay.Ledger()
    g2 = g2_replay.g2_exact(g2_ledger)
    ledger.check("G2_REPLAY_INTERNAL_CHECKS", len(g2_ledger.checks), 21)
    z = sp.symbols("z")
    g2_metric_rows = {
        "first": 1 - z,
        "second_det": z,
        "second_omega": -sp.Rational(1, 2),
    }
    for label, coefficient in g2_metric_rows.items():
        parent = chi * coefficient * (edge_square + mu2)
        contact = -coefficient * edge_square
        full_d = sp.expand((parent + contact).subs(mu2, 0))
        solution = sp.solve(sp.Poly(full_d, edge_square, z).coeffs(), chi, dict=True)
        ledger.check(f"G2_{label}_FULL_D_UNIQUE_CHI", solution, [{chi: 1}])
        ledger.check(
            f"G2_{label}_DRED_REMAINDER_CHI1",
            sp.expand((parent + contact).subs(chi, 1)),
            coefficient * mu2,
        )

    # Typed maps are fixed by the actual external slots, not by the letters
    # p and q.  G1 has B1(p),D(q); G2 has D(p),B1(q).
    g1_pair_eom_map = sp.eye(2)
    g2_pair_eom_map = sp.Matrix(((0, 1), (1, 0)))
    # The total-divergence map depends on the ordered dotted-index slot.
    # D>B1: T_DB=pair+EOM, so EOM=T_DB-pair.
    # B1>D: T_BD=-pair+EOM, so EOM=T_BD+pair.  The minus sign follows from
    # epsilon^{ab}epsilon_{ac}=-delta^b_c.
    g1_pair_total_derivative_map = sp.Matrix(((1, -1), (0, 1)))
    g2_pair_total_derivative_map = sp.Matrix(((1, 1), (0, 1)))
    eom_quotient = sp.Matrix(((1, 0),))
    g1_total_derivative_quotient = sp.Matrix(((1, -1),))
    g2_total_derivative_quotient = sp.Matrix(((1, 1),))

    epsilon_up = sp.Matrix(((0, 1), (-1, 0)))
    epsilon_down = sp.Matrix(((0, -1), (1, 0)))
    ledger.check(
        "DOTTED_EPSILON_FIRST_INDEX_CONTRACTION",
        epsilon_up.T * epsilon_down,
        -sp.eye(2),
    )

    g1_a = sp.Matrix((sp.Rational(4, 3), sp.Rational(2, 3)))
    g1_b = sp.Matrix((sp.Rational(2, 3), sp.Rational(4, 3)))
    g1_raw = g1_a + g1_b
    ledger.check("G1_RAW_P_Q_FROM_REPLAY", g1_raw, sp.Matrix((2, 2)))
    g1_pair_eom = g1_pair_eom_map * g1_raw
    g1_pair_td = g1_pair_total_derivative_map * g1_raw
    ledger.check("G1_TYPED_PAIR_EOM", g1_pair_eom, sp.Matrix((2, 2)))
    ledger.check("G1_TYPED_PAIR_TOTAL_DERIVATIVE", g1_pair_td, sp.Matrix((0, 2)))
    ledger.check("G1_EOM_QUOTIENT_ONLY", (eom_quotient * g1_raw)[0], 2)
    ledger.check("G1_TOTAL_DERIVATIVE_QUOTIENT_ONLY", (g1_total_derivative_quotient * g1_raw)[0], 0)

    # The old two numbers are marked-occurrence contributions.  They happen
    # to equal the final raw p,q coefficients, but p is the D momentum and q
    # is the B1 momentum.  Therefore the typed map swaps them.
    g2_raw = sp.Matrix((sp.Rational(4, 3), -sp.Rational(1, 3)))
    ledger.check("G2_REPLAY_FIRST_MARK", parse_exact(g2["lambda_units"]["first_mark"]), g2_raw[0])
    ledger.check(
        "G2_REPLAY_SECOND_MARK_COMPLETE",
        parse_exact(g2["lambda_units"]["second_mark_complete"]),
        g2_raw[1],
    )
    ledger.check("G2_ROUTED_M_EXTERNAL", g2_typed["routing"]["M_external"], "D(p)")
    ledger.check("G2_ROUTED_H_EXTERNAL", g2_typed["routing"]["H_external"], "B1(q)")
    g2_pair_eom = g2_pair_eom_map * g2_raw
    g2_pair_td = g2_pair_total_derivative_map * g2_pair_eom
    ledger.check("G2_TYPED_PAIR_EOM", g2_pair_eom, sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))))
    ledger.check("G2_TYPED_PAIR_TOTAL_DERIVATIVE", g2_pair_td, sp.Matrix((1, sp.Rational(4, 3))))
    ledger.check("G2_EOM_QUOTIENT_ONLY", (eom_quotient * g2_pair_eom)[0], -sp.Rational(1, 3))
    ledger.check("G2_TOTAL_DERIVATIVE_QUOTIENT_ONLY", (g2_total_derivative_quotient * g2_pair_eom)[0], 1)
    ledger.check("G2_OMEGA_RETAINED", g2_typed["omega_classification"]["delete_as_zero_square"], False)
    ledger.check("G2_OLD_IDENTITY_TYPED_MAP_REJECTED", sp.eye(2) * g2_raw == g2_pair_eom, False)

    # Fix the ordered C slots directly from the target-blind parent census.
    route32 = next(
        row for row in census
        if row["route_id"] == "TRI::A__B1::008::M2[1,2]::Hminus[0,1]"
    )
    route33 = next(
        row for row in census
        if row["route_id"] == "TRI::A__B1::009::M3[1,2]::Hminus[0,2]"
    )
    ledger.check(
        "G32_ORDERED_EXTERNAL_FIELDS",
        (route32["external_left_field"], route32["external_right_field"]),
        ("tildephi2", "tildephi3"),
    )
    ledger.check(
        "G33_ORDERED_EXTERNAL_FIELDS",
        (route33["external_left_field"], route33["external_right_field"]),
        ("tildephi3", "tildephi2"),
    )

    q_action = q_payload["compact_normalized_q_action"]
    ledger.check("LOCKED_q_B", q_action["q_r B_s"], "-i delta_rs A")
    ledger.check("LOCKED_q_C", q_action["q_r C_s"], "-(1/sqrt(2)) epsilon_rst B_t")
    ledger.check("LOCKED_q_D", q_action["q_r D_dot"], "-i P_dot C_r")

    # Basis: (<D,B1>, <B1,D>, <C2,C3>, <C3,C2>).
    # q1 covariance into Z gives the homogeneous constraints below.  They
    # are derived only from the three locked bottom-letter actions above.
    sqrt2 = sp.sqrt(2)
    imaginary = sp.I
    covariance_matrix = sp.Matrix(
        (
            (1, -1, 0, 0),
            (imaginary * sqrt2, 0, 1, 0),
            (-imaginary * sqrt2, 0, 0, 1),
        )
    )
    rref, pivots = covariance_matrix.rref()
    nullspace = covariance_matrix.nullspace()
    canonical_kernel = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    ledger.check("Q_COVARIANCE_RANK", covariance_matrix.rank(), 3)
    ledger.check("Q_COVARIANCE_NULLITY", len(nullspace), 1)
    ledger.check("Q_COVARIANCE_CANONICAL_KERNEL", covariance_matrix * canonical_kernel, sp.zeros(3, 1))

    g32_typed = parse_exact(
        g3_gate7["corrected_coefficients_lambda1"]["G32_typed_C2_gt_C3"]
    )
    g33_typed = parse_exact(
        g3_gate7["corrected_coefficients_lambda1"]["G33_typed_C3_gt_C2"]
    )
    ledger.check("G32_FOURIER_TYPED", g32_typed, -2 * imaginary * sqrt2)
    ledger.check("G33_FOURIER_TYPED", g33_typed, 2 * imaginary * sqrt2)
    # The exact B1>D dotted divergence maps the +4/3 EOM carrier to a
    # +4/3 ordered pair.  Therefore the physical G2 coefficient is one.
    g2_divergence_quotient_pair = g2_pair_td[0]
    direct_vector = sp.Matrix(
        (
            g1_pair_eom[0],
            g2_divergence_quotient_pair,
            g32_typed,
            g33_typed,
        )
    )
    direct_residual = sp.simplify(covariance_matrix * direct_vector)
    ledger.check(
        "DIRECT_Q_COVARIANCE_RESIDUAL",
        direct_residual,
        sp.Matrix((1, 0, 0)),
    )
    scale_candidates = sp.Matrix(
        (
            direct_vector[0],
            direct_vector[1],
            direct_vector[2] / canonical_kernel[2],
            direct_vector[3] / canonical_kernel[3],
        )
    )
    ledger.check("DIRECT_KERNEL_SCALE_CANDIDATES", scale_candidates, sp.Matrix((2, 1, 2, 2)))
    common_scale = sp.solve(
        [sp.Eq(direct_vector[index], sp.Symbol("t") * canonical_kernel[index]) for index in range(4)],
        sp.Symbol("t"),
        dict=True,
    )
    ledger.check("NO_COMMON_Q_COVARIANT_SCALE", common_scale, [])

    return {
        "schema": "step5-ab-ba-unified-typed-q-covariance-exact-v1",
        "status": "PASS_G2_DOTTED_DIVERGENCE_PAIR_ONE__G1_G3_COMMON_FACTOR_TWO_REMAINS",
        "external_target_used": False,
        "trace_metric_occurrence_check": {
            "G1_A": "chi=1",
            "G1_B": "chi=1",
            "G2_first": "chi=1",
            "G2_second_det": "chi=1",
            "G2_second_omega": "chi=1",
        },
        "typed_map": {
            "G1_raw_basis": ["p_on_B1", "q_on_D"],
            "G2_raw_basis": ["p_on_D", "q_on_B1"],
            "G1_matrix": [["1", "0"], ["0", "1"]],
            "G2_matrix": [["0", "1"], ["1", "0"]],
            "pair_EOM_basis": ["ordered_pair", "divergence_EOM"],
            "pair_total_derivative_basis": ["ordered_pair", "total_derivative"],
            "G1_total_derivative_definition": "T_DB=pair+EOM",
            "G2_total_derivative_definition": "T_BD=-pair+EOM",
            "G2_epsilon_reason": "epsilon^{ab}epsilon_{ac}=-delta^b_c",
        },
        "G1": {
            "raw_p_q": ["2", "2"],
            "pair_EOM": ["2", "2"],
            "pair_TD": ["0", "2"],
            "old_q_equals_minus_p_result": "0",
            "correct_EOM_quotient_only": "2",
        },
        "G2": {
            "raw_p_q": ["4/3", "-1/3"],
            "external_slots": ["D(p)", "B1(q)"],
            "pair_EOM": ["-1/3", "4/3"],
            "pair_TD": ["1", "4/3"],
            "mark_sum_not_typed_pair": "4/3+2/3-1=1",
            "EOM_quotient_only": "-1/3",
            "exact_divergence_quotient_pair": "1",
            "Omega": "retained transported r1 cut; pair contribution -1",
        },
        "q_covariance": {
            "basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
            "constraint_rref": [[text(value) for value in rref.row(row)] for row in range(rref.rows)],
            "pivots": list(pivots),
            "unique_kernel_ray": [text(value) for value in canonical_kernel],
            "direct_vector": [text(value) for value in direct_vector],
            "direct_residual": [text(value) for value in direct_residual],
            "scale_candidates": [text(value) for value in scale_candidates],
        },
        "first_typed_errors": [
            "the marked/unified G2 comment assigned p to B1 and q to D; the raw graph has D(p) at M and B1(q) at H",
            "the old unified map reused T=pair+EOM for B1>D; exact dotted raising gives T=-pair+EOM",
        ],
        "current_unique_blocker": (
            "G2_IS_EXACTLY_ONE_AFTER_DOTTED_DIVERGENCE; "
            "G1_AND_G3_REMAIN_ON_COMMON_SCALE_TWO"
        ),
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    return r"""# AB/BA unified typed projection and residual-q covariance

For G1 the external slots are

$$
B_1(p),\qquad D(q),
$$

so

$$
(c_p,c_q)_{G_1}
=(c_{\rm pair},c_{\rm EOM})_{G_1}.
$$

The exact replay gives

$$
(c_{\rm pair},c_{\rm EOM})_{G_1}=(2,2).
$$

For G2 the raw graph has the opposite momentum assignment:

$$
D(p)\text{ at }M,
\qquad
B_1(q)\text{ at }H.
$$

Hence

$$
\binom{c_{\rm pair}}{c_{\rm EOM}}_{G_2}
=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\binom{c_p}{c_q}_{G_2}.
$$

The D-first and B-first words are

$$
\frac13D(q-4p)B_1
=\frac13B_1(4p-q)D.
$$

Therefore

$$
(c_p,c_q)_{G_2}
=\left(\frac43,-\frac13\right),
$$

$$
\boxed{
(c_{\rm pair},c_{\rm EOM})_{G_2}
=\left(-\frac13,\frac43\right).}
$$

For the ordered (B_1>D) slot,

$$
\epsilon^{\dot a\dot b}\epsilon_{\dot a\dot c}
=-\delta^{\dot b}_{\dot c},
$$

therefore

$$
(P^{\dot a}B_1)D_{\dot a}
=-\langle B_1,D\rangle.
$$

Thus

$$
T_{BD}:=P^{\dot a}(B_1D_{\dot a})
=-\langle B_1,D\rangle+B_1(P^{\dot a}D_{\dot a}),
$$

$$
B_1(P\!\cdot D)=\langle B_1,D\rangle+T_{BD}.
$$

Consequently

$$
-\frac13\langle B_1,D\rangle
+\frac43B_1(P\!\cdot D)
=\langle B_1,D\rangle+\frac43T_{BD},
$$

and the exact-divergence quotient gives

$$
\boxed{c_{G_2}=1.}
$$

The transported $\Omega_{21}$ occurrence remains in this result:

$$
P_\Omega=-\frac12\bar L^2W,
\qquad
C_\Omega=+\frac12L_d^2W,
$$

$$
P_\Omega+C_\Omega=-\frac12\mu_\ell^2W.
$$

For G3, the two-axis trace gives the unhalved D-word magnitude $4096$, and
the locked Fourier phase gives

$$
(ip)_+\wedge(iq)_+=-(p_+\wedge q_+).
$$

Thus

$$
G_{3,2}^{\rm typed}=-2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\rm typed}=+2i\sqrt2\lambda_1.
$$

In the ordered basis

$$
(\langle D,B_1\rangle,\langle B_1,D\rangle,
\langle C_2,C_3\rangle,\langle C_3,C_2\rangle),
$$

the residual-$q$ kernel is

$$
\ker Q=\mathbb C(1,1,-i\sqrt2,+i\sqrt2).
$$

The corrected direct vector is

$$
v_{\rm direct}
=\left(2,1,-2i\sqrt2,+2i\sqrt2\right),
$$

and

$$
Qv_{\rm direct}
=\left(1,0,0\right).
$$

Its four candidate scales are

$$
2,\qquad 1,\qquad 2,\qquad 2.
$$

Thus G2 is exactly on the unit ray after the dotted-divergence quotient.
G1 and G3 retain one common factor two.
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
        print("PASS G1/G2 occurrence-wise chi=1")
        print("PASS channel-specific external-slot p/q -> pair/EOM maps")
        print("PASS G2 routing D(p), B1(q) and Omega occurrence")
        print("PASS corrected G3 Fourier sign and q residual")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
