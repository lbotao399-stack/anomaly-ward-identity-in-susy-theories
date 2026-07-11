# 00 3+1d SUSY QFT — Convention Lock

## Step 3B. Component reconstruction of the general gauge–chiral action

### 3B.1 Component slots and ordered projections

$$
R\in\{L,E\},
\qquad
\mathcal M:=\text{chiral target manifold},
\qquad
I,J,K=1,\ldots,\dim_{\mathbb C}\mathcal M,
\qquad
\bar I,\bar J,\bar K=1,\ldots,\dim_{\mathbb C}\mathcal M.
\tag{3B.1}
$$

Normalized symmetrization is

$$
Y_{(a}Z_{b)}:=\frac12(Y_aZ_b+Y_bZ_a),
\qquad
Y_{(A}Z_{B)}:=\frac12(Y_AZ_B+Y_BZ_A).
\tag{3B.1a}
$$

The barred target index labels the antichiral slot.  It is a conjugate
index for $R=L$ and an independent index for $R=E$ before the contour.

$$
\begin{aligned}
\phi^I&:=\Phi^I|,
&\psi_a^I&:=\frac1{\sqrt2}D_a\Phi^I|,
&F^I&:=-\frac14D^2\Phi^I|,\\
\widetilde\phi^{\bar I}&:=\widetilde\Phi^{\bar I}|,
&\widetilde\psi_{\dot a}^{\bar I}
&:=\frac1{\sqrt2}\bar D_{\dot a}\widetilde\Phi^{\bar I}|,
&\widetilde F^{\bar I}&:=-\frac14\bar D^2\widetilde\Phi^{\bar I}|.
\end{aligned}
\tag{3B.2}
$$

$$
[X]_F=-\frac14D^2X|,
\qquad
[\widetilde X]_{\widetilde F}=-\frac14\bar D^2\widetilde X|,
\qquad
[Y]_D=\frac1{16}D^2\bar D^2Y|.
\tag{3B.3}
$$

$$
D^2\vartheta^2=-4,
\qquad
\bar D^2\bar\vartheta^2=-4,
\qquad
[\vartheta^2\bar\vartheta^2]_D=1.
\tag{3B.4}
$$

### 3B.2 Reconstruction of the chiral and antichiral superfields

Define

$$
B_R^M:=\vartheta\sigma_R^M\bar\vartheta,
\qquad
\begin{array}{c|cc}
R&s_R&t_R\\ \hline
L&-i&+i\\
E&+1&-1
\end{array},
\tag{3B.5}
$$

$$
y_R^M=x_R^M+s_RB_R^M,
\qquad
\widetilde y_R^M=x_R^M+t_RB_R^M.
\tag{3B.6}
$$

The Step-2A derivatives give, term by term,

$$
\bar D_{R\dot a}y_R^M=0,
\qquad
D_{Ra}\widetilde y_R^M=0.
\tag{3B.7}
$$

Since $(\vartheta^1)^2=(\vartheta^2)^2=0$, the general solution of
$\bar D_{R\dot a}\Phi_R=0$ is

$$
\Phi_R^I(y_R,\vartheta)
=\mathsf A_R^I(y_R)+\vartheta^a\mathsf B_{Ra}^I(y_R)
+\vartheta^2\mathsf C_R^I(y_R).
\tag{3B.8}
$$

At $\vartheta=\bar\vartheta=0$,

$$
\Phi_R^I|=\mathsf A_R^I,
\qquad
D_{Ra}\Phi_R^I|=\mathsf B_{Ra}^I,
\qquad
D_R^2\Phi_R^I|=-4\mathsf C_R^I.
\tag{3B.9}
$$

Equations (3B.2) and (3B.9) fix

$$
\boxed{
\Phi_R^I(y_R,\vartheta)
=\phi_R^I(y_R)
+\sqrt2\vartheta^a\psi_{Ra}^I(y_R)
+\vartheta^2F_R^I(y_R).}
\tag{3B.10}
$$

The antichiral calculation gives

$$
\boxed{
\widetilde\Phi_R^{\bar I}(\widetilde y_R,\bar\vartheta)
=\widetilde\phi_R^{\bar I}(\widetilde y_R)
+\sqrt2\bar\vartheta_{\dot a}
\widetilde\psi_R^{\dot a\bar I}(\widetilde y_R)
+\bar\vartheta^2\widetilde F_R^{\bar I}(\widetilde y_R).}
\tag{3B.11}
$$

The fermion Taylor term in (3B.10) is

$$
\begin{aligned}
\sqrt2s_R\vartheta^aB_R^M\partial_M\psi_a
&=-\sqrt2s_R\vartheta^a\vartheta^c
(\partial_M\psi_a)(\sigma_R^M)_{c\dot b}
\bar\vartheta^{\dot b}\\
&=\frac{s_R}{\sqrt2}\vartheta^2\epsilon^{ac}
(\partial_M\psi_a)(\sigma_R^M)_{c\dot b}
\bar\vartheta^{\dot b}\\
&=-\frac{s_R}{\sqrt2}\vartheta^2
(\partial_M\psi^c)(\sigma_R^M)_{c\dot b}
\bar\vartheta^{\dot b}.
\end{aligned}
\tag{3B.12}
$$

Similarly,

$$
\sqrt2t_R\bar\vartheta_{\dot a}B_R^M
\partial_M\widetilde\psi^{\dot a}
=-\frac{t_R}{\sqrt2}\vartheta^c
(\sigma_R^M)_{c\dot a}
(\partial_M\widetilde\psi^{\dot a})\bar\vartheta^2.
\tag{3B.13}
$$

Here

$$
\vartheta^a\vartheta^b=-\frac12\epsilon^{ab}\vartheta^2,
\qquad
\bar\vartheta_{\dot a}\bar\vartheta^{\dot b}
=\frac12\delta_{\dot a}{}^{\dot b}\bar\vartheta^2.
\tag{3B.14}
$$

Taylor expansion of (3B.10)--(3B.11) gives

$$
\boxed{
\begin{aligned}
\Phi_L^I={}&\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
-iB_L^\mu\partial_\mu\phi^I\\
&+\frac{i}{\sqrt2}\vartheta^2
(\partial_\mu\psi^{Ia})(\sigma_L^\mu)_{a\dot b}
\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Box_L\phi^I,\\
\bar\Phi_L^{\bar I}={}&\bar\phi^{\bar I}
+\sqrt2\bar\vartheta\bar\psi^{\bar I}
+\bar\vartheta^2\bar F^{\bar I}
+iB_L^\mu\partial_\mu\bar\phi^{\bar I}\\
&-\frac{i}{\sqrt2}\vartheta^a(\sigma_L^\mu)_{a\dot b}
(\partial_\mu\bar\psi^{\dot b\bar I})\bar\vartheta^2
+\frac14\vartheta^2\bar\vartheta^2\Box_L\bar\phi^{\bar I}.
\end{aligned}}
\tag{3B.15}
$$

$$
\boxed{
\begin{aligned}
\Phi_E^I={}&\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
+B_E^m\partial_m\phi^I\\
&-\frac1{\sqrt2}\vartheta^2
(\partial_m\psi^{Ia})(\sigma_E^m)_{a\dot b}
\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Delta_E\phi^I,\\
\widetilde\Phi_E^{\bar I}={}&\widetilde\phi^{\bar I}
+\sqrt2\bar\vartheta\widetilde\psi^{\bar I}
+\bar\vartheta^2\widetilde F^{\bar I}
-B_E^m\partial_m\widetilde\phi^{\bar I}\\
&+\frac1{\sqrt2}\vartheta^a(\sigma_E^m)_{a\dot b}
(\partial_m\widetilde\psi^{\dot b\bar I})\bar\vartheta^2
+\frac14\vartheta^2\bar\vartheta^2\Delta_E
\widetilde\phi^{\bar I}.
\end{aligned}}
\tag{3B.16}
$$

Applying (3B.2) to (3B.15)--(3B.16) returns all six defining
components because

$$
D_a\vartheta^b|=\delta_a{}^b,
\qquad
-\frac14D^2\vartheta^2|=1,
\qquad
-\frac14\bar D^2\bar\vartheta^2|=1.
\tag{3B.17}
$$

The Lorentzian aliases are

$$
\widetilde\Phi_L:=\bar\Phi_L,
\qquad
(\widetilde\phi_L,\widetilde\psi_L,\widetilde F_L)
:=(\bar\phi_L,\bar\psi_L,\bar F_L).
\tag{3B.17a}
$$

### 3B.3 Reconstruction of the bridge and covariant derivatives

Take the general Wess--Zumino polynomial

$$
\mathcal V_R
=c_RB_R^MA_M
+\alpha_R\vartheta^2\bar\vartheta_{\dot a}
\widetilde\lambda^{\dot a}
+\beta_R\bar\vartheta^2\vartheta^a\lambda_a
+\gamma_R\vartheta^2\bar\vartheta^2\mathscr D.
\tag{3B.18}
$$

The vector projection uses

$$
[D_a,\bar D_{\dot b}]_{\rm ord}B_R^M|
=2(\sigma_R^M)_{a\dot b}.
\tag{3B.19}
$$

Therefore

$$
A_\mu^L=-\frac{c_L}{2}A_\mu^L,
\qquad
A_m^E=\frac{ic_E}{2}A_m^E,
\qquad
c_L=-2,
\qquad
c_E=-2i.
\tag{3B.20}
$$

For the chiral gaugino slot,

$$
\mathcal W_a|
=-\frac18\bar D^2D_a
(\beta_R\bar\vartheta^2\vartheta^b\lambda_b)|
=\frac{\beta_R}{2}\lambda_a.
\tag{3B.21}
$$

The definition $\lambda_a=i\mathcal W_a|$ gives

$$
\beta_R=-2i.
\tag{3B.22}
$$

For the antichiral gaugino,

$$
\widetilde\Gamma_{\dot a}
=-\bar D_{\dot a}\mathcal V+\cdots
=-\alpha_R\vartheta^2\widetilde\lambda_{\dot a}+\cdots,
\tag{3B.23}
$$

$$
\widetilde{\mathcal W}_{\dot a}|
=\frac18D^2\widetilde\Gamma_{\dot a}|
=\frac{\alpha_R}{2}\widetilde\lambda_{\dot a}.
\tag{3B.24}
$$

The definition $\widetilde\lambda_{\dot a}
=-i\widetilde{\mathcal W}_{\dot a}|$ gives

$$
\alpha_R=2i.
\tag{3B.25}
$$

Finally,

$$
-\frac12D^a\mathcal W_a|
=\gamma_R\mathscr D,
\qquad
\gamma_R=1.
\tag{3B.26}
$$

Thus

$$
\boxed{
\begin{aligned}
\mathcal V_L={}&-2B_L^\mu A_\mu
+2i\vartheta^2\bar\vartheta\bar\lambda
-2i\bar\vartheta^2\vartheta\lambda
+\vartheta^2\bar\vartheta^2\mathscr D,\\
\mathcal V_E={}&-2iB_E^m A_m
+2i\vartheta^2\bar\vartheta\widetilde\lambda
-2i\bar\vartheta^2\vartheta\lambda
+\vartheta^2\bar\vartheta^2\mathscr D.
\end{aligned}}
\tag{3B.27}
$$

Since $\mathcal V_R^3=0$,

$$
e^{\mathcal V_R}=1+\mathcal V_R+\frac12\mathcal V_R^2,
\qquad
e^{-\mathcal V_R}=1-\mathcal V_R+\frac12\mathcal V_R^2.
\tag{3B.28}
$$

Direct ordered multiplication gives

$$
\boxed{
\begin{aligned}
\Gamma_a
&:=e^{-\mathcal V}D_ae^{\mathcal V}
=D_a\mathcal V+\frac12[D_a\mathcal V,\mathcal V],\\
\widetilde\Gamma_{\dot a}
&:=e^{\mathcal V}\bar D_{\dot a}e^{-\mathcal V}
=-\bar D_{\dot a}\mathcal V
+\frac12[\bar D_{\dot a}\mathcal V,\mathcal V].
\end{aligned}}
\tag{3B.29}
$$

For a homogeneous dual-row superfield $X$, the graded right-module
derivative is

$$
\boxed{
\widetilde\nabla_{\dot a}^{\,\mathrm{row}}X
:=\bar D_{\dot a}X-(-1)^{|X|}X\widetilde\Gamma_{\dot a}.}
\tag{3B.30}
$$

