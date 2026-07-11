# 00 3+1d SUSY QFT — Convention Lock

## Step 2B. Superconformal superspace

### 2B.1 New symbols

The spinor derivatives remain \(D_a,\bar D_{\dot a}\).  Dilatation generators carry the label \({\rm dil}\):

$$
D_{{\rm dil},L},
\qquad
\mathsf D_{{\rm dil},L},
\qquad
D_{{\rm dil},E},
\qquad
\mathsf D_{{\rm dil},E}.
\tag{2B.1}
$$

$$
\begin{gathered}
E_x:=x^\mu\partial_\mu,
\qquad
E_y:=y^\mu\partial_\mu^y,\\
N_\vartheta:=\vartheta^a\partial_a,
\qquad
N_{\bar\vartheta}:=
\bar\vartheta_{\dot a}\bar\partial^{\dot a}.
\end{gathered}
\tag{2B.2}
$$

The Lorentzian active element is fixed as

$$
\begin{aligned}
U_L\big|_{\rm sc}
:={}&1+\frac i2\omega_{\mu\nu}J_L^{\mu\nu}
-ia^\mu P_\mu^L-i\lambda D_{{\rm dil},L}-i\rho R_L\\
&-ib^\mu K_\mu^L-i\zeta^aS_a^L
-i\bar\zeta_{\dot a}\bar S_L^{\dot a}.
\end{aligned}
\tag{2B.3}
$$

For each generator \(G_A^L\),

$$
G_A^L=\int_{\Sigma_L}d\Sigma_\mu\,j_A^{L\mu},
\qquad
\delta_\epsilon S_L
=\int_{\partial M_L}d\Sigma_\mu\,j_A^{L\mu}\epsilon^A.
\tag{2B.4}
$$

Coordinate--Noether covariance is

$$
\mathbb G_A^L
:=\mathsf G_A^L\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes G_A^L,
\qquad
[\mathbb G_A^L,M_{\Phi_L}\}=0.
\tag{2B.5}
$$

### 2B.2 Lorentzian inversion and bosonic \(K\)

$$
\mathcal U_L:=\{x\in\mathbb R^{1,3}:x^2\ne0\},
\qquad
x^2:=\eta_{\mu\nu}x^\mu x^\nu.
\tag{2B.6}
$$

$$
I_L(x)^\mu:=\frac{x^\mu}{x^2},
\qquad
I_L^2=\operatorname{id}_{\mathcal U_L},
\qquad
(I_Lx)^2=\frac1{x^2}.
\tag{2B.7}
$$

$$
\frac{\partial I_L(x)^\mu}{\partial x^\nu}
=\frac1{x^2}
\left(
\delta^\mu{}_\nu-\frac{2x^\mu x_\nu}{x^2}
\right).
\tag{2B.8}
$$

For a scalar coordinate module of real weight \(\Delta\),

$$
(\mathcal I_{L,\Delta}f)(x)
:=|x^2|^{-\Delta}f(I_Lx),
\qquad
\mathcal I_{L,\Delta}^2=1.
\tag{2B.9}
$$

Direct differentiation gives

$$
\begin{aligned}
\mathcal I_{L,\Delta}\partial_\mu\mathcal I_{L,\Delta}
&=x^2\partial_\mu-2x_\mu(E_x+\Delta),\\
\mathsf P_\mu^L&=-i\partial_\mu,\\
\mathsf D_{{\rm dil},L}^{(\Delta)}&=-i(E_x+\Delta),\\
\mathsf J_{\mu\nu}^L&=-i(x_\mu\partial_\nu-x_\nu\partial_\mu),\\
\mathsf K_\mu^{L,(\Delta)}
&:=\mathcal I_{L,\Delta}\mathsf P_\mu^L\mathcal I_{L,\Delta}\\
&=-i\left[x^2\partial_\mu-2x_\mu(E_x+\Delta)\right].
\end{aligned}
\tag{2B.10}
$$

$$
I_LT_bI_L(x)^\mu
=\frac{x^\mu+b^\mu x^2}
{1+2b\cdot x+b^2x^2}.
\tag{2B.11}
$$

$$
\delta_bx^\mu=b^\mu x^2-2(b\cdot x)x^\mu,
\tag{2B.12}
$$

$$
\delta_bf
=-b^\mu\left[x^2\partial_\mu-2x_\mu(E_x+\Delta)\right]f
=-ib^\mu\mathsf K_\mu^{L,(\Delta)}f.
\tag{2B.13}
$$

The direct commutators are

$$
\boxed{
\begin{aligned}
[\mathsf D_{{\rm dil},L},\mathsf P_\mu^L]
&=i\mathsf P_\mu^L,\\
[\mathsf D_{{\rm dil},L},\mathsf K_\mu^L]
&=-i\mathsf K_\mu^L,\\
[\mathsf P_\mu^L,\mathsf K_\nu^L]
&=2i\left(
\eta_{\mu\nu}\mathsf D_{{\rm dil},L}
-\mathsf J_{\mu\nu}^L
\right),\\
[\mathsf K_\mu^L,\mathsf K_\nu^L]&=0.
\end{aligned}}
\tag{2B.14}
$$

$$
[\mathsf J_{\mu\nu}^L,\mathsf K_\rho^L]
=i\eta_{\mu\rho}\mathsf K_\nu^L
-i\eta_{\nu\rho}\mathsf K_\mu^L.
\tag{2B.15}
$$

### 2B.3 Full superspace dilatation, \(R\), and Lorentz generators

Begin with

$$
\mathsf D_{{\rm dil},L}
=-i(E_x+wN_\vartheta+\bar wN_{\bar\vartheta}).
\tag{2B.16}
$$

Homogeneity of the two terms in \(\mathsf Q_a^L\) gives

$$
-w=\bar w-1.
\tag{2B.17}
$$

Lorentzian conjugation gives \(w=\bar w\); hence

$$
w=\bar w=\frac12,
\qquad
\boxed{
\mathsf D_{{\rm dil},L}
=-i\left(E_x+\frac12N_\vartheta+\frac12N_{\bar\vartheta}\right).}
\tag{2B.18}
$$

For

$$
\mathsf R_L=rN_\vartheta+\bar rN_{\bar\vartheta},
\tag{2B.19}
$$

homogeneity of \(\mathsf Q_a^L\) gives \(\bar r=-r\).  The primitive normalization \(\mathsf R_L\vartheta^a=\vartheta^a\) fixes

$$
\boxed{\mathsf R_L=N_\vartheta-N_{\bar\vartheta}.}
\tag{2B.20}
$$

Define

$$
\widetilde{\bar\partial}_{\dot a}
:=\frac{\vec\partial}{\partial\bar\vartheta^{\dot a}}
=-\bar\partial_{\dot a}.
\tag{2B.21}
$$

Then

$$
\boxed{
\begin{aligned}
\mathsf J_{\mu\nu}^{L,{\rm ss}}
={}&-i(x_\mu\partial_\nu-x_\nu\partial_\mu)
+i\vartheta^c(\sigma_{L,\mu\nu})_c{}^d\partial_d\\
&-i(\bar\sigma_{L,\mu\nu})^{\dot c}{}_{\dot d}
\bar\vartheta^{\dot d}\widetilde{\bar\partial}_{\dot c}.
\end{aligned}}
\tag{2B.22}
$$

$$
\begin{gathered}
[\mathsf D_{{\rm dil},L},\mathsf Q_a^L]
=\frac i2\mathsf Q_a^L,
\qquad
[\mathsf D_{{\rm dil},L},\bar{\mathsf Q}_{\dot a}^L]
=\frac i2\bar{\mathsf Q}_{\dot a}^L,\\
[\mathsf R_L,\mathsf Q_a^L]=-\mathsf Q_a^L,
\qquad
[\mathsf R_L,\bar{\mathsf Q}_{\dot a}^L]
=+\bar{\mathsf Q}_{\dot a}^L.
\end{gathered}
\tag{2B.23}
$$

### 2B.4 Lorentzian chiral chart

$$
y^\mu:=x^\mu-i\vartheta\sigma_L^\mu\bar\vartheta,
\qquad
\bar D_{\dot a}^Ly^\mu=0.
\tag{2B.24}
$$

On \(F(y,\vartheta)\),

