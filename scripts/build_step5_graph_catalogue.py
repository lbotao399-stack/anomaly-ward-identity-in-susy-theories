#!/usr/bin/env python3
"""Build the deterministic Step-5 tree/draw-map candidate catalogue.

Loop entries are topology requests until field-compatible Wick kernels, the
Euler-core expansion, and regulated cycles are locked.  Only explicitly
generic topology fixtures instantiate GraphIR, and none carries physical
channel or admitted-amplitude semantics.
"""

from __future__ import annotations

from dataclasses import replace
import hashlib
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sys
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (
    Chirality,
    DerivativeKind,
    DerivativeLedgerEntry,
    DerivativeToken,
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
    emit_ordered_family_channels,
)
from scripts.step5_vertex_grammar import (
    ActionMonomial,
    ExactCoefficient,
    VertexGrammarBundle,
    build_project_vertex_grammar,
)


GENERATED = ROOT / "generated" / "step5"
CATALOGUE_PATH = GENERATED / "graph-catalogue.json"
MAPS_PATH = GENERATED / "graph-maps.md"
AUDIT_PATH = ROOT / "audits" / "step5-graph-catalogue-verification.json"
CONTRACT_PATH = ROOT / "contracts" / "foundations" / "step-05-euclidean-n4-awi-supergraphs.md"
GRAPH_IR_SOURCE = ROOT / "scripts" / "step5_graph_ir.py"
VERTEX_GRAMMAR_SOURCE = ROOT / "scripts" / "step5_vertex_grammar.py"

LOOP_BLOCKERS = (
    "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
    "BLOCKED_GAUGE_FIXED_DENSITY_BEREZINIAN",
    "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
    "BLOCKED_FP_GHOST_CYCLE_UNDECLARED",
    "BLOCKED_NK_BRANCH_AND_KERNEL_UNFIXED",
    "BLOCKED_UNINSTANTIATED_E_XI_CORE",
    "BLOCKED_COMPOSITE_DESCENDANT_INSERTION_UNINSTANTIATED",
    "BLOCKED_EDGE_TAGGED_PROJECTOR_DALGEBRA_TRACE",
)


def _coefficient_dict(coefficient: ExactCoefficient) -> dict[str, object]:
    return {
        "numerator": coefficient.rational.numerator,
        "denominator": coefficient.rational.denominator,
        "sqrt2_power": coefficient.sqrt2_power,
        "i_power": coefficient.i_power,
        "symbols": list(coefficient.symbols),
        "rendered": coefficient.render(),
    }