The factor $(-1)^{|X|}$ is required when (3B.30) acts on odd
descendants.  For an even dual row $X$,

$$
\begin{aligned}
\{D_a,\widetilde\nabla_{\dot b}^{\,\mathrm{row}}\}X|
&=\{D_a,\bar D_{\dot b}\}X|-X(D_a\widetilde\Gamma_{\dot b})|.
\end{aligned}
\tag{3B.31}
$$

The connection projections are

$$
\begin{array}{c|cc}
R&\bar D_{\dot b}\Gamma_a|&D_a\widetilde\Gamma_{\dot b}|\\ \hline
L&2(\sigma_L^\mu)_{a\dot b}A_\mu
&2(\sigma_L^\mu)_{a\dot b}A_\mu\\
E&2i(\sigma_E^m)_{a\dot b}A_m
&2i(\sigma_E^m)_{a\dot b}A_m
\end{array}.
\tag{3B.32}
$$

Hence

$$
\boxed{
\begin{aligned}
\{\nabla_{La},\bar D_{L\dot b}\}Y|
&=2i(\sigma_L^\mu)_{a\dot b}(\partial_\mu-iA_\mu)Y,\\
\{\nabla_{Ea},\bar D_{E\dot b}\}Y|
&=-2(\sigma_E^m)_{a\dot b}(\partial_m-iA_m)Y,
\end{aligned}}
\tag{3B.33}
$$

Here $Y$ is a column; $X$ in (3B.34) is a dual row.

$$
\boxed{
\begin{aligned}
\{D_{La},\widetilde\nabla_{L\dot b}^{\,\mathrm{row}}\}X|
&=2i(\sigma_L^\mu)_{a\dot b}(\partial_\mu X+iXA_\mu),\\
\{D_{Ea},\widetilde\nabla_{E\dot b}^{\,\mathrm{row}}\}X|
&=-2(\sigma_E^m)_{a\dot b}(\partial_mX+iXA_m).
\end{aligned}}
\tag{3B.34}
$$

### 3B.4 Reconstruction of both field-strength superfields

$$
\mathcal W_a=-\frac18\bar D^2\Gamma_a,
\qquad
\widetilde{\mathcal W}_{\dot a}
=+\frac18D^2\widetilde\Gamma_{\dot a}.
\tag{3B.35}
$$

$$
\mathcal V_{L,\mathrm{vec}}:=-2B_L^\mu A_\mu,
\qquad
\mathcal V_{E,\mathrm{vec}}:=-2iB_E^mA_m.
\tag{3B.35a}
$$

The vector-linear and ordered quadratic curvature projections are

$$
\begin{array}{c|cc}
R&-\frac18D_{(a}\bar D^2D_{b)}\mathcal V_{R,\mathrm{vec}}|
&-\frac1{16}D_{(a}\bar D^2
[D_{b)}\mathcal V_{R,\mathrm{vec}},\mathcal V_{R,\mathrm{vec}}]|\\ \hline
L&i(\sigma_L^{\mu\nu})_{ab}
(\partial_\mu A_\nu-\partial_\nu A_\mu)
&(\sigma_L^{\mu\nu})_{ab}[A_\mu,A_\nu]\\[1mm]
E&-i(\sigma_E^{mn})_{ab}
(\partial_mA_n-\partial_nA_m)
&-(\sigma_E^{mn})_{ab}[A_m,A_n]
\end{array}.
\tag{3B.36}
$$

Therefore

$$
F_{MN}=\partial_MA_N-\partial_NA_M-i[A_M,A_N].
\tag{3B.37}
$$

The chiral-coordinate results are

