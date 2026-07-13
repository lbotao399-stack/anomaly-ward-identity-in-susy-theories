#!/usr/bin/env python3
"""Exact Step-6 four-free-index color/Jacobi canonicalizer.

The input tensor language is restricted to totally antisymmetric ``c`` nodes
and ``kappa``/``kappa_inverse`` metric nodes.  Metric contraction and exact
antisymmetry canonicalization precede every Jacobi operation.  The finite IHX
orbit is converted into an exact rational relation matrix.  Descending
lexicographic pivots orient every rewrite from a larger canonical graph key to
strictly smaller keys, so reduction terminates and has one RREF normal form.

No adjoint-Casimir rule, numerator, integral, or graph coefficient is used.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:
    from scripts import step6_color_tensor as color
except ModuleNotFoundError:  # direct execution
    import step6_color_tensor as color


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/color-jacobi"
GENERATED_JSON = GENERATED_DIR / "color-jacobi.json"
GENERATED_MD = GENERATED_DIR / "color-jacobi.md"
AUDIT = ROOT / "audits/step6-color-jacobi-verification.json"

SCHEMA_VERSION = "step6.color_jacobi.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
STAGE = "EXACT_COLOR_METRIC_ANTISYMMETRY_JACOBI_QUOTIENT"
FREE_INDEX_ORDER = tuple(color.FREE_INDEX_ORDER)
MAX_ORBIT_SIZE = 4096
ADJOINT_CASIMIR_STATUS = "NOT_DEFINED_IN_PROJECT_AUTHORITY_NO_REWRITE"


class ColorJacobiError(ValueError):
    """Base fail-closed color/Jacobi error."""


class ColorInputError(ColorJacobiError):
    """Raised when the tensor or coefficient schema is malformed."""


class JacobiIncidenceError(ColorJacobiError):
    """Raised when an IHX local edge is not a two-trivalent-vertex edge."""


class OrbitLimitError(ColorJacobiError):
    """Raised when a finite exact orbit exceeds the certified bound."""


class RewriteSystemError(ColorJacobiError):
    """Raised when the oriented exact relation system is inconsistent."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def fraction_json(value: Fraction) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ColorInputError("color coefficients must be exact rational numbers")
    if isinstance(value, (int, Fraction)):
        return Fraction(value)
    if isinstance(value, Mapping):
        if set(value) == {"numerator", "denominator"}:
            return Fraction(int(value["numerator"]), int(value["denominator"]))
        if "rational" in value:
            rational = parse_fraction(value["rational"])
            sign = int(value.get("sign", 1))
            if sign not in {-1, 1}:
                raise ColorInputError("exact coefficient sign is not +1 or -1")
            atoms = value.get("atoms", ())
            if atoms:
                raise ColorInputError("Jacobi quotient accepts rational color scalars only")
            return sign * rational
    raise ColorInputError("unsupported exact rational coefficient schema")


def tensor_indices(tensor: Mapping[str, Any]) -> list[str]:
    if tensor.get("kind") == "c":
        source = tensor.get("ordered_indices", tensor.get("canonical_indices"))
    else:
        source = tensor.get("indices")
    if not isinstance(source, Sequence) or isinstance(source, (str, bytes)):
        raise ColorInputError("tensor index list is absent")
    return [str(index) for index in source]


def validate_and_project_tensor(tensor: Mapping[str, Any]) -> dict[str, Any]:
    kind = str(tensor.get("kind"))
    indices = tensor_indices(tensor)
    if kind == "c":
        if len(indices) != 3:
            raise ColorInputError("c node must have exactly three ordered slots")
        return {"kind": "c", "ordered_indices": indices}
    if kind not in {"kappa", "kappa_inverse"}:
        raise ColorInputError(f"unsupported color tensor kind {kind}")
    if len(indices) != 2:
        raise ColorInputError("metric node must have exactly two slots")
    required_variance = "lower" if kind == "kappa" else "upper"
    if tensor.get("variance") != required_variance:
        raise ColorInputError(
            f"{kind} requires variance={required_variance}"
        )
    return {"kind": kind, "indices": indices, "variance": required_variance}


def adapt_network_input(network: Any) -> tuple[list[dict[str, Any]], Fraction, dict[str, Any]]:
    """Accept raw tensors or the existing full compiler canonical-network schema."""
    if isinstance(network, Sequence) and not isinstance(network, (str, bytes, bytearray)):
        tensors = [validate_and_project_tensor(tensor) for tensor in network]
        return tensors, Fraction(1), {
            "schema": "RAW_COLOR_TENSOR_SEQUENCE",
            "source_signature_sha256": None,
        }
    if not isinstance(network, Mapping):
        raise ColorInputError("network must be a tensor sequence or canonical-network mapping")
    if "canonical_tensors" not in network:
        raise ColorInputError("canonical-network mapping lacks canonical_tensors")
    if bool(network.get("zero_by_antisymmetry", False)):
        return [], Fraction(0), {
            "schema": "STEP6_COLOR_COMPILER_CANONICAL_NETWORK",
            "source_signature_sha256": network.get("signature_sha256"),
            "source_zero_by_antisymmetry": True,
        }
    sign = int(network.get("overall_antisymmetry_sign", 1))
    if sign not in {-1, 1}:
        raise ColorInputError("canonical network has an illegal overall sign")
    tensors = [
        validate_and_project_tensor(tensor)
        for tensor in network["canonical_tensors"]
    ]
    return tensors, Fraction(sign), {
        "schema": "STEP6_COLOR_COMPILER_CANONICAL_NETWORK",
        "source_signature_sha256": network.get("signature_sha256"),
        "source_zero_by_antisymmetry": False,
    }


