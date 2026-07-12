# 00 3+1d SUSY QFT — Convention Lock

## Step 4C. Pure \(\mathcal N=4\) super Yang--Mills

### 4C.1 \(\mathcal N=1\) superspace ansatz

$$
c_{ABC}:=\kappa_{CD}c_{AB}{}^D=c_{[ABC]},
\qquad
h:=g^{-2}.
\tag{4C.1}
$$

For three adjoint chiral superfields, take

$$
\mathscr U_u(\Phi)
:=\frac{uh}{6}\varepsilon_{rst}c_{ABC}
\Phi_r^A\Phi_s^B\Phi_t^C.
\tag{4C.2}
$$

The second cubic is fixed, not implicit:

$$
\widetilde{\mathscr U}_{u,L}
:=(\mathscr U_{u,L})^\dagger,
\qquad
\widetilde{\mathscr U}_{u,E}(\widetilde\Phi)
:=\frac{uh}{6}\varepsilon_{rst}c_{ABC}
\widetilde\Phi_r^A\widetilde\Phi_s^B\widetilde\Phi_t^C.
\tag{4C.2a}
$$

The Lorentzian action ansatz is

$$
\boxed{
\begin{aligned}
S_L^{(4)}=\int d^4x_L\Big\{&
h\kappa_{AB}
[\widetilde\Phi_r^A(\mathcal E_{\rm ad})^B{}_C\Phi_r^C]_D\\
&+\frac14[f_{AB}\mathcal W_L^{Aa}\mathcal W^B_{La}]_F
+\frac14[\bar f_{AB}\widetilde{\mathcal W}_{L\dot a}^A
\widetilde{\mathcal W}_L^{B\dot a}]_{\widetilde F}\\
&+[\mathscr U_u]_F+[\widetilde{\mathscr U}_u]_{\widetilde F}
\Big\}.
\end{aligned}}
\tag{4C.3}
$$

The Euclidean action is obtained independently by the Step-3A
Euclidean projectors:

$$
\boxed{
\begin{aligned}
S_E^{(4)}=-\int d^4x_E\Big\{&
h\kappa_{AB}
[\widetilde\Phi_r^A(\mathcal E_{\rm ad})^B{}_C\Phi_r^C]_D\\
&+\frac14[f_{AB}\mathcal W_E^{Aa}\mathcal W^B_{Ea}]_F
+\frac14[\widetilde f_{AB}\widetilde{\mathcal W}_{E\dot a}^A
\widetilde{\mathcal W}_E^{B\dot a}]_{\widetilde F}\\
&+[\mathscr U_u]_F+[\widetilde{\mathscr U}_u]_{\widetilde F}
\Big\}.
\end{aligned}}
\tag{4C.4}
$$

### 4C.2 Cubic coefficient from the two Yukawa families

Use the Step-4 definitions

$$
\Lambda^{\mathcal I}
=(\psi_1,\psi_2,\psi_3,\lambda),
\qquad
\varphi^{r4}=\phi_r,
\qquad
\varphi^{rs}=\varepsilon^{rst}\widetilde\phi_t.
\tag{4C.5}
$$

The unique index contraction with one scalar and two left-handed
fermions is

$$
\mathcal L_{Y,L}^{(+)}
=Chc_{ABC}\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}.
\tag{4C.6}
$$

Direct expansion of all ordered \((\mathcal I,\mathcal J)\) slots gives

$$
\boxed{
\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
=2\widetilde\phi_r^A\psi_r^B\lambda^C
+\varepsilon_{rst}\phi_t^A\psi_r^B\psi_s^C.}
\tag{4C.7}
$$

The Step-3B gauge Yukawa is

$$
\begin{aligned}
i\sqrt2h\widetilde\phi_B(T_A^{\rm ad})^B{}_C
\lambda^A\psi^C
&=i\sqrt2h\widetilde\phi_B(ic_{AC}{}^B)
\lambda^A\psi^C\\
&=\sqrt2h c_{ABC}\widetilde\phi^A\psi^B\lambda^C.
\end{aligned}
\tag{4C.8}
$$

Comparison of (4C.7) and (4C.8) gives

$$
2C=\sqrt2,
\qquad
C=\frac1{\sqrt2}.
\tag{4C.9}
$$

Two derivatives of (4C.2) give

$$
(\mathscr U_u)_{rA,sB}
=uh\varepsilon_{rst}c_{ABC}\phi_t^C,
\tag{4C.10}
$$

so its Step-3B fermion term is

$$
-\frac12(\mathscr U_u)_{rA,sB}\psi_r^A\psi_s^B
=-\frac{uh}{2}\varepsilon_{rst}c_{ABC}
\phi_t^C\psi_r^A\psi_s^B.
\tag{4C.11}
$$

Comparison with (4C.7) gives

$$
-\frac u2=C=\frac1{\sqrt2},
\qquad
\boxed{u=-\sqrt2.}
\tag{4C.12}
$$

Therefore

$$
\boxed{
\mathscr U_4
=-\frac{\sqrt2}{6g^2}\varepsilon_{rst}c_{ABC}
\Phi_r^A\Phi_s^B\Phi_t^C.}
\tag{4C.13}
$$

### 4C.3 Lorentzian \(\mathcal N=1\) off-shell components

The Lorentzian off-shell contour is

$$
\boxed{
\widetilde\phi_{r,L}:=\bar\phi_r,
\qquad
\widetilde\psi_{r,L}:=\bar\psi_r,
\qquad
\widetilde F_{r,L}:=\bar F_r=(F_{r,L})^\dagger.}
\tag{4C.13a}
$$

Direct Step-3B projection of (4C.3) gives

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm off}}^{(4)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
+i\bar\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B
+\frac12\mathscr D^A\mathscr D^B\\
&\quad
-(\mathcal D_\mu\widetilde\phi_r)^A
(\mathcal D^\mu\phi_r)^B
+i\widetilde\psi_r^A\bar\sigma_L^\mu
\mathcal D_\mu\psi_r^B
+\widetilde F_r^AF_r^B\\
&\quad
+i\mathscr D^A(\phi_r\times\widetilde\phi_r)^B
\Big]\\
&+\sqrt2h c_{ABC}\left(
\widetilde\phi_r^A\psi_r^B\lambda^C
+\phi_r^A\widetilde\psi_r^B\widetilde\lambda^C
\right)\\
&-\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}\left(
F_r^A\phi_s^B\phi_t^C
+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C
\right)\\
&+\frac h{\sqrt2}\varepsilon_{rst}c_{ABC}\left(
\phi_t^A\psi_r^B\psi_s^C
+\widetilde\phi_t^A\widetilde\psi_r^B
\widetilde\psi_s^C
\right)\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{4C.14}
$$

The three auxiliary equations are obtained without completing a square:

$$
\frac{\partial\mathcal L}{\partial\mathscr D^A}
=h\kappa_{AB}\left[\mathscr D^B
+i(\phi_r\times\widetilde\phi_r)^B\right]=0,
\tag{4C.15}
$$

$$
\frac{\partial\mathcal L}{\partial\widetilde F_r^A}
=h\kappa_{AB}\left[F_r^B
-\frac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t)^B\right]=0,
\tag{4C.16}
$$

$$
\frac{\partial\mathcal L}{\partial F_r^A}
=h\kappa_{AB}\left[\widetilde F_r^B
-\frac1{\sqrt2}\varepsilon_{rst}
(\phi_s\times\phi_t)^B\right]=0.
\tag{4C.17}
$$

Thus

$$
\boxed{
\begin{aligned}
\mathscr D&=-i(\phi_r\times\widetilde\phi_r),\\
F_r&=\frac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t),\\
\widetilde F_r&=\frac1{\sqrt2}\varepsilon_{rst}
(\phi_s\times\phi_t).
\end{aligned}}
\tag{4C.18}
$$

### 4C.4 Scalar and Yukawa packaging identities

Define

$$
C_0:=\phi_r\times\widetilde\phi_r.
\tag{4C.19}
$$

Substitution of (4C.18) into (4C.14) gives

$$
\begin{aligned}
\mathcal L_{L,{\rm pot}}^{(4)}={}&
\frac h2\operatorname{tr}_\kappa(C_0C_0)\\
&-2h\sum_{(st)=(23),(31),(12)}
\operatorname{tr}_\kappa
\left[(\phi_s\times\phi_t)
(\widetilde\phi_s\times\widetilde\phi_t)\right].
\end{aligned}
\tag{4C.20}
$$

For

$$
\mathsf B(X,Y;Z,W)
:=\operatorname{tr}_\kappa[(X\times Y)(Z\times W)],
\tag{4C.20a}
$$

invariance of \(\kappa\) and the Jacobi identity give

$$
\mathsf B(X,Y;Z,W)-\mathsf B(X,Z;Y,W)
+\mathsf B(X,W;Y,Z)=0.
\tag{4C.20b}
$$

Expansion of the \(4^4\) internal-index slots followed only by
(4C.20b) gives

$$
\boxed{
\begin{aligned}
&\operatorname{tr}_\kappa
\left[(\varphi^{\mathcal I\mathcal J}
\times\varphi^{\mathcal K\mathcal L})
(\widetilde\varphi_{\mathcal I\mathcal J}
\times\widetilde\varphi_{\mathcal K\mathcal L})\right]\\
&\qquad=-8\operatorname{tr}_\kappa(C_0C_0)
+32\sum_{r<s}\operatorname{tr}_\kappa
\left[(\phi_r\times\phi_s)
(\widetilde\phi_r\times\widetilde\phi_s)\right].
\end{aligned}}
\tag{4C.21}
$$

Equations (4C.7), its barred counterpart, and (4C.21) give the
Lorentzian on-shell action

$$
\boxed{
\begin{aligned}
\mathcal L_L^{(4)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-\frac14(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})^A
(\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J})^B\\
&\qquad
+i\bar\Lambda_{\dot a\mathcal I}^A
(\bar\sigma_L^\mu)^{\dot aa}
(\mathcal D_\mu\Lambda_a^{\mathcal I})^B\\
&\qquad
-\frac1{16}
(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B
\Big]\\
&+\frac h{\sqrt2}c_{ABC}\left(
\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
+\varphi^{\mathcal I\mathcal J,A}
\bar\Lambda_{\mathcal I}^B\bar\Lambda_{\mathcal J}^C
\right)\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{4C.22}
$$

### 4C.5 Sixteen Lorentzian transformations

Define

$$
\mathcal M^{\mathcal I}{}_{\mathcal K}
:=\varphi^{\mathcal I\mathcal J}
\times\widetilde\varphi_{\mathcal J\mathcal K}.
\tag{4C.23}
$$

The complete on-shell ansatz is fixed by its manifest
\(\mathcal I=4\) restriction and \(SU(4)_R\) covariance:

$$
\boxed{
\delta_LA_\mu
=-i\varepsilon^{\mathcal I}\sigma_{L,\mu}
\bar\Lambda_{\mathcal I}
-i\bar\varepsilon_{\mathcal I}\bar\sigma_{L,\mu}
\Lambda^{\mathcal I}.}
\tag{4C.24}
$$

$$
\boxed{
\begin{aligned}
\delta_L\varphi^{\mathcal I\mathcal J}
={}&\sqrt2\left(
\varepsilon^{\mathcal I}\Lambda^{\mathcal J}
-\varepsilon^{\mathcal J}\Lambda^{\mathcal I}\right)\\
&+\sqrt2\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\bar\varepsilon_{\mathcal K}\bar\Lambda_{\mathcal L}.
\end{aligned}}
\tag{4C.25}
$$

Hence

$$
\boxed{
\begin{aligned}
\delta_L\widetilde\varphi_{\mathcal I\mathcal J}
&=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\delta_L\varphi^{\mathcal K\mathcal L}\\
&=\sqrt2\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varepsilon^{\mathcal K}\Lambda^{\mathcal L}
+\sqrt2(\bar\varepsilon_{\mathcal I}\bar\Lambda_{\mathcal J}
-\bar\varepsilon_{\mathcal J}\bar\Lambda_{\mathcal I}).
\end{aligned}}
\tag{4C.25a}
$$

$$
\boxed{
\begin{aligned}
\delta_L\Lambda_a^{\mathcal I}={}&
(\sigma_L^{\mu\nu})_a{}^b
\varepsilon_b^{\mathcal I}F_{\mu\nu}
+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\bar\varepsilon_{\mathcal J}^{\dot b}
\mathcal D_\mu\varphi^{\mathcal I\mathcal J}\\
&+\mathcal M^{\mathcal I}{}_{\mathcal K}
\varepsilon_a^{\mathcal K},
\end{aligned}}
\tag{4C.26}
$$

$$
\boxed{
\begin{aligned}
\delta_L\bar\Lambda_{\dot a\mathcal I}={}&
-\bar\varepsilon_{\dot b\mathcal I}
(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}F_{\mu\nu}
-i\sqrt2\varepsilon^{\mathcal Jb}(\sigma_L^\mu)_{b\dot a}
\mathcal D_\mu\widetilde\varphi_{\mathcal I\mathcal J}\\
&+(\widetilde\varphi_{\mathcal I\mathcal J}
\times\varphi^{\mathcal J\mathcal K})
\bar\varepsilon_{\dot a\mathcal K}.
\end{aligned}}
\tag{4C.27}
$$

For \(\varepsilon^{1,2,3}=0\), equations (4C.24)--(4C.27) give

