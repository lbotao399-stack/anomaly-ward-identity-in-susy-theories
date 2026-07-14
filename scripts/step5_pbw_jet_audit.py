#!/usr/bin/env python3
"""Target-blind Lyndon--PBW audit for the two covariant Step-5 jet directions.

The only mathematical inputs read by this script are locked Project foundations.
No Step-5 contract, Step-5 engine, or holomorphic-twist target is read.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_BASE = "00000f748fe4bdd1b5d122663cc1fb814faace66"
SOURCE_FILES = {
    "contracts/foundations/step-03c-gauge-vector-representation.md":
        "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1",
    "contracts/foundations/step-04-extended-sym-notation.md":
        "3fcf7e242928d3512c02059d8c28d9551b5cb86156f9d6259cd2bba713211d27",
}
LOCKED_FOUNDATIONS = [
    "contracts/foundations/step-01-supersymmetry-commutator.md",
    "contracts/foundations/step-02a-flat-superspace.md",
    "contracts/foundations/step-03a-gauge-chiral-action.md",
    "contracts/foundations/step-03b-component-reconstruction.md",
    "contracts/foundations/step-03c-gauge-vector-representation.md",
    "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
    "contracts/foundations/step-04-extended-sym-notation.md",
    "contracts/foundations/step-04a-n1-super-yang-mills.md",
    "contracts/foundations/step-04b-n2-super-yang-mills.md",
    "contracts/foundations/step-04c-n4-super-yang-mills.md",
]
LINK_TERMS = (
    "wilson",
    "duhamel",
    "parallel transport",
    "path-order",
    "path order",
    "link completion",
    "bilocal",
)

Word = str
LieFactor = str
SymMonomial = Tuple[LieFactor, ...]
WordPoly = Dict[Word, Fraction]
SymPoly = Dict[SymMonomial, Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean(poly: Dict) -> Dict:
    return {key: value for key, value in poly.items() if value}


def add_poly(left: Dict, right: Dict) -> Dict:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + value
    return clean(out)


def scale_poly(poly: Dict, scalar: Fraction) -> Dict:
    return clean({key: scalar * value for key, value in poly.items()})


def word_product(left: WordPoly, right: WordPoly) -> WordPoly:
    out: WordPoly = {}
    for word_l, coeff_l in left.items():
        for word_r, coeff_r in right.items():
            word = word_l + word_r
            out[word] = out.get(word, Fraction(0)) + coeff_l * coeff_r
    return clean(out)


def commutator(left: WordPoly, right: WordPoly) -> WordPoly:
    return add_poly(word_product(left, right), scale_poly(word_product(right, left), Fraction(-1)))


def is_lyndon(word: Word) -> bool:
    if not word:
        return False
    return all(word < word[index:] for index in range(1, len(word)))


def standard_lyndon_bracket(word: Word, cache: Dict[Word, WordPoly]) -> WordPoly:
    if word in cache:
        return cache[word]
    if len(word) == 1:
        cache[word] = {word: Fraction(1)}
        return cache[word]
    suffixes = [word[index:] for index in range(1, len(word)) if is_lyndon(word[index:])]
    suffix = max(suffixes, key=len)
    prefix = word[: len(word) - len(suffix)]
    assert is_lyndon(prefix), (word, prefix, suffix)
    cache[word] = commutator(
        standard_lyndon_bracket(prefix, cache),
        standard_lyndon_bracket(suffix, cache),
    )
    return cache[word]


def distinct_permutations(items: Sequence[LieFactor]) -> List[Tuple[LieFactor, ...]]:
    return sorted(set(itertools.permutations(items)))


def symmetrization_expand(monomial: SymMonomial, brackets: Dict[LieFactor, WordPoly]) -> WordPoly:
    if not monomial:
        return {"": Fraction(1)}
    orders = distinct_permutations(monomial)
    out: WordPoly = {}
    for order in orders:
        term: WordPoly = {"": Fraction(1)}
        for factor in order:
            term = word_product(term, brackets[factor])
        out = add_poly(out, term)
    return scale_poly(out, Fraction(1, len(orders)))


def symmetric_monomials(factors: Sequence[LieFactor], degree: int) -> List[SymMonomial]:
    if degree == 0:
        return [tuple()]
    out: List[SymMonomial] = []

    def rec(start: int, remaining: int, current: List[LieFactor]) -> None:
        if remaining == 0:
            out.append(tuple(current))
            return
        for index in range(start, len(factors)):
            factor = factors[index]
            weight = len(factor)
            if weight <= remaining:
                current.append(factor)
                rec(index, remaining - weight, current)
                current.pop()

    rec(0, degree, [])
    return sorted(out, key=lambda item: (len(item), item))


def invert_matrix(matrix: List[List[Fraction]]) -> List[List[Fraction]]:
    size = len(matrix)
    augmented = [
        row[:] + [Fraction(int(i == j)) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][index] - factor * augmented[column][index]
                    for index in range(2 * size)
                ]
    return [row[size:] for row in augmented]


def matrix_product(left: List[List[Fraction]], right: List[List[Fraction]]) -> List[List[Fraction]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def identity_matrix(size: int) -> List[List[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def sym_poly_expand(poly: SymPoly, brackets: Dict[LieFactor, WordPoly]) -> WordPoly:
    out: WordPoly = {}
    for monomial, coefficient in poly.items():
        out = add_poly(out, scale_poly(symmetrization_expand(monomial, brackets), coefficient))
    return clean(out)


def word_poly_inverse(
    poly: WordPoly,
    degree: int,
    words_by_degree: Dict[int, List[Word]],
    sym_basis_by_degree: Dict[int, List[SymMonomial]],
    inverse_by_degree: Dict[int, List[List[Fraction]]],
) -> SymPoly:
    words = words_by_degree[degree]
    basis = sym_basis_by_degree[degree]
    vector = [poly.get(word, Fraction(0)) for word in words]
    inverse = inverse_by_degree[degree]
    coefficients = [sum(inverse[row][column] * vector[column] for column in range(len(words))) for row in range(len(basis))]
    return clean({basis[index]: coefficient for index, coefficient in enumerate(coefficients)})


def sym_product(left: SymPoly, right: SymPoly, factor_order: Dict[LieFactor, int]) -> SymPoly:
    out: SymPoly = {}
    for monomial_l, coefficient_l in left.items():
        for monomial_r, coefficient_r in right.items():
            monomial = tuple(sorted(monomial_l + monomial_r, key=factor_order.__getitem__))
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient_l * coefficient_r
    return clean(out)


def star_product(
    left: SymPoly,
    right: SymPoly,
    brackets: Dict[LieFactor, WordPoly],
    words_by_degree: Dict[int, List[Word]],
    sym_basis_by_degree: Dict[int, List[SymMonomial]],
    inverse_by_degree: Dict[int, List[List[Fraction]]],
) -> SymPoly:
    degree_l = next((sum(len(factor) for factor in monomial) for monomial in left), 0)
    degree_r = next((sum(len(factor) for factor in monomial) for monomial in right), 0)
    product = word_product(sym_poly_expand(left, brackets), sym_poly_expand(right, brackets))
    return word_poly_inverse(
        product,
        degree_l + degree_r,
        words_by_degree,
        sym_basis_by_degree,
        inverse_by_degree,
    )


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def sym_name(monomial: SymMonomial) -> str:
    if not monomial:
        return "1"
    names = {"1": "p1", "2": "p2"}
    return "*".join(names.get(factor, f"l{factor}") for factor in monomial)


def serialize_word_poly(poly: WordPoly) -> Dict[str, str]:
    return {word or "1": fraction_string(poly[word]) for word in sorted(poly)}


def serialize_sym_poly(poly: SymPoly) -> Dict[str, str]:
    return {sym_name(monomial): fraction_string(poly[monomial]) for monomial in sorted(poly)}


def serialize_matrix(matrix: List[List[Fraction]]) -> List[List[str]]:
    return [[fraction_string(entry) for entry in row] for row in matrix]


def signed_term(coefficient: Fraction, symbol: str, first: bool) -> str:
    sign = "-" if coefficient < 0 else "+"
    magnitude = abs(coefficient)
    if magnitude == 1:
        body = symbol
    else:
        body = f"\\frac{{{magnitude.numerator}}}{{{magnitude.denominator}}}{symbol}" if magnitude.denominator != 1 else f"{magnitude.numerator}{symbol}"
    if first:
        return body if coefficient > 0 else f"-{body}"
    return f" {sign} {body}"


def sym_poly_latex(poly: SymPoly) -> str:
    factor_names = {"1": "p_1", "2": "p_2"}
    pieces: List[str] = []
    for monomial, coefficient in sorted(poly.items()):
        counts = Counter(monomial)
        factor_pieces = []
        for factor in sorted(counts):
            name = factor_names.get(factor, f"\\ell_{{{factor}}}")
            exponent = counts[factor]
            factor_pieces.append(name if exponent == 1 else f"{name}^{{{exponent}}}")
        symbol = "".join(factor_pieces) or "1"
        pieces.append(signed_term(coefficient, symbol, not pieces))
    return "".join(pieces) if pieces else "0"


def build_markdown(report: Dict) -> str:
    degree_table = "\n".join(
        f"| {degree} | {entry['word_dimension']} | {entry['symmetric_dimension']} | {entry['forward_inverse']} | {entry['inverse_forward']} |"
        for degree, entry in report["degree_audit"].items()
    )
    shuffle_table = "\n".join(
        f"| $({entry['m']},{entry['n']})$ | ${entry['distinct_shuffles']}$ | ${entry['coefficient']}$ |"
        for entry in report["shuffle_normalization"]
    )
    degree_three_rows = "\n".join(
        f"| $P_{{{word[0]}}}P_{{{word[1]}}}P_{{{word[2]}}}$ | ${sym_poly_latex(poly)}$ |"
        for word, poly in report["degree_three_sym_polys"].items()
    )
    return rf"""# Step 5 target-blind Lyndon--PBW covariant-jet audit

