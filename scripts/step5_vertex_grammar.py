#!/usr/bin/env python3
"""Project-derived ordered vertex grammar for Step 5.

Only the locked Project equations named in ``source_equations`` determine the
objects below.  Imported source coefficients and anomaly coefficients do not
enter this module.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial
from typing import Sequence

from scripts.step5_graph_ir import Chirality, IndexSpace, Statistics, Variance


class GrammarStatus(str, Enum):
    PROVED_FROM_PROJECT = "PROVED_FROM_PROJECT"
    BLOCKED_GHOST_NORMALIZATION = "BLOCKED_GHOST_NORMALIZATION"
    BLOCKED_UNINSTANTIATED_E_XI_CORE = "BLOCKED_UNINSTANTIATED_E_XI_CORE"


class CompositeKind(str, Enum):
    GAMMA = "Gamma"
    TILDE_GAMMA = "TildeGamma"
    W = "W"
    TILDE_W = "TildeW"


@dataclass(frozen=True)
class ExactCoefficient:
    """An exact scalar in Q[sqrt(2), i] times named commuting symbols."""

    rational: Fraction = Fraction(1)
    sqrt2_power: int = 0
    i_power: int = 0
    symbols: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        rational = Fraction(self.rational)
        sqrt2_power = self.sqrt2_power
        i_power = self.i_power
        if sqrt2_power < 0:
            raise ValueError("negative sqrt(2) powers are not used in the locked Step-5 grammar")
        if any(not symbol for symbol in self.symbols):
            raise ValueError("coefficient symbols must be nonempty")
        sqrt_pairs, sqrt_remainder = divmod(sqrt2_power, 2)
        rational *= 2**sqrt_pairs
        i_remainder = i_power % 4
        if i_remainder == 2:
            rational *= -1
            i_remainder = 0
        elif i_remainder == 3:
            rational *= -1
            i_remainder = 1
        object.__setattr__(self, "rational", rational)
        object.__setattr__(self, "sqrt2_power", sqrt_remainder)
        object.__setattr__(self, "i_power", i_remainder)
        object.__setattr__(self, "symbols", tuple(sorted(self.symbols)))

    def __mul__(self, other: ExactCoefficient | int | Fraction) -> ExactCoefficient:
        if isinstance(other, (int, Fraction)):
            other = ExactCoefficient(Fraction(other))
        if not isinstance(other, ExactCoefficient):
            return NotImplemented
        return ExactCoefficient(
            self.rational * other.rational,
            self.sqrt2_power + other.sqrt2_power,
            self.i_power + other.i_power,
            self.symbols + other.symbols,
        )

    def __neg__(self) -> ExactCoefficient:
        return ExactCoefficient(
            -self.rational,
            self.sqrt2_power,
            self.i_power,
            self.symbols,
        )

    def render(self) -> str:
        if self.rational == 0:
            return "0"
        factors: list[str] = []
        magnitude = abs(self.rational)
        if magnitude != 1 or not (self.sqrt2_power or self.i_power or self.symbols):
            factors.append(
                str(magnitude.numerator)
                if magnitude.denominator == 1
                else f"{magnitude.numerator}/{magnitude.denominator}"
            )
        if self.sqrt2_power:
            factors.append("sqrt(2)")
        if self.i_power:
            factors.append("i")
        factors.extend(self.symbols)
        word = "*".join(factors) if factors else "1"
        return f"-{word}" if self.rational < 0 else word


@dataclass(frozen=True)
class FieldOccurrence:
    occurrence_id: str
    field_name: str
    statistics: Statistics
    chirality: Chirality
    color_label: str
    flavor_label: str | None = None
    spinor_label: str | None = None
    direct_derivatives: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if any(not value for value in (self.occurrence_id, self.field_name, self.color_label)):
            raise ValueError("field occurrences need id, type, and color")

    @property
    def parity(self) -> int:
        return int(self.statistics is Statistics.FERMION)


@dataclass(frozen=True)
class DerivativeScope:
    scope_id: str
    operators: tuple[str, ...]
    ordered_occurrence_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.scope_id or not self.operators or not self.ordered_occurrence_ids:
            raise ValueError("a derivative scope must retain operator word and ordered support")


@dataclass(frozen=True)
class SpinorContraction:
    index_space: IndexSpace
    left_label: str
    left_variance: Variance
    right_label: str
    right_variance: Variance
    pairing: str

    def __post_init__(self) -> None:
        if self.index_space not in (IndexSpace.UNDOTTED, IndexSpace.DOTTED):
            raise ValueError("a spinor contraction must be undotted or dotted")
        if any(not value for value in (self.left_label, self.right_label, self.pairing)):
            raise ValueError("a spinor contraction must retain both labels and pairing")
        if {self.left_variance, self.right_variance} != {Variance.UP, Variance.DOWN}:
            raise ValueError("a contracted spinor pair has one upper and one lower slot")


@dataclass(frozen=True)
class CompositeExpansionTerm:
    term_id: str
    composite: CompositeKind
    degree_in_v: int
    coefficient: ExactCoefficient
    occurrences: tuple[FieldOccurrence, ...]
    derivative_scopes: tuple[DerivativeScope, ...]
    output_color: str
    color_word: tuple[str, ...]
    source_equations: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.degree_in_v < 1:
            raise ValueError("connection and field-strength terms start at one V")
        _validate_occurrences_and_scopes(self.occurrences, self.derivative_scopes)
        if self.coefficient.rational == 0:
            raise ValueError("zero composite terms are omitted")


@dataclass(frozen=True)
class ActionMonomial:
    monomial_id: str
    sector: str
    measure: str
    coefficient: ExactCoefficient
    ordered_fields: tuple[FieldOccurrence, ...]
    color_word: tuple[str, ...]
    derivative_scopes: tuple[DerivativeScope, ...] = ()
    source_equations: tuple[str, ...] = ()
    status: GrammarStatus = GrammarStatus.PROVED_FROM_PROJECT
    spinor_contractions: tuple[SpinorContraction, ...] = ()

    def __post_init__(self) -> None:
        if any(not value for value in (self.monomial_id, self.sector, self.measure)):
            raise ValueError("an action monomial needs id, sector, and superspace measure")
        if self.coefficient.rational == 0:
            raise ValueError("zero action monomials are omitted")
        if not self.source_equations:
            raise ValueError("every action monomial must cite its Project derivation equations")
        _validate_occurrences_and_scopes(self.ordered_fields, self.derivative_scopes)
        spinor_labels = {field.spinor_label for field in self.ordered_fields if field.spinor_label}
        for contraction in self.spinor_contractions:
            if contraction.left_label not in spinor_labels or contraction.right_label not in spinor_labels:
                raise ValueError("a spinor contraction references an absent field spinor slot")


@dataclass(frozen=True)
class TypedZeroMonomial:
    monomial_id: str
    sector: str
    zero_reason: str
    source_equations: tuple[str, ...]

    def __post_init__(self) -> None:
        if any(not value for value in (self.monomial_id, self.sector, self.zero_reason)):
            raise ValueError("a typed zero must retain id, sector, and exact reason")
        if not self.source_equations:
            raise ValueError("a typed zero must cite its Project derivation equations")


@dataclass(frozen=True)
class DerivativeRequest:
    field_name: str
    external_slot: str


@dataclass(frozen=True)
class ExternalVertexSlot:
    external_slot: str
    selected_occurrence_id: str
    field_name: str
    color_label: str
    flavor_label: str | None
    spinor_label: str | None
    direct_derivatives: tuple[str, ...]


@dataclass(frozen=True)
class FunctionalDerivativeTerm:
    permutation_id: tuple[str, ...]
    koszul_sign: int
    coefficient: ExactCoefficient
    external_slots: tuple[ExternalVertexSlot, ...]
    remaining_fields: tuple[FieldOccurrence, ...]


@dataclass(frozen=True)
class OrderedVertex:
    vertex_id: str
    source_monomial_id: str
    ordered_derivative_requests: tuple[DerivativeRequest, ...]
    terms: tuple[FunctionalDerivativeTerm, ...]
    color_word: tuple[str, ...]
    derivative_scopes: tuple[DerivativeScope, ...]
    spinor_contractions: tuple[SpinorContraction, ...]
    source_equations: tuple[str, ...]


def ordered_functional_derivative(
    monomial: ActionMonomial,
    requests: Sequence[DerivativeRequest],
    *,
    vertex_id: str | None = None,
) -> OrderedVertex:
    """Apply ordered left functional derivatives without combining permutations."""

    state: list[
        tuple[
            tuple[FieldOccurrence, ...],
            tuple[ExternalVertexSlot, ...],
            tuple[str, ...],
            int,
        ]
    ] = [(monomial.ordered_fields, (), (), 1)]
    for request in requests:
        next_state: list[
            tuple[
                tuple[FieldOccurrence, ...],
                tuple[ExternalVertexSlot, ...],
                tuple[str, ...],
                int,
            ]
        ] = []
        for fields, slots, permutation, sign in state:
            for position, occurrence in enumerate(fields):
                if occurrence.field_name != request.field_name:
                    continue
                preceding_parity = sum(item.parity for item in fields[:position]) % 2
                local_sign = -1 if occurrence.parity and preceding_parity else 1
                slot = ExternalVertexSlot(
                    request.external_slot,
                    occurrence.occurrence_id,
                    occurrence.field_name,
                    occurrence.color_label,
                    occurrence.flavor_label,
                    occurrence.spinor_label,
                    occurrence.direct_derivatives,
                )
                next_state.append(
                    (
                        fields[:position] + fields[position + 1 :],
                        slots + (slot,),
                        permutation + (occurrence.occurrence_id,),
                        sign * local_sign,
                    )
                )
        state = next_state
    terms = tuple(
        FunctionalDerivativeTerm(
            permutation,
            sign,
            monomial.coefficient * sign,
            slots,
            remaining,
        )
        for remaining, slots, permutation, sign in sorted(state, key=lambda item: item[2])
    )
    return OrderedVertex(
        vertex_id or f"vertex__{monomial.monomial_id}",
        monomial.monomial_id,
        tuple(requests),
        terms,
        monomial.color_word,
        monomial.derivative_scopes,
        monomial.spinor_contractions,
        monomial.source_equations,
    )


def full_ordered_vertex(monomial: ActionMonomial) -> OrderedVertex:
    """Differentiate every ordered occurrence and retain identical-leg branches."""

    return ordered_functional_derivative(
        monomial,
        tuple(
            DerivativeRequest(occurrence.field_name, f"slot_{position}")
            for position, occurrence in enumerate(monomial.ordered_fields)
        ),
        vertex_id=f"full_vertex__{monomial.monomial_id}",
    )


def matter_bridge_monomials() -> tuple[ActionMonomial, ...]:
    """Expand -h kappa tildePhi exp(V_ad) Phi through V^2."""

    base = (
        FieldOccurrence("matter_tphi", "TildePhi", Statistics.BOSON, Chirality.ANTICHIRAL, "A", "r"),
        FieldOccurrence("matter_phi", "Phi", Statistics.BOSON, Chirality.CHIRAL, "C", "r"),
    )
    quadratic = ActionMonomial(
        "matter_bridge_v0",
        "MATTER_BRIDGE",
        "E,8",
        ExactCoefficient(Fraction(-1), symbols=("h",)),
        base,
        ("kappa[A,B]", "delta[B,C]"),
        source_equations=("4C.4", "5.16"),
    )
    cubic = ActionMonomial(
        "matter_bridge_v1",
        "MATTER_BRIDGE",
        "E,8",
        ExactCoefficient(Fraction(-1), i_power=1, symbols=("h",)),
        (
            base[0],
            FieldOccurrence("matter_v1", "V", Statistics.BOSON, Chirality.REAL, "D"),
            base[1],
        ),
        ("kappa[A,B]", "c[D,C,B]"),
        source_equations=("3A.32", "4C.4", "4C.8", "5.16"),
    )
    quartic = ActionMonomial(
        "matter_bridge_v2",
        "MATTER_BRIDGE",
        "E,8",
        ExactCoefficient(Fraction(1, 2), symbols=("h",)),
        (
            base[0],
            FieldOccurrence("matter_v2a", "V", Statistics.BOSON, Chirality.REAL, "D"),
            FieldOccurrence("matter_v2b", "V", Statistics.BOSON, Chirality.REAL, "F"),
            base[1],
        ),
        ("kappa[A,B]", "c[D,E,B]", "c[F,C,E]"),
        source_equations=("3A.32", "4C.4", "4C.8", "5.16"),
    )
    return quadratic, cubic, quartic


def chiral_cubic_monomials() -> tuple[ActionMonomial, ...]:
    coefficient = ExactCoefficient(Fraction(1, 6), sqrt2_power=1, symbols=("h",))
    chiral = ActionMonomial(
        "n4_chiral_cubic",
        "N4_SUPERPOTENTIAL",
        "E,+",
        coefficient,
        tuple(
            FieldOccurrence(
                f"phi_{slot}",
                "Phi",
                Statistics.BOSON,
                Chirality.CHIRAL,
                color,
                flavor,
            )
            for slot, color, flavor in ((1, "A", "r"), (2, "B", "s"), (3, "C", "t"))
        ),
        ("epsilon[r,s,t]", "c[A,B,C]"),
        source_equations=("4C.4", "4C.13"),
    )
    tilded = ActionMonomial(
        "n4_tilde_chiral_cubic",
        "N4_TILDE_SUPERPOTENTIAL",
        "E,-",
        coefficient,
        tuple(
            FieldOccurrence(
                f"tphi_{slot}",
                "TildePhi",
                Statistics.BOSON,
                Chirality.ANTICHIRAL,
                color,
                flavor,
            )
            for slot, color, flavor in ((1, "A", "r"), (2, "B", "s"), (3, "C", "t"))
        ),
        ("epsilon[r,s,t]", "c[A,B,C]"),
        source_equations=("4C.2a", "4C.4", "4C.13"),
    )
    return chiral, tilded


def connection_expansion(kind: CompositeKind) -> tuple[CompositeExpansionTerm, ...]:
    if kind not in (CompositeKind.GAMMA, CompositeKind.TILDE_GAMMA):
        raise ValueError("connection_expansion accepts Gamma or TildeGamma")
    terms: list[CompositeExpansionTerm] = []
    for degree in range(1, 4):
        n = degree - 1
        if kind is CompositeKind.GAMMA:
            rational = Fraction((-1) ** n, factorial(n + 1))
            direct_derivative = "D_a"
            equations = ("3A.34",)
        else:
            rational = Fraction(-1, factorial(n + 1))
            direct_derivative = "barD_dot_a"
            equations = ("3A.34a",)
        occurrences = _adjoint_word_occurrences(
            degree,
            prefix=f"{kind.value}_d{degree}",
            core_derivative=direct_derivative,
        )
        terms.append(
            CompositeExpansionTerm(
                f"{kind.value}_degree_{degree}",
                kind,
                degree,
                ExactCoefficient(rational, i_power=n),
                occurrences,
                (),
                "X",
                _nested_ad_color(tuple(item.color_label for item in occurrences), "X"),
                equations,
            )
        )
    return tuple(terms)


def field_strength_expansion(kind: CompositeKind) -> tuple[CompositeExpansionTerm, ...]:
    if kind is CompositeKind.W:
        connection_kind = CompositeKind.GAMMA
        projector = ("barD^2",)
        projector_coefficient = ExactCoefficient(Fraction(-1, 8))
        equations = ("3A.34", "3A.51")
    elif kind is CompositeKind.TILDE_W:
        connection_kind = CompositeKind.TILDE_GAMMA
        projector = ("D^2",)
        projector_coefficient = ExactCoefficient(Fraction(1, 8))
        equations = ("3A.34a", "3A.52")
    else:
        raise ValueError("field_strength_expansion accepts W or TildeW")
    terms: list[CompositeExpansionTerm] = []
    for connection_term in connection_expansion(connection_kind):
        support = tuple(item.occurrence_id for item in connection_term.occurrences)
        terms.append(
            CompositeExpansionTerm(
                f"{kind.value}_degree_{connection_term.degree_in_v}",
                kind,
                connection_term.degree_in_v,
                projector_coefficient * connection_term.coefficient,
                connection_term.occurrences,
                (DerivativeScope(f"{kind.value}_projector_{connection_term.degree_in_v}", projector, support),),
                connection_term.output_color,
                connection_term.color_word,
                equations,
            )
        )
    return tuple(terms)


def gauge_kinetic_monomials() -> tuple[ActionMonomial, ...]:
    result: list[ActionMonomial] = []
    for kind, sector, measure, left_spinor, right_spinor, equations in (
        (CompositeKind.W, "GAUGE_KINETIC_W", "E,+", "a_up", "a_down", ("3A.51", "4C.4", "5.16")),
        (
            CompositeKind.TILDE_W,
            "GAUGE_KINETIC_TILDE_W",
            "E,-",
            "dot_a_down",
            "dot_a_up",
            ("3A.52", "4C.4", "5.16"),
        ),
    ):
        for left_degree in range(1, 4):
            for right_degree in range(1, 4):
                if left_degree + right_degree > 4:
                    continue
                left = _field_strength_term_with_prefix(kind, left_degree, "L", "X", left_spinor)
                right = _field_strength_term_with_prefix(kind, right_degree, "R", "Y", right_spinor)
                result.append(
                    ActionMonomial(
                        f"{sector.lower()}_v{left_degree}_{right_degree}",
                        sector,
                        measure,
                        ExactCoefficient(Fraction(-1, 4), symbols=("h",))
                        * left.coefficient
                        * right.coefficient,
                        left.occurrences + right.occurrences,
                        left.color_word + right.color_word + ("kappa[X,Y]",),
                        left.derivative_scopes + right.derivative_scopes,
                        equations,
                        spinor_contractions=(
                            SpinorContraction(
                                IndexSpace.UNDOTTED
                                if kind is CompositeKind.W
                                else IndexSpace.DOTTED,
                                left_spinor,
                                Variance.UP if kind is CompositeKind.W else Variance.DOWN,
                                right_spinor,
                                Variance.DOWN if kind is CompositeKind.W else Variance.UP,
                                (
                                    "W^a W_a upper-lower evaluation"
                                    if kind is CompositeKind.W
                                    else "TildeW_dot_a TildeW^dot_a lower-upper evaluation"
                                ),
                            ),
                        ),
                    )
                )
    return tuple(result)


def prepotential_euler_insertion_terms(max_v_order: int = 3) -> tuple[ActionMonomial, ...]:
    if max_v_order < 0 or max_v_order > 3:
        raise ValueError("the locked Step-5 insertion grammar is derived through V^3")
    terms: list[ActionMonomial] = []
    for n in range(max_v_order + 1):
        colors = tuple(f"A{position}" for position in range(1, n + 1)) + ("B",)
        occurrences = tuple(
            FieldOccurrence(
                f"euler_v_{position}",
                "V",
                Statistics.BOSON,
                Chirality.REAL,
                color,
            )
            for position, color in enumerate(colors[:-1], start=1)
        ) + (
            FieldOccurrence(
                "euler_core",
                "E_Xi",
                Statistics.BOSON,
                Chirality.UNCONSTRAINED,
                "B",
            ),
        )
        terms.append(
            ActionMonomial(
                f"prepotential_euler_ad_{n}",
                "PREPOTENTIAL_EULER_INSERTION",
                "E,8;local-insertion",
                ExactCoefficient(Fraction(1, factorial(n + 1)), i_power=n),
                occurrences,
                _nested_ad_color(colors, "C"),
                source_equations=("5.26", "5.28"),
            )
        )
    return tuple(terms)


def fp_ghost_monomials(max_v_order: int = 2) -> tuple[ActionMonomial, ...]:
    """Expand the exact (3D.84) BRST chart inside (3D.86),(3D.90)."""

    if max_v_order < 0 or max_v_order > 3:
        raise ValueError("the exact displayed Bernoulli series is implemented through V^3")
    # sV = i[(1-A/2+A^2/12) tilde_c -(1+A/2+A^2/12)c] + O(A^4).
    bernoulli: dict[str, tuple[Fraction, ...]] = {
        "tilde_c": (Fraction(1), Fraction(-1, 2), Fraction(1, 12), Fraction(0)),
        "c": (Fraction(-1), Fraction(-1, 2), Fraction(-1, 12), Fraction(0)),
    }
    result: list[ActionMonomial] = []
    for projection, antighost_name, measure, outer_operator in (
        ("plus", "cprime_plus", "E,+", "barNabla_B^2"),
        ("minus", "tilde_cprime_minus", "E,-", "Nabla_B^2"),
    ):
        for ghost_name, coefficients in bernoulli.items():
            for n in range(max_v_order + 1):
                rational = coefficients[n]
                if rational == 0:
                    continue
                if n == 0 and (
                    (projection == "plus" and ghost_name == "c")
                    or (projection == "minus" and ghost_name == "tilde_c")
                ):
                    continue
                v_occurrences = tuple(
                    FieldOccurrence(
                        f"fp_{projection}_{ghost_name}_v{n}_{position}",
                        "V",
                        Statistics.BOSON,
                        Chirality.REAL,
                        f"A{position}",
                    )
                    for position in range(1, n + 1)
                )
                ghost = FieldOccurrence(
                    f"fp_{projection}_{ghost_name}_core_{n}",
                    ghost_name,
                    Statistics.FERMION,
                    Chirality.ANTICHIRAL if ghost_name == "tilde_c" else Chirality.CHIRAL,
                    "B",
                )
                antighost = FieldOccurrence(
                    f"fp_{projection}_{ghost_name}_antighost_{n}",
                    antighost_name,
                    Statistics.FERMION,
                    Chirality.CHIRAL if projection == "plus" else Chirality.ANTICHIRAL,
                    "P",
                )
                support = tuple(item.occurrence_id for item in v_occurrences + (ghost,))
                colors = tuple(item.color_label for item in v_occurrences) + (ghost.color_label,)
                result.append(
                    ActionMonomial(
                        f"fp_{projection}_{ghost_name}_v{n}",
                        "FP_GHOST",
                        measure,
                        ExactCoefficient(Fraction(1, 4))
                        * ExactCoefficient(rational, i_power=n + 1),
                        (antighost,) + v_occurrences + (ghost,),
                        _nested_ad_color(colors, "X") + ("kappa[P,X]",),
                        (DerivativeScope(f"fp_scope_{projection}_{ghost_name}_{n}", (outer_operator,), support),),
                        source_equations=("3D.84", "3D.86", "3D.90", "3D.91"),
                        status=GrammarStatus.PROVED_FROM_PROJECT,
                    )
                )
    return tuple(result)


def fp_ghost_typed_zeros() -> tuple[TypedZeroMonomial, ...]:
    return (
        TypedZeroMonomial(
            "fp_plus_c_v0",
            "FP_GHOST",
            "barNabla_B^2 c=0 by background-covariant chirality",
            ("3D.43", "3D.83", "3D.84", "3D.86", "3D.90"),
        ),
        TypedZeroMonomial(
            "fp_minus_tilde_c_v0",
            "FP_GHOST",
            "Nabla_B^2 tilde_c=0 by background-covariant antichirality",
            ("3D.43", "3D.83", "3D.84", "3D.86", "3D.90"),
        ),
    )


@dataclass(frozen=True)
class VertexGrammarBundle:
    connection_terms: tuple[CompositeExpansionTerm, ...]
    field_strength_terms: tuple[CompositeExpansionTerm, ...]
    action_monomials: tuple[ActionMonomial, ...]
    insertion_monomials: tuple[ActionMonomial, ...]
    action_vertices: tuple[OrderedVertex, ...]
    insertion_vertices: tuple[OrderedVertex, ...]
    typed_zero_monomials: tuple[TypedZeroMonomial, ...]
    ghost_status: GrammarStatus
    insertion_chart_status: GrammarStatus
    insertion_core_status: GrammarStatus
    blockers: tuple[str, ...]


def build_project_vertex_grammar() -> VertexGrammarBundle:
    connection_terms = connection_expansion(CompositeKind.GAMMA) + connection_expansion(
        CompositeKind.TILDE_GAMMA
    )
    field_strength_terms = field_strength_expansion(CompositeKind.W) + field_strength_expansion(
        CompositeKind.TILDE_W
    )
    action = (
        matter_bridge_monomials()
        + chiral_cubic_monomials()
        + gauge_kinetic_monomials()
        + fp_ghost_monomials()
    )
    insertion = prepotential_euler_insertion_terms()
    return VertexGrammarBundle(
        connection_terms,
        field_strength_terms,
        action,
        insertion,
        tuple(full_ordered_vertex(monomial) for monomial in action),
        tuple(full_ordered_vertex(monomial) for monomial in insertion),
        fp_ghost_typed_zeros(),
        GrammarStatus.PROVED_FROM_PROJECT,
        GrammarStatus.PROVED_FROM_PROJECT,
        GrammarStatus.BLOCKED_UNINSTANTIATED_E_XI_CORE,
        ("BLOCKED_UNINSTANTIATED_E_XI_CORE",),
    )


@dataclass(frozen=True)
class CensusContractionRule:
    rule_id: str
    left_field: str
    right_field: str
    oriented: bool = False


@dataclass(frozen=True)
class CensusInternalPair:
    rule_id: str
    left_occurrence: str
    right_occurrence: str


@dataclass(frozen=True)
class TopologyCandidate:
    candidate_id: str
    insertion_monomial_id: str
    action_monomial_ids: tuple[str, ...]
    external_assignment: tuple[tuple[str, str], ...]
    internal_pairs: tuple[CensusInternalPair, ...]
    vertex_count: int
    internal_edge_count: int
    loop_number: int
    connected: bool
    topology: str
    external_extraction_sign: int
    wick_koszul_sign: int
    total_koszul_sign: int


@dataclass(frozen=True)
class TopologyCensus:
    candidates: tuple[TopologyCandidate, ...]
    generated_pairings: int
    rejected_disconnected: int
    rejected_non_one_loop: int


class CensusOverflow(RuntimeError):
    pass


@dataclass(frozen=True)
class _CensusOccurrence:
    occurrence_id: str
    vertex_id: str
    field_name: str
    parity: int


def census_one_loop_candidates(
    insertion_monomials: Sequence[ActionMonomial],
    action_monomials: Sequence[ActionMonomial],
    contraction_rules: Sequence[CensusContractionRule],
    external_fields: Sequence[str],
    *,
    min_action_vertices: int = 0,
    max_action_vertices: int = 2,
    allow_same_vertex_contractions: bool = False,
    max_candidates: int = 100_000,
) -> TopologyCensus:
    """Exhaustive labelled one-loop census; no graph is symmetry-quotiented."""

    if min_action_vertices < 0 or max_action_vertices < min_action_vertices:
        raise ValueError("invalid action-vertex range")
    rules = tuple(sorted(contraction_rules, key=lambda rule: rule.rule_id))
    candidates: list[TopologyCandidate] = []
    generated_pairings = 0
    rejected_disconnected = 0
    rejected_non_one_loop = 0

    for insertion in sorted(insertion_monomials, key=lambda item: item.monomial_id):
        for action_count in range(min_action_vertices, max_action_vertices + 1):
            for selected_actions in combinations_with_replacement(
                sorted(action_monomials, key=lambda item: item.monomial_id), action_count
            ):
                selected = (insertion,) + selected_actions
                occurrences: list[_CensusOccurrence] = []
                for vertex_position, monomial in enumerate(selected):
                    vertex_id = f"v{vertex_position}:{monomial.monomial_id}"
                    for occurrence in monomial.ordered_fields:
                        occurrences.append(
                            _CensusOccurrence(
                                f"{vertex_id}:{occurrence.occurrence_id}",
                                vertex_id,
                                occurrence.field_name,
                                occurrence.parity,
                            )
                        )
                for remaining, assignment, extraction_sign in _external_assignments(
                    tuple(occurrences), tuple(external_fields)
                ):
                    for pairs, wick_sign in _census_pairings(
                        remaining,
                        rules,
                        allow_same_vertex_contractions,
                    ):
                        generated_pairings += 1
                        vertex_ids = tuple(f"v{position}:{monomial.monomial_id}" for position, monomial in enumerate(selected))
                        connected = _is_connected(vertex_ids, pairs, remaining)
                        edge_count = len(pairs)
                        loop_number = edge_count - len(vertex_ids) + 1 if connected else -1
                        if not connected:
                            rejected_disconnected += 1
                            continue
                        if loop_number != 1:
                            rejected_non_one_loop += 1
                            continue
                        topology = {
                            (1, 1): "TADPOLE",
                            (2, 2): "BUBBLE",
                            (3, 3): "TRIANGLE",
                        }.get((len(vertex_ids), edge_count), "ONE_LOOP_MULTIGRAPH")
                        signature = tuple(
                            (pair.left_occurrence, pair.right_occurrence, pair.rule_id) for pair in pairs
                        )
                        candidate_id = (
                            f"candidate_{len(candidates):06d}__{insertion.monomial_id}__"
                            + "__".join(monomial.monomial_id for monomial in selected_actions)
                        )
                        candidates.append(
                            TopologyCandidate(
                                candidate_id,
                                insertion.monomial_id,
                                tuple(monomial.monomial_id for monomial in selected_actions),
                                assignment,
                                tuple(pairs),
                                len(vertex_ids),
                                edge_count,
                                loop_number,
                                connected,
                                topology,
                                extraction_sign,
                                wick_sign,
                                extraction_sign * wick_sign,
                            )
                        )
                        if len(candidates) > max_candidates:
                            raise CensusOverflow(
                                f"candidate count exceeded exact limit {max_candidates}; no truncation was returned"
                            )
    candidates.sort(
        key=lambda candidate: (
            candidate.insertion_monomial_id,
            candidate.action_monomial_ids,
            candidate.external_assignment,
            tuple(
                (pair.left_occurrence, pair.right_occurrence, pair.rule_id)
                for pair in candidate.internal_pairs
            ),
        )
    )
    candidates = [replace(candidate, candidate_id=f"candidate_{position:06d}") for position, candidate in enumerate(candidates)]
    return TopologyCensus(
        tuple(candidates),
        generated_pairings,
        rejected_disconnected,
        rejected_non_one_loop,
    )


def _validate_occurrences_and_scopes(
    occurrences: Sequence[FieldOccurrence], scopes: Sequence[DerivativeScope]
) -> None:
    ids = tuple(item.occurrence_id for item in occurrences)
    if len(ids) != len(set(ids)):
        raise ValueError("field occurrence ids must be unique")
    known = set(ids)
    for scope in scopes:
        if not set(scope.ordered_occurrence_ids) <= known:
            raise ValueError("a derivative scope references an absent occurrence")


def _adjoint_word_occurrences(
    degree: int,
    *,
    prefix: str,
    core_derivative: str,
) -> tuple[FieldOccurrence, ...]:
    return tuple(
        FieldOccurrence(
            f"{prefix}_v{position}",
            "V",
            Statistics.BOSON,
            Chirality.REAL,
            f"A{position}",
            direct_derivatives=(core_derivative,) if position == degree else (),
        )
        for position in range(1, degree + 1)
    )


def _nested_ad_color(input_colors: Sequence[str], output_color: str) -> tuple[str, ...]:
    if not input_colors:
        raise ValueError("an adjoint word needs a core color")
    if len(input_colors) == 1:
        return (f"delta[{input_colors[0]},{output_color}]",)
    core = input_colors[-1]
    current = "M1" if len(input_colors) > 2 else output_color
    result = [f"c[{input_colors[-2]},{core},{current}]"]
    intermediate_number = 1
    for position in range(len(input_colors) - 3, -1, -1):
        next_output = output_color if position == 0 else f"M{intermediate_number + 1}"
        result.append(f"c[{input_colors[position]},{current},{next_output}]")
        current = next_output
        intermediate_number += 1
    return tuple(result)


def _field_strength_term_with_prefix(
    kind: CompositeKind,
    degree: int,
    prefix: str,
    output_color: str,
    spinor_label: str,
) -> CompositeExpansionTerm:
    generic = field_strength_expansion(kind)[degree - 1]
    mapping: dict[str, str] = {}
    occurrences: list[FieldOccurrence] = []
    for occurrence in generic.occurrences:
        new_id = f"{prefix}_{occurrence.occurrence_id}"
        mapping[occurrence.occurrence_id] = new_id
        derivatives = tuple(
            f"D_{spinor_label}"
            if derivative == "D_a"
            else f"barD_{spinor_label}"
            if derivative == "barD_dot_a"
            else derivative
            for derivative in occurrence.direct_derivatives
        )
        occurrences.append(
            replace(
                occurrence,
                occurrence_id=new_id,
                color_label=f"{prefix}_{occurrence.color_label}",
                spinor_label=spinor_label if derivatives else occurrence.spinor_label,
                direct_derivatives=derivatives,
            )
        )
    scopes = tuple(
        DerivativeScope(
            f"{prefix}_{scope.scope_id}",
            scope.operators,
            tuple(mapping[item] for item in scope.ordered_occurrence_ids),
        )
        for scope in generic.derivative_scopes
    )
    colors = tuple(item.color_label for item in occurrences)
    return replace(
        generic,
        term_id=f"{prefix}_{generic.term_id}",
        occurrences=tuple(occurrences),
        derivative_scopes=scopes,
        output_color=output_color,
        color_word=_nested_ad_color(colors, output_color),
    )


def _external_assignments(
    occurrences: tuple[_CensusOccurrence, ...],
    external_fields: tuple[str, ...],
) -> tuple[tuple[tuple[_CensusOccurrence, ...], tuple[tuple[str, str], ...], int], ...]:
    def recurse(
        remaining: tuple[_CensusOccurrence, ...],
        field_position: int,
        assignment: tuple[tuple[str, str], ...],
        sign: int,
    ) -> list[tuple[tuple[_CensusOccurrence, ...], tuple[tuple[str, str], ...], int]]:
        if field_position == len(external_fields):
            return [(remaining, assignment, sign)]
        result: list[tuple[tuple[_CensusOccurrence, ...], tuple[tuple[str, str], ...], int]] = []
        field_name = external_fields[field_position]
        for position, occurrence in enumerate(remaining):
            if occurrence.field_name != field_name:
                continue
            crossed = sum(item.parity for item in remaining[:position])
            local_sign = -1 if occurrence.parity and crossed % 2 else 1
            result.extend(
                recurse(
                    remaining[:position] + remaining[position + 1 :],
                    field_position + 1,
                    assignment + ((f"ext{field_position}:{field_name}", occurrence.occurrence_id),),
                    sign * local_sign,
                )
            )
        return result

    return tuple(recurse(occurrences, 0, (), 1))


def _matching_census_pairs(
    left: _CensusOccurrence,
    right: _CensusOccurrence,
    rules: Sequence[CensusContractionRule],
) -> tuple[CensusInternalPair, ...]:
    result: list[CensusInternalPair] = []
    for rule in rules:
        exact = left.field_name == rule.left_field and right.field_name == rule.right_field
        reverse = left.field_name == rule.right_field and right.field_name == rule.left_field
        if exact:
            result.append(CensusInternalPair(rule.rule_id, left.occurrence_id, right.occurrence_id))
        elif reverse:
            if rule.oriented:
                result.append(CensusInternalPair(rule.rule_id, right.occurrence_id, left.occurrence_id))
            elif rule.left_field != rule.right_field:
                result.append(CensusInternalPair(rule.rule_id, left.occurrence_id, right.occurrence_id))
    return tuple(result)


def _census_pairings(
    occurrences: tuple[_CensusOccurrence, ...],
    rules: Sequence[CensusContractionRule],
    allow_same_vertex: bool,
) -> tuple[tuple[tuple[CensusInternalPair, ...], int], ...]:
    if len(occurrences) % 2:
        return ()

    def recurse(
        remaining: tuple[_CensusOccurrence, ...],
    ) -> list[tuple[tuple[CensusInternalPair, ...], int]]:
        if not remaining:
            return [((), 1)]
        first = remaining[0]
        result: list[tuple[tuple[CensusInternalPair, ...], int]] = []
        for position in range(1, len(remaining)):
            partner = remaining[position]
            if not allow_same_vertex and first.vertex_id == partner.vertex_id:
                continue
            matches = _matching_census_pairs(first, partner, rules)
            if not matches:
                continue
            odd_crossings = 0
            if first.parity == partner.parity == 1:
                odd_crossings = sum(item.parity for item in remaining[1:position])
            sign = -1 if odd_crossings % 2 else 1
            reduced = remaining[1:position] + remaining[position + 1 :]
            for match in matches:
                for child_pairs, child_sign in recurse(reduced):
                    result.append(((match,) + child_pairs, sign * child_sign))
        return result

    return tuple(recurse(occurrences))


def _is_connected(
    vertex_ids: Sequence[str],
    pairs: Sequence[CensusInternalPair],
    occurrences: Sequence[_CensusOccurrence],
) -> bool:
    if not vertex_ids:
        return False
    occurrence_vertex = {item.occurrence_id: item.vertex_id for item in occurrences}
    # External occurrences are absent from ``occurrences``; every pair endpoint is present.
    adjacency = {vertex_id: set() for vertex_id in vertex_ids}
    for pair in pairs:
        left = occurrence_vertex[pair.left_occurrence]
        right = occurrence_vertex[pair.right_occurrence]
        adjacency[left].add(right)
        adjacency[right].add(left)
    visited = set()
    stack = [vertex_ids[0]]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        stack.extend(adjacency[vertex] - visited)
    return visited == set(vertex_ids)


__all__ = [
    "ActionMonomial",
    "CensusContractionRule",
    "CensusOverflow",
    "CompositeExpansionTerm",
    "CompositeKind",
    "DerivativeRequest",
    "DerivativeScope",
    "ExactCoefficient",
    "ExternalVertexSlot",
    "FieldOccurrence",
    "FunctionalDerivativeTerm",
    "GrammarStatus",
    "OrderedVertex",
    "SpinorContraction",
    "TopologyCandidate",
    "TopologyCensus",
    "TypedZeroMonomial",
    "VertexGrammarBundle",
    "build_project_vertex_grammar",
    "census_one_loop_candidates",
    "chiral_cubic_monomials",
    "connection_expansion",
    "field_strength_expansion",
    "fp_ghost_monomials",
    "fp_ghost_typed_zeros",
    "full_ordered_vertex",
    "gauge_kinetic_monomials",
    "matter_bridge_monomials",
    "ordered_functional_derivative",
    "prepotential_euler_insertion_terms",
]
