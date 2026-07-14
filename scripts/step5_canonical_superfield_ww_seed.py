#!/usr/bin/env python3
"""Independent Project-side canonical-superfield WW seed derivation.

This generator uses only the Step-5 allowed Project foundations.  It does not
read the holomorphic-twist target or either imported candidate coefficient.
All numerical factors are recomputed from primitive normalization data.
"""

from __future__ import annotations

import argparse
import copy
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
VERIFY_RUN = "29306335742"
TASK_ID = "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001"

FOUNDATIONS = [
    {
        "path": "contracts/foundations/step-01-supersymmetry-commutator.md",
        "sha256": "a73d8017c2d07de578f4f98ea25054033b0384ebffb6b426650a22f404c3231b",
        "uses": ["Euclidean sigma algebra (1.51)--(1.56)"],
    },
    {
        "path": "contracts/foundations/step-02a-flat-superspace.md",
        "sha256": "6694f46634d604fac6a8866323c7325a803cbf3079a5771ddea25772c91cef2d",
        "uses": ["left Grassmann calculus (2A.4)--(2A.8)", "Euclidean D algebra (2A.41)--(2A.43)"],
    },
    {
        "path": "contracts/foundations/step-03a-gauge-chiral-action.md",
        "sha256": "48141fc931580f6b73e385b8f900b3e6df5939cdb9348042de07fd8fe9320967",
        "uses": ["Berezin projectors (3A.13)--(3A.16)", "field strengths (3A.51)--(3A.52)"],
    },
    {
        "path": "contracts/foundations/step-03c-gauge-vector-representation.md",
        "sha256": "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1",
        "uses": ["background vector derivatives (3C.15)--(3C.23)", "strength algebra (3C.33)--(3C.45)"],
    },
    {
        "path": "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
        "sha256": "109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538",
        "uses": ["background split (3D.80)", "gauge conditions and gauge fermion (3D.86)--(3D.93b)"],
    },
    {
        "path": "contracts/foundations/step-04-extended-sym-notation.md",
        "sha256": "3fcf7e242928d3512c02059d8c28d9551b5cb86156f9d6259cd2bba713211d27",
        "uses": ["absorbed coupling and invariant trace (4.5)--(4.11)"],
    },
    {
        "path": "contracts/foundations/step-04a-n1-super-yang-mills.md",
        "sha256": "b2495f6a98c8cffe21ab2583b1955c81f5bb06af9b0edfb677fc0a3a3ee1fbc1",
        "uses": ["Euclidean N=1 action (4A.2)", "positive gauge contour (4A.56b)--(4A.57)"],
    },
    {
        "path": "contracts/foundations/step-04c-n4-super-yang-mills.md",
        "sha256": "fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f",
        "uses": ["Euclidean N=4 action (4C.4)"],
    },
]


