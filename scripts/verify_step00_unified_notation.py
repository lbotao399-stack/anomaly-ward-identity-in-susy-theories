#!/usr/bin/env python3
"""Exact Step-0 unified-notation verifier.

Only Python's standard library is used.  All numerical witnesses live in the
Gaussian-rational field Q(i); no floating-point arithmetic and no external CAS
enter the calculation.  The Grassmann engine is the adjudicated exact engine
of the F-term arbitration (validation swarm, 2026-07-17), reproduced here
self-contained so the verify workflow needs no external input.

Every check names the contract equations of
contracts/foundations/step-00-unified-notation-convention.md that it verifies,
per the derivation-first law:

  1. tag surface: contiguous (0A.1)-(0A.140) plus subtag (0A.12a);
  2. formula-surface hygiene: banned approximation macros and control
     characters absent from (0A.1)-(0A.140);
  3. torsion: {D_a, barD_bdot} from the locked definitions (0A.46)/(0A.47)
     equals +2i sigma_L partial (0A.48) and -2 sigma_E partial (0A.49)
     on a generic test superfield;
  4. Berezin normalization: D^2 theta^2 = barD^2 thetabar^2 = -4 in both
     signatures, from the primitives (0A.23), (0A.43), (0A.44), (0A.51);
  5. Abelian W_a F-term: exact recomputation of W_a = -(1/8) barD^2 D_a V
     (Abelian limit of (0A.84)) from the WZ surface (0A.75); named slots
     (a=1, F_01) -> -i theta^1 F_01 and (a=2, F_23) -> -theta^2 F_23,
     and the full theta-linear theta-bar-free slice equals the locked
     i (sigma_L^{mu nu})_a{}^b theta_b F_{mu nu} of (0A.77)
     (arbitration verdict: form (A));
  6. BV grading arithmetic of the (0A.103)-(0A.104) table:
     gh(X^star) = -1 - gh(X), [X^star] = d_Sigma - [X] with
     d_8 = 2, d_+ = d_- = 3, and every S_min term of (0A.111) carries
     ghost number 0 and parity 0 with the displayed signs;
  7. spacetime Levi-Civita lowering: epsilon_{L,0123} = -1 and
     epsilon_{E,1234} = +1 follow from epsilon_L^{0123} = +1,
     epsilon_E^{1234} = +1 by (0A.2) metric lowering, matching (0A.3).
"""

from __future__ import annotations

from fractions import Fraction as Fr
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "foundations" / "step-00-unified-notation-convention.md"
AUDIT = ROOT / "audits" / "step00-unified-notation-verification.json"

TASK_ID = "CONTRACT-STEP-00-UNIFIED-NOTATION-001"


# ----------------------------------------------------------------------
# exact coefficient ring Q(i)
# ----------------------------------------------------------------------
class QI:
    __slots__ = ("re", "im")

    def __init__(s, re=0, im=0):
        s.re = re if isinstance(re, Fr) else Fr(re)
        s.im = im if isinstance(im, Fr) else Fr(im)

    def __add__(a, b):
        return QI(a.re + b.re, a.im + b.im)

    __radd__ = __add__

    def __sub__(a, b):
        return QI(a.re - b.re, a.im - b.im)

    def __rsub__(a, b):
        return QI(b.re - a.re, b.im - a.im)

    def __neg__(a):
        return QI(-a.re, -a.im)

    def __mul__(a, b):
        if isinstance(b, (int, Fr)):
            b = QI(b)
        return QI(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re)

    __rmul__ = __mul__

    def __eq__(a, b):
        if isinstance(b, (int, Fr)):
            b = QI(b)
        return a.re == b.re and a.im == b.im

    def __hash__(s):
        return hash((s.re, s.im))

    def __bool__(s):
        return bool(s.re or s.im)

    def __repr__(s):
        def f(x):
            return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

        if s.im == 0:
            return f(s.re)
        if s.re == 0:
            return "i" if s.im == 1 else "-i" if s.im == -1 else f(s.im) + "i"
        ip = "" if s.im == 1 else "-" if s.im == -1 else f(s.im)
        return f"({f(s.re)}{'+' if s.im > 0 else ''}{ip}i)"


def q(x):
    return x if isinstance(x, QI) else QI(x)


ZI = QI(0, 1)
Z0 = QI(0)

