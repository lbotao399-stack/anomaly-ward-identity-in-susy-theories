# 00 3+1d SUSY QFT — Convention Lock

## Step 4B. Pure \(\mathcal N=2\) super Yang--Mills

For Lorentzian formulas only,

$$
(\widetilde\phi,\widetilde\psi,\widetilde F,
\widetilde\lambda)_L
:=(\bar\phi,\bar\psi,\bar F,\bar\lambda)_L.
\tag{4B.0}
$$

All tilded Euclidean fields remain independent.

### 4B.1 \(\mathcal N=1\) superspace action and relative metric

Let \(q_{AB}=q_{BA}\) be the undetermined adjoint-chiral metric:

$$
\begin{aligned}
S_L^{(2)}[q]=\int d^4x_L\Big\{&
[q_{AB}\widetilde\Phi^A
(\mathcal E_{\rm ad})^B{}_C\Phi^C]_D\\
&+\frac14[f_{AB}\mathcal W_L^{Aa}\mathcal W^B_{La}]_F
+\frac14[\bar f_{AB}\widetilde{\mathcal W}_{L\dot a}^{A}
\widetilde{\mathcal W}_L^{B\dot a}]_{\widetilde F}
\Big\}.
\end{aligned}
\tag{4B.1}
$$

Set \(c_{AB}{}^C=0\), \(\mathcal E_{\rm ad}=1\), and replace every
\(\mathcal D_\mu\) by \(\partial_\mu\).  Only in this linear Abelian
coefficient problem define

$$
\delta_2^{\rm lin}\Phi=C\eta^a\mathcal W_a,
\tag{4B.2}
$$

$$
\boxed{
\delta_2^{\rm lin}\mathcal W_a
=A\eta_a\bar D^2\widetilde\Phi
+B(\sigma_L^\mu)_{a\dot b}\bar\eta^{\dot b}
\partial_\mu\Phi.}
\tag{4B.3}
$$

Indeed,

$$
\bar D_{\dot a}\bar D^2\widetilde\Phi=0,
\qquad
\bar D_{\dot a}\partial_\mu\Phi=0,
\tag{4B.3a}
$$

so both terms in (4B.3) are chiral.  No symbol
\(\widetilde\Phi_{\rm ch}\) is introduced.  Equation (4B.3) is not a
non-Abelian transformation law; the covariant Wess--Zumino-gauge lift
is reconstructed in Section 4B.8.

Since \(\mathcal W_a|=-i\lambda_a\), scalar normalization gives

$$
-iC=-\sqrt2,
\qquad
C=-i\sqrt2.
\tag{4B.4}
$$

The lowest slots of (4B.2)--(4B.3) are

$$
\begin{aligned}
\delta_2^{\rm lin}\phi&=-iC\,\eta\lambda,\\
\left.\delta_2^{\rm lin}\lambda_a\right|_{\bar\eta}
&=iB(\sigma_L^\mu)_{a\dot b}\bar\eta^{\dot b}
\partial_\mu\phi,\\
\left.\delta_2^{\rm lin}\lambda_a\right|_{\eta\widetilde F}
&=-4iA\eta_a\widetilde F,\\
\left.\delta_2^{\rm lin}F\right|_{\eta}
&=-C\eta\sigma_L^\mu\partial_\mu\bar\lambda.
\end{aligned}
\tag{4B.4a}
$$

For two parameter sets, the \(\eta_1\sigma^\mu\bar\eta_2\)
coefficient in the scalar commutator is

$$
[\delta_1^{\rm lin},\delta_2^{\rm lin}]\phi
=-CB(\eta_1\sigma_L^\mu\bar\eta_2
-\eta_2\sigma_L^\mu\bar\eta_1)\partial_\mu\phi.
\tag{4B.4b}
$$

Matching \(v_L^\mu=2i(\eta_1\sigma_L^\mu\bar\eta_2-
\eta_2\sigma_L^\mu\bar\eta_1)\) gives \(CB=-2i\).

For the constant \(\bar\eta\) variation, retain the ordered monomial

$$
\mathfrak m_{\bar\eta}^{AB}
:=(\partial_\mu\bar\lambda^A)\bar\eta\,
\partial^\mu\phi^B.
\tag{4B.4c}
$$

The scalar and gaugino kinetic terms give

$$
\begin{aligned}
\delta_{\bar\eta}
[-q_{AB}(\partial_\mu\widetilde\phi^A)
(\partial^\mu\phi^B)]
&=+\sqrt2q_{AB}\mathfrak m_{\bar\eta}^{AB},\\
\delta_{\bar\eta}
[if^{({\rm R})}_{AB}\bar\lambda^A\bar\sigma_L^\mu
\partial_\mu\lambda^B]
&=-Bf^{({\rm R})}_{AB}\mathfrak m_{\bar\eta}^{AB}
+\partial_\mu(\cdots).
\end{aligned}
\tag{4B.4d}
$$

Here the symmetric second-derivative term was expanded with

$$
\bar\sigma_L^{(\mu}\sigma_L^{\nu)}=-\eta^{\mu\nu}\mathbf1_2
\tag{4B.4e}
$$

before one integration by parts.  Hence
\(f^{({\rm R})}_{AB}B=\sqrt2q_{AB}\).

Finally retain

$$
\mathfrak m_{\eta F}^{AB}
:=\widetilde F^B\eta\sigma_L^\mu
\partial_\mu\bar\lambda^A.
\tag{4B.4f}
$$

The auxiliary and gaugino kinetic terms give

$$
\begin{aligned}
\delta_\eta[q_{AB}\widetilde F^AF^B]
&=-Cq_{BA}\mathfrak m_{\eta F}^{AB}
=-Cq_{AB}\mathfrak m_{\eta F}^{AB},\\
\delta_\eta[if^{({\rm R})}_{AB}
\bar\lambda^A\bar\sigma_L^\mu\partial_\mu\lambda^B]
&=+4Af^{({\rm R})}_{AB}\mathfrak m_{\eta F}^{AB}
+\partial_\mu(\cdots).
\end{aligned}
\tag{4B.4g}
$$

Here \(q_{AB}=q_{BA}\) was used only in the second equality of the
first line of (4B.4g).  The ordered monomials
\(\mathfrak m_{\bar\eta}^{AB}\) and
\(\mathfrak m_{\eta F}^{AB}\) are independent for each ordered pair
\((A,B)\).  Their coefficient equations, together with scalar
closure, are therefore

$$
CB=-2i,
\qquad
f^{({\rm R})}_{AB}B=\sqrt2q_{AB},
\qquad
4f^{({\rm R})}_{AB}A=Cq_{AB},
\tag{4B.5}
$$

where \(f^{({\rm R})}_{AB}:=\operatorname{Re}f_{AB}\).  Substitution
of (4B.4) into (4B.5) gives

$$
\boxed{
B=\sqrt2,
\qquad
A=-\frac{i}{2\sqrt2},
\qquad
q_{AB}=f^{({\rm R})}_{AB}=h\kappa_{AB}.}
\tag{4B.6}
$$

Thus

$$
\boxed{
\begin{aligned}
S_L^{(2)}=\int d^4x_L\Big\{&
h\kappa_{AB}
[\widetilde\Phi^A(\mathcal E_{\rm ad})^B{}_C\Phi^C]_D\\
&+\frac14[f_{AB}\mathcal W_L^{Aa}\mathcal W^B_{La}]_F
+\frac14[\bar f_{AB}\widetilde{\mathcal W}_{L\dot a}^{A}
\widetilde{\mathcal W}_L^{B\dot a}]_{\widetilde F}
\Big\}.
\end{aligned}}
\tag{4B.7}
$$

Direct Euclidean projectors give

$$
\boxed{
\begin{aligned}
S_E^{(2)}=-\int d^4x_E\Big\{&
h\kappa_{AB}
[\widetilde\Phi^A(\mathcal E_{\rm ad})^B{}_C\Phi^C]_D\\
&+\frac14[f_{AB}\mathcal W_E^{Aa}\mathcal W^B_{Ea}]_F
+\frac14[\widetilde f_{AB}\widetilde{\mathcal W}_{E\dot a}^{A}
\widetilde{\mathcal W}_E^{B\dot a}]_{\widetilde F}
\Big\}.
\end{aligned}}
\tag{4B.8}
$$

### 4B.2 Direct Lorentzian component projection

Define

$$
\mu^A:=i(\phi\times\widetilde\phi)^A,
\qquad
H^A:=\mathscr D^A+\mu^A.
\tag{4B.9}
$$

Direct specialization of Step-3B gives

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm off}}^{(2)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-(\mathcal D_\mu\widetilde\phi^A)
(\mathcal D^\mu\phi^B)\\
&\quad
+i\bar\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B
+i\widetilde\psi^A\bar\sigma_L^\mu\mathcal D_\mu\psi^B
+\widetilde F^AF^B\\
&\quad
+\frac12\mathscr D^A\mathscr D^B
+\mathscr D^A\mu^B
\Big]\\
&-\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C
+\sqrt2h c_{ACD}\widetilde\psi^D\bar\lambda^A\phi^C\\
&-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F_{\mu\nu}^AF_{\rho\sigma}^B.
\end{aligned}}
\tag{4B.10}
$$

The auxiliary terms obey

$$
\begin{aligned}
\widetilde F^AF^B
+\frac12\mathscr D^A\mathscr D^B
+\mathscr D^A\mu^B
={}&\widetilde F^AF^B
+\frac12H^AH^B
-\frac12\mu^A\mu^B.
\end{aligned}
\tag{4B.11}
$$

With the three Step-4 auxiliary slots,

$$
Y_{11}=-\sqrt2F,
\qquad
Y_{22}=-\sqrt2\widetilde F,
\qquad
Y_{12}=Y_{21}=iH,
\tag{4B.12}
$$

one has, by explicit index raising,

