#!/usr/bin/env python3
"""Typed Step-6 DRED tensor-numerator reducer.

The reducer implements only the metric contract already fixed in Step 5:

* spin/D-algebra emits ``delta_(4)``;
* centered loop-tensor averaging emits ``hat_delta``;
* ``tilde_delta`` can be constructed only by a validated sum of one
  independently derived ``+C hat_delta`` term and one independently derived
  ``-C delta_(4)`` contact term.

There are no master integrals, UV poles, graph coefficients, or imported
comparison data in this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
GENERATED_DIR = ROOT / "generated/step6/dred-reducer"
GENERATED_JSON = GENERATED_DIR / "dred-reducer.json"
GENERATED_MD = GENERATED_DIR / "dred-reducer.md"
AUDIT = ROOT / "audits/step6-dred-reducer-verification.json"

SCHEMA_VERSION = "step6.dred_reducer.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
STAGE = "TYPED_DRED_NUMERATOR_REDUCTION_NO_INTEGRATION"


class DREDReducerError(ValueError):
    """Base fail-closed reducer error."""


class TypeSpaceError(DREDReducerError):
    """Raised when indices or momenta from incompatible spaces are mixed."""


class MetricProvenanceError(DREDReducerError):
    """Raised when a metric is emitted at an illegal derivation stage."""


class BareNumeratorError(DREDReducerError):
    """Raised for a malformed or regulator-contaminated bare numerator."""


class TensorAverageError(DREDReducerError):
    """Raised when rank-two or rank-four averaging is not type safe."""


class ContactSubtractionError(DREDReducerError):
    """Raised when the two independent terms do not prove the DRED difference."""


class IndexSpace(str, Enum):
    VECTOR_4 = "VECTOR_4"
    SPINOR_UNDOTTED = "SPINOR_UNDOTTED"
    SPINOR_DOTTED = "SPINOR_DOTTED"


class Variance(str, Enum):
    UPPER = "UPPER"
    LOWER = "LOWER"


class MomentumRole(str, Enum):
    CENTERED_LOOP = "CENTERED_LOOP"
    ROUTED_LOOP = "ROUTED_LOOP"
    ROUTED_EXTERNAL = "ROUTED_EXTERNAL"


class MomentumSupport(str, Enum):
    REGULATED_HAT = "REGULATED_HAT"
    FOUR_SPIN = "FOUR_SPIN"


class MetricKind(str, Enum):
    DELTA4 = "delta_(4)"
    HAT = "hat_delta"
    TILDE = "tilde_delta"


class MetricStage(str, Enum):
    SPIN_DALGEBRA = "SPIN_DALGEBRA"
    LOOP_TENSOR_AVERAGING = "LOOP_TENSOR_AVERAGING"
    CONTACT_DALGEBRA = "CONTACT_DALGEBRA"
    POST_CONTACT_SUBTRACTION = "POST_CONTACT_SUBTRACTION"
    METRIC_IDENTITY_AUDIT = "METRIC_IDENTITY_AUDIT"


class ScalarAtomKind(str, Enum):
    PHYSICAL = "PHYSICAL"
    DRED_DIMENSION = "DRED_DIMENSION"
    DRED_REGULATOR = "DRED_REGULATOR"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _enum_value(value: Enum | str) -> str:
    return value.value if isinstance(value, Enum) else str(value)


_UNTYPED_DRED_SCALARS = {
    "d",
    "epsilon",
    "eps",
    "epsilon_dred",
    "eps_dred",
    "4-2epsilon",
    "4-2eps",
    "4-2epsilon_dred",
    "4-2eps_dred",
}


def _normalized_scalar_token(value: str) -> str:
    return "".join(value.lower().split()).replace("*", "")


def _contains_untyped_dred_scalar(value: Any) -> bool:
    if isinstance(value, str):
        return _normalized_scalar_token(value) in _UNTYPED_DRED_SCALARS
    if isinstance(value, Mapping):
        return any(
            _contains_untyped_dred_scalar(key)
            or _contains_untyped_dred_scalar(item)
            for key, item in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_untyped_dred_scalar(item) for item in value)
    return False


@dataclass(frozen=True)
class TensorIndex:
    name: str
    space: IndexSpace
    variance: Variance

    def __post_init__(self) -> None:
        if not self.name or not self.name.replace("_", "").isalnum():
            raise TypeSpaceError("index name must be a nonempty alphanumeric token")

    def as_json(self) -> dict[str, str]:
        return {
            "name": self.name,
            "space": self.space.value,
            "variance": self.variance.value,
        }


@dataclass(frozen=True)
class ScalarAtom:
    name: str
    kind: ScalarAtomKind = ScalarAtomKind.PHYSICAL

    def __post_init__(self) -> None:
        if not self.name:
            raise BareNumeratorError("scalar atom name is empty")
        normalized = _normalized_scalar_token(self.name)
        if self.kind is ScalarAtomKind.PHYSICAL and normalized in _UNTYPED_DRED_SCALARS:
            raise BareNumeratorError(
                "DRED dimension/regulator scalar must carry an explicit DRED atom type"
            )
        if self.kind is ScalarAtomKind.DRED_DIMENSION and normalized != "d":
            raise BareNumeratorError("DRED dimension atom must be named d")
        if self.kind is ScalarAtomKind.DRED_REGULATOR and normalized not in {
            "epsilon_dred",
            "eps_dred",
        }:
            raise BareNumeratorError("DRED regulator atom must be named epsilon_DRED")

    def as_json(self) -> dict[str, str]:
        return {"name": self.name, "kind": self.kind.value}


@dataclass(frozen=True)
class ExactCoefficient:
    sign: int = 1
    rational: Fraction = Fraction(1, 1)
    atoms: tuple[ScalarAtom, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", Fraction(self.rational))
        if self.sign not in {-1, 1}:
            raise BareNumeratorError("exact coefficient sign must be +1 or -1")
        if self.rational <= 0:
            raise BareNumeratorError("exact coefficient rational magnitude must be positive")

    def validate_bare(self) -> None:
        illegal = [atom for atom in self.atoms if atom.kind is not ScalarAtomKind.PHYSICAL]
        if illegal:
            raise BareNumeratorError(
                "bare numerator contains a DRED dimension or regulator scalar"
            )

    def magnitude_key(self) -> tuple[int, int, tuple[tuple[str, str], ...]]:
        return (
            self.rational.numerator,
            self.rational.denominator,
            tuple(sorted((atom.name, atom.kind.value) for atom in self.atoms)),
        )

    def negated(self) -> "ExactCoefficient":
        return ExactCoefficient(-self.sign, self.rational, self.atoms)

    def as_json(self) -> dict[str, Any]:
        return {
            "sign": self.sign,
            "rational": {
                "numerator": self.rational.numerator,
                "denominator": self.rational.denominator,
            },
            "atoms": [atom.as_json() for atom in self.atoms],
        }


@dataclass(frozen=True)
class ExternalOperatorTensor:
    operator_id: str
    ordered_indices: tuple[TensorIndex, ...]
    tensor_ast: Mapping[str, Any]
    derivation_provenance: str

    def __post_init__(self) -> None:
        if not self.operator_id or not self.derivation_provenance:
            raise TypeSpaceError("external tensor requires id and derivation provenance")
        labels = [(index.name, index.space.value) for index in self.ordered_indices]
        if len(labels) != len(set(labels)):
            raise TypeSpaceError("external tensor free indices must be unique")
        canonical_json(self.tensor_ast)
        if _contains_untyped_dred_scalar(self.tensor_ast):
            raise BareNumeratorError(
                "external tensor AST contains an untyped DRED scalar token"
            )

    @property
    def identity_sha256(self) -> str:
        return digest(self.as_json(include_hash=False))

    def as_json(self, *, include_hash: bool = True) -> dict[str, Any]:
        row = {
            "operator_id": self.operator_id,
            "ordered_indices": [index.as_json() for index in self.ordered_indices],
            "tensor_ast": dict(self.tensor_ast),
            "derivation_provenance": self.derivation_provenance,
        }
        if include_hash:
            row["identity_sha256"] = self.identity_sha256
        return row


@dataclass(frozen=True)
class MomentumVector:
    name: str
    role: MomentumRole
    support: MomentumSupport = MomentumSupport.REGULATED_HAT

    def __post_init__(self) -> None:
        if not self.name:
            raise TypeSpaceError("momentum name is empty")
        if self.support is not MomentumSupport.REGULATED_HAT:
            raise TypeSpaceError("every routed or centered momentum must lie in hat space")

    def as_json(self) -> dict[str, str]:
        return {
            "name": self.name,
            "role": self.role.value,
            "support": self.support.value,
        }


@dataclass(frozen=True)
class MomentumFactor:
    momentum: MomentumVector
    index: TensorIndex

    def __post_init__(self) -> None:
        if self.index.space is not IndexSpace.VECTOR_4:
            raise TypeSpaceError("momentum factor requires a four-vector index")
        if self.index.variance is not Variance.UPPER:
            raise TypeSpaceError("centered tensor averaging accepts contravariant momenta")

    def as_json(self) -> dict[str, Any]:
        return {"momentum": self.momentum.as_json(), "index": self.index.as_json()}


@dataclass(frozen=True)
class MetricTensor:
    kind: MetricKind
    indices: tuple[TensorIndex, TensorIndex]
    stage: MetricStage
    source_id: str
    construction: str
    proof_sha256: str | None = None

    def __post_init__(self) -> None:
        if len(self.indices) != 2:
            raise TypeSpaceError("metric must have exactly two indices")
        if any(index.space is not IndexSpace.VECTOR_4 for index in self.indices):
            raise TypeSpaceError("four-vector metric cannot carry a spinor index")
        if self.indices[0].name == self.indices[1].name and (
            self.indices[0].variance is self.indices[1].variance
        ):
            raise TypeSpaceError("two equally varied free metric indices must be distinct")
        if not self.source_id or not self.construction:
            raise MetricProvenanceError("metric provenance is incomplete")

        if self.stage is MetricStage.METRIC_IDENTITY_AUDIT:
            return
        allowed = {
            MetricKind.DELTA4: {
                MetricStage.SPIN_DALGEBRA,
                MetricStage.CONTACT_DALGEBRA,
            },
            MetricKind.HAT: {MetricStage.LOOP_TENSOR_AVERAGING},
            MetricKind.TILDE: {MetricStage.POST_CONTACT_SUBTRACTION},
        }
        if self.stage not in allowed[self.kind]:
            raise MetricProvenanceError(
                f"{self.kind.value} cannot be emitted at {self.stage.value}"
            )
        if self.kind is MetricKind.TILDE:
            if self.construction != "VALIDATED_INDEPENDENT_CONTACT_SUBTRACTION":
                raise MetricProvenanceError(
                    "tilde_delta requires a validated independent contact subtraction"
                )
            if not self.proof_sha256:
                raise MetricProvenanceError("tilde_delta requires a subtraction proof hash")

    def as_json(self) -> dict[str, Any]:
        return {
            "kind": self.kind.value,
            "indices": [index.as_json() for index in self.indices],
            "stage": self.stage.value,
            "source_id": self.source_id,
            "construction": self.construction,
            "proof_sha256": self.proof_sha256,
        }


@dataclass(frozen=True)
class BareTensorNumerator:
    numerator_id: str
    external_tensor: ExternalOperatorTensor
    momentum_factors: tuple[MomentumFactor, ...]
    coefficient: ExactCoefficient
    radial_scalar_moment: ScalarAtom
    spin_dalgebra_metrics: tuple[MetricTensor, ...]
    source_graph_id: str
    stage: str = "BARE_DALGEBRA_NUMERATOR"

    def __post_init__(self) -> None:
        if self.stage != "BARE_DALGEBRA_NUMERATOR":
            raise BareNumeratorError("bare numerator stage changed")
        if not self.numerator_id or not self.source_graph_id:
            raise BareNumeratorError("bare numerator provenance is incomplete")
        if len(self.momentum_factors) not in {2, 4}:
            raise BareNumeratorError("only rank-two and rank-four tensors are accepted")
        labels = [factor.index.name for factor in self.momentum_factors]
        if len(labels) != len(set(labels)):
            raise BareNumeratorError("loop-tensor free indices must be distinct")
        self.coefficient.validate_bare()
        if self.radial_scalar_moment.kind is not ScalarAtomKind.PHYSICAL:
            raise BareNumeratorError("bare radial scalar cannot contain d or epsilon")
        for metric in self.spin_dalgebra_metrics:
            if (
                metric.kind is not MetricKind.DELTA4
                or metric.stage is not MetricStage.SPIN_DALGEBRA
            ):
                raise MetricProvenanceError(
                    "bare spin/D-algebra metric must be delta_(4)"
                )

    @property
    def rank(self) -> int:
        return len(self.momentum_factors)

    def as_json(self) -> dict[str, Any]:
        return {
            "schema": "step6.typed_bare_dred_numerator.v1",
            "stage": self.stage,
            "numerator_id": self.numerator_id,
            "source_graph_id": self.source_graph_id,
            "rank": self.rank,
            "coefficient": self.coefficient.as_json(),
            "external_operator_tensor": self.external_tensor.as_json(),
            "momentum_factors": [factor.as_json() for factor in self.momentum_factors],
            "radial_scalar_moment": self.radial_scalar_moment.as_json(),
            "spin_dalgebra_metrics": [metric.as_json() for metric in self.spin_dalgebra_metrics],
            "regulator_scalar_in_bare_numerator": False,
        }


@dataclass(frozen=True)
class Rank4Contractions:
    X: ScalarAtom
    Y: ScalarAtom
    Z: ScalarAtom

    def __post_init__(self) -> None:
        for atom in (self.X, self.Y, self.Z):
            if atom.kind is not ScalarAtomKind.PHYSICAL:
                raise TensorAverageError("rank-four contraction moments must be physical")

    def as_json(self) -> dict[str, Any]:
        return {"X": self.X.as_json(), "Y": self.Y.as_json(), "Z": self.Z.as_json()}


def _dimension_rational(
    numerator_terms: Sequence[tuple[str, ScalarAtom]], denominator: Sequence[str]
) -> dict[str, Any]:
    allowed_factors = {"1", "-1", "d+1"}
    allowed_denominators = {"d", "d-1", "d+2"}
    if any(factor not in allowed_factors for factor, _ in numerator_terms):
        raise TensorAverageError("unsupported dimension-polynomial numerator")
    if any(factor not in allowed_denominators for factor in denominator):
        raise TensorAverageError("unsupported dimension-polynomial denominator")
    return {
        "kind": "EXACT_RATIONAL_FUNCTION_OF_D_AFTER_TENSOR_AVERAGING",
        "numerator_terms": [
            {"dimension_factor": factor, "scalar_moment": atom.as_json()}
            for factor, atom in numerator_terms
        ],
        "denominator_factors": list(denominator),
        "d_definition": "tr(hat_delta)",
        "epsilon_expansion_performed": False,
    }


def rank2_coefficient_exact(d: Fraction) -> Fraction:
    """Exact numerical oracle for the typed symbolic factor ``1/d``."""
    d = Fraction(d)
    if d == 0:
        raise TensorAverageError("rank-two averaging is undefined at d=0")
    return Fraction(1, 1) / d


def rank4_coefficients_exact(
    d: Fraction,
    X: Fraction,
    Y: Fraction,
    Z: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Exact numerical oracle for the three rank-four contraction channels."""
    d, X, Y, Z = map(Fraction, (d, X, Y, Z))
    denominator = d * (d - 1) * (d + 2)
    if denominator == 0:
        raise TensorAverageError("rank-four averaging requires d not in {0,1,-2}")
    return (
        ((d + 1) * X - Y - Z) / denominator,
        (-X + (d + 1) * Y - Z) / denominator,
        (-X - Y + (d + 1) * Z) / denominator,
    )


