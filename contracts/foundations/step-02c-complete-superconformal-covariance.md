# 00 3+1d SUSY QFT — Convention Lock

## Step 2C. Complete superconformal coordinate representation and covariance

### 2C.1 Full-superspace coordinate algebra

$$
z_L^M=(x^\mu,\vartheta^a,\bar\vartheta^{\dot a}),
\qquad
\bar\vartheta^{\dot a}
:=\epsilon^{\dot a\dot b}\bar\vartheta_{\dot b},
\qquad
\widetilde{\bar\partial}_{\dot a}
:=\frac{\vec\partial}{\partial\bar\vartheta^{\dot a}}
=-\bar\partial_{\dot a}.
\tag{2C.1}
$$

$$
\begin{gathered}
B_L^\mu:=\vartheta^a(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b},
\qquad
y^\mu:=x^\mu-iB_L^\mu,
\qquad
\bar y^\mu:=x^\mu+iB_L^\mu,\\
Y_{a\dot a}:=y_\mu(\sigma_L^\mu)_{a\dot a},
\qquad
\widetilde Y^{\dot a a}:=y_\mu(\bar\sigma_L^\mu)^{\dot a a},\\
\bar Y_{a\dot a}:=\bar y_\mu(\sigma_L^\mu)_{a\dot a},
\qquad
\widetilde{\bar Y}^{\dot a a}
:=\bar y_\mu(\bar\sigma_L^\mu)^{\dot a a}.
\end{gathered}
\tag{2C.2}
$$

$$
V_\mu{}^\nu(u)
:=u^2\delta_\mu{}^\nu-2u_\mu u^\nu,
\qquad
\vartheta^2:=\vartheta^a\vartheta_a,
\qquad
\bar\vartheta^2:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}.
\tag{2C.3}
$$

$$
\Lambda(\chi^1,\ldots,\chi^4)
:=\frac{\mathbb C\langle\chi^1,\ldots,\chi^4\rangle}
{\left\langle
\chi^I\chi^J+\chi^J\chi^I
\right\rangle_{I,J=1}^{4}}.
\tag{2C.3a}
$$

All coefficient functions multiply from the left.  The weight-zero scalar coordinate module is

$$
\mathcal F_0^L
:=\mathbb C[x^\mu]\widehat\otimes
\Lambda(\vartheta^1,\vartheta^2,
\bar\vartheta^{\dot1},\bar\vartheta^{\dot2}),
\qquad
\Delta=r=0.
\tag{2C.4}
$$

The Lorentzian translation generator is fixed before every other generator:

$$
\boxed{\mathsf P_\mu^L=-i\partial_\mu.}
\tag{2C.5}
$$

$$
P_\mu^{L,{\rm coordinate}}
:=\mathsf P_\mu^L,
\qquad
P_\mu^{L,{\mathcal H}}:=P_\mu^L.
\tag{2C.5a}
$$

The full flat generators are

$$
\boxed{
\begin{aligned}
\mathsf Q_a^L
&=-i\partial_a
+(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}\partial_\mu,\\
\bar{\mathsf Q}_{\dot a}^L
&=+i\widetilde{\bar\partial}_{\dot a}
-\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu,\\
\mathsf D_{{\rm dil},L}
&=-i\left(
x^\mu\partial_\mu
+\frac12\vartheta^a\partial_a
+\frac12\bar\vartheta^{\dot a}
\widetilde{\bar\partial}_{\dot a}
\right),\\
\mathsf R_L
&=\vartheta^a\partial_a
-\bar\vartheta^{\dot a}
\widetilde{\bar\partial}_{\dot a}.
\end{aligned}}
\tag{2C.6}
$$

$$
\boxed{
\begin{aligned}
\mathsf J_{\mu\nu}^L
={}&-i(x_\mu\partial_\nu-x_\nu\partial_\mu)
+i\vartheta^c(\sigma_{L,\mu\nu})_c{}^d\partial_d\\
&-i(\bar\sigma_{L,\mu\nu})^{\dot c}{}_{\dot d}
\bar\vartheta^{\dot d}
\widetilde{\bar\partial}_{\dot c}.
\end{aligned}}
\tag{2C.7}
$$

### 2C.2 Superinversion conjugation

On the domain of (2B.31a), use the involution fixed in (2B.32):

$$
\begin{aligned}
\widetilde Y'&=-\bar Y^{-1},
&\vartheta'{}^a&=-i\bar\vartheta_{\dot b}(\bar Y^{-1})^{\dot b a},\\
\widetilde{\bar Y}'&=-Y^{-1},
&\bar\vartheta'_{\dot a}
&=+i\epsilon_{\dot a\dot b}(Y^{-1})^{\dot b c}\vartheta_c,
\end{aligned}
\qquad
\mathcal I_{s,L}^2=1.
\tag{2C.8}
$$

$$
x'{}^\mu
=\frac12\left(
\frac{\bar y^\mu}{\bar y^2}
+\frac{y^\mu}{y^2}
\right).
\tag{2C.9}
$$

For

$$
X\in\{\mathsf P_\mu^L,\mathsf Q_a^L,
\bar{\mathsf Q}_{\dot a}^L\},
\qquad
\widehat X:=\mathcal I_{s,L}^*X\mathcal I_{s,L}^*,
\tag{2C.10}
$$

the action on every coordinate is

$$
(\widehat Xz^M)(z)
=\left.
X_u\big(\mathcal I_{s,L}^{M}(u)\big)
\right|_{u=\mathcal I_{s,L}z}.
\tag{2C.11}
$$

The left-derivative chart changes are

