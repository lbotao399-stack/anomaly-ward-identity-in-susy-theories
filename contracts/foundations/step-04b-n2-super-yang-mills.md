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
&=i\sqrt2(\mathcal D_\mu\psi)\sigma_L^\mu\bar\varepsilon
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
-i\psi\sigma_{L,\mu}\bar\eta.
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
&=-i\sqrt2(\mathcal D_\mu\lambda)\sigma_L^\mu\bar\eta
+2i\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta_2\mathscr D
&=-\eta\sigma_L^\mu\mathcal D_\mu\widetilde\psi
-(\mathcal D_\mu\psi)\sigma_L^\mu\bar\eta\\
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
-(\mathcal D_\mu\psi)\sigma_L^\mu\bar\eta
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
=2(\sigma_L^\rho)_{(c|\dot b}
\mathcal D_\rho\widetilde\psi^{\dot b}\eta_{|a)}.
\tag{4B.22b}
$$

Substitution of

$$
\delta_2F_{\mu\nu}
=-f_A\left[
\sigma_{L,\nu}\mathcal D_\mu\widetilde\psi
-\sigma_{L,\mu}\mathcal D_\nu\widetilde\psi\right]\eta
\tag{4B.22c}
$$

and the Step-1 matrices gives

$$
\boxed{f_A=+i.}
\tag{4B.22d}
$$

Lorentzian conjugation fixes the coefficient \(-i\) of
\(\psi\sigma_{L,\mu}\bar\eta\) in (4B.21).

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

### 4B.6 Doublet rules and the off-shell \(SU(2)_R\) gate

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
+i\varepsilon^{ij}\chi_i\sigma_{L,\mu}\bar\zeta_j,
\tag{4B.30}
$$

and the three auxiliary slots have the complete transformations