$$
\boxed{
\begin{aligned}
\mathcal W_{La}={}&-i\lambda_a+\vartheta_a\mathscr D
+i(\sigma_L^{\mu\nu})_a{}^b\vartheta_bF_{\mu\nu}
-\vartheta^2(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{\dot b},\\
\widetilde{\mathcal W}_{L\dot a}={}&
+i\bar\lambda_{\dot a}+\bar\vartheta_{\dot a}\mathscr D
+i\bar\vartheta_{\dot b}
(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}F_{\mu\nu}
-\bar\vartheta^2(\sigma_L^\mu)_{b\dot a}
\mathcal D_\mu\lambda^b.
\end{aligned}}
\tag{3B.38}
$$

$$
\boxed{
\begin{aligned}
\mathcal W_{Ea}={}&-i\lambda_a+\vartheta_a\mathscr D
-i(\sigma_E^{mn})_a{}^b\vartheta_bF_{mn}
-i\vartheta^2(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{\dot b},\\
\widetilde{\mathcal W}_{E\dot a}={}&
+i\widetilde\lambda_{\dot a}+\bar\vartheta_{\dot a}\mathscr D
-i\bar\vartheta_{\dot b}
(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}F_{mn}
-i\bar\vartheta^2(\sigma_E^m)_{b\dot a}
\mathcal D_m\lambda^b.
\end{aligned}}
\tag{3B.39}
$$

They invert to

$$
i\mathcal W_a|=\lambda_a,
\qquad
-i\widetilde{\mathcal W}_{\dot a}|=\widetilde\lambda_{\dot a},
\qquad
-\frac12D^a\mathcal W_a|
=+\frac12\bar D^{\dot a}\widetilde{\mathcal W}_{\dot a}|
=\mathscr D.
\tag{3B.40}
$$

### 3B.5 Raw Kähler Taylor expansion

Set

$$
u^I:=\Phi^I-\phi^I,
\qquad
\widetilde u^{\bar I}:=\widetilde\Phi^{\bar I}
-\widetilde\phi^{\bar I},
\tag{3B.41}
$$

$$
K_{I_1\cdots I_p\bar J_1\cdots\bar J_q}
:=\partial_{I_1}\cdots\partial_{I_p}
\partial_{\bar J_1}\cdots\partial_{\bar J_q}K
\Big|_{(\phi,\widetilde\phi)}.
\tag{3B.42}
$$

The finite Taylor series is

$$
K(\widetilde\Phi,\Phi)
=\sum_{p+q\leq4}\frac1{p!q!}
K_{I_1\cdots I_p\bar J_1\cdots\bar J_q}
u^{I_1}\cdots u^{I_p}
\widetilde u^{\bar J_1}\cdots\widetilde u^{\bar J_q}.
\tag{3B.43}
$$

The products needed for the Lorentzian top component are

$$
B_L^\mu B_L^\nu
=-\frac12\eta^{\mu\nu}\vartheta^2\bar\vartheta^2,
\qquad
(\vartheta\psi^I)(\vartheta\psi^J)
=-\frac12\vartheta^2\psi^I\psi^J,
\tag{3B.44}
$$

$$
(\bar\vartheta\bar\psi^{\bar I})
(\bar\vartheta\bar\psi^{\bar J})
=-\frac12\bar\vartheta^2
\bar\psi^{\bar I}\bar\psi^{\bar J},
\tag{3B.45}
$$

$$
B_L^\mu(\vartheta\psi^I)
(\bar\vartheta\bar\psi^{\bar J})
=-\frac14\vartheta^2\bar\vartheta^2
\bar\psi^{\bar J}\bar\sigma_L^\mu\psi^I.
\tag{3B.46}
$$

Equations (3B.15) and (3B.43)--(3B.46) give the complete raw
Lorentzian coefficient

$$
\boxed{
\begin{aligned}
\mathcal L_{K,L}^{\rm raw}={}&
\frac14K_I\Box_L\phi^I
+\frac14K_{\bar I}\Box_L\bar\phi^{\bar I}
+\frac14K_{IJ}\partial_\mu\phi^I\partial^\mu\phi^J\\
&+\frac14K_{\bar I\bar J}
\partial_\mu\bar\phi^{\bar I}\partial^\mu\bar\phi^{\bar J}
-\frac12K_{I\bar J}\partial_\mu\phi^I
\partial^\mu\bar\phi^{\bar J}
+K_{I\bar J}F^I\bar F^{\bar J}\\
&+\frac i2K_{I\bar J}\bar\psi^{\bar J}
\bar\sigma_L^\mu\partial_\mu\psi^I
-\frac i2K_{I\bar J}(\partial_\mu\bar\psi^{\bar J})
\bar\sigma_L^\mu\psi^I\\
&+\frac i2K_{IJ\bar K}(\partial_\mu\phi^I)
\bar\psi^{\bar K}\bar\sigma_L^\mu\psi^J
-\frac i2K_{I\bar J\bar K}(\partial_\mu\bar\phi^{\bar J})
\bar\psi^{\bar K}\bar\sigma_L^\mu\psi^I\\
&-\frac12K_{IJ\bar K}\psi^I\psi^J\bar F^{\bar K}
-\frac12K_{I\bar J\bar K}F^I
\bar\psi^{\bar J}\bar\psi^{\bar K}\\
&+\frac14K_{IJ\bar K\bar L}
\psi^I\psi^J\bar\psi^{\bar K}\bar\psi^{\bar L}.
\end{aligned}}
\tag{3B.47}
$$

Every $K_{IJK\bar L}$ term contains $\vartheta^3$ and every
$K_{I\bar J\bar K\bar L}$ term contains $\bar\vartheta^3$; both are
zero.

The scalar integrations by parts are

$$
\begin{aligned}
\int\frac14K_I\Box\phi^I
&=-\int\frac14
\left(K_{IJ}\partial_\mu\phi^J
+K_{I\bar J}\partial_\mu\bar\phi^{\bar J}\right)
\partial^\mu\phi^I,\\
\int\frac14K_{\bar I}\Box\bar\phi^{\bar I}
&=-\int\frac14
\left(K_{J\bar I}\partial_\mu\phi^J
+K_{\bar I\bar J}\partial_\mu\bar\phi^{\bar J}\right)
\partial^\mu\bar\phi^{\bar I}.
\end{aligned}
\tag{3B.48}
$$

Thus the two pure terms cancel and the three mixed halves give

$$
-\frac14K_{I\bar J}\partial\phi^I\partial\bar\phi^{\bar J}
-\frac14K_{I\bar J}\partial\phi^I\partial\bar\phi^{\bar J}
-\frac12K_{I\bar J}\partial\phi^I\partial\bar\phi^{\bar J}
=-K_{I\bar J}\partial\bar\phi^{\bar J}\partial\phi^I.
\tag{3B.49}
$$

For the fermions,

$$
\begin{aligned}
&\int-\frac i2K_{I\bar J}
(\partial_\mu\bar\psi^{\bar J})\bar\sigma_L^\mu\psi^I\\
&=\int\left[
+\frac i2K_{I\bar J}\bar\psi^{\bar J}
\bar\sigma_L^\mu\partial_\mu\psi^I
+\frac i2(\partial_\mu K_{I\bar J})
\bar\psi^{\bar J}\bar\sigma_L^\mu\psi^I
\right],
\end{aligned}
\tag{3B.50}
$$

$$
\partial_\mu K_{I\bar J}
=K_{IK\bar J}\partial_\mu\phi^K
+K_{I\bar J\bar K}\partial_\mu\bar\phi^{\bar K}.
\tag{3B.51}
$$

After (3B.51) is substituted into (3B.50), its
$K_{I\bar J\bar K}\partial\bar\phi^{\bar K}$ contribution cancels the
matching term in (3B.47), while its
$K_{IK\bar J}\partial\phi^K$ contribution adds to it.  Hence

$$
iK_{I\bar J}\bar\psi^{\bar J}\bar\sigma_L^\mu
\partial_\mu\psi^I
+iK_{IK\bar J}(\partial_\mu\phi^K)
\bar\psi^{\bar J}\bar\sigma_L^\mu\psi^I.
\tag{3B.52}
$$

### 3B.6 Kähler connection, curvature, and auxiliary reorganization

Define

$$
g_{I\bar J}:=K_{I\bar J},
\qquad
g^{I\bar K}g_{J\bar K}=\delta^I{}_J,
\tag{3B.53}
$$

$$
\mathring\Gamma^I{}_{JK}:=g^{I\bar L}K_{JK\bar L},
\qquad
\widetilde{\mathring\Gamma}^{\bar I}{}_{\bar J\bar K}
:=g^{L\bar I}K_{L\bar J\bar K},
\tag{3B.54}
$$

$$
R_{I\bar J K\bar L}
:=K_{IK\bar J\bar L}
-K_{IK\bar N}g^{M\bar N}K_{M\bar J\bar L}.
\tag{3B.55}
$$

The shifted auxiliaries are

$$
\widehat F^I
:=F^I-\frac12\mathring\Gamma^I{}_{JK}\psi^J\psi^K,
\qquad
\widehat{\bar F}^{\bar I}
:=\bar F^{\bar I}
-\frac12\widetilde{\mathring\Gamma}^{\bar I}{}_{\bar J\bar K}
\bar\psi^{\bar J}\bar\psi^{\bar K}.
\tag{3B.56}
$$

Direct expansion gives

$$
\begin{aligned}
&g_{I\bar J}\widehat F^I\widehat{\bar F}^{\bar J}
+\frac14R_{I\bar J K\bar L}
\psi^I\psi^K\bar\psi^{\bar J}\bar\psi^{\bar L}\\
&=g_{I\bar J}F^I\bar F^{\bar J}
-\frac12K_{IK\bar J}\psi^I\psi^K\bar F^{\bar J}
-\frac12K_{I\bar J\bar L}F^I
\bar\psi^{\bar J}\bar\psi^{\bar L}\\
&\quad
+\frac14K_{IK\bar J\bar L}
\psi^I\psi^K\bar\psi^{\bar J}\bar\psi^{\bar L}.
\end{aligned}
\tag{3B.57}
$$

Thus the ungauged result is

$$
\boxed{
\begin{aligned}
\mathcal L_{K,L}^{A=0}={}&
-g_{I\bar J}\partial_\mu\bar\phi^{\bar J}
\partial^\mu\phi^I
+ig_{I\bar J}\bar\psi^{\bar J}\bar\sigma_L^\mu
\left(\partial_\mu\psi^I
+\mathring\Gamma^I{}_{JK}\partial_\mu\phi^J\psi^K\right)\\
&+g_{I\bar J}\widehat F^I\widehat{\bar F}^{\bar J}
+\frac14R_{I\bar J K\bar L}
\psi^I\psi^K\bar\psi^{\bar J}\bar\psi^{\bar L}.
\end{aligned}}
\tag{3B.58}
$$

### 3B.7 Gauge completion and the moment map

Let

$$
X_A^I:=i(T_A)^I{}_J\phi^J,
\qquad
\bar X_A^{\bar I}
:=-i\bar\phi^{\bar J}(T_A)_{\bar J}{}^{\bar I},
\qquad
(T_A)_{\bar J}{}^{\bar I}
:=\bigl((T_A)^I{}_J\bigr)^*.
\tag{3B.59}
$$

The infinitesimal Kähler shift is

$$
X_A^IK_I+\bar X_A^{\bar I}K_{\bar I}
=r_A(\phi)+\bar r_A(\bar\phi).
\tag{3B.60}
$$

Define

$$
\boxed{
\mu_A:=-i(X_A^IK_I-r_A)
=+i(\bar X_A^{\bar I}K_{\bar I}-\bar r_A).}
\tag{3B.61}
$$

Since $X_A$ and $r_A$ are holomorphic,

$$
\mu_{A,\bar J}
=-iX_A^I\partial_{\bar J}K_I
=-ig_{I\bar J}X_A^I.
\tag{3B.62}
$$

Using the second form of (3B.61),

$$
\mu_{A,I}
=+i\bar X_A^{\bar J}\partial_IK_{\bar J}
=+ig_{I\bar J}\bar X_A^{\bar J}.
\tag{3B.63}
$$

Define the holomorphic and antichiral target vector fields

$$
\mathbf X_A:=X_A^I\partial_I,
\qquad
\bar{\mathbf X}_A:=\bar X_A^{\bar I}\partial_{\bar I}.
\tag{3B.63a}
$$

Differentiating (3B.62) gives

$$
\boxed{
\mu_{A,I\bar J}
=-ig_{K\bar J}
\left(\partial_IX_A^K+\mathring\Gamma^K{}_{IL}X_A^L\right).}
\tag{3B.64}
$$

The local complexified antichiral bridge path is

$$
\begin{aligned}
\mathscr K_g={}&K
+i\mathcal V^A(\bar{\mathbf X}_AK-\bar r_A)\\
&-\frac14\mathcal V^A\mathcal V^B\Big[
\bar{\mathbf X}_A(\bar{\mathbf X}_BK-\bar r_B)
+\bar{\mathbf X}_B(\bar{\mathbf X}_AK-\bar r_A)\Big].
\end{aligned}
\tag{3B.64a}
$$

At the component point,

$$
\bar{\mathbf X}_BK-\bar r_B=-i\mu_B,
\qquad
\bar{\mathbf X}_A\mu_B
=-ig_{I\bar J}X_B^I\bar X_A^{\bar J}.
\tag{3B.64b}
$$

Therefore

$$
\begin{aligned}
i\mathcal V^A(\bar{\mathbf X}_AK-\bar r_A)
&=\mathcal V^A\mu_A,\\
-\frac14\mathcal V^A\mathcal V^B\Big[
\bar{\mathbf X}_A(\bar{\mathbf X}_BK-\bar r_B)
+\bar{\mathbf X}_B(\bar{\mathbf X}_AK-\bar r_A)\Big]
&=\frac12\mathcal V^A\mathcal V^B
g_{I\bar J}X_{(A}^I\bar X_{B)}^{\bar J}.
\end{aligned}
\tag{3B.64c}
$$

The functions in (3B.65) are their superfield lifts; a vertical bar
returns the component functions in (3B.53)--(3B.64):

$$
\boxed{
\mathscr K_g
=K+\mathcal V^A\mu_A
+\frac12\mathcal V^A\mathcal V^B
g_{I\bar J}X_{(A}^I\bar X_{B)}^{\bar J}.}
\tag{3B.65}
$$

Direct Wess--Zumino multiplication gives

$$
\boxed{
\begin{aligned}
[\mathcal V^A\mu_A]_D={}&
\mu_A\mathscr D^A
+i\sqrt2\mu_{A,I}\lambda^{Aa}\psi_a^I
-i\sqrt2\mu_{A,\bar I}
\bar\psi_{\dot a}^{\bar I}\bar\lambda^{A\dot a}\\
&-iA_\mu^A\mu_{A,I}\partial^\mu\phi^I
+iA_\mu^A\mu_{A,\bar I}
\partial^\mu\bar\phi^{\bar I}\\
&+A_\mu^A\mu_{A,I\bar J}
\bar\psi^{\bar J}\bar\sigma_L^\mu\psi^I,
\end{aligned}}
\tag{3B.66}
$$

$$
\boxed{
\left[
\frac12\mathcal V^A\mathcal V^B
g_{I\bar J}X_{(A}^I\bar X_{B)}^{\bar J}
\right]_D
=-A_\mu^AA^{B\mu}g_{I\bar J}
\bar X_A^{\bar J}X_B^I.}
\tag{3B.67}
$$

Define

$$
\begin{aligned}
(\mathcal D_\mu\phi)^I
&:=\partial_\mu\phi^I-A_\mu^AX_A^I,\\
(\mathcal D_\mu\bar\phi)^{\bar I}
&:=\partial_\mu\bar\phi^{\bar I}-A_\mu^A\bar X_A^{\bar I},\\
(\mathfrak D_\mu\psi)^I
&:=\partial_\mu\psi^I
+\mathring\Gamma^I{}_{JK}(\mathcal D_\mu\phi)^J\psi^K
-A_\mu^A(\partial_JX_A^I)\psi^J.
\end{aligned}
\tag{3B.68}
$$

Equations (3B.58), (3B.62)--(3B.68) give

$$
\boxed{
\begin{aligned}
\mathcal L_{K,L}={}&
-g_{I\bar J}(\mathcal D_\mu\bar\phi)^{\bar J}
(\mathcal D^\mu\phi)^I
+ig_{I\bar J}\bar\psi^{\bar J}\bar\sigma_L^\mu
(\mathfrak D_\mu\psi)^I\\
&+g_{I\bar J}\widehat F^I\widehat{\bar F}^{\bar J}
+\frac14R_{I\bar J K\bar L}
\psi^I\psi^K\bar\psi^{\bar J}\bar\psi^{\bar L}\\
&+\mu_A\mathscr D^A
+i\sqrt2\mu_{A,I}\lambda^A\psi^I
-i\sqrt2\mu_{A,\bar I}\bar\psi^{\bar I}\bar\lambda^A.
\end{aligned}}
\tag{3B.69}
$$

The FI term replaces

$$
\mu_A\longmapsto\mathcal P_A:=\mu_A+\xi_A,
\qquad
\xi_Ac_{BC}{}^A=0,
\tag{3B.70}
$$

only in the $\mathscr D^A$ coefficient.

The calculation is local on a Kähler patch.

Equations (3B.62)--(3B.63) give

$$
\begin{aligned}
(\mathbf X_A+\bar{\mathbf X}_A)\mu_B
&=ig_{I\bar J}
\left(X_A^I\bar X_B^{\bar J}-X_B^I\bar X_A^{\bar J}\right).
\end{aligned}
\tag{3B.70b}
$$

Let

$$
\omega:=ig_{I\bar J}d\phi^I\wedge d\bar\phi^{\bar J},
\qquad
\mathbf K_A:=\mathbf X_A+\bar{\mathbf X}_A.
\tag{3B.70b1}
$$

$$
\iota_{\mathbf K}:=\text{contraction by }\mathbf K,
\qquad
\mathcal L_{\mathbf K}:=d\iota_{\mathbf K}+\iota_{\mathbf K}d.
\tag{3B.70b1a}
$$

Equations (3B.62)--(3B.63), the gauge-isometry condition, and the
generator algebra give

$$
d\mu_B=-\iota_{\mathbf K_B}\omega,
\qquad
\mathcal L_{\mathbf K_A}\omega=0,
\qquad
[\mathbf K_A,\mathbf K_B]=c_{AB}{}^C\mathbf K_C.
\tag{3B.70b2}
$$

Therefore

$$
\begin{aligned}
d(\mathbf K_A\mu_B)
&=\mathcal L_{\mathbf K_A}d\mu_B\\
&=-\mathcal L_{\mathbf K_A}\iota_{\mathbf K_B}\omega\\
&=-\iota_{[\mathbf K_A,\mathbf K_B]}\omega
-\iota_{\mathbf K_B}\mathcal L_{\mathbf K_A}\omega\\
&=-c_{AB}{}^C\iota_{\mathbf K_C}\omega
=c_{AB}{}^Cd\mu_C.
\end{aligned}
\tag{3B.70b3}
$$

The gauge lift sets the real constant cocycle in (3B.70b) to zero:

$$
\boxed{
(\mathbf X_A+\bar{\mathbf X}_A)\mu_B
=c_{AB}{}^C\mu_C.}
\tag{3B.70c}
$$

The shift $\mu_A\mapsto\mu_A+\xi_A$ preserves (3B.70c) exactly when
$\xi_Ac_{BC}{}^A=0$.

### 3B.8 Superpotential

With

$$
\delta\Phi^I=\sqrt2\vartheta\psi^I+\vartheta^2F^I,
\tag{3B.71}
$$

$$
\begin{aligned}
\frac12\mathscr U_{IJ}\delta\Phi^I\delta\Phi^J
\Big|_{\vartheta^2}
&=\mathscr U_{IJ}
(\vartheta\psi^I)(\vartheta\psi^J)
\Big|_{\vartheta^2}\\
&=-\frac12\mathscr U_{IJ}\psi^I\psi^J.
\end{aligned}
\tag{3B.72}
$$

Therefore

$$
\boxed{
\begin{aligned}
[\mathscr U(\Phi)]_F
&=\mathscr U_IF^I-\frac12\mathscr U_{IJ}\psi^I\psi^J,\\
[\bar{\mathscr U}(\bar\Phi)]_{\widetilde F}
&=\bar{\mathscr U}_{\bar I}\bar F^{\bar I}
-\frac12\bar{\mathscr U}_{\bar I\bar J}
\bar\psi^{\bar I}\bar\psi^{\bar J}.
\end{aligned}}
\tag{3B.73}
$$

### 3B.9 Field-dependent gauge-kinetic matrix

For $f_{AB}=f_{BA}$,

$$
\boxed{
\begin{aligned}
f_{AB}(\Phi)={}&f_{AB}
+\sqrt2\vartheta^af_{AB,I}\psi_a^I\\
&+\vartheta^2
\left(f_{AB,I}F^I
-\frac12f_{AB,IJ}\psi^I\psi^J\right).
\end{aligned}}
\tag{3B.74}
$$

Write

$$
\mathcal W_{La}^A
=w_a^A+\vartheta^b\mathsf M^A_{L,ba}
+\vartheta^2\rho_a^A,
\tag{3B.75}
$$

$$
\begin{aligned}
w_a^A&=-i\lambda_a^A,\\
\rho_a^A&=-(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{A\dot b},\\
\mathsf M^A_{L,b}{}^a
&:=\epsilon^{ac}\mathsf M^A_{L,bc}
=\delta_b{}^a\mathscr D^A
-i(\sigma_L^{\mu\nu})_b{}^aF_{\mu\nu}^A.
\end{aligned}
\tag{3B.76}
$$

For

$$
\mathcal X_L^{AB}:=\mathcal W_L^{Aa}\mathcal W^B_{La}
=x_L^{AB}+\vartheta^b\zeta_{L,b}^{AB}
+\vartheta^2Z_L^{AB},
\tag{3B.77}
$$

direct multiplication gives

$$
x_L^{AB}=-\lambda^A\lambda^B.
\tag{3B.78}
$$

Before the symmetric gauge-index contraction,

$$
\begin{aligned}
\zeta_{L,b}^{AB}
&=-w^{Aa}\mathsf M^B_{L,ba}
+\mathsf M^A_{L,b}{}^aw_a^B\\
&=+i\lambda^{Aa}\mathsf M^B_{L,ba}
-i\mathsf M^A_{L,b}{}^a\lambda_a^B.
\end{aligned}
\tag{3B.78a}
$$

Since

$$
\mathsf M_{L,ba}\lambda^a
=-\mathsf M_{L,b}{}^a\lambda_a,
\qquad
f_{AB,I}=f_{BA,I},
\tag{3B.78b}
$$

renaming $A\leftrightarrow B$ in the first term gives

$$
f_{AB,I}\zeta_{L,b}^{AB}
=-2if_{AB,I}\mathsf M^A_{L,b}{}^a\lambda_a^B.
\tag{3B.78c}
$$

$$
\boxed{
\begin{aligned}
Z_L^{AB}={}&
\mathscr D^A\mathscr D^B
-\frac12F_{\mu\nu}^AF^{B\mu\nu}
+\frac i4\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B\\
&+i\lambda^A\sigma_L^\mu\mathcal D_\mu\bar\lambda^B
+i\lambda^B\sigma_L^\mu\mathcal D_\mu\bar\lambda^A.
\end{aligned}}
\tag{3B.79}
$$

Since

$$
[(\vartheta\chi)(\vartheta\zeta)]_{\vartheta^2}
=-\frac12\chi^a\zeta_a,
\tag{3B.80}
$$

the complete chiral density is

$$
\boxed{
\begin{aligned}
\mathcal C_{L,f}
:={}&[f_{AB}(\Phi)\mathcal W_L^{Aa}\mathcal W^B_{La}]_F\\
={}&f_{AB}Z_L^{AB}
-f_{AB,I}F^I\lambda^A\lambda^B
+\frac12f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B\\
&+i\sqrt2f_{AB,I}\psi^I\lambda^B\mathscr D^A
+\sqrt2f_{AB,I}\psi^I\sigma_L^{\mu\nu}
\lambda^B F_{\mu\nu}^A.
\end{aligned}}
\tag{3B.81}
$$

For the ordered antichiral multiplication, define

$$
\widetilde{\mathsf M}_{L}{}^{\dot b}{}_{\dot a}
:=\delta^{\dot b}{}_{\dot a}\mathscr D
+i(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}F_{\mu\nu}.
\tag{3B.81a}
$$

The linear coefficient obeys

$$
\bar f_{AB,\bar I}\bar\zeta_L^{AB\dot b}
=+2i\bar f_{AB,\bar I}
\widetilde{\mathsf M}_{L}^{A\dot b}{}_{\dot a}
\bar\lambda^{B\dot a}.
\tag{3B.81b}
$$

Hence

$$
\begin{aligned}
&-\frac1{\sqrt2}\bar f_{AB,\bar I}
\bar\psi_{\dot b}^{\bar I}\bar\zeta_L^{AB\dot b}\\
&=-i\sqrt2\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\lambda^B\mathscr D^A
+\sqrt2\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\sigma_L^{\mu\nu}
\bar\lambda^BF_{\mu\nu}^A.
\end{aligned}
\tag{3B.81c}
$$

The remaining antichiral coefficients give

$$
\boxed{
\begin{aligned}
\bar Z_L^{AB}={}&
\mathscr D^A\mathscr D^B
-\frac12F_{\mu\nu}^AF^{B\mu\nu}
-\frac i4\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B\\
&+i\bar\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B
+i\bar\lambda^B\bar\sigma_L^\mu\mathcal D_\mu\lambda^A,
\end{aligned}}
\tag{3B.82}
$$

$$
\boxed{
\begin{aligned}
\bar{\mathcal C}_{L,\bar f}={}&
\bar f_{AB}\bar Z_L^{AB}
-\bar f_{AB,\bar I}\bar F^{\bar I}
\bar\lambda^A\bar\lambda^B\\
&+\frac12\bar f_{AB,\bar I\bar J}
\bar\psi^{\bar I}\bar\psi^{\bar J}
\bar\lambda^A\bar\lambda^B\\
&-i\sqrt2\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\lambda^B\mathscr D^A
+\sqrt2\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\sigma_L^{\mu\nu}
\bar\lambda^B F_{\mu\nu}^A.
\end{aligned}}
\tag{3B.83}
$$

Thus

$$
\boxed{
\mathcal L_{L,f}=\frac14\mathcal C_{L,f}
+\frac14\bar{\mathcal C}_{L,\bar f}.}
\tag{3B.84}
$$

With

$$
\mathfrak h_{AB}:=\frac12(f_{AB}+\bar f_{AB}),
\qquad
\mathfrak k_{AB}:=\frac1{2i}(f_{AB}-\bar f_{AB}),
\tag{3B.85}
$$

equation (3B.84) is

$$
\boxed{
\begin{aligned}
\mathcal L_{L,f}={}&
-\frac14\mathfrak h_{AB}F_{\mu\nu}^AF^{B\mu\nu}
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B
+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&+\frac i2f_{AB}\lambda^A\sigma_L^\mu
\mathcal D_\mu\bar\lambda^B
+\frac i2\bar f_{AB}\bar\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B\\
&-\frac14f_{AB,I}F^I\lambda^A\lambda^B
-\frac14\bar f_{AB,\bar I}\bar F^{\bar I}
\bar\lambda^A\bar\lambda^B\\
&+\frac18f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B
+\frac18\bar f_{AB,\bar I\bar J}
\bar\psi^{\bar I}\bar\psi^{\bar J}
\bar\lambda^A\bar\lambda^B\\
&+\frac{i}{2\sqrt2}f_{AB,I}\psi^I\lambda^B\mathscr D^A
-\frac{i}{2\sqrt2}\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\lambda^B\mathscr D^A\\
&+\frac1{2\sqrt2}f_{AB,I}
\psi^I\sigma_L^{\mu\nu}\lambda^B F_{\mu\nu}^A
+\frac1{2\sqrt2}\bar f_{AB,\bar I}
\bar\psi^{\bar I}\bar\sigma_L^{\mu\nu}
\bar\lambda^B F_{\mu\nu}^A.
\end{aligned}}
\tag{3B.86}
$$

Gauge covariance of $f_{AB}$ gives

$$
\begin{aligned}
\mathcal D_\mu f_{AB}
&:=\partial_\mu f_{AB}
-A_\mu^C\left(c_{CA}{}^Df_{DB}+c_{CB}{}^Df_{AD}\right)\\
&=f_{AB,I}\partial_\mu\phi^I
-A_\mu^CX_C^If_{AB,I}\\
&=f_{AB,I}(\mathcal D_\mu\phi)^I.
\end{aligned}
\tag{3B.86a}
$$

The contraction $f_{AB}\lambda^A\sigma_L^\mu\bar\lambda^B$ is a
gauge scalar.  The integrated ordering change follows from the ordinary
total derivative

$$
\begin{aligned}
0={}&\int d^4x_L\,\mathcal D_\mu
\left(f_{AB}\lambda^A\sigma_L^\mu\bar\lambda^B\right)\\
={}&\int d^4x_L\Big[
(\mathcal D_\mu f_{AB})\lambda^A\sigma_L^\mu\bar\lambda^B
-f_{AB}\bar\lambda^B\bar\sigma_L^\mu\mathcal D_\mu\lambda^A\\
&\hspace{42mm}
+f_{AB}\lambda^A\sigma_L^\mu\mathcal D_\mu\bar\lambda^B
\Big].
\end{aligned}
\tag{3B.86b}
$$

Consequently

$$
\begin{aligned}
&\int d^4x_L\left[
\frac i2f_{AB}\lambda^A\sigma_L^\mu\mathcal D_\mu\bar\lambda^B
+\frac i2\bar f_{AB}\bar\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B\right]\\
&=\int d^4x_L\left[
i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B
-\frac i2f_{AB,I}(\mathcal D_\mu\phi)^I
\lambda^A\sigma_L^\mu\bar\lambda^B
\right].
\end{aligned}
\tag{3B.86c}
$$

### 3B.10 Complete Lorentzian off-shell action

Combining (3B.69), (3B.70), (3B.73), and (3B.86),

$$
\boxed{
\begin{aligned}
\mathcal L_L={}&
-g_{I\bar J}(\mathcal D_\mu\bar\phi)^{\bar J}
(\mathcal D^\mu\phi)^I
+ig_{I\bar J}\bar\psi^{\bar J}\bar\sigma_L^\mu
(\mathfrak D_\mu\psi)^I\\
&+g_{I\bar J}\widehat F^I\widehat{\bar F}^{\bar J}
+\frac14R_{I\bar J K\bar L}
\psi^I\psi^K\bar\psi^{\bar J}\bar\psi^{\bar L}\\
&+\mathcal P_A\mathscr D^A
+i\sqrt2\mu_{A,I}\lambda^A\psi^I
-i\sqrt2\mu_{A,\bar I}\bar\psi^{\bar I}\bar\lambda^A\\
&+\mathscr U_IF^I-\frac12\mathscr U_{IJ}\psi^I\psi^J
+\bar{\mathscr U}_{\bar I}\bar F^{\bar I}
-\frac12\bar{\mathscr U}_{\bar I\bar J}
\bar\psi^{\bar I}\bar\psi^{\bar J}\\
&+\mathcal L_{L,f}.
\end{aligned}}
\tag{3B.87}
$$

All fields in (3B.87) are off shell.

The gauge-invariance conditions used in (3B.68), (3B.86a), and
(3B.87) are

$$
X_A^I\mathscr U_I=0,
\qquad
X_C^If_{AB,I}
-c_{CA}{}^Df_{DB}
-c_{CB}{}^Df_{AD}=0.
\tag{3B.87a}
$$

### 3B.11 Independent Euclidean multiplication

The direct Euclidean Taylor products use

$$
B_E^mB_E^n
=+\frac12\delta^{mn}\vartheta^2\bar\vartheta^2
\tag{3B.88}
$$

and (3B.16).  Including the overall minus sign in the Euclidean
superspace action, the raw density is

$$
\boxed{
\begin{aligned}
\mathcal L_{K,E}^{\rm raw}={}&
-\frac14K_I\Delta_E\phi^I
-\frac14K_{\bar I}\Delta_E\widetilde\phi^{\bar I}
-\frac14K_{IJ}\partial_m\phi^I\partial_m\phi^J\\
&-\frac14K_{\bar I\bar J}
\partial_m\widetilde\phi^{\bar I}
\partial_m\widetilde\phi^{\bar J}
+\frac12g_{I\bar J}\partial_m\phi^I
\partial_m\widetilde\phi^{\bar J}
-g_{I\bar J}F^I\widetilde F^{\bar J}\\
&+\frac12g_{I\bar J}\widetilde\psi^{\bar J}
\bar\sigma_E^m\partial_m\psi^I
-\frac12g_{I\bar J}(\partial_m\widetilde\psi^{\bar J})
\bar\sigma_E^m\psi^I\\
&+\frac12K_{IJ\bar K}(\partial_m\phi^I)
\widetilde\psi^{\bar K}\bar\sigma_E^m\psi^J
-\frac12K_{I\bar J\bar K}
(\partial_m\widetilde\phi^{\bar J})
\widetilde\psi^{\bar K}\bar\sigma_E^m\psi^I\\
&+\frac12K_{IJ\bar K}\psi^I\psi^J\widetilde F^{\bar K}
+\frac12K_{I\bar J\bar K}F^I
\widetilde\psi^{\bar J}\widetilde\psi^{\bar K}\\
&-\frac14K_{IJ\bar K\bar L}
\psi^I\psi^J\widetilde\psi^{\bar K}
\widetilde\psi^{\bar L}.
\end{aligned}}
\tag{3B.89}
$$

The Euclidean integrations by parts repeat (3B.48)--(3B.52) with
$i\bar\sigma_L^\mu\partial_\mu\mapsto
-\bar\sigma_E^m\partial_m$ before the overall minus.  Define

$$
\widehat{\widetilde F}^{\bar I}
:=\widetilde F^{\bar I}
-\frac12\widetilde{\mathring\Gamma}^{\bar I}{}_{\bar J\bar K}
\widetilde\psi^{\bar J}\widetilde\psi^{\bar K}.
\tag{3B.90}
$$

The independent Euclidean antichiral gauge vector and Kähler
compensator are

$$
\widetilde X_A^{\bar I}
:=-i\widetilde\phi^{\bar J}(T_A)_{\bar J}{}^{\bar I},
\qquad
X_A^IK_I+\widetilde X_A^{\bar I}K_{\bar I}
=r_A+\widetilde r_A.
\tag{3B.90a}
$$

$$
\mu_{E,A}
:=-i(X_A^IK_I-r_A)
=+i(\widetilde X_A^{\bar I}K_{\bar I}-\widetilde r_A),
\tag{3B.90b}
$$

$$
\mu_{E,A,I}=ig_{I\bar J}\widetilde X_A^{\bar J},
\qquad
\mu_{E,A,\bar J}=-ig_{I\bar J}X_A^I.
\tag{3B.90c}
$$

$$
\mathcal P_{E,A}:=\mu_{E,A}+\xi_A.
\tag{3B.90c1}
$$

Differentiating both equalities in (3B.90c) gives

$$
\boxed{
\begin{aligned}
\mu_{E,A,I\bar J}
&=-ig_{K\bar J}
\left(\partial_I X_A^K
+\mathring\Gamma^K{}_{IL}X_A^L\right)\\
&=+ig_{I\bar K}
\left(\partial_{\bar J}\widetilde X_A^{\bar K}
+\widetilde{\mathring\Gamma}^{\bar K}{}_{\bar J\bar L}
\widetilde X_A^{\bar L}\right).
\end{aligned}}
\tag{3B.90c2}
$$

Define

$$
\begin{aligned}
(\mathcal D_m\phi)^I
&:=\partial_m\phi^I-A_m^AX_A^I,\\
(\mathcal D_m\widetilde\phi)^{\bar I}
&:=\partial_m\widetilde\phi^{\bar I}
-A_m^A\widetilde X_A^{\bar I},\\
(\mathfrak D_m\psi)^I
&:=\partial_m\psi^I
+\mathring\Gamma^I{}_{JK}(\mathcal D_m\phi)^J\psi^K
-A_m^A(\partial_JX_A^I)\psi^J.
\end{aligned}
\tag{3B.90d}
$$

Direct Euclidean bridge multiplication, including the overall minus in
$S_E$, gives

$$
\boxed{
\begin{aligned}
-[\mathcal V_E^A\mu_{E,A}]_D={}&
-\mu_{E,A}\mathscr D^A
-i\sqrt2\mu_{E,A,I}\lambda^A\psi^I
+i\sqrt2\mu_{E,A,\bar I}
\widetilde\psi^{\bar I}\widetilde\lambda^A\\
&+iA_m^A\mu_{E,A,I}\partial_m\phi^I
-iA_m^A\mu_{E,A,\bar I}\partial_m\widetilde\phi^{\bar I}\\
&-iA_m^A\mu_{E,A,I\bar J}
\widetilde\psi^{\bar J}\bar\sigma_E^m\psi^I.
\end{aligned}}
\tag{3B.90e}
$$

$$
\boxed{
-\left[
\frac12\mathcal V_E^A\mathcal V_E^B
g_{I\bar J}X_{(A}^I\widetilde X_{B)}^{\bar J}
\right]_D
=+A_m^AA_m^Bg_{I\bar J}
\widetilde X_A^{\bar J}X_B^I.}
\tag{3B.90f}
$$

Equations (3B.90c), (3B.90e), and (3B.90f) give

$$
\begin{aligned}
&g_{I\bar J}\partial_m\widetilde\phi^{\bar J}\partial_m\phi^I
+iA_m^A\mu_{E,A,I}\partial_m\phi^I
-iA_m^A\mu_{E,A,\bar I}\partial_m\widetilde\phi^{\bar I}\\
&\quad
+A_m^AA_m^Bg_{I\bar J}\widetilde X_A^{\bar J}X_B^I
=g_{I\bar J}(\mathcal D_m\widetilde\phi)^{\bar J}
(\mathcal D_m\phi)^I,
\end{aligned}
\tag{3B.90g}
$$

$$
\begin{aligned}
&g_{I\bar J}\widetilde\psi^{\bar J}\bar\sigma_E^m
\left(\partial_m\psi^I
+\mathring\Gamma^I{}_{KL}\partial_m\phi^K\psi^L\right)
-iA_m^A\mu_{E,A,I\bar J}
\widetilde\psi^{\bar J}\bar\sigma_E^m\psi^I\\
&\qquad
=g_{I\bar J}\widetilde\psi^{\bar J}\bar\sigma_E^m
(\mathfrak D_m\psi)^I.
\end{aligned}
\tag{3B.90h}
$$

The independent Euclidean Kähler density is

$$
\boxed{
\begin{aligned}
\mathcal L_{K,E}={}&
+g_{I\bar J}(\mathcal D_m\widetilde\phi)^{\bar J}
(\mathcal D_m\phi)^I
+g_{I\bar J}\widetilde\psi^{\bar J}\bar\sigma_E^m
(\mathfrak D_m\psi)^I\\
&-g_{I\bar J}\widehat F^I
\widehat{\widetilde F}^{\bar J}
-\frac14R_{I\bar J K\bar L}
\psi^I\psi^K\widetilde\psi^{\bar J}
\widetilde\psi^{\bar L}\\
&-\mu_{E,A}\mathscr D^A
-i\sqrt2\mu_{E,A,I}\lambda^A\psi^I
+i\sqrt2\mu_{E,A,\bar I}
\widetilde\psi^{\bar I}\widetilde\lambda^A.
\end{aligned}}
\tag{3B.91}
$$

The Euclidean superpotential density is

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathscr U}={}&
-\mathscr U_IF^I+\frac12\mathscr U_{IJ}\psi^I\psi^J\\
&-\widetilde{\mathscr U}_{\bar I}\widetilde F^{\bar I}
+\frac12\widetilde{\mathscr U}_{\bar I\bar J}
\widetilde\psi^{\bar I}\widetilde\psi^{\bar J}.
\end{aligned}}
\tag{3B.92}
$$

Define

$$
\boxed{
\begin{aligned}
Z_E^{AB}={}&\mathscr D^A\mathscr D^B
-\frac12F_{mn}^AF_{mn}^B
+\frac14\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B\\
&-\lambda^A\sigma_E^m\mathcal D_m\widetilde\lambda^B
-\lambda^B\sigma_E^m\mathcal D_m\widetilde\lambda^A,\\
\widetilde Z_E^{AB}={}&\mathscr D^A\mathscr D^B
-\frac12F_{mn}^AF_{mn}^B
-\frac14\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B\\
&-\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B
-\widetilde\lambda^B\bar\sigma_E^m\mathcal D_m\lambda^A.
\end{aligned}}
\tag{3B.93}
$$

Direct use of (3B.39) gives

$$
\boxed{
\begin{aligned}
\mathcal C_{E,f}={}&f_{AB}Z_E^{AB}
-f_{AB,I}F^I\lambda^A\lambda^B
+\frac12f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B\\
&+i\sqrt2f_{AB,I}\psi^I\lambda^B\mathscr D^A
-\sqrt2f_{AB,I}\psi^I\sigma_E^{mn}
\lambda^BF_{mn}^A,\\
\widetilde{\mathcal C}_{E,\widetilde f}={}&
\widetilde f_{AB}\widetilde Z_E^{AB}
-\widetilde f_{AB,\bar I}\widetilde F^{\bar I}
\widetilde\lambda^A\widetilde\lambda^B\\
&+\frac12\widetilde f_{AB,\bar I\bar J}
\widetilde\psi^{\bar I}\widetilde\psi^{\bar J}
\widetilde\lambda^A\widetilde\lambda^B\\
&-i\sqrt2\widetilde f_{AB,\bar I}
\widetilde\psi^{\bar I}\widetilde\lambda^B\mathscr D^A
-\sqrt2\widetilde f_{AB,\bar I}
\widetilde\psi^{\bar I}\bar\sigma_E^{mn}
\widetilde\lambda^BF_{mn}^A.
\end{aligned}}
\tag{3B.94}
$$

Therefore

$$
\boxed{
\mathcal L_{E,f}
=-\frac14\mathcal C_{E,f}
-\frac14\widetilde{\mathcal C}_{E,\widetilde f}.}
\tag{3B.95}
$$

For

$$
\mathfrak h_{AB}:=\frac12(f_{AB}+\widetilde f_{AB}),
\qquad
\mathfrak k_{AB}:=\frac1{2i}(f_{AB}-\widetilde f_{AB}),
\tag{3B.96}
$$

equation (3B.95) becomes

$$
\boxed{
\begin{aligned}
\mathcal L_{E,f}={}&
+\frac14\mathfrak h_{AB}F_{mn}^AF_{mn}^B
-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}
F_{mn}^AF_{rs}^B\\
&+\frac12f_{AB}\lambda^A\sigma_E^m
\mathcal D_m\widetilde\lambda^B
+\frac12\widetilde f_{AB}\widetilde\lambda^A\bar\sigma_E^m
\mathcal D_m\lambda^B\\
&+\frac14f_{AB,I}F^I\lambda^A\lambda^B
+\frac14\widetilde f_{AB,\bar I}\widetilde F^{\bar I}
\widetilde\lambda^A\widetilde\lambda^B\\
&-\frac18f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B
-\frac18\widetilde f_{AB,\bar I\bar J}
\widetilde\psi^{\bar I}\widetilde\psi^{\bar J}
\widetilde\lambda^A\widetilde\lambda^B\\
&-\frac{i}{2\sqrt2}f_{AB,I}\psi^I\lambda^B\mathscr D^A
+\frac{i}{2\sqrt2}\widetilde f_{AB,\bar I}
\widetilde\psi^{\bar I}\widetilde\lambda^B\mathscr D^A\\
&+\frac1{2\sqrt2}f_{AB,I}
\psi^I\sigma_E^{mn}\lambda^BF_{mn}^A
+\frac1{2\sqrt2}\widetilde f_{AB,\bar I}
\widetilde\psi^{\bar I}\bar\sigma_E^{mn}
\widetilde\lambda^BF_{mn}^A.
\end{aligned}}
\tag{3B.97}
$$

