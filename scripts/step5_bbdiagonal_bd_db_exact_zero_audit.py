#!/usr/bin/env python3
"""Exact target-blind closure of BB diagonal and BD/DB anomaly sectors.

The calculation reads only the target-blind structural parent census and the
local exact sparse-Grassmann D-algebra engine.  It emits every split-source
and spectator parent route for the three BB-diagonal and twelve BD/DB ordered
pairs.  No Project-result or holomorphic-twist ledger is read.
"""

from __future__ import annotations

import argparse
import gc
import importlib.util
import itertools
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CENSUS_PATH = ROOT / "audits/step5-all-triangle-parent-port-census.json"
DWORD_ENGINE_PATH = ROOT / "scripts/step5_ab1_g2_g3_dword_replay.py"
OUTPUT_JSON = ROOT / "audits/step5-bbdiagonal-bd-db-exact-zero.json"
OUTPUT_MD = ROOT / "audits/step5-bbdiagonal-bd-db-exact-zero.md"

FORBIDDEN_INPUTS = {
    ROOT / "generated/step5/project-result-ledger.json",
    ROOT / "generated/step5/ht_ordered_pair_targets.json",
}
INPUTS = (CENSUS_PATH, DWORD_ENGINE_PATH)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


g = load_module("step5_g23_for_bbdiag_bd_db_zero", DWORD_ENGINE_PATH)

BB_DIAGONAL_PAIRS = tuple(f"B{r}__B{r}" for r in range(1, 4))
BD_PAIRS = tuple(f"B{r}__Ddot{dot}" for r in range(1, 4) for dot in range(1, 3))
DB_PAIRS = tuple(f"Ddot{dot}__B{r}" for dot in range(1, 3) for r in range(1, 4))
TARGET_PAIRS = BB_DIAGONAL_PAIRS + BD_PAIRS + DB_PAIRS

EPS_UP = ((0, 1), (-1, 0))
ZERO_MATRIX = [[sp.Integer(0), sp.Integer(0)], [sp.Integer(0), sp.Integer(0)]]


class Ledger:
    def __init__(self) -> None:
        self.rows: list[dict[str, Any]] = []

    def zero(self, name: str, expression: object) -> None:
        value = sp.factor(sp.sympify(expression))
        if sp.simplify(value) != 0:
            raise AssertionError(f"{name}: expected zero, got {value}")
        self.rows.append({"name": name, "actual": "0", "expected": "0", "passed": True})


def matrix_add(left, right):
    return [[sp.expand(left[a][b] + right[a][b]) for b in range(2)] for a in range(2)]


def matrix_neg(value):
    return [[-value[a][b] for b in range(2)] for a in range(2)]


def d_up(poly, vertex: int, spinor: int, momentum):
    return sum(EPS_UP[spinor][lower] * g.d(poly, vertex, lower, momentum) for lower in range(2))


def bar_d_up(poly, vertex: int, dotted: int, momentum):
    return sum(EPS_UP[dotted][lower] * g.bar_d(poly, vertex, lower, momentum) for lower in range(2))


def polarized_vvv_word(sector: str, placement: str, permutation, endpoints, endpoint_momenta):
    """Exact symbolic cubic-vector D-word in the locked G23 conventions."""

    i, j, k = permutation
    ij_momentum = matrix_add(endpoint_momenta[i], endpoint_momenta[j])
    jk_momentum = matrix_add(endpoint_momenta[j], endpoint_momenta[k])
    word = g.Grassmann()
    if sector == "+" and placement == "QL":
        for spinor in range(2):
            word += g.bar_d2(
                endpoints[i] * d_up(endpoints[j], g.H, spinor, endpoint_momenta[j]),
                g.H,
                ij_momentum,
            ) * g.bar_d2(
                g.d(endpoints[k], g.H, spinor, endpoint_momenta[k]),
                g.H,
                endpoint_momenta[k],
            )
    elif sector == "+" and placement == "LQ":
        for spinor in range(2):
            word += g.bar_d2(
                d_up(endpoints[i], g.H, spinor, endpoint_momenta[i]),
                g.H,
                endpoint_momenta[i],
            ) * g.bar_d2(
                endpoints[j] * g.d(endpoints[k], g.H, spinor, endpoint_momenta[k]),
                g.H,
                jk_momentum,
            )
    elif sector == "-" and placement == "QL":
        for dotted in range(2):
            word += g.d2(
                endpoints[i] * g.bar_d(endpoints[j], g.H, dotted, endpoint_momenta[j]),
                g.H,
                ij_momentum,
            ) * g.d2(
                bar_d_up(endpoints[k], g.H, dotted, endpoint_momenta[k]),
                g.H,
                endpoint_momenta[k],
            )
    elif sector == "-" and placement == "LQ":
        for dotted in range(2):
            word += g.d2(
                g.bar_d(endpoints[i], g.H, dotted, endpoint_momenta[i]),
                g.H,
                endpoint_momenta[i],
            ) * g.d2(
                endpoints[j] * bar_d_up(endpoints[k], g.H, dotted, endpoint_momenta[k]),
                g.H,
                jk_momentum,
            )
    else:
        raise ValueError((sector, placement))
    return word


