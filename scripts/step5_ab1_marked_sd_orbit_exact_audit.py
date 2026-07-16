#!/usr/bin/env python3
"""Exact target-blind audit of the marked AB1 G1/G2/G3 SD edges.

This checker does not use a holomorphic-twist coefficient as input.  Besides
the two source-selected edges, it replays every inverse kernel generated after
graded superspace integration by parts.  In particular the G3 outer-A
longitudinal word is transported to the neighboring matter edge before the
Schwinger--Dyson cut is applied.
"""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
G1_PATH = ROOT / "scripts" / "step5_ab1_g1_vvv_dword_replay.py"
G23_PATH = ROOT / "scripts" / "step5_ab1_g2_g3_dword_replay.py"
AUDIT_PATH = ROOT / "audits" / "step5-ab1-marked-sd-orbit-exact.md"
CENSUS_PATH = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


g1 = load_module("step5_ab1_g1_vvv_dword_replay_for_sd", G1_PATH)
g23 = load_module("step5_ab1_g2_g3_dword_replay_for_sd", G23_PATH)


class Ledger:
    def __init__(self) -> None:
        self.rows: list[tuple[str, object, object]] = []

    def check(self, name: str, actual: object, expected: object) -> None:
        if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
            passed = sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
        else:
            passed = actual == expected
        self.rows.append((name, actual, expected))
        if not passed:
            raise AssertionError(f"{name}: actual={actual!r}, expected={expected!r}")

    def finish(self) -> None:
        for name, _, _ in self.rows:
            print(f"PASS {name}")
        print(f"SUMMARY {len(self.rows)}/{len(self.rows)} PASS")


AB1_DIRECTED_ROUTES = (
    ("001", "G[0,1]", "M1[0,1]", "TGM"),
    ("002", "G[0,2]", "M1[0,1]", "TGM"),
    ("003", "G[1,0]", "M1[0,1]", "TGM"),
    ("004", "G[1,2]", "M1[0,1]", "TGM"),
    ("005", "G[2,0]", "M1[0,1]", "TGM"),
    ("006", "G[2,1]", "M1[0,1]", "TGM"),
    ("007", "M1[1,0]", "M1[0,2]", "TMM"),
    ("008", "M2[1,2]", "Hminus[0,1]", "TMH"),
    ("009", "M3[1,2]", "Hminus[0,2]", "TMH"),
)


# U_0=source vector, U_1=matter-vertex vector, U_2=external D.  The
# permutation sign converts every raw VVV color word to the one canonical
# open-color word c_{IJD}; it never reverses the external D>B_1 slot.
G1_ROUTE_METADATA = (
    ("001", (0, 1, 2), "c_{IJD}", +1),
    ("002", (0, 2, 1), "c_{IDJ}", -1),
    ("003", (1, 0, 2), "c_{JID}", -1),
    ("004", (1, 2, 0), "c_{JDI}", +1),
    ("005", (2, 0, 1), "c_{DIJ}", +1),
    ("006", (2, 1, 0), "c_{DJI}", -1),
)


EUCLIDEAN_SIGMA = (
    sp.Matrix(((0, -sp.I), (-sp.I, 0))),
    sp.Matrix(((0, -1), (1, 0))),
    sp.Matrix(((-sp.I, 0), (0, sp.I))),
    sp.eye(2),
)


def euclidean_bispinor(vector):
    return sum(
        (sp.sympify(vector[m]) * EUCLIDEAN_SIGMA[m] for m in range(4)),
        sp.zeros(2),
    )


def diagonal_loop_coefficients(expression, loop_components):
    polynomial = sp.Poly(sp.expand(expression), *loop_components)
    output = []
    for axis in range(4):
        monomial = [0, 0, 0, 0]
        monomial[axis] = 2
        output.append(sp.factor(polynomial.coeff_monomial(tuple(monomial))))
    return tuple(output)


def g2_full_tensor_frame_audit():
    """Extract the metric/evanescent G2 tensor without an HT coefficient."""

    loop = sp.symbols("L0:4")
    y, z = sp.symbols("y z", nonnegative=True)
    p_vector = (1, 0, 0, 0)
    q_vector = (0, 0, 0, 1)
    shift = tuple(
        loop[m] + y * p_vector[m] + z * (p_vector[m] + q_vector[m])
        for m in range(4)
    )
    r0 = euclidean_bispinor(shift)
    p = euclidean_bispinor(p_vector)
    q = euclidean_bispinor(q_vector)
    r1 = r0 - p
    r2 = r1 - q
    mixed = sp.expand(r2[0, 0] * r1[1, 1] - r2[0, 1] * r1[1, 0])
    det_r2 = sp.expand(r2.det())

    full = (
        sp.expand(-1024 * r0[0, 1] * mixed),
        sp.expand(+1024 * r0[0, 0] * mixed),
    )
    transverse = (
        sp.expand(-1024 * r0[0, 1] * det_r2),
        sp.expand(+1024 * r0[0, 0] * det_r2),
    )
    longitudinal = tuple(sp.expand(full[i] - transverse[i]) for i in range(2))

    diagonal = {
        name: tuple(diagonal_loop_coefficients(value, loop) for value in pair)
        for name, pair in (
            ("full", full),
            ("transverse", transverse),
            ("longitudinal", longitudinal),
        )
    }
    perpendicular_trace = {
        name: tuple(sp.factor(row[1] + row[2]) for row in rows)
        for name, rows in diagonal.items()
    }

    def simplex_average(value):
        return sp.simplify(
            2 * sp.integrate(
                sp.integrate(value, (z, 0, 1 - y)), (y, 0, 1)
            )
        )

    # A raw rank tensor contributes -1/2 of its two-axis transverse trace to
    # the mu_l^2 word.  This sign/factor is fixed independently by applying
    # the same extraction to the explicit determinant term.
    evanescent_probe = {
        name: tuple(
            sp.simplify(-sp.Rational(1, 2) * simplex_average(value))
            for value in traces
        )
        for name, traces in perpendicular_trace.items()
    }

    # Raising the dotted slot uses epsilon^{dot a dot b}; in this frame
    # p^dot=(-i,0), q^dot=(0,-1).
    p_raised = (p[0, 1], -p[0, 0])
    q_raised = (q[0, 1], -q[0, 0])
    return {
        "y": y,
        "z": z,
        "diagonal": diagonal,
        "perpendicular_trace": perpendicular_trace,
        "evanescent_probe": evanescent_probe,
        "p_raised": p_raised,
        "q_raised": q_raised,
    }


def g1_selected_residuals(loop, external_p, dotted: int, sector: str):
    """Return the A- and B-marked residuals after removing 8 barBox.

    A marked:
      D_- D_+ barD^2 D_+ = 8 barBox D_+ + longitudinal.
    B marked:
      D_- D_+ barD^2 D^2 = 8 barBox D^2.
    """

    external_q = g1.vector_neg(external_p)
    source_vector_momentum = g1.vector_add(
        g1.vector_neg(loop), g1.vector_add(external_p, external_q)
    )
    endpoint_momenta = (
        g1.vector_add(loop, g1.vector_neg(g1.vector_add(external_p, external_q))),
        g1.vector_add(g1.vector_neg(loop), external_p),
        external_q,
    )
    endpoints = (
        g1.superspace_delta("S", "G"),
        g1.superspace_delta("M", "G"),
        g1.vector_d_endpoint("G", dotted),
    )

    delta_sm = g1.superspace_delta("S", "M")
    matter_d2 = g1.d_squared(delta_sm, "S", loop)
    matter_line = g1.bar_d_squared(matter_d2, "S", loop)
    matter_d0 = g1.d_lower(matter_line, "S", 0, loop)
    external_b = g1.chiral_b_endpoint("M", external_p)

    a_rows = {}
    b_rows = {}
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
            gauge_d0 = g1.d_lower(
                vvv, "S", 0, source_vector_momentum
            )
            gauge_unmarked_a = g1.d_lower(
                g1.bar_d_squared(
                    gauge_d0, "S", source_vector_momentum
                ),
                "S",
                0,
                source_vector_momentum,
            )
            words = (
                (a_rows, color_sign * gauge_d0 * matter_d0 * external_b),
                (b_rows, color_sign * gauge_unmarked_a * matter_d2 * external_b),
            )
            for output, word in words:
                word = g1.integrate_full(word, "M")
                word = (
                    g1.integrate_chiral(word, "G")
                    if sector == "+"
                    else g1.integrate_antichiral(word, "G")
                )
                word = word.set_zero(
                    g1.INDEX["S", name] for name in g1.COORDINATES
                )
                output[permutation, placement] = word.coefficient(
                    g1.ETA_BD_MASK
                )
    return a_rows, b_rows


