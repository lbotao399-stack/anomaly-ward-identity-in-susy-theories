#!/usr/bin/env python3
"""Exact combinatorial IR for the Step-5 Euclidean N=4 supergraph calculation.

This module contains no propagator normalization, interaction coefficient, or
anomaly coefficient.  Every coefficient entering an amplitude is an explicit
symbol supplied by the caller.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction
import json
import re
from typing import Iterable, Mapping, Sequence


class Statistics(str, Enum):
    BOSON = "BOSON"
    FERMION = "FERMION"


class Chirality(str, Enum):
    CHIRAL = "CHIRAL"
    ANTICHIRAL = "ANTICHIRAL"
    REAL = "REAL"
    UNCONSTRAINED = "UNCONSTRAINED"


class Flow(str, Enum):
    IN = "IN"
    OUT = "OUT"
    NONE = "NONE"


class Variance(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    FIXED = "FIXED"


class IndexSpace(str, Enum):
    COLOR_ADJOINT = "COLOR_ADJOINT"
    FLAVOR = "FLAVOR"
    UNDOTTED = "UNDOTTED"
    DOTTED = "DOTTED"
    VECTOR = "VECTOR"


class DerivativeKind(str, Enum):
    D = "D"
    BAR_D = "BAR_D"


class FactorRole(str, Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    COMPOSITE = "COMPOSITE"


class LetterFamily(str, Enum):
    W = "W"
    PHI = "Phi"
    TILDE_PHI = "TildePhi"
    TILDE_W = "TildeW"


@dataclass(frozen=True, order=True)
class IndexSlot:
    space: IndexSpace
    label: str
    variance: Variance

    def __post_init__(self) -> None:
        if not self.label:
            raise ValueError("an index label must be nonempty")


@dataclass(frozen=True)
class FieldType:
    name: str
    statistics: Statistics
    chirality: Chirality
    indices: tuple[IndexSlot, ...] = ()
    color_representation: str = "adjoint"

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("a field type must have a nonempty name")
        if not self.color_representation:
            raise ValueError("a color representation must be explicit")

    @property
    def parity(self) -> int:
        return int(self.statistics is Statistics.FERMION)


@dataclass(frozen=True, order=True)
class DerivativeToken:
    op_id: str
    kind: DerivativeKind
    index: IndexSlot
    origin: str

    def __post_init__(self) -> None:
        if not self.op_id or not self.origin:
            raise ValueError("a derivative needs a unique id and an origin")
        expected = IndexSpace.UNDOTTED if self.kind is DerivativeKind.D else IndexSpace.DOTTED
        if self.index.space is not expected:
            raise ValueError(f"{self.kind.value} requires an {expected.value} index")

    def render(self) -> str:
        head = "D" if self.kind is DerivativeKind.D else "barD"
        return f"{head}[{self.index.label}]"


@dataclass(frozen=True)
class HalfEdge:
    half_edge_id: str
    vertex_id: str
    slot: int
    field_type: FieldType
    flow: Flow
    momentum: str
    derivatives: tuple[DerivativeToken, ...] = ()

    def __post_init__(self) -> None:
        if not self.half_edge_id or not self.vertex_id:
            raise ValueError("half-edge and vertex ids must be nonempty")
        if self.slot < 0:
            raise ValueError("a half-edge slot must be nonnegative")
        if not self.momentum:
            raise ValueError("every half-edge momentum must be typed by a symbol")


@dataclass(frozen=True)
class Vertex:
    vertex_id: str
    kind: str
    ordered_half_edges: tuple[str, ...]
    coefficient_symbol: str
    color_word: tuple[str, ...]
    superspace_point: str
    momentum_delta: str
    momentum_injection: str = "0"
    coefficient_factors: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        required = (
            self.vertex_id,
            self.kind,
            self.coefficient_symbol,
            self.superspace_point,
            self.momentum_delta,
            self.momentum_injection,
        )
        if any(not value for value in required):
            raise ValueError("vertex labels, coefficient, point, and momentum delta are mandatory")
        if len(self.ordered_half_edges) != len(set(self.ordered_half_edges)):
            raise ValueError("a vertex cannot repeat a half-edge")
        if any(not factor for factor in self.coefficient_factors):
            raise ValueError("ordered coefficient factors must be nonempty")

    @property
    def effective_coefficient_factors(self) -> tuple[str, ...]:
        return self.coefficient_factors or (self.coefficient_symbol,)


@dataclass(frozen=True)
class InternalEdge:
    edge_id: str
    left_half_edge: str
    right_half_edge: str
    propagator_symbol: str
    momentum: str
    orientation: Flow = Flow.NONE

    def __post_init__(self) -> None:
        required = (
            self.edge_id,
            self.left_half_edge,
            self.right_half_edge,
            self.propagator_symbol,
            self.momentum,
        )
        if any(not value for value in required):
            raise ValueError("an internal edge must be fully labelled")
        if self.left_half_edge == self.right_half_edge:
            raise ValueError("an internal edge needs two distinct half-edges")


@dataclass(frozen=True)
class ExternalLeg:
    leg_id: str
    attached_half_edge: str
    field_type: FieldType
    momentum: str
    color_label: str
    flavor_label: str | None = None
    spinor_indices: tuple[IndexSlot, ...] = ()
    operator_derivatives: tuple[DerivativeToken, ...] = ()

    def __post_init__(self) -> None:
        if any(not value for value in (self.leg_id, self.attached_half_edge, self.momentum, self.color_label)):
            raise ValueError("an external leg must retain id, half-edge, momentum, and color")

    def operator_word(self) -> str:
        derivative_word = " ".join(token.render() for token in self.operator_derivatives)
        field_word = self.field_type.name
        labels: list[str] = []
        if self.flavor_label is not None:
            labels.append(f"flavor={self.flavor_label}")
        if self.spinor_indices:
            labels.append(
                "spinor="
                + ",".join(
                    f"{index.space.value}:{index.label}:{index.variance.value}"
                    for index in self.spinor_indices
                )
            )
        if labels:
            field_word += "{" + ";".join(labels) + "}"
        return f"{derivative_word} {field_word}".strip()


def _metadata_dict(metadata: tuple[tuple[str, str], ...]) -> dict[str, str]:
    if len({key for key, _ in metadata}) != len(metadata):
        raise ValueError("graph metadata keys must be unique")
    return dict(metadata)


def parse_linear_momentum(expression: str) -> tuple[tuple[str, int], ...]:
    """Parse an exact integer linear combination of symbolic momenta."""

    compact = expression.replace(" ", "")
    if compact in ("", "0"):
        return ()
    if compact[0] not in "+-":
        compact = "+" + compact
    terms: dict[str, int] = {}
    position = 0
    while position < len(compact):
        sign = 1 if compact[position] == "+" else -1
        position += 1
        match = re.match(r"(?:(\d+)\*)?([A-Za-z][A-Za-z0-9_]*)", compact[position:])
        if match is None:
            raise ValueError(f"invalid exact linear momentum expression: {expression}")
        coefficient = int(match.group(1) or "1") * sign
        symbol = match.group(2)
        terms[symbol] = terms.get(symbol, 0) + coefficient
        position += match.end()
    return tuple(sorted((symbol, coefficient) for symbol, coefficient in terms.items() if coefficient))


def render_linear_momentum(momentum: Sequence[tuple[str, int]]) -> str:
    pieces: list[str] = []
    for symbol, coefficient in sorted(momentum):
        if coefficient == 0:
            continue
        magnitude = abs(coefficient)
        body = symbol if magnitude == 1 else f"{magnitude}*{symbol}"
        if not pieces:
            pieces.append(body if coefficient > 0 else f"-{body}")
        else:
            pieces.append(("+" if coefficient > 0 else "-") + body)
    return "".join(pieces) or "0"


def _sum_linear_momenta(*expressions: str) -> str:
    total: dict[str, int] = {}
    for expression in expressions:
        for symbol, coefficient in parse_linear_momentum(expression):
            total[symbol] = total.get(symbol, 0) + coefficient
    return render_linear_momentum(tuple(total.items()))


def _cycle_rank_from_parts(
    vertices: Sequence[Vertex],
    half_edges: Sequence[HalfEdge],
    internal_edges: Sequence[InternalEdge],
) -> int:
    """Return the first Betti number E-V+C of the internal multigraph."""

    if not vertices:
        return 0
    vertex_ids = tuple(vertex.vertex_id for vertex in vertices)
    half_edge_vertex = {half_edge.half_edge_id: half_edge.vertex_id for half_edge in half_edges}
    adjacency = {vertex_id: set() for vertex_id in vertex_ids}
    for edge in internal_edges:
        if edge.left_half_edge not in half_edge_vertex or edge.right_half_edge not in half_edge_vertex:
            raise ValueError("cycle-rank calculation found an absent edge endpoint")
        left = half_edge_vertex[edge.left_half_edge]
        right = half_edge_vertex[edge.right_half_edge]
        adjacency[left].add(right)
        adjacency[right].add(left)
    components = 0
    unseen = set(vertex_ids)
    while unseen:
        components += 1
        stack = [next(iter(unseen))]
        while stack:
            vertex_id = stack.pop()
            if vertex_id not in unseen:
                continue
            unseen.remove(vertex_id)
            stack.extend(adjacency[vertex_id] & unseen)
    rank = len(internal_edges) - len(vertices) + components
    if rank < 0:
        raise AssertionError("an internal graph has negative cycle rank")
    return rank


@dataclass(frozen=True)
class DerivativeLedgerEntry:
    step_id: str
    derivative: DerivativeToken
    from_factor: str
    to_factor: str
    external_leg_id: str | None
    koszul_sign: int

    def __post_init__(self) -> None:
        if self.koszul_sign not in (-1, 1):
            raise ValueError("a Koszul sign is exactly +1 or -1")
        if any(not value for value in (self.step_id, self.from_factor, self.to_factor)):
            raise ValueError("a derivative ledger entry must retain its complete route")


@dataclass(frozen=True)
class GraphIR:
    graph_id: str
    vertices: tuple[Vertex, ...]
    half_edges: tuple[HalfEdge, ...]
    internal_edges: tuple[InternalEdge, ...]
    external_legs: tuple[ExternalLeg, ...]
    loop_momenta: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if not self.graph_id:
            raise ValueError("a graph id must be nonempty")
        self.validate()

    def validate(self) -> None:
        vertices = {vertex.vertex_id: vertex for vertex in self.vertices}
        half_edges = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        if len(vertices) != len(self.vertices):
            raise ValueError("vertex ids must be unique")
        if len(half_edges) != len(self.half_edges):
            raise ValueError("half-edge ids must be unique")
        if len({edge.edge_id for edge in self.internal_edges}) != len(self.internal_edges):
            raise ValueError("internal-edge ids must be unique")
        if len({leg.leg_id for leg in self.external_legs}) != len(self.external_legs):
            raise ValueError("external-leg ids must be unique")
        if len(set(self.loop_momenta)) != len(self.loop_momenta) or any(
            not momentum for momentum in self.loop_momenta
        ):
            raise ValueError("loop-momentum basis symbols must be nonempty and unique")
        expected_loop_rank = _cycle_rank_from_parts(
            self.vertices,
            self.half_edges,
            self.internal_edges,
        )
        if len(self.loop_momenta) != expected_loop_rank:
            raise ValueError(
                "loop-momentum basis length must equal E-V+C: "
                f"got {len(self.loop_momenta)}, expected {expected_loop_rank}"
            )
        _metadata_dict(self.metadata)

        declared: list[str] = []
        for vertex in self.vertices:
            declared.extend(vertex.ordered_half_edges)
            for slot, half_edge_id in enumerate(vertex.ordered_half_edges):
                if half_edge_id not in half_edges:
                    raise ValueError(f"vertex {vertex.vertex_id} names absent half-edge {half_edge_id}")
                half_edge = half_edges[half_edge_id]
                if half_edge.vertex_id != vertex.vertex_id or half_edge.slot != slot:
                    raise ValueError("vertex order and half-edge vertex/slot data disagree")
        if sorted(declared) != sorted(half_edges):
            raise ValueError("every half-edge must occur in exactly one ordered vertex word")

        used: list[str] = []
        for edge in self.internal_edges:
            if edge.left_half_edge not in half_edges or edge.right_half_edge not in half_edges:
                raise ValueError("an internal edge references an absent half-edge")
            used.extend((edge.left_half_edge, edge.right_half_edge))
        for leg in self.external_legs:
            if leg.attached_half_edge not in half_edges:
                raise ValueError("an external leg references an absent half-edge")
            if half_edges[leg.attached_half_edge].field_type != leg.field_type:
                raise ValueError("external-leg and half-edge field types disagree")
            used.append(leg.attached_half_edge)
        if sorted(used) != sorted(half_edges):
            raise ValueError("every half-edge must terminate exactly once internally or externally")

    def cycle_rank(self) -> int:
        return _cycle_rank_from_parts(self.vertices, self.half_edges, self.internal_edges)

    def validate_linear_momentum_routing(self) -> dict[str, object]:
        """Check exact edge opposition/reference and all-incoming vertex conservation."""

        half_edges = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        edge_checks: dict[str, dict[str, bool]] = {}
        for edge in self.internal_edges:
            left = half_edges[edge.left_half_edge].momentum
            right = half_edges[edge.right_half_edge].momentum
            endpoint_opposition = not parse_linear_momentum(_sum_linear_momenta(left, right))
            edge_reference_match = parse_linear_momentum(left) == parse_linear_momentum(edge.momentum)
            edge_checks[edge.edge_id] = {
                "endpoint_opposition": endpoint_opposition,
                "edge_reference_match": edge_reference_match,
            }
        vertex_checks: dict[str, bool] = {}
        for vertex in self.vertices:
            total = _sum_linear_momenta(
                *(half_edges[half_edge_id].momentum for half_edge_id in vertex.ordered_half_edges),
                vertex.momentum_injection,
            )
            vertex_checks[vertex.vertex_id] = not parse_linear_momentum(total)
        passed = all(
            all(check.values()) for check in edge_checks.values()
        ) and all(vertex_checks.values())
        return {
            "passed": passed,
            "edge_checks": edge_checks,
            "vertex_conservation": vertex_checks,
        }

    def assert_linear_momentum_routing(self) -> None:
        result = self.validate_linear_momentum_routing()
        if not result["passed"]:
            raise ValueError(f"linear momentum routing failed: {result}")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "graph_id": self.graph_id,
            "vertices": [
                {
                    "vertex_id": vertex.vertex_id,
                    "kind": vertex.kind,
                    "ordered_half_edges": list(vertex.ordered_half_edges),
                    "coefficient_symbol": vertex.coefficient_symbol,
                    "color_word": list(vertex.color_word),
                    "superspace_point": vertex.superspace_point,
                    "momentum_delta": vertex.momentum_delta,
                    "momentum_injection": vertex.momentum_injection,
                    "coefficient_factors": list(vertex.effective_coefficient_factors),
                }
                for vertex in self.vertices
            ],
            "half_edges": [
                {
                    "half_edge_id": half_edge.half_edge_id,
                    "vertex_id": half_edge.vertex_id,
                    "slot": half_edge.slot,
                    "field_type": _field_type_dict(half_edge.field_type),
                    "flow": half_edge.flow.value,
                    "momentum": half_edge.momentum,
                    "derivatives": [_derivative_dict(token) for token in half_edge.derivatives],
                }
                for half_edge in self.half_edges
            ],
            "internal_edges": [
                {
                    "edge_id": edge.edge_id,
                    "left_half_edge": edge.left_half_edge,
                    "right_half_edge": edge.right_half_edge,
                    "propagator_symbol": edge.propagator_symbol,
                    "momentum": edge.momentum,
                    "orientation": edge.orientation.value,
                }
                for edge in self.internal_edges
            ],
            "external_legs": [
                {
                    "leg_id": leg.leg_id,
                    "attached_half_edge": leg.attached_half_edge,
                    "field_type": _field_type_dict(leg.field_type),
                    "momentum": leg.momentum,
                    "color_label": leg.color_label,
                    "flavor_label": leg.flavor_label,
                    "spinor_indices": [_index_dict(index) for index in leg.spinor_indices],
                    "operator_derivatives": [
                        _derivative_dict(token) for token in leg.operator_derivatives
                    ],
                }
                for leg in self.external_legs
            ],
            "loop_momenta": list(self.loop_momenta),
            "metadata": dict(self.metadata),
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    def to_mermaid(self) -> str:
        half_edges = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        lines = ["graph LR"]
        for vertex in self.vertices:
            lines.append(f'  {vertex.vertex_id}["{vertex.vertex_id}:{vertex.kind}"]')
        for leg in self.external_legs:
            external_id = f"X_{leg.leg_id}"
            lines.append(f'  {external_id}["{leg.leg_id}:{leg.operator_word()}({leg.momentum})"]')
            vertex_id = half_edges[leg.attached_half_edge].vertex_id
            lines.append(
                f'  {external_id} -- "{_half_edge_word(half_edges[leg.attached_half_edge])}" --> {vertex_id}'
            )
        for edge in self.internal_edges:
            left_vertex = half_edges[edge.left_half_edge].vertex_id
            right_vertex = half_edges[edge.right_half_edge].vertex_id
            label = (
                f"{edge.edge_id}:{edge.propagator_symbol}({edge.momentum});"
                f"{_half_edge_word(half_edges[edge.left_half_edge])};"
                f"{_half_edge_word(half_edges[edge.right_half_edge])}"
            )
            arrow = "-->" if edge.orientation is not Flow.NONE else "---"
            lines.append(f'  {left_vertex} {arrow}|"{label}"| {right_vertex}')
        return "\n".join(lines) + "\n"

    def to_dot(self) -> str:
        half_edges = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        lines = [f'digraph "{self.graph_id}" {{']
        for vertex in self.vertices:
            lines.append(f'  "{vertex.vertex_id}" [label="{vertex.vertex_id}:{vertex.kind}"];')
        for leg in self.external_legs:
            external_id = f"X_{leg.leg_id}"
            lines.append(f'  "{external_id}" [shape=box,label="{leg.leg_id}:{leg.operator_word()}({leg.momentum})"];')
            vertex_id = half_edges[leg.attached_half_edge].vertex_id
            lines.append(
                f'  "{external_id}" -> "{vertex_id}" '
                f'[label="{_half_edge_word(half_edges[leg.attached_half_edge])}"];'
            )
        for edge in self.internal_edges:
            left_vertex = half_edges[edge.left_half_edge].vertex_id
            right_vertex = half_edges[edge.right_half_edge].vertex_id
            direction = "forward" if edge.orientation is not Flow.NONE else "none"
            label = (
                f"{edge.edge_id}:{edge.propagator_symbol}({edge.momentum});"
                f"{_half_edge_word(half_edges[edge.left_half_edge])};"
                f"{_half_edge_word(half_edges[edge.right_half_edge])}"
            )
            lines.append(
                f'  "{left_vertex}" -> "{right_vertex}" [dir={direction},label="{label}"];'
            )
        lines.append("}")
        return "\n".join(lines) + "\n"

    def amplitude_skeleton(self) -> str:
        metadata = _metadata_dict(self.metadata)
        half_edges = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        wick_sign = metadata.get("wick_sign", f"WickSign[{self.graph_id}]")
        symmetry = metadata.get("symmetry_factor", f"SymmetryFactor[{self.graph_id}]")
        measure = " ".join(
            f"Integral[d^d {momentum}]" for momentum in self.loop_momenta
        ) or "NoLoopIntegral"
        vertex_word = " ".join(
            f"({vertex.coefficient_symbol})[{','.join(vertex.color_word)}]"
            f"*Delta[{vertex.momentum_delta}]"
            f"*Slots[{','.join(_half_edge_word(half_edges[item]) for item in vertex.ordered_half_edges)}]"
            for vertex in self.vertices
        ) or "1"
        edge_word = " ".join(
            f"Edge[{edge.edge_id}]=({edge.propagator_symbol})["
            f"{_half_edge_word(half_edges[edge.left_half_edge])},"
            f"{_half_edge_word(half_edges[edge.right_half_edge])};{edge.momentum}]"
            for edge in self.internal_edges
        ) or "1"
        external_word = " ".join(
            f"{leg.operator_word()}[{leg.color_label};{leg.momentum};"
            f"{_half_edge_word(half_edges[leg.attached_half_edge])}]"
            for leg in self.external_legs
        ) or "1"
        return (
            f"Amplitude[{self.graph_id}] := ({wick_sign}) * ({symmetry}) * {measure} "
            f"* {vertex_word} * {edge_word} * {external_word}"
        )

    def collapse_edge(self, edge_id: str) -> GraphIR:
        edge_by_id = {edge.edge_id: edge for edge in self.internal_edges}
        if edge_id not in edge_by_id:
            raise KeyError(edge_id)
        collapsed = edge_by_id[edge_id]
        half_edge_by_id = {half_edge.half_edge_id: half_edge for half_edge in self.half_edges}
        left_vertex_id = half_edge_by_id[collapsed.left_half_edge].vertex_id
        right_vertex_id = half_edge_by_id[collapsed.right_half_edge].vertex_id
        merged_vertex_ids = (left_vertex_id,) if left_vertex_id == right_vertex_id else (
            left_vertex_id,
            right_vertex_id,
        )
        vertices_by_id = {vertex.vertex_id: vertex for vertex in self.vertices}
        contact_vertex_id = f"contact__{edge_id}"

        merged_half_edge_ids: list[str] = []
        merged_color_word: list[str] = []
        merged_points: list[str] = []
        merged_deltas: list[str] = []
        for vertex_id in merged_vertex_ids:
            vertex = vertices_by_id[vertex_id]
            merged_half_edge_ids.extend(
                half_edge_id
                for half_edge_id in vertex.ordered_half_edges
                if half_edge_id not in (collapsed.left_half_edge, collapsed.right_half_edge)
            )
            merged_color_word.extend(vertex.color_word)
            merged_points.append(vertex.superspace_point)
            merged_deltas.append(vertex.momentum_delta)

        contact_vertex = Vertex(
            vertex_id=contact_vertex_id,
            kind="CONTACT_CHILD",
            ordered_half_edges=tuple(merged_half_edge_ids),
            coefficient_symbol="OrderedProduct["
            + ",".join(
                tuple(
                    factor
                    for vertex_id in merged_vertex_ids
                    for factor in vertices_by_id[vertex_id].effective_coefficient_factors
                )
                + (f"ContactFrom[{collapsed.propagator_symbol}]",)
            )
            + "]",
            color_word=tuple(merged_color_word),
            superspace_point="=".join(merged_points),
            momentum_delta=" & ".join(merged_deltas),
            momentum_injection=_sum_linear_momenta(
                *(vertices_by_id[vertex_id].momentum_injection for vertex_id in merged_vertex_ids)
            ),
            coefficient_factors=tuple(
                factor
                for vertex_id in merged_vertex_ids
                for factor in vertices_by_id[vertex_id].effective_coefficient_factors
            )
            + (f"ContactFrom[{collapsed.propagator_symbol}]",),
        )

        first_position = min(
            position for position, vertex in enumerate(self.vertices) if vertex.vertex_id in merged_vertex_ids
        )
        new_vertices: list[Vertex] = []
        for position, vertex in enumerate(self.vertices):
            if position == first_position:
                new_vertices.append(contact_vertex)
            if vertex.vertex_id not in merged_vertex_ids:
                new_vertices.append(vertex)

        removed = {collapsed.left_half_edge, collapsed.right_half_edge}
        new_half_edges: list[HalfEdge] = []
        contact_slot = {half_edge_id: slot for slot, half_edge_id in enumerate(merged_half_edge_ids)}
        for half_edge in self.half_edges:
            if half_edge.half_edge_id in removed:
                continue
            if half_edge.vertex_id in merged_vertex_ids:
                new_half_edges.append(
                    replace(
                        half_edge,
                        vertex_id=contact_vertex_id,
                        slot=contact_slot[half_edge.half_edge_id],
                    )
                )
            else:
                new_half_edges.append(half_edge)

        metadata = dict(self.metadata)
        metadata.update(
            {
                "parent_graph_id": self.graph_id,
                "collapsed_edge_id": edge_id,
                "collapsed_propagator_symbol": collapsed.propagator_symbol,
                "graph_relation": "CONTACT_CHILD",
            }
        )
        new_internal_edges = tuple(edge for edge in self.internal_edges if edge.edge_id != edge_id)
        child_cycle_rank = _cycle_rank_from_parts(
            tuple(new_vertices),
            tuple(new_half_edges),
            new_internal_edges,
        )
        if child_cycle_rank > len(self.loop_momenta):
            raise AssertionError("edge contraction cannot increase the cycle rank")
        child_loop_momenta = self.loop_momenta[:child_cycle_rank]
        metadata["loop_basis_parent"] = ",".join(self.loop_momenta)
        metadata["loop_basis_child"] = ",".join(child_loop_momenta)
        metadata["loop_basis_rule"] = "RECOMPUTE_BY_E_MINUS_V_PLUS_C"
        return GraphIR(
            graph_id=f"{self.graph_id}__collapse__{edge_id}",
            vertices=tuple(new_vertices),
            half_edges=tuple(new_half_edges),
            internal_edges=new_internal_edges,
            external_legs=self.external_legs,
            loop_momenta=child_loop_momenta,
            metadata=tuple(sorted(metadata.items())),
        )

    def with_external_derivative_entries(
        self, entries: Sequence[DerivativeLedgerEntry]
    ) -> GraphIR:
        by_leg: dict[str, list[DerivativeToken]] = {}
        for entry in entries:
            if entry.external_leg_id is not None:
                by_leg.setdefault(entry.external_leg_id, []).append(entry.derivative)
        known_legs = {leg.leg_id for leg in self.external_legs}
        unknown = sorted(set(by_leg) - known_legs)
        if unknown:
            raise ValueError(f"external derivative ledger names absent legs: {unknown}")
        new_legs: list[ExternalLeg] = []
        for leg in self.external_legs:
            additions = tuple(by_leg.get(leg.leg_id, ()))
            existing = {token.op_id for token in leg.operator_derivatives}
            if any(token.op_id in existing for token in additions):
                raise ValueError("an external derivative cannot be recorded twice")
            new_legs.append(replace(leg, operator_derivatives=additions + leg.operator_derivatives))
        return replace(self, external_legs=tuple(new_legs))

    def with_external_derivatives_from_branch(self, branch: DAlgebraBranch) -> GraphIR:
        """Transfer the final branch state, not historical derivative routes, to the graph."""

        by_leg = branch.final_external_derivatives()
        known_legs = {leg.leg_id for leg in self.external_legs}
        unknown = sorted(set(by_leg) - known_legs)
        if unknown:
            raise ValueError(f"D-algebra branch names absent external legs: {unknown}")
        return replace(
            self,
            external_legs=tuple(
                replace(leg, operator_derivatives=by_leg.get(leg.leg_id, leg.operator_derivatives))
                for leg in self.external_legs
            ),
        )


@dataclass(frozen=True)
class AllowedContraction:
    rule_id: str
    left_field_name: str
    right_field_name: str
    propagator_symbol: str
    oriented: bool

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.rule_id,
                self.left_field_name,
                self.right_field_name,
                self.propagator_symbol,
            )
        ):
            raise ValueError("a contraction rule must be fully symbolic and explicit")


@dataclass(frozen=True)
class WickPair:
    rule_id: str
    left_half_edge: str
    right_half_edge: str
    propagator_symbol: str
    oriented: bool


@dataclass(frozen=True)
class FermionPermutationStep:
    contracted_half_edges: tuple[str, str]
    odd_factors_crossed: int
    koszul_sign: int


@dataclass(frozen=True)
class WickPairing:
    pairs: tuple[WickPair, ...]
    fermion_permutation: tuple[FermionPermutationStep, ...]
    koszul_sign: int
    declared_field_word: tuple[str, ...] = ()

    def signature(self) -> tuple[tuple[str, str, str], ...]:
        return tuple(
            (pair.left_half_edge, pair.right_half_edge, pair.rule_id) for pair in self.pairs
        )

    def to_internal_edges(self, prefix: str = "e", momentum_prefix: str = "k") -> tuple[InternalEdge, ...]:
        return tuple(
            InternalEdge(
                edge_id=f"{prefix}{position}",
                left_half_edge=pair.left_half_edge,
                right_half_edge=pair.right_half_edge,
                propagator_symbol=pair.propagator_symbol,
                momentum=f"{momentum_prefix}{position}",
                orientation=Flow.OUT if pair.oriented else Flow.NONE,
            )
            for position, pair in enumerate(self.pairs)
        )


class PropagatorGrammar:
    def __init__(self, rules: Iterable[AllowedContraction]) -> None:
        self.rules = tuple(sorted(rules, key=lambda rule: rule.rule_id))
        if len({rule.rule_id for rule in self.rules}) != len(self.rules):
            raise ValueError("contraction rule ids must be unique")

    def matches(self, left: HalfEdge, right: HalfEdge) -> tuple[WickPair, ...]:
        matches: list[WickPair] = []
        for rule in self.rules:
            exact = (
                left.field_type.name == rule.left_field_name
                and right.field_type.name == rule.right_field_name
            )
            reversed_match = (
                left.field_type.name == rule.right_field_name
                and right.field_type.name == rule.left_field_name
            )
            if exact:
                matches.append(
                    WickPair(
                        rule.rule_id,
                        left.half_edge_id,
                        right.half_edge_id,
                        rule.propagator_symbol,
                        rule.oriented,
                    )
                )
            elif reversed_match:
                if rule.oriented:
                    matches.append(
                        WickPair(
                            rule.rule_id,
                            right.half_edge_id,
                            left.half_edge_id,
                            rule.propagator_symbol,
                            rule.oriented,
                        )
                    )
                elif rule.left_field_name != rule.right_field_name:
                    matches.append(
                        WickPair(
                            rule.rule_id,
                            left.half_edge_id,
                            right.half_edge_id,
                            rule.propagator_symbol,
                            rule.oriented,
                        )
                    )
            if (exact or reversed_match) and left.field_type.parity != right.field_type.parity:
                raise ValueError("a propagator cannot contract fields of unequal Grassmann parity")
        return tuple(matches)


def enumerate_wick_pairings(
    half_edges: Sequence[HalfEdge],
    grammar: PropagatorGrammar,
    *,
    forbid_same_vertex: bool = False,
) -> tuple[WickPairing, ...]:
    """Enumerate complete typed Wick pairings in deterministic half-edge order."""

    # The caller tuple is the declared global Grassmann field word.  Opaque ids
    # identify factors but never define their algebraic order.
    declared_word = tuple(half_edges)
    if len(declared_word) % 2:
        return ()
    if len({half_edge.half_edge_id for half_edge in declared_word}) != len(declared_word):
        raise ValueError("Wick enumeration requires unique half-edge ids")

    def recurse(remaining: tuple[HalfEdge, ...]) -> list[WickPairing]:
        if not remaining:
            return [WickPairing((), (), 1)]
        first = remaining[0]
        results: list[WickPairing] = []
        for partner_position in range(1, len(remaining)):
            partner = remaining[partner_position]
            if forbid_same_vertex and first.vertex_id == partner.vertex_id:
                continue
            matches = grammar.matches(first, partner)
            if not matches:
                continue
            odd_crossings = 0
            if first.field_type.parity == partner.field_type.parity == 1:
                odd_crossings = sum(
                    half_edge.field_type.parity for half_edge in remaining[1:partner_position]
                )
            local_sign = -1 if odd_crossings % 2 else 1
            reduced = remaining[1:partner_position] + remaining[partner_position + 1 :]
            for match in matches:
                for child in recurse(reduced):
                    results.append(
                        WickPairing(
                            pairs=(match,) + child.pairs,
                            fermion_permutation=(
                                FermionPermutationStep(
                                    (first.half_edge_id, partner.half_edge_id),
                                    odd_crossings,
                                    local_sign,
                                ),
                            )
                            + child.fermion_permutation,
                            koszul_sign=local_sign * child.koszul_sign,
                        )
                    )
        return results

    completed = tuple(
        replace(
            pairing,
            declared_field_word=tuple(half_edge.half_edge_id for half_edge in declared_word),
        )
        for pairing in recurse(declared_word)
    )
    return tuple(sorted(completed, key=lambda pairing: pairing.signature()))


@dataclass(frozen=True)
class DAlgebraFactor:
    factor_id: str
    symbol: str
    base_parity: int
    role: FactorRole
    external_leg_id: str | None = None
    derivatives: tuple[DerivativeToken, ...] = ()

    def __post_init__(self) -> None:
        if not self.factor_id or not self.symbol:
            raise ValueError("a D-algebra factor must have id and symbol")
        if self.base_parity not in (0, 1):
            raise ValueError("base parity is exactly 0 or 1")
        if self.role is FactorRole.EXTERNAL and not self.external_leg_id:
            raise ValueError("an external factor must name its external leg")
        if self.role is not FactorRole.EXTERNAL and self.external_leg_id is not None:
            raise ValueError("only an external factor may name an external leg")

    @property
    def effective_parity(self) -> int:
        return (self.base_parity + len(self.derivatives)) % 2

    def render(self) -> str:
        word = " ".join(token.render() for token in self.derivatives)
        return f"{word} {self.symbol}".strip()


@dataclass(frozen=True)
class DAlgebraBranch:
    coefficient: int
    factors: tuple[DAlgebraFactor, ...]
    external_derivative_ledger: tuple[DerivativeLedgerEntry, ...] = ()

    def __post_init__(self) -> None:
        if self.coefficient == 0:
            raise ValueError("zero branches must be removed, not stored")
        if len({factor.factor_id for factor in self.factors}) != len(self.factors):
            raise ValueError("factor ids must be unique within an ordered branch")
        derivative_ids = [
            derivative.op_id for factor in self.factors for derivative in factor.derivatives
        ]
        if len(derivative_ids) != len(set(derivative_ids)):
            raise ValueError("derivative ids must be unique within a branch")

    @property
    def total_parity(self) -> int:
        return sum(factor.effective_parity for factor in self.factors) % 2

    def canonical_dict(self) -> dict[str, object]:
        return {
            "coefficient": self.coefficient,
            "factors": [
                {
                    "factor_id": factor.factor_id,
                    "symbol": factor.symbol,
                    "base_parity": factor.base_parity,
                    "effective_parity": factor.effective_parity,
                    "role": factor.role.value,
                    "external_leg_id": factor.external_leg_id,
                    "derivatives": [_derivative_dict(token) for token in factor.derivatives],
                }
                for factor in self.factors
            ],
            "external_derivative_ledger": [
                {
                    "step_id": entry.step_id,
                    "derivative": _derivative_dict(entry.derivative),
                    "from_factor": entry.from_factor,
                    "to_factor": entry.to_factor,
                    "external_leg_id": entry.external_leg_id,
                    "koszul_sign": entry.koszul_sign,
                }
                for entry in self.external_derivative_ledger
            ],
        }

    def final_external_derivatives(self) -> dict[str, tuple[DerivativeToken, ...]]:
        """Return derivatives on final external factors, excluding route history."""

        result: dict[str, tuple[DerivativeToken, ...]] = {}
        for factor in self.factors:
            if factor.role is not FactorRole.EXTERNAL:
                continue
            assert factor.external_leg_id is not None
            if factor.external_leg_id in result:
                raise ValueError("one branch cannot contain two factors for the same external leg")
            result[factor.external_leg_id] = factor.derivatives
        return result


@dataclass(frozen=True)
class RewriteTrace:
    step_id: str
    input: Mapping[str, object]
    rule: str
    assumptions: tuple[str, ...]
    koszul_sign: tuple[int, ...]
    output: tuple[Mapping[str, object], ...]
    invariants: Mapping[str, object]

    def canonical_dict(self) -> dict[str, object]:
        return {
            "step_id": self.step_id,
            "input": dict(self.input),
            "rule": self.rule,
            "assumptions": list(self.assumptions),
            "koszul_sign": list(self.koszul_sign),
            "output": [dict(branch) for branch in self.output],
            "invariants": dict(self.invariants),
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


class DAlgebraEngine:
    """Oriented superspace IBP with a lossless derivative route ledger."""

    ASSUMPTIONS = (
        "superspace_boundary_term=0",
        "D_and_barD_are_odd_graded_derivations",
        "factor_order_is_fixed",
        "derivative_word_is_outermost_left_to_innermost_right",
    )

    def __init__(self) -> None:
        self.traces: list[RewriteTrace] = []

    def integrate_by_parts(
        self,
        branch: DAlgebraBranch,
        *,
        source_factor_id: str,
        derivative_id: str,
        step_id: str,
    ) -> tuple[tuple[DAlgebraBranch, ...], RewriteTrace]:
        if not step_id:
            raise ValueError("every D-algebra rewrite needs a step id")
        source_position = next(
            (position for position, factor in enumerate(branch.factors) if factor.factor_id == source_factor_id),
            None,
        )
        if source_position is None:
            raise KeyError(source_factor_id)
        source = branch.factors[source_position]
        derivative_position = next(
            (position for position, token in enumerate(source.derivatives) if token.op_id == derivative_id),
            None,
        )
        if derivative_position is None:
            raise KeyError(derivative_id)
        if derivative_position != 0:
            raise ValueError(
                "IBP can move only the outermost derivative; commute the operator word explicitly first"
            )
        derivative = source.derivatives[derivative_position]

        stripped_source = replace(
            source,
            derivatives=source.derivatives[:derivative_position] + source.derivatives[derivative_position + 1 :],
        )
        base_factors = list(branch.factors)
        base_factors[source_position] = stripped_source
        prefix_parity: list[int] = []
        running = 0
        for factor in base_factors:
            prefix_parity.append(running)
            running = (running + factor.effective_parity) % 2

        output: list[DAlgebraBranch] = []
        signs: list[int] = []
        for target_position, target in enumerate(base_factors):
            if target_position == source_position:
                continue
            exponent = (prefix_parity[target_position] + prefix_parity[source_position]) % 2
            koszul_sign = -1 if exponent == 0 else 1
            signs.append(koszul_sign)
            routed_factors = list(base_factors)
            routed_factors[target_position] = replace(
                target,
                derivatives=(derivative,) + target.derivatives,
            )
            ledger = branch.external_derivative_ledger
            if target.role is FactorRole.EXTERNAL:
                ledger = ledger + (
                    DerivativeLedgerEntry(
                        step_id=step_id,
                        derivative=derivative,
                        from_factor=source.factor_id,
                        to_factor=target.factor_id,
                        external_leg_id=target.external_leg_id,
                        koszul_sign=koszul_sign,
                    ),
                )
            output.append(
                DAlgebraBranch(
                    coefficient=branch.coefficient * koszul_sign,
                    factors=tuple(routed_factors),
                    external_derivative_ledger=ledger,
                )
            )

        input_derivative_ids = sorted(
            token.op_id for factor in branch.factors for token in factor.derivatives
        )
        factor_order = tuple(factor.factor_id for factor in branch.factors)
        external_ledger_complete = True
        for output_branch, target_position in zip(
            output,
            (position for position in range(len(base_factors)) if position != source_position),
            strict=True,
        ):
            target = base_factors[target_position]
            if target.role is FactorRole.EXTERNAL:
                last = output_branch.external_derivative_ledger[-1]
                external_ledger_complete = external_ledger_complete and (
                    last.derivative.op_id == derivative.op_id
                    and last.external_leg_id == target.external_leg_id
                    and last.to_factor == target.factor_id
                )

        invariants: dict[str, object] = {
            "derivative_id_conservation": all(
                sorted(token.op_id for factor in item.factors for token in factor.derivatives)
                == input_derivative_ids
                for item in output
            ),
            "factor_order_conservation": all(
                tuple(factor.factor_id for factor in item.factors) == factor_order for item in output
            ),
            "total_parity_conservation": all(
                item.total_parity == branch.total_parity for item in output
            ),
            "external_leg_ledger_complete": external_ledger_complete,
            "ibp_branch_count": len(output),
            "expected_ibp_branch_count": max(0, len(branch.factors) - 1),
        }
        if not all(
            bool(invariants[key])
            for key in (
                "derivative_id_conservation",
                "factor_order_conservation",
                "total_parity_conservation",
                "external_leg_ledger_complete",
            )
        ) or invariants["ibp_branch_count"] != invariants["expected_ibp_branch_count"]:
            raise AssertionError("D-algebra IBP invariant failure")

        trace = RewriteTrace(
            step_id=step_id,
            input=branch.canonical_dict(),
            rule=(
                "Integral[Product_i F_i with D_on_F_s] = "
                "-Sum_(j!=s) (-1)^(P_j+P_s) Integral[Product_i F_i with D_on_F_j]"
            ),
            assumptions=self.ASSUMPTIONS,
            koszul_sign=tuple(signs),
            output=tuple(item.canonical_dict() for item in output),
            invariants=invariants,
        )
        self.traces.append(trace)
        return tuple(output), trace


class DescendantNodeType(str, Enum):
    LETTER = "LETTER"
    BASIC_FIELD = "BASIC_FIELD"
    EULER_TOKEN = "EULER_TOKEN"
    COLOR_CROSS = "COLOR_CROSS"
    COVARIANT_DERIVATIVE = "COVARIANT_DERIVATIVE"


class TensorBindingRole(str, Enum):
    CONTRACT_CHILD = "CONTRACT_CHILD"
    OUTPUT_FREE = "OUTPUT_FREE"
    EPSILON_ARGUMENT = "EPSILON_ARGUMENT"


@dataclass(frozen=True)
class TensorIndexBinding:
    tensor_slot: int
    role: TensorBindingRole
    node_path: str
    node_index_space: IndexSpace
    node_index_label: str

    def __post_init__(self) -> None:
        if self.tensor_slot < 0 or not self.node_path or not self.node_index_label:
            raise ValueError("a tensor binding must retain slot, node path, and node index")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "tensor_slot": self.tensor_slot,
            "role": self.role.value,
            "node_path": self.node_path,
            "node_index_space": self.node_index_space.value,
            "node_index_label": self.node_index_label,
        }


@dataclass(frozen=True)
class TypedTensorFactor:
    symbol: str
    ordered_indices: tuple[IndexSlot, ...]
    bindings: tuple[TensorIndexBinding, ...]
    convention: str

    def __post_init__(self) -> None:
        if not self.symbol or not self.convention or not self.ordered_indices:
            raise ValueError("a typed tensor factor needs symbol, indices, and convention")
        if len(self.bindings) != len(self.ordered_indices):
            raise ValueError("every tensor index must have one explicit binding")
        slots = [binding.tensor_slot for binding in self.bindings]
        if sorted(slots) != list(range(len(self.ordered_indices))):
            raise ValueError("tensor bindings must cover every ordered slot exactly once")
        for binding in self.bindings:
            tensor_index = self.ordered_indices[binding.tensor_slot]
            if (
                tensor_index.space is not binding.node_index_space
                or tensor_index.label != binding.node_index_label
            ):
                raise ValueError("tensor slot and bound node index space/label disagree")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "symbol": self.symbol,
            "ordered_indices": [_index_dict(index) for index in self.ordered_indices],
            "bindings": [binding.canonical_dict() for binding in self.bindings],
            "convention": self.convention,
        }


@dataclass(frozen=True)
class DescendantCoefficient:
    rational: Fraction = Fraction(1)
    sqrt2_power: int = 0
    i_power: int = 0

    def __post_init__(self) -> None:
        rational = Fraction(self.rational)
        if self.sqrt2_power < 0:
            raise ValueError("descendant coefficients use nonnegative sqrt(2) powers")
        sqrt_pairs, sqrt_remainder = divmod(self.sqrt2_power, 2)
        rational *= 2**sqrt_pairs
        i_remainder = self.i_power % 4
        if i_remainder == 2:
            rational *= -1
            i_remainder = 0
        elif i_remainder == 3:
            rational *= -1
            i_remainder = 1
        object.__setattr__(self, "rational", rational)
        object.__setattr__(self, "sqrt2_power", sqrt_remainder)
        object.__setattr__(self, "i_power", i_remainder)

    def __mul__(self, other: int | DescendantCoefficient) -> DescendantCoefficient:
        if isinstance(other, int):
            other = DescendantCoefficient(Fraction(other))
        if not isinstance(other, DescendantCoefficient):
            return NotImplemented
        return DescendantCoefficient(
            self.rational * other.rational,
            self.sqrt2_power + other.sqrt2_power,
            self.i_power + other.i_power,
        )

    def canonical_dict(self) -> dict[str, int]:
        return {
            "numerator": self.rational.numerator,
            "denominator": self.rational.denominator,
            "sqrt2_power": self.sqrt2_power,
            "i_power": self.i_power,
        }


@dataclass(frozen=True)
class IndexedDescendantNode:
    node_type: DescendantNodeType
    token: str
    parity: int
    indices: tuple[IndexSlot, ...] = ()
    children: tuple[IndexedDescendantNode, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()
    tensor_factor: TypedTensorFactor | None = None

    def __post_init__(self) -> None:
        if not self.token or self.parity not in (0, 1):
            raise ValueError("an indexed descendant node needs token and Z2 parity")
        _metadata_dict(self.metadata)
        if self.node_type is DescendantNodeType.COLOR_CROSS and len(self.children) != 2:
            raise ValueError("a color cross has exactly two ordered children")
        if self.node_type is DescendantNodeType.COLOR_CROSS and self.tensor_factor is None:
            raise ValueError("a color cross requires a typed structure tensor")
        if self.node_type is not DescendantNodeType.COLOR_CROSS and self.tensor_factor is not None:
            raise ValueError("only a color-cross node owns a structure tensor")
        if self.node_type is DescendantNodeType.COVARIANT_DERIVATIVE and len(self.children) != 1:
            raise ValueError("a covariant derivative has exactly one operand")
        if self.tensor_factor is not None:
            node_indices = {
                "child[0]": self.children[0].indices,
                "child[1]": self.children[1].indices,
                "output": self.indices,
            }
            for binding in self.tensor_factor.bindings:
                if binding.node_path not in node_indices:
                    raise ValueError("structure tensor binding has an invalid node path")
                if not any(
                    index.space is binding.node_index_space
                    and index.label == binding.node_index_label
                    for index in node_indices[binding.node_path]
                ):
                    raise ValueError("structure tensor binding does not resolve on its node")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "node_type": self.node_type.value,
            "token": self.token,
            "parity": self.parity,
            "indices": [_index_dict(index) for index in self.indices],
            "children": [child.canonical_dict() for child in self.children],
            "metadata": dict(self.metadata),
            "tensor_factor": (
                self.tensor_factor.canonical_dict() if self.tensor_factor is not None else None
            ),
        }


@dataclass(frozen=True)
class DescendantTerm:
    intrinsic_coefficient: DescendantCoefficient
    ordered_factors: tuple[IndexedDescendantNode, ...]
    tensor_factors: tuple[TypedTensorFactor, ...]
    koszul_sign: int
    origin: str

    def __post_init__(self) -> None:
        if self.intrinsic_coefficient.rational == 0 or not self.ordered_factors:
            raise ValueError("zero/empty descendant terms are omitted")
        if self.koszul_sign not in (-1, 1):
            raise ValueError("the Leibniz Koszul sign is exactly +1 or -1")
        if not self.origin:
            raise ValueError("a descendant term must retain its Leibniz origin")

    @property
    def parity(self) -> int:
        return sum(factor.parity for factor in self.ordered_factors) % 2

    @property
    def total_coefficient(self) -> DescendantCoefficient:
        return self.intrinsic_coefficient * self.koszul_sign

    @property
    def coefficient(self) -> DescendantCoefficient:
        """Backward-compatible name; always the total signed coefficient."""

        return self.total_coefficient

    def canonical_dict(self) -> dict[str, object]:
        return {
            "coefficient_schema": "TOTAL_EQUALS_KOSZUL_SIGN_TIMES_INTRINSIC",
            "intrinsic_coefficient": self.intrinsic_coefficient.canonical_dict(),
            "intrinsic_coefficient_includes_koszul_sign": False,
            "koszul_sign": self.koszul_sign,
            "total_coefficient": self.total_coefficient.canonical_dict(),
            "total_coefficient_includes_koszul_sign": True,
            "ordered_factors": [factor.canonical_dict() for factor in self.ordered_factors],
            "tensor_factors": [factor.canonical_dict() for factor in self.tensor_factors],
            "origin": self.origin,
            "parity": self.parity,
        }


@dataclass(frozen=True)
class OrderedDescendantAST:
    channel_id: str
    terms: tuple[DescendantTerm, ...]
    expected_parity: int
    source_equations: tuple[str, ...] = ("5.33", "5.34", "5.35")

    def __post_init__(self) -> None:
        if not self.channel_id or self.expected_parity not in (0, 1):
            raise ValueError("an ordered descendant needs channel id and parity")
        if any(term.parity != self.expected_parity for term in self.terms):
            raise ValueError("a channel descendant term has the wrong Z2 parity")

    @property
    def is_zero(self) -> bool:
        return not self.terms

    def canonical_dict(self) -> dict[str, object]:
        return {
            "channel_id": self.channel_id,
            "terms": [term.canonical_dict() for term in self.terms],
            "expected_parity": self.expected_parity,
            "is_zero": self.is_zero,
            "source_equations": list(self.source_equations),
        }


@dataclass(frozen=True)
class LetterPlaceholder:
    family: LetterFamily
    position: str
    color_label: str
    flavor_label: str | None
    spinor_slots: tuple[IndexSlot, ...]
    expression: str

    @property
    def parity(self) -> int:
        return {
            LetterFamily.W: 0,
            LetterFamily.PHI: 1,
            LetterFamily.TILDE_PHI: 0,
            LetterFamily.TILDE_W: 1,
        }[self.family]

    def canonical_dict(self) -> dict[str, object]:
        return {
            "family": self.family.value,
            "position": self.position,
            "color_label": self.color_label,
            "flavor_label": self.flavor_label,
            "spinor_slots": [_index_dict(index) for index in self.spinor_slots],
            "expression": self.expression,
            "parity": self.parity,
        }


@dataclass(frozen=True)
class OrderedFamilyChannel:
    ordinal: int
    channel_id: str
    left: LetterPlaceholder
    right: LetterPlaceholder
    reverse_channel_id: str
    ordered_expression: str
    reversed_expression: str
    descendant: OrderedDescendantAST
    reversed_descendant: OrderedDescendantAST

    def canonical_dict(self) -> dict[str, object]:
        return {
            "ordinal": self.ordinal,
            "channel_id": self.channel_id,
            "left": self.left.canonical_dict(),
            "right": self.right.canonical_dict(),
            "reverse_channel_id": self.reverse_channel_id,
            "ordered_expression": self.ordered_expression,
            "reversed_expression": self.reversed_expression,
            "descendant": self.descendant.canonical_dict(),
            "reversed_descendant": self.reversed_descendant.canonical_dict(),
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_dict(), sort_keys=True, separators=(",", ":"))


def _letter_placeholder(family: LetterFamily, position: str) -> LetterPlaceholder:
    if position not in ("LEFT", "RIGHT"):
        raise ValueError(position)
    color = "A" if position == "LEFT" else "B"
    flavor = "r" if position == "LEFT" else "s"
    dotted = "dot_alpha" if position == "LEFT" else "dot_beta"
    if family is LetterFamily.W:
        return LetterPlaceholder(
            family,
            position,
            color,
            None,
            (
                IndexSlot(IndexSpace.UNDOTTED, "+_nabla", Variance.DOWN),
                IndexSlot(IndexSpace.UNDOTTED, "+_W", Variance.DOWN),
            ),
            f"nabla_+ W_+^{color}",
        )
    if family is LetterFamily.PHI:
        return LetterPlaceholder(
            family,
            position,
            color,
            flavor,
            (IndexSlot(IndexSpace.UNDOTTED, "+_nabla", Variance.DOWN),),
            f"nabla_+ Phi_{flavor}^{color}",
        )
    if family is LetterFamily.TILDE_PHI:
        return LetterPlaceholder(
            family,
            position,
            color,
            flavor,
            (),
            f"TildePhi_{flavor}^{color}",
        )
    return LetterPlaceholder(
        family,
        position,
        color,
        None,
        (IndexSlot(IndexSpace.DOTTED, dotted, Variance.DOWN),),
        f"TildeW^{color}_{dotted}",
    )


@dataclass(frozen=True)
class _SingleDescendantTerm:
    coefficient: DescendantCoefficient
    factor: IndexedDescendantNode
    tensor_factors: tuple[TypedTensorFactor, ...]


def _indexed_node_indices(
    *,
    color: str,
    flavor: str | None = None,
    spinors: Sequence[IndexSlot] = (),
) -> tuple[IndexSlot, ...]:
    indices: list[IndexSlot] = [
        IndexSlot(IndexSpace.COLOR_ADJOINT, color, Variance.UP),
    ]
    if flavor is not None:
        indices.append(IndexSlot(IndexSpace.FLAVOR, flavor, Variance.DOWN))
    indices.extend(spinors)
    return tuple(indices)


def _letter_node(letter: LetterPlaceholder) -> IndexedDescendantNode:
    return IndexedDescendantNode(
        DescendantNodeType.LETTER,
        letter.family.value,
        letter.parity,
        _indexed_node_indices(
            color=letter.color_label,
            flavor=letter.flavor_label,
            spinors=letter.spinor_slots,
        ),
        metadata=(("expression", letter.expression), ("position", letter.position)),
    )


def _basic_field_node(field_name: str, color: str, flavor: str) -> IndexedDescendantNode:
    return IndexedDescendantNode(
        DescendantNodeType.BASIC_FIELD,
        field_name,
        0,
        _indexed_node_indices(color=color, flavor=flavor),
    )


def _cross_node(
    left: IndexedDescendantNode,
    right: IndexedDescendantNode,
    *,
    output_color: str,
    structure_tensor: TypedTensorFactor,
) -> IndexedDescendantNode:
    return IndexedDescendantNode(
        DescendantNodeType.COLOR_CROSS,
        "times",
        (left.parity + right.parity) % 2,
        _indexed_node_indices(color=output_color),
        (left, right),
        (),
        structure_tensor,
    )


def _color_structure_tensor(
    left_color: str,
    right_color: str,
    output_color: str,
) -> TypedTensorFactor:
    return TypedTensorFactor(
        "c",
        (
            IndexSlot(IndexSpace.COLOR_ADJOINT, left_color, Variance.DOWN),
            IndexSlot(IndexSpace.COLOR_ADJOINT, right_color, Variance.DOWN),
            IndexSlot(IndexSpace.COLOR_ADJOINT, output_color, Variance.UP),
        ),
        (
            TensorIndexBinding(
                0,
                TensorBindingRole.CONTRACT_CHILD,
                "child[0]",
                IndexSpace.COLOR_ADJOINT,
                left_color,
            ),
            TensorIndexBinding(
                1,
                TensorBindingRole.CONTRACT_CHILD,
                "child[1]",
                IndexSpace.COLOR_ADJOINT,
                right_color,
            ),
            TensorIndexBinding(
                2,
                TensorBindingRole.OUTPUT_FREE,
                "output",
                IndexSpace.COLOR_ADJOINT,
                output_color,
            ),
        ),
        "c_{AB}{}^C with ordered variances DOWN,DOWN,UP",
    )


def _epsilon_flavor_tensor(
    free_flavor: str,
    left_flavor: str,
    right_flavor: str,
) -> TypedTensorFactor:
    return TypedTensorFactor(
        "epsilon",
        (
            IndexSlot(IndexSpace.FLAVOR, free_flavor, Variance.DOWN),
            IndexSlot(IndexSpace.FLAVOR, left_flavor, Variance.DOWN),
            IndexSlot(IndexSpace.FLAVOR, right_flavor, Variance.DOWN),
        ),
        (
            TensorIndexBinding(
                0,
                TensorBindingRole.OUTPUT_FREE,
                "descendant_output",
                IndexSpace.FLAVOR,
                free_flavor,
            ),
            TensorIndexBinding(
                1,
                TensorBindingRole.EPSILON_ARGUMENT,
                "cross.child[0]",
                IndexSpace.FLAVOR,
                left_flavor,
            ),
            TensorIndexBinding(
                2,
                TensorBindingRole.EPSILON_ARGUMENT,
                "cross.child[1]",
                IndexSpace.FLAVOR,
                right_flavor,
            ),
        ),
        "Project epsilon_{rst} with ordered flavor variances DOWN,DOWN,DOWN",
    )


def _nabla_plus_node(operand: IndexedDescendantNode) -> IndexedDescendantNode:
    return IndexedDescendantNode(
        DescendantNodeType.COVARIANT_DERIVATIVE,
        "nabla_+",
        (operand.parity + 1) % 2,
        operand.indices,
        (operand,),
        (("derivative_index", "+"),),
    )


def _single_letter_descendant(letter: LetterPlaceholder) -> tuple[_SingleDescendantTerm, ...]:
    output_color = letter.color_label
    internal_colors = ("C", "D") if output_color == "A" else ("E", "F")
    if letter.family is LetterFamily.W:
        euler = IndexedDescendantNode(
            DescendantNodeType.EULER_TOKEN,
            "G",
            0,
            _indexed_node_indices(color=output_color),
            metadata=(("euler_equation", "5.27"),),
        )
        phi = _basic_field_node("Phi", internal_colors[0], "u")
        tilde_phi = _basic_field_node("TildePhi", internal_colors[1], "u")
        structure = _color_structure_tensor(
            internal_colors[0],
            internal_colors[1],
            output_color,
        )
        cross = _cross_node(
            phi,
            tilde_phi,
            output_color=output_color,
            structure_tensor=structure,
        )
        return (
            _SingleDescendantTerm(
                DescendantCoefficient(Fraction(-1)),
                _nabla_plus_node(euler),
                (),
            ),
            _SingleDescendantTerm(
                DescendantCoefficient(Fraction(-2), i_power=1),
                _nabla_plus_node(cross),
                (structure,),
            ),
        )
    if letter.family is LetterFamily.PHI:
        assert letter.flavor_label is not None
        euler = IndexedDescendantNode(
            DescendantNodeType.EULER_TOKEN,
            "TildeC",
            0,
            _indexed_node_indices(color=output_color, flavor=letter.flavor_label),
            metadata=(("euler_equation", "5.27"),),
        )
        tilde_phi_u = _basic_field_node("TildePhi", internal_colors[0], "u")
        tilde_phi_v = _basic_field_node("TildePhi", internal_colors[1], "v")
        structure = _color_structure_tensor(
            internal_colors[0],
            internal_colors[1],
            output_color,
        )
        epsilon = _epsilon_flavor_tensor(letter.flavor_label, "u", "v")
        cross = _cross_node(
            tilde_phi_u,
            tilde_phi_v,
            output_color=output_color,
            structure_tensor=structure,
        )
        return (
            _SingleDescendantTerm(DescendantCoefficient(Fraction(1, 2)), euler, ()),
            _SingleDescendantTerm(
                DescendantCoefficient(Fraction(-1), sqrt2_power=1),
                cross,
                (epsilon, structure),
            ),
        )
    return ()


def _ordered_product_descendant(
    left: LetterPlaceholder,
    right: LetterPlaceholder,
    *,
    channel_id: str,
) -> OrderedDescendantAST:
    terms: list[DescendantTerm] = []
    right_letter = _letter_node(right)
    for single in _single_letter_descendant(left):
        terms.append(
            DescendantTerm(
                single.coefficient,
                (single.factor, right_letter),
                single.tensor_factors,
                1,
                "LEFT_DESCENDANT",
            )
        )
    left_letter = _letter_node(left)
    right_koszul_sign = -1 if left.parity else 1
    for single in _single_letter_descendant(right):
        terms.append(
            DescendantTerm(
                single.coefficient,
                (left_letter, single.factor),
                single.tensor_factors,
                right_koszul_sign,
                "RIGHT_DESCENDANT:(-1)^LEFT_PARITY",
            )
        )
    return OrderedDescendantAST(
        channel_id,
        tuple(terms),
        (left.parity + right.parity + 1) % 2,
    )


def emit_ordered_family_channels() -> tuple[OrderedFamilyChannel, ...]:
    """Emit the 4 x 4 ordered family grid without quotienting by reversal."""

    families = (
        LetterFamily.W,
        LetterFamily.PHI,
        LetterFamily.TILDE_PHI,
        LetterFamily.TILDE_W,
    )
    channels: list[OrderedFamilyChannel] = []
    ordinal = 1
    for left_family in families:
        for right_family in families:
            left = _letter_placeholder(left_family, "LEFT")
            right = _letter_placeholder(right_family, "RIGHT")
            channel_id = f"{left_family.value}__{right_family.value}"
            reverse_channel_id = f"{right_family.value}__{left_family.value}"
            channels.append(
                OrderedFamilyChannel(
                    ordinal=ordinal,
                    channel_id=channel_id,
                    left=left,
                    right=right,
                    reverse_channel_id=reverse_channel_id,
                    ordered_expression=f"({left.expression}) ({right.expression})",
                    reversed_expression=f"({right.expression}) ({left.expression})",
                    descendant=_ordered_product_descendant(
                        left,
                        right,
                        channel_id=channel_id,
                    ),
                    reversed_descendant=_ordered_product_descendant(
                        right,
                        left,
                        channel_id=f"reverse_of__{channel_id}",
                    ),
                )
            )
            ordinal += 1
    if len(channels) != 16 or len({channel.channel_id for channel in channels}) != 16:
        raise AssertionError("the ordered family emitter must produce exactly sixteen classes")
    return tuple(channels)


def canonical_channel_catalog_json() -> str:
    """Serialize all sixteen indexed descendants and their fixed-label reversals."""

    return json.dumps(
        [channel.canonical_dict() for channel in emit_ordered_family_channels()],
        sort_keys=True,
        separators=(",", ":"),
    )


def _index_dict(index: IndexSlot) -> dict[str, str]:
    return {
        "space": index.space.value,
        "label": index.label,
        "variance": index.variance.value,
    }


def _derivative_dict(token: DerivativeToken) -> dict[str, object]:
    return {
        "op_id": token.op_id,
        "kind": token.kind.value,
        "index": _index_dict(token.index),
        "origin": token.origin,
    }


def _field_type_dict(field_type: FieldType) -> dict[str, object]:
    return {
        "name": field_type.name,
        "statistics": field_type.statistics.value,
        "chirality": field_type.chirality.value,
        "indices": [_index_dict(index) for index in field_type.indices],
        "color_representation": field_type.color_representation,
    }


def _half_edge_word(half_edge: HalfEdge) -> str:
    derivatives = ",".join(token.render() for token in half_edge.derivatives) or "identity"
    return f"{half_edge.half_edge_id}{{{derivatives}}}"


__all__ = [
    "AllowedContraction",
    "Chirality",
    "DAlgebraBranch",
    "DAlgebraEngine",
    "DAlgebraFactor",
    "DescendantCoefficient",
    "DescendantNodeType",
    "DescendantTerm",
    "DerivativeKind",
    "DerivativeLedgerEntry",
    "DerivativeToken",
    "ExternalLeg",
    "FactorRole",
    "FieldType",
    "Flow",
    "GraphIR",
    "HalfEdge",
    "IndexSlot",
    "IndexSpace",
    "IndexedDescendantNode",
    "InternalEdge",
    "LetterFamily",
    "LetterPlaceholder",
    "OrderedFamilyChannel",
    "OrderedDescendantAST",
    "PropagatorGrammar",
    "RewriteTrace",
    "Statistics",
    "TensorBindingRole",
    "TensorIndexBinding",
    "TypedTensorFactor",
    "Variance",
    "Vertex",
    "WickPair",
    "WickPairing",
    "canonical_channel_catalog_json",
    "emit_ordered_family_channels",
    "enumerate_wick_pairings",
    "parse_linear_momentum",
    "render_linear_momentum",
]
