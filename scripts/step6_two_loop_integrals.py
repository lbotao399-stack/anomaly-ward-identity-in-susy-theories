#!/usr/bin/env python3
"""Proposal-only two-loop integral-family and exact IBP contracts.

Only the decorated literal ``K4_MINUS_ONE_EDGE`` parents emitted by
``step6_two_loop_graphir`` enter this layer.  The module derives denominator
quadratic forms and formal integration-by-parts identities.  It deliberately
does not reduce an integral, select master integrals, evaluate a Laurent
series, or infer a pole or coefficient while the compiled DWord numerator is
absent.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:
    from scripts.step6_two_loop_graphir import build_bundle as build_graph_bundle
    from scripts.step6_two_loop_forest import build_forest_bundle
except ModuleNotFoundError:  # direct ``python scripts/...`` execution
    from step6_two_loop_graphir import build_bundle as build_graph_bundle
    from step6_two_loop_forest import build_forest_bundle


SCHEMA_VERSION = "step6.two_loop_integrals.v1"
STAGE = "PROPOSAL_ONLY_INTEGRAL_FAMILY_AND_IBP_CONTRACT"
INTERNAL_SCALAR_BASIS = ("k2", "l2", "kl", "kp1", "kp2", "lp1", "lp2")
EXTERNAL_INVARIANT_BASIS = ("p1sq", "p2sq", "p1p2")
SCALAR_BASIS = INTERNAL_SCALAR_BASIS + EXTERNAL_INVARIANT_BASIS
ROUTED_VECTOR_BASIS = ("k", "l", "p1", "p2")
LOOP_VECTORS = ("k", "l")
IBP_DOT_VECTORS = ("k", "l", "p1", "p2")
DIMENSION = "d=4-2*epsilon"
TWO_LOOP_MEASURE = "mu^(4*epsilon) d^d k/(2*pi)^d d^d l/(2*pi)^d"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _fraction_ir(value: Fraction | int) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def _fraction_from_ir(value: Mapping[str, Any]) -> Fraction:
    numerator = value.get("numerator")
    denominator = value.get("denominator")
    if not isinstance(numerator, int) or isinstance(numerator, bool):
        raise ValueError("polynomial coefficients require an integer numerator")
    if not isinstance(denominator, int) or isinstance(denominator, bool) or denominator <= 0:
        raise ValueError("polynomial coefficients require a positive integer denominator")
    return Fraction(numerator, denominator)


def _fraction_text(value: Fraction | int) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def rref(matrix: Sequence[Sequence[int | Fraction]]) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    """Return exact reduced row echelon form and pivot columns."""

    if not matrix:
        return [], ()
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("all matrix rows must have the same width")
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(width):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [
                rows[row][index] - factor * rows[pivot_row][index]
                for index in range(width)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, tuple(pivots)


def _serialize_matrix(matrix: Sequence[Sequence[Fraction]]) -> list[list[dict[str, int]]]:
    return [[_fraction_ir(entry) for entry in row] for row in matrix]


def reduce_routing_after_P(momentum_vector: Sequence[int]) -> tuple[int, int, int, int]:
    """Apply exactly ``P=-p1-p2`` to the GraphIR basis ``(k,l,P,p1,p2)``."""

    if len(momentum_vector) != 5:
        raise ValueError("GraphIR routed momenta must use (k,l,P,p1,p2)")
    k, l, source, p1, p2 = (int(entry) for entry in momentum_vector)
    return k, l, p1 - source, p2 - source


def canonical_square_vector(vector: Sequence[int]) -> tuple[int, ...]:
    vector = tuple(int(entry) for entry in vector)
    for entry in vector:
        if entry > 0:
            return vector
        if entry < 0:
            return tuple(-item for item in vector)
    raise ValueError("a denominator cannot have zero routed momentum")


def quadratic_form_row(vector: Sequence[int]) -> tuple[int, ...]:
    """Expand ``(a k+b l+c p1+e p2)^2`` in ``SCALAR_BASIS``."""

    a, b, c, e = canonical_square_vector(vector)
    return (
        a * a,
        b * b,
        2 * a * b,
        2 * a * c,
        2 * a * e,
        2 * b * c,
        2 * b * e,
        c * c,
        e * e,
        2 * c * e,
    )


def _poly_from_dict(terms: Mapping[tuple[int, ...], Fraction]) -> dict[str, Any]:
    cleaned = {
        tuple(int(power) for power in powers): Fraction(coefficient)
        for powers, coefficient in terms.items()
        if coefficient
    }
    for powers in cleaned:
        if len(powers) != len(SCALAR_BASIS) or any(power < 0 for power in powers):
            raise ValueError("a polynomial term requires nonnegative powers in SCALAR_BASIS")
    records = [
        {
            "coefficient": _fraction_ir(cleaned[powers]),
            "powers": {
                variable: power
                for variable, power in zip(SCALAR_BASIS, powers)
                if power
            },
            "power_vector": list(powers),
        }
        for powers in sorted(cleaned, reverse=True)
    ]
    payload = {
        "op": "polynomial",
        "variable_order": list(SCALAR_BASIS),
        "coefficient_domain": "Q_NO_EPSILON",
        "terms": records,
    }
    payload["polynomial_hash"] = digest(payload)
    return payload


def _poly_to_dict(polynomial: Mapping[str, Any]) -> dict[tuple[int, ...], Fraction]:
    if polynomial.get("op") != "polynomial":
        raise ValueError("numerator AST must have op=polynomial")
    if tuple(polynomial.get("variable_order", ())) != SCALAR_BASIS:
        raise ValueError("numerator AST variable order does not match SCALAR_BASIS")
    if polynomial.get("coefficient_domain") != "Q_NO_EPSILON":
        raise ValueError("bare numerator coefficients must lie in Q with no epsilon")
    terms: dict[tuple[int, ...], Fraction] = {}
    for term in polynomial.get("terms", ()):
        powers = tuple(term.get("power_vector", ()))
        if len(powers) != len(SCALAR_BASIS):
            raise ValueError("invalid numerator power vector length")
        if any(not isinstance(power, int) or isinstance(power, bool) or power < 0 for power in powers):
            raise ValueError("numerator powers must be nonnegative integers")
        declared = {
            variable: power
            for variable, power in zip(SCALAR_BASIS, powers)
            if power
        }
        if term.get("powers") != declared:
            raise ValueError("named powers and power vector disagree")
        coefficient = _fraction_from_ir(term.get("coefficient", {}))
        terms[powers] = terms.get(powers, Fraction(0)) + coefficient
    normalized = _poly_from_dict(terms)
    expected_hash = polynomial.get("polynomial_hash")
    if expected_hash is not None and expected_hash != normalized["polynomial_hash"]:
        raise ValueError("numerator polynomial hash is not canonical")
    return {powers: coefficient for powers, coefficient in terms.items() if coefficient}


def polynomial(terms: Iterable[tuple[Fraction | int, Mapping[str, int]]]) -> dict[str, Any]:
    """Construct a canonical rational polynomial with no epsilon coefficients."""

    collected: dict[tuple[int, ...], Fraction] = {}
    for coefficient, named_powers in terms:
        unknown = set(named_powers) - set(SCALAR_BASIS)
        if unknown:
            raise ValueError(f"unknown scalar-product variables: {sorted(unknown)}")
        powers: list[int] = []
        for variable in SCALAR_BASIS:
            power = named_powers.get(variable, 0)
            if not isinstance(power, int) or isinstance(power, bool) or power < 0:
                raise ValueError("polynomial powers must be nonnegative integers")
            powers.append(power)
        key = tuple(powers)
        collected[key] = collected.get(key, Fraction(0)) + Fraction(coefficient)
    return _poly_from_dict(collected)


def zero_polynomial() -> dict[str, Any]:
    return _poly_from_dict({})


def constant_polynomial(value: Fraction | int) -> dict[str, Any]:
    return polynomial(((value, {}),))


def variable_polynomial(variable: str, coefficient: Fraction | int = 1) -> dict[str, Any]:
    return polynomial(((coefficient, {variable: 1}),))


def add_polynomials(*polynomials: Mapping[str, Any]) -> dict[str, Any]:
    output: dict[tuple[int, ...], Fraction] = {}
    for item in polynomials:
        for powers, coefficient in _poly_to_dict(item).items():
            output[powers] = output.get(powers, Fraction(0)) + coefficient
    return _poly_from_dict(output)


def scale_polynomial(polynomial_ast: Mapping[str, Any], coefficient: Fraction | int) -> dict[str, Any]:
    coefficient = Fraction(coefficient)
    return _poly_from_dict(
        {powers: coefficient * value for powers, value in _poly_to_dict(polynomial_ast).items()}
    )


def multiply_polynomials(
    left: Mapping[str, Any], right: Mapping[str, Any]
) -> dict[str, Any]:
    output: dict[tuple[int, ...], Fraction] = {}
    for left_powers, left_coefficient in _poly_to_dict(left).items():
        for right_powers, right_coefficient in _poly_to_dict(right).items():
            powers = tuple(a + b for a, b in zip(left_powers, right_powers))
            output[powers] = output.get(powers, Fraction(0)) + left_coefficient * right_coefficient
    return _poly_from_dict(output)


def polynomial_is_zero(polynomial_ast: Mapping[str, Any]) -> bool:
    return not _poly_to_dict(polynomial_ast)


def tensor_polynomial(
    terms: Iterable[tuple[Mapping[str, Any], Sequence[tuple[str, str]]]],
    *,
    free_indices: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Construct an exact free-index tensor polynomial over scalar polynomials.

    Each factor ``(vector,index)`` denotes a routed hat-space vector component.
    Contracted loop-vector pairs belong in ``SCALAR_BASIS`` instead; tensor
    indices here are therefore required to be distinct and free.
    """

    collected: dict[tuple[tuple[str, str], ...], dict[str, Any]] = {}
    index_signature: tuple[str, ...] | None = (
        tuple(str(index) for index in free_indices) if free_indices is not None else None
    )
    if index_signature is not None and (
        any(not index for index in index_signature)
        or len(index_signature) != len(set(index_signature))
    ):
        raise ValueError("declared tensor free indices must be nonempty and distinct")
    for scalar_polynomial, tensor_word in terms:
        _poly_to_dict(scalar_polynomial)
        word = tuple((str(vector), str(index)) for vector, index in tensor_word)
        if any(vector not in ROUTED_VECTOR_BASIS for vector, _ in word):
            raise ValueError("tensor numerator vectors must lie in (k,l,p1,p2)")
        indices = [index for _, index in word]
        if any(not index for index in indices) or len(indices) != len(set(indices)):
            raise ValueError("tensor numerator indices must be nonempty and free")
        if index_signature is None:
            index_signature = tuple(indices)
        elif tuple(indices) != index_signature:
            raise ValueError("every tensor-polynomial term must have the same ordered free indices")
        if word in collected:
            collected[word] = add_polynomials(collected[word], scalar_polynomial)
        else:
            collected[word] = _poly_from_dict(_poly_to_dict(scalar_polynomial))
    records = [
        {
            "tensor_word": [
                {
                    "vector": vector,
                    "index": index,
                    "index_space": "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE",
                    "metric_type": "hat_delta",
                }
                for vector, index in word
            ],
            "scalar_polynomial": collected[word],
        }
        for word in sorted(collected)
        if not polynomial_is_zero(collected[word])
    ]
    free_indices = list(index_signature or ())
    payload = {
        "op": "tensor_polynomial",
        "coefficient_domain": "Q_NO_EPSILON",
        "scalar_variable_order": list(SCALAR_BASIS),
        "tensor_vector_basis": list(ROUTED_VECTOR_BASIS),
        "free_index_space": "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE",
        "free_indices": free_indices,
        "terms": records,
    }
    payload["tensor_polynomial_hash"] = digest(payload)
    return payload


