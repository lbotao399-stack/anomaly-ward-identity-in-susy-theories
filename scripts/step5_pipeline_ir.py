#!/usr/bin/env python3
"""Immutable notation, graph, and amplitude IR for the Step-5 pipeline.

The module is deliberately independent of the existing physical WW seed.  It
contains no imported Feynman rule or anomaly coefficient.  All numerical
coefficients live in Q(i,sqrt(2)), every symbolic factor resolves through one
frozen notation schema, and every graph/amplitude carries the schema hash that
typed it.  ``Qi`` remains the exact WW-sector subring adapter.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping


class PipelineIRError(ValueError):
    """Base class for typed-pipeline validation failures."""


class UndefinedSymbolError(PipelineIRError):
    """A symbolic dependency is absent from the notation schema."""


class HashDriftError(PipelineIRError):
    """An artifact was typed by a different notation schema or graph."""


class PropagatorPortError(PipelineIRError):
    """An internal edge does not satisfy its declared propagator signature."""


class MomentumConservationError(PipelineIRError):
    """An all-incoming momentum sum is nonzero."""


def _fraction_payload(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def _fraction_from_payload(payload: Mapping[str, object]) -> Fraction:
    if set(payload) != {"numerator", "denominator"}:
        raise PipelineIRError("a rational payload requires numerator and denominator")
    numerator = payload["numerator"]
    denominator = payload["denominator"]
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise PipelineIRError("rational numerator and denominator must be integers")
    if denominator == 0:
        raise PipelineIRError("a rational denominator cannot vanish")
    return Fraction(numerator, denominator)


def _canonical_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(payload: object) -> str:
    return hashlib.sha256(_canonical_json(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class Qi:
    """Exact element ``real + i*imag`` of Q(i)."""

    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "real", Fraction(self.real))
        object.__setattr__(self, "imag", Fraction(self.imag))

    @classmethod
    def rational(cls, numerator: int, denominator: int = 1) -> "Qi":
        return cls(Fraction(numerator, denominator), Fraction(0))

    @classmethod
    def imaginary(cls, numerator: int, denominator: int = 1) -> "Qi":
        return cls(Fraction(0), Fraction(numerator, denominator))

    def __add__(self, other: object) -> "Qi":
        if not isinstance(other, Qi):
            return NotImplemented
        return Qi(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: object) -> "Qi":
        if not isinstance(other, Qi):
            return NotImplemented
        return Qi(self.real - other.real, self.imag - other.imag)

    def __neg__(self) -> "Qi":
        return Qi(-self.real, -self.imag)

    def __mul__(self, other: object) -> "Qi":
        if not isinstance(other, Qi):
            return NotImplemented
        return Qi(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __truediv__(self, other: object) -> "Qi":
        if not isinstance(other, Qi):
            return NotImplemented
        norm = other.real * other.real + other.imag * other.imag
        if norm == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return Qi(
            (self.real * other.real + self.imag * other.imag) / norm,
            (self.imag * other.real - self.real * other.imag) / norm,
        )

    def conjugate(self) -> "Qi":
        return Qi(self.real, -self.imag)

    def canonical_dict(self) -> dict[str, object]:
        return {"real": _fraction_payload(self.real), "imag": _fraction_payload(self.imag)}

    def to_exact_scalar(self) -> "ExactScalar":
        return ExactScalar(self.real, self.imag)

    @classmethod
    def from_dict(cls, payload: Mapping[str, object]) -> "Qi":
        if set(payload) != {"real", "imag"}:
            raise PipelineIRError("a Q(i) payload requires real and imag")
        real = payload["real"]
        imag = payload["imag"]
        if not isinstance(real, Mapping) or not isinstance(imag, Mapping):
            raise PipelineIRError("Q(i) components must be rational payloads")
        return cls(_fraction_from_payload(real), _fraction_from_payload(imag))


QI_ZERO = Qi()
QI_ONE = Qi.rational(1)


def _qsqrt2_multiply(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Multiply ``x0+x1*sqrt(2)`` and ``y0+y1*sqrt(2)`` exactly."""

    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


@dataclass(frozen=True, slots=True)
class ExactScalar:
    """Exact scalar ``a+b*i+c*sqrt(2)+d*i*sqrt(2)``.

    The defining relations are ``i^2=-1``, ``sqrt(2)^2=2``, and commuting
    generators.  This is the degree-four field Q(i,sqrt(2)).
    """

    rational_part: Fraction = Fraction(0)
    i_part: Fraction = Fraction(0)
    sqrt2_part: Fraction = Fraction(0)
    i_sqrt2_part: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        for name in ("rational_part", "i_part", "sqrt2_part", "i_sqrt2_part"):
            object.__setattr__(self, name, Fraction(getattr(self, name)))

    @classmethod
    def rational(cls, numerator: int, denominator: int = 1) -> "ExactScalar":
        return cls(Fraction(numerator, denominator))

    @classmethod
    def imaginary(cls, numerator: int, denominator: int = 1) -> "ExactScalar":
        return cls(i_part=Fraction(numerator, denominator))

    @classmethod
    def sqrt2(cls, numerator: int, denominator: int = 1) -> "ExactScalar":
        return cls(sqrt2_part=Fraction(numerator, denominator))

    @classmethod
    def i_sqrt2(cls, numerator: int, denominator: int = 1) -> "ExactScalar":
        return cls(i_sqrt2_part=Fraction(numerator, denominator))

    @classmethod
    def from_qi(cls, value: Qi) -> "ExactScalar":
        return cls(value.real, value.imag)

    def to_qi(self) -> Qi:
        if self.sqrt2_part or self.i_sqrt2_part:
            raise PipelineIRError("the scalar is outside the Q(i) WW subring")
        return Qi(self.rational_part, self.i_part)

    @property
    def is_zero(self) -> bool:
        return not any(
            (self.rational_part, self.i_part, self.sqrt2_part, self.i_sqrt2_part)
        )

    def __add__(self, other: object) -> "ExactScalar":
        if not isinstance(other, ExactScalar):
            return NotImplemented
        return ExactScalar(
            self.rational_part + other.rational_part,
            self.i_part + other.i_part,
            self.sqrt2_part + other.sqrt2_part,
            self.i_sqrt2_part + other.i_sqrt2_part,
        )

    def __sub__(self, other: object) -> "ExactScalar":
        if not isinstance(other, ExactScalar):
            return NotImplemented
        return self + (-other)

    def __neg__(self) -> "ExactScalar":
        return ExactScalar(
            -self.rational_part,
            -self.i_part,
            -self.sqrt2_part,
            -self.i_sqrt2_part,
        )

    def __mul__(self, other: object) -> "ExactScalar":
        if not isinstance(other, ExactScalar):
            return NotImplemented
        left_real = (self.rational_part, self.sqrt2_part)
        left_imag = (self.i_part, self.i_sqrt2_part)
        right_real = (other.rational_part, other.sqrt2_part)
        right_imag = (other.i_part, other.i_sqrt2_part)
        real_product = _qsqrt2_multiply(left_real, right_real)
        imag_product = _qsqrt2_multiply(left_imag, right_imag)
        cross_left = _qsqrt2_multiply(left_real, right_imag)
        cross_right = _qsqrt2_multiply(left_imag, right_real)
        return ExactScalar(
            real_product[0] - imag_product[0],
            cross_left[0] + cross_right[0],
            real_product[1] - imag_product[1],
            cross_left[1] + cross_right[1],
        )

    def conjugate(self) -> "ExactScalar":
        """Complex conjugation: ``i -> -i`` and ``sqrt(2) -> sqrt(2)``."""

        return ExactScalar(
            self.rational_part,
            -self.i_part,
            self.sqrt2_part,
            -self.i_sqrt2_part,
        )

    def sqrt2_conjugate(self) -> "ExactScalar":
        """The second field automorphism: ``sqrt(2) -> -sqrt(2)``."""

        return ExactScalar(
            self.rational_part,
            self.i_part,
            -self.sqrt2_part,
            -self.i_sqrt2_part,
        )

    def inverse(self) -> "ExactScalar":
        if self.is_zero:
            raise ZeroDivisionError("division by zero in Q(i,sqrt(2))")
        u = (self.rational_part, self.sqrt2_part)
        v = (self.i_part, self.i_sqrt2_part)
        u_squared = _qsqrt2_multiply(u, u)
        v_squared = _qsqrt2_multiply(v, v)
        norm = (u_squared[0] + v_squared[0], u_squared[1] + v_squared[1])
        rational_norm = norm[0] * norm[0] - 2 * norm[1] * norm[1]
        if rational_norm == 0:
            raise ZeroDivisionError("noninvertible scalar in Q(i,sqrt(2))")
        inverse_norm = (norm[0] / rational_norm, -norm[1] / rational_norm)
        inverse_real = _qsqrt2_multiply(u, inverse_norm)
        inverse_imag = _qsqrt2_multiply((-v[0], -v[1]), inverse_norm)
        return ExactScalar(
            inverse_real[0],
            inverse_imag[0],
            inverse_real[1],
            inverse_imag[1],
        )

    def __truediv__(self, other: object) -> "ExactScalar":
        if not isinstance(other, ExactScalar):
            return NotImplemented
        return self * other.inverse()

    def canonical_dict(self) -> dict[str, object]:
        return {
            "rational": _fraction_payload(self.rational_part),
            "i": _fraction_payload(self.i_part),
            "sqrt2": _fraction_payload(self.sqrt2_part),
            "i_sqrt2": _fraction_payload(self.i_sqrt2_part),
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, object]) -> "ExactScalar":
        expected = {"rational", "i", "sqrt2", "i_sqrt2"}
        if set(payload) != expected:
            raise PipelineIRError("an ExactScalar payload requires four basis components")
        components = []
        for name in ("rational", "i", "sqrt2", "i_sqrt2"):
            value = payload[name]
            if not isinstance(value, Mapping):
                raise PipelineIRError(f"ExactScalar component {name} must be rational")
            components.append(_fraction_from_payload(value))
        return cls(*components)


