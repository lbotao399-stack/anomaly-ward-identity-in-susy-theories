#!/usr/bin/env python3
"""Proposal-only Step-6 forest, DRED, and subtraction architecture.

The input graphs are produced by :mod:`scripts.step6_two_loop_graphir`.
This layer proves only graph-theoretic statements and exact symbolic algebra.
It cannot activate a superficially divergent subgraph without an explicit
``NumeratorScalingCertificate`` and never claims a UV pole or coefficient.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts.step6_two_loop_graphir import build_bundle as build_graph_bundle
except ModuleNotFoundError:  # direct ``python scripts/...`` execution
    from step6_two_loop_graphir import build_bundle as build_graph_bundle


SCHEMA_VERSION = "step6.two_loop_forest.v1"
STAGE = "PROPOSAL_ONLY_TOPOLOGY_FOREST_DRED_ARCHITECTURE"
DIMENSION = "d=4-2*epsilon"
PER_LOOP_MEASURE = "mu^(2*epsilon) d^d q/(2*pi)^d"
TWO_LOOP_MEASURE = (
    "mu^(4*epsilon) d^d k/(2*pi)^d d^d l/(2*pi)^d"
)
UV_PROJECTOR = "K_UV"
SUPERSYMMETRY_PROJECTOR = "K_+=-(1/8)D_+ barD^2 D_+"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class NumeratorScalingCertificate:
    """Homogeneous loop-momentum degrees in subgraph-adapted loop bases."""

    graph_hash: str
    rho_by_subgraph: Mapping[str, int | None]
    source_status: str = "UNKNOWN_NUMERATOR_DEMONSTRATION_ONLY"
    adapted_basis_status: str = "BLOCKED_COMPILED_DALGEBRA_NUMERATOR_ABSENT"

    def __post_init__(self) -> None:
        if not self.graph_hash:
            raise ValueError("a numerator-scaling certificate requires the source graph hash")
        for subgraph_id, rho in self.rho_by_subgraph.items():
            if not subgraph_id:
                raise ValueError("subgraph ids cannot be empty")
            if rho is not None and (not isinstance(rho, int) or isinstance(rho, bool) or rho < 0):
                raise ValueError("rho must be a nonnegative integer or UNKNOWN")

    def rho(self, subgraph_id: str) -> int | None:
        return self.rho_by_subgraph.get(subgraph_id)

    def canonical_dict(self) -> dict[str, Any]:
        payload = {
            "schema_version": "step6.numerator_scaling_certificate.v1",
            "graph_hash": self.graph_hash,
            "rho_definition": (
                "highest homogeneous degree under scaling of an adapted subgraph loop basis "
                "with complementary loop and physical external momenta held fixed"
            ),
            "rho_by_subgraph": {
                key: value if value is not None else "UNKNOWN"
                for key, value in sorted(self.rho_by_subgraph.items())
            },
            "source_status": self.source_status,
            "adapted_basis_status": self.adapted_basis_status,
            "forbidden_inference": (
                "DO_NOT_INFER_RHO_FROM_EDGE_COUNT_FREE_INDEX_COUNT_OR_UNCOMPILED_DALGEBRA"
            ),
        }
        payload["certificate_hash"] = digest(payload)
        return payload


def _edge_vertices(edge: Mapping[str, Any]) -> tuple[str, str]:
    return str(edge["source"]), str(edge["target"])


def _used_vertices(edges: Sequence[Mapping[str, Any]]) -> set[str]:
    return {vertex for edge in edges for vertex in _edge_vertices(edge)}


def _connected_on_vertices(vertices: set[str], edges: Sequence[Mapping[str, Any]]) -> bool:
    if not vertices:
        return False
    if len(vertices) == 1:
        return True
    adjacency = {vertex: set() for vertex in vertices}
    for edge in edges:
        source, target = _edge_vertices(edge)
        if source == target:
            continue
        adjacency[source].add(target)
        adjacency[target].add(source)
    reached = {next(iter(vertices))}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - reached:
            reached.add(neighbor)
            frontier.append(neighbor)
    return reached == vertices


def _one_particle_irreducible(edges: Sequence[Mapping[str, Any]]) -> bool:
    vertices = _used_vertices(edges)
    loops = len(edges) - len(vertices) + 1
    if loops <= 0 or not _connected_on_vertices(vertices, edges):
        return False
    for removed in range(len(edges)):
        retained = [edge for index, edge in enumerate(edges) if index != removed]
        if not _connected_on_vertices(vertices, retained):
            return False
    return True


def _named_cycle_map(graph: Mapping[str, Any]) -> dict[frozenset[str], str]:
    return {
        frozenset(str(edge_id) for edge_id in cycle["edge_ids"]): str(cycle["cycle_id"])
        for cycle in graph["simple_one_loop_cycles"]["cycles"]
    }


def enumerate_connected_edge_subgraphs(graph: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Enumerate every connected nonempty edge subset, with exact 1PI status."""

    edges = list(graph["internal_edges"])
    full_edge_set = frozenset(str(edge["edge_id"]) for edge in edges)
    named_cycles = _named_cycle_map(graph)
    records: list[dict[str, Any]] = []
    for size in range(1, len(edges) + 1):
        for subset_indices in combinations(range(len(edges)), size):
            subset = [edges[index] for index in subset_indices]
            vertices = _used_vertices(subset)
            if not _connected_on_vertices(vertices, subset):
                continue
            edge_ids = frozenset(str(edge["edge_id"]) for edge in subset)
            loops = len(subset) - len(vertices) + 1
            one_pi = _one_particle_irreducible(subset)
            is_full = edge_ids == full_edge_set
            named_cycle = named_cycles.get(edge_ids)
            if is_full:
                subgraph_id = "full"
                role = "FULL_GRAPH"
            elif named_cycle is not None:
                subgraph_id = named_cycle
                role = "NAMED_ONE_LOOP_CYCLE"
            else:
                subgraph_id = f"H_{digest(sorted(edge_ids))[:16]}"
                role = "PROPER_1PI" if one_pi else "CONNECTED_NON_1PI"
            if loops == 0:
                topology_status = "TREE_NO_LOOP_INTEGRATION"
            elif one_pi:
                topology_status = "ONE_PARTICLE_IRREDUCIBLE"
            else:
                topology_status = "CONTAINS_BRIDGE_NOT_RENORMALIZATION_PART"
            record = {
                "subgraph_id": subgraph_id,
                "role": role,
                "edge_ids": sorted(edge_ids),
                "vertex_ids": sorted(vertices),
                "counts": {"L": loops, "I": len(subset), "V": len(vertices)},
                "connected": True,
                "one_particle_irreducible": one_pi,
                "proper": not is_full,
                "topology_status": topology_status,
                "superficial_degree_formula": f"omega4=4*{loops}-2*{len(subset)}+rho",
            }
            record["subgraph_hash"] = digest(record)
            records.append(record)
    records.sort(
        key=lambda record: (
            record["counts"]["I"],
            record["counts"]["V"],
            record["edge_ids"],
        )
    )
    return records


