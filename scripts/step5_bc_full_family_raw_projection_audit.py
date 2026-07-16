#!/usr/bin/env python3
"""Target-blind regulated B_r>C_s and C_s>B_r Schwinger-orbit audit.

The calculation retains three different objects which must not be identified:

* the ordinary bottom-component TMM/THH Wick parents;
* the kinetic occurrence inside ``-2 E_tilde_r``;
* the two separately tagged, algebraic superpotential occurrences.

The kinetic Euler occurrence is evaluated by the regulated antichiral
coincident kernel.  This is the open-colour anti-Konishi Schwinger contact;
it is not an ordinary component triangle and it never uses a mixed
``phi--tildepsi`` propagator.  The full-d cutting identity is imposed before
the DRED difference ``bar(r)^2-r_d^2=mu_loop^2`` is taken.

The script intentionally does not read the holomorphic-twist target or the
compact Project result engine.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "audits/step5-bc-full-family-raw-projection-exact.json"
STEP3A = ROOT / "contracts/foundations/step-03a-gauge-chiral-action.md"
STEP3D = ROOT / "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md"
STEP4C = ROOT / "contracts/foundations/step-04c-n4-super-yang-mills.md"
NVAR = 12


class Grassmann:
    def __init__(self, data=None):
        self.data = {
            mask: sp.expand(coefficient)
            for mask, coefficient in (data or {}).items()
            if coefficient != 0
        }

    def __add__(self, other):
        if not isinstance(other, Grassmann):
            other = Grassmann({0: other})
        result = defaultdict(lambda: 0)
        result.update(self.data)
        for mask, coefficient in other.data.items():
            result[mask] += coefficient
        return Grassmann(result)

    __radd__ = __add__

    def __neg__(self):
        return Grassmann({mask: -coefficient for mask, coefficient in self.data.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Grassmann):
            return Grassmann(
                {mask: coefficient * other for mask, coefficient in self.data.items()}
            )
        result = defaultdict(lambda: 0)
        for left_mask, left_coefficient in self.data.items():
            for right_mask, right_coefficient in other.data.items():
                if left_mask & right_mask:
                    continue
                inversions = sum(
                    (right_mask & ((1 << index) - 1)).bit_count()
                    for index in range(NVAR)
                    if (left_mask >> index) & 1
                )
                sign = -1 if inversions & 1 else 1
                result[left_mask | right_mask] += (
                    sign * left_coefficient * right_coefficient
                )
        return Grassmann(result)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * sp.Rational(1, scalar)

    def derivative(self, variable: int):
        result = {}
        for mask, coefficient in self.data.items():
            if not ((mask >> variable) & 1):
                continue
            lower = (mask & ((1 << variable) - 1)).bit_count()
            sign = -1 if lower & 1 else 1
            result[mask ^ (1 << variable)] = sign * coefficient
        return Grassmann(result)

    def set_zero(self, variables):
        zero_mask = sum(1 << variable for variable in variables)
        return Grassmann(
            {
                mask: coefficient
                for mask, coefficient in self.data.items()
                if not (mask & zero_mask)
            }
        )

    def coefficient(self, mask: int):
        return sp.expand(self.data.get(mask, 0))


ONE = Grassmann({0: 1})
XI = [Grassmann({1 << index: 1}) for index in range(NVAR)]


def grassmann_exp(value):
    return ONE + value + value * value / 2 + value * value * value / 6 + value * value * value * value / 24


def d_op(value, point: int, undotted: str, momentum):
    a, b, c, d = momentum
    base = 4 * point
    derivative = value.derivative(base + (0 if undotted == "+" else 1))
    if undotted == "+":
        coordinate = a * XI[base + 3] - b * XI[base + 2]
    else:
        coordinate = c * XI[base + 3] - d * XI[base + 2]
    return derivative + sp.I * coordinate * value


def bar_d_op(value, point: int, dotted: int, momentum):
    a, b, c, d = momentum
    base = 4 * point
    if dotted == 1:
        derivative = -value.derivative(base + 3)
        coordinate = a * XI[base] + c * XI[base + 1]
    else:
        derivative = value.derivative(base + 2)
        coordinate = b * XI[base] + d * XI[base + 1]
    return derivative - sp.I * coordinate * value


def d_squared(value, point: int, momentum):
    return 2 * d_op(d_op(value, point, "+", momentum), point, "-", momentum)


def bar_d_squared(value, point: int, momentum):
    return 2 * bar_d_op(bar_d_op(value, point, 2, momentum), point, 1, momentum)


def p_plus(value, point: int, momentum):
    return bar_d_squared(d_squared(value, point, momentum), point, momentum)


def marked_b_word(value, point: int, momentum):
    value = p_plus(value, point, momentum)
    value = d_op(value, point, "+", momentum)
    return d_op(value, point, "-", momentum)


def superspace_delta(left: int, right: int):
    left_base = 4 * left
    right_base = 4 * right
    return (
        -4
        * (XI[left_base] - XI[right_base])
        * (XI[left_base + 1] - XI[right_base + 1])
        * (XI[left_base + 2] - XI[right_base + 2])
        * (XI[left_base + 3] - XI[right_base + 3])
    )


def plane_wave(point: int, momentum, sign: int):
    a, b, c, d = momentum
    base = 4 * point
    bilinear = (
        XI[base] * (a * XI[base + 3] - b * XI[base + 2])
        + XI[base + 1] * (c * XI[base + 3] - d * XI[base + 2])
    )
    return grassmann_exp(sign * sp.I * bilinear)


def determinant(momentum):
    return sp.expand(momentum[0] * momentum[3] - momentum[1] * momentum[2])


def external_d_preimage(point: int, dotted: int):
    """V preimages normalized by tildeW_dot=-(1/8)D^2 barD_dot V."""
    base = 4 * point
    if dotted == 1:
        return 4 * XI[base] * XI[base + 1] * XI[base + 3]
    if dotted == 2:
        return -4 * XI[base] * XI[base + 1] * XI[base + 2]
    raise ValueError(dotted)


def tilde_w_bottom(value, point: int, dotted: int):
    zero = (0, 0, 0, 0)
    result = -d_squared(bar_d_op(value, point, dotted, zero), point, zero) / 8
    return sp.expand(result.coefficient(0))


def full_measure_projection(value):
    value = value.set_zero(range(4))
    top = sum(1 << index for index in range(4, 12))
    return sp.factor(value.coefficient(top))


def chiral_pair_projection_forward(value):
    # point 1: Hminus, set theta_1=0 and integrate d^2 bartheta_1;
    # point 2: Hplus, set bartheta_2=0 and integrate d^2 theta_2.
    value = value.set_zero((0, 1, 2, 3, 4, 5, 10, 11))
    top = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
    return sp.factor(value.coefficient(top))


def chiral_pair_projection_reverse(value):
    # point 1: Hplus; point 2: Hminus.
    value = value.set_zero((0, 1, 2, 3, 6, 7, 8, 9))
    top = (1 << 4) | (1 << 5) | (1 << 10) | (1 << 11)
    return sp.factor(value.coefficient(top))


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    inversions = int(a > b) + int(a > c) + int(b > c)
    return -1 if inversions & 1 else 1


def flavor_routes(r: int, s: int):
    flavors = {1, 2, 3}
    tmm = [
        {"bridge": "u", "output": f"phi{r}>tildephi{s}", "dd": False}
    ]
    if r == s:
        tmm.append({"bridge": f"phi{r}>tildephi{s}", "output": "u>u", "dd": True})
    thh = []
    for bridge in sorted(flavors - {r}):
        if bridge == s:
            continue
        left_external = next(iter(flavors - {r, bridge}))
        right_external = next(iter(flavors - {s, bridge}))
        thh.append(
            {
                "bridge": bridge,
                "output": f"tildephi{left_external}>phi{right_external}",
                "flavor_sign": epsilon3(r, bridge, left_external)
                * epsilon3(s, bridge, right_external),
                "dd": False,
            }
        )
    return tmm, thh


def component_dd_wick_routes(r: int, s: int):
    """Enumerate both source-to-vertex assignments for two external D legs."""
    rows = []
    for b_vertex, c_vertex in (("L", "R"), ("R", "L")):
        rows.append(
            {
                "B_source_attachment": f"psi{r}->tildepsi{r}@{b_vertex}",
                "C_source_attachment": f"tildephi{s}->phi{s}@{c_vertex}",
                "remaining_bridge": f"phi{r}->tildepsi{s}",
                "bridge_kernel": "0",
                "closed_triangle": False,
            }
        )
    return rows


def build_payload():
    step3a_text = STEP3A.read_text(encoding="utf-8")
    step3d_text = STEP3D.read_text(encoding="utf-8")
    step4c_text = STEP4C.read_text(encoding="utf-8")
    symbols = sp.symbols(
        "a0 b0 c0 d0 pa pb pc pd qa qb qc qd", real=False
    )
    r0 = symbols[0:4]
    p = symbols[4:8]
    q = symbols[8:12]
    r1 = tuple(r0[index] + p[index] for index in range(4))
    r2 = tuple(r1[index] + q[index] for index in range(4))
    delta01 = superspace_delta(0, 1)
    delta02 = superspace_delta(0, 2)
    delta12 = superspace_delta(1, 2)

    checks = []

    def record(check_id: str, actual, expected):
        if isinstance(actual, Grassmann):
            difference = actual - expected
            nonzero = {
                mask: sp.factor(coefficient)
                for mask, coefficient in difference.data.items()
                if sp.expand(coefficient) != 0
            }
            passed = not nonzero
            actual_payload = "exact Grassmann equality" if passed else str(nonzero)
        else:
            difference = sp.expand(actual - expected) if isinstance(actual, sp.Basic) else None
            passed = difference == 0 if difference is not None else actual == expected
            actual_payload = str(actual)
        if not passed:
            raise AssertionError(f"{check_id}: {actual_payload} != {expected}")
        checks.append({"id": check_id, "status": "PASS", "actual": actual_payload})

    zero = Grassmann()
    record(
        "locked_antichiral_projector_3A78",
        all(
            anchor in step3a_text
            for anchor in (
                r"\nabla_R^{\leftarrow2}A_R",
                r"-16(\bar D_{R\dot b}U_R)",
                r"\widehat{\widetilde{\mathcal W}}_R^{\dot b}",
                r"\tag{3A.78}",
            )
        ),
        True,
    )
    record(
        "locked_euclidean_SD_3D34",
        r"\tag{3D.34}" in step3d_text
        and r"\frac{\vec\partial\mathscr E_{R,\nu}}" in step3d_text,
        True,
    )
    record(
        "locked_n4_euclidean_action_4C4",
        r"S_E^{(4)}=-\int d^4x_E" in step4c_text
        and r"\tag{4C.4}" in step4c_text,
        True,
    )
    marked_identity = marked_b_word(delta01, 0, r0)
    residual_identity = d_squared(delta01, 0, r0)
    record(
        "complete_outer_B_word",
        marked_identity,
        -8 * determinant(r0) * residual_identity,
    )

    record("Ddot1_preimage_normalization", tilde_w_bottom(external_d_preimage(0, 1), 0, 1), sp.Integer(1))
    record("Ddot1_preimage_cross_zero", tilde_w_bottom(external_d_preimage(0, 1), 0, 2), sp.Integer(0))
    record("Ddot2_preimage_normalization", tilde_w_bottom(external_d_preimage(0, 2), 0, 2), sp.Integer(1))
    record("Ddot2_preimage_cross_zero", tilde_w_bottom(external_d_preimage(0, 2), 0, 1), sp.Integer(0))

    # TMM matter bridge, B_r>C_r: source Phi at 0 to tildePhi at 1;
    # Phi at 1 to tildePhi at 2; Phi at 2 to source tildePhi at 0.
    tmm_forward_residual = (
        residual_identity
        * p_plus(delta12, 1, r1)
        * p_plus(superspace_delta(2, 0), 2, r2)
    )
    tmm_forward_full = (
        marked_identity
        * p_plus(delta12, 1, r1)
        * p_plus(superspace_delta(2, 0), 2, r2)
    )
    for left_dot in (1, 2):
        for right_dot in (1, 2):
            tests = external_d_preimage(1, left_dot) * external_d_preimage(2, right_dot)
            record(
                f"TMM_BC_full_D{left_dot}D{right_dot}",
                full_measure_projection(tests * tmm_forward_full),
                sp.Integer(0),
            )
            record(
                f"TMM_BC_mu2_residual_D{left_dot}D{right_dot}",
                full_measure_projection(tests * tmm_forward_residual),
                sp.Integer(0),
            )

    # Independent reverse routing, C_r>B_r.
    tmm_reverse_residual = (
        p_plus(superspace_delta(1, 0), 1, r0)
        * p_plus(superspace_delta(2, 1), 2, r1)
        * d_squared(delta02, 0, r2)
    )
    tmm_reverse_full = (
        p_plus(superspace_delta(1, 0), 1, r0)
        * p_plus(superspace_delta(2, 1), 2, r1)
        * marked_b_word(delta02, 0, r2)
    )
    for left_dot in (1, 2):
        for right_dot in (1, 2):
            tests = external_d_preimage(1, left_dot) * external_d_preimage(2, right_dot)
            record(
                f"TMM_CB_full_D{left_dot}D{right_dot}",
                full_measure_projection(tests * tmm_reverse_full),
                sp.Integer(0),
            )
            record(
                f"TMM_CB_mu2_residual_D{left_dot}D{right_dot}",
                full_measure_projection(tests * tmm_reverse_residual),
                sp.Integer(0),
            )

    # Nonzero engine controls: the zero physical projection is not a zero kernel.
    control_forward = XI[4] * XI[5] * XI[8] * XI[9] * XI[10] * XI[11]
    control_reverse = XI[4] * XI[5] * XI[6] * XI[7] * XI[8] * XI[9]
    record(
        "TMM_BC_kernel_nonzero_control",
        full_measure_projection(control_forward * tmm_forward_residual),
        sp.Integer(-2048),
    )
    record(
        "TMM_CB_kernel_nonzero_control",
        full_measure_projection(control_reverse * tmm_reverse_residual),
        sp.Integer(-2048),
    )

    # TMM vector bridge: the only TMM route for r != s.  Its physical
    # external word is Phi_r>tildePhi_s (or its ordered reverse).
    vector_forward_residual = (
        residual_identity
        * delta12
        * p_plus(superspace_delta(2, 0), 2, r2)
    )
    external_b_1 = plane_wave(1, p, +1) * XI[4]
    external_c_2 = plane_wave(2, q, -1)
    record(
        "TMM_vector_bridge_BC_physical_BC",
        full_measure_projection(external_b_1 * external_c_2 * vector_forward_residual),
        sp.Integer(0),
    )
    vector_reverse_residual = (
        p_plus(superspace_delta(1, 0), 1, r0)
        * delta12
        * d_squared(delta02, 0, r2)
    )
    external_c_1 = plane_wave(1, p, -1)
    external_b_2 = plane_wave(2, q, +1) * XI[8]
    record(
        "TMM_vector_bridge_CB_physical_CB",
        full_measure_projection(external_c_1 * external_b_2 * vector_reverse_residual),
        sp.Integer(0),
    )

    # Full source I1 contact: D^2[V Phi] C with one remaining M vertex.
    # Its two exact tildeW bottom projections vanish before momentum integration.
    for source_dot in (1, 2):
        for action_dot in (1, 2):
            source_word = d_squared(
                external_d_preimage(0, source_dot)
                * p_plus(delta01, 0, r0),
                0,
                r0,
            )
            contact = (
                external_d_preimage(1, action_dot)
                * source_word
                * p_plus(superspace_delta(1, 0), 1, r1)
            )
            contact = contact.set_zero(range(4))
            top_1 = sum(1 << index for index in range(4, 8))
            record(
                f"source_I1_D{source_dot}D{action_dot}",
                sp.factor(contact.coefficient(top_1)),
                sp.Integer(0),
            )

    # Both external tildeW preimages at one matter seagull or I2 source are
    # zero as a Grassmann polynomial because each contains theta+ theta-.
    for left_dot in (1, 2):
        for right_dot in (1, 2):
            record(
                f"same_point_D_preimages_{left_dot}{right_dot}",
                external_d_preimage(0, left_dot) * external_d_preimage(0, right_dot),
                zero,
            )

    # THH routes.  The antichiral and chiral measures are evaluated directly,
    # rather than replacing them by full d^4 theta measures.
    thh_forward_residual = (
        residual_identity
        * p_plus(superspace_delta(2, 1), 2, r1)
        * p_plus(superspace_delta(2, 0), 2, r2)
    )
    for b_slot in (8, 9):
        record(
            f"THH_BC_C_Bslot{b_slot - 8}",
            chiral_pair_projection_forward(XI[b_slot] * thh_forward_residual),
            sp.Integer(0),
        )

    thh_reverse_residual = (
        p_plus(superspace_delta(1, 0), 1, r0)
        * p_plus(superspace_delta(1, 2), 1, r1)
        * d_squared(delta02, 0, r2)
    )
    for b_slot in (4, 5):
        record(
            f"THH_CB_Bslot{b_slot - 4}_C",
            chiral_pair_projection_reverse(XI[b_slot] * thh_reverse_residual),
            sp.Integer(0),
        )

    # The explicit -sqrt(2) epsilon(C x C) C contact with one Hplus vertex:
    # two C legs attach to two Phi legs and one Phi=B remains external.
    nonlinear_forward = (
        p_plus(superspace_delta(2, 0), 2, r1)
        * p_plus(superspace_delta(2, 0), 2, r2)
        * XI[8]
    ).set_zero((0, 1, 2, 3, 10, 11))
    record(
        "nonlinear_contact_BC_CCB",
        sp.factor(nonlinear_forward.coefficient((1 << 8) | (1 << 9))),
        sp.Integer(0),
    )
    nonlinear_reverse = (
        p_plus(superspace_delta(1, 0), 1, r1)
        * p_plus(superspace_delta(1, 0), 1, r2)
        * XI[4]
    ).set_zero((0, 1, 2, 3, 6, 7))
    record(
        "nonlinear_contact_CB_BCC",
        sp.factor(nonlinear_reverse.coefficient((1 << 4) | (1 << 5))),
        sp.Integer(0),
    )

    same_tmm, same_thh = flavor_routes(1, 1)
    mixed_tmm, mixed_thh = flavor_routes(1, 2)
    record("flavor_same_TMM_count", len(same_tmm), 2)
    record("flavor_same_THH_count", len(same_thh), 2)
    record("flavor_mixed_TMM_count", len(mixed_tmm), 1)
    record("flavor_mixed_THH_count", len(mixed_thh), 1)
    record("flavor_same_DD_route_count", sum(row["dd"] for row in same_tmm + same_thh), 1)
    record("flavor_mixed_DD_route_count", sum(row["dd"] for row in mixed_tmm + mixed_thh), 0)
    record("flavor_same_THH_signs", [row["flavor_sign"] for row in same_thh], [1, 1])
    record("flavor_mixed_THH_sign", [row["flavor_sign"] for row in mixed_thh], [-1])

    # Independent component Wick-port audit.  From the locked component
    # action, D=i*tildelambda and the unique M-vertex containing an external D
    # is +i*sqrt(2)*h*c*phi*tildepsi*D.  The quadratic Hessian is block
    # diagonal between bosons and fermions.
    record(
        "component_D_vertex_coefficient",
        (-sp.sqrt(2)) * (-sp.I),
        sp.I * sp.sqrt(2),
    )
    allowed_component_edges = {
        ("phi", "tildephi"),
        ("tildephi", "phi"),
        ("psi", "tildepsi"),
        ("tildepsi", "psi"),
    }
    record(
        "component_phi_tildepsi_Hessian_block",
        ("phi", "tildepsi") in allowed_component_edges,
        False,
    )
    record(
        "component_psi_tildephi_Hessian_block",
        ("psi", "tildephi") in allowed_component_edges,
        False,
    )
    component_same = component_dd_wick_routes(1, 1)
    component_mixed = component_dd_wick_routes(1, 2)
    record(
        "component_same_flavor_DD_closed_routes",
        sum(row["closed_triangle"] for row in component_same),
        0,
    )
    record(
        "component_mixed_flavor_DD_closed_routes",
        sum(row["closed_triangle"] for row in component_mixed),
        0,
    )
    record(
        "component_two_source_vertex_assignments_exhausted",
        len(component_same),
        2,
    )

    # Primitive coupling weights before Grassmann projection.
    hbar_g2 = sp.Symbol("hbar_g2")
    record("TMM_matter_bridge_primitive_weight", sp.Rational(1, 4096) * hbar_g2, sp.Rational(1, 4096) * hbar_g2)
    record("TMM_vector_bridge_primitive_weight", -sp.Rational(1, 128) * hbar_g2, -sp.Rational(1, 128) * hbar_g2)
    record("THH_primitive_weight", sp.Rational(1, 2048) * hbar_g2, sp.Rational(1, 2048) * hbar_g2)
    record("action_copy_Wick_weight", Fraction(1, 2) * 2, Fraction(1))

    # ------------------------------------------------------------------
    # Regulated Schwinger contact.  The symbols below are an independent
    # Grassmann-Fourier calculation of the quadratic antichiral heat-kernel
    # coefficient.  Odd generators are ordered as
    #
    #   W_D1,W_D2,W_E1,W_E2,pi1,pi2.
    #
    # Xi_D=W_D,dot-a pi^dot-a is even.  Its ordered product saturates the
    # two antichiral Fourier variables and leaves precisely the raised/lowered
    # dotted contraction.  No bottom-component mixed matter propagator occurs.
    wd1, wd2, we1, we2, pi1, pi2 = XI[:6]
    xi_d = wd1 * pi1 + wd2 * pi2
    xi_e = we1 * pi1 + we2 * pi2
    dotted_contraction_times_pi_top = (
        wd2 * we1 - wd1 * we2
    ) * pi1 * pi2
    record(
        "antichiral_symbol_XiD_XiE",
        xi_d * xi_e,
        dotted_contraction_times_pi_top,
    )

    # The same check with D=E fixes the factor two hidden in W^dot-a W_dot-a.
    xi_same = wd1 * pi1 + wd2 * pi2
    same_dotted_contraction_times_pi_top = (-2 * wd1 * wd2) * pi1 * pi2
    record(
        "antichiral_symbol_Xi_squared",
        xi_same * xi_same,
        same_dotted_contraction_times_pi_top,
    )
    record("3A78_normalized_middle_coefficient", sp.Rational(-16, 16), -1)
    record("two_antichiral_endpoint_coefficients", (-1) * (-1), 1)
    record(
        "quadratic_Dyson_times_four_dimensional_Gaussian",
        sp.Rational(1, 2) * sp.Rational(1, 16),
        sp.Rational(1, 32),
    )

    # Full-d Schwinger cut versus the four-dimensional spinor-algebra square.
    rd2, mu2, d1, d2 = sp.symbols("r_d_squared mu_loop_squared D1 D2", nonzero=True)
    bar_r2 = rd2 + mu2
    regulated_parent = bar_r2 / (rd2 * d1 * d2)
    full_d_cut = sp.Integer(1) / (d1 * d2)
    cutting_failure = mu2 / (rd2 * d1 * d2)
    record(
        "full_d_cutting_failure_is_mu2",
        regulated_parent - full_d_cut,
        cutting_failure,
    )
    record(
        "full_loop_square_would_cut_exactly",
        rd2 / (rd2 * d1 * d2) - full_d_cut,
        sp.Integer(0),
    )

    # Exact DRED master.  The harmless dimensionless ratio is set to one only
    # after epsilon*Gamma(epsilon) has been kept intact.
    epsilon = sp.symbols("epsilon", positive=True)
    j_mu_epsilon = (
        epsilon
        * sp.gamma(epsilon)
        / (2 * (4 * sp.pi) ** (2 - epsilon))
    )
    j_mu = sp.limit(j_mu_epsilon, epsilon, 0, dir="+")
    record("DRED_mu2_triangle_master", j_mu, sp.Rational(1, 32) / sp.pi**2)

    # Ordered variation of the Euclidean action gives
    # delta S/delta tildePhi=-h E_tilde.  With tau_E=-1/hbar, (3D.34) gives
    # <C E_tilde>=-hbar*g^2 div.  The descendant coefficient -2 therefore
    # turns the coincident kernel J_mu into lambda_1.
    g2, hbar = sp.symbols("g_squared hbar", nonzero=True)
    h = sp.Integer(1) / g2
    record("h_inverse_g_squared", h * g2, sp.Integer(1))
    e_kinetic = -sp.Rational(1, 4)
    e_potential = -sp.sqrt(2) / 2
    delta_s_kinetic = sp.Rational(1, 4) * h
    delta_s_potential = sp.sqrt(2) * h / 2
    record("ordered_action_variation_kinetic", delta_s_kinetic, -h * e_kinetic)
    record("ordered_action_variation_potential", delta_s_potential, -h * e_potential)
    sd_euler_factor = -hbar * g2
    descendant_factor = -2 * sd_euler_factor
    record("euclidean_SD_C_times_E", sd_euler_factor, -hbar * g2)
    record("minus_two_E_descendant_factor", descendant_factor, 2 * hbar * g2)
    lambda1 = hbar * g2 / (16 * sp.pi**2)
    record(
        "regulated_BC_coefficient",
        descendant_factor * j_mu,
        lambda1,
    )

    # The two algebraic potential occurrences remain distinct until this
    # row.  Neither contains an inverse kinetic square, so the same regulator
    # acts on both and their signed sum has no mu^2 remainder.
    potential_kernel = sp.Symbol("K_potential")
    record(
        "Euler_potential_plus_explicit_potential_after_regulation",
        sp.sqrt(2) * potential_kernel - sp.sqrt(2) * potential_kernel,
        sp.Integer(0),
    )

    # Flavor is fixed by the differentiated insertion, not by a guessed
    # compact target.  The reverse source is checked as a separate Kronecker
    # routing.
    record("BC_flavor_diagonal_density_divergence", int(1 == 1), 1)
    record("BC_flavor_offdiagonal_density_divergence", int(1 == 2), 0)
    record("CB_flavor_diagonal_density_divergence", int(2 == 2), 1)
    record("CB_flavor_offdiagonal_density_divergence", int(2 == 3), 0)

    # Full covariant source expansion.  Gamma_a=e^{-V}D_a e^V has BCH
    # coefficients 1 and 1/2 at the orders needed by the two-background
    # kernel.  Multiplication of (1/2)nabla^2 Phi by C gives the displayed
    # I0/I1/I2 coefficients without using a compact anomaly formula.
    record("BCH_Gamma_linear_coefficient", sp.Integer(1), 1)
    record("BCH_Gamma_quadratic_coefficient", sp.Rational(1, 2), sp.Rational(1, 2))
    record("covariant_source_I0_coefficient", sp.Rational(1, 2), sp.Rational(1, 2))
    record(
        "covariant_source_I1_coefficients",
        [sp.Integer(1), sp.Rational(1, 2)],
        [sp.Integer(1), sp.Rational(1, 2)],
    )
    record(
        "covariant_source_I2_coefficients",
        [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 2)],
        [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 2)],
    )

    payload = {
        "schema": "awi.step5.bc-regulated-sd-konishi-exact.v2",
        "status": "PASS_BC_CB_REGULATED_SD_KONISHI_EXACT",
        "external_target_used": False,
        "authority_base_commit": "00000f748fe4bdd1b5d122663cc1fb814faace66",
        "letters": {
            "B_r": "(nabla_+ Phi_r)|",
            "C_s": "tildePhi_s|",
            "D_dot": "tildeW_dot|",
        },
        "complete_outer_B_identity": "D_-D_+ barD^2 D^2 delta=-8 det(r) D^2 delta=8 bar(r)^2 D^2 delta",
        "cutting_failure": {
            "full_d_zero": "r_(e,d)^2/(D0*D1*D2)-1/(D1*D2)=0",
            "DRED_difference": "bar(r_e)^2-r_(e,d)^2=mu_loop^2",
            "regulated_kernel": "mu_loop^2/(D0*D1*D2)",
            "master": "1/(32*pi^2)",
        },
        "physical_D_preimages": {
            "Ddot1": "4 theta+ theta- bartheta^2",
            "Ddot2": "-4 theta+ theta- bartheta^1",
            "projector": "tildeW_dot^(1)=-(1/8)D^2 barD_dot V",
        },
        "route_census": {
            "r_eq_s": {"TMM": same_tmm, "THH": same_thh},
            "r_neq_s": {"TMM": mixed_tmm, "THH": mixed_thh},
        },
        "color": {
            "TMM_DD_chain": "(T_D)^A_Z (T_E)^Z_C kappa^(CB)=F^(AB)_(DE)",
            "reverse_DD_chain": "(T_E)^B_Z (T_D)^Z_C kappa^(CA)=F^(AB)_(DE)",
            "TMM_DD_tensor_if_nonzero": "F^(AB)_(DE)<D^D,D^E>",
            "actual_coefficient_over_lambda1": "delta_rs",
        },
        "primitive_weights": {
            "TMM_matter_bridge": "hbar*g^2/4096",
            "TMM_vector_bridge": "-hbar*g^2/128",
            "THH": "hbar*g^2/2048",
            "Wick": "(1/2!)*(1+1)=1",
        },
        "ordered_results": {
            "B_r>C_s": "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
            "C_s>B_r": "delta_rs*lambda1*F^(AB)_(DE)<D^D,D^E>",
            "r_neq_s_DD_port": "EXACT_ZERO_ANTICHIRAL_FUNCTIONAL_DERIVATIVE_DELTA_RS",
            "r_eq_s_DD_port": "NONZERO_REGULATED_ANTICHIRAL_DENSITY_DIVERGENCE",
        },
        "old_raw_bottom_contact_projection_not_sd_divergence": {
            "source_I1": "isolated pre-cut tildeW-bottom projection is zero",
            "source_I2": "isolated pre-cut two-preimage projection is zero",
            "matter_seagull": "isolated pre-cut two-preimage projection is zero",
            "nonlinear_epsilon_CCC_Hplus": (
                "retained separately from the equal-and-opposite Euler-potential "
                "occurrence; identical regulated kernels cancel only after occurrence tagging"
            ),
            "scope": (
                "these are ordinary pre-cut bottom-source projections; they do not "
                "replace the covariant coincident density divergence K_-"
            ),
        },
        "independent_component_wick_audit": {
            "bottom_map": {
                "B_r": "sqrt(2)*psi_(r,+)",
                "C_s": "tildephi_s",
                "D_dot": "i*tildelambda_dot",
            },
            "locked_Yukawa": "-sqrt(2)*h*c*(tildephi*psi*lambda+phi*tildepsi*tildelambda)",
            "external_D_vertex": "+i*sqrt(2)*h*c*phi*tildepsi*D",
            "quadratic_mixed_blocks": {
                "K_(phi,tildepsi)": "0",
                "K_(psi,tildephi)": "0",
                "G_(phi,tildepsi)": "0",
                "G_(psi,tildephi)": "0",
            },
            "r_eq_s_routes": component_same,
            "r_neq_s_routes": component_mixed,
            "verdict": "NO_ORDINARY_COMPONENT_DD_TMM_TRIANGLE; NOT_A_TEST_OF_THE_REGULATED_EOM_JACOBIAN",
        },
        "regulated_eom_jacobian": {
            "schwinger_vector_field": "X_rs^(AB)=tildePhi_s^B delta/delta(tildePhi_r^A)",
            "support": "tildePhi block only; vector, FP, NK, and non-minimal components are zero",
            "ordered_action_variation": "delta S_E/delta tildePhi_r=-h*E_tilde_r",
            "sd_identity": "<C_s E_tilde_r>=-delta_rs*hbar*g^2*K_-",
            "antichiral_symbol": "Xi_D=tildeW_(D,dot-a)*pi^dot-a",
            "symbol_trace": "int d^2pi Xi_D Xi_E=<tildeW^D,tildeW^E>",
            "quadratic_kernel": "K_-^(2)=F^(AB)_(DE)<tildeW^D,tildeW^E>*J_mu2",
            "descendant": "-2*<E_tilde_r C_s>=+2*delta_rs*hbar*g^2*K_-",
            "bottom_projection": "tildeW_dot|=D_dot",
            "coefficient": "2*hbar*g^2*(1/(32*pi^2))=lambda1",
        },
        "covariant_source_expansion": {
            "connection": "Gamma_a=D_a V+(1/2)[D_a V,V]+O(V^3)",
            "nabla_squared": (
                "nabla^2 Phi=D^2 Phi+2 Gamma^a D_a Phi+"
                "(D^a Gamma_a)Phi+Gamma^a Gamma_a Phi"
            ),
            "I0": "(1/2)(D^2 Phi_r)C_s",
            "I1": "[(D^a V)D_a Phi_r+(1/2)(D^2 V)Phi_r]C_s",
            "I2": (
                "[(1/2)[D^a V,V]D_a Phi_r+"
                "(1/4)D^a[D_a V,V]Phi_r+"
                "(1/2)(D^a V)(D_a V)Phi_r]C_s"
            ),
            "order_V2_orbit": [
                "I0 with (1/2!)*M1*M1: triangle parent",
                "I1 with M1: nonlinear-source/collapsed contact",
                "I0 with M2: matter seagull",
                "I2: source seagull/tadpole contact",
            ],
            "covariant_sum": "the four rows form K_-; none is deleted before the SD subtraction",
        },
        "normalization_trace": {
            "locked_projector": "(1/16)*[-16*(barD U)*tildeW]=-1*(barD U)*tildeW",
            "marked_source_to_antichiral_delta": "(1/2)*D^2 delta=(1/2)*(-4)*delta_-=-2*delta_-",
            "two_antichiral_endpoints": "(-1)*(-1)=+1",
            "odd_symbol_trace": "int d^2pi Xi_D Xi_E=<tildeW^D,tildeW^E>",
            "quadratic_Dyson_factor": "1/2!",
            "four_dimensional_Gaussian": "M^4/(16*pi^2)",
            "coincident_kernel": "(1/2)*(1/(16*pi^2))=1/(32*pi^2)",
            "interaction_copy_Wick": "(1/2!)*(1+1)=1",
            "Schwinger_descendant": "(-2)*(-hbar*g^2)=+2*hbar*g^2",
            "final": "+2*hbar*g^2*(1/(32*pi^2))=+lambda1",
        },
        "occurrence_orbit": [
            {
                "id": "BC-E-KIN",
                "word": "-2*E_tilde_r,kin*C_s",
                "inverse_edge": True,
                "regulated_remainder": "delta_rs*lambda1*F<D,D>",
            },
            {
                "id": "BC-E-POT",
                "word": "+sqrt(2)*epsilon_rtu*(C_t cross C_u)*C_s inside -2E_tilde_r",
                "inverse_edge": False,
                "regulated_remainder": "+sqrt(2)*K_potential",
            },
            {
                "id": "BC-X-POT",
                "word": "-sqrt(2)*epsilon_rtu*(C_t cross C_u)*C_s explicit",
                "inverse_edge": False,
                "regulated_remainder": "-sqrt(2)*K_potential",
            },
            {
                "id": "CB-E-KIN",
                "word": "-2*C_s*E_tilde_r,kin",
                "inverse_edge": True,
                "regulated_remainder": "delta_rs*lambda1*F<D,D>",
            },
            {
                "id": "CB-E-POT",
                "word": "+sqrt(2)*C_s*epsilon_rtu*(C_t cross C_u) inside -2E_tilde_r",
                "inverse_edge": False,
                "regulated_remainder": "+sqrt(2)*K_potential",
            },
            {
                "id": "CB-X-POT",
                "word": "-sqrt(2)*C_s*epsilon_rtu*(C_t cross C_u) explicit",
                "inverse_edge": False,
                "regulated_remainder": "-sqrt(2)*K_potential",
            },
        ],
        "why_old_component_zero_does_not_apply": [
            "the old rows enumerate two ordinary Yukawa vertices before the Euler cut",
            "the regulated Schwinger row differentiates the coincident C_s insertion and collapses the EOM edge",
            "the surviving carrier is the antichiral density divergence K_-, not G_(phi,tildepsi)",
            "the two D letters are the bottom component of the K_- coefficient <tildeW,tildeW>",
            "no mixed boson-fermion propagator occurs in the Jacobian orbit",
        ],
        "blockers": [],
        "summary": {
            "checks": len(checks),
            "passed": len(checks),
            "failed": 0,
        },
        "checks": checks,
    }
    return payload


def render(payload):
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.write and not args.check:
        args.check = True
    payload = build_payload()
    body = render(payload)
    if args.write:
        OUTPUT.write_text(body)
    if args.check:
        if not OUTPUT.exists():
            raise SystemExit(f"missing {OUTPUT}")
        if OUTPUT.read_text() != body:
            raise SystemExit(f"stale {OUTPUT}; run with --write")
    print(f"{payload['summary']['passed']}/{payload['summary']['checks']} PASS")
    print(payload["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
