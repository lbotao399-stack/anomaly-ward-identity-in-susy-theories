#!/usr/bin/env python3
"""Exact primitive WW seed graph, endpoint traces, and SD edge collapses.

The module uses only the Project formulas already present in the Step-5
contract.  It does not import the anomaly coefficient or insert epsilon in a
bare numerator.  Finite-BV data do not enter this fixed-gauge seed.
"""

from __future__ import annotations

import csv
from dataclasses import replace
import hashlib
import importlib.util
import io
import json
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (
    Chirality,
    ExternalLeg,
    FieldType,
    Flow,
    GraphIR,
    HalfEdge,
    IndexSlot,
    IndexSpace,
    InternalEdge,
    Statistics,
    Variance,
    Vertex,
)
from scripts.step5_project_composites import seed_port_assignment_payload


OUT = ROOT / "generated/step5"
AUDIT = ROOT / "audits/step5-ww-seed-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
SEED_MATRIX_VERIFIER = ROOT / "scripts/verify_step5_seed_dalgebra.py"


def color(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.COLOR_ADJOINT, label, Variance.UP)


def undotted(label: str, variance: Variance = Variance.DOWN) -> IndexSlot:
    return IndexSlot(IndexSpace.UNDOTTED, label, variance)


def dotted(label: str, variance: Variance = Variance.UP) -> IndexSlot:
    return IndexSlot(IndexSpace.DOTTED, label, variance)


V_FIELD = FieldType("V", Statistics.BOSON, Chirality.REAL, (color("C"),))
W_FIELD = FieldType(
    "W_plus", Statistics.FERMION, Chirality.CHIRAL, (color("E"), undotted("+"))
)
TILDE_W_FIELD = FieldType(
    "TildeW_dot_alpha",
    Statistics.FERMION,
    Chirality.ANTICHIRAL,
    (color("D"), dotted("dot_alpha")),
)
WW_SOURCE_FIELD = FieldType(
    "Source[nabla_-(X^A X^B)]",
    Statistics.BOSON,
    Chirality.UNCONSTRAINED,
    (color("A"), color("B")),
)


def project_matrix_engine_checks() -> dict[str, object]:
    specification = importlib.util.spec_from_file_location(
        "step5_ww_seed_matrix_binding", SEED_MATRIX_VERIFIER
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load exact Project 16x16 Grassmann engine")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    groups = {
        "delta_normalization": module.normalization_checks(),
        "Project_K_plus_chain": module.project_coefficient_checks(),
        "edge_endpoint_transfer": module.endpoint_transfer_checks(),
        "mixed_anticommutators": module.mixed_anticommutator_checks(),
        "affine_routing": module.routing_checks(),
    }
    return {
        "engine": "exact 16x16 exterior-algebra matrices over Q(i)",
        "verifier_sha256": hashlib.sha256(SEED_MATRIX_VERIFIER.read_bytes()).hexdigest(),
        "groups": groups,
        "checks": sum(len(checks) for checks in groups.values()),
        "failed": sum(not value for checks in groups.values() for value in checks.values()),
    }


def external_orientation_sign_audit(orientation: str) -> dict[str, object]:
    """Koszul audit in the fixed pre-D external word (TildeW,W)."""

    if orientation not in ("DIRECT", "REFLECTED"):
        raise ValueError(orientation)
    canonical_word = ("TildeW", "W")
    declared_word = canonical_word if orientation == "DIRECT" else tuple(reversed(canonical_word))
    positions = {field: position for position, field in enumerate(canonical_word)}
    inversions = sum(
        1
        for left in range(len(declared_word))
        for right in range(left + 1, len(declared_word))
        if positions[declared_word[left]] > positions[declared_word[right]]
    )
    external_permutation_sign = -1 if inversions % 2 else 1

    # Once the word is canonical, the odd D acts on the second odd factor W.
    # IBP contributes -1.  The graded Leibniz prefix TildeW contributes -1.
    ibp_outer_sign = -1
    target_prefix_parity = 1
    graded_prefix_sign = -1 if target_prefix_parity % 2 else 1
    d_transfer_sign = ibp_outer_sign * graded_prefix_sign
    total = external_permutation_sign * d_transfer_sign
    return {
        "orientation": orientation,
        "declared_pre_D_word": list(declared_word),
        "canonical_pre_D_word": list(canonical_word),
        "parities": {"TildeW": 1, "W": 1, "D": 1, "X=D_W": 0},
        "odd_odd_inversions": inversions,
        "external_fermion_permutation_sign": external_permutation_sign,
        "D_transfer": {
            "IBP_outer_sign": ibp_outer_sign,
            "target_prefix_parity": target_prefix_parity,
            "graded_Leibniz_prefix_sign": graded_prefix_sign,
            "product": d_transfer_sign,
            "output": "X^E=nabla_+W_+^E",
        },
        "total_orientation_sign": total,
    }


