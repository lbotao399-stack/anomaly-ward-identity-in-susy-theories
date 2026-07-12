# 00 3+1d SUSY QFT — Convention Lock

## Step 4. Common notation for pure \(\mathcal N=1,2,4\) super Yang--Mills

### 4.1 Spacetime and spinor slots

$$
R\in\{L,E\},
\qquad
\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1),
\qquad
\delta_{mn}=\operatorname{diag}(+1,+1,+1,+1).
\tag{4.1}
$$

$$
\mu,\nu=0,1,2,3,
\qquad
m,n=1,2,3,4,
\qquad
a,b=1,2,
\qquad
\dot a,\dot b=\dot1,\dot2.
\tag{4.2}
$$

$$
\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,
\qquad
\epsilon_{12}=\epsilon_{\dot1\dot2}=-1,
\qquad
\xi\chi:=\xi^a\chi_a,
\qquad
\widetilde\xi\widetilde\chi
:=\widetilde\xi_{\dot a}\widetilde\chi^{\dot a}.
\tag{4.3}
$$

The matrices \(\sigma_L,\bar\sigma_L,\sigma_E,\bar\sigma_E\), their
antisymmetric products, and the Wick map are exactly Step 1.  In
particular,

$$
x_E^4=ix_L^0,
\qquad
\partial_0^L=i\partial_4^E,
\qquad
(\sigma_L^\mu)_{a\dot b}\partial_\mu^L
=i(\sigma_E^m)_{a\dot b}\partial_m^E.
\tag{4.4}
$$

### 4.2 Gauge algebra, invariant trace, and absorbed coupling

$$
A,B,C,D=1,\ldots,\dim\mathfrak g,
\qquad
[T_A,T_B]=ic_{AB}{}^CT_C,
\qquad
c_{AB}{}^C\in\mathbb R.
\tag{4.5}
$$

$$
\kappa_{AB}=\kappa_{BA},
\qquad
c_{CA}{}^D\kappa_{DB}+c_{CB}{}^D\kappa_{AD}=0,
\qquad
\kappa^{AC}\kappa_{CB}=\delta^A{}_B.
\tag{4.6}
$$

For homogeneous adjoint-valued component fields,

$$
\boxed{
\begin{aligned}
\operatorname{tr}_\kappa(XY)&:=\kappa_{AB}X^AY^B,\\
\llbracket X,Y\rrbracket^A&:=ic_{BC}{}^AX^BY^C,\\
(X\times Y)^A&:=-i\llbracket X,Y\rrbracket^A
=c_{BC}{}^AX^BY^C,\\
\llbracket Y,X\rrbracket
&=-(-1)^{|X||Y|}\llbracket X,Y\rrbracket,\\
\mathcal D_MX&:=\partial_MX-i\llbracket A_M,X\rrbracket.
\end{aligned}}
\tag{4.7}
$$

Hence

$$
(T_A^{\rm ad})^B{}_C=ic_{AC}{}^B,
\qquad
(\mathcal D_MX)^A
=\partial_MX^A+c_{BC}{}^AA_M^BX^C.
\tag{4.8}
$$

The invariance equation (4.6) gives

$$
\boxed{
\operatorname{tr}_\kappa
(X\llbracket Y,Z\rrbracket)
=\operatorname{tr}_\kappa
(\llbracket X,Y\rrbracket Z)}
\tag{4.9}
$$

with the displayed field order.  The connection and every field in an
extended vector multiplet are in the absorbed basis

$$
\begin{aligned}
A_M&=gA_M^{\rm can},
&\lambda&=g\lambda^{\rm can},
&\phi&=g\phi^{\rm can},\\
\psi&=g\psi^{\rm can},
&\mathscr D&=g\mathscr D^{\rm can},
&F&=gF^{\rm can}.
\end{aligned}
\tag{4.10}
$$

Thus every non-topological pure-SYM density below has one overall
factor \(g^{-2}\).  The independent topological angle is fixed by

$$
\mathfrak h_{AB}=g^{-2}\kappa_{AB},
\qquad
\mathfrak k_{AB}
=-\frac{\vartheta_{\rm YM}}{8\pi^2}\kappa_{AB},
\qquad
f_{AB}=\mathfrak h_{AB}+i\mathfrak k_{AB}.
\tag{4.11}
$$

### 4.3 \(\mathcal N=1\) multiplet

$$
\mathbb V_R
=\left(A_M^A,\lambda_a^A,
\widetilde\lambda_{\dot a}^A,\mathscr D^A\right).
\tag{4.12}
$$

For \(R=L\),