def _hat_metric(indices: tuple[TensorIndex, TensorIndex], source_id: str) -> MetricTensor:
    return MetricTensor(
        MetricKind.HAT,
        indices,
        MetricStage.LOOP_TENSOR_AVERAGING,
        source_id,
        "CENTERED_HAT_SPACE_ISOTROPIC_AVERAGE",
    )


def _base_average(numerator: BareTensorNumerator, expected_rank: int) -> dict[str, Any]:
    if numerator.rank != expected_rank:
        raise TensorAverageError(
            f"rank-{expected_rank} reducer received rank-{numerator.rank} input"
        )
    if any(
        factor.momentum.role is not MomentumRole.CENTERED_LOOP
        for factor in numerator.momentum_factors
    ):
        raise TensorAverageError("tensor averaging requires centered loop momenta")
    return {
        "schema": "step6.typed_dred_tensor_average.v1",
        "stage": MetricStage.LOOP_TENSOR_AVERAGING.value,
        "source_numerator_id": numerator.numerator_id,
        "source_graph_id": numerator.source_graph_id,
        "source_bare_numerator_sha256": digest(numerator.as_json()),
        "external_operator_tensor": numerator.external_tensor.as_json(),
        "external_operator_tensor_preserved_sha256": numerator.external_tensor.identity_sha256,
        "bare_exact_coefficient": numerator.coefficient.as_json(),
        "spectator_spin_dalgebra_metrics": [
            metric.as_json() for metric in numerator.spin_dalgebra_metrics
        ],
        "loop_metric": MetricKind.HAT.value,
        "spin_metric_replacement_performed": False,
        "epsilon_inserted_into_bare_numerator": False,
    }


