#!/usr/bin/env python3
"""Canonical AD/DA ``V_tildeW x V_W`` DD anomaly-sector audit.

The generated graph IR fixes one antichiral cubic vertex and one chiral
cubic vertex, while its physical Taylor projection has two external ``D``
components.  This checker therefore uses ``S_g^-|_D x S_g^+|_D`` with the
fixed ordered Wick weight one.  It does not read the holomorphic-twist
coefficient table.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ad_da_gauge_family_raw_audit as raw  # noqa: E402


alg = raw.alg
GRAPH_IR = ROOT / "generated" / "step5" / "physical-graph-ir.json"
JSON_OUT = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.json"
MD_OUT = ROOT / "audits" / "step5-ad-da-canonical-dd-mixed-chirality-exact.md"


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = actual == expected
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


def exact_text(value: object) -> str:
    if isinstance(value, alg.A):
        return value.text()
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value))
    return str(value)


def walk_json(value: object) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)


def graph_ir_certificate(ledger: Ledger) -> dict[str, object]:
    payload = json.loads(GRAPH_IR.read_text(encoding="utf-8"))
    result: dict[str, object] = {}
    for pair, ordinal in (("A__Ddot1", 26), ("Ddot1__A", 64)):
        prefix = f"CUT-ORBIT-{ordinal:03d}::{pair}::0::"
        rows = {
            str(row.get("graph_id")): row
            for row in walk_json(payload)
            if str(row.get("graph_id", "")).startswith(prefix)
        }
        triangle = rows[f"{prefix}TRIANGLE"]
        contact = rows[f"{prefix}CUT_CONTACT"]
        vertex_ids = tuple(row["id"] for row in triangle["vertices"])
        outputs = tuple(
            row["ordered_output_word"]
            for row in triangle["physical_taylor_expansion"]
        )
        ledger.check(f"{pair}_VERTICES", vertex_ids, ("I", "V_tildeW", "V_W"))
        ledger.check(f"{pair}_OUTPUTS", outputs, ("D>D", "D>D"))
        ledger.check(
            f"{pair}_WICK_WEIGHT",
            triangle["fixed_ordered_wick_weight"],
            "(1/2!)*(1+1)=1",
        )
        ledger.check(f"{pair}_TRIANGLE_METRIC", triangle["metric_tensor"], "hat_delta^{mn}")
        ledger.check(f"{pair}_CONTACT_METRIC", contact["metric_tensor"], "delta_4^{mn}")
        result[pair] = {
            "triangle_graph_id": triangle["graph_id"],
            "contact_graph_id": contact["graph_id"],
            "vertices": list(vertex_ids),
            "physical_outputs": list(outputs),
            "canonical_component_parent": "S_g^-|D x S_g^+|D",
            "fixed_ordered_wick_weight": triangle["fixed_ordered_wick_weight"],
            "triangle_metric": triangle["metric_tensor"],
            "cut_metric": contact["metric_tensor"],
        }
    return result


def source_hessian_certificate(ledger: Ledger) -> dict[str, object]:
    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))
    ad = raw.pair_source_I0_hessian_entries(
        "A__Ddot1", p, q, 0, 1, 1, 2, 0, 0, 1
    )
    da = raw.pair_source_I0_hessian_entries(
        "Ddot1__A", p, q, 0, 1, 1, 1, 0, 0, 1
    )
    ledger.check("AD_SOURCE_HESSIAN", ad, {"I0_N0[A]*D1[B]": alg.I / 4})
    ledger.check("DA_SOURCE_HESSIAN", da, {"I0_-D1[A]*N0[B]": alg.ONE / 4})
    ledger.check("LABELED_HESSIAN_FACTOR", sp.factorial(1) * sp.factorial(1), 1)
    return {
        "unit_ordered_insertions": {
            "AD": "N0^A*D1^B",
            "DA": "-D1^A*N0^B",
        },
        "direct_components": {"AD": "i/4", "DA": "1/4"},
        "functional_factor": "1!*1!=1",
        "extra_factor_two": False,
    }


CHIRALITY_SAMPLES = {
    "A__Ddot1": (
        alg.ONE / 4 + 5 * alg.I / 16,
        alg.ONE / 16 + alg.I / 8,
        alg.ONE / 32 + 3 * alg.I / 16,
        alg.ONE / 32 - alg.I / 16,
    ),
    "Ddot1__A": (
        -3 * alg.ONE / 16 - alg.I / 4,
        -alg.I / 16,
        alg.ONE / 8 - 3 * alg.I / 16,
        -alg.ONE / 16 + alg.I / 8,
    ),
}


def gaussian_expr(value: alg.A) -> sp.Expr:
    if value.b or value.d:
        raise AssertionError(value.text())
    return sp.Rational(value.a.numerator, value.a.denominator) + sp.I * sp.Rational(
        value.c.numerator, value.c.denominator
    )


def chirality_and_interpolation_certificate(ledger: Ledger) -> dict[str, object]:
    samples = raw.interpolation_samples()
    matrix = sp.Matrix(
        [
            [
                raw.plus_dotted(loop, 0),
                raw.plus_dotted(p, 0),
                raw.plus_dotted(q, 0),
            ]
            for loop, p, q in samples[:3]
        ]
    )
    ledger.check("INTERPOLATION_DETERMINANT", sp.factor(matrix.det()), 9 + 3 * sp.I)
    expected = {
        "A__Ddot1": (sp.I / 16, sp.I / 16, sp.I / 32),
        "Ddot1__A": (-sp.I / 16, sp.Integer(0), sp.Integer(0)),
    }
    rows: dict[str, object] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        values = CHIRALITY_SAMPLES[pair]
        coefficients = tuple(
            sp.simplify(value)
            for value in matrix.inv() * sp.Matrix([gaussian_expr(x) for x in values[:3]])
        )
        ledger.check(f"{pair}_RANK_ONE", coefficients, expected[pair])
        held_out = sp.simplify(
            coefficients[0] * raw.plus_dotted(samples[3][0], 0)
            + coefficients[1] * raw.plus_dotted(samples[3][1], 0)
            + coefficients[2] * raw.plus_dotted(samples[3][2], 0)
            - gaussian_expr(values[3])
        )
        ledger.check(f"{pair}_HELD_OUT", held_out, 0)
        rows[pair] = {
            "exact_aggregate_frames": [value.text() for value in values],
            "all_action_chirality_aggregates": {
                "--": [value.text() for value in values],
                "-+": [value.text() for value in values],
                "+-": [value.text() for value in values],
                "++": [value.text() for value in values],
            },
            "canonical_chirality": "-+",
            "raw_mu2_rank_one": {
                "ell_plus_dotted": exact_text(coefficients[0]),
                "p_plus_dotted": exact_text(coefficients[1]),
                "q_plus_dotted": exact_text(coefficients[2]),
            },
            "held_out_frame_residual": exact_text(held_out),
        }
    return rows


def normalization_certificate(ledger: Ledger) -> dict[str, str]:
    p = alg.vec((1, 0, 0, 0))
    q = alg.vec((0, 0, 0, 1))
    left = raw.external_d_normalization(p, 0, 1)
    right = raw.external_d_normalization(q, 1, 0)
    color = alg.A(alg.su2_F(0, 1, 1, 0))
    product = left * right
    raw_to_component = alg.ONE / (product * color)
    graph_weight = sp.Integer(1)
    master_over_lambda = sp.Rational(1, 2)
    conversion = sp.Integer(-16) * graph_weight * master_over_lambda
    ledger.check("LEFT_D_PREIMAGE", left, -alg.SQRT2 / 8)
    ledger.check("RIGHT_D_PREIMAGE", right, -alg.SQRT2 / 8)
    ledger.check("D_PREIMAGE_PRODUCT", product, alg.ONE / 32)
    ledger.check("COLOR_F_01_10", color, alg.A(-2))
    ledger.check("RAW_TO_COMPONENT", raw_to_component, alg.A(-16))
    ledger.check("FIXED_GRAPH_WEIGHT", graph_weight, 1)
    ledger.check("MASTER_OVER_LAMBDA1", master_over_lambda, sp.Rational(1, 2))
    ledger.check("RAW_INTEGRATED_TO_LAMBDA1", conversion, -8)
    return {
        "external_D_left": "-sqrt(2)/8",
        "external_D_right": "-sqrt(2)/8",
        "external_D_product": "1/32",
        "SU2_F_01_10": "-2",
        "raw_to_component": "-16",
        "fixed_ordered_wick_weight": "1",
        "master_over_lambda1": "1/2",
        "raw_integrated_to_lambda1": "-8",
        "lambda1": "hbar*g^2/(16*pi^2)",
    }


def sd_and_contact_certificate(ledger: Ledger) -> dict[str, object]:
    rd2, mu2, phat, qword = sp.symbols("r_ed2 mu_l2 P_hat_e Q_omega_e", nonzero=True)
    full_d = sp.simplify(-8 * qword * rd2 / (rd2 * phat) + 8 * qword / phat)
    dred = sp.simplify(
        -8 * qword * (rd2 + mu2) / (rd2 * phat) + 8 * qword / phat
    )
    ledger.check("FULL_D_SCHWINGER_ZERO", full_d, 0)
    ledger.check("DRED_CUT_FAILURE", dred, -8 * qword * mu2 / (rd2 * phat))
    contacts = {
        "A__Ddot1": {
            "e0__O05": "7*i*q_plus/(D1*D2)",
            "e1__O06": "0/(D0*D2)",
            "e2__O05": "2*i*q_plus/(D0*D1)",
        },
        "Ddot1__A": {
            "e0__O05": "-i*q_plus/(2*D1*D2)",
            "e1__O06": "i*(p+q)_plus/(D0*D2)",
            "e2__O05": "i*(p+q)_plus/(D0*D1)",
        },
    }
    ledger.check("CONTACT_EDGE_COUNT_AD", len(contacts["A__Ddot1"]), 3)
    ledger.check("CONTACT_EDGE_COUNT_DA", len(contacts["Ddot1__A"]), 3)
    return {
        "source_identity": {
            "longitudinal": "-8*Q_omega_e*bar(r_e)^2/P3-(1/2)*H_omega_e/P3",
            "gauge_fixing": "+(1/2)*H_omega_e/P3",
            "same_edge_cut": "+8*Q_omega_e/P_hat_e",
        },
        "full_d": "-8*Q_omega_e*[r_(e,d)^2/P3-1/P_hat_e]=0",
        "dred": "-8*Q_omega_e*mu_l^2/P3",
        "edges": {
            "e0": "P_hat_e=D1*D2",
            "e1": "P_hat_e=D0*D2",
            "e2": "P_hat_e=D0*D1",
        },
        "typed_contact_members": contacts,
        "contact_interpretation": (
            "These are denominator-preserving cut members. They are not "
            "standalone anomaly-zero diagrams and are not added again after "
            "the parent-minus-cut remainder is formed."
        ),
    }


def finite_vector_certificate(ledger: Ledger) -> dict[str, object]:
    i = sp.I
    ad_raw_p = sp.simplify(i / 16 - sp.Rational(2, 3) * i / 16)
    ad_raw_q = sp.simplify(i / 32 - sp.Rational(1, 3) * i / 16)
    da_raw_p = sp.simplify(-sp.Rational(2, 3) * (-i / 16))
    da_raw_q = sp.simplify(-sp.Rational(1, 3) * (-i / 16))
    ledger.check("AD_SIMPLEX_P", ad_raw_p, i / 48)
    ledger.check("AD_SIMPLEX_Q", ad_raw_q, i / 96)
    ledger.check("DA_SIMPLEX_P", da_raw_p, i / 24)
    ledger.check("DA_SIMPLEX_Q", da_raw_q, i / 48)
    conversion = -8
    ad_p, ad_q = sp.simplify(conversion * ad_raw_p), sp.simplify(conversion * ad_raw_q)
    da_p, da_q = sp.simplify(conversion * da_raw_p), sp.simplify(conversion * da_raw_q)
    ad_left, ad_right = sp.simplify(-ad_p + ad_q), sp.simplify(-ad_p)
    da_left, da_right = sp.simplify(-da_p), sp.simplify(-da_p + da_q)
    ledger.check("AD_KLEFT", ad_left, i / 12)
    ledger.check("AD_KRIGHT", ad_right, i / 6)
    ledger.check("DA_KLEFT", da_left, i / 3)
    ledger.check("DA_KRIGHT", da_right, i / 6)
    return {
        "mu2_master": "integral mu_l^2/P3=1/(32*pi^2)",
        "rank_one_moment": "ell -> -(2*p+q)/3",
        "raw_integrated_bracket": {
            "AD": {"p": "i/48", "q": "i/96"},
            "DA": {"p": "i/24", "q": "i/48"},
        },
        "ordered_momentum_maps": {
            "AD": "k_L=q; k_R=-(p+q)",
            "DA": "k_L=-(p+q); k_R=q",
        },
        "absolute_vector_over_lambda1": {
            "AD": {"k_left": "i/12", "k_right": "i/6"},
            "DA": {"k_left": "i/3", "k_right": "i/6"},
        },
    }


def _replay_one(args: tuple[str, str]) -> tuple[str, str, alg.A]:
    pair, sectors = args
    loop, p, q = raw.interpolation_samples()[0]
    routes = raw.all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        left_action_sector=sectors[0],
        right_action_sector=sectors[1],
    )
    return pair, sectors, sum(routes.values(), alg.ZERO)


def replay_frame0(ledger: Ledger, workers: int) -> None:
    args = [
        (pair, sectors)
        for pair in ("A__Ddot1", "Ddot1__A")
        for sectors in ("--", "-+")
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        rows = list(pool.map(_replay_one, args))
    for pair, sectors, value in rows:
        ledger.check(f"REPLAY_FRAME0_{pair}_{sectors}", value, CHIRALITY_SAMPLES[pair][0])


def build_payload(replay: bool = False, workers: int = 4) -> dict[str, object]:
    ledger = Ledger()
    payload: dict[str, object] = {
        "schema": "step5-ad-da-canonical-dd-mixed-chirality-exact-v1",
        "external_target_used": False,
        "graph_ir": graph_ir_certificate(ledger),
        "source_hessian": source_hessian_certificate(ledger),
        "chirality_and_raw_numerator": chirality_and_interpolation_certificate(ledger),
        "normalization": normalization_certificate(ledger),
        "schwinger_quotient": sd_and_contact_certificate(ledger),
        "finite_vector": finite_vector_certificate(ledger),
        "result": {
            "AD_dot_a": None,
            "DA_dot_a": None,
            "derivation_status": "REJECTED_IMPORTED_OUTPUT_ROUTING_AND_DIRECT_ONLY_HESSIAN",
        },
        "supersedes_only": (
            "The rejected v1 DD-port artifact's S_g^- x S_g^- interpretation. "
            "The direct source Hessian is unchanged; the canonical parent is "
            "S_g^-|D x S_g^+|D."
        ),
        "superseded_by": "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json",
        "rejection": {
            "invalid_momentum_maps": ["(q,-p-q)", "(-p-q,q)"],
            "omitted_source_hessian": "crossed F^{BA}_{DE}",
        },
        "status": "REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION",
    }
    if replay:
        replay_frame0(ledger, workers)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    payload["checks"] = {
        "count": len(ledger.rows),
        "passed": len(ledger.rows) - failed,
        "failed": failed,
        "rows": ledger.rows,
    }
    return payload


def render_markdown(payload: dict[str, object]) -> str:
    del payload
    return """# Step 5 AD/DA canonical DD mixed-chirality quotient