$$
\left.\partial_a\right|_x
=\left.\partial_a\right|_y
-i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}\partial_\mu^y,
\qquad
\left.\bar\partial_{\dot a}\right|_xF
=-i\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu^yF.
\tag{2B.25}
$$

Therefore

$$
\boxed{
\mathsf P_\mu^L=-i\partial_\mu^y,
\qquad
\mathsf Q_a^L=-i\partial_a,
\qquad
\bar{\mathsf Q}_{\dot a}^L
=-2\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu^y.}
\tag{2B.26}
$$

$$
\begin{gathered}
Y_{a\dot a}:=y_\mu(\sigma_L^\mu)_{a\dot a},
\qquad
\widetilde Y^{\dot a a}:=y_\mu(\bar\sigma_L^\mu)^{\dot a a},\\
Y\widetilde Y=-y^2\mathbf1_2,
\qquad
Y^{-1}=-\frac{\widetilde Y}{y^2}.
\end{gathered}
\tag{2B.27}
$$

$$
\mathsf D_{{\rm dil},L}
=-i\left(E_y+\frac12N_\vartheta\right),
\qquad
\mathsf R_L=N_\vartheta,
\tag{2B.28}
$$

$$
\mathsf J_{\mu\nu}^L
=-i(y_\mu\partial_\nu^y-y_\nu\partial_\mu^y)
+i\vartheta^a(\sigma_{L,\mu\nu})_a{}^b\partial_b.
\tag{2B.29}
$$

### 2B.5 Superinversion and its phase

Let \(\bar Y_{a\dot a}:=\bar y_\mu(\sigma_L^\mu)_{a\dot a}\).  The matrix contractions are defined by

$$
(\widetilde{\bar\vartheta}\,\bar Y^{-1})^a
:=\bar\vartheta_{\dot b}(\bar Y^{-1})^{\dot b a},
\tag{2B.30}
$$

$$
(Y^{-1}\widetilde\vartheta)_{\dot a}
:=\epsilon_{\dot a\dot b}(Y^{-1})^{\dot b c}\vartheta_c.
\tag{2B.31}
$$

$$
\mathcal U_{s,L}:=
\left\{
\begin{array}{c|c}
(x,\vartheta,\bar\vartheta)&
x\in\mathbb R^{1,3},\quad
y^\mu=x^\mu-i\vartheta\sigma_L^\mu\bar\vartheta,\quad
\bar y^\mu=x^\mu+i\vartheta\sigma_L^\mu\bar\vartheta,\\
&\operatorname{body}(y^2)\ne0,\quad
\operatorname{body}(\bar y^2)\ne0
\end{array}
\right\}.
\tag{2B.31a}
$$

$$
\begin{aligned}
(\sigma_L^\mu)_{b\dot b}(\sigma_{L,\mu})_{a\dot a}
&=-2\epsilon_{ba}\epsilon_{\dot b\dot a},\\
(\vartheta\sigma_L^\mu\bar\vartheta)
(\sigma_{L,\mu})_{a\dot a}
&=-2\vartheta_a\bar\vartheta_{\dot a},\\
\bar y^\mu-y^\mu
&=2i\vartheta\sigma_L^\mu\bar\vartheta,\\
\bar Y_{a\dot a}-Y_{a\dot a}
&=-4i\vartheta_a\bar\vartheta_{\dot a}.
\end{aligned}
\tag{2B.31b}
$$

Fix the Lorentzian superinversion \(\mathcal I_{s,L}\) by

$$
\boxed{
\begin{aligned}
\widetilde Y'&=-\bar Y^{-1},
&\qquad
\vartheta'{}^a&=-i(\widetilde{\bar\vartheta}\,\bar Y^{-1})^a,\\
\widetilde{\bar Y}'&=-Y^{-1},
&
\bar\vartheta'_{\dot a}&=+i(Y^{-1}\widetilde\vartheta)_{\dot a}.
\end{aligned}}
\tag{2B.32}
$$

Equivalently,

$$
y'{}^\mu=\frac{\bar y^\mu}{\bar y^2},
\qquad
\bar y'{}^\mu=\frac{y^\mu}{y^2}.
\tag{2B.33}
$$

Raising the dotted index in (2B.32) gives

$$
\bar\vartheta'{}^{\dot a}
=+i(Y^{-1})^{\dot a b}\vartheta_b.
\tag{2B.33a}
$$

The superspace constraint is preserved:

$$
\begin{aligned}
-4i\vartheta'_a\bar\vartheta'_{\dot a}
&=-4i(-i)(+i)\epsilon_{ab}\epsilon_{\dot a\dot b}
\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c b}
(Y^{-1})^{\dot b d}\vartheta_d\\
&=+4i\epsilon_{ab}\epsilon_{\dot a\dot b}
(Y^{-1})^{\dot b d}\vartheta_d\bar\vartheta_{\dot c}
(\bar Y^{-1})^{\dot c b}\\
&=\epsilon_{ab}\epsilon_{\dot a\dot b}
(Y^{-1})^{\dot b d}(Y-\bar Y)_{d\dot c}
(\bar Y^{-1})^{\dot c b}\\
&=\epsilon_{ab}\epsilon_{\dot a\dot b}
\left[(\bar Y^{-1})^{\dot b b}-(Y^{-1})^{\dot b b}\right]\\
&=\bar Y'_{a\dot a}-Y'_{a\dot a}.
\end{aligned}
\tag{2B.33b}
$$

Therefore

$$
(\bar y'-y')_\mu(\sigma_L^\mu)_{a\dot a}
=-4i\vartheta'_a\bar\vartheta'_{\dot a}
=2i(\vartheta'\sigma_L^\mu\bar\vartheta')
(\sigma_{L,\mu})_{a\dot a},
\qquad
\boxed{\bar y'{}^\mu-y'{}^\mu
=2i\vartheta'\sigma_L^\mu\bar\vartheta'.}
\tag{2B.33c}
$$

The second application uses

$$
\bar Y'=\frac{Y}{y^2},
\qquad
\bar Y'^{-1}=y^2Y^{-1}=-\widetilde Y,
\qquad
Y'=\frac{\bar Y}{\bar y^2},
\qquad
Y'^{-1}=\bar y^2\bar Y^{-1}=-\widetilde{\bar Y}.
\tag{2B.34}
$$

$$
\begin{aligned}
\vartheta''{}^a
&=-i\bar\vartheta'_{\dot b}(\bar Y'^{-1})^{\dot b a}\\
&=(-i)(+i)\epsilon_{\dot b\dot c}
(Y^{-1})^{\dot c d}\vartheta_d
(-\widetilde Y)^{\dot b a}\\
&=-\epsilon_{\dot b\dot c}(Y^{-1})^{\dot c d}
\widetilde Y^{\dot b a}\vartheta_d\\
&=\epsilon^{ad}\vartheta_d
=\vartheta^a,
\end{aligned}
\tag{2B.34a}
$$

where

$$
\begin{aligned}
Y&=
\begin{pmatrix}
-y^0+y^3&y^1-iy^2\\
y^1+iy^2&-y^0-y^3
\end{pmatrix},\\
\widetilde Y&=
\begin{pmatrix}
-y^0-y^3&-y^1+iy^2\\
-y^1-iy^2&-y^0+y^3
\end{pmatrix},\\
\det Y&=\det\widetilde Y
=(y^0)^2-\sum_{i=1}^{3}(y^i)^2
=-\eta_{\mu\nu}y^\mu y^\nu=-y^2,
\end{aligned}
\tag{2B.34b}
$$

and, for every two-by-two matrix \(A^{\dot a b}\) with even mutually commuting entries,

$$
\epsilon_{\dot b\dot c}A^{\dot c d}A^{\dot b a}
=-(\det A)\epsilon^{ad}.
\tag{2B.34ba}
$$

Hence

$$
\begin{aligned}
-\epsilon_{\dot b\dot c}(Y^{-1})^{\dot c d}
\widetilde Y^{\dot b a}
&=\frac1{y^2}\epsilon_{\dot b\dot c}
\widetilde Y^{\dot c d}\widetilde Y^{\dot b a}\\
&=-\frac{\det\widetilde Y}{y^2}\epsilon^{ad}
=\epsilon^{ad}.
\end{aligned}
\tag{2B.34bb}
$$

