# Step 5K Euclidean momentum rules and the typed FP inverse

Status: `DERIVED_EXACT_RULES_WITH_EXPLICIT_DRED_INVERSE_DEFECT`.

This audit uses only the inputs admitted by
`CONTRACT-STEP-05K-STRICT-SUPERGRAPH-COMPLETION-001`.  It derives the
quadratic kernels and the action vertices needed at one loop through order
$g^2$, together with the ordered composite-source generating rules and
resolvent signs.  It does not enumerate the seventeen graph objects; it
supplies the typed rules by which those objects must be evaluated.

Primary-memo equation map: `(K.1)--(K.46)` in
`audits/step5k-strict-supergraph-completion.md`.

## 1. Spaces, parity, Fourier convention, and the two inverse squares

The Euclidean full, chiral, and antichiral domains are

$$
\Sigma_{E,8}=(x,\theta,\bar\theta),\qquad
\Sigma_{E,+}=(y,\theta),\qquad
\Sigma_{E,-}=(\widetilde y,\bar\theta),
\tag{K.1}
$$

with the ordered integrals of (3D.4).  The fields used below are

| field | domain | parity | ghost number |
|---|---:|---:|---:|
| $u^A:=V^A/(\sqrt2g)$ | $\Sigma_{E,8}$ | $0$ | $0$ |
| $\Phi_{c,r}^A:=g^{-1}\Phi_r^A$ | $\Sigma_{E,+}$ | $0$ | $0$ |
| $\widetilde\Phi_{c,r}^A:=g^{-1}\widetilde\Phi_r^A$ | $\Sigma_{E,-}$ | $0$ | $0$ |
| $\mathfrak c_+^A$ | $\Sigma_{E,+}$ | $1$ | $+1$ |
| $\widetilde{\mathfrak c}_-^A$ | $\Sigma_{E,-}$ | $1$ | $+1$ |
| $\mathfrak c'_{+,A}$ | $\Sigma_{E,+}^{\vee}$ | $1$ | $-1$ |
| $\widetilde{\mathfrak c}'_{-,A}$ | $\Sigma_{E,-}^{\vee}$ | $1$ | $-1$ |

Euclidean tilded and untilded fields are independent.  Adjoint generators
obey

$$
[T_A,T_B]=ic_{AB}{}^CT_C,\qquad
(T_A^{\rm ad})^B{}_C=ic_{AC}{}^B,\qquad
c_{ABC}=c_{[ABC]}.
\tag{K.2}
$$

The fixed perturbative $\mathcal N=4$ branch is

$$
h:=g^{-2},
\qquad
f_{AB}=\widetilde f_{AB}:=h\kappa_{AB}.
\tag{K.2a}
$$

The more general Step-5A convention
$f=h\kappa+i\mathfrak k$ and
$\widetilde f=h\kappa-i\mathfrak k$ differs by the topological density.
For compactly supported perturbative variations in the trivial topological
sector,

$$
\begin{aligned}
\delta\int\mathfrak k_{AB}F^A\wedge F^B
&=2\int\mathfrak k_{AB}(D\delta A)^A\wedge F^B\\
&=2\int d\!\left(
\mathfrak k_{AB}\delta A^A\wedge F^B\right)
-2\int\mathfrak k_{AB}\delta A^A\wedge(DF)^B\\
&=0,
\end{aligned}
\tag{K.2b}
$$

because the boundary term vanishes and $DF=0$.  Hence its bulk ordered
functional Hessians vanish; it emits no perturbative propagator or vertex
in the census.  Equations (K.54)--(K.55) therefore use exactly (K.2a).

Every momentum is incoming and

$$
X(x)=\int_p e^{ip\cdot x}X(p),\qquad
\int_p:=\int\frac{d^dp}{(2\pi)^d},\qquad
\partial_m\longmapsto ip_m,\qquad d=4-2\epsilon.
\tag{K.3}
$$

Thus a local $n$-leg word always carries

$$
(2\pi)^d\delta^{(d)}\!\left(\sum_{j=1}^np_j\right).
\tag{K.4}
$$

From (2A.41), the momentum-space spinor derivatives acting on a field of
incoming momentum $p$ are

$$
D_a(p)=\partial_a+i(\sigma_E^mp_m)_{a\dot b}\bar\theta^{\dot b},
\qquad
\bar D_{\dot a}(p)=\bar\partial_{\dot a}
-i\theta^b(\sigma_E^mp_m)_{b\dot a},
\tag{K.5}
$$

and

$$
\{D_a(p),\bar D_{\dot b}(p)\}
=-2i(\sigma_E^mp_m)_{a\dot b}.
\tag{K.6}
$$

If a derivative acts on the ordered subword $X_j\cdots X_k$, its momentum
argument is $p_j+\cdots+p_k$, not the momentum of an arbitrarily chosen
leg.

The DRED ledger of Step 5 requires two distinct scalar operators.  Define

$$
\bar\Box_Ee^{ipx}:=-\bar p^2e^{ipx},
\qquad
\Box_de^{ipx}:=-p_d^2e^{ipx},
\qquad
\mu_p^2:=\bar p^2-p_d^2.
\tag{K.7}
$$

Finite spinor words use the four-spin metric and hence $\bar\Box_E$;
regulated propagator denominators use $\Box_d$.  Therefore

$$
\frac{\bar p^2}{p_d^2}
=1+\frac{\mu_p^2}{p_d^2}.
\tag{K.8}
$$

The exact four-spin projectors are

$$
\mathcal P_+^{\bar4}
:=\frac{\bar D^2D^2}{16\bar\Box_E},
\qquad
\mathcal P_-^{\bar4}
:=\frac{D^2\bar D^2}{16\bar\Box_E},
\qquad
\mathcal P_T^{\bar4}
:=-\frac{D^a\bar D^2D_a}{8\bar\Box_E},
\tag{K.9}
$$

so that

$$
\mathcal P_i^{\bar4}\mathcal P_j^{\bar4}
=\delta_{ij}\mathcal P_i^{\bar4},
\qquad
\mathcal P_T^{\bar4}+\mathcal P_+^{\bar4}
+\mathcal P_-^{\bar4}=1.
\tag{K.10}
$$

The regulated kernels

$$
\mathcal R_+^d:=\frac{\bar D^2D^2}{16\Box_d},
\qquad
\mathcal R_-^d:=\frac{D^2\bar D^2}{16\Box_d}
\tag{K.11}
$$

must not be called projectors.  On constrained fields,

$$
\mathcal R_+^dX_+
=\frac{\bar\Box_E}{\Box_d}X_+,
\qquad
\mathcal R_-^dX_-
=\frac{\bar\Box_E}{\Box_d}X_-.
\tag{K.12}
$$

Equations (K.7)--(K.12) are the typed form of the Step-5 rule that finite
superspace spin words use $\bar\delta$, whereas propagator inverses use
$\delta_d$.

## 2. Ordered differentiation and Euclidean graph factors

For a homogeneous ordered word, the locked left derivative is

$$
\frac{\vec\delta}{\delta X_j}
(X_1\cdots X_n)
=(-1)^{\epsilon_{X_j}\sum_{k<j}\epsilon_{X_k}}
X_1\cdots\widehat X_j\cdots X_n.
\tag{K.13}
$$

The action Hessian with labeled order $(X_1,\ldots,X_n)$ is

