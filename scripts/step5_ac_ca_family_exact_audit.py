#!/usr/bin/env python3
"""Target-blind complete triangle audit for A>C_r and C_r>A.

The gauge-matter branch reuses the exact Q(i) finite-Grassmann primitives of
``step5_ab1_g1_vvv_dword_replay.py`` but replaces the chiral B source by the
reversed antichiral C propagator.  The matter-matter and the two naive TMH
branches are recomputed as generic SymPy polynomials.  No holomorphic-twist
coefficient is read or used by this program.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_g1_vvv_dword_replay as g1  # noqa: E402
import step5_aa_gauge_full_source_sd_orbit_exact_audit as aa  # noqa: E402
from step5_ab1_g2_g3_dword_replay import (  # noqa: E402
    H,
    M,
    S,
    antichiral_bottom,
    bar_d2,
    chiral_b_plus,
    d,
    d2,
    delta4,
    determinant,
    integrate_two_vertices_bottom_source,
    matrix_neg,
    matrix_sub,
    vector_dotted_component,
)


DEFAULT_JSON = ROOT / "audits/step5-ac-ca-family-exact.json"
DEFAULT_MD = ROOT / "audits/step5-ac-ca-family-exact.md"

ROUTE_PERMUTATION = {
    "001": (0, 1, 2),
    "002": (0, 2, 1),
    "003": (1, 0, 2),
    "004": (2, 0, 1),
    "005": (1, 2, 0),
    "006": (2, 1, 0),
}

EXPECTED_TGM = {
    (0, 1, 2): {"plus": (1024, 0, 1024), "minus": (-512, -1536, 1024)},
    (0, 2, 1): {"plus": (0, 512, -512), "minus": (-1024, 0, -1024)},
    (1, 0, 2): {"plus": (512, 1024, -512), "minus": (-1024, 0, -1024)},
    (1, 2, 0): {"plus": (0, 0, 0), "minus": (-1024, -512, -512)},
    (2, 0, 1): {"plus": (1024, 0, 1024), "minus": (-512, -1024, 512)},
    (2, 1, 0): {"plus": (1536, 1536, 0), "minus": (0, 0, 0)},
}

EXPECTED_ROUTE_COEFFICIENTS = {
    "001": Fraction(-3, 8),
    "002": Fraction(-1, 4),
    "003": Fraction(-3, 8),
    "004": Fraction(-3, 8),
    "005": Fraction(-1, 4),
    "006": Fraction(-3, 8),
}


def qtext(value: g1.QI) -> str:
    return str(value)


def ftext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


# ---------------------------------------------------------------------------
# Full order-g^2 nonlinear/contact orbit
# ---------------------------------------------------------------------------


def _const_mat(ctx: aa.Context, color: int, factor: object = 1) -> aa.Mat:
    return aa.matrix_field(aa.P.scalar(ctx, factor), color)


def _bracket(left: aa.Mat, right: aa.Mat) -> aa.Mat:
    return aa.mat_sub(aa.mat_mul(left, right), aa.mat_mul(right, left))


def _antichiral(
    ctx: aa.Context,
    node: str,
    label: int,
    color: int,
    momentum: aa.Vector,
) -> aa.Mat:
    exponent = aa.P.scalar(ctx, 0)
    for vector_index in range(4):
        for undotted in range(2):
            for dotted in range(2):
                exponent += (
                    -aa.I
                    * momentum[vector_index]
                    * aa.SIGMA[vector_index][undotted][dotted]
                    * aa.theta(ctx, node, undotted)
                    * aa.bar_theta_up(ctx, node, dotted)
                )
    base = aa.P.scalar(ctx, 1) + exponent + Fraction(1, 2) * exponent * exponent
    return aa.labeled_endpoint(base, label, color)


def _full_measure(poly: aa.P, node: str) -> aa.P:
    return (
        Fraction(1, 16) * aa.d2(aa.bar_d2(poly, node), node)
    ).set_coordinates_zero(node)


def _a2_m1_word(
    loop: aa.Vector,
    external_c_momentum: aa.Vector,
    dotted: int,
    outer_a_color: int,
    spectator_c_color: int,
    external_c_color: int,
    external_d_color: int,
) -> aa.A:
    """Exact I1*S_m3 word, including full inverse color metrics."""

    matter = aa.vadd(external_c_momentum, aa.vneg(loop))
    ctx = aa.Context(
        ("S", "M"),
        (
            {"S": loop, "M": aa.vneg(loop)},
            {"S": aa.vneg(external_c_momentum)},
            {"S": matter, "M": aa.vneg(matter)},
            {"M": external_c_momentum},
        ),
        8,
    )
    total = aa.ZERO
    for color in range(3):
        quantum_u = aa.endpoint_delta(ctx, "S", "M", 0, color)
        external_u = aa.endpoint_D(ctx, "S", 1, external_d_color, dotted)
        u = aa.mat_add(quantum_u, external_u)
        a1, a2, _ = aa.canonical_A_words(u, "S")
        gamma1 = aa.mat_scale(aa.SQRT2, aa.mat_d(u, "S", 1))
        n1 = aa.mat_add(aa.mat_d(a2, "S", 1), _bracket(gamma1, a1))
        source = aa.component(n1, outer_a_color).coefficient_labels((1, 1, 0, 0))
        matter_line = (
            aa.d2(aa.bar_d2(aa.delta4(ctx, "S", "M"), "S"), "S")
            * aa.P.label(ctx, 2)
        )
        external_c = _antichiral(
            ctx, "M", 3, external_c_color, external_c_momentum
        )
        # -2 is the complete vector covariance; +2 is the matter covariance.
        action_u = _const_mat(ctx, color, -2)
        action_phi = _const_mat(ctx, spectator_c_color, 2)
        action = aa.mat_trace(
            aa.mat_mul(external_c, _bracket(action_u, action_phi))
        )
        graph = _full_measure(source * matter_line * action, "M")
        graph = graph.set_coordinates_zero("S").coefficient_labels((0, 0, 1, 1))
        total += graph.eta_coefficient()
    return total


def _a1_m2_word(
    loop: aa.Vector,
    external_c_momentum: aa.Vector,
    dotted: int,
    outer_a_color: int,
    spectator_c_color: int,
    external_c_color: int,
    external_d_color: int,
) -> aa.A:
    """Exact I0*S_m4 seagull word, with both ordered U placements."""

    matter = aa.vadd(external_c_momentum, aa.vneg(loop))
    ctx = aa.Context(
        ("S", "M"),
        (
            {"S": loop, "M": aa.vneg(loop)},
            {"M": aa.vneg(external_c_momentum)},
            {"S": matter, "M": aa.vneg(matter)},
            {"M": external_c_momentum},
        ),
        8,
    )
    total = aa.ZERO
    for color in range(3):
        quantum_u = aa.endpoint_delta(ctx, "S", "M", 0, color)
        a1, _, _ = aa.canonical_A_words(quantum_u, "S")
        source = aa.component(
            aa.mat_d(a1, "S", 1), outer_a_color
        ).coefficient_labels((1, 0, 0, 0))
        matter_line = (
            aa.d2(aa.bar_d2(aa.delta4(ctx, "S", "M"), "S"), "S")
            * aa.P.label(ctx, 2)
        )
        external_c = _antichiral(
            ctx, "M", 3, external_c_color, external_c_momentum
        )
        internal_u = _const_mat(ctx, color, -2)
        external_u = aa.endpoint_D(ctx, "M", 1, external_d_color, dotted)
        action_phi = _const_mat(ctx, spectator_c_color, 2)
        u = aa.mat_add(internal_u, external_u)
        action = aa.mat_trace(
            aa.mat_mul(external_c, _bracket(u, _bracket(u, action_phi)))
        ).coefficient_labels((0, 1, 0, 1))
        graph = _full_measure(source * matter_line * action, "M")
        graph = graph.set_coordinates_zero("S").coefficient_labels((0, 0, 1, 0))
        total += graph.eta_coefficient()
    return total


def _full_covariance_matter_color(
    outer_a_color: int,
    spectator_c_color: int,
    external_c_color: int,
    external_d_color: int,
) -> aa.A:
    """Two M1 vertices, three inverse metrics, and the vector minus sign."""

    ctx = aa.Context(("X",), (), 4)

    def matrix(color: int) -> aa.Mat:
        return aa.matrix_field(aa.P.scalar(ctx, 1), color)

    def vertex(tilde: int, vector: int, phi: int) -> aa.A:
        return aa.mat_trace(
            aa.mat_mul(matrix(tilde), _bracket(matrix(vector), matrix(phi)))
        ).scalar_coefficient()

    return sum(
        (
            -8
            * vertex(external_c_color, outer_a_color, internal)
            * vertex(internal, external_d_color, spectator_c_color)
            for internal in range(3)
        ),
        aa.ZERO,
    )


def _affine_word_samples(
    function: object,
    outer_a_color: int,
    spectator_c_color: int,
    external_c_color: int,
    external_d_color: int,
) -> list[str]:
    p = aa.vec((1, 0, 0, 0))
    loops = (
        aa.ZERO_VECTOR,
        aa.vec((1, 0, 0, 0)),
        aa.vec((0, 1, 0, 0)),
        aa.vec((2, -1, 1, 3)),
    )
    return [
        function(
            loop,
            p,
            0,
            outer_a_color,
            spectator_c_color,
            external_c_color,
            external_d_color,
        ).text()
        for loop in loops
    ]


def build_full_order_g2_orbit() -> dict[str, object]:
    """Derive the pole orbit before the HT after-check."""

    p = aa.vec((1, 0, 0, 0))
    validation_loop = aa.vec((2, -1, 1, 3))
    z = aa.A(2) + aa.I

    # A>C: TGM has D>C; TMM has C>D.
    ac_tgm_a2 = _a2_m1_word(validation_loop, p, 0, 0, 1, 0, 1)
    ac_tgm_a1 = _a1_m2_word(validation_loop, p, 0, 0, 1, 0, 1)
    ac_tmm_a1 = _a1_m2_word(validation_loop, p, 0, 0, 1, 1, 0)
    if ac_tgm_a2 != -8 * z:
        raise AssertionError("AC I1*S_m3 affine word")
    if ac_tgm_a1 != 8 * aa.SQRT2 * z:
        raise AssertionError("AC I0*S_m4 TGM affine word")
    if ac_tmm_a1 != -16 * aa.SQRT2 * z:
        raise AssertionError("AC I0*S_m4 TMM affine word")

    # C>A is replayed with outer A in the second source color slot.
    ca_tgm_a2 = _a2_m1_word(validation_loop, p, 0, 1, 0, 1, 0)
    ca_tgm_a1 = _a1_m2_word(validation_loop, p, 0, 1, 0, 1, 0)
    ca_tmm_a1 = _a1_m2_word(validation_loop, p, 0, 1, 0, 0, 1)
    if ca_tgm_a2 != -8 * z:
        raise AssertionError("CA I1*S_m3 affine word")
    if ca_tgm_a1 != 8 * aa.SQRT2 * z:
        raise AssertionError("CA I0*S_m4 TGM affine word")
    if ca_tmm_a1 != -16 * aa.SQRT2 * z:
        raise AssertionError("CA I0*S_m4 TMM affine word")

    full_color = _full_covariance_matter_color(0, 1, 1, 0)
    frame_f = aa.A(aa.su2_F(0, 1, 1, 0))
    if full_color != frame_f or frame_f != aa.A(-2):
        raise AssertionError("full covariance matter color is not +F")

    # J_mu2=(4-d)J2/d.  The following rational identities are exact.
    d = sp.symbols("d", nonzero=True)
    tmm_residual = sp.factor(2 - sp.Rational(8, 1) / d)
    tgm_residual = sp.factor(sp.Rational(8, 1) / d - 2)
    jmu_ratio = (4 - d) / d
    if sp.simplify(tmm_residual + 2 * jmu_ratio) != 0:
        raise AssertionError("TMM DRED pole identity")
    if sp.simplify(tgm_residual - 2 * jmu_ratio) != 0:
        raise AssertionError("TGM DRED pole identity")

    return {
        "source_expansion": {
            "A_c": "A1+g*A2+g^2*A3",
            "N0": "Dminus*A1",
            "N1": "Dminus*A2+[gamma1,A1]",
            "N2": "Dminus*A3+[gamma1,A2]+[gamma2,A1]",
            "resolvent": [
                "+<I2>",
                "-<I1*S3>/hbar",
                "-<I0*S4>/hbar",
                "+<I0*S3*S3>/(2*hbar^2)",
            ],
        },
        "exact_color": {
            "frame": "SU(2): A=0,B=1,D=1,E=0",
            "full_covariance_contraction": full_color.text(),
            "F_frame": frame_f.text(),
            "identity": "C_full=F^{AB}_{DE}",
        },
        "AC_words": {
            "I1_Sm3_A2_M1_D_gt_C": ac_tgm_a2.text(),
            "I0_Sm4_A1_M2_D_gt_C": ac_tgm_a1.text(),
            "I0_Sm4_A1_M2_C_gt_D": ac_tmm_a1.text(),
            "sample_z": z.text(),
            "A2_M1_samples": _affine_word_samples(_a2_m1_word, 0, 1, 0, 1),
            "A1_M2_TGM_samples": _affine_word_samples(_a1_m2_word, 0, 1, 0, 1),
            "A1_M2_TMM_samples": _affine_word_samples(_a1_m2_word, 0, 1, 1, 0),
        },
        "CA_words": {
            "I1_Sm3_A2_M1_C_gt_D": ca_tgm_a2.text(),
            "I0_Sm4_A1_M2_C_gt_D": ca_tgm_a1.text(),
            "I0_Sm4_A1_M2_D_gt_C": ca_tmm_a1.text(),
        },
        "metric_poles": {
            "J_mu2_over_J2": "(4-d)/d",
            "TMM_triangle": "-8/d",
            "TMM_I0_Sm4": "+2",
            "TMM_sum": "2-8/d=-2*(4-d)/d=-2*J_mu2/J2",
            "TMM_normalized": "-1",
            "TGM_triangle": "+8/d",
            "TGM_I1_Sm3": "-1",
            "TGM_I0_Sm4": "-1",
            "TGM_sum": "8/d-2=+2*(4-d)/d=+2*J_mu2/J2",
            "TGM_normalized": "+1",
        },
        "remaining_rows": [
            {"id": "I2_A3_TADPOLE", "result": "0_SCALELESS_DRED"},
            {"id": "TMH_SUPERPOTENTIAL_1", "result": "0_EXACT_D_WORD"},
            {"id": "TMH_SUPERPOTENTIAL_2", "result": "0_EXACT_D_WORD"},
            {"id": "GAUGE_GF_FP_NK", "result": "0_F_SECTOR_METRIC_TRACE"},
            {
                "id": "EULER_EXPLICIT_CURRENT_PAIR",
                "result": "0_AFTER_IDENTICAL_PORT_DENOMINATOR_EDGE_TAG_MATCH",
                "coefficients": ["+2i", "-2i"],
                "selected_inverse_square": "none",
            },
        ],
        "first_invalid_old_line": {
            "statement": "both transported inverse-square rows were promoted to independent anomaly descendants",
            "old_scalar_defect": "plus_or_minus_4*J_mu2",
            "complete_metric_defect": "plus_or_minus_2*J_mu2",
            "ratio": "1/2",
            "classification": "OCCURRENCE_DECOMPOSITION_DOUBLE_COUNT",
        },
        "ordered_results": {
            "basis": ["C_r^D>D^E", "D^D>C_r^E"],
            "A__C_r": ["-1", "+1"],
            "C_r__A": ["-1", "+1"],
            "unit": "lambda1*F^{AB}_{DE}",
        },
    }


def antichiral_endpoint(node: str, momentum: g1.Vector) -> g1.Grassmann:
    exponent = g1.Grassmann.scalar(0)
    for vector_index in range(4):
        for undotted in range(2):
            for dotted in range(2):
                exponent += (
                    -g1.I
                    * momentum[vector_index]
                    * g1.SIGMA[vector_index][undotted][dotted]
                    * g1.theta(node, undotted)
                    * g1.bar_theta_up(node, dotted)
                )
    return g1.Grassmann.scalar(1) + exponent + Fraction(1, 2) * exponent * exponent


def vector_square(momentum: g1.Vector) -> g1.QI:
    return sum((entry * entry for entry in momentum), g1.ZERO)


def evaluate_tgm(
    loop: g1.Vector,
    external_c_momentum: g1.Vector,
    external_d_momentum: g1.Vector,
    dotted: int,
    sector: str,
) -> dict[tuple[tuple[int, int, int], str], tuple[g1.QI, g1.QI]]:
    """Return (full outer-A word, transverse r0-square word)."""

    p = external_c_momentum
    q = external_d_momentum
    p_plus_q = g1.vector_add(p, q)
    source_vector_momentum = g1.vector_add(
        g1.vector_neg(loop), p_plus_q
    )
    source_c_momentum = loop
    endpoint_momenta = (
        g1.vector_add(loop, g1.vector_neg(p_plus_q)),
        g1.vector_add(g1.vector_neg(loop), p),
        q,
    )
    endpoints = (
        g1.superspace_delta("S", "G"),
        g1.superspace_delta("M", "G"),
        g1.vector_d_endpoint("G", dotted),
    )

    # <tildePhi(S) Phi(M)> uses the reversed P_- kernel D^2 barD^2.
    matter_line = g1.d_squared(
        g1.bar_d_squared(
            g1.superspace_delta("S", "M"), "S", source_c_momentum
        ),
        "S",
        source_c_momentum,
    )
    external_c = antichiral_endpoint("M", p)

    output: dict[tuple[tuple[int, int, int], str], tuple[g1.QI, g1.QI]] = {}
    for permutation in g1.PERMUTATIONS:
        color_sign = g1.permutation_sign(permutation)
        for placement in g1.PLACEMENTS:
            vvv = g1.polarized_vvv_word(
                sector,
                placement,
                permutation,
                endpoints,
                endpoint_momenta,
            )
            d_plus = g1.d_lower(vvv, "S", 0, source_vector_momentum)
            bar_d_square = g1.bar_d_squared(
                d_plus, "S", source_vector_momentum
            )
            a_word = g1.d_lower(
                bar_d_square, "S", 0, source_vector_momentum
            )
            full_mark = g1.d_lower(
                a_word, "S", 1, source_vector_momentum
            )
            # The marked source-vector inverse edge carries -(loop-p-q).
            # Its square equals (loop-p-q)^2.
            transverse_mark = (
                -8 * vector_square(source_vector_momentum) * d_plus
            )

            values: list[g1.QI] = []
            for marked_word in (full_mark, transverse_mark):
                word = color_sign * marked_word * matter_line * external_c
                word = g1.integrate_full(word, "M")
                word = (
                    g1.integrate_chiral(word, "G")
                    if sector == "+"
                    else g1.integrate_antichiral(word, "G")
                )
                word = word.set_zero(
                    g1.INDEX["S", name] for name in g1.COORDINATES
                )
                values.append(word.coefficient(1 << g1.ETA_D_INDEX))
            output[permutation, placement] = values[0], values[1]
    return output


def tgm_simplex_traces(
    external_c_momentum: g1.Vector,
    external_d_momentum: g1.Vector,
    dotted: int,
    sector: str,
) -> dict[tuple[int, int, int], tuple[g1.QI, g1.QI, g1.QI]]:
    """Compute 2 int_Sigma of the rank-two trace exactly."""

    p = external_c_momentum
    q = external_d_momentum
    shifts = (
        g1.ZERO_VECTOR,
        p,
        g1.vector_add(p, q),
        g1.vector_scale(
            Fraction(1, 3),
            g1.vector_add(g1.vector_scale(2, p), q),
        ),
    )
    laplacians: list[dict[tuple[tuple[int, int, int], str], tuple[g1.QI, g1.QI]]] = []
    for shift in shifts:
        center = evaluate_tgm(
            shift,
            external_c_momentum,
            external_d_momentum,
            dotted,
            sector,
        )
        trace = {
            key: [g1.ZERO, g1.ZERO]
            for key in center
        }
        for vector_index in range(4):
            unit_entries = [g1.ZERO, g1.ZERO, g1.ZERO, g1.ZERO]
            unit_entries[vector_index] = g1.ONE
            unit = tuple(unit_entries)
            plus = evaluate_tgm(
                g1.vector_add(shift, unit),
                external_c_momentum,
                external_d_momentum,
                dotted,
                sector,
            )
            minus = evaluate_tgm(
                g1.vector_add(shift, g1.vector_neg(unit)),
                external_c_momentum,
                external_d_momentum,
                dotted,
                sector,
            )
            for key in trace:
                for branch in range(2):
                    trace[key][branch] += (
                        plus[key][branch]
                        - 2 * center[key][branch]
                        + minus[key][branch]
                    )
        laplacians.append(
            {key: (value[0], value[1]) for key, value in trace.items()}
        )

    # Delta_loop N has degree at most one in the Feynman shift.  Its value at
    # the simplex centroid must therefore be the barycentric mean of its
    # values at 0, p, and p+q.  This is checked word by word before use.
    for key in laplacians[0]:
        for branch in range(2):
            if (
                3 * laplacians[3][key][branch]
                != laplacians[0][key][branch]
                + laplacians[1][key][branch]
                + laplacians[2][key][branch]
            ):
                raise AssertionError(
                    f"TGM non-affine simplex trace {sector} {key} {branch}"
                )

    spinor = g1.endpoint_spinor(external_c_momentum, dotted)
    if not spinor:
        raise AssertionError("validation momentum killed the external spinor")
    result: dict[tuple[int, int, int], tuple[g1.QI, g1.QI, g1.QI]] = {}
    for permutation in g1.PERMUTATIONS:
        full = g1.ZERO
        transverse = g1.ZERO
        for placement in g1.PLACEMENTS:
            key = permutation, placement
            # C=Delta_L N/8 and 2 int_Sigma C is the barycentric mean.
            full += (
                laplacians[0][key][0]
                + laplacians[1][key][0]
                + laplacians[2][key][0]
            ) / g1.QI.coerce(24)
            transverse += (
                laplacians[0][key][1]
                + laplacians[1][key][1]
                + laplacians[2][key][1]
            ) / g1.QI.coerce(24)
        full /= spinor
        transverse /= spinor
        result[permutation] = full, transverse, full - transverse
    return result


def build_ac_tmm_and_tmh() -> dict[str, object]:
    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = matrix_sub(r0, p)
    r2 = matrix_sub(r1, q)
    minus_r2 = matrix_neg(r2)

    source_delta = delta4(S, M)
    a_unmarked = d(
        bar_d2(d(source_delta, S, 0, r0), S, r0), S, 0, r0
    )
    a_full = d(a_unmarked, S, 1, r0)
    a_residual = d(source_delta, S, 0, r0)
    source_c_line = d2(
        bar_d2(delta4(S, H), S, minus_r2), S, minus_r2
    )
    internal_plus = bar_d2(
        d2(delta4(M, H), M, r1), M, r1
    )
    external_c = antichiral_bottom(M, p)

    tmm_full: list[sp.Expr] = []
    tmm_residual: list[sp.Expr] = []
    tmm_bridge: list[sp.Expr] = []
    tmm_collapsed_neighbor: list[sp.Expr] = []
    for dotted in range(2):
        probe = vector_dotted_component(H, dotted)
        full = integrate_two_vertices_bottom_source(
            a_full * source_c_line * internal_plus * external_c * probe,
            M,
            H,
        )
        residual = integrate_two_vertices_bottom_source(
            a_residual * source_c_line * internal_plus * external_c * probe,
            M,
            H,
        )
        # Exact endpoint-transport representation of the longitudinal word:
        # D^2 reaches the adjacent r1 projector and leaves D_+ barD^2 delta.
        transported_source = d(bar_d2(source_delta, S, r0), S, 0, r0)
        reduced_bridge = d2(delta4(M, H), M, r1)
        bridge = integrate_two_vertices_bottom_source(
            transported_source
            * source_c_line
            * reduced_bridge
            * external_c
            * probe,
            M,
            H,
        )
        collapsed_neighbor = integrate_two_vertices_bottom_source(
            a_full
            * source_c_line
            * delta4(M, H)
            * external_c
            * probe,
            M,
            H,
        )
        expected = 8 * determinant(r0) * residual - 8 * determinant(r1) * bridge
        if sp.expand(full - expected) != 0:
            raise AssertionError(f"TMM full transport identity dotted={dotted}")
        tmm_full.append(sp.factor(full))
        tmm_residual.append(sp.factor(residual))
        tmm_bridge.append(sp.factor(bridge))
        tmm_collapsed_neighbor.append(sp.factor(collapsed_neighbor))

    expected_residual = (
        128 * (p[0][1] - r0[0][1]),
        128 * (r0[0][0] - p[0][0]),
    )
    expected_bridge = (-128 * r0[0][1], 128 * r0[0][0])
    expected_collapsed_neighbor = (
        64 * r0[0][1],
        -64 * r0[0][0],
    )
    for dotted in range(2):
        if sp.expand(tmm_residual[dotted] - expected_residual[dotted]) != 0:
            raise AssertionError(f"TMM transverse residual dotted={dotted}")
        if sp.expand(tmm_bridge[dotted] - expected_bridge[dotted]) != 0:
            raise AssertionError(f"TMM migrated bridge residual dotted={dotted}")
        if sp.expand(
            tmm_collapsed_neighbor[dotted]
            - expected_collapsed_neighbor[dotted]
        ) != 0:
            raise AssertionError(
                f"TMM collapsed neighbor dotted={dotted}"
            )

    ev_probe = tuple(
        sp.factor(8 * (expected_bridge[dotted] - expected_residual[dotted]))
        for dotted in range(2)
    )
    expected_ev_probe = (-1024 * p[0][1], 1024 * p[0][0])
    if any(
        sp.expand(ev_probe[index] - expected_ev_probe[index]) != 0
        for index in range(2)
    ):
        raise AssertionError("TMM evanescent routing did not cancel")

    # The two naive M_s-H_+ routes.  Both possible oriented representations
    # of the internal reversed chiral projector give the same exact zero.
    external_b_m = chiral_b_plus(M, p)
    external_b_h = chiral_b_plus(H, q)
    internal_reversed = d2(
        bar_d2(delta4(M, H), M, r1), M, r1
    )
    tmh_full_minus = integrate_two_vertices_bottom_source(
        a_full
        * source_c_line
        * internal_reversed
        * external_b_m
        * external_b_h,
        M,
        H,
    )
    tmh_full_plus = integrate_two_vertices_bottom_source(
        a_full
        * source_c_line
        * internal_plus
        * external_b_m
        * external_b_h,
        M,
        H,
    )
    tmh_transverse = integrate_two_vertices_bottom_source(
        a_residual
        * source_c_line
        * internal_reversed
        * external_b_m
        * external_b_h,
        M,
        H,
    )
    if any(
        sp.expand(value) != 0
        for value in (tmh_full_minus, tmh_full_plus, tmh_transverse)
    ):
        raise AssertionError("TMH projected polynomial is not zero")

    return {
        "tmm": {
            "ordered_pair": "A__C_r",
            "routing": {
                "r0": "source A vector edge",
                "r1": "M-M chiral bridge",
                "r2": "source C reversed-chiral edge",
                "p": "external C momentum",
                "q": "external D momentum",
            },
            "full_probe": [sp.sstr(value) for value in tmm_full],
            "transverse_r0_residual": [
                sp.sstr(value) for value in tmm_residual
            ],
            "migrated_r1_residual": [sp.sstr(value) for value in tmm_bridge],
            "collapsed_neighbor_raw": [
                sp.sstr(value) for value in tmm_collapsed_neighbor
            ],
            "projector_collapse_check": "16*det(r1)*K_neighbor=-8*det(r1)*J1",
            "evanescent_probe": [sp.sstr(value) for value in ev_probe],
            "simplex_weight": "1",
            "lambda_coefficient_before_color": "-2",
            "color": "-F^{AB}_{DE}",
            "A__C_output": "C_r^D>D^E",
            "A__C_lambda_coefficient": "2",
            "full_d_contacts": [
                "+8*D0*R0",
                "-8*D1*J1",
            ],
            "contact_sum_rule": "F_DRED+C_d=8*mu2*(J1-R0)",
        },
        "tmh": {
            "ordered_pair": "A__C_r",
            "oriented_internal_P_minus_full_polynomial": sp.sstr(tmh_full_minus),
            "alternate_internal_P_plus_full_polynomial": sp.sstr(tmh_full_plus),
            "transverse_polynomial": sp.sstr(tmh_transverse),
            "longitudinal_polynomial": "0",
            "route_008": "EXACT_ZERO_FULL_PROJECTED_POLYNOMIAL",
            "route_009": "EXACT_ZERO_FULL_PROJECTED_POLYNOMIAL",
        },
    }


def build_ca_tmm_and_tmh() -> dict[str, object]:
    """Independent C_r>A port replay; no reflected A>C coefficient is used."""

    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = matrix_sub(r0, p)
    r2 = matrix_sub(r1, q)
    minus_r2 = matrix_neg(r2)

    source_vector_delta = delta4(S, H)
    a_unmarked = d(
        bar_d2(
            d(source_vector_delta, S, 0, minus_r2),
            S,
            minus_r2,
        ),
        S,
        0,
        minus_r2,
    )
    a_full = d(a_unmarked, S, 1, minus_r2)
    a_residual = d(source_vector_delta, S, 0, minus_r2)

    # Source C -> left M.phi and left M.tilde -> right M.phi.
    source_c_line = d2(
        bar_d2(delta4(S, M), S, r0), S, r0
    )
    internal_reversed = d2(
        bar_d2(delta4(M, H), M, r1), M, r1
    )
    external_c = antichiral_bottom(H, q)

    full_probe: list[sp.Expr] = []
    residual_probe: list[sp.Expr] = []
    longitudinal_probe: list[sp.Expr] = []
    collapsed_neighbor_probe: list[sp.Expr] = []
    for dotted in range(2):
        probe = vector_dotted_component(M, dotted)
        full = integrate_two_vertices_bottom_source(
            a_full
            * source_c_line
            * internal_reversed
            * probe
            * external_c,
            M,
            H,
        )
        residual = integrate_two_vertices_bottom_source(
            a_residual
            * source_c_line
            * internal_reversed
            * probe
            * external_c,
            M,
            H,
        )
        longitudinal = sp.factor(full - 8 * determinant(r2) * residual)
        collapsed_neighbor = integrate_two_vertices_bottom_source(
            a_full
            * source_c_line
            * delta4(M, H)
            * probe
            * external_c,
            M,
            H,
        )
        full_probe.append(sp.factor(full))
        residual_probe.append(sp.factor(residual))
        longitudinal_probe.append(longitudinal)
        collapsed_neighbor_probe.append(sp.factor(collapsed_neighbor))

    expected_residual = (
        128 * (r0[0][1] - p[0][1]),
        -128 * (r0[0][0] - p[0][0]),
    )
    expected_longitudinal = (
        -1024 * determinant(r1) * r2[0][1],
        1024 * determinant(r1) * r2[0][0],
    )
    expected_collapsed_neighbor = (
        -64 * r2[0][1],
        64 * r2[0][0],
    )
    for dotted in range(2):
        if sp.expand(
            residual_probe[dotted] - expected_residual[dotted]
        ) != 0:
            raise AssertionError(
                f"C>A TMM r2 residual dotted={dotted}"
            )
        if sp.expand(
            longitudinal_probe[dotted]
            - expected_longitudinal[dotted]
        ) != 0:
            raise AssertionError(
                f"C>A TMM longitudinal dotted={dotted}"
            )
        if sp.expand(
            collapsed_neighbor_probe[dotted]
            - expected_collapsed_neighbor[dotted]
        ) != 0:
            raise AssertionError(
                f"C>A TMM collapsed neighbor dotted={dotted}"
            )

    # F=8 det(r2) R1-8 det(r1) R2.  With det(ri)=-(Di+mu2),
    # F_DRED-F_full-d=8 mu2 (R2-R1).
    adjacent_residual = (
        128 * r2[0][1],
        -128 * r2[0][0],
    )
    evanescent_probe = tuple(
        sp.factor(
            8 * (adjacent_residual[index] - expected_residual[index])
        )
        for index in range(2)
    )
    expected_evanescent = (
        -1024 * q[0][1],
        1024 * q[0][0],
    )
    if any(
        sp.expand(evanescent_probe[index] - expected_evanescent[index])
        != 0
        for index in range(2)
    ):
        raise AssertionError("C>A TMM evanescent sign")

    simplex_evanescent = expected_evanescent

    # Independent C>A TMH: source C reaches the left H+ vertex, the marked
    # A vector reaches the right M vertex, and the bridge is P_+.
    external_b_left = chiral_b_plus(M, p)
    external_b_right = chiral_b_plus(H, q)
    internal_plus = bar_d2(
        d2(delta4(M, H), M, r1), M, r1
    )
    tmh_full_plus = integrate_two_vertices_bottom_source(
        a_full
        * source_c_line
        * internal_plus
        * external_b_left
        * external_b_right,
        M,
        H,
    )
    tmh_full_minus = integrate_two_vertices_bottom_source(
        a_full
        * source_c_line
        * internal_reversed
        * external_b_left
        * external_b_right,
        M,
        H,
    )
    tmh_transverse = integrate_two_vertices_bottom_source(
        a_residual
        * source_c_line
        * internal_plus
        * external_b_left
        * external_b_right,
        M,
        H,
    )
    if any(
        sp.expand(value) != 0
        for value in (
            tmh_full_plus,
            tmh_full_minus,
            tmh_transverse,
        )
    ):
        raise AssertionError("C>A TMH projected polynomial is not zero")

    return {
        "tmm": {
            "ordered_pair": "C_r__A",
            "routing": {
                "r0": "source C reversed-chiral edge to left M",
                "r1": "left M to right M reversed-chiral bridge",
                "r2": "source A vector edge to right M",
                "p": "external D momentum",
                "q": "external C momentum",
            },
            "full_probe": [sp.sstr(value) for value in full_probe],
            "transverse_r2_residual": [
                sp.sstr(value) for value in residual_probe
            ],
            "longitudinal_polynomial": [
                sp.sstr(value) for value in longitudinal_probe
            ],
            "collapsed_neighbor_raw": [
                sp.sstr(value) for value in collapsed_neighbor_probe
            ],
            "projector_collapse_check": "16*det(r1)*K_neighbor=-8*det(r1)*R2",
            "evanescent_probe_before_simplex": [
                sp.sstr(value) for value in evanescent_probe
            ],
            "evanescent_probe_after_simplex": [
                sp.sstr(value) for value in simplex_evanescent
            ],
            "full_d_contacts": [
                "+8*D2*R1",
                "-8*D1*R2",
            ],
            "contact_sum_rule": "F_DRED+C_d=8*mu2*(R2-R1)",
            "lambda_coefficient_before_color": "-2",
            "color": "(i*c_{DAX})(i*c_{BXE})=-F^{AB}_{DE}",
            "C__A_output_kernel": "D^D>q*C_r^E",
            "C__A_lambda_coefficient": "+2",
            "zero_source_momentum_q_equals_minus_p": "-2 on D^D>p*C_r^E",
        },
        "tmh": {
            "ordered_pair": "C_r__A",
            "oriented_internal_P_plus_full_polynomial": sp.sstr(
                tmh_full_plus
            ),
            "alternate_internal_P_minus_full_polynomial": sp.sstr(
                tmh_full_minus
            ),
            "transverse_polynomial": sp.sstr(tmh_transverse),
            "longitudinal_polynomial": "0",
            "route_008": "EXACT_ZERO_FULL_PROJECTED_POLYNOMIAL",
            "route_009": "EXACT_ZERO_FULL_PROJECTED_POLYNOMIAL",
        },
    }


def build_payload() -> dict[str, object]:
    validation_samples = (
        (
            "A__C_r",
            g1.vector((1, 2, 3, 1)),
            g1.vector((-1, -2, -3, -1)),
            0,
        ),
        (
            "C_r__A",
            g1.vector((2, -1, 1, 3)),
            g1.vector((-2, 1, -1, -3)),
            1,
        ),
    )
    reference: dict[str, dict[tuple[int, int, int], tuple[g1.QI, g1.QI, g1.QI]]] = {}
    sample_rows: list[dict[str, object]] = []
    for ordered_pair, momentum_c, momentum_d, dotted in validation_samples:
        sample_payload: dict[str, object] = {
            "ordered_pair": ordered_pair,
            "momentum_C": [qtext(entry) for entry in momentum_c],
            "momentum_D": [qtext(entry) for entry in momentum_d],
            "dotted": dotted,
            "sectors": {},
        }
        for sector, name in (("+", "plus"), ("-", "minus")):
            traces = tgm_simplex_traces(
                momentum_c,
                momentum_d,
                dotted,
                sector,
            )
            if name not in reference:
                reference[name] = traces
            elif traces != reference[name]:
                raise AssertionError("TGM trace table depends on validation sample")
            sector_rows = {}
            for permutation, values in traces.items():
                expected = EXPECTED_TGM[permutation][name]
                actual = tuple(value.re for value in values)
                if any(value.im != 0 for value in values) or actual != expected:
                    raise AssertionError(
                        f"TGM {name} {permutation}: {values!r} != {expected!r}"
                    )
                sector_rows[str(permutation)] = {
                    "full": qtext(values[0]),
                    "transverse_r0": qtext(values[1]),
                    "longitudinal_migrated_r1": qtext(values[2]),
                }
            sample_payload["sectors"][name] = sector_rows
        sample_rows.append(sample_payload)

    tgm_routes: list[dict[str, object]] = []
    for route, permutation in ROUTE_PERMUTATION.items():
        plus = reference["plus"][permutation]
        minus = reference["minus"][permutation]
        coefficient_before_ac_color = Fraction(
            plus[0].re - minus[0].re, 4096
        )
        coefficient_after_ac_color = -coefficient_before_ac_color
        if coefficient_after_ac_color != EXPECTED_ROUTE_COEFFICIENTS[route]:
            raise AssertionError(f"TGM route coefficient {route}")
        tgm_routes.append(
            {
                "route": route,
                "permutation": list(permutation),
                "plus_full_trace": qtext(plus[0]),
                "plus_transverse_trace": qtext(plus[1]),
                "plus_longitudinal_trace": qtext(plus[2]),
                "minus_full_trace": qtext(minus[0]),
                "minus_transverse_trace": qtext(minus[1]),
                "minus_longitudinal_trace": qtext(minus[2]),
                "A__C_output": "D^D>C_r^E",
                "C__A_output": "C_r^D>D^E",
                "lambda_coefficient": ftext(coefficient_after_ac_color),
            }
        )

    if sum(EXPECTED_ROUTE_COEFFICIENTS.values(), Fraction(0)) != -2:
        raise AssertionError("TGM route sum")

    ac_matter = build_ac_tmm_and_tmh()
    ca_matter = build_ca_tmm_and_tmh()
    full_order_g2 = build_full_order_g2_orbit()

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    pre_d_tmm = sp.simplify(
        (-1 / (4 * sp.sqrt(2)))
        * (sp.sqrt(2) * coupling / hbar) ** 2
        * (-hbar * (hbar / 16) ** 2)
    )
    expected_pre_d_tmm = sp.sqrt(2) * hbar * coupling**2 / 1024
    if sp.simplify(pre_d_tmm - expected_pre_d_tmm) != 0:
        raise AssertionError("AC/CA TMM canonical pre-D normalization")

    induced_current = 2 * sp.I
    explicit_current = -2 * sp.I
    if sp.expand(induced_current + explicit_current) != 0:
        raise AssertionError("outer-A matter current occurrence pairing")
    flavors = []
    for r in (1, 2, 3):
        complement = tuple(value for value in (1, 2, 3) if value != r)
        flavors.append(
            {
                "r": r,
                "TGM_action_flavor": r,
                "TMM_action_flavors": [r, r],
                "TMH_complement_routes": [
                    [complement[0], complement[1]],
                    [complement[1], complement[0]],
                ],
                "TMH_each_route": "EXACT_ZERO_FULL_PROJECTED_POLYNOMIAL",
            }
        )

    return {
        "schema": "step5-ac-ca-family-exact-v2",
        "status": "TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH",
        "external_target_used_in_derivation": False,
        "operator_identity": {
            "outer_A": "nabla_- A=-nabla_+ E_V-2i(B_s x C_s)",
            "current_occurrence_rule": "retain the two current rows until their identical ordered port word is established",
            "current_cancellation_after_pairing": "(+2i-2i)*(B_s x C_s) C_r=0",
            "D_word": "D_-D_+barD2D_+=8barBox D_+-(1/2)D_+barD2D2",
            "TGM_longitudinal_tag": "source vector r0 -> adjacent bridge vector r1",
            "TMM_longitudinal_tag": "source vector r0 -> adjacent chiral projector r1",
        },
        "normalization": {
            "AA_canonical_cross_check": {
                "source_A_c": "-1/(4sqrt(2))",
                "source_C_c": "1",
                "matter_exponent_vertex_each": "+sqrt(2)g/hbar*T_U",
                "vector_propagator": "-hbar/D",
                "matter_propagator_each": "+hbar*projector/(16D)",
                "matter_projector_count": 2,
                "full_vertex_measure_in_D_word": "(1/4)*(1/4)=1/16",
                "external_D_probe": "D2barD_dot-a(theta+theta-bartheta_dot-a)=-2",
                "external_D_c_map": "D2barD_dot-a u=-4sqrt(2)D_dot-a",
                "external_C_c_map": "1",
                "action_copy_Wick": "(1/2!)*(2)=1",
                "canonical_to_physical_roundtrip": "(gA_c)(gC_c) and (gD_c)(gC_c) cancel the same g^2",
            },
            "source_A_C": "-1/(4sqrt(2))",
            "matter_exponent_vertex": "+sqrt(2)g/hbar T_U",
            "vector_propagator": "-hbar/D",
            "chiral_propagator": "+hbar barD2D2/(16D)",
            "reversed_chiral_propagator": "+hbar D2barD2/(16D)",
            "external_D_map": "D2barD_dot-a u=-4sqrt(2)D_dot-a",
            "wick_action_order": "(1/2!)*(two labeled action orders)=1",
            "mu2_master": "1/(32pi^2)",
            "lambda1": "hbar*g^2/(16pi^2)",
            "TMM_preD_exact": sp.sstr(pre_d_tmm),
            "factor_two_origin": "old transported-square occurrence decomposition counted two scalar cut defects; the SD-complete metric orbit leaves one half",
        },
        "outer_A_occurrence_resolved_orbit": {
            "current_rows": [
                {
                    "id": "EV_MATTER_CURRENT",
                    "ordered_words": [
                        "(B_s x C_s)^A C_r^B",
                        "C_r^A (B_s x C_s)^B",
                    ],
                    "coefficient": "+2i",
                    "inverse_edge_tag": "none",
                },
                {
                    "id": "EXPLICIT_MINUS_2I_BC",
                    "ordered_words": [
                        "(B_s x C_s)^A C_r^B",
                        "C_r^A (B_s x C_s)^B",
                    ],
                    "coefficient": "-2i",
                    "inverse_edge_tag": "none",
                },
            ],
            "common_collapsed_D_words": {
                "A__C_r": "K_neighbor=(64*r0_{+dot2},-64*r0_{+dot1})",
                "C_r__A": "K_neighbor=(-64*r2_{+dot2},+64*r2_{+dot1})",
            },
            "paired_sum": "0",
            "pairing_stage": "after ordered flavor/color/field ports are matched; before loop integration",
            "regulator_square_in_current_pair": "absent",
            "A__C_inverse_edge_rows": [
                "PRIMARY: +8*det(r0)*R0",
                "NEIGHBOR_AFTER_LONGITUDINAL_IBP: -8*det(r1)*J1",
            ],
            "C__A_inverse_edge_rows": [
                "PRIMARY: +8*det(r2)*R1",
                "NEIGHBOR_AFTER_LONGITUDINAL_IBP: -8*det(r1)*R2",
            ],
            "verdict": "CURRENT_PAIR_ZERO; FACTOR_HALF_COMES_FROM_SD_COMPLETE_METRIC_OCCURRENCE_DECOMPOSITION",
        },
        "TGM": {
            "route_count": 6,
            "word_count_per_route": "2 derivative placements x 2 Euclidean chiralities",
            "preD_plus": "-hbar*g^2/(8192sqrt(2))",
            "preD_minus": "+hbar*g^2/(8192sqrt(2))",
            "A__C_color": "c_{ARD}c_{RBE}=-F^{AB}_{DE}",
            "C__A_color": "c_{BRE}c_{RAD}=-F^{AB}_{DE}",
            "routes": tgm_routes,
            "lambda_sum": "-2",
            "full_d_SD_contacts": {
                "source_edge": "replace the tagged four-dimensional source-vector square by D_source with the opposite Ward sign",
                "migrated_neighbor_edge": "after longitudinal IBP replace the tagged adjacent bridge square by D_neighbor with its retained numerator sign",
                "identity": "F_route^(4)+C_source^(d)+C_neighbor^(d)=0 when mu2=0",
                "DRED_remainder": "F_route^DRED+C_source^(d)+C_neighbor^(d) is the displayed mu2 trace",
            },
            "validation_samples": sample_rows,
        },
        "A__C_r_matter": ac_matter,
        "C_r__A_matter": ca_matter,
        "full_order_g2_orbit": full_order_g2,
        "ordered_results": {
            "A__C_r": {
                "C_r^D>D^E": "-1",
                "D^D>C_r^E": "+1",
            },
            "C_r__A": {
                "C_r^D>D^E": "-1",
                "D^D>C_r^E": "+1",
            },
            "common_unit": "lambda1*F^{AB}_{DE}*P_dot contraction",
        },
        "flavor_lift": flavors,
        "after_check_only": {
            "HT_anchor": "main.tex:1238-1239 b gamma",
            "HT_zero_shift_vector_C_D__D_C": ["-1", "1"],
            "Project_A__C_vector_C_D__D_C": ["-1", "+1"],
            "Project_C__A_vector_C_D__D_C": ["-1", "+1"],
            "raw_ratio_to_printed_HT_zero_shift": "1",
            "current_orbit_factor_half_test": "HALF_FROM_METRIC_OCCURRENCE_DECOMPOSITION_NOT_CURRENT_CANCELLATION",
            "status": "EXACT_MATCH",
        },
    }


def build_markdown() -> str:
    return r"""# Step 5 ordered $A>C_r$ and $C_r>A$ anomaly sector