EXACT_ZERO = ExactScalar()
EXACT_ONE = ExactScalar.rational(1)
EXACT_I = ExactScalar.imaginary(1)
EXACT_SQRT2 = ExactScalar.sqrt2(1)
EXACT_I_SQRT2 = ExactScalar.i_sqrt2(1)

ExactCoefficient = Qi | ExactScalar


def _exact_coefficient_from_payload(payload: Mapping[str, object]) -> ExactCoefficient:
    if set(payload) == {"real", "imag"}:
        return Qi.from_dict(payload)
    if set(payload) == {"rational", "i", "sqrt2", "i_sqrt2"}:
        return ExactScalar.from_dict(payload)
    raise PipelineIRError("unknown exact-coefficient basis payload")


def _multiply_exact_coefficients(
    left: ExactCoefficient,
    right: ExactCoefficient,
) -> ExactCoefficient:
    if isinstance(left, Qi) and isinstance(right, Qi):
        return left * right
    left_full = left.to_exact_scalar() if isinstance(left, Qi) else left
    right_full = right.to_exact_scalar() if isinstance(right, Qi) else right
    return left_full * right_full


class SymbolKind(str, Enum):
    COUPLING = "COUPLING"
    NORMALIZATION = "NORMALIZATION"
    MOMENTUM = "MOMENTUM"
    REGULATOR = "REGULATOR"
    METRIC = "METRIC"
    SCALE = "SCALE"
    OTHER = "OTHER"


class Statistics(str, Enum):
    BOSON = "BOSON"
    FERMION = "FERMION"


class Chirality(str, Enum):
    CHIRAL = "CHIRAL"
    ANTICHIRAL = "ANTICHIRAL"
    REAL = "REAL"
    UNCONSTRAINED = "UNCONSTRAINED"


class PortSector(str, Enum):
    BACKGROUND = "BACKGROUND"
    QUANTUM = "QUANTUM"


class Flow(str, Enum):
    IN = "IN"
    OUT = "OUT"


class Variance(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    FIXED = "FIXED"


@dataclass(frozen=True, slots=True)
class SymbolSpec:
    name: str
    kind: SymbolKind

    def __post_init__(self) -> None:
        if not self.name:
            raise PipelineIRError("symbol names must be nonempty")

    def canonical_dict(self) -> dict[str, str]:
        return {"name": self.name, "kind": self.kind.value}


@dataclass(frozen=True, slots=True)
class DerivativeSpec:
    name: str
    parity: int
    index_space: str

    def __post_init__(self) -> None:
        if not self.name or not self.index_space:
            raise PipelineIRError("derivative name and index space are mandatory")
        if self.parity not in (0, 1):
            raise PipelineIRError("derivative parity must be 0 or 1")

    def canonical_dict(self) -> dict[str, object]:
        return {"name": self.name, "parity": self.parity, "index_space": self.index_space}


@dataclass(frozen=True, slots=True)
class DerivativeTerm:
    coefficient: ExactCoefficient
    ordered_derivatives: tuple[str, ...] = ()
    symbol_factors: tuple[str, ...] = ()
    tensor_factors: tuple[str, ...] = ()

    def canonical_dict(self) -> dict[str, object]:
        return {
            "coefficient": self.coefficient.canonical_dict(),
            "ordered_derivatives": list(self.ordered_derivatives),
            "symbol_factors": list(self.symbol_factors),
            "tensor_factors": list(self.tensor_factors),
        }


@dataclass(frozen=True, slots=True)
class DerivativeRule:
    lhs: tuple[str, ...]
    rhs: tuple[DerivativeTerm, ...]
    conditions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.lhs or not self.rhs:
            raise PipelineIRError("a derivative rule requires nonempty lhs and rhs")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "lhs": list(self.lhs),
            "rhs": [term.canonical_dict() for term in self.rhs],
            "conditions": list(self.conditions),
        }


@dataclass(frozen=True, slots=True)
class FieldSpec:
    name: str
    statistics: Statistics
    chirality: Chirality
    index_spaces: tuple[str, ...]
    index_variances: tuple[Variance, ...]

    def __post_init__(self) -> None:
        if not self.name:
            raise PipelineIRError("field names must be nonempty")
        if len(self.index_spaces) != len(self.index_variances):
            raise PipelineIRError("field index-space and variance arities differ")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "statistics": self.statistics.value,
            "chirality": self.chirality.value,
            "index_spaces": list(self.index_spaces),
            "index_variances": [item.value for item in self.index_variances],
        }


@dataclass(frozen=True, slots=True)
class PortSpec:
    name: str
    field_name: str
    allowed_sectors: tuple[PortSector, ...]
    allowed_flows: tuple[Flow, ...]

    def __post_init__(self) -> None:
        if not self.name or not self.field_name:
            raise PipelineIRError("port and field names must be nonempty")
        if not self.allowed_sectors or not self.allowed_flows:
            raise PipelineIRError("a port must declare allowed sectors and flows")
        if len(set(self.allowed_sectors)) != len(self.allowed_sectors):
            raise PipelineIRError("a port repeats an allowed sector")
        if len(set(self.allowed_flows)) != len(self.allowed_flows):
            raise PipelineIRError("a port repeats an allowed flow")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "field_name": self.field_name,
            "allowed_sectors": sorted(item.value for item in self.allowed_sectors),
            "allowed_flows": sorted(item.value for item in self.allowed_flows),
        }


@dataclass(frozen=True, slots=True)
class PropagatorSpec:
    name: str
    left_port_spec: str
    right_port_spec: str
    coefficient: ExactCoefficient
    ordered_left_derivatives: tuple[str, ...] = ()
    ordered_right_derivatives: tuple[str, ...] = ()
    symbol_factors: tuple[str, ...] = ()
    tensor_factors: tuple[str, ...] = ()
    symmetric: bool = False

    def __post_init__(self) -> None:
        if not self.name or not self.left_port_spec or not self.right_port_spec:
            raise PipelineIRError("propagator and endpoint port names are mandatory")

    def accepts(self, left: str, right: str) -> bool:
        exact = (left, right) == (self.left_port_spec, self.right_port_spec)
        reverse = self.symmetric and (left, right) == (
            self.right_port_spec,
            self.left_port_spec,
        )
        return exact or reverse

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "left_port_spec": self.left_port_spec,
            "right_port_spec": self.right_port_spec,
            "coefficient": self.coefficient.canonical_dict(),
            "ordered_left_derivatives": list(self.ordered_left_derivatives),
            "ordered_right_derivatives": list(self.ordered_right_derivatives),
            "symbol_factors": list(self.symbol_factors),
            "tensor_factors": list(self.tensor_factors),
            "symmetric": self.symmetric,
        }


@dataclass(frozen=True, slots=True)
class TensorSpec:
    name: str
    tensor_class: str
    index_spaces: tuple[str, ...]
    variances: tuple[Variance, ...]

    def __post_init__(self) -> None:
        if not self.name or not self.tensor_class:
            raise PipelineIRError("tensor name and class are mandatory")
        if len(self.index_spaces) != len(self.variances):
            raise PipelineIRError("tensor index-space and variance arities differ")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "tensor_class": self.tensor_class,
            "index_spaces": list(self.index_spaces),
            "variances": [item.value for item in self.variances],
        }