@dataclass(frozen=True)
class BasisNetwork:
    key: str
    order_key: str
    tensors: tuple[dict[str, Any], ...]
    free_index_order: tuple[str, ...]

    def as_json(self) -> dict[str, Any]:
        return {
            "basis_key": self.key,
            "canonical_graph_serialization": self.order_key,
            "free_index_order": list(self.free_index_order),
            "canonical_tensors": [dict(tensor) for tensor in self.tensors],
        }


@dataclass(frozen=True)
class NormalizedNetwork:
    coefficient: Fraction
    basis: BasisNetwork | None
    metric_rewrite_count: int
    input_adapter: Mapping[str, Any]

    @property
    def is_zero(self) -> bool:
        return self.coefficient == 0 or self.basis is None


def _basis_rows(canonical: Mapping[str, Any]) -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for tensor in canonical["canonical_tensors"]:
        if tensor["kind"] == "c":
            rows.append(
                {
                    "kind": "c",
                    "ordered_indices": list(tensor["canonical_indices"]),
                }
            )
        else:
            rows.append(
                {
                    "kind": tensor["kind"],
                    "indices": list(tensor["indices"]),
                    "variance": tensor["variance"],
                }
            )
    rows.sort(key=canonical_json)
    return tuple(rows)


def normalize_network(network: Any) -> NormalizedNetwork:
    tensors, input_sign, adapter = adapt_network_input(network)
    if input_sign == 0:
        return NormalizedNetwork(Fraction(0), None, 0, adapter)
    if not tensors:
        raise ColorInputError("nonzero network cannot have an empty tensor product")
    try:
        color.validate_free_indices(tensors, expected=FREE_INDEX_ORDER)
        metric_reduction = color.reduce_metrics_exact(tensors)
        color.validate_free_indices(
            metric_reduction["tensors"], expected=FREE_INDEX_ORDER
        )
        canonical = color.canonicalize_network(
            metric_reduction["tensors"],
            fixed_indices=FREE_INDEX_ORDER,
            antisymmetry=True,
        )
    except color.ColorTensorError as error:
        raise ColorInputError(str(error)) from error
    if canonical["zero_by_antisymmetry"]:
        return NormalizedNetwork(
            Fraction(0), None, int(metric_reduction["rewrite_count"]), adapter
        )
    rows = _basis_rows(canonical)
    record = {
        "free_index_order": list(FREE_INDEX_ORDER),
        "canonical_tensors": list(rows),
    }
    order_key = canonical_json(record)
    basis = BasisNetwork(digest(record), order_key, rows, FREE_INDEX_ORDER)
    coefficient = input_sign * int(canonical["overall_antisymmetry_sign"])
    return NormalizedNetwork(
        Fraction(coefficient),
        basis,
        int(metric_reduction["rewrite_count"]),
        adapter,
    )


Polynomial = dict[str, Fraction]


def clean_polynomial(poly: Mapping[str, Fraction]) -> Polynomial:
    return {key: Fraction(value) for key, value in poly.items() if value != 0}


def add_polynomial(target: Polynomial, source: Mapping[str, Fraction], scale: Fraction = Fraction(1)) -> None:
    for key, coefficient in source.items():
        target[key] = target.get(key, Fraction(0)) + scale * coefficient
        if target[key] == 0:
            del target[key]


def polynomial_json(poly: Mapping[str, Fraction]) -> list[dict[str, Any]]:
    return [
        {"basis_key": key, "coefficient": fraction_json(poly[key])}
        for key in sorted(poly)
        if poly[key]
    ]


def canonical_relation(poly: Mapping[str, Fraction]) -> Polynomial:
    row = clean_polynomial(poly)
    if not row:
        return {}
    leading = max(row)
    scale = row[leading]
    return {key: value / scale for key, value in row.items()}


def relation_key(poly: Mapping[str, Fraction]) -> str:
    return digest(polynomial_json(canonical_relation(poly)))


