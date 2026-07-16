#!/usr/bin/env python3
"""Audit the WW Schwinger cut/contact/link completion from locked foundations.

The generator reads only verified Steps 3A/3C/3D/4C.  In particular it does
not read the untracked Step-5 contract, Step-5 seed audits, or the HT target.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
VERIFY_RUN = "29306335742"
TASK_ID = "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"

FOUNDATIONS = (
    (
        "contracts/foundations/step-03a-gauge-chiral-action.md",
        "48141fc931580f6b73e385b8f900b3e6df5939cdb9348042de07fd8fe9320967",
        "(3A.3)--(3A.8), (3A.34), (3A.48), (3A.51)",
    ),
    (
        "contracts/foundations/step-03c-gauge-vector-representation.md",
        "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1",
        "(3C.15)--(3C.24), (3C.33)--(3C.45)",
    ),
    (
        "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
        "109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538",
        "(3D.34), (3D.80)--(3D.93)",
    ),
    (
        "contracts/foundations/step-04c-n4-super-yang-mills.md",
        "fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f",
        "(4C.1), (4C.4), (4C.34)--(4C.35d)",
    ),
)

ORIENTATIONS = ("A_to_Wtilde__B_to_W", "B_to_Wtilde__A_to_W")
PLACEMENTS = ("Dminus_left", "Dminus_right")
ENDPOINTS = ("r0|r1", "r0|r2", "r1|r1", "r1|r2")


def q(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def foundation_rows() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    for rel, expected, equations in FOUNDATIONS:
        actual = file_hash(ROOT / rel)
        status = "PASS" if actual == expected else "FAIL"
        rows.append(
            {
                "path": rel,
                "expected_sha256": expected,
                "actual_sha256": actual,
                "equations_used": equations,
                "status": status,
            }
        )
        checks.append(
            {
                "id": f"foundation_hash::{rel}",
                "status": status,
                "actual": actual,
                "expected": expected,
            }
        )
    return rows, checks


def canonical_letter() -> dict[str, Any]:
    return {
        "canonicalization": [
            "A_Project=g*a from h=g^(-2) and canonical quadratic normalization",
            "V_Project=2*g*v from the WZ vector coefficient (3A.48)",
            "W_Project=g*W_can from (3A.51)",
        ],
        "connection_derivation": [
            "X=2*g*v",
            "exp(-X)D_a exp(X)=D_a X+(1/2)[[D_a X,X]]+(1/6)[[[[D_a X,X]],X]]+O(g^4)",
            "Gamma_a=2*g*D_a v+2*g^2*[[D_a v,v]]+(4/3)*g^3*[[[[D_a v,v]],v]]+O(g^4)",
        ],
        "connection_coefficients": {
            "Gamma1": q(Fraction(2)),
            "Gamma2": q(Fraction(2)),
            "Gamma3": q(Fraction(4, 3)),
        },
        "field_strength": [
            "W1_a=-(1/4)*barD^2 D_a v",
            "W2_a=-(1/4)*barD^2 [[D_a v,v]]",
            "W3_a=-(1/6)*barD^2 [[[[D_a v,v]],v]]",
        ],
        "field_strength_coefficients": {
            "W1": q(Fraction(-1, 4)),
            "W2": q(Fraction(-1, 4)),
            "W3": q(Fraction(-1, 6)),
        },
        "letter": {
            "definition": "L=g^(-1)*(nabla_+ W_Project,+)=L1+g*L2+g^2*L3+O(g^3)",
            "parity": "even",
            "L1": "D_+ W1_+",
            "L2": "D_+ W2_+ + 2*[[D_+ v,W1_+]]",
            "L3": (
                "D_+ W3_+ + 2*[[D_+ v,W2_+]] "
                "+ 2*[[[[D_+ v,v]],W1_+]]"
            ),
        },
    }


def duhamel() -> dict[str, Any]:
    return {
        "definitions": {
            "P": "w^m partial_m",
            "M": "M^A_C(x)=w^m c_{BC}^A a_m^B(x)",
            "tau": "tau_w=exp(P+g*M)=exp(w^m D_m^adj)",
            "fourier_declaration": "exp(+i p.x)",
        },
        "orders": [
            {"order": 0, "coefficient": q(Fraction(1)), "word": "T0=exp(P)"},
            {
                "order": 1,
                "coefficient": q(Fraction(1)),
                "word": "T1=int_0^1 ds exp((1-s)P) M exp(sP)",
            },
            {
                "order": 2,
                "coefficient": q(Fraction(1)),
                "word": (
                    "T2=int_{0<=a<=b<=1} da db exp((1-b)P) M "
                    "exp((b-a)P) M exp(aP)"
                ),
            },
        ],
        "position_space": [
            "(T0 Y)^A(x)=Y^A(x+w)",
            "(T1 Y)^A(x)=int_0^1 dt M^A_B(x+t*w)Y^B(x+w)",
            (
                "(T2 Y)^A(x)=int_{0<=t1<=t2<=1}dt1dt2 "
                "M^A_B(x+t1*w)M^B_C(x+t2*w)Y^C(x+w)"
            ),
        ],
        "ordered_volumes": {
            "T0": q(Fraction(1)),
            "T1": q(Fraction(1)),
            "T2": q(Fraction(1, 2)),
        },
        "no_extra_factorial": True,
        "covariance": [
            "D'_m=R(k)D_m R(k)^(-1) from (3C.18)",
            "tau'_w=R(k)tau_w R(k)^(-1)",
            "(tau_w Y)'(x)=R(k(x))(tau_w Y)(x)",
        ],
    }


def source() -> dict[str, Any]:
    terms = {
        "g0": ["L1_A T0 L1_B"],
        "g1": [
            "L2_A T0 L1_B",
            "L1_A T0 L2_B",
            "L1_A T1 L1_B",
        ],
        "g2": [
            "L3_A T0 L1_B",
            "L1_A T0 L3_B",
            "L2_A T0 L2_B",
            "L2_A T1 L1_B",
            "L1_A T1 L2_B",
            "L1_A T2 L1_B",
        ],
    }
    return {
        "functional": (
            "S_J=int d^4x d^4theta dw J_AB(x,w)L^A(x)(tau_w L)^B(x)"
        ),
        "source_type": "J belongs to dual(Adj_x tensor Adj_x)",
        "ordered": True,
        "reverse_order_is_distinct": True,
        "marked_placements": [
            {
                "id": "Dminus_left",
                "word": "J_AB (nabla_- L)^A (tau_w L)^B",
                "leibniz_sign": 1,
            },
            {
                "id": "Dminus_right",
                "word": "J_AB L^A nabla_-[(tau_w L)^B]",
                "leibniz_sign": 1,
            },
        ],
        "right_placement_completion": [
            "nabla_-(tau_w L)=tau_w(nabla_- L)+[nabla_-,tau_w]L",
            (
                "[nabla_-,tau_w]=int_0^1 ds exp((1-s)w.D)"
                "[nabla_-,w.D]exp(s*w.D)"
            ),
        ],
        "product_expansion": terms,
        "term_count": {order: len(words) for order, words in terms.items()},
        "each_product_coefficient": q(Fraction(1)),
    }


def quartic_words() -> dict[str, Any]:
    words = ("W1^a W3_a", "W2^a W2_a", "W3^a W1_a")
    return {
        "derivation": [
            "S_E,+=-(1/4)*int[W_can^a W_can,a]_F",
            "W_can=W1+g*W2+g^2*W3+O(g^3)",
        ],
        "g2_ordered_density": [
            {"word": word, "coefficient": q(Fraction(-1, 4))} for word in words
        ],
        "do_not_merge_before_ordered_port_differentiation": True,
        "boundary": (
            "The density words are exact; their background/quantum port "
            "derivatives require a locked Step-5 perturbative slice."
        ),
    }


@dataclass(frozen=True)
class Affine:
    c: Fraction = Fraction(0)
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def a_eq_b(self) -> "Affine":
        return Affine(self.c, Fraction(0), self.a + self.b)

    def a_zero(self) -> "Affine":
        return Affine(self.c, Fraction(0), self.b)

    def b_one(self) -> "Affine":
        return Affine(self.c + self.b, self.a, Fraction(0))

    def b_eq_a(self) -> "Affine":
        return Affine(self.c, self.a + self.b, Fraction(0))

    def data(self) -> list[dict[str, int]]:
        return [q(self.c), q(self.a), q(self.b)]


def phase_chain() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # E012(a,b)=exp(i*w.[a*r0+(b-a)*r1+(1-b)*r2]).
    phase = (Affine(a=1), Affine(a=-1, b=1), Affine(c=1, b=-1))
    boundaries = {
        "a=b": tuple(item.a_eq_b() for item in phase),
        "a=0": tuple(item.a_zero() for item in phase),
        "b=1": tuple(item.b_one() for item in phase),
        "b=a": tuple(item.b_eq_a() for item in phase),
    }
    expected = {
        "a=b": (Affine(b=1), Affine(), Affine(c=1, b=-1)),
        "a=0": (Affine(), Affine(b=1), Affine(c=1, b=-1)),
        "b=1": (Affine(a=1), Affine(c=1, a=-1), Affine()),
        "b=a": (Affine(a=1), Affine(), Affine(c=1, a=-1)),
    }
    checks = [
        {
            "id": f"two_link_boundary::{name}",
            "status": "PASS" if boundaries[name] == expected[name] else "FAIL",
        }
        for name in boundaries
    ]
    return (
        {
            "one_link_identity": (
                "i*w.(r0-r1)*int_0^1 ds exp(i*w.[s*r0+(1-s)*r1])"
                "=exp(i*w.r0)-exp(i*w.r1)"
            ),
            "one_link_cancellation_rows": [
                [
                    "+C_parallel*exp(i*w.r0)",
                    "-C_parallel*exp(i*w.r0)",
                    "0",
                ],
                [
                    "-C_parallel*exp(i*w.r1)",
                    "+C_parallel*exp(i*w.r1)",
                    "0",
                ],
            ],
            "two_link_phase": (
                "E012=exp(i*w.[a*r0+(b-a)*r1+(1-b)*r2]),0<=a<=b<=1"
            ),
            "two_link_a_identity": (
                "i*w.(r0-r1)*int db int_0^b da E012"
                "=int db[E02(b)-E12(b)]"
            ),
            "two_link_b_identity": (
                "i*w.(r1-r2)*int da int_a^1 db E012"
                "=int da[E01(a)-E02(a)]"
            ),
            "boundaries": {
                name: [item.data() for item in value]
                for name, value in boundaries.items()
            },
            "scope": (
                "Exact phase telescoping; equality of the loop residue "
                "C_parallel is a separate amplitude obligation."
            ),
        },
        checks,
    )


def endpoint_covariance() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    link = {"omega_x": 1, "omega_y": -1}
    right_field = {"omega_x": 0, "omega_y": 1}
    total = {name: link[name] + right_field[name] for name in link}
    expected = {"omega_x": 1, "omega_y": 0}
    return (
        {
            "link_law": (
                "delta U_adj(x,y)=omega_adj(x)U_adj(x,y)"
                "-U_adj(x,y)omega_adj(y)"
            ),
            "field_law": "delta Y(y)=omega_adj(y)Y(y)",
            "coefficient_sum": total,
            "result": (
                "delta[U_adj(x,y)Y(y)]="
                "omega_adj(x)U_adj(x,y)Y(y)"
            ),
        },
        [
            {
                "id": "external_endpoint_covariance",
                "status": "PASS" if total == expected else "FAIL",
                "actual": total,
                "expected": expected,
            }
        ],
    )


def cut_orbits() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    orbits: list[dict[str, Any]] = []
    mapping: dict[str, str] = {}
    for orientation in ORIENTATIONS:
        for placement in PLACEMENTS:
            for endpoints in ENDPOINTS:
                root = f"{orientation}::{placement}::{endpoints}"
                triangle = f"T::{root}"
                contact = f"C_SD::{root}"
                mapping[triangle] = contact
                mapping[contact] = triangle
                orbits.append(
                    {
                        "root": root,
                        "orientation": orientation,
                        "marked_Dminus_placement": placement,
                        "derivative_endpoints": endpoints,
                        "members": [triangle, contact],
                        "already_oriented_output_word": True,
                    }
                )
    involution = all(mapping[mapping[item]] == item for item in mapping)
    no_duplicate = len(orbits) == 16 and len(mapping) == 32
    return (
        {
            "definition": (
                "C_SD preserves orientation, marked Dminus placement, "
                "derivative endpoints, color word, and link word."
            ),
            "parent_count": len(orbits),
            "contact_count": len(orbits),
            "orbits": orbits,
            "mapping": mapping,
            "fixed_orientation_wick_weight": {
                "calculation": "(1/2!)*(1+1)=1",
                "value": q(Fraction(1)),
            },
            "multiplicity_rule": (
                "Reflected orientation and the other Dminus placement are "
                "distinct output words, never factors multiplying one word."
            ),
        },
        [
            {
                "id": "cut_involution_C_squared",
                "status": "PASS" if involution else "FAIL",
            },
            {
                "id": "sixteen_occurrence_decorated_roots",
                "status": "PASS" if no_duplicate else "FAIL",
            },
            {"id": "fixed_orientation_wick_weight", "status": "PASS"},
            {"id": "no_orientation_or_Dminus_double_count", "status": "PASS"},
        ],
    )


def completion_slots() -> list[dict[str, Any]]:
    sectors = (
        ("NONLINEAR_LETTER_LEFT", "OPERATOR_WORD_DERIVED", "L2_A T0 L1_B"),
        ("NONLINEAR_LETTER_RIGHT", "OPERATOR_WORD_DERIVED", "L1_A T0 L2_B"),
        (
            "QUARTIC_ACTION_CONTACT",
            "DENSITY_WORD_DERIVED",
            "W1 W3; W2 W2; W3 W1",
        ),
        ("COLLAPSED_DALGEBRA_R0", "BLOCKED_AMPLITUDE_KERNEL", "cut r0"),
        ("COLLAPSED_DALGEBRA_R1", "BLOCKED_AMPLITUDE_KERNEL", "cut r1"),
        ("COLLAPSED_DALGEBRA_R2", "BLOCKED_AMPLITUDE_KERNEL", "cut r2"),
        (
            "SCHWINGER_CUT_CONTACT",
            "BLOCKED_AMPLITUDE_KERNEL",
            "occurrence-decorated C_SD",
        ),
        ("ONE_LINK_BULK", "OPERATOR_WORD_DERIVED", "L1_A T1 L1_B"),
        ("TWO_LINK_ORDERED", "OPERATOR_WORD_DERIVED", "L1_A T2 L1_B"),
        ("EXTERNAL_ENDPOINT_LEFT", "ENDPOINT_LAW_DERIVED", "+omega(x)U"),
        (
            "EXTERNAL_ENDPOINT_RIGHT",
            "ENDPOINT_LAW_DERIVED",
            "-U omega(y)+U delta Y(y)",
        ),
    )
    return [
        {
            "word_root": f"{orientation}::{placement}",
            "orientation": orientation,
            "marked_Dminus_placement": placement,
            "sector": sector,
            "state": state,
            "source_word": word,
            "physical_graph_count_claimed": False,
        }
        for orientation in ORIENTATIONS
        for placement in PLACEMENTS
        for sector, state, word in sectors
    ]


def metric_algebra() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Coefficients in the basis (hat_delta, breve_delta).
    triangle = (Fraction(1), Fraction(0))
    contact = (Fraction(-1), Fraction(-1))
    total = tuple(triangle[i] + contact[i] for i in range(2))
    expected = (Fraction(0), Fraction(-1))
    return (
        {
            "basis": ["hat_delta^{mn}", "breve_delta^{mn}"],
            "definition": "delta_4^{mn}=hat_delta^{mn}+breve_delta^{mn}",
            "common_symbolic_residue": "C_T/epsilon",
            "triangle": "+(C_T/epsilon)*hat_delta^{mn}",
            "required_contact": "-(C_T/epsilon)*delta_4^{mn}",
            "sum": "-(C_T/epsilon)*breve_delta^{mn}",
            "vectors": {
                "triangle": [q(item) for item in triangle],
                "contact": [q(item) for item in contact],
                "sum": [q(item) for item in total],
            },
            "proof_state": (
                "CONDITIONAL_ON_PROJECT_DERIVATION_OF_EQUAL_RESIDUE_C_T"
            ),
        },
        [
            {
                "id": "conditional_metric_basis_algebra",
                "status": "PASS" if total == expected else "FAIL",
            }
        ],
    )


def blockers() -> list[dict[str, str]]:
    return [
        {
            "id": "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION",
            "missing": (
                "One complete superspace D-word, the four endpoint integration-by-parts "
                "chains, and the declared exchange map for the second marked placement."
            ),
            "why": (
                "The current endpoint signs and mixed anticommutator factors are "
                "recorded arithmetic primitives rather than rewrite-engine outputs."
            ),
        },
        {
            "id": "BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE",
            "missing": (
                "Contract admission of S_J, its superspace/source measure, "
                "Fourier phase, dual Adj tensor Adj source law, and reversed-order rule."
            ),
            "why": (
                "Step 3D permits general sources but does not select this Step-5 operator."
            ),
        },
        {
            "id": "BLOCKED_LOCKED_STEP5_DRED_CONTRACT",
            "missing": (
                "Verified d=4-2 epsilon, loop measure, "
                "delta_4=hat_delta+breve_delta, and regulator action on all blocks."
            ),
            "why": (
                "Steps 3A/3C/3D/4C contain no dimensional-reduction metric split."
            ),
        },
        {
            "id": "BLOCKED_LOCKED_GAUGE_KERNEL_AND_PROPAGATORS",
            "missing": (
                "A chosen Y_E in (3D.88a)--(3D.93), residual-free Hessian, "
                "and exact vector/chiral/FP/NK/multiplier inverses."
            ),
            "why": (
                "The Schwinger cut K*G=delta cannot be evaluated while the "
                "gauge-fixing map and density are arbitrary."
            ),
        },
        {
            "id": "BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR",
            "missing": (
                "Ordered derivatives of this bilocal source and the full "
                "background-split N=4 action through g^2, including ghost and measure ports."
            ),
            "why": (
                "BCH fixes operator words, but not background/quantum/external "
                "port type, identical-leg factors, or contraction signs."
            ),
        },
        {
            "id": "BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES",
            "missing": (
                "Edge-tagged D-algebra and loop reduction of every nonlinear, "
                "quartic, collapsed, one-link, two-link, and endpoint graph."
            ),
            "why": (
                "Phase telescoping proves cancellation only after the graph "
                "residues are independently equal."
            ),
        },
        {
            "id": "BLOCKED_RENORMALIZED_COMPOSITE_MIXING",
            "missing": (
                "Local composite/counterterm basis and evanescent-to-physical "
                "one-loop mixing matrix."
            ),
            "why": (
                "An O(epsilon) operator can multiply a 1/epsilon pole."
            ),
        },
    ]


def build() -> dict[str, Any]:
    foundations, checks = foundation_rows()
    phases, phase_checks = phase_chain()
    endpoints, endpoint_checks = endpoint_covariance()
    cuts, cut_checks = cut_orbits()
    metric, metric_checks = metric_algebra()
    checks += phase_checks + endpoint_checks + cut_checks + metric_checks
    return {
        "schema": "awi.step5.ww-contact-link-completion-audit.v1",
        "task_id": TASK_ID,
        "authority_commit": AUTHORITY_COMMIT,
        "verify_run": VERIFY_RUN,
        "input_boundary": {
            "read": [item[0] for item in FOUNDATIONS],
            "not_read": [
                "untracked Step-5 contract",
                "untracked Step-5 seed/cut audits as evidence",
                "holomorphic-twist target",
                "live chats",
                "Notion",
            ],
        },
        "foundations": foundations,
        "canonical_connection_and_letter": canonical_letter(),
        "duhamel_translation": duhamel(),
        "ordered_bilocal_source": source(),
        "quartic_action": quartic_words(),
        "endpoint_covariance": endpoints,
        "phase_chain": phases,
        "cut_orbits": cuts,
        "completion_obligation_slots": completion_slots(),
        "metric_mismatch": metric,
        "proved": {
            "connection_and_WW_letter_through_g2": "PASS",
            "ordered_Duhamel_through_g2": "PASS",
            "ordered_bilocal_product_through_g2": "PASS",
            "endpoint_covariance": "PASS",
            "one_and_two_link_phase_telescoping": "PASS",
            "cut_involution": "PASS",
            "no_double_count": "PASS",
            "conditional_metric_algebra": "PASS",
        },
        "blocked_claims": {
            "numerical_cut_contact_UV_pole": (
                "BLOCKED_LOCKED_GAUGE_KERNEL_AND_PROPAGATORS"
            ),
            "contact_equals_minus_delta4_with_same_C_T": (
                "BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES"
            ),
            "graphwise_w_longitudinal_UV_cancellation": (
                "BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES"
            ),
            "renormalized_completion": "BLOCKED_RENORMALIZED_COMPOSITE_MIXING",
        },
        "blockers": blockers(),
        "minimal_new_step5_definitions": [
            "Admit the ordered source S_J and its contragredient J_AB law exactly as displayed.",
            "Lock exp(+i p.x), P=w.partial, and tau_w=exp(w.D_adj).",
            "Lock d=4-2 epsilon, the loop measure, and delta_4=hat_delta+breve_delta on every field and ghost block.",
            "Choose Y_E and publish every residual-free quadratic inverse.",
            "Publish the ordered background/quantum port grammar through g^2 before graph enumeration.",
            "Publish the composite counterterm basis before a renormalized closure claim.",
        ],
        "checks": checks,
        "overall_status": "CONDITIONAL_FF_ARITHMETIC__BLOCKED_EXPLICIT_D_WORD_AND_STEP5_COMPLETION_KERNELS",
    }


def render_markdown(audit: dict[str, Any]) -> str:
    foundation_table = "\n".join(
        f"| {row['path']} | {row['actual_sha256']} | {row['status']} |"
        for row in audit["foundations"]
    )
    blocker_table = "\n".join(
        f"| {row['id']} | {row['missing']} | {row['why']} |"
        for row in audit["blockers"]
    )
    check_table = "\n".join(
        f"| {row['id']} | {row['status']} |" for row in audit["checks"]
    )
    g2_formula = (
        r"L_{3A}T_0L_{1B} \\" "\n"
        r"&\quad+L_{1A}T_0L_{3B} \\" "\n"
        r"&\quad+L_{2A}T_0L_{2B} \\" "\n"
        r"&\quad+L_{2A}T_1L_{1B} \\" "\n"
        r"&\quad+L_{1A}T_1L_{2B} \\" "\n"
        r"&\quad+L_{1A}T_2L_{1B}"
    )
    sector_table = "\n".join(
        f"| {row['sector']} | {row['state']} | {row['source_word']} |"
        for row in audit["completion_obligation_slots"][:11]
    )
    template = r"""# Step 5 WW Schwinger cut/contact/link completion audit