$$
\begin{aligned}
\bar\vartheta''_{\dot a}
&=+i\epsilon_{\dot a\dot b}(Y'^{-1})^{\dot b c}\vartheta'_c\\
&=(+i)(-i)\epsilon_{\dot a\dot b}
(-\widetilde{\bar Y})^{\dot b c}\epsilon_{cd}
\bar\vartheta_{\dot e}(\bar Y^{-1})^{\dot e d}\\
&=-\epsilon_{\dot a\dot b}\widetilde{\bar Y}^{\dot b c}
\epsilon_{cd}(\bar Y^{-1})^{\dot e d}\bar\vartheta_{\dot e}\\
&=\delta_{\dot a}{}^{\dot e}\bar\vartheta_{\dot e}
=\bar\vartheta_{\dot a},
\end{aligned}
\tag{2B.34c}
$$

where

$$
\begin{aligned}
-\epsilon_{\dot a\dot b}\widetilde{\bar Y}^{\dot b c}
\epsilon_{cd}(\bar Y^{-1})^{\dot e d}
&=\frac1{\bar y^2}\epsilon_{\dot a\dot b}
\widetilde{\bar Y}^{\dot b c}\epsilon_{cd}
\widetilde{\bar Y}^{\dot e d}\\
&=-\frac{\det\widetilde{\bar Y}}{\bar y^2}
\delta_{\dot a}{}^{\dot e}
=\delta_{\dot a}{}^{\dot e}.
\end{aligned}
\tag{2B.34d}
$$

Thus

$$
\mathcal I_{s,L}^2(y,\bar y,\vartheta,\bar\vartheta)
=(y,\bar y,\vartheta,\bar\vartheta).
\tag{2B.34e}
$$

Let \(\mathscr F_{\rm ch}(\mathcal U_{s,L})\) and
\(\mathscr F_{\rm ach}(\mathcal U_{s,L})\) denote functions of
\((y,\vartheta)\) and \((\bar y,\bar\vartheta)\), respectively.  The weight-zero pullback is

$$
\mathcal I_{s,L}^*:\mathscr F_{\rm ch}\longleftrightarrow
\mathscr F_{\rm ach},
\qquad
(\mathcal I_{s,L}^*F)(z):=F(\mathcal I_{s,L}z),
\qquad
(\mathcal I_{s,L}^*)^{-1}=\mathcal I_{s,L}^*.
\tag{2B.35a}
$$

On the antichiral chart,

$$
\left.\mathsf P_\mu^L\right|_{\rm ach}=-i\partial_\mu^{\bar y},
\qquad
\left.\mathsf Q_a^L\right|_{\rm ach}
=2(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\partial_\mu^{\bar y},
\qquad
\left.\bar{\mathsf Q}_{\dot a}^L\right|_{\rm ach}
=-i\left.\bar\partial_{\dot a}\right|_{\bar y}.
\tag{2B.35b}
$$

In (2B.20),

$$
\left.\mathsf R_L\right|_{\rm ch}=N_\vartheta,
\qquad
\left.\mathsf R_L\right|_{\rm ach}=-N_{\bar\vartheta},
\qquad
\mathcal I_{s,L}^*\mathsf R_L(\mathcal I_{s,L}^*)^{-1}
=-\mathsf R_L.
\tag{2B.35c}
$$

Define the \(\phi=0\) conjugates by

$$
\mathsf K_\mu^L
:=\mathcal I_{s,L}^*\mathsf P_\mu^L\mathcal I_{s,L}^*,
\qquad
\mathsf S_{L,a}
:=\mathcal I_{s,L}^*\mathsf Q_a^L\mathcal I_{s,L}^*,
\qquad
\bar{\mathsf S}_{L,\dot a}
:=\mathcal I_{s,L}^*\bar{\mathsf Q}_{\dot a}^L\mathcal I_{s,L}^*.
\tag{2B.35e}
$$

Equations (2B.23), (2B.35c), and (2B.35e) give

$$
[\mathsf R_L,\mathsf K_\mu^L]=0,
\qquad
[\mathsf R_L,\mathsf S_{L,a}]=+\mathsf S_{L,a},
\qquad
[\mathsf R_L,\bar{\mathsf S}_{L,\dot a}]
=-\bar{\mathsf S}_{L,\dot a}.
\tag{2B.35pa}
$$

For

$$
\phi\in\mathbb R/(2\pi\mathbb Z),
\qquad
\mathcal I_{s,L;\phi}^*
:=e^{-i\phi\mathsf R_L}\mathcal I_{s,L}^*,
\qquad
(\mathcal I_{s,L;\phi}^*)^2
=e^{-i\phi\mathsf R_L}e^{+i\phi\mathsf R_L}=1,
\tag{2B.35}
$$

define

$$
\begin{aligned}
\mathsf K_{\mu;\phi}^L
&:=\mathcal I_{s,L;\phi}^*\mathsf P_\mu^L
(\mathcal I_{s,L;\phi}^*)^{-1},\\
\mathsf S_{L,a;\phi}
&:=\mathcal I_{s,L;\phi}^*\mathsf Q_a^L
(\mathcal I_{s,L;\phi}^*)^{-1},\\
\bar{\mathsf S}_{L,\dot a;\phi}
&:=\mathcal I_{s,L;\phi}^*\bar{\mathsf Q}_{\dot a}^L
(\mathcal I_{s,L;\phi}^*)^{-1}.
\end{aligned}
\tag{2B.35d}
$$

Therefore

$$
\mathsf K_{\mu;\phi}^L=\mathsf K_\mu^L,
\qquad
\mathsf S_{L,a;\phi}=e^{-i\phi}\mathsf S_{L,a},
\qquad
\bar{\mathsf S}_{L,\dot a;\phi}
=e^{+i\phi}\bar{\mathsf S}_{L,\dot a}.
\tag{2B.35p}
$$

Equation (2B.32), hence every formula below, uses \(\phi=0\).

The bosonic derivatives in the first pullback are

$$
\begin{aligned}
\left.
\frac{\partial}{\partial\bar y^\mu}
\frac{\bar y^\nu}{\bar y^2}
\right|_{z\mapsto\mathcal I_{s,L}z}
&=
\left.
\frac{\bar y^2\delta_\mu{}^\nu-2\bar y_\mu\bar y^\nu}
(\bar y^2)^2}
\right|_{\bar y\mapsto y/y^2}\\
&=y^2\delta_\mu{}^\nu-2y_\mu y^\nu,\\
\left.
\frac{\partial}{\partial\bar y^\mu}
\left[-i\bar\vartheta_{\dot c}
(\bar Y^{-1})^{\dot c a}\right]
\right|_{z\mapsto\mathcal I_{s,L}z}
&=\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a.
\end{aligned}
\tag{2B.35f}
$$

The second equality in (2B.35f) is

$$
\begin{aligned}
\frac{\partial}{\partial\bar y^\mu}
\left[-i\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c d}\right]
&=+i\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c b}
(\sigma_{L,\mu})_{b\dot e}(\bar Y^{-1})^{\dot e d},\\
\left.\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c b}
\right|_{z\mapsto\mathcal I_{s,L}z}
&=i\vartheta^b,\\
\left.(\bar Y^{-1})^{\dot e d}
\right|_{z\mapsto\mathcal I_{s,L}z}
&=-\widetilde Y^{\dot e d},\\
\left.
\frac{\partial}{\partial\bar y^\mu}
\left[-i\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c d}\right]
\right|_{z\mapsto\mathcal I_{s,L}z}
&=\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^d.
\end{aligned}
\tag{2B.35fa}
$$

The odd derivative is

$$
\begin{aligned}
-i\bar\partial_{\dot a}
\left[-i\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c b}\right]
&=(-i)(-i)\epsilon_{\dot a\dot c}(\bar Y^{-1})^{\dot c b}\\
&=-\epsilon_{\dot a\dot c}(\bar Y^{-1})^{\dot c b},\\
\left.-\epsilon_{\dot a\dot c}(\bar Y^{-1})^{\dot c b}
\right|_{z\mapsto\mathcal I_{s,L}z}
&=\epsilon_{\dot a\dot c}\widetilde Y^{\dot c b}.
\end{aligned}
\tag{2B.35g}
$$