$$
(A_\mu^A)^\dagger=A_\mu^A,
\qquad
(\lambda_a^A)^\dagger=\bar\lambda_{\dot a}^A,
\qquad
(\mathscr D^A)^\dagger=\mathscr D^A.
\tag{4.13}
$$

For \(R=E\),

$$
(\lambda_a^A,\widetilde\lambda_{\dot a}^A)
\quad\hbox{and}\quad
(\mathcal W_{Ea}^A,\widetilde{\mathcal W}_{E\dot a}^A)
\tag{4.14}
$$

are independent before a contour is chosen.

### 4.4 \(SU(2)_R\) slots for \(\mathcal N=2\)

$$
i,j,k,l=1,2,
\qquad
\varepsilon^{12}=+1,
\qquad
\varepsilon_{12}=-1,
\qquad
v_i=\varepsilon_{ij}v^j,
\qquad
v^i=\varepsilon^{ij}v_j.
\tag{4.15}
$$

The \(\mathcal N=1\) decomposition is

$$
\boxed{
\mathbb V_{\mathcal N=2}
=\mathbb V\oplus\Phi,
\qquad
\Phi^A=(\phi^A,\psi_a^A,F^A),
\qquad
\chi_{1a}:=\psi_a,
\qquad
\chi_{2a}:=-\lambda_a.}
\tag{4.16}
$$

The Lorentzian conjugates are

$$
\bar\chi^{1}_{\dot a}:=(\chi_{1a})^\dagger=\bar\psi_{\dot a},
\qquad
\bar\chi^{2}_{\dot a}:=(\chi_{2a})^\dagger=-\bar\lambda_{\dot a},
\qquad
\bar\phi:=(\phi)^\dagger,
\qquad
\bar F:=(F)^\dagger.
\tag{4.17}
$$

The shifted real auxiliary and the symmetric lower-index triplet slots
are defined by

$$
\mu_A:=\widetilde\phi_B(T^{\rm ad}_A)^B{}_C\phi^C,
\qquad
\mu^A:=\kappa^{AB}\mu_B,
\qquad
H^A:=\mathscr D^A+\mu^A,
\tag{4.18}
$$

$$
\boxed{
Y_{11}:=-\sqrt2F,
\qquad
Y_{22}:=-\sqrt2\widetilde F,
\qquad
Y_{12}=Y_{21}:=iH,}
\tag{4.19}
$$

$$
Y^{ij}:=\varepsilon^{ik}\varepsilon^{jl}Y_{kl},
\qquad
Y^{11}=Y_{22},
\qquad
Y^{22}=Y_{11},
\qquad
Y^{12}=-Y_{12}.
\tag{4.19a}
$$

For \(R=L\), the triplet contour is

$$
(Y_{ij})^\dagger=Y^{ij}.
\tag{4.20}
$$

Equations (4.19)--(4.20) give, component by component,

$$
(Y_{11})^\dagger=Y^{11}=Y_{22},
\qquad
(Y_{12})^\dagger=Y^{12}=-Y_{12}.
\tag{4.21}
$$

Thus \(H_L^\dagger=H_L\) is compatible with the factor \(i\) in
(4.19).  For \(R=E\), \((\phi,\widetilde\phi)\),
\((\chi_i,\widetilde\chi^i)\), and the three complex slots
\((F,\widetilde F,H_E)\) are independent before the Wick contour.
They form one $Y_{E,ij}$ by (4.19); $Y_E^{ij}$ is obtained by
epsilon raising and is not a second triplet.

### 4.5 \(SU(3)\subset SU(4)_R\) slots for \(\mathcal N=4\)

$$
r,s,t=1,2,3,
\qquad
\delta_{r\bar s}=\delta_{rs},
\qquad
\varepsilon^{123}=\varepsilon_{123}=+1.
\tag{4.22}
$$

The \(\mathcal N=1\) decomposition is

$$
\boxed{
\mathbb V_{\mathcal N=4}
=\mathbb V\oplus\Phi_1\oplus\Phi_2\oplus\Phi_3,
\qquad
\Phi_r^A=(\phi_r^A,\psi_{ra}^A,F_r^A).}
\tag{4.23}
$$

Write six Lorentzian Hermitian adjoint scalars as

$$
\phi_r:=\frac1{\sqrt2}
\left(X^{2r-1}+iX^{2r}\right),
\qquad
\bar\phi_r:=\frac1{\sqrt2}
\left(X^{2r-1}-iX^{2r}\right).
\tag{4.24}
$$

Then

$$
\operatorname{tr}_\kappa
(\mathcal D_\mu\bar\phi_r\mathcal D^\mu\phi_r)
=\frac12\operatorname{tr}_\kappa
(\mathcal D_\mu X^u\mathcal D^\mu X^u),
\qquad
u=1,\ldots,6.
\tag{4.25}
$$