def internal_c_edges(basis: BasisNetwork) -> list[dict[str, Any]]:
    tensors = list(basis.tensors)
    occurrences: dict[str, list[int]] = {}
    for position, tensor in enumerate(tensors):
        for index in tensor_indices(tensor):
            occurrences.setdefault(index, []).append(position)

    def other_tensor(index: str, current: int) -> int | None:
        rows = occurrences.get(index, [])
        if len(rows) == 1:
            return None
        if len(rows) != 2 or rows[0] == rows[1]:
            raise JacobiIncidenceError(
                f"dummy index {index} does not join exactly two tensor slots"
            )
        return rows[1] if rows[0] == current else rows[0]

    found: dict[str, dict[str, Any]] = {}
    for start_position, start_tensor in enumerate(tensors):
        if start_tensor["kind"] != "c":
            continue
        for start_index in tensor_indices(start_tensor):
            if start_index in FREE_INDEX_ORDER:
                continue
            current_position = start_position
            current_index = start_index
            bridge_positions: list[int] = []
            visited_states: set[tuple[int, str]] = set()
            while True:
                state = (current_position, current_index)
                if state in visited_states:
                    raise JacobiIncidenceError("closed metric-only cycle encountered")
                visited_states.add(state)
                next_position = other_tensor(current_index, current_position)
                if next_position is None:
                    break
                next_tensor = tensors[next_position]
                if next_tensor["kind"] == "c":
                    if next_position == start_position:
                        break
                    left_position, right_position = sorted(
                        (start_position, next_position)
                    )
                    if left_position == start_position:
                        left_index, right_index = start_index, current_index
                    else:
                        left_index, right_index = current_index, start_index
                    descriptor = {
                        "c_positions": [left_position, right_position],
                        "endpoint_indices": [left_index, right_index],
                        "bridge_metric_positions": sorted(bridge_positions),
                        "bridge_metric_kinds": [
                            tensors[position]["kind"]
                            for position in sorted(bridge_positions)
                        ],
                    }
                    descriptor["edge_id"] = digest(descriptor)
                    found.setdefault(descriptor["edge_id"], descriptor)
                    break
                if next_tensor["kind"] not in {"kappa", "kappa_inverse"}:
                    raise JacobiIncidenceError("color path reached a non-metric bivalent node")
                if next_position in bridge_positions:
                    raise JacobiIncidenceError("metric bridge repeats one tensor node")
                bridge_positions.append(next_position)
                metric_indices = tensor_indices(next_tensor)
                if metric_indices[0] == metric_indices[1]:
                    raise JacobiIncidenceError(
                        "closed metric trace requires an explicit adjoint-dimension rule"
                    )
                next_index = (
                    metric_indices[1]
                    if metric_indices[0] == current_index
                    else metric_indices[0]
                )
                current_position = next_position
                current_index = next_index
    return sorted(found.values(), key=lambda row: row["edge_id"])


def _replace_c_pair(
    basis: BasisNetwork,
    positions: tuple[int, int],
    first_indices: Sequence[str],
    second_indices: Sequence[str],
) -> list[dict[str, Any]]:
    output = [
        dict(tensor)
        for position, tensor in enumerate(basis.tensors)
        if position not in positions
    ]
    output.extend(
        [
            {"kind": "c", "ordered_indices": list(first_indices)},
            {"kind": "c", "ordered_indices": list(second_indices)},
        ]
    )
    return output


def jacobi_relation_for_edge(
    basis: BasisNetwork,
    edge: Mapping[str, Any],
) -> tuple[Polynomial, dict[str, BasisNetwork], dict[str, Any]]:
    edge_id = str(edge["edge_id"])
    first_position, second_position = map(int, edge["c_positions"])
    first_endpoint, second_endpoint = map(str, edge["endpoint_indices"])
    first = tensor_indices(basis.tensors[first_position])
    second = tensor_indices(basis.tensors[second_position])
    if first_endpoint not in first or second_endpoint not in second:
        raise JacobiIncidenceError("declared Jacobi edge is absent from one c node")
    a_b = [index for index in first if index != first_endpoint]
    c_d = [index for index in second if index != second_endpoint]
    if len(a_b) != 2 or len(c_d) != 2:
        raise JacobiIncidenceError("Jacobi endpoint must expose exactly four half-edges")
    a, b = a_b
    c, d = c_d
    local_terms = [
        ("I", (a, b, first_endpoint), (second_endpoint, c, d)),
        ("H", (b, c, first_endpoint), (second_endpoint, a, d)),
        ("X", (c, a, first_endpoint), (second_endpoint, b, d)),
    ]
    relation: Polynomial = {}
    registry: dict[str, BasisNetwork] = {}
    local_ledger = []
    for channel, left, right in local_terms:
        raw = _replace_c_pair(
            basis, (first_position, second_position), left, right
        )
        normalized = normalize_network(raw)
        if not normalized.is_zero:
            assert normalized.basis is not None
            relation[normalized.basis.key] = (
                relation.get(normalized.basis.key, Fraction(0))
                + normalized.coefficient
            )
            registry[normalized.basis.key] = normalized.basis
        local_ledger.append(
            {
                "channel": channel,
                "ordered_c_pair": [list(left), list(right)],
                "normalized_basis_key": (
                    None if normalized.basis is None else normalized.basis.key
                ),
                "normalized_coefficient": fraction_json(normalized.coefficient),
            }
        )
    relation = clean_polynomial(relation)
    record = {
        "source_basis_key": basis.key,
        "edge_id": edge_id,
        "c_positions": [first_position, second_position],
        "endpoint_indices": [first_endpoint, second_endpoint],
        "bridge_metric_positions": list(edge["bridge_metric_positions"]),
        "bridge_metric_kinds": list(edge["bridge_metric_kinds"]),
        "local_orientation": (
            "c[a,b,e]c[e,c,d]+c[b,c,e]c[e,a,d]+"
            "c[c,a,e]c[e,b,d]=0"
        ),
        "four_exposed_half_edges": [a, b, c, d],
        "local_terms": local_ledger,
        "canonical_relation": polynomial_json(canonical_relation(relation)),
        "relation_status": (
            "NONTRIVIAL_IHX_RELATION_CONTAINING_SOURCE"
            if relation and basis.key in relation
            else "NONTRIVIAL_IHX_RELATION_AFTER_ISOMORPHIC_CHANNEL_CANCELLATION"
            if relation
            else "TRIVIAL_ZERO_BY_ANTISYMMETRY_OR_GRAPH_AUTOMORPHISM"
        ),
    }
    record["relation_sha256"] = digest(record)
    return relation, registry, record


