#!/usr/bin/env python3
"""Exact Project external-background projection certificate for Step 6.

The compiler substitutes ``V_i=V_{B,i}+v_i`` at labeled ordered Project-AST
ports.  Every role word occurs once.  It then joins only background-bearing
action vertices of the three decorated literal ``K4``-minus-edge topology
records to exact ``S3``/``S4`` Project terms.

No quantum-port bijection, propagator, Wick contraction, D-algebra,
amplitude, graph coefficient, or subtraction is constructed here.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import comb, prod
from pathlib import Path
import re
from typing import Any, Iterator, Mapping, Sequence

try:
    from scripts import step6_two_loop_grammar as grammar
    from scripts import step6_two_loop_graphir as graphir
except ModuleNotFoundError:  # direct execution
    import step6_two_loop_grammar as grammar
    import step6_two_loop_graphir as graphir


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/external-projection"
GENERATED_JSON = GENERATED_DIR / "external-projection-certificate.json"
GENERATED_MD = GENERATED_DIR / "external-projection-certificate.md"
AUDIT = ROOT / "audits/step6-external-projection-verification.json"

SCHEMA_VERSION = "step6.external_projection.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
JOIN_STATUS = "DETERMINISTIC_SOURCE_AST_PROJECTION_CANDIDATE_NOT_QUANTUM_JOINED"
GRAPH_COEFFICIENT_STATUS = "BLOCKED_QUANTUM_PORT_TO_EDGE_WICK_JOIN_ABSENT"
SUPPORTED_GRAPH_IDS = (
    "G6_DIRECT_K4ME_I3_S3CUBED",
    "G6_DIRECT_K4ME_I2_S3SQ_S4",
    "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4",
)


class ProjectionSourceBlocked(RuntimeError):
    """Raised when a topology background port has no exact action-term AST."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def coefficient_one() -> dict[str, Any]:
    return grammar.QI(1).as_json()


def ordered_split_certificate(max_degree: int = 4) -> dict[str, Any]:
    """Prove labeled ordered-port extraction has unit multiplicity."""

    degrees: list[dict[str, Any]] = []
    for degree in range(1, max_degree + 1):
        role_words = list(product(("B", "q"), repeat=degree))
        rendered = ["".join(word) for word in role_words]
        distribution = {
            str(background_count): sum(word.count("B") == background_count for word in role_words)
            for background_count in range(degree + 1)
        }
        degrees.append(
            {
                "ordered_degree": degree,
                "identity": (
                    "F(V_1,...,V_t)|_(V_i=V_B_i+v_i)="
                    "sum_(rho in {B,q}^t) F(V_(rho_1,1),...,V_(rho_t,t))"
                ),
                "role_words": rendered,
                "role_word_count": len(role_words),
                "unique_role_word_count": len(set(rendered)),
                "fixed_background_distribution": distribution,
                "binomial_distribution": {
                    str(background_count): comb(degree, background_count)
                    for background_count in range(degree + 1)
                },
                "coefficient_of_every_labeled_role_word": coefficient_one(),
                "multiplicity_of_every_labeled_role_word": 1,
                "no_unlabeled_binomial_factor": True,
            }
        )
    return {
        "bridge_split": "V=V_B+v",
        "port_law": "each AST V leaf is labeled before substitution",
        "degrees": degrees,
        "proof": [
            "each labeled leaf contributes exactly the two summands V_B_i and v_i",
            "distributivity selects one summand independently at each labeled leaf",
            "the selected sequence is one unique role word rho in {B,q}^t",
            "therefore every ordered role word has coefficient one and multiplicity one",
        ],
    }


def _single_port(term: grammar.Term) -> dict[str, Any]:
    ports = grammar.collect_ports(term.expression)
    if len(ports) != 1:
        raise ValueError(f"{term.term_id} is not linear in V")
    return ports[0]


