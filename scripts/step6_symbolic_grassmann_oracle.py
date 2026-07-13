#!/usr/bin/env python3
"""Exact proposal-only Project superspace oracle for Step 6.

The implementation is deliberately bounded: it proves local polynomial
operator identities and exposes typed product/derivative interfaces.  It does
not contract a graph and does not construct a two-loop numerator.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_3B = ROOT / "contracts/foundations/step-03b-component-reconstruction.md"
CONTRACT_5 = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
PROJECT_PROPAGATOR = ROOT / "scripts/verify_step5_propagators.py"
PROJECT_SEED_DALGEBRA = ROOT / "scripts/verify_step5_seed_dalgebra.py"
OUTPUT_DIR = ROOT / "generated/step6/symbolic-grassmann-oracle"
OUTPUT_JSON = OUTPUT_DIR / "symbolic-grassmann-oracle.json"
OUTPUT_MD = OUTPUT_DIR / "symbolic-grassmann-oracle.md"
AUDIT = ROOT / "audits/step6-symbolic-grassmann-oracle-verification.json"


@dataclass(frozen=True, order=True)
class Gaussian:
    """An exact element of Q(i)."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Gaussian":
        rhs = gaussian(other)
        return Gaussian(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.re, -self.im)

    def __sub__(self, other: object) -> "Gaussian":
        return self + (-gaussian(other))

    def __rsub__(self, other: object) -> "Gaussian":
        return gaussian(other) - self

    def __mul__(self, other: object) -> "Gaussian":
        rhs = gaussian(other)
        return Gaussian(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Gaussian":
        rhs = gaussian(other)
        norm = rhs.re * rhs.re + rhs.im * rhs.im
        if norm == 0:
            raise ZeroDivisionError("division by zero in Q(i)")
        return Gaussian(
            (self.re * rhs.re + self.im * rhs.im) / norm,
            (self.im * rhs.re - self.re * rhs.im) / norm,
        )

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def to_json(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im)}

    def render(self) -> str:
        if not self.im:
            return str(self.re)
        if not self.re:
            return f"{self.im}*i"
        sign = "+" if self.im > 0 else "-"
        return f"({self.re}{sign}{abs(self.im)}*i)"


def gaussian(value: object) -> Gaussian:
    if isinstance(value, Gaussian):
        return value
    if isinstance(value, Fraction):
        return Gaussian(value)
    if isinstance(value, int):
        return Gaussian(Fraction(value))
    raise TypeError(f"unsupported exact scalar {value!r}")


ZERO_QI = Gaussian()
ONE_QI = gaussian(1)
I_QI = Gaussian(Fraction(0), Fraction(1))
Monomial = tuple[tuple[str, int], ...]


def _canonical_monomial(powers: Mapping[str, int]) -> Monomial:
    if any(exponent < 0 for exponent in powers.values()):
        raise ValueError("Q(i)[p] admits no negative monomial exponents")
    return tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent))


def _multiply_monomials(left: Monomial, right: Monomial) -> Monomial:
    powers: dict[str, int] = {}
    for name, exponent in (*left, *right):
        powers[name] = powers.get(name, 0) + exponent
    return _canonical_monomial(powers)


@dataclass(frozen=True)
class Poly:
    """Sparse canonical polynomial in commuting bispinor components over Q(i)."""

    terms: tuple[tuple[Monomial, Gaussian], ...] = ()

    @staticmethod
    def from_terms(terms: Mapping[Monomial, Gaussian]) -> "Poly":
        merged = {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}
        return Poly(tuple(sorted(merged.items())))

    @staticmethod
    def constant(value: object) -> "Poly":
        coefficient = gaussian(value)
        return Poly.from_terms({(): coefficient}) if coefficient else Poly()

    @staticmethod
    def variable(name: str) -> "Poly":
        if not name or any(character.isspace() for character in name):
            raise ValueError("polynomial symbol must be nonempty and whitespace-free")
        return Poly.from_terms({((name, 1),): ONE_QI})

    def as_dict(self) -> dict[Monomial, Gaussian]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __add__(self, other: object) -> "Poly":
        rhs = poly(other)
        merged = self.as_dict()
        for monomial, coefficient in rhs.terms:
            merged[monomial] = merged.get(monomial, ZERO_QI) + coefficient
        return Poly.from_terms(merged)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly.from_terms({monomial: -coefficient for monomial, coefficient in self.terms})

    def __sub__(self, other: object) -> "Poly":
        return self + (-poly(other))

    def __rsub__(self, other: object) -> "Poly":
        return poly(other) - self

    def __mul__(self, other: object) -> "Poly":
        rhs = poly(other)
        result: dict[Monomial, Gaussian] = {}
        for left_monomial, left_coefficient in self.terms:
            for right_monomial, right_coefficient in rhs.terms:
                monomial = _multiply_monomials(left_monomial, right_monomial)
                result[monomial] = (
                    result.get(monomial, ZERO_QI)
                    + left_coefficient * right_coefficient
                )
        return Poly.from_terms(result)

    __rmul__ = __mul__

    def divide_scalar(self, scalar: object) -> "Poly":
        denominator = gaussian(scalar)
        return Poly.from_terms(
            {monomial: coefficient / denominator for monomial, coefficient in self.terms}
        )

    def __pow__(self, exponent: int) -> "Poly":
        if exponent < 0:
            raise ValueError("Q(i)[p] admits no negative powers")
        result = ONE
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def to_json(self) -> list[dict[str, object]]:
        return [
            {
                "monomial": [{"symbol": name, "exponent": exponent} for name, exponent in monomial],
                "coefficient": coefficient.to_json(),
            }
            for monomial, coefficient in self.terms
        ]

    def evaluate(self, substitution: Mapping[str, Gaussian]) -> Gaussian:
        result = ZERO_QI
        for monomial, coefficient in self.terms:
            term = coefficient
            for name, exponent in monomial:
                if name not in substitution:
                    raise KeyError(f"missing exact substitution for {name}")
                for _ in range(exponent):
                    term = term * substitution[name]
            result = result + term
        return result

    def render(self) -> str:
        if not self:
            return "0"
        rendered: list[str] = []
        for monomial, coefficient in self.terms:
            factor = "*".join(
                name if exponent == 1 else f"{name}^{exponent}"
                for name, exponent in monomial
            )
            if factor:
                rendered.append(f"{coefficient.render()}*{factor}")
            else:
                rendered.append(coefficient.render())
        return " + ".join(rendered)


def poly(value: object) -> Poly:
    if isinstance(value, Poly):
        return value
    return Poly.constant(value)


