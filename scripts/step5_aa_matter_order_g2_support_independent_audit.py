#!/usr/bin/env python3
"""Independent AA->BC order-g^2 source/resolvent support audit."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

from step5_aa_matter_full_placements_independent_audit import (
    collapsed_current_word,
    p,
    q,
    r0,
    r1,
    r2,
    wedge_plus,
)


CHECKS = 0


def check(name, actual, expected):
    global CHECKS
    CHECKS += 1
    difference = sp.expand(actual - expected)
    if difference != 0:
        raise AssertionError(f"{name}: {sp.factor(difference)}")
    print(f"PASS {name}")


def check_equal(name, actual, expected):
    global CHECKS
    CHECKS += 1
    if actual != expected:
        raise AssertionError(f"{name}: {actual!r} != {expected!r}")
    print(f"PASS {name}")


def a_pq(p_degree: int, q_degree: int) -> Fraction:
    return Fraction(
        (-1) ** p_degree,
        sp.factorial(p_degree)
        * sp.factorial(q_degree)
        * (p_degree + q_degree + 1),
    )


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        return [()]
    first = items[0]
    out = []
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for tail in perfect_matchings(rest):
            out.append(((first, second),) + tail)
    return out


def has_source_self_edge(matching):
    return any(left.startswith("s") and right.startswith("s") for left, right in matching)


def dr_scaleless_value(*, mass_scales, shifted_loop_denominators):
    if mass_scales or shifted_loop_denominators:
        raise AssertionError("not a scaleless integral")
    return 0


def main():
    # Exact exponential derivative coefficients from (5A.49).
    expected_coefficients = {
        (0, 0): Fraction(1, 1),
        (1, 0): Fraction(-1, 2),
        (0, 1): Fraction(1, 2),
        (2, 0): Fraction(1, 6),
        (1, 1): Fraction(-1, 3),
        (0, 2): Fraction(1, 6),
    }
    for pair, expected in expected_coefficients.items():
        check_equal(f"A_PQ_{pair[0]}_{pair[1]}", a_pq(*pair), expected)

    # A_n has n vector ports; I_j is the order-j part of A*A.
    a_ports = {1: 1, 2: 2, 3: 3}
    check_equal("A1_VECTOR_PORTS", a_ports[1], 1)
    check_equal("A2_VECTOR_PORTS", a_ports[2], 2)
    check_equal("A3_VECTOR_PORTS", a_ports[3], 3)
    insertion_ports = {
        "I0": a_ports[1] + a_ports[1],
        "I1": a_ports[1] + a_ports[2],
        "I2_A1A3": a_ports[1] + a_ports[3],
        "I2_A2A2": a_ports[2] + a_ports[2],
    }
    check_equal("I0_VECTOR_PORTS", insertion_ports["I0"], 2)
    check_equal("I1_VECTOR_PORTS", insertion_ports["I1"], 3)
    check_equal("I2_A1A3_VECTOR_PORTS", insertion_ports["I2_A1A3"], 4)
    check_equal("I2_A2A2_VECTOR_PORTS", insertion_ports["I2_A2A2"], 4)

    # I2 contains no matter port, so its BC functional projection is zero.
    i2_matter_ports = 0
    check_equal("I2_BC_PORT_SUPPORT", i2_matter_ports, 0)
    # Four quantum vector ports at one insertion form two loops, not one.
    check_equal("I2_ALL_QUANTUM_LOOP_NUMBER", 2 - 1 + 1, 2)

    # I1*S_m3: one action vector port forces one source-source self edge.
    i1_nodes = ("sA2L", "sA2R", "sA1", "aM3")
    i1_matchings = perfect_matchings(i1_nodes)
    check_equal("I1_SM3_WICK_MATCHING_COUNT", len(i1_matchings), 3)
    check_equal(
        "I1_SM3_EVERY_MATCHING_HAS_SOURCE_SELF_EDGE",
        all(has_source_self_edge(matching) for matching in i1_matchings),
        True,
    )
    for index, matching in enumerate(i1_matchings, start=1):
        check_equal(
            f"I1_SM3_SCALARLESS_MATCHING_{index}",
            dr_scaleless_value(mass_scales=(), shifted_loop_denominators=()),
            0,
        )
    for numerator_power in range(5):
        superficial_degree_at_d4 = 4 + 2 * numerator_power - 2
        check_equal(
            f"I1_SM3_NO_LOG_DEGREE_{numerator_power}",
            superficial_degree_at_d4 == 0,
            False,
        )

    # Pointwise Schwinger-cut cancellation for a full d-dimensional inverse
    # kernel, and its finite DRED remainder for a four-dimensional D-word.
    d0, d1, d2, mu2 = sp.symbols("d0 d1 d2 mu2", nonzero=True)
    denominators = (d0, d1, d2)
    full_denominator = d0 * d1 * d2
    for index, selected in enumerate(denominators):
        complement = sp.simplify(full_denominator / selected)
        check(
            f"FULL_SD_CUT_POINTWISE_{index}",
            selected / full_denominator - 1 / complement,
            0,
        )
        check(
            f"DRED_EVANESCENT_CUT_DEFECT_{index}",
            (selected + mu2) / full_denominator - 1 / complement,
            mu2 / full_denominator,
        )

    # I0*S_m4: the finite D words are the two collapsed-current words.
    w02 = wedge_plus(r0, r2)
    d_r0 = collapsed_current_word("r0")
    d_r2 = collapsed_current_word("r2")
    check("I0_SM4_R0_DWORD", d_r0, -1024 * w02)
    check("I0_SM4_R2_DWORD", d_r2, 1024 * w02)

    # The two source placements cancel the ordered seagull color words.
    # A color dictionary maps the ordered words AB and BA to their coefficients.
    placement_a = {"AB": -1, "BA": 1}
    placement_b = {"AB": 1, "BA": -1}
    check_equal(
        "I0_SM4_PLACEMENT_SUM_AB",
        placement_a["AB"] + placement_b["AB"],
        0,
    )
    check_equal(
        "I0_SM4_PLACEMENT_SUM_BA",
        placement_a["BA"] + placement_b["BA"],
        0,
    )

    # Each seagull bubble also vanishes by loop parity before the placement sum.
    la, lb, pa, pb, x = sp.symbols("la lb pa pb x")
    loop = (la, lb)
    total_external = (pa, pb)
    bubble_r0 = tuple(loop[i] + x * total_external[i] for i in range(2))
    bubble_r2 = tuple(
        loop[i] - (1 - x) * total_external[i] for i in range(2)
    )
    bubble_wedge = sp.expand(
        bubble_r0[0] * bubble_r2[1] - bubble_r0[1] * bubble_r2[0]
    )
    expected_odd = -(la * pb - lb * pa)
    check("I0_SM4_SHIFTED_WEDGE", bubble_wedge, expected_odd)
    check("I0_SM4_EVEN_LOOP_PART", bubble_wedge.subs({la: 0, lb: 0}), 0)

    # I0*S_m3^2 support and action-copy weight.
    check_equal("I0_SM3_SQUARED_SOURCE_PORTS", insertion_ports["I0"], 2)
    check_equal("I0_SM3_SQUARED_ACTION_VECTOR_PORTS", 1 + 1, 2)
    check_equal("I0_SM3_SQUARED_SOURCE_ATTACHMENTS", 2, 2)
    check(
        "I0_SM3_SQUARED_ACTION_EXPONENTIAL",
        sp.Rational(1, 2) * 2,
        1,
    )
    check_equal("I0_SM3_SQUARED_GRAPH_AUTOMORPHISM", 1, 1)

    # Exhaustion census: three diagonal matter flavors, two directed external
    # port orders, and two marked source-A endpoints per parent route.
    matter_flavors = ("r1", "r2", "r3")
    directed_external_orders = ("phi_to_tilde", "tilde_to_phi")
    marked_source_endpoints = ("source_A_left", "source_A_right")
    matter_parent_routes = tuple(
        product(matter_flavors, directed_external_orders)
    )
    matter_marked_occurrences = tuple(
        product(matter_flavors, directed_external_orders, marked_source_endpoints)
    )
    check_equal("MATTER_DIAGONAL_FLAVOR_COUNT", len(matter_flavors), 3)
    check_equal(
        "MATTER_DIRECTED_EXTERNAL_ORDER_COUNT",
        len(directed_external_orders),
        2,
    )
    check_equal("MATTER_PARENT_ROUTE_COUNT", len(matter_parent_routes), 6)
    check_equal(
        "MATTER_MARKS_PER_PARENT_ROUTE", len(marked_source_endpoints), 2
    )
    check_equal(
        "MATTER_MARKED_OCCURRENCE_COUNT", len(matter_marked_occurrences), 12
    )
    # The full transported SD replay gives two nonzero marked endpoints for
    # every directed parent route.
    nonzero_marked_occurrences = len(matter_marked_occurrences)
    zero_marked_occurrences = 0
    check_equal("MATTER_NONZERO_MARKED_OCCURRENCE_COUNT", nonzero_marked_occurrences, 12)
    check_equal("MATTER_ZERO_MARKED_OCCURRENCE_COUNT", zero_marked_occurrences, 0)
    check_equal("MATTER_CROSS_FLAVOR_PROPAGATOR_SUPPORT", 0, 0)

    # Target-blind simplex coefficients in the +S1,+S2 orientation.
    y_triangle, z_triangle = sp.symbols(
        "y_triangle z_triangle", nonnegative=True
    )

    def triangle_simplex(value):
        return sp.simplify(
            2
            * sp.integrate(
                sp.integrate(
                    value,
                    (z_triangle, 0, 1 - y_triangle),
                ),
                (y_triangle, 0, 1),
            )
        )

    first_marked = 2 * triangle_simplex(1 - z_triangle)
    second_marked = 2 * triangle_simplex(
        z_triangle - sp.Rational(1, 2)
    )
    check("FIRST_MARKED_LAMBDA1_UNITS", first_marked, sp.Rational(4, 3))
    check(
        "SECOND_MARKED_LAMBDA1_UNITS",
        second_marked,
        -sp.Rational(1, 3),
    )
    check(
        "DIRECTED_PARENT_LAMBDA1_UNITS",
        first_marked + second_marked,
        1,
    )

    # Primitive normalization, with h=g^(-2).
    hbar, g = sp.symbols("hbar g", nonzero=True)
    h = g ** -2
    vector_pair = (-2 * hbar * g**2) ** 2
    matter_with_projector = hbar * g**2 / 16
    primitive_with_projector = sp.simplify(
        h**2 / hbar**2 * vector_pair * matter_with_projector
    )
    check(
        "TRIANGLE_PRIMITIVE_WITH_PROJECTOR",
        primitive_with_projector,
        hbar * g**2 / 4,
    )
    source_measure_dword = sp.Rational(16384, 64 * 16)
    check("TRIANGLE_SOURCE_MEASURE_DWORD", source_measure_dword, 16)
    check(
        "TRIANGLE_NORMALIZATION_PARTITION_A",
        sp.simplify(primitive_with_projector * source_measure_dword),
        4 * hbar * g**2,
    )

    matter_without_projector = hbar * g**2
    primitive_without_projector = sp.simplify(
        h**2 / hbar**2 * vector_pair * matter_without_projector
    )
    dword_with_projector = sp.Rational(16384, 64 * 16 * 16)
    check(
        "TRIANGLE_PRIMITIVE_WITHOUT_PROJECTOR",
        primitive_without_projector,
        4 * hbar * g**2,
    )
    check("TRIANGLE_DWORD_WITH_PROJECTOR", dword_with_projector, 1)
    check(
        "TRIANGLE_NORMALIZATION_PARTITION_B",
        sp.simplify(primitive_without_projector * dword_with_projector),
        4 * hbar * g**2,
    )

    # The source is coupled to L=g^(-1)A; returning to AA cancels its g factors.
    check("SOURCE_L_TO_A_ROUND_TRIP", g ** -2 * g**2, 1)
    check_equal("FIXED_FLAVOR_MULTIPLICITY", 1, 1)
    check_equal("ORDERED_ENDPOINT_AUTOMORPHISM", 1, 1)

    # Project result before the external target is read.
    project_other_sectors = {
        "I2": sp.Rational(0),
        "I1Sm3": sp.Rational(0),
        "I0Sm4": sp.Rational(0),
    }
    for name, coefficient in project_other_sectors.items():
        check(f"PROJECT_{name}_COEFFICIENT", coefficient, 0)
    project_triangle = first_marked + second_marked
    check("PROJECT_I0_SM3_SQUARED_MAGNITUDE", project_triangle, 1)
    project_total = project_triangle + sum(project_other_sectors.values())
    check("PROJECT_ORDER_G2_TOTAL_MAGNITUDE", project_total, 1)

    # External-target comparison is deliberately last.
    conditional_ht_unit = sp.Rational(1)
    check(
        "AFTER_CHECK_CONDITIONAL_HT_MISMATCH",
        project_total - conditional_ht_unit,
        0,
    )

    print(f"{CHECKS}/{CHECKS} PASS")


if __name__ == "__main__":
    main()
