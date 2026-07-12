# 00 3+1d SUSY QFT — Convention Lock

## Step 4A. Pure \(\mathcal N=1\) super Yang--Mills

### 4A.1 Superspace action

$$
\boxed{
S_L^{(1)}
=\frac14\int d^4x_L\left(
[f_{AB}\mathcal W_L^{Aa}\mathcal W^B_{La}]_F
+[\bar f_{AB}\widetilde{\mathcal W}_{L\dot a}^{A}
\widetilde{\mathcal W}_L^{B\dot a}]_{\widetilde F}
\right).}
\tag{4A.1}
$$

$$
\boxed{
S_E^{(1)}
=-\frac14\int d^4x_E\left(
[f_{AB}\mathcal W_E^{Aa}\mathcal W^B_{Ea}]_F
+[\widetilde f_{AB}\widetilde{\mathcal W}_{E\dot a}^{A}
\widetilde{\mathcal W}_E^{B\dot a}]_{\widetilde F}
\right).}
\tag{4A.2}
$$

$$
\mathfrak h_{AB}:=\frac12(f_{AB}+\widetilde f_{AB}),
\qquad
\mathfrak k_{AB}:=\frac1{2i}(f_{AB}-\widetilde f_{AB}).
\tag{4A.3}
$$

On the Lorentzian contour,

$$
\widetilde f_{AB}=\bar f_{AB},
\qquad
f_{AB}
=\left(\frac1{g^2}
-\frac{i\vartheta_{\rm YM}}{8\pi^2}\right)\kappa_{AB}.
\tag{4A.4}
$$

### 4A.2 Ordered component projection

Step 3A gives

$$
\begin{aligned}
[\mathcal W_L^{Aa}\mathcal W^B_{La}]_F
={}&\mathscr D^A\mathscr D^B
-\frac12F^A_{\mu\nu}F^{B\mu\nu}
+\frac i4\epsilon_L^{\mu\nu\rho\sigma}
F^A_{\mu\nu}F^B_{\rho\sigma}\\
&+i\lambda^{Aa}\sigma_{L,a\dot b}^{\mu}
\mathcal D_\mu\bar\lambda^{B\dot b}
+i\lambda^{Ba}\sigma_{L,a\dot b}^{\mu}
\mathcal D_\mu\bar\lambda^{A\dot b}.
\end{aligned}
\tag{4A.5}
$$

Using \(f_{AB}=f_{BA}\), direct addition of the antichiral projector is

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm raw}}^{(1)}={}&
-\frac14\mathfrak h_{AB}F_{\mu\nu}^AF^{B\mu\nu}
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B
+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&+\frac i2f_{AB}\lambda^{Aa}\sigma_{L,a\dot b}^{\mu}
\mathcal D_\mu\bar\lambda^{B\dot b}
+\frac i2\bar f_{AB}\bar\lambda^A_{\dot a}
\bar\sigma_L^{\mu\dot aa}\mathcal D_\mu\lambda_a^B.
\end{aligned}}
\tag{4A.6}
$$

The ordered integration by parts is

$$
\begin{aligned}
\mathcal D_\mu
(\lambda^{Aa}\sigma_{L,a\dot b}^{\mu}\bar\lambda^{B\dot b})
={}&
(\mathcal D_\mu\lambda^{Aa})
\sigma_{L,a\dot b}^{\mu}\bar\lambda^{B\dot b}
+\lambda^{Aa}\sigma_{L,a\dot b}^{\mu}
\mathcal D_\mu\bar\lambda^{B\dot b},\\
(\mathcal D_\mu\lambda^{Aa})
\sigma_{L,a\dot b}^{\mu}\bar\lambda^{B\dot b}
={}&-\bar\lambda^B_{\dot b}
\bar\sigma_L^{\mu\dot ba}\mathcal D_\mu\lambda_a^A.
\end{aligned}
\tag{4A.7}
$$

Therefore

