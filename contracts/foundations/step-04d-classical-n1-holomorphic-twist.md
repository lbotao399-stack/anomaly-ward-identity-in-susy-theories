# 00 3+1d SUSY QFT — Convention Lock

## Step 4D. Classical holomorphic twist of Euclidean pure \(\mathcal N=1\) gauge theory

### Abstract

This contract constructs the classical holomorphic twist directly from the
off-shell Euclidean component fields and transformations defined below.  On
\(\mathbb R^4=\mathbb C^2\), for the complexified fields on the trivial
bundle and compact-support boundary condition, the charge \(Q=Q^E_1\) is
off-shell square-zero, both antiholomorphic translations are \(Q\)-exact,
and the complete twisted component BV theory admits an odd-symplectic
canonical decomposition

$$
\boxed{
(\mathcal F_{\mathrm{tw}},\omega_{\mathrm{tw}},S_{\mathrm{tw}})
\cong
(\mathcal F_{\mathrm{hBF}},\omega_{\mathrm{hBF}},S_{\mathrm{hBF}})
\times
(T^*[-1]\mathcal V_{\mathrm{ctr}},\omega_{\mathrm{ctr}},S_{\mathrm{ctr}}).}
\tag{4D.1}
$$

The second factor has an explicit cyclic contraction.  Projection along this
factor is therefore a classical BV quasi-isomorphism to holomorphic BF
theory.  For any finite regulator satisfying the compatibility conditions in
4D.13, the corresponding BV change of variables must also move the
gauge-fixing cycle and semidensity.  On a normalized product cycle its
field-dependent tree-level effective action is exactly
\(S_{\mathrm{hBF}}\); equality with an ordinary Euclidean partition function
is not asserted.  No equation of motion is used in the construction.

### Final Result List

$$
\boxed{
\begin{gathered}
Q^2=0,\qquad
P_{\bar1}=\frac1{4i}\{Q,\bar Q^E_{\dot2}\},\qquad
P_{\bar2}=\frac1{4i}\{Q,\bar Q^E_{\dot1}\},\\
\mathcal A\in\Omega^{0,*}(\mathbb C^2,\mathfrak g_{\mathbb C})[1],
\qquad
\mathcal B\in\Omega^{2,*}(\mathbb C^2,\mathfrak g_{\mathbb C}^*),\\
S_{\mathrm{hBF}}
=\int_{\mathbb C^2}
\langle\mathcal B,
\bar\partial\mathcal A
+\tfrac12[\mathcal A,\mathcal A]_{\mathrm{sus}}\rangle,\\
\frac12(S_{\mathrm{hBF}},S_{\mathrm{hBF}})=0.
\end{gathered}}
\tag{4D.2}
$$

The path-integral corollary and its sharp boundary are

$$
\boxed{
S_{\mathrm{eff},\nu}^{(0),\mathrm{field\ dependent}}
=S_{\mathrm{hBF}},
\qquad
\Gamma_{Y,\nu}
=\Gamma_{\mathrm{hBF},\nu}\times\Gamma_{\mathrm{ctr},\nu}
\ \text{is not proved}.}
$$

### 4D.1 Symbols, degrees, and scope

All spacetime, spinor, gauge, and BV symbols used in the proof are fixed in
this section.  Set

$$
\begin{gathered}
z^1=x^1-ix^2,
\qquad
\bar z^{\bar1}=x^1+ix^2,\\
z^2=x^3+ix^4,
\qquad
\bar z^{\bar2}=x^3-ix^4,\\
\partial_{z^1}=\frac12(\partial_1+i\partial_2),
\qquad
\partial_{\bar1}=\frac12(\partial_1-i\partial_2),\\
\partial_{z^2}=\frac12(\partial_3-i\partial_4),
\qquad
\partial_{\bar2}=\frac12(\partial_3+i\partial_4).
\end{gathered}
\tag{4D.3}
$$

The matching translation components are

$$
P_{\bar1}:=\frac12(P_1^E-iP_2^E),
\qquad
P_{\bar2}:=\frac12(P_3^E+iP_4^E).
\tag{4D.3a}
$$

The one-form components and their inverse map are

$$
\begin{aligned}
A_{z^1}&=\frac12(A_1+iA_2),
&A_{\bar1}&=\frac12(A_1-iA_2),\\
A_{z^2}&=\frac12(A_3-iA_4),
&A_{\bar2}&=\frac12(A_3+iA_4),
\end{aligned}
\qquad
\begin{aligned}
A_1&=A_{z^1}+A_{\bar1},\\
A_2&=-iA_{z^1}+iA_{\bar1},\\
A_3&=A_{z^2}+A_{\bar2},\\
A_4&=iA_{z^2}-iA_{\bar2}.
\end{aligned}
\tag{4D.4}
$$

Set

$$
\Omega:=dz^1\wedge dz^2,
\qquad
\bar\Omega:=d\bar z^{\bar1}\wedge d\bar z^{\bar2}.
\tag{4D.5}
$$

Direct expansion gives

$$
\begin{aligned}
\Omega\wedge\bar\Omega
&=(dx^1-i\,dx^2)\wedge(dx^3+i\,dx^4)
\wedge(dx^1+i\,dx^2)\wedge(dx^3-i\,dx^4)\\
&=-4\,dx^1\wedge dx^2\wedge dx^3\wedge dx^4
=-4\,d^4x_E.
\end{aligned}
\tag{4D.6}
$$

Let \(\mathfrak g_{\mathbb C}\) have basis \(T_A\), structure constants
\(c_{AB}{}^C\), and a nondegenerate invariant symmetric form
\(\kappa_{AB}\).  Write

$$
(X\times Y)^A:=c_{BC}{}^AX^BY^C
=-i\llbracket X,Y\rrbracket^A,
\qquad
\operatorname{tr}_\kappa(XY):=\kappa_{AB}X^AY^B,
$$

$$
\langle \xi,X\rangle:=\xi_AX^A
\quad(\xi\in\mathfrak g_{\mathbb C}^*,\ X\in\mathfrak g_{\mathbb C}),
\qquad
\langle X,Y\rangle_\kappa:=\operatorname{tr}_\kappa(XY).
$$

$$
\mathcal D_mX:=\partial_mX+A_m\times X,
\qquad
F_{mn}:=\partial_mA_n-\partial_nA_m+A_m\times A_n.
\tag{4D.7}
$$

The spinor and Euclidean Clifford conventions are

$$
\epsilon_{12}=-1,
\qquad
\epsilon_{21}=+1,
\qquad
\epsilon^{12}=+1,
\qquad
\epsilon^{21}=-1,
\qquad
\psi_a=\epsilon_{ab}\psi^b,
\qquad
\psi^a=\epsilon^{ab}\psi_b,
$$

The same epsilon convention is used for dotted indices.  The independent
dotted gaugino coordinates are \(\widetilde\lambda^{\dot a}\), with
\(\widetilde\lambda_{\dot a}:=
\epsilon_{\dot a\dot b}\widetilde\lambda^{\dot b}\); their cotangent
coordinates are \(\widetilde\lambda^*_{\dot a}\).

$$
\sigma^1=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad
\sigma^2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\quad
\sigma^3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

$$
\sigma_E^m=(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf1_2),
\qquad
\bar\sigma_E^m=(i\sigma^1,i\sigma^2,i\sigma^3,\mathbf1_2),
$$

$$
\sigma_E^{mn}
:=\frac14(\sigma_E^m\bar\sigma_E^n
-\sigma_E^n\bar\sigma_E^m),
\qquad
\sigma_E^m\bar\sigma_E^n+\sigma_E^n\bar\sigma_E^m
=2\delta^{mn}\mathbf1_2.
\tag{4D.7a}
$$

The supertranslation algebra and its coordinate representation are

$$
\{Q_a^E,Q_b^E\}=0,
\qquad
\{\bar Q_{\dot a}^E,\bar Q_{\dot b}^E\}=0,
\qquad
\{Q_a^E,\bar Q_{\dot b}^E\}
=-2(\sigma_E^m)_{a\dot b}P_m^E,
\qquad
\mathsf P_m^E=-\partial_m.
\tag{4D.7b}
$$

For a purely chiral constant parameter \(\varepsilon^a\), the complete
off-shell transformations used below are

