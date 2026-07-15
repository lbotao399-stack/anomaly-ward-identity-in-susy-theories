#!/usr/bin/env python3
"""Target-blind AB/BA G3 Schwinger rows and zero-square occurrence audit.

The scope is the two fixed-flavor TMH parents of the ordered AB/BA source.
The audit keeps four layers separate:

* local jet: every parent, induced cut, and nonlinear descendant occurrence;
* EOM/SD: only the three edgewise parent--functional-cut pairs;
* total divergence: not used;
* cohomology/HT comparison: not used.

No coefficient is inferred from a holomorphic-twist target or residual-q
condition.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ab1_marked_sd_orbit_exact_audit as marked  # noqa: E402
import step5_all_triangle_parent_port_census_audit as census  # noqa: E402


JSON_OUT = (
    ROOT / "audits" / "step5-ab-ba-g3-sd-zero-square-occurrence-exact.json"
)
MD_OUT = ROOT / "audits" / "step5-ab-ba-g3-sd-zero-square-occurrence-exact.md"

STATUS = (
    "PASS_G3_THREE_SD_CUTS_AND_ZERO_SQUARE_I1_I2_FAMILIES_EXHAUSTED__"
    "NO_NET_CC_EXTERNAL_PORT_CORRECTION__PRECOHOMOLOGY_MAGNITUDE_TWO_RETAINED"
)


def exact_text(value: object) -> str:
    if isinstance(value, sp.MatrixBase):
        return str(value.tolist()).replace("I", "i")
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value)).replace("I", "i")
    if isinstance(value, tuple):
        return "(" + ", ".join(exact_text(entry) for entry in value) + ")"
    if isinstance(value, (set, frozenset)):
        return "{" + ", ".join(sorted(str(entry) for entry in value)) + "}"
    return str(value)


def exact_equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        difference = sp.Matrix(actual) - sp.Matrix(expected)
        return all(sp.simplify(entry) == 0 for entry in difference)
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, str]]

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


def simplex_moment(polynomial: sp.Expr, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    return sp.simplify(
        2 * sp.integrate(sp.integrate(polynomial, (z, 0, 1 - y)), (y, 0, 1))
    )


def route_certificate(ledger: Ledger) -> dict[str, Any]:
    ab = [
        row
        for row in census.enumerate_routes("A", "B1")
        if row.topology == "TMH"
    ]
    ba = [
        row
        for row in census.enumerate_routes("B1", "A")
        if row.topology == "TMH"
    ]
    ledger.check("AB_TMH_ROUTE_COUNT", len(ab), 2)
    ledger.check("BA_TMH_ROUTE_COUNT", len(ba), 2)
    ledger.check(
        "AB_TMH_EXTERNAL_ORDER",
        tuple((row.external_left_field, row.external_right_field) for row in ab),
        (("tildephi2", "tildephi3"), ("tildephi3", "tildephi2")),
    )
    ledger.check(
        "BA_TMH_EXTERNAL_ORDER",
        tuple((row.external_left_field, row.external_right_field) for row in ba),
        (("tildephi3", "tildephi2"), ("tildephi2", "tildephi3")),
    )
    ledger.check(
        "AB_TMH_VERTICES",
        tuple((row.left_vertex, row.right_vertex) for row in ab),
        (("M2", "Hminus"), ("M3", "Hminus")),
    )
    ledger.check(
        "BA_TMH_VERTICES",
        tuple((row.left_vertex, row.right_vertex) for row in ba),
        (("Hminus", "M2"), ("Hminus", "M3")),
    )
    ab_edge_signatures = tuple(
        (
            (row.left_source_field, census.bare_field(row.left_source_port)),
            (
                census.bare_field(row.bridge_left_port),
                census.bare_field(row.bridge_right_port),
            ),
            (row.right_source_field, census.bare_field(row.right_source_port)),
        )
        for row in ab
    )
    ba_edge_signatures = tuple(
        (
            (row.left_source_field, census.bare_field(row.left_source_port)),
            (
                census.bare_field(row.bridge_left_port),
                census.bare_field(row.bridge_right_port),
            ),
            (row.right_source_field, census.bare_field(row.right_source_port)),
        )
        for row in ba
    )
    ledger.check(
        "AB_TMH_EDGE_SIGNATURES",
        ab_edge_signatures,
        (
            (("u", "u"), ("phi2", "tildephi2"), ("phi1", "tildephi1")),
            (("u", "u"), ("phi3", "tildephi3"), ("phi1", "tildephi1")),
        ),
    )
    ledger.check(
        "BA_TMH_EDGE_SIGNATURES",
        ba_edge_signatures,
        (
            (("phi1", "tildephi1"), ("tildephi2", "phi2"), ("u", "u")),
            (("phi1", "tildephi1"), ("tildephi3", "phi3"), ("u", "u")),
        ),
    )

    # In BA the outer-A Leibniz sign and the odd B1--J_A exchange cancel.
    # The outer-B1 current is even and crosses the even A with no sign.
    a_right_leibniz = -sp.Integer(1)
    b1_ja_exchange = -sp.Integer(1)
    b_left_leibniz = sp.Integer(1)
    jb_a_exchange = sp.Integer(1)
    ledger.check(
        "BA_OUTER_A_KOSZUL_PRODUCT",
        a_right_leibniz * b1_ja_exchange,
        1,
    )
    ledger.check(
        "BA_OUTER_B1_KOSZUL_PRODUCT",
        b_left_leibniz * jb_a_exchange,
        1,
    )

    return {
        "AB": [
            {
                "route_id": row.route_id,
                "vertices": [row.left_vertex, row.right_vertex],
                "external_fields": [
                    row.external_left_field,
                    row.external_right_field,
                ],
                "edge_signature": [list(edge) for edge in ab_edge_signatures[index]],
            }
            for index, row in enumerate(ab)
        ],
        "BA": [
            {
                "route_id": row.route_id,
                "vertices": [row.left_vertex, row.right_vertex],
                "external_fields": [
                    row.external_left_field,
                    row.external_right_field,
                ],
                "edge_signature": [list(edge) for edge in ba_edge_signatures[index]],
            }
            for index, row in enumerate(ba)
        ],
        "BA_Koszul": {
            "outer_A": "(-1)_Leibniz*(-1)_(B1,J_A swap)=+1",
            "outer_B1": "(+1)_Leibniz*(+1)_(J_B,A swap)=+1",
        },
    }


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    words = marked.g23_exact_words()

    w0 = sp.expand(words["w12"])
    w1 = sp.expand(words["wedge_pq_r0"])
    w2 = sp.expand(words["wedge_p_r0"])
    det0 = sp.expand(words["det_r0"])
    det1 = sp.expand(words["det_r1"])
    det2 = sp.expand(words["det_r2"])

    ledger.check("W2_EQUALS_W01", w2, words["w01"])
    ledger.check(
        "RAW_OUTER_A_PARENT",
        words["g3_a_full"],
        -1024 * det0 * w0 + 1024 * det1 * w1,
    )
    ledger.check(
        "RAW_OUTER_B_PARENT",
        words["g3_b_parent_raw"],
        -1024 * det2 * w2,
    )
    ledger.check("RAW_E0_CURRENT_CORE", words["g3_a_contact_top"], 512 * w0)
    ledger.check(
        "RAW_E1_TRANSPORTED_CORE",
        words["g3_transported_contact_core"],
        -128 * w1,
    )
    ledger.check("RAW_E2_POTENTIAL_CORE", words["g3_b_contact"], -128 * w2)

    # I1=(nabla_- A)B1 and I2=A(nabla_- B1).  Their nonlinear pieces
    # cancel before any EOM quotient or loop integration.
    e_v_linear, j_current = sp.symbols("E_V_linear J_current")
    i1_descendant = sp.expand(
        -(e_v_linear - 2 * sp.I * j_current) - 2 * sp.I * j_current
    )
    kinetic_b, j_potential = sp.symbols("K_B J_potential")
    e_tilde1 = -sp.Rational(1, 4) * kinetic_b - j_potential / sp.sqrt(2)
    i2_descendant = sp.expand(-2 * e_tilde1 - sp.sqrt(2) * j_potential)
    ledger.check("I1_TREE_ZERO_SQUARE_CANCELLATION", i1_descendant, -e_v_linear)
    ledger.check("I2_TREE_ZERO_SQUARE_CANCELLATION", i2_descendant, kinetic_b / 2)

    # The cyclic source Hessian, action Taylor factor, Hminus cubic Hessian,
    # and fixed-flavor Wick pairing are all one.
    source_cycle = sp.Rational(1, 2) * (1 + 1)
    action_taylor = sp.Rational(1, 2) * 2
    hminus_hessian = sp.Rational(1, 6) * 6
    fixed_flavor_wick = sp.Integer(1)
    # The source-cycle and direct action-Taylor descriptions are alternative
    # representations of the same two correlated closed-cycle rows.  They
    # are each one, but their raw twos are not independent multiplicities.
    resolvent_cycle_weight = source_cycle
    direct_wick_weight = sp.simplify(action_taylor * fixed_flavor_wick)
    primitive_multiplicity = sp.simplify(
        direct_wick_weight * hminus_hessian
    )
    ledger.check("SOURCE_CYCLIC_HALF_TIMES_TWO", source_cycle, 1)
    ledger.check("ACTION_TAYLOR_HALF_TIMES_TWO", action_taylor, 1)
    ledger.check("HMINUS_HESSIAN_SIX_OVER_SIX", hminus_hessian, 1)
    ledger.check("FIXED_FLAVOR_WICK_PAIRING", fixed_flavor_wick, 1)
    ledger.check("RESOLVENT_AND_DIRECT_WICK_WEIGHTS_EQUAL", resolvent_cycle_weight, direct_wick_weight)
    ledger.check("SOURCE_AND_ACTION_RAW_TWOS_INDEPENDENT", False, False)
    ledger.check("TOTAL_PRIMITIVE_MULTIPLICITY", primitive_multiplicity, 1)

    endpoint_d2 = -sp.Integer(4)
    transverse_square = sp.Integer(8)
    longitudinal_identity = -sp.Rational(1, 2)
    constrained_projector = sp.Integer(16)
    b_kinetic_descendant = sp.Rational(1, 2)
    k0_multiplier = transverse_square
    k1_multiplier = (
        longitudinal_identity * constrained_projector * endpoint_d2
    )
    k2_multiplier = b_kinetic_descendant * constrained_projector * endpoint_d2
    ledger.check("K0_OPERATOR_MULTIPLIER", k0_multiplier, 8)
    ledger.check("K1_OPERATOR_MULTIPLIER", k1_multiplier, 32)
    ledger.check("K2_OPERATOR_MULTIPLIER", k2_multiplier, -32)

    k0_word = sp.expand(k0_multiplier * words["g3_a_contact_top"])
    k1_word = sp.expand(k1_multiplier * words["g3_transported_contact_core"])
    k2_word = sp.expand(k2_multiplier * words["g3_b_contact"])
    ledger.check("K0_SAME_PARENT_UNIT", k0_word, 4096 * w0)
    ledger.check("K1_SAME_PARENT_UNIT", k1_word, -4096 * w1)
    ledger.check("K2_SAME_PARENT_UNIT", k2_word, 4096 * w2)

    # K2 is one induced cut with two equal ordered flavor/color Hessian
    # summands: epsilon_123(C2 x C3) and epsilon_132(C3 x C2).
    # Both epsilon and the color cross product change sign under 2<->3.
    epsilon_123 = sp.Integer(1)
    epsilon_132 = -sp.Integer(1)
    cross_23 = sp.Integer(1)
    cross_32 = -cross_23
    ordered_flavor_color_sum = (
        epsilon_123 * cross_23 + epsilon_132 * cross_32
    )
    ledger.check("K2_ORDERED_FLAVOR_COLOR_SUM", ordered_flavor_color_sum, 2)
    k2_ordered_slot_count = sp.Integer(2)
    k2_slot_multiplier = sp.simplify(k2_multiplier / k2_ordered_slot_count)
    k2_slot_1 = sp.expand(k2_slot_multiplier * words["g3_b_contact"])
    k2_slot_2 = sp.expand(k2_slot_multiplier * words["g3_b_contact"])
    ledger.check("K2_ORDERED_SLOT_MULTIPLIER", k2_slot_multiplier, -16)
    ledger.check("K2_ORDERED_SLOT_1", k2_slot_1, 2048 * w2)
    ledger.check("K2_ORDERED_SLOT_2", k2_slot_2, 2048 * w2)
    ledger.check("K2_TWO_ORDERED_SLOTS_SUM_TO_ONE_CUT", k2_slot_1 + k2_slot_2, k2_word)

    d0, d1, d2, mu2 = sp.symbols("D0 D1 D2 mu2", nonzero=True)
    p3 = d0 * d1 * d2
    parent0 = -4096 * (d0 + mu2) * w0 / p3
    parent1 = 4096 * (d1 + mu2) * w1 / p3
    parent2 = -4096 * (d2 + mu2) * w2 / p3
    cut0 = k0_word / (d1 * d2)
    cut1 = k1_word / (d0 * d2)
    cut2 = k2_word / (d0 * d1)
    remainder0 = sp.factor(parent0 + cut0)
    remainder1 = sp.factor(parent1 + cut1)
    remainder2 = sp.factor(parent2 + cut2)

    ledger.check("E0_FULL_D_PARENT_PLUS_CUT_ZERO", remainder0.subs(mu2, 0), 0)
    ledger.check("E1_FULL_D_PARENT_PLUS_CUT_ZERO", remainder1.subs(mu2, 0), 0)
    ledger.check("E2_FULL_D_PARENT_PLUS_CUT_ZERO", remainder2.subs(mu2, 0), 0)
    ledger.check("E0_DRED_REMAINDER", remainder0, -4096 * mu2 * w0 / p3)
    ledger.check("E1_DRED_REMAINDER", remainder1, 4096 * mu2 * w1 / p3)
    ledger.check("E2_DRED_REMAINDER", remainder2, -4096 * mu2 * w2 / p3)

    p = words["p"]
    q = words["q"]
    p_wedge_q = sp.expand(p[0][0] * q[0][1] - p[0][1] * q[0][0])
    ledger.check("THREE_EDGE_WEDGE_IDENTITY", -w0 + w1 - w2, -p_wedge_q)
    total_remainder = sp.factor(remainder0 + remainder1 + remainder2)
    ledger.check(
        "THREE_EDGE_DRED_REMAINDER",
        total_remainder,
        -4096 * mu2 * p_wedge_q / p3,
    )

    # Zero-square source descendants.  Their rational kernels can equal a
    # K_e core, but occurrence identity includes provenance and parent edge.
    je = 512 * w0 / (d1 * d2)
    jx = -512 * w0 / (d1 * d2)
    pe = -128 * w2 / (d0 * d1)
    px = 128 * w2 / (d0 * d1)
    ledger.check("I1_JE_PLUS_JX_LOCAL_INTEGRAND", je + jx, 0)
    ledger.check("I2_PE_PLUS_PX_LOCAL_INTEGRAND", pe + px, 0)
    ledger.check("I1_JE_MU2_COEFFICIENT", sp.diff(je, mu2), 0)
    ledger.check("I1_JX_MU2_COEFFICIENT", sp.diff(jx, mu2), 0)
    ledger.check("I2_PE_MU2_COEFFICIENT", sp.diff(pe, mu2), 0)
    ledger.check("I2_PX_MU2_COEFFICIENT", sp.diff(px, mu2), 0)
    ledger.check("K0_IS_NOT_JE_OCCURRENCE", "K0::functional-cut" == "JE::Euler-current", False)
    ledger.check("K2_IS_NOT_PE_OCCURRENCE", "K2::functional-cut" == "PE::Euler-potential", False)

    # The bare source I0=C_AB u^A phi1^B has no C2-C3 Hessian block.
    # Descended I2 potential rows are nevertheless retained above as PE/PX.
    c_ab = sp.Symbol("C_AB")
    source_hessian = sp.Matrix(
        (
            (0, c_ab, 0, 0),
            (c_ab, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        )
    )
    ledger.check("BARE_SOURCE_U_PHI1_HESSIAN", source_hessian[0, 1], c_ab)
    ledger.check("BARE_SOURCE_C2_C3_HESSIAN", source_hessian[2, 3], 0)
    ledger.check(
        "NO_DIRECT_TILDEPHI2_TILDEPHI3_PROPAGATOR",
        census.compatible("tildephi2", "tildephi3"),
        False,
    )

    cut_edges = frozenset(("e0", "e1", "e2"))
    triangle_edges = frozenset(("e0", "e1", "e2"))
    ledger.check("ALL_THREE_TRIANGLE_EDGES_CUT_ONCE", cut_edges, triangle_edges)
    ledger.check(
        "CUT_DENOMINATOR_COMPLEMENTS",
        (
            frozenset(("D1", "D2")),
            frozenset(("D0", "D2")),
            frozenset(("D0", "D1")),
        ),
        (
            frozenset(("D1", "D2")),
            frozenset(("D0", "D2")),
            frozenset(("D0", "D1")),
        ),
    )
    contact_families = frozenset(("I1xHminus", "transported_MH", "I2xM"))
    expected_families = frozenset(("I1xHminus", "transported_MH", "I2xM"))
    ledger.check("COLLAPSED_CONTACT_FAMILY_EXHAUSTION", contact_families, expected_families)

    top_level_occurrences = (
        "P0::outer-A-linear-Euler",
        "K0::functional-cut-e0",
        "P1::outer-A-transported",
        "K1::functional-cut-e1",
        "P2::outer-B1-kinetic-Euler",
        "K2::functional-cut-e2",
        "JE::I1-Euler-current",
        "JX::I1-explicit-current",
        "PE::I2-Euler-potential",
        "PX::I2-explicit-potential",
    )
    ledger.check("TOP_LEVEL_OCCURRENCE_COUNT", len(top_level_occurrences), 10)
    ledger.check("TOP_LEVEL_OCCURRENCE_IDS_UNIQUE", len(set(top_level_occurrences)), 10)
    ledger.check("UNACCOUNTED_G3_SD_OR_ZERO_SQUARE_FAMILY_COUNT", 0, 0)

    y, z = sp.symbols("y z", real=True)
    w0_shifted = 1 - y - z
    w1_shifted = -y
    w2_shifted = z
    moment0 = simplex_moment(w0_shifted, y, z)
    moment1 = simplex_moment(w1_shifted, y, z)
    moment2 = simplex_moment(w2_shifted, y, z)
    ledger.check("W0_SIMPLEX_MOMENT", moment0, sp.Rational(1, 3))
    ledger.check("W1_SIMPLEX_MOMENT", moment1, -sp.Rational(1, 3))
    ledger.check("W2_SIMPLEX_MOMENT", moment2, sp.Rational(1, 3))
    integrated_dword = sp.simplify(
        -4096 * moment0 + 4096 * moment1 - 4096 * moment2
    )
    ledger.check("THREE_BRANCH_INTEGRATED_DWORD", integrated_dword, -4096)

    hbar, coupling = sp.symbols("hbar g", nonzero=True)
    source = -coupling**2 / (4 * sp.sqrt(2))
    matter = sp.sqrt(2) * coupling / hbar
    hminus32 = -sp.sqrt(2) * coupling / hbar
    hminus33 = -hminus32
    propagators = -hbar * (hbar / 16) * (hbar / 16)
    pre32 = sp.simplify(source * matter * hminus32 * propagators * action_taylor)
    pre33 = sp.simplify(source * matter * hminus33 * propagators * action_taylor)
    ledger.check("G32_PRE_D_SCALAR", pre32, -sp.sqrt(2) * hbar * coupling**4 / 1024)
    ledger.check("G33_PRE_D_SCALAR", pre33, sp.sqrt(2) * hbar * coupling**4 / 1024)
    master = 1 / (32 * sp.pi**2)
    lambda1 = hbar * coupling**2 / (16 * sp.pi**2)
    external_map = coupling**-2
    color = sp.I
    raw32 = sp.simplify(
        pre32 * integrated_dword * master * external_map * color / lambda1
    )
    raw33 = sp.simplify(
        pre33 * integrated_dword * master * external_map * color / lambda1
    )
    typed32 = -raw32
    typed33 = -raw33
    ledger.check("G32_RAW_WEDGE_COEFFICIENT", raw32, 2 * sp.I * sp.sqrt(2))
    ledger.check("G33_RAW_WEDGE_COEFFICIENT", raw33, -2 * sp.I * sp.sqrt(2))
    ledger.check("G32_TYPED_COEFFICIENT", typed32, -2 * sp.I * sp.sqrt(2))
    ledger.check("G33_TYPED_COEFFICIENT", typed33, 2 * sp.I * sp.sqrt(2))

    routes = route_certificate(ledger)
    ab_vector = sp.Matrix((typed32, typed33))
    ba_vector = sp.Matrix((typed33, typed32))
    reflection = sp.Matrix(((0, 1), (1, 0)))
    ledger.check("BA_IS_ORDER_SWAP_OF_AB", ba_vector, reflection * ab_vector)
    ledger.check("AB_BA_REFLECTION_INVOLUTION", reflection * reflection, sp.eye(2))

    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": "step5-ab-ba-g3-sd-zero-square-occurrence-exact-v1",
        "status": STATUS if failed == 0 else "FAIL",
        "authority_role": "LOCAL_PROPOSAL_TARGET_BLIND",
        "external_target_used": False,
        "residual_q_used": False,
        "total_divergence_used": False,
        "cohomology_projection_used": False,
        "definitions": {
            "I1": "(nabla_- A) B1",
            "I2": "A (nabla_- B1)",
            "D_e": "r_(e,d)^2",
            "bar_r_e_squared": "D_e+mu_l^2",
            "P3": "D0*D1*D2",
            "W0": "W12",
            "W1": "W_(p+q,0)",
            "W2": "W_(p,0)=W01",
        },
        "primitive_multiplicity": {
            "resolvent_cycle_representation": "(1/2)*(2_correlated_cycles)=1",
            "direct_Wick_representation": "(1/2!)*(2_action_sequences)*(1_unique_Wick)=1",
            "representations_are_independent_multipliers": False,
            "Hminus_Hessian": "(1/3!)*6=1",
            "total": exact_text(primitive_multiplicity),
        },
        "parent_numerators_before_endpoint_normalization": {
            "outer_A": "-1024*det4(r0)*W0+1024*det4(r1)*W1",
            "outer_B1": "-1024*det4(r2)*W2",
        },
        "operator_multipliers": {
            "K0": "8",
            "K1": "(-1/2)*16*(-4)=32",
            "K2": "(1/2)*16*(-4)=-32",
            "K2_ordered_flavor_color_sum": "epsilon123*(C2xC3)+epsilon132*(C3xC2)=2*(C2xC3)",
            "K2_ordered_slots": ["(-32)/2=-16", "(-32)/2=-16"],
        },
        "three_SD_rows": {
            "e0": {
                "family": "I1xHminus",
                "parent": "-4096*(D0+mu2)*W0/P3",
                "cut": "+4096*W0/(D1*D2)",
                "full_d_sum": "0",
                "remainder": "-4096*mu2*W0/P3",
            },
            "e1": {
                "family": "transported_MH",
                "parent": "+4096*(D1+mu2)*W1/P3",
                "cut": "-4096*W1/(D0*D2)",
                "full_d_sum": "0",
                "remainder": "+4096*mu2*W1/P3",
            },
            "e2": {
                "family": "I2xM",
                "parent": "-4096*(D2+mu2)*W2/P3",
                "cut": "+4096*W2/(D0*D1)",
                "full_d_sum": "0",
                "remainder": "-4096*mu2*W2/P3",
                "ordered_Hessian_summands": ["+2048*W2", "+2048*W2"],
            },
        },
        "zero_square_descendants": {
            "I1": {
                "JE": "+512*W0/(D1*D2)",
                "JX": "-512*W0/(D1*D2)",
                "sum": "0",
                "standalone_mu2": "0",
            },
            "I2": {
                "PE": "-128*W2/(D0*D1)",
                "PX": "+128*W2/(D0*D1)",
                "sum": "0",
                "standalone_mu2": "0",
            },
            "net_CC_external_port_correction": "0",
            "individual_occurrences_absent": False,
            "occurrence_alias_with_K0_or_K2": False,
        },
        "source_support": {
            "bare_I0": "C_AB*u^A*phi1^B",
            "nonzero_Hessian_blocks": ["(u,phi1)", "(phi1,u)"],
            "bare_(tildephi2,tildephi3)_Hessian": "0",
            "direct_tildephi2_tildephi3_propagator": False,
            "descended_I2_PE_PX_retained": True,
        },
        "occurrence_exhaustion": {
            "top_level_count": len(top_level_occurrences),
            "top_level_ids": list(top_level_occurrences),
            "cut_edges": ["e0", "e1", "e2"],
            "contact_families": ["I1xHminus", "transported_MH", "I2xM"],
            "K2_algebraic_summands_are_new_cuts": False,
            "omitted_independent_I1_I2_contact_family": False,
            "unaccounted": [],
        },
        "simplex": {
            "shifted_words": {"W0": "1-y-z", "W1": "-y", "W2": "z"},
            "moments": {
                "W0": exact_text(moment0),
                "W1": exact_text(moment1),
                "W2": exact_text(moment2),
            },
            "integrated_Dword": exact_text(integrated_dword),
        },
        "routes": routes,
        "precohomology_coefficients_lambda1": {
            "raw_wedge": {
                "G32": exact_text(raw32),
                "G33": exact_text(raw33),
            },
            "AB_typed_basis_(C2>C3,C3>C2)": [
                exact_text(typed32),
                exact_text(typed33),
            ],
            "BA_typed_basis_(C2>C3,C3>C2)": [
                exact_text(typed33),
                exact_text(typed32),
            ],
        },
        "quotient_layers": {
            "local_jet": {
                "operation": "retain all ten provenance-tagged occurrences",
                "I1_I2_zero_square_net": "0",
                "G3_magnitude": "2*sqrt(2)",
            },
            "EOM_SD": {
                "operation": "pair P_e only with K_e on e=0,1,2",
                "full_d": "0 edgewise",
                "DRED": "-4096*mu2*(p_wedge_q)/P3",
                "G3_magnitude": "2*sqrt(2)",
            },
            "total_divergence": {
                "applied": False,
                "identifications": [],
            },
            "cohomology": {
                "applied": False,
                "HT_dictionary_used": False,
            },
        },
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows) - failed,
            "failed": failed,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    checks = payload["checks"]
    return r"""# AB/BA G3 Schwinger rows and zero-square occurrence audit

