#!/usr/bin/env python3
"""Proposal-only Step-6 Schwinger--Dyson cut/contact/bubble orbit compiler.

The compiler starts from the three physical K4-minus-edge GraphIR parents,
keeps direct and reflected momentum orientations separate, and emits:

* endpoint-rooted open propagator cuts;
* endpoint-rooted local ``K G = 1`` contact contractions;
* every two-propagator bubble quotient of each one-loop open-cut graph.

This is a graph/occurrence compiler only.  It never performs D-algebra,
numerator reduction, loop integration, Jacobi reduction, or a coefficient
comparison.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import factorial, prod
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_two_loop_grammar as grammar
    from scripts import step6_two_loop_graphir as graphir
    from scripts import step6_two_loop_wick as wick
    from scripts import verify_step5a_fixed_kernel as fixed_kernel
except ModuleNotFoundError:  # direct execution
    import step6_two_loop_grammar as grammar
    import step6_two_loop_graphir as graphir
    import step6_two_loop_wick as wick
    import verify_step5a_fixed_kernel as fixed_kernel


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/sd-orbit"
GENERATED_JSON = GENERATED_DIR / "sd-orbit.json"
GENERATED_MD = GENERATED_DIR / "sd-orbit.md"
AUDIT = ROOT / "audits/step6-sd-orbit-verification.json"

SCHEMA_VERSION = "step6.sd_orbit.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
STAGE = "SCHWINGER_DYSON_GRAPH_OCCURRENCE_ORBIT_NO_DALGEBRA"
SD_IDENTITY = (
    "0=int DV delta/deltaV(F exp(-S/hbar))="
    "<deltaF/deltaV>-hbar^(-1)<F deltaS/deltaV>"
)
DALGEBRA_BLOCK = "BLOCKED_EDGE_TAGGED_DALGEBRA_NUMERATOR_ABSENT"
COEFFICIENT_BLOCK = "BLOCKED_DALGEBRA_INTEGRATION_AND_RENORMALIZATION_ABSENT"


class SDOrbitError(ValueError):
    """Base fail-closed orbit error."""


class ParentGraphError(SDOrbitError):
    """Raised for malformed parent incidence."""


class CutError(SDOrbitError):
    """Raised for an invalid propagator cut."""


class ContactError(SDOrbitError):
    """Raised for an invalid local contact contraction."""


class BubbleError(SDOrbitError):
    """Raised for an invalid two-propagator bubble quotient."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _edge_vertices(edge: Mapping[str, Any]) -> tuple[str, str]:
    return str(edge["source"]), str(edge["target"])


def _vertex_ids(vertices: Sequence[Mapping[str, Any]]) -> list[str]:
    return [str(vertex["vertex_id"]) for vertex in vertices]


def connected(vertices: Sequence[str], edges: Sequence[Mapping[str, Any]]) -> bool:
    if not vertices:
        return False
    adjacency = {vertex: set() for vertex in vertices}
    for edge in edges:
        source, target = _edge_vertices(edge)
        if source not in adjacency or target not in adjacency:
            raise ParentGraphError("edge endpoint does not resolve to a vertex")
        if source != target:
            adjacency[source].add(target)
            adjacency[target].add(source)
    reached = {vertices[0]}
    frontier = [vertices[0]]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - reached:
            reached.add(neighbor)
            frontier.append(neighbor)
    return reached == set(vertices)


def loop_number(vertices: Sequence[str], edges: Sequence[Mapping[str, Any]]) -> int:
    if not connected(vertices, edges):
        raise ParentGraphError("loop number requires a connected graph")
    return len(edges) - len(vertices) + 1


def validate_parent(graph: Mapping[str, Any]) -> None:
    vertices = list(graph["vertices"])
    edges = list(graph["internal_edges"])
    vertex_ids = _vertex_ids(vertices)
    if len(vertex_ids) != len(set(vertex_ids)):
        raise ParentGraphError("duplicate parent vertex id")
    edge_ids = [str(edge["edge_id"]) for edge in edges]
    if len(edge_ids) != len(set(edge_ids)):
        raise ParentGraphError("duplicate parent edge id")
    if len(vertices) != 4 or len(edges) != 5 or loop_number(vertex_ids, edges) != 2:
        raise ParentGraphError("Step-6 literal parent must have V=4,I=5,L=2")
    all_ports = [
        str(port)
        for vertex in vertices
        for port in vertex["quantum_ports"]
    ]
    endpoint_ports = [
        str(port)
        for edge in edges
        for port in (edge["source_port"], edge["target_port"])
    ]
    if sorted(all_ports) != sorted(endpoint_ports) or len(endpoint_ports) != len(
        set(endpoint_ports)
    ):
        raise ParentGraphError("parent quantum ports are not used exactly once")