@dataclass(frozen=True, slots=True)
class FourierDREDData:
    fourier_phase: str
    derivative_momentum_map: str
    dimension: str
    loop_measure: str
    spin_metric_symbol: str
    loop_metric_symbol: str
    evanescent_metric_symbol: str
    epsilon_symbol: str
    mu_symbol: str

    def __post_init__(self) -> None:
        if any(
            not item
            for item in (
                self.fourier_phase,
                self.derivative_momentum_map,
                self.dimension,
                self.loop_measure,
                self.spin_metric_symbol,
                self.loop_metric_symbol,
                self.evanescent_metric_symbol,
                self.epsilon_symbol,
                self.mu_symbol,
            )
        ):
            raise PipelineIRError("Fourier/DRED data must be complete")

    @property
    def symbol_factors(self) -> tuple[str, ...]:
        return (
            self.spin_metric_symbol,
            self.loop_metric_symbol,
            self.evanescent_metric_symbol,
            self.epsilon_symbol,
            self.mu_symbol,
        )

    def canonical_dict(self) -> dict[str, str]:
        return {
            "fourier_phase": self.fourier_phase,
            "derivative_momentum_map": self.derivative_momentum_map,
            "dimension": self.dimension,
            "loop_measure": self.loop_measure,
            "spin_metric_symbol": self.spin_metric_symbol,
            "loop_metric_symbol": self.loop_metric_symbol,
            "evanescent_metric_symbol": self.evanescent_metric_symbol,
            "epsilon_symbol": self.epsilon_symbol,
            "mu_symbol": self.mu_symbol,
        }


@dataclass(frozen=True, slots=True)
class AdapterAliasSpec:
    """Typed adapter from a composite request token to primitive schema names."""

    name: str
    target_kind: str
    expression: str
    symbol_factors: tuple[str, ...] = ()
    derivative_factors: tuple[str, ...] = ()
    field_factors: tuple[str, ...] = ()
    tensor_factors: tuple[str, ...] = ()
    port_factors: tuple[str, ...] = ()
    propagator_factors: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.name or not self.target_kind or not self.expression:
            raise PipelineIRError("adapter aliases require name, kind, and expression")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "target_kind": self.target_kind,
            "expression": self.expression,
            "symbol_factors": list(self.symbol_factors),
            "derivative_factors": list(self.derivative_factors),
            "field_factors": list(self.field_factors),
            "tensor_factors": list(self.tensor_factors),
            "port_factors": list(self.port_factors),
            "propagator_factors": list(self.propagator_factors),
        }


@dataclass(frozen=True, slots=True)
class ScalarRingSpec:
    name: str
    generators: tuple[str, ...]
    relations: tuple[str, ...]
    ordered_basis: tuple[str, ...]
    ww_subring_adapter: str

    def __post_init__(self) -> None:
        if not self.name or not self.ww_subring_adapter:
            raise PipelineIRError("scalar ring name and WW adapter are mandatory")
        if not self.generators or len(set(self.generators)) != len(self.generators):
            raise PipelineIRError("scalar-ring generators must be nonempty and unique")
        if not self.relations or not self.ordered_basis:
            raise PipelineIRError("scalar-ring relations and ordered basis are mandatory")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "generators": list(self.generators),
            "relations": list(self.relations),
            "ordered_basis": list(self.ordered_basis),
            "ww_subring_adapter": self.ww_subring_adapter,
        }

    def admits(self, value: ExactCoefficient) -> bool:
        if isinstance(value, Qi):
            return True
        if self.name == "Q(i)":
            return value.sqrt2_part == 0 and value.i_sqrt2_part == 0
        if self.name == "Q(i,sqrt2)":
            return True
        return False

    @classmethod
    def from_dict(cls, payload: Mapping[str, object]) -> "ScalarRingSpec":
        expected = {
            "name",
            "generators",
            "relations",
            "ordered_basis",
            "ww_subring_adapter",
        }
        if set(payload) != expected:
            raise PipelineIRError("scalar-ring JSON shape mismatch")
        return cls(
            str(payload["name"]),
            tuple(str(value) for value in payload["generators"]),  # type: ignore[union-attr]
            tuple(str(value) for value in payload["relations"]),  # type: ignore[union-attr]
            tuple(str(value) for value in payload["ordered_basis"]),  # type: ignore[union-attr]
            str(payload["ww_subring_adapter"]),
        )


QI_SCALAR_RING = ScalarRingSpec(
    "Q(i)",
    ("i",),
    ("i^2=-1",),
    ("1", "i"),
    "Qi",
)

PROJECT_N4_SCALAR_RING = ScalarRingSpec(
    "Q(i,sqrt2)",
    ("i", "sqrt2"),
    ("i^2=-1", "sqrt2^2=2", "i*sqrt2=sqrt2*i"),
    ("1", "i", "sqrt2", "i*sqrt2"),
    "Qi={a+b*i+c*sqrt2+d*i*sqrt2 | c=d=0}",
)


def _unique_named(items: Iterable[object], label: str) -> dict[str, object]:
    result: dict[str, object] = {}
    for item in items:
        name = getattr(item, "name")
        if name in result:
            raise PipelineIRError(f"duplicate {label} name: {name}")
        result[name] = item
    return result