def integrate_full_m_gauge(poly, sector: str) -> sp.Expr:
    projected = (
        -sp.Rational(1, 4) * g.d2(poly, g.H, ZERO_MATRIX)
        if sector == "+"
        else -sp.Rational(1, 4) * g.bar_d2(poly, g.H, ZERO_MATRIX)
    )
    full_m_mask = 15 << (4 * g.M)
    return sp.factor(projected.coefficient(full_m_mask) / 4)


def epsilon3(i: int, j: int, k: int) -> int:
    if {i, j, k} != {1, 2, 3}:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


def symbolic_momenta():
    r_symbols = sp.symbols("r00 r01 r10 r11")
    p_symbols = sp.symbols("p00 p01 p10 p11")
    q_symbols = sp.symbols("q00 q01 q10 q11")
    r0 = [list(r_symbols[:2]), list(r_symbols[2:])]
    p = [list(p_symbols[:2]), list(p_symbols[2:])]
    q = [list(q_symbols[:2]), list(q_symbols[2:])]
    r1 = g.matrix_sub(r0, p)
    r2 = g.matrix_sub(r1, q)
    return r0, r1, r2, p, q


def prove_bd_tgm_zero(ledger: Ledger, r0, p, q) -> dict[str, Any]:
    """Prove every physical B-D projection of all cubic-gauge words is zero."""

    source_vector_endpoint_momentum = matrix_add(matrix_add(r0, matrix_neg(p)), matrix_neg(q))
    matter_vertex_endpoint_momentum = matrix_add(matrix_neg(r0), p)
    source_derivative_momentum = matrix_neg(source_vector_endpoint_momentum)
    endpoint_momenta = (source_vector_endpoint_momentum, matter_vertex_endpoint_momentum, q)

    matter_line = g.bar_d2(g.d2(g.delta4(g.S, g.M), g.S, r0), g.S, r0)
    b_mark = g.d(g.d(matter_line, g.S, 0, r0), g.S, 1, r0)
    external_b = g.chiral_b_plus(g.M, p)
    count = 0
    for source_dotted in range(2):
        for output_dotted in range(2):
            endpoints = (
                g.delta4(g.S, g.H),
                g.delta4(g.M, g.H),
                g.vector_dotted_component(g.H, output_dotted),
            )
            for sector in ("+", "-"):
                for permutation in itertools.permutations((0, 1, 2)):
                    for placement in ("QL", "LQ"):
                        cubic_word = polarized_vvv_word(
                            sector,
                            placement,
                            permutation,
                            endpoints,
                            endpoint_momenta,
                        )
                        d_source = g.d2(
                            g.bar_d(
                                cubic_word,
                                g.S,
                                source_dotted,
                                source_derivative_momentum,
                            ),
                            g.S,
                            source_derivative_momentum,
                        )
                        result = integrate_full_m_gauge(d_source * b_mark * external_b, sector)
                        name = (
                            f"BD_TGM_srcdot{source_dotted}_outdot{output_dotted}_"
                            f"{sector}_{permutation}_{placement}"
                        )
                        ledger.zero(name, result)
                        count += 1
            sp.core.cache.clear_cache()
            gc.collect()
    if count != 96:
        raise AssertionError(count)
    return {
        "symbolic_projection_count": count,
        "source_projector": "D_S^2 barD_(S,dot-a)",
        "marked_B_projector": "D_(S,-)D_(S,+) barD_S^2 D_S^2",
        "sectors": ["chiral gauge cubic", "antichiral gauge cubic"],
        "gauge_permutations": 6,
        "derivative_placements": ["QL", "LQ"],
        "result": "EXACT_ZERO_EACH_WORD",
    }