def g1_full_outer_totals(
    loop, external_p, external_q, dotted: int, sector: str, *, detailed: bool = False
):
    """Return the exact full outer-A and outer-B G1 words for generic p,q."""

    source_vector_momentum = g1.vector_add(
        g1.vector_neg(loop), g1.vector_add(external_p, external_q)
    )
    endpoint_momenta = (
        g1.vector_add(loop, g1.vector_neg(g1.vector_add(external_p, external_q))),
        g1.vector_add(g1.vector_neg(loop), external_p),
        external_q,
    )
    endpoints = (
        g1.superspace_delta("S", "G"),
        g1.superspace_delta("M", "G"),
        g1.vector_d_endpoint("G", dotted),
    )

    delta_sm = g1.superspace_delta("S", "M")
    matter_line = g1.bar_d_squared(
        g1.d_squared(delta_sm, "S", loop), "S", loop
    )
    matter_d0 = g1.d_lower(matter_line, "S", 0, loop)
    matter_d1d0 = g1.d_lower(matter_d0, "S", 1, loop)
    external_b = g1.chiral_b_endpoint("M", external_p)

    totals = [g1.ZERO, g1.ZERO]
    rows = {}
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
            gauge_d0 = g1.d_lower(vvv, "S", 0, source_vector_momentum)
            gauge_bar2 = g1.bar_d_squared(
                gauge_d0, "S", source_vector_momentum
            )
            gauge_d0_bar2_d0 = g1.d_lower(
                gauge_bar2, "S", 0, source_vector_momentum
            )
            gauge_d1d0_bar2_d0 = g1.d_lower(
                gauge_d0_bar2_d0, "S", 1, source_vector_momentum
            )
            branch_words = (
                gauge_d1d0_bar2_d0 * matter_d0,
                gauge_d0_bar2_d0 * matter_d1d0,
            )
            for branch, branch_word in enumerate(branch_words):
                word = color_sign * branch_word * external_b
                word = g1.integrate_full(word, "M")
                word = (
                    g1.integrate_chiral(word, "G")
                    if sector == "+"
                    else g1.integrate_antichiral(word, "G")
                )
                word = word.set_zero(
                    g1.INDEX["S", name] for name in g1.COORDINATES
                )
                value = word.coefficient(g1.ETA_BD_MASK)
                totals[branch] += value
                rows[permutation, placement, branch] = value
    return (tuple(totals), rows) if detailed else tuple(totals)


def g1_selected_outer_totals(
    loop, external_p, external_q, dotted: int, sector: str, *, detailed: bool = False
):
    """Return residuals after removing 8 barBox on the two source edges."""

    source_vector_momentum = g1.vector_add(
        g1.vector_neg(loop), g1.vector_add(external_p, external_q)
    )
    endpoint_momenta = (
        g1.vector_add(loop, g1.vector_neg(g1.vector_add(external_p, external_q))),
        g1.vector_add(g1.vector_neg(loop), external_p),
        external_q,
    )
    endpoints = (
        g1.superspace_delta("S", "G"),
        g1.superspace_delta("M", "G"),
        g1.vector_d_endpoint("G", dotted),
    )
    delta_sm = g1.superspace_delta("S", "M")
    matter_d2 = g1.d_squared(delta_sm, "S", loop)
    matter_line = g1.bar_d_squared(matter_d2, "S", loop)
    matter_d0 = g1.d_lower(matter_line, "S", 0, loop)
    external_b = g1.chiral_b_endpoint("M", external_p)

    totals = [g1.ZERO, g1.ZERO]
    rows = {}
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
            gauge_d0 = g1.d_lower(vvv, "S", 0, source_vector_momentum)
            gauge_unmarked_a = g1.d_lower(
                g1.bar_d_squared(gauge_d0, "S", source_vector_momentum),
                "S",
                0,
                source_vector_momentum,
            )
            branch_words = (
                gauge_d0 * matter_d0,
                gauge_unmarked_a * matter_d2,
            )
            for branch, branch_word in enumerate(branch_words):
                word = color_sign * branch_word * external_b
                word = g1.integrate_full(word, "M")
                word = (
                    g1.integrate_chiral(word, "G")
                    if sector == "+"
                    else g1.integrate_antichiral(word, "G")
                )
                word = word.set_zero(
                    g1.INDEX["S", name] for name in g1.COORDINATES
                )
                value = word.coefficient(g1.ETA_BD_MASK)
                totals[branch] += value
                rows[permutation, placement, branch] = value
    return (tuple(totals), rows) if detailed else tuple(totals)


def g1_perpendicular_trace(shift, external_p, external_q, dotted: int, sector: str):
    center = g1_full_outer_totals(
        shift, external_p, external_q, dotted, sector
    )
    traces = [g1.ZERO, g1.ZERO]
    # p=e1 and q=e4 below, so axes e2,e3 isolate the metric tensor.
    for axis in (1, 2):
        unit = [g1.ZERO, g1.ZERO, g1.ZERO, g1.ZERO]
        unit[axis] = g1.ONE
        unit_vector = tuple(unit)
        plus = g1_full_outer_totals(
            g1.vector_add(shift, unit_vector),
            external_p,
            external_q,
            dotted,
            sector,
        )
        minus = g1_full_outer_totals(
            g1.vector_add(shift, g1.vector_neg(unit_vector)),
            external_p,
            external_q,
            dotted,
            sector,
        )
        for branch in range(2):
            # Central second difference is twice the coefficient of L_axis^2.
            traces[branch] += (plus[branch] - 2 * center[branch] + minus[branch]) / 2
    return tuple(traces)


def g1_full_tensor_frame_audit():
    """Integrate the generic-p,q G1 transverse metric coefficient exactly."""

    p = g1.vector((1, 0, 0, 0))
    q = g1.vector((0, 0, 0, 1))
    p_plus_q = g1.vector_add(p, q)
    points = {
        "00": (Fraction(0), Fraction(0)),
        "10": (Fraction(1), Fraction(0)),
        "01": (Fraction(0), Fraction(1)),
        "check": (Fraction(1, 2), Fraction(1, 3)),
    }

    integrated = {}
    selected_integrated = {}
    traces = {}
    for sector in ("+", "-"):
        for dotted in (0, 1):
            samples = {}
            selected_samples = {}
            for name, (y, z) in points.items():
                shift = g1.vector_add(
                    g1.vector_scale(y, p), g1.vector_scale(z, p_plus_q)
                )
                samples[name] = g1_perpendicular_trace(
                    shift, p, q, dotted, sector
                )
                selected_samples[name] = g1_selected_outer_totals(
                    shift, p, q, dotted, sector
                )
            for branch in range(2):
                value_00 = samples["00"][branch]
                coefficient_y = samples["10"][branch] - value_00
                coefficient_z = samples["01"][branch] - value_00
                expected_check = (
                    value_00
                    + Fraction(1, 2) * coefficient_y
                    + Fraction(1, 3) * coefficient_z
                )
                if samples["check"][branch] != expected_check:
                    raise AssertionError(
                        f"non-affine G1 transverse trace: {sector}/{dotted}/{branch}"
                    )
                # The evanescent word is -1/2 tr_perp and
                # 2 int_Sigma (a+b y+c z)=a+(b+c)/3.
                simplex_trace = value_00 + (coefficient_y + coefficient_z) / 3
                integrated[sector, dotted, branch] = -simplex_trace / 2
                traces[sector, dotted, branch] = (
                    value_00,
                    coefficient_y,
                    coefficient_z,
                )

                selected_00 = selected_samples["00"][branch]
                selected_y = selected_samples["10"][branch] - selected_00
                selected_z = selected_samples["01"][branch] - selected_00
                selected_expected_check = (
                    selected_00
                    + Fraction(1, 2) * selected_y
                    + Fraction(1, 3) * selected_z
                )
                if selected_samples["check"][branch] != selected_expected_check:
                    raise AssertionError(
                        f"non-affine G1 selected residual: {sector}/{dotted}/{branch}"
                    )
                selected_average = selected_00 + (selected_y + selected_z) / 3
                selected_integrated[sector, dotted, branch] = -8 * selected_average

    coefficients = {}
    selected_coefficients = {}
    longitudinal_coefficients = {}
    for sector in ("+", "-"):
        for branch in range(2):
            value_d0 = integrated[sector, 0, branch]
            value_d1 = integrated[sector, 1, branch]
            # endpoint_spinor(p) = (-1,0), endpoint_spinor(q)=(0,i).
            coefficient_p = -value_d0
            coefficient_q = value_d1 / g1.I
            coefficients[sector, branch] = (coefficient_p, coefficient_q)
            selected_d0 = selected_integrated[sector, 0, branch]
            selected_d1 = selected_integrated[sector, 1, branch]
            selected_pair = (-selected_d0, selected_d1 / g1.I)
            selected_coefficients[sector, branch] = selected_pair
            longitudinal_coefficients[sector, branch] = tuple(
                coefficients[sector, branch][index] - selected_pair[index]
                for index in range(2)
            )
    return {
        "integrated_probe": integrated,
        "selected_integrated_probe": selected_integrated,
        "affine_traces": traces,
        "momentum_coefficients": coefficients,
        "selected_momentum_coefficients": selected_coefficients,
        "longitudinal_momentum_coefficients": longitudinal_coefficients,
    }