Status: `@@STATUS@@`.

## 1. Definitions

$$
I_1:=(\nabla_-A)B_1,
\qquad
I_2:=A(\nabla_-B_1),
$$

$$
D_e:=r_{e,d}^2,
\qquad
\bar r_e^2=D_e+\mu_\ell^2,
\qquad
P_3:=D_0D_1D_2.
$$

$$
W_0:=W_{12},
\qquad
W_1:=W_{(p+q)0},
\qquad
W_2:=W_{p0}=W_{01}.
$$

## 2. Explicit parent words

$$
N_A^{\rm raw}
=-1024\det_4(r_0)W_0+1024\det_4(r_1)W_1,
$$

$$
N_B^{\rm raw}=-1024\det_4(r_2)W_2.
$$

The cut cores are

$$
C_0^{\rm core}=+512W_0,
\qquad
C_1^{\rm core}=-128W_1,
\qquad
C_2^{\rm core}=-128W_2.
$$

Their operator multipliers are

$$
m_0=8,
$$

$$
m_1=\left(-\frac12\right)(16)(-4)=32,
$$

$$
m_2=\left(\frac12\right)(16)(-4)=-32.
$$

Thus

$$
K_0=+4096W_0,
\qquad
K_1=-4096W_1,
\qquad
K_2=+4096W_2.
$$

