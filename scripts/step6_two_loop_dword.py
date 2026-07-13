#!/usr/bin/env python3
"""Proposal-only two-loop edge-tagged D-algebra contract and executor.

The module fixes typed words, a rooted theta decomposition, the ordered
rewrite phases, an exact lexicographic termination measure, exact Q(i)
sign/Koszul ledgers, and a symbolic-polynomial oracle gate.  It deliberately
does not infer a derivative scope from topology.  Every decorated literal
``K4_MINUS_ONE_EDGE`` graph therefore fails closed until a future
Wick-complete record supplies an explicit ordered derivative-scope AST and an
explicit propagator kernel for every internal edge.

Physical graph words still fail closed when their exact scope input is absent.
Independently, a typed exact executor evaluates bounded edge-tagged words and
emits every rewrite sign, mixed momentum, external token, and classification.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step6_two_loop_graphir import build_bundle


GENERATED_DIR = ROOT / "generated/step6/two-loop-dword"
GENERATED_CONTRACT = GENERATED_DIR / "dword-contract.json"
GENERATED_SCHEMA = GENERATED_DIR / "wick-input-schema.json"
GENERATED_MD = GENERATED_DIR / "two-loop-dword.md"
AUDIT = ROOT / "audits/step6-two-loop-dword-verification.json"

SCHEMA_VERSION = "step6.two_loop_dword.v1"
INPUT_SCHEMA_VERSION = "step6.wick_complete_dword_input.v1"
EXECUTOR_SCHEMA_VERSION = "step6.edge_tagged_dalgebra_program.v1"
EXECUTOR_RESULT_VERSION = "step6.edge_tagged_dalgebra_result.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
BLOCKED_STATUS = "BLOCKED_MISSING_WICK_COMPLETE_DWORD_INPUTS"
READY_STATUS = "READY_PHASE_SCHEDULE_CONTRACT_ONLY"
QI_DOMAIN = "Q(i)"

PHASE_ORDER = (
    "SCOPE_EXPANSION",
    "ENDPOINT_CANONICALIZATION",
    "PIVOTED_IBP",
    "PRIMITIVE_NORMAL_ORDERING",
    "PROJECTOR_REDUCTION",
    "EXTERNAL_CHIRALITY",
    "GRASSMANN_SATURATION",
    "TYPED_EDGE_COLLAPSE",
)

MEASURE_COMPONENTS = (
    "unexpanded_scope_nodes",
    "noncanonical_endpoint_tokens",
    "off_tree_pivot_distance",
    "primitive_order_inversions",
    "unreduced_projector_nodes",
    "unresolved_external_chirality_actions",
    "grassmann_saturation_defect",
    "typed_collapsible_edges",
)

DERIVATIVE_KINDS = {
    "D": ("UNDOTTED", 1, 1),
    "BAR_D": ("DOTTED", 1, 1),
    "D2": ("UNDOTTED", 0, 2),
    "BAR_D2": ("DOTTED", 0, 2),
}

LEDGER_KINDS = {
    "KOSZUL",
    "FOURIER",
    "LEIBNIZ",
    "ENDPOINT_TRANSFER",
    "PRIMITIVE_REORDER",
    "PROJECTOR",
    "CHIRALITY",
    "COLLAPSE",
    "MIXED_ANTICOMMUTATOR",
    "NILPOTENCE",
    "EOM",
}

ENDPOINT_KINDS = {
    "INTERNAL_SOURCE",
    "INTERNAL_TARGET",
    "EXTERNAL_BACKGROUND",
    "COMPOSITE_SOURCE",
}

CHIRALITY_CLASSES = {"NONE", "CHIRAL", "ANTICHIRAL"}
EQUATION_CLASSES = {"ORDINARY", "EOM"}
TOKEN_CARRIERS = {"FIELD", "PROPAGATOR_DELTA"}
PRIMITIVE_KINDS = {"D", "BAR_D"}
EXECUTOR_PROGRAM_KINDS = {"FIXTURE", "GLOBAL_NUMERATOR"}
UNDOTTED_COMPONENTS = {"+", "-"}
DOTTED_COMPONENTS = {"dot+", "dot-"}

FORBIDDEN_SAMPLE_KEYS = {
    "sample",
    "samples",
    "sample_point",
    "sample_points",
    "probe",
    "probes",
    "numerical_check",
    "random_check",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"not an exact rational: {value!r}")


@dataclass(frozen=True, order=True)
class GaussianRational:
    """An exact element of Q(i), never a floating-point approximation."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        return GaussianRational(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "GaussianRational":
        return GaussianRational(-self.re, -self.im)

    def __sub__(self, other: object) -> "GaussianRational":
        return self + (-gaussian(other))

    def __mul__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        return GaussianRational(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        norm = rhs.re * rhs.re + rhs.im * rhs.im
        if norm == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return GaussianRational(
            (self.re * rhs.re + self.im * rhs.im) / norm,
            (self.im * rhs.re - self.re * rhs.im) / norm,
        )

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def to_json(self) -> dict[str, str]:
        return {"domain": QI_DOMAIN, "re": str(self.re), "im": str(self.im)}

    @classmethod
    def from_json(cls, value: Mapping[str, object]) -> "GaussianRational":
        if set(value) != {"domain", "re", "im"} or value["domain"] != QI_DOMAIN:
            raise ValueError("every exact scalar must use {domain: Q(i), re, im}")
        return cls(fraction(value["re"]), fraction(value["im"]))


def gaussian(value: object) -> GaussianRational:
    if isinstance(value, GaussianRational):
        return value
    if isinstance(value, (int, Fraction)):
        return GaussianRational(fraction(value))
    raise TypeError(f"not an exact Q(i) scalar: {value!r}")


ONE = GaussianRational(Fraction(1), Fraction(0))
MINUS_ONE = GaussianRational(Fraction(-1), Fraction(0))
I_UNIT = GaussianRational(Fraction(0), Fraction(1))
MINUS_TWO_I = GaussianRational(Fraction(0), Fraction(-2))

Monomial = tuple[tuple[str, int], ...]


def _multiply_monomials(left: Monomial, right: Monomial) -> Monomial:
    powers: dict[str, int] = {}
    for symbol, exponent in (*left, *right):
        powers[symbol] = powers.get(symbol, 0) + exponent
    return tuple(sorted((symbol, exponent) for symbol, exponent in powers.items() if exponent))


@dataclass(frozen=True)
class ExactPolynomial:
    """Sparse exact Q(i) polynomial in typed momentum components."""

    terms: tuple[tuple[Monomial, GaussianRational], ...] = ()

    @staticmethod
    def from_terms(terms: Mapping[Monomial, GaussianRational]) -> "ExactPolynomial":
        return ExactPolynomial(tuple(sorted((monomial, value) for monomial, value in terms.items() if value)))

    @staticmethod
    def constant(value: object) -> "ExactPolynomial":
        coefficient = gaussian(value)
        return ExactPolynomial.from_terms({(): coefficient}) if coefficient else ExactPolynomial()

    @staticmethod
    def variable(symbol: str) -> "ExactPolynomial":
        if not symbol or any(character.isspace() for character in symbol):
            raise ValueError("momentum variable must be nonempty and whitespace-free")
        return ExactPolynomial.from_terms({((symbol, 1),): ONE})

    def as_dict(self) -> dict[Monomial, GaussianRational]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __add__(self, other: "ExactPolynomial") -> "ExactPolynomial":
        merged = self.as_dict()
        for monomial, value in other.terms:
            merged[monomial] = merged.get(monomial, GaussianRational()) + value
        return ExactPolynomial.from_terms(merged)

    def __neg__(self) -> "ExactPolynomial":
        return self.scale(MINUS_ONE)

    def __sub__(self, other: "ExactPolynomial") -> "ExactPolynomial":
        return self + (-other)

    def __mul__(self, other: "ExactPolynomial") -> "ExactPolynomial":
        result: dict[Monomial, GaussianRational] = {}
        for left_monomial, left_value in self.terms:
            for right_monomial, right_value in other.terms:
                monomial = _multiply_monomials(left_monomial, right_monomial)
                result[monomial] = result.get(monomial, GaussianRational()) + left_value * right_value
        return ExactPolynomial.from_terms(result)

    def scale(self, value: object) -> "ExactPolynomial":
        coefficient = gaussian(value)
        return ExactPolynomial.from_terms(
            {monomial: coefficient * term_value for monomial, term_value in self.terms}
        )

    def scalar_multiple_of(self, divisor: "ExactPolynomial") -> GaussianRational | None:
        """Return c only when self=c*divisor exactly."""

        if not divisor:
            raise ZeroDivisionError("zero polynomial divisor")
        left = self.as_dict()
        right = divisor.as_dict()
        if set(left) != set(right):
            return None
        pivot = next(iter(sorted(right)))
        coefficient = left[pivot] / right[pivot]
        return coefficient if self == divisor.scale(coefficient) else None

    def to_json(self) -> list[dict[str, object]]:
        return [
            {
                "monomial": [
                    {"symbol": symbol, "exponent": exponent}
                    for symbol, exponent in monomial
                ],
                "factor": value.to_json(),
            }
            for monomial, value in self.terms
        ]


POLY_ZERO = ExactPolynomial()
POLY_ONE = ExactPolynomial.constant(ONE)


@dataclass(frozen=True)
class ExecutorEndpoint:
    endpoint_id: str
    endpoint_kind: str
    parity: int
    chirality: str
    equation_class: str
    momentum_basis: tuple[str, ...]
    momentum_coefficients: tuple[int, ...]
    edge_id: str | None = None
    paired_endpoint_id: str | None = None

    def __post_init__(self) -> None:
        if not self.endpoint_id:
            raise ValueError("executor endpoint id is required")
        if self.endpoint_kind not in ENDPOINT_KINDS:
            raise ValueError(f"unknown endpoint kind {self.endpoint_kind}")
        if self.parity not in (0, 1):
            raise ValueError("endpoint parity must lie in Z2")
        if self.chirality not in CHIRALITY_CLASSES:
            raise ValueError(f"unknown chirality {self.chirality}")
        if self.equation_class not in EQUATION_CLASSES:
            raise ValueError(f"unknown equation class {self.equation_class}")
        if not self.momentum_basis or len(self.momentum_basis) != len(self.momentum_coefficients):
            raise ValueError("typed endpoint momentum basis and coefficients disagree")
        internal = self.endpoint_kind in {"INTERNAL_SOURCE", "INTERNAL_TARGET"}
        if internal and (self.edge_id is None or self.paired_endpoint_id is None):
            raise ValueError("internal endpoints require an edge and paired endpoint")
        if not internal and (self.edge_id is not None or self.paired_endpoint_id is not None):
            raise ValueError("external/composite endpoints cannot carry an internal edge pairing")

    def to_json(self) -> dict[str, object]:
        return {
            "endpoint_id": self.endpoint_id,
            "endpoint_kind": self.endpoint_kind,
            "parity": self.parity,
            "chirality": self.chirality,
            "equation_class": self.equation_class,
            "momentum": {
                "basis": list(self.momentum_basis),
                "coefficients": list(self.momentum_coefficients),
            },
            "edge_id": self.edge_id,
            "paired_endpoint_id": self.paired_endpoint_id,
        }


@dataclass(frozen=True)
class ExecutorToken:
    token_id: str
    derivative_kind: str
    spinor_component: str
    endpoint_id: str
    carrier: str

    def __post_init__(self) -> None:
        if not self.token_id:
            raise ValueError("executor token id is required")
        if self.derivative_kind not in PRIMITIVE_KINDS:
            raise ValueError(f"unknown primitive derivative {self.derivative_kind}")
        allowed = UNDOTTED_COMPONENTS if self.derivative_kind == "D" else DOTTED_COMPONENTS
        if self.spinor_component not in allowed:
            raise ValueError("spinor component disagrees with derivative kind")
        if self.carrier not in TOKEN_CARRIERS:
            raise ValueError(f"unknown derivative carrier {self.carrier}")

    def with_endpoint(self, endpoint_id: str) -> "ExecutorToken":
        return ExecutorToken(
            self.token_id,
            self.derivative_kind,
            self.spinor_component,
            endpoint_id,
            self.carrier,
        )

    def to_json(self) -> dict[str, object]:
        return {
            "token_id": self.token_id,
            "derivative_kind": self.derivative_kind,
            "spinor_component": self.spinor_component,
            "endpoint_id": self.endpoint_id,
            "carrier": self.carrier,
            "operator_parity": 1,
        }


@dataclass(frozen=True)
class ExecutorTerm:
    branch_id: str
    polynomial: ExactPolynomial
    ordered_tokens: tuple[ExecutorToken, ...]
    denominator_edges: tuple[str, ...]
    ledger: tuple[dict[str, object], ...] = ()

    def replace(
        self,
        *,
        polynomial: ExactPolynomial | None = None,
        ordered_tokens: tuple[ExecutorToken, ...] | None = None,
        denominator_edges: tuple[str, ...] | None = None,
        ledger_entry: dict[str, object] | None = None,
    ) -> "ExecutorTerm":
        return ExecutorTerm(
            self.branch_id,
            self.polynomial if polynomial is None else polynomial,
            self.ordered_tokens if ordered_tokens is None else ordered_tokens,
            self.denominator_edges if denominator_edges is None else denominator_edges,
            self.ledger + (() if ledger_entry is None else (ledger_entry,)),
        )


@dataclass(frozen=True)
class ExactLedgerEntry:
    ledger_id: str
    phase: str
    kind: str
    factor: GaussianRational
    rule_id: str
    token_ids: tuple[str, ...]
    moving_parity: int | None = None
    crossed_parities: tuple[int, ...] = ()
    oracle_identity_id: str | None = None

    def __post_init__(self) -> None:
        if not self.ledger_id or not self.rule_id:
            raise ValueError("ledger id and rule id are required")
        if self.phase not in PHASE_ORDER:
            raise ValueError(f"unknown ledger phase: {self.phase}")
        if self.kind not in LEDGER_KINDS:
            raise ValueError(f"unknown ledger kind: {self.kind}")
        if any(parity not in (0, 1) for parity in self.crossed_parities):
            raise ValueError("crossed parities must lie in Z2")
        if self.kind == "KOSZUL":
            if self.moving_parity not in (0, 1):
                raise ValueError("a Koszul entry requires moving_parity in Z2")
            expected = MINUS_ONE if self.moving_parity * sum(self.crossed_parities) % 2 else ONE
            if self.factor != expected:
                raise ValueError(
                    "Koszul factor must equal (-1)^(moving_parity*sum(crossed_parities))"
                )
        elif self.moving_parity is not None or self.crossed_parities:
            raise ValueError("only a Koszul entry may carry crossed parities")

    def to_json(self) -> dict[str, object]:
        return {
            "ledger_id": self.ledger_id,
            "phase": self.phase,
            "kind": self.kind,
            "factor": self.factor.to_json(),
            "rule_id": self.rule_id,
            "token_ids": list(self.token_ids),
            "moving_parity": self.moving_parity,
            "crossed_parities": list(self.crossed_parities),
            "oracle_identity_id": self.oracle_identity_id,
        }

    @classmethod
    def from_json(cls, value: Mapping[str, object]) -> "ExactLedgerEntry":
        required = {"ledger_id", "phase", "kind", "factor", "rule_id", "token_ids"}
        if not required <= set(value):
            raise ValueError(f"ledger entry misses {sorted(required - set(value))}")
        return cls(
            ledger_id=str(value["ledger_id"]),
            phase=str(value["phase"]),
            kind=str(value["kind"]),
            factor=GaussianRational.from_json(_mapping(value["factor"], "ledger factor")),
            rule_id=str(value["rule_id"]),
            token_ids=tuple(str(item) for item in _sequence(value["token_ids"], "token ids")),
            moving_parity=None if value.get("moving_parity") is None else int(value["moving_parity"]),
            crossed_parities=tuple(int(item) for item in value.get("crossed_parities", ())),
            oracle_identity_id=(
                None if value.get("oracle_identity_id") is None else str(value["oracle_identity_id"])
            ),
        )


def executor_ledger_entry(
    *,
    ledger_id: str,
    phase: str,
    kind: str,
    factor: GaussianRational,
    rule_id: str,
    token_ids: Sequence[str],
    details: Mapping[str, object] | None = None,
) -> dict[str, object]:
    if phase not in PHASE_ORDER or kind not in LEDGER_KINDS:
        raise ValueError("executor ledger phase or kind is undeclared")
    return {
        "ledger_id": ledger_id,
        "phase": phase,
        "kind": kind,
        "factor": factor.to_json(),
        "rule_id": rule_id,
        "token_ids": list(token_ids),
        "details": {} if details is None else dict(details),
    }


def endpoint_from_json(value: Mapping[str, object]) -> ExecutorEndpoint:
    momentum = _mapping(value.get("momentum"), "executor endpoint momentum")
    return ExecutorEndpoint(
        endpoint_id=str(value.get("endpoint_id", "")),
        endpoint_kind=str(value.get("endpoint_kind", "")),
        parity=int(value.get("parity", -1)),
        chirality=str(value.get("chirality", "")),
        equation_class=str(value.get("equation_class", "")),
        momentum_basis=tuple(str(item) for item in _sequence(momentum.get("basis"), "momentum basis")),
        momentum_coefficients=tuple(
            int(item) for item in _sequence(momentum.get("coefficients"), "momentum coefficients")
        ),
        edge_id=None if value.get("edge_id") is None else str(value["edge_id"]),
        paired_endpoint_id=(
            None if value.get("paired_endpoint_id") is None else str(value["paired_endpoint_id"])
        ),
    )


def token_from_json(value: Mapping[str, object]) -> ExecutorToken:
    return ExecutorToken(
        token_id=str(value.get("token_id", "")),
        derivative_kind=str(value.get("derivative_kind", "")),
        spinor_component=str(value.get("spinor_component", "")),
        endpoint_id=str(value.get("endpoint_id", "")),
        carrier=str(value.get("carrier", "")),
    )


def _token_sort_key(token: ExecutorToken, endpoint_order: Mapping[str, int]) -> tuple[int, int, int, str]:
    kind_order = 0 if token.derivative_kind == "BAR_D" else 1
    component_order = {
        "dot+": 0,
        "dot-": 1,
        "+": 0,
        "-": 1,
    }[token.spinor_component]
    return endpoint_order[token.endpoint_id], kind_order, component_order, token.token_id


def _momentum_component(endpoint: ExecutorEndpoint, token_d: ExecutorToken, token_bar: ExecutorToken) -> ExactPolynomial:
    if token_d.derivative_kind != "D" or token_bar.derivative_kind != "BAR_D":
        raise ValueError("mixed momentum requires D then BAR_D")
    suffix = {
        ("+", "dot+"): "pp",
        ("+", "dot-"): "pm",
        ("-", "dot+"): "mp",
        ("-", "dot-"): "mm",
    }[(token_d.spinor_component, token_bar.spinor_component)]
    result = POLY_ZERO
    for coefficient, basis_symbol in zip(endpoint.momentum_coefficients, endpoint.momentum_basis):
        if coefficient:
            result = result + ExactPolynomial.variable(f"{basis_symbol}_{suffix}").scale(coefficient)
    return result


def endpoint_square_polynomial(endpoint: ExecutorEndpoint) -> ExactPolynomial:
    def component(suffix: str) -> ExactPolynomial:
        value = POLY_ZERO
        for coefficient, basis_symbol in zip(endpoint.momentum_coefficients, endpoint.momentum_basis):
            if coefficient:
                value = value + ExactPolynomial.variable(f"{basis_symbol}_{suffix}").scale(coefficient)
        return value

    return component("pp") * component("mm") - component("pm") * component("mp")


def _apply_ibp_transfers(
    term: ExecutorTerm,
    transfers: Sequence[Mapping[str, object]],
    endpoints: Mapping[str, ExecutorEndpoint],
) -> ExecutorTerm:
    current = term
    for ordinal, transfer in enumerate(transfers):
        if str(transfer.get("branch_id")) != term.branch_id:
            continue
        token_id = str(transfer.get("token_id", ""))
        positions = [index for index, token in enumerate(current.ordered_tokens) if token.token_id == token_id]
        if len(positions) != 1:
            raise ValueError(f"IBP transfer token {token_id} is not unique")
        position = positions[0]
        token = current.ordered_tokens[position]
        source_id = str(transfer.get("from_endpoint_id", ""))
        target_id = str(transfer.get("to_endpoint_id", ""))
        if token.endpoint_id != source_id or source_id not in endpoints or target_id not in endpoints:
            raise ValueError("IBP transfer endpoint binding mismatch")
        crossed_ids = [
            str(item)
            for item in _sequence(transfer.get("crossed_endpoint_ids"), "IBP crossed endpoints")
        ]
        if any(endpoint_id not in endpoints for endpoint_id in crossed_ids):
            raise ValueError("IBP transfer crosses an unknown endpoint")
        crossed_parity = sum(endpoints[endpoint_id].parity for endpoint_id in crossed_ids) & 1
        boundary_factor = MINUS_ONE
        koszul_factor = MINUS_ONE if crossed_parity else ONE
        tokens = list(current.ordered_tokens)
        tokens[position] = token.with_endpoint(target_id)
        boundary_ledger = executor_ledger_entry(
            ledger_id=f"{term.branch_id}:IBP:{ordinal}:boundary",
            phase="PIVOTED_IBP",
            kind="ENDPOINT_TRANSFER",
            factor=boundary_factor,
            rule_id="integral_of_total_D_is_zero",
            token_ids=[token_id],
            details={"from": source_id, "to": target_id},
        )
        koszul_ledger = executor_ledger_entry(
            ledger_id=f"{term.branch_id}:IBP:{ordinal}:koszul",
            phase="PIVOTED_IBP",
            kind="KOSZUL",
            factor=koszul_factor,
            rule_id="(-1)^(sum_crossed_endpoint_parities)",
            token_ids=[token_id],
            details={
                "crossed_endpoint_ids": crossed_ids,
                "crossed_parities": [endpoints[endpoint_id].parity for endpoint_id in crossed_ids],
            },
        )
        current = current.replace(
            polynomial=current.polynomial.scale(boundary_factor * koszul_factor),
            ordered_tokens=tuple(tokens),
            ledger_entry=boundary_ledger,
        )
        current = current.replace(ledger_entry=koszul_ledger)
    return current


def _canonicalize_delta_endpoints(
    term: ExecutorTerm, endpoints: Mapping[str, ExecutorEndpoint]
) -> ExecutorTerm:
    current = term
    tokens = list(current.ordered_tokens)
    for position, token in enumerate(tuple(tokens)):
        endpoint = endpoints[token.endpoint_id]
        if token.carrier != "PROPAGATOR_DELTA" or endpoint.endpoint_kind != "INTERNAL_TARGET":
            continue
        assert endpoint.paired_endpoint_id is not None
        paired = endpoints[endpoint.paired_endpoint_id]
        if paired.endpoint_kind != "INTERNAL_SOURCE" or paired.edge_id != endpoint.edge_id:
            raise ValueError("internal delta endpoint pairing is not source-target")
        tokens[position] = token.with_endpoint(paired.endpoint_id)
        entry = executor_ledger_entry(
            ledger_id=f"{term.branch_id}:DELTA_TRANSFER:{position}",
            phase="ENDPOINT_CANONICALIZATION",
            kind="ENDPOINT_TRANSFER",
            factor=MINUS_ONE,
            rule_id="D_target_delta(theta_source-theta_target)=-D_source_delta",
            token_ids=[token.token_id],
            details={
                "edge_id": endpoint.edge_id,
                "from": endpoint.endpoint_id,
                "to": paired.endpoint_id,
            },
        )
        current = current.replace(polynomial=current.polynomial.scale(MINUS_ONE), ledger_entry=entry)
    return current.replace(ordered_tokens=tuple(tokens))


def _normal_order_one_step(
    term: ExecutorTerm,
    endpoints: Mapping[str, ExecutorEndpoint],
    endpoint_order: Mapping[str, int],
) -> tuple[list[ExecutorTerm], dict[str, object] | None]:
    tokens = term.ordered_tokens
    for index in range(len(tokens) - 1):
        left, right = tokens[index], tokens[index + 1]
        if (
            left.endpoint_id == right.endpoint_id
            and left.derivative_kind == right.derivative_kind
            and left.spinor_component == right.spinor_component
        ):
            zero = {
                "branch_id": term.branch_id,
                "classification": "NILPOTENT_ZERO",
                "rule": f"{left.derivative_kind}_{left.spinor_component}^2=0",
                "token_ids": [left.token_id, right.token_id],
                "ledger": [
                    *term.ledger,
                    executor_ledger_entry(
                        ledger_id=f"{term.branch_id}:NILPOTENT:{index}",
                        phase="PRIMITIVE_NORMAL_ORDERING",
                        kind="NILPOTENCE",
                        factor=ONE,
                        rule_id="odd_primitive_square_zero",
                        token_ids=[left.token_id, right.token_id],
                    ),
                ],
            }
            return [], zero
        if _token_sort_key(left, endpoint_order) <= _token_sort_key(right, endpoint_order):
            continue
        swapped_tokens = tokens[:index] + (right, left) + tokens[index + 2 :]
        swap_entry = executor_ledger_entry(
            ledger_id=f"{term.branch_id}:SWAP:{index}:{len(term.ledger)}",
            phase="PRIMITIVE_NORMAL_ORDERING",
            kind="PRIMITIVE_REORDER",
            factor=MINUS_ONE,
            rule_id="odd_primitive_swap",
            token_ids=[left.token_id, right.token_id],
            details={"same_endpoint": left.endpoint_id == right.endpoint_id},
        )
        swapped = term.replace(
            polynomial=term.polynomial.scale(MINUS_ONE),
            ordered_tokens=swapped_tokens,
            ledger_entry=swap_entry,
        )
        if (
            left.endpoint_id == right.endpoint_id
            and left.derivative_kind == "D"
            and right.derivative_kind == "BAR_D"
        ):
            endpoint = endpoints[left.endpoint_id]
            momentum = _momentum_component(endpoint, left, right)
            mixed_entry = executor_ledger_entry(
                ledger_id=f"{term.branch_id}:MIXED:{index}:{len(term.ledger)}",
                phase="PRIMITIVE_NORMAL_ORDERING",
                kind="MIXED_ANTICOMMUTATOR",
                factor=MINUS_TWO_I,
                rule_id="{D_a,barD_dota}=-2*i*p_(a,dota)",
                token_ids=[left.token_id, right.token_id],
                details={
                    "endpoint_id": endpoint.endpoint_id,
                    "momentum_basis": list(endpoint.momentum_basis),
                    "momentum_coefficients": list(endpoint.momentum_coefficients),
                    "undotted": left.spinor_component,
                    "dotted": right.spinor_component,
                },
            )
            contracted = term.replace(
                polynomial=term.polynomial * momentum.scale(MINUS_TWO_I),
                ordered_tokens=tokens[:index] + tokens[index + 2 :],
                ledger_entry=mixed_entry,
            )
            return [swapped, contracted], None
        return [swapped], None
    return [term], None


def _normal_order_terms(
    terms: Sequence[ExecutorTerm], endpoints: Mapping[str, ExecutorEndpoint]
) -> tuple[list[ExecutorTerm], list[dict[str, object]]]:
    endpoint_order = {endpoint_id: index for index, endpoint_id in enumerate(endpoints)}
    queue = list(terms)
    normal: list[ExecutorTerm] = []
    zero_terms: list[dict[str, object]] = []
    steps = 0
    while queue:
        current = queue.pop(0)
        rewritten, zero = _normal_order_one_step(current, endpoints, endpoint_order)
        if zero is not None:
            zero_terms.append(zero)
            continue
        if len(rewritten) == 1 and rewritten[0] == current:
            normal.append(current)
        else:
            queue.extend(rewritten)
        steps += 1
        if steps > 10000:
            raise RuntimeError("primitive normal ordering failed to terminate")
    return normal, zero_terms


def _chirality_and_eom_classify(
    terms: Sequence[ExecutorTerm], endpoints: Mapping[str, ExecutorEndpoint]
) -> tuple[list[ExecutorTerm], list[dict[str, object]]]:
    active: list[ExecutorTerm] = []
    zero_terms: list[dict[str, object]] = []
    for term in terms:
        killed: tuple[ExecutorToken, str] | None = None
        for token in term.ordered_tokens:
            endpoint = endpoints[token.endpoint_id]
            if token.carrier != "FIELD":
                continue
            if endpoint.chirality == "CHIRAL" and token.derivative_kind == "BAR_D":
                killed = (token, "barD_on_chiral_field")
                break
            if endpoint.chirality == "ANTICHIRAL" and token.derivative_kind == "D":
                killed = (token, "D_on_antichiral_field")
                break
        if killed is not None:
            token, rule = killed
            zero_terms.append(
                {
                    "branch_id": term.branch_id,
                    "classification": "CHIRALITY_ZERO",
                    "rule": rule,
                    "token_ids": [token.token_id],
                    "ledger": [
                        *term.ledger,
                        executor_ledger_entry(
                            ledger_id=f"{term.branch_id}:CHIRALITY:{token.token_id}",
                            phase="EXTERNAL_CHIRALITY",
                            kind="CHIRALITY",
                            factor=ONE,
                            rule_id=rule,
                            token_ids=[token.token_id],
                        ),
                    ],
                }
            )
        else:
            active.append(term)
    return active, zero_terms


def _combine_terms(terms: Sequence[ExecutorTerm]) -> list[dict[str, object]]:
    groups: dict[tuple[tuple[tuple[str, str, str, str], ...], tuple[str, ...]], dict[str, object]] = {}
    for term in terms:
        token_key = tuple(
            (token.derivative_kind, token.spinor_component, token.endpoint_id, token.carrier)
            for token in term.ordered_tokens
        )
        key = token_key, tuple(sorted(term.denominator_edges))
        if key not in groups:
            groups[key] = {
                "polynomial": POLY_ZERO,
                "tokens": term.ordered_tokens,
                "denominator_edges": tuple(sorted(term.denominator_edges)),
                "provenance": [],
            }
        groups[key]["polynomial"] = groups[key]["polynomial"] + term.polynomial  # type: ignore[operator]
        groups[key]["provenance"].append(
            {"branch_id": term.branch_id, "ledger": list(term.ledger)}
        )
    return [value for _, value in sorted(groups.items()) if value["polynomial"]]


def _collapse_exact_edge_squares(
    groups: Sequence[dict[str, object]], endpoints: Mapping[str, ExecutorEndpoint]
) -> list[dict[str, object]]:
    source_by_edge = {
        endpoint.edge_id: endpoint
        for endpoint in endpoints.values()
        if endpoint.endpoint_kind == "INTERNAL_SOURCE"
    }
    output: list[dict[str, object]] = []
    for group in groups:
        polynomial = group["polynomial"]
        assert isinstance(polynomial, ExactPolynomial)
        denominators = list(group["denominator_edges"])
        collapsed: list[dict[str, object]] = []
        for edge_id in tuple(denominators):
            if edge_id not in source_by_edge:
                raise ValueError(f"denominator edge {edge_id} lacks an internal source endpoint")
            square = endpoint_square_polynomial(source_by_edge[edge_id])
            quotient = polynomial.scalar_multiple_of(square)
            if quotient is None:
                continue
            polynomial = ExactPolynomial.constant(quotient)
            denominators.remove(edge_id)
            collapsed.append(
                {
                    "edge_id": edge_id,
                    "rule": "exact_numerator_equals_scalar_times_r_square",
                    "quotient": quotient.to_json(),
                }
            )
        tokens = group["tokens"]
        assert isinstance(tokens, tuple)
        classification: list[str] = []
        if collapsed:
            classification.append("PROPAGATOR_COLLAPSE")
        if tokens:
            classification.append("D_ALGEBRA_REMAINDER")
        if not tokens and not collapsed:
            classification.append("SCALAR_REMAINDER")
        output.append(
            {
                "polynomial": polynomial.to_json(),
                "ordered_tokens": [token.to_json() for token in tokens],
                "remaining_denominator_edges": denominators,
                "collapsed_edges": collapsed,
                "classifications": classification,
                "provenance": group["provenance"],
            }
        )
    return output


def validate_global_join_key(value: Mapping[str, object]) -> dict[str, object]:
    required = {
        "parent_id",
        "parent_vertex_order",
        "ordered_local_amplitude_option_ids",
        "global_left_coefficient_word",
        "fixed_edge_pairing_order",
    }
    if set(value) != required:
        raise ValueError(f"global join key fields differ: {sorted(set(value) ^ required)}")
    vertex_order = [
        str(item) for item in _sequence(value["parent_vertex_order"], "parent vertex order")
    ]
    options = [
        str(item)
        for item in _sequence(
            value["ordered_local_amplitude_option_ids"], "ordered local option ids"
        )
    ]
    if not vertex_order or len(vertex_order) != len(options):
        raise ValueError("one ordered local option id is required per parent vertex")
    word_rows = [
        _mapping(item, "global coefficient word entry")
        for item in _sequence(value["global_left_coefficient_word"], "global coefficient word")
    ]
    if len(word_rows) != 10:
        raise ValueError("a five-edge global coefficient word must contain ten entries")
    word: list[dict[str, object]] = []
    for position, row in enumerate(word_rows):
        if set(row) != {"coefficient_id", "basis_index", "parity"}:
            raise ValueError("global coefficient word entry has undeclared fields")
        basis_index = int(row["basis_index"])
        parity = int(row["parity"])
        if not 0 <= basis_index < 16 or parity != (basis_index.bit_count() & 1):
            raise ValueError("global coefficient parity must equal popcount(basis_index) mod 2")
        word.append(
            {
                "position": position,
                "coefficient_id": str(row["coefficient_id"]),
                "basis_index": basis_index,
                "parity": parity,
            }
        )
    coefficient_ids = [str(row["coefficient_id"]) for row in word]
    if len(coefficient_ids) != len(set(coefficient_ids)):
        raise ValueError("global coefficient ids must be unique")
    edge_rows = [
        _mapping(item, "fixed edge pairing")
        for item in _sequence(value["fixed_edge_pairing_order"], "fixed edge pairing order")
    ]
    if len(edge_rows) != 5:
        raise ValueError("fixed two-loop pairing order must contain five edges")
    pairings: list[dict[str, str]] = []
    paired_ids: list[str] = []
    for row in edge_rows:
        if set(row) != {"edge_id", "source_coefficient_id", "target_coefficient_id"}:
            raise ValueError("fixed edge pairing has undeclared fields")
        source = str(row["source_coefficient_id"])
        target = str(row["target_coefficient_id"])
        if source not in coefficient_ids or target not in coefficient_ids or source == target:
            raise ValueError("fixed edge pairing references invalid coefficient ids")
        paired_ids.extend([source, target])
        pairings.append(
            {
                "edge_id": str(row["edge_id"]),
                "source_coefficient_id": source,
                "target_coefficient_id": target,
            }
        )
    if sorted(paired_ids) != sorted(coefficient_ids):
        raise ValueError("fixed five-edge pairing must use every coefficient exactly once")
    normalized = {
        "parent_id": str(value["parent_id"]),
        "parent_vertex_order": vertex_order,
        "ordered_local_amplitude_option_ids": options,
        "global_left_coefficient_word": word,
        "fixed_edge_pairing_order": pairings,
    }
    normalized["join_key_hash"] = digest(normalized)
    return normalized


def execute_edge_tagged_dalgebra(program: Mapping[str, object]) -> dict[str, object]:
    """Execute exact local D-algebra on a typed, already scope-expanded program."""

    if program.get("schema_version") != EXECUTOR_SCHEMA_VERSION:
        raise ValueError("edge-tagged executor schema version mismatch")
    if program.get("left_coefficient_order") is not True:
        raise ValueError("executor input must lock LEFT coefficient order")
    program_kind = str(program.get("program_kind", ""))
    if program_kind not in EXECUTOR_PROGRAM_KINDS:
        raise ValueError("executor program_kind must be FIXTURE or GLOBAL_NUMERATOR")
    global_join_key = None
    if program_kind == "GLOBAL_NUMERATOR":
        global_join_key = validate_global_join_key(
            _mapping(program.get("global_join_key"), "global numerator join key")
        )
    elif program.get("global_join_key") is not None:
        raise ValueError("fixture programs cannot declare a global join key")
    program_id = str(program.get("program_id", ""))
    if not program_id:
        raise ValueError("executor program id is required")
    endpoint_rows = _sequence(program.get("endpoints"), "executor endpoints")
    endpoints = {
        endpoint.endpoint_id: endpoint
        for endpoint in (
            endpoint_from_json(_mapping(row, "executor endpoint")) for row in endpoint_rows
        )
    }
    if len(endpoints) != len(endpoint_rows):
        raise ValueError("executor endpoint ids must be unique")
    branches = _sequence(program.get("branches"), "executor branches")
    terms: list[ExecutorTerm] = []
    token_ids: set[str] = set()
    for branch in branches:
        row = _mapping(branch, "executor branch")
        branch_id = str(row.get("branch_id", ""))
        if not branch_id:
            raise ValueError("executor branch id is required")
        tokens = tuple(
            token_from_json(_mapping(token, "executor token"))
            for token in _sequence(row.get("ordered_tokens"), "executor ordered tokens")
        )
        if any(token.endpoint_id not in endpoints for token in tokens):
            raise ValueError("executor token uses an unknown endpoint")
        for token in tokens:
            qualified = f"{branch_id}:{token.token_id}"
            if qualified in token_ids:
                raise ValueError("executor token ids must be unique per branch")
            token_ids.add(qualified)
        coefficient = GaussianRational.from_json(_mapping(row.get("coefficient"), "branch coefficient"))
        denominators = tuple(
            str(item)
            for item in _sequence(row.get("denominator_edges", ()), "denominator edges")
        )
        terms.append(
            ExecutorTerm(branch_id, ExactPolynomial.constant(coefficient), tokens, denominators)
        )
    transfers = [
        _mapping(item, "IBP transfer")
        for item in _sequence(program.get("ibp_transfers", ()), "IBP transfers")
    ]
    canonical_terms = [_canonicalize_delta_endpoints(term, endpoints) for term in terms]
    ibp_terms = [_apply_ibp_transfers(term, transfers, endpoints) for term in canonical_terms]
    normal_terms, nilpotent_zeros = _normal_order_terms(ibp_terms, endpoints)
    active_terms, chirality_zeros = _chirality_and_eom_classify(normal_terms, endpoints)
    groups = _combine_terms(active_terms)
    output_terms = _collapse_exact_edge_squares(groups, endpoints)
    for output in output_terms:
        token_endpoints = {
            str(token["endpoint_id"])
            for token in output["ordered_tokens"]  # type: ignore[index]
        }
        endpoint_records = [endpoints[endpoint_id] for endpoint_id in token_endpoints]
        classifications = output["classifications"]
        assert isinstance(classifications, list)
        if any(endpoint.equation_class == "EOM" for endpoint in endpoint_records):
            classifications.append("EOM_REMAINDER")
        if any(endpoint.endpoint_kind == "EXTERNAL_BACKGROUND" for endpoint in endpoint_records):
            classifications.append("EXTERNAL_BACKGROUND_DERIVATIVE")
        if any(endpoint.endpoint_kind == "COMPOSITE_SOURCE" for endpoint in endpoint_records):
            classifications.append("COMPOSITE_SOURCE_DERIVATIVE")
        output["classifications"] = sorted(set(classifications))
        output["external_derivative_tokens"] = [
            token
            for token in output["ordered_tokens"]  # type: ignore[index]
            if endpoints[str(token["endpoint_id"])].endpoint_kind
            in {"EXTERNAL_BACKGROUND", "COMPOSITE_SOURCE"}
        ]
    result = {
        "schema_version": EXECUTOR_RESULT_VERSION,
        "program_id": program_id,
        "program_kind": program_kind,
        "program_hash": digest(program),
        "global_join_key": global_join_key,
        "left_coefficient_order": True,
        "mixed_anticommutator": "{D_a,barD_dota}=-2*i*p_(a,dota)",
        "endpoint_transfer_rule": "D_target*delta=-D_source*delta",
        "ibp_rule": "integral (D F)G=-(-1)^|F| integral F(D G)",
        "terms": output_terms,
        "zero_terms": [*nilpotent_zeros, *chirality_zeros],
        "phase_execution": [
            {"phase": "SCOPE_EXPANSION", "status": "INPUT_ALREADY_EXACTLY_EXPANDED"},
            {"phase": "ENDPOINT_CANONICALIZATION", "status": "EXECUTED"},
            {"phase": "PIVOTED_IBP", "status": "EXECUTED"},
            {"phase": "PRIMITIVE_NORMAL_ORDERING", "status": "EXECUTED"},
            {"phase": "PROJECTOR_REDUCTION", "status": "NO_UNDECLARED_PROJECTOR_REWRITE"},
            {"phase": "EXTERNAL_CHIRALITY", "status": "EXECUTED"},
            {"phase": "GRASSMANN_SATURATION", "status": "CLASSIFIED_BY_EXACT_WORD"},
            {"phase": "TYPED_EDGE_COLLAPSE", "status": "EXECUTED_EXACT_R_SQUARE_ONLY"},
        ],
        "DRED_performed": False,
        "IBP_integral_reduction_performed": False,
        "UV_pole": None,
        "two_loop_coefficient": None,
    }
    result["result_hash"] = digest(result)
    return result


def _mapping(value: object, label: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value


def _sequence(value: object, label: str) -> Sequence[object]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        raise ValueError(f"{label} must be an ordered array")
    return value


def _assert_no_sampling(value: object, path: str = "oracle") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).lower()
            if normalized in FORBIDDEN_SAMPLE_KEYS:
                raise ValueError(f"numerical sampling is forbidden at {path}.{key}")
            _assert_no_sampling(child, f"{path}.{key}")
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _assert_no_sampling(child, f"{path}[{index}]")


def _canonical_polynomial(
    value: Mapping[str, object], variables: tuple[str, ...]
) -> tuple[tuple[tuple[int, ...], GaussianRational], ...]:
    terms = _sequence(value.get("terms"), "polynomial terms")
    combined: dict[tuple[int, ...], GaussianRational] = {}
    for term in terms:
        row = _mapping(term, "polynomial term")
        if set(row) != {"powers", "factor"}:
            raise ValueError("a polynomial term must contain exactly powers and factor")
        powers = _mapping(row["powers"], "monomial powers")
        if set(powers) - set(variables):
            raise ValueError(f"unknown polynomial variables: {sorted(set(powers) - set(variables))}")
        exponent = tuple(int(powers.get(variable, 0)) for variable in variables)
        if any(power < 0 for power in exponent):
            raise ValueError("polynomial exponents must be nonnegative")
        factor_value = GaussianRational.from_json(_mapping(row["factor"], "polynomial factor"))
        combined[exponent] = combined.get(exponent, GaussianRational()) + factor_value
    return tuple(sorted((powers, factor_value) for powers, factor_value in combined.items() if factor_value != GaussianRational()))


def validate_polynomial_oracle(value: Mapping[str, object]) -> dict[str, object]:
    """Verify exact coefficient identities; numerical probes are rejected."""

    _assert_no_sampling(value)
    if value.get("proof_mode") != "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY":
        raise ValueError("oracle proof_mode must be EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY")
    if value.get("coefficient_domain") != QI_DOMAIN:
        raise ValueError("oracle coefficient domain must be Q(i)")
    variables = tuple(str(item) for item in _sequence(value.get("variables"), "oracle variables"))
    if not variables or len(variables) != len(set(variables)) or any(not item for item in variables):
        raise ValueError("oracle variables must be a nonempty ordered unique array")
    identities = _sequence(value.get("identities"), "oracle identities")
    if not identities:
        raise ValueError("the exact polynomial oracle requires at least one identity")
    ids: list[str] = []
    checks: list[dict[str, object]] = []
    for identity in identities:
        row = _mapping(identity, "oracle identity")
        identity_id = str(row.get("identity_id", ""))
        if not identity_id:
            raise ValueError("every polynomial identity needs an id")
        lhs = _canonical_polynomial(_mapping(row.get("lhs"), "identity lhs"), variables)
        rhs = _canonical_polynomial(_mapping(row.get("rhs"), "identity rhs"), variables)
        if lhs != rhs:
            raise ValueError(f"exact polynomial identity fails: {identity_id}")
        ids.append(identity_id)
        checks.append(
            {
                "identity_id": identity_id,
                "method": "EXACT_MONOMIAL_COEFFICIENT_COMPARISON",
                "passed": True,
                "canonical_identity_hash": digest(
                    {
                        "variables": variables,
                        "lhs": [([*powers], factor_value.to_json()) for powers, factor_value in lhs],
                        "rhs": [([*powers], factor_value.to_json()) for powers, factor_value in rhs],
                    }
                ),
            }
        )
    if len(ids) != len(set(ids)):
        raise ValueError("polynomial oracle identity ids must be unique")
    return {
        "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
        "coefficient_domain": QI_DOMAIN,
        "variables": list(variables),
        "identity_ids": ids,
        "checks": checks,
        "numerical_sampling_used": False,
    }


def lexicographically_decreases(before: Sequence[int], after: Sequence[int]) -> bool:
    if len(before) != len(MEASURE_COMPONENTS) or len(after) != len(MEASURE_COMPONENTS):
        raise ValueError("termination measures have the wrong arity")
    if any(not isinstance(value, int) or value < 0 for value in (*before, *after)):
        raise ValueError("termination measures must lie in N^8")
    return tuple(after) < tuple(before)


def phase_measure_decreases(
    phase: str, before: Sequence[int], after: Sequence[int]
) -> bool:
    """Check the stronger phase-local lexicographic rewrite obligation."""

    if phase not in PHASE_ORDER:
        raise ValueError(f"unknown phase: {phase}")
    if not lexicographically_decreases(before, after):
        return False
    component = PHASE_ORDER.index(phase)
    return tuple(before[:component]) == tuple(after[:component]) and after[component] < before[component]


def termination_contract() -> dict[str, object]:
    return {
        "order": "LEXICOGRAPHIC_ON_N8",
        "components": list(MEASURE_COMPONENTS),
        "phase_component": dict(zip(PHASE_ORDER, MEASURE_COMPONENTS)),
        "rewrite_obligation": (
            "every applied rewrite must strictly lower the full lexicographic tuple; "
            "all earlier components must remain unchanged"
        ),
        "unchecked_transition_status": "REJECTED_MISSING_EXACT_BEFORE_AFTER_MEASURES",
    }


def _edge_by_id(graph: Mapping[str, object]) -> dict[str, Mapping[str, object]]:
    edges = [_mapping(edge, "internal edge") for edge in _sequence(graph["internal_edges"], "internal edges")]
    result = {str(edge["edge_id"]): edge for edge in edges}
    if len(result) != len(edges):
        raise ValueError("internal edge ids must be unique")
    return result


def theta_decomposition(graph: Mapping[str, object]) -> dict[str, object]:
    """Return a deterministic rooted spanning tree for literal K4 minus one edge."""

    if graph.get("topology") != "K4_MINUS_ONE_EDGE":
        raise ValueError("DWordIR accepts only literal K4_MINUS_ONE_EDGE topology objects")
    vertices = [_mapping(vertex, "vertex") for vertex in _sequence(graph["vertices"], "vertices")]
    edges = list(_edge_by_id(graph).values())
    if len(vertices) != 4 or len(edges) != 5:
        raise ValueError("literal K4 minus one edge must have V=4 and I=5")
    vertex_ids = {str(vertex["vertex_id"]) for vertex in vertices}
    degrees = {vertex_id: 0 for vertex_id in vertex_ids}
    pair_to_edge: dict[frozenset[str], Mapping[str, object]] = {}
    for edge in edges:
        pair = frozenset((str(edge["source"]), str(edge["target"])))
        if len(pair) != 2 or pair in pair_to_edge:
            raise ValueError("literal K4 minus one edge must be a simple graph")
        pair_to_edge[pair] = edge
        for vertex_id in pair:
            degrees[vertex_id] += 1
    if sorted(degrees.values()) != [2, 2, 3, 3]:
        raise ValueError("literal K4 minus one edge degree sequence must be (3,3,2,2)")
    poles = tuple(sorted(vertex_id for vertex_id, degree in degrees.items() if degree == 3))
    waist = tuple(sorted(vertex_id for vertex_id, degree in degrees.items() if degree == 2))
    central = pair_to_edge.get(frozenset(poles))
    if central is None:
        raise ValueError("the two degree-three theta poles must have a unique central edge")
    insertion = [str(vertex["vertex_id"]) for vertex in vertices if vertex["role"] == "COMPOSITE_INSERTION"]
    if len(insertion) != 1:
        raise ValueError("theta scheduler requires one composite-insertion root")
    root = insertion[0]
    anchor = root if root in poles else poles[0]
    tree_edge_ids = {str(central["edge_id"])}
    for vertex_id in waist:
        edge = pair_to_edge.get(frozenset((anchor, vertex_id)))
        if edge is None:
            raise ValueError("each degree-two theta vertex must attach to the anchor pole")
        tree_edge_ids.add(str(edge["edge_id"]))
    if len(tree_edge_ids) != 3:
        raise ValueError("theta spanning tree must have V-1 edges")
    chord_ids = sorted(set(_edge_by_id(graph)) - tree_edge_ids)
    if len(chord_ids) != 2:
        raise ValueError("a two-loop theta decomposition must have two chords")

    tree_adjacency: dict[str, list[tuple[str, str]]] = {vertex_id: [] for vertex_id in vertex_ids}
    edge_map = _edge_by_id(graph)
    for edge_id in tree_edge_ids:
        edge = edge_map[edge_id]
        source, target = str(edge["source"]), str(edge["target"])
        tree_adjacency[source].append((target, edge_id))
        tree_adjacency[target].append((source, edge_id))

    def tree_path(source: str, target: str) -> tuple[list[str], list[str]]:
        frontier: list[tuple[str, list[str], list[str]]] = [(source, [source], [])]
        visited: set[str] = set()
        while frontier:
            vertex_id, vertices_path, edges_path = frontier.pop(0)
            if vertex_id == target:
                return vertices_path, edges_path
            if vertex_id in visited:
                continue
            visited.add(vertex_id)
            for neighbor, edge_id in sorted(tree_adjacency[vertex_id]):
                if neighbor not in visited:
                    frontier.append((neighbor, vertices_path + [neighbor], edges_path + [edge_id]))
        raise ValueError("spanning-tree path does not exist")

    cycles: list[dict[str, object]] = []
    for chord_id in chord_ids:
        chord = edge_map[chord_id]
        vertices_path, edges_path = tree_path(str(chord["source"]), str(chord["target"]))
        cycles.append(
            {
                "chord_edge_id": chord_id,
                "tree_vertex_path": vertices_path,
                "tree_edge_path": edges_path,
                "fundamental_cycle_edge_ids": sorted([chord_id, *edges_path]),
            }
        )
    return {
        "root_vertex_id": root,
        "theta_pole_vertex_ids": list(poles),
        "degree_two_vertex_ids": list(waist),
        "anchor_pole_vertex_id": anchor,
        "central_edge_id": str(central["edge_id"]),
        "central_endpoint_ports": [str(central["source_port"]), str(central["target_port"])],
        "spanning_tree_edge_ids": sorted(tree_edge_ids),
        "chord_edge_ids": chord_ids,
        "fundamental_cycles": cycles,
        "cycle_rank_certificate": {"I_minus_V_plus_1": 2, "chord_count": 2, "passed": True},
    }


def central_critical_pairs(theta: Mapping[str, object]) -> list[dict[str, object]]:
    edge_id = str(theta["central_edge_id"])
    endpoints = [str(item) for item in theta["central_endpoint_ports"]]
    phase_pairs = (
        ("SCOPE_EXPANSION", "ENDPOINT_CANONICALIZATION", "scope_endpoint_overlap"),
        ("ENDPOINT_CANONICALIZATION", "PIVOTED_IBP", "endpoint_pivot_overlap"),
        ("PIVOTED_IBP", "PRIMITIVE_NORMAL_ORDERING", "pivot_primitive_overlap"),
        ("PROJECTOR_REDUCTION", "TYPED_EDGE_COLLAPSE", "projector_collapse_overlap"),
    )
    return [
        {
            "critical_pair_id": f"{edge_id}:{label}:{endpoint}",
            "central_edge_id": edge_id,
            "central_endpoint_port_id": endpoint,
            "left_phase": left,
            "right_phase": right,
            "overlap_class": label,
            "status": "DECLARED_UNJOINED_UNTIL_EXACT_WORD_INPUT",
            "required_certificate": {
                "same_input_word_hash": None,
                "left_normal_form_hash": None,
                "right_normal_form_hash": None,
                "exact_ledger_product_equal_in_Q_i": None,
                "polynomial_oracle_identity_id": None,
            },
        }
        for left, right, label in phase_pairs
        for endpoint in endpoints
    ]


def _required_paths(graph: Mapping[str, object]) -> tuple[str, ...]:
    edge_ids = sorted(_edge_by_id(graph))
    paths = [
        "wick_record.schema_version",
        "wick_record.graph_id",
        "wick_record.graph_hash",
        "wick_record.notation_schema_hash",
        "wick_record.wick_complete",
        "wick_record.wick_pairings",
        "wick_record.wick_completeness_certificate",
        "wick_record.ordered_derivative_scope_ast",
        "wick_record.exact_sign_koszul_ledger",
        "wick_record.polynomial_oracle",
    ]
    paths.extend(f"wick_record.propagator_kernels[{edge_id}]" for edge_id in edge_ids)
    return tuple(paths)


def deterministic_missing_inputs(
    graph: Mapping[str, object], record: Mapping[str, object] | None
) -> tuple[str, ...]:
    if record is None:
        return tuple(sorted(_required_paths(graph)))
    missing: list[str] = []
    for key in (
        "schema_version",
        "graph_id",
        "graph_hash",
        "notation_schema_hash",
        "wick_complete",
        "wick_pairings",
        "wick_completeness_certificate",
        "ordered_derivative_scope_ast",
        "exact_sign_koszul_ledger",
        "polynomial_oracle",
    ):
        if key not in record:
            missing.append(f"wick_record.{key}")
    kernels = record.get("propagator_kernels")
    kernels_by_id: set[str] = set()
    if isinstance(kernels, Sequence) and not isinstance(kernels, (str, bytes, bytearray)):
        for kernel in kernels:
            if isinstance(kernel, Mapping) and "edge_id" in kernel:
                kernels_by_id.add(str(kernel["edge_id"]))
    for edge_id in sorted(_edge_by_id(graph)):
        if edge_id not in kernels_by_id:
            missing.append(f"wick_record.propagator_kernels[{edge_id}]")
    return tuple(sorted(missing))


def _momentum_payload(graph: Mapping[str, object], edge: Mapping[str, object], sign: int) -> dict[str, object]:
    if sign not in (-1, 1):
        raise ValueError("endpoint momentum orientation must be +1 or -1")
    basis = [str(item) for item in graph["momentum_contract"]["basis"]]  # type: ignore[index]
    vector = [sign * int(item) for item in edge["momentum_vector"]]  # type: ignore[index]
    return {
        "basis": basis,
        "coefficients": vector,
        "orientation_sign_from_edge": sign,
        "space": graph["momentum_contract"]["square_space"],  # type: ignore[index]
    }


def validate_derivative_token(
    value: Mapping[str, object], graph: Mapping[str, object]
) -> dict[str, object]:
    required = {
        "token_id",
        "derivative_kind",
        "spinor_index_space",
        "spinor_indices",
        "operator_parity",
        "edge_id",
        "endpoint_port_id",
        "momentum",
    }
    if not required <= set(value):
        raise ValueError(f"derivative token misses {sorted(required - set(value))}")
    kind = str(value["derivative_kind"])
    if kind not in DERIVATIVE_KINDS:
        raise ValueError(f"unknown derivative kind: {kind}")
    index_space, parity, arity = DERIVATIVE_KINDS[kind]
    indices = [str(item) for item in _sequence(value["spinor_indices"], "spinor indices")]
    if str(value["spinor_index_space"]) != index_space or int(value["operator_parity"]) != parity:
        raise ValueError("derivative index space or parity disagrees with its kind")
    if len(indices) != arity or any(not index for index in indices):
        raise ValueError("derivative spinor-index arity is not explicit")
    edge_id = str(value["edge_id"])
    edge = _edge_by_id(graph).get(edge_id)
    if edge is None:
        raise ValueError(f"derivative token uses unknown edge: {edge_id}")
    endpoint = str(value["endpoint_port_id"])
    endpoints = {str(edge["source_port"]), str(edge["target_port"])}
    if endpoint not in endpoints:
        raise ValueError(f"derivative endpoint {endpoint} is not on edge {edge_id}")
    momentum = _mapping(value["momentum"], "typed momentum")
    sign = int(momentum.get("orientation_sign_from_edge", 0))
    expected_momentum = _momentum_payload(graph, edge, sign)
    if dict(momentum) != expected_momentum:
        raise ValueError("derivative momentum must be an exact oriented copy of the edge momentum")
    return {
        "token_id": str(value["token_id"]),
        "derivative_kind": kind,
        "spinor_index_space": index_space,
        "spinor_indices": indices,
        "operator_parity": parity,
        "edge_id": edge_id,
        "endpoint_port_id": endpoint,
        "momentum": expected_momentum,
    }


def validate_scope_ast(
    value: Mapping[str, object], graph: Mapping[str, object]
) -> tuple[dict[str, object], tuple[str, ...]]:
    """Validate an ordered AST without manufacturing any missing scope."""

    token_ids: list[str] = []
    known_ports = {
        str(edge[endpoint])
        for edge in _edge_by_id(graph).values()
        for endpoint in ("source_port", "target_port")
    }
    known_ports.update(
        str(port["port_id"])
        for vertex in _sequence(graph["vertices"], "vertices")
        for port in _sequence(_mapping(vertex, "vertex").get("background_ports", ()), "background ports")
    )

    def visit(node: Mapping[str, object], path: tuple[int, ...]) -> dict[str, object]:
        node_type = str(node.get("node_type", ""))
        if node_type == "FIELD_PORT":
            required = {"node_type", "port_id", "field_type", "parity"}
            if set(node) != required or int(node["parity"]) not in (0, 1):
                raise ValueError(f"invalid FIELD_PORT at AST path {path}")
            if str(node["port_id"]) not in known_ports:
                raise ValueError(f"unknown FIELD_PORT at AST path {path}: {node['port_id']}")
            return {
                "node_type": node_type,
                "port_id": str(node["port_id"]),
                "field_type": str(node["field_type"]),
                "parity": int(node["parity"]),
            }
        if node_type in {"ORDERED_SCOPE", "ORDERED_PRODUCT"}:
            children = _sequence(node.get("ordered_children"), f"{node_type} children")
            if not children:
                raise ValueError(f"{node_type} at AST path {path} is empty")
            result: dict[str, object] = {
                "node_type": node_type,
                "ordered_children": [
                    visit(_mapping(child, "scope child"), path + (index,))
                    for index, child in enumerate(children)
                ],
            }
            if node_type == "ORDERED_SCOPE":
                scope_id = str(node.get("scope_id", ""))
                if not scope_id:
                    raise ValueError(f"ORDERED_SCOPE at AST path {path} needs a scope id")
                result["scope_id"] = scope_id
            elif set(node) != {"node_type", "ordered_children"}:
                raise ValueError(f"ORDERED_PRODUCT at AST path {path} has undeclared fields")
            return result
        if node_type == "DERIVATIVE_APPLICATION":
            if set(node) != {"node_type", "token", "argument"}:
                raise ValueError(f"invalid DERIVATIVE_APPLICATION at AST path {path}")
            token = validate_derivative_token(_mapping(node["token"], "derivative token"), graph)
            token_ids.append(str(token["token_id"]))
            return {
                "node_type": node_type,
                "token": token,
                "argument": visit(_mapping(node["argument"], "derivative argument"), path + (0,)),
            }
        if node_type == "LINEAR_COMBINATION":
            terms = _sequence(node.get("ordered_terms"), "linear-combination terms")
            if not terms:
                raise ValueError(f"LINEAR_COMBINATION at AST path {path} is empty")
            result_terms: list[dict[str, object]] = []
            for index, term in enumerate(terms):
                row = _mapping(term, "linear-combination term")
                if set(row) != {"factor", "expression"}:
                    raise ValueError("linear-combination term must contain factor and expression")
                result_terms.append(
                    {
                        "factor": GaussianRational.from_json(_mapping(row["factor"], "term factor")).to_json(),
                        "expression": visit(_mapping(row["expression"], "term expression"), path + (index,)),
                    }
                )
            return {"node_type": node_type, "ordered_terms": result_terms}
        raise ValueError(f"unknown ordered derivative-scope AST node {node_type!r} at path {path}")

    normalized = visit(value, ())
    if len(token_ids) != len(set(token_ids)):
        raise ValueError("derivative token ids must be unique in the scope AST")
    return normalized, tuple(token_ids)


def _validate_wick_completeness(
    record: Mapping[str, object], graph: Mapping[str, object]
) -> list[dict[str, object]]:
    if record.get("wick_complete") is not True:
        raise ValueError("wick_complete must be true")
    edge_map = _edge_by_id(graph)
    pairings = _sequence(record["wick_pairings"], "Wick pairings")
    normalized: list[dict[str, object]] = []
    for pairing in pairings:
        row = _mapping(pairing, "Wick pairing")
        edge_id = str(row.get("edge_id", ""))
        if edge_id not in edge_map:
            raise ValueError(f"Wick pairing uses unknown edge: {edge_id}")
        edge = edge_map[edge_id]
        endpoint_ports = [str(item) for item in _sequence(row.get("endpoint_ports"), "pairing endpoints")]
        if sorted(endpoint_ports) != sorted((str(edge["source_port"]), str(edge["target_port"]))):
            raise ValueError(f"Wick pairing endpoints disagree on edge {edge_id}")
        field_types = [str(item) for item in _sequence(row.get("ordered_field_types"), "pairing fields")]
        if len(field_types) != 2 or any(not item for item in field_types):
            raise ValueError("each Wick pairing needs two ordered field types")
        normalized.append(
            {"edge_id": edge_id, "endpoint_ports": endpoint_ports, "ordered_field_types": field_types}
        )
    if sorted(row["edge_id"] for row in normalized) != sorted(edge_map):
        raise ValueError("Wick-complete record must pair every internal edge exactly once")
    certificate = _mapping(record["wick_completeness_certificate"], "Wick completeness certificate")
    required_true = {
        "every_quantum_port_used_once": True,
        "connected": True,
        "pairing_edge_ids_equal_graph_edge_ids": True,
    }
    if any(certificate.get(key) is not expected for key, expected in required_true.items()):
        raise ValueError("Wick completeness certificate is not affirmative")
    return sorted(normalized, key=lambda row: str(row["edge_id"]))


def _validate_kernels(
    kernels: Sequence[object], graph: Mapping[str, object], oracle_ids: set[str]
) -> tuple[list[dict[str, object]], tuple[str, ...]]:
    edge_map = _edge_by_id(graph)
    normalized: list[dict[str, object]] = []
    token_ids: list[str] = []
    for kernel in kernels:
        row = _mapping(kernel, "propagator kernel")
        edge_id = str(row.get("edge_id", ""))
        if edge_id not in edge_map:
            raise ValueError(f"propagator kernel uses unknown edge: {edge_id}")
        edge = edge_map[edge_id]
        endpoints = [str(item) for item in _sequence(row.get("endpoint_ports"), "kernel endpoints")]
        if endpoints != [str(edge["source_port"]), str(edge["target_port"])]:
            raise ValueError(f"kernel endpoint order disagrees with oriented edge {edge_id}")
        kernel_ast = _mapping(row.get("ordered_kernel_ast"), "ordered kernel AST")
        if kernel_ast.get("node_type") != "ORDERED_PROPAGATOR_KERNEL":
            raise ValueError("kernel AST must be ORDERED_PROPAGATOR_KERNEL")
        word = _sequence(kernel_ast.get("ordered_derivative_tokens"), "kernel derivative word")
        normalized_word = [
            validate_derivative_token(_mapping(token, "kernel derivative token"), graph)
            for token in word
        ]
        if any(token["edge_id"] != edge_id for token in normalized_word):
            raise ValueError("every kernel derivative token must remain on its kernel edge")
        token_ids.extend(str(token["token_id"]) for token in normalized_word)
        if not isinstance(kernel_ast.get("grassmann_delta_ast"), Mapping):
            raise ValueError("kernel requires an explicit Grassmann-delta AST")
        if not isinstance(kernel_ast.get("scalar_denominator_ast"), Mapping):
            raise ValueError("kernel requires an explicit scalar-denominator AST")
        identity_ids = [str(item) for item in _sequence(row.get("oracle_identity_ids"), "kernel oracle ids")]
        if not identity_ids or not set(identity_ids) <= oracle_ids:
            raise ValueError("every kernel must cite known exact polynomial identities")
        normalized.append(
            {
                "edge_id": edge_id,
                "endpoint_ports": endpoints,
                "ordered_field_types": [
                    str(item) for item in _sequence(row.get("ordered_field_types"), "kernel field types")
                ],
                "ordered_kernel_ast": {
                    "node_type": "ORDERED_PROPAGATOR_KERNEL",
                    "ordered_derivative_tokens": normalized_word,
                    "grassmann_delta_ast": dict(kernel_ast["grassmann_delta_ast"]),
                    "scalar_denominator_ast": dict(kernel_ast["scalar_denominator_ast"]),
                },
                "oracle_identity_ids": identity_ids,
            }
        )
    if sorted(row["edge_id"] for row in normalized) != sorted(edge_map):
        raise ValueError("there must be exactly one propagator kernel per internal edge")
    if len(token_ids) != len(set(token_ids)):
        raise ValueError("kernel derivative token ids must be globally unique")
    return sorted(normalized, key=lambda row: str(row["edge_id"])), tuple(token_ids)


def compile_schedule_contract(
    graph: Mapping[str, object], record: Mapping[str, object] | None
) -> dict[str, object]:
    """Validate complete input and emit only a pending phase schedule."""

    theta = theta_decomposition(graph)
    missing = deterministic_missing_inputs(graph, record)
    if missing:
        return {
            "status": BLOCKED_STATUS,
            "graph_id": graph["graph_id"],
            "graph_hash": graph["graph_hash"],
            "missing_inputs": list(missing),
            "phase_order": list(PHASE_ORDER),
            "theta_decomposition": theta,
            "critical_pairs": central_critical_pairs(theta),
            "global_confluence_claimed": False,
            "phase_execution": None,
        }
    assert record is not None
    if record["schema_version"] != INPUT_SCHEMA_VERSION:
        raise ValueError("Wick input schema version mismatch")
    if record["graph_id"] != graph["graph_id"] or record["graph_hash"] != graph["graph_hash"]:
        raise ValueError("Wick input graph binding mismatch")
    notation_hash = str(record["notation_schema_hash"])
    if len(notation_hash) != 64 or any(character not in "0123456789abcdef" for character in notation_hash):
        raise ValueError("notation_schema_hash must be a lowercase SHA-256 digest")
    pairings = _validate_wick_completeness(record, graph)
    oracle = validate_polynomial_oracle(_mapping(record["polynomial_oracle"], "polynomial oracle"))
    scope_ast, scope_token_ids = validate_scope_ast(
        _mapping(record["ordered_derivative_scope_ast"], "ordered derivative-scope AST"), graph
    )
    kernels, kernel_token_ids = _validate_kernels(
        _sequence(record["propagator_kernels"], "propagator kernels"),
        graph,
        set(str(item) for item in oracle["identity_ids"]),
    )
    if set(scope_token_ids) & set(kernel_token_ids):
        raise ValueError("scope and kernel derivative token ids must be disjoint")
    ledger = [
        ExactLedgerEntry.from_json(_mapping(item, "ledger entry"))
        for item in _sequence(record["exact_sign_koszul_ledger"], "exact sign/Koszul ledger")
    ]
    if len({entry.ledger_id for entry in ledger}) != len(ledger):
        raise ValueError("ledger ids must be unique")
    known_token_ids = set(scope_token_ids) | set(kernel_token_ids)
    if any(not set(entry.token_ids) <= known_token_ids for entry in ledger):
        raise ValueError("ledger entry references an unknown derivative token")
    oracle_ids = set(str(item) for item in oracle["identity_ids"])
    if any(
        entry.oracle_identity_id is not None and entry.oracle_identity_id not in oracle_ids
        for entry in ledger
    ):
        raise ValueError("ledger entry references an unknown exact polynomial identity")
    phases = [
        {
            "phase": phase,
            "status": "PENDING_EXACT_REWRITE_EXECUTION",
            "required_measure_component": MEASURE_COMPONENTS[index],
            "before_measure": None,
            "after_measure": None,
            "applied_rewrites": None,
        }
        for index, phase in enumerate(PHASE_ORDER)
    ]
    normalized_input = {
        "schema_version": INPUT_SCHEMA_VERSION,
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "notation_schema_hash": notation_hash,
        "wick_complete": True,
        "wick_pairings": pairings,
        "ordered_derivative_scope_ast": scope_ast,
        "propagator_kernels": kernels,
        "exact_sign_koszul_ledger": [entry.to_json() for entry in ledger],
        "polynomial_oracle_certificate": oracle,
    }
    return {
        "status": READY_STATUS,
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "notation_schema_hash": notation_hash,
        "normalized_input_hash": digest(normalized_input),
        "phase_order": list(PHASE_ORDER),
        "termination_measure": termination_contract(),
        "theta_decomposition": theta,
        "critical_pairs": central_critical_pairs(theta),
        "global_confluence_claimed": False,
        "exact_sign_koszul_ledger": [entry.to_json() for entry in ledger],
        "polynomial_oracle_certificate": oracle,
        "phase_execution": phases,
        "evaluated_word": None,
    }


def input_schema_contract(graph: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema_version": INPUT_SCHEMA_VERSION,
        "graph_binding": {
            "graph_id": graph["graph_id"],
            "graph_hash": graph["graph_hash"],
            "topology": "K4_MINUS_ONE_EDGE",
        },
        "required_paths": list(_required_paths(graph)),
        "derivative_token": {
            "required_fields": [
                "token_id",
                "derivative_kind",
                "spinor_index_space",
                "spinor_indices",
                "operator_parity",
                "edge_id",
                "endpoint_port_id",
                "momentum",
            ],
            "kinds": {
                kind: {"spinor_index_space": data[0], "parity": data[1], "index_arity": data[2]}
                for kind, data in DERIVATIVE_KINDS.items()
            },
            "momentum_rule": "exact oriented edge momentum; orientation_sign_from_edge is +1 or -1",
        },
        "ordered_scope_ast_nodes": [
            "ORDERED_SCOPE",
            "ORDERED_PRODUCT",
            "DERIVATIVE_APPLICATION",
            "LINEAR_COMBINATION",
            "FIELD_PORT",
        ],
        "propagator_kernel": {
            "one_per_edge": sorted(_edge_by_id(graph)),
            "kernel_node_type": "ORDERED_PROPAGATOR_KERNEL",
            "explicit_fields": [
                "ordered_derivative_tokens",
                "grassmann_delta_ast",
                "scalar_denominator_ast",
                "oracle_identity_ids",
            ],
        },
        "exact_scalar_domain": QI_DOMAIN,
        "polynomial_oracle_gate": {
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "method": "EXACT_MONOMIAL_COEFFICIENT_COMPARISON",
            "forbidden_sampling_keys": sorted(FORBIDDEN_SAMPLE_KEYS),
        },
    }


def graph_executor_endpoints(graph: Mapping[str, object]) -> list[dict[str, object]]:
    basis = tuple(str(item) for item in graph["momentum_contract"]["basis"])  # type: ignore[index]
    endpoints: list[ExecutorEndpoint] = []
    for edge in _edge_by_id(graph).values():
        vector = tuple(int(item) for item in edge["momentum_vector"])  # type: ignore[index]
        endpoints.extend(
            [
                ExecutorEndpoint(
                    str(edge["source_port"]),
                    "INTERNAL_SOURCE",
                    0,
                    "NONE",
                    "ORDINARY",
                    basis,
                    vector,
                    str(edge["edge_id"]),
                    str(edge["target_port"]),
                ),
                ExecutorEndpoint(
                    str(edge["target_port"]),
                    "INTERNAL_TARGET",
                    0,
                    "NONE",
                    "ORDINARY",
                    basis,
                    tuple(-item for item in vector),
                    str(edge["edge_id"]),
                    str(edge["source_port"]),
                ),
            ]
        )
    for vertex in _sequence(graph["vertices"], "vertices"):
        row = _mapping(vertex, "vertex")
        injections = {
            str(injection["momentum"]): tuple(int(item) for item in injection["momentum_vector"])
            for injection in _sequence(row.get("momentum_injections", ()), "momentum injections")
        }
        for port in _sequence(row.get("background_ports", ()), "background ports"):
            port_row = _mapping(port, "background port")
            momentum_label = str(port_row["momentum"])
            endpoints.append(
                ExecutorEndpoint(
                    str(port_row["port_id"]),
                    "EXTERNAL_BACKGROUND",
                    0,
                    "NONE",
                    "ORDINARY",
                    basis,
                    injections[momentum_label],
                )
            )
        for injection in _sequence(row.get("momentum_injections", ()), "momentum injections"):
            injection_row = _mapping(injection, "momentum injection")
            if injection_row.get("kind") == "COMPOSITE_SOURCE_MOMENTUM":
                endpoints.append(
                    ExecutorEndpoint(
                        f"{row['vertex_id']}.composite_source",
                        "COMPOSITE_SOURCE",
                        0,
                        "NONE",
                        "EOM",
                        basis,
                        tuple(int(item) for item in injection_row["momentum_vector"]),
                    )
                )
    ids = [endpoint.endpoint_id for endpoint in endpoints]
    if len(ids) != len(set(ids)):
        raise ValueError("graph executor endpoint ids are not unique")
    return [endpoint.to_json() for endpoint in endpoints]


def executor_program_schema() -> dict[str, object]:
    return {
        "schema_version": EXECUTOR_SCHEMA_VERSION,
        "left_coefficient_order": True,
        "required_program_fields": [
            "schema_version",
            "program_id",
            "program_kind",
            "left_coefficient_order",
            "endpoints",
            "branches",
            "ibp_transfers",
        ],
        "endpoint_kinds": sorted(ENDPOINT_KINDS),
        "endpoint_fields": [
            "endpoint_id",
            "endpoint_kind",
            "parity",
            "chirality",
            "equation_class",
            "momentum",
            "edge_id",
            "paired_endpoint_id",
        ],
        "primitive_token_fields": [
            "token_id",
            "derivative_kind",
            "spinor_component",
            "endpoint_id",
            "carrier",
        ],
        "primitive_kinds": {"D": sorted(UNDOTTED_COMPONENTS), "BAR_D": sorted(DOTTED_COMPONENTS)},
        "carriers": sorted(TOKEN_CARRIERS),
        "exact_rules": {
            "graded_IBP": "integral (D F)G=-(-1)^|F| integral F(D G)",
            "delta_endpoint_transfer": "D_target*delta=-D_source*delta",
            "mixed_anticommutator": "{D_a,barD_dota}=-2*i*p_(a,dota)",
            "nilpotence": "D_a^2=barD_dota^2=0",
            "chirality": "barD*Phi=0; D*TildePhi=0",
            "edge_collapse": "exact numerator polynomial c*r^2 divided by r^2 gives c",
        },
        "typed_output": [
            "polynomial",
            "ordered_tokens",
            "external_derivative_tokens",
            "remaining_denominator_edges",
            "collapsed_edges",
            "classifications",
            "provenance",
        ],
        "global_numerator_interface": "one result per exact global left coefficient word and fixed Wick pairing",
        "program_kinds": sorted(EXECUTOR_PROGRAM_KINDS),
        "global_join_key_fields": [
            "parent_id",
            "parent_vertex_order",
            "ordered_local_amplitude_option_ids",
            "global_left_coefficient_word",
            "fixed_edge_pairing_order",
        ],
    }


def _token_json(
    token_id: str,
    derivative_kind: str,
    spinor_component: str,
    endpoint_id: str,
    carrier: str,
) -> dict[str, object]:
    return ExecutorToken(
        token_id, derivative_kind, spinor_component, endpoint_id, carrier
    ).to_json()


def exact_executor_fixtures(graph: Mapping[str, object]) -> dict[str, object]:
    basis = list(graph["momentum_contract"]["basis"])  # type: ignore[index]
    edge = _edge_by_id(graph)[sorted(_edge_by_id(graph))[0]]
    source = str(edge["source_port"])
    target = str(edge["target_port"])
    edge_id = str(edge["edge_id"])
    graph_endpoints = graph_executor_endpoints(graph)

    ibp_endpoints = [
        ExecutorEndpoint(
            "fixture.background",
            "EXTERNAL_BACKGROUND",
            0,
            "NONE",
            "ORDINARY",
            tuple(basis),
            (0, 0, 0, 1, 0),
        ).to_json(),
        ExecutorEndpoint(
            "fixture.composite",
            "COMPOSITE_SOURCE",
            1,
            "NONE",
            "EOM",
            tuple(basis),
            (0, 0, 1, 0, 0),
        ).to_json(),
        ExecutorEndpoint(
            "fixture.odd_external",
            "EXTERNAL_BACKGROUND",
            1,
            "NONE",
            "ORDINARY",
            tuple(basis),
            (0, 0, 0, 0, 1),
        ).to_json(),
    ]
    ibp_program = {
        "schema_version": EXECUTOR_SCHEMA_VERSION,
        "program_id": "FIXTURE_GRADED_IBP_EXTERNAL_TO_COMPOSITE",
        "program_kind": "FIXTURE",
        "left_coefficient_order": True,
        "endpoints": ibp_endpoints,
        "branches": [
            {
                "branch_id": "ibp_even_source",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("ibp_D", "D", "+", "fixture.background", "FIELD")
                ],
                "denominator_edges": [],
            },
            {
                "branch_id": "ibp_odd_source",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("ibp_D_odd", "D", "-", "fixture.odd_external", "FIELD")
                ],
                "denominator_edges": [],
            }
        ],
        "ibp_transfers": [
            {
                "branch_id": "ibp_even_source",
                "token_id": "ibp_D",
                "from_endpoint_id": "fixture.background",
                "to_endpoint_id": "fixture.composite",
                "crossed_endpoint_ids": ["fixture.background"],
            },
            {
                "branch_id": "ibp_odd_source",
                "token_id": "ibp_D_odd",
                "from_endpoint_id": "fixture.odd_external",
                "to_endpoint_id": "fixture.composite",
                "crossed_endpoint_ids": ["fixture.odd_external"],
            }
        ],
    }

    endpoint_program = {
        "schema_version": EXECUTOR_SCHEMA_VERSION,
        "program_id": "FIXTURE_INTERNAL_TARGET_TRANSFER_AND_MIXED_MOMENTUM",
        "program_kind": "FIXTURE",
        "left_coefficient_order": True,
        "endpoints": graph_endpoints,
        "branches": [
            {
                "branch_id": "target_mixed",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("target_D", "D", "+", target, "PROPAGATOR_DELTA"),
                    _token_json("target_barD", "BAR_D", "dot+", target, "PROPAGATOR_DELTA"),
                ],
                "denominator_edges": [],
            }
        ],
        "ibp_transfers": [],
    }

    collapse_program = {
        "schema_version": EXECUTOR_SCHEMA_VERSION,
        "program_id": "FIXTURE_EXACT_R_SQUARE_PROPAGATOR_COLLAPSE",
        "program_kind": "FIXTURE",
        "left_coefficient_order": True,
        "endpoints": graph_endpoints,
        "branches": [
            {
                "branch_id": "determinant_diagonal",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("a_Dp", "D", "+", source, "PROPAGATOR_DELTA"),
                    _token_json("a_Bp", "BAR_D", "dot+", source, "PROPAGATOR_DELTA"),
                    _token_json("a_Dm", "D", "-", source, "PROPAGATOR_DELTA"),
                    _token_json("a_Bm", "BAR_D", "dot-", source, "PROPAGATOR_DELTA"),
                ],
                "denominator_edges": [edge_id],
            },
            {
                "branch_id": "determinant_off_diagonal",
                "coefficient": MINUS_ONE.to_json(),
                "ordered_tokens": [
                    _token_json("b_Dp", "D", "+", source, "PROPAGATOR_DELTA"),
                    _token_json("b_Bm", "BAR_D", "dot-", source, "PROPAGATOR_DELTA"),
                    _token_json("b_Dm", "D", "-", source, "PROPAGATOR_DELTA"),
                    _token_json("b_Bp", "BAR_D", "dot+", source, "PROPAGATOR_DELTA"),
                ],
                "denominator_edges": [edge_id],
            },
        ],
        "ibp_transfers": [],
    }

    classification_endpoints = [
        ExecutorEndpoint(
            "fixture.chiral", "EXTERNAL_BACKGROUND", 0, "CHIRAL", "ORDINARY", tuple(basis), (0, 0, 0, 1, 0)
        ).to_json(),
        ExecutorEndpoint(
            "fixture.antichiral", "EXTERNAL_BACKGROUND", 0, "ANTICHIRAL", "ORDINARY", tuple(basis), (0, 0, 0, 0, 1)
        ).to_json(),
        ExecutorEndpoint(
            "fixture.eom", "COMPOSITE_SOURCE", 0, "NONE", "EOM", tuple(basis), (0, 0, 1, 0, 0)
        ).to_json(),
        ExecutorEndpoint(
            "fixture.ordinary", "EXTERNAL_BACKGROUND", 0, "NONE", "ORDINARY", tuple(basis), (0, 0, 0, 1, 0)
        ).to_json(),
    ]
    classification_program = {
        "schema_version": EXECUTOR_SCHEMA_VERSION,
        "program_id": "FIXTURE_NILPOTENCE_CHIRALITY_EOM",
        "program_kind": "FIXTURE",
        "left_coefficient_order": True,
        "endpoints": classification_endpoints,
        "branches": [
            {
                "branch_id": "barD_chiral_zero",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("bar_ch", "BAR_D", "dot+", "fixture.chiral", "FIELD")
                ],
                "denominator_edges": [],
            },
            {
                "branch_id": "D_antichiral_zero",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("D_ach", "D", "+", "fixture.antichiral", "FIELD")
                ],
                "denominator_edges": [],
            },
            {
                "branch_id": "eom_remainder",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("D_eom", "D", "-", "fixture.eom", "FIELD")
                ],
                "denominator_edges": [],
            },
            {
                "branch_id": "nilpotent_zero",
                "coefficient": ONE.to_json(),
                "ordered_tokens": [
                    _token_json("D_nil_1", "D", "+", "fixture.ordinary", "FIELD"),
                    _token_json("D_nil_2", "D", "+", "fixture.ordinary", "FIELD"),
                ],
                "denominator_edges": [],
            },
        ],
        "ibp_transfers": [],
    }

    programs = [ibp_program, endpoint_program, collapse_program, classification_program]
    results = [execute_edge_tagged_dalgebra(program) for program in programs]
    return {
        "graph_id": graph["graph_id"],
        "programs": programs,
        "results": results,
        "fixture_hash": digest(results),
    }