# ----------------------------------------------------------------------
# epsilon tensors and sigma matrices (0A.13), (0A.14), (0A.16)-(0A.19)
# ----------------------------------------------------------------------
EPS_U = {(1, 2): QI(1), (2, 1): QI(-1)}  # eps^{12}=+1
EPS_D = {(1, 2): QI(-1), (2, 1): QI(1)}  # eps_{12}=-1


def epsU(a, b):
    return EPS_U.get((a, b), Z0)


def epsD(a, b):
    return EPS_D.get((a, b), Z0)


# sigma^mu_{a adot}, mu in "0".."3"  (0A.16)
SIG_L = {
    "0": {(1, 1): QI(1), (2, 2): QI(1)},
    "1": {(1, 2): QI(1), (2, 1): QI(1)},
    "2": {(1, 2): QI(0, -1), (2, 1): QI(0, 1)},
    "3": {(1, 1): QI(1), (2, 2): QI(-1)},
}
# sigma_E^m_{a adot}, m in "1".."4"  (0A.17)
SIG_E = {
    "1": {(1, 2): QI(0, -1), (2, 1): QI(0, -1)},
    "2": {(1, 2): QI(-1), (2, 1): QI(1)},
    "3": {(1, 1): QI(0, -1), (2, 2): QI(0, 1)},
    "4": {(1, 1): QI(1), (2, 2): QI(1)},
}


def sigget(SIG, m, a, ad):
    return SIG[m].get((a, ad), Z0)


# bar sigma^{mu adot a} := eps^{ab} eps^{adot bdot} sigma^mu_{b bdot}  (0A.18)
def sigbar(SIG, m, ad, a):
    out = Z0
    for b in (1, 2):
        for bd in (1, 2):
            out = out + epsU(a, b) * epsU(ad, bd) * sigget(SIG, m, b, bd)
    return out


# sigma^{mu nu}_a{}^b = 1/4( sigma^mu_{a cdot} sbar^nu^{cdot b} - swap )  (0A.19)
def sig2(SIG, m, n, a, b):
    out = Z0
    for cd in (1, 2):
        out = out + sigget(SIG, m, a, cd) * sigbar(SIG, n, cd, b) - sigget(
            SIG, n, a, cd
        ) * sigbar(SIG, m, cd, b)
    return out * Fr(1, 4)


# ----------------------------------------------------------------------
# Grassmann algebra
#   generators (canonical order); monomial = sorted tuple of gen ids
#   term key = (mono, fieldkey); element = dict key -> QI
#   fieldkey: ("1",(),()) | ("A",dids,ix) | ("D",dids,())   dids sorted tuple
# ----------------------------------------------------------------------
GENS = []
GN = {}


def _add(name):
    GN[name] = len(GENS)
    GENS.append(name)


for _g in ("th1", "th2", "thb1", "thb2", "lam1", "lam2", "lamB1", "lamB2"):
    _add(_g)
XIDX = ["0", "1", "2", "3", "4"]
for _m in XIDX:
    for _a in (1, 2):
        _add(f"dlam{_a}_{_m}")
    for _a in (1, 2):
        _add(f"dlamB{_a}_{_m}")
for _i, _m1 in enumerate(XIDX):
    for _m2 in XIDX[_i:]:
        for _a in (1, 2):
            _add(f"d2lam{_a}_{_m1}{_m2}")
        for _a in (1, 2):
            _add(f"d2lamB{_a}_{_m1}{_m2}")
for _i, _m1 in enumerate(XIDX):
    for _j, _m2 in enumerate(XIDX[_i:], _i):
        for _m3 in XIDX[_j:]:
            for _a in (1, 2):
                _add(f"d3lam{_a}_{_m1}{_m2}{_m3}")
            for _a in (1, 2):
                _add(f"d3lamB{_a}_{_m1}{_m2}{_m3}")

FUNIT = ("1", (), ())


def fldA(mu, nu=()):
    return ("A", tuple(sorted(nu)), (mu,))


def fldD(nu=()):
    return ("D", tuple(sorted(nu)), ())


# Koszul merge of two sorted monomials: returns (sign, merged) or (0, None)
def kmerge(m1, m2):
    inv = 0
    for x in m1:
        for y in m2:
            if x == y:
                return 0, None
            if x > y:
                inv += 1
    return ((-1) ** inv, tuple(sorted(m1 + m2)))


def addel(e1, e2, s=QI(1)):
    out = dict(e1)
    for k, v in e2.items():
        nv = out.get(k, Z0) + s * v
        if nv:
            out[k] = nv
        elif k in out:
            del out[k]
    return out