def rank2_average(numerator: BareTensorNumerator) -> dict[str, Any]:
    """Reduce a centered rank-two loop tensor in the regulated hat subspace."""
    row = _base_average(numerator, 2)
    left, right = (factor.index for factor in numerator.momentum_factors)
    metric = _hat_metric((left, right), numerator.numerator_id + ":rank2")
    row.update(
        {
            "rank": 2,
            "formula": "I[q_i^m q_j^n F]=hat_delta^(mn)/d I[(q_i.q_j)F]",
            "terms": [
                {
                    "metric_product": [metric.as_json()],
                    "coefficient": _dimension_rational(
                        [("1", numerator.radial_scalar_moment)], ["d"]
                    ),
                }
            ],
        }
    )
    row["output_sha256"] = digest(row)
    return row


def rank4_average(
    numerator: BareTensorNumerator,
    contractions: Rank4Contractions,
) -> dict[str, Any]:
    """Reduce a general centered rank-four tensor from its three contractions."""
    row = _base_average(numerator, 4)
    m, n, r, s = (factor.index for factor in numerator.momentum_factors)
    pairings = (
        ((m, n), (r, s), (("d+1", contractions.X), ("-1", contractions.Y), ("-1", contractions.Z)), "A"),
        ((m, r), (n, s), (("-1", contractions.X), ("d+1", contractions.Y), ("-1", contractions.Z)), "B"),
        ((m, s), (n, r), (("-1", contractions.X), ("-1", contractions.Y), ("d+1", contractions.Z)), "C"),
    )
    terms = []
    for first, second, numerator_terms, channel in pairings:
        terms.append(
            {
                "channel": channel,
                "metric_product": [
                    _hat_metric(first, numerator.numerator_id + f":rank4:{channel}:1").as_json(),
                    _hat_metric(second, numerator.numerator_id + f":rank4:{channel}:2").as_json(),
                ],
                "coefficient": _dimension_rational(
                    numerator_terms, ["d", "d-1", "d+2"]
                ),
            }
        )
    row.update(
        {
            "rank": 4,
            "formula": (
                "T^(mnrs)=A hat_delta^(mn)hat_delta^(rs)+"
                "B hat_delta^(mr)hat_delta^(ns)+"
                "C hat_delta^(ms)hat_delta^(nr)"
            ),
            "contractions": contractions.as_json(),
            "terms": terms,
            "linear_system": [
                "X=d^2 A+d B+d C",
                "Y=d A+d^2 B+d C",
                "Z=d A+d B+d^2 C",
            ],
        }
    )
    row["output_sha256"] = digest(row)
    return row


