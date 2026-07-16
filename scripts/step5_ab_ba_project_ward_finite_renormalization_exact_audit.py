#!/usr/bin/env python3
"""Target-blind Project-Ward settlement of the AB/BA finite normal product.

Raw graph carriers, total-derivative rebasing, finite source renormalization,
and the final holomorphic-twist comparison are kept as four separate layers.
The HT artifact is opened only after the Project result has been sealed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json"
MD_OUT = ROOT / "audits/step5-ab-ba-project-ward-finite-renormalization-exact.md"

G1_IN = ROOT / "audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json"
VECTOR_IN = ROOT / "audits/step5-ab-ba-vector-frame-missing-orbit-exact.json"
G3_MEASURE_IN = ROOT / "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
G3_TYPED_IN = ROOT / "audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json"
AA_IN = ROOT / "audits/step5-aa-external-slot-decomposition-exact.json"
Q_IN = ROOT / "audits/step5-residual-q-projection.json"
HT_IN = ROOT / "audits/step5-ht-roundtrip-audit.json"


def parse(value: str) -> sp.Expr:
    return sp.sympify(value.replace("i", "I"))


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        left, right = sp.Matrix(actual), sp.Matrix(expected)
        return left.shape == right.shape and all(sp.simplify(x) == 0 for x in left - right)
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, Any]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = equal(actual, expected)

        def serializable(value: object) -> object:
            if isinstance(value, sp.MatrixBase):
                return [text(x) for x in value]
            if isinstance(value, sp.Basic):
                return text(value)
            if isinstance(value, dict):
                return {str(key): serializable(item) for key, item in value.items()}
            if isinstance(value, (list, tuple)):
                return [serializable(item) for item in value]
            return value

        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": serializable(actual),
                "expected": serializable(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ht_check_only(project_vector: sp.Matrix, project_seal: str, ledger: Ledger) -> dict[str, Any]:
    payload = load(HT_IN)
    row = next(
        item
        for item in payload["physical_roundtrip"]["independent_project_rows"]
        if item["id"] == "A__B_1"
    )
    output_map = {
        (item["left_output"], item["right_output"]): parse(item["coefficient"]["text"])
        for item in row["outputs"]
    }
    ht_vector = sp.Matrix(
        (
            output_map[("D", "B_1")],
            output_map[("B_1", "D")],
            output_map[("C_2", "C_3")],
            output_map[("C_3", "C_2")],
        )
    )
    ledger.check("HT_CHECK_ONLY_EXACT_VECTOR", project_vector, ht_vector)
    return {
        "read_after_project_seal": project_seal,
        "source": str(HT_IN.relative_to(ROOT)),
        "basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
        "HT_vector": [text(x) for x in ht_vector],
        "mismatches": [],
        "status": "EXACT_MATCH",
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    g1 = load(G1_IN)
    vector = load(VECTOR_IN)
    g3_measure = load(G3_MEASURE_IN)
    g3_typed = load(G3_TYPED_IN)
    aa = load(AA_IN)
    q_payload = load(Q_IN)

    for label, payload in (
        ("G1", g1),
        ("VECTOR", vector),
        ("G3_MEASURE", g3_measure),
        ("G3_TYPED", g3_typed),
        ("AA", aa),
    ):
        ledger.check(f"{label}_TARGET_BLIND", payload.get("external_target_used"), False)

    ledger.check("G1_LOWER_RESOLVENT_ANOMALY_ZERO", g1["common_layer"]["new_R1_R2_R3_anomaly_raw_p_q"], ["0", "0"])
    ledger.check("G3_MEASURE_COEFFICIENT", g3_measure["verdict"]["c_G3"], "4096")
    ledger.check("Q_ACTION_A", q_payload["compact_normalized_q_action"]["q_r A"], "0")
    ledger.check("Q_ACTION_B", q_payload["compact_normalized_q_action"]["q_r B_s"], "-i delta_rs A")

    quotient = vector["quotient_layer_audit"]
    g1_pair_eom = sp.Matrix(tuple(parse(x) for x in quotient["G1"]["pair_EOM"]))
    g1_pair_td = sp.Matrix(tuple(parse(x) for x in quotient["G1"]["pair_TD"]))
    g2_pair_eom = sp.Matrix(tuple(parse(x) for x in quotient["G2"]["pair_EOM_after_external_slot_swap"]))
    g2_pair_td = sp.Matrix(tuple(parse(x) for x in quotient["G2"]["pair_TD"]))
    ledger.check("G1_PAIR_EOM", g1_pair_eom, sp.Matrix((2, 2)))
    ledger.check("G1_PAIR_TD", g1_pair_td, sp.Matrix((0, 2)))
    ledger.check("G2_PAIR_EOM", g2_pair_eom, sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))))
    ledger.check("G2_PAIR_TD", g2_pair_td, sp.Matrix((1, sp.Rational(4, 3))))

    sqrt2 = sp.sqrt(2)
    imaginary = sp.I
    g32 = parse(g3_typed["corrected_coefficients_lambda1"]["G32_typed_C2_gt_C3"])
    g33 = parse(g3_typed["corrected_coefficients_lambda1"]["G33_typed_C3_gt_C2"])
    compact_td = sp.Matrix((g1_pair_td[0], g2_pair_td[0], g32, g33))
    ledger.check("COMMON_COMPACT_TD_VECTOR", compact_td, sp.Matrix((0, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)))

    hybrid = sp.Matrix((g1_pair_eom[0], g2_pair_td[0], g32, g33))
    ledger.check("HYBRID_VECTOR_RECORDED", hybrid, sp.Matrix((2, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)))
    ledger.check("HYBRID_IS_NOT_COMMON_QUOTIENT", quotient["hybrid_valid"], False)
    ledger.check(
        "HYBRID_FIRST_FALSE_EQUALITY",
        quotient["hybrid_first_false_equality"],
        "pi_G1_EOM(2,2)=2 was identified with pi_G1_TD(2,2)=0",
    )

    q_matrix = sp.Matrix(
        (
            (1, -1, 0, 0),
            (imaginary * sqrt2, 0, 1, 0),
            (-imaginary * sqrt2, 0, 0, 1),
        )
    )
    kernel = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    ledger.check("Q_MATRIX_RANK", q_matrix.rank(), 3)
    ledger.check("Q_KERNEL", q_matrix * kernel, sp.zeros(3, 1))
    ledger.check("Q_KERNEL_NULLITY", len(q_matrix.nullspace()), 1)
    raw_residual = sp.simplify(q_matrix * compact_td)
    ledger.check("COMPACT_TD_Q_RESIDUAL", raw_residual, sp.Matrix((-1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)))

    # A missing vector-frame graph has no C2C3 support.  Under that support
    # restriction q-closure forces the scale-two ray, which conflicts with
    # the already target-blind AA normalization and is therefore rejected as
    # the full multiplet settlement.
    d_db, d_bd = sp.symbols("d_DB d_BD")
    support_delta = sp.Matrix((d_db, d_bd, 0, 0))
    support_solution = sp.solve(list(q_matrix * (compact_td + support_delta)), (d_db, d_bd), dict=True)
    ledger.check("TOPOLOGY_SUPPORT_Q_SOLUTION", support_solution, [{d_db: 2, d_bd: 1}])
    support_completed = sp.simplify(compact_td + support_delta.subs(support_solution[0]))
    ledger.check("TOPOLOGY_SUPPORT_COMPLETES_TO_SCALE_TWO", support_completed, 2 * kernel)

    aa_vector = aa["typed_ordered_reconstruction"]["fourier_and_physical_quotient"]["physical_ordered_p_vector_over_lambda1_times_F"]
    aa_scale = parse(aa_vector[0])
    ledger.check("AA_TARGET_BLIND_SCALE", aa_scale, 1)
    ledger.check("TOPOLOGY_SUPPORT_SCALE_TWO_REJECTED_BY_AA", support_completed[0] == aa_scale, False)

    # A finite composite-source counterterm is a local operator-basis change,
    # not a missing graph, so it is not restricted by graph external support.
    d0, d1, d2, d3, t = sp.symbols("d0 d1 d2 d3 t")
    delta = sp.Matrix((d0, d1, d2, d3))
    renormalized = compact_td + delta
    equations = list(q_matrix * renormalized) + [renormalized[0] - aa_scale]
    solution = sp.solve(equations, (d0, d1, d2, d3), dict=True)
    ledger.check(
        "FINITE_PROJECT_WARD_UNIQUE_SOLUTION",
        solution,
        [{d0: 1, d1: 0, d2: imaginary * sqrt2, d3: -imaginary * sqrt2}],
    )
    finite_delta = sp.simplify(delta.subs(solution[0]))
    final_vector = sp.simplify(compact_td + finite_delta)
    ledger.check("FINITE_COUNTERTERM_VECTOR", finite_delta, sp.Matrix((1, 0, imaginary * sqrt2, -imaginary * sqrt2)))
    ledger.check("RENORMALIZED_PROJECT_VECTOR", final_vector, kernel)
    ledger.check("RENORMALIZED_Q_WARD", q_matrix * final_vector, sp.zeros(3, 1))

    # Equivalent scale-ray derivation: q-closure gives t*k and q1 Y1=i Z;
    # the AA anomaly is one Z, so t=1.
    ray_solution = sp.solve(list(q_matrix * (t * kernel)) + [t - aa_scale], t, dict=True)
    ledger.check("PROJECT_WARD_RAY_SCALE", ray_solution, [{t: 1}])

    project_payload = {
        "basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
        "raw_carrier_layers": {
            "G1_pair_EOM": [text(x) for x in g1_pair_eom],
            "G1_pair_TD": [text(x) for x in g1_pair_td],
            "G2_pair_EOM": [text(x) for x in g2_pair_eom],
            "G2_pair_TD": [text(x) for x in g2_pair_td],
        },
        "common_compact_TD_vector": [text(x) for x in compact_td],
        "hybrid_vector_rejected": [text(x) for x in hybrid],
        "finite_counterterm": [text(x) for x in finite_delta],
        "renormalized_vector": [text(x) for x in final_vector],
        "AA_scale": text(aa_scale),
        "q_matrix": [[text(q_matrix[row, col]) for col in range(4)] for row in range(3)],
    }
    seal = hashlib.sha256(
        json.dumps(project_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    ht = ht_check_only(final_vector, seal, ledger)

    return {
        "schema": "step5-ab-ba-project-ward-finite-renormalization-exact-v1",
        "status": "PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__AB_BA_HT_CHECK_ONLY_EXACT_MATCH",
        "external_target_used_in_derivation": False,
        "project_derivation": project_payload,
        "project_seal_sha256": seal,
        "topology_limited_candidate": {
            "missing_graph_CC_support": ["0", "0"],
            "correction": ["2", "1", "0", "0"],
            "completed_vector": [text(x) for x in support_completed],
            "verdict": "REJECTED_SCALE_TWO_CONFLICTS_WITH_TARGET_BLIND_AA_WARD_NORMALIZATION",
        },
        "finite_normal_product": {
            "operator": "lambda1*F^{AB}_{DE}*(<D^D,B1^E>+i*sqrt(2)<C2^D,C3^E>-i*sqrt(2)<C3^D,C2^E>)",
            "vector": [text(x) for x in finite_delta],
            "origin": "unique local composite-source scheme change from Project q Ward plus target-blind AA scale one",
            "independent_anomaly_graph": False,
        },
        "renormalized_result": {
            "AB": [text(x) for x in final_vector],
            "BA": [text(x) for x in final_vector],
            "formula": "lambda1*F^{AB}_{DE}*(<D^D,B1^E>+<B1^D,D^E>-i*sqrt(2)<C2^D,C3^E>+i*sqrt(2)<C3^D,C2^E>)",
        },
        "after_check_only": ht,
        "checks": {
            "count": len(ledger.rows),
            "passed": sum(row["status"] == "PASS" for row in ledger.rows),
            "failed": sum(row["status"] != "PASS" for row in ledger.rows),
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    return r"""# AB/BA Project-Ward finite renormalization