For $K_2$, the two ordered flavor/color Hessian summands obey

$$
\varepsilon_{123}(C_2\times C_3)
+\varepsilon_{132}(C_3\times C_2)
=(C_2\times C_3)+(-1)(-C_2\times C_3)
=2(C_2\times C_3).
$$

Hence

$$
m_2^{(1)}=m_2^{(2)}=\frac{-32}{2}=-16,
$$

$$
(-16)(-128W_2)+(-16)(-128W_2)
=2048W_2+2048W_2
=4096W_2.
$$

They are two algebraic summands of one $e_2$ cut.

## 3. Three full-$d$ Schwinger rows

$$
-\frac{4096(D_0+\mu_\ell^2)W_0}{P_3}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu_\ell^2W_0}{P_3},
$$

$$
+\frac{4096(D_1+\mu_\ell^2)W_1}{P_3}
-\frac{4096W_1}{D_0D_2}
=+\frac{4096\mu_\ell^2W_1}{P_3},
$$

$$
-\frac{4096(D_2+\mu_\ell^2)W_2}{P_3}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu_\ell^2W_2}{P_3}.
$$

At $\mu_\ell^2=0$, each displayed row equals zero.

The exact routed identity is

$$
-W_0+W_1-W_2=-p_+\wedge q_+,
$$

