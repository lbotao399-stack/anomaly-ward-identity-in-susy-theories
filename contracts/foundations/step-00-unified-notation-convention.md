# 00 3+1d SUSY QFT — Convention Lock

## Step 0. Unified notation convention

**Contract id:** FOUNDATION-UNIFIED-NOTATION-CONVENTION-000

**Title:** Step 0. Unified notation convention for spacetime, spinors, derivatives, superfields, gauge frames, and BV–BRST

**Status:** DERIVED_UNFROZEN (proposal)

**Date:** 2026-07-17

**Scope.** This contract collects, in one place, every notation and
sign convention that the foundation contracts Step 1 through Step 5A
share, that the Weinberg–Srednicki–Project dictionaries translate, and
that the four channels (Euclidean/Lorentzian \(\times\)
component/superfield) and the paper inherit. Each entry is restated as
a single locked display equation or table row with a contiguous tag
tagged (0A.n), followed by its primary source tag in the foundation
contracts or dictionaries. Nothing in this file overrides the source
contracts; where a restatement narrows or supersedes an earlier naming,
the deviation ledger in Section 11 records the call.

**Authority.** Locks shared notation for contracts/foundations
step-01…step-05a, dictionaries, channels ec/es/lc/ls, and
paper/awi-n4-one-loop.md; file-local symbols remain governed by
per-file ledgers.

### 0.1 Reading rules

Every branch decision is marked by \(\boxed{}\) and by the status
vocabulary of the repository: **LOCK** (adopted project-wide),
**CONDITIONAL** (adopted branch whose residual sign or source gap is
explicitly retained), **OUT_OF_SCOPE** (registered here, decided
elsewhere or not at all). Equation tags are contiguous from
(0A.1); lettered subtags such as (0A.12a) are used
sparingly. The three approximation macros banned by the repository
policy test are banned here as well; to keep this document itself
compliant they are referred to only descriptively (the backslash-sim,
backslash-approx, and backslash-propto macros). Citations in
parentheses, e.g. (2A.28), (3B.114e), (3D.56), (5A.40), (D.3.18),
refer to the tagged equations of the foundation contracts and
dictionaries listed in the manifest. The letter \(R\in\{L,E\}\) is the
Lorentzian/Euclidean sector label everywhere.

## 1. Spacetime, signature, and the Wick map

### 1.1 Indices and parity

$$
\begin{gathered}
\mu,\nu,\rho,\sigma=0,1,2,3,\qquad
i,j,k=1,2,3,\qquad
m,n,r,s=1,2,3,4,\\
a,b,c=1,2,\qquad
\dot a,\dot b,\dot c=\dot1,\dot2,\\
|J|=|P|=0,\qquad |Q|=|\bar Q|=1,\qquad
[A,B\}:=AB-(-1)^{|A||B|}BA .
\end{gathered}
\tag{0A.1}
$$

Source: (1.1), (4.2).

### 1.2 Signature lock

$$
\boxed{
\eta_L=\operatorname{diag}(-1,+1,+1,+1),\qquad
v_\mu=\eta_{\mu\nu}v^\nu,\qquad
\delta_E=\operatorname{diag}(+1,+1,+1,+1)_{mn}.}
\tag{0A.2}
$$

LOCK: the project uses the mostly-plus Lorentzian metric. The
\((+,-,-,-)\) anchor is explicitly **not** used anywhere in the
foundations, dictionaries, channels, or paper. Every sign corollary
(\(\{Q,\bar Q\}=-2\sigma P\), \(D_a=\partial_a-i(\sigma\bar\vartheta)\partial\),
\(y_L=x_L-iB_L\)) propagates from (0A.2). Sources: (1.2), (2B.34b),
(4.1), (D.2.1).

### 1.3 Spacetime Levi-Civita

$$
\epsilon_L^{0123}=+1,\qquad
\epsilon_{L,0123}=-1,\qquad
\epsilon_E^{1234}=+1,\qquad
\epsilon_{E,1234}=+1.
\tag{0A.3}
$$

Sources: (1.2), (3A.62), (3A.90), (D.2.2). The sources state only
\(\epsilon_E^{1234}=+1\) and the Lorentzian \(\epsilon_{0123}=-1\);
the lowered Euclidean value \(+1\) follows from
\(\delta_E\)-lowering per (0A.2).

### 1.4 The complete Wick map

Coordinates and shifts:

$$
\boxed{
x_E^i=x_L^i,\qquad
x_E^4=ix_L^0
\ \Longleftrightarrow\
x_L^0=-ix_E^4.}
\tag{0A.4}
$$

Sources: (1.40), (2B.61), (3A.89), (3D.12a), (4.4).

Derivatives:

$$
\partial_i^L=\partial_i^E,\qquad
\partial_0^L=i\partial_4^E.
\tag{0A.5}
$$

Sources: (2A.38), (3A.89), (4.4).

Gauge fields and curvature:

$$
A_0^L=iA_4^E,\qquad
A_i^L=A_i^E,\qquad
F_{0i}^L=iF_{4i}^E,\qquad
F_{ij}^L=F_{ij}^E.
\tag{0A.6}
$$

Sources: (3A.89), (3B.99).

Sigma–derivative map, equivalently the component dictionary
\(\sigma_L^0=\sigma_E^4\), \(\sigma_L^j=i\sigma_E^j\):

$$
\sigma_L^\mu\partial_\mu^L
=i\,\sigma_E^m\partial_m^E,
\qquad
\sigma_L^\mu\mathcal D_\mu^L
=i\,\sigma_E^m\mathcal D_m^E.
\tag{0A.7}
$$

Sources: (2A.38), (3C.75), (4.4), (4A.11).

Grassmann coordinates are held fixed; supercharges carry \(-i\):

$$
\vartheta_E=\vartheta_L,\qquad
\bar\vartheta_E=\bar\vartheta_L,\qquad
Q_a^E=-iQ_a^L,\qquad
\bar Q_E^{\dot a}=-i\bar Q_L^{\dot a}.
\tag{0A.8}
$$

Sources: (1.47), (1.49), (2B.61), (4.34), (D.6.4).

Spinor-curvature map:

$$
\left.\sigma_L^{\mu\nu}F_{\mu\nu}^L\right|_{\rm Wick}
=-\sigma_E^{mn}F_{mn}^E .
\tag{0A.9}
$$

Sources: (3B.99), (4C.48), (4A.11).

Measures, Lagrangians, actions, and Boltzmann weights:

$$
\boxed{
d^4x_L=-i\,d^4x_E,\qquad
\mathcal L_E=-\mathcal L_L\big|_{\rm Wick},\qquad
S_{0,E}=-iS_{0,L}\big|_{\rm Wick},\qquad
e^{iS_L}=e^{-S_E}.}
\tag{0A.10}
$$

Sources: (3A.92), (3B.99), (3D.116).

Topological density:

$$
\left.\epsilon_L^{\mu\nu\rho\sigma}F_{\mu\nu}^LF_{\rho\sigma}^L
\right|_{\rm Wick}
=-i\,\epsilon_E^{mnrs}F_{mn}^EF_{rs}^E .
\tag{0A.11}
$$

Sources: (3A.90), (3B.99).

Path-integral exponent and source signs:

$$
\boxed{
\tau_L:=\frac{i}{\hbar},\qquad
\tau_E:=-\frac1{\hbar},\qquad
\upsilon_L:=+1,\qquad
\upsilon_E:=-1.}
\tag{0A.12}
$$

The Lorentzian exponent is \((i/\hbar)(S_{0,L}+\mathcal J_L)\); the
Euclidean exponent is \(-S_{0,E}/\hbar+\mathcal J_E/\hbar\). Sources:
(3D.6), (3D.9), (5A.2). LOCK: \(\tau_R\) is reserved for these
path-integral weights; see Section 12.

Currents transport with the same phase split as the coordinate map:

$$
C_E^i=-C_L^i\big|_{\rm Wick},\qquad
C_E^4=-iC_L^0\big|_{\rm Wick}.
\tag{0A.12a}
$$

Source: (4A.56); the same rule holds for \(K^\mu\) and \(j^\mu\)
((4B.52d), (4C.69)).

## 2. Weyl spinors

### 2.1 Spinor metric and index moves

$$
\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,\qquad
\epsilon_{12}=\epsilon_{\dot1\dot2}=-1,
\tag{0A.13}
$$

$$
(\epsilon^{ab})=(\epsilon^{\dot a\dot b})
=
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
(\epsilon_{ab})=(\epsilon_{\dot a\dot b})
=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{0A.14}
$$

Sources: (1.3), (1.4), (4.3), (D.2.3).

$$
\begin{gathered}
\psi^a=\epsilon^{ab}\psi_b,\qquad
\psi_a=\epsilon_{ab}\psi^b,\qquad
\bar\psi^{\dot a}=\epsilon^{\dot a\dot b}\bar\psi_{\dot b},\qquad
\bar\psi_{\dot a}=\epsilon_{\dot a\dot b}\bar\psi^{\dot b},\\
\epsilon^{ab}\epsilon_{bc}=\delta^a{}_c,\qquad
\epsilon_{ab}\epsilon^{bc}=\delta_a{}^c .
\end{gathered}
\tag{0A.15}
$$

Source: (1.5).

### 2.2 Contraction directions

$$
\xi\chi:=\xi^a\chi_a
\ \text{(undotted, NW--SE)},\qquad
\bar\xi\bar\chi:=\bar\xi_{\dot a}\bar\chi^{\dot a}
\ \text{(dotted, SW--NE)},
\tag{0A.16}
$$

and for Grassmann-odd spinors the contractions are symmetric:

$$
\xi\chi=\chi\xi,\qquad
\bar\xi\bar\chi=\bar\chi\bar\xi .
\tag{0A.17}
$$

Sources: (1.6), (1.8).

### 2.3 Sigma matrices

$$
\boxed{
(\sigma_L^\mu)_{a\dot b}=(\mathbf1,\vec\sigma)_{a\dot b},\qquad
(\bar\sigma_L^\mu)^{\dot a a}
:=\epsilon^{ab}\epsilon^{\dot a\dot b}(\sigma_L^\mu)_{b\dot b}
=(\mathbf1,-\vec\sigma)^{\dot a a}.}
\tag{0A.18}
$$

$$
\boxed{
(\sigma_E^m)_{a\dot b}=(-i\vec\sigma,\mathbf1_2),\qquad
(\bar\sigma_E^m)^{\dot a a}=(+i\vec\sigma,\mathbf1_2).}
\tag{0A.19}
$$