@dataclass(frozen=True, slots=True)
class NotationSchema:
    schema_id: str
    index_spaces: tuple[str, ...]
    symbols: tuple[SymbolSpec, ...]
    derivatives: tuple[DerivativeSpec, ...]
    derivative_rules: tuple[DerivativeRule, ...]
    fields: tuple[FieldSpec, ...]
    ports: tuple[PortSpec, ...]
    propagators: tuple[PropagatorSpec, ...]
    tensors: tuple[TensorSpec, ...]
    fourier_dred: FourierDREDData
    required_tensors: tuple[str, ...] = ()
    adapter_aliases: tuple[AdapterAliasSpec, ...] = ()
    scalar_ring: ScalarRingSpec = QI_SCALAR_RING

    def __post_init__(self) -> None:
        if not self.schema_id:
            raise PipelineIRError("schema id must be nonempty")
        if len(set(self.index_spaces)) != len(self.index_spaces):
            raise PipelineIRError("index-space names must be unique")
        symbol_map = _unique_named(self.symbols, "symbol")
        derivative_map = _unique_named(self.derivatives, "derivative")
        field_map = _unique_named(self.fields, "field")
        port_map = _unique_named(self.ports, "port")
        _unique_named(self.propagators, "propagator")
        tensor_map = _unique_named(self.tensors, "tensor")
        alias_map = _unique_named(self.adapter_aliases, "adapter alias")
        if set(symbol_map) & set(alias_map):
            raise PipelineIRError("adapter aliases cannot shadow primitive symbols")

        for derivative in self.derivatives:
            if derivative.index_space not in self.index_spaces:
                raise UndefinedSymbolError(
                    f"derivative {derivative.name} uses undefined index space {derivative.index_space}"
                )
        for field in self.fields:
            self._require_subset(field.index_spaces, self.index_spaces, f"field {field.name}")
        for port in self.ports:
            if port.field_name not in field_map:
                raise UndefinedSymbolError(
                    f"port {port.name} uses undefined field {port.field_name}"
                )
        for rule in self.derivative_rules:
            self._require_subset(rule.lhs, derivative_map, "derivative-rule lhs")
            for term in rule.rhs:
                if not self.scalar_ring.admits(term.coefficient):
                    raise PipelineIRError(
                        f"derivative-rule coefficient is outside {self.scalar_ring.name}"
                    )
                self._require_subset(
                    term.ordered_derivatives,
                    derivative_map,
                    "derivative-rule rhs",
                )
                self._require_subset(term.symbol_factors, symbol_map, "derivative-rule symbols")
                self._require_subset(term.tensor_factors, tensor_map, "derivative-rule tensors")
        for propagator in self.propagators:
            if not self.scalar_ring.admits(propagator.coefficient):
                raise PipelineIRError(
                    f"propagator {propagator.name} coefficient is outside {self.scalar_ring.name}"
                )
            self._require_subset(
                (propagator.left_port_spec, propagator.right_port_spec),
                port_map,
                f"propagator {propagator.name} ports",
            )
            left = port_map[propagator.left_port_spec]
            right = port_map[propagator.right_port_spec]
            assert isinstance(left, PortSpec) and isinstance(right, PortSpec)
            if PortSector.QUANTUM not in left.allowed_sectors or PortSector.QUANTUM not in right.allowed_sectors:
                raise PropagatorPortError(
                    f"propagator {propagator.name} endpoints must admit QUANTUM ports"
                )
            self._require_subset(
                propagator.ordered_left_derivatives + propagator.ordered_right_derivatives,
                derivative_map,
                f"propagator {propagator.name} derivatives",
            )
            self._require_subset(
                propagator.symbol_factors,
                symbol_map,
                f"propagator {propagator.name} symbols",
            )
            self._require_subset(
                propagator.tensor_factors,
                tensor_map,
                f"propagator {propagator.name} tensors",
            )
        for tensor in self.tensors:
            self._require_subset(
                tensor.index_spaces,
                self.index_spaces,
                f"tensor {tensor.name}",
            )
        self._require_subset(self.required_tensors, tensor_map, "required WW tensors")
        for alias in self.adapter_aliases:
            self._require_subset(alias.symbol_factors, symbol_map, f"alias {alias.name} symbols")
            self._require_subset(
                alias.derivative_factors,
                derivative_map,
                f"alias {alias.name} derivatives",
            )
            self._require_subset(alias.field_factors, field_map, f"alias {alias.name} fields")
            self._require_subset(alias.tensor_factors, tensor_map, f"alias {alias.name} tensors")
            self._require_subset(alias.port_factors, port_map, f"alias {alias.name} ports")
            self._require_subset(
                alias.propagator_factors,
                {item.name: item for item in self.propagators},
                f"alias {alias.name} propagators",
            )
        self._require_subset(
            self.fourier_dred.symbol_factors,
            {**symbol_map, **alias_map},
            "Fourier/DRED symbols",
        )

    @staticmethod
    def _require_subset(values: Iterable[str], available: Mapping[str, object] | Iterable[str], context: str) -> None:
        allowed = set(available)
        for value in values:
            if value not in allowed:
                raise UndefinedSymbolError(f"{context} references undefined symbol {value}")

    @property
    def symbol_map(self) -> dict[str, SymbolSpec]:
        return {item.name: item for item in self.symbols}

    @property
    def derivative_map(self) -> dict[str, DerivativeSpec]:
        return {item.name: item for item in self.derivatives}

    @property
    def field_map(self) -> dict[str, FieldSpec]:
        return {item.name: item for item in self.fields}

    @property
    def port_map(self) -> dict[str, PortSpec]:
        return {item.name: item for item in self.ports}

    @property
    def propagator_map(self) -> dict[str, PropagatorSpec]:
        return {item.name: item for item in self.propagators}

    @property
    def tensor_map(self) -> dict[str, TensorSpec]:
        return {item.name: item for item in self.tensors}

    def canonical_dict(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "index_spaces": sorted(self.index_spaces),
            "symbols": [item.canonical_dict() for item in sorted(self.symbols, key=lambda x: x.name)],
            "derivatives": [
                item.canonical_dict() for item in sorted(self.derivatives, key=lambda x: x.name)
            ],
            "derivative_rules": [
                item.canonical_dict()
                for item in sorted(self.derivative_rules, key=lambda x: _canonical_json(x.canonical_dict()))
            ],
            "fields": [item.canonical_dict() for item in sorted(self.fields, key=lambda x: x.name)],
            "ports": [item.canonical_dict() for item in sorted(self.ports, key=lambda x: x.name)],
            "propagators": [
                item.canonical_dict() for item in sorted(self.propagators, key=lambda x: x.name)
            ],
            "tensors": [item.canonical_dict() for item in sorted(self.tensors, key=lambda x: x.name)],
            "fourier_dred": self.fourier_dred.canonical_dict(),
            "required_tensors": sorted(self.required_tensors),
            "adapter_aliases": [
                item.canonical_dict()
                for item in sorted(self.adapter_aliases, key=lambda x: x.name)
            ],
            "scalar_ring": self.scalar_ring.canonical_dict(),
        }

    def canonical_json(self) -> str:
        return _canonical_json(self.canonical_dict())

    @classmethod
    def from_canonical_json(cls, payload: str) -> "NotationSchema":
        value = json.loads(payload)
        if not isinstance(value, dict):
            raise PipelineIRError("notation JSON root must be an object")
        return cls.from_canonical_dict(value)

    @classmethod
    def from_canonical_dict(cls, payload: Mapping[str, object]) -> "NotationSchema":
        def qi(value: Mapping[str, object]) -> ExactCoefficient:
            return _exact_coefficient_from_payload(value)

        def field_spec(item: Mapping[str, object]) -> FieldSpec:
            required = {
                "name",
                "statistics",
                "chirality",
                "index_spaces",
                "index_variances",
            }
            if set(item) != required:
                raise PipelineIRError(
                    "field JSON must carry explicit index_spaces and index_variances"
                )
            return FieldSpec(
                str(item["name"]),
                Statistics(item["statistics"]),
                Chirality(item["chirality"]),
                tuple(item["index_spaces"]),
                tuple(Variance(value) for value in item["index_variances"]),
            )

        derivative_rules = []
        for rule in payload["derivative_rules"]:  # type: ignore[index]
            derivative_rules.append(
                DerivativeRule(
                    tuple(rule["lhs"]),
                    tuple(
                        DerivativeTerm(
                            qi(term["coefficient"]),
                            tuple(term["ordered_derivatives"]),
                            tuple(term["symbol_factors"]),
                            tuple(term.get("tensor_factors", ())),
                        )
                        for term in rule["rhs"]
                    ),
                    tuple(rule["conditions"]),
                )
            )
        fd = payload["fourier_dred"]
        assert isinstance(fd, dict)
        return cls(
            str(payload["schema_id"]),
            tuple(payload["index_spaces"]),  # type: ignore[arg-type]
            tuple(
                SymbolSpec(str(item["name"]), SymbolKind(item["kind"]))
                for item in payload["symbols"]  # type: ignore[index]
            ),
            tuple(
                DerivativeSpec(str(item["name"]), int(item["parity"]), str(item["index_space"]))
                for item in payload["derivatives"]  # type: ignore[index]
            ),
            tuple(derivative_rules),
            tuple(
                field_spec(item)
                for item in payload["fields"]  # type: ignore[index]
            ),
            tuple(
                PortSpec(
                    str(item["name"]),
                    str(item["field_name"]),
                    tuple(PortSector(value) for value in item["allowed_sectors"]),
                    tuple(Flow(value) for value in item["allowed_flows"]),
                )
                for item in payload["ports"]  # type: ignore[index]
            ),
            tuple(
                PropagatorSpec(
                    str(item["name"]),
                    str(item["left_port_spec"]),
                    str(item["right_port_spec"]),
                    qi(item["coefficient"]),
                    tuple(item["ordered_left_derivatives"]),
                    tuple(item["ordered_right_derivatives"]),
                    tuple(item["symbol_factors"]),
                    tuple(item.get("tensor_factors", ())),
                    bool(item["symmetric"]),
                )
                for item in payload["propagators"]  # type: ignore[index]
            ),
            tuple(
                TensorSpec(
                    str(item["name"]),
                    str(item["tensor_class"]),
                    tuple(item["index_spaces"]),
                    tuple(Variance(value) for value in item["variances"]),
                )
                for item in payload["tensors"]  # type: ignore[index]
            ),
            FourierDREDData(
                str(fd["fourier_phase"]),
                str(fd["derivative_momentum_map"]),
                str(fd["dimension"]),
                str(fd["loop_measure"]),
                str(fd["spin_metric_symbol"]),
                str(fd["loop_metric_symbol"]),
                str(fd["evanescent_metric_symbol"]),
                str(fd["epsilon_symbol"]),
                str(fd["mu_symbol"]),
            ),
            tuple(payload.get("required_tensors", ())),  # type: ignore[arg-type]
            tuple(
                AdapterAliasSpec(
                    str(item["name"]),
                    str(item["target_kind"]),
                    str(item["expression"]),
                    tuple(item["symbol_factors"]),
                    tuple(item["derivative_factors"]),
                    tuple(item["field_factors"]),
                    tuple(item["tensor_factors"]),
                    tuple(item["port_factors"]),
                    tuple(item["propagator_factors"]),
                )
                for item in payload.get("adapter_aliases", ())  # type: ignore[union-attr]
            ),
            ScalarRingSpec.from_dict(payload["scalar_ring"])
            if isinstance(payload.get("scalar_ring"), Mapping)
            else QI_SCALAR_RING,
        )

    @property
    def canonical_hash(self) -> str:
        return _sha256(self.canonical_dict())

    def assert_canonical_hash(self, expected: str) -> None:
        if self.canonical_hash != expected:
            raise HashDriftError(
                f"notation hash drift: expected {expected}, found {self.canonical_hash}"
            )

    @classmethod
    def from_dict(cls, payload: Mapping[str, object]) -> "NotationSchema":
        """Parse the complete immutable notation input from canonical JSON data."""

        required = {
            "schema_id",
            "index_spaces",
            "symbols",
            "derivatives",
            "derivative_rules",
            "fields",
            "ports",
            "propagators",
            "tensors",
            "fourier_dred",
            "required_tensors",
            "adapter_aliases",
        }
        allowed = required | {"scalar_ring"}
        if not required.issubset(payload) or not set(payload).issubset(allowed):
            missing = sorted(required - set(payload))
            extra = sorted(set(payload) - allowed)
            raise PipelineIRError(f"notation JSON shape mismatch: missing={missing}, extra={extra}")

        def records(name: str) -> tuple[Mapping[str, object], ...]:
            value = payload[name]
            if not isinstance(value, list) or any(not isinstance(item, Mapping) for item in value):
                raise PipelineIRError(f"notation field {name} must be a list of records")
            return tuple(value)

        schema_id = payload["schema_id"]
        index_spaces = payload["index_spaces"]
        fourier = payload["fourier_dred"]
        if not isinstance(schema_id, str):
            raise PipelineIRError("schema_id must be a string")
        if not isinstance(index_spaces, list) or any(not isinstance(item, str) for item in index_spaces):
            raise PipelineIRError("index_spaces must be a string list")
        if not isinstance(fourier, Mapping):
            raise PipelineIRError("fourier_dred must be a record")

        symbols = tuple(
            SymbolSpec(str(item["name"]), SymbolKind(str(item["kind"])))
            for item in records("symbols")
        )
        derivatives = tuple(
            DerivativeSpec(str(item["name"]), int(item["parity"]), str(item["index_space"]))
            for item in records("derivatives")
        )
        derivative_rules: list[DerivativeRule] = []
        for item in records("derivative_rules"):
            rhs = item.get("rhs")
            if not isinstance(rhs, list) or any(not isinstance(term, Mapping) for term in rhs):
                raise PipelineIRError("derivative-rule rhs must be a list of records")
            derivative_rules.append(
                DerivativeRule(
                    tuple(str(value) for value in item["lhs"]),
                    tuple(
                        DerivativeTerm(
                            _exact_coefficient_from_payload(term["coefficient"]),
                            tuple(str(value) for value in term["ordered_derivatives"]),
                            tuple(str(value) for value in term["symbol_factors"]),
                            tuple(str(value) for value in term.get("tensor_factors", ())),
                        )
                        for term in rhs
                    ),
                    tuple(str(value) for value in item["conditions"]),
                )
            )
        field_records = records("fields")
        required_field_keys = {
            "name",
            "statistics",
            "chirality",
            "index_spaces",
            "index_variances",
        }
        if any(set(item) != required_field_keys for item in field_records):
            raise PipelineIRError(
                "field JSON must carry explicit index_spaces and index_variances"
            )
        fields = tuple(
            FieldSpec(
                str(item["name"]),
                Statistics(str(item["statistics"])),
                Chirality(str(item["chirality"])),
                tuple(str(value) for value in item["index_spaces"]),
                tuple(Variance(str(value)) for value in item["index_variances"]),
            )
            for item in field_records
        )
        ports = tuple(
            PortSpec(
                str(item["name"]),
                str(item["field_name"]),
                tuple(PortSector(str(value)) for value in item["allowed_sectors"]),
                tuple(Flow(str(value)) for value in item["allowed_flows"]),
            )
            for item in records("ports")
        )
        propagators = tuple(
            PropagatorSpec(
                str(item["name"]),
                str(item["left_port_spec"]),
                str(item["right_port_spec"]),
                _exact_coefficient_from_payload(item["coefficient"]),
                tuple(str(value) for value in item["ordered_left_derivatives"]),
                tuple(str(value) for value in item["ordered_right_derivatives"]),
                tuple(str(value) for value in item["symbol_factors"]),
                tuple(str(value) for value in item.get("tensor_factors", ())),
                bool(item["symmetric"]),
            )
            for item in records("propagators")
        )
        tensors = tuple(
            TensorSpec(
                str(item["name"]),
                str(item["tensor_class"]),
                tuple(str(value) for value in item["index_spaces"]),
                tuple(Variance(str(value)) for value in item["variances"]),
            )
            for item in records("tensors")
        )
        fourier_keys = {
            "fourier_phase",
            "derivative_momentum_map",
            "dimension",
            "loop_measure",
            "spin_metric_symbol",
            "loop_metric_symbol",
            "evanescent_metric_symbol",
            "epsilon_symbol",
            "mu_symbol",
        }
        if set(fourier) != fourier_keys:
            raise PipelineIRError("fourier_dred JSON shape mismatch")
        fourier_dred = FourierDREDData(**{key: str(fourier[key]) for key in fourier_keys})
        required_tensors = payload["required_tensors"]
        if not isinstance(required_tensors, list) or any(
            not isinstance(item, str) for item in required_tensors
        ):
            raise PipelineIRError("required_tensors must be a string list")
        aliases = tuple(
            AdapterAliasSpec(
                str(item["name"]),
                str(item["target_kind"]),
                str(item["expression"]),
                tuple(str(value) for value in item["symbol_factors"]),
                tuple(str(value) for value in item["derivative_factors"]),
                tuple(str(value) for value in item["field_factors"]),
                tuple(str(value) for value in item["tensor_factors"]),
                tuple(str(value) for value in item["port_factors"]),
                tuple(str(value) for value in item["propagator_factors"]),
            )
            for item in records("adapter_aliases")
        )
        scalar_payload = payload.get("scalar_ring")
        if scalar_payload is None:
            scalar_ring = QI_SCALAR_RING
        elif isinstance(scalar_payload, Mapping):
            scalar_ring = ScalarRingSpec.from_dict(scalar_payload)
        else:
            raise PipelineIRError("scalar_ring must be a record")
        return cls(
            schema_id,
            tuple(index_spaces),
            symbols,
            derivatives,
            tuple(derivative_rules),
            fields,
            ports,
            propagators,
            tensors,
            fourier_dred,
            tuple(required_tensors),
            aliases,
            scalar_ring,
        )

    @classmethod
    def load_json(cls, path: str | Path) -> "NotationSchema":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(payload, Mapping):
            raise PipelineIRError("notation JSON root must be an object")
        return cls.from_dict(payload)

    def write_json(self, path: str | Path) -> None:
        Path(path).write_text(
            json.dumps(self.canonical_dict(), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


@dataclass(frozen=True, slots=True)
class LinearMomentum:
    """Normalized exact linear combination of named momenta."""

    terms: tuple[tuple[str, Fraction], ...] = ()

    def __post_init__(self) -> None:
        normalized = tuple((name, Fraction(coefficient)) for name, coefficient in self.terms)
        if any(not name or coefficient == 0 for name, coefficient in normalized):
            raise PipelineIRError("momentum terms require nonempty names and nonzero coefficients")
        if tuple(sorted(normalized)) != normalized:
            raise PipelineIRError("momentum terms must be lexically normalized")
        if len({name for name, _ in normalized}) != len(normalized):
            raise PipelineIRError("a normalized momentum cannot repeat a symbol")
        object.__setattr__(self, "terms", normalized)

    @classmethod
    def from_terms(cls, terms: Iterable[tuple[str, int | Fraction]]) -> "LinearMomentum":
        combined: dict[str, Fraction] = {}
        for name, coefficient in terms:
            combined[name] = combined.get(name, Fraction(0)) + Fraction(coefficient)
        return cls(tuple(sorted((name, value) for name, value in combined.items() if value)))

    @classmethod
    def symbol(cls, name: str, coefficient: int | Fraction = 1) -> "LinearMomentum":
        return cls.from_terms(((name, coefficient),))

    def __add__(self, other: "LinearMomentum") -> "LinearMomentum":
        return LinearMomentum.from_terms(self.terms + other.terms)

    def __neg__(self) -> "LinearMomentum":
        return LinearMomentum.from_terms((name, -coefficient) for name, coefficient in self.terms)

    def __sub__(self, other: "LinearMomentum") -> "LinearMomentum":
        return self + (-other)

    @property
    def is_zero(self) -> bool:
        return not self.terms

    def canonical_dict(self) -> list[dict[str, object]]:
        return [
            {"symbol": name, "coefficient": _fraction_payload(coefficient)}
            for name, coefficient in self.terms
        ]


@dataclass(frozen=True, slots=True)
class TypedIndex:
    index_space: str
    label: str
    variance: Variance

    def __post_init__(self) -> None:
        if not self.index_space or not self.label:
            raise PipelineIRError("typed indices require space and label")

    def canonical_dict(self) -> dict[str, str]:
        return {
            "index_space": self.index_space,
            "label": self.label,
            "variance": self.variance.value,
        }


@dataclass(frozen=True, slots=True)
class DerivativeApplication:
    application_id: str
    derivative_name: str
    target_port_id: str

    def __post_init__(self) -> None:
        if not self.application_id or not self.derivative_name or not self.target_port_id:
            raise PipelineIRError("derivative applications require complete ids")

    def canonical_dict(self) -> dict[str, str]:
        return {
            "application_id": self.application_id,
            "derivative_name": self.derivative_name,
            "target_port_id": self.target_port_id,
        }


@dataclass(frozen=True, slots=True)
class OrderedDerivativeScope:
    scope_id: str
    applications: tuple[DerivativeApplication, ...]

    def __post_init__(self) -> None:
        if not self.scope_id or not self.applications:
            raise PipelineIRError("a derivative scope must be nonempty")
        ids = [item.application_id for item in self.applications]
        if len(set(ids)) != len(ids):
            raise PipelineIRError("a derivative scope repeats an application id")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "scope_id": self.scope_id,
            "applications": [item.canonical_dict() for item in self.applications],
        }


@dataclass(frozen=True, slots=True)
class TensorOccurrence:
    occurrence_id: str
    tensor_name: str
    ordered_indices: tuple[TypedIndex, ...]

    def __post_init__(self) -> None:
        if not self.occurrence_id or not self.tensor_name:
            raise PipelineIRError("tensor occurrences require ids")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "occurrence_id": self.occurrence_id,
            "tensor_name": self.tensor_name,
            "ordered_indices": [item.canonical_dict() for item in self.ordered_indices],
        }