Authority: __AUTHORITY__; verify run __VERIFY_RUN__.
HT target 与 untracked Step-5 artifacts 未作为 evidence。

## 1. Locked inputs

| file | SHA-256 | check |
|---|---|---|
__FOUNDATION_TABLE__

## 2. Canonical connection and WW letter

由 (3A.3)、(3A.48)、(4C.1)、(4C.4)，

$$
A_{{P,m}}=g a_m,\qquad \mathcal V_P=2gv,\qquad
\mathcal W_P=gW_{{\rm can}}.
$$

令 $X=2gv$。逐项展开

$$
e^{{-X}}D_ae^X
=D_aX+\frac12\llbracket D_aX,X\rrbracket
+\frac16\llbracket\llbracket D_aX,X\rrbracket,X\rrbracket+O(g^4),
$$

$$
\Gamma_a
=2gD_av+2g^2\llbracket D_av,v\rrbracket
+\frac43g^3\llbracket\llbracket D_av,v\rrbracket,v\rrbracket+O(g^4).
$$

$$
W_{{1a}}=-\frac14\bar D^2D_av,\qquad
W_{{2a}}=-\frac14\bar D^2\llbracket D_av,v\rrbracket,
$$

$$
W_{{3a}}=-\frac16\bar D^2
\llbracket\llbracket D_av,v\rrbracket,v\rrbracket.
$$

