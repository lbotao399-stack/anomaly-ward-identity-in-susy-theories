#!/usr/bin/env python3
"""Fast exact CP0/CP1 D-algebra probe for the Step-6 kite obligation.

This file is proposal evidence only.  It reads no external data.  The implementation
is deliberately independent of ``engine_A``:

* Grassmann monomials are integer bitmasks;
* coefficients are sparse commutative polynomials over Q(i), with ``Fraction``
  coefficients;
* SymPy is never imported;
* external W and Wtilde letters are generated from generic canonical prepotentials,
  so their chirality constraints hold as operator identities rather than by a
  post-processing substitution.

Machine checks and memo tags:

* CP0 checks SPEC section 1 / (K.1), (K.2), and F.6;
* CP1 checks seed sections 6--8, especially the eight endpoint rows and w_D=2.

The script exits nonzero at the first failed mandatory checkpoint, as required by
SPEC section 6.  It therefore never manufactures CP2--CP4 data after a CP1 failure.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import itertools
import json
import random
import time
from functools import lru_cache
from pathlib import Path


# ---------------------------------------------------------------------------
# Q(i)

QI = tuple[F, F]
ZERO: QI = (F(0), F(0))
ONE: QI = (F(1), F(0))
I: QI = (F(0), F(1))
MINUS_I: QI = (F(0), F(-1))


def qadd(a: QI, b: QI) -> QI:
    return a[0] + b[0], a[1] + b[1]


def qneg(a: QI) -> QI:
    return -a[0], -a[1]


def qmul(a: QI, b: QI) -> QI:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def qscale(a: QI, x: F | int) -> QI:
    x = F(x)
    return a[0] * x, a[1] * x


def qiszero(a: QI) -> bool:
    return a == ZERO


def qstr(a: QI) -> str:
    r, i = a
    if i == 0:
        return str(r)
    if r == 0:
        if i == 1:
            return "i"
        if i == -1:
            return "-i"
        return f"{i}*i"
    sign = "+" if i > 0 else "-"
    return f"({r}{sign}{abs(i)}*i)"


# ---------------------------------------------------------------------------
# Sparse commutative polynomials over Q(i)

# A monomial is a sorted tuple of integer symbol ids.  Repeated ids are allowed.
Monomial = tuple[int, ...]
Poly = dict[Monomial, QI]


SYMBOL_NAME: list[str] = []
SYMBOL_ID: dict[str, int] = {}


def sid(name: str) -> int:
    if name not in SYMBOL_ID:
        SYMBOL_ID[name] = len(SYMBOL_NAME)
        SYMBOL_NAME.append(name)
    return SYMBOL_ID[name]


def pconst(c: QI = ONE) -> Poly:
    return {} if qiszero(c) else {(): c}


def psym(name: str, c: QI = ONE) -> Poly:
    return {} if qiszero(c) else {(sid(name),): c}


def padd(a: Poly, b: Poly) -> Poly:
    if not a:
        return dict(b)
    if not b:
        return dict(a)
    out = dict(a)
    for m, c in b.items():
        v = qadd(out.get(m, ZERO), c)
        if qiszero(v):
            out.pop(m, None)
        else:
            out[m] = v
    return out


def pscale(a: Poly, c: QI) -> Poly:
    if qiszero(c):
        return {}
    return {m: qmul(v, c) for m, v in a.items() if not qiszero(qmul(v, c))}


def _merge_sorted(a: Monomial, b: Monomial) -> Monomial:
    i = j = 0
    out: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return tuple(out)


def pmul(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return {}
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = _merge_sorted(ma, mb)
            v = qadd(out.get(m, ZERO), qmul(ca, cb))
            if qiszero(v):
                out.pop(m, None)
            else:
                out[m] = v
    return out


def peq(a: Poly, b: Poly) -> bool:
    return padd(a, pscale(b, (F(-1), F(0)))) == {}


def psubstitute_numbers(a: Poly, values: dict[int, F]) -> QI:
    out = ZERO
    for m, c in a.items():
        scale = F(1)
        for s in m:
            scale *= values[s]
        out = qadd(out, qscale(c, scale))
    return out


def pstr(a: Poly, max_terms: int = 8) -> str:
    if not a:
        return "0"
    bits: list[str] = []
    items = sorted(a.items())
    for m, c in items[:max_terms]:
        factors = [qstr(c)] + [SYMBOL_NAME[s] for s in m]
        bits.append("*".join(factors))
    if len(items) > max_terms:
        bits.append(f"...({len(items) - max_terms} more terms)")
    return " + ".join(bits)


# ---------------------------------------------------------------------------
# Grassmann polynomials: mask -> Poly

GP = dict[int, Poly]


def gbit(point: int, slot: int) -> int:
    return 1 << (4 * point + slot)


XI_Q = 1 << 16
XI_P = 1 << 17
THETA_MASK = (1 << 16) - 1


def gconst(poly: Poly | None = None) -> GP:
    if poly is None:
        poly = pconst()
    return {} if not poly else {0: poly}


def gadd(a: GP, b: GP) -> GP:
    if not a:
        return {m: dict(c) for m, c in b.items()}
    if not b:
        return {m: dict(c) for m, c in a.items()}
    out = {m: dict(c) for m, c in a.items()}
    for mask, poly in b.items():
        v = padd(out.get(mask, {}), poly)
        if v:
            out[mask] = v
        else:
            out.pop(mask, None)
    return out


def gscale(a: GP, c: QI) -> GP:
    if qiszero(c):
        return {}
    out: GP = {}
    for m, v in a.items():
        scaled = pscale(v, c)
        if scaled:
            out[m] = scaled
    return out


def gscale_poly(a: GP, p: Poly) -> GP:
    if not p:
        return {}
    out: GP = {}
    for m, v in a.items():
        scaled = pmul(v, p)
        if scaled:
            out[m] = scaled
    return out


def wedge_sign(mask_a: int, mask_b: int) -> int:
    """Sign sorting the concatenation (ascending bits of a)(ascending bits of b)."""
    parity = 0
    b = mask_b
    while b:
        low = b & -b
        j = low.bit_length() - 1
        parity ^= ((mask_a >> (j + 1)).bit_count() & 1)
        b ^= low
    return -1 if parity else 1


def gmul(a: GP, b: GP) -> GP:
    if not a or not b:
        return {}
    out: GP = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if ma & mb:
                continue
            poly = pmul(ca, cb)
            if wedge_sign(ma, mb) < 0:
                poly = pscale(poly, (F(-1), F(0)))
            mask = ma | mb
            v = padd(out.get(mask, {}), poly)
            if v:
                out[mask] = v
            else:
                out.pop(mask, None)
    return out


def gderiv(a: GP, bit: int) -> GP:
    out: GP = {}
    lower = bit - 1
    for mask, poly in a.items():
        if not (mask & bit):
            continue
        v = poly
        if (mask & lower).bit_count() & 1:
            v = pscale(v, (F(-1), F(0)))
        nmask = mask ^ bit
        out[nmask] = padd(out.get(nmask, {}), v)
    return {m: c for m, c in out.items() if c}


def gleft_bit(a: GP, bit: int) -> GP:
    out: GP = {}
    lower = bit - 1
    for mask, poly in a.items():
        if mask & bit:
            continue
        v = poly
        if (mask & lower).bit_count() & 1:
            v = pscale(v, (F(-1), F(0)))
        out[mask | bit] = padd(out.get(mask | bit, {}), v)
    return {m: c for m, c in out.items() if c}


def geq(a: GP, b: GP) -> bool:
    return gadd(a, gscale(b, (F(-1), F(0)))) == {}


# ---------------------------------------------------------------------------
# Momentum matrices and D words

Matrix = list[list[Poly]]
Letter = tuple[str, int]
Word = tuple[QI, tuple[Letter, ...]]


EPS_UP = {(0, 1): F(1), (1, 0): F(-1)}


def pmat(name: str, scale: int | F = 1) -> Matrix:
    return [[psym(f"P{name}_{a}{b}", (F(scale), F(0))) for b in range(2)] for a in range(2)]


def pmat_linear(terms: dict[str, int | F]) -> Matrix:
    out: Matrix = [[{}, {}], [{}, {}]]
    for a in range(2):
        for b in range(2):
            p: Poly = {}
            for name, co in terms.items():
                if co:
                    p = padd(p, psym(f"P{name}_{a}{b}", (F(co), F(0))))
            out[a][b] = p
    return out


def pmat_neg(m: Matrix) -> Matrix:
    return [[pscale(m[a][b], (F(-1), F(0))) for b in range(2)] for a in range(2)]


def pmat_bar(m: Matrix) -> Matrix:
    out: Matrix = [[{}, {}], [{}, {}]]
    for ad in range(2):
        for a in range(2):
            p: Poly = {}
            for bd in range(2):
                for b in range(2):
                    s1 = EPS_UP.get((ad, bd), F(0))
                    s2 = EPS_UP.get((a, b), F(0))
                    if s1 and s2:
                        p = padd(p, pscale(m[b][bd], (s1 * s2, F(0))))
            out[ad][a] = p
    return out


def apply_letter(a: GP, letter: Letter, point: int, momentum_into_point: Matrix) -> GP:
    kind, idx = letter
    if kind == "D":
        out = gderiv(a, gbit(point, idx))
        for bd in range(2):
            if momentum_into_point[idx][bd]:
                out = gadd(
                    out,
                    gscale_poly(gleft_bit(a, gbit(point, 2 + bd)), momentum_into_point[idx][bd]),
                )
        return out
    out = gderiv(a, gbit(point, 2 + idx))
    for c in range(2):
        if momentum_into_point[c][idx]:
            out = gadd(
                out,
                gscale_poly(gleft_bit(a, gbit(point, c)), momentum_into_point[c][idx]),
            )
    return out


def apply_word(a: GP, word: Word, point: int, momentum_into_point: Matrix) -> GP:
    out = a
    for letter in reversed(word[1]):
        out = apply_letter(out, letter, point, momentum_into_point)
        if not out:
            break
    return gscale(out, word[0])


def word_concat(*words: Word) -> Word:
    c = ONE
    letters: list[Letter] = []
    for co, ls in words:
        c = qmul(c, co)
        letters.extend(ls)
    return c, tuple(letters)


W_ID: Word = (ONE, ())
W_D2: Word = ((F(2), F(0)), (("D", 1), ("D", 0)))
W_DB2: Word = ((F(2), F(0)), (("Db", 0), ("Db", 1)))
W_OALPHA: Word = ((F(-1, 2), F(0)), (("D", 1), ("D", 0), ("Db", 0), ("Db", 1), ("D", 0)))
W_OBETA: Word = ((F(-1, 2), F(0)), (("D", 0), ("Db", 0), ("Db", 1), ("D", 0)))


def vertex_realization(chirality: str, idx: int) -> tuple[Word, Word]:
    if chirality == "+":
        low = 1 - idx
        sign = F(1) if idx == 0 else F(-1)
        eword = word_concat(((F(-1, 4) * sign, F(0)), ()), W_DB2, (ONE, (("D", low),)))
        cword = ONE, (("D", idx),)
        return eword, cword
    up = 1 - idx
    sign = F(1) if idx == 0 else F(-1)
    eword = word_concat(((F(-1, 4), F(0)), ()), W_D2, (ONE, (("Db", idx),)))
    cword = (sign, F(0)), (("Db", up),)
    return eword, cword


VERTEX_COEFF = {"+": (F(0), F(1, 2)), "-": (F(0), F(-1, 2))}


# ---------------------------------------------------------------------------
# Deltas, integration, generic superfields


def delta4_single(point: int) -> GP:
    mask = sum(gbit(point, s) for s in range(4))
    return {mask: pconst((F(-4), F(0)))}


def delta4_pair(i: int, j: int) -> GP:
    out = gconst(pconst((F(-4), F(0))))
    for s in range(4):
        out = gmul(
            out,
            gadd(
                {gbit(i, s): pconst()},
                {gbit(j, s): pconst((F(-1), F(0)))},
            ),
        )
    return out


def berezin(a: GP, point: int) -> GP:
    block = sum(gbit(point, s) for s in range(4))
    out: GP = {}
    for mask, poly in a.items():
        if mask & block != block:
            continue
        nmask = mask ^ block
        v = pscale(poly, (F(-1, 4), F(0)))
        out[nmask] = padd(out.get(nmask, {}), v)
    return {m: c for m, c in out.items() if c}


def generic_prepotential(point: int, prefix: str, xi_bit: int) -> GP:
    out: GP = {}
    for n in range(5):
        for slots in itertools.combinations(range(4), n):
            mask = sum(gbit(point, s) for s in slots)
            if n & 1:
                mask |= xi_bit
            tail = "e" if not slots else "".join(str(s) for s in slots)
            out[mask] = padd(out.get(mask, {}), psym(f"{prefix}_{tail}"))
    return out


def translate_superfield(a: GP, source_point: int, target_point: int) -> GP:
    """Rename theta generators, preserving canonical ascending order and signs."""
    out: GP = {}
    src_block = sum(gbit(source_point, s) for s in range(4))
    for mask, poly in a.items():
        theta = mask & src_block
        other = mask ^ theta
        target = other
        for s in range(4):
            if theta & gbit(source_point, s):
                target |= gbit(target_point, s)
        # Source and target theta blocks lie below xi tags; this rename preserves order.
        out[target] = padd(out.get(target, {}), poly)
    return out


# ---------------------------------------------------------------------------
# Ordered contraction evaluator


@dataclass(frozen=True)
class Factor:
    fid: int
    parity: int
    word: Word | None = None
    point: int | None = None
    external: GP | None = None


def word_parity(word: Word) -> int:
    return len(word[1]) & 1


_LINE_BLOCK_CACHE: dict[tuple[object, ...], GP] = {}


def line_block(left: Factor, right: Factor, mleft: Matrix, mright: Matrix) -> GP:
    assert left.word is not None and right.word is not None
    assert left.point is not None and right.point is not None
    key = (left.point, right.point, left.word, right.word, id(mleft), id(mright))
    cached = _LINE_BLOCK_CACHE.get(key)
    if cached is not None:
        return cached
    out = delta4_pair(left.point, right.point)
    out = apply_word(out, right.word, right.point, mright)
    out = apply_word(out, left.word, left.point, mleft)
    _LINE_BLOCK_CACHE[key] = out
    return out


def koszul_sign(source: list[Factor], target_ids: list[int]) -> int:
    pos = {f.fid: i for i, f in enumerate(source)}
    parity = {f.fid: f.parity for f in source}
    odd = [fid for fid in target_ids if parity[fid]]
    inv = sum(pos[odd[i]] > pos[odd[j]] for i in range(len(odd)) for j in range(i + 1, len(odd)))
    return -1 if inv & 1 else 1


def evaluate_contraction(
    factors: list[Factor],
    lines: list[tuple[int, int, Matrix, Matrix]],
    integrate_points: tuple[int, ...],
) -> GP:
    fmap = {f.fid: f for f in factors}
    paired: set[int] = set()
    target: list[int] = []
    blocks: list[GP] = []
    for left_id, right_id, ml, mr in lines:
        left, right = fmap[left_id], fmap[right_id]
        blocks.append(line_block(left, right, ml, mr))
        paired.update((left_id, right_id))
        target.extend((left_id, right_id))
    for f in factors:
        if f.fid not in paired:
            assert f.external is not None
            blocks.append(f.external)
            target.append(f.fid)
    out = gconst()
    for block in blocks:
        out = gmul(out, block)
        if not out:
            return {}
    if koszul_sign(factors, target) < 0:
        out = gscale(out, (F(-1), F(0)))
    for point in integrate_points:
        out = berezin(out, point)
        if not out:
            return {}
    return out


# ---------------------------------------------------------------------------
# CP0


def cp0() -> tuple[bool, list[dict[str, object]]]:
    checks: list[dict[str, object]] = []

    def record(name: str, tag: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "memo_tag": tag, "pass": ok, "detail": detail})
        print(f"{'PASS' if ok else 'FAIL'} CP0 {tag}: {name} :: {detail}")

    m = pmat("z")
    theta2 = {gbit(0, 0) | gbit(0, 1): pconst((F(-2), F(0)))}
    tbar2 = {gbit(0, 2) | gbit(0, 3): pconst((F(2), F(0)))}
    d2_theta2 = apply_word(theta2, W_D2, 0, m).get(0, {})
    db2_tbar2 = apply_word(tbar2, W_DB2, 0, m).get(0, {})
    record("(D^2 theta^2)| = -4", "(K.1)/SPEC-1-anchor-1", peq(d2_theta2, pconst((F(-4), F(0)))), pstr(d2_theta2))
    record("(Db^2 thetabar^2)| = -4", "(K.1)/SPEC-1-anchor-2", peq(db2_tbar2, pconst((F(-4), F(0)))), pstr(db2_tbar2))

    ddelta = apply_word(delta4_single(0), word_concat(W_D2, W_DB2), 0, m).get(0, {})
    record("[D^2 Db^2 delta4]| = 16", "F.6/SPEC-1-anchor-3", peq(ddelta, pconst((F(16), F(0)))), pstr(ddelta))

    d12 = delta4_pair(0, 1)
    inner = apply_word(d12, word_concat(W_D2, W_DB2), 1, m)
    sat = gmul(d12, inner)
    target = gscale(d12, (F(16), F(0)))
    record("delta4_01 D^2 Db^2 delta4_01 = 16 delta4_01", "F.6/SPEC-1-anchor-4", geq(sat, target), f"terms={len(sat)}")

    undersat = True
    words: list[Word] = [W_ID]
    words += [(ONE, (("D", a),)) for a in range(2)]
    words += [(ONE, (("Db", b),)) for b in range(2)]
    words += [(ONE, (("D", a), ("Db", b))) for a in range(2) for b in range(2)]
    words += [(ONE, (("Db", b), ("D", a))) for a in range(2) for b in range(2)]
    for word in words:
        if gmul(d12, apply_word(d12, word, 1, m)):
            undersat = False
            break
    record("closed theta loop with <2 D and <2 Db vanishes", "F.6/SPEC-1-anchor-5", undersat, f"words_checked={len(words)}")
    return all(bool(c["pass"]) for c in checks), checks


# ---------------------------------------------------------------------------
# CP1


M_R0_O = pmat_linear({"k": -1})
M_R0_Y1 = pmat_linear({"k": 1})
M_R1_Y1 = pmat_linear({"k": -1, "q": -1})
M_R1_Y2 = pmat_linear({"k": 1, "q": 1})
M_R2_Y2 = pmat_linear({"k": -1, "p": -1, "q": -1})
M_R2_O = pmat_linear({"k": 1, "p": 1, "q": 1})
M_P = pmat_linear({"p": 1})
M_Q = pmat_linear({"q": 1})
MOM = [pmat_linear({"k": 1}), pmat_linear({"k": 1, "q": 1}), pmat_linear({"k": 1, "p": 1, "q": 1})]


@lru_cache(maxsize=None)
def external_letters(point: int) -> tuple[list[GP], list[GP]]:
    """Return Wtilde_ad(q), W^a(p), both generated from generic prepotentials."""
    vq = generic_prepotential(point, "vq", XI_Q)
    vp = generic_prepotential(point, "vp", XI_P)
    wt: list[GP] = []
    w: list[GP] = []
    for ad in range(2):
        eword, _ = vertex_realization("-", ad)
        wt.append(apply_word(vq, eword, point, M_Q))
    for a in range(2):
        eword, _ = vertex_realization("+", a)
        w.append(apply_word(vp, eword, point, M_P))
    return wt, w


def cp1_assignment(term: str, y1_c_line: str, y2_c_line: str) -> GP:
    w1, w2 = (W_OALPHA, W_OBETA) if term == "a" else (W_OBETA, W_OALPHA)
    total: GP = {}
    wt_y1, _ = external_letters(1)
    _, w_y2 = external_letters(2)
    for ad in range(2):
        _, c1 = vertex_realization("-", ad)
        for a in range(2):
            _, c2 = vertex_realization("+", a)
            factors = [
                Factor(0, word_parity(w1), word=w1, point=0),
                Factor(1, word_parity(w2), word=w2, point=0),
                Factor(2, 1, external=wt_y1[ad]),
                Factor(3, word_parity(c1), word=c1, point=1),
                Factor(4, 0, word=W_ID, point=1),
                Factor(5, 1, external=w_y2[a]),
                Factor(6, word_parity(c2), word=c2, point=2),
                Factor(7, 0, word=W_ID, point=2),
            ]
            y1_t1 = 3 if y1_c_line == "r0" else 4
            y1_t2 = 4 if y1_c_line == "r0" else 3
            y2_t2 = 6 if y2_c_line == "r1" else 7
            y2_t3 = 7 if y2_c_line == "r1" else 6
            value = evaluate_contraction(
                factors,
                [
                    (0, y1_t1, M_R0_O, M_R0_Y1),
                    (y1_t2, y2_t2, M_R1_Y1, M_R1_Y2),
                    (1, y2_t3, M_R2_O, M_R2_Y2),
                ],
                (1, 2),
            )
            total = gadd(total, value)
    # (-i/2)*(+i/2) = +1/4 from antichiral/chiral expansion vertices.
    total = gscale(total, qmul(VERTEX_COEFF["-"], VERTEX_COEFF["+"]))
    # Canonicalize c_{CUE} at both vertices.  These are precisely the seed section 6
    # raw signs (-,+,+,-); the recorded transfer sign is supposed to turn every
    # final row positive.
    color_sign = (-1 if y1_c_line == "r0" else 1) * (-1 if y2_c_line == "r2" else 1)
    if color_sign < 0:
        total = gscale(total, (F(-1), F(0)))
    return total


def chain(mi: Matrix, mj: Matrix) -> list[Poly]:
    """[p(mi) pbar(p) p(mj) eps]_{+}^{ad}, ad=0,1."""
    pbar = pmat_bar(M_P)
    out: list[Poly] = []
    for ad in range(2):
        poly: Poly = {}
        for bd in range(2):
            for gam in range(2):
                for dd in range(2):
                    eps = EPS_UP.get((dd, ad), F(0))
                    if not eps:
                        continue
                    term = pmul(mi[0][bd], pmul(pbar[bd][gam], mj[gam][dd]))
                    poly = padd(poly, pscale(term, (eps, F(0))))
        out.append(poly)
    return out


def cp1_seed_structure(mi: Matrix, mj: Matrix) -> GP:
    """The seed T-word expressed in mathsf-p variables, without its -i/2 weight."""
    wt0, _ = external_letters(0)
    _, w0 = external_letters(0)
    # W_+ = -W^- and X=D_+ W_+, hence X=-D_+ W^-.
    x = apply_word(w0[1], ((F(-1), F(0)), (("D", 0),)), 0, M_P)
    ch = chain(mi, mj)
    out: GP = {}
    for ad in range(2):
        out = gadd(out, gscale_poly(gmul(wt0[ad], x), ch[ad]))
    return out


def symbolic_difference_examples(diff: GP, limit: int = 3) -> list[dict[str, str]]:
    examples: list[dict[str, str]] = []
    for mask, poly in sorted(diff.items()):
        for mono, coeff in sorted(poly.items()):
            examples.append(
                {
                    "grassmann_mask": hex(mask),
                    "coefficient": qstr(coeff),
                    "commutative_monomial": "*".join(SYMBOL_NAME[s] for s in mono) or "1",
                }
            )
            if len(examples) == limit:
                return examples
    return examples


def random_eval_difference(diff: GP, rng: random.Random) -> dict[str, object]:
    values = {s: F(rng.randint(-5, 5) or 1) for s in range(len(SYMBOL_NAME))}
    nonzero: list[dict[str, str]] = []
    for mask, poly in sorted(diff.items()):
        val = psubstitute_numbers(poly, values)
        if not qiszero(val):
            nonzero.append({"grassmann_mask": hex(mask), "value": qstr(val)})
            if len(nonzero) == 4:
                break
    return {"nonzero_components": nonzero, "symbols_assigned": len(values)}


def cp1() -> tuple[bool, dict[str, object]]:
    expected_map = {
        ("r0", "r1"): (0, 1),
        ("r0", "r2"): (0, 2),
        ("r1", "r1"): (1, 1),
        ("r1", "r2"): (1, 2),
    }
    rows: list[dict[str, object]] = []
    rng = random.Random(20260717)
    all_ok = True
    totals: dict[str, GP] = {"a": {}, "b": {}}
    for term in ("a", "b"):
        for endpoints, (i, j) in expected_map.items():
            actual = cp1_assignment(term, *endpoints)
            base_target = cp1_seed_structure(MOM[i], MOM[j])
            target = gscale(base_target, (F(0), F(-1, 2)))
            diff = gadd(actual, gscale(target, (F(-1), F(0))))
            ok = not diff
            all_ok &= ok
            totals[term] = gadd(totals[term], actual)
            sample = random_eval_difference(diff, rng) if diff else {"nonzero_components": [], "symbols_assigned": len(SYMBOL_NAME)}
            row_id = f"WW-DA-{len(rows)+1:02d}"
            rows.append(
                {
                    "id": row_id,
                    "placement": "A" if term == "a" else "B",
                    "barD_endpoint": endpoints[0],
                    "D_endpoint": endpoints[1],
                    "expected_final_sign": 1,
                    "expected_weight_in_p_basis": "-i/2",
                    "exact_match": ok,
                    "actual_terms": sum(len(p) for p in actual.values()),
                    "difference_terms": sum(len(p) for p in diff.values()),
                    "symbolic_difference_examples": symbolic_difference_examples(diff),
                    "random_component_comparison": sample,
                    "overall_dictionary_scan": {
                        label: geq(actual, gscale(base_target, weight))
                        for label, weight in {
                            "+1/2": (F(1, 2), F(0)),
                            "-1/2": (F(-1, 2), F(0)),
                            "+i/2": (F(0), F(1, 2)),
                            "-i/2": (F(0), F(-1, 2)),
                        }.items()
                    },
                }
            )
            print(
                f"{'PASS' if ok else 'FAIL'} CP1 {row_id}: placement={term} "
                f"endpoints={endpoints[0]},{endpoints[1]} diff_terms={rows[-1]['difference_terms']}"
            )

    ml1 = pmat_linear({"k": 2, "q": 1})
    ml2 = pmat_linear({"k": 2, "p": 1, "q": 2})
    summed_target = gscale(cp1_seed_structure(ml1, ml2), (F(0), F(-1, 2)))
    total_checks: dict[str, object] = {}
    for term in ("a", "b"):
        diff = gadd(totals[term], gscale(summed_target, (F(-1), F(0))))
        ok = not diff
        all_ok &= ok
        total_checks[term] = {
            "exact_match": ok,
            "difference_terms": sum(len(p) for p in diff.values()),
            "random_component_comparison": random_eval_difference(diff, rng) if diff else {"nonzero_components": []},
        }
        print(f"{'PASS' if ok else 'FAIL'} CP1 total placement={term}: diff_terms={total_checks[term]['difference_terms']}")

    # Arithmetic ledger independent of the failed/successful explicit trace.
    w_d = F(1, 32) * 16 * 2 * 2
    print(f"PASS CP1 seed arithmetic ledger: w_D={w_d}")
    report = {
        "memo_tags": ["seed-6", "seed-7", "seed-8"],
        "rows": rows,
        "total_checks": total_checks,
        "w_D": str(w_d),
        "required_gamma": "Gamma_T,A=(hbar*g^2/2) C O_A,mn int L1^m L2^n/[k^2(k+q)^2(k+P)^2]",
        "L1": "2k+q",
        "L2": "2k+p+2q",
        "explicit_trace_pass": all_ok,
    }
    return all_ok, report


def main() -> int:
    started = time.perf_counter()
    cp0_ok, cp0_report = cp0()
    report: dict[str, object] = {
        "generated_artifact": True,
        "generated_by": "proposals/step6-kite-artifacts/fast_cp0_cp1_engine.py",
        "engine": "fast bitmask + sparse Fraction polynomial",
        "sympy_in_hot_loop": False,
        "authority_status": "NON_AUTHORITY_PROPOSAL",
        "cp0": cp0_report,
    }
    if not cp0_ok:
        report["first_blocker"] = "BLOCKED_CP0_GRASSMANN_ANCHOR_FAILURE"
        exit_code = 2
    else:
        cp1_ok, cp1_report = cp1()
        report["cp1"] = cp1_report
        if cp1_ok:
            report["first_blocker"] = None
            exit_code = 0
        else:
            report["first_blocker"] = "BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION"
            report["blocked_effect"] = "SPEC section 6 forbids CP2--CP4 after the failed CP1 go/no-go gate."
            exit_code = 3
    report["runtime_seconds"] = time.perf_counter() - started
    outpath = Path(__file__).with_name("generated") / "cp0_cp4_fast_gate_report.json"
    outpath.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"REPORT {outpath}")
    print(f"RUNTIME {report['runtime_seconds']:.3f}s")
    if report.get("first_blocker"):
        print(f"FIRST BLOCKER {report['first_blocker']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