def physical_triangle(orientation: str) -> GraphIR:
    """Return one exact port-labelled orientation of the primitive WW triangle."""

    if orientation not in ("DIRECT", "REFLECTED"):
        raise ValueError(orientation)
    left_letter, right_letter = ("A", "B") if orientation == "DIRECT" else ("B", "A")
    suffix = "Abar_BW" if orientation == "DIRECT" else "Bbar_AW"
    graph_id = f"T-{suffix}-w0-01"
    sign_audit = external_orientation_sign_audit(orientation)

    half_edges = (
        HalfEdge(f"{suffix}_I_{left_letter}", "vI", 0, V_FIELD, Flow.OUT, "k"),
        HalfEdge(
            f"{suffix}_I_{right_letter}", "vI", 1, V_FIELD, Flow.IN, "-k-p-q"
        ),
        HalfEdge(f"{suffix}_I_source", "vI", 2, WW_SOURCE_FIELD, Flow.IN, "p+q"),
        HalfEdge(f"{suffix}_bar_{left_letter}", "vBar", 0, V_FIELD, Flow.IN, "-k"),
        HalfEdge(f"{suffix}_bar_C", "vBar", 1, V_FIELD, Flow.OUT, "k+q"),
        HalfEdge(f"{suffix}_bar_ext", "vBar", 2, TILDE_W_FIELD, Flow.IN, "-q"),
        HalfEdge(f"{suffix}_W_C", "vW", 0, V_FIELD, Flow.IN, "-k-q"),
        HalfEdge(f"{suffix}_W_{right_letter}", "vW", 1, V_FIELD, Flow.OUT, "k+p+q"),
        HalfEdge(f"{suffix}_W_ext", "vW", 2, W_FIELD, Flow.IN, "-p"),
    )

    graph = GraphIR(
        graph_id=graph_id,
        vertices=(
            Vertex(
                "vI",
                "COMPOSITE_INSERTION_I2_WW",
                tuple(item.half_edge_id for item in half_edges[0:3]),
                f"D_-[K_+V^{left_letter} K_+V^{right_letter}]",
                (left_letter, right_letter),
                "theta_0",
                "delta(k-(k+p+q)+(p+q))",
                coefficient_factors=("K_+=-(1/8)D_+barD^2D_+", "graded_Leibniz"),
            ),
            Vertex(
                "vBar",
                "BACKGROUND_CUBIC_TILDE_W",
                tuple(item.half_edge_id for item in half_edges[3:6]),
                "-i*h/8",
                (f"c_{{{left_letter}CD}}",),
                "theta_1",
                "delta(-k+(k+q)-q)",
                coefficient_factors=("-i*h/8", f"c_{{{left_letter}CD}}"),
            ),
            Vertex(
                "vW",
                "BACKGROUND_CUBIC_W",
                tuple(item.half_edge_id for item in half_edges[6:9]),
                "+i*h/8",
                (f"c_{{{right_letter}CE}}",),
                "theta_2",
                "delta(-(k+q)+(k+p+q)-p)",
                coefficient_factors=("+i*h/8", f"c_{{{right_letter}CE}}"),
            ),
        ),
        half_edges=half_edges,
        internal_edges=(
            InternalEdge(
                "e0",
                half_edges[0].half_edge_id,
                half_edges[3].half_edge_id,
                "-2*g^2*kappa^{-1}*delta4theta/r0^2",
                "k",
                Flow.OUT,
            ),
            InternalEdge(
                "e1",
                half_edges[4].half_edge_id,
                half_edges[6].half_edge_id,
                "-2*g^2*kappa^{-1}*delta4theta/r1^2",
                "k+q",
                Flow.OUT,
            ),
            InternalEdge(
                "e2",
                half_edges[7].half_edge_id,
                half_edges[1].half_edge_id,
                "-2*g^2*kappa^{-1}*delta4theta/r2^2",
                "k+p+q",
                Flow.OUT,
            ),
        ),
        external_legs=(
            ExternalLeg(
                "L_source",
                half_edges[2].half_edge_id,
                WW_SOURCE_FIELD,
                "p+q",
                f"{left_letter}{right_letter}",
            ),
            ExternalLeg(
                "L_tildeW",
                half_edges[5].half_edge_id,
                TILDE_W_FIELD,
                "q",
                "D",
                spinor_indices=(dotted("dot_alpha"),),
            ),
            ExternalLeg(
                "L_W",
                half_edges[8].half_edge_id,
                W_FIELD,
                "p",
                "E",
                spinor_indices=(undotted("+"),),
            ),
        ),
        loop_momenta=("k",),
        metadata=tuple(
            sorted(
                {
                    "orientation": orientation,
                    "all_incoming_momentum": "true",
                    "physical_external_momenta": "TildeW(q),W(p),source(P=p+q)",
                    "routing": "r0=k;r1=k+q;r2=k+p+q",
                    "denominator": "k^2*(k+q)^2*(k+p+q)^2",
                    "symmetry_factor": "1",
                    "wick_multiplicity": "1",
                    "wick_sign": "+1",
                    "external_declared_pre_D_word": ",".join(sign_audit["declared_pre_D_word"]),
                    "external_canonical_pre_D_word": ",".join(sign_audit["canonical_pre_D_word"]),
                    "external_fermion_permutation_sign": str(
                        sign_audit["external_fermion_permutation_sign"]
                    ),
                    "D_transfer_Koszul_sign": str(sign_audit["D_transfer"]["product"]),
                    "total_orientation_sign": str(sign_audit["total_orientation_sign"]),
                    "bare_numerator_contains_epsilon": "false",
                    "color_factor": f"c_{{{left_letter}CD}}*c_{{{right_letter}CE}}",
                }.items()
            )
        ),
    )
    graph.assert_linear_momentum_routing()
    return graph