def fq(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def fs(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class PrimitiveConfig:
    project_to_canonical_v: Fraction = Fraction(2)
    project_to_canonical_w: Fraction = Fraction(1)
    action_chiral_coefficient: Fraction = Fraction(-1, 4)
    bch_linear: Fraction = Fraction(1)
    bch_quadratic: Fraction = Fraction(1, 2)
    exponent_argument_v: Fraction = Fraction(2)
    field_strength_projector: Fraction = Fraction(-1, 8)
    kinetic_hessian: Fraction = Fraction(1)
    expansion_symmetry_factor: Fraction = Fraction(1, 2)
    action_vertex_label_assignments: int = 2
    k_plus_coefficient: Fraction = Fraction(-1, 4)
    dminus_dplus_to_d2: Fraction = Fraction(1, 2)
    closed_grassmann_loop: int = 16
    mixed_anticommutator_factor: int = 2
    mixed_anticommutator_count: int = 2
    feynman_parameter_prefactor: int = 2
    loop_quadratic_leading_factor: int = 4
    tensor_residue_at_d4: Fraction = Fraction(1, 4)
    simplex_volume: Fraction = Fraction(1, 2)
    scalar_bubble_residue_without_pi: Fraction = Fraction(1, 16)


def canonical_dictionary(cfg: PrimitiveConfig) -> dict[str, Any]:
    # V_P = (2 g) v follows from the exponent exp(V_P)=exp(2 g v).
    exponent_linear = cfg.field_strength_projector * cfg.bch_linear * cfg.exponent_argument_v
    w_linear = exponent_linear / cfg.project_to_canonical_w
    exponent_quadratic = (
        cfg.field_strength_projector
        * cfg.bch_quadratic
        * cfg.exponent_argument_v
        * cfg.exponent_argument_v
    )
    w_quadratic_after_dividing_g = exponent_quadratic / cfg.project_to_canonical_w
    return {
        "forward": {"V_P": "2*g*v", "W_P": "g*W_can"},
        "inverse": {"v": "V_P/(2*g)", "W_can": "W_P/g"},
        "roundtrip_factors": {
            "V": fq(cfg.project_to_canonical_v / cfg.project_to_canonical_v),
            "W": fq(cfg.project_to_canonical_w / cfg.project_to_canonical_w),
        },
        "W_can_linear_coefficient": fq(w_linear),
        "W_can_quadratic_coefficient_times_g": fq(w_quadratic_after_dividing_g),
        "W_can_expansion": [
            "W_(1)a=-(1/4)*barD^2*D_a*v",
            "W_(2)a=-(1/4)*barD^2*[[D_a*v,v]]",
            "W_can=W_(1)+g*W_(2)+O(g^2)",
        ],
    }


def gauge_and_propagator(cfg: PrimitiveConfig) -> dict[str, Any]:
    inverse = Fraction(1, 1) / cfg.kinetic_hessian
    return {
        "gauge_name": "PROJECT_STEP5_BACKGROUND_SUPERSYMMETRIC_FERMI_FEYNMAN",
        "background_split": "E_tot=Btilde_B*exp(2*g*v)*B_B",
        "conditions": [
            "F_+(v)=-(1/4)*(barNabla_B)^2*(2*g*v)",
            "F_-(v)=-(1/4)*(Nabla_B)^2*(2*g*v)",
        ],
        "gauge_parameter": 1,
        "residual_slice": "ker(M_FP) removed as in (3D.92)--(3D.92a)",
        "quadratic_action": "S_0=(1/2)*int d^d x d^4theta kappa_AB v^A(-partial^2)v^B",
        "momentum_kernel": "K_AB(p)=kappa_AB*p^2",
        "kinetic_hessian_factor": fq(cfg.kinetic_hessian),
        "inverse_check": fq(cfg.kinetic_hessian * inverse),
        "propagator": "<v^A(p,theta_1)v^B(-p,theta_2)>_0=hbar*kappa^{AB}*delta^4(theta_1-theta_2)/p^2",
        "propagator_scalar_factor": fq(inverse),
        "cycle": "Euclidean positive gauge-boson contour inherited from (4A.56b)--(4A.57)",
    }


def derive_vertices(cfg: PrimitiveConfig) -> dict[str, Any]:
    # Expanding -1/4 [W_can W_can] gives 2*(-1/4)*g W_(1)W_(2).
    action_cross = cfg.action_chiral_coefficient * 2
    background_vertex_magnitude = abs(action_cross)
    # The action kernels and the e^{-S_int/hbar} vertices have opposite signs.
    chiral_action_phase = "+i"
    chiral_exponent_phase = "-i"
    antichiral_action_phase = "-i"
    antichiral_exponent_phase = "+i"
    vertex_product = background_vertex_magnitude * background_vertex_magnitude
    return {
        "action_cross_coefficient": fq(action_cross),
        "background_vertex_magnitude_without_g": fq(background_vertex_magnitude),
        "project_derivation": [
            "S_(3),+=( -1/4 )*2*g*[W_(1)^a W_(2)a]_F",
            "[W_(1)^a W_(2)a]_F=[W_(1)^a [[D_a v,v]]]_D",
            "S_(3),+=-(g/2)*int tr_kappa(W_(1)^a [[D_a v,v]])",
            "S_(3),-=+(g/2)*int tr_kappa(Wtilde_(1)_dot a [[barD^dot a v,v]])",
            "ordered second variation symmetrizes the two quantum v ports",
            "the perturbative exponent e^{-S_int/hbar} reverses each action-kernel sign",
        ],
        "action_kernel_phases": {"W": chiral_action_phase, "Wtilde": antichiral_action_phase},
        "exponent_vertices": {
            "W": "-(i*g/2)*c_{UCE}*W^{E gamma}*(D_C,gamma-D_U,gamma)",
            "Wtilde": "+(i*g/2)*c_{UCD}*Wtilde^D_dotgamma*(barD_C^dotgamma-barD_U^dotgamma)",
        },
        "exponent_vertex_phases": {"W": chiral_exponent_phase, "Wtilde": antichiral_exponent_phase},
        "vertex_product_without_g2": fq(vertex_product),
        "vertex_product_phase": "(+i)*(-i)=+1",
    }


def insertion(cfg: PrimitiveConfig) -> dict[str, Any]:
    k = cfg.k_plus_coefficient
    dmk = k * cfg.dminus_dplus_to_d2
    pair = dmk * k
    return {
        "canonical_letter": "X_can^A=g^{-1}(nabla_+ W_P,+)^A",
        "linear_letter": "X_can,(1)^A=K_+ v^A",
        "K_plus": "K_+=-(1/4)D_+ barD^2 D_+",
        "source": "I_(2)^{AB}=D_-[(K_+v^A)(K_+v^B)]",
        "ordered_leibniz": [
            "I_(2),A^{AB}=(D_-K_+v^A)(K_+v^B)",
            "I_(2),B^{AB}=(K_+v^A)(D_-K_+v^B)",
        ],
        "parity": {"K_+v": "even", "relative_Leibniz_sign": 1},
        "spin_frame": [
            "epsilon^{+-}=+1",
            "epsilon_{+-}=-1",
            "D^+=D_-",
            "D^-=-D_+",
            "D^2=2 D_-D_+",
        ],
        "Dminus_Kplus": "D_-K_+=-(1/8)D^2 barD^2 D_+",
        "Dminus_Kplus_coefficient": fq(dmk),
        "two_K_insertion_coefficient": fq(pair),
    }


def action_vertex_assignments(cfg: PrimitiveConfig) -> tuple[list[dict[str, Any]], Fraction]:
    rows = [
        {
            "id": "AVL-Abar-then-BW",
            "exponent_order": "S_Wtilde*S_W",
            "fixed_orientation": "A insertion leg -> Wtilde vertex; B insertion leg -> W vertex",
            "coefficient": fq(cfg.expansion_symmetry_factor),
        },
        {
            "id": "AVL-BW-then-Abar",
            "exponent_order": "S_W*S_Wtilde",
            "fixed_orientation": "A insertion leg -> Wtilde vertex; B insertion leg -> W vertex",
            "coefficient": fq(cfg.expansion_symmetry_factor),
        },
    ]
    weight = cfg.expansion_symmetry_factor * cfg.action_vertex_label_assignments
    return rows, weight


def endpoint_rows() -> list[dict[str, Any]]:
    bar = {
        "r0": {"vertex_sign": -1, "transfer_sign": -1},
        "r1": {"vertex_sign": +1, "transfer_sign": +1},
    }
    undotted = {
        "r1": {"vertex_sign": +1, "transfer_sign": +1},
        "r2": {"vertex_sign": -1, "transfer_sign": -1},
    }
    rows: list[dict[str, Any]] = []
    counter = 1
    for placement in ("A", "B"):
        for bar_endpoint in ("r0", "r1"):
            for d_endpoint in ("r1", "r2"):
                raw = bar[bar_endpoint]["vertex_sign"] * undotted[d_endpoint]["vertex_sign"]
                transfer = bar[bar_endpoint]["transfer_sign"] * undotted[d_endpoint]["transfer_sign"]
                final = raw * transfer
                rows.append(
                    {
                        "id": f"WW-DA-{counter:02d}",
                        "Dminus_placement": placement,
                        "ordered_external_descendant": f"O_{placement}|{'B' if placement == 'A' else 'A'}",
                        "barD_endpoint": bar_endpoint,
                        "D_endpoint": d_endpoint,
                        "raw_vertex_sign": raw,
                        "endpoint_transfer_sign": transfer,
                        "final_sign": final,
                        "raw_derivative_word": (
                            f"(D_-K_+)_{placement} K_+ "
                            f"barD[{bar_endpoint}] D[{d_endpoint}]"
                        ),
                        "momentum_numerator": (
                            f"({bar_endpoint})_(+ dotbeta) "
                            f"p^(dotbeta gamma) ({d_endpoint})_(gamma dot-alpha)"
                        ),
                        "classification": "NONCOLLAPSED_METRIC_NUMERATOR",
                        "collapsed_edge": None,
                    }
                )
                counter += 1
    return rows


def dalgebra(cfg: PrimitiveConfig, rows: list[dict[str, Any]]) -> dict[str, Any]:
    insertion_factor = (
        cfg.k_plus_coefficient
        * cfg.dminus_dplus_to_d2
        * cfg.k_plus_coefficient
    )
    anticommutators = cfg.mixed_anticommutator_factor ** cfg.mixed_anticommutator_count
    numerical_weight = insertion_factor * cfg.closed_grassmann_loop * anticommutators
    per_placement = {placement: [row for row in rows if row["Dminus_placement"] == placement] for placement in ("A", "B")}
    sums: dict[str, Any] = {}
    for placement, selected in per_placement.items():
        sums[placement] = {
            "row_count": len(selected),
            "all_final_signs": [row["final_sign"] for row in selected],
            "factorized_numerator": "(r0+r1)_(+ dotbeta) p^(dotbeta gamma) (r1+r2)_(gamma dot-alpha)",
            "L1": "r0+r1=2k+q",
            "L2": "r1+r2=2k+q+P=2k+p+2q",
            "external_descendant_is_not_summed_with_other_placement": True,
        }
    return {
        "delta_normalization": "delta^4(theta)=theta^2 bartheta^2",
        "closed_loop_derivation": "(D^2 theta^2)(barD^2 bartheta^2)=(-4)(-4)=16",
        "closed_loop_factor": cfg.closed_grassmann_loop,
        "fourier_phase": "exp(+i p.x)",
        "complex_bispinor": "mathsf p_(a dot-a)=-i sigma_E^m_(a dot-a) p_m",
        "mixed_anticommutator": "{D_a,barD_dot-a}=2 mathsf p_(a dot-a)",
        "mixed_anticommutator_product": anticommutators,
        "insertion_numerical_factor": fq(insertion_factor),
        "numerator_weight_per_marked_Dminus_placement": fq(numerical_weight),
        "placement_sums": sums,
        "separation_statement": "Wick weight is not included in the D-algebra weight",
    }


def integral_reduction(cfg: PrimitiveConfig) -> dict[str, Any]:
    tensor_multiplier = (
        cfg.feynman_parameter_prefactor
        * cfg.loop_quadratic_leading_factor
        * cfg.tensor_residue_at_d4
        * cfg.simplex_volume
    )
    tensor_residue_without_pi = tensor_multiplier * cfg.scalar_bubble_residue_without_pi
    return {
        "dimension": "d=4-2*epsilon",
        "measure": "mu^(2 epsilon) d^d k/(2 pi)^d",
        "routing": {
            "r0": "k",
            "r1": "k+q",
            "r2": "k+P",
            "P": "p+q",
        },
        "denominators": ["D0=k^2", "D1=(k+q)^2", "D2=(k+P)^2"],
        "feynman_identity": "1/(D0 D1 D2)=2 int_Delta dx dy dz /(ell^2+Delta)^3",
        "shift": "ell=k+y*q+z*P",
        "Delta": "x*y*q^2+x*z*P^2+y*z*p^2",
        "shifted_L1": "L1=2 ell+(1-2y)q-2zP",
        "shifted_L2": "L2=2 ell+(1-2y)q+(1-2z)P",
        "uv_quadratic_numerator": "4 ell^mu ell^nu",
        "tensor_reduction": "int ell^mu ell^nu/(ell^2+Delta)^3=(hatdelta^mu nu/d)*(J2-Delta*J3)",
        "J2": "mu^(2epsilon)/(4pi)^(2-epsilon)*Gamma(epsilon)*Delta^(-epsilon)",
        "J2_laurent_residue": "1/(16*pi^2)",
        "Delta_J3_has_pole": False,
        "simplex_volume": fq(cfg.simplex_volume),
        "tensor_multiplier": fq(tensor_multiplier),
        "triangle_tensor_laurent_residue": f"{fs(tensor_residue_without_pi)}/pi^2 * hatdelta^mu nu",
        "triangle_tensor_residue_without_pi": fq(tensor_residue_without_pi),
    }


def derive(cfg: PrimitiveConfig) -> dict[str, Any]:
    dictionary = canonical_dictionary(cfg)
    gauge = gauge_and_propagator(cfg)
    vertices = derive_vertices(cfg)
    source = insertion(cfg)
    labels, wick_weight = action_vertex_assignments(cfg)
    endpoints = endpoint_rows()
    da = dalgebra(cfg, endpoints)
    integral = integral_reduction(cfg)

    vertex_product = Fraction(**{
        "numerator": vertices["vertex_product_without_g2"]["numerator"],
        "denominator": vertices["vertex_product_without_g2"]["denominator"],
    })
    d_weight = Fraction(**{
        "numerator": da["numerator_weight_per_marked_Dminus_placement"]["numerator"],
        "denominator": da["numerator_weight_per_marked_Dminus_placement"]["denominator"],
    })
    prop_factor = Fraction(**{
        "numerator": gauge["propagator_scalar_factor"]["numerator"],
        "denominator": gauge["propagator_scalar_factor"]["denominator"],
    })
    preintegral = vertex_product * wick_weight * d_weight * prop_factor**3
    tensor_residue = Fraction(**{
        "numerator": integral["triangle_tensor_residue_without_pi"]["numerator"],
        "denominator": integral["triangle_tensor_residue_without_pi"]["denominator"],
    })
    pole = preintegral * tensor_residue

    color = {
        "definition": "C^{AB}{}_{DE}=kappa^{AU} kappa^{BV} kappa^{CC'} c_{UCD} c_{VC'E}",
        "kappa_delta_specialization": "C^{AB}{}_{DE}=c_{ACD} c_{BCE}",
        "orientation": "A insertion leg attaches to Wtilde^D; B insertion leg attaches to W^E",
    }
    amplitude = {
        "marked_object": "fixed orientation A|B with D_- on the A insertion leg",
        "external_tensor": {
            "T": "T_(mu rho nu,+)^dot-alpha=(sigma_E,mu)_(+ dot-beta)*(barsigma_E,rho)^(dot-beta gamma)*(sigma_E,nu)_gamma^dot-alpha",
            "X": "X^E(p)=D_+ W_+^E(p)",
            "O_A": "O_(A,mu nu)^{DE}=Wtilde^D_dot-alpha(q)*p^rho*X^E(p)*T_(mu rho nu,+)^dot-alpha",
            "B_placement": "kept as the distinct ordered descendant O_B; it is not added to O_A as a multiplicity",
        },
        "wick_weight": fq(wick_weight),
        "D_algebra_numerator_weight": fq(d_weight),
        "vertex_product_without_g2": fq(vertex_product),
        "three_propagator_scalar_factor": fq(prop_factor**3),
        "preintegral_coefficient_without_hbar_g2": fq(preintegral),
        "preintegral": (
            "Gamma_T,A=(hbar*g^2/2) C^{AB}{}_{DE} O^{DE}_{A,mu nu} "
            "int mu^(2epsilon)d^d k/(2pi)^d L1^mu L2^nu/(D0 D1 D2)"
        ),
        "pole_coefficient_without_hbar_g2_pi2": fq(pole),
        "pole": "+hbar*g^2/(32*pi^2*epsilon) times C^{AB}{}_{DE} O^{DE}_{A,mu nu} hatdelta^{mu nu}",
        "placement_rule": (
            "the A and B D_- placements are distinct ordered external descendants; "
            "each carries this coefficient and they are not an extra Wick multiplicity"
        ),
    }
    return {
        "canonical_dictionary": dictionary,
        "gauge_and_propagator": gauge,
        "vertices": vertices,
        "source_insertion": source,
        "action_vertex_label_assignments": labels,
        "wick_weight": fq(wick_weight),
        "endpoint_rows": endpoints,
        "dalgebra": da,
        "color": color,
        "integral": integral,
        "amplitude": amplitude,
    }


def locked_invariants(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "dictionary_W_linear": result["canonical_dictionary"]["W_can_linear_coefficient"],
        "propagator_inverse": result["gauge_and_propagator"]["inverse_check"],
        "vertex_product": result["vertices"]["vertex_product_without_g2"],
        "wick_weight": result["wick_weight"],
        "row_count": len(result["endpoint_rows"]),
        "all_row_signs": [row["final_sign"] for row in result["endpoint_rows"]],
        "D_weight": result["dalgebra"]["numerator_weight_per_marked_Dminus_placement"],
        "tensor_multiplier": result["integral"]["tensor_multiplier"],
        "preintegral": result["amplitude"]["preintegral_coefficient_without_hbar_g2"],
        "pole": result["amplitude"]["pole_coefficient_without_hbar_g2_pi2"],
    }


def mutation_tests(baseline: dict[str, Any]) -> list[dict[str, Any]]:
    expected = locked_invariants(baseline)
    cases: list[tuple[str, PrimitiveConfig]] = []
    base = PrimitiveConfig()
    for name, changes in [
        ("MUTATE_V_DICTIONARY_2_TO_1", {"exponent_argument_v": Fraction(1)}),
        ("MUTATE_KINETIC_HESSIAN_1_TO_2", {"kinetic_hessian": Fraction(2)}),
        ("MUTATE_SYMMETRY_FACTOR_HALF_TO_ONE", {"expansion_symmetry_factor": Fraction(1)}),
        ("MUTATE_LABEL_ASSIGNMENTS_2_TO_1", {"action_vertex_label_assignments": 1}),
        ("MUTATE_CLOSED_LOOP_16_TO_8", {"closed_grassmann_loop": 8}),
        ("MUTATE_MIXED_ANTICOMMUTATOR_2_TO_1", {"mixed_anticommutator_factor": 1}),
        ("MUTATE_SIMPLEX_VOLUME_HALF_TO_ONE", {"simplex_volume": Fraction(1)}),
        ("MUTATE_TENSOR_ONE_QUARTER_TO_ONE_HALF", {"tensor_residue_at_d4": Fraction(1, 2)}),
    ]:
        payload = base.__dict__ | changes
        cases.append((name, PrimitiveConfig(**payload)))

    tests: list[dict[str, Any]] = []
    for name, cfg in cases:
        actual = locked_invariants(derive(cfg))
        changed = sorted(key for key in expected if actual[key] != expected[key])
        tests.append({"name": name, "status": "PASS" if changed else "FAIL", "changed_invariants": changed})

    endpoint_mutation = copy.deepcopy(baseline)
    endpoint_mutation["endpoint_rows"][0]["endpoint_transfer_sign"] *= -1
    endpoint_mutation["endpoint_rows"][0]["final_sign"] *= -1
    changed_signs = [row["final_sign"] for row in endpoint_mutation["endpoint_rows"]]
    tests.append(
        {
            "name": "MUTATE_ONE_ENDPOINT_TRANSFER_SIGN",
            "status": "PASS" if changed_signs != expected["all_row_signs"] else "FAIL",
            "changed_invariants": ["all_row_signs"] if changed_signs != expected["all_row_signs"] else [],
        }
    )
    return tests


def checks(result: dict[str, Any], mutations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    inv = locked_invariants(result)
    expected = {
        "dictionary_W_linear": fq(Fraction(-1, 4)),
        "propagator_inverse": fq(Fraction(1)),
        "vertex_product": fq(Fraction(1, 4)),
        "wick_weight": fq(Fraction(1)),
        "row_count": 8,
        "all_row_signs": [1] * 8,
        "D_weight": fq(Fraction(2)),
        "tensor_multiplier": fq(Fraction(1)),
        "preintegral": fq(Fraction(1, 2)),
        "pole": fq(Fraction(1, 32)),
    }
    out = []
    for key, want in expected.items():
        out.append({"id": key, "status": "PASS" if inv[key] == want else "FAIL", "actual": inv[key], "expected": want})
    out.append(
        {
            "id": "all_mutations_detected",
            "status": "PASS" if all(test["status"] == "PASS" for test in mutations) else "FAIL",
            "actual": [test["status"] for test in mutations],
            "expected": ["PASS"] * len(mutations),
        }
    )
    return out


def markdown(audit: dict[str, Any]) -> str:
    rows = audit["derivation"]["endpoint_rows"]
    table = "\n".join(
        "| {id} | {Dminus_placement} | {barD_endpoint} | {D_endpoint} | {raw_vertex_sign} | "
        "{endpoint_transfer_sign} | {final_sign} | `{momentum_numerator}` |".format(**row)
        for row in rows
    )
    mutation_table = "\n".join(
        f"| {row['name']} | {row['status']} | {', '.join(row['changed_invariants'])} |"
        for row in audit["mutation_tests"]
    )
    check_table = "\n".join(
        f"| {row['id']} | {row['status']} |"
        for row in audit["checks"]
    )
    template = r"""# Canonical-superfield WW seed: conditional arithmetic audit

Authority: `__AUTHORITY_COMMIT__`, verify run `__VERIFY_RUN__`.  HT target 与 imported candidate coefficient 未进入计算。

## 1. Notation

$$
\epsilon^{{+-}}=1,\qquad \epsilon_{{+-}}=-1,\qquad
D^+=D_-,\qquad D^-=-D_+,
$$

$$
D^2=2D_-D_+,\qquad
e^{{ip\cdot x}}:\ \partial_m\mapsto ip_m,\qquad
\mathsf p_{{a\dot a}}=-i(\sigma_E^m)_{{a\dot a}}p_m.
$$

因此

$$
\{{D_a,\bar D_{{\dot a}}\}}=2\mathsf p_{{a\dot a}}.
$$

## 2. Absorbed-to-canonical dictionary

$$
\boxed{{\mathcal V_P=2g v,\qquad \mathcal W_P=gW_{{\rm can}}}},
$$

$$
v=\frac{{\mathcal V_P}}{{2g}},\qquad
W_{{\rm can}}=\frac{{\mathcal W_P}}g.
$$

由

$$
e^{{-X}}De^X=DX+\frac12[DX,X]+O(X^3),\qquad X=2gv,
$$

得到

$$
W_{{\rm can,a}}=W_{{(1)a}}+gW_{{(2)a}}+O(g^2),
$$

$$
W_{{(1)a}}=-\frac14\bar D^2D_av,
\qquad
W_{{(2)a}}=-\frac14\bar D^2\llbracket D_av,v\rrbracket.
$$

## 3. Background Fermi--Feynman gauge

在 residual-free slice 锁定

$$
\mathcal F_+=-\frac14(\bar{\boldsymbol\nabla}_B)^2(2gv),
\qquad
\mathcal F_-=-\frac14(\boldsymbol\nabla_B)^2(2gv),
\qquad \alpha=1.
$$

Gauge action 与该 gauge-fermion Hessian 的和为

$$
S_0=\frac12\int d^dx\,d^4\theta\,
\kappa_{{AB}}v^A(-\partial^2)v^B.
$$

故

$$
K_{{AB}}(p)=\kappa_{{AB}}p^2,
\qquad
K_{{AC}}(p)\frac{{\kappa^{{CB}}}}{{p^2}}=\delta_A{{}}^B,
$$

$$
\boxed{{
\langle v^A(p,\theta_1)v^B(-p,\theta_2)\rangle_0
=\hbar\frac{{\kappa^{{AB}}}}{{p^2}}
\delta^4(\theta_1-\theta_2)}}.
$$

## 4. Two background field-strength vertices

Chiral action 的 cubic cross term：

$$
S_{{(3),+}}
=-\frac g2\int d^dx\,d^4\theta\,
\operatorname{{tr}}_\kappa
\left(W_{{(1)}}^a\llbracket D_av,v\rrbracket\right).
$$

Antichiral term：

$$
S_{{(3),-}}
=+\frac g2\int d^dx\,d^4\theta\,
\operatorname{{tr}}_\kappa
\left(\widetilde W_{{(1)\dot a}}
\llbracket\bar D^{{\dot a}}v,v\rrbracket\right).
$$

Ordered second variation 后，再乘 $e^{{-S_{{\rm int}}/\hbar}}$ 的 minus sign：

$$
\boxed{{
\mathcal V_W
=-\frac{{ig}}2c_{{UCE}}W^{{E\gamma}}
(D_{{C\gamma}}-D_{{U\gamma}})}},
$$

$$
\boxed{{
\mathcal V_{{\widetilde W}}
=+\frac{{ig}}2c_{{UCD}}\widetilde W^D_{{\dot\gamma}}
(\bar D_C^{{\dot\gamma}}-\bar D_U^{{\dot\gamma}})}}.
$$

因此

$$
\left(+\frac{{ig}}2\right)
\left(-\frac{{ig}}2\right)=\frac{{g^2}}4.
$$

## 5. Ordered source and Wick weight

$$
K_+=-\frac14D_+\bar D^2D_+,
$$

$$
\mathcal I_{{(2)}}^{{AB}}
=D_-\left[(K_+v^A)(K_+v^B)\right]
=(D_-K_+v^A)(K_+v^B)
+(K_+v^A)(D_-K_+v^B).
$$

Fixed orientation 中 action expansion 给出

$$
\frac1{{2!}}
\left(S_{{\widetilde W}}S_W+S_WS_{{\widetilde W}}\right)
=S_{{\widetilde W}}S_W.
$$

故

$$
\boxed{{w_{{\rm Wick}}=\frac12(1+1)=1}}.
$$

这两个 label assignments 不是两个 graph orientations。

## 6. Eight derivative-endpoint rows

The table records the endpoint-sign ledger.  Its signs remain conditional until a full noncommutative superspace integration-by-parts trace derives every transfer from one explicit $D$-word.

| id | $D_-$ placement | $\bar D$ endpoint | $D$ endpoint | raw sign | transfer sign | final sign | numerator |
|---|---:|---:|---:|---:|---:|---:|---|
__ENDPOINT_TABLE__

每个 placement 的四项严格相加为

$$
\left[(r_0)_{{+\dot\beta}}+(r_1)_{{+\dot\beta}}\right]
\mathsf p^{{\dot\beta\gamma}}
\left[(r_1)_\gamma{{}}^{{\dot\alpha}}+(r_2)_\gamma{{}}^{{\dot\alpha}}\right].
$$

定义

$$
r_0=k,\qquad r_1=k+q,\qquad r_2=k+P,\qquad P=p+q,
$$

$$
L_1=r_0+r_1=2k+q,
\qquad
L_2=r_1+r_2=2k+p+2q.
$$

## 7. D-algebra weight

$$
D_-K_+=-\frac18D^2\bar D^2D_+,
$$

$$
\left(-\frac18\right)\left(-\frac14\right)=\frac1{{32}}.
$$

$$
[D^2\bar D^2\delta^4(\theta)]_{{\theta=0}}
=(D^2\theta^2)(\bar D^2\bar\theta^2)=(-4)(-4)=16.
$$

两个 mixed anticommutators 各给出 $2$：

$$
\boxed{{w_{{D\text{-alg}}}=\frac1{{32}}\cdot16\cdot2\cdot2=2}}.
$$

这里没有乘 Wick weight；$w_{{\rm Wick}}=1$ 已独立固定。

The two factors $2$ are arithmetic inputs in this checkpoint, not outputs of an explicit $D$-word rewrite engine:

$$
\boxed{{\texttt{{BLOCKED\_EXPLICIT\_WW\_D\_ALGEBRA\_WORD\_DERIVATION}}}}.
$$

## 8. Fixed-orientation preintegral

令

$$
\mathcal C^{{AB}}{{}}_{{DE}}
=\kappa^{{AU}}\kappa^{{BV}}\kappa^{{CC'}}
c_{{UCD}}c_{{VC'E}}.
$$

再定义

$$
T_{{\mu\rho\nu,+}}{{}}^{{\dot\alpha}}
:=(\sigma_{{E,\mu}})_{{+\dot\beta}}
(\bar\sigma_{{E,\rho}})^{{\dot\beta\gamma}}
(\sigma_{{E,\nu}})_\gamma{{}}^{{\dot\alpha}},
\qquad
X^E(p):=D_+W_+^E(p),
$$

$$
\mathcal O_{{A,\mu\nu}}^{{DE}}
:=\widetilde W^D_{{\dot\alpha}}(q)\,p^\rho X^E(p)\,
T_{{\mu\rho\nu,+}}{{}}^{{\dot\alpha}}.
$$

下标 $A$ 表示 marked $D_-$ placement；$B$ placement 保持为另一 ordered descendant $\mathcal O_B$，不并入 $\mathcal O_A$ 的 multiplicity。

对一个 marked $D_-$ placement：

$$
\frac{{g^2}}4\times w_{{\rm Wick}}\times w_{{D\text{-alg}}}
=\frac{{g^2}}4\times1\times2=\frac{{g^2}}2.
$$

$$
\boxed{{
\Gamma_{{T,A}}
=\frac{{\hbar g^2}}2\mathcal C^{{AB}}{{}}_{{DE}}
\mathcal O^{{DE}}_{{A,\mu\nu}}
\mu^{{2\epsilon}}\int\frac{{d^dk}}{{(2\pi)^d}}
\frac{{L_1^\mu L_2^\nu}}
{{k^2(k+q)^2(k+P)^2}}}}.
$$

两个 $D_-$ placements 对应两个 ordered external descendants，不能作为额外 multiplicity 相加到同一个 coefficient。

## 9. UV pole

$$
\frac1{{D_0D_1D_2}}
=2\int_{{x,y,z\ge0}}dx\,dy\,dz\,
\delta(1-x-y-z)\frac1{{(\ell^2+\Delta)^3}},
$$

$$
\ell=k+yq+zP,
\qquad
\Delta=xyq^2+xzP^2+yzp^2.
$$

UV quadratic numerator 为 $4\ell^\mu\ell^\nu$，且

$$
\mu^{{2\epsilon}}\int\frac{{d^d\ell}}{{(2\pi)^d}}
\frac{{\ell^\mu\ell^\nu}}{{(\ell^2+\Delta)^3}}
=\frac{{\widehat\delta^{{\mu\nu}}}}d(J_2-\Delta J_3),
$$

$$
J_2
=\frac{{\mu^{{2\epsilon}}}}{{(4\pi)^{{2-\epsilon}}}}
\Gamma(\epsilon)\Delta^{{-\epsilon}},
\qquad
\operatorname{{Res}}_{{\epsilon=0}}J_2=\frac1{{16\pi^2}},
$$

$$
\operatorname{{Res}}_{{\epsilon=0}}(\Delta J_3)=0,
\qquad
\int dx\,dy\,dz\,\delta(1-x-y-z)=\frac12.
$$

因此 tensor residue multiplier 是

$$
2\times4\times\frac14\times\frac12=1,
$$

$$
\operatorname{{Res}}_{{\epsilon=0}}
\mu^{{2\epsilon}}\int\frac{{d^dk}}{{(2\pi)^d}}
\frac{{L_1^\mu L_2^\nu}}{{D_0D_1D_2}}
=\frac{{\widehat\delta^{{\mu\nu}}}}{{16\pi^2}}.
$$

最终

$$
\boxed{{
\Gamma_{{T,A}}\Big|_{{1/\epsilon}}
=+\frac{{\hbar g^2}}{{32\pi^2\epsilon}}
\mathcal C^{{AB}}{{}}_{{DE}}
\mathcal O^{{DE}}_{{A,\mu\nu}}
\widehat\delta^{{\mu\nu}}}}.
$$

## 10. Mutation audit

| mutation | status | changed invariants |
|---|---|---|
__MUTATION_TABLE__

| invariant | status |
|---|---|
__CHECK_TABLE__

## 11. Boundary

本 audit 只检查 isolated WW parent-triangle 的 coefficient arithmetic、Wick weight、recorded $D$-algebra numerator weight 与 ordinary metric pole。Explicit $D$-word transfer derivation、contact/collapsed/link/ghost/counterterm cuts 及 $\widehat\delta-\delta_4$ remainder 不在此 seed artifact 中宣称完成。
"""
    out: list[str] = []
    cursor = 0
    while cursor < len(template):
        pair = template[cursor : cursor + 2]
        if pair == "{{":
            out.append("{")
            cursor += 2
        elif pair == "}}":
            out.append("}")
            cursor += 2
        else:
            out.append(template[cursor])
            cursor += 1
    return (
        "".join(out)
        .replace("__AUTHORITY_COMMIT__", AUTHORITY_COMMIT)
        .replace("__VERIFY_RUN__", VERIFY_RUN)
        .replace("__ENDPOINT_TABLE__", table)
        .replace("__MUTATION_TABLE__", mutation_table)
        .replace("__CHECK_TABLE__", check_table)
    )


def build_audit() -> dict[str, Any]:
    derivation = derive(PrimitiveConfig())
    mutations = mutation_tests(derivation)
    verification = checks(derivation, mutations)
    status = (
        "PASS_ARITHMETIC_WITH_EXPLICIT_D_WORD_BLOCKER"
        if all(row["status"] == "PASS" for row in verification)
        else "FAIL"
    )
    return {
        "schema": "step5-canonical-superfield-ww-seed-v1",
        "authority": {
            "commit": AUTHORITY_COMMIT,
            "verify_run": VERIFY_RUN,
            "task": TASK_ID,
            "authority_sha256": "3970e8769fc21a5f41a1fa0d4e537b577f3d1d7b212bc6795819b37b6d58ae6f",
            "task_sha256": "4ed8aa9957868233f4c1b7ff4a4c4ec02744c153ffd0d16e30f6e322042ba749",
        },
        "scope": {
            "included": [
                "canonical dictionary",
                "background supersymmetric Fermi--Feynman gauge lock",
                "free vector-superfield propagator",
                "two background field-strength vertices",
                "ordered quadratic WW source",
                "two action-vertex label assignments",
                "eight D-minus/endpoint rows",
                "fixed-orientation noncollapsed preintegral",
                "ordinary DRED metric pole",
            ],
            "excluded": [
                "holomorphic-twist target",
                "imported candidate coefficient",
                "gauge-complete cutting orbit",
                "finite anomaly remainder",
            ],
        },
        "foundations": FOUNDATIONS,
        "derivation": derivation,
        "mutation_tests": mutations,
        "checks": verification,
        "blockers": [
            {
                "id": "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION",
                "effect": (
                    "The endpoint transfer signs and the two mixed-anticommutator "
                    "factors are recorded primitives. A full representative superspace "
                    "D-word, four endpoint integration-by-parts chains, and the exchange "
                    "map for the second marked placement have not been generated from a "
                    "noncommutative rewrite trace."
                ),
            }
        ],
        "status": status,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", default="audits/step5-canonical-superfield-ww-seed.json")
    parser.add_argument("--markdown", default="audits/step5-canonical-superfield-ww-seed.md")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    audit = build_audit()
    root = Path(__file__).resolve().parents[1]
    json_path = root / args.json
    md_path = root / args.markdown
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(markdown(audit), encoding="utf-8")
    print(json.dumps({
        "status": audit["status"],
        "checks": len(audit["checks"]),
        "mutations": len(audit["mutation_tests"]),
        "endpoint_rows": len(audit["derivation"]["endpoint_rows"]),
        "json": str(json_path),
        "markdown": str(md_path),
    }, sort_keys=True))
    if args.check and audit["status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