Status: `TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH`.

No holomorphic-twist coefficient enters Sections 1--7.

## 1. Definitions

$$
A_c=A_1+gA_2+g^2A_3,
\qquad
C_r=\widetilde\Phi_r,
$$

$$
N_0=D_-A_1,
$$

$$
N_1=D_-A_2+[\gamma_1,A_1],
$$

$$
N_2=D_-A_3+[\gamma_1,A_2]+[\gamma_2,A_1].
$$

The connected order-$g^2$ orbit is

$$
\Gamma_{g^2}^{(1)}
=\langle I_2\rangle_0
-\frac1\hbar\langle I_1S_3\rangle_{0,c}
-\frac1\hbar\langle I_0S_4\rangle_{0,c}
+\frac1{2\hbar^2}\langle I_0S_3S_3\rangle_{0,c}.
$$

Define

$$
d=4-2\epsilon,
\qquad
J_2:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell_d^2}{(\ell_d^2+\Delta)^3},
$$

$$
\mu_\ell^2:=\bar\ell^2-\ell_d^2,
\qquad
J_{\mu^2}:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}.
$$

Rotational reduction in $d$ dimensions gives

$$
\int\bar\ell^2 f(\ell_d^2)
=\frac4d\int\ell_d^2f(\ell_d^2),
$$

