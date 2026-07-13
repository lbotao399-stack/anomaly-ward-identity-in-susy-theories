#!/usr/bin/env python3
"""Fail-closed Project-only census of the primitive WW matter-YZ families.

The audit derives the mixed ``I2-S3m-S3m`` triangle and its mandatory
``I2-S4m`` seagull from the locked Project composite/action grammars.  It
records exact stored coefficients and labeled Wick data, but it does not
assign a chiral-superpropagator normalization, an external-Y D-algebra
projection, an Euler-source I3/I4 derivative, a pole, or an anomaly
coefficient.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (  # noqa: E402
    AllowedContraction,
    Chirality,
    FieldType,
    Flow,
    HalfEdge,
    PropagatorGrammar,
    Statistics,
    WickPairing,
    enumerate_wick_pairings,
)
from scripts.step5_project_composites import (  # noqa: E402
    e_xi_terms,
    insertion_terms_at_valence,
    transport_e_xi_terms,
)
from scripts.step5_vertex_grammar import (  # noqa: E402
    DerivativeRequest,
    matter_bridge_monomials,
    ordered_functional_derivative,
)


GENERATED = ROOT / "generated/step5/full-n4-matter-yz-census.json"
AUDIT = ROOT / "audits/step5-full-n4-matter-yz-census-verification.json"

SOURCE_PATHS = (
    "contracts/foundations/step-04c-n4-super-yang-mills.md",
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md",
    "scripts/step5_graph_ir.py",
    "scripts/step5_project_composites.py",
    "scripts/step5_vertex_grammar.py",
)


@dataclass(frozen=True)
class CanonicalCoefficient:
    rational: Fraction
    sqrt2_power: int = 0
    i_power: int = 0
    symbols: tuple[str, ...] = ()

    @classmethod
    def from_project(cls, value: object) -> CanonicalCoefficient:
        return cls(
            Fraction(getattr(value, "rational")),
            int(getattr(value, "sqrt2_power", 0)),
            int(getattr(value, "i_power", 0)),
            tuple(str(symbol) for symbol in getattr(value, "symbols", ())),
        ).canonicalized()

    def canonicalized(self) -> CanonicalCoefficient:
        phase = self.i_power % 4
        rational = self.rational
        if phase in (2, 3):
            rational = -rational
        return CanonicalCoefficient(
            rational,
            self.sqrt2_power,
            phase % 2,
            tuple(sorted(self.symbols)),
        )

    def __mul__(self, other: CanonicalCoefficient) -> CanonicalCoefficient:
        return CanonicalCoefficient(
            self.rational * other.rational,
            self.sqrt2_power + other.sqrt2_power,
            self.i_power + other.i_power,
            self.symbols + other.symbols,
        ).canonicalized()

    def scaled(self, value: Fraction | int) -> CanonicalCoefficient:
        return CanonicalCoefficient(
            self.rational * Fraction(value),
            self.sqrt2_power,
            self.i_power,
            self.symbols,
        ).canonicalized()

    def payload(self) -> dict[str, object]:
        powers = Counter(self.symbols)
        return {
            "rational": {
                "numerator": self.rational.numerator,
                "denominator": self.rational.denominator,
            },
            "sqrt2_power": self.sqrt2_power,
            "i_power": self.i_power,
            "symbol_powers": dict(sorted(powers.items())),
        }


V_FIELD = FieldType("V", Statistics.BOSON, Chirality.REAL)
PHI_FIELD = FieldType("Phi", Statistics.BOSON, Chirality.CHIRAL)
TILDE_PHI_FIELD = FieldType("TildePhi", Statistics.BOSON, Chirality.ANTICHIRAL)

PROPAGATOR_GRAMMAR = PropagatorGrammar(
    (
        AllowedContraction("P_VV", "V", "V", "P_VV", False),
        AllowedContraction(
            "P_PHI_TILDEPHI_STRUCTURAL",
            "Phi",
            "TildePhi",
            "P_PhiTildePhi_STRUCTURAL",
            True,
        ),
    )
)


def _half_edge(
    half_edge_id: str,
    vertex_id: str,
    slot: int,
    field: FieldType,
) -> HalfEdge:
    return HalfEdge(
        half_edge_id,
        vertex_id,
        slot,
        field,
        Flow.NONE,
        f"momentum[{half_edge_id}]",
    )


def triangle_quantum_ports() -> tuple[HalfEdge, ...]:
    return (
        _half_edge("I_A", "I2", 0, V_FIELD),
        _half_edge("I_B", "I2", 1, V_FIELD),
        _half_edge("Y_TildePhi_M", "S3m_Y", 0, TILDE_PHI_FIELD),
        _half_edge("Y_V_D", "S3m_Y", 1, V_FIELD),
        _half_edge("Z_V_E", "S3m_Z", 0, V_FIELD),
        _half_edge("Z_Phi_N", "S3m_Z", 1, PHI_FIELD),
    )


def seagull_quantum_ports() -> tuple[HalfEdge, ...]:
    return (
        _half_edge("I_A", "I2", 0, V_FIELD),
        _half_edge("I_B", "I2", 1, V_FIELD),
        _half_edge("S4_V_D", "S4m_YZ", 0, V_FIELD),
        _half_edge("S4_V_F", "S4m_YZ", 1, V_FIELD),
    )


def _pairing_certificate(
    ports: Sequence[HalfEdge], pairing: WickPairing
) -> dict[str, object]:
    by_id = {port.half_edge_id: port for port in ports}
    vertices = sorted({port.vertex_id for port in ports})
    adjacency = {vertex: set() for vertex in vertices}
    for pair in pairing.pairs:
        left = by_id[pair.left_half_edge].vertex_id
        right = by_id[pair.right_half_edge].vertex_id
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen: set[str] = set()
    if vertices:
        stack = [vertices[0]]
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            stack.extend(adjacency[vertex] - seen)
    connected = len(seen) == len(vertices)
    loop_number = len(pairing.pairs) - len(vertices) + 1 if connected else None
    return {
        "connected": connected,
        "vertex_count": len(vertices),
        "edge_count": len(pairing.pairs),
        "loop_number_E_minus_V_plus_1": loop_number,
        "is_connected_one_loop": connected and loop_number == 1,
    }


def _partner(pairing: WickPairing, port_id: str) -> str:
    for pair in pairing.pairs:
        if pair.left_half_edge == port_id:
            return pair.right_half_edge
        if pair.right_half_edge == port_id:
            return pair.left_half_edge
    raise KeyError(port_id)


def _serialized_pairs(pairing: WickPairing) -> list[dict[str, object]]:
    return [asdict(pair) for pair in pairing.pairs]


TRIANGLE_COLORS = {
    "DIRECT": (
        "delta[u,v] kappaInv[A,D] kappaInv[B,E] kappaInv[M,N] "
        "cLower[D,P,M] cLower[E,N,Q]"
    ),
    "CROSSED": (
        "delta[u,v] kappaInv[A,E] kappaInv[B,D] kappaInv[M,N] "
        "cLower[D,P,M] cLower[E,N,Q]"
    ),
}

SEAGULL_COLORS = {
    "DIRECT": ("delta[u,v] kappaInv[A,D] kappaInv[B,F] kappa[Q,H] c[D,R,H] c[F,P,R]"),
    "CROSSED": ("delta[u,v] kappaInv[A,F] kappaInv[B,D] kappa[Q,H] c[D,R,H] c[F,P,R]"),
}


def _triangle_orientation(pairing: WickPairing) -> str:
    partner = _partner(pairing, "I_A")
    if partner == "Y_V_D":
        return "DIRECT"
    if partner == "Z_V_E":
        return "CROSSED"
    raise ValueError("not a connected mixed triangle pairing")


def _seagull_orientation(pairing: WickPairing) -> str:
    partner = _partner(pairing, "I_A")
    if partner == "S4_V_D":
        return "DIRECT"
    if partner == "S4_V_F":
        return "CROSSED"
    raise ValueError("not a connected matter-seagull pairing")


Momentum = tuple[int, int, int]


def _momentum_sum(words: Iterable[Momentum]) -> Momentum:
    total = [0, 0, 0]
    for word in words:
        for index, value in enumerate(word):
            total[index] += value
    return tuple(total)  # type: ignore[return-value]


def routing_payload() -> dict[str, object]:
    triangle_vertices: dict[str, tuple[Momentum, ...]] = {
        "I2": ((-1, -1, 0), (1, 0, 1), (0, 1, -1)),
        "S3m_Y": ((1, 0, 0), (0, 0, 1), (-1, 0, -1)),
        "S3m_Z": ((0, 1, 0), (0, 0, -1), (0, -1, 1)),
    }
    triangle_edges = {
        "eY": ((1, 0, 1), (-1, 0, -1)),
        "eZ": ((0, 1, -1), (0, -1, 1)),
        "eM": ((0, 0, 1), (0, 0, -1)),
    }
    seagull_vertices: dict[str, tuple[Momentum, ...]] = {
        "I2": ((-1, -1, 0), (0, 0, -1), (1, 1, 1)),
        "S4m_YZ": (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, -1, -1),
        ),
    }
    seagull_edges = {
        "e0": ((0, 0, -1), (0, 0, 1)),
        "e1": ((1, 1, 1), (-1, -1, -1)),
    }
    return {
        "basis_order": ["p1", "p2", "k"],
        "triangle": {
            "all_incoming_vertex_words": {
                "I2": ["-p1-p2", "p1+k", "p2-k"],
                "S3m_Y": ["p1", "k", "-p1-k"],
                "S3m_Z": ["p2", "-k", "-p2+k"],
            },
            "source_momentum": "-p1-p2",
            "denominators": ["k^2", "(k+p1)^2", "(k-p2)^2"],
            "vertex_sums": {
                vertex: list(_momentum_sum(words))
                for vertex, words in triangle_vertices.items()
            },
            "edge_endpoint_sums": {
                edge: list(_momentum_sum(words))
                for edge, words in triangle_edges.items()
            },
        },
        "seagull": {
            "all_incoming_vertex_words": {
                "I2": ["-p1-p2", "-k", "p1+p2+k"],
                "S4m_YZ": ["p1", "p2", "k", "-p1-p2-k"],
            },
            "source_momentum": "-p1-p2",
            "denominators": ["k^2", "(k+p1+p2)^2"],
            "vertex_sums": {
                vertex: list(_momentum_sum(words))
                for vertex, words in seagull_vertices.items()
            },
            "edge_endpoint_sums": {
                edge: list(_momentum_sum(words))
                for edge, words in seagull_edges.items()
            },
        },
    }


def _coefficient_data() -> dict[str, object]:
    i2 = CanonicalCoefficient.from_project(insertion_terms_at_valence(2)[0].coefficient)
    _, s3m, s4m = matter_bridge_monomials()
    s3 = CanonicalCoefficient.from_project(s3m.coefficient)
    s4 = CanonicalCoefficient.from_project(s4m.coefficient)
    p_vv = CanonicalCoefficient(Fraction(-2), symbols=("g2",))

    triangle_stored = i2 * s3 * s3
    triangle_action_expansion = Fraction(1, 2) * 2
    triangle_labeled = triangle_stored.scaled(triangle_action_expansion)
    triangle_known_propagators = triangle_labeled * p_vv * p_vv

    seagull_stored = i2 * s4
    seagull_action_expansion = Fraction(-1)
    seagull_labeled = seagull_stored.scaled(seagull_action_expansion)
    seagull_with_propagators = seagull_labeled * p_vv * p_vv

    return {
        "triangle": {
            "I2_coefficient": i2.payload(),
            "S3m_coefficient_each": s3.payload(),
            "stored_monomial_product": triangle_stored.payload(),
            "euclidean_action_expansion": {
                "expansion_coefficient": "1/2!",
                "external_YZ_copy_assignment_multiplicity": 2,
                "net_factor": "1",
            },
            "per_labeled_Wick_row_before_propagators": triangle_labeled.payload(),
            "two_exact_vector_propagator_factors": ["-2*g2", "-2*g2"],
            "known_factor_before_open_matter_propagator": (
                triangle_known_propagators.payload()
            ),
            "h_g2_reduction": "h*g2=1 gives -1/16",
            "remaining_factor": "G_PhiTildePhi_STRUCTURAL",
            "coefficient_status": "OPEN_MATTER_SUPERPROPAGATOR_AND_Y_DALGEBRA",
        },
        "seagull": {
            "I2_coefficient": i2.payload(),
            "S4m_coefficient": s4.payload(),
            "stored_monomial_product": seagull_stored.payload(),
            "euclidean_action_expansion": {
                "expansion_coefficient": "-1",
                "external_YZ_copy_assignment_multiplicity": 1,
                "net_factor": "-1",
            },
            "per_labeled_Wick_row_before_propagators": seagull_labeled.payload(),
            "two_exact_vector_propagator_factors": ["-2*g2", "-2*g2"],
            "factor_after_exact_vector_propagators": (
                seagull_with_propagators.payload()
            ),
            "h_g2_reduction": "h*g2=1 gives -g2/32",
            "coefficient_status": "OPEN_EXTERNAL_Y_DALGEBRA_NO_POLE_ASSIGNED",
        },
    }


def _project_derivation_data() -> dict[str, object]:
    i2_terms = insertion_terms_at_valence(2)
    _, cubic, quartic = matter_bridge_monomials()
    y_vertex = ordered_functional_derivative(
        cubic,
        (DerivativeRequest("Phi", "Y_external_precursor"),),
        vertex_id="S3m_Y",
    )
    z_vertex = ordered_functional_derivative(
        cubic,
        (DerivativeRequest("TildePhi", "Z_external"),),
        vertex_id="S3m_Z",
    )
    yz_seagull = ordered_functional_derivative(
        quartic,
        (
            DerivativeRequest("Phi", "Y_external_precursor"),
            DerivativeRequest("TildePhi", "Z_external"),
        ),
        vertex_id="S4m_YZ",
    )
    return {
        "I2": [
            {
                "term_id": term.term_id,
                "origin": term.origin,
                "coefficient": CanonicalCoefficient.from_project(
                    term.coefficient
                ).payload(),
                "tags": list(term.tags),
                "matter_degree": term.matter_degree,
                "v_degree": term.v_degree,
            }
            for term in i2_terms
        ],
        "S3m_source": {
            "monomial_id": cubic.monomial_id,
            "ordered_fields": [field.field_name for field in cubic.ordered_fields],
            "coefficient": CanonicalCoefficient.from_project(
                cubic.coefficient
            ).payload(),
            "color_word": list(cubic.color_word),
        },
        "S3m_Y_extraction": {
            "external_field": y_vertex.terms[0].external_slots[0].field_name,
            "remaining_quantum_fields": [
                field.field_name for field in y_vertex.terms[0].remaining_fields
            ],
            "functional_derivative_koszul_sign": y_vertex.terms[0].koszul_sign,
        },
        "S3m_Z_extraction": {
            "external_field": z_vertex.terms[0].external_slots[0].field_name,
            "remaining_quantum_fields": [
                field.field_name for field in z_vertex.terms[0].remaining_fields
            ],
            "functional_derivative_koszul_sign": z_vertex.terms[0].koszul_sign,
        },
        "S4m_source": {
            "monomial_id": quartic.monomial_id,
            "ordered_fields": [field.field_name for field in quartic.ordered_fields],
            "coefficient": CanonicalCoefficient.from_project(
                quartic.coefficient
            ).payload(),
            "color_word": list(quartic.color_word),
        },
        "S4m_YZ_extraction": {
            "external_fields": [
                slot.field_name for slot in yz_seagull.terms[0].external_slots
            ],
            "remaining_quantum_fields": [
                field.field_name for field in yz_seagull.terms[0].remaining_fields
            ],
            "functional_derivative_koszul_sign": yz_seagull.terms[0].koszul_sign,
        },
    }


def _triangle_rows() -> tuple[list[dict[str, object]], int]:
    ports = triangle_quantum_ports()
    all_pairings = enumerate_wick_pairings(ports, PROPAGATOR_GRAMMAR)
    connected = [
        pairing
        for pairing in all_pairings
        if _pairing_certificate(ports, pairing)["is_connected_one_loop"]
    ]
    rows: list[dict[str, object]] = []
    for placement in ("LEFT", "RIGHT"):
        for pairing in connected:
            orientation = _triangle_orientation(pairing)
            rows.append(
                {
                    "row_id": f"I2_{placement}__{orientation}",
                    "D_minus_placement": placement,
                    "orientation": orientation,
                    "ordered_external_word": ["Y_u^P", "Z_v^Q"],
                    "external_ports": {
                        "Y_precursor": "Phi_u^P at S3m_Y",
                        "Z": "TildePhi_v^Q at S3m_Z",
                    },
                    "quantum_ports": [
                        {
                            "port_id": port.half_edge_id,
                            "vertex_id": port.vertex_id,
                            "field": port.field_type.name,
                        }
                        for port in ports
                    ],
                    "wick_pairs": _serialized_pairs(pairing),
                    "wick_koszul_sign": pairing.koszul_sign,
                    "typed_automorphism_order": 1,
                    "symmetry_division_applied": False,
                    "flavor_tensor": "delta[u,v]",
                    "color_tensor": TRIANGLE_COLORS[orientation],
                    "certificate": _pairing_certificate(ports, pairing),
                }
            )
    disconnected = sum(
        not _pairing_certificate(ports, pairing)["connected"]
        for pairing in all_pairings
    )
    return rows, disconnected


def _seagull_rows() -> tuple[list[dict[str, object]], int]:
    ports = seagull_quantum_ports()
    all_pairings = enumerate_wick_pairings(ports, PROPAGATOR_GRAMMAR)
    connected = [
        pairing
        for pairing in all_pairings
        if _pairing_certificate(ports, pairing)["is_connected_one_loop"]
    ]
    rows: list[dict[str, object]] = []
    for placement in ("LEFT", "RIGHT"):
        for pairing in connected:
            orientation = _seagull_orientation(pairing)
            rows.append(
                {
                    "row_id": f"I2_{placement}__{orientation}",
                    "D_minus_placement": placement,
                    "orientation": orientation,
                    "ordered_external_word": ["Y_u^P", "Z_v^Q"],
                    "external_ports": {
                        "Y_precursor": "Phi_u^P at S4m_YZ",
                        "Z": "TildePhi_v^Q at S4m_YZ",
                    },
                    "quantum_ports": [
                        {
                            "port_id": port.half_edge_id,
                            "vertex_id": port.vertex_id,
                            "field": port.field_type.name,
                        }
                        for port in ports
                    ],
                    "wick_pairs": _serialized_pairs(pairing),
                    "wick_koszul_sign": pairing.koszul_sign,
                    "typed_automorphism_order": 1,
                    "symmetry_division_applied": False,
                    "flavor_tensor": "delta[u,v]",
                    "color_tensor": SEAGULL_COLORS[orientation],
                    "certificate": _pairing_certificate(ports, pairing),
                }
            )
    disconnected = sum(
        not _pairing_certificate(ports, pairing)["connected"]
        for pairing in all_pairings
    )
    return rows, disconnected


def _open_obligations() -> list[dict[str, object]]:
    e_xi_matter = next(term for term in e_xi_terms() if term.term_id == "E_Xi_matter_0")
    transported_matter = [
        term
        for term in transport_e_xi_terms("project_functional_euler")
        if term.matter_degree == 2
    ]
    mixed_i3 = [term for term in insertion_terms_at_valence(3) if term.matter_degree]
    mixed_i4 = [term for term in insertion_terms_at_valence(4) if term.matter_degree]
    return [
        {
            "id": "MATTER_SUPERPROPAGATOR_NORMALIZATION",
            "status": "OPEN",
            "known": "component kernels (5.47b) and a structural G_PhiTildePhi symbol",
            "missing": (
                "the normalized constrained Euclidean superfield inverse "
                "G_0^{Phi,TildePhi}, including ordered D-projectors"
            ),
        },
        {
            "id": "EXTERNAL_Y_DALGEBRA_PROJECTION",
            "status": "OPEN",
            "known": "the action extraction exposes external Phi_u^P",
            "missing": (
                "an edge-tagged transfer retaining D_+ Phi_u^P=Y_u^P, "
                "with endpoint and Koszul signs"
            ),
        },
        {
            "id": "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
            "status": "OPEN",
            "known_E_Xi_term_id": e_xi_matter.term_id,
            "known_E_Xi_coefficient": CanonicalCoefficient.from_project(
                e_xi_matter.coefficient
            ).payload(),
            "missing_functional_derivative": (
                "delta^3{[-2*h^-1*kappaInv[A,L]*nabla_+ E_V,L]*X^B"
                "+(A<->B)-2i*nabla_+(Phi x TildePhi)^A*X^B-(A<->B)}"
                "/(delta V delta Phi_r delta TildePhi_s)|_0"
            ),
            "current_mixed_I3_source_term_count": len(mixed_i3),
        },
        {
            "id": "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            "status": "OPEN",
            "known_transported_E_Xi_matter_term_count": len(transported_matter),
            "missing_functional_derivative": (
                "delta^4{[-2*h^-1*kappaInv[A,L]*nabla_+ E_V,L]*X^B"
                "+(A<->B)-2i*nabla_+(Phi x TildePhi)^A*X^B-(A<->B)}"
                "/(delta V_1 delta V_2 delta Phi_r delta TildePhi_s)|_0"
            ),
            "current_mixed_I4_source_term_count": len(mixed_i4),
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
    derivation = _project_derivation_data()
    coefficients = _coefficient_data()
    routing = routing_payload()
    triangle_rows, triangle_disconnected = _triangle_rows()
    seagull_rows, seagull_disconnected = _seagull_rows()
    obligations = _open_obligations()

    checks = {
        "I2_has_exact_two_D_minus_placements": (
            [row["origin"] for row in derivation["I2"]]
            == ["D_- placement LEFT", "D_- placement RIGHT"]
            and all(
                row["coefficient"]["rational"] == {"numerator": 1, "denominator": 64}
                for row in derivation["I2"]
            )
        ),
        "matter_bridge_vertices_are_exact_Project_monomials": (
            derivation["S3m_source"]["monomial_id"] == "matter_bridge_v1"
            and derivation["S4m_source"]["monomial_id"] == "matter_bridge_v2"
        ),
        "cubic_external_extractions_leave_exact_quantum_ports": (
            derivation["S3m_Y_extraction"]["remaining_quantum_fields"]
            == ["TildePhi", "V"]
            and derivation["S3m_Z_extraction"]["remaining_quantum_fields"]
            == ["V", "Phi"]
        ),
        "quartic_YZ_extraction_leaves_two_vector_ports": (
            derivation["S4m_YZ_extraction"]["external_fields"] == ["Phi", "TildePhi"]
            and derivation["S4m_YZ_extraction"]["remaining_quantum_fields"]
            == ["V", "V"]
        ),
        "triangle_has_four_labeled_rows_and_one_disconnected_matching": (
            len(triangle_rows) == 4
            and {row["orientation"] for row in triangle_rows} == {"DIRECT", "CROSSED"}
            and triangle_disconnected == 1
        ),
        "seagull_has_four_labeled_rows_and_one_disconnected_matching": (
            len(seagull_rows) == 4
            and {row["orientation"] for row in seagull_rows} == {"DIRECT", "CROSSED"}
            and seagull_disconnected == 1
        ),
        "all_internal_Wick_signs_are_bosonic_plus_one": all(
            row["wick_koszul_sign"] == 1 for row in triangle_rows + seagull_rows
        ),
        "all_routes_close_at_vertices_and_edges": all(
            vector == [0, 0, 0]
            for graph in routing.values()
            if isinstance(graph, dict) and "vertex_sums" in graph
            for vector in list(graph["vertex_sums"].values())
            + list(graph["edge_endpoint_sums"].values())
        ),
        "triangle_stored_coefficient_is_minus_h2_over_64": (
            coefficients["triangle"]["stored_monomial_product"]
            == {
                "rational": {"numerator": -1, "denominator": 64},
                "sqrt2_power": 0,
                "i_power": 0,
                "symbol_powers": {"h": 2},
            }
        ),
        "seagull_labeled_Wick_coefficient_is_minus_h_over_128": (
            coefficients["seagull"]["per_labeled_Wick_row_before_propagators"]
            == {
                "rational": {"numerator": -1, "denominator": 128},
                "sqrt2_power": 0,
                "i_power": 0,
                "symbol_powers": {"h": 1},
            }
        ),
        "all_four_physics_gates_remain_explicitly_open": (
            [row["id"] for row in obligations]
            == [
                "MATTER_SUPERPROPAGATOR_NORMALIZATION",
                "EXTERNAL_Y_DALGEBRA_PROJECTION",
                "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
                "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            ]
            and all(row["status"] == "OPEN" for row in obligations)
        ),
        "current_direct_I3_I4_source_grammar_has_no_matter_terms": (
            obligations[2]["current_mixed_I3_source_term_count"] == 0
            and obligations[3]["current_mixed_I4_source_term_count"] == 0
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "schema": "Step5FullN4MatterYZCensus.v1",
        "status": (
            "PASS_EXACT_PROJECT_GRAPH_CENSUS__AMPLITUDES_FAIL_CLOSED"
            if not failed
            else "FAIL"
        ),
        "authority_status": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "scope": "PROJECT_ONLY_WW_MIXED_MATTER_YZ_TRIANGLE_AND_SEAGULL",
        "external_results_imported": False,
        "holomorphic_twist_input_count": 0,
        "external_target_input_count": 0,
        "source_sha256": source_hashes(),
        "letter_dictionary": {
            "X^A": "(nabla_+ W_+)^A",
            "Y_u^P": "(nabla_+ Phi_u)^P",
            "Z_v^Q": "TildePhi_v^Q",
        },
        "project_derivation": derivation,
        "triangle_I2_S3m_S3m": {
            "classification": "GRAMMAR_DERIVED_TYPED_GRAPH_FAMILY",
            "action_vertex_count": 2,
            "internal_edges": ["P_VV", "P_VV", "P_PhiTildePhi_STRUCTURAL"],
            "connected_labeled_Wick_rows": triangle_rows,
            "disconnected_typed_matching_count": triangle_disconnected,
            "coefficient_ledger": coefficients["triangle"],
            "routing": routing["triangle"],
            "result_status": "GRAPH_EXISTS__AMPLITUDE_OPEN",
        },
        "seagull_I2_S4m": {
            "classification": "GRAMMAR_DERIVED_MANDATORY_CONTACT_FAMILY",
            "action_vertex_count": 1,
            "internal_edges": ["P_VV", "P_VV"],
            "connected_labeled_Wick_rows": seagull_rows,
            "disconnected_typed_matching_count": seagull_disconnected,
            "coefficient_ledger": coefficients["seagull"],
            "routing": routing["seagull"],
            "result_status": "GRAPH_EXISTS__DALGEBRA_AND_POLE_OPEN",
        },
        "Euler_matter_contact_boundary": {
            "I3_typed_candidates": [
                "external V,V with two oriented Phi-TildePhi edges",
                "external Phi,TildePhi with one V edge and one matter edge",
                "external TildePhi,Phi with one V edge and one matter edge",
            ],
            "I4_typed_candidates": [
                "external V,V with one matter tadpole edge",
                "external Phi,TildePhi with one vector tadpole edge",
            ],
            "status": "STRUCTURAL_CANDIDATES_ONLY_SOURCE_FUNCTIONAL_DERIVATIVES_OPEN",
        },
        "open_obligations": obligations,
        "acceptance_boundary": {
            "matter_triangle_physical_GraphIR": False,
            "external_Y_projection_accepted": False,
            "I3_Euler_contact_instantiated": False,
            "I4_Euler_contact_instantiated": False,
            "ordinary_UV_pole_computed": False,
            "renormalized_one_loop_coefficient_accepted": False,
        },
        "checks": checks,
        "totals": {
            "checks": len(checks),
            "failed": len(failed),
            "triangle_labeled_rows": len(triangle_rows),
            "seagull_labeled_rows": len(seagull_rows),
            "open_obligations": len(obligations),
            "accepted_coefficients": 0,
        },
    }


def write_artifacts() -> dict[str, object]:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    audit = {
        "schema": "Step5FullN4MatterYZCensusAudit.v1",
        "status": payload["status"],
        "scope": payload["scope"],
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "checks": payload["checks"],
        "totals": payload["totals"],
        "external_results_imported": False,
        "holomorphic_twist_input_count": 0,
    }
    AUDIT.write_bytes(canonical_json(audit))
    return payload


def main() -> int:
    payload = write_artifacts()
    print(json.dumps(payload["totals"], sort_keys=True))
    return 0 if str(payload["status"]).startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