def prove_bd_tmm_tmh_quartic_zero(ledger: Ledger, r0, r1, r2, p, q) -> dict[str, Any]:
    minus_r2 = matrix_neg(r2)

    external_phi = g.chiral_b_plus(g.H, q)
    b_selected = g.d2(g.delta4(g.S, g.M), g.S, r0)
    lr_full = g.bar_d2(g.d2(g.delta4(g.M, g.H), g.M, r1), g.M, r1)
    tmm_count = 0
    for source_dotted in range(2):
        d_source = g.d2(
            g.bar_d(g.delta4(g.S, g.H), g.S, source_dotted, minus_r2),
            g.S,
            minus_r2,
        )
        common = d_source * b_selected * lr_full * external_phi
        for output_dotted in range(2):
            result = -g.integrate_two_vertices_bottom_source(
                common * g.vector_dotted_component(g.M, output_dotted),
                g.M,
                g.H,
            )
            ledger.zero(f"BD_TMM_srcdot{source_dotted}_outdot{output_dotted}", result)
            tmm_count += 1

    del common, d_source, external_phi, b_selected, lr_full
    sp.core.cache.clear_cache()
    gc.collect()

    c_m = g.antichiral_bottom(g.M, p)
    c_h = g.antichiral_bottom(g.H, q)
    half_mh = g.bar_d2(g.delta4(g.M, g.H), g.M, r1)
    choice_a_full = sp.Rational(1, 2) * g.d2(
        g.bar_d2(g.d2(g.delta4(g.S, g.H), g.S, minus_r2), g.S, minus_r2),
        g.S,
        minus_r2,
    )
    choice_b_half = sp.Rational(1, 2) * g.d2(
        g.bar_d2(g.delta4(g.S, g.H), g.S, minus_r2),
        g.S,
        minus_r2,
    )
    choice_b_mh_full = g.bar_d2(g.d2(g.delta4(g.M, g.H), g.M, r1), g.M, r1)
    tmh_count = 0
    for source_dotted in range(2):
        d_source = g.d2(
            g.bar_d(g.delta4(g.S, g.M), g.S, source_dotted, r0),
            g.S,
            r0,
        )
        choice_a = g.integrate_two_vertices_bottom_source(
            d_source * choice_a_full * half_mh * c_m * c_h,
            g.M,
            g.H,
        )
        choice_b = g.integrate_two_vertices_bottom_source(
            d_source * choice_b_half * choice_b_mh_full * c_m * c_h,
            g.M,
            g.H,
        )
        ledger.zero(f"BD_TMH_srcdot{source_dotted}_choiceA", choice_a)
        ledger.zero(f"BD_TMH_srcdot{source_dotted}_choiceB", choice_b)
        tmh_count += 2

    del choice_a, choice_b, d_source, c_m, c_h, half_mh, choice_a_full, choice_b_half, choice_b_mh_full
    sp.core.cache.clear_cache()
    gc.collect()

    matter_line = g.bar_d2(g.d2(g.delta4(g.S, g.M), g.S, r0), g.S, r0)
    b_mark = g.d(g.d(matter_line, g.S, 0, r0), g.S, 1, r0)
    external_b = g.chiral_b_plus(g.M, p)
    source_vector_momentum = matrix_add(matrix_add(matrix_neg(r0), p), q)
    quartic_count = 0
    full_m_mask = 15 << (4 * g.M)
    for source_dotted in range(2):
        d_source = g.d2(
            g.bar_d(g.delta4(g.S, g.M), g.S, source_dotted, source_vector_momentum),
            g.S,
            source_vector_momentum,
        )
        for output_dotted in range(2):
            result = sp.factor(
                (d_source * b_mark * external_b * g.vector_dotted_component(g.M, output_dotted)).coefficient(full_m_mask)
                / 4
            )
            ledger.zero(f"BD_QUARTIC_srcdot{source_dotted}_outdot{output_dotted}", result)
            quartic_count += 1

    return {
        "TMM": {"symbolic_projection_count": tmm_count, "result": "EXACT_ZERO"},
        "TMH": {
            "symbolic_projection_count": tmh_count,
            "endpoint_representations": ["choice_A", "choice_B"],
            "result": "EXACT_ZERO",
        },
        "matter_quartic": {
            "symbolic_projection_count": quartic_count,
            "two_ordered_vector_placements_share_zero_core": True,
            "result": "EXACT_ZERO",
        },
    }