$$
\begin{aligned}
\delta\phi_r&=-\sqrt2\varepsilon^4\psi_r,\\
\delta\psi_r&=-\sqrt2\varepsilon^4F_r
+i\sqrt2\sigma_L^\mu\bar\varepsilon_4
\mathcal D_\mu\phi_r,\\
\delta\lambda&=\sigma_L^{\mu\nu}\varepsilon^4F_{\mu\nu}
-i\varepsilon^4\mathscr D,\\
\delta A_\mu&=-i\varepsilon^4\sigma_{L,\mu}\bar\lambda
-i\bar\varepsilon_4\bar\sigma_{L,\mu}\lambda,
\end{aligned}
\tag{4C.28}
$$

with (4C.18); this is the auxiliary-EOM restriction of Step 4A plus
three Step-3B adjoint chiral multiplets.

Let \(\delta^{(\mathcal I)}\) denote the coefficient of
\(\varepsilon^{\mathcal I}\).  Before auxiliary elimination,

$$
\delta^{(4)}S_{L,{\rm off}}^{(4)}=0
\tag{4C.28a}
$$

follows coefficientwise from the Step-3B superspace projectors.  Since
the auxiliary equations are algebraic,

$$
\begin{aligned}
\delta^{(4)}S_{L,{\rm on}}^{(4)}
&=\left.\delta^{(4)}S_{L,{\rm off}}^{(4)}\right|_{\mathcal E_{\rm aux}=0}
+\left.\frac{\delta S_{L,{\rm off}}^{(4)}}
{\delta Z_{\rm aux}}\delta^{(4)}Z_{\rm aux}
\right|_{\mathcal E_{\rm aux}=0}\\
&=0+0.
\end{aligned}
\tag{4C.28b}
$$

For each \(\mathcal I\), choose
\(U_{\mathcal I}\in SU(4)_R\) with
\(U_{\mathcal I}e_4=e_{\mathcal I}\).  Equations (4C.22) and
(4C.24)--(4C.27) are (SU(4)_R)-covariant, hence

$$
\boxed{
\delta^{(\mathcal I)}S_L^{(4)}[\mathbb V]
=\delta^{(4)}S_L^{(4)}[U_{\mathcal I}^{-1}\mathbb V]
=0,
\qquad
\mathcal I=1,2,3,4.}
\tag{4C.28c}
$$

The same polynomial index argument proves
\(\delta_E^{(\mathcal I)}S_E^{(4)}=0\); no Euclidean dagger is used.

### 4C.6 Exact \(\mathcal N=1\)-superspace reconstruction

For every one of the sixteen component transformations
(4C.24)--(4C.27), first vary the composite auxiliaries:

$$
\begin{aligned}
\delta\mathscr D
&=-i\left[(\delta\phi_r)\times\widetilde\phi_r
+\phi_r\times(\delta\widetilde\phi_r)\right],\\
\delta F_r
&=\frac1{\sqrt2}\varepsilon_{rst}\left[
(\delta\widetilde\phi_s)\times\widetilde\phi_t
+\widetilde\phi_s\times(\delta\widetilde\phi_t)\right],\\
\delta\widetilde F_r
&=\frac1{\sqrt2}\varepsilon_{rst}\left[
(\delta\phi_s)\times\phi_t
+\phi_s\times(\delta\phi_t)\right].
\end{aligned}
\tag{4C.29}
$$

Define the transformed chiral and antichiral superfields by their
locked Step-3B component reconstruction:

$$
\boxed{
\delta\Phi_r(y_L,\vartheta)
:=\delta\phi_r(y_L)
+\sqrt2\vartheta^a\delta\psi_{ra}(y_L)
+\vartheta^2\delta F_r(y_L),}
\tag{4C.30}
$$

$$
\boxed{
\delta\widetilde\Phi_r(\widetilde y_L,\bar\vartheta)
:=\delta\widetilde\phi_r(\widetilde y_L)
+\sqrt2\bar\vartheta_{\dot a}
\delta\widetilde\psi_r^{\dot a}(\widetilde y_L)
+\bar\vartheta^2\delta\widetilde F_r(\widetilde y_L).}
\tag{4C.31}
$$

Because (4C.30) depends only on \((y_L,\vartheta)\) and (4C.31)
only on \((\widetilde y_L,\bar\vartheta)\),

$$
\bar D_{L\dot a}\delta\Phi_r=0,
\qquad
D_{La}\delta\widetilde\Phi_r=0.
\tag{4C.32}
$$

The Wess--Zumino-gauge vector superfield is reconstructed without a
nonchiral naive ansatz:

$$
\boxed{
\begin{aligned}
\delta\mathcal V_L^{\rm WZ}={}&
-2\vartheta\sigma_L^\mu\bar\vartheta\,\delta A_\mu
+2i\vartheta^2\bar\vartheta\,\delta\bar\lambda\\
&-2i\bar\vartheta^2\vartheta\,\delta\lambda
+\vartheta^2\bar\vartheta^2\delta\mathscr D.
\end{aligned}}
\tag{4C.33}
$$

For \(\mathcal E=e^{\mathcal V}\), its exact non-Abelian variation is

$$
\boxed{
\mathcal E^{-1}\delta\mathcal E
=\int_0^1ds\ e^{-s\mathcal V}
(\delta\mathcal V)e^{s\mathcal V}.}
\tag{4C.34}
$$

The field-strength variation is then the functional variation of its
Step-3A definition:

$$
\boxed{
\delta\mathcal W_a
=-\frac18\bar D^2\delta
\left(\mathcal E^{-1}D_a\mathcal E\right),
\qquad
\bar D_{\dot a}\delta\mathcal W_b=0.}
\tag{4C.35}
$$

The independent Euclidean reconstruction is

$$
\boxed{
\begin{aligned}
\delta_E\Phi_r(y_E,\vartheta)
&:=\delta_E\phi_r(y_E)
+\sqrt2\vartheta\delta_E\psi_r(y_E)
+\vartheta^2\delta_EF_r(y_E),\\
\delta_E\widetilde\Phi_r(\widetilde y_E,\bar\vartheta)
&:=\delta_E\widetilde\phi_r(\widetilde y_E)
+\sqrt2\bar\vartheta\delta_E\widetilde\psi_r(\widetilde y_E)
+\bar\vartheta^2\delta_E\widetilde F_r(\widetilde y_E).
\end{aligned}}
\tag{4C.35a}
$$

$$
\boxed{
\begin{aligned}
\delta_E\mathcal V_E^{\rm WZ}={}&
-2i\vartheta\sigma_E^m\bar\vartheta\,\delta_EA_m
+2i\vartheta^2\bar\vartheta\,\delta_E\widetilde\lambda
-2i\bar\vartheta^2\vartheta\,\delta_E\lambda
+\vartheta^2\bar\vartheta^2\delta_E\mathscr D.
\end{aligned}}
\tag{4C.35b}
$$

For

$$
\Xi_E:=\mathcal E_E^{-1}\delta_E\mathcal E_E
=\int_0^1ds\ e^{-s\mathcal V_E}
(\delta_E\mathcal V_E)e^{s\mathcal V_E},
\tag{4C.35c}
$$

one has

$$
\boxed{
\delta_E\mathcal W_{Ea}
=-\frac18\bar D_E^2
\left(D_{Ea}\Xi_E+[\Gamma_{Ea},\Xi_E]\right),
\qquad
\bar D_{E\dot a}\delta_E\mathcal W_{Eb}=0.}
\tag{4C.35d}
$$

Equations (4C.29)--(4C.35) are the complete non-Abelian on-shell
Lorentzian form; equations (4C.35a)--(4C.35d) are its independent
Euclidean counterpart.  They add no independent auxiliary
field and preserve Wess--Zumino gauge coefficient by coefficient.

### 4C.7 Lorentzian closure surface

Define

$$
v_L^\mu
=2i\left(
\varepsilon_1^{\mathcal I}\sigma_L^\mu
\bar\varepsilon_{2\mathcal I}
-\varepsilon_2^{\mathcal I}\sigma_L^\mu
\bar\varepsilon_{1\mathcal I}\right),
\tag{4C.36}
$$

$$
\begin{aligned}
\Omega:=-\sqrt2\Big[&
(\varepsilon_1^{\mathcal I}\varepsilon_2^{\mathcal J}
-\varepsilon_2^{\mathcal I}\varepsilon_1^{\mathcal J})
\widetilde\varphi_{\mathcal I\mathcal J}\\
&+(\bar\varepsilon_{1\mathcal I}\bar\varepsilon_{2\mathcal J}
-\bar\varepsilon_{2\mathcal I}\bar\varepsilon_{1\mathcal J})
\varphi^{\mathcal I\mathcal J}\Big].
\end{aligned}
\tag{4C.37}
$$

The bosonic substitutions give

$$
\boxed{
\begin{aligned}
[\delta_1,\delta_2]A_\mu
&=v_L^\nu F_{\nu\mu}-\mathcal D_\mu\Omega,\\
[\delta_1,\delta_2]\varphi^{\mathcal I\mathcal J}
&=v_L^\mu\mathcal D_\mu\varphi^{\mathcal I\mathcal J}
+\Omega\times\varphi^{\mathcal I\mathcal J}.
\end{aligned}}
\tag{4C.38}
$$

Thus the ordinary-coordinate gauge parameter is

$$
\alpha_{12,L}=-v_L^\mu A_\mu-\Omega.
\tag{4C.38a}
$$

The fermion Euler operators are

$$
\boxed{
\mathcal E_{a\mathcal I}
:=-i(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal I}^{\dot b}
+\sqrt2(\widetilde\varphi_{\mathcal I\mathcal J}
\times\Lambda^{\mathcal J})_a,}
\tag{4C.39}
$$

$$
\boxed{
\widetilde{\mathcal E}_{\dot a}^{\mathcal I}
:=i(\bar\sigma_L^\mu)_{\dot ab}
\mathcal D_\mu\Lambda^{\mathcal I b}
+\sqrt2(\varphi^{\mathcal I\mathcal J}
\times\bar\Lambda_{\mathcal J})_{\dot a}.}
\tag{4C.40}
$$

The unreduced fermion remainder is fixed, with no suppressed term, by

$$
\begin{aligned}
\mathscr R_a^{\mathcal I}:={}&
(\sigma_L^{\mu\nu})_a{}^b
\left[\varepsilon_{2b}^{\mathcal I}\delta_1F_{\mu\nu}
-\varepsilon_{1b}^{\mathcal I}\delta_2F_{\mu\nu}\right]\\
&+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\left[\bar\varepsilon_{2\mathcal J}^{\dot b}
\delta_1(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})
-\bar\varepsilon_{1\mathcal J}^{\dot b}
\delta_2(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})\right]\\
&+\delta_1\mathcal M^{\mathcal I}{}_{\mathcal K}
\varepsilon_{2a}^{\mathcal K}
-\delta_2\mathcal M^{\mathcal I}{}_{\mathcal K}
\varepsilon_{1a}^{\mathcal K}\\
&-v_L^\mu\mathcal D_\mu\Lambda_a^{\mathcal I}
-(\Omega\times\Lambda^{\mathcal I})_a,
\end{aligned}
\tag{4C.41}
$$

where

$$
\delta(\mathcal D_\mu\varphi)
=\mathcal D_\mu(\delta\varphi)
+(\delta A_\mu)\times\varphi.
\tag{4C.42}
$$

The exact EOM reduction of (4C.41) is recorded after the independent
index reduction in Section 4C.11; the elementary matrix identities
used there are machine-checked separately.

### 4C.8 Euclidean action and transformations

Direct Euclidean projection of (4C.4) gives

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm off}}^{(4)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B
-\frac12\mathscr D^A\mathscr D^B\\
&\qquad
+(\mathcal D_m\widetilde\phi_r)^A
(\mathcal D_m\phi_r)^B
+\widetilde\psi_r^A\bar\sigma_E^m\mathcal D_m\psi_r^B
-\widetilde F_r^AF_r^B\\
&\qquad
-i\mathscr D^A(\phi_r\times\widetilde\phi_r)^B
\Big]\\
&-\sqrt2h c_{ABC}\left(
\widetilde\phi_r^A\psi_r^B\lambda^C
+\phi_r^A\widetilde\psi_r^B\widetilde\lambda^C
\right)\\
&+\frac{\sqrt2h}{2}\varepsilon_{rst}c_{ABC}\left(
F_r^A\phi_s^B\phi_t^C
+\widetilde F_r^A\widetilde\phi_s^B\widetilde\phi_t^C
\right)\\
&-\frac h{\sqrt2}\varepsilon_{rst}c_{ABC}\left(
\phi_t^A\psi_r^B\psi_s^C
+\widetilde\phi_t^A\widetilde\psi_r^B\widetilde\psi_s^C
\right)\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}
F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{4C.42a}
$$

Its ordered auxiliary equations are

$$
\boxed{
\mathscr D=-i(\phi_r\times\widetilde\phi_r),
\qquad
F_r=\frac1{\sqrt2}\varepsilon_{rst}
(\widetilde\phi_s\times\widetilde\phi_t),
\qquad
\widetilde F_r=\frac1{\sqrt2}\varepsilon_{rst}
(\phi_s\times\phi_t).}
\tag{4C.42b}
$$

Substitution into (4C.42a) gives

