# GPT Pro ordered-AA derivation correction — 2026-07-14

Status: `NON_AUTHORITY_PRO_REVIEW`.

Chat: https://chatgpt.com/c/6a563e16-0d68-83e8-aaef-928c89fe0b6b

Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-aa-pair-standard-feynman/derivation-prompt.md`

Prompt SHA-256: `0814aa50d9bbe3f28897326285432b85192bda855fab6242496d7c3f889e6a33`.

Elapsed: `29m17s`.

The following is the completed visible response exported from the rendered DOM, with TeX recovered from the page's MathML annotations. Interface labels such as `Pasted text` are retained.

### Notation

$$
x_+\wedge y_+
:=\epsilon^{\dot\alpha\dot\beta}
x_{+\dot\alpha}y_{+\dot\beta},
\qquad
\langle X,Y\rangle
:=(P_{\dot\alpha}X)(P^{\dot\alpha}Y),
$$

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

$$
\operatorname{PP}F
:=\text{\(1/\epsilon\)-coefficient of \(F\)},
\qquad
\Delta_2:=\{(a,b)\mid a\geq0,\ b\geq0,\ a+b\leq1\}.
$$

计算对象仅为 ordered $A^AA^B$ sector；$G$ 与 $M$ triangles 分开，defect 是 $d$-dimensional loop projector 与 four-dimensional cutting projector 的差。Pasted text

---

# CORRECTED_G_RESULT

## 1. Canonical insertion

$$
u=\frac{V}{\sqrt2g},
\qquad
A=g^{-1}\nabla_+\mathcal W_+.
$$

$$
\mathcal W_+^{(1)}
=-\frac18\bar D^2D_+V
=-\frac{\sqrt2g}{8}\bar D^2D_+u.
$$

因此

$$
A^{(1)}
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u
=
K_+^cu,
$$

$$
K_+^c=-\frac1{4\sqrt2}D_+\bar D^2D_+,
$$

$$
D_-K_+^c
=
-\frac1{4\sqrt2}
D_-D_+\bar D^2D_+
=
-\frac1{8\sqrt2}D^2\bar D^2D_+.
$$

一个 marked $D_-$-placement 的 insertion coefficient 为

$$
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=
\frac1{64}.
$$

---

## 2. Wick、vertex、propagator signs

$$
\mathfrak V_{\widetilde W}^c
=
+\frac{ig}{4\hbar}
c_{UCD}D_{\dot\gamma}^D
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}),
$$

$$
\mathfrak V_W^c
=
-\frac{ig}{4\hbar}
c_{VC'E}W^{E\gamma}
(D_{C'\gamma}-D_{V\gamma}).
$$

Vertex product:

$$
\left(+\frac{ig}{4\hbar}\right)
\left(-\frac{ig}{4\hbar}\right)
=
+\frac{g^2}{16\hbar^2}.
$$

Three vector propagators:

$$
(-\hbar)^3=-\hbar^3.
$$

Hence

$$
C_{\mathrm{vertex+prop}}
=
-\frac{\hbar g^2}{16}.
$$

The two labeled cubic vertices give

$$
w_{\mathrm{Wick}}
=
\frac1{2!}(1+1)=1.
$$

The four endpoint rows are

| Endpoint | Vertex-expansion sign | transport sign | product |
| --- | --- | --- | --- |
| $\bar D_CD_{C'}$ | $+1$ | $+1$ | $+1$ |
| $-\bar D_CD_V$ | $-1$ | $-1$ | $+1$ |
| $-\bar D_UD_{C'}$ | $-1$ | $-1$ | $+1$ |
| $+\bar D_UD_V$ | $+1$ | $+1$ | $+1$ |

Berezin factor:

$$
D^2\bar D^2\delta^4(\theta)\big|_{\theta=0}
=(-4)(-4)=16.
$$

For one triangle row, transporting the remaining odd derivative into the common oriented word gives $-1$. Thus

$$
w_{T,j}
=
-\frac1{64}(16)
=
-\frac14,
$$

$$
\sum_{j=1}^4w_{T,j}=-1.
$$

Therefore

$$
C_T
=
\left(-\frac{\hbar g^2}{16}\right)(-1)
=
+\frac{\hbar g^2}{16}.
$$

---

## 3. Triangle pole

Routing:

$$
r_0=k,\qquad
r_1=k+q,\qquad
r_2=k+p+q,
$$

$$
D_0D_1D_2
=
k^2(k+q)^2(k+p+q)^2.
$$

$$
L_1=r_0+r_1=2k+q,
\qquad
L_2=r_1+r_2=2k+p+2q,
$$

$$
T_{m\rho n}:=\sigma_m\bar\sigma_\rho\sigma_n.
$$

The unintegrated graph is

$$
\Gamma_{T,G}
=
\frac{\hbar g^2}{16}
\mathbb F^{AB}{}_{DE}
T_{m\rho n}p^\rho
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}.
$$

Use

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}da\,db\,
\frac1{(\ell^2+\Delta)^3},
$$

with

$$
\ell=k+aq+b(p+q),
$$

$$
\Delta
=
(1-a-b)a\,q^2
+
(1-a-b)b\,(p+q)^2
+
ab\,p^2.
$$

Then

$$
L_1
=
2\ell-2bp+(1-2a-2b)q,
$$

$$
L_2
=
2\ell+(1-2b)p+2(1-a-b)q.
$$

Hence

$$
L_1^mL_2^n
=
4\ell^m\ell^n
+\text{odd-rank terms}
+\text{rank-zero terms}.
$$

Only $4\ell^m\ell^n$ has a logarithmic pole.

Define

$$
I_2(\Delta)
:=
\int_\ell\frac1{(\ell^2+\Delta)^2}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
$$

$$
I_3(\Delta)
:=
\int_\ell\frac1{(\ell^2+\Delta)^3}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(1+\epsilon)}2
\Delta^{-1-\epsilon}.
$$

Exactly,

$$
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=
\frac{\widehat\delta^{mn}}d
\left[I_2(\Delta)-\Delta I_3(\Delta)\right].
$$

Since

$$
\Delta I_3(\Delta)
=
\frac{\epsilon}{2}I_2(\Delta),
$$

$$
I_2-\Delta I_3
=
\left(1-\frac\epsilon2\right)I_2
=
\frac d4I_2,
$$

therefore

$$
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=
\frac{\widehat\delta^{mn}}4I_2(\Delta).
$$

Its pole is

$$
\operatorname{PP}
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=
\frac{\widehat\delta^{mn}}
{64\pi^2\epsilon}.
$$

Consequently

$$
\operatorname{PP}
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}
=
2(4)
\int_{\Delta_2}da\,db\,
\frac{\widehat\delta^{mn}}
{64\pi^2\epsilon}.
$$

$$
\int_{\Delta_2}da\,db=\frac12,
$$

so

$$
\operatorname{PP}
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}
=
\frac{\widehat\delta^{mn}}
{16\pi^2\epsilon}.
$$

Thus

$$
\boxed{
\Gamma_{T,G}^{AB}
=
+\frac{\hbar g^2}{256\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\widehat\delta^{mn}
T_{m\rho n}p^\rho
}
$$

or

$$
\boxed{
\Gamma_{T,G}^{AB}
=
+\frac{\lambda_1}{16\epsilon}
\mathbb F^{AB}{}_{DE}
\widehat\delta^{mn}
T_{m\rho n}p^\rho.
}
$$

---

## 4. Four cut rows

For one selected endpoint row the cut D-word has no final odd-transport sign:

$$
w_{C,j}
=
+\frac1{64}(16)
=
+\frac14.
$$

Hence

$$
C_{C,j}
=
\left(-\frac{\hbar g^2}{16}\right)
\left(+\frac14\right)
=
-\frac{\hbar g^2}{64}.
$$

Define the exact scalar bubble

$$
B(P_j)
=
\int_\ell
\frac1{\ell^2(\ell+P_j)^2}.
$$

Its pole is independent of $P_j$:

$$
\operatorname{PP}B(P_j)
=
\frac1{16\pi^2\epsilon}.
$$

Therefore every row gives

$$
\boxed{
\Gamma_{C,G}^{(j)}
=
-\frac{\hbar g^2}{1024\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}
T_{m\rho n}p^\rho
}
$$

$$
=
-\frac{\lambda_1}{64\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}
T_{m\rho n}p^\rho.
$$

Summing

$$
\bar D_CD_{C'},
\quad
-\bar D_CD_V,
\quad
-\bar D_UD_{C'},
\quad
+\bar D_UD_V,
$$

gives

$$
\boxed{
\Gamma_{C,G}^{AB}
=
-\frac{\hbar g^2}{256\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}
T_{m\rho n}p^\rho
}
$$

$$
=
-\frac{\lambda_1}{16\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}
T_{m\rho n}p^\rho.
$$

---

## 5. Evanescent contraction

$$
\Gamma_{T,G}+\Gamma_{C,G}
=
-\frac{\lambda_1}{16\epsilon}
\mathbb F^{AB}{}_{DE}
\breve\delta^{mn}T_{m\rho n}p^\rho.
$$

Use

$$
\sigma_m\bar\sigma_\rho\sigma_n
+
\sigma_n\bar\sigma_\rho\sigma_m
=
2\delta_{m\rho}\sigma_n
+
2\delta_{n\rho}\sigma_m
-
2\delta_{mn}\sigma_\rho.
$$

Then

$$
\breve\delta^{mn}T_{m\rho n}
=
\frac12\breve\delta^{mn}
(T_{m\rho n}+T_{n\rho m})
$$

$$
=
\breve\delta^{mn}
\left(
\delta_{m\rho}\sigma_n
+
\delta_{n\rho}\sigma_m
-
\delta_{mn}\sigma_\rho
\right)
$$

$$
=
2\breve\delta_\rho{}^n\sigma_n
-
(\breve\delta^m{}_m)\sigma_\rho.
$$

For physical external momentum,

$$
\breve\delta_\rho{}^np^\rho=0,
\qquad
\breve\delta^m{}_m=2\epsilon,
$$

hence

$$
\breve\delta^{mn}T_{m\rho n}p^\rho
=
-2\epsilon\,\sigma_\rho p^\rho.
$$

Thus

$$
-\frac{\lambda_1}{16\epsilon}
(-2\epsilon)
=
+\frac{\lambda_1}{8}.
$$

Therefore

$$
\boxed{
\Gamma_{AA,G}^{AB}
=
\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^DP^{\dot\alpha}A^E
-
(P_{\dot\alpha}A^D)D^{E\dot\alpha}
\right].
}
$$

The independently supplied candidate is verified.

---

## 6. Exact eightfold error

Old insertion:

$$
K_+u
=
\sqrt2\,K_+^cu.
$$

For the bilinear insertion,

$$
\frac{(K_+u)(D_-K_+u)}
{(K_+^cu)(D_-K_+^cu)}
=
(\sqrt2)^2=2.
$$

Old versus corrected vertex pair:

$$
\frac{
\left(\frac g2\right)^2
}{
\left(\frac g4\right)^2
}
=
4.
$$

Therefore

$$
\frac{\Gamma_{G,\mathrm{old}}}
{\Gamma_{G,\mathrm{corrected}}}
=
2\cdot4
=
8.
$$

$$
\lambda_1
=
8\left(\frac{\lambda_1}{8}\right).
$$

The first erroneous line was the use of

$$
X_{(1)}=K_+u
$$

as the canonical $A$-insertion. Under the corrected definitions,

$$
X=\sqrt2\,A,
$$

so reporting the $XX$ graph as an $AA$ graph omitted the division by $2$. The next independent error was using

$$
\pm\frac{ig}{2\hbar}
$$

with the $u$-propagator instead of

$$
\pm\frac{ig}{4\hbar}.
$$

---

# MATTER_BRANCH_A_RESULT

Fix one flavor and one arrow:

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q.
$$

$$
D_i=r_i^2,
\qquad
P:=p+q.
$$

The supplied complete numerator is

$$
N_M^{\mathrm{eff}}
=
4\left[
\det(r_0)(r_{1+}\wedge r_{2+})
-
\det(r_1)(r_{0+}\wedge r_{2+})
\right].
$$

The total prefactor is

$$
+\hbar g^2\mathbb F^{AB}{}_{DE}.
$$

## 1. Finite $2\times2$ determinant reduction

Branch A imposes

$$
\mathsf r=-i\sigma_E^mr_m,
\qquad
\det\mathsf r=-r^2.
$$

Thus

$$
\det(r_0)=-D_0,
\qquad
\det(r_1)=-D_1.
$$

Therefore

$$
N_M^{\mathrm{eff}}
=
4[-D_0(r_{1+}\wedge r_{2+})
+D_1(r_{0+}\wedge r_{2+})].
$$

The complete triangle is

$$
\Gamma_{T,M_r}^{A,\rightarrow}
=
4\hbar g^2\mathbb F^{AB}{}_{DE}
\left[
-\int_k
\frac{r_{1+}\wedge r_{2+}}{D_1D_2}
+
\int_k
\frac{r_{0+}\wedge r_{2+}}{D_0D_2}
\right].
$$

For the first bubble set

$$
\ell=r_1=k-q,
\qquad
r_2=\ell-p.
$$

Then

$$
r_{1+}\wedge r_{2+}
=
\ell_+\wedge(\ell-p)_+
=
-\ell_+\wedge p_+.
$$

For the second bubble,

$$
r_{0+}\wedge r_{2+}
=
k_+\wedge(k-P)_+
=
-k_+\wedge P_+.
$$

Define

$$
B_0(Q^2,\epsilon)
:=
\int_k\frac1{k^2(k-Q)^2}.
$$

Feynman parametrization gives

$$
\int_k\frac{k^m}{k^2(k-Q)^2}
=
\frac{Q^m}{2}B_0(Q^2,\epsilon).
$$

Indeed,

$$
\frac1{k^2(k-Q)^2}
=
\int_0^1dx\,
\frac1{
[(k-(1-x)Q)^2+x(1-x)Q^2]^2
},
$$

and the odd shifted integral vanishes, while

$$
\int_0^1dx\,(1-x)F(x(1-x))
=
\frac12\int_0^1dx\,F(x(1-x)).
$$

Hence

$$
\int_\ell
\frac{\ell_+\wedge p_+}
{\ell^2(\ell-p)^2}
=
\frac12(p_+\wedge p_+)B_0(p^2,\epsilon)
=
0,
$$

$$
\int_k
\frac{k_+\wedge P_+}
{k^2(k-P)^2}
=
\frac12(P_+\wedge P_+)B_0(P^2,\epsilon)
=
0.
$$

Therefore

$$
\boxed{
\Gamma_{T,M_r}^{A,\rightarrow}=0.
}
$$

The reverse arrow gives the same zero:

$$
\boxed{
\Gamma_{T,M_r}^{A,\leftarrow}=0.
}
$$

---

## 2. Denominator-canceling cuts

The two cuts produced by $\det(r_0)$ and $\det(r_1)$ are

$$
\Gamma_{D_0}
=
-4\hbar g^2\mathbb F
\int_k
\frac{r_{1+}\wedge r_{2+}}{D_1D_2}
=
0,
$$

$$
\Gamma_{D_1}
=
+4\hbar g^2\mathbb F
\int_k
\frac{r_{0+}\wedge r_{2+}}{D_0D_2}
=
0.
$$

There is no $D_2$-canceling term:

$$
N_{D_2}=0.
$$

---

## 3. Matter seagull

$$
N_{\mathrm{seagull}}
=
4(r_{0+}\wedge r_{2+})
=
-4(k_+\wedge P_+).
$$

Thus

$$
\Gamma_{\mathrm{seagull}}
=
-4\hbar g^2\mathbb F
\int_k
\frac{k_+\wedge P_+}{k^2(k-P)^2}
$$

$$
=
-4\hbar g^2\mathbb F
\left[
\frac12(P_+\wedge P_+)B_0(P^2,\epsilon)
\right]
=
0.
$$

---

## 4. Vector-Euler-current bubbles

$$
N_{J_C}=-2(k_+\wedge p_+),
$$

$$
\Gamma_{J_C}
=
-2\hbar g^2\mathbb F
\int_k
\frac{k_+\wedge p_+}{k^2(k-p)^2}
$$

$$
=
-\hbar g^2\mathbb F
(p_+\wedge p_+)B_0(p^2,\epsilon)
=
0.
$$

Likewise,

$$
N_{J_B}=-2(k_+\wedge q_+),
$$

$$
\Gamma_{J_B}
=
-\hbar g^2\mathbb F
(q_+\wedge q_+)B_0(q^2,\epsilon)
=
0.
$$

---

## 5. Quadratic-letter and outer-$\Gamma_-$ completions

The canonical quadratic gauge letter is

$$
A^{(2)}
=
-\frac g8D_+\bar D^2[(D_+u),u]
-\frac g4[D_+u,\bar D^2D_+u].
$$

Thus $A^{(2)}A^{(1)}$ contains three quantum $u$-fields.

With two $n=1$ matter vertices, one $u$-field remains unpaired:

$$
\langle uuu\rangle_0=0.
$$

With one $n=1$ and one $n=2$ matter vertex,

$$
I=4,\qquad V=3,
\qquad L=I-V+1=2.
$$

Hence it is two-loop, not one-loop.

For the outer connection,

$$
\Gamma_-^{(1)}
=
\sqrt2g\,D_-u,
$$

so

$$
[\Gamma_-^{(1)},A^{(1)}]A^{(1)}
+
A^{(1)}[\Gamma_-^{(1)},A^{(1)}]
$$

again contains three quantum $u$-fields. The same pairing and loop-count argument gives zero at one loop.

For the matter letter,

$$
B_r
=
D_+\Phi_{c,r}
+
\sqrt2g[D_+u,\Phi_{c,r}]
+\cdots,
$$

whereas

$$
C_r=\widetilde\Phi_{c,r}.
$$

The quadratic part of $B_r$ contains an additional adjoint field $u$; its projection onto the exactly bilinear $B_rC_r$ output is

$$
\Pi_{B_rC_r}^{(2\text{-letter})}
\left(
[D_+u,\Phi_{c,r}]
\widetilde\Phi_{c,r}
\right)
=0.
$$

---

## 6. Two arrows and three flavors

For every $r$,

$$
\Gamma_{M_r}^{A,\rightarrow}=0,
\qquad
\Gamma_{M_r}^{A,\leftarrow}=0.
$$

Therefore

$$
\boxed{
\Gamma_{AA,M}^{A,\mathrm{full}}=0.
}
$$

If one first separates the rank-two projector before imposing the finite determinant identity, its local term is canceled exactly by the remaining finite part:

$$
\left[\Gamma_{T,M}^{A,\mathrm{rank\,2}}\right]_{\mathrm{local}}
=
+\frac{4\lambda_1}{3}\mathbb F
(p_+\wedge q_+),
$$

$$
\left[
\Gamma_{T,M}^{A,\mathrm{rank\,0}}
+
\Gamma_{T,M}^{A,\mathrm{finite\ rank\,2}}
\right]_{\mathrm{local}}
=
-\frac{4\lambda_1}{3}\mathbb F
(p_+\wedge q_+).
$$

Their sum is zero because the complete parent has already reduced to two exact zero bubbles.

---

# MATTER_BRANCH_B_RESULT

## 1. Complete formal triangle decomposition

Introduce the polarization of the formal determinant:

$$
\mathfrak d(x,y)
:=
\frac12[
\det(x+y)-\det x-\det y
],
$$

so that

$$
\det x=\mathfrak d(x,x).
$$

Set

$$
x:=1-a-b,
\qquad
P:=p+q,
$$

$$
s:=aq+bP
=
bp+(a+b)q,
$$

$$
k=\ell+s,
$$

$$
\Delta
=
xa\,q^2
+
xb\,P^2
+
ab\,p^2.
$$

Before the shift,

$$
\frac14N_M^{\mathrm{eff}}
=
\mathfrak d(k,k)(k_+\wedge q_+)
-
\mathfrak d(k,k)(p_+\wedge q_+)
$$

$$
\qquad
-
2\mathfrak d(k,q)(k_+\wedge P_+)
+
\mathfrak d(q,q)(k_+\wedge P_+).
$$

Using

$$
s_+\wedge q_+
=
b(p_+\wedge q_+),
$$

$$
s_+\wedge P_+
=
-a(p_+\wedge q_+),
$$

the even shifted numerator is

$$
\frac14N_{\mathrm{even}}
=
\mathcal Q_2+\mathcal Q_0,
$$

with

$$
\mathcal Q_2
=
(b-1)\mathfrak d(\ell,\ell)
(p_+\wedge q_+)
$$

$$
\qquad
+
2\mathfrak d(\ell,s)
(\ell_+\wedge q_+)
-
2\mathfrak d(\ell,q)
(\ell_+\wedge P_+),
$$

and

$$
\mathcal Q_0
=
\left[
(b-1)\mathfrak d(s,s)
+
2a\mathfrak d(s,q)
-
a\mathfrak d(q,q)
\right]
(p_+\wedge q_+).
$$

The odd part is

$$
\mathcal Q_{\mathrm{odd}}
=
\mathfrak d(\ell,\ell)(\ell_+\wedge q_+)
+
2\mathfrak d(\ell,s)(s_+\wedge q_+)
$$

$$
\qquad
+
\mathfrak d(s,s)(\ell_+\wedge q_+)
-
2\mathfrak d(\ell,s)(p_+\wedge q_+)
$$

$$
\qquad
-
2\mathfrak d(\ell,q)(s_+\wedge P_+)
-
2\mathfrak d(s,q)(\ell_+\wedge P_+)
$$

$$
\qquad
+
\mathfrak d(q,q)(\ell_+\wedge P_+).
$$

Every term in $\mathcal Q_{\mathrm{odd}}$ contains an odd number of $\ell$'s, hence

$$
\int_\ell
\frac{\mathcal Q_{\mathrm{odd}}}
{(\ell^2+\Delta)^3}
=0.
$$

Writing

$$
\mathcal Q_2
=
\ell^m\ell^n\mathcal R_{mn}(a,b;p,q),
$$

the complete triangle is

$$
\boxed{
\Gamma_{T,M_r}^{B,\rightarrow}
=
8\hbar g^2\mathbb F^{AB}{}_{DE}
\int_{\Delta_2}da\,db
\left[
\frac14I_2(\Delta)
\widehat\delta^{mn}
\mathcal R_{mn}
+
I_3(\Delta)\mathcal Q_0
\right].
}
$$

This contains both the rank-two logarithmic part and the finite rank-zero scalar-triangle part.

---

## 2. Fixed rank-two defect

The supplied projector data are

$$
\mathcal R_M[\delta_4]=0,
$$

$$
\mathcal R_M[\widehat\delta]
=
\frac{4\epsilon}{3}
(p_+\wedge q_+).
$$

Therefore

$$
\Gamma_{M_r}^{B,\rightarrow;\mathrm{ev.pole}}
=
\frac{\hbar g^2}{16\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\frac{4\epsilon}{3}
(p_+\wedge q_+)
$$

$$
=
\frac{\hbar g^2}{12\pi^2}
\mathbb F^{AB}{}_{DE}
(p_+\wedge q_+)
$$

$$
=
\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}
\langle B_r^D,C_r^E\rangle.
$$

The reversed arrow reverses the directed matter word:

$$
\Gamma_{M_r}^{B,\leftarrow;\mathrm{ev.pole}}
=
-\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}
\langle C_r^D,B_r^E\rangle.
$$

Thus all three flavors give

$$
\boxed{
\Gamma_{AA,M}^{B,\mathrm{ev.pole}}
=
\frac{4\lambda_1}{3}
\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
\langle B_r^D,C_r^E\rangle
-
\langle C_r^D,B_r^E\rangle
\right].
}
$$

All denominator cuts, the seagull, and both Euler-current bubbles remain zero because their vanishing used only

$$
\int_k
\frac{k^m}{k^2(k-Q)^2}
=
\frac{Q^m}{2}B_0(Q^2,\epsilon)
$$

and

$$
Q_+\wedge Q_+=0.
$$

No Cayley--Hamilton identity was used in those zeroes.

---

## 3. Full Branch-B blocker

The finite remainder needed in addition to the fixed rank-two pole is

$$
8\hbar g^2\mathbb F
\int_{\Delta_2}da\,db
\left[
\frac14
\operatorname{FP}_{\epsilon=0}
\big(
I_2(\Delta)\widehat\delta^{mn}\mathcal R_{mn}
\big)
+
I_3(\Delta)\mathcal Q_0
\right].
$$

The two supplied numbers

$$
\mathcal R_M[\delta_4],
\qquad
\mathcal R_M[\widehat\delta]
$$

fix only the unweighted ultraviolet projector. They do not fix either

$$
\widehat\delta^{mn}\mathcal R_{mn}(a,b;p,q)
\quad\text{for every }(a,b)\in\Delta_2,
$$

or

$$
\mathcal Q_0^{Q4S}(a,b;p,q).
$$

Consequently,

$$
\boxed{
\Gamma_{AA,M}^{B,\mathrm{full}}
\text{ is not determined by the supplied Q4S data.}
}
$$

The minimal missing axiom is the unreduced Q4S Clifford/spinor word

$$
N_M^{Q4S}(k,p,q)
$$

before replacing any chiral spinor contraction by the finite symbol

$$
\det(-i\sigma_E\cdot r).
$$

Equivalently, it is sufficient to supply the pointwise Q4S tensors

$$
\boxed{
\widehat\delta^{mn}\mathcal R_{mn}^{Q4S}(a,b;p,q),
\qquad
\mathcal Q_0^{Q4S}(a,b;p,q)
}
$$

for the whole Feynman simplex. Without them, the alternatives

$$
\Gamma_{AA,M}^{B,\mathrm{full}}
=
\Gamma_{AA,M}^{B,\mathrm{ev.pole}}
$$

and

$$
\Gamma_{AA,M}^{B,\mathrm{full}}=0
$$

cannot be distinguished from the supplied contract.

---

# DRED_RULE_SELECTING_BRANCH

Consistent DRED uses

$$
\delta_4^{mn}
=
\widehat\delta^{mn}
+
\breve\delta^{mn},
$$

$$
\widehat\delta^m{}_m=d,
\qquad
\breve\delta^m{}_m=4-d=2\epsilon,
$$

$$
\widehat\delta\,\breve\delta=0,
\qquad
\ell^m=\widehat\delta^m{}_n\ell^n.
$$

The Q4S Clifford algebra is

$$
\{\gamma^m,\gamma^n\}
=
2\delta_4^{mn}.
$$

Allowed reductions are generated by the Clifford anticommutator, metric-projector relations, cyclic traces, and charge conjugation.

The following finite-dimensional identities are forbidden on a continued loop vector:

$$
2\times2\text{ Cayley--Hamilton},
$$

$$
\det(-i\sigma_E\cdot\ell)=-\ell^2,
$$

$$
\text{finite Weyl-spinor completeness},
$$

$$
\text{four-dimensional Fierz rearrangements}.
$$

Consistent DRED realizes Q4S as an infinite-dimensional formal space; its practical rule is precisely that four-dimensional Fierz identities cannot be used. Hence standard consistent DRED selects Branch B, not Branch A. ar5iv+1

The original Project brief itself left the admissible DRED continuation unfixed. Pasted text

The supplied expression

$$
N_M^{\mathrm{eff}}
=
4[
\det(r_0)(r_{1+}\wedge r_{2+})
-
\det(r_1)(r_{0+}\wedge r_{2+})
]
$$

is already written using a finite $2\times2$ object. Therefore it is sufficient for Branch A and for the stated rank-two projection, but it is not a complete Q4S numerator for the finite Branch-B calculation.

---

# FULL_AA_VERSUS_HT

## 1. Shifted simplex kernel

$$
\mathcal D_{w,z}^{\triangle}(f,g)
=
\int_{\Delta_2}da\,db\,
e^{[z+a(w-z)]\cdot P}P_{\dot\alpha}f\,
e^{[w+b(z-w)]\cdot P}P^{\dot\alpha}g.
$$

Expand

$$
e^{a(w-z)\cdot P}
=
\sum_{r=0}^{\infty}
\frac{a^r}{r!}
((w-z)\cdot P)^r,
$$

$$
e^{b(z-w)\cdot P}
=
\sum_{s=0}^{\infty}
\frac{b^s}{s!}
((z-w)\cdot P)^s.
$$

The simplex moment is

$$
\int_{\Delta_2}da\,db\,a^rb^s
=
\int_0^1da\,a^r
\frac{(1-a)^{s+1}}{s+1}
$$

$$
=
\frac1{s+1}
\frac{\Gamma(r+1)\Gamma(s+2)}
{\Gamma(r+s+3)}
$$

$$
=
\frac{r!s!}{(r+s+2)!}.
$$

Therefore

$$
\mathcal D_{w,z}^{\triangle}(f,g)
=
\sum_{r,s\geq0}
\frac1{(r+s+2)!}
e^{z\cdot P}
((w-z)\cdot P)^rP_{\dot\alpha}f
$$

$$
\qquad\qquad\times
e^{w\cdot P}
((z-w)\cdot P)^sP^{\dot\alpha}g.
$$

At zero shift,

$$
\mathcal D_{0,0}^{\triangle}(f,g)
=
\int_{\Delta_2}da\,db\,
P_{\dot\alpha}fP^{\dot\alpha}g
$$

$$
=
\frac12P_{\dot\alpha}fP^{\dot\alpha}g.
$$

---

## 2. Derivative coefficient

Set $z=0$. If $k$ derivatives in direction $1$ and $l$ derivatives in direction $2$ act on the first field, the parameter factor is

$$
a^{k+l}(1-b)^{m+n-k-l}.
$$

Thus

$$
\int_{\Delta_2}da\,db\,
a^{k+l}(1-b)^{m+n-k-l}
$$

$$
=
\frac1{m+n-k-l+1}
\int_0^1da\,a^{k+l}
\left[
1-a^{m+n-k-l+1}
\right]
$$

$$
=
\frac1{m+n-k-l+1}
\left[
\frac1{k+l+1}
-
\frac1{m+n+2}
\right]
$$

$$
=
\frac1{(k+l+1)(m+n+2)}.
$$

Therefore

$$
\boxed{
T_{m,n;k,l}^{\mathrm{HT}}
=
\frac{\binom mk\binom nl}
{(m+n+2)(k+l+1)}.
}
$$

The triangle Feynman identity contains

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}\cdots .
$$

Hence the Project graph normalized to its local coefficient carries

$$
\boxed{
K_{m,n;k,l}^{P}
=
2T_{m,n;k,l}^{\mathrm{HT}}.
}
$$

In particular,

$$
K_{0,0;0,0}^{P}
=
2\left(\frac12\right)=1.
$$

The numerical factor $2$ is correct, but it is not an additional multiplication of the loop coefficient. The two labeled source/vertex attachments satisfy

$$
\frac1{2!}(1+1)=1.
$$

The remaining factor $2$ is the Feynman-parameter factor

$$
\frac{\Gamma(3)}{\Gamma(1)^3}=2.
$$

Thus the corrected local $G$-coefficient remains

$$
\frac{\lambda_1}{8},
$$

while the shifted formula has coefficient

$$
2\left(\frac{\lambda_1}{8}\right)
=
\frac{\lambda_1}{4}
$$

multiplying $\mathcal D^\triangle$.

---

## 3. Project results

Define

$$
\mathcal G^{DE}
:=
D_{\dot\alpha}^DP^{\dot\alpha}A^E
-
(P_{\dot\alpha}A^D)D^{E\dot\alpha},
$$

$$
\mathcal M^{DE}
:=
\sum_{r=1}^3
\left[
\langle B_r^D,C_r^E\rangle
-
\langle C_r^D,B_r^E\rangle
\right].
$$

### Branch A

$$
\boxed{
\Gamma_{AA}^{A}
=
\mathbb F^{AB}{}_{DE}
\left[
\frac{\lambda_1}{8}\mathcal G^{DE}
+
0\cdot\mathcal M^{DE}
\right].
}
$$

### Branch B, fixed evanescent pole only

$$
\boxed{
\Gamma_{AA}^{B,\mathrm{ev.pole}}
=
\mathbb F^{AB}{}_{DE}
\left[
\frac{\lambda_1}{8}\mathcal G^{DE}
+
\frac{4\lambda_1}{3}\mathcal M^{DE}
\right].
}
$$

The full Branch-B matter coefficient remains blocked by the missing Q4S lift.

---

## 4. Full Project derivative tower

For any fixed local coefficients $C_G,C_M$,

$$
\Gamma_{AA}^{P}
\left(
A^A\partial_1^m\partial_2^nA^B
\right)
=
\mathbb F^{AB}{}_{DE}
\sum_{k=0}^m\sum_{l=0}^n
K_{m,n;k,l}^{P}
$$

$$
\qquad\times
\left[
C_G\mathcal G_{k,l;m,n}^{DE}
+
C_M\mathcal M_{k,l;m,n}^{DE}
\right],
$$

where

$$
\mathcal G_{k,l;m,n}^{DE}
=
\partial_1^k\partial_2^lD_{\dot\alpha}^D\,
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}A)^E
$$

$$
\qquad
-
\partial_1^k\partial_2^l
(P_{\dot\alpha}A)^D\,
\partial_1^{m-k}\partial_2^{n-l}
D^{E\dot\alpha},
$$

and

$$
\mathcal M_{k,l;m,n}^{DE}
=
\sum_{r=1}^3
\Big[
\partial_1^k\partial_2^l(P_{\dot\alpha}B_r)^D
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}C_r)^E
$$

$$
\qquad\qquad
-
\partial_1^k\partial_2^l(P_{\dot\alpha}C_r)^D
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}B_r)^E
\Big].
$$

Thus

$$
\boxed{
K_{m,n;k,l}^{P}
=
\frac{
2\binom mk\binom nl
}{
(m+n+2)(k+l+1)
}.
}
$$

For Branch A,

$$
C_G=\frac{\lambda_1}{8},
\qquad
C_M=0.
$$

For the fixed Branch-B evanescent pole,

$$
C_G=\frac{\lambda_1}{8},
\qquad
C_M=\frac{4\lambda_1}{3}.
$$

---

## 5. HT field map

$$
b\longleftrightarrow-\frac{i}{\sqrt2}A,
\qquad
\partial_{\dot\alpha}c
\longleftrightarrow iD_{\dot\alpha},
$$

$$
\partial_{\dot\alpha}\beta_r
\longleftrightarrow
\frac1{\sqrt2}P_{\dot\alpha}B_r,
\qquad
\partial_{\dot\alpha}\gamma^r
\longleftrightarrow
P_{\dot\alpha}C_r.
$$

Gauge output:

$$
(iD_{\dot\alpha})
\left(-\frac{i}{\sqrt2}P^{\dot\alpha}A\right)
=
\frac1{\sqrt2}D_{\dot\alpha}P^{\dot\alpha}A,
$$

$$
-
\left(-\frac{i}{\sqrt2}P_{\dot\alpha}A\right)
(iD^{\dot\alpha})
=
-\frac1{\sqrt2}
(P_{\dot\alpha}A)D^{\dot\alpha}.
$$

Matter output:

$$
\left(\frac1{\sqrt2}P_{\dot\alpha}B_r\right)
(P^{\dot\alpha}C_r)
=
\frac1{\sqrt2}
\langle B_r,C_r\rangle,
$$

$$
-
(P_{\dot\alpha}C_r)
\left(\frac1{\sqrt2}P^{\dot\alpha}B_r\right)
=
-\frac1{\sqrt2}
\langle C_r,B_r\rangle.
$$

Thus HT requires equal Project coefficients:

$$
C_G=C_M.
$$

Branch A gives

$$
\frac{C_M}{C_G}=0.
$$

The fixed Branch-B rank-two term gives

$$
\frac{C_M}{C_G}
=
\frac{4/3}{1/8}
=
\frac{32}{3}.
$$

Neither equals $1$.

No overall Project-to-HT normalization can change either ratio.

---

## 6. Mismatch table

| Item | Correct graph algebra | Previous/HT value | Earliest mismatch |
| --- | --- | --- | --- |
| Canonical $A$ kernel | $K_+^c=K_+/\sqrt2$ | $K_+$ used with $u$ | $X_{(1)}=K_+u$ was reported as canonical $A$ |
| Bilinear insertion weight | $1/64$ | $1/32$ | missing $1/2$ from two $1/\sqrt2$ insertions |
| Canonical gauge Hessian | $ig/(4\hbar)$ | $ig/(2\hbar)$ | old $v_{\rm old}$ Hessian used with $u$ |
| Pair of Hessians | $g^2/(16\hbar^2)$ | $g^2/(4\hbar^2)$ | factor $4$ |
| Gauge D-word magnitude | $1$ | $2$ | insertion normalization |
| Unintegrated $G$ coefficient | $\hbar g^2/16$ | $\hbar g^2/2$ | factor $8$ |
| $G$-triangle pole | $+\hbar g^2/(256\pi^2\epsilon)$ | $+\hbar g^2/(32\pi^2\epsilon)$ | factor $8$ |
| One $G$-cut row | $-\hbar g^2/(1024\pi^2\epsilon)$ | $-\hbar g^2/(128\pi^2\epsilon)$ | factor $8$ |
| Sum of four $G$-cuts | $-\hbar g^2/(256\pi^2\epsilon)$ | $-\hbar g^2/(32\pi^2\epsilon)$ | factor $8$ |
| Local $G$ defect | $\lambda_1/8$ | $\lambda_1$ | exact eightfold error |
| Matter Branch A | $0$ | nonzero matter target | finite $2\times2$ determinant cancellation |
| Standard DRED choice | Branch B | Branch A determinant identity | Q4S forbids finite Fierz/Cayley--Hamilton |
| Matter Branch-B rank-two defect | $4\lambda_1/3$ | HT-relative coefficient $\lambda_1/8$ would be required | ratio $32/3$ |
| Matter Branch-B full result | not fixed | previously replaced by $\chi_M$ | missing unreduced Q4S spinor word |
| Current bubbles | $0$ | possible contact contribution | $Q_+\wedge Q_+=0$ exactly |
| Matter seagull | $0$ | possible contact contribution | same exact vector-bubble identity |
| Project kernel | $K^P=2T^{HT}$ | $T^{HT}$ | Feynman $\Gamma(3)=2$ |
| Source attachments | $1/2!\times2=1$ | extra graph factor $2$ | attachments must not multiply loop coefficient again |
| $K^P_{0,0;0,0}$ | $1$ | $T^{HT}_{0,0;0,0}=1/2$ | shifted/local normalization fork |
| HT gauge/matter equality | requires $C_G=C_M$ | Branch A: $0$; Branch-B pole: $32/3$ | cannot be repaired by an overall constant |

The HT source itself separately prints a local coefficient twice its shifted/tower $m=n=0$ coefficient; that internal factor-two conflict remains independent of the loop calculation. Pasted text