def linear_map_certificate() -> dict[str, Any]:
    """Derive the three required linear Project maps from the grammar AST."""

    gamma = grammar.gamma_terms(1, spinor="+")[0]
    w = grammar.w_terms(1, spinor="+")[0]
    x_terms = grammar.x_terms_at_degree(1, prefix="X_LINEAR", free_color="A")
    if len(x_terms) != 1:
        raise ValueError("X_(1) must contain only the flat D_+W_(1)+ term")
    x = x_terms[0]
    tilde_gamma = grammar.tilde_gamma_terms(1, spinor="dot_a")[0]
    tilde_w = grammar.tilde_w_terms(1, spinor="dot_a")[0]
    gamma_port = _single_port(gamma)
    w_port = _single_port(w)
    x_port = _single_port(x)
    tilde_gamma_port = _single_port(tilde_gamma)
    tilde_w_port = _single_port(tilde_w)
    maps = {
        "Gamma_(1)+": {
            "source_term_id": gamma.term_id,
            "equation": "Gamma_(1)+[V_B]=D_+ V_B",
            "coefficient": gamma.coefficient.as_json(),
            "derivative_word_outer_to_inner": gamma_port["derivative_word_outer_to_inner"],
            "expression_ast_sha256": digest(gamma.expression),
        },
        "W_(1)+": {
            "source_term_id": w.term_id,
            "equation": "W_(1)+[V_B]=-(1/8) barD^2 D_+ V_B",
            "coefficient": w.coefficient.as_json(),
            "derivative_word_outer_to_inner": w_port["derivative_word_outer_to_inner"],
            "chirality": "CHIRAL",
            "spinor_slot": "+_down",
            "expression_ast_sha256": digest(w.expression),
        },
        "X_(1)": {
            "source_term_id": x.term_id,
            "equation": (
                "X_(1)[V_B]=D_+W_(1)+[V_B]="
                "-(1/8) D_+ barD^2 D_+ V_B=K_+ V_B"
            ),
            "K_+": "-(1/8) D_+ barD^2 D_+",
            "coefficient": x.coefficient.as_json(),
            "derivative_word_outer_to_inner": x_port["derivative_word_outer_to_inner"],
            "connection_sum_at_degree_one": [],
            "chirality": "CHIRAL",
            "spinor_contraction": "+_derivative_with_+_field_strength",
            "expression_ast_sha256": digest(x.expression),
        },
        "TildeGamma_(1)dot_a": {
            "source_term_id": tilde_gamma.term_id,
            "equation": "TildeGamma_(1)dot_a[V_B]=-barD_dot_a V_B",
            "coefficient": tilde_gamma.coefficient.as_json(),
            "derivative_word_outer_to_inner": tilde_gamma_port[
                "derivative_word_outer_to_inner"
            ],
            "expression_ast_sha256": digest(tilde_gamma.expression),
        },
        "TildeW_(1)dot_a": {
            "source_term_id": tilde_w.term_id,
            "equation": "TildeW_(1)dot_a[V_B]=-(1/8) D^2 barD_dot_a V_B",
            "coefficient": tilde_w.coefficient.as_json(),
            "derivative_word_outer_to_inner": tilde_w_port[
                "derivative_word_outer_to_inner"
            ],
            "chirality": "ANTICHIRAL",
            "spinor_slot": "dot_a_down",
            "expression_ast_sha256": digest(tilde_w.expression),
        },
    }
    return {
        "derivation_source": "Project grammar generated from equations 3A.34, 3A.34a, 3A.51, 3A.52",
        "bridge": "E=exp(V)",
        "maps": maps,
        "exact_chain": [
            "Gamma_(1)+[V_B]=D_+V_B",
            "W_(1)+[V_B]=-(1/8)barD^2 Gamma_(1)+[V_B]=-(1/8)barD^2D_+V_B",
            "X_(1)[V_B]=D_+W_(1)+[V_B]+sum_(r=1)^0[Gamma_(r)+,W_(1-r)+]=-(1/8)D_+barD^2D_+V_B",
            "TildeGamma_(1)dot_a[V_B]=-barD_dot_aV_B",
            "TildeW_(1)dot_a[V_B]=+(1/8)D^2TildeGamma_(1)dot_a[V_B]=-(1/8)D^2barD_dot_aV_B",
        ],
    }


def node_at_path(expression: Mapping[str, Any], path: Sequence[int]) -> Mapping[str, Any]:
    node: Mapping[str, Any] = expression
    for index in path:
        node = node["args"][index]
    return node


def color_context(expression: Mapping[str, Any], path: Sequence[int]) -> list[dict[str, Any]]:
    current: Mapping[str, Any] = expression
    result: list[dict[str, Any]] = []
    for depth, child_index in enumerate(path):
        if current["op"] == "AdjointBracket":
            result.append(
                {
                    "ast_path": list(path[:depth]),
                    "output_color": current["attrs"]["output_color"],
                    "color_tensor": current["attrs"]["color_tensor"],
                    "component_rule": current["attrs"]["component_rule"],
                    "port_is_bracket_child": "LEFT" if child_index == 0 else "RIGHT",
                }
            )
        current = current["args"][child_index]
    return result


def action_sector(term: grammar.Term) -> str:
    if term.family.endswith("_PLUS"):
        return "PLUS"
    if term.family.endswith("_MINUS"):
        return "MINUS"
    raise ProjectionSourceBlocked(f"{term.term_id}: not a PLUS/MINUS gauge-action term")


def measure_chirality(term: grammar.Term) -> dict[str, str]:
    sector = action_sector(term)
    expected = {
        "PLUS": ("E_PLUS_CHIRAL", "CHIRAL"),
        "MINUS": ("E_MINUS_ANTICHIRAL", "ANTICHIRAL"),
    }[sector]
    if term.measure != expected[0]:
        raise ValueError(f"{term.term_id}: sector/measure mismatch")
    return {"measure": term.measure, "chirality": expected[1], "sector": sector}


_FACTOR_RE = re.compile(r"(?P<family>TildeW|W)_(?P<degree>[1-9][0-9]*)")