$$
\boxed{
\begin{aligned}
\mathcal L_E^{(4)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+\frac14(\mathcal D_m\varphi^{\mathcal I\mathcal J})^A
(\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J})^B\\
&\qquad
+\widetilde\Lambda_{\dot a\mathcal I}^A
(\bar\sigma_E^m)^{\dot aa}
(\mathcal D_m\Lambda_a^{\mathcal I})^B\\
&\qquad
+\frac1{16}
(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B
\Big]\\
&-\frac h{\sqrt2}c_{ABC}\left(
\widetilde\varphi_{\mathcal I\mathcal J}^A
\Lambda^{\mathcal I B}\Lambda^{\mathcal J C}
+\varphi^{\mathcal I\mathcal J,A}
\widetilde\Lambda_{\mathcal I}^B
\widetilde\Lambda_{\mathcal J}^C
\right)\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{4C.43}
$$

The direct Euclidean transformation is

$$
\boxed{
\delta_EA_m
=\varepsilon^{\mathcal I}\sigma_{E,m}
\widetilde\Lambda_{\mathcal I}
+\widetilde\varepsilon_{\mathcal I}\bar\sigma_{E,m}
\Lambda^{\mathcal I},}
\tag{4C.44}
$$

$$
\boxed{
\begin{aligned}
\delta_E\varphi^{\mathcal I\mathcal J}
={}&\sqrt2(\varepsilon^{\mathcal I}\Lambda^{\mathcal J}
-\varepsilon^{\mathcal J}\Lambda^{\mathcal I})\\
&+\sqrt2\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\widetilde\varepsilon_{\mathcal K}
\widetilde\Lambda_{\mathcal L},
\end{aligned}}
\tag{4C.45}
$$

The second scalar tensor is not varied independently:

$$
\boxed{
\delta_E\widetilde\varphi_{\mathcal I\mathcal J}
=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\delta_E\varphi^{\mathcal K\mathcal L}
=\sqrt2\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varepsilon^{\mathcal K}\Lambda^{\mathcal L}
+\sqrt2(\widetilde\varepsilon_{\mathcal I}
\widetilde\Lambda_{\mathcal J}
-\widetilde\varepsilon_{\mathcal J}
\widetilde\Lambda_{\mathcal I}).}
\tag{4C.45a}
$$

$$
\boxed{
\begin{aligned}
\delta_E\Lambda_a^{\mathcal I}={}&
-(\sigma_E^{mn})_a{}^b\varepsilon_b^{\mathcal I}F_{mn}
-\sqrt2(\sigma_E^m)_{a\dot b}
\widetilde\varepsilon_{\mathcal J}^{\dot b}
\mathcal D_m\varphi^{\mathcal I\mathcal J}\\
&+\mathcal M^{\mathcal I}{}_{\mathcal K}
\varepsilon_a^{\mathcal K},
\end{aligned}}
\tag{4C.46}
$$

$$
\boxed{
\begin{aligned}
\delta_E\widetilde\Lambda_{\dot a\mathcal I}={}&
+\widetilde\varepsilon_{\dot b\mathcal I}
(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}F_{mn}
+\sqrt2\varepsilon^{\mathcal Jb}(\sigma_E^m)_{b\dot a}
\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J}\\
&+(\widetilde\varphi_{\mathcal I\mathcal J}
\times\varphi^{\mathcal J\mathcal K})
\widetilde\varepsilon_{\dot a\mathcal K}.
\end{aligned}}
\tag{4C.47}
$$

Equations (4C.43)--(4C.47) also follow coefficientwise from

$$
\mathcal L_E=-\mathcal L_L|_{\rm Wick},
\qquad
\sigma_L^{\mu\nu}F_{\mu\nu}|_{\rm Wick}
=-\sigma_E^{mn}F_{mn},
\qquad
\sigma_L^\mu\mathcal D_\mu|_{\rm Wick}
=i\sigma_E^m\mathcal D_m.
\tag{4C.48}
$$

### 4C.9 Raw local-parameter currents

For the Step-3B fermion ordering in (4C.22), localization of
\(\varepsilon^{\mathcal I}\) gives

$$
\mathcal R_c{}^{a,\mathcal J}{}_{\mathcal I}
:=\delta^{\mathcal J}{}_{\mathcal I}
(\sigma_L^{\rho\sigma})_c{}^aF_{\rho\sigma}
+\delta_c{}^a\mathcal M^{\mathcal J}{}_{\mathcal I}.
\tag{4C.49}
$$

Termwise contributions from \(F^2\), scalar kinetic, and fermion
kinetic terms give

$$
\boxed{
\begin{aligned}
C_{L,\mathcal I}^{\mu a}
=h\kappa_{AB}\Big[&
+iF^{A\mu\nu}(\sigma_{L,\nu})^a{}_{\dot b}
\bar\Lambda_{\mathcal I}^{B\dot b}\\
&-\sqrt2(\mathcal D^\mu
\widetilde\varphi_{\mathcal I\mathcal J})^A
\Lambda^{\mathcal JaB}\\
&+i\bar\Lambda_{\dot b\mathcal J}^A
(\bar\sigma_L^\mu)^{\dot bc}
(\mathcal R_c{}^{a,\mathcal J}{}_{\mathcal I})^B
\Big].
\end{aligned}}
\tag{4C.50}
$$

The conjugate-slot coefficient is

$$
\boxed{
\begin{aligned}
\widetilde C_L^{\mu\mathcal I}{}_{\dot a}
=h\kappa_{AB}\Big[&
-iF^{A\mu\nu}(\Lambda^{\mathcal IB}
\sigma_{L,\nu})_{\dot a}\\
&-\sqrt2(\mathcal D^\mu
\varphi^{\mathcal I\mathcal J})^A
\bar\Lambda_{\dot a\mathcal J}^B\\
&-\sqrt2\bar\Lambda_{\dot b\mathcal J}^A
(\bar\sigma_L^\mu)^{\dot bc}(\sigma_L^\rho)_{c\dot a}
(\mathcal D_\rho\varphi^{\mathcal J\mathcal I})^B
\Big].
\end{aligned}}
\tag{4C.51}
$$

The constant-parameter boundary coefficients and the exact
\(C-K\) currents are fixed in Section 4C.11.

Direct Euclidean localization gives

$$
\boxed{
\begin{aligned}
C_{E,\mathcal I}^{ma}
=h\kappa_{AB}\Big[&
+F^{Amn}(\sigma_{E,n})^a{}_{\dot b}
\widetilde\Lambda_{\mathcal I}^{B\dot b}\\
&+\sqrt2(\mathcal D^m
\widetilde\varphi_{\mathcal I\mathcal J})^A
\Lambda^{\mathcal JaB}\\
&+\widetilde\Lambda_{\dot b\mathcal J}^A
(\bar\sigma_E^m)^{\dot bc}\left[
-\delta^{\mathcal J}{}_{\mathcal I}
(\sigma_E^{rs})_c{}^aF_{rs}^B
+\delta_c{}^a(\mathcal M^{\mathcal J}{}_{\mathcal I})^B
\right]\Big].
\end{aligned}}
\tag{4C.52}
$$

### 4C.10 Reality and off-shell boundary

Lorentzian reality is (4.30).  The intrinsic Euclidean families

$$
(\phi_r,\widetilde\phi_r),
\qquad
(\Lambda^{\mathcal I},\widetilde\Lambda_{\mathcal I})
\tag{4C.53}
$$

are independent.  The packaged tensors obey (4.28) identically; the
canonical scalar contour is (4.32).

Before imposing (4C.18), the manifest Step-4A plus Step-3B
\(\mathcal N=1\) transformations close off shell on

$$
(A_M,\lambda,\widetilde\lambda,\mathscr D;
\phi_r,\psi_r,F_r;
\widetilde\phi_r,\widetilde\psi_r,\widetilde F_r).
\tag{4C.54}
$$

After imposing (4C.18), all \(SU(4)_R\)-packaged transformations
(4C.24)--(4C.27), including the \(\mathcal I=4\) slot, close only
modulo (4C.39)--(4C.40).  No finite
\(SU(4)_R\)-covariant auxiliary completion is asserted.

### 4C.11 Exact closure and Noether reduction

The scalar bilinear satisfies

$$
\mathcal M^{\mathcal I}{}_{\mathcal I}=0,
\qquad
\widetilde{\mathcal M}_{\mathcal I}{}^{\mathcal J}
:=\widetilde\varphi_{\mathcal I\mathcal K}
\times\varphi^{\mathcal K\mathcal J}
=-\mathcal M^{\mathcal J}{}_{\mathcal I}.
\tag{4C.55}
$$

For constant parameters, the three substitutions in (4C.41) are

$$
\boxed{
\begin{aligned}
\delta F_{\mu\nu}={}&
-i\varepsilon^{\mathcal K}\sigma_{L,\nu}
\mathcal D_\mu\bar\Lambda_{\mathcal K}
+i(\mathcal D_\mu\Lambda^{\mathcal K})
\sigma_{L,\nu}\bar\varepsilon_{\mathcal K}
-(\mu\leftrightarrow\nu),\\
\delta(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})={}&
\sqrt2\mathcal D_\mu
\left(\varepsilon^{\mathcal I}\Lambda^{\mathcal J}
-\varepsilon^{\mathcal J}\Lambda^{\mathcal I}\right)
+\sqrt2\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\bar\varepsilon_{\mathcal K}\mathcal D_\mu
\bar\Lambda_{\mathcal L}\\
&+\left(-i\varepsilon^{\mathcal K}\sigma_{L,\mu}
\bar\Lambda_{\mathcal K}
+i\Lambda^{\mathcal K}\sigma_{L,\mu}
\bar\varepsilon_{\mathcal K}\right)
\times\varphi^{\mathcal I\mathcal J},\\
\delta\mathcal M^{\mathcal I}{}_{\mathcal K}={}&
\sqrt2(\varepsilon^{\mathcal I}\Lambda^{\mathcal J}
-\varepsilon^{\mathcal J}\Lambda^{\mathcal I})
\times\widetilde\varphi_{\mathcal J\mathcal K}\\
&+\sqrt2\epsilon^{\mathcal I\mathcal J\mathcal M\mathcal N}
(\bar\varepsilon_{\mathcal M}\bar\Lambda_{\mathcal N})
\times\widetilde\varphi_{\mathcal J\mathcal K}\\
&+\sqrt2\varphi^{\mathcal I\mathcal J}\times
\left[\epsilon_{\mathcal J\mathcal K\mathcal M\mathcal N}
\varepsilon^{\mathcal M}\Lambda^{\mathcal N}
+\bar\varepsilon_{\mathcal J}\bar\Lambda_{\mathcal K}
-\bar\varepsilon_{\mathcal K}\bar\Lambda_{\mathcal J}
\right].
\end{aligned}}
\tag{4C.55a}
$$

No parameter or fermion has been commuted in (4C.55a).  Move every
parameter to the right and define the ordered bilinears

$$
\begin{aligned}
A^{\mathcal I\mathcal J}
&:=\varepsilon_1^{\mathcal I}\varepsilon_2^{\mathcal J}
-\varepsilon_2^{\mathcal I}\varepsilon_1^{\mathcal J},\\
A_a{}^{\mathcal I\mathcal Jb}
&:=\varepsilon_{1a}^{\mathcal I}\varepsilon_2^{\mathcal Jb}
-\varepsilon_{2a}^{\mathcal I}\varepsilon_1^{\mathcal Jb},\\
\bar A_{\mathcal K\mathcal L}
&:=\bar\varepsilon_{1\mathcal K}\bar\varepsilon_{2\mathcal L}
-\bar\varepsilon_{2\mathcal K}\bar\varepsilon_{1\mathcal L},\\
X_{a\dot b}{}^{\mathcal I}{}_{\mathcal J}
&:=\varepsilon_{1a}^{\mathcal I}
\bar\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal I}
\bar\varepsilon_{1\mathcal J\dot b},\\
T_{a\dot b}
&:=\varepsilon_{1a}^{\mathcal J}
\bar\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal J}
\bar\varepsilon_{1\mathcal J\dot b}.
\end{aligned}
\tag{4C.55b}
$$

Every spinor reduction uses only

$$
\boxed{
\begin{aligned}
\sigma_L^\mu\bar\sigma_L^\nu
&=-\eta^{\mu\nu}\mathbf1_2+2\sigma_L^{\mu\nu},\\
\bar\sigma_L^\mu\sigma_L^\nu
&=-\eta^{\mu\nu}\mathbf1_2+2\bar\sigma_L^{\mu\nu},\\
\sigma_L^{\rho\sigma}\sigma_L^\mu
&=\frac12\left(
\eta^{\rho\mu}\sigma_L^\sigma
-\eta^{\sigma\mu}\sigma_L^\rho
-i\epsilon_L^{\rho\sigma\mu\nu}\sigma_{L,\nu}
\right),\\
\bar\sigma_L^{\rho\sigma}\bar\sigma_L^\mu
&=\frac12\left(
\eta^{\rho\mu}\bar\sigma_L^\sigma
-\eta^{\sigma\mu}\bar\sigma_L^\rho
+i\epsilon_L^{\rho\sigma\mu\nu}\bar\sigma_{L,\nu}
\right),\\
\chi_a(\xi\zeta)+\xi_a(\zeta\chi)+\zeta_a(\chi\xi)&=0.
\end{aligned}}
\tag{4C.55c}
$$

The internal-index reduction uses only