def build_payload() -> dict[str, object]:
    graph_bundle = build_bundle()
    graphs = graph_bundle["literal_direct_graphs"]
    contracts = [compile_schedule_contract(graph, None) for graph in graphs]
    schemas = [input_schema_contract(graph) for graph in graphs]
    fixtures = exact_executor_fixtures(graphs[0])
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "scope": "LITERAL_K4_MINUS_EDGE_SCHEDULER_PLUS_EXACT_EDGE_TAGGED_EXECUTOR",
        "external_result_used_as_calculation_input": False,
        "phase_order": list(PHASE_ORDER),
        "termination_measure": termination_contract(),
        "exact_scalar_domain": QI_DOMAIN,
        "polynomial_oracle_requirement": {
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "numerical_sampling_admissible": False,
        },
        "graph_contracts": contracts,
        "input_schemas": schemas,
        "global_confluence_claimed": False,
        "physical_derivative_scopes_inferred": False,
        "phase_execution_performed": False,
        "exact_fixture_execution_performed": True,
        "edge_tagged_executor_schema": executor_program_schema(),
        "edge_tagged_executor_fixtures": fixtures,
        "physical_global_numerator_execution": "BLOCKED_MISSING_EXACT_GLOBAL_WORD_INPUT",
        "DRED_performed": False,
        "IBP_integral_reduction_performed": False,
        "UV_pole": None,
        "two_loop_coefficient": None,
    }
    payload["payload_hash"] = digest({key: value for key, value in payload.items() if key != "payload_hash"})
    return payload