LOCK: the Euclidean basis \((-i\vec\sigma,\mathbf1_2)\), not the
alternative \((\vec\sigma,\pm i)\), is used; it is fixed by (0A.7).
Sources: (1.10), (1.11), (1.51), (1.52), (D.2.4)–(D.2.5), (D.5.1).

$$
\sigma_L^\mu\bar\sigma_L^\nu+\sigma_L^\nu\bar\sigma_L^\mu
=-2\eta^{\mu\nu}\mathbf1_2,
\qquad
\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m
=+2\delta^{mn}\mathbf1_2 .
\tag{0A.20}
$$

Sources: (1.12)–(1.13), (1.54), (D.2.6).

### 2.4 Lorentz spinor generators, 1/4 normalization

$$
\boxed{
(\sigma_L^{\mu\nu})_a{}^b
:=\frac14\left(\sigma_L^\mu\bar\sigma_L^\nu
-\sigma_L^\nu\bar\sigma_L^\mu\right)_a{}^b,\qquad
(\bar\sigma_L^{\mu\nu})^{\dot a}{}_{\dot b}
:=\frac14\left(\bar\sigma_L^\mu\sigma_L^\nu
-\bar\sigma_L^\nu\sigma_L^\mu\right)^{\dot a}{}_{\dot b},}
\tag{0A.21}
$$

with the same 1/4 factor for \(\sigma_E^{mn}\) and
\(\bar\sigma_E^{mn}\). Explicitly,

$$
\sigma_L^{0i}=-\frac{\sigma^i}2,\qquad
\bar\sigma_L^{0i}=+\frac{\sigma^i}2,\qquad
\sigma_L^{ij}=\bar\sigma_L^{ij}
=-\frac{i}2\epsilon^{ijk}\sigma^k .
\tag{0A.22}
$$

Sources: (1.14)–(1.16), (1.55)–(1.57), (D.2.7).

### 2.5 Grassmann squares: the asymmetric sign lock

$$
\boxed{
\vartheta^2:=\vartheta^a\vartheta_a=-2\vartheta^1\vartheta^2,\qquad
\bar\vartheta^2:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}
=+2\bar\vartheta_{\dot1}\bar\vartheta_{\dot2}.}
\tag{0A.23}
$$

LOCK: the undotted square carries \(-2\), the dotted square carries
\(+2\); this asymmetry is deliberate and propagates into (0A.24) and
into the Srednicki dotted-derivative dictionary entry of Section 11.
Sources: (3A.9), (2C.3).

$$
\vartheta^a\vartheta^b=-\frac12\epsilon^{ab}\vartheta^2,\qquad
\bar\vartheta_{\dot a}\bar\vartheta_{\dot b}
=-\frac12\epsilon_{\dot a\dot b}\bar\vartheta^2,\qquad
(\vartheta\psi)(\vartheta\chi)=-\frac12\vartheta^2\,\psi\chi .
\tag{0A.24}
$$

Sources: (3A.25), (3B.44).

### 2.6 The superspace bilinear \(B_R^M\)

$$
B_R^M:=\vartheta\sigma_R^M\bar\vartheta,\qquad
B_L^\mu B_L^\nu=-\frac12\eta^{\mu\nu}\vartheta^2\bar\vartheta^2,\qquad
B_E^m B_E^n=+\frac12\delta^{mn}\vartheta^2\bar\vartheta^2 .
\tag{0A.25}
$$

Sources: (2A.7), (3A.26), (3B.44), (3B.88).

### 2.7 Spinor trace identities

$$
\begin{gathered}
\operatorname{tr}_2(\sigma_L^{\mu\nu}\sigma_L^{\rho\sigma})
=-\frac12(\eta^{\mu\rho}\eta^{\nu\sigma}
-\eta^{\mu\sigma}\eta^{\nu\rho})
+\frac{i}{2}\epsilon_L^{\mu\nu\rho\sigma},\\
\operatorname{tr}_2(\bar\sigma_L^{\mu\nu}\bar\sigma_L^{\rho\sigma})
=-\frac12(\eta^{\mu\rho}\eta^{\nu\sigma}
-\eta^{\mu\sigma}\eta^{\nu\rho})
-\frac{i}{2}\epsilon_L^{\mu\nu\rho\sigma},\\
\operatorname{tr}_2(\sigma_E^{mn}\sigma_E^{rs})
=-\frac12(\delta^{mr}\delta^{ns}-\delta^{ms}\delta^{nr})
+\frac12\epsilon_E^{mnrs},\\
\operatorname{tr}_2(\bar\sigma_E^{mn}\bar\sigma_E^{rs})
=-\frac12(\delta^{mr}\delta^{ns}-\delta^{ms}\delta^{nr})
-\frac12\epsilon_E^{mnrs}.
\end{gathered}
\tag{0A.26}
$$

Sources: (3A.62), (3A.64), (3C.72l).

### 2.8 Lorentzian reality and the Euclidean independence lock

The formal Lorentzian adjoint \(\ddagger_L\) obeys

$$
\begin{gathered}
(\vartheta^a)^{\ddagger_L}=\bar\vartheta^{\dot a},\qquad
(\partial_a)^{\ddagger_L}=-\bar\partial_{\dot a},\qquad
(AB)^{\ddagger_L}=B^{\ddagger_L}A^{\ddagger_L},\\
(D_a^L)^{\ddagger_L}=-\bar D^L_{\dot a},\qquad
(\mathsf Q_a^L)^{\ddagger_L}=\bar{\mathsf Q}^L_{\dot a},\qquad
(y_L)^{\ddagger_L}=\widetilde y_L .
\end{gathered}
\tag{0A.27}
$$

Sources: (2A.35), (2A.36), (2B.60a).

$$
\boxed{
\text{The two Euclidean Weyl sectors are independent;
no intrinsic Euclidean }\dagger\text{ is imposed.}}
\tag{0A.28}
$$

LOCK: the only adjoint relating the Euclidean sectors is the
Wick-transported adjoint \(\dagger_W\), which is not an intrinsic
Euclidean operation:

$$
(Q_a^E)^{\dagger_W}=-\bar Q^E_{\dot a},\qquad
(\mathcal Q_a^E)^{\dagger_W}=+\bar{\mathcal Q}^E_{\dot a}.
\tag{0A.29}
$$

Sources: (2A.52), (2B.77), (2C §2C.6), (D.5.4). The three named
adjoints — Hilbert-space \(\dagger_{\mathcal H}\), formal coordinate
\(\ddagger_L\), Wick-transported \(\dagger_W\) — are never
identified with one another. Sources: (2A.34)–(2A.37), (D.6.3).

## 3. Majorana and four-component layer

### 3.1 Two-component primacy

$$
\boxed{
\gamma_C^\mu,\ \gamma_{5C},\ \beta_C,\ \mathcal C_C,\ \Psi_C,\ V_C,\
W_{C\alpha},\ [\cdot]_{F,C},\ [\cdot]_{D,C}\ :=\ {\rm UNFIXED}.}
\tag{0A.30}
$$

LOCK: the project column of the dictionary is two-component-primary;
every four-component object exists only inside the Srednicki (S) or
Weinberg (W) columns of the dictionary, never as a project primitive.
Source: (D.1.1).

### 3.2 Stacked Majorana spinor lock

$$
\boxed{
\Psi_{M,S}:=\begin{pmatrix}\psi_a\\ \bar\psi^{\dot a}\end{pmatrix},
\qquad
\bar\Psi_{M,S}=\Psi_{M,S}^T\mathcal C .}
\tag{0A.31}
$$

LOCK: the Majorana layer is the stacked Majorana spinor —
undotted Weyl on top, dotted-raised below. On the Lorentzian contour
\(\bar\psi^{\dot a}=(\psi^a)^\dagger\), recovering the dictionary form
\(\Psi_{M,S}=(\psi_a,\psi^{\dagger\dot a})^T\) of (D.3.15). Source:
(D.3.15).

### 3.3 Dirac matrices in the S-form

$$
\gamma_S^\mu=
\begin{pmatrix}0&\sigma^\mu\\ \bar\sigma^\mu&0\end{pmatrix},
\qquad
\{\gamma_S^\mu,\gamma_S^\nu\}=-2\eta^{\mu\nu}\mathbf1_4,
\tag{0A.32}
$$

$$
\gamma_{5S}:=+i\gamma_S^0\gamma_S^1\gamma_S^2\gamma_S^3,\qquad
P_{L/R}^S=\frac{1\mp\gamma_{5S}}2 .
\tag{0A.33}
$$

Sources: (D.3.1), (D.3.2), (D.3.4), (D.3.6).

### 3.4 Charge conjugation

$$
\boxed{
\mathcal C=-i\begin{pmatrix}\sigma^2&0\\0&-\sigma^2\end{pmatrix}
=\begin{pmatrix}\epsilon_{ab}&0\\0&\epsilon^{\dot a\dot b}\end{pmatrix}.}
\tag{0A.34}
$$

$$
\mathcal C^T=\mathcal C^\dagger=\mathcal C^{-1}=-\mathcal C,\qquad
\mathcal C^2=-\mathbf1_4,\qquad
\mathcal C^{-1}\gamma_S^\mu\mathcal C=-(\gamma_S^\mu)^T .
\tag{0A.35}
$$

Sources: (D.3.12), (D.3.13).

### 3.5 Majorana reality in the S-form

$$
\boxed{
\Psi_{M,S}^{c}:=\mathcal C\bar\Psi_{M,S}^{T}=\Psi_{M,S},
\qquad
\Psi_{M,S}^*=-\beta\mathcal C\Psi_{M,S}.}
\tag{0A.36}
$$

Source: (D.3.15); here \(\beta:=\beta_S\) of (D.3.7) (numerically
\(\gamma_S^0\)), not the UNFIXED project-column \(\beta_C\) of (0A.30).

### 3.6 The Weinberg bridge: adopted branches

$$
\boxed{
\gamma_W^\mu=-i\gamma_S^\mu,\qquad
\{\gamma_W^\mu,\gamma_W^\nu\}=+2\eta^{\mu\nu}\mathbf1_4,\qquad
\gamma_{5W}=-\gamma_{5S}.}
\tag{0A.37}
$$

$$
\boxed{
\Psi_{M,W}=+i\Psi_{M,S},\qquad
\bar\Psi_{M,W}=-i\bar\Psi_{M,S}.}
\tag{0A.38}
$$

$$
\boxed{
\Theta_W=-i\Theta_S^{(4)},\qquad
\bar\Theta_W=+i\bar\Theta_S^{(4)},\qquad
\psi_W=i\begin{pmatrix}\psi_P\\ \bar\psi_P\end{pmatrix},\qquad
\phi_P=A_S=\phi_W,\qquad
F_P=F_S=\mathcal F_W .}
\tag{0A.39}
$$

