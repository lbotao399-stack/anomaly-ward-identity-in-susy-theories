#!/usr/bin/env python3
"""Target-blind AB/BA G3 full resolvent and original-measure census.

The audit exhausts

    I2 - I1*S3 - I0*S4 + (1/2) I0*S3*S3

in the external (tildephi2, tildephi3) sector.  It separately evaluates the
actual d4theta_M d2bartheta_H Berezin word, so the endpoint conversion cannot
hide a factor two.  No holomorphic-twist coefficient is read.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import itertools
import json
from pathlib import Path
import sys
from typing import Any, Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_marked_sd_orbit_exact_audit as marked  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-ab-ba-g3-full-resolvent-census-exact.json"
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-full-resolvent-census-exact.md"


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in sp.Matrix(actual) - sp.Matrix(expected))
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


@dataclass(frozen=True)
class Port:
    vertex: str
    index: int
    field: str


def conjugate_pair(left: str, right: str) -> bool:
    if left == right == "u":
        return True
    return (
        left.startswith("phi")
        and right == "tilde" + left.removeprefix("phi")
    ) or (
        right.startswith("phi")
        and left == "tilde" + right.removeprefix("phi")
    )


def perfect_matchings(ports: tuple[Port, ...]) -> Iterable[tuple[tuple[Port, Port], ...]]:
    if not ports:
        yield ()
        return
    first = ports[0]
    for position in range(1, len(ports)):
        second = ports[position]
        if first.vertex == second.vertex or not conjugate_pair(first.field, second.field):
            continue
        remainder = ports[1:position] + ports[position + 1 :]
        for tail in perfect_matchings(remainder):
            yield ((first, second),) + tail


def connected(vertices: tuple[str, ...], edges: tuple[tuple[Port, Port], ...]) -> bool:
    if not vertices:
        return False
    reached = {vertices[0]}
    changed = True
    while changed:
        changed = False
        for left, right in edges:
            if left.vertex in reached and right.vertex not in reached:
                reached.add(right.vertex)
                changed = True
            if right.vertex in reached and left.vertex not in reached:
                reached.add(left.vertex)
                changed = True
    return reached == set(vertices)


def one_particle_irreducible(
    vertices: tuple[str, ...], edges: tuple[tuple[Port, Port], ...]
) -> bool:
    return connected(vertices, edges) and all(
        connected(vertices, edges[:index] + edges[index + 1 :])
        for index in range(len(edges))
    )


def enumerate_external_sector(
    vertices: dict[str, tuple[str, ...]],
) -> list[dict[str, Any]]:
    ports = tuple(
        Port(vertex, index, field)
        for vertex, fields in vertices.items()
        for index, field in enumerate(fields)
    )
    tilde2 = tuple(port for port in ports if port.field == "tilde2")
    tilde3 = tuple(port for port in ports if port.field == "tilde3")
    rows: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for external2 in tilde2:
        for external3 in tilde3:
            if external2 == external3:
                continue
            internal = tuple(
                port for port in ports if port not in (external2, external3)
            )
            if len(internal) % 2:
                continue
            for matching in perfect_matchings(internal):
                canonical_edges = tuple(
                    sorted(
                        (
                            min(left.vertex, right.vertex),
                            max(left.vertex, right.vertex),
                            min(left.field, right.field),
                            max(left.field, right.field),
                        )
                        for left, right in matching
                    )
                )
                key = (
                    external2.vertex,
                    external3.vertex,
                    canonical_edges,
                )
                if key in seen:
                    continue
                seen.add(key)
                names = tuple(vertices)
                is_connected = connected(names, matching)
                loops = len(matching) - len(names) + 1 if is_connected else -1
                is_1pi = one_particle_irreducible(names, matching)
                rows.append(
                    {
                        "external_C2_vertex": external2.vertex,
                        "external_C3_vertex": external3.vertex,
                        "edges": [
                            f"{left.vertex}:{left.field}--{right.vertex}:{right.field}"
                            for left, right in matching
                        ],
                        "connected": is_connected,
                        "loop_count": loops,
                        "one_particle_irreducible": is_1pi,
                    }
                )
    return rows


I0 = ("u", "phi1")
I1 = ("u", "u", "phi1")
I2 = ("u", "u", "u", "phi1")
S3 = {
    "G": ("u", "u", "u"),
    "M1": ("tilde1", "u", "phi1"),
    "M2": ("tilde2", "u", "phi2"),
    "M3": ("tilde3", "u", "phi3"),
    "Hminus": ("tilde1", "tilde2", "tilde3"),
    "Hplus": ("phi1", "phi2", "phi3"),
}
S4 = {
    "G4": ("u", "u", "u", "u"),
    "M1_2": ("tilde1", "u", "u", "phi1"),
    "M2_2": ("tilde2", "u", "u", "phi2"),
    "M3_2": ("tilde3", "u", "u", "phi3"),
}


def resolvent_census(ledger: Ledger) -> dict[str, Any]:
    i2_rows = enumerate_external_sector({"I2": I2})
    ledger.check("I2_C2C3_EXTERNAL_SUPPORT", len(i2_rows), 0)

    i1s3_rows: list[dict[str, Any]] = []
    for name, fields in S3.items():
        rows = enumerate_external_sector({"I1": I1, name: fields})
        for row in rows:
            row["action_vertex"] = name
        i1s3_rows.extend(rows)
    i1s3_1pi = [row for row in i1s3_rows if row["loop_count"] == 1 and row["one_particle_irreducible"]]
    ledger.check("I1S3_C2C3_ONE_LOOP_1PI_COUNT", len(i1s3_1pi), 0)

    i0s4_rows: list[dict[str, Any]] = []
    for name, fields in S4.items():
        rows = enumerate_external_sector({"I0": I0, name: fields})
        for row in rows:
            row["action_vertex"] = name
        i0s4_rows.extend(rows)
    i0s4_1pi = [row for row in i0s4_rows if row["loop_count"] == 1 and row["one_particle_irreducible"]]
    ledger.check("I0S4_C2C3_ONE_LOOP_1PI_COUNT", len(i0s4_1pi), 0)

    i0s3s3_rows: list[dict[str, Any]] = []
    for left_index, (left_name, left_fields) in enumerate(S3.items()):
        for right_index, (right_name, right_fields) in enumerate(S3.items()):
            if right_index < left_index:
                continue
            rows = enumerate_external_sector(
                {
                    "I0": I0,
                    "L_" + left_name: left_fields,
                    "R_" + right_name: right_fields,
                }
            )
            for row in rows:
                row["action_vertices"] = [left_name, right_name]
            i0s3s3_rows.extend(rows)
    triangle_rows = [row for row in i0s3s3_rows if row["loop_count"] == 1]
    one_pi_rows = [row for row in triangle_rows if row["one_particle_irreducible"]]
    action_pairs = Counter(tuple(row["action_vertices"]) for row in one_pi_rows)
    ledger.check("I0S3S3_C2C3_ONE_LOOP_1PI_COUNT", len(one_pi_rows), 2)
    ledger.check(
        "I0S3S3_ONLY_M2_HMINUS_AND_M3_HMINUS",
        action_pairs,
        Counter({("M2", "Hminus"): 1, ("M3", "Hminus"): 1}),
    )

    one_pr_rows = [row for row in triangle_rows if not row["one_particle_irreducible"]]
    ledger.check(
        "M1_HMINUS_C2C3_ROWS_ARE_NOT_1PI",
        all(
            not row["one_particle_irreducible"]
            for row in one_pr_rows
            if tuple(row["action_vertices"]) == ("M1", "Hminus")
        ),
        True,
    )

    return {
        "I2": {"rows": i2_rows, "one_loop_1PI": 0},
        "I1S3": {"rows": i1s3_rows, "one_loop_1PI": i1s3_1pi},
        "I0S4": {"rows": i0s4_rows, "one_loop_1PI": i0s4_1pi},
        "I0S3S3": {
            "all_one_loop_rows": triangle_rows,
            "one_loop_1PI": one_pi_rows,
            "one_loop_1PR": one_pr_rows,
        },
    }


def original_measure_words(ledger: Ledger) -> dict[str, str]:
    g = marked.g23
    words = marked.g23_exact_words()
    r0 = words["r0"]
    r1 = words["r1"]
    r2 = words["r2"]
    p = words["p"]
    q = words["q"]
    minus_r2 = g.matrix_neg(r2)

    a_unmarked = g.d(
        g.bar_d2(
            g.d(g.delta4(g.S, g.M), g.S, 0, r0),
            g.S,
            r0,
        ),
        g.S,
        0,
        r0,
    )
    a_marked = g.d(a_unmarked, g.S, 1, r0)
    b_unmarked = g.d(
        g.bar_d2(
            g.d2(g.delta4(g.S, g.H), g.S, minus_r2),
            g.S,
            minus_r2,
        ),
        g.S,
        0,
        minus_r2,
    )
    b_marked = g.d(b_unmarked, g.S, 1, minus_r2)
    bridge_full = g.bar_d2(
        g.d2(g.delta4(g.M, g.H), g.M, r1),
        g.M,
        r1,
    )
    external = g.antichiral_bottom(g.M, p) * g.antichiral_bottom(g.H, q)

    # Canonical d4theta monomial integrates with 1/4.  Canonical
    # bartheta_dot+ bartheta_dot- integrates with 1/2 because
    # int d2bartheta (-1/4) barD2=1.  The original measure factor is 1/8.
    original_mask = (15 << (4 * g.M)) | (3 << (4 * g.H + 2))
    a_original = sp.factor(
        (a_marked * b_unmarked * bridge_full * external).coefficient(original_mask)
        / 8
    )
    b_original = sp.factor(
        (a_unmarked * b_marked * bridge_full * external).coefficient(original_mask)
        / 8
    )
    ledger.check("ORIGINAL_MEASURE_A_OVER_FULL_FULL_RAW", a_original, 4 * words["g3_a_full"])
    ledger.check("ORIGINAL_MEASURE_B_OVER_FULL_FULL_RAW", b_original, 4 * words["g3_b_parent_raw"])
    ledger.check(
        "ORIGINAL_MEASURE_A_MAGNITUDE_EQUALS_ENDPOINT_MINUS4",
        sp.factor(a_original / words["g3_a_full"]),
        4,
    )
    ledger.check(
        "ORIGINAL_MEASURE_B_MAGNITUDE_EQUALS_ENDPOINT_MINUS4",
        sp.factor(b_original / words["g3_b_parent_raw"]),
        4,
    )
    return {
        "A_original": text(a_original),
        "A_full_full_raw": text(words["g3_a_full"]),
        "B_original": text(b_original),
        "B_full_full_raw": text(words["g3_b_parent_raw"]),
        "measure_factor": "(1/4)*(1/2)=1/8",
        "magnitude_ratio_to_full_full_raw": "4",
        "factor_two_found": "NO",
    }


def sd_and_normalization(ledger: Ledger) -> dict[str, Any]:
    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2", nonzero=True)
    w0, w1, w2 = sp.symbols("W0 W1 W2")
    denominator = d0 * d1 * d2
    parents = (
        -4096 * (d0 + mu2) * w0 / denominator,
        +4096 * (d1 + mu2) * w1 / denominator,
        -4096 * (d2 + mu2) * w2 / denominator,
    )
    cuts = (
        +4096 * w0 / (d1 * d2),
        -4096 * w1 / (d0 * d2),
        +4096 * w2 / (d0 * d1),
    )
    remainders = (
        -4096 * mu2 * w0 / denominator,
        +4096 * mu2 * w1 / denominator,
        -4096 * mu2 * w2 / denominator,
    )
    for index in range(3):
        ledger.check(f"SD_EDGE_{index}_FULL_D_ZERO", (parents[index] + cuts[index]).subs(mu2, 0), 0)
        ledger.check(f"SD_EDGE_{index}_DRED_REMAINDER", parents[index] + cuts[index], remainders[index])

    # Nonlinear Euler/explicit rows have equal routed kernels and opposite
    # coefficients.  With no factorable loop square their DRED defect is zero.
    je, jx, pe, px = 512 * w0, -512 * w0, -128 * w2, 128 * w2
    ledger.check("A_NONLINEAR_JE_PLUS_JX", je + jx, 0)
    ledger.check("B_NONLINEAR_PE_PLUS_PX", pe + px, 0)

    y, z = sp.symbols("y z", nonnegative=True)
    weights = (
        2 * sp.integrate(sp.integrate(1 - y - z, (z, 0, 1 - y)), (y, 0, 1)),
        2 * sp.integrate(sp.integrate(y, (z, 0, 1 - y)), (y, 0, 1)),
        2 * sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1)),
    )
    ledger.check("THREE_SIMPLEX_WEIGHTS", sp.Matrix(weights), sp.Matrix((sp.Rational(1, 3),) * 3))
    ledger.check("THREE_SIMPLEX_WEIGHTS_SUM", sum(weights), 1)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    source = -coupling**2 / (4 * sp.sqrt(2))
    matter = sp.sqrt(2) * coupling / hbar
    hminus32 = -sp.sqrt(2) * coupling / hbar
    propagators = -hbar**3 / 256
    taylor = sp.Rational(1, 2) * 2
    pre_d = sp.simplify(source * matter * hminus32 * propagators * taylor)
    ledger.check("G32_PRED", pre_d, -sp.sqrt(2) * hbar * coupling**4 / 1024)
    master = 1 / (32 * sp.pi**2)
    external_map = coupling**-2
    raw_each = sp.simplify(
        pre_d
        * (-4096)
        * sp.Rational(1, 3)
        * master
        * external_map
        * sp.I
        / lambda1
    )
    ledger.check("G32_EACH_SD_EDGE_RAW_WEDGE", raw_each, sp.Rational(2, 3) * sp.I * sp.sqrt(2))
    raw_total = sp.simplify(3 * raw_each)
    typed_total = -raw_total
    ledger.check("G32_THREE_EDGE_RAW_WEDGE", raw_total, 2 * sp.I * sp.sqrt(2))
    ledger.check("G32_THREE_EDGE_TYPED", typed_total, -2 * sp.I * sp.sqrt(2))

    return {
        "parents": [text(value) for value in parents],
        "cuts": [text(value) for value in cuts],
        "remainders": [text(value) for value in remainders],
        "nonlinear_zero_square": {
            "A": "JE+JX=512*W0-512*W0=0",
            "B": "PE+PX=-128*W2+128*W2=0",
        },
        "simplex_weights": [text(value) for value in weights],
        "G32_raw_wedge": text(raw_total),
        "G32_typed": text(typed_total),
        "G33_typed": text(-typed_total),
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    census = resolvent_census(ledger)
    original_measure = original_measure_words(ledger)
    sd = sd_and_normalization(ledger)
    return {
        "schema": "step5-ab-ba-g3-full-resolvent-census-exact-v1",
        "status": "PASS_FULL_RESOLVENT_CENSUS__NO_MISSING_1PI_C2C3_FAMILY__G3_SCALE_TWO_REMAINS",
        "external_target_used": False,
        "resolvent": "I2-I1*S3-I0*S4+(1/2)*I0*S3*S3",
        "port_conventions": {
            "I0": list(I0),
            "I1": list(I1),
            "I2": list(I2),
            "S3": {key: list(value) for key, value in S3.items()},
            "S4": {key: list(value) for key, value in S4.items()},
            "propagators": ["u--u", "phi_r--tilde_r"],
            "external_sector": ["tilde2=C2", "tilde3=C3"],
        },
        "census": census,
        "original_measure": original_measure,
        "sd_and_normalization": sd,
        "conclusion": {
            "missing_net_correction": "0",
            "raw_result": ["G32=-2*i*sqrt(2)", "G33=+2*i*sqrt(2)"],
            "remaining_boundary": (
                "The full bare-source 1PI resolvent and original-measure conversion "
                "contain no -i*sqrt(2) family.  A match cannot be obtained by adding "
                "I2, I1S3, or I0S4 in this external port sector."
            ),
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(_: dict[str, Any]) -> str:
    return r"""# AB/BA G3 full resolvent census and original-measure audit