@dataclass(frozen=True, slots=True)
class FactorProvenance:
    factor_id: str
    role: str
    coefficient: ExactCoefficient
    expression: str
    source_ref: str
    symbol_factors: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.factor_id or not self.role or not self.expression or not self.source_ref:
            raise PipelineIRError("factor provenance must be complete")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "factor_id": self.factor_id,
            "role": self.role,
            "coefficient": self.coefficient.canonical_dict(),
            "expression": self.expression,
            "source_ref": self.source_ref,
            "symbol_factors": list(self.symbol_factors),
        }


@dataclass(frozen=True, slots=True)
class PipelinePort:
    port_id: str
    vertex_id: str
    ordinal: int
    port_spec: str
    sector: PortSector
    flow: Flow
    momentum: LinearMomentum
    indices: tuple[TypedIndex, ...]

    def __post_init__(self) -> None:
        if not self.port_id or not self.vertex_id or not self.port_spec:
            raise PipelineIRError("pipeline ports require complete ids")
        if self.ordinal < 0:
            raise PipelineIRError("port ordinal must be nonnegative")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "port_id": self.port_id,
            "vertex_id": self.vertex_id,
            "ordinal": self.ordinal,
            "port_spec": self.port_spec,
            "sector": self.sector.value,
            "flow": self.flow.value,
            "momentum": self.momentum.canonical_dict(),
            "indices": [item.canonical_dict() for item in self.indices],
        }