$$
\mathcal L_{L,{\rm raw}}^{(1)}
=\mathcal L_{L,{\rm compact}}^{(1)}+\partial_\mu B_L^\mu,
\qquad
B_L^\mu
=\frac i2f_{AB}\lambda^{Aa}\sigma_{L,a\dot b}^{\mu}
\bar\lambda^{B\dot b},
\tag{4A.8}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm compact}}^{(1)}={}&
-\frac14\mathfrak h_{AB}F_{\mu\nu}^AF^{B\mu\nu}
+i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu
\mathcal D_\mu\lambda^B
+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{4A.9}
$$

Direct Euclidean multiplication gives

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm raw}}^{(1)}={}&
+\frac14\mathfrak h_{AB}F_{mn}^AF_{mn}^B
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B
-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&+\frac12f_{AB}\lambda^{Aa}\sigma_{E,a\dot b}^{m}
\mathcal D_m\widetilde\lambda^{B\dot b}
+\frac12\widetilde f_{AB}\widetilde\lambda^A_{\dot a}
\bar\sigma_E^{m\dot aa}\mathcal D_m\lambda_a^B.
\end{aligned}}
\tag{4A.10}
$$

The same coefficients follow from

$$
\mathcal L_E=-\mathcal L_L\big|_{\rm Wick},
\qquad
\sigma_L^{\mu\nu}F_{\mu\nu}\big|_{\rm Wick}
=-\sigma_E^{mn}F_{mn},
\qquad
\sigma_L^\mu\mathcal D_\mu\big|_{\rm Wick}
=i\sigma_E^m\mathcal D_m.
\tag{4A.11}
$$

### 4A.3 Generic chiral coefficient calculation

For

$$
X_L(y_L,\vartheta)=x+\vartheta^a\xi_a+\vartheta^2f,
\tag{4A.12}
$$

Step 2A gives

$$
\delta_LX_L
=\left[-\varepsilon^a\partial_a
+2i\vartheta^a(\sigma_L^\mu)_{a\dot b}
\bar\varepsilon^{\dot b}\partial_\mu\right]X_L.
\tag{4A.13}
$$

Since

$$
\partial_a\vartheta^2=2\vartheta_a,
\qquad
\vartheta^a\vartheta^b=-\frac12\epsilon^{ab}\vartheta^2,
\tag{4A.14}
$$

coefficient comparison gives

$$
\boxed{
\begin{aligned}
\delta_Lx&=-\varepsilon^a\xi_a,\\
\delta_L\xi_a
&=-2\varepsilon_af
+2i(\sigma_L^\mu)_{a\dot b}
\bar\varepsilon^{\dot b}\partial_\mu x,\\
\delta_Lf
&=i(\sigma_L^\mu)^a{}_{\dot b}
\bar\varepsilon^{\dot b}\partial_\mu\xi_a.
\end{aligned}}
\tag{4A.15}
$$

The independent Euclidean operator is

$$
\delta_EX_E
=\left[-\varepsilon^a\partial_a
-2\vartheta^a(\sigma_E^m)_{a\dot b}
\bar\varepsilon^{\dot b}\partial_m\right]X_E,
\tag{4A.16}
$$

and hence

$$
\boxed{
\begin{aligned}
\delta_Ex&=-\varepsilon^a\xi_a,\\
\delta_E\xi_a
&=-2\varepsilon_af
-2(\sigma_E^m)_{a\dot b}
\bar\varepsilon^{\dot b}\partial_mx,\\
\delta_Ef
&=-(\sigma_E^m)^a{}_{\dot b}
\bar\varepsilon^{\dot b}\partial_m\xi_a.
\end{aligned}}
\tag{4A.17}
$$

### 4A.4 Wess--Zumino compensator

The forbidden Lorentzian coefficients of the bare inverse pullback are