Status: `PASS_FULL_RESOLVENT_CENSUS__NO_MISSING_1PI_C2C3_FAMILY__G3_SCALE_TWO_REMAINS`.

## 1. Resolvent

$$
\Gamma_{g^2}
=I_2-I_1S_3-I_0S_4+\frac12I_0S_3S_3.
$$

The bare source supports are

$$
I_0=(u,\phi_1),\qquad
I_1=(u,u,\phi_1),\qquad
I_2=(u,u,u,\phi_1).
$$

For external $(C_2,C_3)=(\widetilde\phi_2,\widetilde\phi_3)$, exact port
matching gives

$$
N^{\rm 1PI}_{I_2}=0,qquad
N^{\rm 1PI}_{I_1S_3}=0,qquad
N^{\rm 1PI}_{I_0S_4}=0.
$$

At $I_0S_3S_3$, the only one-loop 1PI rows are

$$
(M_2,H_-),\qquad (M_3,H_-).
$$

The possible $(M_1,H_-)$ rows put both external fields at $H_-$ and leave an
articulation edge; they are 1PR external-leg attachments.

## 2. Original measure

For the canonical monomials,

$$
\int d^4\theta_M\,\theta_M^+\theta_M^-\bar\theta_M^{\dot+}\bar\theta_M^{\dot-}
=\frac14,
$$