LOCK: each boxed pair is an adopted dictionary branch; the underlying
reality conditions fix only \(e^{2i\phi}=-1\). Sources: (D.3.2),
(D.3.5), (D.3.18), (D.7.7), (3B.114a), (D.8.3).

### 3.7 Bilinear flips and Fierz identities

For Majorana fields \(\chi,\psi\),

$$
\bar\chi M\psi=
\begin{cases}
+\bar\psi M\chi,
&M\in\{\mathbf1,\gamma_5,\gamma_5\gamma^\mu\},\\
-\bar\psi M\chi,
&M\in\{\gamma^\mu,[\gamma^\mu,\gamma^\nu]\}.
\end{cases}
\tag{0A.40}
$$

Source: (D.3.22). The project adopts the S-form Fierz identity of
(D.3.33) and its W-form partner (D.3.32) verbatim:

$$
\begin{aligned}
(s_S)_\alpha(s_S)_\beta={}&
+\frac14\mathcal C_{\alpha\beta}(\bar s_Ss_S)
+\frac14(\gamma_{5S}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}s_S)
+\frac14(\gamma_{5S}\gamma_{S\mu}\mathcal C)_{\alpha\beta}
(\bar s_S\gamma_{5S}\gamma_S^\mu s_S),\\
(s_W)_\alpha(s_W)_\beta={}&
-\frac14\mathcal C_{\alpha\beta}(\bar s_Ws_W)
-\frac14(\gamma_{5W}\mathcal C)_{\alpha\beta}
(\bar s_W\gamma_{5W}s_W)
+\frac14(\gamma_{5W}\gamma_{W\mu}\mathcal C)_{\alpha\beta}
(\bar s_W\gamma_{5W}\gamma_W^\mu s_W).
\end{aligned}
\tag{0A.41}
$$

### 3.8 Conditional register

$$
\boxed{
\begin{gathered}
\text{CONDITIONAL: }e^{2i\phi}=-1\text{ fixes }\phi\text{ only up to the
common sign }\pm i;\\
\text{CONDITIONAL: Weinberg-side gaugino phase is
SOURCE\_INSUFFICIENT;}\\
\text{CONDITIONAL: Majorana matrix identities on the Srednicki branch
are conditional checks only.}
\end{gathered}}
\tag{0A.42}
$$

CONDITIONAL: the adopted branches of (0A.38)–(0A.39) stand, but the
residual common sign is not fixed by the reality conditions; the
Weinberg-side gaugino phase remains unresolved at source level; and all
Majorana matrix identities are used as conditional checks only —
project quantities and phases remain as locked in the foundation
contracts, not re-derived from four-component identities. Sources:
(D.3.17), (D4.4).

## 4. Covariant derivatives — all tiers

### 4.1 Ordinary and Grassmann derivatives

The flat derivative is \(\partial_M\). Grassmann derivatives are left
derivatives,

$$
\partial_a:=\frac{\vec\partial}{\partial\vartheta^a},\qquad
\bar\partial^{\dot a}:=\frac{\vec\partial}{\partial\bar\vartheta_{\dot a}},
\qquad
\bar\partial_{\dot a}:=\epsilon_{\dot a\dot b}\bar\partial^{\dot b},
\tag{0A.43}
$$

$$
\{\partial_a,\vartheta^b\}=\delta_a{}^b,\qquad
\{\bar\partial_{\dot a},\bar\vartheta^{\dot b}\}
=-\delta_{\dot a}{}^{\dot b},\qquad
\partial_\zeta(FG)=(\partial_\zeta F)G
+(-1)^{|F|}F(\partial_\zeta G).
\tag{0A.44}
$$

Sources: (2A.4), (2A.5), (2A.6).

### 4.2 Component gauge-covariant derivative

$$
\boxed{
\mathcal D_M:=\partial_M-iA_M,\qquad
[\mathcal D_M,\mathcal D_N]=-iF_{MN},\qquad
F_{MN}=\partial_MA_N-\partial_NA_M-i[A_M,A_N],}
\tag{0A.45}
$$

with \(A_M:=A_M^AT_A\), \([T_A,T_B]=ic_{AB}{}^CT_C\),
\(T_A^\dagger=T_A\), \(c_{AB}{}^C\in\mathbb R\) (coupling absorbed).
Sources: (3A.2), (3A.3), (3A.8), (4.5), (4.50).

### 4.3 Supersymmetric derivatives

$$
\boxed{
D_a^L=\partial_a-i(\sigma_L^\mu\bar\vartheta)_a\partial_\mu^L,\qquad
\bar D_{\dot a}^L
=\bar\partial_{\dot a}+i(\vartheta\sigma_L^\mu)_{\dot a}\partial_\mu^L.}
\tag{0A.46}
$$

$$
\boxed{
D_a^E=\partial_a+(\sigma_E^m\bar\vartheta)_a\partial_m^E,\qquad
\bar D_{\dot a}^E
=\bar\partial_{\dot a}-(\vartheta\sigma_E^m)_{\dot a}\partial_m^E.}
\tag{0A.47}
$$

Sources: (2A.28), (2A.41), (D.4.8). The algebras are