$$
\begin{aligned}
\delta_0\mathcal V_L\big|_{\bar\vartheta}
&=2\varepsilon\sigma_L^\mu\bar\vartheta A_\mu,
&\delta_0\mathcal V_L\big|_{\vartheta}
&=2\vartheta\sigma_L^\mu\bar\varepsilon A_\mu,\\
\delta_0\mathcal V_L\big|_{\vartheta^2}
&=-2i\vartheta^2\bar\varepsilon\bar\lambda,
&\delta_0\mathcal V_L\big|_{\bar\vartheta^2}
&=+2i\bar\vartheta^2\varepsilon\lambda.
\end{aligned}
\tag{4A.18}
$$

For

$$
\delta_ge^{\mathcal V}=i\bar\Lambda e^{\mathcal V}
-ie^{\mathcal V}\Lambda,
\tag{4A.19}
$$

they are cancelled by

$$
\boxed{
\begin{aligned}
\Lambda_L
&=-2i\vartheta\sigma_L^\mu\bar\varepsilon A_\mu
-2\vartheta^2\bar\varepsilon\bar\lambda,\\
\bar\Lambda_L
&=+2i\varepsilon\sigma_L^\mu\bar\vartheta A_\mu
-2\bar\vartheta^2\varepsilon\lambda.
\end{aligned}}
\tag{4A.20}
$$

The direct Euclidean cancellation gives

$$
\boxed{
\begin{aligned}
\Lambda_E
&=+2\vartheta\sigma_E^m\bar\varepsilon A_m
-2\vartheta^2\bar\varepsilon\widetilde\lambda,\\
\widetilde\Lambda_E
&=-2\varepsilon\sigma_E^m\bar\vartheta A_m
-2\bar\vartheta^2\varepsilon\lambda.
\end{aligned}}
\tag{4A.21}
$$

### 4A.5 Lorentzian component transformations

Write

$$
\mathcal W_{La}
=w_a+\vartheta^b\mathsf M_{L,ba}+\vartheta^2\rho_{L,a},
\tag{4A.22}
$$