def factor_context(term: grammar.Term, port: Mapping[str, Any]) -> dict[str, Any]:
    path = list(port["ast_path"])
    if not path or path[0] not in (0, 1):
        raise ValueError(f"{term.term_id}: port is outside ordered action pairing")
    side = "LEFT_RAISED" if path[0] == 0 else "RIGHT_LOWERED"
    match = _FACTOR_RE.search(str(port["port_id"]))
    if match is None:
        raise ValueError(f"{term.term_id}: cannot resolve W/TildeW factor from port id")
    family = match.group("family")
    degree = int(match.group("degree"))
    sector = action_sector(term)
    expected_family = "W" if sector == "PLUS" else "TildeW"
    if family != expected_family:
        raise ValueError(f"{term.term_id}: source factor/sector mismatch")
    root = term.expression
    factor_node: Mapping[str, Any] = root["args"][path[0]]
    if factor_node["op"] == "SpinorRaise":
        factor_node = factor_node["args"][0]
    factor_ports = grammar.collect_ports(dict(factor_node))
    if len(factor_ports) != degree:
        raise ValueError(f"{term.term_id}: factor degree does not match AST port count")
    if family == "W":
        spinor_slot = "a_up" if side == "LEFT_RAISED" else "a_down"
        color_slot = "A" if side == "LEFT_RAISED" else "B"
        factor_coefficient = grammar.w_terms(degree, spinor="a")[degree - 1].coefficient
    else:
        spinor_slot = "dot_a_up" if side == "LEFT_RAISED" else "dot_a_down"
        color_slot = "A" if side == "LEFT_RAISED" else "B"
        factor_coefficient = grammar.tilde_w_terms(degree, spinor="dot_a")[
            degree - 1
        ].coefficient
    return {
        "field_strength_family": family,
        "field_strength_degree": degree,
        "ordered_factor_side": side,
        "spinor_slot": spinor_slot,
        "factor_output_color_slot": color_slot,
        "gauge_color_pairing": root["attrs"]["color_pairing"],
        "factor_coefficient": factor_coefficient.as_json(),
        "factor_ast_sha256": digest(factor_node),
        "factor_ordered_port_ids": [item["port_id"] for item in factor_ports],
        "port_generator_representation": "adjoint",
        "port_color_bracket_context": color_context(term.expression, path),
    }


def linear_factor_supply(context: Mapping[str, Any]) -> dict[str, Any]:
    family = context["field_strength_family"]
    degree = context["field_strength_degree"]
    if degree != 1:
        return {
            "status": "EXACT_NONLINEAR_SOURCE_FACTOR_RETAINED",
            "supplied_object": f"V_B_PORT_INSIDE_{family}_({degree})_AST",
            "standalone_linear_projector": None,
            "forbidden_inference": (
                "DO_NOT_RENAME_A_BACKGROUND_PORT_INSIDE_A_NONLINEAR_FACTOR_AS_"
                "W_(1)_OR_TILDEW_(1)"
            ),
        }
    if family == "W":
        return {
            "status": "EXACT_LINEAR_PROJECT_FIELD_STRENGTH",
            "supplied_object": "W_(1)a[V_B]",
            "standalone_linear_projector": "-(1/8) barD^2 D_a",
            "projector_coefficient": grammar.w_terms(1, spinor="a")[
                0
            ].coefficient.as_json(),
            "coefficient_application": (
                "ALREADY_CONTAINED_IN_SOURCE_TERM_RAW_COEFFICIENT_DO_NOT_MULTIPLY_AGAIN"
            ),
        }
    return {
        "status": "EXACT_LINEAR_PROJECT_TILDE_FIELD_STRENGTH",
        "supplied_object": "TildeW_(1)dot_a[V_B]",
        "standalone_linear_projector": "-(1/8) D^2 barD_dot_a",
        "projector_coefficient": grammar.tilde_w_terms(1, spinor="dot_a")[
            0
        ].coefficient.as_json(),
        "coefficient_application": (
            "ALREADY_CONTAINED_IN_SOURCE_TERM_RAW_COEFFICIENT_DO_NOT_MULTIPLY_AGAIN"
        ),
    }


def action_terms_for_vertex(vertex: Mapping[str, Any]) -> tuple[grammar.Term, ...]:
    if vertex["role"] != "ACTION_VERTEX":
        raise ProjectionSourceBlocked(
            f"{vertex['vertex_id']}: background projection requires an exact action-term AST"
        )
    valence = int(vertex["total_valence"])
    family = str(vertex["family"])
    if family != f"S{valence}" or valence not in (3, 4):
        raise ProjectionSourceBlocked(
            f"{vertex['vertex_id']}: unsupported background source {family} at valence {valence}"
        )
    return tuple(
        sorted(
            (
                *grammar.action_terms_at_valence(valence, "PLUS"),
                *grammar.action_terms_at_valence(valence, "MINUS"),
            ),
            key=lambda term: term.term_id,
        )
    )


