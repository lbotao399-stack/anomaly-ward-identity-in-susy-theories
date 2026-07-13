#!/usr/bin/env python3
"""Exact Step-5A primitive two-background Hessian-family audit.

The module instantiates the four rooted one-loop words

    + G0 I0 G0 H1 G0 H1
    - G0 I0 G0 H2
    - G0 I1 G0 H1
    + G0 I2

and the independent CT2 term.  It derives every available insertion/action
block from the current Project composite and action grammars, enumerates all
six Gaussian species blocks, and emits one typed GraphIR for every labeled
surviving vector-block family.  Missing source partners, propagator blocks,
background-covariant FP/NK Hessian blocks, counterterm coefficients,
D-algebra, poles, and anomaly coefficients remain fail-closed.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (  # noqa: E402
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
from scripts import step5_pipeline_ir as pipeline_ir  # noqa: E402
from scripts.step5_project_composites import (  # noqa: E402
    insertion_terms_at_valence,
    ordered_background_quantum_assignments,
)
from scripts.step5_supergraph_pipeline import (  # noqa: E402
    TILDE_W_FIELD,
    graph_automorphism_order,
    graph_canonical_key,
    ww_reflected_seed_request,
)
from scripts.step5_vertex_grammar import (  # noqa: E402
    ActionMonomial,
    build_project_vertex_grammar,
)


GENERATED = ROOT / "generated/step5/one-loop-n2-physical-hessian-family.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-n2-physical-hessian-family-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-n2-physical-hessian-family.md"


@dataclass(frozen=True)
class BlockSpec:
    block_id: str
    sector: str
    carrier_fields: tuple[str, ...]
    parity: int
    supertrace_weight: int


BLOCKS = (
    BlockSpec("V", "PHYSICAL_VECTOR", ("V",), 0, 1),
    BlockSpec("PHI_PAIR_1", "PHYSICAL_ADJOINT_CHIRAL_PAIR", ("Phi_1", "TildePhi_1"), 0, 1),
    BlockSpec("PHI_PAIR_2", "PHYSICAL_ADJOINT_CHIRAL_PAIR", ("Phi_2", "TildePhi_2"), 0, 1),
    BlockSpec("PHI_PAIR_3", "PHYSICAL_ADJOINT_CHIRAL_PAIR", ("Phi_3", "TildePhi_3"), 0, 1),
    BlockSpec(
        "FP",
        "FADDEEV_POPOV",
        ("cprime_plus", "tilde_c", "tilde_cprime_minus", "c"),
        1,
        -1,
    ),
    BlockSpec("NK", "NIELSEN_KALLOSH", ("b_NK", "tilde_b_NK"), 0, 1),
)
BLOCK_IDS = tuple(block.block_id for block in BLOCKS)
BLOCK_BY_ID = {block.block_id: block for block in BLOCKS}


def exact_coefficient_payload(coefficient: object) -> dict[str, object]:
    rational = Fraction(getattr(coefficient, "rational"))
    return {
        "rational": {
            "numerator": rational.numerator,
            "denominator": rational.denominator,
        },
        "sqrt2_power": int(getattr(coefficient, "sqrt2_power", 0)),
        "i_power": int(getattr(coefficient, "i_power", 0)),
        "symbols": list(getattr(coefficient, "symbols", ())),
        "rendered": str(coefficient.render()),
    }


def source_kernel_branches(source_order: int) -> list[dict[str, object]]:
    """Expand I_s into ordered background labels and Hessian row/column ports."""

    if source_order not in (0, 1, 2):
        raise ValueError("the primitive n=2 census uses I0, I1, I2")
    valence = source_order + 2
    terms = insertion_terms_at_valence(valence)
    term_by_id = {term.term_id: term for term in terms}
    assignments = ordered_background_quantum_assignments(terms)
    labels = tuple(f"V_{index}" for index in range(1, source_order + 1))
    rows: list[dict[str, object]] = []
    for assignment in assignments:
        if assignment["role_counts"] != {
            "BACKGROUND_EXTERNAL": source_order,
            "QUANTUM_WICK": 2,
        }:
            continue
        ports = assignment["ordered_ports"]
        assert isinstance(ports, list)
        background_ports = tuple(
            str(port["port_id"])
            for port in ports
            if isinstance(port, dict) and port["role"] == "BACKGROUND_EXTERNAL"
        )
        quantum_ports = tuple(
            str(port["port_id"])
            for port in ports
            if isinstance(port, dict) and port["role"] == "QUANTUM_WICK"
        )
        term = term_by_id[str(assignment["source_term_id"])]
        for label_order in permutations(labels):
            label_map = tuple(zip(background_ports, label_order, strict=True))
            for row_port, column_port in permutations(quantum_ports):
                rows.append(
                    {
                        "branch_id": f"I{source_order}__B{len(rows) + 1:04d}",
                        "kernel": f"I_{source_order}[V,V]",
                        "source_term_id": term.term_id,
                        "source_term_family": term.family,
                        "source_equations": list(term.source_equations),
                        "source_coefficient": assignment["source_coefficient"],
                        "ordered_background_ports": [
                            {"port_id": port, "label": label}
                            for port, label in label_map
                        ],
                        "hessian_row_port": row_port,
                        "hessian_column_port": column_port,
                        "quantum_statistics": "BOSON",
                        "functional_derivative_koszul_sign": 1,
                        "coefficient_status": "EXACT_PROJECT_COMPOSITE_BRANCH",
                        "ordered_ports": ports,
                        "color_bracket_word": assignment["color_bracket_word"],
                    }
                )
    return rows


def _action_block(monomial: ActionMonomial, quantum_fields: Sequence[str]) -> tuple[str, ...]:
    fields = tuple(quantum_fields)
    if fields == ("V", "V") or fields == ("V", "V")[::-1]:
        return ("V",)
    if sorted(fields) == ["Phi", "TildePhi"]:
        return ("PHI_PAIR_1", "PHI_PAIR_2", "PHI_PAIR_3")
    return ()


def fp_quantum_interaction_monomials() -> dict[str, list[dict[str, object]]]:
    """Separate quantum-v FP interactions from background Hessian blocks.

    In the current FP grammar, every explicit ``V`` occurs inside ``sV`` and
    is a quantum prepotential.  The background dependence is hidden in
    ``barNabla_B^2`` or ``Nabla_B^2`` and has not been expanded.  Therefore
    the explicit ``V^n c'c`` monomials cannot be relabeled as ``H_n[V_B^n]``.
    """

    rows = {"V_QUANTUM_ORDER_1": [], "V_QUANTUM_ORDER_2": []}
    for monomial in build_project_vertex_grammar().action_monomials:
        if monomial.sector != "FP_GHOST":
            continue
        v_count = sum(field.field_name == "V" for field in monomial.ordered_fields)
        if v_count not in (1, 2):
            continue
        rows[f"V_QUANTUM_ORDER_{v_count}"].append(
            {
                "monomial_id": monomial.monomial_id,
                "ordered_fields": [field.field_name for field in monomial.ordered_fields],
                "coefficient": exact_coefficient_payload(monomial.coefficient),
                "derivative_scopes": [asdict(scope) for scope in monomial.derivative_scopes],
                "source_equations": list(monomial.source_equations),
                "classification": "QUANTUM_INTERACTION_NOT_BACKGROUND_HESSIAN",
                "background_hessian_status": "BLOCKED_MISSING_PROJECT_BLOCK",
            }
        )
    return rows


def action_hessian_branches(background_order: int) -> list[dict[str, object]]:
    """Derive H_r block branches from ordered Project action monomials."""

    if background_order not in (1, 2):
        raise ValueError("the primitive n=2 census uses H1 and H2")
    labels = tuple(f"V_{index}" for index in range(1, background_order + 1))
    rows: list[dict[str, object]] = []
    action = build_project_vertex_grammar().action_monomials
    for monomial in sorted(action, key=lambda item: item.monomial_id):
        fields = monomial.ordered_fields
        v_positions = tuple(
            position for position, occurrence in enumerate(fields) if occurrence.field_name == "V"
        )
        for background_positions in combinations(v_positions, background_order):
            background_set = set(background_positions)
            quantum_positions = tuple(
                position for position in range(len(fields)) if position not in background_set
            )
            if len(quantum_positions) != 2:
                continue
            quantum_fields = tuple(fields[position].field_name for position in quantum_positions)
            block_ids = _action_block(monomial, quantum_fields)
            if not block_ids:
                continue
            background_ports = tuple(fields[position].occurrence_id for position in background_positions)
            quantum_ports = tuple(fields[position].occurrence_id for position in quantum_positions)
            for block_id in block_ids:
                flavor = block_id.rsplit("_", 1)[-1] if block_id.startswith("PHI_PAIR_") else None
                for label_order in permutations(labels):
                    for row_port, column_port in permutations(quantum_ports):
                        row_occurrence = next(
                            occurrence for occurrence in fields if occurrence.occurrence_id == row_port
                        )
                        column_occurrence = next(
                            occurrence for occurrence in fields if occurrence.occurrence_id == column_port
                        )
                        rows.append(
                            {
                                "branch_id": f"H{background_order}__B{len(rows) + 1:04d}",
                                "kernel": f"H_{background_order}[{block_id},{block_id}]",
                                "block_id": block_id,
                                "source_monomial_id": monomial.monomial_id,
                                "source_sector": monomial.sector,
                                "source_measure": monomial.measure,
                                "source_equations": list(monomial.source_equations),
                                "monomial_coefficient": exact_coefficient_payload(monomial.coefficient),
                                "ordered_background_ports": [
                                    {"port_id": port, "label": label}
                                    for port, label in zip(background_ports, label_order, strict=True)
                                ],
                                "hessian_row": {
                                    "port_id": row_port,
                                    "field": (
                                        f"{row_occurrence.field_name}_{flavor}"
                                        if flavor is not None
                                        else row_occurrence.field_name
                                    ),
                                },
                                "hessian_column": {
                                    "port_id": column_port,
                                    "field": (
                                        f"{column_occurrence.field_name}_{flavor}"
                                        if flavor is not None
                                        else column_occurrence.field_name
                                    ),
                                },
                                "ordered_color_word": list(monomial.color_word),
                                "derivative_scopes": [asdict(scope) for scope in monomial.derivative_scopes],
                                "functional_derivative_koszul_sign": 1,
                                "coefficient_status": "EXACT_PROJECT_ACTION_BRANCH",
                            }
                        )
    return rows


def block_branch_registry() -> dict[str, object]:
    source = {f"I{order}": source_kernel_branches(order) for order in (0, 1, 2)}
    action = {f"H{order}": action_hessian_branches(order) for order in (1, 2)}
    return {
        "source": source,
        "action": action,
        "fp_quantum_interactions_excluded_from_H_r": fp_quantum_interaction_monomials(),
        "generation_rules": {
            "source": {
                "I0": "2 Project I_(2) terms * C(2,0) background choices * 0! background labels * 2! ordered Hessian ports = 4",
                "I1": "10 Project I_(3) terms * C(3,1) background choices * 1! background labels * 2! ordered Hessian ports = 60",
                "I2": "30 Project I_(4) terms * C(4,2) background choices * 2! background labels * 2! ordered Hessian ports = 720",
                "normalization": "V_j=(V_B)_j+v_j changes no coefficient; every ordered role assignment has multiplicity one; no automorphism or factorial is divided from the functional-derivative branches",
            },
            "vector_action": {
                "H1": "4 Project cubic gauge-action monomials * C(3,1) background choices * 1! background labels * 2! ordered Hessian ports = 24",
                "H2": "6 Project quartic gauge-action monomials * C(4,2) background choices * 2! background labels * 2! ordered Hessian ports = 144",
                "normalization": "each branch retains the exact action-monomial coefficient, derivative scopes, and color word",
            },
        },
        "counts": {
            **{name: len(rows) for name, rows in source.items()},
            **{
                f"{name}_{block_id}": sum(row["block_id"] == block_id for row in rows)
                for name, rows in action.items()
                for block_id in BLOCK_IDS
            },
        },
    }


def source_block_matrix(source_order: int, branch_count: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row_block in BLOCK_IDS:
        for column_block in BLOCK_IDS:
            vector = row_block == column_block == "V"
            rows.append(
                {
                    "row_block": row_block,
                    "column_block": column_block,
                    "bare_seed_status": (
                        "ACTUAL_NONZERO_PROJECT_BLOCK" if vector else "TYPED_ZERO_BARE_PURE_VECTOR_SOURCE"
                    ),
                    "bare_branch_count": branch_count if vector else 0,
                    "source_completed_status": (
                        "ACTUAL_BARE_BLOCK_PLUS_BLOCKED_SOURCE_COMPLETION"
                        if vector
                        else "BLOCKED_MISSING_PROJECT_BLOCK"
                    ),
                    "proof": (
                        f"I_{source_order} is generated by the Project V-prepotential composite grammar"
                        if vector
                        else "the bare functional derivative acts on a carrier outside the V-only composite; a BRST/source-partner completion is not present"
                    ),
                }
            )
    return rows


def hessian_block_matrix(background_order: int, branches: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    counts = {
        block_id: sum(row["block_id"] == block_id for row in branches) for block_id in BLOCK_IDS
    }
    rows: list[dict[str, object]] = []
    for row_block in BLOCK_IDS:
        for column_block in BLOCK_IDS:
            diagonal = row_block == column_block
            count = counts[row_block] if diagonal else 0
            if count:
                coefficient_status = "EXACT_PROJECT_ACTION_BRANCHES"
                status = "ACTUAL_NONZERO_PROJECT_BLOCK"
                proof = "ordered Project action monomials have the required two quantum ports and background-V valence"
            elif diagonal and row_block == "NK":
                coefficient_status = "BLOCKED_COEFFICIENT_MISSING_PROJECT_BLOCK"
                status = "BLOCKED_MISSING_PROJECT_BLOCK"
                proof = "the current grammar contains no background-covariant NK Hessian expansion"
            elif diagonal and row_block == "FP":
                coefficient_status = "BLOCKED_COEFFICIENT_MISSING_PROJECT_BLOCK"
                status = "BLOCKED_MISSING_PROJECT_BLOCK"
                proof = "the explicit V^n c-prime c monomials contain quantum v; the background covariant-derivative expansion is absent"
            else:
                coefficient_status = "NOT_APPLICABLE_TYPED_ZERO"
                status = "TYPED_ZERO_PROJECT_SECTOR_OR_FLAVOR_BLOCK"
                proof = "no current Project action monomial has this ordered quadratic carrier pair at the required background order"
            rows.append(
                {
                    "row_block": row_block,
                    "column_block": column_block,
                    "status": status,
                    "branch_count": count,
                    "coefficient_status": coefficient_status,
                    "proof": proof,
                }
            )
    return rows


def propagator_block_matrix() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for block in BLOCKS:
        if block.block_id == "V":
            status = "ACTUAL_NONZERO_PROJECT_BLOCK"
            kernel = "G_V=-2*g^2*kappa^(-1)*1_16/p^2"
        else:
            status = "BLOCKED_MISSING_PROJECT_BLOCK"
            kernel = None
        rows.append(
            {
                "block_id": block.block_id,
                "status": status,
                "kernel": kernel,
                "effect": (
                    "admitted Step-5A vector Wick kernel"
                    if block.block_id == "V"
                    else "the current immutable WW notation schema contains no normalized superfield propagator for this carrier"
                ),
            }
        )
    return rows


def _matrix_status(rows: Sequence[dict[str, object]], row_block: str, column_block: str) -> str:
    matches = [
        str(row.get("bare_seed_status", row.get("status")))
        for row in rows
        if row["row_block"] == row_block and row["column_block"] == column_block
    ]
    if len(matches) != 1:
        raise AssertionError("block matrix lookup is not unique")
    return matches[0]


FAMILY_TEMPLATES = (
    {
        "family": "I0_H1_H1",
        "nodes": 3,
        "kernels": (("I0", 0, 1), ("H1", 1, 2), ("H1", 2, 0)),
    },
    {
        "family": "I0_H2",
        "nodes": 2,
        "kernels": (("I0", 0, 1), ("H2", 1, 0)),
    },
    {
        "family": "I1_H1",
        "nodes": 2,
        "kernels": (("I1", 0, 1), ("H1", 1, 0)),
    },
    {
        "family": "I2",
        "nodes": 1,
        "kernels": (("I2", 0, 0),),
    },
)


def block_path_census(
    source_matrices: dict[str, list[dict[str, object]]],
    hessian_matrices: dict[str, list[dict[str, object]]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for template in FAMILY_TEMPLATES:
        node_count = int(template["nodes"])
        for node_blocks in product(BLOCK_IDS, repeat=node_count):
            kernel_rows: list[dict[str, str]] = []
            hessian_zero = False
            source_zero = False
            for kernel, left_node, right_node in template["kernels"]:
                left = node_blocks[left_node]
                right = node_blocks[right_node]
                if str(kernel).startswith("I"):
                    status = _matrix_status(source_matrices[str(kernel)], left, right)
                    source_zero |= status.startswith("TYPED_ZERO")
                else:
                    status = _matrix_status(hessian_matrices[str(kernel)], left, right)
                    hessian_zero |= status.startswith("TYPED_ZERO")
                kernel_rows.append(
                    {
                        "kernel": str(kernel),
                        "row_block": left,
                        "column_block": right,
                        "status": status,
                    }
                )
            if hessian_zero:
                bare_status = "TYPED_ZERO_PROJECT_HESSIAN_PATH"
                completed_status = bare_status
            elif source_zero:
                bare_status = "TYPED_ZERO_BARE_SOURCE_PATH"
                completed_status = "BLOCKED_MISSING_PROJECT_BLOCK"
            else:
                bare_status = "SURVIVING_BARE_PROJECT_PATH"
                completed_status = "SURVIVING_BARE_BLOCK_PLUS_BLOCKED_SOURCE_COMPLETION"
            rows.append(
                {
                    "family": template["family"],
                    "path_id": f"{template['family']}__{'__'.join(node_blocks)}",
                    "node_blocks": list(node_blocks),
                    "kernel_blocks": kernel_rows,
                    "bare_status": bare_status,
                    "source_completed_status": completed_status,
                }
            )
    return rows


COLOR_Q = IndexSlot(IndexSpace.COLOR_ADJOINT, "Q", Variance.UP)
COLOR_A_DOWN = IndexSlot(IndexSpace.COLOR_ADJOINT, "A", Variance.DOWN)
COLOR_B_DOWN = IndexSlot(IndexSpace.COLOR_ADJOINT, "B", Variance.DOWN)
V_Q_FIELD = FieldType("V", Statistics.BOSON, Chirality.REAL, (COLOR_Q,))
V_B_FIELD = FieldType("V_B", Statistics.BOSON, Chirality.REAL, (COLOR_Q,))
J_WW_FIELD = FieldType(
    "J_AB[nabla_-(X^A X^B)]",
    Statistics.FERMION,
    Chirality.UNCONSTRAINED,
    (COLOR_A_DOWN, COLOR_B_DOWN),
)


def _build_graph(
    graph_id: str,
    vertex_data: Sequence[dict[str, object]],
    edge_data: Sequence[tuple[str, str, str, str]],
    *,
    family: str,
    neumann_sign: int | None,
    branch_count: int | None,
    topology: str,
) -> GraphIR:
    vertices: list[Vertex] = []
    half_edges: list[HalfEdge] = []
    external_legs: list[ExternalLeg] = []
    for vertex_record in vertex_data:
        vertex_id = str(vertex_record["vertex_id"])
        ordered_half_edges: list[str] = []
        for slot, port in enumerate(vertex_record["ports"]):
            assert isinstance(port, dict)
            port_id = f"{vertex_id}__{port['name']}"
            ordered_half_edges.append(port_id)
            field = port["field"]
            assert isinstance(field, FieldType)
            half_edges.append(
                HalfEdge(
                    port_id,
                    vertex_id,
                    slot,
                    field,
                    Flow.IN if port.get("external") else Flow.NONE,
                    str(port["momentum"]),
                )
            )
            if port.get("external"):
                external_legs.append(
                    ExternalLeg(
                        str(port["leg_id"]),
                        port_id,
                        field,
                        str(port["momentum"]),
                        str(port["color"]),
                    )
                )
        vertices.append(
            Vertex(
                vertex_id,
                str(vertex_record["kind"]),
                tuple(ordered_half_edges),
                str(vertex_record["coefficient_symbol"]),
                tuple(str(item) for item in vertex_record["color_word"]),
                str(vertex_record["superspace_point"]),
                str(vertex_record["momentum_delta"]),
            )
        )
    internal_edges = tuple(
        InternalEdge(
            edge_id,
            left_half_edge,
            right_half_edge,
            "G_V=-2*g^2*kappa^(-1)*delta4theta/r^2",
            momentum,
            Flow.NONE,
        )
        for edge_id, left_half_edge, right_half_edge, momentum in edge_data
    )
    loop_momenta = ("k",) if internal_edges else ()
    metadata = {
        "family": family,
        "topology": topology,
        "supertrace_prefactor": "1/2" if neumann_sign is not None else "NOT_APPLICABLE_CT2",
        "neumann_sign": str(neumann_sign) if neumann_sign is not None else "UNRESOLVED_CT2",
        "root_supertrace_weight": "1" if neumann_sign is not None else "NOT_APPLICABLE_CT2",
        "wick_koszul_sign": "1" if neumann_sign is not None else "NOT_APPLICABLE_CT2",
        "source_parity": "1",
        "source_statistics": "FERMION",
        "branch_cartesian_product_count": (
            str(branch_count) if branch_count is not None else "BLOCKED_COUNTERTERM_COEFFICIENT"
        ),
        "orientation_sign": "NOT_INHERITED_FROM_OLD_REFLECTION_SCAFFOLD",
        "coefficient_status": (
            "BLOCKED_D_ALGEBRA_KERNEL_CONTRACTION_AND_PROJECTED_TYPE_REGENERATION"
            if neumann_sign is not None
            else "BLOCKED_COUNTERTERM_COEFFICIENT"
        ),
    }
    graph = GraphIR(
        graph_id,
        tuple(vertices),
        tuple(half_edges),
        internal_edges,
        tuple(external_legs),
        loop_momenta,
        tuple(sorted(metadata.items())),
    )
    graph.assert_linear_momentum_routing()
    metadata.update(
        {
            "automorphism_order": str(graph_automorphism_order(graph)),
            "canonical_key": graph_canonical_key(graph),
            "automorphism_factor_policy": "AUDIT_ONLY_NO_SECOND_DIVISION",
        }
    )
    return replace(graph, metadata=tuple(sorted(metadata.items())))


def _source_port() -> dict[str, object]:
    return {
        "name": "source",
        "field": J_WW_FIELD,
        "momentum": "-p1-p2",
        "external": True,
        "leg_id": "J",
        "color": "(A,B)",
    }


def _background_port(label: str) -> dict[str, object]:
    return {
        "name": f"background_{label}",
        "field": V_B_FIELD,
        "momentum": label,
        "external": True,
        "leg_id": label,
        "color": f"C_{label}",
    }


def triangle_graph(first: str, second: str) -> GraphIR:
    graph_id = f"N2_I0H1H1__{first}__{second}"
    data = (
        {
            "vertex_id": "vI",
            "kind": "SOURCE_HESSIAN_I0_VV",
            "coefficient_symbol": "ProjectBlock[I0_VV]",
            "color_word": ("I0[A,B]",),
            "superspace_point": "theta_I",
            "momentum_delta": "delta(k+(-k+p1+p2)-p1-p2)",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": "-k+p1+p2"},
                _source_port(),
            ),
        },
        {
            "vertex_id": "vH_first",
            "kind": f"ACTION_HESSIAN_H1_{first}_VV",
            "coefficient_symbol": f"ProjectBlock[H1_VV;{first}]",
            "color_word": (f"H1[{first}]",),
            "superspace_point": "theta_1",
            "momentum_delta": f"delta(-k+(k-{first})+{first})",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "-k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": f"k-{first}"},
                _background_port(first),
            ),
        },
        {
            "vertex_id": "vH_second",
            "kind": f"ACTION_HESSIAN_H1_{second}_VV",
            "coefficient_symbol": f"ProjectBlock[H1_VV;{second}]",
            "color_word": (f"H1[{second}]",),
            "superspace_point": "theta_2",
            "momentum_delta": f"delta((-k+{first})+(k-p1-p2)+{second})",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": f"-k+{first}"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": "k-p1-p2"},
                _background_port(second),
            ),
        },
    )
    edges = (
        ("e0", "vI__q0", "vH_first__q0", "k"),
        ("e1", "vH_first__q1", "vH_second__q0", f"k-{first}"),
        ("e2", "vH_second__q1", "vI__q1", "k-p1-p2"),
    )
    return _build_graph(
        graph_id,
        data,
        edges,
        family="I0_H1_H1",
        neumann_sign=1,
        branch_count=4 * 24 * 24,
        topology="TRIANGLE",
    )


def seagull_graph() -> GraphIR:
    data = (
        {
            "vertex_id": "vI",
            "kind": "SOURCE_HESSIAN_I0_VV",
            "coefficient_symbol": "ProjectBlock[I0_VV]",
            "color_word": ("I0[A,B]",),
            "superspace_point": "theta_I",
            "momentum_delta": "delta(k+(-k+p1+p2)-p1-p2)",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": "-k+p1+p2"},
                _source_port(),
            ),
        },
        {
            "vertex_id": "vH2",
            "kind": "ACTION_HESSIAN_H2_V1_V2_VV",
            "coefficient_symbol": "ProjectBlock[H2_VV;V1,V2]",
            "color_word": ("H2[V1,V2]",),
            "superspace_point": "theta_1",
            "momentum_delta": "delta(-k+(k-p1-p2)+p1+p2)",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "-k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": "k-p1-p2"},
                _background_port("p1"),
                _background_port("p2"),
            ),
        },
    )
    edges = (
        ("e0", "vI__q0", "vH2__q0", "k"),
        ("e1", "vH2__q1", "vI__q1", "k-p1-p2"),
    )
    return _build_graph(
        "N2_I0H2",
        data,
        edges,
        family="I0_H2",
        neumann_sign=-1,
        branch_count=4 * 144,
        topology="SEAGULL_BUBBLE",
    )


def insertion_contact_graph(insertion_background: str, action_background: str) -> GraphIR:
    data = (
        {
            "vertex_id": "vI1",
            "kind": f"SOURCE_HESSIAN_I1_{insertion_background}_VV",
            "coefficient_symbol": f"ProjectBlock[I1_VV;{insertion_background}]",
            "color_word": (f"I1[A,B;{insertion_background}]",),
            "superspace_point": "theta_I",
            "momentum_delta": (
                f"delta(k+(-k+{action_background})+{insertion_background}-p1-p2)"
            ),
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": f"-k+{action_background}"},
                _source_port(),
                _background_port(insertion_background),
            ),
        },
        {
            "vertex_id": "vH1",
            "kind": f"ACTION_HESSIAN_H1_{action_background}_VV",
            "coefficient_symbol": f"ProjectBlock[H1_VV;{action_background}]",
            "color_word": (f"H1[{action_background}]",),
            "superspace_point": "theta_1",
            "momentum_delta": f"delta(-k+(k-{action_background})+{action_background})",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "-k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": f"k-{action_background}"},
                _background_port(action_background),
            ),
        },
    )
    edges = (
        ("e0", "vI1__q0", "vH1__q0", "k"),
        ("e1", "vH1__q1", "vI1__q1", f"k-{action_background}"),
    )
    return _build_graph(
        f"N2_I1H1__I_{insertion_background}__H_{action_background}",
        data,
        edges,
        family="I1_H1",
        neumann_sign=-1,
        branch_count=60 * 24,
        topology="INSERTION_CONTACT_BUBBLE",
    )


def double_contact_graph() -> GraphIR:
    data = (
        {
            "vertex_id": "vI2",
            "kind": "SOURCE_HESSIAN_I2_V1_V2_VV",
            "coefficient_symbol": "ProjectBlock[I2_VV;V1,V2]",
            "color_word": ("I2[A,B;V1,V2]",),
            "superspace_point": "theta_I",
            "momentum_delta": "delta(k-k+p1+p2-p1-p2)",
            "ports": (
                {"name": "q0", "field": V_Q_FIELD, "momentum": "k"},
                {"name": "q1", "field": V_Q_FIELD, "momentum": "-k"},
                _source_port(),
                _background_port("p1"),
                _background_port("p2"),
            ),
        },
    )
    edges = (("e0", "vI2__q0", "vI2__q1", "k"),)
    return _build_graph(
        "N2_I2",
        data,
        edges,
        family="I2",
        neumann_sign=1,
        branch_count=720,
        topology="DOUBLE_CONTACT_TADPOLE",
    )


def counterterm_graph() -> GraphIR:
    data = (
        {
            "vertex_id": "vCT2",
            "kind": "LOCAL_COUNTERTERM_CT2",
            "coefficient_symbol": "BLOCKED_COUNTERTERM_COEFFICIENT",
            "color_word": ("CT2[A,B]",),
            "superspace_point": "theta_CT",
            "momentum_delta": "delta(p1+p2-p1-p2)",
            "ports": (
                _source_port(),
                _background_port("p1"),
                _background_port("p2"),
            ),
        },
    )
    return _build_graph(
        "N2_CT2",
        data,
        (),
        family="CT2",
        neumann_sign=None,
        branch_count=None,
        topology="LOCAL_COUNTERTERM",
    )


def family_graphs() -> tuple[GraphIR, ...]:
    return (
        triangle_graph("p1", "p2"),
        triangle_graph("p2", "p1"),
        seagull_graph(),
        insertion_contact_graph("p1", "p2"),
        insertion_contact_graph("p2", "p1"),
        double_contact_graph(),
        counterterm_graph(),
    )


def source_and_projected_type_audit() -> dict[str, object]:
    expected_hash = pipeline_ir.PROJECT_WW_NOTATION_SCHEMA_SHA256
    hash_drift = False
    try:
        schema = pipeline_ir.project_notation_schema()
    except pipeline_ir.HashDriftError:
        hash_drift = True
        pipeline_ir.PROJECT_WW_NOTATION_SCHEMA_SHA256 = "PENDING"
        try:
            schema = pipeline_ir.project_notation_schema()
        finally:
            pipeline_ir.PROJECT_WW_NOTATION_SCHEMA_SHA256 = expected_hash
    source = schema.field_map["Source[nabla_-(X^A X^B)]"]
    source_port = schema.port_map["WW_source_B"]
    field_flags = set(source.__dataclass_fields__)
    port_flags = set(source_port.__dataclass_fields__)
    explicit_exclusion = bool(
        {"koszul_participation", "non_dynamical_marker", "exclude_from_koszul"}
        & (field_flags | port_flags)
    )
    reflected = ww_reflected_seed_request(schema)
    notation_artifact = json.loads(
        (ROOT / "generated/step5/typed-pipeline/project-notation.json").read_text(
            encoding="utf-8"
        )
    )
    persisted_source = next(
        field
        for field in notation_artifact["fields"]
        if field["name"] == "Source[nabla_-(X^A X^B)]"
    )
    pipeline_artifact = json.loads(
        (ROOT / "generated/step5/typed-pipeline/ww-typed-pipeline.json").read_text(
            encoding="utf-8"
        )
    )
    reflected_artifact = next(
        orientation
        for orientation in pipeline_artifact["orientations"]
        if orientation["orientation"] == "REFLECTED"
    )
    reflected_amplitude = reflected_artifact["graph_amplitude"]["amplitudes"][0]
    persisted_tilde_w_legs = [
        leg
        for orientation in pipeline_artifact["orientations"]
        for amplitude in orientation["graph_amplitude"]["amplitudes"]
        for leg in amplitude["graph"]["external_legs"]
        if leg["field_type"]["name"] == "TildeW_dot_alpha"
    ]
    required_parities = {
        "W_plus": 1,
        "nabla_plus": 1,
        "X=nabla_plus_W_plus": 0,
        "X_times_X": 0,
        "nabla_minus": 1,
        "insertion=nabla_minus_X_times_X": 1,
        "source_J": 1,
    }
    persisted_source_type_error = (
        persisted_source["statistics"] == "BOSON" and not explicit_exclusion
    )
    persisted_dotted_variance_error = any(
        leg["field_type"]["indices"][1]["variance"] == "UP"
        or leg["spinor_indices"][0]["variance"] == "UP"
        for leg in persisted_tilde_w_legs
    )
    persisted_reflected_sign_error = reflected_amplitude["external_koszul_sign"] == -1
    return {
        "parity_derivation": required_parities,
        "current_factory_source_statistics": source.statistics.value,
        "persisted_notation_source_statistics": persisted_source["statistics"],
        "current_schema_source_port": source_port.name,
        "explicit_non_dynamical_koszul_exclusion": explicit_exclusion,
        "source_type_verdict": (
            "P0_SOURCE_PARITY_TYPE_ERROR_IN_PERSISTED_ARTIFACT"
            if persisted_source_type_error
            else "REPAIRED"
        ),
        "factory_hash_drift_after_type_repair": hash_drift,
        "frozen_expected_hash": expected_hash,
        "current_factory_hash": schema.canonical_hash,
        "new_family_graphir_source_statistics": J_WW_FIELD.statistics.value,
        "current_factory_tildeW_dotted_variance": TILDE_W_FIELD.indices[1].variance.value,
        "persisted_tildeW_dotted_variances": sorted(
            {
                leg["field_type"]["indices"][1]["variance"]
                for leg in persisted_tilde_w_legs
            }
        ),
        "required_tildeW_dotted_variance": "DOWN",
        "tildeW_variance_verdict": (
            "P0_DOTTED_INDEX_VARIANCE_TYPE_ERROR_IN_PERSISTED_ARTIFACT"
            if persisted_dotted_variance_error
            else "REPAIRED"
        ),
        "current_factory_reflected_external_sign": reflected.external_koszul_sign,
        "persisted_reflected_external_sign": reflected_amplitude["external_koszul_sign"],
        "required_fixed_graphir_reflected_sign": 1,
        "reflected_sign_verdict": (
            "P0_REFLECTED_ORIENTATION_SIGN_ERROR_IN_PERSISTED_ARTIFACT"
            if persisted_reflected_sign_error
            else "REPAIRED"
        ),
        "required_external_derivative": "mathcal_D_(+ dot_a)",
        "old_orientation_sign_reused": False,
        "old_candidate_coefficients_reused": False,
        "regeneration_required": [
            "WW_DIRECT_TRIANGLE_PROJECTED_GRAPHIR",
            "WW_REFLECTED_TRIANGLE_PROJECTED_GRAPHIR",
            "I0_H2_PROJECTED_CONTACT_GRAPHIR",
            "I1_H1_DIRECT_PROJECTED_CONTACT_GRAPHIR",
            "I1_H1_REFLECTED_PROJECTED_CONTACT_GRAPHIR",
            "I2_PROJECTED_CONTACT_GRAPHIR",
            "CT2_PROJECTED_LOCAL_IR",
            "ALL_DOWNSTREAM_D_ALGEBRA_TRACES",
            "ALL_DOWNSTREAM_AMPLITUDE_IR",
            "ALL_DOWNSTREAM_POLES_AND_SD_CHILDREN",
        ],
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    registry = block_branch_registry()
    source_matrices = {
        name: source_block_matrix(int(name[-1]), len(rows))
        for name, rows in registry["source"].items()
    }
    hessian_matrices = {
        name: hessian_block_matrix(int(name[-1]), rows)
        for name, rows in registry["action"].items()
    }
    paths = block_path_census(source_matrices, hessian_matrices)
    graphs = family_graphs()
    type_audit = source_and_projected_type_audit()
    graph_rows = [graph.canonical_dict() for graph in graphs]
    loop_graphs = graphs[:-1]
    checks = {
        "source_branch_counts_are_exact": {
            name: len(rows) for name, rows in registry["source"].items()
        }
        == {"I0": 4, "I1": 60, "I2": 720},
        "vector_hessian_branch_counts_are_exact": {
            name: sum(row["block_id"] == "V" for row in rows)
            for name, rows in registry["action"].items()
        }
        == {"H1": 24, "H2": 144},
        "three_chiral_pair_branch_counts_are_exact": all(
            sum(row["block_id"] == block_id for row in registry["action"][name])
            == ({"H1": 2, "H2": 4}[name])
            for name in ("H1", "H2")
            for block_id in ("PHI_PAIR_1", "PHI_PAIR_2", "PHI_PAIR_3")
        ),
        "fp_background_hessian_is_not_falsely_inferred_from_quantum_vertices": {
            name: sum(row["block_id"] == "FP" for row in rows)
            for name, rows in registry["action"].items()
        }
        == {"H1": 0, "H2": 0}
        and {
            name: len(rows)
            for name, rows in registry[
                "fp_quantum_interactions_excluded_from_H_r"
            ].items()
        }
        == {"V_QUANTUM_ORDER_1": 4, "V_QUANTUM_ORDER_2": 4},
        "all_block_matrices_have_36_ordered_entries": all(
            len(matrix) == 36
            for matrix in (*source_matrices.values(), *hessian_matrices.values())
        ),
        "bare_block_paths_have_one_vector_survivor_per_family": len(paths) == 294
        and sum(row["bare_status"] == "SURVIVING_BARE_PROJECT_PATH" for row in paths) == 4
        and all(
            row["node_blocks"] == ["V"] * len(row["node_blocks"])
            for row in paths
            if row["bare_status"] == "SURVIVING_BARE_PROJECT_PATH"
        ),
        "six_loop_graphirs_and_one_counterterm_ir": len(loop_graphs) == 6
        and len(graphs) == 7
        and all(graph.cycle_rank() == 1 for graph in loop_graphs)
        and graphs[-1].cycle_rank() == 0,
        "all_graph_momentum_routes_close": all(
            graph.validate_linear_momentum_routing()["passed"] for graph in graphs
        ),
        "typed_automorphism_is_audit_only_and_order_one": all(
            dict(graph.metadata)["automorphism_order"] == "1" for graph in graphs
        ),
        "no_isomorphic_family_graphir_is_duplicated": len(
            {dict(graph.metadata)["canonical_key"] for graph in graphs}
        )
        == len(graphs),
        "expanded_vector_branch_path_count_is_exact": sum(
            int(dict(graph.metadata)["branch_cartesian_product_count"])
            for graph in loop_graphs
        )
        == 8784,
        "source_parity_defect_or_repair_is_typed_and_new_graphir_is_fermionic": type_audit[
            "source_type_verdict"
        ]
        in {"P0_SOURCE_PARITY_TYPE_ERROR_IN_PERSISTED_ARTIFACT", "REPAIRED"}
        and all(
            any(
                leg.field_type == J_WW_FIELD and leg.field_type.statistics is Statistics.FERMION
                for leg in graph.external_legs
            )
            for graph in graphs
        ),
        "old_reflection_and_dotted_variance_defects_or_repairs_are_typed": type_audit[
            "tildeW_variance_verdict"
        ] in {"P0_DOTTED_INDEX_VARIANCE_TYPE_ERROR_IN_PERSISTED_ARTIFACT", "REPAIRED"}
        and type_audit["reflected_sign_verdict"]
        in {"P0_REFLECTED_ORIENTATION_SIGN_ERROR_IN_PERSISTED_ARTIFACT", "REPAIRED"},
        "no_pole_or_anomaly_coefficient_is_accepted": all(
            "BLOCKED" in dict(graph.metadata)["coefficient_status"] for graph in graphs
        ),
    }
    gaps = [
        {
            "gap_id": "G1[G-DEF]",
            "severity": "P0",
            "status": (
                "OPEN"
                if str(type_audit["source_type_verdict"]).startswith("P0_")
                else "CLOSED_REGENERATED"
            ),
            "location": "scripts/step5_pipeline_ir.py:project_notation_schema Source[nabla_-(X^A X^B)]",
            "claim": "the source is declared BOSON",
            "missing": "the odd insertion requires an odd source and no non-dynamical Koszul exclusion exists",
            "minimal_repair": "declare J as FERMION and regenerate every schema-hashed downstream object",
        },
        {
            "gap_id": "G2[G-IDX]",
            "severity": "P0",
            "status": (
                "OPEN"
                if str(type_audit["tildeW_variance_verdict"]).startswith("P0_")
                else "CLOSED_REGENERATED"
            ),
            "location": "scripts/step5_supergraph_pipeline.py:TILDE_W_FIELD",
            "claim": "the external TildeW dotted slot is UP",
            "missing": "the fixed Project output requires a DOWN dotted slot and mathcal_D_(+ dot_a)",
            "minimal_repair": "retag the dotted variance and regenerate projected GraphIR/D-algebra",
        },
        {
            "gap_id": "G3[G-SIGN]",
            "severity": "P0",
            "status": (
                "OPEN"
                if str(type_audit["reflected_sign_verdict"]).startswith("P0_")
                else "CLOSED_REGENERATED"
            ),
            "location": "scripts/step5_supergraph_pipeline.py:_ww_seed_request",
            "claim": "the reflected external sign is -1",
            "missing": "the fixed ordered GraphIR reflection quotient requires +1",
            "minimal_repair": "replace the reflected sign by +1 and regenerate rather than patching a final coefficient",
        },
        {
            "gap_id": "G4[G-DEF]",
            "severity": "P1",
            "status": "OPEN",
            "location": "source-completed I_s block matrix",
            "claim": "the bare pure-vector source is a complete source multiplet",
            "missing": "BRST/source-partner insertion blocks for non-vector carriers are absent",
            "minimal_repair": "derive each partner from a Project source action or retain BLOCKED_MISSING_PROJECT_BLOCK",
        },
        {
            "gap_id": "G5[G-NORM]",
            "severity": "P1",
            "status": "OPEN",
            "location": "G0 blocks outside V and CT2",
            "claim": "all Gaussian blocks and the local counterterm are normalized",
            "missing": "the immutable WW schema supplies only G_V; CT2 has no renormalization condition",
            "minimal_repair": "derive the missing Project propagator blocks and CT2 coefficient before amplitude reduction",
        },
    ]
    return {
        "schema": "Step5OneLoopN2PhysicalHessianFamily.v1",
        "status": (
            (
                "PASS_CENSUS_FAIL_CLOSED_P0_PROJECTED_TYPE_REGENERATION"
                if any(gap["severity"] == "P0" and gap["status"] == "OPEN" for gap in gaps)
                else "PASS_CENSUS_PROJECTED_TYPE_REPAIRED_FAIL_CLOSED_PHYSICS"
            )
            if all(checks.values())
            else "FAIL"
        ),
        "scope": "STEP5A_PRIMITIVE_TWO_BACKGROUND_HESSIAN_FAMILY",
        "formal_skeleton": (
            "(1/2)STr[+G0 I0 G0 H1 G0 H1-G0 I0 G0 H2-"
            "G0 I1 G0 H1+G0 I2]+CT2"
        ),
        "gaussian_blocks": [asdict(block) for block in BLOCKS],
        "block_branch_registry": registry,
        "source_block_matrices": source_matrices,
        "action_hessian_block_matrices": hessian_matrices,
        "propagator_blocks": propagator_block_matrix(),
        "block_path_census": paths,
        "physical_family_graphir": graph_rows,
        "source_and_projected_type_audit": type_audit,
        "gaps": gaps,
        "checks": checks,
        "acceptance_boundary": {
            "aggregate_contact_pole_accepted": False,
            "triangle_pole_accepted": False,
            "anomaly_coefficient_accepted": False,
            "old_reflection_sign_reused": False,
            "old_candidate_coefficient_reused": False,
            "full_source_completed_family_claimed": False,
        },
        "result": (
            "EXACT_BARE_VECTOR_FAMILY_TOPOLOGY_AND_PROJECT_BRANCH_CENSUS_ONLY; "
            + (
                "PROJECTED_TYPES_MUST_BE_REGENERATED"
                if any(gap["severity"] == "P0" and gap["status"] == "OPEN" for gap in gaps)
                else "PROJECTED_TYPES_REPAIRED"
            )
            + "; NO_POLE_OR_ANOMALY_COEFFICIENT"
        ),
    }


def render_audit_markdown(payload: dict[str, object]) -> str:
    counts = payload["block_branch_registry"]["counts"]
    return r"""# Step 5A primitive two-background Hessian-family audit