$$
\boxed{
\begin{aligned}
\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\epsilon_{\mathcal K\mathcal L\mathcal M\mathcal N}
&=2\left(
\delta^{\mathcal I}{}_{\mathcal M}
\delta^{\mathcal J}{}_{\mathcal N}
-\delta^{\mathcal I}{}_{\mathcal N}
\delta^{\mathcal J}{}_{\mathcal M}\right),\\
\widetilde\varphi_{\mathcal I\mathcal J}
&=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varphi^{\mathcal K\mathcal L},\\
X\times(Y\times Z)+Y\times(Z\times X)+Z\times(X\times Y)&=0,\\
\mathcal M^{\mathcal I}{}_{\mathcal I}&=0,
\qquad
\widetilde\varphi_{\mathcal I\mathcal K}\times
\varphi^{\mathcal K\mathcal J}
=-\mathcal M^{\mathcal J}{}_{\mathcal I}.
\end{aligned}}
\tag{4C.55d}
$$

Substitution of (4C.55a), followed in the displayed order by
(4C.55c) and (4C.55d), splits the unreduced remainder into its
derivative and algebraic parts:

$$
\boxed{
\begin{aligned}
\mathscr R_a^{\mathcal I}
={}&\mathscr R_{D,a}^{\mathcal I}
+\mathscr R_{{\rm alg},a}^{\mathcal I},\\[1mm]
\mathscr R_{D,a}^{\mathcal I}={}&
+2iA^{\mathcal I\mathcal J}
(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal J}^{\dot b}
+iA_a{}^{\mathcal I\mathcal Jb}
(\sigma_L^\mu)_{b\dot c}
\mathcal D_\mu\bar\Lambda_{\mathcal J}^{\dot c}\\
&+i\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\bar A_{\mathcal K\mathcal L}
(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal J}^{\dot b}\\
&-iX_{a\dot b}{}^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_L^\mu)^{\dot bc}
\mathcal D_\mu\Lambda_c^{\mathcal J}
+2iT_{a\dot b}(\bar\sigma_L^\mu)^{\dot bc}
\mathcal D_\mu\Lambda_c^{\mathcal I},\\[2mm]
\mathscr R_{{\rm alg},a}^{\mathcal I}={}&
-2\sqrt2A^{\mathcal I\mathcal J}
(\widetilde\varphi_{\mathcal J\mathcal K}
\times\Lambda^{\mathcal K})_a
-\sqrt2A_a{}^{\mathcal I\mathcal Jb}
(\widetilde\varphi_{\mathcal J\mathcal K}
\times\Lambda^{\mathcal K})_b\\
&-\sqrt2\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
\bar A_{\mathcal K\mathcal L}
(\widetilde\varphi_{\mathcal J\mathcal M}
\times\Lambda^{\mathcal M})_a\\
&-\sqrt2X_{a\dot b}{}^{\mathcal I}{}_{\mathcal J}
(\varphi^{\mathcal J\mathcal K}
\times\bar\Lambda_{\mathcal K})^{\dot b}
+2\sqrt2T_{a\dot b}
(\varphi^{\mathcal I\mathcal K}
\times\bar\Lambda_{\mathcal K})^{\dot b}.
\end{aligned}}
\tag{4C.55e}
$$

Thus each ordered parameter tensor has the following exact two-term
coefficient pair:

$$
\begin{array}{c|c|c}
\text{parameter tensor}&\text{derivative coefficient}
&\text{scalar--fermion coefficient}\\ \hline
A^{\mathcal I\mathcal J}&+2i\sigma_L^\mu\mathcal D_\mu\bar\Lambda_{\mathcal J}
&-2\sqrt2\widetilde\varphi_{\mathcal J\mathcal K}\times\Lambda^{\mathcal K}\\
A_a{}^{\mathcal I\mathcal Jb}&+i\sigma_L^\mu\mathcal D_\mu\bar\Lambda_{\mathcal J}
&-\sqrt2\widetilde\varphi_{\mathcal J\mathcal K}\times\Lambda^{\mathcal K}\\
\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}\bar A_{\mathcal K\mathcal L}
&+i\sigma_L^\mu\mathcal D_\mu\bar\Lambda_{\mathcal J}
&-\sqrt2\widetilde\varphi_{\mathcal J\mathcal M}\times\Lambda^{\mathcal M}\\
X_{a\dot b}{}^{\mathcal I}{}_{\mathcal J}
&-i\bar\sigma_L^\mu\mathcal D_\mu\Lambda^{\mathcal J}
&-\sqrt2\varphi^{\mathcal J\mathcal K}\times\bar\Lambda_{\mathcal K}\\
T_{a\dot b}&+2i\bar\sigma_L^\mu\mathcal D_\mu\Lambda^{\mathcal I}
&+2\sqrt2\varphi^{\mathcal I\mathcal K}\times\bar\Lambda_{\mathcal K}
\end{array}
\tag{4C.55f}
$$

Equations (4C.39)--(4C.40) now combine each row of (4C.55f),
without an omitted remainder.  Hence the complete reduction of
(4C.41) is

$$
\boxed{
\begin{aligned}
\mathscr R_a^{\mathcal I}={}&
-2(\varepsilon_1^{\mathcal I}\varepsilon_2^{\mathcal J}
-\varepsilon_2^{\mathcal I}\varepsilon_1^{\mathcal J})
\mathcal E_{a\mathcal J}\\
&-(\varepsilon_{1a}^{\mathcal I}\varepsilon_2^{\mathcal Jb}
-\varepsilon_{2a}^{\mathcal I}\varepsilon_1^{\mathcal Jb})
\mathcal E_{b\mathcal J}\\
&-\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
(\bar\varepsilon_{1\mathcal K}\bar\varepsilon_{2\mathcal L}
-\bar\varepsilon_{2\mathcal K}\bar\varepsilon_{1\mathcal L})
\mathcal E_{a\mathcal J}\\
&-(\varepsilon_{1a}^{\mathcal I}\bar\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal I}\bar\varepsilon_{1\mathcal J\dot b})
\widetilde{\mathcal E}^{\mathcal J\dot b}\\
&+2(\varepsilon_{1a}^{\mathcal J}\bar\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal J}\bar\varepsilon_{1\mathcal J\dot b})
\widetilde{\mathcal E}^{\mathcal I\dot b}.
\end{aligned}}
\tag{4C.56}
$$

For the conjugate slot, define

$$
\begin{aligned}
\bar A_{\mathcal I\mathcal J}
&:=\bar\varepsilon_{1\mathcal I}\bar\varepsilon_{2\mathcal J}
-\bar\varepsilon_{2\mathcal I}\bar\varepsilon_{1\mathcal J},\\
\bar A_{\dot a\mathcal I\mathcal J}{}^{\dot b}
&:=\bar\varepsilon_{1\dot a\mathcal I}
\bar\varepsilon_{2\mathcal J}^{\dot b}
-\bar\varepsilon_{2\dot a\mathcal I}
\bar\varepsilon_{1\mathcal J}^{\dot b},\\
\bar X_{\dot a\mathcal I}{}^{\mathcal Jb}
&:=\bar\varepsilon_{1\dot a\mathcal I}
\varepsilon_2^{\mathcal Jb}
-\bar\varepsilon_{2\dot a\mathcal I}
\varepsilon_1^{\mathcal Jb},\\
\bar T_{\dot a}{}^b
&:=\bar\varepsilon_{1\dot a\mathcal J}
\varepsilon_2^{\mathcal Jb}
-\bar\varepsilon_{2\dot a\mathcal J}
\varepsilon_1^{\mathcal Jb}.
\end{aligned}
\tag{4C.56a}
$$

The derivative and algebraic reductions are explicitly

$$
\boxed{
\begin{aligned}
\widetilde{\mathscr R}_{\dot a\mathcal I}
={}&\widetilde{\mathscr R}_{D,\dot a\mathcal I}
+\widetilde{\mathscr R}_{{\rm alg},\dot a\mathcal I},\\[1mm]
\widetilde{\mathscr R}_{D,\dot a\mathcal I}={}&
-2i\bar A_{\mathcal I\mathcal J}
(\bar\sigma_L^\mu)_{\dot ab}\mathcal D_\mu
\Lambda^{\mathcal Jb}
+i\bar A_{\dot a\mathcal I\mathcal J}{}^{\dot b}
(\bar\sigma_L^\mu)_{\dot bc}\mathcal D_\mu
\Lambda^{\mathcal Jc}\\
&-i\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
A^{\mathcal K\mathcal L}
(\bar\sigma_L^\mu)_{\dot ab}\mathcal D_\mu
\Lambda^{\mathcal Jb}\\
&+i\bar X_{\dot a\mathcal I}{}^{\mathcal Jb}
(\sigma_L^\mu)_{b\dot c}\mathcal D_\mu
\bar\Lambda_{\mathcal J}^{\dot c}
-2i\bar T_{\dot a}{}^b
(\sigma_L^\mu)_{b\dot c}\mathcal D_\mu
\bar\Lambda_{\mathcal I}^{\dot c},\\[2mm]
\widetilde{\mathscr R}_{{\rm alg},\dot a\mathcal I}={}&
-2\sqrt2\bar A_{\mathcal I\mathcal J}
(\varphi^{\mathcal J\mathcal K}\times
\bar\Lambda_{\mathcal K})_{\dot a}
+\sqrt2\bar A_{\dot a\mathcal I\mathcal J}{}^{\dot b}
(\varphi^{\mathcal J\mathcal K}\times
\bar\Lambda_{\mathcal K})_{\dot b}\\
&-\sqrt2\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
A^{\mathcal K\mathcal L}
(\varphi^{\mathcal J\mathcal M}\times
\bar\Lambda_{\mathcal M})_{\dot a}\\
&-\sqrt2\bar X_{\dot a\mathcal I}{}^{\mathcal Jb}
(\widetilde\varphi_{\mathcal J\mathcal K}
\times\Lambda^{\mathcal K})_b
+2\sqrt2\bar T_{\dot a}{}^b
(\widetilde\varphi_{\mathcal I\mathcal K}
\times\Lambda^{\mathcal K})_b.
\end{aligned}}
\tag{4C.56a1}
$$

The same substitutions, now starting from (4C.27), give the five
ordered coefficient pairs

$$
\begin{array}{c|c|c}
\text{parameter tensor}&\text{derivative coefficient}
&\text{scalar--fermion coefficient}\\ \hline
\bar A_{\mathcal I\mathcal J}
&-2i\bar\sigma_L^\mu\mathcal D_\mu\Lambda^{\mathcal J}
&-2\sqrt2\varphi^{\mathcal J\mathcal K}\times\bar\Lambda_{\mathcal K}\\
\bar A_{\dot a\mathcal I\mathcal J}{}^{\dot b}
&+i\bar\sigma_L^\mu\mathcal D_\mu\Lambda^{\mathcal J}
&+\sqrt2\varphi^{\mathcal J\mathcal K}\times\bar\Lambda_{\mathcal K}\\
\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}A^{\mathcal K\mathcal L}
&-i\bar\sigma_L^\mu\mathcal D_\mu\Lambda^{\mathcal J}
&-\sqrt2\varphi^{\mathcal J\mathcal K}\times\bar\Lambda_{\mathcal K}\\
\bar X_{\dot a\mathcal I}{}^{\mathcal Jb}
&+i\sigma_L^\mu\mathcal D_\mu\bar\Lambda_{\mathcal J}
&-\sqrt2\widetilde\varphi_{\mathcal J\mathcal K}\times\Lambda^{\mathcal K}\\
\bar T_{\dot a}{}^b
&-2i\sigma_L^\mu\mathcal D_\mu\bar\Lambda_{\mathcal I}
&+2\sqrt2\widetilde\varphi_{\mathcal I\mathcal K}\times\Lambda^{\mathcal K}
\end{array}
\tag{4C.56b}
$$

The first three rows are respectively
(-2\bar A_{\mathcal I\mathcal J}
\widetilde{\mathcal E}^{\mathcal J}),
(+\bar A_{\dot a\mathcal I\mathcal J}{}^{\dot b}
\widetilde{\mathcal E}_{\dot b}^{\mathcal J}), and
(-\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
A^{\mathcal K\mathcal L}\widetilde{\mathcal E}^{\mathcal J}).
The last two are
(-\bar X_{\dot a\mathcal I}{}^{\mathcal Jb}
\mathcal E_{b\mathcal J}) and
(+2\bar T_{\dot a}{}^b\mathcal E_{b\mathcal I}).
Therefore

$$
\boxed{
\begin{aligned}
\widetilde{\mathscr R}_{\dot a\mathcal I}={}&
-2(\bar\varepsilon_{1\mathcal I}\bar\varepsilon_{2\mathcal J}
-\bar\varepsilon_{2\mathcal I}\bar\varepsilon_{1\mathcal J})
\widetilde{\mathcal E}_{\dot a}^{\mathcal J}\\
&+(\bar\varepsilon_{1\dot a\mathcal I}
\bar\varepsilon_{2\mathcal J}^{\dot b}
-\bar\varepsilon_{2\dot a\mathcal I}
\bar\varepsilon_{1\mathcal J}^{\dot b})
\widetilde{\mathcal E}_{\dot b}^{\mathcal J}\\
&-\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
(\varepsilon_1^{\mathcal K}\varepsilon_2^{\mathcal L}
-\varepsilon_2^{\mathcal K}\varepsilon_1^{\mathcal L})
\widetilde{\mathcal E}_{\dot a}^{\mathcal J}\\
&-(\bar\varepsilon_{1\dot a\mathcal I}\varepsilon_2^{\mathcal Jb}
-\bar\varepsilon_{2\dot a\mathcal I}\varepsilon_1^{\mathcal Jb})
\mathcal E_{b\mathcal J}\\
&+2(\bar\varepsilon_{1\dot a\mathcal J}\varepsilon_2^{\mathcal Jb}
-\bar\varepsilon_{2\dot a\mathcal J}\varepsilon_1^{\mathcal Jb})
\mathcal E_{b\mathcal I}.
\end{aligned}}
\tag{4C.57}
$$

