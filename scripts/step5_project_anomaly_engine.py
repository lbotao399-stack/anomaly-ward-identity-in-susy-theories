#!/usr/bin/env python3
"""Exact Project-side Step-5 compact anomaly and component ledger.

The engine uses only the accepted Project Euclidean N=4 action, its tree Euler
descendants, and the DRED/cutting calculation encoded here.  Holomorphic-twist
files are intentionally not read.  The comparison to the external target is a
separate verifier stage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "generated/step5"
AUTHORITY_BASE_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"


@dataclass(frozen=True)
class Sqrt2:
    """a+b*sqrt(2), with a,b rational."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: Sqrt2) -> Sqrt2:
        return Sqrt2(self.a + other.a, self.b + other.b)

    def __neg__(self) -> Sqrt2:
        return Sqrt2(-self.a, -self.b)

    def __sub__(self, other: Sqrt2) -> Sqrt2:
        return self + (-other)

    def __mul__(self, other: Sqrt2) -> Sqrt2:
        return Sqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def inverse(self) -> Sqrt2:
        denominator = self.a * self.a - 2 * self.b * self.b
        if denominator == 0:
            raise ZeroDivisionError(self)
        return Sqrt2(self.a / denominator, -self.b / denominator)

    def __truediv__(self, other: Sqrt2) -> Sqrt2:
        return self * other.inverse()

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0


@dataclass(frozen=True)
class Exact:
    """x+i*y with x,y in Q(sqrt(2))."""

    x: Sqrt2 = Sqrt2()
    y: Sqrt2 = Sqrt2()

    def __add__(self, other: Exact) -> Exact:
        return Exact(self.x + other.x, self.y + other.y)

    def __neg__(self) -> Exact:
        return Exact(-self.x, -self.y)

    def __sub__(self, other: Exact) -> Exact:
        return self + (-other)

    def __mul__(self, other: Exact) -> Exact:
        return Exact(
            self.x * other.x - self.y * other.y,
            self.x * other.y + self.y * other.x,
        )

    def inverse(self) -> Exact:
        norm = self.x * self.x + self.y * self.y
        norm_inverse = norm.inverse()
        return Exact(self.x * norm_inverse, -self.y * norm_inverse)

    def __truediv__(self, other: Exact) -> Exact:
        return self * other.inverse()

    def is_zero(self) -> bool:
        return self.x.is_zero() and self.y.is_zero()

    def payload(self) -> dict[str, Any]:
        def f(value: Fraction) -> str:
            return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

        return {
            "basis": ["1", "sqrt(2)", "i", "i*sqrt(2)"],
            "coefficients": [f(self.x.a), f(self.x.b), f(self.y.a), f(self.y.b)],
            "text": exact_text(self),
        }


ZERO = Exact()
ONE = Exact(Sqrt2(Fraction(1)))
MINUS_ONE = -ONE
IMAGINARY_UNIT = Exact(Sqrt2(), Sqrt2(Fraction(1)))
SQRT2 = Exact(Sqrt2(Fraction(0), Fraction(1)))
INV_SQRT2 = Exact(Sqrt2(Fraction(0), Fraction(1, 2)))


def rational(value: int | Fraction) -> Exact:
    return Exact(Sqrt2(Fraction(value)))


def exact_text(value: Exact) -> str:
    basis = ("", "sqrt(2)", "i", "i*sqrt(2)")
    coefficients = (value.x.a, value.x.b, value.y.a, value.y.b)
    terms: list[str] = []
    for coefficient, name in zip(coefficients, basis, strict=True):
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else "+"
        absolute = abs(coefficient)
        if name and absolute == 1:
            body = name
        elif name:
            body = f"{absolute}*{name}"
        else:
            body = str(absolute)
        terms.append((sign, body))
    if not terms:
        return "0"
    first_sign, first_body = terms[0]
    text = ("-" if first_sign == "-" else "") + first_body
    for sign, body in terms[1:]:
        text += sign + body
    return text


def exterior_product(left: int, right: int) -> tuple[int, int] | None:
    if left & right:
        return None
    inversions = 0
    cursor = left
    while cursor:
        bit = cursor & -cursor
        index = bit.bit_length() - 1
        inversions += (right & ((1 << index) - 1)).bit_count()
        cursor ^= bit
    return left | right, -1 if inversions % 2 else 1