@dataclass
class JacobiOrbit:
    networks: dict[str, BasisNetwork]
    relations: list[Polynomial]
    relation_records: list[dict[str, Any]]
    start_keys: tuple[str, ...]

    def as_json(self) -> dict[str, Any]:
        return {
            "start_keys": list(self.start_keys),
            "basis_network_count": len(self.networks),
            "relation_count": len(self.relations),
            "basis_networks": [
                self.networks[key].as_json() for key in sorted(self.networks)
            ],
            "relations": sorted(
                self.relation_records, key=lambda row: row["relation_sha256"]
            ),
        }


def build_jacobi_orbit(
    starting_networks: Iterable[BasisNetwork],
    *,
    max_orbit_size: int = MAX_ORBIT_SIZE,
) -> JacobiOrbit:
    networks = {network.key: network for network in starting_networks}
    start_keys = tuple(sorted(networks))
    queue = deque(start_keys)
    expanded: set[str] = set()
    relations_by_serialization: dict[str, Polynomial] = {}
    records_by_serialization: dict[str, dict[str, Any]] = {}
    while queue:
        key = queue.popleft()
        if key in expanded:
            continue
        expanded.add(key)
        basis = networks[key]
        for edge in internal_c_edges(basis):
            relation, new_networks, record = jacobi_relation_for_edge(basis, edge)
            if relation:
                canonical = canonical_relation(relation)
                serialization = canonical_json(polynomial_json(canonical))
                relations_by_serialization.setdefault(serialization, canonical)
                records_by_serialization.setdefault(serialization, record)
            for new_key, network in new_networks.items():
                if new_key in networks:
                    if networks[new_key].order_key != network.order_key:
                        raise RewriteSystemError("canonical graph digest collision")
                    continue
                if len(networks) >= max_orbit_size:
                    raise OrbitLimitError(
                        f"Jacobi orbit exceeds certified bound {max_orbit_size}"
                    )
                networks[new_key] = network
                queue.append(new_key)
    return JacobiOrbit(
        networks,
        [
            relations_by_serialization[key]
            for key in sorted(relations_by_serialization)
        ],
        [
            records_by_serialization[key]
            for key in sorted(records_by_serialization)
        ],
        start_keys,
    )


def exact_rref_rewrite_rules(
    orbit: JacobiOrbit,
) -> tuple[dict[str, Polynomial], list[dict[str, Any]]]:
    """Orient exact RREF pivots from larger graph keys to smaller graph keys."""
    order_keys = {key: network.order_key for key, network in orbit.networks.items()}
    columns = sorted(
        orbit.networks, key=lambda key: order_keys[key], reverse=True
    )
    rows = [clean_polynomial(relation) for relation in orbit.relations]
    rows.sort(key=lambda row: canonical_json(polynomial_json(row)))
    pivot_row = 0
    pivots: list[str] = []
    for column in columns:
        candidate = next(
            (position for position in range(pivot_row, len(rows)) if rows[position].get(column)),
            None,
        )
        if candidate is None:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = {
            key: value / pivot_value for key, value in rows[pivot_row].items()
        }
        for position in range(len(rows)):
            if position == pivot_row:
                continue
            factor = rows[position].get(column, Fraction(0))
            if factor:
                add_polynomial(rows[position], rows[pivot_row], -factor)
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break

    nonzero_rows = [clean_polynomial(row) for row in rows if clean_polynomial(row)]
    if len(nonzero_rows) != len(pivots):
        raise RewriteSystemError("RREF rank ledger is inconsistent")
    rules: dict[str, Polynomial] = {}
    ledger: list[dict[str, Any]] = []
    for row, pivot in zip(nonzero_rows, pivots, strict=True):
        if row.get(pivot) != 1:
            raise RewriteSystemError("RREF pivot is not normalized to one")
        rhs = {key: -value for key, value in row.items() if key != pivot}
        if any(order_keys[key] >= order_keys[pivot] for key in rhs):
            raise RewriteSystemError("oriented Jacobi rewrite does not decrease graph order")
        rules[pivot] = rhs
        ledger.append(
            {
                "pivot_basis_key": pivot,
                "pivot_canonical_graph_serialization": order_keys[pivot],
                "replacement": polynomial_json(rhs),
                "replacement_canonical_graph_serializations": [
                    {
                        "basis_key": key,
                        "canonical_graph_serialization": order_keys[key],
                    }
                    for key in sorted(rhs, key=lambda item: order_keys[item])
                ],
                "all_replacement_keys_strictly_smaller": True,
            }
        )
    return rules, ledger