$$
\begin{aligned}
w_a&=-i\lambda_a,\\
\mathsf M_{L,ba}
&=\epsilon_{ab}\mathscr D
+i(\sigma_L^{\mu\nu})_a{}^c\epsilon_{cb}F_{\mu\nu},\\
\rho_{L,a}
&=-(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\lambda^{\dot b}.
\end{aligned}
\tag{4A.23}
$$

Equations (4A.13) and (4A.23) give

$$
\begin{aligned}
-i\delta\lambda_a
&=-\varepsilon^b\mathsf M_{L,ba}\\
&=-\varepsilon_a\mathscr D
-i(\sigma_L^{\mu\nu})_a{}^b\varepsilon_bF_{\mu\nu},
\end{aligned}
\tag{4A.24}
$$

$$
\delta\mathsf M_{L,ba}
=-2\varepsilon_b\rho_{L,a}
+2i(\sigma_L^\mu)_{b\dot c}\bar\varepsilon^{\dot c}
\mathcal D_\mu w_a.
\tag{4A.25}
$$

The trace and traceless parts of (4A.25), together with (4A.20), give

$$
\boxed{
\begin{aligned}
\delta_LA_\mu^A
&=-i\varepsilon^a(\sigma_{L,\mu})_{a\dot b}
\bar\lambda^{A\dot b}
-i\bar\varepsilon_{\dot a}
(\bar\sigma_{L,\mu})^{\dot ab}\lambda_b^A,\\
\delta_L\lambda_a^A
&=(\sigma_L^{\mu\nu})_a{}^b\varepsilon_bF_{\mu\nu}^A
-i\varepsilon_a\mathscr D^A,\\
\delta_L\bar\lambda_{\dot a}^A
&=-\bar\varepsilon_{\dot b}
(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}F_{\mu\nu}^A
+i\bar\varepsilon_{\dot a}\mathscr D^A,\\
\delta_L\mathscr D^A
&=-\varepsilon^a(\sigma_L^\mu)_{a\dot b}
(\mathcal D_\mu\bar\lambda^{\dot b})^A
+\bar\varepsilon_{\dot a}(\bar\sigma_L^\mu)^{\dot aa}
(\mathcal D_\mu\lambda_a)^A.
\end{aligned}}
\tag{4A.26}
$$

### 4A.6 Euclidean component transformations

Direct comparison of the coefficients of \(\mathcal W_E\), followed by
the independent comparison of \(\widetilde{\mathcal W}_E\), gives

$$
\boxed{
\begin{aligned}
\delta_EA_m^A
&=\varepsilon^a(\sigma_{E,m})_{a\dot b}
\widetilde\lambda^{A\dot b}
+\bar\varepsilon_{\dot a}
(\bar\sigma_{E,m})^{\dot ab}\lambda_b^A,\\
\delta_E\lambda_a^A
&=-(\sigma_E^{mn})_a{}^b\varepsilon_bF_{mn}^A
-i\varepsilon_a\mathscr D^A,\\
\delta_E\widetilde\lambda_{\dot a}^A
&=\bar\varepsilon_{\dot b}
(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}F_{mn}^A
+i\bar\varepsilon_{\dot a}\mathscr D^A,\\
\delta_E\mathscr D^A
&=-i\varepsilon^a(\sigma_E^m)_{a\dot b}
(\mathcal D_m\widetilde\lambda^{\dot b})^A
+i\bar\varepsilon_{\dot a}(\bar\sigma_E^m)^{\dot aa}
(\mathcal D_m\lambda_a)^A.
\end{aligned}}
\tag{4A.27}
$$

Equations (4A.26) and (4A.27) agree term by term under (4A.11).

### 4A.7 Off-shell closure

For \([\delta_1,\delta_2]:=\delta_1\delta_2-\delta_2\delta_1\),

$$
v_L^\mu
=2i(\varepsilon_1\sigma_L^\mu\bar\varepsilon_2
-\varepsilon_2\sigma_L^\mu\bar\varepsilon_1),
\qquad
v_E^m
=-2(\varepsilon_1\sigma_E^m\bar\varepsilon_2
-\varepsilon_2\sigma_E^m\bar\varepsilon_1).
\tag{4A.28}
$$

Direct substitution of (4A.26)--(4A.27) gives

$$
\boxed{
\begin{aligned}
[\delta_1,\delta_2]A_M&=v^NF_{NM},\\
[\delta_1,\delta_2]X&=v^N\mathcal D_NX,
\qquad
X\in\{\lambda,\widetilde\lambda,\bar\lambda,
\mathscr D,F_{MN}\}.
\end{aligned}}
\tag{4A.29}
$$

$$
v^NF_{NM}
=v^N\partial_NA_M+\mathcal D_M(-v^NA_N),
\tag{4A.30}
$$

so

$$
[\delta_1,\delta_2]
=v^N\partial_N+\delta_{\alpha_{12}},
\qquad
\alpha_{12}=-v^NA_N.
\tag{4A.31}
$$

No equation of motion enters.  Closure on \(F_{MN}\) uses

$$
[\mathcal D_M,[\mathcal D_N,\mathcal D_R]]+\text{cyclic}
=-i(\mathcal D_MF_{NR}+\mathcal D_NF_{RM}
+\mathcal D_RF_{MN})=0.
\tag{4A.32}
$$

### 4A.8 Lorentzian local-parameter calculation

For the raw density (4A.6),

$$
\begin{aligned}
\Theta_L^\mu(\delta)={}&
-\left[\mathfrak h_{AB}F^{A\mu\nu}
+\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}\right]
\delta A_\nu^B\\
&+\frac i2f_{AB}\lambda^{Aa}\sigma_{L,a\dot b}^\mu
\delta\bar\lambda^{B\dot b}
+\frac i2\bar f_{AB}\bar\lambda^A_{\dot a}
\bar\sigma_L^{\mu\dot aa}\delta\lambda_a^B,
\end{aligned}
\tag{4A.33}
$$

