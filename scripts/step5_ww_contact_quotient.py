#!/usr/bin/env python3
"""Basis-resolved WW contact graphs and their structural quotient.

This module performs only combinatorics that are already fixed by the Project
composite grammar.  It never imports an aggregate contact coefficient, a pole,
or an anomaly coefficient.  Missing projection/D-algebra data are emitted as
typed proof obligations instead of being inferred.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (
    Chirality,
    ExternalLeg,
    FieldType,
    Flow,
    GraphIR,
    HalfEdge,
    IndexSlot,
    IndexSpace,
    InternalEdge,
    Statistics,
    Variance,
    Vertex,
)
from scripts.step5_project_composites import (
    CompositeTerm,
    antichiral_gauge_s3_terms,
    insertion_terms_at_valence,
    seed_port_assignment_payload,
)


OUT = ROOT / "generated/step5/contact-quotient"
AUDIT = ROOT / "audits/step5-ww-contact-quotient-verification.json"


def stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value: object) -> str:
    return hashlib.sha256(stable_json(value).encode()).hexdigest()


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class ExactMonomial:
    """A normalized monomial in Q(i) and named commuting symbols."""

    rational: Fraction = Fraction(1)
    i_power: int = 0
    symbols: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        rational = Fraction(self.rational)
        power = self.i_power % 4
        if power == 2:
            rational = -rational
            power = 0
        elif power == 3:
            rational = -rational
            power = 1
        object.__setattr__(self, "rational", rational)
        object.__setattr__(self, "i_power", power)
        object.__setattr__(self, "symbols", tuple(sorted(self.symbols)))

    @classmethod
    def from_project_json(cls, value: Mapping[str, object]) -> "ExactMonomial":
        symbols = value["symbols"]
        if not isinstance(symbols, list) or any(not isinstance(item, str) for item in symbols):
            raise TypeError("Project coefficient symbols must be a list of strings")
        return cls(Fraction(str(value["rational"])), int(value["i_power"]), tuple(symbols))

    def __mul__(self, other: "ExactMonomial") -> "ExactMonomial":
        return ExactMonomial(
            self.rational * other.rational,
            self.i_power + other.i_power,
            self.symbols + other.symbols,
        )

    def render(self) -> str:
        if self.rational == 0:
            return "0"
        magnitude = abs(self.rational)
        factors: list[str] = []
        if magnitude != 1 or not (self.i_power or self.symbols):
            factors.append(fraction_text(magnitude))
        if self.i_power:
            factors.append("i")
        factors.extend(self.symbols)
        body = "*".join(factors) if factors else "1"
        return f"-{body}" if self.rational < 0 else body

    def as_json(self) -> dict[str, object]:
        return {
            "rational": fraction_text(self.rational),
            "i_power": self.i_power,
            "symbols": list(self.symbols),
            "rendered": self.render(),
        }


def color(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.COLOR_ADJOINT, label, Variance.UP)


V_FIELD = FieldType("v", Statistics.BOSON, Chirality.REAL, (color("C"),))
X_FIELD = FieldType(
    "X=nabla_+W_+",
    Statistics.BOSON,
    Chirality.UNCONSTRAINED,
    (color("E"),),
)
TILDE_W_FIELD = FieldType(
    "TildeW_dot_alpha",
    Statistics.FERMION,
    Chirality.ANTICHIRAL,
    (color("D"), IndexSlot(IndexSpace.DOTTED, "dot_alpha", Variance.DOWN)),
)
SOURCE_FIELD = FieldType(
    "Source[nabla_-(X^A X^B)]",
    Statistics.FERMION,
    Chirality.UNCONSTRAINED,
    (color("A"), color("B")),
)


def source_term_record(term: CompositeTerm) -> dict[str, object]:
    expression = term.expression.as_json()
    return {
        "term_id": term.term_id,
        "family": term.family,
        "coefficient": term.coefficient.as_json(),
        "v_degree": term.v_degree,
        "parity": term.parity,
        "free_color": term.free_color,
        "free_spinor": term.free_spinor,
        "origin": term.origin,
        "source_equations": list(term.source_equations),
        "tags": list(term.tags),
        "expression": expression,
        "expression_sha256": sha256_json(expression),
    }


def joined_projected_rows(
    selected: Sequence[Mapping[str, object]],
    all_assignments: Sequence[Mapping[str, object]],
) -> list[dict[str, object]]:
    """Join a projected row back to its lossless ordered-port assignment."""

    by_id = {str(row["assignment_id"]): row for row in all_assignments}
    result: list[dict[str, object]] = []
    for projection in selected:
        assignment_id = str(projection["assignment_id"])
        assignment = by_id[assignment_id]
        ordered_ports = assignment["ordered_ports"]
        color_word = assignment["color_bracket_word"]
        if not isinstance(ordered_ports, list) or not ordered_ports:
            raise ValueError(f"{assignment_id} lost its ordered ports")
        if not isinstance(color_word, list):
            raise TypeError(f"{assignment_id} has an invalid color word")
        if any(
            not isinstance(port, dict)
            or not isinstance(port.get("derivative_word_outer_to_inner"), list)
            or not port["derivative_word_outer_to_inner"]
            for port in ordered_ports
        ):
            raise ValueError(f"{assignment_id} lost derivative scope")
        result.append(
            {
                **dict(projection),
                "ordered_ports": ordered_ports,
                "color_bracket_word": color_word,
                "source_family": assignment["source_family"],
                "coefficient_changed_by_split": assignment["coefficient_changed_by_split"],
            }
        )
    return result


def ordered_ports(row: Mapping[str, object]) -> list[dict[str, object]]:
    value = row["ordered_ports"]
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise TypeError("ordered_ports must be a list of dictionaries")
    return value


def port_index(rows: Sequence[Mapping[str, object]], port_id: str) -> int:
    return next(index for index, row in enumerate(rows) if row["port_id"] == port_id)


def role_ports(row: Mapping[str, object], role: str) -> list[dict[str, object]]:
    return [port for port in ordered_ports(row) if port["role"] == role]


def projection_scope_check(row: Mapping[str, object], expected: Sequence[str]) -> dict[str, object]:
    projections = row["external_projections"]
    if not isinstance(projections, list) or len(projections) != 1:
        raise ValueError("a selected WW contact row needs exactly one external projection")
    projected_port = str(projections[0]["port_id"])
    port = next(item for item in ordered_ports(row) if item["port_id"] == projected_port)
    word = list(port["derivative_word_outer_to_inner"])
    return {
        "projected_port": projected_port,
        "actual_local_scope": word,
        "expected_linear_scope": list(expected),
        "status": (
            "LOCAL_SCOPE_MATCH"
            if word == list(expected)
            else "REQUIRES_EDGE_TAGGED_D_ALGEBRA_TRANSFER"
        ),
    }


def decorated_class_id(prefix: str, signature: Mapping[str, object]) -> tuple[str, str]:
    digest = sha256_json(signature)
    return f"{prefix}-{digest[:20]}", digest


def graph_port_provenance(row: Mapping[str, object]) -> list[dict[str, object]]:
    return [
        {
            "ordered_position": position,
            "port_id": port["port_id"],
            "role": port["role"],
            "substituted_field": port["substituted_field"],
            "derivative_word_outer_to_inner": port["derivative_word_outer_to_inner"],
            "derivative_scope_classification": (
                "ORDERED_DERIVATIVE_WORD"
                if port["derivative_word_outer_to_inner"]
                else "IDENTITY_NO_DERIVATIVE"
            ),
            "color_token": f"Color[{port['port_id']}]",
        }
        for position, port in enumerate(ordered_ports(row))
    ]


PROPAGATOR_COEFFICIENT = ExactMonomial(Fraction(-2), symbols=("g^2", "kappa^-1"))


def bubble_graph_record(
    i_number: int,
    s_number: int,
    pairing_number: int,
    i_row: Mapping[str, object],
    s_row: Mapping[str, object],
    source_terms: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    i_ports = ordered_ports(i_row)
    s_ports = ordered_ports(s_row)
    i_quantum = role_ports(i_row, "QUANTUM_WICK")
    s_quantum = role_ports(s_row, "QUANTUM_WICK")
    i_background = role_ports(i_row, "BACKGROUND_EXTERNAL")
    s_background = role_ports(s_row, "BACKGROUND_EXTERNAL")
    if tuple(map(len, (i_quantum, s_quantum, i_background, s_background))) != (2, 2, 1, 1):
        raise ValueError("I3 x S3 contact requires (2,2,1,1) typed port counts")

    permutation = (0, 1) if pairing_number == 1 else (1, 0)
    graph_id = f"CQ-I3S3-I{i_number:03d}-S{s_number:02d}-P{pairing_number}"
    i_half_edge = {str(port["port_id"]): f"{graph_id}__I__h{position}" for position, port in enumerate(i_ports)}
    s_half_edge = {str(port["port_id"]): f"{graph_id}__S__h{position}" for position, port in enumerate(s_ports)}
    source_half_edge = f"{graph_id}__I__source"

    s_quantum_momenta = ("k", "q-k")
    i_opposite_momenta = ("-k", "k-q")
    momentum_by_port: dict[str, str] = {
        str(i_background[0]["port_id"]): "-p",
        str(s_background[0]["port_id"]): "-q",
    }
    for s_position, s_port in enumerate(s_quantum):
        momentum_by_port[str(s_port["port_id"])] = s_quantum_momenta[s_position]
        matched_i = i_quantum[permutation[s_position]]
        momentum_by_port[str(matched_i["port_id"])] = i_opposite_momenta[s_position]

    half_edges: list[HalfEdge] = []
    for position, port in enumerate(i_ports):
        is_background = port["role"] == "BACKGROUND_EXTERNAL"
        half_edges.append(
            HalfEdge(
                i_half_edge[str(port["port_id"])],
                "vI3",
                position,
                X_FIELD if is_background else V_FIELD,
                Flow.IN if is_background else Flow.NONE,
                momentum_by_port[str(port["port_id"])],
            )
        )
    half_edges.append(
        HalfEdge(source_half_edge, "vI3", len(i_ports), SOURCE_FIELD, Flow.IN, "p+q")
    )
    for position, port in enumerate(s_ports):
        is_background = port["role"] == "BACKGROUND_EXTERNAL"
        half_edges.append(
            HalfEdge(
                s_half_edge[str(port["port_id"])],
                "vS3",
                position,
                TILDE_W_FIELD if is_background else V_FIELD,
                Flow.IN if is_background else Flow.NONE,
                momentum_by_port[str(port["port_id"])],
            )
        )

    i_term = source_terms[str(i_row["source_term_id"])]
    s_term = source_terms[str(s_row["source_term_id"])]
    edges: list[InternalEdge] = []
    pairing_rows: list[dict[str, object]] = []
    for edge_position, s_port in enumerate(s_quantum):
        i_port = i_quantum[permutation[edge_position]]
        edge_id = f"e{edge_position}"
        momentum = s_quantum_momenta[edge_position]
        edges.append(
            InternalEdge(
                edge_id,
                s_half_edge[str(s_port["port_id"])],
                i_half_edge[str(i_port["port_id"])],
                "-2*g^2*kappa^-1*delta4theta/p_edge^2",
                momentum,
                Flow.NONE,
            )
        )
        pairing_rows.append(
            {
                "edge_id": edge_id,
                "S3_port": s_port["port_id"],
                "I3_port": i_port["port_id"],
                "S3_ordered_position": port_index(s_ports, str(s_port["port_id"])),
                "I3_ordered_position": port_index(i_ports, str(i_port["port_id"])),
                "momentum_at_S3": momentum,
                "momentum_at_I3": i_opposite_momenta[edge_position],
                "color_contraction": (
                    f"kappa^-1[Color[{s_port['port_id']}],Color[{i_port['port_id']}]]"
                ),
                "propagator_coefficient": PROPAGATOR_COEFFICIENT.as_json(),
            }
        )

    i_coefficient = ExactMonomial.from_project_json(i_row["source_coefficient"])
    s_coefficient = ExactMonomial.from_project_json(s_row["source_coefficient"])
    known_coefficient = i_coefficient * s_coefficient * PROPAGATOR_COEFFICIENT * PROPAGATOR_COEFFICIENT
    metadata = {
        "family": "I3_X_S3_ANTICHIRAL",
        "graph_status": "D_UNREDUCED_DECORATED_WICK_GRAPH_WITH_OPEN_PROJECTION_NORMALIZATION",
        "i3_assignment": str(i_row["projected_assignment_id"]),
        "s3_assignment": str(s_row["projected_assignment_id"]),
        "pairing_permutation": ",".join(map(str, permutation)),
        "wick_sign": "+1",
        "koszul_sign": "+1",
        "symmetry_factor": "OPEN_TYPED_AUTOMORPHISM_AUDIT",
        "typed_automorphism_order": "OPEN_TYPED_AUTOMORPHISM_AUDIT",
        "known_coefficient": known_coefficient.render(),
        "path_integral_vertex_expansion_factor": "OPEN_NOT_EMITTED_BY_COMPOSITE_GRAMMAR",
        "external_projection_normalization": "OPEN_NOT_EMITTED_BY_COMPOSITE_GRAMMAR",
    }
    graph = GraphIR(
        graph_id=graph_id,
        vertices=(
            Vertex(
                "vI3",
                "COMPOSITE_I3_PROJECTED_X_V_V",
                tuple(i_half_edge[str(port["port_id"])] for port in i_ports) + (source_half_edge,),
                str(i_row["source_coefficient"]["rendered"]),
                (f"AST[{i_term['expression_sha256']}]",),
                "theta_I",
                "delta(-p-k+(k-q)+(p+q))",
                coefficient_factors=(
                    str(i_row["source_coefficient"]["rendered"]),
                    "BQ_split_multiplicity=1",
                ),
            ),
            Vertex(
                "vS3",
                "ACTION_S3_ANTICHIRAL_PROJECTED_TILDEW_V_V",
                tuple(s_half_edge[str(port["port_id"])] for port in s_ports),
                str(s_row["source_coefficient"]["rendered"]),
                (f"AST[{s_term['expression_sha256']}]", "kappa[A,B]"),
                "theta_S",
                "delta(-q+k+(q-k))",
                coefficient_factors=(
                    str(s_row["source_coefficient"]["rendered"]),
                    "BQ_split_multiplicity=1",
                    "PATH_INTEGRAL_EXPANSION_FACTOR_OPEN",
                ),
            ),
        ),
        half_edges=tuple(half_edges),
        internal_edges=tuple(edges),
        external_legs=(
            ExternalLeg(
                "X_external",
                i_half_edge[str(i_background[0]["port_id"])],
                X_FIELD,
                "p",
                f"Color[{i_background[0]['port_id']}]",
            ),
            ExternalLeg(
                "TildeW_external",
                s_half_edge[str(s_background[0]["port_id"])],
                TILDE_W_FIELD,
                "q",
                f"Color[{s_background[0]['port_id']}]",
                spinor_indices=(IndexSlot(IndexSpace.DOTTED, "dot_alpha", Variance.DOWN),),
            ),
            ExternalLeg("WW_source", source_half_edge, SOURCE_FIELD, "p+q", "A,B"),
        ),
        loop_momenta=("k",),
        metadata=tuple(sorted(metadata.items())),
    )
    graph.assert_linear_momentum_routing()

    signature = {
        "family": "I3_X_S3_ANTICHIRAL",
        "I3_source_ast": i_term["expression_sha256"],
        "S3_source_ast": s_term["expression_sha256"],
        "I3_external_position": port_index(i_ports, str(i_background[0]["port_id"])),
        "S3_external_position": port_index(s_ports, str(s_background[0]["port_id"])),
        "I3_derivative_scopes": [port["derivative_word_outer_to_inner"] for port in i_ports],
        "S3_derivative_scopes": [port["derivative_word_outer_to_inner"] for port in s_ports],
        "pairing_ordered_positions": [
            [row["S3_ordered_position"], row["I3_ordered_position"]]
            for row in pairing_rows
        ],
    }
    class_id, signature_hash = decorated_class_id("DGC-I3S3", signature)
    return {
        "labeled_graph_id": graph_id,
        "decorated_graph_class_id": class_id,
        "physical_graph_class_status": "OPEN_TYPED_AUTOMORPHISM_COLOR_DWORD_CANONICALIZATION",
        "canonical_signature_sha256": signature_hash,
        "canonical_signature": signature,
        "graph_ir": graph.canonical_dict(),
        "source_term_bindings": {
            "I3": {"term_id": i_term["term_id"], "expression_sha256": i_term["expression_sha256"]},
            "S3": {"term_id": s_term["term_id"], "expression_sha256": s_term["expression_sha256"]},
        },
        "port_provenance": {
            "I3": graph_port_provenance(i_row),
            "S3": graph_port_provenance(s_row),
        },
        "color_provenance": {
            "I3_color_bracket_word": i_row["color_bracket_word"],
            "S3_color_bracket_word": s_row["color_bracket_word"],
            "edge_contractions": [row["color_contraction"] for row in pairing_rows],
            "full_color_tensor_reduction": "OPEN_AST_TO_INDEX_TENSOR_COMPILER",
        },
        "pairing": {
            "declared_quantum_field_word": [
                *[port["port_id"] for port in i_quantum],
                *[port["port_id"] for port in s_quantum],
            ],
            "pairs": pairing_rows,
            "statistics": ["BOSON", "BOSON", "BOSON", "BOSON"],
            "fermion_crossings": 0,
            "koszul_sign": 1,
            "wick_sign": 1,
            "labeled_pairing_multiplicity": 1,
        },
        "coefficient_provenance": {
            "I3_source": i_coefficient.as_json(),
            "S3_source": s_coefficient.as_json(),
            "two_propagators": [PROPAGATOR_COEFFICIENT.as_json()] * 2,
            "BQ_split_multiplicities": [1, 1],
            "Wick_sign": 1,
            "Koszul_sign": 1,
            "typed_automorphism_order_audit": "OPEN",
            "automorphism_division_applied": False,
            "known_product_excluding_open_factors": known_coefficient.as_json(),
            "open_factors": [
                "EUCLIDEAN_PATH_INTEGRAL_ACTION_VERTEX_EXPANSION",
                "EXTERNAL_PROJECTOR_NORMALIZATION_AND_EXTRACTION_SIGN",
                "TYPED_AUTOMORPHISM_AND_SYMMETRY_AUDIT",
            ],
        },
        "projection_scope_checks": {
            "I3_to_X": projection_scope_check(i_row, ("D_+", "barD^2", "D_+")),
            "S3_to_TildeW": projection_scope_check(s_row, ("D^2", "barD_dot_a")),
        },
        "classification": "ENUMERATED_D_UNREDUCED; AMPLITUDE_COEFFICIENT_NOT_CLOSED",
    }


def scope_parity(word: Sequence[str]) -> int:
    odd = {"D_+", "D_-", "D_a", "barD_dot_a", "barD_dot_plus", "barD_dot_minus"}
    return sum(token in odd for token in word) % 2


def pending_projection_field(port: Mapping[str, object]) -> FieldType:
    word = port["derivative_word_outer_to_inner"]
    if not isinstance(word, list):
        raise TypeError("projection scope must be a list")
    statistics = Statistics.FERMION if scope_parity(word) else Statistics.BOSON
    return FieldType(
        "ProjectionPending[" + " ".join(map(str, word)) + "]",
        statistics,
        Chirality.UNCONSTRAINED,
        (color("P"),),
    )


def tadpole_graph_record(
    number: int,
    row: Mapping[str, object],
    source_terms: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    ports = ordered_ports(row)
    backgrounds = role_ports(row, "BACKGROUND_EXTERNAL")
    quantum = role_ports(row, "QUANTUM_WICK")
    if (len(backgrounds), len(quantum)) != (2, 2):
        raise ValueError("I4 tadpole requires two background and two quantum ports")
    graph_id = f"CQ-I4-TADPOLE-{number:03d}"
    half_edge = {str(port["port_id"]): f"{graph_id}__h{position}" for position, port in enumerate(ports)}
    source_half_edge = f"{graph_id}__source"
    momentum_by_port = {
        str(backgrounds[0]["port_id"]): "-p",
        str(backgrounds[1]["port_id"]): "-q",
        str(quantum[0]["port_id"]): "k",
        str(quantum[1]["port_id"]): "-k",
    }
    half_edges: list[HalfEdge] = []
    for position, port in enumerate(ports):
        field = V_FIELD if port["role"] == "QUANTUM_WICK" else pending_projection_field(port)
        half_edges.append(
            HalfEdge(
                half_edge[str(port["port_id"])],
                "vI4",
                position,
                field,
                Flow.IN if port["role"] == "BACKGROUND_EXTERNAL" else Flow.NONE,
                momentum_by_port[str(port["port_id"])],
            )
        )
    half_edges.append(
        HalfEdge(source_half_edge, "vI4", len(ports), SOURCE_FIELD, Flow.IN, "p+q")
    )
    term = source_terms[str(row["source_term_id"])]
    source_coefficient = ExactMonomial.from_project_json(row["source_coefficient"])
    known_coefficient = source_coefficient * PROPAGATOR_COEFFICIENT
    graph = GraphIR(
        graph_id=graph_id,
        vertices=(
            Vertex(
                "vI4",
                "COMPOSITE_I4_TWO_BACKGROUND_TWO_QUANTUM",
                tuple(half_edge[str(port["port_id"])] for port in ports) + (source_half_edge,),
                str(row["source_coefficient"]["rendered"]),
                (f"AST[{term['expression_sha256']}]",),
                "theta_I",
                "delta(-p-q+k-k+(p+q))",
                coefficient_factors=(
                    str(row["source_coefficient"]["rendered"]),
                    "BQ_split_multiplicity=1",
                ),
            ),
        ),
        half_edges=tuple(half_edges),
        internal_edges=(
            InternalEdge(
                "e0",
                half_edge[str(quantum[0]["port_id"])],
                half_edge[str(quantum[1]["port_id"])],
                "-2*g^2*kappa^-1*delta4theta/k^2",
                "k",
                Flow.NONE,
            ),
        ),
        external_legs=(
            ExternalLeg(
                "background_0_projection_pending",
                half_edge[str(backgrounds[0]["port_id"])],
                pending_projection_field(backgrounds[0]),
                "p",
                f"Color[{backgrounds[0]['port_id']}]",
            ),
            ExternalLeg(
                "background_1_projection_pending",
                half_edge[str(backgrounds[1]["port_id"])],
                pending_projection_field(backgrounds[1]),
                "q",
                f"Color[{backgrounds[1]['port_id']}]",
            ),
            ExternalLeg("WW_source", source_half_edge, SOURCE_FIELD, "p+q", "A,B"),
        ),
        loop_momenta=("k",),
        metadata=tuple(
            sorted(
                {
                    "family": "I4_TADPOLE",
                    "graph_status": "PARTIALLY_TYPED_PENDING_WW_EXTERNAL_PROJECTION",
                    "assignment": str(row["assignment_id"]),
                    "wick_sign": "+1",
                    "koszul_sign": "+1",
                    "symmetry_factor": "OPEN_TYPED_AUTOMORPHISM_AUDIT",
                    "typed_automorphism_order": "OPEN_TYPED_AUTOMORPHISM_AUDIT",
                    "normal_ordering_admission": "OPEN",
                    "denominator_external_scale": "NONE_BY_EXACT_ROUTING",
                    "known_coefficient": known_coefficient.render(),
                }.items()
            )
        ),
    )
    graph.assert_linear_momentum_routing()
    signature = {
        "family": "I4_TADPOLE",
        "I4_source_ast": term["expression_sha256"],
        "background_positions": [port_index(ports, str(port["port_id"])) for port in backgrounds],
        "quantum_positions": [port_index(ports, str(port["port_id"])) for port in quantum],
        "derivative_scopes": [port["derivative_word_outer_to_inner"] for port in ports],
        "self_pairing_positions": [
            port_index(ports, str(quantum[0]["port_id"])),
            port_index(ports, str(quantum[1]["port_id"])),
        ],
    }
    class_id, signature_hash = decorated_class_id("DGC-I4", signature)
    return {
        "labeled_graph_id": graph_id,
        "decorated_graph_class_id": class_id,
        "physical_graph_class_status": "OPEN_TYPED_AUTOMORPHISM_COLOR_DWORD_CANONICALIZATION",
        "canonical_signature_sha256": signature_hash,
        "canonical_signature": signature,
        "graph_ir": graph.canonical_dict(),
        "source_term_binding": {
            "term_id": term["term_id"],
            "expression_sha256": term["expression_sha256"],
        },
        "port_provenance": graph_port_provenance(row),
        "color_provenance": {
            "I4_color_bracket_word": row["color_bracket_word"],
            "self_contraction": (
                f"kappa^-1[Color[{quantum[0]['port_id']}],Color[{quantum[1]['port_id']}]]"
            ),
            "full_color_tensor_reduction": "OPEN_AST_TO_INDEX_TENSOR_COMPILER",
        },
        "pairing": {
            "declared_quantum_field_word": [port["port_id"] for port in quantum],
            "pair": [quantum[0]["port_id"], quantum[1]["port_id"]],
            "statistics": ["BOSON", "BOSON"],
            "fermion_crossings": 0,
            "koszul_sign": 1,
            "wick_sign": 1,
            "labeled_pairing_multiplicity": 1,
        },
        "coefficient_provenance": {
            "I4_source": source_coefficient.as_json(),
            "one_propagator": PROPAGATOR_COEFFICIENT.as_json(),
            "BQ_split_multiplicity": 1,
            "Wick_sign": 1,
            "Koszul_sign": 1,
            "typed_automorphism_order_audit": "OPEN",
            "automorphism_division_applied": False,
            "known_product_excluding_open_factors": known_coefficient.as_json(),
            "open_factors": [
                "NORMAL_ORDERING_SELF_CONTRACTION_ADMISSION",
                "TYPED_AUTOMORPHISM_AND_SYMMETRY_AUDIT",
            ],
        },
        "routing_classification": {
            "loop_edge_momentum": "k",
            "denominator": "k^2",
            "external_momentum_in_denominator": False,
            "status": "SCALELESS_DENOMINATOR_ROUTING_PROVED; D_ALGEBRA_NUMERATOR_NOT_REDUCED",
        },
        "external_projection_status": "OPEN_I4_BACKGROUND_PORTS_NOT_MAPPED_TO_X_AND_TILDEW",
        "classification": "ENUMERATED_PARTIAL_GRAPH; PHYSICAL_WW_PROJECTION_NOT_CLOSED",
    }


def quotient_payload(
    bubbles: Sequence[Mapping[str, object]],
    tadpoles: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    representatives = {
        "CR-I3S3-BUBBLE-X-TILDEW": {
            "topology": "TWO_VERTICES_TWO_PARALLEL_V_EDGES",
            "loop_rank": 1,
            "external_targets": ["X=nabla_+W_+", "TildeW_dot_alpha", "WW_source"],
            "status": "STRUCTURAL_COLLAPSED_REPRESENTATIVE_ONLY",
        },
        "CR-I4-ONE-V-TADPOLE": {
            "topology": "ONE_VERTEX_ONE_V_SELF_EDGE",
            "loop_rank": 1,
            "external_targets": ["PROJECTION_PENDING", "PROJECTION_PENDING", "WW_source"],
            "status": "STRUCTURAL_COLLAPSED_REPRESENTATIVE_ONLY",
        },
    }
    maps: list[dict[str, object]] = []
    for record in bubbles:
        maps.append(
            {
                "domain_decorated_graph_class_id": record["decorated_graph_class_id"],
                "domain_labeled_graph_id": record["labeled_graph_id"],
                "codomain_representative_id": "CR-I3S3-BUBBLE-X-TILDEW",
                "preserved": ["loop_rank", "source_momentum", "external_target_inventory"],
                "forgotten_but_retained_in_domain": [
                    "ordered_port_ids",
                    "derivative_scopes",
                    "color_AST",
                    "pairing_permutation",
                    "source_coefficients",
                ],
                "coefficient_transport": "NOT_PERFORMED",
            }
        )
    for record in tadpoles:
        maps.append(
            {
                "domain_decorated_graph_class_id": record["decorated_graph_class_id"],
                "domain_labeled_graph_id": record["labeled_graph_id"],
                "codomain_representative_id": "CR-I4-ONE-V-TADPOLE",
                "preserved": ["loop_rank", "source_momentum", "unresolved_external_count"],
                "forgotten_but_retained_in_domain": [
                    "ordered_port_ids",
                    "derivative_scopes",
                    "color_AST",
                    "source_coefficients",
                ],
                "coefficient_transport": "NOT_PERFORMED",
            }
        )
    return {
        "map_type": "SURJECTIVE_STRUCTURAL_QUOTIENT_NOT_AMPLITUDE_IDENTITY",
        "representatives": representatives,
        "maps": maps,
        "fiber_counts": {
            representative: sum(row["codomain_representative_id"] == representative for row in maps)
            for representative in representatives
        },
        "aggregate_coefficient_inserted": False,
        "linear_sum_over_fibers_proved": False,
    }


def proof_obligations() -> list[dict[str, object]]:
    return [
        {
            "id": "OPEN_CONTACT_001",
            "severity": "P1",
            "statement": "Compile every joined derivative word through edge-tagged D-algebra and bind the external X/TildeW projector normalization and extraction sign.",
            "blocks": "basis-resolved amplitude coefficients",
        },
        {
            "id": "OPEN_CONTACT_002",
            "severity": "P1",
            "statement": "Compile each retained source color AST and kappa inverse edge contraction to an explicit free-index color tensor.",
            "blocks": "color-canonical graph merging",
        },
        {
            "id": "OPEN_CONTACT_003",
            "severity": "P1",
            "statement": "Bind the Euclidean path-integral action-vertex expansion factor to the S3 source coefficient without importing the legacy aggregate sign.",
            "blocks": "complete I3 x S3 coefficient",
        },
        {
            "id": "OPEN_CONTACT_004",
            "severity": "P1",
            "statement": "Resolve the two I4 background ports into the ordered WW external target pair after D-algebra.",
            "blocks": "fully typed I4 WW GraphIR",
        },
        {
            "id": "OPEN_CONTACT_005",
            "severity": "P1",
            "statement": "Fix the composite normal-ordering policy for the 180 I4 self-contractions.",
            "blocks": "I4 graph admission",
        },
        {
            "id": "OPEN_CONTACT_006",
            "severity": "P1",
            "statement": "Prove the linear amplitude identity over each structural quotient fiber; no coefficient transport is currently asserted.",
            "blocks": "explicit-contact to collapsed-representative equality",
        },
        {
            "id": "OPEN_CONTACT_007",
            "severity": "P1",
            "statement": "Bind basis graph classes to DIRECT/REFLECTED and the eight edge-tagged trace channels.",
            "blocks": "ordinary contact-family pole comparison",
        },
        {
            "id": "OPEN_CONTACT_008",
            "severity": "P1",
            "statement": "Compute the typed automorphism group after color and derivative-word canonicalization; only then fix any separate symmetry factor.",
            "blocks": "physical graph classes and symmetry factors",
        },
    ]


def build_payload() -> dict[str, object]:
    base = seed_port_assignment_payload()
    selected = base["selected_for_seed"]
    all_assignments = base["all_ordered_assignments"]
    if not isinstance(selected, dict) or not isinstance(all_assignments, dict):
        raise TypeError("invalid Project seed port payload")

    i3_rows = joined_projected_rows(
        selected["I3_one_background_two_quantum"], all_assignments["I3"]
    )
    s3_rows = joined_projected_rows(
        selected["S3_antichiral_one_background_two_quantum"],
        all_assignments["S3_GAUGE_ANTICHIRAL"],
    )
    i4_rows = selected["I4_two_background_two_quantum_tadpole"]
    if not isinstance(i4_rows, list):
        raise TypeError("I4 selection must be a list")

    terms = (
        *insertion_terms_at_valence(3),
        *antichiral_gauge_s3_terms(),
        *insertion_terms_at_valence(4),
    )
    source_terms = {term.term_id: source_term_record(term) for term in terms}
    i4_assignment_by_id = {
        str(row["assignment_id"]): row for row in all_assignments["I4"]
    }

    bubbles = [
        bubble_graph_record(i_number, s_number, pairing_number, i_row, s_row, source_terms)
        for i_number, i_row in enumerate(i3_rows, start=1)
        for s_number, s_row in enumerate(s3_rows, start=1)
        for pairing_number in (1, 2)
    ]
    joined_i4_rows: list[dict[str, object]] = []
    for row in i4_rows:
        assignment = i4_assignment_by_id[str(row["assignment_id"])]
        color_word = assignment["color_bracket_word"]
        if not isinstance(color_word, list) or not color_word:
            raise TypeError("I4 color word must be a list")
        if row["ordered_ports"] != assignment["ordered_ports"]:
            raise ValueError("selected I4 row disagrees with its source assignment")
        joined_i4_rows.append(
            {
                **dict(row),
                "color_bracket_word": color_word,
                "source_family": assignment["source_family"],
                "coefficient_changed_by_split": assignment["coefficient_changed_by_split"],
            }
        )
    tadpoles = [
        tadpole_graph_record(number, row, source_terms)
        for number, row in enumerate(joined_i4_rows, start=1)
    ]

    quotient = quotient_payload(bubbles, tadpoles)
    return {
        "schema": 1,
        "scope": "STEP5_WW_BASIS_RESOLVED_CONTACT_PHYSICALIZATION",
        "authority_status": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "imports": [
            "scripts.step5_project_composites.seed_port_assignment_payload",
            "scripts.step5_project_composites source CompositeTerm ASTs",
            "scripts.step5_graph_ir",
        ],
        "aggregate_contact_result_imported": False,
        "pole_or_anomaly_coefficient_computed": False,
        "source_terms": source_terms,
        "basis": {
            "joined_I3_rows": i3_rows,
            "joined_S3_antichiral_rows": s3_rows,
            "joined_I4_rows": joined_i4_rows,
        },
        "counts": {
            "I3_rows": len(i3_rows),
            "S3_antichiral_rows": len(s3_rows),
            "I3_x_S3_ordered_vertex_pairs": len(i3_rows) * len(s3_rows),
            "I3_x_S3_labeled_Wick_pairings": len(bubbles),
            "I3_x_S3_decorated_graph_classes": len({row["decorated_graph_class_id"] for row in bubbles}),
            "I4_labeled_Wick_pairings": len(tadpoles),
            "I4_decorated_partial_graph_classes": len({row["decorated_graph_class_id"] for row in tadpoles}),
            "physical_graph_class_canonicalization": "OPEN",
        },
        "I3_x_S3_graphs": bubbles,
        "I4_tadpole_graphs": tadpoles,
        "quotient": quotient,
        "open_proof_obligations": proof_obligations(),
    }


def recursive_values(value: object) -> Iterable[object]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from recursive_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from recursive_values(child)


def build_audit(payload: Mapping[str, object]) -> dict[str, object]:
    counts = payload["counts"]
    bubbles = payload["I3_x_S3_graphs"]
    tadpoles = payload["I4_tadpole_graphs"]
    quotient = payload["quotient"]
    source_terms = payload["source_terms"]
    if not isinstance(counts, dict) or not isinstance(bubbles, list) or not isinstance(tadpoles, list):
        raise TypeError("invalid contact payload")
    if not isinstance(quotient, dict) or not isinstance(source_terms, dict):
        raise TypeError("invalid quotient payload")
    all_graphs = bubbles + tadpoles
    forbidden_fragments = ("1024*pi", "128*pi", "64*pi", "anomaly_coefficient")
    checks = {
        "I3_count_30": counts["I3_rows"] == 30,
        "S3_count_6": counts["S3_antichiral_rows"] == 6,
        "ordered_vertex_pairs_180": counts["I3_x_S3_ordered_vertex_pairs"] == 180,
        "bubble_pairings_360": counts["I3_x_S3_labeled_Wick_pairings"] == 360,
        "I4_pairings_180": counts["I4_labeled_Wick_pairings"] == 180,
        "every_graph_has_unique_id": len({row["labeled_graph_id"] for row in all_graphs}) == 540,
        "every_graph_has_unique_decorated_class": len({row["decorated_graph_class_id"] for row in all_graphs}) == 540,
        "physical_graph_canonicalization_remains_open": counts["physical_graph_class_canonicalization"] == "OPEN"
        and all(
            row["physical_graph_class_status"]
            == "OPEN_TYPED_AUTOMORPHISM_COLOR_DWORD_CANONICALIZATION"
            for row in all_graphs
        ),
        "source_is_fermionic": all(
            next(
                leg for leg in row["graph_ir"]["external_legs"] if leg["leg_id"] == "WW_source"
            )["field_type"]["statistics"]
            == "FERMION"
            for row in all_graphs
        ),
        "X_descendant_not_claimed_chiral": all(
            next(
                leg for leg in row["graph_ir"]["external_legs"] if leg["leg_id"] == "X_external"
            )["field_type"]["chirality"]
            == "UNCONSTRAINED"
            for row in bubbles
        ),
        "symmetry_and_automorphism_are_open": all(
            row["graph_ir"]["metadata"]["symmetry_factor"]
            == row["graph_ir"]["metadata"]["typed_automorphism_order"]
            == "OPEN_TYPED_AUTOMORPHISM_AUDIT"
            for row in all_graphs
        ),
        "all_bubble_routes_pass": all(
            serialized_graph_routing_passes(row["graph_ir"]) for row in bubbles
        ),
        "all_tadpole_routes_pass": all(
            serialized_graph_routing_passes(row["graph_ir"]) for row in tadpoles
        ),
        "all_derivative_scopes_retained": all(
            all(
                "derivative_word_outer_to_inner" in port
                and port["derivative_scope_classification"]
                in ("ORDERED_DERIVATIVE_WORD", "IDENTITY_NO_DERIVATIVE")
                for family in row["port_provenance"].values()
                for port in family
            )
            for row in bubbles
        ) and all(
            all(
                "derivative_word_outer_to_inner" in port
                and port["derivative_scope_classification"]
                in ("ORDERED_DERIVATIVE_WORD", "IDENTITY_NO_DERIVATIVE")
                for port in row["port_provenance"]
            )
            for row in tadpoles
        ),
        "all_color_provenance_retained": all(
            row["color_provenance"]["I3_color_bracket_word"]
            and row["color_provenance"]["S3_color_bracket_word"]
            for row in bubbles
        ) and all(row["color_provenance"]["I4_color_bracket_word"] for row in tadpoles),
        "all_source_AST_hash_bindings_resolve": all(
            all(
                binding["term_id"] in source_terms
                and source_terms[binding["term_id"]]["expression_sha256"]
                == binding["expression_sha256"]
                for binding in row["source_term_bindings"].values()
            )
            for row in bubbles
        ) and all(
            row["source_term_binding"]["term_id"] in source_terms
            and source_terms[row["source_term_binding"]["term_id"]]["expression_sha256"]
            == row["source_term_binding"]["expression_sha256"]
            for row in tadpoles
        ),
        "all_wick_koszul_signs_plus_one": all(
            row["pairing"]["wick_sign"] == row["pairing"]["koszul_sign"] == 1
            for row in all_graphs
        ),
        "quotient_covers_domain_once": len(quotient["maps"]) == 540
        and len({row["domain_decorated_graph_class_id"] for row in quotient["maps"]}) == 540,
        "quotient_fibers_exact": quotient["fiber_counts"]
        == {"CR-I3S3-BUBBLE-X-TILDEW": 360, "CR-I4-ONE-V-TADPOLE": 180},
        "quotient_has_no_coefficient_transport": all(
            row["coefficient_transport"] == "NOT_PERFORMED" for row in quotient["maps"]
        ),
        "aggregate_result_not_imported": payload["aggregate_contact_result_imported"] is False,
        "no_pole_or_anomaly_coefficient": payload["pole_or_anomaly_coefficient_computed"] is False
        and not any(
            isinstance(value, str) and any(fragment in value for fragment in forbidden_fragments)
            for value in recursive_values(payload)
        ),
        "open_obligations_are_machine_readable": len(payload["open_proof_obligations"]) == 8
        and all(row["id"].startswith("OPEN_CONTACT_") for row in payload["open_proof_obligations"]),
    }
    return {
        "schema": 1,
        "scope": payload["scope"],
        "status": "PASS_WITH_OPEN_PROOF_OBLIGATIONS" if all(checks.values()) else "FAIL",
        "checks": [{"id": key, "passed": value} for key, value in sorted(checks.items())],
        "totals": {"checks": len(checks), "failed": sum(not value for value in checks.values())},
        "open_proof_obligation_ids": [row["id"] for row in payload["open_proof_obligations"]],
    }


def serialized_graph_routing_passes(graph: Mapping[str, object]) -> bool:
    """Independent exact routing check on serialized GraphIR momenta."""

    from scripts.step5_graph_ir import parse_linear_momentum

    def add(expressions: Iterable[str]) -> dict[str, int]:
        result: dict[str, int] = {}
        for expression in expressions:
            for symbol, coefficient in parse_linear_momentum(expression):
                result[symbol] = result.get(symbol, 0) + coefficient
        return {key: value for key, value in result.items() if value}

    half_edges = {row["half_edge_id"]: row for row in graph["half_edges"]}
    for edge in graph["internal_edges"]:
        left = half_edges[edge["left_half_edge"]]["momentum"]
        right = half_edges[edge["right_half_edge"]]["momentum"]
        if add((left, right)):
            return False
        if dict(parse_linear_momentum(left)) != dict(parse_linear_momentum(edge["momentum"])):
            return False
    for vertex in graph["vertices"]:
        if add(half_edges[item]["momentum"] for item in vertex["ordered_half_edges"]):
            return False
    return True


def markdown_report(payload: Mapping[str, object]) -> str:
    counts = payload["counts"]
    lines = [
        "# Step 5 WW contact quotient",
        "",
        "$$",
        r"N_{I_3}=30,\qquad N_{\widetilde S_3}=6,\qquad N_{\mathrm{pair}}=30\cdot6\cdot2=360.",
        "$$",
        "",
        "$$",
        r"N_{I_4}=180,\qquad k+(-k)=0.",
        "$$",
        "",
        "$$",
        r"r_0=k,\qquad r_1=q-k,\qquad (-p)+(-k)+(k-q)+(p+q)=0.",
        "$$",
        "",
        f"Decorated classes: {counts['I3_x_S3_decorated_graph_classes']} bubble, {counts['I4_decorated_partial_graph_classes']} tadpole; physical canonicalization is open.",
        "",
        "The quotient is structural only:",
        "",
        "$$",
        r"\mathcal G_{360}\twoheadrightarrow R_{I_3\widetilde S_3},\qquad \mathcal T_{180}\twoheadrightarrow R_{I_4};\qquad C_{\rm fiber}\ \text{not evaluated}.",
        "$$",
        "",
        "## Open proof obligations",
        "",
    ]
    for row in payload["open_proof_obligations"]:
        lines.append(f"- `{row['id']}`: {row['statement']}")
    lines.append("")
    return "\n".join(lines)


def write_outputs(payload: Mapping[str, object], audit: Mapping[str, object]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ww-contact-quotient.json").write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    )
    (OUT / "ww-contact-quotient.md").write_text(markdown_report(payload))
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, sort_keys=True, indent=2) + "\n")


def main() -> int:
    payload = build_payload()
    audit = build_audit(payload)
    write_outputs(payload, audit)
    print(json.dumps({"counts": payload["counts"], "audit": audit["totals"]}, sort_keys=True))
    return 0 if audit["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
