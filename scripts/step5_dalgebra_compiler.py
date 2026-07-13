#!/usr/bin/env python3
"""Deterministic, edge-tagged flat-superspace D-algebra compiler.

Operator words are written from left to right and the rightmost operator acts
first.  Numerical coefficients lie in Q(i); momentum factors remain typed
tokens.  This module contains no graph or anomaly coefficient.
"""

from __future__ import annotations

import hashlib
import json
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