$$
\begin{aligned}
\frac14Y^{Aij}Y_{ij}^B
&=\frac14\left(
Y_{22}^AY_{11}^B+Y_{11}^AY_{22}^B
-2Y_{12}^AY_{12}^B\right)\\
&=\widetilde F^AF^B+\frac12H^AH^B.
\end{aligned}
\tag{4B.13}
$$

Hence

$$
\boxed{
\mathcal L_{L,{\rm aux}}^{(2)}
=\frac h4\kappa_{AB}Y^{Aij}Y_{ij}^B
-\frac h2\kappa_{AB}\mu^A\mu^B.}
\tag{4B.14}
$$

The equations of motion are

$$
F=\widetilde F=0,
\qquad
H=0,
\qquad
\mathscr D=-\mu.
\tag{4B.15}
$$

### 4B.3 Direct Euclidean component projection

Define the intrinsic Euclidean moment map

$$
\mu_E^A:=i(\phi\times\widetilde\phi)^A,
\qquad
H_E:=\mathscr D+\mu_E.
\tag{4B.16}
$$

Direct Step-3A multiplication gives

$$
\boxed{
\begin{aligned}
\mathcal L_{E,{\rm off}}^{(2)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+(\mathcal D_m\widetilde\phi^A)(\mathcal D_m\phi^B)\\
&\quad
+\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B
+\widetilde\psi^A\bar\sigma_E^m\mathcal D_m\psi^B
-\widetilde F^AF^B\\
&\quad
-\frac12\mathscr D^A\mathscr D^B
-\mathscr D^A\mu_E^B
\Big]\\
&+\sqrt2h c_{ACD}\widetilde\phi^D\lambda^A\psi^C
-\sqrt2h c_{ACD}\widetilde\psi^D\widetilde\lambda^A\phi^C\\
&-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F_{mn}^AF_{rs}^B.
\end{aligned}}
\tag{4B.17}
$$

Therefore

$$
\boxed{
\mathcal L_{E,{\rm aux}}^{(2)}
=-\frac h4\kappa_{AB}Y_E^{Aij}Y_{E,ij}^B
+\frac h2\kappa_{AB}\mu_E^A\mu_E^B.}
\tag{4B.18}
$$

Equations (4B.17)--(4B.18) agree termwise with

$$
\mathcal L_E=-\mathcal L_L|_{\rm Wick}.
\tag{4B.19}
$$

### 4B.4 Manifest and hidden low-component transformations

The manifest \(\delta_1(\varepsilon,\bar\varepsilon)\) vector rules are
Step 4A.  Its adjoint-chiral low slots are

$$
\boxed{
\begin{aligned}
\delta_1\phi&=-\sqrt2\varepsilon\psi,\\
\delta_1\psi_a&=-\sqrt2\varepsilon_aF
+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\bar\varepsilon^{\dot b}\mathcal D_\mu\phi.
\end{aligned}}
\tag{4B.20}
$$

The top slots obtained from the same compensated chiral expansion are

$$
\boxed{
\begin{aligned}
\delta_1F
&=+i\sqrt2\bar\varepsilon\bar\sigma_L^\mu
\mathcal D_\mu\psi
-2i\llbracket\bar\varepsilon\bar\lambda,\phi\rrbracket,\\
\delta_1\widetilde F
&=+i\sqrt2\varepsilon\sigma_L^\mu
\mathcal D_\mu\widetilde\psi
-2i\llbracket\varepsilon\lambda,\widetilde\phi\rrbracket.
\end{aligned}}
\tag{4B.20a}
$$

Lorentzian conjugation supplies the remaining manifest chiral slots:

$$
\boxed{
\begin{aligned}
\delta_1\widetilde\phi
&=-\sqrt2\bar\varepsilon\widetilde\psi,\\
\delta_1\widetilde\psi_{\dot a}
&=-\sqrt2\bar\varepsilon_{\dot a}\widetilde F
-i\sqrt2\varepsilon^a(\sigma_L^\mu)_{a\dot a}
\mathcal D_\mu\widetilde\phi,\\
\delta_1\mu
&=-\sqrt2\llbracket\varepsilon\psi,\widetilde\phi\rrbracket
-\sqrt2\llbracket\phi,
\bar\varepsilon\widetilde\psi\rrbracket,\\
\delta_1H
&=-\varepsilon\sigma_L^\mu\mathcal D_\mu\bar\lambda
+\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\lambda
+\delta_1\mu.
\end{aligned}}
\tag{4B.20b}
$$

The corrected ordered hidden low slots following from (4B.2)--(4B.3)
are

$$
\boxed{
\begin{aligned}
\delta_2\phi&=-\sqrt2\eta\lambda,\\
\delta_2\lambda_a
&=-\sqrt2\eta_a\widetilde F
+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\bar\eta^{\dot b}\mathcal D_\mu\phi,\\
\delta_2\psi_a
&=-(\sigma_L^{\mu\nu})_a{}^b\eta_bF_{\mu\nu}
-i\eta_a\mathscr D-2i\eta_a\mu,\\
\delta_2A_\mu
&=+i\eta\sigma_{L,\mu}\widetilde\psi
+i\bar\eta\bar\sigma_{L,\mu}\psi.
\end{aligned}}
\tag{4B.21}
$$

The remaining hidden rules, fixed by direct bridge expansion and
action cancellation, are

$$
\boxed{
\begin{aligned}
\delta_2F
&=i\sqrt2\eta\sigma_L^\mu\mathcal D_\mu\bar\lambda
+2i\llbracket\eta\psi,\widetilde\phi\rrbracket,\\
\delta_2\widetilde F
&=+i\sqrt2\bar\eta\bar\sigma_L^\mu\mathcal D_\mu\lambda
+2i\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta_2\mathscr D
&=-\eta\sigma_L^\mu\mathcal D_\mu\widetilde\psi
+\bar\eta\bar\sigma_L^\mu\mathcal D_\mu\psi\\
&\quad+2\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
+2\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket.
\end{aligned}}
\tag{4B.21a}
$$

The shift (4B.9) removes the two commutator terms:

$$
\delta_2\mu
=-\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
-\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket,
\tag{4B.21b}
$$

$$
\boxed{
\delta_2H
=-\eta\sigma_L^\mu\mathcal D_\mu\widetilde\psi
+\bar\eta\bar\sigma_L^\mu\mathcal D_\mu\psi
+\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
+\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket.}
\tag{4B.21c}
$$

The sign in the third line follows from

$$
D_a(\eta^b\mathcal W_b)
=-\eta^bD_a\mathcal W_b,
\qquad
\eta^b\epsilon_{ba}=-\eta_a.
\tag{4B.22}
$$

The vector phase is fixed independently.  The free part of the
antichiral projector is

$$
\left.\bar D^2\widetilde\Phi\right|_{\vartheta^0+\vartheta^1}
=-4\widetilde F
+4i\sqrt2\vartheta\sigma_L^\mu
\mathcal D_\mu\widetilde\psi.
\tag{4B.22a}
$$

Put \(\delta_2A_\mu=f_A\eta\sigma_{L,\mu}
\widetilde\psi+\cdots\).  The symmetric spinor part of the
\(\vartheta\)-coefficient of (4B.3) is

$$
\left[i(\sigma_L^{\mu\nu})_a{}^b\epsilon_{bc}
\delta_2F_{\mu\nu}\right]_{(ac)}
=-2\eta_{(a}(\sigma_L^\rho)_{c)\dot b}
\mathcal D_\rho\widetilde\psi^{\dot b}.
\tag{4B.22b}
$$

Substitution of

$$
\delta_2F_{\mu\nu}
=f_A\eta\left[
\sigma_{L,\nu}\mathcal D_\mu\widetilde\psi
-\sigma_{L,\mu}\mathcal D_\nu\widetilde\psi\right]
\tag{4B.22c}
$$

and the Step-1 matrices gives

$$
\boxed{f_A=+i.}
\tag{4B.22d}
$$

Lorentzian conjugation fixes the coefficient \(+i\) of
\(\bar\eta\bar\sigma_{L,\mu}\psi\) in (4B.21).

### 4B.5 Non-Abelian compensator and all conjugate slots

The chiral Wess--Zumino compensator required by (4B.21) is

$$
\boxed{
\Lambda_{2,L}^{\rm comp}(y_L,\vartheta)
=2\sqrt2\vartheta^a\eta_a\widetilde\phi(y_L).}
\tag{4B.23}
$$

For

$$
\delta_g\Phi=i\llbracket\Lambda^{\rm comp},\Phi\rrbracket,
\qquad
\delta_g\mathcal W_a
=i\llbracket\Lambda^{\rm comp},\mathcal W_a\rrbracket,
\tag{4B.24}
$$

its nonzero required projections are

$$
\boxed{
\begin{aligned}
\delta_g\psi_a&=-2i\eta_a\mu,\\
\delta_gF&=+2i\llbracket\eta\psi,\widetilde\phi\rrbracket,\\
\left.\delta_g\mathscr D\right|_\eta
&=+\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket.
\end{aligned}}
\tag{4B.25}
$$

Adding the conjugate compensator gives

$$
\boxed{
\begin{aligned}
\delta_2\widetilde\phi&=-\sqrt2\bar\eta\widetilde\lambda,\\
\delta_2\widetilde\lambda_{\dot a}
&=-\sqrt2\bar\eta_{\dot a}F
-i\sqrt2\eta^a(\sigma_L^\mu)_{a\dot a}
\mathcal D_\mu\widetilde\phi,\\
\delta_2\widetilde\psi_{\dot a}
&=+\bar\eta_{\dot b}(\bar\sigma_L^{\mu\nu})^{\dot b}{}_{\dot a}
F_{\mu\nu}+i\bar\eta_{\dot a}\mathscr D
+2i\bar\eta_{\dot a}\mu.
\end{aligned}}
\tag{4B.26}
$$