The full Euclidean density is

$$
\boxed{
\mathcal L_E
=\mathcal L_{K,E}+\mathcal L_{E,\mathscr U}
+\mathcal L_{E,f}-\xi_A\mathscr D^A.}
\tag{3B.98}
$$

### 3B.12 Locked Wick check and positive bosonic contour

The locked map is

$$
\begin{gathered}
x_E^4=ix_L^0,
\qquad
\partial_0^L=i\partial_4^E,
\qquad
A_0^L=iA_4^E,\\
(\sigma_L^\mu\mathcal D_\mu^L)|_W
=i\sigma_E^m\mathcal D_m^E,
\qquad
(\bar\sigma_L^\mu\mathcal D_\mu^L)|_W
=i\bar\sigma_E^m\mathcal D_m^E,\\
(\sigma_L^{\mu\nu}F_{\mu\nu}^L)|_W
=-\sigma_E^{mn}F_{mn}^E,
\qquad
(\bar\sigma_L^{\mu\nu}F_{\mu\nu}^L)|_W
=-\bar\sigma_E^{mn}F_{mn}^E,\\
(\epsilon_LFF)|_W=-i\epsilon_EFF,
\qquad
\mathcal L_E=-\mathcal L_L|_W.
\end{gathered}
\tag{3B.99}
$$