ZERO = Poly()
ONE = Poly.constant(1)
I = Poly.constant(I_QI)


@dataclass(frozen=True)
class SparseMatrix:
    size: int
    entries: tuple[tuple[tuple[int, int], Poly], ...] = ()

    @staticmethod
    def from_entries(size: int, entries: Mapping[tuple[int, int], Poly]) -> "SparseMatrix":
        cleaned: dict[tuple[int, int], Poly] = {}
        for (row, column), value in entries.items():
            if not (0 <= row < size and 0 <= column < size):
                raise IndexError("matrix entry outside declared square size")
            if value:
                cleaned[(row, column)] = value
        return SparseMatrix(size, tuple(sorted(cleaned.items())))

    @staticmethod
    def identity(size: int) -> "SparseMatrix":
        return SparseMatrix.from_entries(size, {(index, index): ONE for index in range(size)})

    def as_dict(self) -> dict[tuple[int, int], Poly]:
        return dict(self.entries)

    def __add__(self, other: "SparseMatrix") -> "SparseMatrix":
        if self.size != other.size:
            raise ValueError("matrix sizes disagree")
        merged = self.as_dict()
        for key, value in other.entries:
            merged[key] = merged.get(key, ZERO) + value
        return SparseMatrix.from_entries(self.size, merged)

    def __neg__(self) -> "SparseMatrix":
        return self.scale(-1)

    def __sub__(self, other: "SparseMatrix") -> "SparseMatrix":
        return self + (-other)

    def scale(self, coefficient: object) -> "SparseMatrix":
        factor = poly(coefficient)
        return SparseMatrix.from_entries(
            self.size, {key: factor * value for key, value in self.entries}
        )

    def __matmul__(self, other: "SparseMatrix") -> "SparseMatrix":
        if self.size != other.size:
            raise ValueError("matrix sizes disagree")
        right_by_row: dict[int, list[tuple[int, Poly]]] = {}
        for (row, column), value in other.entries:
            right_by_row.setdefault(row, []).append((column, value))
        result: dict[tuple[int, int], Poly] = {}
        for (row, pivot), left_value in self.entries:
            for column, right_value in right_by_row.get(pivot, []):
                key = (row, column)
                result[key] = result.get(key, ZERO) + left_value * right_value
        return SparseMatrix.from_entries(self.size, result)

    def apply(self, value: "Exterior") -> "Exterior":
        if self.size != 16:
            raise ValueError("Grassmann matrices must have size 16")
        vector = value.as_dict()
        result: dict[int, Poly] = {}
        for (row, column), coefficient in self.entries:
            if column in vector:
                result[row] = result.get(row, ZERO) + coefficient * vector[column]
        return Exterior.from_terms(result)

    def nonzero_count(self) -> int:
        return len(self.entries)

    def specialize(self, substitution: Mapping[str, Gaussian]) -> dict[tuple[int, int], Gaussian]:
        return {
            key: value.evaluate(substitution)
            for key, value in self.entries
            if value.evaluate(substitution)
        }


GENERATOR_ORDER = (
    "theta_plus",
    "theta_minus",
    "bartheta_dotplus",
    "bartheta_dotminus",
)


def exterior_sign(left_mask: int, right_mask: int) -> int:
    inversions = sum(
        1
        for left_index in range(4)
        if (left_mask >> left_index) & 1
        for right_index in range(4)
        if (right_mask >> right_index) & 1 and left_index > right_index
    )
    return -1 if inversions & 1 else 1


@dataclass(frozen=True)
class Exterior:
    """Sparse element of Lambda(theta+,theta-,bartheta_dot+,bartheta_dot-)."""

    terms: tuple[tuple[int, Poly], ...] = ()

    @staticmethod
    def from_terms(terms: Mapping[int, Poly]) -> "Exterior":
        cleaned = {
            mask: coefficient
            for mask, coefficient in terms.items()
            if coefficient
            and isinstance(mask, int)
            and 0 <= mask < 16
        }
        if any(not isinstance(mask, int) or not (0 <= mask < 16) for mask in terms):
            raise ValueError("exterior mask must lie in [0,15]")
        return Exterior(tuple(sorted(cleaned.items())))

    @staticmethod
    def basis(mask: int, coefficient: object = 1) -> "Exterior":
        return Exterior.from_terms({mask: poly(coefficient)})

    def as_dict(self) -> dict[int, Poly]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __add__(self, other: "Exterior") -> "Exterior":
        merged = self.as_dict()
        for mask, value in other.terms:
            merged[mask] = merged.get(mask, ZERO) + value
        return Exterior.from_terms(merged)

    def __neg__(self) -> "Exterior":
        return self.scale(-1)

    def __sub__(self, other: "Exterior") -> "Exterior":
        return self + (-other)

    def scale(self, coefficient: object) -> "Exterior":
        factor = poly(coefficient)
        return Exterior.from_terms(
            {mask: factor * value for mask, value in self.terms}
        )

    def __mul__(self, other: "Exterior") -> "Exterior":
        result: dict[int, Poly] = {}
        for left_mask, left_value in self.terms:
            for right_mask, right_value in other.terms:
                if left_mask & right_mask:
                    continue
                mask = left_mask | right_mask
                result[mask] = (
                    result.get(mask, ZERO)
                    + exterior_sign(left_mask, right_mask) * left_value * right_value
                )
        return Exterior.from_terms(result)

    def left_derivative(self, generator: int) -> "Exterior":
        result: dict[int, Poly] = {}
        for mask, coefficient in self.terms:
            if not ((mask >> generator) & 1):
                continue
            lower_count = (mask & ((1 << generator) - 1)).bit_count()
            result[mask ^ (1 << generator)] = (
                (-1 if lower_count & 1 else 1) * coefficient
            )
        return Exterior.from_terms(result)

    def coefficient(self, mask: int) -> Poly:
        return self.as_dict().get(mask, ZERO)

    def to_json(self) -> list[dict[str, object]]:
        return [
            {
                "mask": mask,
                "generators": [
                    GENERATOR_ORDER[index]
                    for index in range(4)
                    if (mask >> index) & 1
                ],
                "coefficient": coefficient.to_json(),
            }
            for mask, coefficient in self.terms
        ]


def left_multiplication_matrix(generator: int) -> SparseMatrix:
    entries: dict[tuple[int, int], Poly] = {}
    for mask in range(16):
        if (mask >> generator) & 1:
            continue
        lower_count = (mask & ((1 << generator) - 1)).bit_count()
        entries[(mask | (1 << generator), mask)] = poly(
            -1 if lower_count & 1 else 1
        )
    return SparseMatrix.from_entries(16, entries)