# A graph port is the typed half-edge incident on exactly one vertex.  The
# explicit alias keeps the port vocabulary used by Feynman-rule generation and
# the half-edge vocabulary used by graph algorithms literally identical.
PipelineHalfEdge = PipelinePort


@dataclass(frozen=True, slots=True)
class PipelineVertex:
    vertex_id: str
    kind: str
    ordered_port_ids: tuple[str, ...]
    factor_ids: tuple[str, ...]
    derivative_scopes: tuple[OrderedDerivativeScope, ...] = ()
    tensors: tuple[TensorOccurrence, ...] = ()

    def __post_init__(self) -> None:
        if not self.vertex_id or not self.kind or not self.ordered_port_ids:
            raise PipelineIRError("vertices require ids, kind, and ordered ports")
        if len(set(self.ordered_port_ids)) != len(self.ordered_port_ids):
            raise PipelineIRError("a vertex repeats a port")
        if len(set(self.factor_ids)) != len(self.factor_ids):
            raise PipelineIRError("a vertex repeats a provenance factor")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "vertex_id": self.vertex_id,
            "kind": self.kind,
            "ordered_port_ids": list(self.ordered_port_ids),
            "factor_ids": list(self.factor_ids),
            "derivative_scopes": [item.canonical_dict() for item in self.derivative_scopes],
            "tensors": [item.canonical_dict() for item in self.tensors],
        }


@dataclass(frozen=True, slots=True)
class PipelineEdge:
    edge_id: str
    left_port_id: str
    right_port_id: str
    propagator_name: str
    momentum: LinearMomentum

    def __post_init__(self) -> None:
        if not self.edge_id or not self.left_port_id or not self.right_port_id or not self.propagator_name:
            raise PipelineIRError("edges require complete ids")
        if self.left_port_id == self.right_port_id:
            raise PipelineIRError("an edge cannot use one port twice")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "edge_id": self.edge_id,
            "left_port_id": self.left_port_id,
            "right_port_id": self.right_port_id,
            "propagator_name": self.propagator_name,
            "momentum": self.momentum.canonical_dict(),
        }


@dataclass(frozen=True, slots=True)
class TopologyMetadata:
    connected: bool
    loop_number: int
    automorphism_order: int
    symmetry_factor: Fraction
    orientation: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "symmetry_factor", Fraction(self.symmetry_factor))
        if self.loop_number < 0 or self.automorphism_order < 1:
            raise PipelineIRError("loop number and automorphism order are invalid")
        if self.symmetry_factor <= 0 or not self.orientation:
            raise PipelineIRError("symmetry factor and orientation must be explicit")

    def canonical_dict(self) -> dict[str, object]:
        return {
            "connected": self.connected,
            "loop_number": self.loop_number,
            "automorphism_order": self.automorphism_order,
            "symmetry_factor": _fraction_payload(self.symmetry_factor),
            "orientation": self.orientation,
        }


@dataclass(frozen=True, slots=True)
class PipelineGraph:
    graph_id: str
    notation_hash: str
    vertices: tuple[PipelineVertex, ...]
    ports: tuple[PipelinePort, ...]
    edges: tuple[PipelineEdge, ...]
    factors: tuple[FactorProvenance, ...]
    external_order: tuple[str, ...]
    topology: TopologyMetadata

    def __post_init__(self) -> None:
        if not self.graph_id or not self.notation_hash:
            raise PipelineIRError("graph id and notation hash are mandatory")

    @property
    def half_edges(self) -> tuple[PipelinePort, ...]:
        return self.ports

    def validate(self, schema: NotationSchema) -> None:
        if self.notation_hash != schema.canonical_hash:
            raise HashDriftError(
                f"graph {self.graph_id} notation hash {self.notation_hash} != {schema.canonical_hash}"
            )
        vertices = _unique_named_by(self.vertices, "vertex_id", "vertex")
        ports = _unique_named_by(self.ports, "port_id", "port")
        edges = _unique_named_by(self.edges, "edge_id", "edge")
        factors = _unique_named_by(self.factors, "factor_id", "factor")
        del edges

        for factor in self.factors:
            if not schema.scalar_ring.admits(factor.coefficient):
                raise PipelineIRError(
                    f"factor {factor.factor_id} coefficient is outside {schema.scalar_ring.name}"
                )
            schema._require_subset(
                factor.symbol_factors,
                schema.symbol_map,
                f"factor {factor.factor_id}",
            )
        for port in self.ports:
            if port.vertex_id not in vertices:
                raise PipelineIRError(f"port {port.port_id} uses undefined vertex {port.vertex_id}")
            if port.port_spec not in schema.port_map:
                raise UndefinedSymbolError(
                    f"port {port.port_id} uses undefined port spec {port.port_spec}"
                )
            port_spec = schema.port_map[port.port_spec]
            field = schema.field_map[port_spec.field_name]
            if port.sector not in port_spec.allowed_sectors or port.flow not in port_spec.allowed_flows:
                raise PropagatorPortError(
                    f"port {port.port_id} violates sector/flow specification {port.port_spec}"
                )
            if tuple(index.index_space for index in port.indices) != field.index_spaces:
                raise PipelineIRError(f"port {port.port_id} indices do not match field {field.name}")
            if tuple(index.variance for index in port.indices) != field.index_variances:
                raise PipelineIRError(
                    f"port {port.port_id} index variances do not match field {field.name}"
                )
            schema._require_subset(
                (name for name, _ in port.momentum.terms),
                {
                    name: spec
                    for name, spec in schema.symbol_map.items()
                    if spec.kind is SymbolKind.MOMENTUM
                },
                f"port {port.port_id} momentum",
            )

        for vertex in self.vertices:
            actual_ports = sorted(
                (port for port in self.ports if port.vertex_id == vertex.vertex_id),
                key=lambda item: item.ordinal,
            )
            if tuple(port.port_id for port in actual_ports) != vertex.ordered_port_ids:
                raise PipelineIRError(
                    f"vertex {vertex.vertex_id} ordered ports do not equal ordinal port order"
                )
            if [port.ordinal for port in actual_ports] != list(range(len(actual_ports))):
                raise PipelineIRError(f"vertex {vertex.vertex_id} port ordinals are not contiguous")
            schema._require_subset(vertex.factor_ids, factors, f"vertex {vertex.vertex_id} factors")
            if not _momentum_sum(port.momentum for port in actual_ports).is_zero:
                raise MomentumConservationError(
                    f"momentum is not conserved at vertex {vertex.vertex_id}"
                )
            local_ports = set(vertex.ordered_port_ids)
            scope_ids: set[str] = set()
            for scope in vertex.derivative_scopes:
                if scope.scope_id in scope_ids:
                    raise PipelineIRError(f"vertex {vertex.vertex_id} repeats derivative scope")
                scope_ids.add(scope.scope_id)
                for application in scope.applications:
                    if application.target_port_id not in local_ports:
                        raise PipelineIRError(
                            f"derivative {application.application_id} escapes vertex {vertex.vertex_id}"
                        )
                    if application.derivative_name not in schema.derivative_map:
                        raise UndefinedSymbolError(
                            f"undefined derivative {application.derivative_name}"
                        )
            occurrence_ids: set[str] = set()
            for occurrence in vertex.tensors:
                if occurrence.occurrence_id in occurrence_ids:
                    raise PipelineIRError(f"vertex {vertex.vertex_id} repeats tensor occurrence")
                occurrence_ids.add(occurrence.occurrence_id)
                if occurrence.tensor_name not in schema.tensor_map:
                    raise UndefinedSymbolError(f"undefined tensor {occurrence.tensor_name}")
                tensor = schema.tensor_map[occurrence.tensor_name]
                if tuple(index.index_space for index in occurrence.ordered_indices) != tensor.index_spaces:
                    raise PipelineIRError(
                        f"tensor {occurrence.occurrence_id} index spaces do not match {tensor.name}"
                    )
                if tuple(index.variance for index in occurrence.ordered_indices) != tensor.variances:
                    raise PipelineIRError(
                        f"tensor {occurrence.occurrence_id} variances do not match {tensor.name}"
                    )

        used_quantum_ports: set[str] = set()
        for edge in self.edges:
            if edge.left_port_id not in ports or edge.right_port_id not in ports:
                raise PipelineIRError(f"edge {edge.edge_id} uses an undefined port")
            left = ports[edge.left_port_id]
            right = ports[edge.right_port_id]
            assert isinstance(left, PipelinePort) and isinstance(right, PipelinePort)
            if left.sector is not PortSector.QUANTUM or right.sector is not PortSector.QUANTUM:
                raise PropagatorPortError(f"edge {edge.edge_id} must join two quantum ports")
            if left.flow is not Flow.OUT or right.flow is not Flow.IN:
                raise PropagatorPortError(f"edge {edge.edge_id} must be ordered OUT to IN")
            if edge.propagator_name not in schema.propagator_map:
                raise UndefinedSymbolError(f"undefined propagator {edge.propagator_name}")
            propagator = schema.propagator_map[edge.propagator_name]
            if not propagator.accepts(left.port_spec, right.port_spec):
                raise PropagatorPortError(
                    f"propagator {edge.propagator_name} cannot connect "
                    f"{left.port_spec} to {right.port_spec}"
                )
            if edge.left_port_id in used_quantum_ports or edge.right_port_id in used_quantum_ports:
                raise PropagatorPortError("a quantum port occurs in more than one internal edge")
            used_quantum_ports.update((edge.left_port_id, edge.right_port_id))
            if left.momentum != edge.momentum or right.momentum != -edge.momentum:
                raise MomentumConservationError(
                    f"edge {edge.edge_id} endpoint momenta disagree with its routed momentum"
                )

        quantum_ports = {port.port_id for port in self.ports if port.sector is PortSector.QUANTUM}
        background_ports = {port.port_id for port in self.ports if port.sector is PortSector.BACKGROUND}
        if used_quantum_ports != quantum_ports:
            raise PropagatorPortError("every quantum port must terminate in exactly one edge")
        if len(self.external_order) != len(set(self.external_order)):
            raise PipelineIRError("external order repeats a port")
        if set(self.external_order) != background_ports:
            raise PipelineIRError("external order must contain every background port exactly once")

        adjacency = {vertex_id: set() for vertex_id in vertices}
        for edge in self.edges:
            left_vertex = ports[edge.left_port_id].vertex_id
            right_vertex = ports[edge.right_port_id].vertex_id
            adjacency[left_vertex].add(right_vertex)
            adjacency[right_vertex].add(left_vertex)
        connected = _is_connected(adjacency)
        if connected != self.topology.connected:
            raise PipelineIRError("topology connected flag disagrees with graph incidence")
        components = 1 if connected else _component_count(adjacency)
        loop_number = len(self.edges) - len(self.vertices) + components
        if loop_number != self.topology.loop_number:
            raise PipelineIRError(
                f"declared loop number {self.topology.loop_number} != incidence value {loop_number}"
            )

    def canonical_dict(self) -> dict[str, object]:
        return {
            "graph_id": self.graph_id,
            "notation_hash": self.notation_hash,
            "vertices": [item.canonical_dict() for item in sorted(self.vertices, key=lambda x: x.vertex_id)],
            "ports": [item.canonical_dict() for item in sorted(self.ports, key=lambda x: x.port_id)],
            "edges": [item.canonical_dict() for item in sorted(self.edges, key=lambda x: x.edge_id)],
            "factors": [item.canonical_dict() for item in sorted(self.factors, key=lambda x: x.factor_id)],
            "external_order": list(self.external_order),
            "topology": self.topology.canonical_dict(),
        }

    @property
    def canonical_hash(self) -> str:
        return _sha256(self.canonical_dict())