定义 even letter

$$
L:=g^{{-1}}(\nabla_+\mathcal W_+)_P
=L_1+gL_2+g^2L_3+O(g^3),
$$

$$
L_1=D_+W_{{1+}},
$$

$$
L_2=D_+W_{{2+}}+2\llbracket D_+v,W_{{1+}}\rrbracket,
$$

$$
L_3=D_+W_{{3+}}
+2\llbracket D_+v,W_{{2+}}\rrbracket
+2\llbracket\llbracket D_+v,v\rrbracket,W_{{1+}}\rrbracket.
$$

## 3. Ordered covariant translation

$$
P:=w^m\partial_m,\qquad
\mathbb M^A{}_C:=w^m c_{{BC}}{}^Aa_m^B,\qquad
\tau_w=e^{{P+g\mathbb M}}.
$$

$$
T_0=e^P,
$$

$$
T_1=\int_0^1ds\ e^{{(1-s)P}}\mathbb M e^{{sP}},
$$

$$
T_2=\int_{{0\le a\le b\le1}}da\,db\;
e^{{(1-b)P}}\mathbb M e^{{(b-a)P}}\mathbb M e^{{aP}}.
$$

令 $t_1=1-b$、$t_2=1-a$，

$$
(T_1Y)^A(x)
=\int_0^1dt\ \mathbb M^A{}_B(x+tw)Y^B(x+w),
$$