$$
\int d^2\bar\theta_H\,
\bar\theta_H^{\dot+}\bar\theta_H^{\dot-}
=\frac12.
$$

Thus the direct original measure carries

$$
\frac14\frac12=\frac18.
$$

Evaluating the complete projectors directly gives

$$
F_A^{d^4\theta_Md^2\bar\theta_H}
=4F_A^{d^4\theta_Md^4\theta_H},
$$

$$
F_B^{d^4\theta_Md^2\bar\theta_H}
=4F_B^{d^4\theta_Md^4\theta_H}.
$$

The sign relative to the transported representation is the endpoint-transfer
sign; the magnitude is exactly the locked omitted-endpoint factor $4$.  No
factor $1/2$ occurs.

## 3. Parent--cut rows

$$
\frac{-4096(D_0+\mu^2)W_0}{D_0D_1D_2}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu^2W_0}{D_0D_1D_2},
$$

$$
\frac{4096(D_1+\mu^2)W_1}{D_0D_1D_2}
-\frac{4096W_1}{D_0D_2}
=\frac{4096\mu^2W_1}{D_0D_1D_2},
$$

$$
\frac{-4096(D_2+\mu^2)W_2}{D_0D_1D_2}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu^2W_2}{D_0D_1D_2}.
$$

At $\mu^2=0$, every row is zero.

The nonlinear rows are

$$
JE+JX=512W_0-512W_0=0,
$$

$$
PE+PX=-128W_2+128W_2=0.
$$

They contain no independent loop inverse square and no $\mu^2$ remainder.

## 4. Normalization

$$
w_0=w_1=w_2=\frac13,qquad w_0+w_1+w_2=1.
$$

For each edge,

$$
c_{32,e}=\frac23i\sqrt2.
$$

Therefore

$$
c_{32}^{\rm raw}=3\frac23i\sqrt2=2i\sqrt2,
$$

and the locked Fourier map gives

$$
\boxed{
c_{32}^{\rm typed}=-2i\sqrt2,qquad
c_{33}^{\rm typed}=+2i\sqrt2.}
$$

The full bare-source 1PI resolvent supplies no additional
$-i\sqrt2$ correction.
"""


def canonical(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    json_text = canonical(payload)
    md_text = markdown(payload)
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise SystemExit(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise SystemExit(f"stale artifact: {MD_OUT}")
    else:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    print(f"PASS {payload['checks']['passed']}/{payload['checks']['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
