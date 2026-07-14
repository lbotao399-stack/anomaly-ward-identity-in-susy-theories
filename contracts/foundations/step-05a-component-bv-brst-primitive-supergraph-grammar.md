# 00 3+1d SUSY QFT — Convention Lock

## Step 5A. Component actions, BV--BRST quantization, and primitive supergraph grammar

### 5A.1 Status, source boundary, and notation

Status token: `PASS_EXACT_PARTIAL_SCOPE`.

$$
\boxed{\operatorname{status}(5A)=\mathrm{PASS\_EXACT\_PARTIAL\_SCOPE}.}
\tag{5A.1}
$$

This contract uses only Steps 2A, 3A--3D, and 4A--4C.  Step 3E is
not used.  Exact component actions, BV--BRST identities, and
coordinate-superspace primitive vertices are proved below.  A unique
propagator set, Nielsen--Kallosh branch, and momentum-space rule set
are not asserted.

$$
\begin{gathered}
R\in\{L,E\},\qquad \eta_L=+1,\qquad \eta_E=-1,\qquad
\tau_L=\frac{i}{\hbar},\qquad \tau_E=-\frac1\hbar,\\
[X,Y]:=XY-(-1)^{\epsilon_X\epsilon_Y}YX,\qquad
(X\times Y)^A:=c_{BC}{}^A X^B Y^C,\\
X\cdot Y:=\kappa_{AB}X^AY^B,\qquad
c_{ABC}:=\kappa_{CD}c_{AB}{}^D=c_{[ABC]},\\
h:=g^{-2},\qquad
f_{AB}=h\kappa_{AB}+i\mathfrak k_{AB},\qquad
\widetilde f_{AB}=h\kappa_{AB}-i\mathfrak k_{AB},\\
\widetilde f_{L,AB}=\bar f_{AB},\qquad
(\widetilde\phi,\widetilde\psi,\widetilde F,
\widetilde\lambda)_L=(\bar\phi,\bar\psi,\bar F,\bar\lambda)_L.
\end{gathered}
\tag{5A.2}
$$

Euclidean tilded and untilded fields are independent before an
integration cycle is selected.  Repeated adjoint, spinor, and flavor
indices are contracted in the displayed order.

### 5A.2 Pure $\mathcal N=1$ component action

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{off}}^{(1)}={}&
-\frac h4\kappa_{AB}F_{\mu\nu}^AF^{B\mu\nu}
+ih\kappa_{AB}\widetilde\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B
+\frac h2\kappa_{AB}\mathscr D^A\mathscr D^B\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B,
\end{aligned}}
\tag{5A.3}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{off}}^{(1)}={}&
+\frac h4\kappa_{AB}F_{mn}^AF_{mn}^B
+h\kappa_{AB}\widetilde\lambda^A\bar\sigma_E^m
\mathcal D_m\lambda^B
-\frac h2\kappa_{AB}\mathscr D^A\mathscr D^B\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.4}
$$

$$
\frac{\partial\mathcal L_{L,\mathrm{off}}^{(1)}}
{\partial\mathscr D^A}=h\kappa_{AB}\mathscr D^B=0,
\qquad
\frac{\partial\mathcal L_{E,\mathrm{off}}^{(1)}}
{\partial\mathscr D^A}=-h\kappa_{AB}\mathscr D^B=0,
\qquad
\boxed{\mathscr D=0.}
\tag{5A.5}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{on}}^{(1)}={}&
-\frac h4\kappa_{AB}F_{\mu\nu}^AF^{B\mu\nu}
+ih\kappa_{AB}\widetilde\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B,\\
\mathcal L_{E,\mathrm{on}}^{(1)}={}&
+\frac h4\kappa_{AB}F_{mn}^AF_{mn}^B
+h\kappa_{AB}\widetilde\lambda^A\bar\sigma_E^m
\mathcal D_m\lambda^B
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.6}
$$

### 5A.3 Pure $\mathcal N=2$ component action

$$
\mu:=i(\phi\times\widetilde\phi),
\qquad
H:=\mathscr D+\mu.
\tag{5A.7}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{off}}^{(2)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-(\mathcal D_\mu\widetilde\phi^A)(\mathcal D^\mu\phi^B)
+i\widetilde\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B\\
&\quad+i\widetilde\psi^A\bar\sigma_L^\mu\mathcal D_\mu\psi^B
+\widetilde F^AF^B+\frac12\mathscr D^A\mathscr D^B
+\mathscr D^A\mu^B\Big]\\
&-\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C
+\sqrt2h c_{ACD}\widetilde\psi^D\widetilde\lambda^A\phi^C\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{5A.8}
$$

$$
\widetilde F\cdot F+\frac12\mathscr D\cdot\mathscr D
+\mathscr D\cdot\mu
=\widetilde F\cdot F+\frac12H\cdot H-\frac12\mu\cdot\mu,
\qquad
F=\widetilde F=0,\qquad H=0,\qquad\mathscr D=-\mu.
\tag{5A.9}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{on}}^{(2)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-(\mathcal D_\mu\widetilde\phi^A)(\mathcal D^\mu\phi^B)
+i\widetilde\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B\\
&\quad+i\widetilde\psi^A\bar\sigma_L^\mu\mathcal D_\mu\psi^B
-\frac12\mu^A\mu^B\Big]
-\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C\\
&+\sqrt2h c_{ACD}\widetilde\psi^D\widetilde\lambda^A\phi^C
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{5A.10}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{off}}^{(2)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+(\mathcal D_m\widetilde\phi^A)(\mathcal D_m\phi^B)
+\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B\\
&\quad+\widetilde\psi^A\bar\sigma_E^m\mathcal D_m\psi^B
-\widetilde F^AF^B-\frac12\mathscr D^A\mathscr D^B
-\mathscr D^A\mu^B\Big]\\
&+\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C
-\sqrt2h c_{ACD}\widetilde\psi^D\widetilde\lambda^A\phi^C\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.11}
$$