def connected_census(records: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[tuple[int, int, int, bool], int] = {}
    for record in records:
        counts = record["counts"]
        key = (
            int(counts["L"]),
            int(counts["I"]),
            int(counts["V"]),
            bool(record["one_particle_irreducible"]),
        )
        buckets[key] = buckets.get(key, 0) + 1
    return [
        {
            "count": count,
            "L": key[0],
            "I": key[1],
            "V": key[2],
            "one_particle_irreducible": key[3],
            "omega4_formula": f"rho+{4 * key[0] - 2 * key[1]}",
        }
        for key, count in sorted(buckets.items())
    ]


def _relevant_1pi(records: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [
        record
        for record in records
        if record["one_particle_irreducible"] and int(record["counts"]["L"]) > 0
    ]


def unknown_scaling_certificate(
    graph: Mapping[str, Any], records: Sequence[Mapping[str, Any]]
) -> NumeratorScalingCertificate:
    return NumeratorScalingCertificate(
        graph_hash=str(graph["graph_hash"]),
        rho_by_subgraph={record["subgraph_id"]: None for record in _relevant_1pi(records)},
    )


def power_counting_analysis(
    graph: Mapping[str, Any],
    records: Sequence[Mapping[str, Any]],
    certificate: NumeratorScalingCertificate,
) -> dict[str, Any]:
    if certificate.graph_hash != graph["graph_hash"]:
        raise ValueError("numerator certificate graph hash does not match GraphIR")
    entries: list[dict[str, Any]] = []
    for record in _relevant_1pi(records):
        rho = certificate.rho(str(record["subgraph_id"]))
        counts = record["counts"]
        omega_constant = 4 * int(counts["L"]) - 2 * int(counts["I"])
        omega4 = None if rho is None else omega_constant + rho
        candidate = None if omega4 is None else omega4 >= 0
        if rho is None:
            status = "BLOCKED_NUMERATOR_SCALING_CERTIFICATE_RHO_UNKNOWN"
            pole_status = "BLOCKED_POWER_COUNTING_AND_KUV_EVALUATION"
        elif candidate:
            status = "SUPERFICIALLY_DIVERGENT_CANDIDATE_FROM_CERTIFIED_RHO"
            pole_status = "BLOCKED_NONZERO_KUV_NOT_EVALUATED"
        else:
            status = "PROVED_POWER_COUNTING_CONVERGENT_FROM_CERTIFIED_RHO"
            pole_status = "NO_UV_COUNTERTERM_BY_POWER_COUNTING"
        entries.append(
            {
                "subgraph_id": record["subgraph_id"],
                "subgraph_hash": record["subgraph_hash"],
                "proper": record["proper"],
                "counts": counts,
                "rho": rho if rho is not None else "UNKNOWN",
                "omega4": omega4 if omega4 is not None else "UNKNOWN",
                "superficially_divergent_candidate": candidate,
                "power_counting_status": status,
                "actual_uv_pole": None,
                "actual_uv_pole_status": pole_status,
            }
        )
    unknown = [entry["subgraph_id"] for entry in entries if entry["rho"] == "UNKNOWN"]
    return {
        "definition": "omega4=4*L-2*I+rho",
        "certificate": certificate.canonical_dict(),
        "entries": entries,
        "status": (
            "BLOCKED_RHO_UNKNOWN_FAIL_CLOSED"
            if unknown
            else "POWER_COUNTING_CERTIFIED_KUV_STILL_UNEVALUATED"
        ),
        "unknown_subgraph_ids": unknown,
        "no_pole_or_coefficient_claim": True,
    }


def subgraphs_compatible(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    left_edges = set(left["edge_ids"])
    right_edges = set(right["edge_ids"])
    return (
        left_edges.isdisjoint(right_edges)
        or left_edges <= right_edges
        or right_edges <= left_edges
    )


def _forest_records(subgraphs: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    forests: list[dict[str, Any]] = []
    for size in range(0, len(subgraphs) + 1):
        for forest in combinations(subgraphs, size):
            if not all(subgraphs_compatible(left, right) for left, right in combinations(forest, 2)):
                continue
            ids = [str(subgraph["subgraph_id"]) for subgraph in forest]
            records = {
                "subgraph_ids": ids,
                "cardinality": len(ids),
                "compatible_disjoint_or_nested": True,
            }
            records["forest_hash"] = digest(records)
            forests.append(records)
    forests.sort(key=lambda forest: (forest["cardinality"], forest["subgraph_ids"]))
    return forests


def forest_analysis(
    records: Sequence[Mapping[str, Any]], power_counting: Mapping[str, Any]
) -> dict[str, Any]:
    proper_1pi = [
        record
        for record in records
        if record["proper"]
        and record["one_particle_irreducible"]
        and int(record["counts"]["L"]) > 0
    ]
    structural_forests = _forest_records(proper_1pi)
    compatibility: list[dict[str, Any]] = []
    for left, right in combinations(proper_1pi, 2):
        left_edges = set(left["edge_ids"])
        right_edges = set(right["edge_ids"])
        compatibility.append(
            {
                "pair": [left["subgraph_id"], right["subgraph_id"]],
                "intersection_edge_ids": sorted(left_edges & right_edges),
                "left_subset_right": left_edges < right_edges,
                "right_subset_left": right_edges < left_edges,
                "edge_disjoint": left_edges.isdisjoint(right_edges),
                "compatible": subgraphs_compatible(left, right),
                "relation": (
                    "COMPATIBLE_DISJOINT_OR_NESTED"
                    if subgraphs_compatible(left, right)
                    else "OVERLAP_NON_NESTED"
                ),
            }
        )
    entry_map = {entry["subgraph_id"]: entry for entry in power_counting["entries"]}
    proper_entries = [entry_map[str(record["subgraph_id"])] for record in proper_1pi]
    if any(entry["superficially_divergent_candidate"] is None for entry in proper_entries):
        active_forests: list[dict[str, Any]] | None = None
        active_status = "BLOCKED_RHO_UNKNOWN"
    else:
        candidates = [
            record
            for record in proper_1pi
            if entry_map[str(record["subgraph_id"])]["superficially_divergent_candidate"]
        ]
        active_forests = _forest_records(candidates)
        active_status = "POWER_COUNTING_FORESTS_CERTIFIED_KUV_STILL_UNEVALUATED"
    return {
        "compatibility_rule": "edge-disjoint or one edge-set contained in the other",
        "proper_1pi_subgraph_ids": [record["subgraph_id"] for record in proper_1pi],
        "pair_relations": compatibility,
        "structurally_compatible_forests": structural_forests,
        "power_counting_forests": active_forests,
        "power_counting_forests_status": active_status,
        "current_graph_maximum_structural_forest_cardinality": max(
            forest["cardinality"] for forest in structural_forests
        ),
    }


def contract_subgraph(
    graph: Mapping[str, Any], subgraph: Mapping[str, Any]
) -> dict[str, Any]:
    contracted_edge_ids = set(subgraph["edge_ids"])
    contracted_vertices = set(subgraph["vertex_ids"])
    contracted_vertex = f"C_{subgraph['subgraph_id']}"
    remaining_edges: list[dict[str, Any]] = []
    for edge in graph["internal_edges"]:
        if edge["edge_id"] in contracted_edge_ids:
            continue
        source = contracted_vertex if edge["source"] in contracted_vertices else edge["source"]
        target = contracted_vertex if edge["target"] in contracted_vertices else edge["target"]
        remaining_edges.append(
            {
                "edge_id": edge["edge_id"],
                "source": source,
                "target": target,
                "self_loop": source == target,
            }
        )
    original_vertices = {vertex["vertex_id"] for vertex in graph["vertices"]}
    remaining_vertices = (original_vertices - contracted_vertices) | {contracted_vertex}
    connected = _connected_on_vertices(
        set(remaining_vertices),
        [
            {"source": edge["source"], "target": edge["target"]}
            for edge in remaining_edges
        ],
    )
    loops = len(remaining_edges) - len(remaining_vertices) + 1
    if len(remaining_vertices) == 1 and len(remaining_edges) == 1 and remaining_edges[0]["self_loop"]:
        reduced_topology = "ONE_EDGE_SELF_LOOP_TADPOLE"
    elif len(remaining_vertices) == 2 and len(remaining_edges) == 2:
        reduced_topology = "TWO_EDGE_ONE_LOOP_BUBBLE"
    else:
        reduced_topology = "GENERIC_CONTRACTED_COGRAPH"
    payload = {
        "subgraph_id": subgraph["subgraph_id"],
        "subgraph_hash": subgraph["subgraph_hash"],
        "contracted_vertex": contracted_vertex,
        "counts": {"L": loops, "I": len(remaining_edges), "V": len(remaining_vertices)},
        "count_identity": {
            "L_G_minus_L_gamma": int(graph["identities"]["L"])
            - int(subgraph["counts"]["L"]),
            "I_G_minus_I_gamma": len(graph["internal_edges"])
            - int(subgraph["counts"]["I"]),
            "V_G_minus_V_gamma_plus_one": len(graph["vertices"])
            - int(subgraph["counts"]["V"])
            + 1,
        },
        "connected": connected,
        "remaining_edges": remaining_edges,
        "reduced_topology": reduced_topology,
        "topology_status": "CERTIFIED_FROM_EDGE_CONTRACTION",
        "typed_counterterm_port_status": (
            "BLOCKED_LOCAL_COUNTERTERM_OPERATOR_AND_TYPED_PORT_SIGNATURE_ABSENT"
        ),
        "scaleless_status": "NOT_EVALUATED_REQUIRES_CONTRACTED_NUMERATOR_AND_EXTERNAL_INJECTION",
    }
    payload["contraction_hash"] = digest(payload)
    return payload


def contraction_analysis(
    graph: Mapping[str, Any], records: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    named_cycles = [
        record for record in records if record["role"] == "NAMED_ONE_LOOP_CYCLE"
    ]
    named_cycles.sort(key=lambda record: ("left", "right", "outer").index(record["subgraph_id"]))
    return {
        "rule": "contract selected subgraph edges and identify all selected vertices",
        "cographs": [contract_subgraph(graph, record) for record in named_cycles],
        "typed_status": "BLOCKED_COUNTERTERM_OPERATOR_TYPES_NOT_COMPILED",
    }


def renormalization_ast(
    graph: Mapping[str, Any],
    records: Sequence[Mapping[str, Any]],
    power_counting: Mapping[str, Any],
    forests: Mapping[str, Any],
) -> dict[str, Any]:
    entries = {
        entry["subgraph_id"]: entry
        for entry in power_counting["entries"]
        if entry["proper"]
    }
    contractions = {
        cograph["subgraph_id"]: cograph
        for cograph in contraction_analysis(graph, records)["cographs"]
    }
    terms: list[dict[str, Any]] = [
        {
            "op": "GRAPH_AMPLITUDE",
            "graph_id": graph["graph_id"],
            "symbol": f"Phi({graph['graph_id']})",
        }
    ]
    for subgraph_id in ("left", "right", "outer"):
        entry = entries[subgraph_id]
        if entry["superficially_divergent_candidate"] is None:
            activation = "BLOCKED_RHO_UNKNOWN"
        elif entry["superficially_divergent_candidate"]:
            activation = "ACTIVE_SUPERFICIALLY_DIVERGENT_KUV_NOT_EVALUATED"
        else:
            activation = "INACTIVE_POWER_COUNTING_CONVERGENT"
        terms.append(
            {
                "op": "COUNTERTERM_STAR_COGRAPH",
                "sign": -1,
                "subgraph_id": subgraph_id,
                "counterterm": {
                    "op": "UV_POLE_PROJECTOR",
                    "projector": UV_PROJECTOR,
                    "argument": f"Phi({subgraph_id})",
                    "primitive_one_loop_subgraph": True,
                },
                "cograph": {
                    "op": "CONTRACTED_GRAPH_AMPLITUDE",
                    "symbol": f"Phi({graph['graph_id']}/{subgraph_id})",
                    "counts": contractions[subgraph_id]["counts"],
                    "typed_status": contractions[subgraph_id]["typed_counterterm_port_status"],
                },
                "activation_status": activation,
            }
        )
    rprime = {
        "op": "SUM",
        "name": "Rprime",
        "forest_formula": (
            "Rprime Phi(G)=sum_(proper compatible forests F) "
            "[product_(gamma in F) C(gamma)] star Phi(G/F)"
        ),
        "terms": terms,
        "forest_status": forests["power_counting_forests_status"],
    }
    overall_counterterm = {
        "op": "NEGATIVE_UV_POLE_PROJECTOR",
        "name": "C(G)",
        "projector": UV_PROJECTOR,
        "argument": rprime,
        "formula": "C(G)=-K_UV Rprime Phi(G)",
    }
    renormalized = {
        "op": "ONE_MINUS_UV_POLE_PROJECTOR",
        "name": "R",
        "projector": UV_PROJECTOR,
        "argument": rprime,
        "formula": "R Phi(G)=(1-K_UV) Rprime Phi(G)",
    }
    return {
        "scheme": "DRED_MINIMAL_POLE_SUBTRACTION_FOREST_COMBINATORICS",
        "uv_projector": {
            "symbol": UV_PROJECTOR,
            "definition": "K_UV[sum_n a_n epsilon^n]=sum_(n<0) a_n epsilon^n",
            "distinct_from_superspace_projector": True,
            "superspace_projector": SUPERSYMMETRY_PROJECTOR,
        },
        "rprime": rprime,
        "overall_counterterm": overall_counterterm,
        "renormalized": renormalized,
        "status": (
            "BLOCKED_NUMERATOR_SCALING_CERTIFICATE"
            if power_counting["unknown_subgraph_ids"]
            else "SYMBOLIC_POWER_COUNTING_FOREST_KUV_UNEVALUATED"
        ),
        "uv_pole": None,
        "renormalized_coefficient": None,
    }


def rank2_coefficient(d: Fraction) -> Fraction:
    if d == 0:
        raise ZeroDivisionError("rank-two reduction is undefined at d=0")
    return Fraction(1, 1) / d


def rank4_coefficients(
    d: Fraction, X: Fraction, Y: Fraction, Z: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    denominator = d * (d - 1) * (d + 2)
    if denominator == 0:
        raise ZeroDivisionError("rank-four reduction requires d not in {0,1,-2}")
    return (
        ((d + 1) * X - Y - Z) / denominator,
        ((d + 1) * Y - X - Z) / denominator,
        ((d + 1) * Z - X - Y) / denominator,
    )


def dred_architecture() -> dict[str, Any]:
    return {
        "dimension": DIMENSION,
        "measure": {
            "per_independent_loop": PER_LOOP_MEASURE,
            "two_loop": TWO_LOOP_MEASURE,
            "mu_power": "mu^(4*epsilon)",
            "stripped_vertex_convention": True,
        },
        "metric_types": {
            "spin_dalgebra_metric": "delta_(4)",
            "loop_tensor_metric": "hat_delta",
            "evanescent_metric": "tilde_delta=delta_(4)-hat_delta",
            "identities": [
                "delta_(4)=hat_delta+tilde_delta",
                "hat_delta^2=hat_delta",
                "tilde_delta^2=tilde_delta",
                "hat_delta*tilde_delta=0",
                "tr(delta_(4))=4",
                "tr(hat_delta)=d=4-2*epsilon",
                "tr(tilde_delta)=2*epsilon",
                "tilde_delta^m_n v^n=0 for every routed momentum v",
            ],
            "bare_numerator_epsilon_status": "FORBIDDEN",
        },
        "centered_tensor_reduction": {
            "precondition": (
                "Feynman-parameterize, complete the two-loop quadratic form, and expand "
                "the numerator in centered hat-space loop vectors q_i"
            ),
            "rank_odd": "I[q_(i1)^m1 ... q_(i_(2s+1))^m_(2s+1) F]=0",
            "rank_two": {
                "formula": (
                    "I[q_i^m q_j^n F]=(hat_delta^(mn)/d) I[(q_i.q_j)F]"
                ),
                "coefficient": {"numerator": "1", "denominator": "d"},
            },
            "rank_four": {
                "basis": [
                    "hat_delta^(mn)hat_delta^(rs)",
                    "hat_delta^(mr)hat_delta^(ns)",
                    "hat_delta^(ms)hat_delta^(nr)",
                ],
                "denominator": "d*(d-1)*(d+2)",
                "A": {"X": "d+1", "Y": "-1", "Z": "-1"},
                "B": {"X": "-1", "Y": "d+1", "Z": "-1"},
                "C": {"X": "-1", "Y": "-1", "Z": "d+1"},
                "contractions": {
                    "X": "I[(q_i.q_j)(q_k.q_l)F]",
                    "Y": "I[(q_i.q_k)(q_j.q_l)F]",
                    "Z": "I[(q_i.q_l)(q_j.q_k)F]",
                },
                "identical_vector_specialization": (
                    "I[q^m q^n q^r q^s F]=(hat_delta^(mn)hat_delta^(rs)+"
                    "hat_delta^(mr)hat_delta^(ns)+hat_delta^(ms)hat_delta^(nr))"
                    "/(d*(d+2))*I[(q^2)^2 F]"
                ),
            },
            "keep_d_exact_through_laurent_multiplication": True,
        },
        "evanescent_laurent_rule": {
            "inputs": (
                "A(epsilon)=sum_(m=-P)^infinity a_m epsilon^m; "
                "E(epsilon)=sum_(n=s)^infinity e_n epsilon^n with s>=1"
            ),
            "finite": "[A E]_(epsilon^0)=sum_(n=s)^P a_(-n)e_n",
            "through_pole_order_two": "a_(-1)e_1+a_(-2)e_2",
            "renormalized_gate": (
                "all epsilon^(-2) and epsilon^(-1) terms must vanish in the R-complete family"
            ),
            "free_tilde_metric_warning": (
                "tilde_delta^(mn) is not 2*epsilon; only tr(tilde_delta)=2*epsilon"
            ),
        },
        "pole_order": "UNKNOWN",
        "finite_remainder": None,
    }


def evanescent_finite_remainder(
    a_minus_n: Mapping[int, Fraction],
    e_n: Mapping[int, Fraction],
    pole_order: int = 2,
) -> Fraction:
    if pole_order < 0 or pole_order > 2:
        raise ValueError("this Step-6 layer is restricted to pole order at most two")
    return sum(
        (a_minus_n.get(n, Fraction(0)) * e_n.get(n, Fraction(0)) for n in range(1, pole_order + 1)),
        Fraction(0),
    )


def build_graph_forest_record(
    graph: Mapping[str, Any],
    certificate: NumeratorScalingCertificate | None = None,
) -> dict[str, Any]:
    records = enumerate_connected_edge_subgraphs(graph)
    certificate = certificate or unknown_scaling_certificate(graph, records)
    power_counting = power_counting_analysis(graph, records, certificate)
    forests = forest_analysis(records, power_counting)
    contractions = contraction_analysis(graph, records)
    renormalization = renormalization_ast(graph, records, power_counting, forests)
    record = {
        "schema_version": SCHEMA_VERSION,
        "stage": STAGE,
        "source_graph_id": graph["graph_id"],
        "source_graph_hash": graph["graph_hash"],
        "source_graph_classification": graph["classification"],
        "connected_edge_subgraphs": records,
        "connected_census": connected_census(records),
        "power_counting": power_counting,
        "forests": forests,
        "contractions": contractions,
        "renormalization_ast": renormalization,
        "no_numerator_pole_or_coefficient_claim": True,
    }
    record["record_hash"] = digest(record)
    return record


def build_forest_bundle() -> dict[str, Any]:
    graph_bundle = build_graph_bundle()
    graphs = [
        *graph_bundle["literal_direct_graphs"],
        graph_bundle["raw_marked_theta_lift"],
    ]
    records = [build_graph_forest_record(graph) for graph in graphs]
    bundle = {
        "schema_version": SCHEMA_VERSION,
        "stage": STAGE,
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "source_graph_bundle_hash": graph_bundle["bundle_hash"],
        "numerator_certificate_mode": "DEMONSTRATION_RHO_UNKNOWN_ONLY",
        "graph_records": records,
        "dred_architecture": dred_architecture(),
        "global_fail_closed": {
            "compiled_numerator": None,
            "divergent_subgraph_set": None,
            "uv_poles": None,
            "renormalized_coefficient": None,
            "status": "BLOCKED_COMPILED_DALGEBRA_NUMERATOR_AND_KUV_EVALUATION",
        },
    }
    bundle["bundle_hash"] = digest({key: value for key, value in bundle.items() if key != "bundle_hash"})
    return bundle


def build_audit(
    bundle: Mapping[str, Any], artifact_hashes: Mapping[str, str] | None = None
) -> dict[str, Any]:
    records = list(bundle["graph_records"])
    direct = [
        record
        for record in records
        if record["source_graph_classification"] == "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT"
    ]
    raw = next(
        record
        for record in records
        if record["source_graph_classification"]
        == "RAW_MARKED_K2_3_THETA_LIFT_NOT_DIRECT_BITRIANGLE"
    )
    checks = [
        {
            "id": "FOUR_SOURCE_GRAPH_RECORDS",
            "passed": len(records) == 4 and len(direct) == 3,
            "evidence": [record["source_graph_id"] for record in records],
        },
        {
            "id": "LITERAL_CONNECTED_CENSUS_29",
            "passed": all(len(record["connected_edge_subgraphs"]) == 29 for record in direct),
            "evidence": [len(record["connected_edge_subgraphs"]) for record in direct],
        },
        {
            "id": "RAW_CONNECTED_CENSUS_51",
            "passed": len(raw["connected_edge_subgraphs"]) == 51,
            "evidence": len(raw["connected_edge_subgraphs"]),
        },
        {
            "id": "LEFT_RIGHT_OUTER_ARE_EXACT_1PI",
            "passed": all(
                {
                    subgraph["subgraph_id"]
                    for subgraph in record["connected_edge_subgraphs"]
                    if subgraph["role"] == "NAMED_ONE_LOOP_CYCLE"
                    and subgraph["one_particle_irreducible"]
                }
                == {"left", "right", "outer"}
                for record in records
            ),
            "evidence": "left,right,outer",
        },
        {
            "id": "CURRENT_CYCLE_FORESTS_EMPTY_OR_SINGLETON",
            "passed": all(
                record["forests"]["current_graph_maximum_structural_forest_cardinality"] == 1
                and len(record["forests"]["structurally_compatible_forests"]) == 4
                for record in records
            ),
            "evidence": [
                record["forests"]["structurally_compatible_forests"] for record in records
            ],
        },
        {
            "id": "ALL_CYCLE_PAIRS_OVERLAP_NON_NESTED",
            "passed": all(
                len(record["forests"]["pair_relations"]) == 3
                and all(
                    relation["relation"] == "OVERLAP_NON_NESTED"
                    and not relation["compatible"]
                    for relation in record["forests"]["pair_relations"]
                )
                for record in records
            ),
            "evidence": "three pair relations per graph",
        },
        {
            "id": "UNKNOWN_RHO_FAILS_CLOSED",
            "passed": all(
                record["power_counting"]["status"] == "BLOCKED_RHO_UNKNOWN_FAIL_CLOSED"
                and record["forests"]["power_counting_forests"] is None
                for record in records
            ),
            "evidence": [record["power_counting"]["unknown_subgraph_ids"] for record in records],
        },
        {
            "id": "RPRIME_KUV_DISTINCT_FROM_KPLUS",
            "passed": all(
                record["renormalization_ast"]["uv_projector"]["symbol"] == "K_UV"
                and record["renormalization_ast"]["uv_projector"][
                    "distinct_from_superspace_projector"
                ]
                for record in records
            ),
            "evidence": "K_UV != K_+",
        },
        {
            "id": "CONTRACTION_COUNTS_EXACT",
            "passed": all(
                all(
                    cograph["counts"][key] == cograph["count_identity"][identity_key]
                    for cograph in record["contractions"]["cographs"]
                    for key, identity_key in (
                        ("L", "L_G_minus_L_gamma"),
                        ("I", "I_G_minus_I_gamma"),
                        ("V", "V_G_minus_V_gamma_plus_one"),
                    )
                )
                for record in records
            ),
            "evidence": "L'=L-L_gamma; I'=I-I_gamma; V'=V-V_gamma+1",
        },
        {
            "id": "TWO_LOOP_MEASURE_MU4EPSILON",
            "passed": bundle["dred_architecture"]["measure"]["mu_power"] == "mu^(4*epsilon)",
            "evidence": bundle["dred_architecture"]["measure"],
        },
        {
            "id": "DRED_RANK_TWO_AND_FOUR_EXACT",
            "passed": (
                rank2_coefficient(Fraction(4)) == Fraction(1, 4)
                and rank4_coefficients(
                    Fraction(4), Fraction(1), Fraction(1), Fraction(1)
                )
                == (Fraction(1, 24), Fraction(1, 24), Fraction(1, 24))
            ),
            "evidence": "1/d and [(d+1)X-Y-Z]/[d(d-1)(d+2)] plus permutations",
        },
        {
            "id": "LAURENT_VALUATION_RULE_EXACT",
            "passed": evanescent_finite_remainder(
                {1: Fraction(3), 2: Fraction(5)},
                {1: Fraction(2), 2: Fraction(7)},
            )
            == Fraction(41),
            "evidence": "finite=a_(-1)e_1+a_(-2)e_2",
        },
        {
            "id": "NO_NUMERATOR_POLE_COEFFICIENT_CLAIM",
            "passed": all(
                record["no_numerator_pole_or_coefficient_claim"]
                and record["renormalization_ast"]["uv_pole"] is None
                and record["renormalization_ast"]["renormalized_coefficient"] is None
                for record in records
            )
            and bundle["global_fail_closed"]["uv_poles"] is None
            and bundle["global_fail_closed"]["renormalized_coefficient"] is None,
            "evidence": bundle["global_fail_closed"],
        },
    ]
    passed = all(check["passed"] for check in checks)
    return {
        "schema_version": "step6.two_loop_forest.audit.v1",
        "status": "PASS" if passed else "FAIL",
        "checks": checks,
        "artifact_sha256": dict(artifact_hashes or {}),
        "failure_count": sum(not check["passed"] for check in checks),
    }


def render_summary(bundle: Mapping[str, Any]) -> str:
    lines = [
        "# Step 6 two-loop forest and DRED architecture — proposal only",
        "",
        "$$",
        "d=4-2\\epsilon,\\qquad",
        "\\omega_4(H)=4L_H-2I_H+\\rho_H.",
        "$$",
        "",
        "`rho=UNKNOWN`; divergence, UV pole, and coefficient remain blocked.",
        "",
    ]
    for record in bundle["graph_records"]:
        lines.extend(
            [
                f"## {record['source_graph_id']}",
                "",
                f"Connected edge subgraphs: `{len(record['connected_edge_subgraphs'])}`.",
                "",
                "$$",
                "\\mathcal F_{\\mathrm{struct}}=",
                "\\{\\varnothing,\\{\\gamma_L\\},\\{\\gamma_R\\},\\{\\gamma_O\\}\\}.",
                "$$",
                "",
            ]
        )
    lines.extend(
        [
            "## Subtraction",
            "",
            "$$",
            "C(\\gamma)=-\\mathsf K_{\\mathrm{UV}}R'\\Phi(\\gamma),",
            "\\qquad",
            "R\\Phi(G)=(1-\\mathsf K_{\\mathrm{UV}})R'\\Phi(G).",
            "$$",
            "",
            "$$",
            "\\int_{k,\\ell}=\\mu^{4\\epsilon}",
            "\\int\\frac{d^dk}{(2\\pi)^d}",
            "\\frac{d^d\\ell}{(2\\pi)^d}.",
            "$$",
            "",
            "No numerator, pole, anomaly, or renormalized coefficient is asserted.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(root: Path) -> dict[str, Any]:
    bundle = build_forest_bundle()
    generated = root / "generated" / "step6" / "two-loop-forest"
    generated.mkdir(parents=True, exist_ok=True)
    direct = [
        record
        for record in bundle["graph_records"]
        if record["source_graph_classification"] == "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT"
    ]
    raw = next(
        record
        for record in bundle["graph_records"]
        if record["source_graph_classification"]
        == "RAW_MARKED_K2_3_THETA_LIFT_NOT_DIRECT_BITRIANGLE"
    )
    payloads = {
        "two-loop-forest.json": bundle,
        "literal-k4-minus-edge-forests.json": {
            "schema_version": SCHEMA_VERSION,
            "graph_records": direct,
        },
        "raw-k23-lift-forest.json": raw,
    }
    artifact_hashes: dict[str, str] = {}
    for filename, payload in payloads.items():
        path = generated / filename
        text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        path.write_text(text, encoding="utf-8")
        artifact_hashes[str(path.relative_to(root))] = sha256(text.encode("utf-8")).hexdigest()
    summary_path = generated / "two-loop-forest.md"
    summary = render_summary(bundle)
    summary_path.write_text(summary, encoding="utf-8")
    artifact_hashes[str(summary_path.relative_to(root))] = sha256(summary.encode("utf-8")).hexdigest()
    audit = build_audit(bundle, artifact_hashes)
    if audit["status"] != "PASS":
        failed = [check["id"] for check in audit["checks"] if not check["passed"]]
        raise RuntimeError(f"Step-6 forest audit failed: {failed}")
    audit_path = root / "audits" / "step6-two-loop-forest-verification.json"
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
                "graph_record_count": len(result["bundle"]["graph_records"]),
                "failure_count": result["audit"]["failure_count"],
                "numerator_certificate_mode": result["bundle"]["numerator_certificate_mode"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
