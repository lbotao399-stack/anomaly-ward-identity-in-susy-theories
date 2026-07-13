#!/usr/bin/env python3
"""Proposal-only Step-6 pre-D-algebra AmplitudeIR compiler.

The compiler joins the exact factorized Wick enumeration to the exact
Project external-background projection certificate and then attaches only
the Step-5A Fermi--Feynman vector Green kernel.  The 2,985,984 labeled rows
remain a mixed-radix product; only deterministic samples are materialized.

No D-algebra word is reduced, no pairing is summed, and no loop integral,
pole, subtraction, anomaly, or renormalized coefficient is evaluated.
"""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import importlib
import json
from math import prod
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_external_projection as projection
    from scripts import step6_two_loop_grammar as grammar
    from scripts import step6_two_loop_graphir as graphir
    from scripts import step6_two_loop_wick as wick
    from scripts import verify_step5a_fixed_kernel as fixed_kernel
except ModuleNotFoundError:  # direct execution
    import step6_external_projection as projection
    import step6_two_loop_grammar as grammar
    import step6_two_loop_graphir as graphir
    import step6_two_loop_wick as wick
    import verify_step5a_fixed_kernel as fixed_kernel


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/two-loop-amplitude-ir"
GENERATED_JSON = GENERATED_DIR / "pre-dalgebra-amplitude-ir.json"
GENERATED_MD = GENERATED_DIR / "pre-dalgebra-amplitude-ir.md"
AUDIT = ROOT / "audits/step6-two-loop-amplitude-ir-verification.json"

SCHEMA_VERSION = "step6.two_loop_amplitude_ir.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
STAGE = "PRE_DALGEBRA_AMPLITUDE_IR"
AMPLITUDE_SUM_STATUS = "BLOCKED_NO_DALGEBRA_OR_LABELED_PAIRING_SUM"
DALGEBRA_STATUS = "BLOCKED_EDGE_TAGGED_DALGEBRA_NOT_COMPILED"
NUMERATOR_STATUS = "BLOCKED_DALGEBRA_NUMERATOR_ABSENT"
INTEGRAL_STATUS = "BLOCKED_DALGEBRA_NUMERATOR_ABSENT"
COEFFICIENT_STATUS = "BLOCKED_RENORMALIZED_TWO_LOOP_AMPLITUDE_ABSENT"


class AmplitudeIRError(ValueError):
    """Base fail-closed AmplitudeIR error."""


class ProjectionJoinError(AmplitudeIRError):
    """Raised for a missing, duplicate, or mismatched background join."""


class PropagatorContractError(AmplitudeIRError):
    """Raised when an edge is not attached to the Project Step-5A kernel."""