def _tensor_to_dict(
    numerator_ast: Mapping[str, Any],
) -> dict[tuple[tuple[str, str], ...], dict[str, Any]]:
    if numerator_ast.get("op") != "tensor_polynomial":
        raise ValueError("tensor numerator AST must have op=tensor_polynomial")
    if numerator_ast.get("coefficient_domain") != "Q_NO_EPSILON":
        raise ValueError("tensor numerator coefficients must lie in Q with no epsilon")
    if tuple(numerator_ast.get("scalar_variable_order", ())) != SCALAR_BASIS:
        raise ValueError("tensor numerator scalar basis mismatch")
    if tuple(numerator_ast.get("tensor_vector_basis", ())) != ROUTED_VECTOR_BASIS:
        raise ValueError("tensor numerator routed-vector basis mismatch")
    output: dict[tuple[tuple[str, str], ...], dict[str, Any]] = {}
    index_signature: tuple[str, ...] | None = None
    for record in numerator_ast.get("terms", ()):
        word: list[tuple[str, str]] = []
        for factor in record.get("tensor_word", ()):
            if factor.get("index_space") != "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE":
                raise ValueError("tensor numerator index-space type mismatch")
            if factor.get("metric_type") != "hat_delta":
                raise ValueError("tensor numerator metric type must remain hat_delta")
            vector = factor.get("vector")
            index = factor.get("index")
            if vector not in ROUTED_VECTOR_BASIS or not isinstance(index, str) or not index:
                raise ValueError("invalid tensor numerator vector or index")
            word.append((vector, index))
        if len({index for _, index in word}) != len(word):
            raise ValueError("tensor numerator indices must be free and distinct")
        indices = tuple(index for _, index in word)
        if index_signature is None:
            index_signature = indices
        elif indices != index_signature:
            raise ValueError("tensor numerator terms have incompatible free-index signatures")
        scalar = record.get("scalar_polynomial", {})
        _poly_to_dict(scalar)
        key = tuple(word)
        output[key] = add_polynomials(output[key], scalar) if key in output else scalar
    normalized = tensor_polynomial(
        ((scalar, word) for word, scalar in output.items()),
        free_indices=numerator_ast.get("free_indices", ()),
    )
    if numerator_ast.get("free_indices") != list(index_signature or ()):
        raise ValueError("tensor numerator free-index declaration mismatch")
    if numerator_ast.get("tensor_polynomial_hash") != normalized["tensor_polynomial_hash"]:
        raise ValueError("tensor numerator hash is not canonical")
    return {word: scalar for word, scalar in output.items() if not polynomial_is_zero(scalar)}