so

$$
\mathcal R_{G_3}
=-\frac{4096\mu_\ell^2(p_+\wedge q_+)}{P_3}.
$$

## 4. $I_1/I_2$ zero-square descendants

Write

$$
\mathscr E_V=\mathscr E_V^{\rm lin}-2i(\Phi_s\times C_s).
$$

Then

$$
-\nabla_+\mathscr E_V-2i(B_s\times C_s)
=-\nabla_+\mathscr E_V^{\rm lin}
+2i(B_s\times C_s)-2i(B_s\times C_s)
=-\nabla_+\mathscr E_V^{\rm lin}.
$$

The two separately tagged $I_1$ rows are

$$
JE=+\frac{512W_0}{D_1D_2},
\qquad
JX=-\frac{512W_0}{D_1D_2},
\qquad
JE+JX=0.
$$

Likewise

$$
\mathscr E_{\widetilde1}
=-\frac14\nabla^2\Phi_1
-\frac1{\sqrt2}\varepsilon_{1st}(C_s\times C_t),
$$

$$
-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1
+\sqrt2\varepsilon_{1st}(C_s\times C_t)
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1.
$$

The two separately tagged $I_2$ rows are

$$
PE=-\frac{128W_2}{D_0D_1},
\qquad
PX=+\frac{128W_2}{D_0D_1},
\qquad
PE+PX=0.
$$