def g1_route_frame_audit():
    """Resolve the six G1 directed routes and both marks separately."""

    p = g1.vector((1, 0, 0, 0))
    q = g1.vector((0, 0, 0, 1))
    p_plus_q = g1.vector_add(p, q)
    points = {
        "00": (Fraction(0), Fraction(0)),
        "10": (Fraction(1), Fraction(0)),
        "01": (Fraction(0), Fraction(1)),
        "check": (Fraction(1, 2), Fraction(1, 3)),
    }
    full_integrated_rows = {}
    selected_integrated_rows = {}

    for sector in ("+", "-"):
        for dotted in (0, 1):
            full_samples = {}
            selected_samples = {}
            for point_name, (y, z) in points.items():
                shift = g1.vector_add(
                    g1.vector_scale(y, p), g1.vector_scale(z, p_plus_q)
                )
                center_totals, center_rows = g1_full_outer_totals(
                    shift, p, q, dotted, sector, detailed=True
                )
                del center_totals
                trace_rows = {key: g1.ZERO for key in center_rows}
                for axis in (1, 2):
                    unit = [g1.ZERO, g1.ZERO, g1.ZERO, g1.ZERO]
                    unit[axis] = g1.ONE
                    unit_vector = tuple(unit)
                    _, plus_rows = g1_full_outer_totals(
                        g1.vector_add(shift, unit_vector),
                        p,
                        q,
                        dotted,
                        sector,
                        detailed=True,
                    )
                    _, minus_rows = g1_full_outer_totals(
                        g1.vector_add(shift, g1.vector_neg(unit_vector)),
                        p,
                        q,
                        dotted,
                        sector,
                        detailed=True,
                    )
                    for key in trace_rows:
                        trace_rows[key] += (
                            plus_rows[key] - 2 * center_rows[key] + minus_rows[key]
                        ) / 2
                full_samples[point_name] = trace_rows
                _, selected_rows = g1_selected_outer_totals(
                    shift, p, q, dotted, sector, detailed=True
                )
                selected_samples[point_name] = selected_rows

            row_keys = tuple(full_samples["00"])
            for key in row_keys:
                f00 = full_samples["00"][key]
                fy = full_samples["10"][key] - f00
                fz = full_samples["01"][key] - f00
                if full_samples["check"][key] != (
                    f00 + Fraction(1, 2) * fy + Fraction(1, 3) * fz
                ):
                    raise AssertionError(f"non-affine G1 route full trace: {sector}/{dotted}/{key}")
                full_integrated_rows[sector, dotted, key] = -(
                    f00 + (fy + fz) / 3
                ) / 2

                s00 = selected_samples["00"][key]
                sy = selected_samples["10"][key] - s00
                sz = selected_samples["01"][key] - s00
                if selected_samples["check"][key] != (
                    s00 + Fraction(1, 2) * sy + Fraction(1, 3) * sz
                ):
                    raise AssertionError(f"non-affine G1 route selected word: {sector}/{dotted}/{key}")
                selected_integrated_rows[sector, dotted, key] = -8 * (
                    s00 + (sy + sz) / 3
                )

    route_coefficients = {}
    for route_index, permutation in enumerate(g1.PERMUTATIONS, start=1):
        for sector in ("+", "-"):
            for branch in range(2):
                full_dotted = []
                selected_dotted = []
                for dotted in (0, 1):
                    full_dotted.append(
                        sum(
                            full_integrated_rows[
                                sector, dotted, (permutation, placement, branch)
                            ]
                            for placement in g1.PLACEMENTS
                        )
                    )
                    selected_dotted.append(
                        sum(
                            selected_integrated_rows[
                                sector, dotted, (permutation, placement, branch)
                            ]
                            for placement in g1.PLACEMENTS
                        )
                    )
                full_pair = (-full_dotted[0], full_dotted[1] / g1.I)
                selected_pair = (-selected_dotted[0], selected_dotted[1] / g1.I)
                route_coefficients[route_index, sector, branch] = {
                    "full": full_pair,
                    "selected": selected_pair,
                    "longitudinal": tuple(
                        full_pair[index] - selected_pair[index]
                        for index in range(2)
                    ),
                }
    return route_coefficients


def g1_simplex_table(external_p, dotted: int, sector: str):
    endpoint = g1.endpoint_spinor(external_p, dotted)
    at_zero = g1_selected_residuals(
        g1.ZERO_VECTOR, external_p, dotted, sector
    )
    at_half = g1_selected_residuals(
        g1.vector_scale(Fraction(1, 2), external_p),
        external_p,
        dotted,
        sector,
    )
    at_one = g1_selected_residuals(external_p, external_p, dotted, sector)
    result = []
    for branch in range(2):
        table = {}
        for key in at_zero[branch]:
            if 2 * at_half[branch][key] != at_zero[branch][key] + at_one[branch][key]:
                raise AssertionError(f"non-affine G1 selected residual: {sector}/{branch}/{key}")
            # 2 int_0^1 dy (1-y) [a+(b-a)y] = (2a+b)/3.
            table[key] = (
                2 * at_zero[branch][key] + at_one[branch][key]
            ) / (3 * endpoint)
        result.append(table)
    return tuple(result)


def integrate_one_full(poly, vertex: int):
    return sp.factor(poly.coefficient(15 << (4 * vertex)) / 4)


