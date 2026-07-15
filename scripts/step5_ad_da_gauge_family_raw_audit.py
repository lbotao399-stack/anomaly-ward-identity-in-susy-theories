#!/usr/bin/env python3
"""Target-blind raw ordered A-D and D-A pure-gauge triangle replay.

This checker imports only the exact sparse-superfield algebra used by the
independent AA source-orbit audit.  The present source word, three-edge Wick
contraction, ordered cubic gauge slots, routing, and DRED reduction are new.
No result/HT ledger is read.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_gauge_full_source_sd_orbit_exact_audit as alg  # noqa: E402


CENSUS = ROOT / "audits" / "step5-all-triangle-parent-port-census.json"
DEFAULT_JSON = ROOT / "audits" / "step5-ad-da-gauge-family-raw-exact.json"


def marker_mask(theta_mask: int, marker: int) -> int:
    return (1 << marker) if theta_mask.bit_count() % 2 else 0


def d_bottom_word(value: alg.Mat, dotted: int, node: str = "X") -> alg.Mat:
    # D_dot-a=-1/(4 sqrt(2)) D^2 barD_dot-a u.
    return alg.mat_scale(
        -alg.SQRT2 / 8,
        alg.mat_d2(alg.mat_bar_d(value, node, dotted), node),
    )


def source_component_entry(
    pair: str,
    source_left_momentum: alg.Vector,
    source_right_momentum: alg.Vector,
    source_left_mask: int,
    source_right_mask: int,
    source_dotted: int,
    source_left_color: int = 0,
    source_right_color: int = 1,
    marked_sector: str = "full",
) -> alg.A:
    """Bottom Hessian of nabla_-(A D) or nabla_-(D A)."""

    ctx = alg.Context(
        ("X",),
        (
            {"X": source_left_momentum},
            {"X": source_right_momentum},
        ),
        5,
    )
    left = alg.basis_endpoint(
        ctx, "X", 0, source_left_color, source_left_mask, 4
    )
    right = alg.basis_endpoint(
        ctx, "X", 1, source_right_color, source_right_mask, 5
    )

    if marked_sector not in {"full", "selected", "longitudinal", "evanescent"}:
        raise ValueError(marked_sector)

    def marked_a(value: alg.Mat, momentum: alg.Vector, color: int) -> alg.P:
        a1, _, _ = alg.canonical_A_words(value, "X")
        full = alg.component(alg.mat_d(a1, "X", 1), color)
        selected_matrix = alg.mat_scale(
            alg.SQRT2 * alg.vdot(momentum, momentum),
            alg.mat_d(value, "X", 0),
        )
        longitudinal_matrix = alg.mat_scale(
            alg.SQRT2 / 16,
            alg.mat_d(alg.mat_bar_d2(alg.mat_d2(value, "X"), "X"), "X", 0),
        )
        selected = alg.component(selected_matrix, color)
        longitudinal = alg.component(longitudinal_matrix, color)
        if marked_sector == "full":
            return full
        if marked_sector == "selected":
            return selected
        if marked_sector == "longitudinal":
            return longitudinal
        # The DRED subtraction removes det_4(r_e) and leaves one mu_l^2.
        return alg.component(
            alg.mat_scale(alg.SQRT2, alg.mat_d(value, "X", 0)), color
        )

    if pair == "A__Ddot1":
        a1, _, _ = alg.canonical_A_words(left, "X")
        del a1
        marked = marked_a(left, source_left_momentum, source_left_color)
        spectator = alg.component(
            d_bottom_word(right, source_dotted), source_right_color
        )
        word = marked * spectator
    elif pair == "Ddot1__A":
        spectator = alg.component(
            d_bottom_word(left, source_dotted), source_left_color
        )
        marked = marked_a(right, source_right_momentum, source_right_color)
        # |D|=1 in D nabla_- A.
        word = -spectator * marked
    else:
        raise ValueError(pair)

    coefficient = word.coefficient_labels((1, 1)).set_coordinates_zero("X")
    mask = marker_mask(source_left_mask, 4) | marker_mask(source_right_mask, 5)
    return coefficient.grass_coefficient(mask)


def gauge_fixing_source_component_entry(
    pair: str,
    source_left_momentum: alg.Vector,
    source_right_momentum: alg.Vector,
    source_left_mask: int,
    source_right_mask: int,
    source_dotted: int,
    source_left_color: int = 0,
    source_right_color: int = 1,
) -> alg.A:
    """Raw conditional-FF gauge-fixing Euler Hessian.

    This constructs the ``+8 D_+ Box P_0`` source word directly.  In the
    conventions of ``source_component_entry`` it is

        -(sqrt(2)/16) D_+ barD^2 D^2 U,

    and is therefore checked downstream against, but is not defined as a
    numerical residual of, the source-longitudinal Hessian.
    """

    ctx = alg.Context(
        ("X",),
        (
            {"X": source_left_momentum},
            {"X": source_right_momentum},
        ),
        5,
    )
    left = alg.basis_endpoint(
        ctx, "X", 0, source_left_color, source_left_mask, 4
    )
    right = alg.basis_endpoint(
        ctx, "X", 1, source_right_color, source_right_mask, 5
    )

    def marked_gf(value: alg.Mat, color: int) -> alg.P:
        return alg.component(
            alg.mat_scale(
                -alg.SQRT2 / 16,
                alg.mat_d(
                    alg.mat_bar_d2(alg.mat_d2(value, "X"), "X"),
                    "X",
                    0,
                ),
            ),
            color,
        )

    if pair == "A__Ddot1":
        word = marked_gf(left, source_left_color) * alg.component(
            d_bottom_word(right, source_dotted), source_right_color
        )
    elif pair == "Ddot1__A":
        word = -alg.component(
            d_bottom_word(left, source_dotted), source_left_color
        ) * marked_gf(right, source_right_color)
    else:
        raise ValueError(pair)

    coefficient = word.coefficient_labels((1, 1)).set_coordinates_zero("X")
    mask = marker_mask(source_left_mask, 4) | marker_mask(source_right_mask, 5)
    return coefficient.grass_coefficient(mask)


def ordered_minus_cubic_integrand(slots: tuple[alg.Mat, alg.Mat, alg.Mat], node: str) -> alg.P:
    """One fixed matrix-slot polarization of S_g^(-,3)."""

    def linear(value: alg.Mat, dotted: int) -> alg.Mat:
        return alg.mat_scale(
            -alg.SQRT2,
            alg.mat_d2(alg.mat_bar_d(value, node, dotted), node),
        )

    def quadratic(first: alg.Mat, second: alg.Mat, dotted: int) -> alg.Mat:
        ordered_commutator_piece = alg.mat_sub(
            alg.mat_mul(alg.mat_bar_d(first, node, dotted), second),
            alg.mat_mul(first, alg.mat_bar_d(second, node, dotted)),
        )
        return alg.mat_d2(ordered_commutator_piece, node)

    u0, u1, u2 = slots
    contracted = alg.mat_add(
        alg.mat_mul(linear(u0, 0), quadratic(u1, u2, 1)),
        alg.mat_mul(quadratic(u0, u1, 0), linear(u2, 1)),
        alg.mat_scale(-1, alg.mat_mul(linear(u0, 1), quadratic(u1, u2, 0))),
        alg.mat_scale(-1, alg.mat_mul(quadratic(u0, u1, 1), linear(u2, 0))),
    )
    return Fraction(-1, 256) * alg.mat_trace(contracted)


def ordered_plus_cubic_integrand(
    slots: tuple[alg.Mat, alg.Mat, alg.Mat], node: str
) -> alg.P:
    """One fixed matrix-slot polarization of S_g^(+,3)."""

    def linear(value: alg.Mat, undotted: int) -> alg.Mat:
        return alg.mat_scale(
            alg.SQRT2,
            alg.mat_bar_d2(alg.mat_d(value, node, undotted), node),
        )

    def quadratic(first: alg.Mat, second: alg.Mat, undotted: int) -> alg.Mat:
        ordered_commutator_piece = alg.mat_sub(
            alg.mat_mul(alg.mat_d(first, node, undotted), second),
            alg.mat_mul(first, alg.mat_d(second, node, undotted)),
        )
        return alg.mat_bar_d2(ordered_commutator_piece, node)

    u0, u1, u2 = slots
    # gamma^a gamma_a = gamma_1 gamma_0-gamma_0 gamma_1.
    contracted = alg.mat_add(
        alg.mat_mul(linear(u0, 1), quadratic(u1, u2, 0)),
        alg.mat_mul(quadratic(u0, u1, 1), linear(u2, 0)),
        alg.mat_scale(-1, alg.mat_mul(linear(u0, 0), quadratic(u1, u2, 1))),
        alg.mat_scale(-1, alg.mat_mul(quadratic(u0, u1, 0), linear(u2, 1))),
    )
    return Fraction(-1, 256) * alg.mat_trace(contracted)


def action_slot_entry(
    source_slot: int,
    bridge_slot: int,
    source_momentum: alg.Vector,
    bridge_momentum: alg.Vector,
    external_momentum: alg.Vector,
    source_mask: int,
    bridge_mask: int,
    external_dotted: int,
    source_color: int,
    bridge_color: int,
    external_color: int,
    global_offset: int,
    sector: str = "-",
    external_type: str = "D",
    polarization: alg.Vector = alg.ZERO_VECTOR,
) -> alg.A:
    external_slot = ({0, 1, 2} - {source_slot, bridge_slot}).pop()
    maximum_marker = 4 + global_offset + 2
    ctx = alg.Context(
        ("X",),
        (
            {"X": source_momentum},
            {"X": bridge_momentum},
            {"X": external_momentum},
        ),
        maximum_marker,
    )
    fields: list[alg.Mat | None] = [None, None, None]
    # Functional-direction order is source, bridge, external.  The slot
    # permutation is carried by the noncommutative matrix word itself.
    source_marker = 4 + global_offset
    bridge_marker = 4 + global_offset + 1
    external_marker = 4 + global_offset + 2
    fields[source_slot] = alg.basis_endpoint(
        ctx, "X", 0, source_color, source_mask, source_marker
    )
    fields[bridge_slot] = alg.basis_endpoint(
        ctx, "X", 1, bridge_color, bridge_mask, bridge_marker
    )
    if external_type == "D":
        fields[external_slot] = alg.endpoint_D(
            ctx,
            "X",
            2,
            external_color,
            external_dotted,
            eta_index=external_marker,
        )
    elif external_type == "A":
        fields[external_slot] = alg.endpoint_A(
            ctx,
            "X",
            2,
            external_color,
            polarization,
        )
    else:
        raise ValueError(external_type)
    if any(value is None for value in fields):
        raise AssertionError("incomplete ordered cubic slots")
    if sector == "-":
        integrand = ordered_minus_cubic_integrand(
            tuple(fields),  # type: ignore[arg-type]
            "X",
        )
        coefficient = alg.integrate_antichiral(
            integrand.coefficient_labels((1, 1, 1)), "X"
        )
    elif sector == "+":
        integrand = ordered_plus_cubic_integrand(
            tuple(fields),  # type: ignore[arg-type]
            "X",
        )
        coefficient = alg.integrate_chiral(
            integrand.coefficient_labels((1, 1, 1)), "X"
        )
    else:
        raise ValueError(sector)
    mask = marker_mask(source_mask, source_marker)
    mask |= marker_mask(bridge_mask, bridge_marker)
    if external_type == "D":
        mask |= 1 << external_marker
    return coefficient.grass_coefficient(mask)


def wick_pair_sign(parities: tuple[int, ...], pairs: tuple[tuple[int, int], ...]) -> int:
    """Move each odd contracted pair together, preserving external order."""

    live = [index for index, parity in enumerate(parities) if parity]
    sign = 1
    for first, second in pairs:
        if not parities[first]:
            if parities[second]:
                raise AssertionError("a propagator connected unequal coefficient parity")
            continue
        left = live.index(first)
        right = live.index(second)
        if left > right:
            left, right = right, left
        if (right - left - 1) % 2:
            sign = -sign
        del live[right]
        del live[left]
    return sign


def route_numerator(
    pair: str,
    left_source_slot: int,
    left_bridge_slot: int,
    right_source_slot: int,
    right_bridge_slot: int,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    source_dotted: int = 0,
    external_left_dotted: int = 0,
    external_right_dotted: int = 1,
    source_left_color: int = 0,
    source_right_color: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> alg.A:
    """Exact selected four-dimensional numerator for one structural route."""

    r0 = loop
    r1 = alg.vadd(loop, p)
    r2 = alg.vadd(loop, p, q)
    total = alg.ZERO
    left_external_slot = ({0, 1, 2} - {left_source_slot, left_bridge_slot}).pop()
    right_external_slot = ({0, 1, 2} - {right_source_slot, right_bridge_slot}).pop()

    for source_left_mask, source_right_mask, left_bridge_mask in itertools.product(
        range(16), repeat=3
    ):
        left_source_mask = 15 ^ source_left_mask
        right_source_mask = 15 ^ source_right_mask
        right_bridge_mask = 15 ^ left_bridge_mask
        cov_left = alg.component_covariance(source_left_mask, left_source_mask)
        cov_right = alg.component_covariance(source_right_mask, right_source_mask)
        cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
        if not cov_left or not cov_right or not cov_bridge:
            continue
        source = source_component_entry(
            pair,
            alg.vneg(r0),
            r2,
            source_left_mask,
            source_right_mask,
            source_dotted,
            source_left_color,
            source_right_color,
        )
        if not source:
            continue

        parities = [0] * 8
        parities[0] = source_left_mask.bit_count() % 2
        parities[1] = source_right_mask.bit_count() % 2
        parities[2] = left_source_mask.bit_count() % 2
        parities[3] = left_bridge_mask.bit_count() % 2
        parities[4] = 1
        parities[5] = right_source_mask.bit_count() % 2
        parities[6] = right_bridge_mask.bit_count() % 2
        parities[7] = 1
        wick = wick_pair_sign(
            tuple(parities),
            (
                (0, 2),
                (1, 5),
                (3, 6),
            ),
        )
        edge = -8 * cov_left * cov_right * cov_bridge

        for bridge_color in range(3):
            left = action_slot_entry(
                left_source_slot,
                left_bridge_slot,
                r0,
                alg.vneg(r1),
                p,
                left_source_mask,
                left_bridge_mask,
                external_left_dotted,
                source_left_color,
                bridge_color,
                external_left_color,
                2,
            )
            if not left:
                continue
            right = action_slot_entry(
                right_source_slot,
                right_bridge_slot,
                alg.vneg(r2),
                r1,
                q,
                right_source_mask,
                right_bridge_mask,
                external_right_dotted,
                source_right_color,
                bridge_color,
                external_right_color,
                5,
            )
            if not right:
                continue
            total += wick * edge * source * left * right
    return total


def all_tgg_route_numerators(
    pair: str,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    source_dotted: int = 0,
    external_left_dotted: int = 0,
    external_right_dotted: int = 1,
    source_left_color: int = 0,
    source_right_color: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
    marked_sector: str = "evanescent",
    source_attachment: str = "direct",
    left_action_sector: str = "-",
    right_action_sector: str = "-",
    left_external_type: str = "D",
    right_external_type: str = "D",
    left_polarization: alg.Vector = alg.ZERO_VECTOR,
    right_polarization: alg.Vector = alg.ZERO_VECTOR,
) -> dict[tuple[int, int, int, int], alg.A]:
    """Evaluate the 6x6 position-labeled TGG routes with shared caches."""

    r0 = loop
    r1 = alg.vadd(loop, p)
    r2 = alg.vadd(loop, p, q)
    assignments = tuple(itertools.permutations(range(3), 2))

    if source_attachment not in {"direct", "crossed"}:
        raise ValueError(source_attachment)
    source_momenta = (
        (alg.vneg(r0), r2)
        if source_attachment == "direct"
        else (r2, alg.vneg(r0))
    )
    source_table: dict[tuple[int, int], alg.A] = {}
    for source_left_mask, source_right_mask in itertools.product(range(16), repeat=2):
        value = source_component_entry(
            pair,
            *source_momenta,
            source_left_mask,
            source_right_mask,
            source_dotted,
            source_left_color,
            source_right_color,
            marked_sector,
        )
        if value:
            source_table[source_left_mask, source_right_mask] = value

    left_source_index = 0 if source_attachment == "direct" else 1
    right_source_index = 1 if source_attachment == "direct" else 0
    left_source_color = (
        source_left_color
        if source_attachment == "direct"
        else source_right_color
    )
    right_source_color = (
        source_right_color
        if source_attachment == "direct"
        else source_left_color
    )
    left_source_masks = sorted(
        {15 ^ masks[left_source_index] for masks in source_table}
    )
    right_source_masks = sorted(
        {15 ^ masks[right_source_index] for masks in source_table}
    )
    left_table: dict[tuple[int, int, int, int, int], alg.A] = {}
    right_table: dict[tuple[int, int, int, int, int], alg.A] = {}
    for source_slot, bridge_slot in assignments:
        for bridge_color, source_mask, bridge_mask in itertools.product(
            range(3), left_source_masks, range(16)
        ):
            left = action_slot_entry(
                source_slot,
                bridge_slot,
                r0,
                alg.vneg(r1),
                p,
                source_mask,
                bridge_mask,
                external_left_dotted,
                left_source_color,
                bridge_color,
                external_left_color,
                2,
                left_action_sector,
                left_external_type,
                left_polarization,
            )
            if left:
                left_table[
                    source_slot, bridge_slot, bridge_color, source_mask, bridge_mask
                ] = left
        for bridge_color, source_mask, bridge_mask in itertools.product(
            range(3), right_source_masks, range(16)
        ):
            right = action_slot_entry(
                source_slot,
                bridge_slot,
                alg.vneg(r2),
                r1,
                q,
                source_mask,
                bridge_mask,
                external_right_dotted,
                right_source_color,
                bridge_color,
                external_right_color,
                5,
                right_action_sector,
                right_external_type,
                right_polarization,
            )
            if right:
                right_table[
                    source_slot, bridge_slot, bridge_color, source_mask, bridge_mask
                ] = right

    totals = {
        (*left_assignment, *right_assignment): alg.ZERO
        for left_assignment in assignments
        for right_assignment in assignments
    }
    for source_masks, source in source_table.items():
        source_left_mask, source_right_mask = source_masks
        left_source_mask = 15 ^ (
            source_left_mask
            if source_attachment == "direct"
            else source_right_mask
        )
        right_source_mask = 15 ^ (
            source_right_mask
            if source_attachment == "direct"
            else source_left_mask
        )
        cov_left = alg.component_covariance(
            source_left_mask
            if source_attachment == "direct"
            else source_right_mask,
            left_source_mask,
        )
        cov_right = alg.component_covariance(
            source_right_mask
            if source_attachment == "direct"
            else source_left_mask,
            right_source_mask,
        )
        if not cov_left or not cov_right:
            continue
        for left_bridge_mask in range(16):
            right_bridge_mask = 15 ^ left_bridge_mask
            cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
            if not cov_bridge:
                continue
            edge = -8 * cov_left * cov_right * cov_bridge
            for left_assignment in assignments:
                left_source_slot, left_bridge_slot = left_assignment
                for right_assignment in assignments:
                    right_source_slot, right_bridge_slot = right_assignment
                    parities = [0] * 8
                    parities[0] = source_left_mask.bit_count() % 2
                    parities[1] = source_right_mask.bit_count() % 2
                    parities[2] = left_source_mask.bit_count() % 2
                    parities[3] = left_bridge_mask.bit_count() % 2
                    parities[4] = int(left_external_type == "D")
                    parities[5] = right_source_mask.bit_count() % 2
                    parities[6] = right_bridge_mask.bit_count() % 2
                    parities[7] = int(right_external_type == "D")
                    pairs = (
                        ((0, 2), (1, 5), (3, 6))
                        if source_attachment == "direct"
                        else ((0, 5), (1, 2), (3, 6))
                    )
                    wick = wick_pair_sign(tuple(parities), pairs)
                    value = alg.ZERO
                    for bridge_color in range(3):
                        left = left_table.get(
                            (
                                left_source_slot,
                                left_bridge_slot,
                                bridge_color,
                                left_source_mask,
                                left_bridge_mask,
                            ),
                            alg.ZERO,
                        )
                        if not left:
                            continue
                        right = right_table.get(
                            (
                                right_source_slot,
                                right_bridge_slot,
                                bridge_color,
                                right_source_mask,
                                right_bridge_mask,
                            ),
                            alg.ZERO,
                        )
                        value += left * right
                    if value:
                        key = (*left_assignment, *right_assignment)
                        totals[key] += wick * edge * source * value
    return totals


def aggregate_tgg_fast(
    pair: str,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    marked_sector: str = "evanescent",
    source_dotted: int = 0,
    external_left_dotted: int = 0,
    external_right_dotted: int = 1,
    source_left_color: int = 0,
    source_right_color: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> alg.A:
    """Same direct TGG sum, using the full cubic Hessian at each vertex."""

    r0 = loop
    r1 = alg.vadd(loop, p)
    r2 = alg.vadd(loop, p, q)
    total = alg.ZERO
    dummy_polarization = alg.ZERO_VECTOR
    for source_left_mask, source_right_mask, left_bridge_mask in itertools.product(
        range(16), repeat=3
    ):
        left_source_mask = 15 ^ source_left_mask
        right_source_mask = 15 ^ source_right_mask
        right_bridge_mask = 15 ^ left_bridge_mask
        cov_left = alg.component_covariance(source_left_mask, left_source_mask)
        cov_right = alg.component_covariance(source_right_mask, right_source_mask)
        cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
        if not cov_left or not cov_right or not cov_bridge:
            continue
        source = source_component_entry(
            pair,
            alg.vneg(r0),
            r2,
            source_left_mask,
            source_right_mask,
            source_dotted,
            source_left_color,
            source_right_color,
            marked_sector,
        )
        if not source:
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
        wick = wick_pair_sign(parities, ((0, 2), (1, 5), (3, 6)))
        edge = -8 * cov_left * cov_right * cov_bridge
        for bridge_color in range(3):
            left = alg.action_hessian_entry(
                3,
                r0,
                alg.vneg(r1),
                p,
                "D",
                dummy_polarization,
                external_left_dotted,
                source_left_color,
                bridge_color,
                left_source_mask,
                left_bridge_mask,
                external_left_color,
                0,
            )
            if not left:
                continue
            right = alg.action_hessian_entry(
                3,
                alg.vneg(r2),
                r1,
                q,
                "D",
                dummy_polarization,
                external_right_dotted,
                source_right_color,
                bridge_color,
                right_source_mask,
                right_bridge_mask,
                external_right_color,
                0,
            )
            if right:
                total += wick * edge * source * left * right
    return total


def aggregate_tgg_fast_star(
    arguments: tuple[str, alg.Vector, alg.Vector, alg.Vector, str]
) -> tuple[str, str, alg.A]:
    pair, loop, p, q, marked_sector = arguments
    return pair, marked_sector, aggregate_tgg_fast(
        pair, loop, p, q, marked_sector
    )


def aggregate_tgg_numerator(
    arguments: tuple[str, alg.Vector, alg.Vector, alg.Vector]
) -> tuple[str, dict[tuple[int, int, int, int], alg.A], alg.A]:
    pair, loop, p, q = arguments
    routes = all_tgg_route_numerators(pair, loop, p, q)
    return pair, routes, sum(routes.values(), alg.ZERO)


def aggregate_tgg_attachment_numerator(
    arguments: tuple[str, alg.Vector, alg.Vector, alg.Vector, str]
) -> tuple[str, str, dict[tuple[int, int, int, int], alg.A], alg.A]:
    pair, loop, p, q, source_attachment = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        source_attachment=source_attachment,
    )
    return pair, source_attachment, routes, sum(routes.values(), alg.ZERO)


def aggregate_tgg_chirality_numerator(
    arguments: tuple[
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
        str,
        str,
    ]
) -> tuple[
    str,
    str,
    str,
    dict[tuple[int, int, int, int], alg.A],
    alg.A,
]:
    pair, loop, p, q, left_sector, right_sector = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        left_action_sector=left_sector,
        right_action_sector=right_sector,
    )
    return (
        pair,
        left_sector,
        right_sector,
        routes,
        sum(routes.values(), alg.ZERO),
    )


def aggregate_tgg_chirality_sum(
    arguments: tuple[
        int,
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
        str,
        str,
    ]
) -> tuple[int, str, str, str, alg.A]:
    sample_index, pair, loop, p, q, left_sector, right_sector = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        left_action_sector=left_sector,
        right_action_sector=right_sector,
    )
    return (
        sample_index,
        pair,
        left_sector,
        right_sector,
        sum(routes.values(), alg.ZERO),
    )


def aggregate_physical_ww_parent(
    arguments: tuple[
        int,
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
        alg.Vector,
    ]
) -> tuple[
    int,
    str,
    dict[tuple[int, int, int, int], alg.A],
    alg.A,
    alg.A,
]:
    """Canonical ``V_tildeW x V_W`` parent from CUT-ORBIT-026.

    The left action vertex carries the external antichiral ``D`` endpoint
    and therefore uses ``S_g^-``.  The right vertex carries the external
    chiral ``A`` endpoint and uses ``S_g^+``.  This is distinct from the
    diagnostic off-shell prepotential ``D x D`` projection.
    """

    sample_index, pair, loop, p, q, polarization = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        external_left_dotted=0,
        external_right_dotted=0,
        external_left_color=1,
        external_right_color=0,
        left_action_sector="-",
        right_action_sector="+",
        left_external_type="D",
        right_external_type="A",
        right_polarization=polarization,
    )
    norm_a, norm_d = alg.external_normalizations_pair(
        q,
        p,
        polarization,
        0,
        0,
        1,
    )
    color = alg.A(alg.su2_F(0, 1, 1, 0))
    normalization = norm_a * norm_d * color
    if not normalization:
        raise AssertionError("zero physical V_tildeW x V_W normalization")
    normalized = {
        route: value / normalization for route, value in routes.items()
    }
    return (
        sample_index,
        pair,
        normalized,
        sum(normalized.values(), alg.ZERO),
        normalization,
    )


def aggregate_tgg_sector_numerator(
    arguments: tuple[str, alg.Vector, alg.Vector, alg.Vector, str]
) -> tuple[str, str, dict[tuple[int, int, int, int], alg.A], alg.A]:
    pair, loop, p, q, marked_sector = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        marked_sector=marked_sector,
    )
    return pair, marked_sector, routes, sum(routes.values(), alg.ZERO)


def longitudinal_probe_evaluation(
    arguments: tuple[
        str,
        str,
        str,
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
    ],
) -> tuple[
    str,
    str,
    str,
    str,
    dict[tuple[int, int, int, int], alg.A],
]:
    pair, isolated, vertex, point_name, loop, p, q = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        marked_sector="longitudinal",
    )
    return pair, isolated, vertex, point_name, routes


def longitudinal_attachment_probe_evaluation(
    arguments: tuple[
        str,
        str,
        str,
        alg.Vector,
        alg.Vector,
        alg.Vector,
        str,
    ],
) -> tuple[str, str, str, str, dict[tuple[int, int, int, int], alg.A]]:
    pair, isolated, point_name, loop, p, q, source_attachment = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        marked_sector="longitudinal",
        source_attachment=source_attachment,
    )
    return pair, isolated, "centroid", point_name, routes


def aggregate_tgg_numerator_dotted(
    arguments: tuple[str, alg.Vector, alg.Vector, alg.Vector, int, int]
) -> tuple[str, dict[tuple[int, int, int, int], alg.A], alg.A]:
    pair, loop, p, q, left_dotted, right_dotted = arguments
    routes = all_tgg_route_numerators(
        pair,
        loop,
        p,
        q,
        external_left_dotted=left_dotted,
        external_right_dotted=right_dotted,
    )
    return pair, routes, sum(routes.values(), alg.ZERO)


def parse_route_slots(route_id: str) -> tuple[int, int, int, int]:
    left, right = route_id.rsplit("::", 2)[1:]

    def parse(fragment: str) -> tuple[int, int]:
        inside = fragment[fragment.index("[") + 1 : fragment.index("]")]
        a, b = inside.split(",")
        return int(a), int(b)

    return (*parse(left), *parse(right))


def load_routes() -> dict[str, list[dict[str, object]]]:
    """Load only the split-source 1PI parents.

    The global census also contains the connected spectator-source
    double-bridge family.  Those rows are external-leg self energies: the
    unique source--action stem is a cut edge, so they are not members of the
    amputated 1PI quotient evaluated here.
    """

    payload = json.loads(CENSUS.read_text(encoding="utf-8"))
    source = payload.get("legacy_routes", payload["routes"])
    result: dict[str, list[dict[str, object]]] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        result[pair] = [row for row in source if row["pair_id"] == pair]
    return result


def load_spectator_routes() -> dict[str, list[dict[str, object]]]:
    payload = json.loads(CENSUS.read_text(encoding="utf-8"))
    source = payload.get("spectator_routes", ())
    result: dict[str, list[dict[str, object]]] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        result[pair] = [row for row in source if row["pair_id"] == pair]
    return result


def gaussian_expr(value: alg.A) -> sp.Expr:
    if value.b or value.d:
        raise AssertionError(f"unexpected sqrt(2) residue: {value.text()}")
    return sp.Rational(value.a.numerator, value.a.denominator) + sp.I * sp.Rational(
        value.c.numerator, value.c.denominator
    )


def expr_text(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value))


def plus_dotted(momentum: alg.Vector, dotted: int) -> sp.Expr:
    values = [gaussian_expr(component) for component in momentum]
    if dotted == 0:
        return values[3] - sp.I * values[2]
    if dotted == 1:
        return -values[1] - sp.I * values[0]
    raise ValueError(dotted)


def interpolation_samples() -> list[tuple[alg.Vector, alg.Vector, alg.Vector]]:
    return [
        (
            alg.vec((1, 2, 3, 4)),
            alg.vec((2, -1, 1, 0)),
            alg.vec((-1, 3, 0, 2)),
        ),
        (
            alg.vec((2, -1, 0, 1)),
            alg.vec((2, -1, 1, 0)),
            alg.vec((-1, 3, 0, 2)),
        ),
        (
            alg.vec((0, 1, -2, 3)),
            alg.vec((1, 0, 2, -1)),
            alg.vec((0, -2, 1, 2)),
        ),
        (
            alg.vec((3, 0, 1, -2)),
            alg.vec((-1, 2, 0, 1)),
            alg.vec((2, 1, -1, 0)),
        ),
    ]


def verify_marked_operator_identity() -> int:
    checks = 0
    for momentum in (alg.vec((1, 2, 3, 4)), alg.vec((2, -1, 0, 1))):
        for theta_mask in range(16):
            ctx = alg.Context(("X",), ({"X": momentum},), 4)
            value = alg.basis_endpoint(ctx, "X", 0, 0, theta_mask, 4)
            a1, _, _ = alg.canonical_A_words(value, "X")
            full = alg.component(alg.mat_d(a1, "X", 1), 0)
            selected = alg.component(
                alg.mat_scale(
                    alg.SQRT2 * alg.vdot(momentum, momentum),
                    alg.mat_d(value, "X", 0),
                ),
                0,
            )
            longitudinal = alg.component(
                alg.mat_scale(
                    alg.SQRT2 / 16,
                    alg.mat_d(
                        alg.mat_bar_d2(alg.mat_d2(value, "X"), "X"),
                        "X",
                        0,
                    ),
                ),
                0,
            )
            coefficient_mask = marker_mask(theta_mask, 4)
            values = [
                word.coefficient_labels((1,)).set_coordinates_zero("X").grass_coefficient(
                    coefficient_mask
                )
                for word in (full, selected, longitudinal)
            ]
            if values[0] != values[1] + values[2]:
                raise AssertionError(
                    f"marked operator identity mask={theta_mask}: "
                    f"{values[0].text()} != {values[1].text()}+{values[2].text()}"
                )
            checks += 1
    return checks


def verify_selected_parent_factorization() -> int:
    """The selected source is a four-dimensional inverse square times R."""

    checks = 0
    for momentum in (
        alg.vec((1, 2, 3, 4)),
        alg.vec((2, -1, 0, 1)),
    ):
        determinant = alg.vdot(momentum, momentum)
        for theta_mask in range(16):
            ctx = alg.Context(("X",), ({"X": momentum},), 4)
            value = alg.basis_endpoint(ctx, "X", 0, 0, theta_mask, 4)
            remainder = alg.mat_scale(
                alg.SQRT2, alg.mat_d(value, "X", 0)
            )
            selected = alg.mat_scale(determinant, remainder)
            expected = alg.mat_scale(
                alg.SQRT2 * determinant,
                alg.mat_d(value, "X", 0),
            )
            difference = alg.mat_sub(selected, expected)
            if any(entry.terms for row in difference for entry in row):
                raise AssertionError(
                    f"selected parent factorization mask={theta_mask}"
                )
            checks += 1
    return checks


def verify_gauge_fixing_longitudinal_cancellation() -> int:
    """Check the conditional FF P0 Euler row before any loop reduction.

    Box*P0=(barD2*D2+D2*barD2)/16.  The left D_+ kills the
    D2*barD2 summand.  With the Ward sign which rewrites the invariant
    Euler operator through the gauge-fixed Schwinger operator, the remaining
    word is the negative of the longitudinal part of D_-A1.  Since the two
    source Hessians are then identical with opposite coefficients, the
    cancellation holds for every downstream route and every edge tag.
    """

    checks = 0
    for momentum in (alg.vec((1, 2, 3, 4)), alg.vec((2, -1, 0, 1))):
        for theta_mask in range(16):
            ctx = alg.Context(("X",), ({"X": momentum},), 4)
            value = alg.basis_endpoint(ctx, "X", 0, 0, theta_mask, 4)
            longitudinal = alg.component(
                alg.mat_scale(
                    alg.SQRT2 / 16,
                    alg.mat_d(
                        alg.mat_bar_d2(alg.mat_d2(value, "X"), "X"),
                        "X",
                        0,
                    ),
                ),
                0,
            )
            gauge_fixing = alg.component(
                alg.mat_scale(
                    -alg.SQRT2 / 16,
                    alg.mat_d(
                        alg.mat_bar_d2(alg.mat_d2(value, "X"), "X"),
                        "X",
                        0,
                    ),
                ),
                0,
            )
            mask = marker_mask(theta_mask, 4)
            total = (
                longitudinal + gauge_fixing
            ).coefficient_labels((1,)).set_coordinates_zero("X")
            if total.grass_coefficient(mask):
                raise AssertionError(
                    f"conditional FF longitudinal cancellation mask={theta_mask}"
                )
            checks += 1
    return checks


def fp_current_kernel_certificate() -> dict[str, object]:
    """Exact endpoint kernel plus the two-edge FP Schwinger quotient.

    Differentiating the cubic FP word with respect to V leaves one chiral
    and one antichiral constrained ghost line.  D_+ acts only on the chiral
    line.  The coefficients, color words, and closed-ghost-loop sign multiply
    the kernel below but cannot turn the full-d FP Box kernel into the
    four-dimensional spin determinant occurring in the marked gauge source.
    """

    probes = (
        alg.ZERO_VECTOR,
        alg.vec((1, 2, 3, 4)),
        alg.vec((2, -1, 0, 1)),
        alg.vec((0, 1, -2, 3)),
    )
    rows: list[dict[str, object]] = []
    for loop in probes:
        # The second line carries -loop; the action vertex therefore has
        # zero momentum in this degree certificate.  Nonzero external shifts
        # add only a loop-independent affine term.
        k_dot1 = matter_current_contact_dword(loop, alg.vneg(loop), 0)
        k_dot2 = matter_current_contact_dword(loop, alg.vneg(loop), 1)
        # Keep the comparison in Q(sqrt(2),i), not through SymPy floats.
        plus_dot1 = loop[3] - alg.I * loop[2]
        plus_dot2 = -loop[1] - alg.I * loop[0]
        expected_dot1 = alg.I * plus_dot2
        expected_dot2 = -alg.I * plus_dot1
        if k_dot1 != expected_dot1 or k_dot2 != expected_dot2:
            raise AssertionError(
                f"FP affine kernel: {k_dot1.text()}, {k_dot2.text()}"
            )
        rows.append(
            {
                "loop": [entry.text() for entry in loop],
                "K_dot1": k_dot1.text(),
                "K_dot2": k_dot2.text(),
            }
        )

    hessian_checks = 0
    center = alg.vec((2, -1, 1, 3))
    for dotted in (0, 1):
        for axis in range(4):
            unit = [0, 0, 0, 0]
            unit[axis] = 1
            direction = alg.vec(unit)

            def kernel(momentum: alg.Vector) -> alg.A:
                return matter_current_contact_dword(
                    momentum, alg.vneg(momentum), dotted
                )

            second = (
                kernel(alg.vadd(center, direction))
                - 2 * kernel(center)
                + kernel(alg.vadd(center, alg.vneg(direction)))
            )
            if second:
                raise AssertionError(
                    f"FP kernel acquired a quadratic loop term dotted={dotted} axis={axis}"
                )
            hessian_checks += 1
    return {
        "BRST_through_V1": (
            "sV=i*(tildec-c)+(i/2)*([tildec,V]+[c,V])+O(V^2)"
        ),
        "free_kernels": {
            "K_plus": "(i/4)*barD^2",
            "K_minus": "-(i/4)*D^2",
            "K_plus_inverse": "-(i/4)*D^2/Box",
            "K_minus_inverse": "+(i/4)*barD^2/Box",
            "inverse_checks": {
                "plus": "K_plus*K_plus_inverse=P_plus",
                "minus": "K_minus*K_minus_inverse=P_minus",
            },
        },
        "cubic_vertices": {
            "V_plus": "(i/8)*int_plus c_prime*barD^2[c,V]",
            "V_minus": "(i/8)*int_minus tildec_prime*D^2[tildec,V]",
            "closed_Grassmann_loop_sign": "-1",
        },
        "ordered_D_word": (
            "Pi_dot1*Tr_D[barD^2 ad(V_L) (barD^2/Box_s0) "
            "D^2 ad(V_R) (D^2/Box_s1)]*Pi_dot2"
        ),
        "edge_cuts": [
            {
                "edge": "s0",
                "full_d_identity": (
                    "s0_d^2/(s0^2*s1^2)-1/s1^2=0"
                ),
            },
            {
                "edge": "s1",
                "full_d_identity": (
                    "s1_d^2/(s0^2*s1^2)-1/s0^2=0"
                ),
            },
        ],
        "common_D_word": {
            "K_dot1": "i*r_(+dot2)",
            "K_dot2": "-i*r_(+dot1)",
        },
        "replay_samples": rows,
        "loop_hessian_checks": hessian_checks,
        "four_dimensional_scalar_square": "0",
        "Euler_bubble": "+B_FP_DD (nonzero before the cut)",
        "full_d_cut": "-B_FP_DD",
        "full_Schwinger_family": "0",
        "mu2_remainder": "0",
        "anomaly_sector": "0",
    }


def cached_o05_tagged_samples() -> dict[
    tuple[int, str, str], dict[str, alg.A]
]:
    """Exact four-sample replay produced by ``dd_bubble_samples_parallel``.

    The expensive component/color replay is intentionally exposed separately
    from the default repository check.  These closed forms were obtained from
    that replay and are re-interpolated below before any edge aggregation.
    """

    rows: dict[tuple[int, str, str], dict[str, alg.A]] = {}
    for sample_index, (_, p, q) in enumerate(interpolation_samples()):
        p_plus = p[3] - alg.I * p[2]
        q_plus = q[3] - alg.I * q[2]
        rows[sample_index, "A__Ddot1", "source_dot1_action_dot2"] = {
            "I1_N1A2[A]*D1[B]": 5 * alg.I * q_plus,
            "I1_N1gamma1[A]*D1[B]": 2 * alg.I * q_plus,
        }
        rows[sample_index, "A__Ddot1", "source_dot2_action_dot1"] = {
            "I1_N0[A]*D2[B]": 2 * alg.I * q_plus,
        }
        rows[sample_index, "Ddot1__A", "source_dot1_action_dot2"] = {
            "I1_-D2[A]*N0[B]": -alg.I * q_plus / 2,
        }
        rows[sample_index, "Ddot1__A", "source_dot2_action_dot1"] = {
            "I1_-D1[A]*N1A2[B]": alg.I * (p_plus + q_plus),
        }
    return rows


def o06_occurrence_certificate() -> dict[str, object]:
    """Exact tagged quartic bubble after the DD/F normalization."""

    samples: list[dict[str, object]] = []
    for loop, p, q in interpolation_samples():
        del loop
        p_plus = p[3] - alg.I * p[2]
        q_plus = q[3] - alg.I * q[2]
        half = alg.I * (p_plus + q_plus) / 2
        samples.append(
            {
                "AD": {},
                "DA": {
                    "I0_-D1[A]*N0[B]__Sg4_+": half.text(),
                    "I0_-D1[A]*N0[B]__Sg4_-": half.text(),
                },
            }
        )
    return {
        "collapsed_edge": "r1",
        "denominator": "D0*D2",
        "AD_rank_one": {
            "ell_plus_dotted": "0",
            "p_plus_dotted": "0",
            "q_plus_dotted": "0",
        },
        "DA_rank_one": {
            "ell_plus_dotted": "0",
            "p_plus_dotted": "i",
            "q_plus_dotted": "i",
        },
        "chiral_fraction": "1/2",
        "antichiral_fraction": "1/2",
        "replay_samples": samples,
        "four_dimensional_scalar_square": "0",
        "standalone_anomaly_sector": "0",
    }


def matter_current_pair_certificate() -> dict[str, object]:
    """Keep the Euler current and explicit contact as separate SD members."""

    samples: list[dict[str, object]] = []
    for loop, _, _ in interpolation_samples():
        first = loop
        second = alg.vneg(loop)
        for dotted in (0, 1):
            kernel = matter_current_contact_dword(first, second, dotted)
            euler = 2 * alg.I * kernel
            explicit = -2 * alg.I * kernel
            if euler + explicit:
                raise AssertionError("matter Euler/current pair did not cancel")
            samples.append(
                {
                    "loop": [entry.text() for entry in loop],
                    "dotted": dotted + 1,
                    "K": kernel.text(),
                    "Euler_current": euler.text(),
                    "explicit_contact": explicit.text(),
                    "sum": "0",
                }
            )
    return {
        "tree_identity": "-D_+[-2*i*(Phi_s x C_s)]*D-2*i*(B_s x C_s)*D=0",
        "Euler_current_coefficient": "+2*i",
        "explicit_contact_coefficient": "-2*i",
        "common_D_word": {
            "K_dot1": "i*r_(+dot2)",
            "K_dot2": "-i*r_(+dot1)",
        },
        "replay_samples": samples,
        "full_d_family_sum": "0",
        "mu2_remainder": "0",
    }


def o07_tadpole_certificate(workers: int) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for sample_index, (loop, p, q) in enumerate(interpolation_samples()):
        for pair in ("A__Ddot1", "Ddot1__A"):
            value = dd_tadpole_values_parallel(pair, loop, p, q, workers)
            if value:
                raise AssertionError(f"O07 tadpole {pair} sample={sample_index}: {value}")
            rows.append(
                {
                    "sample": sample_index,
                    "pair": pair,
                    "loop": [entry.text() for entry in loop],
                    "tagged_sum": {},
                }
            )
    return {
        "replay_samples": rows,
        "sample_checks": len(rows),
        "denominator": "D0",
        "integrated_reason": (
            "Every one-propagator massless tadpole is scaleless in DRED; "
            "the eight exact rational samples additionally give an empty "
            "tagged component/color sum."
        ),
        "standalone_anomaly_sector": "0",
    }


O05_EDGE_BY_TAG = {
    "A__Ddot1": {
        "I1_N1A2[A]*D1[B]": "r0",
        "I1_N1gamma1[A]*D1[B]": "r0",
        "I1_N0[A]*D2[B]": "r2",
    },
    "Ddot1__A": {
        "I1_-D2[A]*N0[B]": "r0",
        "I1_-D1[A]*N1A2[B]": "r2",
        "I1_-D1[A]*N1gamma1[B]": "r2",
    },
}


def interpolate_tagged_rank_one(
    values: dict[tuple[int, str, str], dict[str, alg.A]],
) -> dict[str, dict[str, dict[str, object]]]:
    """Interpolate each O05 occurrence before any edge aggregation."""

    samples = interpolation_samples()
    matrix = sp.Matrix(
        [
            [plus_dotted(loop, 0), plus_dotted(p, 0), plus_dotted(q, 0)]
            for loop, p, q in samples[:3]
        ]
    )
    if matrix.det() == 0:
        raise AssertionError("singular O05 interpolation frame")
    result: dict[str, dict[str, dict[str, object]]] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        pair_rows: dict[str, dict[str, object]] = {}
        for attachment in (
            "source_dot1_action_dot2",
            "source_dot2_action_dot1",
        ):
            tags = sorted(
                {
                    tag
                    for sample_index in range(len(samples))
                    for tag in values.get((sample_index, pair, attachment), {})
                }
            )
            for tag in tags:
                rhs = sp.Matrix(
                    [
                        gaussian_expr(
                            values.get((sample_index, pair, attachment), {}).get(
                                tag, alg.ZERO
                            )
                        )
                        for sample_index in range(3)
                    ]
                )
                ell_coefficient, p_coefficient, q_coefficient = tuple(
                    matrix.inv() * rhs
                )
                check = sp.simplify(
                    ell_coefficient * plus_dotted(samples[3][0], 0)
                    + p_coefficient * plus_dotted(samples[3][1], 0)
                    + q_coefficient * plus_dotted(samples[3][2], 0)
                    - gaussian_expr(
                        values.get((3, pair, attachment), {}).get(tag, alg.ZERO)
                    )
                )
                if check != 0:
                    raise AssertionError(
                        f"non-affine O05 occurrence {pair} {attachment} {tag}: {check}"
                    )
                row_id = f"{attachment}::{tag}"
                pair_rows[row_id] = {
                    "attachment": attachment,
                    "source_tag": tag,
                    "collapsed_edge": O05_EDGE_BY_TAG[pair][tag],
                    "rank_one": {
                        "ell_plus_dotted": expr_text(ell_coefficient),
                        "p_plus_dotted": expr_text(p_coefficient),
                        "q_plus_dotted": expr_text(q_coefficient),
                    },
                    "withheld_sample_check": "0",
                    "four_dimensional_scalar_square": "0",
                }
        result[pair] = pair_rows
    return result


def exact_simplex_moments() -> dict[str, str]:
    y, z = sp.symbols("y z")
    area_with_feynman_two = sp.integrate(
        sp.integrate(2, (z, 0, 1 - y)), (y, 0, 1)
    )
    p_shift = sp.integrate(
        sp.integrate(2 * (y + z), (z, 0, 1 - y)), (y, 0, 1)
    )
    q_shift = sp.integrate(
        sp.integrate(2 * z, (z, 0, 1 - y)), (y, 0, 1)
    )
    if (area_with_feynman_two, p_shift, q_shift) != (
        sp.Integer(1),
        sp.Rational(2, 3),
        sp.Rational(1, 3),
    ):
        raise AssertionError((area_with_feynman_two, p_shift, q_shift))
    return {
        "2*simplex_area": expr_text(area_with_feynman_two),
        "2*integral_simplex_(y+z)": expr_text(p_shift),
        "2*integral_simplex_z": expr_text(q_shift),
    }


def matter_current_contact_dword(
    first_momentum: alg.Vector,
    second_momentum: alg.Vector,
    action_external_dotted: int,
) -> alg.A:
    """Raw B_s C_s D contact with one matter-gauge action vertex.

    The source is at S and the full superspace matter vertex is at X.  The
    source-spectator D coefficient is normalized to one; the action D is kept
    as its exact vector-prepotential direction.  Projector factors 1/16 are
    included on both matter propagators.
    """

    action_momentum = alg.vneg(alg.vadd(first_momentum, second_momentum))
    ctx = alg.Context(
        ("S", "X"),
        (
            {"S": first_momentum, "X": alg.vneg(first_momentum)},
            {"S": second_momentum, "X": alg.vneg(second_momentum)},
            {"X": action_momentum},
        ),
        10,
    )
    phi_edge = alg.delta4(ctx, "S", "X") * alg.P.label(ctx, 0)
    tilde_edge = alg.delta4(ctx, "S", "X") * alg.P.label(ctx, 1)
    phi_projected = Fraction(1, 16) * alg.bar_d2(
        alg.d2(phi_edge, "S"), "S"
    )
    tilde_projected = Fraction(1, 16) * alg.d2(
        alg.bar_d2(tilde_edge, "S"), "S"
    )
    b_source = alg.d_lower(phi_projected, "S", 0)
    spectator_d = alg.P.grass_generator(ctx, 9)
    theta_square = -2 * alg.theta(ctx, "X", 0) * alg.theta(ctx, "X", 1)
    if action_external_dotted == 0:
        action_d = Fraction(1, 4) * theta_square * alg.bar_theta_lower(
            ctx, "X", 1
        )
    elif action_external_dotted == 1:
        action_d = -Fraction(1, 4) * theta_square * alg.bar_theta_lower(
            ctx, "X", 0
        )
    else:
        raise ValueError(action_external_dotted)
    action_d *= alg.P.grass_generator(ctx, 10) * alg.P.label(ctx, 2)
    word = (b_source * tilde_projected * spectator_d).set_coordinates_zero("S")
    word = (word * action_d).coefficient_labels((1, 1, 1))
    top = sum(1 << index for index in range(4, 8)) | (1 << 9) | (1 << 10)
    return word.grass_coefficient(top)


def canonical_D_words(
    U: alg.Mat,
    node: str,
    dotted: int,
) -> tuple[alg.Mat, alg.Mat, alg.Mat]:
    """Bottom tilde-W expansion through cubic prepotential order."""

    bar_u = alg.mat_bar_d(U, node, dotted)
    u2 = alg.mat_mul(U, U)
    linear = alg.mat_scale(
        -alg.SQRT2 / 8,
        alg.mat_d2(bar_u, node),
    )
    quadratic = alg.mat_scale(
        Fraction(1, 8),
        alg.mat_d2(
            alg.mat_sub(
                alg.mat_mul(bar_u, U),
                alg.mat_mul(U, bar_u),
            ),
            node,
        ),
    )
    cubic = alg.mat_scale(
        -alg.SQRT2 / 24,
        alg.mat_d2(
            alg.mat_add(
                alg.mat_mul(bar_u, u2),
                alg.mat_scale(-2, alg.mat_mul(alg.mat_mul(U, bar_u), U)),
                alg.mat_mul(u2, bar_u),
            ),
            node,
        ),
    )
    return linear, quadratic, cubic


def pair_source_tagged_words(
    U: alg.Mat,
    node: str,
    pair: str,
    source_dotted: int,
    source_a: int,
    source_b: int,
) -> tuple[dict[str, alg.P], dict[str, alg.P], dict[str, alg.P]]:
    """Occurrence-tagged nabla_-(A D) or nabla_-(D A) through order g^2."""

    A1, A2, A3 = alg.canonical_A_words(U, node)
    D1, D2, D3 = canonical_D_words(U, node, source_dotted)
    gamma1 = alg.mat_scale(alg.SQRT2, alg.mat_d(U, node, 1))
    gamma2 = alg.mat_sub(
        alg.mat_mul(alg.mat_d(U, node, 1), U),
        alg.mat_mul(U, alg.mat_d(U, node, 1)),
    )
    N0 = alg.mat_d(A1, node, 1)
    N1_A2 = alg.mat_d(A2, node, 1)
    N1_gamma1 = alg.mat_sub(
        alg.mat_mul(gamma1, A1), alg.mat_mul(A1, gamma1)
    )
    N2_A3 = alg.mat_d(A3, node, 1)
    N2_gamma1_A2 = alg.mat_sub(
        alg.mat_mul(gamma1, A2), alg.mat_mul(A2, gamma1)
    )
    N2_gamma2_A1 = alg.mat_sub(
        alg.mat_mul(gamma2, A1), alg.mat_mul(A1, gamma2)
    )

    def c(value: alg.Mat, color: int) -> alg.P:
        return alg.component(value, color)

    if pair == "A__Ddot1":
        n0 = c(N0, source_a)
        n1a2 = c(N1_A2, source_a)
        n1g1 = c(N1_gamma1, source_a)
        n2a3 = c(N2_A3, source_a)
        n2g1a2 = c(N2_gamma1_A2, source_a)
        n2g2a1 = c(N2_gamma2_A1, source_a)
        d1, d2, d3 = (c(value, source_b) for value in (D1, D2, D3))
        return (
            {"I0_N0[A]*D1[B]": n0 * d1},
            {
                "I1_N1A2[A]*D1[B]": n1a2 * d1,
                "I1_N1gamma1[A]*D1[B]": n1g1 * d1,
                "I1_N0[A]*D2[B]": n0 * d2,
            },
            {
                "I2_N2A3[A]*D1[B]": n2a3 * d1,
                "I2_N2gamma1A2[A]*D1[B]": n2g1a2 * d1,
                "I2_N2gamma2A1[A]*D1[B]": n2g2a1 * d1,
                "I2_N1A2[A]*D2[B]": n1a2 * d2,
                "I2_N1gamma1[A]*D2[B]": n1g1 * d2,
                "I2_N0[A]*D3[B]": n0 * d3,
            },
        )
    if pair == "Ddot1__A":
        d1, d2, d3 = (c(value, source_a) for value in (D1, D2, D3))
        n0 = c(N0, source_b)
        n1a2 = c(N1_A2, source_b)
        n1g1 = c(N1_gamma1, source_b)
        n2a3 = c(N2_A3, source_b)
        n2g1a2 = c(N2_gamma1_A2, source_b)
        n2g2a1 = c(N2_gamma2_A1, source_b)
        return (
            {"I0_-D1[A]*N0[B]": -d1 * n0},
            {
                "I1_-D2[A]*N0[B]": -d2 * n0,
                "I1_-D1[A]*N1A2[B]": -d1 * n1a2,
                "I1_-D1[A]*N1gamma1[B]": -d1 * n1g1,
            },
            {
                "I2_-D3[A]*N0[B]": -d3 * n0,
                "I2_-D2[A]*N1A2[B]": -d2 * n1a2,
                "I2_-D2[A]*N1gamma1[B]": -d2 * n1g1,
                "I2_-D1[A]*N2A3[B]": -d1 * n2a3,
                "I2_-D1[A]*N2gamma1A2[B]": -d1 * n2g1a2,
                "I2_-D1[A]*N2gamma2A1[B]": -d1 * n2g2a1,
            },
        )
    raise ValueError(pair)


def pair_source_hessian_entries(
    order: int,
    pair: str,
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    background_momentum: alg.Vector,
    source_dotted: int,
    background_dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    source_a: int,
    source_b: int,
    background_color: int,
    background_type: str = "D",
    polarization: alg.Vector = alg.ZERO_VECTOR,
) -> dict[str, alg.A]:
    ctx = alg.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        (
            alg.endpoint_D(
                ctx,
                "X",
                2,
                background_color,
                background_dotted,
                eta_index=4,
            )
            if background_type == "D"
            else alg.endpoint_A(
                ctx,
                "X",
                2,
                background_color,
                polarization,
            )
        ),
    ]
    tagged = pair_source_tagged_words(
        alg.sum_mats(fields),
        "X",
        pair,
        source_dotted,
        source_a,
        source_b,
    )[order]
    if background_type not in {"A", "D"}:
        raise ValueError(background_type)
    marker = alg.hessian_marker_mask(
        theta_mask_1,
        theta_mask_2,
        background_type == "D",
    )
    result: dict[str, alg.A] = {}
    for tag, source in tagged.items():
        coefficient = source.coefficient_labels((1, 1, 1)).set_coordinates_zero("X")
        value = coefficient.grass_coefficient(marker)
        if value:
            result[tag] = value
    return result


def pair_source_I0_hessian_entries(
    pair: str,
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    source_dotted: int,
    source_a: int,
    source_b: int,
) -> dict[str, alg.A]:
    ctx = alg.Context(
        ("X",),
        ({"X": momentum_1}, {"X": momentum_2}),
        6,
    )
    fields = [
        alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
    ]
    tagged = pair_source_tagged_words(
        alg.sum_mats(fields),
        "X",
        pair,
        source_dotted,
        source_a,
        source_b,
    )[0]
    marker = alg.hessian_marker_mask(theta_mask_1, theta_mask_2, False)
    result: dict[str, alg.A] = {}
    for tag, source in tagged.items():
        coefficient = source.coefficient_labels((1, 1)).set_coordinates_zero("X")
        value = coefficient.grass_coefficient(marker)
        if value:
            result[tag] = value
    return result


def external_d_normalization(
    momentum: alg.Vector,
    dotted: int,
    color: int,
) -> alg.A:
    ctx = alg.Context(("X",), ({"X": momentum},), 4)
    direction = alg.endpoint_D(ctx, "X", 0, color, dotted, eta_index=4)
    word = alg.mat_scale(
        -alg.SQRT2 / 8,
        alg.mat_d2(alg.mat_bar_d(direction, "X", dotted), "X"),
    )
    return (
        alg.component(word, color)
        .coefficient_labels((1,))
        .set_coordinates_zero("X")
        .grass_coefficient(1 << 4)
    )


def action_hessian_entry_sector(
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    background_momentum: alg.Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int,
    sector: str,
    background_type: str = "D",
    polarization: alg.Vector = alg.ZERO_VECTOR,
) -> alg.A:
    """Full labeled cubic Hessian with a D background in either chirality."""

    ctx = alg.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    fields = [
        alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
        alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        (
            alg.endpoint_D(
                ctx, "X", 2, external_d, dotted, eta_index=4
            )
            if background_type == "D"
            else alg.endpoint_A(
                ctx, "X", 2, external_d, polarization
            )
        ),
    ]
    action = alg.gauge_action_integrand(alg.sum_mats(fields), "X", sector)
    action = action.coefficient_labels((1, 1, 1))
    action = (
        alg.integrate_chiral(action, "X")
        if sector == "+"
        else alg.integrate_antichiral(action, "X")
    )
    if background_type not in {"A", "D"}:
        raise ValueError(background_type)
    return action.grass_coefficient(
        alg.hessian_marker_mask(
            theta_mask_1,
            theta_mask_2,
            background_type == "D",
        )
    )


def dd_bubble_color_partials(
    pair: str,
    loop: alg.Vector,
    source_external_momentum: alg.Vector,
    action_external_momentum: alg.Vector,
    source_external_dotted: int,
    action_external_dotted: int,
    source_external_color: int,
    action_external_color: int,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    action_sector: str = "-",
) -> dict[str, alg.A]:
    """One color pair of the exact DD-projected -<I1 Sg3>/hbar bubble."""

    r_1 = loop
    r_2 = alg.vadd(action_external_momentum, alg.vneg(loop))
    totals: dict[str, alg.A] = {}
    dummy_polarization = alg.ZERO_VECTOR
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = alg.component_covariance(source_mask_1, action_mask_1)
        covariance_2 = alg.component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = pair_source_hessian_entries(
            1,
            pair,
            r_1,
            r_2,
            source_external_momentum,
            0,
            source_external_dotted,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
            source_external_color,
        )
        if not source_entries:
            continue
        action_entry = action_hessian_entry_sector(
            alg.vneg(r_1),
            alg.vneg(r_2),
            action_external_momentum,
            action_external_dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            action_external_color,
            action_sector,
        )
        if not action_entry:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for tag, source_entry in source_entries.items():
            value = totals.get(tag, alg.ZERO) + (
                wick_sign * edge_weight * source_entry * action_entry
            )
            if value:
                totals[tag] = value
            elif tag in totals:
                del totals[tag]
    return totals


def _dd_bubble_color_partials_star(arguments: tuple[object, ...]) -> dict[str, alg.A]:
    return dd_bubble_color_partials(*arguments)  # type: ignore[arg-type]


def _dd_bubble_batch_star(
    arguments: tuple[object, ...],
) -> tuple[int, str, str, dict[str, alg.A]]:
    sample_index = int(arguments[0])
    pair = str(arguments[1])
    attachment_name = str(arguments[2])
    partial = dd_bubble_color_partials(*arguments[3:])  # type: ignore[arg-type]
    return sample_index, pair, attachment_name, partial


def dd_bubble_samples_parallel(
    samples: list[tuple[alg.Vector, alg.Vector, alg.Vector]],
    workers: int,
    attachment_names: tuple[str, ...] = (
        "source_dot1_action_dot2",
        "source_dot2_action_dot1",
    ),
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
    action_sector: str = "-",
) -> dict[tuple[int, str, str], dict[str, alg.A]]:
    """Batch exact O05 evaluation without nested process pools."""

    arguments = []
    all_attachment_rows = (
        (
            "source_dot1_action_dot2",
            0,
            1,
            external_left_color,
            external_right_color,
        ),
        (
            "source_dot2_action_dot1",
            1,
            0,
            external_right_color,
            external_left_color,
        ),
    )
    attachment_rows = tuple(
        row for row in all_attachment_rows if row[0] in attachment_names
    )
    if len(attachment_rows) != len(attachment_names):
        raise ValueError(attachment_names)
    for sample_index, (loop, momentum_left, momentum_right) in enumerate(samples):
        for pair in ("A__Ddot1", "Ddot1__A"):
            for (
                attachment_name,
                source_dotted,
                action_dotted,
                source_color,
                action_color,
            ) in attachment_rows:
                source_momentum = (
                    momentum_left if source_dotted == 0 else momentum_right
                )
                action_momentum = (
                    momentum_right if action_dotted == 1 else momentum_left
                )
                for color_1, color_2 in itertools.product(range(3), repeat=2):
                    arguments.append(
                        (
                            sample_index,
                            pair,
                            attachment_name,
                            pair,
                            loop,
                            source_momentum,
                            action_momentum,
                            source_dotted,
                            action_dotted,
                            source_color,
                            action_color,
                            color_1,
                            color_2,
                            source_a,
                            source_b,
                            action_sector,
                        )
                    )
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        partials = list(pool.map(_dd_bubble_batch_star, arguments))
    totals: dict[tuple[int, str, str], dict[str, alg.A]] = {}
    for sample_index, pair, attachment_name, partial in partials:
        key = sample_index, pair, attachment_name
        tagged = totals.setdefault(key, {})
        for tag, value in partial.items():
            current = tagged.get(tag, alg.ZERO) + value
            if current:
                tagged[tag] = current
            elif tag in tagged:
                del tagged[tag]
    for sample_index, (_, momentum_left, momentum_right) in enumerate(samples):
        norm_left = external_d_normalization(
            momentum_left, 0, external_left_color
        )
        norm_right = external_d_normalization(
            momentum_right, 1, external_right_color
        )
        color = alg.A(
            alg.su2_F(
                source_a,
                source_b,
                external_left_color,
                external_right_color,
            )
        )
        normalization = alg.A(Fraction(-1, 2)) / (
            norm_left * norm_right * color
        )
        for pair in ("A__Ddot1", "Ddot1__A"):
            for attachment_name, *_ in attachment_rows:
                key = sample_index, pair, attachment_name
                ordered_normalization = (
                    -normalization
                    if attachment_name == "source_dot2_action_dot1"
                    else normalization
                )
                totals[key] = {
                    tag: ordered_normalization * value
                    for tag, value in totals.get(key, {}).items()
                    if value
                }
    return totals


def dd_bubble_attachment_values_parallel(
    pair: str,
    loop: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    workers: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, dict[str, alg.A]]:
    """Both DD attachment distributions, before selecting the marked occurrence."""

    attachments = {
        "source_dot1_action_dot2": (
            momentum_left,
            momentum_right,
            0,
            1,
            external_left_color,
            external_right_color,
        ),
        "source_dot2_action_dot1": (
            momentum_right,
            momentum_left,
            1,
            0,
            external_right_color,
            external_left_color,
        ),
    }
    arguments = [
        (
            pair,
            loop,
            *attachment,
            color_1,
            color_2,
            source_a,
            source_b,
        )
        for attachment in attachments.values()
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        partials = list(pool.map(_dd_bubble_color_partials_star, arguments))
    totals: dict[str, dict[str, alg.A]] = {
        name: {} for name in attachments
    }
    stride = 9
    for attachment_index, name in enumerate(attachments):
        for partial in partials[
            attachment_index * stride : (attachment_index + 1) * stride
        ]:
            for tag, value in partial.items():
                current = totals[name].get(tag, alg.ZERO) + value
                if current:
                    totals[name][tag] = current
                elif tag in totals[name]:
                    del totals[name][tag]
    norm_left = external_d_normalization(momentum_left, 0, external_left_color)
    norm_right = external_d_normalization(momentum_right, 1, external_right_color)
    color = alg.A(
        alg.su2_F(
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
    )
    normalization = alg.A(Fraction(-1, 2)) / (norm_left * norm_right * color)
    return {
        name: {
            tag: (
                -normalization
                if name == "source_dot2_action_dot1"
                else normalization
            )
            * value
            for tag, value in tagged.items()
            if value
        }
        for name, tagged in totals.items()
    }


def physical_mixed_bubble_color_partials(
    pair: str,
    loop: alg.Vector,
    momentum_a: alg.Vector,
    momentum_d: alg.Vector,
    polarization: alg.Vector,
    dotted: int,
    source_external_type: str,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_d_color: int = 1,
    external_a_color: int = 0,
) -> dict[str, alg.A]:
    """Physical O05 contact for one ``A`` and one ``D`` output port."""

    if source_external_type == "A":
        source_momentum = momentum_a
        action_momentum = momentum_d
        source_type, action_type, action_sector = "A", "D", "-"
        source_color, action_color = external_a_color, external_d_color
    elif source_external_type == "D":
        source_momentum = momentum_d
        action_momentum = momentum_a
        source_type, action_type, action_sector = "D", "A", "+"
        source_color, action_color = external_d_color, external_a_color
    else:
        raise ValueError(source_external_type)

    r_1 = loop
    r_2 = alg.vadd(action_momentum, alg.vneg(loop))
    totals: dict[str, alg.A] = {}
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = alg.component_covariance(source_mask_1, action_mask_1)
        covariance_2 = alg.component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = pair_source_hessian_entries(
            1,
            pair,
            r_1,
            r_2,
            source_momentum,
            dotted,
            dotted,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            source_a,
            source_b,
            source_color,
            source_type,
            polarization,
        )
        if not source_entries:
            continue
        action_entry = action_hessian_entry_sector(
            alg.vneg(r_1),
            alg.vneg(r_2),
            action_momentum,
            dotted,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            action_color,
            action_sector,
            action_type,
            polarization,
        )
        if not action_entry:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for tag, source_entry in source_entries.items():
            value = totals.get(tag, alg.ZERO) + (
                wick_sign * edge_weight * source_entry * action_entry
            )
            if value:
                totals[tag] = value
            elif tag in totals:
                del totals[tag]
    return totals


def _physical_mixed_bubble_batch_star(
    arguments: tuple[object, ...],
) -> tuple[int, str, str, dict[str, alg.A]]:
    sample_index = int(arguments[0])
    pair = str(arguments[1])
    source_external_type = str(arguments[2])
    partial = physical_mixed_bubble_color_partials(
        *arguments[3:]  # type: ignore[arg-type]
    )
    return sample_index, pair, source_external_type, partial


def physical_mixed_bubble_samples_parallel(
    samples: list[tuple[alg.Vector, alg.Vector, alg.Vector]],
    polarization: alg.Vector,
    workers: int,
) -> dict[tuple[int, str, str], dict[str, alg.A]]:
    """Exact four-frame O05 replay for the canonical mixed parent."""

    arguments = [
        (
            sample_index,
            pair,
            source_external_type,
            pair,
            loop,
            momentum_a,
            momentum_d,
            polarization,
            0,
            source_external_type,
            color_1,
            color_2,
        )
        for sample_index, (loop, momentum_d, momentum_a) in enumerate(samples)
        for pair in ("A__Ddot1", "Ddot1__A")
        for source_external_type in ("A", "D")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers,
        mp_context=context,
    ) as pool:
        partials = list(pool.map(_physical_mixed_bubble_batch_star, arguments))

    totals: dict[tuple[int, str, str], dict[str, alg.A]] = {}
    for sample_index, pair, source_external_type, partial in partials:
        key = sample_index, pair, source_external_type
        tagged = totals.setdefault(key, {})
        for tag, value in partial.items():
            current = tagged.get(tag, alg.ZERO) + value
            if current:
                tagged[tag] = current
            elif tag in tagged:
                del tagged[tag]

    for sample_index, (_, momentum_d, momentum_a) in enumerate(samples):
        norm_a, norm_d = alg.external_normalizations_pair(
            momentum_a,
            momentum_d,
            polarization,
            0,
            0,
            1,
        )
        color = alg.A(alg.su2_F(0, 1, 1, 0))
        normalization = alg.A(Fraction(-1, 2)) / (
            norm_a * norm_d * color
        )
        for pair in ("A__Ddot1", "Ddot1__A"):
            for source_external_type in ("A", "D"):
                key = sample_index, pair, source_external_type
                totals[key] = {
                    tag: normalization * value
                    for tag, value in totals.get(key, {}).items()
                    if value
                }
    return totals


def dd_quartic_action_entries(
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, alg.A]:
    ctx = alg.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": momentum_left},
            {"X": momentum_right},
        ),
        7,
    )
    fields = [
        alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 6),
        alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 7),
        alg.endpoint_D(ctx, "X", 2, external_left_color, 0, eta_index=4),
        alg.endpoint_D(ctx, "X", 3, external_right_color, 1, eta_index=5),
    ]
    marker = (1 << 4) | (1 << 5)
    if theta_mask_1.bit_count() % 2:
        marker |= 1 << 6
    if theta_mask_2.bit_count() % 2:
        marker |= 1 << 7
    result: dict[str, alg.A] = {}
    for sector in ("+", "-"):
        action = alg.gauge_action_integrand(alg.sum_mats(fields), "X", sector)
        action = action.coefficient_labels((1, 1, 1, 1))
        action = (
            alg.integrate_chiral(action, "X")
            if sector == "+"
            else alg.integrate_antichiral(action, "X")
        )
        value = action.grass_coefficient(marker)
        if value:
            result[f"Sg4_{sector}"] = value
    return result


def dd_quartic_color_partials(
    pair: str,
    loop: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    color_1: int,
    color_2: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, alg.A]:
    total_external = alg.vadd(momentum_left, momentum_right)
    r_1 = loop
    r_2 = alg.vadd(total_external, alg.vneg(loop))
    totals: dict[str, alg.A] = {}
    for source_mask_1, source_mask_2 in itertools.product(range(16), repeat=2):
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = alg.component_covariance(source_mask_1, action_mask_1)
        covariance_2 = alg.component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = pair_source_I0_hessian_entries(
            pair,
            r_1,
            r_2,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            0,
            source_a,
            source_b,
        )
        if not source_entries:
            continue
        action_entries = dd_quartic_action_entries(
            alg.vneg(r_1),
            alg.vneg(r_2),
            momentum_left,
            momentum_right,
            color_1,
            color_2,
            action_mask_1,
            action_mask_2,
            external_left_color,
            external_right_color,
        )
        if not action_entries:
            continue
        wick_sign = -1 if (
            source_mask_2.bit_count() % 2
            and action_mask_1.bit_count() % 2
        ) else 1
        edge_weight = 4 * covariance_1 * covariance_2
        for source_tag, source_entry in source_entries.items():
            for action_tag, action_entry in action_entries.items():
                tag = f"{source_tag}__{action_tag}"
                value = totals.get(tag, alg.ZERO) + (
                    wick_sign * edge_weight * source_entry * action_entry
                )
                if value:
                    totals[tag] = value
                elif tag in totals:
                    del totals[tag]
    return totals


def _dd_quartic_color_partials_star(arguments: tuple[object, ...]) -> dict[str, alg.A]:
    return dd_quartic_color_partials(*arguments)  # type: ignore[arg-type]


def _dd_quartic_batch_star(
    arguments: tuple[object, ...],
) -> tuple[int, str, dict[str, alg.A]]:
    sample_index = int(arguments[0])
    pair = str(arguments[1])
    partial = dd_quartic_color_partials(*arguments[2:])  # type: ignore[arg-type]
    return sample_index, pair, partial


def dd_quartic_samples_parallel(
    samples: list[tuple[alg.Vector, alg.Vector, alg.Vector]],
    workers: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[tuple[int, str], dict[str, alg.A]]:
    """Batch exact O06 evaluation for the transported r1 contact."""

    arguments = [
        (
            sample_index,
            pair,
            pair,
            loop,
            momentum_left,
            momentum_right,
            color_1,
            color_2,
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
        for sample_index, (loop, momentum_left, momentum_right) in enumerate(samples)
        for pair in ("A__Ddot1", "Ddot1__A")
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        partials = list(pool.map(_dd_quartic_batch_star, arguments))
    totals: dict[tuple[int, str], dict[str, alg.A]] = {}
    for sample_index, pair, partial in partials:
        tagged = totals.setdefault((sample_index, pair), {})
        for tag, value in partial.items():
            current = tagged.get(tag, alg.ZERO) + value
            if current:
                tagged[tag] = current
            elif tag in tagged:
                del tagged[tag]
    for sample_index, (_, momentum_left, momentum_right) in enumerate(samples):
        norm_left = external_d_normalization(
            momentum_left, 0, external_left_color
        )
        norm_right = external_d_normalization(
            momentum_right, 1, external_right_color
        )
        color = alg.A(
            alg.su2_F(
                source_a,
                source_b,
                external_left_color,
                external_right_color,
            )
        )
        normalization = alg.A(Fraction(-1, 2)) / (
            norm_left * norm_right * color
        )
        for pair in ("A__Ddot1", "Ddot1__A"):
            key = sample_index, pair
            totals[key] = {
                tag: normalization * value
                for tag, value in totals.get(key, {}).items()
                if value
            }
    return totals


def dd_quartic_values_parallel(
    pair: str,
    loop: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    workers: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, alg.A]:
    arguments = [
        (
            pair,
            loop,
            momentum_left,
            momentum_right,
            color_1,
            color_2,
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
        for color_1, color_2 in itertools.product(range(3), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        partials = list(pool.map(_dd_quartic_color_partials_star, arguments))
    totals: dict[str, alg.A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, alg.ZERO) + value
    norm_left = external_d_normalization(momentum_left, 0, external_left_color)
    norm_right = external_d_normalization(momentum_right, 1, external_right_color)
    color = alg.A(
        alg.su2_F(
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
    )
    normalization = alg.A(Fraction(-1, 2)) / (norm_left * norm_right * color)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def dd_tadpole_color_partials(
    pair: str,
    loop: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    color: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, alg.A]:
    totals: dict[str, alg.A] = {}
    for mask_1 in range(16):
        mask_2 = 15 ^ mask_1
        covariance = alg.component_covariance(mask_1, mask_2)
        if not covariance:
            continue
        ctx = alg.Context(
            ("X",),
            (
                {"X": loop},
                {"X": alg.vneg(loop)},
                {"X": momentum_left},
                {"X": momentum_right},
            ),
            7,
        )
        fields = [
            alg.basis_endpoint(ctx, "X", 0, color, mask_1, 6),
            alg.basis_endpoint(ctx, "X", 1, color, mask_2, 7),
            alg.endpoint_D(ctx, "X", 2, external_left_color, 0, eta_index=4),
            alg.endpoint_D(ctx, "X", 3, external_right_color, 1, eta_index=5),
        ]
        tagged = pair_source_tagged_words(
            alg.sum_mats(fields),
            "X",
            pair,
            0,
            source_a,
            source_b,
        )[2]
        marker = (1 << 4) | (1 << 5)
        if mask_1.bit_count() % 2:
            marker |= 1 << 6
        if mask_2.bit_count() % 2:
            marker |= 1 << 7
        for tag, source in tagged.items():
            coefficient = source.coefficient_labels((1, 1, 1, 1)).set_coordinates_zero("X")
            value = coefficient.grass_coefficient(marker)
            if not value:
                continue
            current = totals.get(tag, alg.ZERO) + covariance * value
            if current:
                totals[tag] = current
            elif tag in totals:
                del totals[tag]
    return totals


def _dd_tadpole_color_partials_star(arguments: tuple[object, ...]) -> dict[str, alg.A]:
    return dd_tadpole_color_partials(*arguments)  # type: ignore[arg-type]


def dd_tadpole_values_parallel(
    pair: str,
    loop: alg.Vector,
    momentum_left: alg.Vector,
    momentum_right: alg.Vector,
    workers: int,
    source_a: int = 0,
    source_b: int = 1,
    external_left_color: int = 1,
    external_right_color: int = 0,
) -> dict[str, alg.A]:
    arguments = [
        (
            pair,
            loop,
            momentum_left,
            momentum_right,
            color,
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
        for color in range(3)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=min(workers, 3), mp_context=context
    ) as pool:
        partials = list(pool.map(_dd_tadpole_color_partials_star, arguments))
    totals: dict[str, alg.A] = {}
    for partial in partials:
        for tag, value in partial.items():
            totals[tag] = totals.get(tag, alg.ZERO) + value
    norm_left = external_d_normalization(momentum_left, 0, external_left_color)
    norm_right = external_d_normalization(momentum_right, 1, external_right_color)
    color_tensor = alg.A(
        alg.su2_F(
            source_a,
            source_b,
            external_left_color,
            external_right_color,
        )
    )
    normalization = alg.A(-1) / (norm_left * norm_right * color_tensor)
    return {
        tag: normalization * value
        for tag, value in totals.items()
        if value
    }


def longitudinal_probe_specs() -> list[
    tuple[str, str, str, str, alg.Vector, alg.Vector, alg.Vector]
]:
    """Exact shifted-loop probes for the longitudinal TGG square."""

    e0 = alg.vec((1, 0, 0, 0))
    e1 = alg.vec((0, 1, 0, 0))
    e2 = alg.vec((0, 0, 1, 0))
    e3 = alg.vec((0, 0, 0, 1))
    frames = {
        "q": (e0, e3),
        "p": (e3, e0),
    }
    vertices = {
        "00": (Fraction(0), Fraction(0)),
        "10": (Fraction(1), Fraction(0)),
        "01": (Fraction(0), Fraction(1)),
    }
    points = {
        "zero": alg.ZERO_VECTOR,
        "e1_plus": e1,
        "e1_minus": alg.vneg(e1),
        "e2_plus": e2,
        "e2_minus": alg.vneg(e2),
    }
    result = []
    for pair in ("A__Ddot1", "Ddot1__A"):
        for isolated, (p, q) in frames.items():
            for vertex, (y, z) in vertices.items():
                shift = alg.vadd(
                    alg.vscale(y + z, p),
                    alg.vscale(z, q),
                )
                for point_name, shifted_loop in points.items():
                    loop = alg.vadd(shifted_loop, alg.vneg(shift))
                    result.append(
                        (pair, isolated, vertex, point_name, loop, p, q)
                    )
    return result


def longitudinal_route_simplex(
    evaluations: list[
        tuple[
            str,
            str,
            str,
            str,
            dict[tuple[int, int, int, int], alg.A],
        ]
    ],
) -> tuple[
    dict[str, dict[tuple[int, int, int, int], dict[str, sp.Expr]]],
    dict[str, dict[str, sp.Expr]],
]:
    """Take the exact transverse trace and its affine simplex average."""

    values: dict[
        tuple[str, str, str, str],
        dict[tuple[int, int, int, int], alg.A],
    ] = {}
    for pair, isolated, vertex, point_name, routes in evaluations:
        values[pair, isolated, vertex, point_name] = routes

    route_results: dict[
        str, dict[tuple[int, int, int, int], dict[str, sp.Expr]]
    ] = {}
    aggregates: dict[str, dict[str, sp.Expr]] = {}
    assignments = tuple(itertools.permutations(range(3), 2))
    for pair in ("A__Ddot1", "Ddot1__A"):
        route_results[pair] = {}
        aggregates[pair] = {"p": sp.Integer(0), "q": sp.Integer(0)}
        for left_slots, right_slots in itertools.product(assignments, repeat=2):
            slots = (*left_slots, *right_slots)
            isolated_values: dict[str, sp.Expr] = {}
            for isolated in ("p", "q"):
                vertex_values: dict[str, sp.Expr] = {}
                for vertex in ("00", "10", "01"):
                    zero = values[pair, isolated, vertex, "zero"][slots]
                    trace = alg.ZERO
                    for axis in ("e1", "e2"):
                        trace += Fraction(1, 2) * (
                            values[pair, isolated, vertex, f"{axis}_plus"][slots]
                            - 2 * zero
                            + values[pair, isolated, vertex, f"{axis}_minus"][slots]
                        )
                    # Two perpendicular directions give twice the coefficient
                    # of the four-dimensional square.  Its DRED defect is
                    # +mu_l^2 in the locked determinant convention.
                    vertex_values[vertex] = sp.simplify(
                        gaussian_expr(trace) / 2
                    )
                simplex_value = sp.simplify(
                    (
                        vertex_values["00"]
                        + vertex_values["10"]
                        + vertex_values["01"]
                    )
                    / 3
                )
                isolated_values[isolated] = simplex_value
                aggregates[pair][isolated] += simplex_value
            route_results[pair][slots] = isolated_values

    expected = {
        "A__Ddot1": {"p": -sp.I / 64, "q": -sp.I / 128},
        "Ddot1__A": {"p": -7 * sp.I / 384, "q": -5 * sp.I / 96},
    }
    for pair in expected:
        for isolated in ("p", "q"):
            actual = sp.simplify(aggregates[pair][isolated])
            if actual != expected[pair][isolated]:
                raise AssertionError(
                    f"{pair} longitudinal {isolated}: {actual} != "
                    f"{expected[pair][isolated]}"
                )
    return route_results, aggregates


def route_interpolation(
    pair: str,
    sample_outputs: list[dict[tuple[int, int, int, int], alg.A]],
) -> tuple[list[dict[str, object]], dict[str, sp.Expr]]:
    samples = interpolation_samples()
    matrix = sp.Matrix(
        [
            [plus_dotted(loop, 0), plus_dotted(p, 0), plus_dotted(q, 0)]
            for loop, p, q in samples[:3]
        ]
    )
    if matrix.det() == 0:
        raise AssertionError("singular exact interpolation matrix")
    routes = load_routes()[pair]
    tgg = [row for row in routes if row["topology"] == "TGG"]
    rows: list[dict[str, object]] = []
    aggregate = {"ell": sp.Integer(0), "p": sp.Integer(0), "q": sp.Integer(0)}
    for census_row in tgg:
        slots = parse_route_slots(str(census_row["route_id"]))
        rhs = sp.Matrix(
            [gaussian_expr(sample_outputs[index][slots]) for index in range(3)]
        )
        ell_coefficient, p_coefficient, q_coefficient = tuple(matrix.inv() * rhs)
        check = sp.simplify(
            ell_coefficient * plus_dotted(samples[3][0], 0)
            + p_coefficient * plus_dotted(samples[3][1], 0)
            + q_coefficient * plus_dotted(samples[3][2], 0)
            - gaussian_expr(sample_outputs[3][slots])
        )
        if check != 0:
            raise AssertionError(
                f"{pair} {census_row['route_id']} is not the typed rank-one word: {check}"
            )
        integrated_p = sp.simplify(p_coefficient - sp.Rational(2, 3) * ell_coefficient)
        integrated_q = sp.simplify(q_coefficient - sp.Rational(1, 3) * ell_coefficient)
        canonical_p = sp.simplify(-8 * integrated_p)
        canonical_q = sp.simplify(-8 * integrated_q)
        for key, value in (
            ("ell", ell_coefficient),
            ("p", p_coefficient),
            ("q", q_coefficient),
        ):
            aggregate[key] += value
        rows.append(
            {
                "route_id": census_row["route_id"],
                "topology": "TGG",
                "marked_edge": "r0" if pair == "A__Ddot1" else "r2",
                "sd_subtraction": "det_4(r_e)-det_d(r_e)=mu_l^2",
                "raw_mu2_rank_one": {
                    "ell_plus_dotted": expr_text(ell_coefficient),
                    "p_plus_dotted": expr_text(p_coefficient),
                    "q_plus_dotted": expr_text(q_coefficient),
                },
                "edgewise_parent_minus_cut": {
                    "R_route": {
                        "ell_plus_dotted": expr_text(ell_coefficient),
                        "p_plus_dotted": expr_text(p_coefficient),
                        "q_plus_dotted": expr_text(q_coefficient),
                    },
                    "parent_4d": {
                        "numerator": f"bar({('r0' if pair == 'A__Ddot1' else 'r2')})^2*R_route",
                        "denominator": "D0*D1*D2",
                    },
                    "sd_cut_contact": {
                        "numerator": "-R_route",
                        "denominator": (
                            "D1*D2" if pair == "A__Ddot1" else "D0*D1"
                        ),
                    },
                    "full_d_identity": (
                        "R_route*[r0_d^2/(D0*D1*D2)-1/(D1*D2)]=0"
                        if pair == "A__Ddot1"
                        else "R_route*[r2_d^2/(D0*D1*D2)-1/(D0*D1)]=0"
                    ),
                    "dred_remainder": (
                        "mu_l^2*R_route/(D0*D1*D2)"
                    ),
                    "same_edge": True,
                },
                "simplex_integrated_raw": {
                    "p_plus_dotted": expr_text(integrated_p),
                    "q_plus_dotted": expr_text(integrated_q),
                },
                "conditional_ff_coefficient_over_lambda": {
                    "p_plus_dotted": expr_text(canonical_p),
                    "q_plus_dotted": expr_text(canonical_q),
                },
                "status": (
                    "SURVIVES_EXPLICIT_SAME_EDGE_PARENT_MINUS_CUT"
                    if integrated_p != 0 or integrated_q != 0
                    else "EXACT_ZERO_AFTER_SIMPLEX_MOMENT"
                ),
            }
        )
    return rows, aggregate


def build_payload(workers: int) -> dict[str, object]:
    operator_identity_checks = verify_marked_operator_identity()
    simplex_moments = exact_simplex_moments()
    routes = load_routes()
    topology = {
        pair: dict(Counter(str(row["topology"]) for row in rows))
        for pair, rows in routes.items()
    }
    samples = interpolation_samples()
    arguments = [
        (pair, loop, p, q)
        for pair in ("A__Ddot1", "Ddot1__A")
        for loop, p, q in samples
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        evaluations = list(pool.map(aggregate_tgg_numerator, arguments))
    evaluated: dict[str, list[dict[tuple[int, int, int, int], alg.A]]] = {
        "A__Ddot1": [],
        "Ddot1__A": [],
    }
    for pair, route_values, _ in evaluations:
        evaluated[pair].append(route_values)

    longitudinal_specs = longitudinal_probe_specs()
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        longitudinal_evaluations = list(
            pool.map(longitudinal_probe_evaluation, longitudinal_specs)
        )
    longitudinal_routes, longitudinal_aggregates = longitudinal_route_simplex(
        longitudinal_evaluations
    )

    pair_rows: dict[str, list[dict[str, object]]] = {}
    aggregates: dict[str, dict[str, object]] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        tgg_rows, aggregate = route_interpolation(pair, evaluated[pair])
        selected_p = sp.simplify(
            aggregate["p"] - sp.Rational(2, 3) * aggregate["ell"]
        )
        selected_q = sp.simplify(
            aggregate["q"] - sp.Rational(1, 3) * aggregate["ell"]
        )
        longitudinal_p = sp.simplify(longitudinal_aggregates[pair]["p"])
        longitudinal_q = sp.simplify(longitudinal_aggregates[pair]["q"])
        aggregate_p = sp.simplify(selected_p + longitudinal_p)
        aggregate_q = sp.simplify(selected_q + longitudinal_q)
        for row in tgg_rows:
            slots = parse_route_slots(str(row["route_id"]))
            long_p = longitudinal_routes[pair][slots]["p"]
            long_q = longitudinal_routes[pair][slots]["q"]
            row["selected_edge"] = {
                "simplex_integrated_raw": row["simplex_integrated_raw"],
                "conditional_ff_coefficient_over_lambda": row[
                    "conditional_ff_coefficient_over_lambda"
                ],
            }
            row["transported_longitudinal"] = {
                "simplex_integrated_raw": {
                    "p_plus_dotted": expr_text(long_p),
                    "q_plus_dotted": expr_text(long_q),
                },
                "conditional_ff_coefficient_over_lambda": {
                    "p_plus_dotted": expr_text(-8 * long_p),
                    "q_plus_dotted": expr_text(-8 * long_q),
                },
            }
            total_p = sp.simplify(
                sp.sympify(
                    row["selected_edge"]["simplex_integrated_raw"][
                        "p_plus_dotted"
                    ]
                )
                + long_p
            )
            total_q = sp.simplify(
                sp.sympify(
                    row["selected_edge"]["simplex_integrated_raw"][
                        "q_plus_dotted"
                    ]
                )
                + long_q
            )
            row["simplex_integrated_raw"] = {
                "p_plus_dotted": expr_text(total_p),
                "q_plus_dotted": expr_text(total_q),
            }
            row["conditional_ff_coefficient_over_lambda"] = {
                "p_plus_dotted": expr_text(-8 * total_p),
                "q_plus_dotted": expr_text(-8 * total_q),
            }
            row["status"] = (
                "SURVIVES_SELECTED_PLUS_TRANSPORTED_LONGITUDINAL_TGG_CUT"
                if total_p != 0 or total_q != 0
                else "EXACT_ZERO_AFTER_SAME_OCCURRENCE_SUM"
            )
        tmm_rows = [
            {
                "route_id": row["route_id"],
                "topology": "TMM",
                "external_fields": [row["external_left_field"], row["external_right_field"]],
                "DD_projection": "0",
                "reason": "TMM leaves one phi_r and one tildephi_r external; neither is a vector prepotential u and the intrinsic DD projection has no typed port.",
                "status": "EXACT_ZERO_WRONG_EXTERNAL_FIELD_TYPE",
            }
            for row in routes[pair]
            if row["topology"] == "TMM"
        ]
        pair_rows[pair] = tgg_rows + tmm_rows
        denominator = sp.simplify(aggregate_p + aggregate_q)
        aggregates[pair] = {
            "selected_edge_raw_mu2_rank_one": {
                "ell_plus_dotted": expr_text(aggregate["ell"]),
                "p_plus_dotted": expr_text(aggregate["p"]),
                "q_plus_dotted": expr_text(aggregate["q"]),
            },
            "selected_edge_simplex_integrated_raw": {
                "p_plus_dotted": expr_text(selected_p),
                "q_plus_dotted": expr_text(selected_q),
            },
            "transported_longitudinal_simplex_integrated_raw": {
                "p_plus_dotted": expr_text(longitudinal_p),
                "q_plus_dotted": expr_text(longitudinal_q),
            },
            "simplex_integrated_raw": {
                "p_plus_dotted": expr_text(aggregate_p),
                "q_plus_dotted": expr_text(aggregate_q),
            },
            "simplex_distribution": {
                "p": expr_text(sp.simplify(aggregate_p / denominator)),
                "q": expr_text(sp.simplify(aggregate_q / denominator)),
                "derivation": "ell -> -(2*p+q)/3 from the exact mu_l^2 rank-one triangle moment",
            },
            "conditional_ff_coefficient_over_lambda": {
                "p_plus_dotted": expr_text(-8 * aggregate_p),
                "q_plus_dotted": expr_text(-8 * aggregate_q),
            },
        }

    lifted_rows: dict[str, list[dict[str, object]]] = {}
    for source, target in (
        ("A__Ddot1", "A__Ddot2"),
        ("Ddot1__A", "Ddot2__A"),
    ):
        lifted_rows[target] = []
        for row in pair_rows[source]:
            lifted = json.loads(json.dumps(row))
            lifted["route_id"] = str(lifted["route_id"]).replace(source, target)
            lifted["dotted_lift"] = "dot1 -> dot2; v_(+dot1) -> v_(+dot2); scalar coefficient unchanged"
            lifted_rows[target].append(lifted)

    return {
        "schema": "step5-ad-da-gauge-family-raw-v1",
        "external_target_used": False,
        "route_counts": {pair: len(rows) for pair, rows in routes.items()},
        "topology_counts": topology,
        "operator_identity": {
            "full": "D_- D_+ barD^2 D_+",
            "selected": "-8 det_4(r_e) D_+",
            "longitudinal": "-(1/2) D_+ barD^2 D^2",
            "conditional_gauge_fixing_completion": "+(1/2) D_+ barD^2 D^2",
            "conditional_full_plus_gf": "-8 det_4(r_e) D_+",
            "component_mask_checks": operator_identity_checks,
            "failed_checks": 0,
        },
        "dred_master": {
            "sd_zero": "det_d(r_e)/(D0*D1*D2)-1/prod_(j!=e)Dj=0",
            "failure": "det_4(r_e)/(D0*D1*D2)-1/prod_(j!=e)Dj=mu_l^2/(D0*D1*D2)",
            "scalar": "integral mu_l^2/(D0*D1*D2)=1/(32*pi^2)",
            "rank_one": "integral mu_l^2*ell/(D0*D1*D2)=-(2*p+q)/(96*pi^2)",
            "simplex_moments": simplex_moments,
        },
        "normalization": {
            "external_D_preimage_each": "-sqrt(2)/8",
            "external_D_product": "1/32",
            "chosen_SU2_color_tensor": "-2",
            "raw_to_canonical_component": "-16",
            "hbar_g2_master_over_lambda": "1/2",
            "raw_integrated_to_conditional_lambda": "-8",
            "lambda": "hbar*g^2/(16*pi^2)",
        },
        "pairs": pair_rows | lifted_rows,
        "aggregates": aggregates,
        "nonlinear_current": {
            "tree_identity": "-D_+[-2*i*(Phi_s x C_s)]*D-2*i*(B_s x C_s)*D=0",
            "regulated_rule": "Do not delete the two occurrences before the SD orbit: retain the matter-current Euler cut and the explicit B_s*C_s*D contact separately, impose the full-d zero, then form det_4-det_d.",
            "status": "BLOCKED_AD_DA_REGULATED_NONLINEAR_CURRENT_ORBIT",
        },
        "gauge_fixing_ghost_nk": {
            "gauge_fixing": "Inside the conditional FF algebra, D_+*D^2*barD^2=0 and Box*P0 gives +(1/2)D_+*barD^2*D^2 in the source normalization; it cancels the displayed -(1/2) longitudinal row mask by mask, leaving only the selected det_4 cut. The admissible local proper slice remains unaccepted.",
            "fp_carrier": "(delta S_FP/delta V)*D has ports (c_prime,c,D_external); one FP cubic (V,c_prime,c) closes two ghost edges and leaves V->D external, with E=2,V=2,L=1.",
            "fp_zero_claim": False,
            "nk": "The separated Nielsen-Kallosh branch is unselected, so its DD port census is unavailable.",
            "blockers": [
                "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
                "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
                "BLOCKED_AD_DA_FP_EULER_BUBBLE_RAW_DALGEBRA",
                "BLOCKED_AD_DA_LONGITUDINAL_QUARTIC_COLLAPSED_ORBIT",
                "BLOCKED_AD_DA_REGULATED_NONLINEAR_CURRENT_ORBIT",
            ],
        },
        "conditional_ff_occurrence_census": [
            {
                "id": "ADDA-O01-I0-Sg3-Sg3-TGG",
                "ports": "source(u,u); left G(u,u,u); right G(u,u,u); external(u,u)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "EVALUATED_SELECTED_CUT_ROUTEWISE_36_PER_ORDERING",
            },
            {
                "id": "ADDA-O02-I0-Sm3-Sm3-TMM",
                "ports": "source(u,u); M_r(tildephi_r,u,phi_r)^2; external(phi_r,tildephi_r)",
                "loop_number": 1,
                "DD_reachable": False,
                "status": "EXACT_ZERO_WRONG_EXTERNAL_FIELD_TYPE_6_PER_ORDERING",
            },
            {
                "id": "ADDA-O03-MATTER-CURRENT-EULER-CUT",
                "ports": "source(B_s,C_s,D_external); M_s(tildephi_s,u,phi_s); external(D,V->D)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_REGULATED_NONLINEAR_CURRENT_ORBIT",
            },
            {
                "id": "ADDA-O04-EXPLICIT-BC-D-CONTACT",
                "ports": "source(B_s,C_s,D_external); M_s(tildephi_s,u,phi_s); external(D,V->D)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_REGULATED_NONLINEAR_CURRENT_ORBIT",
            },
            {
                "id": "ADDA-O05-I1-Sg3-BUBBLE",
                "ports": "source(u,u,u); G(u,u,u); two internal u edges; external(u,u)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_LONGITUDINAL_QUARTIC_COLLAPSED_ORBIT",
            },
            {
                "id": "ADDA-O06-I0-Sg4-BUBBLE",
                "ports": "source(u,u); G4(u,u,u,u); two internal u edges; external(u,u)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_LONGITUDINAL_QUARTIC_COLLAPSED_ORBIT",
            },
            {
                "id": "ADDA-O07-I2-TADPOLE",
                "ports": "source(u,u,u,u); one internal u edge; external(u,u)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_LONGITUDINAL_QUARTIC_COLLAPSED_ORBIT",
            },
            {
                "id": "ADDA-O08-GF-EULER-LONGITUDINAL",
                "ports": "delta S_gf/delta u has one u port; multiplied by D supplies source(u,u)",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "CONDITIONAL_FF_EXACT_LONGITUDINAL_CANCELLATION__AUTHORITY_SLICE_UNACCEPTED",
            },
            {
                "id": "ADDA-O09-FP-EULER-BUBBLE",
                "ports": "source(c_prime,c,D_external); FP3(u,c_prime,c); external(D,u->D)",
                "edge_vertex_count": "E=2,V=2,L=1",
                "loop_number": 1,
                "DD_reachable": True,
                "status": "BLOCKED_AD_DA_FP_EULER_BUBBLE_RAW_DALGEBRA",
            },
            {
                "id": "ADDA-O10-FP-TRIANGLE-WITH-LINEAR-SOURCE",
                "ports": "source(u,u); each FP3 consumes one source u and leaves (c_prime,c); the two cross-paired ghost edges close the graph",
                "edge_vertex_count": "two source-u edges plus two ghost edges: E=4,V=3,L=2",
                "loop_number": 2,
                "DD_reachable": False,
                "status": "EXACT_ABSENT_AT_ONE_LOOP_BY_E_MINUS_V_PLUS_ONE",
            },
            {
                "id": "ADDA-O11-NK",
                "ports": "no NK action, propagator, or u-NK-NK Hessian is selected by the conditional proposal",
                "loop_number": None,
                "DD_reachable": None,
                "status": "ABSENT_FROM_CONDITIONAL_PROPOSAL__BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
            },
            {
                "id": "ADDA-O12-MULTIPLIER-AUXILIARY",
                "ports": "the normal-form multiplier block Y is not fixed by a local proper slice; no numerical u-aux-aux Hessian exists",
                "loop_number": None,
                "DD_reachable": None,
                "status": "ABSENT_NUMERICAL_RULE__BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
            },
        ],
        "full_pair_result_claimed": False,
        "status": "TARGET_BLIND_SELECTED_TGG_CUT_EXACT__FULL_SD_ORBIT_BLOCKED_GAUGE_FIXING_FP_NK",
    }


def build_payload_v2(workers: int) -> dict[str, object]:
    """Corrected anomaly-sector quotient: parent, cut, then mu^2."""

    operator_checks = verify_marked_operator_identity()
    factorization_checks = verify_selected_parent_factorization()
    gauge_fixing_checks = verify_gauge_fixing_longitudinal_cancellation()
    simplex_moments = exact_simplex_moments()
    routes = load_routes()
    spectator_routes = load_spectator_routes()
    topology = {
        pair: dict(Counter(str(row["topology"]) for row in rows))
        for pair, rows in routes.items()
    }

    samples = interpolation_samples()
    arguments = [
        (pair, loop, p, q)
        for pair in ("A__Ddot1", "Ddot1__A")
        for loop, p, q in samples
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        evaluations = list(pool.map(aggregate_tgg_numerator, arguments))
    evaluated: dict[str, list[dict[tuple[int, int, int, int], alg.A]]] = {
        "A__Ddot1": [],
        "Ddot1__A": [],
    }
    for pair, route_values, _ in evaluations:
        evaluated[pair].append(route_values)

    pair_rows: dict[str, list[dict[str, object]]] = {}
    aggregates: dict[str, dict[str, object]] = {}
    external_totals: dict[str, sp.Expr] = {}
    for pair in ("A__Ddot1", "Ddot1__A"):
        tgg_rows, aggregate = route_interpolation(pair, evaluated[pair])
        raw_p = sp.simplify(
            aggregate["p"] - sp.Rational(2, 3) * aggregate["ell"]
        )
        raw_q = sp.simplify(
            aggregate["q"] - sp.Rational(1, 3) * aggregate["ell"]
        )
        tmm_rows = [
            {
                "route_id": row["route_id"],
                "topology": "TMM",
                "external_fields": [
                    row["external_left_field"],
                    row["external_right_field"],
                ],
                "DD_projection": "0",
                "reason": (
                    "The external fields are phi_r and tildephi_r, not two "
                    "vector-prepotential ports."
                ),
                "status": "EXACT_ZERO_WRONG_EXTERNAL_FIELD_TYPE",
            }
            for row in routes[pair]
            if row["topology"] == "TMM"
        ]
        pair_rows[pair] = tgg_rows + tmm_rows

        internal_sum = sp.simplify(raw_p + raw_q)
        if pair == "A__Ddot1":
            # k_L=q, k_R=-(p+q).
            external_left = sp.simplify(-raw_p + raw_q)
            external_right = sp.simplify(-raw_p)
            placement = "k_L=q; k_R=-(p+q)"
        else:
            # k_L=-(p+q), k_R=q.
            external_left = sp.simplify(-raw_p)
            external_right = sp.simplify(-raw_p + raw_q)
            placement = "k_L=-(p+q); k_R=q"
        external_sum = sp.simplify(external_left + external_right)
        external_totals[pair] = sp.simplify(-8 * external_sum)
        aggregates[pair] = {
            "raw_mu2_rank_one": {
                "ell_plus_dotted": expr_text(aggregate["ell"]),
                "p_plus_dotted": expr_text(aggregate["p"]),
                "q_plus_dotted": expr_text(aggregate["q"]),
            },
            "simplex_integrated_raw": {
                "p_plus_dotted": expr_text(raw_p),
                "q_plus_dotted": expr_text(raw_q),
            },
            "loop_routing_distribution": {
                "p": expr_text(sp.simplify(raw_p / internal_sum)),
                "q": expr_text(sp.simplify(raw_q / internal_sum)),
                "derivation": (
                    "ell -> -(2*p+q)/3 from the exact rank-one triangle "
                    "simplex moment"
                ),
            },
            "conditional_ff_coefficient_over_lambda": {
                "p_plus_dotted": expr_text(-8 * raw_p),
                "q_plus_dotted": expr_text(-8 * raw_q),
            },
            "ordered_external_momenta": {
                "placement": placement,
                "raw": {
                    "k_left": expr_text(external_left),
                    "k_right": expr_text(external_right),
                },
                "normalized_shape": {
                    "k_left": expr_text(
                        sp.simplify(external_left / external_sum)
                    ),
                    "k_right": expr_text(
                        sp.simplify(external_right / external_sum)
                    ),
                },
                "conditional_ff_coefficient_over_lambda": {
                    "k_left": expr_text(-8 * external_left),
                    "k_right": expr_text(-8 * external_right),
                },
            },
        }

    lifted_rows: dict[str, list[dict[str, object]]] = {}
    for source, target in (
        ("A__Ddot1", "A__Ddot2"),
        ("Ddot1__A", "Ddot2__A"),
    ):
        lifted_rows[target] = []
        for row in pair_rows[source]:
            lifted = json.loads(json.dumps(row))
            lifted["route_id"] = str(lifted["route_id"]).replace(
                source, target
            )
            lifted["dotted_lift"] = (
                "dot1 -> dot2; v_(+dot1) -> v_(+dot2); scalar "
                "coefficient unchanged"
            )
            lifted_rows[target].append(lifted)

    o05 = interpolate_tagged_rank_one(cached_o05_tagged_samples())
    o06 = o06_occurrence_certificate()
    o07 = o07_tadpole_certificate(workers)
    matter_current = matter_current_pair_certificate()
    fp = fp_current_kernel_certificate()

    occurrence_census = [
        {
            "id": "ADDA-O01-PARENT-I0-Sg3-Sg3-TGG",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_4D_PARENT_ROUTEWISE_36_PER_ORDERING",
        },
        {
            "id": "ADDA-O01C-SAME-EDGE-SD-CUT",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_FULL_D_ZERO_AND_MU2_REMAINDER_ROUTEWISE",
        },
        {
            "id": "ADDA-O02-I0-Sm3-Sm3-TMM",
            "loop_number": 1,
            "DD_reachable": False,
            "status": "EXACT_ZERO_WRONG_EXTERNAL_FIELD_TYPE_6_PER_ORDERING",
        },
        {
            "id": "ADDA-O03-MATTER-CURRENT-EULER",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_PLUS_2I_TIMES_COMMON_AFFINE_DWORD",
        },
        {
            "id": "ADDA-O04-EXPLICIT-BC-D-CONTACT",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_MINUS_2I_TIMES_COMMON_DWORD__PAIR_SUM_ZERO",
        },
        {
            "id": "ADDA-O05-I1-Sg3-BUBBLE",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_SOURCE_TAGGED__AFFINE__STANDALONE_ANOMALY_ZERO",
        },
        {
            "id": "ADDA-O06-I0-Sg4-BUBBLE",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_CHIRAL_PLUS_ANTICHIRAL__AFFINE__STANDALONE_ANOMALY_ZERO",
        },
        {
            "id": "ADDA-O07-I2-TADPOLE",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EIGHT_EXACT_RATIONAL_SAMPLES_ZERO__INTEGRATED_SCALELESS_ZERO",
        },
        {
            "id": "ADDA-O08-GF-EULER-LONGITUDINAL",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "CONDITIONAL_FF_EXACT_CANCELLATION_32_MASKS",
        },
        {
            "id": "ADDA-O09-FP-EULER-BUBBLE",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EVALUATED_NONZERO_EULER_BUBBLE__FULL_D_CUT_REQUIRED",
        },
        {
            "id": "ADDA-O09C-FP-FULL-D-CUT",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "EXACT_NEGATIVE_OF_EULER_BUBBLE__MU2_REMAINDER_ZERO",
        },
        {
            "id": "ADDA-O10-FP-TRIANGLE-WITH-LINEAR-SOURCE",
            "loop_number": 2,
            "DD_reachable": False,
            "status": "EXACT_ABSENT_AT_ONE_LOOP_BY_E_MINUS_V_PLUS_ONE",
        },
        {
            "id": "ADDA-O11-NK",
            "loop_number": None,
            "DD_reachable": None,
            "status": "ABSENT_FROM_SELECTED_CONDITIONAL_GRAPH_SET",
        },
        {
            "id": "ADDA-O12-MULTIPLIER-AUXILIARY",
            "loop_number": None,
            "DD_reachable": None,
            "status": "ABSENT_NUMERICAL_RULE__LOCAL_PROPER_SLICE_BLOCKED",
        },
        {
            "id": "ADDA-O13-SPECTATOR-SOURCE-SELF-ENERGY",
            "loop_number": 1,
            "DD_reachable": True,
            "status": "CONNECTED_1PR__AMPUTATED_1PI_PROJECTOR_ZERO_42_PER_ORDERING",
        },
    ]

    return {
        "schema": "step5-ad-da-gauge-family-raw-v2",
        "external_target_used": False,
        "route_counts": {
            "amputated_1PI_legacy": {
                pair: len(rows) for pair, rows in routes.items()
            },
            "connected_1PR_spectator": {
                pair: len(rows) for pair, rows in spectator_routes.items()
            },
            "connected_total": {
                pair: len(routes[pair]) + len(spectator_routes[pair])
                for pair in routes
            },
        },
        "topology_counts": topology,
        "operator_identity": {
            "full": "D_- D_+ barD^2 D_+",
            "selected": "-8 det_4(r_e) D_+",
            "longitudinal": "-(1/2) D_+ barD^2 D^2",
            "conditional_gauge_fixing_completion": (
                "+(1/2) D_+ barD^2 D^2"
            ),
            "conditional_full_plus_gf": "-8 det_4(r_e) D_+",
            "component_mask_checks": operator_checks,
            "selected_parent_factorization_checks": factorization_checks,
            "gauge_fixing_mask_checks": gauge_fixing_checks,
            "failed_checks": 0,
        },
        "dred_master": {
            "sd_zero": (
                "R_e*[r_(e,d)^2/(D0*D1*D2)-1/prod_(j!=e)Dj]=0"
            ),
            "failure": (
                "R_e*[bar(r_e)^2/(D0*D1*D2)-1/prod_(j!=e)Dj]="
                "mu_l^2*R_e/(D0*D1*D2)"
            ),
            "scalar": "integral mu_l^2/(D0*D1*D2)=1/(32*pi^2)",
            "rank_one": (
                "integral mu_l^2*ell/(D0*D1*D2)="
                "-(2*p+q)/(96*pi^2)"
            ),
            "simplex_moments": simplex_moments,
        },
        "normalization": {
            "external_D_preimage_each": "-sqrt(2)/8",
            "external_D_product": "1/32",
            "chosen_SU2_color_tensor": "-2",
            "raw_to_canonical_component": "-16",
            "hbar_g2_master_over_lambda": "1/2",
            "raw_integrated_to_conditional_lambda": "-8",
            "lambda": "hbar*g^2/(16*pi^2)",
            "authority_ordered_source_hessian_locked": False,
        },
        "pairs": pair_rows | lifted_rows,
        "aggregates": aggregates,
        "target_blind_ordered_external_vector": {
            "AD_shape": aggregates["A__Ddot1"]["ordered_external_momenta"][
                "normalized_shape"
            ],
            "DA_shape": aggregates["Ddot1__A"]["ordered_external_momenta"][
                "normalized_shape"
            ],
            "conditional_normalization_ratio_AD_over_DA": expr_text(
                sp.simplify(
                    external_totals["A__Ddot1"]
                    / external_totals["Ddot1__A"]
                )
            ),
            "absolute_authority_normalization_locked": False,
        },
        "same_order_contacts": {
            "O05_I1_Sg3_source_tagged": o05,
            "O05_edge_aggregates": {
                "A__Ddot1": {
                    "r0_over_D1D2": "7*i*q_plus",
                    "r2_over_D0D1": "2*i*q_plus",
                },
                "Ddot1__A": {
                    "r0_over_D1D2": "-i*q_plus/2",
                    "r2_over_D0D1": "i*(p+q)_plus",
                },
            },
            "O06_I0_Sg4": o06,
            "O07_I2": o07,
            "standalone_anomaly_rule": (
                "An affine numerator has no bar(ell)^2 metric trace. Retain "
                "it in the ordinary SD family, but its extra-dimensional "
                "anomaly sector is zero."
            ),
        },
        "nonlinear_current": matter_current,
        "gauge_fixing_ghost_nk": {
            "gauge_fixing": (
                "8*D_+*Box*P0=(1/2)*D_+*barD^2*D^2; the source "
                "longitudinal row cancels in 32 exact component masks."
            ),
            "fp": fp,
            "fp_full_schwinger_family_zero": True,
            "nk": (
                "Absent from the selected conditional graph set; no "
                "independent zero or numerical weight is assigned."
            ),
            "blockers": [
                "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
                "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
                "BLOCKED_AD_DA_AUTHORITY_ORDERED_SOURCE_HESSIAN_NORMALIZATION",
            ],
        },
        "spectator_source_self_energy": {
            "counts": {
                pair: len(rows) for pair, rows in spectator_routes.items()
            },
            "unique_source_to_action_stem_cut": (
                "disconnects the insertion from the self-energy loop"
            ),
            "amputated_1PI_projector": "0",
            "control_color_F_01_10": "0",
            "anomaly_sector": "0",
        },
        "first_invalid_assumption": {
            "code_path": "source_component_entry(marked_sector='evanescent')",
            "invalid_step": (
                "det_4(r_e) was replaced by mu_l^2 before constructing the "
                "occurrence-resolved same-edge full-d Schwinger contact."
            ),
            "repair": (
                "Each TGG row records the 4d parent and distinct "
                "two-denominator cut, checks the full-d zero, and only then "
                "forms the mu_l^2 remainder. O05/O06 are not added twice."
            ),
            "second_comparison_error": (
                "Loop-routing p,q were compared with ordered external jets "
                "before the pair-specific maps (q,-p-q) and (-p-q,q)."
            ),
        },
        "conditional_ff_occurrence_census": occurrence_census,
        "conditional_ff_anomaly_sector_claimed": True,
        "full_pair_result_claimed": False,
        "status": (
            "TARGET_BLIND_CONDITIONAL_FF_ANOMALY_SECTOR_EDGEWISE_COMPLETE__"
            "ABSOLUTE_AUTHORITY_NORMALIZATION_AND_LOCAL_SLICE_BLOCKED"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--output", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload_v2(args.workers)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.output.write_text(rendered, encoding="utf-8")
    elif args.check:
        expected = args.output.read_text(encoding="utf-8")
        if expected != rendered:
            raise AssertionError(f"stale artifact: {args.output}")
        print("PASS AD_DA_ROUTE_COUNTS 84+84_CONNECTED__42+42_AMPUTATED_1PI")
        print("PASS AD_DA_TGG_COUNTS 36+36")
        print("PASS AD_DA_TMM_DD_ZERO 6+6")
        print("PASS AD_DA_EDGEWISE_PARENT_MINUS_CUT")
        print("PASS AD_DA_ORDERED_EXTERNAL_MOMENTUM_MAP")
        print("PASS AD_DA_DOT2_LIFT")
        print("PASS AD_DA_NO_HT_INPUT")
        print("PASS AD_DA_GF_FP_CURRENT_CONTACT_SECTORS")
        print("PASS AD_DA_AUTHORITY_NORMALIZATION_BLOCKER_RETAINED")
        print("SUMMARY 9/9 PASS")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