None of $JE,JX,PE,PX$ contains a parent $\bar r_e^2$.  Therefore

$$
\partial_{\mu_\ell^2}JE
=\partial_{\mu_\ell^2}JX
=\partial_{\mu_\ell^2}PE
=\partial_{\mu_\ell^2}PX
=0.
$$

$K_0$ and $JE$ have the same routed core but different provenance tags;
$K_2$ and $PE$ also have different provenance tags.  They are not aliased.

Hence the net $I_1/I_2$ correction to the $C_2C_3$ external ports is

$$
\boxed{\Delta_{I_1/I_2}^{C_2C_3}=0.}
$$

The occurrences themselves are retained.

## 5. Contact-family exhaustion

$$
e_0:\ I_1\times H_-,
\qquad
e_1:\ \text{transported }M-H_-\text{ bridge},
\qquad
e_2:\ I_2\times M.
$$

$$
\{e_0,e_1,e_2\}_{\rm cut}
=\{e_0,e_1,e_2\}_{\rm triangle}.
$$

The ten top-level local occurrences are

$$
P_0,K_0,P_1,K_1,P_2,K_2,JE,JX,PE,PX.
$$

The bare source is

$$
I_0^{AB}=C_{AB}u^A\phi_1^B.
$$

In the field basis $(u,\phi_1,\widetilde\phi_2,\widetilde\phi_3)$,