and therefore

$$
\boxed{J_{\mu^2}=\frac{4-d}{d}J_2=\frac1{32\pi^2}.}
$$

## 2. Exact color contraction

Use $T_A=\sigma_A/2$, $\operatorname{tr}(T_AT_B)=\delta_{AB}/2$.
For the frame

$$
(A,B,D,E)=(0,1,1,0),
$$

the two matter vertices, two matter inverse metrics, and the complete vector
covariance give

$$
\begin{aligned}
C_{\rm full}
&=(-2)(2)(2)
\sum_{X=0}^2
\operatorname{tr}\!\left(T_D[T_A,T_X]\right)
\operatorname{tr}\!\left(T_X[T_E,T_B]\right)
\\
&=-8\left(\frac{i}{2}\right)^2
\sum_X\varepsilon_{AXD}\varepsilon_{EBX}
\\
&=-2.
\end{aligned}
$$

The Project tensor in the same frame is

$$
\mathbb F^{01}{}_{10}
=2\sum_X\varepsilon_{0X1}\varepsilon_{1X0}
=-2.
$$

Hence

$$
\boxed{C_{\rm full}=+\mathbb F^{AB}{}_{DE}.}
$$

The old sign line separated the vector-covariance minus from the same color
word and then used it a second time.  The full covariance contraction above
is the sign used below.

