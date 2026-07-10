# 00 3+1d SUSY QFT — Convention Lock

## Step 1. Supersymmetry commutator
### 1.1 Indices, parity, contractions
$$
\begin{gathered}
\mu,\nu,\rho,\sigma=0,1,2,3,\qquad i,j,k=1,2,3,\qquad m,n,r,s=1,2,3,4,\\
a,b,c=1,2,\qquad \dot a,\dot b,\dot c=\dot1,\dot2,\\
|J|=|P|=0,\qquad |Q|=|\bar Q|=1,\\
[A,B\}:=AB-(-1)^{|A||B|}BA .
\end{gathered}
\tag{1.1}
$$
$$
\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1),\qquad
v_\mu=\eta_{\mu\nu}v^\nu,\qquad
\epsilon^{0123}=+1 .
\tag{1.2}
$$
$$
\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,\qquad
\epsilon_{12}=\epsilon_{\dot1\dot2}=-1,
\tag{1.3}
$$
$$
(\epsilon^{ab})=(\epsilon^{\dot a\dot b})
=
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
(\epsilon_{ab})=(\epsilon_{\dot a\dot b})
=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{1.4}
$$
$$
\begin{gathered}
\psi^a=\epsilon^{ab}\psi_b,\qquad
\psi_a=\epsilon_{ab}\psi^b,\qquad
\bar\psi^{\dot a}=\epsilon^{\dot a\dot b}\bar\psi_{\dot b},\qquad
\bar\psi_{\dot a}=\epsilon_{\dot a\dot b}\bar\psi^{\dot b},\\
\epsilon^{ab}\epsilon_{bc}=\delta^a{}_c,\qquad
\epsilon_{ab}\epsilon^{bc}=\delta_a{}^c .
\end{gathered}
\tag{1.5}
$$
$$
\xi\chi:=\xi^a\chi_a,\qquad
\bar\xi\bar\chi:=\bar\xi_{\dot a}\bar\chi^{\dot a}.
\tag{1.6}
$$
$$
\xi^a\chi_a=-\xi_a\chi^a,\qquad
\bar\xi^{\dot a}\bar\chi_{\dot a}
=-\bar\xi_{\dot a}\bar\chi^{\dot a}.
\tag{1.7}
$$
For Grassmann-odd spinors:
$$
\xi\chi=\chi\xi,\qquad
\bar\xi\bar\chi=\bar\chi\bar\xi .
\tag{1.8}
$$
### 1.2 Lorentzian sigma system
$$
\sigma^1=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\sigma^2=
\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\qquad
\sigma^3=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{1.9}
$$
$$
(\sigma_L^\mu)_{a\dot a}
=
(\mathbf 1_2,\sigma^1,\sigma^2,\sigma^3)_{a\dot a}.
\tag{1.10}
$$
$$
(\bar\sigma_L^\mu)^{\dot a a}
:=
\epsilon^{ab}\epsilon^{\dot a\dot b}
(\sigma_L^\mu)_{b\dot b}
=
(\mathbf 1_2,-\sigma^1,-\sigma^2,-\sigma^3)^{\dot a a}.
\tag{1.11}
$$
$$
(\sigma_L^\mu)_{a\dot a}(\bar\sigma_L^\nu)^{\dot a b}
+
(\sigma_L^\nu)_{a\dot a}(\bar\sigma_L^\mu)^{\dot a b}
=
-2\eta^{\mu\nu}\delta_a{}^b,
\tag{1.12}
$$
$$
(\bar\sigma_L^\mu)^{\dot a a}(\sigma_L^\nu)_{a\dot b}
+
(\bar\sigma_L^\nu)^{\dot a a}(\sigma_L^\mu)_{a\dot b}
=
-2\eta^{\mu\nu}\delta^{\dot a}{}_{\dot b}.
\tag{1.13}
$$
$$
(\sigma_L^{\mu\nu})_a{}^b
:=
\frac14
\left[
(\sigma_L^\mu)_{a\dot c}(\bar\sigma_L^\nu)^{\dot c b}
-
(\sigma_L^\nu)_{a\dot c}(\bar\sigma_L^\mu)^{\dot c b}
\right],
\tag{1.14}
$$
$$
(\bar\sigma_L^{\mu\nu})^{\dot a}{}_{\dot b}
:=
\frac14
\left[
(\bar\sigma_L^\mu)^{\dot a c}(\sigma_L^\nu)_{c\dot b}
-
(\bar\sigma_L^\nu)^{\dot a c}(\sigma_L^\mu)_{c\dot b}
\right].
\tag{1.15}
$$
$$
\sigma_L^{0i}=-\frac12\sigma^i,\qquad
\bar\sigma_L^{0i}=+\frac12\sigma^i,\qquad
\sigma_L^{ij}=\bar\sigma_L^{ij}
=-\frac{i}{2}\epsilon^{ijk}\sigma^k .
\tag{1.16}
$$
$$
(\sigma_L^{\mu\nu})_a{}^c(\sigma_L^\rho)_{c\dot b}
-
(\sigma_L^\rho)_{a\dot c}
(\bar\sigma_L^{\mu\nu})^{\dot c}{}_{\dot b}
=
\eta^{\mu\rho}(\sigma_L^\nu)_{a\dot b}
-
\eta^{\nu\rho}(\sigma_L^\mu)_{a\dot b}.
\tag{1.17}
$$
### 1.3 Lorentzian active convention
$$
\left.U_L\right|_{\mathrm{linear}}
:=
1+\frac{i}{2}\omega^L_{\mu\nu}J_L^{\mu\nu}
-i a_L^\mu P^L_\mu
-i\theta_L^aQ^L_a
-i\bar\eta^L_{\dot a}\bar Q_L^{\dot a},
\qquad
\omega^L_{\mu\nu}=-\omega^L_{\nu\mu}.
\tag{1.18}
$$
$$
x_L^{\prime\mu}
=
x_L^\mu+a_L^\mu+\omega_L^\mu{}_\nu x_L^\nu .
\tag{1.19}
$$
The covector transformation of (P\^L_rho) fixes
$$
\begin{aligned}
U_LP^L_\rho U_L^{-1}-P^L_\rho
&=
\frac{i}{2}\omega^L_{\mu\nu}
[J_L^{\mu\nu},P^L_\rho]\\
&=
-\omega^L_\rho{}^\lambda P^L_\lambda ,
\end{aligned}
\tag{1.20}
$$
hence
$$
[P^L_\mu,P^L_\nu]=0,
\tag{1.21}
$$
$$
[J^L_{\mu\nu},P^L_\rho]
=
i\eta_{\mu\rho}P^L_\nu
-i\eta_{\nu\rho}P^L_\mu .
\tag{1.22}
$$
The (JJP) Jacobi identity,
$$
[J^L_{\mu\nu},[J^L_{\rho\sigma},P^L_\lambda]]
-
[J^L_{\rho\sigma},[J^L_{\mu\nu},P^L_\lambda]]
=
[[J^L_{\mu\nu},J^L_{\rho\sigma}],P^L_\lambda],
\tag{1.23}
$$
gives
$$
\begin{aligned}
[J^L_{\mu\nu},J^L_{\rho\sigma}]
=i\big(
&\eta_{\mu\rho}J^L_{\nu\sigma}
-\eta_{\nu\rho}J^L_{\mu\sigma}\\
&-\eta_{\mu\sigma}J^L_{\nu\rho}
+\eta_{\nu\sigma}J^L_{\mu\rho}
\big).
\end{aligned}
\tag{1.24}
$$
### 1.4 Lorentzian Weyl supercharges
$$
\bar Q^L_{\dot a}:=\epsilon_{\dot a\dot b}\bar Q_L^{\dot b},
\qquad
(Q^L_a)^\dagger=\bar Q^L_{\dot a},
\qquad
(Q_L^a)^\dagger=\bar Q_L^{\dot a},
\qquad
(P^L_\mu)^\dagger=P^L_\mu .
\tag{1.25}
$$
$$
(\theta_L^a)^\dagger=\bar\eta_L^{\dot a},
\tag{1.26}
$$
$$
\begin{aligned}
(\theta_L^aQ^L_a)^\dagger
&=
\bar Q^L_{\dot a}\bar\eta_L^{\dot a}\\
&=
-\bar\eta_L^{\dot a}\bar Q^L_{\dot a}\\
&=
\bar\eta^L_{\dot a}\bar Q_L^{\dot a}.
\end{aligned}
\tag{1.27}
$$
Thus the fermionic generator in (1.18) is Hermitian before multiplication by (-i).
The Weyl-spinor transformation is fixed by
$$
\begin{aligned}
Q_a^{L\prime}
&=
Q_a^L+\frac12\omega^L_{\mu\nu}
(\sigma_L^{\mu\nu})_a{}^bQ_b^L,\\
\bar Q_L^{\prime\dot a}
&=
\bar Q_L^{\dot a}
+\frac12\omega^L_{\mu\nu}
(\bar\sigma_L^{\mu\nu})^{\dot a}{}_{\dot b}
\bar Q_L^{\dot b}.
\end{aligned}
\tag{1.28}
$$
Comparing (1.28) with
(delta_omega Q=frac\{i\}\{2\}omega\^L_\{munu\}\[J_L\^\{munu\},Q\]) gives
$$
[J_L^{\mu\nu},Q_a^L]
=
-i(\sigma_L^{\mu\nu})_a{}^bQ_b^L,
\tag{1.29}
$$
$$
[J_L^{\mu\nu},\bar Q_L^{\dot a}]
=
-i(\bar\sigma_L^{\mu\nu})^{\dot a}{}_{\dot b}
\bar Q_L^{\dot b}.
\tag{1.30}
$$
Equivalently,
$$
[J_L^{\mu\nu},\bar Q^L_{\dot a}]
=
+i\bar Q^L_{\dot b}
(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}.
\tag{1.31}
$$
$$
[P^L_\mu,Q^L_a]=0,\qquad
[P^L_\mu,\bar Q_L^{\dot a}]=0 .
\tag{1.32}
$$
Write the Lorentz-covariant mixed anticommutator as
$$
\{Q^L_a,\bar Q^L_{\dot b}\}
=
c_L(\sigma_L^\rho)_{a\dot b}P^L_\rho .
\tag{1.33}
$$
Using (1.17), (1.29), and (1.31),
$$
\begin{aligned}
[J_L^{\mu\nu},\{Q^L_a,\bar Q^L_{\dot b}\}]
&=
\{[J_L^{\mu\nu},Q^L_a],\bar Q^L_{\dot b}\}
+
\{Q^L_a,[J_L^{\mu\nu},\bar Q^L_{\dot b}]\}\\
&=
-ic_L
\left[
(\sigma_L^{\mu\nu})_a{}^c(\sigma_L^\rho)_{c\dot b}
-
(\sigma_L^\rho)_{a\dot c}
(\bar\sigma_L^{\mu\nu})^{\dot c}{}_{\dot b}
\right]P^L_\rho\\
&=
-ic_L
\left[
\eta^{\mu\rho}(\sigma_L^\nu)_{a\dot b}
-
\eta^{\nu\rho}(\sigma_L^\mu)_{a\dot b}
\right]P^L_\rho\\
&=
ic_L
\left[
(\sigma_L^\mu)_{a\dot b}P_L^\nu
-
(\sigma_L^\nu)_{a\dot b}P_L^\mu
\right]\\
&=
c_L(\sigma_L^\rho)_{a\dot b}
[J_L^{\mu\nu},P^L_\rho].
\end{aligned}
\tag{1.34}
$$
Hermitian conjugation of (1.33) gives
$$
c_L\in\mathbb R .
\tag{1.35}
$$
Fix the normalization of (Q\^L_a) by
$$
H:=P_L^0=-P^L_0,\qquad
\{Q^L_1,(Q^L_1)^\dagger\}
+
\{Q^L_2,(Q^L_2)^\dagger\}
:=4H .
\tag{1.36}
$$
At (P\^L_i=0),
$$
\begin{aligned}
\{Q^L_1,(Q^L_1)^\dagger\}
+
\{Q^L_2,(Q^L_2)^\dagger\}
&=
2c_LP^L_0\\
&=
-2c_LH\\
&=
4H,
\end{aligned}
\qquad
c_L=-2 .
\tag{1.37}
$$
For ordinary (N=1) super-Poincaré algebra without tensorial charges,
$$
\{Q^L_a,Q^L_b\}=Z\epsilon_{ab},
\qquad
\{Q^L_a,Q^L_b\}=\{Q^L_b,Q^L_a\},
\qquad
\epsilon_{ab}=-\epsilon_{ba},
\qquad
Z=0 .
\tag{1.38}
$$
Therefore
$$
\boxed{
\begin{aligned}
\{Q^L_a,\bar Q^L_{\dot b}\}
&=-2(\sigma_L^\mu)_{a\dot b}P^L_\mu,\\
\{Q^L_a,Q^L_b\}&=0,\\
\{\bar Q^L_{\dot a},\bar Q^L_{\dot b}\}&=0,\\
[P^L_\mu,Q^L_a]&=0,\\
[P^L_\mu,\bar Q_L^{\dot a}]&=0 .
\end{aligned}}
\tag{1.39}
$$
### 1.5 Wick map fixed by exponent matching
$$
x_E^i=x_L^i,\qquad
x_E^4=i x_L^0,
\qquad
a_E^i=a_L^i,\qquad
a_E^4=i a_L^0 .
\tag{1.40}
$$
From (delta x_E\^4=idelta x_L\^0) and (delta x_E\^i=delta x_L\^i),
$$
\begin{aligned}
\delta x_E^4
&=
i\omega_L^0{}_i x_L^i
=
-i\omega^L_{0i}x_E^i,\\
\delta x_E^i
&=
\omega_L^i{}_0x_L^0+\omega_L^i{}_j x_L^j
=
i\omega^L_{0i}x_E^4+\omega_L^i{}_j x_E^j,
\end{aligned}
\tag{1.41}
$$
hence
$$
\omega^E_{ij}=\omega^L_{ij},
\qquad
\omega^E_{4i}=-i\omega^L_{0i}.
\tag{1.42}
$$
Require the translation terms to be identical:
$$
a_E^mP^E_m
=
a_L^iP^E_i+i a_L^0P^E_4
=
-i a_L^iP^L_i-i a_L^0P^L_0 .
\tag{1.43}
$$
Thus
$$
P^E_i=-iP^L_i,\qquad
P^E_4=-P^L_0=P_L^0=H .
\tag{1.44}
$$
Require the rotation terms to be identical:
$$
\frac{i}{2}\omega^E_{mn}J_E^{mn}
=
\frac{i}{2}\omega^L_{\mu\nu}J_L^{\mu\nu}.
\tag{1.45}
$$
Using (1.42),
$$
J_E^{ij}=J_L^{ij},
\qquad
J_E^{4i}=iJ_L^{0i}=-iJ^L_{0i}.
\tag{1.46}
$$
Keep the odd parameters fixed,
$$
\theta_E^a=\theta_L^a,\qquad
\bar\eta^E_{\dot a}=\bar\eta^L_{\dot a},
\tag{1.47}
$$
and require
$$
\theta_E^aQ^E_a+\bar\eta^E_{\dot a}\bar Q_E^{\dot a}
=
-i\theta_L^aQ^L_a-i\bar\eta^L_{\dot a}\bar Q_L^{\dot a}.
\tag{1.48}
$$
Therefore
$$
Q^E_a=-iQ^L_a,\qquad
\bar Q_E^{\dot a}=-i\bar Q_L^{\dot a}.
\tag{1.49}
$$
The complete linear exponent matches exactly:
$$
\begin{aligned}
&\frac{i}{2}\omega^E_{mn}J_E^{mn}
+a_E^mP^E_m
+\theta_E^aQ^E_a
+\bar\eta^E_{\dot a}\bar Q_E^{\dot a}\\
&\qquad=
\frac{i}{2}\omega^L_{\mu\nu}J_L^{\mu\nu}
-i a_L^\mu P^L_\mu
-i\theta_L^aQ^L_a
-i\bar\eta^L_{\dot a}\bar Q_L^{\dot a}.
\end{aligned}
\tag{1.50}
$$
### 1.6 Euclidean sigma system and algebra
$$
(\sigma_E^m)_{a\dot a}
=
(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf1_2)_{a\dot a}.
\tag{1.51}
$$
$$
(\bar\sigma_E^m)^{\dot a a}
:=
\epsilon^{ab}\epsilon^{\dot a\dot b}
(\sigma_E^m)_{b\dot b}
=
(+i\sigma^1,+i\sigma^2,+i\sigma^3,\mathbf1_2)^{\dot a a}.
\tag{1.52}
$$
$$
\begin{aligned}
\sigma_E^4\bar\sigma_E^4+\sigma_E^4\bar\sigma_E^4
&=2\mathbf1_2,\\
\sigma_E^4\bar\sigma_E^i+\sigma_E^i\bar\sigma_E^4
&=i\sigma^i-i\sigma^i=0,\\
\sigma_E^i\bar\sigma_E^j+\sigma_E^j\bar\sigma_E^i
&=(-i)(i)(\sigma^i\sigma^j+\sigma^j\sigma^i)
=2\delta^{ij}\mathbf1_2.
\end{aligned}
\tag{1.53}
$$
Thus
$$
(\sigma_E^m)_{a\dot a}(\bar\sigma_E^n)^{\dot a b}
+
(\sigma_E^n)_{a\dot a}(\bar\sigma_E^m)^{\dot a b}
=
2\delta^{mn}\delta_a{}^b .
\tag{1.54}
$$
$$
(\sigma_E^{mn})_a{}^b
:=
\frac14
\left[
(\sigma_E^m)_{a\dot c}(\bar\sigma_E^n)^{\dot c b}
-
(\sigma_E^n)_{a\dot c}(\bar\sigma_E^m)^{\dot c b}
\right],
\tag{1.55}
$$
$$
(\bar\sigma_E^{mn})^{\dot a}{}_{\dot b}
:=
\frac14
\left[
(\bar\sigma_E^m)^{\dot a c}(\sigma_E^n)_{c\dot b}
-
(\bar\sigma_E^n)^{\dot a c}(\sigma_E^m)_{c\dot b}
\right].
\tag{1.56}
$$
$$
\begin{gathered}
\sigma_E^{ij}=\frac{i}{2}\epsilon^{ijk}\sigma^k=-\sigma_L^{ij},
\qquad
\sigma_E^{4i}=\frac{i}{2}\sigma^i=-i\sigma_L^{0i},\\
\bar\sigma_E^{ij}=\frac{i}{2}\epsilon^{ijk}\sigma^k=-\bar\sigma_L^{ij},
\qquad
\bar\sigma_E^{4i}=-\frac{i}{2}\sigma^i=-i\bar\sigma_L^{0i}.
\end{gathered}
\tag{1.57}
$$
$$
\left.U_E\right|_{\mathrm{linear}}
:=
1+\frac{i}{2}\omega^E_{mn}J_E^{mn}
+a_E^mP^E_m
+\theta_E^aQ^E_a
+\bar\eta^E_{\dot a}\bar Q_E^{\dot a}.
\tag{1.58}
$$
$$
x_E^{\prime m}
=
x_E^m+a_E^m+\omega_E^m{}_n x_E^n .
\tag{1.59}
$$
$$
[P^E_m,P^E_n]=0,
\tag{1.60}
$$
$$
[J^E_{mn},P^E_r]
=
i\delta_{mr}P^E_n-i\delta_{nr}P^E_m,
\tag{1.61}
$$
$$
\begin{aligned}
[J^E_{mn},J^E_{rs}]
=i\big(
&\delta_{mr}J^E_{ns}
-\delta_{nr}J^E_{ms}\\
&-\delta_{ms}J^E_{nr}
+\delta_{ns}J^E_{mr}
\big).
\end{aligned}
\tag{1.62}
$$
The continued spinor action is
$$
[J_E^{mn},Q^E_a]
=
+i(\sigma_E^{mn})_a{}^bQ^E_b,
\tag{1.63}
$$
$$
[J_E^{mn},\bar Q_E^{\dot a}]
=
+i(\bar\sigma_E^{mn})^{\dot a}{}_{\dot b}\bar Q_E^{\dot b}.
\tag{1.64}
$$
Spatial check:
$$
\begin{aligned}
[J_E^{ij},Q_E]
&=
[J_L^{ij},-iQ_L]\\
&=
-i[-i\sigma_L^{ij}Q_L]\\
&=
-i\sigma_L^{ij}Q_E\\
&=
+i\sigma_E^{ij}Q_E .
\end{aligned}
\tag{1.65}
$$
Mixed check:
$$
\begin{aligned}
[J_E^{4i},Q_E]
&=
[iJ_L^{0i},-iQ_L]\\
&=
[J_L^{0i},Q_L]\\
&=
-i\sigma_L^{0i}Q_L\\
&=
\sigma_L^{0i}Q_E\\
&=
+i\sigma_E^{4i}Q_E .
\end{aligned}
\tag{1.66}
$$
Finally,
$$
\begin{aligned}
\{Q^E_a,\bar Q^E_{\dot b}\}
&=
(-i)^2\{Q^L_a,\bar Q^L_{\dot b}\}\\
&=
2(\sigma_L^\mu)_{a\dot b}P^L_\mu\\
&=
2\left[
-\mathbf1_{a\dot b}P^E_4
+i(\sigma^i)_{a\dot b}P^E_i
\right]\\
&=
-2(\sigma_E^m)_{a\dot b}P^E_m .
\end{aligned}
\tag{1.67}
$$
$$
\boxed{
\begin{aligned}
\{Q^E_a,\bar Q^E_{\dot b}\}
&=-2(\sigma_E^m)_{a\dot b}P^E_m,\\
\{Q^E_a,Q^E_b\}&=0,\\
\{\bar Q^E_{\dot a},\bar Q^E_{\dot b}\}&=0,\\
[P^E_m,Q^E_a]&=0,\\
[P^E_m,\bar Q_E^{\dot a}]&=0 .
\end{aligned}}
\tag{1.68}
$$
Euclidean \(Q_E\) and \(\bar Q_E\) are independent; no Euclidean dagger relation is imposed.