$$
\begin{aligned}
\left.\partial_a\right|_x
&=\left.\partial_a\right|_y
-i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\partial_\mu^y\\
&=\left.\partial_a\right|_{\bar y}
+i(\sigma_L^\mu)_{a\dot b}\bar\vartheta^{\dot b}
\partial_\mu^{\bar y},\\
\left.\widetilde{\bar\partial}_{\dot a}\right|_x
&=\left.\widetilde{\bar\partial}_{\dot a}\right|_y
+i\vartheta^b(\sigma_L^\mu)_{b\dot a}\partial_\mu^y\\
&=\left.\widetilde{\bar\partial}_{\dot a}\right|_{\bar y}
-i\vartheta^b(\sigma_L^\mu)_{b\dot a}
\partial_\mu^{\bar y}.
\end{aligned}
\tag{2C.12}
$$

At $u=\mathcal I_{s,L}z$,

$$
\left.Y(u)^{-1}\right|_{u=\mathcal I_{s,L}z}
=Y'(z)^{-1}=-\widetilde{\bar Y}(z),
\qquad
\left.\bar Y(u)^{-1}\right|_{u=\mathcal I_{s,L}z}
=\bar Y'(z)^{-1}=-\widetilde Y(z).
\tag{2C.12a}
$$

The even Jacobian block is

$$
\begin{aligned}
\left.
\frac{\partial}{\partial x^\mu}
\frac{\bar y^\nu}{\bar y^2}
\right|_{u=\mathcal I_{s,L}z}
&=V_\mu{}^\nu(y),\\
\left.
\frac{\partial}{\partial x^\mu}
\frac{y^\nu}{y^2}
\right|_{u=\mathcal I_{s,L}z}
&=V_\mu{}^\nu(\bar y),\\
\left.
\partial_{x^\mu}
\left[-i\bar\vartheta_{\dot c}
(\bar Y^{-1})^{\dot c a}\right]
\right|_{u=\mathcal I_{s,L}z}
&=\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a,\\
\left.
\partial_{x^\mu}
\left[+i(Y^{-1})^{\dot a c}\vartheta_c\right]
\right|_{u=\mathcal I_{s,L}z}
&=\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_{L,\mu})^{\dot a}{}_{\dot b}.
\end{aligned}
\tag{2C.12b}
$$

The simple odd Jacobian block is

$$
\begin{aligned}
\mathsf S_L^a\bar\vartheta^{\dot c}
&=\epsilon^{ab}
\left.
(-i\partial_b)
\left[+i(Y^{-1})^{\dot c d}\vartheta_d\right]
\right|_{u=\mathcal I_{s,L}z}\\
&=-\epsilon^{ab}
\widetilde{\bar Y}^{\dot c d}\epsilon_{db}
=\widetilde{\bar Y}^{\dot c a},\\
\bar{\mathsf S}_L^{\dot a}\vartheta^c
&=\epsilon^{\dot a\dot b}
\left.
(-i\bar\partial_{\dot b})
\left[-i\bar\vartheta_{\dot d}
(\bar Y^{-1})^{\dot d c}\right]
\right|_{u=\mathcal I_{s,L}z}\\
&=\epsilon^{\dot a\dot b}
\epsilon_{\dot b\dot d}\widetilde Y^{\dot d c}
=\widetilde Y^{\dot a c}.
\end{aligned}
\tag{2C.12c}
$$

The remaining odd Jacobian block is

$$
\begin{aligned}
\mathsf S_L^ay^\nu
&=\epsilon^{ab}
\left.
2(\sigma_L^\mu)_{b\dot c}\bar\vartheta^{\dot c}
\frac{\partial}{\partial\bar y^\mu}
\frac{\bar y^\nu}{\bar y^2}
\right|_{u=\mathcal I_{s,L}z}\\
&=2i\vartheta^c(\sigma_L^\nu\widetilde Y)_c{}^a,\\
\mathsf S_L^a\vartheta^c
&=\epsilon^{ab}
\left.
2(\sigma_L^\mu)_{b\dot d}\bar\vartheta^{\dot d}
\frac{\partial}{\partial\bar y^\mu}
\left[-i\bar\vartheta_{\dot e}
(\bar Y^{-1})^{\dot e c}\right]
\right|_{u=\mathcal I_{s,L}z}\\
&=-2i\vartheta^2\epsilon^{ac},\\
\bar{\mathsf S}_L^{\dot a}\bar y^\nu
&=2i\bar\vartheta^{\dot c}
(\widetilde{\bar Y}\sigma_L^\nu)^{\dot a}{}_{\dot c},\\
\bar{\mathsf S}_L^{\dot a}\bar\vartheta^{\dot c}
&=2i\bar\vartheta^2\epsilon^{\dot a\dot c}.
\end{aligned}
\tag{2C.12d}
$$

Define

$$
\mathsf K_\mu^L:=\mathcal I_{s,L}^*\mathsf P_\mu^L\mathcal I_{s,L}^*,
\quad
\mathsf S_{L,a}:=\mathcal I_{s,L}^*\mathsf Q_a^L\mathcal I_{s,L}^*,
\quad
\bar{\mathsf S}_{L,\dot a}
:=\mathcal I_{s,L}^*\bar{\mathsf Q}_{\dot a}^L\mathcal I_{s,L}^*.
\tag{2C.13}
$$

Equation (2C.11) gives

$$
\begin{array}{c|cccc}
&y^\nu&\bar y^\nu&\vartheta^c&\bar\vartheta^{\dot c}\\ \hline
\mathsf K_\mu^L
&-iV_\mu{}^\nu(y)
&-iV_\mu{}^\nu(\bar y)
&-i\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^c
&-i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_{L,\mu})^{\dot c}{}_{\dot b}\\
\mathsf S_L^a
&2i\vartheta^b(\sigma_L^\nu\widetilde Y)_b{}^a
&0
&-2i\vartheta^2\epsilon^{ac}
&\widetilde{\bar Y}^{\dot c a}\\
\bar{\mathsf S}_L^{\dot a}
&0
&2i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\nu)^{\dot a}{}_{\dot b}
&\widetilde Y^{\dot a c}
&2i\bar\vartheta^2\epsilon^{\dot a\dot c}
\end{array}
\tag{2C.14}
$$

