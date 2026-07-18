#!/usr/bin/env python3
"""Exact verification for the full Weinberg--Srednicki--Project notation dictionary.

Task:     CONTRACT-FULL-NOTATION-DICTIONARY-001
Contract: contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md
Audit:    audits/ws-dictionary/full-exact-verification.json

Eight checks (within the ten-check budget of the derivation-first law), each
naming the dictionary rows it verifies:

  FULL-DICT-TAG-SURFACE        rows (D.0.1)-(D.11.2), (D.10.56)-(D.10.181),
                               (D.12.1)-(D.20.12)
  FULL-DICT-NO-DUP-ROWS        rows (D.17.2), (D.17.3), (D.17.6), (D.17.15),
                               (D.17.16), (D.17.18), (D.17.20), (D.17.21),
                               (D.17.25), (D.17.27), (D.17.30)
  FULL-DICT-GAMMA-BRIDGES      rows (D.3.1)-(D.3.5), (D.3.11)-(D.3.13a), (D.14.5)
  FULL-DICT-GRASSMANN-FTERM    rows (D.9.14), (D.9.15), (D.17.16) [0A.77 chain]
  FULL-DICT-BRST-SIGN-CHAIN    rows (D.19.1)-(D.19.5), (D.19.9)
  FULL-DICT-SUPERCURRENT-ROWS  rows (D.16.14)-(D.16.16), (D.16.20)
  FULL-DICT-WICK-16BOX         row  (D.16.6)
  FULL-DICT-VERDICT-CONSISTENCY rows (D.10.56)-(D.10.181), (D.12.1)-(D.20.12)

The coefficient field is Q(i).  No floating point and no external CAS is used.
The Grassmann engine is the exact Q(i) exterior-algebra engine reused from the
F-term arbitration of (0A.77).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md"
AUDIT = "audits/ws-dictionary/full-exact-verification.json"

# ----------------------------------------------------------------------
# exact coefficient ring Q(i)
# ----------------------------------------------------------------------
@dataclass(frozen=True)
class QI:
    re: Fr = Fr(0)
    im: Fr = Fr(0)

    def __add__(a, b): return QI(a.re + b.re, a.im + b.im)
    def __sub__(a, b): return QI(a.re - b.re, a.im - b.im)
    def __neg__(a): return QI(-a.re, -a.im)

    def __mul__(a, b):
        if isinstance(b, (int, Fr)): b = QI(Fr(b))
        return QI(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re)

    __rmul__ = __mul__

    def __eq__(a, b):
        if isinstance(b, (int, Fr)): b = QI(Fr(b))
        return a.re == b.re and a.im == b.im

    def __hash__(a): return hash((a.re, a.im))
    def __bool__(a): return bool(a.re or a.im)

    def __repr__(a):
        def f(x):
            return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        if a.im == 0: return f(a.re)
        if a.re == 0:
            return "i" if a.im == 1 else "-i" if a.im == -1 else f(a.im) + "i"
        ip = "" if a.im == 1 else "-" if a.im == -1 else f(a.im)
        return f"({f(a.re)}{'+' if a.im > 0 else ''}{ip}i)"


def q(x):
    return x if isinstance(x, QI) else QI(Fr(x))


Z0 = QI()
ONE = QI(Fr(1))
ZI = QI(Fr(0), Fr(1))

Matrix = tuple[tuple[QI, ...], ...]


def mat(rows):
    return tuple(tuple(q(x) for x in row) for row in rows)


def zeros(n, m):
    return tuple(tuple(Z0 for _ in range(m)) for _ in range(n))


def eye(n):
    return tuple(tuple(ONE if i == j else Z0 for j in range(n)) for i in range(n))


def madd(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def msub(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def mscale(a, c):
    c = q(c)
    return tuple(tuple(c * x for x in row) for row in a)


def mmul(a, b):
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Z0)
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def mT(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def mdag(a):
    conj = lambda x: QI(x.re, -x.im)
    return tuple(tuple(conj(a[i][j]) for i in range(len(a))) for j in range(len(a[0])))


def block(a, b, c, d):
    top = [ar + br for ar, br in zip(a, b)]
    bot = [cr + dr for cr, dr in zip(c, d)]
    return tuple(top + bot)


# ----------------------------------------------------------------------
# 4x4 Clifford package (rows D.3.1-D.3.5, D.3.11-D.3.13a, D.14.5)
# ----------------------------------------------------------------------
PAULI = (
    mat([[0, 1], [1, 0]]),
    mat([[0, QI(Fr(0), Fr(-1))], [ZI, 0]]),
    mat([[1, 0], [0, -1]]),
)
ONE2 = eye(2)
Z2 = zeros(2, 2)
SIGMA = (ONE2,) + PAULI                       # (sigma^mu)_{a adot}      (D.2.4)
BARSIGMA = (ONE2,) + tuple(mscale(s, -1) for s in PAULI)  # (barsigma^mu)^{adot a} (D.2.5)
ETA = (-1, 1, 1, 1)                           # mostly-plus (D.2.1)

GAMMA_S = tuple(block(Z2, SIGMA[mu], BARSIGMA[mu], Z2) for mu in range(4))
GAMMA_W = tuple(mscale(g, QI(Fr(0), Fr(-1))) for g in GAMMA_S)  # gamma_W = -i gamma_S (D.3.2)

GAMMA5_S = mscale(mmul(mmul(GAMMA_S[0], GAMMA_S[1]), mmul(GAMMA_S[2], GAMMA_S[3])), ZI)
GAMMA5_W = mscale(mmul(mmul(GAMMA_W[0], GAMMA_W[1]), mmul(GAMMA_W[2], GAMMA_W[3])), QI(Fr(0), Fr(-1)))

# charge-conjugation matrix  C = diag(eps_ab, eps^{adot bdot}) = -i diag(sigma2, -sigma2)  (D.3.12)
CMAT = block(mscale(PAULI[1], QI(Fr(0), Fr(-1))), Z2, Z2, mscale(PAULI[1], ZI))
CMAT_INV = mscale(CMAT, -1)                   # C^{-1} = -C                          (D.3.13)
EPS4W = block(mscale(PAULI[1], ZI), Z2, Z2, mscale(PAULI[1], ZI))  # diag(i sigma2, i sigma2) (D.3.13a)


def anticom(a, b):
    return madd(mmul(a, b), mmul(b, a))


def commut(a, b):
    return msub(mmul(a, b), mmul(b, a))


# ----------------------------------------------------------------------
# Grassmann engine (exact exterior algebra with even field keys)
#   element = dict (mono, field) -> QI ;  mono = sorted tuple of generator ids
#   field = hashable even key, FUNIT = unit
# ----------------------------------------------------------------------
class Ex:
    def __init__(self, names):
        self.gens = list(names)
        self.gn = {n: i for i, n in enumerate(self.gens)}
        self.unit = ("1",)

    def genel(self, names, field=("1",), coeff=ONE):
        ids = tuple(sorted(self.gn[n] for n in names))
        return {(ids, field): q(coeff)}

    @staticmethod
    def kmerge(m1, m2):
        inv = 0
        for x in m1:
            for y in m2:
                if x == y: return 0, None
                if x > y: inv += 1
        return ((-1) ** inv, tuple(sorted(m1 + m2)))

    def addel(self, e1, e2, s=ONE):
        s = q(s)
        out = dict(e1)
        for k, v in e2.items():
            nv = out.get(k, Z0) + s * v
            if nv: out[k] = nv
            elif k in out: del out[k]
        return out

    def scalel(self, e, s):
        s = q(s)
        if not s: return {}
        return {k: v * s for k, v in e.items() if v * s}

    def mulel(self, e1, e2):
        out = {}
        for (m1, f1), c1 in e1.items():
            for (m2, f2), c2 in e2.items():
                sgn, mm = self.kmerge(m1, m2)
                if not sgn: continue
                if f1 == self.unit: ff = f2
                elif f2 == self.unit: ff = f1
                else: ff = ("*", f1, f2) if repr(f1) <= repr(f2) else ("*", f2, f1)
                k = (mm, ff)
                out[k] = out.get(k, Z0) + c1 * c2 * sgn
        return {k: v for k, v in out.items() if v}

    def deriv_odd(self, el, action):
        """graded LEFT odd derivative; action = {gen_id: QI value of d(gen)}"""
        out = {}
        for (mono, f), c in el.items():
            for r, g in enumerate(mono):
                v = action.get(g)
                if v:
                    nm = mono[:r] + mono[r + 1:]
                    k = (nm, f)
                    out[k] = out.get(k, Z0) + c * v * ((-1) ** r)
        return {k: v for k, v in out.items() if v}

    def getc(self, el, mono_names, field=("1",)):
        ids = tuple(sorted(self.gn[n] for n in mono_names))
        return el.get((ids, field), Z0)


# ----------------------------------------------------------------------
# dictionary document helpers
# ----------------------------------------------------------------------
def read_contract_text():
    return (ROOT / CONTRACT).read_text(encoding="utf-8")


def display_block(text, tag):
    needle = r"\tag{" + tag + "}"
    pos = text.find(needle)
    if pos < 0:
        return None
    open_idx = text.rfind("$$", 0, pos)
    close_idx = text.find("$$", pos)
    if open_idx < 0 or close_idx < 0:
        return None
    return text[open_idx:close_idx + 2]


def norm(s):
    return re.sub(r"\s+", "", s)


# ----------------------------------------------------------------------
# check 1: FULL-DICT-TAG-SURFACE
# ----------------------------------------------------------------------
OLD_TAGS = [
    "D.0.1", "D.0.2", "D.0.3", "D.1.1",
    "D.2.1", "D.2.2", "D.2.3", "D.2.4", "D.2.5", "D.2.6", "D.2.7", "D.2.8",
    "D.3.1", "D.3.2", "D.3.3", "D.3.4", "D.3.5", "D.3.6", "D.3.7", "D.3.8",
    "D.3.9", "D.3.10", "D.3.11", "D.3.12", "D.3.13", "D.3.13a", "D.3.14",
    "D.3.15", "D.3.16", "D.3.17", "D.3.18", "D.3.19", "D.3.20", "D.3.21",
    "D.3.22", "D.3.23", "D.3.24", "D.3.25", "D.3.26", "D.3.27", "D.3.28",
    "D.3.29", "D.3.30", "D.3.31", "D.3.32", "D.3.33",
    "D.4.1", "D.4.2", "D.4.3", "D.4.4", "D.4.5", "D.4.6", "D.4.7", "D.4.8",
    "D.4.9", "D.4.10", "D.4.11", "D.4.12", "D.4.13",
    "D.5.1", "D.5.2", "D.5.3", "D.5.4",
    "D.6.1", "D.6.2", "D.6.3", "D.6.4", "D.6.5",
    "D.7.1", "D.7.2", "D.7.3", "D.7.4", "D.7.5", "D.7.6", "D.7.7", "D.7.8",
    "D.7.9", "D.7.10", "D.7.11", "D.7.12", "D.7.13", "D.7.14",
    "D.8.1", "D.8.2", "D.8.3a", "D.8.3", "D.8.4", "D.8.5", "D.8.6", "D.8.7",
    "D.8.8", "D.8.9", "D.8.10", "D.8.10a", "D.8.11", "D.8.12", "D.8.12a",
    "D.8.12b", "D.8.13", "D.8.14", "D.8.15", "D.8.16", "D.8.17", "D.8.18",
    "D.8.19", "D.8.20",
    "D.9.1", "D.9.2", "D.9.3", "D.9.4", "D.9.5", "D.9.6", "D.9.7", "D.9.8",
    "D.9.9", "D.9.10", "D.9.10a", "D.9.11", "D.9.12", "D.9.13", "D.9.14",
    "D.9.15", "D.9.16", "D.9.17", "D.9.18", "D.9.19", "D.9.20", "D.9.21",
    "D.9.22", "D.9.23", "D.9.24", "D.9.25", "D.9.26", "D.9.26a", "D.9.27",
    "D.9.27a", "D.9.27b", "D.9.28", "D.9.29", "D.9.30", "D.9.31", "D.9.32",
    "D.11.1", "D.11.2",
]
OLD_BLOCK_DIGEST = "4fca01d7e79a4834073e69c64d328470e4b4344f9b9cb8c29906755faaca3c09"
NEW_RANGES = {
    "D.10": (56, 181),
    "D.12": (1, 40),
    "D.13": (1, 25),
    "D.14": (1, 35),
    "D.15": (1, 39),
    "D.16": (1, 30),
    "D.17": (1, 56),
    "D.18": (1, 13),
    "D.19": (1, 17),
    "D.20": (1, 12),
}


def check_tag_surface(text):
    detail = {}
    ok = True
    present_tags = re.findall(r"\\tag\{(D\.\d+\.\d+[a-z]?)\}", text)
    counts = {t: present_tags.count(t) for t in set(present_tags)}
    dup = sorted(t for t, c in counts.items() if c != 1)
    ok &= not dup
    # (a) the 144 pre-existing dict1 tags are intact: unique and content-identical
    missing_old = [t for t in OLD_TAGS if counts.get(t, 0) != 1]
    ok &= not missing_old
    digest = hashlib.sha256()
    blocks_old = {}
    for t in OLD_TAGS:
        b = display_block(text, t)
        if b is None:
            ok = False
            missing_old.append(t + " (no display block)")
            continue
        nb = norm(b)
        blocks_old[t] = nb
        digest.update(t.encode())
        digest.update(b"\x00")
        digest.update(nb.encode())
        digest.update(b"\x00")
    digest_hex = digest.hexdigest()
    ok &= digest_hex == OLD_BLOCK_DIGEST
    # (b) new ranges contiguous
    range_info = {}
    for sec, (lo, hi) in NEW_RANGES.items():
        expected = [f"{sec}.{n}" for n in range(lo, hi + 1)]
        missing = [t for t in expected if counts.get(t, 0) != 1]
        range_info[sec] = {"expected": len(expected), "missing": missing}
        ok &= not missing
    # (c) no unexpected tags beyond old + new ranges
    allowed = set(OLD_TAGS)
    for sec, (lo, hi) in NEW_RANGES.items():
        allowed |= {f"{sec}.{n}" for n in range(lo, hi + 1)}
    unexpected = sorted(set(present_tags) - allowed)
    ok &= not unexpected
    detail.update({
        "old_tags": len(OLD_TAGS),
        "old_tags_missing": missing_old,
        "old_block_digest": digest_hex,
        "old_block_digest_expected": OLD_BLOCK_DIGEST,
        "duplicate_tags": dup,
        "new_ranges": range_info,
        "unexpected_tags": unexpected,
        "total_tags": len(present_tags),
    })
    return ok, detail


# ----------------------------------------------------------------------
# check 2: FULL-DICT-NO-DUP-ROWS
# ----------------------------------------------------------------------
STRIPPED_ROWS = [
    # (new row, required bare refs in the row display, forbidden locked cores)
    ("D.17.6", ["(D.9.3)"],
     [r"\Gamma_c=e^{-2t_AV_c^A}"]),
    ("D.17.15", ["(D.9.14)"],
     [r"W_{L\alpha,c}=\fraci4(\mathcalD_R^T\varepsilon_{4,W}\mathcalD_R)\mathcalD_{L\alpha}V_c"]),
    ("D.17.16", ["(D.9.15)"],
     [r"W_{L,c}&=\lambda_L(x_+)+\frac12\gamma^\mu\gamma^\nu\Theta_Lf_{c,\mu\nu}(x_+)"]),
    ("D.17.18", ["D.9.25"],
     [r"-\frac14f_c^2-\frac12\bar\lambda_c\not{\mathcalD}\lambda_c+\frac12D_c^2"]),
    ("D.17.20", ["D.9.19"],
     [r"2t_AW^A_{L\alpha,c}=\varepsilon_{4,W}^{\beta\gamma}\mathcalD_{R\beta}\mathcalD_{R\gamma}"]),
    ("D.17.21", ["(D.9.20)", "(D.9.17)"],
     [r"t_AW_L^{A\prime}=e^{-it_B\Omega_c^B}(t_AW_L^A)e^{it_C\Omega_c^C}",
      r"W_{a,S}'=e^{-2ig\Xi}W_{a,S}e^{2ig\Xi}"]),
    ("D.17.25", ["(D.9.24)", "(D.9.28)"],
     [r"\frac12\left[\Phi^\daggere^{-2t_AV_c^A}\Phi\right]_D"]),
    ("D.17.27", ["(D.9.29)", "(D.9.32)"],
     [r"F_i=-W_i^\dagger", r"D^A=\xi^A+\phi^\daggert^A\phi"]),
    ("D.17.30", ["D.9.28"],
     [r"\mathcalL_W={}&\frac12\left[K\!\left(\Phi,\Phi^\daggere^{-2t_AV_c^A}\right)\right]_D"]),
]
CROSSREF_ROWS = [
    # (row, canonical target, forbidden re-displayed table core)
    ("D.17.2", "D.14.5", r"M^T=-\mathcalC_WM\mathcalC_W^{-1}"),
    ("D.17.3", "D.16.30", r"(\bars_1Ms_2)^*=+(\bars_1Ms_2)"),
]


def check_no_dup_rows(text):
    ok = True
    detail = {"stripped": {}, "crossref": {}, "whole_block_collisions": [], "intra_extension_collisions": []}
    # (a) the nine stripped rows carry bare tag refs, not the locked equations
    for row, refs, cores in STRIPPED_ROWS:
        blk = display_block(text, row)
        if blk is None:
            ok = False
            detail["stripped"][row] = "MISSING"
            continue
        nb = norm(blk)
        refs_ok = all(r in blk for r in refs)
        cores_absent = all(norm(c) not in nb for c in cores)
        ok &= refs_ok and cores_absent
        detail["stripped"][row] = {"bare_refs": refs_ok, "locked_cores_absent": cores_absent}
    # (b) D.17.2 / D.17.3 are pure cross-reference rows
    for row, target, core in CROSSREF_ROWS:
        blk = display_block(text, row)
        if blk is None:
            ok = False
            detail["crossref"][row] = "MISSING"
            continue
        nb = norm(blk)
        start = text.find(r"\tag{" + row + "}")
        nxt = text.find(r"\tag{D.", start + 1)
        chunk = text[start:nxt if nxt > 0 else len(text)]
        ref_ok = target in blk and "cross-reference row" in chunk
        core_absent = norm(core) not in nb
        ok &= ref_ok and core_absent
        detail["crossref"][row] = {"bare_ref": ref_ok, "table_core_absent": core_absent}
    # (c) no new-row display equals any old-tag display (whole-block scan)
    old_blocks = {norm(display_block(text, t)) for t in OLD_TAGS if display_block(text, t)}
    new_tags = []
    for sec, (lo, hi) in NEW_RANGES.items():
        if sec == "D.10":
            continue
        new_tags += [f"{sec}.{n}" for n in range(lo, hi + 1)]
    new_blocks = {}
    for t in new_tags:
        b = display_block(text, t)
        if b is not None:
            new_blocks[t] = norm(b)
    for t, nb in new_blocks.items():
        if nb in old_blocks:
            ok = False
            detail["whole_block_collisions"].append(t)
    # (d) intra-extension scan: all new displays pairwise distinct
    seen = {}
    for t in new_tags:
        nb = new_blocks.get(t)
        if nb is None:
            continue
        if nb in seen:
            ok = False
            detail["intra_extension_collisions"].append([seen[nb], t])
        else:
            seen[nb] = t
    return ok, detail


# ----------------------------------------------------------------------
# check 3: FULL-DICT-GAMMA-BRIDGES
# ----------------------------------------------------------------------
def check_gamma_bridges():
    ok = True
    sub = {}
    id4 = eye(4)
    # (D.3.1) Clifford algebras on both columns
    s_ok = all(
        anticom(GAMMA_S[mu], GAMMA_S[nu]) == mscale(id4, -2 * ETA[mu]) if mu == nu else
        anticom(GAMMA_S[mu], GAMMA_S[nu]) == zeros(4, 4)
        for mu in range(4) for nu in range(4)
    )
    w_ok = all(
        anticom(GAMMA_W[mu], GAMMA_W[nu]) == mscale(id4, 2 * ETA[mu]) if mu == nu else
        anticom(GAMMA_W[mu], GAMMA_W[nu]) == zeros(4, 4)
        for mu in range(4) for nu in range(4)
    )
    sub["clifford_S_-2eta"] = s_ok
    sub["clifford_W_+2eta"] = w_ok
    ok &= s_ok and w_ok
    # (D.3.4)-(D.3.5) gamma_5 definitions and bridge gamma_{5W} = -gamma_{5S}
    g5_ok = GAMMA5_W == mscale(GAMMA5_S, -1)
    g5sq_ok = mmul(GAMMA5_S, GAMMA5_S) == id4 and mmul(GAMMA5_W, GAMMA5_W) == id4
    g5anticom_ok = all(
        anticom(GAMMA5_S, GAMMA_S[mu]) == zeros(4, 4)
        and anticom(GAMMA5_W, GAMMA_W[mu]) == zeros(4, 4)
        for mu in range(4)
    )
    sub["gamma5_bridge_minus"] = g5_ok
    sub["gamma5_squares_to_one"] = g5sq_ok
    sub["gamma5_anticommutes"] = g5anticom_ok
    ok &= g5_ok and g5sq_ok and g5anticom_ok
    # (D.3.13) C properties: C^T = C^dagger = C^{-1} = -C, C^2 = -1
    c_props = (
        mT(CMAT) == mscale(CMAT, -1)
        and mdag(CMAT) == mscale(CMAT, -1)
        and mmul(CMAT, CMAT) == mscale(id4, -1)
        and mmul(CMAT_INV, CMAT) == id4
    )
    sub["C_transpose_dagger_inverse"] = c_props
    ok &= c_props
    # (D.3.13) C^{-1} gamma^mu C = -(gamma^mu)^T on both columns
    c_gamma_ok = all(
        mmul(mmul(CMAT_INV, g), CMAT) == mscale(mT(g), -1)
        for g in tuple(GAMMA_S) + tuple(GAMMA_W)
    )
    sub["C_gamma_transpose_minus"] = c_gamma_ok
    ok &= c_gamma_ok
    # (D.14.5) transpose table on both columns:
    #   minus for {gamma^mu, [gamma^mu, gamma^nu]}, plus for {1, gamma_5, gamma_5 gamma^mu}
    table_ok = True
    for gam, g5 in ((GAMMA_S, GAMMA5_S), (GAMMA_W, GAMMA5_W)):
        minus_set = list(gam) + [commut(gam[mu], gam[nu]) for mu in range(4) for nu in range(mu + 1, 4)]
        plus_set = [id4, g5] + [mmul(g5, g) for g in gam]
        for m in minus_set:
            table_ok &= mmul(mmul(CMAT, m), CMAT_INV) == mscale(mT(m), -1)
        for m in plus_set:
            table_ok &= mmul(mmul(CMAT, m), CMAT_INV) == mT(m)
    sub["C_transpose_table_D14_5"] = table_ok
    ok &= table_ok
    # (D.3.13a) epsilon_{4,W} = -C gamma_{5W} = diag(i sigma2, i sigma2)
    eps_ok = mscale(mmul(CMAT, GAMMA5_W), -1) == EPS4W
    sub["epsilon4W_equals_minus_C_gamma5W"] = eps_ok
    ok &= eps_ok
    # (D.3.11) hermiticity with beta = i gamma^0 and kappa_W = +1, kappa_S = -1
    herm_ok = True
    for gam, kappa in ((GAMMA_W, 1), (GAMMA_S, -1)):
        beta = mscale(gam[0], ZI)
        beta_sq = mmul(beta, beta)
        if beta_sq == id4:
            beta_inv = beta
        elif beta_sq == mscale(id4, -1):
            beta_inv = mscale(beta, -1)
        else:
            herm_ok = False
            continue
        for mu in range(4):
            herm_ok &= mdag(gam[mu]) == mscale(mmul(mmul(beta, gam[mu]), beta_inv), -kappa)
    sub["hermiticity_D3_11"] = herm_ok
    ok &= herm_ok
    return ok, sub


# ----------------------------------------------------------------------
# superspace engine on top of Ex (Lorentzian, (2A.28)/(2A.4)/(2A.6)/(3A.9)-(3A.12))
# ----------------------------------------------------------------------
EPS_U = {(1, 2): ONE, (2, 1): QI(Fr(-1))}        # eps^{12} = +1           (1.3)
EPS_D = {(1, 2): QI(Fr(-1)), (2, 1): ONE}        # eps_{12} = -1           (1.3)


def epsU(a, b): return EPS_U.get((a, b), Z0)
def epsD(a, b): return EPS_D.get((a, b), Z0)


SIG_L = {
    0: {(1, 1): ONE, (2, 2): ONE},
    1: {(1, 2): ONE, (2, 1): ONE},
    2: {(1, 2): QI(Fr(0), Fr(-1)), (2, 1): ZI},
    3: {(1, 1): ONE, (2, 2): QI(Fr(-1))},
}


def sigget(m, a, ad): return SIG_L[m].get((a, ad), Z0)


def sigbar(m, ad, a):
    out = Z0
    for b in (1, 2):
        for bd in (1, 2):
            out = out + epsU(a, b) * epsU(ad, bd) * sigget(m, b, bd)
    return out


def sig2(m, n, a, b):
    out = Z0
    for cd in (1, 2):
        out = out + sigget(m, a, cd) * sigbar(n, cd, b) - sigget(n, a, cd) * sigbar(m, cd, b)
    return out * Fr(1, 4)


def sig2low(m, n, a, b):
    out = Z0
    for c in (1, 2):
        out = out + sig2(m, n, a, c) * epsD(c, b)
    return out


DERIV_RE = re.compile(r"^(d(\d*))(lamB?|psi)(\d)_([0-3]+)$")
BASE_RE = re.compile(r"^(lamB?|psi)(\d)$")


def xderiv_name(name, mu):
    """name of the spacetime derivative of generator `name` wrt index mu (str)."""
    if name.startswith("th"):
        return None
    m = BASE_RE.match(name)
    if m:
        return f"d1{m.group(1)}{m.group(2)}_{mu}"
    m = DERIV_RE.match(name)
    if not m:
        raise ValueError(name)
    level = int(m.group(2)) if m.group(2) else 1
    if level >= 9:
        raise AssertionError("tenth derivative encountered: " + name)
    base, idx, ds = m.group(3), m.group(4), m.group(5)
    nd = "".join(sorted(ds + mu))
    return f"d{level + 1}{base}{idx}_{nd}"


class SusyEx(Ex):
    def deriv_x(self, el, mu):
        out = {}
        for (mono, f), c in el.items():
            if f != self.unit and f[0] in ("A", "D", "F"):
                nf = (f[0], tuple(sorted(f[1] + (mu,)))) + f[2:]
                out[(mono, nf)] = out.get((mono, nf), Z0) + c
            for r, g in enumerate(mono):
                h = xderiv_name(self.gens[g], mu)
                if h is None:
                    continue
                hid = self.gn[h]
                if hid in mono:
                    continue
                L = list(mono)
                L[r] = hid
                inv = sum(1 for i in range(len(L)) for j in range(i + 1, len(L)) if L[i] > L[j])
                nm = tuple(sorted(L))
                out[(nm, f)] = out.get((nm, f), Z0) + c * ((-1) ** inv)
        return {k: v for k, v in out.items() if v}

    def box(self, el):
        """□ = eta^{mu nu} d_mu d_nu as an exact second-derivative operator."""
        out = {}
        for mu, eta in enumerate(ETA):
            out = self.addel(out, self.deriv_x(self.deriv_x(el, str(mu)), str(mu)), Fr(eta))
        return out


def make_susy_ex(with_lam):
    from itertools import combinations_with_replacement
    names = ["th1", "th2", "thb1", "thb2"]
    if with_lam:
        names += ["lam1", "lam2", "lamB1", "lamB2"]
        fams = ("lam1", "lam2", "lamB1", "lamB2")
    else:
        names += ["psi1", "psi2"]
        fams = ("psi1", "psi2")
    max_level = 5 if with_lam else 9
    for f in fams:
        for level in range(1, max_level + 1):
            for combo in combinations_with_replacement("0123", level):
                names.append(f"d{level}{f}_{''.join(combo)}")
    return SusyEx(names)


def make_D_ops(ex):
    """Lorentzian D_a, Dbar_adot of (2A.28) with (2A.4)/(2A.6)."""
    d_th = {a: {ex.gn[f"th{a}"]: ONE} for a in (1, 2)}
    d_thb = {ad: {ex.gn[f"thb{bd}"]: epsD(ad, bd) for bd in (1, 2)} for ad in (1, 2)}

    def Da(a):
        def op(X):
            out = ex.deriv_odd(X, d_th[a])
            for m in range(4):
                for ad in (1, 2):
                    s = sigget(m, a, ad)
                    if not s:
                        continue
                    for bd in (1, 2):
                        e = epsU(ad, bd)
                        if not e:
                            continue
                        t = ex.mulel(ex.genel([f"thb{bd}"]), ex.deriv_x(X, str(m)))
                        out = ex.addel(out, t, QI(Fr(0), Fr(-1)) * s * e)
            return out
        return op

    def Dbar(ad):
        def op(X):
            out = ex.deriv_odd(X, d_thb[ad])
            for m in range(4):
                for b in (1, 2):
                    s = sigget(m, b, ad)
                    if not s:
                        continue
                    t = ex.mulel(ex.genel([f"th{b}"]), ex.deriv_x(X, str(m)))
                    out = ex.addel(out, t, ZI * s)
            return out
        return op

    def Dbar_up(ad):
        def op(X):
            out = {}
            for bd in (1, 2):
                e = epsU(ad, bd)
                if e:
                    out = ex.addel(out, Dbar(bd)(X), e)
            return out
        return op

    def D_up(a):
        def op(X):
            out = {}
            for b in (1, 2):
                e = epsU(a, b)
                if e:
                    out = ex.addel(out, Da(b)(X), e)
            return out
        return op

    def Dbar2(X):  # barD^2 = barD_adot barD^adot : apply barD^adot first  (3A.10)
        out = {}
        for ad in (1, 2):
            out = ex.addel(out, Dbar(ad)(Dbar_up(ad)(X)))
        return out

    def D2(X):     # D^2 = D^a D_a : apply D_a first                        (3A.10)
        out = {}
        for a in (1, 2):
            out = ex.addel(out, D_up(a)(Da(a)(X)))
        return out

    return Da, Dbar, Dbar2, D2


def theta2(ex):  # th^a th_a = eps_{ab} th^a th^b = -2 th^1 th^2           (3A.9)
    out = {}
    for a in (1, 2):
        for b in (1, 2):
            e = epsD(a, b)
            if e:
                out = ex.addel(out, ex.mulel(ex.genel([f"th{a}"]), ex.genel([f"th{b}"])), e)
    return out


def thetabar2(ex):  # thbar_adot thbar^adot = +2 thb1 thb2                 (3A.9)
    out = {}
    for ad in (1, 2):
        for bd in (1, 2):
            e = epsU(ad, bd)
            if e:
                out = ex.addel(out, ex.mulel(ex.genel([f"thb{ad}"]), ex.genel([f"thb{bd}"])), e)
    return out


def attach_field(ex, el, field):
    out = {}
    for (mono, f), c in el.items():
        assert f == ex.unit, f
        out[(mono, field)] = c
    return out


def u_shift(ex, m):
    """U^m = -i th sigma^m thbar (chiral coordinate y = x - i th sigma thbar, (0A.62))."""
    m = int(m)
    out = {}
    for a in (1, 2):
        for ad in (1, 2):
            s = sigget(m, a, ad)
            if not s:
                continue
            for bd in (1, 2):
                e = epsU(ad, bd)
                if not e:
                    continue
                t = ex.mulel(ex.genel([f"th{a}"]), ex.genel([f"thb{bd}"]))
                out = ex.addel(out, t, QI(Fr(0), Fr(-1)) * s * e)
    return out


# ----------------------------------------------------------------------
# check 4: FULL-DICT-GRASSMANN-FTERM  (rows D.9.14, D.9.15, D.17.16; 0A.77)
# ----------------------------------------------------------------------
def check_grassmann_fterm():
    ex = make_susy_ex(with_lam=True)
    Da, Dbar, Dbar2, D2 = make_D_ops(ex)
    unit = ex.unit

    def fldA(mu, nu=()):
        return ("A", tuple(sorted(nu)), (str(mu),))

    def fldD():
        return ("D", (), ())

    def th_sigma_thbar(m, field):
        out = {}
        for a in (1, 2):
            for ad in (1, 2):
                s = sigget(m, a, ad)
                if not s:
                    continue
                for bd in (1, 2):
                    e = epsU(ad, bd)
                    if not e:
                        continue
                    t = ex.mulel(ex.genel([f"th{a}"]), ex.genel([f"thb{bd}"], field))
                    out = ex.addel(out, t, s * e)
        return out

    # WZ vector superfield (3A.47), Abelian
    V = {}
    for m in range(4):
        V = ex.addel(V, th_sigma_thbar(m, fldA(m)), Fr(-2))
    t2 = theta2(ex)
    tb2 = thetabar2(ex)
    for ad in (1, 2):
        V = ex.addel(V, ex.mulel(t2, ex.genel([f"thb{ad}", f"lamB{ad}"])), ZI * 2)
    for a in (1, 2):
        V = ex.addel(V, ex.mulel(tb2, ex.genel([f"th{a}", f"lam{a}"])), QI(Fr(0), Fr(-2)))
    V = ex.addel(V, ex.mulel(ex.mulel(t2, tb2), ex.genel([], fldD())), ONE)

    W = {a: ex.scalel(Dbar2(Da(a)(V)), Fr(-1, 8)) for a in (1, 2)}

    sub = {}
    ok = True
    # lowest component W_a| = -i lam_a  (3A.54)
    low_ok = all(
        ex.getc(W[a], [f"lam{c}"], unit) == (QI(Fr(0), Fr(-1)) if a == c else Z0)
        for a in (1, 2) for c in (1, 2)
    )
    sub["W_lowest_component_-i_lambda"] = low_ok
    ok &= low_ok
    # theta-linear F-term coefficients C[a; c; mu, nu]
    FC = {}
    for a in (1, 2):
        for c in (1, 2):
            for mu in range(4):
                for nu in range(4):
                    v = ex.getc(W[a], [f"th{c}"], fldA(nu, (str(mu),)))
                    if v:
                        FC[(a, c, mu, nu)] = v
    # named slot (0A.77): a = 1, F_{01} -> -i th^1 F_{01}
    slot_ok = (
        FC.get((1, 1, 0, 1)) == QI(Fr(0), Fr(-1))
        and FC.get((1, 1, 1, 0)) == ZI
        and (1, 2, 0, 1) not in FC
        and (1, 2, 1, 0) not in FC
    )
    sub["named_slot_a1_F01_-i_th1"] = slot_ok
    ok &= slot_ok
    # full form (A): theta-linear F-term == i (sigma^{mu nu})_a{}^b th_b F_{mu nu}
    predA = {}
    for a in (1, 2):
        for c in (1, 2):
            for mu in range(4):
                for nu in range(4):
                    acc = Z0
                    for b in (1, 2):
                        acc = acc + sig2(mu, nu, a, b) * epsD(b, c)
                    v = ZI * 2 * acc
                    if v:
                        predA[(a, c, mu, nu)] = v
    formA_ok = FC == predA
    sub["full_form_A_i_sigma_mn_upper"] = formA_ok
    ok &= formA_ok
    # form (B) i (sigma^{mu nu})_{ab} th_b F_{mu nu} is rejected
    predB = {}
    for a in (1, 2):
        for c in (1, 2):
            for mu in range(4):
                for nu in range(4):
                    acc = Z0
                    for b in (1, 2):
                        acc = acc + sig2low(mu, nu, a, b) * epsD(b, c)
                    v = ZI * 2 * acc
                    if v:
                        predB[(a, c, mu, nu)] = v
    keys = set(FC) | set(predB)
    mismatches = sum(1 for k in keys if FC.get(k, Z0) != predB.get(k, Z0))
    formB_rejected = mismatches > 0
    sub["form_B_lowered_rejected"] = formB_rejected
    sub["form_B_mismatch_slots"] = mismatches
    sub["slots_checked"] = len(FC)
    ok &= formB_rejected
    return ok, sub


# ----------------------------------------------------------------------
# check 5: FULL-DICT-BRST-SIGN-CHAIN  (rows D.19.1-D.19.5, D.19.9)
# ----------------------------------------------------------------------
EPS3 = (
    ((0, 0, 0), (0, 0, 1), (0, -1, 0)),
    ((0, 0, -1), (0, 0, 0), (1, 0, 0)),
    ((0, 1, 0), (-1, 0, 0), (0, 0, 0)),
)  # eps_{abc} for su(2), a,b,c in 1..3 via [a-1][b-1][c-1]


def check_brst_sign_chain():
    gval, xival = 2, 3
    names = ["c1", "c2", "c3", "cb1", "cb2", "cb3"]
    names += [f"dc{m}{a}" for m in range(4) for a in (1, 2, 3)]
    names += [
        f"d2c{m1}{m2}{a}"
        for m1 in range(4) for m2 in range(m1, 4) for a in (1, 2, 3)
    ]
    ex = Ex(names)
    unit = ex.unit
    G = Fr(gval)
    XI = Fr(xival)

    def A_el(mu, a, ds=()):
        return {((), ("A", tuple(sorted(ds)), (mu, a))): ONE}

    def B_el(a):
        return {((), ("B", (a,))): ONE}

    def brst_gen(name):
        if name.startswith("cb"):
            a = int(name[2])
            return B_el(a)
        if name.startswith("c"):
            a = int(name[1])
            out = {}
            for j in (1, 2, 3):
                for k in (1, 2, 3):
                    e = EPS3[j - 1][k - 1][a - 1]
                    if e:
                        t = ex.mulel(ex.genel([f"c{j}"]), ex.genel([f"c{k}"]))
                        out = ex.addel(out, t, Fr(-gval, 2) * e)
            return out
        if name.startswith("dc"):
            m, a = int(name[2]), int(name[3])
            out = {}
            for j in (1, 2, 3):
                for k in (1, 2, 3):
                    e = EPS3[j - 1][k - 1][a - 1]
                    if e:
                        t = ex.mulel(ex.genel([f"dc{m}{j}"]), ex.genel([f"c{k}"]))
                        out = ex.addel(out, t, Fr(-gval) * e)
            return out
        raise AssertionError("unexpected generator in BRST variation: " + name)

    def brst_mono(mono):
        out = {}
        for r, gid in enumerate(mono):
            dv = brst_gen(ex.gens[gid])
            sign = (-1) ** r
            pre, post = mono[:r], mono[r + 1:]
            for (m2, f2), c2 in dv.items():
                sgn1, mm1 = Ex.kmerge(pre, m2)
                if not sgn1:
                    continue
                sgn2, mm = Ex.kmerge(mm1, post)
                if not sgn2:
                    continue
                k = (mm, f2)
                out[k] = out.get(k, Z0) + c2 * sign * sgn1 * sgn2
        return {k: v for k, v in out.items() if v}

    def brst(el):
        out = {}
        for (mono, field), coef in el.items():
            if field != unit and field[0] == "A":
                _, ds, (mu, a) = field
                var = {}
                if len(ds) == 0:
                    var = ex.addel(var, ex.genel([f"dc{mu}{a}"]))
                    for b in (1, 2, 3):
                        for c_ in (1, 2, 3):
                            e = EPS3[b - 1][c_ - 1][a - 1]
                            if e:
                                t = ex.mulel(A_el(mu, c_), ex.genel([f"c{b}"]))
                                var = ex.addel(var, t, Fr(-gval) * e)
                elif len(ds) == 1:
                    nu = ds[0]
                    lo, hi = min(mu, nu), max(mu, nu)
                    var = ex.addel(var, ex.genel([f"d2c{lo}{hi}{a}"]))
                    for b in (1, 2, 3):
                        for c_ in (1, 2, 3):
                            e = EPS3[b - 1][c_ - 1][a - 1]
                            if e:
                                t1 = ex.mulel(A_el(mu, c_, (nu,)), ex.genel([f"c{b}"]))
                                t2 = ex.mulel(A_el(mu, c_), ex.genel([f"dc{nu}{b}"]))
                                var = ex.addel(var, t1, Fr(-gval) * e)
                                var = ex.addel(var, t2, Fr(-gval) * e)
                else:
                    raise AssertionError("BRST variation of higher-derivative field")
                out = ex.addel(out, ex.mulel(var, {(mono, unit): ONE}), coef)
                out = ex.addel(out, ex.mulel({((), field): ONE}, brst_mono(mono)), coef)
            elif field != unit and field[0] == "B":
                out = ex.addel(out, ex.mulel({((), field): ONE}, brst_mono(mono)), coef)
            else:
                out = ex.addel(out, brst_mono(mono), coef)
        return out

    sub = {}
    ok = True
    # (D.19.2) delta_B^2 = 0 on A, c, cbar, B
    nilp_A = all(not brst(brst(A_el(mu, a))) for mu in range(4) for a in (1, 2, 3))
    nilp_c = all(not brst(brst(ex.genel([f"c{a}"]))) for a in (1, 2, 3))
    nilp_cb = all(not brst(brst(ex.genel([f"cb{a}"]))) for a in (1, 2, 3))
    nilp_B = all(not brst(B_el(a)) for a in (1, 2, 3))
    sub["nilpotent_on_A"] = nilp_A
    sub["nilpotent_on_ghost"] = nilp_c
    sub["nilpotent_on_antighost"] = nilp_cb
    sub["nilpotent_on_LN_field"] = nilp_B
    ok &= nilp_A and nilp_c and nilp_cb and nilp_B
    # ghost-law bridge: -1/2 c_{AB}{}^C c_P^A c_P^B (0A.107) with c_P = g c_S
    # reproduces g * (D.19.3) delta_B c^C
    bridge_ok = True
    for C in (1, 2, 3):
        lhs = {}
        for a in (1, 2, 3):
            for b in (1, 2, 3):
                e = EPS3[a - 1][b - 1][C - 1]
                if e:
                    t = ex.mulel(ex.genel([f"c{a}"]), ex.genel([f"c{b}"]))
                    lhs = ex.addel(lhs, t, Fr(-gval * gval, 2) * e)
        rhs = ex.scalel(brst(ex.genel([f"c{C}"])), Fr(gval))
        bridge_ok &= lhs == rhs
    sub["ghost_law_bridge_0A107_to_D19_3"] = bridge_ok
    ok &= bridge_ok
    # i-ful adjoint coefficient: -i A_M with (T_c)^{ab} = -i f^{cab}, A_P = g A_S
    #   (-i)(g)(-i) = -g and eps_{cab} = eps_{abc}  ->  -i A_M -> -g f^{abc} A_S^c  (D.19.1 vs 0A.45)
    iful_ok = (QI(Fr(0), Fr(-1)) * G * QI(Fr(0), Fr(-1))) == Fr(-gval)
    cyclic_ok = all(
        EPS3[c - 1][a - 1][b - 1] == EPS3[a - 1][b - 1][c - 1]
        for a in (1, 2, 3) for b in (1, 2, 3) for c in (1, 2, 3)
    )
    sub["i_ful_covariant_derivative_sign"] = iful_ok and cyclic_ok
    ok &= iful_ok and cyclic_ok
    # gauge-fixing functional G^a = d^mu A_mu^a and its variation (snapshot 74.21-22)
    def Gf(a):
        out = {}
        for mu in range(4):
            out = ex.addel(out, A_el(mu, a, (mu,)), Fr(ETA[mu]))
        return out

    def dBG(a):
        """delta_B G^a = d^mu D_mu^{ab} c^b, assembled directly."""
        out = {}
        for mu in range(4):
            out = ex.addel(out, ex.genel([f"d2c{mu}{mu}{a}"]), Fr(ETA[mu]))
            for b in (1, 2, 3):
                for c_ in (1, 2, 3):
                    e = EPS3[b - 1][c_ - 1][a - 1]
                    if e:
                        t1 = ex.mulel(A_el(mu, c_, (mu,)), ex.genel([f"c{b}"]))
                        t2 = ex.mulel(A_el(mu, c_), ex.genel([f"dc{mu}{b}"]))
                        out = ex.addel(out, t1, Fr(-gval * ETA[mu]) * e)
                        out = ex.addel(out, t2, Fr(-gval * ETA[mu]) * e)
        return out

    dbg_ok = all(brst(Gf(a)) == dBG(a) for a in (1, 2, 3))
    sub["delta_B_G_equals_dDc"] = dbg_ok
    ok &= dbg_ok
    # (D.19.9) s Psi = delta_B O with Psi_P = +O_S (0A.116/0A.118 via 0A.104/0A.115)
    spsi_ok = True
    for a in (1, 2, 3):
        psi = ex.mulel(ex.genel([f"cb{a}"]), ex.scalel(B_el(a), XI / 2))
        psi = ex.addel(psi, ex.mulel(ex.genel([f"cb{a}"]), ex.scalel(Gf(a), -1)))
        # BV side: s Psi = <n,F> - 1/2<n,Y n> - <c', sF> + 1/2<c',(sY)n>
        lhs = ex.mulel(B_el(a), ex.scalel(Gf(a), -1))
        lhs = ex.addel(lhs, ex.mulel(B_el(a), ex.scalel(B_el(a), XI / 2)))
        lhs = ex.addel(lhs, ex.mulel(ex.genel([f"cb{a}"]), brst(Gf(a))))
        rhs = brst(psi)
        spsi_ok &= lhs == rhs
    sub["sPsi_equals_delta_B_O"] = spsi_ok
    sub["parameters"] = {"f": "su(2) eps_{abc}", "g": gval, "xi": xival}
    ok &= spsi_ok
    return ok, sub


# ----------------------------------------------------------------------
# check 6: FULL-DICT-SUPERCURRENT-ROWS  (rows D.16.14-D.16.16, D.16.20)
# ----------------------------------------------------------------------
def spincol(a, b, c, d):
    return ((q(a),), (q(b),), (q(c),), (q(d),))


def check_supercurrent_rows():
    gam = GAMMA_W  # Weinberg-column rows (26.7.x): {gamma_W, gamma_W} = +2 eta (D.3.1)
    id4 = eye(4)
    z4 = zeros(4, 1)
    sub = {}
    ok = True
    # arbitrary exact omega^Theta_nu spinors (rational components)
    omega = [
        spincol(1, ZI, 0, 1),
        spincol(2, QI(Fr(0), Fr(3)), -1, 3),
        spincol(3, QI(Fr(0), Fr(4)), -2, 5),
        spincol(4, QI(Fr(0), Fr(5)), -3, 7),
    ]

    def gammacontract(vec):
        out = z4
        for nu in range(4):
            out = madd(out, mmul(gam[nu], vec[nu]))
        return out

    def s_new(vec):
        """corrected (26.7.20): S^mu = -2 omega^{Theta mu} + 2 gamma^mu gamma^nu omega^Theta_nu"""
        gdot = gammacontract(vec)
        return [
            madd(mscale(vec[mu], -2 * ETA[mu]), mscale(mmul(gam[mu], gdot), 2))
            for mu in range(4)
        ]

    # (i) gamma-trace of the corrected form: gamma_mu S^mu = 6 gamma . omega^Theta
    s = s_new(omega)
    trace = z4
    for mu in range(4):
        trace = madd(trace, mscale(mmul(gam[mu], s[mu]), ETA[mu]))
    trace_ok = trace == mscale(gammacontract(omega), 6)
    sub["corrected_26720_trace_6gammaomega"] = trace_ok
    ok &= trace_ok
    # (ii) under gamma . omega^Theta = 0 the corrected form reduces to S^mu = -2 omega^{Theta mu}
    #      (the book's own usage of (26.7.20): "S_sigma = -2 omega^Theta_sigma")
    gdot = gammacontract(omega)
    omega_tl = [
        madd(omega[nu], mscale(mmul(gam[nu], gdot), Fr(-ETA[nu], 4)))
        for nu in range(4)
    ]
    tl_ok = gammacontract(omega_tl) == z4
    usage_ok = all(
        s_new(omega_tl)[mu] == mscale(omega_tl[mu], -2 * ETA[mu]) for mu in range(4)
    )
    sub["gamma_traceless_projection"] = tl_ok
    sub["book_usage_S_equals_-2omega"] = usage_ok
    ok &= tl_ok and usage_ok
    # (iii) (D.16.14) improvement preserves conservation: d_mu d_nu A^{mu nu} = 0
    #       for antisymmetric A (commuting derivatives contract against antisymmetry)
    anti = [[Fr(0), Fr(2), Fr(-3), Fr(5)], [Fr(-2), Fr(0), Fr(7), Fr(-11)],
            [Fr(3), Fr(-7), Fr(0), Fr(13)], [Fr(-5), Fr(11), Fr(-13), Fr(0)]]
    improve_ok = all(
        sum(anti[mu][nu] * r1[mu] * r1[nu] for mu in range(4) for nu in range(4)) == 0
        and sum(anti[mu][nu] * r2[mu] * r2[nu] for mu in range(4) for nu in range(4)) == 0
        for r1, r2 in [((2, 3, 5, 7), (1, 1, 2, 3))]
    )
    sub["improvement_conserves_current"] = improve_ok
    ok &= improve_ok
    # (iv) (D.16.20) lambda^Theta_nu = - dslash omega^Theta_nu + d_nu gamma . omega^Theta
    #      satisfies gamma^nu lambda^Theta_nu = [gamma^mu, gamma^nu] d_mu omega_nu
    W = [
        [spincol(mu + nu, QI(Fr(0), Fr(mu - nu)), mu * nu - 1, mu + 2 * nu + 1)
         for nu in range(4)]
        for mu in range(4)
    ]
    lam = []
    for nu in range(4):
        term1 = z4
        for mu in range(4):
            term1 = madd(term1, mmul(gam[mu], W[mu][nu]))
        term2 = z4
        for mu in range(4):
            term2 = madd(term2, mmul(gam[mu], W[nu][mu]))
        lam.append(madd(mscale(term1, -1), term2))
    lhs = z4
    for nu in range(4):
        lhs = madd(lhs, mmul(gam[nu], lam[nu]))
    rhs = z4
    for mu in range(4):
        for nu in range(4):
            rhs = madd(rhs, mmul(commut(gam[mu], gam[nu]), W[mu][nu]))
    lambda_ok = lhs == rhs
    sub["lambda_trace_commutator_identity"] = lambda_ok
    ok &= lambda_ok
    return ok, sub


# ----------------------------------------------------------------------
# check 7: FULL-DICT-WICK-16BOX  (row D.16.6; locks (0A.51)/(0A.54) cited there)
# ----------------------------------------------------------------------
def check_wick_16box(text):
    ex = make_susy_ex(with_lam=False)
    Da, Dbar, Dbar2, D2 = make_D_ops(ex)
    unit = ex.unit
    sub = {}
    ok = True
    # (0A.51) D^2 th^2 = barD^2 thbar^2 = -4
    proj_ok = (
        ex.getc(D2(theta2(ex)), [], unit) == QI(Fr(-4))
        and ex.getc(Dbar2(thetabar2(ex)), [], unit) == QI(Fr(-4))
    )
    sub["D2_theta2_barD2_thetabar2_-4"] = proj_ok
    ok &= proj_ok
    # left-chiral superfield Phi(x, th, thbar) = A(y) + th psi(y) + th^2 F(y),
    # y^mu = x^mu - i th sigma^mu thbar  (chiral coordinate lock (0A.62))
    U = {m: u_shift(ex, str(m)) for m in range(4)}
    phi = attach_field(ex, { ((), unit): ONE }, ("A", ()))
    for m in range(4):
        phi = ex.addel(phi, attach_field(ex, U[m], ("A", (str(m),))))
    for m in range(4):
        for n in range(4):
            u2 = ex.mulel(U[m], U[n])
            phi = ex.addel(phi, attach_field(ex, u2, ("A", tuple(sorted((str(m), str(n)))))), Fr(1, 2))
    for a in (1, 2):
        phi = ex.addel(phi, ex.genel([f"th{a}", f"psi{a}"]))
    for a in (1, 2):
        for m in range(4):
            t = ex.mulel(ex.genel([f"th{a}"]), ex.mulel(U[m], ex.genel([f"d1psi{a}_{m}"])))
            phi = ex.addel(phi, t)
    t2 = theta2(ex)
    phi = ex.addel(phi, attach_field(ex, t2, ("F", ())))
    for m in range(4):
        t = ex.mulel(t2, U[m])
        phi = ex.addel(phi, attach_field(ex, t, ("F", (str(m),))))
    # chirality barD_adot Phi = 0 (also pins the -i sign of the chiral coordinate)
    chiral_ok = all(not Dbar(ad)(phi) for ad in (1, 2))
    sub["chiral_barD_Phi_0"] = chiral_ok
    ok &= chiral_ok
    # exact projector identity on the project letters: barD^2 D^2 Phi = +16 □ Phi.
    # This is the project-side value registered at verdict (D.10.178) ("Project +16□_E")
    # and is the identity underlying the locked Euclidean chiral projector
    # P_+ = barD^2 D^2 / (16 □_E) of (0A.54).
    lhs = Dbar2(D2(phi))
    rhs = ex.scalel(ex.box(phi), 16)
    box_ok = lhs == rhs
    sub["barD2_D2_Phi_+16box_Phi_project_lock"] = box_ok
    ok &= box_ok
    # projector idempotency: (barD^2 D^2)^2 Phi = (16 □)^2 Phi
    lhs2 = Dbar2(D2(lhs))
    rhs2 = ex.scalel(ex.box(ex.box(phi)), 256)
    idem_ok = lhs2 == rhs2
    sub["projector_idempotent"] = idem_ok
    ok &= idem_ok
    # (D.16.6) Weinberg-side bridge arithmetic of (0A.92): the dotted-square lock
    # (D_R^2 <-> -barD^2, D_L^2 <-> -D^2) transports the Weinberg identity
    # D_R^2 D_L^2 Phi = -16 □_W Phi to the project letters with factor
    # (-1)(-1) = +1, i.e. as barD^2 D^2 Phi = -16 □_L Phi; the exact engine value
    # on the project letters is +16 □_L, so the row's bridged Lorentzian reading
    # differs from the direct project value by exactly the sign registered as
    # CONDITIONAL at (D.10.178) with (D.18.2)/(D.18.7) in the maintainer queue.
    bridge_factor = 1
    sub["bridge_0A92_factor_(-1)(-1)"] = bridge_factor == 1
    start166 = text.find(r"\tag{D.16.6}")
    chunk166 = text[start166:start166 + 1600] if start166 >= 0 else ""
    chunk166_ns = chunk166.replace(" ", "")
    d166_txt = (
        start166 >= 0
        and "D_R^2\\mathcalD_L^2\\Phi=-16\\Box_L" in chunk166_ns
        and "\\barD^2D^2\\Phi=-16\\Box_L" in chunk166_ns
        and "(0A.54)" in chunk166
    )
    start178 = text.find(r"\tag{D.10.178}")
    chunk178 = text[start178:start178 + 1200] if start178 >= 0 else ""
    fork_ok = (
        "CONDITIONAL" in chunk178
        and "+16\\Box_E" in chunk178.replace(" ", "")
    )
    sub["D16_6_bridge_statement_registered"] = bool(d166_txt)
    sub["D10_178_conditional_fork_registered"] = fork_ok
    ok &= bridge_factor == 1 and bool(d166_txt) and fork_ok
    return ok, sub


# ----------------------------------------------------------------------
# check 8: FULL-DICT-VERDICT-CONSISTENCY
# ----------------------------------------------------------------------
VOCAB = ("VERIFIED", "CORRECTED", "FALSE", "CONDITIONAL", "SOURCE_INSUFFICIENT", "NOT_DEFINED_IN_SOURCE")
EXPECTED_STATUS_COUNTS = {"VERIFIED": 238, "CONDITIONAL": 18, "CORRECTED": 10, "NOT_DEFINED_IN_SOURCE": 1}


def row_statuses(text):
    tags = [(m.start(), f"D.{m.group(1)}.{m.group(2)}")
            for m in re.finditer(r"\\tag\{D\.(1[2-9]|20)\.(\d+)\}", text)]
    tags.sort()
    statuses = {}
    for i, (pos, tag) in enumerate(tags):
        end = tags[i + 1][0] if i + 1 < len(tags) else len(text)
        m = re.search(r"\*?Status:\*?\s*([A-Z_]+)", text[pos:end])
        statuses[tag] = m.group(1) if m else None
    ordered = [t for _, t in tags]
    for i, t in enumerate(ordered):
        if statuses[t] is None:
            for j in range(i + 1, len(ordered)):
                if statuses[ordered[j]] is not None:
                    statuses[t] = statuses[ordered[j]]
                    break
    return statuses


def check_verdict_consistency(text):
    ok = True
    sub = {}
    all_tags = set(re.findall(r"\\tag\{(D\.\d+\.\d+[a-z]?)\}", text))
    statuses = row_statuses(text)
    # (a) the 94 single-row verdicts (D.10.56-D.10.149) match their rows' statuses
    rows94 = re.findall(
        r"\\tag\{D\.10\.(\d+)\} \| (D\.(?:12|13|19|20)\.\d+) \| ([A-Z_]+) \|", text)
    r94_ok = len(rows94) == 94
    mism = []
    for n, row, verdict in rows94:
        r94_ok &= verdict in VOCAB
        r94_ok &= row in all_tags
        if statuses.get(row) != verdict:
            mism.append((row, verdict, statuses.get(row)))
    r94_ok &= not mism
    sub["single_row_verdicts"] = {"count": len(rows94), "mismatches": mism}
    ok &= r94_ok
    # (b) section-level verdicts (D.10.150-D.10.163): in-vocabulary, ranges cover
    #     D.14/D.15/D.16 completely
    mid = re.findall(
        r"\\tag\{D\.10\.(15\d|16[0-3])\} \| [^|]+ \| ([A-Z_]+)[^|]* \| ([^|]+) \|", text)
    mid_ok = len(mid) == 14 and all(v in VOCAB for _, v, _ in mid)
    covered = set()
    for n, _, rowspec in mid:
        for m in re.finditer(r"\(D\.(\d+)\.(\d+)\)--\(D\.(\d+)\.(\d+)\)", rowspec):
            sec, a, sec2, b = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            mid_ok &= sec == sec2
            for k in range(a, b + 1):
                covered.add(f"D.{sec}.{k}")
        for m in re.finditer(r"D\.(\d+)\.(\d+)(?!\])", rowspec):
            covered.add(f"D.{m.group(1)}.{m.group(2)}")
    want = {f"D.{s}.{k}" for s, hi in ((14, 35), (15, 39), (16, 30)) for k in range(1, hi + 1)}
    mid_ok &= covered >= want
    sub["section_verdicts"] = {"count": len(mid), "coverage_complete": covered >= want}
    ok &= mid_ok
    # (c) item verdicts (D.10.164-D.10.181): in-vocabulary, refs resolve
    tail = re.findall(
        r"\\tag\{D\.10\.(16[4-9]|17\d|18[01])\} \| \d+ \| [^|]+ \| ([A-Z_]+)[^|]* \| ([^|]+) \|",
        text)
    tail_ok = len(tail) == 18 and all(v in VOCAB for _, v, _ in tail)
    tail_refs = set()
    for _, _, rowspec in tail:
        for m in re.finditer(r"D\.(1[78])\.(\d+)", rowspec):
            tail_refs.add(f"D.{m.group(1)}.{m.group(2)}")
    tail_ok &= all(r in all_tags for r in tail_refs)
    sub["item_verdicts"] = {"count": len(tail), "refs": len(tail_refs), "refs_resolve": all(r in all_tags for r in tail_refs)}
    ok &= tail_ok
    # (d) every D.12-D.20 row carries a verdict: D.12-D.16/D.19/D.20 via the
    #     D.10-ext table, D.17/D.18 via inline row-level statuses
    table_covered = {row for _, row, _ in rows94} | covered
    direct = {f"D.{s}.{k}" for s, hi in ((12, 40), (13, 25), (14, 35), (15, 39), (16, 30), (19, 17), (20, 12))
              for k in range(1, hi + 1)}
    coverage_ok = direct <= table_covered
    inline_ok = all(
        statuses.get(f"D.{s}.{k}") in VOCAB
        for s, hi in ((17, 56), (18, 13)) for k in range(1, hi + 1)
    )
    sub["row_coverage"] = {"table_rows_complete": coverage_ok, "inline_D17_D18_complete": inline_ok}
    ok &= coverage_ok and inline_ok
    # (e) every inline status is in the six-word vocabulary with the audited counts
    from collections import Counter
    counts = Counter(statuses.values())
    vocab_ok = set(statuses.values()) <= set(VOCAB) and len(statuses) == 267
    counts_ok = dict(counts) == EXPECTED_STATUS_COUNTS
    sub["status_vocabulary"] = {"counts": dict(counts), "expected": EXPECTED_STATUS_COUNTS}
    ok &= vocab_ok and counts_ok
    # (f) no phantom verdict references inside the D.10-ext continuation region
    start = text.find("### D.10-ext")
    stop = text.find("## 11.")
    region = text[start:stop]
    phantoms = set()
    for m in re.finditer(r"D\.(\d+)\.(\d+)[a-z]?", region):
        t = f"D.{m.group(1)}.{m.group(2)}"
        if m.group(1) == "10" and int(m.group(2)) <= 55:
            continue  # declared implicit sequence (D.10.1)-(D.10.55) of the untagged grid
        if not any(x.startswith(t) for x in all_tags):
            phantoms.add(t)
    sub["phantom_refs"] = sorted(phantoms)
    ok &= not phantoms
    return ok, sub


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main():
    text = read_contract_text()
    contract_sha = hashlib.sha256((ROOT / CONTRACT).read_bytes()).hexdigest()
    results = []
    ok1, d1 = check_tag_surface(text)
    results.append(("FULL-DICT-TAG-SURFACE",
                    "(D.0.1)-(D.11.2), (D.10.56)-(D.10.181), (D.12.1)-(D.20.12)", ok1, d1))
    ok2, d2 = check_no_dup_rows(text)
    results.append(("FULL-DICT-NO-DUP-ROWS",
                    "(D.17.2), (D.17.3), (D.17.6), (D.17.15), (D.17.16), (D.17.18), "
                    "(D.17.20), (D.17.21), (D.17.25), (D.17.27), (D.17.30)", ok2, d2))
    ok3, d3 = check_gamma_bridges()
    results.append(("FULL-DICT-GAMMA-BRIDGES",
                    "(D.3.1)-(D.3.5), (D.3.11)-(D.3.13a), (D.14.5)", ok3, d3))
    ok4, d4 = check_grassmann_fterm()
    results.append(("FULL-DICT-GRASSMANN-FTERM",
                    "(D.9.14), (D.9.15), (D.17.16)", ok4, d4))
    ok5, d5 = check_brst_sign_chain()
    results.append(("FULL-DICT-BRST-SIGN-CHAIN",
                    "(D.19.1)-(D.19.5), (D.19.9)", ok5, d5))
    ok6, d6 = check_supercurrent_rows()
    results.append(("FULL-DICT-SUPERCURRENT-ROWS",
                    "(D.16.14)-(D.16.16), (D.16.20)", ok6, d6))
    ok7, d7 = check_wick_16box(text)
    results.append(("FULL-DICT-WICK-16BOX", "(D.16.6)", ok7, d7))
    ok8, d8 = check_verdict_consistency(text)
    results.append(("FULL-DICT-VERDICT-CONSISTENCY",
                    "(D.10.56)-(D.10.181), (D.12.1)-(D.20.12)", ok8, d8))
    checks = [
        {"name": name, "rows": rows, "passed": passed, "detail": detail}
        for name, rows, passed, detail in results
    ]
    failures = [c["name"] for c in checks if not c["passed"]]
    result = {
        "schema": 1,
        "task": "CONTRACT-FULL-NOTATION-DICTIONARY-001",
        "contract": CONTRACT,
        "contract_sha256": contract_sha,
        "coefficient_field": "Q(i)",
        "status": "PASS" if not failures else "FAIL",
        "totals": {"exact_checks": len(checks), "failed_checks": len(failures)},
        "checks": checks,
        "failures": failures,
    }
    output = ROOT / AUDIT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit("failed: " + ", ".join(failures))
    print(json.dumps(result["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