$$
-\widetilde F\cdot F-\frac12\mathscr D\cdot\mathscr D
-\mathscr D\cdot\mu
=-\widetilde F\cdot F-\frac12H\cdot H+\frac12\mu\cdot\mu,
\qquad
F=\widetilde F=0,\qquad H=0,\qquad\mathscr D=-\mu.
\tag{5A.12}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{on}}^{(2)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+(\mathcal D_m\widetilde\phi^A)(\mathcal D_m\phi^B)
+\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B\\
&\quad+\widetilde\psi^A\bar\sigma_E^m\mathcal D_m\psi^B
+\frac12\mu^A\mu^B\Big]
+\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C\\
&-\sqrt2h c_{ACD}\widetilde\psi^D\widetilde\lambda^A\phi^C
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.13}
$$

### 5A.4 Pure $\mathcal N=4$ component action

$$
\Lambda^{\mathcal I}=(\psi_1,\psi_2,\psi_3,\lambda),
\qquad
\varphi^{r4}=\phi_r,
\qquad
\varphi^{rs}=\varepsilon^{rst}\widetilde\phi_t,\\
\widetilde\varphi_{\mathcal I\mathcal J}
=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varphi^{\mathcal K\mathcal L},
\qquad
\widetilde\varphi_{r4}=\widetilde\phi_r,
\qquad
\widetilde\varphi_{rs}=\varepsilon_{rst}\phi_t,\\
\bar\Lambda_{L,\dot a\mathcal I}
=(\widetilde\psi_{1\dot a},\widetilde\psi_{2\dot a},
\widetilde\psi_{3\dot a},\widetilde\lambda_{\dot a})_L,
\qquad
\widetilde\Lambda_{E,\dot a\mathcal I}
=(\widetilde\psi_{1\dot a},\widetilde\psi_{2\dot a},
\widetilde\psi_{3\dot a},\widetilde\lambda_{\dot a})_E.
\tag{5A.14}
$$

The valid Yukawa identity is the contracted identity

$$
\boxed{
c_{ABC}\widetilde\varphi_{\mathcal I\mathcal J}^{A}
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
=c_{ABC}\left(
2\widetilde\phi_r^A\psi_r^B\lambda^C
+\varepsilon_{rst}\phi_t^A\psi_r^B\psi_s^C\right).}
\tag{5A.15}
$$

The corresponding uncontracted expansion is

$$
\widetilde\varphi_{\mathcal I\mathcal J}^{A}
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
=\widetilde\phi_r^A(\psi_r^B\lambda^C-\lambda^B\psi_r^C)
+\varepsilon_{rst}\phi_t^A\psi_r^B\psi_s^C.
\tag{5A.16}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{off}}^{(4)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
+i\widetilde\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B
+\frac12\mathscr D^A\mathscr D^B\\
&\quad-(\mathcal D_\mu\widetilde\phi_r)^A(\mathcal D^\mu\phi_r)^B
+i\widetilde\psi_r^A\bar\sigma_L^\mu\mathcal D_\mu\psi_r^B
+\widetilde F_r^AF_r^B
+i\mathscr D^A(\phi_r\times\widetilde\phi_r)^B\Big]\\
&+\sqrt2h c_{ABC}(\widetilde\phi_r^A\psi_r^B\lambda^C
+\phi_r^A\widetilde\psi_r^B\widetilde\lambda^C)\\
&-\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}
(F_r^A\phi_s^B\phi_t^C
+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C)\\
&+\frac h{\sqrt2}\varepsilon_{rst}c_{ABC}
(\phi_t^A\psi_r^B\psi_s^C
+\widetilde\phi_t^A\widetilde\psi_r^B\widetilde\psi_s^C)\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{5A.17}
$$

$$
C_0:=\phi_r\times\widetilde\phi_r,
\qquad
Q_r:=\frac1{\sqrt2}\varepsilon_{rst}(\phi_s\times\phi_t),
\qquad
\widetilde Q_r:=\frac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t).
\tag{5A.18}
$$

$$
\begin{aligned}
\frac12\mathscr D\cdot\mathscr D+i\mathscr D\cdot C_0
&=\frac12(\mathscr D+iC_0)\cdot(\mathscr D+iC_0)
+\frac12C_0\cdot C_0,\\
\widetilde F_r\cdot F_r-F_r\cdot Q_r
-\widetilde F_r\cdot\widetilde Q_r
&=(\widetilde F_r-Q_r)\cdot(F_r-\widetilde Q_r)
-Q_r\cdot\widetilde Q_r.
\end{aligned}
\tag{5A.19}
$$

$$
\boxed{
\mathscr D=-iC_0,
\qquad F_r=\widetilde Q_r,
\qquad\widetilde F_r=Q_r,}
\qquad
Q_r\cdot\widetilde Q_r
=2\sum_{(st)=(23),(31),(12)}
(\phi_s\times\phi_t)\cdot
(\widetilde\phi_s\times\widetilde\phi_t).
\tag{5A.20}
$$

Define

$$
\mathsf B(X,Y;Z,W):=(X\times Y)\cdot(Z\times W),
\qquad
\mathsf B(X,Y;Z,W)-\mathsf B(X,Z;Y,W)
+\mathsf B(X,W;Y,Z)=0.
\tag{5A.21}
$$

For

$$
A_{rs}:=\mathsf B(\phi_r,\phi_s;\widetilde\phi_r,\widetilde\phi_s),
\quad
U_{rs}:=\mathsf B(\phi_r,\widetilde\phi_s;
\widetilde\phi_r,\phi_s),
\quad
C_{rs}:=\mathsf B(\phi_r,\widetilde\phi_r;
\phi_s,\widetilde\phi_s),
\tag{5A.22}
$$

Jacobi gives