Since $x=(y+\bar y)/2$,

$$
\begin{aligned}
\mathsf K_\mu^Lx^\nu
&=-\frac i2\left[V_\mu{}^\nu(y)+V_\mu{}^\nu(\bar y)\right],\\
\mathsf S_L^ax^\mu
&=i\vartheta^b(\sigma_L^\mu\widetilde Y)_b{}^a,\\
\bar{\mathsf S}_L^{\dot a}x^\mu
&=i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\mu)^{\dot a}{}_{\dot b}.
\end{aligned}
\tag{2C.15}
$$

Therefore the complete full-superspace operators are

$$
\boxed{
\begin{aligned}
\mathsf K_\mu^L
={}&-\frac i2
\left[V_\mu{}^\nu(y)+V_\mu{}^\nu(\bar y)\right]\partial_\nu\\
&-i\vartheta^b(\sigma_{L,\mu}\widetilde Y)_b{}^a\partial_a\\
&-i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_{L,\mu})^{\dot a}{}_{\dot b}
\widetilde{\bar\partial}_{\dot a},
\end{aligned}}
\tag{2C.16}
$$

$$
\boxed{
\begin{aligned}
\mathsf S_L^a
={}&i\vartheta^b(\sigma_L^\mu\widetilde Y)_b{}^a\partial_\mu
-2i\vartheta^2\epsilon^{ab}\partial_b
+\widetilde{\bar Y}^{\dot b a}
\widetilde{\bar\partial}_{\dot b},\\
\bar{\mathsf S}_L^{\dot a}
={}&i\bar\vartheta^{\dot b}
(\widetilde{\bar Y}\sigma_L^\mu)^{\dot a}{}_{\dot b}\partial_\mu
+\widetilde Y^{\dot a b}\partial_b
+2i\bar\vartheta^2\epsilon^{\dot a\dot b}
\widetilde{\bar\partial}_{\dot b}.
\end{aligned}}
\tag{2C.17}
$$

$$
\mathsf S_{L,a}:=\epsilon_{ab}\mathsf S_L^b,
\qquad
\bar{\mathsf S}_{L,\dot a}
:=\epsilon_{\dot a\dot b}\bar{\mathsf S}_L^{\dot b}.
\tag{2C.18}
$$

The chiral restriction of (2C.16)--(2C.17) is exactly (2B.36)--(2B.38); the antichiral restriction is the weight-zero vector-field part of (2B.58b).

For the phase family (2B.35),

$$
\mathsf K_{\mu;\phi}^L=\mathsf K_\mu^L,
\qquad
\mathsf S_{L;\phi}^a=e^{-i\phi}\mathsf S_L^a,
\qquad
\bar{\mathsf S}_{L;\phi}^{\dot a}
=e^{+i\phi}\bar{\mathsf S}_L^{\dot a}.
\tag{2C.19}
$$

### 2C.3 Complete Lorentzian coordinate algebra

$$
[A,B\}:=AB-(-1)^{|A||B|}BA.
\tag{2C.20}
$$

The complete even sector is

$$
\begin{aligned}
[\mathsf J_{\mu\nu}^L,\mathsf J_{\rho\sigma}^L]
=i\big(&\eta_{\mu\rho}\mathsf J_{\nu\sigma}^L
-\eta_{\nu\rho}\mathsf J_{\mu\sigma}^L\\
&-\eta_{\mu\sigma}\mathsf J_{\nu\rho}^L
+\eta_{\nu\sigma}\mathsf J_{\mu\rho}^L\big),
\end{aligned}
\tag{2C.21}
$$

$$
\begin{aligned}
[\mathsf J_{\mu\nu}^L,\mathsf P_\rho^L]
&=i\eta_{\mu\rho}\mathsf P_\nu^L
-i\eta_{\nu\rho}\mathsf P_\mu^L,\\
[\mathsf J_{\mu\nu}^L,\mathsf K_\rho^L]
&=i\eta_{\mu\rho}\mathsf K_\nu^L
-i\eta_{\nu\rho}\mathsf K_\mu^L,\\
[\mathsf D_{{\rm dil},L},\mathsf P_\mu^L]
&=+i\mathsf P_\mu^L,\\
[\mathsf D_{{\rm dil},L},\mathsf K_\mu^L]
&=-i\mathsf K_\mu^L,\\
[\mathsf P_\mu^L,\mathsf K_\nu^L]
&=2i\left(
\eta_{\mu\nu}\mathsf D_{{\rm dil},L}
-\mathsf J_{\mu\nu}^L
\right).
\end{aligned}
\tag{2C.22}
$$

$$
\begin{gathered}
[\mathsf P_\mu^L,\mathsf P_\nu^L]
=[\mathsf K_\mu^L,\mathsf K_\nu^L]
=[\mathsf D_{{\rm dil},L},\mathsf J_{\mu\nu}^L]
=[\mathsf D_{{\rm dil},L},\mathsf R_L]=0,\\
[\mathsf D_{{\rm dil},L},\mathsf D_{{\rm dil},L}]
=[\mathsf R_L,\mathsf R_L]=0,\\
[\mathsf R_L,\mathsf J_{\mu\nu}^L]
=[\mathsf R_L,\mathsf P_\mu^L]
=[\mathsf R_L,\mathsf K_\mu^L]=0.
\end{gathered}
\tag{2C.23}
$$

