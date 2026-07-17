"""Covariant (sigma-word) organization of kite numerators.

Building blocks in engine variables (p_{a ad}(X) = -i sigma_E . X):
  chain3(x,y,z)_{a ad}  = [p(x) pbar(y) p(z)]_{a ad}
  chain1(x)_{a ad}      = p(x)_{a ad}
  inv2(x,y)             = tr[p(x) pbar(y)]  = sum_{a,ad} p(x)_{a ad} pbar(y)^{ad a}
                        = -2 x.y  (Euclidean)
  chain5, inv4 analogous.
All free undotted indices in the kite reduce to component '+' by the insertion
word; free dotted indices are carried by the outjet family.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *

BASIS_MOM = ['l', 'k', 'p']

def PM(x):
    return pmat({x: 1})

def mat_mul_bar(A, Bbar):
    """(A Bbar)_a^b = A[a][bd] Bbar[bd][b] -> 2x2 undotted."""
    R = [[{} for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            e = {}
            for bd in range(2):
                e = cp_add(e, cp_mul(A[a][bd], Bbar[bd][b]))
            R[a][b] = e
    return R

def matU_mul(A, B):
    """undotted 2x2 times p-type: (A B)_{a bd} = A[a][c] B[c][bd]."""
    R = [[{} for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for bd in range(2):
            e = {}
            for c in range(2):
                e = cp_add(e, cp_mul(A[a][c], B[c][bd]))
            R[a][bd] = e
    return R

def chain3(x, y, z):
    """[p(x) pbar(y) p(z)] as 2x2 (a, ad)."""
    return matU_mul(mat_mul_bar(PM(x), pmat_bar(PM(y))), PM(z))

def inv2(x, y):
    """tr p(x) pbar(y) (= -2 x.y)."""
    A, Bb = PM(x), pmat_bar(PM(y))
    e = {}
    for a in range(2):
        for bd in range(2):
            e = cp_add(e, cp_mul(A[a][bd], Bb[bd][a]))
    return e

def structures_1free_dotted(maxdeg):
    """dict name -> {(ad,): CP} for N_{+,ad} type families.
    degree = number of p-entries. Includes chain1*inv2^k, chain3*inv2^k, chain5."""
    out = {}
    def put(name, fam):
        out[name] = fam
    for x in BASIS_MOM:
        if 1 <= maxdeg:
            put("p(%s)_{+ad}" % x, {(ad,): PM(x)[0][ad] for ad in range(2)})
    if maxdeg >= 3:
        for x in BASIS_MOM:
            for y in BASIS_MOM:
                for z in BASIS_MOM:
                    ch = chain3(x, y, z)
                    put("[p(%s)pb(%s)p(%s)]_{+ad}" % (x, y, z), {(ad,): ch[0][ad] for ad in range(2)})
        for x in BASIS_MOM:
            for y in BASIS_MOM:
                for z in BASIS_MOM:
                    if BASIS_MOM.index(y) > BASIS_MOM.index(z): continue
                    iv = inv2(y, z)
                    put("p(%s)_{+ad}*tr[p(%s)pb(%s)]" % (x, y, z),
                        {(ad,): cp_mul(PM(x)[0][ad], iv) for ad in range(2)})
    if maxdeg >= 5:
        # chain3 * inv2 and chain5 (only if needed)
        for x in BASIS_MOM:
            for y in BASIS_MOM:
                for z in BASIS_MOM:
                    ch = chain3(x, y, z)
                    for u in BASIS_MOM:
                        for w in BASIS_MOM:
                            if BASIS_MOM.index(u) > BASIS_MOM.index(w): continue
                            iv = inv2(u, w)
                            put("[p(%s)pb(%s)p(%s)]_{+ad}*tr[p(%s)pb(%s)]" % (x, y, z, u, w),
                                {(ad,): cp_mul(ch[0][ad], iv) for ad in range(2)})
    return out

def structures_scalar(maxdeg):
    """scalars: inv2 products, tr chains of length 4."""
    out = {}
    if maxdeg >= 2:
        for y in BASIS_MOM:
            for z in BASIS_MOM:
                if BASIS_MOM.index(y) > BASIS_MOM.index(z): continue
                out["tr[p(%s)pb(%s)]" % (y, z)] = inv2(y, z)
    if maxdeg >= 4:
        for c in itertools.product(BASIS_MOM, repeat=4):
            # tr p(x)pb(y)p(z)pb(w): canonical under cyclic (pairs)
            x, y, z, w = c
            key = min([(x, y, z, w), (z, w, x, y)])
            nm = "tr[p(%s)pb(%s)p(%s)pb(%s)]" % key
            if nm in out: continue
            A = matU_mul(mat_mul_bar(PM(key[0]), pmat_bar(PM(key[1]))), PM(key[2]))
            Bb = pmat_bar(PM(key[3]))
            e = {}
            for a in range(2):
                for bd in range(2):
                    e = cp_add(e, cp_mul(A[a][bd], Bb[bd][a]))
            out[nm] = e
        names = list(out)
        for n1 in names:
            for n2 in names:
                if "tr" in n1 and "tr" in n2 and n1 <= n2 and n1.count("pb") == 1 and n2.count("pb") == 1:
                    out[n1 + "*" + n2] = cp_mul(out[n1], out[n2])
    return out