$$
\boxed{
\begin{aligned}
\delta_\varepsilon A_m
&=\varepsilon^a(\sigma_E^m)_{a\dot b}
\widetilde\lambda^{\dot b},\\
\delta_\varepsilon\widetilde\lambda^{\dot a}&=0,\\
\delta_\varepsilon\lambda_a
&=-(\sigma_E^{mn})_a{}^b\varepsilon_bF_{mn}
-i\varepsilon_a\mathscr D,\\
\delta_\varepsilon\mathscr D
&=-i\varepsilon^a(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{\dot b}.
\end{aligned}}
\tag{4D.7c}
$$

Set \(\epsilon_E^{1234}=+1\), \(g\in\mathbb C^\times\), and
\(k\in\mathbb C\).  The fermion contraction and Euclidean component action
are

$$
\widetilde\lambda\bar\sigma_E^m\mathcal D_m\lambda
:=\widetilde\lambda_{\dot a}
(\bar\sigma_E^m)^{\dot a a}\mathcal D_m\lambda_a,
$$

$$
\boxed{
S_E^{(1)}
=\int d^4x_E\,\operatorname{tr}_\kappa\left\{
g^{-2}\left[
\frac14F_{mn}F_{mn}
+\widetilde\lambda\bar\sigma_E^m\mathcal D_m\lambda
-\frac12\mathscr D^2\right]
-\frac{ik}{8}\epsilon_E^{mnrs}F_{mn}F_{rs}
\right\}.}
\tag{4D.7d}
$$

All fields are complexified.  The proof is on the trivial
\(G_{\mathbb C}\)-bundle over \(\mathbb R^4\), and the connection and every
variation have compact support.  Hence every displayed integration by parts
has zero boundary term.  No Euclidean reality contour is imposed.

### 4D.2 Nilpotent charge and exact antiholomorphic translations

Choose

$$
Q:=Q^E_1,
\qquad
\varepsilon^1=1,
\qquad
\varepsilon^2=0,
\qquad
\bar\varepsilon_{\dot1}=\bar\varepsilon_{\dot2}=0.
\tag{4D.8}
$$

Since \(\epsilon_{21}=+1\), lowering the parameter gives

$$
\varepsilon_1=\epsilon_{11}\varepsilon^1
+\epsilon_{12}\varepsilon^2=0,
\qquad
\varepsilon_2=\epsilon_{21}\varepsilon^1
+\epsilon_{22}\varepsilon^2=1.
\tag{4D.9}
$$

The first rows of all Euclidean sigma matrices are

$$
\begin{array}{c|cccc}
m&1&2&3&4\\ \hline
(\sigma_E^m)_{1\dot1}&0&0&-i&1\\
(\sigma_E^m)_{1\dot2}&-i&-1&0&0.
\end{array}
\tag{4D.10}
$$

Using \(\{Q^E_a,\bar Q^E_{\dot b}\}
=-2(\sigma_E^m)_{a\dot b}P_m^E\),

$$
\begin{aligned}
\{Q,\bar Q^E_{\dot1}\}
&=-2(-iP_3^E+P_4^E)
=4i\,\frac12(P_3^E+iP_4^E)
=4iP_{\bar2},\\
\{Q,\bar Q^E_{\dot2}\}
&=-2(-iP_1^E-P_2^E)
=4i\,\frac12(P_1^E-iP_2^E)
=4iP_{\bar1}.
\end{aligned}
\tag{4D.11}
$$

Because \(\mathsf P_m^E=-\partial_m\), the coordinate operators obey

$$
\boxed{
\{\mathsf Q,\bar{\mathsf Q}^E_{\dot1}\}
=-4i\partial_{\bar2},
\qquad
\{\mathsf Q,\bar{\mathsf Q}^E_{\dot2}\}
=-4i\partial_{\bar1}.}
\tag{4D.12}
$$

For chiral and antichiral parameters set
\(\delta_\varepsilon:=\varepsilon^aQ_a^E\),
\(\delta_{\bar\varepsilon}:=
\bar\varepsilon^{\dot a}\bar Q_{\dot a}^E\), and
\(v^n:=-2\varepsilon^a(\sigma_E^n)_{a\dot b}
\bar\varepsilon^{\dot b}\).  On the connection, gauge-covariant closure
expands the same operator into a translation and a field-dependent gauge
transformation:

$$
[\delta_\varepsilon,\delta_{\bar\varepsilon}]A_m
=v^nF_{nm}
=v^n\partial_nA_m+\mathcal D_m(-v^nA_n).
\tag{4D.12a}
$$

Thus (4D.12) is an equality on gauge-invariant functionals and on the BV
quotient; the gauge term is retained by the ghost sector below.

The pure-chiral algebra (4D.7b) also gives

$$
\boxed{Q^2=\frac12\{Q^E_1,Q^E_1\}=0.}
\tag{4D.13}
$$

### 4D.3 Complete component \(Q\)-differential

Substitution of (4D.8)--(4D.10) into (4D.7c) gives

$$
\begin{aligned}
QA_1&=-i\widetilde\lambda^{\dot2},
&QA_2&=-\widetilde\lambda^{\dot2},\\
QA_3&=-i\widetilde\lambda^{\dot1},
&QA_4&=+\widetilde\lambda^{\dot1}.
\end{aligned}
\tag{4D.14}
$$

Therefore

$$
\boxed{
\begin{aligned}
QA_{z^1}&=-i\widetilde\lambda^{\dot2},
&QA_{\bar1}&=0,\\
QA_{z^2}&=-i\widetilde\lambda^{\dot1},
&QA_{\bar2}&=0,\\
Q\widetilde\lambda^{\dot1}&=0,
&Q\widetilde\lambda^{\dot2}&=0.
\end{aligned}}
\tag{4D.15}
$$

The six independent antisymmetric matrices are

$$
\begin{gathered}
\sigma_E^{12}=\frac i2\sigma^3,
\qquad
\sigma_E^{13}=-\frac i2\sigma^2,
\qquad
\sigma_E^{23}=\frac i2\sigma^1,\\
\sigma_E^{14}=-\frac i2\sigma^1,
\qquad
\sigma_E^{24}=-\frac i2\sigma^2,
\qquad
\sigma_E^{34}=-\frac i2\sigma^3.
\end{gathered}
\tag{4D.16}
$$

Since both orders of \((m,n)\) occur in
\(\sigma_E^{mn}F_{mn}\),

$$
\sigma_E^{mn}F_{mn}
=i\left[
\sigma^3(F_{12}-F_{34})
+\sigma^1(F_{23}-F_{14})
-\sigma^2(F_{13}+F_{24})
\right].
\tag{4D.17}
$$

Multiplying (4D.17) by \(\varepsilon_b=(0,1)\) gives

$$
\boxed{
\begin{aligned}
Q\lambda_1
&=F_{13}+F_{24}+iF_{14}-iF_{23}
=4F_{\bar1\bar2},\\
Q\lambda_2
&=i(F_{12}-F_{34})-i\mathscr D.
\end{aligned}}
\tag{4D.18}
$$

Here

$$
\begin{aligned}
F_{\bar1\bar2}
&=\frac14(F_{13}+F_{24}+iF_{14}-iF_{23}),\\
F_{z^1z^2}
&=\frac14(F_{13}+F_{24}-iF_{14}+iF_{23}),\\
F_{z^1\bar1}&=-\frac i2F_{12},
\qquad
F_{z^2\bar2}=+\frac i2F_{34}.
\end{aligned}
\tag{4D.19}
$$

Define the invertible auxiliary coordinate

$$
Z:=F_{12}-F_{34}
=2i(F_{z^1\bar1}+F_{z^2\bar2}),
\qquad
H:=\mathscr D-Z.
\tag{4D.20}
$$

Then

$$
Q\lambda_2=-iH.
\tag{4D.21}
$$

The remaining variations are

$$
\begin{aligned}
QF_{z^1\bar1}
&=\mathcal D_{z^1}(QA_{\bar1})
-\mathcal D_{\bar1}(QA_{z^1})
=i\mathcal D_{\bar1}\widetilde\lambda^{\dot2},\\
QF_{z^2\bar2}
&=\mathcal D_{z^2}(QA_{\bar2})
-\mathcal D_{\bar2}(QA_{z^2})
=i\mathcal D_{\bar2}\widetilde\lambda^{\dot1},\\
QZ
&=2i\left(
i\mathcal D_{\bar1}\widetilde\lambda^{\dot2}
+i\mathcal D_{\bar2}\widetilde\lambda^{\dot1}
\right)\\
&=-2\left(
\mathcal D_{\bar1}\widetilde\lambda^{\dot2}
+\mathcal D_{\bar2}\widetilde\lambda^{\dot1}
\right)
=Q\mathscr D,\\
QH&=Q\mathscr D-QZ=0.
\end{aligned}
\tag{4D.22}
$$

Off-shell nilpotence now holds component by component:

$$
\begin{gathered}
Q^2A_{\bar i}=0,
\qquad
Q^2A_{z^1}=-iQ\widetilde\lambda^{\dot2}=0,
\qquad
Q^2A_{z^2}=-iQ\widetilde\lambda^{\dot1}=0,\\
Q^2\lambda_1=4QF_{\bar1\bar2}=0,
\qquad
Q^2\lambda_2=-iQH=0,\\
Q^2\mathscr D
=-2Q\left(
\mathcal D_{\bar1}\widetilde\lambda^{\dot2}
+\mathcal D_{\bar2}\widetilde\lambda^{\dot1}
\right),\\
Q(\mathcal D_{\bar i}\widetilde\lambda)
=\mathcal D_{\bar i}(Q\widetilde\lambda)
+(QA_{\bar i})\times\widetilde\lambda
=0,\\
Q^2\mathscr D=0.
\end{gathered}
\tag{4D.23}
$$

### 4D.4 Component minimal BV theory

Introduce the single residual component gauge ghost \(c=c^AT_A\).
The field and antifield ledger is

$$
\begin{array}{c|ccccc}
X&A_m&\lambda_a&\widetilde\lambda^{\dot a}&\mathscr D&c\\ \hline
\epsilon_X&0&1&1&0&1\\
\operatorname{gh}_{\mathrm{BV}}(X)&0&0&0&0&1\\
\operatorname{gh}_{\mathrm{BV}}(X^*)&-1&-1&-1&-1&-2\\
\epsilon_{X^*}&1&0&0&1&0.
\end{array}
\tag{4D.24}
$$

The ordered odd cotangent form and antibracket are defined by

$$
\omega_{\mathrm{BV}}
=\sum_X\int d^4x_E\,\kappa_{AB}\,
\delta X^{*A}\wedge\delta X^B,
\tag{4D.25}
$$

$$
(F,G)
=\sum_X\int d^4x_E\,\kappa^{AB}
\left[
F\frac{\overleftarrow\delta}{\delta X^A}
\frac{\vec\delta G}{\delta X^{*B}}
-F\frac{\overleftarrow\delta}{\delta X^{*A}}
\frac{\vec\delta G}{\delta X^B}
\right].
\tag{4D.26}
$$

Define the gauge BRST differential by

$$
\boxed{
\mathbf sA_m=\mathcal D_mc,
\qquad
\mathbf sc=ic^2=-\frac12c\times c,
\qquad
\mathbf sX=i\llbracket c,X\rrbracket=-c\times X,}
\tag{4D.27}
$$

for \(X\in\{\lambda,\widetilde\lambda,\mathscr D,F_{mn},H\}\).
The second equality follows from the odd matrix coefficients of \(c\).

For an adjoint covariant field \(X\), the graded Jacobi identity gives

$$
\begin{aligned}
\mathbf s^2X
&=-\mathbf s(c\times X)\\
&=-(\mathbf sc)\times X+c\times(\mathbf sX)\\
&=+\frac12(c\times c)\times X-c\times(c\times X)\\
&=+\frac12(c\times c)\times X
-\frac12(c\times c)\times X=0.
\end{aligned}
\tag{4D.28}
$$

For the connection,

$$
\begin{aligned}
\mathbf s^2A_m
&=\mathbf s(\partial_mc+A_m\times c)\\
&=\partial_m(\mathbf sc)
+(\mathbf sA_m)\times c+A_m\times(\mathbf sc)\\
&=\mathcal D_m\left(-\frac12c\times c\right)
+(\mathcal D_mc)\times c\\
&=-\frac12\left[
(\mathcal D_mc)\times c+c\times(\mathcal D_mc)
\right]+(\mathcal D_mc)\times c\\
&=-(\mathcal D_mc)\times c+(\mathcal D_mc)\times c=0.
\end{aligned}
\tag{4D.29}
$$

The same Jacobi calculation gives \(\mathbf s^2c=0\).  In the
displayed matrix order,

$$
\mathbf s^2c
=i\left[(ic^2)c-c(ic^2)\right]
=-c^2c+cc^2=0.
\tag{4D.29a}
$$

The component minimal master action is therefore

$$
\boxed{
\begin{aligned}
S_{\min,E}^{\mathrm{comp}}
=S_E^{(1)}+\int d^4x_E\,\operatorname{tr}_\kappa\Big[
&A^{*m}\mathbf sA_m
-\lambda^{*a}\mathbf s\lambda_a
-\widetilde\lambda^*_{\dot a}\mathbf s\widetilde\lambda^{\dot a}\\
&+\mathscr D^*\mathbf s\mathscr D
-c^*\mathbf sc\Big].
\end{aligned}}
\tag{4D.30}
$$

Gauge invariance and (4D.28)--(4D.29) give

$$
\frac12(S_{\min,E}^{\mathrm{comp}},
S_{\min,E}^{\mathrm{comp}})
=\mathbf sS_E^{(1)}
+\sum_X(-1)^{\epsilon_X}X^*\mathbf s^2X=0.
\tag{4D.31}
$$

This is a direct component BV definition.  It does not assert a canonical
reduction from the unconstrained superfield BV coordinates of Step 3D.

### 4D.5 \(U(1)_R\) derivation and twisted degree

Assign

$$
r(A_m)=r(\mathscr D)=r(c)=0,
\qquad
r(\lambda)=+1,
\qquad
r(\widetilde\lambda)=-1.
\tag{4D.32}
$$

Every bosonic term of (4D.7d) has charge zero, and

$$
r(\widetilde\lambda\bar\sigma^m\mathcal D_m\lambda)
=-1+0+1=0.
\tag{4D.33}
$$

Thus (4D.32) is a symmetry of the pure component action.  Equations
(4D.15), (4D.18), and (4D.22) determine the charge of \(Q\):

$$
\begin{aligned}
r(Q)+r(A_z)&=r(\widetilde\lambda)=-1,\\
r(Q)+r(\lambda)&=r(F)=0,\\
r(Q)+r(\mathscr D)&=r(\mathcal D\widetilde\lambda)=-1,
\end{aligned}
\qquad
\boxed{r(Q)=-1.}
\tag{4D.34}
$$

Set

$$
r(X^*)=-r(X),
\qquad
\deg_{\mathrm{HT}}X
:=\operatorname{gh}_{\mathrm{BV}}(X)-r(X).
\tag{4D.35}
$$

Then

$$
\begin{array}{c|cccccccccc}
X&c&A_m&\lambda&\widetilde\lambda&\mathscr D
&c^*&A^*&\lambda^*&\widetilde\lambda^*&\mathscr D^*\\ \hline
\deg_{\mathrm{HT}}X
&1&0&-1&1&0&-2&-1&0&-2&-1.
\end{array}
\tag{4D.36}
$$

Both \(Q\) and \(\mathbf s\) have twisted degree \(+1\), and every
field in (4D.36) has parity equal to its twisted degree modulo two.

### 4D.6 Combined twisted BV differential

Extend \(Q\) by

$$
Qc=0.
\tag{4D.37}
$$

For a covariant field \(X\),

$$
\begin{aligned}
(\mathbf sQ+Q\mathbf s)X
&=-c\times QX+Q(-c\times X)\\
&=-c\times QX-(Qc)\times X+c\times QX=0.
\end{aligned}
\tag{4D.38}
$$

For the connection,

$$
\begin{aligned}
(\mathbf sQ+Q\mathbf s)A_m
&=-c\times QA_m+Q(\partial_mc+A_m\times c)\\
&=-c\times QA_m+(QA_m)\times c+A_m\times Qc\\
&=-c\times QA_m+c\times QA_m=0,
\end{aligned}
\tag{4D.39}
$$

because \(QA_m\) and \(c\) are both odd.  Hence

$$
\boxed{\delta:=\mathbf s+Q,
\qquad
\delta^2=\mathbf s^2+(\mathbf sQ+Q\mathbf s)+Q^2=0.}
\tag{4D.40}
$$

The complete twisted master action is

$$
\boxed{
S_{\mathrm{tw}}
:=S_E^{(1)}
+\sum_X\int d^4x_E\,
(-1)^{\epsilon_X}\operatorname{tr}_\kappa(X^*\delta X).}
\tag{4D.41}
$$

For every antifield, its differential is fixed without an omitted rule:

$$
\delta X^*:=(S_{\mathrm{tw}},X^*)
=\frac{\overleftarrow\delta S_E^{(1)}}{\delta X}
+\sum_Y(-1)^{\epsilon_Y}Y^*
\frac{\overleftarrow\delta(\delta Y)}{\delta X}.
\tag{4D.42}
$$

Equations (4D.40) and \(\delta S_E^{(1)}=0\) give

$$
\frac12(S_{\mathrm{tw}},S_{\mathrm{tw}})
=\delta S_E^{(1)}
+\sum_X(-1)^{\epsilon_X}X^*\delta^2X=0.
\tag{4D.43}
$$

### 4D.7 Exact \(Q\)-primitive of the Euclidean action

Write \(\mathfrak h_{AB}=g^{-2}\kappa_{AB}\) and
\(\mathfrak k_{AB}=k\kappa_{AB}\).  Define

$$
P:=F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23}
=\frac18\epsilon_E^{mnrs}F_{mn}F_{rs},
\tag{4D.44}
$$