The Lorentz action on the odd generators is

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
\tag{2C.24}
$$

$$
\begin{aligned}
[\mathsf D_{{\rm dil},L},\mathsf Q_a^L]
&=+\frac i2\mathsf Q_a^L,
&[\mathsf D_{{\rm dil},L},\bar{\mathsf Q}_{\dot a}^L]
&=+\frac i2\bar{\mathsf Q}_{\dot a}^L,\\
[\mathsf D_{{\rm dil},L},\mathsf S_L^a]
&=-\frac i2\mathsf S_L^a,
&[\mathsf D_{{\rm dil},L},\bar{\mathsf S}_L^{\dot a}]
&=-\frac i2\bar{\mathsf S}_L^{\dot a},\\
[\mathsf R_L,\mathsf Q_a^L]
&=-\mathsf Q_a^L,
&[\mathsf R_L,\bar{\mathsf Q}_{\dot a}^L]
&=+\bar{\mathsf Q}_{\dot a}^L,\\
[\mathsf R_L,\mathsf S_L^a]
&=+\mathsf S_L^a,
&[\mathsf R_L,\bar{\mathsf S}_L^{\dot a}]
&=-\bar{\mathsf S}_L^{\dot a}.
\end{aligned}
\tag{2C.25}
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
\tag{2C.26}
$$

$$
\begin{gathered}
[\mathsf P_\mu^L,\mathsf Q_a^L]
=[\mathsf P_\mu^L,\bar{\mathsf Q}_{\dot a}^L]=0,\\
[\mathsf K_\mu^L,\mathsf S_L^a]
=[\mathsf K_\mu^L,\bar{\mathsf S}_L^{\dot a}]=0.
\end{gathered}
\tag{2C.27}
$$

The complete odd sector is

$$
\boxed{
\begin{aligned}
\{\mathsf Q_a^L,\bar{\mathsf Q}_{\dot b}^L\}
&=-2(\sigma_L^\mu)_{a\dot b}\mathsf P_\mu^L,\\
\{\mathsf S_{L,a},\bar{\mathsf S}_{L,\dot b}\}
&=-2(\sigma_L^\mu)_{a\dot b}\mathsf K_\mu^L,\\
\{\mathsf Q_a^L,\mathsf S_L^b\}
&=-2i(\sigma_L^{\mu\nu})_a{}^b\mathsf J_{\mu\nu}^L
-2i\delta_a{}^b\mathsf D_{{\rm dil},L}
+3\delta_a{}^b\mathsf R_L,\\
\{\bar{\mathsf Q}_{\dot a}^L,
\bar{\mathsf S}_L^{\dot b}\}
&=-2i(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}
\mathsf J_{\mu\nu}^L
+2i\delta_{\dot a}{}^{\dot b}\mathsf D_{{\rm dil},L}
+3\delta_{\dot a}{}^{\dot b}\mathsf R_L.
\end{aligned}}
\tag{2C.28}
$$

$$
\begin{gathered}
\{\mathsf Q_a^L,\mathsf Q_b^L\}
=\{\bar{\mathsf Q}_{\dot a}^L,\bar{\mathsf Q}_{\dot b}^L\}=0,\\
\{\mathsf S_{L,a},\mathsf S_{L,b}\}
=\{\bar{\mathsf S}_{L,\dot a},\bar{\mathsf S}_{L,\dot b}\}=0,\\
\{\mathsf Q_a^L,\bar{\mathsf S}_{L,\dot b}\}
=\{\bar{\mathsf Q}_{\dot a}^L,\mathsf S_{L,b}\}=0.
\end{gathered}
\tag{2C.29}
$$

### 2C.4 Coordinate–Noether covariance

Let $\mathscr L_L$ be a fixed set of typed coordinate modules satisfying

$$
\mathcal F^L:=\bigoplus_{\lambda\in\mathscr L_L}\mathcal F_\lambda^L,
\qquad
[\mathsf G_A^{L,[\lambda]},\mathsf G_B^{L,[\lambda]}\}
=f_{AB}{}^C\mathsf G_C^{L,[\lambda]}.
\tag{2C.29a}
$$

The object $\lambda=0$ is (2C.4), with generators (2C.5)--(2C.17).  A scalar chiral-primary object is

$$
\lambda=(\Delta,r)_{\rm ch},
\qquad
r=-\frac23\Delta,
\qquad
\mathcal F_{(\Delta,r)_{\rm ch}}^L
=\mathbb C[y^\mu]\widehat\otimes
\Lambda(\vartheta^1,\vartheta^2),
\tag{2C.29b}
$$

$$
\mathsf G_A^{L,[(0,0)_{\rm ch}]}
:=\left.
\mathsf G_A^{L,[0]}
\right|_{\mathcal F_{(0,0)_{\rm ch}}^L}.
\tag{2C.29ba}
$$

$$
\begin{aligned}
\mathsf D_{{\rm dil},L}^{[(\Delta,r)_{\rm ch}]}
&=\mathsf D_{{\rm dil},L}^{[(0,0)_{\rm ch}]}-i\Delta,\\
\mathsf R_L^{[(\Delta,r)_{\rm ch}]}
&=\mathsf R_L^{[(0,0)_{\rm ch}]}+r,\\
\mathsf K_\mu^{L,[(\Delta,r)_{\rm ch}]}
&=\mathsf K_\mu^{L,[(0,0)_{\rm ch}]}+2i\Delta y_\mu,\\
\mathsf S_L^{a,[(\Delta,r)_{\rm ch}]}
&=\mathsf S_L^{a,[(0,0)_{\rm ch}]}-4i\Delta\vartheta^a.
\end{aligned}
\tag{2C.29c}
$$

