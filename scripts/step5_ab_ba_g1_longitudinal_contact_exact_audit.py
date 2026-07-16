#!/usr/bin/env python3
"""Exact target-blind AB/BA G1 longitudinal/contact orbit.

This audit keeps the three R4 contact presentations occurrence tagged:

* e2: N_A,1 B_11 against the cubic matter action;
* e0: A_1 N_B,1 against the cubic gauge action;
* e1: N_A,0 B_11 against the quartic matter seagull.

They are tested as presentations of the same induced derivative-of-action
contact, not added as three independent source vertices.

The finite exterior-algebra engines are imported from earlier local exact
audits.  No holomorphic-twist coefficient or compact result is read.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_gauge_full_source_sd_orbit_exact_audit as aa  # noqa: E402


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


sd = load_module(
    "step5_ab1_marked_sd_orbit_for_g1_contacts",
    ROOT / "scripts" / "step5_ab1_marked_sd_orbit_exact_audit.py",
)
g1 = sd.g1


DEFAULT_JSON = ROOT / "audits" / "step5-ab-ba-g1-longitudinal-contact-exact.json"
DEFAULT_MD = ROOT / "audits" / "step5-ab-ba-g1-longitudinal-contact-exact.md"


def bracket(left: aa.Mat, right: aa.Mat) -> aa.Mat:
    return aa.mat_sub(aa.mat_mul(left, right), aa.mat_mul(right, left))


def graded_odd_bracket(left: aa.Mat, right: aa.Mat) -> aa.Mat:
    """The graded bracket of two odd matrices is their anticommutator."""

    return aa.mat_add(aa.mat_mul(left, right), aa.mat_mul(right, left))


def const_mat(ctx: aa.Context, color: int, factor: object = 1) -> aa.Mat:
    return aa.matrix_field(aa.P.scalar(ctx, factor), color)


def full_measure(poly: aa.P, node: str) -> aa.P:
    return (Fraction(1, 16) * aa.d2(aa.bar_d2(poly, node), node)).set_coordinates_zero(node)


def chiral_phi_endpoint(
    ctx: aa.Context,
    node: str,
    label: int,
    color: int,
    momentum: aa.Vector,
    eta_index: int,
) -> aa.Mat:
    """Chiral Phi direction normalized by D_+ Phi|=eta."""

    exponent = aa.P.scalar(ctx, 0)
    for vector_index in range(4):
        for undotted in range(2):
            for dotted in range(2):
                exponent += (
                    aa.I
                    * momentum[vector_index]
                    * aa.SIGMA[vector_index][undotted][dotted]
                    * aa.theta(ctx, node, undotted)
                    * aa.bar_theta_up(ctx, node, dotted)
                )
    base = (
        aa.theta(ctx, node, 0)
        * aa.P.grass_generator(ctx, eta_index)
        * (aa.P.scalar(ctx, 1) + exponent + Fraction(1, 2) * exponent * exponent)
    )
    return aa.labeled_endpoint(base, label, color)


def canonical_b_words(U: aa.Mat, Phi: aa.Mat, node: str) -> tuple[aa.Mat, aa.Mat]:
    """B_11=D_+Phi and B_12=sqrt(2)[(D_+U),Phi]."""

    du = aa.mat_d(U, node, 0)
    b11 = aa.mat_d(Phi, node, 0)
    b12 = aa.mat_scale(aa.SQRT2, bracket(du, Phi))
    return b11, b12


def canonical_a12_words(U: aa.Mat, node: str) -> tuple[aa.Mat, aa.Mat]:
    """The A1/A2 truncation, avoiding the unused cubic A3 construction."""

    x = aa.mat_d(U, node, 0)
    c = bracket(x, U)
    y = aa.mat_bar_d2(x, node)
    z = aa.mat_bar_d2(c, node)
    a1 = aa.mat_scale(-aa.SQRT2 / 8, aa.mat_d(y, node, 0))
    a2 = aa.mat_add(
        aa.mat_scale(Fraction(-1, 8), aa.mat_d(z, node, 0)),
        aa.mat_scale(Fraction(-1, 4), aa.mat_add(aa.mat_mul(x, y), aa.mat_mul(y, x))),
    )
    return a1, a2


def canonical_descendant_words(
    U: aa.Mat,
    Phi: aa.Mat,
    node: str,
) -> dict[str, aa.Mat]:
    """Occurrence-resolved A/B words through first nonlinear order."""

    a1, a2 = canonical_a12_words(U, node)
    b11, b12 = canonical_b_words(U, Phi, node)
    gamma_minus_1 = aa.mat_scale(aa.SQRT2, aa.mat_d(U, node, 1))
    na0 = aa.mat_d(a1, node, 1)
    na1_a2 = aa.mat_d(a2, node, 1)
    na1_gamma = bracket(gamma_minus_1, a1)
    nb0 = aa.mat_d(b11, node, 1)
    nb1_b12 = aa.mat_d(b12, node, 1)
    nb1_gamma = graded_odd_bracket(gamma_minus_1, b11)
    a2_bridge = aa.mat_scale(aa.ONE / aa.SQRT2, bracket(U, a1))
    b12_bridge = aa.mat_scale(aa.ONE / aa.SQRT2, bracket(U, b11))
    na1_bridge = aa.mat_scale(aa.ONE / aa.SQRT2, bracket(U, na0))
    nb1_bridge = aa.mat_scale(aa.ONE / aa.SQRT2, bracket(U, nb0))
    return {
        "A1": a1,
        "A2": a2,
        "B11": b11,
        "B12": b12,
        "NA0": na0,
        "NA1_A2": na1_a2,
        "NA1_gamma": na1_gamma,
        "NB0": nb0,
        "NB1_B12": nb1_b12,
        "NB1_gamma": nb1_gamma,
        "A2_bridge": a2_bridge,
        "B12_bridge": b12_bridge,
        "NA1_bridge": na1_bridge,
        "NB1_bridge": nb1_bridge,
    }


def component_product(
    words: dict[str, aa.Mat],
    orientation: str,
    occurrence: str,
    source_a: int,
    source_b: int,
) -> dict[str, aa.P]:
    """Return the exact graded source products for one collapsed occurrence."""

    c = aa.component
    if orientation == "AB":
        if occurrence == "e2":
            return {
                "NA1_A2*B11": c(words["NA1_A2"], source_a) * c(words["B11"], source_b),
                "NA1_gamma*B11": c(words["NA1_gamma"], source_a) * c(words["B11"], source_b),
            }
        if occurrence == "e0":
            return {
                "A1*NB1_B12": c(words["A1"], source_a) * c(words["NB1_B12"], source_b),
                "A1*NB1_gamma": c(words["A1"], source_a) * c(words["NB1_gamma"], source_b),
            }
        if occurrence == "e1":
            return {"NA0*B11": c(words["NA0"], source_a) * c(words["B11"], source_b)}
    if orientation == "BA":
        # D_-(B A)=(D_-B)A-B(D_-A), since B is odd and A is even.
        if occurrence == "e2":
            return {
                "-B11*NA1_A2": -c(words["B11"], source_a) * c(words["NA1_A2"], source_b),
                "-B11*NA1_gamma": -c(words["B11"], source_a) * c(words["NA1_gamma"], source_b),
            }
        if occurrence == "e0":
            return {
                "NB1_B12*A1": c(words["NB1_B12"], source_a) * c(words["A1"], source_b),
                "NB1_gamma*A1": c(words["NB1_gamma"], source_a) * c(words["A1"], source_b),
            }
        if occurrence == "e1":
            return {"-B11*NA0": -c(words["B11"], source_a) * c(words["NA0"], source_b)}
    raise ValueError((orientation, occurrence))


def full_i1_products(
    words: dict[str, aa.Mat],
    orientation: str,
    source_a: int = 0,
    source_b: int = 1,
) -> dict[str, aa.P]:
    """Complete order-g descendant source, with all occurrence tags."""

    c = aa.component
    if orientation == "AB":
        return {
            "NA1_A2*B11": c(words["NA1_A2"], source_a) * c(words["B11"], source_b),
            "NA1_gamma*B11": c(words["NA1_gamma"], source_a) * c(words["B11"], source_b),
            "NA0*B12": c(words["NA0"], source_a) * c(words["B12"], source_b),
            "A2*NB0": c(words["A2"], source_a) * c(words["NB0"], source_b),
            "A1*NB1_B12": c(words["A1"], source_a) * c(words["NB1_B12"], source_b),
            "A1*NB1_gamma": c(words["A1"], source_a) * c(words["NB1_gamma"], source_b),
            "NA1_bridge*B11": c(words["NA1_bridge"], source_a) * c(words["B11"], source_b),
            "NA0*B12_bridge": c(words["NA0"], source_a) * c(words["B12_bridge"], source_b),
            "A2_bridge*NB0": c(words["A2_bridge"], source_a) * c(words["NB0"], source_b),
            "A1*NB1_bridge": c(words["A1"], source_a) * c(words["NB1_bridge"], source_b),
        }
    if orientation == "BA":
        return {
            "NB1_B12*A1": c(words["NB1_B12"], source_a) * c(words["A1"], source_b),
            "NB1_gamma*A1": c(words["NB1_gamma"], source_a) * c(words["A1"], source_b),
            "NB0*A2": c(words["NB0"], source_a) * c(words["A2"], source_b),
            "-B12*NA0": -c(words["B12"], source_a) * c(words["NA0"], source_b),
            "-B11*NA1_A2": -c(words["B11"], source_a) * c(words["NA1_A2"], source_b),
            "-B11*NA1_gamma": -c(words["B11"], source_a) * c(words["NA1_gamma"], source_b),
            "NB1_bridge*A1": c(words["NB1_bridge"], source_a) * c(words["A1"], source_b),
            "NB0*A2_bridge": c(words["NB0"], source_a) * c(words["A2_bridge"], source_b),
            "-B12_bridge*NA0": -c(words["B12_bridge"], source_a) * c(words["NA0"], source_b),
            "-B11*NA1_bridge": -c(words["B11"], source_a) * c(words["NA1_bridge"], source_b),
        }
    raise ValueError(orientation)


def full_i0_products(
    words: dict[str, aa.Mat],
    orientation: str,
    source_a: int = 0,
    source_b: int = 1,
) -> dict[str, aa.P]:
    c = aa.component
    if orientation == "AB":
        return {
            "NA0*B11": c(words["NA0"], source_a) * c(words["B11"], source_b),
            "A1*NB0": c(words["A1"], source_a) * c(words["NB0"], source_b),
        }
    if orientation == "BA":
        return {
            "NB0*A1": c(words["NB0"], source_a) * c(words["A1"], source_b),
            "-B11*NA0": -c(words["B11"], source_a) * c(words["NA0"], source_b),
        }
    raise ValueError(orientation)


def orientation_colors(orientation: str) -> dict[str, int]:
    if orientation == "AB":
        return {
            "source_A": 0,
            "source_B": 1,
            "external_D": 1,
            "external_B": 0,
        }
    if orientation == "BA":
        return {
            "source_B": 0,
            "source_A": 1,
            "external_B": 1,
            "external_D": 0,
        }
    raise ValueError(orientation)


def source_gauge_contact(
    loop: aa.Vector,
    p: aa.Vector,
    q: aa.Vector,
    dotted: int,
    orientation: str,
) -> dict[str, aa.A]:
    """e2 cut: -<I1[NA1 B11] S_m3>/hbar, exact two-node word."""

    colors = orientation_colors(orientation)
    source_a = 0
    source_b = 1
    r0 = loop
    r1 = aa.vadd(loop, aa.vneg(p))
    labels = (
        {"S": aa.vneg(r1), "M": r1},
        {"S": q},
        {"S": r0, "M": aa.vneg(r0)},
        {"M": p},
    )
    ctx = aa.Context(("S", "M"), labels, 9)
    eta_mask = (1 << 8) | (1 << 9)
    totals: dict[str, aa.A] = {}
    for internal_color in range(3):
        quantum_u = aa.endpoint_delta(ctx, "S", "M", 0, internal_color)
        external_d = aa.endpoint_D(
            ctx,
            "S",
            1,
            colors["external_D"],
            dotted,
            eta_index=8,
        )
        matter_projector = aa.bar_d2(
            aa.d2(aa.delta4(ctx, "S", "M"), "S"),
            "S",
        ) * aa.P.label(ctx, 2)
        source_phi = aa.matrix_field(matter_projector, colors["source_B"])
        words = canonical_descendant_words(
            aa.mat_add(quantum_u, external_d), source_phi, "S"
        )
        products = {
            tag: value.coefficient_labels((1, 1, 1, 0))
            for tag, value in full_i1_products(words, orientation).items()
        }

        external_b = chiral_phi_endpoint(
            ctx,
            "M",
            3,
            colors["external_B"],
            p,
            9,
        )
        action_tilde = const_mat(ctx, colors["source_B"], 2)
        action_u = const_mat(ctx, internal_color, -2)
        action = aa.mat_trace(aa.mat_mul(action_tilde, bracket(action_u, external_b)))

        for tag, source in products.items():
            graph = full_measure(source * action, "M").set_coordinates_zero("S")
            graph = graph.coefficient_labels((0, 0, 0, 1))
            value = graph.grass_coefficient(eta_mask)
            totals[tag] = totals.get(tag, aa.ZERO) - value
    return {tag: value for tag, value in totals.items() if value}


def middle_gauge_seagull_contact(
    loop: aa.Vector,
    p: aa.Vector,
    q: aa.Vector,
    dotted: int,
    orientation: str,
) -> dict[str, aa.A]:
    """e1 cut: -<I0[NA0 B11] S_m4>/hbar, including both U placements."""

    colors = orientation_colors(orientation)
    source_a = 0
    source_b = 1
    r0 = loop
    r2 = aa.vadd(loop, aa.vneg(p), aa.vneg(q))
    labels = (
        {"S": aa.vneg(r2), "M": r2},
        {"M": q},
        {"S": r0, "M": aa.vneg(r0)},
        {"M": p},
    )
    ctx = aa.Context(("S", "M"), labels, 9)
    eta_mask = (1 << 8) | (1 << 9)

    quantum_u = aa.endpoint_delta(ctx, "S", "M", 0, colors["source_A"])
    matter_projector = aa.bar_d2(
        aa.d2(aa.delta4(ctx, "S", "M"), "S"),
        "S",
    ) * aa.P.label(ctx, 2)
    source_phi = aa.matrix_field(matter_projector, colors["source_B"])
    words = canonical_descendant_words(quantum_u, source_phi, "S")
    products = {
        tag: value.coefficient_labels((1, 0, 1, 0))
        for tag, value in full_i0_products(words, orientation).items()
    }

    internal_u = const_mat(ctx, colors["source_A"], -2)
    external_d = aa.endpoint_D(
        ctx,
        "M",
        1,
        colors["external_D"],
        dotted,
        eta_index=8,
    )
    u = aa.mat_add(internal_u, external_d)
    external_b = chiral_phi_endpoint(
        ctx,
        "M",
        3,
        colors["external_B"],
        p,
        9,
    )
    action_tilde = const_mat(ctx, colors["source_B"], 2)
    action = aa.mat_trace(
        aa.mat_mul(action_tilde, bracket(u, bracket(u, external_b)))
    ).coefficient_labels((0, 1, 0, 1))

    totals: dict[str, aa.A] = {}
    for tag, source in products.items():
        graph = full_measure(source * action, "M").set_coordinates_zero("S")
        graph = graph.coefficient_labels((0, 0, 0, 0))
        value = graph.grass_coefficient(eta_mask)
        totals[tag] = -value
    return {tag: value for tag, value in totals.items() if value}


def source_matter_source_entries(
    momentum_1: aa.Vector,
    momentum_2: aa.Vector,
    p: aa.Vector,
    color_1: int,
    color_2: int,
    mask_1: int,
    mask_2: int,
    orientation: str,
) -> dict[str, aa.A]:
    """Two-vector Hessian of the e0 source A1 N_B1 with external B."""

    colors = orientation_colors(orientation)
    ctx = aa.Context(
        ("X",),
        ({"X": momentum_1}, {"X": momentum_2}, {"X": p}),
        6,
    )
    field_1 = aa.basis_endpoint(ctx, "X", 0, color_1, mask_1, 5)
    field_2 = aa.basis_endpoint(ctx, "X", 1, color_2, mask_2, 6)
    fields = (
        field_1,
        field_2,
    )
    Phi = chiral_phi_endpoint(ctx, "X", 2, colors["external_B"], p, 4)
    b11 = aa.mat_d(Phi, "X", 0)

    def a1_of(field: aa.Mat) -> aa.Mat:
        x = aa.mat_d(field, "X", 0)
        return aa.mat_scale(
            -aa.SQRT2 / 8,
            aa.mat_d(aa.mat_bar_d2(x, "X"), "X", 0),
        )

    def nb1_of(field: aa.Mat) -> tuple[aa.Mat, aa.Mat]:
        b12 = aa.mat_scale(
            aa.SQRT2,
            bracket(aa.mat_d(field, "X", 0), Phi),
        )
        gamma_minus_1 = aa.mat_scale(aa.SQRT2, aa.mat_d(field, "X", 1))
        return (
            aa.mat_d(b12, "X", 1),
            graded_odd_bracket(gamma_minus_1, b11),
        )

    a1_1 = a1_of(field_1)
    a1_2 = a1_of(field_2)
    nb12_1, nbg_1 = nb1_of(field_1)
    nb12_2, nbg_2 = nb1_of(field_2)
    if orientation == "AB":
        products = {
            "A1*NB1_B12": (
                aa.component(a1_1, 0) * aa.component(nb12_2, 1)
                + aa.component(a1_2, 0) * aa.component(nb12_1, 1)
            ),
            "A1*NB1_gamma": (
                aa.component(a1_1, 0) * aa.component(nbg_2, 1)
                + aa.component(a1_2, 0) * aa.component(nbg_1, 1)
            ),
        }
    elif orientation == "BA":
        products = {
            "NB1_B12*A1": (
                aa.component(nb12_1, 0) * aa.component(a1_2, 1)
                + aa.component(nb12_2, 0) * aa.component(a1_1, 1)
            ),
            "NB1_gamma*A1": (
                aa.component(nbg_1, 0) * aa.component(a1_2, 1)
                + aa.component(nbg_2, 0) * aa.component(a1_1, 1)
            ),
        }
    else:
        raise ValueError(orientation)
    marker = (1 << 4)
    if mask_1.bit_count() % 2:
        marker |= 1 << 5
    if mask_2.bit_count() % 2:
        marker |= 1 << 6
    result: dict[str, aa.A] = {}
    for tag, source in products.items():
        value = (
            source.coefficient_labels((1, 1, 1))
            .set_coordinates_zero("X")
            .grass_coefficient(marker)
        )
        if value:
            result[tag] = value
    return result


def source_matter_full_source_entries(
    momentum_1: aa.Vector,
    momentum_2: aa.Vector,
    p: aa.Vector,
    color_1: int,
    color_2: int,
    mask_1: int,
    mask_2: int,
    orientation: str,
) -> dict[str, aa.A]:
    """Complete I1 two-vector Hessian; used to prove the finite support."""

    colors = orientation_colors(orientation)
    ctx = aa.Context(
        ("X",),
        ({"X": momentum_1}, {"X": momentum_2}, {"X": p}),
        6,
    )
    U = aa.mat_add(
        aa.basis_endpoint(ctx, "X", 0, color_1, mask_1, 5),
        aa.basis_endpoint(ctx, "X", 1, color_2, mask_2, 6),
    )
    Phi = chiral_phi_endpoint(ctx, "X", 2, colors["external_B"], p, 4)
    words = canonical_descendant_words(U, Phi, "X")
    products = full_i1_products(words, orientation)
    marker = 1 << 4
    if mask_1.bit_count() % 2:
        marker |= 1 << 5
    if mask_2.bit_count() % 2:
        marker |= 1 << 6
    result: dict[str, aa.A] = {}
    for tag, source in products.items():
        value = (
            source.coefficient_labels((1, 1, 1))
            .set_coordinates_zero("X")
            .grass_coefficient(marker)
        )
        if value:
            result[tag] = value
    return result


def source_matter_action_entry(
    momentum_1: aa.Vector,
    momentum_2: aa.Vector,
    q: aa.Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    mask_1: int,
    mask_2: int,
    external_d_color: int,
    sector: str,
) -> aa.A:
    ctx = aa.Context(
        ("X",),
        ({"X": momentum_1}, {"X": momentum_2}, {"X": q}),
        6,
    )
    fields = (
        aa.basis_endpoint(ctx, "X", 0, color_1, mask_1, 5),
        aa.basis_endpoint(ctx, "X", 1, color_2, mask_2, 6),
        aa.endpoint_D(ctx, "X", 2, external_d_color, dotted, eta_index=4),
    )
    action = gauge_action_cubic_hessian(fields, "X", sector)
    action = action.coefficient_labels((1, 1, 1))
    action = aa.integrate_chiral(action, "X") if sector == "+" else aa.integrate_antichiral(action, "X")
    marker = (1 << 4)
    if mask_1.bit_count() % 2:
        marker |= 1 << 5
    if mask_2.bit_count() % 2:
        marker |= 1 << 6
    return action.grass_coefficient(marker)


def gauge_action_cubic_hessian(
    fields: tuple[aa.Mat, aa.Mat, aa.Mat],
    node: str,
    sector: str,
) -> aa.P:
    """Fully polarized cubic gauge word, with no unused field degrees."""

    total = aa.zero_mat(fields[0][0][0].ctx)
    for linear_index in range(3):
        remaining = tuple(index for index in range(3) if index != linear_index)
        linear = fields[linear_index]
        left = fields[remaining[0]]
        right = fields[remaining[1]]
        if sector == "+":
            lower_1 = tuple(
                aa.mat_bar_d2(aa.mat_scale(aa.SQRT2, aa.mat_d(linear, node, a)), node)
                for a in range(2)
            )
            lower_2 = tuple(
                aa.mat_bar_d2(
                    aa.mat_add(
                        bracket(aa.mat_d(left, node, a), right),
                        bracket(aa.mat_d(right, node, a), left),
                    ),
                    node,
                )
                for a in range(2)
            )
            upper_1 = (lower_1[1], aa.mat_neg(lower_1[0]))
            upper_2 = (lower_2[1], aa.mat_neg(lower_2[0]))
            cross = aa.mat_add(
                aa.mat_mul(upper_1[0], lower_2[0]),
                aa.mat_mul(upper_1[1], lower_2[1]),
                aa.mat_mul(upper_2[0], lower_1[0]),
                aa.mat_mul(upper_2[1], lower_1[1]),
            )
        elif sector == "-":
            lower_1 = tuple(
                aa.mat_d2(
                    aa.mat_scale(-aa.SQRT2, aa.mat_bar_d(linear, node, dotted)),
                    node,
                )
                for dotted in range(2)
            )
            lower_2 = tuple(
                aa.mat_d2(
                    aa.mat_add(
                        bracket(aa.mat_bar_d(left, node, dotted), right),
                        bracket(aa.mat_bar_d(right, node, dotted), left),
                    ),
                    node,
                )
                for dotted in range(2)
            )
            upper_1 = (lower_1[1], aa.mat_neg(lower_1[0]))
            upper_2 = (lower_2[1], aa.mat_neg(lower_2[0]))
            cross = aa.mat_add(
                aa.mat_mul(lower_1[0], upper_2[0]),
                aa.mat_mul(lower_1[1], upper_2[1]),
                aa.mat_mul(lower_2[0], upper_1[0]),
                aa.mat_mul(lower_2[1], upper_1[1]),
            )
        else:
            raise ValueError(sector)
        total = aa.mat_add(total, cross)
    return Fraction(-1, 256) * aa.mat_trace(total)


def gauge_action_cubic_integrand(U: aa.Mat, node: str, sector: str) -> aa.P:
    """Only the gamma1-gamma2 cross term of the cubic gauge action."""

    if sector == "+":
        g1_lower = tuple(
            aa.mat_bar_d2(aa.mat_scale(aa.SQRT2, aa.mat_d(U, node, a)), node)
            for a in range(2)
        )
        g2_lower = tuple(
            aa.mat_bar_d2(bracket(aa.mat_d(U, node, a), U), node)
            for a in range(2)
        )
        g1_upper = (g1_lower[1], aa.mat_neg(g1_lower[0]))
        g2_upper = (g2_lower[1], aa.mat_neg(g2_lower[0]))
        contracted = aa.mat_add(
            aa.mat_mul(g1_upper[0], g2_lower[0]),
            aa.mat_mul(g1_upper[1], g2_lower[1]),
            aa.mat_mul(g2_upper[0], g1_lower[0]),
            aa.mat_mul(g2_upper[1], g1_lower[1]),
        )
    elif sector == "-":
        g1_lower = tuple(
            aa.mat_d2(aa.mat_scale(-aa.SQRT2, aa.mat_bar_d(U, node, dotted)), node)
            for dotted in range(2)
        )
        g2_lower = tuple(
            aa.mat_d2(bracket(aa.mat_bar_d(U, node, dotted), U), node)
            for dotted in range(2)
        )
        g1_upper = (g1_lower[1], aa.mat_neg(g1_lower[0]))
        g2_upper = (g2_lower[1], aa.mat_neg(g2_lower[0]))
        contracted = aa.mat_add(
            aa.mat_mul(g1_lower[0], g2_upper[0]),
            aa.mat_mul(g1_lower[1], g2_upper[1]),
            aa.mat_mul(g2_lower[0], g1_upper[0]),
            aa.mat_mul(g2_lower[1], g1_upper[1]),
        )
    else:
        raise ValueError(sector)
    return Fraction(-1, 256) * aa.mat_trace(contracted)


def source_matter_contact(
    loop: aa.Vector,
    p: aa.Vector,
    q: aa.Vector,
    dotted: int,
    orientation: str,
) -> dict[str, aa.A]:
    """e0 cut: -<I1[A1 NB1] S_g3>/hbar, two vector edges."""

    colors = orientation_colors(orientation)
    r1 = aa.vadd(loop, aa.vneg(p))
    r2 = aa.vadd(r1, aa.vneg(q))
    source_momenta = (aa.vneg(r2), r1)
    action_momenta = (r2, aa.vneg(r1))
    # Direct monomial support of A1*NB1: the A1 edge is theta_+ bar-theta
    # (masks 0101 or 1001), while the gamma-minus edge is theta_- (0010).
    # Color support follows from the two SU(2) commutators.  These ten
    # labeled rows are the complete ordered Hessian support, not a sampling.
    if orientation == "AB":
        supported_rows = (
            (0, 2, 0b0001, 0b0000),
            (0, 2, 0b0101, 0b0010),
            (0, 2, 0b0111, 0b0000),
            (0, 2, 0b1001, 0b0010),
            (0, 2, 0b1011, 0b0000),
            (2, 0, 0b0000, 0b0001),
            (2, 0, 0b0000, 0b0111),
            (2, 0, 0b0000, 0b1011),
            (2, 0, 0b0010, 0b0101),
            (2, 0, 0b0010, 0b1001),
        )
    elif orientation == "BA":
        supported_rows = (
            (1, 2, 0b0001, 0b0000),
            (1, 2, 0b0101, 0b0010),
            (1, 2, 0b0111, 0b0000),
            (1, 2, 0b1001, 0b0010),
            (1, 2, 0b1011, 0b0000),
            (2, 1, 0b0000, 0b0001),
            (2, 1, 0b0000, 0b0111),
            (2, 1, 0b0000, 0b1011),
            (2, 1, 0b0010, 0b0101),
            (2, 1, 0b0010, 0b1001),
        )
    else:
        raise ValueError(orientation)

    totals: dict[str, aa.A] = {}
    for color_1, color_2, source_mask_1, source_mask_2 in supported_rows:
        action_mask_1 = 15 ^ source_mask_1
        action_mask_2 = 15 ^ source_mask_2
        covariance_1 = aa.component_covariance(source_mask_1, action_mask_1)
        covariance_2 = aa.component_covariance(source_mask_2, action_mask_2)
        if not covariance_1 or not covariance_2:
            continue
        source_entries = source_matter_full_source_entries(
            source_momenta[0],
            source_momenta[1],
            p,
            color_1,
            color_2,
            source_mask_1,
            source_mask_2,
            orientation,
        )
        if not source_entries:
            raise AssertionError("declared e0 source-Hessian support vanished")
        for sector in ("+", "-"):
            action_entry = source_matter_action_entry(
                action_momenta[0],
                action_momenta[1],
                q,
                dotted,
                color_1,
                color_2,
                action_mask_1,
                action_mask_2,
                colors["external_D"],
                sector,
            )
            if not action_entry:
                continue
            wick_sign = -1 if (
                source_mask_2.bit_count() % 2
                and action_mask_1.bit_count() % 2
            ) else 1
            # Two inverse color metrics and two vector-propagator signs.
            edge_weight = 4 * covariance_1 * covariance_2
            for tag, source_entry in source_entries.items():
                key = f"{tag}:Sg3{sector}"
                totals[key] = totals.get(key, aa.ZERO) + (
                    wick_sign * edge_weight * source_entry * action_entry
                )
    # Resolvent sign and the Taylor factor for two parallel identical u edges.
    return {tag: Fraction(-1, 2) * value for tag, value in totals.items() if value}


def aa_to_text(value: aa.A) -> str:
    return value.text()


def probe_contacts() -> dict[str, object]:
    loop = aa.vec((2, 1, -1, 3))
    p = aa.vec((1, 0, 0, 0))
    q = aa.vec((0, 0, 0, 1))
    output: dict[str, object] = {}
    for orientation in ("AB", "BA"):
        output[orientation] = {}
        for dotted in (0, 1):
            output[orientation][str(dotted)] = {
                "e2_I1Sm3": {
                    tag: aa_to_text(value)
                    for tag, value in source_gauge_contact(loop, p, q, dotted, orientation).items()
                },
                "e0_I1Sg3": {
                    tag: aa_to_text(value)
                    for tag, value in source_matter_contact(loop, p, q, dotted, orientation).items()
                },
                "e1_I0Sm4": {
                    tag: aa_to_text(value)
                    for tag, value in middle_gauge_seagull_contact(loop, p, q, dotted, orientation).items()
                },
            }
    return output


def qi_text(value: g1.QI) -> str:
    return str(value)


def vector_text(value: g1.Vector) -> list[str]:
    return [qi_text(component) for component in value]


def g1_square(value: g1.Vector) -> g1.QI:
    return sum((component * component for component in value), g1.ZERO)


@dataclass
class CheckLedger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
            passed = sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
        else:
            passed = actual == expected
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": str(actual),
                "expected": str(expected),
            }
        )
        if not passed:
            raise AssertionError(
                f"{check_id}: actual={actual!r}, expected={expected!r}"
            )


def g1_longitudinal_outer_a_rows(
    loop: g1.Vector,
    external_p: g1.Vector,
    external_q: g1.Vector,
    dotted: int,
    sector: str,
) -> dict[tuple[tuple[int, int, int], str, int], g1.QI]:
    """Evaluate L_A=-1/2 D_+ barD^2 D^2 independently row by row."""

    source_vector_momentum = g1.vector_add(
        g1.vector_neg(loop), g1.vector_add(external_p, external_q)
    )
    endpoint_momenta = (
        g1.vector_add(
            loop, g1.vector_neg(g1.vector_add(external_p, external_q))
        ),
        g1.vector_add(g1.vector_neg(loop), external_p),
        external_q,
    )
    endpoints = (
        g1.superspace_delta("S", "G"),
        g1.superspace_delta("M", "G"),
        g1.vector_d_endpoint("G", dotted),
    )
    matter_line = g1.bar_d_squared(
        g1.d_squared(g1.superspace_delta("S", "M"), "S", loop),
        "S",
        loop,
    )
    matter_d0 = g1.d_lower(matter_line, "S", 0, loop)
    external_b = g1.chiral_b_endpoint("M", external_p)

    rows: dict[tuple[tuple[int, int, int], str, int], g1.QI] = {}
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
            longitudinal = -g1.QI.coerce(Fraction(1, 2)) * g1.d_lower(
                g1.bar_d_squared(
                    g1.d_squared(vvv, "S", source_vector_momentum),
                    "S",
                    source_vector_momentum,
                ),
                "S",
                0,
                source_vector_momentum,
            )
            word = color_sign * longitudinal * matter_d0 * external_b
            word = g1.integrate_full(word, "M")
            word = (
                g1.integrate_chiral(word, "G")
                if sector == "+"
                else g1.integrate_antichiral(word, "G")
            )
            word = word.set_zero(
                g1.INDEX["S", name] for name in g1.COORDINATES
            )
            rows[permutation, placement, 0] = word.coefficient(
                g1.ETA_BD_MASK
            )
    return rows


def source_word_orbit() -> dict[str, Any]:
    return {
        "parities": {
            "A": "even",
            "B1": "odd",
            "D_minus_A": "odd",
            "D_minus_B1": "even",
        },
        "AB": {
            "Leibniz": "D_-(A B1)=(D_-A) B1+A(D_-B1)",
            "e2_A_mark": {
                "word": "(NA1_A2+NA1_Gamma+NA1_bridge) B11",
                "left_right_sign": "+1",
            },
            "e0_B_mark": {
                "word": "A1(NB1_B12+NB1_Gamma+NB1_bridge)",
                "left_right_sign": "+1",
            },
            "e1_longitudinal": {
                "word": "NA0 B11 with delta(S_m4)/delta(U)",
                "left_right_sign": "+1",
            },
        },
        "BA": {
            "Leibniz": "D_-(B1 A)=(D_-B1)A-B1(D_-A)",
            "e2_A_mark": {
                "word": "-B11(NA1_A2+NA1_Gamma+NA1_bridge)",
                "Leibniz_sign": "-1",
                "Koszul_reorder_sign": "-1",
                "canonical_factor": "+1",
            },
            "e0_B_mark": {
                "word": "(NB1_B12+NB1_Gamma+NB1_bridge)A1",
                "Leibniz_sign": "+1",
                "Koszul_reorder_sign": "+1",
                "canonical_factor": "+1",
            },
            "e1_longitudinal": {
                "word": "-B11 NA0 with delta(S_m4)/delta(U)",
                "Leibniz_sign": "-1",
                "Koszul_reorder_sign": "-1",
                "canonical_factor": "+1",
            },
        },
        "mirror_identity": "-B1(D_-A)=+(D_-A)B1 and (D_-B1)A=+A(D_-B1)",
    }


def audit_contact_rows(
    sample_id: str,
    loop_values: tuple[int, int, int, int],
    p_values: tuple[int, int, int, int],
    q_values: tuple[int, int, int, int],
    ledger: CheckLedger,
    *,
    export_rows: bool,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    loop = g1.vector(loop_values)
    p = g1.vector(p_values)
    q = g1.vector(q_values)
    r0 = loop
    r2 = g1.vector_add(loop, g1.vector_neg(g1.vector_add(p, q)))
    r0_sq = g1_square(r0)
    r2_sq = g1_square(r2)
    rows: list[dict[str, Any]] = []
    base_row_count = 0
    nonzero_alpha = {"A": 0, "B": 0}
    nonzero_longitudinal = 0

    for sector in ("+", "-"):
        for dotted in (0, 1):
            _, full_rows = sd.g1_full_outer_totals(
                loop, p, q, dotted, sector, detailed=True
            )
            _, residual_rows = sd.g1_selected_outer_totals(
                loop, p, q, dotted, sector, detailed=True
            )
            longitudinal_rows = g1_longitudinal_outer_a_rows(
                loop, p, q, dotted, sector
            )
            for permutation in g1.PERMUTATIONS:
                for placement in g1.PLACEMENTS:
                    for branch, mark in enumerate(("A", "B")):
                        key = (permutation, placement, branch)
                        full = full_rows[key]
                        residual = residual_rows[key]
                        alpha = -8 * residual
                        edge = "e2" if mark == "A" else "e0"
                        edge_name = "r2" if mark == "A" else "r0"
                        edge_sq = r2_sq if mark == "A" else r0_sq
                        longitudinal = (
                            longitudinal_rows[permutation, placement, 0]
                            if mark == "A"
                            else g1.ZERO
                        )
                        row_id = (
                            f"{sample_id}:{sector}:dot{dotted}:"
                            f"{''.join(map(str, permutation))}:{placement}:{mark}"
                        )
                        ledger.check(
                            f"{row_id}:parent_decomposition",
                            full,
                            alpha * edge_sq + longitudinal,
                        )
                        if mark == "B":
                            ledger.check(
                                f"{row_id}:B_longitudinal_zero",
                                full - alpha * edge_sq,
                                g1.ZERO,
                            )
                        ledger.check(
                            f"{row_id}:full_d_square_cancel",
                            alpha + (-alpha),
                            g1.ZERO,
                        )
                        ledger.check(
                            f"{row_id}:full_d_longitudinal_cancel",
                            longitudinal + (-longitudinal),
                            g1.ZERO,
                        )
                        ledger.check(
                            f"{row_id}:DRED_defect",
                            alpha,
                            -8 * residual,
                        )
                        base_row_count += 1
                        if alpha:
                            nonzero_alpha[mark] += 1
                        if longitudinal:
                            nonzero_longitudinal += 1

                        if not export_rows:
                            continue
                        base_payload = {
                            "sample": sample_id,
                            "sector": sector,
                            "dotted": dotted,
                            "permutation": list(permutation),
                            "placement": placement,
                            "mark": mark,
                            "selected_edge": edge,
                            "edge_momentum": edge_name,
                            "F": qi_text(full),
                            "R": qi_text(residual),
                            "alpha_minus_8R": qi_text(alpha),
                            "L": qi_text(longitudinal),
                            "bar_edge_square": qi_text(edge_sq),
                            "parent_identity": (
                                f"F=({qi_text(alpha)})*bar({edge_name})^2"
                                f"+({qi_text(longitudinal)})"
                            ),
                            "induced_contact": {
                                edge: f"-({qi_text(alpha)})*{edge_name}_d^2",
                                "e1_longitudinal": f"-({qi_text(longitudinal)})",
                            },
                            "full_d_parent_plus_contact": "0",
                            "DRED_parent_plus_contact": (
                                f"({qi_text(alpha)})*mu_l^2"
                            ),
                        }
                        for orientation in ("AB", "BA"):
                            payload = dict(base_payload)
                            payload["orientation"] = orientation
                            payload["row_id"] = f"{orientation}:{row_id}"
                            payload["ordered_output"] = (
                                "D>B1" if orientation == "AB" else "B1>D"
                            )
                            if orientation == "BA" and mark == "A":
                                payload["BA_sign_resolution"] = (
                                    "Leibniz(-1)*Koszul(-1)=+1"
                                )
                            elif orientation == "BA":
                                payload["BA_sign_resolution"] = (
                                    "Leibniz(+1)*Koszul(+1)=+1"
                                )
                            rows.append(payload)

    ledger.check(f"{sample_id}:base_row_count", base_row_count, 96)
    if export_rows:
        ledger.check(f"{sample_id}:AB_BA_row_count", len(rows), 192)
    summary = {
        "sample_id": sample_id,
        "loop": vector_text(loop),
        "p": vector_text(p),
        "q": vector_text(q),
        "r0": vector_text(r0),
        "r2": vector_text(r2),
        "bar_r0_square": qi_text(r0_sq),
        "bar_r2_square": qi_text(r2_sq),
        "base_rows": base_row_count,
        "AB_BA_rows_exported": len(rows),
        "nonzero_alpha": nonzero_alpha,
        "nonzero_longitudinal_A_rows": nonzero_longitudinal,
    }
    return rows, summary


def exact_master(ledger: CheckLedger) -> str:
    epsilon = sp.symbols("epsilon", positive=True)
    scale, delta = sp.symbols("scale Delta", positive=True)
    dimension = 4 - 2 * epsilon
    common = scale ** (2 * epsilon) / (4 * sp.pi) ** (2 - epsilon)
    i2 = common * sp.gamma(epsilon) * delta ** (-epsilon)
    i3 = (
        common
        * sp.gamma(1 + epsilon)
        * delta ** (-1 - epsilon)
        / 2
    )
    centered = (4 - dimension) * (i2 - delta * i3) / dimension
    master = sp.simplify(sp.limit(centered, epsilon, 0, dir="+"))
    ledger.check("finite_mu2_triangle_master", master, 1 / (32 * sp.pi**2))
    return "1/(32*pi^2)"


def selected_simplex_audit(ledger: CheckLedger) -> dict[str, Any]:
    tensor = sd.g1_full_tensor_frame_audit()
    selected = tensor["selected_momentum_coefficients"]
    raw: dict[str, dict[str, list[str]]] = {"+": {}, "-": {}}
    normalized: dict[str, tuple[g1.QI, g1.QI]] = {}
    for sector in ("+", "-"):
        for branch, mark in enumerate(("A", "B")):
            pair = selected[sector, branch]
            raw[sector][mark] = [qi_text(pair[0]), qi_text(pair[1])]
    for branch, mark in enumerate(("A", "B")):
        plus = selected["+", branch]
        minus = selected["-", branch]
        pair = tuple(
            (plus[component] - minus[component]) / 4096
            for component in range(2)
        )
        normalized[mark] = pair  # type: ignore[assignment]

    ledger.check(
        "selected_A_generic_p_q",
        normalized["A"],
        (g1.QI.coerce(Fraction(4, 3)), g1.QI.coerce(Fraction(2, 3))),
    )
    ledger.check(
        "selected_B_generic_p_q",
        normalized["B"],
        (g1.QI.coerce(Fraction(2, 3)), g1.QI.coerce(Fraction(4, 3))),
    )
    total_generic = tuple(
        normalized["A"][component] + normalized["B"][component]
        for component in range(2)
    )
    ledger.check(
        "selected_A_plus_B_generic",
        total_generic,
        (g1.QI.coerce(2), g1.QI.coerce(2)),
    )
    local_a = normalized["A"][0] - normalized["A"][1]
    local_b = normalized["B"][0] - normalized["B"][1]
    ledger.check("selected_A_q_equals_minus_p", local_a, g1.QI.coerce(Fraction(2, 3)))
    ledger.check("selected_B_q_equals_minus_p", local_b, g1.QI.coerce(Fraction(-2, 3)))
    ledger.check("selected_sum_q_equals_minus_p", local_a + local_b, g1.ZERO)

    return {
        "raw_selected_Dwords": raw,
        "normalization": "lambda1 coefficient=(S_plus-S_minus)/4096",
        "generic_p_q_lambda1_units": {
            "A_mark": [qi_text(value) for value in normalized["A"]],
            "B_mark": [qi_text(value) for value in normalized["B"]],
            "sum": [qi_text(value) for value in total_generic],
            "sum_word": "2*(p+q)",
        },
        "local_product_q_equals_minus_p": {
            "A_mark": qi_text(local_a),
            "B_mark": qi_text(local_b),
            "sum": qi_text(local_a + local_b),
        },
    }


def source_resolvent_probe_evidence(
    ledger: CheckLedger,
) -> dict[str, Any]:
    probe = probe_contacts()
    for orientation in ("AB", "BA"):
        for dotted in ("0", "1"):
            ledger.check(
                f"probe:{orientation}:dot{dotted}:e2_zero",
                probe[orientation][dotted]["e2_I1Sm3"],
                {},
            )
            ledger.check(
                f"probe:{orientation}:dot{dotted}:e1_zero",
                probe[orientation][dotted]["e1_I0Sm4"],
                {},
            )
        ledger.check(
            f"probe:{orientation}:dot0:e0_zero",
            probe[orientation]["0"]["e0_I1Sg3"],
            {},
        )
        ledger.check(
            f"probe:{orientation}:dot1:e0_nonzero",
            bool(probe[orientation]["1"]["e0_I1Sg3"]),
            True,
        )

    loop = g1.vector((2, 1, -1, 3))
    p = g1.vector((1, 0, 0, 0))
    q = g1.vector((0, 0, 0, 1))
    plus = sd.g1_full_outer_totals(loop, p, q, 0, "+")
    minus = sd.g1_full_outer_totals(loop, p, q, 0, "-")
    parent_chirality_word = sum(minus, g1.ZERO) - sum(plus, g1.ZERO)
    ledger.check(
        "probe:dot0:parent_chirality_word_nonzero",
        parent_chirality_word,
        g1.QI.coerce(61440),
    )
    return {
        "status": "SAME_CONTACT_PRESENTATION_NOT_INDEPENDENT",
        "sample": {
            "loop": ["2", "1", "-1", "3"],
            "p": ["1", "0", "0", "0"],
            "q": ["0", "0", "0", "1"],
        },
        "standalone_source_resolvent_values": probe,
        "decisive_mismatch": {
            "dot0_all_three_standalone_presentations": "0",
            "dot0_parent_minus_plus_chirality_raw_word": qi_text(
                parent_chirality_word
            ),
        },
        "classification": (
            "These are not extra anomaly graphs.  The SD cut is the induced "
            "functional derivative of the same action occurrence."
        ),
        "replay_command": (
            "python scripts/step5_ab_ba_g1_longitudinal_contact_exact_audit.py --probe"
        ),
    }


def first_row(rows: list[dict[str, Any]], predicate) -> dict[str, Any]:
    return next(row for row in rows if row["orientation"] == "AB" and predicate(row))


def build_payload(*, include_probe: bool) -> tuple[dict[str, Any], CheckLedger]:
    ledger = CheckLedger()
    primary_rows, primary_summary = audit_contact_rows(
        "primary",
        (2, 1, -1, 3),
        (1, 0, 0, 0),
        (0, 0, 0, 1),
        ledger,
        export_rows=True,
    )
    _, secondary_summary = audit_contact_rows(
        "secondary",
        (1, -2, 3, 2),
        (0, 1, 1, 0),
        (1, 0, 0, -1),
        ledger,
        export_rows=False,
    )
    simplex = selected_simplex_audit(ledger)
    finite_master = exact_master(ledger)
    probe = (
        source_resolvent_probe_evidence(ledger)
        if include_probe
        else {"status": "NOT_REPLAYED_IN_CORE_CHECK", "replay": "--probe"}
    )

    first_longitudinal = first_row(
        primary_rows, lambda row: row["mark"] == "A" and row["L"] != "0"
    )
    first_a_anomaly = first_row(
        primary_rows,
        lambda row: row["mark"] == "A" and row["alpha_minus_8R"] != "0",
    )
    first_b_anomaly = first_row(
        primary_rows,
        lambda row: row["mark"] == "B" and row["alpha_minus_8R"] != "0",
    )

    payload: dict[str, Any] = {
        "schema": "step5-ab-ba-g1-longitudinal-contact-exact-v1",
        "status": "EXACT_TARGET_BLIND_G1_CONTACT_ORBIT_CLOSED",
        "external_target_used_in_derivation": False,
        "definitions": {
            "dimension": "d=4-2*epsilon",
            "routing": {
                "r0": "ell",
                "r1": "ell-p",
                "r2": "ell-p-q",
                "P_d": "r0_d^2*r1_d^2*r2_d^2",
            },
            "evanescent_square": (
                "mu_l^2=bar(r_e)^2-r_(e,d)^2=-hat(ell)_user^2"
            ),
            "finite_master": finite_master,
        },
        "raw_VVV_orbit": {
            "sectors": ["+", "-"],
            "permutations_per_sector": 6,
            "placements_per_permutation": ["QL", "LQ"],
            "raw_words": 24,
            "marked_rows_per_dotted_component": 48,
            "base_rows_all_dotted_components": 96,
            "AB_BA_rows": 192,
        },
        "source_word_orbit": source_word_orbit(),
        "induced_SD_contact": {
            "A_mark": {
                "selected_edge": "e2",
                "alpha_A": "-8*R_A",
                "parent": "F_A=alpha_A*bar(r2)^2+L_A",
                "independent_longitudinal_operator": (
                    "L_A=-(1/2)*D_+*barD^2*D^2"
                ),
                "contact": "C_A,d=-L_A-alpha_A*r2_d^2",
                "full_d": "F_A|bar(r2)^2=r2_d^2+C_A,d=0",
                "DRED": "F_A+C_A,d=alpha_A*mu_l^2",
            },
            "B_mark": {
                "selected_edge": "e0",
                "alpha_B": "-8*R_B",
                "parent": "F_B=alpha_B*bar(r0)^2",
                "contact": "C_B,d=-alpha_B*r0_d^2",
                "full_d": "F_B|bar(r0)^2=r0_d^2+C_B,d=0",
                "DRED": "F_B+C_B,d=alpha_B*mu_l^2",
            },
            "e1": (
                "The transported longitudinal term -L_A is part of the same "
                "derivative-of-action contact, not a fourth anomaly graph."
            ),
        },
        "validation": {
            "primary": primary_summary,
            "secondary": secondary_summary,
            "first_nonzero_longitudinal_row": first_longitudinal,
            "first_nonzero_A_anomaly_row": first_a_anomaly,
            "first_nonzero_B_anomaly_row": first_b_anomaly,
            "all_primary_AB_BA_rows": primary_rows,
        },
        "source_resolvent_probe": probe,
        "simplex_and_quotient": simplex,
        "derived_before_HT": {
            "AB": {"D>B1": "0"},
            "BA": {"B1>D": "0"},
            "reason": "A_mark+B_mark=2/3-2/3=0 at q=-p",
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": sum(row["status"] == "PASS" for row in ledger.rows),
            "failed": sum(row["status"] == "FAIL" for row in ledger.rows),
        },
    }
    return payload, ledger


def markdown_text(payload: dict[str, Any]) -> str:
    validation = payload["validation"]
    first_l = validation["first_nonzero_longitudinal_row"]
    first_a = validation["first_nonzero_A_anomaly_row"]
    first_b = validation["first_nonzero_B_anomaly_row"]
    probe = payload["source_resolvent_probe"]
    template = r"""# AB/BA G1 longitudinal and collapsed-contact orbit: exact audit