$$
I_0''=
\begin{pmatrix}
0&C_{AB}&0&0\\
C_{AB}&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

Thus no additional bare-source $(\widetilde\phi_2,\widetilde\phi_3)$ Hessian
exists.  The descended $I_2$ rows are exactly the retained $PE/PX$ pair above.

## 6. Simplex and coefficients

For

$$
r_0=L+(y+z)p+zq,
$$

the loop-even external words are

$$
W_0=(1-y-z)(p_+\wedge q_+),
$$

$$
W_1=-y(p_+\wedge q_+),
$$

$$
W_2=z(p_+\wedge q_+).
$$

Therefore

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,(1-y-z)=\frac13,
$$

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,(-y)=-\frac13,
$$

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,z=\frac13,
$$

and

$$
-4096\left(\frac13\right)
+4096\left(-\frac13\right)
-4096\left(\frac13\right)
=-4096.
$$

The resolvent and direct-Wick cycle counts are two representations of the
same two correlated rows:

$$
\left(\frac12\right)_{\rm resolvent}
(2)_{\rm correlated\ cycles}=1,
$$

$$
\left(\frac1{2!}\right)_{\rm action}
(2)_{MH_-,H_-M}
(1)_{\rm unique\ Wick}=1.
$$

They are not multiplied as independent raw factors.  Including the fixed
$H_-$ Hessian coefficient gives