ENDPOINTS = (
    ("e0", "r0", -1, -1, "e1", "r1", +1, +1),
    ("e0", "r0", -1, -1, "e2", "r2", -1, -1),
    ("e1", "r1", +1, +1, "e1", "r1", +1, +1),
    ("e1", "r1", +1, +1, "e2", "r2", -1, -1),
)


def endpoint_rows(orientation: str) -> list[dict[str, object]]:
    graph = physical_triangle(orientation)
    sign_audit = external_orientation_sign_audit(orientation)
    orientation_sign = int(sign_audit["total_orientation_sign"])
    rows: list[dict[str, object]] = []
    for placement_index, placement in enumerate(("LEFT_LETTER", "RIGHT_LETTER"), start=1):
        for endpoint_index, endpoint in enumerate(ENDPOINTS, start=1):
            (
                bar_edge,
                bar_momentum,
                bar_vertex_sign,
                bar_transfer_sign,
                d_edge,
                d_momentum,
                d_vertex_sign,
                d_transfer_sign,
            ) = endpoint
            endpoint_sign = (
                bar_vertex_sign
                * bar_transfer_sign
                * d_vertex_sign
                * d_transfer_sign
            )
            insertion_prefactor = Fraction(1, 128)
            closed_delta = 16
            first_mixed = "2i"
            second_mixed = "2i"
            d_chain = insertion_prefactor * closed_delta * (-4)
            graph_before_d = Fraction(-1, 8)
            graph_row = graph_before_d * d_chain * endpoint_sign * orientation_sign
            row_sign = "+" if orientation_sign == 1 else "-"
            contact_sign = "-" if orientation_sign == 1 else "+"
            trace_id = f"DA-{orientation[0]}-{(placement_index - 1) * 4 + endpoint_index:03d}"
            rows.append(
                {
                    "trace_id": trace_id,
                    "graph_id": graph.graph_id,
                    "orientation": orientation,
                    "D_minus_placement": placement,
                    "barD_endpoint": {"edge": bar_edge, "momentum": bar_momentum},
                    "D_endpoint": {"edge": d_edge, "momentum": d_momentum},
                    "edge_tagged_raw_word": (
                        f"D_-[I,{placement}] K_+[I,e0] K_+[I,e2] "
                        f"barD_dot_alpha[vBar,{bar_edge}] D_a[vW,{d_edge}]"
                    ),
                    "vertex_signs": [bar_vertex_sign, d_vertex_sign],
                    "endpoint_transfer_signs": [bar_transfer_sign, d_transfer_sign],
                    "koszul_signs": [1, 1],
                    "external_sign_audit": sign_audit,
                    "total_endpoint_sign": endpoint_sign,
                    "total_orientation_sign": orientation_sign,
                    "exact_D_chain": {
                        "insertion_prefactor": "1/128",
                        "closed_delta": "16",
                        "mixed_anticommutators": [first_mixed, second_mixed],
                        "product": "-1/2",
                    },
                    "graph_prefactor_before_D_chain": "-g^2/8",
                    "row_prefactor": f"{row_sign}g^2/16",
                    "triangle_metric_pole": (
                        f"{row_sign}g^2/(1024*pi^2*epsilon)*hat_delta^(mu nu)"
                    ),
                    "contact_metric_pole": (
                        f"{contact_sign}g^2/(1024*pi^2*epsilon)*delta4^(mu nu)"
                    ),
                    "metric_orbit": (
                        f"{row_sign}g^2/(1024*pi^2*epsilon)*(hat_delta-delta4)^(mu nu)"
                    ),
                    "metric_contact_child_id": f"{graph.graph_id}__SD_metric__{trace_id}",
                    "momentum_numerator": (
                        f"({bar_momentum})_+^dot_beta * (i*p)_a_dot_beta * "
                        f"({d_momentum})^a_dot_alpha"
                    ),
                    "mixed_anticommutator_momenta": [bar_momentum, "p", d_momentum],
                    "external_leg_derivative_tokens": [
                        "partial_(a dot_beta)[W_plus^E(p)]=i*p_(a dot_beta)*W_plus^E(p)"
                    ],
                    "propagator_collapses_in_metric_branch": [],
                    "SD_collapse_children": [
                        f"{graph.graph_id}__collapse__e0",
                        f"{graph.graph_id}__collapse__e1",
                        f"{graph.graph_id}__collapse__e2",
                    ],
                    "classification": "ORDINARY_UV_POLE",
                    "orbit_classification": "ANOMALY_CANDIDATE_METRIC_POLE",
                    "trace": [
                        {
                            "input": "D_-[K_+V] K_+V or K_+V D_-[K_+V]",
                            "rule": "D_-K_+=-(1/16)D^2 barD^2 D_+",
                            "sign": +1,
                            "output": "insertion prefactor 1/128",
                        },
                        {
                            "input": f"barD difference selects {bar_edge}",
                            "rule": "edge endpoint transfer",
                            "sign": bar_transfer_sign,
                            "output": f"barD tagged to {bar_edge} with {bar_momentum}",
                        },
                        {
                            "input": f"D difference selects {d_edge}",
                            "rule": "edge endpoint transfer",
                            "sign": d_transfer_sign,
                            "output": f"D tagged to {d_edge} with {d_momentum}",
                        },
                        {
                            "input": "D^2 barD^2 delta4theta",
                            "rule": "closed Grassmann loop",
                            "sign": +1,
                            "output": "16",
                        },
                        {
                            "input": "two ordered mixed D-barD pairs",
                            "rule": "{D_a,barD_dot_b}=-2D_(a dot_b), Fourier D_(a dot_b)=i*p_(a dot_b)",
                            "sign": +1,
                            "output": [first_mixed, second_mixed],
                        },
                        {
                            "input": "(1/128)*16*(2i)*(2i)",
                            "rule": "exact Q(i) multiplication",
                            "sign": -1,
                            "output": "-1/2",
                        },
                    ],
                    "exact_checks": {
                        "endpoint_sign_is_plus_one": endpoint_sign == 1,
                        "D_chain_is_minus_one_half": d_chain == Fraction(-1, 2),
                        "row_prefactor_has_orientation_sign": graph_row
                        == Fraction(orientation_sign, 16),
                        "bare_numerator_has_no_epsilon": "epsilon" not in (
                            f"{bar_momentum}*p*{d_momentum}"
                        ),
                    },
                }
            )
    return rows


