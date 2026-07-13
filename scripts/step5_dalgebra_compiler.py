#!/usr/bin/env python3
"""Deterministic, edge-tagged flat-superspace D-algebra compiler.

Operator words are written from left to right and the rightmost operator acts
first.  Numerical coefficients lie in Q(i); momentum factors remain typed
tokens.  This module contains no graph or anomaly coefficient.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction
from typing import Callable, Iterable, Sequence, TypeAlias


@dataclass(frozen=True, order=True)
class GaussianRational:
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

    def __rsub__(self, other: object) -> "GaussianRational":
        return gaussian(other) - self

    def __mul__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        return GaussianRational(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "GaussianRational":
        rhs = gaussian(other)
        denominator = rhs.re * rhs.re + rhs.im * rhs.im
        if denominator == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return GaussianRational(
            (self.re * rhs.re + self.im * rhs.im) / denominator,
            (self.im * rhs.re - self.re * rhs.im) / denominator,
        )

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def to_json(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im)}


def gaussian(value: object) -> GaussianRational:
    if isinstance(value, GaussianRational):
        return value
    if isinstance(value, Fraction):
        return GaussianRational(value)
    if isinstance(value, int):
        return GaussianRational(Fraction(value))
    raise TypeError(f"not an exact Gaussian-rational scalar: {value!r}")


ZERO = GaussianRational()
ONE = gaussian(1)
I = GaussianRational(Fraction(0), Fraction(1))


class Chirality(str, Enum):
    GENERAL = "GENERAL"
    CHIRAL = "CHIRAL"
    ANTICHIRAL = "ANTICHIRAL"


class LedgerKind(str, Enum):
    IBP = "IBP"
    KOSZUL = "KOSZUL"
    ALGEBRA = "ALGEBRA"
    CHIRALITY = "CHIRALITY"
    COLLAPSE = "COLLAPSE"


IMPLEMENTATION_STATUS = "PARTIAL_DECLARED_PHASES_ONLY"
IMPLEMENTED_PHASES = (
    "EXACT_LOCAL_OPERATOR_NORMALIZATION",
    "SINGLE_OPERATOR_EXTERNAL_CHIRALITY",
    "TYPED_PROPAGATOR_COLLAPSE",
)
ENDPOINT_TRANSFER_POLICY = "EXPLICIT_API_ONLY_NEVER_INVOKED_BY_COMPILE"


class UnimplementedPhaseSequenceError(ValueError):
    code = "UNIMPLEMENTED_PHASE_SEQUENCE"

    def __init__(
        self,
        message: str,
        *,
        leg_id: str,
        operator_types: tuple[str, ...],
    ) -> None:
        super().__init__(message)
        self.leg_id = leg_id
        self.operator_types = operator_types

    def to_json(self) -> dict[str, object]:
        return {
            "code": self.code,
            "message": str(self),
            "leg_id": self.leg_id,
            "operator_types": list(self.operator_types),
            "required_order": [
                "MIXED_D_BARD_NORMALIZATION",
                "EXTERNAL_CHIRALITY",
            ],
        }


@dataclass(frozen=True, order=True)
class EndpointTag:
    edge_id: str
    endpoint: str


@dataclass(frozen=True)
class D:
    index: str
    tag: EndpointTag
    momentum: str


@dataclass(frozen=True)
class BarD:
    index: str
    tag: EndpointTag
    momentum: str


@dataclass(frozen=True)
class D2:
    tag: EndpointTag
    momentum: str


@dataclass(frozen=True)
class BarD2:
    tag: EndpointTag
    momentum: str


@dataclass(frozen=True)
class MixedMomentum:
    undotted: str
    dotted: str
    tag: EndpointTag
    momentum: str
    fourier_factor: GaussianRational = I


@dataclass(frozen=True)
class MomentumSquare:
    tag: EndpointTag
    momentum: str


@dataclass(frozen=True)
class ExternalLeg:
    leg_id: str
    chirality: Chirality
    parity: int
    tag: EndpointTag


@dataclass(frozen=True)
class ExternalDerivative:
    leg_id: str
    derivative_kind: str
    tag: EndpointTag
    momentum: str
    undotted: str | None = None
    dotted: str | None = None


@dataclass(frozen=True)
class Propagator:
    edge_id: str
    momentum: str


@dataclass(frozen=True)
class Collapse:
    edge_id: str
    momentum: str
    reason: str


Token: TypeAlias = (
    D
    | BarD
    | D2
    | BarD2
    | MixedMomentum
    | MomentumSquare
    | ExternalLeg
    | ExternalDerivative
    | Propagator
    | Collapse
)


@dataclass(frozen=True)
class EdgeDeclaration:
    edge_id: str
    endpoints: tuple[str, ...]
    momentum: str

    def to_json(self) -> dict[str, object]:
        return {
            "edge_id": self.edge_id,
            "endpoints": list(self.endpoints),
            "momentum": self.momentum,
        }


@dataclass(frozen=True)
class LegDeclaration:
    leg_id: str
    chirality: Chirality
    parity: int
    tag: EndpointTag

    def to_json(self) -> dict[str, object]:
        return {
            "leg_id": self.leg_id,
            "chirality": self.chirality.value,
            "parity": self.parity,
            "tag": tag_to_json(self.tag),
        }


@dataclass(frozen=True)
class PropagatorDeclaration:
    edge_id: str
    momentum: str
    propagator_type: str

    def to_json(self) -> dict[str, str]:
        return {
            "edge_id": self.edge_id,
            "momentum": self.momentum,
            "propagator_type": self.propagator_type,
        }


@dataclass(frozen=True)
class SignLedgerEntry:
    kind: LedgerKind
    factor: GaussianRational
    rule: str
    operator: str
    source_tag: EndpointTag | None = None
    target_tag: EndpointTag | None = None
    crossed_parities: tuple[int, ...] = ()

    def to_json(self) -> dict[str, object]:
        return {
            "kind": self.kind.value,
            "factor": self.factor.to_json(),
            "rule": self.rule,
            "operator": self.operator,
            "source_tag": tag_to_json(self.source_tag),
            "target_tag": tag_to_json(self.target_tag),
            "crossed_parities": list(self.crossed_parities),
        }


@dataclass(frozen=True)
class Term:
    coefficient: GaussianRational | Fraction | int
    word: tuple[Token, ...]
    sign_ledger: tuple[SignLedgerEntry, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "coefficient", gaussian(self.coefficient))

    def scaled(
        self, factor: GaussianRational | Fraction | int, entry: SignLedgerEntry
    ) -> "Term":
        exact = gaussian(factor)
        return Term(exact * self.coefficient, self.word, self.sign_ledger + (entry,))


@dataclass(frozen=True)
class RewriteChoice:
    rule_id: str
    positions: tuple[int, ...]
    priority: int

    @property
    def span(self) -> tuple[int, int]:
        return min(self.positions), max(self.positions) + 1


@dataclass(frozen=True)
class RewriteStep:
    rule_id: str
    positions: tuple[int, ...]
    input_term: Term
    output_terms: tuple[Term, ...]
    measure_before: tuple[int, int]
    measures_after: tuple[tuple[int, int], ...]

    def to_json(self) -> dict[str, object]:
        return {
            "rule_id": self.rule_id,
            "positions": list(self.positions),
            "measure_before": list(self.measure_before),
            "measures_after": [list(value) for value in self.measures_after],
            "input": term_to_json(self.input_term),
            "outputs": [term_to_json(term) for term in self.output_terms],
        }


@dataclass(frozen=True)
class NormalFormTerm:
    coefficient: GaussianRational
    word: tuple[Token, ...]
    provenance_ledgers: tuple[tuple[SignLedgerEntry, ...], ...]

    def to_json(self) -> dict[str, object]:
        return {
            "coefficient": self.coefficient.to_json(),
            "word": [token_to_json(token) for token in self.word],
            "provenance_ledgers": [
                [entry.to_json() for entry in ledger]
                for ledger in self.provenance_ledgers
            ],
        }


@dataclass(frozen=True)
class NormalFormTrace:
    inputs: tuple[Term, ...]
    steps: tuple[RewriteStep, ...]
    outputs: tuple[NormalFormTerm, ...]
    terminated: bool
    ordering: tuple[str, ...]
    implementation_status: str = IMPLEMENTATION_STATUS
    implemented_phases: tuple[str, ...] = IMPLEMENTED_PHASES
    endpoint_transfer_policy: str = ENDPOINT_TRANSFER_POLICY

    def to_json(self) -> dict[str, object]:
        return {
            "schema": 1,
            "arithmetic": "EXACT_Q_I",
            "operator_order": "RIGHTMOST_ACTS_FIRST",
            "ordering": list(self.ordering),
            "implementation_status": self.implementation_status,
            "implemented_phases": list(self.implemented_phases),
            "endpoint_transfer_policy": self.endpoint_transfer_policy,
            "terminated": self.terminated,
            "inputs": [term_to_json(term) for term in self.inputs],
            "steps": [step.to_json() for step in self.steps],
            "outputs": [term.to_json() for term in self.outputs],
        }

    def deterministic_json(self) -> str:
        return json.dumps(self.to_json(), indent=2, sort_keys=True) + "\n"


def _is_sha256(value: str) -> bool:
    return len(value) == 64 and all(character in "0123456789abcdef" for character in value)


@dataclass(frozen=True)
class DAlgebraJob:
    job_id: str
    notation_hash: str
    graph_hash: str | None
    amplitude_id: str | None
    coefficient: GaussianRational
    edges: tuple[EdgeDeclaration, ...]
    legs: tuple[LegDeclaration, ...]
    propagators: tuple[PropagatorDeclaration, ...]
    operator_word: tuple[Token, ...]
    schema: int = 1

    def __post_init__(self) -> None:
        object.__setattr__(self, "coefficient", gaussian(self.coefficient))
        self.validate()

    def validate(self) -> None:
        if self.schema != 1:
            raise ValueError(f"unsupported DAlgebraJob schema: {self.schema}")
        if not self.job_id:
            raise ValueError("job_id is required")
        if not _is_sha256(self.notation_hash):
            raise ValueError("notation_hash must be a lowercase SHA-256")
        if self.graph_hash is not None and not _is_sha256(self.graph_hash):
            raise ValueError("graph_hash must be null or a lowercase SHA-256")
        if self.graph_hash is None and not self.amplitude_id:
            raise ValueError("either graph_hash or amplitude_id is required")

        edge_map = {edge.edge_id: edge for edge in self.edges}
        if len(edge_map) != len(self.edges):
            raise ValueError("edge declarations must have unique edge_id values")
        declared_tags: set[EndpointTag] = set()
        for edge in self.edges:
            if not edge.edge_id or not edge.momentum or not edge.endpoints:
                raise ValueError("every edge needs id, momentum, and at least one endpoint")
            if len(set(edge.endpoints)) != len(edge.endpoints):
                raise ValueError(f"edge {edge.edge_id} repeats an endpoint")
            declared_tags.update(EndpointTag(edge.edge_id, endpoint) for endpoint in edge.endpoints)

        leg_map = {leg.leg_id: leg for leg in self.legs}
        if len(leg_map) != len(self.legs):
            raise ValueError("leg declarations must have unique leg_id values")
        for leg in self.legs:
            if leg.parity not in {0, 1}:
                raise ValueError(f"leg {leg.leg_id} parity must be 0 or 1")
            if leg.tag not in declared_tags:
                raise ValueError(f"leg {leg.leg_id} uses an unknown endpoint tag")

        propagator_map = {propagator.edge_id: propagator for propagator in self.propagators}
        if len(propagator_map) != len(self.propagators):
            raise ValueError("propagator declarations must have unique edge_id values")
        for propagator in self.propagators:
            edge = edge_map.get(propagator.edge_id)
            if edge is None:
                raise ValueError(f"propagator uses unknown edge {propagator.edge_id}")
            if propagator.momentum != edge.momentum:
                raise ValueError(f"propagator momentum disagrees on edge {propagator.edge_id}")

        for token in self.operator_word:
            tag = getattr(token, "tag", None)
            if tag is not None:
                if tag not in declared_tags:
                    raise ValueError(f"operator token uses unknown endpoint tag {tag}")
                edge = edge_map[tag.edge_id]
                momentum = getattr(token, "momentum", edge.momentum)
                if momentum != edge.momentum:
                    raise ValueError(f"operator momentum disagrees on edge {edge.edge_id}")
            if isinstance(token, (ExternalLeg, ExternalDerivative)):
                declaration = leg_map.get(token.leg_id)
                if declaration is None:
                    raise ValueError(f"operator word uses unknown leg {token.leg_id}")
                if token.tag != declaration.tag:
                    raise ValueError(f"leg {token.leg_id} endpoint tag disagrees")
                if isinstance(token, ExternalLeg) and (
                    token.chirality != declaration.chirality
                    or token.parity != declaration.parity
                ):
                    raise ValueError(f"leg {token.leg_id} chirality/parity disagrees")
            if isinstance(token, Propagator):
                declaration = propagator_map.get(token.edge_id)
                if declaration is None:
                    raise ValueError(f"operator word uses undeclared propagator {token.edge_id}")
                if token.momentum != declaration.momentum:
                    raise ValueError(f"propagator token momentum disagrees on {token.edge_id}")
            if isinstance(token, Collapse) and token.edge_id not in edge_map:
                raise ValueError(f"collapse token uses unknown edge {token.edge_id}")

    def to_json(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "job_id": self.job_id,
            "notation_hash": self.notation_hash,
            "graph_hash": self.graph_hash,
            "amplitude_id": self.amplitude_id,
            "coefficient": self.coefficient.to_json(),
            "edges": [edge.to_json() for edge in self.edges],
            "legs": [leg.to_json() for leg in self.legs],
            "propagators": [propagator.to_json() for propagator in self.propagators],
            "operator_word": [token_to_json(token) for token in self.operator_word],
        }

    def canonical_json(self) -> str:
        return json.dumps(self.to_json(), sort_keys=True, separators=(",", ":")) + "\n"

    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_json().encode("utf-8")).hexdigest()

    @classmethod
    def from_json(cls, data: object) -> "DAlgebraJob":
        required = {
            "schema",
            "job_id",
            "notation_hash",
            "graph_hash",
            "amplitude_id",
            "coefficient",
            "edges",
            "legs",
            "propagators",
            "operator_word",
        }
        if not isinstance(data, dict) or set(data) != required:
            keys = sorted(data) if isinstance(data, dict) else []
            raise ValueError(f"DAlgebraJob keys are {keys}; expected {sorted(required)}")

        def declaration(item: object, keys: set[str], kind: str) -> dict[str, object]:
            if not isinstance(item, dict) or set(item) != keys:
                actual = sorted(item) if isinstance(item, dict) else []
                raise ValueError(f"{kind} keys are {actual}; expected {sorted(keys)}")
            return item

        edges = tuple(
            EdgeDeclaration(
                str(checked["edge_id"]),
                tuple(str(endpoint) for endpoint in checked["endpoints"]),
                str(checked["momentum"]),
            )
            for checked in (
                declaration(item, {"edge_id", "endpoints", "momentum"}, "edge")
                for item in data["edges"]
            )
        )
        legs = tuple(
            LegDeclaration(
                str(checked["leg_id"]),
                Chirality(str(checked["chirality"])),
                int(checked["parity"]),
                endpoint_tag_from_json(checked["tag"]),
            )
            for checked in (
                declaration(item, {"leg_id", "chirality", "parity", "tag"}, "leg")
                for item in data["legs"]
            )
        )
        propagators = tuple(
            PropagatorDeclaration(
                str(checked["edge_id"]),
                str(checked["momentum"]),
                str(checked["propagator_type"]),
            )
            for checked in (
                declaration(
                    item,
                    {"edge_id", "momentum", "propagator_type"},
                    "propagator",
                )
                for item in data["propagators"]
            )
        )
        return cls(
            job_id=str(data["job_id"]),
            notation_hash=str(data["notation_hash"]),
            graph_hash=None if data["graph_hash"] is None else str(data["graph_hash"]),
            amplitude_id=None if data["amplitude_id"] is None else str(data["amplitude_id"]),
            coefficient=gaussian_from_json(data["coefficient"]),
            edges=edges,
            legs=legs,
            propagators=propagators,
            operator_word=tuple(token_from_json(item) for item in data["operator_word"]),
            schema=int(data["schema"]),
        )


@dataclass(frozen=True)
class CriticalPairAudit:
    source: Term
    left_choice: RewriteChoice
    right_choice: RewriteChoice
    left_normal_form: tuple[tuple[str, tuple[str, str]], ...]
    right_normal_form: tuple[tuple[str, tuple[str, str]], ...]
    joinable: bool

    def to_json(self) -> dict[str, object]:
        return {
            "source": term_to_json(self.source),
            "left": {
                "rule": self.left_choice.rule_id,
                "positions": list(self.left_choice.positions),
                "normal_form": list(self.left_normal_form),
            },
            "right": {
                "rule": self.right_choice.rule_id,
                "positions": list(self.right_choice.positions),
                "normal_form": list(self.right_normal_form),
            },
            "joinable": self.joinable,
        }


DECLARED_CRITICAL_PAIR_SCOPE = (
    "DECLARED_FINITE_CRITICAL_PAIR_SUITE_NOT_GLOBAL_CONFLUENCE"
)


@dataclass(frozen=True)
class DAlgebraResult:
    job_id: str
    notation_hash: str
    graph_hash: str | None
    amplitude_id: str | None
    input_job_sha256: str
    normal_form: NormalFormTrace | None
    critical_pair_audits: tuple[CriticalPairAudit, ...]
    status: str
    error: dict[str, object] | None = None
    schema: int = 1
    critical_pair_scope: str = DECLARED_CRITICAL_PAIR_SCOPE
    implementation_status: str = IMPLEMENTATION_STATUS
    implemented_phases: tuple[str, ...] = IMPLEMENTED_PHASES
    endpoint_transfer_policy: str = ENDPOINT_TRANSFER_POLICY

    def to_json(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "job_id": self.job_id,
            "notation_hash": self.notation_hash,
            "graph_hash": self.graph_hash,
            "amplitude_id": self.amplitude_id,
            "input_job_sha256": self.input_job_sha256,
            "status": self.status,
            "error": self.error,
            "implementation_status": self.implementation_status,
            "implemented_phases": list(self.implemented_phases),
            "endpoint_transfer_policy": self.endpoint_transfer_policy,
            "critical_pair_scope": self.critical_pair_scope,
            "critical_pair_audits": [
                audit.to_json() for audit in self.critical_pair_audits
            ],
            "normal_form": None if self.normal_form is None else self.normal_form.to_json(),
        }

    def canonical_json(self) -> str:
        return json.dumps(self.to_json(), sort_keys=True, separators=(",", ":")) + "\n"


SCHEDULED_WW_PHASES = (
    "SCOPE_EXPANSION",
    "ENDPOINT_CANONICALIZATION",
    "PIVOTED_IBP",
    "PRIMITIVE_NORMAL_ORDERING",
    "PROJECTOR_REDUCTION",
    "EXTERNAL_CHIRALITY",
    "GRASSMANN_SATURATION",
    "TYPED_EDGE_COLLAPSE",
)
SCHEDULED_WW_SCOPE = "PHYSICAL_WW_TRIANGLE_ONLY_FAIL_CLOSED_ELSEWHERE"


class UnsupportedScheduledWWGraphError(ValueError):
    code = "UNSUPPORTED_SCHEDULED_WW_GRAPH"


@dataclass(frozen=True)
class ScheduledWWAlgebraCertificate:
    notation_hash: str
    k_plus_coefficient: GaussianRational
    dminus_dplus_coefficient: GaussianRational
    dminus_kplus_coefficient: GaussianRational
    closed_delta_coefficient: GaussianRational
    mixed_reordering_coefficient: GaussianRational
    mixed_momentum_coefficient: GaussianRational
    ordered_mixed_factor: GaussianRational
    matrix_probe_momenta: tuple[tuple[int, int, int, int], ...]
    matrix_checks: tuple[tuple[str, bool], ...]

    def __post_init__(self) -> None:
        if not _is_sha256(self.notation_hash):
            raise ValueError("scheduled WW algebra certificate needs a notation hash")
        if not self.matrix_checks or not all(value for _, value in self.matrix_checks):
            failed = [name for name, value in self.matrix_checks if not value]
            raise UnsupportedScheduledWWGraphError(
                "the exact 16x16 scheduled WW matrix oracle did not pass: "
                + ",".join(failed)
            )

    def evidence_json(self) -> dict[str, object]:
        return {
            "notation_hash": self.notation_hash,
            "notation_rule_coefficients": {
                "K_plus": self.k_plus_coefficient.to_json(),
                "Dminus_Dplus": self.dminus_dplus_coefficient.to_json(),
                "Dminus_Kplus": self.dminus_kplus_coefficient.to_json(),
                "closed_D2_barD2_delta": self.closed_delta_coefficient.to_json(),
                "mixed_reordering": self.mixed_reordering_coefficient.to_json(),
                "mixed_momentum": self.mixed_momentum_coefficient.to_json(),
                "ordered_mixed_factor": self.ordered_mixed_factor.to_json(),
            },
            "matrix_representation": "EXACT_16_BY_16_EXTERIOR_ALGEBRA_Q_I",
            "matrix_probe_momenta": [list(momentum) for momentum in self.matrix_probe_momenta],
            "matrix_checks": dict(self.matrix_checks),
        }

    def sha256(self) -> str:
        canonical = json.dumps(
            self.evidence_json(), sort_keys=True, separators=(",", ":")
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def to_json(self) -> dict[str, object]:
        return {
            **self.evidence_json(),
            "status": "PASS_NOTATION_AND_EXACT_16X16_ORACLE",
            "certificate_sha256": self.sha256(),
        }


def _qi_from_notation(value: object) -> GaussianRational:
    if not hasattr(value, "real") or not hasattr(value, "imag"):
        raise UnsupportedScheduledWWGraphError("notation coefficient is not in Q(i)")
    return GaussianRational(Fraction(value.real), Fraction(value.imag))  # type: ignore[arg-type]


def _notation_derivative_rule(notation_schema: object, lhs: tuple[str, ...]) -> object:
    matches = [
        rule
        for rule in notation_schema.derivative_rules  # type: ignore[attr-defined]
        if tuple(rule.lhs) == lhs
    ]
    if len(matches) != 1:
        raise UnsupportedScheduledWWGraphError(
            f"notation has no unique derivative rule {lhs}"
        )
    return matches[0]


def build_scheduled_ww_algebra_certificate(
    notation_schema: object,
    matrix_oracle: object,
) -> ScheduledWWAlgebraCertificate:
    """Bind the narrow WW constants to notation rules and exact matrices."""

    k_rule = _notation_derivative_rule(notation_schema, ("K_+",))
    d_pair_rule = _notation_derivative_rule(notation_schema, ("D_-", "D_+"))
    d_k_rule = _notation_derivative_rule(notation_schema, ("D_-", "K_+"))
    mixed_rule = _notation_derivative_rule(
        notation_schema, ("D_a", "barD_dot_alpha")
    )
    closed_rule = _notation_derivative_rule(notation_schema, ("D2", "barD2"))
    if len(k_rule.rhs) != 1 or tuple(k_rule.rhs[0].ordered_derivatives) != (
        "D_+",
        "barD2",
        "D_+",
    ):
        raise UnsupportedScheduledWWGraphError("notation K_plus rule has drifted")
    if len(d_pair_rule.rhs) != 1 or tuple(d_pair_rule.rhs[0].ordered_derivatives) != (
        "D2",
    ):
        raise UnsupportedScheduledWWGraphError("notation Dminus-Dplus rule has drifted")
    if len(d_k_rule.rhs) != 1 or tuple(d_k_rule.rhs[0].ordered_derivatives) != (
        "D2",
        "barD2",
        "D_+",
    ):
        raise UnsupportedScheduledWWGraphError("notation Dminus-Kplus rule has drifted")
    if len(closed_rule.rhs) != 1 or tuple(closed_rule.rhs[0].tensor_factors) != (
        "delta4theta",
    ):
        raise UnsupportedScheduledWWGraphError("notation closed-delta rule has drifted")
    if len(mixed_rule.rhs) != 2:
        raise UnsupportedScheduledWWGraphError("notation mixed rule has drifted")
    reordered = next(
        (
            term
            for term in mixed_rule.rhs
            if tuple(term.ordered_derivatives) == ("barD_dot_alpha", "D_a")
            and not term.symbol_factors
        ),
        None,
    )
    momentum = next(
        (
            term
            for term in mixed_rule.rhs
            if not term.ordered_derivatives and tuple(term.symbol_factors) == ("p",)
        ),
        None,
    )
    if reordered is None or momentum is None:
        raise UnsupportedScheduledWWGraphError("notation mixed branches are not typed")

    k_plus = _qi_from_notation(k_rule.rhs[0].coefficient)
    dminus_dplus = _qi_from_notation(d_pair_rule.rhs[0].coefficient)
    dminus_kplus = _qi_from_notation(d_k_rule.rhs[0].coefficient)
    closed_delta = _qi_from_notation(closed_rule.rhs[0].coefficient)
    mixed_reordering = _qi_from_notation(reordered.coefficient)
    mixed_momentum = _qi_from_notation(momentum.coefficient)
    ordered_mixed = mixed_reordering * mixed_momentum
    if dminus_kplus != k_plus * dminus_dplus:
        raise UnsupportedScheduledWWGraphError(
            "notation Dminus-Kplus coefficient disagrees with Kplus and Dminus-Dplus"
        )

    probe_momenta = ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3))
    checks: list[tuple[str, bool]] = []

    def oracle_scalar(value: GaussianRational) -> object:
        return matrix_oracle.QComplex(value.re, value.im)  # type: ignore[attr-defined]

    for probe in probe_momenta:
        operators = matrix_oracle.flat_operators(probe)  # type: ignore[attr-defined]
        label = "_".join(str(value).replace("-", "m") for value in probe)
        checks.append(
            (
                f"Dminus_Dplus_{label}",
                matrix_oracle.multiply(operators["D_minus"], operators["D_plus"])  # type: ignore[attr-defined]
                == matrix_oracle.scale(oracle_scalar(dminus_dplus), operators["D2"]),  # type: ignore[attr-defined]
            )
        )
        k_matrix = matrix_oracle.scale(  # type: ignore[attr-defined]
            oracle_scalar(k_plus),
            matrix_oracle.multiply(  # type: ignore[attr-defined]
                matrix_oracle.multiply(operators["D_plus"], operators["barD2"]),  # type: ignore[attr-defined]
                operators["D_plus"],
            ),
        )
        checks.append(
            (
                f"Dminus_Kplus_{label}",
                matrix_oracle.multiply(operators["D_minus"], k_matrix)  # type: ignore[attr-defined]
                == matrix_oracle.scale(  # type: ignore[attr-defined]
                    oracle_scalar(dminus_kplus),
                    matrix_oracle.multiply(  # type: ignore[attr-defined]
                        matrix_oracle.multiply(operators["D2"], operators["barD2"]),  # type: ignore[attr-defined]
                        operators["D_plus"],
                    ),
                ),
            )
        )
        sigma = matrix_oracle.sigma_e(probe)  # type: ignore[attr-defined]
        d_operators = (operators["D_plus"], operators["D_minus"])
        bar_operators = (operators["barD_plus"], operators["barD_minus"])
        for undotted in range(2):
            for dotted in range(2):
                anticommutator = matrix_oracle.add(  # type: ignore[attr-defined]
                    matrix_oracle.multiply(d_operators[undotted], bar_operators[dotted]),  # type: ignore[attr-defined]
                    matrix_oracle.multiply(bar_operators[dotted], d_operators[undotted]),  # type: ignore[attr-defined]
                )
                expected = matrix_oracle.scale(  # type: ignore[attr-defined]
                    oracle_scalar(mixed_momentum) * sigma[undotted][dotted],
                    operators["identity"],
                )
                checks.append(
                    (
                        f"mixed_{label}_{undotted}_{dotted}",
                        anticommutator == expected,
                    )
                )
        normalized_delta = matrix_oracle.polynomial_basis(15, -4)  # type: ignore[attr-defined]
        saturated = matrix_oracle.matrix_vector(  # type: ignore[attr-defined]
            matrix_oracle.multiply(operators["D2"], operators["barD2"]),  # type: ignore[attr-defined]
            normalized_delta,
        )
        checks.append(
            (
                f"closed_delta_evaluated_at_zero_{label}",
                saturated[0] == oracle_scalar(closed_delta),
            )
        )

    return ScheduledWWAlgebraCertificate(
        notation_hash=notation_schema.canonical_hash,  # type: ignore[attr-defined]
        k_plus_coefficient=k_plus,
        dminus_dplus_coefficient=dminus_dplus,
        dminus_kplus_coefficient=dminus_kplus,
        closed_delta_coefficient=closed_delta,
        mixed_reordering_coefficient=mixed_reordering,
        mixed_momentum_coefficient=mixed_momentum,
        ordered_mixed_factor=ordered_mixed,
        matrix_probe_momenta=probe_momenta,
        matrix_checks=tuple(checks),
    )


@dataclass(frozen=True)
class ScheduledDerivativeApplication:
    application_id: str
    scope_id: str
    derivative_kind: str
    spinor_index: str
    vertex_id: str
    half_edge_id: str
    edge_id: str
    momentum: str
    vertex_sign: int
    source_tag: EndpointTag
    pivot_tag: EndpointTag
    endpoint_transfer_count: int
    endpoint_transfer_sign: int
    crossed_parities: tuple[int, ...]
    koszul_sign: int

    def to_json(self) -> dict[str, object]:
        return {
            "application_id": self.application_id,
            "scope_id": self.scope_id,
            "derivative_kind": self.derivative_kind,
            "spinor_index": self.spinor_index,
            "vertex_id": self.vertex_id,
            "half_edge_id": self.half_edge_id,
            "edge_id": self.edge_id,
            "momentum": self.momentum,
            "vertex_sign": self.vertex_sign,
            "source_tag": tag_to_json(self.source_tag),
            "pivot_tag": tag_to_json(self.pivot_tag),
            "endpoint_transfer_count": self.endpoint_transfer_count,
            "endpoint_transfer_sign": self.endpoint_transfer_sign,
            "crossed_parities": list(self.crossed_parities),
            "koszul_sign": self.koszul_sign,
        }


@dataclass(frozen=True)
class ScheduledDMinusPlacement:
    placement_id: str
    placement_name: str
    insertion_vertex_id: str
    target_half_edge_id: str
    preceding_field_parities: tuple[int, ...]
    leibniz_sign: int

    def to_json(self) -> dict[str, object]:
        return {
            "placement_id": self.placement_id,
            "placement_name": self.placement_name,
            "insertion_vertex_id": self.insertion_vertex_id,
            "target_half_edge_id": self.target_half_edge_id,
            "preceding_field_parities": list(self.preceding_field_parities),
            "leibniz_sign": self.leibniz_sign,
        }


@dataclass(frozen=True)
class ScheduledPhaseTrace:
    phase: str
    applied: bool
    measure_before: int
    measure_after: int
    exact_factor: GaussianRational
    rule: str
    input: str
    output: str
    ledger: tuple[SignLedgerEntry, ...] = ()

    def __post_init__(self) -> None:
        if self.phase not in SCHEDULED_WW_PHASES:
            raise ValueError(f"unknown scheduled WW phase {self.phase}")
        if self.applied and not self.measure_after < self.measure_before:
            raise ValueError(
                f"applied phase {self.phase} does not lower its measure: "
                f"{self.measure_before} -> {self.measure_after}"
            )

    def to_json(self) -> dict[str, object]:
        return {
            "phase": self.phase,
            "applied": self.applied,
            "measure_before": self.measure_before,
            "measure_after": self.measure_after,
            "exact_factor": self.exact_factor.to_json(),
            "rule": self.rule,
            "input": self.input,
            "output": self.output,
            "ledger": [entry.to_json() for entry in self.ledger],
        }


@dataclass(frozen=True)
class ScheduledNumeratorFactor:
    factor_kind: str
    momentum: str
    edge_id: str | None
    external_leg_id: str | None
    undotted: str
    dotted: str
    fourier_factor: GaussianRational

    def to_json(self) -> dict[str, object]:
        return {
            "factor_kind": self.factor_kind,
            "momentum": self.momentum,
            "edge_id": self.edge_id,
            "external_leg_id": self.external_leg_id,
            "undotted": self.undotted,
            "dotted": self.dotted,
            "fourier_factor": self.fourier_factor.to_json(),
        }


@dataclass(frozen=True)
class ScheduledWWNormalForm:
    coefficient_in_g2: GaussianRational
    numerator_factors: tuple[ScheduledNumeratorFactor, ...]
    propagator_collapses: tuple[str, ...]
    classification: str

    def to_json(self) -> dict[str, object]:
        return {
            "arithmetic": "EXACT_Q_I",
            "coefficient_in_g2": self.coefficient_in_g2.to_json(),
            "numerator_factors": [factor.to_json() for factor in self.numerator_factors],
            "propagator_collapses": list(self.propagator_collapses),
            "classification": self.classification,
        }

    def canonical_json(self) -> str:
        return json.dumps(self.to_json(), sort_keys=True, separators=(",", ":")) + "\n"

    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_json().encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ScheduledWWRow:
    trace_id: str
    notation_hash: str
    graph_hash: str
    amplitude_id: str
    orientation: str
    orientation_koszul_sign: int
    external_w_field_name: str
    external_w_color_label: str
    placement: ScheduledDMinusPlacement
    bar_application: ScheduledDerivativeApplication
    d_application: ScheduledDerivativeApplication
    insertion_prefactor: Fraction
    closed_delta: int
    mixed_anticommutator_factors: tuple[GaussianRational, GaussianRational]
    exact_d_chain: GaussianRational
    graph_prefactor_in_g2: Fraction
    phase_trace: tuple[ScheduledPhaseTrace, ...]
    normal_form: ScheduledWWNormalForm

    def __post_init__(self) -> None:
        if tuple(phase.phase for phase in self.phase_trace) != SCHEDULED_WW_PHASES:
            raise ValueError("scheduled WW phases are missing or out of order")

    @property
    def total_endpoint_sign(self) -> int:
        return (
            self.bar_application.vertex_sign
            * self.bar_application.endpoint_transfer_sign
            * self.bar_application.koszul_sign
            * self.d_application.vertex_sign
            * self.d_application.endpoint_transfer_sign
            * self.d_application.koszul_sign
        )

    @property
    def external_derivative_rendering(self) -> str:
        factor = self.normal_form.numerator_factors[1]
        return (
            "partial_(a dot_beta)["
            + self.external_w_field_name
            + "^"
            + self.external_w_color_label
            + "("
            + factor.momentum
            + ")]=i*"
            + factor.momentum
            + "_(a dot_beta)*"
            + self.external_w_field_name
            + "^"
            + self.external_w_color_label
            + "("
            + factor.momentum
            + ")"
        )

    def to_json(self) -> dict[str, object]:
        return {
            "schema": 1,
            "scope": SCHEDULED_WW_SCOPE,
            "trace_id": self.trace_id,
            "notation_hash": self.notation_hash,
            "graph_hash": self.graph_hash,
            "amplitude_id": self.amplitude_id,
            "orientation": self.orientation,
            "orientation_koszul_sign": self.orientation_koszul_sign,
            "external_w_field_name": self.external_w_field_name,
            "external_w_color_label": self.external_w_color_label,
            "placement": self.placement.to_json(),
            "bar_application": self.bar_application.to_json(),
            "d_application": self.d_application.to_json(),
            "total_endpoint_sign": self.total_endpoint_sign,
            "exact_d_chain": {
                "insertion_prefactor": str(self.insertion_prefactor),
                "closed_delta": self.closed_delta,
                "mixed_anticommutator_factors": [
                    factor.to_json() for factor in self.mixed_anticommutator_factors
                ],
                "product": self.exact_d_chain.to_json(),
            },
            "graph_prefactor_in_g2": str(self.graph_prefactor_in_g2),
            "phase_order": list(SCHEDULED_WW_PHASES),
            "phase_trace": [phase.to_json() for phase in self.phase_trace],
            "normal_form": self.normal_form.to_json(),
            "normal_form_sha256": self.normal_form.sha256(),
            "external_derivative_rendering": self.external_derivative_rendering,
        }

    def canonical_json(self) -> str:
        return json.dumps(self.to_json(), sort_keys=True, separators=(",", ":")) + "\n"

    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_json().encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ScheduledWWCompilation:
    notation_hash: str
    graph_hash: str
    amplitude_id: str
    orientation: str
    algebra_certificate: ScheduledWWAlgebraCertificate
    placements: tuple[ScheduledDMinusPlacement, ...]
    bar_scope: tuple[ScheduledDerivativeApplication, ...]
    d_scope: tuple[ScheduledDerivativeApplication, ...]
    rows: tuple[ScheduledWWRow, ...]

    def __post_init__(self) -> None:
        if len(self.placements) != 2 or len(self.bar_scope) != 2 or len(self.d_scope) != 2:
            raise ValueError("physical WW schedule requires 2 x 2 x 2 choices")
        if len(self.rows) != 8:
            raise ValueError("one WW orientation requires exactly eight scheduled rows")

    def to_json(self) -> dict[str, object]:
        return {
            "schema": 1,
            "status": "PASS_PHYSICAL_WW_EIGHT_ROW_PHASE_SEQUENCE",
            "scope": SCHEDULED_WW_SCOPE,
            "notation_hash": self.notation_hash,
            "graph_hash": self.graph_hash,
            "amplitude_id": self.amplitude_id,
            "orientation": self.orientation,
            "algebra_certificate": self.algebra_certificate.to_json(),
            "placements": [placement.to_json() for placement in self.placements],
            "bar_scope": [application.to_json() for application in self.bar_scope],
            "d_scope": [application.to_json() for application in self.d_scope],
            "rows": [
                {**row.to_json(), "row_sha256": row.sha256()} for row in self.rows
            ],
            "critical_pair_scope": DECLARED_CRITICAL_PAIR_SCOPE,
            "global_confluence_claimed": False,
            "contact_cancellation_claimed": False,
            "anomaly_coefficient_claimed": False,
        }

    def canonical_json(self) -> str:
        return json.dumps(self.to_json(), sort_keys=True, separators=(",", ":")) + "\n"


def _require_unique(items: Sequence[object], predicate: Callable[[object], bool], label: str) -> object:
    selected = [item for item in items if predicate(item)]
    if len(selected) != 1:
        raise UnsupportedScheduledWWGraphError(
            f"physical WW schedule requires exactly one {label}; found {len(selected)}"
        )
    return selected[0]


def _difference_scope(expression: str) -> tuple[str, str, str]:
    compact = expression.replace(" ", "")
    match = re.fullmatch(r"(?P<head>[^()]+)\((?P<plus>[^()]+)\)-(?P=head)\((?P<minus>[^()]+)\)", compact)
    if match is None:
        raise UnsupportedScheduledWWGraphError(
            f"derivative scope is not an ordered binary difference: {expression}"
        )
    return match.group("head"), match.group("plus"), match.group("minus")


def _half_edge_for_label(vertex: object, label: str, external_half_edges: set[str]) -> str:
    candidates = [
        half_edge_id
        for half_edge_id in vertex.ordered_half_edges  # type: ignore[attr-defined]
        if half_edge_id not in external_half_edges and half_edge_id.endswith("_" + label)
    ]
    if len(candidates) != 1:
        raise UnsupportedScheduledWWGraphError(
            f"vertex {vertex.vertex_id} has no unique quantum port for label {label}"  # type: ignore[attr-defined]
        )
    return candidates[0]


def _vertex_operator(vertex: object, prefix: str) -> str:
    candidates = [
        factor
        for factor in vertex.effective_coefficient_factors  # type: ignore[attr-defined]
        if factor.startswith(prefix)
    ]
    if len(candidates) != 1:
        raise UnsupportedScheduledWWGraphError(
            f"vertex {vertex.vertex_id} has no unique operator beginning {prefix}"  # type: ignore[attr-defined]
        )
    return candidates[0]


def _scheduled_application(
    *,
    scope_id: str,
    derivative_kind: str,
    spinor_index: str,
    vertex: object,
    half_edge_id: str,
    vertex_sign: int,
    edge_by_half_edge: dict[str, object],
    central_edge_id: str,
    half_edges: dict[str, object],
) -> ScheduledDerivativeApplication:
    edge = edge_by_half_edge[half_edge_id]
    source_tag = EndpointTag(edge.edge_id, half_edge_id)  # type: ignore[attr-defined]
    transfer_count = 0 if edge.edge_id == central_edge_id else 1  # type: ignore[attr-defined]
    transfer_sign = 1
    koszul_sign = 1
    crossed_parities: tuple[int, ...] = ()
    pivot_tag = source_tag
    if transfer_count:
        other = (
            edge.right_half_edge  # type: ignore[attr-defined]
            if edge.left_half_edge == half_edge_id  # type: ignore[attr-defined]
            else edge.left_half_edge  # type: ignore[attr-defined]
        )
        pivot_tag = EndpointTag(edge.edge_id, other)  # type: ignore[attr-defined]
        crossed_parities = (half_edges[half_edge_id].field_type.parity,)
        token: Token
        if derivative_kind == "barD":
            token = BarD(spinor_index, source_tag, edge.momentum)  # type: ignore[attr-defined]
        else:
            token = D(spinor_index, source_tag, edge.momentum)  # type: ignore[attr-defined]
        moved = transfer_endpoint(Term(1, (token,)), 0, pivot_tag, crossed_parities)
        transfer_sign = int(moved.sign_ledger[0].factor.re)
        koszul_sign = int(moved.sign_ledger[1].factor.re)
        if moved.sign_ledger[0].factor.im or moved.sign_ledger[1].factor.im:
            raise UnsupportedScheduledWWGraphError("endpoint signs must be real")
    return ScheduledDerivativeApplication(
        application_id=f"{scope_id}:{half_edge_id}",
        scope_id=scope_id,
        derivative_kind=derivative_kind,
        spinor_index=spinor_index,
        vertex_id=vertex.vertex_id,  # type: ignore[attr-defined]
        half_edge_id=half_edge_id,
        edge_id=edge.edge_id,  # type: ignore[attr-defined]
        momentum=edge.momentum,  # type: ignore[attr-defined]
        vertex_sign=vertex_sign,
        source_tag=source_tag,
        pivot_tag=pivot_tag,
        endpoint_transfer_count=transfer_count,
        endpoint_transfer_sign=transfer_sign,
        crossed_parities=crossed_parities,
        koszul_sign=koszul_sign,
    )


def compile_scheduled_ww_rows(
    amplitude: object,
    notation_schema: object | None = None,
    matrix_oracle: object | None = None,
) -> ScheduledWWCompilation:
    """Compile the physical 2 x 4 WW ledger from GraphIR and AmplitudeIR.

    The constructor reads the typed graph topology, ordered vertex derivative
    differences, the two insertion ports, the exact reduced amplitude
    coefficient, and the external-leg parity/chirality data.  It does not read
    the legacy endpoint table.
    """

    if notation_schema is None or matrix_oracle is None:
        raise UnsupportedScheduledWWGraphError(
            "physical WW scheduling requires notation and exact 16x16 oracle inputs"
        )
    algebra_certificate = build_scheduled_ww_algebra_certificate(
        notation_schema, matrix_oracle
    )
    graph = amplitude.graph  # type: ignore[attr-defined]
    graph.validate()
    graph.assert_linear_momentum_routing()
    if graph.cycle_rank() != 1 or len(graph.vertices) != 3 or len(graph.internal_edges) != 3:
        raise UnsupportedScheduledWWGraphError("scheduled WW compiler accepts only the one-loop triangle")
    if amplitude.orientation not in {"DIRECT", "REFLECTED"}:  # type: ignore[attr-defined]
        raise UnsupportedScheduledWWGraphError("unknown WW orientation")
    if amplitude.external_koszul_sign not in {-1, 1}:  # type: ignore[attr-defined]
        raise UnsupportedScheduledWWGraphError("external orientation sign is not exact")
    if amplitude.schema_hash != algebra_certificate.notation_hash:  # type: ignore[attr-defined]
        raise UnsupportedScheduledWWGraphError(
            "amplitude notation hash disagrees with the algebra certificate"
        )

    vertices = tuple(graph.vertices)
    insertion = _require_unique(
        vertices,
        lambda vertex: vertex.kind == "COMPOSITE_INSERTION_I2_WW",  # type: ignore[attr-defined]
        "WW insertion",
    )
    bar_vertex = _require_unique(
        vertices,
        lambda vertex: vertex.kind == "BACKGROUND_CUBIC_TILDE_W",  # type: ignore[attr-defined]
        "antichiral cubic vertex",
    )
    d_vertex = _require_unique(
        vertices,
        lambda vertex: vertex.kind == "BACKGROUND_CUBIC_W",  # type: ignore[attr-defined]
        "chiral cubic vertex",
    )
    half_edges = {half_edge.half_edge_id: half_edge for half_edge in graph.half_edges}
    external_half_edges = {leg.attached_half_edge for leg in graph.external_legs}
    edge_by_half_edge: dict[str, object] = {}
    for edge in graph.internal_edges:
        edge_by_half_edge[edge.left_half_edge] = edge
        edge_by_half_edge[edge.right_half_edge] = edge
    internal_vertices = {
        half_edges[edge.left_half_edge].vertex_id
        for edge in graph.internal_edges
    } | {
        half_edges[edge.right_half_edge].vertex_id
        for edge in graph.internal_edges
    }
    if internal_vertices != {vertex.vertex_id for vertex in graph.vertices}:
        raise UnsupportedScheduledWWGraphError("every WW vertex must lie on the triangle")
    central_edges = [
        edge
        for edge in graph.internal_edges
        if insertion.vertex_id
        not in {
            half_edges[edge.left_half_edge].vertex_id,
            half_edges[edge.right_half_edge].vertex_id,
        }
    ]
    if len(central_edges) != 1:
        raise UnsupportedScheduledWWGraphError("WW triangle has no unique action-action edge")
    central_edge_id = central_edges[0].edge_id

    insertion_expression = _vertex_operator(insertion, "D_-[")
    insertion_match = re.fullmatch(
        r"D_-\[K_\+V\^(?P<left>[A-Za-z0-9_]+)K_\+V\^(?P<right>[A-Za-z0-9_]+)\]",
        insertion_expression.replace(" ", ""),
    )
    if insertion_match is None:
        raise UnsupportedScheduledWWGraphError("WW insertion scope is not the ordered two-letter form")
    insertion_labels = (insertion_match.group("left"), insertion_match.group("right"))
    insertion_half_edges = tuple(
        _half_edge_for_label(insertion, label, external_half_edges)
        for label in insertion_labels
    )
    placements: list[ScheduledDMinusPlacement] = []
    for index, half_edge_id in enumerate(insertion_half_edges):
        preceding = tuple(
            half_edges[item].field_type.parity for item in insertion_half_edges[:index]
        )
        placements.append(
            ScheduledDMinusPlacement(
                placement_id=f"D_MINUS:{half_edge_id}",
                placement_name="LEFT_LETTER" if index == 0 else "RIGHT_LETTER",
                insertion_vertex_id=insertion.vertex_id,
                target_half_edge_id=half_edge_id,
                preceding_field_parities=preceding,
                leibniz_sign=-1 if sum(preceding) % 2 else 1,
            )
        )

    bar_expression = _vertex_operator(bar_vertex, "barD^")
    bar_head, bar_plus, bar_minus = _difference_scope(bar_expression)
    if not bar_head.startswith("barD^"):
        raise UnsupportedScheduledWWGraphError("antichiral cubic scope has the wrong derivative family")
    d_expression = _vertex_operator(d_vertex, "D_")
    d_head, d_plus, d_minus = _difference_scope(d_expression)
    if not d_head.startswith("D_"):
        raise UnsupportedScheduledWWGraphError("chiral cubic scope has the wrong derivative family")

    bar_scope = tuple(
        sorted(
            (
                _scheduled_application(
                    scope_id="CUBIC_BAR_DIFFERENCE",
                    derivative_kind="barD",
                    spinor_index="dot_alpha",
                    vertex=bar_vertex,
                    half_edge_id=_half_edge_for_label(bar_vertex, label, external_half_edges),
                    vertex_sign=sign,
                    edge_by_half_edge=edge_by_half_edge,
                    central_edge_id=central_edge_id,
                    half_edges=half_edges,
                )
                for label, sign in ((bar_plus, 1), (bar_minus, -1))
            ),
            key=lambda application: application.edge_id,
        )
    )
    d_scope = tuple(
        sorted(
            (
                _scheduled_application(
                    scope_id="CUBIC_D_DIFFERENCE",
                    derivative_kind="D",
                    spinor_index="a",
                    vertex=d_vertex,
                    half_edge_id=_half_edge_for_label(d_vertex, label, external_half_edges),
                    vertex_sign=sign,
                    edge_by_half_edge=edge_by_half_edge,
                    central_edge_id=central_edge_id,
                    half_edges=half_edges,
                )
                for label, sign in ((d_plus, 1), (d_minus, -1))
            ),
            key=lambda application: application.edge_id,
        )
    )

    external_w = _require_unique(
        tuple(graph.external_legs),
        lambda leg: leg.field_type.name == "W_plus",  # type: ignore[attr-defined]
        "external W_plus leg",
    )
    external_tilde_w = _require_unique(
        tuple(graph.external_legs),
        lambda leg: leg.field_type.name == "TildeW_dot_alpha",  # type: ignore[attr-defined]
        "external TildeW leg",
    )
    if external_w.field_type.chirality.value != "CHIRAL" or external_w.field_type.parity != 1:
        raise UnsupportedScheduledWWGraphError("external W_plus typing is inconsistent")
    if (
        external_tilde_w.field_type.chirality.value != "ANTICHIRAL"
        or external_tilde_w.field_type.parity != 1
        or len(external_w.spinor_indices) != 1
        or len(external_tilde_w.spinor_indices) != 1
    ):
        raise UnsupportedScheduledWWGraphError("external spinor typing is inconsistent")
    plus_index = external_w.spinor_indices[0].label
    dotted_external_index = external_tilde_w.spinor_indices[0].label
    coefficient = amplitude.exact_coefficient_reduced  # type: ignore[attr-defined]
    if coefficient.sqrt2_power != 0 or coefficient.i_power % 4 != 0 or coefficient.symbols != ("g2",):
        raise UnsupportedScheduledWWGraphError("WW amplitude coefficient must be an exact Q*g2 scalar")
    graph_prefactor = Fraction(coefficient.rational)
    if graph_prefactor * amplitude.external_koszul_sign != Fraction(-1, 8):  # type: ignore[attr-defined]
        raise UnsupportedScheduledWWGraphError("orientation-stripped WW graph prefactor is not -1/8")

    projector_expression = _vertex_operator(insertion, "K_+=")
    projector_match = re.fullmatch(
        r"K_\+=-\((?P<num>\d+)/(?P<den>\d+)\)D_\+barD\^2D_\+",
        projector_expression.replace(" ", ""),
    )
    if projector_match is None:
        raise UnsupportedScheduledWWGraphError("K_plus normalization is not the locked Project word")
    parsed_k_plus = GaussianRational(
        -Fraction(int(projector_match.group("num")), int(projector_match.group("den")))
    )
    if parsed_k_plus != algebra_certificate.k_plus_coefficient:
        raise UnsupportedScheduledWWGraphError(
            "GraphIR K_plus expression disagrees with the notation rule"
        )
    insertion_prefactor_qi = (
        algebra_certificate.dminus_kplus_coefficient
        * algebra_certificate.k_plus_coefficient
    )
    if insertion_prefactor_qi.im:
        raise UnsupportedScheduledWWGraphError("WW insertion prefactor must be real")
    insertion_prefactor = insertion_prefactor_qi.re
    if algebra_certificate.closed_delta_coefficient.im:
        raise UnsupportedScheduledWWGraphError("closed-delta coefficient must be real")
    closed_delta_fraction = algebra_certificate.closed_delta_coefficient.re
    if closed_delta_fraction.denominator != 1:
        raise UnsupportedScheduledWWGraphError("closed-delta coefficient must be integral")
    closed_delta = closed_delta_fraction.numerator
    mixed_factors = (
        algebra_certificate.ordered_mixed_factor,
        algebra_certificate.ordered_mixed_factor,
    )
    exact_d_chain = gaussian(insertion_prefactor * closed_delta) * mixed_factors[0] * mixed_factors[1]
    if exact_d_chain != gaussian(Fraction(-1, 2)):
        raise UnsupportedScheduledWWGraphError("scheduled Project D-chain is not -1/2")

    rows: list[ScheduledWWRow] = []
    row_number = 0
    for placement in placements:
        for bar_application in bar_scope:
            for d_application in d_scope:
                row_number += 1
                scope_factor = gaussian(
                    placement.leibniz_sign
                    * bar_application.vertex_sign
                    * d_application.vertex_sign
                )
                ibp_factor = gaussian(
                    bar_application.endpoint_transfer_sign
                    * bar_application.koszul_sign
                    * d_application.endpoint_transfer_sign
                    * d_application.koszul_sign
                )
                primitive_factor = mixed_factors[0] * mixed_factors[1]
                phase_trace = (
                    ScheduledPhaseTrace(
                        "SCOPE_EXPANSION", True, 3, 0, scope_factor,
                        "ordered Leibniz placement and two ordered cubic differences",
                        insertion_expression + ";" + bar_expression + ";" + d_expression,
                        placement.placement_name + ";" + bar_application.application_id + ";" + d_application.application_id,
                    ),
                    ScheduledPhaseTrace(
                        "ENDPOINT_CANONICALIZATION", True, 2, 0, ONE,
                        "map each selected quantum port to its unique GraphIR edge endpoint",
                        bar_application.half_edge_id + ";" + d_application.half_edge_id,
                        bar_application.edge_id + ";" + d_application.edge_id,
                    ),
                    ScheduledPhaseTrace(
                        "PIVOTED_IBP", bool(bar_application.endpoint_transfer_count + d_application.endpoint_transfer_count),
                        bar_application.endpoint_transfer_count + d_application.endpoint_transfer_count,
                        0,
                        ibp_factor,
                        "D_i(r) Delta_ij(r)=-D_j(-r) Delta_ij(r), with explicit bosonic Koszul crossings",
                        str(tag_to_json(bar_application.source_tag)) + ";" + str(tag_to_json(d_application.source_tag)),
                        str(tag_to_json(bar_application.pivot_tag)) + ";" + str(tag_to_json(d_application.pivot_tag)),
                        tuple(
                            entry
                            for application in (bar_application, d_application)
                            for entry in (
                                SignLedgerEntry(
                                    LedgerKind.IBP,
                                    gaussian(application.endpoint_transfer_sign),
                                    "scheduled endpoint transfer",
                                    application.derivative_kind,
                                    application.source_tag,
                                    application.pivot_tag,
                                    application.crossed_parities,
                                ),
                                SignLedgerEntry(
                                    LedgerKind.KOSZUL,
                                    gaussian(application.koszul_sign),
                                    "scheduled graded prefix crossing",
                                    application.derivative_kind,
                                    application.source_tag,
                                    application.pivot_tag,
                                    application.crossed_parities,
                                ),
                            )
                            if application.endpoint_transfer_count
                        ),
                    ),
                    ScheduledPhaseTrace(
                        "PRIMITIVE_NORMAL_ORDERING", True, 2, 0, primitive_factor,
                        "two ordered mixed anticommutators, each 2i times its typed momentum",
                        "two mixed D-barD pairs",
                        "(2i)*(2i)=-4",
                    ),
                    ScheduledPhaseTrace(
                        "PROJECTOR_REDUCTION", True, 2, 0, gaussian(insertion_prefactor),
                        "D_-K_+=-(1/16)D^2barD^2D_+ and K_+=-(1/8)D_+barD^2D_+",
                        projector_expression,
                        "insertion_prefactor=" + str(insertion_prefactor),
                    ),
                    ScheduledPhaseTrace(
                        "EXTERNAL_CHIRALITY", True, 1, 0, ONE,
                        "the vector derivative on chiral W_plus is retained as an external token",
                        "D_a barD_dot_beta W_plus",
                        "i*" + external_w.momentum + "_(a dot_beta) W_plus",
                    ),
                    ScheduledPhaseTrace(
                        "GRASSMANN_SATURATION", True, 1, 0, gaussian(closed_delta),
                        "[D^2 barD^2(theta^2 bartheta^2)]_0=16",
                        "one normalized closed Grassmann delta",
                        "16",
                    ),
                    ScheduledPhaseTrace(
                        "TYPED_EDGE_COLLAPSE", False, 0, 0, ONE,
                        "no p^2/propagator match occurs in the metric numerator branch",
                        "three typed propagators",
                        "no collapse",
                    ),
                )
                scheduled_factor = ONE
                for phase in phase_trace:
                    scheduled_factor *= phase.exact_factor
                coefficient_in_g2 = gaussian(graph_prefactor) * scheduled_factor
                endpoint_sign = (
                    bar_application.vertex_sign
                    * bar_application.endpoint_transfer_sign
                    * bar_application.koszul_sign
                    * d_application.vertex_sign
                    * d_application.endpoint_transfer_sign
                    * d_application.koszul_sign
                )
                expected = gaussian(graph_prefactor) * exact_d_chain * endpoint_sign * placement.leibniz_sign
                if coefficient_in_g2 != expected:
                    raise AssertionError("scheduled phase product disagrees with the exact WW chain")
                normal_form = ScheduledWWNormalForm(
                    coefficient_in_g2,
                    (
                        ScheduledNumeratorFactor(
                            "EDGE_MOMENTUM", bar_application.momentum,
                            bar_application.edge_id, None, plus_index, "dot_beta", ONE,
                        ),
                        ScheduledNumeratorFactor(
                            "EXTERNAL_VECTOR_DERIVATIVE", external_w.momentum,
                            None, external_w.leg_id, "a", "dot_beta", I,
                        ),
                        ScheduledNumeratorFactor(
                            "EDGE_MOMENTUM", d_application.momentum,
                            d_application.edge_id, None, "a", dotted_external_index, ONE,
                        ),
                    ),
                    (),
                    "ORDINARY_UV_POLE_METRIC_BRANCH",
                )
                rows.append(
                    ScheduledWWRow(
                        trace_id=f"DA-{amplitude.orientation[0]}-{row_number:03d}",  # type: ignore[attr-defined]
                        notation_hash=amplitude.schema_hash,  # type: ignore[attr-defined]
                        graph_hash=amplitude.canonical_key,  # type: ignore[attr-defined]
                        amplitude_id=amplitude.amplitude_id,  # type: ignore[attr-defined]
                        orientation=amplitude.orientation,  # type: ignore[attr-defined]
                        orientation_koszul_sign=amplitude.external_koszul_sign,  # type: ignore[attr-defined]
                        external_w_field_name=external_w.field_type.name,
                        external_w_color_label=external_w.color_label,
                        placement=placement,
                        bar_application=bar_application,
                        d_application=d_application,
                        insertion_prefactor=insertion_prefactor,
                        closed_delta=closed_delta,
                        mixed_anticommutator_factors=mixed_factors,
                        exact_d_chain=exact_d_chain,
                        graph_prefactor_in_g2=graph_prefactor,
                        phase_trace=phase_trace,
                        normal_form=normal_form,
                    )
                )

    return ScheduledWWCompilation(
        notation_hash=amplitude.schema_hash,  # type: ignore[attr-defined]
        graph_hash=amplitude.canonical_key,  # type: ignore[attr-defined]
        amplitude_id=amplitude.amplitude_id,  # type: ignore[attr-defined]
        orientation=amplitude.orientation,  # type: ignore[attr-defined]
        algebra_certificate=algebra_certificate,
        placements=tuple(placements),
        bar_scope=bar_scope,
        d_scope=d_scope,
        rows=tuple(rows),
    )


def compare_scheduled_ww_to_legacy(
    scheduled: ScheduledWWCompilation,
    legacy_rows: Sequence[dict[str, object]],
) -> dict[str, object]:
    """Equality oracle only; legacy data never participates in construction."""

    if len(legacy_rows) != len(scheduled.rows):
        return {"status": "FAIL", "reason": "row count mismatch", "rows": []}
    audits: list[dict[str, object]] = []
    for row, legacy in zip(scheduled.rows, legacy_rows, strict=True):
        exact_chain = legacy["exact_D_chain"]
        if not isinstance(exact_chain, dict):
            raise ValueError("legacy exact_D_chain is not a record")
        def momentum_equal(actual: str, legacy_value: object, edge_id: str) -> bool:
            return str(legacy_value) in {actual, "r" + edge_id.removeprefix("e")}

        legacy_bar = legacy["barD_endpoint"]
        legacy_d = legacy["D_endpoint"]
        if not isinstance(legacy_bar, dict) or not isinstance(legacy_d, dict):
            raise ValueError("legacy endpoints are not records")
        legacy_mixed = legacy["mixed_anticommutator_momenta"]
        if not isinstance(legacy_mixed, list) or len(legacy_mixed) != 3:
            raise ValueError("legacy mixed momentum word is not length three")
        checks = {
            "trace_id": row.trace_id == legacy["trace_id"],
            "orientation": row.orientation == legacy["orientation"],
            "D_minus_placement": row.placement.placement_name == legacy["D_minus_placement"],
            "bar_edge": row.bar_application.edge_id == legacy_bar["edge"],
            "bar_momentum": momentum_equal(
                row.bar_application.momentum,
                legacy_bar["momentum"],
                row.bar_application.edge_id,
            ),
            "D_edge": row.d_application.edge_id == legacy_d["edge"],
            "D_momentum": momentum_equal(
                row.d_application.momentum,
                legacy_d["momentum"],
                row.d_application.edge_id,
            ),
            "vertex_signs": [row.bar_application.vertex_sign, row.d_application.vertex_sign]
            == legacy["vertex_signs"],
            "endpoint_transfer_signs": [
                row.bar_application.endpoint_transfer_sign,
                row.d_application.endpoint_transfer_sign,
            ]
            == legacy["endpoint_transfer_signs"],
            "koszul_signs": [row.bar_application.koszul_sign, row.d_application.koszul_sign]
            == legacy["koszul_signs"],
            "total_endpoint_sign": row.total_endpoint_sign == legacy["total_endpoint_sign"],
            "orientation_sign": row.orientation_koszul_sign == legacy["total_orientation_sign"],
            "D_chain": row.exact_d_chain == gaussian(Fraction(str(exact_chain["product"]))),
            "mixed_momenta": (
                momentum_equal(
                    row.bar_application.momentum,
                    legacy_mixed[0],
                    row.bar_application.edge_id,
                )
                and row.normal_form.numerator_factors[1].momentum == legacy_mixed[1]
                and momentum_equal(
                    row.d_application.momentum,
                    legacy_mixed[2],
                    row.d_application.edge_id,
                )
            ),
            "external_derivative": [row.external_derivative_rendering]
            == legacy["external_leg_derivative_tokens"],
            "propagator_collapses": list(row.normal_form.propagator_collapses)
            == legacy["propagator_collapses_in_metric_branch"],
        }
        audits.append(
            {
                "trace_id": row.trace_id,
                "scheduled_row_sha256": row.sha256(),
                "scheduled_normal_form_sha256": row.normal_form.sha256(),
                "checks": checks,
                "status": "PASS" if all(checks.values()) else "FAIL",
            }
        )
    return {
        "status": "PASS" if all(audit["status"] == "PASS" for audit in audits) else "FAIL",
        "construction_independent_of_legacy": True,
        "routing_dictionary": {
            application.edge_id: application.momentum
            for application in scheduled.bar_scope + scheduled.d_scope
        },
        "rows": audits,
    }


RULE_ORDER = (
    "PROJECTOR_D2_BARD2_D2",
    "PROJECTOR_BARD2_D2_BARD2",
    "SAME_CHIRAL_D",
    "SAME_CHIRAL_BARD",
    "SAME_CHIRAL_NILPOTENCE",
    "MIXED_ANTICOMMUTATOR",
    "EXTERNAL_LEG_ACTION",
    "COLLAPSE_PROPAGATOR",
    "CENTRAL_MOMENTUM_SQUARE_LEFT",
)
RULE_PRIORITY = {rule: index for index, rule in enumerate(RULE_ORDER)}


def tag_to_json(tag: EndpointTag | None) -> dict[str, str] | None:
    if tag is None:
        return None
    return {"edge_id": tag.edge_id, "endpoint": tag.endpoint}


def token_to_json(token: Token) -> dict[str, object]:
    data: dict[str, object] = {"type": type(token).__name__}
    for name, value in token.__dict__.items():
        if isinstance(value, EndpointTag):
            data[name] = tag_to_json(value)
        elif isinstance(value, Enum):
            data[name] = value.value
        elif isinstance(value, GaussianRational):
            data[name] = value.to_json()
        else:
            data[name] = value
    return data


def gaussian_from_json(data: object) -> GaussianRational:
    if not isinstance(data, dict) or set(data) != {"re", "im"}:
        raise ValueError("an exact Q(i) scalar must have exactly re and im")
    try:
        return GaussianRational(Fraction(str(data["re"])), Fraction(str(data["im"])))
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"invalid exact Q(i) scalar: {data!r}") from error


def gaussian_from_qi(value: object) -> GaussianRational:
    """Exact adapter from a repository QComplex-like object."""

    if not hasattr(value, "re") or not hasattr(value, "im"):
        raise TypeError("Q(i) adapter input must expose exact re and im")
    return GaussianRational(Fraction(value.re), Fraction(value.im))  # type: ignore[arg-type]


def gaussian_to_qi(
    value: GaussianRational, factory: Callable[[Fraction, Fraction], object]
) -> object:
    """Exact adapter to a repository QComplex-like constructor."""

    return factory(value.re, value.im)


def endpoint_tag_from_json(data: object) -> EndpointTag:
    if not isinstance(data, dict) or set(data) != {"edge_id", "endpoint"}:
        raise ValueError("endpoint tag must have exactly edge_id and endpoint")
    return EndpointTag(str(data["edge_id"]), str(data["endpoint"]))


def token_from_json(data: object) -> Token:
    if not isinstance(data, dict) or "type" not in data:
        raise ValueError("operator token must be an object with a type")
    token_type = data["type"]
    values = dict(data)
    values.pop("type")

    def exact_keys(required: set[str]) -> None:
        if set(values) != required:
            raise ValueError(
                f"{token_type} token keys are {sorted(values)}; expected {sorted(required)}"
            )

    if token_type in {"D", "BarD"}:
        exact_keys({"index", "tag", "momentum"})
        constructor = D if token_type == "D" else BarD
        index = str(values["index"])
        if index not in {"+", "-"}:
            raise ValueError(f"invalid spinor index: {index!r}")
        return constructor(
            index,
            endpoint_tag_from_json(values["tag"]),
            str(values["momentum"]),
        )
    if token_type in {"D2", "BarD2", "MomentumSquare"}:
        exact_keys({"tag", "momentum"})
        constructor = {
            "D2": D2,
            "BarD2": BarD2,
            "MomentumSquare": MomentumSquare,
        }[str(token_type)]
        return constructor(endpoint_tag_from_json(values["tag"]), str(values["momentum"]))
    if token_type == "MixedMomentum":
        exact_keys({"undotted", "dotted", "tag", "momentum", "fourier_factor"})
        undotted, dotted = str(values["undotted"]), str(values["dotted"])
        if undotted not in {"+", "-"} or dotted not in {"+", "-"}:
            raise ValueError("mixed-momentum spinor indices must be + or -")
        return MixedMomentum(
            undotted,
            dotted,
            endpoint_tag_from_json(values["tag"]),
            str(values["momentum"]),
            gaussian_from_json(values["fourier_factor"]),
        )
    if token_type == "ExternalLeg":
        exact_keys({"leg_id", "chirality", "parity", "tag"})
        parity = int(values["parity"])
        if parity not in {0, 1}:
            raise ValueError("external-leg parity must be 0 or 1")
        return ExternalLeg(
            str(values["leg_id"]),
            Chirality(str(values["chirality"])),
            parity,
            endpoint_tag_from_json(values["tag"]),
        )
    if token_type == "ExternalDerivative":
        exact_keys(
            {"leg_id", "derivative_kind", "tag", "momentum", "undotted", "dotted"}
        )
        return ExternalDerivative(
            str(values["leg_id"]),
            str(values["derivative_kind"]),
            endpoint_tag_from_json(values["tag"]),
            str(values["momentum"]),
            None if values["undotted"] is None else str(values["undotted"]),
            None if values["dotted"] is None else str(values["dotted"]),
        )
    if token_type == "Propagator":
        exact_keys({"edge_id", "momentum"})
        return Propagator(str(values["edge_id"]), str(values["momentum"]))
    if token_type == "Collapse":
        exact_keys({"edge_id", "momentum", "reason"})
        return Collapse(
            str(values["edge_id"]), str(values["momentum"]), str(values["reason"])
        )
    raise ValueError(f"unknown D-algebra token type: {token_type!r}")


def term_to_json(term: Term) -> dict[str, object]:
    return {
        "coefficient": term.coefficient.to_json(),
        "word": [token_to_json(token) for token in term.word],
        "sign_ledger": [entry.to_json() for entry in term.sign_ledger],
    }


def token_key(token: Token) -> str:
    return json.dumps(token_to_json(token), sort_keys=True, separators=(",", ":"))


def word_key(word: tuple[Token, ...]) -> str:
    return "|".join(token_key(token) for token in word)


def token_parity(token: Token) -> int:
    if isinstance(token, (D, BarD)):
        return 1
    if isinstance(token, ExternalLeg):
        return token.parity
    return 0


def derivative_order(token: Token) -> int:
    if isinstance(token, (D, BarD, MixedMomentum)):
        return 1
    if isinstance(token, (D2, BarD2)):
        return 2
    raise TypeError(f"token is not transferable derivative data: {token!r}")


def transfer_endpoint(
    term: Term,
    token_index: int,
    target: EndpointTag,
    crossed_field_parities: Sequence[int],
) -> Term:
    """Transfer one derivative by IBP and retain both sign sources."""

    token = term.word[token_index]
    if not isinstance(token, (D, BarD, D2, BarD2, MixedMomentum)):
        raise TypeError("only derivative tokens can be endpoint-transferred")
    source = token.tag
    parities = tuple(int(value) & 1 for value in crossed_field_parities)
    ibp_factor = gaussian(-1 if derivative_order(token) % 2 else 1)
    koszul_factor = gaussian(
        -1 if token_parity(token) * sum(parities) % 2 else 1
    )
    moved = replace(token, tag=target)
    word = list(term.word)
    word[token_index] = moved
    ledger = term.sign_ledger + (
        SignLedgerEntry(
            LedgerKind.IBP,
            ibp_factor,
            "integration by parts across an endpoint",
            type(token).__name__,
            source,
            target,
            parities,
        ),
        SignLedgerEntry(
            LedgerKind.KOSZUL,
            koszul_factor,
            "graded transfer through the declared field prefix",
            type(token).__name__,
            source,
            target,
            parities,
        ),
    )
    return Term(
        term.coefficient * ibp_factor * koszul_factor,
        tuple(word),
        ledger,
    )


def _same_location(left: Token, right: Token) -> bool:
    return (
        hasattr(left, "tag")
        and hasattr(right, "tag")
        and hasattr(left, "momentum")
        and hasattr(right, "momentum")
        and left.tag == right.tag  # type: ignore[attr-defined]
        and left.momentum == right.momentum  # type: ignore[attr-defined]
    )


def _disorder(word: tuple[Token, ...]) -> int:
    mixed = sum(
        1
        for index, left in enumerate(word)
        for right in word[index + 1 :]
        if isinstance(left, D) and isinstance(right, BarD) and _same_location(left, right)
    )
    central = sum(
        1
        for index, token in enumerate(word)
        if isinstance(token, MomentumSquare)
        for left in word[:index]
        if not isinstance(left, MomentumSquare)
    )
    return mixed + central


def termination_measure(term: Term) -> tuple[int, int]:
    return len(term.word), _disorder(term.word)


def _ledger(
    factor: int | Fraction | GaussianRational,
    rule: str,
    operator: str,
    kind: LedgerKind = LedgerKind.ALGEBRA,
) -> SignLedgerEntry:
    return SignLedgerEntry(kind, gaussian(factor), rule, operator)


class DAlgebraCompiler:
    @staticmethod
    def validate_phase_sequence(term: Term) -> None:
        """Reject mixed spinor words on one external factor.

        A single D-family or barD-family word can be reduced and then tested
        against chirality.  A word containing both families requires the
        unimplemented descendant algebra on D Phi or barD Phi and therefore
        cannot be simplified by terminal chirality.
        """

        spinor_tokens = (D, BarD, D2, BarD2)
        for leg_position, token in enumerate(term.word):
            if not isinstance(token, ExternalLeg):
                continue
            operators: list[Token] = []
            position = leg_position - 1
            while position >= 0 and isinstance(term.word[position], spinor_tokens):
                operators.append(term.word[position])
                position -= 1
            has_d = any(isinstance(operator, (D, D2)) for operator in operators)
            has_bar_d = any(
                isinstance(operator, (BarD, BarD2)) for operator in operators
            )
            if has_d and has_bar_d:
                operator_types = tuple(
                    type(operator).__name__ for operator in reversed(operators)
                )
                raise UnimplementedPhaseSequenceError(
                    "mixed D/barD external-factor descendants must be normalized "
                    "before chirality, but that descendant phase is not implemented",
                    leg_id=token.leg_id,
                    operator_types=operator_types,
                )

    def matches(self, term: Term) -> tuple[RewriteChoice, ...]:
        word = term.word
        found: list[RewriteChoice] = []
        for index in range(len(word) - 2):
            triple = word[index : index + 3]
            if (
                isinstance(triple[0], D2)
                and isinstance(triple[1], BarD2)
                and isinstance(triple[2], D2)
                and _same_location(triple[0], triple[1])
                and _same_location(triple[1], triple[2])
            ):
                rule = "PROJECTOR_D2_BARD2_D2"
                found.append(RewriteChoice(rule, (index, index + 1, index + 2), RULE_PRIORITY[rule]))
            if (
                isinstance(triple[0], BarD2)
                and isinstance(triple[1], D2)
                and isinstance(triple[2], BarD2)
                and _same_location(triple[0], triple[1])
                and _same_location(triple[1], triple[2])
            ):
                rule = "PROJECTOR_BARD2_D2_BARD2"
                found.append(RewriteChoice(rule, (index, index + 1, index + 2), RULE_PRIORITY[rule]))

        for index in range(len(word) - 1):
            left, right = word[index], word[index + 1]
            positions = (index, index + 1)
            if isinstance(left, D) and isinstance(right, D) and _same_location(left, right):
                rule = "SAME_CHIRAL_D"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))
            if isinstance(left, BarD) and isinstance(right, BarD) and _same_location(left, right):
                rule = "SAME_CHIRAL_BARD"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))
            if _same_location(left, right) and (
                isinstance(left, D2) and isinstance(right, (D, D2))
                or isinstance(right, D2) and isinstance(left, D)
                or isinstance(left, BarD2) and isinstance(right, (BarD, BarD2))
                or isinstance(right, BarD2) and isinstance(left, BarD)
            ):
                rule = "SAME_CHIRAL_NILPOTENCE"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))
            if (
                isinstance(left, (D, BarD, D2, BarD2, MixedMomentum))
                and isinstance(right, ExternalLeg)
                and left.tag == right.tag
            ):
                rule = "EXTERNAL_LEG_ACTION"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))
            if isinstance(left, D) and isinstance(right, BarD) and _same_location(left, right):
                rule = "MIXED_ANTICOMMUTATOR"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))
            if not isinstance(left, MomentumSquare) and isinstance(right, MomentumSquare):
                rule = "CENTRAL_MOMENTUM_SQUARE_LEFT"
                found.append(RewriteChoice(rule, positions, RULE_PRIORITY[rule]))

        squares = [
            (index, token)
            for index, token in enumerate(word)
            if isinstance(token, MomentumSquare)
        ]
        propagators = [
            (index, token)
            for index, token in enumerate(word)
            if isinstance(token, Propagator)
        ]
        for square_index, square in squares:
            for propagator_index, propagator in propagators:
                if (
                    square.tag.edge_id == propagator.edge_id
                    and square.momentum == propagator.momentum
                ):
                    rule = "COLLAPSE_PROPAGATOR"
                    found.append(
                        RewriteChoice(
                            rule,
                            tuple(sorted((square_index, propagator_index))),
                            RULE_PRIORITY[rule],
                        )
                    )
        return tuple(
            sorted(found, key=lambda item: (item.priority, item.positions, item.rule_id))
        )

    @staticmethod
    def _replace_slice(
        term: Term,
        choice: RewriteChoice,
        replacement: tuple[Token, ...],
        factor: int | Fraction | GaussianRational,
        entry: SignLedgerEntry,
    ) -> Term:
        start, end = choice.span
        if choice.positions != tuple(range(start, end)):
            raise ValueError("slice replacement requires contiguous positions")
        return Term(
            term.coefficient * gaussian(factor),
            term.word[:start] + replacement + term.word[end:],
            term.sign_ledger + (entry,),
        )

    def apply(self, term: Term, choice: RewriteChoice) -> tuple[Term, ...]:
        word = term.word
        start, end = choice.span
        selected = tuple(word[index] for index in choice.positions)
        rule = choice.rule_id
        if rule == "PROJECTOR_D2_BARD2_D2":
            first = selected[0]
            assert isinstance(first, D2)
            replacement_tokens: tuple[Token, ...] = (
                MomentumSquare(first.tag, first.momentum),
                D2(first.tag, first.momentum),
            )
            return (
                self._replace_slice(
                    term,
                    choice,
                    replacement_tokens,
                    -16,
                    _ledger(-16, rule, "D2 BarD2 D2"),
                ),
            )
        if rule == "PROJECTOR_BARD2_D2_BARD2":
            first = selected[0]
            assert isinstance(first, BarD2)
            replacement_tokens = (
                MomentumSquare(first.tag, first.momentum),
                BarD2(first.tag, first.momentum),
            )
            return (
                self._replace_slice(
                    term,
                    choice,
                    replacement_tokens,
                    -16,
                    _ledger(-16, rule, "BarD2 D2 BarD2"),
                ),
            )
        if rule in {"SAME_CHIRAL_D", "SAME_CHIRAL_BARD"}:
            left, right = selected
            if left.index == right.index:  # type: ignore[attr-defined]
                return ()
            epsilon_down = {("+", "-"): -1, ("-", "+"): 1}
            epsilon = epsilon_down[(left.index, right.index)]  # type: ignore[attr-defined]
            if rule == "SAME_CHIRAL_D":
                assert isinstance(left, D)
                factor = Fraction(epsilon, 2)
                replacement_token: Token = D2(left.tag, left.momentum)
            else:
                assert isinstance(left, BarD)
                factor = Fraction(-epsilon, 2)
                replacement_token = BarD2(left.tag, left.momentum)
            return (
                self._replace_slice(
                    term,
                    choice,
                    (replacement_token,),
                    factor,
                    _ledger(factor, rule, f"{type(left).__name__}_{left.index}{right.index}"),
                ),
            )
        if rule == "SAME_CHIRAL_NILPOTENCE":
            return ()
        if rule == "MIXED_ANTICOMMUTATOR":
            left, right = selected
            assert isinstance(left, D) and isinstance(right, BarD)
            reordered = self._replace_slice(
                term,
                choice,
                (right, left),
                -1,
                _ledger(-1, rule, "BarD D branch"),
            )
            momentum = self._replace_slice(
                term,
                choice,
                (MixedMomentum(left.index, right.index, left.tag, left.momentum),),
                -2,
                _ledger(-2, rule, "-2 D_vector branch"),
            )
            return reordered, momentum
        if rule == "EXTERNAL_LEG_ACTION":
            operator, leg = selected
            assert isinstance(leg, ExternalLeg)
            annihilated = (
                isinstance(operator, (BarD, BarD2)) and leg.chirality is Chirality.CHIRAL
            ) or (
                isinstance(operator, (D, D2)) and leg.chirality is Chirality.ANTICHIRAL
            )
            if annihilated:
                return ()
            if isinstance(operator, D):
                derivative = ExternalDerivative(
                    leg.leg_id, "D", leg.tag, operator.momentum, undotted=operator.index
                )
            elif isinstance(operator, BarD):
                derivative = ExternalDerivative(
                    leg.leg_id, "barD", leg.tag, operator.momentum, dotted=operator.index
                )
            elif isinstance(operator, D2):
                derivative = ExternalDerivative(leg.leg_id, "D2", leg.tag, operator.momentum)
            elif isinstance(operator, BarD2):
                derivative = ExternalDerivative(leg.leg_id, "barD2", leg.tag, operator.momentum)
            else:
                assert isinstance(operator, MixedMomentum)
                derivative = ExternalDerivative(
                    leg.leg_id,
                    "vector",
                    leg.tag,
                    operator.momentum,
                    operator.undotted,
                    operator.dotted,
                )
            return (
                self._replace_slice(
                    term,
                    choice,
                    (derivative,),
                    1,
                    _ledger(1, rule, type(operator).__name__, LedgerKind.CHIRALITY),
                ),
            )
        if rule == "COLLAPSE_PROPAGATOR":
            square_index, propagator_index = choice.positions
            square = word[square_index]
            propagator = word[propagator_index]
            assert isinstance(square, MomentumSquare) and isinstance(propagator, Propagator)
            remaining = [
                token
                for index, token in enumerate(word)
                if index not in choice.positions
            ]
            remaining.insert(
                min(choice.positions),
                Collapse(propagator.edge_id, propagator.momentum, "p^2 times 1/p^2"),
            )
            return (
                Term(
                    term.coefficient,
                    tuple(remaining),
                    term.sign_ledger
                    + (_ledger(1, rule, propagator.edge_id, LedgerKind.COLLAPSE),),
                ),
            )
        if rule == "CENTRAL_MOMENTUM_SQUARE_LEFT":
            left, square = selected
            assert isinstance(square, MomentumSquare)
            return (
                self._replace_slice(
                    term,
                    choice,
                    (square, left),
                    1,
                    _ledger(1, rule, "p^2 central"),
                ),
            )
        raise KeyError(f"unknown rewrite rule: {rule}")

    def _normalise(self, term: Term, steps: list[RewriteStep]) -> list[Term]:
        if not term.coefficient:
            return []
        self.validate_phase_sequence(term)
        matches = self.matches(term)
        if not matches:
            return [term]
        choice = matches[0]
        outputs = self.apply(term, choice)
        before = termination_measure(term)
        after = tuple(termination_measure(output) for output in outputs)
        if any(value >= before for value in after):
            raise RuntimeError(
                f"non-decreasing rewrite {choice.rule_id}: {before} -> {after}"
            )
        steps.append(RewriteStep(choice.rule_id, choice.positions, term, outputs, before, after))
        result: list[Term] = []
        for output in outputs:
            result.extend(self._normalise(output, steps))
        return result

    def compile(self, terms: Iterable[Term]) -> NormalFormTrace:
        inputs = tuple(terms)
        steps: list[RewriteStep] = []
        leaves: list[Term] = []
        for term in inputs:
            leaves.extend(self._normalise(term, steps))
        coefficients: dict[tuple[Token, ...], GaussianRational] = {}
        ledgers: dict[tuple[Token, ...], list[tuple[SignLedgerEntry, ...]]] = {}
        for term in leaves:
            coefficients[term.word] = coefficients.get(term.word, ZERO) + term.coefficient
            ledgers.setdefault(term.word, []).append(term.sign_ledger)
        outputs = tuple(
            NormalFormTerm(
                coefficients[word],
                word,
                tuple(
                    sorted(
                        ledgers[word],
                        key=lambda ledger: json.dumps(
                            [entry.to_json() for entry in ledger], sort_keys=True
                        ),
                    )
                ),
            )
            for word in sorted(coefficients, key=word_key)
            if coefficients[word]
        )
        return NormalFormTrace(inputs, tuple(steps), outputs, True, RULE_ORDER)

    @staticmethod
    def _signature(trace: NormalFormTrace) -> tuple[tuple[str, tuple[str, str]], ...]:
        return tuple(
            (word_key(term.word), (str(term.coefficient.re), str(term.coefficient.im)))
            for term in trace.outputs
        )

    def audit_critical_pairs(self, source: Term) -> tuple[CriticalPairAudit, ...]:
        matches = self.matches(source)
        audits: list[CriticalPairAudit] = []
        for left_index, left in enumerate(matches):
            for right in matches[left_index + 1 :]:
                if not set(left.positions).intersection(right.positions):
                    continue
                left_trace = self.compile(self.apply(source, left))
                right_trace = self.compile(self.apply(source, right))
                left_signature = self._signature(left_trace)
                right_signature = self._signature(right_trace)
                audits.append(
                    CriticalPairAudit(
                        source,
                        left,
                        right,
                        left_signature,
                        right_signature,
                        left_signature == right_signature,
                    )
                )
        return tuple(audits)


def compile_job(
    job: DAlgebraJob, compiler: DAlgebraCompiler | None = None
) -> DAlgebraResult:
    """Validate and compile one provenance-bound D-word job."""

    job.validate()
    selected = compiler or DAlgebraCompiler()
    source = Term(job.coefficient, job.operator_word)
    try:
        normal_form = selected.compile((source,))
    except UnimplementedPhaseSequenceError as error:
        return DAlgebraResult(
            job_id=job.job_id,
            notation_hash=job.notation_hash,
            graph_hash=job.graph_hash,
            amplitude_id=job.amplitude_id,
            input_job_sha256=job.sha256(),
            normal_form=None,
            critical_pair_audits=(),
            status=error.code,
            error=error.to_json(),
        )
    audits = selected.audit_critical_pairs(source)
    passed = normal_form.terminated and all(audit.joinable for audit in audits)
    return DAlgebraResult(
        job_id=job.job_id,
        notation_hash=job.notation_hash,
        graph_hash=job.graph_hash,
        amplitude_id=job.amplitude_id,
        input_job_sha256=job.sha256(),
        normal_form=normal_form,
        critical_pair_audits=audits,
        status="PASS" if passed else "FAIL",
        error=None,
    )


@dataclass(frozen=True)
class MatrixOracleAdapter:
    identity: object
    zero: object
    add: Callable[[object, object], object]
    multiply: Callable[[object, object], object]
    scale: Callable[[object, object], object]
    scalar: Callable[[GaussianRational], object]
    operator: Callable[[Token], object]


def evaluate_terms_with_oracle(
    terms: Iterable[Term | NormalFormTerm], adapter: MatrixOracleAdapter
) -> object:
    total = adapter.zero
    for term in terms:
        product = adapter.identity
        for token in term.word:
            product = adapter.multiply(product, adapter.operator(token))
        total = adapter.add(
            total,
            adapter.scale(adapter.scalar(term.coefficient), product),
        )
    return total


def critical_pair_suite() -> tuple[CriticalPairAudit, ...]:
    """Audit only this declared finite list; this is not global confluence."""

    compiler = DAlgebraCompiler()
    tag = EndpointTag("e0", "loop")
    p = "k"
    sources = (
        Term(1, (D2(tag, p), BarD2(tag, p), D2(tag, p), BarD2(tag, p))),
        Term(1, (BarD2(tag, p), D2(tag, p), BarD2(tag, p), D2(tag, p))),
        Term(1, (D("+", tag, p), D("+", tag, p), D("+", tag, p))),
    )
    return tuple(audit for source in sources for audit in compiler.audit_critical_pairs(source))


def main() -> int:
    audits = critical_pair_suite()
    payload = {
        "schema": 1,
        "scope": "ISOLATED_EDGE_TAGGED_D_ALGEBRA_NO_GRAPH_COEFFICIENT",
        "implementation_status": IMPLEMENTATION_STATUS,
        "implemented_phases": list(IMPLEMENTED_PHASES),
        "endpoint_transfer_policy": ENDPOINT_TRANSFER_POLICY,
        "critical_pair_scope": DECLARED_CRITICAL_PAIR_SCOPE,
        "critical_pairs": [audit.to_json() for audit in audits],
        "status": "PASS" if audits and all(audit.joinable for audit in audits) else "FAIL",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
