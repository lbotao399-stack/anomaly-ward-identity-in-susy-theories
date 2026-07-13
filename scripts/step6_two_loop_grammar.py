#!/usr/bin/env python3
"""Exact Step-6 pure-gauge Project grammar through total ``V`` degree six.

This is a proposal compiler.  It derives only composite and action ASTs from
the Project bridge, field-strength, insertion, and Euler recursions.  It does
not construct Wick graphs, loop integrands, or renormalized operator data.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from itertools import product
from math import comb, factorial
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/two-loop-grammar"
GENERATED_JSON = GENERATED_DIR / "project-two-loop-grammar.json"
GENERATED_MD = GENERATED_DIR / "project-two-loop-grammar.md"
AUDIT = ROOT / "audits/step6-two-loop-grammar-verification.json"

STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
EXTERNAL_PROJECTION_STATUS = "BLOCKED_MISSING_PROJECT_EXTERNAL_PROJECTION_CERTIFICATE"
MAX_COMPOSITE_DEGREE = 5
MAX_INSERTION_VALENCE = 6

SOURCE_PATHS = (
    "contracts/foundations/step-03a-gauge-chiral-action.md",
    "contracts/foundations/step-04c-n4-super-yang-mills.md",
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md",
)


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class QI:
    """One exact monomial in ``Q(i)`` times named commuting symbols."""

    rational: Fraction = Fraction(1)
    i_power: int = 0
    symbols: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        rational = Fraction(self.rational)
        i_power = self.i_power % 4
        if i_power == 2:
            rational = -rational
            i_power = 0
        elif i_power == 3:
            rational = -rational
            i_power = 1
        if any(not symbol for symbol in self.symbols):
            raise ValueError("empty normalization symbol")
        object.__setattr__(self, "rational", rational)
        object.__setattr__(self, "i_power", i_power)
        object.__setattr__(self, "symbols", tuple(sorted(self.symbols)))

    def __mul__(self, other: QI | Fraction | int) -> QI:
        if isinstance(other, (Fraction, int)):
            other = QI(Fraction(other))
        if not isinstance(other, QI):
            return NotImplemented
        return QI(
            self.rational * other.rational,
            self.i_power + other.i_power,
            self.symbols + other.symbols,
        )

    def __neg__(self) -> QI:
        return QI(-self.rational, self.i_power, self.symbols)

    def render(self) -> str:
        if self.rational == 0:
            return "0"
        magnitude = abs(self.rational)
        factors: list[str] = []
        if magnitude != 1 or not (self.i_power or self.symbols):
            factors.append(fraction_text(magnitude))
        if self.i_power:
            factors.append("i")
        factors.extend(self.symbols)
        body = "*".join(factors) if factors else "1"
        return f"-{body}" if self.rational < 0 else body

    def as_json(self) -> dict[str, object]:
        return {
            "field": "Q(i)",
            "rational": fraction_text(self.rational),
            "i_power_reduced": self.i_power,
            "symbols": list(self.symbols),
            "rendered": self.render(),
        }


def ast(op: str, *args: dict[str, object], **attrs: object) -> dict[str, object]:
    return {
        "op": op,
        "attrs": dict(sorted(attrs.items())),
        "args": list(args),
    }


def v_leaf(port_id: str) -> dict[str, object]:
    return ast(
        "V",
        port_id=port_id,
        field="Project_bridge_exponent",
        representation="adjoint",
        parity=0,
    )


def flat_d(index: str, argument: dict[str, object]) -> dict[str, object]:
    return ast(
        "FlatD",
        argument,
        index=index,
        parity=1,
        action="left",
        source_equation="3A.34",
    )


def flat_bar_d(index: str, argument: dict[str, object]) -> dict[str, object]:
    return ast(
        "FlatBarD",
        argument,
        index=index,
        parity=1,
        action="left",
        source_equation="3A.34a",
    )


def bar_d2(argument: dict[str, object]) -> dict[str, object]:
    return ast(
        "BarD2",
        argument,
        parity=0,
        ordered_word=["barD_dot_plus", "barD_dot_minus"],
        source_equation="3A.51",
    )


def d2(argument: dict[str, object]) -> dict[str, object]:
    return ast(
        "D2",
        argument,
        parity=0,
        ordered_word=["D_plus", "D_minus"],
        source_equation="3A.52",
    )


def bracket(
    left: dict[str, object],
    right: dict[str, object],
    *,
    output_color: str,
    contraction: str | None = None,
) -> dict[str, object]:
    attrs: dict[str, object] = {
        "output_color": output_color,
        "component_rule": "[Y,Z]^C=i*c[A,B,C]*Y^A*Z^B",
        "color_tensor": "c[A,B,C]",
    }
    if contraction is not None:
        attrs["contraction"] = contraction
    return ast("AdjointBracket", left, right, **attrs)


def prefix_ports(expression: dict[str, object], prefix: str) -> dict[str, object]:
    attrs = dict(expression["attrs"])
    if expression["op"] == "V":
        attrs["port_id"] = f"{prefix}.{attrs['port_id']}"
    return ast(
        str(expression["op"]),
        *(prefix_ports(argument, prefix) for argument in expression["args"]),
        **attrs,
    )


def nested_ad_v(
    degree: int,
    spinor: str,
    prefix: str,
    output_color: str,
    *,
    core_operator: str,
) -> dict[str, object]:
    if degree < 1:
        raise ValueError("BCH degree must be positive")
    core = v_leaf(f"{prefix}.v{degree}")
    if core_operator == "D":
        expression = flat_d(spinor, core)
    elif core_operator == "barD":
        expression = flat_bar_d(spinor, core)
    else:
        raise ValueError("core operator must be D or barD")
    for position in range(degree - 1, 0, -1):
        expression = bracket(
            v_leaf(f"{prefix}.v{position}"),
            expression,
            output_color=f"{output_color}.ad{position}",
        )
    return ast("FreeColor", expression, color=output_color)


def collect_ports(expression: dict[str, object]) -> tuple[dict[str, object], ...]:
    ports: list[dict[str, object]] = []

    def visit(current: dict[str, object], word: tuple[str, ...], path: tuple[int, ...]) -> None:
        attrs = current["attrs"]
        op = current["op"]
        next_word = word
        if op == "FlatD":
            next_word = word + (f"D_{attrs['index']}",)
        elif op == "FlatBarD":
            next_word = word + (f"barD_{attrs['index']}",)
        elif op == "BarD2":
            next_word = word + ("barD^2",)
        elif op == "D2":
            next_word = word + ("D^2",)
        if op == "V":
            ports.append(
                {
                    "port_id": str(attrs["port_id"]),
                    "field": "V",
                    "representation": "adjoint",
                    "parity": 0,
                    "ast_path": list(path),
                    "derivative_word_outer_to_inner": list(next_word),
                }
            )
        for position, argument in enumerate(current["args"]):
            visit(argument, next_word, path + (position,))

    visit(expression, (), ())
    ids = [str(port["port_id"]) for port in ports]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate ordered V port")
    return tuple(ports)


def collect_color_ast(expression: dict[str, object]) -> tuple[dict[str, object], ...]:
    nodes: list[dict[str, object]] = []

    def visit(current: dict[str, object], path: tuple[int, ...]) -> None:
        if current["op"] in {
            "AdjointBracket",
            "GaugeInvariantPairing",
            "EulerKappaPairing",
            "FreeColor",
        }:
            nodes.append(
                {
                    "path": list(path),
                    "op": current["op"],
                    "attrs": current["attrs"],
                }
            )
        for position, argument in enumerate(current["args"]):
            visit(argument, path + (position,))

    visit(expression, ())
    return tuple(nodes)


@dataclass(frozen=True)
class Term:
    term_id: str
    family: str
    total_v_degree: int
    parity: int
    measure: str
    coefficient: QI
    expression: dict[str, object]
    source_equations: tuple[str, ...]
    derivation: str
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.total_v_degree < 0:
            raise ValueError("negative V degree")
        if self.parity not in (0, 1):
            raise ValueError("parity is Z/2 valued")
        if not self.source_equations:
            raise ValueError("missing equation provenance")
        ports = collect_ports(self.expression)
        if len(ports) != self.total_v_degree:
            raise ValueError(
                f"{self.term_id}: V degree {self.total_v_degree} but {len(ports)} ports"
            )

    def as_json(self) -> dict[str, object]:
        ports = collect_ports(self.expression)
        return {
            "status": STATUS,
            "term_id": self.term_id,
            "family": self.family,
            "degree": {
                "total_v": self.total_v_degree,
                "background_v": None,
                "quantum_v": None,
                "split_status": "UNASSIGNED",
            },
            "parity": self.parity,
            "measure": self.measure,
            "coefficient": self.coefficient.as_json(),
            "ports": list(ports),
            "color_ast": list(collect_color_ast(self.expression)),
            "expression_ast": self.expression,
            "source_equations": list(self.source_equations),
            "derivation": self.derivation,
            "tags": list(self.tags),
        }


def gamma_coefficient(degree: int) -> QI:
    if degree < 1:
        raise ValueError("Gamma degree must be positive")
    return QI(Fraction((-1) ** (degree - 1), factorial(degree)), degree - 1)


def tilde_gamma_coefficient(degree: int) -> QI:
    if degree < 1:
        raise ValueError("TildeGamma degree must be positive")
    return QI(Fraction(-1, factorial(degree)), degree - 1)


def gamma_terms(max_degree: int = MAX_COMPOSITE_DEGREE, *, spinor: str = "a") -> tuple[Term, ...]:
    return tuple(
        Term(
            term_id=f"Gamma_{degree}",
            family="Gamma",
            total_v_degree=degree,
            parity=1,
            measure="LOCAL_SUPERFIELD",
            coefficient=gamma_coefficient(degree),
            expression=nested_ad_v(
                degree,
                spinor,
                f"Gamma_{degree}",
                "C",
                core_operator="D",
            ),
            source_equations=("3A.34", "5.53n"),
            derivation="degree-n coefficient of exp(-V) D_a exp(V)",
            tags=("BCH_DERIVED", "COMPONENT_COLOR_BRACKETS"),
        )
        for degree in range(1, max_degree + 1)
    )


def w_terms(max_degree: int = MAX_COMPOSITE_DEGREE, *, spinor: str = "a") -> tuple[Term, ...]:
    result: list[Term] = []
    for gamma in gamma_terms(max_degree, spinor=spinor):
        result.append(
            Term(
                term_id=f"W_{gamma.total_v_degree}",
                family="W",
                total_v_degree=gamma.total_v_degree,
                parity=1,
                measure="LOCAL_CHIRAL_SUPERFIELD",
                coefficient=QI(Fraction(-1, 8)) * gamma.coefficient,
                expression=bar_d2(prefix_ports(gamma.expression, f"W_{gamma.total_v_degree}")),
                source_equations=("3A.34", "3A.51", "5.53n"),
                derivation="W_(n)=-1/8 barD^2 Gamma_(n)",
                tags=("PROJECT_FIELD_STRENGTH", "BCH_DERIVED"),
            )
        )
    return tuple(result)


def tilde_gamma_terms(
    max_degree: int = MAX_COMPOSITE_DEGREE,
    *,
    spinor: str = "dot_a",
) -> tuple[Term, ...]:
    return tuple(
        Term(
            term_id=f"TildeGamma_{degree}",
            family="TildeGamma",
            total_v_degree=degree,
            parity=1,
            measure="LOCAL_SUPERFIELD",
            coefficient=tilde_gamma_coefficient(degree),
            expression=nested_ad_v(
                degree,
                spinor,
                f"TildeGamma_{degree}",
                "C",
                core_operator="barD",
            ),
            source_equations=("3A.34a",),
            derivation="degree-n coefficient of exp(V) barD_dot_a exp(-V)",
            tags=("BCH_DERIVED", "INDEPENDENT_EUCLIDEAN_TILDED_SECTOR"),
        )
        for degree in range(1, max_degree + 1)
    )


def tilde_w_terms(
    max_degree: int = MAX_COMPOSITE_DEGREE,
    *,
    spinor: str = "dot_a",
) -> tuple[Term, ...]:
    result: list[Term] = []
    for gamma in tilde_gamma_terms(max_degree, spinor=spinor):
        result.append(
            Term(
                term_id=f"TildeW_{gamma.total_v_degree}",
                family="TildeW",
                total_v_degree=gamma.total_v_degree,
                parity=1,
                measure="LOCAL_ANTICHIRAL_SUPERFIELD",
                coefficient=QI(Fraction(1, 8)) * gamma.coefficient,
                expression=d2(prefix_ports(gamma.expression, f"TildeW_{gamma.total_v_degree}")),
                source_equations=("3A.34a", "3A.52"),
                derivation="TildeW_(n)=+1/8 D^2 TildeGamma_(n)",
                tags=("PROJECT_TILDE_FIELD_STRENGTH", "INDEPENDENT_EUCLIDEAN_TILDED_SECTOR"),
            )
        )
    return tuple(result)


def covariant_w_terms_at_degree(
    degree: int,
    *,
    prefix: str,
    derivative_spinor: str,
    w_spinor: str,
    free_color: str,
    overall: QI = QI(1),
    family: str = "X",
) -> tuple[Term, ...]:
    if degree < 1 or degree > MAX_COMPOSITE_DEGREE:
        raise ValueError("covariant W derivative is compiled through V degree five")
    strengths = w_terms(degree, spinor=w_spinor)
    connections = gamma_terms(degree, spinor=derivative_spinor)
    linear = strengths[degree - 1]
    result = [
        Term(
            term_id=f"{prefix}_{degree}_flat",
            family=family,
            total_v_degree=degree,
            parity=0,
            measure="LOCAL_CHIRAL_SUPERFIELD",
            coefficient=overall * linear.coefficient,
            expression=ast(
                "FreeColor",
                flat_d(
                    derivative_spinor,
                    prefix_ports(linear.expression, f"{prefix}.{degree}.flat"),
                ),
                color=free_color,
            ),
            source_equations=("3A.34", "3A.51", "5.53n"),
            derivation=f"D_{derivative_spinor} W_({degree})_{w_spinor}",
            tags=("FLAT_DERIVATIVE",),
        )
    ]
    for gamma_degree in range(1, degree):
        w_degree = degree - gamma_degree
        gamma = connections[gamma_degree - 1]
        strength = strengths[w_degree - 1]
        result.append(
            Term(
                term_id=f"{prefix}_{degree}_connection_{gamma_degree}_{w_degree}",
                family=family,
                total_v_degree=degree,
                parity=0,
                measure="LOCAL_CHIRAL_SUPERFIELD",
                coefficient=overall * gamma.coefficient * strength.coefficient * QI(1, 1),
                expression=ast(
                    "FreeColor",
                    bracket(
                        prefix_ports(
                            gamma.expression,
                            f"{prefix}.{degree}.connection.{gamma_degree}.{w_degree}.Gamma",
                        ),
                        prefix_ports(
                            strength.expression,
                            f"{prefix}.{degree}.connection.{gamma_degree}.{w_degree}.W",
                        ),
                        output_color=free_color,
                        contraction=f"{derivative_spinor} with {w_spinor}",
                    ),
                    color=free_color,
                ),
                source_equations=("3A.34", "3A.51", "5.53n"),
                derivation=f"[Gamma_({gamma_degree})_{derivative_spinor},W_({w_degree})_{w_spinor}]",
                tags=("COVARIANT_CONNECTION", "NONLINEAR_LETTER"),
            )
        )
    return tuple(result)


def x_terms_at_degree(
    degree: int,
    *,
    prefix: str = "X",
    free_color: str = "C",
) -> tuple[Term, ...]:
    return covariant_w_terms_at_degree(
        degree,
        prefix=prefix,
        derivative_spinor="+",
        w_spinor="+",
        free_color=free_color,
        family="X",
    )


def x_terms(max_degree: int = MAX_COMPOSITE_DEGREE) -> tuple[Term, ...]:
    return tuple(
        term
        for degree in range(1, max_degree + 1)
        for term in x_terms_at_degree(degree)
    )


def insertion_terms_at_valence(valence: int) -> tuple[Term, ...]:
    if valence < 2 or valence > MAX_INSERTION_VALENCE:
        raise ValueError("insertion valence must be in 2,...,6")
    result: list[Term] = []
    serial = 0
    for left_degree in range(1, valence):
        right_degree = valence - left_degree
        if left_degree > MAX_COMPOSITE_DEGREE or right_degree > MAX_COMPOSITE_DEGREE:
            continue
        left_terms = x_terms_at_degree(left_degree, prefix=f"I{valence}.L", free_color="A")
        right_terms = x_terms_at_degree(right_degree, prefix=f"I{valence}.R", free_color="B")
        for left in left_terms:
            for right in right_terms:
                for placement in ("LEFT", "RIGHT"):
                    serial += 1
                    left_body = left.expression
                    right_body = right.expression
                    if placement == "LEFT":
                        left_body = flat_d("-", left_body)
                    else:
                        right_body = flat_d("-", right_body)
                    result.append(
                        Term(
                            term_id=f"I{valence}_direct_{serial:03d}",
                            family=f"I{valence}",
                            total_v_degree=valence,
                            parity=1,
                            measure="LOCAL_OPERATOR_INSERTION",
                            coefficient=left.coefficient * right.coefficient,
                            expression=ast(
                                "OrderedProduct",
                                left_body,
                                right_body,
                                factor_order=["A", "B"],
                                graded_leibniz_sign=1,
                            ),
                            source_equations=("5.53n", "5.53p"),
                            derivation=f"D_- acts on {placement} factor of X^A X^B",
                            tags=(
                                "DIRECT_D_MINUS",
                                f"D_MINUS_{placement}",
                                "ORDERED_AB",
                            ),
                        )
                    )
    for gamma_degree in range(1, valence - 1):
        remaining = valence - gamma_degree
        if gamma_degree > MAX_COMPOSITE_DEGREE:
            continue
        gamma = gamma_terms(gamma_degree, spinor="-")[gamma_degree - 1]
        for left_degree in range(1, remaining):
            right_degree = remaining - left_degree
            if left_degree > MAX_COMPOSITE_DEGREE or right_degree > MAX_COMPOSITE_DEGREE:
                continue
            left_terms = x_terms_at_degree(left_degree, prefix=f"I{valence}.L", free_color="L")
            right_terms = x_terms_at_degree(right_degree, prefix=f"I{valence}.R", free_color="R")
            for left in left_terms:
                for right in right_terms:
                    for placement in ("LEFT", "RIGHT"):
                        serial += 1
                        gamma_body = prefix_ports(
                            gamma.expression,
                            f"I{valence}.outer.{serial}.Gamma",
                        )
                        if placement == "LEFT":
                            left_body = ast(
                                "FreeColor",
                                bracket(gamma_body, left.expression, output_color="A"),
                                color="A",
                            )
                            right_body = ast("FreeColor", right.expression, color="B")
                        else:
                            left_body = ast("FreeColor", left.expression, color="A")
                            right_body = ast(
                                "FreeColor",
                                bracket(gamma_body, right.expression, output_color="B"),
                                color="B",
                            )
                        result.append(
                            Term(
                                term_id=f"I{valence}_outer_connection_{serial:03d}",
                                family=f"I{valence}",
                                total_v_degree=valence,
                                parity=1,
                                measure="LOCAL_OPERATOR_INSERTION",
                                coefficient=gamma.coefficient
                                * left.coefficient
                                * right.coefficient
                                * QI(1, 1),
                                expression=ast(
                                    "OrderedProduct",
                                    left_body,
                                    right_body,
                                    factor_order=["A", "B"],
                                    graded_leibniz_sign=1,
                                ),
                                source_equations=("3A.34", "5.53n", "5.53p"),
                                derivation=f"outer Gamma_({gamma_degree})_- connection on {placement} color factor",
                                tags=(
                                    "OUTER_NABLA_MINUS_CONNECTION",
                                    f"OUTER_CONNECTION_{placement}",
                                    "ORDERED_AB",
                                ),
                            )
                        )
    return tuple(result)


def insertion_terms() -> dict[int, tuple[Term, ...]]:
    return {
        valence: insertion_terms_at_valence(valence)
        for valence in range(2, MAX_INSERTION_VALENCE + 1)
    }


def action_terms_at_valence(valence: int, sector: str) -> tuple[Term, ...]:
    if valence < 3 or valence > 6:
        raise ValueError("action valence must be in 3,...,6")
    if sector == "PLUS":
        strengths = w_terms(valence - 1, spinor="a")
        measure = "E_PLUS_CHIRAL"
        family = f"S{valence}_PLUS"
        source_strength = "W"
        raise_rule = "W^a=epsilon^{ab}W_b"
        sector_tag = "CHIRAL_EUCLIDEAN_SECTOR"
    elif sector == "MINUS":
        strengths = tilde_w_terms(valence - 1, spinor="dot_a")
        measure = "E_MINUS_ANTICHIRAL"
        family = f"S{valence}_MINUS"
        source_strength = "TildeW"
        raise_rule = "TildeW^dot_a=epsilon^{dot_a dot_b}TildeW_dot_b"
        sector_tag = "ANTICHIRAL_EUCLIDEAN_SECTOR"
    else:
        raise ValueError("sector must be PLUS or MINUS")
    result: list[Term] = []
    for left_degree in range(1, valence):
        right_degree = valence - left_degree
        left = strengths[left_degree - 1]
        right = strengths[right_degree - 1]
        result.append(
            Term(
                term_id=f"{family}_{left_degree}_{right_degree}",
                family=family,
                total_v_degree=valence,
                parity=0,
                measure=measure,
                coefficient=QI(Fraction(-1, 4), symbols=("h",))
                * left.coefficient
                * right.coefficient,
                expression=ast(
                    "GaugeInvariantPairing",
                    ast(
                        "SpinorRaise",
                        prefix_ports(left.expression, f"{family}.{left_degree}.{right_degree}.L"),
                        rule=raise_rule,
                    ),
                    prefix_ports(right.expression, f"{family}.{left_degree}.{right_degree}.R"),
                    color_pairing="kappa[A,B]",
                    ordered_factors=["left_raised", "right_lowered"],
                    measure=measure,
                ),
                source_equations=(
                    "3A.51" if sector == "PLUS" else "3A.52",
                    "4C.4",
                    "5.16",
                    "5.53n",
                ),
                derivation=f"-h/4 {source_strength}_({left_degree}) {source_strength}_({right_degree})",
                tags=("PURE_GAUGE_ACTION", "ORDERED_SPLIT", sector_tag),
            )
        )
    return tuple(result)


def action_terms() -> dict[str, tuple[Term, ...]]:
    return {
        f"S{valence}_{sector}": action_terms_at_valence(valence, sector)
        for valence in range(3, 7)
        for sector in ("PLUS", "MINUS")
    }


def e_xi_gauge_terms(max_degree: int = MAX_COMPOSITE_DEGREE) -> tuple[Term, ...]:
    result: list[Term] = []
    serial = 0
    for degree in range(1, max_degree + 1):
        divergence = (
            covariant_w_terms_at_degree(
                degree,
                prefix="E_Xi.minus_plus",
                derivative_spinor="-",
                w_spinor="+",
                free_color="B",
                family="NABLA_W_DIVERGENCE",
            )
            + covariant_w_terms_at_degree(
                degree,
                prefix="E_Xi.plus_minus",
                derivative_spinor="+",
                w_spinor="-",
                free_color="B",
                overall=QI(-1),
                family="NABLA_W_DIVERGENCE",
            )
        )
        for core in divergence:
            serial += 1
            result.append(
                Term(
                    term_id=f"E_Xi_gauge_{degree}_{serial:03d}",
                    family="E_Xi_GAUGE",
                    total_v_degree=degree,
                    parity=0,
                    measure="FULL_E8_EULER_DENSITY",
                    coefficient=QI(Fraction(1, 2), symbols=("h", "kappa[A,B]"))
                    * core.coefficient,
                    expression=ast(
                        "EulerKappaPairing",
                        core.expression,
                        free_color="A",
                        core_color="B",
                        color_pairing="kappa[A,B]",
                        divergence_identity="nabla^a W_a=nabla_- W_+-nabla_+ W_-",
                    ),
                    source_equations=("5.23d", "5.26", "5.53n"),
                    derivation=f"h*kappa[A,B]/2 times {core.derivation}",
                    tags=("PURE_GAUGE_EULER_CORE",),
                )
            )
    return tuple(result)


def e_v_project_terms(max_total_degree: int = MAX_COMPOSITE_DEGREE) -> tuple[Term, ...]:
    result: list[Term] = []
    for core in e_xi_gauge_terms(max_total_degree):
        for ad_degree in range(0, max_total_degree - core.total_v_degree + 1):
            expression = core.expression
            for position in range(ad_degree, 0, -1):
                expression = bracket(
                    v_leaf(f"E_V.{core.term_id}.ad{position}"),
                    expression,
                    output_color=f"E_V.{core.term_id}.C{position}",
                )
            result.append(
                Term(
                    term_id=f"E_V_project__{core.term_id}__ad_{ad_degree}",
                    family="E_V_PROJECT_FUNCTIONAL",
                    total_v_degree=core.total_v_degree + ad_degree,
                    parity=0,
                    measure="FULL_E8_FUNCTIONAL_EULER_DENSITY",
                    coefficient=core.coefficient
                    * QI(Fraction(1, factorial(ad_degree + 1)), ad_degree),
                    expression=ast("FreeColor", expression, color="A"),
                    source_equations=core.source_equations + ("5.28a-5.28d", "5.28"),
                    derivation=f"1/{ad_degree + 1}! ad_V^{ad_degree}({core.term_id})",
                    tags=(
                        "PROJECT_FUNCTIONAL_EULER_TRANSPORT",
                        f"AD_DEGREE_{ad_degree}",
                    ),
                )
            )
    return tuple(result)


class ExternalProjectionBlocked(RuntimeError):
    pass


def background_quantum_assignments(term: Term) -> tuple[dict[str, object], ...]:
    """Enumerate ordered ``V=B+v`` assignments without external projection."""

    ports = collect_ports(term.expression)
    assignments: list[dict[str, object]] = []
    for serial, roles in enumerate(
        product(("BACKGROUND_UNPROJECTED", "QUANTUM_WICK"), repeat=len(ports)),
        start=1,
    ):
        background_degree = roles.count("BACKGROUND_UNPROJECTED")
        quantum_degree = roles.count("QUANTUM_WICK")
        assignments.append(
            {
                "status": STATUS,
                "assignment_id": f"{term.term_id}__BQ_{serial:03d}",
                "source_term_id": term.term_id,
                "degree": {
                    "total_v": term.total_v_degree,
                    "background_v": background_degree,
                    "quantum_v": quantum_degree,
                    "identity_check": term.total_v_degree
                    == background_degree + quantum_degree,
                },
                "ordered_ports": [
                    {
                        **port,
                        "role": role,
                        "substituted_field": "V_BACKGROUND_UNPROJECTED"
                        if role == "BACKGROUND_UNPROJECTED"
                        else "v_QUANTUM_WICK",
                    }
                    for port, role in zip(ports, roles, strict=True)
                ],
                "coefficient": term.coefficient.as_json(),
                "coefficient_changed_by_split": False,
                "external_projection": EXTERNAL_PROJECTION_STATUS,
            }
        )
    return tuple(assignments)


def project_external_assignment(
    assignment: dict[str, object],
    targets: Sequence[str],
) -> dict[str, object]:
    del assignment, targets
    raise ExternalProjectionBlocked(EXTERNAL_PROJECTION_STATUS)


def assignment_census(terms: Sequence[Term]) -> dict[str, object]:
    by_degree: dict[str, dict[str, int]] = {}
    total = 0
    for term in terms:
        degree = term.total_v_degree
        total += 2**degree
        degree_key = str(degree)
        if degree_key not in by_degree:
            by_degree[degree_key] = {
                "terms": 0,
                "ordered_assignments": 0,
            }
        by_degree[degree_key]["terms"] += 1
        by_degree[degree_key]["ordered_assignments"] += 2**degree
    bq_distribution: dict[str, int] = {}
    for degree_key, data in by_degree.items():
        degree = int(degree_key)
        term_count = data["terms"]
        for background_degree in range(degree + 1):
            quantum_degree = degree - background_degree
            key = f"t{degree}_b{background_degree}_q{quantum_degree}"
            bq_distribution[key] = term_count * comb(degree, background_degree)
    return {
        "status": STATUS,
        "total_ordered_assignments": total,
        "by_total_v_degree": by_degree,
        "by_total_background_quantum_degree": bq_distribution,
        "external_projection": EXTERNAL_PROJECTION_STATUS,
    }


def derived_insertion_count(valence: int) -> dict[str, int]:
    x_counts = {
        degree: len(x_terms_at_degree(degree))
        for degree in range(1, min(valence, MAX_COMPOSITE_DEGREE + 1))
    }
    direct = 2 * sum(
        x_counts[left] * x_counts[valence - left]
        for left in range(1, valence)
        if left in x_counts and valence - left in x_counts
    )
    connection = 2 * sum(
        x_counts[left] * x_counts[valence - gamma_degree - left]
        for gamma_degree in range(1, valence - 1)
        if gamma_degree <= MAX_COMPOSITE_DEGREE
        for left in range(1, valence - gamma_degree)
        if left in x_counts and valence - gamma_degree - left in x_counts
    )
    return {
        "direct_D_minus": direct,
        "outer_Gamma_minus": connection,
        "total": direct + connection,
    }


def term_metadata_complete(term: Term) -> bool:
    payload = term.as_json()
    return bool(
        payload["term_id"]
        and payload["family"]
        and payload["source_equations"]
        and payload["measure"]
        and payload["color_ast"]
        and len(payload["ports"]) == term.total_v_degree
        and payload["coefficient"]["field"] == "Q(i)"
    )


def source_contracts() -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for relative in SOURCE_PATHS:
        data = (ROOT / relative).read_bytes()
        result.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    return result


def flatten_term_groups(groups: Iterable[Sequence[Term]]) -> tuple[Term, ...]:
    return tuple(term for group in groups for term in group)


def build_payload() -> dict[str, object]:
    gamma = gamma_terms()
    w = w_terms()
    tilde_gamma = tilde_gamma_terms()
    tilde_w = tilde_w_terms()
    x = x_terms()
    insertions = insertion_terms()
    actions = action_terms()
    e_xi = e_xi_gauge_terms()
    e_v = e_v_project_terms()
    insertion_all = flatten_term_groups(insertions.values())
    action_all = flatten_term_groups(actions.values())
    all_terms = gamma + w + tilde_gamma + tilde_w + x + insertion_all + action_all + e_xi + e_v
    insertion_derivation = {
        f"I{valence}": derived_insertion_count(valence)
        for valence in range(2, MAX_INSERTION_VALENCE + 1)
    }
    e_xi_by_degree = {
        str(degree): sum(term.total_v_degree == degree for term in e_xi)
        for degree in range(1, MAX_COMPOSITE_DEGREE + 1)
    }
    e_v_by_degree = {
        str(degree): sum(term.total_v_degree == degree for term in e_v)
        for degree in range(1, MAX_COMPOSITE_DEGREE + 1)
    }
    return {
        "schema": 1,
        "status": STATUS,
        "scope": "STEP6_PURE_GAUGE_PROJECT_COMPOSITE_AND_ACTION_GRAMMAR",
        "source_contracts": source_contracts(),
        "normalization": {
            "bridge": "E=exp(V)",
            "generator_commutator": "[T_A,T_B]=i*c[A,B,C]*T_C",
            "Gamma": "exp(-V) D_a exp(V)",
            "W": "-1/8 barD^2 Gamma",
            "TildeGamma": "exp(V) barD_dot_a exp(-V)",
            "TildeW": "+1/8 D^2 TildeGamma",
            "X": "D_+ W_+ + [Gamma_+,W_+]",
            "insertion": "nabla_-[X^A X^B]",
            "gauge_action": "-h/4 times ordered same-sector field-strength pairing",
            "E_Xi_gauge": "h*kappa[A,B]/2*nabla^a W_a^B",
            "E_V_project": "sum_(r>=0) ad_V^r(E_Xi)/(r+1)!",
        },
        "recursion_bounds": {
            "Gamma_W_TildeGamma_TildeW_X_max_total_v": MAX_COMPOSITE_DEGREE,
            "I_min_max_total_v": [2, MAX_INSERTION_VALENCE],
            "S_min_max_total_v": [3, 6],
            "E_Xi_E_V_max_total_v": MAX_COMPOSITE_DEGREE,
        },
        "coefficient_tables": {
            "Gamma": [term.coefficient.as_json() for term in gamma],
            "W": [term.coefficient.as_json() for term in w],
            "TildeGamma": [term.coefficient.as_json() for term in tilde_gamma],
            "TildeW": [term.coefficient.as_json() for term in tilde_w],
            "X_by_degree": {
                str(degree): [
                    term.coefficient.as_json()
                    for term in x_terms_at_degree(degree)
                ]
                for degree in range(1, 6)
            },
            "X_term_counts_by_degree": [len(x_terms_at_degree(degree)) for degree in range(1, 6)],
        },
        "composites": {
            "Gamma": [term.as_json() for term in gamma],
            "W": [term.as_json() for term in w],
            "TildeGamma": [term.as_json() for term in tilde_gamma],
            "TildeW": [term.as_json() for term in tilde_w],
            "X": [term.as_json() for term in x],
        },
        "insertions": {
            f"I{valence}": [term.as_json() for term in terms]
            for valence, terms in insertions.items()
        },
        "gauge_action_vertices": {
            name: [term.as_json() for term in terms]
            for name, terms in actions.items()
        },
        "euler": {
            "E_Xi_gauge": [term.as_json() for term in e_xi],
            "E_V_project_functional": [term.as_json() for term in e_v],
        },
        "term_count_derivation": {
            "X": {
                "identity": "|X_(n)|=1+sum_(r=1)^(n-1)1=n",
                "by_degree": {
                    str(degree): len(x_terms_at_degree(degree))
                    for degree in range(1, 6)
                },
            },
            "I": insertion_derivation,
            "E_Xi_gauge": {
                "identity": "sum_(n=1)^5 2|X_(n)|",
                "by_degree": e_xi_by_degree,
                "total": len(e_xi),
            },
            "E_V_project_functional": {
                "identity": "sum_(d=1)^5 |E_Xi_(d)|(6-d)",
                "by_total_degree": e_v_by_degree,
                "total": len(e_v),
            },
            "gauge_action": {
                name: {
                    "ordered_splits": len(terms),
                    "identity": f"{name}: left_degree=1,...,{terms[0].total_v_degree - 1}",
                }
                for name, terms in actions.items()
            },
        },
        "background_quantum_assignment_generator": {
            "roles": ["BACKGROUND_UNPROJECTED", "QUANTUM_WICK"],
            "degree_identity": "total_v=background_v+quantum_v",
            "external_projection": EXTERNAL_PROJECTION_STATUS,
            "census": {
                "insertions": assignment_census(insertion_all),
                "gauge_action_vertices": assignment_census(action_all),
                "E_Xi_gauge": assignment_census(e_xi),
                "E_V_project_functional": assignment_census(e_v),
            },
            "representative_assignments": {
                "Gamma_5": list(background_quantum_assignments(gamma[-1])),
                "I6_first": list(background_quantum_assignments(insertions[6][0])),
                "S6_PLUS_first": list(background_quantum_assignments(actions["S6_PLUS"][0])),
                "E_V_degree5_first": list(
                    background_quantum_assignments(
                        next(term for term in e_v if term.total_v_degree == 5)
                    )
                ),
            },
        },
        "all_terms_metadata_complete": all(term_metadata_complete(term) for term in all_terms),
        "result_products": [],
    }


def exact_checks(payload: dict[str, object]) -> dict[str, bool]:
    gamma = gamma_terms()
    w = w_terms()
    tilde_gamma = tilde_gamma_terms()
    tilde_w = tilde_w_terms()
    insertions = insertion_terms()
    actions = action_terms()
    e_xi = e_xi_gauge_terms()
    e_v = e_v_project_terms()
    all_terms = (
        gamma
        + w
        + tilde_gamma
        + tilde_w
        + x_terms()
        + flatten_term_groups(insertions.values())
        + flatten_term_groups(actions.values())
        + e_xi
        + e_v
    )
    insertion_actual = tuple(len(insertions[n]) for n in range(2, 7))
    insertion_derived = tuple(derived_insertion_count(n)["total"] for n in range(2, 7))
    e_xi_derived = sum(2 * len(x_terms_at_degree(n)) for n in range(1, 6))
    e_v_derived = sum(
        sum(term.total_v_degree == degree for term in e_xi) * (6 - degree)
        for degree in range(1, 6)
    )
    try:
        project_external_assignment(background_quantum_assignments(gamma[0])[0], ("X",))
    except ExternalProjectionBlocked as exc:
        external_projection_fail_closed = str(exc) == EXTERNAL_PROJECTION_STATUS
    else:
        external_projection_fail_closed = False
    representative_assignments = background_quantum_assignments(insertions[6][0])
    return {
        "status_is_proposal_only": payload["status"] == STATUS
        and all(term.as_json()["status"] == STATUS for term in all_terms),
        "gamma_coefficients_follow_BCH_formula": all(
            term.coefficient == QI(Fraction((-1) ** (n - 1), factorial(n)), n - 1)
            for n, term in enumerate(gamma, start=1)
        ),
        "w_coefficients_are_minus_one_eighth_gamma": all(
            strength.coefficient == QI(Fraction(-1, 8)) * connection.coefficient
            for strength, connection in zip(w, gamma, strict=True)
        ),
        "tilde_gamma_coefficients_follow_BCH_formula": all(
            term.coefficient == QI(Fraction(-1, factorial(n)), n - 1)
            for n, term in enumerate(tilde_gamma, start=1)
        ),
        "tilde_w_coefficients_are_plus_one_eighth_tilde_gamma": all(
            strength.coefficient == QI(Fraction(1, 8)) * connection.coefficient
            for strength, connection in zip(tilde_w, tilde_gamma, strict=True)
        ),
        "x_counts_derived_from_covariant_recursion": all(
            len(x_terms_at_degree(n)) == 1 + sum(1 for _ in range(1, n))
            for n in range(1, 6)
        ),
        "x_coefficients_follow_covariant_recursion": all(
            [term.coefficient for term in x_terms_at_degree(n)]
            == [w[n - 1].coefficient]
            + [
                gamma[r - 1].coefficient * w[n - r - 1].coefficient * QI(1, 1)
                for r in range(1, n)
            ]
            for n in range(1, 6)
        ),
        "insertion_counts_equal_composition_derivation": insertion_actual == insertion_derived,
        "insertion_counts_are_2_10_30_70_140": insertion_derived == (2, 10, 30, 70, 140),
        "both_D_minus_placements_in_every_I": all(
            {
                tag
                for term in insertions[n]
                for tag in term.tags
                if tag in {"D_MINUS_LEFT", "D_MINUS_RIGHT"}
            }
            == {"D_MINUS_LEFT", "D_MINUS_RIGHT"}
            for n in range(2, 7)
        ),
        "outer_Gamma_minus_present_I3_through_I6": all(
            any("OUTER_NABLA_MINUS_CONNECTION" in term.tags for term in insertions[n])
            for n in range(3, 7)
        ),
        "action_ordered_splits_complete": all(
            len(actions[f"S{n}_{sector}"]) == n - 1
            for n in range(3, 7)
            for sector in ("PLUS", "MINUS")
        ),
        "action_measures_parallel": all(
            all(term.measure == "E_PLUS_CHIRAL" for term in actions[f"S{n}_PLUS"])
            and all(term.measure == "E_MINUS_ANTICHIRAL" for term in actions[f"S{n}_MINUS"])
            for n in range(3, 7)
        ),
        "E_Xi_count_equals_recursion_derivation": len(e_xi) == e_xi_derived,
        "E_Xi_count_is_30": e_xi_derived == 30,
        "E_V_count_equals_transport_derivation": len(e_v) == e_v_derived,
        "E_V_count_is_70": e_v_derived == 70,
        "E_V_uses_project_positive_factorial_transport": all(
            "PROJECT_FUNCTIONAL_EULER_TRANSPORT" in term.tags for term in e_v
        ),
        "term_port_parity_measure_color_provenance_complete": all(
            term_metadata_complete(term) for term in all_terms
        ),
        "background_quantum_degrees_are_separate_and_exact": len(representative_assignments)
        == 2 ** insertions[6][0].total_v_degree
        and all(
            row["degree"]["identity_check"]
            and row["degree"]["total_v"]
            == row["degree"]["background_v"] + row["degree"]["quantum_v"]
            for row in representative_assignments
        ),
        "external_projection_fails_closed": external_projection_fail_closed,
        "source_hashes_present": all(
            len(item["sha256"]) == 64 for item in payload["source_contracts"]
        ),
        "result_products_empty": payload["result_products"] == [],
    }


def render_markdown(payload: dict[str, object], checks: dict[str, bool]) -> str:
    tables = payload["coefficient_tables"]
    gamma = [item["rendered"] for item in tables["Gamma"]]
    w = [item["rendered"] for item in tables["W"]]
    tilde_gamma = [item["rendered"] for item in tables["TildeGamma"]]
    tilde_w = [item["rendered"] for item in tables["TildeW"]]
    x_coefficients = {
        degree: [item["rendered"] for item in tables["X_by_degree"][str(degree)]]
        for degree in range(1, 6)
    }
    i_counts = [payload["term_count_derivation"]["I"][f"I{n}"]["total"] for n in range(2, 7)]
    lines = [
        "# Step 6 — pure-gauge Project grammar",
        "",
        f"`{STATUS}`",
        "",
        "$$",
        r"\Gamma_{(n)a}=\frac{(-1)^{n-1}}{n!}\operatorname{ad}_{V}^{n-1}(D_aV),",
        r"\qquad W_{(n)a}=-\frac18\bar D^2\Gamma_{(n)a},",
        "$$",
        "",
        "$$",
        r"\widetilde\Gamma_{(n)\dot a}=-\frac1{n!}\operatorname{ad}_{V}^{n-1}(\bar D_{\dot a}V),",
        r"\qquad \widetilde W_{(n)\dot a}=\frac18D^2\widetilde\Gamma_{(n)\dot a}.",
        "$$",
        "",
        "| $n$ | 1 | 2 | 3 | 4 | 5 |",
        "|---:|---:|---:|---:|---:|---:|",
        "| $\\Gamma_{(n)}$ | " + " | ".join(gamma) + " |",
        "| $W_{(n)}$ | " + " | ".join(w) + " |",
        "| $\\widetilde\\Gamma_{(n)}$ | " + " | ".join(tilde_gamma) + " |",
        "| $\\widetilde W_{(n)}$ | " + " | ".join(tilde_w) + " |",
        "",
        "$$",
        r"X_{(n)}=D_+W_{(n)+}+\sum_{r=1}^{n-1}[\Gamma_{(r)+},W_{(n-r)+}],",
        r"\qquad |X_{(n)}|=n.",
        "$$",
        "",
        "| $n$ | exact ordered $X_{(n)}$ coefficients |",
        "|---:|:---|",
        *(
            f"| {degree} | " + ", ".join(x_coefficients[degree]) + " |"
            for degree in range(1, 6)
        ),
        "",
        "$$",
        r"|I_{(N)}|=2\sum_{r=1}^{N-1}|X_{(r)}||X_{(N-r)}|",
        r"+2\sum_{t=1}^{N-2}\sum_{r=1}^{N-t-1}|X_{(r)}||X_{(N-t-r)}|.",
        "$$",
        "",
        "| $N$ | 2 | 3 | 4 | 5 | 6 |",
        "|---:|---:|---:|---:|---:|---:|",
        "| $|I_{(N)}|$ | " + " | ".join(str(value) for value in i_counts) + " |",
        "",
        "$$",
        r"S_{(N)}^+=-\frac h4\sum_{r=1}^{N-1}\int_{E,+}\kappa_{AB}W_{(r)}^{Aa}W_{(N-r)a}^{B},",
        "$$",
        "",
        "$$",
        r"S_{(N)}^-=-\frac h4\sum_{r=1}^{N-1}\int_{E,-}\kappa_{AB}\widetilde W_{(r)\dot a}^{A}\widetilde W_{(N-r)}^{B\dot a},",
        r"\qquad N=3,4,5,6.",
        "$$",
        "",
        "$$",
        r"|E_{\Xi}^{\rm gauge}|=2\sum_{n=1}^{5}n=30,",
        r"\qquad |E_V|=\sum_{d=1}^{5}2d(6-d)=70.",
        "$$",
        "",
        "$$",
        r"V_j=(V_B)_j+v_j,\qquad t=b+q.",
        "$$",
        "",
        f"External projection: `{EXTERNAL_PROJECTION_STATUS}`.",
        "",
        f"Exact checks: `{sum(checks.values())}/{len(checks)}`.",
        "",
    ]
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, object], dict[str, object]]:
    payload = build_payload()
    checks = exact_checks(payload)
    failures = sorted(name for name, passed in checks.items() if not passed)
    audit = {
        "schema": 1,
        "status": STATUS,
        "generator": "scripts/step6_two_loop_grammar.py",
        "generated": [
            str(GENERATED_JSON.relative_to(ROOT)),
            str(GENERATED_MD.relative_to(ROOT)),
        ],
        "checks": checks,
        "passed": len(checks) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "source_contracts": payload["source_contracts"],
    }
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    GENERATED_MD.write_text(render_markdown(payload, checks))
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    return payload, audit


def main() -> int:
    _, audit = write_outputs()
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0 if audit["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
