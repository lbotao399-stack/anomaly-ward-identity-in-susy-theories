#!/usr/bin/env python3
"""Retract the obsolete scale-one AB/BA full-1PI quotient artifact.

This regression has no graph-discovery role.  It records the first false G3
normalization equality, replays the exact raw-carrier to common-TD rebasing,
and binds the result to the accepted finite Project-Ward normal product.

Only two already sealed target-blind artifacts are read:

* the exact G3 original/full Berezin-measure equivalence audit;
* the exact AB/BA finite Project-Ward renormalization audit.

No holomorphic-twist artifact and no Project result engine is read or imported.
All arithmetic is exact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_g2_g3_dword_replay as g23  # noqa: E402


JSON_OUT = ROOT / "audits/step5-ab-ba-full-1pi-quotient-exact.json"
MD_OUT = ROOT / "audits/step5-ab-ba-full-1pi-quotient-exact.md"

G3_MEASURE_IN = (
    ROOT / "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
)
FINITE_IN = (
    ROOT / "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json"
)

SCHEMA = "step5-ab-ba-full-1pi-quotient-historical-retraction-exact-v2"
STATUS = (
    "HISTORICAL_RETRACTION__FALSE_G3_SCALE_ONE__"
    "CORRECT_RAW_TO_COMMON_TD__FINITE_NORMAL_PRODUCT_ACCEPTED"
)


def parse(value: str) -> sp.Expr:
    return sp.sympify(value.replace("i", "I"))


def exact_text(value: object) -> str:
    if isinstance(value, sp.MatrixBase):
        return "[" + ", ".join(exact_text(item) for item in value) + "]"
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        left = sp.Matrix(actual)
        right = sp.Matrix(expected)
        return left.shape == right.shape and all(
            sp.simplify(item) == 0 for item in left - right
        )
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, Any]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = exact_equal(actual, expected)
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

    @property
    def checks(self) -> list[dict[str, Any]]:
        """Compatibility alias for target-blind audits written before v2."""

        return self.rows


def euclidean_bispinor(
    vector: tuple[object, object, object, object],
) -> list[list[sp.Expr]]:
    """Locked Euclidean four-vector to two-spinor map."""

    imaginary = sp.I
    sigma_e = (
        -imaginary * sp.Matrix(((0, 1), (1, 0))),
        -imaginary * sp.Matrix(((0, -imaginary), (imaginary, 0))),
        -imaginary * sp.Matrix(((1, 0), (0, -1))),
        sp.eye(2),
    )
    mathsf = tuple(-imaginary * matrix for matrix in sigma_e)
    matrix = sum(
        (mathsf[index] * vector[index] for index in range(4)),
        sp.zeros(2),
    )
    return [
        [sp.expand(matrix[row, column]) for column in range(2)]
        for row in range(2)
    ]


def matrix_add(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [
        [sp.expand(left[a][b] + right[a][b]) for b in range(2)]
        for a in range(2)
    ]


def matrix_scale(
    scalar: object, matrix: list[list[sp.Expr]]
) -> list[list[sp.Expr]]:
    return [[sp.expand(scalar * item) for item in row] for row in matrix]


def determinant(matrix: list[list[sp.Expr]]) -> sp.Expr:
    return sp.expand(
        matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    )


def wedge(
    left: list[list[sp.Expr]], right: list[list[sp.Expr]]
) -> sp.Expr:
    return sp.expand(
        left[0][0] * right[0][1] - left[0][1] * right[0][0]
    )


def simplex(value: sp.Expr, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    """Normalized integral over y>=0, z>=0, y+z<=1."""

    return sp.simplify(
        2 * sp.integrate(sp.integrate(value, (z, 0, 1 - y)), (y, 0, 1))
    )


def load_with_binding(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    return json.loads(raw.decode("utf-8")), hashlib.sha256(raw).hexdigest()


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def finite_project_seal(project_derivation: dict[str, Any]) -> str:
    raw = json.dumps(
        project_derivation,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def finite_master(ledger: Ledger) -> sp.Expr:
    epsilon = sp.symbols("epsilon", positive=True)
    renormalization_scale, delta = sp.symbols("mu Delta", positive=True)
    d = 4 - 2 * epsilon
    j2 = (
        renormalization_scale ** (2 * epsilon)
        * sp.gamma(epsilon)
        * delta ** (-epsilon)
        / (4 * sp.pi) ** (2 - epsilon)
    )
    value = sp.limit((4 - d) * (d / 4) * j2 / d, epsilon, 0, dir="+")
    ledger.check("DRED_FINITE_MASTER", value, 1 / (32 * sp.pi**2))
    return value


def dred_cutting_identity(ledger: Ledger) -> dict[str, str]:
    d_e, mu_l2, d0, d1, d2 = sp.symbols("D_e mu_l2 D0 D1 D2", nonzero=True)
    product = d0 * d1 * d2
    other_product = sp.simplify(product / d_e)
    full_d_parent = d_e / product
    schwinger_cut = -1 / other_product
    four_d_parent = (d_e + mu_l2) / product

    ledger.check(
        "FULL_D_SQUARE_PLUS_SCHWINGER_CUT_ZERO",
        sp.simplify(full_d_parent + schwinger_cut),
        0,
    )
    ledger.check(
        "FOUR_D_SQUARE_PLUS_SCHWINGER_CUT_IS_MU2",
        sp.simplify(four_d_parent + schwinger_cut),
        mu_l2 / product,
    )
    return {
        "D_e": "r_{e,d}^2",
        "bar_r_e_squared": "D_e+mu_l^2",
        "full_d_square_plus_cut": "D_e/(D0*D1*D2)-1/prod_{j!=e}(D_j)=0",
        "four_d_square_plus_cut": (
            "(D_e+mu_l^2)/(D0*D1*D2)-1/prod_{j!=e}(D_j)="
            "mu_l^2/(D0*D1*D2)"
        ),
    }


def g2_exact(ledger: Any) -> dict[str, Any]:
    """Replay the historical G2 metric words without a target vector.

    This compatibility entry point is retained because later routing audits
    independently type the two momentum slots.  It returns only the exact
    D-algebra polynomial, its DRED cutting defect, and simplex moments.
    """

    y, z = sp.symbols("y z", real=True)
    first_mark = 1 - z
    second_mark_determinant = z
    second_mark_omega = -sp.Rational(1, 2)
    second_mark_complete = sp.expand(
        second_mark_determinant + second_mark_omega
    )

    ledger.check(
        "G2_M21_DET_OMEGA_IDENTITY",
        second_mark_determinant + second_mark_omega,
        second_mark_complete,
    )
    external_wedge = wedge(
        euclidean_bispinor((1, 0, 0, 0)),
        euclidean_bispinor((0, 0, 0, 1)),
    )
    ledger.check("G2_EXTERNAL_WEDGE", external_wedge, -sp.I)
    ledger.check("G2_FIRST_MARK_METRIC", first_mark, 1 - z)
    ledger.check(
        "G2_SECOND_MARK_DET_METRIC", second_mark_determinant, z
    )
    ledger.check(
        "G2_SECOND_MARK_OMEGA_METRIC",
        second_mark_omega,
        -sp.Rational(1, 2),
    )
    ledger.check(
        "G2_SECOND_MARK_FULL_METRIC",
        second_mark_complete,
        z - sp.Rational(1, 2),
    )
    ledger.check(
        "G2_SECOND_MARK_DET_PLUS_OMEGA",
        second_mark_determinant + second_mark_omega,
        second_mark_complete,
    )

    loop_d_squared, mu_l_squared = sp.symbols("L_d_squared mu_l_squared")
    bar_loop_squared = loop_d_squared + mu_l_squared
    for check_prefix, coefficient in (
        ("G2_FIRST_MARK", first_mark),
        ("G2_SECOND_DET", second_mark_determinant),
        ("G2_SECOND_OMEGA", second_mark_omega),
    ):
        parent = coefficient * bar_loop_squared
        schwinger_cut = -coefficient * loop_d_squared
        ledger.check(
            f"{check_prefix}_FULL_D_ZERO",
            sp.expand((parent + schwinger_cut).subs(mu_l_squared, 0)),
            0,
        )
        ledger.check(
            f"{check_prefix}_DRED_DEFECT",
            sp.expand(parent + schwinger_cut),
            coefficient * mu_l_squared,
        )

    delta = sp.symbols("Delta", nonzero=True)
    rank_zero_completion = (
        1 / (loop_d_squared + delta) ** 2
        - delta / (loop_d_squared + delta) ** 3
    )
    ledger.check(
        "G2_OMEGA_RANK_ZERO_COMPLETION",
        loop_d_squared / (loop_d_squared + delta) ** 3,
        rank_zero_completion,
    )

    first_simplex = simplex(first_mark, y, z)
    second_det_simplex = simplex(second_mark_determinant, y, z)
    second_omega_simplex = simplex(second_mark_omega, y, z)
    second_full_simplex = simplex(second_mark_complete, y, z)
    ledger.check("G2_FIRST_SIMPLEX", first_simplex, sp.Rational(2, 3))
    ledger.check(
        "G2_SECOND_DET_SIMPLEX", second_det_simplex, sp.Rational(1, 3)
    )
    ledger.check(
        "G2_SECOND_OMEGA_SIMPLEX", second_omega_simplex, -sp.Rational(1, 2)
    )
    ledger.check(
        "G2_SECOND_FULL_SIMPLEX", second_full_simplex, -sp.Rational(1, 6)
    )

    first_lambda = 2 * first_simplex
    second_lambda = 2 * second_full_simplex
    complete_lambda = first_lambda + second_lambda
    ledger.check("G2_FIRST_LAMBDA", first_lambda, sp.Rational(4, 3))
    ledger.check("G2_SECOND_LAMBDA", second_lambda, -sp.Rational(1, 3))
    ledger.check("G2_COMPLETE_LAMBDA", complete_lambda, 1)

    return {
        "metric_words": {
            "first_mark": exact_text(first_mark),
            "second_mark_determinant": exact_text(second_mark_determinant),
            "second_mark_omega": exact_text(second_mark_omega),
            "second_mark_complete": exact_text(second_mark_complete),
        },
        "simplex": {
            "first_mark": exact_text(first_simplex),
            "second_mark_determinant": exact_text(second_det_simplex),
            "second_mark_omega": exact_text(second_omega_simplex),
            "second_mark_complete": exact_text(second_full_simplex),
        },
        "lambda_units": {
            "first_mark": exact_text(first_lambda),
            "second_mark_complete": exact_text(second_lambda),
            "sum": exact_text(complete_lambda),
        },
    }


def _g3_original_measure_values(
    y_value: sp.Expr,
    z_value: sp.Expr,
    loop4: tuple[object, object, object, object],
) -> tuple[sp.Expr, sp.Expr]:
    """Normalized G3 coefficients before the two transverse traces."""

    p = euclidean_bispinor((1, 0, 0, 0))
    q = euclidean_bispinor((0, 0, 0, 1))
    total = matrix_add(p, q)
    r0 = matrix_add(
        euclidean_bispinor(loop4),
        matrix_add(matrix_scale(y_value, p), matrix_scale(z_value, total)),
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
    common_dword_normalization = sp.Integer(32768)
    return (
        sp.factor(
            (a_marked * b_unmarked * external).coefficient(mask)
            / common_dword_normalization
        ),
        sp.factor(
            (a_unmarked * b_marked * external).coefficient(mask)
            / common_dword_normalization
        ),
    )


def _g3_transverse_trace(
    y_value: sp.Expr, z_value: sp.Expr
) -> tuple[sp.Expr, sp.Expr]:
    center = _g3_original_measure_values(
        y_value, z_value, (0, 0, 0, 0)
    )
    traces = [sp.Integer(0), sp.Integer(0)]
    for axis in (1, 2):
        plus = tuple(1 if index == axis else 0 for index in range(4))
        minus = tuple(-1 if index == axis else 0 for index in range(4))
        value_plus = _g3_original_measure_values(y_value, z_value, plus)
        value_minus = _g3_original_measure_values(y_value, z_value, minus)
        for mark in range(2):
            traces[mark] += sp.factor(
                (value_plus[mark] + value_minus[mark] - 2 * center[mark]) / 2
            )
    return tuple(sp.factor(value) for value in traces)


def g3_exact(ledger: Any) -> dict[str, Any]:
    """Replay only the normalized G3 shape; no absolute graph scale is set."""

    points = {
        "00": (sp.Rational(0), sp.Rational(0)),
        "10": (sp.Rational(1), sp.Rational(0)),
        "01": (sp.Rational(0), sp.Rational(1)),
        "check": (sp.Rational(1, 3), sp.Rational(1, 3)),
    }
    samples = {
        label: _g3_transverse_trace(y_value, z_value)
        for label, (y_value, z_value) in points.items()
    }
    expected = {
        "00": (-2 * sp.I, 0),
        "10": (-2 * sp.I, 0),
        "01": (0, -2 * sp.I),
        "check": (-sp.Rational(4, 3) * sp.I, -sp.Rational(2, 3) * sp.I),
    }
    for label in points:
        ledger.check(f"G3_ORIGINAL_MEASURE_{label}_A", samples[label][0], expected[label][0])
        ledger.check(f"G3_ORIGINAL_MEASURE_{label}_B", samples[label][1], expected[label][1])

    y, z = sp.symbols("y z", real=True)
    affine_a = sp.expand(
        samples["00"][0]
        + y * (samples["10"][0] - samples["00"][0])
        + z * (samples["01"][0] - samples["00"][0])
    )
    affine_b = sp.expand(
        samples["00"][1]
        + y * (samples["10"][1] - samples["00"][1])
        + z * (samples["01"][1] - samples["00"][1])
    )
    ledger.check(
        "G3_A_AFFINE_CHECK_POINT",
        affine_a.subs({y: sp.Rational(1, 3), z: sp.Rational(1, 3)}),
        samples["check"][0],
    )
    ledger.check(
        "G3_B_AFFINE_CHECK_POINT",
        affine_b.subs({y: sp.Rational(1, 3), z: sp.Rational(1, 3)}),
        samples["check"][1],
    )

    external_wedge = wedge(
        euclidean_bispinor((1, 0, 0, 0)),
        euclidean_bispinor((0, 0, 0, 1)),
    )
    metric_a = sp.simplify(affine_a / (2 * external_wedge))
    metric_b = sp.simplify(affine_b / (2 * external_wedge))
    ledger.check("G3_A_METRIC", metric_a, 1 - z)
    ledger.check("G3_B_METRIC", metric_b, z)

    loop_d_squared, mu_l_squared = sp.symbols("L_d_squared mu_l_squared")
    bar_loop_squared = loop_d_squared + mu_l_squared
    for label, coefficient in (("G3_A", metric_a), ("G3_B", metric_b)):
        parent = coefficient * bar_loop_squared
        schwinger_cut = -coefficient * loop_d_squared
        ledger.check(
            f"{label}_FULL_D_ZERO",
            sp.expand((parent + schwinger_cut).subs(mu_l_squared, 0)),
            0,
        )
        ledger.check(
            f"{label}_DRED_DEFECT",
            sp.expand(parent + schwinger_cut),
            coefficient * mu_l_squared,
        )

    weight_a = simplex(metric_a, y, z)
    weight_b = simplex(metric_b, y, z)
    ledger.check("G3_A_SIMPLEX", weight_a, sp.Rational(2, 3))
    ledger.check("G3_B_SIMPLEX", weight_b, sp.Rational(1, 3))
    ledger.check("G3_COMPLETE_SIMPLEX", weight_a + weight_b, 1)

    return {
        "metric_words": {
            "A_mark": exact_text(metric_a),
            "B_mark": exact_text(metric_b),
        },
        "simplex": {
            "A_mark": exact_text(weight_a),
            "B_mark": exact_text(weight_b),
            "sum": exact_text(weight_a + weight_b),
        },
    }


def quotient_exact(*_args: object, **_kwargs: object) -> None:
    """Fail-closed compatibility tombstone for the retracted v1 quotient."""

    # Historical v1 imported scale output through project.build_bundle().
    # v2 never imports or executes that engine and rejects every call here.
    raise RuntimeError(
        "quotient_exact was retracted: use the sealed raw-to-common-TD and "
        "finite-normal-product audits"
    )


def validate_g3_source(
    payload: dict[str, Any], ledger: Ledger
) -> dict[str, Any]:
    ledger.check(
        "G3_SOURCE_SCHEMA",
        payload["schema"],
        "step5-ab-ba-g3-original-full-measure-equivalence-exact-v1",
    )
    ledger.check(
        "G3_SOURCE_STATUS",
        payload["status"],
        (
            "PASS_G3_ORIGINAL_FULL_MEASURE_EQUIVALENCE__"
            "CONVERSION_MAGNITUDE_FOUR__TWO_SUPERTRACE_CYCLES_CANCEL_HALF__"
            "C_G3_4096"
        ),
    )
    ledger.check("G3_SOURCE_EXTERNAL_TARGET_UNUSED", payload["external_target_used"], False)
    ledger.check("G3_SOURCE_HT_UNUSED", payload["HT_used"], False)
    ledger.check(
        "G3_SOURCE_DESIRED_VECTOR_FITTING_UNUSED",
        payload["desired_vector_fitting_used"],
        False,
    )
    ledger.check("G3_SOURCE_CHECKS_FAILED", payload["checks"]["failed"], 0)
    ledger.check(
        "G3_SOURCE_CHECKS_COMPLETE",
        payload["checks"]["passed"],
        payload["checks"]["count"],
    )

    measure = payload["grassmann_measure_equivalence"]
    chain = measure["coefficient_chain"]
    cycles = payload["supertrace_cycle_census"]
    verdict = payload["verdict"]

    ledger.check("G3_ABSOLUTE_COEFFICIENT", parse(chain["c_G3"]), 4096)
    ledger.check(
        "G3_ORIGINAL_MEASURE_CHAIN",
        chain["original"],
        "32768*(1/4)_M*(1/2)_barH=4096",
    )
    ledger.check(
        "G3_FULL_MEASURE_CHAIN",
        chain["full"],
        "65536*(1/4)_M*(1/4)_H=4096",
    )
    ledger.check(
        "G3_REJECTED_HALF_CHAIN",
        chain["rejected"],
        "32768*(1/4)_M*(1/4)_H=2048",
    )
    ledger.check("G3_NONZERO_SUPERTRACE_CYCLES", cycles["nonzero_count"], 2)
    ledger.check(
        "G3_CORRELATED_CYCLE_SUM",
        cycles["correct"],
        "(1/2)*(C1+C2)=C1",
    )
    ledger.check(
        "G3_FIRST_FALSE_EQUALITY",
        cycles["first_false_equality"],
        "(1/2)*(C1+C2) -> (1/2)*C1",
    )
    ledger.check(
        "G3_VERDICT_FIRST_FALSE_EQUALITY",
        verdict["first_false_equality"],
        cycles["first_false_equality"],
    )
    ledger.check("G3_VERDICT_REJECTS_2048", verdict["rejected_2048"], True)

    outer_half = sp.Rational(1, 2)
    c1 = sp.Integer(1)
    c2 = sp.Integer(1)
    correct_cycle_factor = outer_half * (c1 + c2)
    false_cycle_factor = outer_half * c1
    ledger.check("G3_TWO_CYCLES_CANCEL_OUTER_HALF", correct_cycle_factor, 1)
    ledger.check("G3_FALSE_SINGLE_CYCLE_FACTOR", false_cycle_factor, sp.Rational(1, 2))
    ledger.check(
        "G3_FALSE_NORMALIZATION_IS_2048",
        sp.Integer(4096) * false_cycle_factor / correct_cycle_factor,
        2048,
    )
    ledger.check(
        "G3_CORRECT_TO_REJECTED_RATIO",
        sp.Integer(4096) / sp.Integer(2048),
        2,
    )

    simplex = measure["simplex_weights"]
    ledger.check("G3_SIMPLEX_A_SHAPE", parse(simplex["A_mark"]), sp.Rational(2, 3))
    ledger.check("G3_SIMPLEX_B_SHAPE", parse(simplex["B_mark"]), sp.Rational(1, 3))
    ledger.check("G3_SIMPLEX_SHAPE_SUM", parse(simplex["sum"]), 1)

    return {
        "original_full_measure_coefficient": "4096",
        "rejected_single_cycle_coefficient": "2048",
        "raw_multiplicity_scale": "2",
        "simplex_shape_sum": "1",
        "nonzero_supertrace_cycles": 2,
        "outer_supertrace_factor": "1/2",
        "correct_cycle_factor": "(1/2)*(C1+C2)=1 for C1=C2=1",
        "first_false_equality": "(1/2)*(C1+C2) -> (1/2)*C1",
        "first_false_numeric_equality": "4096 -> 2048",
        "retracted_claim": "simplex 2/3+1/3=1 fixes the absolute G3 graph scale",
        "verdict": "RETRACTED_FALSE_SCALE_ONE_NORMALIZATION",
    }


def validate_finite_source(
    payload: dict[str, Any], ledger: Ledger
) -> tuple[dict[str, Any], sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    ledger.check(
        "FINITE_SOURCE_SCHEMA",
        payload["schema"],
        "step5-ab-ba-project-ward-finite-renormalization-exact-v1",
    )
    ledger.check(
        "FINITE_SOURCE_STATUS",
        payload["status"],
        "PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__AB_BA_HT_CHECK_ONLY_EXACT_MATCH",
    )
    ledger.check(
        "FINITE_SOURCE_EXTERNAL_TARGET_UNUSED_IN_DERIVATION",
        payload["external_target_used_in_derivation"],
        False,
    )
    ledger.check("FINITE_SOURCE_CHECKS_FAILED", payload["checks"]["failed"], 0)
    ledger.check(
        "FINITE_SOURCE_CHECKS_COMPLETE",
        payload["checks"]["passed"],
        payload["checks"]["count"],
    )
    ledger.check(
        "FINITE_SOURCE_PROJECT_SEAL",
        finite_project_seal(payload["project_derivation"]),
        payload["project_seal_sha256"],
    )

    project = payload["project_derivation"]
    ledger.check(
        "FINITE_SOURCE_BASIS",
        project["basis"],
        ["D>B1", "B1>D", "C2>C3", "C3>C2"],
    )
    layers = project["raw_carrier_layers"]
    g1_eom = sp.Matrix(tuple(parse(item) for item in layers["G1_pair_EOM"]))
    g1_td = sp.Matrix(tuple(parse(item) for item in layers["G1_pair_TD"]))
    g2_eom = sp.Matrix(tuple(parse(item) for item in layers["G2_pair_EOM"]))
    g2_td = sp.Matrix(tuple(parse(item) for item in layers["G2_pair_TD"]))

    ledger.check("FINITE_SOURCE_G1_EOM", g1_eom, sp.Matrix((2, 2)))
    ledger.check("FINITE_SOURCE_G1_TD", g1_td, sp.Matrix((0, 2)))
    ledger.check(
        "FINITE_SOURCE_G2_EOM",
        g2_eom,
        sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))),
    )
    ledger.check(
        "FINITE_SOURCE_G2_TD",
        g2_td,
        sp.Matrix((1, sp.Rational(4, 3))),
    )

    common_td = sp.Matrix(tuple(parse(item) for item in project["common_compact_TD_vector"]))
    finite_delta = sp.Matrix(tuple(parse(item) for item in project["finite_counterterm"]))
    renormalized = sp.Matrix(tuple(parse(item) for item in project["renormalized_vector"]))
    sqrt2 = sp.sqrt(2)
    imaginary = sp.I
    ledger.check(
        "FINITE_SOURCE_COMMON_TD",
        common_td,
        sp.Matrix((0, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)),
    )
    ledger.check(
        "FINITE_SOURCE_DELTA",
        finite_delta,
        sp.Matrix((1, 0, imaginary * sqrt2, -imaginary * sqrt2)),
    )
    ledger.check(
        "FINITE_SOURCE_RENORMALIZED",
        renormalized,
        sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2)),
    )
    ledger.check(
        "FINITE_SOURCE_DELTA_NOT_GRAPH",
        payload["finite_normal_product"]["independent_anomaly_graph"],
        False,
    )
    ledger.check(
        "FINITE_SOURCE_DELTA_VECTOR_MATCH",
        sp.Matrix(tuple(parse(item) for item in payload["finite_normal_product"]["vector"])),
        finite_delta,
    )
    ledger.check(
        "FINITE_SOURCE_RESULT_AB",
        sp.Matrix(tuple(parse(item) for item in payload["renormalized_result"]["AB"])),
        renormalized,
    )
    ledger.check(
        "FINITE_SOURCE_RESULT_BA",
        sp.Matrix(tuple(parse(item) for item in payload["renormalized_result"]["BA"])),
        renormalized,
    )

    return project, g1_eom, g2_eom, common_td, finite_delta


def rebase_and_settle(
    project: dict[str, Any],
    g1_eom: sp.Matrix,
    g2_eom: sp.Matrix,
    source_common_td: sp.Matrix,
    finite_delta: sp.Matrix,
    ledger: Ledger,
) -> dict[str, Any]:
    sqrt2 = sp.sqrt(2)
    imaginary = sp.I

    # Raw carrier basis:
    # (X_DB,E_DB,X_BD,E_BD,C23,C32).
    raw = sp.Matrix(
        (
            g1_eom[0],
            g1_eom[1],
            g2_eom[0],
            g2_eom[1],
            source_common_td[2],
            source_common_td[3],
        )
    )
    expected_raw = sp.Matrix(
        (2, 2, -sp.Rational(1, 3), sp.Rational(4, 3), -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)
    )
    ledger.check("RAW_SIX_CARRIER_VECTOR", raw, expected_raw)

    # T_DB=X_DB+E_DB => E_DB=T_DB-X_DB.
    # T_BD=-X_BD+E_BD => E_BD=T_BD+X_BD.
    rebase = sp.Matrix(
        (
            (1, -1, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0),
            (0, 0, 1, 1, 0, 0),
            (0, 0, 0, 1, 0, 0),
            (0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 1),
        )
    )
    rebased = sp.simplify(rebase * raw)
    expected_rebased = sp.Matrix(
        (0, 2, 1, sp.Rational(4, 3), -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)
    )
    ledger.check("RAW_TO_X_T_REBASING", rebased, expected_rebased)
    ledger.check("G1_X_E_TO_X_T", rebased[:2, :], sp.Matrix((0, 2)))
    ledger.check("G2_X_E_TO_X_T", rebased[2:4, :], sp.Matrix((1, sp.Rational(4, 3))))

    compact_projection = sp.Matrix(
        (
            (1, 0, 0, 0, 0, 0),
            (0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 1),
        )
    )
    common_td = sp.simplify(compact_projection * rebased)
    expected_td = sp.Matrix((0, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2))
    ledger.check("COMMON_TD_FROM_RAW_REBASING", common_td, expected_td)
    ledger.check("COMMON_TD_MATCHES_ACCEPTED_SOURCE", common_td, source_common_td)

    hybrid = sp.Matrix(tuple(parse(item) for item in project["hybrid_vector_rejected"]))
    ledger.check(
        "OBSOLETE_HYBRID_REJECTED",
        hybrid,
        sp.Matrix((2, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2)),
    )
    ledger.check("OBSOLETE_HYBRID_DIFFERS_FROM_COMMON_TD", hybrid == common_td, False)

    renormalized = sp.simplify(common_td + finite_delta)
    expected_renormalized = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    ledger.check("FINITE_NORMAL_PRODUCT_SETTLEMENT", renormalized, expected_renormalized)

    q_matrix = sp.Matrix(
        (
            (1, -1, 0, 0),
            (imaginary * sqrt2, 0, 1, 0),
            (-imaginary * sqrt2, 0, 0, 1),
        )
    )
    ledger.check("RENORMALIZED_PROJECT_WARD", q_matrix * renormalized, sp.zeros(3, 1))
    ledger.check("PROJECT_WARD_KERNEL_NULLITY", len(q_matrix.nullspace()), 1)

    return {
        "raw_basis": ["X_DB", "E_DB", "X_BD", "E_BD", "C23", "C32"],
        "raw_vector": [exact_text(item) for item in raw],
        "relations": ["T_DB=X_DB+E_DB", "T_BD=-X_BD+E_BD"],
        "rebased_basis": ["X_DB", "T_DB", "X_BD", "T_BD", "C23", "C32"],
        "rebased_vector": [exact_text(item) for item in rebased],
        "compact_basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
        "common_TD_vector": [exact_text(item) for item in common_td],
        "rejected_hybrid_vector": [exact_text(item) for item in hybrid],
        "finite_normal_product_vector": [exact_text(item) for item in finite_delta],
        "renormalized_vector": [exact_text(item) for item in renormalized],
        "renormalized_q_Ward": [exact_text(item) for item in q_matrix * renormalized],
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    g3_payload, g3_sha256 = load_with_binding(G3_MEASURE_IN)
    finite_payload, finite_sha256 = load_with_binding(FINITE_IN)

    g3_retraction = validate_g3_source(g3_payload, ledger)
    project, g1_eom, g2_eom, common_td, finite_delta = validate_finite_source(
        finite_payload, ledger
    )
    cutting = dred_cutting_identity(ledger)
    master = finite_master(ledger)
    carrier = rebase_and_settle(
        project,
        g1_eom,
        g2_eom,
        common_td,
        finite_delta,
        ledger,
    )

    failed = [row for row in ledger.rows if row["status"] != "PASS"]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    return {
        "schema": SCHEMA,
        "status": STATUS,
        "artifact_role": "HISTORICAL_RETRACTION_REGRESSION",
        "accepted_as_positive_derivation": False,
        "external_target_used_in_derivation": False,
        "holomorphic_twist_read": False,
        "project_result_engine_read": False,
        "derivation_sources": [
            {
                "path": str(G3_MEASURE_IN.relative_to(ROOT)),
                "sha256": g3_sha256,
                "semantic_gate": "exact original/full measure and two-cycle census",
            },
            {
                "path": str(FINITE_IN.relative_to(ROOT)),
                "sha256": finite_sha256,
                "semantic_gate": "sealed common-TD and finite normal-product settlement",
                "project_seal_sha256": finite_payload["project_seal_sha256"],
            },
        ],
        "definitions": {
            "d": "4-2*epsilon",
            "mu_l_squared": "bar(l)^2-l_d^2=-hat(l)_user^2",
            "finite_master": exact_text(master),
            "lambda1": "hbar*g^2/(16*pi^2)",
        },
        "DRED_cutting_failure": cutting,
        "historical_retraction": g3_retraction,
        "carrier_rebasing_and_finite_settlement": carrier,
        "raw_G1_boundary": {
            "status": "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
            "generic_pq_occurrence_result_is_not_used": True,
            "reason": (
                "the rejected generic-p,q occurrence lift is not restored by this "
                "historical retraction"
            ),
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    g3_source = payload["derivation_sources"][0]
    finite_source = payload["derivation_sources"][1]
    return f"""# AB/BA full-1PI quotient historical retraction

