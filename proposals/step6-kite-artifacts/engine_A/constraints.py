"""Chirality constraints for external letters.

W_a  = -1/4 Db^2 D_a v  is chiral:      Db_bd W_a  = 0   (Db Db^2 = 0)
Wt_ad = -1/4 D^2 Db_ad v is antichiral:  D_a Wt_ad = 0   (D D^2 = 0)

For a generic 16-component representation F (ext_superfield) with momentum M,
the constraint letters give linear relations expressing every component whose
theta-monomial contains a constrained slot in terms of lower components times
momentum entries. This module builds the substitution map and applies it.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *
from model import ext_superfield, apply_letter

def constraint_subst(prefix, M, kind, xi, parity=1):
    """kind: 'chiral' -> apply Db_bd (b=0,1) = 0 ; 'antichiral' -> D_a = 0.
    Returns dict sym -> CP (fully closed substitution)."""
    F = ext_superfield(0, prefix, xi, parity)
    eqs = []
    for idx in range(2):
        letter = ('Db', idx, 0, M) if kind == 'chiral' else ('D', idx, 0, M)
        C = apply_letter(F, letter)
        for gmono, cp in C.items():
            eqs.append(dict(cp))
    # each equation: sum_s coeff(mono_with_s) = 0, linear in prefix comps
    def compdeg(s):
        tail = s.split("_")[-1]
        return 0 if tail == "e" else len(tail)
    subst = {}
    def apply_sub_cp(cp):
        return cp_apply_subst(cp, subst)
    pending = [dict(cp) for cp in eqs if cp]
    for sweep in range(20):
        progress = False
        newpending = []
        for cp in pending:
            cp = apply_sub_cp(cp)
            if not cp: continue
            terms = {}
            for mono, c in cp.items():
                syms = [s for s in mono if s.startswith(prefix + "_")]
                assert len(syms) == 1, (mono,)
                rest = list(mono); rest.remove(syms[0])
                terms.setdefault(syms[0], {})
                terms[syms[0]] = cp_add(terms[syms[0]], {tuple(rest): c})
            terms = {s: co for s, co in terms.items() if co}
            if not terms:
                continue
            piv = None
            for s, co in terms.items():
                if list(co.keys()) == [()] and (piv is None or compdeg(s) > compdeg(piv)):
                    piv = s
            if piv is None:
                if len(terms) == 1:
                    # c(mom) * sym = 0 with generic momentum -> sym = 0
                    s = next(iter(terms))
                    subst[s] = {}
                    progress = True
                else:
                    newpending.append(cp)
                continue
            pc = terms[piv][()]
            assert pc[1] == 0 and pc[0] != 0
            expr = {}
            for s, co in terms.items():
                if s == piv: continue
                sc = cp_scale(co, (Fr(-1) / pc[0], Fr(0)))
                for mono, c in sc.items():
                    key = tuple(sorted(mono + (s,)))
                    expr[key] = cadd(expr.get(key, CZERO), c)
            expr = {m: c for m, c in expr.items() if not ciszero(c)}
            subst[piv] = expr
            progress = True
        pending = newpending
        if not pending or not progress:
            break
    assert not pending, ("unresolved constraint equations", len(pending))
    # close the map
    for piv in list(subst):
        subst[piv] = cp_apply_subst(subst[piv], subst)
    for piv in list(subst):
        subst[piv] = cp_apply_subst(subst[piv], subst)
    return subst

def cp_apply_subst(cp, subst):
    out = {}
    stack = list(cp.items())
    while stack:
        mono, c = stack.pop()
        dep = [s for s in mono if s in subst]
        if not dep:
            out[mono] = cadd(out.get(mono, CZERO), c)
            continue
        s0 = dep[0]
        rest = list(mono); rest.remove(s0)
        for m2, c2 in subst[s0].items():
            stack.append((tuple(sorted(tuple(rest) + m2)), cmul(c, c2)))
    return {m: c for m, c in out.items() if not ciszero(c)}

def gp_apply_subst(A, subst):
    R = {}
    for m, cp in A.items():
        r = cp_apply_subst(cp, subst)
        if r: R[m] = r
    return R