$$
U_{rs}=A_{rs}-C_{rs},\qquad
\sum_{r,s}C_{rs}=C_0\cdot C_0,\qquad
\sum_{r,s}A_{rs}=2\sum_{r<s}A_{rs}.
\tag{5A.23}
$$

The $4^4=256$ internal slots contain $112$ diagonal zero slots and
$144=36\cdot4$ off-diagonal reversal slots.  Their exact reduction is

$$
\begin{aligned}
\mathscr S_{256}
&=8\sum_{r,s}(A_{rs}+U_{rs})
=16\sum_{r,s}A_{rs}-8\sum_{r,s}C_{rs}\\
&=-8C_0\cdot C_0+32\sum_{r<s}A_{rs},
\end{aligned}
\tag{5A.24}
$$

$$
\boxed{
\begin{aligned}
&(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})\cdot
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})\\
&\qquad=-8C_0\cdot C_0
+32\sum_{r<s}(\phi_r\times\phi_s)\cdot
(\widetilde\phi_r\times\widetilde\phi_s).
\end{aligned}}
\tag{5A.25}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,\mathrm{on}}^{(4)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-\frac14(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})^A
(\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J})^B\\
&\quad+i\bar\Lambda_{\dot a\mathcal I}^A
(\bar\sigma_L^\mu)^{\dot aa}(\mathcal D_\mu\Lambda_a^{\mathcal I})^B
-\frac1{16}(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B\Big]\\
&+\frac h{\sqrt2}c_{ABC}\Big(
\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
+\varphi^{\mathcal I\mathcal J,A}
\bar\Lambda_{\mathcal I}^B\bar\Lambda_{\mathcal J}^C\Big)\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{5A.26}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{off}}^{(4)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B
-\frac12\mathscr D^A\mathscr D^B\\
&\quad+(\mathcal D_m\widetilde\phi_r)^A(\mathcal D_m\phi_r)^B
+\widetilde\psi_r^A\bar\sigma_E^m\mathcal D_m\psi_r^B
-\widetilde F_r^AF_r^B
-i\mathscr D^A(\phi_r\times\widetilde\phi_r)^B\Big]\\
&-\sqrt2h c_{ABC}(\widetilde\phi_r^A\psi_r^B\lambda^C
+\phi_r^A\widetilde\psi_r^B\widetilde\lambda^C)\\
&+\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}
(F_r^A\phi_s^B\phi_t^C
+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C)\\
&-\frac h{\sqrt2}\varepsilon_{rst}c_{ABC}
(\phi_t^A\psi_r^B\psi_s^C
+\widetilde\phi_t^A\widetilde\psi_r^B\widetilde\psi_s^C)\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.27}
$$

$$
\begin{aligned}
-\frac12\mathscr D\cdot\mathscr D-i\mathscr D\cdot C_0
&=-\frac12(\mathscr D+iC_0)\cdot(\mathscr D+iC_0)
-\frac12C_0\cdot C_0,\\
-\widetilde F_r\cdot F_r+F_r\cdot Q_r
+\widetilde F_r\cdot\widetilde Q_r
&=-(\widetilde F_r-Q_r)\cdot(F_r-\widetilde Q_r)
+Q_r\cdot\widetilde Q_r.
\end{aligned}
\tag{5A.28}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{E,\mathrm{on}}^{(4)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+\frac14(\mathcal D_m\varphi^{\mathcal I\mathcal J})^A
(\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J})^B\\
&\quad+\widetilde\Lambda_{\dot a\mathcal I}^A
(\bar\sigma_E^m)^{\dot aa}(\mathcal D_m\Lambda_a^{\mathcal I})^B
+\frac1{16}(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B\Big]\\
&-\frac h{\sqrt2}c_{ABC}\Big(
\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
+\varphi^{\mathcal I\mathcal J,A}
\widetilde\Lambda_{\mathcal I}^B\widetilde\Lambda_{\mathcal J}^C\Big)\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{5A.29}
$$

### 5A.5 Wess--Zumino component surface and full BV prepotential

The component actions (5A.3)--(5A.29) use

$$
\begin{aligned}
\mathcal V_L^{\mathrm{WZ}}={}&
-2\vartheta\sigma_L^\mu\bar\vartheta A_\mu
+2i\vartheta^2\bar\vartheta\widetilde\lambda
-2i\bar\vartheta^2\vartheta\lambda
+\vartheta^2\bar\vartheta^2\mathscr D,\\
\mathcal V_E^{\mathrm{WZ}}={}&
-2i\vartheta\sigma_E^m\bar\vartheta A_m
+2i\vartheta^2\bar\vartheta\widetilde\lambda
-2i\bar\vartheta^2\vartheta\lambda
+\vartheta^2\bar\vartheta^2\mathscr D.
\end{aligned}
\tag{5A.30}
$$

BV--BRST quantization instead uses the unrestricted connected-chart
prepotential

$$
\mathcal E_R:=e^{\mathcal V_R},
\qquad
\mathcal V_R\in\Gamma(\Sigma_{R,8},\mathfrak g),
\qquad
\mathcal V_R\ne\mathcal V_R^{\mathrm{WZ}}
\quad\text{before gauge fixing}.
\tag{5A.31}
$$

No Wess--Zumino-gauge component propagator or ghost rule is inferred
from the unrestricted BV system.

### 5A.6 Unified $\mathcal N=1$ superspace action

$$
m_1=0,\qquad m_2=1,\qquad m_4=3,\qquad
\delta_{N4}:=\begin{cases}1,&N=4,\\0,&N=1,2.\end{cases}
\tag{5A.32}
$$

$$
\Gamma_{Ra}:=e^{-\mathcal V_R}D_{Ra}e^{\mathcal V_R},
\qquad
\widetilde\Gamma_{R\dot a}:=e^{\mathcal V_R}
\bar D_{R\dot a}e^{-\mathcal V_R},
\qquad
\mathcal W_{Ra}:=-\frac18\bar D_R^2\Gamma_{Ra},
\qquad
\widetilde{\mathcal W}_{R\dot a}:=
+\frac18D_R^2\widetilde\Gamma_{R\dot a}.
\tag{5A.33}
$$

