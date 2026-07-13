#!/usr/bin/env python3
"""Typed Step-6 join from Project AST terms to two literal K4-minus-edge parents.

This compiler is proposal-only.  It admits exactly the ``I3 S3^3`` and
``I2 S3^2 S4`` topology records already constructed by the Step-6 topology
compiler.  It preserves every Project term and background/quantum split, then
represents all labeled Wick contractions as an exact factorized Cartesian
product with deterministic mixed-radix rank/unrank.

No external-background projection, propagator, D-algebra, amplitude,
subtraction, or coefficient is inferred here.
"""

from __future__ import annotations

import ast as py_ast
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, prod
import json
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence

try:
    from scripts import step6_two_loop_grammar as grammar
    from scripts import step6_two_loop_graphir as graphir
except ModuleNotFoundError:  # direct execution: python scripts/step6_two_loop_wick.py
    import step6_two_loop_grammar as grammar
    import step6_two_loop_graphir as graphir


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/two-loop-wick"
GENERATED_JSON = GENERATED_DIR / "typed-wick-join.json"
GENERATED_MD = GENERATED_DIR / "typed-wick-join.md"
AUDIT = ROOT / "audits/step6-two-loop-wick-verification.json"

SCHEMA_VERSION = "step6.two_loop_wick.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
EXTERNAL_PROJECTION_STATUS = grammar.EXTERNAL_PROJECTION_STATUS
PROPAGATOR_STATUS = "BLOCKED_PROJECT_VECTOR_PROPAGATOR_ATTACHMENT_NOT_COMPILED"
DALGEBRA_STATUS = "BLOCKED_EDGE_TAGGED_DALGEBRA_NOT_COMPILED"
AMPLITUDE_STATUS = "BLOCKED_PROPAGATOR_AND_DALGEBRA_IR_ABSENT"
SUBTRACTION_STATUS = "BLOCKED_AMPLITUDE_AND_FOREST_JOIN_ABSENT"
COEFFICIENT_STATUS = "BLOCKED_RENORMALIZED_AMPLITUDE_IR_ABSENT"
CHIRALITY_ZERO_STATUS = "UNPROVED_NO_MEASURE_SATURATION_OR_DALGEBRA_CERTIFICATE"