Status: `{STATUS}`.

This filename is retained only as a regression tombstone. It is not an accepted positive derivation.

## 1. Notation

$$
d=4-2\\epsilon,
\\qquad
\\mu_\\ell^2=\\bar\\ell^2-\\ell_d^2=-\\widehat\\ell_{{\\rm user}}^2,
\\qquad
D_i=r_{{i,d}}^2.
$$

## 2. Exact DRED cutting failure

$$
\\frac{{D_e}}{{D_0D_1D_2}}-\\frac1{{\\prod_{{j\\ne e}}D_j}}=0.
$$

$$
\\frac{{\\bar r_e^2}}{{D_0D_1D_2}}-\\frac1{{\\prod_{{j\\ne e}}D_j}}
=\\frac{{D_e+\\mu_\\ell^2}}{{D_0D_1D_2}}-\\frac{{D_e}}{{D_0D_1D_2}}
=\\frac{{\\mu_\\ell^2}}{{D_0D_1D_2}}.
$$

$$
\\int\\frac{{d^dL}}{{(2\\pi)^d}}\\frac{{\\mu_L^2}}{{(L_d^2+\\Delta)^3}}
=\\frac1{{32\\pi^2}}.
$$

## 3. Retracted G3 normalization

Exact original/full measures give

$$
32768\\left(\\frac14\\right)_M\\left(\\frac12\\right)_{{\\bar H}}
=65536\\left(\\frac14\\right)_M\\left(\\frac14\\right)_H
=4096.
$$