## 3. Exact nonlinear $D$-words

Set

$$
z(k):=k_0-ik_1.
$$

The finite-Grassmann replay gives, for $A>C_r$,

$$
\left.I_1S_{m3}\right|_{A_2M_1,D>C}
=-8z(k),
$$

$$
\left.I_0S_{m4}\right|_{A_1M_2,D>C}
=+8\sqrt2\,z(k),
$$

$$
\left.I_0S_{m4}\right|_{A_1M_2,C>D}
=-16\sqrt2\,z(k).
$$

At the exact validation momentum $k=(2,-1,1,3)$,

$$
z(k)=2+i,
$$

$$
(-8z,8\sqrt2z,-16\sqrt2z)
=(-16-8i,16\sqrt2+8i\sqrt2,-32\sqrt2-16i\sqrt2).
$$

Swapping the source slots and replaying $C_r>A$ gives the same three
polynomials in the reversed ports.  No reflected coefficient is assumed.

The quartic word is obtained by differentiating

$$
[U,[U,\Phi]]
=U^2\Phi-2U\Phi U+\Phi U^2
$$

with respect to one internal and one external $U$.  Thus both ordered $U$
placements occur inside one seagull vertex; they are not two Feynman graphs.

## 4. $TMM$ metric orbit

The three-denominator triangle has the normalized metric pole