def prove_bb_diagonal_zero(ledger: Ledger, r0, r1, r2, p, q) -> dict[str, Any]:
    minus_r2 = matrix_neg(r2)
    left_full = g.bar_d2(g.d2(g.delta4(g.S, g.M), g.S, r0), g.S, r0)
    right_full = g.bar_d2(g.d2(g.delta4(g.S, g.H), g.S, minus_r2), g.S, minus_r2)
    left_unmarked = g.d(left_full, g.S, 0, r0)
    left_marked = g.d(left_unmarked, g.S, 1, r0)
    right_unmarked = g.d(right_full, g.S, 0, minus_r2)
    right_marked = g.d(right_unmarked, g.S, 1, minus_r2)
    bridge = g.delta4(g.M, g.H)
    external_left = g.chiral_b_plus(g.M, p)
    external_right = g.chiral_b_plus(g.H, q)

    left_word = g.integrate_two_vertices_bottom_source(
        left_marked * right_unmarked * bridge * external_left * external_right,
        g.M,
        g.H,
    )
    right_word = g.integrate_two_vertices_bottom_source(
        left_unmarked * right_marked * bridge * external_left * external_right,
        g.M,
        g.H,
    )
    ledger.zero("BB_DIAGONAL_TMM_left_mark", left_word)
    ledger.zero("BB_DIAGONAL_TMM_right_mark", right_word)
    ledger.zero("BB_DIAGONAL_TMM_graded_sum", left_word - right_word)

    flavor_rows = []
    for r in range(1, 4):
        left_sum = sum(epsilon3(r, t, u) * int(r == t) for t in range(1, 4) for u in range(1, 4))
        right_sum = sum(epsilon3(r, t, u) * int(r == u) for t in range(1, 4) for u in range(1, 4))
        ledger.zero(f"BB_DIAGONAL_H_flavor_left_r{r}", left_sum)
        ledger.zero(f"BB_DIAGONAL_H_flavor_right_r{r}", right_sum)
        flavor_rows.extend(
            [
                {
                    "r": r,
                    "spectator_match": "delta_rt",
                    "tensor": "epsilon_rtu*delta_rt=epsilon_rru",
                    "value": 0,
                },
                {
                    "r": r,
                    "spectator_match": "delta_ru",
                    "tensor": "epsilon_rtu*delta_ru=epsilon_rtr",
                    "value": 0,
                },
            ]
        )

    return {
        "TMM": {
            "left_marked_projected_word": sp.sstr(sp.factor(left_word)),
            "right_marked_projected_word": sp.sstr(sp.factor(right_word)),
            "graded_leibniz_signs": [1, -1],
            "sum": sp.sstr(sp.factor(left_word - right_word)),
        },
        "H_Yukawa_flavor_rows": flavor_rows,
        "H_Yukawa_result": "EXACT_ZERO_EPSILON_REPEATED_INDEX",
    }


def route_classification(route: dict[str, Any]) -> tuple[str, str]:
    pair_id = route["pair_id"]
    if route["parent_family"] == "SPECTATOR_SOURCE_DOUBLE_BRIDGE":
        return (
            "EXACT_ZERO_1PR_EXCLUDED",
            "source_action_edge_is_cut_edge=true; one_particle_irreducible=false",
        )
    if pair_id in BB_DIAGONAL_PAIRS:
        if route["topology"] != "TMM":
            raise AssertionError(route)
        return (
            "EXACT_ZERO_PROJECTED_DWORD",
            "BB_DIAGONAL_TMM_left_mark=0; right_mark=0; graded signs=(+1,-1)",
        )
    if route["topology"] == "TGM":
        return (
            "EXACT_ZERO_PROJECTED_DWORD",
            "BD_TGM 96/96 symbolic source-dot/output-dot/chirality/permutation/placement projections vanish",
        )
    if route["topology"] == "TMM":
        return (
            "EXACT_ZERO_PROJECTED_DWORD",
            "BD_TMM 4/4 symbolic source-dot/output-dot projections vanish",
        )
    if route["topology"] == "TMH":
        return (
            "EXACT_ZERO_PROJECTED_DWORD",
            "BD_TMH 4/4 symbolic source-dot/endpoint-representation projections vanish",
        )
    raise AssertionError(route)


def build_route_rows(census: dict[str, Any]) -> list[dict[str, Any]]:
    routes = [
        route
        for route in census["legacy_routes"] + census["spectator_routes"]
        if route["pair_id"] in TARGET_PAIRS
    ]
    rows = []
    for ordinal, route in enumerate(routes, start=1):
        classification, certificate = route_classification(route)
        row = {
            "ordinal": ordinal,
            "route_id": route["route_id"],
            "pair_id": route["pair_id"],
            "parent_family": route["parent_family"],
            "topology": route["topology"],
            "marked_occurrences": route["marked_occurrences"],
            "classification": classification,
            "certificate": certificate,
        }
        if route["parent_family"] == "SPLIT_SOURCE_SINGLE_BRIDGE":
            row.update(
                {
                    "left_vertex": route["left_vertex"],
                    "right_vertex": route["right_vertex"],
                    "source_ports": [route["left_source_port"], route["right_source_port"]],
                    "bridge_ports": [route["bridge_left_port"], route["bridge_right_port"]],
                    "external_fields": [route["external_left_field"], route["external_right_field"]],
                }
            )
        else:
            row.update(
                {
                    "source_action_vertex": route["source_action_vertex"],
                    "loop_action_vertex": route["loop_action_vertex"],
                    "spectator_source_side": route["spectator_source_side"],
                    "spectator_external_field": route["spectator_external_field"],
                    "external_output_field": route["external_output_field"],
                    "one_particle_irreducible": route["one_particle_irreducible"],
                    "source_action_edge_is_cut_edge": route["source_action_edge_is_cut_edge"],
                }
            )
        rows.append(row)
    return rows