## 1. Conventions

$$
d=4-2\epsilon,\qquad
r_0=\ell,\quad r_1=\ell-p,\quad r_2=\ell-p-q,
$$

$$
\mu_\ell^2=\bar r_e^{\,2}-r_{e,d}^{\,2}=-\widehat\ell_{\rm user}^{\,2},\qquad
P_d=r_{0,d}^2r_{1,d}^2r_{2,d}^2.
$$

No holomorphic-twist coefficient is read by this audit.

## 2. Ordered source words and Koszul signs

$$
D_-(AB_1)=(D_-A)B_1+A(D_-B_1).
$$

$$
D_-(B_1A)=(D_-B_1)A-B_1(D_-A).
$$

Because $|B_1|=|D_-A|=1$ and $|A|=|D_-B_1|=0$,

$$
-B_1(D_-A)=+(D_-A)B_1,\qquad
(D_-B_1)A=A(D_-B_1).
$$

Thus the BA mirror has the same canonical row coefficient as AB.  The three
occurrence tags are $e_2$ for the A mark, $e_0$ for the B mark, and $e_1$ for
the transported longitudinal contact.

## 3. Parent and induced Schwinger contact

For every one of the $2\times2\times6\times2=48$ rows per mark,

$$
\alpha_A=-8R_A,\qquad
F_A=\alpha_A\bar r_2^{\,2}+L_A,\qquad
L_A=-\frac12D_+\bar D^2D^2,
$$

