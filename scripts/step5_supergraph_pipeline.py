#!/usr/bin/env python3
"""Connected partially-contracted supergraph -> amplitude pipeline.

This module deliberately separates three layers:

1. a physical request with ordered, typed quantum/external ports;
2. exact Wick enumeration and connected one-loop graph construction;
3. a factorized pre-integration amplitude and a textbook renderer.

The WW fixture is the already-derived Project seed.  The matter fixture is
structural: its oriented chiral edge remains a named exact symbol and is not
assigned an unproved superfield normalization.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
import re
from typing import Iterable, Mapping, Sequence

from scripts import step5_pipeline_ir as pipeline_ir

from scripts.step5_graph_ir import (
    AllowedContraction,
    Chirality,
    ExternalLeg,
    FieldType,
    Flow,
    GraphIR,
    HalfEdge,
    IndexSlot,
    IndexSpace,
    InternalEdge,
    PropagatorGrammar,
    Statistics,
    Variance,
    Vertex,
    WickPair,
    WickPairing,
    enumerate_wick_pairings,
)
from scripts.step5_vertex_grammar import ExactCoefficient, matter_bridge_monomials


class RequestKind(str, Enum):
    PHYSICAL_PARTIAL_CONTRACTION = "PHYSICAL_PARTIAL_CONTRACTION"
    STRUCTURAL_PARTIAL_CONTRACTION = "STRUCTURAL_PARTIAL_CONTRACTION"
    VALENCE_ONLY_REQUEST = "VALENCE_ONLY_REQUEST"


class PortRole(str, Enum):
    QUANTUM_WICK = "QUANTUM_WICK"
    EXTERNAL = "EXTERNAL"


class VertexRole(str, Enum):
    INSERTION = "INSERTION"
    ACTION = "ACTION"


class ValenceOnlyRequestError(ValueError):
    pass


def _coefficient_dict(coefficient: ExactCoefficient) -> dict[str, object]:
    return {
        "numerator": coefficient.rational.numerator,
        "denominator": coefficient.rational.denominator,
        "sqrt2_power": coefficient.sqrt2_power,
        "i_power": coefficient.i_power,
        "symbols": list(coefficient.symbols),
        "rendered": coefficient.render(),
    }


def _index_dict(index: IndexSlot) -> dict[str, str]:
    return {
        "space": index.space.value,
        "label": index.label,
        "variance": index.variance.value,
    }


@dataclass(frozen=True)
class PortSpec:
    port_id: str
    field_type: FieldType
    role: PortRole
    flow: Flow
    incoming_momentum: str
    color_label: str
    flavor_label: str | None = None
    physical_external_momentum: str | None = None
    spinor_indices: tuple[IndexSlot, ...] = ()
    operator_derivatives: tuple = ()
    origin: str = ""
    notation_port_spec: str = ""
    notation_sector: str = ""

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.port_id,
                self.incoming_momentum,
                self.color_label,
                self.origin,
                self.notation_port_spec,
                self.notation_sector,
            )
        ):
            raise ValueError(
                "every port needs id, momentum, color, origin, and explicit notation typing"
            )
        try:
            pipeline_ir.PortSector(self.notation_sector)
        except ValueError as exc:
            raise ValueError(f"unknown notation sector {self.notation_sector}") from exc
        if self.role is PortRole.EXTERNAL and self.physical_external_momentum is None:
            raise ValueError("an external port needs its physical momentum")
        if self.role is PortRole.QUANTUM_WICK and self.physical_external_momentum is not None:
            raise ValueError("a quantum port cannot carry an external momentum label")


@dataclass(frozen=True)
class VertexSpec:
    vertex_id: str
    role: VertexRole
    kind: str
    coefficient: ExactCoefficient
    ordered_ports: tuple[PortSpec, ...]
    color_word: tuple[str, ...]
    superspace_point: str
    momentum_delta: str
    momentum_injection: str
    operator_factors: tuple[str, ...]
    origins: tuple[str, ...]

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.vertex_id,
                self.kind,
                self.superspace_point,
                self.momentum_delta,
                self.momentum_injection,
            )
        ):
            raise ValueError("a vertex specification is incomplete")
        if not self.ordered_ports or not self.origins:
            raise ValueError("a vertex needs ordered ports and Project origins")
        if len({port.port_id for port in self.ordered_ports}) != len(self.ordered_ports):
            raise ValueError("port ids are unique within a vertex")


@dataclass(frozen=True)
class PropagatorSpec:
    rule_id: str
    left_field_name: str
    right_field_name: str
    oriented: bool
    coefficient: ExactCoefficient
    kernel_template: str
    color_tensor: str
    flavor_tensor: str | None
    normalization_status: str
    origins: tuple[str, ...]
    left_notation_port_spec: str
    right_notation_port_spec: str

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.rule_id,
                self.left_field_name,
                self.right_field_name,
                self.kernel_template,
                self.color_tensor,
                self.normalization_status,
                self.left_notation_port_spec,
                self.right_notation_port_spec,
            )
        ) or not self.origins:
            raise ValueError("a propagator specification is incomplete")

    def contraction_rule(self) -> AllowedContraction:
        return AllowedContraction(
            self.rule_id,
            self.left_field_name,
            self.right_field_name,
            self.kernel_template,
            self.oriented,
        )

    def validate_ports(self, left: PortSpec, right: PortSpec) -> None:
        exact = (
            left.field_type.name == self.left_field_name
            and right.field_type.name == self.right_field_name
        )
        reverse = (
            left.field_type.name == self.right_field_name
            and right.field_type.name == self.left_field_name
        )
        if self.oriented and not exact:
            raise ValueError(f"{self.rule_id} requires the declared left-to-right orientation")
        if not self.oriented and not (exact or reverse):
            raise ValueError(f"{self.rule_id} has incompatible endpoint fields")
        if left.field_type.parity != right.field_type.parity:
            raise ValueError("a propagator cannot join unequal Grassmann parities")
        if self.flavor_tensor is not None and left.flavor_label != right.flavor_label:
            raise ValueError("a flavor-diagonal propagator has unequal endpoint flavors")


@dataclass(frozen=True)
class MomentumBinding:
    binding_id: str
    rule_id: str
    left_port_id: str
    right_port_id: str
    momentum: str

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.binding_id,
                self.rule_id,
                self.left_port_id,
                self.right_port_id,
                self.momentum,
            )
        ):
            raise ValueError("a momentum binding is incomplete")
        if self.left_port_id == self.right_port_id:
            raise ValueError("a propagator binding needs two distinct ports")


@dataclass(frozen=True)
class DiagramRequest:
    request_id: str
    request_kind: RequestKind
    vertices: tuple[VertexSpec, ...]
    propagators: tuple[PropagatorSpec, ...]
    momentum_bindings: tuple[MomentumBinding, ...]
    loop_momentum: str
    coefficient_relations: tuple[tuple[str, str], ...]
    origins: tuple[str, ...]
    schema_hash: str
    orientation: str
    external_fermion_word: tuple[str, ...]
    external_koszul_sign: int
    orientation_sign_ledger: tuple[tuple[str, int], ...] = (
        ("external_subword", 1),
        ("quantum_subword", 1),
    )

    def __post_init__(self) -> None:
        if any(
            not value
            for value in (
                self.request_id,
                self.loop_momentum,
                self.origins,
                self.schema_hash,
                self.orientation,
            )
        ):
            raise ValueError(
                "a request needs id, loop momentum, origins, schema hash, and orientation"
            )
        if self.external_koszul_sign not in (-1, 1):
            raise ValueError("an external Koszul sign must be +1 or -1")
        sign_ledger = dict(self.orientation_sign_ledger)
        if set(sign_ledger) != {"external_subword", "quantum_subword"}:
            raise ValueError(
                "the orientation sign ledger needs external and quantum subwords"
            )
        if any(value not in (-1, 1) for value in sign_ledger.values()):
            raise ValueError("every orientation sub-sign is exactly +1 or -1")
        if (
            sign_ledger["external_subword"] * sign_ledger["quantum_subword"]
            != self.external_koszul_sign
        ):
            raise ValueError("orientation sub-signs do not multiply to the total sign")
        if len({vertex.vertex_id for vertex in self.vertices}) != len(self.vertices):
            raise ValueError("vertex ids are globally unique")
        port_ids = [port.port_id for vertex in self.vertices for port in vertex.ordered_ports]
        if len(port_ids) != len(set(port_ids)):
            raise ValueError("port ids are globally unique")
        if len({item.rule_id for item in self.propagators}) != len(self.propagators):
            raise ValueError("propagator rule ids are unique")
        if len({item.binding_id for item in self.momentum_bindings}) != len(
            self.momentum_bindings
        ):
            raise ValueError("momentum binding ids are unique")


@dataclass(frozen=True)
class AmplitudeFactor:
    factor_id: str
    category: str
    expression: str
    coefficient: ExactCoefficient
    origins: tuple[str, ...]
    metadata: tuple[tuple[str, str], ...] = ()

    def canonical_dict(self) -> dict[str, object]:
        return {
            "factor_id": self.factor_id,
            "category": self.category,
            "expression": self.expression,
            "coefficient": _coefficient_dict(self.coefficient),
            "origins": list(self.origins),
            "metadata": dict(self.metadata),
        }


@dataclass(frozen=True)
class AmplitudeRecord:
    amplitude_id: str
    request_id: str
    schema_hash: str
    orientation: str
    external_fermion_word: tuple[str, ...]
    external_koszul_sign: int
    orientation_sign_ledger: tuple[tuple[str, int], ...]
    graph: GraphIR
    canonical_key: str
    orientation_signature: tuple[str, ...]
    class_multiplicity: int
    wick_koszul_sign: int
    automorphism_order: int
    automorphism_symmetry_factor: Fraction
    factors: tuple[AmplitudeFactor, ...]
    exact_coefficient_raw: ExactCoefficient
    exact_coefficient_reduced: ExactCoefficient
    coefficient_reduction_trace: tuple[str, ...]
    normalization_status: str

    def canonical_dict(self) -> dict[str, object]:
        return {
            "amplitude_id": self.amplitude_id,
            "request_id": self.request_id,
            "schema_hash": self.schema_hash,
            "orientation": self.orientation,
            "external_fermion_word": list(self.external_fermion_word),
            "external_koszul_sign": self.external_koszul_sign,
            "orientation_sign_ledger": dict(self.orientation_sign_ledger),
            "canonical_key": self.canonical_key,
            "orientation_signature": list(self.orientation_signature),
            "class_multiplicity": self.class_multiplicity,
            "wick_koszul_sign": self.wick_koszul_sign,
            "automorphism_order": self.automorphism_order,
            "automorphism_symmetry_factor": {
                "numerator": self.automorphism_symmetry_factor.numerator,
                "denominator": self.automorphism_symmetry_factor.denominator,
            },
            "automorphism_factor_policy": (
                "AUDIT_ONLY_CLASS_ALREADY_SUMS_LABELED_PAIRINGS"
            ),
            "factors": [factor.canonical_dict() for factor in self.factors],
            "exact_coefficient_raw": _coefficient_dict(self.exact_coefficient_raw),
            "exact_coefficient_reduced": _coefficient_dict(self.exact_coefficient_reduced),
            "coefficient_reduction_trace": list(self.coefficient_reduction_trace),
            "normalization_status": self.normalization_status,
            "preintegration_product": " * ".join(
                factor.factor_id
                for factor in self.factors
                if not factor.category.endswith("AUDIT_ONLY")
            ),
            "audit_factors": [
                factor.factor_id
                for factor in self.factors
                if factor.category.endswith("AUDIT_ONLY")
            ],
            "graph": self.graph.canonical_dict(),
            "renderers": {
                "dot": self.graph.to_dot(),
                "mermaid": self.graph.to_mermaid(),
            },
        }


@dataclass(frozen=True)
class CompilationResult:
    request_id: str
    request_kind: RequestKind
    schema_hash: str
    typed_pairings: int
    endpoint_admissible_pairings: int
    rejected_disconnected: int
    rejected_non_one_loop: int
    isomorphism_classes: int
    accepted_pairings_reconstructed: int
    amplitudes: tuple[AmplitudeRecord, ...]

    def canonical_dict(self) -> dict[str, object]:
        return {
            "request_id": self.request_id,
            "request_kind": self.request_kind.value,
            "schema_hash": self.schema_hash,
            "completeness": {
                "typed_pairings": self.typed_pairings,
                "endpoint_admissible_pairings": self.endpoint_admissible_pairings,
                "rejected_disconnected": self.rejected_disconnected,
                "rejected_non_one_loop": self.rejected_non_one_loop,
                "isomorphism_classes": self.isomorphism_classes,
                "accepted_pairings_reconstructed": self.accepted_pairings_reconstructed,
                "no_double_count": (
                    self.accepted_pairings_reconstructed
                    == self.endpoint_admissible_pairings
                    - self.rejected_disconnected
                    - self.rejected_non_one_loop
                ),
            },
            "amplitudes": [item.canonical_dict() for item in self.amplitudes],
        }


_DERIVATIVE_SURFACES: tuple[tuple[str, str], ...] = (
    ("barD^dot_alpha", "barD_dot_alpha"),
    ("barD_dot_alpha", "barD_dot_alpha"),
    ("nabla_+", "nabla_+"),
    ("nabla_-", "nabla_-"),
    ("barD^2", "barD2"),
    ("barD2", "barD2"),
    ("D_+", "D_+"),
    ("D_-", "D_-"),
    ("D_a", "D_a"),
    ("D^2", "D2"),
    ("D2", "D2"),
    ("K_+", "K_+"),
)

_RESIDUAL_DERIVATIVE = re.compile(
    r"(?:nabla|barD|D|K)(?:_|\^)[A-Za-z0-9_+\-.]+|(?:barD|D)2"
)

_TENSOR_SURFACES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bkappa(?:\[|\^|_)"), "kappa"),
    (re.compile(r"\bc(?:\[|_)"), "c"),
    (re.compile(r"\bdelta4theta\b"), "delta4theta"),
    (re.compile(r"delta_\{rs\}"), "delta_flavor"),
)

_MOMENTUM_IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*")


def _require_schema_names(
    names: Iterable[str],
    available: Mapping[str, object],
    context: str,
) -> None:
    for name in names:
        if name not in available:
            raise pipeline_ir.UndefinedSymbolError(
                f"{context} references undefined notation name {name}"
            )


def _extract_derivative_names(expression: str) -> tuple[str, ...]:
    """Extract the fixed Step-5 derivative vocabulary and reject unknown operators."""

    residual = expression
    found: list[str] = []
    # Longest surfaces are removed first so ``barD_dot_alpha`` is one token.
    for surface, notation_name in sorted(
        _DERIVATIVE_SURFACES,
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        count = residual.count(surface)
        if count:
            found.extend([notation_name] * count)
            residual = residual.replace(surface, " " * len(surface))
    unknown = _RESIDUAL_DERIVATIVE.findall(residual)
    if unknown:
        raise pipeline_ir.UndefinedSymbolError(
            "operator factor contains unsupported derivative token(s): "
            + ", ".join(sorted(set(unknown)))
        )
    return tuple(found)


def _derivative_token_name(token: object) -> str:
    kind = getattr(token, "kind", None)
    index = getattr(token, "index", None)
    label = getattr(index, "label", None)
    if kind is None or label is None:
        raise pipeline_ir.PipelineIRError("an operator derivative token is not typed")
    head = "D" if getattr(kind, "value", "") == "D" else "barD"
    aliases = {
        ("D", "+"): "D_+",
        ("D", "-"): "D_-",
        ("D", "a"): "D_a",
        ("barD", "dot_alpha"): "barD_dot_alpha",
    }
    name = aliases.get((head, label))
    if name is None:
        raise pipeline_ir.UndefinedSymbolError(
            f"operator derivative token {head}[{label}] has no fixed notation name"
        )
    return name


def _tensor_names(expression: str) -> tuple[str, ...]:
    return tuple(name for pattern, name in _TENSOR_SURFACES if pattern.search(expression))


def _validate_momentum_expression(
    expression: str,
    schema: pipeline_ir.NotationSchema,
    context: str,
    *,
    allow_delta: bool = False,
) -> None:
    identifiers = _MOMENTUM_IDENTIFIER.findall(expression)
    if allow_delta:
        identifiers = [name for name in identifiers if name != "delta"]
    momentum_symbols = {
        name: spec
        for name, spec in schema.symbol_map.items()
        if spec.kind is pipeline_ir.SymbolKind.MOMENTUM
    }
    _require_schema_names(identifiers, momentum_symbols, context)


def _exact_numeric_qi(coefficient: ExactCoefficient) -> pipeline_ir.Qi:
    if coefficient.sqrt2_power != 0:
        raise pipeline_ir.PipelineIRError(
            "a propagator coefficient with sqrt(2) power cannot equal a Q(i) schema coefficient"
        )
    phase = coefficient.i_power % 4
    if phase == 0:
        return pipeline_ir.Qi(coefficient.rational, Fraction(0))
    if phase == 1:
        return pipeline_ir.Qi(Fraction(0), coefficient.rational)
    if phase == 2:
        return pipeline_ir.Qi(-coefficient.rational, Fraction(0))
    return pipeline_ir.Qi(Fraction(0), -coefficient.rational)


def _validate_field_type(
    field_type: FieldType,
    schema: pipeline_ir.NotationSchema,
    context: str,
) -> None:
    if field_type.name not in schema.field_map:
        raise pipeline_ir.UndefinedSymbolError(
            f"{context} uses undefined field {field_type.name}"
        )
    declared = schema.field_map[field_type.name]
    if declared.statistics.value != field_type.statistics.value:
        raise pipeline_ir.PipelineIRError(
            f"{context} statistics disagree for field {field_type.name}"
        )
    if declared.chirality.value != field_type.chirality.value:
        raise pipeline_ir.PipelineIRError(
            f"{context} chirality disagrees for field {field_type.name}"
        )
    actual_spaces = tuple(index.space.value for index in field_type.indices)
    if declared.index_spaces != actual_spaces:
        raise pipeline_ir.PipelineIRError(
            f"{context} index spaces {actual_spaces} != {declared.index_spaces}"
        )
    actual_variances = tuple(
        pipeline_ir.Variance(index.variance.value) for index in field_type.indices
    )
    if declared.index_variances != actual_variances:
        raise pipeline_ir.PipelineIRError(
            f"{context} index variances {actual_variances} "
            f"!= {declared.index_variances}"
        )


def _validate_request_against_schema(
    request: DiagramRequest,
    schema: pipeline_ir.NotationSchema,
) -> None:
    if not isinstance(schema, pipeline_ir.NotationSchema):
        raise TypeError("compile_request requires an explicit NotationSchema")
    schema.assert_canonical_hash(request.schema_hash)

    _validate_momentum_expression(request.loop_momentum, schema, "loop momentum")
    relation_symbols = tuple(name for pair in request.coefficient_relations for name in pair)
    _require_schema_names(relation_symbols, schema.symbol_map, "coefficient relation")
    request_ports = {
        port.port_id: port
        for vertex in request.vertices
        for port in vertex.ordered_ports
    }
    request_field_types = {
        port.field_type.name: port.field_type for port in request_ports.values()
    }

    for vertex in request.vertices:
        _require_schema_names(
            vertex.coefficient.symbols,
            schema.symbol_map,
            f"vertex {vertex.vertex_id} exact coefficient",
        )
        _validate_momentum_expression(
            vertex.momentum_injection,
            schema,
            f"vertex {vertex.vertex_id} momentum injection",
        )
        _validate_momentum_expression(
            vertex.momentum_delta,
            schema,
            f"vertex {vertex.vertex_id} momentum delta",
            allow_delta=True,
        )
        for factor in vertex.operator_factors:
            derivatives = _extract_derivative_names(factor)
            _require_schema_names(
                derivatives,
                schema.derivative_map,
                f"vertex {vertex.vertex_id} operator factor",
            )
        for tensor_name in _tensor_names(" ".join(vertex.color_word)):
            _require_schema_names(
                (tensor_name,),
                schema.tensor_map,
                f"vertex {vertex.vertex_id} color word",
            )
        for port in vertex.ordered_ports:
            _validate_field_type(port.field_type, schema, f"port {port.port_id}")
            if port.notation_port_spec not in schema.port_map:
                raise pipeline_ir.UndefinedSymbolError(
                    f"port {port.port_id} uses undefined port spec {port.notation_port_spec}"
                )
            notation_port = schema.port_map[port.notation_port_spec]
            if notation_port.field_name != port.field_type.name:
                raise pipeline_ir.PipelineIRError(
                    f"port {port.port_id} field {port.field_type.name} != "
                    f"{notation_port.field_name} from {port.notation_port_spec}"
                )
            sector = pipeline_ir.PortSector(port.notation_sector)
            notation_flow = pipeline_ir.Flow(port.flow.value)
            if sector not in notation_port.allowed_sectors:
                raise pipeline_ir.PropagatorPortError(
                    f"port {port.port_id} sector {sector.value} violates {port.notation_port_spec}"
                )
            if notation_flow not in notation_port.allowed_flows:
                raise pipeline_ir.PropagatorPortError(
                    f"port {port.port_id} flow {notation_flow.value} violates {port.notation_port_spec}"
                )
            _validate_momentum_expression(
                port.incoming_momentum,
                schema,
                f"port {port.port_id} incoming momentum",
            )
            if port.physical_external_momentum is not None:
                _validate_momentum_expression(
                    port.physical_external_momentum,
                    schema,
                    f"port {port.port_id} external momentum",
                )
            derivative_names = tuple(
                _derivative_token_name(token) for token in port.operator_derivatives
            )
            _require_schema_names(
                derivative_names,
                schema.derivative_map,
                f"port {port.port_id} derivative word",
            )

    for propagator in request.propagators:
        if propagator.rule_id not in schema.propagator_map:
            raise pipeline_ir.UndefinedSymbolError(
                f"undefined propagator {propagator.rule_id}"
            )
        _require_schema_names(
            (propagator.left_field_name, propagator.right_field_name),
            request_field_types,
            f"propagator {propagator.rule_id} request fields",
        )
        _validate_field_type(
            request_field_types[propagator.left_field_name],
            schema,
            f"propagator {propagator.rule_id} left field",
        )
        _validate_field_type(
            request_field_types[propagator.right_field_name],
            schema,
            f"propagator {propagator.rule_id} right field",
        )
        declared = schema.propagator_map[propagator.rule_id]
        if not declared.accepts(
            propagator.left_notation_port_spec,
            propagator.right_notation_port_spec,
        ):
            raise pipeline_ir.PropagatorPortError(
                f"propagator {propagator.rule_id} ports "
                f"{propagator.left_notation_port_spec}, {propagator.right_notation_port_spec} "
                "disagree with the notation schema"
            )
        if declared.symmetric == propagator.oriented:
            raise pipeline_ir.PropagatorPortError(
                f"propagator {propagator.rule_id} orientation/symmetry disagrees with schema"
            )
        if _exact_numeric_qi(propagator.coefficient) != declared.coefficient:
            raise pipeline_ir.PipelineIRError(
                f"propagator {propagator.rule_id} numeric coefficient disagrees with schema"
            )
        _require_schema_names(
            propagator.coefficient.symbols,
            schema.symbol_map,
            f"propagator {propagator.rule_id} exact coefficient",
        )
        if tuple(sorted(propagator.coefficient.symbols)) != tuple(
            sorted(declared.symbol_factors)
        ):
            raise pipeline_ir.PipelineIRError(
                f"propagator {propagator.rule_id} exact symbolic factors "
                f"{propagator.coefficient.symbols} != {declared.symbol_factors}"
            )
        tensor_expression = " ".join(
            item
            for item in (
                propagator.kernel_template,
                propagator.color_tensor,
                propagator.flavor_tensor,
            )
            if item is not None
        )
        tensor_names = _tensor_names(tensor_expression)
        _require_schema_names(
            tensor_names,
            schema.tensor_map,
            f"propagator {propagator.rule_id} tensor factors",
        )
        if tuple(sorted(set(tensor_names))) != tuple(sorted(set(declared.tensor_factors))):
            raise pipeline_ir.PipelineIRError(
                f"propagator {propagator.rule_id} tensor factors "
                f"{tuple(sorted(set(tensor_names)))} != {tuple(sorted(set(declared.tensor_factors)))}"
            )

    known_ports = set(request_ports)
    known_rules = {item.rule_id for item in request.propagators}
    request_propagators = {item.rule_id: item for item in request.propagators}
    for binding in request.momentum_bindings:
        _require_schema_names((binding.rule_id,), {name: None for name in known_rules}, "binding")
        _require_schema_names(
            (binding.left_port_id, binding.right_port_id),
            {name: None for name in known_ports},
            f"binding {binding.binding_id}",
        )
        _validate_momentum_expression(
            binding.momentum,
            schema,
            f"binding {binding.binding_id} momentum",
        )
        propagator = request_propagators[binding.rule_id]
        left = request_ports[binding.left_port_id]
        right = request_ports[binding.right_port_id]
        propagator.validate_ports(left, right)
        notation_exact = (
            left.notation_port_spec == propagator.left_notation_port_spec
            and right.notation_port_spec == propagator.right_notation_port_spec
        )
        notation_reverse = (
            not propagator.oriented
            and left.notation_port_spec == propagator.right_notation_port_spec
            and right.notation_port_spec == propagator.left_notation_port_spec
        )
        if not (notation_exact or notation_reverse):
            raise pipeline_ir.PropagatorPortError(
                f"binding {binding.binding_id} endpoint port specs disagree with "
                f"propagator {binding.rule_id}"
            )


def _port_maps(
    request: DiagramRequest,
) -> tuple[dict[str, PortSpec], dict[str, str], dict[str, int]]:
    ports: dict[str, PortSpec] = {}
    vertex_by_port: dict[str, str] = {}
    slot_by_port: dict[str, int] = {}
    for vertex in request.vertices:
        for slot, port in enumerate(vertex.ordered_ports):
            ports[port.port_id] = port
            vertex_by_port[port.port_id] = vertex.vertex_id
            slot_by_port[port.port_id] = slot
    return ports, vertex_by_port, slot_by_port


def _binding_for_pair(
    pair: WickPair,
    request: DiagramRequest,
    propagators: Mapping[str, PropagatorSpec],
) -> MomentumBinding | None:
    spec = propagators[pair.rule_id]
    for binding in request.momentum_bindings:
        if binding.rule_id != pair.rule_id:
            continue
        if spec.oriented:
            if (
                pair.left_half_edge == binding.left_port_id
                and pair.right_half_edge == binding.right_port_id
            ):
                return binding
        elif {pair.left_half_edge, pair.right_half_edge} == {
            binding.left_port_id,
            binding.right_port_id,
        }:
            return binding
    return None


def _pairing_bindings(
    pairing: WickPairing,
    request: DiagramRequest,
    propagators: Mapping[str, PropagatorSpec],
) -> tuple[MomentumBinding, ...] | None:
    result: list[MomentumBinding] = []
    used: set[str] = set()
    for pair in pairing.pairs:
        binding = _binding_for_pair(pair, request, propagators)
        if binding is None or binding.binding_id in used:
            return None
        used.add(binding.binding_id)
        result.append(binding)
    return tuple(sorted(result, key=lambda item: item.binding_id))


def _connected_one_loop(
    request: DiagramRequest,
    pairing: WickPairing,
    vertex_by_port: Mapping[str, str],
) -> tuple[bool, int]:
    adjacency = {vertex.vertex_id: set() for vertex in request.vertices}
    for pair in pairing.pairs:
        left = vertex_by_port[pair.left_half_edge]
        right = vertex_by_port[pair.right_half_edge]
        adjacency[left].add(right)
        adjacency[right].add(left)
    visited: set[str] = set()
    stack = [request.vertices[0].vertex_id]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        stack.extend(adjacency[vertex] - visited)
    connected = visited == set(adjacency)
    loop_number = len(pairing.pairs) - len(request.vertices) + 1 if connected else -1
    return connected, loop_number


def _build_graph(
    request: DiagramRequest,
    pairing: WickPairing,
    bindings: Sequence[MomentumBinding],
    serial: int,
) -> GraphIR:
    ports, vertex_by_port, slot_by_port = _port_maps(request)
    propagators = {item.rule_id: item for item in request.propagators}
    binding_by_id = {item.binding_id: item for item in bindings}

    half_edges = tuple(
        HalfEdge(
            port.port_id,
            vertex.vertex_id,
            slot,
            port.field_type,
            port.flow,
            port.incoming_momentum,
            tuple(port.operator_derivatives),
        )
        for vertex in request.vertices
        for slot, port in enumerate(vertex.ordered_ports)
    )
    vertices = tuple(
        Vertex(
            vertex.vertex_id,
            vertex.kind,
            tuple(port.port_id for port in vertex.ordered_ports),
            vertex.coefficient.render(),
            vertex.color_word,
            vertex.superspace_point,
            vertex.momentum_delta,
            vertex.momentum_injection,
            tuple(
                [vertex.coefficient.render()]
                + list(vertex.operator_factors)
                + [f"origin:{origin}" for origin in vertex.origins]
            ),
        )
        for vertex in request.vertices
    )

    internal_edges: list[InternalEdge] = []
    used_bindings: set[str] = set()
    for pair in pairing.pairs:
        binding = _binding_for_pair(pair, request, propagators)
        if binding is None:
            raise AssertionError("an admitted pairing lost its momentum binding")
        if binding.binding_id not in binding_by_id or binding.binding_id in used_bindings:
            raise AssertionError("momentum bindings must be used exactly once")
        used_bindings.add(binding.binding_id)
        spec = propagators[binding.rule_id]
        left = ports[binding.left_port_id]
        right = ports[binding.right_port_id]
        spec.validate_ports(left, right)
        internal_edges.append(
            InternalEdge(
                binding.binding_id,
                binding.left_port_id,
                binding.right_port_id,
                spec.kernel_template.format(momentum=binding.momentum),
                binding.momentum,
                Flow.OUT if spec.oriented else Flow.NONE,
            )
        )

    external_legs = tuple(
        ExternalLeg(
            f"L_{port.port_id}",
            port.port_id,
            port.field_type,
            port.physical_external_momentum or "",
            port.color_label,
            port.flavor_label,
            port.spinor_indices,
            tuple(port.operator_derivatives),
        )
        for vertex in request.vertices
        for port in vertex.ordered_ports
        if port.role is PortRole.EXTERNAL
    )
    typed_metadata: dict[str, str] = {}
    source_legs = [
        leg for leg in external_legs if leg.field_type.name.startswith("Source[")
    ]
    tilde_w_legs = [
        leg for leg in external_legs if leg.field_type.name == "TildeW_dot_alpha"
    ]
    if len(source_legs) == 1:
        source_leg = source_legs[0]
        insertion_operator_parity = 1
        typed_metadata.update(
            {
                "source_port_statistics": source_leg.field_type.statistics.value,
                "source_port_parity": str(source_leg.field_type.parity),
                "source_color_variances": ",".join(
                    index.variance.value for index in source_leg.field_type.indices
                ),
                "insertion_operator_parity": str(insertion_operator_parity),
                "source_coupled_insertion_vertex_parity": str(
                    (source_leg.field_type.parity + insertion_operator_parity) % 2
                ),
            }
        )
    if len(tilde_w_legs) == 1 and len(tilde_w_legs[0].spinor_indices) == 1:
        typed_metadata["tildeW_dotted_variance"] = (
            tilde_w_legs[0].spinor_indices[0].variance.value
        )
    graph_metadata = {
        "request_id": request.request_id,
        "request_kind": request.request_kind.value,
        "pairing_signature": json.dumps(pairing.signature()),
        "wick_koszul_sign": str(pairing.koszul_sign),
        "source_status": "PHYSICAL" if request.request_kind is RequestKind.PHYSICAL_PARTIAL_CONTRACTION else "STRUCTURAL",
        "notation_schema_hash": request.schema_hash,
        "orientation": request.orientation,
        "external_fermion_word": ",".join(request.external_fermion_word),
        "external_koszul_sign": str(request.external_koszul_sign),
        "orientation_external_subsign": str(
            dict(request.orientation_sign_ledger)["external_subword"]
        ),
        "orientation_quantum_subsign": str(
            dict(request.orientation_sign_ledger)["quantum_subword"]
        ),
        **typed_metadata,
    }
    graph = GraphIR(
        f"{request.request_id}__pairing_{serial:03d}",
        vertices,
        half_edges,
        tuple(sorted(internal_edges, key=lambda edge: edge.edge_id)),
        external_legs,
        (request.loop_momentum,),
        tuple(sorted(graph_metadata.items())),
    )
    graph.assert_linear_momentum_routing()
    if set(used_bindings) != set(binding_by_id):
        raise AssertionError("the constructed graph did not consume every selected binding")
    if set(vertex_by_port) != {half_edge.half_edge_id for half_edge in graph.half_edges}:
        raise AssertionError("port-to-half-edge compilation is not bijective")
    if any(slot_by_port[item.half_edge_id] != item.slot for item in graph.half_edges):
        raise AssertionError("ordered port slots changed during GraphIR compilation")
    return graph


def _signature_for_order(graph: GraphIR, order: Sequence[str]) -> str:
    vertices = {item.vertex_id: item for item in graph.vertices}
    half_edges = {item.half_edge_id: item for item in graph.half_edges}
    external_by_half_edge = {item.attached_half_edge: item for item in graph.external_legs}
    new_index = {vertex_id: position for position, vertex_id in enumerate(order)}

    vertex_words: list[object] = []
    for vertex_id in order:
        vertex = vertices[vertex_id]
        ports: list[object] = []
        for half_edge_id in vertex.ordered_half_edges:
            half_edge = half_edges[half_edge_id]
            external = external_by_half_edge.get(half_edge_id)
            ports.append(
                (
                    half_edge.slot,
                    half_edge.field_type.name,
                    half_edge.field_type.statistics.value,
                    half_edge.field_type.chirality.value,
                    None
                    if external is None
                    else (
                        external.leg_id,
                        external.momentum,
                        external.color_label,
                        external.flavor_label,
                        tuple(
                            (item.space.value, item.label, item.variance.value)
                            for item in external.spinor_indices
                        ),
                    ),
                )
            )
        vertex_words.append(
            (
                vertex.kind,
                vertex.coefficient_symbol,
                tuple(vertex.color_word),
                tuple(ports),
            )
        )

    edge_words: list[object] = []
    for edge in graph.internal_edges:
        left_half = half_edges[edge.left_half_edge]
        right_half = half_edges[edge.right_half_edge]
        left = (
            new_index[left_half.vertex_id],
            left_half.slot,
            left_half.field_type.name,
        )
        right = (
            new_index[right_half.vertex_id],
            right_half.slot,
            right_half.field_type.name,
        )
        endpoints = (left, right) if edge.orientation is not Flow.NONE else tuple(sorted((left, right)))
        edge_words.append(
            (
                edge.propagator_symbol.replace(
                    f"({edge.momentum})", "(<r>)"
                ),
                edge.orientation.value,
                endpoints,
            )
        )
    payload = {"vertices": vertex_words, "edges": sorted(edge_words, key=repr)}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def graph_canonical_form(graph: GraphIR) -> str:
    return min(
        _signature_for_order(graph, order)
        for order in permutations(tuple(vertex.vertex_id for vertex in graph.vertices))
    )


def graph_canonical_key(graph: GraphIR) -> str:
    return sha256(graph_canonical_form(graph).encode()).hexdigest()


def graph_automorphism_order(graph: GraphIR) -> int:
    identity = _signature_for_order(graph, tuple(vertex.vertex_id for vertex in graph.vertices))
    order = sum(
        _signature_for_order(graph, permutation) == identity
        for permutation in permutations(tuple(vertex.vertex_id for vertex in graph.vertices))
    )
    if order < 1:
        raise AssertionError("the identity graph automorphism must exist")
    return order


def _orientation_signature(
    graph: GraphIR,
    request: DiagramRequest,
) -> tuple[str, ...]:
    specs = {item.rule_id: item for item in request.propagators}
    bindings = {item.binding_id: item for item in request.momentum_bindings}
    output: list[str] = []
    for edge in sorted(graph.internal_edges, key=lambda item: item.edge_id):
        binding = bindings[edge.edge_id]
        spec = specs[binding.rule_id]
        arrow = "->" if spec.oriented else "--"
        output.append(
            f"{binding.binding_id}:{spec.left_field_name}{arrow}{spec.right_field_name}:{binding.momentum}"
        )
    return tuple(output)


def _multiply_coefficients(factors: Iterable[ExactCoefficient]) -> ExactCoefficient:
    result = ExactCoefficient(1)
    for factor in factors:
        result = result * factor
    return result


def _reduce_coefficient(
    coefficient: ExactCoefficient,
    relations: Sequence[tuple[str, str]],
) -> tuple[ExactCoefficient, tuple[str, ...]]:
    rational = coefficient.rational
    symbols = list(coefficient.symbols)
    trace: list[str] = []
    for left, right in relations:
        cancellations = min(symbols.count(left), symbols.count(right))
        for _ in range(cancellations):
            symbols.remove(left)
            symbols.remove(right)
        if cancellations:
            trace.append(f"used ({left})*({right})=1 exactly {cancellations} time(s)")
    return (
        ExactCoefficient(
            rational,
            coefficient.sqrt2_power,
            coefficient.i_power,
            tuple(symbols),
        ),
        tuple(trace),
    )


def _amplitude_factors(
    request: DiagramRequest,
    graph: GraphIR,
    pairing: WickPairing,
    class_multiplicity: int,
    automorphism_order: int,
) -> tuple[AmplitudeFactor, ...]:
    propagators = {item.rule_id: item for item in request.propagators}
    bindings = {item.binding_id: item for item in request.momentum_bindings}
    orientation_sign_ledger = dict(request.orientation_sign_ledger)
    factors: list[AmplitudeFactor] = [
        AmplitudeFactor(
            "F_wick",
            "WICK_KOSZUL",
            str(pairing.koszul_sign),
            ExactCoefficient(pairing.koszul_sign),
            ("scripts/step5_graph_ir.py:enumerate_wick_pairings",),
        ),
        AmplitudeFactor(
            "F_orientation_external_subword",
            "ORIENTATION_KOSZUL_SUBSIGN",
            str(orientation_sign_ledger["external_subword"]),
            ExactCoefficient(orientation_sign_ledger["external_subword"]),
            request.origins,
            (
                ("subword", "external"),
                ("canonical_word", ",".join(request.external_fermion_word)),
            ),
        ),
        AmplitudeFactor(
            "F_orientation_quantum_subword",
            "ORIENTATION_KOSZUL_SUBSIGN",
            str(orientation_sign_ledger["quantum_subword"]),
            ExactCoefficient(orientation_sign_ledger["quantum_subword"]),
            request.origins,
            (("subword", "odd derivative-dressed quantum word"),),
        ),
        AmplitudeFactor(
            "F_orientation_total",
            "ORIENTATION_TOTAL_AUDIT_ONLY",
            str(request.external_koszul_sign),
            ExactCoefficient(1),
            request.origins,
            (
                (
                    "external_subsign",
                    str(orientation_sign_ledger["external_subword"]),
                ),
                (
                    "quantum_subsign",
                    str(orientation_sign_ledger["quantum_subword"]),
                ),
                ("product", str(request.external_koszul_sign)),
            ),
        ),
        AmplitudeFactor(
            "F_aut",
            "AUTOMORPHISM_AUDIT_ONLY",
            f"|Aut(G)|={automorphism_order}",
            ExactCoefficient(1),
            ("scripts/step5_supergraph_pipeline.py:graph_automorphism_order",),
            (
                ("automorphism_order", str(automorphism_order)),
                (
                    "coefficient_policy",
                    "AUDIT_ONLY_CLASS_ALREADY_SUMS_LABELED_PAIRINGS",
                ),
            ),
        ),
        AmplitudeFactor(
            "F_iso_mult",
            "ISOMORPHISM_CLASS_MULTIPLICITY",
            str(class_multiplicity),
            ExactCoefficient(class_multiplicity),
            ("scripts/step5_supergraph_pipeline.py:compile_request",),
        ),
    ]
    for vertex in request.vertices:
        factors.append(
            AmplitudeFactor(
                f"F_vertex_{vertex.vertex_id}",
                "INSERTION" if vertex.role is VertexRole.INSERTION else "ACTION_VERTEX",
                vertex.kind,
                vertex.coefficient,
                vertex.origins,
                (("superspace_point", vertex.superspace_point),),
            )
        )
        for position, operator in enumerate(vertex.operator_factors):
            factors.append(
                AmplitudeFactor(
                    f"F_operator_{vertex.vertex_id}_{position}",
                    "DERIVATIVE_OPERATOR",
                    operator,
                    ExactCoefficient(1),
                    vertex.origins,
                )
            )
        factors.append(
            AmplitudeFactor(
                f"F_delta_{vertex.vertex_id}",
                "VERTEX_DELTA",
                vertex.momentum_delta,
                ExactCoefficient(1),
                vertex.origins,
            )
        )
        for position, color_factor in enumerate(vertex.color_word):
            factors.append(
                AmplitudeFactor(
                    f"F_color_{vertex.vertex_id}_{position}",
                    "COLOR_FLAVOR_TENSOR",
                    color_factor,
                    ExactCoefficient(1),
                    vertex.origins,
                )
            )
    for edge in graph.internal_edges:
        binding = bindings[edge.edge_id]
        spec = propagators[binding.rule_id]
        metadata = [
            ("momentum", binding.momentum),
            ("normalization_status", spec.normalization_status),
            ("color_tensor", spec.color_tensor),
        ]
        if spec.flavor_tensor is not None:
            metadata.append(("flavor_tensor", spec.flavor_tensor))
        factors.append(
            AmplitudeFactor(
                f"F_prop_{edge.edge_id}",
                "PROPAGATOR",
                edge.propagator_symbol,
                spec.coefficient,
                spec.origins,
                tuple(metadata),
            )
        )
        factors.append(
            AmplitudeFactor(
                f"F_prop_color_{edge.edge_id}",
                "COLOR_FLAVOR_TENSOR",
                " * ".join(
                    item
                    for item in (spec.color_tensor, spec.flavor_tensor)
                    if item is not None
                ),
                ExactCoefficient(1),
                spec.origins,
            )
        )
    factors.append(
        AmplitudeFactor(
            "F_loop_measure",
            "LOOP_MEASURE",
            f"mu^(2 epsilon) d^d {request.loop_momentum}/(2 pi)^d",
            ExactCoefficient(1),
            request.origins,
        )
    )
    for leg in graph.external_legs:
        factors.append(
            AmplitudeFactor(
                f"F_external_{leg.leg_id}",
                "EXTERNAL_LEG",
                leg.operator_word(),
                ExactCoefficient(1),
                request.origins,
                (
                    ("momentum", leg.momentum),
                    ("color", leg.color_label),
                    ("flavor", leg.flavor_label or "NONE"),
                ),
            )
        )
    return tuple(factors)


def compile_request(
    request: DiagramRequest,
    schema: pipeline_ir.NotationSchema,
) -> CompilationResult:
    _validate_request_against_schema(request, schema)
    if request.request_kind is RequestKind.VALENCE_ONLY_REQUEST:
        raise ValenceOnlyRequestError(
            "VALENCE_ONLY_REQUEST is declarative and cannot be promoted to GraphIR"
        )
    if not request.vertices or not request.propagators:
        raise ValueError("a physical/structural request needs vertices and propagators")

    ports, vertex_by_port, _ = _port_maps(request)
    quantum_half_edges = tuple(
        HalfEdge(
            port.port_id,
            vertex.vertex_id,
            slot,
            port.field_type,
            port.flow,
            port.incoming_momentum,
            tuple(port.operator_derivatives),
        )
        for vertex in request.vertices
        for slot, port in enumerate(vertex.ordered_ports)
        if port.role is PortRole.QUANTUM_WICK
    )
    propagators = {item.rule_id: item for item in request.propagators}
    grammar = PropagatorGrammar(item.contraction_rule() for item in request.propagators)
    typed_pairings = enumerate_wick_pairings(
        quantum_half_edges,
        grammar,
        forbid_same_vertex=True,
    )

    admitted: list[tuple[GraphIR, WickPairing]] = []
    endpoint_admissible = 0
    rejected_disconnected = 0
    rejected_non_one_loop = 0
    for serial, pairing in enumerate(typed_pairings, start=1):
        bindings = _pairing_bindings(pairing, request, propagators)
        if bindings is None:
            continue
        endpoint_admissible += 1
        for pair in pairing.pairs:
            binding = _binding_for_pair(pair, request, propagators)
            assert binding is not None
            propagators[pair.rule_id].validate_ports(
                ports[binding.left_port_id], ports[binding.right_port_id]
            )
        connected, loop_number = _connected_one_loop(request, pairing, vertex_by_port)
        if not connected:
            rejected_disconnected += 1
            continue
        if loop_number != 1:
            rejected_non_one_loop += 1
            continue
        admitted.append((_build_graph(request, pairing, bindings, serial), pairing))

    grouped: dict[tuple[str, int], list[tuple[GraphIR, WickPairing]]] = {}
    for graph, pairing in admitted:
        grouped.setdefault((graph_canonical_key(graph), pairing.koszul_sign), []).append(
            (graph, pairing)
        )

    amplitudes: list[AmplitudeRecord] = []
    for amplitude_number, ((canonical_key, wick_sign), members) in enumerate(
        sorted(grouped.items()), start=1
    ):
        representative, pairing = members[0]
        multiplicity = len(members)
        automorphism_order = graph_automorphism_order(representative)
        factors = _amplitude_factors(
            request,
            representative,
            pairing,
            multiplicity,
            automorphism_order,
        )
        raw = _multiply_coefficients(factor.coefficient for factor in factors)
        reduced, reduction_trace = _reduce_coefficient(raw, request.coefficient_relations)
        normalization_statuses = {
            item.normalization_status
            for item in request.propagators
            if any(binding.rule_id == item.rule_id for binding in request.momentum_bindings)
        }
        normalization_status = (
            "EXACT_PROJECT_NORMALIZATION"
            if normalization_statuses == {"EXACT_PROJECT_NORMALIZATION"}
            else "+".join(sorted(normalization_statuses))
        )
        metadata = dict(representative.metadata)
        metadata.update(
            {
                "canonical_key": canonical_key,
                "isomorphism_class_multiplicity": str(multiplicity),
                "automorphism_order": str(automorphism_order),
                "automorphism_symmetry_factor": f"1/{automorphism_order}",
                "wick_koszul_sign": str(wick_sign),
            }
        )
        representative = replace(representative, metadata=tuple(sorted(metadata.items())))
        amplitudes.append(
            AmplitudeRecord(
                f"A_{request.request_id}_{amplitude_number:03d}",
                request.request_id,
                request.schema_hash,
                request.orientation,
                request.external_fermion_word,
                request.external_koszul_sign,
                request.orientation_sign_ledger,
                representative,
                canonical_key,
                _orientation_signature(representative, request),
                multiplicity,
                wick_sign,
                automorphism_order,
                Fraction(1, automorphism_order),
                factors,
                raw,
                reduced,
                reduction_trace,
                normalization_status,
            )
        )

    reconstructed = sum(item.class_multiplicity for item in amplitudes)
    expected = endpoint_admissible - rejected_disconnected - rejected_non_one_loop
    if reconstructed != expected:
        raise AssertionError("isomorphism quotient lost or duplicated admitted pairings")
    if len({item.canonical_key for item in amplitudes}) != len(amplitudes):
        raise AssertionError("canonical isomorphism classes were emitted twice")
    return CompilationResult(
        request.request_id,
        request.request_kind,
        request.schema_hash,
        len(typed_pairings),
        endpoint_admissible,
        rejected_disconnected,
        rejected_non_one_loop,
        len(amplitudes),
        reconstructed,
        tuple(amplitudes),
    )


def _color(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.COLOR_ADJOINT, label, Variance.UP)


def _color_down(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.COLOR_ADJOINT, label, Variance.DOWN)


def _undotted(label: str, variance: Variance = Variance.DOWN) -> IndexSlot:
    return IndexSlot(IndexSpace.UNDOTTED, label, variance)


def _dotted(label: str, variance: Variance = Variance.UP) -> IndexSlot:
    return IndexSlot(IndexSpace.DOTTED, label, variance)


V_FIELD = FieldType("V", Statistics.BOSON, Chirality.REAL, (_color("Q"),))
PHI_FIELD = FieldType("Phi", Statistics.BOSON, Chirality.CHIRAL, (_color("Q"),))
TILDE_PHI_FIELD = FieldType(
    "TildePhi", Statistics.BOSON, Chirality.ANTICHIRAL, (_color("Q"),)
)
W_FIELD = FieldType(
    "W_plus", Statistics.FERMION, Chirality.CHIRAL, (_color("E"), _undotted("+"))
)
TILDE_W_FIELD = FieldType(
    "TildeW_dot_alpha",
    Statistics.FERMION,
    Chirality.ANTICHIRAL,
    (_color("D"), _dotted("dot_alpha", Variance.DOWN)),
)
WW_SOURCE_FIELD = FieldType(
    "Source[nabla_-(X^A X^B)]",
    Statistics.FERMION,
    Chirality.UNCONSTRAINED,
    (_color_down("A"), _color_down("B")),
)


def _ww_seed_request(
    schema: pipeline_ir.NotationSchema,
    orientation: str,
) -> DiagramRequest:
    """Exact port-labelled WW seed in one declared external orientation."""

    if orientation not in ("DIRECT", "REFLECTED"):
        raise ValueError(orientation)
    left_letter, right_letter = ("A", "B") if orientation == "DIRECT" else ("B", "A")
    external_word = ("TildeW_dot_alpha", "W_plus")
    orientation_sign_ledger = (
        (("external_subword", 1), ("quantum_subword", 1))
        if orientation == "DIRECT"
        else (("external_subword", -1), ("quantum_subword", -1))
    )
    external_koszul_sign = 1

    insertion = VertexSpec(
        "vI",
        VertexRole.INSERTION,
        "COMPOSITE_INSERTION_I2_WW",
        ExactCoefficient(1),
        (
            PortSpec(
                f"I_{left_letter}", V_FIELD, PortRole.QUANTUM_WICK, Flow.OUT,
                "k", left_letter,
                origin="5.53a", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                f"I_{right_letter}", V_FIELD, PortRole.QUANTUM_WICK, Flow.IN,
                "-k-p-q", right_letter,
                origin="5.53a", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "I_source",
                WW_SOURCE_FIELD,
                PortRole.EXTERNAL,
                Flow.IN,
                "p+q",
                left_letter + right_letter,
                physical_external_momentum="p+q",
                origin="5.53a-5.53b",
                notation_port_spec="WW_source_B",
                notation_sector="BACKGROUND",
            ),
        ),
        (left_letter, right_letter),
        "theta_0",
        "delta(k-(k+p+q)+(p+q))",
        "0",
        (
            f"D_-[K_+V^{left_letter} K_+V^{right_letter}]",
            "K_+=-(1/8)D_+barD^2D_+",
        ),
        ("contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md:5.53a-5.53b",),
    )
    bar_vertex = VertexSpec(
        "vBar",
        VertexRole.ACTION,
        "BACKGROUND_CUBIC_TILDE_W",
        ExactCoefficient(Fraction(-1, 8), i_power=1, symbols=("h",)),
        (
            PortSpec(
                f"bar_{left_letter}", V_FIELD, PortRole.QUANTUM_WICK, Flow.IN,
                "-k", left_letter,
                origin="5.53e", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "bar_C", V_FIELD, PortRole.QUANTUM_WICK, Flow.OUT, "k+q", "C",
                origin="5.53e", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "bar_ext",
                TILDE_W_FIELD,
                PortRole.EXTERNAL,
                Flow.IN,
                "-q",
                "D",
                physical_external_momentum="q",
                spinor_indices=(_dotted("dot_alpha", Variance.DOWN),),
                origin="5.53e",
                notation_port_spec="TildeW_B",
                notation_sector="BACKGROUND",
            ),
        ),
        (f"c_{{{left_letter}CD}}",),
        "theta_1",
        "delta(-k+(k+q)-q)",
        "0",
        (f"barD^dot_alpha(C)-barD^dot_alpha({left_letter})",),
        ("contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md:5.53e",),
    )
    w_vertex = VertexSpec(
        "vW",
        VertexRole.ACTION,
        "BACKGROUND_CUBIC_W",
        ExactCoefficient(Fraction(1, 8), i_power=1, symbols=("h",)),
        (
            PortSpec(
                "W_C", V_FIELD, PortRole.QUANTUM_WICK, Flow.IN, "-k-q", "C",
                origin="5.53e", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                f"W_{right_letter}", V_FIELD, PortRole.QUANTUM_WICK, Flow.OUT,
                "k+p+q", right_letter,
                origin="5.53e", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "W_ext",
                W_FIELD,
                PortRole.EXTERNAL,
                Flow.IN,
                "-p",
                "E",
                physical_external_momentum="p",
                spinor_indices=(_undotted("+"),),
                origin="5.53e",
                notation_port_spec="W_plus_B",
                notation_sector="BACKGROUND",
            ),
        ),
        (f"c_{{{right_letter}CE}}",),
        "theta_2",
        "delta(-(k+q)+(k+p+q)-p)",
        "0",
        (f"D_a(C)-D_a({right_letter})",),
        ("contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md:5.53e",),
    )
    vector = PropagatorSpec(
        "P_VV",
        "V",
        "V",
        False,
        ExactCoefficient(-2, symbols=("g2",)),
        "kappa^(-1)*delta4theta/({momentum})^2",
        "kappa^{AB}",
        None,
        "EXACT_PROJECT_NORMALIZATION",
        ("contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md:5.46",),
        "V_Q",
        "V_Q",
    )
    return DiagramRequest(
        f"WW_{orientation}_EXACT",
        RequestKind.PHYSICAL_PARTIAL_CONTRACTION,
        (insertion, bar_vertex, w_vertex),
        (vector,),
        (
            MomentumBinding(
                "e0", "P_VV", f"I_{left_letter}", f"bar_{left_letter}", "k"
            ),
            MomentumBinding("e1", "P_VV", "bar_C", "W_C", "k+q"),
            MomentumBinding(
                "e2", "P_VV", f"W_{right_letter}", f"I_{right_letter}",
                "k+p+q",
            ),
        ),
        "k",
        (("h", "g2"),),
        (
            "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md:5.53a-5.53v",
            "scripts/step5_ww_seed.py:physical_triangle",
        ),
        schema.canonical_hash,
        orientation,
        external_word,
        external_koszul_sign,
        orientation_sign_ledger,
    )


def ww_seed_request(schema: pipeline_ir.NotationSchema) -> DiagramRequest:
    """Direct WW orientation."""

    return _ww_seed_request(schema, "DIRECT")


def ww_reflected_seed_request(schema: pipeline_ir.NotationSchema) -> DiagramRequest:
    """Reflected WW orientation with external and quantum sub-sign replay."""

    return _ww_seed_request(schema, "REFLECTED")


def matter_edge_structural_request(schema: pipeline_ir.NotationSchema) -> DiagramRequest:
    """One exact topology with a named, unevaluated chiral superfield edge."""

    matter = matter_bridge_monomials()[1]
    origins = tuple(f"{equation}" for equation in matter.source_equations)
    first = VertexSpec(
        "vM1",
        VertexRole.ACTION,
        "MATTER_BRIDGE_V1_STRUCTURAL",
        matter.coefficient,
        (
            PortSpec(
                "M1_tilde_ext",
                TILDE_PHI_FIELD,
                PortRole.EXTERNAL,
                Flow.IN,
                "-p",
                "A",
                "r",
                "p",
                origin="matter_bridge_v1:TildePhi",
                notation_port_spec="TildePhi_Q",
                notation_sector="QUANTUM",
            ),
            PortSpec(
                "M1_V", V_FIELD, PortRole.QUANTUM_WICK, Flow.OUT, "k", "D",
                origin="matter_bridge_v1:V", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "M1_Phi", PHI_FIELD, PortRole.QUANTUM_WICK, Flow.OUT, "p-k", "C", "r",
                origin="matter_bridge_v1:Phi", notation_port_spec="Phi_Q", notation_sector="QUANTUM",
            ),
        ),
        matter.color_word,
        "theta_1",
        "delta(-p+k+(p-k))",
        "0",
        (),
        origins,
    )
    second = VertexSpec(
        "vM2",
        VertexRole.ACTION,
        "MATTER_BRIDGE_V1_STRUCTURAL",
        matter.coefficient,
        (
            PortSpec(
                "M2_TildePhi", TILDE_PHI_FIELD, PortRole.QUANTUM_WICK, Flow.IN,
                "k-p", "A2", "r", origin="matter_bridge_v1:TildePhi",
                notation_port_spec="TildePhi_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "M2_V", V_FIELD, PortRole.QUANTUM_WICK, Flow.IN, "-k", "D2",
                origin="matter_bridge_v1:V", notation_port_spec="V_Q", notation_sector="QUANTUM",
            ),
            PortSpec(
                "M2_phi_ext",
                PHI_FIELD,
                PortRole.EXTERNAL,
                Flow.OUT,
                "p",
                "C2",
                "r",
                "-p",
                origin="matter_bridge_v1:Phi",
                notation_port_spec="Phi_Q",
                notation_sector="QUANTUM",
            ),
        ),
        matter.color_word,
        "theta_2",
        "delta((k-p)-k+p)",
        "0",
        (),
        origins,
    )
    vector = PropagatorSpec(
        "P_VV",
        "V",
        "V",
        False,
        ExactCoefficient(-2, symbols=("g2",)),
        "kappa^(-1)*delta4theta/({momentum})^2",
        "kappa^{AB}",
        None,
        "EXACT_PROJECT_NORMALIZATION",
        ("5.46",),
        "V_Q",
        "V_Q",
    )
    matter_edge = PropagatorSpec(
        "P_PHI_TILDEPHI_STRUCTURAL",
        "Phi",
        "TildePhi",
        True,
        ExactCoefficient(symbols=("G_PhiTildePhi",)),
        "P_PhiTildePhi[{momentum}]",
        "kappa^{AB}",
        "delta_{rs}",
        "STRUCTURAL_SYMBOL_NOT_EVALUATED",
        (
            "5.47b component kernels",
            "superfield normalization intentionally not assigned in this fixture",
        ),
        "Phi_Q",
        "TildePhi_Q",
    )
    return DiagramRequest(
        "MATTER_EDGE_STRUCTURAL",
        RequestKind.STRUCTURAL_PARTIAL_CONTRACTION,
        (first, second),
        (vector, matter_edge),
        (
            MomentumBinding("eV", "P_VV", "M1_V", "M2_V", "k"),
            MomentumBinding(
                "eM",
                "P_PHI_TILDEPHI_STRUCTURAL",
                "M1_Phi",
                "M2_TildePhi",
                "p-k",
            ),
        ),
        "k",
        (("h", "g2"),),
        ("scripts/step5_vertex_grammar.py:matter_bridge_monomials",),
        schema.canonical_hash,
        "MATTER_STRUCTURAL",
        (),
        1,
    )


def valence_only_fixture(schema: pipeline_ir.NotationSchema) -> DiagramRequest:
    return DiagramRequest(
        "VALENCE_ONLY_FIXTURE",
        RequestKind.VALENCE_ONLY_REQUEST,
        (),
        (),
        (),
        "k",
        (),
        ("generated/step5/graph-catalogue.json:valence_only_request_product",),
        schema.canonical_hash,
        "VALENCE_ONLY",
        (),
        1,
    )


def render_textbook_markdown(result: CompilationResult) -> str:
    lines = [
        f"# {result.request_id}",
        "",
        "## Completeness",
        "",
        "$$",
        "N_{\\rm typed}=" + str(result.typed_pairings)
        + ",\\qquad N_{\\rm endpoint}=" + str(result.endpoint_admissible_pairings)
        + ",\\qquad N_{\\rm classes}=" + str(result.isomorphism_classes) + ".",
        "$$",
        "",
    ]
    for amplitude in result.amplitudes:
        lines.extend(
            [
                f"## {amplitude.amplitude_id}",
                "",
                "$$",
                "\\mathcal A_G="
                + "\\left(" + str(amplitude.wick_koszul_sign) + "\\right)"
                + "\\left(" + str(amplitude.external_koszul_sign) + "\\right)"
                + "\\left(" + str(amplitude.class_multiplicity) + "\\right)"
                + "\\prod_{f\\in F_G^{\\rm coefficient}} f,"
                + "\\qquad |\\operatorname{Aut}G|="
                + str(amplitude.automorphism_order)
                + "\\quad(\\mathrm{audit\\ only}),",
                "$$",
                "",
                "$$",
                "C_G^{\\rm raw}=" + amplitude.exact_coefficient_raw.render()
                + ",\\qquad C_G^{\\rm Project}="
                + amplitude.exact_coefficient_reduced.render() + ".",
                "$$",
                "",
                "| factor | category | exact expression | coefficient | origin |",
                "|---|---|---|---|---|",
            ]
        )
        for factor in amplitude.factors:
            expression = factor.expression.replace("|", "\\mid")
            origins = "; ".join(factor.origins).replace("|", "\\mid")
            lines.append(
                f"| `{factor.factor_id}` | `{factor.category}` | `{expression}` | "
                f"`{factor.coefficient.render()}` | `{origins}` |"
            )
        lines.extend(
            [
                "",
                "```dot",
                amplitude.graph.to_dot().rstrip(),
                "```",
                "",
                "```mermaid",
                amplitude.graph.to_mermaid().rstrip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def build_demo_payload(
    ww_schema: pipeline_ir.NotationSchema,
    matter_schema: pipeline_ir.NotationSchema,
) -> dict[str, object]:
    ww = compile_request(ww_seed_request(ww_schema), ww_schema)
    ww_reflected = compile_request(
        ww_reflected_seed_request(ww_schema), ww_schema
    )
    matter = compile_request(matter_edge_structural_request(matter_schema), matter_schema)
    return {
        "schema": 1,
        "schema_hashes": {
            ww.request_id: ww.schema_hash,
            ww_reflected.request_id: ww_reflected.schema_hash,
            matter.request_id: matter.schema_hash,
        },
        "pipelines": [
            ww.canonical_dict(),
            ww_reflected.canonical_dict(),
            matter.canonical_dict(),
        ],
        "markdown": {
            ww.request_id: render_textbook_markdown(ww),
            ww_reflected.request_id: render_textbook_markdown(ww_reflected),
            matter.request_id: render_textbook_markdown(matter),
        },
    }


__all__ = [
    "AmplitudeFactor",
    "AmplitudeRecord",
    "CompilationResult",
    "DiagramRequest",
    "MomentumBinding",
    "PortRole",
    "PortSpec",
    "PropagatorSpec",
    "RequestKind",
    "ValenceOnlyRequestError",
    "VertexRole",
    "VertexSpec",
    "build_demo_payload",
    "compile_request",
    "graph_automorphism_order",
    "graph_canonical_form",
    "graph_canonical_key",
    "matter_edge_structural_request",
    "render_textbook_markdown",
    "valence_only_fixture",
    "ww_reflected_seed_request",
    "ww_seed_request",
]