Equations (4B.21), (4B.21a), and (4B.26) contain all Lorentzian
component slots.

### 4B.6 Off-shell \(SU(2)_R\) doublet/triplet coefficient lock

Define the component arrays

$$
\chi_{1a}:=\psi_a,
\qquad
\chi_{2a}:=-\lambda_a,
\qquad
\zeta^1:=\varepsilon,
\qquad
\zeta^2:=-\eta,
\tag{4B.27}
$$

$$
\bar\chi^1:=\widetilde\psi,
\qquad
\bar\chi^2:=-\widetilde\lambda,
\qquad
\bar\zeta_1:=\bar\varepsilon,
\qquad
\bar\zeta_2:=-\bar\eta.
\tag{4B.28}
$$

Then (4B.20)--(4B.21) give

$$
\delta\phi=-\sqrt2\zeta^i\chi_i,
\tag{4B.29}
$$

$$
\delta A_\mu
=-i\varepsilon_{ij}\zeta^i\sigma_{L,\mu}\bar\chi^j
-i\varepsilon^{ij}\bar\zeta_j\bar\sigma_{L,\mu}\chi_i,
\tag{4B.30}
$$

and the three auxiliary slots have the complete transformations

$$
\boxed{
\begin{aligned}
\delta Y_{11}={}&
-2i\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\psi
-2i\eta\sigma_L^\mu\mathcal D_\mu\bar\lambda\\
&+2i\sqrt2\llbracket\bar\varepsilon\bar\lambda,\phi\rrbracket
-2i\sqrt2\llbracket\eta\psi,\widetilde\phi\rrbracket,\\
\delta Y_{22}={}&
-2i\varepsilon\sigma_L^\mu\mathcal D_\mu\widetilde\psi
-2i\bar\eta\bar\sigma_L^\mu\mathcal D_\mu\lambda\\
&+2i\sqrt2\llbracket\varepsilon\lambda,\widetilde\phi\rrbracket
-2i\sqrt2\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta Y_{12}={}&
-i\varepsilon\sigma_L^\mu\mathcal D_\mu\bar\lambda
+i\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\lambda\\
&-i\eta\sigma_L^\mu\mathcal D_\mu\widetilde\psi
+i\bar\eta\bar\sigma_L^\mu\mathcal D_\mu\psi\\
&-i\sqrt2\llbracket\varepsilon\psi,\widetilde\phi\rrbracket
-i\sqrt2\llbracket\phi,\bar\varepsilon\widetilde\psi\rrbracket\\
&+i\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
+i\sqrt2\llbracket\phi,\bar\eta\bar\lambda\rrbracket.
\end{aligned}}
\tag{4B.31}
$$

Equivalently,

$$
\delta Y_{11}=-\sqrt2\delta F,
\qquad
\delta Y_{22}=-\sqrt2\delta\widetilde F,
\qquad
\delta Y_{12}=i(\delta\mathscr D+\delta\mu).
\tag{4B.32}
$$

The following coefficients exist only inside this packaging audit:

$$
\begin{aligned}
\chi_1&=\psi,
&\chi_2&=\rho_\chi\lambda,
&\zeta^1&=\varepsilon,
&\zeta^2&=\rho_\chi^{-1}\eta,\\
Y_{11}&=u_FF,
&Y_{22}&=u_{\widetilde F}\widetilde F,
&Y_{12}&=Y_{21}=u_HH,
\end{aligned}
\qquad
\rho_\chi u_Fu_{\widetilde F}u_H\ne0.
\tag{4B.33}
$$

The local symbols \(u_F,u_{\widetilde F},u_H,\rho_\chi\) are packaging
coefficients; they are not spinor, gauge, or \(SU(3)\) indices.  The tensor
auxiliary term in \(\delta\chi_i\) is

$$
\left.\delta\chi_i\right|_{Y,\mu}
=\gamma Y_{ij}\zeta^j
+\beta\mu\varepsilon_{ij}\zeta^j.
\tag{4B.33L1}
$$

The \(F\varepsilon\) and \(\mathscr D\varepsilon\) slots give

$$
\gamma u_F=-\sqrt2,
\qquad
\gamma u_H=-i\rho_\chi.
\tag{4B.33L2}
$$

In the global parameter-left order of (4.38a)--(4.38b), the derivative
law is

$$
\left.\delta Y_{ij}\right|_{\bar\zeta}
=\mathsf A_{\rm PL}\,
\bar\zeta_{(i}\bar\sigma_L^\mu\mathcal D_\mu\chi_{j)}.
\tag{4B.33L3}
$$

Its field-left rewriting is

$$
\left.\delta Y_{ij}\right|_{\bar\zeta}
=\mathsf A_{\rm FL}
(\mathcal D_\mu\chi_{(i})\sigma_L^\mu\bar\zeta_{j)},
\qquad
\mathsf A_{\rm FL}=-\mathsf A_{\rm PL}.
\tag{4B.33L4}
$$

The \(Y_{11}\) and \(Y_{12}\) slots give, without changing order,

$$
\begin{aligned}
\mathsf A_{\rm PL}&=i\sqrt2\,u_F,
&u_H&=\frac12\mathsf A_{\rm PL}\rho_\chi,\\
\mathsf A_{\rm FL}&=-i\sqrt2\,u_F,
&u_H&=-\frac12\mathsf A_{\rm FL}\rho_\chi.
\end{aligned}
\tag{4B.33L5}
$$

The hidden \(\widetilde F\eta\) slot and the manifest \(\mu\varepsilon\)
slot give

$$
\gamma u_{\widetilde F}=-\sqrt2\rho_\chi^2,
\qquad
\gamma u_H+\beta=0.
\tag{4B.33L5a}
$$

Consequently both derivative orders give the same coefficient:

$$
\begin{aligned}
\gamma u_H
&=\frac12(\gamma u_F)i\sqrt2\,\rho_\chi\\
&=\frac12(-\sqrt2)i\sqrt2\,\rho_\chi\\
&=-i\rho_\chi.
\end{aligned}
\tag{4B.33L6}
$$

Solving (4B.33L2), (4B.33L5), and (4B.33L5a), with
\(\gamma\rho_\chi\ne0\), gives the candidate solution

$$
\begin{aligned}
u_F&=-\frac{\sqrt2}{\gamma},
&u_{\widetilde F}&=-\frac{\sqrt2\rho_\chi^2}{\gamma},
&u_H&=-\frac{i\rho_\chi}{\gamma},\\
\beta&=i\rho_\chi,
&\mathsf A_{\rm PL}&=-\frac{2i}{\gamma},
&\mathsf A_{\rm FL}&=+\frac{2i}{\gamma}.
\end{aligned}
\tag{4B.33L6a}
$$

The exact dual-order coefficient gate and the exact three-generator
\(SU(2)_R\) intertwiner gate support the canonical specialization

$$
\boxed{
(u_F,u_{\widetilde F},u_H,\rho_\chi,
\gamma,\beta,\mathsf A_{\rm PL},\mathsf A_{\rm FL})
=(-\sqrt2,-\sqrt2,i,-1,1,-i,-2i,+2i).}
\tag{4B.33L6b}
$$

Within the fields and transformation slots checked by those gates,

$$
\boxed{
\begin{aligned}
\delta\chi_{ia}={}&
-\varepsilon_{ij}(\sigma_L^{\mu\nu})_a{}^b
\zeta_b^jF_{\mu\nu}
+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\bar\zeta_i^{\dot b}\mathcal D_\mu\phi\\
&+Y_{ij}\zeta_a^j
-i\mu\varepsilon_{ij}\zeta_a^j.
\end{aligned}}
\tag{4B.33L6c}
$$

These finite verifier gates do not prove interacting closure for an arbitrary
Lie algebra.

Restricting the verifier-gated canonical package to the auxiliary surface
(4B.15),

$$
F=\widetilde F=H=0,
\qquad
\mathscr D=-\mu,
\tag{4B.33L7a}
$$

direct substitution in (4B.20)--(4B.26) gives the physical-field rule

$$
\boxed{
\begin{aligned}
\delta_{\rm on}\phi&=-\sqrt2\zeta^i\chi_i,\\
\delta_{\rm on}A_\mu
&=-i\varepsilon_{ij}\zeta^i\sigma_{L,\mu}\bar\chi^j
-i\varepsilon^{ij}\bar\zeta_j\bar\sigma_{L,\mu}\chi_i,\\
\delta_{\rm on}\chi_{ia}
&=-\varepsilon_{ij}(\sigma_L^{\mu\nu})_a{}^b
\zeta_b^jF_{\mu\nu}
+i\sqrt2(\sigma_L^\mu)_{a\dot b}
\bar\zeta_i^{\dot b}\mathcal D_\mu\phi
-i\mu\varepsilon_{ij}\zeta_a^j.
\end{aligned}}
\tag{4B.33L7b}
$$

For \(i=1\), its \(\zeta^2=-\eta\) slot is
\(-\sigma_L^{\mu\nu}\eta F_{\mu\nu}-i\eta\mu\); for \(i=2\),
its \(\zeta^1=\varepsilon\) slot is the negative of
\(\sigma_L^{\mu\nu}\varepsilon F_{\mu\nu}+i\varepsilon\mu\).
These are the auxiliary-eliminated \(\psi\) and \(-\lambda\) slots.
Equation (4B.33L7b) is the restriction of (4B.33L6c) within the exact
intertwiner-gate scope.  Neither this restriction nor the finite gate proves
interacting closure for an arbitrary Lie algebra.

The density still has the algebraic slot identity

