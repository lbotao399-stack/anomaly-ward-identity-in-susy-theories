#!/usr/bin/env python3
"""Exact epsilon/color/Hessian canonicalization audit for HT AB/BA G3."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-ht-ab-epsilon-canonicalization-exact.json"
MD_OUT = ROOT / "audits/step5-ht-ab-epsilon-canonicalization-exact.md"
NORMALIZATION_IN = ROOT / "audits/step5-ht-ab-normalization-quotient-exact.json"
RAW_G3_IN = ROOT / "audits/step5-ab-ba-g3-absolute-normalization-first-difference-exact.json"
MULTIPLICITY_IN = ROOT / "audits/step5-ab-ba-g1-g3-raw-multiplicity-trace-exact.json"
FULL_FAMILY_IN = ROOT / "audits/step5-ab-ba-full-family-exact.json"
HT_ROUNDTRIP_IN = ROOT / "audits/step5-ht-roundtrip-audit.json"


def parse_exact(value: str) -> sp.Expr:
    return sp.sympify(value.replace("i", "I"))


def text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        a, e = sp.Matrix(actual), sp.Matrix(expected)
        return a.shape == e.shape and all(sp.simplify(item) == 0 for item in a - e)
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


def jsonable(value: object) -> object:
    if isinstance(value, sp.MatrixBase):
        return [text(item) for item in value]
    if isinstance(value, sp.Basic):
        return text(value)
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(item) for item in value]
    return value


@dataclass
class Ledger:
    rows: list[dict[str, Any]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = equal(actual, expected)
        self.rows.append({
            "id": check_id,
            "status": "PASS" if passed else "FAIL",
            "actual": jsonable(actual),
            "expected": jsonable(expected),
        })
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def epsilon3(a: int, b: int, c: int) -> int:
    if {a, b, c} != {1, 2, 3}:
        return 0
    inversions = int(a > b) + int(a > c) + int(b > c)
    return -1 if inversions % 2 else 1


def su2_f(a: int, b: int, d: int, e: int) -> int:
    """F in the locked SU(2) frame kappa_ab=delta_ab/2."""
    return 2 * sum(
        epsilon3(a + 1, c + 1, d + 1) * epsilon3(b + 1, c + 1, e + 1)
        for c in range(3)
    )


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    normalization = json.loads(NORMALIZATION_IN.read_text(encoding="utf-8"))
    raw_g3 = json.loads(RAW_G3_IN.read_text(encoding="utf-8"))
    multiplicity = json.loads(MULTIPLICITY_IN.read_text(encoding="utf-8"))
    family = json.loads(FULL_FAMILY_IN.read_text(encoding="utf-8"))
    ht = json.loads(HT_ROUNDTRIP_IN.read_text(encoding="utf-8"))
    sqrt2, imaginary = sp.sqrt(2), sp.I

    ledger.check("NORMALIZATION_SCALE", normalization["ab_translation"]["verdict"], "SCALE_ONE")
    ledger.check("RAW_G3_TARGET_NOT_USED", raw_g3["external_target_used"], False)
    ledger.check("RAW_MULTIPLICITY_TARGET_NOT_USED", multiplicity["external_target_used"], False)

    epsilon_terms = [
        (j, k, epsilon3(1, j, k))
        for j in range(1, 4)
        for k in range(1, 4)
        if epsilon3(1, j, k)
    ]
    ledger.check("EPSILON_1JK_EXPANSION", epsilon_terms, [(2, 3, 1), (3, 2, -1)])

    ordered_basis = normalization["ab_translation"]["basis"][2:]
    ht_ordered = sp.Matrix(tuple(
        parse_exact(item)
        for item in normalization["ab_translation"]["HT_zero_component_main_compact_vector"][2:]
    ))
    raw_chain = raw_g3["G3_primitives_and_output"]["output_chain"]
    raw_ordered = sp.Matrix((
        parse_exact(raw_chain["typed_G32_C2_gt_C3"]),
        parse_exact(raw_chain["typed_G33_C3_gt_C2"]),
    ))
    ledger.check("ORDERED_BASIS", ordered_basis, ["C2>C3", "C3>C2"])
    ledger.check("HT_ORDERED", ht_ordered, sp.Matrix((-imaginary * sqrt2, imaginary * sqrt2)))
    ledger.check("RAW_ORDERED", raw_ordered, sp.Matrix((-2 * imaginary * sqrt2, 2 * imaginary * sqrt2)))

    # C is even; antisymmetry comes from the dotted epsilon contraction.
    c_parity = 0
    graded_sign = (-1) ** (c_parity * c_parity)
    dotted_sign = -1
    ledger.check("C_PARITY", c_parity, 0)
    ledger.check("GRADED_FIELD_EXCHANGE", graded_sign, 1)
    ledger.check("DOTTED_EXCHANGE", dotted_sign, -1)
    ledger.check("TOTAL_OUTPUT_EXCHANGE", graded_sign * dotted_sign, -1)
    x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2", commutative=True)
    eps_dot = sp.Matrix(((0, 1), (-1, 0)))
    x, y = sp.Matrix((x1, x2)), sp.Matrix((y1, y2))
    ledger.check("DOTTED_POLYNOMIAL", (y.T * eps_dot * x)[0], -(x.T * eps_dot * y)[0])

    simultaneous = all(
        su2_f(a, b, e, d) == su2_f(b, a, d, e)
        for a in range(3) for b in range(3)
        for d in range(3) for e in range(3)
    )
    fixed_ab_symmetric = all(
        su2_f(a, b, e, d) == su2_f(a, b, d, e)
        for a in range(3) for b in range(3)
        for d in range(3) for e in range(3)
    )
    ledger.check("COLOR_SIMULTANEOUS_EXCHANGE", simultaneous, True)
    ledger.check("COLOR_FIXED_AB_OUTPUT_SYMMETRY", fixed_ab_symmetric, False)
    ledger.check(
        "LOCKED_COLOR_IDENTITY",
        ht["typed_dictionary"]["color_frame"]["reversed_color_identity"],
        "C_Project^{BA}{}_{DE}=C_Project^{AB}{}_{ED}",
    )
    counterexample = {
        "F01_10": su2_f(0, 1, 1, 0),
        "F01_01": su2_f(0, 1, 0, 1),
        "F10_10": su2_f(1, 0, 1, 0),
        "F10_01": su2_f(1, 0, 0, 1),
    }
    ledger.check("COUNTEREXAMPLE_F01_10", counterexample["F01_10"], -2)
    ledger.check("COUNTEREXAMPLE_F01_01", counterexample["F01_01"], 0)
    ledger.check("COUNTEREXAMPLE_F10_10", counterexample["F10_10"], 0)
    ledger.check("COUNTEREXAMPLE_F10_01", counterexample["F10_01"], -2)

    # X_32^{DE}=-X_23^{ED}; after D<->E,
    # F^{AB}_{ED}=F^{BA}_{DE}.  Coordinates map by diag(1,-1).
    change = sp.diag(1, -1)
    ht_can = change * ht_ordered
    raw_can = change * raw_ordered
    ledger.check("HT_CANONICAL_TWO_TENSOR", ht_can, sp.Matrix((-imaginary * sqrt2, -imaginary * sqrt2)))
    ledger.check("RAW_CANONICAL_TWO_TENSOR", raw_can, sp.Matrix((-2 * imaginary * sqrt2, -2 * imaginary * sqrt2)))

    ht_plus, raw_plus = ht_can[0], raw_can[0]
    ht_sym, raw_sym = 2 * ht_plus, 2 * raw_plus
    ledger.check("HT_FPLUS_COEFFICIENT", ht_plus, -imaginary * sqrt2)
    ledger.check("RAW_FPLUS_COEFFICIENT", raw_plus, -2 * imaginary * sqrt2)
    ledger.check("HT_FNORMALIZED_COEFFICIENT", ht_sym, -2 * imaginary * sqrt2)
    ledger.check("RAW_FNORMALIZED_COEFFICIENT", raw_sym, -4 * imaginary * sqrt2)
    for check_id, actual in (
        ("ORDERED_RATIO", raw_ordered[0] / ht_ordered[0]),
        ("CANONICAL_TWO_TENSOR_RATIO", raw_can[0] / ht_can[0]),
        ("FPLUS_RATIO", raw_plus / ht_plus),
        ("FNORMALIZED_RATIO", raw_sym / ht_sym),
    ):
        ledger.check(check_id, sp.simplify(actual), 2)

    # The raw ordered coordinate and HT normalized-symmetric coordinate are
    # numerically equal but multiply different tensors.
    ledger.check("CROSS_BASIS_NUMERICAL_COINCIDENCE", raw_ordered[0], ht_sym)
    raw_frame = raw_ordered[0] * counterexample["F01_10"]
    ht_full_frame = ht_sym * sp.Rational(1, 2) * (
        counterexample["F01_10"] + counterexample["F10_10"]
    )
    ledger.check("RAW_FRAME_VALUE", raw_frame, 4 * imaginary * sqrt2)
    ledger.check("HT_FULL_FRAME_VALUE", ht_full_frame, 2 * imaginary * sqrt2)
    ledger.check("RAW_FRAME_NOT_HT_FRAME", raw_frame == ht_full_frame, False)

    # Input A is even and B1 is odd, so the ordered Hessian exchange has no
    # Koszul sign.  Its 2! has already been consumed by the two cyclic blocks.
    ledger.check("AB_INPUT_EXCHANGE_SIGN", (-1) ** (0 * 1), 1)
    blocks = multiplicity["cyclic_source_hessian"]["block_traces"]
    ledger.check("SOURCE_HESSIAN_BLOCKS", blocks, ["1", "1"])
    hessian_factor = sp.Rational(1, 2) * sum(parse_exact(item) for item in blocks)
    ledger.check("SOURCE_HESSIAN_HALF_TIMES_TWO", hessian_factor, 1)
    ledger.check(
        "SOURCE_HESSIAN_STORED",
        multiplicity["cyclic_source_hessian"]["supertrace"],
        "(1/2)*(1+1)=1",
    )
    ledger.check(
        "RAW_SOURCE_CYCLE_STORED",
        raw_g3["G3_primitives_and_output"]["primitive_factors"]["source_cycle"],
        "(1/2)*2=1",
    )
    ledger.check("FORBIDDEN_SECOND_HESSIAN_HALF", sp.Rational(1, 2) * hessian_factor, sp.Rational(1, 2))

    routes = family["route_order"]
    ledger.check("G32_EXTERNAL_ORDER", routes["AB_G32"]["external_fields"], ["tildephi2", "tildephi3"])
    ledger.check("G33_EXTERNAL_ORDER", routes["AB_G33"]["external_fields"], ["tildephi3", "tildephi2"])
    ledger.check("G32_G33_DISTINCT_ROUTES", routes["AB_G32"]["route_id"] != routes["AB_G33"]["route_id"], True)

    failed = [row for row in ledger.rows if row["status"] != "PASS"]
    if failed:
        raise AssertionError(failed)
    return {
        "schema": "step5-ht-ab-epsilon-canonicalization-exact-v1",
        "status": (
            "PASS_HT_EPSILON_ORDERED_AND_CANONICAL_BASES_EXACT__"
            "RAW_G32_G33_REMAIN_FACTOR_TWO__NO_HESSIAN_RESCALING"
        ),
        "epsilon_expansion": {
            "ordered_terms": [list(row) for row in epsilon_terms],
            "formula": "epsilon_1JK X_JK=X_23-X_32",
        },
        "ordered_basis": {
            "basis": ["F^{AB}X_23", "F^{AB}X_32"],
            "HT": [text(item) for item in ht_ordered],
            "raw": [text(item) for item in raw_ordered],
            "raw_over_HT": ["2", "2"],
        },
        "canonical_two_tensor_basis": {
            "exchange": "X_32^{DE}=-X_23^{ED}",
            "color": "F^{AB}_{ED}=F^{BA}_{DE}",
            "basis": ["F^{AB}X_23", "F^{BA}X_23"],
            "HT": [text(item) for item in ht_can],
            "raw": [text(item) for item in raw_can],
            "raw_over_HT": ["2", "2"],
        },
        "canonical_single_monomial_bases": {
            "F_plus": "F^{AB}+F^{BA}",
            "HT_F_plus_coefficient": text(ht_plus),
            "raw_F_plus_coefficient": text(raw_plus),
            "F_normalized": "(F^{AB}+F^{BA})/2",
            "HT_F_normalized_coefficient": text(ht_sym),
            "raw_F_normalized_coefficient": text(raw_sym),
            "ratio_in_either_basis": "2",
            "cross_basis_trap": (
                "raw ordered -2*i*sqrt(2) equals HT normalized-symmetric "
                "-2*i*sqrt(2) only as numbers, not as tensor coordinates"
            ),
        },
        "color_counterexample": counterexample,
        "hessian_factor": {
            "ordered_blocks": ["H_(u,phi1)", "H_(phi1,u)"],
            "block_traces": blocks,
            "exact_result": "(1/2!)*(1+1)=1",
            "forbidden_second_half": "1/2",
        },
        "first_false_equality": {
            "canonicalization": "F^{AB}_{ED}=F^{AB}_{DE}",
            "correct": "F^{AB}_{ED}=F^{BA}_{DE}",
            "equivalent_cross_basis_error": "F^{AB}=F_(AB)",
            "SU2_counterexample": "F^{01}_{10}=-2 while F^{10}_{10}=0",
            "hessian": "(1/2!)*(T_(u,phi)+T_(phi,u))=T, not T/2",
        },
        "verdict": (
            "RAW_G32_G33_ARE_STILL_TWICE_HT_IN_EVERY_COMMON_BASIS; "
            "CANONICALIZATION_AND_THE_EXTERNAL_HESSIAN_2_FACTOR_DO_NOT_REMOVE_THE_MISMATCH"
        ),
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    return rf"""# HT \(I=1\) epsilon canonicalization and G3 factor-two audit