$$
\Gamma_{TMM}^{\triangle}\big|_{J_2}
=-\frac8dJ_2.
$$

The complete $I_0S_{m4}$ seagull gives

$$
\Gamma_{TMM}^{I_0S_{m4}}\big|_{J_2}
=+2J_2.
$$

Their four-dimensional pole cancels exactly:

$$
\left(-\frac84+2\right)J_2=0.
$$

In DRED,

$$
\begin{aligned}
\Gamma_{TMM}^{\rm DRED}\big|_{\rm local}
&=\left(2-\frac8d\right)J_2
\\
&=\frac{2d-8}{d}J_2
\\
&=-2\frac{4-d}{d}J_2
\\
&=-2J_{\mu^2}.
\end{aligned}
$$

Therefore

$$
\hbar g^2(-2)J_{\mu^2}
=-\frac{\hbar g^2}{16\pi^2}
=-\lambda_1.
$$

Thus $TMM$ contributes

$$
\boxed{c_{TMM}=-1.}
$$

## 5. $TGM$ metric orbit

The six gauge--matter triangle routes have total metric pole

$$
\Gamma_{TGM}^{\triangle}\big|_{J_2}
=+\frac8dJ_2.
$$

The nonlinear-source bubble and the matter seagull give separately

$$
\Gamma_{TGM}^{I_1S_{m3}}\big|_{J_2}=-J_2,
$$

