#!/usr/bin/env python3
"""Proposal-only two-loop DWordIR scheduler contract.

The module fixes typed words, a rooted theta decomposition, the ordered
rewrite phases, an exact lexicographic termination measure, exact Q(i)
sign/Koszul ledgers, and a symbolic-polynomial oracle gate.  It deliberately
does not infer a derivative scope from topology.  Every decorated literal
``K4_MINUS_ONE_EDGE`` graph therefore fails closed until a future
Wick-complete record supplies an explicit ordered derivative-scope AST and an
explicit propagator kernel for every internal edge.

No D-algebra trace multiplicity or evaluated local result is constructed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step6_two_loop_graphir import build_bundle


GENERATED_DIR = ROOT / "generated/step6/two-loop-dword"
GENERATED_CONTRACT = GENERATED_DIR / "dword-contract.json"
GENERATED_SCHEMA = GENERATED_DIR / "wick-input-schema.json"
GENERATED_MD = GENERATED_DIR / "two-loop-dword.md"
AUDIT = ROOT / "audits/step6-two-loop-dword-verification.json"

SCHEMA_VERSION = "step6.two_loop_dword.v1"
INPUT_SCHEMA_VERSION = "step6.wick_complete_dword_input.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
BLOCKED_STATUS = "BLOCKED_MISSING_WICK_COMPLETE_DWORD_INPUTS"
READY_STATUS = "READY_PHASE_SCHEDULE_CONTRACT_ONLY"
QI_DOMAIN = "Q(i)"

PHASE_ORDER = (
    "SCOPE_EXPANSION",
    "ENDPOINT_CANONICALIZATION",
    "PIVOTED_IBP",
    "PRIMITIVE_NORMAL_ORDERING",
    "PROJECTOR_REDUCTION",
    "EXTERNAL_CHIRALITY",
    "GRASSMANN_SATURATION",
    "TYPED_EDGE_COLLAPSE",
)

MEASURE_COMPONENTS = (
    "unexpanded_scope_nodes",
    "noncanonical_endpoint_tokens",
    "off_tree_pivot_distance",
    "primitive_order_inversions",
    "unreduced_projector_nodes",
    "unresolved_external_chirality_actions",
    "grassmann_saturation_defect",
    "typed_collapsible_edges",
)

DERIVATIVE_KINDS = {
    "D": ("UNDOTTED", 1, 1),
    "BAR_D": ("DOTTED", 1, 1),
    "D2": ("UNDOTTED", 0, 2),
    "BAR_D2": ("DOTTED", 0, 2),
}

LEDGER_KINDS = {
    "KOSZUL",
    "FOURIER",
    "LEIBNIZ",
    "ENDPOINT_TRANSFER",
    "PRIMITIVE_REORDER",
    "PROJECTOR",
    "CHIRALITY",
    "COLLAPSE",
}

FORBIDDEN_SAMPLE_KEYS = {
    "sample",
    "samples",
    "sample_point",
    "sample_points",
    "probe",
    "probes",
    "numerical_check",
    "random_check",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"not an exact rational: {value!r}")


@dataclass(frozen=True, order=True)
class GaussianRational:
    """An exact element of Q(i), never a floating-point approximation."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        return GaussianRational(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "GaussianRational":
        return GaussianRational(-self.re, -self.im)

    def __sub__(self, other: object) -> "GaussianRational":
        return self + (-gaussian(other))

    def __mul__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        return GaussianRational(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def to_json(self) -> dict[str, str]:
        return {"domain": QI_DOMAIN, "re": str(self.re), "im": str(self.im)}

    @classmethod
    def from_json(cls, value: Mapping[str, object]) -> "GaussianRational":
        if set(value) != {"domain", "re", "im"} or value["domain"] != QI_DOMAIN:
            raise ValueError("every exact scalar must use {domain: Q(i), re, im}")
        return cls(fraction(value["re"]), fraction(value["im"]))


def gaussian(value: object) -> GaussianRational:
    if isinstance(value, GaussianRational):
        return value
    if isinstance(value, (int, Fraction)):
        return GaussianRational(fraction(value))
    raise TypeError(f"not an exact Q(i) scalar: {value!r}")


ONE = GaussianRational(Fraction(1), Fraction(0))
MINUS_ONE = GaussianRational(Fraction(-1), Fraction(0))


@dataclass(frozen=True)
class ExactLedgerEntry:
    ledger_id: str
    phase: str
    kind: str
    factor: GaussianRational
    rule_id: str
    token_ids: tuple[str, ...]
    moving_parity: int | None = None
    crossed_parities: tuple[int, ...] = ()
    oracle_identity_id: str | None = None

    def __post_init__(self) -> None:
        if not self.ledger_id or not self.rule_id:
            raise ValueError("ledger id and rule id are required")
        if self.phase not in PHASE_ORDER:
            raise ValueError(f"unknown ledger phase: {self.phase}")
        if self.kind not in LEDGER_KINDS:
            raise ValueError(f"unknown ledger kind: {self.kind}")
        if any(parity not in (0, 1) for parity in self.crossed_parities):
            raise ValueError("crossed parities must lie in Z2")
        if self.kind == "KOSZUL":
            if self.moving_parity not in (0, 1):
                raise ValueError("a Koszul entry requires moving_parity in Z2")
            expected = MINUS_ONE if self.moving_parity * sum(self.crossed_parities) % 2 else ONE
            if self.factor != expected:
                raise ValueError(
                    "Koszul factor must equal (-1)^(moving_parity*sum(crossed_parities))"
                )
        elif self.moving_parity is not None or self.crossed_parities:
            raise ValueError("only a Koszul entry may carry crossed parities")

    def to_json(self) -> dict[str, object]:
        return {
            "ledger_id": self.ledger_id,
            "phase": self.phase,
            "kind": self.kind,
            "factor": self.factor.to_json(),
            "rule_id": self.rule_id,
            "token_ids": list(self.token_ids),
            "moving_parity": self.moving_parity,
            "crossed_parities": list(self.crossed_parities),
            "oracle_identity_id": self.oracle_identity_id,
        }

    @classmethod
    def from_json(cls, value: Mapping[str, object]) -> "ExactLedgerEntry":
        required = {"ledger_id", "phase", "kind", "factor", "rule_id", "token_ids"}
        if not required <= set(value):
            raise ValueError(f"ledger entry misses {sorted(required - set(value))}")
        return cls(
            ledger_id=str(value["ledger_id"]),
            phase=str(value["phase"]),
            kind=str(value["kind"]),
            factor=GaussianRational.from_json(_mapping(value["factor"], "ledger factor")),
            rule_id=str(value["rule_id"]),
            token_ids=tuple(str(item) for item in _sequence(value["token_ids"], "token ids")),
            moving_parity=None if value.get("moving_parity") is None else int(value["moving_parity"]),
            crossed_parities=tuple(int(item) for item in value.get("crossed_parities", ())),
            oracle_identity_id=(
                None if value.get("oracle_identity_id") is None else str(value["oracle_identity_id"])
            ),
        )


def _mapping(value: object, label: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value


def _sequence(value: object, label: str) -> Sequence[object]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        raise ValueError(f"{label} must be an ordered array")
    return value


def _assert_no_sampling(value: object, path: str = "oracle") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).lower()
            if normalized in FORBIDDEN_SAMPLE_KEYS:
                raise ValueError(f"numerical sampling is forbidden at {path}.{key}")
            _assert_no_sampling(child, f"{path}.{key}")
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _assert_no_sampling(child, f"{path}[{index}]")


def _canonical_polynomial(
    value: Mapping[str, object], variables: tuple[str, ...]
) -> tuple[tuple[tuple[int, ...], GaussianRational], ...]:
    terms = _sequence(value.get("terms"), "polynomial terms")
    combined: dict[tuple[int, ...], GaussianRational] = {}
    for term in terms:
        row = _mapping(term, "polynomial term")
        if set(row) != {"powers", "factor"}:
            raise ValueError("a polynomial term must contain exactly powers and factor")
        powers = _mapping(row["powers"], "monomial powers")
        if set(powers) - set(variables):
            raise ValueError(f"unknown polynomial variables: {sorted(set(powers) - set(variables))}")
        exponent = tuple(int(powers.get(variable, 0)) for variable in variables)
        if any(power < 0 for power in exponent):
            raise ValueError("polynomial exponents must be nonnegative")
        factor_value = GaussianRational.from_json(_mapping(row["factor"], "polynomial factor"))
        combined[exponent] = combined.get(exponent, GaussianRational()) + factor_value
    return tuple(sorted((powers, factor_value) for powers, factor_value in combined.items() if factor_value != GaussianRational()))


def validate_polynomial_oracle(value: Mapping[str, object]) -> dict[str, object]:
    """Verify exact coefficient identities; numerical probes are rejected."""

    _assert_no_sampling(value)
    if value.get("proof_mode") != "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY":
        raise ValueError("oracle proof_mode must be EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY")
    if value.get("coefficient_domain") != QI_DOMAIN:
        raise ValueError("oracle coefficient domain must be Q(i)")
    variables = tuple(str(item) for item in _sequence(value.get("variables"), "oracle variables"))
    if not variables or len(variables) != len(set(variables)) or any(not item for item in variables):
        raise ValueError("oracle variables must be a nonempty ordered unique array")
    identities = _sequence(value.get("identities"), "oracle identities")
    if not identities:
        raise ValueError("the exact polynomial oracle requires at least one identity")
    ids: list[str] = []
    checks: list[dict[str, object]] = []
    for identity in identities:
        row = _mapping(identity, "oracle identity")
        identity_id = str(row.get("identity_id", ""))
        if not identity_id:
            raise ValueError("every polynomial identity needs an id")
        lhs = _canonical_polynomial(_mapping(row.get("lhs"), "identity lhs"), variables)
        rhs = _canonical_polynomial(_mapping(row.get("rhs"), "identity rhs"), variables)
        if lhs != rhs:
            raise ValueError(f"exact polynomial identity fails: {identity_id}")
        ids.append(identity_id)
        checks.append(
            {
                "identity_id": identity_id,
                "method": "EXACT_MONOMIAL_COEFFICIENT_COMPARISON",
                "passed": True,
                "canonical_identity_hash": digest(
                    {
                        "variables": variables,
                        "lhs": [([*powers], factor_value.to_json()) for powers, factor_value in lhs],
                        "rhs": [([*powers], factor_value.to_json()) for powers, factor_value in rhs],
                    }
                ),
            }
        )
    if len(ids) != len(set(ids)):
        raise ValueError("polynomial oracle identity ids must be unique")
    return {
        "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
        "coefficient_domain": QI_DOMAIN,
        "variables": list(variables),
        "identity_ids": ids,
        "checks": checks,
        "numerical_sampling_used": False,
    }


def lexicographically_decreases(before: Sequence[int], after: Sequence[int]) -> bool:
    if len(before) != len(MEASURE_COMPONENTS) or len(after) != len(MEASURE_COMPONENTS):
        raise ValueError("termination measures have the wrong arity")
    if any(not isinstance(value, int) or value < 0 for value in (*before, *after)):
        raise ValueError("termination measures must lie in N^8")
    return tuple(after) < tuple(before)


def phase_measure_decreases(
    phase: str, before: Sequence[int], after: Sequence[int]
) -> bool:
    """Check the stronger phase-local lexicographic rewrite obligation."""

    if phase not in PHASE_ORDER:
        raise ValueError(f"unknown phase: {phase}")
    if not lexicographically_decreases(before, after):
        return False
    component = PHASE_ORDER.index(phase)
    return tuple(before[:component]) == tuple(after[:component]) and after[component] < before[component]


def termination_contract() -> dict[str, object]:
    return {
        "order": "LEXICOGRAPHIC_ON_N8",
        "components": list(MEASURE_COMPONENTS),
        "phase_component": dict(zip(PHASE_ORDER, MEASURE_COMPONENTS)),
        "rewrite_obligation": (
            "every applied rewrite must strictly lower the full lexicographic tuple; "
            "all earlier components must remain unchanged"
        ),
        "unchecked_transition_status": "REJECTED_MISSING_EXACT_BEFORE_AFTER_MEASURES",
    }


def _edge_by_id(graph: Mapping[str, object]) -> dict[str, Mapping[str, object]]:
    edges = [_mapping(edge, "internal edge") for edge in _sequence(graph["internal_edges"], "internal edges")]
    result = {str(edge["edge_id"]): edge for edge in edges}
    if len(result) != len(edges):
        raise ValueError("internal edge ids must be unique")
    return result


def theta_decomposition(graph: Mapping[str, object]) -> dict[str, object]:
    """Return a deterministic rooted spanning tree for literal K4 minus one edge."""

    if graph.get("topology") != "K4_MINUS_ONE_EDGE":
        raise ValueError("DWordIR accepts only literal K4_MINUS_ONE_EDGE topology objects")
    vertices = [_mapping(vertex, "vertex") for vertex in _sequence(graph["vertices"], "vertices")]
    edges = list(_edge_by_id(graph).values())
    if len(vertices) != 4 or len(edges) != 5:
        raise ValueError("literal K4 minus one edge must have V=4 and I=5")
    vertex_ids = {str(vertex["vertex_id"]) for vertex in vertices}
    degrees = {vertex_id: 0 for vertex_id in vertex_ids}
    pair_to_edge: dict[frozenset[str], Mapping[str, object]] = {}
    for edge in edges:
        pair = frozenset((str(edge["source"]), str(edge["target"])))
        if len(pair) != 2 or pair in pair_to_edge:
            raise ValueError("literal K4 minus one edge must be a simple graph")
        pair_to_edge[pair] = edge
        for vertex_id in pair:
            degrees[vertex_id] += 1
    if sorted(degrees.values()) != [2, 2, 3, 3]:
        raise ValueError("literal K4 minus one edge degree sequence must be (3,3,2,2)")
    poles = tuple(sorted(vertex_id for vertex_id, degree in degrees.items() if degree == 3))
    waist = tuple(sorted(vertex_id for vertex_id, degree in degrees.items() if degree == 2))
    central = pair_to_edge.get(frozenset(poles))
    if central is None:
        raise ValueError("the two degree-three theta poles must have a unique central edge")
    insertion = [str(vertex["vertex_id"]) for vertex in vertices if vertex["role"] == "COMPOSITE_INSERTION"]
    if len(insertion) != 1:
        raise ValueError("theta scheduler requires one composite-insertion root")
    root = insertion[0]
    anchor = root if root in poles else poles[0]
    tree_edge_ids = {str(central["edge_id"])}
    for vertex_id in waist:
        edge = pair_to_edge.get(frozenset((anchor, vertex_id)))
        if edge is None:
            raise ValueError("each degree-two theta vertex must attach to the anchor pole")
        tree_edge_ids.add(str(edge["edge_id"]))
    if len(tree_edge_ids) != 3:
        raise ValueError("theta spanning tree must have V-1 edges")
    chord_ids = sorted(set(_edge_by_id(graph)) - tree_edge_ids)
    if len(chord_ids) != 2:
        raise ValueError("a two-loop theta decomposition must have two chords")

    tree_adjacency: dict[str, list[tuple[str, str]]] = {vertex_id: [] for vertex_id in vertex_ids}
    edge_map = _edge_by_id(graph)
    for edge_id in tree_edge_ids:
        edge = edge_map[edge_id]
        source, target = str(edge["source"]), str(edge["target"])
        tree_adjacency[source].append((target, edge_id))
        tree_adjacency[target].append((source, edge_id))

    def tree_path(source: str, target: str) -> tuple[list[str], list[str]]:
        frontier: list[tuple[str, list[str], list[str]]] = [(source, [source], [])]
        visited: set[str] = set()
        while frontier:
            vertex_id, vertices_path, edges_path = frontier.pop(0)
            if vertex_id == target:
                return vertices_path, edges_path
            if vertex_id in visited:
                continue
            visited.add(vertex_id)
            for neighbor, edge_id in sorted(tree_adjacency[vertex_id]):
                if neighbor not in visited:
                    frontier.append((neighbor, vertices_path + [neighbor], edges_path + [edge_id]))
        raise ValueError("spanning-tree path does not exist")

    cycles: list[dict[str, object]] = []
    for chord_id in chord_ids:
        chord = edge_map[chord_id]
        vertices_path, edges_path = tree_path(str(chord["source"]), str(chord["target"]))
        cycles.append(
            {
                "chord_edge_id": chord_id,
                "tree_vertex_path": vertices_path,
                "tree_edge_path": edges_path,
                "fundamental_cycle_edge_ids": sorted([chord_id, *edges_path]),
            }
        )
    return {
        "root_vertex_id": root,
        "theta_pole_vertex_ids": list(poles),
        "degree_two_vertex_ids": list(waist),
        "anchor_pole_vertex_id": anchor,
        "central_edge_id": str(central["edge_id"]),
        "central_endpoint_ports": [str(central["source_port"]), str(central["target_port"])],
        "spanning_tree_edge_ids": sorted(tree_edge_ids),
        "chord_edge_ids": chord_ids,
        "fundamental_cycles": cycles,
        "cycle_rank_certificate": {"I_minus_V_plus_1": 2, "chord_count": 2, "passed": True},
    }


def central_critical_pairs(theta: Mapping[str, object]) -> list[dict[str, object]]:
    edge_id = str(theta["central_edge_id"])
    endpoints = [str(item) for item in theta["central_endpoint_ports"]]
    phase_pairs = (
        ("SCOPE_EXPANSION", "ENDPOINT_CANONICALIZATION", "scope_endpoint_overlap"),
        ("ENDPOINT_CANONICALIZATION", "PIVOTED_IBP", "endpoint_pivot_overlap"),
        ("PIVOTED_IBP", "PRIMITIVE_NORMAL_ORDERING", "pivot_primitive_overlap"),
        ("PROJECTOR_REDUCTION", "TYPED_EDGE_COLLAPSE", "projector_collapse_overlap"),
    )
    return [
        {
            "critical_pair_id": f"{edge_id}:{label}:{endpoint}",
            "central_edge_id": edge_id,
            "central_endpoint_port_id": endpoint,
            "left_phase": left,
            "right_phase": right,
            "overlap_class": label,
            "status": "DECLARED_UNJOINED_UNTIL_EXACT_WORD_INPUT",
            "required_certificate": {
                "same_input_word_hash": None,
                "left_normal_form_hash": None,
                "right_normal_form_hash": None,
                "exact_ledger_product_equal_in_Q_i": None,
                "polynomial_oracle_identity_id": None,
            },
        }
        for left, right, label in phase_pairs
        for endpoint in endpoints
    ]


def _required_paths(graph: Mapping[str, object]) -> tuple[str, ...]:
    edge_ids = sorted(_edge_by_id(graph))
    paths = [
        "wick_record.schema_version",
        "wick_record.graph_id",
        "wick_record.graph_hash",
        "wick_record.notation_schema_hash",
        "wick_record.wick_complete",
        "wick_record.wick_pairings",
        "wick_record.wick_completeness_certificate",
        "wick_record.ordered_derivative_scope_ast",
        "wick_record.exact_sign_koszul_ledger",
        "wick_record.polynomial_oracle",
    ]
    paths.extend(f"wick_record.propagator_kernels[{edge_id}]" for edge_id in edge_ids)
    return tuple(paths)


def deterministic_missing_inputs(
    graph: Mapping[str, object], record: Mapping[str, object] | None
) -> tuple[str, ...]:
    if record is None:
        return tuple(sorted(_required_paths(graph)))
    missing: list[str] = []
    for key in (
        "schema_version",
        "graph_id",
        "graph_hash",
        "notation_schema_hash",
        "wick_complete",
        "wick_pairings",
        "wick_completeness_certificate",
        "ordered_derivative_scope_ast",
        "exact_sign_koszul_ledger",
        "polynomial_oracle",
    ):
        if key not in record:
            missing.append(f"wick_record.{key}")
    kernels = record.get("propagator_kernels")
    kernels_by_id: set[str] = set()
    if isinstance(kernels, Sequence) and not isinstance(kernels, (str, bytes, bytearray)):
        for kernel in kernels:
            if isinstance(kernel, Mapping) and "edge_id" in kernel:
                kernels_by_id.add(str(kernel["edge_id"]))
    for edge_id in sorted(_edge_by_id(graph)):
        if edge_id not in kernels_by_id:
            missing.append(f"wick_record.propagator_kernels[{edge_id}]")
    return tuple(sorted(missing))


def _momentum_payload(graph: Mapping[str, object], edge: Mapping[str, object], sign: int) -> dict[str, object]:
    if sign not in (-1, 1):
        raise ValueError("endpoint momentum orientation must be +1 or -1")
    basis = [str(item) for item in graph["momentum_contract"]["basis"]]  # type: ignore[index]
    vector = [sign * int(item) for item in edge["momentum_vector"]]  # type: ignore[index]
    return {
        "basis": basis,
        "coefficients": vector,
        "orientation_sign_from_edge": sign,
        "space": graph["momentum_contract"]["square_space"],  # type: ignore[index]
    }


def validate_derivative_token(
    value: Mapping[str, object], graph: Mapping[str, object]
) -> dict[str, object]:
    required = {
        "token_id",
        "derivative_kind",
        "spinor_index_space",
        "spinor_indices",
        "operator_parity",
        "edge_id",
        "endpoint_port_id",
        "momentum",
    }
    if not required <= set(value):
        raise ValueError(f"derivative token misses {sorted(required - set(value))}")
    kind = str(value["derivative_kind"])
    if kind not in DERIVATIVE_KINDS:
        raise ValueError(f"unknown derivative kind: {kind}")
    index_space, parity, arity = DERIVATIVE_KINDS[kind]
    indices = [str(item) for item in _sequence(value["spinor_indices"], "spinor indices")]
    if str(value["spinor_index_space"]) != index_space or int(value["operator_parity"]) != parity:
        raise ValueError("derivative index space or parity disagrees with its kind")
    if len(indices) != arity or any(not index for index in indices):
        raise ValueError("derivative spinor-index arity is not explicit")
    edge_id = str(value["edge_id"])
    edge = _edge_by_id(graph).get(edge_id)
    if edge is None:
        raise ValueError(f"derivative token uses unknown edge: {edge_id}")
    endpoint = str(value["endpoint_port_id"])
    endpoints = {str(edge["source_port"]), str(edge["target_port"])}
    if endpoint not in endpoints:
        raise ValueError(f"derivative endpoint {endpoint} is not on edge {edge_id}")
    momentum = _mapping(value["momentum"], "typed momentum")
    sign = int(momentum.get("orientation_sign_from_edge", 0))
    expected_momentum = _momentum_payload(graph, edge, sign)
    if dict(momentum) != expected_momentum:
        raise ValueError("derivative momentum must be an exact oriented copy of the edge momentum")
    return {
        "token_id": str(value["token_id"]),
        "derivative_kind": kind,
        "spinor_index_space": index_space,
        "spinor_indices": indices,
        "operator_parity": parity,
        "edge_id": edge_id,
        "endpoint_port_id": endpoint,
        "momentum": expected_momentum,
    }


def validate_scope_ast(
    value: Mapping[str, object], graph: Mapping[str, object]
) -> tuple[dict[str, object], tuple[str, ...]]:
    """Validate an ordered AST without manufacturing any missing scope."""

    token_ids: list[str] = []
    known_ports = {
        str(edge[endpoint])
        for edge in _edge_by_id(graph).values()
        for endpoint in ("source_port", "target_port")
    }
    known_ports.update(
        str(port["port_id"])
        for vertex in _sequence(graph["vertices"], "vertices")
        for port in _sequence(_mapping(vertex, "vertex").get("background_ports", ()), "background ports")
    )

    def visit(node: Mapping[str, object], path: tuple[int, ...]) -> dict[str, object]:
        node_type = str(node.get("node_type", ""))
        if node_type == "FIELD_PORT":
            required = {"node_type", "port_id", "field_type", "parity"}
            if set(node) != required or int(node["parity"]) not in (0, 1):
                raise ValueError(f"invalid FIELD_PORT at AST path {path}")
            if str(node["port_id"]) not in known_ports:
                raise ValueError(f"unknown FIELD_PORT at AST path {path}: {node['port_id']}")
            return {
                "node_type": node_type,
                "port_id": str(node["port_id"]),
                "field_type": str(node["field_type"]),
                "parity": int(node["parity"]),
            }
        if node_type in {"ORDERED_SCOPE", "ORDERED_PRODUCT"}:
            children = _sequence(node.get("ordered_children"), f"{node_type} children")
            if not children:
                raise ValueError(f"{node_type} at AST path {path} is empty")
            result: dict[str, object] = {
                "node_type": node_type,
                "ordered_children": [
                    visit(_mapping(child, "scope child"), path + (index,))
                    for index, child in enumerate(children)
                ],
            }
            if node_type == "ORDERED_SCOPE":
                scope_id = str(node.get("scope_id", ""))
                if not scope_id:
                    raise ValueError(f"ORDERED_SCOPE at AST path {path} needs a scope id")
                result["scope_id"] = scope_id
            elif set(node) != {"node_type", "ordered_children"}:
                raise ValueError(f"ORDERED_PRODUCT at AST path {path} has undeclared fields")
            return result
        if node_type == "DERIVATIVE_APPLICATION":
            if set(node) != {"node_type", "token", "argument"}:
                raise ValueError(f"invalid DERIVATIVE_APPLICATION at AST path {path}")
            token = validate_derivative_token(_mapping(node["token"], "derivative token"), graph)
            token_ids.append(str(token["token_id"]))
            return {
                "node_type": node_type,
                "token": token,
                "argument": visit(_mapping(node["argument"], "derivative argument"), path + (0,)),
            }
        if node_type == "LINEAR_COMBINATION":
            terms = _sequence(node.get("ordered_terms"), "linear-combination terms")
            if not terms:
                raise ValueError(f"LINEAR_COMBINATION at AST path {path} is empty")
            result_terms: list[dict[str, object]] = []
            for index, term in enumerate(terms):
                row = _mapping(term, "linear-combination term")
                if set(row) != {"factor", "expression"}:
                    raise ValueError("linear-combination term must contain factor and expression")
                result_terms.append(
                    {
                        "factor": GaussianRational.from_json(_mapping(row["factor"], "term factor")).to_json(),
                        "expression": visit(_mapping(row["expression"], "term expression"), path + (index,)),
                    }
                )
            return {"node_type": node_type, "ordered_terms": result_terms}
        raise ValueError(f"unknown ordered derivative-scope AST node {node_type!r} at path {path}")

    normalized = visit(value, ())
    if len(token_ids) != len(set(token_ids)):
        raise ValueError("derivative token ids must be unique in the scope AST")
    return normalized, tuple(token_ids)


def _validate_wick_completeness(
    record: Mapping[str, object], graph: Mapping[str, object]
) -> list[dict[str, object]]:
    if record.get("wick_complete") is not True:
        raise ValueError("wick_complete must be true")
    edge_map = _edge_by_id(graph)
    pairings = _sequence(record["wick_pairings"], "Wick pairings")
    normalized: list[dict[str, object]] = []
    for pairing in pairings:
        row = _mapping(pairing, "Wick pairing")
        edge_id = str(row.get("edge_id", ""))
        if edge_id not in edge_map:
            raise ValueError(f"Wick pairing uses unknown edge: {edge_id}")
        edge = edge_map[edge_id]
        endpoint_ports = [str(item) for item in _sequence(row.get("endpoint_ports"), "pairing endpoints")]
        if sorted(endpoint_ports) != sorted((str(edge["source_port"]), str(edge["target_port"]))):
            raise ValueError(f"Wick pairing endpoints disagree on edge {edge_id}")
        field_types = [str(item) for item in _sequence(row.get("ordered_field_types"), "pairing fields")]
        if len(field_types) != 2 or any(not item for item in field_types):
            raise ValueError("each Wick pairing needs two ordered field types")
        normalized.append(
            {"edge_id": edge_id, "endpoint_ports": endpoint_ports, "ordered_field_types": field_types}
        )
    if sorted(row["edge_id"] for row in normalized) != sorted(edge_map):
        raise ValueError("Wick-complete record must pair every internal edge exactly once")
    certificate = _mapping(record["wick_completeness_certificate"], "Wick completeness certificate")
    required_true = {
        "every_quantum_port_used_once": True,
        "connected": True,
        "pairing_edge_ids_equal_graph_edge_ids": True,
    }
    if any(certificate.get(key) is not expected for key, expected in required_true.items()):
        raise ValueError("Wick completeness certificate is not affirmative")
    return sorted(normalized, key=lambda row: str(row["edge_id"]))


def _validate_kernels(
    kernels: Sequence[object], graph: Mapping[str, object], oracle_ids: set[str]
) -> tuple[list[dict[str, object]], tuple[str, ...]]:
    edge_map = _edge_by_id(graph)
    normalized: list[dict[str, object]] = []
    token_ids: list[str] = []
    for kernel in kernels:
        row = _mapping(kernel, "propagator kernel")
        edge_id = str(row.get("edge_id", ""))
        if edge_id not in edge_map:
            raise ValueError(f"propagator kernel uses unknown edge: {edge_id}")
        edge = edge_map[edge_id]
        endpoints = [str(item) for item in _sequence(row.get("endpoint_ports"), "kernel endpoints")]
        if endpoints != [str(edge["source_port"]), str(edge["target_port"])]:
            raise ValueError(f"kernel endpoint order disagrees with oriented edge {edge_id}")
        kernel_ast = _mapping(row.get("ordered_kernel_ast"), "ordered kernel AST")
        if kernel_ast.get("node_type") != "ORDERED_PROPAGATOR_KERNEL":
            raise ValueError("kernel AST must be ORDERED_PROPAGATOR_KERNEL")
        word = _sequence(kernel_ast.get("ordered_derivative_tokens"), "kernel derivative word")
        normalized_word = [
            validate_derivative_token(_mapping(token, "kernel derivative token"), graph)
            for token in word
        ]
        if any(token["edge_id"] != edge_id for token in normalized_word):
            raise ValueError("every kernel derivative token must remain on its kernel edge")
        token_ids.extend(str(token["token_id"]) for token in normalized_word)
        if not isinstance(kernel_ast.get("grassmann_delta_ast"), Mapping):
            raise ValueError("kernel requires an explicit Grassmann-delta AST")
        if not isinstance(kernel_ast.get("scalar_denominator_ast"), Mapping):
            raise ValueError("kernel requires an explicit scalar-denominator AST")
        identity_ids = [str(item) for item in _sequence(row.get("oracle_identity_ids"), "kernel oracle ids")]
        if not identity_ids or not set(identity_ids) <= oracle_ids:
            raise ValueError("every kernel must cite known exact polynomial identities")
        normalized.append(
            {
                "edge_id": edge_id,
                "endpoint_ports": endpoints,
                "ordered_field_types": [
                    str(item) for item in _sequence(row.get("ordered_field_types"), "kernel field types")
                ],
                "ordered_kernel_ast": {
                    "node_type": "ORDERED_PROPAGATOR_KERNEL",
                    "ordered_derivative_tokens": normalized_word,
                    "grassmann_delta_ast": dict(kernel_ast["grassmann_delta_ast"]),
                    "scalar_denominator_ast": dict(kernel_ast["scalar_denominator_ast"]),
                },
                "oracle_identity_ids": identity_ids,
            }
        )
    if sorted(row["edge_id"] for row in normalized) != sorted(edge_map):
        raise ValueError("there must be exactly one propagator kernel per internal edge")
    if len(token_ids) != len(set(token_ids)):
        raise ValueError("kernel derivative token ids must be globally unique")
    return sorted(normalized, key=lambda row: str(row["edge_id"])), tuple(token_ids)


def compile_schedule_contract(
    graph: Mapping[str, object], record: Mapping[str, object] | None
) -> dict[str, object]:
    """Validate complete input and emit only a pending phase schedule."""

    theta = theta_decomposition(graph)
    missing = deterministic_missing_inputs(graph, record)
    if missing:
        return {
            "status": BLOCKED_STATUS,
            "graph_id": graph["graph_id"],
            "graph_hash": graph["graph_hash"],
            "missing_inputs": list(missing),
            "phase_order": list(PHASE_ORDER),
            "theta_decomposition": theta,
            "critical_pairs": central_critical_pairs(theta),
            "global_confluence_claimed": False,
            "phase_execution": None,
        }
    assert record is not None
    if record["schema_version"] != INPUT_SCHEMA_VERSION:
        raise ValueError("Wick input schema version mismatch")
    if record["graph_id"] != graph["graph_id"] or record["graph_hash"] != graph["graph_hash"]:
        raise ValueError("Wick input graph binding mismatch")
    notation_hash = str(record["notation_schema_hash"])
    if len(notation_hash) != 64 or any(character not in "0123456789abcdef" for character in notation_hash):
        raise ValueError("notation_schema_hash must be a lowercase SHA-256 digest")
    pairings = _validate_wick_completeness(record, graph)
    oracle = validate_polynomial_oracle(_mapping(record["polynomial_oracle"], "polynomial oracle"))
    scope_ast, scope_token_ids = validate_scope_ast(
        _mapping(record["ordered_derivative_scope_ast"], "ordered derivative-scope AST"), graph
    )
    kernels, kernel_token_ids = _validate_kernels(
        _sequence(record["propagator_kernels"], "propagator kernels"),
        graph,
        set(str(item) for item in oracle["identity_ids"]),
    )
    if set(scope_token_ids) & set(kernel_token_ids):
        raise ValueError("scope and kernel derivative token ids must be disjoint")
    ledger = [
        ExactLedgerEntry.from_json(_mapping(item, "ledger entry"))
        for item in _sequence(record["exact_sign_koszul_ledger"], "exact sign/Koszul ledger")
    ]
    if len({entry.ledger_id for entry in ledger}) != len(ledger):
        raise ValueError("ledger ids must be unique")
    known_token_ids = set(scope_token_ids) | set(kernel_token_ids)
    if any(not set(entry.token_ids) <= known_token_ids for entry in ledger):
        raise ValueError("ledger entry references an unknown derivative token")
    oracle_ids = set(str(item) for item in oracle["identity_ids"])
    if any(
        entry.oracle_identity_id is not None and entry.oracle_identity_id not in oracle_ids
        for entry in ledger
    ):
        raise ValueError("ledger entry references an unknown exact polynomial identity")
    phases = [
        {
            "phase": phase,
            "status": "PENDING_EXACT_REWRITE_EXECUTION",
            "required_measure_component": MEASURE_COMPONENTS[index],
            "before_measure": None,
            "after_measure": None,
            "applied_rewrites": None,
        }
        for index, phase in enumerate(PHASE_ORDER)
    ]
    normalized_input = {
        "schema_version": INPUT_SCHEMA_VERSION,
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "notation_schema_hash": notation_hash,
        "wick_complete": True,
        "wick_pairings": pairings,
        "ordered_derivative_scope_ast": scope_ast,
        "propagator_kernels": kernels,
        "exact_sign_koszul_ledger": [entry.to_json() for entry in ledger],
        "polynomial_oracle_certificate": oracle,
    }
    return {
        "status": READY_STATUS,
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "notation_schema_hash": notation_hash,
        "normalized_input_hash": digest(normalized_input),
        "phase_order": list(PHASE_ORDER),
        "termination_measure": termination_contract(),
        "theta_decomposition": theta,
        "critical_pairs": central_critical_pairs(theta),
        "global_confluence_claimed": False,
        "exact_sign_koszul_ledger": [entry.to_json() for entry in ledger],
        "polynomial_oracle_certificate": oracle,
        "phase_execution": phases,
        "evaluated_word": None,
    }


def input_schema_contract(graph: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema_version": INPUT_SCHEMA_VERSION,
        "graph_binding": {
            "graph_id": graph["graph_id"],
            "graph_hash": graph["graph_hash"],
            "topology": "K4_MINUS_ONE_EDGE",
        },
        "required_paths": list(_required_paths(graph)),
        "derivative_token": {
            "required_fields": [
                "token_id",
                "derivative_kind",
                "spinor_index_space",
                "spinor_indices",
                "operator_parity",
                "edge_id",
                "endpoint_port_id",
                "momentum",
            ],
            "kinds": {
                kind: {"spinor_index_space": data[0], "parity": data[1], "index_arity": data[2]}
                for kind, data in DERIVATIVE_KINDS.items()
            },
            "momentum_rule": "exact oriented edge momentum; orientation_sign_from_edge is +1 or -1",
        },
        "ordered_scope_ast_nodes": [
            "ORDERED_SCOPE",
            "ORDERED_PRODUCT",
            "DERIVATIVE_APPLICATION",
            "LINEAR_COMBINATION",
            "FIELD_PORT",
        ],
        "propagator_kernel": {
            "one_per_edge": sorted(_edge_by_id(graph)),
            "kernel_node_type": "ORDERED_PROPAGATOR_KERNEL",
            "explicit_fields": [
                "ordered_derivative_tokens",
                "grassmann_delta_ast",
                "scalar_denominator_ast",
                "oracle_identity_ids",
            ],
        },
        "exact_scalar_domain": QI_DOMAIN,
        "polynomial_oracle_gate": {
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "method": "EXACT_MONOMIAL_COEFFICIENT_COMPARISON",
            "forbidden_sampling_keys": sorted(FORBIDDEN_SAMPLE_KEYS),
        },
    }


def build_payload() -> dict[str, object]:
    graph_bundle = build_bundle()
    graphs = graph_bundle["literal_direct_graphs"]
    contracts = [compile_schedule_contract(graph, None) for graph in graphs]
    schemas = [input_schema_contract(graph) for graph in graphs]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "scope": "LITERAL_K4_MINUS_EDGE_TWO_LOOP_DWORD_PHASE_SCHEDULER_CONTRACT",
        "external_result_used_as_calculation_input": False,
        "phase_order": list(PHASE_ORDER),
        "termination_measure": termination_contract(),
        "exact_scalar_domain": QI_DOMAIN,
        "polynomial_oracle_requirement": {
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "numerical_sampling_admissible": False,
        },
        "graph_contracts": contracts,
        "input_schemas": schemas,
        "global_confluence_claimed": False,
        "physical_derivative_scopes_inferred": False,
        "phase_execution_performed": False,
    }
    payload["payload_hash"] = digest({key: value for key, value in payload.items() if key != "payload_hash"})
    return payload