def numerator_hash(numerator_ast: Mapping[str, Any]) -> str:
    if numerator_ast.get("op") == "polynomial":
        _poly_to_dict(numerator_ast)
        return str(numerator_ast["polynomial_hash"])
    if numerator_ast.get("op") == "tensor_polynomial":
        _tensor_to_dict(numerator_ast)
        return str(numerator_ast["tensor_polynomial_hash"])
    raise ValueError("numerator must be a scalar or tensor polynomial AST")


def numerator_is_zero(numerator_ast: Mapping[str, Any]) -> bool:
    if numerator_ast.get("op") == "polynomial":
        return polynomial_is_zero(numerator_ast)
    return not _tensor_to_dict(numerator_ast)


def multiply_numerator_by_polynomial(
    numerator_ast: Mapping[str, Any], scalar_polynomial: Mapping[str, Any]
) -> dict[str, Any]:
    _poly_to_dict(scalar_polynomial)
    if numerator_ast.get("op") == "polynomial":
        return multiply_polynomials(numerator_ast, scalar_polynomial)
    tensor_terms = _tensor_to_dict(numerator_ast)
    return tensor_polynomial(
        (
            (multiply_polynomials(scalar, scalar_polynomial), word)
            for word, scalar in tensor_terms.items()
        ),
        free_indices=numerator_ast["free_indices"],
    )


def polynomial_from_row(row: Sequence[int]) -> dict[str, Any]:
    if len(row) != len(SCALAR_BASIS):
        raise ValueError("quadratic-form row has wrong width")
    return polynomial(
        (coefficient, {variable: 1})
        for variable, coefficient in zip(SCALAR_BASIS, row)
        if coefficient
    )


def render_polynomial(polynomial_ast: Mapping[str, Any]) -> str:
    terms = _poly_to_dict(polynomial_ast)
    if not terms:
        return "0"
    rendered: list[str] = []
    for powers in sorted(terms, reverse=True):
        coefficient = terms[powers]
        factors = [
            variable if power == 1 else f"{variable}^{power}"
            for variable, power in zip(SCALAR_BASIS, powers)
            if power
        ]
        magnitude = abs(coefficient)
        if factors and magnitude == 1:
            body = "*".join(factors)
        elif factors:
            body = f"{_fraction_text(magnitude)}*" + "*".join(factors)
        else:
            body = _fraction_text(magnitude)
        if not rendered:
            rendered.append(body if coefficient > 0 else f"-{body}")
        else:
            rendered.append(("+" if coefficient > 0 else "-") + body)
    return "".join(rendered)


_DOT_VARIABLE = {
    frozenset(("k",)): "k2",
    frozenset(("l",)): "l2",
    frozenset(("p1",)): "p1sq",
    frozenset(("p2",)): "p2sq",
    frozenset(("k", "l")): "kl",
    frozenset(("k", "p1")): "kp1",
    frozenset(("k", "p2")): "kp2",
    frozenset(("l", "p1")): "lp1",
    frozenset(("l", "p2")): "lp2",
    frozenset(("p1", "p2")): "p1p2",
}


def dot_polynomial(left: str, right: str) -> dict[str, Any]:
    if left not in ROUTED_VECTOR_BASIS or right not in ROUTED_VECTOR_BASIS:
        raise ValueError("dot-product vectors must lie in (k,l,p1,p2)")
    return variable_polynomial(_DOT_VARIABLE[frozenset((left, right))])


def derivation_kernel(derivative_loop: str, dot_vector: str) -> dict[str, dict[str, Any]]:
    """Give ``dot_vector . partial_derivative_loop`` on every scalar generator."""

    if derivative_loop not in LOOP_VECTORS or dot_vector not in IBP_DOT_VECTORS:
        raise ValueError("invalid standard IBP generator")
    kernel = {variable: zero_polynomial() for variable in SCALAR_BASIS}
    if derivative_loop == "k":
        kernel["k2"] = scale_polynomial(dot_polynomial("k", dot_vector), 2)
        kernel["kl"] = dot_polynomial("l", dot_vector)
        kernel["kp1"] = dot_polynomial("p1", dot_vector)
        kernel["kp2"] = dot_polynomial("p2", dot_vector)
    else:
        kernel["l2"] = scale_polynomial(dot_polynomial("l", dot_vector), 2)
        kernel["kl"] = dot_polynomial("k", dot_vector)
        kernel["lp1"] = dot_polynomial("p1", dot_vector)
        kernel["lp2"] = dot_polynomial("p2", dot_vector)
    return kernel


def directional_derivative_polynomial(
    polynomial_ast: Mapping[str, Any], derivative_loop: str, dot_vector: str
) -> dict[str, Any]:
    """Apply an exact standard IBP derivation using Leibniz on the polynomial AST."""

    source = _poly_to_dict(polynomial_ast)
    kernel = derivation_kernel(derivative_loop, dot_vector)
    output = zero_polynomial()
    for powers, coefficient in source.items():
        for index, exponent in enumerate(powers):
            if exponent == 0 or polynomial_is_zero(kernel[SCALAR_BASIS[index]]):
                continue
            reduced = list(powers)
            reduced[index] -= 1
            base = _poly_from_dict({tuple(reduced): coefficient * exponent})
            output = add_polynomials(
                output,
                multiply_polynomials(base, kernel[SCALAR_BASIS[index]]),
            )
    return output


def directional_derivative_numerator(
    numerator_ast: Mapping[str, Any], derivative_loop: str, dot_vector: str
) -> dict[str, Any]:
    """Differentiate either a scalar polynomial or a free-index tensor polynomial."""

    if numerator_ast.get("op") == "polynomial":
        return directional_derivative_polynomial(numerator_ast, derivative_loop, dot_vector)
    source = _tensor_to_dict(numerator_ast)
    output_terms: list[tuple[Mapping[str, Any], Sequence[tuple[str, str]]]] = []
    for word, scalar in source.items():
        scalar_derivative = directional_derivative_polynomial(
            scalar, derivative_loop, dot_vector
        )
        if not polynomial_is_zero(scalar_derivative):
            output_terms.append((scalar_derivative, word))
        for index, (vector, free_index) in enumerate(word):
            if vector != derivative_loop:
                continue
            differentiated_word = list(word)
            differentiated_word[index] = (dot_vector, free_index)
            output_terms.append((scalar, differentiated_word))
    return tensor_polynomial(output_terms, free_indices=numerator_ast["free_indices"])


def direct_denominator_derivative(
    routed_vector: Sequence[int], derivative_loop: str, dot_vector: str
) -> dict[str, Any]:
    """Compute ``v . partial_q (r^2)=2 coefficient(q,r) (v.r)`` directly."""

    routed = canonical_square_vector(routed_vector)
    q_index = ROUTED_VECTOR_BASIS.index(derivative_loop)
    q_coefficient = routed[q_index]
    if q_coefficient == 0:
        return zero_polynomial()
    v_dot_r = zero_polynomial()
    for vector, coefficient in zip(ROUTED_VECTOR_BASIS, routed):
        if coefficient:
            v_dot_r = add_polynomials(
                v_dot_r,
                scale_polynomial(dot_polynomial(dot_vector, vector), coefficient),
            )
    return scale_polynomial(v_dot_r, 2 * q_coefficient)