Therefore

$$
\boxed{
\begin{aligned}
[\delta_1,\delta_2]\Lambda_a^{\mathcal I}
&=v_L^\mu\mathcal D_\mu\Lambda_a^{\mathcal I}
+(\Omega\times\Lambda^{\mathcal I})_a
+\mathscr R_a^{\mathcal I},\\
[\delta_1,\delta_2]\bar\Lambda_{\dot a\mathcal I}
&=v_L^\mu\mathcal D_\mu\bar\Lambda_{\dot a\mathcal I}
+(\Omega\times\bar\Lambda_{\mathcal I})_{\dot a}
+\widetilde{\mathscr R}_{\dot a\mathcal I}.
\end{aligned}}
\tag{4C.58}
$$

For

$$
\mathscr C_{L,a\mathcal I}^{\mu}
:=-\epsilon_{ab}C_{L,\mathcal I}^{\mu b},
\tag{4C.58a}
$$

split the non-topological density into

$$
\begin{aligned}
\mathcal L_{L,g}&=-\frac h4\operatorname{tr}_\kappa(F_{\mu\nu}F^{\mu\nu}),\\
\mathcal L_{L,s}&=-\frac h4\operatorname{tr}_\kappa(
\mathcal D_\mu\varphi^{\mathcal I\mathcal J}
\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J}),\\
\mathcal L_{L,f}&=ih\operatorname{tr}_\kappa(
\bar\Lambda_{\mathcal I}\bar\sigma_L^\mu
\mathcal D_\mu\Lambda^{\mathcal I}),\\
\mathcal L_{L,Y}&=\frac h{\sqrt2}\operatorname{tr}_\kappa\left[
\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\bar\Lambda_{\mathcal I}\times\bar\Lambda_{\mathcal J})\right],\\
\mathcal L_{L,V}&=-\frac h{16}\operatorname{tr}_\kappa\left[
(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})\right].
\end{aligned}
\tag{4C.58b}
$$

One product rule and one covariant integration by parts in each
kinetic sector give the following five independent identities:

$$
\boxed{
\begin{aligned}
\delta\mathcal L_{L,g}
={}&\partial_\mu\Theta_{L,g}^\mu+\mathscr B_{L,g},\\
\Theta_{L,g}^\mu
={}&-h\operatorname{tr}_\kappa(F^{\mu\nu}\delta A_\nu),\\
\mathscr B_{L,g}
={}&h\operatorname{tr}_\kappa[(\mathcal D_\mu F^{\mu\nu})\delta A_\nu],\\[1mm]
\delta\mathcal L_{L,s}
={}&\partial_\mu\Theta_{L,s}^\mu+\mathscr B_{L,s},\\
\Theta_{L,s}^\mu
={}&-\frac h4\operatorname{tr}_\kappa\left[
\delta\varphi^{\mathcal I\mathcal J}
\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J}
+\mathcal D^\mu\varphi^{\mathcal I\mathcal J}
\delta\widetilde\varphi_{\mathcal I\mathcal J}\right],\\
\mathscr B_{L,s}
={}&\frac h4\operatorname{tr}_\kappa\left[
\delta\varphi^{\mathcal I\mathcal J}
\mathcal D^2\widetilde\varphi_{\mathcal I\mathcal J}
+\mathcal D^2\varphi^{\mathcal I\mathcal J}
\delta\widetilde\varphi_{\mathcal I\mathcal J}\right]\\
&-\frac h4\operatorname{tr}_\kappa\left[
(\delta A_\mu\times\varphi^{\mathcal I\mathcal J})
\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J}
+\mathcal D^\mu\varphi^{\mathcal I\mathcal J}
(\delta A_\mu\times\widetilde\varphi_{\mathcal I\mathcal J})
\right],\\[1mm]
\delta\mathcal L_{L,f}
={}&\partial_\mu\Theta_{L,f}^\mu+\mathscr B_{L,f},\\
\Theta_{L,f}^\mu
={}&ih\operatorname{tr}_\kappa(
\bar\Lambda_{\mathcal I}\bar\sigma_L^\mu
\delta\Lambda^{\mathcal I}),\\
\mathscr B_{L,f}
={}&ih\operatorname{tr}_\kappa\left[
\delta\bar\Lambda_{\mathcal I}\bar\sigma_L^\mu
\mathcal D_\mu\Lambda^{\mathcal I}
-(\mathcal D_\mu\bar\Lambda_{\mathcal I})
\bar\sigma_L^\mu\delta\Lambda^{\mathcal I}
+\bar\Lambda_{\mathcal I}\bar\sigma_L^\mu
(\delta A_\mu\times\Lambda^{\mathcal I})
\right],\\[1mm]
\delta\mathcal L_{L,Y}
={}&\mathscr B_{L,Y},
\qquad
\delta\mathcal L_{L,V}=\mathscr B_{L,V},
\end{aligned}}
\tag{4C.58c}
$$

with no hidden boundary term in the last two sectors and

$$
\begin{aligned}
\mathscr B_{L,Y}={}&\frac h{\sqrt2}\operatorname{tr}_\kappa\Big[
\delta\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\widetilde\varphi_{\mathcal I\mathcal J}
(\delta\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\delta\Lambda^{\mathcal J})\\
&+\delta\varphi^{\mathcal I\mathcal J}
(\bar\Lambda_{\mathcal I}\times\bar\Lambda_{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\delta\bar\Lambda_{\mathcal I}\times\bar\Lambda_{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\bar\Lambda_{\mathcal I}\times\delta\bar\Lambda_{\mathcal J})
\Big],\\
\mathscr B_{L,V}={}&-\frac h{16}\operatorname{tr}_\kappa\Big[
(\delta\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L}
+\varphi^{\mathcal I\mathcal J}\times
\delta\varphi^{\mathcal K\mathcal L})
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})\\
&+(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})
(\delta\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L}
+\widetilde\varphi_{\mathcal I\mathcal J}\times
\delta\widetilde\varphi_{\mathcal K\mathcal L})
\Big].
\end{aligned}
\tag{4C.58d}
$$

Insert the left-parameter parts of (4C.24)--(4C.27) into
(4C.58c)--(4C.58d), move \(\varepsilon^{\mathcal Ia}\) to the
right, and use (4C.55c)--(4C.55d).  Here
\(\mathscr B|_\varepsilon\) denotes the term containing
\(\varepsilon\) and no \(\bar\varepsilon\).  The complete bulk
coefficient is

$$
\sum_{q=g,s,f,Y,V}\mathscr B_{L,q}
\big|_{\varepsilon}
=-\partial_\mu
\left(\mathcal S_{L,a\mathcal I}^{\mu}
\varepsilon^{\mathcal Ia}\right),
\tag{4C.58e}
$$

where the product rule on the right-hand side is, term by term,

$$
\boxed{
\begin{aligned}
-\partial_\mu\mathcal S_{L,a\mathcal I}^{\mu}
=h\operatorname{tr}_\kappa\Big[&
+i(\mathcal D_\mu F_{\rho\sigma})
(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}\bar\Lambda_{\mathcal I}^{\dot b}
+iF_{\rho\sigma}(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal I}^{\dot b}\\
&-\sqrt2(\mathcal D_\mu\mathcal D_\nu
\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_L^\nu)_{a\dot b}(\bar\sigma_L^\mu)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&-\sqrt2(\mathcal D_\nu
\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_L^\nu)_{a\dot b}(\bar\sigma_L^\mu)^{\dot bb}
\mathcal D_\mu\Lambda_b^{\mathcal J}\\
&-i(\mathcal D_\mu\mathcal M^{\mathcal J}{}_{\mathcal I})
(\sigma_L^\mu)_{a\dot b}\bar\Lambda_{\mathcal J}^{\dot b}
-i\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal J}^{\dot b}
\Big].
\end{aligned}}
\tag{4C.58f}
$$

The sectorwise reduction has no further tensor family:

$$
\begin{array}{c|c}
\text{ordered tensor family}&
\sum_{q=g,s,f,Y,V}\mathscr B_{L,q}\big|_\varepsilon\\ \hline
(\mathcal D F)\bar\Lambda, F\mathcal D\bar\Lambda
&+ih\operatorname{tr}_\kappa\!\left[
\mathcal D_\mu(F_{\rho\sigma}
\sigma_L^{\rho\sigma}\sigma_L^\mu\bar\Lambda_{\mathcal I})\right]\\
(\mathcal D\mathcal D\widetilde\varphi)\Lambda,
\ (\mathcal D\widetilde\varphi)\mathcal D\Lambda
&-\sqrt2h\operatorname{tr}_\kappa\!\left[
\mathcal D_\mu((\mathcal D_\nu
\widetilde\varphi_{\mathcal I\mathcal J})
\sigma_L^\nu\bar\sigma_L^\mu\Lambda^{\mathcal J})\right]\\
(\mathcal D\mathcal M)\bar\Lambda,
\ \mathcal M\mathcal D\bar\Lambda
&-ih\operatorname{tr}_\kappa\!\left[
\mathcal D_\mu(\mathcal M^{\mathcal J}{}_{\mathcal I}
\sigma_L^\mu\bar\Lambda_{\mathcal J})\right]\\
F\widetilde\varphi\Lambda,
\ (\mathcal D\varphi)\Lambda\bar\Lambda,
\ \varphi^3\Lambda,
\ \Lambda^3&0
\end{array}
\tag{4C.58g}
$$

Here the final zero is obtained respectively from the two Yukawa
orders, trace invariance, the Jacobi identity, and the two-spinor
Schouten identity in (4C.55c); the quartic variation is required in
the \(\varphi^3\Lambda\) row.

Equation (4C.58f) fixes, before the word ``current'' is used,

$$
\boxed{
\begin{aligned}
\mathcal S_{L,a\mathcal I}^{\mu}
=h\operatorname{tr}_{\kappa}\Big[&
-iF_{\rho\sigma}(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}\bar\Lambda_{\mathcal I}^{\dot b}\\
&+\sqrt2(\mathcal D_\nu\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_L^\nu)_{a\dot b}(\bar\sigma_L^\mu)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&+i\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_L^\mu)_{a\dot b}\bar\Lambda_{\mathcal J}^{\dot b}
\Big].
\end{aligned}}
\tag{4C.58h}
$$

Since
\(\Theta_L^\mu|_\varepsilon
=\mathscr C_{L,a\mathcal I}^{\mu}\varepsilon^{\mathcal Ia}\),
equations (4C.58c) and (4C.58e) give the constant-parameter boundary
coefficient

$$
\boxed{
K_{L,a\mathcal I}^{\mu}
=\mathscr C_{L,a\mathcal I}^{\mu}
-\mathcal S_{L,a\mathcal I}^{\mu},
\qquad
\delta_\varepsilon\mathcal L_L^{(4)}\big|_\varepsilon
=\partial_\mu(K_{L,a\mathcal I}^{\mu}
\varepsilon^{\mathcal Ia}).}
\tag{4C.58i}
$$

Only now the ordered Noether definition gives

$$
j_{L,a\mathcal I}^{\mu}
:=\mathscr C_{L,a\mathcal I}^{\mu}
-K_{L,a\mathcal I}^{\mu}
=\mathcal S_{L,a\mathcal I}^{\mu}.
\tag{4C.58j}
$$

Thus the unimproved Lorentzian \(SU(4)_R\)-fundamental current is

$$
\boxed{
\begin{aligned}
j_{L,a\mathcal I}^{\mu}
=h\operatorname{tr}_{\kappa}\Big[&
-iF_{\rho\sigma}(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}\bar\Lambda_{\mathcal I}^{\dot b}\\
&+\sqrt2(\mathcal D_\nu\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_L^\nu)_{a\dot b}(\bar\sigma_L^\mu)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&+i\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_L^\mu)_{a\dot b}\bar\Lambda_{\mathcal J}^{\dot b}
\Big].
\end{aligned}}
\tag{4C.59}
$$

Its manifest slot expands to

$$
\boxed{
\begin{aligned}
j_{L,a4}^{\mu}=h\operatorname{tr}_{\kappa}\Big[&
-iF_{\rho\sigma}\sigma_L^{\rho\sigma}\sigma_L^\mu
\bar\lambda
-\sqrt2\mathcal D_\nu\bar\phi_r
\sigma_L^\nu\bar\sigma_L^\mu\psi_r\\
&+\mathscr D\sigma_L^\mu\bar\lambda
-i\sqrt2F_r\sigma_L^\mu\bar\psi_r\Big]_a,
\end{aligned}}
\tag{4C.60}
$$

because

$$
\mathcal M^4{}_4=-C_0,
\qquad
\mathcal M^r{}_4=-\sqrt2F_r,
\qquad
\mathcal M^4{}_r=+\sqrt2\widetilde F_r,
\qquad
\mathscr D=-iC_0.
\tag{4C.61}
$$

The topological contribution is