Status: `PBW_PASS__{report['link_completion']['status']}`

## 1. Locked notation

Only `{report['source_files'][0]}` and `{report['source_files'][1]}` supply the algebra.  No Step-5 contract, Step-5 engine, or external target was read.  The symbol $+$ denotes one fixed undotted spin-frame slot, with no sum over $+$.

$$
P_{{\dot a}}:=\boldsymbol{{\mathcal D}}^{{\mathsf V}}_{{E+\dot a}},
\qquad
A:=\boldsymbol\nabla^{{\mathsf V}}_{{E+}}\boldsymbol{{\mathcal W}}^{{\mathsf V}}_{{E+}},
\qquad
\operatorname{{ad}}_A(X):=\llbracket A,X\rrbracket .
$$

From (3C.1), (3C.2), and (3C.44), $\rho_E=1$ and $\epsilon_{{++}}=0$, hence

$$
\begin{{aligned}}
[\boldsymbol{{\mathcal D}}^{{\mathsf V}}_{{E+\dot a}},
 \boldsymbol{{\mathcal D}}^{{\mathsf V}}_{{E+\dot b}}]
&=\rho_E\epsilon_{{\dot a\dot b}}
\frac12\left(
\boldsymbol\nabla^{{\mathsf V}}_{{E+}}
\boldsymbol{{\mathcal W}}^{{\mathsf V}}_{{E+}}
+\boldsymbol\nabla^{{\mathsf V}}_{{E+}}
\boldsymbol{{\mathcal W}}^{{\mathsf V}}_{{E+}}
\right)
+\rho_E\epsilon_{{++}}
\bar{{\boldsymbol\nabla}}^{{\mathsf V}}_{{E(\dot a}}
\widetilde{{\boldsymbol{{\mathcal W}}}}^{{\mathsf V}}_{{E\dot b)}}\\
&=1\cdot\epsilon_{{\dot a\dot b}}
\boldsymbol\nabla^{{\mathsf V}}_{{E+}}
\boldsymbol{{\mathcal W}}^{{\mathsf V}}_{{E+}}
+1\cdot0\cdot
\bar{{\boldsymbol\nabla}}^{{\mathsf V}}_{{E(\dot a}}
\widetilde{{\boldsymbol{{\mathcal W}}}}^{{\mathsf V}}_{{E\dot b)}}.
\end{{aligned}}
$$