def enriched_parent_vertices(graph: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for vertex in graph["vertices"]:
        background_momenta = [
            str(port["momentum"]) for port in vertex["background_ports"]
        ]
        source_momenta = [
            str(item["momentum"])
            for item in vertex["momentum_injections"]
            if item["kind"] == "COMPOSITE_SOURCE_MOMENTUM"
        ]
        rows.append(
            {
                **vertex,
                "origin_vertices": [vertex["vertex_id"]],
                "background_momenta": background_momenta,
                "source_momenta": source_momenta,
                "cut_open_half_edge_count": 0,
                "rooted_SD_endpoint": False,
            }
        )
    return rows


def oriented_edge(graph: Mapping[str, Any], orientation: str, edge_id: str) -> dict[str, Any]:
    rows = [
        edge
        for edge in graph["orientations"][orientation]["edges"]
        if edge["edge_id"] == edge_id
    ]
    if len(rows) != 1:
        raise CutError("oriented edge does not resolve uniquely")
    return dict(rows[0])


def denominator_factors(graph: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(factor["edge_id"]): dict(factor)
        for factor in graph["denominator_ast"]["factors"]
    }


def functional_channel(vertex: Mapping[str, Any]) -> dict[str, Any]:
    role = str(vertex["role"])
    if role == "COMPOSITE_INSERTION":
        return {
            "channel": "DELTA_F_INSERTION",
            "SD_zero_sum_sign": 1,
            "identity_term": "<deltaF/deltaV>",
        }
    if role == "ACTION_VERTEX":
        return {
            "channel": "MINUS_F_DELTA_S",
            "SD_zero_sum_sign": -1,
            "identity_term": "-hbar^(-1)<F deltaS/deltaV>",
        }
    raise CutError(f"unsupported SD endpoint role {role}")


def _negate_vector(vector: Sequence[int]) -> list[int]:
    return [-int(value) for value in vector]


def open_endpoint_record(
    base_edge: Mapping[str, Any],
    oriented: Mapping[str, Any],
    vertex_id: str,
    *,
    rooted: bool,
) -> dict[str, Any]:
    if vertex_id == oriented["source"]:
        endpoint = "source"
        momentum_vector = list(oriented["momentum_vector"])
        momentum = str(oriented["momentum"])
        sign = 1
    elif vertex_id == oriented["target"]:
        endpoint = "target"
        momentum_vector = _negate_vector(oriented["momentum_vector"])
        momentum = f"-({oriented['momentum']})"
        sign = -1
    else:
        raise CutError("root vertex is not an endpoint of the cut edge")
    base_port = (
        base_edge["source_port"]
        if vertex_id == base_edge["source"]
        else base_edge["target_port"]
    )
    return {
        "vertex_id": vertex_id,
        "parent_quantum_port_id": base_port,
        "orientation_endpoint": endpoint,
        "incoming_momentum": momentum,
        "incoming_momentum_vector": momentum_vector,
        "orientation_momentum_sign": sign,
        "rooted_functional_derivative_endpoint": rooted,
    }


def bridge_edge_ids(vertices: Sequence[str], edges: Sequence[Mapping[str, Any]]) -> set[str]:
    bridges: set[str] = set()
    for position, edge in enumerate(edges):
        retained = [row for index, row in enumerate(edges) if index != position]
        if not connected(vertices, retained):
            bridges.add(str(edge["edge_id"]))
    return bridges


def source_occurrence_domain(vertex: Mapping[str, Any]) -> dict[str, Any]:
    valence = int(vertex["total_valence"])
    if vertex["role"] == "COMPOSITE_INSERTION":
        terms = grammar.insertion_terms_at_valence(valence)
        return {
            "role": vertex["role"],
            "family": f"I{valence}",
            "allowed_sector": None,
            "term_ids": [term.term_id for term in terms],
            "term_count": len(terms),
            "coefficient_source": "EXACT_PROJECT_GRAMMAR_QI_PER_TERM",
        }
    sectors = {}
    for sector in ("PLUS", "MINUS"):
        terms = grammar.action_terms_at_valence(valence, sector)
        sectors[sector] = {
            "family": f"S{valence}_{sector}",
            "term_ids": [term.term_id for term in terms],
            "term_count": len(terms),
            "coefficients_Qi": [term.coefficient.as_json() for term in terms],
        }
    return {
        "role": vertex["role"],
        "family": f"S{valence}",
        "allowed_sectors": sectors,
        "coefficient_source": "EXACT_PROJECT_GRAMMAR_QI_PER_TERM",
    }


def sector_expansion_table(graph: Mapping[str, Any]) -> list[dict[str, Any]]:
    actions = [vertex for vertex in graph["vertices"] if vertex["role"] == "ACTION_VERTEX"]
    actions.sort(key=lambda row: str(row["vertex_id"]))
    rows = []
    for sectors in product(("PLUS", "MINUS"), repeat=len(actions)):
        multiplicities: dict[str, int] = {}
        assignment = []
        for vertex, sector in zip(actions, sectors, strict=True):
            key = f"{vertex['family']}_{sector}"
            multiplicities[key] = multiplicities.get(key, 0) + 1
            assignment.append({"vertex_id": vertex["vertex_id"], "sector": sector})
        factor = wick.expansion_factor(multiplicities)
        rows.append(
            {
                "assignment": assignment,
                "family_sector_multiplicities": multiplicities,
                "exponential_factor": factor,
                "labeled_action_occurrence_policy": (
                    "NO_ADDITIONAL_AUTOMORPHISM_DIVISION_AFTER_WICK_ENUMERATION"
                ),
            }
        )
    return rows


def _vertex_signature(vertex: Mapping[str, Any], labeled: bool) -> tuple[Any, ...]:
    base = (
        vertex["role"],
        vertex["family"],
        int(vertex["total_valence"]),
        int(vertex["background_valence"]),
        int(vertex["quantum_valence"]),
        int(vertex.get("cut_open_half_edge_count", 0)),
        bool(vertex.get("rooted_SD_endpoint", False)),
    )
    if labeled:
        return base + (
            tuple(sorted(map(str, vertex.get("background_momenta", ())))),
            tuple(sorted(map(str, vertex.get("source_momenta", ())))),
        )
    return base


def automorphism_certificate(
    vertices: Sequence[Mapping[str, Any]], edges: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    ids = _vertex_ids(vertices)
    edge_multiset = Counter(
        tuple(sorted(_edge_vertices(edge))) for edge in edges
    )

    def order(labeled: bool) -> int:
        signatures = {v["vertex_id"]: _vertex_signature(v, labeled) for v in vertices}
        count = 0
        for image in permutations(ids):
            mapping = dict(zip(ids, image, strict=True))
            if any(signatures[vertex] != signatures[mapping[vertex]] for vertex in ids):
                continue
            mapped = Counter(
                tuple(sorted((mapping[source], mapping[target])))
                for source, target in edge_multiset.elements()
            )
            if mapped == edge_multiset:
                count += 1
        return count

    parallel_order = prod(factorial(value) for value in edge_multiset.values())
    typed = order(False)
    labeled = order(True)
    return {
        "vertex_automorphism_order_typed_external_unlabeled": typed,
        "vertex_automorphism_order_background_source_labeled": labeled,
        "parallel_edge_permutation_order": parallel_order,
        "full_multigraph_order_typed": typed * parallel_order,
        "full_multigraph_order_background_source_labeled": labeled * parallel_order,
        "automorphism_denominator_applied": None,
        "policy": "AUDIT_ONLY_LABELED_OCCURRENCES_ARE_NOT_DIVIDED_AGAIN",
    }


def cut_vertices(
    graph: Mapping[str, Any], edge: Mapping[str, Any], root_vertex: str
) -> list[dict[str, Any]]:
    result = enriched_parent_vertices(graph)
    endpoints = set(_edge_vertices(edge))
    for vertex in result:
        if vertex["vertex_id"] in endpoints:
            vertex["cut_open_half_edge_count"] = 1
        if vertex["vertex_id"] == root_vertex:
            vertex["rooted_SD_endpoint"] = True
    return result


def build_cut_descendant(
    graph: Mapping[str, Any], orientation: str, edge_id: str, root_vertex: str
) -> dict[str, Any]:
    validate_parent(graph)
    matches = [edge for edge in graph["internal_edges"] if edge["edge_id"] == edge_id]
    if len(matches) != 1:
        raise CutError("cut edge must resolve exactly once")
    edge = matches[0]
    if root_vertex not in _edge_vertices(edge):
        raise CutError("cut root must be one edge endpoint")
    remaining = [dict(row) for row in graph["internal_edges"] if row["edge_id"] != edge_id]
    vertices = cut_vertices(graph, edge, root_vertex)
    ids = _vertex_ids(vertices)
    if not connected(ids, remaining) or loop_number(ids, remaining) != 1:
        raise CutError("single K4-minus-edge cut must be connected and one-loop")
    bridges = bridge_edge_ids(ids, remaining)
    cycle_edges = sorted(
        str(row["edge_id"]) for row in remaining if row["edge_id"] not in bridges
    )
    if len(cycle_edges) not in {3, 4}:
        raise CutError("open cut must have a unique triangle or box cycle")
    oriented = oriented_edge(graph, orientation, edge_id)
    open_endpoints = [
        open_endpoint_record(edge, oriented, vertex, rooted=vertex == root_vertex)
        for vertex in _edge_vertices(edge)
    ]
    channel = functional_channel(next(v for v in graph["vertices"] if v["vertex_id"] == root_vertex))
    factors = denominator_factors(graph)
    record = {
        "schema_version": "step6.sd_open_cut.v1",
        "descendant_kind": "ROOTED_OPEN_PROPAGATOR_CUT",
        "parent_graph_id": graph["graph_id"],
        "parent_graph_hash": graph["graph_hash"],
        "orientation": orientation,
        "cut_edge_id": edge_id,
        "root_vertex": root_vertex,
        "SD_functional_channel": channel,
        "sign_ledger": {
            "SD_zero_sum_sign": channel["SD_zero_sum_sign"],
            "bosonic_V_endpoint_Koszul_sign": 1,
            "action_exponential_factor": "PARENT_SECTOR_ASSIGNMENT_TABLE_REF",
            "D_algebra_collapse_sign": None,
            "D_algebra_collapse_sign_status": DALGEBRA_BLOCK,
        },
        "vertices": vertices,
        "remaining_propagator_edges": remaining,
        "open_cut_endpoints": open_endpoints,
        "counts": {"V": 4, "I_propagator": 4, "L": 1},
        "bridge_edge_ids": sorted(bridges),
        "unique_cycle_edge_ids": cycle_edges,
        "unique_cycle_length": len(cycle_edges),
        "denominator_ast": {
            "op": "product",
            "factors": [factors[row["edge_id"]] for row in remaining],
            "removed_factor_edge_id": edge_id,
        },
        "automorphisms": automorphism_certificate(vertices, remaining),
        "symmetry_factor_ledger": {
            "rooted_functional_occurrence_multiplicity": 1,
            "labeled_occurrence_weight": 1,
            "automorphism_division": None,
        },
        "downstream": {
            "edge_tagged_D_algebra": {"status": DALGEBRA_BLOCK, "value": None},
            "nonanomalous_numerator_cancellation": {"status": DALGEBRA_BLOCK, "value": None},
            "coefficient": {"status": COEFFICIENT_BLOCK, "value": None},
        },
    }
    record["cut_descendant_id"] = (
        f"{graph['graph_id']}::{orientation}::CUT::{edge_id}::ROOT::{root_vertex}"
    )
    record["cut_descendant_hash"] = digest(record)
    return record


def contact_candidate_domain(
    left: Mapping[str, Any], right: Mapping[str, Any], merged_valence: int
) -> dict[str, Any]:
    roles = {left["role"], right["role"]}
    if "COMPOSITE_INSERTION" in roles:
        terms = grammar.insertion_terms_at_valence(merged_valence)
        return {
            "merged_role": "COMPOSITE_INSERTION",
            "candidate_family": f"I{merged_valence}",
            "candidate_term_ids": [term.term_id for term in terms],
            "candidate_term_count": len(terms),
            "coefficient_equality_to_candidate": None,
            "coefficient_status": (
                "BLOCKED_ORDERED_FUNCTIONAL_DERIVATIVE_AST_JOIN_NOT_PERFORMED"
            ),
        }
    sector_rows = []
    for left_sector, right_sector in product(("PLUS", "MINUS"), repeat=2):
        if left_sector == right_sector:
            terms = grammar.action_terms_at_valence(merged_valence, left_sector)
            candidate = {
                "family": f"S{merged_valence}_{left_sector}",
                "term_ids": [term.term_id for term in terms],
            }
            status = "SAME_SECTOR_SINGLE_ACTION_GRAMMAR_CANDIDATE"
        else:
            candidate = None
            status = "MIXED_SECTOR_CONTACT_NO_SINGLE_CHIRAL_ACTION_TERM"
        sector_rows.append(
            {
                "left_sector": left_sector,
                "right_sector": right_sector,
                "status": status,
                "candidate": candidate,
                "coefficient_equality_to_candidate": None,
            }
        )
    return {
        "merged_role": "ACTION_CONTACT",
        "candidate_family": f"S{merged_valence}",
        "sector_compatibility": sector_rows,
        "coefficient_status": (
            "BLOCKED_ORDERED_FUNCTIONAL_DERIVATIVE_AST_JOIN_NOT_PERFORMED"
        ),
    }


def fuse_contact_vertices(
    graph: Mapping[str, Any], edge: Mapping[str, Any], root_vertex: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    left_id, right_id = _edge_vertices(edge)
    parent_vertices = {v["vertex_id"]: v for v in enriched_parent_vertices(graph)}
    left = parent_vertices[left_id]
    right = parent_vertices[right_id]
    merged_id = "F_" + "_".join(sorted((left_id, right_id)))
    merged_total = int(left["total_valence"]) + int(right["total_valence"]) - 2
    merged_background = int(left["background_valence"]) + int(right["background_valence"])
    merged_quantum = int(left["quantum_valence"]) + int(right["quantum_valence"]) - 2
    candidate = contact_candidate_domain(left, right, merged_total)
    merged = {
        "vertex_id": merged_id,
        "role": candidate["merged_role"],
        "family": candidate["candidate_family"],
        "total_valence": merged_total,
        "background_valence": merged_background,
        "quantum_valence": merged_quantum,
        "background_ports": [*left["background_ports"], *right["background_ports"]],
        "momentum_injections": [
            *left["momentum_injections"],
            *right["momentum_injections"],
        ],
        "origin_vertices": sorted((left_id, right_id)),
        "background_momenta": sorted(
            [*left["background_momenta"], *right["background_momenta"]]
        ),
        "source_momenta": sorted([*left["source_momenta"], *right["source_momenta"]]),
        "cut_open_half_edge_count": 0,
        "rooted_SD_endpoint": True,
        "root_origin_vertex": root_vertex,
    }
    vertices = [
        vertex
        for vertex_id, vertex in parent_vertices.items()
        if vertex_id not in {left_id, right_id}
    ] + [merged]
    vertices.sort(key=lambda row: str(row["vertex_id"]))
    remaining = []
    for source_edge in graph["internal_edges"]:
        if source_edge["edge_id"] == edge["edge_id"]:
            continue
        row = dict(source_edge)
        if row["source"] in {left_id, right_id}:
            row["source"] = merged_id
        if row["target"] in {left_id, right_id}:
            row["target"] = merged_id
        if row["source"] == row["target"]:
            raise ContactError("single-edge contraction produced an untracked self-loop")
        remaining.append(row)
    incident = Counter(
        vertex
        for row in remaining
        for vertex in (row["source"], row["target"])
    )
    if any(incident[v["vertex_id"]] != int(v["quantum_valence"]) for v in vertices):
        raise ContactError("fused contact quantum valence does not match remaining edges")
    return vertices, remaining, candidate


def contact_classification(candidate: Mapping[str, Any], merged_valence: int) -> str:
    if merged_valence == 4 and candidate["merged_role"] == "COMPOSITE_INSERTION":
        return "QUARTIC_INSERTION_CONTACT"
    if merged_valence == 4:
        return "QUARTIC_ACTION_CONTACT"
    if candidate["merged_role"] == "COMPOSITE_INSERTION":
        return "NONLINEAR_INSERTION_CONTACT"
    return "HIGHER_ACTION_CONTACT"


def build_contact_child(
    graph: Mapping[str, Any], orientation: str, edge_id: str, root_vertex: str,
    kernel_certificate: Mapping[str, Any]
) -> dict[str, Any]:
    matches = [edge for edge in graph["internal_edges"] if edge["edge_id"] == edge_id]
    if len(matches) != 1:
        raise ContactError("contact edge must resolve exactly once")
    edge = matches[0]
    if root_vertex not in _edge_vertices(edge):
        raise ContactError("contact root must be one contracted endpoint")
    vertices, remaining, candidate = fuse_contact_vertices(graph, edge, root_vertex)
    ids = _vertex_ids(vertices)
    if len(vertices) != 3 or len(remaining) != 4 or loop_number(ids, remaining) != 2:
        raise ContactError("local edge contraction must have V=3,I=4,L=2")
    parent_vertex = next(v for v in graph["vertices"] if v["vertex_id"] == root_vertex)
    channel = functional_channel(parent_vertex)
    merged = next(v for v in vertices if root_vertex in v["origin_vertices"] and len(v["origin_vertices"]) == 2)
    factors = denominator_factors(graph)
    record = {
        "schema_version": "step6.sd_contact_child.v1",
        "descendant_kind": "ROOTED_LOCAL_KG_CONTACT_CHILD",
        "parent_graph_id": graph["graph_id"],
        "parent_graph_hash": graph["graph_hash"],
        "orientation": orientation,
        "contracted_edge_id": edge_id,
        "root_vertex": root_vertex,
        "SD_functional_channel": channel,
        "contact_classification": contact_classification(
            candidate, int(merged["total_valence"])
        ),
        "merged_vertex": merged,
        "contact_grammar_candidate_domain": candidate,
        "source_occurrence_product_preserved": [
            source_occurrence_domain(
                next(v for v in graph["vertices"] if v["vertex_id"] == origin)
            )
            for origin in merged["origin_vertices"]
        ],
        "sign_ledger": {
            "SD_zero_sum_sign": channel["SD_zero_sum_sign"],
            "bosonic_V_endpoint_Koszul_sign": 1,
            "K_times_G_identity_sign": 1,
            "K_times_G_certificate_sha256": kernel_certificate["verification_sha256"],
            "source_Qi_product": "PRESERVED_FACTORIZED_NOT_ASSEMBLED",
            "D_algebra_endpoint_transfer_sign": None,
            "D_algebra_endpoint_transfer_status": DALGEBRA_BLOCK,
        },
        "vertices": vertices,
        "remaining_propagator_edges": remaining,
        "counts": {"V": 3, "I_propagator": 4, "L": 2},
        "denominator_ast": {
            "op": "product",
            "factors": [factors[row["edge_id"]] for row in remaining],
            "locally_collapsed_edge_id": edge_id,
        },
        "automorphisms": automorphism_certificate(vertices, remaining),
        "symmetry_factor_ledger": {
            "rooted_functional_occurrence_multiplicity": 1,
            "labeled_occurrence_weight": 1,
            "automorphism_division": None,
            "source_action_exponential_factor": "PARENT_SECTOR_ASSIGNMENT_TABLE_REF",
        },
        "downstream": {
            "edge_tagged_D_algebra": {"status": DALGEBRA_BLOCK, "value": None},
            "ordinary_nonanomalous_numerator_cancellation": {
                "status": DALGEBRA_BLOCK,
                "value": None,
            },
            "coefficient": {"status": COEFFICIENT_BLOCK, "value": None},
        },
    }
    record["contact_child_id"] = (
        f"{graph['graph_id']}::{orientation}::CONTACT::{edge_id}::ROOT::{root_vertex}"
    )
    record["contact_child_hash"] = digest(record)
    return record


class UnionFind:
    def __init__(self, values: Sequence[str]):
        self.parent = {value: value for value in values}

    def find(self, value: str) -> str:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: str, right: str) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[max(a, b)] = min(a, b)


def bubble_supervertices(
    cut: Mapping[str, Any], retained_edge_ids: Sequence[str]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    if len(retained_edge_ids) != 2 or len(set(retained_edge_ids)) != 2:
        raise BubbleError("bubble quotient requires two distinct retained cycle edges")
    cycle = set(cut["unique_cycle_edge_ids"])
    if not set(retained_edge_ids) <= cycle:
        raise BubbleError("bubble retained edges must lie on the unique cycle")
    vertices = list(cut["vertices"])
    vertex_ids = _vertex_ids(vertices)
    remaining_edges = list(cut["remaining_propagator_edges"])
    contract_ids = sorted(
        str(edge["edge_id"])
        for edge in remaining_edges
        if edge["edge_id"] not in set(retained_edge_ids)
    )
    union = UnionFind(vertex_ids)
    for edge in remaining_edges:
        if edge["edge_id"] in contract_ids:
            union.union(str(edge["source"]), str(edge["target"]))
    groups: dict[str, list[str]] = defaultdict(list)
    for vertex_id in vertex_ids:
        groups[union.find(vertex_id)].append(vertex_id)
    if len(groups) != 2:
        raise BubbleError("cycle quotient did not produce exactly two supervertices")
    parent_by_id = {v["vertex_id"]: v for v in vertices}
    supervertices = []
    origin_to_super: dict[str, str] = {}
    for ordinal, origins in enumerate(sorted((sorted(v) for v in groups.values())), start=1):
        super_id = f"U{ordinal}"
        for origin in origins:
            origin_to_super[origin] = super_id
        members = [parent_by_id[origin] for origin in origins]
        supervertices.append(
            {
                "vertex_id": super_id,
                "role": "BUBBLE_CONTACT_SUPERVERTEX",
                "family": "CONTACT_FOREST",
                "total_valence": 2
                + sum(int(member["background_valence"]) for member in members)
                + sum(int(member.get("cut_open_half_edge_count", 0)) for member in members),
                "background_valence": sum(
                    int(member["background_valence"]) for member in members
                ),
                "quantum_valence": 2,
                "origin_vertices": origins,
                "origin_vertex_type_multiset": sorted(
                    f"{member['role']}:{member['family']}" for member in members
                ),
                "background_momenta": sorted(
                    momentum for member in members for momentum in member["background_momenta"]
                ),
                "source_momenta": sorted(
                    momentum for member in members for momentum in member["source_momenta"]
                ),
                "cut_open_half_edge_count": sum(
                    int(member.get("cut_open_half_edge_count", 0)) for member in members
                ),
                "rooted_SD_endpoint": any(
                    bool(member.get("rooted_SD_endpoint", False)) for member in members
                ),
                "contact_contraction_edge_ids": [
                    edge_id
                    for edge_id in contract_ids
                    if any(
                        parent_by_id[origin]["vertex_id"] in _edge_vertices(edge)
                        for origin in origins
                        for edge in remaining_edges
                        if edge["edge_id"] == edge_id
                    )
                ],
            }
        )
    retained = []
    for edge in remaining_edges:
        if edge["edge_id"] not in set(retained_edge_ids):
            continue
        row = dict(edge)
        row["source"] = origin_to_super[str(edge["source"])]
        row["target"] = origin_to_super[str(edge["target"])]
        if row["source"] == row["target"]:
            raise BubbleError("retained bubble propagator became a self-loop")
        retained.append(row)
    if len(retained) != 2 or len(
        {tuple(sorted(_edge_vertices(edge))) for edge in retained}
    ) != 1:
        raise BubbleError("retained propagators are not a parallel bubble pair")
    return supervertices, retained, contract_ids


def build_bubble_child(
    graph: Mapping[str, Any], cut: Mapping[str, Any], retained_edge_ids: Sequence[str]
) -> dict[str, Any]:
    supervertices, retained, contact_edges = bubble_supervertices(cut, retained_edge_ids)
    ids = _vertex_ids(supervertices)
    if loop_number(ids, retained) != 1:
        raise BubbleError("two-edge parallel quotient must have L=1")
    factors = denominator_factors(graph)
    record = {
        "schema_version": "step6.sd_bubble.v1",
        "descendant_kind": "ROOTED_TWO_PROPAGATOR_BUBBLE_QUOTIENT",
        "parent_graph_id": graph["graph_id"],
        "parent_graph_hash": graph["graph_hash"],
        "orientation": cut["orientation"],
        "source_cut_descendant_id": cut["cut_descendant_id"],
        "source_cut_edge_id": cut["cut_edge_id"],
        "root_vertex": cut["root_vertex"],
        "SD_functional_channel": cut["SD_functional_channel"],
        "retained_propagator_edge_ids": list(retained_edge_ids),
        "contact_contraction_edge_ids": contact_edges,
        "supervertices": supervertices,
        "propagator_edges": retained,
        "counts": {"V": 2, "I_propagator": 2, "L": 1},
        "denominator_ast": {
            "op": "product",
            "factors": [factors[edge_id] for edge_id in retained_edge_ids],
        },
        "sign_ledger": {
            "SD_zero_sum_sign": cut["SD_functional_channel"]["SD_zero_sum_sign"],
            "bosonic_V_Koszul_sign": 1,
            "contact_contraction_KG_sign_each": 1,
            "D_algebra_endpoint_transfer_sign": None,
            "D_algebra_endpoint_transfer_status": DALGEBRA_BLOCK,
        },
        "automorphisms": automorphism_certificate(supervertices, retained),
        "symmetry_factor_ledger": {
            "derivation_path_multiplicity": 1,
            "labeled_occurrence_weight": 1,
            "parallel_edge_permutation_is_automorphism_audit_only": True,
            "automorphism_division": None,
        },
        "downstream": {
            "bubble_D_algebra_numerator": {"status": DALGEBRA_BLOCK, "value": None},
            "ordinary_nonanomalous_parent_bubble_cancellation": {
                "status": DALGEBRA_BLOCK,
                "value": None,
            },
            "integral": {"status": DALGEBRA_BLOCK, "value": None},
            "coefficient": {"status": COEFFICIENT_BLOCK, "value": None},
        },
    }
    family_record = {
        "source_cut_cycle_length": cut["unique_cycle_length"],
        "SD_functional_channel": cut["SD_functional_channel"]["channel"],
        "supervertex_types": sorted(
            (
                tuple(vertex["origin_vertex_type_multiset"]),
                tuple(vertex["background_momenta"]),
                tuple(vertex["source_momenta"]),
                vertex["cut_open_half_edge_count"],
                vertex["rooted_SD_endpoint"],
            )
            for vertex in supervertices
        ),
        "parallel_propagator_count": 2,
        "contact_contraction_count": len(contact_edges),
    }
    record["bubble_family_signature_record"] = family_record
    record["bubble_family_signature_sha256"] = digest(family_record)
    retained_tag = "+".join(retained_edge_ids)
    record["bubble_child_id"] = (
        f"{cut['cut_descendant_id']}::BUBBLE::{retained_tag}"
    )
    record["bubble_child_hash"] = digest(record)
    return record


def fixed_kernel_certificate() -> dict[str, Any]:
    verification = fixed_kernel.run_verification()
    if verification["status"] != "PASS" or verification["totals"]["failed"] != 0:
        raise ContactError("Step-5A fixed kernel verification failed")
    required = {
        "left_product": "K_(AB)^tot*G^(BC)=delta_A^C*1_16",
        "right_product": "G^(AB)*K_(BC)^tot=delta^A_C*1_16",
    }
    if any(
        verification["derived_equations"].get(key) != value
        for key, value in required.items()
    ):
        raise ContactError("Step-5A K G identity changed")
    return {
        "K_times_G": 1,
        "G_times_K": 1,
        "verification_sha256": digest(verification),
        "verification_check_count": verification["totals"]["checks"],
    }


def parent_orbit(graph: Mapping[str, Any], orientation: str, kernel: Mapping[str, Any]) -> dict[str, Any]:
    validate_parent(graph)
    cuts = []
    contacts = []
    bubbles = []
    links = []
    for edge in graph["internal_edges"]:
        edge_id = str(edge["edge_id"])
        for root_vertex in _edge_vertices(edge):
            cut = build_cut_descendant(graph, orientation, edge_id, root_vertex)
            contact = build_contact_child(
                graph, orientation, edge_id, root_vertex, kernel
            )
            child_bubbles = [
                build_bubble_child(graph, cut, retained)
                for retained in combinations(cut["unique_cycle_edge_ids"], 2)
            ]
            cuts.append(cut)
            contacts.append(contact)
            bubbles.extend(child_bubbles)
            links.append(
                {
                    "parent_edge_id": edge_id,
                    "root_vertex": root_vertex,
                    "cut_descendant_id": cut["cut_descendant_id"],
                    "contact_child_id": contact["contact_child_id"],
                    "bubble_child_ids": [row["bubble_child_id"] for row in child_bubbles],
                    "SD_zero_sum_sign": cut["SD_functional_channel"]["SD_zero_sum_sign"],
                }
            )
    if len(cuts) != 10 or len(contacts) != 10 or len(bubbles) != 36:
        raise SDOrbitError("unexpected K4-minus-edge rooted orbit census")
    row = {
        "parent_graph_id": graph["graph_id"],
        "parent_graph_hash": graph["graph_hash"],
        "orientation": orientation,
        "orientation_hash": graph["orientations"][orientation]["orientation_hash"],
        "source_vertex_occurrence_domains": {
            vertex["vertex_id"]: source_occurrence_domain(vertex)
            for vertex in graph["vertices"]
        },
        "source_action_sector_expansion_table": sector_expansion_table(graph),
        "source_automorphisms": graph["automorphisms"],
        "rooted_open_cuts": cuts,
        "rooted_contact_children": contacts,
        "rooted_bubble_derivation_paths": bubbles,
        "orbit_links": links,
        "census": {
            "rooted_open_cut_count": len(cuts),
            "rooted_contact_child_count": len(contacts),
            "rooted_bubble_derivation_path_count": len(bubbles),
            "cycle_length_histogram_for_rooted_cuts": dict(
                sorted(Counter(row["unique_cycle_length"] for row in cuts).items())
            ),
            "contact_classification_histogram": dict(
                sorted(Counter(row["contact_classification"] for row in contacts).items())
            ),
            "bubble_family_signature_histogram": dict(
                sorted(
                    Counter(
                        row["bubble_family_signature_sha256"] for row in bubbles
                    ).items()
                )
            ),
        },
        "cancellation_gate": {
            "SD_identity": SD_IDENTITY,
            "ordinary_nonanomalous_numerator_terms": None,
            "bubble_contact_parent_pairing": None,
            "status": DALGEBRA_BLOCK,
            "reason": (
                "graph orbit and exact occurrence signs are fixed; edge-tagged derivative "
                "words and scalar numerators are not compiled"
            ),
            "anomaly_coefficient": None,
        },
    }
    row["parent_orbit_hash"] = digest(row)
    return row


def build_payload() -> dict[str, Any]:
    graph_bundle = graphir.build_bundle()
    grammar_payload = grammar.build_payload()
    wick_payload, _ = wick.build_payload()
    kernel = fixed_kernel_certificate()
    graphs = list(graph_bundle["literal_direct_graphs"])
    orbits = [
        parent_orbit(graph, orientation, kernel)
        for graph in graphs
        for orientation in ("direct", "reflected")
    ]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "scope": "THREE_LITERAL_K4_MINUS_EDGE_PARENTS_BOTH_ORIENTATIONS",
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "input_firewall": {
            "allowed_modules": [
                "scripts/step6_two_loop_graphir.py",
                "scripts/step6_two_loop_grammar.py",
                "scripts/step6_two_loop_wick.py",
                "scripts/verify_step5a_fixed_kernel.py",
            ],
            "external_target_or_review_read": False,
        },
        "input_provenance": {
            "graph_bundle_sha256": graph_bundle["bundle_hash"],
            "grammar_payload_sha256": digest(grammar_payload),
            "wick_payload_sha256": wick_payload["payload_sha256"],
            "generator_sha256": {
                path: file_sha256(ROOT / path)
                for path in (
                    "scripts/step6_two_loop_graphir.py",
                    "scripts/step6_two_loop_grammar.py",
                    "scripts/step6_two_loop_wick.py",
                    "scripts/verify_step5a_fixed_kernel.py",
                )
            },
        },
        "Schwinger_Dyson_identity": {
            "equation": SD_IDENTITY,
            "delta_F_sign": 1,
            "minus_F_delta_S_sign": -1,
            "bosonic_V_Koszul_sign": 1,
        },
        "fixed_kernel_identity": kernel,
        "orbits": orbits,
        "orbit_count": len(orbits),
        "global_census": {
            "rooted_open_cut_count": sum(len(row["rooted_open_cuts"]) for row in orbits),
            "rooted_contact_child_count": sum(
                len(row["rooted_contact_children"]) for row in orbits
            ),
            "rooted_bubble_derivation_path_count": sum(
                len(row["rooted_bubble_derivation_paths"]) for row in orbits
            ),
        },
        "global_cancellation_gate": {
            "ordinary_nonanomalous_numerator_cancellation": {
                "status": DALGEBRA_BLOCK,
                "value": None,
            },
            "D_algebra": {"status": DALGEBRA_BLOCK, "value": None},
            "integrals": {"status": DALGEBRA_BLOCK, "value": None},
            "renormalized_coefficient": {"status": COEFFICIENT_BLOCK, "value": None},
        },
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    )
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    orbits = payload["orbits"]
    cuts = [child for orbit in orbits for child in orbit["rooted_open_cuts"]]
    contacts = [child for orbit in orbits for child in orbit["rooted_contact_children"]]
    bubbles = [
        child for orbit in orbits for child in orbit["rooted_bubble_derivation_paths"]
    ]
    return {
        "six_oriented_parent_orbits": len(orbits) == 6
        and len({(row["parent_graph_id"], row["orientation"]) for row in orbits}) == 6,
        "exact_rooted_census_60_60_216": len(cuts) == 60
        and len(contacts) == 60
        and len(bubbles) == 216,
        "every_cut_is_connected_one_loop_four_propagators": all(
            child["counts"] == {"V": 4, "I_propagator": 4, "L": 1}
            and len(child["open_cut_endpoints"]) == 2
            for child in cuts
        ),
        "cut_cycle_histogram_per_orbit_is_3_to_8_and_4_to_2": all(
            orbit["census"]["cycle_length_histogram_for_rooted_cuts"]
            == {3: 8, 4: 2}
            for orbit in orbits
        ),
        "every_contact_is_V3_I4_L2_with_KG_plus_one": all(
            child["counts"] == {"V": 3, "I_propagator": 4, "L": 2}
            and child["sign_ledger"]["K_times_G_identity_sign"] == 1
            for child in contacts
        ),
        "every_bubble_is_two_parallel_propagators": all(
            child["counts"] == {"V": 2, "I_propagator": 2, "L": 1}
            and len(child["retained_propagator_edge_ids"]) == 2
            and child["automorphisms"]["parallel_edge_permutation_order"] == 2
            for child in bubbles
        ),
        "functional_signs_are_exact_by_root_role": all(
            child["SD_functional_channel"]["SD_zero_sum_sign"]
            == (
                1
                if child["SD_functional_channel"]["channel"] == "DELTA_F_INSERTION"
                else -1
            )
            for child in [*cuts, *contacts, *bubbles]
        ),
        "bosonic_Koszul_sign_is_plus_one": all(
            child["sign_ledger"].get(
                "bosonic_V_endpoint_Koszul_sign",
                child["sign_ledger"].get("bosonic_V_Koszul_sign"),
            )
            == 1
            for child in [*cuts, *contacts, *bubbles]
        ),
        "automorphisms_are_audit_only": all(
            child["automorphisms"]["automorphism_denominator_applied"] is None
            for child in [*cuts, *contacts, *bubbles]
        ),
        "source_action_expansion_has_all_eight_sector_assignments": all(
            len(orbit["source_action_sector_expansion_table"]) == 8 for orbit in orbits
        ),
        "no_Dalgebra_integral_or_coefficient_claim": all(
            gate["value"] is None
            for gate in payload["global_cancellation_gate"].values()
        )
        and all(
            orbit["cancellation_gate"]["status"] == DALGEBRA_BLOCK
            and orbit["cancellation_gate"]["anomaly_coefficient"] is None
            for orbit in orbits
        ),
        "external_input_firewall": payload["external_result_used_as_calculation_input"]
        is False
        and payload["input_firewall"]["external_target_or_review_read"] is False,
    }


def build_audit(
    payload: Mapping[str, Any], artifact_hashes: Mapping[str, str] | None = None
) -> dict[str, Any]:
    checks = exact_checks(payload)
    return {
        "schema_version": "step6.sd_orbit.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "totals": {
            "checks": len(checks),
            "passed": sum(checks.values()),
            "failed": sum(not value for value in checks.values()),
        },
        "global_census": payload["global_census"],
        "payload_sha256": payload["payload_sha256"],
        "artifact_sha256": dict(artifact_hashes or {}),
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    dalgebra_block_tex = DALGEBRA_BLOCK.replace("_", "\\_")
    lines = [
        "# Step 6 — Schwinger–Dyson cut/contact/bubble orbit",
        "",
        f"Status: `{payload['status']}`",
        "",
        "$$",
        "0=\\int \\mathcal DV\\,\\frac{\\delta}{\\delta V}",
        "\\left(\\mathcal F e^{-S/\\hbar}\\right)",
        "=\\left\\langle\\frac{\\delta\\mathcal F}{\\delta V}\\right\\rangle",
        "-\\hbar^{-1}\\left\\langle\\mathcal F\\frac{\\delta S}{\\delta V}\\right\\rangle.",
        "$$",
        "",
        "$$",
        "K_VG_V=G_VK_V=1.",
        "$$",
        "",
        "| parent | orientation | rooted cuts | contacts | bubble paths |",
        "|---|---:|---:|---:|---:|",
    ]
    for orbit in payload["orbits"]:
        census = orbit["census"]
        lines.append(
            f"| `{orbit['parent_graph_id']}` | `{orbit['orientation']}` | "
            f"{census['rooted_open_cut_count']} | "
            f"{census['rooted_contact_child_count']} | "
            f"{census['rooted_bubble_derivation_path_count']} |"
        )
    census = payload["global_census"]
    lines.extend(
        [
            "",
            "$$",
            "(N_{\\rm cut},N_{\\rm contact},N_{\\rm bubble})="
            f"({census['rooted_open_cut_count']},"
            f"{census['rooted_contact_child_count']},"
            f"{census['rooted_bubble_derivation_path_count']}).",
            "$$",
            "",
            "$$",
            "\\mathcal N_{\\rm parent}+\\mathcal N_{\\rm contact}",
            "+\\mathcal N_{\\rm bubble}:\\quad",
            f"\\text{{{dalgebra_block_tex}}}.",
            "$$",
            "",
            f"Verification: `{audit['status']}`; "
            f"{audit['totals']['passed']}/{audit['totals']['checks']} checks.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    provisional = build_audit(payload)
    GENERATED_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload, provisional), encoding="utf-8")
    hashes = {
        str(GENERATED_JSON.relative_to(ROOT)): file_sha256(GENERATED_JSON),
        str(GENERATED_MD.relative_to(ROOT)): file_sha256(GENERATED_MD),
    }
    audit = build_audit(payload, hashes)
    GENERATED_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    hashes[str(GENERATED_MD.relative_to(ROOT))] = file_sha256(GENERATED_MD)
    audit = build_audit(payload, hashes)
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "checks": audit["totals"],
                "orbits": payload["orbit_count"],
                "census": payload["global_census"],
                "output": str(GENERATED_JSON.relative_to(ROOT)),
            },
            sort_keys=True,
        )
    )
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