$$
\boxed{
\begin{aligned}
S_R^{(N)}=\eta_R\Bigg\{&
h\kappa_{AB}\sum_{r=1}^{m_N}
\int_{R,8}\widetilde\Phi_r^A
(e^{\mathcal V_{R,\mathrm{ad}}})^B{}_C\Phi_r^C\\
&+\frac14f_{AB}\int_{R,+}\mathcal W_R^{Aa}\mathcal W_{Ra}^B
+\frac14\widetilde f_{AB}\int_{R,-}
\widetilde{\mathcal W}_{R\dot a}^A
\widetilde{\mathcal W}_R^{B\dot a}\\
&-\delta_{N4}\frac{\sqrt2h}{6}\varepsilon_{rst}c_{ABC}
\left(\int_{R,+}\Phi_r^A\Phi_s^B\Phi_t^C
+\int_{R,-}\widetilde\Phi_r^A\widetilde\Phi_s^B
\widetilde\Phi_t^C\right)\Bigg\}.
\end{aligned}}
\tag{5A.34}
$$

### 5A.7 Exact classical BRST and minimal BV action

$$
\bar D_R\mathfrak c_R=0,\qquad
D_R\widetilde{\mathfrak c}_R=0,\qquad
\epsilon(\mathfrak c_R)=\epsilon(\widetilde{\mathfrak c}_R)=1,
\qquad
\operatorname{gh}(\mathfrak c_R)
=\operatorname{gh}(\widetilde{\mathfrak c}_R)=1.
\tag{5A.35}
$$

$$
\boxed{
\begin{aligned}
\mathbf s_R\mathcal E_R&=i\widetilde{\mathfrak c}_R\mathcal E_R
-i\mathcal E_R\mathfrak c_R,
&\mathbf s_R\mathfrak c_R&=i\mathfrak c_R^2,
&\mathbf s_R\widetilde{\mathfrak c}_R&=i\widetilde{\mathfrak c}_R^2,\\
\mathbf s_R\Phi_R&=i\mathfrak c_R\Phi_R,
&\mathbf s_R\widetilde\Phi_R&=-i\widetilde\Phi_R
\widetilde{\mathfrak c}_R.
\end{aligned}}
\tag{5A.36}
$$

$$
\mathbf s_R\mathfrak c_R^C
=-\frac12c_{AB}{}^C\mathfrak c_R^A\mathfrak c_R^B,
\qquad
\mathbf s_R^2\mathfrak c_R
=i(i\mathfrak c_R^2\mathfrak c_R-i\mathfrak c_R\mathfrak c_R^2)=0,
\qquad
\mathbf s_R^2\widetilde{\mathfrak c}_R=0.
\tag{5A.37}
$$

$$
\begin{aligned}
\mathbf s_R^2\mathcal E_R={}&
-\widetilde{\mathfrak c}_R^2\mathcal E_R
+\widetilde{\mathfrak c}_R^2\mathcal E_R
-\widetilde{\mathfrak c}_R\mathcal E_R\mathfrak c_R
+\widetilde{\mathfrak c}_R\mathcal E_R\mathfrak c_R\\
&-\mathcal E_R\mathfrak c_R^2+\mathcal E_R\mathfrak c_R^2=0,\\
\mathbf s_R^2\Phi_R={}&-\mathfrak c_R^2\Phi_R
+\mathfrak c_R^2\Phi_R=0,\\
\mathbf s_R^2\widetilde\Phi_R={}&
-\widetilde\Phi_R\widetilde{\mathfrak c}_R^2
+\widetilde\Phi_R\widetilde{\mathfrak c}_R^2=0.
\end{aligned}
\tag{5A.38}
$$

$$
\boxed{
\mathbf s_R\mathcal V_R
=\frac{\operatorname{ad}_{\mathcal V_R}}
{1-e^{-\operatorname{ad}_{\mathcal V_R}}}
\left(ie^{-\operatorname{ad}_{\mathcal V_R}}
\widetilde{\mathfrak c}_R-i\mathfrak c_R\right),
\qquad
\mathbf s_RS_R^{(N)}=0,\qquad\mathbf s_R^2=0.}
\tag{5A.39}
$$

For fields $Q^{\mathfrak i}$ and antifields $Q^\star_{\mathfrak i}$,

$$
(F,G)_R:=\sum_{\mathfrak i}\int_{\Sigma_{\mathfrak i}}
\left[
F\frac{\overleftarrow\delta}{\delta Q^{\mathfrak i}}
\frac{\vec\delta G}{\delta Q^\star_{\mathfrak i}}
-F\frac{\overleftarrow\delta}{\delta Q^\star_{\mathfrak i}}
\frac{\vec\delta G}{\delta Q^{\mathfrak i}}
\right].
\tag{5A.40}
$$

$$
\boxed{
S_{\min,R}:=S_R^{(N)}
+\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
Q^\star_{R,\mathfrak i}\mathbf s_RQ_R^{\mathfrak i},
\qquad
\frac12(S_{\min,R},S_{\min,R})_R
=\mathbf s_RS_R^{(N)}
+\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
Q^\star_{\mathfrak i}\mathbf s_R^2Q^{\mathfrak i}=0.}
\tag{5A.41}
$$

$$
\boxed{
\mathbf s_RF=(S_{\min,R},F)_R,
\qquad
\mathbf s_R^2F
=\frac12((S_{\min,R},S_{\min,R})_R,F)_R=0.}
\tag{5A.42}
$$

For a finite projector $\pi_{R,\nu}$ and inclusion
$\iota_{R,\nu}$, define