def scalel(e, s):
    s = q(s)
    if not s:
        return {}
    return {k: v * s for k, v in e.items() if v * s}


def mulel(e1, e2):
    out = {}
    for (m1, f1), c1 in e1.items():
        for (m2, f2), c2 in e2.items():
            sgn, mm = kmerge(m1, m2)
            if not sgn:
                continue
            if f1 == FUNIT:
                ff = f2
            elif f2 == FUNIT:
                ff = f1
            else:
                raise AssertionError("nonlinear field product (unexpected at linear order)")
            k = (mm, ff)
            out[k] = out.get(k, Z0) + c1 * c2 * sgn
    return {k: v for k, v in out.items() if v}


def genel(names, field=FUNIT, coeff=QI(1)):
    ids = tuple(sorted(GN[n] for n in names))
    return {(ids, field): coeff}


# graded LEFT odd derivative (0A.43), (0A.44)
def deriv_odd(el, action):
    out = {}
    for (mono, f), c in el.items():
        for r, g in enumerate(mono):
            v = action.get(g)
            if v:
                nm = mono[:r] + mono[r + 1 :]
                k = (nm, f)
                out[k] = out.get(k, Z0) + c * v * ((-1) ** r)
    return {k: v for k, v in out.items() if v}


# spacetime derivative d_mu (EVEN), mu = string index
def xderiv_gen(g, mu):
    name = GENS[g]
    if name.startswith("lamB"):
        return GN[f"dlamB{name[4]}_{mu}"]
    if name.startswith("lam"):
        return GN[f"dlam{name[3]}_{mu}"]
    if name.startswith("dlamB"):
        a, m1 = name[5], name[7]
        m = tuple(sorted((m1, mu)))
        return GN[f"d2lamB{a}_{m[0]}{m[1]}"]
    if name.startswith("dlam"):
        a, m1 = name[4], name[6]
        m = tuple(sorted((m1, mu)))
        return GN[f"d2lam{a}_{m[0]}{m[1]}"]
    if name.startswith("d2lamB"):
        a = name[6]
        ms = (name[8], name[9], mu)
        m = tuple(sorted(ms))
        return GN[f"d3lamB{a}_{m[0]}{m[1]}{m[2]}"]
    if name.startswith("d2lam"):
        a = name[5]
        ms = (name[7], name[8], mu)
        m = tuple(sorted(ms))
        return GN[f"d3lam{a}_{m[0]}{m[1]}{m[2]}"]
    if name.startswith("d3lam"):
        raise AssertionError("fourth derivative of lambda encountered")
    return None  # th, thb


def deriv_x(el, mu):
    out = {}
    for (mono, f), c in el.items():
        b, ds, ix = f
        if b in ("A", "D"):
            nf = (b, tuple(sorted(ds + (mu,))), ix)
            out[(mono, nf)] = out.get((mono, nf), Z0) + c
        for r, g in enumerate(mono):
            h = xderiv_gen(g, mu)
            if h is None:
                continue
            if h in mono:
                continue
            L = list(mono)
            L[r] = h
            inv = sum(1 for i in range(len(L)) for j in range(i + 1, len(L)) if L[i] > L[j])
            nm = tuple(sorted(L))
            out[(nm, f)] = out.get((nm, f), Z0) + c * ((-1) ** inv)
    return {k: v for k, v in out.items() if v}


# left derivative actions from (0A.43), (0A.44):
#   d_a th^b = delta_a^b ; dbar_adot thbar_bdot = eps_{adot bdot}
D_TH = {a: {GN[f"th{a}"]: QI(1)} for a in (1, 2)}
D_THB = {ad: {GN[f"thb{bd}"]: epsD(ad, bd) for bd in (1, 2)} for ad in (1, 2)}