For a homogeneous typed local operator

$$
M_{\Phi_{\lambda'\leftarrow\lambda}}:
\mathcal F_\lambda^L\widehat\otimes\mathcal H
\longrightarrow
\mathcal F_{\lambda'}^L\widehat\otimes\mathcal H,
\tag{2C.29d}
$$

covariant functoriality means

$$
\begin{aligned}
0={}&
\left(\mathsf G_A^{L,[\lambda']}\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes G_A^L\right)
M_{\Phi_{\lambda'\leftarrow\lambda}}\\
&-(-1)^{|A||\Phi|}
M_{\Phi_{\lambda'\leftarrow\lambda}}
\left(\mathsf G_A^{L,[\lambda]}\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes G_A^L\right).
\end{aligned}
\tag{2C.29e}
$$

Define the block-diagonal coordinate operator and its diagonal coordinate–Noether sum by

$$
\boldsymbol{\mathsf G}_A^L
:=\bigoplus_{\lambda\in\mathscr L_L}
\mathsf G_A^{L,[\lambda]},
\qquad
\mathbb G_A^L
:=\boldsymbol{\mathsf G}_A^L\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes G_A^L,
\qquad
[\mathbb G_A^L,M_{\Phi_{\lambda'\leftarrow\lambda}}\}=0.
\tag{2C.30}
$$

For translations,

$$
\begin{aligned}
[\boldsymbol{\mathsf P}_\mu^L,
M_{\Phi_{\lambda'\leftarrow\lambda}}]
&=-iM_{\partial_\mu\Phi_{\lambda'\leftarrow\lambda}},\\
[P_\mu^L,M_{\Phi_{\lambda'\leftarrow\lambda}}]
&=+iM_{\partial_\mu\Phi_{\lambda'\leftarrow\lambda}},\\
[\boldsymbol{\mathsf P}_\mu^L\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes P_\mu^L,
M_{\Phi_{\lambda'\leftarrow\lambda}}]
&=0.
\end{aligned}
\tag{2C.30a}
$$

The graded tensor-product multiplication gives

$$
\begin{aligned}
&(\boldsymbol{\mathsf G}_A\widehat\otimes\mathbf1)
(\mathbf1\widehat\otimes G_B)
=\boldsymbol{\mathsf G}_A\widehat\otimes G_B,\\
&(\mathbf1\widehat\otimes G_B)
(\boldsymbol{\mathsf G}_A\widehat\otimes\mathbf1)
=(-1)^{|A||B|}\boldsymbol{\mathsf G}_A\widehat\otimes G_B,
\end{aligned}
\tag{2C.31}
$$

hence

$$
[\mathbb G_A,\mathbb G_B\}
=[\boldsymbol{\mathsf G}_A,\boldsymbol{\mathsf G}_B\}
\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes[G_A,G_B\}.
\tag{2C.32}
$$

Let

$$
[\boldsymbol{\mathsf G}_A,\boldsymbol{\mathsf G}_B\}
=f_{AB}{}^C\boldsymbol{\mathsf G}_C.
\tag{2C.33}
$$

The graded Jacobi identity and (2C.30) give

$$
\begin{aligned}
0
={}&[\mathbb G_A,
[\mathbb G_B,M_{\Phi_{\lambda'\leftarrow\lambda}}\}\}
-(-1)^{|A||B|}
[\mathbb G_B,
[\mathbb G_A,M_{\Phi_{\lambda'\leftarrow\lambda}}\}\}\\
={}&[[\mathbb G_A,\mathbb G_B\},
M_{\Phi_{\lambda'\leftarrow\lambda}}\}.
\end{aligned}
\tag{2C.34}
$$

Subtracting $f_{AB}{}^C[\mathbb G_C,M_\Phi\}=0$ yields

$$
\begin{gathered}
Z_{AB}:=[G_A,G_B\}-f_{AB}{}^CG_C,\\
[\mathbf1\widehat\otimes Z_{AB},
M_{\Phi_{\lambda'\leftarrow\lambda}}\}=0
\quad
\text{for every typed }(\lambda'\leftarrow\lambda).
\end{gathered}
\tag{2C.35}
$$

Fix the local supercommutant and Noether normalization by

$$
\mathcal C_{\rm loc}
:=\left\{Z:
[\mathbf1\widehat\otimes Z,
M_{\Phi_{\lambda'\leftarrow\lambda}}\}=0
\ \text{for every typed }(\lambda'\leftarrow\lambda)\right\}
=\mathbb C\mathbf1,
\tag{2C.36}
$$

$$
G_A|0\rangle=0,
\qquad
\langle0|0\rangle=1,
\qquad
\text{no scalar central cocycle}.
\tag{2C.37}
$$

Odd $Z_{AB}$ vanish by (2C.36).  For even $Z_{AB}=z_{AB}\mathbf1$,

$$
0=Z_{AB}|0\rangle=z_{AB}|0\rangle,
\qquad
z_{AB}=0.
\tag{2C.38}
$$

Therefore

$$
\boxed{
[\boldsymbol{\mathsf G}_A^L,\boldsymbol{\mathsf G}_B^L\}
=f_{AB}{}^C\boldsymbol{\mathsf G}_C^L
\quad\Longrightarrow\quad
[G_A^L,G_B^L\}
=f_{AB}{}^CG_C^L.}
\tag{2C.39}
$$

Thus (2C.21)--(2C.29), with every sans-serif symbol replaced by its Noether symbol, are the Hilbert-space superconformal commutation rules.  The physical adjoints are

$$
\begin{gathered}
(P_\mu^L)^{\dagger_{\mathcal H}}=P_\mu^L,
\quad
(J_{\mu\nu}^L)^{\dagger_{\mathcal H}}=J_{\mu\nu}^L,
\quad
D_{{\rm dil},L}^{\dagger_{\mathcal H}}=D_{{\rm dil},L},
\quad
R_L^{\dagger_{\mathcal H}}=R_L,\\
(K_\mu^L)^{\dagger_{\mathcal H}}=K_\mu^L,
\qquad
(Q_a^L)^{\dagger_{\mathcal H}}=\bar Q_{\dot a}^L,
\qquad
(S_a^L)^{\dagger_{\mathcal H}}=\bar S_{\dot a}^L.
\end{gathered}
\tag{2C.40}
$$

### 2C.5 Euclidean continuation

$$
\begin{gathered}
B_E^m:=\vartheta^a(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b},
\qquad
y_E^m:=x_E^m+B_E^m,
\qquad
\bar y_E^m:=x_E^m-B_E^m,\\
(Y_E)_{a\dot a}:=y_{E,m}(\sigma_E^m)_{a\dot a},
\qquad
\widetilde Y_E^{\dot a a}:=y_{E,m}(\bar\sigma_E^m)^{\dot a a},\\
(\bar Y_E)_{a\dot a}:=\bar y_{E,m}(\sigma_E^m)_{a\dot a},
\qquad
\widetilde{\bar Y}_E^{\dot a a}
:=\bar y_{E,m}(\bar\sigma_E^m)^{\dot a a}.
\end{gathered}
\tag{2C.41}
$$

$$
V_m{}^n(u):=u^2\delta_m{}^n-2u_m u^n.
\tag{2C.42}
$$

The full Euclidean coordinate generators are

$$
\boxed{
\begin{aligned}
\mathsf P_m^E
&=-\partial_m,\\
\mathsf Q_a^E
&=-\partial_a
+(\sigma_E^m)_{a\dot b}\bar\vartheta^{\dot b}\partial_m,\\
\bar{\mathsf Q}_{\dot a}^E
&=+\widetilde{\bar\partial}_{\dot a}
-\vartheta^b(\sigma_E^m)_{b\dot a}\partial_m,\\
\mathsf D_{{\rm dil},E}
&=-\left(
x_E^m\partial_m
+\frac12\vartheta^a\partial_a
+\frac12\bar\vartheta^{\dot a}
\widetilde{\bar\partial}_{\dot a}
\right),\\
\mathsf R_E
&=-i\left(
\vartheta^a\partial_a
-\bar\vartheta^{\dot a}
\widetilde{\bar\partial}_{\dot a}
\right).
\end{aligned}}
\tag{2C.43}
$$

$$
\pi_m^E:=i\mathsf P_m^E=-i\partial_m,
\qquad
\Pi_m^E:=iP_m^E,
\qquad
[\pi_m^E\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes\Pi_m^E,M_{\Phi_E}]=0.
\tag{2C.43a}
$$

$$
\boxed{
\begin{aligned}
\mathsf J_{mn}^E
={}&-i(x_{E,m}\partial_n-x_{E,n}\partial_m)
-i\vartheta^a(\sigma_{E,mn})_a{}^b\partial_b\\
&+i(\bar\sigma_{E,mn})^{\dot a}{}_{\dot b}
\bar\vartheta^{\dot b}
\widetilde{\bar\partial}_{\dot a}.
\end{aligned}}
\tag{2C.44}
$$

Wick transport of (2C.16)--(2C.17) gives

$$
\boxed{
\begin{aligned}
\mathsf K_m^E
={}&-\frac12\left[V_m{}^n(y_E)+V_m{}^n(\bar y_E)\right]\partial_n\\
&+\vartheta^b(\sigma_{E,m}\widetilde Y_E)_b{}^a\partial_a\\
&+\bar\vartheta^{\dot b}
(\widetilde{\bar Y}_E\sigma_{E,m})^{\dot a}{}_{\dot b}
\widetilde{\bar\partial}_{\dot a},
\end{aligned}}
\tag{2C.45}
$$

$$
\boxed{
\begin{aligned}
\mathsf S_E^a
={}&-\vartheta^b(\sigma_E^m\widetilde Y_E)_b{}^a\partial_m
-2\vartheta^2\epsilon^{ab}\partial_b
+\widetilde{\bar Y}_E^{\dot b a}
\widetilde{\bar\partial}_{\dot b},\\
\bar{\mathsf S}_E^{\dot a}
={}&-\bar\vartheta^{\dot b}
(\widetilde{\bar Y}_E\sigma_E^m)^{\dot a}{}_{\dot b}\partial_m
+\widetilde Y_E^{\dot a b}\partial_b
+2\bar\vartheta^2\epsilon^{\dot a\dot b}
\widetilde{\bar\partial}_{\dot b}.
\end{aligned}}
\tag{2C.46}
$$

$$
\mathsf S_{E,a}:=\epsilon_{ab}\mathsf S_E^b,
\qquad
\bar{\mathsf S}_{E,\dot a}
:=\epsilon_{\dot a\dot b}\bar{\mathsf S}_E^{\dot b}.
\tag{2C.46a}
$$

$$
\mathcal I_{s,E}=\mathcal W\mathcal I_{s,L}\mathcal W^{-1},
\qquad
\mathcal I_{s,E}^2=1,
\tag{2C.47}
$$

$$
\mathsf K_m^E
:=\mathcal I_{s,E}^*\mathsf P_m^E\mathcal I_{s,E}^*,
\qquad
\mathsf S_{E,a}
:=\mathcal I_{s,E}^*\mathsf Q_a^E\mathcal I_{s,E}^*,
\qquad
\bar{\mathsf S}_{E,\dot a}
:=\mathcal I_{s,E}^*\bar{\mathsf Q}_{\dot a}^E
\mathcal I_{s,E}^*.
\tag{2C.47a}
$$

$$
\begin{gathered}
\mathsf D_{{\rm dil},E}=-i\mathcal W(\mathsf D_{{\rm dil},L}),
\quad
\mathsf R_E=-i\mathcal W(\mathsf R_L),\\
\mathsf Q_a^E=-i\mathcal W(\mathsf Q_a^L),
\quad
\bar{\mathsf Q}_{\dot a}^E
=-i\mathcal W(\bar{\mathsf Q}_{\dot a}^L),
\quad
\mathsf S_E^a=-i\mathcal W(\mathsf S_L^a),
\quad
\bar{\mathsf S}_E^{\dot a}
=-i\mathcal W(\bar{\mathsf S}_L^{\dot a}).
\end{gathered}
\tag{2C.48}
$$

$$
\begin{aligned}
\mathsf P_i^E&=-i\mathcal W(\mathsf P_i^L),
&\mathsf P_4^E&=-\mathcal W(\mathsf P_0^L),\\
\mathsf K_i^E&=-i\mathcal W(\mathsf K_i^L),
&\mathsf K_4^E&=-\mathcal W(\mathsf K_0^L),\\
\mathsf J_{ij}^E&=\mathcal W(\mathsf J_{ij}^L),
&\mathsf J_{4i}^E&=-i\mathcal W(\mathsf J_{0i}^L).
\end{aligned}
\tag{2C.49}
$$

Let $\mathcal W_{\rm exp}$ denote the componentwise exponent-matched map in (2C.48)--(2C.49).  Define

$$
\mathscr L_E:=\mathcal W_{\rm exp}(\mathscr L_L),
\qquad
\mathcal F^E
:=\bigoplus_{\lambda_E\in\mathscr L_E}
\mathcal F_{\lambda_E}^E,
\qquad
\mathcal F_{\lambda_E}^E
:=\mathcal W_{\rm exp}(\mathcal F_\lambda^L).
\tag{2C.49a}
$$

$$
\begin{gathered}
\mathsf G_A^{E,[\lambda_E]}
:=\mathcal W_{\rm exp}
(\mathsf G_A^{L,[\lambda]}),
\qquad
\boldsymbol{\mathsf G}_A^E
:=\bigoplus_{\lambda_E\in\mathscr L_E}
\mathsf G_A^{E,[\lambda_E]},\\
\mathbb G_A^E
:=\boldsymbol{\mathsf G}_A^E\widehat\otimes\mathbf1
+\mathbf1\widehat\otimes G_A^E,
\qquad
[\mathbb G_A^E,
M_{\Phi_{\lambda_E'\leftarrow\lambda_E}}\}=0.
\end{gathered}
\tag{2C.49b}
$$

### 2C.6 Complete Euclidean coordinate algebra

$$
\begin{aligned}
[\mathsf J_{mn}^E,\mathsf J_{rs}^E]
=i\big(&\delta_{mr}\mathsf J_{ns}^E
-\delta_{nr}\mathsf J_{ms}^E\\
&-\delta_{ms}\mathsf J_{nr}^E
+\delta_{ns}\mathsf J_{mr}^E\big),\\
[\mathsf J_{mn}^E,\mathsf P_r^E]
&=i\delta_{mr}\mathsf P_n^E-i\delta_{nr}\mathsf P_m^E,\\
[\mathsf J_{mn}^E,\mathsf K_r^E]
&=i\delta_{mr}\mathsf K_n^E-i\delta_{nr}\mathsf K_m^E.
\end{aligned}
\tag{2C.50}
$$

$$
\begin{aligned}
[\mathsf D_{{\rm dil},E},\mathsf P_m^E]
&=+\mathsf P_m^E,
&[\mathsf D_{{\rm dil},E},\mathsf K_m^E]
&=-\mathsf K_m^E,\\
[\mathsf P_m^E,\mathsf K_n^E]
&=2\delta_{mn}\mathsf D_{{\rm dil},E}
+2i\mathsf J_{mn}^E.
\end{aligned}
\tag{2C.51}
$$

$$
\begin{gathered}
[\mathsf P_m^E,\mathsf P_n^E]
=[\mathsf K_m^E,\mathsf K_n^E]
=[\mathsf D_{{\rm dil},E},\mathsf J_{mn}^E]
=[\mathsf D_{{\rm dil},E},\mathsf R_E]=0,\\
[\mathsf D_{{\rm dil},E},\mathsf D_{{\rm dil},E}]
=[\mathsf R_E,\mathsf R_E]=0,\\
[\mathsf R_E,\mathsf J_{mn}^E]
=[\mathsf R_E,\mathsf P_m^E]
=[\mathsf R_E,\mathsf K_m^E]=0.
\end{gathered}
\tag{2C.52}
$$

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
\tag{2C.53}
$$

$$
\begin{aligned}
[\mathsf D_{{\rm dil},E},\mathsf Q_a^E]
&=+\frac12\mathsf Q_a^E,
&[\mathsf D_{{\rm dil},E},\bar{\mathsf Q}_{\dot a}^E]
&=+\frac12\bar{\mathsf Q}_{\dot a}^E,\\
[\mathsf D_{{\rm dil},E},\mathsf S_E^a]
&=-\frac12\mathsf S_E^a,
&[\mathsf D_{{\rm dil},E},\bar{\mathsf S}_E^{\dot a}]
&=-\frac12\bar{\mathsf S}_E^{\dot a},\\
[\mathsf R_E,\mathsf Q_a^E]
&=+i\mathsf Q_a^E,
&[\mathsf R_E,\bar{\mathsf Q}_{\dot a}^E]
&=-i\bar{\mathsf Q}_{\dot a}^E,\\
[\mathsf R_E,\mathsf S_E^a]
&=-i\mathsf S_E^a,
&[\mathsf R_E,\bar{\mathsf S}_E^{\dot a}]
&=+i\bar{\mathsf S}_E^{\dot a}.
\end{aligned}
\tag{2C.54}
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
\tag{2C.55}
$$

$$
\begin{gathered}
[\mathsf P_m^E,\mathsf Q_a^E]
=[\mathsf P_m^E,\bar{\mathsf Q}_{\dot a}^E]=0,\\
[\mathsf K_m^E,\mathsf S_E^a]
=[\mathsf K_m^E,\bar{\mathsf S}_E^{\dot a}]=0.
\end{gathered}
\tag{2C.56}
$$

$$
\boxed{
\begin{aligned}
\{\mathsf Q_a^E,\bar{\mathsf Q}_{\dot b}^E\}
&=-2(\sigma_E^m)_{a\dot b}\mathsf P_m^E,\\
\{\mathsf S_{E,a},\bar{\mathsf S}_{E,\dot b}\}
&=-2(\sigma_E^m)_{a\dot b}\mathsf K_m^E,\\
\{\mathsf Q_a^E,\mathsf S_E^b\}
&=-2i(\sigma_E^{mn})_a{}^b\mathsf J_{mn}^E
-2\delta_a{}^b\mathsf D_{{\rm dil},E}
-3i\delta_a{}^b\mathsf R_E,\\
\{\bar{\mathsf Q}_{\dot a}^E,
\bar{\mathsf S}_E^{\dot b}\}
&=-2i(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}\mathsf J_{mn}^E
+2\delta_{\dot a}{}^{\dot b}\mathsf D_{{\rm dil},E}
-3i\delta_{\dot a}{}^{\dot b}\mathsf R_E.
\end{aligned}}
\tag{2C.57}
$$

$$
\begin{gathered}
\{\mathsf Q_a^E,\mathsf Q_b^E\}
=\{\bar{\mathsf Q}_{\dot a}^E,\bar{\mathsf Q}_{\dot b}^E\}=0,\\
\{\mathsf S_{E,a},\mathsf S_{E,b}\}
=\{\bar{\mathsf S}_{E,\dot a},\bar{\mathsf S}_{E,\dot b}\}=0,\\
\{\mathsf Q_a^E,\bar{\mathsf S}_{E,\dot b}\}
=\{\bar{\mathsf Q}_{\dot a}^E,\mathsf S_{E,b}\}=0.
\end{gathered}
\tag{2C.58}
$$

The exponent-normalized and (i)-rescaled Euclidean bases obey

$$
\widehat{\mathsf G}_A^E:=h_A\mathsf G_A^E,
\qquad
h_{J_{mn}}:=1,
\qquad
h_A:=i
\quad
\text{for }
A\in\{P,K,D_{\rm dil},R,Q,\bar Q,S,\bar S\}.
\tag{2C.58a}
$$

$$
[\mathsf G_A^E,\mathsf G_B^E\}
=f_{AB}{}^C\mathsf G_C^E
\quad\Longrightarrow\quad
[\widehat{\mathsf G}_A^E,\widehat{\mathsf G}_B^E\}
=\frac{h_Ah_B}{h_C}f_{AB}{}^C
\widehat{\mathsf G}_C^E.
\tag{2C.58b}
$$

$$
\widehat{\mathsf P}_m^E
=i\mathsf P_m^E
=-i\partial_m
\tag{2C.58c}
$$

is $L^2(\mathbb R^4)$-Hermitian without an additional Berezin pairing.  The rescaling (2C.58a) does not impose an intrinsic Euclidean adjoint on the two Weyl sectors.

With the same local-supercommutant and Noether-normalization conditions as (2C.36)--(2C.38), equations (2C.50)--(2C.58) also hold for the Euclidean Noether charges after removing every sans-serif font.  The two Euclidean Weyl sectors remain independent; no intrinsic Euclidean dagger relation is imposed.

### 2C.7 Exact verification criterion

For $R=L,E$, let

$$
\mathcal B_R
:=\left\{
(\vartheta^1)^{i_1}(\vartheta^2)^{i_2}
(\bar\vartheta^{\dot1})^{j_1}(\bar\vartheta^{\dot2})^{j_2}
w
\;\middle|\;
i_1,i_2,j_1,j_2\in\{0,1\},
\ w\in\mathcal X_R
\right\},
\qquad
\mathcal X_L:=\{1,x^0,x^1,x^2,x^3\},
\qquad
\mathcal X_E:=\{1,x_E^1,x_E^2,x_E^3,x_E^4\}.
\tag{2C.59}
$$

$$
|\mathcal B_L|=|\mathcal B_E|=16\cdot5=80.
\tag{2C.60}
$$

Every difference of two brackets in (2C.21)--(2C.29) or (2C.50)--(2C.58) is a first-order differential operator with exact polynomial coefficients.  Its action on $1$, all four bosonic coordinate generators, and the complete sixteen-dimensional exterior basis determines every derivative coefficient and every zero-order coefficient.  Thus vanishing on (2C.59) is an exact identity test, not sampling.

$$
N_L
=731\cdot80+96+16\cdot20
=58{,}896,
\qquad
N_E=62{,}704.
\tag{2C.61}
$$

$$
\begin{array}{c|c|c|c}
R&\text{Grassmann monomials}&\text{exact cases}&\text{failures}\\ \hline
L&16&58{,}896&0\\
E&16&62{,}704&0
\end{array}
\tag{2C.62}
$$

The exact executables are `scripts/verify_step2c_full_lorentz_superconformal.py` and `scripts/verify_step2c_full_euclidean_superconformal.py`.