SUPPORTED_FAMILIES = {
    "I3__S3^3": "I3_S3_CUBED",
    "I2__S3^2__S4^1": "I2_S3_SQUARED_S4",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def duplicate_literal_dict_keys(path: Path) -> list[dict[str, Any]]:
    tree = py_ast.parse(path.read_text())
    duplicates: list[dict[str, Any]] = []
    for node in py_ast.walk(tree):
        if not isinstance(node, py_ast.Dict):
            continue
        keys = [
            key.value
            for key in node.keys
            if isinstance(key, py_ast.Constant) and isinstance(key.value, str)
        ]
        repeated = sorted({key for key in keys if keys.count(key) > 1})
        if repeated:
            duplicates.append({"line": node.lineno, "keys": repeated})
    return duplicates


def exact_fraction(value: Fraction) -> dict[str, Any]:
    value = Fraction(value)
    return {
        "field": "Q",
        "numerator": value.numerator,
        "denominator": value.denominator,
        "rendered": (
            str(value.numerator)
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        ),
    }


def term_chirality(term: Mapping[str, Any]) -> dict[str, str]:
    measure = term["measure"]
    tags = set(term["tags"])
    if measure == "E_PLUS_CHIRAL" and "CHIRAL_EUCLIDEAN_SECTOR" in tags:
        return {
            "class": "CHIRAL_EUCLIDEAN_SECTOR",
            "source": "measure_and_term_tag",
        }
    if measure == "E_MINUS_ANTICHIRAL" and "ANTICHIRAL_EUCLIDEAN_SECTOR" in tags:
        return {
            "class": "ANTICHIRAL_EUCLIDEAN_SECTOR",
            "source": "measure_and_term_tag",
        }
    if measure == "LOCAL_OPERATOR_INSERTION":
        return {
            "class": "LOCAL_INSERTION_CHIRALITY_UNRESOLVED",
            "source": "measure_only_no_inference",
        }
    return {"class": "UNRESOLVED", "source": "no_project_certificate"}


def term_dictionary_row(term: Mapping[str, Any]) -> dict[str, Any]:
    expression_ast = term["expression_ast"]
    color_ast = term["color_ast"]
    row = {
        "term_id": term["term_id"],
        "family": term["family"],
        "t": term["degree"]["total_v"],
        "unassigned_degree": term["degree"],
        "grassmann_parity": term["parity"],
        "measure": term["measure"],
        "chirality": term_chirality(term),
        "coefficient_raw": term["coefficient"],
        "ports": term["ports"],
        "color_ast": color_ast,
        "expression_ast": expression_ast,
        "source_equations": term["source_equations"],
        "tags": term["tags"],
        "status": term["status"],
        "color_ast_sha256": digest(color_ast),
        "expression_ast_sha256": digest(expression_ast),
    }
    row["term_record_sha256"] = digest(row)
    return row


def selected_terms(grammar_payload: Mapping[str, Any]) -> dict[str, list[dict[str, Any]]]:
    insertions = grammar_payload["insertions"]
    actions = grammar_payload["gauge_action_vertices"]
    selected = {
        "I2": list(insertions["I2"]),
        "I3": list(insertions["I3"]),
        "S3": sorted(
            [*actions["S3_PLUS"], *actions["S3_MINUS"]],
            key=lambda term: term["term_id"],
        ),
        "S4": sorted(
            [*actions["S4_PLUS"], *actions["S4_MINUS"]],
            key=lambda term: term["term_id"],
        ),
    }
    expected = {"I2": 2, "I3": 10, "S3": 4, "S4": 6}
    actual = {family: len(terms) for family, terms in selected.items()}
    if actual != expected:
        raise ValueError(f"Project term census changed: expected {expected}, found {actual}")
    return selected


def edge_endpoint_index(graph: Mapping[str, Any], orientation: str) -> dict[str, dict[str, Any]]:
    base_edges = {edge["edge_id"]: edge for edge in graph["internal_edges"]}
    oriented_edges = {
        edge["edge_id"]: edge for edge in graph["orientations"][orientation]["edges"]
    }
    index: dict[str, dict[str, Any]] = {}
    for edge_id, base in base_edges.items():
        oriented = oriented_edges[edge_id]
        base_port_by_vertex = {
            base["source"]: base["source_port"],
            base["target"]: base["target_port"],
        }
        for endpoint_role in ("source", "target"):
            vertex_id = oriented[endpoint_role]
            topology_port_id = base_port_by_vertex[vertex_id]
            if topology_port_id in index:
                raise ValueError(f"topology port {topology_port_id} occurs on two edges")
            index[topology_port_id] = {
                "edge_id": edge_id,
                "orientation": orientation,
                "orientation_endpoint": endpoint_role,
                "vertex_id": vertex_id,
                "topology_port_id": topology_port_id,
                "momentum": oriented["momentum"],
                "momentum_vector": oriented["momentum_vector"],
            }
    return index


def background_quantum_assignments(
    term: Mapping[str, Any], vertex: Mapping[str, Any]
) -> list[dict[str, Any]]:
    ports = term["ports"]
    t = len(ports)
    b = vertex["background_valence"]
    q = vertex["quantum_valence"]
    if t != vertex["total_valence"] or t != b + q:
        return []
    topology_background_ports = [port["port_id"] for port in vertex["background_ports"]]
    if len(topology_background_ports) != b:
        raise ValueError("topology background port list does not match background valence")
    rows: list[dict[str, Any]] = []
    ordinal = 0
    for background_indices in combinations(range(t), b):
        background_index_set = set(background_indices)
        background_ports = [ports[index] for index in background_indices]
        quantum_ports = [ports[index] for index in range(t) if index not in background_index_set]
        for target_permutation in permutations(topology_background_ports):
            ordinal += 1
            labeled_background_bijection = [
                {
                    "grammar_port_id": source["port_id"],
                    "grammar_port_occurrence_id": (
                        f"{vertex['vertex_id']}::{source['port_id']}"
                    ),
                    "topology_background_port_id": target,
                }
                for source, target in zip(
                    background_ports, target_permutation, strict=True
                )
            ]
            background_projection_join = {
                "status": EXTERNAL_PROJECTION_STATUS,
                "value": None,
                "labeled_background_port_bijection": labeled_background_bijection,
                "bijection_is_enumerated": True,
                "component_or_letter_projection_is_not_inferred": True,
            }
            assignment_id = f"{vertex['vertex_id']}::{term['term_id']}::BQ{ordinal:03d}"
            rows.append(
                {
                    "assignment_id": assignment_id,
                    "vertex_id": vertex["vertex_id"],
                    "source_term_id": term["term_id"],
                    "t": t,
                    "b": b,
                    "q": q,
                    "degree_identity": t == b + q,
                    "grassmann_parity": term["parity"],
                    "measure": term["measure"],
                    "chirality": term_chirality(term),
                    "color_ast_ref": term["term_id"],
                    "color_ast_sha256": digest(term["color_ast"]),
                    "expression_ast_ref": term["term_id"],
                    "expression_ast_sha256": digest(term["expression_ast"]),
                    "coefficient_raw": term["coefficient"],
                    "background_grammar_ports": background_ports,
                    "quantum_grammar_ports": quantum_ports,
                    "background_projection_join": background_projection_join,
                    "external_projection": EXTERNAL_PROJECTION_STATUS,
                    "chirality_zero_inference": CHIRALITY_ZERO_STATUS,
                }
            )
    return rows


def local_wick_options(
    graph: Mapping[str, Any],
    orientation: str,
    vertex: Mapping[str, Any],
    terms: Sequence[Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    endpoint_index = edge_endpoint_index(graph, orientation)
    assignments: list[dict[str, Any]] = []
    options: list[dict[str, Any]] = []
    topology_quantum_ports = tuple(vertex["quantum_ports"])
    for term in terms:
        for assignment in background_quantum_assignments(term, vertex):
            assignments.append(assignment)
            grammar_quantum_ports = assignment["quantum_grammar_ports"]
            for permutation_ordinal, target_permutation in enumerate(
                permutations(topology_quantum_ports), start=1
            ):
                attachments = []
                for grammar_port, topology_port_id in zip(
                    grammar_quantum_ports, target_permutation, strict=True
                ):
                    endpoint = endpoint_index[topology_port_id]
                    attachments.append(
                        {
                            "grammar_port_id": grammar_port["port_id"],
                            "grammar_port_occurrence_id": (
                                f"{vertex['vertex_id']}::{grammar_port['port_id']}"
                            ),
                            "grammar_port_parity": grammar_port["parity"],
                            "grammar_derivative_word_outer_to_inner": grammar_port[
                                "derivative_word_outer_to_inner"
                            ],
                            **endpoint,
                        }
                    )
                option_id = (
                    f"{orientation}::{assignment['assignment_id']}::"
                    f"P{permutation_ordinal:03d}"
                )
                option = {
                    "local_option_id": option_id,
                    "orientation": orientation,
                    "vertex_id": vertex["vertex_id"],
                    "source_term_id": term["term_id"],
                    "assignment_id": assignment["assignment_id"],
                    "t": assignment["t"],
                    "b": assignment["b"],
                    "q": assignment["q"],
                    "grassmann_parity": term["parity"],
                    "measure": term["measure"],
                    "chirality": assignment["chirality"],
                    "color_ast_ref": term["term_id"],
                    "color_ast_sha256": assignment["color_ast_sha256"],
                    "expression_ast_ref": term["term_id"],
                    "expression_ast_sha256": assignment["expression_ast_sha256"],
                    "coefficient_raw": term["coefficient"],
                    "background_projection_join": assignment["background_projection_join"],
                    "quantum_attachment": attachments,
                    "quantum_bijection": (
                        len(attachments) == len(topology_quantum_ports)
                        and {item["topology_port_id"] for item in attachments}
                        == set(topology_quantum_ports)
                        and len({item["grammar_port_id"] for item in attachments})
                        == len(attachments)
                    ),
                    "wick_field_statistics_sign": {
                        "value": 1,
                        "certificate": "ALL_CONTRACTED_FIELDS_ARE_PARITY_ZERO_V_PORTS",
                    },
                    "derivative_transfer_and_ibp_sign": "UNCOMPUTED_DALGEBRA_STAGE",
                    "propagator": None,
                    "propagator_status": PROPAGATOR_STATUS,
                }
                option["local_option_sha256"] = digest(option)
                options.append(option)
    assignments.sort(key=lambda row: row["assignment_id"])
    options.sort(key=lambda row: row["local_option_id"])
    return assignments, options


def action_sector(term_id: str) -> str | None:
    if term_id.startswith("S") and "_PLUS_" in term_id:
        return "PLUS"
    if term_id.startswith("S") and "_MINUS_" in term_id:
        return "MINUS"
    return None


def expansion_factor(family_sector_multiplicities: Mapping[str, int]) -> dict[str, Any]:
    """Raw multinomial coefficient before decorated-role embeddings.

    This grouped record is retained only for the sector census.  It is not the
    coefficient of one fixed decorated GraphIR row: assigning the selected
    interaction occurrences to the fixed topology roles supplies the matching
    factorials, followed by the external-source-labeled topology quotient.
    """
    multiplicities = {
        key: int(value)
        for key, value in sorted(family_sector_multiplicities.items())
        if value
    }
    if any(value < 0 for value in multiplicities.values()):
        raise ValueError("action multiplicities cannot be negative")
    n_action = sum(multiplicities.values())
    denominator = prod(factorial(value) for value in multiplicities.values())
    rational = Fraction((-1) ** n_action, denominator)
    n_plus = sum(value for key, value in multiplicities.items() if key.endswith("_PLUS"))
    n_minus = sum(value for key, value in multiplicities.items() if key.endswith("_MINUS"))
    factorial_word = "*".join(
        f"{value}!_[{key}]" for key, value in multiplicities.items()
    ) or "1"
    return {
        "source": "exp[-sum_(r,sector) S_(r,sector)/hbar]",
        "N": n_action,
        "n_plus": n_plus,
        "n_minus": n_minus,
        "family_sector_multiplicities": multiplicities,
        "factorial_denominator": denominator,
        "rational": exact_fraction(rational),
        "hbar_power": -n_action,
        "rendered": (
            f"(-1)^{n_action}/({factorial_word}*hbar^{n_action})"
        ),
        "kept_separate_from_raw_action_coefficients": True,
        "physical_decorated_graph_coefficient": (
            "NOT_THIS_RAW_FACTOR_USE_DECORATED_OCCURRENCE_ORBIT_FACTOR"
        ),
    }


def decorated_occurrence_orbit_factor(
    graph: Mapping[str, Any], action_options: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    """Exact exponential/occurrence/automorphism weight of one labeled row.

    A shifted interaction monomial is fixed by ``assignment_id``.  If it occurs
    ``n_tau`` times, the exponential contributes ``1/n_tau!`` while its
    occurrence-to-decorated-role embeddings contribute ``n_tau!``.  The
    remaining quotient is the external-source-labeled topology automorphism.
    """

    multiplicities = Counter(
        f"{option['source_term_id']}::{option['assignment_id']}"
        for option in action_options
    )
    n_action = sum(multiplicities.values())
    source_denominator = prod(factorial(value) for value in multiplicities.values())
    role_embedding_count = source_denominator
    automorphism_order = int(
        graph["automorphisms"]["background_source_labeled"]["order"]
    )
    if automorphism_order <= 0:
        raise ValueError("topology automorphism order must be positive")
    source_rational = Fraction((-1) ** n_action, source_denominator)
    embedding_rational = Fraction(role_embedding_count, automorphism_order)
    combined = source_rational * embedding_rational
    if combined != Fraction((-1) ** n_action, automorphism_order):
        raise AssertionError("decorated occurrence-orbit cancellation failed")
    return {
        "source_interaction_monomial_multiplicities": dict(sorted(multiplicities.items())),
        "N": n_action,
        "source_exponential_factor": {
            "rational": exact_fraction(source_rational),
            "hbar_power": -n_action,
            "factorial_denominator": source_denominator,
        },
        "occurrence_to_decorated_role_embeddings": role_embedding_count,
        "background_source_labeled_automorphism_order": automorphism_order,
        "role_embedding_and_topology_quotient": exact_fraction(embedding_rational),
        "combined_rational": exact_fraction(combined),
        "combined_hbar_power": -n_action,
        "exact_chain": (
            f"(-1)^{n_action}/{source_denominator}"
            f"*{role_embedding_count}/{automorphism_order}"
            f"={combined.numerator}/{combined.denominator}"
        ),
        "orientation_policy": (
            "DIRECT_IS_PHYSICAL_REPRESENTATIVE_REFLECTED_IS_ROUTING_CHECK_ONLY"
        ),
    }


def coupling_grade(graph: Mapping[str, Any]) -> dict[str, Any]:
    propagator_count = len(graph["internal_edges"])
    action_vertex_count = sum(
        vertex["role"] == "ACTION_VERTEX" for vertex in graph["vertices"]
    )
    g2_power_before_h_substitution = propagator_count
    h_power = action_vertex_count
    g2_power_after_h_substitution = propagator_count - action_vertex_count
    return {
        "propagator_count": propagator_count,
        "vector_propagator_grade": {
            "base": "g^2",
            "power": propagator_count,
            "rendered": f"(g^2)^{propagator_count}",
        },
        "action_vertex_count": action_vertex_count,
        "raw_action_h_grade": {
            "base": "h",
            "power": h_power,
            "rendered": f"h^{h_power}",
        },
        "normalization_identity": "h=(g^2)^(-1)",
        "derived_g2_power": g2_power_after_h_substitution,
        "derived_g_power": 2 * g2_power_after_h_substitution,
        "exact_chain": [
            f"(g^2)^{g2_power_before_h_substitution}*h^{h_power}",
            f"(g^2)^{g2_power_before_h_substitution}*(g^2)^(-{h_power})",
            f"(g^2)^{g2_power_after_h_substitution}",
            f"g^{2 * g2_power_after_h_substitution}",
        ],
        "kept_separate_from_numeric_action_and_wick_factors": True,
    }


def _mixed_radix_rank(indices: Sequence[int], radices: Sequence[int]) -> int:
    if len(indices) != len(radices):
        raise ValueError("indices and radices have different lengths")
    rank = 0
    for index, radix in zip(indices, radices, strict=True):
        if index < 0 or index >= radix:
            raise ValueError(f"index {index} outside radix {radix}")
        rank = rank * radix + index
    return rank


def _mixed_radix_unrank(rank: int, radices: Sequence[int]) -> tuple[int, ...]:
    cardinality = prod(radices)
    if rank < 0 or rank >= cardinality:
        raise ValueError(f"rank {rank} outside [0,{cardinality})")
    indices = [0] * len(radices)
    residual = rank
    for position in range(len(radices) - 1, -1, -1):
        residual, indices[position] = divmod(residual, radices[position])
    return tuple(indices)


@dataclass(frozen=True)
class ParentJoin:
    graph: dict[str, Any]
    orientation: str
    vertex_order: tuple[str, ...]
    term_dictionary: dict[str, dict[str, Any]]
    assignment_catalog: dict[str, list[dict[str, Any]]]
    local_options: dict[str, list[dict[str, Any]]]

    @property
    def radices(self) -> tuple[int, ...]:
        return tuple(len(self.local_options[vertex_id]) for vertex_id in self.vertex_order)

    @property
    def cardinality(self) -> int:
        return prod(self.radices)

    def unrank(self, rank: int) -> tuple[dict[str, Any], ...]:
        indices = _mixed_radix_unrank(rank, self.radices)
        return tuple(
            self.local_options[vertex_id][index]
            for vertex_id, index in zip(self.vertex_order, indices, strict=True)
        )

    def rank(self, options: Sequence[Mapping[str, Any]]) -> int:
        if len(options) != len(self.vertex_order):
            raise ValueError("one local option is required per topology vertex")
        indices = []
        for vertex_id, selected in zip(self.vertex_order, options, strict=True):
            option_ids = [row["local_option_id"] for row in self.local_options[vertex_id]]
            indices.append(option_ids.index(selected["local_option_id"]))
        return _mixed_radix_rank(indices, self.radices)

    def pairing_id(self, rank: int) -> str:
        width = max(1, len(str(self.cardinality - 1)))
        return f"{self.graph['graph_id']}::{self.orientation}::W{rank:0{width}d}"

    def iter_pairing_ids(self) -> Iterator[str]:
        for rank in range(self.cardinality):
            yield self.pairing_id(rank)

    def materialize(self, rank: int) -> dict[str, Any]:
        selected_options = self.unrank(rank)
        selected_by_vertex = {
            vertex_id: option
            for vertex_id, option in zip(self.vertex_order, selected_options, strict=True)
        }
        port_to_grammar: dict[str, dict[str, Any]] = {}
        for vertex_id, option in selected_by_vertex.items():
            for attachment in option["quantum_attachment"]:
                topology_port_id = attachment["topology_port_id"]
                port_to_grammar[topology_port_id] = {
                    "vertex_id": vertex_id,
                    "source_term_id": option["source_term_id"],
                    "grammar_port_id": attachment["grammar_port_id"],
                    "grammar_port_occurrence_id": attachment[
                        "grammar_port_occurrence_id"
                    ],
                    "grammar_port_parity": attachment["grammar_port_parity"],
                    "grammar_derivative_word_outer_to_inner": attachment[
                        "grammar_derivative_word_outer_to_inner"
                    ],
                    "topology_port_id": topology_port_id,
                }
        base_edges = {edge["edge_id"]: edge for edge in self.graph["internal_edges"]}
        oriented_edges = self.graph["orientations"][self.orientation]["edges"]
        edge_rows = []
        for oriented in oriented_edges:
            base = base_edges[oriented["edge_id"]]
            topology_port_by_vertex = {
                base["source"]: base["source_port"],
                base["target"]: base["target_port"],
            }
            source_port = topology_port_by_vertex[oriented["source"]]
            target_port = topology_port_by_vertex[oriented["target"]]
            edge_rows.append(
                {
                    "edge_id": oriented["edge_id"],
                    "source": port_to_grammar[source_port],
                    "target": port_to_grammar[target_port],
                    "momentum": oriented["momentum"],
                    "momentum_vector": oriented["momentum_vector"],
                    "field_type": "V_QUANTUM_WICK_TO_V_QUANTUM_WICK",
                    "propagator": None,
                    "propagator_status": PROPAGATOR_STATUS,
                }
            )
        vertices_by_id = {
            vertex["vertex_id"]: vertex for vertex in self.graph["vertices"]
        }
        action_items = [
            (vertex_id, option, vertices_by_id[vertex_id]["family"])
            for vertex_id, option in selected_by_vertex.items()
            if vertices_by_id[vertex_id]["role"] == "ACTION_VERTEX"
        ]
        family_sector_multiplicities: dict[str, int] = {}
        for _, option, family in action_items:
            sector = action_sector(option["source_term_id"])
            if sector is None:
                raise ValueError("action term without PLUS or MINUS sector")
            key = f"{family}_{sector}"
            family_sector_multiplicities[key] = (
                family_sector_multiplicities.get(key, 0) + 1
            )
        insertion_items = [
            (vertex_id, option)
            for vertex_id, option in selected_by_vertex.items()
            if vertices_by_id[vertex_id]["role"] == "COMPOSITE_INSERTION"
        ]
        if len(insertion_items) != 1:
            raise ValueError("expected exactly one insertion vertex")
        row = {
            "pairing_id": self.pairing_id(rank),
            "rank": rank,
            "graph_id": self.graph["graph_id"],
            "orientation": self.orientation,
            "classification": "TYPED_LABELED_WICK_PAIRING_NO_PROPAGATOR",
            "selected_local_option_ids": [
                selected_by_vertex[vertex_id]["local_option_id"]
                for vertex_id in self.vertex_order
            ],
            "selected_term_ids": {
                vertex_id: selected_by_vertex[vertex_id]["source_term_id"]
                for vertex_id in self.vertex_order
            },
            "global_grassmann_parity": sum(
                option["grassmann_parity"] for option in selected_options
            )
            % 2,
            "edges": edge_rows,
            "coefficient_factorization": {
                "insertion_raw_coefficient": insertion_items[0][1]["coefficient_raw"],
                "ordered_action_raw_coefficients": [
                    {
                        "vertex_id": vertex_id,
                        "term_id": option["source_term_id"],
                        "family": family,
                        "coefficient": option["coefficient_raw"],
                    }
                    for vertex_id, option, family in action_items
                ],
                "raw_grouped_exponential_factor_for_sector_census_only": expansion_factor(
                    family_sector_multiplicities
                ),
                "decorated_occurrence_orbit_factor": decorated_occurrence_orbit_factor(
                    self.graph, [option for _, option, _ in action_items]
                ),
                "wick_field_statistics_sign": 1,
                "automorphism_denominator": self.graph["automorphisms"]
                ["background_source_labeled"]["order"],
                "automorphism_policy": (
                    "DIVIDE_ONCE_AFTER_OCCURRENCE_TO_DECORATED_ROLE_EMBEDDINGS"
                ),
                "assembled_numeric_coefficient": None,
                "assembled_numeric_coefficient_status": COEFFICIENT_STATUS,
            },
            "coupling_grade": coupling_grade(self.graph),
            "chirality_zero_inference": {
                "status": CHIRALITY_ZERO_STATUS,
                "discarded": False,
            },
            "external_projection": {
                "status": EXTERNAL_PROJECTION_STATUS,
                "value": None,
            },
            "downstream_fail_closed": downstream_fail_closed(),
        }
        row["pairing_sha256"] = digest(row)
        return row


def downstream_fail_closed() -> dict[str, dict[str, Any]]:
    return {
        "propagator_ir": {"status": PROPAGATOR_STATUS, "value": None},
        "d_algebra_ir": {"status": DALGEBRA_STATUS, "value": None},
        "amplitude_ir": {"status": AMPLITUDE_STATUS, "value": None},
        "subtracted_integral_ir": {"status": SUBTRACTION_STATUS, "value": None},
        "renormalized_coefficient": {"status": COEFFICIENT_STATUS, "value": None},
    }


def make_parent_join(
    graph: Mapping[str, Any],
    orientation: str,
    terms_by_family: Mapping[str, Sequence[Mapping[str, Any]]],
) -> ParentJoin:
    if graph["valence_family_id"] not in SUPPORTED_FAMILIES:
        raise ValueError(f"unsupported topology family {graph['valence_family_id']}")
    if orientation not in ("direct", "reflected"):
        raise ValueError(f"unsupported orientation {orientation}")
    vertex_order = tuple(vertex["vertex_id"] for vertex in graph["vertices"])
    assignments: dict[str, list[dict[str, Any]]] = {}
    options: dict[str, list[dict[str, Any]]] = {}
    used_term_ids: set[str] = set()
    for vertex in graph["vertices"]:
        family = vertex["family"]
        family_terms = terms_by_family[family]
        vertex_assignments, vertex_options = local_wick_options(
            graph, orientation, vertex, family_terms
        )
        if not vertex_assignments or not vertex_options:
            raise ValueError(f"no admissible assignments for {graph['graph_id']}:{vertex['vertex_id']}")
        assignments[vertex["vertex_id"]] = vertex_assignments
        options[vertex["vertex_id"]] = vertex_options
        used_term_ids.update(row["source_term_id"] for row in vertex_assignments)
    term_dictionary = {
        term["term_id"]: term_dictionary_row(term)
        for terms in terms_by_family.values()
        for term in terms
        if term["term_id"] in used_term_ids
    }
    return ParentJoin(
        graph=dict(graph),
        orientation=orientation,
        vertex_order=vertex_order,
        term_dictionary=term_dictionary,
        assignment_catalog=assignments,
        local_options=options,
    )


def sector_histogram(join: ParentJoin) -> list[dict[str, Any]]:
    action_vertices = [
        vertex["vertex_id"]
        for vertex in join.graph["vertices"]
        if vertex["role"] == "ACTION_VERTEX"
    ]
    insertion_vertices = [
        vertex["vertex_id"]
        for vertex in join.graph["vertices"]
        if vertex["role"] == "COMPOSITE_INSERTION"
    ]
    insertion_multiplier = prod(len(join.local_options[vertex]) for vertex in insertion_vertices)
    local_counts = {
        vertex_id: {
            sector: sum(
                action_sector(option["source_term_id"]) == sector
                for option in join.local_options[vertex_id]
            )
            for sector in ("PLUS", "MINUS")
        }
        for vertex_id in action_vertices
    }
    action_family = {
        vertex["vertex_id"]: vertex["family"]
        for vertex in join.graph["vertices"]
        if vertex["role"] == "ACTION_VERTEX"
    }
    histogram: dict[tuple[tuple[str, int], ...], int] = {}
    for sector_choice in product(("PLUS", "MINUS"), repeat=len(action_vertices)):
        family_sector_multiplicities: dict[str, int] = {}
        for vertex_id, sector in zip(action_vertices, sector_choice, strict=True):
            key = f"{action_family[vertex_id]}_{sector}"
            family_sector_multiplicities[key] = (
                family_sector_multiplicities.get(key, 0) + 1
            )
        key = tuple(sorted(family_sector_multiplicities.items()))
        multiplicity = insertion_multiplier * prod(
            local_counts[vertex_id][sector]
            for vertex_id, sector in zip(action_vertices, sector_choice, strict=True)
        )
        histogram[key] = histogram.get(key, 0) + multiplicity
    return [
        {
            "n_plus": sum(value for name, value in key if name.endswith("_PLUS")),
            "n_minus": sum(value for name, value in key if name.endswith("_MINUS")),
            "family_sector_multiplicities": dict(key),
            "labeled_pairing_count": count,
            "exponential_expansion_factor": expansion_factor(dict(key)),
        }
        for key, count in sorted(histogram.items())
    ]


def stream_certificate(join: ParentJoin) -> dict[str, Any]:
    stream_hash = sha256()
    for rank, options in enumerate(
        product(*(join.local_options[vertex] for vertex in join.vertex_order))
    ):
        encoded = canonical_json(
            {
                "rank": rank,
                "local_option_ids": [option["local_option_id"] for option in options],
            }
        )
        stream_hash.update(encoded.encode("utf-8"))
        stream_hash.update(b"\n")
    last_rank = join.cardinality - 1
    return {
        "representation": "EXACT_FACTORIZED_CARTESIAN_PRODUCT",
        "rank_convention": "row-major mixed radix in vertex_order",
        "vertex_order": list(join.vertex_order),
        "radices": list(join.radices),
        "cardinality": join.cardinality,
        "first_pairing_id": join.pairing_id(0),
        "last_pairing_id": join.pairing_id(last_rank),
        "first_local_option_ids": [option["local_option_id"] for option in join.unrank(0)],
        "last_local_option_ids": [option["local_option_id"] for option in join.unrank(last_rank)],
        "stream_sha256": stream_hash.hexdigest(),
        "materialization": "rank -> mixed-radix local options -> edge-tagged endpoints",
        "not_a_valence_only_request": True,
    }


def factorized_local_catalog(join: ParentJoin) -> dict[str, Any]:
    endpoint_index = edge_endpoint_index(join.graph, join.orientation)
    vertices = {vertex["vertex_id"]: vertex for vertex in join.graph["vertices"]}
    catalog: dict[str, Any] = {}
    for vertex_id in join.vertex_order:
        vertex = vertices[vertex_id]
        topology_ports = tuple(vertex["quantum_ports"])
        permutation_rows = []
        for ordinal, target_permutation in enumerate(permutations(topology_ports), start=1):
            permutation_rows.append(
                {
                    "permutation_id": f"{join.orientation}::{vertex_id}::P{ordinal:03d}",
                    "source_grammar_port_position_to_topology_endpoint": [
                        {
                            "source_position": position,
                            **endpoint_index[topology_port_id],
                        }
                        for position, topology_port_id in enumerate(target_permutation)
                    ],
                }
            )
        assignment_ids = [
            row["assignment_id"] for row in join.assignment_catalog[vertex_id]
        ]
        catalog[vertex_id] = {
            "assignment_factor_ref": f"{join.graph['graph_id']}::{vertex_id}",
            "assignment_ids": assignment_ids,
            "assignment_count": len(assignment_ids),
            "vertex_port_bijection_permutations": permutation_rows,
            "permutation_count": len(permutation_rows),
            "local_option_count": len(join.local_options[vertex_id]),
            "local_option_identity": (
                f"{len(join.local_options[vertex_id])}="
                f"{len(assignment_ids)}*{len(permutation_rows)}"
            ),
            "local_option_id_rule": (
                "orientation::background_quantum_assignment_id::permutation_ordinal"
            ),
        }
    return catalog


def join_as_json(join: ParentJoin) -> dict[str, Any]:
    certificate = stream_certificate(join)
    samples = {
        "first": join.materialize(0),
        "middle": join.materialize(join.cardinality // 2),
        "last": join.materialize(join.cardinality - 1),
    }
    row = {
        "graph_id": join.graph["graph_id"],
        "graph_hash": join.graph["graph_hash"],
        "valence_family_id": join.graph["valence_family_id"],
        "orientation": join.orientation,
        "orientation_hash": join.graph["orientations"][join.orientation]["orientation_hash"],
        "orientation_role": (
            "PHYSICAL_SUM_REPRESENTATIVE"
            if join.orientation == "direct"
            else "ROUTING_COVARIANCE_CHECK_ONLY_NOT_ADDED_TO_PHYSICAL_SUM"
        ),
        "classification": "EXACT_FACTORIZED_TYPED_LABELED_WICK_ENUMERATION",
        "vertex_order": list(join.vertex_order),
        "term_dictionary_refs": sorted(join.term_dictionary),
        "background_quantum_assignment_catalog_ref": join.graph["graph_id"],
        "assignment_counts": {
            vertex_id: len(join.assignment_catalog[vertex_id])
            for vertex_id in join.vertex_order
        },
        "local_wick_factor_catalog": factorized_local_catalog(join),
        "local_option_counts": {
            vertex_id: len(join.local_options[vertex_id])
            for vertex_id in join.vertex_order
        },
        "global_pairing_enumeration": certificate,
        "sector_histogram": sector_histogram(join),
        "coupling_grade": coupling_grade(join.graph),
        "chirality_policy": {
            "status": CHIRALITY_ZERO_STATUS,
            "discarded_assignment_count": 0,
            "rule": "PRESERVE_ALL_PLUS_MINUS_MEASURE_WORDS_UNTIL_TYPED_DALGEBRA_CERTIFICATE",
        },
        "coefficient_policy": {
            "raw_term_coefficients": "PRESERVED_IN_TERM_AND_LOCAL_OPTION_RECORDS",
            "raw_grouped_exponential_factor": "SECTOR_CENSUS_ONLY_NOT_PHYSICAL_ROW_WEIGHT",
            "physical_row_weight": (
                "SOURCE_EXACT_MONOMIAL_FACTOR_TIMES_OCCURRENCE_ROLE_EMBEDDINGS_"
                "DIVIDED_ONCE_BY_BACKGROUND_SOURCE_LABELED_AUTOMORPHISM"
            ),
            "orientation": "DIRECT_ONLY_REFLECTED_IS_ROUTING_COVARIANCE_CHECK",
            "assembled_coefficient": None,
            "status": COEFFICIENT_STATUS,
        },
        "external_projection": {"status": EXTERNAL_PROJECTION_STATUS, "value": None},
        "downstream_fail_closed": downstream_fail_closed(),
        "samples_only_not_full_materialization": samples,
    }
    row["join_sha256"] = digest(row)
    return row


def build_runtime() -> tuple[dict[str, Any], list[ParentJoin]]:
    grammar_payload = grammar.build_payload()
    topology_bundle = graphir.build_bundle()
    terms_by_family = selected_terms(grammar_payload)
    supported_graphs = [
        graph
        for graph in topology_bundle["literal_direct_graphs"]
        if graph["valence_family_id"] in SUPPORTED_FAMILIES
    ]
    if len(supported_graphs) != 3:
        raise ValueError(
            "exactly three decorated K4-minus-edge graphs across the two supported families "
            "are required"
        )
    joins = [
        make_parent_join(graph, orientation, terms_by_family)
        for graph in supported_graphs
        for orientation in ("direct", "reflected")
    ]
    provenance = {
        "grammar_payload_sha256": digest(grammar_payload),
        "topology_bundle_sha256": digest(topology_bundle),
        "grammar_generator": "scripts/step6_two_loop_grammar.py",
        "grammar_generator_sha256": file_sha256(ROOT / "scripts/step6_two_loop_grammar.py"),
        "topology_generator": "scripts/step6_two_loop_graphir.py",
        "topology_generator_sha256": file_sha256(ROOT / "scripts/step6_two_loop_graphir.py"),
        "authority_role": "UNMERGED_PROPOSAL_INPUTS_NOT_COMPUTATIONAL_EVIDENCE",
    }
    return provenance, joins


def build_payload() -> tuple[dict[str, Any], list[ParentJoin]]:
    provenance, joins = build_runtime()
    join_rows = [join_as_json(join) for join in joins]
    term_dictionary: dict[str, dict[str, Any]] = {}
    assignment_catalog: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for join in joins:
        for term_id, term in join.term_dictionary.items():
            if term_id in term_dictionary and term_dictionary[term_id] != term:
                raise ValueError(f"term dictionary drift for {term_id}")
            term_dictionary[term_id] = term
        graph_id = join.graph["graph_id"]
        if graph_id in assignment_catalog and assignment_catalog[graph_id] != join.assignment_catalog:
            raise ValueError(f"orientation-dependent B/Q assignment drift for {graph_id}")
        assignment_catalog[graph_id] = join.assignment_catalog
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "stage": "TYPED_AST_TO_TOPOLOGY_WICK_JOIN_ONLY",
        "scope": "ONLY_LITERAL_K4_MINUS_EDGE_I3_S3_CUBED_AND_I2_S3_SQUARED_S4",
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "input_provenance": provenance,
        "supported_valence_families": list(SUPPORTED_FAMILIES),
        "decorated_graph_count": len({join.graph["graph_id"] for join in joins}),
        "source_family_count": len(SUPPORTED_FAMILIES),
        "term_dictionary": dict(sorted(term_dictionary.items())),
        "decorated_graph_background_quantum_assignment_catalog": dict(
            sorted(assignment_catalog.items())
        ),
        "joins": join_rows,
        "exact_total_labeled_pairings": sum(
            row["global_pairing_enumeration"]["cardinality"] for row in join_rows
        ),
        "exact_total_physical_representative_pairings_before_automorphism_weight": sum(
            row["global_pairing_enumeration"]["cardinality"]
            for row in join_rows
            if row["orientation_role"] == "PHYSICAL_SUM_REPRESENTATIVE"
        ),
        "orientation_sum_policy": (
            "SUM_DIRECT_ONLY_REFLECTED_ROWS_CERTIFY_ROUTING_COVARIANCE"
        ),
        "global_chirality_policy": {
            "status": CHIRALITY_ZERO_STATUS,
            "discarded_assignment_count": 0,
        },
        "global_downstream_fail_closed": downstream_fail_closed(),
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    )
    return payload, joins


def exact_checks(payload: Mapping[str, Any], joins: Sequence[ParentJoin]) -> dict[str, bool]:
    rows = payload["joins"]
    terms_by_family = selected_terms(grammar.build_payload())
    by_key = {(join.graph["graph_id"], join.orientation): join for join in joins}
    expected_assignment_counts = {
        "G6_DIRECT_K4ME_I3_S3CUBED": {"I": 10, "A": 12, "B": 12, "C": 4},
        "G6_DIRECT_K4ME_I2_S3SQ_S4": {"I": 2, "A": 12, "B": 4, "C": 24},
        "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": {"I": 2, "A": 4, "B": 4, "C": 72},
    }
    expected_option_counts = {
        "G6_DIRECT_K4ME_I3_S3CUBED": {"I": 60, "A": 24, "B": 24, "C": 24},
        "G6_DIRECT_K4ME_I2_S3SQ_S4": {"I": 4, "A": 24, "B": 24, "C": 144},
        "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": {"I": 4, "A": 24, "B": 24, "C": 144},
    }
    expected_cardinality = {
        "G6_DIRECT_K4ME_I3_S3CUBED": 829_440,
        "G6_DIRECT_K4ME_I2_S3SQ_S4": 331_776,
        "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": 331_776,
    }
    sampled = [
        join.materialize(rank)
        for join in joins
        for rank in (0, join.cardinality // 2, join.cardinality - 1)
    ]
    return {
        "status_is_proposal_only": payload["status"] == STATUS
        and all(row["classification"] == "EXACT_FACTORIZED_TYPED_LABELED_WICK_ENUMERATION" for row in rows),
        "only_two_literal_parent_families": set(payload["supported_valence_families"])
        == set(SUPPORTED_FAMILIES)
        and payload["source_family_count"] == 2
        and payload["decorated_graph_count"] == 3
        and len(rows) == 6
        and all(join.graph["topology"] == "K4_MINUS_ONE_EDGE" for join in joins),
        "direct_and_reflected_preserved": {
            (join.graph["graph_id"], join.orientation) for join in joins
        }
        == {
            (graph_id, orientation)
            for graph_id in expected_cardinality
            for orientation in ("direct", "reflected")
        },
        "exact_bq_assignment_counts": all(
            {
                vertex: len(join.assignment_catalog[vertex]) for vertex in join.vertex_order
            }
            == expected_assignment_counts[graph_id]
            for (graph_id, _), join in by_key.items()
        ),
        "exact_local_wick_option_counts": all(
            {vertex: len(join.local_options[vertex]) for vertex in join.vertex_order}
            == expected_option_counts[graph_id]
            for (graph_id, _), join in by_key.items()
        ),
        "exact_global_labeled_pairing_counts": all(
            join.cardinality == expected_cardinality[graph_id]
            for (graph_id, _), join in by_key.items()
        )
        and payload["exact_total_labeled_pairings"] == 2_985_984
        and payload[
            "exact_total_physical_representative_pairings_before_automorphism_weight"
        ]
        == 1_492_992,
        "all_t_b_q_identities_exact": all(
            assignment["t"] == assignment["b"] + assignment["q"]
            and assignment["degree_identity"]
            for join in joins
            for assignments in join.assignment_catalog.values()
            for assignment in assignments
        ),
        "labeled_background_bijections_are_enumerated_without_projection": all(
            len(join.assignment_catalog[vertex["vertex_id"]])
            == len(terms_by_family[vertex["family"]])
            * comb(vertex["total_valence"], vertex["background_valence"])
            * factorial(vertex["background_valence"])
            and all(
                assignment["background_projection_join"]["bijection_is_enumerated"]
                and assignment["background_projection_join"]["value"] is None
                and assignment["background_projection_join"]["status"]
                == EXTERNAL_PROJECTION_STATUS
                and len(
                    assignment["background_projection_join"][
                        "labeled_background_port_bijection"
                    ]
                )
                == vertex["background_valence"]
                for assignment in join.assignment_catalog[vertex["vertex_id"]]
            )
            for join in joins
            for vertex in join.graph["vertices"]
        ),
        "term_ids_parity_measure_chirality_color_ast_preserved": all(
            term_id == term["term_id"]
            and term["grassmann_parity"] in (0, 1)
            and bool(term["measure"])
            and bool(term["chirality"]["class"])
            and digest(term["color_ast"]) == term["color_ast_sha256"]
            and digest(term["expression_ast"]) == term["expression_ast_sha256"]
            for join in joins
            for term_id, term in join.term_dictionary.items()
        ),
        "each_local_quantum_attachment_is_bijective": all(
            option["quantum_bijection"]
            and len(option["quantum_attachment"]) == option["q"]
            and all(item["grammar_port_parity"] == 0 for item in option["quantum_attachment"])
            for join in joins
            for options in join.local_options.values()
            for option in options
        ),
        "sampled_global_pairings_saturate_five_edges": all(
            len(row["edges"]) == 5
            and len(
                {
                    endpoint["grammar_port_occurrence_id"]
                    for edge in row["edges"]
                    for endpoint in (edge["source"], edge["target"])
                }
            )
            == 10
            for row in sampled
        ),
        "rank_unrank_are_exact_inverses": all(
            join.rank(join.unrank(rank)) == rank
            for join in joins
            for rank in (0, join.cardinality // 2, join.cardinality - 1)
        ),
        "sector_histograms_are_complete": all(
            sum(row["labeled_pairing_count"] for row in sector_histogram(join))
            == join.cardinality
            and len(sector_histogram(join))
            == (4 if join.graph["valence_family_id"] == "I3__S3^3" else 6)
            and all(
                sum(row["family_sector_multiplicities"].values()) == 3
                and row["exponential_expansion_factor"]["factorial_denominator"]
                == prod(
                    factorial(value)
                    for value in row["family_sector_multiplicities"].values()
                )
                for row in sector_histogram(join)
            )
            for join in joins
        ),
        "raw_sector_factor_is_not_physical_row_weight": all(
            row["coefficient_policy"]["raw_grouped_exponential_factor"]
            == "SECTOR_CENSUS_ONLY_NOT_PHYSICAL_ROW_WEIGHT"
            and row["coefficient_policy"]["raw_term_coefficients"]
            == "PRESERVED_IN_TERM_AND_LOCAL_OPTION_RECORDS"
            for row in rows
        ),
        "decorated_occurrence_orbit_factor_is_exact": all(
            row["coefficient_policy"]["orientation"]
            == "DIRECT_ONLY_REFLECTED_IS_ROUTING_COVARIANCE_CHECK"
            and sample["coefficient_factorization"]["automorphism_denominator"]
            == sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
            ["background_source_labeled_automorphism_order"]
            and Fraction(
                sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
                ["combined_rational"]["numerator"],
                sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
                ["combined_rational"]["denominator"],
            )
            == Fraction(
                -1,
                sample["coefficient_factorization"]["automorphism_denominator"],
            )
            for row in rows
            for sample in row["samples_only_not_full_materialization"].values()
        ),
        "direct_only_is_physical_sum": payload["orientation_sum_policy"]
        == "SUM_DIRECT_ONLY_REFLECTED_ROWS_CERTIFY_ROUTING_COVARIANCE"
        and all(
            row["orientation_role"]
            == (
                "PHYSICAL_SUM_REPRESENTATIVE"
                if row["orientation"] == "direct"
                else "ROUTING_COVARIANCE_CHECK_ONLY_NOT_ADDED_TO_PHYSICAL_SUM"
            )
            for row in rows
        ),
        "coupling_grade_is_g4": all(
            row["coupling_grade"]["propagator_count"] == 5
            and row["coupling_grade"]["action_vertex_count"] == 3
            and row["coupling_grade"]["derived_g2_power"] == 2
            and row["coupling_grade"]["derived_g_power"] == 4
            and row["coupling_grade"]["kept_separate_from_numeric_action_and_wick_factors"]
            for row in rows
        ),
        "no_chirality_zero_was_inferred": payload["global_chirality_policy"]
        == {"status": CHIRALITY_ZERO_STATUS, "discarded_assignment_count": 0}
        and all(row["chirality_policy"]["discarded_assignment_count"] == 0 for row in rows),
        "external_projection_fails_closed": all(
            row["external_projection"] == {"status": EXTERNAL_PROJECTION_STATUS, "value": None}
            for row in rows
        ),
        "propagator_dalgebra_amplitude_coefficient_fail_closed": all(
            stage["value"] is None and stage["status"].startswith("BLOCKED_")
            for row in rows
            for stage in row["downstream_fail_closed"].values()
        )
        and all(
            stage["value"] is None and stage["status"].startswith("BLOCKED_")
            for stage in payload["global_downstream_fail_closed"].values()
        ),
        "stream_certificates_have_exact_cardinality_and_hash": all(
            row["global_pairing_enumeration"]["cardinality"]
            == expected_cardinality[row["graph_id"]]
            and len(row["global_pairing_enumeration"]["stream_sha256"]) == 64
            for row in rows
        ),
        "serialized_ir_is_exact_factorization_not_global_row_materialization": len(
            payload["term_dictionary"]
        )
        == 22
        and len(payload["decorated_graph_background_quantum_assignment_catalog"])
        == 3
        and all(
            "local_wick_option_catalog" not in row
            and row["global_pairing_enumeration"]["cardinality"]
            == prod(
                factor["local_option_count"]
                for factor in row["local_wick_factor_catalog"].values()
            )
            and all(
                factor["local_option_count"]
                == factor["assignment_count"] * factor["permutation_count"]
                for factor in row["local_wick_factor_catalog"].values()
            )
            for row in rows
        ),
        "input_provenance_hashes_present": all(
            len(value) == 64
            for key, value in payload["input_provenance"].items()
            if key.endswith("sha256")
        ),
        "source_has_no_duplicate_literal_dict_keys": duplicate_literal_dict_keys(
            ROOT / "scripts/step6_two_loop_wick.py"
        )
        == [],
    }


def build_audit(payload: Mapping[str, Any], joins: Sequence[ParentJoin]) -> dict[str, Any]:
    checks = exact_checks(payload, joins)
    failures = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "step6.two_loop_wick.audit.v1",
        "status": "PASS" if not failures else "FAIL",
        "proposal_status": STATUS,
        "generator": "scripts/step6_two_loop_wick.py",
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "exact_total_labeled_pairings": payload["exact_total_labeled_pairings"],
        "payload_sha256": payload["payload_sha256"],
        "input_provenance": payload["input_provenance"],
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    rows = payload["joins"]
    direct_rows = [row for row in rows if row["orientation"] == "direct"]
    lines = [
        "# Step 6 — typed Project-AST to two-loop Wick join",
        "",
        f"`{STATUS}`",
        "",
        "$$",
        r"t_v=b_v+q_v,\qquad",
        r"\mathfrak W_{G,o}=\prod_{v\in V(G)}\mathfrak W_{v,o},\qquad",
        r"|\mathfrak W_{G,o}|=\prod_{v\in V(G)}|\mathfrak W_{v,o}|.",
        "$$",
        "",
        "| parent | orientation | local radices | labeled Wick pairings |",
        "|:---|:---:|:---:|---:|",
    ]
    for row in rows:
        certificate = row["global_pairing_enumeration"]
        lines.append(
            f"| `{row['valence_family_id']}` | `{row['orientation']}` | "
            f"`{certificate['radices']}` | {certificate['cardinality']} |"
        )
    lines.extend(
        [
            "",
            "$$",
            r"F_{\exp}(\{n_{r,\sigma}\})",
            r"=\frac{(-1)^N}{\hbar^N\prod_{r,\sigma}n_{r,\sigma}!},",
            r"\qquad N=\sum_{r,\sigma}n_{r,\sigma}=3.",
            "$$",
            "",
            "$$",
            r"(g^2)^5h^3=(g^2)^5(g^2)^{-3}=(g^2)^2=g^4.",
            "$$",
            "",
            "| $n_+$ | $n_-$ | expansion factor |",
            "|---:|---:|:---|",
        ]
    )
    first_histogram = direct_rows[0]["sector_histogram"]
    for item in first_histogram:
        lines.append(
            f"| {item['n_plus']} | {item['n_minus']} | "
            f"`{item['exponential_expansion_factor']['rendered']}` |"
        )
    lines.extend(
        [
            "",
            "$$",
            r"F_{\exp}(S_{3,+}^2S_{4,+})=-\frac1{2!\,1!\,\hbar^3}",
            r"=-\frac1{2\hbar^3}.",
            "$$",
            "",
            f"Chirality zero inference: `{CHIRALITY_ZERO_STATUS}`; discarded `0`.",
            "",
            f"External projection: `{EXTERNAL_PROJECTION_STATUS}`.",
            "",
            f"Propagator: `{PROPAGATOR_STATUS}`.",
            "",
            f"D-algebra: `{DALGEBRA_STATUS}`.",
            "",
            f"Amplitude: `{AMPLITUDE_STATUS}`.",
            "",
            f"Coefficient: `{COEFFICIENT_STATUS}`.",
            "",
            f"Exact checks: `{audit['passed']}/{audit['passed'] + audit['failed']}`.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload, joins = build_payload()
    audit = build_audit(payload, joins)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    GENERATED_MD.write_text(render_markdown(payload, audit))
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "proposal_status": payload["status"],
                "join_count": len(payload["joins"]),
                "exact_total_labeled_pairings": payload["exact_total_labeled_pairings"],
                "passed": audit["passed"],
                "failed": audit["failed"],
            },
            sort_keys=True,
        )
    )
    return 0 if audit["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