def _external_vector(graph: Mapping[str, Any], momentum: str) -> list[int]:
    basis = graph["momentum_contract"]["basis"]
    if momentum not in basis:
        raise ValueError(f"external momentum {momentum} is outside graph momentum basis")
    return [1 if item == momentum else 0 for item in basis]


def vertex_projection_candidates(
    graph: Mapping[str, Any], vertex: Mapping[str, Any]
) -> list[dict[str, Any]]:
    """Enumerate only exact AST-supported projections at one background vertex."""

    background_degree = int(vertex["background_valence"])
    if background_degree <= 0:
        raise ProjectionSourceBlocked(
            f"{graph['graph_id']}:{vertex['vertex_id']}: no background port to project"
        )
    topology_ports = tuple(vertex["background_ports"])
    if len(topology_ports) != background_degree:
        raise ValueError("topology background port count mismatch")
    result: list[dict[str, Any]] = []
    for term in action_terms_for_vertex(vertex):
        ports = grammar.collect_ports(term.expression)
        if len(ports) != int(vertex["total_valence"]):
            raise ValueError("term/topology total valence mismatch")
        for selected_indices in combinations(range(len(ports)), background_degree):
            selected = tuple(ports[index] for index in selected_indices)
            selected_ids = {item["port_id"] for item in selected}
            role_word = [
                "BACKGROUND_PROJECT" if port["port_id"] in selected_ids else "QUANTUM_UNJOINED"
                for port in ports
            ]
            for external_permutation_ordinal, external_order in enumerate(
                permutations(topology_ports), start=1
            ):
                port_rows: list[dict[str, Any]] = []
                factor_groups: dict[tuple[str, str], dict[str, Any]] = {}
                for source_order, (source_port, topology_port) in enumerate(
                    zip(selected, external_order, strict=True)
                ):
                    context = factor_context(term, source_port)
                    group_key = (
                        str(context["ordered_factor_side"]),
                        str(context["factor_ast_sha256"]),
                    )
                    if group_key not in factor_groups:
                        factor_groups[group_key] = {
                            "ordered_factor_side": context["ordered_factor_side"],
                            "field_strength_family": context["field_strength_family"],
                            "field_strength_degree": context["field_strength_degree"],
                            "factor_ordered_port_ids": context["factor_ordered_port_ids"],
                            "selected_background_port_ids": [],
                        }
                    factor_groups[group_key]["selected_background_port_ids"].append(
                        source_port["port_id"]
                    )
                    port_rows.append(
                        {
                            "source_port_order": source_order,
                            "grammar_port_id": source_port["port_id"],
                            "grammar_ast_path": source_port["ast_path"],
                            "topology_port_id": topology_port["port_id"],
                            "external_momentum": topology_port["momentum"],
                            "external_momentum_vector": _external_vector(
                                graph, topology_port["momentum"]
                            ),
                            "ordered_split_substitution": "V_i -> V_B_i",
                            "ordered_split_coefficient": coefficient_one(),
                            "ordered_split_multiplicity": 1,
                            "derivative_word_outer_to_inner": source_port[
                                "derivative_word_outer_to_inner"
                            ],
                            "derivative_scope_semantics": (
                                "AST_ENCLOSING_SCOPE_NOT_LEIBNIZ_EXPANDED_OR_TRANSFERRED"
                            ),
                            "spinor_and_color_slots": context,
                            "source_supply": linear_factor_supply(context),
                        }
                    )
                factor_group_rows: list[dict[str, Any]] = []
                for group in factor_groups.values():
                    selected_count = len(group["selected_background_port_ids"])
                    degree = int(group["field_strength_degree"])
                    quantum_count = degree - selected_count
                    if selected_count == degree == 1:
                        classification = "LINEAR_PURE_BACKGROUND_FACTOR"
                    elif quantum_count == 0:
                        classification = "NONLINEAR_PURE_BACKGROUND_FACTOR"
                    else:
                        classification = "NONLINEAR_MIXED_BACKGROUND_QUANTUM_FACTOR"
                    factor_group_rows.append(
                        {
                            **group,
                            "background_port_count": selected_count,
                            "quantum_port_count": quantum_count,
                            "classification": classification,
                        }
                    )
                join_key = {
                    "graph_id": graph["graph_id"],
                    "graph_hash": graph["graph_hash"],
                    "vertex_id": vertex["vertex_id"],
                    "vertex_family": vertex["family"],
                    "source_term_id": term.term_id,
                    "source_expression_ast_sha256": digest(term.expression),
                    "selected_grammar_port_ids_in_ast_order": [
                        item["port_id"] for item in selected
                    ],
                    "topology_port_ids_in_source_assignment_order": [
                        item["port_id"] for item in external_order
                    ],
                    "external_momenta_in_source_assignment_order": [
                        item["momentum"] for item in external_order
                    ],
                }
                candidate_id = (
                    f"{graph['graph_id']}::{vertex['vertex_id']}::{term.term_id}::"
                    f"B{'.'.join(str(index) for index in selected_indices)}::"
                    f"E{external_permutation_ordinal}"
                )
                row = {
                    "projection_candidate_id": candidate_id,
                    "status": JOIN_STATUS,
                    "join_key": join_key,
                    "join_key_sha256": digest(join_key),
                    "graph_id": graph["graph_id"],
                    "vertex_id": vertex["vertex_id"],
                    "source_term_id": term.term_id,
                    "source_term_family": term.family,
                    "source_expression_ast_sha256": digest(term.expression),
                    "source_term_coefficient_raw": term.coefficient.as_json(),
                    "source_term_coefficient_role": (
                        "PROVENANCE_ONLY_NOT_AN_ASSEMBLED_VERTEX_OR_GRAPH_COEFFICIENT"
                    ),
                    "measure_chirality": measure_chirality(term),
                    "ordered_source_ports": [port["port_id"] for port in ports],
                    "ordered_role_word": role_word,
                    "ordered_split_term_coefficient": coefficient_one(),
                    "ordered_split_term_multiplicity": 1,
                    "selected_background_source_indices": list(selected_indices),
                    "external_permutation_ordinal": external_permutation_ordinal,
                    "external_permutation": [item["momentum"] for item in external_order],
                    "background_port_projections": port_rows,
                    "factor_groups": factor_group_rows,
                    "unselected_quantum_port_ids": [
                        port["port_id"] for port in ports if port["port_id"] not in selected_ids
                    ],
                    "quantum_join": None,
                    "assembled_vertex_coefficient": None,
                    "assembled_vertex_coefficient_status": GRAPH_COEFFICIENT_STATUS,
                }
                row["projection_candidate_sha256"] = digest(row)
                result.append(row)
    result.sort(key=lambda row: row["projection_candidate_id"])
    ids = [row["projection_candidate_id"] for row in result]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate vertex projection candidate id")
    return result