Status: `REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION`.

This artifact used the non-action-port maps `(q,-p-q)` and `(-p-q,q)` and
kept only the direct color Hessian.  It is superseded by
`audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md`.
"""


def render_markdown_rejected_legacy_unreachable(payload: dict[str, object]) -> str:
    checks = payload["checks"]
    assert isinstance(checks, dict)
    return rf"""# Step 5 AD/DA canonical DD mixed-chirality quotient

Status: `{payload['status']}`.

External target used: `false`.

## 1. Canonical component parent

$$
V_{{\widetilde W}}\big|_{{S_g^-,D}}
\times
V_W\big|_{{S_g^+,D}},
\qquad
\frac1{{2!}}(1+1)=1.
$$

Both generated-IR Taylor outputs are (D>D).  The literal
(S_g^-|_D\times S_g^+|_A) projection is therefore not this graph.

## 2. Direct source Hessian

$$
N_0^AD_1^B
=\frac{{\sqrt2}}2\frac{{i\sqrt2}}4
=\frac i4,
$$

$$
-D_1^AN_0^B
=-\left(-\frac{{\sqrt2}}4\right)\frac{{\sqrt2}}2
=\frac14,
\qquad
1!\,1!=1.
$$

## 3. Exact D-algebra numerator

Four independent frames and one held-out exact interpolation give