For $n\geq0$, set

$$
\boldsymbol I_n=(I_1,\ldots,I_n),
\qquad
\bar{\boldsymbol I}_n=(\bar I_1,\ldots,\bar I_n),
\tag{3B.99a}
$$

with an empty multi-index for $n=0$.  The complete component and
coupling transport is

$$
\begin{aligned}
&(\bar\phi^{\bar I},\bar\psi^{\bar I},\bar F^{\bar I},
\bar\lambda^A)\Big|_W\\
&\qquad=
(\widetilde\phi^{\bar I},\widetilde\psi^{\bar I},
\widetilde F^{\bar I},\widetilde\lambda^A),\\
&(\bar{\mathscr U}_{\bar{\boldsymbol I}_n},
\bar f_{AB,\bar{\boldsymbol I}_n})\Big|_W
=(\widetilde{\mathscr U}_{\bar{\boldsymbol I}_n},
\widetilde f_{AB,\bar{\boldsymbol I}_n}).
\end{aligned}
\tag{3B.99b}
$$

$$
\begin{aligned}
&(\phi^I,\psi^I,F^I,\lambda^A,\mathscr D^A)\Big|_W
=(\phi^I,\psi^I,F^I,\lambda^A,\mathscr D^A),\\
&(\mathscr U_{\boldsymbol I_n},f_{AB,\boldsymbol I_n})\Big|_W
=(\mathscr U_{\boldsymbol I_n},f_{AB,\boldsymbol I_n}).
\end{aligned}
\tag{3B.99c}
$$