$$
\mathcal C_E[X_1,\ldots,X_n]
:=\frac{\vec\delta}{\delta X_n}\cdots
\frac{\vec\delta}{\delta X_1}S_E.
\tag{K.14}
$$

For a permutation $\pi$, the only fermionic reordering sign is

$$
(-1)^{\kappa(\pi)}
=(-1)^{\sum_{i<j,\,\pi(i)>\pi(j)}\epsilon_i\epsilon_j}.
\tag{K.15}
$$

Since the Euclidean exponent is $-S_E/\hbar+\mathscr J_E/\hbar$, an
ordinary action vertex and a source vertex carry, respectively,

$$
\mathfrak v_E[X_1,\ldots,X_n]
=-\frac1\hbar\mathcal C_E[X_1,\ldots,X_n],
\qquad
\mathfrak v_{J,E}[X_1,\ldots,X_n]
=+\frac1\hbar\mathcal C_{J,E}[X_1,\ldots,X_n].
\tag{K.16}
$$

An oriented internal edge carries

$$
\mathfrak p_E=\hbar K^{-1}.
\tag{K.17}
$$

Equations (K.13)--(K.17) reproduce (5A.63) without an implicit Lorentzian
$i$.  An unlabeled graph is divided once by the automorphism group that
preserves field type, chirality, edge orientation, derivative slot, and
ordered color word.

The exact full-to-half measure identities are

$$
\int_{E,8}U
=\int_{E,+}\left(-\frac14\bar D^2\right)U
=\int_{E,-}\left(-\frac14D^2\right)U.
\tag{K.18a}
$$

Conversely, for a chiral $X_+$ or antichiral $X_-$ on the residual-free
four-spin complement,

$$
\int_{E,+}X_+
=\int_{E,8}\left(-\frac{D^2}{4\bar\Box_E}\right)X_+,
\qquad
\int_{E,-}X_-
=\int_{E,8}\left(-\frac{\bar D^2}{4\bar\Box_E}\right)X_-.
\tag{K.18b}
$$

Indeed,

$$
\left(-\frac14\bar D^2\right)
\left(-\frac{D^2}{4\bar\Box_E}\right)X_+
=\frac{\bar D^2D^2}{16\bar\Box_E}X_+
=X_+,
\tag{K.18c}
$$

and the antichiral identity follows with $D^2\bar D^2$.  Replacing
$\bar\Box_E^{-1}$ in (K.18b) by $\Box_d^{-1}$ is a regulated line, not the
exact inverse; it produces the ratio in (K.12).  No derivative in
(K.18a)--(K.18c) may be moved through an odd ghost word without the sign
from (K.13).

## 3. Vector and adjoint-chiral quadratic blocks

The linear field strengths obtained from (5A.49)--(5A.50) are

$$
\mathcal W_a^{(1)}=-\frac18\bar D^2D_aV,
\qquad
\widetilde{\mathcal W}_{\dot a}^{(1)}
=-\frac18D^2\bar D_{\dot a}V.
\tag{K.19}
$$

Using the locked coupling (K.2a), the canonical vector coordinate is

$$
V:=\sqrt2g\,u.
\tag{K.19a}
$$

The invariant vector quadratic term and the fixed Fermi--Feynman averaging
term are

$$
S_{E,V,{\rm inv}}^{(2)}
=\frac h4\int_{E,8}V\cdot\bar\Box_E
\mathcal P_T^{\bar4}V,
\qquad
S_{E,V,{\rm gf}}^{(2)}
=\frac h4\int_{E,8}V\cdot\bar\Box_E
\left(\mathcal P_+^{\bar4}+\mathcal P_-^{\bar4}\right)V.
\tag{K.20}
$$

By (K.10), their sum gives the exact four-spin quadratic block

$$
S_{E,V}^{(2)}
=\frac12\int_{E,8}V^A(K_{E,\bar4}^V)_{AB}V^B,
\qquad
(K_{E,\bar4}^V)_{AB}
=\frac h2\kappa_{AB}\bar\Box_E.
\tag{K.21}
$$

Its exact inverse on the residual-free four-spin space is

$$
(K_{E,\bar4}^V)^{-1\,AB}
=2g^2\kappa^{AB}\bar\Box_E^{-1},
\qquad
(K_{E,\bar4}^V)_{AC}
(K_{E,\bar4}^V)^{-1\,CB}
=\delta_A{}^B.
\tag{K.22}
$$

Substitution of (K.19a) into (K.21) gives every normalization factor:

$$
\begin{aligned}
S_{E,V}^{(2)}
&=\frac12\int_{E,8}
(\sqrt2g\,u^A)
\left(\frac h2\kappa_{AB}\bar\Box_E\right)
(\sqrt2g\,u^B)\\
&=\frac12\int_{E,8}
u^A\left(2g^2\frac h2\kappa_{AB}\bar\Box_E\right)u^B\\
&=\frac12\int_{E,8}
u^A\left(g^2h\,\kappa_{AB}\bar\Box_E\right)u^B\\
&=\frac12\int_{E,8}
u^A\kappa_{AB}\bar\Box_Eu^B,
\qquad g^2h=g^2g^{-2}=1.
\end{aligned}
\tag{K.22a}
$$

Therefore

$$
(K_{E,\bar4}^u)_{AB}=\kappa_{AB}\bar\Box_E,
\qquad
(K_{E,\bar4}^u)^{-1\,AB}
=\kappa^{AB}\bar\Box_E^{-1}.
\tag{K.23}
$$

The DRED line replaces only the inverse scalar square:

$$
(K_E^u)^{-1\,AB}_{d}
:=\kappa^{AB}\Box_d^{-1}.
\tag{K.23a}
$$

Therefore the DRED momentum-space vector line is