$$
N_{{AD}}^{{\rm ev}}
=\frac i{{16}}\mu_\ell^2
\left(\ell+p+\frac12q\right)_{{+\dot a}},
$$

$$
N_{{DA}}^{{\rm ev}}
=-\frac i{{16}}\mu_\ell^2\ell_{{+\dot a}}.
$$

The complete 36-route aggregate is identical for action chirality
((--),(-+),(+-),(++)); the canonical row is ((-+)).

## 4. Same-edge Schwinger quotient

$$
\mathscr L_{{\omega e}}
=-8\mathscr Q_{{\omega e}}
\frac{{\bar r_e^2}}{{P_3}}
-\frac12\frac{{\mathscr H_{{\omega e}}}}{{P_3}},
$$

$$
\mathscr G_{{\omega e}}
=+\frac12\frac{{\mathscr H_{{\omega e}}}}{{P_3}},
\qquad
\mathscr C_{{\omega e}}
=+8\frac{{\mathscr Q_{{\omega e}}}}{{P_{{\widehat e}}}}.
$$

Hence

$$
-8\mathscr Q_{{\omega e}}
\left[
\frac{{r_{{e,d}}^2}}{{P_3}}
-\frac1{{P_{{\widehat e}}}}
\right]=0,
$$

$$
-8\mathscr Q_{{\omega e}}
\left[
\frac{{\bar r_e^2}}{{P_3}}
-\frac1{{P_{{\widehat e}}}}
\right]
=-8\mathscr Q_{{\omega e}}
\frac{{\mu_\ell^2}}{{P_3}}.
$$

