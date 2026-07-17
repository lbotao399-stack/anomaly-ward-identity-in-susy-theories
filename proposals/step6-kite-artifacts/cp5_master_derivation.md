# CP5 — AAA kite master integrals in the common-evanescent DRED ledger

Status: `NON_AUTHORITY_PROPOSAL`.

Notation: $s_1:=q_1^2$, $s_2:=q_2^2$, $u_{12}:=q_1\!\cdot q_2$,
$Q:=q_1+q_2$, $d:=4-2\epsilon$; $d\Omega_4:=\prod_{i=1}^5dx_i\,
\delta(1-\sum_i x_i)$ is the four-dimensional projective simplex measure.
$A,B,C,U,F$ below are Feynman-parameter polynomials, and
$G:=\begin{psmallmatrix}A&C\\C&B\end{psmallmatrix}^{-1}$ is the two-loop Gaussian
covariance matrix before the factor $1/2$ in an ordinary Gaussian second moment.
All numerical data set $\mu^2=1$.

## 1. The insertion lemma (K.11)

For

$$
J_n(\Delta):=\mu^{2\epsilon}\!\int\!\frac{d^dr}{(2\pi)^d}
\frac{1}{(r^2+\Delta)^n}
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}{\Gamma(n)}\Delta^{d/2-n},
$$

the locked one-loop rule gives

$$
\begin{aligned}
L(n,\Delta)
&:=\mu^{2\epsilon}\!\int\!\frac{d^dr}{(2\pi)^d}
\frac{\mu_r^2}{(r^2+\Delta)^n}\\
&=\frac{4-d}{d}\big[J_{n-1}(\Delta)-\Delta J_n(\Delta)\big]\\
&=\epsilon\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-1-d/2)}{\Gamma(n)}
\Delta^{d/2+1-n}.
\end{aligned}
\tag{CP5.1}
$$

Thus, without suppressing any $\epsilon$ dependence,

$$
\begin{aligned}
L(2,\Delta)
&=\epsilon\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(-1+\epsilon)\Delta^{1-\epsilon},\\
L(3,\Delta)
&=\frac{\Gamma(1+\epsilon)}{2(4\pi)^{2-\epsilon}}
\mu^{2\epsilon}\Delta^{-\epsilon}
=\frac{\Gamma(1+\epsilon)}{32\pi^2}
\left(\frac{4\pi\mu^2}{\Delta}\right)^{\epsilon},\\
L(4,\Delta)
&=\epsilon\frac{\mu^{2\epsilon}}{6(4\pi)^{2-\epsilon}}
\Gamma(1+\epsilon)\Delta^{-1-\epsilon},\\
L(3,\Delta)\big|_{\epsilon=0}&=\frac1{32\pi^2}.
\end{aligned}
\tag{CP5.2}
$$

## 2. Exact two-loop quadratic form

For (K3.3),

$$
\sum_{i=1}^5x_iD_i
=A\ell^2+Bk^2+2C\ell\!\cdot k-2r_\ell\!\cdot\ell-2r_k\!\cdot k+H,
$$

with

$$
\begin{aligned}
A&=x_1+x_3+x_4,&B&=x_2+x_3+x_5,&C&=x_3,\\
r_\ell&=x_3Q+x_4q_1,&r_k&=x_3Q+x_5q_2,&
H&=x_3Q^2+x_4s_1+x_5s_2,\\
U&=AB-C^2
=x_1x_2+x_1x_3+x_1x_5+x_2x_3+x_2x_4+x_3x_4+x_3x_5+x_4x_5.
\end{aligned}
\tag{CP5.3}
$$

Completing both loop squares gives $F:=UH-Br_\ell^2-Ar_k^2+2Cr_\ell\!\cdot r_k$ and

$$
\begin{aligned}
F={}&s_1x_1(x_2x_3+x_2x_4+x_3x_4+x_3x_5+x_4x_5)\\
&+s_2x_2(x_1x_3+x_1x_5+x_3x_4+x_3x_5+x_4x_5)
+2u_{12}x_1x_2x_3.
\end{aligned}
\tag{CP5.4}
$$