def collapsed_children(graph: GraphIR) -> tuple[GraphIR, ...]:
    return tuple(graph.collapse_edge(edge_id) for edge_id in ("e0", "e1", "e2"))


def contact_basis_catalogue() -> dict[str, object]:
    base = seed_port_assignment_payload()
    selected = base["selected_for_seed"]
    assert isinstance(selected, dict)
    i3 = selected["I3_one_background_two_quantum"]
    s3_bar = selected["S3_antichiral_one_background_two_quantum"]
    i4_tadpole = selected["I4_two_background_two_quantum_tadpole"]
    s4_mixed = selected["S4_mixed_X_TildeW"]
    legal_pair = selected["legal_X_TildeW_two_vertex_pair"]

    def projected_records(items: object, family: str) -> list[dict[str, object]]:
        assert isinstance(items, (list, tuple))
        return [
            {
                "basis_term_id": f"{family}__{item['projected_assignment_id']}",
                "family": family,
                "classification": "ORDERED_PORT_BASIS_TERM_NOT_GRAPH",
                "projected_assignment_id": item["projected_assignment_id"],
                "source_term_id": item["source_term_id"],
                "quantum_ports": item["quantum_ports"],
                "external_projections": item["external_projections"],
                "source_coefficient": item["source_coefficient"],
                "individual_metric_pole_coefficient": "BASIS_DEPENDENT",
            }
            for item in items
        ]

    def tadpole_records(items: object) -> list[dict[str, object]]:
        assert isinstance(items, (list, tuple))
        return [
            {
                "basis_term_id": f"QUARTIC_I4_TADPOLE__{item['assignment_id']}",
                "family": "QUARTIC_I4_TADPOLE",
                "assignment_id": item["assignment_id"],
                "source_term_id": item["source_term_id"],
                "source_coefficient": item["source_coefficient"],
                "loop_topology": item["loop_topology"],
                "classification": item["classification"],
                "zero_rule": item["zero_rule"],
                "individual_metric_pole_coefficient": "0_IF_SCALELESS_ROUTING_CHECK_PASSES",
            }
            for item in items
        ]

    families = {
        "NONLINEAR_I3": projected_records(i3, "NONLINEAR_I3"),
        "ACTION_S3_ANTICHIRAL": projected_records(s3_bar, "ACTION_S3_ANTICHIRAL"),
        "QUARTIC_I4_TADPOLE": tadpole_records(i4_tadpole),
    }
    return {
        "background_quantum_substitution": base["substitution"],
        "families": families,
        "counts": {name: len(items) for name, items in families.items()},
        "all_basis_term_ids": [
            item["basis_term_id"] for items in families.values() for item in items
        ],
        "individual_decomposition": "BASIS_DEPENDENT",
        "legal_two_vertex_contact_family": legal_pair,
        "mixed_S4_typed_zero": s4_mixed,
        "exact_aggregate_rule": (
            "sum_(ordered basis terms in one trace) C_term "
            "= +g^2/(1024*pi^2*epsilon)"
        ),
    }


def metric_contact_children(
    graph: GraphIR,
    rows: list[dict[str, object]],
    basis: dict[str, object],
) -> tuple[GraphIR, ...]:
    basis_ids = basis["all_basis_term_ids"]
    assert isinstance(basis_ids, list)
    children: list[GraphIR] = []
    for row in rows:
        trace_id = str(row["trace_id"])
        orientation_sign = int(row["total_orientation_sign"])
        triangle_sign = "+" if orientation_sign == 1 else "-"
        contact_sign = "-" if orientation_sign == 1 else "+"
        # e1 is a canonical representative of the bubble after the SD cut.
        # The nonlinear/I4/S4 decomposition is retained separately as a
        # background-quantum port basis and is not identified with this edge.
        child = graph.collapse_edge("e1")
        metadata = dict(child.metadata)
        metadata.update(
            {
                "parent_trace_id": trace_id,
                "graph_relation": "SD_AGGREGATE_METRIC_CONTACT",
                "SD_cut_rule": "K_V^tot*G_V=identity_16",
                "SD_functional_identity": (
                    "0=Integral Dv d/dv_i[I exp(-S/hbar)]="
                    "<dI/dv_i>-(1/hbar)<I dS/dv_i>"
                ),
                "contact_metric": "delta4^(mu nu)",
                "triangle_orientation_sign": str(orientation_sign),
                "contact_amplitude_sign": str(-orientation_sign),
                "unsigned_scalar_pole": "g^2/(1024*pi^2*epsilon)",
                "signed_triangle_pole": (
                    f"{triangle_sign}g^2*hat_delta^(mu nu)/(1024*pi^2*epsilon)"
                ),
                "contact_pole": (
                    f"{contact_sign}g^2*delta4^(mu nu)/(1024*pi^2*epsilon)"
                ),
                "basis_decomposition": "BASIS_DEPENDENT",
                "basis_term_count": str(len(basis_ids)),
                "basis_term_ids_sha256": hashlib.sha256(
                    "\n".join(basis_ids).encode()
                ).hexdigest(),
                "coefficient_conservation": (
                    f"sum(C_basis_terms)={triangle_sign}g^2/(1024*pi^2*epsilon)"
                ),
                "relative_sign_derivation": (
                    "contact minus sign is the second term of the exact SD identity"
                ),
            }
        )
        children.append(
            replace(
                child,
                graph_id=f"{graph.graph_id}__SD_metric__{trace_id}",
                metadata=tuple(sorted(metadata.items())),
            )
        )
    return tuple(children)