$$
\boxed{
\mathscr C_{\vartheta,L,a\mathcal I}^{\mu}
=K_{\vartheta,L,a\mathcal I}^{\mu}
=-i\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}
(\sigma_{L,\nu})_{a\dot b}
\bar\Lambda_{\mathcal I}^{B\dot b}.}
\tag{4C.64}
$$

Thus the theta density cancels from (4C.59).

For the conjugate parameter, define

$$
\bar{\mathscr C}_L^{\mu\dot a\mathcal I}
:=-\epsilon^{\dot a\dot b}
\widetilde C_L^{\mu\mathcal I}{}_{\dot b}.
\tag{4C.64a}
$$

Insert the \(\bar\varepsilon_{\mathcal I}\) parts of
(4C.24)--(4C.27) into the same five sector identities.  Their bulk
sum is

$$
\sum_{q=g,s,f,Y,V}\mathscr B_{L,q}
\big|_{\bar\varepsilon}
=-\partial_\mu\left(
\bar{\mathcal S}_L^{\mu\dot a\mathcal I}
\bar\varepsilon_{\dot a\mathcal I}\right),
\tag{4C.64b0}
$$

with the full product-rule coefficient

$$
\boxed{
\begin{aligned}
-\partial_\mu\bar{\mathcal S}_L^{\mu\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
-i(\mathcal D_\mu F_{\rho\sigma})
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\Lambda_b^{\mathcal I}
-iF_{\rho\sigma}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
(\bar\sigma_L^\mu)^{\dot bb}
\mathcal D_\mu\Lambda_b^{\mathcal I}\\
&-\sqrt2(\mathcal D_\mu\mathcal D_\nu
\varphi^{\mathcal I\mathcal J})
(\bar\sigma_L^\nu)^{\dot ab}(\sigma_L^\mu)_{b\dot b}
\bar\Lambda_{\mathcal J}^{\dot b}\\
&-\sqrt2(\mathcal D_\nu\varphi^{\mathcal I\mathcal J})
(\bar\sigma_L^\nu)^{\dot ab}(\sigma_L^\mu)_{b\dot b}
\mathcal D_\mu\bar\Lambda_{\mathcal J}^{\dot b}\\
&-i(\mathcal D_\mu\mathcal M^{\mathcal I}{}_{\mathcal J})
(\bar\sigma_L^\mu)^{\dot ab}\Lambda_b^{\mathcal J}
-i\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_L^\mu)^{\dot ab}
\mathcal D_\mu\Lambda_b^{\mathcal J}
\Big].
\end{aligned}}
\tag{4C.64b1}
$$

The remaining ordered families satisfy

$$
\left.
\sum_{q=g,s,f,Y,V}\mathscr B_{L,q}
\big|_{\bar\varepsilon}
\right|_{
F\varphi\bar\Lambda,
(\mathcal D\varphi)\Lambda\bar\Lambda,
\varphi^3\bar\Lambda,
\bar\Lambda^3}=0.
\tag{4C.64b1b}
$$

The primitive fixed by (4C.64b1) is

$$
\boxed{
\begin{aligned}
\bar{\mathcal S}_L^{\mu\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
+iF_{\rho\sigma}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\Lambda_b^{\mathcal I}\\
&+\sqrt2(\mathcal D_\nu\varphi^{\mathcal I\mathcal J})
(\bar\sigma_L^\nu)^{\dot ab}(\sigma_L^\mu)_{b\dot b}
\bar\Lambda_{\mathcal J}^{\dot b}\\
&+i\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_L^\mu)^{\dot ab}\Lambda_b^{\mathcal J}
\Big].
\end{aligned}}
\tag{4C.64b1a}
$$

Therefore the independently fixed boundary coefficient is

$$
\boxed{
\bar K_L^{\mu\dot a\mathcal I}
=\bar{\mathscr C}_L^{\mu\dot a\mathcal I}
-\bar{\mathcal S}_L^{\mu\dot a\mathcal I},
\qquad
\delta_{\bar\varepsilon}\mathcal L_L^{(4)}
=\partial_\mu(\bar K_L^{\mu\dot a\mathcal I}
\bar\varepsilon_{\dot a\mathcal I}).}
\tag{4C.64b2}
$$

The Noether difference
\(\bar j_L=\bar{\mathscr C}_L-\bar K_L\)
is consequently

$$
\boxed{
\begin{aligned}
\bar j_L^{\mu\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
+iF_{\rho\sigma}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\Lambda_b^{\mathcal I}\\
&+\sqrt2(\mathcal D_\nu\varphi^{\mathcal I\mathcal J})
(\bar\sigma_L^\nu)^{\dot ab}(\sigma_L^\mu)_{b\dot b}
\bar\Lambda_{\mathcal J}^{\dot b}\\
&+i\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_L^\mu)^{\dot ab}\Lambda_b^{\mathcal J}
\Big].
\end{aligned}}
\tag{4C.64b}
$$

Its manifest slot is

$$
\boxed{
\begin{aligned}
\bar j_L^{\mu\dot a4}
=h\operatorname{tr}_\kappa\Big[&
+iF_{\rho\sigma}\bar\sigma_L^{\rho\sigma}
\bar\sigma_L^\mu\lambda
-\sqrt2\mathcal D_\nu\phi_r
\bar\sigma_L^\nu\sigma_L^\mu\bar\psi_r\\
&+\mathscr D\bar\sigma_L^\mu\lambda
+i\sqrt2\widetilde F_r\bar\sigma_L^\mu\psi_r
\Big]^{\dot a}.
\end{aligned}}
\tag{4C.64c}
$$

The conjugate topological coefficient is

$$
\boxed{
\bar{\mathscr C}_{\vartheta,L}^{\mu\dot a\mathcal I}
=\bar K_{\vartheta,L}^{\mu\dot a\mathcal I}
=-i\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}
(\bar\sigma_{L,\nu})^{\dot ab}\Lambda_b^{B\mathcal I}.}
\tag{4C.64d}
$$

Define the normalized bosonic Euler operators

$$
\boxed{
\begin{aligned}
\mathscr A^\nu={}&
\mathcal D_\mu F^{\mu\nu}
-\frac14\left(
\varphi^{\mathcal I\mathcal J}
\times\mathcal D^\nu\widetilde\varphi_{\mathcal I\mathcal J}
+\widetilde\varphi_{\mathcal I\mathcal J}
\times\mathcal D^\nu\varphi^{\mathcal I\mathcal J}
\right)\\
&-i\left[
(\bar\Lambda_{\dot a\mathcal I}
\bar\sigma_L^{\nu\dot aa})\times\Lambda_a^{\mathcal I}
\right],\\
\mathscr P_{\mathcal I\mathcal J}={}&
\frac12\mathcal D^2\widetilde\varphi_{\mathcal I\mathcal J}
-\frac14\varphi^{\mathcal K\mathcal L}\times
(\widetilde\varphi_{\mathcal I\mathcal J}
\times\widetilde\varphi_{\mathcal K\mathcal L})
+\sqrt2(\bar\Lambda_{\mathcal I}
\times\bar\Lambda_{\mathcal J}),\\
\widetilde{\mathscr P}^{\mathcal I\mathcal J}={}&
\frac12\mathcal D^2\varphi^{\mathcal I\mathcal J}
-\frac14\widetilde\varphi_{\mathcal K\mathcal L}\times
(\varphi^{\mathcal I\mathcal J}
\times\varphi^{\mathcal K\mathcal L})
+\sqrt2(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J}).
\end{aligned}}
\tag{4C.65}
$$

Direct differentiation of (4C.59) gives

$$
\boxed{
\begin{aligned}
\partial_\mu j_{L,a\mathcal I}^{\mu}
=h\operatorname{tr}_{\kappa}\Big\{&
-i\mathscr A^\nu(\sigma_{L,\nu})_{a\dot b}
\bar\Lambda_{\mathcal I}^{\dot b}
+\sqrt2\mathscr P_{\mathcal I\mathcal J}
\Lambda_a^{\mathcal J}\\
&+\frac1{\sqrt2}
\epsilon_{\mathcal J\mathcal K\mathcal I\mathcal M}
\widetilde{\mathscr P}^{\mathcal J\mathcal K}
\Lambda_a^{\mathcal M}\\
&+\left[
\delta_{\mathcal I}^{\mathcal J}
(\sigma_L^{\rho\sigma})_b{}^c\epsilon_{ca}F_{\rho\sigma}
+\mathcal M^{\mathcal J}{}_{\mathcal I}\epsilon_{ba}
\right]\mathcal E^b{}_{\mathcal J}\\
&-i\sqrt2(\sigma_L^\rho)_{a\dot b}
(\mathcal D_\rho\widetilde\varphi_{\mathcal J\mathcal I})
\widetilde{\mathcal E}^{\dot b\mathcal J}
\Big\}.
\end{aligned}}
\tag{4C.66}
$$

The conjugate current obeys

$$
\boxed{
\begin{aligned}
\partial_\mu\bar j_L^{\mu\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big\{&
-i\mathscr A^\nu(\bar\sigma_{L,\nu})^{\dot ab}
\Lambda_b^{\mathcal I}
+\sqrt2\widetilde{\mathscr P}^{\mathcal I\mathcal J}
\bar\Lambda_{\mathcal J}^{\dot a}\\
&+\frac1{\sqrt2}
\epsilon^{\mathcal J\mathcal K\mathcal I\mathcal M}
\mathscr P_{\mathcal J\mathcal K}
\bar\Lambda_{\mathcal M}^{\dot a}\\
&+\left[
-\delta_{\mathcal J}^{\mathcal I}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}F_{\rho\sigma}
-\mathcal M^{\mathcal I}{}_{\mathcal J}
\delta^{\dot a}{}_{\dot b}
\right]\widetilde{\mathcal E}^{\dot b\mathcal J}\\
&-i\sqrt2(\bar\sigma_L^\rho)^{\dot ab}
(\mathcal D_\rho\varphi^{\mathcal J\mathcal I})
\mathcal E_{b\mathcal J}
\Big\}.
\end{aligned}}
\tag{4C.66e}
$$

Define

$$
\mathscr C_{E,a\mathcal I}^{m}
:=-\epsilon_{ab}C_{E,\mathcal I}^{mb}.
\tag{4C.66a}
$$

The direct Euclidean product rules, without Wick transport, are

$$
\boxed{
\begin{aligned}
\delta\mathcal L_{E,g}
&=\partial_m\Theta_{E,g}^m+\mathscr B_{E,g},
&\Theta_{E,g}^m
&=h\operatorname{tr}_\kappa(F^{mn}\delta A_n),
&\mathscr B_{E,g}
&=-h\operatorname{tr}_\kappa[(\mathcal D_mF^{mn})\delta A_n],\\
\delta\mathcal L_{E,s}
&=\partial_m\Theta_{E,s}^m+\mathscr B_{E,s},
&\Theta_{E,s}^m
&=\frac h4\operatorname{tr}_\kappa\left[
\delta\varphi^{\mathcal I\mathcal J}
\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J}
+\mathcal D_m\varphi^{\mathcal I\mathcal J}
\delta\widetilde\varphi_{\mathcal I\mathcal J}\right],\\
\delta\mathcal L_{E,f}
&=\partial_m\Theta_{E,f}^m+\mathscr B_{E,f},
&\Theta_{E,f}^m
&=h\operatorname{tr}_\kappa(
\widetilde\Lambda_{\mathcal I}\bar\sigma_E^m
\delta\Lambda^{\mathcal I}),\\
\delta\mathcal L_{E,Y}&=\mathscr B_{E,Y},
&\delta\mathcal L_{E,V}&=\mathscr B_{E,V}.
\end{aligned}}
\tag{4C.66b}
$$

The three bulk kinetic coefficients are

$$
\boxed{
\begin{aligned}
\mathscr B_{E,s}={}&-\frac h4\operatorname{tr}_\kappa\left[
\delta\varphi^{\mathcal I\mathcal J}
\mathcal D_m\mathcal D_m
\widetilde\varphi_{\mathcal I\mathcal J}
+(\mathcal D_m\mathcal D_m\varphi^{\mathcal I\mathcal J})
\delta\widetilde\varphi_{\mathcal I\mathcal J}\right]\\
&+\frac h4\operatorname{tr}_\kappa\left[
(\delta A_m\times\varphi^{\mathcal I\mathcal J})
\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J}
+\mathcal D_m\varphi^{\mathcal I\mathcal J}
(\delta A_m\times\widetilde\varphi_{\mathcal I\mathcal J})
\right],\\
\mathscr B_{E,f}={}&h\operatorname{tr}_\kappa\left[
\delta\widetilde\Lambda_{\mathcal I}\bar\sigma_E^m
\mathcal D_m\Lambda^{\mathcal I}
-(\mathcal D_m\widetilde\Lambda_{\mathcal I})
\bar\sigma_E^m\delta\Lambda^{\mathcal I}
+\widetilde\Lambda_{\mathcal I}\bar\sigma_E^m
(\delta A_m\times\Lambda^{\mathcal I})\right],\\
\mathscr B_{E,g}={}&-h\operatorname{tr}_\kappa[
(\mathcal D_mF^{mn})\delta A_n].
\end{aligned}}
\tag{4C.66c}
$$

The algebraic sectors are varied directly from