class CoefficientApplicationError(AmplitudeIRError):
    """Raised when a source or projector coefficient would be applied twice."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qi_from_json(value: Mapping[str, Any]) -> grammar.QI:
    if value.get("field") != "Q(i)":
        raise CoefficientApplicationError("raw Project coefficients must lie in Q(i)")
    return grammar.QI(
        Fraction(str(value["rational"])),
        int(value["i_power_reduced"]),
        tuple(str(symbol) for symbol in value.get("symbols", ())),
    )


def fraction_from_json(value: Mapping[str, Any]) -> Fraction:
    if value.get("field") != "Q":
        raise CoefficientApplicationError("expansion coefficient must lie in Q")
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def step5a_kernel_certificate() -> dict[str, Any]:
    verification = fixed_kernel.run_verification()
    required = {
        "K_V^tot": "-(h/2)*kappa_AB*p_(4)^2*1_16",
        "G_V": "-2*g^2*kappa^AB*1_16/p_(4)^2",
        "left_product": "K_(AB)^tot*G^(BC)=delta_A^C*1_16",
        "right_product": "G^(AB)*K_(BC)^tot=delta^A_C*1_16",
    }
    if verification.get("status") != "PASS":
        raise PropagatorContractError("Step-5A fixed-kernel verification did not pass")
    equations = verification.get("derived_equations", {})
    if any(equations.get(name) != equation for name, equation in required.items()):
        raise PropagatorContractError("Step-5A symbolic kernel equations changed")
    if verification.get("totals", {}).get("failed") != 0:
        raise PropagatorContractError("Step-5A fixed-kernel checks contain failures")
    return {
        "scope": verification["scope"],
        "admission_status": verification["admission_status"],
        "arithmetic": verification["arithmetic"],
        "derived_equations": required,
        "grassmann_representation": "identity_16",
        "two_sided_inverse_checks": {
            "left": True,
            "right": True,
        },
        "verification_check_count": verification["totals"]["checks"],
        "verification_sha256": digest(verification),
    }


def background_momentum_by_topology_port(graph: Mapping[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for vertex in graph["vertices"]:
        for port in vertex["background_ports"]:
            port_id = str(port["port_id"])
            if port_id in result:
                raise ProjectionJoinError(f"duplicate topology background port {port_id}")
            result[port_id] = str(port["momentum"])
    return result


def projection_join_key_from_wick(
    join: wick.ParentJoin,
    vertex: Mapping[str, Any],
    option: Mapping[str, Any],
    assignment: Mapping[str, Any],
) -> dict[str, Any]:
    if option["assignment_id"] != assignment["assignment_id"]:
        raise ProjectionJoinError("local option and B/Q assignment ids disagree")
    if option["source_term_id"] != assignment["source_term_id"]:
        raise ProjectionJoinError("local option and B/Q source terms disagree")
    if option["vertex_id"] != vertex["vertex_id"]:
        raise ProjectionJoinError("local option and topology vertex disagree")
    rows = assignment["background_projection_join"][
        "labeled_background_port_bijection"
    ]
    if len(rows) != int(vertex["background_valence"]):
        raise ProjectionJoinError("background-port join has the wrong cardinality")
    grammar_occurrences = [str(row["grammar_port_occurrence_id"]) for row in rows]
    expected_occurrences = [
        f"{vertex['vertex_id']}::{row['grammar_port_id']}" for row in rows
    ]
    if grammar_occurrences != expected_occurrences:
        raise ProjectionJoinError("grammar background port occurrence id changed")
    grammar_ports = [str(row["grammar_port_id"]) for row in rows]
    topology_ports = [str(row["topology_background_port_id"]) for row in rows]
    if len(grammar_ports) != len(set(grammar_ports)):
        raise ProjectionJoinError("duplicate grammar background port in join")
    if len(topology_ports) != len(set(topology_ports)):
        raise ProjectionJoinError("duplicate topology background port in join")
    momentum_by_port = background_momentum_by_topology_port(join.graph)
    if any(port not in momentum_by_port for port in topology_ports):
        raise ProjectionJoinError("background join names a missing topology port")
    term = join.term_dictionary[option["source_term_id"]]
    return {
        "graph_id": join.graph["graph_id"],
        "graph_hash": join.graph["graph_hash"],
        "vertex_id": vertex["vertex_id"],
        "vertex_family": vertex["family"],
        "source_term_id": option["source_term_id"],
        "source_expression_ast_sha256": term["expression_ast_sha256"],
        "selected_grammar_port_ids_in_ast_order": grammar_ports,
        "topology_port_ids_in_source_assignment_order": topology_ports,
        "external_momenta_in_source_assignment_order": [
            momentum_by_port[port] for port in topology_ports
        ],
    }


def build_projection_index(
    runtime: Sequence[projection.GraphProjection],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_key: dict[str, dict[str, Any]] = {}
    by_id: dict[str, dict[str, Any]] = {}
    for graph_projection in runtime:
        for vertex_id in graph_projection.background_vertex_order:
            for candidate in graph_projection.local_candidates[vertex_id]:
                key = canonical_json(candidate["join_key"])
                candidate_id = str(candidate["projection_candidate_id"])
                if key in by_key:
                    raise ProjectionJoinError("two projection candidates share one join key")
                if candidate_id in by_id:
                    raise ProjectionJoinError("duplicate projection candidate id")
                if digest(candidate["join_key"]) != candidate["join_key_sha256"]:
                    raise ProjectionJoinError("projection join-key hash mismatch")
                by_key[key] = candidate
                by_id[candidate_id] = candidate
    return by_key, by_id


def validate_projection_candidate(
    join: wick.ParentJoin,
    vertex: Mapping[str, Any],
    option: Mapping[str, Any],
    assignment: Mapping[str, Any],
    candidate: Mapping[str, Any],
) -> dict[str, Any]:
    expected_key = projection_join_key_from_wick(join, vertex, option, assignment)
    if candidate.get("join_key") != expected_key:
        raise ProjectionJoinError("Wick B/Q assignment and projection join key disagree")
    if candidate.get("join_key_sha256") != digest(expected_key):
        raise ProjectionJoinError("projection join-key certificate is invalid")
    if candidate.get("source_term_coefficient_raw") != option["coefficient_raw"]:
        raise CoefficientApplicationError("projection and Wick raw source coefficient disagree")
    if candidate.get("assembled_vertex_coefficient") is not None:
        raise CoefficientApplicationError("projection candidate already assembled a coefficient")
    if candidate.get("ordered_split_term_coefficient", {}).get("rendered") != "1":
        raise CoefficientApplicationError("ordered background split coefficient is not one")
    if candidate.get("ordered_split_term_multiplicity") != 1:
        raise CoefficientApplicationError("ordered background split multiplicity is not one")
    selected_rows = list(candidate.get("background_port_projections", ()))
    if len(selected_rows) != int(vertex["background_valence"]):
        raise ProjectionJoinError("projection candidate has missing background ports")
    grammar_ports = [row["grammar_port_id"] for row in selected_rows]
    topology_ports = [row["topology_port_id"] for row in selected_rows]
    if len(grammar_ports) != len(set(grammar_ports)):
        raise ProjectionJoinError("projection candidate duplicates a grammar port")
    if len(topology_ports) != len(set(topology_ports)):
        raise ProjectionJoinError("projection candidate duplicates a topology port")
    if grammar_ports != expected_key["selected_grammar_port_ids_in_ast_order"]:
        raise ProjectionJoinError("projection candidate reordered grammar background ports")
    if topology_ports != expected_key["topology_port_ids_in_source_assignment_order"]:
        raise ProjectionJoinError("projection candidate reordered topology background ports")
    if [row["external_momentum"] for row in selected_rows] != expected_key[
        "external_momenta_in_source_assignment_order"
    ]:
        raise ProjectionJoinError("projection candidate changed p1/p2 source order")
    if candidate.get("unselected_quantum_port_ids") != [
        port["port_id"] for port in assignment["quantum_grammar_ports"]
    ]:
        raise ProjectionJoinError("projection quantum complement disagrees with Wick B/Q split")
    for row in selected_rows:
        supply = row["source_supply"]
        if "coefficient_application" in supply and supply["coefficient_application"] != (
            "ALREADY_CONTAINED_IN_SOURCE_TERM_RAW_COEFFICIENT_DO_NOT_MULTIPLY_AGAIN"
        ):
            raise CoefficientApplicationError("external projector coefficient policy changed")
    return expected_key


def join_local_option(
    join: wick.ParentJoin,
    vertex: Mapping[str, Any],
    option: Mapping[str, Any],
    assignment: Mapping[str, Any],
    projection_by_key: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    background_valence = int(vertex["background_valence"])
    projection_ref: dict[str, Any]
    if background_valence == 0:
        if assignment["background_grammar_ports"]:
            raise ProjectionJoinError("zero-background vertex has background grammar ports")
        projection_ref = {
            "status": "NOT_APPLICABLE_EXACT_B0_VERTEX",
            "projection_candidate_id": None,
            "projection_candidate_sha256": None,
            "join_key_sha256": None,
            "external_projector_coefficient_applied_separately": False,
        }
    else:
        join_key = projection_join_key_from_wick(join, vertex, option, assignment)
        candidate = projection_by_key.get(canonical_json(join_key))
        if candidate is None:
            raise ProjectionJoinError("missing projection candidate for Wick B/Q assignment")
        validate_projection_candidate(join, vertex, option, assignment, candidate)
        projection_ref = {
            "status": "EXACT_BIJECTIVE_PROJECT_BACKGROUND_JOIN",
            "projection_candidate_id": candidate["projection_candidate_id"],
            "projection_candidate_sha256": candidate["projection_candidate_sha256"],
            "join_key_sha256": candidate["join_key_sha256"],
            "external_projector_coefficient_applied_separately": False,
            "source_term_raw_coefficient_applied_once_at_amplitude_stage": True,
        }
    row = {
        "local_amplitude_option_id": option["local_option_id"],
        "source_wick_local_option_sha256": option["local_option_sha256"],
        "orientation": option["orientation"],
        "vertex_id": option["vertex_id"],
        "source_term_id": option["source_term_id"],
        "assignment_id": option["assignment_id"],
        "t": option["t"],
        "b": option["b"],
        "q": option["q"],
        "measure": option["measure"],
        "chirality": option["chirality"],
        "coefficient_raw": option["coefficient_raw"],
        "color_ast_ref": option["color_ast_ref"],
        "color_ast_sha256": option["color_ast_sha256"],
        "expression_ast_ref": option["expression_ast_ref"],
        "expression_ast_sha256": option["expression_ast_sha256"],
        "quantum_attachment": option["quantum_attachment"],
        "quantum_bijection": option["quantum_bijection"],
        "background_projection": projection_ref,
    }
    row["local_amplitude_option_sha256"] = digest(row)
    return row


def _denominator_factor(
    graph: Mapping[str, Any], oriented_edge: Mapping[str, Any]
) -> dict[str, Any]:
    vector = tuple(int(value) for value in oriented_edge["momentum_vector"])
    canonical = graphir.canonical_square_argument(vector)
    factor = {
        "op": "power",
        "exponent": 1,
        "base": {
            "op": "square",
            "bilinear_form": "POSITIVE_EUCLIDEAN",
            "space": graphir.SQUARE_SPACE,
            "argument": graphir.linear_ast(canonical),
        },
        "edge_id": oriented_edge["edge_id"],
    }
    source = next(
        item
        for item in graph["denominator_ast"]["factors"]
        if item["edge_id"] == oriented_edge["edge_id"]
    )
    if factor != source:
        raise PropagatorContractError("orientation square does not equal GraphIR denominator")
    return factor


def attach_vector_propagator(
    graph: Mapping[str, Any],
    orientation: str,
    edge: Mapping[str, Any],
    kernel_certificate: Mapping[str, Any],
) -> dict[str, Any]:
    expected_equation = "-2*g^2*kappa^AB*1_16/p_(4)^2"
    if kernel_certificate.get("derived_equations", {}).get("G_V") != expected_equation:
        raise PropagatorContractError("non-Project vector propagator rejected")
    if kernel_certificate.get("grassmann_representation") != "identity_16":
        raise PropagatorContractError("vector propagator is not identity_16")
    if edge.get("field_type") != "V_QUANTUM_WICK_TO_V_QUANTUM_WICK":
        raise PropagatorContractError("Step-5A vector kernel cannot contract this edge type")
    denominator = _denominator_factor(graph, edge)
    source_theta = f"theta_{edge['source']['vertex_id']}"
    target_theta = f"theta_{edge['target']['vertex_id']}"
    source_color = f"{edge['edge_id']}.C_source"
    target_color = f"{edge['edge_id']}.D_target"
    propagator = {
        "schema_version": "step6.project_vector_propagator_ir.v1",
        "source_scope": "STEP5A_PERTURBATIVE_FERMI_FEYNMAN",
        "equation": (
            "G_V^{CD}(r)=-2*g^2*kappa^{CD}*"
            "Delta^4(theta_source-theta_target)*identity_16/r^2"
        ),
        "edge_id": edge["edge_id"],
        "orientation": orientation,
        "oriented_source_vertex": edge["source"]["vertex_id"],
        "oriented_target_vertex": edge["target"]["vertex_id"],
        "momentum": edge["momentum"],
        "momentum_vector": edge["momentum_vector"],
        "coefficient": grammar.QI(-2, symbols=("g^2",)).as_json(),
        "inverse_Hessian_kernel": "G_V",
        "Wick_contraction": "hbar*G_V",
        "Wick_hbar_factor": {"base": "hbar", "power": 1, "rendered": "hbar"},
        "color_ast": {
            "op": "inverse_metric",
            "tensor": "kappa",
            "upper_indices": [source_color, target_color],
        },
        "grassmann_delta_ast": {
            "op": "GrassmannDelta",
            "degree": 4,
            "argument": {
                "op": "difference",
                "left": source_theta,
                "right": target_theta,
            },
        },
        "grassmann_operator": "identity_16",
        "denominator": denominator,
        "kernel_verification_sha256": kernel_certificate["verification_sha256"],
    }
    propagator["propagator_sha256"] = digest(propagator)
    return propagator


def _enrich_endpoint(
    endpoint: Mapping[str, Any], term_dictionary: Mapping[str, Mapping[str, Any]]
) -> dict[str, Any]:
    term = term_dictionary[endpoint["source_term_id"]]
    matching = [
        port for port in term["ports"] if port["port_id"] == endpoint["grammar_port_id"]
    ]
    if len(matching) != 1:
        raise AmplitudeIRError("endpoint grammar port does not resolve uniquely")
    port = matching[0]
    if port["derivative_word_outer_to_inner"] != endpoint[
        "grammar_derivative_word_outer_to_inner"
    ]:
        raise AmplitudeIRError("endpoint derivative word drifted from source AST")
    return {
        **endpoint,
        "grammar_port_record": port,
        "source_expression_ast_ref": term["term_id"],
        "source_expression_ast_sha256": term["expression_ast_sha256"],
        "source_color_ast_ref": term["term_id"],
        "source_color_ast_sha256": term["color_ast_sha256"],
        "source_measure": term["measure"],
    }


def exact_coefficient_factorization(
    graph: Mapping[str, Any],
    selected: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    vertex_by_id = {vertex["vertex_id"]: vertex for vertex in graph["vertices"]}
    selected_by_vertex = {option["vertex_id"]: option for option in selected}
    if set(selected_by_vertex) != set(vertex_by_id):
        raise CoefficientApplicationError("coefficient factorization is missing a vertex")
    insertion = [
        selected_by_vertex[vertex_id]
        for vertex_id, vertex in vertex_by_id.items()
        if vertex["role"] == "COMPOSITE_INSERTION"
    ]
    actions = [
        (vertex_id, selected_by_vertex[vertex_id], vertex)
        for vertex_id, vertex in vertex_by_id.items()
        if vertex["role"] == "ACTION_VERTEX"
    ]
    if len(insertion) != 1 or len(actions) != 3:
        raise CoefficientApplicationError("expected one insertion and three action vertices")
    multiplicities: dict[str, int] = {}
    for _, option, vertex in actions:
        sector = wick.action_sector(option["source_term_id"])
        if sector is None:
            raise CoefficientApplicationError("action term has no PLUS/MINUS sector")
        key = f"{vertex['family']}_{sector}"
        multiplicities[key] = multiplicities.get(key, 0) + 1
    raw_sector_expansion = wick.expansion_factor(multiplicities)
    occurrence_orbit = wick.decorated_occurrence_orbit_factor(
        graph, [option for _, option, _ in actions]
    )
    if occurrence_orbit["N"] != 3 or occurrence_orbit["combined_hbar_power"] != -3:
        raise CoefficientApplicationError("three-action occurrence-orbit factor changed")

    raw_insertion = qi_from_json(insertion[0]["coefficient_raw"])
    raw_actions = [qi_from_json(option["coefficient_raw"]) for _, option, _ in actions]
    if any(Counter(value.symbols) != Counter({"h": 1}) for value in raw_actions):
        raise CoefficientApplicationError("each Project action coefficient must contain h once")
    expansion_rational = fraction_from_json(occurrence_orbit["combined_rational"])
    propagator_factors = [grammar.QI(-2, symbols=("g^2",)) for _ in range(5)]
    combined = raw_insertion * expansion_rational
    for value in raw_actions:
        combined = combined * value
    for value in propagator_factors:
        combined = combined * value
    symbols = Counter(combined.symbols)
    if symbols != Counter({"g^2": 5, "h": 3}):
        raise CoefficientApplicationError("raw h and g^2 grades changed")
    rewritten = grammar.QI(
        combined.rational,
        combined.i_power,
        ("g^2", "g^2"),
    )
    return {
        "insertion_raw_Qi": insertion[0]["coefficient_raw"],
        "ordered_action_raw_Qi": [
            {
                "vertex_id": vertex_id,
                "source_term_id": option["source_term_id"],
                "coefficient": option["coefficient_raw"],
                "certificate": (
                    "SOURCE_ACTION_COEFFICIENT_ALREADY_CONTAINS_MINUS_H_OVER_4_"
                    "AND_W_OR_TILDEW_FACTORS"
                ),
            }
            for vertex_id, option, _ in actions
        ],
        "raw_grouped_exponential_factor_for_sector_census_only": raw_sector_expansion,
        "decorated_occurrence_orbit_factor": occurrence_orbit,
        "ordered_vector_Wick_factors": [
            {
                "ordinal": ordinal,
                "inverse_Hessian_GV_coefficient": value.as_json(),
                "Wick_hbar_factor": {
                    "base": "hbar",
                    "power": 1,
                    "rendered": "hbar",
                },
                "combined_rendered": "hbar*(-2*g^2)",
            }
            for ordinal, value in enumerate(propagator_factors, start=1)
        ],
        "bosonic_wick_sign": {
            "value": 1,
            "certificate": "ALL_CONTRACTED_V_PORTS_HAVE_GRASSMANN_PARITY_ZERO",
        },
        "external_projector_coefficient_factor": None,
        "external_projector_coefficient_policy": (
            "ALREADY_CONTAINED_IN_ACTION_RAW_QI_DO_NOT_MULTIPLY_AGAIN"
        ),
        "exact_product_before_h_rewrite": {
            "Qi": combined.as_json(),
            "hbar_power": 2,
            "normalization_exponents": {"g^2": 5, "h": 3, "hbar": 2},
            "hbar_power_certificate": {
                "action_occurrence_orbit_power": -3,
                "five_Wick_edge_power": 5,
                "identity": "-3+5=2",
            },
        },
        "h_equals_inverse_g_squared_rewrite_certificate": {
            "identity": "h=(g^2)^(-1)",
            "input": "(g^2)^5*h^3*hbar^2",
            "step_1": "(g^2)^5*(g^2)^(-3)*hbar^2",
            "step_2": "(g^2)^2*hbar^2",
            "output": "g^4*hbar^2",
            "derived_g2_power": 2,
            "derived_g_power": 4,
        },
        "exact_product_after_h_rewrite": {
            "Qi": rewritten.as_json(),
            "hbar_power": 2,
            "coupling_grade": "g^4",
            "loop_grade": "hbar^2",
        },
        "pairing_sum": None,
        "pairing_sum_status": AMPLITUDE_SUM_STATUS,
    }


def coefficient_signature_histogram(parent: "AmplitudeParent") -> list[dict[str, Any]]:
    grouped: list[list[tuple[str, int, Mapping[str, Any]]]] = []
    for vertex_id in parent.vertex_order:
        by_term: dict[str, list[Mapping[str, Any]]] = {}
        for option in parent.local_options[vertex_id]:
            by_term.setdefault(option["source_term_id"], []).append(option)
        grouped.append(
            [
                (term_id, len(options), options[0])
                for term_id, options in sorted(by_term.items())
            ]
        )
    histogram: dict[str, dict[str, Any]] = {}
    for choices in product(*grouped):
        count = prod(choice[1] for choice in choices)
        factorization = exact_coefficient_factorization(
            parent.graph, [choice[2] for choice in choices]
        )
        signature = {
            "insertion_raw_Qi": factorization["insertion_raw_Qi"],
            "ordered_action_raw_Qi": [
                row["coefficient"] for row in factorization["ordered_action_raw_Qi"]
            ],
            "family_sector_multiplicities": factorization[
                "raw_grouped_exponential_factor_for_sector_census_only"
            ][
                "family_sector_multiplicities"
            ],
            "raw_grouped_exponential_rational": factorization[
                "raw_grouped_exponential_factor_for_sector_census_only"
            ]["rational"],
            "decorated_occurrence_orbit_rational": factorization[
                "decorated_occurrence_orbit_factor"
            ]["combined_rational"],
            "exact_product_before_h_rewrite": factorization[
                "exact_product_before_h_rewrite"
            ],
            "exact_product_after_h_rewrite": factorization[
                "exact_product_after_h_rewrite"
            ],
        }
        key = digest(signature)
        if key not in histogram:
            histogram[key] = {
                "coefficient_signature_sha256": key,
                "signature": signature,
                "labeled_pairing_count": 0,
                "collapsed_term_tuple_count": 0,
            }
        histogram[key]["labeled_pairing_count"] += count
        histogram[key]["collapsed_term_tuple_count"] += 1
    return [histogram[key] for key in sorted(histogram)]


def optional_integral_interface() -> dict[str, dict[str, Any]]:
    try:
        module = importlib.import_module("scripts.step6_two_loop_integrals")
    except ModuleNotFoundError:
        return {}
    bundle = module.build_integral_bundle()
    return {
        family["source_graph_id"]: {
            "status": "OPTIONAL_INTERFACE_LINKED_NOT_A_DEPENDENCY",
            "integral_family_id": family["integral_family_id"],
            "integral_family_hash": family["integral_family_hash"],
            "edge_order": family["edge_order"],
            "source_routing_vectors": {
                denominator["edge_id"]: denominator["source_routing_vector"]
                for denominator in family["denominators"]
            },
            "physical_numerator": None,
        }
        for family in bundle["integral_families"]
    }


@dataclass(frozen=True)
class AmplitudeParent:
    wick_join: wick.ParentJoin
    wick_join_row: dict[str, Any]
    local_options: dict[str, list[dict[str, Any]]]
    projection_dictionary: dict[str, dict[str, Any]]
    term_dictionary: dict[str, dict[str, Any]]
    kernel_certificate: dict[str, Any]
    integral_interface: dict[str, Any] | None

    @property
    def graph(self) -> dict[str, Any]:
        return self.wick_join.graph

    @property
    def orientation(self) -> str:
        return self.wick_join.orientation

    @property
    def vertex_order(self) -> tuple[str, ...]:
        return self.wick_join.vertex_order

    @property
    def radices(self) -> tuple[int, ...]:
        return tuple(len(self.local_options[vertex]) for vertex in self.vertex_order)

    @property
    def cardinality(self) -> int:
        return prod(self.radices)

    def unrank(self, rank: int) -> tuple[dict[str, Any], ...]:
        indices = wick._mixed_radix_unrank(rank, self.radices)
        return tuple(
            self.local_options[vertex_id][index]
            for vertex_id, index in zip(self.vertex_order, indices, strict=True)
        )

    def rank(self, selected: Sequence[Mapping[str, Any]]) -> int:
        if len(selected) != len(self.vertex_order):
            raise ValueError("one local amplitude option is required per vertex")
        indices: list[int] = []
        for vertex_id, option in zip(self.vertex_order, selected, strict=True):
            ids = [
                row["local_amplitude_option_id"] for row in self.local_options[vertex_id]
            ]
            indices.append(ids.index(option["local_amplitude_option_id"]))
        return wick._mixed_radix_rank(indices, self.radices)

    def amplitude_id(self, rank: int) -> str:
        width = max(1, len(str(self.cardinality - 1)))
        return f"{self.graph['graph_id']}::{self.orientation}::A{rank:0{width}d}"

    def materialize(self, rank: int) -> dict[str, Any]:
        selected = self.unrank(rank)
        source_pairing = self.wick_join.materialize(rank)
        selected_by_vertex = {
            vertex_id: option
            for vertex_id, option in zip(self.vertex_order, selected, strict=True)
        }
        vertices_by_id = {vertex["vertex_id"]: vertex for vertex in self.graph["vertices"]}
        theta_vertices = []
        for vertex_id in self.vertex_order:
            option = selected_by_vertex[vertex_id]
            term = self.term_dictionary[option["source_term_id"]]
            theta_vertices.append(
                {
                    "vertex_id": vertex_id,
                    "theta_label": f"theta_{vertex_id}",
                    "topology_role": vertices_by_id[vertex_id]["role"],
                    "source_term_id": term["term_id"],
                    "measure": term["measure"],
                    "chirality": term["chirality"],
                    "expression_ast_ref": term["term_id"],
                    "expression_ast_sha256": term["expression_ast_sha256"],
                    "color_ast_ref": term["term_id"],
                    "color_ast_sha256": term["color_ast_sha256"],
                }
            )

        background_source_order: list[dict[str, Any]] = []
        for vertex_id in self.vertex_order:
            ref = selected_by_vertex[vertex_id]["background_projection"]
            candidate_id = ref["projection_candidate_id"]
            if candidate_id is not None:
                background_source_order.extend(
                    deepcopy(
                        self.projection_dictionary[candidate_id][
                            "background_port_projections"
                        ]
                    )
                )
        topology_port_order = [
            port["port_id"]
            for vertex in self.graph["vertices"]
            for port in vertex["background_ports"]
        ]
        by_topology_port = {
            row["topology_port_id"]: row for row in background_source_order
        }
        if len(by_topology_port) != 2 or set(by_topology_port) != set(topology_port_order):
            raise ProjectionJoinError("global background projection is not a two-port bijection")
        topology_background_order = [by_topology_port[port] for port in topology_port_order]
        if [row["external_momentum"] for row in topology_background_order] != ["p1", "p2"]:
            raise ProjectionJoinError("topology external order must remain p1,p2")

        edge_rows = []
        for edge in source_pairing["edges"]:
            source = _enrich_endpoint(edge["source"], self.term_dictionary)
            target = _enrich_endpoint(edge["target"], self.term_dictionary)
            enriched = {**edge, "source": source, "target": target}
            propagator = attach_vector_propagator(
                self.graph, self.orientation, enriched, self.kernel_certificate
            )
            edge_rows.append({**enriched, "propagator": propagator})
        denominator_product = {
            "op": "product",
            "factors": [edge["propagator"]["denominator"] for edge in edge_rows],
            "rendered": self.graph["denominator_ast"]["rendered"],
            "all_powers": [1] * len(edge_rows),
        }
        if denominator_product != self.graph["denominator_ast"]:
            raise PropagatorContractError("five attached denominators changed GraphIR routing")

        factorization = exact_coefficient_factorization(self.graph, selected)
        row = {
            "schema_version": SCHEMA_VERSION,
            "amplitude_ir_id": self.amplitude_id(rank),
            "rank": rank,
            "source_pairing_id": source_pairing["pairing_id"],
            "source_pairing_sha256": source_pairing["pairing_sha256"],
            "graph_id": self.graph["graph_id"],
            "graph_hash": self.graph["graph_hash"],
            "orientation": self.orientation,
            "orientation_hash": self.graph["orientations"][self.orientation][
                "orientation_hash"
            ],
            "orientation_role": (
                "PHYSICAL_SUM_REPRESENTATIVE"
                if self.orientation == "direct"
                else "ROUTING_COVARIANCE_CHECK_ONLY_NOT_ADDED_TO_PHYSICAL_SUM"
            ),
            "classification": "EXACT_PRE_DALGEBRA_LABELED_AMPLITUDE_IR",
            "selected_local_amplitude_option_ids": [
                option["local_amplitude_option_id"] for option in selected
            ],
            "selected_source_term_ids": {
                vertex_id: selected_by_vertex[vertex_id]["source_term_id"]
                for vertex_id in self.vertex_order
            },
            "theta_vertices": theta_vertices,
            "external_background_projection": {
                "source_assignment_order": background_source_order,
                "topology_background_port_order": topology_background_order,
                "topology_external_momentum_order": ["p1", "p2"],
                "bijection": True,
                "projector_coefficients_applied_separately": False,
            },
            "edges": edge_rows,
            "denominator_product": denominator_product,
            "coefficient_factorization": factorization,
            "integral_family_interface": self.integral_interface,
            "pre_dalgebra_integrand_ast": {
                "op": "product",
                "factors": [
                    {"op": "coefficient_factorization_ref", "value": factorization},
                    {
                        "op": "vertex_source_AST_product",
                        "ordered_term_refs": [
                            selected_by_vertex[vertex_id]["source_term_id"]
                            for vertex_id in self.vertex_order
                        ],
                    },
                    {
                        "op": "five_Project_vector_propagators",
                        "ordered_edge_refs": [edge["edge_id"] for edge in edge_rows],
                    },
                ],
            },
            "downstream_fail_closed": downstream_fail_closed(),
        }
        row["amplitude_ir_sha256"] = digest(row)
        return row


def downstream_fail_closed() -> dict[str, dict[str, Any]]:
    return {
        "compiled_d_algebra": {"status": DALGEBRA_STATUS, "value": None},
        "scalar_numerator": {"status": NUMERATOR_STATUS, "value": None},
        "labeled_pairing_sum": {"status": AMPLITUDE_SUM_STATUS, "value": None},
        "integral_reduction": {"status": INTEGRAL_STATUS, "value": None},
        "uv_pole": {"status": INTEGRAL_STATUS, "value": None},
        "renormalized_coefficient": {"status": COEFFICIENT_STATUS, "value": None},
    }


def make_amplitude_parent(
    join: wick.ParentJoin,
    wick_join_row: Mapping[str, Any],
    projection_by_key: Mapping[str, Mapping[str, Any]],
    projection_dictionary: Mapping[str, Mapping[str, Any]],
    kernel_certificate: Mapping[str, Any],
    integral_interface: Mapping[str, Any] | None,
) -> AmplitudeParent:
    vertex_by_id = {vertex["vertex_id"]: vertex for vertex in join.graph["vertices"]}
    local_options: dict[str, list[dict[str, Any]]] = {}
    for vertex_id in join.vertex_order:
        assignments = {
            row["assignment_id"]: row for row in join.assignment_catalog[vertex_id]
        }
        rows = []
        for option in join.local_options[vertex_id]:
            rows.append(
                join_local_option(
                    join,
                    vertex_by_id[vertex_id],
                    option,
                    assignments[option["assignment_id"]],
                    projection_by_key,
                )
            )
        local_options[vertex_id] = rows
    parent = AmplitudeParent(
        wick_join=join,
        wick_join_row=dict(wick_join_row),
        local_options=local_options,
        projection_dictionary={key: dict(value) for key, value in projection_dictionary.items()},
        term_dictionary=join.term_dictionary,
        kernel_certificate=dict(kernel_certificate),
        integral_interface=dict(integral_interface) if integral_interface is not None else None,
    )
    if parent.radices != join.radices or parent.cardinality != join.cardinality:
        raise AmplitudeIRError("projection join changed the Wick mixed-radix enumeration")
    return parent


def parent_as_json(parent: AmplitudeParent) -> dict[str, Any]:
    samples = {
        "first": parent.materialize(0),
        "middle": parent.materialize(parent.cardinality // 2),
        "last": parent.materialize(parent.cardinality - 1),
    }
    histogram = coefficient_signature_histogram(parent)
    row = {
        "graph_id": parent.graph["graph_id"],
        "graph_hash": parent.graph["graph_hash"],
        "orientation": parent.orientation,
        "orientation_hash": parent.graph["orientations"][parent.orientation][
            "orientation_hash"
        ],
        "orientation_role": (
            "PHYSICAL_SUM_REPRESENTATIVE"
            if parent.orientation == "direct"
            else "ROUTING_COVARIANCE_CHECK_ONLY_NOT_ADDED_TO_PHYSICAL_SUM"
        ),
        "classification": "EXACT_FACTORIZED_PRE_DALGEBRA_AMPLITUDE_ENUMERATION",
        "vertex_order": list(parent.vertex_order),
        "local_amplitude_option_catalog": parent.local_options,
        "local_option_counts": {
            vertex: len(parent.local_options[vertex]) for vertex in parent.vertex_order
        },
        "global_amplitude_enumeration": {
            **parent.wick_join_row["global_pairing_enumeration"],
            "amplitude_id_rule": "graph_id::orientation::A<rank>",
            "cardinality_unchanged_by_projection_and_propagator_join": True,
        },
        "coefficient_signature_histogram": histogram,
        "coefficient_histogram_pairing_count": sum(
            item["labeled_pairing_count"] for item in histogram
        ),
        "denominator_product": parent.graph["denominator_ast"],
        "integral_family_interface": parent.integral_interface,
        "samples_only_not_full_materialization": samples,
        "downstream_fail_closed": downstream_fail_closed(),
    }
    row["parent_amplitude_sha256"] = digest(row)
    return row


def build_runtime() -> tuple[dict[str, Any], list[AmplitudeParent], dict[str, Any]]:
    wick_payload, wick_joins = wick.build_payload()
    projection_payload, projection_runtime = projection.build_payload()
    projection_by_key, projection_dictionary = build_projection_index(projection_runtime)
    kernel_certificate = step5a_kernel_certificate()
    integral_interfaces = optional_integral_interface()
    wick_rows = {
        (row["graph_id"], row["orientation"]): row for row in wick_payload["joins"]
    }
    parents = [
        make_amplitude_parent(
            join,
            wick_rows[(join.graph["graph_id"], join.orientation)],
            projection_by_key,
            projection_dictionary,
            kernel_certificate,
            integral_interfaces.get(join.graph["graph_id"]),
        )
        for join in wick_joins
    ]
    provenance = {
        "wick_payload_sha256": wick_payload["payload_sha256"],
        "projection_payload_sha256": projection_payload["payload_sha256"],
        "wick_generator": "scripts/step6_two_loop_wick.py",
        "wick_generator_sha256": file_sha256(ROOT / "scripts/step6_two_loop_wick.py"),
        "projection_generator": "scripts/step6_external_projection.py",
        "projection_generator_sha256": file_sha256(
            ROOT / "scripts/step6_external_projection.py"
        ),
        "step5a_kernel_generator": "scripts/verify_step5a_fixed_kernel.py",
        "step5a_kernel_generator_sha256": file_sha256(
            ROOT / "scripts/verify_step5a_fixed_kernel.py"
        ),
        "authority_role": "UNMERGED_PROPOSAL_INPUTS_NOT_COMPUTATIONAL_EVIDENCE",
    }
    dictionaries = {
        "term_dictionary": wick_payload["term_dictionary"],
        "projection_candidate_dictionary": dict(sorted(projection_dictionary.items())),
        "kernel_certificate": kernel_certificate,
    }
    return provenance, parents, dictionaries


def build_payload() -> tuple[dict[str, Any], list[AmplitudeParent]]:
    provenance, parents, dictionaries = build_runtime()
    parent_rows = [parent_as_json(parent) for parent in parents]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "scope": "THREE_DECORATED_LITERAL_K4_MINUS_EDGE_PARENTS_BOTH_ORIENTATIONS",
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "input_provenance": provenance,
        "Project_step5a_kernel": dictionaries["kernel_certificate"],
        "term_dictionary": dictionaries["term_dictionary"],
        "projection_candidate_dictionary": dictionaries[
            "projection_candidate_dictionary"
        ],
        "parents": parent_rows,
        "parent_count": len(parent_rows),
        "exact_total_labeled_amplitudes": sum(
            row["global_amplitude_enumeration"]["cardinality"] for row in parent_rows
        ),
        "exact_total_physical_representative_amplitudes_before_automorphism_weight": sum(
            row["global_amplitude_enumeration"]["cardinality"]
            for row in parent_rows
            if row["orientation_role"] == "PHYSICAL_SUM_REPRESENTATIVE"
        ),
        "orientation_sum_policy": (
            "SUM_DIRECT_ONLY_REFLECTED_ROWS_CERTIFY_ROUTING_COVARIANCE"
        ),
        "global_coefficient_policy": {
            "raw_insertion_coefficient_count": 1,
            "raw_action_coefficient_count": 3,
            "vector_propagator_coefficient_count": 5,
            "Wick_hbar_factor_count": 5,
            "action_occurrence_orbit_hbar_power": -3,
            "net_hbar_power": 2,
            "external_projector_coefficient_count": 0,
            "bosonic_wick_sign": 1,
            "h_rewrite": "h=(g^2)^(-1)",
            "coupling_grade": "g^4",
            "pairing_sum": None,
        },
        "global_downstream_fail_closed": downstream_fail_closed(),
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    )
    return payload, parents


def exact_checks(
    payload: Mapping[str, Any], parents: Sequence[AmplitudeParent]
) -> dict[str, bool]:
    rows = payload["parents"]
    samples = [
        sample
        for row in rows
        for sample in row["samples_only_not_full_materialization"].values()
    ]
    projection_ids = set(payload["projection_candidate_dictionary"])
    referenced_projection_ids = {
        option["background_projection"]["projection_candidate_id"]
        for parent in parents
        for options in parent.local_options.values()
        for option in options
        if option["background_projection"]["projection_candidate_id"] is not None
    }
    return {
        "status_is_proposal_only": payload["status"] == STATUS
        and payload["stage"] == STAGE,
        "six_oriented_parents_preserved": len(parents) == len(rows) == 6
        and {
            (parent.graph["graph_id"], parent.orientation) for parent in parents
        }
        == {
            (graph_id, orientation)
            for graph_id in projection.SUPPORTED_GRAPH_IDS
            for orientation in ("direct", "reflected")
        },
        "exact_total_pairing_cardinality_preserved": payload[
            "exact_total_labeled_amplitudes"
        ]
        == 2_985_984
        and payload[
            "exact_total_physical_representative_amplitudes_before_automorphism_weight"
        ]
        == 1_492_992
        and all(parent.cardinality == parent.wick_join.cardinality for parent in parents),
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
        "rank_unrank_stable": all(
            parent.rank(parent.unrank(rank)) == rank
            for parent in parents
            for rank in (0, parent.cardinality // 2, parent.cardinality - 1)
        ),
        "every_background_wick_assignment_has_one_projection": all(
            option["background_projection"]["status"]
            in ("EXACT_BIJECTIVE_PROJECT_BACKGROUND_JOIN", "NOT_APPLICABLE_EXACT_B0_VERTEX")
            for parent in parents
            for options in parent.local_options.values()
            for option in options
        ),
        "all_projection_candidates_are_referenced": referenced_projection_ids
        == projection_ids,
        "external_p1_p2_topology_order_preserved": all(
            sample["external_background_projection"][
                "topology_external_momentum_order"
            ]
            == ["p1", "p2"]
            and [
                port["external_momentum"]
                for port in sample["external_background_projection"][
                    "topology_background_port_order"
                ]
            ]
            == ["p1", "p2"]
            for sample in samples
        ),
        "five_Project_vector_propagators_per_sample": all(
            len(sample["edges"]) == 5
            and all(
                edge["propagator"]["source_scope"]
                == "STEP5A_PERTURBATIVE_FERMI_FEYNMAN"
                and edge["propagator"]["coefficient"]["rendered"] == "-2*g^2"
                and edge["propagator"]["Wick_hbar_factor"]["power"] == 1
                and edge["propagator"]["Wick_contraction"] == "hbar*G_V"
                and edge["propagator"]["grassmann_operator"] == "identity_16"
                and edge["propagator"]["grassmann_delta_ast"]["degree"] == 4
                for edge in sample["edges"]
            )
            for sample in samples
        ),
        "denominator_products_equal_GraphIR": all(
            sample["denominator_product"] == parent.graph["denominator_ast"]
            for parent, row in zip(parents, rows, strict=True)
            for sample in row["samples_only_not_full_materialization"].values()
        ),
        "endpoint_derivative_words_and_source_refs_preserved": all(
            endpoint["grammar_port_record"]["derivative_word_outer_to_inner"]
            == endpoint["grammar_derivative_word_outer_to_inner"]
            and endpoint["source_color_ast_ref"] in payload["term_dictionary"]
            and endpoint["source_expression_ast_ref"] in payload["term_dictionary"]
            for sample in samples
            for edge in sample["edges"]
            for endpoint in (edge["source"], edge["target"])
        ),
        "theta_vertices_and_measures_preserved": all(
            len(sample["theta_vertices"]) == 4
            and all(
                vertex["measure"]
                == payload["term_dictionary"][vertex["source_term_id"]]["measure"]
                for vertex in sample["theta_vertices"]
            )
            for sample in samples
        ),
        "coefficient_factor_counts_are_1_3_5": all(
            len(sample["coefficient_factorization"]["ordered_action_raw_Qi"]) == 3
            and len(
                sample["coefficient_factorization"]["ordered_vector_Wick_factors"]
            )
            == 5
            and all(
                factor["Wick_hbar_factor"]["power"] == 1
                for factor in sample["coefficient_factorization"][
                    "ordered_vector_Wick_factors"
                ]
            )
            and sample["coefficient_factorization"]["bosonic_wick_sign"]["value"]
            == 1
            for sample in samples
        ),
        "decorated_occurrence_orbit_weights_are_graphwise_exact": all(
            Fraction(
                sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
                ["combined_rational"]["numerator"],
                sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
                ["combined_rational"]["denominator"],
            )
            == Fraction(
                -1,
                sample["coefficient_factorization"]["decorated_occurrence_orbit_factor"]
                ["background_source_labeled_automorphism_order"],
            )
            for sample in samples
        ),
        "external_projector_coefficient_never_multiplied": all(
            sample["coefficient_factorization"][
                "external_projector_coefficient_factor"
            ]
            is None
            and not sample["external_background_projection"][
                "projector_coefficients_applied_separately"
            ]
            for sample in samples
        ),
        "h_rewrite_gives_exact_g4": all(
            sample["coefficient_factorization"][
                "h_equals_inverse_g_squared_rewrite_certificate"
            ]["derived_g_power"]
            == 4
            and sample["coefficient_factorization"]["exact_product_after_h_rewrite"][
                "coupling_grade"
            ]
            == "g^4"
            and sample["coefficient_factorization"]["exact_product_after_h_rewrite"][
                "hbar_power"
            ]
            == 2
            and sample["coefficient_factorization"]["exact_product_after_h_rewrite"][
                "loop_grade"
            ]
            == "hbar^2"
            for sample in samples
        ),
        "coefficient_histograms_are_exact": all(
            row["coefficient_histogram_pairing_count"]
            == row["global_amplitude_enumeration"]["cardinality"]
            for row in rows
        ),
        "optional_integral_interface_does_not_supply_numerator": all(
            row["integral_family_interface"] is None
            or (
                row["integral_family_interface"]["status"]
                == "OPTIONAL_INTERFACE_LINKED_NOT_A_DEPENDENCY"
                and row["integral_family_interface"]["physical_numerator"] is None
                and row["integral_family_interface"]["edge_order"]
                == [factor["edge_id"] for factor in row["denominator_product"]["factors"]]
            )
            for row in rows
        ),
        "kernel_is_two_sided_identity_16": payload["Project_step5a_kernel"][
            "two_sided_inverse_checks"
        ]
        == {"left": True, "right": True}
        and payload["Project_step5a_kernel"]["grassmann_representation"]
        == "identity_16",
        "no_global_pairing_rows_materialized": all(
            "amplitude_rows" not in row
            and set(row["samples_only_not_full_materialization"])
            == {"first", "middle", "last"}
            for row in rows
        ),
        "all_later_stages_fail_closed": all(
            stage["value"] is None and stage["status"].startswith("BLOCKED_")
            for row in rows
            for stage in row["downstream_fail_closed"].values()
        )
        and all(
            stage["value"] is None and stage["status"].startswith("BLOCKED_")
            for stage in payload["global_downstream_fail_closed"].values()
        ),
        "source_hashes_present": all(
            len(value) == 64
            for key, value in payload["input_provenance"].items()
            if key.endswith("sha256")
        ),
    }


def build_audit(
    payload: Mapping[str, Any],
    parents: Sequence[AmplitudeParent],
    artifact_hashes: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    checks = exact_checks(payload, parents)
    failures = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "step6.two_loop_amplitude_ir.audit.v1",
        "status": "PASS" if not failures else "FAIL",
        "proposal_status": STATUS,
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "parent_count": payload["parent_count"],
        "exact_total_labeled_amplitudes": payload["exact_total_labeled_amplitudes"],
        "payload_sha256": payload["payload_sha256"],
        "artifact_sha256": dict(artifact_hashes or {}),
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    lines = [
        "# Step 6 pre-$D$-algebra AmplitudeIR",
        "",
        "$$",
        "G_V^{CD}(r)=-2g^2\\kappa^{CD}\\,\\Delta^4(\\theta_s-\\theta_t)\\,\\mathbf 1_{16}\\,\\frac{1}{r^2}.",
        "$$",
        "",
        "$$",
        "\\langle V^C V^D\\rangle_0=\\hbar G_V^{CD}.",
        "$$",
        "",
        "$$",
        "\\mathcal C_{\\rho}=c_I\\left(\\prod_{v=1}^{3}c_{S_v}\\right)"
        "\\left[\\frac{(-1)^3}{\\hbar^3\\prod_{\\tau}n_{\\tau}!}"
        "\\frac{\\prod_{\\tau}n_{\\tau}!}{|\\operatorname{Aut}_{B}(G)|}\\right]"
        "\\left(\\prod_{e=1}^{5}\\hbar(-2g^2)\\right)(+1).",
        "$$",
        "",
        "$$",
        "\\frac{(-1)^3}{\\prod_{\\tau}n_{\\tau}!}"
        "\\frac{\\prod_{\\tau}n_{\\tau}!}{|\\operatorname{Aut}_{B}(G)|}"
        "=-\\frac{1}{|\\operatorname{Aut}_{B}(G)|}.",
        "$$",
        "",
        "$$",
        "\\hbar^{-3}\\hbar^5=\\hbar^2,\\qquad "
        "(g^2)^5h^3=(g^2)^5(g^2)^{-3}=(g^2)^2=g^4,\\qquad h=(g^2)^{-1}.",
        "$$",
        "",
        "| GraphIR | orientation | denominator | labeled amplitudes |",
        "|---|---:|---:|---:|",
    ]
    for row in payload["parents"]:
        lines.append(
            f"| `{row['graph_id']}` | `{row['orientation']}` | "
            f"`${row['denominator_product']['rendered']}$` | "
            f"`{row['global_amplitude_enumeration']['cardinality']}` |"
        )
    lines.extend(
        [
            "",
            f"- exact labeled cardinality: `{payload['exact_total_labeled_amplitudes']}`.",
            "- physical sum uses `direct` only; `reflected` is a routing-covariance check.",
            f"- projection candidates: `{len(payload['projection_candidate_dictionary'])}`.",
            f"- verification: `{audit['passed']}/{audit['passed'] + audit['failed']}`.",
            f"- $D$-algebra, numerator, pairing sum, integral, pole, coefficient: `{DALGEBRA_STATUS}`.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    payload, parents = build_payload()
    provisional_audit = build_audit(payload, parents)
    GENERATED_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    GENERATED_MD.write_text(render_markdown(payload, provisional_audit), encoding="utf-8")
    artifact_hashes = {
        GENERATED_JSON.relative_to(ROOT).as_posix(): file_sha256(GENERATED_JSON),
        GENERATED_MD.relative_to(ROOT).as_posix(): file_sha256(GENERATED_MD),
    }
    audit = build_audit(payload, parents, artifact_hashes)
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "passed": audit["passed"],
                "failed": audit["failed"],
                "parent_count": payload["parent_count"],
                "exact_total_labeled_amplitudes": payload[
                    "exact_total_labeled_amplitudes"
                ],
            },
            sort_keys=True,
        )
    )
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