$$
({}^{\star}F_L)^{\mu\nu}
:=\frac12\epsilon_L^{\mu\nu\rho\sigma}F_{\rho\sigma},
\qquad
\mathcal G_{L,B}^{\mu\nu}
:=\mathfrak h_{AB}F^{A\mu\nu}
+\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}.
\tag{4A.34}
$$

Move the local parameters to the right:

$$
\Theta_L^\mu(\delta_\varepsilon)
=C_{L,a}^\mu\varepsilon^a
+\bar C_L^{\mu\dot a}\bar\varepsilon_{\dot a}.
\tag{4A.35}
$$

Substitution of (4A.26) into (4A.33) gives

$$
\boxed{
\begin{aligned}
C_{L,a}^\mu={}&
-i\mathcal G_{L,B}^{\mu\nu}
(\sigma_{L,\nu})_{a\dot b}\bar\lambda^{B\dot b}\\
&+\frac i2\bar f_{AB}\bar\lambda^A_{\dot c}
(\bar\sigma_L^\mu)^{\dot cb}
(\sigma_L^{\rho\sigma})_b{}^d\epsilon_{da}F_{\rho\sigma}^B\\
&+\frac12\bar f_{AB}\bar\lambda^A_{\dot c}
(\bar\sigma_L^\mu)^{\dot cb}\epsilon_{ba}\mathscr D^B,
\end{aligned}}
\tag{4A.36}
$$

$$
\boxed{
\begin{aligned}
\bar C_L^{\mu\dot a}={}&
-i\mathcal G_{L,B}^{\mu\nu}
(\bar\sigma_{L,\nu})^{\dot ab}\lambda_b^B\\
&-\frac i2f_{AB}\lambda^{Ab}(\sigma_L^\mu)_{b\dot c}
\epsilon^{\dot c\dot d}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot d}
F_{\rho\sigma}^B\\
&-\frac12f_{AB}\lambda^{Ab}(\sigma_L^\mu)_{b\dot c}
\epsilon^{\dot c\dot a}\mathscr D^B.
\end{aligned}}
\tag{4A.37}
$$

The linear fermion coefficients of the two chiral projectors are