$$
\begin{aligned}
\mathcal L_{E,Y}&=-\frac h{\sqrt2}\operatorname{tr}_\kappa\left[
\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\widetilde\Lambda_{\mathcal I}\times
\widetilde\Lambda_{\mathcal J})\right],\\
\mathcal L_{E,V}&=+\frac h{16}\operatorname{tr}_\kappa\left[
(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})\right],\\
\mathscr B_{E,Y}&:=\delta\mathcal L_{E,Y},
\qquad
\mathscr B_{E,V}:=\delta\mathcal L_{E,V},
\end{aligned}
\tag{4C.66c1}
$$

Explicitly,

$$
\begin{aligned}
\mathscr B_{E,Y}={}&-\frac h{\sqrt2}\operatorname{tr}_\kappa\Big[
\delta\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\widetilde\varphi_{\mathcal I\mathcal J}
(\delta\Lambda^{\mathcal I}\times\Lambda^{\mathcal J})
+\widetilde\varphi_{\mathcal I\mathcal J}
(\Lambda^{\mathcal I}\times\delta\Lambda^{\mathcal J})\\
&+\delta\varphi^{\mathcal I\mathcal J}
(\widetilde\Lambda_{\mathcal I}\times
\widetilde\Lambda_{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\delta\widetilde\Lambda_{\mathcal I}\times
\widetilde\Lambda_{\mathcal J})
+\varphi^{\mathcal I\mathcal J}
(\widetilde\Lambda_{\mathcal I}\times
\delta\widetilde\Lambda_{\mathcal J})\Big],\\
\mathscr B_{E,V}={}&+\frac h{16}\operatorname{tr}_\kappa\Big[
(\delta\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L}
+\varphi^{\mathcal I\mathcal J}\times
\delta\varphi^{\mathcal K\mathcal L})
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})\\
&+(\varphi^{\mathcal I\mathcal J}\times
\varphi^{\mathcal K\mathcal L})
(\delta\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L}
+\widetilde\varphi_{\mathcal I\mathcal J}\times
\delta\widetilde\varphi_{\mathcal K\mathcal L})\Big].
\end{aligned}
\tag{4C.66c1a}
$$

Inserting (4C.44)--(4C.47) gives

$$
\sum_{q=g,s,f,Y,V}\mathscr B_{E,q}\big|_\varepsilon
=-\partial_m(\mathcal S_{E,a\mathcal I}^{m}
\varepsilon^{\mathcal Ia}),
\tag{4C.66c2}
$$

The direct Euclidean residual ledger is

$$
\left.
\sum_{q=g,s,f,Y,V}\mathscr B_{E,q}\big|_\varepsilon
\right|_{
F\widetilde\varphi\Lambda,
(\mathcal D\varphi)\Lambda\widetilde\Lambda,
\varphi^3\Lambda,
\Lambda^3}=0;
\tag{4C.66c2a}
$$

the four zero coefficients use the same ordered trace, Jacobi, and
Schouten identities as (4C.58g), with no Lorentzian conjugation.