### 4.6 \(SU(4)_R\) packaging

$$
\mathcal I,\mathcal J,\mathcal K,\mathcal L=1,2,3,4,
\qquad
\epsilon_{1234}=\epsilon^{1234}=+1.
\tag{4.26}
$$

Define

$$
\boxed{
\Lambda_a^4:=\lambda_a,
\qquad
\Lambda_a^r:=\psi_{ra},
\qquad
\varphi^{r4}:=\phi_r,
\qquad
\varphi^{rs}:=\varepsilon^{rst}\widetilde\phi_t.}
\tag{4.27}
$$

The right-handed component slots are

$$
\boxed{
\begin{aligned}
\bar\Lambda_{L,\dot a4}&:=\bar\lambda_{\dot a},
&\bar\Lambda_{L,\dot ar}&:=\bar\psi_{r\dot a},\\
\widetilde\Lambda_{E,\dot a4}&:=\widetilde\lambda_{\dot a},
&\widetilde\Lambda_{E,\dot ar}&:=\widetilde\psi_{r\dot a}.
\end{aligned}}
\tag{4.27a}
$$

The antisymmetry \(\varphi^{\mathcal I\mathcal J}
=-\varphi^{\mathcal J\mathcal I}\) determines the remaining slots.
Define

$$
\widetilde\varphi_{\mathcal I\mathcal J}
:=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varphi^{\mathcal K\mathcal L}.
\tag{4.28}
$$

Equations (4.27)--(4.28) give exactly

$$
\widetilde\varphi_{r4}=\widetilde\phi_r,
\qquad
\widetilde\varphi_{rs}=\varepsilon_{rst}\phi_t.
\tag{4.29}
$$

For \(R=L\),

$$
\boxed{
(\varphi^{\mathcal I\mathcal J})^\dagger
=\widetilde\varphi_{\mathcal I\mathcal J}
=\frac12\epsilon_{\mathcal I\mathcal J\mathcal K\mathcal L}
\varphi^{\mathcal K\mathcal L},
\qquad
(\Lambda_a^{\mathcal I})^\dagger
=\bar\Lambda_{\dot a\mathcal I}.}
\tag{4.30}
$$

The scalar contraction is fixed by

$$
\boxed{
\frac14\widetilde\varphi_{\mathcal I\mathcal J}
\varphi^{\mathcal I\mathcal J}
=\widetilde\phi_r\phi_r.}
\tag{4.31}
$$

For \(R=E\), the six chiral-representation scalar slots
\((\phi_r,\widetilde\phi_r)\) and the two fermion families
\((\Lambda_E^{\mathcal I},\widetilde\Lambda_{E,\mathcal I})\) are
independent.  Equations (4.27)--(4.29) package all six scalar slots into
one antisymmetric \(\varphi_E^{\mathcal I\mathcal J}\); its Hodge dual
\(\widetilde\varphi_{E,\mathcal I\mathcal J}\) remains defined by
(4.28) and is not a second independent scalar.  The canonical scalar
contour adds

$$
\widetilde\varphi_{E,\mathcal I\mathcal J}
=(\varphi_E^{\mathcal I\mathcal J})^\dagger.
\tag{4.32}
$$

No finite \(SU(4)_R\)-covariant auxiliary multiplet is introduced.
The \(\mathcal N=1\) fields \((\mathscr D,F_r,\widetilde F_r)\) are kept
only in the manifest off-shell formulation and are eliminated before
the \(SU(4)_R\)-covariant formulation.

### 4.7 Supersymmetry parameters and closure labels

$$
\varepsilon_a^{\mathcal I},
\qquad
\bar\varepsilon_{\dot a\mathcal I}
=(\varepsilon_a^{\mathcal I})^\dagger
\quad(R=L),
\tag{4.33}
$$

where only \(\mathcal I=4\) is manifest in the \(\mathcal N=1\)
superspace decomposition (4.27).  In Euclidean signature the two
parameter families are independent.  Step 1 fixes

$$
\varepsilon_E^{\mathcal I}=\varepsilon_L^{\mathcal I},
\qquad
\bar\varepsilon_{E,\mathcal I}=\bar\varepsilon_{L,\mathcal I},
\qquad
Q_E^{\mathcal I}=-iQ_L^{\mathcal I},
\qquad
\bar Q_{E,\mathcal I}=-i\bar Q_{L,\mathcal I}.
\tag{4.34}
$$

In Euclidean formulas the notation-only alias is