def reduce_polynomial(
    poly: Mapping[str, Fraction],
    rules: Mapping[str, Polynomial],
    order_keys: Mapping[str, str],
) -> Polynomial:
    result = clean_polynomial(poly)
    for pivot in sorted(rules, key=lambda key: order_keys[key], reverse=True):
        coefficient = result.pop(pivot, Fraction(0))
        if coefficient:
            add_polynomial(result, rules[pivot], coefficient)
    if set(result) & set(rules):
        raise RewriteSystemError("a reducible pivot remains after ordered reduction")
    return clean_polynomial(result)


def canonicalize_expression(
    terms: Sequence[Mapping[str, Any]],
    *,
    max_orbit_size: int = MAX_ORBIT_SIZE,
) -> dict[str, Any]:
    if not terms:
        raise ColorInputError("color expression requires at least one term")
    input_polynomial: Polynomial = {}
    registry: dict[str, BasisNetwork] = {}
    normalization_ledger = []
    for ordinal, term in enumerate(terms):
        if not isinstance(term, Mapping) or "network" not in term:
            raise ColorInputError("expression term requires a network")
        coefficient = parse_fraction(term.get("coefficient", 1))
        normalized = normalize_network(term["network"])
        total = coefficient * normalized.coefficient
        if total and normalized.basis is not None:
            input_polynomial[normalized.basis.key] = (
                input_polynomial.get(normalized.basis.key, Fraction(0)) + total
            )
            registry[normalized.basis.key] = normalized.basis
        normalization_ledger.append(
            {
                "term_ordinal": ordinal,
                "input_coefficient": fraction_json(coefficient),
                "normalization_sign": fraction_json(normalized.coefficient),
                "basis_key": None if normalized.basis is None else normalized.basis.key,
                "metric_rewrite_count": normalized.metric_rewrite_count,
                "input_adapter": dict(normalized.input_adapter),
            }
        )
    input_polynomial = clean_polynomial(input_polynomial)
    if not registry:
        return {
            "schema": "step6.color_jacobi.normal_form.v1",
            "input_normalization": normalization_ledger,
            "normalized_input": [],
            "orbit": {
                "start_keys": [],
                "basis_network_count": 0,
                "relation_count": 0,
                "basis_networks": [],
                "relations": [],
            },
            "termination_order": "DESCENDING_LEXICOGRAPHIC_BASIS_KEY",
            "rewrite_rules": [],
            "normal_form": [],
            "zero_in_jacobi_quotient": True,
            "adjoint_Casimir_status": ADJOINT_CASIMIR_STATUS,
        }
    orbit = build_jacobi_orbit(registry.values(), max_orbit_size=max_orbit_size)
    rules, rule_ledger = exact_rref_rewrite_rules(orbit)
    order_keys = {key: network.order_key for key, network in orbit.networks.items()}
    normal_form = reduce_polynomial(input_polynomial, rules, order_keys)
    result = {
        "schema": "step6.color_jacobi.normal_form.v1",
        "input_normalization": normalization_ledger,
        "normalized_input": polynomial_json(input_polynomial),
        "orbit": orbit.as_json(),
        "termination_order": (
            "DESCENDING_LEXICOGRAPHIC_CANONICAL_GRAPH_SERIALIZATION;"
            "EACH_RHS_KEY_IS_STRICTLY_SMALLER_THAN_ITS_PIVOT"
        ),
        "relation_matrix_rank": len(rules),
        "rewrite_rules": rule_ledger,
        "normal_form": polynomial_json(normal_form),
        "irreducible_basis_networks": [
            orbit.networks[key].as_json() for key in sorted(normal_form)
        ],
        "zero_in_jacobi_quotient": not normal_form,
        "adjoint_Casimir_status": ADJOINT_CASIMIR_STATUS,
        "numerator_or_integral_used": False,
        "external_target_used": False,
    }
    result["normal_form_sha256"] = digest(
        {
            "normal_form": result["normal_form"],
            "irreducible_basis_networks": result["irreducible_basis_networks"],
        }
    )
    return result


def one_step_rhs(relation: Mapping[str, Fraction], source_key: str) -> Polynomial:
    coefficient = Fraction(relation.get(source_key, 0))
    if not coefficient:
        raise RewriteSystemError("local relation cannot solve for source graph")
    return {
        key: -value / coefficient
        for key, value in relation.items()
        if key != source_key and value
    }