def _canonical_payload_sha256(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _monomial_manifest(monomial: ActionMonomial) -> dict[str, object]:
    return {
        "monomial_id": monomial.monomial_id,
        "sector": monomial.sector,
        "measure": monomial.measure,
        "valence": len(monomial.ordered_fields),
        "coefficient": _coefficient_dict(monomial.coefficient),
        "ordered_fields": [
            {
                "occurrence_id": field.occurrence_id,
                "field_name": field.field_name,
                "statistics": field.statistics.value,
                "chirality": field.chirality.value,
                "color_label": field.color_label,
                "flavor_label": field.flavor_label,
                "spinor_label": field.spinor_label,
                "direct_derivatives": list(field.direct_derivatives),
            }
            for field in monomial.ordered_fields
        ],
        "color_word": list(monomial.color_word),
        "derivative_scopes": [
            {
                "scope_id": scope.scope_id,
                "operators": list(scope.operators),
                "ordered_occurrence_ids": list(scope.ordered_occurrence_ids),
            }
            for scope in monomial.derivative_scopes
        ],
        "spinor_contractions": [
            {
                "index_space": contraction.index_space.value,
                "left_label": contraction.left_label,
                "left_variance": contraction.left_variance.value,
                "right_label": contraction.right_label,
                "right_variance": contraction.right_variance.value,
                "pairing": contraction.pairing,
            }
            for contraction in monomial.spinor_contractions
        ],
        "source_equations": list(monomial.source_equations),
    }


def _typed_tensor_label(tensor: Mapping[str, object]) -> str:
    slots = ",".join(
        f'{index["label"]}:{index["space"]}:{index["variance"]}'
        for index in tensor["ordered_indices"]  # type: ignore[index]
    )
    bindings = ",".join(
        f'{binding["tensor_slot"]}->{binding["node_path"]}:{binding["role"]}'
        for binding in tensor["bindings"]  # type: ignore[index]
    )
    return f'{tensor["symbol"]}[{slots}]{{{bindings}}}'


def _tree_ast_mermaid(ast: Mapping[str, object], prefix: str) -> str:
    lines = ["graph TD", f'  {prefix}_root["{ast["channel_id"]}"]']
    node_counter = 0

    def visit_node(node: Mapping[str, object], parent: str) -> None:
        nonlocal node_counter
        node_counter += 1
        node_id = f"{prefix}_n{node_counter}"
        indices = ",".join(
            f'{index["label"]}:{index["variance"]}' for index in node["indices"]  # type: ignore[index]
        )
        label = f'{node["node_type"]}:{node["token"]}[{indices}]'
        if node["tensor_factor"] is not None:
            label += "|" + _typed_tensor_label(node["tensor_factor"])
        lines.append(f'  {node_id}["{label}"]')
        lines.append(f"  {parent} --> {node_id}")
        for child in node["children"]:  # type: ignore[index]
            visit_node(child, node_id)

    for term_position, term in enumerate(ast["terms"]):  # type: ignore[index]
        coefficient = term["total_coefficient"]
        coefficient_label = (
            f'{coefficient["numerator"]}/{coefficient["denominator"]};'
            f'sqrt2^{coefficient["sqrt2_power"]};i^{coefficient["i_power"]};'
            f'K={term["koszul_sign"]}'
        )
        term_id = f"{prefix}_term{term_position}"
        lines.append(f'  {term_id}["{coefficient_label}"]')
        lines.append(f"  {prefix}_root --> {term_id}")
        for factor in term["ordered_factors"]:
            visit_node(factor, term_id)
        for tensor_position, tensor in enumerate(term["tensor_factors"]):
            tensor_id = f"{term_id}_tensor{tensor_position}"
            lines.append(f'  {tensor_id}["{_typed_tensor_label(tensor)}"]')
            lines.append(f"  {term_id} --> {tensor_id}")
    if ast["is_zero"]:
        lines.append(f'  {prefix}_zero["EXACT_ZERO_TREE_AST"]')
        lines.append(f"  {prefix}_root --> {prefix}_zero")
    return "\n".join(lines) + "\n"


def _tree_ast_dot(ast: Mapping[str, object], prefix: str) -> str:
    lines = [f'digraph "{prefix}" {{', f'  "{prefix}_root" [label="{ast["channel_id"]}"];']
    node_counter = 0

    def visit_node(node: Mapping[str, object], parent: str) -> None:
        nonlocal node_counter
        node_counter += 1
        node_id = f"{prefix}_n{node_counter}"
        indices = ",".join(index["label"] for index in node["indices"])  # type: ignore[index]
        label = f'{node["node_type"]}:{node["token"]}[{indices}]'
        if node["tensor_factor"] is not None:
            label += "|" + _typed_tensor_label(node["tensor_factor"])
        lines.append(f'  "{node_id}" [label="{label}"];')
        lines.append(f'  "{parent}" -> "{node_id}";')
        for child in node["children"]:  # type: ignore[index]
            visit_node(child, node_id)

    for term_position, term in enumerate(ast["terms"]):  # type: ignore[index]
        term_id = f"{prefix}_term{term_position}"
        coefficient = term["total_coefficient"]
        label = (
            f'{coefficient["numerator"]}/{coefficient["denominator"]};'
            f'K={term["koszul_sign"]}'
        )
        lines.append(f'  "{term_id}" [shape=box,label="{label}"];')
        lines.append(f'  "{prefix}_root" -> "{term_id}";')
        for factor in term["ordered_factors"]:
            visit_node(factor, term_id)
        for tensor_position, tensor in enumerate(term["tensor_factors"]):
            tensor_id = f"{term_id}_tensor{tensor_position}"
            lines.append(
                f'  "{tensor_id}" [shape=diamond,label="{_typed_tensor_label(tensor)}"];'
            )
            lines.append(f'  "{term_id}" -> "{tensor_id}";')
    if ast["is_zero"]:
        lines.append(f'  "{prefix}_zero" [label="EXACT_ZERO_TREE_AST"];')
        lines.append(f'  "{prefix}_root" -> "{prefix}_zero";')
    lines.append("}")
    return "\n".join(lines) + "\n"


def _valence_only_templates(bundle: VertexGrammarBundle) -> tuple[dict[str, object], ...]:
    actions = tuple(sorted(bundle.action_monomials, key=lambda item: item.monomial_id))
    insertions = tuple(sorted(bundle.insertion_monomials, key=lambda item: item.monomial_id))
    templates: list[dict[str, object]] = []

    for insertion in insertions:
        insertion_valence = len(insertion.ordered_fields)
        if insertion_valence == 4:
            templates.append(
                {
                    "template_id": f"tadpole__{insertion.monomial_id}",
                    "classification": "VALENCE_ONLY_NOT_GRAPH",
                    "topology": "TADPOLE",
                    "orientation": "CYCLIC",
                    "insertion_monomial_id": insertion.monomial_id,
                    "action_monomial_ids": [],
                    "vertex_count": 1,
                    "internal_edge_count": 1,
                    "external_leg_count": 2,
                    "loop_number": 1,
                    "reflection_template_id": f"tadpole__{insertion.monomial_id}",
                }
            )

        for action in actions:
            if insertion_valence + len(action.ordered_fields) != 6:
                continue
            template_id = f"bubble__{insertion.monomial_id}__{action.monomial_id}"
            templates.append(
                {
                    "template_id": template_id,
                    "classification": "VALENCE_ONLY_NOT_GRAPH",
                    "topology": "BUBBLE",
                    "orientation": "DIRECT",
                    "insertion_monomial_id": insertion.monomial_id,
                    "action_monomial_ids": [action.monomial_id],
                    "vertex_count": 2,
                    "internal_edge_count": 2,
                    "external_leg_count": 2,
                    "loop_number": 1,
                    "reflection_template_id": template_id,
                }
            )

        for left_action, right_action in combinations_with_replacement(actions, 2):
            if (
                insertion_valence
                + len(left_action.ordered_fields)
                + len(right_action.ordered_fields)
                != 8
            ):
                continue
            base = (
                f"triangle__{insertion.monomial_id}__"
                f"{left_action.monomial_id}__{right_action.monomial_id}"
            )
            direct_id = f"{base}__direct"
            reflected_id = f"{base}__reflected"
            common = {
                "classification": "VALENCE_ONLY_NOT_GRAPH",
                "topology": "TRIANGLE",
                "insertion_monomial_id": insertion.monomial_id,
                "vertex_count": 3,
                "internal_edge_count": 3,
                "external_leg_count": 2,
                "loop_number": 1,
            }
            templates.append(
                {
                    **common,
                    "template_id": direct_id,
                    "orientation": "DIRECT",
                    "action_monomial_ids": [left_action.monomial_id, right_action.monomial_id],
                    "reflection_template_id": reflected_id,
                }
            )
            templates.append(
                {
                    **common,
                    "template_id": reflected_id,
                    "orientation": "REFLECTED",
                    "action_monomial_ids": [right_action.monomial_id, left_action.monomial_id],
                    "reflection_template_id": direct_id,
                }
            )
    templates.sort(key=lambda item: item["template_id"])
    return tuple(templates)


def _ordinary_mermaid(graph: GraphIR) -> str:
    half_edges = {half_edge.half_edge_id: half_edge for half_edge in graph.half_edges}
    lines = ["graph LR"]
    for vertex in graph.vertices:
        lines.append(f'  {vertex.vertex_id}["{vertex.vertex_id}:{vertex.kind}"]')
    for leg in graph.external_legs:
        external_id = f"X_{leg.leg_id}"
        lines.append(f'  {external_id}["{leg.leg_id}:{leg.momentum}"]')
        lines.append(f"  {external_id} --> {half_edges[leg.attached_half_edge].vertex_id}")
    for edge in graph.internal_edges:
        left = half_edges[edge.left_half_edge].vertex_id
        right = half_edges[edge.right_half_edge].vertex_id
        lines.append(f'  {left} -->|"{edge.edge_id}:{edge.momentum}"| {right}')
    return "\n".join(lines) + "\n"


def _ordinary_dot(graph: GraphIR) -> str:
    half_edges = {half_edge.half_edge_id: half_edge for half_edge in graph.half_edges}
    lines = [f'digraph "ordinary__{graph.graph_id}" {{']
    for vertex in graph.vertices:
        lines.append(f'  "{vertex.vertex_id}" [label="{vertex.vertex_id}:{vertex.kind}"];')
    for leg in graph.external_legs:
        external_id = f"X_{leg.leg_id}"
        vertex_id = half_edges[leg.attached_half_edge].vertex_id
        lines.append(f'  "{external_id}" [shape=box,label="{leg.leg_id}:{leg.momentum}"];')
        lines.append(f'  "{external_id}" -> "{vertex_id}";')
    for edge in graph.internal_edges:
        left = half_edges[edge.left_half_edge].vertex_id
        right = half_edges[edge.right_half_edge].vertex_id
        lines.append(f'  "{left}" -> "{right}" [label="{edge.edge_id}:{edge.momentum}"];')
    lines.append("}")
    return "\n".join(lines) + "\n"


def _graph_inventory(graph: GraphIR) -> dict[str, list[str]]:
    return {
        "vertex_ids": [vertex.vertex_id for vertex in graph.vertices],
        "internal_edge_ids": [edge.edge_id for edge in graph.internal_edges],
        "external_leg_ids": [leg.leg_id for leg in graph.external_legs],
    }


def _ledger_dict(entry: DerivativeLedgerEntry) -> dict[str, object]:
    return {
        "step_id": entry.step_id,
        "op_id": entry.derivative.op_id,
        "kind": entry.derivative.kind.value,
        "index": entry.derivative.index.label,
        "origin": entry.derivative.origin,
        "from_factor": entry.from_factor,
        "to_factor": entry.to_factor,
        "external_leg_id": entry.external_leg_id,
        "koszul_sign": entry.koszul_sign,
    }


def _generic_triangle_fixture(
    orientation: str,
    insertion: ActionMonomial,
    action_left: ActionMonomial,
    action_right: ActionMonomial,
) -> tuple[GraphIR, tuple[DerivativeLedgerEntry, ...]]:
    vector = FieldType("V_UNRESOLVED", Statistics.BOSON, Chirality.REAL)
    outgoing_field = FieldType(
        "OUTGOING_FIELD_UNRESOLVED",
        Statistics.BOSON,
        Chirality.UNCONSTRAINED,
    )
    if orientation == "DIRECT":
        first_action, second_action = action_left, action_right
        edge_data = (
            ("eI1", "i0", "a10", "k0"),
            ("e12", "a11", "a20", "k0-p1"),
            ("e2I", "a21", "i1", "k0-p1-p2"),
        )
        momentum_by_half_edge = {
            "i0": "k0",
            "i1": "-k0+p1+p2",
            "a10": "-k0",
            "a11": "k0-p1",
            "a20": "-k0+p1",
            "a21": "k0-p1-p2",
        }
    elif orientation == "REFLECTED":
        first_action, second_action = action_right, action_left
        edge_data = (
            ("eI2", "i1", "a20", "k0"),
            ("e21", "a21", "a10", "k0-p2"),
            ("e1I", "a11", "i0", "k0-p1-p2"),
        )
        momentum_by_half_edge = {
            "i0": "-k0+p1+p2",
            "i1": "k0",
            "a10": "-k0+p2",
            "a11": "k0-p1-p2",
            "a20": "-k0",
            "a21": "k0-p2",
        }
    else:
        raise ValueError(orientation)
    graph_id = f"generic_blocked_triangle_fixture__{orientation.lower()}"
    half_edges = (
        HalfEdge("i0", "I", 0, vector, Flow.OUT, momentum_by_half_edge["i0"]),
        HalfEdge("i1", "I", 1, vector, Flow.IN, momentum_by_half_edge["i1"]),
        HalfEdge("a10", "A1", 0, vector, Flow.IN, momentum_by_half_edge["a10"]),
        HalfEdge("a11", "A1", 1, vector, Flow.OUT, momentum_by_half_edge["a11"]),
        HalfEdge("a1x", "A1", 2, outgoing_field, Flow.OUT, "p1"),
        HalfEdge("a20", "A2", 0, vector, Flow.IN, momentum_by_half_edge["a20"]),
        HalfEdge("a21", "A2", 1, vector, Flow.OUT, momentum_by_half_edge["a21"]),
        HalfEdge("a2x", "A2", 2, outgoing_field, Flow.OUT, "p2"),
    )
    graph = GraphIR(
        graph_id,
        (
            Vertex(
                "I",
                "EULER_CHART_TRANSPORT_FIXTURE",
                ("i0", "i1"),
                insertion.coefficient.render(),
                insertion.color_word,
                "zI",
                "qI+p1+p2",
                momentum_injection="-p1-p2",
            ),
            Vertex(
                "A1",
                "ACTION_CANDIDATE",
                ("a10", "a11", "a1x"),
                first_action.coefficient.render(),
                first_action.color_word,
                "z1",
                "q1+p1",
            ),
            Vertex(
                "A2",
                "ACTION_CANDIDATE",
                ("a20", "a21", "a2x"),
                second_action.coefficient.render(),
                second_action.color_word,
                "z2",
                "q2+p2",
            ),
        ),
        half_edges,
        tuple(
            InternalEdge(edge_id, left, right, "BLOCKED_VECTOR_WICK_KERNEL", momentum, Flow.OUT)
            for edge_id, left, right, momentum in edge_data
        ),
        (
            ExternalLeg("OUT_D", "a1x", outgoing_field, "p1", "D"),
            ExternalLeg("OUT_E", "a2x", outgoing_field, "p2", "E"),
        ),
        ("k0",),
        tuple(
            sorted(
                {
                    "candidate_status": "BLOCKED_NOT_ADMITTED_AMPLITUDE",
                    "channel_id": "UNASSIGNED_GENERIC_FIXTURE",
                    "composite_descendant_status": (
                        "BLOCKED_COMPOSITE_DESCENDANT_INSERTION_UNINSTANTIATED"
                    ),
                    "orientation": orientation,
                    "wick_kernel": "BLOCKED_VECTOR_WICK_KERNEL",
                    "wick_sign": "BLOCKED_WICK_SIGN",
                    "symmetry_factor": "BLOCKED_SYMMETRY_FACTOR",
                }.items()
            )
        ),
    )
    graph.assert_linear_momentum_routing()
    derivative_a = DerivativeToken(
        "D_external_out_D",
        DerivativeKind.D,
        IndexSlot(IndexSpace.UNDOTTED, "+", Variance.DOWN),
        f"{graph_id}:unresolved_out_D",
    )
    derivative_b = DerivativeToken(
        "D_external_out_E",
        DerivativeKind.D,
        IndexSlot(IndexSpace.UNDOTTED, "+", Variance.DOWN),
        f"{graph_id}:unresolved_out_E",
    )
    ledger = (
        DerivativeLedgerEntry(
            f"{graph_id}:external-route-D",
            derivative_a,
            "generic_fixture_insertion",
            "external_out_D",
            "OUT_D",
            1,
        ),
        DerivativeLedgerEntry(
            f"{graph_id}:external-route-E",
            derivative_b,
            "generic_fixture_insertion",
            "external_out_E",
            "OUT_E",
            1,
        ),
    )
    return graph.with_external_derivative_entries(ledger), ledger


def _graph_entry(
    graph: GraphIR,
    ledger: Sequence[DerivativeLedgerEntry],
    *,
    relation: str,
    parent_graph_id: str | None,
) -> dict[str, object]:
    return {
        "graph_id": graph.graph_id,
        "classification": "DRAW_MAP_TOPOLOGY_CANDIDATE",
        "relation": relation,
        "parent_graph_id": parent_graph_id,
        "admitted_amplitude": False,
        "blockers": list(LOOP_BLOCKERS),
        "graph_ir": graph.canonical_dict(),
        "momentum_validation": graph.validate_linear_momentum_routing(),
        "render_id_inventory": _graph_inventory(graph),
        "maps": {
            "ordinary_mermaid": _ordinary_mermaid(graph),
            "ordinary_dot": _ordinary_dot(graph),
            "supergraph_mermaid": graph.to_mermaid(),
            "supergraph_dot": graph.to_dot(),
        },
        "amplitude_skeleton": {
            "status": "BLOCKED_NOT_ADMITTED_AMPLITUDE",
            "expression": graph.amplitude_skeleton(),
        },
        "external_derivative_ledger": [_ledger_dict(entry) for entry in ledger],
    }


def _generic_fixture_entries(bundle: VertexGrammarBundle) -> tuple[dict[str, object], ...]:
    insertion = next(
        monomial
        for monomial in bundle.insertion_monomials
        if monomial.monomial_id == "prepotential_euler_ad_1"
    )
    cubic_actions = tuple(
        sorted(
            (
                monomial
                for monomial in bundle.action_monomials
                if monomial.sector == "GAUGE_KINETIC_W" and len(monomial.ordered_fields) == 3
            ),
            key=lambda item: item.monomial_id,
        )
    )
    if len(cubic_actions) != 2:
        raise AssertionError("the Project grammar must expose two ordered cubic W-kinetic monomials")
    entries: list[dict[str, object]] = []
    for orientation in ("DIRECT", "REFLECTED"):
        parent, ledger = _generic_triangle_fixture(
            orientation,
            insertion,
            cubic_actions[0],
            cubic_actions[1],
        )
        entries.append(_graph_entry(parent, ledger, relation="PARENT_TRIANGLE", parent_graph_id=None))
        for edge in parent.internal_edges:
            child = parent.collapse_edge(edge.edge_id)
            child.assert_linear_momentum_routing()
            metadata = dict(child.metadata)
            metadata["candidate_status"] = "BLOCKED_CONTACT_CHILD_NOT_ADMITTED_AMPLITUDE"
            child = replace(child, metadata=tuple(sorted(metadata.items())))
            entries.append(
                _graph_entry(
                    child,
                    ledger,
                    relation="COLLAPSED_CONTACT_CANDIDATE",
                    parent_graph_id=parent.graph_id,
                )
            )
    return tuple(entries)


def build_catalogue() -> dict[str, object]:
    bundle = build_project_vertex_grammar()
    channels = emit_ordered_family_channels()
    templates = _valence_only_templates(bundle)
    template_by_id = {template["template_id"]: template for template in templates}
    if len(template_by_id) != len(templates):
        raise AssertionError("topology template ids must be unique")

    tree_channels: list[dict[str, object]] = []
    reverse_bindings: list[dict[str, object]] = []
    for channel in channels:
        canonical = channel.canonical_dict()
        tree_channels.append(
            {
                "channel": canonical,
                "ordered_tree_maps": {
                    "mermaid": _tree_ast_mermaid(canonical["descendant"], f"tree_{channel.ordinal}_ordered"),
                    "dot": _tree_ast_dot(canonical["descendant"], f"tree_{channel.ordinal}_ordered"),
                },
                "reversed_tree_maps": {
                    "mermaid": _tree_ast_mermaid(
                        canonical["reversed_descendant"], f"tree_{channel.ordinal}_reversed"
                    ),
                    "dot": _tree_ast_dot(
                        canonical["reversed_descendant"], f"tree_{channel.ordinal}_reversed"
                    ),
                },
            }
        )
        reverse_bindings.append(
            {
                "reverse_binding_id": f"reverse_binding__{channel.channel_id}",
                "source_channel_id": channel.channel_id,
                "target_family_channel_id": channel.reverse_channel_id,
                "fixed_index_permutation": [
                    {
                        "source_position": 0,
                        "target_position": 1,
                        "letter": channel.left.canonical_dict(),
                    },
                    {
                        "source_position": 1,
                        "target_position": 0,
                        "letter": channel.right.canonical_dict(),
                    },
                ],
                "bound_reversed_descendant_channel_id": (
                    channel.reversed_descendant.channel_id
                ),
                "bound_reversed_descendant_sha256": _canonical_payload_sha256(
                    channel.reversed_descendant.canonical_dict()
                ),
                "tree_channel_ordinal": channel.ordinal,
            }
        )

    valence_only_request_product = {
        "kind": "DECLARATIVE_CARTESIAN_PRODUCT",
        "enumeration_order": ["ordered_channel_ids", "ordered_template_ids"],
        "ordered_channel_ids": [channel.channel_id for channel in channels],
        "ordered_template_ids": [str(template["template_id"]) for template in templates],
        "request_id_rule": "loop__{channel_id}__{template_id}",
        "reverse_request_id_rule": (
            "loop__{reverse_channel_id(channel_id)}__"
            "{reflection_template_id(template_id)}"
        ),
        "reverse_channel_id_source": "tree_channels[].channel.reverse_channel_id",
        "reflection_template_id_source": (
            "valence_only_templates[].reflection_template_id"
        ),
        "reverse_binding_id_rule": "reverse_binding__{channel_id}",
        "classification": "VALENCE_ONLY_NOT_GRAPH",
        "status": "BLOCKED_VALENCE_ONLY_NOT_GRAPH",
        "blocker_contract_ref": "blocker_contract.loop_blockers",
        "total_count": len(channels) * len(templates),
    }

    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "status": "BLOCKED_GAUGE_KERNEL_CANDIDATE_CATALOGUE",
        "authority_inputs": [
            "scripts/step5_graph_ir.py",
            "scripts/step5_vertex_grammar.py",
        ],
        "blocker_contract": {
            "loop_blockers": list(LOOP_BLOCKERS),
            "vertex_grammar_blockers": list(bundle.blockers),
            "candidate_pairing_is_admitted_amplitude": False,
            "topology_request_without_wick_pairing_is_graph": False,
        },
        "counts": {
            "ordered_channels": len(channels),
            "action_monomials": len(bundle.action_monomials),
            "action_vertices": len(bundle.action_vertices),
            "typed_zero_action_monomials": len(bundle.typed_zero_monomials),
            "insertion_chart_monomials": len(bundle.insertion_monomials),
            "insertion_chart_vertices": len(bundle.insertion_vertices),
            "valence_only_templates_per_channel": len(templates),
            "valence_only_requests": valence_only_request_product["total_count"],
            "generic_blocked_graph_fixtures": 8,
        },
        "typed_zero_action_monomials": [
            {
                "monomial_id": item.monomial_id,
                "sector": item.sector,
                "zero_reason": item.zero_reason,
                "source_equations": list(item.source_equations),
            }
            for item in bundle.typed_zero_monomials
        ],
        "action_monomials": [_monomial_manifest(item) for item in bundle.action_monomials],
        "insertion_chart_monomials": [
            {
                **_monomial_manifest(item),
                "core_status": "BLOCKED_UNINSTANTIATED_E_XI_CORE",
                "chart_series_status": "PROVED_5_28",
            }
            for item in bundle.insertion_monomials
        ],
        "tree_channels": tree_channels,
        "reverse_bindings": reverse_bindings,
        "valence_only_templates": list(templates),
        "valence_only_request_product": valence_only_request_product,
        "generic_blocked_graph_fixtures": list(_generic_fixture_entries(bundle)),
    }