def mixed_radix_unrank(rank: int, radices: Sequence[int]) -> tuple[int, ...]:
    cardinality = prod(radices)
    if rank < 0 or rank >= cardinality:
        raise ValueError(f"rank {rank} outside [0,{cardinality})")
    indices = [0] * len(radices)
    residual = rank
    for position in range(len(radices) - 1, -1, -1):
        residual, indices[position] = divmod(residual, radices[position])
    return tuple(indices)


@dataclass(frozen=True)
class GraphProjection:
    graph: dict[str, Any]
    background_vertex_order: tuple[str, ...]
    local_candidates: dict[str, list[dict[str, Any]]]

    @property
    def radices(self) -> tuple[int, ...]:
        return tuple(len(self.local_candidates[vertex]) for vertex in self.background_vertex_order)

    @property
    def cardinality(self) -> int:
        return prod(self.radices)

    def unrank(self, rank: int) -> tuple[dict[str, Any], ...]:
        indices = mixed_radix_unrank(rank, self.radices)
        return tuple(
            self.local_candidates[vertex][index]
            for vertex, index in zip(self.background_vertex_order, indices, strict=True)
        )

    def candidate_id(self, rank: int) -> str:
        width = max(1, len(str(self.cardinality - 1)))
        return f"{self.graph['graph_id']}::P{rank:0{width}d}"

    def materialize(self, rank: int) -> dict[str, Any]:
        selected = self.unrank(rank)
        projections = [
            port
            for candidate in selected
            for port in candidate["background_port_projections"]
        ]
        momenta = sorted(port["external_momentum"] for port in projections)
        if momenta != ["p1", "p2"]:
            raise ValueError("every graph projection must carry p1 and p2 exactly once")
        row = {
            "graph_projection_candidate_id": self.candidate_id(rank),
            "rank": rank,
            "graph_id": self.graph["graph_id"],
            "valid_orientations": ["direct", "reflected"],
            "orientation_policy": (
                "BACKGROUND_PORT_AST_PROJECTION_IS_INVARIANT_UNDER_INTERNAL_EDGE_REFLECTION"
            ),
            "selected_vertex_projection_candidate_ids": [
                candidate["projection_candidate_id"] for candidate in selected
            ],
            "background_port_projections": projections,
            "external_momentum_multiset": momenta,
            "source_to_quantum_edge_join": None,
            "propagator": None,
            "wick_contraction": None,
            "d_algebra": None,
            "amplitude": None,
            "assembled_graph_coefficient": None,
            "assembled_graph_coefficient_status": GRAPH_COEFFICIENT_STATUS,
        }
        row["graph_projection_candidate_sha256"] = digest(row)
        return row