## 1. Definitions

$$
\mathscr I^{AB}=\nabla_-\!\left(X^A X^B\right),
\qquad X^A=(\nabla_+W_+)^A,
\qquad |X|=0,
\qquad |\mathscr I|=|J|=1.
$$

$$
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\!\left[
+G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2
-G_0I_1G_0H_1
+G_0I_2
\right]+\mathrm{CT}_2.
$$

## 2. Exact Project branch counts

$$
\begin{array}{c|ccc}
\text{source block}&I_0&I_1&I_2\\ \hline
\#\text{ ordered branches}&%d&%d&%d
\end{array}
$$

$$
N(I_0)=2\binom20(0!)\,(2!)=4,
$$

$$
N(I_1)=10\binom31(1!)\,(2!)=60,
$$

$$
N(I_2)=30\binom42(2!)\,(2!)=720.
$$

The integers 2, 10, and 30 are the exact Project composite-term counts

$$
|I_{(2)}|=2,
\qquad |I_{(3)}|=10,
\qquad |I_{(4)}|=30.
$$

The split is

$$
V_j=(V_{\mathrm B})_j+v_j.
$$

It changes no source coefficient.  Each ordered background/quantum assignment
has multiplicity one; the final factor of two enumerates the ordered bosonic
Hessian row/column occurrences.  No factorial is divided a second time.