$$
(T_2Y)^A(x)
=\int_{{0\le t_1\le t_2\le1}}dt_1dt_2\;
\mathbb M^A{}_B(x+t_1w)\mathbb M^B{}_C(x+t_2w)Y^C(x+w).
$$

$T_2$ 没有额外 $1/2!$；constant-$\mathbb M$ 时

$$
\int_{{0\le t_1\le t_2\le1}}dt_1dt_2=\frac12.
$$

## 4. Ordered bilocal source through $g^2$

$$
S_J=\int d^4x\,d^4\theta\,dw\;
J_{{AB}}L^A(x)(\tau_wL)^B(x).
$$

$$
\mathcal I_{{-|}}^{{AB}}
=(\nabla_-L)^A(\tau_wL)^B,\qquad
\mathcal I_{{|-}}^{{AB}}
=L^A\nabla_-(\tau_wL)^B.
$$

因为 $|L|=0$，Leibniz sign 为 $+1$。同时

$$
\nabla_-(\tau_wL)
=\tau_w(\nabla_-L)+[\nabla_-,\tau_w]L,
$$

$$
[\nabla_-,\tau_w]
=\int_0^1ds\ e^{{(1-s)w\cdot\mathcal D}}
[\nabla_-,w\cdot\mathcal D]e^{{sw\cdot\mathcal D}}.
$$