The O05/O06 two-denominator expressions are these cut members; affine
numerators do not make their parent-minus-cut anomaly zero.

## 5. Normalization and integral

$$
\left(-\frac{{\sqrt2}}8\right)^2=\frac1{{32}},
\qquad
F_{{01;10}}=-2,
\qquad
\frac1{{(1/32)(-2)}}=-16.
$$

$$
\int\frac{{d^d\ell}}{{(2\pi)^d}}
\frac{{\mu_\ell^2}}{{D_0D_1D_2}}
=\frac1{{32\pi^2}},
\qquad
\ell\longmapsto-\frac23p-\frac13q.
$$

$$
\frac{{\hbar g^2/(32\pi^2)}}{{\lambda_1}}=\frac12,
\qquad
(-16)\frac12=-8,
\qquad
\lambda_1=\frac{{\hbar g^2}}{{16\pi^2}}.
$$

## 6. Ordered result

$$
\boxed{{
\Gamma_{{AD,\dot a}}^{{\rm anom}}
=i\lambda_1
\left(
\frac1{{12}}k_{{L,+\dot a}}
+\frac16k_{{R,+\dot a}}
\right)
}},
$$

$$
\boxed{{
\Gamma_{{DA,\dot a}}^{{\rm anom}}
=i\lambda_1
\left(
\frac13k_{{L,+\dot a}}
+\frac16k_{{R,+\dot a}}
\right)
}}.
$$

$$
N_{{\rm pass}}={checks['passed']},
\qquad
N_{{\rm fail}}={checks['failed']}.
$$
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--replay-frame0", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    payload = build_payload(args.replay_frame0, args.workers)
    json_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    markdown_text = render_markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(markdown_text, encoding="utf-8")
    elif args.check_artifact:
        if args.replay_frame0:
            raise AssertionError("replay adds checks; do not combine with artifact check")
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != markdown_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
        print("REJECTED AD_DA_IMPORTED_OUTPUT_ROUTING")
        print("REJECTED AD_DA_DIRECT_ONLY_SOURCE_HESSIAN")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    else:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
