#!/usr/bin/env python3
"""Target-blind port census for every leading one-loop triangle parent.

The census uses only the linear source letters and the cubic vertices derived
from the locked action.  It does not inspect either the Project result ledger
or the holomorphic-twist target.  A row is a directed Wick route: the left
source port attaches to the first action vertex, the right source port attaches
to the second, one compatible bridge joins the two action vertices, and the
two unused ports are retained as ordered external fields.

There are two incidence families.  ``SPLIT_SOURCE_SINGLE_BRIDGE`` is the
legacy family in which each source letter attaches to a different cubic and
the cubics share one bridge.  ``SPECTATOR_SOURCE_DOUBLE_BRIDGE`` leaves one
source letter external, attaches the other source letter to the first cubic,
and joins the two cubics by two compatible bridges.  Both have E=3, V=3,
L=1.  No coefficient is inferred from this structural census.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "audits/step5-all-triangle-parent-port-census.json"
DEFAULT_AUDIT = ROOT / "audits/step5-all-triangle-parent-port-census.md"


LETTERS = (
    "A",
    "B1",
    "B2",
    "B3",
    "C1",
    "C2",
    "C3",
    "Ddot1",
    "Ddot2",
)
PARITY = {
    "A": 0,
    "B1": 1,
    "B2": 1,
    "B3": 1,
    "C1": 0,
    "C2": 0,
    "C3": 0,
    "Ddot1": 1,
    "Ddot2": 1,
}
ACTIVE_DESCENDANT = frozenset(("A", "B1", "B2", "B3"))


SOURCE_PORT = {
    "A": "u",
    "B1": "phi1",
    "B2": "phi2",
    "B3": "phi3",
    "C1": "tildephi1",
    "C2": "tildephi2",
    "C3": "tildephi3",
    "Ddot1": "u",
    "Ddot2": "u",
}


# Gauge ports are position-labeled because their six assignments and two
# derivative placements are distinct D-words before the action sum.
VERTICES = {
    "G": ("u[g0]", "u[g1]", "u[g2]"),
    "M1": ("tildephi1", "u", "phi1"),
    "M2": ("tildephi2", "u", "phi2"),
    "M3": ("tildephi3", "u", "phi3"),
    "Hplus": ("phi1", "phi2", "phi3"),
    "Hminus": ("tildephi1", "tildephi2", "tildephi3"),
}


def bare_field(port: str) -> str:
    return "u" if port.startswith("u") else port


def dual(field: str) -> str:
    field = bare_field(field)
    if field == "u":
        return "u"
    if field.startswith("phi"):
        return "tilde" + field
    if field.startswith("tildephi"):
        return field.removeprefix("tilde")
    raise ValueError(field)


def compatible(left: str, right: str) -> bool:
    return dual(left) == bare_field(right)


def topology(left_vertex: str, right_vertex: str) -> str:
    families = {left_vertex[0], right_vertex[0]}
    if left_vertex == right_vertex == "G":
        return "TGG"
    if families == {"G", "M"}:
        return "TGM"
    if left_vertex.startswith("M") and right_vertex.startswith("M"):
        return "TMM"
    if (
        left_vertex.startswith("M")
        and right_vertex.startswith("H")
    ) or (
        left_vertex.startswith("H")
        and right_vertex.startswith("M")
    ):
        return "TMH"
    if left_vertex.startswith("H") and right_vertex.startswith("H"):
        return "THH"
    raise AssertionError((left_vertex, right_vertex))


def marked_sides(left: str, right: str) -> tuple[tuple[str, str, int], ...]:
    rows: list[tuple[str, str, int]] = []
    if left in ACTIVE_DESCENDANT:
        rows.append(("L", left, 1))
    if right in ACTIVE_DESCENDANT:
        rows.append(("R", right, -1 if PARITY[left] else 1))
    return tuple(rows)


@dataclass(frozen=True)
class Route:
    route_id: str
    pair_id: str
    left_letter: str
    right_letter: str
    left_source_field: str
    right_source_field: str
    left_vertex: str
    right_vertex: str
    left_source_port: str
    right_source_port: str
    bridge_left_port: str
    bridge_right_port: str
    external_left_field: str
    external_right_field: str
    topology: str
    expansion_factor: str
    marked_occurrences: tuple[tuple[str, str, int], ...]
    coefficient_status: str


@dataclass(frozen=True)
class SpectatorRoute:
    route_id: str
    pair_id: str
    parent_family: str
    left_letter: str
    right_letter: str
    spectator_source_side: str
    spectator_source_letter: str
    spectator_external_field: str
    quantum_source_side: str
    quantum_source_letter: str
    quantum_source_field: str
    source_action_vertex: str
    loop_action_vertex: str
    source_action_port: str
    bridge_1_source_action_port: str
    bridge_1_loop_action_port: str
    bridge_2_source_action_port: str
    bridge_2_loop_action_port: str
    external_output_field: str
    topology: str
    internal_edge_count: int
    vertex_count: int
    loop_count: int
    connected: bool
    one_particle_irreducible: bool
    graph_classification: str
    source_action_edge_is_cut_edge: bool
    loop_cycle_edges: tuple[str, str]
    expansion_factor: str
    marked_occurrences: tuple[tuple[str, str, int], ...]
    quantum_marked_occurrences: tuple[tuple[str, str, int], ...]
    spectator_marked_occurrences: tuple[tuple[str, str, int], ...]
    coefficient_status: str


def enumerate_routes(left: str, right: str) -> list[Route]:
    routes: list[Route] = []
    left_source = SOURCE_PORT[left]
    right_source = SOURCE_PORT[right]
    marks = marked_sides(left, right)
    if not marks:
        return routes

    local_ordinal = 0
    for left_vertex, left_ports in VERTICES.items():
        for right_vertex, right_ports in VERTICES.items():
            for left_source_index, left_port in enumerate(left_ports):
                if not compatible(left_source, left_port):
                    continue
                for right_source_index, right_port in enumerate(right_ports):
                    if not compatible(right_source, right_port):
                        continue
                    left_remaining = tuple(
                        index for index in range(3) if index != left_source_index
                    )
                    right_remaining = tuple(
                        index for index in range(3) if index != right_source_index
                    )
                    for bridge_left_index in left_remaining:
                        for bridge_right_index in right_remaining:
                            bridge_left = left_ports[bridge_left_index]
                            bridge_right = right_ports[bridge_right_index]
                            if not compatible(bridge_left, bridge_right):
                                continue
                            external_left_index = next(
                                index
                                for index in left_remaining
                                if index != bridge_left_index
                            )
                            external_right_index = next(
                                index
                                for index in right_remaining
                                if index != bridge_right_index
                            )
                            local_ordinal += 1
                            route_id = (
                                f"TRI::{left}__{right}::{local_ordinal:03d}::"
                                f"{left_vertex}[{left_source_index},{bridge_left_index}]::"
                                f"{right_vertex}[{right_source_index},{bridge_right_index}]"
                            )
                            routes.append(
                                Route(
                                    route_id=route_id,
                                    pair_id=f"{left}__{right}",
                                    left_letter=left,
                                    right_letter=right,
                                    left_source_field=left_source,
                                    right_source_field=right_source,
                                    left_vertex=left_vertex,
                                    right_vertex=right_vertex,
                                    left_source_port=left_port,
                                    right_source_port=right_port,
                                    bridge_left_port=bridge_left,
                                    bridge_right_port=bridge_right,
                                    external_left_field=bare_field(
                                        left_ports[external_left_index]
                                    ),
                                    external_right_field=bare_field(
                                        right_ports[external_right_index]
                                    ),
                                    topology=topology(left_vertex, right_vertex),
                                    expansion_factor="(1/2!)*(two action orderings)=1",
                                    marked_occurrences=marks,
                                    coefficient_status=(
                                        "PENDING_EDGE_TAGGED_D_ALGEBRA_AND_SD_ORBIT"
                                    ),
                                )
                            )
    return routes


def enumerate_spectator_routes(left: str, right: str) -> list[SpectatorRoute]:
    """Enumerate the omitted one-external-source/two-bridge family."""

    marks = marked_sides(left, right)
    if not marks:
        return []
    routes: list[SpectatorRoute] = []
    local_ordinal = 0
    for spectator_side in ("L", "R"):
        if spectator_side == "L":
            spectator_letter, quantum_letter = left, right
            quantum_side = "R"
        else:
            spectator_letter, quantum_letter = right, left
            quantum_side = "L"
        quantum_field = SOURCE_PORT[quantum_letter]
        quantum_marks = tuple(row for row in marks if row[0] == quantum_side)
        spectator_marks = tuple(row for row in marks if row[0] == spectator_side)
        for source_vertex, source_ports in VERTICES.items():
            for source_index, source_port in enumerate(source_ports):
                if not compatible(quantum_field, source_port):
                    continue
                source_bridges = tuple(
                    index for index in range(3) if index != source_index
                )
                for loop_vertex, loop_ports in VERTICES.items():
                    for loop_bridge_1 in range(3):
                        for loop_bridge_2 in range(3):
                            if loop_bridge_1 == loop_bridge_2:
                                continue
                            if not compatible(
                                source_ports[source_bridges[0]],
                                loop_ports[loop_bridge_1],
                            ):
                                continue
                            if not compatible(
                                source_ports[source_bridges[1]],
                                loop_ports[loop_bridge_2],
                            ):
                                continue
                            external_index = next(
                                index
                                for index in range(3)
                                if index not in (loop_bridge_1, loop_bridge_2)
                            )
                            local_ordinal += 1
                            route_id = (
                                f"TRI-SPEC::{left}__{right}::{local_ordinal:03d}::"
                                f"SPEC-{spectator_side}::"
                                f"{source_vertex}[{source_index};"
                                f"{source_bridges[0]},{source_bridges[1]}]::"
                                f"{loop_vertex}[{loop_bridge_1},{loop_bridge_2};"
                                f"{external_index}]"
                            )
                            routes.append(
                                SpectatorRoute(
                                    route_id=route_id,
                                    pair_id=f"{left}__{right}",
                                    parent_family="SPECTATOR_SOURCE_DOUBLE_BRIDGE",
                                    left_letter=left,
                                    right_letter=right,
                                    spectator_source_side=spectator_side,
                                    spectator_source_letter=spectator_letter,
                                    spectator_external_field=SOURCE_PORT[spectator_letter],
                                    quantum_source_side=quantum_side,
                                    quantum_source_letter=quantum_letter,
                                    quantum_source_field=quantum_field,
                                    source_action_vertex=source_vertex,
                                    loop_action_vertex=loop_vertex,
                                    source_action_port=source_port,
                                    bridge_1_source_action_port=source_ports[source_bridges[0]],
                                    bridge_1_loop_action_port=loop_ports[loop_bridge_1],
                                    bridge_2_source_action_port=source_ports[source_bridges[1]],
                                    bridge_2_loop_action_port=loop_ports[loop_bridge_2],
                                    external_output_field=bare_field(loop_ports[external_index]),
                                    topology=topology(source_vertex, loop_vertex),
                                    internal_edge_count=3,
                                    vertex_count=3,
                                    loop_count=1,
                                    connected=True,
                                    one_particle_irreducible=False,
                                    graph_classification=(
                                        "CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY"
                                    ),
                                    source_action_edge_is_cut_edge=True,
                                    loop_cycle_edges=("bridge_1", "bridge_2"),
                                    expansion_factor="(1/2!)*(two action orderings)=1",
                                    marked_occurrences=marks,
                                    quantum_marked_occurrences=quantum_marks,
                                    spectator_marked_occurrences=spectator_marks,
                                    coefficient_status=(
                                        "PENDING_EDGE_TAGGED_D_ALGEBRA_AND_SD_ORBIT"
                                    ),
                                )
                            )
    return routes


def build_payload() -> dict[str, object]:
    routes: list[Route] = []
    spectator_routes: list[SpectatorRoute] = []
    pairs: list[dict[str, object]] = []
    for left in LETTERS:
        for right in LETTERS:
            pair_routes = enumerate_routes(left, right)
            pair_spectator_routes = enumerate_spectator_routes(left, right)
            marks = marked_sides(left, right)
            routes.extend(pair_routes)
            spectator_routes.extend(pair_spectator_routes)
            pairs.append(
                {
                    "pair_id": f"{left}__{right}",
                    "left": left,
                    "right": right,
                    "marked_occurrences_per_route": [
                        {"side": side, "letter": letter, "koszul_sign": sign}
                        for side, letter, sign in marks
                    ],
                    "split_source_single_bridge_route_count": len(pair_routes),
                    "spectator_source_double_bridge_route_count": len(pair_spectator_routes),
                    "triangle_parent_route_count": len(pair_routes) + len(pair_spectator_routes),
                    "status": (
                        "PENDING_EDGE_TAGGED_D_ALGEBRA_AND_SD_ORBIT"
                        if marks
                        else "EXACT_ZERO_NO_OUTER_DESCENDANT"
                    ),
                }
            )

    all_routes = [*routes, *spectator_routes]
    legacy_topology_counts = Counter(route.topology for route in routes)
    spectator_topology_counts = Counter(route.topology for route in spectator_routes)
    topology_counts = Counter(route.topology for route in all_routes)
    family_counts = Counter(
        f"{route.left_letter[0]}>{route.right_letter[0]}" for route in all_routes
    )
    external_counts = Counter(
        f"{route.external_left_field}>{route.external_right_field}"
        for route in routes
    )
    spectator_external_counts = Counter(
        f"{route.spectator_external_field}>{route.external_output_field}"
        for route in spectator_routes
    )
    legacy_marked_occurrence_count = sum(len(route.marked_occurrences) for route in routes)
    spectator_marked_occurrence_count = sum(
        len(route.marked_occurrences) for route in spectator_routes
    )
    spectator_quantum_marked_count = sum(
        len(route.quantum_marked_occurrences) for route in spectator_routes
    )
    spectator_external_marked_count = sum(
        len(route.spectator_marked_occurrences) for route in spectator_routes
    )
    return {
        "schema": "step5-all-triangle-parent-port-census-v2",
        "status": "STRUCTURAL_PARENT_CENSUS_ONLY__D_ALGEBRA_AND_SD_ORBITS_PENDING",
        "external_target_used": False,
        "source_order": "I0*S3*S3/(2*hbar^2)",
        "ordered_pair_count": len(pairs),
        "marked_pair_count": sum(bool(row["marked_occurrences_per_route"]) for row in pairs),
        "no_descendant_pair_count": sum(not row["marked_occurrences_per_route"] for row in pairs),
        "directed_parent_route_count": len(all_routes),
        "legacy_directed_parent_route_count": len(routes),
        "spectator_directed_parent_route_count": len(spectator_routes),
        "marked_inverse_edge_occurrence_count": (
            legacy_marked_occurrence_count + spectator_quantum_marked_count
        ),
        "all_marked_occurrence_count": (
            legacy_marked_occurrence_count + spectator_marked_occurrence_count
        ),
        "parent_families": {
            "SPLIT_SOURCE_SINGLE_BRIDGE": {
                "route_count": len(routes),
                "internal_edges": 3,
                "vertices": 3,
                "loops": 1,
                "connected": True,
                "one_particle_irreducible": True,
                "graph_classification": "CONNECTED_1PI_TRIANGLE_PARENT",
                "marked_inverse_edges": legacy_marked_occurrence_count,
                "topology_counts": dict(sorted(legacy_topology_counts.items())),
            },
            "SPECTATOR_SOURCE_DOUBLE_BRIDGE": {
                "route_count": len(spectator_routes),
                "internal_edges": 3,
                "vertices": 3,
                "loops": 1,
                "connected": True,
                "one_particle_irreducible": False,
                "graph_classification": (
                    "CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY"
                ),
                "source_action_edge_is_cut_edge": True,
                "loop_cycle_edges": ["bridge_1", "bridge_2"],
                "quantum_marked_inverse_edges": spectator_quantum_marked_count,
                "external_spectator_marks": spectator_external_marked_count,
                "topology_counts": dict(sorted(spectator_topology_counts.items())),
            },
        },
        "topology_counts": dict(sorted(topology_counts.items())),
        "family_route_counts": dict(sorted(family_counts.items())),
        "external_field_route_counts": dict(sorted(external_counts.items())),
        "spectator_external_field_route_counts": dict(
            sorted(spectator_external_counts.items())
        ),
        "source_ports": SOURCE_PORT,
        "cubic_vertices": {name: list(ports) for name, ports in VERTICES.items()},
        "pairs": pairs,
        "legacy_routes": [
            {"parent_family": "SPLIT_SOURCE_SINGLE_BRIDGE", **asdict(route)}
            for route in routes
        ],
        "spectator_routes": [asdict(route) for route in spectator_routes],
        "routes": [
            *(
                {"parent_family": "SPLIT_SOURCE_SINGLE_BRIDGE", **asdict(route)}
                for route in routes
            ),
            *(asdict(route) for route in spectator_routes),
        ],
    }


def verify(payload: dict[str, object], audit_text: str) -> list[tuple[str, object]]:
    checks: list[tuple[str, object]] = []

    def check(name: str, condition: bool, actual: object) -> None:
        if not condition:
            raise AssertionError(f"{name}: {actual!r}")
        checks.append((name, actual))

    routes = payload["routes"]
    pairs = payload["pairs"]
    assert isinstance(routes, list)
    assert isinstance(pairs, list)
    check("external_target_used", payload["external_target_used"] is False, False)
    check("ordered_pair_count", payload["ordered_pair_count"] == 81, payload["ordered_pair_count"])
    check("marked_pair_count", payload["marked_pair_count"] == 56, payload["marked_pair_count"])
    check("no_descendant_pair_count", payload["no_descendant_pair_count"] == 25, payload["no_descendant_pair_count"])
    check("directed_parent_route_count", len(routes) == 1365, len(routes))
    check(
        "legacy_directed_parent_route_count",
        payload["legacy_directed_parent_route_count"] == 495,
        payload["legacy_directed_parent_route_count"],
    )
    check(
        "spectator_directed_parent_route_count",
        payload["spectator_directed_parent_route_count"] == 870,
        payload["spectator_directed_parent_route_count"],
    )
    check(
        "marked_inverse_edge_occurrence_count",
        payload["marked_inverse_edge_occurrence_count"] == 1098,
        payload["marked_inverse_edge_occurrence_count"],
    )
    check(
        "all_marked_occurrence_count",
        payload["all_marked_occurrence_count"] == 1698,
        payload["all_marked_occurrence_count"],
    )
    check(
        "topology_counts",
        payload["topology_counts"]
        == {"TGG": 792, "TGM": 144, "THH": 102, "TMH": 60, "TMM": 267},
        payload["topology_counts"],
    )
    route_ids = [row["route_id"] for row in routes]
    check("route_ids_unique", len(route_ids) == len(set(route_ids)), len(route_ids))
    check(
        "all_bridge_edges_compatible",
        all(
            (
                compatible(row["bridge_left_port"], row["bridge_right_port"])
                if row["parent_family"] == "SPLIT_SOURCE_SINGLE_BRIDGE"
                else compatible(
                    row["bridge_1_source_action_port"],
                    row["bridge_1_loop_action_port"],
                )
                and compatible(
                    row["bridge_2_source_action_port"],
                    row["bridge_2_loop_action_port"],
                )
            )
            for row in routes
        ),
        True,
    )
    check(
        "all_source_edges_compatible",
        all(
            (
                compatible(row["left_source_field"], row["left_source_port"])
                and compatible(row["right_source_field"], row["right_source_port"])
                if row["parent_family"] == "SPLIT_SOURCE_SINGLE_BRIDGE"
                else compatible(row["quantum_source_field"], row["source_action_port"])
            )
            for row in routes
        ),
        True,
    )
    spectator_routes = [
        row
        for row in routes
        if row["parent_family"] == "SPECTATOR_SOURCE_DOUBLE_BRIDGE"
    ]
    check(
        "spectator_connected_but_1pr",
        all(
            row["connected"] is True
            and row["one_particle_irreducible"] is False
            and row["source_action_edge_is_cut_edge"] is True
            and row["loop_cycle_edges"] == ("bridge_1", "bridge_2")
            for row in spectator_routes
        ),
        len(spectator_routes),
    )
    check(
        "no_coefficient_claim",
        all(
            row["coefficient_status"]
            == "PENDING_EDGE_TAGGED_D_ALGEBRA_AND_SD_ORBIT"
            for row in routes
        ),
        True,
    )
    required_audit = (
        "N_{\\mathrm{directed\\ parent\\ routes}}=495+870=1365",
        "N_{\\mathrm{legacy}}=495",
        "N_{\\mathrm{spectator}}=870",
        "N_{\\mathrm{marked\\ inverse\\ edges}}=612+486=1098",
        "T_{GG}=180+612=792",
        "T_{GM}=144",
        "T_{MM}=87+180=267",
        "T_{MH}=60",
        "T_{HH}=24+78=102",
        "SPECTATOR_SOURCE_DOUBLE_BRIDGE",
        "CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY",
        "25=5\\times5",
        "STRUCTURAL_PARENT_CENSUS_ONLY__D_ALGEBRA_AND_SD_ORBITS_PENDING",
    )
    check(
        "audit_anchors",
        all(fragment in audit_text for fragment in required_audit),
        True,
    )
    return checks


def render_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    args = parser.parse_args()
    if not args.write and not args.check:
        args.check = True
    if not args.audit.is_file():
        raise SystemExit(f"missing audit: {args.audit}")
    payload = build_payload()
    checks = verify(payload, args.audit.read_text(encoding="utf-8"))
    expected = render_json(payload)
    if args.write:
        args.output.write_text(expected, encoding="utf-8")
    if args.check:
        if not args.output.is_file():
            raise SystemExit(f"missing output: {args.output}")
        actual = args.output.read_text(encoding="utf-8")
        if actual != expected:
            raise SystemExit("triangle parent census artifact is stale")
    for name, value in checks:
        print(f"PASS {name}: {value}")
    print(f"SUMMARY {len(checks)}/{len(checks)} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