def left_derivative_matrix(generator: int) -> SparseMatrix:
    entries: dict[tuple[int, int], Poly] = {}
    for mask in range(16):
        if not ((mask >> generator) & 1):
            continue
        lower_count = (mask & ((1 << generator) - 1)).bit_count()
        entries[(mask ^ (1 << generator), mask)] = poly(
            -1 if lower_count & 1 else 1
        )
    return SparseMatrix.from_entries(16, entries)


@dataclass(frozen=True)
class BispinorMomentum:
    label: str
    components: tuple[tuple[Poly, Poly], tuple[Poly, Poly]]

    @staticmethod
    def symbolic(label: str) -> "BispinorMomentum":
        return BispinorMomentum(
            label,
            (
                (Poly.variable(f"{label}_pp"), Poly.variable(f"{label}_pm")),
                (Poly.variable(f"{label}_mp"), Poly.variable(f"{label}_mm")),
            ),
        )

    def __add__(self, other: "BispinorMomentum") -> "BispinorMomentum":
        return BispinorMomentum(
            f"({self.label}+{other.label})",
            tuple(
                tuple(self.components[row][column] + other.components[row][column] for column in range(2))
                for row in range(2)
            ),  # type: ignore[arg-type]
        )

    def square_four(self) -> Poly:
        return (
            self.components[0][0] * self.components[1][1]
            - self.components[0][1] * self.components[1][0]
        )


def matrix_sum(*matrices: SparseMatrix) -> SparseMatrix:
    if not matrices:
        raise ValueError("matrix_sum requires at least one operand")
    result = SparseMatrix.from_entries(matrices[0].size, {})
    for matrix in matrices:
        result = result + matrix
    return result


def flat_operators(momentum: BispinorMomentum) -> dict[str, SparseMatrix]:
    """Translate the verified Project matrices to symbolic p_(a dot a)."""

    theta = [left_multiplication_matrix(0), left_multiplication_matrix(1)]
    bartheta_lower = [left_multiplication_matrix(2), left_multiplication_matrix(3)]
    derivative = [left_derivative_matrix(index) for index in range(4)]
    bartheta_upper = [bartheta_lower[1], bartheta_lower[0].scale(-1)]
    bar_derivative_lower = [left_derivative_matrix(3).scale(-1), left_derivative_matrix(2)]

    d_lower: list[SparseMatrix] = []
    bar_d_lower: list[SparseMatrix] = []
    for undotted in range(2):
        operator = derivative[undotted]
        for dotted in range(2):
            operator = operator + bartheta_upper[dotted].scale(
                I * momentum.components[undotted][dotted]
            )
        d_lower.append(operator)
    for dotted in range(2):
        operator = bar_derivative_lower[dotted]
        for undotted in range(2):
            operator = operator + theta[undotted].scale(
                -I * momentum.components[undotted][dotted]
            )
        bar_d_lower.append(operator)

    d_upper = [d_lower[1], d_lower[0].scale(-1)]
    bar_d_upper = [bar_d_lower[1], bar_d_lower[0].scale(-1)]
    d2 = d_upper[0] @ d_lower[0] + d_upper[1] @ d_lower[1]
    bar_d2 = bar_d_lower[0] @ bar_d_upper[0] + bar_d_lower[1] @ bar_d_upper[1]
    d_bar_d2_d = d_upper[0] @ bar_d2 @ d_lower[0] + d_upper[1] @ bar_d2 @ d_lower[1]
    k_plus = (d_lower[0] @ bar_d2 @ d_lower[0]).scale(Fraction(-1, 8))
    return {
        "D_plus": d_lower[0],
        "D_minus": d_lower[1],
        "barD_dotplus": bar_d_lower[0],
        "barD_dotminus": bar_d_lower[1],
        "D2": d2,
        "barD2": bar_d2,
        "DbarD2D": d_bar_d2_d,
        "K_plus": k_plus,
        "identity": SparseMatrix.identity(16),
        "zero": SparseMatrix.from_entries(16, {}),
    }


def anticommutator(left: SparseMatrix, right: SparseMatrix) -> SparseMatrix:
    return left @ right + right @ left


def normalized_delta() -> Exterior:
    """delta^4(theta)=theta^2 bartheta^2=-4 theta+theta-bartheta+bartheta-."""

    return Exterior.basis(15, -4)


def constant_projection(value: Exterior) -> Poly:
    return value.coefficient(0)


def chiral_measure(value: Exterior, operators: Mapping[str, SparseMatrix]) -> Poly:
    return constant_projection(operators["D2"].apply(value)).divide_scalar(-4)


def antichiral_measure(value: Exterior, operators: Mapping[str, SparseMatrix]) -> Poly:
    return constant_projection(operators["barD2"].apply(value)).divide_scalar(-4)


def full_measure(value: Exterior, operators: Mapping[str, SparseMatrix]) -> Poly:
    return constant_projection((operators["D2"] @ operators["barD2"]).apply(value)).divide_scalar(16)


PRIMITIVE_DERIVATIVES = (
    "D_plus",
    "D_minus",
    "barD_dotplus",
    "barD_dotminus",
)


def expand_derivative_word(
    outer_to_inner: Sequence[str],
) -> tuple[tuple[Gaussian, tuple[str, ...]], ...]:
    """Expand D2/barD2 while retaining outer-to-inner operator order."""

    token_expansions: dict[str, tuple[tuple[Gaussian, tuple[str, ...]], ...]] = {
        name: ((ONE_QI, (name,)),) for name in PRIMITIVE_DERIVATIVES
    }
    token_expansions["D2"] = (
        (ONE_QI, ("D_minus", "D_plus")),
        (-ONE_QI, ("D_plus", "D_minus")),
    )
    token_expansions["barD2"] = (
        (ONE_QI, ("barD_dotplus", "barD_dotminus")),
        (-ONE_QI, ("barD_dotminus", "barD_dotplus")),
    )
    expanded: list[tuple[Gaussian, tuple[str, ...]]] = [(ONE_QI, ())]
    for token in outer_to_inner:
        if token not in token_expansions:
            raise KeyError(f"unknown derivative token {token}")
        expanded = [
            (left_coefficient * right_coefficient, left_word + right_word)
            for left_coefficient, left_word in expanded
            for right_coefficient, right_word in token_expansions[token]
        ]
    return tuple(expanded)