@dataclass(frozen=True, slots=True)
class AmplitudeIR:
    amplitude_id: str
    notation_hash: str
    graph_hash: str
    ordered_factor_ids: tuple[str, ...]
    factors: tuple[FactorProvenance, ...]
    exact_coefficient: ExactCoefficient
    denominator_factors: tuple[str, ...]
    external_operator: str

    def __post_init__(self) -> None:
        if not self.amplitude_id or not self.notation_hash or not self.graph_hash:
            raise PipelineIRError("amplitude ids and hashes are mandatory")
        if not self.external_operator:
            raise PipelineIRError("the external operator must be explicit")

    @classmethod
    def from_factors(
        cls,
        amplitude_id: str,
        schema: NotationSchema,
        graph: PipelineGraph,
        factors: tuple[FactorProvenance, ...],
        denominator_factors: tuple[str, ...],
        external_operator: str,
    ) -> "AmplitudeIR":
        coefficient: ExactCoefficient = QI_ONE
        for factor in factors:
            coefficient = _multiply_exact_coefficients(coefficient, factor.coefficient)
        amplitude = cls(
            amplitude_id,
            schema.canonical_hash,
            graph.canonical_hash,
            tuple(factor.factor_id for factor in factors),
            factors,
            coefficient,
            denominator_factors,
            external_operator,
        )
        amplitude.validate(schema, graph)
        return amplitude

    def validate(self, schema: NotationSchema, graph: PipelineGraph) -> None:
        if self.notation_hash != schema.canonical_hash:
            raise HashDriftError("amplitude notation hash drift")
        if self.graph_hash != graph.canonical_hash:
            raise HashDriftError("amplitude graph hash drift")
        factors = _unique_named_by(self.factors, "factor_id", "amplitude factor")
        if tuple(factors) != self.ordered_factor_ids:
            raise PipelineIRError("ordered amplitude factors must list each factor exactly once")
        coefficient: ExactCoefficient = QI_ONE
        for factor_id in self.ordered_factor_ids:
            factor = factors[factor_id]
            assert isinstance(factor, FactorProvenance)
            if not schema.scalar_ring.admits(factor.coefficient):
                raise PipelineIRError(
                    f"amplitude factor {factor.factor_id} is outside {schema.scalar_ring.name}"
                )
            schema._require_subset(
                factor.symbol_factors,
                schema.symbol_map,
                f"amplitude factor {factor.factor_id}",
            )
            coefficient = _multiply_exact_coefficients(coefficient, factor.coefficient)
        if coefficient != self.exact_coefficient:
            raise PipelineIRError("amplitude exact coefficient disagrees with factor provenance")
        schema._require_subset(
            self.denominator_factors,
            schema.symbol_map,
            f"amplitude {self.amplitude_id} denominator",
        )

    def canonical_dict(self) -> dict[str, object]:
        return {
            "amplitude_id": self.amplitude_id,
            "notation_hash": self.notation_hash,
            "graph_hash": self.graph_hash,
            "ordered_factor_ids": list(self.ordered_factor_ids),
            "factors": [item.canonical_dict() for item in self.factors],
            "exact_coefficient": self.exact_coefficient.canonical_dict(),
            "denominator_factors": list(self.denominator_factors),
            "external_operator": self.external_operator,
        }

    @property
    def canonical_hash(self) -> str:
        return _sha256(self.canonical_dict())


def _unique_named_by(items: Iterable[object], attribute: str, label: str) -> dict[str, object]:
    result: dict[str, object] = {}
    for item in items:
        name = getattr(item, attribute)
        if name in result:
            raise PipelineIRError(f"duplicate {label} id: {name}")
        result[name] = item
    return result


def _momentum_sum(momenta: Iterable[LinearMomentum]) -> LinearMomentum:
    result = LinearMomentum()
    for momentum in momenta:
        result = result + momentum
    return result


def _is_connected(adjacency: Mapping[str, set[str]]) -> bool:
    if not adjacency:
        return False
    root = next(iter(adjacency))
    visited: set[str] = set()
    stack = [root]
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        stack.extend(adjacency[current] - visited)
    return len(visited) == len(adjacency)


def _component_count(adjacency: Mapping[str, set[str]]) -> int:
    remaining = set(adjacency)
    count = 0
    while remaining:
        count += 1
        stack = [next(iter(remaining))]
        while stack:
            current = stack.pop()
            if current not in remaining:
                continue
            remaining.remove(current)
            stack.extend(adjacency[current] & remaining)
    return count


# Updated only when the canonical Project WW notation payload changes by an
# intentional reviewed edit.  The factory checks this value before returning.
PROJECT_WW_NOTATION_SCHEMA_SHA256 = (
    "fcdd284541dcdcf6d0217432ab146b908ad8aadf2a90e6f9201f87b149250025"
)