def exact_checks(payload: Mapping[str, object]) -> dict[str, bool]:
    contracts = payload["graph_contracts"]  # type: ignore[index]

    def keys(value: object) -> set[str]:
        if isinstance(value, Mapping):
            return {str(key) for key in value} | set().union(*(keys(child) for child in value.values()))
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            return set().union(*(keys(child) for child in value))
        return set()

    forbidden_result_keys = {
        "d_algebra_row_count",
        "numerator",
        "uv_pole",
        "renormalized_pole",
        "anomaly_coefficient",
        "local_coefficient",
    }
    checks = {
        "proposal_status": payload["status"] == STATUS,
        "phase_order_exact": tuple(payload["phase_order"]) == PHASE_ORDER,  # type: ignore[arg-type]
        "termination_components_exact": tuple(payload["termination_measure"]["components"]) == MEASURE_COMPONENTS,  # type: ignore[index]
        "literal_graph_set_nonempty": bool(contracts),
        "all_inputs_are_literal_k4_minus_edge": all(
            contract["theta_decomposition"]["cycle_rank_certificate"]["passed"]  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "all_real_graph_attempts_fail_closed": all(contract["status"] == BLOCKED_STATUS for contract in contracts),  # type: ignore[union-attr]
        "all_missing_lists_deterministic": all(
            contract["missing_inputs"] == sorted(contract["missing_inputs"]) for contract in contracts  # type: ignore[union-attr]
        ),
        "all_theta_cycle_rank_two": all(
            contract["theta_decomposition"]["cycle_rank_certificate"] == {  # type: ignore[union-attr]
                "I_minus_V_plus_1": 2,
                "chord_count": 2,
                "passed": True,
            }
            for contract in contracts  # type: ignore[union-attr]
        ),
        "all_theta_trees_have_three_edges_two_chords": all(
            len(contract["theta_decomposition"]["spanning_tree_edge_ids"]) == 3  # type: ignore[union-attr]
            and len(contract["theta_decomposition"]["chord_edge_ids"]) == 2  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "central_critical_pairs_declared_unjoined": all(
            contract["critical_pairs"]  # type: ignore[union-attr]
            and all(pair["status"] == "DECLARED_UNJOINED_UNTIL_EXACT_WORD_INPUT" for pair in contract["critical_pairs"])  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "no_global_confluence_claim": payload["global_confluence_claimed"] is False,
        "no_scope_inference": payload["physical_derivative_scopes_inferred"] is False,
        "no_phase_execution": payload["phase_execution_performed"] is False,
        "polynomial_oracle_is_symbolic_gate": payload["polynomial_oracle_requirement"] == {  # type: ignore[index]
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "numerical_sampling_admissible": False,
        },
        "no_evaluated_physical_result_fields": not (keys(payload) & forbidden_result_keys),
        "payload_hash_recomputes": payload["payload_hash"] == digest(
            {key: value for key, value in payload.items() if key != "payload_hash"}
        ),
    }
    return checks


def build_audit(payload: Mapping[str, object]) -> dict[str, object]:
    checks = exact_checks(payload)
    failures = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "step6.two_loop_dword.audit.v1",
        "status": "PASS" if not failures else "FAIL",
        "proposal_status": STATUS,
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
    }


def render_markdown(payload: Mapping[str, object]) -> str:
    lines = [
        "# Step 6 — literal $K_4\\setminus e$ DWordIR scheduler contract",
        "",
        f"`{STATUS}`",
        "",
        "$$",
        "\\mathsf{Scope}\\to\\mathsf{Endpoint}\\to\\mathsf{IBP}\\to\\mathsf{Primitive}",
        "\\to\\mathsf{Projector}\\to\\mathsf{Chirality}\\to\\mathsf{Saturation}",
        "\\to\\mathsf{Collapse}.",
        "$$",
        "",
        "$$",
        "\\mu=(n_{\\rm scope},n_{\\rm endpoint},n_{\\rm pivot},n_{\\rm inv},",
        "n_{\\rm proj},n_{\\rm chir},n_{\\rm sat},n_{\\rm coll})\\in\\mathbb N^8,",
        "\\qquad \\mu_{j+1}<_{\\rm lex}\\mu_j.",
        "$$",
        "",
    ]
    for contract in payload["graph_contracts"]:  # type: ignore[index]
        theta = contract["theta_decomposition"]
        lines.extend(
            [
                f"## `{contract['graph_id']}`",
                "",
                "$$",
                f"e_c={theta['central_edge_id']},\\qquad "
                f"T=\\{{{','.join(theta['spanning_tree_edge_ids'])}\\}},\\qquad "
                f"C=\\{{{','.join(theta['chord_edge_ids'])}\\}}.",
                "$$",
                "",
                f"`{contract['status']}`",
                "",
            ]
        )
    lines.extend(
        [
            "Exact input domain: `Q(i)`.",
            "",
            "Polynomial gate: `EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY`; numerical samples are rejected.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, object], dict[str, object]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise RuntimeError(f"Step-6 DWordIR audit failed: {audit['failures']}")
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_CONTRACT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GENERATED_SCHEMA.write_text(
        json.dumps(
            {
                "schema_version": INPUT_SCHEMA_VERSION,
                "graph_schemas": payload["input_schemas"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload), encoding="utf-8")
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "proposal_status": payload["status"],
                "graph_contract_count": len(payload["graph_contracts"]),
                "failed": audit["failed"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