$$
\widetilde\varepsilon_{E,\mathcal I}
:=\bar\varepsilon_{E,\mathcal I};
\tag{4.34a}
$$

it does not impose Hermitian conjugation.

For two transformations, define

$$
v_L^\mu
:=2i\left(
\varepsilon_1^{\mathcal I}\sigma_L^\mu
\bar\varepsilon_{2,\mathcal I}
-\varepsilon_2^{\mathcal I}\sigma_L^\mu
\bar\varepsilon_{1,\mathcal I}\right),
\tag{4.35}
$$

$$
v_E^m
:=-2\left(
\varepsilon_1^{\mathcal I}\sigma_E^m
\bar\varepsilon_{2,\mathcal I}
-\varepsilon_2^{\mathcal I}\sigma_E^m
\bar\varepsilon_{1,\mathcal I}\right).
\tag{4.36}
$$

The ordinary gauge transformation is

$$
\delta_\alpha A_M=\mathcal D_M\alpha,
\qquad
\delta_\alpha X=i\llbracket\alpha,X\rrbracket.
\tag{4.37}
$$

Therefore

$$
v^NF_{NM}
=v^N\partial_NA_M+\mathcal D_M(-v^NA_N).
\tag{4.38}
$$

Equation (4.38), rather than a suppressed ``translation plus gauge'',
is the closure convention used below.

### 4.8 Global parameter-left and Noether parameter-right orders

Every displayed constant-parameter component transformation is written in
global parameter-left order: each odd supersymmetry parameter precedes every
dynamical odd field in the same monomial.  Even matrices, derivatives, and
bosonic fields retain their tensor order.  For a component \(\Xi\),

$$
\delta_{\varepsilon}^{\rm glob}\Xi
=\varepsilon^{\mathsf s}
\mathcal R_{{\rm PL},\mathsf s}^{\Xi},
\qquad
\left|\mathcal R_{{\rm PL},\mathsf s}^{\Xi}\right|
=|\Xi|+1\pmod2.
\tag{4.38a}
$$

For two odd spinors,

$$
\begin{aligned}
\mathsf N_{\rm PL}
(\bar\zeta\bar\sigma^M\mathcal D_M\chi)
&:=\bar\zeta\bar\sigma^M\mathcal D_M\chi,\\
\mathsf N_{\rm FL}
(\bar\zeta\bar\sigma^M\mathcal D_M\chi)
&:=(\mathcal D_M\chi)\sigma^M\bar\zeta,\\
\mathsf N_{\rm PL}&=-\mathsf N_{\rm FL}.
\end{aligned}
\tag{4.38b}
$$

Thus a coefficient \(\mathsf A_{\rm PL}\) becomes
\(\mathsf A_{\rm FL}=-\mathsf A_{\rm PL}\).  The label \({\rm FL}\)
never denotes the Noether ordering below.

Only in the local-parameter Noether calculation are the odd parameters moved
to the far right:

$$
\delta_{\varepsilon(x)}^{\rm loc}\Xi
=\mathcal R_{{\rm PR},\mathsf s}^{\Xi}
\varepsilon^{\mathsf s}(x),
\qquad
\mathcal R_{{\rm PR},\mathsf s}^{\Xi}
=(-1)^{|\Xi|+1}\mathcal R_{{\rm PL},\mathsf s}^{\Xi}.
\tag{4.38c}
$$

All \(\mathcal C_{\mathsf s}^M\), \(\mathcal K_{\mathsf s}^M\), and
\(j_{\mathsf s}^M\) below use \({\rm PR}\) order.  For a displayed
component density \(\mathcal L\), first compute its symplectic coefficient
\(\mathcal C_{\mathsf s}^M\) and its constant-parameter boundary coefficient
\(\mathcal K_{\mathsf s}^M\), where \(\mathsf s\) labels a supersymmetry
generator:

$$
\Theta^M(\delta_\varepsilon)
=\mathcal C_{\mathsf s}^M\varepsilon^{\mathsf s},
\qquad
\delta_{\varepsilon={\rm const}}\mathcal L
=\partial_M(\mathcal K_{\mathsf s}^M
\varepsilon^{\mathsf s}).
\tag{4.39}
$$

For a local parameter, direct expansion gives

$$
\delta_{\varepsilon(x)}\mathcal L
=\partial_M(\mathcal K_{\mathsf s}^M\varepsilon^{\mathsf s})
+(\mathcal C_{\mathsf s}^M-\mathcal K_{\mathsf s}^M)
\partial_M\varepsilon^{\mathsf s}.
\tag{4.40}
$$

The unimproved current is