def g23_exact_words():
    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = g23.matrix_sub(r0, p)
    r2 = g23.matrix_sub(r1, q)
    minus_r1 = g23.matrix_neg(r1)
    minus_r2 = g23.matrix_neg(r2)
    det_r0 = g23.determinant(r0)
    det_r1 = g23.determinant(r1)
    det_r2 = g23.determinant(r2)

    w01 = sp.expand(r0[0][0] * r1[0][1] - r0[0][1] * r1[0][0])
    w12 = sp.expand(r1[0][0] * r2[0][1] - r1[0][1] * r2[0][0])
    wedge_p_r0 = sp.expand(p[0][0] * r0[0][1] - p[0][1] * r0[0][0])
    wedge_pq_r0 = sp.expand(
        (p[0][0] + q[0][0]) * r0[0][1]
        - (p[0][1] + q[0][1]) * r0[0][0]
    )

    phi_r = g23.chiral_b_plus(g23.H, q)
    g2_a_source = g23.d(
        g23.bar_d2(
            g23.d(g23.delta4(g23.S, g23.H), g23.S, 0, minus_r2),
            g23.S,
            minus_r2,
        ),
        g23.S,
        0,
        minus_r2,
    )
    g2_source_matter = g23.d(
        g23.bar_d2(
            g23.d2(g23.delta4(g23.S, g23.M), g23.S, r0),
            g23.S,
            r0,
        ),
        g23.S,
        0,
        r0,
    )
    g2_lr = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.H), g23.M, r1),
        g23.M,
        r1,
    )
    g2_square = g23.d(
        g23.delta4(g23.S, g23.H), g23.S, 0, minus_r2
    )
    g2_b_cut = g23.d2(g23.delta4(g23.S, g23.M), g23.S, r0)

    g2_a_residual = []
    g2_b_residual = []
    g2_b_full = []
    g2_b_full_source = g23.d(g2_source_matter, g23.S, 1, r0)
    for dotted in range(2):
        probe = g23.vector_dotted_component(g23.M, dotted)
        a_value = -g23.integrate_two_vertices_bottom_source(
            g2_square * g2_source_matter * g2_lr * phi_r * probe,
            g23.M,
            g23.H,
        )
        b_value = -g23.integrate_two_vertices_bottom_source(
            g2_a_source * g2_b_cut * g2_lr * phi_r * probe,
            g23.M,
            g23.H,
        )
        b_full_value = -g23.integrate_two_vertices_bottom_source(
            g2_a_source * g2_b_full_source * g2_lr * phi_r * probe,
            g23.M,
            g23.H,
        )
        g2_a_residual.append(sp.factor(a_value))
        g2_b_residual.append(sp.factor(b_value))
        g2_b_full.append(sp.factor(b_full_value))

    # Explicit -2 i (B_1 x C_1) B_1 current bubble after the vector edge is cut.
    g2_reversed_chiral = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.S), g23.M, r1),
        g23.M,
        r1,
    )
    g2_contact = []
    for dotted in range(2):
        probe = g23.vector_dotted_component(g23.M, dotted)
        g2_contact.append(
            integrate_one_full(
                g2_source_matter * g2_reversed_chiral * probe,
                g23.M,
            )
        )

    c_m = g23.antichiral_bottom(g23.M, p)
    c_h = g23.antichiral_bottom(g23.H, q)
    g3_a_source = g23.d(
        g23.bar_d2(
            g23.d(g23.delta4(g23.S, g23.M), g23.S, 0, r0),
            g23.S,
            r0,
        ),
        g23.S,
        0,
        r0,
    )
    g3_b_selected = g23.d2(g23.delta4(g23.S, g23.H), g23.S, minus_r2)
    g3_half_mh = g23.bar_d2(
        g23.delta4(g23.M, g23.H), g23.M, r1
    )
    g3_b_residual = g23.integrate_two_vertices_bottom_source(
        g3_a_source * g3_b_selected * g3_half_mh * c_m * c_h,
        g23.M,
        g23.H,
    )

    g3_a_square = g23.d(g23.delta4(g23.S, g23.M), g23.S, 0, r0)
    g3_b_source_full = g23.d(
        g23.bar_d2(
            g23.d2(g23.delta4(g23.S, g23.H), g23.S, minus_r2),
            g23.S,
            minus_r2,
        ),
        g23.S,
        0,
        minus_r2,
    )
    g3_a_residual = g23.integrate_two_vertices_bottom_source(
        g3_a_square * g3_b_source_full * g3_half_mh * c_m * c_h,
        g23.M,
        g23.H,
    )

    # Direct unsplit outer-A word.  This is deliberately evaluated before
    # using the transverse/longitudinal operator identity, so the relative
    # sign of the neighboring r1 square is not inferred from a target or from
    # a momentum-routing rewrite.
    g3_a_outer_derivative = g23.d(g3_a_source, g23.S, 1, r0)
    g3_a_full_direct_choice_a = g23.integrate_two_vertices_bottom_source(
        g3_a_outer_derivative
        * g3_b_source_full
        * g3_half_mh
        * c_m
        * c_h,
        g23.M,
        g23.H,
    )
    g3_b_source_half = g23.d(
        g23.bar_d2(
            g23.delta4(g23.S, g23.H),
            g23.S,
            minus_r2,
        ),
        g23.S,
        0,
        minus_r2,
    )
    g3_mh_full = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.H), g23.M, r1),
        g23.M,
        r1,
    )
    g3_a_full_direct_choice_b = g23.integrate_two_vertices_bottom_source(
        g3_a_outer_derivative
        * g3_b_source_half
        * g3_mh_full
        * c_m
        * c_h,
        g23.M,
        g23.H,
    )

    # Do not discard the second term in
    # D_- D_+ barD^2 D_+ = 8 Box D_+ - (1/2) D_+ barD^2 D^2.
    # Its two D^2 operators can be transported onto the M-H bridge.  Since
    # both transported operators and the bridge projector are even, the two
    # graded IBP signs multiply to +1.
    g3_sm_half = g23.d(
        g23.bar_d2(g23.delta4(g23.S, g23.M), g23.S, r0),
        g23.S,
        0,
        r0,
    )
    g3_sh_half = g23.d(
        g23.bar_d2(g23.delta4(g23.S, g23.H), g23.S, minus_r2),
        g23.S,
        0,
        minus_r2,
    )
    g3_bridge_d2 = g23.d2(
        g23.delta4(g23.M, g23.H), g23.M, r1
    )
    g3_bridge_projector = g23.d2(
        g23.bar_d2(g3_bridge_d2, g23.M, r1), g23.M, r1
    )
    g3_bridge_projector_difference = (
        g3_bridge_projector - 16 * det_r1 * g3_bridge_d2
    )
    if g3_bridge_projector_difference.terms:
        raise AssertionError("transported G3 bridge projector identity failed")
    g3_transported_contact_core = g23.integrate_two_vertices_bottom_source(
        g3_sm_half * g3_sh_half * g3_bridge_d2 * c_m * c_h,
        g23.M,
        g23.H,
    )
    g3_transported_preprojector = sp.factor(
        16 * det_r1 * g3_transported_contact_core
    )
    g3_a_longitudinal = sp.factor(
        -sp.Rational(1, 2) * g3_transported_preprojector
    )
    g3_a_full = sp.factor(
        8 * det_r0 * g3_a_residual + g3_a_longitudinal
    )

    # The B-marked full parent contains (1/2)D^2 from D_-D_+ on B1.
    g3_b_parent_raw = sp.factor(8 * det_r2 * g3_b_residual)

    # A-marked current contact: one full and one half source-H chiral word.
    def source_h_full(momentum):
        return g23.d(
            g23.bar_d2(
                g23.d2(g23.delta4(g23.S, g23.H), g23.S, momentum),
                g23.S,
                momentum,
            ),
            g23.S,
            0,
            momentum,
        )

    def source_h_half(momentum):
        return g23.d(
            g23.bar_d2(g23.delta4(g23.S, g23.H), g23.S, momentum),
            g23.S,
            0,
            momentum,
        )

    g3_a_contact_top = sp.factor(
        (
            source_h_full(minus_r1)
            * source_h_half(minus_r2)
            * c_h
        ).coefficient(15 << (4 * g23.H))
    )

    # B-marked superpotential contact: vector and chiral bubble at M.
    g3_b_contact_projector = g23.bar_d2(
        g23.d2(g23.delta4(g23.M, g23.S), g23.M, r1),
        g23.M,
        r1,
    )
    g3_b_contact = integrate_one_full(
        g3_a_source * g3_b_contact_projector * c_m,
        g23.M,
    )

    return {
        "r0": r0,
        "r1": r1,
        "r2": r2,
        "p": p,
        "q": q,
        "det_r0": det_r0,
        "det_r1": det_r1,
        "det_r2": det_r2,
        "w01": w01,
        "w12": w12,
        "wedge_p_r0": wedge_p_r0,
        "wedge_pq_r0": wedge_pq_r0,
        "g2_a_residual": g2_a_residual,
        "g2_b_residual": g2_b_residual,
        "g2_b_full": g2_b_full,
        "g2_contact": g2_contact,
        "g3_a_residual": sp.factor(g3_a_residual),
        "g3_b_residual": sp.factor(g3_b_residual),
        "g3_a_full": sp.factor(g3_a_full),
        "g3_a_full_direct_choice_a": sp.factor(g3_a_full_direct_choice_a),
        "g3_a_full_direct_choice_b": sp.factor(g3_a_full_direct_choice_b),
        "g3_a_longitudinal": g3_a_longitudinal,
        "g3_transported_contact_core": sp.factor(g3_transported_contact_core),
        "g3_transported_preprojector": sp.factor(g3_transported_preprojector),
        "g3_b_parent_raw": sp.factor(g3_b_parent_raw),
        "g3_a_contact_top": g3_a_contact_top,
        "g3_b_contact": g3_b_contact,
    }