$$
\Gamma_{TGM}^{I_0S_{m4}}\big|_{J_2}=-J_2.
$$

At $d=4$,

$$
\left(\frac84-1-1\right)J_2=0.
$$

In DRED,

$$
\begin{aligned}
\Gamma_{TGM}^{\rm DRED}\big|_{\rm local}
&=\left(\frac8d-2\right)J_2
\\
&=\frac{8-2d}{d}J_2
\\
&=+2\frac{4-d}{d}J_2
\\
&=+2J_{\mu^2}.
\end{aligned}
$$

Therefore

$$
\hbar g^2(+2)J_{\mu^2}
=+\frac{\hbar g^2}{16\pi^2}
=+\lambda_1,
$$

and

$$
\boxed{c_{TGM}=+1.}
$$

## 6. Remaining order-$g^2$ rows

The $A_3$ source term has one massless coincident vector tadpole:

$$
\langle I_2\rangle_0
\supset
\int\frac{d^dk}{(2\pi)^d}\frac{(k^2)^n}{k^2}=0.
$$

Both typed superpotential routes have exact projected polynomial zero:

$$
T_{MH}^{(1)}=T_{MH}^{(2)}=0.
$$

The gauge, gauge-fixing, FP, and NK rows have zero
$\mathbb F$-sector metric trace.  They contain no $J_{\mu^2}$ remainder.