def rank4_identical_average(numerator: BareTensorNumerator) -> dict[str, Any]:
    """Specialize rank four to q^m q^n q^r q^s without expanding d."""
    if numerator.rank != 4:
        raise TensorAverageError("identical-vector specialization requires rank four")
    names = {factor.momentum.name for factor in numerator.momentum_factors}
    if len(names) != 1:
        raise TensorAverageError("identical-vector specialization received distinct momenta")
    row = _base_average(numerator, 4)
    m, n, r, s = (factor.index for factor in numerator.momentum_factors)
    pairings = (((m, n), (r, s)), ((m, r), (n, s)), ((m, s), (n, r)))
    terms = []
    for channel, (first, second) in zip(("A", "B", "C"), pairings, strict=True):
        terms.append(
            {
                "channel": channel,
                "metric_product": [
                    _hat_metric(first, numerator.numerator_id + f":rank4-identical:{channel}:1").as_json(),
                    _hat_metric(second, numerator.numerator_id + f":rank4-identical:{channel}:2").as_json(),
                ],
                "coefficient": {
                    "kind": "EXACT_RATIONAL_FUNCTION_OF_D_AFTER_TENSOR_AVERAGING",
                    "numerator_terms": [
                        {
                            "dimension_factor": "1",
                            "scalar_moment": numerator.radial_scalar_moment.as_json(),
                        }
                    ],
                    "denominator_factors": ["d", "d+2"],
                    "d_definition": "tr(hat_delta)",
                    "epsilon_expansion_performed": False,
                },
            }
        )
    row.update(
        {
            "rank": 4,
            "specialization": "ONE_IDENTICAL_CENTERED_LOOP_VECTOR",
            "formula": (
                "I[q^m q^n q^r q^s F]=(hat_delta^(mn)hat_delta^(rs)+"
                "hat_delta^(mr)hat_delta^(ns)+hat_delta^(ms)hat_delta^(nr))"
                "/(d(d+2)) I[(q^2)^2F]"
            ),
            "terms": terms,
        }
    )
    row["output_sha256"] = digest(row)
    return row