def build_runtime() -> tuple[dict[str, Any], list[GraphProjection]]:
    topology_bundle = graphir.build_bundle()
    graphs = topology_bundle["literal_direct_graphs"]
    if tuple(graph["graph_id"] for graph in graphs) != SUPPORTED_GRAPH_IDS:
        raise ValueError("the three decorated literal K4-minus-edge graph ids changed")
    projections: list[GraphProjection] = []
    for graph in graphs:
        background_vertices = tuple(
            vertex for vertex in graph["vertices"] if vertex["background_valence"] > 0
        )
        if sum(vertex["background_valence"] for vertex in background_vertices) != 2:
            raise ValueError("each decorated graph must have exactly two background ports")
        local = {
            vertex["vertex_id"]: vertex_projection_candidates(graph, vertex)
            for vertex in background_vertices
        }
        if any(not rows for rows in local.values()):
            raise ProjectionSourceBlocked(f"{graph['graph_id']}: empty projection catalog")
        projections.append(
            GraphProjection(
                graph=dict(graph),
                background_vertex_order=tuple(vertex["vertex_id"] for vertex in background_vertices),
                local_candidates=local,
            )
        )
    provenance = {
        "grammar_generator": "scripts/step6_two_loop_grammar.py",
        "grammar_generator_sha256": file_sha256(ROOT / "scripts/step6_two_loop_grammar.py"),
        "topology_generator": "scripts/step6_two_loop_graphir.py",
        "topology_generator_sha256": file_sha256(ROOT / "scripts/step6_two_loop_graphir.py"),
        "topology_bundle_sha256": digest(topology_bundle),
        "input_authority_role": "UNMERGED_PROPOSAL_INPUTS_NOT_COMPUTATIONAL_EVIDENCE",
    }
    return provenance, projections


def projection_as_json(projection: GraphProjection) -> dict[str, Any]:
    stream = sha256()
    for rank in range(projection.cardinality):
        selected = projection.unrank(rank)
        stream.update(
            canonical_json(
                {
                    "rank": rank,
                    "ids": [item["projection_candidate_id"] for item in selected],
                }
            ).encode("utf-8")
        )
        stream.update(b"\n")
    row = {
        "graph_id": projection.graph["graph_id"],
        "graph_hash": projection.graph["graph_hash"],
        "topology": projection.graph["topology"],
        "background_vertex_order": list(projection.background_vertex_order),
        "local_projection_candidate_catalogs": projection.local_candidates,
        "factorized_graph_projection_enumeration": {
            "representation": "EXACT_FACTORIZED_CARTESIAN_PRODUCT",
            "radices": list(projection.radices),
            "cardinality": projection.cardinality,
            "first_candidate_id": projection.candidate_id(0),
            "last_candidate_id": projection.candidate_id(projection.cardinality - 1),
            "stream_sha256": stream.hexdigest(),
        },
        "samples_only": {
            "first": projection.materialize(0),
            "middle": projection.materialize(projection.cardinality // 2),
            "last": projection.materialize(projection.cardinality - 1),
        },
        "orientation_covariance": {
            "valid_orientations": ["direct", "reflected"],
            "reason": "reflection changes only internal-edge directions and momenta",
        },
        "downstream_fail_closed": {
            "quantum_port_to_edge_join": None,
            "propagator": None,
            "wick_contraction": None,
            "d_algebra": None,
            "amplitude": None,
            "assembled_graph_coefficient": None,
            "status": GRAPH_COEFFICIENT_STATUS,
        },
    }
    row["graph_projection_sha256"] = digest(row)
    return row


def build_payload() -> tuple[dict[str, Any], list[GraphProjection]]:
    provenance, runtime = build_runtime()
    rows = [projection_as_json(projection) for projection in runtime]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "stage": "PROJECT_EXTERNAL_BACKGROUND_PROJECTION_ONLY",
        "scope": "THREE_DECORATED_LITERAL_K4_MINUS_EDGE_PURE_GAUGE_PARENTS",
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "input_provenance": provenance,
        "ordered_bridge_split": ordered_split_certificate(),
        "linear_project_maps": linear_map_certificate(),
        "graphs": rows,
        "exact_total_graph_projection_candidates": sum(
            projection.cardinality for projection in runtime
        ),
        "coefficient_policy": {
            "source_term_raw_coefficients": "RETAINED_AS_AST_PROVENANCE",
            "ordered_split_coefficient": "EXACTLY_ONE_PER_LABELED_ROLE_WORD",
            "assembled_vertex_coefficient": None,
            "assembled_graph_coefficient": None,
            "status": GRAPH_COEFFICIENT_STATUS,
        },
        "forbidden_stages": [
            "QUANTUM_PORT_TO_EDGE_JOIN",
            "PROPAGATOR",
            "WICK_CONTRACTION",
            "D_ALGEBRA",
            "AMPLITUDE",
            "GRAPH_COEFFICIENT",
            "SUBTRACTION",
        ],
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    )
    return payload, runtime


def iter_materialized(projection: GraphProjection) -> Iterator[dict[str, Any]]:
    for rank in range(projection.cardinality):
        yield projection.materialize(rank)


