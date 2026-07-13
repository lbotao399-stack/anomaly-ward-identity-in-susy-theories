#!/usr/bin/env python3
"""Executable internal census for the full Step-5 one-loop topology gate.

This module proves only finite graph combinatorics and typed-port existence
criteria.  It does not evaluate a supergraph, pole, counterterm, or anomaly
coefficient, and it imports no external target result.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
from itertools import product
import json
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/full-n4-topology-census.json"
AUDIT = ROOT / "audits/step5-full-n4-topology-census-verification.json"

SOURCE_PATHS = (
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md",
    "audits/step5-one-loop-covariant-completion-final-audit.md",
    "scripts/step5_graph_ir.py",
)


@dataclass(frozen=True)
class TopologySolution:
    topology_id: str
    insertion_valence: int
    action_valences: tuple[int, ...]
    action_vertex_count: int
    total_vertex_count: int
    internal_edge_count: int
    external_leg_count: int
    defect_sum: int
    loop_number: int


@dataclass(frozen=True)
class Port:
    port_id: str
    vertex_id: str
    field: str
    flavor: int | None = None

    def __post_init__(self) -> None:
        if not self.port_id or not self.vertex_id or not self.field:
            raise ValueError("each quantum port needs an id, vertex, and field")


@dataclass(frozen=True)
class MatchEdge:
    left_port: str
    right_port: str
    propagator_rule: str


@dataclass(frozen=True)
class LetterFamily:
    family: str
    component_multiplicity: int
    parity: int
    differential_nonzero: bool


LETTER_FAMILIES = (
    LetterFamily("X", 1, 0, True),
    LetterFamily("Y", 3, 1, True),
    LetterFamily("Z", 3, 0, False),
    LetterFamily("T", 2, 1, False),
)

FAMILY_BY_NAME = {family.family: family for family in LETTER_FAMILIES}


def topology_name(insertion_valence: int, action_valences: Sequence[int]) -> str:
    return f"I{insertion_valence}" + "".join(
        f"S{valence}" for valence in action_valences
    )


def enumerate_two_external_one_loop_topologies() -> tuple[TopologySolution, ...]:
    """Solve the valence equation without assuming the four output names.

    Let ``N`` be the number of genuine action vertices.  Since each action
    valence is at least three, each action defect ``n_a-2`` is at least one.
    The total defect is two, hence ``N<=2``, ``2<=n_I<=4``, and
    ``3<=n_a<=4``.  These derived bounds make the enumeration exhaustive.
    """

    rows: list[TopologySolution] = []
    external_legs = 2
    for action_count in range(3):
        for insertion_valence in range(2, 5):
            for action_valences in product((3, 4), repeat=action_count):
                defect = (insertion_valence - 2) + sum(
                    valence - 2 for valence in action_valences
                )
                if defect != 2:
                    continue
                total_vertices = action_count + 1
                internal_edges = action_count + 1
                total_half_edges = insertion_valence + sum(action_valences)
                if total_half_edges != 2 * internal_edges + external_legs:
                    raise AssertionError("half-edge and defect equations disagree")
                loop_number = internal_edges - total_vertices + 1
                rows.append(
                    TopologySolution(
                        topology_name(insertion_valence, action_valences),
                        insertion_valence,
                        tuple(action_valences),
                        action_count,
                        total_vertices,
                        internal_edges,
                        external_legs,
                        defect,
                        loop_number,
                    )
                )
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                -row.action_vertex_count,
                row.action_valences,
                -row.insertion_valence,
            ),
        )
    )


def propagator_rule(left: Port, right: Port) -> str | None:
    """Return the exact free typed propagator signature, or ``None``."""

    if left.field == right.field == "V":
        return "P_VV"
    if {left.field, right.field} == {"Phi", "TildePhi"}:
        if left.flavor is not None and left.flavor == right.flavor:
            return "P_Phi_TildePhi_delta_rs"
        return None
    fp_pairs = {
        frozenset(("cprime_plus", "tilde_c")),
        frozenset(("tilde_cprime_minus", "c")),
    }
    if frozenset((left.field, right.field)) in fp_pairs:
        return "P_FP_oriented_pair"
    if {left.field, right.field} == {"b_NK", "tilde_b_NK"}:
        return "P_NK"
    return None


def enumerate_perfect_matchings(
    ports: Iterable[Port],
) -> tuple[tuple[MatchEdge, ...], ...]:
    """Enumerate every typed perfect matching of the quantum ports."""

    ordered = tuple(sorted(ports, key=lambda port: port.port_id))
    if len({port.port_id for port in ordered}) != len(ordered):
        raise ValueError("quantum port ids must be unique")
    if len(ordered) % 2:
        return ()
    if not ordered:
        return ((),)

    first = ordered[0]
    rows: list[tuple[MatchEdge, ...]] = []
    for position, other in enumerate(ordered[1:], start=1):
        rule = propagator_rule(first, other)
        if rule is None:
            continue
        remainder = ordered[1:position] + ordered[position + 1 :]
        for tail in enumerate_perfect_matchings(remainder):
            rows.append((MatchEdge(first.port_id, other.port_id, rule), *tail))
    return tuple(rows)


def matching_graph_certificate(
    ports: Sequence[Port], matching: Sequence[MatchEdge]
) -> dict[str, object]:
    """Check saturation, connectedness, and first Betti number."""

    by_id = {port.port_id: port for port in ports}
    if len(by_id) != len(ports):
        raise ValueError("quantum port ids must be unique")
    used = [
        port_id for edge in matching for port_id in (edge.left_port, edge.right_port)
    ]
    saturated = len(used) == len(ports) and len(set(used)) == len(ports)
    typed = all(
        edge.left_port in by_id
        and edge.right_port in by_id
        and propagator_rule(by_id[edge.left_port], by_id[edge.right_port])
        == edge.propagator_rule
        for edge in matching
    )

    vertices = sorted({port.vertex_id for port in ports})
    adjacency = {vertex: set() for vertex in vertices}
    for edge in matching:
        left_vertex = by_id[edge.left_port].vertex_id
        right_vertex = by_id[edge.right_port].vertex_id
        adjacency[left_vertex].add(right_vertex)
        adjacency[right_vertex].add(left_vertex)

    seen: set[str] = set()
    if vertices:
        stack = [vertices[0]]
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            stack.extend(adjacency[vertex] - seen)
    connected = bool(vertices) and len(seen) == len(vertices)
    loop_number = len(matching) - len(vertices) + 1 if connected else None
    return {
        "quantum_ports_saturated_once": saturated,
        "every_edge_typed": typed,
        "connected": connected,
        "vertex_count": len(vertices),
        "edge_count": len(matching),
        "loop_number_E_minus_V_plus_1": loop_number,
        "is_connected_one_loop": saturated and typed and connected and loop_number == 1,
    }


def v_ports(vertex_id: str, count: int) -> tuple[Port, ...]:
    return tuple(Port(f"{vertex_id}.q{slot}", vertex_id, "V") for slot in range(count))


def topology_witness_ports(topology_id: str) -> tuple[Port, ...]:
    """Return one labeled all-vector witness for each abstract topology."""

    quantum_port_counts = {
        "I2S3S3": (("I2", 2), ("S3a", 2), ("S3b", 2)),
        "I3S3": (("I3", 2), ("S3", 2)),
        "I2S4": (("I2", 2), ("S4", 2)),
        "I4": (("I4", 2),),
    }
    return tuple(
        port
        for vertex_id, count in quantum_port_counts[topology_id]
        for port in v_ports(vertex_id, count)
    )


def topology_witnesses() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for topology in enumerate_two_external_one_loop_topologies():
        ports = topology_witness_ports(topology.topology_id)
        all_matchings = enumerate_perfect_matchings(ports)
        valid = [
            matching
            for matching in all_matchings
            if matching_graph_certificate(ports, matching)["is_connected_one_loop"]
        ]
        rows.append(
            {
                "topology_id": topology.topology_id,
                "quantum_ports": [asdict(port) for port in ports],
                "typed_perfect_matching_count": len(all_matchings),
                "connected_one_loop_matching_count": len(valid),
                "canonical_witness": [asdict(edge) for edge in valid[0]],
                "certificate": matching_graph_certificate(ports, valid[0]),
                "role": "ABSTRACT_EXISTENCE_WITNESS_NOT_A_PHYSICAL_SUPERGRAPH",
            }
        )
    return rows


def typed_matching_fixtures() -> list[dict[str, object]]:
    fixtures = (
        (
            "vector_pair",
            (Port("a", "u", "V"), Port("b", "v", "V")),
            True,
        ),
        (
            "matter_same_flavor",
            (Port("a", "u", "Phi", 2), Port("b", "v", "TildePhi", 2)),
            True,
        ),
        (
            "matter_wrong_flavor",
            (Port("a", "u", "Phi", 1), Port("b", "v", "TildePhi", 3)),
            False,
        ),
        (
            "mixed_vector_matter",
            (Port("a", "u", "V"), Port("b", "v", "Phi", 1)),
            False,
        ),
        (
            "fp_pair",
            (Port("a", "u", "cprime_plus"), Port("b", "v", "tilde_c")),
            True,
        ),
        (
            "nk_pair",
            (Port("a", "u", "b_NK"), Port("b", "v", "tilde_b_NK")),
            True,
        ),
        (
            "odd_vector_ports",
            (
                Port("a", "u", "V"),
                Port("b", "v", "V"),
                Port("c", "w", "V"),
            ),
            False,
        ),
    )
    return [
        {
            "fixture_id": fixture_id,
            "ports": [asdict(port) for port in ports],
            "matching_exists": bool(enumerate_perfect_matchings(ports)),
            "expected": expected,
        }
        for fixture_id, ports, expected in fixtures
    ]


def tree_terms(left: LetterFamily, right: LetterFamily) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    if left.differential_nonzero:
        rows.append({"sign": 1, "ordered_word": [f"d{left.family}", right.family]})
    if right.differential_nonzero:
        rows.append(
            {
                "sign": -1 if left.parity else 1,
                "ordered_word": [left.family, f"d{right.family}"],
            }
        )
    return rows


def channel_ledger() -> list[dict[str, object]]:
    topologies = [
        row.topology_id for row in enumerate_two_external_one_loop_topologies()
    ]
    rows: list[dict[str, object]] = []
    for left in LETTER_FAMILIES:
        for right in LETTER_FAMILIES:
            channel_id = f"{left.family}{right.family}"
            terms = tree_terms(left, right)
            if not terms:
                state = "PROVED_BARE_ZERO__RENORMALIZED_MIXING_OPEN"
                required: list[str] = []
            elif channel_id == "XX":
                state = "PARTIAL_PURE_VECTOR_I2S3S3_ONLY__NO_ACCEPTED_COEFFICIENT"
                required = topologies
            else:
                state = "OPEN_NO_PHYSICAL_GRAPHIR"
                required = topologies
            rows.append(
                {
                    "channel_id": channel_id,
                    "left_family": left.family,
                    "right_family": right.family,
                    "left_parity": left.parity,
                    "component_multiplicity": (
                        left.component_multiplicity * right.component_multiplicity
                    ),
                    "tree_terms": terms,
                    "bare_insertion_zero": not terms,
                    "required_two_external_one_loop_topologies": required,
                    "implementation_state": state,
                    "accepted_renormalized_result": False,
                }
            )
    return rows


def ww_missing_family_ledger() -> list[dict[str, object]]:
    return [
        {
            "family": "I2S3S3",
            "graph_role": "triangle",
            "state": "PARTIAL_PURE_VECTOR_DIRECT_AND_REFLECTED_ONLY",
        },
        {
            "family": "I3S3",
            "graph_role": "insertion-action bubble",
            "state": "OPEN_SHARED_SCOPE_DALGEBRA_AND_POLE",
            "labeled_candidate_count": 360,
        },
        {
            "family": "I2S4",
            "graph_role": "seagull bubble",
            "state": "OPEN_H2_PROJECTOR_DALGEBRA_AND_NORMALIZATION",
        },
        {
            "family": "I4",
            "graph_role": "insertion tadpole/contact",
            "state": "OPEN_180_LOCALITY_TO_POLYNOMIAL_PROOFS",
            "labeled_candidate_count": 180,
        },
        {
            "family": "DALGEBRA_COLLAPSED_CHILDREN",
            "graph_role": "propagator-cut descendants",
            "state": "OPEN_COEFFICIENT_TRANSPORT_AND_BASIS_BIJECTION",
            "binding_count": 48,
            "current_child_graphir_count": 6,
        },
        {
            "family": "CT2",
            "graph_role": "additive local source counterterm",
            "state": "OPEN_OPERATOR_MIXING_BASIS_AND_RENORMALIZATION_CONDITION",
        },
    ]


def source_hashes() -> dict[str, str]:
    return {
        path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        for path in SOURCE_PATHS
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    topologies = enumerate_two_external_one_loop_topologies()
    witnesses = topology_witnesses()
    matching_fixtures = typed_matching_fixtures()
    channels = channel_ledger()
    nonzero_channels = [row for row in channels if not row["bare_insertion_zero"]]
    bare_zero_channels = [row for row in channels if row["bare_insertion_zero"]]
    partial_channels = [
        row
        for row in channels
        if str(row["implementation_state"]).startswith("PARTIAL")
    ]
    ungenerated_channels = [
        row
        for row in channels
        if row["implementation_state"] == "OPEN_NO_PHYSICAL_GRAPHIR"
    ]
    checks = {
        "diophantine_solution_set_is_exact": [row.topology_id for row in topologies]
        == ["I2S3S3", "I3S3", "I2S4", "I4"],
        "every_solution_has_two_external_legs_and_one_loop": all(
            row.external_leg_count == 2 and row.loop_number == 1 for row in topologies
        ),
        "every_topology_has_a_typed_connected_one_loop_witness": all(
            row["connected_one_loop_matching_count"] > 0 for row in witnesses
        ),
        "typed_matching_fixtures_obey_expectations": all(
            row["matching_exists"] == row["expected"] for row in matching_fixtures
        ),
        "sixteen_ordered_family_channels": len(channels) == 16,
        "eighty_one_component_channels": sum(
            int(row["component_multiplicity"]) for row in channels
        )
        == 81,
        "twelve_bare_nonzero_families_with_fifty_six_components": (
            len(nonzero_channels) == 12
            and sum(int(row["component_multiplicity"]) for row in nonzero_channels)
            == 56
        ),
        "four_bare_zero_families_with_twenty_five_components": (
            {row["channel_id"] for row in bare_zero_channels}
            == {"ZZ", "ZT", "TZ", "TT"}
            and sum(int(row["component_multiplicity"]) for row in bare_zero_channels)
            == 25
        ),
        "one_partial_and_eleven_ungenerated_nonzero_families": (
            [row["channel_id"] for row in partial_channels] == ["XX"]
            and len(ungenerated_channels) == 11
        ),
        "no_channel_has_an_accepted_renormalized_result": not any(
            row["accepted_renormalized_result"] for row in channels
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "schema": "Step5FullN4OneLoopTopologyCensus.v1",
        "status": "PASS_INTERNAL_CENSUS__PHYSICAL_AMPLITUDES_FAIL_CLOSED"
        if not failed
        else "FAIL",
        "authority_status": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "scope": "INTERNAL_ONLY_TWO_EXTERNAL_ONE_LOOP_TOPOLOGY_AND_CHANNEL_CENSUS",
        "external_results_imported": False,
        "external_target_data_imported": False,
        "source_sha256": source_hashes(),
        "diophantine_derivation": {
            "half_edge_equation": "n_I+sum_a n_a=2E+2",
            "connected_one_loop_euler_equation": "1=E-(N+1)+1; E=N+1",
            "defect_equation": "(n_I-2)+sum_a(n_a-2)=2",
            "derived_bounds": "N<=2; 2<=n_I<=4; 3<=n_a<=4",
            "solutions": [asdict(row) for row in topologies],
        },
        "typed_perfect_matching_contract": {
            "quantum_port_rule": "every quantum port occurs in exactly one matched edge",
            "external_port_rule": "external background ports are excluded from the matching",
            "graph_rule": "matching graph is connected and b1=E-V+1=1",
            "absence_rule": "PROVED_ABSENT requires no valid matching over every legal insertion/action expansion",
            "zero_after_dalgebra_rule": "a matched graph killed later is GRAPH_EXISTS_AMPLITUDE_ZERO",
            "topology_witnesses": witnesses,
            "typed_fixtures": matching_fixtures,
        },
        "letter_dictionary": {
            "X": "nabla_+ W_+",
            "Y_r": "nabla_+ Phi_r",
            "Z_r": "TildePhi_r",
            "T_dot_a": "TildeW_dot_a",
        },
        "channel_ledger": channels,
        "ww_missing_families": ww_missing_family_ledger(),
        "full_n4_fluctuation_blocks": [
            "V",
            "(Phi_1,TildePhi_1)",
            "(Phi_2,TildePhi_2)",
            "(Phi_3,TildePhi_3)",
            "FP",
            "NK",
        ],
        "result_boundary": {
            "physical_graphir_complete": False,
            "complete_contact_pole_computed": False,
            "counterterm_fixed": False,
            "full_n4_one_loop_coefficient_accepted": False,
        },
        "checks": [{"id": name, "passed": passed} for name, passed in checks.items()],
        "totals": {
            "checks": len(checks),
            "failed": len(failed),
            "topology_solutions": len(topologies),
            "ordered_family_channels": len(channels),
            "component_channels": sum(
                int(row["component_multiplicity"]) for row in channels
            ),
            "partial_family_channels": len(partial_channels),
            "ungenerated_nonzero_family_channels": len(ungenerated_channels),
            "bare_zero_family_channels": len(bare_zero_channels),
            "accepted_family_channels": sum(
                bool(row["accepted_renormalized_result"]) for row in channels
            ),
        },
    }


def write_artifacts() -> dict[str, object]:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    audit = {
        "schema": "Step5FullN4OneLoopTopologyCensusAudit.v1",
        "status": payload["status"],
        "scope": payload["scope"],
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "checks": payload["checks"],
        "totals": payload["totals"],
        "external_results_imported": False,
    }
    AUDIT.write_bytes(canonical_json(audit))
    return payload


def main() -> int:
    payload = write_artifacts()
    print(json.dumps(payload["totals"], sort_keys=True))
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