def build_denominator_record(edge: Mapping[str, Any]) -> dict[str, Any]:
    reduced = canonical_square_vector(reduce_routing_after_P(edge["momentum_vector"]))
    row = quadratic_form_row(reduced)
    polynomial_ast = polynomial_from_row(row)
    record = {
        "denominator_id": f"D_{edge['edge_id']}",
        "edge_id": str(edge["edge_id"]),
        "source_routing_basis": ["k", "l", "P", "p1", "p2"],
        "source_routing_vector": [int(entry) for entry in edge["momentum_vector"]],
        "source_routing_rendered": edge["momentum"],
        "substitution": "P=-p1-p2",
        "reduced_routing_basis": list(ROUTED_VECTOR_BASIS),
        "reduced_routing_vector": list(reduced),
        "square_metric": "hat_delta",
        "quadratic_form_basis": list(SCALAR_BASIS),
        "quadratic_form_row": list(row),
        "loop_scalar_row": list(row[: len(INTERNAL_SCALAR_BASIS)]),
        "external_invariant_row": list(row[len(INTERNAL_SCALAR_BASIS) :]),
        "quadratic_form_polynomial": polynomial_ast,
        "quadratic_form_rendered": render_polynomial(polynomial_ast),
    }
    record["denominator_hash"] = digest(record)
    return record


def enumerate_sectors(edge_order: Sequence[str]) -> list[dict[str, Any]]:
    """Enumerate power sectors only; no graph-connectivity statement is made."""

    edge_order = tuple(str(edge) for edge in edge_order)
    sectors: list[dict[str, Any]] = []
    for bits in product((0, 1), repeat=len(edge_order)):
        active = [edge for edge, bit in zip(edge_order, bits) if bit]
        pinched = [edge for edge, bit in zip(edge_order, bits) if not bit]
        bit_text = "".join(str(bit) for bit in bits)
        pinch_text = "".join(str(1 - bit) for bit in bits)
        record = {
            "sector_id": f"SECTOR_{bit_text}",
            "pinch_id": f"PINCH_{pinch_text}",
            "edge_order": list(edge_order),
            "sector_bits": list(bits),
            "active_edge_ids": active,
            "pinched_edge_ids": pinched,
            "power_domain": {
                "active": "a_e>0",
                "pinched": "a_e<=0",
                "all_a_e": "Z",
            },
            "graph_connectivity_status": "NOT_EVALUATED_BY_INTEGRAL_SECTOR_ENUMERATION",
            "zero_scale_status": "NOT_EVALUATED_REQUIRES_NUMERATOR_AND_IR_DOMAIN",
        }
        record["sector_hash"] = digest(record)
        sectors.append(record)
    return sectors


def _power_symbols(edge_order: Sequence[str]) -> list[dict[str, str]]:
    return [
        {"edge_id": edge_id, "symbol": f"a[{edge_id}]", "domain": "Z"}
        for edge_id in edge_order
    ]


def instantiate_ibp_identity(
    family: Mapping[str, Any],
    derivative_loop: str,
    dot_vector: str,
    numerator_ast: Mapping[str, Any],
) -> dict[str, Any]:
    """Instantiate the exact IBP identity for any accepted polynomial numerator AST."""

    input_numerator_hash = numerator_hash(numerator_ast)
    edge_order = tuple(family["edge_order"])
    denominators = list(family["denominators"])
    generator_id = f"IBP_d{derivative_loop}_dot_{dot_vector}"
    zero_shift = {edge_id: 0 for edge_id in edge_order}
    terms: list[dict[str, Any]] = []
    if derivative_loop == dot_vector:
        terms.append(
            {
                "term_role": "VECTOR_DIVERGENCE",
                "coefficient_ast": {"op": "dimension_symbol", "symbol": "d"},
                "power_shift": zero_shift,
                "numerator_ast": numerator_ast,
            }
        )
    numerator_derivative = directional_derivative_numerator(
        numerator_ast, derivative_loop, dot_vector
    )
    if not numerator_is_zero(numerator_derivative):
        terms.append(
            {
                "term_role": "NUMERATOR_DIRECTIONAL_DERIVATIVE",
                "coefficient_ast": {"op": "rational", "value": _fraction_ir(1)},
                "power_shift": zero_shift,
                "numerator_ast": numerator_derivative,
            }
        )
    for denominator in denominators:
        derivative = directional_derivative_polynomial(
            denominator["quadratic_form_polynomial"], derivative_loop, dot_vector
        )
        if polynomial_is_zero(derivative):
            continue
        direct = direct_denominator_derivative(
            denominator["reduced_routing_vector"], derivative_loop, dot_vector
        )
        if derivative["polynomial_hash"] != direct["polynomial_hash"]:
            raise AssertionError("quadratic-form and routed-vector denominator derivatives disagree")
        edge_id = denominator["edge_id"]
        shift = dict(zero_shift)
        shift[edge_id] = 1
        terms.append(
            {
                "term_role": "DENOMINATOR_LOG_DERIVATIVE",
                "edge_id": edge_id,
                "coefficient_ast": {
                    "op": "negative_power_symbol",
                    "symbol": f"a[{edge_id}]",
                },
                "power_shift": shift,
                "numerator_ast": multiply_numerator_by_polynomial(numerator_ast, derivative),
                "denominator_directional_derivative": derivative,
            }
        )
    identity = {
        "schema_version": "step6.ibp_identity_ir.v1",
        "generator_id": generator_id,
        "operator": f"partial/{derivative_loop} dot {dot_vector}",
        "general_propagator_powers": _power_symbols(edge_order),
        "general_power_domain": "Z^number_of_denominators",
        "input_numerator_ast_kind": numerator_ast["op"],
        "input_numerator_hash": input_numerator_hash,
        "equation": {
            "op": "equals_zero",
            "left": {"op": "sum_of_shifted_integrals", "terms": terms},
            "right": {"op": "integer", "value": 0},
        },
        "surface_term_contract": (
            "DRED_ANALYTIC_CONTINUATION_FORMAL_IBP; MASTER_EVALUATION_REQUIRES_IR_DOMAIN"
        ),
    }
    identity["identity_hash"] = digest(identity)
    return identity


def validation_numerator() -> dict[str, Any]:
    return polynomial(
        (
            (1, {"k2": 2, "kl": 1}),
            (Fraction(3, 2), {"kp1": 1, "lp2": 1}),
            (-1, {"p1p2": 1}),
        )
    )