and the degree-minus-one gauge-invariant functional

$$
\boxed{
\Psi_0
:=\int d^4x_E\,\operatorname{tr}_\kappa\left[
2\lambda_1F_{z^1z^2}
-i\lambda_2\left(Z+\frac12H\right)
\right].}
\tag{4D.45}
$$

The first term varies as

$$
\begin{aligned}
Q(2\lambda_1F_{z^1z^2})
&=2(Q\lambda_1)F_{z^1z^2}
-2\lambda_1QF_{z^1z^2}\\
&=8F_{\bar1\bar2}F_{z^1z^2}
+2i\lambda_1\left(
\mathcal D_{z^1}\widetilde\lambda^{\dot1}
-\mathcal D_{z^2}\widetilde\lambda^{\dot2}
\right).
\end{aligned}
\tag{4D.46}
$$

The second term varies as

$$
\begin{aligned}
Q\left[-i\lambda_2\left(Z+\frac12H\right)\right]
={}&-i(Q\lambda_2)\left(Z+\frac12H\right)
+i\lambda_2\left(QZ+\frac12QH\right)\\
={}&-HZ-\frac12H^2
-2i\lambda_2\left(
\mathcal D_{\bar1}\widetilde\lambda^{\dot2}
+\mathcal D_{\bar2}\widetilde\lambda^{\dot1}
\right).
\end{aligned}
\tag{4D.47}
$$

For the bosonic terms, set

$$
X:=F_{13}+F_{24},
\qquad
Y:=F_{14}-F_{23}.
\tag{4D.48}
$$

Inside \(\operatorname{tr}_\kappa\), symmetry of \(\kappa\) gives

$$
\begin{aligned}
8F_{\bar1\bar2}F_{z^1z^2}
&=8\frac{X+iY}{4}\frac{X-iY}{4}\\
&=\frac12X^2+\frac12Y^2\\
&=\frac12F_{13}^2+\frac12F_{24}^2+F_{13}F_{24}
+\frac12F_{14}^2+\frac12F_{23}^2-F_{14}F_{23},\\
-HZ-\frac12H^2
&=-(\mathscr D-Z)Z-\frac12(\mathscr D-Z)^2\\
&=-\mathscr DZ+Z^2-\frac12\mathscr D^2
+\mathscr DZ-\frac12Z^2\\
&=\frac12F_{12}^2+\frac12F_{34}^2-F_{12}F_{34}
-\frac12\mathscr D^2.
\end{aligned}
\tag{4D.49}
$$

Adding the two lines gives

$$
8F_{\bar1\bar2}F_{z^1z^2}
-HZ-\frac12H^2
=\frac14F_{mn}F_{mn}-\frac12\mathscr D^2-P.
\tag{4D.50}
$$

Raising \(\lambda^1=\lambda_2\), \(\lambda^2=-\lambda_1\), and
using (4D.3) gives the complete fermionic expansion

$$
\begin{aligned}
\lambda^a(\sigma_E^m)_{a\dot b}
\mathcal D_m\widetilde\lambda^{\dot b}
={}&2i\lambda_1\left(
\mathcal D_{z^1}\widetilde\lambda^{\dot1}
-\mathcal D_{z^2}\widetilde\lambda^{\dot2}
\right)\\
&-2i\lambda_2\left(
\mathcal D_{\bar1}\widetilde\lambda^{\dot2}
+\mathcal D_{\bar2}\widetilde\lambda^{\dot1}
\right).
\end{aligned}
\tag{4D.51}
$$

The exact integration-by-parts identity is

$$
\lambda\sigma_E^m\mathcal D_m\widetilde\lambda
=\partial_m(\lambda\sigma_E^m\widetilde\lambda)
+\widetilde\lambda\bar\sigma_E^m\mathcal D_m\lambda.
\tag{4D.52}
$$

The compact-support condition removes its first term after integration.
Equations (4D.46)--(4D.52) therefore give

$$
\boxed{
Q\Psi_0
=\int d^4x_E\,\operatorname{tr}_\kappa\left[
\frac14F_{mn}F_{mn}
+\widetilde\lambda\bar\sigma_E^m\mathcal D_m\lambda
-\frac12\mathscr D^2-P
\right].}
\tag{4D.53}
$$

The action (4D.7d) becomes

$$
S_E^{(1)}
=g^{-2}Q\Psi_0
+(g^{-2}-ik)\int d^4x_E\,\operatorname{tr}_\kappa P.
\tag{4D.54}
$$

Set \(C:=A\times A\), so \(F=dA+\tfrac12C\).  Graded cyclicity
and trace invariance give the following.  The first line is the graded
Jacobi identity with all three inputs equal to the degree-one form \(A\):

$$
\begin{aligned}
0
&=-A\times(A\times A)-A\times(A\times A)
-A\times(A\times A),\\
A\times C&=A\times(A\times A)=0,\\
\operatorname{tr}_\kappa(C\wedge C)
&=\langle A\times A,C\rangle_\kappa
=\langle A,A\times C\rangle_\kappa=0,\\
\operatorname{tr}_\kappa(dA\wedge C)
&=\operatorname{tr}_\kappa(C\wedge dA),\\
\operatorname{tr}_\kappa(dA\wedge C)
&=-\operatorname{tr}_\kappa\left[
A\wedge(dA\times A)\right]
=\operatorname{tr}_\kappa\left[
A\wedge(A\times dA)\right],\\
\operatorname{tr}_\kappa(F\wedge F)
&=\operatorname{tr}_\kappa(dA\wedge dA)
+\frac12\operatorname{tr}_\kappa(dA\wedge C)
+\frac12\operatorname{tr}_\kappa(C\wedge dA)
+\frac14\operatorname{tr}_\kappa(C\wedge C)\\
&=\operatorname{tr}_\kappa(dA\wedge dA)
+\operatorname{tr}_\kappa(dA\wedge C),\\
d\,\operatorname{tr}_\kappa\left[
A\wedge dA+\frac13A\wedge C\right]
&=\operatorname{tr}_\kappa(dA\wedge dA)\\
&\quad+\frac13\operatorname{tr}_\kappa\left[
dA\wedge C-A\wedge(dA\times A-A\times dA)
\right]\\
&=\operatorname{tr}_\kappa(dA\wedge dA)
+\frac13\left[1+1+1\right]
\operatorname{tr}_\kappa(dA\wedge C)\\
&=\operatorname{tr}_\kappa(F\wedge F).
\end{aligned}
\tag{4D.55}
$$

and

$$
\operatorname{tr}_\kappa(P)d^4x_E
=\frac12\operatorname{tr}_\kappa(F\wedge F).
\tag{4D.56}
$$

Compact support and Stokes' theorem now give the exact equality

$$
\int_{\mathbb R^4}d^4x_E\,\operatorname{tr}_\kappa P=0,
\qquad
\boxed{S_E^{(1)}=g^{-2}Q\Psi_0.}
\tag{4D.57}
$$

### 4D.8 First canonical transformation

For the right functional derivative used in (4D.26), fix the ordered
field-space one-form and its contraction with the odd vector \(\delta\) by

$$
d_{\mathrm{fld}}\Psi_0
:=\sum_X\int\operatorname{tr}_\kappa\left(
\frac{\overrightarrow\delta\Psi_0}{\delta X}
d_{\mathrm{fld}}X\right),
\qquad
\iota_\delta d_{\mathrm{fld}}\Psi_0
:=\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa\left(
\frac{\overrightarrow\delta\Psi_0}{\delta X}\delta X\right)
=\delta\Psi_0.
\tag{4D.58}
$$

Define the shifted antifields and the unweighted super-Darboux potential by

$$
X^*:=\widehat X^*-g^{-2}
\frac{\overrightarrow\delta\Psi_0}{\delta X},
\qquad
\Theta_{\mathrm{BV}}
:=\sum_X\int\operatorname{tr}_\kappa
(X^*d_{\mathrm{fld}}X).
\tag{4D.59}
$$

Then

$$
\Theta_{\mathrm{BV}}
=\sum_X\int\operatorname{tr}_\kappa
(\widehat X^*d_{\mathrm{fld}}X)
-g^{-2}d_{\mathrm{fld}}\Psi_0,
\qquad
\omega_{\mathrm{BV}}=d_{\mathrm{fld}}\Theta_{\mathrm{BV}}
=\sum_X\int\operatorname{tr}_\kappa
(d_{\mathrm{fld}}\widehat X^*\wedge d_{\mathrm{fld}}X).
\tag{4D.60}
$$