There are two correlated nonzero supertrace cycles:

$$
\\frac12(C_1+C_2)=C_1,
\\qquad C_2=C_1.
$$

The first false equality was

$$
\\boxed{{\\frac12(C_1+C_2)\\longrightarrow\\frac12C_1}},
$$

which changes

$$
4096\\longrightarrow2048.
$$

Therefore

$$
\\mathfrak I[1-z]=\\frac23,
\\qquad
\\mathfrak I[z]=\\frac13,
\\qquad
\\frac23+\\frac13=1
$$

fixes only the simplex shape, not the absolute graph multiplicity. The old scale-one G3 conclusion is retracted.

## 4. Exact raw-carrier rebasing

In the basis

$$
(X_{{DB}},E_{{DB}},X_{{BD}},E_{{BD}},C_{{23}},C_{{32}}),
$$

$$
v_{{\\rm raw}}
=\\left(2,2,-\\frac13,\\frac43,-2i\\sqrt2,2i\\sqrt2\\right).
$$

Using

$$
T_{{DB}}=X_{{DB}}+E_{{DB}},
\\qquad
T_{{BD}}=-X_{{BD}}+E_{{BD}},
$$

$$
(2,2)_{{(X,E)}}=(0,2)_{{(X,T)}},
$$

$$
\\left(-\\frac13,\\frac43\\right)_{{(X,E)}}
=\\left(1,\\frac43\\right)_{{(X,T)}}.
$$