def exact_checks(
    payload: Mapping[str, Any], runtime: Sequence[GraphProjection]
) -> dict[str, bool]:
    by_id = {projection.graph["graph_id"]: projection for projection in runtime}
    expected_radices = {
        "G6_DIRECT_K4ME_I3_S3CUBED": (12, 12),
        "G6_DIRECT_K4ME_I2_S3SQ_S4": (12, 24),
        "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": (72,),
    }
    expected_cardinalities = {
        graph_id: prod(radices) for graph_id, radices in expected_radices.items()
    }
    maps = payload["linear_project_maps"]["maps"]
    all_local = [
        candidate
        for projection in runtime
        for vertex in projection.background_vertex_order
        for candidate in projection.local_candidates[vertex]
    ]
    all_materialized = [row for projection in runtime for row in iter_materialized(projection)]
    nonlinear_supply = [
        port["source_supply"]
        for candidate in all_local
        for port in candidate["background_port_projections"]
        if port["spinor_and_color_slots"]["field_strength_degree"] > 1
    ]
    double = by_id["G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"]
    double_local = double.local_candidates["C"]
    split = payload["ordered_bridge_split"]["degrees"]
    return {
        "status_is_proposal_only": payload["status"] == STATUS,
        "exactly_three_decorated_graphs": tuple(by_id) == SUPPORTED_GRAPH_IDS,
        "all_topologies_are_literal_k4_minus_edge": all(
            projection.graph["topology"] == "K4_MINUS_ONE_EDGE" for projection in runtime
        ),
        "ordered_split_role_words_are_unique_and_unit_multiplicity": all(
            row["role_word_count"] == row["unique_role_word_count"] == 2 ** row["ordered_degree"]
            and row["multiplicity_of_every_labeled_role_word"] == 1
            and row["coefficient_of_every_labeled_role_word"]["rendered"] == "1"
            for row in split
        ),
        "ordered_split_fixed_b_counts_are_binomial_census_only": all(
            row["fixed_background_distribution"] == row["binomial_distribution"] for row in split
        ),
        "linear_gamma_map_exact": maps["Gamma_(1)+"]["coefficient"]["rendered"] == "1"
        and maps["Gamma_(1)+"]["derivative_word_outer_to_inner"] == ["D_+"],
        "linear_w_map_exact": maps["W_(1)+"]["coefficient"]["rendered"] == "-1/8"
        and maps["W_(1)+"]["derivative_word_outer_to_inner"] == ["barD^2", "D_+"],
        "linear_x_map_exact": maps["X_(1)"]["coefficient"]["rendered"] == "-1/8"
        and maps["X_(1)"]["derivative_word_outer_to_inner"]
        == ["D_+", "barD^2", "D_+"]
        and maps["X_(1)"]["connection_sum_at_degree_one"] == [],
        "linear_tilde_gamma_map_exact": maps["TildeGamma_(1)dot_a"]["coefficient"]["rendered"]
        == "-1"
        and maps["TildeGamma_(1)dot_a"]["derivative_word_outer_to_inner"]
        == ["barD_dot_a"],
        "linear_tilde_w_map_exact": maps["TildeW_(1)dot_a"]["coefficient"]["rendered"]
        == "-1/8"
        and maps["TildeW_(1)dot_a"]["derivative_word_outer_to_inner"]
        == ["D^2", "barD_dot_a"],
        "exact_projection_radices": all(
            by_id[graph_id].radices == radices for graph_id, radices in expected_radices.items()
        ),
        "exact_projection_cardinalities": all(
            by_id[graph_id].cardinality == cardinality
            for graph_id, cardinality in expected_cardinalities.items()
        )
        and payload["exact_total_graph_projection_candidates"] == 504,
        "double_background_s4_has_both_external_permutations": len(double_local) == 72
        and sum(row["external_permutation"] == ["p1", "p2"] for row in double_local) == 36
        and sum(row["external_permutation"] == ["p2", "p1"] for row in double_local) == 36,
        "each_graph_projection_has_p1_p2_once": all(
            row["external_momentum_multiset"] == ["p1", "p2"] for row in all_materialized
        ),
        "all_source_joins_have_deterministic_keys": all(
            candidate["status"] == JOIN_STATUS
            and candidate["join_key_sha256"] == digest(candidate["join_key"])
            for candidate in all_local
        ),
        "all_port_derivative_words_match_source_ast": all(
            port["derivative_word_outer_to_inner"]
            == next(
                source["derivative_word_outer_to_inner"]
                for term in action_terms_for_vertex(
                    next(
                        vertex
                        for projection in runtime
                        if projection.graph["graph_id"] == candidate["graph_id"]
                        for vertex in projection.graph["vertices"]
                        if vertex["vertex_id"] == candidate["vertex_id"]
                    )
                )
                if term.term_id == candidate["source_term_id"]
                for source in grammar.collect_ports(term.expression)
                if source["port_id"] == port["grammar_port_id"]
            )
            for candidate in all_local
            for port in candidate["background_port_projections"]
        ),
        "measure_chirality_is_exactly_parallel": all(
            candidate["measure_chirality"]
            in (
                {"measure": "E_PLUS_CHIRAL", "chirality": "CHIRAL", "sector": "PLUS"},
                {
                    "measure": "E_MINUS_ANTICHIRAL",
                    "chirality": "ANTICHIRAL",
                    "sector": "MINUS",
                },
            )
            for candidate in all_local
        ),
        "spinor_and_color_slots_are_retained": all(
            port["spinor_and_color_slots"]["spinor_slot"]
            and port["spinor_and_color_slots"]["factor_output_color_slot"] in ("A", "B")
            and port["spinor_and_color_slots"]["gauge_color_pairing"] == "kappa[A,B]"
            for candidate in all_local
            for port in candidate["background_port_projections"]
        ),
        "nonlinear_ports_never_claim_linear_letters": bool(nonlinear_supply)
        and all(
            supply["status"] == "EXACT_NONLINEAR_SOURCE_FACTOR_RETAINED"
            and supply["standalone_linear_projector"] is None
            for supply in nonlinear_supply
        ),
        "orientation_covariance_is_projection_only": all(
            row["orientation_covariance"]["valid_orientations"] == ["direct", "reflected"]
            for row in payload["graphs"]
        ),
        "source_coefficients_retained_but_not_assembled": all(
            candidate["source_term_coefficient_raw"]["field"] == "Q(i)"
            and candidate["assembled_vertex_coefficient"] is None
            for candidate in all_local
        )
        and all(row["assembled_graph_coefficient"] is None for row in all_materialized),
        "downstream_stages_fail_closed": set(payload["forbidden_stages"])
        == {
            "QUANTUM_PORT_TO_EDGE_JOIN",
            "PROPAGATOR",
            "WICK_CONTRACTION",
            "D_ALGEBRA",
            "AMPLITUDE",
            "GRAPH_COEFFICIENT",
            "SUBTRACTION",
        }
        and payload["coefficient_policy"]["assembled_graph_coefficient"] is None,
        "no_external_target_used": payload["external_result_used_as_calculation_input"] is False,
    }


