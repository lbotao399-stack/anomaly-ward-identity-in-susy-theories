# 00 3+1d SUSY QFT — Convention Lock

## Step 3A. Gauge–chiral action in chiral representation

### 3A.1 Scope, indices, and ordinary gauge connection

$$
R\in\{L,E\},\qquad
I,J,K=1,\ldots,\dim\mathcal R_{\rm mat},\qquad
A,B,C=1,\ldots,\dim\mathfrak g .
\tag{3A.1}
$$

$$
[T_A,T_B]=ic_{AB}{}^CT_C,
\qquad
T_A^{\dagger}=T_A,
\qquad
c_{AB}{}^C\in\mathbb R .
\tag{3A.2}
$$

The gauge coupling is absorbed into

$$
A_M:=A_M^AT_A,
\qquad
\boxed{\mathcal D_M:=\partial_M-iA_M.}
\tag{3A.3}
$$

For a matter column and its dual row,

$$
\begin{aligned}
(\mathcal D_M\phi)^I
&:=\partial_M\phi^I-iA_M^A(T_A)^I{}_J\phi^J,\\
(\mathcal D_M\widetilde\phi)_I
&:=\partial_M\widetilde\phi_I
+i\widetilde\phi_JA_M^A(T_A)^J{}_I,\\
(\mathcal D_MX)^A
&:=\partial_MX^A+c_{BC}{}^AA_M^BX^C .
\end{aligned}
\tag{3A.4}
$$

Lorentzian reality and intrinsic Euclidean independence are

$$
\widetilde\phi_{L,I}=(\phi_L^I)^\dagger,
\qquad
(\phi_E^I,\widetilde\phi_{E,I})
\text{ are independent before a contour is chosen}.
\tag{3A.5}
$$

For $g=e^{i\alpha}$,

$$
\phi'=g\phi,
\qquad
\widetilde\phi'=\widetilde\phi g^{-1}.
\tag{3A.6}
$$

The equation $\mathcal D'_M(g\phi)=g\mathcal D_M\phi$ gives

$$
\begin{aligned}
\partial_Mg-iA'_Mg
&=-igA_M,\\
\boxed{A'_M
&=gA_Mg^{-1}-i(\partial_Mg)g^{-1}.}
\end{aligned}
\tag{3A.7}
$$

$$
\begin{aligned}
[\mathcal D_M,\mathcal D_N]
&=-iF_{MN},\\
\boxed{F_{MN}
&=\partial_MA_N-\partial_NA_M-i[A_M,A_N],}\\
F'_{MN}&=gF_{MN}g^{-1}.
\end{aligned}
\tag{3A.8}
$$

### 3A.2 Ordered Berezin projectors

$$
\vartheta^2:=\vartheta^a\vartheta_a
=-2\vartheta^1\vartheta^2,
\qquad
\bar\vartheta^2
:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}
=2\bar\vartheta_{\dot1}\bar\vartheta_{\dot2}.
\tag{3A.9}
$$

$$
D_R^2:=D_R^aD_{Ra},
\qquad
\bar D_R^2:=\bar D_{R\dot a}\bar D_R^{\dot a}.
\tag{3A.10}
$$

At $\vartheta=\bar\vartheta=0$,

$$
D_R^2=2\partial_2\partial_1,
\qquad
\bar D_R^2
=-2
\frac{\vec\partial}{\partial\bar\vartheta_{\dot2}}
\frac{\vec\partial}{\partial\bar\vartheta_{\dot1}}.
\tag{3A.11}
$$

Therefore

$$
D_R^2\vartheta^2=-4,
\qquad
\bar D_R^2\bar\vartheta^2=-4.
\tag{3A.12}
$$

The ordered projectors are

$$
[X]_F:=-\frac14D_R^2X\Big|,
\qquad
[\widetilde X]_{\widetilde F}
:=-\frac14\bar D_R^2\widetilde X\Big|,
\tag{3A.13}
$$

$$
[Y]_D:=\frac1{16}D_R^2\bar D_R^2Y\Big|,
\qquad
\bar D_R^2\text{ acts first}.
\tag{3A.14}
$$

$$
[\vartheta^2]_F=1,
\qquad
[\bar\vartheta^2]_{\widetilde F}=1,
\qquad
[\vartheta^2\bar\vartheta^2]_D=1.
\tag{3A.15}
$$

For a full superfield, with vanishing spacetime boundary term,

$$
\int d^4x_R\,d^4\vartheta\,Y
:=
\int d^4x_R\,[Y]_D
=
\int d^4x_R\,[Y]_{\vartheta^2\bar\vartheta^2}.
\tag{3A.16}
$$

### 3A.3 Chiral and antichiral component projections

$$
\bar D_{R\dot a}\Phi_R^I=0,
\qquad
D_{Ra}\widetilde\Phi_{R,I}=0.
\tag{3A.17}
$$

$$
\boxed{
\phi_R^I:=\Phi_R^I\Big|,
\qquad
\psi_{Ra}^I:=\frac1{\sqrt2}D_{Ra}\Phi_R^I\Big|,
\qquad
F_R^I:=-\frac14D_R^2\Phi_R^I\Big|.}
\tag{3A.18}
$$

$$
\boxed{
\widetilde\phi_{R,I}:=\widetilde\Phi_{R,I}\Big|,
\qquad
\widetilde\psi_{R\dot a,I}
:=\frac1{\sqrt2}\bar D_{R\dot a}\widetilde\Phi_{R,I}\Big|,
\qquad
\widetilde F_{R,I}
:=-\frac14\bar D_R^2\widetilde\Phi_{R,I}\Big|.}
\tag{3A.19}
$$

In Lorentzian signature,

$$
\widetilde\Phi_L=\bar\Phi_L,
\qquad
(\widetilde\phi_L,\widetilde\psi_L,\widetilde F_L)
=(\bar\phi_L,\bar\psi_L,\bar F_L).
\tag{3A.20}
$$

The plus sign in

$$
\bar\psi_{L\dot a}
=+\frac1{\sqrt2}\bar D_{L\dot a}\bar\Phi_L\Big|
\tag{3A.21}
$$

is fixed by the Step-2A choice
$\bar D_{L\dot a}=\bar\partial_{\dot a}
+i\vartheta\sigma_{L,\dot a}\partial$.
The formal integrated adjoint
$(D_a^L)^{\ddagger_L}=-\bar D_{\dot a}^L$
does not replace the pointwise projection (3A.21).

Define

$$
\begin{array}{c|cc}
R&y_R&\widetilde y_R\\ \hline
L&x_L-i\vartheta\sigma_L\bar\vartheta
&x_L+i\vartheta\sigma_L\bar\vartheta\\
E&x_E+\vartheta\sigma_E\bar\vartheta
&x_E-\vartheta\sigma_E\bar\vartheta
\end{array}.
\tag{3A.22}
$$

Then

$$
\Phi_R^I(y_R,\vartheta)
=\phi_R^I(y_R)
+\sqrt2\vartheta^a\psi_{Ra}^I(y_R)
+\vartheta^2F_R^I(y_R),
\tag{3A.23}
$$

