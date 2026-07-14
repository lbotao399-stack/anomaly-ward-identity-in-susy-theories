#!/usr/bin/env python3
"""Independent 16-state gate for the 142 selected Step-6 edge-word pairs.

The selected word pairs are reconstructed directly from the frozen raw-history
seed.  Selection executes only the deferred ``barD2`` coproduct on factor
words; it never calls the preaggregation replay or its primitive executor.

The left side is the existing edge-tagged DWord normal form.  The right side
is a local, self-contained exterior-matrix representation over
``Q(i)[k_pp,k_pm,k_mp,k_mm]``.  The local representation does not import or
call ``step6_symbolic_grassmann_oracle``, ``step6_coefficient_tensor``,
``flat_operators``, the grouped classifier, or the replay compiler.

This certificate proves only the primitive D-algebra identity on the selected
word domain.  It does not compare aggregated remainder objects, execute
residual contact IBP, perform DRED, or determine the two-loop AWI coefficient.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_two_loop_dword as dword
except ModuleNotFoundError:  # direct execution
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import step6_two_loop_dword as dword


ROOT = Path(__file__).resolve().parents[1]
SEED_FIXTURE = (
    ROOT / "generated/step6/measure-tagged-delta-convolution/"
    "measure-tagged-delta-convolution.json"
)
GENERATED = (
    ROOT / "generated/step6/independent-selected-edge-word-dalgebra-gate/"
    "independent-selected-edge-word-dalgebra-gate.json"
)
AUDIT = (
    ROOT / "audits/step6-independent-selected-edge-word-dalgebra-gate-verification.json"
)
TEST_PATH = ROOT / "tests/test_step6_independent_selected_edge_word_dalgebra_gate.py"
DWORD_SOURCE = ROOT / "scripts/step6_two_loop_dword.py"
REPLAY_SOURCE = ROOT / "scripts/step6_preaggregation_measure_delta_replay.py"

SCHEMA = "step6.independent_selected_edge_word_dalgebra_gate.v1"
STATUS = "PASS_EXACT_142_EDGE_WORD_PAIRS_X_16_INDEPENDENT_LOCAL_EXTERIOR_GATE"
RESOLVED_TYPE_ID = "TYPE::IndependentLocalExteriorMatrixGateForSelectedEdgeWordPairs"
SEMANTIC_SCOPE = "SELECTED_EDGE_WORD_PRIMITIVE_DALGEBRA_ONLY"
EXPECTED_SEED_FILE_SHA256 = (
    "b5ecf1ac6a471f7a6d75158d502ec6a869fe5d0bce6599343f285b7cf404a940"
)
EXPECTED_SEED_PAYLOAD_SHA256 = (
    "f10375c672a750baeeb81151ee4379a9052ff43d45bc8c9b1911e69849b65450"
)

OPEN_MISSING_TYPE_IDS = (
    "MISSING_TYPE::IndependentRemainderObjectComparator",
    "MISSING_TYPE::EdgeTaggedContactIBPToALocalSurvivors",
)

PRIMITIVE_TOKEN = {
    "D_plus": ("D", "+"),
    "D_minus": ("D", "-"),
    "barD_dotplus": ("BAR_D", "dot+"),
    "barD_dotminus": ("BAR_D", "dot-"),
}
TOKEN_PRIMITIVE = {value: key for key, value in PRIMITIVE_TOKEN.items()}
PRIMITIVES = tuple(PRIMITIVE_TOKEN)

MOMENTUM_VARIABLES = ("k_pp", "k_pm", "k_mp", "k_mm")
MOMENTUM_VARIABLE_INDEX = {
    symbol: index for index, symbol in enumerate(MOMENTUM_VARIABLES)
}
ZERO_MONOMIAL = (0, 0, 0, 0)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True, order=True)
class LocalGaussian:
    """Exact local copy of Q(i), independent of the DWord scalar class."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "LocalGaussian":
        rhs = local_gaussian(other)
        return LocalGaussian(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "LocalGaussian":
        return LocalGaussian(-self.re, -self.im)

    def __sub__(self, other: object) -> "LocalGaussian":
        return self + (-local_gaussian(other))

    def __mul__(self, other: object) -> "LocalGaussian":
        rhs = local_gaussian(other)
        return LocalGaussian(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def to_json(self) -> dict[str, str]:
        return {"field": "Q(i)", "re": str(self.re), "im": str(self.im)}


def local_gaussian(value: object) -> LocalGaussian:
    if isinstance(value, LocalGaussian):
        return value
    if isinstance(value, int):
        return LocalGaussian(Fraction(value))
    if isinstance(value, Fraction):
        return LocalGaussian(value)
    raise TypeError(f"not an exact local Q(i) scalar: {value!r}")


LOCAL_ZERO_QI = LocalGaussian()
LOCAL_ONE_QI = LocalGaussian(Fraction(1))
LOCAL_MINUS_ONE_QI = LocalGaussian(Fraction(-1))
LOCAL_I_QI = LocalGaussian(Fraction(0), Fraction(1))

Monomial = tuple[int, int, int, int]


@dataclass(frozen=True)
class LocalPolynomial:
    """Sparse Q(i)[k_pp,k_pm,k_mp,k_mm] polynomial."""

    terms: tuple[tuple[Monomial, LocalGaussian], ...] = ()

    @staticmethod
    def from_terms(
        values: Mapping[Monomial, LocalGaussian],
    ) -> "LocalPolynomial":
        return LocalPolynomial(
            tuple(
                sorted((monomial, value) for monomial, value in values.items() if value)
            )
        )

    @staticmethod
    def constant(value: object) -> "LocalPolynomial":
        scalar = local_gaussian(value)
        if not scalar:
            return LocalPolynomial()
        return LocalPolynomial(((ZERO_MONOMIAL, scalar),))

    @staticmethod
    def variable(symbol: str) -> "LocalPolynomial":
        if symbol not in MOMENTUM_VARIABLE_INDEX:
            raise ValueError(f"unknown local momentum variable {symbol}")
        powers = [0, 0, 0, 0]
        powers[MOMENTUM_VARIABLE_INDEX[symbol]] = 1
        return LocalPolynomial(((tuple(powers), LOCAL_ONE_QI),))  # type: ignore[arg-type]

    def as_dict(self) -> dict[Monomial, LocalGaussian]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __add__(self, other: "LocalPolynomial") -> "LocalPolynomial":
        values = self.as_dict()
        for monomial, coefficient in other.terms:
            values[monomial] = values.get(monomial, LOCAL_ZERO_QI) + coefficient
        return LocalPolynomial.from_terms(values)

    def __neg__(self) -> "LocalPolynomial":
        return self.scale(LOCAL_MINUS_ONE_QI)

    def __sub__(self, other: "LocalPolynomial") -> "LocalPolynomial":
        return self + (-other)

    def __mul__(self, other: "LocalPolynomial") -> "LocalPolynomial":
        values: dict[Monomial, LocalGaussian] = {}
        for left_monomial, left_coefficient in self.terms:
            for right_monomial, right_coefficient in other.terms:
                monomial = tuple(
                    left + right
                    for left, right in zip(left_monomial, right_monomial, strict=True)
                )
                values[monomial] = (
                    values.get(monomial, LOCAL_ZERO_QI)
                    + left_coefficient * right_coefficient
                )
        return LocalPolynomial.from_terms(values)

    def scale(self, value: object) -> "LocalPolynomial":
        scalar = local_gaussian(value)
        return LocalPolynomial.from_terms(
            {monomial: scalar * coefficient for monomial, coefficient in self.terms}
        )

    def to_json(self) -> list[dict[str, Any]]:
        return [
            {
                "powers": {
                    symbol: exponent
                    for symbol, exponent in zip(
                        MOMENTUM_VARIABLES, monomial, strict=True
                    )
                    if exponent
                },
                "coefficient": coefficient.to_json(),
            }
            for monomial, coefficient in self.terms
        ]


LOCAL_ZERO = LocalPolynomial()
LOCAL_ONE = LocalPolynomial.constant(LOCAL_ONE_QI)


@dataclass(frozen=True)
class LocalExteriorMatrix:
    """Sparse 16 by 16 matrix over the local exact polynomial ring."""

    entries: tuple[tuple[tuple[int, int], LocalPolynomial], ...] = ()

    @staticmethod
    def from_entries(
        values: Mapping[tuple[int, int], LocalPolynomial],
    ) -> "LocalExteriorMatrix":
        for row, column in values:
            if not 0 <= row < 16 or not 0 <= column < 16:
                raise ValueError("local exterior-matrix index is outside 0,...,15")
        return LocalExteriorMatrix(
            tuple(sorted((key, value) for key, value in values.items() if value))
        )

    @staticmethod
    def identity() -> "LocalExteriorMatrix":
        return LocalExteriorMatrix.from_entries(
            {(index, index): LOCAL_ONE for index in range(16)}
        )

    def as_dict(self) -> dict[tuple[int, int], LocalPolynomial]:
        return dict(self.entries)

    def __add__(self, other: "LocalExteriorMatrix") -> "LocalExteriorMatrix":
        values = self.as_dict()
        for key, value in other.entries:
            values[key] = values.get(key, LOCAL_ZERO) + value
        return LocalExteriorMatrix.from_entries(values)

    def __matmul__(self, other: "LocalExteriorMatrix") -> "LocalExteriorMatrix":
        left_by_pivot: dict[int, list[tuple[int, LocalPolynomial]]] = {}
        right_by_pivot: dict[int, list[tuple[int, LocalPolynomial]]] = {}
        for (row, pivot), value in self.entries:
            left_by_pivot.setdefault(pivot, []).append((row, value))
        for (pivot, column), value in other.entries:
            right_by_pivot.setdefault(pivot, []).append((column, value))
        values: dict[tuple[int, int], LocalPolynomial] = {}
        for pivot in sorted(set(left_by_pivot) & set(right_by_pivot)):
            for row, left in left_by_pivot[pivot]:
                for column, right in right_by_pivot[pivot]:
                    key = row, column
                    values[key] = values.get(key, LOCAL_ZERO) + left * right
        return LocalExteriorMatrix.from_entries(values)

    def scale(
        self, value: LocalPolynomial | LocalGaussian | int
    ) -> "LocalExteriorMatrix":
        scalar = (
            value
            if isinstance(value, LocalPolynomial)
            else LocalPolynomial.constant(value)
        )
        return LocalExteriorMatrix.from_entries(
            {key: scalar * coefficient for key, coefficient in self.entries}
        )

    def apply_basis(self, mask: int) -> tuple[tuple[int, LocalPolynomial], ...]:
        if not 0 <= mask < 16:
            raise ValueError("basis mask is outside 0,...,15")
        return tuple(
            sorted(
                (row, coefficient)
                for (row, column), coefficient in self.entries
                if column == mask
            )
        )

    def to_json(self) -> list[dict[str, Any]]:
        return [
            {"row": row, "column": column, "coefficient": value.to_json()}
            for (row, column), value in self.entries
        ]


def _left_multiplication(generator: int) -> LocalExteriorMatrix:
    values: dict[tuple[int, int], LocalPolynomial] = {}
    for mask in range(16):
        if (mask >> generator) & 1:
            continue
        lower_count = (mask & ((1 << generator) - 1)).bit_count()
        sign = -1 if lower_count & 1 else 1
        values[(mask | (1 << generator), mask)] = LocalPolynomial.constant(sign)
    return LocalExteriorMatrix.from_entries(values)


def _left_derivative(generator: int) -> LocalExteriorMatrix:
    values: dict[tuple[int, int], LocalPolynomial] = {}
    for mask in range(16):
        if not ((mask >> generator) & 1):
            continue
        lower_count = (mask & ((1 << generator) - 1)).bit_count()
        sign = -1 if lower_count & 1 else 1
        values[(mask ^ (1 << generator), mask)] = LocalPolynomial.constant(sign)
    return LocalExteriorMatrix.from_entries(values)


class LocalExteriorEvaluator:
    """Independent representation of the locked primitive superspace algebra."""

    def __init__(self) -> None:
        theta_plus = _left_multiplication(0)
        theta_minus = _left_multiplication(1)
        bartheta_dotplus = _left_multiplication(2)
        bartheta_dotminus = _left_multiplication(3)
        d_theta_plus = _left_derivative(0)
        d_theta_minus = _left_derivative(1)
        d_bartheta_dotplus = _left_derivative(2)
        d_bartheta_dotminus = _left_derivative(3)

        k_pp = LocalPolynomial.variable("k_pp")
        k_pm = LocalPolynomial.variable("k_pm")
        k_mp = LocalPolynomial.variable("k_mp")
        k_mm = LocalPolynomial.variable("k_mm")
        i = LOCAL_I_QI
        minus_i = -LOCAL_I_QI

        self.operators = {
            "D_plus": (
                d_theta_plus
                + bartheta_dotminus.scale(k_pp.scale(i))
                + bartheta_dotplus.scale(k_pm.scale(-i))
            ),
            "D_minus": (
                d_theta_minus
                + bartheta_dotminus.scale(k_mp.scale(i))
                + bartheta_dotplus.scale(k_mm.scale(-i))
            ),
            "barD_dotplus": (
                d_bartheta_dotminus.scale(-1)
                + theta_plus.scale(k_pp.scale(minus_i))
                + theta_minus.scale(k_mp.scale(minus_i))
            ),
            "barD_dotminus": (
                d_bartheta_dotplus
                + theta_plus.scale(k_pm.scale(minus_i))
                + theta_minus.scale(k_mm.scale(minus_i))
            ),
        }

    @lru_cache(maxsize=None)
    def word_matrix(self, word: tuple[str, ...]) -> LocalExteriorMatrix:
        value = LocalExteriorMatrix.identity()
        for primitive in word:
            if primitive not in self.operators:
                raise ValueError(f"unknown primitive {primitive}")
            value = value @ self.operators[primitive]
        return value

    def raw_delta_matrix(
        self, action_word: tuple[str, ...], insertion_word: tuple[str, ...]
    ) -> LocalExteriorMatrix:
        transfer_sign = -1 if len(insertion_word) & 1 else 1
        return (self.word_matrix(action_word) @ self.word_matrix(insertion_word)).scale(
            transfer_sign
        )

    def algebra_certificate(self) -> dict[str, Any]:
        zero = LocalExteriorMatrix()
        same_kind_cases = []
        for left in PRIMITIVES:
            for right in PRIMITIVES:
                same_kind = left.startswith("D_") == right.startswith("D_")
                if not same_kind:
                    continue
                anticommutator = (
                    self.operators[left] @ self.operators[right]
                    + self.operators[right] @ self.operators[left]
                )
                same_kind_cases.append(
                    {
                        "left": left,
                        "right": right,
                        "zero": anticommutator == zero,
                    }
                )

        mixed_component = {
            ("D_plus", "barD_dotplus"): "k_pp",
            ("D_plus", "barD_dotminus"): "k_pm",
            ("D_minus", "barD_dotplus"): "k_mp",
            ("D_minus", "barD_dotminus"): "k_mm",
        }
        mixed_cases = []
        for (left, right), symbol in mixed_component.items():
            anticommutator = (
                self.operators[left] @ self.operators[right]
                + self.operators[right] @ self.operators[left]
            )
            expected = LocalExteriorMatrix.identity().scale(
                LocalPolynomial.variable(symbol).scale(LocalGaussian(0, Fraction(-2)))
            )
            mixed_cases.append(
                {
                    "left": left,
                    "right": right,
                    "momentum_component": symbol,
                    "equals_minus_2_i_p": anticommutator == expected,
                }
            )
        return {
            "generator_order": [
                "theta_plus",
                "theta_minus",
                "bartheta_lower_dotplus",
                "bartheta_lower_dotminus",
            ],
            "primitive_definitions": {
                "D_plus": "d_theta_plus+i*bartheta_dotminus*k_pp-i*bartheta_dotplus*k_pm",
                "D_minus": "d_theta_minus+i*bartheta_dotminus*k_mp-i*bartheta_dotplus*k_mm",
                "barD_dotplus": "-d_bartheta_dotminus-i*theta_plus*k_pp-i*theta_minus*k_mp",
                "barD_dotminus": "d_bartheta_dotplus-i*theta_plus*k_pm-i*theta_minus*k_mm",
            },
            "same_chirality_anticommutator_cases": same_kind_cases,
            "mixed_anticommutator_cases": mixed_cases,
            "all_same_chirality_anticommutators_zero": all(
                row["zero"] for row in same_kind_cases
            ),
            "all_mixed_anticommutators_equal_minus_2_i_p": all(
                row["equals_minus_2_i_p"] for row in mixed_cases
            ),
        }


def _record_hash_valid(record: Mapping[str, Any]) -> bool:
    return str(record.get("record_sha256")) == digest(
        {key: value for key, value in record.items() if key != "record_sha256"}
    )


def _load_seed() -> dict[str, Any]:
    if file_sha256(SEED_FIXTURE) != EXPECTED_SEED_FILE_SHA256:
        raise AssertionError("frozen preaggregation seed file hash changed")
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    if payload.get("payload_sha256") != EXPECTED_SEED_PAYLOAD_SHA256:
        raise AssertionError("frozen preaggregation seed payload hash changed")
    if payload["payload_sha256"] != digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    ):
        raise AssertionError("frozen preaggregation seed self-hash fails")
    replay = payload["measure_tagged_raw_replay"]
    if not all(_record_hash_valid(row) for row in replay["raw_histories"]):
        raise AssertionError("a frozen raw-history record hash fails")
    if not all(
        _record_hash_valid(row) for row in replay["unaggregated_contact_provenance"]
    ):
        raise AssertionError("a frozen raw-parent record hash fails")
    return payload


def _measure_word_children(
    action_history: Mapping[str, Any], contracted_port: str
) -> list[tuple[str, ...]]:
    factors = [
        {
            "port": str(row["grammar_port_id"]),
            "word": tuple(
                str(token) for token in row["derivative_word_outer_to_inner"]
            ),
        }
        for row in action_history["factors_in_raw_AST_order"]
    ]
    if sum(row["port"] == contracted_port for row in factors) != 1:
        raise AssertionError("contracted action port does not resolve uniquely")
    output: list[tuple[str, ...]] = []
    expansions = (
        ("barD_dotplus", "barD_dotminus"),
        ("barD_dotminus", "barD_dotplus"),
    )
    for expansion in expansions:
        states = [factors]
        for primitive in reversed(expansion):
            children = []
            for state in states:
                for hit in range(len(state)):
                    child = [dict(row) for row in state]
                    child[hit]["word"] = (primitive, *child[hit]["word"])
                    children.append(child)
            states = children
        for state in states:
            output.append(
                next(row["word"] for row in state if row["port"] == contracted_port)
            )
    return output


def selected_word_pairs() -> tuple[
    list[tuple[tuple[str, ...], tuple[str, ...]]], dict[str, Any]
]:
    payload = _load_seed()
    replay = payload["measure_tagged_raw_replay"]
    if replay["measure_scopes"] != [
        {
            "distribution_performed": False,
            "execution_state": "DEFERRED_AT_RAW_EXPRESSION_TRACE",
            "measure_kind": "E_MINUS_ANTICHIRAL",
            "normalization": {"field": "Q(i)", "im": "0", "re": "-1/4"},
            "scope_id": "MEASURE::S3_MINUS_1_2::DEFERRED",
            "type_id": "TYPE::MeasureScope",
            "word_outer_to_inner": ["barD2"],
        }
    ]:
        raise AssertionError("frozen deferred measure scope changed")
    histories = {str(row["history_id"]): row for row in replay["raw_histories"]}
    pairs: set[tuple[tuple[str, ...], tuple[str, ...]]] = set()
    raw_measure_pair_count = 0
    for parent in replay["unaggregated_contact_provenance"]:
        action_history = histories[str(parent["action_raw_trace_history_id"])]
        insertion_history = histories[str(parent["insertion_raw_trace_history_id"])]
        action_port = str(parent["contracted_action_port"])
        insertion_port = str(parent["contracted_insertion_port"])
        insertion_factor = next(
            row
            for row in insertion_history["factors_in_raw_AST_order"]
            if str(row["grammar_port_id"]) == insertion_port
        )
        insertion_word = tuple(
            str(token) for token in insertion_factor["derivative_word_outer_to_inner"]
        )
        if list(insertion_word) != parent["contracted_insertion_word_outer_to_inner"]:
            raise AssertionError("frozen insertion word changed")
        action_children = _measure_word_children(action_history, action_port)
        raw_measure_pair_count += len(action_children)
        pairs.update((action_word, insertion_word) for action_word in action_children)
    ordered = sorted(pairs)
    if len(ordered) != 142:
        raise AssertionError(f"selected edge-word pair count changed: {len(ordered)}")
    return ordered, {
        "seed_file_sha256": EXPECTED_SEED_FILE_SHA256,
        "seed_payload_sha256": EXPECTED_SEED_PAYLOAD_SHA256,
        "raw_parent_pair_count": len(replay["unaggregated_contact_provenance"]),
        "measure_expanded_raw_pair_occurrence_count": raw_measure_pair_count,
        "selected_unique_edge_word_pair_count": len(ordered),
        "selected_word_pairs_sha256": digest(
            [
                {
                    "action_word_outer_to_inner": list(action),
                    "insertion_word_outer_to_inner": list(insertion),
                }
                for action, insertion in ordered
            ]
        ),
        "selection_engine": "INDEPENDENT_SEED_WORD_COPRODUCT_NO_DWORD_EXECUTION",
    }


def _dword_endpoints() -> dict[str, dword.ExecutorEndpoint]:
    source = dword.ExecutorEndpoint(
        "edge.source",
        "INTERNAL_SOURCE",
        0,
        "NONE",
        "ORDINARY",
        ("k",),
        (1,),
        "e_AI",
        "edge.target",
    )
    target = dword.ExecutorEndpoint(
        "edge.target",
        "INTERNAL_TARGET",
        0,
        "NONE",
        "ORDINARY",
        ("k",),
        (-1,),
        "e_AI",
        "edge.source",
    )
    return {source.endpoint_id: source, target.endpoint_id: target}


def dword_normal_form(
    action_word: tuple[str, ...], insertion_word: tuple[str, ...]
) -> tuple[list[dword.ExecutorTerm], list[dict[str, object]]]:
    endpoints = _dword_endpoints()
    tokens = []
    for side, word, endpoint in (
        ("A", action_word, "edge.source"),
        ("I", insertion_word, "edge.target"),
    ):
        for position, primitive in enumerate(word):
            kind, component = PRIMITIVE_TOKEN[primitive]
            tokens.append(
                dword.ExecutorToken(
                    f"{side}.{position}", kind, component, endpoint, "PROPAGATOR_DELTA"
                )
            )
    initial = dword.ExecutorTerm(
        "SELECTED_EDGE_WORD",
        dword.ExactPolynomial.constant(dword.ONE),
        tuple(tokens),
        ("e_AI",),
    )
    transferred = dword._canonicalize_delta_endpoints(initial, endpoints)
    return dword._normal_order_terms([transferred], endpoints)


def _local_polynomial_from_dword(value: dword.ExactPolynomial) -> LocalPolynomial:
    terms: dict[Monomial, LocalGaussian] = {}
    for monomial, coefficient in value.terms:
        powers = [0, 0, 0, 0]
        for symbol, exponent in monomial:
            if symbol not in MOMENTUM_VARIABLE_INDEX:
                raise ValueError(f"DWordNF emitted unknown momentum symbol {symbol}")
            powers[MOMENTUM_VARIABLE_INDEX[symbol]] += exponent
        key = tuple(powers)
        terms[key] = terms.get(key, LOCAL_ZERO_QI) + LocalGaussian(
            coefficient.re, coefficient.im
        )
    return LocalPolynomial.from_terms(terms)  # type: ignore[arg-type]


def _normal_form_matrix(
    evaluator: LocalExteriorEvaluator, normal: Sequence[dword.ExecutorTerm]
) -> LocalExteriorMatrix:
    result = LocalExteriorMatrix()
    for term in normal:
        word = tuple(
            TOKEN_PRIMITIVE[(token.derivative_kind, token.spinor_component)]
            for token in term.ordered_tokens
        )
        result = result + evaluator.word_matrix(word).scale(
            _local_polynomial_from_dword(term.polynomial)
        )
    return result


def _basis_output_json(
    value: tuple[tuple[int, LocalPolynomial], ...],
) -> list[dict[str, Any]]:
    return [
        {"output_mask": mask, "coefficient": coefficient.to_json()}
        for mask, coefficient in value
    ]


def _dword_nf_json(normal: Sequence[dword.ExecutorTerm]) -> list[dict[str, Any]]:
    return [
        {
            "polynomial": term.polynomial.to_json(),
            "ordered_primitives": [
                TOKEN_PRIMITIVE[(token.derivative_kind, token.spinor_component)]
                for token in term.ordered_tokens
            ],
        }
        for term in normal
    ]


def _source_independence_certificate() -> dict[str, Any]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    script_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == "scripts":
                script_imports.extend(alias.name for alias in node.names)
            elif node.module.startswith("scripts."):
                script_imports.append(node.module.removeprefix("scripts."))
    independent_node_names = {
        "LocalGaussian",
        "LocalPolynomial",
        "LocalExteriorMatrix",
        "LocalExteriorEvaluator",
        "_left_multiplication",
        "_left_derivative",
    }
    independent_sources = [
        ast.get_source_segment(source, node)
        for node in tree.body
        if isinstance(node, (ast.ClassDef, ast.FunctionDef))
        and node.name in independent_node_names
    ]
    if len(independent_sources) != len(independent_node_names) or any(
        item is None for item in independent_sources
    ):
        raise AssertionError("cannot isolate the complete local exterior engine source")
    independent_source = "\n".join(str(item) for item in independent_sources)
    selector_sources = [
        ast.get_source_segment(source, node)
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"selected_word_pairs", "_measure_word_children"}
    ]
    if len(selector_sources) != 2 or any(item is None for item in selector_sources):
        raise AssertionError("cannot isolate the independent word selector source")
    selector_source = "\n".join(str(item) for item in selector_sources)
    forbidden_tokens = (
        "coefficient.oracle",
        "flat_operators",
        "step6_symbolic_grassmann_oracle",
        "step6_coefficient_tensor",
        "step6_grouped_e_v_i2_i3_ordered_port_normal_form",
        "step6_preaggregation_measure_delta_replay",
    )
    return {
        "imported_project_modules": sorted(set(script_imports)),
        "only_existing_dwordnf_imported": sorted(set(script_imports))
        == ["step6_two_loop_dword"],
        "independent_evaluator_forbidden_token_hits": [
            token for token in forbidden_tokens if token in independent_source
        ],
        "independent_evaluator_uses_existing_dword_module": "dword."
        in independent_source,
        "selector_forbidden_token_hits": [
            token for token in forbidden_tokens if token in selector_source
        ],
        "selector_uses_preaggregation_replay": (
            "step6_preaggregation_measure_delta_replay" in selector_source
        ),
        "independent_ring_and_matrix_classes_are_local": all(
            name in source
            for name in (
                "class LocalGaussian",
                "class LocalPolynomial",
                "class LocalExteriorMatrix",
                "class LocalExteriorEvaluator",
            )
        ),
    }