def exact_checks(payload: Mapping[str, object]) -> dict[str, bool]:
    contracts = payload["graph_contracts"]  # type: ignore[index]

    def keys(value: object) -> set[str]:
        if isinstance(value, Mapping):
            return {str(key) for key in value} | set().union(*(keys(child) for child in value.values()))
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            return set().union(*(keys(child) for child in value))
        return set()

    forbidden_result_keys = {
        "d_algebra_row_count",
        "numerator",
        "uv_pole",
        "renormalized_pole",
        "anomaly_coefficient",
        "local_coefficient",
    }
    fixture_results = payload["edge_tagged_executor_fixtures"]["results"]  # type: ignore[index]
    collapse_result = next(
        result
        for result in fixture_results
        if result["program_id"] == "FIXTURE_EXACT_R_SQUARE_PROPAGATOR_COLLAPSE"
    )
    classification_result = next(
        result
        for result in fixture_results
        if result["program_id"] == "FIXTURE_NILPOTENCE_CHIRALITY_EOM"
    )
    ibp_result = next(
        result
        for result in fixture_results
        if result["program_id"] == "FIXTURE_GRADED_IBP_EXTERNAL_TO_COMPOSITE"
    )
    endpoint_result = next(
        result
        for result in fixture_results
        if result["program_id"] == "FIXTURE_INTERNAL_TARGET_TRANSFER_AND_MIXED_MOMENTUM"
    )
    checks = {
        "proposal_status": payload["status"] == STATUS,
        "phase_order_exact": tuple(payload["phase_order"]) == PHASE_ORDER,  # type: ignore[arg-type]
        "termination_components_exact": tuple(payload["termination_measure"]["components"]) == MEASURE_COMPONENTS,  # type: ignore[index]
        "literal_graph_set_nonempty": bool(contracts),
        "all_inputs_are_literal_k4_minus_edge": all(
            contract["theta_decomposition"]["cycle_rank_certificate"]["passed"]  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "all_real_graph_attempts_fail_closed": all(contract["status"] == BLOCKED_STATUS for contract in contracts),  # type: ignore[union-attr]
        "all_missing_lists_deterministic": all(
            contract["missing_inputs"] == sorted(contract["missing_inputs"]) for contract in contracts  # type: ignore[union-attr]
        ),
        "all_theta_cycle_rank_two": all(
            contract["theta_decomposition"]["cycle_rank_certificate"] == {  # type: ignore[union-attr]
                "I_minus_V_plus_1": 2,
                "chord_count": 2,
                "passed": True,
            }
            for contract in contracts  # type: ignore[union-attr]
        ),
        "all_theta_trees_have_three_edges_two_chords": all(
            len(contract["theta_decomposition"]["spanning_tree_edge_ids"]) == 3  # type: ignore[union-attr]
            and len(contract["theta_decomposition"]["chord_edge_ids"]) == 2  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "central_critical_pairs_declared_unjoined": all(
            contract["critical_pairs"]  # type: ignore[union-attr]
            and all(pair["status"] == "DECLARED_UNJOINED_UNTIL_EXACT_WORD_INPUT" for pair in contract["critical_pairs"])  # type: ignore[union-attr]
            for contract in contracts  # type: ignore[union-attr]
        ),
        "no_global_confluence_claim": payload["global_confluence_claimed"] is False,
        "no_scope_inference": payload["physical_derivative_scopes_inferred"] is False,
        "no_phase_execution": payload["phase_execution_performed"] is False,
        "exact_fixture_execution": payload["exact_fixture_execution_performed"] is True,
        "left_coefficient_order_locked": all(
            result["left_coefficient_order"] is True for result in fixture_results
        ),
        "graded_ibp_fixture_executes": any(
            "COMPOSITE_SOURCE_DERIVATIVE" in term["classifications"]
            and "EOM_REMAINDER" in term["classifications"]
            for term in ibp_result["terms"]
        ),
        "internal_endpoint_transfer_and_mixed_momentum_execute": any(
            any(
                ledger["kind"] == "MIXED_ANTICOMMUTATOR"
                for provenance in term["provenance"]
                for ledger in provenance["ledger"]
            )
            for term in endpoint_result["terms"]
        ),
        "nilpotence_chirality_eom_classified": {
            zero["classification"] for zero in classification_result["zero_terms"]
        }
        == {"NILPOTENT_ZERO", "CHIRALITY_ZERO"}
        and any("EOM_REMAINDER" in term["classifications"] for term in classification_result["terms"]),
        "exact_propagator_collapse_executes": any(
            "PROPAGATOR_COLLAPSE" in term["classifications"]
            and any(edge["quotient"] == (MINUS_ONE * 4).to_json() for edge in term["collapsed_edges"])
            for term in collapse_result["terms"]
        ),
        "external_tokens_are_retained": any(
            term["external_derivative_tokens"] for term in ibp_result["terms"]
        ),
        "global_numerator_join_api_is_typed": payload["edge_tagged_executor_schema"][
            "global_join_key_fields"
        ]
        == [
            "parent_id",
            "parent_vertex_order",
            "ordered_local_amplitude_option_ids",
            "global_left_coefficient_word",
            "fixed_edge_pairing_order",
        ]
        and payload["physical_global_numerator_execution"]
        == "BLOCKED_MISSING_EXACT_GLOBAL_WORD_INPUT",
        "polynomial_oracle_is_symbolic_gate": payload["polynomial_oracle_requirement"] == {  # type: ignore[index]
            "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
            "numerical_sampling_admissible": False,
        },
        "no_evaluated_physical_result_fields": not (keys(payload) & forbidden_result_keys),
        "payload_hash_recomputes": payload["payload_hash"] == digest(
            {key: value for key, value in payload.items() if key != "payload_hash"}
        ),
        "no_DRED_IBP_pole_or_coefficient": payload["DRED_performed"] is False
        and payload["IBP_integral_reduction_performed"] is False
        and payload["UV_pole"] is None
        and payload["two_loop_coefficient"] is None,
    }
    return checks


def build_audit(payload: Mapping[str, object]) -> dict[str, object]:
    checks = exact_checks(payload)
    failures = sorted(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "step6.two_loop_dword.audit.v1",
        "status": "PASS" if not failures else "FAIL",
        "proposal_status": STATUS,
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
    }


def render_markdown(payload: Mapping[str, object]) -> str:
    lines = [
        "# Step 6 — literal $K_4\\setminus e$ edge-tagged D-algebra executor",
        "",
        f"`{STATUS}`",
        "",
        "$$",
        "\\mathsf{Scope}\\to\\mathsf{Endpoint}\\to\\mathsf{IBP}\\to\\mathsf{Primitive}",
        "\\to\\mathsf{Projector}\\to\\mathsf{Chirality}\\to\\mathsf{Saturation}",
        "\\to\\mathsf{Collapse}.",
        "$$",
        "",
        "$$",
        "\\mu=(n_{\\rm scope},n_{\\rm endpoint},n_{\\rm pivot},n_{\\rm inv},",
        "n_{\\rm proj},n_{\\rm chir},n_{\\rm sat},n_{\\rm coll})\\in\\mathbb N^8,",
        "\\qquad \\mu_{j+1}<_{\\rm lex}\\mu_j.",
        "$$",
        "",
    ]
    for contract in payload["graph_contracts"]:  # type: ignore[index]
        theta = contract["theta_decomposition"]
        lines.extend(
            [
                f"## `{contract['graph_id']}`",
                "",
                "$$",
                f"e_c={theta['central_edge_id']},\\qquad "
                f"T=\\{{{','.join(theta['spanning_tree_edge_ids'])}\\}},\\qquad "
                f"C=\\{{{','.join(theta['chord_edge_ids'])}\\}}.",
                "$$",
                "",
                f"`{contract['status']}`",
                "",
            ]
        )
    lines.extend(
        [
            "Exact input domain: `Q(i)`.",
            "",
            "Polynomial gate: `EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY`; numerical samples are rejected.",
            "",
            "## Exact edge-tagged executor fixtures",
            "",
            "$$",
            "\\int (D F)G=-(-1)^{|F|}\\int F(DG),\\qquad",
            "D^{(t)}\\delta=-D^{(s)}\\delta,",
            "$$",
            "",
            "$$",
            "D_a\\bar D_{\\dot a}=-\\bar D_{\\dot a}D_a-2ip_{a\\dot a}.",
            "$$",
            "",
            "$$",
            "D_a^2=\\bar D_{\\dot a}^2=0,\\qquad",
            "\\bar D_{\\dot a}\\Phi=0,\\qquad D_a\\widetilde\\Phi=0.",
            "$$",
            "",
            f"Executed fixtures: `{len(payload['edge_tagged_executor_fixtures']['results'])}`.",  # type: ignore[index]
            "",
            "Physical global numerator: `BLOCKED_MISSING_EXACT_GLOBAL_WORD_INPUT`.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, object], dict[str, object]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise RuntimeError(f"Step-6 DWordIR audit failed: {audit['failures']}")
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_CONTRACT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GENERATED_SCHEMA.write_text(
        json.dumps(
            {
                "schema_version": INPUT_SCHEMA_VERSION,
                "graph_schemas": payload["input_schemas"],
                "edge_tagged_executor_program_schema": payload["edge_tagged_executor_schema"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload), encoding="utf-8")
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "proposal_status": payload["status"],
                "graph_contract_count": len(payload["graph_contracts"]),
                "failed": audit["failed"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