$$
\boxed{
\begin{aligned}
\delta Y_{11}={}&
-2i(\mathcal D_\mu\psi)\sigma_L^\mu\bar\varepsilon
-2i\eta\sigma_L^\mu\mathcal D_\mu\bar\lambda\\
&+2i\sqrt2\llbracket\bar\varepsilon\bar\lambda,\phi\rrbracket
-2i\sqrt2\llbracket\eta\psi,\widetilde\phi\rrbracket,\\
\delta Y_{22}={}&
-2i\varepsilon\sigma_L^\mu\mathcal D_\mu\widetilde\psi
+2i(\mathcal D_\mu\lambda)\sigma_L^\mu\bar\eta\\
&+2i\sqrt2\llbracket\varepsilon\lambda,\widetilde\phi\rrbracket
-2i\sqrt2\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta Y_{12}={}&
-i\varepsilon\sigma_L^\mu\mathcal D_\mu\bar\lambda
+i\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\lambda\\
&-i\eta\sigma_L^\mu\mathcal D_\mu\widetilde\psi
-i(\mathcal D_\mu\psi)\sigma_L^\mu\bar\eta\\
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

We now test, rather than assume, a linear off-shell \(SU(2)_R\)
tensor structure.  Allow the full invertible ansatz

$$
\chi_1=\psi,
\quad
\chi_2=s\lambda,
\quad
\zeta^1=\varepsilon,
\quad
\zeta^2=s^{-1}\eta,
\quad
Y_{11}=aF,
\quad
Y_{22}=b\widetilde F,
\quad
Y_{12}=cH,
\quad s\ne0.
\tag{4B.33}
$$

The most general tensor auxiliary term in \(\delta\chi_i\) is

$$
\left.\delta\chi_i\right|_{Y,\mu}
=\gamma Y_{ij}\zeta^j
+\beta\mu\varepsilon_{ij}\zeta^j.
\tag{4B.33L1}
$$

The manifest \(F\varepsilon\) and \(\mathscr D\varepsilon\) slots fix

$$
\gamma a=-\sqrt2,
\qquad
\gamma c=-is.
\tag{4B.33L2}
$$

A symmetric lower-index tensor must also have

$$
\left.\delta Y_{ij}\right|_{\mathcal D\chi\bar\zeta}
=A(\mathcal D_\mu\chi_{(i})
\sigma_L^\mu\bar\zeta_{j)}.
\tag{4B.33L3}
$$

The manifest \(Y_{11}\) slot gives \(A=ai\sqrt2\).  Since

$$
\bar\varepsilon\bar\sigma_L^\mu\mathcal D_\mu\lambda
=-(\mathcal D_\mu\lambda)\sigma_L^\mu\bar\varepsilon,
\tag{4B.33L4}
$$

the manifest \(Y_{12}\) slot gives

$$
\frac12As=-c,
\qquad
\gamma c=+is.
\tag{4B.33L5}
$$

Equations (4B.33L2) and (4B.33L5) imply \(s=0\), contrary to
(4B.33).  This obstruction is Abelian and precedes every compensator,
Jacobi, auxiliary shift, and hidden top-slot coefficient.  It excludes
only the declared linear invertible doublet/triplet ansatz (4B.33);
nonlinear or field-dependent alternatives are not tested here.

The two projected signs in this contradiction are fixed directly.
Equations (3A.28) and (2A.20d) give

$$
\begin{aligned}
\left[-\varepsilon^a\partial_a\widetilde\Phi_L
\right]_{\bar\vartheta^2}
&=\frac{i}{\sqrt2}\varepsilon\sigma_L^\mu
\partial_\mu\widetilde\psi,\\
\left[-i\varepsilon\sigma_L^\mu\bar\vartheta\,
\partial_\mu\widetilde\Phi_L\right]_{\bar\vartheta^2}
&=\frac{i}{\sqrt2}\varepsilon\sigma_L^\mu
\partial_\mu\widetilde\psi,
\end{aligned}
\tag{4B.33L6}
$$

so \(\delta_1\widetilde F=+i\sqrt2\varepsilon\sigma_L^\mu
\partial_\mu\widetilde\psi\).  Moreover, (4A.25),
\(\mathscr D=-\frac12\epsilon^{ab}\mathsf M_{ba}\), and
\(w_a=-i\lambda_a\) give

$$
\begin{aligned}
\left.\delta\mathscr D\right|_{\bar\varepsilon}
&=-\epsilon^{ab}(\sigma_L^\mu)_{b\dot c}
\bar\varepsilon^{\dot c}\mathcal D_\mu\lambda_a\\
&=+\bar\varepsilon_{\dot a}
(\bar\sigma_L^\mu)^{\dot aa}\mathcal D_\mu\lambda_a.
\end{aligned}
\tag{4B.33L7}
$$

Thus neither sign may be flipped.  The component rules and their
checked closure remain valid; the stronger linear off-shell
\(SU(2)_R\)-triplet claim is blocked by (4B.33L5).

After deleting the auxiliary slots on the surface (4B.15),

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
+i\varepsilon^{ij}\chi_i\sigma_{L,\mu}\bar\zeta_j,\\
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
These are exactly the auxiliary-eliminated \(\psi\) and
\(-\lambda\) rules.  Equation (4B.33L7b) is therefore a
componentwise \(SU(2)_R\)-covariant rewriting of the physical-field
variations.  Neither invariance of the eliminated action nor closure
of the on-shell algebra is proved or claimed here.

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

Contracted indices do not prove covariance of the transformation law.
For the explicit candidate

$$
U_R=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
U_R^T\varepsilon U_R=\varepsilon,
\qquad
Y\longmapsto U_RYU_R^T,
\tag{4B.33L10}
$$

the \(11\to22\) image of the derivative term disagrees with the direct
\(22\) slot in (4B.31).  Therefore
\(\delta_2=U_R\delta_1U_R^{-1}\) is not asserted.  Hidden invariance is
the direct component cancellation fixed by (4B.4d), (4B.4g), their
conjugates, and the non-Abelian Jacobi cancellations below.

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
&=-\sqrt2(\mathcal D_m\psi)\sigma_E^m\bar\varepsilon
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
+\psi\sigma_{E,m}\bar\eta,\\
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
&=+\sqrt2(\mathcal D_m\lambda)\sigma_E^m\bar\eta
+2i\llbracket\bar\eta\widetilde\psi,\phi\rrbracket,\\
\delta_{2,E}\mathscr D
&=-i\eta\sigma_E^m\mathcal D_m\widetilde\psi
-i(\mathcal D_m\psi)\sigma_E^m\bar\eta\\
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
-i(\mathcal D_m\psi)\sigma_E^m\bar\eta\\
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

The tensor expression one would need for an off-shell triplet is

$$
\begin{aligned}
\delta_E^{\rm cand}\chi_{ia}:={}&
\varepsilon_{ij}(\sigma_E^{mn})_a{}^b\zeta_b^jF_{mn}
-\sqrt2(\sigma_E^m)_{a\dot b}\bar\zeta_i^{\dot b}
\mathcal D_m\phi\\
&+Y_{E,ij}\zeta_a^j
-i\mu_E\varepsilon_{ij}\zeta_a^j.
\end{aligned}
\tag{4B.35c}
$$

It is not equal to the direct rules in (4B.33b)--(4B.35): its
manifest mixed auxiliary slot is the Wick image of the contradiction
(4B.33L2)--(4B.33L5).  Hence only the explicit Euclidean component
rules above are used off shell.  On \(F=\widetilde F=H_E=0\), the
candidate reduces to the Wick image of the physical on-shell rule
(4B.33L7b).

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

### 4B.9 Off-shell closure

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

Coefficientwise substitution of (4B.20)--(4B.35) gives

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

No Euler operator is used.  In ordinary-coordinate form,

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

Direct substitution gives

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

Here (X_E) runs over the Euclidean version of every field in
(4B.45).

### 4B.10 Two parameter-basis Noether currents

Because (4B.33L5) blocks the off-shell tensor dictionary, the label
\(i=1,2\) below denotes the manifest/hidden parameter basis only.  No
\(SU(2)_R\)-doublet transformation law is claimed for these currents.

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

The two parameter-basis currents are

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