def compile_derivative_word(
    operators: Mapping[str, SparseMatrix], outer_to_inner: Sequence[str]
) -> SparseMatrix:
    """Compile displayed outer-to-inner order as M_outer ... M_inner."""

    result = SparseMatrix.from_entries(16, {})
    for coefficient, primitive_word in expand_derivative_word(outer_to_inner):
        term = SparseMatrix.identity(16)
        for primitive in primitive_word:
            term = term @ operators[primitive]
        result = result + term.scale(coefficient)
    return result


@dataclass(frozen=True)
class LabeledLeaf:
    label: str
    momentum: BispinorMomentum
    parity: int
    value: Exterior
    derivative_word: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.parity not in (0, 1):
            raise ValueError("leaf parity must be 0 or 1")


@dataclass(frozen=True)
class ProductTerm:
    coefficient: Poly
    factors: tuple[LabeledLeaf, ...]
    ordered_tensors: tuple[str, ...] = ()


@dataclass(frozen=True)
class LeafAST:
    leaf: LabeledLeaf


@dataclass(frozen=True)
class OrderedProductAST:
    children: tuple["LocalAST", ...]

    def __post_init__(self) -> None:
        if not self.children:
            raise ValueError("ordered product requires at least one child")


@dataclass(frozen=True)
class GradedBracketAST:
    """Generic superalgebra commutator; not the component adjoint grammar node."""

    left: "LocalAST"
    right: "LocalAST"


@dataclass(frozen=True)
class ComponentAdjointOrderedProductAST:
    """One ordered c-tensor product; the grammar QI owns every bracket i."""

    left: "LocalAST"
    right: "LocalAST"
    left_color: str
    right_color: str
    output_color: str
    qi_prefactor: Poly = ONE


@dataclass(frozen=True)
class DerivativeAST:
    outer_to_inner: tuple[str, ...]
    child: "LocalAST"
    coefficient: Poly = ONE


LocalAST = (
    LeafAST
    | OrderedProductAST
    | GradedBracketAST
    | ComponentAdjointOrderedProductAST
    | DerivativeAST
)


def _merge_product_terms(terms: Iterable[ProductTerm]) -> tuple[ProductTerm, ...]:
    merged: dict[tuple[tuple[LabeledLeaf, ...], tuple[str, ...]], Poly] = {}
    for term in terms:
        key = (term.factors, term.ordered_tensors)
        merged[key] = merged.get(key, ZERO) + term.coefficient
    return tuple(
        ProductTerm(coefficient, factors, ordered_tensors)
        for (factors, ordered_tensors), coefficient in sorted(
            merged.items(),
            key=lambda item: (
                tuple(factor.label for factor in item[0][0]),
                item[0][1],
            ),
        )
        if coefficient
    )


def apply_primitive_graded_leibniz(
    terms: Sequence[ProductTerm], primitive: str
) -> tuple[ProductTerm, ...]:
    if primitive not in PRIMITIVE_DERIVATIVES:
        raise KeyError(f"graded Leibniz accepts primitive odd derivatives, got {primitive}")
    emitted: list[ProductTerm] = []
    for term in terms:
        prefix_parity = 0
        for index, factor in enumerate(term.factors):
            operator = flat_operators(factor.momentum)[primitive]
            differentiated = operator.apply(factor.value)
            if differentiated:
                replacement = LabeledLeaf(
                    label=factor.label,
                    momentum=factor.momentum,
                    parity=factor.parity ^ 1,
                    value=differentiated,
                    derivative_word=(primitive,) + factor.derivative_word,
                )
                factors = term.factors[:index] + (replacement,) + term.factors[index + 1 :]
                emitted.append(
                    ProductTerm(
                        term.coefficient * (-1 if prefix_parity else 1),
                        factors,
                        term.ordered_tensors,
                    )
                )
            prefix_parity ^= factor.parity
    return _merge_product_terms(emitted)


def apply_word_graded_leibniz(
    leaves: Sequence[LabeledLeaf], outer_to_inner: Sequence[str], coefficient: object = 1
) -> tuple[ProductTerm, ...]:
    return apply_word_to_product_terms(
        (ProductTerm(ONE, tuple(leaves)),), outer_to_inner, coefficient
    )


def apply_word_to_product_terms(
    input_terms: Sequence[ProductTerm],
    outer_to_inner: Sequence[str],
    coefficient: object = 1,
) -> tuple[ProductTerm, ...]:
    """Apply one derivative scope to the complete ordered product below it."""

    emitted: list[ProductTerm] = []
    for branch_coefficient, primitive_word in expand_derivative_word(outer_to_inner):
        branch: tuple[ProductTerm, ...] = tuple(
            ProductTerm(
                term.coefficient * poly(coefficient) * branch_coefficient,
                term.factors,
                term.ordered_tensors,
            )
            for term in input_terms
        )
        for primitive in reversed(primitive_word):
            branch = apply_primitive_graded_leibniz(branch, primitive)
        emitted.extend(branch)
    return _merge_product_terms(emitted)


def ast_parity(node: LocalAST) -> int:
    if isinstance(node, LeafAST):
        return node.leaf.parity
    if isinstance(node, OrderedProductAST):
        return sum(ast_parity(child) for child in node.children) & 1
    if isinstance(node, GradedBracketAST):
        return (ast_parity(node.left) + ast_parity(node.right)) & 1
    if isinstance(node, ComponentAdjointOrderedProductAST):
        return (ast_parity(node.left) + ast_parity(node.right)) & 1
    if isinstance(node, DerivativeAST):
        branch_parities = {
            len(word) & 1 for _, word in expand_derivative_word(node.outer_to_inner)
        }
        if len(branch_parities) != 1:
            raise ValueError("derivative token expansion has inhomogeneous parity")
        return ast_parity(node.child) ^ next(iter(branch_parities))
    raise TypeError(f"undeclared local AST node {type(node)!r}")


def multiply_product_terms(
    left: Sequence[ProductTerm], right: Sequence[ProductTerm]
) -> tuple[ProductTerm, ...]:
    """Concatenate without reordering; the noncommutative leaf order is retained."""

    return _merge_product_terms(
        ProductTerm(
            left_term.coefficient * right_term.coefficient,
            left_term.factors + right_term.factors,
            left_term.ordered_tensors + right_term.ordered_tensors,
        )
        for left_term in left
        for right_term in right
    )