$$
\{D_a^L,\bar D_{\dot b}^L\}
=+2i(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=-2(\sigma_L^\mu)_{a\dot b}\mathsf P_\mu^L,
\tag{0A.48}
$$

$$
\{D_a^E,\bar D_{\dot b}^E\}
=-2(\sigma_E^m)_{a\dot b}\partial_m^E
=+2(\sigma_E^m)_{a\dot b}\mathsf P_m^E,
\tag{0A.49}
$$

$$
\{D_a,D_b\}=\{\bar D_{\dot a},\bar D_{\dot b}\}=0,\qquad
\{D_a,\mathsf Q_b\}=\{D_a,\bar{\mathsf Q}_{\dot b}\}
=\{\bar D_{\dot a},\mathsf Q_b\}
=\{\bar D_{\dot a},\bar{\mathsf Q}_{\dot b}\}=0 .
\tag{0A.50}
$$

Sources: (2A.29), (2A.30), (2A.42).

### 4.4 Berezin powers, projectors, and measures

$$
D^2:=D^aD_a,\qquad
\bar D^2:=\bar D_{\dot a}\bar D^{\dot a},\qquad
D^2\vartheta^2=\bar D^2\bar\vartheta^2=-4 .
\tag{0A.51}
$$

$$
\boxed{
[X]_F:=-\frac14D^2X\Big|,\qquad
[\widetilde X]_{\widetilde F}:=-\frac14\bar D^2\widetilde X\Big|,\qquad
[Y]_D:=\frac1{16}D^2\bar D^2Y\Big|\ (\bar D^2\text{ acts first}).}
\tag{0A.52}
$$

$$
\int_{R,8}Y:=\int d^4x_R\,[Y]_D,\qquad
\int_{R,+}X:=\int d^4x_R\,[X]_F,\qquad
\int_{R,-}\widetilde X:=\int d^4x_R\,[\widetilde X]_{\widetilde F}.
\tag{0A.53}
$$

Sources: (3A.10)–(3A.16), (3B.3), (3B.4), (3D.4). The 16-normalized
D-algebra projectors of the Euclidean one-loop grammar are

$$
\boxed{
P_+:=\frac{\bar D^2D^2}{16\Box_E},\qquad
P_-:=\frac{D^2\bar D^2}{16\Box_E},\qquad
P_T:=-\frac{D^a\bar D^2D_a}{8\Box_E},\qquad
P_++P_-+P_T=1 .}
\tag{0A.54}
$$

LOCK at the algebra level; the FF-propagator application of these
projectors remains conditional per (5A.79). Sources: (5A.64)–(5A.66),
paper §2.

### 4.5 Operator tiers

$$
\boxed{
\mathsf G\ =\ \text{coordinate representation},\qquad
G\ =\ \text{abstract Noether charge},\qquad
\mathbb G=\mathsf G\otimes\mathbf1+\mathbf1\otimes G\ =\
\text{diagonal total},}
\tag{0A.55}
$$

with the covariance law \([\mathbb G_A,M_\Phi\}=0\). Sources:
(2A.15)–(2A.19), (2B.5), (2C.29e).

$$
\boxed{
\mathsf P_\mu^L=-i\partial_\mu^L,\qquad
\mathsf P_m^E=-\partial_m^E .}
\tag{0A.56}
$$

Sources: (2A.20), (2A.39), (2B.10), (2B.65).

$$
\mathsf Q_a^L=-i\partial_a+(\sigma_L^\mu\bar\vartheta)_a\partial_\mu^L,
\qquad
\bar{\mathsf Q}_{\dot a}^L
=-i\bar\partial_{\dot a}-(\vartheta\sigma_L^\mu)_{\dot a}\partial_\mu^L,
\tag{0A.57}
$$

$$
\{\mathsf Q_a^L,\bar{\mathsf Q}_{\dot b}^L\}
=2i(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=-2(\sigma_L^\mu)_{a\dot b}\mathsf P_\mu^L .
\tag{0A.58}
$$

$$
\mathsf Q_a^E=-\partial_a+(\sigma_E^m\bar\vartheta)_a\partial_m^E,\qquad
\bar{\mathsf Q}_{\dot a}^E
=-\bar\partial_{\dot a}-(\vartheta\sigma_E^m)_{\dot a}\partial_m^E,
\tag{0A.59}
$$

$$
\{\mathsf Q_a^E,\bar{\mathsf Q}_{\dot b}^E\}
=+2(\sigma_E^m)_{a\dot b}\partial_m^E
=-2(\sigma_E^m)_{a\dot b}\mathsf P_m^E .
\tag{0A.60}
$$

Sources: (2A.21), (2A.25), (2A.41), (2A.42). The bridge to the
textbook differential operator is

$$
\boxed{
\mathsf Q_a^L=-i\mathcal Q_a^S,\qquad
\bar{\mathsf Q}_{\dot a}^L=-i\mathcal Q^{S*}_{\dot a},\qquad
Q_a^L=Q_a^S\ \text{(Noether)},\qquad
[Q_a^L,\Phi\}=+i\mathcal Q_a^S\Phi .}
\tag{0A.61}
$$

LOCK: \(\mathsf Q\) carries an overall \(-i\) relative to the standard
differential operator \(\mathcal Q^S\); consequently
\(\{\mathsf Q,\bar{\mathsf Q}\}\) and \(\{D,\bar D\}\) have the same
sign here. Sources: (D.4.4), (D.4.6).

### 4.6 Chiral coordinates

$$
\boxed{
y_R:=x_R+s_RB_R,\qquad
\widetilde y_R:=x_R+t_RB_R,\qquad
s_L=-i,\ t_L=+i;\qquad
s_E=+1,\ t_E=-1 .}
\tag{0A.62}
$$

Equivalently \(y_L=x_L-iB_L\), \(\widetilde y_L=x_L+iB_L\),
\(y_E=x_E+B_E\), \(\widetilde y_E=x_E-B_E\), with
\(\bar D_Ry_R=0\), \(D_R\widetilde y_R=0\). Sources: (3B.5), (3B.6),
(3B.7), (2A.31), (2A.44).

### 4.7 Super-gauge-covariant derivatives

The symbol \(\nabla\) is reserved for gauge-covariant derivatives
((2A §2A.5)). Chiral frame \(\mathsf C\):

$$
\boxed{
\nabla_a^{\mathsf C}
=\mathcal E^{-1}\circ D_a\circ\mathcal E
=D_a+\Gamma_a,\qquad
\bar\nabla_{\dot a}^{\mathsf C}=\bar D_{\dot a} .}
\tag{0A.63}
$$

Antichiral frame \(\mathsf A\):

$$
\nabla_a^{\mathsf A}=D_a,\qquad
\bar\nabla_{\dot a}^{\mathsf A}
=\mathcal E\circ\bar D_{\dot a}\circ\mathcal E^{-1}
=\bar D_{\dot a}+\widetilde\Gamma_{\dot a} .
\tag{0A.64}
$$

Vector frame \(\mathsf V\) (bold = gauge-dressed):

$$
\boxed{
\boldsymbol\nabla^{\mathsf V}_{R\mathfrak A}
:=D_{R\mathfrak A}-i\boldsymbol{\mathcal A}^{\mathsf V}_{R\mathfrak A},
\qquad
\boldsymbol\nabla^{\mathsf V}_{Ra}
=\widetilde{\mathcal B}_R^{-1}\circ D_{Ra}\circ\widetilde{\mathcal B}_R,
\qquad
\bar{\boldsymbol\nabla}^{\mathsf V}_{R\dot a}
=\mathcal B_R\circ\bar D_{R\dot a}\circ\mathcal B_R^{-1}.}
\tag{0A.65}
$$

The connections are

$$
\boxed{
\Gamma_a:=\mathcal E^{-1}(D_a\mathcal E),\qquad
\widetilde\Gamma_{\dot a}:=\mathcal E(\bar D_{\dot a}\mathcal E^{-1}).}
\tag{0A.66}
$$

Sources: (3A.34), (3A.34a), (3C.15), (3C.22), (3C.25), (3C.27).

### 4.8 Torsion and the vector derivative

$$
\boxed{
\{\nabla_a,\bar\nabla_{\dot b}\}
=\kappa_R(\sigma_R^M)_{a\dot b}\mathcal D_M,\qquad
\kappa_L=2i,\qquad
\kappa_E=-2 .}
\tag{0A.67}
$$

LOCK: the flat torsion is \(T^R_{a\dot b}{}^M=\kappa_R(\sigma_R^M)_{a\dot b}\)
and is the only nonzero torsion component. Sources: (3C.14), (3C.23),
(3A.36), (3A.37), (3A.74).

$$
u_R:=\frac4{\kappa_R},\qquad
\rho_R:=\frac4{\kappa_R^2},\qquad
(u_L,\rho_L)=(-2i,-1),\qquad
(u_E,\rho_E)=(-2,+1).
\tag{0A.68}
$$

Sources: (3C.1), (3C.2).

$$
[\bar\nabla^{\mathsf V}_{\dot a},\mathcal D^{\mathsf V}_{b\dot b}]
=u_R\,\epsilon_{\dot a\dot b}\mathcal W^{\mathsf V}_b,\qquad
[\nabla^{\mathsf V}_a,\mathcal D^{\mathsf V}_{b\dot b}]
=u_R\,\epsilon_{ab}\widetilde{\mathcal W}^{\mathsf V}_{\dot b},\qquad
\nabla^a\mathcal W_a+\bar\nabla^{\dot a}\widetilde{\mathcal W}_{\dot a}=0 .
\tag{0A.69}
$$

Sources: (3C.40), (3C.43).

## 5. \(\vartheta\)-expansion of superfields

### 5.1 Coordinate/parameter lock

$$
\boxed{
(\vartheta^a,\bar\vartheta_{\dot a})\ =\
\text{superspace coordinates};\qquad
(\varepsilon^a,\bar\varepsilon_{\dot a})\ =\
\text{SUSY transformation parameters}.}
\tag{0A.70}
$$

LOCK: \(\vartheta\) is always the coordinate; \(\varepsilon\) is
always the parameter. The Step-1 usage of \(\theta\) for the
transformation parameter is superseded and \(\theta\) is retired as a
Grassmann symbol project-wide; the only surviving \(\theta\)-glyph is
the Yang–Mills angle \(\vartheta_{\rm YM}\). Sources: (2A.1), (2A.2);
Step-1 naming (1.18), (1.26) superseded.

### 5.2 Chiral and antichiral superfields

Chirality constraints \(\bar D_{\dot a}\Phi^I=0\),
\(D_a\widetilde\Phi_{\bar I}=0\) ((3A.17)); on the chiral/antichiral
coordinates,

$$
\boxed{
\Phi^I(y,\vartheta)=\phi^I(y)+\sqrt2\,\vartheta\psi^I(y)
+\vartheta^2F^I(y),\qquad
\widetilde\Phi_{\bar I}(\widetilde y,\bar\vartheta)
=\widetilde\phi_{\bar I}+\sqrt2\,\bar\vartheta\widetilde\psi_{\bar I}
+\bar\vartheta^2\widetilde F_{\bar I} .}
\tag{0A.71}
$$

Sources: (3A.23), (3A.24), (4B.36). The \(x\)-space forms are

$$
\begin{aligned}
\Phi_L^I={}&\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
-iB_L^\mu\partial_\mu\phi^I
+\frac{i}{\sqrt2}\vartheta^2(\partial_\mu\psi^{Ia})
(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Box_L\phi^I,\\
\Phi_E^I={}&\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
+B_E^m\partial_m\phi^I
-\frac1{\sqrt2}\vartheta^2(\partial_m\psi^{Ia})
(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Delta_E\phi^I,
\end{aligned}
\tag{0A.72}
$$

with the conjugate/independent antichiral mirrors of (3B.15)–(3B.16).
Component identifications:

$$
\boxed{
\phi^I:=\Phi^I\Big|,\qquad
\psi_a^I:=\frac1{\sqrt2}D_a\Phi^I\Big|,\qquad
F^I:=-\frac14D^2\Phi^I\Big|,}
\tag{0A.73}
$$

and the antichiral mirror
\(\widetilde\phi=\widetilde\Phi|\),
\(\widetilde\psi_{\dot a}=(1/\sqrt2)\bar D_{\dot a}\widetilde\Phi|\),
\(\widetilde F=-\frac14\bar D^2\widetilde\Phi|\). Sources: (3A.18),
(3A.19), (3B.2).

### 5.3 Monomials and top components

$$
\Theta_+:=\vartheta^a\vartheta_a=\vartheta^2,\qquad
\Theta_-:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}=\bar\vartheta^2,
\qquad
[\Theta_+]_F=1,\qquad
[\Theta_-]_{\widetilde F}=1,\qquad
[\Theta_+\Theta_-]_D=1 .
\tag{0A.74}
$$

Sources: (3D.10), (3D.11), (3B.4).

### 5.4 Vector superfield: Wess–Zumino surface

$$
\boxed{
\mathcal V_L^{\rm WZ}
=-2\vartheta\sigma_L^\mu\bar\vartheta\,A_\mu
+2i\vartheta^2\bar\vartheta_{\dot a}\bar\lambda^{\dot a}
-2i\bar\vartheta^2\vartheta^a\lambda_a
+\vartheta^2\bar\vartheta^2\mathscr D,}
\tag{0A.75}
$$

$$
\boxed{
\mathcal V_E^{\rm WZ}
=-2i\vartheta\sigma_E^m\bar\vartheta\,A_m
+2i\vartheta^2\bar\vartheta_{\dot a}\widetilde\lambda^{\dot a}
-2i\bar\vartheta^2\vartheta^a\lambda_a
+\vartheta^2\bar\vartheta^2\mathscr D.}
\tag{0A.76}
$$

LOCK: the coefficient \(-2\) on the gauge-field term (Euclidean
\(-2i\)) is deliberate; it is the \(e^{\mathcal V}\) normalization of
(0A.83), twice the common textbook coefficient. Sources: (3A.47),
(3A.48), (3B.27), (5A.30).

### 5.5 Field-strength superfield expansions

$$
\boxed{
\mathcal W_{La}(y_L,\vartheta)
=-i\lambda_a+\vartheta_a\mathscr D
+i(\sigma_L^{\mu\nu})_a{}^b\vartheta_bF_{\mu\nu}
-\vartheta^2(\sigma_L^\mu)_{a\dot b}\mathcal D_\mu\bar\lambda^{\dot b},}
\tag{0A.77}
$$

$$
\mathcal W_{Ea}(y_E,\vartheta)
=-i\lambda_a+\vartheta_a\mathscr D
-i(\sigma_E^{mn})_a{}^b\vartheta_bF_{mn}
-i\vartheta^2(\sigma_E^m)_{a\dot b}\mathcal D_m\widetilde\lambda^{\dot b}.
\tag{0A.78}
$$

Sources: (3A.58), (3A.59); antichiral mirrors (3A.59a)–(3A.59b).

### 5.6 Vector-multiplet component identifications

$$
\boxed{
\lambda_a:=i\mathcal W_a\Big|,\qquad
\widetilde\lambda_{\dot a}:=-i\widetilde{\mathcal W}_{\dot a}\Big|,\qquad
\mathscr D:=-\frac12D^a\mathcal W_a\Big|
=+\frac12\bar D^{\dot a}\widetilde{\mathcal W}_{\dot a}\Big| .}
\tag{0A.79}
$$

The last equality is the superspace Bianchi identity. Sources:
(3A.54), (3A.55), (3B.40).

### 5.7 Wess–Zumino projections and residual parameter

$$
\Gamma_{Ra}\Big|=0,\qquad
D_R^a\Gamma_{Ra}\Big|=0,\qquad
\nabla_{Ra}\Phi_R\Big|=D_{Ra}\Phi_R\Big|,\qquad
\nabla_R^2\Phi_R\Big|=D_R^2\Phi_R\Big|,
\tag{0A.80}
$$

$$
D_{Ra}\Lambda_R\Big|=D_R^2\Lambda_R\Big|=0 .
\tag{0A.81}
$$

Sources: (3A.50a), (3A.50b).

## 6. Vector versus chiral representation

### 6.1 Chiral representation and the bridge lock

$$
\boxed{
h=e^{i\Lambda},\quad
\widetilde h=e^{i\widetilde\Lambda},\quad
\bar D_{\dot a}\Lambda=0,\quad
D_a\widetilde\Lambda=0;\qquad
\Phi'=h\Phi,\quad
\widetilde\Phi'=\widetilde\Phi\widetilde h^{-1},\quad
\mathcal E'=\widetilde h\,\mathcal E\,h^{-1}.}
\tag{0A.82}
$$

$$
\boxed{
\mathcal E:=e^{\mathcal V}}
\tag{0A.83}
$$

LOCK: the bridge is the single-exponent \(e^{\mathcal V}\). The
textbook \(e^{2V}\) appears only in the dictionary tables (0A.90) and
is never a project primitive. Lorentzian reality
\(\mathcal V_L^{\ddagger_L}=\mathcal V_L\),
\(\widetilde\Lambda_L=\Lambda_L^{\ddagger_L}\). Sources: (3A.31),
(3A.32), (3A.33), (3D.36).

### 6.2 Field strengths

$$
\boxed{
\mathcal W_a:=-\frac18\bar D^2\big[\mathcal E^{-1}(D_a\mathcal E)\big]
=-\frac18\bar D^2\Gamma_a,\qquad
\widetilde{\mathcal W}_{\dot a}
:=+\frac18D^2\big[\mathcal E(\bar D_{\dot a}\mathcal E^{-1})\big]
=+\frac18D^2\widetilde\Gamma_{\dot a} .}
\tag{0A.84}
$$

LOCK: coefficient \(-\frac18\) (antichiral \(+\frac18\)) with the
single exponent, not the textbook \(-\frac14\bar D^2e^{-2V}De^{2V}\);
Step-3C explicitly declines the source coefficient and fixes the
definition by (3A.51)–(3A.55). Transformation laws
\(\mathcal W'=h\mathcal Wh^{-1}\),
\(\widetilde{\mathcal W}'=\widetilde h\widetilde{\mathcal W}\widetilde h^{-1}\).
Sources: (3A.51), (3A.52), (3A.53), (3B.35), (3C.34), (3C.79).

### 6.3 The three frames

$$
\mathsf V:=\text{gauge-vector frame},\qquad
\mathsf C:=\text{gauge-chiral frame},\qquad
\mathsf A:=\text{gauge-antichiral frame},
\tag{0A.85}
$$

distinct from the chiral coordinates \((y_R,\vartheta)\). The bridge
factors and their product obey

$$
\boxed{
\mathcal E=\widetilde{\mathcal B}\,\mathcal B=e^{\mathcal V},\qquad
\mathcal B'=k\mathcal Bh^{-1},\qquad
\widetilde{\mathcal B}'=\widetilde h\widetilde{\mathcal B}k^{-1},\qquad
h,\widetilde h,k,\mathcal B,\widetilde{\mathcal B}
\in G_{\mathbb C}^{\rm loc}.}
\tag{0A.86}
$$

Matter in the vector frame,

$$
\boldsymbol\Phi^{\mathsf V}=\mathcal B\Phi,\qquad
\widetilde{\boldsymbol\Phi}^{\mathsf V}
=\widetilde\Phi\widetilde{\mathcal B},\qquad
\widetilde\Phi\,\mathcal E\,\Phi
=\widetilde{\boldsymbol\Phi}^{\mathsf V}\boldsymbol\Phi^{\mathsf V},
\qquad
\boldsymbol\Phi^{\mathsf V}{}'=k\boldsymbol\Phi^{\mathsf V} .
\tag{0A.87}
$$

Sources: (3C.3), (3C.4), (3C.5), (3C.6), (3C.7), (3C.52), (3C.54),
(3C.55).

### 6.4 Symmetric bridge gauge and Wess–Zumino gauge

$$
\mathcal B=\widetilde{\mathcal B}=e^{\mathcal V/2}
\quad\text{(symmetric bridge gauge)},\qquad
k(\Lambda,\widetilde\Lambda)=e^{\mathcal V'/2}h e^{-\mathcal V/2},
\tag{0A.88}
$$

$$
\mathcal B\Big|=\widetilde{\mathcal B}\Big|=1,\qquad
D\mathcal B\Big|=D^2\mathcal B\Big|
=\bar D\mathcal B\Big|=\bar D^2\mathcal B\Big|=0
\quad\text{(WZ gauge)}.
\tag{0A.89}
$$

Sources: (3C.29), (3C.31), (3C.71).

### 6.5 Source dictionary (Project \(\leftrightarrow\) Srednicki
\(\leftrightarrow\) Weinberg)

Bridges and exponents:

$$
\boxed{
\mathcal E_P=e^{\mathcal V_P}=E_S=e^{-2gV_S}
=\Gamma_c=e^{-2t_AV_c^A},\qquad
\mathcal V_P=-2gV_S=-2t_AV_c^A=-2T_A\widehat V^A,\qquad
t_A=gT_A .}
\tag{0A.90}
$$

Components:

$$
A_P=gv_S=gV_c=\widehat V,\qquad
\lambda_P=-ig\lambda_S,\qquad
\bar\lambda_P=+ig\lambda_S^\dagger,\qquad
\mathscr D_P=-gD_S=-gD_c=-\widehat D,\qquad
F_P=gF_S=gf_c=\widehat f .
\tag{0A.91}
$$

Field strengths and the dotted-square sign:

$$
\mathcal W_{P,a}=-gW_{a,S},\qquad
\boxed{\mathcal D_S^{*2}=-\bar D_P^2 .}
\tag{0A.92}
$$

Projectors:

$$
[X]^P_F=[X]^S_F=[X]^W_{\mathcal F},\qquad
[X]^P_D=[X]^S_D=\frac12[X]^W_D+\frac14\Box C_X .
\tag{0A.93}
$$

Sources: (3B.114b)–(3B.114h), (D.8.12), (D.9.5), (D.9.9), (D4.2),
(D4.3). LOCK: the dotted-square identity is signed as in (0A.92);
Srednicki's \(\mathcal D_S^{*2}\theta_S^{*2}=+4\) is not used.

### 6.6 GGRS frame dictionary

$$
e^\Omega\leftrightarrow\widetilde{\mathcal B}_L,\qquad
e^{\bar\Omega}\leftrightarrow\mathcal B_L,\qquad
e^V=e^\Omega e^{\bar\Omega}\leftrightarrow\mathcal E_L=e^{\mathcal V_L},
\qquad
e^{iK}\leftrightarrow k_L,\qquad
e^{i\Lambda}\leftrightarrow h_L,\qquad
\Phi_{\rm vector}\leftrightarrow\boldsymbol\Phi^{\mathsf V}_L .
\tag{0A.94}
$$

Source: (3C.78).

## 7. Action and coupling conventions

### 7.1 Master action form

$$
\boxed{
S_L=\int d^4x_L\left\{
[\mathcal K_g]_D+[\mathcal U]_F+[\bar{\mathcal U}]_{\widetilde F}
+\frac14[f_{AB}\mathcal W^A\mathcal W^B]_F
+\frac14[\bar f_{AB}\widetilde{\mathcal W}^A
\widetilde{\mathcal W}^B]_{\widetilde F}
+\xi_A[\mathcal V^A]_D\right\}.}
\tag{0A.95}
$$

$$
\boxed{
S_E=\varsigma_E\int d^4x_E\{\cdots\},\qquad
\varsigma_L=+1,\qquad
\varsigma_E=-1 .}
\tag{0A.96}
$$

LOCK: the Euclidean action carries an overall minus, equivalently
\(\mathcal L_E=-\mathcal L_L|_{\rm Wick}\) of (0A.10). Sources:
(3A.67), (3A.93), (3C.62), (3C.63), (4B.8), (4C.4).

### 7.2 Densities and couplings

Canonical Kähler D-density:

$$
\boxed{
\mathcal K_g=\widetilde\Phi\,\mathcal E\,\Phi .}
\tag{0A.97}
$$

Gauge-kinetic function, real and imaginary parts:

$$
f_{AB}=f_{BA}=\mathfrak h_{AB}+i\mathfrak k_{AB},\qquad
\mathfrak h_{AB}:=\operatorname{Re}f_{AB}=\frac12(f+\bar f)_{AB},\qquad
\mathfrak k_{AB}:=\operatorname{Im}f_{AB}=\frac1{2i}(f-\bar f)_{AB} .
\tag{0A.98}
$$

Absorbed-coupling basis:

$$
\boxed{
h:=g^{-2},\qquad
\mathfrak h_{AB}=g^{-2}\kappa_{AB},\qquad
\mathfrak k_{AB}=-\frac{\vartheta_{\rm YM}}{8\pi^2}\kappa_{AB},\qquad
c_{ABC}:=\kappa_{CD}c_{AB}{}^D=c_{[ABC]} .}
\tag{0A.99}
$$

Sources: (3A.73), (3A.85), (3A.88), (3B.85), (3B.114k), (4.11),
(4B.0a), (5A.2). Fayet–Iliopoulos data are Abelian-only:

$$
\xi_Ac_{BC}{}^A=0 .
\tag{0A.100}
$$

Source: (3A.72). The component gauge Lagrangian in the absorbed
basis is

$$
\mathcal L_{\rm gauge}
=-\frac14\mathfrak h_{AB}F^AF^B
+i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B
+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\frac18\mathfrak k_{AB}\,
\epsilon_L^{\mu\nu\rho\sigma}F_{\mu\nu}^AF_{\rho\sigma}^B .
\tag{0A.101}
$$

Sources: (3A.86), (4A.9); Euclidean partner (4A.56b), (5A.3)–(5A.6).

## 8. BV–BRST

### 8.1 Gradings and antifields

For every homogeneous object \(X\),

$$
\epsilon_X\in\mathbb Z_2,\qquad
\operatorname{gh}(X)\in\mathbb Z,\qquad
[X]\in\frac12\mathbb Z .
\tag{0A.102}
$$

The symbol \(X^\star\) denotes the BV antifield and never denotes
complex conjugation:

$$
\boxed{
\epsilon_{X^\star}=\epsilon_X+1,\qquad
\operatorname{gh}(X^\star)=-1-\operatorname{gh}(X),\qquad
[X^\star]=d_{\Sigma_X}-[X],\qquad
d_8=2,\quad d_+=d_-=3 .}
\tag{0A.103}
$$

Sources: (3D.2), (3D.3), (3D.52).

### 8.2 Field, ghost, and antifield inventory

$$
\begin{array}{c|c|c|c|c|c}
\text{field} & \text{domain} & \epsilon & \operatorname{gh} & [X] &
[X^\star]\\ \hline
\mathcal V & \Sigma_{R,8} & 0 & 0 & 0 & 2\\
\Phi^I & \Sigma_{R,+} & 0 & 0 & 1 & 2\\
\widetilde\Phi_I & \Sigma_{R,-} & 0 & 0 & 1 & 2\\
\mathfrak c & \Sigma_{R,+} & 1 & 1 & 0 & 3\\
\widetilde{\mathfrak c} & \Sigma_{R,-} & 1 & 1 & 0 & 3\\
\mathfrak c' & \Sigma_{R,\pm} & 1 & -1 & 2 & 1\\
\mathfrak n & \Sigma_{R,\pm} & 0 & 0 & 2 & 1
\end{array}
\tag{0A.104}
$$

Sources: (3D.51), (3D.52), (3D.87).

### 8.3 Ghosts and the BRST differential

One chiral and one antichiral Faddeev–Popov ghost,

$$
\boxed{
\mathfrak c=\mathfrak c^AT_A,\quad
\bar D_{\dot a}\mathfrak c=0;\qquad
\widetilde{\mathfrak c}=\widetilde{\mathfrak c}^AT_A,\quad
D_a\widetilde{\mathfrak c}=0;\qquad
\epsilon_{\mathfrak c}=1,\quad
\operatorname{gh}(\mathfrak c)=1,\quad
[\mathfrak c]=0 .}
\tag{0A.105}
$$

The bold odd derivation \(\mathbf s_R\), \(\epsilon(\mathbf s)=1\),
\(\operatorname{gh}(\mathbf s)=1\), \([\mathbf s]=0\), acts as

$$
\boxed{
\mathbf s\mathcal E=i\widetilde{\mathfrak c}\mathcal E-i\mathcal E\mathfrak c,
\qquad
\mathbf s\mathfrak c=i\mathfrak c^2,\qquad
\mathbf s\widetilde{\mathfrak c}=i\widetilde{\mathfrak c}^2,\qquad
\mathbf s\Phi=i\mathfrak c\Phi,\qquad
\mathbf s\widetilde\Phi=-i\widetilde\Phi\widetilde{\mathfrak c},}
\tag{0A.106}
$$

$$
\mathbf s\mathfrak c^C=-\frac12c_{AB}{}^C\mathfrak c^A\mathfrak c^B,
\qquad
\mathbf s^2=0,\qquad
\mathbf sS_{0,R}=0 .
\tag{0A.107}
$$

LOCK: the \(i\)-ful BRST convention of (0A.106), paired with the
Hermitian generators of (0A.45); an \(i\)-less math-BRST convention is
not used. Sources: (3D.43), (3D.43a), (3D.44)–(3D.46), (3D.50),
(5A.35)–(5A.38). The prepotential form is

$$
\mathbf s_R\mathcal V_R
=\frac{\operatorname{ad}_{\mathcal V_R}}
{1-e^{-\operatorname{ad}_{\mathcal V_R}}}
\left(ie^{-\operatorname{ad}_{\mathcal V_R}}\widetilde{\mathfrak c}_R
-i\mathfrak c_R\right).
\tag{0A.108}
$$

Source: (3D.48).

### 8.4 Antibracket

$$
\boxed{
(F,G)_R:=\sum_X\int_{\Sigma_X}\left[
F\frac{\overleftarrow\delta}{\delta X_R}\,
\frac{\vec\delta G}{\delta X_R^\star}
-
F\frac{\overleftarrow\delta}{\delta X_R^\star}\,
\frac{\vec\delta G}{\delta X_R}\right].}
\tag{0A.109}
$$

$$
(\widehat Q^{\mathsf i},\widehat Q^\star_{\mathsf j})
=\delta^{\mathsf i}{}_{\mathsf j},\qquad
\epsilon_{(F,G)}=\epsilon_F+\epsilon_G+1,\qquad
\operatorname{gh}(F,G)=\operatorname{gh}F+\operatorname{gh}G+1,\qquad
(F,G)=-(-1)^{(\epsilon_F+1)(\epsilon_G+1)}(G,F).
\tag{0A.110}
$$

Sources: (3D.54), (3D.55), (5A.40). Pairing orientation and sign
rule: in \(\langle X^\star,\mathbf sX\rangle\) the antifield sits on
the left and the variation on the right (3D.53), and the left
derivative obeys the Leibniz sign rule
\((-1)^{\epsilon_j\sum_{k<j}\epsilon_k}\) (5A.61); with these, the
signs of (0A.111) and (0A.118) follow from (0A.109) internally.

### 8.5 Minimal master action and classical master equation

$$
\boxed{
S_{\min}=S_0+\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
\langle Q^\star_{\mathfrak i},\mathbf sQ^{\mathfrak i}\rangle
=S_0+\langle\mathcal V^\star,\mathbf s\mathcal V\rangle_8
+\langle\Phi^\star,\mathbf s\Phi\rangle_+
+\langle\widetilde\Phi^\star,\mathbf s\widetilde\Phi\rangle_-
-\langle\mathfrak c^\star,\mathbf s\mathfrak c\rangle_+
-\langle\widetilde{\mathfrak c}^\star,
\mathbf s\widetilde{\mathfrak c}\rangle_- .}
\tag{0A.111}
$$

$$
\frac12(S_{\min},S_{\min})=0,\qquad
\mathbf sF=(S_{\min},F) .
\tag{0A.112}
$$

LOCK: at finite cutoff the regulated identity retains its defect,
\(\frac12(S_{\min,\nu},S_{\min,\nu})
=\mathbf s_\nu S_{0,\nu}+\sum(-1)^{\epsilon_{\mathfrak i}}Q^\star_{\mathfrak i}
\mathfrak r^{\mathfrak i}\); it is not set to zero. Sources: (3D.56),
(3D.56a), (3D.57), (3D.58), (3D.59), (3D.60), (5A.41)–(5A.42b).

### 8.6 BV Laplacian and quantum master equation

$$
\boxed{
\Delta_0F:=\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
\frac{\vec\partial}{\partial\widehat Q^{\mathfrak i}}
\frac{\vec\partial F}{\partial\widehat Q^\star_{\mathfrak i}},\qquad
\Delta:=\Delta_0+\frac12(\log\widehat{\boldsymbol\varpi},\cdot),\qquad
\Delta^2=0 .}
\tag{0A.113}
$$

$$
\boxed{
\frac12(W_L,W_L)-i\hbar\Delta_LW_L=0\ (L),\qquad
\frac12(W_E,W_E)-\hbar\Delta_EW_E=0\ (E),\qquad
\mathfrak e_L^{\rm QME}:=i,\qquad
\mathfrak e_E^{\rm QME}:=1 .}
\tag{0A.114}
$$

Loop expansion \(W=\sum_n\hbar^nM_n\), \(M_0=S_{\min}\), with recursion
\(\mathbf sM_n=\mathfrak e_R^{\rm QME}\Delta M_{n-1}
-\frac12\sum_{k=1}^{n-1}(M_k,M_{n-k})\). Sources: (3D.60a), (3D.61),
(3D.63), (3D.64)–(3D.66), (3D.68a), (3D.69), (5A.42c)–(5A.42f).

### 8.7 Non-minimal sector, gauge fermion, gauge-fixing graph

$$
\boxed{
\mathbf s\mathfrak c'=\mathfrak n,\qquad
\mathbf s\mathfrak n=0,\qquad
\widetilde{\mathfrak c}'_L=-(\mathfrak c'_L)^{\ddagger_L},\qquad
\widetilde{\mathfrak n}_L=+(\mathfrak n_L)^{\ddagger_L} .}
\tag{0A.115}
$$

$$
\boxed{
\Psi=\langle\mathfrak c',\mathcal F\rangle
-\frac12\langle\mathfrak c',\mathcal Y\mathfrak n\rangle,\qquad
\epsilon_\Psi=1,\quad
\operatorname{gh}\Psi=-1,\quad
[\Psi]=0,\qquad
\Psi_L^{\ddagger_L}=-\Psi_L .}
\tag{0A.116}
$$

LOCK: the gauge fermion is anti-Hermitian under \(\ddagger_L\). The
background-covariant gauge condition is

$$
\mathcal F_+=-\frac14(\bar{\boldsymbol\nabla}^{\mathsf V}_{\rm B})^2
\mathcal V_{\rm q},\qquad
\mathcal F_-=-\frac14(\boldsymbol\nabla^{\mathsf V}_{\rm B})^2
\mathcal V_{\rm q},\qquad
[\mathcal F_\pm]=1 .
\tag{0A.117}
$$

Sources: (3D.70), (3D.87), (3D.74), (3D.75), (3D.89), (3D.86),
(5A.43)–(5A.46). The gauge-fixing graph carries the MINUS sign:

$$
\boxed{
X^\star_{\rm BV}=X^{\star\,{\rm ext}}
-\frac{\vec\delta\Psi}{\delta X},\qquad
S_\Psi=S_0+\mathbf s\Psi .}
\tag{0A.118}
$$

Sources: (3D.76), (3D.77).

### 8.8 Conjugation signs

$$
\boxed{
(X_L^\star)^{\ddagger_L}=-(X_L^{\ddagger_L})^\star,\qquad
(\mathbf s_LX)^{\ddagger_L}
=(-1)^{\epsilon_X}\mathbf s_L(X^{\ddagger_L}),\qquad
\widetilde{\mathfrak c}_L=\mathfrak c_L^{\ddagger_L} .}
\tag{0A.119}
$$

LOCK: the antifield conjugation carries the minus sign of (0A.119);
these signs propagate verbatim into every channel. Sources: (3D.52a),
(3D.49).

### 8.9 Functional chain

$$
\boxed{
\mathcal Z_\Psi\ \text{unnormalized},\qquad
Z_\Psi=\frac{\mathcal Z_\Psi}{\mathcal Z_\Psi[0]},\qquad
\mathscr W_c=\frac{\upsilon_R}{\tau_R}\log Z_\Psi,\qquad
\mathscr W_{c,L}=-i\hbar\log Z_L,\quad
\mathscr W_{c,E}=+\hbar\log Z_E .}
\tag{0A.120}
$$

$$
\mathscr S^{\rm 1PI}
=\upsilon_R\left(\mathscr W_c
-\langle\jmath,\mathcal Q_{\rm mean}\rangle\right),\qquad
\mathcal Q_{\rm mean}
=\frac{\vec\delta\mathscr W_c}{\delta\jmath} .
\tag{0A.121}
$$

Sources: (3D.125), (3D.125a), (3D.126), (3D.127).

### 8.10 Wick transport of BV data

$$
\boxed{
\Psi_E=-i\Psi_L\big|_{\rm Wick},\qquad
W_E=-iW_L\big|_{\rm Wick},\qquad
\mathscr W_{c,E}=i\mathscr W_{c,L}\big|_{\rm Wick},\qquad
\mathscr S^{\rm 1PI}_E=-i\mathscr S^{\rm 1PI}_L\big|_{\rm Wick} .}
\tag{0A.122}
$$

$$
Q^\star_E=-iQ^\star_L(M^{\rm W})^{-1},\qquad
\widehat\jmath_E=+i\widehat\jmath_L(M^{\rm W})^{-1},\qquad
\mathcal Q_{{\rm mean},E}=M^{\rm W}\mathcal Q_{{\rm mean},L} .
\tag{0A.123}
$$

Sources: (3D.118a), (3D.120), (3D.128a).

### 8.11 Berezin orientation

$$
\boxed{
\int d\eta^{n}\cdots d\eta^2d\eta^1\,\eta^1\eta^2\cdots\eta^{n}=1,}
\tag{0A.124}
$$

LOCK: measure orders even coordinates by the coefficient order
\(\prec_\nu\) and odd coordinates by the reversed order \(\succ_\nu\).
Sources: (3D.18), (3D.19).

## 9. Extended-SUSY packaging

### 9.1 \(\mathrm{SU}(2)_R\)

$$
\varepsilon^{12}=+1,\qquad
\varepsilon_{12}=-1,\qquad
v_i=\varepsilon_{ij}v^j,\qquad
v^i=\varepsilon^{ij}v_j,\qquad
i,j=1,2 .
\tag{0A.125}
$$

Fermion and parameter doublets:

$$
\chi_{1a}:=\psi_a,\qquad
\chi_{2a}:=-\lambda_a;\qquad
\bar\chi^1=\bar\psi,\qquad
\bar\chi^2=-\bar\lambda;\qquad
\zeta^1:=\varepsilon,\qquad
\zeta^2:=-\eta .
\tag{0A.126}
$$

Auxiliary triplet and the shifted D:

$$
Y_{11}:=-\sqrt2F,\qquad
Y_{22}:=-\sqrt2\widetilde F,\qquad
Y_{12}=Y_{21}:=iH,\qquad
Y^{ij}:=\varepsilon^{ik}\varepsilon^{jl}Y_{kl},\qquad
(Y_{ij})^\dagger=Y^{ij},\qquad
H^A:=\mathscr D^A+\mu^A .
\tag{0A.127}
$$

Sources: (4.15), (4.16), (4.17), (4.18), (4.19), (4.19a), (4.20),
(4B.27)–(4B.28), (4B.12), (4B.9).

### 9.2 \(\mathrm{SU}(3)\) flavour and \(\mathrm{SU}(4)_R\)

$$
r,s,t=1,2,3,\qquad
\varepsilon^{123}=\varepsilon_{123}=+1;\qquad
\mathcal I,\mathcal J=1,\ldots,4,\qquad
\epsilon_{1234}=\epsilon^{1234}=+1 .
\tag{0A.128}
$$

$$
\Lambda_a^{\mathcal I}
=(\psi_{1a},\psi_{2a},\psi_{3a},\lambda_a),\qquad
\Lambda_a^4:=\lambda_a,\qquad
\Lambda_a^r:=\psi_{ra} .
\tag{0A.129}
$$

$$
\boxed{
\varphi^{r4}:=\phi_r,\qquad
\varphi^{rs}:=\varepsilon^{rst}\widetilde\phi_t,\qquad
\varphi^{\mathcal I\mathcal J}=-\varphi^{\mathcal J\mathcal I},\qquad
\widetilde\varphi_{\mathcal I\mathcal J}
:=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varphi^{\mathcal K\mathcal L},\qquad
(\varphi^{\mathcal I\mathcal J})^\dagger
=\widetilde\varphi_{\mathcal I\mathcal J} .}
\tag{0A.130}
$$

Sources: (4.22), (4.26), (4.27), (4.28), (4.30), (4C.5), (4C.25a).

### 9.3 \(N=4\) superpotential and the R-charge branch

$$
\boxed{
\mathcal U_4=-\frac{\sqrt2}{6g^2}\varepsilon_{rst}c_{ABC}
\Phi_r^A\Phi_s^B\Phi_t^C .}
\tag{0A.131}
$$

$$
\boxed{
r=-\frac{2\Delta}3\ \text{(chiral primary)},\qquad
[R,Q_a]=-Q_a .}
\tag{0A.132}
$$

LOCK: the R-normalization \(\mathsf R\vartheta^a=\vartheta^a\) fixes
the branch \(r=-2\Delta/3\); the opposite-sign branch is not used.
Sources: (4C.12), (4C.13), (2B.20), (2B.55), (2C.29b).

### 9.4 Adjoint bracket package

$$
\operatorname{tr}_\kappa(XY):=\kappa_{AB}X^AY^B,\qquad
\llbracket X,Y\rrbracket^A:=ic_{BC}{}^AX^BY^C,\qquad
(X\times Y)^A:=-i\llbracket X,Y\rrbracket^A,\qquad
\operatorname{tr}_\kappa(X\llbracket Y,Z\rrbracket)
=\operatorname{tr}_\kappa(\llbracket X,Y\rrbracket Z) .
\tag{0A.133}
$$

Sources: (4.7), (4.9), (5A.2).

## 10. Regulator and measure notation

### 10.1 Path-integral weights

$$
\boxed{
\mathcal Z_L=\int d\mu_L\,
e^{(i/\hbar)(S_{0,L}+\mathcal J_L)},\qquad
\mathcal Z_E=\int d\mu_E\,
e^{-S_{0,E}/\hbar+\mathcal J_E/\hbar} .}
\tag{0A.134}
$$

Sources: (3D.6), (3D.9), (3D.24), (3D.27), (5A.2).

### 10.2 DRED and dimension shift

$$
\boxed{
d=4-2\epsilon,\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},\qquad
\widehat\delta^m{}_m=d,\qquad
\breve\delta^m{}_m=2\epsilon,\qquad
\widehat\delta\,\breve\delta=0 .}
\tag{0A.135}
$$

$$
\boxed{
\delta_d=\bar\delta+\widetilde\delta,\qquad
\operatorname{tr}\bar\delta=4,\qquad
\operatorname{tr}\widetilde\delta=-2\epsilon,\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2 .}
\tag{0A.136}
$$

LOCK: the two projector pairs \((\widehat\delta,\breve\delta)\) and
\((\bar\delta,\widetilde\delta)\) are never cross-contracted; the
regulator axiom reads "spin words use \(\bar\delta\), propagator
inverses use \(\delta_d\)". Sources: step-05 §1 (boxed), paper §3.

### 10.3 Loop measure and Fourier

$$
\int_\ell^{\rm DRED}
:=\mu^{2\epsilon}\int\frac{d^{\,d}\ell}{(2\pi)^d},\qquad
X(x)=\int\frac{d^{\,d}p}{(2\pi)^d}e^{ip\cdot x}X(p),\qquad
\Box_E\mapsto-p^2,\qquad
\text{all momenta incoming} .
\tag{0A.137}
$$

Sources: step-05 §1, (5A.74), paper §3.

### 10.4 BV measure density and reference scale

$$
\boxed{
d\mu_{R,\nu}
=\boldsymbol\varpi_{R,\nu}(\widehat q)\,
{\prod}^{\prec_\nu}d\widehat q^{\rm even}\,
{\prod}^{\succ_\nu}d\widehat q^{\rm odd},\qquad
\epsilon_{\boldsymbol\varpi}
=\operatorname{gh}(\boldsymbol\varpi)
=[\boldsymbol\varpi]=0,\quad
\boldsymbol\varpi\ \text{nowhere vanishing},}
\tag{0A.138}
$$

$$
\boldsymbol\varpi'=\boldsymbol\varpi\,
\operatorname{Ber}(\vec\partial\widehat q/\partial\widehat q'),\qquad
\widehat q:=\mu^{-[q]}q,\qquad
\mu>0\ \text{reference scale} .
\tag{0A.139}
$$

LOCK: \(\boldsymbol\varpi\) is a free quantization datum, not fixed
by \(S_0\). Sources: (3D.17), (3D.18), (3D.18a), (3D.22).

## 11. Deviation and branch ledger

Every deliberate fork from a textbook anchor is registered below.
Status vocabulary: LOCK (project-wide), CONDITIONAL (residual gap
retained), OUT_OF_SCOPE (Section 14).

| # | Item | Project lock | Textbook anchor | Source tag | Status |
|---|---|---|---|---|---|
| 1 | Metric signature | \(\eta_L=(-,+,+,+)\), (0A.2) | \((+,-,-,-)\) | (1.2), (2B.34b), (D.2.1) | LOCK |
| 2 | SUSY anticommutator | \(\{Q,\bar Q\}=-2\sigma P\) | \(+2\sigma P\) | (1.39), (D.6.1) | LOCK (of #1) |
| 3 | SUSY derivative sign | \(D_a=\partial_a-i(\sigma\bar\vartheta)\partial\), (0A.46) | \(+i\) term | (2A.28), (D.4.8) | LOCK (of #1) |
| 4 | Bridge exponent | \(\mathcal E=e^{\mathcal V}\), (0A.83) | \(e^{2V}\) | (3A.32), (3D.36) | LOCK |
| 5 | \(\mathcal W\) normalization | \(-\frac18\bar D^2(\mathcal E^{-1}D\mathcal E)\), (0A.84) | \(-\frac14\bar D^2e^{-2V}De^{2V}\) | (3A.51), (3C.79) | LOCK |
| 6 | WZ vector coefficient | \(-2\vartheta\sigma\bar\vartheta A\), (0A.75) | \(\mp\vartheta\sigma\bar\vartheta A\) | (3A.47) | LOCK (of #4) |
| 7 | Operator bridge | \(\mathsf Q^L=-i\mathcal Q^S\), (0A.61) | differential \(Q\) primary | (D.4.4) | LOCK |
| 8 | Torsion constant | \(\kappa_L=2i\), \(\kappa_E=-2\), (0A.67) | Lorentzian-only value | (3C.1), (3A.74) | LOCK |
| 9 | BRST \(i\)-factors | \(\mathbf s\mathfrak c=i\mathfrak c^2\), (0A.106) | \(i\)-less \(sc=-\frac12fcc\) | (3D.44), (3D.45) | LOCK |
| 10 | Dotted-square identity | \(\mathcal D_S^{*2}=-\bar D_P^2\), (0A.92) | \(\mathcal D_S^{*2}\theta^{*2}=+4\) | (3B.114h) | LOCK |
| 11 | R-charge branch | \(r=-2\Delta/3\), (0A.132) | \(r=+2\Delta/3\) | (2B.55), (2C.29b) | LOCK |
| 12 | Gauge-fermion reality | \(\Psi^{\ddagger_L}=-\Psi\), (0A.116) | Hermitian \(\Psi\) | (3D.75) | LOCK |
| 13 | Antifield conjugation | \((X^\star)^{\ddagger_L}=-(X^{\ddagger_L})^\star\), (0A.119) | plus sign | (3D.52a) | LOCK |
| 14 | Grassmann glyph split | \(\vartheta\) coordinate, \(\varepsilon\) parameter, (0A.70) | \(\theta\) coordinate; Step-1 \(\theta\)-parameter | (2A.2) | LOCK (Step-1 naming superseded) |
| 15 | Weinberg D-term | \([X]^P_D=\frac12[X]^W_D+\frac14\Box C_X\), (0A.93) | plain equality | (3B.114b), (D.8.12) | LOCK |
| 16 | Euclidean \(\theta\)-term | relative \(i\) in \(\mathcal L_E\), (0A.11) | no relative \(i\) | (5A.3)–(5A.6), (3B.99) | LOCK |
| 17 | Killing vector | \(X_A^I:=i(T_A)^I{}_J\Phi^J\) | \(X_A=T_A\phi\) | (3A.69) | LOCK |
| 18 | Chiral coordinate | \(y_L=x_L-iB_L\), \(y_E=x_E+B_E\), (0A.62) | \(y=x+i\theta\sigma\bar\theta\) | (2A.31), (2A.44) | LOCK (of #1) |
| 19 | Majorana common sign | \(+i\) branch adopted, \(e^{2i\phi}=-1\) residual | — | (D.3.17), (D.3.18) | CONDITIONAL |
| 20 | Weinberg gaugino phase | unresolved at source | — | (D4.4) | CONDITIONAL (SOURCE_INSUFFICIENT) |
| 21 | Majorana matrix identities | conditional checks only, (0A.42) | — | (D.3.x) | CONDITIONAL |
| 22 | Euclidean adjoint | none intrinsic; \(\dagger_W\) only, (0A.28) | OS/reflection adjoint | (2A.52), (D.5.4) | LOCK |
| 23 | Finite-cutoff CME | defect retained, (0A.112) | zero at finite cutoff | (3D.60) | LOCK (by design) |
| 24 | DRED two-projector rule | \(\bar\delta\ne\delta_4\), no cross-contraction, (0A.136) | single \(d\)-dimensional metric | step-05 §1 | LOCK |
| 25 | \(N=2\)↔\(N=4\) closure signs | deferred cross-check | — | (4B.43)–(4B.46) vs (4C.37)–(4C.38a) | OUT_OF_SCOPE_N2_N4_CLOSURE_CROSSCHECK |

Where extraction reports disagreed, this contract follows the
foundation contracts over the paper, and Steps 01–03d over Step-04/05
restatements; each such call is one of the rows above.

## 12. Symbol-collision registry

| Symbol | Reserved meaning (this contract) | Colliding/forbidden use | Source tag |
|---|---|---|---|
| \(\vartheta,\bar\vartheta\) | superspace Grassmann coordinates, (0A.70) | \(\theta\) retired as Grassmann symbol; \(\vartheta_{\rm YM}\) is the theta angle | (2A.2), (4.11) |
| \(\theta\) | retired; Step-1 parameter naming superseded | never a coordinate | (2A.2) |
| \(\epsilon\) (macro) | spinor metric, spacetime Levi-Civita, \(\mathrm{SU}(4)_R\) tensor | not for SUSY parameters | (1.3), (4.26) |
| \(\varepsilon\) (macro) | SUSY parameters, \(\mathrm{SU}(2)_R\) metric, \(\mathrm{SU}(3)\) flavour | not the spinor metric | (2A.2), (4.15), (4.22) |
| \(\epsilon\) in \(d=4-2\epsilon\) | DRED regulator | distinct from every Levi-Civita by context | step-05 §1 |
| \(\mathcal D_M\) | gauge-covariant derivative, (0A.45) | not the auxiliary field | (3A.3) |
| \(\mathscr D\) | vector-multiplet auxiliary field, (0A.79) | not a derivative, not \([\cdot]_D\) | (3A.54) |
| \([\cdot]_D\) | D-term projector, (0A.52) | not the auxiliary field | (3A.14) |
| \(\mu\) | Lorentz index | moment map \(\mu_A\) (0A.127); 't Hooft scale \(\mu^{2\epsilon}\) (0A.137) | (4B.9), step-05 §1 |
| \(\tau_R\) | RESERVED: path-integral weights \(i/\hbar,-1/\hbar\), (0A.12) | Step-3C algebraic constant \(\tau_L:=i,\tau_E:=-i\) shadowed; use \(u_R,\rho_R\) | (3D.6), (3C.72h) |
| \(s_R,t_R\) | chiral-coordinate constants \((-i,+i)/(+1,-1)\), (0A.62) | never BRST | (3B.5) |
| \(\mathbf s\) | BRST differential (bold), (0A.106) | plain \(s\) never BRST | (3D.43a), (3D.133) |
| \(X^\star\) | BV antifield, (0A.103) | never complex conjugation | (3D.3) |
| \(\ddagger_L\) | Lorentzian formal adjoint, (0A.27) | not \(\dagger_{\mathcal H}\), not \(\dagger_W\) | (2A.35) |
| \(\dagger_W\) | Wick-transported adjoint, (0A.29) | not an intrinsic Euclidean adjoint | (2A.52) |
| bold glyphs | gauge-dressed/vector-frame objects (\(\boldsymbol\nabla^{\mathsf V},\boldsymbol{\mathcal A},\boldsymbol{\mathcal D},\boldsymbol\Phi^{\mathsf V}\)) and \(\boldsymbol\varpi\) | bridges \(\mathcal B,\widetilde{\mathcal B},\mathcal E\) are not bold | (3C.15), (3D.18) |
| \(Q/\mathsf Q/\mathcal Q\) | Noether charge / coordinate rep / textbook differential operator, (0A.55), (0A.61) | never interchanged | (2A.15)–(2A.21), (D.4.4), (D.0.2) |
| \(h\) | chiral gauge parameter \(e^{i\Lambda}\), (0A.82) | absorbed coupling \(h=g^{-2}\), (0A.99); never in one equation | (3A.31), (4B.0a) |
| \(\kappa\) | Killing metric \(\kappa_{AB}\), (0A.99) | torsion constant \(\kappa_R\), (0A.67); Clifford sign \(\kappa_{W/S}\), (D.3.11) | (3C.1) |
| \(F\) | chiral auxiliary, (0A.73) | \(F_{MN}\) curvature; \(\mathcal F_\pm\) gauge functions | (3A.18), (3D.86) |
| \(\mathcal E\) | gauge bridge \(e^{\mathcal V}\), (0A.83) | Euler operator \(\mathcal E_\Xi\) in current algebra | (3A.32), (4B.47c) |
| \(P_+,P_-,P_T\) | D-algebra projectors, (0A.54) | momentum \(P\); \(P_{\dot a}:=\mathcal D_{+\dot a}\) (step-05) | (5A.64)–(5A.66) |
| \(\mathfrak c,\widetilde{\mathfrak c}\) | chiral/antichiral FP ghosts, (0A.105) | not antighosts; antighost is \(\mathfrak c'\) | (3D.43), (3D.87) |
| \(\Theta_\pm\) | top monomials \(\vartheta^2,\bar\vartheta^2\), (0A.74) | \(\Theta_W\) Weinberg 4-coordinate, (0A.39) | (3D.10), (D.7.7) |

## 13. Compliance and citation rules

(a) The three approximation macros banned by the repository policy
test (referred to descriptively in Section 0.1) are forbidden in this
contract and in every document citing it.

(b) Equation tags in this contract are (0A.n), contiguous from
1; lettered subtags are used sparingly (only (0A.12a)).

(c) Citation rule:

$$
\boxed{
\text{Channels ec/es/lc/ls and paper/awi-n4-one-loop.md cite
FOUNDATION-UNIFIED-NOTATION-CONVENTION-000 for any symbol of
Sections 1--10.}}
\tag{0A.140}
$$

(d) File-local symbols — symbols not covered by Sections 1–10 — remain
governed by per-file notation ledgers and still require a local ledger
entry in the citing document.

(e) Any change to a lock in Sections 1–10 is a CONTRACT_CHANGE and
travels in one pull request with: the task packet rotation in
tasks/CURRENT.yaml (type CONTRACT_CHANGE); the
ledger/proof_obligations.json registration of the CURRENT id with its
task_sha256 pin; the contracts/manifest.yaml registration (JSON
syntax) with a make-hashes re-hash of all entries; the audit triplet
audits/step00-{notation-ledger,gap-audit,independent-review}.json with
result PASS, empty P0/P1, and all findings RESOLVED; the byte-exact
verifier scripts/verify_step00_\*.py regenerating the committed
audits/\*-verification.json byte-for-byte; the companion assertions
in tests/test_repository_policy.py; the paper/awi-n4-one-loop.md
co-update; and the Current work日志.md frontier-log entry. The Notion
mirror is post-merge only, never a pull-request input.

## 14. Explicit OUT_OF_SCOPE list

The following are registered as not decided by this contract:

- **OUT_OF_SCOPE_N2_N4_CLOSURE_CROSSCHECK** (physics cross-check, not
  notation): the \(N=2\leftrightarrow N=4\) closure-sign cross-check,
  (4B.43)–(4B.46) versus (4C.37)–(4C.38a). Recorded as an open physics
  item, not a notation item.
- **OUT_OF_SCOPE_WEINBERG_GAUGINO_PHASE** (source gap): the
  Weinberg-side gaugino phase, SOURCE_INSUFFICIENT per (D4.4).
- **OUT_OF_SCOPE_DRED_MOMENTUM_LEDGER_LOR_CYCLE** (blocked ledger):
  the momentum-space DRED ledger and the Lorentzian cycle, BLOCKED per
  (5A.80).
- **OUT_OF_SCOPE_NK_BRANCH_TABLE** (branch table): the NK branch table
  (3D.95b); the BV–NK row is admissible only after (3D.96b) holds.