def project_notation_schema() -> NotationSchema:
    """Frozen dependency closure of ``ww_seed_request`` notation.

    The factory contains types and algebra only.  It contains neither a graph
    multiplicity nor a loop integral nor an anomaly coefficient.
    """

    color = "COLOR_ADJOINT"
    undotted = "UNDOTTED"
    dotted = "DOTTED"
    scalar = "SCALAR"
    schema = NotationSchema(
        schema_id="STEP5_EUCLIDEAN_N4_WW_REQUEST_NOTATION_V1",
        index_spaces=(color, undotted, dotted, scalar),
        symbols=(
            SymbolSpec("h", SymbolKind.NORMALIZATION),
            SymbolSpec("g2", SymbolKind.COUPLING),
            SymbolSpec("k", SymbolKind.MOMENTUM),
            SymbolSpec("p", SymbolKind.MOMENTUM),
            SymbolSpec("q", SymbolKind.MOMENTUM),
            SymbolSpec("pi", SymbolKind.OTHER),
            SymbolSpec("epsilon", SymbolKind.REGULATOR),
            SymbolSpec("mu", SymbolKind.SCALE),
            SymbolSpec("g4", SymbolKind.METRIC),
            SymbolSpec("ghat", SymbolKind.METRIC),
        ),
        derivatives=(
            DerivativeSpec("D_+", 1, undotted),
            DerivativeSpec("D_-", 1, undotted),
            DerivativeSpec("D_a", 1, undotted),
            DerivativeSpec("barD_dot_alpha", 1, dotted),
            DerivativeSpec("D2", 0, scalar),
            DerivativeSpec("barD2", 0, scalar),
            DerivativeSpec("K_+", 0, scalar),
            DerivativeSpec("nabla_+", 1, undotted),
            DerivativeSpec("nabla_-", 1, undotted),
        ),
        derivative_rules=(
            DerivativeRule(
                ("K_+",),
                (
                    DerivativeTerm(
                        Qi.rational(-1, 8),
                        ("D_+", "barD2", "D_+"),
                    ),
                ),
                ("K_+=-(1/8)D_+barD2D_+",),
            ),
            DerivativeRule(
                ("D_-", "D_+"),
                (DerivativeTerm(Qi.rational(1, 2), ("D2",)),),
                ("Project plus/minus spin frame",),
            ),
            DerivativeRule(
                ("D_-", "K_+"),
                (
                    DerivativeTerm(
                        Qi.rational(-1, 16),
                        ("D2", "barD2", "D_+"),
                    ),
                ),
                ("linear WW insertion",),
            ),
            DerivativeRule(
                ("D_a", "barD_dot_alpha"),
                (
                    DerivativeTerm(
                        Qi.rational(-1),
                        ("barD_dot_alpha", "D_a"),
                    ),
                    DerivativeTerm(Qi.imaginary(-2), symbol_factors=("p",)),
                ),
                (
                    "{D_a,barD_dot_alpha}=-2 partial_(a dot_alpha)",
                    "Fourier partial_(a dot_alpha)=+i p_(a dot_alpha)",
                ),
            ),
            DerivativeRule(
                ("D2", "barD2"),
                (
                    DerivativeTerm(
                        Qi.rational(16),
                        tensor_factors=("delta4theta",),
                    ),
                ),
                ("acts on normalized Grassmann delta and is then evaluated at zero",),
            ),
            DerivativeRule(
                ("nabla_-", "K_+"),
                (DerivativeTerm(QI_ONE, ("D_-", "K_+")),),
                ("reference-flat linear quantum prepotential",),
            ),
        ),
        fields=(
            FieldSpec(
                "V", Statistics.BOSON, Chirality.REAL, (color,), (Variance.UP,)
            ),
            FieldSpec(
                "W_plus",
                Statistics.FERMION,
                Chirality.CHIRAL,
                (color, undotted),
                (Variance.UP, Variance.DOWN),
            ),
            FieldSpec(
                "TildeW_dot_alpha",
                Statistics.FERMION,
                Chirality.ANTICHIRAL,
                (color, dotted),
                (Variance.UP, Variance.DOWN),
            ),
            FieldSpec(
                "Source[nabla_-(X^A X^B)]",
                Statistics.FERMION,
                Chirality.UNCONSTRAINED,
                (color, color),
                (Variance.DOWN, Variance.DOWN),
            ),
        ),
        ports=(
            PortSpec("V_Q", "V", (PortSector.QUANTUM,), (Flow.IN, Flow.OUT)),
            PortSpec("W_plus_B", "W_plus", (PortSector.BACKGROUND,), (Flow.IN,)),
            PortSpec(
                "TildeW_B",
                "TildeW_dot_alpha",
                (PortSector.BACKGROUND,),
                (Flow.IN,),
            ),
            PortSpec(
                "WW_source_B",
                "Source[nabla_-(X^A X^B)]",
                (PortSector.BACKGROUND,),
                (Flow.IN,),
            ),
        ),
        propagators=(
            PropagatorSpec(
                "P_VV",
                "V_Q",
                "V_Q",
                Qi.rational(-2),
                symbol_factors=("g2",),
                tensor_factors=("kappa", "delta4theta"),
                symmetric=True,
            ),
        ),
        tensors=(
            TensorSpec(
                "kappa",
                "INVERSE_COLOR_METRIC_IN_P_VV",
                (color, color),
                (Variance.UP, Variance.UP),
            ),
            TensorSpec(
                "c",
                "COLOR_STRUCTURE_CONSTANT",
                (color, color, color),
                (Variance.DOWN, Variance.DOWN, Variance.DOWN),
            ),
            TensorSpec("delta4theta", "GRASSMANN_DELTA", (), ()),
        ),
        fourier_dred=FourierDREDData(
            "exp(+i p.x)",
            "partial_mu -> +i p_mu",
            "d=4-2 epsilon",
            "mu^(2 epsilon) d^d k/(2 pi)^d",
            "g4",
            "ghat",
            "gtilde",
            "epsilon",
            "mu",
        ),
        required_tensors=("kappa", "c", "delta4theta"),
        adapter_aliases=(
            AdapterAliasSpec(
                "gtilde",
                "METRIC_EXPRESSION",
                "g4-ghat",
                symbol_factors=("g4", "ghat"),
            ),
            AdapterAliasSpec(
                "X",
                "FIELD_EXPRESSION",
                "nabla_+ W_plus",
                derivative_factors=("nabla_+",),
                field_factors=("W_plus",),
            ),
            AdapterAliasSpec("r0", "MOMENTUM_EXPRESSION", "k", symbol_factors=("k",)),
            AdapterAliasSpec(
                "r1",
                "MOMENTUM_EXPRESSION",
                "k+q",
                symbol_factors=("k", "q"),
            ),
            AdapterAliasSpec(
                "r2",
                "MOMENTUM_EXPRESSION",
                "k+p+q",
                symbol_factors=("k", "p", "q"),
            ),
            AdapterAliasSpec(
                "P_VV(r)",
                "PROPAGATOR_EXPRESSION",
                "-2*g2*kappa*delta4theta/r^2",
                symbol_factors=("g2",),
                tensor_factors=("kappa", "delta4theta"),
                port_factors=("V_Q",),
                propagator_factors=("P_VV",),
            ),
        ),
        scalar_ring=PROJECT_N4_SCALAR_RING,
    )
    if PROJECT_WW_NOTATION_SCHEMA_SHA256 != "PENDING":
        schema.assert_canonical_hash(PROJECT_WW_NOTATION_SCHEMA_SHA256)
    return schema


__all__ = [
    "AdapterAliasSpec",
    "AmplitudeIR",
    "Chirality",
    "DerivativeApplication",
    "DerivativeRule",
    "DerivativeSpec",
    "DerivativeTerm",
    "EXACT_I",
    "EXACT_I_SQRT2",
    "EXACT_ONE",
    "EXACT_SQRT2",
    "EXACT_ZERO",
    "ExactCoefficient",
    "ExactScalar",
    "FactorProvenance",
    "FieldSpec",
    "Flow",
    "FourierDREDData",
    "HashDriftError",
    "LinearMomentum",
    "MomentumConservationError",
    "NotationSchema",
    "OrderedDerivativeScope",
    "PipelineEdge",
    "PipelineGraph",
    "PipelineHalfEdge",
    "PipelineIRError",
    "PipelinePort",
    "PipelineVertex",
    "PortSector",
    "PortSpec",
    "PropagatorPortError",
    "PropagatorSpec",
    "PROJECT_WW_NOTATION_SCHEMA_SHA256",
    "PROJECT_N4_SCALAR_RING",
    "QI_ONE",
    "QI_ZERO",
    "Qi",
    "QI_SCALAR_RING",
    "ScalarRingSpec",
    "Statistics",
    "SymbolKind",
    "SymbolSpec",
    "TensorOccurrence",
    "TensorSpec",
    "TopologyMetadata",
    "TypedIndex",
    "UndefinedSymbolError",
    "Variance",
    "project_notation_schema",
]