Use

$$
\operatorname{tr}(\sigma_L^\nu\widetilde Y)
=y_\rho\operatorname{tr}(\sigma_L^\nu\bar\sigma_L^\rho)
=-2y_\rho\eta^{\nu\rho}=-2y^\nu,
\qquad
\epsilon_{ab}\epsilon^{cd}A_c{}^b
=(\operatorname{tr}A)\delta_a{}^d-A_a{}^d.
\tag{2B.35ha}
$$

The first term in \(\mathsf Q_a^L|_{\rm ach}\) gives

$$
\begin{aligned}
&\left.
2(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\frac{\partial}{\partial\bar y^\mu}
\frac{\bar y^\nu}{\bar y^2}
\right|_{z\mapsto\mathcal I_{s,L}z}\\
&\qquad
=2i(\sigma_L^\mu)_{a\dot b}(Y^{-1})^{\dot b c}
\vartheta_c(y^2\delta_\mu{}^\nu-2y_\mu y^\nu)\\
&\qquad
=-\frac{2i}{y^2}(\sigma_L^\mu\widetilde Y)_a{}^c
\vartheta_c(y^2\delta_\mu{}^\nu-2y_\mu y^\nu)\\
&\qquad
=-2i\vartheta_c\left[
(\sigma_L^\nu\widetilde Y)_a{}^c
-\frac{2y^\nu}{y^2}(Y\widetilde Y)_a{}^c
\right]\\
&\qquad
=-2i\vartheta_c\left[
(\sigma_L^\nu\widetilde Y)_a{}^c+2y^\nu\delta_a{}^c
\right]\\
&\qquad
=2i\vartheta_d\epsilon_{ab}\epsilon^{cd}
(\sigma_L^\nu\widetilde Y)_c{}^b\\
&\qquad
=2i\epsilon_{ab}\vartheta^c
(\sigma_L^\nu\widetilde Y)_c{}^b.
\end{aligned}
\tag{2B.35h}
$$

For the second term,

$$
\vartheta_e\vartheta_f=\frac12\epsilon_{ef}\vartheta^2,
\qquad
\vartheta_e\vartheta^c=-\frac12\delta_e{}^c\vartheta^2,
\tag{2B.35ia}
$$

$$
(\sigma_L^\mu)_{a\dot a}(\bar\sigma_L^\rho)^{\dot a b}
(\sigma_{L,\mu})_{b\dot b}
=2(\sigma_L^\rho)_{a\dot b},
\qquad
\sigma_L^\mu\widetilde Y\sigma_{L,\mu}\widetilde Y
=y_\rho\sigma_L^\mu\bar\sigma_L^\rho\sigma_{L,\mu}\widetilde Y
=2Y\widetilde Y=-2y^2\mathbf1_2.
\tag{2B.35ib}
$$

$$
\begin{aligned}
&\left.
2(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\frac{\partial}{\partial\bar y^\mu}
\left[-i\bar\vartheta_{\dot c}(\bar Y^{-1})^{\dot c d}\right]
\right|_{z\mapsto\mathcal I_{s,L}z}\\
&\qquad
=2i(\sigma_L^\mu)_{a\dot b}(Y^{-1})^{\dot b e}
\vartheta_e\vartheta^c(\sigma_{L,\mu}\widetilde Y)_c{}^d\\
&\qquad
=-\frac{2i}{y^2}(\sigma_L^\mu\widetilde Y)_a{}^e
\vartheta_e\vartheta^c(\sigma_{L,\mu}\widetilde Y)_c{}^d\\
&\qquad
=\frac{i\vartheta^2}{y^2}
(\sigma_L^\mu\widetilde Y\sigma_{L,\mu}\widetilde Y)_a{}^d\\
&\qquad
=\frac{i\vartheta^2}{y^2}(-2y^2\delta_a{}^d)\\
&\qquad
=-2i\vartheta^2\delta_a{}^d.
\end{aligned}
\tag{2B.35i}
$$

Therefore

$$
\begin{aligned}
\mathcal I_{s,L}^*\mathsf P_\mu^L\mathcal I_{s,L}^*
&=-i\left[
(y^2\delta_\mu{}^\nu-2y_\mu y^\nu)\partial_\nu^y
+\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a\partial_a
\right],\\
\mathcal I_{s,L}^*\bar{\mathsf Q}_{\dot a}^L\mathcal I_{s,L}^*
&=\epsilon_{\dot a\dot c}\widetilde Y^{\dot c b}\partial_b,\\
\mathcal I_{s,L}^*\mathsf Q_a^L\mathcal I_{s,L}^*
&=2i\epsilon_{ab}\vartheta^c
(\sigma_L^\nu\widetilde Y)_c{}^b\partial_\nu^y
-2i\vartheta^2\partial_a.
\end{aligned}
\tag{2B.35j}
$$

Raising the free spinor indices gives

$$
\begin{array}{c|cc}
&y^\nu&\vartheta^b\\ \hline
\mathsf K_\mu^L
&-i(y^2\delta_\mu{}^\nu-2y_\mu y^\nu)
&-i\vartheta^c(\sigma_{L,\mu}\widetilde Y)_c{}^b\\
\bar{\mathsf S}_L^{\dot a}
&0
&\widetilde Y^{\dot a b}\\
\mathsf S_L^a
&2i\vartheta^c(\sigma_L^\nu\widetilde Y)_c{}^a
&-2i\vartheta^2\epsilon^{ab}
\end{array}
\tag{2B.35k}
$$

### 2B.6 Lorentzian \(K,S,\bar S\) coordinate generators

The chain rule for (2B.32) gives

$$
\boxed{
\mathsf K_\mu^L
=-i\left[
(y^2\delta_\mu{}^\nu-2y_\mu y^\nu)\partial_\nu^y
+\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a\partial_a
\right].}
\tag{2B.36}
$$

$$
\boxed{
\bar{\mathsf S}_L^{\dot a}
=\widetilde Y^{\dot a b}\partial_b,}
\tag{2B.37}
$$

$$
\boxed{
\mathsf S_L^a
=2i\vartheta^b(\sigma_L^\mu\widetilde Y)_b{}^a\partial_\mu^y
-2i\vartheta^2\epsilon^{ab}\partial_b,}
\qquad
\vartheta^2:=\vartheta^a\vartheta_a.
\tag{2B.38}
$$

$$
\mathsf S_{L,a}:=\epsilon_{ab}\mathsf S_L^b,
\qquad
\bar{\mathsf S}_{L,\dot a}
:=\epsilon_{\dot a\dot b}\bar{\mathsf S}_L^{\dot b}.
\tag{2B.39}
$$

The direct reductions use

$$
\sigma_L^\nu\widetilde Y
=-y^\nu\mathbf1_2+2\sigma_L^{\nu\rho}y_\rho,
\qquad
\partial_a\vartheta^2=2\vartheta_a,
\tag{2B.40}
$$

$$
(\sigma_L^{\mu\nu})_a{}^b
(\sigma_{L,\mu\nu})_c{}^d
=-2\delta_a{}^d\delta_c{}^b
+\delta_a{}^b\delta_c{}^d,
\tag{2B.41}
$$

$$
\widetilde Y\sigma_L^\nu\widetilde Y
=-2y^\nu\widetilde Y+y^2\bar\sigma_L^\nu.
\tag{2B.42}
$$

For example,

$$
\begin{aligned}
[\mathsf K_\mu^L,\mathsf Q_a^L]
&=
(\sigma_{L,\mu}\widetilde Y)_a{}^b\partial_b\\
&=(\sigma_{L,\mu})_{a\dot b}
\bar{\mathsf S}_L^{\dot b},
\end{aligned}
\tag{2B.43}
$$

$$
\begin{aligned}
[\mathsf P_\mu^L,\bar{\mathsf S}_L^{\dot a}]
&=-i(\bar\sigma_{L,\mu})^{\dot a b}\partial_b\\
&=(\bar\sigma_{L,\mu})^{\dot a b}\mathsf Q_b^L.
\end{aligned}
\tag{2B.44}
$$

Equations (2B.40)--(2B.42) give

$$
\begin{aligned}
\{\mathsf Q_a^L,\mathsf S_L^b\}
={}&-2i(\sigma_L^{\mu\nu})_a{}^b\mathsf J_{\mu\nu}^L
-2i\delta_a{}^b\mathsf D_{{\rm dil},L}
+3\delta_a{}^b\mathsf R_L.
\end{aligned}
\tag{2B.45}
$$

### 2B.7 Lorentzian superconformal algebra

The bosonic algebra is (2B.14), (2B.15), the Step-1 Lorentz algebra, and

$$
[\mathsf D_{{\rm dil},L},\mathsf J_{\mu\nu}^L]
=[\mathsf R_L,\mathsf J_{\mu\nu}^L]
=[\mathsf R_L,\mathsf P_\mu^L]
=[\mathsf R_L,\mathsf K_\mu^L]=0.
\tag{2B.46}
$$

$$
\begin{aligned}
[\mathsf J_{\mu\nu}^L,\mathsf Q_a^L]
&=-i(\sigma_{L,\mu\nu})_a{}^b\mathsf Q_b^L,\\
[\mathsf J_{\mu\nu}^L,\bar{\mathsf Q}_{\dot a}^L]
&=+i\bar{\mathsf Q}_{\dot b}^L
(\bar\sigma_{L,\mu\nu})^{\dot b}{}_{\dot a},\\
[\mathsf J_{\mu\nu}^L,\mathsf S_L^a]
&=+i\mathsf S_L^b(\sigma_{L,\mu\nu})_b{}^a,\\
[\mathsf J_{\mu\nu}^L,\bar{\mathsf S}_L^{\dot a}]
&=-i(\bar\sigma_{L,\mu\nu})^{\dot a}{}_{\dot b}
\bar{\mathsf S}_L^{\dot b}.
\end{aligned}
\tag{2B.47}
$$

$$
\begin{gathered}
[\mathsf D_{{\rm dil},L},\mathsf Q_a^L]
=\frac i2\mathsf Q_a^L,
\qquad
[\mathsf D_{{\rm dil},L},\bar{\mathsf Q}_{\dot a}^L]
=\frac i2\bar{\mathsf Q}_{\dot a}^L,\\
[\mathsf D_{{\rm dil},L},\mathsf S_L^a]
=-\frac i2\mathsf S_L^a,
\qquad
[\mathsf D_{{\rm dil},L},\bar{\mathsf S}_L^{\dot a}]
=-\frac i2\bar{\mathsf S}_L^{\dot a},\\
[\mathsf R_L,\mathsf Q_a^L]=-\mathsf Q_a^L,
\qquad
[\mathsf R_L,\bar{\mathsf Q}_{\dot a}^L]
=+\bar{\mathsf Q}_{\dot a}^L,\\
[\mathsf R_L,\mathsf S_L^a]=+\mathsf S_L^a,
\qquad
[\mathsf R_L,\bar{\mathsf S}_L^{\dot a}]
=-\bar{\mathsf S}_L^{\dot a}.
\end{gathered}
\tag{2B.48}
$$

$$
\begin{aligned}
[\mathsf K_\mu^L,\mathsf Q_a^L]
&=(\sigma_{L,\mu})_{a\dot b}\bar{\mathsf S}_L^{\dot b},\\
[\mathsf K_\mu^L,\bar{\mathsf Q}_{\dot a}^L]
&=-(\sigma_{L,\mu})_{b\dot a}\mathsf S_L^b,\\
[\mathsf P_\mu^L,\mathsf S_L^a]
&=-(\bar\sigma_{L,\mu})^{\dot b a}\bar{\mathsf Q}_{\dot b}^L,\\
[\mathsf P_\mu^L,\bar{\mathsf S}_L^{\dot a}]
&=(\bar\sigma_{L,\mu})^{\dot a b}\mathsf Q_b^L.
\end{aligned}
\tag{2B.49}
$$

$$
[\mathsf K_\mu^L,\mathsf S_L^a]
=[\mathsf K_\mu^L,\bar{\mathsf S}_L^{\dot a}]
=[\mathsf P_\mu^L,\mathsf Q_a^L]
=[\mathsf P_\mu^L,\bar{\mathsf Q}_{\dot a}^L]=0.
\tag{2B.50}
$$

$$
\boxed{
\begin{aligned}
\{\mathsf Q_a^L,\mathsf S_L^b\}
={}&-2i(\sigma_L^{\mu\nu})_a{}^b\mathsf J_{\mu\nu}^L
-2i\delta_a{}^b\mathsf D_{{\rm dil},L}
+3\delta_a{}^b\mathsf R_L,\\
\{\bar{\mathsf Q}_{\dot a}^L,\bar{\mathsf S}_L^{\dot b}\}
={}&-2i(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}
\mathsf J_{\mu\nu}^L
+2i\delta_{\dot a}{}^{\dot b}\mathsf D_{{\rm dil},L}
+3\delta_{\dot a}{}^{\dot b}\mathsf R_L.
\end{aligned}}
\tag{2B.51}
$$

$$
\boxed{
\{\mathsf S_{L,a},\bar{\mathsf S}_{L,\dot b}\}
=-2(\sigma_L^\mu)_{a\dot b}\mathsf K_\mu^L.}
\tag{2B.52}
$$

$$
\begin{gathered}
\{\mathsf Q_a^L,\bar{\mathsf S}_{L,\dot b}\}
=\{\bar{\mathsf Q}_{\dot a}^L,\mathsf S_{L,b}\}=0,\\
\{\mathsf S_{L,a},\mathsf S_{L,b}\}
=\{\bar{\mathsf S}_{L,\dot a},\bar{\mathsf S}_{L,\dot b}\}=0.
\end{gathered}
\tag{2B.53}
$$

### 2B.8 Chiral primary modules and adjoints

For a scalar chiral primary of scaling weight \(\Delta\), define

$$
\begin{aligned}
\mathsf D_{{\rm dil},L}^{(\Delta)}
&=-i\left(E_y+\frac12N_\vartheta+\Delta\right),\\
\mathsf R_L^{(r)}&=N_\vartheta+r,\\
\mathsf K_\mu^{L,(\Delta)}
&=\mathsf K_\mu^{L,(0)}+2i\Delta y_\mu,\\
\mathsf S_L^{a,(\Delta)}
&=\mathsf S_L^{a,(0)}-4i\Delta\vartheta^a.
\end{aligned}
\tag{2B.54}
$$

Insertion of (2B.54) into (2B.51) gives

$$
-4\Delta=-2\Delta+3r,
\qquad
\boxed{r=-\frac23\Delta.}
\tag{2B.55}
$$

For \(f,g\in C_c^\infty(\mathcal U_L)\), let

$$
\langle f,g\rangle_{L^2}:=\int_{\mathcal U_L}d^4x\,f(x)^*g(x).
\tag{2B.56a}
$$

Since

$$
d^4(I_Lx)=|x^2|^{-4}d^4x,
\tag{2B.56b}
$$

the core sesquilinear identities are

$$
\begin{aligned}
\langle f,\mathcal I_{L,\Delta}g\rangle_{L^2}
&=\int d^4u\,|u^2|^{\Delta-4}f(I_Lu)^*g(u)\\
&=\langle\mathcal I_{L,4-\Delta^*}f,g\rangle_{L^2},\\
\langle f,\mathsf D_{{\rm dil},L}^{(\Delta)}g\rangle_{L^2}
&=\int d^4x\,
\left[i(E_xf^*)+i(4-\Delta)f^*\right]g\\
&=\langle\mathsf D_{{\rm dil},L}^{(4-\Delta^*)}f,g\rangle_{L^2}.
\end{aligned}
\tag{2B.56}
$$

Using
\(\mathsf K_\mu^{L,(\Delta)}
=\mathcal I_{L,\Delta}\mathsf P_\mu^L\mathcal I_{L,\Delta}\)
and
\(\langle f,\mathsf P_\mu^Lg\rangle
=\langle\mathsf P_\mu^Lf,g\rangle\) on this core,

$$
\begin{aligned}
\langle f,\mathsf K_\mu^{L,(\Delta)}g\rangle
&=\langle\mathcal I_{L,4-\Delta^*}f,
\mathsf P_\mu^L\mathcal I_{L,\Delta}g\rangle\\
&=\langle\mathsf P_\mu^L\mathcal I_{L,4-\Delta^*}f,
\mathcal I_{L,\Delta}g\rangle\\
&=\langle
\mathcal I_{L,4-\Delta^*}\mathsf P_\mu^L
\mathcal I_{L,4-\Delta^*}f,g\rangle\\
&=\langle\mathsf K_\mu^{L,(4-\Delta^*)}f,g\rangle.
\end{aligned}
\tag{2B.57}
$$

No closed or maximal Hilbert-adjoint domains are asserted in (2B.56)--(2B.57).

For the algebraic formal adjoint (2A.35), define

$$
\begin{gathered}
E_{\bar y}:=\bar y^\mu\partial_\mu^{\bar y},
\qquad
\bar\vartheta^2:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a},
\qquad
\Delta':=3-\Delta^*,\\
\bar V_\mu{}^\nu
:=\bar y^2\delta_\mu{}^\nu-2\bar y_\mu\bar y^\nu,\\
\bar T_\mu
:=\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_{L,\mu})^{\dot a}{}_{\dot b}
\bar\partial_{\dot a}.
\end{gathered}
\tag{2B.58a}
$$

