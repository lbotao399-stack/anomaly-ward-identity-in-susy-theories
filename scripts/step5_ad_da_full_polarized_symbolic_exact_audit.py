#!/usr/bin/env python3
"""Exact polynomial AD/DA replay with the full cubic gauge Hessian.

Both external prepotential directions are ``D`` components.  Each cubic
functional Hessian is generated from the complete chiral or antichiral gauge
action, so the external direction is allowed in every ``W``, derivative, and
commutator slot.  The four chirality products are retained separately.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_full_polarized_symbolic_exact_audit as poly  # noqa: E402
import step5_ad_da_ordered_ports_crossed_hessian_exact_audit as audit  # noqa: E402


alg = audit.alg


def expr(value: poly.PolyA) -> sp.Expr:
    return sp.expand(value.as_expr())


def text(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value))


def plus_dotted(momentum: tuple[poly.PolyA, ...], dotted: int) -> poly.PolyA:
    if dotted == 0:
        return momentum[3] - alg.I * momentum[2]
    if dotted == 1:
        return -momentum[1] - alg.I * momentum[0]
    raise ValueError(dotted)


def loop_coefficient(value: poly.PolyA, loop: tuple[poly.PolyA, ...]) -> tuple[sp.Expr, sp.Expr]:
    variables = sp.symbols("l0:4")
    value_expr = expr(value)
    loop_plus = expr(plus_dotted(loop, 0))
    ratios: list[sp.Expr] = []
    for variable in variables:
        denominator = sp.expand(loop_plus).coeff(variable)
        numerator = sp.expand(value_expr).coeff(variable)
        if denominator != 0:
            ratios.append(sp.simplify(numerator / denominator))
        elif numerator != 0:
            raise AssertionError(("non-plus loop component", variable, numerator))
    if not ratios or any(sp.simplify(item - ratios[0]) != 0 for item in ratios[1:]):
        raise AssertionError(("not rank-one plus", value_expr, loop_plus, ratios))
    coefficient = ratios[0]
    constant = sp.expand(value_expr - coefficient * loop_plus)
    if any(sp.expand(constant).coeff(variable) != 0 for variable in variables):
        raise AssertionError(("loop remainder", constant))
    return sp.simplify(coefficient), constant


def contract_all_modes(
    pair: str,
    allocation: str,
    loop: tuple[poly.PolyA, ...],
    p: tuple[poly.PolyA, ...],
    q: tuple[poly.PolyA, ...],
    tables: dict[str, dict[tuple[str, int, int, int, int, int], poly.PolyA]],
) -> dict[str, dict[tuple[str, str], poly.PolyA]]:
    """Contract all marked-operator sectors through one shared Wick kernel."""

    modes = ("evanescent", "selected", "longitudinal", "gauge_fixing", "full")
    r0 = loop
    r2 = alg.vadd(loop, p, q)
    direct = allocation == "direct"
    if allocation not in {"direct", "crossed"}:
        raise ValueError(allocation)
    source_momenta = (alg.vneg(r0), r2) if direct else (r2, alg.vneg(r0))
    source_tables: dict[str, dict[tuple[int, int], poly.PolyA]] = {
        mode: {} for mode in modes
    }
    for source_left_mask, source_right_mask in itertools.product(range(16), repeat=2):
        for mode in modes:
            if mode == "gauge_fixing":
                value = audit.raw.gauge_fixing_source_component_entry(
                    pair,
                    *source_momenta,
                    source_left_mask,
                    source_right_mask,
                    0,
                    0,
                    1,
                )
            else:
                value = audit.raw.source_component_entry(
                    pair,
                    *source_momenta,
                    source_left_mask,
                    source_right_mask,
                    0,
                    0,
                    1,
                    mode,
                )
            if value:
                source_tables[mode][source_left_mask, source_right_mask] = value

    totals = {
        mode: {
            (left, right): alg.ZERO
            for left in ("+", "-")
            for right in ("+", "-")
        }
        for mode in modes
    }
    support = set().union(*(set(table) for table in source_tables.values()))
    left_source_index = 0 if direct else 1
    right_source_index = 1 if direct else 0
    left_source_color = 0 if direct else 1
    right_source_color = 1 if direct else 0
    left_external_color = 1 if direct else 0
    right_external_color = 0 if direct else 1
    for source_left_mask, source_right_mask in support:
        source_masks = (source_left_mask, source_right_mask)
        left_source_mask = 15 ^ source_masks[left_source_index]
        right_source_mask = 15 ^ source_masks[right_source_index]
        cov_left = alg.component_covariance(
            source_masks[left_source_index], left_source_mask
        )
        cov_right = alg.component_covariance(
            source_masks[right_source_index], right_source_mask
        )
        if not cov_left or not cov_right:
            continue
        for left_bridge_mask in range(16):
            right_bridge_mask = 15 ^ left_bridge_mask
            cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
            if not cov_bridge:
                continue
            parities = (
                source_left_mask.bit_count() % 2,
                source_right_mask.bit_count() % 2,
                left_source_mask.bit_count() % 2,
                left_bridge_mask.bit_count() % 2,
                1,
                right_source_mask.bit_count() % 2,
                right_bridge_mask.bit_count() % 2,
                1,
            )
            pairs = (
                ((0, 2), (1, 5), (3, 6))
                if direct
                else ((0, 5), (1, 2), (3, 6))
            )
            wick = audit.raw.wick_pair_sign(parities, pairs)
            edge = -8 * cov_left * cov_right * cov_bridge
            action_kernel: dict[tuple[str, str], poly.PolyA] = {}
            for left_sector, right_sector in itertools.product(("+", "-"), repeat=2):
                value = alg.ZERO
                for bridge_color in range(3):
                    left = tables["left"].get(
                        (
                            left_sector,
                            left_external_color,
                            left_source_color,
                            bridge_color,
                            left_source_mask,
                            left_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    right = tables["right"].get(
                        (
                            right_sector,
                            right_external_color,
                            right_source_color,
                            bridge_color,
                            right_source_mask,
                            right_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    value += left * right
                action_kernel[left_sector, right_sector] = value
            for mode in modes:
                source = source_tables[mode].get(
                    (source_left_mask, source_right_mask), alg.ZERO
                )
                if not source:
                    continue
                for chirality, value in action_kernel.items():
                    totals[mode][chirality] += wick * edge * source * value
    return totals


def build(frame: str, workers: int) -> dict[str, object]:
    loop = poly.install_polynomial_scalar()
    if frame == "p_only":
        p = alg.vec((0, 0, 0, 1))
        q = alg.vec((1, 0, 0, 0))
    elif frame == "q_only":
        p = alg.vec((1, 0, 0, 0))
        q = alg.vec((0, 0, 0, 1))
    else:
        raise ValueError(frame)

    p_plus = expr(plus_dotted(p, 0))
    q_plus = expr(plus_dotted(q, 0))
    if frame == "p_only":
        if p_plus == 0 or q_plus != 0:
            raise AssertionError((p_plus, q_plus))
        isolate = p_plus
    else:
        if p_plus != 0 or q_plus == 0:
            raise AssertionError((p_plus, q_plus))
        isolate = q_plus

    tables = audit._full_cubic_hessian_tables(loop, p, q, workers)
    r0_square = alg.vdot(loop, loop)
    r2 = alg.vadd(loop, p, q)
    r2_square = alg.vdot(r2, r2)
    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    for pair_id, pair in (("AD", "A__Ddot1"), ("DA", "Ddot1__A")):
        rows[pair_id] = {}
        for allocation in ("direct", "crossed"):
            edge = (
                "e0"
                if (pair_id, allocation) in (("AD", "direct"), ("DA", "crossed"))
                else "e2"
            )
            basis = (
                "R1"
                if (pair_id, allocation) in (("AD", "direct"), ("DA", "crossed"))
                else "R2"
            )
            expected_evanescent = (
                alg.I
                * (
                    plus_dotted(loop, 0)
                    + plus_dotted(p, 0)
                    + plus_dotted(q, 0) / 2
                )
                / 16
                if basis == "R1"
                else -alg.I * plus_dotted(loop, 0) / 16
            )
            edge_square = r0_square if edge == "e0" else r2_square
            sectors = contract_all_modes(
                pair,
                allocation,
                loop,
                p,
                q,
                tables,
            )
            sector_rows: dict[str, object] = {}
            for chirality in (("+", "+"), ("+", "-"), ("-", "+"), ("-", "-")):
                tag = "".join(chirality)
                evanescent = sectors["evanescent"][chirality]
                selected = sectors["selected"][chirality]
                longitudinal = sectors["longitudinal"][chirality]
                gauge_fixing = sectors["gauge_fixing"][chirality]
                full = sectors["full"][chirality]
                prefix = f"{pair_id}_{allocation}_{tag}"
                checks[f"{prefix}_{basis}_polynomial"] = (
                    evanescent == expected_evanescent
                )
                checks[f"{prefix}_selected_edge_divisibility"] = (
                    selected == edge_square * evanescent
                )
                checks[f"{prefix}_full_selected_longitudinal"] = (
                    full == selected + longitudinal
                )
                checks[f"{prefix}_longitudinal_gf"] = (
                    longitudinal + gauge_fixing == alg.ZERO
                )
                checks[f"{prefix}_full_gf_selected"] = (
                    full + gauge_fixing == selected
                )
                ell_coefficient, constant = loop_coefficient(evanescent, loop)
                external_coefficient = sp.simplify(constant / isolate)
                checks[f"{prefix}_external_isolate_exact"] = sp.simplify(
                    constant - external_coefficient * isolate
                ) == 0
                sector_rows[tag] = {
                    "evanescent_quotient": text(expr(evanescent)),
                    "selected_kinetic": text(expr(selected)),
                    "source_longitudinal": text(expr(longitudinal)),
                    "gauge_fixing": text(expr(gauge_fixing)),
                    "full_source": text(expr(full)),
                    "rank_one": {
                        "ell_plus": text(ell_coefficient),
                        f"{frame.removesuffix('_only')}_raw_plus": text(
                            external_coefficient
                        ),
                    },
                }
            total_evanescent = sum(
                sectors["evanescent"].values(), alg.ZERO
            )
            total_selected = sum(sectors["selected"].values(), alg.ZERO)
            total_longitudinal = sum(
                sectors["longitudinal"].values(), alg.ZERO
            )
            total_gf = sum(sectors["gauge_fixing"].values(), alg.ZERO)
            total_full = sum(sectors["full"].values(), alg.ZERO)
            total_ell, total_constant = loop_coefficient(total_evanescent, loop)
            total_external = sp.simplify(total_constant / isolate)
            prefix = f"{pair_id}_{allocation}_TOTAL"
            checks[f"{prefix}_four_times_{basis}"] = (
                total_evanescent == 4 * expected_evanescent
            )
            checks[f"{prefix}_selected_edge_divisibility"] = (
                total_selected == edge_square * total_evanescent
            )
            checks[f"{prefix}_longitudinal_gf"] = (
                total_longitudinal + total_gf == alg.ZERO
            )
            checks[f"{prefix}_full_gf_selected"] = (
                total_full + total_gf == total_selected
            )
            rows[pair_id][allocation] = {
                "marked_edge": edge,
                "evanescent_basis": basis,
                "chirality_sectors": sector_rows,
                "four_sector_sum": {
                    "evanescent_quotient": text(expr(total_evanescent)),
                    "rank_one": {
                        "ell_plus": text(total_ell),
                        f"{frame.removesuffix('_only')}_raw_plus": text(
                            total_external
                        ),
                    },
                    "selected_kinetic": text(expr(total_selected)),
                    "source_longitudinal": text(expr(total_longitudinal)),
                    "gauge_fixing": text(expr(total_gf)),
                    "full_source": text(expr(total_full)),
                },
            }

    return {
        "schema": "step5-ad-da-full-polarized-symbolic-exact-v1",
        "external_target_used": False,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "frame": frame,
        "routing": {
            "r0": "ell",
            "r1": "ell+p_raw",
            "r2": "ell+p_raw+q_raw",
            "p_raw": [text(expr(component)) for component in p],
            "q_raw": [text(expr(component)) for component in q],
            "p_raw_plus": text(p_plus),
            "q_raw_plus": text(q_plus),
        },
        "action_table_sizes": {
            vertex: len(table) for vertex, table in tables.items()
        },
        "rows": rows,
        "checks": {
            "count": len(checks),
            "passed": sum(checks.values()),
            "failed": sum(not value for value in checks.values()),
            "rows": checks,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frame", choices=("p_only", "q_only"), required=True)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build(args.frame, args.workers)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