$$
\widetilde\Phi_{R,I}(\widetilde y_R,\bar\vartheta)
=\widetilde\phi_{R,I}(\widetilde y_R)
+\sqrt2\bar\vartheta_{\dot a}
\widetilde\psi_R^{\dot a}{}_{I}(\widetilde y_R)
+\bar\vartheta^2\widetilde F_{R,I}(\widetilde y_R).
\tag{3A.24}
$$

The bilinear identities are

$$
\vartheta^a\vartheta^b
=-\frac12\epsilon^{ab}\vartheta^2,
\qquad
\bar\vartheta_{\dot a}\bar\vartheta_{\dot b}
=-\frac12\epsilon_{\dot a\dot b}\bar\vartheta^2,
\tag{3A.25}
$$

$$
B_L^\mu B_L^\nu
=-\frac12\eta^{\mu\nu}\vartheta^2\bar\vartheta^2,
\qquad
B_E^mB_E^n
=+\frac12\delta^{mn}\vartheta^2\bar\vartheta^2.
\tag{3A.26}
$$

The Lorentzian $x$-coordinate expansions are

$$
\begin{aligned}
\Phi_L^I={}&
\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
-iB_L^\mu\partial_\mu\phi^I\\
&+\frac{i}{\sqrt2}\vartheta^2
(\partial_\mu\psi^{Ia})(\sigma_L^\mu)_{a\dot b}
\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Box_L\phi^I,
\end{aligned}
\tag{3A.27}
$$

$$
\begin{aligned}
\bar\Phi_{L,I}={}&
\bar\phi_I+\sqrt2\bar\vartheta\bar\psi_I
+\bar\vartheta^2\bar F_I
+iB_L^\mu\partial_\mu\bar\phi_I\\
&-\frac{i}{\sqrt2}\vartheta^a
(\sigma_L^\mu)_{a\dot b}
(\partial_\mu\bar\psi_I^{\dot b})\bar\vartheta^2
+\frac14\vartheta^2\bar\vartheta^2\Box_L\bar\phi_I.
\end{aligned}
\tag{3A.28}
$$

The Euclidean $x$-coordinate expansions are

$$
\begin{aligned}
\Phi_E^I={}&
\phi^I+\sqrt2\vartheta\psi^I+\vartheta^2F^I
+B_E^m\partial_m\phi^I\\
&-\frac1{\sqrt2}\vartheta^2
(\partial_m\psi^{Ia})(\sigma_E^m)_{a\dot b}
\bar\vartheta^{\dot b}
+\frac14\vartheta^2\bar\vartheta^2\Delta_E\phi^I,
\end{aligned}
\tag{3A.29}
$$

$$
\begin{aligned}
\widetilde\Phi_{E,I}={}&
\widetilde\phi_I
+\sqrt2\bar\vartheta\widetilde\psi_I
+\bar\vartheta^2\widetilde F_I
-B_E^m\partial_m\widetilde\phi_I\\
&+\frac1{\sqrt2}\vartheta^a
(\sigma_E^m)_{a\dot b}
(\partial_m\widetilde\psi_I^{\dot b})\bar\vartheta^2
+\frac14\vartheta^2\bar\vartheta^2\Delta_E\widetilde\phi_I.
\end{aligned}
\tag{3A.30}
$$

### 3A.4 Chiral gauge representation and bridge

$$
h:=e^{i\Lambda},
\qquad
\bar h:=e^{i\bar\Lambda},
\qquad
\bar D_{\dot a}\Lambda=0,
\qquad
D_a\bar\Lambda=0.
\tag{3A.31}
$$

Let $\mathcal V=\mathcal V^AT_A$ denote the bridge exponent and
$\mathcal E:=e^{\mathcal V}$ the bridge:

$$
\Phi'=h\Phi,
\qquad
\widetilde\Phi'=\widetilde\Phi\bar h^{-1},
\qquad
\boxed{\mathcal E'=\bar h\mathcal E h^{-1}.}
\tag{3A.32}
$$

$$
\mathcal V_L^{\ddagger_L}=\mathcal V_L,
\qquad
\bar\Lambda_L=\Lambda_L^{\ddagger_L}.
\tag{3A.33}
$$

Define the multiplication connection and the differential operator separately:

$$
\Gamma_a:=\mathcal E^{-1}(D_a\mathcal E),
\qquad
\nabla_a:=D_a+\Gamma_a
=\mathcal E^{-1}\circ D_a\circ\mathcal E,
\qquad
\bar\nabla_{\dot a}:=\bar D_{\dot a}.
\tag{3A.34}
$$

For a homogeneous dual row $X$ in the antichiral frame, define

$$
\begin{aligned}
\widetilde\Gamma_{\dot a}
&:=\mathcal E(\bar D_{\dot a}\mathcal E^{-1}),\\
\widetilde\nabla_{\dot a}^{\,{\rm row}}X
&:=\bar D_{\dot a}X
-(-1)^{|X|}X\widetilde\Gamma_{\dot a},\\
\widetilde\nabla_{\dot a}^{\,{\rm row}}\widetilde\Phi
&=\bar D_{\dot a}\widetilde\Phi
-\widetilde\Phi\,\widetilde\Gamma_{\dot a}
\qquad(|\widetilde\Phi|=0).
\end{aligned}
\tag{3A.34a}
$$

$$
\widetilde\Gamma'_{\dot a}
=\bar h\widetilde\Gamma_{\dot a}\bar h^{-1}
+\bar h(\bar D_{\dot a}\bar h^{-1}),
\qquad
(\widetilde\nabla_{\dot a}^{\,{\rm row}}\widetilde\Phi)'
=(\widetilde\nabla_{\dot a}^{\,{\rm row}}\widetilde\Phi)\bar h^{-1}.
\tag{3A.34b}
$$

Since $D_a\bar h=0$ and $\bar D_{\dot a}h=0$,

$$
\nabla'_a=h\nabla_ah^{-1},
\qquad
\bar\nabla'_{\dot a}=h\bar\nabla_{\dot a}h^{-1}
=\bar D_{\dot a}.
\tag{3A.35}
$$

The vector derivatives are defined by

$$
\{\nabla_a^L,\bar\nabla_{\dot b}^L\}
=2i(\sigma_L^\mu)_{a\dot b}\mathcal D_\mu^L,
\tag{3A.36}
$$

$$
\{\nabla_a^E,\bar\nabla_{\dot b}^E\}
=-2(\sigma_E^m)_{a\dot b}\mathcal D_m^E.
\tag{3A.37}
$$

Thus

$$
\mathcal D_\mu^L
=\frac{i}{4}(\bar\sigma_{L,\mu})^{\dot ba}
\{\nabla_a^L,\bar\nabla_{\dot b}^L\},
\qquad
\mathcal D_m^E
=-\frac14(\bar\sigma_{E,m})^{\dot ba}
\{\nabla_a^E,\bar\nabla_{\dot b}^E\}.
\tag{3A.38}
$$

### 3A.5 Bridge normalization from derivative projections

Set

$$
\mathcal V_{L,A}=c_LB_L^\mu A_\mu,
\qquad
\mathcal V_{E,A}=c_EB_E^mA_m.
\tag{3A.39}
$$

The ordered derivative algebra gives

$$
\begin{gathered}
[D_{Ra},\bar D_{R\dot b}]_{\rm ord}B_R^M\Big|
=2(\sigma_R^M)_{a\dot b},\\
(\bar\sigma_{L,\mu})^{\dot ba}
(\sigma_L^\nu)_{a\dot b}=-2\delta_\mu{}^\nu,
\qquad
(\bar\sigma_{E,m})^{\dot ba}
(\sigma_E^n)_{a\dot b}=+2\delta_m{}^n.
\end{gathered}
\tag{3A.40}
$$

Define the vector components by

$$
\begin{aligned}
A_\mu^L
&:=\frac18(\bar\sigma_{L,\mu})^{\dot ba}
[D_{La},\bar D_{L\dot b}]_{\rm ord}\mathcal V_L\Big|
&=-\frac{c_L}{2}A_\mu,\\
A_m^E
&:=\frac{i}{8}(\bar\sigma_{E,m})^{\dot ba}
[D_{Ea},\bar D_{E\dot b}]_{\rm ord}\mathcal V_E\Big|
&=+\frac{ic_E}{2}A_m.
\end{aligned}
\tag{3A.41}
$$

Thus

$$
-\frac{c_L}{2}=1,
\qquad
\frac{ic_E}{2}=1,
\qquad
\boxed{c_L=-2,\qquad c_E=-2i.}
\tag{3A.42}
$$

Since
$\mathcal V_R|=D_{Ra}\mathcal V_R|=
\bar D_{R\dot a}\mathcal V_R|=0$,

$$
\Gamma_{Ra}|=0,
\qquad
\bar D_{R\dot b}\Gamma_{Ra}\Big|
=-c_R(\sigma_R^M)_{a\dot b}A_M.
\tag{3A.43}
$$

Hence

$$
\begin{aligned}
\{\nabla_{La},\bar D_{L\dot b}\}\Big|
&=2i(\sigma_L^\mu)_{a\dot b}\partial_\mu
+2(\sigma_L^\mu)_{a\dot b}A_\mu,\\
\{\nabla_{Ea},\bar D_{E\dot b}\}\Big|
&=-2(\sigma_E^m)_{a\dot b}\partial_m
+2i(\sigma_E^m)_{a\dot b}A_m.
\end{aligned}
\tag{3A.44}
$$

Factoring the right-hand sides gives

$$
\begin{aligned}
\{\nabla_{La},\bar D_{L\dot b}\}\Big|
&=2i(\sigma_L^\mu)_{a\dot b}(\partial_\mu-iA_\mu),\\
\{\nabla_{Ea},\bar D_{E\dot b}\}\Big|
&=-2(\sigma_E^m)_{a\dot b}(\partial_m-iA_m).
\end{aligned}
\tag{3A.45}
$$

Therefore both signatures give

$$
\boxed{\mathcal D_M=\partial_M-iA_M.}
\tag{3A.46}
$$

The normalized Wess--Zumino gauges are therefore

$$
\boxed{
\begin{aligned}
\mathcal V_L^{\rm WZ}={}&
-2\vartheta\sigma_L^\mu\bar\vartheta\,A_\mu
+2i\vartheta^2\bar\vartheta_{\dot a}\bar\lambda^{\dot a}\\
&-2i\bar\vartheta^2\vartheta^a\lambda_a
+\vartheta^2\bar\vartheta^2\mathscr D,
\end{aligned}}
\tag{3A.47}
$$

$$
\boxed{
\begin{aligned}
\mathcal V_E^{\rm WZ}={}&
-2i\vartheta\sigma_E^m\bar\vartheta\,A_m
+2i\vartheta^2\bar\vartheta_{\dot a}\widetilde\lambda^{\dot a}\\
&-2i\bar\vartheta^2\vartheta^a\lambda_a
+\vartheta^2\bar\vartheta^2\mathscr D.
\end{aligned}}
\tag{3A.48}
$$

The vector projections use the ordinary commutator:

$$
\boxed{
A_\mu^L
=\frac18(\bar\sigma_{L,\mu})^{\dot ba}
[D_a^L,\bar D_{\dot b}^L]_{\rm ord}\mathcal V_L\Big|,}
\tag{3A.49}
$$

$$
\boxed{
A_m^E
=\frac{i}{8}(\bar\sigma_{E,m})^{\dot ba}
[D_a^E,\bar D_{\dot b}^E]_{\rm ord}\mathcal V_E\Big|.}
\tag{3A.50}
$$

In Wess--Zumino gauge,

$$
\Gamma_{Ra}\Big|=0,
\qquad
D_R^a\Gamma_{Ra}\Big|=0,
\qquad
\nabla_{Ra}\Phi_R\Big|=D_{Ra}\Phi_R\Big|,
\qquad
\nabla_R^2\Phi_R\Big|=D_R^2\Phi_R\Big|.
\tag{3A.50a}
$$

The residual parameter obeys

$$
D_{Ra}\Lambda_R\Big|=D_R^2\Lambda_R\Big|=0,
\qquad
\bar D_{R\dot a}\bar\Lambda_R\Big|
=\bar D_R^2\bar\Lambda_R\Big|=0.
\tag{3A.50b}
$$

Thus (3A.18)--(3A.19) are Wess--Zumino coefficient projections and
transform under the residual ordinary gauge group.  Outside this gauge,
\(\Phi\) uses \(\nabla_R\), while the dual row \(\widetilde\Phi\) uses
\(\widetilde\nabla_R^{\,{\rm row}}\).

The same bridge normalization independently gives

$$
\bar D_{L\dot b}\Gamma_{La}\Big|
=2(\sigma_L^\mu)_{a\dot b}A_\mu,
\qquad
\bar D_{E\dot b}\Gamma_{Ea}\Big|
=2i(\sigma_E^m)_{a\dot b}A_m.
\tag{3A.50c}
$$

Therefore

$$
\boxed{
\begin{aligned}
\{\nabla_{La},\bar D_{L\dot b}\}\Big|
&=2i(\sigma_L^\mu)_{a\dot b}(\partial_\mu-iA_\mu),\\
\{\nabla_{Ea},\bar D_{E\dot b}\}\Big|
&=-2(\sigma_E^m)_{a\dot b}(\partial_m-iA_m).
\end{aligned}}
\tag{3A.50d}
$$

### 3A.6 Gauge field-strength superfields

Define

$$
\boxed{
\mathcal W_{Ra}
:=-\frac18\bar D_R^2
\left[\mathcal E_R^{-1}(D_{Ra}\mathcal E_R)\right].}
\tag{3A.51}
$$

The antichiral-frame field strength is

$$
\boxed{
\widetilde{\mathcal W}_{R\dot a}
:=+\frac18D_R^2
\left[\mathcal E_R(\bar D_{R\dot a}\mathcal E_R^{-1})\right].}
\tag{3A.52}
$$

The projectors and (3A.35) give

$$
\begin{gathered}
\bar D_{R\dot a}\mathcal W_{Rb}=0,
\qquad
D_{Ra}\widetilde{\mathcal W}_{R\dot b}=0,\\
\mathcal W'_{Ra}=h\mathcal W_{Ra}h^{-1},
\qquad
\widetilde{\mathcal W}'_{R\dot a}
=\bar h\widetilde{\mathcal W}_{R\dot a}\bar h^{-1}.
\end{gathered}
\tag{3A.53}
$$

$$
\widetilde{\mathcal W}_{L\dot a}=\bar{\mathcal W}_{L\dot a},
\qquad
(\mathcal W_E,\widetilde{\mathcal W}_E)
\text{ are independent before the Euclidean contour}.
\tag{3A.53a}
$$

The vector-multiplet components are the projections

$$
\boxed{
\lambda_{Ra}^A:=i\mathcal W_{Ra}^A\Big|,
\qquad
\widetilde\lambda_{R\dot a}^A
:=-i\widetilde{\mathcal W}_{R\dot a}^A\Big|,
\qquad
\mathscr D_R^A:=-\frac12D_R^a\mathcal W_{Ra}^A\Big|.}
\tag{3A.54}
$$

$$
\widetilde\lambda_{L\dot a}=\bar\lambda_{L\dot a},
\qquad
(\lambda_E,\widetilde\lambda_E)
\text{ are independent before the Euclidean contour}.
\tag{3A.54a}
$$

The superspace Bianchi identity fixes the same auxiliary field in the
antichiral frame:

$$
\boxed{
\mathscr D_R^A
=+\frac12\bar D_R^{\dot a}
\widetilde{\mathcal W}_{R\dot a}^{A}\Big|.}
\tag{3A.55}
$$

For example, the gaugino slot of (3A.47) gives

$$
\bar D_L^2D_{La}
\left(-2i\bar\vartheta^2\vartheta^b\lambda_b\right)\Big|
=8i\lambda_a,
\qquad
-\frac18(8i\lambda_a)=-i\lambda_a.
\tag{3A.56}
$$

The curvature projection is

$$
\boxed{
\nabla_{R(a}\mathcal W_{Rb)}\Big|
=D_{R(a}\mathcal W_{Rb)}\Big|_{\rm WZ}
=
\begin{cases}
i(\sigma_L^{\mu\nu})_{ab}F^L_{\mu\nu},&R=L,\\
-i(\sigma_E^{mn})_{ab}F^E_{mn},&R=E.
\end{cases}}
\tag{3A.57}
$$

The Lorentzian chiral-coordinate expansion is

$$
\boxed{
\begin{aligned}
\mathcal W_{La}(y_L,\vartheta)={}&
-i\lambda_a
+\vartheta_a\mathscr D
+i(\sigma_L^{\mu\nu})_a{}^b\vartheta_bF_{\mu\nu}\\
&-\vartheta^2(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{\dot b}.
\end{aligned}}
\tag{3A.58}
$$

The Euclidean chiral-coordinate expansion is

$$
\boxed{
\begin{aligned}
\mathcal W_{Ea}(y_E,\vartheta)={}&
-i\lambda_a
+\vartheta_a\mathscr D
-i(\sigma_E^{mn})_a{}^b\vartheta_bF_{mn}\\
&-i\vartheta^2(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{\dot b}.
\end{aligned}}
\tag{3A.59}
$$

The antichiral-coordinate expansions obtained directly from (3A.52)
are

$$
\boxed{
\begin{aligned}
\widetilde{\mathcal W}_{L\dot a}
(\widetilde y_L,\bar\vartheta)={}&
+i\bar\lambda_{\dot a}
+\bar\vartheta_{\dot a}\mathscr D
+i\bar\vartheta_{\dot b}
(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}F_{\mu\nu}\\
&-\bar\vartheta^2(\sigma_L^\mu)_{b\dot a}
\mathcal D_\mu\lambda^b,
\end{aligned}}
\tag{3A.59a}
$$

$$
\boxed{
\begin{aligned}
\widetilde{\mathcal W}_{E\dot a}
(\widetilde y_E,\bar\vartheta)={}&
+i\widetilde\lambda_{\dot a}
+\bar\vartheta_{\dot a}\mathscr D
-i\bar\vartheta_{\dot b}
(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}F_{mn}\\
&-i\bar\vartheta^2(\sigma_E^m)_{b\dot a}
\mathcal D_m\lambda^b.
\end{aligned}}
\tag{3A.59b}
$$

For the Lorentzian multiplication, write

$$
\begin{aligned}
\mathcal W_a&=w_a+\vartheta^b\mathsf M_{ba}+\vartheta^2\rho_a,\\
w_a&=-i\lambda_a,\\
\mathsf M_{ba}&=\epsilon_{ab}\mathscr D
+i(\sigma_L^{\mu\nu})_a{}^c\epsilon_{cb}F_{\mu\nu},\\
\rho_a&=-(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{\dot b}.
\end{aligned}
\tag{3A.60}
$$

Moving each odd component field through the displayed $\vartheta$'s gives

$$
[\mathcal W^a\mathcal W_a]_{\vartheta^2}
=2w^a\rho_a
-\frac12\epsilon^{bc}\epsilon^{ad}\mathsf M_{bd}\mathsf M_{ca}.
\tag{3A.61}
$$

The Step-1 matrices obey

$$
\operatorname{tr}_2
(\sigma_L^{\mu\nu}\sigma_L^{\rho\sigma})
=-\frac12
(\eta^{\mu\rho}\eta^{\nu\sigma}
-\eta^{\mu\sigma}\eta^{\nu\rho})
+\frac i2\epsilon_L^{\mu\nu\rho\sigma},
\qquad
\epsilon_L^{0123}=+1.
\tag{3A.62}
$$

Hence

$$
\boxed{
\begin{aligned}
[\mathcal W_L^{Aa}\mathcal W^B_{La}]_F={}&
\mathscr D^A\mathscr D^B
-\frac12F^A_{\mu\nu}F^{B\mu\nu}\\
&+\frac i4\epsilon_L^{\mu\nu\rho\sigma}
F^A_{\mu\nu}F^B_{\rho\sigma}
+i\lambda^{Aa}(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{B\dot b}
+i\lambda^{Ba}(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{A\dot b}.
\end{aligned}}
\tag{3A.63}
$$

With $\epsilon_E^{1234}=+1$, the Euclidean multiplication gives

$$
\boxed{
\begin{aligned}
[\mathcal W_E^{Aa}\mathcal W^B_{Ea}]_F={}&
\mathscr D^A\mathscr D^B
-\frac12F^A_{mn}F^B_{mn}\\
&+\frac14\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}
-\lambda^{Aa}(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{B\dot b}
-\lambda^{Ba}(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{A\dot b}.
\end{aligned}}
\tag{3A.64}
$$

### 3A.7 General rigid local two-derivative action

The engineering dimensions are

$$
[\Phi]=1,
\qquad
[\mathcal W_a]=\frac32,
\qquad
[d^2\vartheta]=1,
\qquad
[d^4\vartheta]=2.
\tag{3A.65}
$$

Define the two-derivative truncation by

$$
\mathfrak A_{\leq2}
:=\left\{
\text{local superspace scalars with no explicit }
\nabla_M,\nabla_a,\bar\nabla_{\dot a}
\text{ outside }\mathcal W,\widetilde{\mathcal W}
\right\}.
\tag{3A.65a}
$$

Its Lorentz-scalar density classification is

$$
\begin{array}{c|c|c}
\text{measure}&\text{required integrand}&\text{complete density}\\ \hline
d^4\vartheta&\text{real, gauge scalar, dimension }2
&\mathscr K_g+\xi_A\mathcal V^A\\
d^2\vartheta&\text{chiral, gauge scalar, dimension }3
&\mathscr U+\frac14f_{AB}\mathcal W^{Aa}\mathcal W_a^B\\
d^2\bar\vartheta&\text{antichiral, gauge scalar, dimension }3
&\bar{\mathscr U}
+\frac14\bar f_{AB}\bar{\mathcal W}_{\dot a}^A
\bar{\mathcal W}^{B\dot a}
\end{array}.
\tag{3A.65b}
$$

Indeed, a bosonic Lorentz scalar containing explicit spinor derivatives
requires a contracted pair; the algebra (3A.36)--(3A.37) produces a
vector derivative and leaves \(\mathfrak A_{\leq2}\).

At this derivative order the independent data are

$$
\begin{gathered}
\mathscr K_g(\widetilde\Phi,\Phi,\mathcal E),
\qquad
\mathscr U(\Phi),
\qquad
f_{AB}(\Phi)=f_{BA}(\Phi),\\
[\mathscr K_g]=2,
\qquad
[\mathscr U]=3,
\qquad
[f_{AB}]=0,
\qquad
[\xi_A]=2.
\end{gathered}
\tag{3A.66}
$$

Lorentzian reality is

$$
\boxed{
\mathscr K_{g,L}^{\ddagger_L}=\mathscr K_{g,L},
\qquad
\bar{\mathscr U}=\mathscr U^{\ddagger_L},
\qquad
\bar f_{AB}=f_{AB}^{\ddagger_L},
\qquad
\xi_A\in\mathbb R.}
\tag{3A.66a}
$$

The Lorentzian action is

$$
\boxed{
\begin{aligned}
S_L=\int d^4x_L\Big\{&
[\mathscr K_g(\bar\Phi,\Phi,\mathcal E)]_D
+[\mathscr U(\Phi)]_F
+[\bar{\mathscr U}(\bar\Phi)]_{\widetilde F}\\
&+\frac14[f_{AB}(\Phi)
\mathcal W_L^{Aa}\mathcal W^B_{La}]_F\\
&+\frac14[\bar f_{AB}(\bar\Phi)
\bar{\mathcal W}_{L\dot a}^{A}
\bar{\mathcal W}_L^{B\dot a}]_{\widetilde F}
+\xi_A[\mathcal V_L^A]_D\Big\}.
\end{aligned}}
\tag{3A.67}
$$

The finite Kähler condition is

$$
\begin{aligned}
&\mathscr K_g
(\widetilde\Phi\bar h^{-1},h\Phi,
\bar h\mathcal E h^{-1})\\
&\qquad=
\mathscr K_g(\widetilde\Phi,\Phi,\mathcal E)
+\mathscr F_{\Lambda}(\Phi)
+\widetilde{\mathscr F}_{\bar\Lambda}(\widetilde\Phi),\\
&[\mathscr F_{\Lambda}]_D
=[\widetilde{\mathscr F}_{\bar\Lambda}]_D=0.
\end{aligned}
\tag{3A.68}
$$

For

$$
X_A^I(\Phi):=i(T_A)^I{}_J\Phi^J,
\tag{3A.69}
$$

gauge invariance of the superpotential is exactly

$$
\boxed{X_A^I\partial_I\mathscr U=0.}
\tag{3A.70}
$$

Gauge covariance of the kinetic matrix is exactly

$$
\boxed{
X_C^I\partial_If_{AB}
-c_{CA}{}^Df_{DB}
-c_{CB}{}^Df_{AD}=0.}
\tag{3A.71}
$$

The Fayet--Iliopoulos coefficient is allowed precisely on the Abelian
quotient:

$$
\boxed{\xi_Ac_{BC}{}^A=0.}
\tag{3A.72}
$$

### 3A.8 Canonical matter $D$-density from covariant $D$-algebra

Take

$$
\mathscr K_{g,R}
=\widetilde\Phi_{R,I}(\mathcal E_R)^I{}_J\Phi_R^J,
\qquad
\widetilde\Phi_L=\bar\Phi_L,
\qquad
f_{AB}=f_{BA}=\text{constant},
\qquad
c_{CA}{}^Df_{DB}+c_{CB}{}^Df_{AD}=0,
\qquad
\operatorname{Re}f_{AB}>0.
\tag{3A.73}
$$

Introduce

$$
\begin{gathered}
\kappa_L:=2i,
\qquad
\kappa_E:=-2,
\qquad
u_R:=\frac4{\kappa_R},
\qquad
\rho_R:=\frac4{\kappa_R^2},\\
U_{R,I}:=\widetilde\Phi_{R,J}(\mathcal E_R)^J{}_I,
\qquad
\widehat{\widetilde{\mathcal W}}_{R\dot a}
:=\mathcal E_R^{-1}\widetilde{\mathcal W}_{R\dot a}\mathcal E_R,\\
(\nabla_{Ra}^{\leftarrow}X)_I
:=D_{Ra}X_I-(-1)^{|X|}X_J(\Gamma_{Ra})^J{}_I,
\qquad
\bar\nabla_{R\dot a}^{\leftarrow}X:=\bar D_{R\dot a}X.
\end{gathered}
\tag{3A.74}
$$

The chiral-frame constraints and Wess--Zumino projections are

$$
\begin{gathered}
\nabla_{Ra}^{\leftarrow}U_R
=D_{Ra}(\widetilde\Phi_R\mathcal E_R)
-U_R\Gamma_{Ra}
=\widetilde\Phi_RD_{Ra}\mathcal E_R-U_R\Gamma_{Ra}=0,
\qquad
\bar D_{R\dot a}\Phi_R=0,
\qquad
\{\nabla_{Ra}^{\leftarrow},\bar D_{R\dot b}\}X
=\kappa_R(\sigma_R^M)_{a\dot b}\mathcal D_{RM}^{\leftarrow}X,\\
\kappa_R(\sigma_R^M)_{a\dot b}
\mathcal D_{RM}^{\leftarrow}X\Big|
=\kappa_R(\sigma_R^M)_{a\dot b}\partial_{RM}X\Big|
-X|\,\bar D_{R\dot b}\Gamma_{Ra}\Big|,\\
\mathcal D_{RM}^{\leftarrow}X\Big|
=\partial_{RM}X\Big|+iX|A_M,\\
U_R|=\widetilde\phi_R,
\quad
\bar D_{R\dot a}U_R|=\sqrt2\widetilde\psi_{R\dot a},
\quad
-\frac14\bar D_R^2U_R|=\widetilde F_R,\\
\nabla_{Ra}\Phi_R|=\sqrt2\psi_{Ra},
\quad
-\frac14\nabla_R^2\Phi_R|=F_R,
\quad
\mathcal W_{Ra}|=-i\lambda_{Ra},
\quad
\widehat{\widetilde{\mathcal W}}_{R\dot a}|=i\widetilde\lambda_{R\dot a},
\quad
-\frac12\nabla_R^a\mathcal W_{Ra}|=\mathscr D_R.
\end{gathered}
\tag{3A.75}
$$

Set $A_R:=\bar D_R^2U_R$.  The first derivative is obtained only by
commuting $\nabla_R^{\leftarrow}$ through the two $\bar D_R$'s:

$$
\begin{aligned}
[\bar D_{R\dot c},
\kappa_R\mathcal D_{Ra\dot b}^{\leftarrow}]U_R
&=-U_R\bar D_{R\dot c}\bar D_{R\dot b}\Gamma_{Ra}\\
&=+\frac12\epsilon_{\dot c\dot b}
U_R\bar D_R^2\Gamma_{Ra}
=-4\epsilon_{\dot c\dot b}U_R\mathcal W_{Ra},\\
[\bar D_{R\dot b},
\kappa_R\mathcal D_{Ra}{}^{\dot b\,\leftarrow}]U_R
&=+8U_R\mathcal W_{Ra},\\
\nabla_{Ra}^{\leftarrow}A_R
&=2\kappa_R\mathcal D_{Ra\dot b}^{\leftarrow}
\bar D_R^{\dot b}U_R
-[\bar D_{R\dot b},
\kappa_R\mathcal D_{Ra}{}^{\dot b\,\leftarrow}]U_R\\
&=2\kappa_R\mathcal D_{Ra\dot b}^{\leftarrow}
\bar D_R^{\dot b}U_R-8U_R\mathcal W_{Ra}.
\end{aligned}
\tag{3A.76}
$$

Chirality and the graded Leibniz rule give the complete ordered
projector:

$$
\begin{aligned}
 D_{Ra}(X_IY^I)
&=(\nabla_{Ra}^{\leftarrow}X)_IY^I
+(-1)^{|X|}X_I\nabla_{Ra}Y^I,\\
\bar D_{R\dot a}(X_IY^I)
&=(\bar D_{R\dot a}X)_IY^I
+(-1)^{|X|}X_I\bar D_{R\dot a}Y^I,\\
\bar D_R^2(U_{R,I}\Phi_R^I)&=A_{R,I}\Phi_R^I,\\
D_R^2(A_{R,I}\Phi_R^I)
&=(\nabla_R^{\leftarrow2}A_R)_I\Phi_R^I
+2(\nabla_R^{\leftarrow a}A_R)_I\nabla_{Ra}\Phi_R^I
+A_{R,I}\nabla_R^2\Phi_R^I.
\end{aligned}
\tag{3A.77}
$$

For the odd row
$Z_R^{\dot b}:=\bar D_R^{\dot b}U_R$, the curvature and sigma
contractions are

$$
\begin{gathered}
[\nabla_{Rc},\mathcal D_{Ra\dot b}]_{\rm col}
=u_R\epsilon_{ca}
\widehat{\widetilde{\mathcal W}}_{R\dot b},\\
[\nabla_{Rc}^{\leftarrow},
\mathcal D_{Ra\dot b}^{\leftarrow}]Z_R^{\dot b}
=+u_R\epsilon_{ca}Z_R^{\dot b}
\widehat{\widetilde{\mathcal W}}_{R\dot b}
\qquad(|Z_R|=1),\\
[\nabla_R^{\leftarrow a},
\mathcal D_{Ra\dot b}^{\leftarrow}]Z_R^{\dot b}
=+2u_RZ_R^{\dot b}
\widehat{\widetilde{\mathcal W}}_{R\dot b}
=-2u_RZ_{R\dot b}
\widehat{\widetilde{\mathcal W}}_R^{\dot b},
\qquad
\nabla_R^{\leftarrow a}\bar D_R^{\dot b}U_R
=\kappa_R\mathcal D_R^{a\dot b\,\leftarrow}U_R,\\
\mathcal D_{Ra\dot b}^{\leftarrow}
\mathcal D_R^{a\dot b\,\leftarrow}
=2\rho_R\mathcal D_{RM}^{\leftarrow}
\mathcal D_R^{M\,\leftarrow},
\qquad
\kappa_Ru_R=4,
\qquad
\kappa_R^2\rho_R=4,\\[1mm]
\begin{aligned}
\nabla_R^{\leftarrow2}A_R
={}&2\kappa_R\nabla_R^{\leftarrow a}
(\mathcal D_{Ra\dot b}^{\leftarrow}Z_R^{\dot b})
-8\nabla_R^{\leftarrow a}(U_R\mathcal W_{Ra})\\
={}&2\kappa_R^2
\mathcal D_{Ra\dot b}^{\leftarrow}
\mathcal D_R^{a\dot b\,\leftarrow}U_R
-4\kappa_Ru_R
(\bar D_{R\dot b}U_R)
\widehat{\widetilde{\mathcal W}}_R^{\dot b}
-8U_R\nabla_R^a\mathcal W_{Ra}\\
={}&16\mathcal D_{RM}^{\leftarrow}
\mathcal D_R^{M\,\leftarrow}U_R
-16(\bar D_{R\dot b}U_R)
\widehat{\widetilde{\mathcal W}}_R^{\dot b}
-8U_R\nabla_R^a\mathcal W_{Ra}.
\end{aligned}
\end{gathered}
\tag{3A.78}
$$

The three terms in (3A.77) therefore project to

$$
\begin{aligned}
\frac{\kappa_R}{2}
(\mathcal D_{RM}\widetilde\psi_R^{\dot b})_I
\epsilon^{ac}(\sigma_R^M)_{c\dot b}\psi_{Ra}^I
&=-\frac{\kappa_R}{2}
(\mathcal D_{RM}\widetilde\psi_{R\dot a})_I
(\bar\sigma_R^M)^{\dot aa}\psi_{Ra}^I,\\
\frac1{16}(\nabla_R^{\leftarrow2}A_R)_I|\,\phi_R^I
={}&(\mathcal D_{RM}\mathcal D_R^M\widetilde\phi_R)_I\phi_R^I
-i\sqrt2\widetilde\psi_{R\dot a,I}(T_A)^I{}_J
\widetilde\lambda_R^{A\dot a}\phi_R^J
+\widetilde\phi_{R,I}\mathscr D_R^A(T_A)^I{}_J\phi_R^J,\\
\frac18(\nabla_R^{\leftarrow a}A_R)_I|
\,\nabla_{Ra}\Phi_R^I|
={}&-\frac{\kappa_R}{2}
(\mathcal D_{RM}\widetilde\psi_{R\dot a})_I
(\bar\sigma_R^M)^{\dot aa}\psi_{Ra}^I
+i\sqrt2\widetilde\phi_{R,I}(T_A)^I{}_J
\lambda_R^{Aa}\psi_{Ra}^J,\\
\frac1{16}A_{R,I}|\,\nabla_R^2\Phi_R^I|
={}&\widetilde F_{R,I}F_R^I.
\end{aligned}
\tag{3A.79}
$$

Define the ordered representative and its current by

$$
\begin{aligned}
\mathcal K_R^{\rm ord}:={}&
[\widetilde\Phi_R\mathcal E_R\Phi_R]_D\\
={}&(\mathcal D_{RM}\mathcal D_R^M\widetilde\phi_R)_I\phi_R^I
-\frac{\kappa_R}{2}
(\mathcal D_{RM}\widetilde\psi_{R\dot a})_I
(\bar\sigma_R^M)^{\dot aa}\psi_{Ra}^I
+\widetilde F_{R,I}F_R^I\\
&+\widetilde\phi_{R,I}\mathscr D_R^A(T_A)^I{}_J\phi_R^J\\
&+i\sqrt2\left[
\widetilde\phi_{R,I}(T_A)^I{}_J\lambda_R^{Aa}\psi_{Ra}^J
-\widetilde\psi_{R\dot a,I}(T_A)^I{}_J
\widetilde\lambda_R^{A\dot a}\phi_R^J\right],\\
J_R^M:={}&
(\mathcal D_R^M\widetilde\phi_R)_I\phi_R^I
-\frac{\kappa_R}{2}\widetilde\psi_{R\dot a,I}
(\bar\sigma_R^M)^{\dot aa}\psi_{Ra}^I,\\
\partial_{RM}J_R^M={}&
(\mathcal D_{RM}\mathcal D_R^M\widetilde\phi_R)_I\phi_R^I
+(\mathcal D_R^M\widetilde\phi_R)_I
(\mathcal D_{RM}\phi_R)^I\\
&-\frac{\kappa_R}{2}
(\mathcal D_{RM}\widetilde\psi_{R\dot a})_I
(\bar\sigma_R^M)^{\dot aa}\psi_{Ra}^I
-\frac{\kappa_R}{2}\widetilde\psi_{R\dot a,I}
(\bar\sigma_R^M)^{\dot aa}(\mathcal D_{RM}\psi_{Ra})^I,\\
\mathcal K_R^{\rm ord}
={}&\mathcal K_R^{\rm can}+\partial_{RM}J_R^M.
\end{aligned}
\tag{3A.80}
$$

For $R=L$, $\kappa_L/2=i$ and the boundary integral vanishes, so

$$
\boxed{
\begin{aligned}
\mathcal K_L^{\rm can}={}&
-(\mathcal D_\mu\bar\phi)_I(\mathcal D^\mu\phi)^I
+i\bar\psi_{\dot a,I}(\bar\sigma_L^\mu)^{\dot aa}
(\mathcal D_\mu\psi_a)^I
+\bar F_IF^I\\
&+\bar\phi_I\mathscr D^A(T_A)^I{}_J\phi^J\\
&+i\sqrt2\left[
\bar\phi_I(T_A)^I{}_J\lambda^{Aa}\psi_a^J
-\bar\psi_{\dot a,I}(T_A)^I{}_J
\bar\lambda^{A\dot a}\phi^J\right],\\
\int d^4x_L\,[\bar\Phi\mathcal E_L\Phi]_D
={}&\int d^4x_L\,\mathcal K_L^{\rm can}.
\end{aligned}}
\tag{3A.81}
$$

For the superpotential, set

$$
\delta\Phi^I:=\sqrt2\vartheta\psi^I+\vartheta^2F^I.
\tag{3A.82}
$$

Its quadratic odd product is

$$
\begin{aligned}
(\vartheta\psi^I)(\vartheta\psi^J)
&=\vartheta^a\psi_a^I\vartheta^b\psi_b^J
=-\vartheta^a\vartheta^b\psi_a^I\psi_b^J\\
&=+\frac12\vartheta^2\epsilon^{ab}\psi_a^I\psi_b^J
=-\frac12\vartheta^2\psi^{Ia}\psi_a^J.
\end{aligned}
\tag{3A.83}
$$

Thus

$$
\boxed{
[\mathscr U(\Phi)]_F
=\mathscr U_I(\phi)F^I
-\frac12\mathscr U_{IJ}(\phi)\psi^{Ia}\psi_a^J,}
\qquad
\mathscr U_I:=\frac{\partial\mathscr U}{\partial\phi^I}.
\tag{3A.84}
$$

$$
\boxed{
[\bar{\mathscr U}(\bar\Phi)]_{\widetilde F}
=\bar{\mathscr U}^{\,I}(\bar\phi)\bar F_I
-\frac12\bar{\mathscr U}^{\,IJ}(\bar\phi)
\bar\psi_{\dot a,I}\bar\psi_J^{\dot a}.}
\tag{3A.84a}
$$

Let

$$
\mathfrak h_{AB}:=\operatorname{Re}f_{AB},
\qquad
\mathfrak k_{AB}:=\operatorname{Im}f_{AB}.
\tag{3A.85}
$$

For constant $f_{AB}$, (3A.63) and its Lorentzian conjugate give

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm gauge}}={}&
-\frac14\mathfrak h_{AB}F^A_{\mu\nu}F^{B\mu\nu}
+i\mathfrak h_{AB}\bar\lambda^A_{\dot a}
(\bar\sigma_L^\mu)^{\dot aa}
(\mathcal D_\mu\lambda_a)^B\\
&+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F^A_{\mu\nu}F^B_{\rho\sigma}.
\end{aligned}}
\tag{3A.86}
$$

The canonical Lorentzian component action is (3A.81), (3A.84), its
conjugate, and (3A.86).  Its connection is exactly

$$
\boxed{\mathcal D_\mu=\partial_\mu-iA_\mu.}
\tag{3A.87}
$$

Restoring an explicit coupling uses

$$
A_\mu=gA_\mu^{\rm can},
\qquad
\lambda=g\lambda^{\rm can},
\qquad
\mathscr D=g\mathscr D^{\rm can},
\qquad
\mathfrak h_{AB}=g^{-2}\kappa_{AB}.
\tag{3A.88}
$$

### 3A.9 Euclidean continuation and canonical contour

The locked Wick map extends to the connection by

$$
\begin{gathered}
x_E^4=ix_L^0,
\qquad
\partial_0^L=i\partial_4^E,
\qquad
A_0^L=iA_4^E,
\qquad
A_i^L=A_i^E,\\
\mathcal D_0^L=i\mathcal D_4^E,
\qquad
F_{0i}^L=iF_{4i}^E,
\qquad
F_{ij}^L=F_{ij}^E.
\end{gathered}
\tag{3A.89}
$$

With the independently fixed orientations,

$$
\epsilon_L^{0123}=+1,
\qquad
\epsilon_E^{1234}=+1,
\qquad
\left(\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}F_{\rho\sigma}\right)\Big|_{\rm Wick}
=-i\epsilon_E^{mnrs}F_{mn}F_{rs}.
\tag{3A.90}
$$

Before a Euclidean contour is chosen,

$$
(\Phi_E,\widetilde\Phi_E),
\qquad
(\mathcal W_E,\widetilde{\mathcal W}_E),
\qquad
(\mathscr U_E,\widetilde{\mathscr U}_E),
\qquad
(f_E,\widetilde f_E)
\quad\text{are independent pairs}.
\tag{3A.91}
$$

Since $e^{iS_L}=e^{-S_E}$,

$$
\begin{gathered}
d^4x_L:=dx_L^0\,d^3x,
\qquad
d^4x_E:=dx_E^4\,d^3x,
\qquad
dx_L^0=-i\,dx_E^4,\\
d^4x_L=-i\,d^4x_E,
\qquad
\boxed{\mathcal L_E=-\mathcal L_L\Big|_{\rm Wick}.}
\end{gathered}
\tag{3A.92}
$$

Therefore the Euclidean superspace action is

$$
\boxed{
\begin{aligned}
S_E=-\int d^4x_E\Big\{&
[\mathscr K_{g,E}(\widetilde\Phi,\Phi,\mathcal E_E)]_D
+[\mathscr U_E(\Phi)]_F
+[\widetilde{\mathscr U}_E(\widetilde\Phi)]_{\widetilde F}\\
&+\frac14[f_{E,AB}(\Phi)
\mathcal W_E^{Aa}\mathcal W^B_{Ea}]_F\\
&+\frac14[\widetilde f_{E,AB}(\widetilde\Phi)
\widetilde{\mathcal W}_{E\dot a}^{A}
\widetilde{\mathcal W}_E^{B\dot a}]_{\widetilde F}
+\xi_A[\mathcal V_E^A]_D\Big\}.
\end{aligned}}
\tag{3A.93}
$$

Equation (3A.80) with $\kappa_E=-2$, before the minus sign in
(3A.93), gives the pointwise ordered representative

$$
\begin{aligned}
[\widetilde\Phi\mathcal E_E\Phi]_D={}&
(\mathcal D_m\mathcal D_m\widetilde\phi)_I\phi^I
+(\mathcal D_m\widetilde\psi_{\dot a})_I
(\bar\sigma_E^m)^{\dot aa}\psi_a^I
+\widetilde F_IF^I\\
&+\widetilde\phi_I\mathscr D^A(T_A)^I{}_J\phi^J\\
&+i\sqrt2\left[
\widetilde\phi_I(T_A)^I{}_J\lambda^{Aa}\psi_a^J
-\widetilde\psi_{\dot a,I}(T_A)^I{}_J
\widetilde\lambda^{A\dot a}\phi^J\right],\\
J_E^m={}&(\mathcal D_m\widetilde\phi)_I\phi^I
+\widetilde\psi_{\dot a,I}(\bar\sigma_E^m)^{\dot aa}\psi_a^I,\\
[\widetilde\Phi\mathcal E_E\Phi]_D
={}&\mathcal K_E^{\rm can}+\partial_mJ_E^m.
\end{aligned}
\tag{3A.94}
$$

Consequently, for $\int d^4x_E\,\partial_mJ_E^m=0$,

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm matter}}={}&
+(\mathcal D_m\widetilde\phi)_I(\mathcal D_m\phi)^I
+\widetilde\psi_{\dot a,I}(\bar\sigma_E^m)^{\dot aa}
(\mathcal D_m\psi_a)^I
-\widetilde F_IF^I\\
&-\widetilde\phi_I\mathscr D^A(T_A)^I{}_J\phi^J\\
&-i\sqrt2\left[
\widetilde\phi_I(T_A)^I{}_J\lambda^{Aa}\psi_a^J
-\widetilde\psi_{\dot a,I}(T_A)^I{}_J
\widetilde\lambda^{A\dot a}\phi^J\right].
\end{aligned}}
\tag{3A.95}
$$