def _existing_engine_audit() -> dict[str, Any]:
    dword_source = DWORD_SOURCE.read_text(encoding="utf-8")
    replay_source = REPLAY_SOURCE.read_text(encoding="utf-8")
    required_dword_definitions = (
        "def _canonicalize_delta_endpoints(",
        "def _normal_order_one_step(",
        "def _normal_order_terms(",
    )
    return {
        "existing_DWordNF": {
            "source": "scripts/step6_two_loop_dword.py",
            "source_sha256": file_sha256(DWORD_SOURCE),
            "required_definition_hits": {
                definition: definition in dword_source
                for definition in required_dword_definitions
            },
            "role_in_gate": "LEFT_ENGINE_UNDER_TEST",
        },
        "preaggregation_replay": {
            "source": "scripts/step6_preaggregation_measure_delta_replay.py",
            "source_sha256": file_sha256(REPLAY_SOURCE),
            "declares_shared_primitive_oracle_role": (
                "same primitive D-algebra oracle" in replay_source
            ),
            "imports_shared_coefficient_tensor": (
                "step6_coefficient_tensor as coefficient" in replay_source
            ),
            "imports_existing_DWordNF": (
                "step6_two_loop_dword as dword" in replay_source
            ),
            "admissible_as_independent_side": False,
            "gap_id": "G1[G-SCOPE]",
            "gap_type": "G-SCOPE",
            "severity": "P0",
            "missing_before_this_gate": (
                "a local exterior evaluator independent of the shared replay primitive engine"
            ),
            "used_to_select_142_pairs": False,
            "used_by_independent_side": False,
        },
    }