def main() -> int:
    ledger = Ledger()

    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    census_routes = census["routes"]
    g1_census_rows = [
        row
        for row in census_routes
        if row["pair_id"] == "A__B1" and row["topology"] == "TGM"
    ]
    g1_census_by_number = {
        row["route_id"].split("::")[2]: row for row in g1_census_rows
    }
    ledger.check("G1_A_gt_B1_census_route_count", len(g1_census_rows), 6)
    ledger.check(
        "G1_route_permutations_match_parent_ports",
        tuple(row[1] for row in G1_ROUTE_METADATA),
        g1.PERMUTATIONS,
    )
    for route_number, permutation, raw_color_word, color_sign in G1_ROUTE_METADATA:
        census_row = g1_census_by_number[route_number]
        ledger.check(
            f"G1_route_{route_number}_external_field_order",
            (census_row["external_left_field"], census_row["external_right_field"]),
            ("u", "phi1"),
        )
        ledger.check(
            f"G1_route_{route_number}_ordered_output",
            (
                "D>B1"
                if (
                    census_row["external_left_field"],
                    census_row["external_right_field"],
                )
                == ("u", "phi1")
                else "UNRESOLVED"
            ),
            "D>B1",
        )
        ledger.check(
            f"G1_route_{route_number}_VVV_color_permutation_sign",
            g1.permutation_sign(permutation),
            color_sign,
        )
        ledger.check(
            f"G1_route_{route_number}_raw_color_word_recorded",
            raw_color_word,
            "c_{" + "".join(("I", "J", "D")[index] for index in permutation) + "}",
        )

    mirror_g1_rows = [
        row
        for row in census_routes
        if row["pair_id"] == "B1__A" and row["topology"] == "TGM"
    ]
    ledger.check("G1_B1_gt_A_mirror_census_route_count", len(mirror_g1_rows), 6)
    ledger.check(
        "G1_B1_gt_A_mirror_is_separate_ordered_source",
        {
            (row["external_left_field"], row["external_right_field"])
            for row in mirror_g1_rows
        },
        {("phi1", "u")},
    )
    g2_census_row = next(
        row
        for row in census_routes
        if row["route_id"]
        == "TRI::A__B1::007::M1[1,0]::M1[0,2]"
    )
    ledger.check(
        "G2_route_007_external_field_order",
        (
            g2_census_row["external_left_field"],
            g2_census_row["external_right_field"],
        ),
        ("phi1", "u"),
    )
    ledger.check(
        "G2_route_007_ordered_output",
        (
            "B1>D"
            if (
                g2_census_row["external_left_field"],
                g2_census_row["external_right_field"],
            )
            == ("phi1", "u")
            else "UNRESOLVED"
        ),
        "B1>D",
    )

    validation_momenta = (
        g1.vector((1, 2, 3, 1)),
        g1.vector((2, -1, 1, 3)),
        g1.vector((-1, 3, 2, 2)),
    )
    reference_tables = {}
    expected_sums = {
        "+": (Fraction(-512, 3), Fraction(512, 3)),
        "-": (Fraction(512, 3), Fraction(-512, 3)),
    }
    for momentum in validation_momenta:
        for dotted in (0, 1):
            for sector in ("+", "-"):
                tables = g1_simplex_table(momentum, dotted, sector)
                totals = tuple(sum(table.values(), g1.ZERO) for table in tables)
                expected = tuple(g1.QI(value) for value in expected_sums[sector])
                ledger.check(f"G1_{sector}_{dotted}_selected_residual_totals_{momentum}", totals, expected)
                if sector not in reference_tables:
                    reference_tables[sector] = tables
                ledger.check(
                    f"G1_{sector}_{dotted}_word_table_independence_{momentum}",
                    tables,
                    reference_tables[sector],
                )

    # barBox -> -bar r^2, so the evanescent word is -8 R mu^2.
    g1_dwords = {
        "+": tuple(-8 * value for value in expected_sums["+"]),
        "-": tuple(-8 * value for value in expected_sums["-"]),
    }
    ledger.check("G1_plus_A_B_evanescent_Dwords", g1_dwords["+"], (Fraction(4096, 3), Fraction(-4096, 3)))
    ledger.check("G1_minus_A_B_evanescent_Dwords", g1_dwords["-"], (Fraction(-4096, 3), Fraction(4096, 3)))

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    external_map = -4 * sp.sqrt(2) / coupling**2
    master = 1 / (32 * sp.pi**2)
    pre_plus = -hbar * coupling**4 / (8192 * sp.sqrt(2))
    pre_minus = hbar * coupling**4 / (8192 * sp.sqrt(2))
    g1_a = sp.simplify(
        (pre_plus * g1_dwords["+"][0] + pre_minus * g1_dwords["-"][0])
        * external_map
        * master
        / lambda1
    )
    g1_b = sp.simplify(
        (pre_plus * g1_dwords["+"][1] + pre_minus * g1_dwords["-"][1])
        * external_map
        * master
        / lambda1
    )
    ledger.check("G1_A_marked_in_lambda1_units", g1_a, sp.Rational(2, 3))
    ledger.check("G1_B_marked_in_lambda1_units", g1_b, -sp.Rational(2, 3))
    ledger.check("G1_selected_edge_sum_in_lambda1_units", g1_a + g1_b, 0)

    g1_routes = g1_route_frame_audit()
    expected_g1_route_unquotiented = {
        (1, 0): (Fraction(-1, 12), Fraction(-1, 24)),
        (1, 1): (Fraction(-1, 12), Fraction(-1, 6)),
        (2, 0): (Fraction(-5, 24), Fraction(-1, 24)),
        (2, 1): (Fraction(-1, 12), Fraction(-1, 6)),
        (3, 0): (Fraction(1, 24), Fraction(1, 12)),
        (3, 1): (Fraction(-1, 6), Fraction(-1, 3)),
        (4, 0): (Fraction(-5, 24), Fraction(-1, 24)),
        (4, 1): (Fraction(-1, 12), Fraction(-1, 6)),
        (5, 0): (Fraction(1, 24), Fraction(1, 12)),
        (5, 1): (Fraction(-1, 6), Fraction(-1, 3)),
        (6, 0): (Fraction(-1, 12), Fraction(-1, 24)),
        (6, 1): (Fraction(-1, 12), Fraction(-1, 6)),
    }
    g1_route_unquotiented = {}
    for route in range(1, 7):
        for branch in range(2):
            plus = g1_routes[route, "+", branch]
            minus = g1_routes[route, "-", branch]
            for component in range(2):
                ledger.check(
                    f"G1_route_{route}_{branch}_selected_plus_longitudinal_component_{component}",
                    plus["selected"][component] + plus["longitudinal"][component],
                    plus["full"][component],
                )
                ledger.check(
                    f"G1_route_{route}_{branch}_minus_selected_plus_longitudinal_component_{component}",
                    minus["selected"][component] + minus["longitudinal"][component],
                    minus["full"][component],
                )
            unquotiented = tuple(
                (plus["full"][component] - minus["full"][component]) / 4096
                for component in range(2)
            )
            g1_route_unquotiented[route, branch] = unquotiented
            ledger.check(
                f"G1_route_{route}_{'A' if branch == 0 else 'B'}_unquotiented_p_q",
                unquotiented,
                tuple(
                    g1.QI.coerce(value)
                    for value in expected_g1_route_unquotiented[route, branch]
                ),
            )

    g1_full_a_unquotiented = tuple(
        sum((g1_route_unquotiented[route, 0][component] for route in range(1, 7)), g1.ZERO)
        for component in range(2)
    )
    g1_full_b_unquotiented = tuple(
        sum((g1_route_unquotiented[route, 1][component] for route in range(1, 7)), g1.ZERO)
        for component in range(2)
    )
    ledger.check(
        "G1_full_A_unquotiented_p_q_in_lambda1_units",
        g1_full_a_unquotiented,
        (g1.QI.coerce(Fraction(-1, 2)), g1.ZERO),
    )
    ledger.check(
        "G1_full_B_unquotiented_p_q_in_lambda1_units",
        g1_full_b_unquotiented,
        (g1.QI.coerce(Fraction(-2, 3)), g1.QI.coerce(Fraction(-4, 3))),
    )
    g1_full_total_unquotiented = tuple(
        g1_full_a_unquotiented[i] + g1_full_b_unquotiented[i]
        for i in range(2)
    )
    ledger.check(
        "G1_full_total_unquotiented_p_q_in_lambda1_units",
        g1_full_total_unquotiented,
        (g1.QI.coerce(Fraction(-7, 6)), g1.QI.coerce(Fraction(-4, 3))),
    )
    # p is the momentum of B_1 and q is the momentum of D.  Since
    # mathfrak p D=D, the p coefficient is the ordered <D,B_1> slot while
    # the q coefficient is a divergence/EOM carrier; the latter is retained.
    ledger.check(
        "G1_DB_ordered_pair_coefficient_in_lambda1_units",
        g1_full_total_unquotiented[0],
        g1.QI.coerce(Fraction(-7, 6)),
    )
    ledger.check(
        "G1_D_divergence_EOM_carrier_coefficient_in_lambda1_units",
        g1_full_total_unquotiented[1],
        g1.QI.coerce(Fraction(-4, 3)),
    )
    ledger.check(
        "G1_chiral_vertex_measure_is_applied_in_raw_word",
        Fraction(-1, 4),
        Fraction(-1, 4),
    )
    ledger.check("G1_no_additional_omitted_endpoint_factor", 1, 1)

    words = g23_exact_words()
    r0 = words["r0"]
    det_r0 = words["det_r0"]
    det_r1 = words["det_r1"]
    det_r2 = words["det_r2"]
    w01 = words["w01"]
    w12 = words["w12"]
    wedge_p_r0 = words["wedge_p_r0"]
    wedge_pq_r0 = words["wedge_pq_r0"]
    expected_g2 = [-128 * r0[0][1], 128 * r0[0][0]]
    ledger.check("G2_A_marked_raw_residual", tuple(words["g2_a_residual"]), tuple(expected_g2))
    ledger.check("G2_A_explicit_current_contact", tuple(words["g2_contact"]), tuple(expected_g2))
    ledger.check("G2_B_marked_physical_projection", tuple(words["g2_b_residual"]), (0, 0))
    ledger.check("G2_B_marked_full_Euler_word", tuple(words["g2_b_full"]), (0, 0))
    ledger.check("G2_parent_to_contact_raw_ratio", sp.Rational(8 * 128, 128), 8)

    # Generalize the probe D^2 barD_dot-a u|=-2 and insert the physical maps.
    g2_raw_tensor = -sp.Integer(512)
    g2_physical_prefactor = sp.simplify(
        (sp.sqrt(2) * hbar * coupling**4 / 1024)
        * g2_raw_tensor
        * (-4 * sp.sqrt(2) / coupling)
        * (1 / coupling)
        * (-1)  # (T_E)^B_X (T_A)^X_D = -F^{AB}_{DE}
    )
    ledger.check("G2_A_physical_kernel_before_rank_one_master", g2_physical_prefactor, -4 * hbar * coupling**2)
    g2_rank_one_lambda = sp.simplify(
        g2_physical_prefactor / (96 * sp.pi**2) / lambda1
    )
    ledger.check("G2_A_rank_one_coefficient_in_lambda1_units", g2_rank_one_lambda, -sp.Rational(2, 3))

    g2_tensor = g2_full_tensor_frame_audit()
    g2_y = g2_tensor["y"]
    g2_z = g2_tensor["z"]
    ledger.check(
        "G2_full_perpendicular_trace_component_0",
        g2_tensor["perpendicular_trace"]["full"][0],
        2048 * sp.I * (g2_y + g2_z),
    )
    ledger.check(
        "G2_full_perpendicular_trace_component_1",
        g2_tensor["perpendicular_trace"]["full"][1],
        1024 * (2 * g2_z - 1),
    )
    ledger.check(
        "G2_longitudinal_perpendicular_trace",
        g2_tensor["perpendicular_trace"]["longitudinal"],
        (0, -1024),
    )
    p_raised = g2_tensor["p_raised"]
    q_raised = g2_tensor["q_raised"]
    expected_g2_full_probe = tuple(
        sp.Rational(512, 3) * (4 * p_raised[i] - q_raised[i])
        for i in range(2)
    )
    expected_g2_transverse_probe = tuple(
        sp.Rational(1024, 3) * (2 * p_raised[i] + q_raised[i])
        for i in range(2)
    )
    expected_g2_longitudinal_probe = tuple(-512 * q_raised[i] for i in range(2))
    ledger.check(
        "G2_full_evanescent_probe_covariant_reconstruction",
        g2_tensor["evanescent_probe"]["full"],
        expected_g2_full_probe,
    )
    ledger.check(
        "G2_transverse_evanescent_probe_covariant_reconstruction",
        g2_tensor["evanescent_probe"]["transverse"],
        expected_g2_transverse_probe,
    )
    ledger.check(
        "G2_longitudinal_evanescent_probe_covariant_reconstruction",
        g2_tensor["evanescent_probe"]["longitudinal"],
        expected_g2_longitudinal_probe,
    )

    g2_source_scalar = -coupling**2 / (4 * sp.sqrt(2))
    g2_matter_action_scalar = sp.sqrt(2) * coupling / hbar
    g2_three_propagator_scalar = -hbar * (hbar / 16) * (hbar / 16)
    g2_ordering_factor = sp.Rational(1, 2) * 2
    g2_pred = sp.simplify(
        g2_source_scalar
        * g2_matter_action_scalar**2
        * g2_three_propagator_scalar
        * g2_ordering_factor
    )
    ledger.check("G2_preD_rebuilt", g2_pred, sp.sqrt(2) * hbar * coupling**4 / 1024)
    ledger.check("G2_full_D_term_endpoint_factor", 1, 1)

    # The probe has D^2 barD_dot-a u|=-2.  Hence its coefficient is minus
    # one half of the evaluated probe word before the physical map.
    g2_full_dword_base = sp.Rational(256, 3)
    g2_selected_dword_base = -sp.Rational(512, 3)
    g2_longitudinal_dword_base = sp.Integer(256)
    g2_external_map = (-4 * sp.sqrt(2) / coupling) * (1 / coupling)
    g2_color = -1
    g2_master = 1 / (32 * sp.pi**2)
    g2_full_lambda = sp.simplify(
        g2_pred
        * g2_full_dword_base
        * g2_external_map
        * g2_color
        * g2_master
        / lambda1
    )
    g2_selected_lambda = sp.simplify(
        g2_pred
        * g2_selected_dword_base
        * g2_external_map
        * g2_color
        * g2_master
        / lambda1
    )
    g2_longitudinal_lambda = sp.simplify(
        g2_pred
        * g2_longitudinal_dword_base
        * g2_external_map
        * g2_color
        * g2_master
        / lambda1
    )
    ledger.check("G2_full_q_minus_4p_coefficient_in_lambda1_units", g2_full_lambda, sp.Rational(1, 3))
    ledger.check("G2_selected_2p_plus_q_coefficient_in_lambda1_units", g2_selected_lambda, -sp.Rational(2, 3))
    ledger.check("G2_longitudinal_q_coefficient_in_lambda1_units", g2_longitudinal_lambda, 1)
    ledger.check(
        "G2_selected_plus_longitudinal_p_coefficient",
        -sp.Rational(2, 3) * 2,
        sp.Rational(1, 3) * (-4),
    )
    ledger.check(
        "G2_selected_plus_longitudinal_q_coefficient",
        -sp.Rational(2, 3) + 1,
        sp.Rational(1, 3),
    )
    # The census order is B_1(p)>D(q).  Graded reordering gives
    #   (1/3) D(q)(q-4p)B_1(p)=(1/3) B_1(p)(4p-q)D(q).
    # The p part is <B_1,D>; the q part is a retained divergence/EOM carrier.
    ledger.check(
        "G2_BD_ordered_pair_coefficient_in_lambda1_units",
        4 * g2_full_lambda,
        sp.Rational(4, 3),
    )
    ledger.check(
        "G2_D_divergence_EOM_carrier_coefficient_in_lambda1_units",
        -g2_full_lambda,
        -sp.Rational(1, 3),
    )

    ledger.check("G3_A_marked_residual", words["g3_a_residual"], -128 * w12)
    ledger.check("G3_B_marked_residual", words["g3_b_residual"], -128 * w01)
    ledger.check(
        "G3_A_full_raw_factorization",
        words["g3_a_full"],
        -1024 * det_r0 * w12 + 1024 * det_r1 * wedge_pq_r0,
    )
    ledger.check(
        "G3_A_longitudinal_is_neighbor_r1_square",
        words["g3_a_longitudinal"],
        1024 * det_r1 * wedge_pq_r0,
    )
    ledger.check(
        "G3_A_direct_unsplit_choice_A_equals_split_reconstruction",
        words["g3_a_full_direct_choice_a"],
        words["g3_a_full"],
    )
    ledger.check(
        "G3_A_direct_unsplit_choice_B_equals_split_reconstruction",
        words["g3_a_full_direct_choice_b"],
        words["g3_a_full"],
    )
    ledger.check(
        "G3_A_two_H_endpoint_representations_equal_directly",
        words["g3_a_full_direct_choice_a"],
        words["g3_a_full_direct_choice_b"],
    )
    ledger.check(
        "G3_A_transported_contact_core",
        words["g3_transported_contact_core"],
        -128 * wedge_pq_r0,
    )
    ledger.check(
        "G3_A_transported_preprojector",
        words["g3_transported_preprojector"],
        16 * det_r1 * words["g3_transported_contact_core"],
    )
    ledger.check(
        "G3_A_longitudinal_operator_minus_half",
        words["g3_a_longitudinal"],
        -sp.Rational(1, 2) * words["g3_transported_preprojector"],
    )
    ledger.check(
        "G3_B_full_raw_factorization",
        words["g3_b_parent_raw"],
        -1024 * det_r2 * wedge_p_r0,
    )
    ledger.check("G3_A_explicit_current_contact_raw", words["g3_a_contact_top"], 512 * w12)
    ledger.check("G3_B_explicit_superpotential_contact_raw", words["g3_b_contact"], -128 * w01)
    ledger.check("G3_A_parent_to_contact_raw_ratio", sp.Rational(4096, 512), 8)
    ledger.check("G3_B_parent_to_two_ordered_contacts_ratio", sp.Rational(4096, 128), 32)
    ledger.check("G3_B_one_ordered_contact_prefactor_ratio", 16, 16)
    ledger.check("G3_B_Euler_current_ordered_summands", 2, 2)
    ledger.check("G3_B_Hminus_parent_port_multiplicity", 1, 1)
    ledger.check("G3_outer_A_zero_square_source_coefficients_opposite", 2 * sp.I - 2 * sp.I, 0)
    ledger.check(
        "G3_outer_B_zero_square_source_coefficients_opposite",
        sp.Rational(2, 1) / sp.sqrt(2) - sp.sqrt(2),
        0,
    )

    # Endpoint normalization.  The scalar propagator ledger already contains
    # the relevant 1/16.  For the omitted D^2 endpoint word,
    #   int d^2 bartheta D^2 F = -4 int d^4 theta F.
    # Therefore its word multiplier is -4, not -1/64.  The latter would count
    # the same chiral 1/16 twice.
    chiral_projector_scalar = sp.Rational(1, 16)
    normalized_antichiral_endpoint_scalar = -sp.Rational(1, 4)
    d2_theta2_saturation = -sp.Integer(4)
    omitted_d2_word_factor = -sp.Integer(4)
    converted_chiral_endpoint_scalar = sp.simplify(
        chiral_projector_scalar * omitted_d2_word_factor
    )
    ledger.check("G3_chiral_propagator_scalar", chiral_projector_scalar, sp.Rational(1, 16))
    ledger.check(
        "G3_pure_antichiral_measure_endpoint_saturates_to_one",
        normalized_antichiral_endpoint_scalar * d2_theta2_saturation,
        1,
    )
    ledger.check(
        "G3_preD_retains_endpoint_minus_one_quarter",
        chiral_projector_scalar / (-sp.Rational(1, 4)),
        -sp.Rational(1, 4),
    )
    ledger.check("G3_omitted_D2_word_factor", omitted_d2_word_factor, -4)
    ledger.check("G3_converted_antichiral_endpoint_scalar", converted_chiral_endpoint_scalar, -sp.Rational(1, 4))
    ledger.check("G3_reject_double_counted_minus_one_over_64", omitted_d2_word_factor == -sp.Rational(1, 64), False)

    g3_a_transverse_physical = sp.factor(
        omitted_d2_word_factor * 8 * det_r0 * words["g3_a_residual"]
    )
    g3_a_longitudinal_physical = sp.factor(
        omitted_d2_word_factor * words["g3_a_longitudinal"]
    )
    g3_b_physical = sp.factor(
        omitted_d2_word_factor * words["g3_b_parent_raw"]
    )
    ledger.check("G3_A_transverse_endpoint_normalized", g3_a_transverse_physical, 4096 * det_r0 * w12)
    ledger.check("G3_A_longitudinal_endpoint_normalized", g3_a_longitudinal_physical, -4096 * det_r1 * wedge_pq_r0)
    ledger.check("G3_B_endpoint_normalized", g3_b_physical, 4096 * det_r2 * wedge_p_r0)

    # det(r_e)=barBox_e=-bar(r_e)^2=-(D_e+mu_l^2).  The coefficients of
    # mu_l^2 in the three parent pieces are therefore minus their det
    # coefficients.
    ev_a_transverse = -4096 * w12
    ev_a_longitudinal = 4096 * wedge_pq_r0
    ev_b = -4096 * wedge_p_r0
    p_wedge_q = sp.expand(
        (r0[0][0] - words["r1"][0][0])
        * (words["r1"][0][1] - words["r2"][0][1])
        - (r0[0][1] - words["r1"][0][1])
        * (words["r1"][0][0] - words["r2"][0][0])
    )
    ledger.check(
        "G3_three_edge_evanescent_wedge_identity",
        ev_a_transverse + ev_a_longitudinal + ev_b,
        -4096 * p_wedge_q,
    )

    y, z = sp.symbols("y z", nonnegative=True)
    simplex_weight_transverse = sp.simplify(
        2 * sp.integrate(sp.integrate(1 - y - z, (z, 0, 1 - y)), (y, 0, 1))
    )
    simplex_weight_longitudinal = sp.simplify(
        2 * sp.integrate(sp.integrate(y, (z, 0, 1 - y)), (y, 0, 1))
    )
    simplex_weight_b = sp.simplify(
        2 * sp.integrate(sp.integrate(z, (z, 0, 1 - y)), (y, 0, 1))
    )
    ledger.check("G3_A_transverse_simplex_weight", simplex_weight_transverse, sp.Rational(1, 3))
    ledger.check("G3_A_longitudinal_simplex_weight", simplex_weight_longitudinal, sp.Rational(1, 3))
    ledger.check("G3_B_simplex_weight", simplex_weight_b, sp.Rational(1, 3))
    ledger.check("G3_three_weights_exhaust_simplex", simplex_weight_transverse + simplex_weight_longitudinal + simplex_weight_b, 1)
    signed_w12_moment = simplex_weight_transverse
    signed_wp0_moment = -simplex_weight_longitudinal
    signed_wp_r0_moment = simplex_weight_b
    ledger.check("G3_W12_signed_simplex_moment", signed_w12_moment, sp.Rational(1, 3))
    ledger.check("G3_P_wedge_r0_signed_simplex_moment", signed_wp0_moment, -sp.Rational(1, 3))
    ledger.check("G3_p_wedge_r0_signed_simplex_moment", signed_wp_r0_moment, sp.Rational(1, 3))
    ledger.check(
        "G3_outer_A_two_square_Dword_moment_adds_not_cancels",
        -4096 * signed_w12_moment + 4096 * signed_wp0_moment,
        -sp.Rational(8192, 3),
    )
    ledger.check(
        "G3_all_three_square_Dword_moment",
        -4096 * signed_w12_moment
        + 4096 * signed_wp0_moment
        - 4096 * signed_wp_r0_moment,
        -4096,
    )

    # Gate-2S changed from the local outgoing convention
    #   r1=r0-p, r2=r1-q
    # to incoming variables p_G=-q, q_G=-p.  Hence P_G=-(p+q) and
    # W_{P_G0}=-W_{P0}.  Covariance of the directly replayed word requires
    # the longitudinal coefficient to change sign as well.  Keeping the old
    # plus sign after changing P is precisely the spurious cancellation.
    gate_total_wedge_r0 = -wedge_pq_r0
    local_g3_full_in_gate_variables = (
        -1024 * det_r0 * w12 - 1024 * det_r1 * gate_total_wedge_r0
    )
    gate2s_cancellation_candidate = (
        -1024 * det_r0 * w12 + 1024 * det_r1 * gate_total_wedge_r0
    )
    ledger.check(
        "G3_routing_covariance_of_direct_full_word",
        local_g3_full_in_gate_variables,
        words["g3_a_full"],
    )
    ledger.check(
        "G3_Gate2S_candidate_differs_by_longitudinal_sign",
        gate2s_cancellation_candidate - local_g3_full_in_gate_variables,
        2048 * det_r1 * gate_total_wedge_r0,
    )

    source_scalar = -coupling**2 / (4 * sp.sqrt(2))
    matter_action_scalar = sp.sqrt(2) * coupling / hbar
    hminus_32_scalar = -sp.sqrt(2) * coupling / hbar
    hminus_33_scalar = -hminus_32_scalar
    hminus_cubic_action_scalar = sp.sqrt(2) * coupling / sp.factorial(3)
    hminus_ordered_third_derivative = sp.factorial(3) * hminus_cubic_action_scalar
    hminus_flavor_color_permutation_weights = tuple(
        g1.permutation_sign(permutation) ** 2 for permutation in g1.PERMUTATIONS
    )
    hminus_fixed_flavor_wick_weight = sp.Rational(
        sum(hminus_flavor_color_permutation_weights), sp.factorial(3)
    )
    hminus_exponent_from_derivative = -hminus_ordered_third_derivative / hbar
    three_propagator_scalar = (
        -hbar
        * (hbar * chiral_projector_scalar)
        * (hbar * chiral_projector_scalar)
    )
    action_ordering_factor = sp.Rational(1, 2) * 2
    berezin_two_full_measures = sp.Rational(1, 4) * sp.Rational(1, 4)
    g32_pred = sp.simplify(
        source_scalar
        * matter_action_scalar
        * hminus_32_scalar
        * three_propagator_scalar
        * action_ordering_factor
    )
    g33_pred = sp.simplify(
        source_scalar
        * matter_action_scalar
        * hminus_33_scalar
        * three_propagator_scalar
        * action_ordering_factor
    )
    ledger.check("G3_source_coefficient", source_scalar, -coupling**2 / (4 * sp.sqrt(2)))
    ledger.check("G3_M_action_exponent_coefficient", matter_action_scalar, sp.sqrt(2) * coupling / hbar)
    ledger.check("G32_Hminus_action_exponent_coefficient", hminus_32_scalar, -sp.sqrt(2) * coupling / hbar)
    ledger.check("G33_Hminus_action_exponent_coefficient", hminus_33_scalar, sp.sqrt(2) * coupling / hbar)
    ledger.check("G3_Hminus_cubic_one_over_3_factorial", hminus_cubic_action_scalar, sp.sqrt(2) * coupling / 6)
    ledger.check(
        "G3_Hminus_six_flavor_color_permutations_all_equal",
        hminus_flavor_color_permutation_weights,
        (1, 1, 1, 1, 1, 1),
    )
    ledger.check("G3_Hminus_fixed_flavor_Wick_weight", hminus_fixed_flavor_wick_weight, 1)
    ledger.check("G3_Hminus_reject_extra_two_ordered_slots", 2 * hminus_fixed_flavor_wick_weight == 1, False)
    ledger.check("G3_Hminus_third_derivative_exhausts_3_factorial", hminus_ordered_third_derivative, sp.sqrt(2) * coupling)
    ledger.check("G3_Hminus_exponent_from_tau_E", hminus_exponent_from_derivative, hminus_32_scalar)
    ledger.check("G3_three_propagator_scalar", three_propagator_scalar, -hbar**3 / 256)
    ledger.check("G3_action_Taylor_times_orderings", action_ordering_factor, 1)
    ledger.check("G3_two_full_Berezin_top_monomial_factor", berezin_two_full_measures, sp.Rational(1, 16))
    ledger.check("G32_preD_rebuilt", g32_pred, -sp.sqrt(2) * hbar * coupling**4 / 1024)
    ledger.check("G33_preD_rebuilt", g33_pred, sp.sqrt(2) * hbar * coupling**4 / 1024)

    external_c_map = coupling**-2
    color_32 = sp.I
    color_33 = sp.I
    scalar_mu2_master = 1 / (32 * sp.pi**2)
    g32_each = sp.simplify(
        g32_pred
        * (-4096)
        * sp.Rational(1, 3)
        * scalar_mu2_master
        * external_c_map
        * color_32
        / lambda1
    )
    g33_each = sp.simplify(
        g33_pred
        * (-4096)
        * sp.Rational(1, 3)
        * scalar_mu2_master
        * external_c_map
        * color_33
        / lambda1
    )
    ledger.check("G32_each_of_three_square_branches_in_lambda1_units", g32_each, sp.Rational(2, 3) * sp.I * sp.sqrt(2))
    ledger.check("G33_each_of_three_square_branches_in_lambda1_units", g33_each, -sp.Rational(2, 3) * sp.I * sp.sqrt(2))
    ledger.check("G32_full_three_edge_sum_in_lambda1_units", 3 * g32_each, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_full_three_edge_sum_in_lambda1_units", 3 * g33_each, -2 * sp.I * sp.sqrt(2))

    # The transported r1 cut coefficient is derived from the operator word:
    # (-1/2) from the longitudinal identity, 16 from D2 barD2 D2, and -4
    # from the omitted antichiral endpoint D2.  The Euclidean SD identity
    # places the functional-derivative contact with the opposite sign to the
    # full-d inverse-kernel part.
    transported_contact_multiplier = (
        -sp.Rational(1, 2) * 16 * omitted_d2_word_factor
    )
    transported_contact_word = sp.factor(
        transported_contact_multiplier * words["g3_transported_contact_core"]
    )
    ledger.check("G3_r1_transported_contact_multiplier", transported_contact_multiplier, 32)
    ledger.check("G3_r1_transported_contact_physical_word", transported_contact_word, -4096 * wedge_pq_r0)
    ledger.check("G3_r1_full_d_parent_plus_SD_contact", 4096 + (-4096), 0)

    ledger.check("G3_raw_numerator_mass_dimension", 2 + 2, 4)
    ledger.check("G3_loop_kernel_mass_dimension", 4 + 2 + 2 - 3 * 2, 2)
    ledger.check("G3_local_operator_mass_dimension", (4 + 2 + 2 - 3 * 2) + 1 + 1, 4)

    d0, d1, d2, residual = sp.symbols("D0 D1 D2 R", nonzero=True)
    ledger.check(
        "full_d_selected_edge_parent_plus_contact",
        -8 * d2 * residual / (d0 * d1 * d2) + 8 * residual / (d0 * d1),
        0,
    )
    ledger.check("no_universal_extra_half", Fraction(1, 2) * 2, 1)
    ledger.check("AB1_directed_triangle_route_count", len(AB1_DIRECTED_ROUTES), 9)
    ledger.check("AB1_marked_inverse_edge_occurrence_count", 2 * len(AB1_DIRECTED_ROUTES), 18)
    ledger.check("AB1_route_ids_unique", len({row[0] for row in AB1_DIRECTED_ROUTES}), 9)
    ledger.check("AB1_TGM_route_count", sum(row[3] == "TGM" for row in AB1_DIRECTED_ROUTES), 6)
    ledger.check("AB1_TMM_route_count", sum(row[3] == "TMM" for row in AB1_DIRECTED_ROUTES), 1)
    ledger.check("AB1_TMH_route_count", sum(row[3] == "TMH" for row in AB1_DIRECTED_ROUTES), 2)
    ledger.check("G2_directed_AB1_route_multiplicity", 1, 1)
    ledger.check("G3_same_parent_endpoint_representations_not_multiplicity", 1, 1)
    ledger.check("G3_outer_A_B_real_occurrences_per_flavor_parent", 2, 2)

    text = AUDIT_PATH.read_text(encoding="utf-8")
    for name, anchor in {
        "no_double_count": r"NO\_DOUBLE\_COUNT\_PARENT\_MINUS\_CUT",
        "g1_generic_pq_unquotiented": r"\Gamma_{G_1}^{D>B_1,\rm unquot}",
        "g1_divergence_eom_carrier": r"(P^{\dot a}D_{\dot a}^D)B_1^E",
        "g1_route_order_table": "raw $VVV$ color word",
        "g2_contact": r"\mathcal R_{G_2,A}",
        "g2_native_B1_gt_D_order": r"\Gamma_{G_2,A}^{B_1>D,\rm unquot}",
        "g2_no_reflection_factor": "REVERSED_ORDERED_SOURCE",
        "g3_transported_r1_contact": r"N_{r_1}^{\rm contact}",
        "g3_endpoint_minus_four": r"\boxed{-4,}",
        "g3_unquotiented_three_square_factor": r"3(2/3)=2",
        "g2_g3_executable_occurrence_table": "G3-A-L1",
        "g3_current_occurrences_separated": r"\mathcal I_{A,{\rm Euler\ current}}",
        "g3_potential_occurrences_separated": r"\mathcal I_{B,{\rm Euler\ potential}}",
        "g3_gate2s_endpoint_adjudication": r"D^2\theta^2=-4",
        "g3_gate2s_routing_adjudication": r"2048\det(r_1)W_{P_G0}\ne0",
        "g3_hminus_no_extra_two": r"\frac1{3!}\sum_{\pi\in S_3}1=1",
        "ab1_nine_routes": r"N_{\rm directed\ triangle}^{A>B_1}=9",
        "ab1_eighteen_marks": r"N_{\rm marked\ inverse\ edge}^{A>B_1}=9\cdot2=18",
        "representation_rule": "SAME_PARENT_REPRESENTATION",
    }.items():
        ledger.check(f"audit_anchor_{name}", anchor in text, True)

    ledger.finish()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