$$
\boxed{
\begin{aligned}
\mathcal L_{L,{\rm off}}^{(2)}
=h\operatorname{tr}_\kappa\Big[&
-\frac14F_{\mu\nu}F^{\mu\nu}
-\mathcal D_\mu\widetilde\phi\mathcal D^\mu\phi
+i\bar\chi^i\bar\sigma_L^\mu\mathcal D_\mu\chi_i\\
&+\frac14Y^{ij}Y_{ij}-\frac12\mu^2
-\frac1{\sqrt2}\widetilde\phi\,
\varepsilon^{ij}(\chi_i\times\chi_j)
+\frac1{\sqrt2}\phi\,
\varepsilon_{ij}(\bar\chi^i\times\bar\chi^j)
\Big],
\end{aligned}}
\tag{4B.33L8}
$$

because

$$
\varepsilon^{ij}(\chi_i\times\chi_j)=2(\lambda\times\psi),
\qquad
\varepsilon_{ij}(\bar\chi^i\times\bar\chi^j)
=2(\widetilde\psi\times\bar\lambda).
\tag{4B.33L9}
$$

Contracted indices alone do not prove covariance.  The exact verifier gate
uses

$$
\tau_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\tau_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\qquad
\tau_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
t_A=\frac i2\tau_A.
\tag{4B.33L9a}
$$

Write \(R_A^{\rm par}\) and \(R_A^{\rm fields}\) for the parameter and
field representations induced by \(t_A\), and
\(\Pi:=(\zeta,\bar\zeta)\).  For each \(A=1,2,3\), the gate checks

$$
R_A^{\rm fields}\!\left[\delta_\Pi X\right]
-\delta_\Pi\!\left[R_A^{\rm fields}X\right]
-\delta_{R_A^{\rm par}\Pi}X=0,
\qquad A=1,2,3,
\tag{4B.33L10}
$$

on every component slot represented by the verifier and returns zero
intertwiner residual for the canonical tuple (4B.33L6b).  This finite
representation check is not a general non-Abelian closure theorem.

### 4B.7 Euclidean component rules

The three Euclidean auxiliary slots are

$$
\widetilde\chi^1:=\widetilde\psi,
\qquad
\widetilde\chi^2:=-\widetilde\lambda,
\qquad
Y_{E,11}:=-\sqrt2F,
\qquad
Y_{E,22}:=-\sqrt2\widetilde F,
\qquad
Y_{E,12}=Y_{E,21}:=iH_E.
\tag{4B.33a}
$$

The complete Euclidean manifest chiral rules are

$$
\boxed{
\begin{aligned}
\delta_{1,E}\phi&=-\sqrt2\varepsilon\psi,
&\delta_{1,E}\widetilde\phi
&=-\sqrt2\bar\varepsilon\widetilde\psi,\\
\delta_{1,E}\psi_a
&=-\sqrt2\varepsilon_aF
-\sqrt2(\sigma_E^m)_{a\dot b}\bar\varepsilon^{\dot b}
\mathcal D_m\phi,
&\delta_{1,E}\widetilde\psi_{\dot a}
&=-\sqrt2\bar\varepsilon_{\dot a}\widetilde F
+\sqrt2\varepsilon^a(\sigma_E^m)_{a\dot a}
\mathcal D_m\widetilde\phi,\\
\delta_{1,E}F
&=+\sqrt2\bar\varepsilon\bar\sigma_E^m\mathcal D_m\psi
-2i\llbracket\bar\varepsilon\widetilde\lambda,\phi\rrbracket,
&\delta_{1,E}\widetilde F
&=-\sqrt2\varepsilon\sigma_E^m\mathcal D_m\widetilde\psi
-2i\llbracket\varepsilon\lambda,\widetilde\phi\rrbracket.
\end{aligned}}
\tag{4B.33b}
$$

The independent Euclidean hidden rules are

$$
\boxed{
\begin{aligned}
\delta_{2,E}\phi&=-\sqrt2\eta\lambda,\\
\delta_{2,E}\widetilde\phi&=-\sqrt2\bar\eta\widetilde\lambda,\\
\delta_{2,E}A_m
&=-\eta\sigma_{E,m}\widetilde\psi
-\bar\eta\bar\sigma_{E,m}\psi,\\
\delta_{2,E}\lambda_a
&=-\sqrt2\eta_a\widetilde F
-\sqrt2(\sigma_E^m)_{a\dot b}\bar\eta^{\dot b}
\mathcal D_m\phi,\\
\delta_{2,E}\widetilde\lambda_{\dot a}
&=-\sqrt2\bar\eta_{\dot a}F
+\sqrt2\eta^a(\sigma_E^m)_{a\dot a}
\mathcal D_m\widetilde\phi,\\
\delta_{2,E}\psi_a
&=+(\sigma_E^{mn})_a{}^b\eta_bF_{mn}
-i\eta_a\mathscr D-2i\eta_a\mu_E,\\
\delta_{2,E}\widetilde\psi_{\dot a}
&=-\bar\eta_{\dot b}(\bar\sigma_E^{mn})^{\dot b}{}_{\dot a}
F_{mn}+i\bar\eta_{\dot a}\mathscr D
+2i\bar\eta_{\dot a}\mu_E.
\end{aligned}}
\tag{4B.34}
$$

$$
\boxed{
\begin{aligned}
\delta_{2,E}F
&=-\sqrt2\eta\sigma_E^m\mathcal D_m\widetilde\lambda
+2i\llbracket\eta\psi,\widetilde\phi\rrbracket,\\
\delta_{2,E}\widetilde F
&=-\sqrt2\bar\eta\bar\sigma_E^m\mathcal D_m\lambda
+2i\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta_{2,E}\mathscr D
&=-i\eta\sigma_E^m\mathcal D_m\widetilde\psi
+i\bar\eta\bar\sigma_E^m\mathcal D_m\psi\\
&\quad+2\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
+2\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket.
\end{aligned}}
\tag{4B.35}
$$

The Euclidean moment-map, shifted-auxiliary, and three slot rules are

$$
\boxed{
\begin{aligned}
\delta_{1,E}\mu_E
&=-\sqrt2\llbracket\varepsilon\psi,\widetilde\phi\rrbracket
-\sqrt2\llbracket\phi,\bar\varepsilon\widetilde\psi\rrbracket,\\
\delta_{1,E}H_E
&=-i\varepsilon\sigma_E^m\mathcal D_m\widetilde\lambda
+i\bar\varepsilon\bar\sigma_E^m\mathcal D_m\lambda
+\delta_{1,E}\mu_E,\\
\delta_{2,E}\mu_E
&=-\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
-\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket,\\
\delta_{2,E}H_E
&=-i\eta\sigma_E^m\mathcal D_m\widetilde\psi
+i\bar\eta\bar\sigma_E^m\mathcal D_m\psi\\
&\quad+\sqrt2\llbracket\eta\lambda,\widetilde\phi\rrbracket
+\sqrt2\llbracket\phi,\bar\eta\widetilde\lambda\rrbracket,
\end{aligned}}
\tag{4B.35a}
$$

$$
\boxed{
\delta Y_{E,11}=-\sqrt2\delta F,
\qquad
\delta Y_{E,22}=-\sqrt2\delta\widetilde F,
\qquad
\delta Y_{E,12}=i(\delta\mathscr D+\delta\mu_E).}
\tag{4B.35b}
$$

The Euclidean off-shell triplet expression is

$$
\begin{aligned}
\delta_E\chi_{ia}:={}&
\varepsilon_{ij}(\sigma_E^{mn})_a{}^b\zeta_b^jF_{mn}
-\sqrt2(\sigma_E^m)_{a\dot b}\bar\zeta_i^{\dot b}
\mathcal D_m\phi\\
&+Y_{E,ij}\zeta_a^j
-i\mu_E\varepsilon_{ij}\zeta_a^j.
\end{aligned}
\tag{4B.35c}
$$

The exact Euclidean component-slot and three-generator intertwiner gates
support equality of (4B.35c) with the direct rules
(4B.33b)--(4B.35b) for the canonical tuple (4B.33L6b).  This checked
finite scope does not prove interacting closure for an arbitrary Lie algebra.

Direct Euclidean projection and the Wick image of (4B.21),
(4B.21a), and (4B.26) give the same component coefficients.

### 4B.8 Wess--Zumino-gauge superspace reconstruction

For either signature, define

$$
\mathscr C_R[c,\chi,f](y_R,\vartheta)
:=c(y_R)+\sqrt2\vartheta\chi(y_R)+\vartheta^2f(y_R).
\tag{4B.36}
$$

Then

$$
\boxed{
\delta\Phi_R
:=\mathscr C_R[\delta\phi,\delta\psi,\delta F],
\qquad
\delta\widetilde\Phi_R
:=\widetilde{\mathscr C}_R
[\delta\widetilde\phi,\delta\widetilde\psi,
\delta\widetilde F].}
\tag{4B.37}
$$

$$
\bar D_R\delta\Phi_R=0,
\qquad
D_R\delta\widetilde\Phi_R=0,
\tag{4B.38}
$$

and the Step-3B projections of (4B.37) return the three displayed
varied components exactly.

$$
\boxed{
\begin{aligned}
\delta\mathcal V_L^{\rm WZ}={}&
-2\vartheta\sigma_L^\mu\bar\vartheta\,\delta A_\mu
+2i\vartheta^2\bar\vartheta\,\delta\widetilde\lambda
-2i\bar\vartheta^2\vartheta\,\delta\lambda
+\vartheta^2\bar\vartheta^2\delta\mathscr D,\\
\delta\mathcal V_E^{\rm WZ}={}&
-2i\vartheta\sigma_E^m\bar\vartheta\,\delta A_m
+2i\vartheta^2\bar\vartheta\,\delta\widetilde\lambda
-2i\bar\vartheta^2\vartheta\,\delta\lambda
+\vartheta^2\bar\vartheta^2\delta\mathscr D.
\end{aligned}}
\tag{4B.39}
$$

For \(\Xi:=\mathcal E^{-1}\delta\mathcal E\),