The Kähler and moment-map data obey

$$
\boxed{
\begin{aligned}
&(K_{\boldsymbol I_p\bar{\boldsymbol I}_q},g_{I\bar J},
\mathring\Gamma^I{}_{JK},
\widetilde{\mathring\Gamma}^{\bar I}{}_{\bar J\bar K},
R_{I\bar J K\bar L})\Big|_W
=(K_{\boldsymbol I_p\bar{\boldsymbol I}_q},g_{I\bar J},
\mathring\Gamma^I{}_{JK},
\widetilde{\mathring\Gamma}^{\bar I}{}_{\bar J\bar K},
R_{I\bar J K\bar L}),\\
&(X_A^I,\bar X_A^{\bar I},r_A,\bar r_A,
\mu_A,\mathcal P_A,\xi_A)\Big|_W\\
&\qquad=(X_A^I,\widetilde X_A^{\bar I},r_A,
\widetilde r_A,\mu_{E,A},\mathcal P_{E,A},\xi_A),
\qquad p,q\geq0.
\end{aligned}}
\tag{3B.99d}
$$

Equations (3B.99a)--(3B.99d) are analytic transport rules; they do not
identify either Euclidean member with a dagger before the contour.

Every line of (3B.91)--(3B.97) follows from (3B.69), (3B.73), and
(3B.86) by (3B.99).  For example,

$$
-\left[i\bar\psi\bar\sigma_L^\mu
\mathfrak D_\mu\psi\right]_W
=+\widetilde\psi\bar\sigma_E^m\mathfrak D_m\psi,
\tag{3B.100}
$$

$$
-\left[
\frac1{2\sqrt2}f_{AB,I}\psi^I\sigma_L^{\mu\nu}
\lambda^BF_{\mu\nu}^A
\right]_W
=+\frac1{2\sqrt2}f_{AB,I}\psi^I\sigma_E^{mn}
\lambda^BF_{mn}^A.
\tag{3B.101}
$$

For the full auxiliary sector define

$$
\begin{aligned}
\mathbb A_I
&:=\mathscr U_I-\frac14f_{AB,I}\lambda^A\lambda^B
-\frac12K_{I\bar J\bar K}
\widetilde\psi^{\bar J}\widetilde\psi^{\bar K},\\
\widetilde{\mathbb A}_{\bar I}
&:=\widetilde{\mathscr U}_{\bar I}
-\frac14\widetilde f_{AB,\bar I}
\widetilde\lambda^A\widetilde\lambda^B
-\frac12K_{JK\bar I}\psi^J\psi^K,
\end{aligned}
\tag{3B.102}
$$

$$
\mathbb M_A
:=\mathcal P_{E,A}
+\frac{i}{2\sqrt2}f_{AB,I}\psi^I\lambda^B
-\frac{i}{2\sqrt2}\widetilde f_{AB,\bar I}
\widetilde\psi^{\bar I}\widetilde\lambda^B.
\tag{3B.103}
$$

Then

$$
\begin{aligned}
\mathcal L_{E,\mathrm{aux}}={}&
-g_{I\bar J}F^I\widetilde F^{\bar J}
-\mathbb A_IF^I
-\widetilde{\mathbb A}_{\bar J}\widetilde F^{\bar J}\\
&-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\mathbb M_A\mathscr D^A.
\end{aligned}
\tag{3B.104}
$$

Set

$$
\begin{aligned}
G^I&:=F^I+g^{I\bar J}\widetilde{\mathbb A}_{\bar J},\\
\widetilde G^{\bar J}
&:=\widetilde F^{\bar J}+\mathbb A_Ig^{I\bar J},\\
H^A&:=\mathscr D^A+(\mathfrak h^{-1})^{AB}\mathbb M_B.
\end{aligned}
\tag{3B.105}
$$

Expanding every product gives

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{aux}}={}&
-g_{I\bar J}G^I\widetilde G^{\bar J}
+\mathbb A_Ig^{I\bar J}\widetilde{\mathbb A}_{\bar J}\\
&-\frac12\mathfrak h_{AB}H^AH^B
+\frac12\mathbb M_A(\mathfrak h^{-1})^{AB}\mathbb M_B.
\end{aligned}}
\tag{3B.106}
$$

In the bosonic sector choose

$$
\widetilde\phi=\phi^\dagger,
\qquad
g_{I\bar J}=g_{I\bar J}^\dagger>0,
\qquad
\widetilde f=f^\dagger,
\qquad
\mathfrak h_{AB}>0,
\tag{3B.107}
$$

$$
\widetilde{\mathscr U}_{\bar I}
=(\mathscr U_I)^\dagger,
\qquad
\mathcal P_{E,A}^\dagger=\mathcal P_{E,A}.
\tag{3B.107a}
$$

$$
A_m^\dagger=A_m,
\qquad
\widetilde G^{\bar I}=-(G^I)^\dagger,
\qquad
H^A=id^A,
\qquad
d^A\in\mathbb R.
\tag{3B.108}
$$

Then

$$
\boxed{
\begin{aligned}
\operatorname{Re}\mathcal L_{E,\mathrm{bos}}={}&
g_{I\bar J}(\mathcal D_m\phi)^I
\bigl((\mathcal D_m\phi)^J\bigr)^\dagger
+\frac14\mathfrak h_{AB}F_{mn}^AF_{mn}^B\\
&+g_{I\bar J}G^I(G^J)^\dagger
+\mathscr U_Ig^{I\bar J}(\mathscr U_J)^\dagger\\
&+\frac12\mathfrak h_{AB}d^Ad^B
+\frac12\mathcal P_{E,A}(\mathfrak h^{-1})^{AB}\mathcal P_{E,B}.
\end{aligned}}
\tag{3B.109}
$$

### 3B.13 Canonical specialization

Set

$$
K=\bar\phi_I\phi^I,
\qquad
g_{I\bar J}=\delta_{I\bar J},
\qquad
\mathring\Gamma=0,
\qquad
R=0.
\tag{3B.110}
$$

$$
\bar\phi_I:=\delta_{I\bar J}\bar\phi^{\bar J},
\qquad
\bar\psi_I:=\delta_{I\bar J}\bar\psi^{\bar J},
\qquad
\bar F_I:=\delta_{I\bar J}\bar F^{\bar J}.
\tag{3B.110a}
$$

Equations (3B.59)--(3B.64) give

$$
\mu_A=\bar\phi T_A\phi,
\qquad
\mu_{A,I}=\bar\phi T_A,
\qquad
\mu_{A,\bar I}=T_A\phi,
\qquad
\mu_{A,I\bar J}=T_A.
\tag{3B.111}
$$

Therefore (3B.69) becomes

$$
\boxed{
\begin{aligned}
\mathcal L_{K,L}={}&
-(\mathcal D_\mu\bar\phi)(\mathcal D^\mu\phi)
+i\bar\psi\bar\sigma_L^\mu\mathcal D_\mu\psi
+\bar FF\\
&+\bar\phi T_A\phi\,\mathscr D^A
+i\sqrt2\bar\phi T_A\lambda^A\psi
-i\sqrt2\bar\psi T_A\bar\lambda^A\phi,
\end{aligned}}
\tag{3B.112}
$$

$$
\mathcal D_\mu=\partial_\mu-iA_\mu.
\tag{3B.113}
$$

For constant $f_{AB}$, all five derivative families in the last four
lines of (3B.86) vanish, and (3B.86) gives