def build_audit(payload: Mapping[str, Any], runtime: Sequence[GraphProjection]) -> dict[str, Any]:
    checks = exact_checks(payload, runtime)
    return {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "scope": "STEP6_EXTERNAL_BACKGROUND_PROJECTION_VERIFICATION",
        "checks": checks,
        "summary": {
            "passed": sum(checks.values()),
            "failed": sum(not value for value in checks.values()),
            "total": len(checks),
        },
        "gaps": [
            "quantum grammar ports are not yet joined to topology edge endpoints for all three graphs",
            "propagators, Wick contractions, D-algebra, amplitudes, graph coefficients, and subtraction are absent",
            "nonlinear W_(n) and TildeW_(n) background ports remain exact AST contexts and are not renamed as linear external letters",
        ],
    }


def render_markdown(payload: Mapping[str, Any]) -> str:
    maps = payload["linear_project_maps"]["maps"]
    rows = [
        "# Step 6 — Project external-background projection",
        "",
        "$$",
        "V_i=V_{B,i}+v_i,\\qquad",
        "F(V_1,\\ldots,V_t)=\\sum_{\\rho\\in\\{B,q\\}^t}",
        "F(V_{\\rho_1,1},\\ldots,V_{\\rho_t,t}),",
        "\\qquad [F_\\rho]=1.",
        "$$",
        "",
        "$$",
        r"\Gamma_{(1)+}[V_B]=D_+V_B,",
        r"\qquad W_{(1)+}[V_B]=-\frac18\bar D^2D_+V_B,",
        "$$",
        "",
        "$$",
        r"X_{(1)}[V_B]=D_+W_{(1)+}[V_B]",
        r"=-\frac18D_+\bar D^2D_+V_B=K_+V_B,",
        r"\qquad K_+:=-\frac18D_+\bar D^2D_+.",
        "$$",
        "",
        "$$",
        r"\widetilde\Gamma_{(1)\dot a}[V_B]=-\bar D_{\dot a}V_B,",
        r"\qquad \widetilde W_{(1)\dot a}[V_B]",
        r"=-\frac18D^2\bar D_{\dot a}V_B.",
        "$$",
        "",
        "| GraphIR | local radices | candidates |",
        "|---|---:|---:|",
    ]
    for graph in payload["graphs"]:
        enumeration = graph["factorized_graph_projection_enumeration"]
        rows.append(
            f"| `{graph['graph_id']}` | `{enumeration['radices']}` | "
            f"{enumeration['cardinality']} |"
        )
    rows.extend(
        [
            "",
            "$$",
            "N_{\\rm projection}=12\\cdot12+12\\cdot24+72=504.",
            "$$",
            "",
            "Nonlinear source factors remain their exact ordered AST; no linear-letter rename is made.",
            "",
            f"Linear-map AST hashes: `{digest(maps)}`.",
            "",
            "Quantum-edge join, propagators, Wick contractions, D-algebra, amplitudes, and graph coefficients are absent.",
            "",
        ]
    )
    return "\n".join(rows)


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload, runtime = build_payload()
    audit = build_audit(payload, runtime)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    GENERATED_MD.write_text(render_markdown(payload))
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")
    return payload, audit


def main() -> int:
    _, audit = write_outputs()
    print(json.dumps(audit["summary"], sort_keys=True))
    return 0 if audit["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