This is the same unweighted odd form as (4D.25), so the shift is
odd-symplectic.  The factor \((-1)^{\epsilon_X}\) occurs only in the
cotangent Hamiltonian and in the contraction convention (4D.58).

For any two adjoint fields \(U,V\) occurring in (4D.45), the graded
Leibniz rule and trace invariance give

$$
\begin{aligned}
\mathbf s\operatorname{tr}_\kappa(UV)
&=\operatorname{tr}_\kappa\left[
i\llbracket c,U\rrbracket V
+(-1)^{\epsilon_U}U\,i\llbracket c,V\rrbracket
\right]\\
&=i\operatorname{tr}_\kappa\llbracket c,UV\rrbracket=0.
\end{aligned}
\qquad
\mathbf s\Psi_0=0,
\qquad
\delta\Psi_0=Q\Psi_0.
\tag{4D.61}
$$

Substitution of (4D.59) into the master action gives

$$
\begin{aligned}
S_{\mathrm{tw}}
={}&g^{-2}Q\Psi_0
+\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa\left[
\left(\widehat X^*-g^{-2}
\frac{\overrightarrow\delta\Psi_0}{\delta X}\right)\delta X
\right]\\
={}&g^{-2}Q\Psi_0
+\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa(\widehat X^*\delta X)
-g^{-2}\iota_\delta d_{\mathrm{fld}}\Psi_0\\
={}&g^{-2}Q\Psi_0
+\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa(\widehat X^*\delta X)
-g^{-2}Q\Psi_0\\
&=\boxed{\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa(\widehat X^*\delta X)}.
\end{aligned}
\tag{4D.62}
$$

Thus the classical action has been removed by a canonical cotangent shift,
not by deleting it from the path integral.

### 4D.9 Triangular field coordinates

Define the horizontal variables

$$
c,
\qquad
A_{\bar1},
\qquad
A_{\bar2},
\qquad
\alpha:=-\frac14\lambda_1,
\tag{4D.63}
$$

and vertical variables

$$
u_1:=A_{z^1},
\qquad
u_2:=A_{z^2},
\qquad
w:=\lambda_2,
\tag{4D.64}
$$

$$
\begin{aligned}
\eta_1&:=\delta u_1
=\mathcal D_{z^1}c-i\widetilde\lambda^{\dot2},\\
\eta_2&:=\delta u_2
=\mathcal D_{z^2}c-i\widetilde\lambda^{\dot1},\\
K&:=\delta w
=i\llbracket c,w\rrbracket-iH.
\end{aligned}
\tag{4D.65}
$$

This field map is invertible.  Its inverse is

$$
\begin{aligned}
\lambda_1&=-4\alpha,
&\widetilde\lambda^{\dot2}
&=i(\eta_1-\mathcal D_{z^1}c),\\
\widetilde\lambda^{\dot1}
&=i(\eta_2-\mathcal D_{z^2}c),
&H&=\llbracket c,w\rrbracket+iK,\\
\mathscr D&=Z+\llbracket c,w\rrbracket+iK.
\end{aligned}
\tag{4D.66}
$$

The horizontal differential is

$$
\boxed{
\begin{aligned}
\delta c&=ic^2=-\frac12c\times c,\\
\delta A_{\bar i}&=\mathcal D_{\bar i}c,\\
\delta\alpha
&=i\llbracket c,\alpha\rrbracket-F_{\bar1\bar2}
=-c\times\alpha-F_{\bar1\bar2}.
\end{aligned}}
\tag{4D.67}
$$

It contains no vertical variable.  The vertical differential is

$$
\boxed{
\delta u_i=\eta_i,
\qquad
\delta\eta_i=0,
\qquad
\delta w=K,
\qquad
\delta K=0.}
\tag{4D.68}
$$

The two zeroes in (4D.68) are not assumptions:

$$
\delta\eta_i=\delta^2u_i=0,
\qquad
\delta K=\delta^2w=0,
\tag{4D.69}
$$

by the three separately proved terms in (4D.40).

Let \(X\) denote the old field coordinates after (4D.59), and let
\(Y=F(X)\) denote the complete list (4D.63)--(4D.65).  Their
unweighted super-Darboux potentials are

$$
\Theta_X:=\sum_I\int\operatorname{tr}_\kappa
(\widehat X_I^*d_{\mathrm{fld}}X^I),
\qquad
\Theta_Y:=\sum_I\int\operatorname{tr}_\kappa
(Y_I^*d_{\mathrm{fld}}Y^I).
\tag{4D.70}
$$

The cotangent lift is defined, with no omitted parity factor, by

$$
Y^I=F^I(X),
\qquad
\widehat X_I^*=(dF_X)^\vee{}_I{}^JY_J^*,
\qquad
\boxed{\Theta_X=\Theta_Y}.
\tag{4D.71}
$$

The complete field-space differentials entering the Frechet transpose are

$$
\begin{aligned}
d_{\mathrm{fld}}\alpha
&=-\frac14d_{\mathrm{fld}}\lambda_1,\\
d_{\mathrm{fld}}\eta_i
&=\mathcal D_{z^i}d_{\mathrm{fld}}c
+(d_{\mathrm{fld}}u_i)\times c
-i\,d_{\mathrm{fld}}\widetilde\lambda^{\dot\jmath(i)},\\
d_{\mathrm{fld}}Z
&=2i\sum_{i=1}^2\left[
\mathcal D_{z^i}d_{\mathrm{fld}}A_{\bar i}
-\mathcal D_{\bar i}d_{\mathrm{fld}}u_i
\right],\\
d_{\mathrm{fld}}K
&=i\llbracket d_{\mathrm{fld}}c,w\rrbracket
+i\llbracket c,d_{\mathrm{fld}}w\rrbracket
-i\,d_{\mathrm{fld}}\mathscr D
+i\,d_{\mathrm{fld}}Z,
\end{aligned}
\qquad
\dot\jmath(1)=\dot2,
\quad
\dot\jmath(2)=\dot1.
\tag{4D.72}
$$

Equating the coefficient of every independent \(d_{\mathrm{fld}}X^I\)
in (4D.71)--(4D.72) fixes all derivative-transpose mixing.  The
compact-support transpose and the three graded invariant-pairing identities
needed for this calculation are

$$
\begin{aligned}
\int\operatorname{tr}_\kappa(\rho\,\mathcal D_i\xi)
&=-\int\operatorname{tr}_\kappa((\mathcal D_i\rho)\xi),\\
\int\operatorname{tr}_\kappa(\eta_i^*[(d_{\mathrm{fld}}u_i)\times c])
&=\int\operatorname{tr}_\kappa[(c\times\eta_i^*)d_{\mathrm{fld}}u_i],\\
\int\operatorname{tr}_\kappa(K^*i\llbracket d_{\mathrm{fld}}c,w\rrbracket)
&=-\int\operatorname{tr}_\kappa[(w\times K^*)d_{\mathrm{fld}}c],\\
\int\operatorname{tr}_\kappa(K^*i\llbracket c,d_{\mathrm{fld}}w\rrbracket)
&=-\int\operatorname{tr}_\kappa[(c\times K^*)d_{\mathrm{fld}}w].
\end{aligned}
\tag{4D.72a}
$$

Indeed, the \(K^*i\,d_{\mathrm{fld}}Z\) term is

$$
\begin{aligned}
\int\operatorname{tr}_\kappa(K^*i\,d_{\mathrm{fld}}Z)
&=\sum_{i=1}^2\int\operatorname{tr}_\kappa\left[
-2K^*\mathcal D_{z^i}d_{\mathrm{fld}}A_{\bar i}
+2K^*\mathcal D_{\bar i}d_{\mathrm{fld}}u_i\right]\\
&=\sum_{i=1}^2\int\operatorname{tr}_\kappa\left[
2(\mathcal D_{z^i}K^*)d_{\mathrm{fld}}A_{\bar i}
-2(\mathcal D_{\bar i}K^*)d_{\mathrm{fld}}u_i\right].
\end{aligned}
\tag{4D.72b}
$$

Therefore every nontrivial old shifted antifield is

$$
\boxed{
\begin{aligned}
\widehat c^*
&=c^*-\mathcal D_{z^1}\eta_1^*
-\mathcal D_{z^2}\eta_2^*-w\times K^*,\\
\widehat A_{\bar i}^*
&=A_{\bar i}^*+2\mathcal D_{z^i}K^*,\\
\widehat u_i^*
&=u_i^*+c\times\eta_i^*-2\mathcal D_{\bar i}K^*,\\
\widehat w^*&=w^*-c\times K^*,\\
\widehat\lambda^{*1}&=-\frac14\alpha^*,\\
\widehat{\widetilde\lambda}^*_{\dot2}&=-i\eta_1^*,\\
\widehat{\widetilde\lambda}^*_{\dot1}&=-i\eta_2^*,\\
\widehat{\mathscr D}^{*}&=-iK^*,\\
d_{\mathrm{fld}}\Theta_X&=d_{\mathrm{fld}}\Theta_Y.
\end{aligned}}
\tag{4D.73}
$$

Thus the nonlinear, derivative-dependent map has been lifted canonically;
raw antifields are never identified with transformed antifields.

Contracting the now explicit equality \(\Theta_X=\Theta_Y\) with the
vector field (4D.67)--(4D.69) gives, coefficient by coefficient,

$$
\begin{aligned}
\sum_X(-1)^{\epsilon_X}\widehat X^*\delta X
&=\sum_Y(-1)^{\epsilon_Y}Y^*\delta Y\\
&=-c^*\left(-\frac12c\times c\right)
+A_{\bar1}^*\mathcal D_{\bar1}c
+A_{\bar2}^*\mathcal D_{\bar2}c\\
&\quad-\alpha^*(-c\times\alpha-F_{\bar1\bar2})
+u_1^*\eta_1+u_2^*\eta_2-w^*K\\
&\quad-\eta_1^*\,0-\eta_2^*\,0+K^*\,0.
\end{aligned}
\tag{4D.73a}
$$

Using \(\alpha^*=-4B\), the first line of fields in (4D.73a) is
\(S_{\mathrm{hor}}\), and the second is \(S_{\mathrm{ctr}}\).  Thus

$$
\boxed{S_{\mathrm{tw}}=S_{\mathrm{hor}}+S_{\mathrm{ctr}},}
\tag{4D.74}
$$

where, in the transformed antifields,

$$
\boxed{
\begin{aligned}
S_{\mathrm{hor}}
=\int d^4x_E\,\operatorname{tr}_\kappa\Big[
&A_{\bar1}^*\mathcal D_{\bar1}c
+A_{\bar2}^*\mathcal D_{\bar2}c
-c^*ic^2\\
&+4B\left(i\llbracket c,\alpha\rrbracket
-F_{\bar1\bar2}\right)\Big],
\qquad
B:=\widehat\lambda^{*1}=-\frac14\alpha^*,
\end{aligned}}
\tag{4D.75}
$$

$$
\boxed{
S_{\mathrm{ctr}}
=\int d^4x_E\,\operatorname{tr}_\kappa\left[
u_1^*\eta_1+u_2^*\eta_2-w^*K
\right].}
\tag{4D.76}
$$

Every un-hatted star in (4D.75)--(4D.76) is a final \(Y\)-cotangent
coordinate.  The coefficient \(B\) is the same horizontal coordinate written
in the intermediate chart as
\(B=\widehat\lambda^{*1}\) and in the final chart as
\(B=-\alpha^*/4\).  No raw antifield from (4D.30) occurs in these formulas.