$$
\boxed{
\begin{aligned}
\mathcal L_{L,f}={}&
-\frac14\mathfrak h_{AB}F_{\mu\nu}^AF^{B\mu\nu}
+i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B
+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{3B.114}
$$

Equations (3B.112) and (3B.114) are exactly Step-3A (3A.81) and
(3A.86).  Their Euclidean images are exactly Step-3A (3A.95) and
(3A.98).

### 3B.14 Project–Srednicki–Weinberg comparison after derivation

No entry in the Srednicki or Weinberg column was used in
(3B.1)--(3B.114).

Let $P,S,W$ denote Project, Srednicki, and Weinberg.  The matter map is

$$
\boxed{
\phi_P=A_S=\phi_W,
\qquad
\psi_P=\psi_S,
\qquad
F_P=F_S=\mathcal F_W,
\qquad
\psi_W=i\begin{pmatrix}\psi_P\\ \bar\psi_P\end{pmatrix}.}
\tag{3B.114a}
$$

$$
\boxed{
[X]^P_F=[X]^S_F=[X]^W_{\mathcal F},
\qquad
[X]^P_D=[X]^S_D
=\frac12[X]^W_D+\frac14\Box C_X.}
\tag{3B.114b}
$$

The bridge map is

$$
\boxed{
\mathcal E_P=e^{\mathcal V_P}
=E_S=e^{-2gV_S}
=\Gamma_c=e^{-2t_AV_c^A},}
\tag{3B.114c}
$$

$$
\boxed{
\mathcal V_P=-2gV_S=-2t_AV_c^A=-2T_A\widehat V^A,
\qquad
t_A=gT_A,
\qquad
\widehat V^A=gV_c^A.}
\tag{3B.114d}
$$

Comparison of the Wess--Zumino coefficients gives

$$
\boxed{
\begin{aligned}
A_{\mu,P}^A&=gv_{\mu,S}^A=gV_{c,\mu}^A=\widehat V_\mu^A,\\
\lambda_P^A&=-ig\lambda_S^A,
&\bar\lambda_P^A&=+ig\lambda_S^{\dagger A},\\
\mathscr D_P^A&=-gD_S^A=-gD_c^A=-\widehat D^A,\\
F_{\mu\nu,P}^A&=gF_{\mu\nu,S}^A
=gf_{c,\mu\nu}^A=\widehat f_{\mu\nu}^A.
\end{aligned}}
\tag{3B.114e}
$$

The ordered barred squares are not equal.  Project gives

$$
\bar D_P^2\bar\vartheta_P^2=-4,
\tag{3B.114f}
$$

whereas Srednicki's simultaneous source equations
$W_{a,S}|=\lambda_{a,S}$ and
$V_S\supset\theta_S^{*2}\theta_S^a\lambda_{a,S}$ give

$$
\mathcal D_S^{*2}\theta_S^{*2}=+4.
\tag{3B.114g}
$$

Therefore

$$
\boxed{
\mathcal D_S^{*2}=-\bar D_P^2,
\qquad
\mathcal W_{P,a}
=-\frac18\bar D_P^2(E_S^{-1}\mathcal D_{Sa}E_S)
=-gW_{a,S}.}
\tag{3B.114h}
$$

The matter $\mathscr D$ and Yukawa coefficients translate term by term:

$$
\begin{aligned}
\bar\phi\mathscr D_P\phi
&=-gA^\dagger D_SA,\\
i\sqrt2A^\dagger\lambda_P\psi
&=i\sqrt2A^\dagger(-ig\lambda_S)\psi
=+\sqrt2gA^\dagger\lambda_S\psi,\\
-i\sqrt2\psi^\dagger\bar\lambda_PA
&=-i\sqrt2\psi^\dagger(+ig\lambda_S^\dagger)A
=+\sqrt2g\psi^\dagger\lambda_S^\dagger A.
\end{aligned}
\tag{3B.114i}
$$

Define the real symmetric invariant source trace metric by

$$
\boxed{
\kappa_{AB}=\kappa_{BA},
\qquad
c_{CA}{}^D\kappa_{DB}+c_{CB}{}^D\kappa_{AD}=0,
\qquad
\kappa_{AB}\Big|_{\rm source\ orthonormal}=\delta_{AB}.}
\tag{3B.114i1}
$$

For $\mathfrak h_{P,AB}=g^{-2}\kappa_{AB}$,

$$
\begin{aligned}
-\frac1{4g^2}\kappa_{AB}(gF_S^A)(gF_S^B)
&=-\frac14\kappa_{AB}F_S^AF_S^B,\\
i\frac1{g^2}\kappa_{AB}(ig\lambda_S^{\dagger A})
\bar\sigma^\mu\mathcal D_\mu(-ig\lambda_S^B)
&=+i\kappa_{AB}\lambda_S^{\dagger A}
\bar\sigma^\mu\mathcal D_\mu\lambda_S^B,\\
\frac1{2g^2}\kappa_{AB}(-gD_S^A)(-gD_S^B)
&=\frac12\kappa_{AB}D_S^AD_S^B.
\end{aligned}
\tag{3B.114j}
$$

The Weinberg topological and FI maps are

$$
\boxed{
\operatorname{Im}f_{P,AB}
=-\frac{\vartheta_{\rm YM}}{8\pi^2}\kappa_{AB},
\qquad
\xi_{W,A}=g\xi_{P,A},
\qquad
\xi_{P,A}\mathscr D_P^A=-\xi_{W,A}D_c^A.}
\tag{3B.114k}
$$

The symbol ``can'' in Step-3A (3A.88) denotes an internal Project
rescaling; it is not a Srednicki or Weinberg component identification.
The Weinberg--Srednicki gaugino phase, and hence the direct
$\lambda_P\leftrightarrow\lambda_c$ map, remains `SOURCE_INSUFFICIENT`.

The allowed source keys are

| key | vendored snapshot | exact Notion page |
|---|---|---|
| `S95` | `references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md` | [Srednicki 95](https://app.notion.com/p/0151805c7e85457a9928fcfd0e83da2a) |
| `W26.2` | `references/vendor/notion/weinberg/26-02-general-superfields-34cee2b74b3f8182a538e629f277c1e7.md` | [Weinberg 26.2](https://app.notion.com/p/34cee2b74b3f8182a538e629f277c1e7) |
| `W26.3` | `references/vendor/notion/weinberg/26-03-chiral-linear-superfields-34cee2b74b3f8163b3b3fa265e1815b0.md` | [Weinberg 26.3](https://app.notion.com/p/34cee2b74b3f8163b3b3fa265e1815b0) |
| `W26.4` | `references/vendor/notion/weinberg/26-04-renormalizable-chiral-theories-34cee2b74b3f81f6bba1c92f1c61727b.md` | [Weinberg 26.4](https://app.notion.com/p/34cee2b74b3f81f6bba1c92f1c61727b) |
| `W27.1` | `references/vendor/notion/weinberg/27-01-gauge-invariant-chiral-action-34cee2b74b3f81b6b72bd47d34df4d88.md` | [Weinberg 27.1](https://app.notion.com/p/34cee2b74b3f81b6b72bd47d34df4d88) |
| `W27.2` | `references/vendor/notion/weinberg/27-02-abelian-gauge-superfield-action-34cee2b74b3f8131b10edd7a1dad0172.md` | [Weinberg 27.2](https://app.notion.com/p/34cee2b74b3f8131b10edd7a1dad0172) |
| `W27.3` | `references/vendor/notion/weinberg/27-03-general-gauge-superfield-action-34cee2b74b3f812f97c2d0aa902aba5d.md` | [Weinberg 27.3](https://app.notion.com/p/34cee2b74b3f812f97c2d0aa902aba5d) |
| `W27.4` | `references/vendor/notion/weinberg/27-04-renormalizable-gauge-theory-34cee2b74b3f81949500f3f35884f580.md` | [Weinberg 27.4](https://app.notion.com/p/34cee2b74b3f81949500f3f35884f580) |

| rule or coefficient | Project | Srednicki | Weinberg |
|---|---|---|---|
| Lorentz coordinates | $\vartheta_P=\theta_S$, $\bar\vartheta_P^{\dot a}=\theta_S^{*\dot a}$; (3B.5)--(3B.15) | $y_S=x-i\theta_S\sigma_L\theta_S^*$; `S95`:135--161; (D.7.14) | $\Theta_W=-i(\theta_S,\theta_S^*)^{\rm T}$, $x_{+,W}=y_S$; `W26.3`:196--205; (D.7.7)--(D.7.14) |
| chiral covariant derivatives | $D_{P,a}=\mathcal D_{S,a}$, $\bar D_{P,\dot a}=\mathcal D^*_{S,\dot a}$; Step-2A (2A.28)--(2A.32) | native two-component operators; `S95`:27--154; (D.7.3), (D.7.9) | four-component $\mathcal D_W$; `W26.2`:18--72,355--394; (D.7.1)--(D.7.2), (D.7.8)--(D.7.9) |
| $F$ projector | $[X]^P_F=-\frac14D^2X|$; (3B.2)--(3B.3) | $[X]^S_F$ is the $\theta_S^2$ coefficient; `S95`:155--161 | $[X]^W_{\mathcal F}=[X]^P_F$; `W26.3`:196--205,275--300; (D.8.12b) |
| $D$ projector | $[X]^P_D=\frac1{16}D^2\bar D^2X|$; (3B.3) | $[X]^S_D=[X]^P_D$; `S95`:253--321 | $[X]^P_D=\frac12[X]^W_D+\frac14\Box C_X$; `W26.2`:135--142; (D.8.10)--(D.8.12a) |
| chiral expansion | (3B.10) | $A_S+\sqrt2\theta_S\psi_S+\theta_S^2F_S$; `S95`:155--185; (D.8.2), (D.8.5) | (D.8.1), (D.8.6), with $\phi_W=A_S$, $\psi_W=i(\psi_S,\psi_S^\dagger)^{\rm T}$, $\mathcal F_W=F_S$; `W26.3`:129--205 |
| antichiral expansion | (3B.15) | Hermitian conjugate of (D.8.2), (D.8.5); `S95`:155--185 | Lorentz conjugate of (D.8.1), (D.8.6); `W26.3`:129--205 |
| chiral product $F$ coefficient | $A_1F_2+A_2F_1-\psi_1\psi_2$; (3B.72), (3B.74) | same coefficient; `S95`:233--252; (D.8.13)--(D.8.14) | same coefficient under (D.8.3)--(D.8.4); `W26.3`:252--265 |
| bridge exponent | $\mathcal E_P=e^{\mathcal V_P}$, $\mathcal V_P=-2gV_S=-2t_AV_c^A$; (3B.18)--(3B.27), (3B.114c)--(3B.114d) | $E_S=e^{-2gV_S}$; `S95`:436--447,645--686; (D.9.4)--(D.9.7), (D.9.16) | $\Gamma_c=e^{-2t_AV_c^A}$, $t_A=gT_A$; `W27.1`:141--165,483--493; (D.9.3)--(D.9.9) |
| vector coefficient | $A_{\mu,P}=gv_{\mu,S}=gV_{c,\mu}=\widehat V_\mu$; (3B.27), (3B.114e) | $v_{\mu,S}$; `S95`:388--423; (D.9.1) | $V_{c,\mu}$ and $\widehat V_\mu=gV_{c,\mu}$; `W26.2`:135--142, `W27.1`:208--218; (D.9.2), (D.9.8) |
| gaugino coefficient | $\lambda_P=-ig\lambda_S$, $\bar\lambda_P=+ig\lambda_S^\dagger$; (3B.27), (3B.114e) | $\lambda_S$; `S95`:388--423 | direct $\lambda_P\leftrightarrow\lambda_c$: `SOURCE_INSUFFICIENT`; `W27.1`:208--218; (D.9.2), (D.9.11) |
| auxiliary-$D$ coefficient | $\mathscr D_P=-gD_S=-gD_c=-\widehat D$; (3B.27), (3B.114e) | $D_S$; `S95`:388--423,506--511; (D.9.1), (D.9.10a) | $D_c=D_S$, $\widehat D=gD_c$; `W27.1`:483--493; (D.9.10)--(D.9.11) |
| column gauge derivative | $\nabla_aX=\mathcal E_P^{-1}D_a(\mathcal E_PX)$; (3B.28)--(3B.29) | $E_S^{-1}\mathcal D_{S,a}(E_SX)$; follows from `S95`:645--686 and (D.9.16) | native connection has the opposite order $\Gamma_c\mathcal D_{L,W}\Gamma_c^{-1}$; `W27.3`:183--224; (D.9.19); direct Project-order map `SOURCE_INSUFFICIENT` |
| row gauge derivative | $\widetilde\nabla_{\dot a}^{\rm row}Y=\bar D_{\dot a}Y-Y\widetilde\Gamma_{\dot a}=[\bar D_{\dot a}(Y\mathcal E_P)]\mathcal E_P^{-1}$ for even $Y$; (3B.29)--(3B.34) | Lorentz conjugate of the preceding Srednicki column rule | native conjugate ordering only; direct Project-row map `SOURCE_INSUFFICIENT`; (D.9.19) |
| chiral field strength | $\mathcal W_{P,a}=-\frac18\bar D_P^2(\mathcal E_P^{-1}D_{P,a}\mathcal E_P)=-gW_{a,S}$; (3B.35), (3B.114f)--(3B.114h) | $W_{a,S}=-(8g)^{-1}\mathcal D_S^{*2}(E_S^{-1}\mathcal D_{S,a}E_S)$; `S95`:645--686; (D.9.16) | $2t_AW^A_{L,c}$ as in (D.9.19); `W27.3`:183--224 |
| antichiral field strength | (3B.35a)--(3B.39) | Lorentz conjugate of (D.9.16); `S95`:645--686 | Lorentz conjugate of (D.9.19); `W27.3`:183--224 |
| curvature coefficient | $F_{\mu\nu,P}=gF_{\mu\nu,S}=gf_{c,\mu\nu}=\widehat f_{\mu\nu}$; (3B.38), (3B.114e) | $F_{\mu\nu,S}$; `S95`:583--618; (D.9.13) | $f_{c,\mu\nu}=F_{\mu\nu,S}$, $\widehat f=g f_c$; `W27.2`:260--304, `W27.3`:287--320; (D.9.10)--(D.9.11), (D.9.15) |
| canonical scalar kinetic | $-(\mathcal D_\mu\bar\phi)(\mathcal D^\mu\phi)$; (3B.112) | coefficient $-1$; `S95`:436--511; (D.9.22) | component coefficient: `SOURCE_INSUFFICIENT`; superspace only, `W27.1`:141--147,483--493; (D.9.24) |
| canonical matter-fermion kinetic | $+i\bar\psi\bar\sigma_L^\mu\mathcal D_\mu\psi$; (3B.112) | coefficient $+i$; `S95`:436--511; (D.9.22) | component coefficient: `SOURCE_INSUFFICIENT`; superspace only, (D.9.24) |
| canonical matter $\bar FF$ | $+\bar FF$; (3B.112) | coefficient $+1$; `S95`:436--511; (D.9.22) | component coefficient: `SOURCE_INSUFFICIENT`; superspace only, (D.9.24) |
| canonical matter $D$ coupling | $+\bar\phi\mathscr D_P\phi=-gA_S^\dagger D_SA_S=-D_c^A\phi^\dagger t_A\phi$; (3B.112), (3B.114i) | coefficient $-g$; `S95`:506--511; (D.9.22) | coefficient $-1$ in the $t_A,D_c$ basis; `W27.1`:483--493; (D.9.10a) |
| canonical $\lambda\psi$ Yukawa | $+i\sqrt2\bar\phi\lambda_P\psi=+\sqrt2gA_S^\dagger\lambda_S\psi$; (3B.112), (3B.114i) | coefficient $+\sqrt2g$; `S95`:436--511; (D.9.22) | component coefficient and $\lambda_c$ phase: `SOURCE_INSUFFICIENT`; (D.9.2), (D.9.11), (D.9.24) |
| canonical $\bar\psi\bar\lambda$ Yukawa | $-i\sqrt2\bar\psi\bar\lambda_P\phi=+\sqrt2g\psi_S^\dagger\lambda_S^\dagger A_S$; (3B.112), (3B.114i) | coefficient $+\sqrt2g$; `S95`:436--511; (D.9.22) | component coefficient and $\lambda_c$ phase: `SOURCE_INSUFFICIENT`; (D.9.2), (D.9.11), (D.9.24) |
| superpotential $F$ term | $+\mathscr U_I F^I+\bar{\mathscr U}_{\bar I}\bar F^{\bar I}$; (3B.73) | $+W_iF_i+\mathrm{h.c.}$; `S95`:246--252; (D.8.16) | $+[f_W]_{\mathcal F}+\mathrm{h.c.}$; `W26.4`:132--151; (D.8.15)--(D.8.17) |
| superpotential $\psi\psi$ term | $-\frac12\mathscr U_{IJ}\psi^I\psi^J+\mathrm{h.c.}$; (3B.73) | coefficient $-\frac12$; `S95`:246--252; (D.8.16) | coefficient $-\frac12$ under (D.8.3)--(D.8.4); `W26.4`:132--151 |
| gauge $F^2$ | $-\frac14\mathfrak h_{P,AB}F_P^AF_P^B$; for $\mathfrak h_P=g^{-2}\kappa$, this is $-\frac14\kappa_{AB}F_S^AF_S^B$; (3B.114), (3B.114j) | coefficient $-\frac14\kappa_{AB}$; `S95`:620--644; (D.9.26) | canonical coefficient $-\frac14$ and rescaled $-\frac1{4g^2}$ in the source trace metric; `W27.2`:41--92, `W27.3`:261--320; (D.9.25), (D.9.27) |
| gauge-gaugino kinetic | $+i\mathfrak h_{P,AB}\bar\lambda_P^A\bar\sigma_L^\mu\mathcal D_\mu\lambda_P^B$; $\mathfrak h_P=g^{-2}\kappa$ gives $+i\kappa_{AB}\lambda_S^{\dagger A}\bar\sigma_L\mathcal D\lambda_S^B$; (3B.114), (3B.114j) | coefficient $+i\kappa_{AB}$; `S95`:620--644; (D.9.26) | four-component coefficient $-\frac12$ and rescaled $-\frac1{2g^2}$ in the source trace metric; `W27.2`:41--92, `W27.3`:261--320; (D.9.25), (D.9.27) |
| gauge $D^2$ | $+\frac12\mathfrak h_{P,AB}\mathscr D_P^A\mathscr D_P^B$; $\mathfrak h_P=g^{-2}\kappa$ gives $+\frac12\kappa_{AB}D_S^AD_S^B$; (3B.114), (3B.114j) | coefficient $+\frac12\kappa_{AB}$; `S95`:620--644; (D.9.26) | canonical $+\frac12D_c^2$ and rescaled $+\frac1{2g^2}\widehat D^2$ in the source trace metric; `W27.2`:41--92, `W27.3`:261--320; (D.9.25), (D.9.27) |
| topological coefficient | $-\frac18\mathfrak k_{P,AB}\epsilon_LF^AF^B$ with $\mathfrak k_{P,AB}=\operatorname{Im}f_{P,AB}=-\vartheta_{\rm YM}\kappa_{AB}/(8\pi^2)$; (3B.114), (3B.114k) | `SOURCE_INSUFFICIENT` | $+\vartheta_{\rm YM}(32\pi^2)^{-1}\widehat f^A\widetilde{\widehat f}^{A}$ in the source orthonormal basis; `W27.3`:261--320; (D.9.26a)--(D.9.27) |
| general $K$ raw components | (3B.41)--(3B.52) | `SOURCE_INSUFFICIENT` | general superspace $K$ only; `W27.4`:627--639; component coefficients `SOURCE_INSUFFICIENT`; (D.9.28) |
| $K$ connection and curvature | (3B.53)--(3B.58) | `SOURCE_INSUFFICIENT` | `SOURCE_INSUFFICIENT` |
| moment map and gauge completion | (3B.59)--(3B.70c) | canonical linear specialization only; `S95`:436--511; (D.9.22) | canonical linear $D$ coupling only; `W27.1`:483--493; (D.9.10a); general component coefficients `SOURCE_INSUFFICIENT` |
| $f_{AB,I}F^I\lambda^A\lambda^B$ in $\mathcal L_L$ | coefficient $-\frac14$; (3B.81), (3B.84), (3B.86) | `SOURCE_INSUFFICIENT` | general superspace $h_{AB}(\Phi)$ only; `W27.4`:627--639; component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B$ in $\mathcal L_L$ | coefficient $+\frac18$; (3B.81), (3B.84), (3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $f_{AB,I}\psi^I\lambda^B\mathscr D^A$ in $\mathcal L_L$ | coefficient $+i/(2\sqrt2)$; (3B.81), (3B.84), (3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $f_{AB,I}\psi^I\sigma_L^{\mu\nu}\lambda^BF^A_{\mu\nu}$ in $\mathcal L_L$ | coefficient $+1/(2\sqrt2)$; (3B.81), (3B.84), (3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $\bar f_{AB,\bar I}\bar F^{\bar I}\bar\lambda^A\bar\lambda^B$ in $\mathcal L_L$ | coefficient $-\frac14$; (3B.83)--(3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $\bar f_{AB,\bar I\bar J}\bar\psi^{\bar I}\bar\psi^{\bar J}\bar\lambda^A\bar\lambda^B$ in $\mathcal L_L$ | coefficient $+\frac18$; (3B.83)--(3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $\bar f_{AB,\bar I}\bar\psi^{\bar I}\bar\lambda^B\mathscr D^A$ in $\mathcal L_L$ | coefficient $-i/(2\sqrt2)$; (3B.83)--(3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| $\bar f_{AB,\bar I}\bar\psi^{\bar I}\bar\sigma_L^{\mu\nu}\bar\lambda^BF^A_{\mu\nu}$ in $\mathcal L_L$ | coefficient $+1/(2\sqrt2)$; (3B.83)--(3B.86) | `SOURCE_INSUFFICIENT` | component coefficient `SOURCE_INSUFFICIENT`; (D.9.28) |
| FI coefficient | $+\xi_{P,A}\mathscr D_P^A=-\xi_{W,A}D_c^A$, $\xi_W=g\xi_P$; (3B.87), (3B.114k) | `SOURCE_INSUFFICIENT` | $D_c^A=\xi_W^A+\phi^\dagger t^A\phi$; `W27.4`:34--75; (D.9.32) |
| Euclidean chiral and antichiral expansions | (3B.16)--(3B.17) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean bridge and both field strengths | (3B.27), (3B.39) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean scalar kinetic | $+g_{I\bar J}(\mathcal D_m\widetilde\phi)^{\bar J}(\mathcal D_m\phi)^I$; (3B.89), (3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean matter-fermion kinetic | $+g_{I\bar J}\widetilde\psi^{\bar J}\bar\sigma_E^m(\mathfrak D_m\psi)^I$; (3B.89)--(3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean matter auxiliary | $-g_{I\bar J}\widehat F^I\widehat{\widetilde F}^{\bar J}$; (3B.90)--(3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean target-curvature four-fermion | $-\frac14R_{I\bar J K\bar L}\psi^I\psi^K\widetilde\psi^{\bar J}\widetilde\psi^{\bar L}$; (3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean moment-map $D$ coupling | $-\mu_{E,A}\mathscr D^A$; (3B.90d)--(3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean moment-map Yukawas | $-i\sqrt2\mu_{E,A,I}\lambda^A\psi^I+i\sqrt2\mu_{E,A,\bar I}\widetilde\psi^{\bar I}\widetilde\lambda^A$; (3B.90e)--(3B.91) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean FI coefficient | $-\xi_A\mathscr D^A$, hence $-\mathcal P_{E,A}\mathscr D^A$ together with the preceding moment-map row; (3B.90c1), (3B.98) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean superpotential | $-\mathscr U_IF^I+\frac12\mathscr U_{IJ}\psi^I\psi^J-\widetilde{\mathscr U}_{\bar I}\widetilde F^{\bar I}+\frac12\widetilde{\mathscr U}_{\bar I\bar J}\widetilde\psi^{\bar I}\widetilde\psi^{\bar J}$; (3B.92) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean gauge $F^2$ and $D^2$ | $+\frac14\mathfrak h_{AB}F_{mn}^AF_{mn}^B-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B$; (3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean gauge-gaugino kinetic | $+\frac12f_{AB}\lambda^A\sigma_E^m\mathcal D_m\widetilde\lambda^B+\frac12\widetilde f_{AB}\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B$; (3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean topological coefficient | $-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B$; (3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $f_{AB,I}F^I\lambda^A\lambda^B$ | coefficient $+\frac14$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $f_{AB,IJ}\psi^I\psi^J\lambda^A\lambda^B$ | coefficient $-\frac18$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $f_{AB,I}\psi^I\lambda^B\mathscr D^A$ | coefficient $-i/(2\sqrt2)$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $f_{AB,I}\psi^I\sigma_E^{mn}\lambda^BF^A_{mn}$ | coefficient $+1/(2\sqrt2)$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $\widetilde f_{AB,\bar I}\widetilde F^{\bar I}\widetilde\lambda^A\widetilde\lambda^B$ | coefficient $+\frac14$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $\widetilde f_{AB,\bar I\bar J}\widetilde\psi^{\bar I}\widetilde\psi^{\bar J}\widetilde\lambda^A\widetilde\lambda^B$ | coefficient $-\frac18$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $\widetilde f_{AB,\bar I}\widetilde\psi^{\bar I}\widetilde\lambda^B\mathscr D^A$ | coefficient $+i/(2\sqrt2)$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean $\widetilde f_{AB,\bar I}\widetilde\psi^{\bar I}\bar\sigma_E^{mn}\widetilde\lambda^BF^A_{mn}$ | coefficient $+1/(2\sqrt2)$; (3B.94)--(3B.97) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Wick map | (3B.99)--(3B.101) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |
| Euclidean auxiliary contour | (3B.102)--(3B.109) | `NOT_DEFINED_IN_SOURCE` | `NOT_DEFINED_IN_SOURCE` |

The old `PROJECT_UNFIXED` status in dictionary Sections 8--9 is
superseded by verified Step 3A and the present reconstruction.

### 3B.15 Verification obligations

The exact verifier must check

$$
\begin{gathered}
(\Phi_R,\widetilde\Phi_R)
\xrightarrow{\text{projections}}
(\phi,\psi,F;\widetilde\phi,\widetilde\psi,\widetilde F),\\
\mathcal V_R
\xrightarrow{\Gamma_R,\widetilde\Gamma_R}
(\mathcal W_R,\widetilde{\mathcal W}_R),\\
K(\widetilde\Phi,\Phi)
\xrightarrow{\vartheta^2\bar\vartheta^2}
\mathcal L_{K,R}^{\rm raw}
\xrightarrow{\mathrm{IBP}}
\mathcal L_{K,R},\\
f_{AB}(\Phi)\mathcal W^A\mathcal W^B
\xrightarrow{\vartheta^2}
\mathcal C_{R,f},\\
\widetilde f_{AB}(\widetilde\Phi)
\widetilde{\mathcal W}^A\widetilde{\mathcal W}^B
\xrightarrow{\bar\vartheta^2}
\widetilde{\mathcal C}_{R,\widetilde f}.
\end{gathered}
\tag{3B.115}
$$

The exact result is

$$
\boxed{
N_{\rm new\ identities}=99,
\qquad
N_{\rm new\ coefficients}=772,
\qquad
N_{\rm failures}=0,}
\tag{3B.116}
$$

$$
N_{\rm cumulative\ identities}=88+99=187,
\qquad
N_{\rm cumulative\ coefficients}=336+772=1108.
\tag{3B.117}
$$