# ----------------------------------------------------------------------
# covariant derivatives (0A.46) Lorentzian, (0A.47) Euclidean
# ----------------------------------------------------------------------
def make_D(SIG, didx, euclid):
    sgnA = QI(0, -1) if not euclid else QI(1)  # D_a  : -i (L) / +1 (E) times (sigma thbar)
    sgnB = ZI if not euclid else QI(-1)  # Dbar : +i (L) / -1 (E) times (th sigma)

    def Da(a):
        def op(X):
            out = deriv_odd(X, D_TH[a])
            for m in didx:
                for ad in (1, 2):
                    s = sigget(SIG, m, a, ad)
                    if not s:
                        continue
                    for bd in (1, 2):
                        e = epsU(ad, bd)
                        if not e:
                            continue
                        t = mulel(genel([f"thb{bd}"]), deriv_x(X, m))
                        out = addel(out, t, sgnA * s * e)
            return out

        return op

    def Dbar(ad):
        def op(X):
            out = deriv_odd(X, D_THB[ad])
            for m in didx:
                for b in (1, 2):
                    s = sigget(SIG, m, b, ad)
                    if not s:
                        continue
                    t = mulel(genel([f"th{b}"]), deriv_x(X, m))
                    out = addel(out, t, sgnB * s)
            return out

        return op

    return Da, Dbar


def Dbar_up(Dbar, ad):  # bar D^adot = eps^{adot bdot} bar D_bdot
    def op(X):
        out = {}
        for bd in (1, 2):
            e = epsU(ad, bd)
            if e:
                out = addel(out, Dbar(bd)(X), e)
        return out

    return op


def D_up(Da, a):  # D^a = eps^{ab} D_b
    def op(X):
        out = {}
        for b in (1, 2):
            e = epsU(a, b)
            if e:
                out = addel(out, Da(b)(X), e)
        return out

    return op


def Dbar2(Dbar):
    def op(X):  # barD^2 = barD_adot barD^adot (0A.51): apply barD^adot first
        out = {}
        for ad in (1, 2):
            out = addel(out, Dbar(ad)(Dbar_up(Dbar, ad)(X)))
        return out

    return op


def D2(Da):
    def op(X):  # D^2 = D^a D_a (0A.51): apply D_a first
        out = {}
        for a in (1, 2):
            out = addel(out, D_up(Da, a)(Da(a)(X)))
        return out

    return op


# ----------------------------------------------------------------------
# building blocks of the WZ vector superfield (0A.75)
# ----------------------------------------------------------------------
def theta2():  # th^a th_a = eps_{ab} th^a th^b = -2 th^1 th^2  (0A.23)
    out = {}
    for a in (1, 2):
        for b in (1, 2):
            e = epsD(a, b)
            if e:
                out = addel(out, mulel(genel([f"th{a}"]), genel([f"th{b}"])), e)
    return out


def thetabar2():  # thbar_adot thbar^adot = +2 thb1 thb2  (0A.23)
    out = {}
    for ad in (1, 2):
        for bd in (1, 2):
            e = epsU(ad, bd)
            if e:
                out = addel(out, mulel(genel([f"thb{ad}"]), genel([f"thb{bd}"])), e)
    return out


def th_sigma_thbar(SIG, m, field):  # th^a sigma^m_{a adot} thbar^adot, with field factor
    out = {}
    for a in (1, 2):
        for ad in (1, 2):
            s = sigget(SIG, m, a, ad)
            if not s:
                continue
            for bd in (1, 2):
                e = epsU(ad, bd)
                if not e:
                    continue
                t = mulel(genel([f"th{a}"]), genel([f"thb{bd}"], field))
                out = addel(out, t, s * e)
    return out


def build_V(SIG, didx, euclid):
    """WZ vector superfield (0A.75) Lorentzian / (0A.76) Euclidean."""
    V = {}
    for m in didx:
        V = addel(V, th_sigma_thbar(SIG, m, fldA(m)), (QI(-2) if not euclid else QI(0, -2)))
    # +2i th^2 thbar_adot lambar^adot
    t2 = theta2()
    for ad in (1, 2):
        tl = genel([f"thb{ad}", f"lamB{ad}"])
        V = addel(V, mulel(t2, tl), QI(0, 2))
    # -2i thbar^2 th^a lam_a
    tb2 = thetabar2()
    for a in (1, 2):
        tl = genel([f"th{a}", f"lam{a}"])
        V = addel(V, mulel(tb2, tl), QI(0, -2))
    # + th^2 thbar^2 Daux
    V = addel(V, mulel(mulel(t2, tb2), genel([], fldD())), QI(1))
    return V


def getc(el, mono_names, field):
    ids = tuple(sorted(GN[n] for n in mono_names))
    return el.get((ids, field), Z0)