@dataclass(frozen=True)
class IndependentMetricTerm:
    term_id: str
    source_graph_id: str
    derivation_sha256: str
    coefficient: ExactCoefficient
    metric: MetricTensor
    external_tensor: ExternalOperatorTensor
    contact_census_status: str | None = None

    def __post_init__(self) -> None:
        if not self.term_id or not self.source_graph_id or not self.derivation_sha256:
            raise ContactSubtractionError("metric term derivation provenance is incomplete")

    def as_json(self) -> dict[str, Any]:
        return {
            "term_id": self.term_id,
            "source_graph_id": self.source_graph_id,
            "derivation_sha256": self.derivation_sha256,
            "coefficient": self.coefficient.as_json(),
            "metric": self.metric.as_json(),
            "external_operator_tensor": self.external_tensor.as_json(),
            "contact_census_status": self.contact_census_status,
        }


def validated_contact_subtraction(
    triangle: IndependentMetricTerm,
    contact: IndependentMetricTerm,
) -> dict[str, Any]:
    """Form ``-C tilde_delta`` only after all independent-term checks pass."""
    if triangle.metric.kind is not MetricKind.HAT or (
        triangle.metric.stage is not MetricStage.LOOP_TENSOR_AVERAGING
    ):
        raise ContactSubtractionError("triangle term must carry averaged hat_delta")
    if contact.metric.kind is not MetricKind.DELTA4 or (
        contact.metric.stage is not MetricStage.CONTACT_DALGEBRA
    ):
        raise ContactSubtractionError("contact term must carry D-algebra delta_(4)")
    if triangle.coefficient.sign != 1 or contact.coefficient.sign != -1:
        raise ContactSubtractionError("required signs are +C for triangle and -C for contact")
    if triangle.coefficient.magnitude_key() != contact.coefficient.magnitude_key():
        raise ContactSubtractionError("triangle and contact coefficient magnitudes differ")
    if triangle.source_graph_id == contact.source_graph_id or (
        triangle.derivation_sha256 == contact.derivation_sha256
    ):
        raise ContactSubtractionError("triangle and contact must be independently derived")
    if contact.contact_census_status != "SD_COMPLETE_CONTACT_FAMILY":
        raise ContactSubtractionError("complete SD contact-family certificate is absent")
    if triangle.external_tensor.identity_sha256 != contact.external_tensor.identity_sha256:
        raise ContactSubtractionError("external operator tensor changed across subtraction")
    if triangle.metric.indices != contact.metric.indices:
        raise ContactSubtractionError("metric indices or variance changed across subtraction")

    proof_record = {
        "triangle_term_sha256": digest(triangle.as_json()),
        "contact_term_sha256": digest(contact.as_json()),
        "same_coefficient_magnitude": True,
        "opposite_required_signs": True,
        "independent_source_graphs": True,
        "same_external_operator_tensor_sha256": triangle.external_tensor.identity_sha256,
        "complete_contact_census": True,
        "identity": "hat_delta-delta_(4)=-tilde_delta",
    }
    proof_sha256 = digest(proof_record)
    tilde = MetricTensor(
        MetricKind.TILDE,
        triangle.metric.indices,
        MetricStage.POST_CONTACT_SUBTRACTION,
        triangle.term_id + "+" + contact.term_id,
        "VALIDATED_INDEPENDENT_CONTACT_SUBTRACTION",
        proof_sha256,
    )
    output = {
        "schema": "step6.validated_dred_contact_subtraction.v1",
        "stage": MetricStage.POST_CONTACT_SUBTRACTION.value,
        "inputs": {
            "triangle": triangle.as_json(),
            "contact": contact.as_json(),
        },
        "proof_record": proof_record,
        "proof_sha256": proof_sha256,
        "result": {
            "coefficient": triangle.coefficient.negated().as_json(),
            "metric": tilde.as_json(),
            "external_operator_tensor": triangle.external_tensor.as_json(),
        },
        "interpretation_status": "TYPED_METRIC_IDENTITY_ONLY_NOT_AN_ANOMALY_COEFFICIENT",
        "epsilon_trace_applied": False,
    }
    output["output_sha256"] = digest(output)
    return output


def metric_trace(kind: MetricKind) -> dict[str, Any]:
    """Return exact metric traces for audit; never mutate a bare numerator."""
    rows = {
        MetricKind.DELTA4: {
            "expression": "4",
            "atoms": [],
        },
        MetricKind.HAT: {
            "expression": "d",
            "definition": "d=4-2*epsilon_DRED",
            "atoms": [ScalarAtom("d", ScalarAtomKind.DRED_DIMENSION).as_json()],
        },
        MetricKind.TILDE: {
            "expression": "2*epsilon_DRED",
            "atoms": [
                ScalarAtom("epsilon_DRED", ScalarAtomKind.DRED_REGULATOR).as_json()
            ],
        },
    }
    return {
        "stage": MetricStage.METRIC_IDENTITY_AUDIT.value,
        "metric": kind.value,
        **rows[kind],
        "bare_numerator_mutated": False,
    }