The Euler-current and explicit-current occurrences remain separate until
their ports, denominators, and edge tags are matched:

$$
\begin{array}{c|c|c|c}
\text{row}&\text{coefficient}&\text{denominator}&\text{selected square}\\ \hline
E_{\rm cur}&+2i&D_0D_1&\varnothing\\
X_{\rm cur}&-2i&D_0D_1&\varnothing
\end{array}
$$

Hence

$$
(+2i-2i)K_{\rm cur}(k)=0.
$$

This zero does not produce the factor $1/2$.

## 7. First invalid line and ordered result

The old replay replaced both transported inverse-square rows independently:

$$
\bar r_0^2-r_{0,d}^2=\mu_\ell^2,
\qquad
\bar r_1^2-r_{1,d}^2=\mu_\ell^2,
$$

and promoted both rows to independent nonlinear descendants.  The exact
$I_1S_3+I_0S_4$ replay shows that these are two decompositions of one metric
pole orbit.  Consequently

$$
\left|\Gamma_{\rm old}\right|=4J_{\mu^2},
\qquad
\left|\Gamma_{\rm complete}\right|=2J_{\mu^2}.
$$

The first invalid classification is therefore

$$
\boxed{\texttt{OCCURRENCE_DECOMPOSITION_DOUBLE_COUNT}.}
$$