External shifts are strictly hatted. With

$$
G=\frac1U\begin{pmatrix}B&-C\\-C&A\end{pmatrix},
$$

Wick contraction in the common formal $(d-4)=-2\epsilon$-dimensional evanescent
subspace, with $\mu_r^2=-\widetilde r^{,2}$, gives the following Wick polynomials
after the common Schwinger factors $t^{-1}$ for degree two and $t^{-2}$ for degree
four have been extracted:

$$
\begin{aligned}
\langle\mu_\ell^2\rangle&=\epsilon G_{\ell\ell}=\epsilon\frac BU,&
\langle\mu_k^2\rangle&=\epsilon G_{kk}=\epsilon\frac AU,&
\langle\mu_{\ell k}\rangle&=\epsilon G_{\ell k}=-\epsilon\frac CU,\\
\langle\mu_\ell^2\mu_k^2\rangle
&=\epsilon^2G_{\ell\ell}G_{kk}-\epsilon G_{\ell k}^2
=\frac{\epsilon^2AB-\epsilon C^2}{U^2},\\
\langle\mu_\ell^2\mu_{\ell k}\rangle
&=-\epsilon(1-\epsilon)G_{\ell\ell}G_{\ell k}
=\frac{\epsilon(1-\epsilon)BC}{U^2},\\
\langle\mu_{\ell k}^2\rangle
&=-\frac\epsilon2G_{\ell\ell}G_{kk}
-\frac\epsilon2(1-2\epsilon)G_{\ell k}^2
=-\frac{\epsilon[AB+(1-2\epsilon)C^2]}{2U^2}.
\end{aligned}
\tag{CP5.5}
$$

The $-\epsilon G_{\ell k}^2$ and $-\epsilon G_{\ell\ell}G_{kk}/2$ terms are the exact
$\mu_{\ell k}^2/(2\epsilon)$ angular enhancement required by D3.

## 3. Exact parameter representations of $N_1,\ldots,N_6$

Define

$$
\mathcal C_2(\epsilon):=
\frac{\mu^{4\epsilon}\Gamma(-1+2\epsilon)}{(4\pi)^d},
\qquad
\mathcal C_1(\epsilon):=
\frac{\mu^{4\epsilon}\Gamma(2\epsilon)}{(4\pi)^d}.
$$

The six scalar probes requested in SPEC v2.6 are

$$
\begin{aligned}
N_1&=\mathcal C_2\!\int d\Omega_4\,
(\epsilon^2AB-\epsilon C^2)\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_2&=\mathcal C_2\!\int d\Omega_4\,
\epsilon(1-\epsilon)BC\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_3&=-\frac\epsilon2\mathcal C_2\!\int d\Omega_4\,
[AB+(1-2\epsilon)C^2]\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}},\\
N_4&=-\epsilon\mathcal C_1\!\int d\Omega_4\,
C\frac{F^{-2\epsilon}}{U^{3-3\epsilon}},\\
N_5&=\epsilon\mathcal C_1\!\int d\Omega_4\,
A\frac{F^{-2\epsilon}}{U^{3-3\epsilon}},\\
N_6&=\epsilon\mathcal C_1\!\int d\Omega_4\,
B\frac{F^{-2\epsilon}}{U^{3-3\epsilon}}.
\end{aligned}
\tag{CP5.6}
$$

They are not a CP4-closed parent basis.  The degree-two envelope in (K3.16) also
allows $x^2$, $y^2$, and $yz$, with $x=\mu_\ell^2$, $y=\mu_k^2$,
$z=\mu_{\ell k}$; their denominator masks and coefficients remain
`BLOCKED_CP4_NUMERATOR_INVENTORY`.

The exact change of variables

$$
(\ell,k,q_1,q_2)\longmapsto(k,\ell,q_2,q_1)
$$