Acting on an adjoint field gives

$$
[P_{{\dot a}},P_{{\dot b}}]
=\epsilon_{{\dot a\dot b}}\operatorname{{ad}}_A,
\qquad
\epsilon_{{\dot1\dot2}}=-1.
$$

Set $P_1:=P_{{\dot1}}$, $P_2:=P_{{\dot2}}$, $C:=[P_1,P_2]$.  Then

$$
C=-\operatorname{{ad}}_A.
$$

## 2. Lyndon Lie basis through degree four

For alphabet $1<2$, the nontrivial Lyndon brackets are

$$
\begin{{aligned}}
\ell_{{12}}&=[P_1,P_2]=C,\\
\ell_{{112}}&=[P_1,C],
&\ell_{{122}}&=[C,P_2],\\
\ell_{{1112}}&=[P_1,[P_1,C]],
&\ell_{{1122}}&=[P_1,[C,P_2]],
&\ell_{{1222}}&=[[C,P_2],P_2].
\end{{aligned}}
$$

Because $P_i$ is a covariant derivation,

$$
[P_i,\operatorname{{ad}}_B]=\operatorname{{ad}}_{{P_iB}},
\qquad
[\operatorname{{ad}}_B,P_i]=-\operatorname{{ad}}_{{P_iB}}.
$$