The Euclidean superpotential terms are

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathscr U}={}&
-\mathscr U_IF^I
+\frac12\mathscr U_{IJ}\psi^{Ia}\psi_a^J\\
&-\widetilde{\mathscr U}^{,I}\widetilde F_I
+\frac12\widetilde{\mathscr U}^{,IJ}
\widetilde\psi_{\dot a,I}\widetilde\psi_J^{\dot a}.
\end{aligned}}
\tag{3A.96}
$$

On the Wick contour

$$
f_{E,AB}=\mathfrak h_{AB}+i\mathfrak k_{AB},
\qquad
\widetilde f_{E,AB}=\mathfrak h_{AB}-i\mathfrak k_{AB},
\tag{3A.97}
$$

and (3A.64) gives

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm gauge}}={}&
+\frac14\mathfrak h_{AB}F^A_{mn}F^B_{mn}
+\mathfrak h_{AB}\widetilde\lambda^A_{\dot a}
(\bar\sigma_E^m)^{\dot aa}(\mathcal D_m\lambda_a)^B\\
&-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}
F^A_{mn}F^B_{rs}.
\end{aligned}}
\tag{3A.98}
$$

For the canonical matter metric, define

$$
\mu_A:=\widetilde\phi_IT_A{}^I{}_J\phi^J+\xi_A,
\qquad
G^I:=F^I+\widetilde{\mathscr U}^{,I},
\qquad
\widetilde G_I:=\widetilde F_I+\mathscr U_I,
\tag{3A.99}
$$