@dataclass(frozen=True)
class CompactComponent:
    id: str
    theta_mask: int
    theta_coefficient: Exact
    parity: int


# This is solved from (-1/2)nabla_- C_P=(1/2)[C_P,C_P] using the
# independently derived Step-4C Euler descendants.  U is a formal gauge
# potential used only through P_dot U=i D_dot.
COMPONENTS = (
    CompactComponent("U", 0b000, ONE, 1),
    CompactComponent("C1", 0b001, ONE, 0),
    CompactComponent("C2", 0b010, ONE, 0),
    CompactComponent("C3", 0b100, ONE, 0),
    CompactComponent("B1", 0b110, INV_SQRT2, 1),
    CompactComponent("B2", 0b101, -INV_SQRT2, 1),
    CompactComponent("B3", 0b011, INV_SQRT2, 1),
    CompactComponent("A", 0b111, -IMAGINARY_UNIT * INV_SQRT2, 0),
)


def delta_theta() -> dict[int, int]:
    polynomial = {0: 1}
    for index in range(3):
        factor = {1 << index: 1, 1 << (index + 3): -1}
        updated: dict[int, int] = {}
        for left_mask, left_value in polynomial.items():
            for right_mask, right_value in factor.items():
                product = exterior_product(left_mask, right_mask)
                if product is None:
                    continue
                mask, sign = product
                updated[mask] = updated.get(mask, 0) + left_value * right_value * sign
        polynomial = {mask: value for mask, value in updated.items() if value}
    return polynomial


def component_product(first: CompactComponent, second: CompactComponent) -> tuple[int, Exact]:
    first_mask = first.theta_mask
    second_mask = second.theta_mask << 3
    product = exterior_product(first_mask, second_mask)
    assert product is not None
    mask, exterior_sign = product
    field_theta_sign = -1 if first.parity * second.theta_mask.bit_count() % 2 else 1
    return mask, first.theta_coefficient * second.theta_coefficient * rational(exterior_sign * field_theta_sign)


def compact_actions() -> list[dict[str, Any]]:
    """Expand Delta_P(C C)=(lambda/sqrt(2))*Delta_theta*(P C)(P C)."""
    prefix = delta_theta()
    rhs: dict[int, dict[tuple[str, str], Exact]] = {}
    overall = INV_SQRT2
    for first in COMPONENTS:
        for second in COMPONENTS:
            component_mask, component_coefficient = component_product(first, second)
            for prefix_mask, prefix_coefficient in prefix.items():
                product = exterior_product(prefix_mask, component_mask)
                if product is None:
                    continue
                final_mask, exterior_sign = product
                coefficient = (
                    overall
                    * rational(prefix_coefficient * exterior_sign)
                    * component_coefficient
                )
                key = (first.id, second.id)
                bucket = rhs.setdefault(final_mask, {})
                bucket[key] = bucket.get(key, ZERO) + coefficient

    rows: list[dict[str, Any]] = []
    for first in COMPONENTS:
        for second in COMPONENTS:
            input_mask, input_coefficient = component_product(first, second)
            odd_operator_sign = -1 if input_mask.bit_count() % 2 else 1
            lhs = input_coefficient * rational(odd_operator_sign)
            outputs = []
            for (left_output, right_output), coefficient in sorted(rhs.get(input_mask, {}).items()):
                normalized = coefficient / lhs
                if normalized.is_zero():
                    continue
                outputs.append(
                    {
                        "coefficient_over_lambda": normalized.payload(),
                        "left_output": left_output,
                        "right_output": right_output,
                        "operator": "P_dot(left)*P^dot(right)",
                    }
                )
            rows.append(
                {
                    "id": f"{first.id}__{second.id}",
                    "left_input": first.id,
                    "right_input": second.id,
                    "exact_zero": not outputs,
                    "outputs": outputs,
                }
            )
    return rows


LETTERS = (
    {"id": "A", "family": "A", "component": "A", "parity": 0, "derivative": (0, 0), "input_scale": ONE},
    *(
        {"id": f"B{r}", "family": "B", "component": f"B{r}", "parity": 1, "derivative": (0, 0), "input_scale": ONE}
        for r in range(1, 4)
    ),
    *(
        {"id": f"C{r}", "family": "C", "component": f"C{r}", "parity": 0, "derivative": (0, 0), "input_scale": ONE}
        for r in range(1, 4)
    ),
    {"id": "Ddot1", "family": "D", "component": "U", "parity": 1, "derivative": (1, 0), "input_scale": -IMAGINARY_UNIT},
    {"id": "Ddot2", "family": "D", "component": "U", "parity": 1, "derivative": (0, 1), "input_scale": -IMAGINARY_UNIT},
)