def build_alternative_rows() -> list[dict[str, Any]]:
    rows = []
    ordinal = 0
    for pair_id in TARGET_PAIRS:
        for sector in ("PURE_GAUGE", "GAUGE_FIXING", "FP_GHOST", "NK_GHOST"):
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": sector,
                    "classification": "EXACT_ABSENT_NO_B_MATTER_SOURCE_PORT",
                    "proof": "B_r source field phi_r requires a tildephi_r port; sector has only u/ghost ports",
                }
            )
        if pair_id in BB_DIAGONAL_PAIRS:
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": "MATTER_QUARTIC",
                    "classification": "EXACT_ABSENT_PORT_MULTIPLICITY",
                    "proof": "two B_r source phi_r legs require two tildephi_r ports; Q_r=(tildephi_r,u,u,phi_r) has one",
                }
            )
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": "SD_JACOBIAN",
                    "classification": "EXACT_ZERO_TYPED_FUNCTIONAL_DERIVATIVE",
                    "proof": "delta B_r/delta tildephi_r=0 in the constrained source coordinates",
                }
            )
        else:
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": "MATTER_QUARTIC",
                    "classification": "EXACT_ZERO_PROJECTED_DWORD",
                    "proof": "BD_QUARTIC 4/4 symbolic source-dot/output-dot projections vanish; both ordered V slots share the zero core",
                }
            )
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": "SD_JACOBIAN",
                    "classification": "EXACT_ZERO_TYPED_FUNCTIONAL_DERIVATIVE",
                    "proof": "delta D_dot/delta tildephi_r=0 because D_dot is a functional of V only",
                }
            )
            ordinal += 1
            rows.append(
                {
                    "ordinal": ordinal,
                    "pair_id": pair_id,
                    "sector": "EULER_POTENTIAL_PLUS_EXPLICIT_POTENTIAL",
                    "classification": "EXACT_ZERO_OPERATOR_PAIR",
                    "proof": "+sqrt(2)*epsilon_rtu(C_t cross C_u)D_dot -sqrt(2)*epsilon_rtu(C_t cross C_u)D_dot=0; reverse order has the common Koszul minus",
                }
            )
    return rows


def validate_route_counts(route_rows: list[dict[str, Any]]) -> dict[str, Any]:
    if len(route_rows) != 399:
        raise AssertionError(f"route count={len(route_rows)}")
    pair_counts = Counter(row["pair_id"] for row in route_rows)
    expected_pair_counts = {**{pair: 5 for pair in BB_DIAGONAL_PAIRS}, **{pair: 32 for pair in BD_PAIRS + DB_PAIRS}}
    if pair_counts != Counter(expected_pair_counts):
        raise AssertionError(pair_counts)
    parent_counts = Counter(row["parent_family"] for row in route_rows)
    if parent_counts != Counter({"SPLIT_SOURCE_SINGLE_BRIDGE": 111, "SPECTATOR_SOURCE_DOUBLE_BRIDGE": 288}):
        raise AssertionError(parent_counts)
    split_topologies = Counter(
        row["topology"] for row in route_rows if row["parent_family"] == "SPLIT_SOURCE_SINGLE_BRIDGE"
    )
    if split_topologies != Counter({"TGM": 72, "TMM": 15, "TMH": 24}):
        raise AssertionError(split_topologies)
    spectator_topologies = Counter(
        row["topology"] for row in route_rows if row["parent_family"] == "SPECTATOR_SOURCE_DOUBLE_BRIDGE"
    )
    if spectator_topologies != Counter({"TGG": 216, "TMM": 54, "THH": 18}):
        raise AssertionError(spectator_topologies)
    classification_counts = Counter(row["classification"] for row in route_rows)
    if classification_counts != Counter({"EXACT_ZERO_1PR_EXCLUDED": 288, "EXACT_ZERO_PROJECTED_DWORD": 111}):
        raise AssertionError(classification_counts)
    return {
        "total": len(route_rows),
        "per_pair": dict(sorted(pair_counts.items())),
        "parent_family": dict(sorted(parent_counts.items())),
        "split_topology": dict(sorted(split_topologies.items())),
        "spectator_topology": dict(sorted(spectator_topologies.items())),
        "classification": dict(sorted(classification_counts.items())),
    }