def critical_pair_certificates(network: Any) -> list[dict[str, Any]]:
    normalized = normalize_network(network)
    if normalized.is_zero or normalized.basis is None:
        raise RewriteSystemError("critical-pair source is zero")
    source = normalized.basis
    edges = internal_c_edges(source)
    if len(edges) < 2:
        raise RewriteSystemError("critical-pair source has fewer than two Jacobi edges")
    orbit = build_jacobi_orbit([source])
    rules, _ = exact_rref_rewrite_rules(orbit)
    order_keys = {key: network.order_key for key, network in orbit.networks.items()}
    source_normal = reduce_polynomial({source.key: Fraction(1)}, rules, order_keys)

    edge_relations: dict[str, Polynomial] = {}
    edge_vertices: dict[str, set[int]] = {}
    for edge in edges:
        relation, _, _ = jacobi_relation_for_edge(source, edge)
        if not relation or source.key not in relation:
            continue
        edge_relations[str(edge["edge_id"])] = relation
        edge_vertices[str(edge["edge_id"])] = set(map(int, edge["c_positions"]))

    certificates = []
    edge_names = sorted(edge_relations)
    for left_position, left in enumerate(edge_names):
        for right in edge_names[left_position + 1 :]:
            shared_vertices = sorted(edge_vertices[left] & edge_vertices[right])
            if not shared_vertices:
                continue
            left_branch = one_step_rhs(edge_relations[left], source.key)
            right_branch = one_step_rhs(edge_relations[right], source.key)
            left_normal = reduce_polynomial(left_branch, rules, order_keys)
            right_normal = reduce_polynomial(right_branch, rules, order_keys)
            joined = left_normal == right_normal == source_normal
            certificates.append(
                {
                    "overlap_edges": [left, right],
                    "shared_c_positions": shared_vertices,
                    "left_one_step_rhs": polynomial_json(left_branch),
                    "right_one_step_rhs": polynomial_json(right_branch),
                    "left_normal_form": polynomial_json(left_normal),
                    "right_normal_form": polynomial_json(right_normal),
                    "source_normal_form": polynomial_json(source_normal),
                    "joinable": joined,
                }
            )
    if not certificates:
        raise RewriteSystemError("no overlapping Jacobi critical pair was found")
    if not all(row["joinable"] for row in certificates):
        raise RewriteSystemError("one Jacobi critical pair is not joinable")
    return certificates


def c(a: str, b: str, c_: str) -> dict[str, Any]:
    return {"kind": "c", "ordered_indices": [a, b, c_]}


def jacobi_three_term_fixture() -> list[dict[str, Any]]:
    return [
        {"coefficient": 1, "network": [c("A", "B", "x"), c("x", "R", "S")]},
        {"coefficient": 1, "network": [c("B", "R", "x"), c("x", "A", "S")]},
        {"coefficient": 1, "network": [c("R", "A", "x"), c("x", "B", "S")]},
    ]


def metric_bridged_jacobi_fixture() -> list[dict[str, Any]]:
    bridge = {
        "kind": "kappa_inverse",
        "indices": ["x", "y"],
        "variance": "upper",
    }
    return [
        {
            "coefficient": 1,
            "network": [c("A", "B", "x"), dict(bridge), c("y", "R", "S")],
        },
        {
            "coefficient": 1,
            "network": [c("B", "R", "x"), dict(bridge), c("y", "A", "S")],
        },
        {
            "coefficient": 1,
            "network": [c("R", "A", "x"), dict(bridge), c("y", "B", "S")],
        },
    ]


def square_critical_fixture() -> list[dict[str, Any]]:
    return [
        c("A", "x", "w"),
        c("B", "y", "x"),
        c("R", "z", "y"),
        c("S", "w", "z"),
    ]


def metric_contraction_fixture() -> list[dict[str, Any]]:
    return [
        c("A", "B", "x"),
        c("x", "R", "u"),
        {"kind": "kappa", "indices": ["u", "v"], "variance": "lower"},
        {
            "kind": "kappa_inverse",
            "indices": ["v", "S"],
            "variance": "upper",
        },
    ]


def levi_civita3(a: int, b: int, c_: int) -> int:
    if len({a, b, c_}) < 3:
        return 0
    permutation = (a, b, c_)
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def su2_jacobi_component_oracle() -> dict[str, Any]:
    failures = []
    checked = 0
    for a in range(3):
        for b in range(3):
            for r in range(3):
                for s in range(3):
                    value = sum(
                        levi_civita3(a, b, e) * levi_civita3(e, r, s)
                        + levi_civita3(b, r, e) * levi_civita3(e, a, s)
                        + levi_civita3(r, a, e) * levi_civita3(e, b, s)
                        for e in range(3)
                    )
                    checked += 1
                    if value:
                        failures.append({"indices": [a, b, r, s], "value": value})
    return {
        "oracle": "integer Levi-Civita components in three dimensions",
        "component_assignments_checked": checked,
        "failures": failures,
        "passed": not failures,
        "used_as_normalization_input": False,
    }


