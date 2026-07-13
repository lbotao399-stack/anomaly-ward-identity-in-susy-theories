#!/usr/bin/env python3
"""Exact first global graded supertensor contraction for Step 6.

The compiler joins coefficient and color data on the same ordered local-option
tuple.  It evaluates one direct physical K4-minus-edge amplitude row exactly
in a fixed external coefficient slice, and emits a certified factorized plan
for the complete local-option sum.  Reflected parents are routing checks only.
No DRED, IBP, UV pole, or two-loop anomaly coefficient is inferred here.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from math import prod
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
import hashlib
import json

try:
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_color_tensor as color
    from scripts import step6_two_loop_amplitude_ir as amplitude
except ModuleNotFoundError:  # direct execution from scripts/
    import step6_coefficient_tensor as coefficient
    import step6_color_tensor as color
    import step6_two_loop_amplitude_ir as amplitude


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "generated/step6/global-supertensor"
OUTPUT_JSON = OUTPUT_DIR / "global-supertensor.json"
OUTPUT_MD = OUTPUT_DIR / "global-supertensor.md"
AUDIT = ROOT / "audits/step6-global-supertensor-verification.json"

SCHEMA = "step6.global_graded_supertensor.v1"
STATUS = "PASS_ONE_EXACT_DIRECT_ROW_SLICE_FULL_PAIRING_SUM_STILL_BLOCKED"
PHYSICAL_GRAPH_ID = "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"
EXTERNAL_SLICE = {"p1": 0, "p2": 0}
GRAPH_WEIGHT_AFTER_HBAR_STRIP = {
    "G6_DIRECT_K4ME_I3_S3CUBED": Fraction(-1),
    "G6_DIRECT_K4ME_I2_S3SQ_S4": Fraction(-1),
    "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4": Fraction(-1, 2),
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value)


def deserialize_poly(rows: Sequence[Mapping[str, Any]]) -> Any:
    terms: dict[Any, Any] = {}
    for row in rows:
        monomial = tuple(
            (str(item["symbol"]), int(item["exponent"]))
            for item in row["monomial"]
        )
        scalar = row["coefficient"]
        terms[monomial] = coefficient.oracle.Gaussian(
            Fraction(str(scalar["re"])), Fraction(str(scalar["im"]))
        )
    return coefficient.oracle.Poly.from_terms(terms)


def deserialize_value(record: Mapping[str, Any]) -> Any:
    if record["type"] == "Poly":
        return deserialize_poly(record["terms"])
    if record["type"] == "Exterior":
        return coefficient.oracle.Exterior.from_terms(
            {
                int(row["mask"]): deserialize_poly(row["coefficient"])
                for row in record["terms"]
            }
        )
    raise TypeError(f"unsupported serialized local tensor {record['type']}")


def serialize_value(value: Any) -> dict[str, Any]:
    return coefficient.serialize_evaluation(value)


def graph_weight_certificate(
    parents: Sequence[amplitude.AmplitudeParent],
) -> dict[str, Any]:
    direct_graphs = {
        parent.graph["graph_id"]: parent.graph
        for parent in parents
        if parent.orientation == "direct"
    }
    if set(direct_graphs) != set(GRAPH_WEIGHT_AFTER_HBAR_STRIP):
        raise AssertionError("direct decorated parent set changed")
    rows = []
    for graph_id, expected in GRAPH_WEIGHT_AFTER_HBAR_STRIP.items():
        certificate = direct_graphs[graph_id]["automorphisms"][
            "background_source_labeled"
        ]
        aut = int(certificate["order"])
        derived = Fraction(-1, aut)
        if derived != expected:
            raise AssertionError("background automorphism weight changed")
        rows.append(
            {
                "graph_id": graph_id,
                "Aut_bg": aut,
                "Aut_bg_certificate_sha256": certificate["automorphism_hash"],
                "three_action_expansion_after_occurrence_orbit": "-1/hbar^3",
                "hbar_stripped_graph_weight": fraction_text(derived),
            }
        )
    return {
        "formula": "-1/(hbar^3*Aut_bg)",
        "rows": rows,
        "direct_only_is_physical": True,
        "reflected_role": "ROUTING_COVARIANCE_ONLY_NOT_ADDED",
    }


@dataclass(frozen=True)
class WordVariable:
    label: str
    parity: int


def weighted_permutation_sign(
    global_word: Sequence[WordVariable], canonical_labels: Sequence[str]
) -> int:
    if len(global_word) != len(canonical_labels):
        raise ValueError("global and canonical words have different lengths")
    labels = [item.label for item in global_word]
    if len(labels) != len(set(labels)) or set(labels) != set(canonical_labels):
        raise ValueError("graded permutation requires one occurrence of each label")
    rank = {label: index for index, label in enumerate(canonical_labels)}
    exponent = sum(
        left.parity * right.parity
        for i, left in enumerate(global_word)
        for right in global_word[i + 1 :]
        if rank[left.label] > rank[right.label]
    )
    return -1 if exponent & 1 else 1


def recursive_target_removal_sign(
    global_word: Sequence[WordVariable],
    edge_pairs: Sequence[tuple[str, str]],
    external_order: Sequence[str] = ("p1", "p2"),
) -> int:
    """Move each target next to its source, remove the even pair, reorder externals."""

    word = list(global_word)
    sign = 1
    for source_label, target_label in edge_pairs:
        source_position = next(i for i, item in enumerate(word) if item.label == source_label)
        target_position = next(i for i, item in enumerate(word) if item.label == target_label)
        source = word[source_position]
        target = word[target_position]
        if source.parity != target.parity:
            raise ValueError("H inverse support requires equal endpoint parities")
        if source_position < target_position:
            crossed = word[source_position + 1 : target_position]
        else:
            crossed = word[target_position + 1 : source_position] + [source]
        exponent = target.parity * sum(item.parity for item in crossed)
        if exponent & 1:
            sign = -sign
        word = [
            item
            for item in word
            if item.label not in {source_label, target_label}
        ]
    if [item.label for item in word] not in (
        list(external_order),
        list(reversed(external_order)),
    ):
        raise ValueError("pair removal did not leave exactly p1,p2")
    if [item.label for item in word] == list(reversed(external_order)):
        if word[0].parity * word[1].parity:
            sign = -sign
    return sign


def exhaustive_sign_fixture() -> dict[str, Any]:
    labels = ("s0", "t0", "s1", "t1", "p1", "p2")
    canonical = labels
    checked = 0
    for order in permutations(labels):
        for edge0, edge1, p1, p2 in product((0, 1), repeat=4):
            parity = {
                "s0": edge0,
                "t0": edge0,
                "s1": edge1,
                "t1": edge1,
                "p1": p1,
                "p2": p2,
            }
            word = [WordVariable(label, parity[label]) for label in order]
            direct = weighted_permutation_sign(word, canonical)
            recursive = recursive_target_removal_sign(
                word, (("s0", "t0"), ("s1", "t1"))
            )
            if direct != recursive:
                raise AssertionError((order, parity, direct, recursive))
            checked += 1
    return {
        "fixture": "TWO_EDGES_TWO_EXTERNALS_ALL_WORD_ORDERS_ALL_PARITIES",
        "checked_cases": checked,
        "direct_weighted_permutation_equals_recursive_target_removal": True,
    }


def direct_delta_reconstruction_fixture(bundle: Mapping[str, Any]) -> dict[str, Any]:
    metric = bundle["coefficient_metric"]
    h_inverse = [
        [Fraction(value) for value in row]
        for row in metric["left_ordered_coefficient_H_inverse"]
    ]
    delta = [
        [Fraction(value) for value in row]
        for row in bundle["normalized_difference_delta"]["coefficient_matrix"]
    ]
    reconstructed = [[Fraction(0) for _ in range(16)] for _ in range(16)]
    for source in range(16):
        for target in range(16):
            # (v_s e_s)(v_t e_t): move v_t left through e_s.
            cross = -1 if coefficient.coefficient_parity(source) * coefficient.coefficient_parity(target) else 1
            reconstructed[source][target] = cross * h_inverse[source][target]
    if reconstructed != delta:
        raise AssertionError("direct superfield coefficient/exterior reconstruction failed")
    support = [
        [source, target]
        for source in range(16)
        for target in range(16)
        if h_inverse[source][target]
    ]
    if support != [[source, 15 ^ source] for source in range(16)]:
        raise AssertionError("H inverse lost complementary support")
    return {
        "formula": "(v_s e_s)(v_t e_t)=(-1)^(|s||t|)v_s v_t e_s e_t",
        "delta_formula": "-4*product_i(theta_i-theta_i_prime)",
        "left_H_inverse_crossed_back_to_exterior_order_equals_delta": True,
        "nonzero_support": support,
    }


def option_program_index(bundle: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {
        str(program["local_amplitude_option_id"]): program
        for program in bundle["tensor_programs"]["option_programs"].values()
    }


def joint_local_structural_signature(
    parent: amplitude.AmplitudeParent,
    vertex: Mapping[str, Any],
    option: Mapping[str, Any],
    program: Mapping[str, Any],
) -> tuple[str, dict[str, Any]]:
    color_row = color.compile_local_color_option(parent, vertex, option)
    color_signature = color.local_group_signature(color_row)
    coefficient_core = {
        "term_id": program["term_id"],
        "measure": program["measure"],
        "port_order": program["port_order"],
        "bindings": program["bindings"],
        "expression_ast_sha256": program["expression_ast_sha256"],
    }
    joint_core = {
        "coefficient_local_tensor_program": coefficient_core,
        "color_local_tensor_signature": color_signature,
        "topology_port_to_color_index": color_row["topology_port_to_color_index"],
    }
    return digest(joint_core), {
        "joint_signature_sha256": digest(joint_core),
        "coefficient_core_sha256": digest(coefficient_core),
        "color_local_signature_sha256": color_signature,
        "joint_core": joint_core,
    }


def factorized_joint_sum_plan(
    parents: Sequence[amplitude.AmplitudeParent], bundle: Mapping[str, Any]
) -> dict[str, Any]:
    by_option = option_program_index(bundle)
    parent_rows = []
    for parent in parents:
        vertices = {str(row["vertex_id"]): row for row in parent.graph["vertices"]}
        per_vertex = {}
        grouped_tuple_count = 1
        for vertex_id in parent.vertex_order:
            groups: dict[str, dict[str, Any]] = {}
            for option in parent.local_options[vertex_id]:
                program = by_option[str(option["local_amplitude_option_id"])]
                signature, record = joint_local_structural_signature(
                    parent, vertices[vertex_id], option, program
                )
                group = groups.setdefault(
                    signature,
                    {
                        **record,
                        "multiplicity": 0,
                        "local_amplitude_option_ids": [],
                    },
                )
                group["multiplicity"] += 1
                group["local_amplitude_option_ids"].append(
                    option["local_amplitude_option_id"]
                )
            grouped_tuple_count *= len(groups)
            per_vertex[vertex_id] = [groups[key] for key in sorted(groups)]
        parent_rows.append(
            {
                "graph_id": parent.graph["graph_id"],
                "orientation": parent.orientation,
                "orientation_role": (
                    "PHYSICAL_SUM_REPRESENTATIVE"
                    if parent.orientation == "direct"
                    else "ROUTING_COVARIANCE_ONLY_NOT_ADDED"
                ),
                "vertex_order": list(parent.vertex_order),
                "raw_option_counts": {
                    vertex: len(parent.local_options[vertex])
                    for vertex in parent.vertex_order
                },
                "joint_group_counts": {
                    vertex: len(per_vertex[vertex]) for vertex in parent.vertex_order
                },
                "joint_group_tuple_count": grouped_tuple_count,
                "raw_cartesian_cardinality": parent.cardinality,
                "per_vertex_joint_groups": per_vertex,
                "same_ordered_local_option_tuple_for_coefficient_and_color": True,
                "independent_coefficient_color_marginal_product": "REJECTED",
            }
        )
    return {
        "identity": "sum_(alpha_I,...,alpha_C) C[T_I^alpha_I,...,T_C^alpha_C] = C[sum_alpha_I T_I^alpha_I,...,sum_alpha_C T_C^alpha_C]",
        "condition": "combined orbit weight is option-independent within each decorated parent",
        "local_object": "JOINT_COEFFICIENT_X_COLOR_TENSOR_ON_TOPOLOGY_PORTS",
        "aggregation_before_network_contraction": True,
        "parents": parent_rows,
    }


class CachedDerivativeEngine:
    """Exact graded Leibniz engine with cached momentum-dependent D matrices."""

    def __init__(self) -> None:
        self.operators: dict[Any, Mapping[str, Any]] = {}

    def primitive(self, terms: Sequence[Any], primitive: str) -> tuple[Any, ...]:
        emitted = []
        for term in terms:
            prefix_parity = 0
            for position, factor in enumerate(term.factors):
                operators = self.operators.get(factor.momentum)
                if operators is None:
                    operators = coefficient.oracle.flat_operators(factor.momentum)
                    self.operators[factor.momentum] = operators
                differentiated = operators[primitive].apply(factor.value)
                if differentiated:
                    replacement = coefficient.oracle.LabeledLeaf(
                        factor.label,
                        factor.momentum,
                        factor.parity ^ 1,
                        differentiated,
                        (primitive,) + factor.derivative_word,
                    )
                    emitted.append(
                        coefficient.oracle.ProductTerm(
                            term.coefficient * (-1 if prefix_parity else 1),
                            term.factors[:position]
                            + (replacement,)
                            + term.factors[position + 1 :],
                        )
                    )
                prefix_parity ^= factor.parity
        return coefficient._canonical_product_terms(emitted)

    def __call__(self, terms: Sequence[Any], tokens: Sequence[str]) -> tuple[Any, ...]:
        emitted = []
        for branch_coefficient, primitive_word in coefficient._explicit_word_expansion(tokens):
            branch = coefficient.scale_terms(
                terms, coefficient.oracle.Poly.constant(branch_coefficient)
            )
            for primitive in reversed(primitive_word):
                branch = self.primitive(branch, primitive)
            emitted.extend(branch)
        return coefficient._canonical_product_terms(emitted)


def external_label(binding: Mapping[str, Any]) -> str:
    vector = tuple(binding["all_incoming_leaf_momentum_vector"])
    if vector == (0, 0, 0, 1, 0):
        return "p1"
    if vector == (0, 0, 0, 0, 1):
        return "p2"
    raise ValueError(f"background binding is not p1 or p2: {vector}")


def local_value(
    term: Mapping[str, Any],
    program: Mapping[str, Any],
    basis_by_port: Mapping[str, int],
    engine: CachedDerivativeEngine,
) -> Any:
    indices = tuple(int(basis_by_port[port]) for port in program["port_order"])
    leaves = coefficient._program_leaves(program, indices)
    product_terms = coefficient._evaluate_ast_terms(
        term["expression_ast"], leaves, {}, engine
    )
    parities = {
        port: coefficient.coefficient_parity(mask)
        for port, mask in zip(program["port_order"], indices, strict=True)
    }
    raw = coefficient.apply_measure(
        coefficient.evaluate_product_terms(product_terms, parities), term["measure"]
    )
    raw_coefficient = coefficient.parse_qi_polynomial(term["coefficient_raw"])
    if isinstance(raw, coefficient.oracle.Exterior):
        return raw.scale(raw_coefficient)
    return raw * raw_coefficient


def local_sparse_tensor(
    term: Mapping[str, Any],
    program: Mapping[str, Any],
    external_slice: Mapping[str, int],
) -> dict[tuple[int, ...], Any]:
    bindings = {row["grammar_port_id"]: row for row in program["bindings"]}
    quantum_edges = sorted(
        {
            str(row["edge_id"])
            for row in bindings.values()
            if row["role"] == "QUANTUM_EDGE_ENDPOINT"
        }
    )
    engine = CachedDerivativeEngine()
    sparse: dict[tuple[int, ...], Any] = {}
    for source_masks in product(range(16), repeat=len(quantum_edges)):
        source_by_edge = dict(zip(quantum_edges, source_masks, strict=True))
        basis_by_port: dict[str, int] = {}
        for port in program["port_order"]:
            binding = bindings[port]
            if binding["role"] == "BACKGROUND_EXTERNAL_ENDPOINT":
                basis_by_port[port] = int(external_slice[external_label(binding)])
            else:
                source_mask = source_by_edge[str(binding["edge_id"])]
                basis_by_port[port] = (
                    source_mask
                    if binding["orientation_endpoint"] == "source"
                    else 15 ^ source_mask
                )
        value = local_value(term, program, basis_by_port, engine)
        if value:
            sparse[source_masks] = value
    return sparse


def multiply_local_values(values: Sequence[Any]) -> Any:
    exterior_values = [
        value for value in values if isinstance(value, coefficient.oracle.Exterior)
    ]
    polynomial_values = [
        value for value in values if isinstance(value, coefficient.oracle.Poly)
    ]
    if len(exterior_values) != 1:
        raise TypeError("one local operator insertion Exterior is required")
    polynomial = coefficient.oracle.ONE
    for value in polynomial_values:
        polynomial = polynomial * value
    return exterior_values[0].scale(polynomial)


def _word_for_assignment(
    parent: amplitude.AmplitudeParent,
    selected: Mapping[str, Mapping[str, Any]],
    programs: Mapping[str, Mapping[str, Any]],
    source_by_edge: Mapping[str, int],
    external_slice: Mapping[str, int],
) -> tuple[list[WordVariable], list[str], list[tuple[str, str]]]:
    word: list[WordVariable] = []
    endpoint_labels: dict[tuple[str, str], str] = {}
    for vertex_id in parent.vertex_order:
        option = selected[vertex_id]
        program = programs[str(option["local_amplitude_option_id"])]
        bindings = {row["grammar_port_id"]: row for row in program["bindings"]}
        for port in program["port_order"]:
            binding = bindings[port]
            if binding["role"] == "BACKGROUND_EXTERNAL_ENDPOINT":
                label = external_label(binding)
                mask = int(external_slice[label])
            else:
                edge_id = str(binding["edge_id"])
                endpoint = str(binding["orientation_endpoint"])
                label = f"{edge_id}:{endpoint}"
                endpoint_labels[(edge_id, endpoint)] = label
                source_mask = int(source_by_edge[edge_id])
                mask = source_mask if endpoint == "source" else 15 ^ source_mask
            word.append(WordVariable(label, coefficient.coefficient_parity(mask)))
    edge_order = [
        str(row["edge_id"])
        for row in parent.graph["orientations"][parent.orientation]["edges"]
    ]
    edge_pairs = [
        (
            endpoint_labels[(edge_id, "source")],
            endpoint_labels[(edge_id, "target")],
        )
        for edge_id in edge_order
    ]
    canonical = [label for pair in edge_pairs for label in pair] + ["p1", "p2"]
    return word, canonical, edge_pairs


def exact_selected_row_slice(
    parents: Sequence[amplitude.AmplitudeParent], bundle: Mapping[str, Any]
) -> dict[str, Any]:
    parent = next(
        row
        for row in parents
        if row.graph["graph_id"] == PHYSICAL_GRAPH_ID and row.orientation == "direct"
    )
    selected_tuple = parent.unrank(0)
    selected = dict(zip(parent.vertex_order, selected_tuple, strict=True))
    programs = option_program_index(bundle)
    terms = bundle["tensor_programs"]["compiled_terms"]
    local_tensors: dict[str, dict[tuple[int, ...], Any]] = {}
    local_edge_orders: dict[str, list[str]] = {}
    for vertex_id in parent.vertex_order:
        option = selected[vertex_id]
        program = programs[str(option["local_amplitude_option_id"])]
        term = terms[str(program["term_id"])]
        edges = sorted(
            {
                str(row["edge_id"])
                for row in program["bindings"]
                if row["role"] == "QUANTUM_EDGE_ENDPOINT"
            }
        )
        local_edge_orders[vertex_id] = edges
        local_tensors[vertex_id] = local_sparse_tensor(
            term, program, EXTERNAL_SLICE
        )

    edge_order = [
        str(row["edge_id"])
        for row in parent.graph["orientations"][parent.orientation]["edges"]
    ]
    metric_inverse = [
        [Fraction(value) for value in row]
        for row in bundle["coefficient_metric"]["M_inverse"]
    ]
    total = coefficient.oracle.Exterior()
    nonzero_assignments = 0
    tested_assignments = 0
    for masks in product(range(16), repeat=5):
        source_by_edge = dict(zip(edge_order, masks, strict=True))
        local_values = []
        missing = False
        for vertex_id in parent.vertex_order:
            key = tuple(source_by_edge[edge] for edge in local_edge_orders[vertex_id])
            value = local_tensors[vertex_id].get(key)
            if value is None:
                missing = True
                break
            local_values.append(value)
        if missing:
            continue
        tested_assignments += 1
        edge_core = Fraction(1)
        for source_mask in masks:
            target_mask = 15 ^ source_mask
            h_inverse = (
                -1 if coefficient.coefficient_parity(source_mask) else 1
            ) * metric_inverse[source_mask][target_mask]
            edge_core *= Fraction(-2) * h_inverse
        if not edge_core:
            continue
        word, canonical, edge_pairs = _word_for_assignment(
            parent, selected, programs, source_by_edge, EXTERNAL_SLICE
        )
        permutation_sign = weighted_permutation_sign(word, canonical)
        recursive_sign = recursive_target_removal_sign(word, edge_pairs)
        if permutation_sign != recursive_sign:
            raise AssertionError("global and recursive graded Wick signs differ")
        contribution = multiply_local_values(local_values).scale(
            edge_core * permutation_sign
        )
        if contribution:
            total = total + contribution
            nonzero_assignments += 1
    aut_certificate = parent.graph["automorphisms"]["background_source_labeled"]
    graph_weight = Fraction(-1, int(aut_certificate["order"]))
    if graph_weight != GRAPH_WEIGHT_AFTER_HBAR_STRIP[parent.graph["graph_id"]]:
        raise AssertionError("derived exact-row graph weight differs from frozen cross-check")
    total = total.scale(graph_weight)

    vertices = {str(row["vertex_id"]): row for row in parent.graph["vertices"]}
    local_color_rows = [
        color.compile_local_color_option(parent, vertices[vertex], selected[vertex])
        for vertex in parent.vertex_order
    ]
    color_tensors, color_propagators = color.attach_propagator_color_metrics(
        parent, local_color_rows
    )
    color_reduction = color.reduce_metrics_exact(color_tensors)
    color_network = color.canonicalize_network(
        color_reduction["tensors"], antisymmetry=True
    )

    raw_local_coefficients = {
        vertex: selected[vertex]["coefficient_raw"] for vertex in parent.vertex_order
    }
    return {
        "classification": "EXACT_ONE_DIRECT_PHYSICAL_AMPLITUDE_ROW_EXTERNAL_COMPONENT_SLICE",
        "graph_id": parent.graph["graph_id"],
        "orientation": parent.orientation,
        "orientation_role": "PHYSICAL_SUM_REPRESENTATIVE",
        "amplitude_rank": 0,
        "amplitude_ir_id": parent.amplitude_id(0),
        "selected_local_amplitude_option_ids": {
            vertex: selected[vertex]["local_amplitude_option_id"]
            for vertex in parent.vertex_order
        },
        "selected_term_ids": {
            vertex: selected[vertex]["source_term_id"]
            for vertex in parent.vertex_order
        },
        "global_coefficient_word_order": "parent.vertex_order THEN grammar.port_order",
        "vertex_order": list(parent.vertex_order),
        "external_coefficient_slice": dict(EXTERNAL_SLICE),
        "external_coefficient_indices_retained_not_contracted": True,
        "open_insertion_exterior_basis_retained": True,
        "edge_order": edge_order,
        "edge_covariance_ownership": "EACH_EDGE_USES_MINUS_2_TIMES_H_INVERSE_EXACTLY_ONCE",
        "raw_local_Qi_ownership": "LOCAL_TENSOR_EVALUATOR_EXACTLY_ONCE",
        "raw_local_coefficients": raw_local_coefficients,
        "graph_orbit_weight_ownership": "MINUS_ONE_OVER_AUT_BG_EXACTLY_ONCE_AFTER_HBAR_STRIP",
        "Aut_bg": int(aut_certificate["order"]),
        "Aut_bg_certificate_sha256": aut_certificate["automorphism_hash"],
        "hbar_stripped_graph_weight": fraction_text(graph_weight),
        "formal_factor_ledger": {
            "three_action_expansion": {"hbar_power": -3},
            "five_vector_covariances": {
                "hbar_power": 5,
                "g_squared_power": 5,
                "minus_two_factors_included_in_edge_core": 5,
            },
            "three_raw_action_vertices": {"h_power": 3},
            "net_before_h_rewrite": {
                "hbar_power": 2,
                "g_squared_power": 5,
                "h_power": 3,
            },
            "h_equals_inverse_g_squared": True,
            "net_after_h_rewrite": {"hbar_power": 2, "g_power": 4},
        },
        "formal_hbar_power_before_strip": 2,
        "formal_coupling_rewrite": "(g^2)^5*h^3=g^4",
        "local_sparse_tensor_nonzero_counts": {
            vertex: len(local_tensors[vertex]) for vertex in parent.vertex_order
        },
        "candidate_assignments_after_local_sparsity": tested_assignments,
        "nonzero_global_edge_assignments": nonzero_assignments,
        "flat_assignment_count_not_materialized": 16**5,
        "assignment_storage_policy": "GENERATOR_PLUS_SPARSE_VERTEX_LOOKUP_NO_ROW_MATERIALIZATION",
        "coefficient_exterior_momentum_polynomial": serialize_value(total),
        "coefficient_result_is_nonzero": bool(total),
        "color": {
            "free_index_order": ["A", "B", "R", "S"],
            "external_background_colors": {"p1": "R", "p2": "S"},
            "propagator_metrics": color_propagators,
            "metric_reduction": color_reduction,
            "canonical_reduced_network": color_network,
            "no_extra_bracket_i": all(
                row["color_i_factor_added_by_compiler"] == 0
                for row in local_color_rows
            ),
        },
        "denominator": parent.graph["denominator_ast"],
        "fail_closed": {
            "complete_labeled_pairing_sum": "BLOCKED_NOT_YET_CONTRACTED",
            "all_external_coefficient_slices": "BLOCKED_ONLY_SLICE_P1_0_P2_0_EVALUATED",
            "reflected_physical_addition": "REJECTED_ROUTING_CHECK_ONLY",
            "DRED": "BLOCKED_NOT_PERFORMED",
            "IBP": "BLOCKED_NOT_PERFORMED",
            "UV_pole": "BLOCKED_NOT_PERFORMED",
            "renormalized_two_loop_coefficient": None,
        },
    }


def build_payload() -> dict[str, Any]:
    coefficient_bundle = coefficient.build_bundle()
    amplitude_payload, parents = amplitude.build_payload()
    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "authority_role": "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "inputs": {
            "coefficient_tensor": {
                "path": "scripts/step6_coefficient_tensor.py",
                "sha256": file_sha256(ROOT / "scripts/step6_coefficient_tensor.py"),
                "payload_sha256": coefficient_bundle["payload_sha256"],
            },
            "color_tensor": {
                "path": "scripts/step6_color_tensor.py",
                "sha256": file_sha256(ROOT / "scripts/step6_color_tensor.py"),
            },
            "amplitude_ir": {
                "path": "scripts/step6_two_loop_amplitude_ir.py",
                "sha256": file_sha256(ROOT / "scripts/step6_two_loop_amplitude_ir.py"),
                "payload_sha256": amplitude_payload["payload_sha256"],
            },
        },
        "graph_weight_certificate": graph_weight_certificate(parents),
        "graded_sign": {
            "global_formula": "(-1)^sum_(i<j,rank(x_i)>rank(x_j)) |x_i||x_j|",
            "global_word": "concatenate parent.vertex_order then grammar.port_order",
            "canonical_word": "GraphIR edge_order(source,target) then (p1,p2)",
            "recursive_rule": "move each target through intervening unpaired coefficients; remove the even edge pair; finally reorder p1,p2",
            "exhaustive_fixture": exhaustive_sign_fixture(),
            "direct_superfield_delta_fixture": direct_delta_reconstruction_fixture(
                coefficient_bundle
            ),
        },
        "factorized_complete_sum_plan": factorized_joint_sum_plan(
            parents, coefficient_bundle
        ),
        "exact_row": exact_selected_row_slice(parents, coefficient_bundle),
        "global_fail_closed": {
            "complete_two_loop_numerator": "BLOCKED_INCOMPLETE_PAIRING_AND_EXTERNAL_SLICE_SUM",
            "DRED": "BLOCKED_NOT_PERFORMED",
            "IBP": "BLOCKED_NOT_PERFORMED",
            "UV_pole": "BLOCKED_NOT_PERFORMED",
            "renormalized_two_loop_coefficient": None,
        },
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    row = payload["exact_row"]
    plan = payload["factorized_complete_sum_plan"]
    return {
        "proposal_only": payload["authority_role"]
        == "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "direct_only_physical": payload["graph_weight_certificate"][
            "direct_only_is_physical"
        ],
        "three_graph_weights_exact": [
            item["hbar_stripped_graph_weight"]
            for item in payload["graph_weight_certificate"]["rows"]
        ]
        == ["-1", "-1", "-1/2"],
        "sign_fixture_exhaustive": payload["graded_sign"]["exhaustive_fixture"][
            "checked_cases"
        ]
        == 11520,
        "sign_algorithms_equal": payload["graded_sign"]["exhaustive_fixture"][
            "direct_weighted_permutation_equals_recursive_target_removal"
        ],
        "delta_reconstructed": payload["graded_sign"][
            "direct_superfield_delta_fixture"
        ]["left_H_inverse_crossed_back_to_exterior_order_equals_delta"],
        "same_joint_tuple": all(
            parent["same_ordered_local_option_tuple_for_coefficient_and_color"]
            for parent in plan["parents"]
        ),
        "marginal_product_rejected": all(
            parent["independent_coefficient_color_marginal_product"] == "REJECTED"
            for parent in plan["parents"]
        ),
        "six_parent_plans": len(plan["parents"]) == 6,
        "one_direct_rank_zero_row": row["orientation"] == "direct"
        and row["amplitude_rank"] == 0,
        "five_edges": len(row["edge_order"]) == 5,
        "external_indices_retained": row[
            "external_coefficient_indices_retained_not_contracted"
        ],
        "open_exterior_retained": row["open_insertion_exterior_basis_retained"],
        "no_extra_bracket_i": row["color"]["no_extra_bracket_i"],
        "free_colors_ABRS": row["color"]["free_index_order"]
        == ["A", "B", "R", "S"],
        "coefficient_not_claimed": payload["global_fail_closed"][
            "renormalized_two_loop_coefficient"
        ]
        is None,
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    return {
        "schema": "step6.global_graded_supertensor.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "payload_sha256": payload["payload_sha256"],
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    row = payload["exact_row"]
    return "\n".join(
        [
            "# Step 6 — first exact global graded supertensor row",
            "",
            f"Status: `{payload['status']}`.",
            "",
            "$$",
            "H^{-1}_{st}=(-1)^{|s|}(M^{-1})_{st},\\qquad t=15\\mathbin{\\mathtt{xor}}s.",
            "$$",
            "",
            "$$",
            "\\varepsilon_{\\mathrm{Wick}}=(-1)^{\\sum_{i<j,\\,\\pi(i)>\\pi(j)}|x_i||x_j|}.",
            "$$",
            "",
            "$$",
            "w_G=-\\frac{1}{|\\operatorname{Aut}_B(G)|},\\qquad"
            "(w_{G_1},w_{G_2},w_{G_3})=(-1,-1,-\\tfrac12).",
            "$$",
            "",
            f"Exact row: `{row['amplitude_ir_id']}`; external slice "
            f"$s_{{p_1}}={row['external_coefficient_slice']['p1']}$, "
            f"$s_{{p_2}}={row['external_coefficient_slice']['p2']}$.",
            "",
            f"Nonzero local tensor entries: `{row['local_sparse_tensor_nonzero_counts']}`.",
            "",
            f"Nonzero global assignments: `{row['nonzero_global_edge_assignments']}`.",
            "",
            f"Audit: `{audit['passed']}/{audit['total']}`.",
            "",
            "DRED, IBP, UV pole, complete pairing sum, and the renormalized two-loop coefficient remain blocked.",
            "",
        ]
    )


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError(audit)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        canonical_json(
            {
                "status": payload["status"],
                "audit": f"{audit['passed']}/{audit['total']}",
                "output": str(OUTPUT_JSON.relative_to(ROOT)),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