$$
H^A:=\mathscr D^A+(\mathfrak h^{-1})^{AB}\mu_B.
\tag{3A.100}
$$

The auxiliary terms complete exactly as

$$
\begin{aligned}
-\widetilde F_IF^I
-\mathscr U_IF^I
-\widetilde{\mathscr U}^{\,I}\widetilde F_I
&=-\widetilde G_IG^I
+\mathscr U_I\widetilde{\mathscr U}^{\,I},\\
-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B
-\mu_A\mathscr D^A
&=-\frac12\mathfrak h_{AB}H^AH^B
+\frac12\mu_A(\mathfrak h^{-1})^{AB}\mu_B.
\end{aligned}
\tag{3A.101}
$$

For $\mathfrak h_{AB}$ positive definite, choose

$$
\boxed{
\widetilde\phi_I=(\phi^I)^\dagger,
\qquad
A_m^\dagger=A_m,
\qquad
\widetilde{\mathscr U}^{\,I}=(\mathscr U_I)^\dagger,
\qquad
\widetilde G_I=-(G^I)^\dagger,
\qquad
H^A=id^A,\qquad d^A\in\mathbb R.}
\tag{3A.102}
$$

The real canonical bosonic density is then

$$
\boxed{
\begin{aligned}
\operatorname{Re}\mathcal L_{E,{\rm bos}}={}&
(\mathcal D_m\phi)^\dagger\mathcal D_m\phi
+\frac14\mathfrak h_{AB}F^A_{mn}F^B_{mn}
+G^\dagger_IG^I
+\widetilde{\mathscr U}^{\,I}\mathscr U_I\\
+\frac12\mathfrak h_{AB}d^Ad^B
+\frac12\mu_A(\mathfrak h^{-1})^{AB}\mu_B.
\end{aligned}}
\tag{3A.103}
$$