def build_payload() -> dict[str, Any]:
    if FORBIDDEN_INPUTS.intersection(INPUTS):
        raise AssertionError("forbidden target/result ledger entered inputs")
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    if census.get("external_target_used") is not False:
        raise AssertionError("structural census is not target-blind")

    tgm_stage = run_stage_subprocess("tgm")
    remaining_stage = run_stage_subprocess("remaining")
    bb_stage = run_stage_subprocess("bb")
    tgm = tgm_stage["certificate"]
    remaining = remaining_stage["certificate"]
    bb = bb_stage["certificate"]
    symbolic_checks = tgm_stage["checks"] + remaining_stage["checks"] + bb_stage["checks"]

    route_rows = build_route_rows(census)
    route_counts = validate_route_counts(route_rows)
    alternative_rows = build_alternative_rows()
    if len(alternative_rows) != 102:
        raise AssertionError(len(alternative_rows))

    pair_results = []
    for pair_id in TARGET_PAIRS:
        left, right = pair_id.split("__")
        if pair_id in BB_DIAGONAL_PAIRS:
            transport = {
                "representative": "B1__B1",
                "letter_index": f"flavor pi: B1->B{left[-1]}",
                "marked_signs": ["L:+1", "R:-1"],
                "source_slot_map": "fixed",
                "color_map": "identity; no color tensor survives the zero D-word/flavor factor",
            }
        elif pair_id in BD_PAIRS:
            transport = {
                "representative": "B1__Ddot1",
                "letter_index": f"B1->{left}; Ddot1->{right}",
                "marked_signs": ["L:+1"],
                "source_slot_map": "fixed",
                "color_map": "(A,B,D,E) fixed; each projected word is zero before color contraction",
            }
        else:
            transport = {
                "representative": "Ddot1__B1",
                "letter_index": f"Ddot1->{left}; B1->{right}",
                "marked_signs": ["R:-1"],
                "source_slot_map": "B>D zero rebase (A,B,D,E)->(B,A,E,D)",
                "color_map": "zero is invariant under color-slot rebase; no nonzero coefficient inferred",
            }
        pair_results.append(
            {
                "pair_id": pair_id,
                "result": "0",
                "final_state": "COMPLETE_EXACT_ZERO",
                "transport": transport,
                "split_route_count": 1 if pair_id in BB_DIAGONAL_PAIRS else 9,
                "spectator_route_count": 4 if pair_id in BB_DIAGONAL_PAIRS else 23,
            }
        )

    payload = {
        "schema": "awi.step5.bbdiagonal-bd-db-exact-zero.v1",
        "status": "PASS_BB_DIAGONAL_BD_DB_TARGET_BLIND_EXACT_ZERO",
        "authority_status": "LOCAL_PROPOSAL_FROM_DIRTY_WORKTREE",
        "authority_base": "origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66",
        "external_target_used": False,
        "project_result_ledger_used": False,
        "inputs": [str(path.relative_to(ROOT)) for path in INPUTS],
        "operator_identities": {
            "BB_diagonal": "nabla_-(B_r B_r)=(nabla_-B_r)B_r-B_r(nabla_-B_r)",
            "BD": "nabla_-(B_r D_dot)=(nabla_-B_r)D_dot",
            "DB": "nabla_-(D_dot B_r)=-D_dot(nabla_-B_r)",
            "D_source_projector": "D^2 barD_dot",
            "B_marked_projector": "D_-D_+ barD^2 D^2",
            "cutting_failure_requirement": "a nonzero four-dimensional scalar loop square multiplying the marked inverse kernel",
        },
        "symbolic_dword": {
            "TGM": tgm,
            **remaining,
            "BB_diagonal": bb,
            "check_count": len(symbolic_checks),
            "checks": symbolic_checks,
        },
        "route_counts": route_counts,
        "route_rows": route_rows,
        "alternative_rows": alternative_rows,
        "pair_results": pair_results,
        "summary": {
            "ordered_pairs": len(pair_results),
            "exact_zero_pairs": sum(row["result"] == "0" for row in pair_results),
            "split_routes": route_counts["parent_family"]["SPLIT_SOURCE_SINGLE_BRIDGE"],
            "spectator_routes": route_counts["parent_family"]["SPECTATOR_SOURCE_DOUBLE_BRIDGE"],
            "all_routes": route_counts["total"],
            "symbolic_dword_checks": len(symbolic_checks),
            "alternative_rows": len(alternative_rows),
        },
    }
    validate_payload(payload)
    return payload