def evaluate_local_ast(node: LocalAST) -> tuple[ProductTerm, ...]:
    """Recursively evaluate derivative scopes at product/bracket nodes."""

    if isinstance(node, LeafAST):
        return (ProductTerm(ONE, (node.leaf,)),)
    if isinstance(node, OrderedProductAST):
        result = evaluate_local_ast(node.children[0])
        for child in node.children[1:]:
            result = multiply_product_terms(result, evaluate_local_ast(child))
        return result
    if isinstance(node, GradedBracketAST):
        left = evaluate_local_ast(node.left)
        right = evaluate_local_ast(node.right)
        forward = multiply_product_terms(left, right)
        reverse_sign = -1 if (ast_parity(node.left) * ast_parity(node.right)) % 2 == 0 else 1
        reverse = tuple(
            ProductTerm(
                term.coefficient * reverse_sign,
                term.factors,
                term.ordered_tensors,
            )
            for term in multiply_product_terms(right, left)
        )
        return _merge_product_terms((*forward, *reverse))
    if isinstance(node, ComponentAdjointOrderedProductAST):
        color_tensor = (
            f"c[{node.left_color},{node.right_color},{node.output_color}]"
        )
        return _merge_product_terms(
            ProductTerm(
                node.qi_prefactor * term.coefficient,
                term.factors,
                term.ordered_tensors + (color_tensor,),
            )
            for term in multiply_product_terms(
                evaluate_local_ast(node.left), evaluate_local_ast(node.right)
            )
        )
    if isinstance(node, DerivativeAST):
        return apply_word_to_product_terms(
            evaluate_local_ast(node.child),
            node.outer_to_inner,
            node.coefficient,
        )
    raise TypeError(f"undeclared local AST node {type(node)!r}")


def evaluate_ordered_product(terms: Sequence[ProductTerm]) -> Exterior:
    result = Exterior()
    for term in terms:
        value = Exterior.basis(0, term.coefficient)
        for factor in term.factors:
            value = value * factor.value
        result = result + value
    return result


@dataclass(frozen=True)
class RationalKernel:
    """Factorized scalar kernel used only for exact p_(4)^2 cancellation."""

    coefficient: Gaussian
    numerator: tuple[str, ...] = ()
    denominator: tuple[str, ...] = ()

    def reduced(self) -> "RationalKernel":
        numerator = list(self.numerator)
        denominator = list(self.denominator)
        for factor in sorted(set(numerator) & set(denominator)):
            count = min(numerator.count(factor), denominator.count(factor))
            for _ in range(count):
                numerator.remove(factor)
                denominator.remove(factor)
        return RationalKernel(
            self.coefficient, tuple(sorted(numerator)), tuple(sorted(denominator))
        )

    def __mul__(self, other: "RationalKernel") -> "RationalKernel":
        return RationalKernel(
            self.coefficient * other.coefficient,
            self.numerator + other.numerator,
            self.denominator + other.denominator,
        ).reduced()


def exact_identity_checks() -> dict[str, bool]:
    p = BispinorMomentum.symbolic("p")
    operators = flat_operators(p)
    zero = operators["zero"]
    unit = operators["identity"]
    d = (operators["D_plus"], operators["D_minus"])
    bar_d = (operators["barD_dotplus"], operators["barD_dotminus"])
    checks: dict[str, bool] = {}
    for left in range(2):
        for right in range(2):
            checks[f"D_D_{left}_{right}"] = anticommutator(d[left], d[right]) == zero
            checks[f"barD_barD_{left}_{right}"] = anticommutator(bar_d[left], bar_d[right]) == zero
            checks[f"D_barD_{left}_{right}"] = anticommutator(d[left], bar_d[right]) == unit.scale(
                -2 * I * p.components[left][right]
            )
    p4_squared = p.square_four()
    checks["D2_barD2_D2"] = (
        operators["D2"] @ operators["barD2"] @ operators["D2"]
        == operators["D2"].scale(-16 * p4_squared)
    )
    checks["barD2_D2_barD2"] = (
        operators["barD2"] @ operators["D2"] @ operators["barD2"]
        == operators["barD2"].scale(-16 * p4_squared)
    )
    saturated = (operators["D2"] @ operators["barD2"]).apply(normalized_delta())
    checks["normalized_delta_closed_constant_16"] = constant_projection(saturated) == poly(16)
    checks["normalized_delta_full_measure_1"] = full_measure(normalized_delta(), operators) == ONE
    theta2 = Exterior.basis(3, -2)
    bartheta2 = Exterior.basis(12, 2)
    checks["theta2_chiral_measure_1"] = chiral_measure(theta2, operators) == ONE
    checks["bartheta2_antichiral_measure_1"] = antichiral_measure(bartheta2, operators) == ONE

    # The contract relation g^2=h^{-1} is kept as an exact factor cancellation;
    # no numerical sample for h is used here.
    k_v = RationalKernel(Gaussian(Fraction(-1, 2)), ("h", "p_(4)^2"), ())
    g_v = RationalKernel(gaussian(-2), (), ("h", "p_(4)^2"))
    scalar_identity = RationalKernel(ONE_QI)
    checks["K_V_G_V_scalar_left"] = k_v * g_v == scalar_identity
    checks["G_V_K_V_scalar_right"] = g_v * k_v == scalar_identity
    return checks