def _v(name: str, variance: Variance = Variance.UPPER) -> TensorIndex:
    return TensorIndex(name, IndexSpace.VECTOR_4, variance)


def _external(operator_id: str, names: Sequence[str]) -> ExternalOperatorTensor:
    return ExternalOperatorTensor(
        operator_id,
        tuple(_v(name, Variance.LOWER) for name in names),
        {
            "op": "ExternalOperatorTensor",
            "operator": operator_id,
            "ordered_vector_slots": list(names),
            "free_color_slots": ["A", "B", "R", "S"],
        },
        "TYPED_FIXTURE_NO_PHYSICAL_COEFFICIENT",
    )


def build_fixtures() -> dict[str, Any]:
    m, n, r, s = (_v(name) for name in ("m", "n", "r", "s"))
    u, v = (_v(name) for name in ("u", "v"))
    q = MomentumVector("q", MomentumRole.CENTERED_LOOP)
    spin_metric = MetricTensor(
        MetricKind.DELTA4,
        (u, v),
        MetricStage.SPIN_DALGEBRA,
        "fixture:D-algebra",
        "FOUR_DIMENSIONAL_SPINOR_ANTICOMMUTATOR",
    )
    coefficient = ExactCoefficient(1, Fraction(3, 5), (ScalarAtom("C"),))
    rank2_bare = BareTensorNumerator(
        "N_rank2_fixture",
        _external("T2", ("m", "n")),
        (MomentumFactor(q, m), MomentumFactor(q, n)),
        coefficient,
        ScalarAtom("I_qiqj"),
        (spin_metric,),
        "G_rank2_fixture",
    )
    rank4_bare = BareTensorNumerator(
        "N_rank4_fixture",
        _external("T4", ("m", "n", "r", "s")),
        tuple(MomentumFactor(q, index) for index in (m, n, r, s)),
        coefficient,
        ScalarAtom("I_q4"),
        (spin_metric,),
        "G_rank4_fixture",
    )
    generic_contractions = Rank4Contractions(
        ScalarAtom("X"), ScalarAtom("Y"), ScalarAtom("Z")
    )

    contact_external = _external("T2", ("m", "n"))
    c = ExactCoefficient(1, Fraction(1, 1), (ScalarAtom("C"),))
    triangle = IndependentMetricTerm(
        "triangle_metric_fixture",
        "G_triangle_fixture",
        digest({"fixture": "triangle-independent-derivation"}),
        c,
        _hat_metric((m, n), "triangle:rank2-average"),
        contact_external,
    )
    contact = IndependentMetricTerm(
        "contact_metric_fixture",
        "G_contact_family_fixture",
        digest({"fixture": "contact-independent-derivation"}),
        c.negated(),
        MetricTensor(
            MetricKind.DELTA4,
            (m, n),
            MetricStage.CONTACT_DALGEBRA,
            "contact:D-algebra",
            "INDEPENDENT_SD_CONTACT_DALGEBRA",
        ),
        contact_external,
        "SD_COMPLETE_CONTACT_FAMILY",
    )
    return {
        "rank2_bare": rank2_bare.as_json(),
        "rank2_average": rank2_average(rank2_bare),
        "rank4_bare": rank4_bare.as_json(),
        "rank4_generic_average": rank4_average(rank4_bare, generic_contractions),
        "rank4_identical_average": rank4_identical_average(rank4_bare),
        "contact_subtraction": validated_contact_subtraction(triangle, contact),
    }


def _expect_failure(label: str, fn: Any) -> dict[str, Any]:
    try:
        fn()
    except DREDReducerError as error:
        return {
            "label": label,
            "status": "EXPECTED_FAIL_CLOSED",
            "exception": type(error).__name__,
            "message": str(error),
        }
    raise AssertionError(f"negative test {label} unexpectedly succeeded")


