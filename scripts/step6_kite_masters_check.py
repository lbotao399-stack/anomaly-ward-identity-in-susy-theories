#!/usr/bin/env python3
"""My independent check of the mu^2-insertion lemma and master M1.

Lemma (mu1):  mu^{2eps} int d^dk/(2pi)^d  mu_k^2/(k^2+Delta)^n
            = eps * mu^{2eps} (4pi)^{-d/2} Gamma(n-1-d/2)/Gamma(n) * Delta^{d/2+1-n}
derived from the project rule  int mu_k^2 f = ((4-d)/d) int k^2 f  and the
standard J_n = mu^{2eps}(4pi)^{-d/2} Gamma(n-d/2)/Gamma(n) Delta^{d/2-n}.

Checks:
  (a) n=3 anchor -> 1/(32 pi^2) at eps->0 (Delta-independent).
  (b) M1 = int int mu_l^2 mu_k^2 / [l^2 (p-l)^2 k^2 (l-k)^2 (p-l+k)^2]
         = (1/32pi^2) * int_l mu_l^2/(l^2 (p-l)^2) + O(eps)
         = (1/32pi^2) * (-p^2/(96 pi^2)) = -p^2/(3072 pi^4).
     Verify the outer factor: int_l mu_l^2/(l^2(p-l)^2)
        = int_0^1 dx L(2, x(1-x)p^2)  with L from the lemma.
"""
import sympy as sp

eps, Delta, p2, x, mu2 = sp.symbols('eps Delta p2 x mu2', positive=True)
d = 4 - 2*eps

def J(n, D):
    return (4*sp.pi)**(-d/2) * sp.gamma(n - d/2)/sp.gamma(n) * D**(d/2 - n)

def L(n, D):
    """mu_k^2 insertion, from ((4-d)/d)*(J_{n-1} - Delta*J_n)."""
    return sp.simplify(((4-d)/d) * (J(n-1, D) - D*J(n, D)))

# closed form claimed
def Lclaim(n, D):
    return eps * (4*sp.pi)**(-d/2) * sp.gamma(n - 1 - d/2)/sp.gamma(n) * D**(d/2 + 1 - n)

for n in (2, 3, 4):
    diff = sp.simplify(sp.nsimplify(sp.simplify(L(n, Delta) / Lclaim(n, Delta))))
    print(f"n={n}: L/Lclaim = {diff}")

# (a) anchor
anchor = sp.limit(L(3, Delta), eps, 0)
print("anchor n=3, eps->0:", sp.simplify(anchor), " expected", 1/(32*sp.pi**2), "=", sp.nsimplify(anchor*32*sp.pi**2))

# (b) outer factor: int_0^1 dx L(2, x(1-x)p^2), eps->0
L2 = Lclaim(2, x*(1-x)*p2)
outer = sp.integrate(sp.series(L2, eps, 0, 1).removeO(), (x, 0, 1))
outer0 = sp.limit(outer, eps, 0)
print("outer = int mu_l^2/(l^2 (p-l)^2) at eps->0:", sp.simplify(outer0))
print("expected -p2/(96 pi^2):", sp.simplify(outer0 + p2/(96*sp.pi**2)))

M1 = sp.simplify(outer0 / (32*sp.pi**2))
print("M1 =", M1, "  == -p2/3072/pi^4 ?", sp.simplify(M1 + p2/(3072*sp.pi**4)))