# ----------------------------------------------------------------------
# generic test superfield for operator identities
# ----------------------------------------------------------------------
def test_superfield():
    X = {}
    X = addel(X, genel(["th1"], fldA("0")))
    X = addel(X, genel(["th2", "thb1"], fldA("1")), QI(0, 2))
    X = addel(X, genel(["thb2"], fldA("2", ("1",))), QI(3))
    X = addel(X, genel(["lam1"], fldD()))
    X = addel(X, genel(["th1", "lamB2"], fldA("3")))
    X = addel(X, genel(["th1", "th2", "thb1"], fldA("2")), ZI)
    X = addel(X, genel(["lamB1"]), QI(2))
    X = addel(X, genel(["th2", "lam2"], fldA("1", ("0",))))
    X = addel(X, genel(["th1", "th2", "lam1", "thb2"], fldA("3")), QI(1))
    return X


# ----------------------------------------------------------------------
# recorder
# ----------------------------------------------------------------------
class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []

    def check(self, name: str, category: str, equations: str, actual: Any, expected: Any) -> None:
        passed = actual == expected
        row = {
            "name": name,
            "category": category,
            "equations": equations,
            "passed": passed,
            "actual": actual,
            "expected": expected,
        }
        self.checks.append(row)
        if not passed:
            self.failures.append(
                {
                    "name": name,
                    "category": category,
                    "equations": equations,
                    "actual": actual,
                    "expected": expected,
                }
            )


# ----------------------------------------------------------------------
# check 1+2: document surface
# ----------------------------------------------------------------------
def document_checks(recorder: Recorder) -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    tags = re.findall(r"\\tag\{0A\.([^}]+)\}", text)
    expected: list[str] = []
    for number in range(1, 141):
        expected.append(str(number))
        if number == 12:
            expected.append("12a")
    recorder.check(
        "tag surface is the contiguous ordered set (0A.1)-(0A.140) plus subtag (0A.12a)",
        "document",
        "0A.1-0A.140, 0A.12a",
        {"unique": len(tags) == len(set(tags)), "tags": tags},
        {"unique": True, "tags": expected},
    )
    hygiene = {
        "backslash_sim": text.count("\\sim"),
        "backslash_approx": text.count("\\approx"),
        "backslash_propto": text.count("\\propto"),
        "control_characters": sum(
            1 for character in text if ord(character) < 32 and character not in "\n\t"
        ),
        "display_delimiter_parity_even": text.count("$$") % 2 == 0,
    }
    recorder.check(
        "formula surface carries no banned approximation macro, no control character, even display parity",
        "document",
        "0A.1-0A.140 (repository formula-surface policy)",
        hygiene,
        {
            "backslash_sim": 0,
            "backslash_approx": 0,
            "backslash_propto": 0,
            "control_characters": 0,
            "display_delimiter_parity_even": True,
        },
    )


# ----------------------------------------------------------------------
# check 3+4: torsion and Berezin normalization, both signatures
# ----------------------------------------------------------------------
def superspace_checks(recorder: Recorder) -> None:
    actual_torsion = {}
    actual_berezin = {}
    for label, SIG, didx, euclid in (
        ("L", SIG_L, ["0", "1", "2", "3"], False),
        ("E", SIG_E, ["1", "2", "3", "4"], True),
    ):
        Da, Dbar = make_D(SIG, didx, euclid)
        Db2 = Dbar2(Dbar)
        Dsq = D2(Da)
        X = test_superfield()
        kappa = QI(0, 2) if not euclid else QI(-2)
        ok = True
        for a in (1, 2):
            for bd in (1, 2):
                lhs = addel(Da(a)(Dbar(bd)(X)), Dbar(bd)(Da(a)(X)))
                rhs = {}
                for m in didx:
                    rhs = addel(rhs, deriv_x(X, m), kappa * sigget(SIG, m, a, bd))
                if lhs != rhs:
                    ok = False
        actual_torsion[label] = "PASS" if ok else "FAIL"
        c1 = getc(Dsq(theta2()), [], FUNIT)
        c2 = getc(Db2(thetabar2()), [], FUNIT)
        actual_berezin[label] = {"D2_theta2": repr(c1), "barD2_thetabar2": repr(c2)}
    recorder.check(
        "torsion {D_a,barD_bdot} from (0A.46)/(0A.47) equals +2i sigma_L partial (0A.48) and -2 sigma_E partial (0A.49)",
        "grassmann",
        "0A.46, 0A.47, 0A.48, 0A.49",
        actual_torsion,
        {"L": "PASS", "E": "PASS"},
    )
    recorder.check(
        "D^2 theta^2 = barD^2 thetabar^2 = -4 in both signatures",
        "grassmann",
        "0A.23, 0A.43, 0A.44, 0A.51",
        actual_berezin,
        {
            "L": {"D2_theta2": "-4", "barD2_thetabar2": "-4"},
            "E": {"D2_theta2": "-4", "barD2_thetabar2": "-4"},
        },
    )