def build_ibp_generators(family: Mapping[str, Any]) -> list[dict[str, Any]]:
    numerator = validation_numerator()
    generators: list[dict[str, Any]] = []
    for derivative_loop in LOOP_VECTORS:
        for dot_vector in IBP_DOT_VECTORS:
            generator_id = f"IBP_d{derivative_loop}_dot_{dot_vector}"
            kernel = derivation_kernel(derivative_loop, dot_vector)
            derivatives: list[dict[str, Any]] = []
            for denominator in family["denominators"]:
                by_polynomial = directional_derivative_polynomial(
                    denominator["quadratic_form_polynomial"], derivative_loop, dot_vector
                )
                by_routing = direct_denominator_derivative(
                    denominator["reduced_routing_vector"], derivative_loop, dot_vector
                )
                derivatives.append(
                    {
                        "edge_id": denominator["edge_id"],
                        "by_quadratic_form": by_polynomial,
                        "by_routed_vector": by_routing,
                        "exact_match": by_polynomial["polynomial_hash"]
                        == by_routing["polynomial_hash"],
                    }
                )
            record = {
                "generator_id": generator_id,
                "derivative_loop": derivative_loop,
                "dot_vector": dot_vector,
                "vector_divergence": "d" if derivative_loop == dot_vector else "0",
                "derivation_on_scalar_generators": kernel,
                "leibniz_rule": "delta_v(FG)=delta_v(F)G+F delta_v(G)",
                "denominator_directional_derivatives": derivatives,
                "general_identity": (
                    "0=(partial_q dot v) I[a;N]+I[a;delta_(q,v)N]"
                    "-sum_e a[e] I[a+unit_e;(delta_(q,v)D_e)N]"
                ),
                "general_power_domain": "a[e] in Z",
                "polynomial_numerator_schema": "step6.rational_scalar_polynomial.v1",
                "validation_numerator_role": "ALGEBRA_FIXTURE_NOT_PHYSICAL_DWORD_NUMERATOR",
                "validation_identity": instantiate_ibp_identity(
                    family, derivative_loop, dot_vector, numerator
                ),
            }
            record["generator_hash"] = digest(record)
            generators.append(record)
    return generators


def external_kinematic_domain() -> dict[str, Any]:
    p_squared = polynomial(
        ((1, {"p1sq": 1}), (1, {"p2sq": 1}), (2, {"p1p2": 1}))
    )
    gram = polynomial(
        ((1, {"p1sq": 1, "p2sq": 1}), (-1, {"p1p2": 2}))
    )
    return {
        "signature": "EUCLIDEAN",
        "all_incoming_relation": "P+p1+p2=0",
        "invariant_basis": list(EXTERNAL_INVARIANT_BASIS),
        "definitions": {
            "p1sq": "hat_delta(p1,p1)",
            "p2sq": "hat_delta(p2,p2)",
            "p1p2": "hat_delta(p1,p2)",
            "Psq": p_squared,
            "Gram_p1_p2": gram,
        },
        "generic_off_shell_domain": [
            "p1sq>0",
            "p2sq>0",
            "Psq=p1sq+p2sq+2*p1p2>0",
            "Gram_p1_p2=p1sq*p2sq-p1p2^2>0",
        ],
        "domain_status": "SYMBOLIC_DOMAIN_SPECIFIED_NOT_NUMERICALLY_INSTANTIATED",
        "ir_pole_status": "UNKNOWN_UNTIL_MASTER_INTEGRALS_AND_ALL_PINCHES_ARE_EVALUATED",
        "forbidden_inference": "OFF_SHELL_SYMBOLS_ALONE_DO_NOT_PROVE_ABSENCE_OF_EVERY_IR_POLE",
    }


def dred_integral_contract() -> dict[str, Any]:
    return {
        "dimension": DIMENSION,
        "measure": {
            "two_loop": TWO_LOOP_MEASURE,
            "mu_power": "mu^(4*epsilon)",
            "loop_order": 2,
        },
        "metric_types": {
            "spin_dalgebra_metric": "delta_(4)",
            "loop_integral_metric": "hat_delta",
            "evanescent_metric": "tilde_delta=delta_(4)-hat_delta",
            "pairwise_distinct_types": True,
            "traces": {
                "tr_delta_(4)": "4",
                "tr_hat_delta": "d=4-2*epsilon",
                "tr_tilde_delta": "2*epsilon",
            },
        },
        "scalar_product_metric": "hat_delta",
        "bare_numerator_coefficient_domain": "Q_NO_EPSILON",
        "bare_numerator_epsilon_status": "FORBIDDEN",
        "dimension_symbol_location": (
            "IBP_VECTOR_DIVERGENCE_AND_POST_INTEGRATION_TENSOR_REDUCTION_ONLY"
        ),
        "no_metric_identification": [
            "delta_(4) != hat_delta",
            "tilde_delta != scalar 2*epsilon",
            "no bare epsilon factor is inserted into a DWord numerator",
        ],
    }


def ibp_certificate_schema() -> dict[str, Any]:
    schema = {
        "schema_id": "step6.ibp_certificate_ir.v1",
        "required_fields": [
            "source_graph_id",
            "source_graph_hash",
            "integral_family_id",
            "integral_family_hash",
            "compiled_dword_numerator",
            "ibp_generator_hashes",
            "gates",
            "outputs",
        ],
        "gate_order": [
            "DENOMINATOR_FAMILY_CERTIFIED",
            "COMPILED_DWORD_NUMERATOR_PRESENT",
            "NUMERATOR_TO_SCALAR_POLYNOMIAL_CERTIFIED",
            "SECTOR_AND_BOUNDARY_IDENTITIES_CERTIFIED",
            "MASTER_BASIS_CERTIFIED",
            "MASTER_REDUCTION_CERTIFIED",
            "UV_AND_IR_LAURENT_DEPTH_CERTIFIED",
            "R_COMPLETE_POLE_CANCELLATION_CERTIFIED",
        ],
        "current_required_fail_closed_reason": "COMPILED_DWORD_NUMERATOR_ABSENT",
    }
    schema["schema_hash"] = digest(schema)
    return schema