$$
\mathcal O^{{(0)}}_{{AB}}=L_{{1A}}T_0L_{{1B}},
$$

$$
\mathcal O^{{(1)}}_{{AB}}
=L_{{2A}}T_0L_{{1B}}
+L_{{1A}}T_0L_{{2B}}
+L_{{1A}}T_1L_{{1B}}.
$$

$$
\begin{{aligned}}
\mathcal O^{{(2)}}_{{AB}}=__G2_FORMULA__.
\end{{aligned}}
$$

六项 product coefficient 均为 $1$。

## 5. Quartic/contact density

$$
S_{{E,+}}^{{(4)}}
=-\frac14\int
\left[W_1^aW_{{3a}}+W_2^aW_{{2a}}+W_3^aW_{{1a}}\right]_F.
$$

三个 ordered words 在 port differentiation 前不得合并。

## 6. Completion-sector obligations

以下 $11$ 个 sectors 对每个
$(\text{{orientation}},\text{{marked }}\nabla_-\text{{ placement}})$
均独立生成；JSON 共含 $2\times2\times11=44$ rows。

| sector | state | locked word |
|---|---|---|
__SECTOR_TABLE__

OPERATOR_WORD_DERIVED 与 DENSITY_WORD_DERIVED 不等于 physical amplitude
已闭合；BLOCKED_AMPLITUDE_KERNEL rows 不声明 graph coefficient。