Therefore

$$
\begin{{aligned}}
\ell_{{12}}&=-\operatorname{{ad}}_A,
&\ell_{{112}}&=-\operatorname{{ad}}_{{P_1A}},
&\ell_{{122}}&=+\operatorname{{ad}}_{{P_2A}},\\
\ell_{{1112}}&=-\operatorname{{ad}}_{{P_1^2A}},
&\ell_{{1122}}&=+\operatorname{{ad}}_{{P_1P_2A}},
&\ell_{{1222}}&=-\operatorname{{ad}}_{{P_2^2A}}.
\end{{aligned}}
$$

The equality $P_1P_2A=P_2P_1A$ used in $\ell_{{1122}}$ follows exactly from

$$
(P_1P_2-P_2P_1)A=-\llbracket A,A\rrbracket=0,
$$

because $A$ is even.

## 3. PBW symmetrization and exact inverse

Let $\mathfrak L=\operatorname{{Lie}}\langle P_1,P_2\rangle$, let $S(\mathfrak L)$ be its symmetric algebra, and let $U(\mathfrak L)$ be its universal enveloping algebra.  Let $\operatorname{{Perm}}(y_1,\ldots,y_k)$ denote the set of distinct permutations of the displayed multiset.  The PBW map used here is the filtered linear map

$$
\operatorname{{Sym}}_{{\rm PBW}}:S(\mathfrak L)\longrightarrow U(\mathfrak L),
\qquad
y_1\cdots y_k\longmapsto
\frac1{{|\operatorname{{Perm}}(y_1,\ldots,y_k)|}}
\sum_{{\tau\in\operatorname{{Perm}}(y_1,\ldots,y_k)}}
y_{{\tau(1)}}\cdots y_{{\tau(k)}}.
$$

Let $\operatorname{{Sh}}(1^m,2^n)$ denote the $\binom{{m+n}}{{m}}$ distinct binary words containing $m$ symbols $1$ and $n$ symbols $2$.  For repeated $P_1,P_2$ factors,

$$
J_{{m,n}}(X):=
\frac1{{\binom{{m+n}}{{m}}}}
\sum_{{w\in\operatorname{{Sh}}(1^m,2^n)}}P_wX.
$$