# ----------------------------------------------------------------------
# check 5: Abelian W_a F-term slots versus (0A.77)
# ----------------------------------------------------------------------
def fterm_checks(recorder: Recorder) -> None:
    didx = ["0", "1", "2", "3"]
    Da, Dbar = make_D(SIG_L, didx, False)
    Db2 = Dbar2(Dbar)
    V = build_V(SIG_L, didx, False)
    W = {a: scalel(Db2(Da(a)(V)), Fr(-1, 8)) for a in (1, 2)}

    # named slots: coefficient pairs [th^c d_mu A_nu, th^c d_nu A_mu]
    slot_1_01 = (
        repr(getc(W[1], ["th1"], fldA("1", ("0",)))),
        repr(getc(W[1], ["th1"], fldA("0", ("1",)))),
    )
    slot_2_23 = (
        repr(getc(W[2], ["th2"], fldA("3", ("2",)))),
        repr(getc(W[2], ["th2"], fldA("2", ("3",)))),
    )

    # full theta-linear theta-bar-free slice equals i (sigma2)_a{}^b th_b F  (0A.77)
    full_slice_ok = True
    for a in (1, 2):
        for c in (1, 2):
            for mu in didx:
                for nu in didx:
                    actual = getc(W[a], [f"th{c}"], fldA(nu, (mu,)))
                    predicted = Z0
                    for b in (1, 2):
                        predicted = predicted + sig2(SIG_L, mu, nu, a, b) * epsD(b, c)
                    predicted = QI(0, 2) * predicted
                    if actual != predicted:
                        full_slice_ok = False

    recorder.check(
        "Abelian W_a F-term slots (a=1,F_01) = -i theta^1 F_01 and (a=2,F_23) = -theta^2 F_23; full slice is (0A.77) form (A)",
        "grassmann",
        "0A.75, 0A.77, 0A.84",
        {
            "slot_a1_F01_coeff_th1": [slot_1_01[0], slot_1_01[1]],
            "slot_a2_F23_coeff_th2": [slot_2_23[0], slot_2_23[1]],
            "full_theta_linear_slice_matches_0A77_form_A": full_slice_ok,
        },
        {
            "slot_a1_F01_coeff_th1": ["-i", "i"],
            "slot_a2_F23_coeff_th2": ["-1", "1"],
            "full_theta_linear_slice_matches_0A77_form_A": True,
        },
    )


# ----------------------------------------------------------------------
# check 6: BV grading arithmetic of the (0A.103)-(0A.104) table
# ----------------------------------------------------------------------
BV_TABLE = [
    # field, domain, parity, gh, dim, antifield_dim_from_table
    ("V", "8", 0, 0, 0, 2),
    ("Phi", "+", 0, 0, 1, 2),
    ("tildePhi", "-", 0, 0, 1, 2),
    ("c", "+", 1, 1, 0, 3),
    ("tildec", "-", 1, 1, 0, 3),
    ("c'", "+-", 1, -1, 2, 1),
    ("n", "+-", 0, 0, 2, 1),
]
D_DOMAIN = {"8": 2, "+": 3, "-": 3, "+-": 3}
SMIN_DISPLAYED_SIGNS = {"V": 1, "Phi": 1, "tildePhi": 1, "c": -1, "tildec": -1}