### 3A.10 Exact component verification

The matter $D$-density is derived by (3A.74)--(3A.80).  The
exterior-algebra implementation below is an independent coefficient check.

The exact verifier computes

$$
\mathcal V_R
\longrightarrow
(\Gamma_R,\widetilde\Gamma_R)
\longrightarrow
(\mathcal W_R,\widetilde{\mathcal W}_R)
\longrightarrow
(A_M,\lambda,\widetilde\lambda,\mathscr D,
F_{MN},\mathcal D_M\widetilde\lambda)
\tag{3A.104a}
$$

and uses the coefficient ring
$\mathbb Q(i,\sqrt2)$ and the exterior-algebra order

$$
\vartheta^1<\vartheta^2<
\bar\vartheta_{\dot1}<\bar\vartheta_{\dot2}.
\tag{3A.104}
$$

It checks

$$
\boxed{
N_{\rm identities}=88,
\qquad
N_{\rm component\ coefficients}=336,
\qquad
N_{\rm failures}=0.}
\tag{3A.105}
$$

The 336 coefficients are

$$
164^{\rm bridge/projection}
+38_L^{\rm matter}
+38_E^{\rm matter}
+2^{\mathscr U}
+18_L^{\mathcal W^A\mathcal W^A}
+18_E^{\mathcal W^A\mathcal W^A}
+29_L^{\mathcal W^A\mathcal W^B}
+29_E^{\mathcal W^A\mathcal W^B}
=336.
\tag{3A.106}
$$