def _convention_bridge() -> dict[str, Any]:
    return {
        "word_order": {
            "input": "outer_to_inner=(P_1,...,P_n)",
            "matrix": "M(P_1)...M(P_n)",
            "action_on_basis": "P_n acts first",
        },
        "delta_endpoint_transfer": {
            "primitive_rule": "P_target*delta=-P_source*delta",
            "insertion_word_length": 5,
            "total_transfer_factor": -1,
            "raw_matrix_formula": "(-1)^len(I)*M(A)*M(I)",
        },
        "primitive_token_bridge": {
            primitive: {
                "dword_kind": kind,
                "dword_component": component,
                "local_matrix": f"M({primitive})",
            }
            for primitive, (kind, component) in PRIMITIVE_TOKEN.items()
        },
        "momentum_bridge": {
            "DWord_endpoint_basis": ["k"],
            "DWord_endpoint_coefficients": [1],
            "local_polynomial_variables": list(MOMENTUM_VARIABLES),
            "component_map": {
                "k_pp": "k_(+,dot+)",
                "k_pm": "k_(+,dot-)",
                "k_mp": "k_(-,dot+)",
                "k_mm": "k_(-,dot-)",
            },
        },
        "normal_form_reconstruction": ("sum_j c_j(k)*M(P_(j,1))...M(P_(j,n_j))"),
    }