### 4D.10 Exact holomorphic-BF packaging

The horizontal degrees are

$$
\begin{array}{c|ccc|ccc}
X&c&A_{\bar i}&\alpha&B&A_{\bar i}^*&c^*\\ \hline
\deg_{\mathrm{HT}}X&1&0&-1&0&-1&-2.
\end{array}
\tag{4D.77}
$$

Package them as

$$
\boxed{
\mathcal A
:=c+A_{\bar1}d\bar z^{\bar1}
+A_{\bar2}d\bar z^{\bar2}
+\alpha\,d\bar z^{\bar1}\wedge d\bar z^{\bar2}
\in\Omega^{0,*}(\mathbb C^2,\mathfrak g_{\mathbb C})[1],}
\tag{4D.78}
$$

$$
\boxed{
\begin{aligned}
\mathcal B:={}&B\Omega\\
&+\Omega\wedge\left(
-\frac14A_{\bar2}^*d\bar z^{\bar1}
+\frac14A_{\bar1}^*d\bar z^{\bar2}
\right)\\
&-\frac14c^*\Omega\wedge
d\bar z^{\bar1}\wedge d\bar z^{\bar2}
\in\Omega^{2,*}(\mathbb C^2,\mathfrak g_{\mathbb C}^*).
\end{aligned}}
\tag{4D.79}
$$

The shift convention is

$$
\deg_{\mathrm{HT}}\mathcal A^{0,q}=1-q,
\qquad
\deg_{\mathrm{HT}}\mathcal B^{2,q}=-q.
\tag{4D.80}
$$

For complementary antiholomorphic degrees,

$$
(1-q)+[-(2-q)]=-1,
\tag{4D.81}
$$

so the pairing has BV degree \(-1\).  Direct use of (4D.6) gives

$$
\begin{aligned}
\omega_{\mathrm{hBF}}
&:=\int_{\mathbb C^2}
\langle\delta\mathcal B\wedge\delta\mathcal A\rangle\\
&=\int d^4x_E\,\operatorname{tr}_\kappa\left[
\delta B\wedge\delta\lambda_1
+\delta A_{\bar1}^*\wedge\delta A_{\bar1}
+\delta A_{\bar2}^*\wedge\delta A_{\bar2}
+\delta c^*\wedge\delta c
\right].
\end{aligned}
\tag{4D.82}
$$

Indeed, the first term is

$$
\int\delta(B\Omega)\wedge
\delta(\alpha\bar\Omega)
=-4\int d^4x_E\,\delta B\wedge\delta\alpha
=\int d^4x_E\,\delta B\wedge\delta\lambda_1,
\tag{4D.83}
$$

because \(\lambda_1=-4\alpha\); the remaining three terms follow by
the same two wedge multiplications in (4D.79).

Define

$$
\bar\partial
:=d\bar z^{\bar1}\partial_{\bar1}
+d\bar z^{\bar2}\partial_{\bar2}.
$$

Define the suspended Dolbeault self-bracket by its complete component
expansion:

$$
\boxed{
\begin{aligned}
\mathfrak F(\mathcal A)
&:=\bar\partial\mathcal A
+\frac12[\mathcal A,\mathcal A]_{\mathrm{sus}}\\
&=\frac12c\times c\\
&\quad+(\mathcal D_{\bar1}c)d\bar z^{\bar1}
+(\mathcal D_{\bar2}c)d\bar z^{\bar2}\\
&\quad+\left(
F_{\bar1\bar2}+c\times\alpha
\right)d\bar z^{\bar1}\wedge d\bar z^{\bar2}.
\end{aligned}}
\tag{4D.84}
$$

This equation fixes every suspension sign; its underlying Lie product is
only the Project product (4D.7).

The holomorphic-BF master action is

$$
\boxed{
S_{\mathrm{hBF}}
:=\int_{\mathbb C^2}
\left\langle\mathcal B\wedge
\left(\bar\partial\mathcal A
+\frac12[\mathcal A,\mathcal A]_{\mathrm{sus}}\right)
\right\rangle.}
\tag{4D.85}
$$

Its three antiholomorphic-degree products are

$$
\begin{aligned}
\mathcal B^{2,0}\wedge\mathfrak F^{0,2}
&=-4\,d^4x_E\,
B(F_{\bar1\bar2}+c\times\alpha),\\
\mathcal B^{2,1}\wedge\mathfrak F^{0,1}
&=d^4x_E\left[
A_{\bar1}^*\mathcal D_{\bar1}c
+A_{\bar2}^*\mathcal D_{\bar2}c
\right],\\
\mathcal B^{2,2}\wedge\mathfrak F^{0,0}
&=\frac12d^4x_E\,c^*(c\times c)
=-d^4x_E\,c^*ic^2.
\end{aligned}
\tag{4D.86}
$$

Since \(i\llbracket c,\alpha\rrbracket=-c\times\alpha\), summing
(4D.86) gives

$$
S_{\mathrm{hBF}}=S_{\mathrm{hor}}.
\tag{4D.87}
$$

Thus the BF \(B\)-field is the transformed antifield
\(B=\widehat\lambda^{*1}=-\alpha^*/4\); it is not inserted as a new
physical field.

### 4D.11 Classical master equation of holomorphic BF

Let \(\delta_{\mathrm h}\) be the horizontal restriction of (4D.67):

$$
\delta_{\mathrm h}c=-\frac12c\times c,
\qquad
\delta_{\mathrm h}A_{\bar i}=\mathcal D_{\bar i}c,
\qquad
\delta_{\mathrm h}\alpha=-c\times\alpha-F_{\bar1\bar2}.
\tag{4D.88}
$$

The ghost and connection squares expand as

$$
\begin{aligned}
\delta_{\mathrm h}^2c
&=-\frac12\left[
(\delta_{\mathrm h}c)\times c
-c\times(\delta_{\mathrm h}c)
\right]\\
&=\frac14\left[
(c\times c)\times c-c\times(c\times c)
\right]=0,\\
\delta_{\mathrm h}^2A_{\bar i}
&=\delta_{\mathrm h}(\partial_{\bar i}c
+A_{\bar i}\times c)\\
&=\mathcal D_{\bar i}\left(-\frac12c\times c\right)
+(\mathcal D_{\bar i}c)\times c\\
&=-\frac12\left[
(\mathcal D_{\bar i}c)\times c
+c\times(\mathcal D_{\bar i}c)
\right]
+(\mathcal D_{\bar i}c)\times c=0.
\end{aligned}
\tag{4D.89}
$$

The curvature is covariant under (4D.88):
\(\delta_{\mathrm h}F_{\bar1\bar2}=-c\times F_{\bar1\bar2}\).
Therefore

$$
\begin{aligned}
\delta_{\mathrm h}^2\alpha
&=-\delta_{\mathrm h}(c\times\alpha)
-\delta_{\mathrm h}F_{\bar1\bar2}\\
&=-(\delta_{\mathrm h}c)\times\alpha
+c\times(\delta_{\mathrm h}\alpha)
+c\times F_{\bar1\bar2}\\
&=\frac12(c\times c)\times\alpha
+c\times(-c\times\alpha-F_{\bar1\bar2})
+c\times F_{\bar1\bar2}\\
&=\frac12(c\times c)\times\alpha
-c\times(c\times\alpha)=0.
\end{aligned}
\tag{4D.90}
$$

The last equality is the same graded Jacobi identity used in (4D.28).
Direct functional differentiation of (4D.75), using
\(\alpha^*=-4B\), gives the remaining four Hamiltonian components:

$$
\boxed{
\begin{aligned}
\delta_{\mathrm h}B
&=-c\times B,\\
\delta_{\mathrm h}A_{\bar1}^*
&=-c\times A_{\bar1}^*-4\mathcal D_{\bar2}B,\\
\delta_{\mathrm h}A_{\bar2}^*
&=-c\times A_{\bar2}^*+4\mathcal D_{\bar1}B,\\
\delta_{\mathrm h}c^*
&=-c\times c^*
-\mathcal D_{\bar1}A_{\bar1}^*
-\mathcal D_{\bar2}A_{\bar2}^*
+4\alpha\times B.
\end{aligned}}
\tag{4D.90a}
$$

For example, the two curvature variations are
\(\delta F_{\bar1\bar2}/\delta A_{\bar1}
=-\mathcal D_{\bar2}\) and
\(\delta F_{\bar1\bar2}/\delta A_{\bar2}
=+\mathcal D_{\bar1}\); compact-support transposition produces the
two derivative signs in (4D.90a).

The \(B\)-square is

$$
\begin{aligned}
\delta_{\mathrm h}^2B
&=-(\delta_{\mathrm h}c)\times B
+c\times(\delta_{\mathrm h}B)\\
&=\frac12(c\times c)\times B
-c\times(c\times B)=0.
\end{aligned}
\tag{4D.90b}
$$

For \(A_{\bar1}^*\), every derivative term is visible in

$$
\begin{aligned}
\delta_{\mathrm h}^2A_{\bar1}^*
={}&\frac12(c\times c)\times A_{\bar1}^*
+c\times\left(-c\times A_{\bar1}^*
-4\mathcal D_{\bar2}B\right)\\
&-4\mathcal D_{\bar2}(-c\times B)
-4(\mathcal D_{\bar2}c)\times B\\
={}&\frac12(c\times c)\times A_{\bar1}^*
-c\times(c\times A_{\bar1}^*)\\
&-4c\times\mathcal D_{\bar2}B
+4(\mathcal D_{\bar2}c)\times B
+4c\times\mathcal D_{\bar2}B
-4(\mathcal D_{\bar2}c)\times B=0.
\end{aligned}
\tag{4D.90c}
$$

The second connection-antifield square differs only by the sign of its
\(B\)-term:

$$
\begin{aligned}
\delta_{\mathrm h}^2A_{\bar2}^*
={}&\frac12(c\times c)\times A_{\bar2}^*
+c\times\left(-c\times A_{\bar2}^*
+4\mathcal D_{\bar1}B\right)\\
&+4\mathcal D_{\bar1}(-c\times B)
+4(\mathcal D_{\bar1}c)\times B\\
={}&\frac12(c\times c)\times A_{\bar2}^*
-c\times(c\times A_{\bar2}^*)\\
&+4c\times\mathcal D_{\bar1}B
-4(\mathcal D_{\bar1}c)\times B
-4c\times\mathcal D_{\bar1}B
+4(\mathcal D_{\bar1}c)\times B=0.
\end{aligned}
\tag{4D.90d}
$$

Finally, substituting all four lines of (4D.90a) gives