The antichiral operators are

$$
\boxed{
\begin{aligned}
\mathsf D_{{\rm dil},L}^{(\Delta'),{\rm ach}}
&:=-i\left(E_{\bar y}+\frac12N_{\bar\vartheta}+\Delta'\right),\\
\mathsf K_\mu^{L,(\Delta'),{\rm ach}}
&:=-i\left(\bar V_\mu{}^\nu\partial_\nu^{\bar y}-\bar T_\mu\right)
+2i\Delta'\bar y_\mu,\\
\bar{\mathsf S}_L^{\dot a,(\Delta'),{\rm ach}}
&:=2i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\mu)^{\dot a}{}_{\dot b}
\partial_\mu^{\bar y}
-2i\bar\vartheta^2\epsilon^{\dot a\dot b}\bar\partial_{\dot b}
-4i\Delta'\bar\vartheta^{\dot a}.
\end{aligned}}
\tag{2B.58b}
$$

The dilatation calculation is

$$
\begin{aligned}
(E_y)^{\ddagger_L}
&=(-\partial_\mu^{\bar y})\bar y^\mu=-E_{\bar y}-4,\\
(N_\vartheta)^{\ddagger_L}
&=-\bar\partial_{\dot a}\bar\vartheta^{\dot a}
=2-N_{\bar\vartheta},\\
(\mathsf D_{{\rm dil},L}^{(\Delta),{\rm ch}})^{\ddagger_L}
&=+i\left[-E_{\bar y}-4+\frac12(2-N_{\bar\vartheta})+\Delta^*\right]\\
&=-i\left(E_{\bar y}+\frac12N_{\bar\vartheta}+3-\Delta^*\right)\\
&=\mathsf D_{{\rm dil},L}^{(3-\Delta^*),{\rm ach}}.
\end{aligned}
\tag{2B.58c}
$$

For \(V_\mu{}^\nu:=y^2\delta_\mu{}^\nu-2y_\mu y^\nu\),

$$
\begin{gathered}
\partial_\nu^{\bar y}\bar V_\mu{}^\nu=-8\bar y_\mu,
\qquad
\operatorname{tr}(\widetilde{\bar Y}\sigma_{L,\mu})=-2\bar y_\mu,\\
[V_\mu{}^\nu\partial_\nu^y]^{\ddagger_L}
=-\bar V_\mu{}^\nu\partial_\nu^{\bar y}+8\bar y_\mu,\\
\left[
\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a\partial_a
\right]^{\ddagger_L}
=\bar T_\mu-2\bar y_\mu.
\end{gathered}
\tag{2B.58d}
$$

Therefore

$$
\begin{aligned}
(\mathsf K_\mu^{L,(\Delta),{\rm ch}})^{\ddagger_L}
&=+i\left[-\bar V_\mu{}^\nu\partial_\nu^{\bar y}
+\bar T_\mu+6\bar y_\mu\right]-2i\Delta^*\bar y_\mu\\
&=-i\left(\bar V_\mu{}^\nu\partial_\nu^{\bar y}-\bar T_\mu\right)
+2i(3-\Delta^*)\bar y_\mu\\
&=\mathsf K_\mu^{L,(3-\Delta^*),{\rm ach}}.
\end{aligned}
\tag{2B.58e}
$$

The spinor calculation is

$$
\begin{aligned}
\left[
2i\vartheta^b(\sigma_L^\mu\widetilde Y)_b{}^a\partial_\mu^y
\right]^{\ddagger_L}
&=2i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\mu)^{\dot a}{}_{\dot b}
\partial_\mu^{\bar y}-8i\bar\vartheta^{\dot a},\\
\left[-2i\vartheta^2\epsilon^{ab}\partial_b\right]^{\ddagger_L}
&=-2i\bar\vartheta^2\epsilon^{\dot a\dot b}\bar\partial_{\dot b}
-4i\bar\vartheta^{\dot a},\\
[-4i\Delta\vartheta^a]^{\ddagger_L}
&=+4i\Delta^*\bar\vartheta^{\dot a}.
\end{aligned}
\tag{2B.58f}
$$

Thus

$$
\begin{aligned}
(\mathsf S_L^{a,(\Delta),{\rm ch}})^{\ddagger_L}
={}&2i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\mu)^{\dot a}{}_{\dot b}
\partial_\mu^{\bar y}
-2i\bar\vartheta^2\epsilon^{\dot a\dot b}\bar\partial_{\dot b}\\
&-4i(3-\Delta^*)\bar\vartheta^{\dot a}\\
={}&\bar{\mathsf S}_L^{\dot a,(3-\Delta^*),{\rm ach}}.
\end{aligned}
\tag{2B.58g}
$$

For the \(R\)-weight,

$$
\begin{aligned}
(\mathsf R_L^{(r),{\rm ch}})^{\ddagger_L}
&=(N_\vartheta+r)^{\ddagger_L}\\
&=2-N_{\bar\vartheta}+r^*\\
&=-N_{\bar\vartheta}+r',
\qquad
r':=2+r^*.
\end{aligned}
\tag{2B.58h}
$$

Consequently,

$$
\boxed{
\begin{aligned}
(\mathsf D_{{\rm dil},L}^{(\Delta),{\rm ch}})^{\ddagger_L}
&=\mathsf D_{{\rm dil},L}^{(3-\Delta^*),{\rm ach}},\\
(\mathsf K_\mu^{L,(\Delta),{\rm ch}})^{\ddagger_L}
&=\mathsf K_\mu^{L,(3-\Delta^*),{\rm ach}},\\
(\mathsf S_L^{a,(\Delta),{\rm ch}})^{\ddagger_L}
&=\bar{\mathsf S}_L^{\dot a,(3-\Delta^*),{\rm ach}},\\
(\mathsf R_L^{(r),{\rm ch}})^{\ddagger_L}
&=\mathsf R_L^{(2+r^*),{\rm ach}},
\qquad
\mathsf R_L^{(r'),{\rm ach}}:=-N_{\bar\vartheta}+r'.
\end{aligned}}
\tag{2B.58}
$$

Since

$$
r=-\frac23\Delta,
\qquad
r'=2+r^*
=2-\frac23\Delta^*
=\frac23(3-\Delta^*)
=\frac23\Delta',
\tag{2B.59a}
$$

the same-weight chiral/antichiral coordinate pairing occurs at

$$
\Delta=\frac32,
\qquad
r_{\rm ch}=-1,
\qquad
r_{\rm ach}=+1,
\qquad
(\mathsf S_L^{a,(3/2),{\rm ch}})^{\ddagger_L}
=\bar{\mathsf S}_L^{\dot a,(3/2),{\rm ach}}.
\tag{2B.59}
$$

For real bosonic parameters and Lorentzian spinor reality,

$$
\lambda^*=\lambda,
\qquad
\rho^*=\rho,
\qquad
(b^\mu)^*=b^\mu,
\qquad
(\zeta^a)^{\dagger}=\bar\zeta^{\dot a}.
\tag{2B.60a}
$$

Choose the Noether currents in (2B.4) with

$$
(j_D^\mu)^{\dagger_{\mathcal H}}=j_D^\mu,
\qquad
(j_R^\mu)^{\dagger_{\mathcal H}}=j_R^\mu,
\qquad
(j_{K_\nu}^\mu)^{\dagger_{\mathcal H}}=j_{K_\nu}^\mu,
\qquad
(j_{S,a}^\mu)^{\dagger_{\mathcal H}}=\bar j_{S,\dot a}^\mu.
\tag{2B.60b}
$$

Order reversal for the odd parameter gives

$$
\begin{aligned}
(\zeta^aS_a^L)^{\dagger_{\mathcal H}}
&=\bar S_{\dot a}^L\bar\zeta^{\dot a}
=-\bar\zeta^{\dot a}\bar S_{\dot a}^L
=\bar\zeta_{\dot a}\bar S_L^{\dot a}.
\end{aligned}
\tag{2B.60c}
$$

Thus the generator multiplying \(-i\) in (2B.3) is Hermitian,
\(U_L^\dagger U_L=1\), and the physical Noether charges obey

$$
D_{{\rm dil},L}^{\dagger_{\mathcal H}}=D_{{\rm dil},L},
\quad
R_L^{\dagger_{\mathcal H}}=R_L,
\quad
(K_\mu^L)^{\dagger_{\mathcal H}}=K_\mu^L,
\quad
(S_a^L)^{\dagger_{\mathcal H}}=\bar S_{\dot a}^L.
\tag{2B.60}
$$

### 2B.9 Euclidean Wick continuation

Let \(\mathcal W\) denote

$$
x_L^0=-ix_E^4,
\qquad
\partial_0^L=i\partial_4^E,
\qquad
\vartheta_E=\vartheta_L,
\qquad
\bar\vartheta_E=\bar\vartheta_L.
\tag{2B.61}
$$

The Euclidean active element is

$$
\begin{aligned}
U_E\big|_{\rm sc}
:={}&1+\frac i2\omega_{mn}^EJ_E^{mn}
+a_E^mP_m^E+\lambda_E D_{{\rm dil},E}+\rho_E R_E\\
&+b_E^mK_m^E+\zeta_E^aS_a^E
+\bar\zeta^E_{\dot a}\bar S_E^{\dot a}.
\end{aligned}
\tag{2B.61a}
$$

The parameters are

$$
\lambda_E=\lambda_L,
\qquad
\rho_E=\rho_L,
\qquad
\zeta_E=\zeta_L,
\qquad
\bar\zeta_E=\bar\zeta_L,
\qquad
b_E^i=b_L^i,
\qquad
b_E^4=ib_L^0.
\tag{2B.61b}
$$

Exponent matching first gives the physical Noether charges

$$
\begin{gathered}
D_{{\rm dil},E}=-i\mathcal W(D_{{\rm dil},L}),
\qquad
R_E=-i\mathcal W(R_L),\\
Q_a^E=-i\mathcal W(Q_a^L),
\qquad
\bar Q_{\dot a}^E=-i\mathcal W(\bar Q_{\dot a}^L),\\
S_a^E=-i\mathcal W(S_a^L),
\qquad
\bar S_{\dot a}^E=-i\mathcal W(\bar S_{\dot a}^L),\\
P_i^E=-i\mathcal W(P_i^L),
\qquad
P_4^E=-\mathcal W(P_0^L),\\
K_i^E=-i\mathcal W(K_i^L),
\qquad
K_4^E=-\mathcal W(K_0^L),\\
J_{ij}^E=\mathcal W(J_{ij}^L),
\qquad
J_{4i}^E=-i\mathcal W(J_{0i}^L).
\end{gathered}
\tag{2B.61c}
$$

Diagonal covariance gives the same phases for the coordinate realizations:

$$
\boxed{
\begin{gathered}
\mathsf D_{{\rm dil},E}=-i\mathcal W(\mathsf D_{{\rm dil},L}),
\qquad
\mathsf R_E=-i\mathcal W(\mathsf R_L),\\
\mathsf Q_a^E=-i\mathcal W(\mathsf Q_a^L),
\qquad
\bar{\mathsf Q}_{\dot a}^E=-i\mathcal W(\bar{\mathsf Q}_{\dot a}^L),\\
\mathsf S_E^a=-i\mathcal W(\mathsf S_L^a),
\qquad
\bar{\mathsf S}_E^{\dot a}
=-i\mathcal W(\bar{\mathsf S}_L^{\dot a}).
\end{gathered}}
\tag{2B.62}
$$

$$
\boxed{
\begin{aligned}
\mathsf P_i^E&=-i\mathcal W(\mathsf P_i^L),
&\mathsf P_4^E&=-\mathcal W(\mathsf P_0^L),\\
\mathsf K_i^E&=-i\mathcal W(\mathsf K_i^L),
&\mathsf K_4^E&=-\mathcal W(\mathsf K_0^L),\\
\mathsf J_{ij}^E&=\mathcal W(\mathsf J_{ij}^L),
&\mathsf J_{4i}^E&=-i\mathcal W(\mathsf J_{0i}^L).
\end{aligned}}
\tag{2B.63}
$$

The Euclidean superinversion is defined without a Euclidean dagger:

$$
\mathcal I_{s,E}:=\mathcal W\mathcal I_{s,L}\mathcal W^{-1},
\qquad
\mathcal I_{s,E}^2=1,
\tag{2B.63a}
$$

$$
y_E'{}^m=\frac{\bar y_E^m}{\bar y_E^2},
\qquad
\bar y_E'{}^m=\frac{y_E^m}{y_E^2},
\tag{2B.63b}
$$

On the domain where the bodies of \(y_E^2\) and \(\bar y_E^2\) are nonzero, the full \(\mathcal W\)-image of (2B.32) is

$$
\boxed{
\begin{aligned}
\widetilde Y_E'&=\bar Y_E^{-1},
&\qquad
\vartheta_E'{}^a
&=-(\widetilde{\bar\vartheta}_E\bar Y_E^{-1})^a,\\
\widetilde{\bar Y}_E'&=Y_E^{-1},
&
\bar\vartheta'_{E,\dot a}
&=+(Y_E^{-1}\widetilde\vartheta_E)_{\dot a}.
\end{aligned}}
\tag{2B.63c}
$$

The two Euclidean Weyl coordinates remain independent.

### 2B.10 Euclidean chiral coordinate generators

$$
y_E^m=x_E^m+\vartheta\sigma_E^m\bar\vartheta,
\qquad
\widetilde Y_E^{\dot a a}
:=y_{E,m}(\bar\sigma_E^m)^{\dot a a}.
\tag{2B.64}
$$

$$
\boxed{
\begin{aligned}
\mathsf P_m^E&=-\partial_m^E,\\
\mathsf Q_a^E&=-\partial_a,\\
\bar{\mathsf Q}_{\dot a}^E
&=-2\vartheta^b(\sigma_E^m)_{b\dot a}\partial_m^E,\\
\mathsf D_{{\rm dil},E}
&=-\left(y_E^m\partial_m^E+\frac12N_\vartheta\right),\\
\mathsf R_E&=-iN_\vartheta.
\end{aligned}}
\tag{2B.65}
$$

$$
\boxed{
\mathsf J_{mn}^E
=-i(y_{E,m}\partial_n^E-y_{E,n}\partial_m^E)
-i\vartheta^a(\sigma_{E,mn})_a{}^b\partial_b.}
\tag{2B.66}
$$

$$
\boxed{
\mathsf K_m^E
=-\left[
(y_E^2\delta_m{}^n-2y_{E,m}y_E^n)\partial_n^E
-\vartheta^b(\sigma_{E,m}\widetilde Y_E)_b{}^a\partial_a
\right].}
\tag{2B.67}
$$

$$
\boxed{
\bar{\mathsf S}_E^{\dot a}
=\widetilde Y_E^{\dot a b}\partial_b,}
\tag{2B.68}
$$

$$
\boxed{
\mathsf S_E^a
=-2\vartheta^b(\sigma_E^m\widetilde Y_E)_b{}^a\partial_m^E
-2\vartheta^2\epsilon^{ab}\partial_b.}
\tag{2B.69}
$$

### 2B.11 Euclidean superconformal algebra

$$
\begin{gathered}
[\mathsf D_{{\rm dil},E},\mathsf P_m^E]=+\mathsf P_m^E,
\qquad
[\mathsf D_{{\rm dil},E},\mathsf K_m^E]=-\mathsf K_m^E,\\
[\mathsf P_m^E,\mathsf K_n^E]
=2\delta_{mn}\mathsf D_{{\rm dil},E}+2i\mathsf J_{mn}^E,\\
[\mathsf K_m^E,\mathsf K_n^E]=0.
\end{gathered}
\tag{2B.70}
$$

$$
\begin{gathered}
[\mathsf D_{{\rm dil},E},\mathsf Q_a^E]
=\frac12\mathsf Q_a^E,
\qquad
[\mathsf D_{{\rm dil},E},\bar{\mathsf Q}_{\dot a}^E]
=\frac12\bar{\mathsf Q}_{\dot a}^E,\\
[\mathsf D_{{\rm dil},E},\mathsf S_E^a]
=-\frac12\mathsf S_E^a,
\qquad
[\mathsf D_{{\rm dil},E},\bar{\mathsf S}_E^{\dot a}]
=-\frac12\bar{\mathsf S}_E^{\dot a},\\
[\mathsf R_E,\mathsf Q_a^E]=+i\mathsf Q_a^E,
\qquad
[\mathsf R_E,\bar{\mathsf Q}_{\dot a}^E]
=-i\bar{\mathsf Q}_{\dot a}^E,\\
[\mathsf R_E,\mathsf S_E^a]=-i\mathsf S_E^a,
\qquad
[\mathsf R_E,\bar{\mathsf S}_E^{\dot a}]
=+i\bar{\mathsf S}_E^{\dot a}.
\end{gathered}
\tag{2B.71}
$$

$$
\begin{aligned}
[\mathsf K_m^E,\mathsf Q_a^E]
&=(\sigma_{E,m})_{a\dot b}\bar{\mathsf S}_E^{\dot b},\\
[\mathsf K_m^E,\bar{\mathsf Q}_{\dot a}^E]
&=-(\sigma_{E,m})_{b\dot a}\mathsf S_E^b,\\
[\mathsf P_m^E,\mathsf S_E^a]
&=-(\bar\sigma_{E,m})^{\dot b a}\bar{\mathsf Q}_{\dot b}^E,\\
[\mathsf P_m^E,\bar{\mathsf S}_E^{\dot a}]
&=(\bar\sigma_{E,m})^{\dot a b}\mathsf Q_b^E.
\end{aligned}
\tag{2B.72}
$$

$$
\boxed{
\begin{aligned}
\{\mathsf Q_a^E,\mathsf S_E^b\}
={}&-2i(\sigma_E^{mn})_a{}^b\mathsf J_{mn}^E
-2\delta_a{}^b\mathsf D_{{\rm dil},E}
-3i\delta_a{}^b\mathsf R_E,\\
\{\bar{\mathsf Q}_{\dot a}^E,\bar{\mathsf S}_E^{\dot b}\}
={}&-2i(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}\mathsf J_{mn}^E
+2\delta_{\dot a}{}^{\dot b}\mathsf D_{{\rm dil},E}
-3i\delta_{\dot a}{}^{\dot b}\mathsf R_E.
\end{aligned}}
\tag{2B.73}
$$

$$
\{\mathsf Q_a^E,\bar{\mathsf Q}_{\dot b}^E\}
=-2(\sigma_E^m)_{a\dot b}\mathsf P_m^E,
\qquad
\{\mathsf S_{E,a},\bar{\mathsf S}_{E,\dot b}\}
=-2(\sigma_E^m)_{a\dot b}\mathsf K_m^E.
\tag{2B.74}
$$

All same-chirality \(Q\)-\(Q\), \(S\)-\(S\), crossed \(Q\)-\(\bar S\), and crossed \(\bar Q\)-\(S\) anticommutators vanish.  The \(SO(4)\) action is

$$
\begin{aligned}
[\mathsf J_{mn}^E,\mathsf Q_a^E]
&=+i(\sigma_{E,mn})_a{}^b\mathsf Q_b^E,\\
[\mathsf J_{mn}^E,\bar{\mathsf Q}_{\dot a}^E]
&=-i\bar{\mathsf Q}_{\dot b}^E
(\bar\sigma_{E,mn})^{\dot b}{}_{\dot a},\\
[\mathsf J_{mn}^E,\mathsf S_E^a]
&=-i\mathsf S_E^b(\sigma_{E,mn})_b{}^a,\\
[\mathsf J_{mn}^E,\bar{\mathsf S}_E^{\dot a}]
&=+i(\bar\sigma_{E,mn})^{\dot a}{}_{\dot b}
\bar{\mathsf S}_E^{\dot b}.
\end{aligned}
\tag{2B.75}
$$

### 2B.12 Euclidean adjoints

Define the bosonic restrictions on \(C_c^\infty(\mathbb R^4\setminus\{0\})\):

$$
\mathsf D_{{\rm dil},E,{\rm bos}}^{(\Delta)}
:=-(x_E\cdot\partial_E+\Delta),
\tag{2B.75a}
$$

$$
\mathsf K_{m,E,{\rm bos}}^{(\Delta)}
:=-(x_E^2\delta_m{}^n-2x_{E,m}x_E^n)\partial_n^E
+2\Delta x_{E,m}.
\tag{2B.75b}
$$

For \(f,g\in C_c^\infty(\mathbb R^4\setminus\{0\})\), the bosonic
core sesquilinear identities are

$$
\begin{aligned}
\langle f,\mathsf D_{{\rm dil},E,{\rm bos}}^{(\Delta)}g\rangle_{L^2}
&=\langle-\mathsf D_{{\rm dil},E,{\rm bos}}^{(4-\Delta^*)}f,g\rangle_{L^2},\\
\langle f,\mathsf K_{m,E,{\rm bos}}^{(\Delta)}g\rangle_{L^2}
&=\langle-\mathsf K_{m,E,{\rm bos}}^{(4-\Delta^*)}f,g\rangle_{L^2}.
\end{aligned}
\tag{2B.76}
$$

$$
(x_E\cdot\partial_E)^{\dagger_{L^2}}
=-x_E\cdot\partial_E-4,
\tag{2B.76a}
$$

$$
\begin{aligned}
\left(
-x_E^2\partial_m^E
+2x_{E,m}x_E\cdot\partial_E
+2\Delta x_{E,m}
\right)^{\dagger_{L^2}}
={}&x_E^2\partial_m^E
-2x_{E,m}x_E\cdot\partial_E\\
&+(2\Delta^*-8)x_{E,m}\\
=-{}&\mathsf K_{m,E,{\rm bos}}^{(4-\Delta^*)}.
\end{aligned}
\tag{2B.76b}
$$

No closed or maximal Hilbert-adjoint domains are asserted in (2B.76).

Wick transport of the physical Lorentzian adjoint gives

$$
\begin{gathered}
(D_{{\rm dil},E})^{\dagger_W}=-D_{{\rm dil},E},
\qquad
(R_E)^{\dagger_W}=-R_E,\\
(K_i^E)^{\dagger_W}=-K_i^E,
\qquad
(K_4^E)^{\dagger_W}=K_4^E,\\
(S_a^E)^{\dagger_W}=-\bar S_{\dot a}^E,
\qquad
(iS_a^E)^{\dagger_W}=i\bar S_{\dot a}^E.
\end{gathered}
\tag{2B.77}
$$

Intrinsic Euclidean superspace imposes no adjoint relation between \(S_a^E\) and \(\bar S_{\dot a}^E\).  A full superspace \(L^2\) adjoint requires a separately fixed Berezin pairing.

### 2B.13 Verification surface

$$
\begin{array}{c|ccc}
&\text{operator identities}&\text{exact input cases}&\text{failures}\\ \hline
L&905&54300&0\\
E&763&45780&0
\end{array}
\tag{2B.78}
$$

The structural checks use only `SUPERCONFORMAL-KILLING-STRUCTURE` and `SUPERINVERSION-DUALITY-STRUCTURE`.  The generator coefficients, graded algebra, and Wick phases are covered by (2B.78).  The inversion and adjoint statements are established separately by (2B.7)--(2B.10), (2B.32)--(2B.35c), (2B.56)--(2B.60), and (2B.75a)--(2B.77).