$$
\begin{aligned}
\zeta_{L,a}
&=-2f_{AB}(\sigma_L^{\rho\sigma})_a{}^b
F_{\rho\sigma}^A\lambda_b^B
-2if_{AB}\mathscr D^A\lambda_a^B,\\
\widetilde\zeta_L^{\dot a}
&=-2\bar f_{AB}(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
F_{\rho\sigma}^A\bar\lambda^{B\dot b}
+2i\bar f_{AB}\mathscr D^A\bar\lambda^{B\dot a}.
\end{aligned}
\tag{4A.38}
$$

Equation (4A.15) applied to the two projector multiplets gives

$$
\delta_L\mathcal L_{L,{\rm raw}}^{(1)}
=\partial_\mu
\left(K_{L,a}^\mu\varepsilon^a
+\bar K_L^{\mu\dot a}\bar\varepsilon_{\dot a}\right),
\tag{4A.39}
$$

$$
K_{L,a}^\mu
=-\frac i4(\sigma_L^\mu)_{a\dot b}
\widetilde\zeta_L^{\dot b},
\qquad
\bar K_L^{\mu\dot a}
=-\frac i4(\sigma_L^\mu)^{b\dot a}\zeta_{L,b}.
\tag{4A.40}
$$

Therefore

$$
\delta_{\varepsilon(x)}\mathcal L_L
=\partial_\mu(K_L^\mu\varepsilon)
+(C_L^\mu-K_L^\mu)\partial_\mu\varepsilon,
\tag{4A.41}
$$

$$
\boxed{
j_{L,a}^\mu=C_{L,a}^\mu-K_{L,a}^\mu,
\qquad
\bar j_L^{\mu\dot a}
=\bar C_L^{\mu\dot a}-\bar K_L^{\mu\dot a}.}
\tag{4A.42}
$$

No improvement has been added.

### 4A.9 Euler operators and current divergence

$$
\mathcal E_{\mathscr D,C}
=\mathfrak h_{CB}\mathscr D^B,
\tag{4A.43}
$$

$$
\mathcal E_\lambda^{Ca}
=i\mathfrak h_{CB}(\mathcal D_\mu\bar\lambda^B_{\dot b})
(\bar\sigma_L^\mu)^{\dot ba},
\qquad
\mathcal E_{\bar\lambda}^{C\dot a}
=i\mathfrak h_{CB}(\bar\sigma_L^\mu)^{\dot aa}
(\mathcal D_\mu\lambda_a)^B,
\tag{4A.44}
$$

$$
\mathcal E_{A,C}^{\nu}
=\mathfrak h_{CB}(\mathcal D_\mu F^{\mu\nu})^B
+i\mathfrak h_{AB}c_{CD}{}^B
\bar\lambda^A_{\dot a}(\bar\sigma_L^\nu)^{\dot aa}
\lambda_a^D.
\tag{4A.45}
$$

The \(\mathfrak k\)-term drops out because

$$
(\mathcal D_\mu{}^{\star}F_L^{\mu\nu})^A=0.
\tag{4A.46}
$$

Direct differentiation of (4A.42) gives

$$
\boxed{
\begin{aligned}
\partial_\mu j_{L,a}^\mu={}&
-i\mathcal E_{A,C}^{\nu}
(\sigma_{L,\nu})_{a\dot b}\bar\lambda^{C\dot b}\\
&-\mathcal E_{\mathscr D,C}
(\sigma_L^\rho)_{a\dot b}
(\mathcal D_\rho\bar\lambda^{\dot b})^C\\
&+\left[(\sigma_L^{\rho\sigma})_b{}^c\epsilon_{ca}
F_{\rho\sigma}^C-i\epsilon_{ba}\mathscr D^C\right]
\mathcal E_\lambda^{Cb},
\end{aligned}}
\tag{4A.47}
$$

$$
\boxed{
\begin{aligned}
\partial_\mu\bar j_L^{\mu\dot a}={}&
-i\mathcal E_{A,C}^{\nu}
(\bar\sigma_{L,\nu})^{\dot ab}\lambda_b^C\\
&-\mathcal E_{\mathscr D,C}
(\sigma_L^\rho)^{b\dot a}(\mathcal D_\rho\lambda_b)^C\\
&+\left[-(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
F_{\rho\sigma}^C+i\delta^{\dot a}{}_{\dot b}\mathscr D^C\right]
\mathcal E_{\bar\lambda}^{C\dot b}.
\end{aligned}}
\tag{4A.48}
$$

### 4A.10 Euclidean current

$$
({}^{\star}F_E)^{mn}:=\frac12\epsilon_E^{mnrs}F_{rs},
\qquad
\mathcal G_{E,B}^{mn}
:=\mathfrak h_{AB}F^{Amn}
-i\mathfrak k_{AB}({}^{\star}F_E^A)^{mn}.
\tag{4A.49}
$$

The direct Euclidean symplectic coefficient is

$$
\begin{aligned}
\Theta_E^m(\delta)={}&
\mathcal G_{E,B}^{mn}\delta A_n^B
+\frac12f_{AB}\lambda^{Aa}\sigma_{E,a\dot b}^{m}
\delta\widetilde\lambda^{B\dot b}\\
&+\frac12\widetilde f_{AB}\widetilde\lambda^A_{\dot a}
\bar\sigma_E^{m\dot aa}\delta\lambda_a^B.
\end{aligned}
\tag{4A.50}
$$

Its ordered local-parameter coefficients are

$$
\boxed{
\begin{aligned}
C_{E,a}^m={}&
-\mathcal G_{E,B}^{mn}(\sigma_{E,n})_{a\dot b}
\widetilde\lambda^{B\dot b}\\
&-\frac12\widetilde f_{AB}\widetilde\lambda^A_{\dot c}
(\bar\sigma_E^m)^{\dot cb}(\sigma_E^{rs})_b{}^d
\epsilon_{da}F_{rs}^B\\
&-\frac i2\widetilde f_{AB}\widetilde\lambda^A_{\dot c}
(\bar\sigma_E^m)^{\dot cb}\epsilon_{ba}\mathscr D^B,
\end{aligned}}
\tag{4A.51}
$$

$$
\boxed{
\begin{aligned}
\bar C_E^{m\dot a}={}&
-\mathcal G_{E,B}^{mn}(\bar\sigma_{E,n})^{\dot ab}\lambda_b^B\\
&+\frac12f_{AB}\lambda^{Ab}(\sigma_E^m)_{b\dot c}
\epsilon^{\dot c\dot d}(\bar\sigma_E^{rs})^{\dot a}{}_{\dot d}
F_{rs}^B\\
&+\frac i2f_{AB}\lambda^{Ab}(\sigma_E^m)_{b\dot c}
\epsilon^{\dot c\dot a}\mathscr D^B.
\end{aligned}}
\tag{4A.52}
$$

$$
\begin{aligned}
\zeta_{E,a}
&=2f_{AB}(\sigma_E^{rs})_a{}^bF_{rs}^A\lambda_b^B
-2if_{AB}\mathscr D^A\lambda_a^B,\\
\widetilde\zeta_E^{\dot a}
&=2\widetilde f_{AB}(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
F_{rs}^A\widetilde\lambda^{B\dot b}
+2i\widetilde f_{AB}\mathscr D^A\widetilde\lambda^{B\dot a}.
\end{aligned}
\tag{4A.53}
$$

$$
K_{E,a}^m=-\frac14(\sigma_E^m)_{a\dot b}
\widetilde\zeta_E^{\dot b},
\qquad
\bar K_E^{m\dot a}=-\frac14(\sigma_E^m)^{b\dot a}\zeta_{E,b},
\tag{4A.54}
$$

$$
\boxed{
j_{E,a}^m=C_{E,a}^m-K_{E,a}^m,
\qquad
\bar j_E^{m\dot a}
=\bar C_E^{m\dot a}-\bar K_E^{m\dot a}.}
\tag{4A.55}
$$

Direct Euclidean multiplication and Wick transport agree:

$$
\begin{array}{c|cc}
&m=i&m=4\\ \hline
C_E^m&-C_L^i|_{\rm Wick}&-iC_L^0|_{\rm Wick}\\
K_E^m&-K_L^i|_{\rm Wick}&-iK_L^0|_{\rm Wick}\\
j_E^m&-j_L^i|_{\rm Wick}&-ij_L^0|_{\rm Wick}
\end{array}.
\tag{4A.56}
$$

The Euclidean integration by parts is

$$
f_{AB}\lambda^{Aa}\sigma_{E,a\dot b}^{m}
\mathcal D_m\widetilde\lambda^{B\dot b}
=\partial_m\!\left(
f_{AB}\lambda^A\sigma_E^m\widetilde\lambda^B\right)
+f_{AB}\widetilde\lambda^A\bar\sigma_E^m
\mathcal D_m\lambda^B,
\tag{4A.56a}
$$

and therefore

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm compact}}^{(1)}={}&
+\frac14\mathfrak h_{AB}F_{mn}^AF_{mn}^B
+\mathfrak h_{AB}\widetilde\lambda^A\bar\sigma_E^m
\mathcal D_m\lambda^B
-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B,
\end{aligned}}
\qquad
\mathcal L_{E,{\rm raw}}^{(1)}
=\mathcal L_{E,{\rm compact}}^{(1)}
+\partial_m\!\left(
\frac12f_{AB}\lambda^A\sigma_E^m\widetilde\lambda^B\right).
\tag{4A.56b}
$$