$$
\mathbf s_{R,\nu}:=\pi_{R,\nu}\mathbf s_R\iota_{R,\nu},
\qquad
\mathfrak R_{R,\nu}^{\mathsf i}
:=\mathbf s_{R,\nu}^2Q_{R,\nu}^{\mathsf i}.
\tag{5A.42a}
$$

The finite-cutoff master identity is

$$
\boxed{
\frac12(S_{\min,R,\nu},S_{\min,R,\nu})_{R,\nu}
=\mathbf s_{R,\nu}S_{R,\nu}^{(N)}
+\sum_{\mathsf i}(-1)^{\epsilon_{\mathsf i}}
Q^\star_{R,\nu,\mathsf i}\mathfrak R_{R,\nu}^{\mathsf i}.}
\tag{5A.42b}
$$

For an even nowhere-vanishing BV density
$\widehat{\boldsymbol\varpi}_{R,\nu}$, define its modular defect by

$$
\begin{aligned}
\Delta_{0,R,\nu}F
&:=\sum_{\mathsf i}(-1)^{\epsilon_{\mathsf i}}
\frac{\vec\partial}{\partial\widehat Q^{\mathsf i}}
\frac{\vec\partial F}{\partial\widehat Q^\star_{\mathsf i}},\\
\Delta_{R,\nu}F
&:=\Delta_{0,R,\nu}F
+\frac12(\log\widehat{\boldsymbol\varpi}_{R,\nu},F)_{R,\nu},
\\
\mathfrak M^\Delta_{R,\nu}[F]
&:=\Delta_{R,\nu}^2F,\qquad
\widehat{\boldsymbol\varpi}_{R,\nu}\ \text{BV-compatible}
\Longleftrightarrow
\mathfrak M^\Delta_{R,\nu}[F]=0\quad\text{for every }F.
\end{aligned}
\tag{5A.42c}
$$

The two signature-dependent QME operators are

$$
\boxed{
\begin{aligned}
\mathfrak O^{\mathrm{BV}}_{L,\nu}[W]
&:=\frac12(W_{L,\nu},W_{L,\nu})_{L,\nu}
-i\hbar\Delta_{L,\nu}W_{L,\nu},\\
\mathfrak O^{\mathrm{BV}}_{E,\nu}[W]
&:=\frac12(W_{E,\nu},W_{E,\nu})_{E,\nu}
-\hbar\Delta_{E,\nu}W_{E,\nu}.
\end{aligned}}
\tag{5A.42d}
$$

Assume that both terms on the right of (5A.42b) vanish and that
$\widehat{\boldsymbol\varpi}_{R,\nu}$ is BV-compatible.  Then a
solution of $\mathfrak O^{\mathrm{BV}}_{R,\nu}[W]=0$ with expansion

$$
W_{R,\nu}=\sum_{n=0}^{\infty}\hbar^nM_{n,R,\nu},
\qquad
M_{0,R,\nu}:=S_{\min,R,\nu}
\tag{5A.42e}
$$

obey the order-by-order QME condition

$$
\boxed{
\mathbf s_{R,\nu}M_{n,R,\nu}
=\mathfrak e_R^{\mathrm{QME}}\Delta_{R,\nu}M_{n-1,R,\nu}
-\frac12\sum_{k=1}^{n-1}
(M_{k,R,\nu},M_{n-k,R,\nu})_{R,\nu},
\quad n\geq1,\quad
\mathfrak e_L^{\mathrm{QME}}=i,\quad
\mathfrak e_E^{\mathrm{QME}}=1.}
\tag{5A.42f}
$$

If either term in (5A.42b) is nonzero or
$\mathfrak M^\Delta_{R,\nu}\ne0$, the corresponding defect is retained
and $\mathfrak O^{\mathrm{BV}}_{R,\nu}=0$ is not asserted.

### 5A.8 Nonminimal doublets and gauge fermion

$$
\boxed{
\mathbf s_R\mathfrak c'_{R,+}=\mathfrak n_{R,+},
\quad\mathbf s_R\mathfrak n_{R,+}=0,
\qquad
\mathbf s_R\widetilde{\mathfrak c}'_{R,-}
=\widetilde{\mathfrak n}_{R,-},
\quad\mathbf s_R\widetilde{\mathfrak n}_{R,-}=0.}
\tag{5A.43}
$$

$$
\mathcal F_{R,+}(\mathcal V_{R,\mathrm q})
:=-\frac14(\bar{\boldsymbol\nabla}_{R,\mathrm B}^{\mathsf V})^2
\mathcal V_{R,\mathrm q},
\qquad
\mathcal F_{R,-}(\mathcal V_{R,\mathrm q})
:=-\frac14(\boldsymbol\nabla_{R,\mathrm B}^{\mathsf V})^2
\mathcal V_{R,\mathrm q}.
\tag{5A.44}
$$

$$
\langle A,B\rangle_R:=\int_{R,+}A_+B_+
+\int_{R,-}A_-B_-,
\qquad
\epsilon(\mathcal Y_R)=0,\qquad
\operatorname{gh}(\mathcal Y_R)=0,\qquad
[\mathcal Y_R]=-1,\qquad
\mathcal Y_R\ \text{local, invertible, graded-self-adjoint}.
\tag{5A.45}
$$