def build_integral_family(
    graph: Mapping[str, Any], forest_record: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    if graph.get("classification") != "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT":
        raise ValueError("the integral-family layer accepts only literal decorated direct parents")
    if graph.get("topology") != "K4_MINUS_ONE_EDGE":
        raise ValueError("source graph topology is not K4_MINUS_ONE_EDGE")
    denominators = [build_denominator_record(edge) for edge in graph["internal_edges"]]
    edge_order = [denominator["edge_id"] for denominator in denominators]
    loop_matrix = [denominator["loop_scalar_row"] for denominator in denominators]
    augmented_matrix = [denominator["quadratic_form_row"] for denominator in denominators]
    loop_rref, loop_pivots = rref(loop_matrix)
    augmented_rref, augmented_pivots = rref(augmented_matrix)
    free_columns = [
        index for index in range(len(INTERNAL_SCALAR_BASIS)) if index not in loop_pivots
    ]
    family = {
        "schema_version": "step6.integral_family_ir.v1",
        "stage": STAGE,
        "source_graph_id": graph["graph_id"],
        "source_graph_hash": graph["graph_hash"],
        "source_graph_classification": graph["classification"],
        "source_forest_record_hash": (
            forest_record["record_hash"] if forest_record is not None else None
        ),
        "source_forest_status": (
            forest_record["renormalization_ast"]["status"]
            if forest_record is not None
            else "BLOCKED_FOREST_RECORD_NOT_BOUND"
        ),
        "integral_family_id": f"IF_{graph['graph_id']}",
        "substitution": "P=-p1-p2",
        "loop_momenta": list(LOOP_VECTORS),
        "independent_external_momenta": ["p1", "p2"],
        "internal_scalar_basis": list(INTERNAL_SCALAR_BASIS),
        "external_invariant_basis": list(EXTERNAL_INVARIANT_BASIS),
        "scalar_basis": list(SCALAR_BASIS),
        "edge_order": edge_order,
        "denominators": denominators,
        "rank_certificate": {
            "loop_scalar_matrix": loop_matrix,
            "loop_scalar_rref": _serialize_matrix(loop_rref),
            "loop_scalar_rank": len(loop_pivots),
            "loop_scalar_pivot_columns": list(loop_pivots),
            "loop_scalar_pivot_variables": [INTERNAL_SCALAR_BASIS[index] for index in loop_pivots],
            "augmented_matrix_rank": len(augmented_pivots),
            "augmented_pivot_columns": list(augmented_pivots),
            "independent_loop_scalar_product_count": len(INTERNAL_SCALAR_BASIS),
            "isp_count": len(free_columns),
            "canonical_free_isp_columns": free_columns,
            "canonical_free_isp_variables": [INTERNAL_SCALAR_BASIS[index] for index in free_columns],
            "identity": (
                f"{len(INTERNAL_SCALAR_BASIS)}={len(loop_pivots)}+{len(free_columns)}"
            ),
        },
        "general_integral": {
            "symbol": f"I_{graph['graph_id']}[a;N]",
            "definition": (
                "mu^(4*epsilon) integral d^d k/(2*pi)^d d^d l/(2*pi)^d "
                "N(k,l,p1,p2) product_e D_e^(-a[e])"
            ),
            "power_symbols": _power_symbols(edge_order),
            "power_domain": "Z^number_of_denominators",
            "numerator_schemas": [
                "step6.rational_scalar_polynomial.v1",
                "step6.rational_tensor_polynomial.v1",
            ],
            "physical_numerator_status": "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
        },
        "sectors": enumerate_sectors(edge_order),
    }
    family["ibp_generators"] = build_ibp_generators(family)
    family["integral_family_hash"] = digest(
        {key: value for key, value in family.items() if key != "integral_family_hash"}
    )
    return family


def build_ibp_certificate(family: Mapping[str, Any]) -> dict[str, Any]:
    certificate = {
        "schema_version": "step6.ibp_certificate_ir.v1",
        "source_graph_id": family["source_graph_id"],
        "source_graph_hash": family["source_graph_hash"],
        "source_forest_record_hash": family["source_forest_record_hash"],
        "integral_family_id": family["integral_family_id"],
        "integral_family_hash": family["integral_family_hash"],
        "compiled_dword_numerator": {
            "status": "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
            "dword_hash": None,
            "scalar_polynomial_ast": None,
            "bare_epsilon_factor": None,
        },
        "ibp_generator_hashes": [
            generator["generator_hash"] for generator in family["ibp_generators"]
        ],
        "gates": {
            "denominator_family": "PASS_EXACT_ROUTING_QUADRATIC_FORMS_RANK_AND_ISP",
            "compiled_dword_numerator": "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
            "numerator_to_scalar_polynomial": "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
            "sector_and_boundary_identities": (
                "BLOCKED_PHYSICAL_NUMERATOR_SECTOR_AND_PINCH_SUPPORT_UNKNOWN"
            ),
            "master_basis": "BLOCKED_NO_PHYSICAL_IBP_SYSTEM_OR_BOUNDARY_CONDITIONS",
            "master_reduction": "BLOCKED_MASTER_BASIS_AND_COMPILED_NUMERATOR_ABSENT",
            "laurent_depth": (
                "BLOCKED_MASTER_UV_IR_DEPTH_AND_FOREST_COUNTERTERMS_UNEVALUATED"
            ),
            "forest_counterterms": family["source_forest_status"],
            "r_complete_pole_cancellation": "BLOCKED_REDUCTION_AND_FOREST_INPUTS_ABSENT",
        },
        "master_laurent_contract": {
            "master_integral_ids": None,
            "reduction_coefficients": None,
            "required_uv_laurent_depth": None,
            "required_ir_laurent_depth": None,
            "maximum_pole_order": None,
            "finite_remainder": None,
            "status": "UNCOMPUTED_FAIL_CLOSED",
        },
        "outputs": {
            "reduced_integral": None,
            "master_basis": None,
            "uv_pole": None,
            "ir_pole": None,
            "r_complete_integral": None,
            "renormalized_coefficient": None,
        },
        "acceptance_rule": (
            "NO_REDUCTION_POLE_OR_COEFFICIENT_BEFORE_COMPILED_DWORD_NUMERATOR_HASH_"
            "AND_COMPLETE_IBP_MASTER_LAURENT_CERTIFICATES"
        ),
    }
    certificate["certificate_hash"] = digest(certificate)
    return certificate


def build_integral_bundle() -> dict[str, Any]:
    graph_bundle = build_graph_bundle()
    forest_bundle = build_forest_bundle()
    forest_by_graph_hash = {
        record["source_graph_hash"]: record for record in forest_bundle["graph_records"]
    }
    graphs = [
        graph
        for graph in graph_bundle["literal_direct_graphs"]
        if graph["classification"] == "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT"
        and graph["topology"] == "K4_MINUS_ONE_EDGE"
    ]
    families = [
        build_integral_family(graph, forest_by_graph_hash.get(graph["graph_hash"]))
        for graph in graphs
    ]
    certificates = [build_ibp_certificate(family) for family in families]
    bundle = {
        "schema_version": SCHEMA_VERSION,
        "stage": STAGE,
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "source_graph_bundle_hash": graph_bundle["bundle_hash"],
        "source_forest_bundle_hash": forest_bundle["bundle_hash"],
        "dynamic_graph_selection": {
            "predicate": (
                "classification=LITERAL_K4_MINUS_EDGE_DIRECT_PARENT and "
                "topology=K4_MINUS_ONE_EDGE"
            ),
            "source_graph_count": len(graphs),
            "source_graph_ids": [graph["graph_id"] for graph in graphs],
            "hardcoded_graph_count": False,
        },
        "scalar_product_contract": {
            "internal_basis": list(INTERNAL_SCALAR_BASIS),
            "external_invariant_basis": list(EXTERNAL_INVARIANT_BASIS),
            "total_internal_scalar_products": (
                "L*(L+1)/2+L*E=2*3/2+2*2=7"
            ),
            "substitution": "P=-p1-p2",
        },
        "polynomial_numerator_schema": {
            "schema_id": "step6.rational_scalar_polynomial.v1",
            "variables": list(SCALAR_BASIS),
            "coefficient_domain": "Q_NO_EPSILON",
            "powers": "NONNEGATIVE_INTEGERS",
            "physical_dword_input": None,
        },
        "tensor_numerator_schema": {
            "schema_id": "step6.rational_tensor_polynomial.v1",
            "scalar_coefficients": "step6.rational_scalar_polynomial.v1",
            "tensor_vectors": list(ROUTED_VECTOR_BASIS),
            "free_index_space": "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE",
            "metric_type": "hat_delta",
            "directional_derivative": (
                "delta_(q,v)[r^m F]=(delta_(q,r) v^m)F+r^m delta_(q,v)F"
            ),
            "upstream_spin_dalgebra_indices": (
                "NOT_ACCEPTED_WITHOUT_EXPLICIT_DELTA4_TO_HAT_PROJECTION_COMPILER"
            ),
            "physical_dword_input": None,
        },
        "ibp_certificate_schema": ibp_certificate_schema(),
        "external_kinematic_domain": external_kinematic_domain(),
        "dred_integral_contract": dred_integral_contract(),
        "integral_families": families,
        "ibp_certificates": certificates,
        "external_target_used_as_input": False,
        "global_fail_closed": {
            "compiled_dword_numerator": None,
            "ibp_reduction": None,
            "master_integrals": None,
            "laurent_depth": None,
            "uv_poles": None,
            "ir_poles": None,
            "renormalized_coefficient": None,
            "status": "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
        },
    }
    bundle["bundle_hash"] = digest(
        {key: value for key, value in bundle.items() if key != "bundle_hash"}
    )
    return bundle


def build_audit(
    bundle: Mapping[str, Any], artifact_hashes: Mapping[str, str] | None = None
) -> dict[str, Any]:
    families = list(bundle["integral_families"])
    certificates = list(bundle["ibp_certificates"])
    source_count = bundle["dynamic_graph_selection"]["source_graph_count"]
    metric_values = bundle["dred_integral_contract"]["metric_types"]
    checks = [
        {
            "id": "DYNAMIC_LITERAL_GRAPH_SELECTION_NONEMPTY",
            "passed": source_count > 0 and len(families) == len(certificates) == source_count,
            "evidence": bundle["dynamic_graph_selection"],
        },
        {
            "id": "P_SUBSTITUTION_REMOVES_SOURCE_MOMENTUM",
            "passed": all(
                denominator["substitution"] == "P=-p1-p2"
                and denominator["reduced_routing_basis"] == list(ROUTED_VECTOR_BASIS)
                for family in families
                for denominator in family["denominators"]
            ),
            "evidence": "(k,l,P,p1,p2)->(k,l,p1-P,p2-P)",
        },
        {
            "id": "QUADRATIC_FORMS_EXACT_IN_TEN_COMPONENT_BASIS",
            "passed": all(
                denominator["quadratic_form_row"]
                == list(quadratic_form_row(denominator["reduced_routing_vector"]))
                and len(denominator["quadratic_form_row"]) == len(SCALAR_BASIS)
                for family in families
                for denominator in family["denominators"]
            ),
            "evidence": list(SCALAR_BASIS),
        },
        {
            "id": "RANK_AND_ISP_COUNTS_EXACT",
            "passed": all(
                family["rank_certificate"]["loop_scalar_rank"]
                + family["rank_certificate"]["isp_count"]
                == len(INTERNAL_SCALAR_BASIS)
                and family["rank_certificate"]["loop_scalar_rank"]
                == len(rref(family["rank_certificate"]["loop_scalar_matrix"])[1])
                for family in families
            ),
            "evidence": [
                {
                    "graph_id": family["source_graph_id"],
                    "rank": family["rank_certificate"]["loop_scalar_rank"],
                    "isps": family["rank_certificate"]["isp_count"],
                    "isp_variables": family["rank_certificate"]["canonical_free_isp_variables"],
                }
                for family in families
            ],
        },
        {
            "id": "SECTOR_AND_PINCH_IDS_COMPLETE_WITHOUT_CONNECTIVITY_CLAIM",
            "passed": all(
                len(family["sectors"]) == 2 ** len(family["edge_order"])
                and len({sector["sector_id"] for sector in family["sectors"]})
                == len(family["sectors"])
                and all(
                    sector["graph_connectivity_status"]
                    == "NOT_EVALUATED_BY_INTEGRAL_SECTOR_ENUMERATION"
                    for sector in family["sectors"]
                )
                for family in families
            ),
            "evidence": [
                {
                    "graph_id": family["source_graph_id"],
                    "denominators": len(family["edge_order"]),
                    "sectors": len(family["sectors"]),
                }
                for family in families
            ],
        },
        {
            "id": "EIGHT_STANDARD_IBP_GENERATORS_PER_FAMILY",
            "passed": all(
                {(item["derivative_loop"], item["dot_vector"]) for item in family["ibp_generators"]}
                == set(product(LOOP_VECTORS, IBP_DOT_VECTORS))
                and len(family["ibp_generators"]) == 8
                for family in families
            ),
            "evidence": "{d/dk,d/dl} dot {k,l,p1,p2}",
        },
        {
            "id": "IBP_DENOMINATOR_DERIVATIVES_HAVE_TWO_EXACT_DERIVATIONS",
            "passed": all(
                derivative["exact_match"]
                for family in families
                for generator in family["ibp_generators"]
                for derivative in generator["denominator_directional_derivatives"]
            ),
            "evidence": "Leibniz derivative of quadratic-form AST equals 2*r_q*(v.r)",
        },
        {
            "id": "GENERAL_INTEGER_POWERS_AND_POLYNOMIAL_AST",
            "passed": all(
                generator["general_power_domain"] == "a[e] in Z"
                and generator["validation_identity"]["general_power_domain"]
                == "Z^number_of_denominators"
                and generator["validation_identity"]["input_numerator_hash"]
                == validation_numerator()["polynomial_hash"]
                for family in families
                for generator in family["ibp_generators"]
            ),
            "evidence": "exact rational polynomial Leibniz AST",
        },
        {
            "id": "THREE_METRIC_TYPES_DISTINCT_AND_NO_BARE_EPSILON",
            "passed": (
                metric_values["spin_dalgebra_metric"] == "delta_(4)"
                and metric_values["loop_integral_metric"] == "hat_delta"
                and metric_values["evanescent_metric"]
                == "tilde_delta=delta_(4)-hat_delta"
                and bundle["dred_integral_contract"]["bare_numerator_epsilon_status"]
                == "FORBIDDEN"
            ),
            "evidence": metric_values,
        },
        {
            "id": "TWO_LOOP_DRED_MEASURE_EXACT",
            "passed": bundle["dred_integral_contract"]["measure"]["two_loop"]
            == TWO_LOOP_MEASURE,
            "evidence": bundle["dred_integral_contract"]["measure"],
        },
        {
            "id": "OFF_SHELL_INVARIANTS_DEFINED_WITH_IR_STATUS_UNKNOWN",
            "passed": (
                bundle["external_kinematic_domain"]["definitions"]["Psq"]
                ["polynomial_hash"]
                == external_kinematic_domain()["definitions"]["Psq"]["polynomial_hash"]
                and bundle["external_kinematic_domain"]["definitions"]["Gram_p1_p2"]
                ["polynomial_hash"]
                == external_kinematic_domain()["definitions"]["Gram_p1_p2"]
                ["polynomial_hash"]
                and bundle["external_kinematic_domain"]["ir_pole_status"].startswith("UNKNOWN_")
            ),
            "evidence": bundle["external_kinematic_domain"],
        },
        {
            "id": "IBP_CERTIFICATES_REFUSE_REDUCTION_POLES_AND_COEFFICIENT",
            "passed": all(
                certificate["compiled_dword_numerator"]["status"]
                == "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT"
                and certificate["master_laurent_contract"]["status"]
                == "UNCOMPUTED_FAIL_CLOSED"
                and all(value is None for value in certificate["outputs"].values())
                for certificate in certificates
            )
            and all(value is None for key, value in bundle["global_fail_closed"].items() if key != "status"),
            "evidence": bundle["global_fail_closed"],
        },
        {
            "id": "CERTIFICATE_HASH_BINDINGS_EXACT",
            "passed": all(
                certificate["source_graph_hash"] == family["source_graph_hash"]
                and certificate["source_forest_record_hash"]
                == family["source_forest_record_hash"]
                and family["source_forest_record_hash"] is not None
                and certificate["integral_family_hash"] == family["integral_family_hash"]
                and certificate["ibp_generator_hashes"]
                == [generator["generator_hash"] for generator in family["ibp_generators"]]
                for family, certificate in zip(families, certificates)
            ),
            "evidence": [certificate["certificate_hash"] for certificate in certificates],
        },
        {
            "id": "SCALAR_AND_TENSOR_NUMERATOR_SCHEMAS_ARE_EXACT_AND_TYPED",
            "passed": (
                bundle["polynomial_numerator_schema"]["coefficient_domain"]
                == "Q_NO_EPSILON"
                and bundle["tensor_numerator_schema"]["metric_type"] == "hat_delta"
                and bundle["tensor_numerator_schema"]["free_index_space"]
                == "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE"
                and bundle["tensor_numerator_schema"]["physical_dword_input"] is None
            ),
            "evidence": {
                "scalar": bundle["polynomial_numerator_schema"]["schema_id"],
                "tensor": bundle["tensor_numerator_schema"]["schema_id"],
            },
        },
        {
            "id": "NO_EXTERNAL_TARGET_INPUT",
            "passed": bundle["external_target_used_as_input"] is False,
            "evidence": False,
        },
    ]
    passed = all(check["passed"] for check in checks)
    return {
        "schema_version": "step6.two_loop_integrals.audit.v1",
        "status": "PASS" if passed else "FAIL",
        "dynamic_source_graph_count": source_count,
        "rank_isp_report": [
            {
                "source_graph_id": family["source_graph_id"],
                "denominator_count": len(family["denominators"]),
                "loop_scalar_rank": family["rank_certificate"]["loop_scalar_rank"],
                "isp_count": family["rank_certificate"]["isp_count"],
                "sector_count": len(family["sectors"]),
                "ibp_generator_count": len(family["ibp_generators"]),
            }
            for family in families
        ],
        "checks": checks,
        "artifact_sha256": dict(artifact_hashes or {}),
        "failure_count": sum(not check["passed"] for check in checks),
    }


def render_summary(bundle: Mapping[str, Any]) -> str:
    lines = [
        "# Step 6 two-loop integral families and IBP certificates — proposal only",
        "",
        "$$",
        "P=-p_1-p_2,\\qquad",
        "\\mathcal S=(k^2,l^2,k\\cdot l,k\\cdot p_1,k\\cdot p_2,",
        "l\\cdot p_1,l\\cdot p_2).",
        "$$",
        "",
        "$$",
        "\\int_{k,l}=\\mu^{4\\epsilon}",
        "\\int\\frac{d^d k}{(2\\pi)^d}\\frac{d^d l}{(2\\pi)^d},",
        "\\qquad d=4-2\\epsilon.",
        "$$",
        "",
    ]
    for family in bundle["integral_families"]:
        rank = family["rank_certificate"]
        lines.extend(
            [
                f"## {family['source_graph_id']}",
                "",
                "$$",
                "\\{D_e\\}="
                + "\\{" + ",".join(
                    denominator["quadratic_form_rendered"]
                    for denominator in family["denominators"]
                ) + "\\}.",
                "$$",
                "",
                "$$",
                f"\\operatorname{{rank}}D={rank['loop_scalar_rank']},\\qquad",
                f"N_{{\\mathrm{{ISP}}}}=7-{rank['loop_scalar_rank']}={rank['isp_count']}.",
                "$$",
                "",
                f"Sectors: `{len(family['sectors'])}`; IBP generators: `8`.",
                "",
            ]
        )
    lines.extend(
        [
            "$$",
            "0=\\int_{k,l}\\partial_{q^\\mu}",
            "\\left[v^\\mu N\\prod_eD_e^{-a_e}\\right],",
            "\\qquad q\\in\\{k,l\\},\\quad v\\in\\{k,l,p_1,p_2\\}.",
            "$$",
            "",
            "`BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT`: reduction, masters, Laurent depth, poles, and coefficient are unset.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(root: Path) -> dict[str, Any]:
    bundle = build_integral_bundle()
    generated = root / "generated" / "step6" / "two-loop-integrals"
    generated.mkdir(parents=True, exist_ok=True)
    payloads = {
        "two-loop-integrals.json": bundle,
        "integral-families.json": {
            "schema_version": SCHEMA_VERSION,
            "bundle_hash": bundle["bundle_hash"],
            "integral_family_index": [
                {
                    "source_graph_id": family["source_graph_id"],
                    "source_graph_hash": family["source_graph_hash"],
                    "source_forest_record_hash": family["source_forest_record_hash"],
                    "integral_family_id": family["integral_family_id"],
                    "integral_family_hash": family["integral_family_hash"],
                    "denominator_count": len(family["denominators"]),
                    "loop_scalar_rank": family["rank_certificate"]["loop_scalar_rank"],
                    "isp_count": family["rank_certificate"]["isp_count"],
                    "sector_count": len(family["sectors"]),
                    "ibp_generator_count": len(family["ibp_generators"]),
                    "full_record_location": "two-loop-integrals.json",
                }
                for family in bundle["integral_families"]
            ],
        },
        "ibp-certificates.json": {
            "schema_version": "step6.ibp_certificate_ir.v1",
            "schema": bundle["ibp_certificate_schema"],
            "certificates": bundle["ibp_certificates"],
        },
    }
    artifact_hashes: dict[str, str] = {}
    for filename, payload in payloads.items():
        path = generated / filename
        text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        path.write_text(text, encoding="utf-8")
        artifact_hashes[str(path.relative_to(root))] = sha256(text.encode("utf-8")).hexdigest()
    summary_path = generated / "two-loop-integrals.md"
    summary = render_summary(bundle)
    summary_path.write_text(summary, encoding="utf-8")
    artifact_hashes[str(summary_path.relative_to(root))] = sha256(summary.encode("utf-8")).hexdigest()
    audit = build_audit(bundle, artifact_hashes)
    if audit["status"] != "PASS":
        failed = [check["id"] for check in audit["checks"] if not check["passed"]]
        raise RuntimeError(f"Step-6 integral-family audit failed: {failed}")
    audit_path = root / "audits" / "step6-two-loop-integrals-verification.json"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return {"bundle": bundle, "audit": audit}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    result = write_outputs(root)
    print(
        json.dumps(
            {
                "status": result["audit"]["status"],
                "dynamic_source_graph_count": result["audit"]["dynamic_source_graph_count"],
                "rank_isp_report": result["audit"]["rank_isp_report"],
                "failure_count": result["audit"]["failure_count"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