def build_fixtures() -> dict[str, Any]:
    jacobi = canonicalize_expression(jacobi_three_term_fixture())
    metric_bridged_jacobi = canonicalize_expression(metric_bridged_jacobi_fixture())
    metric_normalized = normalize_network(metric_contraction_fixture())
    if metric_normalized.basis is None:
        raise RewriteSystemError("metric contraction fixture vanished")
    full_schema = color.canonicalize_network(
        [c("A", "B", "x"), c("x", "R", "S")],
        fixed_indices=FREE_INDEX_ORDER,
        antisymmetry=True,
    )
    adapted = normalize_network(full_schema)
    raw = normalize_network([c("A", "B", "x"), c("x", "R", "S")])
    metric_raw_network = metric_bridged_jacobi_fixture()[0]["network"]
    metric_full_schema = color.canonicalize_network(
        metric_raw_network,
        fixed_indices=FREE_INDEX_ORDER,
        antisymmetry=True,
    )
    metric_adapted = normalize_network(metric_full_schema)
    metric_raw = normalize_network(metric_raw_network)
    if metric_adapted.basis is None:
        raise RewriteSystemError("metric-bridged full schema adapter vanished")
    metric_edges = internal_c_edges(metric_adapted.basis)
    return {
        "jacobi_three_term": jacobi,
        "metric_bridged_jacobi_three_term": metric_bridged_jacobi,
        "metric_contraction": {
            "input": metric_contraction_fixture(),
            "metric_rewrite_count": metric_normalized.metric_rewrite_count,
            "normalized": metric_normalized.basis.as_json(),
            "normalization_coefficient": fraction_json(metric_normalized.coefficient),
        },
        "full_compiler_schema_adapter": {
            "input_schema": full_schema,
            "adapted_basis_key": None if adapted.basis is None else adapted.basis.key,
            "raw_basis_key": None if raw.basis is None else raw.basis.key,
            "adapted_coefficient": fraction_json(adapted.coefficient),
            "raw_coefficient": fraction_json(raw.coefficient),
            "exact_match": (
                adapted.basis is not None
                and raw.basis is not None
                and adapted.basis.key == raw.basis.key
                and adapted.coefficient == raw.coefficient
            ),
            "metric_bridged_schema": {
                "input_schema": metric_full_schema,
                "adapted_basis_key": metric_adapted.basis.key,
                "raw_basis_key": None if metric_raw.basis is None else metric_raw.basis.key,
                "exact_match": (
                    metric_raw.basis is not None
                    and metric_adapted.basis.key == metric_raw.basis.key
                    and metric_adapted.coefficient == metric_raw.coefficient
                ),
                "internal_edge_count": len(metric_edges),
                "bridge_metric_positions": [
                    edge["bridge_metric_positions"] for edge in metric_edges
                ],
            },
        },
        "critical_pairs": critical_pair_certificates(square_critical_fixture()),
        "component_oracle": su2_jacobi_component_oracle(),
    }