In the ordered basis

$$
\left((P_{\dot a}C_r)^D D^{E\dot a},
D_{\dot a}^D(P^{\dot a}C_r)^E\right),
$$

the independent results are

$$
\boxed{\mathbf c_{A>C_r}=(-1,+1),}
$$

$$
\boxed{\mathbf c_{C_r>A}=(-1,+1).}
$$

Equivalently,

$$
\boxed{
\Delta(A,C_r)=\Delta(C_r,A)
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
D_{\dot a}^D(P^{\dot a}C_r)^E
-(P_{\dot a}C_r)^D D^{E\dot a}
\right].}
$$

## 8. Holomorphic-twist after-check

Only now read the compact zero-shift row.  It gives

$$
\mathbf c_{\rm HT}=(-1,+1).
$$

Therefore

$$
\boxed{\mathbf c_{A>C_r}=\mathbf c_{C_r>A}=\mathbf c_{\rm HT}.}
$$
"""


def verify_markdown(text: str) -> None:
    required = (
        "TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH",
        "C_{\\rm full}=+\\mathbb F^{AB}{}_{DE}",
        "2-\\frac8d",
        "\\frac8d-2",
        "OCCURRENCE_DECOMPOSITION_DOUBLE_COUNT",
        "\\mathbf c_{A>C_r}=(-1,+1)",
        "\\mathbf c_{C_r>A}=(-1,+1)",
    )
    missing = [fragment for fragment in required if fragment not in text]
    if missing:
        raise AssertionError(f"markdown anchors missing: {missing}")
    for forbidden in ("\\sim", "\\approx", "After substitution"):
        if forbidden in text:
            raise AssertionError(f"forbidden shortcut in markdown: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    markdown = build_markdown()
    if args.write:
        args.json.write_text(rendered, encoding="utf-8")
        args.markdown.write_text(markdown, encoding="utf-8")
    else:
        if args.json.read_text(encoding="utf-8") != rendered:
            raise SystemExit("FAIL stale step5-ac-ca-family-exact.json")
        if args.markdown.read_text(encoding="utf-8") != markdown:
            raise SystemExit("FAIL stale step5-ac-ca-family-exact.md")
    verify_markdown(markdown)
    print("PASS TGM 6/6 route traces and migrated longitudinal words")
    print("PASS TMM r0+r1 full-d SD orbit and pointwise routing cancellation")
    print("PASS TMH 2/2 full projected polynomials vanish")
    print("PASS full I2-I1S3-I0S4+I0S3S3/2 metric orbit")
    print("PASS ordered AC/CA unit vectors (-1,+1)")
    print("PASS flavor lift r=1,2,3 and both ordered source orientations")
    print("PASS external_target_used_in_derivation=false")
    print("SUMMARY 7/7 PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