@lru_cache(maxsize=1)
def build_payload() -> dict[str, Any]:
    pairs, selection = selected_word_pairs()
    evaluator = LocalExteriorEvaluator()
    algebra = evaluator.algebra_certificate()
    pair_rows = []
    basis_case_count = 0
    mismatch_count = 0
    normal_term_count = 0
    zero_pair_count = 0
    for ordinal, (action_word, insertion_word) in enumerate(pairs):
        normal, zeros = dword_normal_form(action_word, insertion_word)
        raw_matrix = evaluator.raw_delta_matrix(action_word, insertion_word)
        reconstructed_matrix = _normal_form_matrix(evaluator, normal)
        matrix_equal = raw_matrix == reconstructed_matrix
        basis_rows = []
        for mask in range(16):
            raw_output = raw_matrix.apply_basis(mask)
            reconstructed_output = reconstructed_matrix.apply_basis(mask)
            equal = raw_output == reconstructed_output
            basis_case_count += 1
            mismatch_count += int(not equal)
            basis_rows.append(
                {
                    "basis_mask": mask,
                    "raw_output_sha256": digest(_basis_output_json(raw_output)),
                    "dwordnf_output_sha256": digest(
                        _basis_output_json(reconstructed_output)
                    ),
                    "outputs_equal": equal,
                    "raw_output_term_count": len(raw_output),
                }
            )
        normal_term_count += len(normal)
        zero_pair_count += int(not normal)
        core = {
            "pair_ordinal": ordinal,
            "action_word_outer_to_inner": list(action_word),
            "insertion_word_outer_to_inner": list(insertion_word),
            "target_delta_transfer_sign": -1 if len(insertion_word) & 1 else 1,
            "dwordnf_normal_term_count": len(normal),
            "dwordnf_zero_branch_count": len(zeros),
            "dwordnf_normal_form_sha256": digest(_dword_nf_json(normal)),
            "independent_raw_matrix_sha256": digest(raw_matrix.to_json()),
            "dwordnf_reconstructed_matrix_sha256": digest(
                reconstructed_matrix.to_json()
            ),
            "operator_matrices_equal": matrix_equal,
            "basis_cases": basis_rows,
            "all_16_basis_outputs_equal": all(
                row["outputs_equal"] for row in basis_rows
            ),
        }
        pair_rows.append({"pair_id": f"EDGEWORD::{digest(core)[:24]}", **core})

    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "resolved_type_id": RESOLVED_TYPE_ID,
        "semantic_scope": SEMANTIC_SCOPE,
        "selection": selection,
        "existing_engine_audit": _existing_engine_audit(),
        "independence_contract": _source_independence_certificate(),
        "convention_bridge": _convention_bridge(),
        "local_exterior_algebra": algebra,
        "comparison": {
            "left_engine": "EXISTING_EDGE_TAGGED_DWORD_NORMAL_FORM",
            "right_engine": "INDEPENDENT_LOCAL_EXTERIOR_MATRIX_EVALUATOR",
            "coefficient_ring": "Q(i)[k_pp,k_pm,k_mp,k_mm]",
            "delta_transfer_rule": "D_target*delta=-D_source*delta",
            "mixed_anticommutator": "{D_a,barD_dota}=-2*i*k_(a,dota)",
            "selected_word_pair_count": len(pair_rows),
            "coefficient_basis_dimension": 16,
            "exact_basis_case_count": basis_case_count,
            "basis_mismatch_count": mismatch_count,
            "dwordnf_normal_term_count": normal_term_count,
            "dwordnf_zero_pair_count": zero_pair_count,
            "all_operator_matrices_equal": all(
                row["operator_matrices_equal"] for row in pair_rows
            ),
            "all_basis_outputs_equal": all(
                row["all_16_basis_outputs_equal"] for row in pair_rows
            ),
            "pair_rows": pair_rows,
            "pair_rows_sha256": digest(pair_rows),
        },
        "open_missing_type_ids": list(OPEN_MISSING_TYPE_IDS),
        "excluded_claims": {
            "aggregated_remainder_object_equality": None,
            "residual_contact_ibp": None,
            "DRED_performed": False,
            "UV_pole": None,
            "two_loop_AWI_coefficient": None,
            "two_loop_AWI_coefficient_status": "UNCOMPUTED",
        },
        "external_result_used_as_input": False,
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    comparison = payload["comparison"]
    algebra = payload["local_exterior_algebra"]
    independence = payload["independence_contract"]
    return {
        "schema_and_status_exact": (
            payload["schema"] == SCHEMA
            and payload["status"] == STATUS
            and payload["resolved_type_id"] == RESOLVED_TYPE_ID
        ),
        "frozen_seed_hashes_exact": (
            payload["selection"]["seed_file_sha256"] == EXPECTED_SEED_FILE_SHA256
            and payload["selection"]["seed_payload_sha256"]
            == EXPECTED_SEED_PAYLOAD_SHA256
        ),
        "selected_pair_count_exact": comparison["selected_word_pair_count"] == 142,
        "basis_case_count_exact": comparison["exact_basis_case_count"] == 142 * 16,
        "no_basis_mismatch": comparison["basis_mismatch_count"] == 0,
        "all_operator_matrices_equal": comparison["all_operator_matrices_equal"],
        "all_basis_outputs_equal": comparison["all_basis_outputs_equal"],
        "local_same_chirality_algebra_exact": algebra[
            "all_same_chirality_anticommutators_zero"
        ],
        "local_mixed_algebra_exact": algebra[
            "all_mixed_anticommutators_equal_minus_2_i_p"
        ],
        "independent_side_has_no_shared_primitive_engine": (
            independence["only_existing_dwordnf_imported"]
            and not independence["independent_evaluator_forbidden_token_hits"]
            and not independence["independent_evaluator_uses_existing_dword_module"]
            and not independence["selector_forbidden_token_hits"]
            and not independence["selector_uses_preaggregation_replay"]
            and independence["independent_ring_and_matrix_classes_are_local"]
        ),
        "open_boundaries_explicit": (
            payload["open_missing_type_ids"] == list(OPEN_MISSING_TYPE_IDS)
            and payload["excluded_claims"]["aggregated_remainder_object_equality"]
            is None
            and payload["excluded_claims"]["residual_contact_ibp"] is None
            and payload["excluded_claims"]["two_loop_AWI_coefficient"] is None
            and payload["excluded_claims"]["two_loop_AWI_coefficient_status"]
            == "UNCOMPUTED"
        ),
        "no_external_result": payload["external_result_used_as_input"] is False,
        "payload_hash_valid": payload["payload_sha256"]
        == digest(
            {key: value for key, value in payload.items() if key != "payload_sha256"}
        ),
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    return {
        "schema": "step6.independent_selected_edge_word_dalgebra_gate.audit.v1",
        "status": payload["status"],
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "counts": {
            "selected_word_pairs": payload["comparison"]["selected_word_pair_count"],
            "coefficient_basis_dimension": payload["comparison"][
                "coefficient_basis_dimension"
            ],
            "exact_basis_cases": payload["comparison"]["exact_basis_case_count"],
            "basis_mismatches": payload["comparison"]["basis_mismatch_count"],
            "dwordnf_normal_terms": payload["comparison"]["dwordnf_normal_term_count"],
            "dwordnf_zero_pairs": payload["comparison"]["dwordnf_zero_pair_count"],
        },
        "selected_word_pairs_sha256": payload["selection"][
            "selected_word_pairs_sha256"
        ],
        "pair_rows_sha256": payload["comparison"]["pair_rows_sha256"],
        "resolved_type_id": RESOLVED_TYPE_ID,
        "semantic_scope": SEMANTIC_SCOPE,
        "open_missing_type_ids": list(OPEN_MISSING_TYPE_IDS),
        "two_loop_AWI_coefficient_status": "UNCOMPUTED",
        "payload_sha256": payload["payload_sha256"],
        "script_sha256": file_sha256(Path(__file__)),
        "test_sha256": file_sha256(TEST_PATH),
    }


def write_outputs(payload: Mapping[str, Any]) -> None:
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    AUDIT.write_text(
        json.dumps(build_audit(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    payload = build_payload()
    audit = build_audit(payload)
    if not audit["all_checks_passed"]:
        failed = [name for name, passed in audit["checks"].items() if not passed]
        raise SystemExit(f"independent selected-word gate failed: {failed}")
    write_outputs(payload)
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