$$
\boxed{
\langle u^A(p,1)u^B(p',2)\rangle_E
=-(2\pi)^d\delta^{(d)}(p+p')
\frac{\hbar\kappa^{AB}}{p_d^2}
\delta^4(\theta_1-\theta_2).}
\tag{K.24}
$$

Its regulated inverse check retains the same scalar defect as (K.12):

$$
\boxed{
(K_{E,\bar4}^u)_{AC}(K_E^u)^{-1\,CB}_{d}
=(K_E^u)^{-1\,BC}_{d}(K_{E,\bar4}^u)_{CA}
=\frac{\bar\Box_E}{\Box_d}\delta_A{}^B
=\left(1+\frac{\mu_p^2}{p_d^2}\right)\delta_A{}^B.}
\tag{K.24a}
$$

For the canonical adjoint chirals,

$$
S_{E,\Phi}^{(2)}
=-\sum_{r=1}^3\int_{E,8}
\widetilde\Phi_{c,r}\cdot\Phi_{c,r}.
\tag{K.25}
$$

On the exact four-spin constrained spaces,

$$
K_E^{\Phi\widetilde\Phi}
=-\kappa\mathbf1_+,
\qquad
(K_E^{\Phi\widetilde\Phi})^{-1}_{\bar4}
=-\kappa^{-1}\mathcal P_+^{\bar4},
\tag{K.26}
$$

and

$$
K_E^{\Phi\widetilde\Phi}
(K_E^{\Phi\widetilde\Phi})^{-1}_{\bar4}
=\mathbf1_+,
\qquad
(K_E^{\Phi\widetilde\Phi})^{-1}_{\bar4}
K_E^{\Phi\widetilde\Phi}
=\mathbf1_+.
\tag{K.27}
$$

For the reversed oriented block on the antichiral constrained space,

$$
K_E^{\widetilde\Phi\Phi}
=-\kappa\mathbf1_-,
\qquad
(K_E^{\widetilde\Phi\Phi})^{-1}_{\bar4}
=-\kappa^{-1}\mathcal P_-^{\bar4},
\tag{K.27a}
$$

and both ordered compositions are

$$
K_E^{\widetilde\Phi\Phi}
(K_E^{\widetilde\Phi\Phi})^{-1}_{\bar4}
=\mathbf1_-,
\qquad
(K_E^{\widetilde\Phi\Phi})^{-1}_{\bar4}
K_E^{\widetilde\Phi\Phi}
=\mathbf1_-.
\tag{K.27b}
$$

The DRED-regulated line replaces $\mathcal P_+^{\bar4}$ by
$\mathcal R_+^d$:

$$
\boxed{
\begin{aligned}
\langle\Phi_{c,r}^A(p,1)
\widetilde\Phi_{c,s}^B(p',2)\rangle_E
={}&(2\pi)^d\delta^{(d)}(p+p')\delta_{rs}
\frac{\hbar\kappa^{AB}}{16p_d^2}\\
&\times\bar D_1^2(p)D_1^2(p)
\delta^4(\theta_1-\theta_2).
\end{aligned}}
\tag{K.28}
$$

The reversed orientation uses $\mathcal R_-^d$.  Its regulated inverse
check is not the four-spin identity:

$$
K_E^{\Phi\widetilde\Phi}
(K_E^{\Phi\widetilde\Phi})^{-1}_{d}
=\frac{\bar\Box_E}{\Box_d}\mathbf1_+
=\left(1+\frac{\mu_p^2}{p_d^2}\right)\mathbf1_+.
\tag{K.29}
$$

Equation (K.29), rather than an untyped assertion that the chiral line is an
exact DRED inverse, is the required matter-line inverse ledger.

## 4. Derivation of the odd FP block

### 4.1 Free FP map

At trivial background, the zeroth-order Bernoulli word in (5A.57) is

$$
\left.\mathbf s_EV\right|_{V=0}
=i(\widetilde{\mathfrak c}_--\mathfrak c_+).
\tag{K.30}
$$

The gauge conditions are

$$
\mathcal F_+=-\frac14\bar D^2V,
\qquad
\mathcal F_-=-\frac14D^2V.
\tag{K.31}
$$

Using

$$
\bar D_{\dot a}\mathfrak c_+=0,
\qquad
D_a\widetilde{\mathfrak c}_-=0,
\tag{K.32}
$$

their BRST variations are, without a suppressed term,

$$
\begin{aligned}
\mathbf s_E\mathcal F_+
&=-\frac14\bar D^2 i
(\widetilde{\mathfrak c}_--\mathfrak c_+)
=-\frac i4\bar D^2\widetilde{\mathfrak c}_-,\\
\mathbf s_E\mathcal F_-
&=-\frac14D^2 i
(\widetilde{\mathfrak c}_--\mathfrak c_+)
=+\frac i4D^2\mathfrak c_+.
\end{aligned}
\tag{K.33}
$$

Define the typed spaces

$$
\mathscr G:=\mathscr G_+\oplus\mathscr G_-,
\qquad
\mathscr F:=\mathscr F_+\oplus\mathscr F_-,
\tag{K.34}
$$

with ordered columns

$$
\mathbf c:=
\begin{pmatrix}\mathfrak c_+\\
\widetilde{\mathfrak c}_-
\end{pmatrix},
\qquad
\mathbf c':=
\begin{pmatrix}\mathfrak c'_+\\
\widetilde{\mathfrak c}'_-
\end{pmatrix}.
\tag{K.35}
$$

The gauge-tangent FP map and its domain are

$$
\boxed{
\mathcal M_E^{(0)}:
\mathscr G^{\perp}\longrightarrow\mathscr F^{\perp},
\qquad
\mathcal M_E^{(0)}=
\begin{pmatrix}
0&-\dfrac i4\bar D^2\\[2mm]
+\dfrac i4D^2&0
\end{pmatrix}.}
\tag{K.36}
$$

The superscript $\perp$ removes
$\ker\mathcal M_E^{(0)}$, exactly as in (3D.92).  No inverse is asserted
on the residual sector.

The ghost term in the gauge-fixed action is

$$
S_{E,{\rm FP}}^{(2)}
=-\langle\mathbf c',\mathcal M_E^{(0)}\mathbf c\rangle_E
=\langle\mathbf c',K_E^{\rm FP}\mathbf c\rangle_E,
\tag{K.37}
$$

where the ordered action Hessian is

$$
\boxed{
K_E^{\rm FP}:=-\mathcal M_E^{(0)}
=\begin{pmatrix}
0&+\dfrac i4\bar D^2\\[2mm]
-\dfrac i4D^2&0
\end{pmatrix}:
\mathscr G^{\perp}\longrightarrow\mathscr F^{\perp}.}
\tag{K.38}
$$

This reproduces the two terms of (5A.60):

$$
S_{E,{\rm FP}}^{(2)}
=\frac i4\int_{E,+}\mathfrak c'_+\bar D^2
\widetilde{\mathfrak c}_-
-\frac i4\int_{E,-}\widetilde{\mathfrak c}'_-D^2
\mathfrak c_+.
\tag{K.39}
$$

For one coefficient-basis word

$$
S_{E,{\rm FP}}^{(2)}=b_\alpha K^\alpha{}_i g^i,
\qquad \epsilon_b=\epsilon_g=1,
\tag{K.39a}
$$

the two left derivatives are

$$
\frac{\vec\partial S}{\partial b_\alpha}
=K^\alpha{}_ig^i,
\qquad
\frac{\vec\partial S}{\partial g^i}
=-b_\alpha K^\alpha{}_i.
\tag{K.39b}
$$

The second minus sign is exactly
$(-1)^{\epsilon_g\epsilon_b}=-1$ from (K.13).  Consequently

$$
\mathcal C_E[b_\alpha,g^i]=+K^\alpha{}_i,
\qquad
\mathcal C_E[g^i,b_\alpha]=-K^\alpha{}_i,
\tag{K.39c}
$$

with endpoint exchange, dual transpose, and superspace integration by parts
understood in the second ordered kernel.  Thus the two endpoint orders are
not two independent sign conventions.

### 4.2 Exact four-spin left and right inverse

The exact algebraic inverse is

$$
\boxed{
(K_E^{\rm FP})^{-1}_{\bar4}
=\begin{pmatrix}
0&+\dfrac i4\bar\Box_E^{-1}\bar D^2\\[2mm]
-\dfrac i4\bar\Box_E^{-1}D^2&0
\end{pmatrix}:
\mathscr F^{\perp}\longrightarrow\mathscr G^{\perp}.}
\tag{K.40}
$$

The right-inverse check, $K_E^{\rm FP}(K_E^{\rm FP})^{-1}_{\bar4}=1$
on the codomain, is

$$
\begin{aligned}
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_{\bar4}
&=
\begin{pmatrix}
\dfrac1{16}\bar D^2D^2\bar\Box_E^{-1}&0\\[2mm]
0&\dfrac1{16}D^2\bar D^2\bar\Box_E^{-1}
\end{pmatrix}\\
&=
\begin{pmatrix}
\mathcal P_+^{\bar4}&0\\0&\mathcal P_-^{\bar4}
\end{pmatrix}
=\mathbf1_{\mathscr F^{\perp}}.
\end{aligned}
\tag{K.41}
$$

Every scalar coefficient in (K.41) is fixed:

$$
\left(+\frac i4\right)
\left(-\frac i4\right)=+\frac1{16},
\qquad
\left(-\frac i4\right)
\left(+\frac i4\right)=+\frac1{16}.
\tag{K.42}
$$

The left-inverse check,
$(K_E^{\rm FP})^{-1}_{\bar4}K_E^{\rm FP}=1$ on the domain, is

$$
\begin{aligned}
(K_E^{\rm FP})^{-1}_{\bar4}K_E^{\rm FP}
&=
\begin{pmatrix}
\dfrac1{16}\bar\Box_E^{-1}\bar D^2D^2&0\\[2mm]
0&\dfrac1{16}\bar\Box_E^{-1}D^2\bar D^2
\end{pmatrix}\\
&=
\begin{pmatrix}
\mathcal P_+^{\bar4}&0\\0&\mathcal P_-^{\bar4}
\end{pmatrix}
=\mathbf1_{\mathscr G^{\perp}}.
\end{aligned}
\tag{K.43}
$$

Thus the former claim that the odd FP block had no typed inverse is closed on
the declared residual complement.

### 4.3 DRED-regulated FP line and its exact defect

The regulated line uses the full $d$-dimensional scalar denominator:

$$
\boxed{
(K_E^{\rm FP})^{-1}_{d}
=\begin{pmatrix}
0&+\dfrac i4\Box_d^{-1}\bar D^2\\[2mm]
-\dfrac i4\Box_d^{-1}D^2&0
\end{pmatrix}.}
\tag{K.44}
$$

It has the momentum representative

$$
(K_E^{\rm FP})^{-1}_{d}(p)
=\begin{pmatrix}
0&-\dfrac{i}{4p_d^2}\bar D^2(p)\\[2mm]
+\dfrac{i}{4p_d^2}D^2(p)&0
\end{pmatrix}.
\tag{K.45}
$$

The regulated right-inverse composition is

$$
\begin{aligned}
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_{d}
&=
\begin{pmatrix}
\dfrac{\bar D^2D^2}{16\Box_d}&0\\[2mm]
0&\dfrac{D^2\bar D^2}{16\Box_d}
\end{pmatrix}\\
&=\frac{\bar\Box_E}{\Box_d}
\mathbf1_{\mathscr F^{\perp}}.
\end{aligned}
\tag{K.46}
$$

The regulated left-inverse composition is independently

$$
(K_E^{\rm FP})^{-1}_{d}K_E^{\rm FP}
=\frac{\bar\Box_E}{\Box_d}
\mathbf1_{\mathscr G^{\perp}}.
\tag{K.47}
$$

For an internal line $r$, (K.46)--(K.47) become

$$
\boxed{
K_E^{\rm FP}(r)(K_E^{\rm FP})^{-1}_{d}(r)-1
=(K_E^{\rm FP})^{-1}_{d}(r)K_E^{\rm FP}(r)-1
=\frac{\mu_r^2}{r_d^2}.}
\tag{K.48}
$$

Consequently, inside a triangle, multiplication by the cut line's regulated
inverse square gives

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
\left(K_E^{\rm FP}(r_e)(K_E^{\rm FP})^{-1}_{d}(r_e)-1\right)
=\frac{\mu_\ell^2}{D_0D_1D_2},
\tag{K.49}
$$

because every external shift has zero evanescent component.  The exact
four-spin inverse (K.40) and the regulated line (K.44) are therefore two
different objects.  Replacing both by one untyped inverse would erase the
accepted cutting failure.

### 4.4 Oriented FP propagators

Let one anticommuting coefficient pair satisfy
$\eta:=c'\prec\xi:=c$.  The locked measure orientation gives

$$
\int d\xi\,d\eta\,\eta\xi=1.
\tag{K.50}
$$

For $S=\eta K\xi$,

$$
\begin{aligned}
Z&=\int d\xi\,d\eta
\left(1-\frac1\hbar\eta K\xi\right)
=-\frac K\hbar,\\
\int d\xi\,d\eta\,\xi\eta
\left(1-\frac1\hbar\eta K\xi\right)&=-1,\\
\int d\xi\,d\eta\,\eta\xi
\left(1-\frac1\hbar\eta K\xi\right)&=+1.
\end{aligned}
\tag{K.51}
$$

Hence

$$
\boxed{
\langle\xi\eta\rangle=+\hbar K^{-1},
\qquad
\langle\eta\xi\rangle=-\hbar K^{-1}.}
\tag{K.52}
$$

Applying (K.52) to (K.45), the two nonzero ghost-to-antighost lines are

$$
\boxed{
\begin{aligned}
\langle\mathfrak c_+^A(p,1)
\widetilde{\mathfrak c}'_{-,B}(p',2)\rangle_E
={}&(2\pi)^d\delta^{(d)}(p+p')\delta^A{}_B
\left[-\frac{i\hbar}{4p_d^2}\bar D_1^2(p)\right]_{+\leftarrow-},\\
\langle\widetilde{\mathfrak c}_-^A(p,1)
\mathfrak c'_{+,B}(p',2)\rangle_E
={}&(2\pi)^d\delta^{(d)}(p+p')\delta^A{}_B
\left[+\frac{i\hbar}{4p_d^2}D_1^2(p)\right]_{-\leftarrow+}.
\end{aligned}}
\tag{K.53}
$$

All other free ghost contractions vanish.

The subscripts in (K.53) specify the constrained identity kernel on which
the displayed operator acts.  Reversing either ordered contraction changes
its sign by (K.52).  A closed FP loop has one cyclic odd permutation and
therefore carries one overall factor $-1$; no second ad hoc ``ghost-loop
sign'' is permitted.

The commuting coefficient ends in the parity-reversed finite ghost space
use the Euclidean contour of (3D.93c).  They have the same operator inverse
and do not add a Koszul sign.

For comparison only, converting both half-superspace terms in (K.39) once
to full superspace gives

$$
\int_{E,+}\mathfrak c'_+\bar D^2\widetilde{\mathfrak c}_-
=-4\int_{E,8}\mathfrak c'_+\widetilde{\mathfrak c}_-,
\qquad
\int_{E,-}\widetilde{\mathfrak c}'_-D^2\mathfrak c_+
=-4\int_{E,8}\widetilde{\mathfrak c}'_-\mathfrak c_+,
\tag{K.53a}
$$

and hence

$$
S_{E,{\rm FP}}^{(2)}
=-i\int_{E,8}\mathfrak c'_+\widetilde{\mathfrak c}_-
+i\int_{E,8}\widetilde{\mathfrak c}'_-\mathfrak c_+.
\tag{K.53b}
$$

The corresponding exact four-spin full-measure inverse kernel is

$$
(K_{E,8}^{\rm FP})^{-1}_{\bar4}(1,2)
=
\begin{pmatrix}
0&-i\mathcal P_{+,1}^{\bar4}\\
+i\mathcal P_{-,1}^{\bar4}&0
\end{pmatrix}
\delta_E^8(z_1-z_2).
\tag{K.53c}
$$

Equations (K.40) and (K.53c) are the half-measure and full-measure
representatives of the same inverse.  A graph must choose one representation;
attaching the conversion factors (K.18a)--(K.18c) to both would double count
the projector.

## 5. Complete action vertices through order $g^2$

At one-loop order $\hbar g^2$, action vertices of order $g^3$ and higher
cannot enter.  The following list is therefore complete for the Step-5K
ordinary-action side of the census.

### 5.1 Pure-gauge vertices

For $n=3,4$, the chiral gauge word in canonical $u$ variables is

$$
\begin{aligned}
S_{E,+}^{g,(n)}
={}&-\!\sum_{p+q+r+s=n-2}
\frac{(\sqrt2g)^n(-1)^{p+r}f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}\\
&\times\int_{E,+}
\left[\bar D^2(u^pD^au\,u^q)\right]^A
\left[\bar D^2(u^rD_au\,u^s)\right]^B,
\end{aligned}
\tag{K.54}
$$

and the antichiral word is

$$
\begin{aligned}
S_{E,-}^{g,(n)}
={}&-\!\sum_{p+q+r+s=n-2}
\frac{(\sqrt2g)^n(-1)^{q+s}\widetilde f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}\\
&\times\int_{E,-}
\left[D^2(u^p\bar D_{\dot a}u\,u^q)\right]^A
\left[D^2(u^r\bar D^{\dot a}u\,u^s)\right]^B.
\end{aligned}
\tag{K.55}
$$

For each quadruple $(p,q,r,s)$, the matrix order displayed in
(K.54)--(K.55) is part of the rule.  The labeled momentum-space vertex is

$$
\mathfrak v_{E,\pm}^{g,(n)}
=-\frac1\hbar
\frac{\vec\delta}{\delta u^{A_n}(p_n)}\cdots
\frac{\vec\delta}{\delta u^{A_1}(p_1)}
S_{E,\pm}^{g,(n)},
\tag{K.56}
$$

with (K.4), (K.5), and the derivative momentum of its own ordered subword.
Equation (K.56), not a symmetrized color trace quoted from another
convention, emits every cubic and quartic gauge rule needed by the census.

The finite dispatcher is made explicit as follows.  Define the ordered
matrix words, without commuting any two factors,

$$
\begin{aligned}
\mathscr W_{+;pqrs}^{AB}
&:=\int_{E,+}
\left[\bar D^2(u^pD^au\,u^q)\right]^A
\left[\bar D^2(u^rD_au\,u^s)\right]^B,\\
\mathscr W_{-;pqrs}^{AB}
&:=\int_{E,-}
\left[D^2(u^p\bar D_{\dot a}u\,u^q)\right]^A
\left[D^2(u^r\bar D^{\dot a}u\,u^s)\right]^B.
\end{aligned}
\tag{K.56a}
$$

Thus

$$
S_{E,+}^{g,(n)}
=\sum_{p+q+r+s=n-2}
\alpha_{+;n,pqrs}(\sqrt2g)^nf_{AB}
\mathscr W_{+;pqrs}^{AB},
\qquad
S_{E,-}^{g,(n)}
=\sum_{p+q+r+s=n-2}
\alpha_{-;n,pqrs}(\sqrt2g)^n\widetilde f_{AB}
\mathscr W_{-;pqrs}^{AB},
\tag{K.56b}
$$

where the complete cubic/quartic map is

| $n$ | $(p,q,r,s)$ | $\alpha_{+;n,pqrs}$ | $\alpha_{-;n,pqrs}$ |
|---:|---:|---:|---:|
| $3$ | $(0,0,0,1)$ | $-1/512$ | $+1/512$ |
| $3$ | $(0,0,1,0)$ | $+1/512$ | $-1/512$ |
| $3$ | $(0,1,0,0)$ | $-1/512$ | $+1/512$ |
| $3$ | $(1,0,0,0)$ | $+1/512$ | $-1/512$ |
| $4$ | $(0,0,0,2)$ | $-1/1536$ | $-1/1536$ |
| $4$ | $(0,0,1,1)$ | $+1/768$ | $+1/768$ |
| $4$ | $(0,0,2,0)$ | $-1/1536$ | $-1/1536$ |
| $4$ | $(0,1,0,1)$ | $-1/1024$ | $-1/1024$ |
| $4$ | $(0,1,1,0)$ | $+1/1024$ | $+1/1024$ |
| $4$ | $(0,2,0,0)$ | $-1/1536$ | $-1/1536$ |
| $4$ | $(1,0,0,1)$ | $+1/1024$ | $+1/1024$ |
| $4$ | $(1,0,1,0)$ | $-1/1024$ | $-1/1024$ |
| $4$ | $(1,1,0,0)$ | $+1/768$ | $+1/768$ |
| $4$ | $(2,0,0,0)$ | $-1/1536$ | $-1/1536$ |

For example, the overall action minus sign and the two chirality signs give

$$
\begin{aligned}
\alpha_{+;3,0001}
&=-\frac{(-1)^{0+0}}
{256(0!)(0!)(0!)(1!)(0+0+1)(0+1+1)}
=-\frac1{512},\\
\alpha_{-;3,0001}
&=-\frac{(-1)^{0+1}}
{256(0!)(0!)(0!)(1!)(0+0+1)(0+1+1)}
=+\frac1{512},\\
\alpha_{+;4,0011}
&=-\frac{(-1)^{0+1}}
{256(0!)(0!)(1!)(1!)(0+0+1)(1+1+1)}
=+\frac1{768},\\
\alpha_{-;4,0011}
&=-\frac{(-1)^{0+1}}
{256(0!)(0!)(1!)(1!)(0+0+1)(1+1+1)}
=+\frac1{768}.
\end{aligned}
\tag{K.56c}
$$

Each table row therefore fixes all of: the ordered matrix word
$\mathscr W_{\pm;pqrs}^{AB}$, the chiral or antichiral color metric
$f_{AB}$ or $\widetilde f_{AB}$, the full factor $(\sqrt2g)^n$, the
overall action sign, and the labeled ordered Hessian (K.56).

The deterministic complete momentum-space expansion is
`generated/step5k-momentum-rule-ledger.json`, rebuilt by
`scripts/build_step5k_momentum_rule_ledger.py`.  It contains all $28$ raw
chirality/monomial rows and every labeled incoming-leg assignment:

$$
N_{\rm cubic}^{\rm labeled}
=2(4)(3!)=48,
\qquad
N_{\rm quartic}^{\rm labeled}
=2(10)(4!)=480,
\qquad
N_{\rm total}^{\rm labeled}=528.
\tag{K.56d}
$$

For each labeled row it records the ordered color slots, the complete
canonical coefficient after $h=g^{-2}$, the half-measure conversion, the
ordered functional-derivative sequence, the momentum-conservation delta,
and the momentum of every derivative's own ordered subword.  The same
ledger separately stores the exact four-spin and DRED vector, matter, and
FP inverses; it has no unresolved row.

### 5.2 Matter vertices

The canonical matter action is

$$
S_E^{\rm mat}
=-\sum_{r=1}^3\sum_{n=0}^{\infty}
\frac{(\sqrt2g)^n}{n!}
\int_{E,8}\widetilde\Phi_{c,r}^A
u^{A_1}\cdots u^{A_n}
\kappa_{AB}(T_{A_1}\cdots T_{A_n})^B{}_C
\Phi_{c,r}^C.
\tag{K.57}
$$

The one-vector Hessian is

$$
\boxed{
\mathcal C_E[
\widetilde\Phi_{c,r}^A,u^M,\Phi_{c,s}^C]
=-\sqrt2g\,\delta_{rs}\kappa_{AB}(T_M)^B{}_C.}
\tag{K.58}
$$

The two-vector Hessian is

$$
\boxed{
\begin{aligned}
\mathcal C_E[
\widetilde\Phi_{c,r}^A,u^{M_1},u^{M_2},\Phi_{c,s}^C]
=-g^2\delta_{rs}\kappa_{AB}
\Big[&(T_{M_1}T_{M_2})^B{}_C\\
&+(T_{M_2}T_{M_1})^B{}_C\Big].
\end{aligned}}
\tag{K.59}
$$

No closed-matter-loop minus sign occurs because
$\Phi_c,\widetilde\Phi_c$ are even.  The two possible loop orientations
remain distinct ordered color chains until their explicit Wick pairing is
performed.

### 5.3 Superpotential vertices

The two labeled canonical cubics are

$$
\boxed{
\begin{aligned}
\mathcal C_E[
\Phi_{c,r_1}^{A_1},\Phi_{c,r_2}^{A_2},\Phi_{c,r_3}^{A_3}]
&=+\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3},\\
\mathcal C_E[
\widetilde\Phi_{c,r_1}^{A_1},
\widetilde\Phi_{c,r_2}^{A_2},
\widetilde\Phi_{c,r_3}^{A_3}]
&=+\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
\end{aligned}}
\tag{K.60}
$$

They contain no vector, FP, or NK port.

### 5.4 FP vertices

Define

$$
d:=\widetilde{\mathfrak c}_--\mathfrak c_+,
\qquad
s:=\widetilde{\mathfrak c}_-+\mathfrak c_+.
\tag{K.61}
$$

Using $B_0=1$, $B_1=-1/2$, $B_2=1/6$, and $B_3=0$, direct
expansion of (5A.57) gives

$$
\boxed{
\mathbf s_EV
=id-\frac i2[V,s]+\frac i{12}[V,[V,d]]+O(V^4).}
\tag{K.62}
$$

The two order-$V$ contributions are displayed explicitly:

$$
\begin{aligned}
\left.\mathbf s_EV\right|_{p=1,q=0}
&=-\frac i2(V\widetilde{\mathfrak c}+V\mathfrak c),\\
\left.\mathbf s_EV\right|_{p=0,q=1}
&=+\frac i2(\widetilde{\mathfrak c}V+\mathfrak cV),\\
\left.\mathbf s_EV\right|_{V^1}
&=-\frac i2[V,s].
\end{aligned}
\tag{K.63}
$$

The three order-$V^2$ contributions are

$$
\begin{aligned}
\left.\mathbf s_EV\right|_{2,0}
&=\frac i{12}V^2d,\\
\left.\mathbf s_EV\right|_{1,1}
&=-\frac i6VdV,\\
\left.\mathbf s_EV\right|_{0,2}
&=\frac i{12}dV^2,\\
\left.\mathbf s_EV\right|_{V^2}
&=\frac i{12}[V,[V,d]].
\end{aligned}
\tag{K.64}
$$

Substituting (K.62) into (5A.58), and then $V=\sqrt2g\,u$, gives

$$
\boxed{
\begin{aligned}
S_{E,{\rm FP}}^{(1u)}
=-\frac{i\sqrt2g}{8}\Big[&
\int_{E,+}\mathfrak c'_+\bar D^2[u,s]
+\int_{E,-}\widetilde{\mathfrak c}'_-D^2[u,s]
\Big],\\
S_{E,{\rm FP}}^{(2u)}
=+\frac{ig^2}{24}\Big[&
\int_{E,+}\mathfrak c'_+\bar D^2[u,[u,d]]
+\int_{E,-}\widetilde{\mathfrak c}'_-D^2[u,[u,d]]
\Big].
\end{aligned}}
\tag{K.65}
$$

Since

$$
[u,s]^C=ic_{MN}{}^Cu^Ms^N,
\tag{K.66}
$$

the canonical ordered one-vector action Hessians are

$$
\boxed{
\begin{aligned}
\mathcal C_E[\mathfrak c'_{+,C},u^M,\mathfrak c_+^N]
&=\frac{\sqrt2g}{8}c_{MN}{}^C
\bar D^2(p_u+p_{\mathfrak c}),\\
\mathcal C_E[\mathfrak c'_{+,C},u^M,
\widetilde{\mathfrak c}_-^N]
&=\frac{\sqrt2g}{8}c_{MN}{}^C
\bar D^2(p_u+p_{\widetilde{\mathfrak c}}),\\
\mathcal C_E[\widetilde{\mathfrak c}'_{-,C},u^M,\mathfrak c_+^N]
&=\frac{\sqrt2g}{8}c_{MN}{}^C
D^2(p_u+p_{\mathfrak c}),\\
\mathcal C_E[\widetilde{\mathfrak c}'_{-,C},u^M,
\widetilde{\mathfrak c}_-^N]
&=\frac{\sqrt2g}{8}c_{MN}{}^C
D^2(p_u+p_{\widetilde{\mathfrak c}}).
\end{aligned}}
\tag{K.67}
$$

Each line in (K.67) also carries (K.4).  The first field order displayed in
$\mathcal C_E$ is the first derivative in (K.14); reversing the two odd
legs multiplies the result by $-1$.

The double commutator is

$$
[u,[u,d]]^C
=-c_{MD}{}^Cc_{NB}{}^D u^Mu^Nd^B.
\tag{K.68}
$$

Differentiating the two even vector legs gives the exact symmetric color
word

$$
\mathscr C_{M_1M_2;B}{}^C
:=c_{M_1D}{}^Cc_{M_2B}{}^D
+c_{M_2D}{}^Cc_{M_1B}{}^D.
\tag{K.69}
$$

Hence

$$
\boxed{
\begin{aligned}
\mathcal C_E[\mathfrak c'_{+,C},u^{M_1},u^{M_2},
\widetilde{\mathfrak c}_-^B]
&=-\frac{ig^2}{24}\mathscr C_{M_1M_2;B}{}^C
\bar D^2(p_{u_1}+p_{u_2}+p_{\widetilde{\mathfrak c}}),\\
\mathcal C_E[\mathfrak c'_{+,C},u^{M_1},u^{M_2},
\mathfrak c_+^B]
&=+\frac{ig^2}{24}\mathscr C_{M_1M_2;B}{}^C
\bar D^2(p_{u_1}+p_{u_2}+p_{\mathfrak c}),\\
\mathcal C_E[\widetilde{\mathfrak c}'_{-,C},u^{M_1},u^{M_2},
\widetilde{\mathfrak c}_-^B]
&=-\frac{ig^2}{24}\mathscr C_{M_1M_2;B}{}^C
D^2(p_{u_1}+p_{u_2}+p_{\widetilde{\mathfrak c}}),\\
\mathcal C_E[\widetilde{\mathfrak c}'_{-,C},u^{M_1},u^{M_2},
\mathfrak c_+^B]
&=+\frac{ig^2}{24}\mathscr C_{M_1M_2;B}{}^C
D^2(p_{u_1}+p_{u_2}+p_{\mathfrak c}).
\end{aligned}}
\tag{K.70}
$$

There is no three-vector FP vertex because $B_3=0$.  The next FP vertex
contains four vectors and is order $g^4$, so it is absent from an
$\hbar g^2$ census.

### 5.5 Gauge-fixing, multiplier, and Nielsen--Kallosh sectors

In the accepted physical representative,

$$
\mathcal F_+=-\frac14\bar D^2V,
\qquad
\mathcal F_-=-\frac14D^2V,
\qquad
\mathcal Y_{E,{\rm FF}}^{-1}
=\frac h2
\begin{pmatrix}0&-\bar D^2/4\\-D^2/4&0\end{pmatrix}
\tag{K.71}
$$

are field independent at trivial background.  Therefore

$$
\frac12\langle\mathcal Y_{E,{\rm FF}}^{-1}\mathcal F,
\mathcal F\rangle_E
=\frac h4\int_{E,8}V\cdot\bar\Box_E
\left(\mathcal P_+^{\bar4}+\mathcal P_-^{\bar4}\right)V
\tag{K.72}
$$

is exactly quadratic.  It produces no $V^3$, $V^4$, ghost, or matter
interaction vertex.  After the multiplier square is completed, the shifted
multiplier is a decoupled Gaussian and is not an edge of the reduced physical
graph representative.

The Step-5 decision D2 keeps the Nielsen--Kallosh factor as an external
field-independent measure constant.  Hence

$$
\frac{\delta^n}{\delta X_1\cdots\delta X_n}
\log\mathfrak F_E^{\rm NK}=0,
\qquad n\ge1,
\tag{K.73}
$$

for every physical, ghost, and source field $X_j$.  There is no NK
propagator and no NK interaction vertex in this representative.  A proposed
graph containing an NK edge is therefore not a graph of the fixed D1/D2
field content; a proposed graph containing a gauge-fixing interaction vertex
has zero vertex Hessian by (K.72).

## 6. Composite-letter insertion vertices and resolvent signs

### 6.1 Canonical ordered $WW$ insertion

For the canonical linear letter, define the locked operator

$$
K_+^c:=-\frac1{4\sqrt2}D_+\bar D^2D_+,
\qquad
A_1^A:=K_+^cu^A.
\tag{K.73a}
$$

Using $D^2=2D_-D_+$, the marked descendant operator is

$$
\begin{aligned}
D_-K_+^c
&=-\frac1{4\sqrt2}D_-D_+\bar D^2D_+\\
&=-\frac1{4\sqrt2}\left(\frac12D^2\right)\bar D^2D_+\\
&=-\frac1{8\sqrt2}D^2\bar D^2D_+.
\end{aligned}
\tag{K.73b}
$$

Let

$$
\mathsf T_w:=e^{w_{\dot a}\partial^{\dot a}}.
\tag{K.73c}
$$

On an incoming momentum-$q$ right endpoint,

$$
\mathsf T_wX(q)=e^{iw_{\dot a}q^{\dot a}}X(q).
\tag{K.73d}
$$

The quadratic ordered source insertion is

$$
\begin{aligned}
\mathcal I_{0,w}^{AB}
&:=D_-\!\left[(K_+^cu^A)\,
\mathsf T_w(K_+^cu^B)\right]\\
&=\underbrace{(D_-K_+^cu^A)\,
\mathsf T_w(K_+^cu^B)}_{\mathfrak m_L}\\
&\quad+
\underbrace{(K_+^cu^A)\,
\mathsf T_w(D_-K_+^cu^B)}_{\mathfrak m_R}.
\end{aligned}
\tag{K.73e}
$$

There is a plus sign in the second line because $K_+^cu$ is even, and
$[D_-,\partial^{\dot a}]=0$.  The two terms $\mathfrak m_L$ and
$\mathfrak m_R$ are distinct occurrence marks; neither is a multiplicity
two and there is no source factor $1/2$.

With incoming source momentum $k$ and occurrence-labeled ports
$u_L^C(p)$ and $u_R^D(q)$, ordered differentiation gives

$$
\boxed{
\begin{aligned}
\mathcal C_{J,E;0,w}^{\mathfrak m_L}
[u_L^C(p),u_R^D(q)]
={}&(2\pi)^d\delta^{(d)}(k+p+q)\,
\delta^A{}_C\delta^B{}_D\\
&\times e^{iw\cdot q}
(D_-K_+^c)(p)K_+^c(q),\\
\mathcal C_{J,E;0,w}^{\mathfrak m_R}
[u_L^C(p),u_R^D(q)]
={}&(2\pi)^d\delta^{(d)}(k+p+q)\,
\delta^A{}_C\delta^B{}_D\\
&\times e^{iw\cdot q}
K_+^c(p)(D_-K_+^c)(q).
\end{aligned}}
\tag{K.73f}
$$

Exchange of $L$ and $R$ is a separate Wick routing.  It is not inserted
again inside either marked Hessian in (K.73f).  Before differentiation with
respect to the source, the source vertex carries
$+\mathcal C_{J,E}/\hbar$ by (K.16).

### 6.2 Nonlinear all-letter generating rule

For the full link, Step 5 fixes

$$
S_J=\int d^4x\,J_{AB}\,
L^A(x)\left(e^{w_{\dot a}\mathcal D_{\rm adj}^{\dot a}}L\right)^B(x),
\qquad
L:=g^{-1}\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+.
\tag{K.73g}
$$

Writing the locked link exponent as $X+gY$, its ordered expansion is

$$
\begin{aligned}
e^{X+gY}
={}&e^X
+g\int_0^1ds\,e^{(1-s)X}Ye^{sX}\\
&+g^2\int_0^1ds_1\int_0^{s_1}ds_2\,
e^{(1-s_1)X}Ye^{(s_1-s_2)X}Ye^{s_2X}
+O(g^3),
\end{aligned}
\tag{K.73h}
$$

where $X=w_{\dot a}\partial^{\dot a}$ and
$Y=w_{\dot a}\operatorname{ad}_{v}^{\dot a}$ are the locked Step-5
operators.  Matrix order and the simplex order $0\le s_2\le s_1\le1$
must not be symmetrized.

For any admitted ordered bi-letter insertion
$\mathcal I_{\alpha\beta,w}^{AB}$ and any occurrence mark $\mathfrak m$,
the exact momentum-space source rule is the ordered derivative

$$
\boxed{
\mathcal C_{J,E;\alpha\beta,\mathfrak m}
[X_1(p_1),\ldots,X_n(p_n)]
:=
\left.
\frac{\vec\delta}{\delta X_n(p_n)}\cdots
\frac{\vec\delta}{\delta X_1(p_1)}
\mathcal I_{\alpha\beta,w;\mathfrak m}^{AB}
\right|_{\Psi_{\rm q}=0}.}
\tag{K.73i}
$$

Each derivative in (K.73i) uses (K.13), every translated right-endpoint
field uses the phase (K.73d), and every local source vertex carries (K.4)
with the incoming source momentum included.  A field-word mismatch makes
the Hessian exactly zero.  Only the differentiated quantum fields
$\Psi_{\rm q}$ are set to zero; undifferentiated background or spectator
legs remain as external operators.

The nonlinear letter words and their typed occurrence placements are not
reconstructed from an unstated convention here.  The census invokes their
accepted definitions in
`step5-aa-external-slot-decomposition-exact.md`,
`step5-spectator-source-self-energy-orbit-exact.md`,
`step5-ac-ca-family-exact.md`,
`step5-ad-da-ordered-ports-crossed-hessian-exact.md`, and
`step5-bc-full-family-raw-projection-exact.md`, then applies (K.73i).

### 6.3 Resolvent insertion classes

Let

$$
\mathcal I(g)=\mathcal I_0+g\mathcal I_1+g^2\mathcal I_2+O(g^3),
\qquad
S_{\rm int}(g)=gS_3+g^2S_4+O(g^3).
\tag{K.73j}
$$

The Euclidean interaction exponential expands without a suppressed term:

$$
\begin{aligned}
e^{-S_{\rm int}(g)/\hbar}
={}&1-\frac g\hbar S_3\\
&+g^2\left(
-\frac1\hbar S_4
+\frac1{2\hbar^2}S_3S_3
\right)
+O(g^3).
\end{aligned}
\tag{K.73k}
$$

Multiplication of (K.73j) and (K.73k) gives the connected order-$g^2$
coefficient

$$
\boxed{
\begin{aligned}
\left[\langle\mathcal I(g)\rangle_c\right]_{g^2}
={}&+\langle\mathcal I_2\rangle_{0,c}
-\frac1\hbar\langle\mathcal I_1S_3\rangle_{0,c}\\
&-\frac1\hbar\langle\mathcal I_0S_4\rangle_{0,c}
+\frac1{2\hbar^2}
\langle\mathcal I_0S_3S_3\rangle_{0,c}.
\end{aligned}}
\tag{K.73l}
$$

Thus the four graph-factor signs and coefficients are, respectively,
$+1$, $-1/\hbar$, $-1/\hbar$, and $+1/(2\hbar^2)$.  The $1/2$ in the last
class is canceled only when two labeled $S_3$ assignments are explicitly
summed; it is never removed before the Wick-routing stabilizer is known.

## 7. Incidence rules for the Step-5K census

The fixed-slice rule dispatcher is

| typed field word | nonzero rule | graph factor |
|---|---|---|
| $u\,u$ | vector line (K.24) | already includes $+\hbar(K_E^u)^{-1}_d$ |
| $\Phi_{c,r}\,\widetilde\Phi_{c,s}$ | oriented matter line (K.28), $\delta_{rs}$ | already includes $+\hbar(K_E^{\Phi\widetilde\Phi})^{-1}_d$ |
| $\mathfrak c_+\,\widetilde{\mathfrak c}'_-$ or $\widetilde{\mathfrak c}_-\,\mathfrak c'_+$ | oriented FP lines (K.53) | endpoint order from (K.52), one closed-loop Koszul sign |
| $u^3$ or $u^4$ | ordered gauge Hessian (K.54)--(K.56) | $-\mathcal C_E/\hbar$ |
| $\widetilde\Phi_c\,u\,\Phi_c$ | matter Hessian (K.58) | $-\mathcal C_E/\hbar$ |
| $\widetilde\Phi_c\,u\,u\,\Phi_c$ | matter Hessian (K.59) | $-\mathcal C_E/\hbar$ |
| $\Phi_c^3$ or $\widetilde\Phi_c^3$ | superpotential Hessian (K.60) | $-\mathcal C_E/\hbar$ |
| $\mathfrak c'\,u\,\mathfrak c$ | FP Hessians (K.67) | $-\mathcal C_E/\hbar$ |
| $\mathfrak c'\,u\,u\,\mathfrak c$ | FP Hessians (K.70) | $-\mathcal C_E/\hbar$ |
| marked quadratic $WW$ source | (K.73f) | $+\mathcal C_{J,E}/\hbar$ before the source derivative |
| nonlinear admitted bi-letter source | (K.73i) with the accepted typed source audit | $+\mathcal C_{J,E}/\hbar$ before the source derivative |
| gauge-fixing interaction or NK port | no rule, (K.72)--(K.73) | exact zero or absent field |

The locked action implies the following exact incidence statements.

1. A vector propagator joins $u$ only to $u$.
2. A matter propagator joins $\Phi_{c,r}$ to
   $\widetilde\Phi_{c,r}$ with fixed orientation; flavor is diagonal.
3. An FP propagator joins $\mathfrak c_+$ only to
   $\widetilde{\mathfrak c}'_-$, or
   $\widetilde{\mathfrak c}_-$ only to $\mathfrak c'_+$, with the
   orientations in (K.53).
4. Every FP interaction contains exactly one antighost, exactly one ghost,
   and one or two vectors through order $g^2$.
5. There is no FP--matter vertex.
6. There is no source--FP vertex in the locked bilocal physical source; an
   FP loop can attach to a source graph only through vector ports and the FP
   vertices (K.67) or (K.70).
7. There is no NK edge or NK vertex in the fixed representative.
8. There is no gauge-fixing interaction vertex at trivial background.

Thus a candidate word violating any of statements 1--8 is `EXACT_ZERO` or
`NOT_A_GRAPH_OF_THE_FIXED_REPRESENTATIVE` before loop integration.  A
candidate that satisfies them must still retain the closed-FP-loop sign and
the DRED defect (K.48); it cannot be declared zero merely by replacing the
regulated line by the exact four-spin inverse.

## 8. Settled rules and genuine remaining boundaries

| item | result |
|---|---|
| vector quadratic kernel and inverse | `DERIVED_EXACT_ON_FOUR_SPIN_COMPLEMENT_WITH_EXPLICIT_MU2_DEFECT`, (K.21)--(K.24a) |
| matter algebraic inverse | `DERIVED_EXACT_ON_FOUR_SPIN_COMPLEMENT`, (K.26)--(K.27) |
| matter DRED line | `DERIVED_WITH_EXPLICIT_MU2_DEFECT`, (K.28)--(K.29) |
| FP gauge-tangent map | `DERIVED_EXACT`, (K.30)--(K.36) |
| FP action Hessian | `DERIVED_EXACT`, (K.37)--(K.39) |
| FP left and right four-spin inverse | `DERIVED_EXACT_ON_RESIDUAL_COMPLEMENT`, (K.40)--(K.43) |
| FP DRED line | `DERIVED_WITH_EXPLICIT_MU2_DEFECT`, (K.44)--(K.49) |
| FP oriented propagators | `DERIVED_EXACT`, (K.50)--(K.53) |
| gauge, matter, superpotential, FP vertices through $g^2$ | `DERIVED_EXACT`, (K.54)--(K.70) |
| gauge-fixing interactions | `EXACT_ZERO_AT_TRIVIAL_BACKGROUND`, (K.71)--(K.72) |
| NK propagator and vertices | `ABSENT_FIELD_INDEPENDENT_EXTERNAL_MEASURE`, (K.73) |
| canonical ordered $WW$ source marks | `DERIVED_EXACT`, (K.73a)--(K.73f) |
| nonlinear all-letter source rule | `ORDERED_GENERATING_DIFFERENTIATION_RULE_WITH_ACCEPTED_TYPED_REFERENCES`, (K.73g)--(K.73i) |
| resolvent graph-factor signs | `DERIVED_EXACT`, (K.73j)--(K.73l) |

Two boundaries remain and must not be hidden.

First, there is no inverse of the FP block on
$\ker\mathcal M_E^{(0)}$.  The locked path integral removes this residual
sector and integrates only $\mathscr G^{\perp}$; this is a declared domain,
not a missing propagator.

Second, no single operator is simultaneously the exact four-spin inverse
and the DRED-regulated propagator.  The exact relation is (K.48).  Any census
implementation that requires

$$
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_d=1
\tag{K.74}
$$

is inconsistent with the locked DRED ledger.  The admissible replacement is

$$
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_d
=1+\frac{\mu_r^2}{r_d^2},
\tag{K.75}
$$

with the second term carried occurrence by occurrence into the graph IR.