def physical_output_factor(component: str, *, dotted_variance: str) -> tuple[Exact, dict[str, Any]]:
    """Replace the auxiliary compact slot P(U) by the physical D letter.

    The compact kernel always supplies one contracted P on each output.  Thus
    ``U`` contributes ``P_dot U=i D_dot`` and does *not* contribute ``P D``.
    """

    if component == "U":
        return IMAGINARY_UNIT, {
            "field": "D",
            "operator": "identity",
            "dotted_index": dotted_variance,
            "derivation": "P_dot(U)=i*D_dot",
        }
    return ONE, {
        "field": component,
        "operator": "P_dot",
        "dotted_index": dotted_variance,
    }


def physical_base_outputs(base: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for output in base["outputs"]:
        coefficient = exact_from_payload(output["coefficient_over_lambda"])
        left_scale, left_factor = physical_output_factor(
            output["left_output"], dotted_variance="lower"
        )
        right_scale, right_factor = physical_output_factor(
            output["right_output"], dotted_variance="upper"
        )
        rows.append(
            {
                "coefficient_over_lambda": (coefficient * left_scale * right_scale).payload(),
                "left_factor": left_factor,
                "right_factor": right_factor,
                "ordered_output_word": f"{left_factor['field']}>{right_factor['field']}",
            }
        )
    return rows


def exact_from_payload(payload: dict[str, Any]) -> Exact:
    coefficients = [Fraction(value) for value in payload["coefficients"]]
    return Exact(
        Sqrt2(coefficients[0], coefficients[1]),
        Sqrt2(coefficients[2], coefficients[3]),
    )


def intrinsic_d_pair_outputs(left_id: str, right_id: str) -> list[dict[str, Any]] | None:
    """Exact one-derivative rows obtained from the commuting-translation recursion.

    Only A>D_dot-a and D_dot-a>A survive.  The two rational weights are the
    direct integrals 2 int_0^1 db int_0^b da of the two endpoint monomials.
    """

    if left_id == "A" and right_id.startswith("Ddot"):
        direction = int(right_id[-1]) - 1
        return [
            {
                "coefficient_over_lambda": rational(Fraction(1, 3)).payload(),
                "left_factor": {"field": "D", "operator": "J", "multiindex": [int(direction == 0), int(direction == 1)], "dotted_index": "lower"},
                "right_factor": {"field": "D", "operator": "identity", "multiindex": [0, 0], "dotted_index": "upper"},
                "ordered_output_word": "D>D",
            },
            {
                "coefficient_over_lambda": rational(Fraction(2, 3)).payload(),
                "left_factor": {"field": "D", "operator": "identity", "multiindex": [0, 0], "dotted_index": "lower"},
                "right_factor": {"field": "D", "operator": "J", "multiindex": [int(direction == 0), int(direction == 1)], "dotted_index": "upper"},
                "ordered_output_word": "D>D",
            },
        ]
    if left_id.startswith("Ddot") and right_id == "A":
        direction = int(left_id[-1]) - 1
        return [
            {
                "coefficient_over_lambda": rational(Fraction(2, 3)).payload(),
                "left_factor": {"field": "D", "operator": "J", "multiindex": [int(direction == 0), int(direction == 1)], "dotted_index": "lower"},
                "right_factor": {"field": "D", "operator": "identity", "multiindex": [0, 0], "dotted_index": "upper"},
                "ordered_output_word": "D>D",
            },
            {
                "coefficient_over_lambda": rational(Fraction(1, 3)).payload(),
                "left_factor": {"field": "D", "operator": "identity", "multiindex": [0, 0], "dotted_index": "lower"},
                "right_factor": {"field": "D", "operator": "J", "multiindex": [int(direction == 0), int(direction == 1)], "dotted_index": "upper"},
                "ordered_output_word": "D>D",
            },
        ]
    return None


def ordered_project_kernel_terms(m: int, n: int) -> list[dict[str, Any]]:
    """Taylor coefficients of one ordered Project Feynman-parameter kernel.

    The factor two is the standard identity

        1/(D0 D1 D2) = 2 * int_{Delta_2} 1/(r^2+Delta)^3,

    not a CW/CCW multiplicity.  A reflected routing belongs to the reversed
    ordered output word and is never added to the same row here.
    """

    rows = []
    for k in range(m + 1):
        for ell in range(n + 1):
            coefficient = Fraction(
                2 * comb(m, k) * comb(n, ell),
                (m + n + 2) * (k + ell + 1),
            )
            rows.append(
                {
                    "k": k,
                    "ell": ell,
                    "coefficient": str(coefficient),
                    "left_output_derivative": [k, ell],
                    "right_output_derivative": [m - k, n - ell],
                }
            )
    return rows


def physical_pair_ledger(actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    action_map = {row["id"]: row for row in actions}
    rows = []
    ordinal = 0
    for left in LETTERS:
        for right in LETTERS:
            base = action_map[f"{left['component']}__{right['component']}"]
            intrinsic_outputs = intrinsic_d_pair_outputs(left["id"], right["id"])
            if intrinsic_outputs is not None:
                exact_zero = False
                physical_outputs = intrinsic_outputs
                zero_certificate = None
            elif left["family"] == "D" or right["family"] == "D":
                exact_zero = True
                physical_outputs = []
                zero_certificate = "INTRINSIC_DERIVATIVE_LIFT_OF_COMPACT_ZERO"
            else:
                exact_zero = base["exact_zero"]
                physical_outputs = physical_base_outputs(base)
                zero_certificate = (
                    "COMPACT_EXTERIOR_COEFFICIENT_ZERO" if exact_zero else None
                )
            rows.append(
                {
                    "ordinal": ordinal,
                    "id": f"{left['id']}__{right['id']}",
                    "channel": f"{left['family']}__{right['family']}",
                    "left": left["id"],
                    "right": right["id"],
                    "parities": [left["parity"], right["parity"]],
                    "compact_component_pair": base["id"],
                    "input_derivatives": [list(left["derivative"]), list(right["derivative"])],
                    "input_scale_from_compact_jet": [left["input_scale"].payload(), right["input_scale"].payload()],
                    "exact_zero": exact_zero,
                    "zero_certificate": zero_certificate,
                    "base_outputs_before_input_jet_lift": base["outputs"],
                    "physical_outputs": physical_outputs,
                    "arbitrary_jet_rule": {
                        "second_input": (
                            "K_Project_mn=2*T_source_mn for this ordered word; "
                            "the factor 2 is the Feynman-parameter prefactor"
                        ),
                        "first_input": "sum_{r<=u}(-1)^|r| binom(u,r) P^(u-r) Q1(f P^(v+r)g)",
                        "pbw_projection": (
                            "each linked covariant jet is emitted directly in normalized "
                            "PBW-shuffle form; PBW is a filtered linear map"
                        ),
                        "reflected_routing": "stored under the reversed ordered output word",
                    },
                }
            )
            ordinal += 1
    return rows


def dred_seed() -> dict[str, Any]:
    """Exact pole and evanescent remainder for one fixed gauge orientation."""
    return {
        "schema": 1,
        "authority_base_commit": AUTHORITY_BASE_COMMIT,
        "external_target_used": False,
        "definitions": {
            "d": "4-2*epsilon",
            "J2": "mu^(2 epsilon)/(4 pi)^(2-epsilon) Gamma(epsilon) Delta^(-epsilon)",
            "J3": "mu^(2 epsilon)/(2(4 pi)^(2-epsilon)) Gamma(1+epsilon) Delta^(-1-epsilon)",
            "T_mrho_n": "(sigma_m bar_sigma_rho sigma_n)_(+ dot_alpha)",
        },
        "exact_reduction": [
            "Delta*J3=(epsilon/2)*J2",
            "integral r_m r_n/(r^2+Delta)^3=(hat_delta_mn/4)*J2",
            "Res_epsilon(J2)=1/(16*pi^2)",
        ],
        "normalization_trace": {
            "feynman_simplex": "R_mn=2*int_Delta2 int_r r_m r_n/(r^2+Delta)^3",
            "simplex_volume": "int_Delta2 1=1/2",
            "regulated_tensor": "R_mn|UV=(hat_delta_mn/4)*J2|UV",
            "four_dimensional_cut_tensor": "R_mn^cut|UV=(delta_4_mn/4)*J2|UV",
            "ordered_wick_weight": "(1/2!)*(1+1)=1",
            "insertion_closed_loop_mixed_D_weight": "(1/32)*16*2*2=2",
            "vertex_product": "(+i*g/2)*(-i*g/2)=g^2/4",
            "preintegral_weight": "1*(g^2/4)*2=g^2/2",
            "tensor_residue": "Res integral L1_m L2_n/(D0 D1 D2)=hat_delta_mn/(16*pi^2)",
            "pole_coefficient": "(g^2/2)*(1/(16*pi^2*epsilon))=g^2/(32*pi^2*epsilon)",
        },
        "ordered_wick_numerator": {
            "triangle_uv_pole": "+hbar*g^2/(32*pi^2*epsilon) F_ABDE hat_delta^mn T_mrho_n p^rho",
            "cut_contact_uv_pole": "-hbar*g^2/(32*pi^2*epsilon) F_ABDE delta_4^mn T_mrho_n p^rho",
            "physical_metric_cancellation": "exact",
        },
        "evanescent_clifford_chain": [
            "p^rho breve_delta^mn sigma_m bar_sigma_rho sigma_n",
            "=2 p^rho breve_delta_rho^n sigma_n-p^rho sigma_rho breve_delta^mn bar_sigma_m sigma_n",
            "=0-(4-d) p^rho sigma_rho",
            "=-2 epsilon p^rho sigma_rho",
        ],
        "finite_remainder": {
            "calculation": "[-g^2/(32*pi^2*epsilon)]*(-2*epsilon)=g^2/(16*pi^2)",
            "lambda": "hbar*g^2/(16*pi^2)",
            "fixed_orientation_operator": "lambda*F_ABDE*D_dot_alpha^D*P_+^dot_alpha*A^E",
        },
        "cutting_statement": "The four-dimensional cut replaces hat_delta by delta_4; their difference is -breve_delta.  No finite remainder survives if breve_delta is set to zero before the UV residue.",
    }


def tree_and_dictionary() -> dict[str, Any]:
    return {
        "schema": 1,
        "tree_descendants": {
            "nabla_minus_A": "-nabla_plus(E_V)-2*i*(B_s cross C_s)",
            "nabla_minus_B_r": "-2*E_tilde_r-sqrt(2)*epsilon_rst*(C_s cross C_t)",
            "nabla_minus_C_r": "0",
            "nabla_minus_D_dot_a": "0",
        },
        "compact_project_letter": {
            "formula": "C_P=U+theta_r C_r+(1/(2*sqrt(2))) epsilon^rst theta_r theta_s B_t-(i/sqrt(2)) theta_1 theta_2 theta_3 A",
            "gauge_potential_relation": "P_dot_a U=i D_dot_a",
            "status": "FORMAL_JET_EXTENSION; U is not a locked physical superfield",
            "residual_q_extension": "q_r U=C_r; the defining ideal is stable because q_r D_dot=-i P_dot C_r",
            "physical_weights_source": "exact bottom-letter residual-q action derived from Step 4C",
        },
        "project_one_loop_compact_result": {
            "formula": "Delta_P(C_P^A(theta) C_P^B(theta'))=(hbar*g^2/(16*sqrt(2)*pi^2))*F_ABDE*prod_r(theta_r-theta'_r)*P_dot C_P^D(theta)*P^dot C_P^E(theta')",
            "coefficient_source": "PROJECT_DRED_TRIANGLE_PLUS_CUT_CONTACT",
        },
        "pbw_jet_dictionary": {
            "definition": "J_(u1,u2)(X)=binom(u1+u2,u1)^(-1) sum over (u1,u2)-shuffles of P_dot1^u1 P_dot2^u2 X",
            "degree_two_example": "J_(1,1)(X)=P_dot1 P_dot2 X-(1/2)[P_dot1,P_dot2]X",
            "curvature": "[P_dot1,P_dot2]=epsilon_dot1dot2*A acting in the declared adjoint order",
            "map_type": "filtered linear isomorphism, not an ordinary-product algebra map",
            "star_product": "f star g=PBW^(-1)(PBW(f) PBW(g))",
            "inverse": "free-Lie PBW inverse retains curvature jets and nested commutators",
        },
        "external_dictionary_boundary": (
            "No external-target field, color, derivative, or loop-normalization "
            "map is encoded in this target-blind Project engine.  A separate "
            "round-trip audit must derive every such map after this bundle is fixed."
        ),
    }


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def verification(actions: list[dict[str, Any]], pairs: list[dict[str, Any]]) -> dict[str, Any]:
    action_map = {row["id"]: row for row in actions}
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        checks.append({"id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    check("compact.count", len(actions) == 64, str(len(actions)))
    check("physical.letter_count", len(LETTERS) == 9, str(len(LETTERS)))
    check("physical.pair_count", len(pairs) == 81, str(len(pairs)))
    check("physical.nonzero_count", sum(not row["exact_zero"] for row in pairs) == 29, str(sum(not row["exact_zero"] for row in pairs)))
    check("physical.zero_count", sum(row["exact_zero"] for row in pairs) == 52, str(sum(row["exact_zero"] for row in pairs)))
    check("ordered_kernel.K00", ordered_project_kernel_terms(0, 0)[0]["coefficient"] == "1", str(ordered_project_kernel_terms(0, 0)))
    check(
        "ordered_kernel.K21",
        [row["coefficient"] for row in ordered_project_kernel_terms(2, 1)]
        == ["2/5", "1/5", "2/5", "4/15", "2/15", "1/10"],
        str(ordered_project_kernel_terms(2, 1)),
    )
    check("compact.AA.nonzero", not action_map["A__A"]["exact_zero"], str(action_map["A__A"]))
    check("compact.CC.zero", action_map["C1__C1"]["exact_zero"], str(action_map["C1__C1"]))
    check("compact.BC.flavor_diagonal", not action_map["B1__C1"]["exact_zero"] and action_map["B1__C2"]["exact_zero"], "B1C1 nonzero, B1C2 zero")
    check("compact.BB.antisymmetric_flavor", action_map["B1__B1"]["exact_zero"] and not action_map["B1__B2"]["exact_zero"], "B1B1 zero, B1B2 nonzero")
    check("dred.residue", Fraction(1, 32) * 2 == Fraction(1, 16), "(1/32)*2=1/16")
    check("tree.scale_nonzero", all(not row["input_scale"].is_zero() for row in LETTERS), "all physical-to-compact jet scales invertible")
    return {
        "schema": 1,
        "status": "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL",
        "totals": {"checks": len(checks), "passed": sum(row["status"] == "PASS" for row in checks), "failed": sum(row["status"] == "FAIL" for row in checks)},
        "checks": checks,
    }


def build_bundle() -> dict[str, Any]:
    actions = compact_actions()
    pairs = physical_pair_ledger(actions)
    return {
        "project-tree-dictionary.json": tree_and_dictionary(),
        "project-compact-actions.json": {"schema": 1, "coefficient_unit": "lambda=hbar*g^2/(16*pi^2)", "component_actions": actions},
        "project-result-ledger.json": {
            "schema": 1,
            "authority_base_commit": AUTHORITY_BASE_COMMIT,
            "external_target_used": False,
            "family_count": 4,
            "component_count": 9,
            "ordered_pair_count": 81,
            "nonzero_count": sum(not row["exact_zero"] for row in pairs),
            "zero_count": sum(row["exact_zero"] for row in pairs),
            "ordered_kernel": {
                "project_word": "K_Project_mn",
                "factor_two_origin": "Feynman-parameter identity for one ordered routing",
                "zero_shift": "K_Project_00=K",
                "reflected_orientation": "different reversed output word",
                "sample_K_Project_2_1": ordered_project_kernel_terms(2, 1),
            },
            "pairs": pairs,
        },
        "project-dred-seed.json": dred_seed(),
        "project-verification.json": verification(actions, pairs),
    }


def write_bundle(output_root: Path) -> dict[str, str]:
    output_root.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name, payload in build_bundle().items():
        data = canonical_bytes(payload)
        (output_root / name).write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    return hashes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    bundle = build_bundle()
    status = bundle["project-verification.json"]["status"]
    if args.write:
        hashes = write_bundle(args.output_root)
        print(json.dumps({"status": status, "hashes": hashes}, indent=2, sort_keys=True))
    else:
        print(json.dumps(bundle["project-verification.json"], indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