def negative_fixture_results() -> list[dict[str, Any]]:
    m, n = _v("m"), _v("n")
    lower_m = _v("m", Variance.LOWER)
    external = _external("T2", ("m", "n"))
    q = MomentumVector("q", MomentumRole.CENTERED_LOOP)
    c = ExactCoefficient(1, atoms=(ScalarAtom("C"),))

    def bare_with_illegal_epsilon() -> None:
        BareTensorNumerator(
            "bad-epsilon",
            external,
            (MomentumFactor(q, m), MomentumFactor(q, n)),
            ExactCoefficient(
                1, atoms=(ScalarAtom("epsilon_DRED", ScalarAtomKind.DRED_REGULATOR),)
            ),
            ScalarAtom("I2"),
            (),
            "G_bad",
        )

    def spinor_momentum_index() -> None:
        MomentumFactor(
            q,
            TensorIndex("a", IndexSpace.SPINOR_UNDOTTED, Variance.UPPER),
        )

    def four_spin_momentum_support() -> None:
        MomentumVector(
            "q4", MomentumRole.CENTERED_LOOP, MomentumSupport.FOUR_SPIN
        )

    def hat_in_spin_algebra() -> None:
        MetricTensor(
            MetricKind.HAT,
            (m, n),
            MetricStage.SPIN_DALGEBRA,
            "bad",
            "bad",
        )

    def delta4_in_loop_average() -> None:
        MetricTensor(
            MetricKind.DELTA4,
            (m, n),
            MetricStage.LOOP_TENSOR_AVERAGING,
            "bad",
            "bad",
        )

    def premature_tilde() -> None:
        MetricTensor(
            MetricKind.TILDE,
            (m, n),
            MetricStage.LOOP_TENSOR_AVERAGING,
            "bad",
            "bad",
        )

    def spinor_metric_index() -> None:
        MetricTensor(
            MetricKind.DELTA4,
            (
                TensorIndex("a", IndexSpace.SPINOR_UNDOTTED, Variance.UPPER),
                n,
            ),
            MetricStage.SPIN_DALGEBRA,
            "bad",
            "bad",
        )

    def repeated_rank2_index() -> None:
        BareTensorNumerator(
            "bad-repeat",
            external,
            (MomentumFactor(q, m), MomentumFactor(q, m)),
            c,
            ScalarAtom("I2"),
            (),
            "G_bad",
        )

    def wrong_variance_momentum() -> None:
        MomentumFactor(q, lower_m)

    return [
        _expect_failure("epsilon_in_bare_numerator", bare_with_illegal_epsilon),
        _expect_failure("spinor_index_on_momentum", spinor_momentum_index),
        _expect_failure("momentum_outside_hat_space", four_spin_momentum_support),
        _expect_failure("hat_metric_in_spin_D_algebra", hat_in_spin_algebra),
        _expect_failure("delta4_metric_in_loop_average", delta4_in_loop_average),
        _expect_failure("premature_tilde_metric", premature_tilde),
        _expect_failure("spinor_index_on_vector_metric", spinor_metric_index),
        _expect_failure("repeated_rank2_free_index", repeated_rank2_index),
        _expect_failure("covariant_centered_momentum", wrong_variance_momentum),
    ]


def build_payload() -> dict[str, Any]:
    fixtures = build_fixtures()
    negative = negative_fixture_results()
    return {
        "schema": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "authority": {
            "contract": str(CONTRACT.relative_to(ROOT)),
            "contract_sha256": file_sha256(CONTRACT),
            "external_target_imported": False,
            "review_input_imported": False,
        },
        "typed_contract": {
            "delta4": {
                "owner": MetricStage.SPIN_DALGEBRA.value,
                "contact_owner": MetricStage.CONTACT_DALGEBRA.value,
            },
            "hat_delta": {"owner": MetricStage.LOOP_TENSOR_AVERAGING.value},
            "tilde_delta": {
                "owner": MetricStage.POST_CONTACT_SUBTRACTION.value,
                "only_constructor": "validated_contact_subtraction",
            },
            "metric_decomposition": "delta_(4)=hat_delta+tilde_delta",
            "orthogonality": "hat_delta*tilde_delta=0",
            "projectors": [
                "hat_delta^2=hat_delta",
                "tilde_delta^2=tilde_delta",
            ],
            "traces": {
                "delta_(4)": metric_trace(MetricKind.DELTA4),
                "hat_delta": metric_trace(MetricKind.HAT),
                "tilde_delta": metric_trace(MetricKind.TILDE),
            },
            "bare_numerator_epsilon": "FORBIDDEN",
            "d_expansion_before_laurent_multiplication": "FORBIDDEN",
        },
        "fixtures": fixtures,
        "negative_type_tests": negative,
        "terminal_blocks": {
            "master_integrals": None,
            "UV_poles": None,
            "renormalized_coefficients": None,
            "external_target_comparison": None,
            "status": "OUT_OF_SCOPE_NO_RESULT_CLAIM",
        },
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    fixtures = payload["fixtures"]
    checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, evidence: Any) -> None:
        checks.append(
            {
                "name": name,
                "status": "PASS" if passed else "FAIL",
                "evidence": evidence,
            }
        )

    check("contract_exists", CONTRACT.is_file(), str(CONTRACT))
    check(
        "rank2_external_tensor_preserved",
        fixtures["rank2_bare"]["external_operator_tensor"]["identity_sha256"]
        == fixtures["rank2_average"]["external_operator_tensor_preserved_sha256"],
        fixtures["rank2_average"]["external_operator_tensor_preserved_sha256"],
    )
    check(
        "rank2_average_uses_hat_over_d",
        fixtures["rank2_average"]["terms"][0]["metric_product"][0]["kind"]
        == MetricKind.HAT.value
        and fixtures["rank2_average"]["terms"][0]["coefficient"]["denominator_factors"]
        == ["d"],
        fixtures["rank2_average"]["terms"][0],
    )
    rank4_terms = fixtures["rank4_generic_average"]["terms"]
    check(
        "rank4_three_pairings",
        len(rank4_terms) == 3
        and all(len(term["metric_product"]) == 2 for term in rank4_terms)
        and [term["channel"] for term in rank4_terms] == ["A", "B", "C"],
        [term["channel"] for term in rank4_terms],
    )
    check(
        "rank4_exact_denominator",
        all(
            term["coefficient"]["denominator_factors"] == ["d", "d-1", "d+2"]
            for term in rank4_terms
        ),
        [term["coefficient"]["denominator_factors"] for term in rank4_terms],
    )
    identical_terms = fixtures["rank4_identical_average"]["terms"]
    check(
        "rank4_identical_specialization",
        len(identical_terms) == 3
        and all(
            term["coefficient"]["denominator_factors"] == ["d", "d+2"]
            for term in identical_terms
        ),
        fixtures["rank4_identical_average"]["formula"],
    )
    check(
        "spin_metric_is_not_replaced",
        fixtures["rank2_average"]["spin_metric_replacement_performed"] is False
        and fixtures["rank2_average"]["spectator_spin_dalgebra_metrics"][0]["kind"]
        == MetricKind.DELTA4.value,
        fixtures["rank2_average"]["spectator_spin_dalgebra_metrics"],
    )
    check(
        "no_epsilon_in_bare_numerators",
        all(
            not row["regulator_scalar_in_bare_numerator"]
            for row in (fixtures["rank2_bare"], fixtures["rank4_bare"])
        ),
        "typed ScalarAtomKind gate",
    )
    subtraction = fixtures["contact_subtraction"]
    check(
        "tilde_only_after_validated_contact_subtraction",
        subtraction["stage"] == MetricStage.POST_CONTACT_SUBTRACTION.value
        and subtraction["result"]["metric"]["kind"] == MetricKind.TILDE.value
        and subtraction["result"]["metric"]["proof_sha256"]
        == subtraction["proof_sha256"],
        subtraction["proof_record"],
    )
    check(
        "contact_result_is_minus_C_tilde",
        subtraction["result"]["coefficient"]["sign"] == -1
        and subtraction["proof_record"]["identity"]
        == "hat_delta-delta_(4)=-tilde_delta",
        subtraction["result"],
    )
    negative = payload["negative_type_tests"]
    check(
        "all_illegal_type_mixes_fail_closed",
        len(negative) == 9
        and all(row["status"] == "EXPECTED_FAIL_CLOSED" for row in negative),
        negative,
    )
    check(
        "trace_contract_exact",
        payload["typed_contract"]["traces"]["delta_(4)"]["expression"] == "4"
        and payload["typed_contract"]["traces"]["hat_delta"]["expression"] == "d"
        and payload["typed_contract"]["traces"]["tilde_delta"]["expression"]
        == "2*epsilon_DRED",
        payload["typed_contract"]["traces"],
    )
    check(
        "no_terminal_physics_result",
        all(
            payload["terminal_blocks"][key] is None
            for key in (
                "master_integrals",
                "UV_poles",
                "renormalized_coefficients",
                "external_target_comparison",
            )
        ),
        payload["terminal_blocks"],
    )
    failed = sum(row["status"] == "FAIL" for row in checks)
    return {
        "schema": "step6.dred_reducer.audit.v1",
        "status": "PASS" if failed == 0 else "FAIL",
        "checks": checks,
        "totals": {"checks": len(checks), "failed": failed},
        "payload_sha256": digest(payload),
    }