Status: {payload['status']}.

## 1. Ordered basis

$$
X_{{st}}^{{DE}}:=(P_{{\dot a}}C_s^D)(P^{{\dot a}}C_t^E),
\qquad
X_{{32}}^{{DE}}=-X_{{23}}^{{ED}}.
$$

$$
\sum_{{J,K}}\varepsilon_{{1JK}}X_{{JK}}^{{DE}}
=X_{{23}}^{{DE}}-X_{{32}}^{{DE}}.
$$

In the basis

$$
\left(\mathbb F^{{AB}}{{}}_{{DE}}X_{{23}}^{{DE}},
\mathbb F^{{AB}}{{}}_{{DE}}X_{{32}}^{{DE}}\right),
$$

$$
v_{{HT}}=(-i\sqrt2,+i\sqrt2),
\qquad
v_{{raw}}=(-2i\sqrt2,+2i\sqrt2)=2v_{{HT}}.
$$

## 2. Canonical single monomial

$$
\mathbb F^{{AB}}{{}}_{{ED}}=\mathbb F^{{BA}}{{}}_{{DE}},
$$

so

$$
\mathbb F^{{AB}}{{}}_{{DE}}
\left(X_{{23}}^{{DE}}-X_{{32}}^{{DE}}\right)
=\left(\mathbb F^{{AB}}{{}}_{{DE}}
+\mathbb F^{{BA}}{{}}_{{DE}}\right)X_{{23}}^{{DE}}.
$$