$$
\Xi=\int_0^1ds\ e^{-s\mathcal V}
(\delta\mathcal V)e^{s\mathcal V},
\tag{4B.40}
$$

$$
\boxed{
\delta\mathcal W_a
=-\frac18\bar D^2
\left(D_a\Xi+[\Gamma_a,\Xi]\right),
\qquad
\bar D_{\dot a}\delta\mathcal W_b=0.}
\tag{4B.41}
$$

Equations (4B.36)--(4B.41) are the complete non-Abelian
Wess--Zumino-gauge component-reconstructed \(\mathcal N=1\)
superspace realization.

### 4B.9 Exact closure gates and general-law boundary

For two complete parameter sets \((\varepsilon_s,\eta_s)\), define

$$
\begin{aligned}
v_L^\mu:=2i\Big[&
\varepsilon_1\sigma_L^\mu\bar\varepsilon_2
-\varepsilon_2\sigma_L^\mu\bar\varepsilon_1\\
&+\eta_1\sigma_L^\mu\bar\eta_2
-\eta_2\sigma_L^\mu\bar\eta_1\Big],
\end{aligned}
\tag{4B.42}
$$

$$
\begin{aligned}
\Omega_{12}:=2\sqrt2\Big[&
(\varepsilon_1\eta_2-\varepsilon_2\eta_1)
\widetilde\phi\\
&+(\bar\varepsilon_1\bar\eta_2
-\bar\varepsilon_2\bar\eta_1)\phi\Big].
\end{aligned}
\tag{4B.43}
$$

The general closure law to be tested is

$$
\boxed{
\begin{aligned}
[\delta(\varepsilon_1,\eta_1),
\delta(\varepsilon_2,\eta_2)]A_\mu
&=v_L^\nu F_{\nu\mu}+\mathcal D_\mu\Omega_{12},\\
[\delta(\varepsilon_1,\eta_1),
\delta(\varepsilon_2,\eta_2)]X
&=v_L^\mu\mathcal D_\mu X
+i\llbracket\Omega_{12},X\rrbracket,
\end{aligned}}
\tag{4B.44}
$$

for

$$
X\in\{\phi,\widetilde\phi,\lambda,\widetilde\lambda,
\psi,\widetilde\psi,F,\widetilde F,\mathscr D,H,Y_{ij}\}.
\tag{4B.45}
$$

The exact verifier proves (4B.44) in the two sectors

$$
\begin{aligned}
\mathscr S_{\rm free}^{L,E}:&\quad
c_{AB}{}^C=0,
\quad p_M\ \hbox{arbitrary},
\quad X\ \hbox{as in (4B.45)},\\
\mathscr S_{\rm int}^{L}:&\quad
c_{AB}{}^C=\epsilon_{AB}{}^C,
\quad A_\mu=\partial_\mu X=0,\\
&\quad
\delta(\mathcal D_\mu X)
=(\delta A_\mu)\mathbin{\times}X\ \hbox{retained}.
\end{aligned}
\tag{4B.45a}
$$

No Euler operator is used in either checked sector.  In
ordinary-coordinate form, the candidate gauge parameter is

$$
\alpha_{12}=-v_L^\mu A_\mu+\Omega_{12}.
\tag{4B.46}
$$

The Euclidean closure parameters are

$$
\begin{aligned}
v_E^m:=-2\Big[&
\varepsilon_1\sigma_E^m\bar\varepsilon_2
-\varepsilon_2\sigma_E^m\bar\varepsilon_1\\
&+\eta_1\sigma_E^m\bar\eta_2
-\eta_2\sigma_E^m\bar\eta_1\Big],
\end{aligned}
\tag{4B.46a}
$$

$$
\Omega_{12,E}=2\sqrt2\Big[
(\varepsilon_1\eta_2-\varepsilon_2\eta_1)\widetilde\phi
+(\bar\varepsilon_1\bar\eta_2
-\bar\varepsilon_2\bar\eta_1)\phi\Big].
\tag{4B.46b}
$$

The Euclidean free all-field gate verifies the
(c_{AB}{}^C=0) specialization of

$$
\boxed{
\begin{aligned}
[\delta_E(\varepsilon_1,\eta_1),
\delta_E(\varepsilon_2,\eta_2)]A_m
&=v_E^nF_{nm}+\mathcal D_m\Omega_{12,E},\\
[\delta_E(\varepsilon_1,\eta_1),
\delta_E(\varepsilon_2,\eta_2)]X_E
&=v_E^m\mathcal D_mX_E
+i\llbracket\Omega_{12,E},X_E\rrbracket.
\end{aligned}}
\tag{4B.46c}
$$

Here \(X_E\) runs over the Euclidean version of every field in
(4B.45).

The finite \(SU(2)\)-color gate in (4B.45a) is a regression gate; by
itself it is not an arbitrary-Lie theorem.  The universal gate uses
\(\mathcal A_{\rm univ}^{R}\) of (4.43)--(4.50).  Define

$$
\Delta_R:=\delta_{R,1}\delta_{R,2}-\delta_{R,2}\delta_{R,1},
\tag{4B.46d}
$$

$$
\begin{aligned}
\mathsf T_R(A_M)&:=v_R^NF_{NM}+\mathcal D_M\Omega_{12,R},\\
\mathsf T_R(X)&:=v_R^M\mathcal D_MX
+i\llbracket\Omega_{12,R},X\rrbracket,\\
\mathscr R_R[Z]&:=
\operatorname{NF}_{\mathcal A_{\rm univ}^{R}}
\!\left(\Delta_RZ-\mathsf T_R(Z)\right),
\end{aligned}
\tag{4B.46e}
$$

$$
\Omega_{12,R}:=
\begin{cases}
\Omega_{12},&R=L,\\
\Omega_{12,E},&R=E.
\end{cases}
\tag{4B.46f}
$$

The directly expanded primitive bases are

$$
\begin{aligned}
\mathscr P_L:=(&A_0,A_1,A_2,A_3,
\phi,\widetilde\phi,
\lambda_1,\lambda_2,
\widetilde\lambda_{\dot1},\widetilde\lambda_{\dot2},\\
&\psi_1,\psi_2,
\widetilde\psi_{\dot1},\widetilde\psi_{\dot2},
F,\widetilde F,\mathscr D),\\
\mathscr P_E:=(&A_1,A_2,A_3,A_4,
\phi,\widetilde\phi,
\lambda_1,\lambda_2,
\widetilde\lambda_{\dot1},\widetilde\lambda_{\dot2},\\
&\psi_1,\psi_2,
\widetilde\psi_{\dot1},\widetilde\psi_{\dot2},
F,\widetilde F,\mathscr D).
\end{aligned}
\tag{4B.46g}
$$

The verifier's internal Euclidean vector labels obey

$$
\boxed{A_r^{\rm internal}=A_{E,r+1},\qquad r=0,1,2,3.}
\tag{4B.46g1}
$$

Direct double application of the Step-4A Lorentzian vector rules and
(4B.20)--(4B.26) gives

$$
\begin{aligned}
(&\mathscr R_L[A_0],\mathscr R_L[A_1],
\mathscr R_L[A_2],\mathscr R_L[A_3],
\mathscr R_L[\phi],\mathscr R_L[\widetilde\phi],\\
&\mathscr R_L[\lambda_1],\mathscr R_L[\lambda_2],
\mathscr R_L[\widetilde\lambda_{\dot1}],
\mathscr R_L[\widetilde\lambda_{\dot2}],\\
&\mathscr R_L[\psi_1],\mathscr R_L[\psi_2],
\mathscr R_L[\widetilde\psi_{\dot1}],
\mathscr R_L[\widetilde\psi_{\dot2}],
\mathscr R_L[F],\mathscr R_L[\widetilde F],
\mathscr R_L[\mathscr D])\\
&=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0).
\end{aligned}
\tag{4B.46h}
$$

Direct double application of the Step-4A Euclidean vector rules and
(4B.33b)--(4B.35) gives

$$
\begin{aligned}
(&\mathscr R_E[A_1],\mathscr R_E[A_2],
\mathscr R_E[A_3],\mathscr R_E[A_4],
\mathscr R_E[\phi],\mathscr R_E[\widetilde\phi],\\
&\mathscr R_E[\lambda_1],\mathscr R_E[\lambda_2],
\mathscr R_E[\widetilde\lambda_{\dot1}],
\mathscr R_E[\widetilde\lambda_{\dot2}],\\
&\mathscr R_E[\psi_1],\mathscr R_E[\psi_2],
\mathscr R_E[\widetilde\psi_{\dot1}],
\mathscr R_E[\widetilde\psi_{\dot2}],
\mathscr R_E[F],\mathscr R_E[\widetilde F],
\mathscr R_E[\mathscr D])\\
&=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0).
\end{aligned}
\tag{4B.46i}
$$

The exact object and binding counts are

$$
\begin{aligned}
N_{\rm primitive}^{L}=N_{\rm primitive}^{E}&=17,\\
N_{\rm derived}^{L}=N_{\rm derived}^{E}&=5,\\
N_{\rm residual}^{L}=N_{\rm residual}^{E}&=22,\\
N_{\rm free\text{-}bind}^{L}=N_{\rm free\text{-}bind}^{E}
&=2\cdot17\cdot17=578,\\
N_{\rm free\text{-}bind}^{L+E}&=1156.
\end{aligned}
\tag{4B.46j}
$$

Only after (4B.46h)--(4B.46i), the even-derivation identities give

$$
\boxed{
\begin{aligned}
\mathscr R_R[\mathcal D_MX]
&=\mathcal D_M\mathscr R_R[X]
-i\llbracket\mathscr R_R[A_M],X\rrbracket,\\
\mathscr R_R[F_{MN}]
&=\mathcal D_M\mathscr R_R[A_N]
-\mathcal D_N\mathscr R_R[A_M],\\
\mathscr R_R[\llbracket U,V\rrbracket]
&=\llbracket\mathscr R_R[U],V\rrbracket
+\llbracket U,\mathscr R_R[V]\rrbracket.
\end{aligned}}
\tag{4B.46k}
$$