def render_markdown(payload: Mapping[str, Any]) -> str:
    subtraction = payload["fixtures"]["contact_subtraction"]
    return rf"""# Step 6 typed DRED numerator reducer

`{STATUS}`

## 1. Metric types

$$
\delta_{{(4)}}^{{mn}}=\widehat\delta^{{mn}}+\widetilde\delta^{{mn}},
\qquad
\widehat\delta\widetilde\delta=0.
$$

$$
\operatorname{{tr}}\delta_{{(4)}}=4,
\qquad
\operatorname{{tr}}\widehat\delta=d=4-2\epsilon,
\qquad
\operatorname{{tr}}\widetilde\delta=2\epsilon.
$$

$$
\text{{spin/D algebra}}:\ \delta_{{(4)}},
\qquad
\text{{loop tensor averaging}}:\ \widehat\delta.
$$

## 2. Rank two

$$
\int q_i^m q_j^nF
=\frac{{\widehat\delta^{{mn}}}}{{d}}
\int(q_i\cdot q_j)F.
$$

## 3. Rank four

$$
T^{{mnrs}}
=A\widehat\delta^{{mn}}\widehat\delta^{{rs}}
+B\widehat\delta^{{mr}}\widehat\delta^{{ns}}
+C\widehat\delta^{{ms}}\widehat\delta^{{nr}}.
$$

$$
\begin{{aligned}}
X&=d^2A+dB+dC,\\
Y&=dA+d^2B+dC,\\
Z&=dA+dB+d^2C,
\end{{aligned}}
$$

$$
\begin{{aligned}}
A&=\frac{{(d+1)X-Y-Z}}{{d(d-1)(d+2)}},\\
B&=\frac{{-X+(d+1)Y-Z}}{{d(d-1)(d+2)}},\\
C&=\frac{{-X-Y+(d+1)Z}}{{d(d-1)(d+2)}}.
\end{{aligned}}
$$

For one centered vector,

$$
\int q^mq^nq^rq^sF
=\frac{{
\widehat\delta^{{mn}}\widehat\delta^{{rs}}
+\widehat\delta^{{mr}}\widehat\delta^{{ns}}
+\widehat\delta^{{ms}}\widehat\delta^{{nr}}
}}{{d(d+2)}}\int(q^2)^2F.
$$

## 4. Contact subtraction gate

$$
+C\widehat\delta^{{mn}}-C\delta_{{(4)}}^{{mn}}
=-C\widetilde\delta^{{mn}}.
$$

Proof hash:

`{subtraction['proof_sha256']}`

No master integral, UV pole, or anomaly coefficient is evaluated.
"""


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError("Step-6 typed DRED reducer audit failed")
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
                "negative_type_tests": len(payload["negative_type_tests"]),
                "generated": str(GENERATED_JSON.relative_to(ROOT)),
            },
            sort_keys=True,
        )
    )
