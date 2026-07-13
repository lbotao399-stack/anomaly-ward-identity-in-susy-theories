#!/usr/bin/env python3
"""Exact Step-6 two-loop topology and momentum-routing certificates.

This module deliberately stops before propagators, ordered interaction
coefficients, Wick signs, D-algebra, loop integration, subtraction, and the
renormalized coefficient.  The twelve solutions of the valence equation are
classified as ``VALENCE_NOT_GRAPH``; only the three explicitly constructed
port-saturated objects are GraphIR records.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = "step6.two_loop_graphir.v1"
STAGE = "TOPOLOGY_AND_ROUTING_ONLY"
MOMENTUM_BASIS = ("k", "l", "P", "p1", "p2")
MOMENTUM_RELATION = (0, 0, 1, 1, 1)  # P+p1+p2=0
SQUARE_SPACE = "PROJECT_EUCLIDEAN_DRED_HAT_MOMENTUM_SUBSPACE"
N_EXTERNAL_BACKGROUND = 2


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def vec(**coefficients: int) -> tuple[int, ...]:
    unknown = set(coefficients) - set(MOMENTUM_BASIS)
    if unknown:
        raise ValueError(f"unknown momentum symbols: {sorted(unknown)}")
    return tuple(int(coefficients.get(symbol, 0)) for symbol in MOMENTUM_BASIS)


def add(*vectors: Sequence[int]) -> tuple[int, ...]:
    return tuple(sum(vector[index] for vector in vectors) for index in range(len(MOMENTUM_BASIS)))


def scale(coefficient: int, vector: Sequence[int]) -> tuple[int, ...]:
    return tuple(coefficient * entry for entry in vector)


def reduce_by_external_relation(vector: Sequence[int]) -> tuple[int, ...]:
    """Substitute P=-p1-p2 and retain the ordered basis (k,l,p1,p2)."""

    k, l, source, p1, p2 = vector
    return (k, l, p1 - source, p2 - source)


def relation_multiple(vector: Sequence[int]) -> int | None:
    if vector[0] != 0 or vector[1] != 0:
        return None
    if vector[2] == vector[3] == vector[4]:
        return int(vector[2])
    return None


def linear_ast(vector: Sequence[int]) -> dict[str, Any]:
    return {
        "op": "integer_linear_combination",
        "basis": list(MOMENTUM_BASIS),
        "terms": [
            {"symbol": symbol, "coefficient": int(coefficient)}
            for symbol, coefficient in zip(MOMENTUM_BASIS, vector)
            if coefficient
        ],
    }


def render_linear(vector: Sequence[int]) -> str:
    terms: list[str] = []
    for symbol, coefficient in zip(MOMENTUM_BASIS, vector):
        if not coefficient:
            continue
        magnitude = abs(coefficient)
        body = symbol if magnitude == 1 else f"{magnitude}*{symbol}"
        if not terms:
            terms.append(body if coefficient > 0 else f"-{body}")
        else:
            terms.append(("+" if coefficient > 0 else "-") + body)
    return "".join(terms) or "0"


def canonical_square_argument(vector: Sequence[int]) -> tuple[int, ...]:
    for coefficient in vector:
        if coefficient > 0:
            return tuple(vector)
        if coefficient < 0:
            return scale(-1, vector)
    raise ValueError("a propagator denominator cannot carry zero momentum")


def render_square(vector: Sequence[int]) -> str:
    expression = render_linear(canonical_square_argument(vector))
    if sum(1 for coefficient in canonical_square_argument(vector) if coefficient) == 1:
        return f"{expression}^2"
    return f"({expression})^2"


def matrix_rank_integer(matrix: Sequence[Sequence[int]]) -> int:
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_columns = len(rows[0])
    pivot_row = 0
    for column in range(n_columns):
        pivot = next((row for row in range(pivot_row, n_rows) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [
                rows[row][index] - factor * rows[pivot_row][index]
                for index in range(n_columns)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def enumerate_valence_families() -> list[dict[str, Any]]:
    families: list[dict[str, Any]] = []
    for m in range(2, 7):
        for n3, n4, n5, n6 in product(range(5), repeat=4):
            counts = {3: n3, 4: n4, 5: n5, 6: n6}
            lhs = (m - 2) + sum((r - 2) * count for r, count in counts.items())
            if lhs != 4:
                continue
            action_word = [f"S{r}^{count}" for r, count in counts.items() if count]
            total_half_edges = m + sum(r * count for r, count in counts.items())
            if (total_half_edges - N_EXTERNAL_BACKGROUND) % 2:
                raise AssertionError("the exact half-edge identity must give an integer I")
            internal_edges = (total_half_edges - N_EXTERNAL_BACKGROUND) // 2
            vertices = 1 + sum(counts.values())
            loops = internal_edges - vertices + 1
            family = {
                "family_id": f"I{m}__" + ("__".join(action_word) if action_word else "NO_ACTION_VERTEX"),
                "classification": "VALENCE_NOT_GRAPH",
                "insertion": {"family": f"I{m}", "total_valence": m},
                "action_vertex_multiplicities": {f"S{r}": count for r, count in counts.items() if count},
                "typed_valence_totals": {
                    "total_valence": total_half_edges,
                    "background_valence": N_EXTERNAL_BACKGROUND,
                    "quantum_valence": 2 * internal_edges,
                    "background_distribution": "UNRESOLVED",
                },
                "identity": {
                    "lhs": lhs,
                    "rhs": 2 * loops + N_EXTERNAL_BACKGROUND - 2,
                    "required_value": 4,
                    "V": vertices,
                    "I": internal_edges,
                    "L": loops,
                    "loop_identity": f"{loops}={internal_edges}-{vertices}+1",
                    "half_edge_identity": f"{total_half_edges}=2*{internal_edges}+{N_EXTERNAL_BACKGROUND}",
                },
                "graph_ir": None,
                "blocked_reason": (
                    "NO_BACKGROUND_DISTRIBUTION_NO_TYPED_PORTS_NO_WICK_PAIRING_NO_CONNECTIVITY"
                ),
            }
            families.append(family)
    families.sort(
        key=lambda family: (
            family["insertion"]["total_valence"],
            -sum(family["action_vertex_multiplicities"].values()),
            family["family_id"],
        )
    )
    if len(families) != 12:
        raise AssertionError(f"expected twelve valence families, found {len(families)}")
    return families


def _connected(vertex_ids: Sequence[str], edges: Sequence[Mapping[str, Any]]) -> bool:
    adjacency = {vertex: set() for vertex in vertex_ids}
    for edge in edges:
        adjacency[edge["source"]].add(edge["target"])
        adjacency[edge["target"]].add(edge["source"])
    reached = {vertex_ids[0]}
    frontier = [vertex_ids[0]]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - reached:
            reached.add(neighbor)
            frontier.append(neighbor)
    return reached == set(vertex_ids)


def _assign_quantum_ports(
    vertices: list[dict[str, Any]], edges: list[dict[str, Any]]
) -> dict[str, Any]:
    by_id = {vertex["vertex_id"]: vertex for vertex in vertices}
    used: dict[str, int] = {vertex_id: 0 for vertex_id in by_id}
    for edge in edges:
        endpoints: list[dict[str, str]] = []
        for endpoint_name in ("source", "target"):
            vertex_id = edge[endpoint_name]
            slot = used[vertex_id]
            used[vertex_id] += 1
            endpoints.append({"vertex_id": vertex_id, "port_id": f"{vertex_id}.q{slot}"})
        edge["source_port"] = endpoints[0]["port_id"]
        edge["target_port"] = endpoints[1]["port_id"]
    all_ports: list[str] = []
    used_ports: list[str] = []
    for vertex in vertices:
        expected = vertex["quantum_valence"]
        actual = used[vertex["vertex_id"]]
        if actual != expected:
            raise ValueError(
                f"{vertex['vertex_id']} has quantum valence {expected} but graph degree {actual}"
            )
        vertex["quantum_ports"] = [f"{vertex['vertex_id']}.q{slot}" for slot in range(expected)]
        all_ports.extend(vertex["quantum_ports"])
    for edge in edges:
        used_ports.extend((edge["source_port"], edge["target_port"]))
    return {
        "all_quantum_ports": sorted(all_ports),
        "edge_endpoint_ports": sorted(used_ports),
        "each_quantum_port_used_once": sorted(all_ports) == sorted(used_ports)
        and len(used_ports) == len(set(used_ports)),
    }


def _incidence_and_routing(
    vertices: Sequence[Mapping[str, Any]], edges: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    vertex_ids = [vertex["vertex_id"] for vertex in vertices]
    edge_ids = [edge["edge_id"] for edge in edges]
    incidence: list[list[int]] = []
    balances: dict[str, Any] = {}
    for vertex in vertices:
        row = [
            1 if edge["source"] == vertex["vertex_id"] else -1 if edge["target"] == vertex["vertex_id"] else 0
            for edge in edges
        ]
        incidence.append(row)
        internal = tuple(
            sum(row[index] * edges[index]["momentum_vector"][component] for index in range(len(edges)))
            for component in range(len(MOMENTUM_BASIS))
        )
        injection_vectors = [tuple(injection["momentum_vector"]) for injection in vertex["momentum_injections"]]
        balance = add(internal, *injection_vectors) if injection_vectors else internal
        reduced = reduce_by_external_relation(balance)
        multiple = relation_multiple(balance)
        balances[vertex["vertex_id"]] = {
            "raw_balance": list(balance),
            "raw_balance_rendered": render_linear(balance),
            "relation_multiple": multiple,
            "reduced_basis": ["k", "l", "p1", "p2"],
            "reduced_balance": list(reduced),
            "passed": reduced == (0, 0, 0, 0),
        }
    columns_valid = all(
        sorted(row[column] for row in incidence) == [-1, *([0] * (len(vertices) - 2)), 1]
        for column in range(len(edges))
    )
    return {
        "convention": "B[v,e]=+1_at_source,-1_at_target; B*r+j=0 modulo P+p1+p2=0",
        "vertex_order": vertex_ids,
        "edge_order": edge_ids,
        "matrix": incidence,
        "rank": matrix_rank_integer(incidence),
        "expected_connected_rank": len(vertices) - 1,
        "each_column_has_one_source_and_one_target": columns_valid,
        "vertex_conservation": balances,
        "passed": columns_valid
        and matrix_rank_integer(incidence) == len(vertices) - 1
        and all(balance["passed"] for balance in balances.values()),
    }


def _denominator_ast(edges: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    factors: list[dict[str, Any]] = []
    rendered: list[str] = []
    for edge in edges:
        canonical_argument = canonical_square_argument(edge["momentum_vector"])
        factors.append(
            {
                "op": "power",
                "exponent": 1,
                "base": {
                    "op": "square",
                    "bilinear_form": "POSITIVE_EUCLIDEAN",
                    "space": SQUARE_SPACE,
                    "argument": linear_ast(canonical_argument),
                },
                "edge_id": edge["edge_id"],
            }
        )
        rendered.append(render_square(edge["momentum_vector"]))
    return {
        "op": "product",
        "factors": factors,
        "rendered": " ".join(rendered),
        "all_powers": [1 for _ in factors],
    }


def _simple_cycles(
    vertices: Sequence[Mapping[str, Any]],
    edges: Sequence[Mapping[str, Any]],
    labels: Mapping[frozenset[str], str],
) -> dict[str, Any]:
    vertex_ids = [vertex["vertex_id"] for vertex in vertices]
    found: list[frozenset[str]] = []
    for size in range(3, len(edges) + 1):
        for subset in combinations(edges, size):
            degrees = {vertex: 0 for vertex in vertex_ids}
            used_vertices: set[str] = set()
            for edge in subset:
                degrees[edge["source"]] += 1
                degrees[edge["target"]] += 1
                used_vertices.update((edge["source"], edge["target"]))
            if not used_vertices or any(degrees[vertex] != 2 for vertex in used_vertices):
                continue
            if any(degrees[vertex] != 0 for vertex in set(vertex_ids) - used_vertices):
                continue
            if not _connected(sorted(used_vertices), subset):
                continue
            if len(subset) - len(used_vertices) + 1 != 1:
                continue
            found.append(frozenset(edge["edge_id"] for edge in subset))
    expected_sets = set(labels)
    if set(found) != expected_sets:
        raise ValueError(
            f"cycle enumeration mismatch: found={sorted(map(sorted, found))} expected={sorted(map(sorted, expected_sets))}"
        )
    cycles: list[dict[str, Any]] = []
    label_order = {"left": 0, "right": 1, "outer": 2}
    for edge_set in sorted(found, key=lambda item: (label_order[labels[item]], sorted(item))):
        record = {
            "cycle_id": labels[edge_set],
            "edge_ids": sorted(edge_set),
            "one_loop_rank": 1,
        }
        record["cycle_hash"] = digest(record)
        cycles.append(record)
    overlaps: list[dict[str, Any]] = []
    by_name = {cycle["cycle_id"]: set(cycle["edge_ids"]) for cycle in cycles}
    for left, right in combinations(cycles, 2):
        left_set = set(left["edge_ids"])
        right_set = set(right["edge_ids"])
        intersection = sorted(left_set & right_set)
        symmetric_difference = left_set ^ right_set
        third = next(
            (name for name, edge_set in by_name.items() if edge_set == symmetric_difference),
            None,
        )
        overlaps.append(
            {
                "cycle_pair": [left["cycle_id"], right["cycle_id"]],
                "intersection_edge_ids": intersection,
                "edge_disjoint": not intersection,
                "left_subset_right": left_set < right_set,
                "right_subset_left": right_set < left_set,
                "relation": "OVERLAP_NON_NESTED" if intersection else "DISJOINT",
                "symmetric_difference_cycle": third,
            }
        )
    xor_all: set[str] = set()
    for cycle in cycles:
        xor_all ^= set(cycle["edge_ids"])
    return {
        "enumeration_rule": "connected edge subsets with degree two at every used vertex and E-V+1=1",
        "cycles": cycles,
        "overlap_relations": overlaps,
        "gf2_relation": {
            "equation": "left XOR right XOR outer = empty",
            "residual_edge_ids": sorted(xor_all),
            "passed": not xor_all,
        },
    }


def _vertex_signature(vertex: Mapping[str, Any], port_labeled: bool) -> tuple[Any, ...]:
    signature: tuple[Any, ...] = (
        vertex["role"],
        vertex["family"],
        vertex["total_valence"],
        vertex["background_valence"],
        vertex["quantum_valence"],
    )
    if port_labeled:
        signature += (
            tuple(port["momentum"] for port in vertex["background_ports"]),
            tuple(
                (injection["kind"], injection["momentum"])
                for injection in vertex["momentum_injections"]
            ),
        )
    return signature


def _automorphisms(
    vertices: Sequence[Mapping[str, Any]], edges: Sequence[Mapping[str, Any]], port_labeled: bool
) -> dict[str, Any]:
    vertex_ids = [vertex["vertex_id"] for vertex in vertices]
    signatures = {vertex["vertex_id"]: _vertex_signature(vertex, port_labeled) for vertex in vertices}
    undirected_edges = {frozenset((edge["source"], edge["target"])) for edge in edges}
    valid: list[dict[str, str]] = []
    for permuted_ids in permutations(vertex_ids):
        mapping = dict(zip(vertex_ids, permuted_ids))
        if any(signatures[vertex] != signatures[mapping[vertex]] for vertex in vertex_ids):
            continue
        mapped_edges = {
            frozenset((mapping[edge["source"]], mapping[edge["target"]])) for edge in edges
        }
        if mapped_edges == undirected_edges:
            valid.append({vertex: mapping[vertex] for vertex in vertex_ids})
    payload = {
        "preserves": (
            "typed vertices, topology, and labeled background/source momentum ports"
            if port_labeled
            else "typed vertices and topology; background momentum labels forgotten"
        ),
        "order": len(valid),
        "permutations": valid,
    }
    payload["automorphism_hash"] = digest(payload)
    return payload


def _orientation_record(edges: Sequence[Mapping[str, Any]], reflected: bool) -> dict[str, Any]:
    oriented_edges: list[dict[str, Any]] = []
    for edge in edges:
        source = edge["target"] if reflected else edge["source"]
        target = edge["source"] if reflected else edge["target"]
        momentum = scale(-1, edge["momentum_vector"]) if reflected else tuple(edge["momentum_vector"])
        oriented_edges.append(
            {
                "edge_id": edge["edge_id"],
                "source": source,
                "target": target,
                "momentum_vector": list(momentum),
                "momentum": render_linear(momentum),
            }
        )
    record = {
        "orientation_id": "reflected" if reflected else "direct",
        "edges": oriented_edges,
    }
    record["orientation_hash"] = digest(record)
    return record


def _downstream_fail_closed() -> dict[str, Any]:
    return {
        "amplitude_ir": {
            "status": "BLOCKED_ORDERED_PROJECT_VERTEX_PROPAGATOR_AND_WICK_DATA_ABSENT",
            "value": None,
        },
        "d_algebra_ir": {
            "status": "BLOCKED_AMPLITUDE_IR_ABSENT",
            "value": None,
        },
        "subtracted_integral_ir": {
            "status": "BLOCKED_DALGEBRA_AND_FOREST_COUNTERTERMS_ABSENT",
            "value": None,
        },
        "renormalized_coefficient": {
            "status": "BLOCKED_SUBTRACTED_INTEGRAL_IR_ABSENT",
            "value": None,
        },
    }


def _build_graph(
    *,
    graph_id: str,
    classification: str,
    topology: str,
    valence_family_id: str,
    insertion_m: int,
    action_multiplicities: Mapping[int, int],
    vertex_specs: Sequence[Mapping[str, Any]],
    edge_specs: Sequence[Mapping[str, Any]],
    cycle_labels: Mapping[frozenset[str], str],
    expected_automorphism_orders: tuple[int, int],
) -> dict[str, Any]:
    vertices: list[dict[str, Any]] = []
    for spec in vertex_specs:
        background_momenta = tuple(spec.get("background_momenta", ()))
        source_momentum = spec.get("source_momentum")
        background_ports = [
            {
                "port_id": f"{spec['vertex_id']}.b{slot}",
                "kind": "BACKGROUND_EXTERNAL",
                "momentum": momentum,
            }
            for slot, momentum in enumerate(background_momenta)
        ]
        injections = [
            {
                "kind": "BACKGROUND_EXTERNAL",
                "momentum": momentum,
                "momentum_vector": list(vec(**{momentum: 1})),
            }
            for momentum in background_momenta
        ]
        if source_momentum is not None:
            injections.append(
                {
                    "kind": "COMPOSITE_SOURCE_MOMENTUM",
                    "momentum": source_momentum,
                    "momentum_vector": list(vec(**{source_momentum: 1})),
                    "counts_toward_background_valence": False,
                }
            )
        vertex = {
            "vertex_id": spec["vertex_id"],
            "role": spec["role"],
            "family": spec["family"],
            "total_valence": int(spec["total_valence"]),
            "background_valence": len(background_ports),
            "quantum_valence": int(spec["total_valence"]) - len(background_ports),
            "background_ports": background_ports,
            "momentum_injections": injections,
        }
        if vertex["quantum_valence"] < 0:
            raise ValueError("background valence cannot exceed total valence")
        vertices.append(vertex)

    edges: list[dict[str, Any]] = []
    for spec in edge_specs:
        momentum = tuple(spec["momentum_vector"])
        edges.append(
            {
                "edge_id": spec["edge_id"],
                "source": spec["source"],
                "target": spec["target"],
                "endpoint_type": "QUANTUM_PORT_TO_QUANTUM_PORT",
                "momentum_vector": list(momentum),
                "momentum": render_linear(momentum),
                "propagator": None,
                "propagator_status": "BLOCKED_FIELD_AND_PROJECTOR_ASSIGNMENT_ABSENT",
            }
        )
    port_certificate = _assign_quantum_ports(vertices, edges)
    vertex_ids = [vertex["vertex_id"] for vertex in vertices]
    connected = _connected(vertex_ids, edges)
    V = len(vertices)
    I = len(edges)
    L = I - V + 1 if connected else None
    valence_lhs = (insertion_m - 2) + sum(
        (r - 2) * count for r, count in action_multiplicities.items()
    )
    total_valence = sum(vertex["total_valence"] for vertex in vertices)
    background_valence = sum(vertex["background_valence"] for vertex in vertices)
    quantum_valence = sum(vertex["quantum_valence"] for vertex in vertices)
    identity = {
        "connected": connected,
        "V": V,
        "I": I,
        "L": L,
        "loop_identity": {
            "lhs": L,
            "rhs": I - V + 1,
            "equation": f"{L}={I}-{V}+1",
            "passed": L == 2,
        },
        "valence_identity": {
            "lhs": valence_lhs,
            "rhs": 2 * L + N_EXTERNAL_BACKGROUND - 2,
            "required_value": 4,
            "equation": f"{valence_lhs}=2*{L}+{N_EXTERNAL_BACKGROUND}-2=4",
            "passed": valence_lhs == 2 * L + N_EXTERNAL_BACKGROUND - 2 == 4,
        },
        "total_half_edge_identity": {
            "lhs": total_valence,
            "rhs": 2 * I + N_EXTERNAL_BACKGROUND,
            "passed": total_valence == 2 * I + N_EXTERNAL_BACKGROUND,
        },
        "background_valence_identity": {
            "lhs": background_valence,
            "rhs": N_EXTERNAL_BACKGROUND,
            "passed": background_valence == N_EXTERNAL_BACKGROUND,
        },
        "quantum_valence_identity": {
            "lhs": quantum_valence,
            "rhs": 2 * I,
            "passed": quantum_valence == 2 * I,
        },
    }
    direct_orientation = _orientation_record(edges, reflected=False)
    reflected_orientation = _orientation_record(edges, reflected=True)
    incidence_direct = _incidence_and_routing(vertices, direct_orientation["edges"])
    incidence_reflected = _incidence_and_routing(vertices, reflected_orientation["edges"])
    automorphisms_typed = _automorphisms(vertices, edges, port_labeled=False)
    automorphisms_port_labeled = _automorphisms(vertices, edges, port_labeled=True)
    if (automorphisms_typed["order"], automorphisms_port_labeled["order"]) != expected_automorphism_orders:
        raise ValueError(
            f"unexpected automorphism orders for {graph_id}: "
            f"{automorphisms_typed['order']}, {automorphisms_port_labeled['order']}"
        )
    topology_payload = {
        "typed_vertices": [
            {
                key: vertex[key]
                for key in (
                    "vertex_id",
                    "role",
                    "family",
                    "total_valence",
                    "background_valence",
                    "quantum_valence",
                )
            }
            for vertex in vertices
        ],
        "undirected_edges": sorted(
            [sorted((edge["source"], edge["target"])) for edge in edges]
        ),
    }
    orientation_pair = {
        "semantics": "EDGE_DIRECTION_AND_MOMENTUM_SIGN_ONLY_NOT_A_WICK_OR_FIELD_ORIENTATION",
        "direct": direct_orientation,
        "reflected": reflected_orientation,
    }
    orientation_pair["orientation_pair_hash"] = digest(
        sorted(
            (
                direct_orientation["orientation_hash"],
                reflected_orientation["orientation_hash"],
            )
        )
    )
    graph = {
        "schema_version": SCHEMA_VERSION,
        "stage": STAGE,
        "graph_kind": "TOPOLOGY_GRAPHIR_NO_FIELD_OR_WICK_ASSIGNMENT",
        "sector": "EUCLIDEAN_N4_SYM_PURE_GAUGE",
        "operator_seed": "nabla_-[(nabla_+W_+)^A (nabla_+W_+)^B]",
        "graph_id": graph_id,
        "classification": classification,
        "topology": topology,
        "valence_family_id": valence_family_id,
        "momentum_contract": {
            "basis": list(MOMENTUM_BASIS),
            "loop_momenta": ["k", "l"],
            "composite_source_momentum": "P",
            "background_external_momenta": ["p1", "p2"],
            "all_incoming_relation": "P+p1+p2=0",
            "relation_vector": list(MOMENTUM_RELATION),
            "square_space": SQUARE_SPACE,
            "square_bilinear_form": "POSITIVE_EUCLIDEAN",
        },
        "vertices": vertices,
        "internal_edges": edges,
        "typed_port_saturation": port_certificate,
        "identities": identity,
        "incidence_routing": {
            "direct": incidence_direct,
            "reflected": incidence_reflected,
        },
        "denominator_ast": _denominator_ast(edges),
        "simple_one_loop_cycles": _simple_cycles(vertices, edges, cycle_labels),
        "automorphisms": {
            "typed_external_unlabeled": automorphisms_typed,
            "background_source_labeled": automorphisms_port_labeled,
        },
        "orientations": orientation_pair,
        "topology_hash": digest(topology_payload),
        "downstream_fail_closed": _downstream_fail_closed(),
    }
    graph_hash_payload = {key: value for key, value in graph.items() if key != "graph_hash"}
    graph["graph_hash"] = digest(graph_hash_payload)
    return graph


def build_direct_i3_s3_cubed() -> dict[str, Any]:
    return _build_graph(
        graph_id="G6_DIRECT_K4ME_I3_S3CUBED",
        classification="LITERAL_K4_MINUS_EDGE_DIRECT_PARENT",
        topology="K4_MINUS_ONE_EDGE",
        valence_family_id="I3__S3^3",
        insertion_m=3,
        action_multiplicities={3: 3},
        vertex_specs=(
            {"vertex_id": "I", "role": "COMPOSITE_INSERTION", "family": "I3", "total_valence": 3, "source_momentum": "P"},
            {"vertex_id": "A", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3, "background_momenta": ("p1",)},
            {"vertex_id": "B", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3, "background_momenta": ("p2",)},
            {"vertex_id": "C", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
        ),
        edge_specs=(
            {"edge_id": "e_CI", "source": "C", "target": "I", "momentum_vector": vec(k=1)},
            {"edge_id": "e_CA", "source": "C", "target": "A", "momentum_vector": vec(l=1)},
            {"edge_id": "e_AI", "source": "A", "target": "I", "momentum_vector": vec(l=1, p1=-1)},
            {"edge_id": "e_CB", "source": "C", "target": "B", "momentum_vector": vec(k=-1, l=-1)},
            {"edge_id": "e_BI", "source": "B", "target": "I", "momentum_vector": vec(k=-1, l=-1, p2=-1)},
        ),
        cycle_labels={
            frozenset(("e_CI", "e_CA", "e_AI")): "left",
            frozenset(("e_CI", "e_CB", "e_BI")): "right",
            frozenset(("e_CA", "e_AI", "e_CB", "e_BI")): "outer",
        },
        expected_automorphism_orders=(2, 1),
    )


def build_direct_i2_s3_squared_s4() -> dict[str, Any]:
    return _build_graph(
        graph_id="G6_DIRECT_K4ME_I2_S3SQ_S4",
        classification="LITERAL_K4_MINUS_EDGE_DIRECT_PARENT",
        topology="K4_MINUS_ONE_EDGE",
        valence_family_id="I2__S3^2__S4^1",
        insertion_m=2,
        action_multiplicities={3: 2, 4: 1},
        vertex_specs=(
            {"vertex_id": "I", "role": "COMPOSITE_INSERTION", "family": "I2", "total_valence": 2, "source_momentum": "P"},
            {"vertex_id": "A", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3, "background_momenta": ("p1",)},
            {"vertex_id": "B", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
            {"vertex_id": "C", "role": "ACTION_VERTEX", "family": "S4", "total_valence": 4, "background_momenta": ("p2",)},
        ),
        edge_specs=(
            {"edge_id": "e_BI", "source": "B", "target": "I", "momentum_vector": vec(k=1)},
            {"edge_id": "e_IC", "source": "I", "target": "C", "momentum_vector": vec(k=1, P=-1)},
            {"edge_id": "e_BA", "source": "B", "target": "A", "momentum_vector": vec(l=1)},
            {"edge_id": "e_AC", "source": "A", "target": "C", "momentum_vector": vec(l=1, p1=-1)},
            {"edge_id": "e_BC", "source": "B", "target": "C", "momentum_vector": vec(k=-1, l=-1)},
        ),
        cycle_labels={
            frozenset(("e_BI", "e_IC", "e_BC")): "left",
            frozenset(("e_BA", "e_AC", "e_BC")): "right",
            frozenset(("e_BI", "e_IC", "e_BA", "e_AC")): "outer",
        },
        expected_automorphism_orders=(1, 1),
    )


def build_direct_i2_s3_squared_s4_double_background_s4() -> dict[str, Any]:
    """Second decorated K4-minus-edge realization of I2 S3^2 S4.

    Both background legs are extracted from the ordered S4 vertex.  The I2 and
    S4 vertices therefore have quantum degree two and are the non-adjacent
    degree-two vertices of K4 minus one edge.  This realization is not obtained
    from the one-background-S3/one-background-S4 graph by a typed automorphism.
    """

    return _build_graph(
        graph_id="G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4",
        classification="LITERAL_K4_MINUS_EDGE_DIRECT_PARENT",
        topology="K4_MINUS_ONE_EDGE",
        valence_family_id="I2__S3^2__S4^1",
        insertion_m=2,
        action_multiplicities={3: 2, 4: 1},
        vertex_specs=(
            {"vertex_id": "I", "role": "COMPOSITE_INSERTION", "family": "I2", "total_valence": 2, "source_momentum": "P"},
            {"vertex_id": "A", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
            {"vertex_id": "B", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
            {"vertex_id": "C", "role": "ACTION_VERTEX", "family": "S4", "total_valence": 4, "background_momenta": ("p1", "p2")},
        ),
        edge_specs=(
            {"edge_id": "e_AI", "source": "A", "target": "I", "momentum_vector": vec(k=1)},
            {"edge_id": "e_IB", "source": "I", "target": "B", "momentum_vector": vec(k=1, P=-1)},
            {"edge_id": "e_CA", "source": "C", "target": "A", "momentum_vector": vec(l=1)},
            {"edge_id": "e_BC", "source": "B", "target": "C", "momentum_vector": vec(l=1, P=-1)},
            {"edge_id": "e_BA", "source": "B", "target": "A", "momentum_vector": vec(k=1, l=-1)},
        ),
        cycle_labels={
            frozenset(("e_AI", "e_IB", "e_BA")): "left",
            frozenset(("e_CA", "e_BC", "e_BA")): "right",
            frozenset(("e_AI", "e_IB", "e_CA", "e_BC")): "outer",
        },
        expected_automorphism_orders=(2, 2),
    )


def build_raw_marked_k23_theta_lift() -> dict[str, Any]:
    graph = _build_graph(
        graph_id="G6_RAW_MARKED_K23_THETA_I2_S3FOURTH",
        classification="RAW_MARKED_K2_3_THETA_LIFT_NOT_DIRECT_BITRIANGLE",
        topology="K2_3_COMPLETE_BIPARTITE_RAW_MARKED",
        valence_family_id="I2__S3^4",
        insertion_m=2,
        action_multiplicities={3: 4},
        vertex_specs=(
            {"vertex_id": "I", "role": "COMPOSITE_INSERTION", "family": "I2", "total_valence": 2, "source_momentum": "P"},
            {"vertex_id": "A", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3, "background_momenta": ("p1",)},
            {"vertex_id": "B", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3, "background_momenta": ("p2",)},
            {"vertex_id": "C", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
            {"vertex_id": "D", "role": "ACTION_VERTEX", "family": "S3", "total_valence": 3},
        ),
        edge_specs=(
            {"edge_id": "e_CI", "source": "C", "target": "I", "momentum_vector": vec(k=1)},
            {"edge_id": "e_ID", "source": "I", "target": "D", "momentum_vector": vec(k=1, P=-1)},
            {"edge_id": "e_CA", "source": "C", "target": "A", "momentum_vector": vec(l=1)},
            {"edge_id": "e_AD", "source": "A", "target": "D", "momentum_vector": vec(l=1, p1=-1)},
            {"edge_id": "e_CB", "source": "C", "target": "B", "momentum_vector": vec(k=-1, l=-1)},
            {"edge_id": "e_BD", "source": "B", "target": "D", "momentum_vector": vec(k=-1, l=-1, p2=-1)},
        ),
        cycle_labels={
            frozenset(("e_CI", "e_ID", "e_CA", "e_AD")): "left",
            frozenset(("e_CI", "e_ID", "e_CB", "e_BD")): "right",
            frozenset(("e_CA", "e_AD", "e_CB", "e_BD")): "outer",
        },
        expected_automorphism_orders=(4, 2),
    )
    graph["homeomorphic_suppression"] = {
        "status": "BLOCKED_NO_TYPED_DALGEBRA_PROPAGATOR_COLLAPSE_CERTIFICATE",
        "raw_graph_is_literal_k4_minus_edge": False,
        "raw_counts": {"V": 5, "I": 6, "L": 2},
        "literal_k4_minus_edge_counts": {"V": 4, "I": 5, "L": 2},
        "forbidden_inference": "DO_NOT_IDENTIFY_RAW_SIX_EDGE_GRAPH_WITH_FIVE_EDGE_BITRIANGLE",
    }
    graph_hash_payload = {key: value for key, value in graph.items() if key != "graph_hash"}
    graph["graph_hash"] = digest(graph_hash_payload)
    return graph


def build_bundle() -> dict[str, Any]:
    families = enumerate_valence_families()
    direct_graphs = [
        build_direct_i3_s3_cubed(),
        build_direct_i2_s3_squared_s4(),
        build_direct_i2_s3_squared_s4_double_background_s4(),
    ]
    raw_graph = build_raw_marked_k23_theta_lift()
    bundle = {
        "schema_version": SCHEMA_VERSION,
        "stage": STAGE,
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "scope": "PURE_GAUGE_TWO_LOOP_TWO_BACKGROUND_LEG_TOPOLOGY_ROUTING",
        "external_result_used_as_calculation_input": False,
        "exact_identities": {
            "loop": "L=I-V+1 for a connected graph",
            "two_loop_two_background_leg_valence": "(m-2)+sum_(r>=3)(r-2)n_r=4",
        },
        "valence_families": families,
        "literal_direct_graphs": direct_graphs,
        "raw_marked_theta_lift": raw_graph,
        "downstream_fail_closed": _downstream_fail_closed(),
    }
    bundle["bundle_hash"] = digest({key: value for key, value in bundle.items() if key != "bundle_hash"})
    return bundle


def build_audit(bundle: Mapping[str, Any], artifact_hashes: Mapping[str, str] | None = None) -> dict[str, Any]:
    families = bundle["valence_families"]
    direct = bundle["literal_direct_graphs"]
    raw = bundle["raw_marked_theta_lift"]
    graphs = [*direct, raw]
    raw_cycles = raw["simple_one_loop_cycles"]
    checks = [
        {"id": "VALENCE_FAMILY_COUNT_12", "passed": len(families) == 12, "evidence": len(families)},
        {
            "id": "VALENCE_FAMILIES_ARE_NOT_GRAPHS",
            "passed": all(family["classification"] == "VALENCE_NOT_GRAPH" and family["graph_ir"] is None for family in families),
            "evidence": [family["family_id"] for family in families],
        },
        {
            "id": "VALENCE_IDENTITIES_EQUAL_FOUR",
            "passed": all(family["identity"]["lhs"] == family["identity"]["rhs"] == 4 and family["identity"]["L"] == 2 for family in families),
            "evidence": [family["identity"] for family in families],
        },
        {"id": "LITERAL_K4_MINUS_EDGE_DECORATED_GRAPH_COUNT_3", "passed": len(direct) == 3 and all(graph["topology"] == "K4_MINUS_ONE_EDGE" for graph in direct) and {graph["valence_family_id"] for graph in direct} == {"I3__S3^3", "I2__S3^2__S4^1"}, "evidence": [graph["graph_id"] for graph in direct]},
        {"id": "RAW_K23_IS_SEPARATE", "passed": raw["topology"] == "K2_3_COMPLETE_BIPARTITE_RAW_MARKED" and not raw["homeomorphic_suppression"]["raw_graph_is_literal_k4_minus_edge"], "evidence": raw["graph_id"]},
        {"id": "ALL_GRAPHS_CONNECTED_TWO_LOOP", "passed": all(graph["identities"]["connected"] and graph["identities"]["L"] == 2 for graph in graphs), "evidence": [{"graph_id": graph["graph_id"], "V": graph["identities"]["V"], "I": graph["identities"]["I"], "L": graph["identities"]["L"]} for graph in graphs]},
        {"id": "ALL_TYPED_VALENCE_IDENTITIES_PASS", "passed": all(all(certificate["passed"] for certificate in graph["identities"].values() if isinstance(certificate, dict) and "passed" in certificate) for graph in graphs), "evidence": "total=background+quantum; sum_q=2I; sum_b=2"},
        {"id": "ALL_QUANTUM_PORTS_SATURATED", "passed": all(graph["typed_port_saturation"]["each_quantum_port_used_once"] for graph in graphs), "evidence": [graph["graph_id"] for graph in graphs]},
        {"id": "DIRECT_AND_REFLECTED_INCIDENCE_PASS", "passed": all(graph["incidence_routing"][orientation]["passed"] for graph in graphs for orientation in ("direct", "reflected")), "evidence": [graph["graph_id"] for graph in graphs]},
        {"id": "RAW_ROUTING_LITERAL", "passed": [edge["momentum"] for edge in raw["internal_edges"]] == ["k", "k-P", "l", "l-p1", "-k-l", "-k-l-p2"], "evidence": [edge["momentum"] for edge in raw["internal_edges"]]},
        {"id": "RAW_DENOMINATOR_LITERAL", "passed": raw["denominator_ast"]["rendered"] == "k^2 (k-P)^2 l^2 (l-p1)^2 (k+l)^2 (k+l+p2)^2", "evidence": raw["denominator_ast"]["rendered"]},
        {"id": "RAW_LEFT_RIGHT_OUTER_COMPLETE", "passed": [cycle["cycle_id"] for cycle in raw_cycles["cycles"]] == ["left", "right", "outer"], "evidence": raw_cycles["cycles"]},
        {"id": "RAW_CYCLES_PAIRWISE_OVERLAP_NON_NESTED", "passed": len(raw_cycles["overlap_relations"]) == 3 and all(relation["relation"] == "OVERLAP_NON_NESTED" and relation["intersection_edge_ids"] for relation in raw_cycles["overlap_relations"]), "evidence": raw_cycles["overlap_relations"]},
        {"id": "CYCLE_GF2_RELATION", "passed": all(graph["simple_one_loop_cycles"]["gf2_relation"]["passed"] for graph in graphs), "evidence": "left XOR right XOR outer = empty"},
        {"id": "AUTOMORPHISM_HASHES_PRESENT", "passed": all(graph["automorphisms"][kind]["automorphism_hash"] for graph in graphs for kind in ("typed_external_unlabeled", "background_source_labeled")), "evidence": [{"graph_id": graph["graph_id"], "orders": [graph["automorphisms"]["typed_external_unlabeled"]["order"], graph["automorphisms"]["background_source_labeled"]["order"]]} for graph in graphs]},
        {"id": "ORIENTATION_HASHES_DISTINCT", "passed": all(graph["orientations"]["direct"]["orientation_hash"] != graph["orientations"]["reflected"]["orientation_hash"] for graph in graphs), "evidence": [graph["orientations"]["orientation_pair_hash"] for graph in graphs]},
        {"id": "GRAPH_HASHES_UNIQUE", "passed": len({graph["graph_hash"] for graph in graphs}) == len(graphs), "evidence": [graph["graph_hash"] for graph in graphs]},
        {"id": "AMPLITUDE_DALGEBRA_COEFFICIENT_FAIL_CLOSED", "passed": all(stage["value"] is None and stage["status"].startswith("BLOCKED_") for graph in graphs for stage in graph["downstream_fail_closed"].values()) and all(stage["value"] is None and stage["status"].startswith("BLOCKED_") for stage in bundle["downstream_fail_closed"].values()), "evidence": bundle["downstream_fail_closed"]},
    ]
    passed = all(check["passed"] for check in checks)
    return {
        "schema_version": "step6.two_loop_graphir.audit.v1",
        "status": "PASS" if passed else "FAIL",
        "checks": checks,
        "artifact_sha256": dict(artifact_hashes or {}),
        "failure_count": sum(not check["passed"] for check in checks),
    }


def render_summary(bundle: Mapping[str, Any]) -> str:
    raw = bundle["raw_marked_theta_lift"]
    lines = [
        "# Step 6 pure-gauge two-loop GraphIR: topology and routing only",
        "",
        "$$",
        "L=I-V+1=2,\\qquad (m-2)+\\sum_{r\\ge 3}(r-2)n_r=4.",
        "$$",
        "",
        f"- valence solutions: `{len(bundle['valence_families'])}`; every item is `VALENCE_NOT_GRAPH`.",
        f"- literal K4-minus-edge direct parents: `{len(bundle['literal_direct_graphs'])}`.",
        "- raw marked K2,3 theta lift: one separate six-edge GraphIR.",
        "- amplitude, D-algebra, subtraction, coefficient: `BLOCKED`.",
        "",
        "## Literal direct parents",
        "",
    ]
    for graph in bundle["literal_direct_graphs"]:
        lines.extend(
            [
                f"### {graph['graph_id']}",
                "",
                "$$",
                f"D={graph['denominator_ast']['rendered']}.",
                "$$",
                "",
                "$$",
                f"V={graph['identities']['V']},\\quad I={graph['identities']['I']},\\quad L={graph['identities']['L']}.",
                "$$",
                "",
            ]
        )
    lines.extend(
        [
            "## Raw marked theta lift",
            "",
            "$$",
            "(r_{CI},r_{ID},r_{CA},r_{AD},r_{CB},r_{BD})",
            "=(k,k-P,l,l-p_1,-k-l,-k-l-p_2).",
            "$$",
            "",
            "$$",
            f"D={raw['denominator_ast']['rendered']}.",
            "$$",
            "",
            "$$",
            "\\gamma_L=\\{CI,ID,CA,AD\\},\\quad",
            "\\gamma_R=\\{CI,ID,CB,BD\\},\\quad",
            "\\gamma_O=\\{CA,AD,CB,BD\\}.",
            "$$",
            "",
            "`RAW_MARKED_K2_3_THETA_LIFT_NOT_DIRECT_BITRIANGLE`; no collapse certificate is asserted.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(root: Path) -> dict[str, Any]:
    bundle = build_bundle()
    generated = root / "generated" / "step6" / "two-loop-graphir"
    generated.mkdir(parents=True, exist_ok=True)
    outputs = {
        "two-loop-graphir.json": bundle,
        "valence-families.json": {
            "schema_version": SCHEMA_VERSION,
            "families": bundle["valence_families"],
        },
        "direct-k4-minus-edge.json": {
            "schema_version": SCHEMA_VERSION,
            "graphs": bundle["literal_direct_graphs"],
        },
        "raw-k23-theta-lift.json": bundle["raw_marked_theta_lift"],
    }
    artifact_hashes: dict[str, str] = {}
    for filename, payload in outputs.items():
        path = generated / filename
        text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        path.write_text(text, encoding="utf-8")
        artifact_hashes[str(path.relative_to(root))] = sha256(text.encode("utf-8")).hexdigest()
    summary_path = generated / "two-loop-graphir.md"
    summary = render_summary(bundle)
    summary_path.write_text(summary, encoding="utf-8")
    artifact_hashes[str(summary_path.relative_to(root))] = sha256(summary.encode("utf-8")).hexdigest()
    audit = build_audit(bundle, artifact_hashes)
    if audit["status"] != "PASS":
        failed = [check["id"] for check in audit["checks"] if not check["passed"]]
        raise RuntimeError(f"Step-6 topology audit failed: {failed}")
    audit_path = root / "audits" / "step6-two-loop-graphir-verification.json"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return {"bundle": bundle, "audit": audit}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    result = write_outputs(root)
    print(
        json.dumps(
            {
                "status": result["audit"]["status"],
                "valence_family_count": len(result["bundle"]["valence_families"]),
                "literal_direct_graph_count": len(result["bundle"]["literal_direct_graphs"]),
                "raw_marked_graph_count": 1,
                "failure_count": result["audit"]["failure_count"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