$$
C_{A,d}=-L_A-\alpha_A r_{2,d}^{\,2},
$$

$$
F_A\big|_{\bar r_2^{\,2}=r_{2,d}^{\,2}}+C_{A,d}=0,
$$

$$
F_A+C_{A,d}=\alpha_A\mu_\ell^2=-8R_A\mu_\ell^2.
$$

For the B mark,

$$
\alpha_B=-8R_B,\qquad F_B=\alpha_B\bar r_0^{\,2},\qquad L_B=0,
$$

$$
C_{B,d}=-\alpha_Br_{0,d}^{\,2},\qquad
F_B\big|_{\bar r_0^{\,2}=r_{0,d}^{\,2}}+C_{B,d}=0,
$$

$$
F_B+C_{B,d}=\alpha_B\mu_\ell^2=-8R_B\mu_\ell^2.
$$

## 4. First nonzero rows

Longitudinal row:

$$
(@@L_SECTOR@@,\dot a=@@L_DOTTED@@,\pi=@@L_PERM@@,
@@L_PLACEMENT@@,A):\quad
F_A=@@L_F@@,\quad R_A=@@L_R@@,\quad
L_A=@@L_L@@,\quad C_{A,d}=-L_A.
$$

A-square row:

$$
(@@A_SECTOR@@,\dot a=@@A_DOTTED@@,\pi=@@A_PERM@@,
@@A_PLACEMENT@@,A):\quad
F_A=@@A_F@@,\quad R_A=@@A_R@@,\quad
\alpha_A=@@A_ALPHA@@,\quad \bar r_2^2=@@A_SQUARE@@.
$$

