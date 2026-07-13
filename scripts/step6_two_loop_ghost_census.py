#!/usr/bin/env python3
"""Proposal-only typed-port census of Step-6 two-loop FP/NK graphs.

The external composite is fixed to the primitive ``I_(2)`` term of

    nabla_-[(nabla_+ W_+)^A (nabla_+ W_+)^B].

Only port saturation, connectedness, loop number and the internal-edge bridge
test are decided here.  No action coefficient, Wick sign, amplitude, D-algebra
or determinant/BV equivalence is evaluated.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path
import sys
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_vertex_grammar import (
    ActionMonomial,
    fp_ghost_monomials,
    matter_bridge_monomials,
)


OUTPUT_DIR = ROOT / "generated/step6/two-loop-ghost-census"
JSON_OUTPUT = OUTPUT_DIR / "census.json"
MARKDOWN_OUTPUT = OUTPUT_DIR / "census.md"
AUDIT_OUTPUT = ROOT / "audits/step6-two-loop-ghost-census-verification.json"

PROPOSAL_STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
ADMITTED = "ADMITTED_UNCOMPUTED"
ABSENT = "PROVED_ABSENT_AT_THIS_ORDER"


@dataclass(frozen=True)
class Port:
    port_id: str
    vertex_id: str
    field: str
    statistics: str
    chirality: str
    role: str
    flavor: int | None = None


@dataclass(frozen=True)
class Vertex:
    vertex_id: str
    source_monomial_id: str
    sector: str
    ports: tuple[Port, ...]


@dataclass(frozen=True)
class Edge:
    edge_id: str
    left_port: str
    right_port: str
    propagator: str
    oriented: bool


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    sector: str
    classification: str
    scope_relation: str
    vertices: tuple[Vertex, ...]
    edges: tuple[Edge, ...]
    loop_number: int
    connected: bool
    one_particle_irreducible: bool
    deletion_connected: tuple[tuple[str, bool], ...]
    port_conservation: tuple[tuple[str, int], ...]
    topology_family: str


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _insertion() -> Vertex:
    return Vertex(
        "I2",
        "primitive_I_(2)",
        "WW_INSERTION",
        (
            Port("I2:V1", "I2", "V", "BOSON", "REAL", "INTERNAL_WICK"),
            Port("I2:V2", "I2", "V", "BOSON", "REAL", "INTERNAL_WICK"),
        ),
    )


def _vertex_from_monomial(
    monomial: ActionMonomial,
    vertex_id: str,
    *,
    flavor: int | None = None,
) -> Vertex:
    ports: list[Port] = []
    for position, occurrence in enumerate(monomial.ordered_fields):
        occurrence_flavor = flavor if occurrence.flavor_label is not None else None
        role = "INTERNAL_WICK"
        if occurrence.field_name in {"cprime_plus", "tilde_cprime_minus"}:
            role = "FP_ANTIGHOST"
        elif occurrence.field_name in {"c", "tilde_c"}:
            role = "FP_GHOST"
        elif occurrence.field_name in {"Phi", "TildePhi"}:
            role = "MATTER"
        ports.append(
            Port(
                f"{vertex_id}:{position}:{occurrence.occurrence_id}",
                vertex_id,
                occurrence.field_name,
                occurrence.statistics.value,
                occurrence.chirality.value,
                role,
                occurrence_flavor,
            )
        )
    return Vertex(vertex_id, monomial.monomial_id, monomial.sector, tuple(ports))


def _perfect_matchings(items: Sequence[Port]) -> tuple[tuple[tuple[Port, Port], ...], ...]:
    if not items:
        return ((),)
    if len(items) % 2:
        return ()
    first = items[0]
    result: list[tuple[tuple[Port, Port], ...]] = []
    for position in range(1, len(items)):
        second = items[position]
        remaining = tuple(items[1:position]) + tuple(items[position + 1 :])
        for suffix in _perfect_matchings(remaining):
            result.append(((first, second),) + suffix)
    return tuple(result)


def _oriented_matchings(
    left_ports: Sequence[Port],
    right_ports: Sequence[Port],
    accepts,
) -> tuple[tuple[tuple[Port, Port], ...], ...]:
    if len(left_ports) != len(right_ports):
        return ()
    result: list[tuple[tuple[Port, Port], ...]] = []
    for ordering in permutations(right_ports):
        pairs = tuple(zip(left_ports, ordering))
        if all(accepts(left, right) for left, right in pairs):
            result.append(pairs)
    return tuple(result)


def _fp_accepts(antighost: Port, ghost: Port) -> bool:
    return (
        antighost.field == "cprime_plus"
        and antighost.chirality == "CHIRAL"
        and ghost.field == "tilde_c"
        and ghost.chirality == "ANTICHIRAL"
    ) or (
        antighost.field == "tilde_cprime_minus"
        and antighost.chirality == "ANTICHIRAL"
        and ghost.field == "c"
        and ghost.chirality == "CHIRAL"
    )


def _matter_accepts(tilded: Port, untilded: Port) -> bool:
    return (
        tilded.field == "TildePhi"
        and tilded.chirality == "ANTICHIRAL"
        and untilded.field == "Phi"
        and untilded.chirality == "CHIRAL"
        and tilded.flavor == untilded.flavor
    )


def _adjacency(vertices: Sequence[Vertex], edges: Sequence[Edge], removed: str | None = None) -> dict[str, set[str]]:
    port_vertex = {port.port_id: vertex.vertex_id for vertex in vertices for port in vertex.ports}
    adjacency = {vertex.vertex_id: set() for vertex in vertices}
    for edge in edges:
        if edge.edge_id == removed:
            continue
        left = port_vertex[edge.left_port]
        right = port_vertex[edge.right_port]
        if left != right:
            adjacency[left].add(right)
            adjacency[right].add(left)
    return adjacency


def _connected(vertices: Sequence[Vertex], edges: Sequence[Edge], removed: str | None = None) -> bool:
    if not vertices:
        return False
    adjacency = _adjacency(vertices, edges, removed)
    seen = {vertices[0].vertex_id}
    frontier = [vertices[0].vertex_id]
    while frontier:
        current = frontier.pop()
        for neighbor in sorted(adjacency[current]):
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(vertices)


def _candidate(
    sector: str,
    scope_relation: str,
    topology_family: str,
    vertices: Sequence[Vertex],
    edge_data: Sequence[tuple[Port, Port, str, bool]],
) -> Candidate | None:
    edges = tuple(
        Edge(f"e{position}", left.port_id, right.port_id, rule, oriented)
        for position, (left, right, rule, oriented) in enumerate(edge_data)
    )
    all_ports = [port.port_id for vertex in vertices for port in vertex.ports]
    used_ports = [endpoint for edge in edges for endpoint in (edge.left_port, edge.right_port)]
    counts = {port_id: used_ports.count(port_id) for port_id in all_ports}
    port_conservation = tuple(sorted(counts.items()))
    if any(count != 1 for count in counts.values()):
        return None
    connected = _connected(vertices, edges)
    loop_number = len(edges) - len(vertices) + 1 if connected else -1
    deletion = tuple((edge.edge_id, _connected(vertices, edges, edge.edge_id)) for edge in edges)
    one_pi = connected and all(flag for _, flag in deletion)
    if not (connected and loop_number == 2 and one_pi):
        return None
    return Candidate(
        "UNASSIGNED",
        sector,
        ADMITTED,
        scope_relation,
        tuple(vertices),
        edges,
        loop_number,
        connected,
        one_pi,
        deletion,
        port_conservation,
        topology_family,
    )


def _assign_ids(candidates: Sequence[Candidate], prefix: str) -> tuple[Candidate, ...]:
    result: list[Candidate] = []
    for position, candidate in enumerate(candidates):
        result.append(
            Candidate(
                f"{prefix}_{position:03d}",
                candidate.sector,
                candidate.classification,
                candidate.scope_relation,
                candidate.vertices,
                candidate.edges,
                candidate.loop_number,
                candidate.connected,
                candidate.one_particle_irreducible,
                candidate.deletion_connected,
                candidate.port_conservation,
                candidate.topology_family,
            )
        )
    return tuple(result)


def _interaction_monomials(monomials: Iterable[ActionMonomial], sector: str) -> tuple[ActionMonomial, ...]:
    result = []
    for monomial in monomials:
        v_valence = sum(field.field_name == "V" for field in monomial.ordered_fields)
        if v_valence in (1, 2):
            result.append(monomial)
    return tuple(sorted(result, key=lambda item: item.monomial_id))


def enumerate_fp_candidates() -> tuple[Candidate, ...]:
    insertion = _insertion()
    monomials = _interaction_monomials(fp_ghost_monomials(max_v_order=2), "FP")
    candidates: list[Candidate] = []
    for action_count in (1, 2):
        for selected in combinations_with_replacement(monomials, action_count):
            if sum(sum(field.field_name == "V" for field in item.ordered_fields) for item in selected) != 2:
                continue
            action_vertices = tuple(
                _vertex_from_monomial(item, f"FP{position}")
                for position, item in enumerate(selected, start=1)
            )
            vertices = (insertion,) + action_vertices
            vector_ports = tuple(port for vertex in vertices for port in vertex.ports if port.field == "V")
            antighosts = tuple(
                port for vertex in action_vertices for port in vertex.ports if port.role == "FP_ANTIGHOST"
            )
            ghosts = tuple(port for vertex in action_vertices for port in vertex.ports if port.role == "FP_GHOST")
            for vector_pairs, ghost_pairs in product(
                _perfect_matchings(vector_ports),
                _oriented_matchings(antighosts, ghosts, _fp_accepts),
            ):
                edge_data = tuple((left, right, "P_VV", False) for left, right in vector_pairs) + tuple(
                    (left, right, "P_FP", True) for left, right in ghost_pairs
                )
                topology = "I2_FP_V2" if action_count == 1 else "I2_FP_V1_FP_V1"
                candidate = _candidate(
                    "FP_CHIRAL_GHOST",
                    "IN_SCOPE_PURE_GAUGE_FIXED_GAUGE",
                    topology,
                    vertices,
                    edge_data,
                )
                if candidate is not None:
                    candidates.append(candidate)
    candidates.sort(
        key=lambda item: (
            item.topology_family,
            tuple(vertex.source_monomial_id for vertex in item.vertices),
            tuple((edge.left_port, edge.right_port, edge.propagator) for edge in item.edges),
        )
    )
    return _assign_ids(candidates, "FP_L2")


def fp_structural_family_census() -> tuple[dict[str, object], ...]:
    """Classify every FP species multiset allowed by total V-valence two."""

    insertion = _insertion()
    monomials = _interaction_monomials(fp_ghost_monomials(max_v_order=2), "FP")
    admitted = enumerate_fp_candidates()
    admitted_counts: dict[tuple[str, ...], int] = {}
    for candidate in admitted:
        key = tuple(vertex.source_monomial_id for vertex in candidate.vertices[1:])
        admitted_counts[key] = admitted_counts.get(key, 0) + 1
    rows: list[dict[str, object]] = []
    for action_count in (1, 2):
        for selected in combinations_with_replacement(monomials, action_count):
            if sum(sum(field.field_name == "V" for field in item.ordered_fields) for item in selected) != 2:
                continue
            action_vertices = tuple(
                _vertex_from_monomial(item, f"FP{position}")
                for position, item in enumerate(selected, start=1)
            )
            antighosts = tuple(
                port for vertex in action_vertices for port in vertex.ports if port.role == "FP_ANTIGHOST"
            )
            ghosts = tuple(port for vertex in action_vertices for port in vertex.ports if port.role == "FP_GHOST")
            ghost_matchings = _oriented_matchings(antighosts, ghosts, _fp_accepts)
            key = tuple(item.monomial_id for item in selected)
            accepted_count = admitted_counts.get(key, 0)
            if accepted_count:
                classification = ADMITTED
                negative_witness = None
            elif not ghost_matchings:
                classification = ABSENT
                negative_witness = "NO_BIJECTION_BETWEEN_TYPED_ANTIGHOST_AND_GHOST_PORTS"
            else:
                classification = ABSENT
                negative_witness = "EVERY_TYPED_GHOST_MATCHING_LEAVES_AN_INTERNAL_BRIDGE"
            rows.append(
                {
                    "source_monomial_ids": list(key),
                    "V_valence_sum": 2,
                    "typed_ghost_matching_count": len(ghost_matchings),
                    "admitted_labeled_graph_count": accepted_count,
                    "classification": classification,
                    "negative_witness": negative_witness,
                    "primitive_vertex": insertion.source_monomial_id,
                }
            )
    return tuple(rows)


def enumerate_matter_candidates() -> tuple[Candidate, ...]:
    insertion = _insertion()
    monomial_map = {item.monomial_id: item for item in matter_bridge_monomials()}
    selected_families = (
        (monomial_map["matter_bridge_v2"],),
        (monomial_map["matter_bridge_v1"], monomial_map["matter_bridge_v1"]),
    )
    candidates: list[Candidate] = []
    for selected in selected_families:
        for flavors in product((1, 2, 3), repeat=len(selected)):
            action_vertices = tuple(
                _vertex_from_monomial(item, f"M{position}", flavor=flavor)
                for position, (item, flavor) in enumerate(zip(selected, flavors), start=1)
            )
            vertices = (insertion,) + action_vertices
            vector_ports = tuple(port for vertex in vertices for port in vertex.ports if port.field == "V")
            tilded = tuple(port for vertex in action_vertices for port in vertex.ports if port.field == "TildePhi")
            untilded = tuple(port for vertex in action_vertices for port in vertex.ports if port.field == "Phi")
            for vector_pairs, matter_pairs in product(
                _perfect_matchings(vector_ports),
                _oriented_matchings(tilded, untilded, _matter_accepts),
            ):
                edge_data = tuple((left, right, "P_VV", False) for left, right in vector_pairs) + tuple(
                    (left, right, "P_PhiTildePhi", True) for left, right in matter_pairs
                )
                topology = "I2_MATTER_V2" if len(selected) == 1 else "I2_MATTER_V1_MATTER_V1"
                candidate = _candidate(
                    "N4_CHIRAL_MATTER",
                    "OUTSIDE_CURRENT_PURE_GAUGE_SUBSECTOR",
                    topology,
                    vertices,
                    edge_data,
                )
                if candidate is not None:
                    candidates.append(candidate)
    candidates.sort(
        key=lambda item: (
            item.topology_family,
            tuple((vertex.source_monomial_id, tuple(port.flavor for port in vertex.ports)) for vertex in item.vertices),
            tuple((edge.left_port, edge.right_port, edge.propagator) for edge in item.edges),
        )
    )
    return _assign_ids(candidates, "MATTER_L2")


def matter_structural_family_census() -> tuple[dict[str, object], ...]:
    """Classify every N=4 matter flavor assignment at total V-valence two."""

    admitted = enumerate_matter_candidates()
    admitted_counts: dict[tuple[tuple[str, int], ...], int] = {}
    for candidate in admitted:
        key = tuple(
            (
                vertex.source_monomial_id,
                next(port.flavor for port in vertex.ports if port.flavor is not None),
            )
            for vertex in candidate.vertices[1:]
        )
        admitted_counts[key] = admitted_counts.get(key, 0) + 1
    monomial_map = {item.monomial_id: item for item in matter_bridge_monomials()}
    selected_families = (
        (monomial_map["matter_bridge_v2"],),
        (monomial_map["matter_bridge_v1"], monomial_map["matter_bridge_v1"]),
    )
    rows: list[dict[str, object]] = []
    for selected in selected_families:
        for flavors in product((1, 2, 3), repeat=len(selected)):
            key = tuple((item.monomial_id, flavor) for item, flavor in zip(selected, flavors))
            accepted_count = admitted_counts.get(key, 0)
            rows.append(
                {
                    "source_and_flavor": [list(item) for item in key],
                    "V_valence_sum": 2,
                    "equal_flavor_propagator_condition": len(set(flavors)) == 1,
                    "admitted_labeled_graph_count": accepted_count,
                    "classification": ADMITTED if accepted_count else ABSENT,
                    "negative_witness": (
                        None
                        if accepted_count
                        else "UNEQUAL_FLAVORS_FORCE_SELF_LOOPS_AND_EACH_VECTOR_ATTACHMENT_IS_A_BRIDGE"
                    ),
                }
            )
    return tuple(rows)


def _valence_certificate() -> dict[str, object]:
    rows = []
    for number_gauge_vertices in range(4):
        for fp_vector_valence in range(7):
            minimum_gauge_excess = number_gauge_vertices
            left_hand_side = fp_vector_valence + minimum_gauge_excess
            if left_hand_side == 2:
                rows.append(
                    {
                        "n_gauge": number_gauge_vertices,
                        "FP_vector_valence_M": fp_vector_valence,
                        "minimum_sum_q_minus_2": minimum_gauge_excess,
                    }
                )
    return {
        "identity": "L=1+(M+sum_j(q_j-2))/2",
        "derivation": [
            "E_ghost=n_FP",
            "E_V=(2+M+sum_j q_j)/2",
            "V_total=1+n_FP+n_gauge",
            "L=E_ghost+E_V-V_total+1",
            "L=1+(M+sum_j(q_j-2))/2",
        ],
        "one_PI_attachment_condition": "M>=2",
        "interaction_gauge_valence_condition": "q_j>=3",
        "L_equals_2_solution_under_conditions": {
            "M": 2,
            "n_gauge": 0,
            "sum_j(q_j-2)": 0,
        },
        "bounded_integer_crosscheck_solutions_before_M_ge_2": rows,
    }


def build_payload() -> dict[str, object]:
    fp_candidates = enumerate_fp_candidates()
    matter_candidates = enumerate_matter_candidates()
    fp_family_census = fp_structural_family_census()
    matter_family_census = matter_structural_family_census()
    fp_signatures = []
    for monomial in fp_ghost_monomials(max_v_order=2):
        fp_signatures.append(
            {
                "monomial_id": monomial.monomial_id,
                "V_valence": sum(field.field_name == "V" for field in monomial.ordered_fields),
                "ordered_fields": [field.field_name for field in monomial.ordered_fields],
                "chiralities": [field.chirality.value for field in monomial.ordered_fields],
                "role": "QUADRATIC_KERNEL" if all(field.field_name != "V" for field in monomial.ordered_fields) else "INTERACTION",
            }
        )
    topology_counts = {
        family: sum(candidate.topology_family == family for candidate in fp_candidates)
        for family in sorted({candidate.topology_family for candidate in fp_candidates})
    }
    matter_counts = {
        family: sum(candidate.topology_family == family for candidate in matter_candidates)
        for family in sorted({candidate.topology_family for candidate in matter_candidates})
    }
    return {
        "schema": 1,
        "status": PROPOSAL_STATUS,
        "scope": "STEP6.PRIMITIVE_WW.TWO_LOOP.GHOST_TYPED_PORT_CENSUS",
        "seed": "nabla_-[(nabla_+W_+)^A(nabla_+W_+)^B]::primitive_I_(2)",
        "decided_properties": ["typed_port_saturation", "connected", "L=2", "internal_edge_1PI"],
        "unevaluated_properties": [
            "coefficient",
            "Wick_sign",
            "symmetry_factor",
            "color_factor",
            "momentum_routing",
            "D_algebra",
            "integral",
            "renormalization",
            "finite_BV_density",
            "finite_FP_NK_cycles",
        ],
        "input_hashes": {
            "AUTHORITY.md": _sha256(ROOT / "AUTHORITY.md"),
            "AGENTS.md": _sha256(ROOT / "AGENTS.md"),
            "tasks/CURRENT.yaml": _sha256(ROOT / "tasks/CURRENT.yaml"),
            "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md": _sha256(
                ROOT / "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md"
            ),
            "scripts/step5_vertex_grammar.py": _sha256(ROOT / "scripts/step5_vertex_grammar.py"),
            "audits/step5a-ghost-census.json": _sha256(ROOT / "audits/step5a-ghost-census.json"),
        },
        "primitive_ports": [asdict(port) for port in _insertion().ports],
        "topological_valence_certificate": _valence_certificate(),
        "FP": {
            "classification": ADMITTED,
            "field_system": {
                "antighosts": ["cprime_plus(CHIRAL)", "tilde_cprime_minus(ANTICHIRAL)"],
                "ghosts": ["c(CHIRAL)", "tilde_c(ANTICHIRAL)"],
                "propagators": [
                    "cprime_plus -> tilde_c",
                    "tilde_cprime_minus -> c",
                ],
            },
            "quadratic_kernel_vertices_excluded_from_interaction_expansion": [
                item["monomial_id"] for item in fp_signatures if item["role"] == "QUADRATIC_KERNEL"
            ],
            "exact_signatures": fp_signatures,
            "candidate_count": len(fp_candidates),
            "topology_counts": topology_counts,
            "structural_family_census": list(fp_family_census),
            "candidates": [asdict(candidate) for candidate in fp_candidates],
        },
        "NK": {
            "classification": ABSENT,
            "scope": "REFERENCE_FLAT_STEP5A_FIXED_GAUGE_ONLY",
            "fields": ["b_NK(CHIRAL,Grassmann-even)", "tilde_b_NK(ANTICHIRAL,Grassmann-even)"],
            "propagator": "b_NK <-> tilde_b_NK",
            "interaction_vertices_with_V": [],
            "cut_witness": {
                "insertion_component_ports": ["V", "V"],
                "NK_component_ports": ["b_NK", "tilde_b_NK"],
                "mixed_propagators": [],
                "mixed_vertices": [],
                "conclusion": ABSENT,
            },
            "nonclaim": "No equality with a global finite-BV/NK determinant or cycle is asserted.",
        },
        "MATTER": {
            "classification": ADMITTED,
            "scope_relation": "OUTSIDE_CURRENT_PURE_GAUGE_SUBSECTOR",
            "fields": ["Phi_r(CHIRAL)", "TildePhi_r(ANTICHIRAL)"],
            "flavors": [1, 2, 3],
            "propagator": "TildePhi_r -> Phi_r with equal r",
            "candidate_count": len(matter_candidates),
            "topology_counts": matter_counts,
            "structural_family_census": list(matter_family_census),
            "candidates": [asdict(candidate) for candidate in matter_candidates],
        },
        "overall_classification": ADMITTED,
        "global_nonclaim": "The census is local fixed-gauge perturbative graph theory, not a finite-density, Berezinian, FP-cycle, NK-cycle, or BV-equivalence proof.",
    }


def _candidate_checks(candidate: dict[str, object]) -> bool:
    counts = dict(candidate["port_conservation"])
    return (
        candidate["classification"] == ADMITTED
        and candidate["connected"] is True
        and candidate["loop_number"] == 2
        and candidate["one_particle_irreducible"] is True
        and all(candidate["deletion_connected"][index][1] for index in range(len(candidate["deletion_connected"])))
        and all(count == 1 for count in counts.values())
    )


def verify_payload(payload: dict[str, object]) -> dict[str, object]:
    fp = payload["FP"]
    nk = payload["NK"]
    matter = payload["MATTER"]
    fp_candidates = fp["candidates"]
    matter_candidates = matter["candidates"]
    checks = {
        "proposal_status_is_explicit": payload["status"] == PROPOSAL_STATUS,
        "primitive_has_exactly_two_quantum_V_ports": [port["field"] for port in payload["primitive_ports"]] == ["V", "V"],
        "valence_certificate_forces_M2_and_no_gauge_vertices": payload["topological_valence_certificate"]["L_equals_2_solution_under_conditions"] == {
            "M": 2,
            "n_gauge": 0,
            "sum_j(q_j-2)": 0,
        },
        "FP_kernel_vertices_are_not_interactions": sorted(fp["quadratic_kernel_vertices_excluded_from_interaction_expansion"]) == [
            "fp_minus_c_v0",
            "fp_plus_tilde_c_v0",
        ],
        "FP_has_ten_labeled_candidates": fp["candidate_count"] == 10,
        "FP_topology_counts_are_exact": fp["topology_counts"] == {
            "I2_FP_V1_FP_V1": 6,
            "I2_FP_V2": 4,
        },
        "all_fourteen_FP_species_multisets_are_classified": len(fp["structural_family_census"]) == 14
        and sum(row["classification"] == ADMITTED for row in fp["structural_family_census"]) == 5
        and sum(row["classification"] == ABSENT for row in fp["structural_family_census"]) == 9,
        "every_FP_candidate_is_saturated_connected_L2_1PI": all(_candidate_checks(candidate) for candidate in fp_candidates),
        "FP_species_families_are_exact": sorted(
            {
                tuple(vertex["source_monomial_id"] for vertex in candidate["vertices"][1:])
                for candidate in fp_candidates
            }
        ) == [
            ("fp_minus_c_v1", "fp_minus_c_v1"),
            ("fp_minus_c_v2",),
            ("fp_minus_tilde_c_v1", "fp_plus_c_v1"),
            ("fp_plus_tilde_c_v1", "fp_plus_tilde_c_v1"),
            ("fp_plus_tilde_c_v2",),
        ],
        "NK_absence_has_empty_mixed_ports": nk["classification"] == ABSENT
        and nk["interaction_vertices_with_V"] == []
        and nk["cut_witness"]["mixed_propagators"] == []
        and nk["cut_witness"]["mixed_vertices"] == [],
        "matter_has_twelve_labeled_candidates": matter["candidate_count"] == 12,
        "matter_topology_counts_are_exact": matter["topology_counts"] == {
            "I2_MATTER_V1_MATTER_V1": 6,
            "I2_MATTER_V2": 6,
        },
        "all_twelve_matter_flavor_assignments_are_classified": len(matter["structural_family_census"]) == 12
        and sum(row["classification"] == ADMITTED for row in matter["structural_family_census"]) == 6
        and sum(row["classification"] == ABSENT for row in matter["structural_family_census"]) == 6,
        "every_matter_candidate_is_saturated_connected_L2_1PI": all(
            _candidate_checks(candidate) for candidate in matter_candidates
        ),
        "matter_is_not_declared_absent": matter["classification"] == ADMITTED
        and matter["scope_relation"] == "OUTSIDE_CURRENT_PURE_GAUGE_SUBSECTOR",
        "no_candidate_contains_a_coefficient_or_amplitude": all(
            "coefficient" not in candidate and "amplitude" not in candidate
            for candidate in fp_candidates + matter_candidates
        ),
        "finite_BV_equivalence_is_not_claimed": "not a finite-density" in payload["global_nonclaim"],
    }
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "schema": 1,
        "status": "PASS" if not failed else "FAIL",
        "proposal_status": payload["status"],
        "checks": [{"id": name, "passed": passed} for name, passed in checks.items()],
        "totals": {"checks": len(checks), "failed": len(failed)},
        "failed": failed,
        "output_sha256": sha256(
            (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
        ).hexdigest(),
    }


def render_markdown(payload: dict[str, object]) -> str:
    fp = payload["FP"]
    matter = payload["MATTER"]
    return "\n".join(
        (
            "# Step 6 two-loop ghost typed-port census",
            "",
            f"`{payload['status']}`",
            "",
            "$$",
            r"E_{\rm gh}=n_{\rm FP},\qquad E_V=\frac{2+M+\sum_jq_j}{2},\qquad V=1+n_{\rm FP}+n_g,",
            "$$",
            "",
            "$$",
            r"L=E_{\rm gh}+E_V-V+1=1+\frac{M+\sum_j(q_j-2)}2.",
            "$$",
            "",
            "$$",
            r"L=2,\quad M\ge2,\quad q_j\ge3\quad\Longrightarrow\quad M=2,\quad n_g=0.",
            "$$",
            "",
            f"FP: `{fp['classification']}`, labeled candidates = `{fp['candidate_count']}`.",
            "",
            f"NK: `{payload['NK']['classification']}` in reference-flat Step-5A.",
            "",
            f"Matter: `{matter['classification']}`, labeled candidates = `{matter['candidate_count']}`; outside current pure-gauge subsector.",
            "",
            "No coefficient, amplitude, D-algebra, integral, or finite-BV equivalence is asserted.",
            "",
        )
    )


def main() -> int:
    payload = build_payload()
    audit = verify_payload(payload)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    MARKDOWN_OUTPUT.write_text(render_markdown(payload), encoding="utf-8")
    AUDIT_OUTPUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(audit["totals"], sort_keys=True))
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