maps $D_1\leftrightarrow D_2$, $D_4\leftrightarrow D_5$, $D_3\leftrightarrow D_3$;
hence

$$
\begin{aligned}
N_1(s_1,s_2,u_{12})&=N_1(s_2,s_1,u_{12}),\\
N_3(s_1,s_2,u_{12})&=N_3(s_2,s_1,u_{12}),\\
N_4(s_1,s_2,u_{12})&=N_4(s_2,s_1,u_{12}),\\
N_5(s_1,s_2,u_{12})&=N_6(s_2,s_1,u_{12}).
\end{aligned}
\tag{CP5.7}
$$

## 4. First blocker: the starting-snapshot draft master is incompatible with D3 and the routing

The starting-snapshot formula at commit `cca5d34` (then tagged K3.7) and its stated
mirror require simultaneously

$$
N_1=-\frac{s_1}{3072\pi^4}+O(\epsilon),
\qquad
N_1=-\frac{s_2}{3072\pi^4}+O(\epsilon).
$$

Equation (CP5.7) instead requires a symmetric function. At $s_1=1$, $s_2=2$ the two
claimed finite values differ by

$$
\left(-\frac1{3072\pi^4}\right)
-\left(-\frac2{3072\pi^4}\right)
=\frac1{3072\pi^4}
=3.3417910985300572\times10^{-6}\neq0.
\tag{CP5.8}
$$

The first omitted term is visible before the outer integration. Parameterize
$D_2D_3D_5$ by $\alpha+\eta+\zeta=1$ and write

$$
\begin{aligned}
R&:=\eta(Q-\ell)+\zeta q_2,&k&=K+R,&\widetilde R&=-\eta\widetilde\ell,\\
\Delta_k&=\alpha\eta(Q-\ell)^2+\alpha\zeta q_2^2
+\eta\zeta(q_1-\ell)^2,\\
\mu_k^2&=\mu_K^2+\eta^2\mu_\ell^2-2\eta\mu_{\ell K}.
\end{aligned}
$$

The term odd in $K$ integrates to zero, but the $\eta^2\mu_\ell^2$ term remains:

$$
\begin{aligned}
N_1
=2\!\int_{\alpha+\eta+\zeta=1}\!d\alpha\,d\eta\,d\zeta
\int\!\frac{\mu^{2\epsilon}d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_1D_4}
\left[L(3,\Delta_k)+\eta^2\mu_\ell^2J_3(\Delta_k)\right].
\end{aligned}
\tag{CP5.9}
$$

Keeping only the first bracketed term produces the former $s_1$ branch. Dropping
the second term treats the loop-dependent shift as hatted and violates the common
evanescent subspace of D3. Moreover, the $O(\epsilon)$ part of $L(3,\Delta_k)$ multiplies
an outer divergent integral and cannot be discarded.

## 5. Sector decomposition and pole classification

Set

$$
\begin{aligned}
a&:=x_1+x_4,&x_1&=au,&x_4&=a(1-u),\\
b&:=x_2+x_5,&x_2&=bv,&x_5&=b(1-v),\\
c&:=x_3,&a+b+c&=1,&d\Omega_4&=ab\,da\,db\,du\,dv.
\end{aligned}
$$

Then

$$
\begin{aligned}
U&=ab+c(a+b),\\
F&=s_1au\big[a(1-u)(b+c)+bc\big]
+s_2bv\big[b(1-v)(a+c)+ac\big]
+2u_{12}abcuv.
\end{aligned}
\tag{CP5.10}
$$

$a\to1$ is the $k$-subgraph corner and $b\to1$ is the $\ell$-subgraph corner. A
primary sector followed by $y=r$, $z=rt$ or $y=rt$, $z=r$ gives the following exact
radial powers:

| master | $a\to1$ | $b\to1$ | classification |
|---|---:|---:|---|
| $N_1$ | $\epsilon^2r^{-1+\epsilon}$ | $\epsilon^2r^{-1+\epsilon}$ | finite local |
| $N_2$ | no $r^{-1+\epsilon}$ term | $\epsilon r^{-1+\epsilon}$ | $1/\epsilon$ |
| $N_3$ | $\epsilon r^{-1+\epsilon}$ | $\epsilon r^{-1+\epsilon}$ | $1/\epsilon$ |
| $N_4$ | no $r^{-1+\epsilon}$ term | no $r^{-1+\epsilon}$ term | finite local |
| $N_5$ | $r^{-1+\epsilon}$ | no $r^{-1+\epsilon}$ term | $1/\epsilon$ |
| $N_6$ | no $r^{-1+\epsilon}$ term | $r^{-1+\epsilon}$ | $1/\epsilon$ |

The corner integrals are elementary:

$$
\begin{aligned}
N_2&=-\frac{s_2}{18432\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_3&=\frac{s_1+s_2}{12288\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_5&=\frac1{1024\pi^4}\frac1\epsilon+O(\epsilon^0),\\
N_6&=\frac1{1024\pi^4}\frac1\epsilon+O(\epsilon^0).
\end{aligned}
\tag{CP5.11}
$$

For the two finite local masters, define the exact boundary coefficient

$$
S_{AB}:=\underset{\epsilon=0}{\operatorname{Res}}
\int d\Omega_4\,AB\frac{F^{1-2\epsilon}}{U^{5-3\epsilon}}.
$$

The two primary corners give $s_1/12$ and $s_2/12$.  The remaining parameter
integrals are

$$
\begin{aligned}
\int d\Omega_4\frac{C}{U^3}&=\frac12,\\
S_{AB}&=\frac{s_1+s_2}{12},\\
\int d\Omega_4\frac{C^2F}{U^5}
&=\frac{s_1+s_2}{24}+\frac{u_{12}}{48},\\[2pt]
N_1\big|_{\epsilon=0}
&=-\frac{2(s_1+s_2)-u_{12}}{24576\pi^4},\\
N_4\big|_{\epsilon=0}&=-\frac1{1024\pi^4}.
\end{aligned}
\tag{CP5.12}
$$

At the requested generic point, (CP5.12) gives

$$
N_1\big|_{\epsilon=0}=-\frac{19}{81920\pi^4}
=-2.3810261577026656\times10^{-6},
\qquad
N_4\big|_{\epsilon=0}=-1.0025373295590174\times10^{-5}.
$$

Thus the D3 value of $N_1$ equals neither former draft branch.

## 6. Numerical cross-check and extrapolation

`cp5_sector_numeric.c` applies $r=w^{1/\epsilon}$ exactly to each
$r^{-1+\epsilon}$ sector, so $r^{-1+\epsilon}dr=dw/\epsilon$. The table uses
$524288$ Halton points in each of $12$ randomized replicas; entries below are rounded
to three significant digits.

| $\epsilon$ | $N_1$ | $N_2$ | $N_3$ | $N_4$ | $N_5$ | $N_6$ |
|---:|---:|---:|---:|---:|---:|---:|
| $0.03$ | $-3.47\times10^{-6}$ | $-5.06\times10^{-5}$ | $1.15\times10^{-4}$ | $-1.19\times10^{-5}$ | $4.42\times10^{-4}$ | $4.25\times10^{-4}$ |
| $0.02$ | $-3.06\times10^{-6}$ | $-6.85\times10^{-5}$ | $1.55\times10^{-4}$ | $-1.12\times10^{-5}$ | $6.04\times10^{-4}$ | $5.89\times10^{-4}$ |
| $0.01$ | $-2.70\times10^{-6}$ | $-1.24\times10^{-4}$ | $2.79\times10^{-4}$ | $-1.06\times10^{-5}$ | $1.10\times10^{-3}$ | $1.09\times10^{-3}$ |

Quadratic extrapolation of $N_1,N_4$ and of $\epsilon N_2,\epsilon N_3,
\epsilon N_5,\epsilon N_6$ gives

| quantity | three-point extrapolate | exact value from (CP5.11)--(CP5.12) |
|---|---:|---:|
| $N_1(0)$ | $-2.3855905267\times10^{-6}$ | $-2.3810261577\times10^{-6}$ |
| $\epsilon N_2$ | $-1.1153231543\times10^{-6}$ | $-1.1139303662\times10^{-6}$ |
| $\epsilon N_3$ | $2.5099582310\times10^{-6}$ | $2.5063433239\times10^{-6}$ |
| $N_4(0)$ | $-1.0028852965\times10^{-5}$ | $-1.0025373296\times10^{-5}$ |
| $\epsilon N_5$ | $1.0033565247\times10^{-5}$ | $1.0025373296\times10^{-5}$ |
| $\epsilon N_6$ | $1.0031837624\times10^{-5}$ | $1.0025373296\times10^{-5}$ |

Subtracting the exact poles in (CP5.11), then fitting the three residuals to
$B+C\epsilon+D\epsilon^2$, gives the pointwise finite-part estimators

$$
\begin{aligned}
N_2^{\rm fin}&=-1.1602165675\times10^{-5},&
N_3^{\rm fin}&=2.6661759063\times10^{-5},\\
N_5^{\rm fin}&=9.4335900225\times10^{-5},&
N_6^{\rm fin}&=8.0434019205\times10^{-5}.
\end{aligned}
\tag{CP5.13}
$$

These four decimals are numerical three-point estimators at $\mu^2=1$, not closed
generic-kinematics formulae. The exact pole residues and the exact local values
$N_1(0),N_4(0)$ are analytic results.

## 7. Daughters and tensor-numerator interface

For a denominator subset $S\subseteq\{1,2,3,4,5\}$, $n_S:=|S|$, and a centered
Gaussian moment of evanescent degree $2m$, the common generator is

$$
\mathcal I_{S,m}[P_m]
=\frac{\mu^{4\epsilon}}{(4\pi)^d}
\Gamma(n_S-d-m)
\int d\Omega_{n_S-1}\,
U_S^{-d/2}P_m(G_S)
\left(\frac{F_S}{U_S}\right)^{-(n_S-d-m)}.
\tag{CP5.14}
$$

A one-denominator daughter has $S=\{1,2,3,4,5\}\setminus\{j\}$; the formula fixes
its normalization, but not whether CP4 requests that daughter or which numerator
multiplies it.

For hatted tensor numerators, with $h:=G(r_\ell,r_k)^T$, the centered source is

$$
\mathcal Z_t(J_\ell,J_k)
=\exp\!\left[J_\ell\!\cdot h_\ell+J_k\!\cdot h_k
+\frac1{4t}\left(G_{\ell\ell}J_\ell^2
+2G_{\ell k}J_\ell\!\cdot J_k+G_{kk}J_k^2\right)\right].
\tag{CP5.15}
$$

Every $\ell^{\mu_1}\cdots k^{\nu_r}$ version is obtained by the corresponding source
derivatives. Each covariance contraction contributes one additional inverse Schwinger
scale and therefore uses the shifted Gamma factor in (CP5.14); it cannot be assigned
before the exact CP4 row fixes the tensor rank and denominator mask.

The typed request is

```text
(cp4_row_id, memo_tag, denominator_mask, evanescent_monomial,
 hatted_tensor_word, coefficient)
```

It is admissible only together with a verified CP4 receipt/hash and a row present in
that receipt; hatted tensor words additionally require the covariance-count reduction
fixing the shifted Gamma factor.  The current CP1 gate report has
`explicit_trace_pass=false`; CP2--CP4 are forbidden by SPEC §6. Therefore no request
is currently admitted, and the status is

```text
BLOCKED_CP4_NUMERATOR_INVENTORY
```

The missing $x^2,y^2,yz$ parents, every daughter, and every
$\ell^\mu/k^\mu$ numerator version remain blocked rather than guessed.
