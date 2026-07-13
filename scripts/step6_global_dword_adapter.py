#!/usr/bin/env python3
"""Typed adapter from one exact global coefficient assignment to DWordIR.

The adapter is deliberately narrow.  It freezes the first nonzero source-mask
assignment already found in the direct rank-zero physical row, reconstructs
all ten internal LEFT coefficient slots from the selected grammar programs,
and executes one actual insertion-port derivative word.  The executed word is
checked as an exact 16x16 matrix identity at the same edge momentum and basis
index.

The action-vertex measure comparison uses the coefficient-left derivative
rule on every leaf.  The complete global DWord contraction remains outside
this bounded one-assignment adapter.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import prod
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_global_supertensor as global_tensor
    from scripts import step6_two_loop_amplitude_ir as amplitude
    from scripts import step6_two_loop_dword as dword
except ModuleNotFoundError:  # direct execution from scripts/
    import step6_coefficient_tensor as coefficient
    import step6_global_supertensor as global_tensor
    import step6_two_loop_amplitude_ir as amplitude
    import step6_two_loop_dword as dword


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "generated/step6/global-dword-adapter"
OUTPUT_JSON = OUTPUT_DIR / "global-dword-adapter.json"
OUTPUT_PROGRAM = OUTPUT_DIR / "physical-port-projection-program.json"
OUTPUT_RESULT = OUTPUT_DIR / "physical-port-projection-result.json"
OUTPUT_MD = OUTPUT_DIR / "global-dword-adapter.md"
AUDIT = ROOT / "audits/step6-global-dword-adapter-verification.json"

SCHEMA = "step6.global_dword_adapter.v1"
STATUS = "PASS_COEFFICIENT_LEFT_DERIVATIVE_FIXED_FULL_GLOBAL_CONTRACTION_BLOCKED"
PHYSICAL_GRAPH_ID = global_tensor.PHYSICAL_GRAPH_ID
FROZEN_SOURCE_MASKS = {
    "e_AI": 0,
    "e_IB": 0,
    "e_CA": 4,
    "e_BC": 4,
    "e_BA": 11,
}
FIXED_FIELD = "LabeledLeaf.coefficient_parity"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qi_json(value: Any) -> dict[str, str]:
    return {
        "domain": dword.QI_DOMAIN,
        "re": str(value.re),
        "im": str(value.im),
    }


def constant_gaussian(value: Any) -> Any:
    if len(value.terms) != 1 or value.terms[0][0] != ():
        raise ValueError("a DWord branch coefficient must be a constant in Q(i)")
    return value.terms[0][1]


def matrix_json(value: Any) -> list[dict[str, Any]]:
    return [
        {
            "row": row,
            "column": column,
            "coefficient": polynomial.to_json(),
        }
        for (row, column), polynomial in value.entries
    ]


def dword_polynomial_to_oracle(rows: Sequence[Mapping[str, Any]]) -> Any:
    terms: dict[Any, Any] = {}
    for row in rows:
        monomial = tuple(
            (str(item["symbol"]), int(item["exponent"]))
            for item in row["monomial"]
        )
        scalar = row["factor"]
        if scalar["domain"] != dword.QI_DOMAIN:
            raise ValueError("DWord output left Q(i)")
        terms[monomial] = coefficient.oracle.Gaussian(
            Fraction(str(scalar["re"])), Fraction(str(scalar["im"]))
        )
    return coefficient.oracle.Poly.from_terms(terms)


@dataclass(frozen=True)
class SelectedContext:
    amplitude_payload: Mapping[str, Any]
    coefficient_bundle: Mapping[str, Any]
    parent: Any
    selected: Mapping[str, Mapping[str, Any]]
    programs: Mapping[str, Mapping[str, Any]]
    terms: Mapping[str, Mapping[str, Any]]


def selected_context() -> SelectedContext:
    amplitude_payload, parents = amplitude.build_payload()
    coefficient_bundle = coefficient.build_bundle()
    parent = next(
        row
        for row in parents
        if row.graph["graph_id"] == PHYSICAL_GRAPH_ID
        and row.orientation == "direct"
    )
    selected_tuple = parent.unrank(0)
    selected = dict(zip(parent.vertex_order, selected_tuple, strict=True))
    return SelectedContext(
        amplitude_payload=amplitude_payload,
        coefficient_bundle=coefficient_bundle,
        parent=parent,
        selected=selected,
        programs=global_tensor.option_program_index(coefficient_bundle),
        terms=coefficient_bundle["tensor_programs"]["compiled_terms"],
    )


def edge_order(context: SelectedContext) -> list[str]:
    return [
        str(edge["edge_id"])
        for edge in context.parent.graph["orientations"]["direct"]["edges"]
    ]


def basis_index(binding: Mapping[str, Any]) -> int:
    if binding["role"] == "BACKGROUND_EXTERNAL_ENDPOINT":
        return int(global_tensor.EXTERNAL_SLICE[global_tensor.external_label(binding)])
    source = FROZEN_SOURCE_MASKS[str(binding["edge_id"])]
    return source if binding["orientation_endpoint"] == "source" else 15 ^ source


def coefficient_id(vertex_id: str, grammar_port_id: str) -> str:
    return f"{vertex_id}::{grammar_port_id}"


def port_ledger(context: SelectedContext) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for vertex_id in context.parent.vertex_order:
        option = context.selected[vertex_id]
        option_id = str(option["local_amplitude_option_id"])
        program = context.programs[option_id]
        source_term = context.amplitude_payload["term_dictionary"][program["term_id"]]
        source_ports = {str(row["port_id"]): row for row in source_term["ports"]}
        bindings = {str(row["grammar_port_id"]): row for row in program["bindings"]}
        for local_position, port_id in enumerate(program["port_order"]):
            binding = bindings[str(port_id)]
            source_port = source_ports[str(port_id)]
            mask = basis_index(binding)
            rows.append(
                {
                    "global_position_including_external": len(rows),
                    "vertex_id": vertex_id,
                    "vertex_position": list(context.parent.vertex_order).index(vertex_id),
                    "local_position": local_position,
                    "term_id": str(program["term_id"]),
                    "local_amplitude_option_id": option_id,
                    "coefficient_id": coefficient_id(vertex_id, str(port_id)),
                    "grammar_port_id": str(port_id),
                    "topology_port_id": str(binding["topology_port_id"]),
                    "role": str(binding["role"]),
                    "orientation_endpoint": str(binding["orientation_endpoint"]),
                    "edge_id": binding["edge_id"],
                    "basis_index": mask,
                    "coefficient_parity": coefficient.coefficient_parity(mask),
                    "all_incoming_leaf_momentum": str(binding["all_incoming_leaf_momentum"]),
                    "all_incoming_leaf_momentum_vector": list(
                        binding["all_incoming_leaf_momentum_vector"]
                    ),
                    "grammar_derivative_word_outer_to_inner": list(
                        source_port["derivative_word_outer_to_inner"]
                    ),
                    "grammar_ast_path": list(source_port["ast_path"]),
                    "source_field": str(source_port["field"]),
                }
            )
    if len(rows) != 12:
        raise AssertionError("rank-zero I2-S3-S3-S4 row must have twelve ports")
    return rows


def global_join_key(
    context: SelectedContext, rows: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    internal = [row for row in rows if row["role"] == "QUANTUM_EDGE_ENDPOINT"]
    if len(internal) != 10:
        raise AssertionError("five internal propagators require ten coefficient slots")
    by_edge_endpoint = {
        (str(row["edge_id"]), str(row["orientation_endpoint"])): row
        for row in internal
    }
    pairings = []
    for current_edge in edge_order(context):
        pairings.append(
            {
                "edge_id": current_edge,
                "source_coefficient_id": by_edge_endpoint[
                    (current_edge, "source")
                ]["coefficient_id"],
                "target_coefficient_id": by_edge_endpoint[
                    (current_edge, "target")
                ]["coefficient_id"],
            }
        )
    value = {
        "parent_id": context.parent.amplitude_id(0),
        "parent_vertex_order": list(context.parent.vertex_order),
        "ordered_local_amplitude_option_ids": [
            context.selected[vertex]["local_amplitude_option_id"]
            for vertex in context.parent.vertex_order
        ],
        "global_left_coefficient_word": [
            {
                "coefficient_id": row["coefficient_id"],
                "basis_index": row["basis_index"],
                "parity": row["coefficient_parity"],
            }
            for row in internal
        ],
        "fixed_edge_pairing_order": pairings,
    }
    dword.validate_global_join_key(value)
    return value


def executor_endpoints(
    context: SelectedContext, rows: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    internal = [row for row in rows if row["role"] == "QUANTUM_EDGE_ENDPOINT"]
    by_edge_endpoint = {
        (str(row["edge_id"]), str(row["orientation_endpoint"])): row
        for row in internal
    }
    endpoints: list[dict[str, Any]] = []
    for row in rows:
        if row["role"] == "BACKGROUND_EXTERNAL_ENDPOINT":
            endpoints.append(
                {
                    "endpoint_id": row["coefficient_id"],
                    "endpoint_kind": "EXTERNAL_BACKGROUND",
                    "parity": row["coefficient_parity"],
                    "chirality": "NONE",
                    "equation_class": "ORDINARY",
                    "momentum": {
                        "basis": list(coefficient.MOMENTUM_BASIS),
                        "coefficients": row["all_incoming_leaf_momentum_vector"],
                    },
                    "edge_id": None,
                    "paired_endpoint_id": None,
                }
            )
            continue
        current_edge = str(row["edge_id"])
        current_endpoint = str(row["orientation_endpoint"])
        paired_endpoint = "target" if current_endpoint == "source" else "source"
        paired = by_edge_endpoint[(current_edge, paired_endpoint)]
        endpoints.append(
            {
                "endpoint_id": row["coefficient_id"],
                "endpoint_kind": (
                    "INTERNAL_SOURCE"
                    if current_endpoint == "source"
                    else "INTERNAL_TARGET"
                ),
                "parity": row["coefficient_parity"],
                "chirality": "NONE",
                "equation_class": "ORDINARY",
                "momentum": {
                    "basis": list(coefficient.MOMENTUM_BASIS),
                    "coefficients": row["all_incoming_leaf_momentum_vector"],
                },
                "edge_id": current_edge,
                "paired_endpoint_id": paired["coefficient_id"],
            }
        )
    endpoints.append(
        {
            "endpoint_id": "I::COMPOSITE_SOURCE_P",
            "endpoint_kind": "COMPOSITE_SOURCE",
            "parity": 0,
            "chirality": "NONE",
            "equation_class": "EOM",
            "momentum": {
                "basis": list(coefficient.MOMENTUM_BASIS),
                "coefficients": [0, 0, 1, 0, 0],
            },
            "edge_id": None,
            "paired_endpoint_id": None,
        }
    )
    for endpoint in endpoints:
        dword.endpoint_from_json(endpoint)
    return endpoints


class ScopeOnlyDerivativeEngine:
    """Exact coproduct expansion retaining the derivative target on every leaf."""

    def primitive(self, terms: Sequence[Any], primitive: str) -> tuple[Any, ...]:
        emitted = []
        for term in terms:
            prefix_parity = 0
            for position, factor in enumerate(term.factors):
                replacement = coefficient.oracle.LabeledLeaf(
                    factor.label,
                    factor.momentum,
                    factor.parity ^ 1,
                    factor.value,
                    (primitive,) + factor.derivative_word,
                    factor.coefficient_parity,
                )
                sign_exponent = prefix_parity ^ factor.coefficient_parity
                emitted.append(
                    coefficient.oracle.ProductTerm(
                        term.coefficient * (-1 if sign_exponent else 1),
                        term.factors[:position]
                        + (replacement,)
                        + term.factors[position + 1 :],
                    )
                )
                prefix_parity ^= factor.parity
        return coefficient._canonical_product_terms(emitted)

    def __call__(
        self, terms: Sequence[Any], tokens: Sequence[str]
    ) -> tuple[Any, ...]:
        emitted = []
        for branch_coefficient, primitive_word in coefficient._explicit_word_expansion(
            tokens
        ):
            branch = coefficient.scale_terms(
                terms, coefficient.oracle.Poly.constant(branch_coefficient)
            )
            for primitive in reversed(primitive_word):
                branch = self.primitive(branch, primitive)
            emitted.extend(branch)
        return coefficient._canonical_product_terms(emitted)


def local_basis_by_port(program: Mapping[str, Any]) -> dict[str, int]:
    return {
        str(binding["grammar_port_id"]): basis_index(binding)
        for binding in program["bindings"]
    }


def scope_terms(
    term: Mapping[str, Any], program: Mapping[str, Any]
) -> tuple[Any, ...]:
    basis = local_basis_by_port(program)
    leaves = coefficient._program_leaves(
        program, [basis[str(port)] for port in program["port_order"]]
    )
    engine = ScopeOnlyDerivativeEngine()
    terms = coefficient._evaluate_ast_terms(term["expression_ast"], leaves, {}, engine)
    if term["measure"] == "E_MINUS_ANTICHIRAL":
        terms = coefficient.scale_terms(
            engine(terms, ("barD2",)),
            coefficient.oracle.Poly.constant(Fraction(-1, 4)),
        )
    elif term["measure"] == "E_PLUS_CHIRAL":
        terms = coefficient.scale_terms(
            engine(terms, ("D2",)),
            coefficient.oracle.Poly.constant(Fraction(-1, 4)),
        )
    elif term["measure"] != "LOCAL_OPERATOR_INSERTION":
        raise ValueError(f"unknown measure {term['measure']}")
    return terms


def scope_branch_record(term: Any, branch_index: int) -> dict[str, Any]:
    return {
        "branch_index": branch_index,
        "coefficient": term.coefficient.to_json(),
        "ordered_factors": [
            {
                "grammar_port_id": factor.label,
                "derivative_word_outer_to_inner": list(factor.derivative_word),
                "derived_factor_parity": factor.parity,
                "coefficient_parity": factor.coefficient_parity,
            }
            for factor in term.factors
        ],
    }


def scope_branch_summary(
    context: SelectedContext,
) -> tuple[dict[str, Any], dict[str, tuple[Any, ...]]]:
    summaries: dict[str, Any] = {}
    retained: dict[str, tuple[Any, ...]] = {}
    for vertex_id in context.parent.vertex_order:
        option = context.selected[vertex_id]
        program = context.programs[str(option["local_amplitude_option_id"])]
        term = context.terms[str(program["term_id"])]
        branches = scope_terms(term, program)
        retained[vertex_id] = branches
        records = [scope_branch_record(branch, index) for index, branch in enumerate(branches)]
        summaries[vertex_id] = {
            "term_id": program["term_id"],
            "measure": term["measure"],
            "branch_count": len(branches),
            "complete_branch_ledger_sha256": digest(records),
            "first_branch": records[0],
            "branch_ledger_persisted_in_prior_global_row": False,
            "branch_ledger_regenerated_from_exact_expression_ast": True,
        }
    return summaries, retained


def direct_bare_measure_value(
    term: Mapping[str, Any], program: Mapping[str, Any]
) -> Any:
    basis = local_basis_by_port(program)
    leaves = coefficient._program_leaves(
        program, [basis[str(port)] for port in program["port_order"]]
    )
    inner = coefficient._evaluate_ast_terms(
        term["expression_ast"], leaves, {}, global_tensor.CachedDerivativeEngine()
    )
    parities = {
        port: coefficient.coefficient_parity(mask) for port, mask in basis.items()
    }
    return coefficient.apply_measure(
        coefficient.evaluate_product_terms(inner, parities), term["measure"]
    )


def distributed_bare_measure_value(
    term: Mapping[str, Any], program: Mapping[str, Any]
) -> Any:
    if term["measure"] not in {"E_MINUS_ANTICHIRAL", "E_PLUS_CHIRAL"}:
        raise ValueError("distributed measure comparison is only for chiral measures")
    basis = local_basis_by_port(program)
    leaves = coefficient._program_leaves(
        program, [basis[str(port)] for port in program["port_order"]]
    )
    engine = global_tensor.CachedDerivativeEngine()
    inner = coefficient._evaluate_ast_terms(term["expression_ast"], leaves, {}, engine)
    token = "barD2" if term["measure"] == "E_MINUS_ANTICHIRAL" else "D2"
    expanded = engine(inner, (token,))
    parities = {
        port: coefficient.coefficient_parity(mask) for port, mask in basis.items()
    }
    exterior = coefficient.evaluate_product_terms(expanded, parities)
    return exterior.coefficient(0).divide_scalar(-4)


def measure_scope_comparison(context: SelectedContext) -> dict[str, Any]:
    rows = []
    for vertex_id in context.parent.vertex_order:
        option = context.selected[vertex_id]
        program = context.programs[str(option["local_amplitude_option_id"])]
        term = context.terms[str(program["term_id"])]
        if term["measure"] == "LOCAL_OPERATOR_INSERTION":
            continue
        direct = direct_bare_measure_value(term, program)
        distributed = distributed_bare_measure_value(term, program)
        rows.append(
            {
                "vertex_id": vertex_id,
                "term_id": term["term_id"],
                "measure": term["measure"],
                "apply_measure_after_left_collection": coefficient.serialize_evaluation(
                    direct
                ),
                "distributed_measure_before_left_collection": coefficient.serialize_evaluation(
                    distributed
                ),
                "distributed_equals_direct": distributed == direct,
            }
        )
    if not rows or not all(row["distributed_equals_direct"] for row in rows):
        raise AssertionError("coefficient-left measure distribution identity failed")
    return {
        "comparison_domain": "EXACT_Q(i)_MOMENTUM_POLYNOMIALS",
        "rows": rows,
        "derivative_fix": {
            "field_name": FIXED_FIELD,
            "primitive_sign": "(-1)^(prefix_full_factor_parity+hit_leaf_coefficient_parity)",
            "replacement_preserves_field": True,
            "status": "PASS",
        },
        "complete_global_dword_equality": "BLOCKED_FULL_GLOBAL_DWORD_CONTRACTION_NOT_PERFORMED",
    }


def fixed_assignment_certificate(
    context: SelectedContext, rows: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    engine = global_tensor.CachedDerivativeEngine()
    local_values = []
    local_rows = []
    for vertex_id in context.parent.vertex_order:
        option = context.selected[vertex_id]
        program = context.programs[str(option["local_amplitude_option_id"])]
        term = context.terms[str(program["term_id"])]
        value = global_tensor.local_value(
            term, program, local_basis_by_port(program), engine
        )
        if not value:
            raise AssertionError(f"frozen assignment vanished at vertex {vertex_id}")
        local_values.append(value)
        serialized = global_tensor.serialize_value(value)
        local_rows.append(
            {
                "vertex_id": vertex_id,
                "term_id": term["term_id"],
                "value": serialized,
                "value_sha256": digest(serialized),
            }
        )
    product_value = global_tensor.multiply_local_values(local_values)
    if not product_value:
        raise AssertionError("frozen assignment local product vanished")
    metric_inverse = [
        [Fraction(str(value)) for value in row]
        for row in context.coefficient_bundle["coefficient_metric"]["M_inverse"]
    ]
    edge_rows = []
    edge_core = Fraction(1)
    for current_edge in edge_order(context):
        source = FROZEN_SOURCE_MASKS[current_edge]
        target = 15 ^ source
        h_inverse = (
            -1 if coefficient.coefficient_parity(source) else 1
        ) * metric_inverse[source][target]
        factor = Fraction(-2) * h_inverse
        edge_core *= factor
        edge_rows.append(
            {
                "edge_id": current_edge,
                "source_basis_index": source,
                "target_basis_index": target,
                "source_parity": coefficient.coefficient_parity(source),
                "target_parity": coefficient.coefficient_parity(target),
                "M_inverse_entry": str(metric_inverse[source][target]),
                "minus_2_H_inverse_factor": str(factor),
            }
        )
    selected = context.selected
    word, canonical, edge_pairs = global_tensor._word_for_assignment(
        context.parent,
        selected,
        context.programs,
        FROZEN_SOURCE_MASKS,
        global_tensor.EXTERNAL_SLICE,
    )
    sign = global_tensor.weighted_permutation_sign(word, canonical)
    recursive = global_tensor.recursive_target_removal_sign(word, edge_pairs)
    if sign != recursive:
        raise AssertionError("two exact graded sign algorithms disagree")
    contribution = product_value.scale(edge_core * sign)
    if not contribution:
        raise AssertionError("frozen assignment is not globally surviving")
    serialized_product = global_tensor.serialize_value(product_value)
    serialized_contribution = global_tensor.serialize_value(contribution)
    return {
        "classification": "ONE_EXACT_SURVIVING_EDGE_MASK_ASSIGNMENT",
        "source_masks_in_graph_edge_order": [
            FROZEN_SOURCE_MASKS[current_edge] for current_edge in edge_order(context)
        ],
        "source_mask_by_edge": dict(FROZEN_SOURCE_MASKS),
        "external_basis_indices": dict(global_tensor.EXTERNAL_SLICE),
        "port_basis_assignment": [
            {
                "coefficient_id": row["coefficient_id"],
                "basis_index": row["basis_index"],
                "parity": row["coefficient_parity"],
            }
            for row in rows
        ],
        "local_values": local_rows,
        "local_product": serialized_product,
        "local_product_sha256": digest(serialized_product),
        "edge_factors": edge_rows,
        "edge_core": str(edge_core),
        "graded_wick_sign": sign,
        "recursive_graded_wick_sign": recursive,
        "assignment_contribution_before_graph_weight": serialized_contribution,
        "assignment_contribution_sha256": digest(serialized_contribution),
        "survives": True,
    }


PRIMITIVE_TOKEN = {
    "D_plus": ("D", "+"),
    "D_minus": ("D", "-"),
    "barD_dotplus": ("BAR_D", "dot+"),
    "barD_dotminus": ("BAR_D", "dot-"),
}
TOKEN_PRIMITIVE = {value: key for key, value in PRIMITIVE_TOKEN.items()}


def actual_insertion_factor(
    context: SelectedContext,
    scope_by_vertex: Mapping[str, Sequence[Any]],
    rows: Sequence[Mapping[str, Any]],
) -> tuple[Any, Any, Mapping[str, Any]]:
    insertion_rows = {
        str(row["grammar_port_id"]): row for row in rows if row["vertex_id"] == "I"
    }
    for branch_index, branch in enumerate(scope_by_vertex["I"]):
        for factor in branch.factors:
            row = insertion_rows[factor.label]
            word = factor.derivative_word
            has_mixed_pair = any(
                left.startswith("D_") and right.startswith("barD_")
                for left, right in zip(word, word[1:])
            )
            if (
                row["edge_id"] == "e_IB"
                and row["orientation_endpoint"] == "source"
                and has_mixed_pair
            ):
                return branch_index, branch, row
    raise AssertionError("no actual insertion source factor contains a mixed pair")


def physical_projection_program(
    context: SelectedContext,
    rows: Sequence[Mapping[str, Any]],
    endpoints: Sequence[Mapping[str, Any]],
    join_key: Mapping[str, Any],
    scope_by_vertex: Mapping[str, Sequence[Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    branch_index, branch, row = actual_insertion_factor(context, scope_by_vertex, rows)
    factor = next(item for item in branch.factors if item.label == row["grammar_port_id"])
    insertion_program = context.programs[
        str(context.selected["I"]["local_amplitude_option_id"])
    ]
    insertion_term = context.terms[str(insertion_program["term_id"])]
    raw_coefficient = constant_gaussian(
        coefficient.parse_qi_polynomial(insertion_term["coefficient_raw"])
    )
    branch_coefficient = constant_gaussian(branch.coefficient) * raw_coefficient
    tokens = []
    for position, primitive in enumerate(factor.derivative_word):
        derivative_kind, component = PRIMITIVE_TOKEN[primitive]
        tokens.append(
            {
                "token_id": f"I.branch{branch_index}.{factor.label}.d{position}",
                "derivative_kind": derivative_kind,
                "spinor_component": component,
                "endpoint_id": row["coefficient_id"],
                "carrier": "PROPAGATOR_DELTA",
            }
        )
    program = {
        "schema_version": dword.EXECUTOR_SCHEMA_VERSION,
        "program_id": "PHYSICAL_RANK0_FIXED_ASSIGNMENT_I2_PORT_WORD",
        "program_kind": "GLOBAL_NUMERATOR",
        "left_coefficient_order": True,
        "endpoints": list(endpoints),
        "branches": [
            {
                "branch_id": f"I_SCOPE_BRANCH_{branch_index}_E_IB_SOURCE_FACTOR",
                "coefficient": qi_json(branch_coefficient),
                "ordered_tokens": tokens,
                "denominator_edges": edge_order(context),
            }
        ],
        "ibp_transfers": [],
        "global_join_key": dict(join_key),
    }
    metadata = {
        "execution_scope": "ONE_COMPLETE_ACTUAL_GRAMMAR_PORT_WORD",
        "not_the_complete_global_numerator": True,
        "vertex_id": "I",
        "term_id": insertion_term["term_id"],
        "local_amplitude_option_id": context.selected["I"][
            "local_amplitude_option_id"
        ],
        "scope_branch_index": branch_index,
        "grammar_port_id": factor.label,
        "coefficient_id": row["coefficient_id"],
        "edge_id": row["edge_id"],
        "orientation_endpoint": row["orientation_endpoint"],
        "basis_index": row["basis_index"],
        "basis_parity": row["coefficient_parity"],
        "all_incoming_momentum_vector": row["all_incoming_leaf_momentum_vector"],
        "derivative_word_outer_to_inner": list(factor.derivative_word),
        "branch_coefficient_including_raw_I2_coefficient": qi_json(branch_coefficient),
    }
    return program, metadata


def independent_oracle_comparison(
    program: Mapping[str, Any],
    result: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> dict[str, Any]:
    momentum = coefficient.momentum_from_vector(metadata["all_incoming_momentum_vector"])
    operators = coefficient.oracle.flat_operators(momentum)
    branch_coefficient = program["branches"][0]["coefficient"]
    scalar = coefficient.oracle.Gaussian(
        Fraction(str(branch_coefficient["re"])),
        Fraction(str(branch_coefficient["im"])),
    )
    original = coefficient.oracle.SparseMatrix.identity(16)
    for primitive in metadata["derivative_word_outer_to_inner"]:
        original = original @ operators[str(primitive)]
    original = original.scale(scalar)

    reconstructed = coefficient.oracle.SparseMatrix.from_entries(16, {})
    for output in result["terms"]:
        term_matrix = coefficient.oracle.SparseMatrix.identity(16)
        for token in output["ordered_tokens"]:
            primitive = TOKEN_PRIMITIVE[
                (str(token["derivative_kind"]), str(token["spinor_component"]))
            ]
            term_matrix = term_matrix @ operators[primitive]
        reconstructed = reconstructed + term_matrix.scale(
            dword_polynomial_to_oracle(output["polynomial"])
        )

    assigned_basis = coefficient.oracle.Exterior.basis(int(metadata["basis_index"]))
    original_assigned = original.apply(assigned_basis)
    reconstructed_assigned = reconstructed.apply(assigned_basis)
    original_json = matrix_json(original)
    reconstructed_json = matrix_json(reconstructed)
    assigned_json = coefficient.serialize_evaluation(original_assigned)
    return {
        "oracle": "INDEPENDENT_SYMBOLIC_16_BY_16_GRASSMANN_MATRICES",
        "same_edge_id": metadata["edge_id"],
        "same_orientation_endpoint": metadata["orientation_endpoint"],
        "same_all_incoming_momentum_vector": metadata[
            "all_incoming_momentum_vector"
        ],
        "same_basis_index": metadata["basis_index"],
        "original_operator_sha256": digest(original_json),
        "dword_reconstructed_operator_sha256": digest(reconstructed_json),
        "operator_matrices_equal": original == reconstructed,
        "assigned_basis_outputs_equal": original_assigned == reconstructed_assigned,
        "assigned_basis_output_nonzero": bool(original_assigned),
        "assigned_basis_output": assigned_json,
        "assigned_basis_output_sha256": digest(assigned_json),
        "numerical_sampling_used": False,
    }


def momentum_conservation(context: SelectedContext) -> dict[str, Any]:
    sums: dict[str, list[int]] = {}
    for vertex_id in context.parent.vertex_order:
        program = context.programs[
            str(context.selected[vertex_id]["local_amplitude_option_id"])
        ]
        vectors = [
            tuple(int(value) for value in binding["all_incoming_leaf_momentum_vector"])
            for binding in program["bindings"]
        ]
        sums[vertex_id] = [sum(vector[index] for vector in vectors) for index in range(5)]
    return {
        "basis": list(coefficient.MOMENTUM_BASIS),
        "leaf_sums": sums,
        "I_plus_composite_source_P": [
            sums["I"][index] + (1 if index == 2 else 0) for index in range(5)
        ],
        "A": sums["A"],
        "B": sums["B"],
        "C_equals_declared_external_relation": sums["C"]
        == context.parent.graph["momentum_contract"]["relation_vector"],
        "declared_relation": context.parent.graph["momentum_contract"][
            "all_incoming_relation"
        ],
    }


def build_payload() -> dict[str, Any]:
    context = selected_context()
    ports = port_ledger(context)
    join_key = global_join_key(context, ports)
    endpoints = executor_endpoints(context, ports)
    scope_summary, scope_by_vertex = scope_branch_summary(context)
    assignment = fixed_assignment_certificate(context, ports)
    measure_comparison = measure_scope_comparison(context)
    program, projection = physical_projection_program(
        context, ports, endpoints, join_key, scope_by_vertex
    )
    result = dword.execute_edge_tagged_dalgebra(program)
    oracle_comparison = independent_oracle_comparison(program, result, projection)
    branch_counts = [scope_summary[vertex]["branch_count"] for vertex in context.parent.vertex_order]
    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "authority_role": "PROPOSAL_ONLY_EXACT_ADAPTER_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "inputs": {
            "amplitude_ir": {
                "path": "scripts/step6_two_loop_amplitude_ir.py",
                "sha256": file_sha256(ROOT / "scripts/step6_two_loop_amplitude_ir.py"),
                "payload_sha256": context.amplitude_payload["payload_sha256"],
            },
            "coefficient_tensor": {
                "path": "scripts/step6_coefficient_tensor.py",
                "sha256": file_sha256(ROOT / "scripts/step6_coefficient_tensor.py"),
                "payload_sha256": context.coefficient_bundle["payload_sha256"],
            },
            "global_tensor": {
                "path": "scripts/step6_global_supertensor.py",
                "sha256": file_sha256(ROOT / "scripts/step6_global_supertensor.py"),
            },
            "dword_executor": {
                "path": "scripts/step6_two_loop_dword.py",
                "sha256": file_sha256(ROOT / "scripts/step6_two_loop_dword.py"),
            },
        },
        "physical_parent": {
            "graph_id": context.parent.graph["graph_id"],
            "orientation": context.parent.orientation,
            "amplitude_rank": 0,
            "amplitude_ir_id": context.parent.amplitude_id(0),
            "vertex_order": list(context.parent.vertex_order),
            "edge_order": edge_order(context),
            "selected_local_amplitude_option_ids": {
                vertex: context.selected[vertex]["local_amplitude_option_id"]
                for vertex in context.parent.vertex_order
            },
        },
        "momentum_conservation": momentum_conservation(context),
        "port_ledger": ports,
        "global_join_key": join_key,
        "fixed_assignment": assignment,
        "scope_expansion": {
            "method": "EXACT_EXPRESSION_AST_GRADED_LEIBNIZ_WITH_MEASURE_SCOPE",
            "per_vertex": scope_summary,
            "factorized_global_branch_counts": branch_counts,
            "factorized_global_cartesian_cardinality": prod(branch_counts),
            "full_cartesian_materialization_performed": False,
        },
        "physical_dword_projection": projection,
        "physical_dword_program": program,
        "physical_dword_result": result,
        "independent_oracle_comparison": oracle_comparison,
        "measure_scope_comparison": measure_comparison,
        "acceptance_boundary": {
            "typed_ten_slot_left_assignment": "PASS",
            "one_actual_complete_grammar_port_word": "PASS",
            "same_assignment_16_by_16_oracle": "PASS",
            "coefficient_left_derivative_fix": "PASS",
            "complete_global_dword_equality": "BLOCKED_FULL_GLOBAL_DWORD_CONTRACTION_NOT_PERFORMED",
            "global_numerator_claimed": False,
            "integral_reduction_performed": False,
            "pole_claimed": False,
            "two_loop_coefficient_claimed": False,
        },
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    parent = payload["physical_parent"]
    join_key = payload["global_join_key"]
    assignment = payload["fixed_assignment"]
    endpoints = payload["physical_dword_program"]["endpoints"]
    endpoint_kinds = [row["endpoint_kind"] for row in endpoints]
    internal_word = join_key["global_left_coefficient_word"]
    pairings = join_key["fixed_edge_pairing_order"]
    paired_ids = [
        item
        for pairing in pairings
        for item in (
            pairing["source_coefficient_id"],
            pairing["target_coefficient_id"],
        )
    ]
    checks = {
        "direct_rank_zero_physical_parent": parent["orientation"] == "direct"
        and parent["amplitude_rank"] == 0
        and parent["graph_id"] == PHYSICAL_GRAPH_ID,
        "five_graphir_edges": len(parent["edge_order"]) == 5,
        "frozen_assignment_survives": assignment["survives"] is True
        and assignment["source_masks_in_graph_edge_order"] == [0, 0, 4, 4, 11],
        "ten_internal_left_coefficients": len(internal_word) == 10
        and len({row["coefficient_id"] for row in internal_word}) == 10,
        "left_parities_match_basis_popcount": all(
            row["parity"] == (int(row["basis_index"]).bit_count() & 1)
            for row in internal_word
        ),
        "five_pairings_cover_word_exactly": len(pairings) == 5
        and sorted(paired_ids)
        == sorted(row["coefficient_id"] for row in internal_word),
        "external_p1_p2_preserved": endpoint_kinds.count("EXTERNAL_BACKGROUND") == 2
        and {
            tuple(row["momentum"]["coefficients"])
            for row in endpoints
            if row["endpoint_kind"] == "EXTERNAL_BACKGROUND"
        }
        == {(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)},
        "composite_source_preserved": endpoint_kinds.count("COMPOSITE_SOURCE") == 1,
        "all_incoming_momenta_close": payload["momentum_conservation"][
            "I_plus_composite_source_P"
        ]
        == [0, 0, 0, 0, 0]
        and payload["momentum_conservation"]["A"] == [0, 0, 0, 0, 0]
        and payload["momentum_conservation"]["B"] == [0, 0, 0, 0, 0]
        and payload["momentum_conservation"]["C_equals_declared_external_relation"],
        "grammar_words_preserved": all(
            row["grammar_derivative_word_outer_to_inner"]
            for row in payload["port_ledger"]
        ),
        "scope_branches_regenerated": all(
            row["branch_ledger_regenerated_from_exact_expression_ast"]
            and row["branch_count"] > 0
            for row in payload["scope_expansion"]["per_vertex"].values()
        ),
        "actual_complete_port_word_executed": payload["physical_dword_projection"][
            "execution_scope"
        ]
        == "ONE_COMPLETE_ACTUAL_GRAMMAR_PORT_WORD"
        and len(payload["physical_dword_projection"]["derivative_word_outer_to_inner"])
        == len(payload["physical_dword_program"]["branches"][0]["ordered_tokens"]),
        "dword_oracle_operator_equality": payload["independent_oracle_comparison"][
            "operator_matrices_equal"
        ],
        "same_assigned_basis_equality": payload["independent_oracle_comparison"][
            "assigned_basis_outputs_equal"
        ]
        and payload["independent_oracle_comparison"]["assigned_basis_output_nonzero"],
        "no_numerical_sampling": not payload["independent_oracle_comparison"][
            "numerical_sampling_used"
        ],
        "coefficient_left_measure_scope_identity": all(
            row["distributed_equals_direct"]
            for row in payload["measure_scope_comparison"]["rows"]
        ),
        "coefficient_parity_field_is_authoritative": payload[
            "measure_scope_comparison"
        ]["derivative_fix"]["field_name"]
        == FIXED_FIELD
        and payload["measure_scope_comparison"]["derivative_fix"]["status"]
        == "PASS",
        "complete_global_equality_fail_closed": payload["acceptance_boundary"][
            "complete_global_dword_equality"
        ]
        == "BLOCKED_FULL_GLOBAL_DWORD_CONTRACTION_NOT_PERFORMED"
        and payload["acceptance_boundary"]["global_numerator_claimed"] is False,
        "no_reduction_pole_or_coefficient_claim": payload["acceptance_boundary"][
            "integral_reduction_performed"
        ]
        is False
        and payload["acceptance_boundary"]["pole_claimed"] is False
        and payload["acceptance_boundary"]["two_loop_coefficient_claimed"] is False,
        "external_result_firewall": payload["external_result_used_as_calculation_input"]
        is False,
        "payload_hash_recomputes": payload["payload_sha256"]
        == digest({key: value for key, value in payload.items() if key != "payload_sha256"}),
    }
    return checks


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    failures = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema": "step6.global_dword_adapter.audit.v1",
        "status": "PASS" if not failures else "FAIL",
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "payload_sha256": payload["payload_sha256"],
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    projection = payload["physical_dword_projection"]
    branch_counts = payload["scope_expansion"]["factorized_global_branch_counts"]
    return "\n".join(
        [
            "# Step 6 — global LEFT assignment to typed DWord",
            "",
            f"`{payload['status']}`",
            "",
            "$$",
            "(s_{e_{AI}},s_{e_{IB}},s_{e_{CA}},s_{e_{BC}},s_{e_{BA}})",
            r"=(0,0,4,4,11),\qquad t_e=15\mathbin{\mathtt{xor}}s_e.",
            "$$",
            "",
            "$$",
            f"N_{{\rm branch}}={'\\cdot'.join(str(value) for value in branch_counts)}",
            f"={payload['scope_expansion']['factorized_global_cartesian_cardinality']}.",
            "$$",
            "",
            "Executed actual port:",
            "",
            "$$",
            r"{}:\quad {}.".format(
                projection["edge_id"],
                "\\,".join(projection["derivative_word_outer_to_inner"]),
            ),
            "$$",
            "",
            "$$",
            r"\mathcal M_{16\times16}^{\rm DWord}=\mathcal M_{16\times16}^{\rm direct}.",
            "$$",
            "",
            "For each selected antichiral action vertex:",
            "",
            "$$",
            r"\left[\bar D^2\right]_{\rm distributed,LEFT}",
            r"=\left[\bar D^2\right]_{\rm apply\ measure\ after\ LEFT\ collection}.",
            "$$",
            "",
            f"Derivative field: `{FIXED_FIELD}`.",
            "",
            f"Audit: `{audit['passed']}/{len(audit['checks'])}`.",
            "",
        ]
    )


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError(audit)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUTPUT_PROGRAM.write_text(
        json.dumps(payload["physical_dword_program"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUTPUT_RESULT.write_text(
        json.dumps(payload["physical_dword_result"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUTPUT_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        canonical_json(
            {
                "status": payload["status"],
                "audit": f"{audit['passed']}/{len(audit['checks'])}",
                "operator_matrices_equal": payload["independent_oracle_comparison"][
                    "operator_matrices_equal"
                ],
                "complete_global_dword_equality": payload["acceptance_boundary"][
                    "complete_global_dword_equality"
                ],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