Thus the instructor recursion is the conditional implication

$$
\operatorname{DiffLie}(\mathscr P_R)
:=\langle\mathscr P_R\rangle_{\mathcal D,\llbracket\ ,\ \rrbracket},
\qquad
\left.\mathscr R_R\right|_{\mathscr P_R}=0
\quad\Longrightarrow\quad
\left.\mathscr R_R\right|_{\operatorname{DiffLie}(\mathscr P_R)}=0;
\tag{4B.46l}
$$

it does not establish the premise.  The five derived slots are

$$
\mu:=\llbracket\phi,\widetilde\phi\rrbracket,
\qquad
H:=\mathscr D+\mu,
\qquad
Y_{11}:=-\sqrt2F,
\qquad
Y_{22}:=-\sqrt2\widetilde F,
\qquad
Y_{12}:=iH.
\tag{4B.46m}
$$

Direct double application to the five expressions in (4B.46m) first
gives five zero PBW residuals.  Independently, (4B.46k) reproduces them
as

$$
\begin{aligned}
\mathscr R_R[\mu]
&=\llbracket\mathscr R_R[\phi],\widetilde\phi\rrbracket
+\llbracket\phi,\mathscr R_R[\widetilde\phi]\rrbracket=0,\\
\mathscr R_R[H]
&=\mathscr R_R[\mathscr D]+\mathscr R_R[\mu]=0,\\
\mathscr R_R[Y_{11}]&=-\sqrt2\mathscr R_R[F]=0,\\
\mathscr R_R[Y_{22}]&=-\sqrt2\mathscr R_R[\widetilde F]=0,\\
\mathscr R_R[Y_{12}]&=i\mathscr R_R[H]=0.
\end{aligned}
\tag{4B.46n}
$$

For a Lie algebra \(\mathfrak g\) with basis \(T_A\), let
\(\mathscr C_{R,\mathfrak g}\) be the free supercommutative coefficient
algebra generated by the colored jets \(J_{\Xi,\mathbf n}^{A}\).  Define

$$
\begin{aligned}
\operatorname{ev}_{\mathfrak g}:\mathcal A_{\rm univ}^{R}
&\longrightarrow
\Lambda(\Theta_R)\widehat\otimes
\mathscr C_{R,\mathfrak g}\widehat\otimes U(\mathfrak g),\\
\operatorname{ev}_{\mathfrak g}(\theta_i)&=\theta_i,\\
\operatorname{ev}_{\mathfrak g}(J_{\Xi,\mathbf n})
&=J_{\Xi,\mathbf n}^{A}T_A,
\end{aligned}
$$

where \(\widehat\otimes\) uses the Koszul product.  The tensor-algebra
universal property extends \(\operatorname{ev}_{\mathfrak g}\) to an
algebra homomorphism.  Hence

$$
X=0\ \text{in }\mathcal A_{\rm univ}^{R}
\quad\Longrightarrow\quad
\operatorname{ev}_{\mathfrak g}(X)=0.
$$

PBW is used only for the injective inclusion
\(\mathfrak g\hookrightarrow U(\mathfrak g)\); injectivity of
\(\operatorname{ev}_{\mathfrak g}\) is neither asserted nor required.
Therefore

$$
\left.
\begin{gathered}
c_{AB}{}^C=-c_{BA}{}^C,\\
c_{AB}{}^Ec_{EC}{}^D
+c_{BC}{}^Ec_{EA}{}^D
+c_{CA}{}^Ec_{EB}{}^D=0,\\
J_{\Xi,\mathbf n}\text{ are algebraically independent},\\
\mathcal D_MX\text{ and }F_{MN}\text{ are expanded by (4.50)}
\end{gathered}
\right\}
\Longrightarrow
\boxed{
\texttt{N2\_GENERAL\_LIE\_CLOSURE}
=\texttt{PASS\_EXACT\_GENERAL\_LIE\_CLOSURE}.}
\tag{4B.46o}
$$

No Euler operator enters (4B.46h)--(4B.46o).  The auxiliary-eliminated
surface remains a separate boundary:

$$
\boxed{
\texttt{N2\_ONSHELL\_SU2\_R\_BOUNDARY}:
\qquad
F=\widetilde F=H=0,
\qquad
\mathscr D=-\mu.}
\tag{4B.46p}
$$

### 4B.10 Noether currents in the verifier-gated \(SU(2)_R\) field basis

Here \(i=1,2\) is the \(SU(2)_R\) doublet index fixed by
(4B.27)--(4B.33L6c) within the exact intertwiner-gate scope.  The global
rules use \({\rm PL}\) order; before applying (4.39)--(4.42), localization
uses the parity map (4.38c) to place every local parameter in \({\rm PR}\)
order.  The current-generator intertwiner is not separately
machine-checked.

The non-topological symplectic coefficient of (4B.10) is

$$
\boxed{
\begin{aligned}
C_{L,ia}^\mu=h\operatorname{tr}_\kappa\Big[&
-iF^{\mu\nu}\varepsilon_{ij}
(\sigma_{L,\nu})_{a\dot b}\bar\chi^{j\dot b}
-\sqrt2(\mathcal D^\mu\widetilde\phi)\chi_{ia}\\
&+i\bar\chi^k_{\dot b}(\bar\sigma_L^\mu)^{\dot bc}
\left(-\varepsilon_{ki}(\sigma_L^{\rho\sigma})_c{}^d
\epsilon_{da}F_{\rho\sigma}
+\epsilon_{ca}Y_{ki}-i\epsilon_{ca}\mu\varepsilon_{ki}
\right)\Big].
\end{aligned}}
\tag{4B.47}
$$

The ordered constant-parameter variation of the four non-topological
sectors of (4B.10) gives, before defining a current,

$$
\delta_{\zeta={\rm const}}\mathcal L_L^{(2)}
=\partial_\mu(K_{L,ia}^\mu\zeta^{ia})
+\partial_\mu(\bar K_L^{\mu i\dot a}\bar\zeta_{i\dot a}),
\tag{4B.47a}
$$

with