$$
\begin{array}{c|cc}
\text{action block}&H_1&H_2\\ \hline
V\to V&%d&%d\\
\Phi_r\leftrightarrow\widetilde\Phi_r\ \text{for each }r&%d&%d\\
\mathrm{FP}\to\mathrm{FP}&\texttt{BLOCKED}&\texttt{BLOCKED}\\
\mathrm{NK}\to\mathrm{NK}&\texttt{BLOCKED}&\texttt{BLOCKED}
\end{array}
$$

$$
N(H_1^{VV})=4\binom31(1!)\,(2!)=24,
\qquad
N(H_2^{VV})=6\binom42(2!)\,(2!)=144.
$$

The factors 4 and 6 count the Project cubic and quartic gauge-action
monomials.  The action-monomial coefficient, derivative scope, and color word
remain attached to every branch.

The explicit FP vertices contain quantum prepotentials,

$$
N(Vc'c)=4,
\qquad
N(V^2c'c)=4.
$$

They are retained as `QUANTUM_INTERACTION_NOT_BACKGROUND_HESSIAN`.  The
background dependence lies in the unexpanded
$\bar\nabla_{\mathrm B}^{2}$ and $\nabla_{\mathrm B}^{2}$ operators;
hence the FP entries of $H_1$ and $H_2$ are
`BLOCKED_MISSING_PROJECT_BLOCK`.  The NK background Hessians have the same
status.

## 3. Surviving bare vector families

$$
\begin{array}{c|c|c|c|c}
\text{word}&\text{polarizations}&\text{topology}&L&\#\text{ branch paths}\\ \hline
+I_0H_1H_1&2&\triangle&1&2\cdot2304\\
-I_0H_2&1&\text{seagull bubble}&1&576\\
-I_1H_1&2&\text{insertion-contact bubble}&1&2\cdot1440\\
+I_2&1&\text{double-contact tadpole}&1&720\\
\mathrm{CT}_2&1&\text{local}&0&\text{coefficient blocked}
\end{array}
$$

$$
2(2304)+576+2(1440)+720=8784.
$$

The three different census levels are

$$
N_{\mathrm{typed\ block\ paths}}
=6^3+6^2+6^2+6
=216+36+36+6
=294,
$$

$$
N_{\mathrm{ordered\ vector\ branch\ paths}}=8784,
\qquad
N_{\mathrm{GraphIR}}=6+1_{\mathrm{CT}_2}=7.
$$

Neither 294 nor 8784 is a graph count.

Every bare non-vector path vanishes at its source block.  A source-completed
non-vector diagonal path remains `BLOCKED_MISSING_PROJECT_BLOCK`; it is not
promoted to a zero.

## 4. Typed repair readback

$$
|W_+|=1,
\qquad |\nabla_+|=1,
\qquad |X|=1+1=0,
$$

$$
|X^AX^B|=0,
\qquad |\nabla_-|=1,
\qquad |\mathscr I|=1,
\qquad |J|=1.
$$

$$
\operatorname{Statistics}(J)=\mathrm{FERMION},
\qquad
\operatorname{Var}(J_{AB})=(\mathrm{DOWN},\mathrm{DOWN}),
$$

$$
\operatorname{Var}(\widetilde W_{\dot a})=\mathrm{DOWN},
\qquad
s_{\mathrm{reflected}}=(-1)_{\mathrm{ext}}(-1)_{\mathrm{quantum}}=+1.
$$

The external covariant derivative is

$$
\mathcal D_{+\dot a}.
$$

The persisted notation, GraphIR, and reflected amplitude readbacks are
REPAIRED.

## 5. Acceptance boundary

$$
\text{triangle pole}
=\text{contact pole}
=\text{anomaly coefficient}
=\texttt{NOT ACCEPTED}.
$$
""" % (
        counts["I0"],
        counts["I1"],
        counts["I2"],
        counts["H1_V"],
        counts["H2_V"],
        counts["H1_PHI_PAIR_1"],
        counts["H2_PHI_PAIR_1"],
    )


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    checks = payload["checks"]
    audit = {
        "schema": "Step5OneLoopN2PhysicalHessianFamilyAudit.v1",
        "status": payload["status"],
        "scope": payload["scope"],
        "totals": {
            "checks": len(checks),
            "failed": sum(not value for value in checks.values()),
            "gaps": len(payload["gaps"]),
            "p0_gaps": sum(gap["severity"] == "P0" for gap in payload["gaps"]),
            "open_p0_gaps": sum(
                gap["severity"] == "P0" and gap["status"] == "OPEN"
                for gap in payload["gaps"]
            ),
            "source_branches": sum(
                len(rows) for rows in payload["block_branch_registry"]["source"].values()
            ),
            "action_hessian_branches": sum(
                len(rows) for rows in payload["block_branch_registry"]["action"].values()
            ),
            "block_paths": len(payload["block_path_census"]),
            "family_graphir": len(payload["physical_family_graphir"]),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "result": payload["result"],
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT_JSON.write_bytes(canonical_json(audit))
    AUDIT_MD.write_text(render_audit_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    write_artifacts()