Hence

$$
v_{{\\rm TD}}=\\left(0,1,-2i\\sqrt2,2i\\sqrt2\\right).
$$

The hybrid vector

$$
\\left(2,1,-2i\\sqrt2,2i\\sqrt2\\right)
$$

mixes the G1 EOM projection with the G2 TD projection and is rejected.

## 5. Accepted finite normal product

$$
\\delta_{{\\rm fin}}
=\\left(1,0,i\\sqrt2,-i\\sqrt2\\right),
$$

$$
v_{{\\rm ren}}
=v_{{\\rm TD}}+\\delta_{{\\rm fin}}
=\\left(1,1,-i\\sqrt2,i\\sqrt2\\right).
$$

For

$$
M_q=
\\begin{{pmatrix}}
1&-1&0&0\\\\
i\\sqrt2&0&1&0\\\\
-i\\sqrt2&0&0&1
\\end{{pmatrix}},
$$

$$
M_qv_{{\\rm ren}}=0.
$$

The finite term is a composite-source normal-product scheme term, not an additional anomaly graph.

## 6. Bound evidence

- `{g3_source['path']}`: `{g3_source['sha256']}`
- `{finite_source['path']}`: `{finite_source['sha256']}`
- finite Project seal: `{finite_source['project_seal_sha256']}`

No holomorphic-twist artifact and no Project result engine enters this retraction derivation.

Checks: `{payload['checks']['passed']}/{payload['checks']['count']}` exact PASS.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()

    payload = build_artifact()
    rendered_json = canonical(payload)
    rendered_md = markdown(payload)

    if args.write:
        JSON_OUT.write_text(rendered_json, encoding="utf-8")
        MD_OUT.write_text(rendered_md, encoding="utf-8")
    if args.check or args.check_artifact:
        if JSON_OUT.read_text(encoding="utf-8") != rendered_json:
            raise AssertionError(f"stored JSON artifact is stale or tampered: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != rendered_md:
            raise AssertionError(f"stored Markdown artifact is stale or tampered: {MD_OUT}")
    if args.print_json:
        print(rendered_json, end="")
    else:
        print("PASS HISTORICAL_RETRACTION false G3 scale-one normalization")
        print("PASS first false equality (1/2)*(C1+C2) -> (1/2)*C1")
        print("PASS vraw -> vTD -> vren exact rebasing and finite settlement")
        print("PASS DRED cutting failure finite master 1/(32*pi^2)")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