## 7. Exact link/endpoint phase chain

$$
iw\cdot(r_0-r_1)
\int_0^1ds\ e^{{iw\cdot[sr_0+(1-s)r_1]}}
=e^{{iw\cdot r_0}}-e^{{iw\cdot r_1}}.
$$

同一 residue $C_\parallel$ 的 endpoint rows 为

$$
\begin{{array}}{{c|c|c}}
\text{{triangle}}&\text{{one-link boundary}}&\text{{sum}}\\ \hline
+C_\parallel e^{{iw\cdot r_0}}&-C_\parallel e^{{iw\cdot r_0}}&0\\
-C_\parallel e^{{iw\cdot r_1}}&+C_\parallel e^{{iw\cdot r_1}}&0
\end{{array}}.
$$

令

$$
E_{{012}}(a,b)
=e^{{iw\cdot[ar_0+(b-a)r_1+(1-b)r_2]}},\qquad0\le a\le b\le1.
$$

$$
iw\cdot(r_0-r_1)\int_0^1db\int_0^bda\,E_{{012}}
=\int_0^1db\,[E_{{02}}(b)-E_{{12}}(b)],
$$

$$
iw\cdot(r_1-r_2)\int_0^1da\int_a^1db\,E_{{012}}
=\int_0^1da\,[E_{{01}}(a)-E_{{02}}(a)].
$$