def validate_payload(payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    expected = {
        "ordered_pairs": 15,
        "exact_zero_pairs": 15,
        "split_routes": 111,
        "spectator_routes": 288,
        "all_routes": 399,
        "symbolic_dword_checks": 117,
        "alternative_rows": 102,
    }
    if summary != expected:
        raise AssertionError((summary, expected))
    if {row["pair_id"] for row in payload["pair_results"]} != set(TARGET_PAIRS):
        raise AssertionError("pair result set drift")
    if any(row["result"] != "0" or row["final_state"] != "COMPLETE_EXACT_ZERO" for row in payload["pair_results"]):
        raise AssertionError("nonzero/open result entered exact-zero family")
    if any(row["classification"].startswith("OPEN") for row in payload["route_rows"]):
        raise AssertionError("OPEN route entered exact-zero family")
    if payload["external_target_used"] is not False or payload["project_result_ledger_used"] is not False:
        raise AssertionError("target boundary drift")


def run_stage_local(stage: str) -> dict[str, Any]:
    ledger = Ledger()
    r0, r1, r2, p, q = symbolic_momenta()
    if stage == "tgm":
        certificate = prove_bd_tgm_zero(ledger, r0, p, q)
    elif stage == "remaining":
        certificate = prove_bd_tmm_tmh_quartic_zero(ledger, r0, r1, r2, p, q)
    elif stage == "bb":
        certificate = prove_bb_diagonal_zero(ledger, r0, r1, r2, p, q)
    else:
        raise ValueError(stage)
    return {"stage": stage, "certificate": certificate, "checks": ledger.rows}


def run_stage_subprocess(stage: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--stage", stage],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"symbolic stage {stage} failed with {completed.returncode}: {completed.stderr}"
        )
    return json.loads(completed.stdout)


def render_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def compact_ports(row: dict[str, Any]) -> str:
    if row["parent_family"] == "SPLIT_SOURCE_SINGLE_BRIDGE":
        return (
            f"src={row['source_ports']};bridge={row['bridge_ports']};"
            f"ext={row['external_fields']}"
        )
    return (
        f"spectator={row['spectator_source_side']}:{row['spectator_external_field']};"
        f"output={row['external_output_field']};cut_edge={row['source_action_edge_is_cut_edge']}"
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Step 5 diagonal `BB` and `BD/DB` target-blind exact-zero audit",
        "",
        "Status: `PASS_BB_DIAGONAL_BD_DB_TARGET_BLIND_EXACT_ZERO`.",
        "",
        "Authority status: `LOCAL_PROPOSAL_FROM_DIRTY_WORKTREE` on frozen base `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`.",
        "",
        "## 1. Projectors and graded source signs",
        "",
        "$$",
        "\\mathcal P_{D_{\\dot a}}=D^2\\bar D_{\\dot a},",
        "\\qquad",
        "\\mathcal P_{B,\\mathrm{mark}}=D_-D_+\\bar D^2D^2.",
        "$$",
        "",
        "$$",
        "\\nabla_-(B_rB_r)=(\\nabla_-B_r)B_r-B_r(\\nabla_-B_r),",
        "$$",
        "",
        "$$",
        "\\nabla_-(B_rD_{\\dot a})=(\\nabla_-B_r)D_{\\dot a},",
        "\\qquad",
        "\\nabla_-(D_{\\dot a}B_r)=-D_{\\dot a}(\\nabla_-B_r).",
        "$$",
        "",
        "A DRED cutting remainder requires a nonzero four-dimensional scalar loop square on a marked inverse kernel. The symbolic projected words below vanish before color contraction; therefore no `bar(r)^2-r_d^2` remainder exists.",
        "",
        "## 2. Diagonal `BB`",
        "",
        "The unique split-source route for each flavor is `TMM`. Its two marked words are",
        "",
        "$$",
        "K_L=\\int d^8z_Ld^8z_R",
        "[D_-D_+\\bar D^2D^2\\delta_{SL}]",
        "[D_+\\bar D^2D^2\\delta_{SR}]",
        "\\delta_{LR}B_r(L)B_r(R)=0,",
        "$$",
        "",
        "$$",
        "K_R=\\int d^8z_Ld^8z_R",
        "[D_+\\bar D^2D^2\\delta_{SL}]",
        "[D_-D_+\\bar D^2D^2\\delta_{SR}]",
        "\\delta_{LR}B_r(L)B_r(R)=0,",
        "$$",
        "",
        "$$",
        "K_L-K_R=0.",
        "$$",
        "",
        "For every possible `Hminus`/Yukawa attachment of the spectator `B_r`, the propagator flavor delta forces one potential flavor to equal `r`:",
        "",
        "$$",
        "\\epsilon_{rtu}\\delta_{rt}=\\epsilon_{rru}=0,",
        "\\qquad",
        "\\epsilon_{rtu}\\delta_{ru}=\\epsilon_{rtr}=0.",
        "$$",
        "",
        "A matter quartic has ports `(tildephi_r,u,u,phi_r)` and cannot absorb two `B_r` source legs. Pure gauge, gauge-fixing, FP and NK vertices have no `tildephi_r` port. All twelve spectator parents are 1PR.",
        "",
        "## 3. `BD/DB`",
        "",
        "The exact symbolic sparse-Grassmann replay gives",
        "",
        "$$",
        "K_{TGM}^{\\dot a\\dot b}(\\mathrm{chirality},\\pi,\\mathrm{placement})=0",
        "$$",
        "",
        "for `2*2*2*6*2=96` source-dot/output-dot/chirality/gauge-permutation/derivative-placement words, and",
        "",
        "$$",
        "K_{TMM}^{\\dot a\\dot b}=0\\quad(4/4),",
        "\\qquad",
        "K_{TMH}^{\\dot a}(A)=K_{TMH}^{\\dot a}(B)=0\\quad(4/4),",
        "$$",
        "",
        "$$",
        "K_{M^{(2)}}^{\\dot a\\dot b}=0\\quad(4/4).",
        "$$",
        "",
        "The Euler-potential and explicit-potential occurrences cancel before integration:",
        "",
        "$$",
        "+\\sqrt2\\epsilon_{rtu}(C_t\\times C_u)D_{\\dot a}",
        "-\\sqrt2\\epsilon_{rtu}(C_t\\times C_u)D_{\\dot a}=0.",
        "$$",
        "",
        "For reverse order both terms carry the common Leibniz sign `-1`. The regulated Schwinger Jacobian is independently zero:",
        "",
        "$$",
        "\\frac{\\vec\\delta D_{\\dot a}^B}{\\delta\\widetilde\\Phi_r^A}=0,",
        "$$",
        "",
        "because `D_dot` is a functional of `V` only. All 276 `BD/DB` spectator parents are 1PR.",
        "",
        "## 4. Pair results",
        "",
        "| pair | source mark/Koszul | split | spectator | result |",
        "|---|---|---:|---:|---|",
    ]
    for row in payload["pair_results"]:
        signs = ",".join(row["transport"]["marked_signs"])
        lines.append(
            f"| `{row['pair_id']}` | `{signs}` | {row['split_route_count']} | {row['spectator_route_count']} | `0` |"
        )
    lines.extend(
        [
            "",
            "## 5. All typed parent routes",
            "",
            "| # | route | pair | family/topology | mark | ports | classification |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for row in payload["route_rows"]:
        marks = ",".join(f"{mark[0]}:{mark[2]:+d}" for mark in row["marked_occurrences"])
        lines.append(
            f"| {row['ordinal']:03d} | `{row['route_id']}` | `{row['pair_id']}` | "
            f"`{row['parent_family']}/{row['topology']}` | `{marks}` | `{compact_ports(row)}` | "
            f"`{row['classification']}` |"
        )
    lines.extend(
        [
            "",
            "## 6. Counts",
            "",
            "$$",
            "399=111_{\\mathrm{split}}+288_{\\mathrm{spectator}},",
            "$$",
            "",
            "$$",
            "111=72_{TGM}+15_{TMM}+24_{TMH}.",
            "$$",
            "",
            "$$",
            "15=3_{BB\\,\\mathrm{diag}}+6_{BD}+6_{DB},",
            "\\qquad",
            "\\Gamma_{\\mathrm{ev}}=0\\quad\\text{for all fifteen pairs}.",
            "$$",
            "",
            "Verification:",
            "",
            "```text",
            "python scripts/step5_bbdiagonal_bd_db_exact_zero_audit.py --check",
            "python -m unittest tests.test_step5_bbdiagonal_bd_db_exact_zero",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_artifacts(payload: dict[str, Any]) -> None:
    OUTPUT_JSON.write_text(render_json(payload), encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def check_artifacts(payload: dict[str, Any]) -> None:
    if not OUTPUT_JSON.is_file() or OUTPUT_JSON.read_text(encoding="utf-8") != render_json(payload):
        raise SystemExit(f"FAIL stale {OUTPUT_JSON.relative_to(ROOT)}")
    if not OUTPUT_MD.is_file() or OUTPUT_MD.read_text(encoding="utf-8") != render_markdown(payload):
        raise SystemExit(f"FAIL stale {OUTPUT_MD.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--stage", choices=("tgm", "remaining", "bb"))
    args = parser.parse_args()

    if args.stage:
        print(json.dumps(run_stage_local(args.stage), sort_keys=True))
        return 0

    payload = build_payload()
    if args.write:
        write_artifacts(payload)
    else:
        check_artifacts(payload)

    summary = payload["summary"]
    print(f"PASS ordered_pairs={summary['ordered_pairs']}")
    print(f"PASS exact_zero_pairs={summary['exact_zero_pairs']}")
    print(f"PASS split_routes={summary['split_routes']}")
    print(f"PASS spectator_routes={summary['spectator_routes']}")
    print(f"PASS all_routes={summary['all_routes']}")
    print(f"PASS symbolic_dword_checks={summary['symbolic_dword_checks']}")
    print(f"PASS alternative_rows={summary['alternative_rows']}")
    print("PASS external_target_used=false")
    print("PASS project_result_ledger_used=false")
    print(payload["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