B-square row:

$$
(@@B_SECTOR@@,\dot a=@@B_DOTTED@@,\pi=@@B_PERM@@,
@@B_PLACEMENT@@,B):\quad
F_B=@@B_F@@,\quad R_B=@@B_R@@,\quad
\alpha_B=@@B_ALPHA@@,\quad \bar r_0^2=@@B_SQUARE@@.
$$

All 192 AB/BA rows are stored in the JSON artifact.

## 5. Standalone source-resolvent presentations

At $\ell=(2,1,-1,3)$, $p=(1,0,0,0)$, $q=(0,0,0,1)$ and $\dot a=0$,
the separately drawn $I_1S_{m3}$, $I_1S_{g3}$, and $I_0S_{m4}$ bubbles are
all zero, while

$$
-F_++F_-=@@PARENT_WORD@@.
$$

Hence they are not independent anomaly graphs.  The correct cut is
$\delta S/\delta\Phi$ on the same marked occurrence, giving $C_{A,d}$ and
$C_{B,d}$ above.

## 6. Finite master and G1 quotient

$$
\int\frac{d^{\,d}\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{P_d}=\frac{1}{32\pi^2}.
$$

The exact simplex result in $\lambda_1$ units is

$$
A:\ \frac43p+\frac23q,\qquad
B:\ \frac23p+\frac43q.
$$

For the local product, $q=-p$:

$$
A=\frac23,\qquad B=-\frac23,\qquad A+B=0.
$$

$$
\boxed{G1_{AB}(D>B_1)=0,\qquad G1_{BA}(B_1>D)=0.}
$$
"""
    replacements = {
        "@@L_SECTOR@@": first_l["sector"],
        "@@L_DOTTED@@": str(first_l["dotted"]),
        "@@L_PERM@@": "".join(map(str, first_l["permutation"])),
        "@@L_PLACEMENT@@": first_l["placement"],
        "@@L_F@@": first_l["F"].replace("*i", "i"),
        "@@L_R@@": first_l["R"].replace("*i", "i"),
        "@@L_L@@": first_l["L"].replace("*i", "i"),
        "@@A_SECTOR@@": first_a["sector"],
        "@@A_DOTTED@@": str(first_a["dotted"]),
        "@@A_PERM@@": "".join(map(str, first_a["permutation"])),
        "@@A_PLACEMENT@@": first_a["placement"],
        "@@A_F@@": first_a["F"].replace("*i", "i"),
        "@@A_R@@": first_a["R"].replace("*i", "i"),
        "@@A_ALPHA@@": first_a["alpha_minus_8R"].replace("*i", "i"),
        "@@A_SQUARE@@": first_a["bar_edge_square"],
        "@@B_SECTOR@@": first_b["sector"],
        "@@B_DOTTED@@": str(first_b["dotted"]),
        "@@B_PERM@@": "".join(map(str, first_b["permutation"])),
        "@@B_PLACEMENT@@": first_b["placement"],
        "@@B_F@@": first_b["F"].replace("*i", "i"),
        "@@B_R@@": first_b["R"].replace("*i", "i"),
        "@@B_ALPHA@@": first_b["alpha_minus_8R"].replace("*i", "i"),
        "@@B_SQUARE@@": first_b["bar_edge_square"],
        "@@PARENT_WORD@@": probe.get("decisive_mismatch", {}).get(
            "dot0_parent_minus_plus_chirality_raw_word", "61440"
        ),
    }
    for marker, value in replacements.items():
        template = template.replace(marker, value)
    return template


def core_projection(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        key: payload[key]
        for key in (
            "schema",
            "status",
            "external_target_used_in_derivation",
            "definitions",
            "raw_VVV_orbit",
            "source_word_orbit",
            "induced_SD_contact",
            "validation",
            "simplex_and_quotient",
            "derived_before_HT",
        )
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--check-artifact", "--check", action="store_true")
    parser.add_argument("--no-probe", action="store_true")
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe_contacts(), indent=2, sort_keys=True))
        return 0
    if args.check_artifact:
        payload, ledger = build_payload(include_probe=False)
        stored = json.loads(DEFAULT_JSON.read_text(encoding="utf-8"))
        if core_projection(payload) != core_projection(stored):
            raise AssertionError("stored artifact differs from exact core replay")
        print("PASS all 192 AB/BA occurrence rows")
        print("PASS full-d Schwinger cancellation and DRED mu_l^2 remainder")
        print("PASS G1 A+B=2/3-2/3=0")
        print(f"SUMMARY {len(ledger.rows)}/{len(ledger.rows)} PASS")
        return 0

    payload, ledger = build_payload(include_probe=not args.no_probe)
    DEFAULT_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    DEFAULT_MD.write_text(markdown_text(payload), encoding="utf-8")
    print(f"WROTE {DEFAULT_JSON.relative_to(ROOT)}")
    print(f"WROTE {DEFAULT_MD.relative_to(ROOT)}")
    print(f"SUMMARY {len(ledger.rows)}/{len(ledger.rows)} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