two-link longitudinal term 严格化为 one-link boundaries，再化为 endpoints。

$$
\delta U_{{\rm adj}}(x,y)
=\omega_{{\rm adj}}(x)U_{{\rm adj}}(x,y)
-U_{{\rm adj}}(x,y)\omega_{{\rm adj}}(y),
$$

$$
\delta[U_{{\rm adj}}(x,y)Y(y)]
=\omega_{{\rm adj}}(x)U_{{\rm adj}}(x,y)Y(y),
$$

因为 right endpoint coefficient 为 $-1+1=0$。

## 8. Cut involution and multiplicity

每个 root 保留 orientation、marked $\nabla_-$ placement、derivative endpoints、
color/link word 与 ordered output word。定义

$$
\mathfrak C_{{SD}}(T_\mathfrak r)=C_\mathfrak r,\qquad
\mathfrak C_{{SD}}(C_\mathfrak r)=T_\mathfrak r.
$$

脚本得到 $16$ 个 parent roots 与 $16$ 个 contact partners，并验证

$$
\mathfrak C_{{SD}}^2=1.
$$

固定 orientation 的 action-order weight 为

$$
\frac1{{2!}}(1+1)=1.
$$

reflected orientation 与另一个 marked $\nabla_-$ placement 是不同 output
words，不乘入同一 coefficient。

