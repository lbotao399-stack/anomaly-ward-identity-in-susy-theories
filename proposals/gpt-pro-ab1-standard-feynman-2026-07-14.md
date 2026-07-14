# GPT Pro ordered-AB1 standard-Feynman calculation — 2026-07-14

Status: `NON_AUTHORITY_PRO_REVIEW`.

Chat: https://chatgpt.com/c/6a56596b-5448-83e8-9284-5a6e4fc5dc65

Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-ab1-pair-standard-feynman/initial-prompt.md`

Prompt SHA-256: `2f8307295b028b317ca07ae29696eca93a8c3850f0c4fe3005584439add1b658`.

Rendered-response body SHA-256: `040d0d7f4f043b77edb28c4724546c607f29599e47d8ecf7a438c1ffa9b64ec9`.

Elapsed: `29m36s`.

The following is the completed visible response exported from the rendered DOM, with TeX recovered from the page's MathML annotations.

## Notation introduced below

$$
\sigma\in\{+1,-1\},\qquad   
Z_\sigma:=\int\mathcal D\Xi\,e^{\sigma S_E}.
$$

Thus $\sigma=+1$ means exponent $e^{+S_E}$, while $\sigma=-1$ means the conventional $e^{-S_E}$.

$$
\widehat g_{\mu\nu}:\text{\(d=4-2\epsilon\) momentum-space metric},\qquad
g_{\mu\nu}:\text{Q4S metric},
$$

$$
g_{\mu\nu}=\widehat g_{\mu\nu}+\widetilde g_{\mu\nu},\qquad
g^\mu{}_\mu=4,\quad
\widehat g^\mu{}_\mu=d,\quad
\widetilde g^\mu{}_\mu=2\epsilon .
$$

$$
\Sigma_2:=\{(y,z)\mid y\geq0,\ z\geq0,\ y+z\leq1\},\qquad x:=1-y-z.
$$

$$
K^{AB}{}_{DE}:=f_{BCD}f_{ACE}.
$$

`Pole` denotes the $1/\epsilon$ coefficient;
$\operatorname{Fin}_{\overline{\rm DR}}$ denotes the finite part with

$$
\overline\mu^{\,2}:=4\pi e^{-\gamma_E}\mu^2.
$$

---

# Project status

The supplied data do **not** determine a unique ordinary-supergraph answer. The unresolved branches are

```
BLOCKED_EUCLIDEAN_EXPONENT_UNSPECIFIED
BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED
BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED
BLOCKED_STEP5A_NK_BRANCH_UNSELECTED
BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED
```

The first two are logically prior to the three retained Project blocks: the sign of the labeled vertices and the raw graph multiplicities already depend on them.

A standard Euclidean $\mathcal N=1$ superfield treatment indeed has opposite quadratic signs for vector and chiral superfields, and its vector propagator depends explicitly on the supersymmetric gauge-fixing choice; Fermi–Feynman gauge is a particular branch, not a consequence of the matter action alone. [arXiv+2arXiv+2](https://arxiv.org/pdf/hep-th/9908171)

---

# 1. `TREE_DESCENDANT`

## 1.1 Exact matter-action expansion

Let

$$
X:=\sqrt2g\,u^UT_U.
$$

From

$$
S_{\rm mat}
=\eta_E h\int d^8z\,\widetilde\Phi_r e^V\Phi_r,
\qquad
\eta_E=-1,\quad h=g^{-2},
$$

and

$$
\widetilde\Phi_r=g\widetilde\phi_r,\qquad
\Phi_r=g\phi_r,\qquad
V=\sqrt2g\,u,
$$

one obtains

$$
S_{\rm mat}
=-\int d^8z\,\widetilde\phi_r e^X\phi_r.
$$

The exponential is

$$
e^X
=1+X+\frac12X^2+\frac16X^3+\cdots ,
$$

with

$$
X^2
=2g^2u^{U_1}u^{U_2}T_{U_1}T_{U_2}.
$$

Therefore

$$
\boxed{
S_{\rm mat}^{(2)}
=-\int d^8z\,\widetilde\phi_r\phi_r
}
$$

$$
\boxed{
S_{\rm mat}^{(3)}
=-\sqrt2g\int d^8z\,
\widetilde\phi_r^A u^U(T_U)^A{}_C\phi_r^C
}
$$

$$
\boxed{
S_{\rm mat}^{(4)}
=-g^2\int d^8z\,
\widetilde\phi_r^A u^{U_1}u^{U_2}
(T_{U_1}T_{U_2})^A{}_C\phi_r^C
}.
$$

No generator-order interchange has been used.

For two **labeled** bosonic $u$-legs, functional differentiation gives

$$
\boxed{
\mathcal V_{\widetilde\phi^A\,u^{U_1}u^{U_2}\phi^C}
=
-\sigma g^2
\left[
(T_{U_1}T_{U_2})^A{}_C+
(T_{U_2}T_{U_1})^A{}_C
\right].
}
$$

The two ordered words remain separate.

---

## 1.2 Euclidean-exponent sign ledger

For the conditional Fermi–Feynman quadratic kernel

$$
S^{(2)}_{\rm FF}
=
\frac12\int d^8z\,u^A\Box u^A
-\int d^8z\,\widetilde\phi_r^A\phi_r^A,
$$

the formal Gaussian inverses are

$$
\boxed{
\langle u^A(p,\theta_1)u^B(-p,\theta_2)\rangle_\sigma
=
-\sigma\,\delta^{AB}
\frac{\delta^4(\theta_{12})}{p^2}
}
$$

and

$$
\boxed{
\langle\phi_r^A(p,\theta_1)
\widetilde\phi_s^B(-p,\theta_2)\rangle_\sigma
=
\sigma\,\delta_{rs}\delta^{AB}
\frac{\delta^4(\theta_{12})}{p^2}.
}
$$

The interaction coefficients in the exponent are

$$
\boxed{
\mathcal V_{\widetilde\phi u\phi}
=
-\sigma\sqrt2g\,(T_U)^A{}_C
}
$$

and

$$
\boxed{
\mathcal V_{\widetilde\phi uu\phi}
=
-\sigma g^2
\left(T_{U_1}T_{U_2}+T_{U_2}T_{U_1}\right)^A{}_C .
}
$$

Hence

| exponent | matter propagator | vector propagator | $\widetilde\phi u\phi$ vertex |
| --- | --- | --- | --- |
| $e^{+S_E}$, $\sigma=+1$ | $+\Delta$ | $-\Delta$ | $-\sqrt2gT_U$ |
| $e^{-S_E}$, $\sigma=-1$ | $-\Delta$ | $+\Delta$ | $+\sqrt2gT_U$ |

---

## 1.3 Antichiral cubic vertex

Write

$$
S_{\widetilde\phi^3}
=
\frac{\sqrt2g}{6}
F_{(rA)(sB)(tC)}
\int d^6\widetilde z\,
\widetilde\phi_r^A\widetilde\phi_s^B\widetilde\phi_t^C,
$$

where

$$
F_{(rA)(sB)(tC)}:=\varepsilon_{rst}c_{ABC}.
$$

Without assuming symmetry of $c_{ABC}$, the labeled rule is

$$
\mathcal V_{1\,2\,3}
=
\sigma\frac{\sqrt2g}{6}
\sum_{\pi\in S_3}
\varepsilon_{r_{\pi(1)}r_{\pi(2)}r_{\pi(3)}}
c_{A_{\pi(1)}A_{\pi(2)}A_{\pi(3)}}.
$$

For

$$
c_{ABC}=c_{[ABC]},
$$

the two antisymmetries make $F$ symmetric under exchange of composite labels $(r,A)$. All six terms are then equal:

$$
\boxed{
\mathcal V_{\widetilde\phi_{r_1}^{A_1}
\widetilde\phi_{r_2}^{A_2}
\widetilde\phi_{r_3}^{A_3}}
=
\sigma\sqrt2g\,
\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
}
$$

Consequently, the proposed sign

$$
+\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}
$$

selects

$$
\boxed{\sigma=+1,\qquad Z=\int\mathcal D\Xi\,e^{+S_E}.}
$$

Under $e^{-S_E}$, the labeled vertex is instead

$$
-\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
$$

This sign cannot be declared fixed until the exponent convention is supplied.

---

## 1.4 Ordered antichiral variation

The first variation is

$$
\begin{aligned}
\delta_{\widetilde\phi_1}S_{\widetilde\phi^3}
&=
\frac{\sqrt2g}{6}
\int d^6\widetilde z\,
\Big[
\varepsilon_{1st}c_{ABC}\,
\delta\widetilde\phi_1^A
\widetilde\phi_s^B\widetilde\phi_t^C\\
&\qquad+
\varepsilon_{s1t}c_{BAC}\,
\widetilde\phi_s^B
\delta\widetilde\phi_1^A
\widetilde\phi_t^C\\
&\qquad+
\varepsilon_{st1}c_{BCA}\,
\widetilde\phi_s^B\widetilde\phi_t^C
\delta\widetilde\phi_1^A
\Big].
\end{aligned}
$$

Since $\widetilde\phi$ is even and $c$ is totally antisymmetric,

$$
\varepsilon_{s1t}c_{BAC}
=
\varepsilon_{1st}c_{ABC},
$$

$$
\varepsilon_{st1}c_{BCA}
=
\varepsilon_{1st}c_{ABC}.
$$

Thus

$$
\boxed{
\delta_{\widetilde\phi_1}S_{\widetilde\phi^3}
=
\frac{\sqrt2g}{2}
\varepsilon_{1st}c_{ABC}
\int d^6\widetilde z\,
\delta\widetilde\phi_1^A
\widetilde\phi_s^B\widetilde\phi_t^C.
}
$$

For $r=1$,

$$
\varepsilon_{1st}
\widetilde\phi_s^B\widetilde\phi_t^C
=
\widetilde\phi_2^B\widetilde\phi_3^C
-
\widetilde\phi_3^B\widetilde\phi_2^C.
$$

Hence the primitive ordered flavor words are exactly

$$
(C_2\times C_3)^B-(C_3\times C_2)^B.
$$

---

## 1.5 Ordered product rule

Since

$$
|\nabla_-|=1,\qquad |A|=0,\qquad |B_1|=1,
$$

the graded Leibniz rule is

$$
\begin{aligned}
\nabla_-(A^AB_1^B)
&=
(\nabla_-A^A)B_1^B
+
(-1)^{|\nabla_-||A|}
A^A\nabla_-B_1^B\\
&=
(\nabla_-A^A)B_1^B
+A^A\nabla_-B_1^B.
\end{aligned}
$$

Therefore, **conditional on** the two single-letter bare-source identities,

$$
\nabla_-A
=-\nabla_+\mathscr E_V-2i(B_s\times C_s),
$$

$$
\nabla_-B_1
=-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t),
$$

one gets

$$
\boxed{
\begin{aligned}
\nabla_-(A^AB_1^B)
={}&-(\nabla_+\mathscr E_V)^A B_1^B
-2i(B_s\times C_s)^A B_1^B\\
&-2A^A\mathscr E_{\widetilde1}^B\\
&-\sqrt2A^A(C_2\times C_3)^B
+\sqrt2A^A(C_3\times C_2)^B .
\end{aligned}
}
$$

All four terms are even:

$$
1+1=0,\qquad 1+1=0,\qquad 0+0=0,\qquad 0+0=0
\pmod2.
$$

The ordered Leibniz calculation is fixed. The derivation of the two single-letter identities is not fixed because the full gauge action, the definitions of $\mathscr E_V,\mathscr E_{\widetilde1}$, the spinor-index conventions, and the normalization of $\nabla_\pm$ were not supplied.

```
BLOCKED_ACCEPTED_ACTION_EOM_NORMALIZATION_UNSPECIFIED
```

---

# 2. `RAW_GRAPH_CENSUS`

Let the ordered source be expanded as

$$
I_{AB_1}
=
I^{(0)}
+gI^{(1)}
+g^2I^{(2)}.
$$

A gauge-covariant bilocal source necessarily has the schematic decomposition

$$
I^{(0)}
=
A^{(1)A}(z)B_1^{(1)B}(w),
$$

$$
I^{(1)}
=
A^{(2)A}(z)B_1^{(1)B}(w)
+
A^{(1)A}(z)B_1^{(2)B}(w)
+
I_{\rm link}^{(1)},
$$

$$
\begin{aligned}
I^{(2)}
={}&
A^{(3)A}B_1^{(1)B}
+A^{(2)A}B_1^{(2)B}
+A^{(1)A}B_1^{(3)B}\\
&+I_{\rm link}^{(2)}
+I_{\rm link\text{-}letter}^{(2)}.
\end{aligned}
$$

The coefficients and color ordering of these terms require explicit definitions of

$$
\mathcal W_+(V),\qquad
\nabla_+,\qquad
\text{the bilocal parallel transporter/source link}.
$$

They are not determined by the matter action.

## 2.1 Candidate triangle occurrences

The minimally allowed ordered occurrences are

$$
\boxed{
\begin{aligned}
&G_1^{(B_1,D)},\qquad G_1^{(D,B_1)},\\
&G_2^{(B_1,D)},\qquad G_2^{(D,B_1)},\\
&G_3^{(C_2,C_3)},\qquad G_3^{(C_3,C_2)}.
\end{aligned}
}
$$

Their status is:

| occurrence | interaction content | action order | possible output | fixed information |
| --- | --- | --- | --- | --- |
| $G_1$ | $I_{AB_1}+\widetilde\Phi V\Phi+VVV$ | $g^2$ | $B_1D,DB_1$ | matter vertex fixed conditionally; $VVV$ and source insertion absent |
| $G_2$ | $I_{AB_1}+2(\widetilde\Phi V\Phi)$ | $g^2$ | $B_1D,DB_1$ | both matter vertices fixed conditionally |
| $G_3$ | $I_{AB_1}+\widetilde\Phi V\Phi+\widetilde\Phi^3$ | $g^2$ | $C_2C_3,C_3C_2$ | primitive relative flavor sign fixed |

No numerical symmetry multiplicity can be assigned before $I^{(0)},I^{(1)},I^{(2)}$ are known.

## 2.2 Required non-triangle orbit

The triangle list is not complete. At the same order one must include

$$
\boxed{
\begin{aligned}
&\text{three EOM denominator cuts},\\
&\text{\(n=2\) matter seagull from }S_{\rm mat}^{(4)},\\
&\text{nonlinear }A^{(2)}B_1^{(1)}\text{ contact},\\
&\text{nonlinear }A^{(1)}B_1^{(2)}\text{ contact},\\
&\text{first source-link completion},\\
&\text{double nonlinear/source-link contacts at }g^2.
\end{aligned}
}
$$

The labeled matter seagull is already fixed:

$$
\boxed{
\mathcal V_{\widetilde\phi^A u^{U_1}u^{U_2}\phi^C}
=
-\sigma g^2
\left[
(T_{U_1}T_{U_2})^A{}_C+
(T_{U_2}T_{U_1})^A{}_C
\right].
}
$$

The remaining contact rules are source-definition dependent.

```
BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED
```

---

# 3. `BD_OUTPUT`

## What is fixed without the HT target

The output parities are

$$
|B_1|+|D_{\dot a}|=1+1=0.
$$

Both ordered outputs are therefore allowed:

$$
(B_1,D),\qquad(D,B_1).
$$

They can arise from $G_1$ and $G_2$, together with their EOM/contact orbits.

The derivative-transport identities are

$$
D_{1\alpha}\delta^4(\theta_{12})
=
-D_{2\alpha}\delta^4(\theta_{12}),
$$

$$
\overline D_{1\dot\alpha}\delta^4(\theta_{12})
=
-\overline D_{2\dot\alpha}\delta^4(\theta_{12}).
$$

Transporting an odd derivative through $B_1$ gives a further sign:

$$
D(FG)
=
(DF)G+(-1)^{|F|}F(DG),
\qquad |B_1|=1.
$$

The number of transport operations depends on the precise source insertion and the $VVV$ rule. Hence neither the relative sign nor the overall coefficient of the two BD words is fixed.

$$
\boxed{
\mathrm{BD}_{\rm Project}:
\quad
\texttt{BLOCKED\_BILOCAL\_SOURCE\_INSERTION\_UNSPECIFIED}.
}
$$

In particular, no justified Project statement of the form

$$
\lambda\,(B_1,D)+\lambda\,(D,B_1)
$$

can presently be made, because $\lambda$ and the equality of the two coefficients have not been derived.

---

# 4. `CC_OUTPUT`

## 4.1 Primitive flavor signs

Let the internal antichiral line at the cubic vertex carry flavor $1$ and color $X$.

For ordered output $(C_2^D,C_3^E)$,

$$
\boxed{
\mathcal V_{1;2,3}^{X;D,E}
=
\sigma\sqrt2g\,
\varepsilon_{123}c_{XDE}
=
+\sigma\sqrt2g\,c_{XDE}.
}
$$

For ordered output $(C_3^D,C_2^E)$,

$$
\boxed{
\mathcal V_{1;3,2}^{X;D,E}
=
\sigma\sqrt2g\,
\varepsilon_{132}c_{XDE}
=
-\sigma\sqrt2g\,c_{XDE}.
}
$$

Because $C_2,C_3$ are even, there is no Koszul sign from commuting them. Thus the primitive $G_3$ flavor ratio is

$$
\boxed{
\frac{
\mathcal A_{G_3}(C_3^D,C_2^E)
}{
\mathcal A_{G_3}(C_2^D,C_3^E)
}
=-1.
}
$$

This fixes the relative flavor sign before source-link and color-word recombination.

The overall coefficient and the final color tensor remain blocked because the contraction of the source colors $A,B$ with the matter generator and the cubic tensor is source-routing dependent.

$$
\boxed{
\mathrm{CC}_{\rm Project}
=
\text{overall coefficient unresolved},
\qquad
(C_2,C_3):(C_3,C_2)=+1:-1
\text{ at the primitive cubic}.
}
$$

---

# 5. `CUTTING_FAILURE_LEDGER`

## 5.1 Genuine DRED/Q4S setup

Consistent DRED uses an infinite-dimensional Q4S containing the quasi-$d$-dimensional momentum space as a subspace. Four-dimensional finite-basis Fierz and Cayley–Hamilton identities cannot be applied to a continued loop vector. [arXiv](https://arxiv.org/pdf/hep-ph/0503129)

Take nonexceptional Euclidean external momenta

$$
p^2>0,\qquad q^2>0,\qquad(p+q)^2>0,
$$

and define

$$
D_0:=\ell^2,\qquad
D_1:=(\ell+p)^2,\qquad
D_2:=(\ell-q)^2.
$$

Consider the rank-two triangle

$$
J_\epsilon^{\mu\nu}(p,q)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^\mu\ell^\nu}{D_0D_1D_2}.
$$

Feynman parametrization gives

$$
\frac1{D_0D_1D_2}
=
2\int_{\Sigma_2}dy\,dz\,
\frac1{(k^2+\Delta)^3},
$$

where

$$
k:=\ell+yp-zq,
$$

$$
r:=yp-zq,
$$

$$
\Delta
=
xy\,p^2+xz\,q^2+yz\,(p+q)^2.
$$

Since

$$
\ell=k-r,
$$

the odd terms vanish and

$$
J_\epsilon^{\mu\nu}
=
J_{2,\epsilon}^{\mu\nu}
+
J_{0,\epsilon}^{\mu\nu}.
$$

---

## 5.2 Rank-two pole

Using

$$
\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu k^\nu}{(k^2+\Delta)^3}
=
\frac{\widehat g^{\mu\nu}}d
\int\frac{d^dk}{(2\pi)^d}
\frac{k^2}{(k^2+\Delta)^3},
$$

and

$$
\frac{k^2}{(k^2+\Delta)^3}
=
\frac1{(k^2+\Delta)^2}
-
\frac{\Delta}{(k^2+\Delta)^3},
$$

one obtains

$$
\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu k^\nu}{(k^2+\Delta)^3}
=
\frac{\widehat g^{\mu\nu}}{4(4\pi)^{d/2}}
\Gamma\!\left(2-\frac d2\right)
\Delta^{d/2-2}.
$$

Since $d=4-2\epsilon$,

$$
\boxed{
J_{2,\epsilon}^{\mu\nu}
=
\widehat g^{\mu\nu}
\frac{\mu^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon}.
}
$$

Its pole is

$$
\boxed{
\operatorname{Pole}J_{2,\epsilon}^{\mu\nu}
=
\frac{\widehat g^{\mu\nu}}{64\pi^2\epsilon}.
}
$$

Its $\overline{\rm DR}$ finite part is

$$
\boxed{
\operatorname{Fin}_{\overline{\rm DR}}
J_{2,\epsilon}^{\mu\nu}
=
-\frac{\widehat g^{\mu\nu}}{32\pi^2}
\int_{\Sigma_2}dy\,dz\,
\ln\frac{\Delta}{\overline\mu^{\,2}}.
}
$$

---

## 5.3 Rank-zero finite term

The shifted-numerator contribution is

$$
\boxed{
J_{0,\epsilon}^{\mu\nu}
=
\frac{\mu^{2\epsilon}\Gamma(1+\epsilon)}
{(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,
r^\mu r^\nu\Delta^{-1-\epsilon}.
}
$$

It has no UV pole. Its finite value is

$$
\boxed{
J_{0,0}^{\mu\nu}
=
\frac1{16\pi^2}
\int_{\Sigma_2}dy\,dz\,
\frac{r^\mu r^\nu}{\Delta}.
}
$$

---

## 5.4 Exact denominator cuts

Cancelling $D_i$ gives three bubbles:

$$
C_0(p,q)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{D_1D_2}
=
B_\epsilon((p+q)^2),
$$

$$
C_1(q)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{D_0D_2}
=
B_\epsilon(q^2),
$$

$$
C_2(p)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{D_0D_1}
=
B_\epsilon(p^2),
$$

where the exact $d$-dimensional bubble is

$$
\boxed{
B_\epsilon(s)
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)
\frac{\Gamma(1-\epsilon)^2}
{\Gamma(2-2\epsilon)}
s^{-\epsilon}.
}
$$

Its pole and finite part are

$$
\boxed{
\operatorname{Pole}B_\epsilon(s)
=
\frac1{16\pi^2\epsilon},
}
$$

$$
\boxed{
\operatorname{Fin}_{\overline{\rm DR}}B_\epsilon(s)
=
\frac1{16\pi^2}
\left(
2-\ln\frac{s}{\overline\mu^{\,2}}
\right).
}
$$

---

## 5.5 Triangle-minus-cut remainder

At the integrand level,

$$
\widehat g_{\mu\nu}J_\epsilon^{\mu\nu}
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat g_{\mu\nu}\ell^\mu\ell^\nu}
{D_0D_1D_2}.
$$

Since loop momentum belongs to QDS,

$$
\widehat g_{\mu\nu}\ell^\mu\ell^\nu
=
\ell^2
=
D_0.
$$

Therefore

$$
\boxed{
\widehat g_{\mu\nu}J_\epsilon^{\mu\nu}
=
B_\epsilon((p+q)^2)
}
$$

exactly.

Define the scalar rank-two coefficient

$$
A_\epsilon(p,q)
:=
\frac{\mu^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon}.
$$

Then

$$
J_{2,\epsilon}^{\mu\nu}
=
\widehat g^{\mu\nu}A_\epsilon.
$$

The regulated QDS cut orbit is

$$
dA_\epsilon
+
\widehat g_{\mu\nu}J_{0,\epsilon}^{\mu\nu}.
$$

A Q4S spin-algebra contraction that prints the formal trace $4$ gives

$$
4A_\epsilon
+
\widehat g_{\mu\nu}J_{0,\epsilon}^{\mu\nu}.
$$

The rank-zero finite term cancels exactly in their difference:

$$
\begin{aligned}
R_{\rm Q4S}
&=
\lim_{\epsilon\to0}
\left[
4A_\epsilon
+\widehat g_{\mu\nu}J_{0,\epsilon}^{\mu\nu}
-dA_\epsilon
-\widehat g_{\mu\nu}J_{0,\epsilon}^{\mu\nu}
\right]\\
&=
\lim_{\epsilon\to0}
(4-d)A_\epsilon\\
&=
\lim_{\epsilon\to0}
2\epsilon
\frac{\mu^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon}\\
&=
\frac1{(4\pi)^2}
\int_{\Sigma_2}dy\,dz\,1\\
&=
\frac1{16\pi^2}\cdot\frac12.
\end{aligned}
$$

Hence the exact elementary DRED remainder is

$$
\boxed{
R_{\rm Q4S}
=
\frac1{32\pi^2}.
}
$$

For the reverse subtraction, cut minus triangle,

$$
R_{\rm reverse}
=
-\frac1{32\pi^2}.
$$

This is the complete universal integral factor. The graph-specific multiplier still requires the explicit numerator, source coefficient, vertex signs, routing multiplicity and color contraction.

---

## 5.6 Contact/ghost/counterterm ledger

| contribution | conditional Fermi–Feynman $g^2$ branch |
| --- | --- |
| $D_0,D_1,D_2$ EOM cuts | exact bubbles above |
| $n=2$ matter contact | $-\sigma g^2(T_{U_1}T_{U_2}+T_{U_2}T_{U_1})$ |
| nonlinear $A^{(2)}$ contact | `BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED` |
| nonlinear $B_1^{(2)}$ contact | `BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED` |
| source-link completion | `BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED` |
| linear Fermi–Feynman gauge-fixing vertex | zero; the gauge-fixing functional is quadratic |
| FP ghost triangle | zero at $g^2$ in the leading linear-source branch: ghosts have no matter vertex, and a closed ghost loop connected to a matter line needs at least three interaction vertices |
| FP ghost with nonlinear source | source dependent; blocked |
| Nielsen–Kallosh ghost | `BLOCKED_STEP5A_NK_BRANCH_UNSELECTED` |
| constant Jacobian from $V,\Phi,\widetilde\Phi$ rescaling | field independent; cancels in normalized correlators |
| nonlinear gauge-measure vertex | gauge parameterization not supplied |
| bulk one-loop $\mathcal N=4$ counterterm | no independent bulk coupling counterterm in a supersymmetry-preserving scheme |
| composite $AB_1$ counterterm | source-renormalization prescription not supplied |
| evanescent operator mixing | Q4S operator basis not supplied |

Bulk finiteness does not remove the need to specify local counterterms for a composite bilocal source.

---

# 6. `SHIFTED_DERIVATIVE_TOWER`

Because the Project supergraph coefficient is blocked, the following subsection is strictly the **external HT comparison**, not an input used to fix the Project branch.

Define

$$
\boxed{
\begin{aligned}
\mathscr T_{m,n}(f,g)
:={}&
\sum_{k=0}^{m}\sum_{l=0}^{n}
T_{m,n;k,l}^{\rm HT}\\
&\times
\left(
\partial_1^k\partial_2^lP_{\dot\alpha}f
\right)
\left(
\partial_1^{m-k}\partial_2^{n-l}
P^{\dot\alpha}g
\right),
\end{aligned}
}
$$

where

$$
\boxed{
T_{m,n;k,l}^{\rm HT}
=
\frac{\binom mk\binom nl}
{(m+n+2)(k+l+1)}.
}
$$

This is the coefficient printed by the shifted holomorphic master integral. [arXiv+1](https://arxiv.org/pdf/2512.07771)

The ordered HT tower is therefore

$$
\boxed{
\begin{aligned}
Q_1\!\left(
b^A\partial_1^m\partial_2^n\beta_1^B
\right)
={}&
\kappa_H^2K^{AB}{}_{DE}
\Big[
\mathscr T_{m,n}(\beta_1^D,c^E)
+\mathscr T_{m,n}(c^D,\beta_1^E)\\
&+\mathscr T_{m,n}(\gamma_2^D,\gamma_3^E)
-\mathscr T_{m,n}(\gamma_3^D,\gamma_2^E)
\Big].
\end{aligned}
}
$$

Some exact levels are:

$$
\boxed{
\mathscr T_{0,0}(f,g)
=
\frac12P_{\dot\alpha}fP^{\dot\alpha}g
}
$$

$$
\boxed{
\mathscr T_{1,0}(f,g)
=
\frac13P_{\dot\alpha}f\,
\partial_1P^{\dot\alpha}g
+
\frac16\partial_1P_{\dot\alpha}f\,
P^{\dot\alpha}g
}
$$

$$
\boxed{
\mathscr T_{0,1}(f,g)
=
\frac13P_{\dot\alpha}f\,
\partial_2P^{\dot\alpha}g
+
\frac16\partial_2P_{\dot\alpha}f\,
P^{\dot\alpha}g
}
$$

$$
\boxed{
\begin{aligned}
\mathscr T_{1,1}(f,g)
={}&
\frac14P_{\dot\alpha}f\,
\partial_1\partial_2P^{\dot\alpha}g\\
&+\frac18\partial_1P_{\dot\alpha}f\,
\partial_2P^{\dot\alpha}g\\
&+\frac18\partial_2P_{\dot\alpha}f\,
\partial_1P^{\dot\alpha}g\\
&+\frac1{12}\partial_1\partial_2P_{\dot\alpha}f\,
P^{\dot\alpha}g .
\end{aligned}
}
$$

$$
\boxed{
\begin{aligned}
\mathscr T_{2,0}(f,g)
={}&
\frac14P_{\dot\alpha}f\,
\partial_1^2P^{\dot\alpha}g\\
&+\frac14\partial_1P_{\dot\alpha}f\,
\partial_1P^{\dot\alpha}g\\
&+\frac1{12}\partial_1^2P_{\dot\alpha}f\,
P^{\dot\alpha}g.
\end{aligned}
}
$$

## Explicit HT factor-two fork

The shifted master integral defines

$$
\boxed{
\mathcal D_{0,0}^{\triangle}(f,g)
=
\frac12P_{\dot\alpha}fP^{\dot\alpha}g.
}
$$

Thus the zero-shift coefficient produced by the integral formula is

$$
\boxed{
\frac{\kappa_H^2}{2}.
}
$$

The separately printed zero-component formula has coefficient

$$
\boxed{\kappa_H^2.}
$$

Therefore

$$
\boxed{
\frac{
\text{printed zero-component coefficient}
}{
\text{coefficient obtained from }\mathcal D_{0,0}^{\triangle}
}
=2.
}
$$

The current public formula simultaneously contains $\mathcal D_{0,0}=\frac12P fPg$ and the separate local expression with coefficient $\kappa^2$. [arXiv+1](https://arxiv.org/pdf/2512.07771)

No branch is selected here.

---

# 7. `PROJECT_VERSUS_HT_MISMATCH_TABLE`

| datum | ordinary Project/Feynman calculation | HT target | status |
| --- | --- | --- | --- |
| ordered source | $A^AB_1^B$, no identification with $B_1^BA^A$ | $b^A\beta_1^B=\beta_1^Bb^A$ | different ordering rules; HT commutativity cannot be imported into Project |
| Euclidean exponent | not supplied | not part of HT calculation | `BLOCKED_EUCLIDEAN_EXPONENT_UNSPECIFIED` |
| antichiral labeled vertex | $+\sqrt2g\,\varepsilon c$ only for $e^{+S_E}$ | cubic BV interaction | Project sign branch unresolved |
| matter propagator | $+\Delta$ for $\sigma=+1$, $-\Delta$ for $\sigma=-1$ | holomorphic propagator | unresolved |
| vector propagator | gauge-fixing dependent | holomorphic $bc$ propagator | `BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED` |
| source-link contacts | not supplied | encoded in shifted holomorphic operation | `BLOCKED_BILOCAL_SOURCE_INSERTION_UNSPECIFIED` |
| $BD$ support | $G_1,G_2$ plus contacts | $(\beta_1,c)+(c,\beta_1)$ | support agrees; coefficients/signs not Project-fixed |
| $CC$ support | $G_3$ plus contacts | $(\gamma_2,\gamma_3)-(\gamma_3,\gamma_2)$ | primitive relative sign $+1:-1$ agrees |
| color tensor | depends on $T_U,c_{ABC}$, source routing and source links | $f_{BCD}f_{ACE}$ | no Project equality established |
| universal DRED local unit | $+1/(32\pi^2)$ for triangle-minus-cut trace $4-d$ | absorbed into $\kappa_H^2$ normalization | exact universal integral, but graph multiplier unresolved |
| $n=2$ matter contact | exact anticommutator word shown above | not separately displayed | must be included before comparison |
| FP ghosts | zero at $g^2$ in leading linear-source FF branch | absent as separate sector | conditional agreement |
| NK ghosts | branch unselected | absent as separate sector | `BLOCKED_STEP5A_NK_BRANCH_UNSELECTED` |
| evanescent mixing | operator basis absent | holomorphic regularization | unresolved scheme comparison |
| derivative tower | source/Fourier routing not fixed | $T_{m,n;k,l}^{\rm HT}$ | `BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED` |
| zero-shift normalization | no Project number | $\kappa_H^2/2$ from $\mathcal D$, $\kappa_H^2$ from separate formula | exact internal factor-two fork |
| accepted overall $BD,CC$ coefficient | **unfixed** | $\kappa_H^2$ convention | target fitting forbidden |

---

## Final regulated conclusion

The action-derived coefficients that are fixed are

$$
S_{\rm mat}^{(3)}=-\sqrt2g\,\widetilde\phi uT\phi,
\qquad
S_{\rm mat}^{(4)}=-g^2\,\widetilde\phi uuTT\phi,
$$

and, for $c_{ABC}=c_{[ABC]}$,

$$
\mathcal V_{\widetilde\phi^3}
=
\sigma\sqrt2g\,\varepsilon c.
$$

The exact universal DRED triangle-minus-cut unit is

$$
\boxed{\frac1{32\pi^2}}.
$$

The primitive $CC$ relative sign is

$$
\boxed{(C_2,C_3):(C_3,C_2)=+1:-1.}
$$

The accepted Project coefficients multiplying the $BD$ and $CC$ sectors cannot be fixed from the supplied conventions. Assigning them from $\kappa_H^2$, from the HT derivative tower, or from the zero-component formula would be target fitting rather than an ordinary superspace Feynman calculation.