$$
\boxed{
\begin{aligned}
K_{L,ia}^\mu=C_{L,ia}^\mu
-h\operatorname{tr}_\kappa\Big[&
-i\varepsilon_{ij}F_{\rho\sigma}
(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}\bar\chi^{j\dot b}\\
&-\sqrt2(\mathcal D_\nu\widetilde\phi)
(\sigma_L^\nu)_{a\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\chi_{ib}\\
&+iY_{ij}(\sigma_L^\mu)_{a\dot b}\bar\chi^{j\dot b}
-\mu\varepsilon_{ij}(\sigma_L^\mu)_{a\dot b}
\bar\chi^{j\dot b}\Big].
\end{aligned}}
\tag{4B.47b}
$$

The local-parameter coefficient is therefore

$$
j_{L,ia}^\mu:=C_{L,ia}^\mu-K_{L,ia}^\mu.
\tag{4B.47c}
$$

Substitution of (4B.47b) gives

$$
\boxed{
\begin{aligned}
j_{L,ia}^\mu=h\operatorname{tr}_\kappa\Big[&
-i\varepsilon_{ij}F_{\rho\sigma}
(\sigma_L^{\rho\sigma})_a{}^b
(\sigma_L^\mu)_{b\dot b}\bar\chi^{j\dot b}\\
&-\sqrt2(\mathcal D_\nu\widetilde\phi)
(\sigma_L^\nu)_{a\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\chi_{ib}\\
&+iY_{ij}(\sigma_L^\mu)_{a\dot b}\bar\chi^{j\dot b}
-\mu\varepsilon_{ij}(\sigma_L^\mu)_{a\dot b}
\bar\chi^{j\dot b}\Big].
\end{aligned}}
\tag{4B.48}
$$

Equation (4B.48) is therefore a derived (C-K) coefficient, not an
improved current.

Lorentzian conjugation gives the second independent spinor slot:

$$
\boxed{
\begin{aligned}
\bar j_L^{\mu\dot a i}
=h\operatorname{tr}_\kappa\Big[&
-i\varepsilon^{ij}F_{\rho\sigma}
(\bar\sigma_L^{\rho\sigma})^{\dot a}{}_{\dot b}
(\bar\sigma_L^\mu)^{\dot bb}\chi_{jb}\\
&-\sqrt2(\mathcal D_\nu\phi)
(\bar\sigma_L^\nu)^{\dot ab}(\sigma_L^\mu)_{b\dot b}
\bar\chi^{i\dot b}\\
&-iY^{ij}(\bar\sigma_L^\mu)^{\dot ab}\chi_{jb}
+\mu\varepsilon^{ij}(\bar\sigma_L^\mu)^{\dot ab}
\chi_{jb}\Big].
\end{aligned}}
\tag{4B.48a}
$$

$$
\bar j_L^{\mu\dot a i}
=(j_{L,ia}^\mu)^\dagger,
\qquad
\bar K_L^{\mu\dot a i}
=(K_{L,ia}^\mu)^\dagger,
\qquad
\bar C_L^{\mu\dot a i}
=(C_{L,ia}^\mu)^\dagger.
\tag{4B.48b}
$$

The topological sector obeys

$$
C_{\vartheta,L,ia}^\mu
=K_{\vartheta,L,ia}^\mu
=-i\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}
\varepsilon_{ij}(\sigma_{L,\nu})_{a\dot b}
\bar\chi^{Bj\dot b},
\tag{4B.50}
$$

and therefore does not occur in (4B.48).

The manifest and hidden components of the verifier-gated doublet are

$$
\boxed{
\begin{aligned}
j_{L,1a}^\mu=h\operatorname{tr}_\kappa\Big[&
-iF_{\rho\sigma}\sigma_L^{\rho\sigma}\sigma_L^\mu
\widetilde\lambda
-\sqrt2\mathcal D_\nu\widetilde\phi
\sigma_L^\nu\bar\sigma_L^\mu\psi\\
&+\mathscr D\sigma_L^\mu\widetilde\lambda
-i\sqrt2F\sigma_L^\mu\widetilde\psi\Big]_a,
\end{aligned}}
\tag{4B.51}
$$

$$
\boxed{
\begin{aligned}
j_{L,\eta a}^\mu:=-j_{L,2a}^\mu
=h\operatorname{tr}_\kappa\Big[&
+iF_{\rho\sigma}\sigma_L^{\rho\sigma}\sigma_L^\mu
\widetilde\psi
-\sqrt2\mathcal D_\nu\widetilde\phi
\sigma_L^\nu\bar\sigma_L^\mu\lambda\\
&+(\mathscr D+2\mu)\sigma_L^\mu\widetilde\psi
-i\sqrt2\widetilde F\sigma_L^\mu\widetilde\lambda
\Big]_a.
\end{aligned}}
\tag{4B.52}
$$

Equations (4B.47)--(4B.52) contain no improvement term.

Direct localization of (4B.17) gives the Euclidean symplectic
coefficient

$$
\boxed{
\begin{aligned}
C_{E,ia}^{m}=h\operatorname{tr}_\kappa\Big[&
-F^{mn}\varepsilon_{ij}(\sigma_{E,n})_{a\dot b}
\widetilde\chi^{j\dot b}
+\sqrt2(\mathcal D^m\widetilde\phi)\chi_{ia}\\
&+\widetilde\chi^k_{\dot b}(\bar\sigma_E^m)^{\dot bc}
\left(
\varepsilon_{ki}(\sigma_E^{rs})_c{}^d\epsilon_{da}F_{rs}
+\epsilon_{ca}Y_{E,ki}
-i\epsilon_{ca}\mu_E\varepsilon_{ki}
\right)\Big].
\end{aligned}}
\tag{4B.50a}
$$

The ordered constant-parameter variation gives

$$
\delta_{\zeta={\rm const}}\mathcal L_E^{(2)}
=\partial_m(K_{E,ia}^m\zeta^{ia})
+\partial_m(\widetilde K_E^{mi\dot a}\bar\zeta_{i\dot a}),
\tag{4B.50b}
$$

$$
\boxed{
\begin{aligned}
K_{E,ia}^{m}=C_{E,ia}^{m}
-h\operatorname{tr}_\kappa\Big[&
+\varepsilon_{ij}F_{rs}
(\sigma_E^{rs})_a{}^b(\sigma_E^m)_{b\dot b}
\widetilde\chi^{j\dot b}\\
&-\sqrt2(\mathcal D_n\widetilde\phi)
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\chi_{ib}\\
&+Y_{E,ij}(\sigma_E^m)_{a\dot b}
\widetilde\chi^{j\dot b}
+i\mu_E\varepsilon_{ij}(\sigma_E^m)_{a\dot b}
\widetilde\chi^{j\dot b}\Big].
\end{aligned}}
\tag{4B.50c}
$$

The Euclidean topological coefficient obeys

$$
\boxed{
C_{\vartheta,E,ia}^{m}
=K_{\vartheta,E,ia}^{m}
=+i\mathfrak k_{AB}({}^{\star}F_E^A)^{mn}
\varepsilon_{ij}(\sigma_{E,n})_{a\dot b}
\widetilde\chi^{Bj\dot b}.}
\tag{4B.50d}
$$

Hence \(j_E=C_E-K_E\) gives

$$
\boxed{
\begin{aligned}
j_{E,ia}^{m}=h\operatorname{tr}_\kappa\Big[&
+\varepsilon_{ij}F_{rs}
(\sigma_E^{rs})_a{}^b(\sigma_E^m)_{b\dot b}
\widetilde\chi^{j\dot b}\\
&-\sqrt2(\mathcal D_n\widetilde\phi)
(\sigma_E^n)_{a\dot b}(\bar\sigma_E^m)^{\dot bb}
\chi_{ib}\\
&+Y_{E,ij}(\sigma_E^m)_{a\dot b}
\widetilde\chi^{j\dot b}
+i\mu_E\varepsilon_{ij}(\sigma_E^m)_{a\dot b}
\widetilde\chi^{j\dot b}\Big].
\end{aligned}}
\tag{4B.52a}
$$

The independently localized
\(\widetilde\varepsilon_{\dot a i}\) current is

$$
\boxed{
\begin{aligned}
\widetilde j_E^{m\dot a i}
=h\operatorname{tr}_\kappa\Big[&
+\varepsilon^{ij}F_{rs}
(\bar\sigma_E^{rs})^{\dot a}{}_{\dot b}
(\bar\sigma_E^m)^{\dot bb}\chi_{jb}\\
&-\sqrt2(\mathcal D_n\phi)
(\bar\sigma_E^n)^{\dot ab}(\sigma_E^m)_{b\dot b}
\widetilde\chi^{i\dot b}\\
&-Y_E^{ij}(\bar\sigma_E^m)^{\dot ab}\chi_{jb}
-i\mu_E\varepsilon^{ij}(\bar\sigma_E^m)^{\dot ab}
\chi_{jb}\Big].
\end{aligned}}
\tag{4B.52a1}
$$

Its direct constant-parameter boundary coefficient satisfies

$$
\widetilde j_E^{m\dot a i}
=\widetilde C_E^{m\dot a i}
-\widetilde K_E^{m\dot a i},
\tag{4B.52a2}
$$

and its topological sector obeys

$$
\widetilde C_{\vartheta,E}^{m\dot a i}
=\widetilde K_{\vartheta,E}^{m\dot a i}
=+i\mathfrak k_{AB}({}^{\star}F_E^A)^{mn}
\varepsilon^{ij}(\bar\sigma_{E,n})^{\dot ab}
\chi_{jb}^{B}.
\tag{4B.52a3}
$$

For the manifest parameter,

$$
\boxed{
\begin{aligned}
j_{E,1a}^{m}=h\operatorname{tr}_\kappa\Big[&
+F_{rs}\sigma_E^{rs}\sigma_E^m\widetilde\lambda
-\sqrt2\mathcal D_n\widetilde\phi
\sigma_E^n\bar\sigma_E^m\psi\\
&-i\mathscr D\sigma_E^m\widetilde\lambda
-\sqrt2F\sigma_E^m\widetilde\psi\Big]_a.
\end{aligned}}
\tag{4B.52b}
$$

The hidden-parameter current is

$$
\boxed{
\begin{aligned}
j_{E,\eta a}^{m}:=-j_{E,2a}^{m}
=h\operatorname{tr}_\kappa\Big[&
-F_{rs}\sigma_E^{rs}\sigma_E^m\widetilde\psi
-\sqrt2\mathcal D_n\widetilde\phi
\sigma_E^n\bar\sigma_E^m\lambda\\
&-i(\mathscr D+2\mu_E)\sigma_E^m\widetilde\psi
-\sqrt2\widetilde F\sigma_E^m\widetilde\lambda
\Big]_a.
\end{aligned}}
\tag{4B.52c}
$$

Every term obeys the locked vector-current Wick map

$$
j_{E,i}^{k}=-j_{L,i}^{k}\big|_{\rm Wick},
\qquad
j_{E,i}^{4}=-ij_{L,i}^{0}\big|_{\rm Wick}.
\tag{4B.52d}
$$

### 4B.11 Current divergence

The normalized Lorentzian Euler operators obtained by ordered
variation of (4B.10) are

$$
\boxed{
\begin{aligned}
\mathscr A^\nu={}&
\mathcal D_\mu F^{\mu\nu}
-(\phi\times\mathcal D^\nu\widetilde\phi)
-(\widetilde\phi\times\mathcal D^\nu\phi)\\
&-i[(\bar\lambda_{\dot a}\bar\sigma_L^{\nu\dot aa})
\times\lambda_a]
-i[(\widetilde\psi_{\dot a}\bar\sigma_L^{\nu\dot aa})
\times\psi_a],\\
\mathscr P={}&
\mathcal D_\mu\mathcal D^\mu\widetilde\phi
+i(\widetilde\phi\times\mathscr D)
+\sqrt2(\widetilde\psi\times\bar\lambda),\\
\widetilde{\mathscr P}={}&
\mathcal D_\mu\mathcal D^\mu\phi
+i(\mathscr D\times\phi)
-\sqrt2(\lambda\times\psi),\\
\mathcal E_{\psi,a}={}&
-i(\sigma_L^\mu)_{a\dot b}\mathcal D_\mu
\widetilde\psi^{\dot b}
+\sqrt2(\widetilde\phi\times\lambda)_a,\\
\mathcal E_{\lambda,a}={}&
-i(\sigma_L^\mu)_{a\dot b}\mathcal D_\mu
\bar\lambda^{\dot b}
-\sqrt2(\widetilde\phi\times\psi)_a,\\
\widetilde{\mathcal E}_{\widetilde\psi}^{\dot a}={}&
+i(\bar\sigma_L^\mu)^{\dot aa}\mathcal D_\mu\psi_a
+\sqrt2(\phi\times\bar\lambda)^{\dot a},\\
\widetilde{\mathcal E}_{\bar\lambda}^{\dot a}={}&
+i(\bar\sigma_L^\mu)^{\dot aa}\mathcal D_\mu\lambda_a
-\sqrt2(\phi\times\widetilde\psi)^{\dot a},\\
\mathcal E_{\mathscr D}&=H,
\qquad
\mathcal E_F=\widetilde F,
\qquad
\mathcal E_{\widetilde F}=F.
\end{aligned}}
\tag{4B.52f}
$$

Write (4B.48) as

$$
j_{L,ia}^\mu=j_{F,ia}^\mu+j_{\phi,ia}^\mu
+j_{Y,ia}^\mu+j_{\mu,ia}^\mu.
\tag{4B.52g}
$$

Trace invariance converts every ordinary divergence into a covariant
product rule.  Before using any equation of motion,

$$
\boxed{
\begin{aligned}
\frac1h\partial_\mu j_{L,ia}^\mu
=\operatorname{tr}_\kappa\Big[{}
&-i\varepsilon_{ij}(\mathcal D_\mu F_{\rho\sigma})
(\sigma_L^{\rho\sigma}\sigma_L^\mu)_{a\dot b}
\bar\chi^{j\dot b}\\
&-i\varepsilon_{ij}F_{\rho\sigma}
(\sigma_L^{\rho\sigma}\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\chi^{j\dot b}\\
&-\sqrt2(\mathcal D_\mu\mathcal D_\nu\widetilde\phi)
(\sigma_L^\nu\bar\sigma_L^\mu)_a{}^b\chi_{ib}\\
&-\sqrt2(\mathcal D_\nu\widetilde\phi)
(\sigma_L^\nu\bar\sigma_L^\mu)_a{}^b
\mathcal D_\mu\chi_{ib}\\
&+i(\mathcal D_\mu Y_{ij})(\sigma_L^\mu)_{a\dot b}
\bar\chi^{j\dot b}
+iY_{ij}(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\chi^{j\dot b}\\
&-(\mathcal D_\mu\mu)\varepsilon_{ij}
(\sigma_L^\mu)_{a\dot b}\bar\chi^{j\dot b}
-\mu\varepsilon_{ij}(\sigma_L^\mu)_{a\dot b}
\mathcal D_\mu\bar\chi^{j\dot b}\Big].
\end{aligned}}
\tag{4B.52h}
$$

The two second-derivative reductions are

$$
\begin{aligned}
(\mathcal D_\mu F_{\rho\sigma})
\sigma_L^{\rho\sigma}\sigma_L^\mu
&=(\mathcal D_\rho F^{\rho\nu})\sigma_{L,\nu}
-\frac i2\epsilon_L^{\rho\sigma\mu\nu}
(\mathcal D_\mu F_{\rho\sigma})\sigma_{L,\nu}\\
&=(\mathcal D_\rho F^{\rho\nu})\sigma_{L,\nu},\\
(\mathcal D_\mu\mathcal D_\nu\widetilde\phi)
\sigma_L^\nu\bar\sigma_L^\mu
&=-\mathcal D_\mu\mathcal D^\mu\widetilde\phi
+i\sigma_L^{\mu\nu}
\llbracket F_{\mu\nu},\widetilde\phi\rrbracket.
\end{aligned}
\tag{4B.52i}
$$

The first equality uses the exact Step-1 identity

$$
\sigma_L^{\rho\sigma}\sigma_L^\mu
=\frac12\left(
\eta^{\rho\mu}\sigma_L^\sigma
-\eta^{\sigma\mu}\sigma_L^\rho
-i\epsilon_L^{\rho\sigma\mu\nu}\sigma_{L,\nu}
\right),
\tag{4B.52j}
$$

and the second line of (4B.52i) uses

$$
[\mathcal D_\mu,\mathcal D_\nu]X
=-i\llbracket F_{\mu\nu},X\rrbracket.
\tag{4B.52k}
$$

The remaining differentiated composite slots expand without a
suppressed term:

$$
\begin{aligned}
\mathcal D_\mu\mu
&=\llbracket\mathcal D_\mu\phi,\widetilde\phi\rrbracket
+\llbracket\phi,\mathcal D_\mu\widetilde\phi\rrbracket,\\
\mathcal D_\mu Y_{11}&=-\sqrt2\mathcal D_\mu F,\\
\mathcal D_\mu Y_{22}&=-\sqrt2\mathcal D_\mu\widetilde F,\\
\mathcal D_\mu Y_{12}
&=i\mathcal D_\mu\mathscr D+i\mathcal D_\mu\mu.
\end{aligned}
\tag{4B.52l}
$$

Thus the \(\epsilon_L^{\rho\sigma\mu\nu}\) remainder vanishes by

$$
\mathcal D_{[\mu}F_{\rho\sigma]}=0.
\tag{4B.52m}
$$

Every cubic remainder is reduced with the two displayed identities

$$
\begin{aligned}
\operatorname{tr}_\kappa
\big(X\llbracket Y,Z\rrbracket\big)
&=\operatorname{tr}_\kappa
\big(\llbracket X,Y\rrbracket Z\big),\\
\llbracket X,\llbracket Y,Z\rrbracket\rrbracket
&+(-1)^{|X|(|Y|+|Z|)}
\llbracket Y,\llbracket Z,X\rrbracket\rrbracket\\
&+(-1)^{|Z|(|X|+|Y|)}
\llbracket Z,\llbracket X,Y\rrbracket\rrbracket=0.
\end{aligned}
\tag{4B.52n}
$$

Substitution of (4B.52i)--(4B.52n) into the eight lines of
(4B.52h) groups the gauge-divergence terms into \(\mathscr A^\nu\),
the scalar second derivatives into \(\mathscr P,
\widetilde{\mathscr P}\), the four first-order spinor terms into the
four fermion Euler operators, and the last three lines into
\(H,\widetilde F,F\).  No term remains after the Bianchi and Jacobi
lines above.  Therefore the ordered local-parameter identity is

$$
\delta_\zeta\Xi
=\mathcal R_{\Xi,ia}\zeta^{ia}
+\widetilde{\mathcal R}_{\Xi}^{i\dot a}
\bar\zeta_{i\dot a},
\tag{4B.52e}
$$

where every odd parameter has first been moved to the right.  Then

$$
\boxed{
\begin{aligned}
\partial_\mu j_{L,ia}^\mu
=-h\operatorname{tr}_\kappa\Big[
\mathscr A^\nu\mathcal R_{A_\nu,ia}
+\mathscr P\mathcal R_{\phi,ia}
+\widetilde{\mathscr P}\mathcal R_{\widetilde\phi,ia}
+\mathcal E_{\psi}^b\mathcal R_{\psi_b,ia}
+\mathcal E_{\lambda}^b\mathcal R_{\lambda_b,ia}\\
\qquad
+\widetilde{\mathcal E}_{\widetilde\psi,\dot b}
\mathcal R_{\widetilde\psi^{\dot b},ia}
+\widetilde{\mathcal E}_{\bar\lambda,\dot b}
\mathcal R_{\bar\lambda^{\dot b},ia}
+H\mathcal R_{\mathscr D,ia}
+\widetilde F\mathcal R_{F,ia}
+F\mathcal R_{\widetilde F,ia}
\Big].
\end{aligned}}
\tag{4B.53}
$$

where

$$
\Xi\in\{A_\mu,\phi,\widetilde\phi,
\chi_i,\bar\chi^i,F,\widetilde F,\mathscr D\},
\tag{4B.54}
$$

and every \(\mathcal R\) on the right is the explicit coefficient in
(4B.20)--(4B.35c).  Hence all ten Euler equations imply

$$
\partial_\mu j_{L,ia}^\mu=0.
\tag{4B.55}
$$

For the Euclidean ordered Euler operators of (4B.17), direct
differentiation of (4B.52a) gives

$$
\begin{gathered}
\mathscr A_E^i=-\mathscr A_L^i|_{\rm Wick},
\qquad
\mathscr A_E^4=-i\mathscr A_L^0|_{\rm Wick},
\qquad
\mathscr P_E=-\mathscr P_L|_{\rm Wick},
\qquad
\widetilde{\mathscr P}_E
=-\widetilde{\mathscr P}_L|_{\rm Wick},\\
\mathcal E_{E,\psi}=\mathcal E_{L,\psi}|_{\rm Wick},
\qquad
\mathcal E_{E,\lambda}=\mathcal E_{L,\lambda}|_{\rm Wick},
\qquad
\widetilde{\mathcal E}_{E}
=\widetilde{\mathcal E}_{L}|_{\rm Wick},\\
\mathcal E_{E,\mathscr D}=-H_E,
\qquad
\mathcal E_{E,F}=-\widetilde F,
\qquad
\mathcal E_{E,\widetilde F}=-F.
\end{gathered}
\tag{4B.55a}
$$

These equations follow both from direct variation of (4B.17) and from
the locked Wick map.  Then

$$
\boxed{
\partial_m j_{E,ia}^{m}
=-h\operatorname{tr}_\kappa\!\left[
\sum_{\Xi_E}
\mathcal E_{E,\Xi_E}\mathcal R_{E,\Xi_E,ia}\right].}
\tag{4B.56}
$$

The second spinor slots obey

$$
\boxed{
\partial_\mu\bar j_L^{\mu\dot a i}
=\left(\partial_\mu j_{L,ia}^{\mu}\right)^\dagger
=-h\operatorname{tr}_\kappa\!\left[
\sum_\Xi\mathcal E_{L,\Xi}
\widetilde{\mathcal R}_{L,\Xi}^{i\dot a}\right],}
\tag{4B.56a}
$$

$$
\boxed{
\partial_m\widetilde j_E^{m\dot a i}
=-h\operatorname{tr}_\kappa\!\left[
\sum_{\Xi_E}\mathcal E_{E,\Xi_E}
\widetilde{\mathcal R}_{E,\Xi_E}^{i\dot a}\right].}
\tag{4B.56b}
$$

$$
\Xi_E\in\{A_m,\phi,\widetilde\phi,
\chi_i,\widetilde\chi^i,F,\widetilde F,\mathscr D\}.
\tag{4B.57}
$$

Thus

$$
\mathcal E_{E,\Xi_E}=0
\quad\Longrightarrow\quad
\partial_m j_{E,ia}^{m}=0.
\tag{4B.58}
$$