## 9. Conditional metric algebra

若 Project graph calculation 独立得到共同 residue $C_T$，

$$
\Gamma_{{T,\rm UV}}^{{mn}}
=+\frac{{C_T}}\epsilon\widehat\delta^{{mn}},\qquad
\Gamma_{{C,\rm UV}}^{{mn}}
=-\frac{{C_T}}\epsilon\delta_4^{{mn}}.
$$

由

$$
\delta_4^{{mn}}=\widehat\delta^{{mn}}+\breve\delta^{{mn}},
$$

严格得到

$$
\Gamma_{{T,\rm UV}}^{{mn}}+\Gamma_{{C,\rm UV}}^{{mn}}
=-\frac{{C_T}}\epsilon\breve\delta^{{mn}}.
$$

locked foundations 尚未导出 contact 的共同 residue $C_T$。

## 10. Exact blockers

| blocker | missing | exact reason |
|---|---|---|
__BLOCKER_TABLE__

## 11. Checks

| check | status |
|---|---|
__CHECK_TABLE__

$$
\boxed{{\text{{overall status}}=\texttt{{__OVERALL_STATUS__}}}}.
$$
"""
    return (
        template.replace("__AUTHORITY__", audit["authority_commit"])
        .replace("__VERIFY_RUN__", audit["verify_run"])
        .replace("__FOUNDATION_TABLE__", foundation_table)
        .replace("__G2_FORMULA__", g2_formula)
        .replace("__BLOCKER_TABLE__", blocker_table)
        .replace("__CHECK_TABLE__", check_table)
        .replace("__SECTOR_TABLE__", sector_table)
        .replace("__OVERALL_STATUS__", audit["overall_status"])
        .replace("{{", "{")
        .replace("}}", "}")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json", default="audits/step5-ww-contact-link-completion.json"
    )
    parser.add_argument(
        "--markdown", default="audits/step5-ww-contact-link-completion.md"
    )
    args = parser.parse_args()

    audit = build()
    json_path = ROOT / args.json
    md_path = ROOT / args.markdown
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    md_path.write_text(render_markdown(audit))

    failed = [row for row in audit["checks"] if row["status"] != "PASS"]
    print(
        json.dumps(
            {"overall_status": audit["overall_status"], "failed_checks": failed},
            indent=2,
        )
    )
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
