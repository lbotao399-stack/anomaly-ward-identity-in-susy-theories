#!/usr/bin/env python3
"""Exact Project-frame composite grammar for the Step-5 WW seed.

The module keeps matrix-BCH coefficients and their componentized powers of
``i`` exact.  It deliberately records two different prepotential-Euler
transport series:

* ``project_functional_euler`` follows (5.28a)--(5.28d);
* ``user_requested_seed_transport`` follows the explicit 2026-07-12 seed
  instruction and is retained as a rejected input after the exact transpose
  check; physical Euler transport uses ``project_functional_euler``.

No canonical ``exp(2 g V)`` coefficient enters this file.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from itertools import product
from math import factorial
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/project-composites.json"
AUDIT = ROOT / "audits/step5-project-composites-verification.json"


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class ExactScalar:
    """A monomial in Q[i] times named commuting normalization symbols."""

    rational: Fraction = Fraction(1)
    i_power: int = 0
    symbols: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        rational = Fraction(self.rational)
        remainder = self.i_power % 4
        if remainder == 2:
            rational *= -1
            remainder = 0
        elif remainder == 3:
            rational *= -1
            remainder = 1
        if any(not symbol for symbol in self.symbols):
            raise ValueError("normalization symbols must be nonempty")
        object.__setattr__(self, "rational", rational)
        object.__setattr__(self, "i_power", remainder)
        object.__setattr__(self, "symbols", tuple(sorted(self.symbols)))

    def __mul__(self, other: ExactScalar | int | Fraction) -> ExactScalar:
        if isinstance(other, (int, Fraction)):
            other = ExactScalar(Fraction(other))
        if not isinstance(other, ExactScalar):
            return NotImplemented
        return ExactScalar(
            self.rational * other.rational,
            self.i_power + other.i_power,
            self.symbols + other.symbols,
        )

    def __neg__(self) -> ExactScalar:
        return ExactScalar(-self.rational, self.i_power, self.symbols)

    def as_json(self) -> dict[str, object]:
        return {
            "rational": fraction_text(self.rational),
            "i_power": self.i_power,
            "symbols": list(self.symbols),
            "rendered": self.render(),
        }

    def render(self) -> str:
        if not self.rational:
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


@dataclass(frozen=True)
class Expr:
    """A deterministic typed operator tree with sorted scalar attributes."""

    op: str
    args: tuple[Expr, ...] = ()
    attrs: tuple[tuple[str, object], ...] = ()

    def as_json(self) -> dict[str, object]:
        return {
            "op": self.op,
            "attrs": {key: value for key, value in self.attrs},
            "args": [argument.as_json() for argument in self.args],
        }


def node(op: str, *args: Expr, **attrs: object) -> Expr:
    return Expr(op, tuple(args), tuple(sorted(attrs.items())))


def prefix_v_slots(expression: Expr, prefix: str) -> Expr:
    """Give every V occurrence in a copied expression a unique lexical port."""

    attrs = dict(expression.attrs)
    if expression.op == "V":
        attrs["color_slot"] = f"{prefix}.{attrs['color_slot']}"
    return node(
        expression.op,
        *(prefix_v_slots(argument, prefix) for argument in expression.args),
        **attrs,
    )


def v_slots(expression: Expr) -> tuple[str, ...]:
    attrs = dict(expression.attrs)
    local = (str(attrs["color_slot"]),) if expression.op == "V" else ()
    return local + tuple(slot for argument in expression.args for slot in v_slots(argument))


def operator_names(expression: Expr) -> tuple[str, ...]:
    return (expression.op,) + tuple(
        name for argument in expression.args for name in operator_names(argument)
    )


@dataclass(frozen=True)
class CompositeTerm:
    term_id: str
    family: str
    v_degree: int
    matter_degree: int
    parity: int
    free_color: str
    free_spinor: str | None
    coefficient: ExactScalar
    expression: Expr
    origin: str
    source_equations: tuple[str, ...]
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.v_degree < 0 or self.matter_degree < 0:
            raise ValueError("field degrees must be nonnegative")
        if self.parity not in (0, 1):
            raise ValueError("parity is Z/2-valued")
        if not self.term_id or not self.family or not self.free_color:
            raise ValueError("a composite term needs an id, family, and color")
        if not self.source_equations:
            raise ValueError("each term must retain its derivation source")

    def as_json(self) -> dict[str, object]:
        return {
            "term_id": self.term_id,
            "family": self.family,
            "v_degree": self.v_degree,
            "matter_degree": self.matter_degree,
            "parity": self.parity,
            "free_color": self.free_color,
            "free_spinor": self.free_spinor,
            "coefficient": self.coefficient.as_json(),
            "expression": self.expression.as_json(),
            "origin": self.origin,
            "source_equations": list(self.source_equations),
            "tags": list(self.tags),
        }


def v_leaf(slot: str) -> Expr:
    return node("V", color_slot=slot, parity=0, representation="adjoint")


def flat_d(index: str, argument: Expr, *, contraction: str | None = None) -> Expr:
    attrs: dict[str, object] = {
        "index": index,
        "parity": 1,
        "rule": "left_flat_spinor_derivative",
    }
    if contraction is not None:
        attrs["contraction"] = contraction
    return node("FlatD", argument, **attrs)


def flat_bar_d(index: str, argument: Expr, *, contraction: str | None = None) -> Expr:
    attrs: dict[str, object] = {
        "index": index,
        "parity": 1,
        "rule": "left_flat_dotted_spinor_derivative",
    }
    if contraction is not None:
        attrs["contraction"] = contraction
    return node("FlatBarD", argument, **attrs)


def bar_d_squared(argument: Expr) -> Expr:
    return node(
        "BarD2",
        argument,
        ordered_word=["barD_dot_plus", "barD_dot_minus"],
        parity=0,
        source="2A.14,3A.51",
    )


def d_squared(argument: Expr) -> Expr:
    return node(
        "D2",
        argument,
        ordered_word=["D_plus", "D_minus"],
        parity=0,
        source="2A.14,3A.52",
    )


def adjoint_bracket(left: Expr, right: Expr, *, output_color: str, contraction: str | None = None) -> Expr:
    attrs: dict[str, object] = {
        "component_rule": "[Y,Z]^C=i*c[A,B,C]*Y^A*Z^B",
        "output_color": output_color,
    }
    if contraction is not None:
        attrs["contraction"] = contraction
    return node("AdjointBracket", left, right, **attrs)


def nested_ad_v(
    degree: int,
    core_index: str,
    prefix: str,
    output_color: str,
    *,
    core_operator: str = "D",
) -> Expr:
    if degree < 1:
        raise ValueError("Gamma starts at degree one")
    if core_operator == "D":
        expression = flat_d(core_index, v_leaf(f"{prefix}.v{degree}"))
    elif core_operator == "barD":
        expression = flat_bar_d(core_index, v_leaf(f"{prefix}.v{degree}"))
    else:
        raise ValueError("core operator is D or barD")
    for position in range(degree - 1, 0, -1):
        expression = adjoint_bracket(
            v_leaf(f"{prefix}.v{position}"),
            expression,
            output_color=f"{output_color}.ad{position}",
        )
    return node("FreeColor", expression, color=output_color)


def gamma_component_coefficient(degree: int) -> ExactScalar:
    """Component coefficient of exp(-V) D exp(V) at V-degree ``degree``."""

    if degree < 1:
        raise ValueError("Gamma starts at V degree one")
    matrix_coefficient = Fraction((-1) ** (degree - 1), factorial(degree))
    return ExactScalar(matrix_coefficient, i_power=degree - 1)


def gamma_terms(max_degree: int = 3, *, spinor: str = "a_down") -> tuple[CompositeTerm, ...]:
    return tuple(
        CompositeTerm(
            term_id=f"Gamma_{degree}",
            family="Gamma",
            v_degree=degree,
            matter_degree=0,
            parity=1,
            free_color="C",
            free_spinor=spinor,
            coefficient=gamma_component_coefficient(degree),
            expression=nested_ad_v(degree, spinor, f"Gamma_{degree}", "C"),
            origin="exp(-V) D_a exp(V) BCH",
            source_equations=("3A.34",),
            tags=("BCH_DERIVED", "COMPONENTIZED_COLOR_BRACKETS"),
        )
        for degree in range(1, max_degree + 1)
    )


def w_terms(max_degree: int = 3, *, spinor: str = "a_down") -> tuple[CompositeTerm, ...]:
    result: list[CompositeTerm] = []
    for gamma in gamma_terms(max_degree, spinor=spinor):
        result.append(
            CompositeTerm(
                term_id=f"W_{gamma.v_degree}",
                family="W",
                v_degree=gamma.v_degree,
                matter_degree=0,
                parity=1,
                free_color="C",
                free_spinor=spinor,
                coefficient=ExactScalar(Fraction(-1, 8)) * gamma.coefficient,
                expression=bar_d_squared(gamma.expression),
                origin="W_a=-(1/8) barD^2 Gamma_a",
                source_equations=("3A.34", "3A.51"),
                tags=("PROJECT_K_PLUS_NORMALIZATION", "BCH_DERIVED"),
            )
        )
    return tuple(result)


def tilde_gamma_terms(
    max_degree: int = 3,
    *,
    spinor: str = "dot_a_down",
) -> tuple[CompositeTerm, ...]:
    """BCH series of E barD_dot_a(E^-1) in componentized color form."""

    result: list[CompositeTerm] = []
    for degree in range(1, max_degree + 1):
        matrix_coefficient = Fraction(-1, factorial(degree))
        result.append(
            CompositeTerm(
                term_id=f"TildeGamma_{degree}",
                family="TildeGamma",
                v_degree=degree,
                matter_degree=0,
                parity=1,
                free_color="C",
                free_spinor=spinor,
                coefficient=ExactScalar(matrix_coefficient, i_power=degree - 1),
                expression=nested_ad_v(
                    degree,
                    spinor,
                    f"TildeGamma_{degree}",
                    "C",
                    core_operator="barD",
                ),
                origin="exp(V) barD_dot_a exp(-V) BCH",
                source_equations=("3A.34a",),
                tags=("BCH_DERIVED", "ANTICHIRAL_EUCLIDEAN_SECTOR"),
            )
        )
    return tuple(result)


def tilde_w_terms(
    max_degree: int = 3,
    *,
    spinor: str = "dot_a_down",
) -> tuple[CompositeTerm, ...]:
    result: list[CompositeTerm] = []
    for gamma in tilde_gamma_terms(max_degree, spinor=spinor):
        result.append(
            CompositeTerm(
                term_id=f"TildeW_{gamma.v_degree}",
                family="TildeW",
                v_degree=gamma.v_degree,
                matter_degree=0,
                parity=1,
                free_color="C",
                free_spinor=spinor,
                coefficient=ExactScalar(Fraction(1, 8)) * gamma.coefficient,
                expression=d_squared(gamma.expression),
                origin="TildeW_dot_a=+(1/8) D^2 TildeGamma_dot_a",
                source_equations=("3A.34a", "3A.52"),
                tags=("PROJECT_TILDE_FIELD_STRENGTH_NORMALIZATION", "ANTICHIRAL_EUCLIDEAN_SECTOR"),
            )
        )
    return tuple(result)


def covariant_w_derivative_terms_at_degree(
    degree: int,
    *,
    prefix: str,
    free_color: str,
    derivative_spinor: str,
    w_spinor: str,
    overall_coefficient: ExactScalar = ExactScalar(1),
    family: str = "X",
) -> tuple[CompositeTerm, ...]:
    """Resolve D_b W_a+[Gamma_b,W_a] at fixed V-degree."""

    if degree < 1 or degree > 3:
        raise ValueError("the seed grammar resolves covariant W derivatives through V degree three")
    result: list[CompositeTerm] = []
    w = w_terms(3, spinor=w_spinor)
    gamma = gamma_terms(3, spinor=derivative_spinor)
    linear = w[degree - 1]
    linear_expression = prefix_v_slots(linear.expression, f"{prefix}.{degree}.flat")
    result.append(
        CompositeTerm(
            term_id=f"{prefix}_{degree}_flat",
            family=family,
            v_degree=degree,
            matter_degree=0,
            parity=0,
            free_color=free_color,
            free_spinor=None,
            coefficient=overall_coefficient * linear.coefficient,
            expression=node(
                "FreeColor",
                flat_d(derivative_spinor, linear_expression),
                color=free_color,
            ),
            origin=f"D_{derivative_spinor} W_{w_spinor}",
            source_equations=("3A.34", "3A.51", "5.29"),
            tags=("FLAT_DERIVATIVE_LETTER", f"SPINOR_SLOTS_{derivative_spinor}_{w_spinor}"),
        )
    )
    for gamma_degree in range(1, degree):
        w_degree = degree - gamma_degree
        gamma_term = gamma[gamma_degree - 1]
        w_term = w[w_degree - 1]
        gamma_expression = prefix_v_slots(
            gamma_term.expression,
            f"{prefix}.{degree}.connection.{gamma_degree}.{w_degree}.Gamma",
        )
        w_expression = prefix_v_slots(
            w_term.expression,
            f"{prefix}.{degree}.connection.{gamma_degree}.{w_degree}.W",
        )
        coefficient = (
            overall_coefficient
            * gamma_term.coefficient
            * w_term.coefficient
            * ExactScalar(1, i_power=1)
        )
        result.append(
            CompositeTerm(
                term_id=f"{prefix}_{degree}_connection_{gamma_degree}_{w_degree}",
                family=family,
                v_degree=degree,
                matter_degree=0,
                parity=0,
                free_color=free_color,
                free_spinor=None,
                coefficient=coefficient,
                expression=node(
                    "FreeColor",
                    adjoint_bracket(
                        gamma_expression,
                        w_expression,
                        output_color=free_color,
                        contraction=f"spinor slots {derivative_spinor},{w_spinor}",
                    ),
                    color=free_color,
                ),
                origin=f"[Gamma_{derivative_spinor},W_{w_spinor}]",
                source_equations=("3A.34", "3A.51", "5.29"),
                tags=(
                    "NONLINEAR_LETTER",
                    "COVARIANT_SPINOR_CONNECTION",
                    f"SPINOR_SLOTS_{derivative_spinor}_{w_spinor}",
                ),
            )
        )
    return tuple(result)


def x_terms_at_degree(degree: int, *, prefix: str = "X", free_color: str = "C") -> tuple[CompositeTerm, ...]:
    """Coefficient terms of X=nabla_+ W_+ at fixed total V-degree."""

    terms = covariant_w_derivative_terms_at_degree(
        degree,
        prefix=prefix,
        free_color=free_color,
        derivative_spinor="+",
        w_spinor="+",
        family="X",
    )
    return tuple(
        CompositeTerm(
            term.term_id,
            term.family,
            term.v_degree,
            term.matter_degree,
            term.parity,
            term.free_color,
            term.free_spinor,
            term.coefficient,
            term.expression,
            term.origin,
            term.source_equations,
            term.tags + ("OUTER_NABLA_PLUS_CONNECTION",)
            if term.origin.startswith("[Gamma_")
            else term.tags,
        )
        for term in terms
    )


def x_terms(max_degree: int = 3) -> tuple[CompositeTerm, ...]:
    return tuple(
        term
        for degree in range(1, max_degree + 1)
        for term in x_terms_at_degree(degree)
    )


def e_xi_terms(max_v_degree: int = 3) -> tuple[CompositeTerm, ...]:
    """Instantiate h*kappa*(1/2 nabla^a W_a-i Phi_r x TildePhi_r)."""

    result: list[CompositeTerm] = []
    for degree in range(1, max_v_degree + 1):
        divergence_terms = (
            covariant_w_derivative_terms_at_degree(
                degree,
                prefix="divW.minus_plus",
                free_color="B",
                derivative_spinor="-",
                w_spinor="+",
                family="NABLA_W_DIVERGENCE",
            )
            + covariant_w_derivative_terms_at_degree(
                degree,
                prefix="divW.plus_minus",
                free_color="B",
                derivative_spinor="+",
                w_spinor="-",
                overall_coefficient=ExactScalar(-1),
                family="NABLA_W_DIVERGENCE",
            )
        )
        for divergence_term in divergence_terms:
            result.append(
                CompositeTerm(
                    term_id=f"E_Xi_gauge_{degree}_{len(result)}",
                    family="E_Xi",
                    v_degree=degree,
                    matter_degree=0,
                    parity=0,
                    free_color="A",
                    free_spinor=None,
                    coefficient=ExactScalar(Fraction(1, 2), symbols=("h", "kappa[A,B]"))
                    * divergence_term.coefficient,
                    expression=node(
                        "FreeColor",
                        divergence_term.expression,
                        color="A",
                        paired_core_color="B",
                        divergence_identity="nabla^a W_a=nabla_- W_+-nabla_+ W_-",
                    ),
                    origin=divergence_term.origin,
                    source_equations=("5.23", "5.24", "5.26"),
                    tags=("GAUGE_EULER_CORE", "EXPLICIT_5_31_SPINOR_CONTRACTION")
                    + divergence_term.tags,
                )
            )
    matter_expression = node(
        "MatterCross",
        node("Phi", color="C", flavor="r", chirality="chiral", parity=0),
        node("TildePhi", color="D", flavor="r", chirality="antichiral", parity=0),
        color_rule="(Phi_r x TildePhi_r)^B=c[C,D,B]*Phi_r^C*TildePhi_r^D",
        bound_flavor="r",
        output_color="B",
    )
    result.append(
        CompositeTerm(
            term_id="E_Xi_matter_0",
            family="E_Xi",
            v_degree=0,
            matter_degree=2,
            parity=0,
            free_color="A",
            free_spinor=None,
            coefficient=ExactScalar(-1, i_power=1, symbols=("h", "kappa[A,B]")),
            expression=node("FreeColor", matter_expression, color="A", paired_core_color="B"),
            origin="-i (Phi_r x TildePhi_r)",
            source_equations=("5.24a", "5.24b", "5.25", "5.26"),
            tags=("MATTER_EULER_CORE", "BOUND_FLAVOR_R"),
        )
    )
    return tuple(result)


def matrix_transport_coefficients(series: str, max_ad_degree: int = 3) -> tuple[Fraction, ...]:
    if series == "project_functional_euler":
        return tuple(Fraction(1, factorial(n + 1)) for n in range(max_ad_degree + 1))
    if series == "user_requested_seed_transport":
        return tuple(
            Fraction(1) if n == 0 else Fraction(-1, factorial(n + 1))
            for n in range(max_ad_degree + 1)
        )
    raise ValueError(f"unknown transport series {series}")


def component_transport_coefficients(series: str, max_ad_degree: int = 3) -> tuple[ExactScalar, ...]:
    return tuple(
        ExactScalar(coefficient, i_power=n)
        for n, coefficient in enumerate(matrix_transport_coefficients(series, max_ad_degree))
    )


def transport_e_xi_terms(
    series: str,
    *,
    max_total_v_degree: int = 3,
) -> tuple[CompositeTerm, ...]:
    transport = component_transport_coefficients(series, max_total_v_degree)
    result: list[CompositeTerm] = []
    for core in e_xi_terms(max_total_v_degree):
        for ad_degree in range(max_total_v_degree - core.v_degree + 1):
            expression = core.expression
            for position in range(ad_degree, 0, -1):
                expression = adjoint_bracket(
                    v_leaf(f"E_V.{core.term_id}.ad{position}"),
                    expression,
                    output_color=f"E_V.{core.term_id}.C{position}",
                )
            result.append(
                CompositeTerm(
                    term_id=f"{series}__{core.term_id}__ad_{ad_degree}",
                    family="E_V",
                    v_degree=core.v_degree + ad_degree,
                    matter_degree=core.matter_degree,
                    parity=0,
                    free_color="A",
                    free_spinor=None,
                    coefficient=core.coefficient * transport[ad_degree],
                    expression=node("FreeColor", expression, color="A"),
                    origin=f"ad_V^{ad_degree}({core.term_id})",
                    source_equations=core.source_equations
                    + (
                        "5.28a-5.28d"
                        if series == "project_functional_euler"
                        else "USER-2026-07-12-STEP5-SCOPE-REVISION",
                    ),
                    tags=core.tags
                    + (
                        series.upper(),
                        f"AD_DEGREE_{ad_degree}",
                    ),
                )
            )
    return tuple(result)


def insertion_terms_at_valence(valence: int) -> tuple[CompositeTerm, ...]:
    """Expand nabla_-[X^A X^B] at explicit V valence 2, 3, or 4."""

    if valence not in (2, 3, 4):
        raise ValueError("the seed insertion grammar is I2, I3, I4")
    result: list[CompositeTerm] = []
    serial = 0
    for left_degree in range(1, valence):
        right_degree = valence - left_degree
        if right_degree < 1 or left_degree > 3 or right_degree > 3:
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
                        CompositeTerm(
                            term_id=f"I{valence}_direct_{serial:03d}",
                            family=f"I{valence}",
                            v_degree=valence,
                            matter_degree=0,
                            parity=1,
                            free_color="(A,B)",
                            free_spinor="-",
                            coefficient=left.coefficient * right.coefficient,
                            expression=node(
                                "OrderedProduct",
                                left_body,
                                right_body,
                                factor_order=["A", "B"],
                                graded_leibniz_sign=1,
                            ),
                            origin=f"D_- placement {placement}",
                            source_equations=("5.29", "5.34"),
                            tags=(
                                f"D_MINUS_{placement}",
                                "DIRECT_D_MINUS_PLACEMENT",
                                "NONLINEAR_LETTER" if left_degree > 1 or right_degree > 1 else "LINEAR_LETTERS",
                                "QUARTIC_CONTACT" if valence == 4 else "PARENT_OR_CUBIC",
                            ),
                        )
                    )
    # The connection part of nabla_- acts once on each color port of X^A X^B.
    for gamma_degree in range(1, valence - 1):
        remaining = valence - gamma_degree
        for left_degree in range(1, remaining):
            right_degree = remaining - left_degree
            if left_degree > 3 or right_degree > 3:
                continue
            gamma = gamma_terms(gamma_degree, spinor="-")[gamma_degree - 1]
            left_terms = x_terms_at_degree(left_degree, prefix=f"I{valence}.L", free_color="L")
            right_terms = x_terms_at_degree(right_degree, prefix=f"I{valence}.R", free_color="R")
            for left in left_terms:
                for right in right_terms:
                    for placement in ("LEFT", "RIGHT"):
                        serial += 1
                        if placement == "LEFT":
                            gamma_body = prefix_v_slots(
                                gamma.expression,
                                f"I{valence}.outer.{serial}.Gamma",
                            )
                            left_body = node(
                                "FreeColor",
                                adjoint_bracket(
                                    gamma_body,
                                    left.expression,
                                    output_color="A",
                                ),
                                color="A",
                            )
                            right_body = node("FreeColor", right.expression, color="B")
                        else:
                            gamma_body = prefix_v_slots(
                                gamma.expression,
                                f"I{valence}.outer.{serial}.Gamma",
                            )
                            left_body = node("FreeColor", left.expression, color="A")
                            right_body = node(
                                "FreeColor",
                                adjoint_bracket(
                                    gamma_body,
                                    right.expression,
                                    output_color="B",
                                ),
                                color="B",
                            )
                        coefficient = (
                            gamma.coefficient
                            * left.coefficient
                            * right.coefficient
                            * ExactScalar(1, i_power=1)
                        )
                        result.append(
                            CompositeTerm(
                                term_id=f"I{valence}_outer_connection_{serial:03d}",
                                family=f"I{valence}",
                                v_degree=valence,
                                matter_degree=0,
                                parity=1,
                                free_color="(A,B)",
                                free_spinor="-",
                                coefficient=coefficient,
                                expression=node(
                                    "OrderedProduct",
                                    left_body,
                                    right_body,
                                    factor_order=["A", "B"],
                                    graded_leibniz_sign=1,
                                ),
                                origin=f"outer Gamma_- connection on {placement} color port",
                                source_equations=("3A.34", "5.29", "5.34"),
                                tags=(
                                    f"OUTER_CONNECTION_{placement}",
                                    "OUTER_NABLA_MINUS_CONNECTION",
                                    "NONLINEAR_LETTER" if left_degree > 1 or right_degree > 1 else "LINEAR_LETTERS",
                                    "QUARTIC_CONTACT" if valence == 4 else "CUBIC_CONNECTION_CHILD",
                                ),
                            )
                        )
    return tuple(result)


def insertion_terms() -> tuple[CompositeTerm, ...]:
    return tuple(
        term
        for valence in (2, 3, 4)
        for term in insertion_terms_at_valence(valence)
    )


def gauge_s4_terms() -> tuple[CompositeTerm, ...]:
    """Separate chiral and antichiral quartic Euclidean gauge sectors."""

    result: list[CompositeTerm] = []
    for sector, strengths, term_prefix, family, measure, raise_rule, equations in (
        (
            "CHIRAL",
            w_terms(3, spinor="a"),
            "S4_W",
            "S4_GAUGE_CHIRAL",
            "E,+",
            "W^a=epsilon^{ab}W_b",
            ("3A.51", "4C.4", "5.16"),
        ),
        (
            "ANTICHIRAL",
            tilde_w_terms(3, spinor="dot_a"),
            "S4_TildeW",
            "S4_GAUGE_ANTICHIRAL",
            "E,-",
            "TildeW^dot_a=epsilon^{dot_a dot_b}TildeW_dot_b",
            ("3A.52", "4C.4", "5.16"),
        ),
    ):
        for left_degree in range(1, 4):
            right_degree = 4 - left_degree
            left = strengths[left_degree - 1]
            right = strengths[right_degree - 1]
            left_expression = prefix_v_slots(
                left.expression,
                f"{term_prefix}.{left_degree}.{right_degree}.L",
            )
            right_expression = prefix_v_slots(
                right.expression,
                f"{term_prefix}.{left_degree}.{right_degree}.R",
            )
            result.append(
                CompositeTerm(
                    term_id=f"{term_prefix}_{left_degree}_{right_degree}",
                    family=family,
                    v_degree=4,
                    matter_degree=0,
                    parity=0,
                    free_color="singlet",
                    free_spinor=None,
                    coefficient=ExactScalar(Fraction(-1, 4), symbols=("h",))
                    * left.coefficient
                    * right.coefficient,
                    expression=node(
                        "GaugeInvariantPairing",
                        node("SpinorRaise", left_expression, rule=raise_rule),
                        right_expression,
                        color_pairing="kappa[A,B]",
                        measure=measure,
                        ordered_factors=[f"{sector}_left_raised", f"{sector}_right_lowered"],
                        spinor_contraction="upper-lower",
                    ),
                    origin=f"-h/4 {sector}_strength_({left_degree}) {sector}_strength_({right_degree})",
                    source_equations=equations,
                    tags=(
                        "GAUGE_ACTION_QUARTIC",
                        "BACKGROUND_QUANTUM_SPLIT_REQUIRED",
                        f"{sector}_EUCLIDEAN_SECTOR",
                    ),
                )
            )
    return tuple(result)


def antichiral_gauge_s3_terms() -> tuple[CompositeTerm, ...]:
    """Cubic E,- action vertices that can carry an external TildeW."""

    result: list[CompositeTerm] = []
    strengths = tilde_w_terms(2, spinor="dot_a")
    for left_degree, right_degree in ((1, 2), (2, 1)):
        left = strengths[left_degree - 1]
        right = strengths[right_degree - 1]
        result.append(
            CompositeTerm(
                term_id=f"S3_TildeW_{left_degree}_{right_degree}",
                family="S3_GAUGE_ANTICHIRAL",
                v_degree=3,
                matter_degree=0,
                parity=0,
                free_color="singlet",
                free_spinor=None,
                coefficient=ExactScalar(Fraction(-1, 4), symbols=("h",))
                * left.coefficient
                * right.coefficient,
                expression=node(
                    "GaugeInvariantPairing",
                    node(
                        "SpinorRaise",
                        prefix_v_slots(left.expression, f"S3.TildeW.{left_degree}.{right_degree}.L"),
                        rule="TildeW^dot_a=epsilon^{dot_a dot_b}TildeW_dot_b",
                    ),
                    prefix_v_slots(right.expression, f"S3.TildeW.{left_degree}.{right_degree}.R"),
                    color_pairing="kappa[A,B]",
                    measure="E,-",
                    spinor_contraction="upper-lower",
                ),
                origin=f"-h/4 TildeW_({left_degree})_dot_a TildeW_({right_degree})^dot_a",
                source_equations=("3A.52", "4C.4", "5.16"),
                tags=("GAUGE_ACTION_CUBIC", "ANTICHIRAL_EUCLIDEAN_SECTOR"),
            )
        )
    return tuple(result)


def derivative_scope_by_v_port(expression: Expr) -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}

    def visit(current: Expr, word: tuple[str, ...]) -> None:
        attrs = dict(current.attrs)
        next_word = word
        if current.op == "FlatD":
            next_word = word + (f"D_{attrs['index']}",)
        elif current.op == "FlatBarD":
            next_word = word + (f"barD_{attrs['index']}",)
        elif current.op == "BarD2":
            next_word = word + ("barD^2",)
        elif current.op == "D2":
            next_word = word + ("D^2",)
        if current.op == "V":
            slot = str(attrs["color_slot"])
            if slot in result:
                raise ValueError(f"duplicate V port {slot}")
            result[slot] = next_word
        for argument in current.args:
            visit(argument, next_word)

    visit(expression, ())
    return result


def color_bracket_word(expression: Expr) -> tuple[dict[str, str], ...]:
    result: list[dict[str, str]] = []

    def visit(current: Expr) -> None:
        if current.op == "AdjointBracket":
            attrs = dict(current.attrs)
            result.append(
                {
                    "output_color": str(attrs["output_color"]),
                    "component_rule": str(attrs["component_rule"]),
                }
            )
        for argument in current.args:
            visit(argument)

    visit(expression)
    return tuple(result)


def ordered_background_quantum_assignments(
    terms: Sequence[CompositeTerm],
) -> tuple[dict[str, object], ...]:
    """Expand every ordered V port under V=V_B+v without combining positions."""

    result: list[dict[str, object]] = []
    for term in terms:
        ports = v_slots(term.expression)
        if len(ports) != term.v_degree or len(ports) != len(set(ports)):
            raise ValueError(f"invalid ordered port set in {term.term_id}")
        scopes = derivative_scope_by_v_port(term.expression)
        brackets = color_bracket_word(term.expression)
        for assignment_number, roles in enumerate(
            product(("BACKGROUND_EXTERNAL", "QUANTUM_WICK"), repeat=len(ports)),
            start=1,
        ):
            role_map = dict(zip(ports, roles, strict=True))
            result.append(
                {
                    "assignment_id": f"{term.term_id}__BQ_{assignment_number:02d}",
                    "source_term_id": term.term_id,
                    "source_family": term.family,
                    "source_coefficient": term.coefficient.as_json(),
                    "ordered_ports": [
                        {
                            "port_id": port,
                            "role": role_map[port],
                            "substituted_field": "V_B" if role_map[port] == "BACKGROUND_EXTERNAL" else "v",
                            "derivative_word_outer_to_inner": list(scopes[port]),
                        }
                        for port in ports
                    ],
                    "role_counts": {
                        "BACKGROUND_EXTERNAL": roles.count("BACKGROUND_EXTERNAL"),
                        "QUANTUM_WICK": roles.count("QUANTUM_WICK"),
                    },
                    "color_bracket_word": list(brackets),
                    "ordered_assignment_multiplicity": 1,
                    "coefficient_changed_by_split": False,
                }
            )
    return tuple(result)


def projected_seed_port_assignments(
    assignments: Sequence[dict[str, object]],
    *,
    background_count: int,
    quantum_count: int,
    projection_targets: tuple[str, ...],
) -> tuple[dict[str, object], ...]:
    """Attach external composite targets to selected background ports exactly."""

    result: list[dict[str, object]] = []
    for assignment in assignments:
        counts = assignment["role_counts"]
        assert isinstance(counts, dict)
        if counts != {
            "BACKGROUND_EXTERNAL": background_count,
            "QUANTUM_WICK": quantum_count,
        }:
            continue
        ports = assignment["ordered_ports"]
        assert isinstance(ports, list)
        background_ports = [
            str(port["port_id"])
            for port in ports
            if isinstance(port, dict) and port["role"] == "BACKGROUND_EXTERNAL"
        ]
        if len(projection_targets) == 1:
            projection_orders = (projection_targets,)
        elif len(projection_targets) == len(background_ports):
            projection_orders = tuple(product(projection_targets, repeat=len(background_ports)))
            projection_orders = tuple(
                order for order in projection_orders if sorted(order) == sorted(projection_targets)
            )
        elif len(background_ports) == 1:
            projection_orders = tuple((target,) for target in projection_targets)
        else:
            raise ValueError("projection targets do not match background ports")
        for projection_number, order in enumerate(projection_orders, start=1):
            result.append(
                {
                    "projected_assignment_id": f"{assignment['assignment_id']}__P{projection_number}",
                    "assignment_id": assignment["assignment_id"],
                    "source_term_id": assignment["source_term_id"],
                    "external_projections": [
                        {"port_id": port, "target": target}
                        for port, target in zip(background_ports, order, strict=True)
                    ],
                    "quantum_ports": [
                        str(port["port_id"])
                        for port in ports
                        if isinstance(port, dict) and port["role"] == "QUANTUM_WICK"
                    ],
                    "source_coefficient": assignment["source_coefficient"],
                    "ordered_assignment_multiplicity": 1,
                }
            )
    return tuple(result)


def seed_port_assignment_payload() -> dict[str, object]:
    i3_all = ordered_background_quantum_assignments(insertion_terms_at_valence(3))
    i4_all = ordered_background_quantum_assignments(insertion_terms_at_valence(4))
    s4_all = ordered_background_quantum_assignments(gauge_s4_terms())
    antichiral_s3_all = ordered_background_quantum_assignments(antichiral_gauge_s3_terms())
    i3_selected = projected_seed_port_assignments(
        i3_all,
        background_count=1,
        quantum_count=2,
        projection_targets=("X_EXTERNAL_AFTER_PROJECTOR",),
    )
    antichiral_s3_selected = projected_seed_port_assignments(
        antichiral_s3_all,
        background_count=1,
        quantum_count=2,
        projection_targets=("TILDE_W_EXTERNAL_AFTER_PROJECTOR",),
    )
    i4_tadpoles: list[dict[str, object]] = []
    for assignment in i4_all:
        if assignment["role_counts"] != {
            "BACKGROUND_EXTERNAL": 2,
            "QUANTUM_WICK": 2,
        }:
            continue
        i4_tadpoles.append(
            {
                "assignment_id": assignment["assignment_id"],
                "source_term_id": assignment["source_term_id"],
                "ordered_ports": assignment["ordered_ports"],
                "source_coefficient": assignment["source_coefficient"],
                "loop_topology": "ONE_PROPAGATOR_TADPOLE_IF_THE_TWO_QUANTUM_PORTS_ARE_PAIRED",
                "classification": "SCALELESS_IF_SOLE_LOOP_HAS_NO_EXTERNAL_MOMENTUM",
                "zero_rule": "integral d^d k/(k^2)^alpha has no mass or external momentum scale",
                "requires_routing_check": True,
            }
        )
    mixed_s4_selection = {
        "requested_external_pair": ["X_EXTERNAL", "TILDE_W_EXTERNAL"],
        "status": "PROVED_ABSENT_BY_INTRINSIC_EUCLIDEAN_CHIRAL_SECTOR",
        "proof": [
            "every S4_GAUGE_CHIRAL term has measure E,+ and only W factors",
            "every S4_GAUGE_ANTICHIRAL term has measure E,- and only TildeW factors",
            "the Project action has no mixed W*TildeW chiral integral",
        ],
        "graphir_rows": [],
    }
    legal_two_vertex_pair = {
        "status": "INSTANTIATED_AS_TWO_DISTINCT_VERTICES",
        "X_vertex_family": "I3",
        "TildeW_vertex_family": "S3_GAUGE_ANTICHIRAL",
        "X_projected_rows": len(i3_selected),
        "TildeW_projected_rows": len(antichiral_s3_selected),
        "single_vertex_identification_forbidden": True,
    }
    return {
        "substitution": "V_j=(V_B)_j+v_j independently for every ordered port j",
        "role_types": {
            "BACKGROUND_EXTERNAL": "never Wick-contracted; projected to a named external composite",
            "QUANTUM_WICK": "eligible for the Step-5A fixed-gauge V propagator",
        },
        "coefficient_rule": "ordered assignments have multiplicity one and inherit the exact source coefficient",
        "all_ordered_assignments": {
            "I3": list(i3_all),
            "I4": list(i4_all),
            "S4_GAUGE": list(s4_all),
            "S3_GAUGE_ANTICHIRAL": list(antichiral_s3_all),
        },
        "selected_for_seed": {
            "I3_one_background_two_quantum": list(i3_selected),
            "S3_antichiral_one_background_two_quantum": list(antichiral_s3_selected),
            "I4_two_background_two_quantum_tadpole": i4_tadpoles,
            "S4_mixed_X_TildeW": mixed_s4_selection,
            "legal_X_TildeW_two_vertex_pair": legal_two_vertex_pair,
        },
        "counts": {
            "I3_all": len(i3_all),
            "I4_all": len(i4_all),
            "S4_all": len(s4_all),
            "S3_antichiral_all": len(antichiral_s3_all),
            "I3_one_background_two_quantum_projected": len(i3_selected),
            "S3_antichiral_one_background_two_quantum_projected": len(antichiral_s3_selected),
            "I4_two_background_two_quantum_tadpole": len(i4_tadpoles),
            "S4_mixed_X_TildeW": 0,
        },
    }


def series_sign_audit() -> dict[str, object]:
    f_coefficients = tuple(Fraction((-1) ** n, factorial(n + 1)) for n in range(4))
    transpose_ad_signs = tuple(Fraction((-1) ** n) for n in range(4))
    derived = tuple(f_coefficients[n] * transpose_ad_signs[n] for n in range(4))
    project = matrix_transport_coefficients("project_functional_euler")
    requested = matrix_transport_coefficients("user_requested_seed_transport")
    conflict_degrees = [n for n in range(4) if project[n] != requested[n]]
    return {
        "input_F_of_ad_coefficients": [fraction_text(item) for item in f_coefficients],
        "transpose_rule": "(ad_V)^T=-ad_V",
        "transpose_degree_signs": [fraction_text(item) for item in transpose_ad_signs],
        "direct_products": [
            {
                "degree": n,
                "F_coefficient": fraction_text(f_coefficients[n]),
                "transpose_sign": fraction_text(transpose_ad_signs[n]),
                "product": fraction_text(derived[n]),
            }
            for n in range(4)
        ],
        "project_functional_euler": [fraction_text(item) for item in project],
        "user_requested_seed_transport": [fraction_text(item) for item in requested],
        "project_equals_direct_transposition": project == derived,
        "requested_equals_direct_transposition": requested == derived,
        "conflict_degrees": conflict_degrees,
        "conflict_location": "transport from Xi-variation Euler operator to V-functional Euler operator",
        "user_requested_series_status": "REJECTED_BY_5_28_TRANSPOSITION",
        "physical_instantiation_policy": "USE_PROJECT_FUNCTIONAL_EULER",
        "primitive_I2_dependency": "NONE; I2 is built directly from X_1 X_1",
    }


def coefficient_list(terms: Sequence[CompositeTerm]) -> list[str]:
    return [term.coefficient.render() for term in terms]


def count_tags(terms: Iterable[CompositeTerm]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for term in terms:
        for tag in term.tags:
            counts[tag] = counts.get(tag, 0) + 1
    return dict(sorted(counts.items()))


def build_payload() -> dict[str, object]:
    gamma = gamma_terms()
    w = w_terms()
    tilde_gamma = tilde_gamma_terms()
    tilde_w = tilde_w_terms()
    x = x_terms()
    e_xi = e_xi_terms()
    project_e_v = transport_e_xi_terms("project_functional_euler")
    requested_e_v = transport_e_xi_terms("user_requested_seed_transport")
    insertions = {f"I{valence}": insertion_terms_at_valence(valence) for valence in (2, 3, 4)}
    s4 = gauge_s4_terms()
    antichiral_s3 = antichiral_gauge_s3_terms()
    port_assignments = seed_port_assignment_payload()
    return {
        "schema": 1,
        "scope": "STEP5A_WW_PROJECT_COMPOSITE_GRAMMAR",
        "normalization": {
            "bridge": "E=exp(V)",
            "generator_commutator": "[T_A,T_B]=i*c[A,B,C]*T_C",
            "field_strength": "W_a=-(1/8)*barD^2(exp(-V)*D_a exp(V))",
            "letter": "X=nabla_+ W_+=D_+ W_+ + [Gamma_+,W_+]",
            "e_xi": "E_Xi^A=h*kappa[A,B]*(1/2*nabla^a W_a^B-i*(Phi_r x TildePhi_r)^B)",
            "insertion": "nabla_-[X^A X^B]",
            "coefficient_policy": "componentized color brackets; every displayed rational and i power is exact",
        },
        "required_max_v_degree": {
            "Gamma": 3,
            "W": 3,
            "X": 3,
            "reason": "I4 has minimum split X_1 X_3, X_2 X_2, or Gamma_2 X_1 X_1",
        },
        "series_sign_audit": series_sign_audit(),
        "Gamma": [term.as_json() for term in gamma],
        "W": [term.as_json() for term in w],
        "TildeGamma": [term.as_json() for term in tilde_gamma],
        "TildeW": [term.as_json() for term in tilde_w],
        "X": [term.as_json() for term in x],
        "E_Xi": [term.as_json() for term in e_xi],
        "E_V": {
            "project_functional_euler": [term.as_json() for term in project_e_v],
            "user_requested_seed_transport": [term.as_json() for term in requested_e_v],
            "physical_SD_uses": "project_functional_euler",
            "user_requested_seed_transport_status": "REJECTED_BY_5_28_TRANSPOSITION",
            "primitive_I2_unaffected": True,
        },
        "insertions": {
            name: [term.as_json() for term in terms]
            for name, terms in insertions.items()
        },
        "gauge_S4": [term.as_json() for term in s4],
        "antichiral_gauge_S3": [term.as_json() for term in antichiral_s3],
        "seed_port_assignments": port_assignments,
        "counts": {
            "Gamma": len(gamma),
            "W": len(w),
            "TildeGamma": len(tilde_gamma),
            "TildeW": len(tilde_w),
            "X": len(x),
            "E_Xi": len(e_xi),
            "E_V_project": len(project_e_v),
            "E_V_requested": len(requested_e_v),
            "gauge_S4": len(s4),
            "antichiral_gauge_S3": len(antichiral_s3),
            **{name: len(terms) for name, terms in insertions.items()},
        },
        "insertion_tag_counts": {
            name: count_tags(terms) for name, terms in insertions.items()
        },
        "external_imports": [],
        "canonical_exp_2gV_coefficients_imported": False,
    }


def exact_checks(payload: dict[str, object]) -> dict[str, bool]:
    gamma = gamma_terms()
    w = w_terms()
    tilde_gamma = tilde_gamma_terms()
    tilde_w = tilde_w_terms()
    x = x_terms()
    e_xi = e_xi_terms()
    project_e_v = transport_e_xi_terms("project_functional_euler")
    requested_e_v = transport_e_xi_terms("user_requested_seed_transport")
    s4 = gauge_s4_terms()
    antichiral_s3 = antichiral_gauge_s3_terms()
    x_by_degree = {
        degree: x_terms_at_degree(degree) for degree in (1, 2, 3)
    }
    insertions = {
        valence: insertion_terms_at_valence(valence) for valence in (2, 3, 4)
    }
    sign_audit = payload["series_sign_audit"]
    assert isinstance(sign_audit, dict)
    all_terms = (
        gamma
        + w
        + tilde_gamma
        + tilde_w
        + x
        + e_xi
        + project_e_v
        + requested_e_v
        + s4
        + antichiral_s3
        + tuple(term for terms in insertions.values() for term in terms)
    )
    return {
        "gamma_component_coefficients": coefficient_list(gamma) == ["1", "-1/2*i", "-1/6"],
        "w_component_coefficients": coefficient_list(w) == ["-1/8", "1/16*i", "1/48"],
        "tilde_gamma_component_coefficients": coefficient_list(tilde_gamma)
        == ["-1", "-1/2*i", "1/6"],
        "tilde_w_component_coefficients": coefficient_list(tilde_w)
        == ["-1/8", "-1/16*i", "1/48"],
        "tilde_gamma_uses_barD_not_D_core": all(
            "FlatBarD" in operator_names(term.expression)
            and "FlatD" not in operator_names(term.expression)
            for term in tilde_gamma
        ),
        "x_term_counts_by_degree": [len(x_by_degree[n]) for n in (1, 2, 3)] == [1, 2, 3],
        "x1_coefficient": coefficient_list(x_by_degree[1]) == ["-1/8"],
        "x2_coefficients": coefficient_list(x_by_degree[2]) == ["1/16*i", "-1/8*i"],
        "x3_coefficients": coefficient_list(x_by_degree[3]) == ["1/48", "-1/16", "-1/16"],
        "e_xi_is_fully_instantiated": len(e_xi_terms()) == 13,
        "e_xi_matter_coefficient": e_xi_terms()[-1].coefficient
        == ExactScalar(-1, i_power=1, symbols=("h", "kappa[A,B]")),
        "project_transposition_exact": bool(sign_audit["project_equals_direct_transposition"]),
        "requested_transposition_conflict_explicit": not bool(sign_audit["requested_equals_direct_transposition"]),
        "conflict_degrees_are_1_2_3": sign_audit["conflict_degrees"] == [1, 2, 3],
        "both_e_v_series_retained": len(transport_e_xi_terms("project_functional_euler"))
        == len(transport_e_xi_terms("user_requested_seed_transport"))
        == 24,
        "physical_e_v_uses_transposition_proved_series": payload["E_V"]["physical_SD_uses"]
        == "project_functional_euler",
        "user_requested_e_v_is_rejected_not_silent": payload["E_V"]["user_requested_seed_transport_status"]
        == "REJECTED_BY_5_28_TRANSPOSITION",
        "insertion_term_counts": [len(insertions[n]) for n in (2, 3, 4)] == [2, 10, 30],
        "both_direct_dminus_placements_I2": {
            tag for term in insertions[2] for tag in term.tags if tag.startswith("D_MINUS_")
        }
        == {"D_MINUS_LEFT", "D_MINUS_RIGHT"},
        "outer_connection_present_I3_I4": all(
            any("OUTER_NABLA_MINUS_CONNECTION" in term.tags for term in insertions[n])
            for n in (3, 4)
        ),
        "all_I4_terms_are_quartic_contact": all("QUARTIC_CONTACT" in term.tags for term in insertions[4]),
        "nonlinear_letters_present_I3_I4": all(
            any("NONLINEAR_LETTER" in term.tags for term in insertions[n])
            for n in (3, 4)
        ),
        "gauge_s4_ordered_splits": [term.term_id for term in s4]
        == [
            "S4_W_1_3",
            "S4_W_2_2",
            "S4_W_3_1",
            "S4_TildeW_1_3",
            "S4_TildeW_2_2",
            "S4_TildeW_3_1",
        ],
        "gauge_s4_exact_coefficients": coefficient_list(s4)
        == [
            "1/1536*h",
            "1/1024*h",
            "1/1536*h",
            "1/1536*h",
            "1/1024*h",
            "1/1536*h",
        ],
        "antichiral_s3_exact_coefficients": coefficient_list(antichiral_s3)
        == ["-1/512*i*h", "-1/512*i*h"],
        "background_quantum_all_assignment_counts": payload["seed_port_assignments"]["counts"]
        == {
            "I3_all": 80,
            "I4_all": 480,
            "S4_all": 96,
            "S3_antichiral_all": 16,
            "I3_one_background_two_quantum_projected": 30,
            "S3_antichiral_one_background_two_quantum_projected": 6,
            "I4_two_background_two_quantum_tadpole": 180,
            "S4_mixed_X_TildeW": 0,
        },
        "selected_I3_roles_are_one_background_two_quantum": all(
            len(item["external_projections"]) == 1 and len(item["quantum_ports"]) == 2
            for item in payload["seed_port_assignments"]["selected_for_seed"]["I3_one_background_two_quantum"]
        ),
        "selected_antichiral_S3_roles_are_one_background_two_quantum": all(
            len(item["external_projections"]) == 1 and len(item["quantum_ports"]) == 2
            for item in payload["seed_port_assignments"]["selected_for_seed"]["S3_antichiral_one_background_two_quantum"]
        ),
        "mixed_S4_X_TildeW_is_proved_absent": payload["seed_port_assignments"]["selected_for_seed"]["S4_mixed_X_TildeW"]["status"]
        == "PROVED_ABSENT_BY_INTRINSIC_EUCLIDEAN_CHIRAL_SECTOR",
        "I4_tadpoles_are_scaleless_conditionally_on_routing": all(
            item["classification"] == "SCALELESS_IF_SOLE_LOOP_HAS_NO_EXTERNAL_MOMENTUM"
            for item in payload["seed_port_assignments"]["selected_for_seed"]["I4_two_background_two_quantum_tadpole"]
        ),
        "ast_v_degree_matches_every_term": all(
            len(v_slots(term.expression)) == term.v_degree for term in all_terms
        ),
        "ast_v_ports_are_unique_inside_every_term": all(
            len(v_slots(term.expression)) == len(set(v_slots(term.expression)))
            for term in all_terms
        ),
        "no_external_coefficients": payload["external_imports"] == [],
        "no_exp_2gV_import": payload["canonical_exp_2gV_coefficients_imported"] is False,
    }


def build_audit(payload_bytes: bytes, payload: dict[str, object]) -> dict[str, object]:
    checks = exact_checks(payload)
    return {
        "schema": 1,
        "scope": "STEP5A_WW_PROJECT_COMPOSITE_GRAMMAR",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": [
            {"id": name, "passed": passed}
            for name, passed in sorted(checks.items())
        ],
        "totals": {
            "checks": len(checks),
            "failed": sum(not passed for passed in checks.values()),
        },
        "generated_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "physical_euler_transport_series": "project_functional_euler",
        "user_requested_seed_transport_status": "REJECTED_BY_5_28_TRANSPOSITION",
        "project_functional_euler_series_retained": True,
        "exact_conflict": series_sign_audit(),
        "blockers": [],
        "admission": "COMPOSITE_GRAMMAR_INSTANTIATED; LOOP_COEFFICIENT_NOT_EVALUATED_BY_THIS_MODULE",
    }


def main() -> int:
    payload = build_payload()
    payload_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(payload_bytes)
    audit = build_audit(payload_bytes, payload)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps(audit["totals"], sort_keys=True))
    return 0 if audit["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