$$
\begin{aligned}
\delta_{\mathrm h}^2c^*
={}&\frac12(c\times c)\times c^*
+c\times\left[-c\times c^*
-\mathcal D_{\bar1}A_{\bar1}^*
-\mathcal D_{\bar2}A_{\bar2}^*
+4\alpha\times B\right]\\
&-\mathcal D_{\bar1}\left[-c\times A_{\bar1}^*
-4\mathcal D_{\bar2}B\right]
-(\mathcal D_{\bar1}c)\times A_{\bar1}^*\\
&-\mathcal D_{\bar2}\left[-c\times A_{\bar2}^*
+4\mathcal D_{\bar1}B\right]
-(\mathcal D_{\bar2}c)\times A_{\bar2}^*\\
&+4(-c\times\alpha-F_{\bar1\bar2})\times B
-4\alpha\times(-c\times B)\\
={}&\frac12(c\times c)\times c^*-c\times(c\times c^*)
-c\times\mathcal D_{\bar1}A_{\bar1}^*
-c\times\mathcal D_{\bar2}A_{\bar2}^*\\
&+4c\times(\alpha\times B)
+(\mathcal D_{\bar1}c)\times A_{\bar1}^*
+c\times\mathcal D_{\bar1}A_{\bar1}^*
+4\mathcal D_{\bar1}\mathcal D_{\bar2}B
-(\mathcal D_{\bar1}c)\times A_{\bar1}^*\\
&+(\mathcal D_{\bar2}c)\times A_{\bar2}^*
+c\times\mathcal D_{\bar2}A_{\bar2}^*
-4\mathcal D_{\bar2}\mathcal D_{\bar1}B
-(\mathcal D_{\bar2}c)\times A_{\bar2}^*\\
&-4(c\times\alpha)\times B
-4F_{\bar1\bar2}\times B
+4\alpha\times(c\times B)\\
={}&4(\mathcal D_{\bar1}\mathcal D_{\bar2}
-\mathcal D_{\bar2}\mathcal D_{\bar1})B
-4F_{\bar1\bar2}\times B\\
&+4\left[
c\times(\alpha\times B)
-(c\times\alpha)\times B
+\alpha\times(c\times B)
\right]\\
={}&4F_{\bar1\bar2}\times B-4F_{\bar1\bar2}\times B+0=0.
\end{aligned}
\tag{4D.90e}
$$

Therefore the Hamiltonian vector field squares to zero on all eight
horizontal coordinates, and

$$
\boxed{
\frac12(S_{\mathrm{hBF}},S_{\mathrm{hBF}})
=\sum_{Y\in\{c,A_{\bar1},A_{\bar2},\alpha\}}
(-1)^{\epsilon_Y}Y^*\delta_{\mathrm h}^2Y=0.}
\tag{4D.91}
$$

No field equation has entered (4D.89)--(4D.91).

### 4D.12 Cyclic contraction of the vertical sector

Let

$$
\mathcal V_{\mathrm{ctr}}
:=\operatorname{span}
\{u_1,u_2,w,\eta_1,\eta_2,K\}.
\tag{4D.92}
$$

On fields define

$$
h\eta_i=u_i,
\qquad
hK=w,
\qquad
hu_i=hw=0.
\tag{4D.93}
$$

Then every basis element satisfies

$$
\begin{array}{c|cccccc}
x&u_1&u_2&w&\eta_1&\eta_2&K\\ \hline
(\delta h+h\delta)x
&h\eta_1&h\eta_2&hK&\delta u_1&\delta u_2&\delta w\\
&u_1&u_2&w&\eta_1&\eta_2&K.
\end{array}
\tag{4D.94}
$$

Hence

$$
\delta h+h\delta=\operatorname{id}_{\mathcal V_{\mathrm{ctr}}}.
\tag{4D.95}
$$

The ordered bracket (4D.26) applied directly to (4D.76) gives the complete
dual differential and fixes its signs:

$$
\begin{array}{c|cccccc}
x&u_1^*&u_2^*&w^*&\eta_1^*&\eta_2^*&K^*\\ \hline
\delta x&0&0&0&u_1^*&u_2^*&-w^*\\
hx&\eta_1^*&\eta_2^*&-K^*&0&0&0.
\end{array}
\qquad
\begin{aligned}
\delta\eta_i^*
&=(S_{\mathrm{ctr}},\eta_i^*)=u_i^*,\\
\delta K^*
&=(S_{\mathrm{ctr}},K^*)=-w^*.
\end{aligned}
\tag{4D.96}
$$

Together with (4D.68) and (4D.93), every dual basis element obeys

$$
\begin{array}{c|cccccc}
x&u_1^*&u_2^*&w^*&\eta_1^*&\eta_2^*&K^*\\ \hline
(\delta h+h\delta)x
&\delta\eta_1^*&\delta\eta_2^*&-\delta K^*
&hu_1^*&hu_2^*&-hw^*\\
&u_1^*&u_2^*&w^*&\eta_1^*&\eta_2^*&K^*.
\end{array}
$$

Hence \(\delta h+h\delta=\operatorname{id}\) on all twelve vertical
coordinates.  For the ordered cotangent pairing, the only independent
nonzero cyclicity checks are

$$
\begin{aligned}
\omega_{\mathrm{ctr}}(h\eta_i,u_i^*)
+(-1)^{|\eta_i|}\omega_{\mathrm{ctr}}(\eta_i,hu_i^*)
&=\omega_{\mathrm{ctr}}(u_i,u_i^*)
-\omega_{\mathrm{ctr}}(\eta_i,\eta_i^*)=1-1=0,\\
\omega_{\mathrm{ctr}}(hK,w^*)
+(-1)^{|K|}\omega_{\mathrm{ctr}}(K,hw^*)
&=\omega_{\mathrm{ctr}}(w,w^*)
-\omega_{\mathrm{ctr}}(K,K^*)=1-1=0.
\end{aligned}
\tag{4D.97}
$$

All other basis pairs vanish or follow from graded antisymmetry; the
contraction is cyclic.  If \(i\) includes the horizontal factor and
\(p\) sets all vertical fields and antifields to zero, then

$$
pi=\operatorname{id}_{\mathcal F_{\mathrm{hBF}}},
\qquad
\delta h+h\delta
=\operatorname{id}_{\mathcal F_{\mathrm{tw}}}-ip.
\tag{4D.98}
$$

Equations (4D.58), (4D.70), (4D.74), and (4D.98) prove the result
(4D.1).

### 4D.13 Regulated BV path-integral substitution and its obstruction

A path integral requires data that are not contained in the classical triple
\((\mathcal F,\omega,S_0)\).  To separate the classical statement from these
additional data, conditionally fix a finite-dimensional BV regulator \(\nu\).
Write \(\mathscr T_\nu\) for the regulated restriction of the combined
new-to-old map \(T_0\circ T_1^{-1}\).  The regulator is admissible here only
if it preserves the identities already proved:

$$
\delta_\nu^2=0,
\qquad
\frac12(S_{0,\nu},S_{0,\nu})_\nu=0,
\qquad
\mathscr T_\nu^*S_{0,X,\nu}
=S_{\mathrm{hBF},\nu}+S_{\mathrm{ctr},\nu},
\qquad
\delta_\nu h_\nu+h_\nu\delta_\nu
=\operatorname{id}-i_\nu p_\nu.
$$

Here \(i_\nu,p_\nu,h_\nu\) are the regulated inclusion, projection, and
cyclic homotopy corresponding to (4D.98).  A naive mode projection is not
admissible.  Indeed, for even gauge-algebra-valued coefficients \(x,y,z\),
if \(P_\nu^2=P_\nu\) and
\([x,y]_\nu:=P_\nu[P_\nu x,P_\nu y]\), then its Jacobiator is

$$
\begin{aligned}
J_\nu(x,y,z)
&:=P_\nu\Big(
[P_\nu[P_\nu x,P_\nu y],P_\nu z]
+[P_\nu[P_\nu y,P_\nu z],P_\nu x]\\
&\hspace{3.2cm}
+[P_\nu[P_\nu z,P_\nu x],P_\nu y]\Big)\\
&=P_\nu\Big(
[(P_\nu-\operatorname{id})[P_\nu x,P_\nu y],P_\nu z]
+[(P_\nu-\operatorname{id})[P_\nu y,P_\nu z],P_\nu x]\\
&\hspace{3.2cm}
+[(P_\nu-\operatorname{id})[P_\nu z,P_\nu x],P_\nu y]\Big),
\end{aligned}
$$

This defect is nonzero already for a three-mode cutoff.  Let
\(e_n(t):=e^{int}\), retain \(n\in\{-1,0,1\}\), and set
\(P_\nu e_n=e_n\) for retained \(n\) and \(P_\nu e_n=0\) otherwise.
For

$$
[H,E]=2E,
\qquad
[E,F]=H,
\qquad
[F,H]=2F,
$$

choose \(x=He_1\), \(y=Ee_1\), and \(z=Fe_{-1}\).  Then

$$
\begin{aligned}
[[x,y]_\nu,z]_\nu&=[0,Fe_{-1}]_\nu=0,\\
[[y,z]_\nu,x]_\nu&=[He_0,He_1]_\nu=0,\\
[[z,x]_\nu,y]_\nu&=[2Fe_0,Ee_1]_\nu=-2He_1,\\
J_\nu(x,y,z)&=-2He_1\neq0.
\end{aligned}
$$

Thus the Jacobiator is not identically zero for a general \(P_\nu\).
Existence of an
admissible interacting regulator is not proved below.  Subject to this
condition, let
\(\widehat{\boldsymbol\varpi}_{X,\nu}\) be an even nowhere-vanishing BV
density in the regulated \(X\)-Darboux chart, let \(\Psi_{\mathrm{gf}}\) be an
odd gauge-fixing fermion, and let \(\Gamma_{X,\nu}\) be a convergent real
integration cycle inside the complex gauge-fixing Lagrangian.  No
regulator-removal statement is made.  The Project minus-graph convention is

$$
\boxed{
\begin{aligned}
\mathfrak L_{\Psi_{\mathrm{gf}},0,\nu}
&:=\left\{
X^*=-\frac{\overrightarrow\partial\Psi_{\mathrm{gf}}}
{\partial X}
\ \text{for every regulated coordinate }X
\right\},\\
\mathcal Z_{X,\nu}[\Psi_{\mathrm{gf}},\Gamma_X]
&:=\int_{\Gamma_{X,\nu}\subset
\mathfrak L_{\Psi_{\mathrm{gf}},0,\nu}}
\ell_X^*\left[
\widehat{\boldsymbol\varpi}_{X,\nu}^{1/2}
\exp\left(-\frac{S_{0,X}}{\hbar}\right)
\right].
\end{aligned}}
\tag{4D.99}
$$

In (4D.99)--(4D.101), the symbols
\(X,\delta,\Psi_0,S_E^{(1)}\) denote their regulated counterparts
\(X_\nu,\delta_\nu,\Psi_{0,\nu},S_{E,\nu}^{(1)}\); the subscript is
suppressed only to keep the earlier coordinate formulas unchanged.

Here \(\operatorname{Dens}^{1/2}(\mathcal F_{\mathrm{BV}})\) denotes the
half-density line on the regulated BV space and
\(\operatorname{Dens}(\mathfrak L)\) the density line on a Lagrangian.  The
odd symplectic structure defines the canonical BV restriction

$$
\operatorname{Res}_{\mathfrak L}:
\operatorname{Dens}^{1/2}(\mathcal F_{\mathrm{BV}})
\longrightarrow
\operatorname{Dens}(\mathfrak L).
$$

The notation \(\ell_X^*\) in (4D.99), and every \(\ell^*\) below, means this
BV restriction; it is not the ordinary tensor pullback of a half-density.
The phrase
``classical path-integral statement'' below means the field-dependent
coefficient of \(\hbar^0\) in the effective master action; the integral in
(4D.99) itself is quantum data.

Let \(T_0\) denote the first coordinate substitution from hatted to old
coordinates,

$$
T_0:\quad
(X,\widehat X^*)\longmapsto
\left(
X,
X^*=\widehat X^*-g^{-2}
\frac{\overrightarrow\partial\Psi_0}{\partial X}
\right).
$$

Its regulated Jacobian and its pullback of the old gauge-fixing graph are

