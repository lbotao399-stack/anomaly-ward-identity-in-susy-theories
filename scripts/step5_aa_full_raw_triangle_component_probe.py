#!/usr/bin/env python3
"""Exact component probe of the full polarized AA gauge triangle.

This probe deliberately keeps the gauge-action chirality independent of the
external component and evaluates the complete cubic functional derivative.
It is a numerator probe only; graph normalization and DRED edge cuts are
settled in the companion audit after the full loop polynomial is known.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import multiprocessing
import os
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_gauge_full_source_sd_orbit_exact_audit as aa  # noqa: E402


def action_hessian_sector_task(args):
    (
        sector,
        momentum_1,
        momentum_2,
        background_momentum,
        background_type,
        polarization,
        dotted,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
        external_d,
        external_a,
    ) = args
    ctx = aa.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        aa.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        aa.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        (
            aa.endpoint_A(ctx, "X", 2, external_a, polarization)
            if background_type == "A"
            else aa.endpoint_D(ctx, "X", 2, external_d, dotted, eta_index=4)
        ),
    ]
    action = aa.gauge_action_integrand(aa.sum_mats(fields), "X", sector)
    action = action.coefficient_labels((1, 1, 1))
    action = (
        aa.integrate_chiral(action, "X")
        if sector == "+"
        else aa.integrate_antichiral(action, "X")
    )
    value = action.grass_coefficient(
        aa.hessian_marker_mask(
            theta_mask_1,
            theta_mask_2,
            background_type == "D",
        )
    )
    return (
        sector,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
        value,
    )


def fixed_field_strength_hessian_task(args):
    (
        sector,
        momentum_1,
        momentum_2,
        background_momentum,
        background_type,
        polarization,
        dotted,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
        external_d,
        external_a,
    ) = args
    if (sector, background_type) not in (("+", "A"), ("-", "D")):
        return sector, color_1, color_2, theta_mask_1, theta_mask_2, aa.ZERO
    ctx = aa.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    quantum = aa.sum_mats(
        [
            aa.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
            aa.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        ]
    )
    background = (
        aa.endpoint_A(ctx, "X", 2, external_a, polarization)
        if background_type == "A"
        else aa.endpoint_D(ctx, "X", 2, external_d, dotted, eta_index=4)
    )
    if sector == "+":
        strength_lower = tuple(
            aa.mat_scale(
                -aa.SQRT2 / Fraction(8),
                aa.mat_bar_d2(aa.mat_d(background, "X", index), "X"),
            )
            for index in range(2)
        )
        strength_upper = (strength_lower[1], aa.mat_neg(strength_lower[0]))
        commutator_lower = []
        for index in range(2):
            derivative = aa.mat_d(quantum, "X", index)
            commutator_lower.append(
                aa.mat_sub(
                    aa.mat_mul(derivative, quantum),
                    aa.mat_mul(quantum, derivative),
                )
            )
        integrand = Fraction(-1, 4) * aa.mat_trace(
            aa.mat_add(
                aa.mat_mul(strength_upper[0], commutator_lower[0]),
                aa.mat_mul(strength_upper[1], commutator_lower[1]),
            )
        )
    else:
        strength_lower = tuple(
            aa.mat_scale(
                -aa.SQRT2 / Fraction(8),
                aa.mat_d2(aa.mat_bar_d(background, "X", index), "X"),
            )
            for index in range(2)
        )
        commutator_lower = []
        for index in range(2):
            derivative = aa.mat_bar_d(quantum, "X", index)
            commutator_lower.append(
                aa.mat_sub(
                    aa.mat_mul(derivative, quantum),
                    aa.mat_mul(quantum, derivative),
                )
            )
        commutator_upper = (commutator_lower[1], aa.mat_neg(commutator_lower[0]))
        integrand = Fraction(1, 4) * aa.mat_trace(
            aa.mat_add(
                aa.mat_mul(strength_lower[0], commutator_upper[0]),
                aa.mat_mul(strength_lower[1], commutator_upper[1]),
            )
        )
    integrand = integrand.coefficient_labels((1, 1, 1))
    integrand = Fraction(1, 16) * aa.d2(aa.bar_d2(integrand, "X"), "X")
    integrand = integrand.set_coordinates_zero("X")
    value = integrand.grass_coefficient(
        aa.hessian_marker_mask(
            theta_mask_1,
            theta_mask_2,
            background_type == "D",
        )
    )
    return sector, color_1, color_2, theta_mask_1, theta_mask_2, value


def source_hessian_task(args):
    momentum_1, momentum_2, color_1, color_2, mask_1, mask_2 = args
    full_entries = aa.source_I0_hessian_entries(
        momentum_1,
        momentum_2,
        color_1,
        color_2,
        mask_1,
        mask_2,
    )
    ctx = aa.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
        ),
        6,
    )
    fields = [
        aa.basis_endpoint(ctx, "X", 0, color_1, mask_1, 5),
        aa.basis_endpoint(ctx, "X", 1, color_2, mask_2, 6),
    ]
    quantum = aa.sum_mats(fields)
    a1 = aa.canonical_A_words(quantum, "X")[0]
    full_n0 = aa.mat_d(a1, "X", 1)
    longitudinal_n0 = aa.mat_scale(
        aa.SQRT2 / Fraction(16),
        aa.mat_d(
            aa.mat_bar_d2(aa.mat_d2(quantum, "X"), "X"),
            "X",
            0,
        ),
    )
    selected_n0 = aa.mat_sub(full_n0, longitudinal_n0)

    def entries_for(n0):
        words = {
            "I0_DminusA1[A]*A1[B]": aa.component(n0, 0) * aa.component(a1, 1),
            "I0_A1[A]*DminusA1[B]": aa.component(a1, 0) * aa.component(n0, 1),
        }
        marker = aa.hessian_marker_mask(mask_1, mask_2, False)
        result = {}
        for tag, word in words.items():
            value = (
                word.coefficient_labels((1, 1))
                .set_coordinates_zero("X")
                .grass_coefficient(marker)
            )
            if value:
                result[tag] = value
        return result

    selected_entries = entries_for(selected_n0)
    longitudinal_entries = entries_for(longitudinal_n0)
    for tag in set(full_entries) | set(selected_entries) | set(longitudinal_entries):
        if full_entries.get(tag, aa.ZERO) != (
            selected_entries.get(tag, aa.ZERO)
            + longitudinal_entries.get(tag, aa.ZERO)
        ):
            raise AssertionError((tag, color_1, color_2, mask_1, mask_2))
    return (
        color_1,
        color_2,
        mask_1,
        mask_2,
        full_entries,
        selected_entries,
        longitudinal_entries,
    )


def parallel_map(function, tasks, workers):
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers,
        mp_context=context,
    ) as executor:
        return tuple(executor.map(function, tasks, chunksize=8))


def action_table(
    momentum_1,
    momentum_2,
    background_momentum,
    background_type,
    polarization,
    dotted,
    workers,
    *,
    fixed_field_strength=False,
):
    tasks = (
        (
            sector,
            momentum_1,
            momentum_2,
            background_momentum,
            background_type,
            polarization,
            dotted,
            color_1,
            color_2,
            mask_1,
            mask_2,
            1,
            0,
        )
        for sector, color_1, color_2, mask_1, mask_2 in itertools.product(
            ("+", "-"), range(3), range(3), range(16), range(16)
        )
    )
    table = {}
    task_function = (
        fixed_field_strength_hessian_task
        if fixed_field_strength
        else action_hessian_sector_task
    )
    for sector, color_1, color_2, mask_1, mask_2, value in parallel_map(
        task_function,
        tasks,
        workers,
    ):
        if value:
            table[sector, color_1, color_2, mask_1, mask_2] = value
    return table


def source_table(momentum_1, momentum_2, workers):
    tasks = (
        (momentum_1, momentum_2, color_1, color_2, mask_1, mask_2)
        for color_1, color_2, mask_1, mask_2 in itertools.product(
            range(3), range(3), range(16), range(16)
        )
    )
    tables = {mode: {} for mode in ("full", "selected", "longitudinal")}
    tagged_tables = {mode: {} for mode in tables}
    for (
        color_1,
        color_2,
        mask_1,
        mask_2,
        full_entries,
        selected_entries,
        longitudinal_entries,
    ) in parallel_map(
        source_hessian_task,
        tasks,
        workers,
    ):
        for mode, entries in (
            ("full", full_entries),
            ("selected", selected_entries),
            ("longitudinal", longitudinal_entries),
        ):
            value = sum(entries.values(), aa.ZERO)
            if value:
                tables[mode][color_1, color_2, mask_1, mask_2] = value
            for tag, tag_value in entries.items():
                if tag_value:
                    tagged_tables[mode][
                        tag,
                        color_1,
                        color_2,
                        mask_1,
                        mask_2,
                    ] = tag_value
    return tables, tagged_tables


def contract_triangle(source, action_d, action_a, source_tagged=None):
    totals = {(left, right): aa.ZERO for left in ("+", "-") for right in ("+", "-")}
    nonzero_products = {key: 0 for key in totals}
    tagged_totals = {}
    for color_0, color_1, color_2 in itertools.product(range(3), repeat=3):
        for source_mask_0, source_mask_2, middle_mask_d in itertools.product(
            range(16), repeat=3
        ):
            source_value = source.get(
                (color_0, color_2, source_mask_0, source_mask_2),
                aa.ZERO,
            )
            if not source_value:
                continue
            action_mask_0 = 15 ^ source_mask_0
            action_mask_a1 = 15 ^ middle_mask_d
            action_mask_2 = 15 ^ source_mask_2
            covariance_0 = aa.component_covariance(source_mask_0, action_mask_0)
            covariance_1 = aa.component_covariance(middle_mask_d, action_mask_a1)
            covariance_2 = aa.component_covariance(source_mask_2, action_mask_2)
            if not covariance_0 or not covariance_1 or not covariance_2:
                continue
            wick_sign = -1 if (
                source_mask_0.bit_count() * source_mask_2.bit_count()
            ) % 2 else 1
            edge_weight = 8 * covariance_0 * covariance_1 * covariance_2
            for sector_d, sector_a in totals:
                value_d = action_d.get(
                    (sector_d, color_0, color_1, action_mask_0, middle_mask_d),
                    aa.ZERO,
                )
                if not value_d:
                    continue
                value_a = action_a.get(
                    (sector_a, color_1, color_2, action_mask_a1, action_mask_2),
                    aa.ZERO,
                )
                if not value_a:
                    continue
                totals[sector_d, sector_a] += (
                    wick_sign
                    * edge_weight
                    * source_value
                    * value_d
                    * value_a
                )
                nonzero_products[sector_d, sector_a] += 1
                if source_tagged is not None:
                    for source_tag in (
                        "I0_DminusA1[A]*A1[B]",
                        "I0_A1[A]*DminusA1[B]",
                    ):
                        tagged_source_value = source_tagged.get(
                            (
                                source_tag,
                                color_0,
                                color_2,
                                source_mask_0,
                                source_mask_2,
                            ),
                            aa.ZERO,
                        )
                        if not tagged_source_value:
                            continue
                        tagged_key = source_tag, sector_d, sector_a
                        tagged_totals[tagged_key] = tagged_totals.get(
                            tagged_key,
                            aa.ZERO,
                        ) + (
                            wick_sign
                            * edge_weight
                            * tagged_source_value
                            * value_d
                            * value_a
                        )
    return totals, nonzero_products, tagged_totals


def triangle_numerator(
    loop,
    workers,
    compare_fixed=False,
    *,
    p=None,
    q=None,
    polarization=None,
    dotted=0,
):
    p = aa.vec((1, 0, 0, 0)) if p is None else p
    q = aa.vec((0, 1, 0, 0)) if q is None else q
    polarization = (
        aa.vec((0, 0, 0, 1)) if polarization is None else polarization
    )
    r0 = loop
    r1 = aa.vadd(loop, aa.vneg(q))
    r2 = aa.vadd(loop, aa.vneg(aa.vadd(p, q)))

    source_tables, source_tagged_tables = source_table(r0, aa.vneg(r2), workers)
    source = source_tables["full"]
    source_tagged = source_tagged_tables["full"]
    action_d = action_table(
        aa.vneg(r0),
        r1,
        q,
        "D",
        polarization,
        dotted,
        workers,
    )
    action_a = action_table(
        aa.vneg(r1),
        r2,
        p,
        "A",
        polarization,
        dotted,
        workers,
    )

    totals, nonzero_products, tagged_totals = contract_triangle(
        source,
        action_d,
        action_a,
        source_tagged,
    )
    norm_a, norm_d = aa.external_normalizations_pair(
        p,
        q,
        polarization,
        dotted,
        0,
        1,
    )
    color = aa.A(aa.su2_F(0, 1, 1, 0))
    normalized = {
        key: value / (norm_a * norm_d * color)
        for key, value in totals.items()
    }
    result = {
        "full": normalized,
        "full_products": nonzero_products,
        "full_source_tags": {
            key: value / (norm_a * norm_d * color)
            for key, value in tagged_totals.items()
        },
    }
    for mode in ("selected", "longitudinal"):
        mode_totals, mode_products, mode_tagged_totals = contract_triangle(
            source_tables[mode],
            action_d,
            action_a,
            source_tagged_tables[mode],
        )
        result[mode] = {
            key: value / (norm_a * norm_d * color)
            for key, value in mode_totals.items()
        }
        result[f"{mode}_products"] = mode_products
        result[f"{mode}_source_tags"] = {
            key: value / (norm_a * norm_d * color)
            for key, value in mode_tagged_totals.items()
        }
    table_sizes = {
        "source": len(source),
        "action_d": len(action_d),
        "action_a": len(action_a),
    }
    if compare_fixed:
        fixed_d = action_table(
            aa.vneg(r0), r1, q, "D", polarization, dotted, workers,
            fixed_field_strength=True,
        )
        fixed_a = action_table(
            aa.vneg(r1), r2, p, "A", polarization, dotted, workers,
            fixed_field_strength=True,
        )
        fixed_totals, fixed_products, fixed_tagged_totals = contract_triangle(
            source,
            fixed_d,
            fixed_a,
            source_tagged,
        )
        result["fixed"] = {
            key: value / (norm_a * norm_d * color)
            for key, value in fixed_totals.items()
        }
        result["fixed_products"] = fixed_products
        result["fixed_source_tags"] = {
            key: value / (norm_a * norm_d * color)
            for key, value in fixed_tagged_totals.items()
        }
        table_sizes["fixed_d"] = len(fixed_d)
        table_sizes["fixed_a"] = len(fixed_a)
    return result, table_sizes


def parse_loop(text):
    values = tuple(Fraction(piece) for piece in text.split(","))
    if len(values) != 4:
        raise argparse.ArgumentTypeError("loop must have four comma-separated rationals")
    return aa.vec(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--loop", type=parse_loop, default=aa.ZERO_VECTOR)
    parser.add_argument("--p", type=parse_loop, default=aa.vec((1, 0, 0, 0)))
    parser.add_argument("--q", type=parse_loop, default=aa.vec((0, 1, 0, 0)))
    parser.add_argument(
        "--polarization",
        type=parse_loop,
        default=aa.vec((0, 0, 0, 1)),
    )
    parser.add_argument("--dotted", type=int, choices=(0, 1), default=0)
    parser.add_argument("--workers", type=int, default=max(1, min(12, os.cpu_count() or 1)))
    parser.add_argument("--compare-fixed", action="store_true")
    args = parser.parse_args()
    result, table_sizes = triangle_numerator(
        args.loop,
        args.workers,
        args.compare_fixed,
        p=args.p,
        q=args.q,
        polarization=args.polarization,
        dotted=args.dotted,
    )
    print("loop", *(value.text() for value in args.loop))
    print("table_sizes", table_sizes)
    for family in ("full", "selected", "longitudinal", "fixed"):
        if family not in result:
            continue
        products = result[f"{family}_products"]
        for key in (("+", "+"), ("+", "-"), ("-", "+"), ("-", "-")):
            print(
                f"{family} {key[0]}{key[1]} numerator "
                f"{result[family][key].text()} products {products[key]}"
            )
        for source_tag in (
            "I0_DminusA1[A]*A1[B]",
            "I0_A1[A]*DminusA1[B]",
        ):
            key = source_tag, "-", "+"
            value = result[f"{family}_source_tags"].get(key, aa.ZERO)
            print(f"{family} source_tag {source_tag} -+ {value.text()}")


if __name__ == "__main__":
    main()
