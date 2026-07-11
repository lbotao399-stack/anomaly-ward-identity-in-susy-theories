# 00 3+1d SUSY QFT — Convention Lock

## Step 2A. Flat superspace and covariant derivatives

### 2A.1 Superspace coordinates and left Grassmann calculus

$$
z_L^M=(x_L^\mu,\vartheta^a,\bar\vartheta_{\dot a}),
\qquad
z_E^M=(x_E^m,\vartheta^a,\bar\vartheta_{\dot a}).
\tag{2A.1}
$$

The transformation parameters in Step 1 and the superspace coordinates are distinct:

$$
(\varepsilon^a,\bar\varepsilon_{\dot a})
\ne
(\vartheta^a,\bar\vartheta_{\dot a}).
\tag{2A.2}
$$

$$
\bar\vartheta^{\dot a}:=
\epsilon^{\dot a\dot b}\bar\vartheta_{\dot b},
\qquad
\vartheta\sigma_R^M\bar\vartheta
:=
\vartheta^a(\sigma_R^M)_{a\dot b}\bar\vartheta^{\dot b}.
\tag{2A.3}
$$

$$
\partial_a:=\frac{\vec\partial}{\partial\vartheta^a},
\qquad
\bar\partial^{\dot a}:=
\frac{\vec\partial}{\partial\bar\vartheta_{\dot a}},
\qquad
\bar\partial_{\dot a}:=
\epsilon_{\dot a\dot b}\bar\partial^{\dot b}.
\tag{2A.4}
$$

For an odd left derivative \(\partial_\zeta\),

$$
\partial_\zeta(FG)
=
(\partial_\zeta F)G
+(-1)^{|F|}F(\partial_\zeta G).
\tag{2A.5}
$$

$$
\begin{gathered}
\{\partial_a,\vartheta^b\}=\delta_a{}^b,
\qquad
\{\bar\partial^{\dot a},\bar\vartheta_{\dot b}\}
=\delta^{\dot a}{}_{\dot b},\\
\{\bar\partial_{\dot a},\bar\vartheta^{\dot b}\}
=-\delta_{\dot a}{}^{\dot b},
\qquad
\{\partial_a,\bar\vartheta_{\dot b}\}
=\{\bar\partial^{\dot a},\vartheta^b\}=0.
\end{gathered}
\tag{2A.6}
$$

Let

$$
B_R^M:=\vartheta\sigma_R^M\bar\vartheta.
\tag{2A.7}
$$

Then

$$
\partial_aB_R^M
=(\sigma_R^M)_{a\dot b}\bar\vartheta^{\dot b},
\qquad
\bar\partial_{\dot a}B_R^M
=+\vartheta^b(\sigma_R^M)_{b\dot a}.
\tag{2A.8}
$$

### 2A.2 Noether charges and active fixed-coordinate action

For every Noether generator \(G_A^R\),

$$
G_A^R
:=
\int_{\Sigma_R}d\Sigma_\mu\,j_A^{R\mu},
\qquad
\delta_\varepsilon S_R
=
\int_{\partial M_R}d\Sigma_\mu\,
j_A^{R\mu}\varepsilon^A.
\tag{2A.9}
$$

The parameter order in (2A.9) is fixed as \(j_A^{R\mu}\varepsilon^A\).
The active field action is

$$
\Phi_R'(z_R):=U_R^{-1}\Phi_R(z_R)U_R.
\tag{2A.10}
$$

Lorentzian translations give

$$
\begin{aligned}
U_L&=1-i a_L^\mu P^L_\mu,\\
\delta_a\Phi_L
&=i a_L^\mu[P^L_\mu,\Phi_L]
=-a_L^\mu\partial_\mu^L\Phi_L,
\end{aligned}
\tag{2A.11}
$$

therefore

$$
[P^L_\mu,\Phi_L]=i\partial_\mu^L\Phi_L.
\tag{2A.12}
$$

Euclidean translations give

$$
\begin{aligned}
U_E&=1+a_E^mP^E_m,\\
\delta_a\Phi_E
&=-a_E^m[P^E_m,\Phi_E]
=-a_E^m\partial_m^E\Phi_E,
\end{aligned}
\tag{2A.13}
$$

therefore

$$
[P^E_m,\Phi_E]=\partial_m^E\Phi_E.
\tag{2A.14}
$$

### 2A.3 Coordinate and Noether representations

For homogeneous operators, the graded tensor product is

$$
(A\widehat\otimes B)(C\widehat\otimes D)
:=
(-1)^{|B||C|}AC\widehat\otimes BD.
\tag{2A.15}
$$