$$
\boxed{
\begin{aligned}
\frac{\overrightarrow\partial(X,X^*)}
{\partial(X,\widehat X^*)}
&=
\begin{pmatrix}
\mathbf1&0\\
-g^{-2}\Psi_0''&\mathbf1
\end{pmatrix},
&\operatorname{Ber}(dT_0)&=1,\\
T_0^{-1}\mathfrak L_{\Psi_{\mathrm{gf}},0,\nu}
&=\left\{
\widehat X^*
=-\frac{\overrightarrow\partial}{\partial X}
\left(\Psi_{\mathrm{gf}}-g^{-2}\Psi_0\right)
\right\}
=\mathfrak L_{\Psi_{\mathrm{gf}}-g^{-2}\Psi_0,0,\nu}.
\end{aligned}}
\tag{4D.100}
$$

Thus the old zero section does not become the hatted zero section.  For
\(\Psi_{\mathrm{gf}}=0\), its pullback is

$$
\widehat X^*=g^{-2}
\frac{\overrightarrow\partial\Psi_0}{\partial X}.
$$

Restricting the transformed action (4D.62) to this correct graph gives every
term explicitly:

$$
\boxed{
\begin{aligned}
\left.T_0^*S_{0,X}\right|_{T_0^{-1}\mathfrak L_{0,0,\nu}}
&=g^{-2}\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa\left(
\frac{\overrightarrow\partial\Psi_0}{\partial X}
\delta X\right)\\
&=g^{-2}\iota_\delta d_{\mathrm{fld}}\Psi_0
=g^{-2}\delta\Psi_0
=g^{-2}Q\Psi_0
=S_E^{(1)}.
\end{aligned}}
\tag{4D.101}
$$

The \(Q\)-exact action has therefore moved from the master function to the
integration cycle; it has not vanished from the integral.  Replacing the
last graph in (4D.100) by \(\widehat X^*=0\) changes the integral.

Now let \(T_1\) be the old-to-new cotangent lift (4D.71).  Work in the
intermediate complex component chart already fixed by (4D.4), and order one
regulated adjoint coefficient by parity as

$$
\begin{aligned}
X_{\bar0}&=(A_{\bar1},A_{\bar2},u_1,u_2,\mathscr D),
&Y_{\bar0}&=(A_{\bar1},A_{\bar2},u_1,u_2,K),\\
X_{\bar1}&=(c,w,\lambda_1,
\widetilde\lambda^{\dot1},\widetilde\lambda^{\dot2}),
&Y_{\bar1}&=(c,w,\alpha,\eta_1,\eta_2).
\end{aligned}
$$

Equations (4D.63)--(4D.66) give triangular Fr\'echet matrices.  Their
full parity-block matrix has the form
\(dF_\nu=\left(\begin{smallmatrix}A_{\bar0\bar0}&B\\
C&D_{\bar1\bar1}\end{smallmatrix}\right)\).
The only nonzero entries of \(B\) have output \(K\) and inputs \(c,w\);
the only nonzero entries of \(C\) have outputs \(\eta_i\) and inputs \(u_i\);
and

$$
(D_{\bar1\bar1}^{-1})_{\beta\gamma}=0
\quad
\text{for }
\beta\in\{c,w\},
\quad
\gamma\in\{\eta_1,\eta_2\}.
$$

Hence \(BD_{\bar1\bar1}^{-1}C=0\) exactly and
\(\operatorname{Ber}(dF_\nu)
=\det(A_{\bar0\bar0}-BD_{\bar1\bar1}^{-1}C)/
\det D_{\bar1\bar1}
=\det A_{\bar0\bar0}/\det D_{\bar1\bar1}\).
The two diagonal determinants are

$$
\boxed{
\begin{aligned}
\det(dF_\nu)_{\bar0}
&=1\cdot1\cdot1\cdot1\cdot(-i)=-i,\\
\det(dF_\nu)_{\bar1}
&=1\cdot1\cdot
\det\begin{pmatrix}
-\frac14&0&0\\
0&0&-i\\
0&-i&0
\end{pmatrix}\\
&=-\frac14\left[0-(-i)(-i)\right]
=-\frac14,\\
\operatorname{Ber}(dF_\nu)
&=\frac{\det(dF_\nu)_{\bar0}}
{\det(dF_\nu)_{\bar1}}
=\frac{-i}{-1/4}=4i.
\end{aligned}}
\tag{4D.102}
$$

The entries containing \(\mathcal D_zc\), \(u_i\times c\),
\(Z(A_{\bar i},u_i)\), and \(\llbracket c,w\rrbracket\) are strictly
off-diagonal in this order and do not enter either determinant.  If
\(N_\nu\) is the number of regulated spacetime coefficients times
\(\dim\mathfrak g_{\mathbb C}\), then

$$
\operatorname{Ber}(dF_\nu)=(4i)^{N_\nu}.
$$

For completeness, let \(V_\nu\) be the regulated field superspace and write
\(J=dF_\nu\in\operatorname{GL}(V_\nu)\).  The field map is \(dY=J\,dX\),
whereas the cotangent map following from
\(\widehat X^*dX=Y^*dY\) is
\(Y^*=(J^\vee)^{-1}\widehat X^*\).  On the parity-reversed cotangent
fiber,

$$
\begin{aligned}
\operatorname{Ber}_{\Pi V_\nu^*}
\left((J^\vee)^{-1}\right)
&=\left[
\operatorname{Ber}_{V_\nu^*}
\left((J^\vee)^{-1}\right)
\right]^{-1}\\
&=\left[\operatorname{Ber}_{V_\nu}(J)^{-1}\right]^{-1}
=\operatorname{Ber}(J),\\
\boxed{\operatorname{Ber}(dT_1)}
&=\operatorname{Ber}(J)\,
\operatorname{Ber}_{\Pi V_\nu^*}
\left((J^\vee)^{-1}\right)
=\operatorname{Ber}(J)^2
=(-16)^{N_\nu}.
\end{aligned}
\tag{4D.103}
$$

Consequently an odd-symplectic coordinate change need not preserve a chosen
flat density.  With the declared forward Jacobian and flat coordinate
semidensities,

$$
\boxed{
|D\Phi_X|^{1/2}
=\operatorname{Ber}(dT_1)^{-1/2}|D\Phi_Y|^{1/2}
=(4i)^{-N_\nu}|D\Phi_Y|^{1/2},}
\tag{4D.104}
$$

where the square root is fixed by the ordered base Berezinian in (4D.102).
The same factor may be placed in the exponent as

$$
(4i)^{-N_\nu}
e^{-(S_{\mathrm{hBF}}+S_{\mathrm{ctr}})/\hbar}
=\exp\left[-\frac{
S_{\mathrm{hBF}}+S_{\mathrm{ctr}}
+\hbar N_\nu\log(4i)}{\hbar}\right].
\tag{4D.105}
$$

This is a field-independent regulated vacuum normalization.  For a general
Project density, the exact rule is instead to pull the old semidensity back
along the new-to-old substitution.  Define

$$
\mathscr T_\nu
:=T_{0,\nu}\circ T_{1,\nu}^{-1}:
\mathcal F_{Y,\nu}\longrightarrow\mathcal F_{X,\nu}.
$$

Its defining action identity is

$$
\mathscr T_\nu^*S_{0,X,\nu}
=S_{\mathrm{hBF},\nu}+S_{\mathrm{ctr},\nu}.
$$

For the flat semidensity,
\(\operatorname{Ber}(d\mathscr T_\nu)
=\operatorname{Ber}(dT_1)^{-1}\) and its multiplier is
\((4i)^{-N_\nu}\), in agreement with (4D.104).  For a general density,
define the pulled-back cycle and the density ratio by

$$
\boxed{
\begin{aligned}
\Gamma_{Y,\nu}&:=\mathscr T_\nu^{-1}(\Gamma_{X,\nu}),\\
\mathscr T_\nu^*\widehat{\boldsymbol\varpi}_{X,\nu}^{1/2}
&=:\mathcal J_{\mathscr T,\nu}^{1/2}
\widehat{\boldsymbol\varpi}_{Y,\nu}^{1/2},\\
\mathcal Z_{X,\nu}
&=\int_{\Gamma_{Y,\nu}}
\ell_Y^*\left[
\mathcal J_{\mathscr T,\nu}^{1/2}
\widehat{\boldsymbol\varpi}_{Y,\nu}^{1/2}
\exp\left(-\frac{S_{\mathrm{hBF}}+S_{\mathrm{ctr}}}{\hbar}\right)
\right].
\end{aligned}}
\tag{4D.106}
$$

Equation (4D.106) is only a change of variables and requires no QME.  It also
shows the first path-integral obstruction: (4D.74) splits the action, but it
does not prove either of the two independent factorization conditions

$$
\boxed{
\begin{aligned}
\Gamma_{Y,\nu}
&=\Gamma_{\mathrm{hBF},\nu}
\times\Gamma_{\mathrm{ctr},\nu},\\
\ell_Y^*\left(
\mathcal J_{\mathscr T,\nu}^{1/2}
\widehat{\boldsymbol\varpi}_{Y,\nu}^{1/2}
\right)
&=\ell_{\mathrm h}^*
\widehat{\boldsymbol\varpi}_{\mathrm{hBF},\nu}^{1/2}
\boxtimes
\ell_{\mathrm{ctr}}^*
\widehat{\boldsymbol\varpi}_{\mathrm{ctr},\nu}^{1/2}.
\end{aligned}}
\tag{4D.107}
$$

If (4D.107) is supplied, an explicit vertical Lagrangian is

$$
\mathfrak L_{\mathrm{ctr},\nu}
:=\{u_i=\eta_i^*=w=K^*=0\}.
$$

Its free coordinates are
\((u_1^*,u_2^*,\eta_1,\eta_2,w^*,K)\).  Pullback of every term in
\(\omega_{\mathrm{ctr}}\) vanishes, its dimension is one half of the
vertical BV dimension, and

$$
\left.S_{\mathrm{ctr}}\right|_{\mathfrak L_{\mathrm{ctr},\nu}}
=\int d^4x_E\,\operatorname{tr}_\kappa
\left(u_1^*\eta_1+u_2^*\eta_2-w^*K\right).
$$

After choosing a convergent real contour inside this complex Lagrangian and
a Berezin orientation, define

$$
\boxed{
C_{\mathrm{ctr},\nu}(\hbar)
:=\int_{\Gamma_{\mathrm{ctr},\nu}}
\ell_{\mathrm{ctr}}^*\left[
\widehat{\boldsymbol\varpi}_{\mathrm{ctr},\nu}^{1/2}
\exp\left(-\frac{S_{\mathrm{ctr}}}{\hbar}\right)
\right].}
\tag{4D.108}
$$

The bosonic Hessian of \(-w^*K\) in the ordered coordinates
\((w^*,K)\) is

$$
-\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\det\left[-\begin{pmatrix}0&1\\1&0\end{pmatrix}\right]=-1.
$$

It is nondegenerate but has one positive and one negative eigenvalue, so the
contract does not supply a canonical convergent real contour.  Acyclicity
alone does not assign a value to (4D.108).  Let
\(\pi_*^{\mathrm{BV}}\) denote integration of the BV-restricted product
semidensity along \(\Gamma_{\mathrm{ctr},\nu}\), leaving a horizontal
semidensity.

When (4D.107)--(4D.108) hold, BV fiber integration is exact:

$$
\boxed{
\begin{aligned}
\pi_*^{\mathrm{BV}}\!\left[
\left(
\widehat{\boldsymbol\varpi}_{\mathrm{hBF},\nu}^{1/2}
\boxtimes
\widehat{\boldsymbol\varpi}_{\mathrm{ctr},\nu}^{1/2}
\right)
e^{-(S_{\mathrm{hBF}}+S_{\mathrm{ctr}})/\hbar}
\right]
&=\widehat{\boldsymbol\varpi}_{\mathrm{hBF},\nu}^{1/2}
e^{-S_{\mathrm{eff},\nu}/\hbar}\\
&=\widehat{\boldsymbol\varpi}_{\mathrm{hBF},\nu}^{1/2}
e^{-S_{\mathrm{hBF}}/\hbar}
C_{\mathrm{ctr},\nu}(\hbar),\\
S_{\mathrm{eff},\nu}
&=S_{\mathrm{hBF}}
-\hbar\log C_{\mathrm{ctr},\nu}(\hbar).
\end{aligned}}
\tag{4D.109}
$$

The normalized pushforward divides the first line of (4D.109) by
\(C_{\mathrm{ctr},\nu}(\hbar)\).  It gives

$$
\boxed{
S_{\mathrm{eff},\nu}^{\mathrm{normalized}}
=S_{\mathrm{hBF}},
\qquad
S_{\mathrm{eff},\nu}^{(0),\mathrm{field\ dependent}}
=S_{\mathrm{hBF}}.}
\tag{4D.110}
$$

No vertical interaction contains a horizontal variable by (4D.74)--(4D.76),
so no connected tree with a horizontal external leg can contain a vertical
internal edge.  This is the precise path-integral form of the classical
cyclic contraction.

Changing \(\Gamma_{Y,\nu}\) to a preferred product cycle is not a mere
coordinate substitution.  For a BV-compatible chosen density with
\(\Delta_\nu^2=0\), use the Step-3D convention

$$
\Delta_\nu(FG)
=(\Delta_\nu F)G
+(-1)^{\epsilon_F}F\Delta_\nu G
+(-1)^{\epsilon_F}(F,G),
$$

direct differentiation gives

$$
\boxed{
\Delta_\nu e^{-W_\nu/\hbar}
=\left[
-\frac1\hbar\Delta_\nu W_\nu
+\frac1{2\hbar^2}(W_\nu,W_\nu)
\right]e^{-W_\nu/\hbar},
\qquad
\frac12(W_\nu,W_\nu)-\hbar\Delta_\nu W_\nu=0.}
\tag{4D.111}
$$

Write the quantum master action without omitted orders as
\(W_\nu=\sum_{n\geq0}\hbar^nS_{n,\nu}\).  Equality of every coefficient in
(4D.111) requires

$$
\boxed{
\begin{aligned}
\frac12(S_{0,\nu},S_{0,\nu})&=0,\\
(S_{0,\nu},S_{1,\nu})-\Delta_\nu S_{0,\nu}&=0,\\
\frac12\sum_{r+s=n}(S_{r,\nu},S_{s,\nu})
-\Delta_\nu S_{n-1,\nu}&=0,
\qquad n\geq2.
\end{aligned}}
\tag{4D.112}
$$

The first line is the CME already proved.  The second line has a solution
only if \(\Delta_\nu S_{0,\nu}\) lies in the image of
\((S_{0,\nu},\cdot)\).  This is the first quantum obstruction.  A deformation
of cycles additionally needs the BV--Stokes identity and zero flux at
field-space infinity; compact support in spacetime does not imply either
condition.

Finally, before the compact-support step (4D.57), set

$$
I_P[A]:=\int_M d^4x_E\,\operatorname{tr}_\kappa P
=\frac12\int_M\operatorname{tr}_\kappa(F\wedge F),
\qquad
\tau:=g^{-2}-ik.
$$

The first shift then gives, without discarding a term,

$$
\boxed{
T_0^*S_{0,X}^{\mathrm{global}}
=\tau I_P[A]
+\sum_X\int(-1)^{\epsilon_X}
\operatorname{tr}_\kappa(\widehat X^*\delta X).}
\tag{4D.113}
$$

On a trivialized bundle over a manifold with boundary, (4D.55) gives

$$
\begin{aligned}
I_P[A]
&=\frac12\int_{\partial M}
\operatorname{tr}_\kappa\left[
A\wedge dA+\frac13A\wedge(A\times A)\right],\\
d_{\mathrm{fld}}I_P[A]
&=\int_{\partial M}
\operatorname{tr}_\kappa(d_{\mathrm{fld}}A\wedge F).
\end{aligned}
$$

In this contract the connection \(A\), not only its variation, has compact
support.  Therefore

$$
I_P[A]
=\frac12\lim_{R\to\infty}\int_{S_R^3}
\operatorname{tr}_\kappa\left[
A\wedge dA+\frac13A\wedge(A\times A)\right]
=0.
$$

On a closed manifold and within a fixed bundle sector \(\mathfrak p\),
\(d_{\mathrm{fld}}I_P=0\).  The value \(I_P(\mathfrak p)\) is then a
sector-dependent constant: it does not change the local classical BV vector
field, but it prevents strict equality of master functions and contributes
the exact path-integral weight

$$
\exp\left[-\frac{\tau I_P(\mathfrak p)}{\hbar}\right].
$$

On a boundary or asymptotic sector,
\(d_{\mathrm{fld}}I_P\) is the second line above and need not vanish; boundary
conditions or a BV--BFV completion are then required.  Since
\(\mathbb R^4\) is contractible, a smooth principal bundle on it is trivial.
A nonzero instanton number on \(\mathbb R^4\) is encoded by the transition
map at \(S_\infty^3\), equivalently by extension to a nontrivial bundle on
\(S^4\); such a connection violates the compact-support condition.  The
symbol \(\tau_E\) below denotes an antilinear Euclidean reality involution,
and \(S_{\mathrm{nonmin}}\) denotes the master action of the antighost and
Nakanishi--Lautrup contractible pairs.  The complete obstruction hierarchy is

$$
\boxed{
\begin{array}{c|l}
\text{statement}&\text{obstruction}\\ \hline
\text{local complexified classical BV theorem in the stated scope}
&\varnothing\\
\text{strict global master-function equality}
&\tau I_P(\mathfrak p)\ \text{and global bundle patching}\\
\text{boundary or asymptotic classical BV theory}
&d_{\mathrm{fld}}I_P,\ \text{boundary conditions, and BV--BFV data}\\
\text{actual Euclidean BV integral before loop expansion}
&\tau_E,\ S_{\mathrm{nonmin}},\ \Psi_{\mathrm{gf}},\
\Gamma^E_{X,\nu},\ \text{then the two factorizations (4D.107)}\\
\text{quantum comparison}
&\text{admissible regulator},\
\widehat{\boldsymbol\varpi}_{\nu},\ \Delta_\nu,\
\text{QME, and vertical normalization}
\end{array}}
\tag{4D.114}
$$

Thus (4D.1) proves a classical BV quasi-isomorphism and the normalized
tree-level pushforward (4D.110).  It does not prove equality between the
ordinary Euclidean \(\mathcal N=1\) partition function and a standard
holomorphic-BF partition function.

### 4D.14 Derivation-gap audit

All obligations inside the stated component, complexified,
compact-support, trivial-bundle scope are closed:

$$
\boxed{
\mathrm{P0}=\varnothing,
\qquad
\mathrm{P1}=\varnothing.}
\tag{4D.115}
$$

The unproved extensions are

$$
\begin{array}{c|c|c|p{4.7cm}|p{5.7cm}}
\mathrm{id}&\mathrm{type}&\mathrm{severity}&\mathrm{claim\ not\ made}
&\mathrm{minimal\ additional\ obligation}\\ \hline
\mathrm{HT\!-
GAP\!-
01}&\mathrm{G\!-
SCOPE}&\mathrm{P2}
&Canonical equivalence between the unconstrained Step-3D superfield BV
theory and the residual component BV theory (4D.30).
&Construct the supergauge Wess--Zumino reduction, all superghost
contractible pairs, and its cotangent lift.\\
\mathrm{HT\!-
GAP\!-
02}&\mathrm{G\!-
SCOPE}&\mathrm{P2}
&Removal of the topological functional on nontrivial bundles, instanton
sectors, manifolds with boundary, or non-compact-support fields.
&Retain the exact \((g^{-2}-ik)\int P\) sector and specify boundary and
bundle data.\\
\mathrm{HT\!-
GAP\!-
03}&\mathrm{G\!-
SCOPE}&\mathrm{P2}
&Quantum commutation of twist and BV quantization.
&Choose a regulator and BV density, prove the QME, and calculate the
obstruction class and regulated Berezinian of the canonical reduction.\\
\mathrm{HT\!-
GAP\!-
04}&\mathrm{G\!-
DEF}&\mathrm{P2}
&Equality with an ordinary Euclidean component BV path integral.
&Adjoin a non-minimal gauge-fixing sector, choose
\(\Psi_{\mathrm{gf}}\), the Euclidean reality cycle, its convergence
conditions, and the regulated semidensity in (4D.99).\\
\mathrm{HT\!-
GAP\!-
05}&\mathrm{G\!-
PROJ}&\mathrm{P2}
&Factorization of the transformed Euclidean cycle into horizontal and
vertical cycles.
&Prove both equalities in (4D.107), or construct a Lagrangian homotopy and
prove the regulated QME, BV--Stokes identity, and zero field-space boundary
flux.\\
\mathrm{HT\!-
GAP\!-
06}&\mathrm{G\!-
NORM}&\mathrm{P2}
&The unnormalized vertical BV integral is canonically equal to one.
&Choose the bosonic contour and fermionic orientation in (4D.108), evaluate
\(C_{\mathrm{ctr},\nu}(\hbar)\), and state the regulator-removal
normalization.\\
\mathrm{HT\!-
GAP\!-
07}&\mathrm{G\!-
OP}&\mathrm{P2}
&Existence of a finite interacting BV regulator preserving the classical
master equation, exact split, and cyclic contraction.
&Construct a regulator satisfying the four identities preceding (4D.99);
a naive cylindrical projection is excluded by its displayed Jacobiator.\\
\end{array}
\tag{4D.116}
$$

Their dependency graph is

$$
\mathrm{HT\!-
GAP\!-
01}
\longrightarrow
\text{superfield-level classical extension},
\qquad
\mathrm{HT\!-
GAP\!-
02}
\longrightarrow
\text{global classical extension},
\qquad
\mathrm{HT\!-
GAP\!-
03}
\longrightarrow
\text{quantum extension},
\qquad
\mathrm{HT\!-
GAP\!-
04}
\longrightarrow
\mathrm{HT\!-
GAP\!-
05}
\longrightarrow
\mathrm{HT\!-
GAP\!-
06}
\longrightarrow
\text{Euclidean partition-function comparison},
\qquad
\mathrm{HT\!-
GAP\!-
07}
\longrightarrow
\text{regulated path-integral and quantum comparisons}.
\tag{4D.117}
$$

### 4D.15 Repository provenance surface

The repository convention provenance is restricted to:

1. Step 1 (1.3)--(1.5), (1.51)--(1.57), and (1.67)--(1.68);
2. Step 2A (2A.39)--(2A.43);
3. Step 3D (3D.43)--(3D.58);
4. Step 4 (4.1)--(4.14), (4.33)--(4.38);
5. Step 4A (4A.2)--(4A.11), (4A.27)--(4A.32), and
   (4A.56a)--(4A.57).

Every formula needed to check the proof has been restated and derived in
(4D.3)--(4D.117); the list above is not a logical prerequisite.  No external
holomorphic-twist or holomorphic-BF formula is used as an input.