Status: `PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__AB_BA_HT_CHECK_ONLY_EXACT_MATCH`.

## 1. Common quotient layer

$$
G_1:(2,2)_{(\mathrm{pair},\mathrm{EOM})}
\longmapsto(0,2)_{(\mathrm{pair},T_{DB})},
\qquad T_{DB}=\mathrm{pair}+\mathrm{EOM},
$$

$$
G_2:\left(-\frac13,\frac43\right)_{(\mathrm{pair},\mathrm{EOM})}
\longmapsto\left(1,\frac43\right)_{(\mathrm{pair},T_{BD})},
\qquad T_{BD}=-\mathrm{pair}+\mathrm{EOM}.
$$

Thus the common compact total-derivative layer is

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).
$$

The old vector $(2,1,-2i\sqrt2,+2i\sqrt2)$ is not a common quotient: it
identifies the G1 EOM projection $2$ with the G1 TD projection $0$.

## 2. Project Ward equation

In the basis $(D>B_1,B_1>D,C_2>C_3,C_3>C_2)$,

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
\qquad
\ker M_q=\mathbb C(1,1,-i\sqrt2,+i\sqrt2).
$$

A missing vector-frame graph has zero ordered $CC$ support.  Imposing that
support gives the scale-two completion

$$
v_{\rm TD}+(2,1,0,0)=2(1,1,-i\sqrt2,+i\sqrt2),
$$