def build_payload() -> dict[str, Any]:
    fixtures = build_fixtures()
    return {
        "schema": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "input_firewall": {
            "allowed_tensor_nodes": ["c", "kappa", "kappa_inverse"],
            "accepted_upstream_schema": color.SCHEMA_VERSION,
            "external_target_read": False,
            "review_result_read": False,
        },
        "algebra_contract": {
            "antisymmetry": "c[a,b,c]=sgn(pi)c[pi(a,b,c)]",
            "jacobi": (
                "c[a,b,e]c[e,c,d]+c[b,c,e]c[e,a,d]+"
                "c[c,a,e]c[e,b,d]=0"
            ),
            "operation_order": [
                "KAPPA_KAPPA_INVERSE_CONTRACTION",
                "TOTAL_ANTISYMMETRY_AND_DUMMY_CANONICALIZATION",
                "FINITE_IHX_ORBIT",
                "EXACT_RATIONAL_RREF",
                "DESCENDING_ORIENTED_REWRITE",
            ],
            "termination_order": (
                "DESCENDING_LEXICOGRAPHIC_CANONICAL_GRAPH_SERIALIZATION;"
                "EVERY_REPLACEMENT_KEY_STRICTLY_SMALLER"
            ),
            "critical_pair_policy": "EXACT_RREF_NORMAL_FORM_JOINABILITY",
            "adjoint_Casimir": {
                "status": ADJOINT_CASIMIR_STATUS,
                "rewrite_applied": False,
                "unreduced_closed_two_c_subgraphs_preserved": True,
            },
        },
        "fixtures": fixtures,
        "terminal_blocks": {
            "numerator": None,
            "integral": None,
            "UV_pole": None,
            "anomaly_coefficient": None,
            "external_target_comparison": None,
            "status": "OUT_OF_SCOPE_NO_PHYSICS_COEFFICIENT_CLAIM",
        },
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    fixtures = payload["fixtures"]
    jacobi = fixtures["jacobi_three_term"]
    checks = []

    def check(name: str, passed: bool, evidence: Any) -> None:
        checks.append(
            {"name": name, "status": "PASS" if passed else "FAIL", "evidence": evidence}
        )

    check(
        "jacobi_three_term_is_exact_zero",
        jacobi["zero_in_jacobi_quotient"] and jacobi["normal_form"] == [],
        jacobi["normal_form"],
    )
    check(
        "jacobi_orbit_has_exact_relation",
        jacobi["orbit"]["basis_network_count"] == 3
        and jacobi["orbit"]["relation_count"] == 1
        and jacobi["relation_matrix_rank"] == 1,
        {
            "basis": jacobi["orbit"]["basis_network_count"],
            "relations": jacobi["orbit"]["relation_count"],
            "rank": jacobi["relation_matrix_rank"],
        },
    )
    metric_jacobi = fixtures["metric_bridged_jacobi_three_term"]
    check(
        "metric_bridged_jacobi_is_exact_zero",
        metric_jacobi["zero_in_jacobi_quotient"]
        and metric_jacobi["normal_form"] == []
        and any(
            relation["bridge_metric_positions"]
            for relation in metric_jacobi["orbit"]["relations"]
        ),
        {
            "normal_form": metric_jacobi["normal_form"],
            "relations": metric_jacobi["orbit"]["relations"],
        },
    )
    check(
        "all_oriented_rules_strictly_decrease",
        all(
            row["all_replacement_keys_strictly_smaller"]
            for row in jacobi["rewrite_rules"]
        ),
        jacobi["rewrite_rules"],
    )
    check(
        "metric_contraction_precedes_jacobi",
        fixtures["metric_contraction"]["metric_rewrite_count"] == 1,
        fixtures["metric_contraction"]["metric_rewrite_count"],
    )
    check(
        "full_compiler_canonical_schema_is_accepted_exactly",
        fixtures["full_compiler_schema_adapter"]["exact_match"]
        and fixtures["full_compiler_schema_adapter"]["metric_bridged_schema"][
            "exact_match"
        ]
        and fixtures["full_compiler_schema_adapter"]["metric_bridged_schema"][
            "internal_edge_count"
        ]
        == 1,
        fixtures["full_compiler_schema_adapter"],
    )
    check(
        "all_critical_pairs_join",
        len(fixtures["critical_pairs"]) >= 4
        and all(row["joinable"] for row in fixtures["critical_pairs"]),
        fixtures["critical_pairs"],
    )
    check(
        "integer_component_oracle_passes",
        fixtures["component_oracle"]["passed"]
        and fixtures["component_oracle"]["component_assignments_checked"] == 81,
        fixtures["component_oracle"],
    )
    check(
        "adjoint_Casimir_not_imported",
        payload["algebra_contract"]["adjoint_Casimir"]["status"]
        == ADJOINT_CASIMIR_STATUS
        and not payload["algebra_contract"]["adjoint_Casimir"]["rewrite_applied"],
        payload["algebra_contract"]["adjoint_Casimir"],
    )
    check(
        "no_external_target",
        not payload["input_firewall"]["external_target_read"],
        payload["input_firewall"],
    )
    check(
        "no_downstream_physics_result",
        all(
            payload["terminal_blocks"][key] is None
            for key in (
                "numerator",
                "integral",
                "UV_pole",
                "anomaly_coefficient",
                "external_target_comparison",
            )
        ),
        payload["terminal_blocks"],
    )
    failed = sum(row["status"] == "FAIL" for row in checks)
    return {
        "schema": "step6.color_jacobi.audit.v1",
        "status": "PASS" if failed == 0 else "FAIL",
        "checks": checks,
        "totals": {"checks": len(checks), "failed": failed},
        "payload_sha256": digest(payload),
    }


def render_markdown(payload: Mapping[str, Any]) -> str:
    jacobi = payload["fixtures"]["jacobi_three_term"]
    critical = payload["fixtures"]["critical_pairs"]
    return rf"""# Step 6 exact color/Jacobi canonicalizer

`{STATUS}`

## 1. Tensor algebra

$$
c_{{abc}}=-c_{{bac}}=-c_{{acb}},
$$

$$
\kappa_{{ab}}\kappa^{{ac}}=\delta_b^c.
$$

$$
c_{{abe}}c_{{ecd}}
+c_{{bce}}c_{{ead}}
+c_{{cae}}c_{{ebd}}=0.
$$

## 2. Rewrite order

$$
\kappa\text{{ contraction}}
\longrightarrow
c\text{{ antisymmetry}}
\longrightarrow
\operatorname{{IHX\ orbit}}
\longrightarrow
\operatorname{{RREF}}_{{\mathbb Q}}.
$$

For every pivot graph $G_p$,

$$
G_p\longrightarrow\sum_{{G_j<G_p}}r_jG_j,
\qquad r_j\in\mathbb Q.
$$

## 3. Jacobi fixture

$$
c_{{ABe}}c_{{eRS}}
+c_{{BRe}}c_{{eAS}}
+c_{{RAe}}c_{{eBS}}=0.
$$

$$
\#\mathcal O={jacobi['orbit']['basis_network_count']},
\qquad
\operatorname{{rank}}R={jacobi['relation_matrix_rank']},
\qquad
\operatorname{{NF}}=0.
$$

## 4. Critical pairs

$$
\#\operatorname{{overlap}}={len(critical)},
\qquad
\operatorname{{NF}}(\text{{left branch}})
=\operatorname{{NF}}(\text{{right branch}}).
$$

Adjoint-Casimir reduction: `{ADJOINT_CASIMIR_STATUS}`.

No numerator, integral, UV pole, or anomaly coefficient is evaluated.
"""


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError("Step-6 color/Jacobi audit failed")
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload), encoding="utf-8")
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload, audit


if __name__ == "__main__":
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "checks": audit["totals"]["checks"],
                "jacobi_zero": payload["fixtures"]["jacobi_three_term"][
                    "zero_in_jacobi_quotient"
                ],
                "critical_pairs": len(payload["fixtures"]["critical_pairs"]),
            },
            sort_keys=True,
        )
    )