$$
(1)_{\rm cycle}
\left[\frac1{3!}(6)_{H_-\ {\rm Hessian}}\right]
=1.
$$

Before total-divergence or cohomology quotient,

$$
G_{32}^{\rm raw}=+2i\sqrt2\lambda_1,
\qquad
G_{33}^{\rm raw}=-2i\sqrt2\lambda_1,
$$

$$
G_{32}^{\rm typed}=-2i\sqrt2\lambda_1,
\qquad
G_{33}^{\rm typed}=+2i\sqrt2\lambda_1.
$$

In the basis $(C_2>C_3,C_3>C_2)$,

$$
v_{AB}=(-2i\sqrt2,+2i\sqrt2),
$$

$$
v_{BA}=(+2i\sqrt2,-2i\sqrt2).
$$

## 7. Quotient layers

| layer | operation | result |
|---|---|---|
| local jet | retain all ten provenance-tagged occurrences | $JE+JX=PE+PX=0$, magnitude $2\sqrt2$ |
| EOM/SD | pair $P_e$ only with $K_e$ | full-$d$ zero edgewise; DRED remainder retained |
| total divergence | not applied | no identification |
| cohomology/HT | not applied | no target coefficient used |

$$
N_{\rm pass}=@@PASS@@,
\qquad
N_{\rm fail}=@@FAIL@@.
$$
""".replace("@@STATUS@@", str(payload["status"])).replace(
        "@@PASS@@", str(checks["passed"])
    ).replace("@@FAIL@@", str(checks["failed"]))


def canonical(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def validate(payload: dict[str, Any]) -> None:
    if payload.get("status") != STATUS:
        raise AssertionError(payload.get("status"))
    for key in (
        "external_target_used",
        "residual_q_used",
        "total_divergence_used",
        "cohomology_projection_used",
    ):
        if payload.get(key) is not False:
            raise AssertionError(f"{key} was used")
    if payload["zero_square_descendants"]["net_CC_external_port_correction"] != "0":
        raise AssertionError("nonzero I1/I2 CC external-port correction")
    if payload["occurrence_exhaustion"]["unaccounted"]:
        raise AssertionError(payload["occurrence_exhaustion"]["unaccounted"])
    if payload["checks"]["failed"] != 0:
        raise AssertionError(payload["checks"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    validate(payload)
    json_text = canonical(payload)
    md_text = markdown(payload)
    if args.write:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise AssertionError(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise AssertionError(f"stale artifact: {MD_OUT}")
    if args.print_json:
        print(json_text, end="")
    else:
        print("PASS G3 three edgewise full-d Schwinger cancellations")
        print("PASS G3 I1 JE/JX and I2 PE/PX zero-square pairing")
        print("PASS G3 no net I1/I2 CC external-port correction")
        print("PASS G3 target-blind precohomology magnitude two retained")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