$$
\boxed{j_{\mathsf s}^M
:=\mathcal C_{\mathsf s}^M-\mathcal K_{\mathsf s}^M,}
\tag{4.41}
$$

and its divergence check is

$$
\boxed{
\partial_M j_{\mathsf s}^M
=-\sum_\Xi\mathcal E_\Xi
\mathcal R_{{\rm PR},\mathsf s}^\Xi,}
\tag{4.42}
$$

No identically conserved improvement is added.

### 4.9 Universal graded differential--Lie normal form

$$
K:=\mathbb Q(i,\sqrt2),
\qquad
\Theta_R:=\operatorname{sort}
\{\varepsilon_r^a,\bar\varepsilon_{r\dot a},
\eta_r^a,\bar\eta_{r\dot a}:r=1,2\}.
\tag{4.43}
$$

For commuting ordinary partial derivatives, define the totally ordered
homogeneous jet alphabet

$$
(M_1^L,M_2^L,M_3^L,M_4^L):=(0,1,2,3),
\qquad
(M_1^E,M_2^E,M_3^E,M_4^E):=(1,2,3,4),
\tag{4.43a}
$$

$$
J_{\Xi,\mathbf n}
:=\left(\prod_{r=1}^{4}
\partial_{M_r^R}^{n_r}\right)\Xi,
\qquad
\mathfrak J_R
:=\operatorname{sort}
\{J_{\Xi,\mathbf n}:\mathbf n\in\mathbb N^4,
\ \Xi\ \hbox{a component field}\},
\tag{4.44}
$$

define

$$
\boxed{
\mathcal A_{\rm univ}^{R}
:=K\otimes\Lambda(\Theta_R)
\otimes T(\mathfrak J_R).}
\tag{4.45}
$$

Let

$$
\begin{gathered}
I=(i_1<\cdots<i_p),
\qquad
J=(j_1<\cdots<j_s),\\
\theta_I:=\theta_{i_1}\cdots\theta_{i_p},
\qquad
\theta_J:=\theta_{j_1}\cdots\theta_{j_s},\\
W:=J_{a_1}\cdots J_{a_q},
\qquad
Z:=J_{b_1}\cdots J_{b_t},\\
|W|:=\sum_{r=1}^{q}|J_{a_r}|\pmod2,
\qquad
|Z|:=\sum_{r=1}^{t}|J_{b_r}|\pmod2,\\
|I|:=\#I\pmod2,
\qquad
|J|:=\#J\pmod2.
\end{gathered}
\tag{4.46}
$$

The tensor-word order \(J_{a_1}\cdots J_{a_q}\) is retained and is never
sorted.

For disjoint \(I,J\), the parameter-left/PBW product is

$$
\boxed{
(\theta_I\otimes W)(\theta_J\otimes Z)
=(-1)^{|W||J|+\operatorname{inv}(I,J)}
\theta_{\operatorname{sort}(I\sqcup J)}\otimes WZ,}
\tag{4.47}
$$

$$
\operatorname{inv}(I,J)
:=\#\{(i,j)\in I\times J:i>j\},
\qquad
(\theta_I\otimes W)(\theta_J\otimes Z)=0
\quad(I\cap J\ne\varnothing).
\tag{4.48}
$$

Let \(\operatorname{DiffLie}_R\) denote the graded differential--Lie
algebra generated by \(\Theta_R\sqcup\mathfrak J_R\), with the commuting
ordinary derivatives in (4.44).  Its associative realization is the map

$$
\iota_R:\operatorname{DiffLie}_R\longrightarrow
\mathcal A_{\rm univ}^{R},
\qquad
\iota_R(\theta_i)=\theta_i,
\qquad
\iota_R(J_a)=J_a,
$$

fixed recursively by

$$
\boxed{
\iota_R\!\left(\llbracket U,V\rrbracket\right)
=\iota_R(U)\iota_R(V)
-(-1)^{|U||V|}\iota_R(V)\iota_R(U).}
\tag{4.49}
$$

On jet generators and products,

$$
\begin{aligned}
\partial_{M_r^R}J_{\Xi,\mathbf n}
&:=J_{\Xi,\mathbf n+\mathbf e_r},\\
\partial_M(UV)&=(\partial_MU)V+U(\partial_MV),\\
\mathcal D_MX&:=\partial_MX-i\llbracket A_M,X\rrbracket,\\
F_{MN}&:=\partial_MA_N-\partial_NA_M
-i\llbracket A_M,A_N\rrbracket,\\
[\mathcal D_M,\mathcal D_N]X
&=-i\llbracket F_{MN},X\rrbracket,\\
\mathcal D_{[M}F_{NP]}&=0.
\end{aligned}
\tag{4.50}
$$