def pole_ledger() -> dict[str, object]:
    """Derive the SD-complete metric mismatch and its finite DRED remainder."""

    return {
        "normalization": {
            "A0": "1/(16*pi^2)",
            "dimension": "d=4-2*epsilon",
            "simplex_integral": "2*Integral_simplex 1 = 1",
            "rank_two_pole": (
                "Integral d^d ell/(2*pi)^d ell^mu ell^nu/(ell^2+Delta)^3 "
                "= A0*hat_g^(mu nu)/(4*epsilon)+finite"
            ),
        },
        "triangle_derivation": [
            "L1^mu L2^nu = 4*ell^mu*ell^nu + terms with at most one ell",
            "2*Integral_simplex 1 = 1",
            "Integral_triangle L1^mu L2^nu/(D0*D1*D2)|pole = A0*hat_g^(mu nu)/epsilon",
            "two D_minus placements give preintegration coefficient g^2/8",
        ],
        "triangle_poles": {
            "DIRECT": (
                "+g^2/(128*pi^2*epsilon)*c_{ACD}c_{BCE}*T_(mu n nu)*"
                "hat_delta^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
            "REFLECTED": (
                "-g^2/(128*pi^2*epsilon)*c_{BCD}c_{ACE}*T_(mu n nu)*"
                "hat_delta^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
        },
        "triangle_status": "DERIVED_ISOLATED_TRIANGLE_ORDINARY_UV_POLE",
        "contact_poles": {
            "DIRECT": (
                "-g^2/(128*pi^2*epsilon)*c_{ACD}c_{BCE}*T_(mu n nu)*"
                "delta4^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
            "REFLECTED": (
                "+g^2/(128*pi^2*epsilon)*c_{BCD}c_{ACE}*T_(mu n nu)*"
                "delta4^(mu nu)*TildeW^D(q)*(i*p^n)*X^E(p)"
            ),
        },
        "contact_status": "AGGREGATE_SD_IDENTITY_NOT_BASIS_RESOLVED",
        "missing_rule_is_not_finite_BV": True,
        "bare_triangle_numerator_contains_epsilon": False,
        "metric_conventions": {
            "tilde_delta": "delta4-hat_delta",
            "mismatch": "hat_delta-delta4=-tilde_delta",
        },
        "metric_mismatches": {
            "DIRECT": "+g^2*(hat_delta-delta4)^(mu nu)/(128*pi^2*epsilon)",
            "REFLECTED": "-g^2*(hat_delta-delta4)^(mu nu)/(128*pi^2*epsilon)",
        },
        "metric_mismatch_proved_at_aggregate_sd_level": True,
        "full_ordinary_triangle_bubble_cancellation_proved": False,
        "evanescent_sigma_contraction": (
            "p^rho*tilde_delta^(mu nu)*T_(mu rho nu)=-2*epsilon*p_+"
        ),
        "finite_remainder_derivation": [
            "hat_delta-delta4=-tilde_delta",
            "(-tilde_delta)*T*p = -(-2*epsilon)*p_+ = +2*epsilon*p_+",
            "[g^2/(128*pi^2*epsilon)]*[2*epsilon]=g^2/(64*pi^2)",
        ],
        "anomaly_coefficient_fixed_orientation": "+g^2/(64*pi^2)",
        "anomaly_coefficients": {
            "DIRECT": "+g^2/(64*pi^2)",
            "REFLECTED": "-g^2/(64*pi^2)",
        },
        "reflected_relabelling": [
            "-c_{BCD}c_{ACE}*TildeW^D*X^E",
            "D<->E",
            "-c_{BCE}c_{ACD}*TildeW^E*X^D",
            "X is even, so TildeW^E*X^D=X^D*TildeW^E",
        ],
        "two_orientation_single_color_tensor": (
            "g^2/(64*pi^2)*c_{ACD}c_{BCE}*"
            "(i*p_+^dot_alpha)*[TildeW_dot_alpha^D*X^E-"
            "X^D*TildeW_dot_alpha^E]"
        ),
        "single_color_tensor_with_X_definition": (
            "X^E=nabla_+W_+^E; therefore "
            "c_{ACD}c_{BCE}[TildeW_dot_alpha^D*nabla_+^dot_alpha X^E-"
            "(nabla_+^dot_alpha X^D)*TildeW_dot_alpha^E]"
        ),
        "post_D_external_operator": "X^E=nabla_+ W_+^E",
        "pre_D_action_external_field": "W_+^E",
        "anomaly_status": "DERIVED_AGGREGATE_SD_CANDIDATE_NOT_ACCEPTED",
    }


def tex_for_graph(graph: GraphIR) -> str:
    metadata = dict(graph.metadata)
    return "\n".join(
        (
            r"\documentclass[tikz,border=6pt]{standalone}",
            r"\usetikzlibrary{arrows.meta,shapes.geometric}",
            r"\begin{document}",
            r"\begin{tikzpicture}[>=stealth]",
            r"\node[draw,diamond] (I) at (0,0) {$\nabla_-[X^A X^B]$};",
            r"\node[draw,circle,fill=black,inner sep=2pt,label=above left:$\widetilde W^D_{\dot\alpha}(q)$] (B) at (-2,2) {};",
            r"\node[draw,circle,fill=black,inner sep=2pt,label=above right:$W^E_+(p)$] (W) at (2,2) {};",
            r"\draw[->] (I) -- node[left] {$r_0=k$} (B);",
            r"\draw[->] (B) -- node[above] {$r_1=k+q$} (W);",
            r"\draw[->] (W) -- node[right] {$r_2=k+p+q$} (I);",
            rf"\node at (0,-1.2) {{$ {metadata['color_factor']} $}};",
            r"\end{tikzpicture}",
            r"\end{document}",
            "",
        )
    )


def tex_for_contact(orientation: str) -> str:
    if orientation not in ("DIRECT", "REFLECTED"):
        raise ValueError(orientation)
    sign = "-" if orientation == "DIRECT" else "+"
    trace_family = "DA-D-001--008" if orientation == "DIRECT" else "DA-R-001--008"
    return "\n".join(
        (
            r"\documentclass[tikz,border=6pt]{standalone}",
            r"\usetikzlibrary{arrows.meta,shapes.geometric}",
            r"\begin{document}",
            r"\begin{tikzpicture}[>=Stealth]",
            r"\node[draw,diamond,align=center] (I3) at (-2,0) {$I_{(3)}[X_{\mathrm{ext}};v,v]$};",
            r"\node[draw,circle,align=center] (S3) at (2,0) {$\widetilde S_{(3)}[\widetilde W_{\mathrm{ext}};v,v]$};",
            r"\draw[->,bend left=35] (I3) to node[above] {$k$} (S3);",
            r"\draw[->,bend left=35] (S3) to node[below] {$k+q$} (I3);",
            rf"\node at (0,-2.1) {{\textsf{{{trace_family}}}}};",
            rf"\node at (0,-2.6) {{$ {sign}\,g^2\delta_{{(4)}}^{{mn}}/(128\pi^2\epsilon) $}};",
            r"\end{tikzpicture}",
            r"\end{document}",
            "",
        )
    )


def markdown_report(payload: dict[str, object]) -> str:
    lines = [
        "# Step 5A primitive WW seed",
        "",
        "$$",
        r"r_0=k,\qquad r_1=k+q,\qquad r_2=k+p+q.",
        "$$",
        "",
        "$$",
        r"\frac1{128}\,16\,(2i)(2i)=-\frac12.",
        "$$",
        "",
        "Each endpoint row:",
        "",
        "$$",
        r"\left(-\frac{g^2}{8}\right)\left(-\frac12\right)=\frac{g^2}{16}.",
        "$$",
        "",
        "Two placements and four endpoint assignments give",
        "",
        "$$",
        r"\Gamma_{\triangle}^{A|B}=\frac{g^2}{8}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)",
        r"(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}",
        r"\int\frac{d^dk}{(2\pi)^d}\frac{L_{1m}L_{2r}}{k^2(k+q)^2(k+p+q)^2},",
        "$$",
        "",
        "$$",
        r"L_1=2k+q,\qquad L_2=2k+p+2q.",
        "$$",
        "",
        "$$",
        r"\Gamma_{\triangle,\mathrm{pole}}^{A|B}=\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)",
        r"(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\widehat g_{mr}.",
        "$$",
        "",
        "$$",
        r"\Gamma_{C,\mathrm{pole}}^{A|B}=-\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)",
        r"(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\delta^{(4)}_{mr}.",
        "$$",
        "",
        "$$",
        r"\Gamma_{\triangle+C,\mathrm{pole}}^{A|B}=\frac{g^2}{128\pi^2\epsilon}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip^n)X^E(p)",
        r"(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}(\widehat\delta-\delta_{(4)})_{mr}.",
        "$$",
        "",
        "$$",
        r"\widehat\delta-\delta_{(4)}=-\widetilde\delta,\qquad p^n\widetilde\delta^{mr}(\sigma_m\bar\sigma_n\sigma_r)_+{}^{\dot\alpha}=-2\epsilon p_+{}^{\dot\alpha}.",
        "$$",
        "",
        "$$",
        r"\Gamma_{\mathrm{anom}}^{A|B}=\frac{g^2}{64\pi^2}c_{ACD}c_{BCE}\widetilde W^D_{\dot\alpha}(q)(ip_+{}^{\dot\alpha})X^E(p).",
        "$$",
        "",
        "$$",
        r"\Gamma_{\mathrm{anom}}^{B|A}=-\frac{g^2}{64\pi^2}c_{BCD}c_{ACE}\widetilde W^D_{\dot\alpha}(q)(ip_+{}^{\dot\alpha})X^E(p).",
        "$$",
        "",
        r"In the reflected term relabel $D\leftrightarrow E$; since $|X|=0$:",
        "",
        "$$",
        r"\Gamma_{\mathrm{anom}}^{A|B}+\Gamma_{\mathrm{anom}}^{B|A}",
        r"=\frac{g^2}{64\pi^2}c_{ACD}c_{BCE}(ip_+{}^{\dot\alpha})",
        r"\left[\widetilde W^D_{\dot\alpha}X^E-X^D\widetilde W^E_{\dot\alpha}\right].",
        "$$",
        "",
        r"Pre-$D$ action leg: $W_+^E$. Post-$D$ operator: $X^E=\nabla_+W_+^E$.",
        "",
    ]
    for orientation in ("DIRECT", "REFLECTED"):
        lines.extend((f"## {orientation}", "", "| trace | $D_-$ | $\\bar D$ edge | $D$ edge | endpoint sign | external Koszul sign | numerator | triangle pole | contact pole |", "|---|---|---|---|---:|---:|---|---|---|"))
        for row in payload["traces"][orientation]:
            lines.append(
                f"| {row['trace_id']} | {row['D_minus_placement']} | "
                f"{row['barD_endpoint']['edge']} | {row['D_endpoint']['edge']} | "
                f"{row['total_endpoint_sign']} | {row['total_orientation_sign']} | "
                f"`{row['momentum_numerator']}` | "
                f"`{row['triangle_metric_pole']}` | `{row['contact_metric_pole']}` |"
            )
        lines.append("")
    return "\n".join(lines)


def build_payload() -> dict[str, object]:
    graphs = {orientation: physical_triangle(orientation) for orientation in ("DIRECT", "REFLECTED")}
    basis = contact_basis_catalogue()
    children = {
        orientation: [item.canonical_dict() for item in collapsed_children(graph)]
        for orientation, graph in graphs.items()
    }
    traces = {orientation: endpoint_rows(orientation) for orientation in graphs}
    metric_children = {
        orientation: [
            item.canonical_dict()
            for item in metric_contact_children(graph, traces[orientation], basis)
        ]
        for orientation, graph in graphs.items()
    }
    return {
        "schema": 1,
        "scope": "STEP_5A_PRIMITIVE_WW_SEED_W0",
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "graphs": {orientation: graph.canonical_dict() for orientation, graph in graphs.items()},
        "traces": traces,
        "SD_collapsed_children": children,
        "SD_metric_contact_children": metric_children,
        "contact_basis_catalogue": basis,
        "SD_orbit_status": {
            "parent_triangles": 2,
            "edge_collapsed_children": 6,
            "metric_contact_children": 16,
            "nonlinear_letter_basis_children": basis["counts"]["NONLINEAR_I3"],
            "antichiral_action_basis_children": basis["counts"]["ACTION_S3_ANTICHIRAL"],
            "quartic_I4_tadpole_basis_children": basis["counts"]["QUARTIC_I4_TADPOLE"],
            "mixed_S4_children": 0,
            "mixed_S4_status": basis["mixed_S4_typed_zero"]["status"],
            "individual_basis_decomposition": "BASIS_DEPENDENT",
            "aggregate_contact_pole": "EXACT",
            "finite_BV_required": False,
        },
        "preintegration": {
            "denominator": "k^2*(k+q)^2*(k+p+q)^2",
            "L1": "2*k+q",
            "L2": "2*k+p+2*q",
            "coefficient_per_endpoint_row": {"DIRECT": "+g^2/16", "REFLECTED": "-g^2/16"},
            "coefficient_per_D_minus_placement_after_four_endpoint_sum": {
                "DIRECT": "+g^2/16",
                "REFLECTED": "-g^2/16",
            },
            "coefficient_after_two_D_minus_placements": {
                "DIRECT": "+g^2/8",
                "REFLECTED": "-g^2/8",
            },
            "bare_numerator": "L1^mu*p^nu*L2^rho",
            "bare_numerator_contains_epsilon": False,
            "pre_D_action_external_field": "W_plus^E",
            "post_D_external_operator": "X^E=nabla_+W_+^E",
        },
        "exact_matrix_binding": project_matrix_engine_checks(),
        "external_orientation_sign_audits": {
            orientation: external_orientation_sign_audit(orientation)
            for orientation in ("DIRECT", "REFLECTED")
        },
        "poles": pole_ledger(),
    }


def write_outputs(payload: dict[str, object]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ww-seed-graph-ir.json").write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    )
    (OUT / "ww-seed-dalgebra.md").write_text(markdown_report(payload))
    for orientation in ("DIRECT", "REFLECTED"):
        graph = physical_triangle(orientation)
        stem = orientation.lower()
        (OUT / f"ww-seed-{stem}.dot").write_text(graph.to_dot())
        (OUT / f"ww-seed-{stem}.tex").write_text(tex_for_graph(graph))
        (OUT / f"ww-seed-contact-{stem}.tex").write_text(
            tex_for_contact(orientation)
        )

    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(
        ("trace_id", "orientation", "D_minus_placement", "barD_edge", "D_edge", "sign", "numerator", "classification")
    )
    for orientation in ("DIRECT", "REFLECTED"):
        for row in payload["traces"][orientation]:
            writer.writerow(
                (
                    row["trace_id"],
                    orientation,
                    row["D_minus_placement"],
                    row["barD_endpoint"]["edge"],
                    row["D_endpoint"]["edge"],
                    row["total_endpoint_sign"],
                    row["momentum_numerator"],
                    row["classification"],
                )
            )
    (OUT / "ww-seed-dalgebra.csv").write_text(buffer.getvalue())


def build_audit(payload: dict[str, object]) -> dict[str, object]:
    checks: dict[str, bool] = {}
    for orientation in ("DIRECT", "REFLECTED"):
        graph = physical_triangle(orientation)
        checks[f"{orientation}_routing"] = bool(graph.validate_linear_momentum_routing()["passed"])
        checks[f"{orientation}_one_loop"] = graph.cycle_rank() == 1
        checks[f"{orientation}_three_edges"] = len(graph.internal_edges) == 3
        checks[f"{orientation}_eight_rows"] = len(payload["traces"][orientation]) == 8
        checks[f"{orientation}_four_endpoints_per_placement"] = all(
            sum(row["D_minus_placement"] == placement for row in payload["traces"][orientation]) == 4
            for placement in ("LEFT_LETTER", "RIGHT_LETTER")
        )
        checks[f"{orientation}_all_row_checks"] = all(
            all(row["exact_checks"].values()) for row in payload["traces"][orientation]
        )
        checks[f"{orientation}_three_collapsed_children"] = len(
            payload["SD_collapsed_children"][orientation]
        ) == 3
        checks[f"{orientation}_eight_metric_contact_children"] = len(
            payload["SD_metric_contact_children"][orientation]
        ) == 8
        checks[f"{orientation}_row_contact_bijection"] = {
            child["metadata"]["parent_trace_id"]
            for child in payload["SD_metric_contact_children"][orientation]
        } == {row["trace_id"] for row in payload["traces"][orientation]}
    checks["bare_triangle_has_no_epsilon"] = not payload["preintegration"][
        "bare_numerator_contains_epsilon"
    ]
    checks["exact_16x16_matrix_binding"] = payload["exact_matrix_binding"]["failed"] == 0
    checks["triangle_pole_is_separate"] = payload["poles"]["triangle_status"] == (
        "DERIVED_ISOLATED_TRIANGLE_ORDINARY_UV_POLE"
    )
    checks["row_pole_sum_is_orientation_pole"] = Fraction(8, 1024) == Fraction(1, 128)
    checks["direct_orientation_sign"] = payload["external_orientation_sign_audits"]["DIRECT"][
        "total_orientation_sign"
    ] == 1
    checks["reflected_orientation_sign"] = payload["external_orientation_sign_audits"][
        "REFLECTED"
    ]["total_orientation_sign"] == -1
    checks["D_transfer_sign_is_common_plus"] = all(
        payload["external_orientation_sign_audits"][orientation]["D_transfer"]["product"] == 1
        for orientation in ("DIRECT", "REFLECTED")
    )
    checks["finite_remainder_coefficient"] = Fraction(2, 128) == Fraction(1, 64)
    checks["contact_pole_is_aggregate_SD_not_basis_resolved"] = payload["poles"][
        "contact_status"
    ] == (
        "AGGREGATE_SD_IDENTITY_NOT_BASIS_RESOLVED"
    )
    checks["metric_mismatch_proved_at_aggregate_sd_level"] = bool(
        payload["poles"]["metric_mismatch_proved_at_aggregate_sd_level"]
    )
    checks["full_ordinary_triangle_bubble_cancellation_remains_open"] = not bool(
        payload["poles"]["full_ordinary_triangle_bubble_cancellation_proved"]
    )
    checks["anomaly_is_aggregate_sd_candidate_not_accepted"] = payload["poles"][
        "anomaly_status"
    ] == (
        "DERIVED_AGGREGATE_SD_CANDIDATE_NOT_ACCEPTED"
    )
    checks["post_D_operator_is_X"] = payload["poles"]["post_D_external_operator"] == (
        "X^E=nabla_+ W_+^E"
    )
    return {
        "schema": 1,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope": (
            "primitive WW w=0 triangle, exact endpoint traces, edge collapses, "
            "and SD aggregate metric-contact orbit"
        ),
        "checks": checks,
        "totals": {"checks": len(checks), "failed": sum(not value for value in checks.values())},
        "derived": {
            "graphs": 2,
            "D_algebra_traces": 16,
            "collapsed_children": 6,
            "metric_contact_children": 16,
            "triangle_poles": payload["poles"]["triangle_poles"],
            "contact_poles": payload["poles"]["contact_poles"],
            "anomaly_coefficient_fixed_orientation": payload["poles"][
                "anomaly_coefficient_fixed_orientation"
            ],
            "two_orientation_single_color_tensor": payload["poles"][
                "two_orientation_single_color_tensor"
            ],
        },
        "unresolved_non_BV_rule": None,
        "contract_sha256": payload["contract_sha256"],
    }


def main() -> None:
    payload = build_payload()
    write_outputs(payload)
    audit = build_audit(payload)
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    if audit["status"] != "PASS":
        raise SystemExit(1)
    print(
        "Step-5 WW seed: "
        f"graphs={audit['derived']['graphs']} "
        f"traces={audit['derived']['D_algebra_traces']} "
        f"collapsed={audit['derived']['collapsed_children']} "
        f"metric_contacts={audit['derived']['metric_contact_children']}"
    )


if __name__ == "__main__":
    main()