For the multiplication operator \(M_{\Phi_R}\),

$$
[\partial_M,M_{\Phi_R}\}
=M_{\partial_M\Phi_R}.
\tag{2A.15a}
$$

The coordinate realization of a Step-1 Noether charge is denoted by a sans-serif letter.  Diagonal covariance is

$$
\begin{aligned}
\mathbb P_M^R
&:=\mathsf P_M^R\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes P_M^R,\\
\mathbb Q_a^R
&:=\mathsf Q_a^R\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes Q_a^R,\\
\bar{\mathbb Q}_{\dot a}^R
&:=\bar{\mathsf Q}_{\dot a}^R\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes\bar Q_{\dot a}^R,
\end{aligned}
\tag{2A.16}
$$

$$
[\mathbb P_M^R,\Phi_R]=0,
\qquad
[\mathbb Q_a^R,\Phi_R\}=0,
\qquad
[\bar{\mathbb Q}_{\dot a}^R,\Phi_R\}=0.
\tag{2A.17}
$$

At \(\vartheta=\bar\vartheta=0\), (2A.17) gives

$$
\begin{array}{c|cc}
R&\mathsf P_M^R\Phi_R&[P_M^R,\Phi_R]\\ \hline
L&-i\partial_\mu^L\Phi_L&+i\partial_\mu^L\Phi_L\\
E&-\partial_m^E\Phi_E&+\partial_m^E\Phi_E
\end{array}
\tag{2A.18}
$$

and

$$
\begin{array}{c|cc}
R&\mathsf Q_a^R\Phi_R&[Q_a^R,\Phi_R\}\\ \hline
L&-i\partial_a\Phi_L&+i\partial_a\Phi_L\\
E&-\partial_a\Phi_E&+\partial_a\Phi_E.
\end{array}
\tag{2A.19}
$$

### 2A.4 Lorentzian flat superspace

$$
\boxed{\mathsf P^L_\mu=-i\partial_\mu^L.}
\tag{2A.20}
$$

The symmetric supertranslation section is

$$
g_L(z_L):=e^{X_L(z_L)},
\qquad
X_L(z_L):=
-ix_L^\mu P_\mu^L
-i\vartheta^aQ_a^L
-i\bar\vartheta_{\dot a}\bar Q_L^{\dot a}
.
\tag{2A.20a}
$$

The Step-1 anticommutator terminates the BCH series:

$$
\begin{aligned}
[X_L(\varepsilon,\bar\varepsilon),X_L(z_L)]
={}&[-i\varepsilon^aQ_a^L,
-i\bar\vartheta_{\dot b}\bar Q_L^{\dot b}]\\
&+[-i\bar\varepsilon_{\dot b}\bar Q_L^{\dot b},
-i\vartheta^aQ_a^L]\\
={}&2\left(
\varepsilon\sigma_L^\mu\bar\vartheta
-\vartheta\sigma_L^\mu\bar\varepsilon
\right)P_\mu^L,\\
X_L(z_L')
={}&X_L(\varepsilon,\bar\varepsilon)+X_L(z_L)
+\frac12[X_L(\varepsilon,\bar\varepsilon),X_L(z_L)].
\end{aligned}
\tag{2A.20b}
$$

$$
\begin{aligned}
g_L(\varepsilon,\bar\varepsilon)g_L(z_L)
&=g_L(z_L'),\\
\vartheta'^a
&=\vartheta^a+\varepsilon^a,\\
\bar\vartheta'_{\dot a}
&=\bar\vartheta_{\dot a}+\bar\varepsilon_{\dot a},\\
x_L^{\prime\mu}
&=x_L^\mu
+i\varepsilon^a(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
-i\vartheta^a(\sigma_L^\mu)_{a\dot b}\bar\varepsilon^{\dot b}.
\end{aligned}
\tag{2A.20c}
$$

The inverse pullback is

$$
\begin{aligned}
\delta\Phi_L
={}&-\varepsilon^a\partial_a\Phi_L
-\bar\varepsilon_{\dot a}\bar\partial^{\dot a}\Phi_L\\
&-i\varepsilon^a(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\partial_\mu^L\Phi_L
+i\vartheta^a(\sigma_L^\mu)_{a\dot b}\bar\varepsilon^{\dot b}
\partial_\mu^L\Phi_L.
\end{aligned}
\tag{2A.20d}
$$

Equations (2A.3)--(2A.6) lower the barred generator.  Equation (2A.20d) fixes

$$
\boxed{
\begin{aligned}
\mathsf Q^L_a
&=-i\partial_a
+(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}\partial_\mu^L,\\
\bar{\mathsf Q}^L_{\dot a}
&=-i\bar\partial_{\dot a}
-\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu^L.
\end{aligned}}
\tag{2A.21}
$$

For

$$
X_a=A\partial_a
+B(\sigma_L^\mu)_{a\dot c}\bar\vartheta^{\dot c}\partial_\mu^L,
\qquad
\bar X_{\dot b}=C\bar\partial_{\dot b}
+D\vartheta^c(\sigma_L^\mu)_{c\dot b}\partial_\mu^L,
\tag{2A.22}
$$

(2A.6) gives

$$
\{X_a,\bar X_{\dot b}\}
=(AD-BC)(\sigma_L^\mu)_{a\dot b}\partial_\mu^L.
\tag{2A.23}
$$

For (2A.21),

$$
A=-i,
\qquad B=1,
\qquad C=-i,
\qquad D=-1,
\qquad AD-BC=2i.
\tag{2A.24}
$$

Thus

$$
\boxed{
\{\mathsf Q_a^L,\bar{\mathsf Q}_{\dot b}^L\}
=2i(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=-2(\sigma_L^\mu)_{a\dot b}\mathsf P_\mu^L.}
\tag{2A.25}
$$

$$
\begin{gathered}
\{\mathsf Q_a^L,\mathsf Q_b^L\}=0,
\qquad
\{\bar{\mathsf Q}_{\dot a}^L,\bar{\mathsf Q}_{\dot b}^L\}=0,\\
[\mathsf P_\mu^L,\mathsf Q_a^L]=0,
\qquad
[\mathsf P_\mu^L,\bar{\mathsf Q}_{\dot a}^L]=0.
\end{gathered}
\tag{2A.26}
$$

### 2A.5 Lorentzian flat covariant derivatives

The conditions

$$
\begin{gathered}
\{D_a^L,\mathsf Q_b^L\}
=\{D_a^L,\bar{\mathsf Q}_{\dot b}^L\}=0,\\
\{\bar D_{\dot a}^L,\mathsf Q_b^L\}
=\{\bar D_{\dot a}^L,\bar{\mathsf Q}_{\dot b}^L\}=0
\end{gathered}
\tag{2A.27}
$$

fix

$$
\boxed{
\begin{aligned}
D_a^L
&=\partial_a
-i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}\partial_\mu^L,\\
\bar D_{\dot a}^L
&=\bar\partial_{\dot a}
+i\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu^L.
\end{aligned}}
\tag{2A.28}
$$

$$
\boxed{
\{D_a^L,\bar D_{\dot b}^L\}
=+2i(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=-2(\sigma_L^\mu)_{a\dot b}\mathsf P_\mu^L.}
\tag{2A.29}
$$

$$
\begin{gathered}
\{D_a^L,D_b^L\}=0,
\qquad
\{\bar D_{\dot a}^L,\bar D_{\dot b}^L\}=0,\\
[\mathsf P_\mu^L,D_a^L]=0,
\qquad
[\mathsf P_\mu^L,\bar D_{\dot a}^L]=0,
\end{gathered}
\tag{2A.30}
$$

and all four mixed \(\mathsf Q\)-\(D\) anticommutators vanish.  The symbol \(\nabla\) is reserved for gauge-covariant superspace derivatives.

Define

$$
y_L^\mu:=x_L^\mu-iB_L^\mu,
\qquad
\bar y_L^\mu:=x_L^\mu+iB_L^\mu.
\tag{2A.31}
$$

Then

$$
\begin{aligned}
\bar D_{\dot a}^Ly_L^\mu
&=
i\vartheta^b(\sigma_L^\mu)_{b\dot a}
+\bar\partial_{\dot a}(-iB_L^\mu)\\
&=
i\vartheta^b(\sigma_L^\mu)_{b\dot a}
-i\vartheta^b(\sigma_L^\mu)_{b\dot a}=0,
\end{aligned}
\tag{2A.32}
$$

$$
\begin{aligned}
D_a^L\bar y_L^\mu
&=
-i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
+\partial_a(+iB_L^\mu)\\
&=
-i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
+i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}=0.
\end{aligned}
\tag{2A.33}
$$

### 2A.6 Lorentzian adjoints

The physical Hilbert-space adjoint is

$$
(P_\mu^L)^{\dagger_{\mathcal H}}=P_\mu^L,
\qquad
(Q_a^L)^{\dagger_{\mathcal H}}=\bar Q_{\dot a}^L.
\tag{2A.34}
$$

The coordinate formal adjoint is fixed by

$$
\begin{gathered}
(x_L^\mu)^{\ddagger_L}=x_L^\mu,
\qquad
(\partial_\mu^L)^{\ddagger_L}=-\partial_\mu^L,\\
(\vartheta^a)^{\ddagger_L}=\bar\vartheta^{\dot a},
\qquad
(\partial_a)^{\ddagger_L}=-\bar\partial_{\dot a},
\qquad
(AB)^{\ddagger_L}=B^{\ddagger_L}A^{\ddagger_L}.
\end{gathered}
\tag{2A.35}
$$

Consequently,

$$
(\mathsf P_\mu^L)^{\ddagger_L}=\mathsf P_\mu^L,
\qquad
(\mathsf Q_a^L)^{\ddagger_L}=\bar{\mathsf Q}_{\dot a}^L,
\qquad
(D_a^L)^{\ddagger_L}=-\bar D_{\dot a}^L,
\qquad
(y_L^\mu)^{\ddagger_L}=\bar y_L^\mu.
\tag{2A.36}
$$

On the bosonic coordinate domain with vanishing boundary term,

$$
\begin{aligned}
\int d^4x\,f^*(-i\partial_\mu g)
&=\int d^4x\,( -i\partial_\mu f)^*g,\\
(\mathsf P_\mu^L)^{\dagger_{L^2_x}}
&=\mathsf P_\mu^L.
\end{aligned}
\tag{2A.37}
$$

The three symbols \(\dagger_{\mathcal H}\), \(\ddagger_L\), and \(\dagger_{L^2_x}\) are not identified.

### 2A.7 Euclidean continuation

The coordinate derivatives continue as

$$
\partial_i^L=\partial_i^E,
\qquad
\partial_0^L=i\partial_4^E,
\qquad
(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=i(\sigma_E^m)_{a\dot b}\partial_m^E.
\tag{2A.38}
$$

The coordinate realization follows the Step-1 exponent normalization:

$$
\mathsf P_i^E=-i\mathsf P_i^L,
\qquad
\mathsf P_4^E=-\mathsf P_0^L,
\qquad
\boxed{\mathsf P_m^E=-\partial_m^E.}
\tag{2A.39}
$$

$$
\mathsf Q_a^E=-i\mathsf Q_a^L,
\qquad
\bar{\mathsf Q}_{\dot a}^E=-i\bar{\mathsf Q}_{\dot a}^L,
\qquad
D_a^E=\left.D_a^L\right|_{\mathrm{Wick}},
\qquad
\bar D_{\dot a}^E=\left.\bar D_{\dot a}^L\right|_{\mathrm{Wick}}.
\tag{2A.40}
$$

Therefore

$$
\boxed{
\begin{aligned}
\mathsf Q_a^E
&=-\partial_a
+(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b}\partial_m^E,\\
\bar{\mathsf Q}_{\dot a}^E
&=-\bar\partial_{\dot a}
-\vartheta^b(\sigma_E^m)_{b\dot a}\partial_m^E,\\
D_a^E
&=\partial_a
+(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b}\partial_m^E,\\
\bar D_{\dot a}^E
&=\bar\partial_{\dot a}
-\vartheta^b(\sigma_E^m)_{b\dot a}\partial_m^E.
\end{aligned}}
\tag{2A.41}
$$

$$
\boxed{
\begin{aligned}
\{\mathsf Q_a^E,\bar{\mathsf Q}_{\dot b}^E\}
&=+2(\sigma_E^m)_{a\dot b}\partial_m^E
=-2(\sigma_E^m)_{a\dot b}\mathsf P_m^E,\\
\{D_a^E,\bar D_{\dot b}^E\}
&=-2(\sigma_E^m)_{a\dot b}\partial_m^E
=+2(\sigma_E^m)_{a\dot b}\mathsf P_m^E.
\end{aligned}}
\tag{2A.42}
$$

$$
\begin{gathered}
\{\mathsf Q_a^E,\mathsf Q_b^E\}
=\{\bar{\mathsf Q}_{\dot a}^E,\bar{\mathsf Q}_{\dot b}^E\}=0,\\
\{D_a^E,D_b^E\}
=\{\bar D_{\dot a}^E,\bar D_{\dot b}^E\}=0,
\end{gathered}
\tag{2A.43}
$$

all four mixed \(\mathsf Q^E\)-\(D^E\) anticommutators vanish, and every Euclidean operator in (2A.41) commutes with \(\mathsf P_m^E\).

Define

$$
y_E^m:=x_E^m+B_E^m,
\qquad
\bar y_E^m:=x_E^m-B_E^m.
\tag{2A.44}
$$

Then

$$
\begin{aligned}
\bar D_{\dot a}^Ey_E^m
&=
\bar\partial_{\dot a}B_E^m
-\vartheta^b(\sigma_E^m)_{b\dot a}=0,\\
D_a^E\bar y_E^m
&=
(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b}
-\partial_aB_E^m=0.
\end{aligned}
\tag{2A.45}
$$

The Wick map gives

$$
y_E^i=y_L^i,
\qquad
y_E^4=i y_L^0,
\qquad
\bar y_E^i=\bar y_L^i,
\qquad
\bar y_E^4=i\bar y_L^0.
\tag{2A.46}
$$

### 2A.8 Euclidean Hermitian coordinate basis and reality

The exponent-normalized coordinate generator and the Hermitian coordinate momentum are distinct:

$$
\boxed{
\mathsf P_m^E=-\partial_m^E,
\qquad
\pi_m^E:=i\mathsf P_m^E=-i\partial_m^E.}
\tag{2A.47}
$$

Define the matching normalized Noether charges

$$
\Pi_m^E:=iP_m^E,
\qquad
\mathcal Q_a^E:=iQ_a^E,
\qquad
\bar{\mathcal Q}_{\dot a}^E:=i\bar Q_{\dot a}^E.
\tag{2A.48}
$$

Multiplication of (2A.17) by \(i\) gives

$$
[\pi_m^E\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes\Pi_m^E,\Phi_E]=0,
\tag{2A.49}
$$

$$
[i\mathsf Q_a^E\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes\mathcal Q_a^E,\Phi_E\}=0,
\qquad
[i\bar{\mathsf Q}_{\dot a}^E\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes\bar{\mathcal Q}_{\dot a}^E,\Phi_E\}=0.
\tag{2A.50}
$$

$$
\begin{aligned}
\{i\mathsf Q_a^E,i\bar{\mathsf Q}_{\dot b}^E\}
&=-2i(\sigma_E^m)_{a\dot b}\pi_m^E,\\
\{\mathcal Q_a^E,\bar{\mathcal Q}_{\dot b}^E\}
&=-2i(\sigma_E^m)_{a\dot b}\Pi_m^E.
\end{aligned}
\tag{2A.50a}
$$

On \(L^2(\mathbb R^4)\),

$$
(\mathsf P_m^E)^{\dagger_{L^2_x}}=-\mathsf P_m^E,
\qquad
(\pi_m^E)^{\dagger_{L^2_x}}=\pi_m^E.
\tag{2A.51}
$$

Wick transport of the Lorentzian Hilbert adjoint gives

$$
\begin{gathered}
(P_i^E)^{\dagger_W}=-P_i^E,
\qquad
(P_4^E)^{\dagger_W}=P_4^E,\\
(\Pi_i^E)^{\dagger_W}=\Pi_i^E,
\qquad
(\Pi_4^E)^{\dagger_W}=-\Pi_4^E,\\
(Q_a^E)^{\dagger_W}=-\bar Q_{\dot a}^E,
\qquad
(\mathcal Q_a^E)^{\dagger_W}=\bar{\mathcal Q}_{\dot a}^E.
\end{gathered}
\tag{2A.52}
$$

Intrinsic Euclidean superspace imposes no relation between \(Q_a^E\) and \(\bar Q_{\dot a}^E\), and no relation between \(\mathsf Q_a^E\) and \(\bar{\mathsf Q}_{\dot a}^E\).  The operation \(\dagger_W\) in (2A.52) is not an intrinsic Euclidean Hilbert adjoint.

### 2A.9 Locked result surface

$$
\begin{array}{c|cc}
&L&E\\ \hline
\mathsf P&-i\partial_\mu&-\partial_m\\
\{\mathsf Q,\bar{\mathsf Q}\}&-2\sigma_L^\mu\mathsf P_\mu&-2\sigma_E^m\mathsf P_m\\
\{D,\bar D\}&-2\sigma_L^\mu\mathsf P_\mu&+2\sigma_E^m\mathsf P_m\\
y&x-i\vartheta\sigma_L\bar\vartheta&x+\vartheta\sigma_E\bar\vartheta\\
\bar y&x+i\vartheta\sigma_L\bar\vartheta&x-\vartheta\sigma_E\bar\vartheta
\end{array}
\tag{2A.53}
$$

Structural source checks are restricted to the registered claims
`FLAT-SUPERSPACE-GROUP-STRUCTURE` and `CHIRAL-SUBSPACE-STRUCTURE`; every sign and factor in (2A.1)--(2A.53) is derived from Step 1.