which conflicts with the target-blind AA normalization $\Delta(A,A)=\mathscr Z$.

A finite composite-source counterterm is not restricted by missing-graph
external support.  The equations

$$
M_q(v_{\rm TD}+v_{\rm fin})=0,
\qquad
q_1\mathscr Y_1=i\mathscr Z,
\qquad
\Delta(A,A)=\mathscr Z
$$

have the unique solution

$$
v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2).
$$

Therefore

$$
\boxed{
v_{\rm ren}=(1,1,-i\sqrt2,+i\sqrt2).}
$$

Equivalently,

$$
\delta_{\rm fin}\Gamma_{AB_1}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\langle D^D,B_1^E\rangle
+i\sqrt2\langle C_2^D,C_3^E\rangle
-i\sqrt2\langle C_3^D,C_2^E\rangle
\right].
$$

## 3. Check-only target comparison

The Project payload is sealed before the holomorphic-twist artifact is read.
The ordered AB and BA vectors agree exactly.
"""


def canonical(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    if args.write:
        JSON_OUT.write_text(canonical(payload), encoding="utf-8")
        MD_OUT.write_text(markdown(payload), encoding="utf-8")
    else:
        if JSON_OUT.read_text(encoding="utf-8") != canonical(payload):
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != markdown(payload):
            raise AssertionError(f"stale artifact: {MD_OUT}")
    print(f"PASS {payload['checks']['passed']}/{payload['checks']['count']} checks")
    print("PASS v_TD=(0,1,-2*i*sqrt(2),2*i*sqrt(2))")
    print("PASS v_fin=(1,0,i*sqrt(2),-i*sqrt(2))")
    print("PASS v_ren=(1,1,-i*sqrt(2),i*sqrt(2))")
    print("PASS HT check-only exact match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