def _load_verified_project_module():
    specification = importlib.util.spec_from_file_location(
        "step6_project_translation_source", PROJECT_PROPAGATOR
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load verified Project matrix implementation")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def translation_checks() -> dict[str, bool]:
    """Specialize the polynomial matrices and compare the verified Project source."""

    source = _load_verified_project_module()
    checks: dict[str, bool] = {}
    names = {
        "D_plus": "D_plus",
        "D_minus": "D_minus",
        "barD_dotplus": "barD_plus",
        "barD_dotminus": "barD_minus",
        "D2": "D2",
        "barD2": "barD2",
        "DbarD2D": "DbarD2D",
    }
    for four_vector in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
        p1, p2, p3, p4 = (Fraction(entry) for entry in four_vector)
        substitution = {
            "p_pp": Gaussian(p4, -p3),
            "p_pm": Gaussian(-p2, -p1),
            "p_mp": Gaussian(p2, -p1),
            "p_mm": Gaussian(p4, p3),
        }
        translated = flat_operators(BispinorMomentum.symbolic("p"))
        verified = source.flat_operators(four_vector)
        label = "_".join(str(entry).replace("-", "m") for entry in four_vector)
        for translated_name, verified_name in names.items():
            specialized = translated[translated_name].specialize(substitution)
            verified_sparse = {
                (row, column): Gaussian(value.re, value.im)
                for row, values in enumerate(verified[verified_name])
                for column, value in enumerate(values)
                if value
            }
            checks[f"{label}_{translated_name}"] = specialized == verified_sparse
    return checks


def exterior_axiom_checks() -> dict[str, bool]:
    generators = [Exterior.basis(1 << index) for index in range(4)]
    checks: dict[str, bool] = {}
    for left in range(4):
        checks[f"nilpotent_{left}"] = generators[left] * generators[left] == Exterior()
        for right in range(4):
            checks[f"anticommute_{left}_{right}"] = (
                generators[left] * generators[right]
                + generators[right] * generators[left]
                == Exterior()
            )
            checks[f"left_derivative_{left}_{right}"] = (
                generators[right].left_derivative(left)
                == Exterior.basis(0, 1 if left == right else 0)
            )
    return checks


def word_and_leibniz_checks() -> dict[str, bool]:
    p = BispinorMomentum.symbolic("p")
    q = BispinorMomentum.symbolic("q")
    operators = flat_operators(p)
    w1_word = ("barD2", "D_plus")
    x1_word = ("D_plus", "barD2", "D_plus")
    w1_compiled = compile_derivative_word(operators, w1_word).scale(Fraction(-1, 8))
    w1_direct = (operators["barD2"] @ operators["D_plus"]).scale(Fraction(-1, 8))
    x1_compiled = compile_derivative_word(operators, x1_word).scale(Fraction(-1, 8))

    odd_leaf = LabeledLeaf("Psi_1", p, 1, Exterior.basis(1))
    even_leaf = LabeledLeaf(
        "V_2", q, 0, Exterior.basis(0) + Exterior.basis(15, Poly.variable("v2_top"))
    )
    product = odd_leaf.value * even_leaf.value
    leibniz_terms = apply_word_graded_leibniz((odd_leaf, even_leaf), ("D_plus",))
    leibniz_value = evaluate_ordered_product(leibniz_terms)
    direct_value = flat_operators(p + q)["D_plus"].apply(product)
    return {
        "W1_compiled_equals_direct": w1_compiled == w1_direct,
        "X1_compiled_equals_K_plus": x1_compiled == operators["K_plus"],
        "odd_even_graded_Leibniz_equals_total_momentum_matrix": leibniz_value == direct_value,
        "labeled_leaf_histories_retained": all(
            any(factor.derivative_word for factor in term.factors)
            for term in leibniz_terms
        ),
    }


def generic_graded_bracket_scope_fixture() -> dict[str, object]:
    """Certify outer-scope distribution for a generic graded commutator only."""

    p = BispinorMomentum.symbolic("p")
    q = BispinorMomentum.symbolic("q")
    even_masks = (0, 3, 5, 6, 9, 10, 12, 15)
    v1_value = Exterior()
    v2_value = Exterior()
    for mask in even_masks:
        v1_value = v1_value + Exterior.basis(mask, Poly.variable(f"v1_{mask}"))
        v2_value = v2_value + Exterior.basis(mask, Poly.variable(f"v2_{mask}"))
    v1 = LeafAST(LabeledLeaf("F_1", p, 0, v1_value))
    v2 = LeafAST(LabeledLeaf("F_2", q, 0, v2_value))

    d_v2 = DerivativeAST(("D_plus",), v2)
    full_scope = DerivativeAST(
        ("barD2",),
        GradedBracketAST(v1, d_v2),
    )
    wrong_leafwise_scope = OrderedProductAST(
        (
            DerivativeAST(("barD2",), v1),
            DerivativeAST(("barD2",), d_v2),
        )
    )
    correct_terms = evaluate_local_ast(full_scope)
    wrong_terms = evaluate_local_ast(wrong_leafwise_scope)

    def bar_allocation(term: ProductTerm) -> tuple[int, ...]:
        return tuple(
            sum(1 for token in factor.derivative_word if token.startswith("barD_"))
            for factor in term.factors
        )

    correct_allocations = {bar_allocation(term) for term in correct_terms}
    wrong_allocations = {bar_allocation(term) for term in wrong_terms}
    correct_orders = {
        tuple(factor.label for factor in term.factors) for term in correct_terms
    }
    checks = {
        "full_scope_has_terms": bool(correct_terms),
        "full_scope_retains_both_bracket_orders": correct_orders
        == {("F_1", "F_2"), ("F_2", "F_1")},
        "full_scope_uses_exactly_two_outer_bar_derivatives": all(
            sum(allocation) == 2 for allocation in correct_allocations
        ),
        "full_scope_contains_mixed_endpoint_terms": (1, 1) in correct_allocations,
        "full_scope_contains_left_endpoint_terms": (2, 0) in correct_allocations,
        "full_scope_contains_right_endpoint_terms": (0, 2) in correct_allocations,
        "generic_inner_D_history_stays_on_F2": all(
            any(
                factor.label == "F_2" and "D_plus" in factor.derivative_word
                for factor in term.factors
            )
            for term in correct_terms
        ),
        "leafwise_double_application_has_four_bar_derivatives": all(
            sum(allocation) == 4 for allocation in wrong_allocations
        ),
        "full_scope_rejects_leafwise_double_application": correct_terms != wrong_terms,
    }
    return {
        "certifies": "OUTER_SCOPE_DISTRIBUTION_ONLY_NOT_COMPONENT_ADJOINT_GRAMMAR",
        "formula": "barD2*graded_bracket(F_1,D_plus*F_2)",
        "rejected_formula": "(barD2*F_1)*(barD2*D_plus*F_2)",
        "correct_term_count": len(correct_terms),
        "wrong_term_count": len(wrong_terms),
        "correct_bar_allocations": [list(allocation) for allocation in sorted(correct_allocations)],
        "wrong_bar_allocations": [list(allocation) for allocation in sorted(wrong_allocations)],
        "checks": checks,
    }


def component_adjoint_ordered_product_fixture() -> dict[str, object]:
    """Certify the post-commutator-expansion component grammar node."""

    p = BispinorMomentum.symbolic("p")
    q = BispinorMomentum.symbolic("q")
    even_masks = (0, 3, 5, 6, 9, 10, 12, 15)
    left_value = Exterior()
    right_value = Exterior()
    for mask in even_masks:
        left_value = left_value + Exterior.basis(mask, Poly.variable(f"y_{mask}"))
        right_value = right_value + Exterior.basis(mask, Poly.variable(f"z_{mask}"))
    y_a = LeafAST(LabeledLeaf("Y^A", p, 0, left_value))
    z_b = LeafAST(LabeledLeaf("Z^B", q, 0, right_value))
    d_z_b = DerivativeAST(("D_plus",), z_b)

    ordered_without_adjoint = multiply_product_terms(
        evaluate_local_ast(y_a), evaluate_local_ast(d_z_b)
    )
    component_adjoint = ComponentAdjointOrderedProductAST(
        y_a,
        d_z_b,
        left_color="A",
        right_color="B",
        output_color="C",
        qi_prefactor=ONE,
    )
    adjoint_terms = evaluate_local_ast(component_adjoint)
    gamma2_terms = apply_word_to_product_terms(
        adjoint_terms, (), (-I).divide_scalar(2)
    )
    w2_terms = apply_word_to_product_terms(
        adjoint_terms, ("barD2",), I.divide_scalar(16)
    )
    expected_gamma2 = tuple(
        ProductTerm(
            term.coefficient * (-I).divide_scalar(2),
            term.factors,
            term.ordered_tensors + ("c[A,B,C]",),
        )
        for term in ordered_without_adjoint
    )
    expected_w2 = apply_word_to_product_terms(
        tuple(
            ProductTerm(
                term.coefficient,
                term.factors,
                term.ordered_tensors + ("c[A,B,C]",),
            )
            for term in ordered_without_adjoint
        ),
        ("barD2",),
        I.divide_scalar(16),
    )
    orders = {
        tuple(factor.label for factor in term.factors) for term in adjoint_terms
    }
    checks = {
        "component_adjoint_has_one_ordered_term": len(adjoint_terms) == 1,
        "component_adjoint_has_forward_order_only": orders == {("Y^A", "Z^B")},
        "component_adjoint_has_no_reverse_term": ("Z^B", "Y^A") not in orders,
        "component_adjoint_carries_one_color_tensor": all(
            term.ordered_tensors == ("c[A,B,C]",) for term in adjoint_terms
        ),
        "component_adjoint_adds_no_extra_i": all(
            term.coefficient == ONE for term in adjoint_terms
        ),
        "component_adjoint_has_no_factor_two": all(
            term.coefficient != 2 * ONE for term in adjoint_terms
        ),
        "Gamma2_post_commutator_prefactor_stays_minus_i_over_2": (
            gamma2_terms == expected_gamma2
        ),
        "W2_post_commutator_prefactor_stays_plus_i_over_16": (
            w2_terms == expected_w2
        ),
        "W2_component_scope_has_forward_order_only": all(
            tuple(factor.label for factor in term.factors) == ("Y^A", "Z^B")
            for term in w2_terms
        ),
    }
    return {
        "generator_commutator": "[T_A,T_B]=i*c[A,B,C]*T_C",
        "grammar_component_node": "c[A,B,C]*Y^A*Z^B",
        "grammar_QI_is_after_commutator_expansion": True,
        "reverse_component_term": False,
        "adjoint_QI_prefactor": "1",
        "Gamma2_raw_prefactor": "-i/2",
        "Gamma2_component_prefactor": "-i/2",
        "W2_raw_prefactor": "i/16",
        "W2_component_prefactor": "i/16",
        "adjoint_term_count": len(adjoint_terms),
        "W2_scope_term_count": len(w2_terms),
        "checks": checks,
    }


def canonical_ring_checks() -> dict[str, bool]:
    p = Poly.variable("p_pp")
    q = Poly.variable("q_mm")
    left = (p + q) * (p - q)
    right = p**2 - q**2
    monomials = [monomial for monomial, _ in left.terms]
    return {
        "difference_of_squares_exact": left == right,
        "canonical_monomial_sort": all(monomial == tuple(sorted(monomial)) for monomial in monomials),
        "zero_terms_removed": (p - p) == ZERO,
        "no_float_in_coefficients": all(
            isinstance(number, Fraction)
            for _, coefficient in left.terms
            for number in (coefficient.re, coefficient.im)
        ),
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flatten(grouped: Mapping[str, Mapping[str, bool]]) -> list[dict[str, object]]:
    return [
        {"id": f"{group}.{name}", "passed": passed}
        for group, checks in grouped.items()
        for name, passed in checks.items()
    ]


def build_result() -> dict[str, object]:
    generic_scope = generic_graded_bracket_scope_fixture()
    generic_checks = generic_scope["checks"]
    component_adjoint = component_adjoint_ordered_product_fixture()
    component_checks = component_adjoint["checks"]
    assert isinstance(generic_checks, dict)
    assert isinstance(component_checks, dict)
    grouped = {
        "ring": canonical_ring_checks(),
        "exterior": exterior_axiom_checks(),
        "project_translation": translation_checks(),
        "project_polynomial_identities": exact_identity_checks(),
        "word_and_leibniz": word_and_leibniz_checks(),
        "generic_graded_bracket_scope": generic_checks,
        "component_adjoint_ordered_product": component_checks,
    }
    checks = flatten(grouped)
    failed = [check for check in checks if not check["passed"]]
    p = BispinorMomentum.symbolic("p")
    operators = flat_operators(p)
    return {
        "schema": 1,
        "scope": "STEP6_PROPOSAL_ONLY_SYMBOLIC_GRASSMANN_FOUNDATION",
        "status": "PASS" if not failed else "FAIL",
        "admission_status": (
            "EXACT_LOCAL_ORACLE_NO_GRAPH_CONTRACTION"
            if not failed
            else "BLOCKED_SYMBOLIC_PROJECT_IDENTITY_MISMATCH"
        ),
        "arithmetic": "SPARSE_Q_I_POLYNOMIAL_NO_FLOATING_POINT",
        "generator_order": list(GENERATOR_ORDER),
        "momentum_symbols": {
            "p_pp": "p_(+ dot+)",
            "p_pm": "p_(+ dot-)",
            "p_mp": "p_(- dot+)",
            "p_mm": "p_(- dot-)",
            "p_(4)^2": p.square_four().to_json(),
        },
        "operator_nonzero_entries": {
            name: operator.nonzero_count() for name, operator in operators.items()
        },
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "provenance": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                CONTRACT_3B,
                CONTRACT_5,
                PROJECT_PROPAGATOR,
                PROJECT_SEED_DALGEBRA,
            )
        },
        "derived_exact_relations": {
            "mixed_anticommutator": "{D_a,barD_dotb}=-2*i*p_(a dotb)*1_16",
            "D_projector_identity": "D2*barD2*D2=-16*p_(4)^2*D2",
            "barD_projector_identity": "barD2*D2*barD2=-16*p_(4)^2*barD2",
            "normalized_delta": "theta2*bartheta2=-4*theta+*theta-*bartheta_dot+*bartheta_dot-",
            "closed_delta": "[D2*barD2(delta)]_(theta=0)=16",
            "W1_word": "W_(1)+=(-1/8)*barD2*D_plus*V",
            "X1_word": "X_(1)=(-1/8)*D_plus*barD2*D_plus*V=K_plus*V",
            "vector_scalar_inverse": "[-(h/2)*p_(4)^2]*[-2/(h*p_(4)^2)]=1",
            "component_adjoint": (
                "[T_A,T_B]=i*c[A,B,C]*T_C; grammar QI is post-expansion; "
                "AST node=c[A,B,C]*Y^A*Z^B with no extra i and no reverse term"
            ),
            "Gamma2_component_prefactor": "-i/2",
            "W2_component_prefactor": "i/16",
        },
        "derivative_word_fixtures": {
            "W1": {
                "coefficient": "-1/8",
                "outer_to_inner": ["barD2", "D_plus"],
                "expanded": [
                    {
                        "coefficient": coefficient.render(),
                        "outer_to_inner": list(word),
                    }
                    for coefficient, word in expand_derivative_word(("barD2", "D_plus"))
                ],
            },
            "X1": {
                "coefficient": "-1/8",
                "outer_to_inner": ["D_plus", "barD2", "D_plus"],
                "expanded": [
                    {
                        "coefficient": coefficient.render(),
                        "outer_to_inner": list(word),
                    }
                    for coefficient, word in expand_derivative_word(
                        ("D_plus", "barD2", "D_plus")
                    )
                ],
            },
            "GENERIC_GRADED_BRACKET_SCOPE_FIXTURE": {
                key: value
                for key, value in generic_scope.items()
                if key != "checks"
            },
            "COMPONENT_ADJOINT_ORDERED_PRODUCT_FIXTURE": {
                key: value
                for key, value in component_adjoint.items()
                if key != "checks"
            },
        },
        "implemented_interfaces": [
            "canonical sparse Q(i) polynomial ring",
            "four-generator exterior product and left derivative",
            "symbolic Project 16x16 operators",
            "outer-to-inner derivative-word compiler",
            "ordered labeled-leaf graded Leibniz expansion",
            "recursive generic graded-bracket derivative-scope evaluation",
            "component adjoint ordered-product evaluation",
            "chiral antichiral full-measure functionals",
        ],
        "remaining_interface": {
            "status": "BLOCKED_GRAPH_TENSOR_CONTRACTION_INTERFACE_NOT_IMPLEMENTED",
            "required": [
                "typed map from GraphIR ports to labeled leaves and routed bispinor momenta",
                "propagator endpoint delta and edge-orientation object",
                "color and coupling coefficient tensor carried independently of Grassmann tensors",
                "edge-tagged endpoint transfer and collapse certificates",
                "streaming contraction sink from Wick rows into local S3 S4 I2 I3 tensors",
            ],
        },
        "negative_claims": {
            "graph_contraction_performed": False,
            "two_loop_numerator_computed": False,
            "integral_reduction_performed": False,
            "coefficient_computed": False,
        },
    }


