# Step 5 target-blind Lyndon--PBW covariant-jet audit

Status: `PBW_PASS__BLOCKED_LINK_COMPLETION_NOT_IN_LOCKED_INPUT`

## 1. Locked notation

Only `contracts/foundations/step-03c-gauge-vector-representation.md` and `contracts/foundations/step-04-extended-sym-notation.md` supply the algebra.  No Step-5 contract, Step-5 engine, or external target was read.  The symbol $+$ denotes one fixed undotted spin-frame slot, with no sum over $+$.

$$
P_{\dot a}:=\boldsymbol{\mathcal D}^{\mathsf V}_{E+\dot a},
\qquad
A:=\boldsymbol\nabla^{\mathsf V}_{E+}\boldsymbol{\mathcal W}^{\mathsf V}_{E+},
\qquad
\operatorname{ad}_A(X):=\llbracket A,X\rrbracket .
$$

From (3C.1), (3C.2), and (3C.44), $\rho_E=1$ and $\epsilon_{++}=0$, hence

$$
\begin{aligned}
[\boldsymbol{\mathcal D}^{\mathsf V}_{E+\dot a},
 \boldsymbol{\mathcal D}^{\mathsf V}_{E+\dot b}]
&=\rho_E\epsilon_{\dot a\dot b}
\frac12\left(
\boldsymbol\nabla^{\mathsf V}_{E+}
\boldsymbol{\mathcal W}^{\mathsf V}_{E+}
+\boldsymbol\nabla^{\mathsf V}_{E+}
\boldsymbol{\mathcal W}^{\mathsf V}_{E+}
\right)
+\rho_E\epsilon_{++}
\bar{\boldsymbol\nabla}^{\mathsf V}_{E(\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{E\dot b)}\\
&=1\cdot\epsilon_{\dot a\dot b}
\boldsymbol\nabla^{\mathsf V}_{E+}
\boldsymbol{\mathcal W}^{\mathsf V}_{E+}
+1\cdot0\cdot
\bar{\boldsymbol\nabla}^{\mathsf V}_{E(\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V}_{E\dot b)}.
\end{aligned}
$$

Acting on an adjoint field gives

$$
[P_{\dot a},P_{\dot b}]
=\epsilon_{\dot a\dot b}\operatorname{ad}_A,
\qquad
\epsilon_{\dot1\dot2}=-1.
$$

Set $P_1:=P_{\dot1}$, $P_2:=P_{\dot2}$, $C:=[P_1,P_2]$.  Then

$$
C=-\operatorname{ad}_A.
$$

## 2. Lyndon Lie basis through degree four

For alphabet $1<2$, the nontrivial Lyndon brackets are

$$
\begin{aligned}
\ell_{12}&=[P_1,P_2]=C,\\
\ell_{112}&=[P_1,C],
&\ell_{122}&=[C,P_2],\\
\ell_{1112}&=[P_1,[P_1,C]],
&\ell_{1122}&=[P_1,[C,P_2]],
&\ell_{1222}&=[[C,P_2],P_2].
\end{aligned}
$$

Because $P_i$ is a covariant derivation,

$$
[P_i,\operatorname{ad}_B]=\operatorname{ad}_{P_iB},
\qquad
[\operatorname{ad}_B,P_i]=-\operatorname{ad}_{P_iB}.
$$

Therefore

$$
\begin{aligned}
\ell_{12}&=-\operatorname{ad}_A,
&\ell_{112}&=-\operatorname{ad}_{P_1A},
&\ell_{122}&=+\operatorname{ad}_{P_2A},\\
\ell_{1112}&=-\operatorname{ad}_{P_1^2A},
&\ell_{1122}&=+\operatorname{ad}_{P_1P_2A},
&\ell_{1222}&=-\operatorname{ad}_{P_2^2A}.
\end{aligned}
$$

The equality $P_1P_2A=P_2P_1A$ used in $\ell_{1122}$ follows exactly from

$$
(P_1P_2-P_2P_1)A=-\llbracket A,A\rrbracket=0,
$$

because $A$ is even.

## 3. PBW symmetrization and exact inverse

Let $\mathfrak L=\operatorname{Lie}\langle P_1,P_2\rangle$, let $S(\mathfrak L)$ be its symmetric algebra, and let $U(\mathfrak L)$ be its universal enveloping algebra.  Let $\operatorname{Perm}(y_1,\ldots,y_k)$ denote the set of distinct permutations of the displayed multiset.  The PBW map used here is the filtered linear map

$$
\operatorname{Sym}_{\rm PBW}:S(\mathfrak L)\longrightarrow U(\mathfrak L),
\qquad
y_1\cdots y_k\longmapsto
\frac1{|\operatorname{Perm}(y_1,\ldots,y_k)|}
\sum_{\tau\in\operatorname{Perm}(y_1,\ldots,y_k)}
y_{\tau(1)}\cdots y_{\tau(k)}.
$$

Let $\operatorname{Sh}(1^m,2^n)$ denote the $\binom{m+n}{m}$ distinct binary words containing $m$ symbols $1$ and $n$ symbols $2$.  For repeated $P_1,P_2$ factors,

$$
J_{m,n}(X):=
\frac1{\binom{m+n}{m}}
\sum_{w\in\operatorname{Sh}(1^m,2^n)}P_wX.
$$

The denominator is $\binom{m+n}{m}$, not $(m+n)!$.

Every binary word has a unique nonincreasing Chen--Fox--Lyndon factorization.  Each standard Lyndon bracket $\ell_w$ has associative leading word $w$ with coefficient one.  Ordered products of these brackets therefore give a triangular word-basis change with unit diagonal.  Symmetrization is consequently a filtered linear isomorphism.  It does not preserve the ordinary product.

| $(m,n)$ | distinct shuffles | coefficient per word |
|---:|---:|---:|
| $(0,0)$ | $1$ | $1$ |
| $(0,1)$ | $1$ | $1$ |
| $(1,0)$ | $1$ | $1$ |
| $(0,2)$ | $1$ | $1$ |
| $(1,1)$ | $2$ | $1/2$ |
| $(2,0)$ | $1$ | $1$ |
| $(0,3)$ | $1$ | $1$ |
| $(1,2)$ | $3$ | $1/3$ |
| $(2,1)$ | $3$ | $1/3$ |
| $(3,0)$ | $1$ | $1$ |
| $(0,4)$ | $1$ | $1$ |
| $(1,3)$ | $4$ | $1/4$ |
| $(2,2)$ | $6$ | $1/6$ |
| $(3,1)$ | $4$ | $1/4$ |
| $(4,0)$ | $1$ | $1$ |

| degree | word dimension | $S(\mathfrak L)$ dimension | forward-inverse | inverse-forward |
|---:|---:|---:|:---:|:---:|
| 0 | 1 | 1 | PASS | PASS |
| 1 | 2 | 2 | PASS | PASS |
| 2 | 4 | 4 | PASS | PASS |
| 3 | 8 | 8 | PASS | PASS |
| 4 | 16 | 16 | PASS | PASS |

All matrix entries were computed in `fractions.Fraction`; no floating-point arithmetic occurs.
The exact degree-$0$ through degree-$4$ word bases, symmetric bases, forward matrices, and inverse matrices are recorded in `audits/step5-pbw-jet-audit.json`.

## 4. Degree-two and degree-three identities

$$
J_{1,1}(X)=\frac12(P_1P_2+P_2P_1)X.
$$

$$
\begin{aligned}
P_1P_2X
&=J_{1,1}(X)+\frac12CX
=J_{1,1}(X)-\frac12\llbracket A,X\rrbracket,\\
P_2P_1X
&=J_{1,1}(X)-\frac12CX
=J_{1,1}(X)+\frac12\llbracket A,X\rrbracket.
\end{aligned}
$$

Define commutative PBW symbols $p_i:=\operatorname{Sym}_{\rm PBW}^{-1}(P_i)$ and retain $\ell_w$ as the Lyndon generators.  Exact inverse images of all degree-three ordered words are:

| ordered word | $\operatorname{Sym}_{\rm PBW}^{-1}$ |
|---|---|
| $P_{1}P_{1}P_{1}$ | $p_1^{3}$ |
| $P_{1}P_{1}P_{2}$ | $p_1^{2}p_2 + p_1\ell_{12} + \frac{1}{6}\ell_{112}$ |
| $P_{1}P_{2}P_{1}$ | $p_1^{2}p_2 - \frac{1}{3}\ell_{112}$ |
| $P_{1}P_{2}P_{2}$ | $p_1p_2^{2} + \frac{1}{6}\ell_{122} + \ell_{12}p_2$ |
| $P_{2}P_{1}P_{1}$ | $p_1^{2}p_2 - p_1\ell_{12} + \frac{1}{6}\ell_{112}$ |
| $P_{2}P_{1}P_{2}$ | $p_1p_2^{2} - \frac{1}{3}\ell_{122}$ |
| $P_{2}P_{2}P_{1}$ | $p_1p_2^{2} + \frac{1}{6}\ell_{122} - \ell_{12}p_2$ |
| $P_{2}P_{2}P_{2}$ | $p_2^{3}$ |

Equivalently, the pure symmetric jets are

$$
\begin{aligned}
J_{2,1}(X)&=\frac13(P_1P_1P_2+P_1P_2P_1+P_2P_1P_1)X,\\
J_{1,2}(X)&=\frac13(P_1P_2P_2+P_2P_1P_2+P_2P_2P_1)X.
\end{aligned}
$$

Let

$$
S_{1C}:=\frac12(P_1C+CP_1),
\qquad
S_{C2}:=\frac12(CP_2+P_2C),
\qquad
C_1:=[P_1,C],
\qquad
C_2:=[C,P_2].
$$

The six mixed ordered words are therefore

$$
\begin{aligned}
P_1P_1P_2&=J_{2,1}+S_{1C}+\frac16C_1,
&P_1P_2P_1&=J_{2,1}-\frac13C_1,
&P_2P_1P_1&=J_{2,1}-S_{1C}+\frac16C_1,\\
P_1P_2P_2&=J_{1,2}+S_{C2}+\frac16C_2,
&P_2P_1P_2&=J_{1,2}-\frac13C_2,
&P_2P_2P_1&=J_{1,2}-S_{C2}+\frac16C_2.
\end{aligned}
$$

Here

$$
C=-\operatorname{ad}_A,
\qquad
C_1=-\operatorname{ad}_{P_1A},
\qquad
C_2=+\operatorname{ad}_{P_2A}.
$$

## 5. Pullback product

$\operatorname{Sym}_{\rm PBW}$ is not an algebra map for the ordinary commutative product:

$$
\operatorname{Sym}_{\rm PBW}(p_1p_2)
=\frac12(P_1P_2+P_2P_1)
\ne P_1P_2
=\operatorname{Sym}_{\rm PBW}(p_1)\operatorname{Sym}_{\rm PBW}(p_2).
$$

Define only the pullback product

$$
f\star g:=\operatorname{Sym}_{\rm PBW}^{-1}
\left(\operatorname{Sym}_{\rm PBW}(f)
\operatorname{Sym}_{\rm PBW}(g)\right).
$$

Then

$$
p_1\star p_2=p_1p_2+\frac12\ell_{12},
\qquad
p_2\star p_1=p_1p_2-\frac12\ell_{12}.
$$

The script checked exactly every homogeneous PBW-basis triple of total degree at most four:

$$
(f\star g)\star h=f\star(g\star h),
\qquad
N_{\rm triples}=351.
$$

It also checked the defining intertwining identity on every homogeneous basis pair of total degree at most four:

$$
\operatorname{Sym}_{\rm PBW}(f\star g)
=\operatorname{Sym}_{\rm PBW}(f)\operatorname{Sym}_{\rm PBW}(g),
\qquad
N_{\rm pairs}=129.
$$

## 6. Commuting-jet projection and link-completion blocker

For a commuting two-direction jet monomial $p_1^mp_2^n$, the unique curvature-free PBW lift is

$$
\operatorname{Sym}_{\rm PBW}(p_1^mp_2^n)
=\frac1{\binom{m+n}{m}}
\sum_{w\in\operatorname{Sh}(1^m,2^n)}P_w.
$$

Define the curvature-forgetting projection

$$
q:S(\mathfrak L)\longrightarrow\mathbb Q[p_1,p_2],
\qquad
q(\ell_w)=0\quad(|w|\ge2).
$$

For $m,n>0$, any single mixed ordered lift has an inverse PBW expansion containing at least one of
$\ell_{12},\ell_{112},\ell_{122},\ldots$; after the Step-3C relation these are explicit curvature words.  The map $q$ erases those words, so $q$ alone is non-injective and cannot define a bidirectional roundtrip.  A roundtrip to a commuting jet tower with no curvature generators is curvature-free before applying $q$ only for the PBW-symmetrized lift.  Thus a bilocal/Wilson/link Taylor completion must combine its connection and endpoint terms into that lift before an invertible no-extra-curvature comparison is possible.

The locked foundations contain no Wilson line, Duhamel expansion, path-ordering rule, bilocal insertion, or link-completion theorem.  Therefore the statement that the actual Step-5 link completion produces this lift is not proved here:

`BLOCKED_LINK_COMPLETION_NOT_IN_LOCKED_INPUT`.