The denominator is $\binom{{m+n}}{{m}}$, not $(m+n)!$.

Every binary word has a unique nonincreasing Chen--Fox--Lyndon factorization.  Each standard Lyndon bracket $\ell_w$ has associative leading word $w$ with coefficient one.  Ordered products of these brackets therefore give a triangular word-basis change with unit diagonal.  Symmetrization is consequently a filtered linear isomorphism.  It does not preserve the ordinary product.

| $(m,n)$ | distinct shuffles | coefficient per word |
|---:|---:|---:|
{shuffle_table}

| degree | word dimension | $S(\mathfrak L)$ dimension | forward-inverse | inverse-forward |
|---:|---:|---:|:---:|:---:|
{degree_table}

All matrix entries were computed in `fractions.Fraction`; no floating-point arithmetic occurs.
The exact degree-$0$ through degree-$4$ word bases, symmetric bases, forward matrices, and inverse matrices are recorded in `audits/step5-pbw-jet-audit.json`.

## 4. Degree-two and degree-three identities

$$
J_{{1,1}}(X)=\frac12(P_1P_2+P_2P_1)X.
$$

$$
\begin{{aligned}}
P_1P_2X
&=J_{{1,1}}(X)+\frac12CX
=J_{{1,1}}(X)-\frac12\llbracket A,X\rrbracket,\\
P_2P_1X
&=J_{{1,1}}(X)-\frac12CX
=J_{{1,1}}(X)+\frac12\llbracket A,X\rrbracket.
\end{{aligned}}
$$

Define commutative PBW symbols $p_i:=\operatorname{{Sym}}_{{\rm PBW}}^{{-1}}(P_i)$ and retain $\ell_w$ as the Lyndon generators.  Exact inverse images of all degree-three ordered words are:

| ordered word | $\operatorname{{Sym}}_{{\rm PBW}}^{{-1}}$ |
|---|---|
{degree_three_rows}

Equivalently, the pure symmetric jets are

$$
\begin{{aligned}}
J_{{2,1}}(X)&=\frac13(P_1P_1P_2+P_1P_2P_1+P_2P_1P_1)X,\\
J_{{1,2}}(X)&=\frac13(P_1P_2P_2+P_2P_1P_2+P_2P_2P_1)X.
\end{{aligned}}
$$

Let

$$
S_{{1C}}:=\frac12(P_1C+CP_1),
\qquad
S_{{C2}}:=\frac12(CP_2+P_2C),
\qquad
C_1:=[P_1,C],
\qquad
C_2:=[C,P_2].
$$

The six mixed ordered words are therefore

$$
\begin{{aligned}}
P_1P_1P_2&=J_{{2,1}}+S_{{1C}}+\frac16C_1,
&P_1P_2P_1&=J_{{2,1}}-\frac13C_1,
&P_2P_1P_1&=J_{{2,1}}-S_{{1C}}+\frac16C_1,\\
P_1P_2P_2&=J_{{1,2}}+S_{{C2}}+\frac16C_2,
&P_2P_1P_2&=J_{{1,2}}-\frac13C_2,
&P_2P_2P_1&=J_{{1,2}}-S_{{C2}}+\frac16C_2.
\end{{aligned}}
$$

Here

$$
C=-\operatorname{{ad}}_A,
\qquad
C_1=-\operatorname{{ad}}_{{P_1A}},
\qquad
C_2=+\operatorname{{ad}}_{{P_2A}}.
$$

## 5. Pullback product

$\operatorname{{Sym}}_{{\rm PBW}}$ is not an algebra map for the ordinary commutative product:

$$
\operatorname{{Sym}}_{{\rm PBW}}(p_1p_2)
=\frac12(P_1P_2+P_2P_1)
\ne P_1P_2
=\operatorname{{Sym}}_{{\rm PBW}}(p_1)\operatorname{{Sym}}_{{\rm PBW}}(p_2).
$$

Define only the pullback product

$$
f\star g:=\operatorname{{Sym}}_{{\rm PBW}}^{{-1}}
\left(\operatorname{{Sym}}_{{\rm PBW}}(f)
\operatorname{{Sym}}_{{\rm PBW}}(g)\right).
$$

