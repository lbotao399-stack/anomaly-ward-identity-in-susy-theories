#!/usr/bin/env python3
"""Exact coefficient-space TensorProgramIR for the proposal-only Step-6 parents.

This layer compiles the complete local grammar AST and evaluates requested
Grassmann-basis entries.  It deliberately stops before the five-edge tensor
contraction, DRED, IBP, UV subtraction, or any two-loop coefficient.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
GRAMMAR = ROOT / "generated/step6/two-loop-grammar/project-two-loop-grammar.json"
GRAPHIR = ROOT / "generated/step6/two-loop-graphir/two-loop-graphir.json"
AMPLITUDE = ROOT / "generated/step6/two-loop-amplitude-ir/pre-dalgebra-amplitude-ir.json"
ORACLE = ROOT / "scripts/step6_symbolic_grassmann_oracle.py"
OUTPUT_DIR = ROOT / "generated/step6/coefficient-tensor"
OUTPUT_JSON = OUTPUT_DIR / "coefficient-tensor-programs.json"
OUTPUT_MD = OUTPUT_DIR / "coefficient-tensor-programs.md"
AUDIT = ROOT / "audits/step6-coefficient-tensor-verification.json"

SCHEMA = "step6.coefficient_tensor_program_ir.v1"
STATUS = "PASS_LOCAL_TENSOR_PROGRAMS_GLOBAL_CONTRACTION_BLOCKED"
MOMENTUM_BASIS = ("k", "l", "P", "p1", "p2")
RELATION = (0, 0, 1, 1, 1)
SELECTED_FAMILIES = (
    "I2",
    "I3",
    "S3_PLUS",
    "S3_MINUS",
    "S4_PLUS",
    "S4_MINUS",
)
SUPPORTED_OPS = (
    "V",
    "FlatD",
    "FlatBarD",
    "D2",
    "BarD2",
    "FreeColor",
    "AdjointBracket",
    "OrderedProduct",
    "SpinorRaise",
    "GaugeInvariantPairing",
)


def _load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    import sys

    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


oracle = _load_module(ORACLE, "step6_symbolic_grassmann_oracle_for_tensor")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fraction_json(value: Fraction) -> str:
    return str(value)


def fraction_matrix_json(matrix: Sequence[Sequence[Fraction]]) -> list[list[str]]:
    return [[fraction_json(value) for value in row] for row in matrix]


def exterior_product_sign(left_mask: int, right_mask: int, width: int = 4) -> int:
    inversions = sum(
        1
        for left in range(width)
        if (left_mask >> left) & 1
        for right in range(width)
        if (right_mask >> right) & 1 and left > right
    )
    return -1 if inversions & 1 else 1


def coefficient_pairing_matrix() -> list[list[Fraction]]:
    """M_st=[e_s e_t]_D for the locked full-measure normalization."""

    zero = oracle.BispinorMomentum(
        "0", ((oracle.ZERO, oracle.ZERO), (oracle.ZERO, oracle.ZERO))
    )
    operators = oracle.flat_operators(zero)
    matrix: list[list[Fraction]] = []
    for source_mask in range(16):
        row: list[Fraction] = []
        for target_mask in range(16):
            value = oracle.full_measure(
                oracle.Exterior.basis(source_mask) * oracle.Exterior.basis(target_mask),
                operators,
            )
            if not value:
                row.append(Fraction(0))
                continue
            if len(value.terms) != 1 or value.terms[0][0] != () or value.terms[0][1].im:
                raise AssertionError("zero-momentum coefficient pairing left Q")
            row.append(value.terms[0][1].re)
        matrix.append(row)
    return matrix


def invert_fraction_matrix(matrix: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    augmented = [
        [Fraction(value) for value in row]
        + [Fraction(1 if row_index == column else 0) for column in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for pivot_column in range(size):
        pivot_row = next(
            (row for row in range(pivot_column, size) if augmented[row][pivot_column]),
            None,
        )
        if pivot_row is None:
            raise ValueError("singular coefficient pairing")
        augmented[pivot_column], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[pivot_column],
        )
        pivot = augmented[pivot_column][pivot_column]
        augmented[pivot_column] = [value / pivot for value in augmented[pivot_column]]
        for row in range(size):
            if row == pivot_column:
                continue
            factor = augmented[row][pivot_column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[pivot_column])
                ]
    return [row[size:] for row in augmented]


def multiply_fraction_matrices(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    size = len(left)
    if any(len(row) != size for row in left) or len(right) != size or any(
        len(row) != size for row in right
    ):
        raise ValueError("matrix sizes disagree")
    return [
        [sum(left[row][pivot] * right[pivot][column] for pivot in range(size)) for column in range(size)]
        for row in range(size)
    ]


def normalized_difference_delta_coefficients() -> list[list[Fraction]]:
    """Expand -4 product_i(theta_i-theta'_i) in theta-before-theta' order."""

    coefficients = [[Fraction(0) for _ in range(16)] for _ in range(16)]
    for primed_choice_mask in range(16):
        occupied = 0
        coefficient = Fraction(-4)
        for generator in range(4):
            if (primed_choice_mask >> generator) & 1:
                selected = 4 + generator
                coefficient = -coefficient
            else:
                selected = generator
            if (occupied >> selected) & 1:
                raise AssertionError("difference delta repeated a generator")
            higher = sum(1 for index in range(selected + 1, 8) if (occupied >> index) & 1)
            if higher & 1:
                coefficient = -coefficient
            occupied |= 1 << selected
        source_mask = occupied & 15
        target_mask = (occupied >> 4) & 15
        coefficients[source_mask][target_mask] += coefficient
    return coefficients


def identity_fraction_matrix(size: int = 16) -> list[list[Fraction]]:
    return [
        [Fraction(1 if row == column else 0) for column in range(size)]
        for row in range(size)
    ]


def coefficient_parity(mask: int) -> int:
    if not 0 <= mask < 16:
        raise ValueError("coefficient basis mask lies outside [0,15]")
    return mask.bit_count() & 1


def left_ordered_coefficient_hessian(
    pairing: Sequence[Sequence[Fraction]],
) -> list[list[Fraction]]:
    """H_st=(-1)^(|s||t|)M_st after collecting v_s v_t to the left."""

    return [
        [
            ((-1) if coefficient_parity(source) * coefficient_parity(target) else 1)
            * pairing[source][target]
            for target in range(16)
        ]
        for source in range(16)
    ]


def left_ordered_covariance_core(
    metric_inverse: Sequence[Sequence[Fraction]],
) -> list[list[Fraction]]:
    """H^{-1}_st=(-1)^|s| (M^{-1})_st in the locked left order."""

    return [
        [
            ((-1) if coefficient_parity(source) else 1)
            * metric_inverse[source][target]
            for target in range(16)
        ]
        for source in range(16)
    ]


def reconstruct_delta_from_left_ordered_covariance(
    covariance_core: Sequence[Sequence[Fraction]],
) -> list[list[Fraction]]:
    """Move the target coefficient through e_s and recover Delta coefficients."""

    return [
        [
            ((-1) if coefficient_parity(source) * coefficient_parity(target) else 1)
            * covariance_core[source][target]
            for target in range(16)
        ]
        for source in range(16)
    ]


def edge_covariance_entry(
    source_mask: int,
    target_mask: int,
    metric_inverse: Sequence[Sequence[Fraction]],
    *,
    coefficient_kernel: str = "LEFT_ORDERED_H_INVERSE",
) -> dict[str, Any]:
    if coefficient_kernel == "identity_16":
        raise ValueError("identity_16 is an operator identity, not coefficient covariance")
    if coefficient_kernel == "M_inverse":
        raise ValueError("bare M_inverse omits the locked coefficient/exterior ordering sign")
    if coefficient_kernel != "LEFT_ORDERED_H_INVERSE":
        raise ValueError("undeclared coefficient covariance kernel")
    ordering_sign = -1 if coefficient_parity(source_mask) else 1
    covariance_core = ordering_sign * metric_inverse[source_mask][target_mask]
    value = Fraction(-2) * covariance_core
    source_parity = coefficient_parity(source_mask)
    target_parity = coefficient_parity(target_mask)
    return {
        "ordered_endpoint_basis": [source_mask, target_mask],
        "ordered_endpoint_coefficient_parities": [source_parity, target_parity],
        "entry_even_when_nonzero": value == 0 or source_parity == target_parity,
        "left_coefficient_ordering_sign": ordering_sign,
        "left_ordered_H_inverse_entry": str(covariance_core),
        "ordinary_kernel_coefficient": str(value),
        "factorized_rule": "hbar*(-2*g^2)*(-1)^|s|*M_inverse[s,t]/r^2",
        "formal_factors": {"hbar_power": 1, "g_squared_power": 1, "edge_square_power": -1},
        "endpoint_order": "SOURCE_COEFFICIENT_THEN_TARGET_COEFFICIENT_NO_REORDERING",
        "coefficient_supertranspose_convention": "C^sT[s,t]=(-1)^(|s||t|)*C[t,s]",
        "global_koszul_wick_permutation": "BLOCKED_NOT_DERIVED_AT_THIS_LAYER",
    }


def vector_add(*vectors: Sequence[int]) -> tuple[int, ...]:
    if not vectors:
        return (0,) * len(MOMENTUM_BASIS)
    if any(len(vector) != len(MOMENTUM_BASIS) for vector in vectors):
        raise ValueError("momentum vector has wrong basis")
    return tuple(sum(vector[index] for vector in vectors) for index in range(len(MOMENTUM_BASIS)))


def vector_scale(coefficient: int, vector: Sequence[int]) -> tuple[int, ...]:
    return tuple(coefficient * value for value in vector)


def render_vector(vector: Sequence[int]) -> str:
    terms: list[str] = []
    for coefficient, symbol in zip(vector, MOMENTUM_BASIS):
        if coefficient == 0:
            continue
        if coefficient == 1:
            terms.append(symbol)
        elif coefficient == -1:
            terms.append(f"-{symbol}")
        else:
            terms.append(f"{coefficient}*{symbol}")
    rendered = "+".join(terms).replace("+-", "-")
    return rendered or "0"


def momentum_from_vector(vector: Sequence[int]) -> Any:
    component_suffixes = (("pp", "pm"), ("mp", "mm"))
    components: list[list[Any]] = []
    for row in range(2):
        component_row: list[Any] = []
        for column in range(2):
            value = oracle.ZERO
            suffix = component_suffixes[row][column]
            for coefficient, symbol in zip(vector, MOMENTUM_BASIS):
                if coefficient:
                    value = value + coefficient * oracle.Poly.variable(f"{symbol}_{suffix}")
            component_row.append(value)
        components.append(component_row)
    return oracle.BispinorMomentum(
        render_vector(vector),
        ((components[0][0], components[0][1]), (components[1][0], components[1][1])),
    )


def parse_qi_polynomial(record: Mapping[str, Any]) -> Any:
    rational = Fraction(str(record["rational"]))
    i_power = int(record["i_power_reduced"]) % 4
    units = (oracle.ONE_QI, oracle.I_QI, -oracle.ONE_QI, -oracle.I_QI)
    value = oracle.Poly.constant(units[i_power] * rational)
    for symbol in record.get("symbols", []):
        value = value * oracle.Poly.variable(str(symbol).replace("^", "_pow_"))
    return value


def _canonical_product_terms(terms: Iterable[Any]) -> tuple[Any, ...]:
    merged: dict[tuple[Any, ...], Any] = {}
    for term in terms:
        merged[term.factors] = merged.get(term.factors, oracle.ZERO) + term.coefficient
    return tuple(
        oracle.ProductTerm(coefficient, factors)
        for factors, coefficient in sorted(
            merged.items(), key=lambda item: tuple(factor.label for factor in item[0])
        )
        if coefficient
    )


def multiply_terms(left: Sequence[Any], right: Sequence[Any]) -> tuple[Any, ...]:
    return _canonical_product_terms(
        oracle.ProductTerm(a.coefficient * b.coefficient, a.factors + b.factors)
        for a in left
        for b in right
    )


def scale_terms(terms: Sequence[Any], coefficient: Any) -> tuple[Any, ...]:
    return tuple(
        oracle.ProductTerm(term.coefficient * coefficient, term.factors) for term in terms
    )


def _explicit_word_expansion(tokens: Sequence[str]) -> tuple[tuple[Any, tuple[str, ...]], ...]:
    expansions: dict[str, tuple[tuple[Any, tuple[str, ...]], ...]] = {
        "D_plus": ((oracle.ONE_QI, ("D_plus",)),),
        "D_minus": ((oracle.ONE_QI, ("D_minus",)),),
        "barD_dotplus": ((oracle.ONE_QI, ("barD_dotplus",)),),
        "barD_dotminus": ((oracle.ONE_QI, ("barD_dotminus",)),),
        "D2": (
            (oracle.ONE_QI, ("D_minus", "D_plus")),
            (-oracle.ONE_QI, ("D_plus", "D_minus")),
        ),
        "barD2": (
            (oracle.ONE_QI, ("barD_dotplus", "barD_dotminus")),
            (-oracle.ONE_QI, ("barD_dotminus", "barD_dotplus")),
        ),
    }
    branches: list[tuple[Any, tuple[str, ...]]] = [(oracle.ONE_QI, ())]
    for token in tokens:
        if token not in expansions:
            raise KeyError(token)
        branches = [
            (left_coefficient * right_coefficient, left_word + right_word)
            for left_coefficient, left_word in branches
            for right_coefficient, right_word in expansions[token]
        ]
    return tuple(branches)


def _explicit_apply_primitive(terms: Sequence[Any], primitive: str) -> tuple[Any, ...]:
    emitted: list[Any] = []
    for term in terms:
        prefix_parity = 0
        for position, factor in enumerate(term.factors):
            differentiated = oracle.flat_operators(factor.momentum)[primitive].apply(factor.value)
            if differentiated:
                replacement = oracle.LabeledLeaf(
                    factor.label,
                    factor.momentum,
                    factor.parity ^ 1,
                    differentiated,
                    (primitive,) + factor.derivative_word,
                )
                emitted.append(
                    oracle.ProductTerm(
                        term.coefficient * (-1 if prefix_parity else 1),
                        term.factors[:position] + (replacement,) + term.factors[position + 1 :],
                    )
                )
            prefix_parity ^= factor.parity
    return _canonical_product_terms(emitted)


def explicit_apply_word(terms: Sequence[Any], tokens: Sequence[str]) -> tuple[Any, ...]:
    emitted: list[Any] = []
    for coefficient, primitive_word in _explicit_word_expansion(tokens):
        branch = scale_terms(terms, oracle.Poly.constant(coefficient))
        for primitive in reversed(primitive_word):
            branch = _explicit_apply_primitive(branch, primitive)
        emitted.extend(branch)
    return _canonical_product_terms(emitted)


DerivativeEngine = Callable[[Sequence[Any], Sequence[str]], tuple[Any, ...]]


def oracle_apply_word(terms: Sequence[Any], tokens: Sequence[str]) -> tuple[Any, ...]:
    return oracle.apply_word_to_product_terms(terms, tokens)


def _resolved_component(index: str, environment: Mapping[str, str]) -> str:
    if index in ("+", "-"):
        return index
    if index in ("a", "dot_a"):
        if index not in environment:
            raise ValueError(f"unresolved generic spinor index {index}")
        component = environment[index]
        if component not in ("+", "-"):
            raise ValueError("spinor component must be + or -")
        return component
    raise ValueError(f"undeclared spinor index {index}")


def _derivative_token(op: str, index: str, environment: Mapping[str, str]) -> str:
    component = _resolved_component(index, environment)
    if op == "FlatD":
        return "D_plus" if component == "+" else "D_minus"
    if op == "FlatBarD":
        return "barD_dotplus" if component == "+" else "barD_dotminus"
    raise ValueError(op)


def _generic_index_kind(node: Mapping[str, Any]) -> str:
    encoded = canonical_json(node)
    if '"index":"dot_a"' in encoded:
        return "dot_a"
    if '"index":"a"' in encoded:
        return "a"
    raise ValueError("SpinorRaise has no generic index below it")


def _evaluate_ast_terms(
    node: Mapping[str, Any],
    leaves: Mapping[str, Any],
    environment: Mapping[str, str],
    derivative_engine: DerivativeEngine,
) -> tuple[Any, ...]:
    op = str(node["op"])
    args = node.get("args", [])
    attrs = node.get("attrs", {})
    if op == "V":
        port_id = str(attrs["port_id"])
        if port_id not in leaves:
            raise KeyError(f"unbound grammar port {port_id}")
        return (oracle.ProductTerm(oracle.ONE, (leaves[port_id],)),)
    if op in ("FlatD", "FlatBarD"):
        child = _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
        return derivative_engine(child, (_derivative_token(op, str(attrs["index"]), environment),))
    if op == "D2":
        child = _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
        return derivative_engine(child, ("D2",))
    if op == "BarD2":
        child = _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
        return derivative_engine(child, ("barD2",))
    if op == "FreeColor":
        return _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
    if op == "AdjointBracket":
        # Component rule: [Y,Z]^C=i*c[A,B,C]Y^A Z^B.  The grammar Q(i)
        # coefficient already contains this i; superspace factors remain ordered.
        left = _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
        right = _evaluate_ast_terms(args[1], leaves, environment, derivative_engine)
        return multiply_terms(left, right)
    if op == "OrderedProduct":
        if not args:
            raise ValueError("empty OrderedProduct")
        result = _evaluate_ast_terms(args[0], leaves, environment, derivative_engine)
        for child in args[1:]:
            result = multiply_terms(
                result, _evaluate_ast_terms(child, leaves, environment, derivative_engine)
            )
        return result
    if op == "SpinorRaise":
        raise ValueError("SpinorRaise must be consumed by GaugeInvariantPairing")
    if op == "GaugeInvariantPairing":
        if len(args) != 2 or args[0].get("op") != "SpinorRaise":
            raise ValueError("GaugeInvariantPairing requires left SpinorRaise")
        generic = _generic_index_kind(args[0])
        raised_child = args[0]["args"][0]
        lowered_child = args[1]
        branches: list[Any] = []
        # epsilon^(+-)=+1, epsilon^(-+)=-1.
        for upper_component, lower_component, epsilon in (
            ("+", "-", 1),
            ("-", "+", -1),
        ):
            left_environment = dict(environment)
            left_environment[generic] = lower_component
            right_environment = dict(environment)
            right_environment[generic] = upper_component
            left = _evaluate_ast_terms(
                raised_child, leaves, left_environment, derivative_engine
            )
            right = _evaluate_ast_terms(
                lowered_child, leaves, right_environment, derivative_engine
            )
            branches.extend(scale_terms(multiply_terms(left, right), oracle.Poly.constant(epsilon)))
        return _canonical_product_terms(branches)
    raise ValueError(f"unsupported grammar op {op}")


def evaluate_product_terms(
    terms: Sequence[Any], coefficient_parities_by_label: Mapping[str, int]
) -> Any:
    """Collect ordered coefficient variables left of the exterior monomials.

    For (v_s e_s)(v_t e_t), moving v_t through e_s contributes
    (-1)^(|v_t| degree(e_s)).  Coefficient variables themselves remain in the
    grammar factor order; no coefficient-coefficient reordering is made.
    """

    result = oracle.Exterior()
    for term in terms:
        value = oracle.Exterior.basis(0, term.coefficient)
        for factor in term.factors:
            if factor.label not in coefficient_parities_by_label:
                raise KeyError(f"missing coefficient parity for {factor.label}")
            coefficient_parity_value = coefficient_parities_by_label[factor.label]
            for mask, _ in factor.value.terms:
                expected_exterior_parity = coefficient_parity_value ^ factor.parity
                if (mask.bit_count() & 1) != expected_exterior_parity:
                    raise AssertionError("derivative output violated coefficient/exterior parity")
            collected: dict[int, Any] = {}
            for left_mask, left_coefficient in value.terms:
                for right_mask, right_coefficient in factor.value.terms:
                    if left_mask & right_mask:
                        continue
                    cross_sign = -1 if coefficient_parity_value and (left_mask.bit_count() & 1) else 1
                    wedge_sign = oracle.exterior_sign(left_mask, right_mask)
                    output_mask = left_mask | right_mask
                    collected[output_mask] = (
                        collected.get(output_mask, oracle.ZERO)
                        + cross_sign * wedge_sign * left_coefficient * right_coefficient
                    )
            value = oracle.Exterior.from_terms(collected)
        result = result + value
    return result


def apply_measure(value: Any, measure: str) -> Any:
    zero = oracle.BispinorMomentum(
        "0", ((oracle.ZERO, oracle.ZERO), (oracle.ZERO, oracle.ZERO))
    )
    operators = oracle.flat_operators(zero)
    if measure == "LOCAL_OPERATOR_INSERTION":
        return value
    if measure == "E_PLUS_CHIRAL":
        return oracle.chiral_measure(value, operators)
    if measure == "E_MINUS_ANTICHIRAL":
        return oracle.antichiral_measure(value, operators)
    raise ValueError(f"undeclared measure {measure}")


def serialize_polynomial(value: Any) -> list[dict[str, Any]]:
    return value.to_json()


def serialize_evaluation(value: Any) -> dict[str, Any]:
    if isinstance(value, oracle.Exterior):
        return {"type": "Exterior", "terms": value.to_json()}
    if isinstance(value, oracle.Poly):
        return {"type": "Poly", "terms": value.to_json()}
    raise TypeError(type(value))


def selected_grammar_terms(grammar: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    families = {
        "I2": grammar["insertions"]["I2"],
        "I3": grammar["insertions"]["I3"],
        "S3_PLUS": grammar["gauge_action_vertices"]["S3_PLUS"],
        "S3_MINUS": grammar["gauge_action_vertices"]["S3_MINUS"],
        "S4_PLUS": grammar["gauge_action_vertices"]["S4_PLUS"],
        "S4_MINUS": grammar["gauge_action_vertices"]["S4_MINUS"],
    }
    terms = {term["term_id"]: term for family in SELECTED_FAMILIES for term in families[family]}
    if len(terms) != 22:
        raise AssertionError(f"selected grammar term count is {len(terms)}, not 22")
    return terms


def grammar_ast_hashes(term: Mapping[str, Any]) -> tuple[str, str]:
    return digest(term["expression_ast"]), digest(term["color_ast"])


def _graph_map(graphir: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {graph["graph_id"]: graph for graph in graphir["literal_direct_graphs"]}


def edge_covariance_templates(graphir: Mapping[str, Any]) -> list[dict[str, Any]]:
    templates: list[dict[str, Any]] = []
    for graph in graphir["literal_direct_graphs"]:
        for orientation in ("direct", "reflected"):
            for edge in graph["orientations"][orientation]["edges"]:
                routing = tuple(edge["momentum_vector"])
                templates.append(
                    {
                        "graph_id": graph["graph_id"],
                        "graph_hash": graph["graph_hash"],
                        "orientation": orientation,
                        "orientation_hash": graph["orientations"][orientation][
                            "orientation_hash"
                        ],
                        "edge_id": edge["edge_id"],
                        "source": edge["source"],
                        "target": edge["target"],
                        "routing_momentum": edge["momentum"],
                        "routing_vector": list(routing),
                        "source_all_incoming_vector": list(routing),
                        "target_all_incoming_vector": list(vector_scale(-1, routing)),
                        "coefficient_basis_entry_rule": "hbar*(-2*g^2)*(-1)^|s|*M_inverse[s,t]/r^2",
                        "coefficient_kernel": "LEFT_ORDERED_H_INVERSE",
                        "coefficient_endpoint_order": "SOURCE_THEN_TARGET",
                        "operator_identity_16_as_coefficient_covariance": "REJECTED",
                    }
                )
    return templates


def _vertex(graph: Mapping[str, Any], vertex_id: str) -> Mapping[str, Any]:
    return next(vertex for vertex in graph["vertices"] if vertex["vertex_id"] == vertex_id)


def _binding_records(
    option: Mapping[str, Any],
    amplitude: Mapping[str, Any],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for attachment in option["quantum_attachment"]:
        sign = 1 if attachment["orientation_endpoint"] == "source" else -1
        vector = vector_scale(sign, attachment["momentum_vector"])
        records.append(
            {
                "grammar_port_id": attachment["grammar_port_id"],
                "role": "QUANTUM_EDGE_ENDPOINT",
                "topology_port_id": attachment["topology_port_id"],
                "edge_id": attachment["edge_id"],
                "orientation_endpoint": attachment["orientation_endpoint"],
                "edge_routing_vector": attachment["momentum_vector"],
                "all_incoming_leaf_momentum_vector": list(vector),
                "all_incoming_leaf_momentum": render_vector(vector),
            }
        )
    candidate_id = option["background_projection"].get("projection_candidate_id")
    if candidate_id is not None:
        candidate = amplitude["projection_candidate_dictionary"][candidate_id]
        for projection in candidate["background_port_projections"]:
            vector = tuple(projection["external_momentum_vector"])
            records.append(
                {
                    "grammar_port_id": projection["grammar_port_id"],
                    "role": "BACKGROUND_EXTERNAL_ENDPOINT",
                    "topology_port_id": projection["topology_port_id"],
                    "edge_id": None,
                    "orientation_endpoint": "EXTERNAL_INCOMING",
                    "edge_routing_vector": None,
                    "all_incoming_leaf_momentum_vector": list(vector),
                    "all_incoming_leaf_momentum": render_vector(vector),
                }
            )
    return sorted(records, key=lambda item: item["grammar_port_id"])


def _conservation_record(
    graph: Mapping[str, Any], vertex_id: str, bindings: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    vertex = _vertex(graph, vertex_id)
    leaf_sum = vector_add(
        *(tuple(binding["all_incoming_leaf_momentum_vector"]) for binding in bindings)
    )
    injection_sum = vector_add(
        *(
            tuple(injection["momentum_vector"])
            for injection in vertex["momentum_injections"]
            if injection["kind"] == "COMPOSITE_SOURCE_MOMENTUM"
        )
    )
    total = vector_add(leaf_sum, injection_sum)
    relation_multiple: int | None = None
    if total == (0, 0, 0, 0, 0):
        relation_multiple = 0
    elif total[0] == total[1] == 0 and total[2] == total[3] == total[4]:
        relation_multiple = total[2]
    passed = relation_multiple is not None
    return {
        "leaf_sum_vector": list(leaf_sum),
        "injection_sum_vector": list(injection_sum),
        "raw_total_vector": list(total),
        "raw_total": render_vector(total),
        "relation": "P+p1+p2=0",
        "relation_multiple": relation_multiple,
        "passed": passed,
    }


def build_tensor_programs(
    grammar: Mapping[str, Any],
    graphir: Mapping[str, Any],
    amplitude: Mapping[str, Any],
) -> dict[str, Any]:
    terms = selected_grammar_terms(grammar)
    graphs = _graph_map(graphir)
    if set(terms) != set(amplitude["term_dictionary"]):
        raise AssertionError("AmplitudeIR selected term dictionary differs from grammar")
    compiled_terms: dict[str, Any] = {}
    for term_id, term in sorted(terms.items()):
        expression_hash, color_hash = grammar_ast_hashes(term)
        source = amplitude["term_dictionary"][term_id]
        if expression_hash != source["expression_ast_sha256"]:
            raise AssertionError(f"expression AST hash mismatch for {term_id}")
        if color_hash != source["color_ast_sha256"]:
            raise AssertionError(f"color AST hash mismatch for {term_id}")
        ops: set[str] = set()

        def walk(node: Mapping[str, Any]) -> None:
            ops.add(str(node["op"]))
            for child in node.get("args", []):
                walk(child)

        walk(term["expression_ast"])
        undeclared = ops - set(SUPPORTED_OPS)
        if undeclared:
            raise AssertionError(f"unsupported AST ops {undeclared}")
        compiled_terms[term_id] = {
            "term_id": term_id,
            "family": term["family"],
            "measure": term["measure"],
            "coefficient_raw": term["coefficient"],
            "port_order": [port["port_id"] for port in term["ports"]],
            "port_count": len(term["ports"]),
            "expression_ast": term["expression_ast"],
            "expression_ast_sha256": expression_hash,
            "color_ast": term["color_ast"],
            "color_ast_sha256": color_hash,
            "ops": sorted(ops),
            "bracket_semantics": "ORDERED_SUPERSPACE_PRODUCT_WITH_SEPARATE_C_TENSOR_NO_SECOND_I",
        }
    parent_records: list[dict[str, Any]] = []
    option_programs: dict[str, Any] = {}
    for parent in amplitude["parents"]:
        graph = graphs[parent["graph_id"]]
        option_ids: list[str] = []
        for vertex_id in parent["vertex_order"]:
            for option in parent["local_amplitude_option_catalog"][vertex_id]:
                term = compiled_terms[option["source_term_id"]]
                local_hash = option["local_amplitude_option_sha256"]
                if digest({key: value for key, value in option.items() if key != "local_amplitude_option_sha256"}) != local_hash:
                    raise AssertionError("local AmplitudeIR option hash mismatch")
                if option["expression_ast_sha256"] != term["expression_ast_sha256"]:
                    raise AssertionError("local option expression hash mismatch")
                if option["color_ast_sha256"] != term["color_ast_sha256"]:
                    raise AssertionError("local option color hash mismatch")
                if option["measure"] != term["measure"]:
                    raise AssertionError("local option measure mismatch")
                bindings = _binding_records(option, amplitude)
                bound_ports = [binding["grammar_port_id"] for binding in bindings]
                if sorted(bound_ports) != sorted(term["port_order"]):
                    raise AssertionError(
                        f"bound ports differ from full AST ports for {option['local_amplitude_option_id']}"
                    )
                if len(bound_ports) != len(set(bound_ports)):
                    raise AssertionError("a grammar port was bound more than once")
                conservation = _conservation_record(graph, vertex_id, bindings)
                if not conservation["passed"]:
                    raise AssertionError(
                        "all-incoming leaf momenta violate vertex conservation for "
                        f"{option['local_amplitude_option_id']}: {conservation}"
                    )
                program_core = {
                    "local_amplitude_option_id": option["local_amplitude_option_id"],
                    "local_amplitude_option_sha256": local_hash,
                    "graph_id": parent["graph_id"],
                    "graph_hash": parent["graph_hash"],
                    "orientation": parent["orientation"],
                    "orientation_hash": parent["orientation_hash"],
                    "vertex_id": vertex_id,
                    "term_id": option["source_term_id"],
                    "expression_ast_sha256": term["expression_ast_sha256"],
                    "color_ast_sha256": term["color_ast_sha256"],
                    "measure": term["measure"],
                    "port_order": term["port_order"],
                    "bindings": bindings,
                    "vertex_conservation": conservation,
                    "tensor_materialization": "FACTORIZED_AST_REQUESTED_BASIS_EVALUATOR_ONLY",
                }
                program_hash = digest(program_core)
                program = dict(program_core)
                program["tensor_program_sha256"] = program_hash
                program_id = f"TP::{option['local_amplitude_option_id']}::{program_hash[:16]}"
                program["tensor_program_id"] = program_id
                if program_id in option_programs:
                    raise AssertionError("duplicate tensor program id")
                option_programs[program_id] = program
                option_ids.append(program_id)
        parent_records.append(
            {
                "graph_id": parent["graph_id"],
                "orientation": parent["orientation"],
                "parent_amplitude_sha256": parent["parent_amplitude_sha256"],
                "local_option_count": len(option_ids),
                "tensor_program_ids": option_ids,
                "all_local_options_compiled": len(option_ids)
                == sum(parent["local_option_counts"].values()),
            }
        )
    return {
        "compiled_terms": compiled_terms,
        "parents": parent_records,
        "option_programs": option_programs,
        "compiled_term_count": len(compiled_terms),
        "parent_count": len(parent_records),
        "local_option_program_count": len(option_programs),
    }


def _program_leaves(
    program: Mapping[str, Any], basis_indices: Sequence[int]
) -> dict[str, Any]:
    if len(basis_indices) != len(program["port_order"]):
        raise ValueError("basis-index count differs from local tensor rank")
    if any(not isinstance(mask, int) or not 0 <= mask < 16 for mask in basis_indices):
        raise ValueError("basis indices must lie in [0,15]")
    binding_by_port = {binding["grammar_port_id"]: binding for binding in program["bindings"]}
    return {
        port_id: oracle.LabeledLeaf(
            port_id,
            momentum_from_vector(binding_by_port[port_id]["all_incoming_leaf_momentum_vector"]),
            0,
            oracle.Exterior.basis(mask),
        )
        for port_id, mask in zip(program["port_order"], basis_indices)
    }


_EVALUATION_CACHE: dict[tuple[str, tuple[int, ...], str], dict[str, Any]] = {}


def evaluate_tensor_entry(
    term: Mapping[str, Any],
    program: Mapping[str, Any],
    basis_indices: Sequence[int],
    *,
    engine: str = "recursive",
) -> dict[str, Any]:
    key = (program["tensor_program_sha256"], tuple(basis_indices), engine)
    if key in _EVALUATION_CACHE:
        return _EVALUATION_CACHE[key]
    if engine == "recursive":
        derivative_engine = oracle_apply_word
    elif engine == "expanded":
        derivative_engine = explicit_apply_word
    else:
        raise ValueError("engine must be recursive or expanded")
    leaves = _program_leaves(program, basis_indices)
    product_terms = _evaluate_ast_terms(term["expression_ast"], leaves, {}, derivative_engine)
    coefficient_parities_by_label = {
        port_id: coefficient_parity(mask)
        for port_id, mask in zip(program["port_order"], basis_indices)
    }
    unmeasured = evaluate_product_terms(product_terms, coefficient_parities_by_label)
    raw = apply_measure(unmeasured, term["measure"])
    coefficient = parse_qi_polynomial(term["coefficient_raw"])
    if isinstance(raw, oracle.Exterior):
        value = raw.scale(coefficient)
    else:
        value = raw * coefficient
    record = {
        "tensor_program_id": program["tensor_program_id"],
        "basis_indices": list(basis_indices),
        "basis_coefficient_parities": [coefficient_parity(mask) for mask in basis_indices],
        "coefficient_exterior_cross_sign": "INCLUDED_WHEN_COLLECTING_ORDERED_COEFFICIENTS_LEFT",
        "engine": engine,
        "product_term_count_before_exterior_product": len(product_terms),
        "measure": term["measure"],
        "value": serialize_evaluation(value),
    }
    record["entry_sha256"] = digest(record)
    _EVALUATION_CACHE[key] = record
    return record


def _first_program(
    bundle: Mapping[str, Any], family: str
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    terms = bundle["tensor_programs"]["compiled_terms"]
    for program in bundle["tensor_programs"]["option_programs"].values():
        term = terms[program["term_id"]]
        if term["family"] == family:
            return term, program
    raise KeyError(family)


def fixture_indices(family: str) -> tuple[int, ...]:
    # Frozen deterministic entries, chosen only from the local 16-state basis.
    return {
        "I2": (0, 0),
        "S3_PLUS": (0, 0, 15),
        "S3_MINUS": (0, 0, 15),
        "S4_PLUS": (0, 0, 0, 15),
    }[family]


def exact_fixtures(bundle: Mapping[str, Any]) -> list[dict[str, Any]]:
    fixtures: list[dict[str, Any]] = []
    for family in ("I2", "S3_PLUS", "S3_MINUS", "S4_PLUS"):
        term, program = _first_program(bundle, family)
        indices = fixture_indices(family)
        recursive = evaluate_tensor_entry(term, program, indices, engine="recursive")
        expanded = evaluate_tensor_entry(term, program, indices, engine="expanded")
        equal = recursive["value"] == expanded["value"]
        if not equal:
            raise AssertionError(f"recursive and expanded evaluators differ for {family}")
        if family == "I2" and recursive["value"]["type"] != "Exterior":
            raise AssertionError("I2 insertion was incorrectly measured")
        if family != "I2" and recursive["value"]["type"] != "Poly":
            raise AssertionError("action vertex did not apply its measure")
        fixtures.append(
            {
                "family": family,
                "term_id": term["term_id"],
                "tensor_program_id": program["tensor_program_id"],
                "basis_indices": list(indices),
                "recursive_expanded_equal": equal,
                "value": recursive["value"],
                "value_is_nonzero": bool(recursive["value"]["terms"]),
            }
        )
    return fixtures


def component_bracket_regression(grammar: Mapping[str, Any]) -> dict[str, Any]:
    gamma2 = grammar["composites"]["Gamma"][1]
    w2 = grammar["composites"]["W"][1]

    def op_count(node: Mapping[str, Any], op: str) -> int:
        return (1 if node["op"] == op else 0) + sum(
            op_count(child, op) for child in node.get("args", [])
        )

    checks = {
        "Gamma2_coefficient_is_minus_i_over_2": gamma2["coefficient"]["rational"] == "-1/2"
        and gamma2["coefficient"]["i_power_reduced"] == 1,
        "W2_coefficient_is_plus_i_over_16": w2["coefficient"]["rational"] == "1/16"
        and w2["coefficient"]["i_power_reduced"] == 1,
        "Gamma2_one_component_bracket": op_count(gamma2["expression_ast"], "AdjointBracket") == 1,
        "W2_one_component_bracket": op_count(w2["expression_ast"], "AdjointBracket") == 1,
        "Gamma2_two_ordered_V_leaves": op_count(gamma2["expression_ast"], "V") == 2,
        "W2_two_ordered_V_leaves": op_count(w2["expression_ast"], "V") == 2,
    }
    if not all(checks.values()):
        raise AssertionError("Gamma2/W2 component-bracket regression failed")
    return {
        "component_rule": "[Y,Z]^C=i*c[A,B,C]*Y^A*Z^B",
        "superspace_interpretation": "ONE_ORDERED_PRODUCT_NO_FORWARD_MINUS_REVERSE",
        "Gamma2_component_ordered_product_count": 1,
        "W2_component_ordered_product_count": 1,
        "forward_minus_reverse_product_count": "REJECTED_WOULD_INCORRECTLY_BE_2",
        "coefficient_i_is_already_in_Qi_record": True,
        "checks": checks,
    }


def build_bundle(root: Path = ROOT) -> dict[str, Any]:
    grammar = load_json(root / GRAMMAR.relative_to(ROOT))
    graphir = load_json(root / GRAPHIR.relative_to(ROOT))
    amplitude = load_json(root / AMPLITUDE.relative_to(ROOT))
    pairing = coefficient_pairing_matrix()
    inverse = invert_fraction_matrix(pairing)
    left_product = multiply_fraction_matrices(pairing, inverse)
    right_product = multiply_fraction_matrices(inverse, pairing)
    identity = identity_fraction_matrix()
    delta = normalized_difference_delta_coefficients()
    coefficient_hessian = left_ordered_coefficient_hessian(pairing)
    coefficient_hessian_inverse = invert_fraction_matrix(coefficient_hessian)
    signed_inverse_formula = left_ordered_covariance_core(inverse)
    reconstructed_delta = reconstruct_delta_from_left_ordered_covariance(
        coefficient_hessian_inverse
    )
    if left_product != identity or right_product != identity:
        raise AssertionError("coefficient metric inversion failed")
    if inverse != delta:
        raise AssertionError("M inverse differs from normalized difference delta")
    if coefficient_hessian_inverse != signed_inverse_formula:
        raise AssertionError("left-ordered coefficient Hessian inverse has wrong sign")
    if multiply_fraction_matrices(coefficient_hessian, coefficient_hessian_inverse) != identity:
        raise AssertionError("left-ordered coefficient Hessian inverse failed on the right")
    if multiply_fraction_matrices(coefficient_hessian_inverse, coefficient_hessian) != identity:
        raise AssertionError("left-ordered coefficient Hessian inverse failed on the left")
    if reconstructed_delta != delta:
        raise AssertionError("coefficient/exterior reconstruction did not recover delta")
    tensor_programs = build_tensor_programs(grammar, graphir, amplitude)
    covariance_templates = edge_covariance_templates(graphir)
    bundle: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "authority_role": "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "inputs": {
            "grammar": {"path": str(GRAMMAR.relative_to(ROOT)), "sha256": file_sha256(GRAMMAR)},
            "graphir": {"path": str(GRAPHIR.relative_to(ROOT)), "sha256": file_sha256(GRAPHIR)},
            "amplitude_ir": {"path": str(AMPLITUDE.relative_to(ROOT)), "sha256": file_sha256(AMPLITUDE)},
            "grassmann_oracle": {"path": str(ORACLE.relative_to(ROOT)), "sha256": file_sha256(ORACLE)},
        },
        "basis": {
            "generator_order": list(oracle.GENERATOR_ORDER),
            "monomial_order": list(range(16)),
            "e_s": "ordered product of generators whose bits occur in s",
            "coefficient_parity": "|v_s|=degree(e_s) mod 2",
            "superfield_evenness": "|v_s*e_s|=0 mod 2",
            "coefficient_exterior_collection": "(v_s*e_s)(v_t*e_t)=(-1)^(|v_t|*degree(e_s))*v_s*v_t*e_s*e_t",
            "coefficient_order": "GRAMMAR_FACTOR_ORDER_NO_COEFFICIENT_REORDERING",
        },
        "coefficient_metric": {
            "definition": "M[s,t]=full_measure(e_s*e_t) at total momentum zero",
            "M": fraction_matrix_json(pairing),
            "M_inverse": fraction_matrix_json(inverse),
            "M_times_M_inverse": fraction_matrix_json(left_product),
            "M_inverse_times_M": fraction_matrix_json(right_product),
            "identity_16": fraction_matrix_json(identity),
            "nonzero_M_entries": sum(value != 0 for row in pairing for value in row),
            "nonzero_M_inverse_entries": sum(value != 0 for row in inverse for value in row),
            "operator_identity_16_is_not_coefficient_metric_inverse": inverse != identity,
            "left_ordered_coefficient_H": fraction_matrix_json(coefficient_hessian),
            "left_ordered_coefficient_H_inverse": fraction_matrix_json(
                coefficient_hessian_inverse
            ),
            "H_times_H_inverse": fraction_matrix_json(
                multiply_fraction_matrices(coefficient_hessian, coefficient_hessian_inverse)
            ),
            "H_inverse_times_H": fraction_matrix_json(
                multiply_fraction_matrices(coefficient_hessian_inverse, coefficient_hessian)
            ),
            "H_definition": "H[s,t]=(-1)^(|s||t|)*M[s,t] in left coefficient order",
            "H_inverse_formula": "H_inverse[s,t]=(-1)^|s|*M_inverse[s,t] on the complementary support",
        },
        "normalized_difference_delta": {
            "generator_order": [
                *oracle.GENERATOR_ORDER,
                *(f"{name}_prime" for name in oracle.GENERATOR_ORDER),
            ],
            "formula": "-4*product_i(theta_i-theta_i_prime)",
            "coefficient_matrix": fraction_matrix_json(delta),
            "coefficient_matrix_equals_M_inverse": delta == inverse,
            "reproducing_identity": "sum_t DeltaCoeff[s,t]*M[t,u]=delta[s,u]",
            "reconstructed_from_left_ordered_coefficient_covariance": fraction_matrix_json(
                reconstructed_delta
            ),
            "coefficient_exterior_reconstruction_equals_delta": reconstructed_delta == delta,
        },
        "spinor_expansion": {
            "epsilon_upper_nonzero": {"+-": "1", "-+": "-1"},
            "undotted": "F^+=F_-; F^-=-F_+",
            "dotted": "F^dot+=F_dot-; F^dot-=-F_dot+",
        },
        "component_bracket_regression": component_bracket_regression(grammar),
        "tensor_programs": tensor_programs,
        "edge_covariance": {
            "rule": "hbar*(-2*g^2)*(-1)^|s|*M_inverse[s,t]/r^2",
            "coefficient_kernel": "LEFT_ORDERED_H_INVERSE",
            "ordinary_exterior_delta_kernel": "M_inverse",
            "operator_kernel": "identity_16_only_before_coefficient-basis inversion",
            "identity_16_as_coefficient_covariance": "REJECTED",
            "bare_M_inverse_as_left_ordered_coefficient_covariance": "REJECTED_MISSING_ORDERING_SIGN",
            "sample_nonzero_entries": [
                edge_covariance_entry(source, 15 ^ source, inverse)
                for source in (0, 1, 3, 7, 15)
            ],
            "per_oriented_parent_edge_templates": covariance_templates,
            "per_oriented_parent_edge_template_count": len(covariance_templates),
            "graded_global_join": "BLOCKED_COEFFICIENT_WICK_PERMUTATION_NOT_DERIVED",
        },
        "fail_closed": {
            "five_edge_global_tensor_contraction": "BLOCKED_NOT_PERFORMED",
            "global_coefficient_koszul_sign": "BLOCKED_NOT_DERIVED",
            "DRED": "BLOCKED_NOT_PERFORMED",
            "IBP": "BLOCKED_NOT_PERFORMED",
            "UV_pole": "BLOCKED_NOT_PERFORMED",
            "renormalized_two_loop_coefficient": None,
        },
    }
    bundle["fixtures"] = exact_fixtures(bundle)
    payload_for_hash = dict(bundle)
    bundle["payload_sha256"] = digest(payload_for_hash)
    return bundle


def audit_bundle(bundle: Mapping[str, Any]) -> dict[str, Any]:
    metric = bundle["coefficient_metric"]
    programs = bundle["tensor_programs"]
    checks = {
        "pairing_is_16_by_16": len(metric["M"]) == 16
        and all(len(row) == 16 for row in metric["M"]),
        "pairing_inverse_is_two_sided": metric["M_times_M_inverse"] == metric["identity_16"]
        and metric["M_inverse_times_M"] == metric["identity_16"],
        "delta_coefficients_equal_metric_inverse": bundle["normalized_difference_delta"][
            "coefficient_matrix_equals_M_inverse"
        ],
        "left_ordered_H_inverse_is_two_sided": metric["H_times_H_inverse"]
        == metric["identity_16"]
        and metric["H_inverse_times_H"] == metric["identity_16"],
        "coefficient_exterior_reconstruction_recovers_delta": bundle[
            "normalized_difference_delta"
        ]["coefficient_exterior_reconstruction_equals_delta"],
        "metric_inverse_not_operator_identity": metric[
            "operator_identity_16_is_not_coefficient_metric_inverse"
        ],
        "selected_22_terms_compiled": programs["compiled_term_count"] == 22,
        "six_oriented_parents_compiled": programs["parent_count"] == 6,
        "all_1048_local_options_compiled": programs["local_option_program_count"] == 1048,
        "all_parent_counts_close": all(
            parent["all_local_options_compiled"] for parent in programs["parents"]
        ),
        "all_vertex_conservation_checks_pass": all(
            program["vertex_conservation"]["passed"]
            for program in programs["option_programs"].values()
        ),
        "all_fixture_evaluators_agree": all(
            fixture["recursive_expanded_equal"] for fixture in bundle["fixtures"]
        ),
        "I2_fixture_retains_Exterior": bundle["fixtures"][0]["value"]["type"] == "Exterior",
        "action_fixtures_apply_measure": all(
            fixture["value"]["type"] == "Poly" for fixture in bundle["fixtures"][1:]
        ),
        "component_bracket_checks_pass": all(
            bundle["component_bracket_regression"]["checks"].values()
        ),
        "local_coefficient_exterior_cross_sign_locked": bundle["basis"][
            "coefficient_exterior_collection"
        ]
        == "(v_s*e_s)(v_t*e_t)=(-1)^(|v_t|*degree(e_s))*v_s*v_t*e_s*e_t",
        "coefficient_covariance_uses_metric_inverse": bundle["edge_covariance"][
            "coefficient_kernel"
        ]
        == "LEFT_ORDERED_H_INVERSE",
        "all_30_oriented_edge_covariances_instantiated": bundle["edge_covariance"][
            "per_oriented_parent_edge_template_count"
        ]
        == 30,
        "edge_endpoint_momenta_are_opposite": all(
            tuple(template["target_all_incoming_vector"])
            == tuple(-value for value in template["source_all_incoming_vector"])
            for template in bundle["edge_covariance"]["per_oriented_parent_edge_templates"]
        ),
        "global_contraction_remains_blocked": bundle["fail_closed"][
            "five_edge_global_tensor_contraction"
        ]
        == "BLOCKED_NOT_PERFORMED",
        "no_two_loop_coefficient_claim": bundle["fail_closed"][
            "renormalized_two_loop_coefficient"
        ]
        is None,
    }
    return {
        "schema": "step6.coefficient_tensor_program_ir.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "payload_sha256": bundle["payload_sha256"],
        "check_count": len(checks),
        "passed_count": sum(checks.values()),
        "checks": checks,
        "remaining_boundary": [
            "GLOBAL_FIVE_EDGE_TENSOR_CONTRACTION",
            "GLOBAL_COEFFICIENT_WICK_KOSZUL_SIGN",
            "DRED",
            "IBP",
            "UV_POLE",
            "RENORMALIZED_TWO_LOOP_COEFFICIENT",
        ],
    }


def render_markdown(bundle: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    fixtures = bundle["fixtures"]
    return "\n".join(
        [
            "# Step 6 coefficient-space TensorProgramIR",
            "",
            f"Status: `{bundle['status']}`.",
            "",
            "## Coefficient metric",
            "",
            "$$",
            "M_{st}:=[e_s e_t]_{D},\\qquad",
            "\\sum_tM_{st}(M^{-1})_{tu}=\\delta_{su},",
            "$$",
            "",
            "$$",
            "\\Delta^4(\\theta-\\theta')=-4\\prod_{i=0}^{3}(\\theta_i-\\theta'_i)",
            "=\\sum_{s,t}(M^{-1})_{st}e_s(\\theta)e_t(\\theta').",
            "$$",
            "",
            "$$",
            "\\langle v_s(r)v_t(-r)\\rangle",
            "=\\hbar\\frac{-2g^2}{r^2}(-1)^{|s|}(M^{-1})_{st}.",
            "$$",
            "",
            "`identity_16` is the operator identity; it is not `M_inverse`.",
            "",
            "$$",
            "V=\\sum_{s=0}^{15}v_s e_s,\\qquad |v_s|=\\deg(e_s)\\pmod 2,",
            "$$",
            "",
            "$$",
            "(v_s e_s)(v_t e_t)=(-1)^{|v_t|\\deg(e_s)}v_sv_t e_se_t.",
            "$$",
            "",
            "$$",
            "H_{st}=(-1)^{|s||t|}M_{st},\\qquad",
            "(H^{-1})_{st}=(-1)^{|s|}(M^{-1})_{st}",
            "\\quad(M^{-1}_{st}\\ne0).",
            "$$",
            "",
            "$$",
            "[Y,Z]^C=i\\,c[A,B,C]Y^A Z^B:",
            "\\quad\\text{superspace AST}=Y^A Z^B,",
            "$$",
            "",
            "The `i` is already contained in the exact Q(i) grammar coefficient.",
            "",
            "## Exact local compilation",
            "",
            f"- grammar terms: `{bundle['tensor_programs']['compiled_term_count']}`",
            f"- oriented parents: `{bundle['tensor_programs']['parent_count']}`",
            f"- local TensorProgram references: `{bundle['tensor_programs']['local_option_program_count']}`",
            "- materialization: `FACTORIZED_AST_REQUESTED_BASIS_EVALUATOR_ONLY`",
            "",
            "## Fixtures",
            "",
            *[
                f"- `{fixture['family']}` `{fixture['basis_indices']}`: recursive=expanded, "
                f"type `{fixture['value']['type']}`, nonzero `{fixture['value_is_nonzero']}`"
                for fixture in fixtures
            ],
            "",
            "## Boundary",
            "",
            "$$",
            "\\text{five-edge contraction}=\\texttt{BLOCKED\\_NOT\\_PERFORMED},\\qquad",
            "C_{2\\text{-loop}}=\\varnothing.",
            "$$",
            "",
            f"Audit: `{audit['passed_count']}/{audit['check_count']}` checks pass.",
            "",
        ]
    )


def write_outputs(root: Path = ROOT) -> tuple[dict[str, Any], dict[str, Any]]:
    bundle = build_bundle(root)
    audit = audit_bundle(bundle)
    output_dir = root / OUTPUT_DIR.relative_to(ROOT)
    output_dir.mkdir(parents=True, exist_ok=True)
    (root / OUTPUT_JSON.relative_to(ROOT)).write_text(
        json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (root / OUTPUT_MD.relative_to(ROOT)).write_text(
        render_markdown(bundle, audit), encoding="utf-8"
    )
    (root / AUDIT.relative_to(ROOT)).write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return bundle, audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    bundle, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "checks": f"{audit['passed_count']}/{audit['check_count']}",
                "terms": bundle["tensor_programs"]["compiled_term_count"],
                "parents": bundle["tensor_programs"]["parent_count"],
                "local_programs": bundle["tensor_programs"]["local_option_program_count"],
                "payload_sha256": bundle["payload_sha256"],
            },
            sort_keys=True,
        )
    )
    if args.check and audit["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