$$
\boxed{
\begin{aligned}
-\partial_m\mathcal S_{E,a\mathcal I}^{m}
=h\operatorname{tr}_\kappa\Big[&
-(\mathcal D_mF_{rs})(\sigma_E^{rs})_a{}^b
(\sigma_E^m)_{b\dot b}\widetilde\Lambda_{\mathcal I}^{\dot b}
-F_{rs}(\sigma_E^{rs})_a{}^b
(\sigma_E^m)_{b\dot b}\mathcal D_m
\widetilde\Lambda_{\mathcal I}^{\dot b}\\
&-\sqrt2(\mathcal D_m\mathcal D_n
\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&-\sqrt2(\mathcal D_n
\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\mathcal D_m\Lambda_b^{\mathcal J}\\
&-(\mathcal D_m\mathcal M^{\mathcal J}{}_{\mathcal I})
(\sigma_E^m)_{a\dot b}\widetilde\Lambda_{\mathcal J}^{\dot b}
-\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_E^m)_{a\dot b}\mathcal D_m
\widetilde\Lambda_{\mathcal J}^{\dot b}\Big].
\end{aligned}}
\tag{4C.66c3}
$$

Thus

$$
\boxed{
\begin{aligned}
\mathcal S_{E,a\mathcal I}^{m}
=h\operatorname{tr}_\kappa\Big[&
F_{rs}(\sigma_E^{rs})_a{}^b
(\sigma_E^m)_{b\dot b}\widetilde\Lambda_{\mathcal I}^{\dot b}\\
&+\sqrt2(\mathcal D_n\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&+\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_E^m)_{a\dot b}\widetilde\Lambda_{\mathcal J}^{\dot b}
\Big],\\
K_{E,a\mathcal I}^{m}
&=\mathscr C_{E,a\mathcal I}^{m}-\mathcal S_{E,a\mathcal I}^{m},\\
\delta_\varepsilon\mathcal L_E^{(4)}
&=\partial_m(K_{E,a\mathcal I}^{m}\varepsilon^{\mathcal Ia}).
\end{aligned}}
\tag{4C.66c4}
$$

The topological term satisfies

$$
\mathscr C_{\vartheta,E,a\mathcal I}^{m}
=K_{\vartheta,E,a\mathcal I}^{m}
=+i\mathfrak k_{AB}({}^{\star}F_E^A)^{mn}
(\sigma_{E,n})_{a\dot b}
\widetilde\Lambda_{\mathcal I}^{B\dot b}.
\tag{4C.66d}
$$

The Noether difference is now taken only after (4C.66c2):

$$
j_{E,a\mathcal I}^{m}
:=\mathscr C_{E,a\mathcal I}^{m}-K_{E,a\mathcal I}^{m}
=\mathcal S_{E,a\mathcal I}^{m}.
\tag{4C.66c5}
$$

Therefore

$$
\boxed{
\begin{aligned}
j_{E,a\mathcal I}^{m}
=h\operatorname{tr}_{\kappa}\Big[&
F_{rs}(\sigma_E^{rs})_a{}^b
(\sigma_E^m)_{b\dot b}\widetilde\Lambda_{\mathcal I}^{\dot b}\\
&+\sqrt2(\mathcal D_n\widetilde\varphi_{\mathcal I\mathcal J})
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\Lambda_b^{\mathcal J}\\
&+\mathcal M^{\mathcal J}{}_{\mathcal I}
(\sigma_E^m)_{a\dot b}\widetilde\Lambda_{\mathcal J}^{\dot b}
\Big].
\end{aligned}}
\tag{4C.67}
$$

For the independent Euclidean
\(\widetilde\varepsilon_{\mathcal I}\) slot, direct localization gives

$$
\boxed{
\begin{aligned}
\widetilde C_E^{m\mathcal I}{}_{\dot a}
=h\kappa_{AB}\Big[&
-F^{Amn}(\Lambda^{\mathcal IB}\sigma_{E,n})_{\dot a}
+\sqrt2(\mathcal D^m\varphi^{\mathcal I\mathcal J})^A
\widetilde\Lambda_{\dot a\mathcal J}^B\\
&-\sqrt2\widetilde\Lambda_{\dot b\mathcal J}^A
(\bar\sigma_E^m)^{\dot bc}(\sigma_E^n)_{c\dot a}
(\mathcal D_n\varphi^{\mathcal J\mathcal I})^B
\Big].
\end{aligned}}
\tag{4C.67a}
$$

Define

$$
\widetilde{\mathscr C}_E^{m\dot a\mathcal I}
:=-\epsilon^{\dot a\dot b}
\widetilde C_E^{m\mathcal I}{}_{\dot b}.
\tag{4C.67b}
$$

The independent \(\widetilde\varepsilon_{\mathcal I}\) substitution
in (4C.66b)--(4C.66c1) gives

$$
\sum_{q=g,s,f,Y,V}\mathscr B_{E,q}
\big|_{\widetilde\varepsilon}
=-\partial_m\left(
\widetilde{\mathcal S}_E^{m\dot a\mathcal I}
\widetilde\varepsilon_{\dot a\mathcal I}\right),
\tag{4C.67b1}
$$

$$
\left.
\sum_{q=g,s,f,Y,V}\mathscr B_{E,q}
\big|_{\widetilde\varepsilon}
\right|_{
F\varphi\widetilde\Lambda,
(\mathcal D\varphi)\Lambda\widetilde\Lambda,
\varphi^3\widetilde\Lambda,
\widetilde\Lambda^3}=0.
\tag{4C.67b1a}
$$

$$
\boxed{
\begin{aligned}
-\partial_m\widetilde{\mathcal S}_E^{m\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
+(\mathcal D_mF_{rs})
(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
(\bar\sigma_E^m)^{\dot bb}\Lambda_b^{\mathcal I}
+F_{rs}(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
(\bar\sigma_E^m)^{\dot bb}\mathcal D_m\Lambda_b^{\mathcal I}\\
&-\sqrt2(\mathcal D_m\mathcal D_n
\varphi^{\mathcal I\mathcal J})
(\bar\sigma_E^n)^{\dot ab}(\sigma_E^m)_{b\dot b}
\widetilde\Lambda_{\mathcal J}^{\dot b}\\
&-\sqrt2(\mathcal D_n\varphi^{\mathcal I\mathcal J})
(\bar\sigma_E^n)^{\dot ab}(\sigma_E^m)_{b\dot b}
\mathcal D_m\widetilde\Lambda_{\mathcal J}^{\dot b}\\
&-(\mathcal D_m\mathcal M^{\mathcal I}{}_{\mathcal J})
(\bar\sigma_E^m)^{\dot ab}\Lambda_b^{\mathcal J}
-\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_E^m)^{\dot ab}\mathcal D_m\Lambda_b^{\mathcal J}
\Big].
\end{aligned}}
\tag{4C.67b2}
$$

Consequently the boundary primitive and coefficient are

$$
\boxed{
\begin{aligned}
\widetilde{\mathcal S}_E^{m\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
-F_{rs}(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
(\bar\sigma_E^m)^{\dot bb}\Lambda_b^{\mathcal I}\\
&+\sqrt2(\mathcal D_n\varphi^{\mathcal I\mathcal J})
(\bar\sigma_E^n)^{\dot ab}(\sigma_E^m)_{b\dot b}
\widetilde\Lambda_{\mathcal J}^{\dot b}\\
&+\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_E^m)^{\dot ab}\Lambda_b^{\mathcal J}
\Big],\\
\widetilde K_E^{m\dot a\mathcal I}
&=\widetilde{\mathscr C}_E^{m\dot a\mathcal I}
-\widetilde{\mathcal S}_E^{m\dot a\mathcal I},\\
\delta_{\widetilde\varepsilon}\mathcal L_E^{(4)}
&=\partial_m(\widetilde K_E^{m\dot a\mathcal I}
\widetilde\varepsilon_{\dot a\mathcal I}).
\end{aligned}}
\tag{4C.67b3}
$$

Thus

$$
\widetilde j_E^{m\dot a\mathcal I}
:=\widetilde{\mathscr C}_E^{m\dot a\mathcal I}
-\widetilde K_E^{m\dot a\mathcal I}
=\widetilde{\mathcal S}_E^{m\dot a\mathcal I},
\tag{4C.67b4}
$$

namely

$$
\boxed{
\begin{aligned}
\widetilde j_E^{m\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big[&
-F_{rs}(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
(\bar\sigma_E^m)^{\dot bb}\Lambda_b^{\mathcal I}\\
&+\sqrt2(\mathcal D_n\varphi^{\mathcal I\mathcal J})
(\bar\sigma_E^n)^{\dot ab}(\sigma_E^m)_{b\dot b}
\widetilde\Lambda_{\mathcal J}^{\dot b}\\
&+\mathcal M^{\mathcal I}{}_{\mathcal J}
(\bar\sigma_E^m)^{\dot ab}\Lambda_b^{\mathcal J}
\Big].
\end{aligned}}
\tag{4C.67c}
$$

The topological coefficient is

$$
\boxed{
\widetilde{\mathscr C}_{\vartheta,E}^{m\dot a\mathcal I}
=\widetilde K_{\vartheta,E}^{m\dot a\mathcal I}
=+i\mathfrak k_{AB}({}^{\star}F_E^A)^{mn}
(\bar\sigma_{E,n})^{\dot ab}\Lambda_b^{B\mathcal I}.}
\tag{4C.67d}
$$

The Euclidean fermion Euler operators are

$$
\boxed{
\begin{aligned}
\mathcal E_{E,a\mathcal I}
&=(\sigma_E^m)_{a\dot b}\mathcal D_m
\widetilde\Lambda_{\mathcal I}^{\dot b}
+\sqrt2(\widetilde\varphi_{\mathcal I\mathcal J}
\times\Lambda^{\mathcal J})_a,\\
\widetilde{\mathcal E}_{E,\dot a}^{\mathcal I}
&=-(\bar\sigma_E^m)_{\dot ab}\mathcal D_m
\Lambda^{\mathcal Ib}
+\sqrt2(\varphi^{\mathcal I\mathcal J}
\times\widetilde\Lambda_{\mathcal J})_{\dot a}.
\end{aligned}}
\tag{4C.68}
$$

The direct ordered bosonic variation of (4C.43) gives

$$
\boxed{
\begin{aligned}
\mathscr A_E^n={}&
-\mathcal D_mF_{mn}
+\frac14\left(
\varphi^{\mathcal I\mathcal J}
\times\mathcal D_n\widetilde\varphi_{\mathcal I\mathcal J}
+\widetilde\varphi_{\mathcal I\mathcal J}
\times\mathcal D_n\varphi^{\mathcal I\mathcal J}
\right)\\
&-\left[
(\widetilde\Lambda_{\dot a\mathcal I}
\bar\sigma_E^{n\dot aa})\times\Lambda_a^{\mathcal I}
\right],\\
\mathscr P_{E,\mathcal I\mathcal J}={}&
-\frac12\mathcal D_m\mathcal D_m
\widetilde\varphi_{\mathcal I\mathcal J}
+\frac14\varphi^{\mathcal K\mathcal L}\times
(\widetilde\varphi_{\mathcal I\mathcal J}
\times\widetilde\varphi_{\mathcal K\mathcal L})
-\sqrt2(\widetilde\Lambda_{\mathcal I}
\times\widetilde\Lambda_{\mathcal J}),\\
\widetilde{\mathscr P}_E^{\mathcal I\mathcal J}={}&
-\frac12\mathcal D_m\mathcal D_m
\varphi^{\mathcal I\mathcal J}
+\frac14\widetilde\varphi_{\mathcal K\mathcal L}\times
(\varphi^{\mathcal I\mathcal J}
\times\varphi^{\mathcal K\mathcal L})
-\sqrt2(\Lambda^{\mathcal I}\times\Lambda^{\mathcal J}).
\end{aligned}}
\tag{4C.68a}
$$

The exact Wick maps are

$$
\begin{gathered}
j_E^i=-j_L^i|_{\rm Wick},
\qquad
j_E^4=-ij_L^0|_{\rm Wick},
\qquad
\partial_m j_E^m=-(\partial_\mu j_L^\mu)|_{\rm Wick},\\
\mathscr A_E^i=-\mathscr A_L^i|_{\rm Wick},
\qquad
\mathscr A_E^4=-i\mathscr A_L^0|_{\rm Wick},
\qquad
\mathscr P_E=-\mathscr P_L|_{\rm Wick},
\qquad
\widetilde{\mathscr P}_E=-\widetilde{\mathscr P}_L|_{\rm Wick},\\
\mathcal E_E=\mathcal E_L|_{\rm Wick},
\qquad
\widetilde{\mathcal E}_E
=\widetilde{\mathcal E}_L|_{\rm Wick}.
\end{gathered}
\tag{4C.69}
$$

Consequently, direct differentiation of (4C.67) gives

$$
\boxed{
\begin{aligned}
\partial_m j_{E,a\mathcal I}^{m}
=h\operatorname{tr}_{\kappa}\Big\{&
+\mathscr A_E^n(\sigma_{E,n})_{a\dot b}
\widetilde\Lambda_{\mathcal I}^{\dot b}
+\sqrt2\mathscr P_{E,\mathcal I\mathcal J}
\Lambda_a^{\mathcal J}\\
&+\frac1{\sqrt2}
\epsilon_{\mathcal J\mathcal K\mathcal I\mathcal M}
\widetilde{\mathscr P}_E^{\mathcal J\mathcal K}
\Lambda_a^{\mathcal M}\\
&+\left[
\delta_{\mathcal I}^{\mathcal J}
(\sigma_E^{rs})_b{}^c\epsilon_{ca}F_{rs}
-\mathcal M^{\mathcal J}{}_{\mathcal I}\epsilon_{ba}
\right]\mathcal E_E^b{}_{\mathcal J}\\
&-\sqrt2(\sigma_E^n)_{a\dot b}
(\mathcal D_n\widetilde\varphi_{\mathcal J\mathcal I})
\widetilde{\mathcal E}_E^{\dot b\mathcal J}
\Big\}.
\end{aligned}}
\tag{4C.69a}
$$

The independent Euclidean tilde-current obeys

$$
\boxed{
\begin{aligned}
\partial_m\widetilde j_E^{m\dot a\mathcal I}
=h\operatorname{tr}_\kappa\Big\{&
+\mathscr A_E^n(\bar\sigma_{E,n})^{\dot ab}
\Lambda_b^{\mathcal I}
+\sqrt2\widetilde{\mathscr P}_E^{\mathcal I\mathcal J}
\widetilde\Lambda_{\mathcal J}^{\dot a}\\
&+\frac1{\sqrt2}
\epsilon^{\mathcal J\mathcal K\mathcal I\mathcal M}
\mathscr P_{E,\mathcal J\mathcal K}
\widetilde\Lambda_{\mathcal M}^{\dot a}\\
&+\left[
-\delta_{\mathcal J}^{\mathcal I}
(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}F_{rs}
+\mathcal M^{\mathcal I}{}_{\mathcal J}
\delta^{\dot a}{}_{\dot b}
\right]\widetilde{\mathcal E}_E^{\dot b\mathcal J}\\
&-\sqrt2(\bar\sigma_E^n)^{\dot ab}
(\mathcal D_n\varphi^{\mathcal J\mathcal I})
\mathcal E_{E,b\mathcal J}
\Big\}.
\end{aligned}}
\tag{4C.69a1}
$$

For two Euclidean transformations, define

$$
v_E^m=-2\left(
\varepsilon_1^{\mathcal I}\sigma_E^m
\widetilde\varepsilon_{2\mathcal I}
-\varepsilon_2^{\mathcal I}\sigma_E^m
\widetilde\varepsilon_{1\mathcal I}\right),
\tag{4C.69b}
$$

$$
\begin{aligned}
\Omega_E:=-\sqrt2\Big[&
(\varepsilon_1^{\mathcal I}\varepsilon_2^{\mathcal J}
-\varepsilon_2^{\mathcal I}\varepsilon_1^{\mathcal J})
\widetilde\varphi_{\mathcal I\mathcal J}\\
&+(\widetilde\varepsilon_{1\mathcal I}
\widetilde\varepsilon_{2\mathcal J}
-\widetilde\varepsilon_{2\mathcal I}
\widetilde\varepsilon_{1\mathcal J})
\varphi^{\mathcal I\mathcal J}\Big].
\end{aligned}
\tag{4C.69c}
$$

The bosonic Euclidean closure is

$$
\boxed{
\begin{aligned}
[\delta_{E,1},\delta_{E,2}]A_m
&=v_E^nF_{nm}-\mathcal D_m\Omega_E,\\
[\delta_{E,1},\delta_{E,2}]
\varphi^{\mathcal I\mathcal J}
&=v_E^m\mathcal D_m\varphi^{\mathcal I\mathcal J}
+\Omega_E\times\varphi^{\mathcal I\mathcal J},\\
[\delta_{E,1},\delta_{E,2}]
\widetilde\varphi_{\mathcal I\mathcal J}
&=v_E^m\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J}
+\Omega_E\times\widetilde\varphi_{\mathcal I\mathcal J}.
\end{aligned}}
\tag{4C.69d}
$$

The ordinary-coordinate gauge parameter is

$$
\alpha_{12,E}=-v_E^mA_m-\Omega_E.
\tag{4C.69d1}
$$

The two Euclidean fermion remainders are

$$
\boxed{
\begin{aligned}
\mathscr R_{E,a}^{\mathcal I}={}&
-2(\varepsilon_1^{\mathcal I}\varepsilon_2^{\mathcal J}
-\varepsilon_2^{\mathcal I}\varepsilon_1^{\mathcal J})
\mathcal E_{E,a\mathcal J}\\
&-(\varepsilon_{1a}^{\mathcal I}\varepsilon_2^{\mathcal Jb}
-\varepsilon_{2a}^{\mathcal I}\varepsilon_1^{\mathcal Jb})
\mathcal E_{E,b\mathcal J}\\
&-\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}
(\widetilde\varepsilon_{1\mathcal K}
\widetilde\varepsilon_{2\mathcal L}
-\widetilde\varepsilon_{2\mathcal K}
\widetilde\varepsilon_{1\mathcal L})
\mathcal E_{E,a\mathcal J}\\
&-(\varepsilon_{1a}^{\mathcal I}
\widetilde\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal I}
\widetilde\varepsilon_{1\mathcal J\dot b})
\widetilde{\mathcal E}_E^{\mathcal J\dot b}\\
&+2(\varepsilon_{1a}^{\mathcal J}
\widetilde\varepsilon_{2\mathcal J\dot b}
-\varepsilon_{2a}^{\mathcal J}
\widetilde\varepsilon_{1\mathcal J\dot b})
\widetilde{\mathcal E}_E^{\mathcal I\dot b},
\end{aligned}}
\tag{4C.69e}
$$

$$
\boxed{
\begin{aligned}
\widetilde{\mathscr R}_{E,\dot a\mathcal I}={}&
-2(\widetilde\varepsilon_{1\mathcal I}
\widetilde\varepsilon_{2\mathcal J}
-\widetilde\varepsilon_{2\mathcal I}
\widetilde\varepsilon_{1\mathcal J})
\widetilde{\mathcal E}_{E,\dot a}^{\mathcal J}\\
&+(\widetilde\varepsilon_{1\dot a\mathcal I}
\widetilde\varepsilon_{2\mathcal J}^{\dot b}
-\widetilde\varepsilon_{2\dot a\mathcal I}
\widetilde\varepsilon_{1\mathcal J}^{\dot b})
\widetilde{\mathcal E}_{E,\dot b}^{\mathcal J}\\
&-\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
(\varepsilon_1^{\mathcal K}\varepsilon_2^{\mathcal L}
-\varepsilon_2^{\mathcal K}\varepsilon_1^{\mathcal L})
\widetilde{\mathcal E}_{E,\dot a}^{\mathcal J}\\
&-(\widetilde\varepsilon_{1\dot a\mathcal I}
\varepsilon_2^{\mathcal Jb}
-\widetilde\varepsilon_{2\dot a\mathcal I}
\varepsilon_1^{\mathcal Jb})\mathcal E_{E,b\mathcal J}\\
&+2(\widetilde\varepsilon_{1\dot a\mathcal J}
\varepsilon_2^{\mathcal Jb}
-\widetilde\varepsilon_{2\dot a\mathcal J}
\varepsilon_1^{\mathcal Jb})\mathcal E_{E,b\mathcal I}.
\end{aligned}}
\tag{4C.69f}
$$

Therefore

$$
\boxed{
\begin{aligned}
[\delta_{E,1},\delta_{E,2}]\Lambda_a^{\mathcal I}
&=v_E^m\mathcal D_m\Lambda_a^{\mathcal I}
+(\Omega_E\times\Lambda^{\mathcal I})_a
+\mathscr R_{E,a}^{\mathcal I},\\
[\delta_{E,1},\delta_{E,2}]
\widetilde\Lambda_{\dot a\mathcal I}
&=v_E^m\mathcal D_m\widetilde\Lambda_{\dot a\mathcal I}
+(\Omega_E\times\widetilde\Lambda_{\mathcal I})_{\dot a}
+\widetilde{\mathscr R}_{E,\dot a\mathcal I}.
\end{aligned}}
\tag{4C.69g}
$$

Finally, the exact internal and spinor reductions used in
(4C.55)--(4C.69) are

$$
\begin{gathered}
\varphi^{\mathcal I\mathcal J}
=\frac1{\sqrt2}\rho_u^{\mathcal I\mathcal J}X^u,
\qquad
\widetilde\varphi_{\mathcal I\mathcal J}
=\frac1{\sqrt2}\widetilde\rho_{u,\mathcal I\mathcal J}X^u,\\
\rho_{2r-1}^{\,s4}=\delta_r^s,
\qquad
\rho_{2r}^{\,s4}=i\delta_r^s,
\qquad
\rho_{2r-1}^{\,st}=\varepsilon^{str},
\qquad
\rho_{2r}^{\,st}=-i\varepsilon^{str},\\
\widetilde\rho_{u,\mathcal I\mathcal J}
=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\rho_u^{\mathcal K\mathcal L},\\
\rho_u^{\mathcal I\mathcal K}
\widetilde\rho_{v,\mathcal K\mathcal J}
+\rho_v^{\mathcal I\mathcal K}
\widetilde\rho_{u,\mathcal K\mathcal J}
=-2\delta_{uv}\delta^{\mathcal I}{}_{\mathcal J},\\
\sum_u\widetilde\rho_{u,\mathcal I\mathcal J}
\rho_u^{\mathcal K\mathcal L}
=2(\delta_{\mathcal I}^{\mathcal K}\delta_{\mathcal J}^{\mathcal L}
-\delta_{\mathcal I}^{\mathcal L}\delta_{\mathcal J}^{\mathcal K}),\\
\sum_u\rho_u^{\mathcal I\mathcal J}
\rho_u^{\mathcal K\mathcal L}=2\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L},
\qquad
\operatorname{tr}_4(\rho_u\widetilde\rho_v)=-4\delta_{uv}.
\end{gathered}
\tag{4C.70}
$$

$$
\begin{gathered}
(\bar\sigma_L^\mu)^{\dot aa}(\sigma_{L,\mu})_{b\dot b}
=-2\delta_b{}^a\delta_{\dot b}{}^{\dot a},\\
\chi_a(\xi\zeta)+\xi_a(\zeta\chi)+\zeta_a(\chi\xi)=0,\\
(\sigma_L^{\rho\sigma})_a{}^b(\sigma_L^\mu)_{b\dot b}
=\frac12\left(
\eta^{\rho\mu}\sigma_L^\sigma
-\eta^{\sigma\mu}\sigma_L^\rho
-i\epsilon_L^{\rho\sigma\mu\nu}\sigma_{L,\nu}
\right)_{a\dot b}.
\end{gathered}
\tag{4C.71}
$$