Direct variation of (4A.56b), with the odd Euler coefficient placed to
the right of the varied left-handed fermion, gives

$$
\boxed{
\begin{aligned}
\mathcal E_{E,\mathscr D,C}
&=-\mathfrak h_{CB}\mathscr D^B,\\
\mathcal E_{E,\lambda}^{Ca}
&=\mathfrak h_{CB}(\mathcal D_m\widetilde\lambda^B_{\dot b})
(\bar\sigma_E^m)^{\dot ba},\\
\mathcal E_{E,\widetilde\lambda}^{C\dot a}
&=\mathfrak h_{CB}(\bar\sigma_E^m)^{\dot aa}
(\mathcal D_m\lambda_a)^B,\\
\mathcal E_{E,A,C}^{n}
&=-\mathfrak h_{CB}(\mathcal D_mF^{mn})^B
+\mathfrak h_{AB}c_{CD}{}^B
\widetilde\lambda^A_{\dot a}
(\bar\sigma_E^n)^{\dot aa}\lambda_a^D.
\end{aligned}}
\tag{4A.56c}
$$

The topological contribution to
\(\mathcal E_{E,A,C}^{n}\) is zero because

$$
(\mathcal D_m{}^{\star}F_E^{mn})^A
=\frac16\epsilon_E^{mnrs}
\left(\mathcal D_mF_{rs}+\mathcal D_rF_{sm}
+\mathcal D_sF_{mr}\right)^A=0.
\tag{4A.56d}
$$

