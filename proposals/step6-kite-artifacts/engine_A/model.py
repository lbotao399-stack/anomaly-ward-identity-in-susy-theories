"""Engine A: vertices, insertion words, contraction evaluator, color canonicalization.

Global-word evaluation scheme (see report):
  For a fixed contraction assignment the integrand is an ordered product of
  dressed-field factors F_1 F_2 ... F_n (source order = insertion legs, then
  vertex words in vertex order, external factors in their vertex positions).
  Each propagator line L pairs two factors (fE, fL) with fE earlier in source
  order. Its value with both dressings is
      G_L = WordE^{(ptE, M_into_E)} [ WordL^{(ptL, M_into_L)} delta4(thE - thL) ]
  (later factor's word applied FIRST). The total integrand equals
      (Koszul sign of the permutation source-order -> target-order)
      * product over target order of blocks,
  target order = [pair(L_1)..pair(L_m), externals in source order] with each
  pair contributing its G_L at the position of the block, then Berezin over
  the internal points. Koszul sign counts inversions of ODD factors only
  (word parity = number of D letters mod 2; odd external letters carry a xi tag
  and odd parity).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *

# ---------- vertex words --------------------------------------------------
# chi = '+' : (-1/hbar) S_{3,+} => coeff (+ i g /2) c_{CUE} (E-word v^E)(C-word v^C)(v^U)
#   E-word(a) = -1/4 Db^2 D^a ; C-word(a) = D_a  (sum over a)
# chi = '-' : coeff (- i g /2) c_{CUE},  E-word(ad) = -1/4 D^2 Db_ad ; C-word(ad)= Db^ad
# vertex numeric prefactors returned separately; g, hbar tracked as powers.

def vertex_realizations(chi):
    """returns list over contracted index value of (Eword, Cword); word=(coeff,letters)."""
    out = []
    if chi == '+':
        for a in range(2):
            # D^+ = D_-, D^- = -D_+
            low = 1 - a
            sgn = Fr(1) if a == 0 else Fr(-1)
            Ew = word_concat(((Fr(-1, 4) * sgn, Fr(0)), []), W_Db2, (CONE, [('D', low)]))
            Cw = (CONE, [('D', a)])
            out.append((Ew, Cw))
    else:
        for ad in range(2):
            Ew = word_concat(((Fr(-1, 4), Fr(0)), []), W_D2, (CONE, [('Db', ad)]))
            # Db^1 = Db_2 ; Db^2 = -Db_1
            up = 1 - ad
            sgn = Fr(1) if ad == 0 else Fr(-1)
            Cw = ((sgn, Fr(0)), [('Db', up)])
            out.append((Ew, Cw))
    return out

VERTEX_COEFF = {'+': (Fr(0), Fr(1, 2)), '-': (Fr(0), Fr(-1, 2))}   # (+-) i/2, incl (-1/hbar) sign

# insertion leg words (SPEC section 3); coefficients folded (D^2=2.., Db^2=2..)
# Oalpha = -1/8 D^2 Db^2 D_+  -> coeff -1/2, letters D_- D_+ Db_1 Db_2 D_+   (odd)
# Obeta  = -1/4 D_+ Db^2 D_+  -> coeff -1/2, letters D_+ Db_1 Db_2 D_+       (even)
W_OALPHA = ((Fr(-1, 2), Fr(0)), [('D', 1), ('D', 0), ('Db', 0), ('Db', 1), ('D', 0)])
W_OBETA = ((Fr(-1, 2), Fr(0)), [('D', 0), ('Db', 0), ('Db', 1), ('D', 0)])
W_ID = (CONE, [])

def word_parity(w): return len(w[1]) % 2

# ---------- factors and contraction evaluation ----------------------------

class Factor:
    __slots__ = ('fid', 'word', 'pt', 'parity', 'ext_poly')
    def __init__(self, fid, word=None, pt=None, ext_poly=None, parity=None):
        self.fid = fid; self.word = word; self.pt = pt; self.ext_poly = ext_poly
        self.parity = parity if parity is not None else (word_parity(word) if word else 0)

_gl_cache = {}

def line_block(fE, fL, ME, ML, cache_key=None):
    """G_L = WordE^{(fE.pt,ME)} WordL^{(fL.pt,ML)} delta4(thE-thL)."""
    if cache_key is not None and cache_key in _gl_cache:
        return _gl_cache[cache_key]
    d = delta4_pair(fE.pt, fL.pt)
    r = apply_word(d, fL.word[0], fL.word[1], fL.pt, ML)
    r = apply_word(r, fE.word[0], fE.word[1], fE.pt, ME)
    if cache_key is not None:
        _gl_cache[cache_key] = r
    return r

def koszul_sign(src_ids, src_par, tgt_ids):
    pos = {f: i for i, f in enumerate(src_ids)}
    odd = [f for f in tgt_ids if src_par[f] == 1]
    inv = 0
    for i in range(len(odd)):
        for j in range(i + 1, len(odd)):
            if pos[odd[i]] > pos[odd[j]]: inv += 1
    return (-1) ** inv

def eval_contraction(factors, lines, int_points, line_key_extra=""):
    """factors: list of Factor in source order.
    lines: list of (fidE, fidL, ME, ML, mkeyE, mkeyL)  with fidE earlier in source.
    Returns GPoly after multiplying blocks in target order and Berezin over int_points.
    """
    fmap = {f.fid: f for f in factors}
    src_ids = [f.fid for f in factors]
    src_par = {f.fid: f.parity for f in factors}
    paired = set()
    tgt_ids = []
    blocks = []
    for (fe, fl, ME, ML, mke, mkl) in lines:
        FE, FL = fmap[fe], fmap[fl]
        key = (line_key_extra, fe, fl, FE.pt, FL.pt,
               str(FE.word), str(FL.word), mke, mkl)
        blocks.append(line_block(FE, FL, ME, ML, cache_key=key))
        tgt_ids += [fe, fl]
        paired.update((fe, fl))
    for f in factors:
        if f.fid not in paired:
            blocks.append(f.ext_poly)
            tgt_ids.append(f.fid)
    sign = koszul_sign(src_ids, src_par, tgt_ids)
    R = gp_const(cp_const(CONE))
    for b in blocks:
        R = gp_mul(R, b)
        if not R: return {}
    if sign < 0:
        R = gp_scale(R, (Fr(-1), Fr(0)))
    for pt in int_points:
        R = berezin(R, pt)
        if not R: return {}
    return R

# ---------- color ----------------------------------------------------------

def color_canon(cfactors):
    """cfactors: list of (i,j,k) index-name triples of c_{ijk} (totally antisym).
    Returns (sign, canonical tuple of sorted triples sorted as list)."""
    sign = 1
    canon = []
    for tri in cfactors:
        perm = sorted(range(3), key=lambda t: tri[t])
        s = tri[perm[0]], tri[perm[1]], tri[perm[2]]
        # permutation parity
        inv = sum(1 for x in range(3) for y in range(x + 1, 3) if perm[x] > perm[y])
        if inv % 2: sign = -sign
        canon.append(s)
    canon.sort()
    return sign, tuple(canon)

def color_str(canon):
    return "".join("c[%s,%s,%s]" % t for t in canon)

# ---------- external superfields -------------------------------------------

MONOS4 = []
for k in range(5):
    for comb in itertools.combinations(range(4), k):
        MONOS4.append(tuple(comb))

def mono_name(m):
    return "".join(str(s) for s in m) if m else "e"

def ext_superfield(pt, prefix, xi, parity):
    """generic superfield of definite total Grassmann parity `parity` at point pt:
        F = sum_m m(theta_pt) * F_m ,  F_m parity = parity+|m| mod 2.
    Components with odd parity are represented as xi * f_m with commuting symbol
    f_m and the single odd tag generator `xi` (appended to the RIGHT of m(theta)).
    """
    R = {}
    for m in MONOS4:
        gm = tuple(gen(pt, s) for s in m)
        sym = cp_sym("%s_%s" % (prefix, mono_name(m)))
        if (len(m) + parity) % 2 == 1:
            gm = gm + (xi,)          # ascending append, no sign
        R[gm] = cp_add(R.get(gm, {}), sym)
    return R

# ---------- covariant jet basis at point 0 ----------------------------------

def jet_words():
    """16 covariant words; returns list of (name, (coeff, letters))."""
    out = [("v", (CONE, []))]
    for a, nm in ((0, "D[+]"), (1, "D[-]")):
        out.append(("%sv" % nm, (CONE, [('D', a)])))
    for b, nm in ((0, "Db[1]"), (1, "Db[2]")):
        out.append(("%sv" % nm, (CONE, [('Db', b)])))
    out.append(("D2v", W_D2))
    out.append(("Db2v", W_Db2))
    for a, na in ((0, "D[+]"), (1, "D[-]")):
        for b, nb in ((0, "Db[1]"), (1, "Db[2]")):
            out.append(("%s%sv" % (na, nb), (CONE, [('D', a), ('Db', b)])))
    for b, nb in ((0, "Db[1]"), (1, "Db[2]")):
        out.append(("D2%sv" % nb, word_concat(W_D2, (CONE, [('Db', b)]))))
    for a, na in ((0, "D[+]"), (1, "D[-]")):
        out.append(("Db2%sv" % na, word_concat(W_Db2, (CONE, [('D', a)]))))
    out.append(("D2Db2v", word_concat(W_D2, W_Db2)))
    assert len({n for n, _ in out}) == 16
    return out

def build_jet_basis(prefix, Mext, xi, parity):
    """returns dict name -> GPoly  ([W F](theta_0) with F generic components)."""
    v0 = ext_superfield(0, prefix, xi, parity)
    B = {}
    for name, w in jet_words():
        B[name] = apply_word(v0, w[0], w[1], 0, Mext)
    return B

def theta_pt(m): return tuple(g for g in m if g < 16)
def xi_pt(m): return tuple(g for g in m if g >= 16)

def lead_form(bpoly, preflist):
    """theta-free content of a basis poly: comp-sym -> (xi-tuple, CP rest)."""
    form = {}
    for m, cp in bpoly.items():
        if theta_pt(m): continue
        xit = xi_pt(m)
        for mono, c in cp.items():
            comps = [s for s in mono if any(s.startswith(p + "_") for p in preflist)]
            assert len(comps) == 1, (mono, comps)
            rest = list(mono); rest.remove(comps[0])
            s = comps[0]
            if s in form:
                assert form[s][0] == xit
                form[s] = (xit, cp_add(form[s][1], {tuple(rest): c}))
            else:
                form[s] = (xit, {tuple(rest): c})
    return form

def decompose_jets_OLD(R, basis, comp_prefixes):
    """R: GPoly in point-0 gens (+xi tags), linear in comp symbols of ONE field.
    basis: name -> GPoly. Solve R = sum_{m,W} c_{m,W} * m(theta0)*B_W  degree by degree.
    Returns list of (theta0_mono, jetname, CP coeff) and residual (should be {}).
    """
    names = [n for n, _ in jet_words()]
    # scalar parts of basis, as linear forms in comp symbols: sym -> CP coeff
    def linform(cp):
        # cp: CP whose monomials contain exactly one comp symbol (prefix match)
        form = {}
        for mono, c in cp.items():
            comps = [s for s in mono if any(s.startswith(p + "_") for p in comp_prefixes)]
            assert len(comps) == 1, (mono, comps)
            rest = tuple(s for s in mono if s != comps[0] or mono.count(comps[0]) > 1 and False)
            rest = list(mono); rest.remove(comps[0]); rest = tuple(rest)
            form.setdefault(comps[0], {})
            form[comps[0]] = cp_add(form[comps[0]], {rest: c})
        return form
    # order words by number of letters DESC for triangular solve
    wl = {n: len(w[1]) for n, w in jet_words()}
    # component degree of a comp symbol name: number of digits in mono part
    def compdeg(sym):
        tail = sym.split("_")[-1]
        return 0 if tail == "e" else len(tail)
    rows = []
    Rw = {m: dict(c) for m, c in R.items()}
    theta_monos = sorted({m for m in Rw}, key=lambda m: (len([g for g in m if g < 16]),) + m)
    # iterate theta0 monomials by ascending degree (gens <16 only; xi tags ride along)
    processed = set()
    for tm in list(theta_monos):
        pass
    # collect all theta-monomials present, ascending degree
    def tdeg(m): return len([g for g in m if g < 16])
    maxiter = 100
    it = 0
    while Rw and it < maxiter:
        it += 1
        tm = min(Rw.keys(), key=lambda m: (tdeg(m),) + m)
        cur = Rw[tm]
        # solve  cur = sum_W c_W * (B_W scalar-part-with-same-xi-structure)
        # basis element scalar part: B_W[()] but xi tags: B_W monomial = xi-part + ...
        xit = tuple(g for g in tm if g >= 16)
        tht = tuple(g for g in tm if g < 16)
        # scalar (theta-free) component of B_W including xi part
        Bs = {}
        for n in names:
            Bs[n] = basis[n].get(xit, {}) if xit else basis[n].get((), {})
        # solve triangularly by comp degree, high to low
        cw = {n: {} for n in names}
        work = dict(cur)
        for deg in (4, 3, 2, 1, 0):
            for n in names:
                if wl[n] != deg: continue
                fB = linform(Bs[n]) if Bs[n] else {}
                # diagonal comp symbol: the unique comp of degree == deg in fB
                diag = [s for s in fB if compdeg(s) == deg]
                if len(diag) != 1: continue
                ds = diag[0]; dcoef = fB[ds]
                # dcoef must be +-1 constant
                assert list(dcoef.keys()) == [()], (n, dcoef)
                dc = dcoef[()]
                # coefficient of ds in work
                cn = {}
                for mono, c in work.items():
                    if ds in mono:
                        rest = list(mono); rest.remove(ds)
                        cn[tuple(rest)] = cadd(cn.get(tuple(rest), CZERO), c)
                if not cn: continue
                inv = (Fr(1) / (dc[0] if dc[0] != 0 else 1), Fr(0))
                if dc[0] == 0: raise RuntimeError("non-real diagonal")
                cwn = cp_scale(cn, inv)
                cw[n] = cwn
                # subtract cwn * fB from work
                for s, co in fB.items():
                    sub = cp_mul(cwn, co)
                    for mono, c in sub.items():
                        nm = tuple(sorted(mono + (s,)))
                        v = cadd(work.get(nm, CZERO), cneg(c))
                        if ciszero(v): work.pop(nm, None)
                        else: work[nm] = v
        if work:
            raise RuntimeError("jet solve residual at %s: %s" % (str(tm), cp_str(work)))
        # record rows and subtract  tm_theta * B_W  from Rw   (xi part already in B_W)
        for n in names:
            if not cw[n]: continue
            rows.append((tht, n, cw[n]))
            # tm(theta) * B_W : multiply basis poly by theta monomial from left
            TB = basis[n]
            for g in reversed(tht):
                TB = gp_mulgen(TB, g)
            TB = gp_scale_cp(TB, cw[n])
            for m, c in TB.items():
                v = cp_add(Rw.get(m, {}), cp_scale(c, (Fr(-1), Fr(0))))
                if not v: Rw.pop(m, None)
                else: Rw[m] = v
    return rows, Rw

def _compdeg(sym):
    tail = sym.split("_")[-1]
    return 0 if tail == "e" else len(tail)

def decompose_jets(R, basis, comp_prefixes):
    """R linear in ONE external field's components. Solve
         R = sum_{t,W} c_{t,W} * t(theta0) * B_W
    theta0-monomials t ascending, jet words W by length descending (triangular).
    Returns rows [(t, name, CP)], residual (must be {})."""
    names = [n for n, _ in jet_words()]
    wl = {n: len(w[1]) for n, w in jet_words()}
    lead = {n: lead_form(basis[n], comp_prefixes) for n in names}
    diag = {}
    for n in names:
        cand = [s for s in lead[n] if _compdeg(s) == wl[n]]
        assert len(cand) == 1, (n, cand)
        diag[n] = cand[0]
    rows = []
    Rw = {m: dict(c) for m, c in R.items()}
    guard = 0
    while Rw:
        guard += 1
        if guard > 200: raise RuntimeError("no convergence")
        t = min((theta_pt(m) for m in Rw), key=lambda x: (len(x),) + x)
        # collect work: {(xi-tuple, cp-mono): coeff} over monomials with theta part == t
        work = {}
        for m, cp in Rw.items():
            if theta_pt(m) != t: continue
            xit = xi_pt(m)
            for mono, c in cp.items():
                k = (xit, mono)
                v = cadd(work.get(k, CZERO), c)
                if ciszero(v): work.pop(k, None)
                else: work[k] = v
        found = {}
        for deg in (4, 3, 2, 1, 0):
            for n in names:
                if wl[n] != deg: continue
                ds = diag[n]
                xit_d, dcoef = lead[n][ds]
                dc = dcoef[()]
                assert dc[1] == 0 and dc[0] != 0
                cn = {}
                for (xit, mono), c in list(work.items()):
                    if ds in mono:
                        assert xit == xit_d, (n, ds, xit, xit_d)
                        rest = list(mono); rest.remove(ds)
                        cn[tuple(rest)] = cadd(cn.get(tuple(rest), CZERO), c)
                if not cn: continue
                cw = cp_scale(cn, (Fr(1) / dc[0], Fr(0)))
                found[n] = cp_add(found.get(n, {}), cw)
                for s, (xits, cps) in lead[n].items():
                    sub = cp_mul(cw, cps)
                    for mono, c in sub.items():
                        k = (xits, tuple(sorted(mono + (s,))))
                        v = cadd(work.get(k, CZERO), cneg(c))
                        if ciszero(v): work.pop(k, None)
                        else: work[k] = v
        if work:
            raise RuntimeError("jet solve residual at theta part %s: %s keys" % (str(t), len(work)))
        for n, cw in found.items():
            if not cw: continue
            rows.append((t, n, cw))
            TB = gp_scale_cp(basis[n], cw)
            for g in reversed(t):
                TB = gp_mulgen(TB, g)
            for m, c in TB.items():
                v = cp_add(Rw.get(m, {}), cp_scale(c, (Fr(-1), Fr(0))))
                if not v: Rw.pop(m, None)
                else: Rw[m] = v
        if not found:
            raise RuntimeError("stuck at theta part %s" % (str(t),))
    return rows, Rw