In

$$
\left(\mathbb F^{{AB}}X_{{23}},\mathbb F^{{BA}}X_{{23}}\right),
$$

$$
v_{{HT}}^{{can}}=(-i\sqrt2,-i\sqrt2),
\qquad
v_{{raw}}^{{can}}=(-2i\sqrt2,-2i\sqrt2).
$$

For \(\mathbb F_+=\mathbb F^{{AB}}+\mathbb F^{{BA}}\),

$$
c_{{HT,+}}=-i\sqrt2,\qquad c_{{raw,+}}=-2i\sqrt2.
$$

For

$$
\mathbb F_{{(AB)}}=\frac12
\left(\mathbb F^{{AB}}+\mathbb F^{{BA}}\right),
$$

$$
c_{{HT,(AB)}}=-2i\sqrt2,\qquad c_{{raw,(AB)}}=-4i\sqrt2.
$$

The ratio is \(2\) in every common basis.  The numerical equality
\(c_{{raw,ordered}}=-2i\sqrt2=c_{{HT,(AB)}}\) compares coordinates of
different tensors \(\mathbb F^{{AB}}\) and \(\mathbb F_{{(AB)}}\).

In the locked \(SU(2)\) frame,

$$
\mathbb F^{{01}}{{}}_{{10}}=-2,\qquad
\mathbb F^{{10}}{{}}_{{10}}=0.
$$

## 3. Ordered external Hessian

$$
T_{{u\phi}}=T_{{\phi u}}=T,
$$

$$
\frac1{{2!}}\left(T_{{u\phi}}+T_{{\phi u}}\right)
=\frac12(T+T)=T.
$$

The raw primitive already contains \(\frac12(1+1)=1\).  Another factor
\(1/2\) would divide the same ordered Hessian orbit twice.

## 4. First false equality

$$
\boxed{{\mathbb F^{{AB}}{{}}_{{ED}}
\ne\mathbb F^{{AB}}{{}}_{{DE}}}},
\qquad
\boxed{{\mathbb F^{{AB}}{{}}_{{ED}}
=\mathbb F^{{BA}}{{}}_{{DE}}}}.
$$

Thus raw \(G_{{32}},G_{{33}}\) remain exactly twice HT after
canonicalization.

Checks: {payload['checks']['passed']}/{payload['checks']['count']} PASS.
"""


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    json_text, md_text = canonical(payload), markdown(payload)
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise SystemExit(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise SystemExit(f"stale artifact: {MD_OUT}")
    if args.write or not args.check:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    print(payload["status"])
    print(f"PASS {payload['checks']['passed']}/{payload['checks']['count']}")


if __name__ == "__main__":
    main()