$$
\boxed{
\Psi_{\mathcal F,\mathcal Y,R}
:=\langle\mathfrak c'_R,\mathcal F_R\rangle_R
-\frac12\langle\mathfrak c'_R,\mathcal Y_R\mathfrak n_R\rangle_R.}
\tag{5A.46}
$$

$$
\boxed{
\begin{aligned}
\mathbf s_R\Psi_{\mathcal F,\mathcal Y,R}={}&
\langle\mathfrak n_R,\mathcal F_R\rangle_R
-\langle\mathfrak c'_R,
\mathcal M_R^{\mathrm{FP}}\mathfrak c_R^{\mathrm{pair}}\rangle_R
-\frac12\langle\mathfrak n_R,\mathcal Y_R\mathfrak n_R\rangle_R\\
&+\frac12\langle\mathfrak c'_R,
(\mathbf s_R\mathcal Y_R)\mathfrak n_R\rangle_R,
\qquad
\mathcal M_R^{\mathrm{FP}}\mathfrak c_R^{\mathrm{pair}}
:=\mathbf s_R\mathcal F_R.
\end{aligned}}
\tag{5A.47}
$$

If $\mathbf s_R\mathcal Y_R=0$, then

$$
\begin{aligned}
\langle\mathfrak n,\mathcal F\rangle
-\frac12\langle\mathfrak n,\mathcal Y\mathfrak n\rangle
={}&\frac12\langle\mathcal Y^{-1}\mathcal F,\mathcal F\rangle\\
&-\frac12\langle\mathfrak n-\mathcal Y^{-1}\mathcal F,
\mathcal Y(\mathfrak n-\mathcal Y^{-1}\mathcal F)\rangle.
\end{aligned}
\tag{5A.48}
$$

The separated Nielsen--Kallosh factor is not selected by
(5A.43)--(5A.48).

### 5A.9 All-order coordinate-superspace primitive rules

In this section only, write $V:=\mathcal V_R$ and retain the displayed
matrix order before taking adjoint components.

The two exact exponential derivatives are

$$
\boxed{
\Gamma_{Ra}
=\sum_{p,q\ge0}a_{pq}\mathcal V_R^p(D_{Ra}\mathcal V_R)
\mathcal V_R^q,
\qquad
a_{pq}:=\frac{(-1)^p}{p!q!(p+q+1)},}
\tag{5A.49}
$$

$$
\boxed{
\widetilde\Gamma_{R\dot a}
=\sum_{p,q\ge0}\widetilde a_{pq}\mathcal V_R^p
(\bar D_{R\dot a}\mathcal V_R)\mathcal V_R^q,
\qquad
\widetilde a_{pq}:=\frac{(-1)^{q+1}}{p!q!(p+q+1)}.}
\tag{5A.50}
$$

Indeed,

$$
e^{-V}De^V=\int_0^1dt\,e^{-tV}(DV)e^{tV},
\qquad
e^V\bar De^{-V}=-\int_0^1dt\,e^{tV}(\bar DV)e^{-tV},
\qquad
\int_0^1t^{p+q}dt=\frac1{p+q+1}.
\tag{5A.51}
$$

The complete gauge-word convolution is

$$
\boxed{
\begin{aligned}
S_{R,+}^{\mathrm g}={}&
\sum_{p,q,r,s\ge0}
\frac{\eta_R(-1)^{p+r}f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}\\
&\times\int_{R,+}
\left[\bar D_R^2(V^pD_R^aV V^q)\right]^A
\left[\bar D_R^2(V^rD_{Ra}V V^s)\right]^B,\\
S_{R,-}^{\mathrm g}={}&
\sum_{p,q,r,s\ge0}
\frac{\eta_R(-1)^{q+s}\widetilde f_{AB}}
{256p!q!r!s!(p+q+1)(r+s+1)}\\
&\times\int_{R,-}
\left[D_R^2(V^p\bar D_{R\dot a}V V^q)\right]^A
\left[D_R^2(V^r\bar D_R^{\dot a}V V^s)\right]^B.
\end{aligned}}
\tag{5A.52}
$$

For $T_A:=T_A^{\mathrm{ad}}$,

$$
\boxed{
S_R^{\mathrm{mat}}
=\eta_Rh\kappa_{AB}\sum_{r=1}^{m_N}\sum_{n=0}^{\infty}
\frac1{n!}\int_{R,8}
\widetilde\Phi_r^A
V^{A_1}\cdots V^{A_n}
(T_{A_1}\cdots T_{A_n})^B{}_C\Phi_r^C.}
\tag{5A.53}
$$

The ordered adjoint color chain is

$$
(T_{\emptyset})^B{}_C=\delta^B{}_C,
\qquad
(T_{A_1}\cdots T_{A_n})^B{}_C
=i^n c_{A_1D_1}{}^B c_{A_2D_2}{}^{D_1}\cdots
c_{A_nC}{}^{D_{n-1}},\qquad n\geq1.
\tag{5A.53a}
$$

Labeled differentiation of the $n$ vector legs gives the exact
ordered color sum

$$
\boxed{
\left.
\frac{\delta^n S_R^{\mathrm{mat}}}
{\delta V^{B_1}\cdots\delta V^{B_n}}
\right|_{V=0}
=\eta_Rh\kappa_{AB}\sum_{r=1}^{m_N}\int_{R,8}
\widetilde\Phi_r^A
\left[\frac1{n!}\sum_{\pi\in S_n}
T_{B_{\pi(1)}}\cdots T_{B_{\pi(n)}}\right]^B{}_C
\Phi_r^C.}
\tag{5A.54}
$$

The labeled $\mathcal N=4$ chiral and antichiral cubic primitives are

$$
\boxed{
\mathcal V_{R,\Phi\Phi\Phi}
=-\eta_R\sqrt2h\,\varepsilon_{r_1r_2r_3}
c_{A_1A_2A_3},
\qquad
\mathcal V_{R,\widetilde\Phi\widetilde\Phi\widetilde\Phi}
=-\eta_R\sqrt2h\,\varepsilon_{r_1r_2r_3}
c_{A_1A_2A_3}.}
\tag{5A.55}
$$

Let $B_n$ be fixed by

$$
\frac z{e^z-1}=\sum_{n=0}^{\infty}\frac{B_n}{n!}z^n,
\qquad
B_0=1,\qquad B_1=-\frac12,\qquad B_2=\frac16,\qquad B_3=0.
\tag{5A.56}
$$

Then the exact BRST word expansion is

$$
\boxed{
\mathbf s_RV
=i\sum_{p,q\ge0}\frac{B_{p+q}}{p!q!}
\left[(-1)^qV^p\widetilde{\mathfrak c}_RV^q
-(-1)^pV^p\mathfrak c_RV^q\right].}
\tag{5A.57}
$$

At trivial background, the complete FP action is

$$
\boxed{
S_R^{\mathrm{FP}}
=\frac14\int_{R,+}\mathfrak c'_{R,+}\bar D_R^2(\mathbf s_RV)
+\frac14\int_{R,-}\widetilde{\mathfrak c}'_{R,-}D_R^2(\mathbf s_RV).}
\tag{5A.58}
$$

For every $p,q\ge0$, its two ghost-word coefficients are

$$
\boxed{
g^{\widetilde c}_{pq}
=\frac i4\frac{B_{p+q}(-1)^q}{p!q!},
\qquad
g^c_{pq}
=-\frac i4\frac{B_{p+q}(-1)^p}{p!q!}.}
\tag{5A.59}
$$

The free FP term follows by chirality:

$$
\boxed{
S_{R,\mathrm{FP}}^{(2)}
=\frac i4\int_{R,+}\mathfrak c'_{R,+}\bar D_R^2
\widetilde{\mathfrak c}_R
-\frac i4\int_{R,-}\widetilde{\mathfrak c}'_{R,-}D_R^2
\mathfrak c_R.}
\tag{5A.60}
$$

For a homogeneous ordered word $X_1\cdots X_n$, left functional
differentiation at slot $j$ gives

$$
\frac{\vec\delta}{\delta X_j}
(X_1\cdots X_n)
=(-1)^{\epsilon_{X_j}\sum_{k<j}\epsilon_{X_k}}
X_1\cdots\widehat X_j\cdots X_n.
\tag{5A.61}
$$

For labeled legs permuted by $\pi$,

$$
(-1)^{\kappa(\pi)}
:=(-1)^{\sum_{i<j,\,\pi(i)>\pi(j)}
\epsilon_i\epsilon_j},
\qquad
\mathcal C_R[X_1,\ldots,X_n]
:=
\frac{\vec\delta}{\delta X_n}\cdots
\frac{\vec\delta}{\delta X_1}S_R.
\tag{5A.62}
$$

Thus every connected coordinate-superspace graph $G$ has primitive
weight

$$
\boxed{
\mathfrak W_R(G)
=\tau_R^{|V(G)|}(-\tau_R^{-1})^{|E(G)|}
\left(\prod_{v\in V(G)}\mathcal C_v\right)
\left(\prod_{e\in E(G)}K_e^{-1}\right)
(-1)^{\kappa_G},
\qquad
\tau_L=\frac i\hbar,\qquad\tau_E=-\frac1\hbar,
\qquad
-\tau_L^{-1}=i\hbar,\qquad-\tau_E^{-1}=\hbar.}
\tag{5A.63}
$$

Here $\mathcal C_v$ is obtained only from (5A.52)--(5A.60) by the
ordered rule (5A.61)--(5A.62).  This is the labeled-graph weight.  An
unlabeled graph is divided once by the automorphism group preserving
field type, chirality, edge orientation, derivative slot, and ordered
color word.  Equation (5A.63) becomes a numerical Feynman rule only
after every $K_e^{-1}$ and integration cycle is locked.

### 5A.10 Conditional Euclidean Fermi--Feynman algebra

This section is **CONDITIONAL**.  Fix only inside this section

$$
\Box_E:=\delta^{mn}\partial_m\partial_n,
\qquad
\mathcal P_+:=\frac{\bar D_E^2D_E^2}{16\Box_E},
\qquad
\mathcal P_-:=\frac{D_E^2\bar D_E^2}{16\Box_E},
\qquad
\mathcal P_T:=-\frac{D_E^a\bar D_E^2D_{Ea}}{8\Box_E},
\qquad
\mathcal P_0:=\mathcal P_++\mathcal P_-.
\tag{5A.64}
$$

Assume a residual-free domain on which $\Box_E^{-1}$ exists and

$$
\bar D^2D^2\bar D^2=16\Box_E\bar D^2,
\qquad
D^2\bar D^2D^2=16\Box_ED^2,
\qquad
-D^a\bar D^2D_a=8\Box_E-\frac12\{D^2,\bar D^2\}.
\tag{5A.65}
$$

Then direct multiplication gives

$$
\mathcal P_i\mathcal P_j=\delta_{ij}\mathcal P_i,
\qquad
\mathcal P_T+\mathcal P_++\mathcal P_-=1,
\qquad
i,j\in\{T,+,-\}.
\tag{5A.66}
$$

The conditional Fermi--Feynman quadratic form is

$$
\boxed{
S_{E,V}^{(2)}
=\frac h4\int_{E,8}V\cdot\Box_E
(\mathcal P_T+\mathcal P_0)V
=\frac12\int_{E,8}V^AK_{E,AB}^VV^B.}
\tag{5A.67}
$$

$$
\boxed{
K_{E,AB}^V=\frac h2\kappa_{AB}\Box_E,
\qquad
(K_E^V)^{-1\,AB}=2g^2\kappa^{AB}\Box_E^{-1}.}
\tag{5A.68}
$$

$$
K_E^V(K_E^V)^{-1}=hg^2\Box_E\Box_E^{-1}=1,
\qquad
\boxed{G_E^{VV}:=\hbar(K_E^V)^{-1}
=2\hbar g^2\kappa^{-1}\Box_E^{-1}.}
\tag{5A.69}
$$

The two pieces are

$$
S_{E,V,\mathrm{inv}}^{(2)}
=\frac h4\int_{E,8}V\cdot\Box_E\mathcal P_TV,
\qquad
S_{E,V,\mathrm{gf}}^{(2)}
=\frac h4\int_{E,8}V\cdot\Box_E\mathcal P_0V.
\tag{5A.70}
$$

The vector component normalization is

$$
V_E\big|_A=-2i\vartheta\sigma_E^m\bar\vartheta A_m,
\qquad
[V_E\Box_EV_E]_D\big|_{A^2}=-2A_m\Box_EA_m,
\qquad
\frac h4[V_E\Box_EV_E]_D\big|_{A^2}
=-\frac h2A_m\Box_EA_m.
\tag{5A.71}
$$

Define the constrained identity kernels

$$
\mathbf1_+:=\mathcal P_+\delta_E^8(z-z'),
\qquad
\mathbf1_-:=\mathcal P_-\delta_E^8(z-z'),
\qquad
\mathcal P_+\mathbf1_+=\mathbf1_+,
\qquad
\mathcal P_-\mathbf1_-=\mathbf1_-.
\tag{5A.72}
$$

For $S_{E,\Phi}^{(2)}=-h\int_{E,8}\widetilde\Phi\cdot\Phi$,

$$
\boxed{
K_{E,AB}^{\Phi\widetilde\Phi}
=-h\kappa_{AB}\mathbf1_+,
\qquad
(K_E^{\Phi\widetilde\Phi})^{-1\,AB}
=-g^2\kappa^{AB}\mathbf1_+,
\qquad
G_E^{\Phi\widetilde\Phi}
=-\hbar g^2\kappa^{-1}\mathcal P_+\delta_E^8(z-z').}
\tag{5A.73}
$$

The reversed orientation uses $\mathcal P_-$.  With the conditional
Fourier phase $e^{ipx}$, $\Box_E\mapsto-p^2$, and

$$
\begin{aligned}
\langle V^A(p,\vartheta_1)V^B(p',\vartheta_2)\rangle_E
&=-(2\pi)^4\delta^4(p+p')\frac{2\hbar g^2\kappa^{AB}}{p^2}
\delta^4(\vartheta_1-\vartheta_2),\\
\langle\Phi^A(p,1)\widetilde\Phi^B(p',2)\rangle_E
&=(2\pi)^4\delta^4(p+p')\frac{\hbar g^2\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\vartheta_1-\vartheta_2).
\end{aligned}
\tag{5A.74}
$$

### 5A.11 Exact locality obstruction for the Fermi--Feynman map

On the conditional domain (5A.64)--(5A.66), set

$$
\mathcal A_E:=
\begin{pmatrix}0&-\bar D_E^2/4\\-D_E^2/4&0\end{pmatrix},
\qquad
\mathcal A_E^2=\Box_E\mathbf1,
\qquad
\mathcal Y_{E,\mathrm{FF}}^{-1}:=\frac h2\mathcal A_E,
\qquad
\mathcal Y_{E,\mathrm{FF}}:=2g^2\frac{\mathcal A_E}{\Box_E}.
\tag{5A.75}
$$

Explicitly,

$$
\mathcal Y_{E,\mathrm{FF}}
=-\frac{g^2}{2}
\begin{pmatrix}0&\bar D_E^2/\Box_E\\D_E^2/\Box_E&0\end{pmatrix},
\qquad
\mathcal Y_{E,\mathrm{FF}}\mathcal Y_{E,\mathrm{FF}}^{-1}=1.
\tag{5A.76}
$$

With $\mathcal F_+=-\bar D_E^2V/4$ and
$\mathcal F_-=-D_E^2V/4$,

$$
\int_{E,8}\mathcal F_-\cdot\mathcal F_+
=\frac1{16}\int_{E,8}(D_E^2V)\cdot(\bar D_E^2V)
=\frac12\int_{E,8}V\cdot\Box_E\mathcal P_0V.
\tag{5A.77}
$$

Therefore

$$
\frac12\langle\mathcal Y_{E,\mathrm{FF}}^{-1}\mathcal F,
\mathcal F\rangle_E
=\frac h2\int_{E,8}\mathcal F_-\cdot\mathcal F_+
=\frac h4\int_{E,8}V\cdot\Box_E\mathcal P_0V.
\tag{5A.78}
$$

However,

$$
\boxed{
\mathcal Y_{E,\mathrm{FF}}\text{ contains }\Box_E^{-1};
\qquad
\operatorname{supp}(\Box_E^{-1}X)
\not\subseteq\operatorname{supp}(X);
\qquad
\mathcal Y_{E,\mathrm{FF}}\text{ is nonlocal}.}
\tag{5A.79}
$$

Thus (5A.75) violates the locality requirement of Step 3D.88a.
Equations (5A.64)--(5A.78) are not an admissible completed
perturbative slice of the current contract.

### 5A.12 Blocker ledger

Exact blocker tokens:
`BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED`,
`BLOCKED_STEP5A_NK_BRANCH_UNSELECTED`,
`BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED`, and
`BLOCKED_STEP3D_LC_VECTOR_CYCLE`.

$$
\boxed{
\begin{array}{ll}
\mathrm{BLOCKED\_STEP5A\_UNIQUE\_PROPAGATORS\_PERTURBATIVE\_SLICE\_UNFIXED}
&\text{No admissible residual-free local slice and cycle are locked},\\
\mathrm{BLOCKED\_STEP5A\_NK\_BRANCH\_UNSELECTED}
&\text{No Step-3D.95b Nielsen--Kallosh branch is selected},\\
\mathrm{BLOCKED\_STEP5A\_MOMENTUM\_RULES\_FOURIER\_DRED\_LEDGER\_UNFIXED}
&\text{Fourier phase, all-incoming convention, and DRED ledger are absent},\\
\mathrm{BLOCKED\_STEP3D\_LC\_VECTOR\_CYCLE}
&\text{The Lorentzian vector integration cycle remains unfixed}.
\end{array}}
\tag{5A.80}
$$

$$
\boxed{
\text{Exact output of Step 5A}
=\{\text{component actions},\text{BV--BRST},
\text{all-order primitive coordinate grammar}\};
\qquad
\text{complete accepted Feynman rules are not claimed}.}
\tag{5A.81}
$$