Then

$$
p_1\star p_2=p_1p_2+\frac12\ell_{{12}},
\qquad
p_2\star p_1=p_1p_2-\frac12\ell_{{12}}.
$$

The script checked exactly every homogeneous PBW-basis triple of total degree at most four:

$$
(f\star g)\star h=f\star(g\star h),
\qquad
N_{{\rm triples}}={report['star_associativity']['triples_checked']}.
$$

It also checked the defining intertwining identity on every homogeneous basis pair of total degree at most four:

$$
\operatorname{{Sym}}_{{\rm PBW}}(f\star g)
=\operatorname{{Sym}}_{{\rm PBW}}(f)\operatorname{{Sym}}_{{\rm PBW}}(g),
\qquad
N_{{\rm pairs}}={report['star_intertwining']['pairs_checked']}.
$$

## 6. Commuting-jet projection and link-completion blocker

For a commuting two-direction jet monomial $p_1^mp_2^n$, the unique curvature-free PBW lift is

$$
\operatorname{{Sym}}_{{\rm PBW}}(p_1^mp_2^n)
=\frac1{{\binom{{m+n}}{{m}}}}
\sum_{{w\in\operatorname{{Sh}}(1^m,2^n)}}P_w.
$$

Define the curvature-forgetting projection

$$
q:S(\mathfrak L)\longrightarrow\mathbb Q[p_1,p_2],
\qquad
q(\ell_w)=0\quad(|w|\ge2).
$$

For $m,n>0$, any single mixed ordered lift has an inverse PBW expansion containing at least one of
$\ell_{{12}},\ell_{{112}},\ell_{{122}},\ldots$; after the Step-3C relation these are explicit curvature words.  The map $q$ erases those words, so $q$ alone is non-injective and cannot define a bidirectional roundtrip.  A roundtrip to a commuting jet tower with no curvature generators is curvature-free before applying $q$ only for the PBW-symmetrized lift.  Thus a bilocal/Wilson/link Taylor completion must combine its connection and endpoint terms into that lift before an invertible no-extra-curvature comparison is possible.

The locked foundations contain no Wilson line, Duhamel expansion, path-ordering rule, bilocal insertion, or link-completion theorem.  Therefore the statement that the actual Step-5 link completion produces this lift is not proved here:

`{report['link_completion']['status']}`.
"""


def main() -> None:
    for relative, expected in SOURCE_FILES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)

    link_hits = []
    for relative in LOCKED_FOUNDATIONS:
        text = (ROOT / relative).read_text(encoding="utf-8").lower()
        for term in LINK_TERMS:
            if term in text:
                link_hits.append({"file": relative, "term": term})
    assert not link_hits, link_hits

    max_degree = 4
    words_by_degree = {
        degree: ["".join(bits) for bits in itertools.product("12", repeat=degree)]
        for degree in range(max_degree + 1)
    }
    lyndon_factors = [
        word
        for degree in range(1, max_degree + 1)
        for word in words_by_degree[degree]
        if is_lyndon(word)
    ]
    factor_order = {factor: index for index, factor in enumerate(lyndon_factors)}
    bracket_cache: Dict[Word, WordPoly] = {}
    brackets = {factor: standard_lyndon_bracket(factor, bracket_cache) for factor in lyndon_factors}

    expected_lyndon = ["1", "2", "12", "112", "122", "1112", "1122", "1222"]
    assert lyndon_factors == expected_lyndon, lyndon_factors

    sym_basis_by_degree: Dict[int, List[SymMonomial]] = {}
    forward_by_degree: Dict[int, List[List[Fraction]]] = {}
    inverse_by_degree: Dict[int, List[List[Fraction]]] = {}
    degree_audit = {}
    exact_matrices = {}

    for degree in range(max_degree + 1):
        words = words_by_degree[degree]
        basis = symmetric_monomials(lyndon_factors, degree)
        sym_basis_by_degree[degree] = basis
        assert len(words) == len(basis) == 2**degree
        forward = [
            [symmetrization_expand(monomial, brackets).get(word, Fraction(0)) for monomial in basis]
            for word in words
        ]
        inverse = invert_matrix(forward)
        forward_by_degree[degree] = forward
        inverse_by_degree[degree] = inverse
        left_identity = matrix_product(inverse, forward)
        right_identity = matrix_product(forward, inverse)
        assert left_identity == identity_matrix(len(words))
        assert right_identity == identity_matrix(len(words))
        degree_audit[str(degree)] = {
            "word_dimension": len(words),
            "symmetric_dimension": len(basis),
            "forward_inverse": "PASS",
            "inverse_forward": "PASS",
        }
        exact_matrices[str(degree)] = {
            "word_basis": [word or "1" for word in words],
            "symmetric_basis": [sym_name(monomial) for monomial in basis],
            "forward_rows_word_columns_symmetric": serialize_matrix(forward),
            "inverse_rows_symmetric_columns_word": serialize_matrix(inverse),
        }

    shuffle_audit = []
    for total in range(0, max_degree + 1):
        for m in range(total + 1):
            n = total - m
            monomial = tuple(sorted(("1",) * m + ("2",) * n, key=factor_order.__getitem__))
            expansion = symmetrization_expand(monomial, brackets)
            denominator = math.comb(total, m)
            assert len(expansion) == denominator
            assert set(expansion.values()) == {Fraction(1, denominator)}
            shuffle_audit.append(
                {
                    "m": m,
                    "n": n,
                    "distinct_shuffles": denominator,
                    "coefficient": fraction_string(Fraction(1, denominator)),
                }
            )

    all_basis = [
        (degree, monomial)
        for degree in range(max_degree + 1)
        for monomial in sym_basis_by_degree[degree]
    ]
    triples_checked = 0
    for degree_a, monomial_a in all_basis:
        for degree_b, monomial_b in all_basis:
            for degree_c, monomial_c in all_basis:
                if degree_a + degree_b + degree_c > max_degree:
                    continue
                a = {monomial_a: Fraction(1)}
                b = {monomial_b: Fraction(1)}
                c = {monomial_c: Fraction(1)}
                left = star_product(
                    star_product(a, b, brackets, words_by_degree, sym_basis_by_degree, inverse_by_degree),
                    c,
                    brackets,
                    words_by_degree,
                    sym_basis_by_degree,
                    inverse_by_degree,
                )
                right = star_product(
                    a,
                    star_product(b, c, brackets, words_by_degree, sym_basis_by_degree, inverse_by_degree),
                    brackets,
                    words_by_degree,
                    sym_basis_by_degree,
                    inverse_by_degree,
                )
                assert left == right, (monomial_a, monomial_b, monomial_c, left, right)
                triples_checked += 1

    pairs_checked = 0
    for degree_a, monomial_a in all_basis:
        for degree_b, monomial_b in all_basis:
            if degree_a + degree_b > max_degree:
                continue
            a = {monomial_a: Fraction(1)}
            b = {monomial_b: Fraction(1)}
            star = star_product(a, b, brackets, words_by_degree, sym_basis_by_degree, inverse_by_degree)
            left = sym_poly_expand(star, brackets)
            right = word_product(sym_poly_expand(a, brackets), sym_poly_expand(b, brackets))
            assert left == right, (monomial_a, monomial_b, left, right)
            pairs_checked += 1

    p1 = {("1",): Fraction(1)}
    p2 = {("2",): Fraction(1)}
    ordinary_p1p2 = sym_product(p1, p2, factor_order)
    star_p1p2 = star_product(p1, p2, brackets, words_by_degree, sym_basis_by_degree, inverse_by_degree)
    star_p2p1 = star_product(p2, p1, brackets, words_by_degree, sym_basis_by_degree, inverse_by_degree)
    assert star_p1p2 != ordinary_p1p2
    assert star_p1p2 == {("1", "2"): Fraction(1), ("12",): Fraction(1, 2)}
    assert star_p2p1 == {("1", "2"): Fraction(1), ("12",): Fraction(-1, 2)}

    degree_three_sym_polys = {
        word: word_poly_inverse(
            {word: Fraction(1)},
            3,
            words_by_degree,
            sym_basis_by_degree,
            inverse_by_degree,
        )
        for word in words_by_degree[3]
    }

    report = {
        "schema": "step5-target-blind-pbw-jet-audit-v1",
        "authority_base": AUTHORITY_BASE,
        "target_blind": True,
        "forbidden_reads": [
            "contracts/foundations/step-05-euclidean-n4-awi-one-loop.md",
            "scripts/step5_* other than this audit",
            "references/vendor/arxiv/2512.07771v2/*",
            "any live chat, web page, Notion page, memory, or external file",
        ],
        "source_files": list(SOURCE_FILES),
        "source_sha256": SOURCE_FILES,
        "locked_relations": {
            "epsilon_dot1_dot2": "-1",
            "rho_E": "1",
            "P_dot_a": "D^V_(E,+,dot-a)",
            "A": "nabla^V_(E,+) W^V_(E,+)",
            "commutator": "[P_dot-a,P_dot-b]=epsilon_(dot-a,dot-b) ad_A",
            "C": "[P1,P2]=-ad_A",
        },
        "lyndon_factors_through_degree_4": lyndon_factors,
        "lyndon_associative_expansions": {
            factor: serialize_word_poly(brackets[factor]) for factor in lyndon_factors
        },
        "degree_audit": degree_audit,
        "exact_pbw_matrices": exact_matrices,
        "shuffle_normalization": shuffle_audit,
        "degree_three_inverse": {
            word: serialize_sym_poly(poly) for word, poly in degree_three_sym_polys.items()
        },
        "degree_three_sym_polys": degree_three_sym_polys,
        "ordinary_product_homomorphism": {
            "status": "FAIL_AS_EXPECTED",
            "ordinary_p1p2": serialize_sym_poly(ordinary_p1p2),
            "star_p1p2": serialize_sym_poly(star_p1p2),
            "star_p2p1": serialize_sym_poly(star_p2p1),
        },
        "star_associativity": {
            "maximum_total_degree": max_degree,
            "triples_checked": triples_checked,
            "exact_rational": True,
            "status": "PASS",
        },
        "star_intertwining": {
            "maximum_total_degree": max_degree,
            "pairs_checked": pairs_checked,
            "exact_rational": True,
            "status": "PASS",
        },
        "mutation_guards": {
            "factorial_denominator_for_J_2_1": {
                "mutated_coefficient_per_shuffle": "1/6",
                "three_term_coefficient_sum": "1/2",
                "required_sum": "1",
                "status": "REJECTED",
            },
            "ordinary_product_algebra_map": "REJECTED_BY_p1_p2_COUNTEREXAMPLE",
        },
        "link_completion": {
            "searched_locked_foundations": LOCKED_FOUNDATIONS,
            "search_terms": list(LINK_TERMS),
            "matches": link_hits,
            "required_output_for_curvature_free_commuting_projection": "PBW-symmetrized jets",
            "status": "BLOCKED_LINK_COMPLETION_NOT_IN_LOCKED_INPUT",
        },
        "overall": "CONDITIONAL_PBW_PROVED_LINK_COMPLETION_BLOCKED",
    }

    json_report = dict(report)
    json_report.pop("degree_three_sym_polys")
    json_path = ROOT / "audits/step5-pbw-jet-audit.json"
    md_path = ROOT / "audits/step5-pbw-jet-audit.md"
    json_path.write_text(json.dumps(json_report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(build_markdown(report), encoding="utf-8")
    print(json.dumps({
        "overall": report["overall"],
        "degrees": degree_audit,
        "star_triples_checked": triples_checked,
        "star_pairs_checked": pairs_checked,
        "link_completion": report["link_completion"]["status"],
        "json": str(json_path.relative_to(ROOT)),
        "markdown": str(md_path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()
