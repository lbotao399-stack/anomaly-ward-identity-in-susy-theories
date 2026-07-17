"""Calibration Level 0: D-algebra anchors of SPEC section 1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from galg import *

OK = True
def check(name, cond):
    global OK
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond: OK = False

# generic momentum matrix at point 0 (symbolic momentum 'r')
M = pmat({'r': 1})
M0 = pmat({})  # zero momentum

# theta^2 at point 0 : -2 th+ th-
th2 = {(gen(0,0), gen(0,1)): cp_const((Fr(-2), Fr(0)))}
# thetabar^2 : +2 tb1 tb2
tb2 = {(gen(0,2), gen(0,3)): cp_const((Fr(2), Fr(0)))}

# (D^2 theta^2)| = -4   (momentum-independent: use symbolic M)
r = apply_word(th2, *W_D2, 0, M)
check("(D^2 theta^2)| = -4", cp_eq(theta_restrict(r), cp_const((Fr(-4), Fr(0)))))

# (Db^2 thetabar^2)| = -4
r = apply_word(tb2, *W_Db2, 0, M)
check("(Db^2 tbar^2)| = -4", cp_eq(theta_restrict(r), cp_const((Fr(-4), Fr(0)))))

# delta4 = theta^2 tbar^2 and [D^2 Db^2 delta4]| = 16
d4 = gp_mul(th2, tb2)
check("delta4(theta) = theta^2*tbar^2 matches stored form", gp_eq(d4, delta4_single(0)))
r = apply_word(d4, *W_Db2, 0, M)
r = apply_word(r, *W_D2, 0, M)
check("[D^2 Db^2 delta4]| = 16", cp_eq(theta_restrict(r), cp_const((Fr(16), Fr(0)))))

# Berezin normalization: int d4th delta4 = 1
check("int d4theta delta4 = 1",
      cp_eq(scalar_part(berezin(delta4_single(0), 0)), cp_const(CONE)))

# {D_a, Db_bd} = 2 P_{a bd} on a generic test polynomial
import itertools
testpoly = gp_zero()
# generic element: sum over all monomials in point-0 gens with distinct symbols
allg = [gen(0, s) for s in range(4)]
cnt = 0
for k in range(5):
    for comb in itertools.combinations(allg, k):
        testpoly = gp_add(testpoly, {tuple(comb): cp_sym("t%d" % cnt)})
        cnt += 1
ok = True
for a in range(2):
    for bd in range(2):
        x1 = apply_letter(apply_letter(testpoly, ('Db', bd, 0, M)), ('D', a, 0, M))
        x2 = apply_letter(apply_letter(testpoly, ('D', a, 0, M)), ('Db', bd, 0, M))
        anti = gp_add(x1, x2)
        expect = gp_scale_cp(testpoly, cp_scale(M[a][bd], (Fr(2), Fr(0))))
        if not gp_eq(anti, expect): ok = False
check("{D_a, Db_bd} = 2 p_{a bd} (all a,bd, generic poly)", ok)
ok = True
for a in range(2):
    for b in range(2):
        x1 = apply_letter(apply_letter(testpoly, ('D', b, 0, M)), ('D', a, 0, M))
        x2 = apply_letter(apply_letter(testpoly, ('D', a, 0, M)), ('D', b, 0, M))
        if gp_add(x1, x2): ok = False
        x1 = apply_letter(apply_letter(testpoly, ('Db', b, 0, M)), ('Db', a, 0, M))
        x2 = apply_letter(apply_letter(testpoly, ('Db', a, 0, M)), ('Db', b, 0, M))
        if gp_add(x1, x2): ok = False
check("{D,D} = {Db,Db} = 0", ok)

# F.6 : delta4(th12) D^2 Db^2 delta4(th12) = 16 delta4(th12); D at point 1, momentum symbolic
d12 = delta4_pair(1, 2)
r = apply_word(d12, *W_Db2, 1, M1 := pmat({'s': 1}))
r = apply_word(r, *W_D2, 1, M1)
lhs = gp_mul(d12, r)
rhs = gp_scale(d12, (Fr(16), Fr(0)))
check("delta4(th12) D^2Db^2 delta4(th12) = 16 delta4(th12)  [F.6]", gp_eq(lhs, rhs))

# also the Db^2 D^2 order
r = apply_word(d12, *W_D2, 1, M1)
r = apply_word(r, *W_Db2, 1, M1)
lhs = gp_mul(d12, r)
check("delta4(th12) Db^2D^2 delta4(th12) = 16 delta4(th12)", gp_eq(lhs, rhs))

# delta4(th12) [word with <2 D and <2 Db] delta4(th12) = 0
words = [ ( (Fr(1),Fr(0)), [] ) ]
for a in range(2):
    words.append(((Fr(1), Fr(0)), [('D', a)]))
    words.append(((Fr(1), Fr(0)), [('Db', a)]))
    for b in range(2):
        words.append(((Fr(1), Fr(0)), [('D', a), ('Db', b)]))
        words.append(((Fr(1), Fr(0)), [('Db', b), ('D', a)]))
ok = True
for co, le in words:
    r = apply_word(d12, co, le, 1, M1)
    if gp_mul(d12, r): ok = False
check("delta4 [words with <2 D and <2 Db] delta4 = 0  (all such words)", ok)

# D_- K_+ = -1/8 D^2 Db^2 D_+  as operator identity on generic 2-point poly
testpoly2 = gp_zero()
allg2 = [gen(1, s) for s in range(4)] + [gen(2, s) for s in range(4)]
cnt = 0
for k in range(9):
    for comb in itertools.combinations(allg2, k):
        testpoly2 = gp_add(testpoly2, {tuple(comb): cp_sym("u%d" % cnt)})
        cnt += 1
# K_+ = -1/4 D_+ Db^2 D_+
Kw = word_concat(((Fr(-1,4),Fr(0)), [('D',0)]), W_Db2, (CONE, [('D',0)]))
lhs = apply_word(testpoly2, *word_concat(((Fr(1),Fr(0)),[('D',1)]), Kw), 1, M1)
rhs = apply_word(testpoly2, *word_concat(((Fr(-1,8),Fr(0)),[]), W_D2, W_Db2, (CONE,[('D',0)])), 1, M1)
check("D_- K_+ = -1/8 D^2 Db^2 D_+ (generic poly, symbolic momentum)", gp_eq(lhs, rhs))

print()
print("LEVEL 0: " + ("ALL ANCHORS PASS" if OK else "FAILURES PRESENT"))
