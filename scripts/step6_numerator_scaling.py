#!/usr/bin/env python3
"""Exact Step-6 numerator-scaling certificate compiler.

For every repository K4-minus-edge parent, the compiler derives the adapted
loop-scaling subspace from routed edge momenta.  Scalar and free-index tensor
polynomial numerators are then substituted into that adapted basis over the
exact rational polynomial ring.  Like monomials are collected before the
highest surviving scaling degree is read.

The current graph census has no compiled physical D-algebra numerator.  The
certificates emitted here therefore use explicit validation fixtures only and
do not assert an integral, pole, or coefficient.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from hashlib import sha256
from math import gcd
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:
    from scripts import step6_two_loop_forest as forest
    from scripts import step6_two_loop_graphir as graphir
    from scripts import step6_two_loop_integrals as integrals
except ModuleNotFoundError:  # direct execution
    import step6_two_loop_forest as forest
    import step6_two_loop_graphir as graphir
    import step6_two_loop_integrals as integrals


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/numerator-scaling"
GENERATED_JSON = GENERATED_DIR / "numerator-scaling.json"
GENERATED_MD = GENERATED_DIR / "numerator-scaling.md"
AUDIT = ROOT / "audits/step6-numerator-scaling-verification.json"

SCHEMA_VERSION = "step6.numerator_scaling.compiler.v1"
STATUS = "PROPOSAL_ONLY_FIXTURE_NUMERATOR_PHYSICAL_NUMERATOR_UNCONNECTED"
STAGE = "EXACT_SUBGRAPH_ADAPTED_NUMERATOR_SCALING"
LOOP_BASIS = ("k", "l")
VECTOR_BASIS = tuple(integrals.ROUTED_VECTOR_BASIS)
SCALAR_BASIS = tuple(integrals.SCALAR_BASIS)


class NumeratorScalingError(ValueError):
    """Base fail-closed scaling compiler error."""


class ScalingMapError(NumeratorScalingError):
    """Raised when routed momenta do not define the requested adapted basis."""


class NumeratorSubstitutionError(NumeratorScalingError):
    """Raised for a malformed scalar or tensor polynomial substitution."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def fraction_json(value: Fraction | int) -> dict[str, int]:
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def determinant_2(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ScalingMapError("the two-loop adapted matrix must be 2 by 2")
    return Fraction(matrix[0][0]) * Fraction(matrix[1][1]) - Fraction(
        matrix[0][1]
    ) * Fraction(matrix[1][0])


def matrix_json(matrix: Sequence[Sequence[Fraction]]) -> list[list[dict[str, int]]]:
    return [[fraction_json(value) for value in row] for row in matrix]


def primitive_integer_direction(row: Sequence[int]) -> tuple[int, int]:
    if len(row) != 2 or not any(row):
        raise ScalingMapError("one-loop complement constraint must be a nonzero row")
    a, b = map(int, row)
    u = [b, -a]
    divisor = gcd(abs(u[0]), abs(u[1]))
    u = [entry // divisor for entry in u]
    first = next(entry for entry in u if entry)
    if first < 0:
        u = [-entry for entry in u]
    return u[0], u[1]


def loop_row(edge: Mapping[str, Any]) -> tuple[int, int]:
    reduced = integrals.reduce_routing_after_P(edge["momentum_vector"])
    return int(reduced[0]), int(reduced[1])


@dataclass(frozen=True)
class ScalingMap:
    graph_id: str
    graph_hash: str
    subgraph_id: str
    subgraph_hash: str
    subgraph_edge_ids: tuple[str, ...]
    subgraph_loop_count: int
    basis_matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
    derivation: str
    outside_loop_rows: tuple[tuple[int, int], ...] = ()

    def __post_init__(self) -> None:
        if self.subgraph_loop_count not in {1, 2}:
            raise ScalingMapError("this two-loop compiler accepts subgraph loop count 1 or 2")
        if determinant_2(self.basis_matrix) == 0:
            raise ScalingMapError("adapted loop-basis matrix is singular")
        scaled_columns = range(self.subgraph_loop_count)
        for row in self.outside_loop_rows:
            for column in scaled_columns:
                contraction = sum(
                    Fraction(row[component]) * self.basis_matrix[component][column]
                    for component in range(2)
                )
                if contraction:
                    raise ScalingMapError(
                        "outside edge depends on a scaled subgraph loop coordinate"
                    )

    @property
    def adapted_atoms(self) -> tuple[str, str]:
        if self.subgraph_loop_count == 1:
            return "h0", "c0"
        return "h0", "h1"

    @property
    def scaled_atoms(self) -> tuple[str, ...]:
        return self.adapted_atoms[: self.subgraph_loop_count]

    @property
    def fixed_atoms(self) -> tuple[str, ...]:
        return self.adapted_atoms[self.subgraph_loop_count :] + ("p1", "p2")

    def vector_substitution(self) -> dict[str, tuple[tuple[Fraction, int, str], ...]]:
        output: dict[str, tuple[tuple[Fraction, int, str], ...]] = {}
        for row_index, vector in enumerate(LOOP_BASIS):
            terms = []
            for column, atom in enumerate(self.adapted_atoms):
                coefficient = Fraction(self.basis_matrix[row_index][column])
                if coefficient:
                    terms.append(
                        (
                            coefficient,
                            1 if column < self.subgraph_loop_count else 0,
                            atom,
                        )
                    )
            output[vector] = tuple(terms)
        output["p1"] = ((Fraction(1), 0, "p1"),)
        output["p2"] = ((Fraction(1), 0, "p2"),)
        return output

    def as_json(self) -> dict[str, Any]:
        payload = {
            "schema": "step6.subgraph_adapted_scaling_map.v1",
            "graph_id": self.graph_id,
            "graph_hash": self.graph_hash,
            "subgraph_id": self.subgraph_id,
            "subgraph_hash": self.subgraph_hash,
            "subgraph_edge_ids": list(self.subgraph_edge_ids),
            "subgraph_loop_count": self.subgraph_loop_count,
            "original_loop_basis": list(LOOP_BASIS),
            "adapted_basis_atoms": list(self.adapted_atoms),
            "scaled_atoms": list(self.scaled_atoms),
            "fixed_atoms": list(self.fixed_atoms),
            "basis_equation": "(k,l)^T=B*(adapted atoms)^T",
            "basis_matrix_B": matrix_json(self.basis_matrix),
            "determinant_B": fraction_json(determinant_2(self.basis_matrix)),
            "outside_loop_rows": [list(row) for row in self.outside_loop_rows],
            "derivation": self.derivation,
            "scaling_rule": {
                atom: (f"{atom}->t*{atom}" if atom in self.scaled_atoms else f"{atom}->fixed")
                for atom in (*self.adapted_atoms, "p1", "p2")
            },
            "outside_edges_fixed_under_scaling": True,
        }
        payload["scaling_map_hash"] = digest(payload)
        return payload


def graph_subgraph_records(graph: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    records = forest.enumerate_connected_edge_subgraphs(graph)
    named = {
        str(cycle["cycle_id"])
        for cycle in graph["simple_one_loop_cycles"]["cycles"]
    }
    wanted = named | {"full"}
    selected = [
        record
        for record in records
        if str(record["subgraph_id"]) in wanted
        and bool(record["one_particle_irreducible"])
        and int(record["counts"]["L"]) > 0
    ]
    found = {str(record["subgraph_id"]) for record in selected}
    if found != wanted:
        raise ScalingMapError(
            f"named/full subgraph mismatch missing={sorted(wanted-found)} extra={sorted(found-wanted)}"
        )
    return sorted(
        selected,
        key=lambda record: (
            1 if record["subgraph_id"] == "full" else 0,
            str(record["subgraph_id"]),
        ),
    )


def derive_scaling_map(
    graph: Mapping[str, Any], subgraph: Mapping[str, Any]
) -> ScalingMap:
    edge_by_id = {str(edge["edge_id"]): edge for edge in graph["internal_edges"]}
    inside = set(map(str, subgraph["edge_ids"]))
    outside_edges = [edge for edge_id, edge in edge_by_id.items() if edge_id not in inside]
    outside_rows = tuple(loop_row(edge) for edge in outside_edges)
    loops = int(subgraph["counts"]["L"])
    if loops == 2:
        matrix = (
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)),
        )
        derivation = "FULL_TWO_LOOP_SUBSPACE_IDENTITY_BASIS"
    elif loops == 1:
        nonzero_rows = [row for row in outside_rows if any(row)]
        if not nonzero_rows:
            raise ScalingMapError("proper one-loop subgraph has no complement constraint")
        u = primitive_integer_direction(nonzero_rows[0])
        if any(sum(row[i] * u[i] for i in range(2)) for row in nonzero_rows):
            raise ScalingMapError("outside routed rows do not have one common null direction")
        complement = (1, 0) if u[1] != 0 else (0, 1)
        matrix = (
            (Fraction(u[0]), Fraction(complement[0])),
            (Fraction(u[1]), Fraction(complement[1])),
        )
        derivation = "PRIMITIVE_INTEGER_NULL_DIRECTION_OF_OUTSIDE_EDGE_ROUTINGS"
    else:
        raise ScalingMapError("only one- and two-loop 1PI subgraphs are accepted")
    scaling_map = ScalingMap(
        str(graph["graph_id"]),
        str(graph["graph_hash"]),
        str(subgraph["subgraph_id"]),
        str(subgraph["subgraph_hash"]),
        tuple(sorted(inside)),
        loops,
        matrix,
        derivation,
        outside_rows,
    )
    if loops == 1:
        scaled_column = tuple(matrix[row][0] for row in range(2))
        for edge_id in inside:
            row = loop_row(edge_by_id[edge_id])
            if sum(Fraction(row[i]) * scaled_column[i] for i in range(2)) == 0:
                raise ScalingMapError(
                    f"subgraph edge {edge_id} is fixed along its claimed loop direction"
                )
    return scaling_map


def alternative_adapted_basis(scaling_map: ScalingMap) -> ScalingMap:
    B = scaling_map.basis_matrix
    if scaling_map.subgraph_loop_count == 1:
        # h'=2h and c'=c+3h preserve the scaled filtration.
        matrix = (
            (2 * B[0][0], B[0][1] + 3 * B[0][0]),
            (2 * B[1][0], B[1][1] + 3 * B[1][0]),
        )
    else:
        # Both columns scale; any exact GL(2,Q) change is adapted.
        matrix = (
            (B[0][0], B[0][0] + B[0][1]),
            (B[1][0], B[1][0] + B[1][1]),
        )
    return ScalingMap(
        scaling_map.graph_id,
        scaling_map.graph_hash,
        scaling_map.subgraph_id,
        scaling_map.subgraph_hash,
        scaling_map.subgraph_edge_ids,
        scaling_map.subgraph_loop_count,
        matrix,
        "EXACT_ADAPTED_BASIS_CHANGE_FOR_INVARIANCE_AUDIT",
        scaling_map.outside_loop_rows,
    )


@dataclass(frozen=True)
class ExpandedKey:
    t_degree: int
    scalar_factors: tuple[str, ...] = ()
    tensor_word: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.t_degree < 0:
            raise NumeratorSubstitutionError("scaling powers must be nonnegative")


ExpandedPolynomial = dict[ExpandedKey, Fraction]


@dataclass
class CollectionStats:
    emitted_contributions: int = 0
    like_monomial_merges: int = 0
    exact_zero_cancellations: int = 0
    merged_coefficient_updates: int = 0

    def as_json(self) -> dict[str, int]:
        return {
            "emitted_contributions": self.emitted_contributions,
            "like_monomial_merges": self.like_monomial_merges,
            "merged_coefficient_updates": self.merged_coefficient_updates,
            "exact_zero_cancellations": self.exact_zero_cancellations,
        }


def add_expanded_term(
    target: ExpandedPolynomial,
    key: ExpandedKey,
    coefficient: Fraction | int,
    stats: CollectionStats,
) -> None:
    coefficient = Fraction(coefficient)
    if not coefficient:
        return
    stats.emitted_contributions += 1
    if key in target:
        stats.like_monomial_merges += 1
        combined = target[key] + coefficient
        stats.merged_coefficient_updates += 1
        if combined:
            target[key] = combined
        else:
            del target[key]
            stats.exact_zero_cancellations += 1
    else:
        target[key] = coefficient


def multiply_expanded(
    left: Mapping[ExpandedKey, Fraction],
    right: Mapping[ExpandedKey, Fraction],
    stats: CollectionStats,
) -> ExpandedPolynomial:
    output: ExpandedPolynomial = {}
    for left_key, left_coefficient in left.items():
        for right_key, right_coefficient in right.items():
            key = ExpandedKey(
                left_key.t_degree + right_key.t_degree,
                tuple(sorted(left_key.scalar_factors + right_key.scalar_factors)),
                left_key.tensor_word + right_key.tensor_word,
            )
            add_expanded_term(
                output, key, left_coefficient * right_coefficient, stats
            )
    return output


def dot_generator(left: str, right: str) -> str:
    first, second = sorted((left, right))
    return f"dot({first},{second})"


def dot_substitution(
    left: str,
    right: str,
    vector_map: Mapping[str, Sequence[tuple[Fraction, int, str]]],
    stats: CollectionStats,
) -> ExpandedPolynomial:
    if left not in vector_map or right not in vector_map:
        raise NumeratorSubstitutionError("unknown routed vector in dot product")
    output: ExpandedPolynomial = {}
    for left_coefficient, left_degree, left_atom in vector_map[left]:
        for right_coefficient, right_degree, right_atom in vector_map[right]:
            key = ExpandedKey(
                left_degree + right_degree,
                (dot_generator(left_atom, right_atom),),
                (),
            )
            add_expanded_term(
                output,
                key,
                left_coefficient * right_coefficient,
                stats,
            )
    return output


SCALAR_PAIR = {
    "k2": ("k", "k"),
    "l2": ("l", "l"),
    "kl": ("k", "l"),
    "kp1": ("k", "p1"),
    "kp2": ("k", "p2"),
    "lp1": ("l", "p1"),
    "lp2": ("l", "p2"),
    "p1sq": ("p1", "p1"),
    "p2sq": ("p2", "p2"),
    "p1p2": ("p1", "p2"),
}


def substitute_scalar_polynomial(
    polynomial_ast: Mapping[str, Any],
    scaling_map: ScalingMap,
    stats: CollectionStats | None = None,
) -> tuple[ExpandedPolynomial, CollectionStats]:
    stats = stats or CollectionStats()
    try:
        source = integrals._poly_to_dict(polynomial_ast)
    except ValueError as error:
        raise NumeratorSubstitutionError(str(error)) from error
    vector_map = scaling_map.vector_substitution()
    used_variables = {
        variable
        for powers in source
        for variable, power in zip(SCALAR_BASIS, powers)
        if power
    }
    generator_images = {
        variable: dot_substitution(*SCALAR_PAIR[variable], vector_map, stats)
        for variable in used_variables
    }
    output: ExpandedPolynomial = {}
    for powers, coefficient in source.items():
        monomial: ExpandedPolynomial = {ExpandedKey(0): Fraction(coefficient)}
        for variable, power in zip(SCALAR_BASIS, powers):
            for _ in range(power):
                monomial = multiply_expanded(monomial, generator_images[variable], stats)
        for key, value in monomial.items():
            add_expanded_term(output, key, value, stats)
    return output, stats


def substitute_tensor_word(
    word: Sequence[tuple[str, str]],
    scaling_map: ScalingMap,
    stats: CollectionStats,
) -> ExpandedPolynomial:
    vector_map = scaling_map.vector_substitution()
    output: ExpandedPolynomial = {ExpandedKey(0): Fraction(1)}
    for vector, index in word:
        factor: ExpandedPolynomial = {}
        if vector not in vector_map:
            raise NumeratorSubstitutionError("unknown vector in tensor word")
        for coefficient, degree, atom in vector_map[vector]:
            add_expanded_term(
                factor,
                ExpandedKey(degree, (), ((atom, str(index)),)),
                coefficient,
                stats,
            )
        output = multiply_expanded(output, factor, stats)
    return output


def substitute_numerator(
    numerator_ast: Mapping[str, Any], scaling_map: ScalingMap
) -> dict[str, Any]:
    stats = CollectionStats()
    op = numerator_ast.get("op")
    try:
        input_hash = integrals.numerator_hash(numerator_ast)
    except ValueError as error:
        raise NumeratorSubstitutionError(str(error)) from error
    if op == "polynomial":
        expanded, stats = substitute_scalar_polynomial(numerator_ast, scaling_map, stats)
        free_indices: list[str] = []
    elif op == "tensor_polynomial":
        try:
            source = integrals._tensor_to_dict(numerator_ast)
        except ValueError as error:
            raise NumeratorSubstitutionError(str(error)) from error
        expanded = {}
        for word, scalar in source.items():
            scalar_expanded, _ = substitute_scalar_polynomial(scalar, scaling_map, stats)
            tensor_expanded = substitute_tensor_word(word, scaling_map, stats)
            product = multiply_expanded(scalar_expanded, tensor_expanded, stats)
            for key, coefficient in product.items():
                add_expanded_term(expanded, key, coefficient, stats)
        free_indices = list(numerator_ast["free_indices"])
    else:
        raise NumeratorSubstitutionError("numerator must be scalar or tensor polynomial AST")
    terms = expanded_terms_json(expanded)
    rho = max((key.t_degree for key in expanded), default=None)
    leading = [row for row in terms if row["t_degree"] == rho] if rho is not None else []
    payload = {
        "schema": "step6.exact_scaled_numerator.v1",
        "input_numerator_kind": op,
        "input_numerator_hash": input_hash,
        "scaling_map_hash": scaling_map.as_json()["scaling_map_hash"],
        "free_indices": free_indices,
        "coefficient_domain": "Q_NO_EPSILON",
        "substitution_performed_before_degree_readout": True,
        "like_monomials_collected_before_degree_readout": True,
        "expanded_terms": terms,
        "collection_stats": stats.as_json(),
        "rho": rho if rho is not None else "ZERO_NUMERATOR",
        "highest_surviving_t_degree": rho,
        "leading_terms": leading,
        "certificate_status": (
            "EXACT_HIGHEST_HOMOGENEOUS_DEGREE"
            if rho is not None
            else "IDENTICALLY_ZERO_AFTER_EXACT_SUBSTITUTION"
        ),
    }
    payload["scaled_numerator_hash"] = digest(payload)
    return payload


def expanded_terms_json(poly: Mapping[ExpandedKey, Fraction]) -> list[dict[str, Any]]:
    records = []
    for key in sorted(
        poly,
        key=lambda item: (
            -item.t_degree,
            item.scalar_factors,
            item.tensor_word,
        ),
    ):
        counts = Counter(key.scalar_factors)
        records.append(
            {
                "coefficient": fraction_json(poly[key]),
                "t_degree": key.t_degree,
                "scalar_monomial": [
                    {"generator": generator, "power": counts[generator]}
                    for generator in sorted(counts)
                ],
                "tensor_word": [
                    {"adapted_vector": vector, "free_index": index}
                    for vector, index in key.tensor_word
                ],
            }
        )
    return records


def fixture_numerator() -> dict[str, Any]:
    # The loop-quadratic part has matrix [[1,1],[1,3]], nonzero on every
    # nonzero rational one-loop direction.
    return integrals.polynomial(
        (
            (1, {}),
            (1, {"k2": 1}),
            (2, {"kl": 1}),
            (3, {"l2": 1}),
            (1, {"kp1": 1}),
            (-2, {"lp2": 1}),
        )
    )


def manual_fixture_map(*, alternative: bool = False) -> ScalingMap:
    canonical = ScalingMap(
        "FIXTURE_GRAPH",
        digest({"fixture": "graph"}),
        "FIXTURE_ONE_LOOP_SUBGRAPH",
        digest({"fixture": "subgraph"}),
        ("e0", "e1", "e2"),
        1,
        (
            (Fraction(1), Fraction(1)),
            (Fraction(-1), Fraction(1)),
        ),
        "MANUALLY_AUDITABLE_K_EQUALS_H_PLUS_C_L_EQUALS_MINUS_H_PLUS_C",
        ((1, 1),),
    )
    return alternative_adapted_basis(canonical) if alternative else canonical


def cancellation_fixtures() -> dict[str, Any]:
    canonical = manual_fixture_map()
    alternative = manual_fixture_map(alternative=True)
    scalar_rho0 = integrals.polynomial(
        ((1, {"k2": 1}), (2, {"kl": 1}), (1, {"l2": 1}))
    )
    scalar_rho1 = integrals.polynomial(
        ((1, {"k2": 1}), (-1, {"l2": 1}))
    )
    tensor_rho0 = integrals.tensor_polynomial(
        (
            (integrals.constant_polynomial(1), (("k", "m"),)),
            (integrals.constant_polynomial(1), (("l", "m"),)),
        ),
        free_indices=("m",),
    )
    fixtures = {}
    for fixture_id, numerator, expected in (
        ("SCALAR_K_PLUS_L_SQUARED", scalar_rho0, 0),
        ("SCALAR_K2_MINUS_L2", scalar_rho1, 1),
        ("TENSOR_K_PLUS_L", tensor_rho0, 0),
    ):
        first = substitute_numerator(numerator, canonical)
        second = substitute_numerator(numerator, alternative)
        fixtures[fixture_id] = {
            "identity": {
                "SCALAR_K_PLUS_L_SQUARED": "k2+2*kl+l2=(k+l)^2=4*c0^2",
                "SCALAR_K2_MINUS_L2": "k2-l2=4*h0.c0",
                "TENSOR_K_PLUS_L": "k^m+l^m=2*c0^m",
            }[fixture_id],
            "input_numerator": numerator,
            "canonical_basis_result": first,
            "alternative_basis_result": second,
            "expected_rho": expected,
            "basis_change_invariant": (
                first["highest_surviving_t_degree"]
                == second["highest_surviving_t_degree"]
                == expected
            ),
            "leading_degree_cancellation_observed": (
                first["collection_stats"]["exact_zero_cancellations"] > 0
                or first["collection_stats"]["like_monomial_merges"] > 0
            ),
        }
    return {
        "canonical_scaling_map": canonical.as_json(),
        "alternative_scaling_map": alternative.as_json(),
        "fixtures": fixtures,
    }


def edge_routing_scaling_ledger(
    graph: Mapping[str, Any], scaling_map: ScalingMap
) -> list[dict[str, Any]]:
    vector_map = scaling_map.vector_substitution()
    rows = []
    for edge in graph["internal_edges"]:
        reduced = integrals.reduce_routing_after_P(edge["momentum_vector"])
        loop_coefficients = reduced[:2]
        adapted_coefficients = []
        for column in range(2):
            adapted_coefficients.append(
                sum(
                    Fraction(loop_coefficients[row])
                    * scaling_map.basis_matrix[row][column]
                    for row in range(2)
                )
            )
        rows.append(
            {
                "edge_id": edge["edge_id"],
                "inside_subgraph": edge["edge_id"] in scaling_map.subgraph_edge_ids,
                "source_routing_vector_k_l_P_p1_p2": list(edge["momentum_vector"]),
                "reduced_routing_vector_k_l_p1_p2": list(reduced),
                "adapted_loop_coefficients": [
                    fraction_json(value) for value in adapted_coefficients
                ],
                "scaled_coordinate_coefficients": [
                    fraction_json(adapted_coefficients[column])
                    for column in range(scaling_map.subgraph_loop_count)
                ],
                "fixed_under_subgraph_scaling": all(
                    adapted_coefficients[column] == 0
                    for column in range(scaling_map.subgraph_loop_count)
                ),
            }
        )
    return rows


def compile_graph_fixture_certificate(
    graph: Mapping[str, Any], numerator_ast: Mapping[str, Any]
) -> dict[str, Any]:
    subgraphs = graph_subgraph_records(graph)
    rows = []
    rho_by_subgraph: dict[str, int] = {}
    invariance_rows = []
    for subgraph in subgraphs:
        scaling_map = derive_scaling_map(graph, subgraph)
        alternative = alternative_adapted_basis(scaling_map)
        result = substitute_numerator(numerator_ast, scaling_map)
        alternate_result = substitute_numerator(numerator_ast, alternative)
        rho = result["highest_surviving_t_degree"]
        alternate_rho = alternate_result["highest_surviving_t_degree"]
        if rho is None or alternate_rho is None:
            raise NumeratorSubstitutionError("validation fixture vanished under scaling")
        if rho != alternate_rho:
            raise NumeratorSubstitutionError("rho changed under an adapted basis change")
        rho_by_subgraph[str(subgraph["subgraph_id"])] = int(rho)
        ledger = edge_routing_scaling_ledger(graph, scaling_map)
        outside_fixed = all(
            row["fixed_under_subgraph_scaling"]
            for row in ledger
            if not row["inside_subgraph"]
        )
        inside_varies = all(
            not row["fixed_under_subgraph_scaling"]
            for row in ledger
            if row["inside_subgraph"]
        )
        rows.append(
            {
                "subgraph_id": subgraph["subgraph_id"],
                "subgraph_hash": subgraph["subgraph_hash"],
                "scaling_map": scaling_map.as_json(),
                "edge_routing_scaling_ledger": ledger,
                "outside_edges_fixed": outside_fixed,
                "every_inside_edge_varies": inside_varies,
                "scaled_numerator": result,
            }
        )
        invariance_rows.append(
            {
                "subgraph_id": subgraph["subgraph_id"],
                "canonical_rho": rho,
                "alternative_rho": alternate_rho,
                "invariant": rho == alternate_rho,
                "alternative_scaling_map": alternative.as_json(),
            }
        )

    certificate = forest.NumeratorScalingCertificate(
        graph_hash=str(graph["graph_hash"]),
        rho_by_subgraph=rho_by_subgraph,
        source_status="EXACT_VALIDATION_FIXTURE_ONLY_PHYSICAL_NUMERATOR_UNCONNECTED",
        adapted_basis_status="EXACT_ROUTED_MOMENTUM_SUBSTITUTION_AND_COLLECTION",
    )
    forest_record = forest.build_graph_forest_record(graph, certificate)
    return {
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "graph_classification": graph["classification"],
        "input_numerator": numerator_ast,
        "input_numerator_hash": integrals.numerator_hash(numerator_ast),
        "input_status": "VALIDATION_FIXTURE_NOT_PHYSICAL_DALGEBRA_NUMERATOR",
        "subgraph_certificates": rows,
        "basis_change_invariance": invariance_rows,
        "forest_certificate": certificate.canonical_dict(),
        "forest_API_result": {
            "power_counting": forest_record["power_counting"],
            "forests": forest_record["forests"],
            "renormalization_ast": forest_record["renormalization_ast"],
            "no_numerator_pole_or_coefficient_claim": forest_record[
                "no_numerator_pole_or_coefficient_claim"
            ],
        },
    }


def build_payload() -> dict[str, Any]:
    bundle = graphir.build_bundle()
    direct_graphs = list(bundle["literal_direct_graphs"])
    numerator = fixture_numerator()
    graph_records = [
        compile_graph_fixture_certificate(graph, numerator) for graph in direct_graphs
    ]
    return {
        "schema": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "input_provenance": {
            "graph_bundle_hash": bundle["bundle_hash"],
            "graph_source": "REPOSITORY_GRAPHIR_ONLY",
            "numerator_AST_source": "REPOSITORY_INTEGRALS_POLYNOMIAL_AND_TENSOR_AST",
            "forest_API_source": "REPOSITORY_TWO_LOOP_FOREST",
            "comparison_data_read": False,
        },
        "repository_direct_parent_count_discovered": len(direct_graphs),
        "repository_direct_parent_ids": [graph["graph_id"] for graph in direct_graphs],
        "coverage_policy": "ALL_LITERAL_DIRECT_GRAPHS_DISCOVERED_AT_RUNTIME",
        "physical_numerator_status": {
            "compiled_Dalgebra_numerator": None,
            "status": "BLOCKED_PHYSICAL_NUMERATOR_NOT_CONNECTED",
            "fixture_certificates_are_not_physical_certificates": True,
        },
        "algorithm": {
            "adapted_subspace": "NULLSPACE_OF_LOOP_ROWS_OF_EDGES_OUTSIDE_SUBGRAPH",
            "scaling": "h_i->t*h_i; complement and p1,p2 fixed",
            "degree_readout": (
                "SUBSTITUTE_EVERY_SCALAR_DOT_AND_TENSOR_VECTOR; EXPAND; "
                "COLLECT_EXACT_Q_MONOMIALS; TAKE_MAX_SURVIVING_T_POWER"
            ),
            "edge_or_free_index_heuristic_used": False,
            "regulator_inserted_into_numerator": False,
        },
        "manual_cancellation_and_basis_fixtures": cancellation_fixtures(),
        "graph_fixture_certificates": graph_records,
        "terminal_blocks": {
            "physical_rho_by_subgraph": None,
            "physical_divergent_forest": None,
            "master_integral": None,
            "UV_pole": None,
            "renormalized_coefficient": None,
            "status": "FIXTURE_ONLY_NO_PHYSICS_RESULT_CLAIM",
        },
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = []

    def check(name: str, passed: bool, evidence: Any) -> None:
        checks.append(
            {"name": name, "status": "PASS" if passed else "FAIL", "evidence": evidence}
        )

    graph_records = payload["graph_fixture_certificates"]
    check(
        "all_repository_direct_parents_discovered",
        len(graph_records) == payload["repository_direct_parent_count_discovered"]
        and {row["graph_id"] for row in graph_records}
        == set(payload["repository_direct_parent_ids"]),
        payload["repository_direct_parent_ids"],
    )
    check(
        "left_right_outer_full_covered_for_every_parent",
        all(
            {row["subgraph_id"] for row in graph["subgraph_certificates"]}
            == {"left", "right", "outer", "full"}
            for graph in graph_records
        ),
        {
            graph["graph_id"]: [
                row["subgraph_id"] for row in graph["subgraph_certificates"]
            ]
            for graph in graph_records
        },
    )
    check(
        "outside_edges_fixed_inside_edges_vary",
        all(
            row["outside_edges_fixed"] and row["every_inside_edge_varies"]
            for graph in graph_records
            for row in graph["subgraph_certificates"]
        ),
        "routed-edge substitution ledgers",
    )
    check(
        "all_fixture_rhos_are_exact_integers",
        all(
            isinstance(row["scaled_numerator"]["highest_surviving_t_degree"], int)
            and not isinstance(
                row["scaled_numerator"]["highest_surviving_t_degree"], bool
            )
            for graph in graph_records
            for row in graph["subgraph_certificates"]
        ),
        {
            graph["graph_id"]: {
                row["subgraph_id"]: row["scaled_numerator"][
                    "highest_surviving_t_degree"
                ]
                for row in graph["subgraph_certificates"]
            }
            for graph in graph_records
        },
    )
    check(
        "rho_basis_change_invariant_for_every_subgraph",
        all(
            row["invariant"]
            for graph in graph_records
            for row in graph["basis_change_invariance"]
        ),
        {
            graph["graph_id"]: graph["basis_change_invariance"]
            for graph in graph_records
        },
    )
    fixtures = payload["manual_cancellation_and_basis_fixtures"]["fixtures"]
    check(
        "manual_scalar_cancellation_rhos",
        fixtures["SCALAR_K_PLUS_L_SQUARED"]["canonical_basis_result"][
            "highest_surviving_t_degree"
        ]
        == 0
        and fixtures["SCALAR_K2_MINUS_L2"]["canonical_basis_result"][
            "highest_surviving_t_degree"
        ]
        == 1,
        {
            key: value["canonical_basis_result"]["expanded_terms"]
            for key, value in fixtures.items()
            if key.startswith("SCALAR")
        },
    )
    check(
        "manual_tensor_cancellation_rho",
        fixtures["TENSOR_K_PLUS_L"]["canonical_basis_result"][
            "highest_surviving_t_degree"
        ]
        == 0
        and fixtures["TENSOR_K_PLUS_L"]["canonical_basis_result"]["free_indices"]
        == ["m"],
        fixtures["TENSOR_K_PLUS_L"]["canonical_basis_result"]["expanded_terms"],
    )
    check(
        "manual_fixtures_basis_change_invariant",
        all(value["basis_change_invariant"] for value in fixtures.values()),
        {key: value["basis_change_invariant"] for key, value in fixtures.items()},
    )
    check(
        "forest_API_received_complete_fixture_certificate",
        all(
            graph["forest_API_result"]["power_counting"]["unknown_subgraph_ids"] == []
            and graph["forest_API_result"]["power_counting"]["certificate"][
                "graph_hash"
            ]
            == graph["graph_hash"]
            for graph in graph_records
        ),
        {
            graph["graph_id"]: graph["forest_API_result"]["power_counting"][
                "status"
            ]
            for graph in graph_records
        },
    )
    check(
        "no_regulator_inserted",
        not payload["algorithm"]["regulator_inserted_into_numerator"]
        and all(
            row["scaled_numerator"]["coefficient_domain"] == "Q_NO_EPSILON"
            for graph in graph_records
            for row in graph["subgraph_certificates"]
        ),
        "Q exact coefficients",
    )
    check(
        "no_comparison_data",
        not payload["input_provenance"]["comparison_data_read"],
        payload["input_provenance"],
    )
    check(
        "physical_numerator_remains_unconnected",
        payload["physical_numerator_status"]["compiled_Dalgebra_numerator"] is None
        and payload["terminal_blocks"]["physical_rho_by_subgraph"] is None,
        payload["physical_numerator_status"],
    )
    check(
        "no_pole_or_coefficient_claim",
        all(
            payload["terminal_blocks"][key] is None
            for key in (
                "physical_divergent_forest",
                "master_integral",
                "UV_pole",
                "renormalized_coefficient",
            )
        )
        and all(
            graph["forest_API_result"]["no_numerator_pole_or_coefficient_claim"]
            for graph in graph_records
        ),
        payload["terminal_blocks"],
    )
    failed = sum(row["status"] == "FAIL" for row in checks)
    return {
        "schema": "step6.numerator_scaling.audit.v1",
        "status": "PASS" if failed == 0 else "FAIL",
        "checks": checks,
        "totals": {"checks": len(checks), "failed": failed},
        "payload_sha256": digest(payload),
    }


def render_markdown(payload: Mapping[str, Any]) -> str:
    graphs = payload["graph_fixture_certificates"]
    scalar0 = payload["manual_cancellation_and_basis_fixtures"]["fixtures"][
        "SCALAR_K_PLUS_L_SQUARED"
    ]["canonical_basis_result"]
    scalar1 = payload["manual_cancellation_and_basis_fixtures"]["fixtures"][
        "SCALAR_K2_MINUS_L2"
    ]["canonical_basis_result"]
    return rf"""# Step 6 exact numerator-scaling certificates

`{STATUS}`

## 1. Adapted scaling

$$
\binom{{k}}{{l}}=B\binom{{h}}{{c}},
\qquad
h\mapsto th,
\qquad
(c,p_1,p_2)\mapsto(c,p_1,p_2).
$$

For a one-loop subgraph (H),

$$
r_e^{{\rm loop}}B_{{\cdot h}}=0,
\qquad e\notin H.
$$

For the full graph,

$$
(k,l)\mapsto(tk,tl).
$$

## 2. Exact degree

$$
N(B(th,c),p_1,p_2)
=\sum_{{j=0}}^\rho t^jN_j(h,c,p_1,p_2),
\qquad
N_\rho\ne0.
$$

$$
\rho_H=\max\{{j:N_j\ne0\}}.
$$

## 3. Cancellation fixtures

$$
k=h+c,
\qquad
l=-h+c.
$$

$$
k^2+2k\cdot l+l^2=4c^2,
\qquad
\rho={scalar0['highest_surviving_t_degree']}.
$$

$$
k^2-l^2=4h\cdot c,
\qquad
\rho={scalar1['highest_surviving_t_degree']}.
$$

$$
k^m+l^m=2c^m,
\qquad
\rho=0.
$$

## 4. Repository graph census

$$
\#G_{{\rm direct}}={len(graphs)}.
$$

Each discovered parent contains certified fixture rows for

$$
H\in\{{\mathrm{{left}},\mathrm{{right}},\mathrm{{outer}},\mathrm{{full}}\}}.
$$

The physical D-algebra numerator remains unconnected.  No pole or coefficient is evaluated.
"""


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError("Step-6 numerator-scaling audit failed")
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload), encoding="utf-8")
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload, audit


if __name__ == "__main__":
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "checks": audit["totals"]["checks"],
                "direct_parents_discovered": payload[
                    "repository_direct_parent_count_discovered"
                ],
                "subgraph_rows": sum(
                    len(graph["subgraph_certificates"])
                    for graph in payload["graph_fixture_certificates"]
                ),
            },
            sort_keys=True,
        )
    )