Move the parameters in (4A.27) to the right and differentiate
(4A.55).  The two independent spinor coefficients are

$$
\boxed{
\begin{aligned}
\partial_mj_{E,a}^{m}={}&
+\mathcal E_{E,A,C}^{n}(\sigma_{E,n})_{a\dot b}
\widetilde\lambda^{C\dot b}
-i\mathcal E_{E,\mathscr D,C}(\sigma_E^r)_{a\dot b}
(\mathcal D_r\widetilde\lambda^{\dot b})^C\\
&+\left[-(\sigma_E^{rs})_b{}^c\epsilon_{ca}F_{rs}^C
-i\epsilon_{ba}\mathscr D^C\right]
\mathcal E_{E,\lambda}^{Cb},\\[2mm]
\partial_m\bar j_E^{m\dot a}={}&
+\mathcal E_{E,A,C}^{n}(\bar\sigma_{E,n})^{\dot ab}
\lambda_b^C
+i\mathcal E_{E,\mathscr D,C}(\bar\sigma_E^r)^{\dot ab}
(\mathcal D_r\lambda_b)^C\\
&+\left[(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}F_{rs}^C
+i\delta^{\dot a}{}_{\dot b}\mathscr D^C\right]
\mathcal E_{E,\widetilde\lambda}^{C\dot b}.
\end{aligned}}
\tag{4A.56e}
$$

The second derivatives of the gauge term reduce to (4A.56d).
The remaining cubic terms are already the second term of
\(\mathcal E_{E,A,C}^{n}\) in (4A.56c), with the field order fixed by
the two-spinor Schouten identity and trace invariance (4.9).
Thus (4A.56e) has no residual, and the Wick map sends
(4A.47)--(4A.48) to (4A.56e) coefficient by coefficient.

### 4A.11 Reality contour

$$
A_m^\dagger=A_m,
\qquad
\widetilde f=f^\dagger,
\qquad
\mathfrak h>0,
\qquad
\mathscr D^A=id^A,
\qquad
d^A\in\mathbb R.
\tag{4A.57}
$$

The intrinsic Euclidean pair
\((\lambda_E,\widetilde\lambda_E)\) remains independent; no
Euclidean fermionic dagger condition is imposed.