def render_maps_markdown(catalogue: Mapping[str, object]) -> str:
    lines = [
        "# Step 5 deterministic graph maps",
        "",
        "Loop status: `BLOCKED_GAUGE_KERNEL_CANDIDATE_CATALOGUE`.",
        "",
    ]
    for tree in catalogue["tree_channels"]:  # type: ignore[index]
        channel = tree["channel"]
        lines.extend(
            [
                f'## Tree {channel["ordinal"]}: `{channel["channel_id"]}`',
                "",
                "```mermaid",
                tree["ordered_tree_maps"]["mermaid"].rstrip(),
                "```",
                "",
                "Reversed fixed-index word:",
                "",
                "```mermaid",
                tree["reversed_tree_maps"]["mermaid"].rstrip(),
                "```",
                "",
            ]
        )
    lines.extend(["## Generic blocked topology fixtures", ""])
    for entry in catalogue["generic_blocked_graph_fixtures"]:  # type: ignore[index]
        lines.extend(
            [
                f'### `{entry["graph_id"]}`',
                "",
                f'Status: `{entry["amplitude_skeleton"]["status"]}`.',
                "",
                "Ordinary Mermaid:",
                "",
                "```mermaid",
                entry["maps"]["ordinary_mermaid"].rstrip(),
                "```",
                "",
                "Ordinary DOT:",
                "",
                "```dot",
                entry["maps"]["ordinary_dot"].rstrip(),
                "```",
                "",
                "Supergraph Mermaid:",
                "",
                "```mermaid",
                entry["maps"]["supergraph_mermaid"].rstrip(),
                "```",
                "",
                "Supergraph DOT:",
                "",
                "```dot",
                entry["maps"]["supergraph_dot"].rstrip(),
                "```",
                "",
                "Formal blocked amplitude skeleton:",
                "",
                "```text",
                entry["amplitude_skeleton"]["expression"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_audit(catalogue_bytes: bytes, maps_bytes: bytes, catalogue: Mapping[str, object]) -> dict[str, object]:
    product = catalogue["valence_only_request_product"]  # type: ignore[index]
    fixtures = catalogue["generic_blocked_graph_fixtures"]  # type: ignore[index]
    topology_counts = {"TADPOLE": 0, "BUBBLE": 0, "TRIANGLE": 0}
    templates = {
        template["template_id"]: template
        for template in catalogue["valence_only_templates"]  # type: ignore[index]
    }
    channels = {
        tree["channel"]["channel_id"]: tree["channel"]
        for tree in catalogue["tree_channels"]  # type: ignore[index]
    }
    virtual_requests = []
    for channel_id in product["ordered_channel_ids"]:
        channel = channels[channel_id]
        for template_id in product["ordered_template_ids"]:
            template = templates[template_id]
            topology_counts[template["topology"]] += 1
            virtual_requests.append(
                {
                    "request_id": f"loop__{channel_id}__{template_id}",
                    "reverse_request_id": (
                        f"loop__{channel['reverse_channel_id']}__"
                        f"{template['reflection_template_id']}"
                    ),
                    "reverse_binding_id": f"reverse_binding__{channel_id}",
                }
            )
    request_ids = {request["request_id"] for request in virtual_requests}
    request_by_id = {request["request_id"]: request for request in virtual_requests}
    reverse_binding_by_id = {
        binding["reverse_binding_id"]: binding
        for binding in catalogue["reverse_bindings"]  # type: ignore[index]
    }
    reverse_bindings_exact = len(reverse_binding_by_id) == 16 and all(
        request["reverse_binding_id"] in reverse_binding_by_id
        for request in virtual_requests
    ) and all(
        binding["bound_reversed_descendant_sha256"]
        == _canonical_payload_sha256(
            catalogue["tree_channels"][binding["tree_channel_ordinal"] - 1]["channel"][  # type: ignore[index]
                "reversed_descendant"
            ]
        )
        for binding in reverse_binding_by_id.values()
    )
    fixture_render_equivalence = all(
        all(
            identifier in rendering
            for rendering in item["maps"].values()
            for identifier in (
                item["render_id_inventory"]["vertex_ids"]
                + item["render_id_inventory"]["internal_edge_ids"]
            )
        )
        for item in fixtures
    )
    fixture_amplitude_equivalence = all(
        all(
            edge_id in item["amplitude_skeleton"]["expression"]
            for edge_id in item["render_id_inventory"]["internal_edge_ids"]
        )
        for item in fixtures
    )
    typed_tensor_factors = [
        tensor
        for tree in catalogue["tree_channels"]  # type: ignore[index]
        for descendant_key in ("descendant", "reversed_descendant")
        for term in tree["channel"][descendant_key]["terms"]
        for tensor in term["tensor_factors"]
    ]
    typed_tensor_schema_exact = bool(typed_tensor_factors) and all(
        isinstance(tensor, dict)
        and tensor["symbol"] in ("c", "epsilon", "kappa")
        and len(tensor["ordered_indices"]) == len(tensor["bindings"])
        and all(index["variance"] in ("UP", "DOWN") for index in tensor["ordered_indices"])
        for tensor in typed_tensor_factors
    )
    checks = {
        "sixteen_indexed_tree_maps": len(catalogue["tree_channels"]) == 16,  # type: ignore[index]
        "twenty_seven_nonzero_action_vertices": catalogue["counts"]["action_vertices"] == 27,  # type: ignore[index]
        "two_typed_zero_fp_monomials": catalogue["counts"]["typed_zero_action_monomials"] == 2,  # type: ignore[index]
        "four_chart_insertions_core_blocked": all(
            item["core_status"] == "BLOCKED_UNINSTANTIATED_E_XI_CORE"
            for item in catalogue["insertion_chart_monomials"]  # type: ignore[index]
        ),
        "six_hundred_fifty_two_valence_only_templates_per_channel": catalogue["counts"]["valence_only_templates_per_channel"] == 652,  # type: ignore[index]
        "ten_thousand_four_hundred_thirty_two_valence_only_requests": (
            product["total_count"] == len(virtual_requests) == 10432
        ),
        "topology_distribution_exact": topology_counts
        == {"TADPOLE": 16, "BUBBLE": 432, "TRIANGLE": 9984},
        "all_valence_only_requests_are_not_graphs": (
            product["classification"] == "VALENCE_ONLY_NOT_GRAPH"
            and product["status"] == "BLOCKED_VALENCE_ONLY_NOT_GRAPH"
            and product["blocker_contract_ref"] == "blocker_contract.loop_blockers"
            and not any(
                key in product for key in ("graph_ir", "maps", "amplitude_skeleton")
            )
        ),
        "reverse_request_census_closed": all(
            request["reverse_request_id"] in request_ids for request in virtual_requests
        ),
        "reverse_request_map_is_involutive": all(
            request_by_id[request["reverse_request_id"]]["reverse_request_id"]
            == request["request_id"]
            for request in virtual_requests
        ),
        "fixed_index_reverse_bindings_exact": reverse_bindings_exact,
        "tree_tensor_factors_fully_typed": typed_tensor_schema_exact,
        "eight_generic_blocked_fixtures": len(fixtures) == 8,
        "two_generic_parent_triangle_fixtures": sum(
            item["relation"] == "PARENT_TRIANGLE" for item in fixtures
        )
        == 2,
        "six_contact_children": sum(
            item["relation"] == "COLLAPSED_CONTACT_CANDIDATE" for item in fixtures
        )
        == 6,
        "fixture_amplitudes_all_blocked": all(
            not item["admitted_amplitude"] for item in fixtures
        ),
        "external_derivative_ledger_retained": all(
            len(item["external_derivative_ledger"]) == 2 for item in fixtures
        ),
        "fixture_momentum_routing_exact": all(
            item["momentum_validation"]["passed"] for item in fixtures
        ),
        "fixture_ir_render_id_equivalence": fixture_render_equivalence,
        "fixture_ir_amplitude_edge_equivalence": fixture_amplitude_equivalence,
        "physical_ww_seed_not_claimed": all(
            "WW_seed" not in item["graph_id"]
            and item["graph_ir"]["metadata"]["channel_id"]
            == "UNASSIGNED_GENERIC_FIXTURE"
            for item in fixtures
        ),
        "no_numeric_anomaly_coefficient": b"anomaly_coefficient" not in catalogue_bytes.lower(),
    }
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "schema": 1,
        "task": catalogue["task"],
        "status": "PASS" if not failed else "FAIL",
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "failures": failed,
        "counts": catalogue["counts"],
        "topology_distribution": topology_counts,
        "sha256": {
            "generated/step5/graph-catalogue.json": _sha256(catalogue_bytes),
            "generated/step5/graph-maps.md": _sha256(maps_bytes),
            "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md": _sha256(
                CONTRACT_PATH.read_bytes()
            ),
            "scripts/step5_graph_ir.py": _sha256(GRAPH_IR_SOURCE.read_bytes()),
            "scripts/step5_vertex_grammar.py": _sha256(VERTEX_GRAMMAR_SOURCE.read_bytes()),
        },
    }


def _json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    catalogue = build_catalogue()
    catalogue_bytes = _json_bytes(catalogue)
    maps_bytes = render_maps_markdown(catalogue).encode("utf-8")
    audit = build_audit(catalogue_bytes, maps_bytes, catalogue)
    GENERATED.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOGUE_PATH.write_bytes(catalogue_bytes)
    MAPS_PATH.write_bytes(maps_bytes)
    AUDIT_PATH.write_bytes(_json_bytes(audit))
    print(json.dumps(audit["totals"], sort_keys=True))
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