def render_markdown(result: Mapping[str, object]) -> str:
    provenance = result["provenance"]
    assert isinstance(provenance, dict)
    return "\n".join(
        [
            "# Step 6 symbolic Grassmann oracle",
            "",
            "`PROPOSAL_ONLY`; `NO_GRAPH_CONTRACTION`; `NO_TWO_LOOP_NUMERATOR`.",
            "",
            "$$",
            "\\Lambda=\\Lambda(\\vartheta^+,\\vartheta^-,\\bar\\vartheta_{\\dot+},\\bar\\vartheta_{\\dot-}),",
            "\\qquad",
            "p_{(4)}^2=p_{+\\dot+}p_{-\\dot-}-p_{+\\dot-}p_{-\\dot+}.",
            "$$",
            "",
            "$$",
            "\\{D_a,\\bar D_{\\dot b}\\}=-2ip_{a\\dot b},\\qquad",
            "D^2\\bar D^2D^2=-16p_{(4)}^2D^2,\\qquad",
            "\\bar D^2D^2\\bar D^2=-16p_{(4)}^2\\bar D^2.",
            "$$",
            "",
            "$$",
            "\\delta^4(\\vartheta)=\\vartheta^2\\bar\\vartheta^2",
            "=-4\\vartheta^+\\vartheta^-\\bar\\vartheta_{\\dot+}\\bar\\vartheta_{\\dot-},",
            "\\qquad",
            "[D^2\\bar D^2\\delta^4(\\vartheta)]_{\\vartheta=0}=16.",
            "$$",
            "",
            "$$",
            "\\mathcal W_{(1)+}=-\\frac18\\bar D^2D_+V,\\qquad",
            "X_{(1)}=-\\frac18D_+\\bar D^2D_+V=K_+V.",
            "$$",
            "",
            "The generic graded-bracket fixture certifies outer-scope distribution only.",
            "The component adjoint grammar is instead",
            "",
            "$$",
            "[Y,Z]^C=i\\,c_{AB}{}^C Y^A Z^B,\\qquad",
            "\\text{no reverse component term}.",
            "$$",
            "",
            "$$",
            "\\left(-\\frac{i}{2}\\right)i=\\frac12,\\qquad",
            "\\left(\\frac{i}{16}\\right)i=-\\frac1{16}.",
            "$$",
            "",
            f"Checks: `{result['totals']}`.",
            "",
            "## Provenance SHA-256",
            "",
            *[f"- `{path}`: `{digest}`" for path, digest in sorted(provenance.items())],
            "",
            "## Open typed boundary",
            "",
            "`BLOCKED_GRAPH_TENSOR_CONTRACTION_INTERFACE_NOT_IMPLEMENTED`.",
            "",
        ]
    )


def main() -> int:
    result = build_result()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(result), encoding="utf-8")
    audit = {
        "schema": 1,
        "generator": str(Path(__file__).resolve().relative_to(ROOT)),
        "generated": [
            str(OUTPUT_JSON.relative_to(ROOT)),
            str(OUTPUT_MD.relative_to(ROOT)),
        ],
        "status": result["status"],
        "admission_status": result["admission_status"],
        "totals": result["totals"],
        "checks": result["checks"],
        "provenance": result["provenance"],
        "generated_sha256": {
            str(OUTPUT_JSON.relative_to(ROOT)): sha256(OUTPUT_JSON),
            str(OUTPUT_MD.relative_to(ROOT)): sha256(OUTPUT_MD),
        },
        "negative_claims": result["negative_claims"],
        "remaining_interface": result["remaining_interface"],
    }
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], **result["totals"]}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