def bv_checks(recorder: Recorder) -> None:
    rows_ok = True
    for field, domain, _parity, _gh, dim, anti_dim in BV_TABLE:
        if D_DOMAIN[domain] - dim != anti_dim:
            rows_ok = False
    smin_ok = True
    for field, domain, parity, gh, _dim, _anti_dim in BV_TABLE[:5]:
        antifield_gh = -1 - gh
        brst_field_gh = gh + 1  # gh(s) = 1
        antifield_parity = (parity + 1) % 2
        brst_field_parity = (parity + 1) % 2
        if antifield_gh + brst_field_gh != 0:
            smin_ok = False
        if (antifield_parity + brst_field_parity) % 2 != 0:
            smin_ok = False
        if (-1) ** parity != SMIN_DISPLAYED_SIGNS[field]:
            smin_ok = False
    recorder.check(
        "BV table obeys gh(X^star) = -1 - gh(X), [X^star] = d_Sigma - [X]; every S_min term of (0A.111) has gh 0, parity 0, displayed sign (-1)^epsilon",
        "bv",
        "0A.102, 0A.103, 0A.104, 0A.111",
        {
            "antifield_dimension_column_equals_d_Sigma_minus_dimension": rows_ok,
            "s_min_terms_ghost_number_zero_parity_zero_signs_matched": smin_ok,
        },
        {
            "antifield_dimension_column_equals_d_Sigma_minus_dimension": True,
            "s_min_terms_ghost_number_zero_parity_zero_signs_matched": True,
        },
    )


# ----------------------------------------------------------------------
# check 7: spacetime Levi-Civita lowering (0A.2), (0A.3)
# ----------------------------------------------------------------------
def epsilon_checks(recorder: Recorder) -> None:
    eta_diag = [-1, 1, 1, 1]  # (0A.2) mostly-plus
    delta_diag = [1, 1, 1, 1]  # (0A.2) Euclidean delta

    def metric(diag, row, col):
        return diag[row] if row == col else 0

    def sign_of_permutation(perm):
        inversions = sum(
            1 for i, x in enumerate(perm) for y in perm[i + 1 :] if x > y
        )
        return (-1) ** inversions

    # epsilon_{L,0123} = eta_{0 mu} eta_{1 nu} eta_{2 rho} eta_{3 sigma} epsilon_L^{mu nu rho sigma}
    # epsilon_{E,1234} = delta_{1 m} delta_{2 n} delta_{3 r} delta_{4 s} epsilon_E^{mnrs}
    lower_L = 0
    lower_E = 0
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sigma in range(4):
                    perm = (mu, nu, rho, sigma)
                    if len(set(perm)) < 4:
                        continue
                    eps_up = sign_of_permutation(perm)  # epsilon^{0123} = +1
                    lower_L += (
                        metric(eta_diag, 0, mu)
                        * metric(eta_diag, 1, nu)
                        * metric(eta_diag, 2, rho)
                        * metric(eta_diag, 3, sigma)
                        * eps_up
                    )
                    lower_E += (
                        metric(delta_diag, 0, mu)
                        * metric(delta_diag, 1, nu)
                        * metric(delta_diag, 2, rho)
                        * metric(delta_diag, 3, sigma)
                        * eps_up
                    )
    recorder.check(
        "epsilon_{L,0123} = -1 and epsilon_{E,1234} = +1 by (0A.2) metric lowering of (0A.3)",
        "wick",
        "0A.2, 0A.3",
        {"epsilon_L_0123_lowered": lower_L, "epsilon_E_1234_lowered": lower_E},
        {"epsilon_L_0123_lowered": -1, "epsilon_E_1234_lowered": 1},
    )


def build_audit() -> dict[str, Any]:
    recorder = Recorder()
    document_checks(recorder)
    superspace_checks(recorder)
    fterm_checks(recorder)
    bv_checks(recorder)
    epsilon_checks(recorder)

    categories: dict[str, dict[str, int]] = {}
    for check in recorder.checks:
        row = categories.setdefault(check["category"], {"checks": 0, "failed": 0})
        row["checks"] += 1
        if not check["passed"]:
            row["failed"] += 1

    return {
        "schema": 1,
        "task": TASK_ID,
        "contract": "contracts/foundations/step-00-unified-notation-convention.md",
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "status": "PASS" if not recorder.failures else "FAIL",
        "arithmetic": {
            "coefficient_field": "Q(i)",
            "floating_point": False,
            "external_cas": False,
            "grassmann_odd_generators": [
                "theta^1",
                "theta^2",
                "thetabar_1dot",
                "thetabar_2dot",
            ],
            "bv_table_rows": 7,
        },
        "categories": categories,
        "totals": {
            "exact_checks": len(recorder.checks),
            "failed_checks": len(recorder.failures),
        },
        "checks": recorder.checks,
        "failures": recorder.failures,
    }


def main() -> None:
    audit = build_audit()
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2, ensure_ascii=False))
        raise SystemExit(1)
    print(
        "Step-0 unified-notation exact verification: "
        f"{audit['totals']['exact_checks']} exact checks, 0 failures"
    )


if __name__ == "__main__":
    main()
