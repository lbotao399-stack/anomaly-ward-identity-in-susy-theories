# 00 3+1d SUSY QFT — Convention Lock

## Step 3E. \(N=1\) superspace and component Feynman-rule generators

### 3E.1 Domains, weights, and rule labels

$$
R\in\{L,E\},
\qquad
\varkappa_L:=+1,
\qquad
\varkappa_E:=-1,
\qquad
d_8:=2,
\qquad
d_+:=d_-:=3.
\tag{3E.1}
$$

$$
\Box_L:=\eta^{\mu\nu}\partial_\mu^L\partial_\nu^L,
\qquad
\Box_E:=\Delta_E:=\delta^{mn}\partial_m^E\partial_n^E.
\tag{3E.2}
$$

$$
\begin{gathered}
[\mathcal V]=[\mathfrak c]=[\widetilde{\mathfrak c}]=0,
\qquad
[\Phi]=[\widetilde\Phi]=1,
\qquad
[\mathcal W_a]=\frac32,\\
[\nabla_M]=1,
\qquad
[\nabla_a]=[\bar\nabla_{\dot a}]=\frac12,
\qquad
[d^4\vartheta]=2,
\qquad
[d^2\vartheta]=[d^2\bar\vartheta]=1.
\end{gathered}
\tag{3E.3}
$$

For every active non-minimal doublet,

$$
\boxed{
\begin{gathered}
\mathbf s_R\mathfrak u_{R,\ell}=\mathfrak v_{R,\ell},
\qquad
\mathbf s_R\mathfrak v_{R,\ell}=0,\\
\epsilon_{\mathfrak v_\ell}=\epsilon_{\mathfrak u_\ell}+1,
\qquad
\operatorname{gh}(\mathfrak v_\ell)
=\operatorname{gh}(\mathfrak u_\ell)+1,
\qquad
d_\ell:=[\mathfrak u_\ell]=[\mathfrak v_\ell],\\
0\le d_\ell\le d_{\Sigma_\ell}.
\end{gathered}}
\tag{3E.4}
$$

The last line is the power-counting lock.  A negative active \(d_\ell\)
would admit derivative words of unbounded degree.

The Step-3D multiplier kernel is a fixed quadratic normalization:

$$
\boxed{
\mathcal Y_R:=\mu^{-1}\widehat{\mathcal Y}_R,
\qquad
[\widehat{\mathcal Y}_R]=0,
\qquad
[\mathcal Y_R]=-1,
\qquad
\epsilon(\mathcal Y_R)=0,
\qquad
\operatorname{gh}(\mathcal Y_R)=0,
\qquad
\widehat{\mathcal Y}_R
\text{ local, algebraic, analytic, background-covariant,
graded-self-adjoint, and invertible}.}
\tag{3E.5}
$$

$$
\boxed{
\mathcal Y_L^{\ddagger_L}=\mathcal Y_L,
\qquad
\mathcal Y_E\text{ is independent before its cycle},
\qquad
\mathbf s_R\mathcal Y_R
=\frac{\vec\delta\mathcal Y_R}{\delta\Xi_{R,\rm int}^{\mathsf A}}
\mathbf s_R\Xi_{R,\rm int}^{\mathsf A}.}
\tag{3E.5a}
$$

No other inverse-mass derivative coupling is admitted.

Separate integrated coordinates from external insertions:

$$
\boxed{
\begin{aligned}
\Xi_{R,\rm int}^{\mathsf A}
&\in
\left(
\mathcal V_{\rm q},\chi,\widetilde\chi,
\mathfrak c,\widetilde{\mathfrak c},
\{\mathfrak u_\ell,\mathfrak v_\ell\}_{\ell\in\mathscr R_{\rm nm}}
\right),\\
\Xi_{R,\rm ext}^{\boldsymbol\alpha}
&\in
\left(
\overline Q_R,\Omega_R,Q_R^{\star{\rm ext}},
\overline Q_R^{\star{\rm ext}},\Omega_R^\star
\right),\\
\Xi_{R,\rm tot}&:=(\Xi_{R,\rm int};\Xi_{R,\rm ext}).
\end{aligned}}
\tag{3E.6}
$$

The internal symbol ledger is

$$
\boxed{
\begin{array}{c|c|c|c|c|c|c}
X&\varsigma(X)&\text{representation}&\epsilon_X&\operatorname{gh}X&[X]
&\text{Lorentz datum}\\ \hline
\mathcal V_{\rm q}&8&\operatorname{Ad}&0&0&0
&\mathcal V_{L,\rm q}^{\ddagger_L}=\mathcal V_{L,\rm q}\\
\chi&+&\mathcal R&0&0&1
&\widetilde\chi_L=\chi_L^{\ddagger_L}\\
\widetilde\chi&-&\mathcal R^\vee&0&0&1
&\chi_L=\widetilde\chi_L^{\ddagger_L}\\
\mathfrak c&+&\operatorname{Ad}&1&1&0
&\widetilde{\mathfrak c}_L=\mathfrak c_L^{\ddagger_L}\\
\widetilde{\mathfrak c}&-&\operatorname{Ad}&1&1&0
&\mathfrak c_L=\widetilde{\mathfrak c}_L^{\ddagger_L}\\
\mathfrak u_\ell&\varsigma_\ell&\mathcal R_\ell
&\epsilon_\ell&g_\ell&d_\ell
&(\mathfrak u_{L,\ell})^{\ddagger_L}
=(-1)^{\epsilon_\ell}\mathfrak u_{L,\ell^\ddagger}\\
\mathfrak v_\ell&\varsigma_\ell&\mathcal R_\ell
&\epsilon_\ell+1&g_\ell+1&d_\ell
&(\mathfrak v_{L,\ell})^{\ddagger_L}
=\mathfrak v_{L,\ell^\ddagger}
\end{array}}
\tag{3E.6a}
$$

Here
\(\varsigma\in\{8,+,-\}\),
\(g_\ell:=\operatorname{gh}(\mathfrak u_\ell)\), and
\(\epsilon_\ell:=\epsilon_{\mathfrak u_\ell}\).  Every Euclidean row
is independent before its cycle.  For each field row \(Y\),

$$
\boxed{
\begin{array}{c|c|c|c|c}
X_{\rm ext}&\varsigma&\epsilon&\operatorname{gh}&[X_{\rm ext}]\\ \hline
\overline Q_Y&\varsigma(Y)&\epsilon_Y&\operatorname{gh}Y&[Y]\\
\Omega_Y&\varsigma(Y)&\epsilon_Y+1&\operatorname{gh}Y+1&[Y]\\
Q_Y^{\star{\rm ext}}&\varsigma(Y)&\epsilon_Y+1
&-1-\operatorname{gh}Y&d_{\varsigma(Y)}-[Y]
\end{array}}
\tag{3E.6b}
$$

The background antifields \(\overline Q_Y^{\star{\rm ext}}\) and
\(\Omega_Y^\star\) obey the same antifield rule applied to their
respective rows.

Each label contains its superspace domain, gauge representation,
internal or external role, parity, ghost number, dimension, Lorentz
reality datum, Euclidean cycle datum, and Wick block.  Hessians and
internal contractions use only \(\Xi_{R,\rm int}\); vertex derivatives
may also use \(\Xi_{R,\rm ext}\).  No external label is paired by a
Green kernel.

The four rule ledgers are

$$
\boxed{
\mathrm{LS}:=(L,\text{superspace}),\quad
\mathrm{ES}:=(E,\text{superspace}),\quad
\mathrm{LC}:=(L,\text{full unconstrained components}),\quad
\mathrm{EC}:=(E,\text{full unconstrained components}).}
\tag{3E.7}
$$

Every rule also carries

$$
\beta_{\rm NK}\in
\left\{
\mathrm{coupled},
\mathrm{external},
\mathrm{density},
\mathrm{BV\!-!NK}
\right\}.
\tag{3E.8}
$$

### 3E.2 Complete power-counting-renormalizable physical action

After removal of constants and Kähler-exact chiral or antichiral
\(D\)-densities,

$$
\boxed{
\begin{aligned}
\mathscr K_{\rm ren}
&=\widetilde\Phi_I(\mathsf Z\mathcal E)^I{}_J\Phi^J,
\qquad \mathcal E=e^{\mathcal V},\\
\mathscr U_{\rm ren}
&=\ell_I\Phi^I
+\frac12m_{IJ}\Phi^I\Phi^J
+\frac1{3!}y_{IJK}\Phi^I\Phi^J\Phi^K,\\
\widetilde{\mathscr U}_{\rm ren}
&=\widetilde\ell^{I}\widetilde\Phi_I
+\frac12\widetilde m^{IJ}\widetilde\Phi_I\widetilde\Phi_J
+\frac1{3!}\widetilde y^{IJK}
\widetilde\Phi_I\widetilde\Phi_J\widetilde\Phi_K,\\
f_{AB}&=\kappa_{AB}=\kappa_{BA},
\qquad
\widetilde f_{AB}=\widetilde\kappa_{AB}
=\widetilde\kappa_{BA},
\qquad
S_{\rm FI}=\xi_A[\mathcal V^A]_D.
\end{aligned}}
\tag{3E.9}
$$

$$
\boxed{
\begin{gathered}
[\ell]=[\widetilde\ell]=2,
\qquad
[m]=[\widetilde m]=1,
\qquad
[y]=[\widetilde y]=0,\\
m_{IJ}=m_{JI},
\qquad
\widetilde m^{IJ}=\widetilde m^{JI},
\qquad
y_{IJK}=y_{(IJK)},
\qquad
\widetilde y^{IJK}=\widetilde y^{(IJK)},\\
\mathsf Z\text{ is a nondegenerate gauge intertwiner}.
\end{gathered}}
\tag{3E.9a}
$$

The direct Lorentzian and Euclidean physical actions are one typed
formula with the signature coefficient of (3E.1):

$$
\boxed{
\begin{aligned}
S_{0,R}^{\rm ren}
=\varkappa_R\int d^4x_R\Big\{&
[\widetilde\Phi\,\mathsf Z e^{\mathcal V}\Phi]_D
+[\mathscr U_{R,\rm ren}]_F
+[\widetilde{\mathscr U}_{R,\rm ren}]_{\widetilde F}\\
&+\frac14[\kappa_{R,AB}\mathcal W_R^{Aa}\mathcal W^B_{Ra}]_F\\
&+\frac14[\widetilde\kappa_{R,AB}
\widetilde{\mathcal W}_{R\dot a}^{A}
\widetilde{\mathcal W}_R^{B\dot a}]_{\widetilde F}
+\xi_{R,A}[\mathcal V_R^A]_D\Big\}.
\end{aligned}}
\tag{3E.9b}
$$

Thus \(S_{0,L}^{\rm ren}\) has the Step-3A Lorentzian sign and
\(S_{0,E}^{\rm ren}\) has the independently defined direct-Euclidean
overall minus sign.  No Euclidean dagger relation is used in (3E.9b).

The invariant tensors obey

$$
\boxed{
\begin{aligned}
[\mathsf Z,T_A]&=0,\\
\ell_I(T_A)^I{}_J&=0,\\
m_{IK}(T_A)^K{}_J+m_{JK}(T_A)^K{}_I&=0,\\
y_{LJK}(T_A)^L{}_I
+y_{ILK}(T_A)^L{}_J
+y_{IJL}(T_A)^L{}_K&=0,\\
c_{CA}{}^D\kappa_{DB}+c_{CB}{}^D\kappa_{AD}&=0,\\
\xi_Ac_{BC}{}^A&=0.
\end{aligned}}
\tag{3E.10}
$$

The independent dual-representation tensors obey

$$
\boxed{
\begin{aligned}
\widetilde\ell^{I}(T_A)^J{}_{I}&=0,\\
\widetilde m^{IK}(T_A)^J{}_{I}
+\widetilde m^{IJ}(T_A)^K{}_{I}&=0,\\
\widetilde y^{ILM}(T_A)^J{}_{I}
+\widetilde y^{IJM}(T_A)^L{}_{I}
+\widetilde y^{IJL}(T_A)^M{}_{I}&=0,\\
c_{CA}{}^D\widetilde\kappa_{DB}
+c_{CB}{}^D\widetilde\kappa_{AD}&=0.
\end{aligned}}
\tag{3E.10a}
$$

In Lorentzian signature,

$$
\mathsf Z^{\ddagger_L}=\mathsf Z,
\qquad
(\widetilde\ell,\widetilde m,\widetilde y,
\widetilde\kappa)
=(\ell,m,y,\kappa)^{\ddagger_L}.
\tag{3E.11}
$$

In intrinsic Euclidean signature, the tilded tensors are independent
until the cycle is selected.

The non-topological gauge metric is

$$
\boxed{
\mathfrak h_{R,AB}
:=\frac12\left(\kappa_{R,AB}+\widetilde\kappa_{R,AB}\right),
\qquad
c_{CA}{}^D\mathfrak h_{R,DB}
+c_{CB}{}^D\mathfrak h_{R,AD}=0.}
\tag{3E.11a}
$$

On the Lorentzian cycle,
\(\mathfrak h_{L,AB}=\operatorname{Re}\kappa_{L,AB}\).  Every
\(\mathfrak h_R^{-1}\) below is restricted to its declared
nondegenerate invariant color subspace.

The degree bounds follow directly from

$$
\begin{aligned}
d^4\vartheta:&\quad N_\Phi+N_{\widetilde\Phi}\le2,\\
d^2\vartheta:&\quad
N_\Phi+\frac32N_{\mathcal W}\le3,
\qquad N_{\mathcal W}\in2\mathbb Z_{\ge0}.
\end{aligned}
\tag{3E.12}
$$

Hence

$$
N_{\mathcal W}=0\Longrightarrow N_\Phi\le3,
\qquad
N_{\mathcal W}=2\Longrightarrow N_\Phi=0.
\tag{3E.13}
$$

The dimension-zero bridge does not evade gauge invariance.  First, for
every chiral polynomial \(F(\Phi)\) and antichiral polynomial
\(\widetilde F(\widetilde\Phi)\),

$$
\boxed{
\begin{aligned}
[F(\Phi)]_D
&=\int_{R,+}\left[-\frac14\bar D_R^2F(\Phi)\right]
=0,\\
[\widetilde F(\widetilde\Phi)]_D
&=\int_{R,-}\left[-\frac14D_R^2
\widetilde F(\widetilde\Phi)\right]
=0.
\end{aligned}}
\tag{3E.13a}
$$

At matter degree two, write the only nonchiral candidate as
\(\widetilde\Phi K(\mathcal E)\Phi\).  Using (3A.32), invariance for
independent \(h\) and \(\bar h\) requires

$$
K(\bar h\mathcal Eh^{-1})=\bar hK(\mathcal E)h^{-1}.
\tag{3E.13b}
$$

Setting \(\mathcal E=\mathbf1\) and \(\bar h=h\) gives
\(K(\mathbf1)=hK(\mathbf1)h^{-1}\).  With
\(\mathsf Z:=K(\mathbf1)\), this is
\([\mathsf Z,T_A]=0\).  Setting instead
\(\mathcal E=\mathbf1\), \(h=\mathbf1\), and \(\bar h=G\) gives

$$
K(G)=GK(\mathbf1),
\qquad
K(\mathcal E)=\mathcal E\mathsf Z=\mathsf Z\mathcal E,
\qquad
[\mathsf Z,T_A]=0,
\tag{3E.13c}
$$

For an Abelian bridge coordinate,
\(\delta\mathcal V=i(\bar\Lambda-\Lambda)\).  A pure-vector
\(D\)-density obeys

$$
\begin{aligned}
\delta\int_{R,8}K(\mathcal V)
&=i\int_{R,8}K'(\mathcal V)(\bar\Lambda-\Lambda),\\
\int_{R,8}K'(\mathcal V)\Lambda
&=\int_{R,+}
\left[-\frac14\bar D_R^2K'(\mathcal V)\right]\Lambda,\\
\bar D_R^2K'(\mathcal V)
&=K''(\mathcal V)\bar D_R^2\mathcal V
+K'''(\mathcal V)
(\bar D_{R\dot a}\mathcal V)(\bar D_R^{\dot a}\mathcal V).
\end{aligned}
\tag{3E.13d}
$$

Arbitrariness of \(\Lambda\), \(\bar D^2\mathcal V\), and
\((\bar D\mathcal V)^2\) gives
\(K''=K'''=0\), hence \(K(\mathcal V)=K_0+\xi\mathcal V\).
The constant integrates to zero.  On a non-Abelian factor the finite
left--right action
\(\mathcal E\mapsto\bar h\mathcal Eh^{-1}\) is locally transitive,
so an invariant pure-bridge scalar is constant.  A linear term
survives precisely on the Abelian quotient:

$$
\boxed{S_{\rm FI}=\xi_A[\mathcal V^A]_D,
\qquad \xi_Ac_{BC}{}^A=0.}
\tag{3E.13e}
$$

Any nonconstant \(f_{AB}(\Phi)\) requires a negative-dimension
coefficient and is excluded.

Dimension-zero prepotentials retain every valence:

$$
\boxed{
\widetilde\Phi\,\mathsf Z e^{\mathcal V}\Phi
=\sum_{n=0}^{\infty}\frac1{n!}
\widetilde\Phi\,\mathsf Z
\mathcal V^{A_1}\cdots\mathcal V^{A_n}
T_{A_1}\cdots T_{A_n}\Phi.}
\tag{3E.14}
$$

For labeled vector legs,

$$
\frac{\vec\delta}{\delta\mathcal V^{A_n}}\cdots
\frac{\vec\delta}{\delta\mathcal V^{A_1}}
\left(\widetilde\Phi\mathsf Z e^{\mathcal V}\Phi\right)\Big|_{\mathcal V=0}
=\frac1{n!}\sum_{\pi\in S_n}
\widetilde\Phi\mathsf Z
T_{A_{\pi(1)}}\cdots T_{A_{\pi(n)}}\Phi.
\tag{3E.15}
$$

The exact curvature generator is

$$
\boxed{
e^{-\mathcal V}D_a e^{\mathcal V}
=\sum_{n=0}^{\infty}
\frac{(-1)^n}{(n+1)!}
\operatorname{ad}_{\mathcal V}^{n}(D_a\mathcal V),
\qquad
\mathcal W_a=-\frac18\bar D^2
\left(e^{-\mathcal V}D_a e^{\mathcal V}\right).}
\tag{3E.16}
$$

Equations (3E.14)--(3E.16) prove that a finite universal vertex table
does not exist.

### 3E.3 Most general renormalizable non-minimal generator

Let \(\mathfrak X_R\) be the canonically ordered jet alphabet

$$
\mathfrak X_R
=\left(
\mathcal V_{\rm q},\chi,\widetilde\chi,
\mathfrak c,\widetilde{\mathfrak c},
\mathfrak u_\ell,\mathfrak v_\ell;
\text{declared backgrounds}
\right).
\tag{3E.17}
$$

For a derivative word \(P\),

$$
\begin{aligned}
d(PX)&=[X]+N_M(P)+\frac12N_s(P),\\
\operatorname{gh}(PX)&=\operatorname{gh}(X),\\
\epsilon(PX)&=\epsilon_X+N_s(P)\pmod2.
\end{aligned}
\tag{3E.18}
$$

Define \(\mathfrak W_{R,\Sigma}^{\rm pc,+}\) as the set of all local,
background-covariant, ordered words

$$
\omega=(P_1X_1)\cdots(P_NX_N)
\tag{3E.19}
$$

with complete spinor, vector, gauge, and matter-index contraction and

$$
\boxed{
\begin{aligned}
[g_{R,\omega}]+\sum_{r=1}^{N}d(P_rX_r)&=d_\Sigma,
& [g_{R,\omega}]&\ge0,\\
\sum_{r=1}^{N}\operatorname{gh}(X_r)&=-1,
&\sum_{r=1}^{N}\epsilon(P_rX_r)&=1\pmod2.
\end{aligned}}
\tag{3E.20}
$$

The word also obeys the chirality condition of \(\Sigma\).  Work in the
formal-adic topology in the dimension-zero letters.  There are two
distinct normal-form maps:

$$
\boxed{
\begin{aligned}
\operatorname{NF}_R^{\rm flat}
&:\ \mathfrak W_R\big/
\langle\text{total superspace derivatives, chirality,
(3E.37)--(3E.41), zero Berezin densities}\rangle,\\
\operatorname{NF}_R^{\rm B}
&:\ \mathfrak W_R^{\rm B}\big/
\langle\text{total background-covariant derivatives, chirality,
(3C.23),(3C.35),(3C.40)--(3C.44), zero Berezin densities}\rangle.
\end{aligned}}
\tag{3E.20a}
$$

The background alphabet \(\mathfrak W_R^{\rm B}\) contains
\(\boldsymbol\nabla_{Ra}\),
\(\bar{\boldsymbol\nabla}_{R\dot a}\),
\(\boldsymbol{\mathcal D}_{Ra\dot a}\), and the independent curvature
letters
\(\boldsymbol{\mathcal W}_{Ra}\),
\(\widetilde{\boldsymbol{\mathcal W}}_{R\dot a}\) with all ordered
background-covariant derivatives.  In particular,

$$
\begin{aligned}
[\bar{\boldsymbol\nabla}_{R\dot a},
\boldsymbol{\mathcal D}_{Rb\dot b}]
&=u_R\epsilon_{\dot a\dot b}
\boldsymbol{\mathcal W}_{Rb},\\
[\boldsymbol\nabla_{Ra},
\boldsymbol{\mathcal D}_{Rb\dot b}]
&=u_R\epsilon_{ab}
\widetilde{\boldsymbol{\mathcal W}}_{R\dot b},
\qquad
(u_L,u_E)=(-2i,-2),
\end{aligned}
\tag{3E.20b}
$$

so no curvature letter is set to zero on the background branch.
Every relation in (3E.20a) is homogeneous in superspace domain,
representation, parity, ghost number, engineering dimension, and
ordered color word; therefore either rewriting preserves all six
types.  Color words are never quotiented by cyclic or symmetric
reordering.  Set

$$
\operatorname{NF}_R^{\rm branch}
:=\begin{cases}
\operatorname{NF}_R^{\rm flat},&overline{\mathcal W}_R
=\widetilde{\overline{\mathcal W}}_R=0,\\
\operatorname{NF}_R^{\rm B},&\text{arbitrary background}.
\end{cases}
\tag{3E.20c}
$$

Here \(\overline{\mathcal W}_R\) and
\(\widetilde{\overline{\mathcal W}}_R\) are the two background
supercurvatures constructed from \(\overline Q_R\).

The complete gauge-fermion family is

$$
\boxed{
\Psi_R^{\rm pc}
:=-\frac{b_{Y,R}}2\langle\mathfrak c'_R,
\mathcal Y_R\mathfrak n_R\rangle_R
+\sum_{\Sigma\in\{8,+,-\}}
\int_{R,\Sigma}
\sum_{\omega\in\operatorname{NF}_R^{\rm branch}(
\mathfrak W_{R,\Sigma}^{\rm pc,+})}
g_{R,\omega}\operatorname{Contr}_\omega
\left[(P_1X_1)\cdots(P_NX_N)\right].}
\tag{3E.21}
$$

Here \(b_{Y,R}\in\{0,1\}\); \(b_{Y,R}=1\) exactly when the typed
standard multiplier pair is selected.  Thus the first term in
(3E.21) is the unique admitted negative-dimension quadratic
normalization, and it may be absent on a general coupled branch.  The direct word
\(\langle\mathfrak c'_R,\mathcal F_R\rangle_R\) belongs to the
nonnegative-dimension sum.  No derivative acts on the explicit
\(\mu^{-1}\) in \(\mathcal Y_R\).

$$
(\Psi_L^{\rm pc})^{\ddagger_L}=-\Psi_L^{\rm pc},
\qquad
\Psi_E^{\rm pc}
\text{ has independent tilded and untilded arguments}.
\tag{3E.22}
$$

The universal non-minimal theory is the union over arbitrary finite
typed sets \(\mathscr R_{\rm nm}\).  The admitted family is

$$
\boxed{
\begin{aligned}
\mathfrak G_R^{\rm pc}:=
\bigg\{\Psi_R^{\rm pc}:\;&
\mathcal M_{\Psi,R,\nu}^{\rm FP,\perp}:
\mathscr G_{\Psi,R,\nu}^{\perp}
\overset{\cong}{\longrightarrow}
\mathscr F_{\Psi,R,\nu}^{\perp},\\
&\operatorname{Hess}\mathbb A_{R,\nu}\big|_{
\mathscr H_{\Psi,R,\nu}^{\perp}}
\text{ is nondegenerate}\bigg\}.
\end{aligned}}
\tag{3E.22a}
$$

A doublet is active exactly when it occurs in an element of
\(\mathfrak G_R^{\rm pc}\).

For a direct antighost term,

$$
\int_{R,\Sigma_\ell}\mathfrak u_\ell\mathcal F_\ell:
\qquad
[\mathcal F_\ell]=d_{\Sigma_\ell}-d_\ell,
\quad
\operatorname{gh}(\mathcal F_\ell)=-1-\operatorname{gh}(\mathfrak u_\ell),
\quad
\epsilon(\mathcal F_\ell)=1-\epsilon_{\mathfrak u_\ell}.
\tag{3E.23}
$$

For a quadratic doublet word,

$$
\int_{R,\Sigma}\mathfrak u_\ell
\mathcal K_{\ell m}\mathfrak v_m:
\quad
[\mathcal K_{\ell m}]=d_\Sigma-d_\ell-d_m,
\quad
\operatorname{gh}(\mathcal K_{\ell m})=-2-g_\ell-g_m,
\quad
\epsilon(\mathcal K_{\ell m})=\epsilon_\ell+\epsilon_m.
\tag{3E.24}
$$

For the standard antighost
\(g_\ell=-1\), \(d_\ell=2\), and
\(\Sigma\in\{+,-\}\),

$$
[\mathcal K_{\ell\ell}]=3-2(2)=-1,
\tag{3E.25}
$$

which is exactly the fixed normalization (3E.5).

Define the Boolean predicates

$$
\begin{aligned}
B_{R,\rm std}&:=
[\Psi_R=\Psi_{\mathcal F,\mathcal Y,R}]
[\mathbf s_R\mathcal Y_R=0],\\
B_{R,\rm ext}&:=
\prod_{x_{R,\nu}^{\mathsf r}}
\left[
\frac{\vec\partial\mathcal Y_R}{\partial x_{R,\nu}^{\mathsf r}}=0
\right]
\left[
\frac{\vec\partial\mathfrak F_{R,\nu}^{\rm NK,req}}
{\partial x_{R,\nu}^{\mathsf r}}=0
\right],\\
B_{R,\rm BV}&:=
[\text{every map, cycle, density, normalized-integral,
master, and QME equality in (3D.96b) holds}].
\end{aligned}
\tag{3E.25a}
$$

Here \([P]\in\{0,1\}\) is the truth value of \(P\), and
\(B_{R,\rm BV}=1\) implies \(B_{R,\rm std}=1\).  The four NK branches
are the disjoint partition

$$
\boxed{
\begin{aligned}
\beta_{\rm NK}=\mathrm{BV\!-!NK}
&\Longleftrightarrow B_{R,\rm BV}=1,\\
\beta_{\rm NK}=\mathrm{coupled}
&\Longleftrightarrow B_{R,\rm BV}=0, B_{R,\rm std}=0,\\
\beta_{\rm NK}=\mathrm{external}
&\Longleftrightarrow B_{R,\rm BV}=0, B_{R,\rm std}=1,
B_{R,\rm ext}=1,\\
\beta_{\rm NK}=\mathrm{density}
&\Longleftrightarrow B_{R,\rm BV}=0, B_{R,\rm std}=1,
B_{R,\rm ext}=0.
\end{aligned}}
\tag{3E.26}
$$

Their rule carriers are, respectively,

$$
\begin{array}{c|c|c}
\beta_{\rm NK}&\text{integrated NK coordinates}&\text{rule contribution}\\ \hline
\mathrm{coupled}&\varnothing&
(\mathfrak c',\mathfrak c,\mathfrak n)\text{ complete mixed Hessian}\\
\mathrm{external}&\varnothing&
\mathfrak F_{R,\nu}^{\rm NK,req}\text{ outside the integral}\\
\mathrm{density}&\varnothing&
\tau_R^{-1}\delta^n\log\mathfrak F_{R,\nu}^{\rm NK,req}\\
\mathrm{BV\!-!NK}&\mathscr R_{\rm NK}^{\rm BV}&
W_{\Psi,R,\nu}\text{ Hessian and vertices}
\end{array}.
\tag{3E.26a}
$$

### 3E.4 Fourier, Berezin deltas, and spinor projectors

Fix

$$
\boxed{
\begin{aligned}
X_L(x_L,\vartheta,\bar\vartheta)
&=\int\frac{d^4p_L}{(2\pi)^4}
e^{+ip_{L\mu}x_L^\mu}X_L(p_L,\vartheta,\bar\vartheta),\\
X_E(x_E,\vartheta,\bar\vartheta)
&=\int\frac{d^4p_E}{(2\pi)^4}
e^{+ip_{Em}x_E^m}X_E(p_E,\vartheta,\bar\vartheta).
\end{aligned}}
\tag{3E.27}
$$

$$
\partial_\mu^L\mapsto ip_{L\mu},
\quad
\partial_m^E\mapsto ip_{Em},
\quad
\Box_L\mapsto-p_L^2,
\quad
\Delta_E\mapsto-p_E^2,
\tag{3E.28}
$$

where

$$
p_L^2:=\eta^{\mu\nu}p_{L\mu}p_{L\nu},
\qquad
p_E^2:=\delta^{mn}p_{Em}p_{En}.
\tag{3E.29}
$$

All vertex momenta are incoming:

$$
\int d^4x_R\,e^{i(p_1+\cdots+p_n)\cdot x_R}
=(2\pi)^4\delta_R^{(4)}(p_1+\cdots+p_n).
\tag{3E.30}
$$

The Wick exponent gives

$$
p_{Ei}=p_{Li},
\qquad
p_{E4}=-ip_{L0},
\qquad
p_E^2=p_L^2.
\tag{3E.31}
$$

Thus

$$
\begin{aligned}
D_a^L(p)&=\partial_a
+(\sigma_L^\mu p_{L\mu})_{a\dot b}\bar\vartheta^{\dot b},\\
\bar D_{L\dot a}(p)&=\bar\partial_{\dot a}
-\vartheta^b(\sigma_L^\mu p_{L\mu})_{b\dot a},\\
D_a^E(p)&=\partial_a
+i(\sigma_E^m p_{Em})_{a\dot b}\bar\vartheta^{\dot b},\\
\bar D_{E\dot a}(p)&=\bar\partial_{\dot a}
-i\vartheta^b(\sigma_E^m p_{Em})_{b\dot a}.
\end{aligned}
\tag{3E.32}
$$

The normalized Grassmann deltas are

$$
\delta_\vartheta^{(2)}(\vartheta-\vartheta')
:=(\vartheta-\vartheta')^2,
\qquad
\delta_{\bar\vartheta}^{(2)}(\bar\vartheta-\bar\vartheta')
:=(\bar\vartheta-\bar\vartheta')^2.
\tag{3E.33}
$$

$$
\boxed{
\begin{aligned}
\delta_{R,8}(z,z')
&:=\delta_R^{(4)}(x-x')
\delta_\vartheta^{(2)}(\vartheta-\vartheta')
\delta_{\bar\vartheta}^{(2)}(\bar\vartheta-\bar\vartheta'),\\
\delta_{R,+}(z,z')
&:=-\frac14\bar D_{R,z}^{2}\delta_{R,8}(z,z'),\\
\delta_{R,-}(z,z')
&:=-\frac14D_{R,z}^{2}\delta_{R,8}(z,z').
\end{aligned}}
\tag{3E.34}
$$

$$
\begin{aligned}
\int_{R,8}'\delta_{R,8}(z,z')X_8(z')&=X_8(z),\\
\int_{R,+}'\delta_{R,+}(z,z')X_+(z')&=X_+(z),\\
\int_{R,-}'\delta_{R,-}(z,z')X_-(z')&=X_-(z).
\end{aligned}
\tag{3E.35}
$$

At finite cutoff, every \(\delta_{R,\varsigma}\) in (3E.34)--(3E.35)
is replaced by \(\delta_{R,\nu,\varsigma}\) of (3D.20), and the right
side is the regulated projector:

$$
\boxed{
\int_{R,\varsigma}'
\delta_{R,\nu,\varsigma}(z,z')X(z')
=(P_{R,\nu,\varsigma}X)(z).}
\tag{3E.35a}
$$

All Step-3E inverses use (3E.35a).  Equation (3E.35) is used only if
convergence to the identity has been proved on a separately declared
test-field class; no such continuum limit is assumed here.

Set

$$
C_L:=2i,
\qquad
C_E:=-2,
\qquad
\mathcal G^R_{a\dot b}:=
C_R(\sigma_R^M)_{a\dot b}\partial_M.
\tag{3E.36}
$$

Then

$$
\{D_{Ra},\bar D_{R\dot b}\}=\mathcal G^R_{a\dot b},
\qquad
\mathcal G^R_{a\dot b}\mathcal G_R^{a\dot b}=8\Box_R.
\tag{3E.37}
$$

Direct spinor-index reduction gives

$$
\begin{gathered}
D_aD_b=\frac12\epsilon_{ab}D^2,
\qquad
D^aD^b=-\frac12\epsilon^{ab}D^2,\\
\bar D_{\dot a}\bar D_{\dot b}
=-\frac12\epsilon_{\dot a\dot b}\bar D^2,
\qquad
\bar D^{\dot a}\bar D^{\dot b}
=\frac12\epsilon^{\dot a\dot b}\bar D^2,\\
[D^2,\bar D_{\dot a}]
=2\mathcal G_{a\dot a}D^a,
\qquad
[\bar D^2,D_a]
=-2\mathcal G_{a\dot b}\bar D^{\dot b}.
\end{gathered}
\tag{3E.38}
$$

For

$$
\mathcal X_R:=D_R^a\bar D_R^2D_{Ra}
=\bar D_{R\dot a}D_R^2\bar D_R^{\dot a},
\tag{3E.39}
$$

one obtains

$$
2\mathcal X_R
=D_R^2\bar D_R^2+\bar D_R^2D_R^2-16\Box_R.
\tag{3E.40}
$$

Nilpotency of three equal-chirality spinor derivatives gives

$$
D_R^2\mathcal X_R=0,
\qquad
\bar D_R^2\mathcal X_R=0,
\qquad
D_R^2D_R^2=0,
\qquad
\bar D_R^2\bar D_R^2=0.
\tag{3E.40a}
$$

Multiplying (3E.40) first by \(D_R^2\), then by \(\bar D_R^2\),
gives the two unsuppressed chains

$$
\begin{aligned}
0
&=D_R^2\bar D_R^2D_R^2-16\Box_RD_R^2,\\
0
&=\bar D_R^2D_R^2\bar D_R^2-16\Box_R\bar D_R^2.
\end{aligned}
\tag{3E.40b}
$$

Hence

$$
\boxed{
D_R^2\bar D_R^2D_R^2=16\Box_RD_R^2,
\qquad
\bar D_R^2D_R^2\bar D_R^2=16\Box_R\bar D_R^2.}
\tag{3E.41}
$$

On the declared \(\Box_R\)-invertible complement,

$$
\boxed{
\Pi_{R,+}:=\frac{\bar D_R^2D_R^2}{16\Box_R},
\qquad
\Pi_{R,-}:=\frac{D_R^2\bar D_R^2}{16\Box_R},
\qquad
\Pi_{R,T}:=-\frac{D_R^a\bar D_R^2D_{Ra}}{8\Box_R}.}
\tag{3E.42}
$$

$$
\boxed{
\Pi_{R,r}\Pi_{R,s}=\delta_{rs}\Pi_{R,r},
\qquad
\Pi_{R,+}+\Pi_{R,-}+\Pi_{R,T}=\mathbf1,
\qquad
r,s\in\{+,-,T\}.}
\tag{3E.43}
$$

For example,

$$
\begin{aligned}
\Pi_{R,+}^2
&=\frac{\bar D^2D^2\bar D^2D^2}{(16\Box_R)^2}
=\frac{16\Box_R\bar D^2D^2}{(16\Box_R)^2}
=\Pi_{R,+},\\
\Pi_{R,+}\Pi_{R,-}
&=\frac{\bar D^2(D^2D^2)\bar D^2}{(16\Box_R)^2}=0,\\
\Pi_{R,+}+\Pi_{R,-}+\Pi_{R,T}
&=\frac{\bar D^2D^2+D^2\bar D^2-2\mathcal X_R}
{16\Box_R}=\mathbf1.
\end{aligned}
\tag{3E.43a}
$$

The remaining products follow by exchanging dotted and undotted
indices; \(\Pi_{R,T}^2=\Pi_{R,T}\) follows from completeness and the
four vanishing mixed products.

Let \(P_{R,\nu}:=\bigoplus_\varsigma P_{R,\nu,\varsigma}\) on the
complete typed superspace coefficient space and define

$$
\boxed{
\begin{aligned}
D_{R,\nu a}&:=P_{R,\nu}D_{Ra}P_{R,\nu},
&
\bar D_{R,\nu\dot a}&:=P_{R,\nu}\bar D_{R\dot a}P_{R,\nu},\\
\mathfrak R_{D,R,\nu;a\dot b}
&:=\{D_{R,\nu a},\bar D_{R,\nu\dot b}\}
-P_{R,\nu}\mathcal G^R_{a\dot b}P_{R,\nu}\\
&=-P_{R,\nu}D_{Ra}(\mathbf1-P_{R,\nu})
\bar D_{R\dot b}P_{R,\nu}
-P_{R,\nu}\bar D_{R\dot b}(\mathbf1-P_{R,\nu})
D_{Ra}P_{R,\nu}.
\end{aligned}}
\tag{3E.43b}
$$

The exact flat analytic-rule gate is

$$
\boxed{
\mathfrak B_{R,\nu}^{\rm flat}=1
\Longleftrightarrow
\begin{cases}
P_{R,\nu}^{\rm out}\mathcal O
=\mathcal O P_{R,\nu}^{\rm in}
&\text{for every typed }
\mathcal O\in\{D_R,\bar D_R,\Box_R,
D_R^2,\bar D_R^2,\mathcal X_R,\Pi_{R,+},\Pi_{R,-},\Pi_{R,T}\},\\
[P_{R,\nu},\mathbb P_{\Psi,R,\nu}^{\perp}]=0,
&
\Box_{R,\nu}:=P_{R,\nu}\Box_RP_{R,\nu}
\text{ is invertible on }\mathscr V_{R,\nu}^{\circ},\\
\mathscr V_{R,\nu}^{\circ}
:=\operatorname{span}\{|p,m\rangle:
p\in\Lambda_{R,\nu},\ \Box_R(p)\ne0\}.
\end{cases}}
\tag{3E.43c}
$$

This gate has a direct finite realization in a finite periodic volume.
For a finite Wick-paired momentum set \(\Lambda_{R,\nu}\) and the
complete allowed Grassmann
polynomial fibre \(\mathscr P_\varsigma\), choose

$$
P_{R,\nu,\varsigma}
=\sum_{p\in\Lambda_{R,\nu}}
|p\rangle\langle p|\otimes\mathbf1_{\mathscr P_\varsigma}.
\tag{3E.43d}
$$

Equation (3E.32) gives, for every polynomial \(f\),

$$
\begin{aligned}
D_R(p)(|p\rangle\otimes f)
&=|p\rangle\otimes
\left(\partial_\vartheta f+\alpha_R
\sigma_R\!\cdot\!p\,\bar\vartheta f\right),\\
\bar D_R(p)(|p\rangle\otimes f)
&=|p\rangle\otimes
\left(\partial_{\bar\vartheta}f-\alpha_R
\vartheta\sigma_R\!\cdot\!p\,f\right),
\qquad
\alpha_L=1,\quad\alpha_E=i.
\end{aligned}
\tag{3E.43e}
$$

Both right sides remain at the same momentum and inside the complete
Grassmann fibre.  Therefore
\((\mathbf1-P_{R,\nu})D_RP_{R,\nu}=0\) and
\((\mathbf1-P_{R,\nu})\bar D_RP_{R,\nu}=0\); repeated multiplication
proves every intertwiner in (3E.43c).  A residual projector built
modewise from (3E.42) commutes with the same \(P_{R,\nu}\).  On
\(\mathscr V_{R,\nu}^{\circ}\), set

$$
\Box_{R,\nu}^{-1}\Box_{R,\nu}
=\Box_{R,\nu}\Box_{R,\nu}^{-1}
=P_{R,\nu}|_{\mathscr V_{R,\nu}^{\circ}},
\qquad
\Pi_{R,r,\nu}:=P_{R,\nu}\Pi_{R,r}P_{R,\nu}.
\tag{3E.43f}
$$

Then (3E.37)--(3E.43a) hold at finite \(\nu\), with the identity
replaced by \(P_{R,\nu}|_{\mathscr V_{R,\nu}^{\circ}}\).  No
\(\Box_R^{-1}\) acts on any mode in \(\ker\Box_R\), including every
Lorentzian lightlike mode, an FP stabilizer, or an undeclared zero
mode.  If \(\mathfrak B_{R,\nu}^{\rm flat}=0\), the nonzero matrix
\(\mathfrak R_{D,R,\nu}\) and the analogous products in
(3E.41)--(3E.43a) are retained; none of the analytic inverses below is
identified with the finite-cutoff propagator.

### 3E.5 Ordered Gaussian and universal rule definition

Fold every field-dependent density into the exponent:

$$
\boxed{
\mathbb A_{R,\nu}
:=W_{\Psi,R,\nu}
+\tau_R^{-1}\log\boldsymbol\varpi_{\Psi,R,\nu}.}
\tag{3E.44}
$$

Until an explicit regulator limit is proved, use the abbreviations

$$
\boxed{
\mathbb A_R\equiv\mathbb A_{R,\nu},
\qquad
\mathbb V_R\equiv\mathbb V_{R,\nu},
\qquad
\mathbb H_R\equiv\mathbb H_{R,\nu},
\qquad
\mathbb G_R\equiv\mathbb G_{R,\nu},
\qquad
\mathcal C_R\equiv\mathcal C_{R,\nu},
\qquad
\boldsymbol\varpi_{\Psi,R}\equiv
\boldsymbol\varpi_{\Psi,R,\nu},
\qquad
\mathbb H_{C,R}\equiv\mathbb H_{C,R,\nu},
\qquad
\mathbb V_{C,R}^{(n)}\equiv\mathbb V_{C,R,\nu}^{(n)}.}
\tag{3E.44a}
$$

No \(\nu\to\infty\) equality is used below.  The typed operations are

$$
\boxed{
\begin{aligned}
\int d\mu_{R,\mathsf A}&:=\int_{R,\varsigma(\mathsf A)},\\
\langle\widetilde x,\mathsf Zx\rangle
&:=\langle\mathsf Z^{\mathsf T}\widetilde x,x\rangle,\\
\langle n,\mathcal F_R^{(1)}v\rangle_R
&:=\langle(\mathcal F_R^{(1)})^\sharp n,v\rangle_R,\\
\langle T^{\mathrm{sT}}\lambda,x\rangle_R
&:=(-1)^{\epsilon_T\epsilon_\lambda}\langle\lambda,Tx\rangle_R,
\qquad
(T^{-1})^{\mathrm{sT}}=(T^{\mathrm{sT}})^{-1},\\
F\frac{\overleftarrow\delta}{\delta\Xi^{\mathsf A}}
&:=(-1)^{\epsilon_{\mathsf A}(\epsilon_F+1)}
\frac{\vec\delta F}{\delta\Xi^{\mathsf A}},\\
(\mathscr Q''_{\Psi,L,\nu})_{\mathsf A\mathsf B}
&:=\left.
\frac{\vec\delta}{\delta\Xi^{\mathsf B}}
\frac{\vec\delta}{\delta\Xi^{\mathsf A}}
\mathscr Q_{\Psi,L,\nu}\right|_{\Xi=\Xi_{\rm vac}}.
\end{aligned}}
\tag{3E.44b}
$$

On the density branch,
\(\boldsymbol\varpi_{\Psi,R,\nu}\) includes
\(\mathfrak F_{R,\nu}^{\rm NK,req}\).  On the external branch that
factor is independent of every integrated coordinate and has no
propagator or vertex.

For ordered left derivatives define

$$
\boxed{
\mathbb V_{R;\mathsf A_1\cdots\mathsf A_n}
:=
\left.
\frac{\vec\delta}{\delta\Xi_{R,\rm tot}^{\mathsf A_n}}
\cdots
\frac{\vec\delta}{\delta\Xi_{R,\rm tot}^{\mathsf A_1}}
\mathbb A_{R,\nu}
\right|_{\Xi_{\rm int}=\Xi_{\rm vac}}.}
\tag{3E.45}
$$

The Taylor reconstruction is

$$
\boxed{
\mathbb A_{R,\nu}[\Xi_{\rm vac}+\xi_{\rm int};
\Xi_{\rm ext}+\xi_{\rm ext}]
=\mathbb A_{R,\nu}[\Xi_{\rm vac};\Xi_{\rm ext}]
+\sum_{n=1}^{\infty}\frac1{n!}
\xi^{\mathsf A_1}\cdots\xi^{\mathsf A_n}
\mathbb V_{R;\mathsf A_1\cdots\mathsf A_n}.}
\tag{3E.46}
$$

Every odd permutation is fixed by its Koszul sign:

$$
\mathbb V_{R;\mathsf A_{\pi(1)}\cdots\mathsf A_{\pi(n)}}
=(-1)^{\kappa(\pi;\epsilon)}
\mathbb V_{R;\mathsf A_1\cdots\mathsf A_n}.
\tag{3E.47}
$$

The quadratic Hessian is

$$
\mathbb H_{R;\mathsf A\mathsf B}
:=\mathbb V_{R;\mathsf A\mathsf B},
\qquad
\mathsf A,\mathsf B\in\Xi_{R,\rm int}.
\tag{3E.48}
$$

In the canonical internal order

$$
\mathsf I=(\mathsf P,\mathsf C,\mathsf N,\mathsf K)
:=(\text{physical},\text{minimal ghosts},
\text{base non-minimal},\text{BV--NK}),
$$

the complete quadratic operator is

$$
\boxed{
\mathbb H_R=
\begin{pmatrix}
H_{\mathsf PP}&H_{\mathsf PC}&H_{\mathsf PN}&H_{\mathsf PK}\\
H_{\mathsf CP}&H_{\mathsf CC}&H_{\mathsf CN}&H_{\mathsf CK}\\
H_{\mathsf NP}&H_{\mathsf NC}&H_{\mathsf NN}&H_{\mathsf NK}\\
H_{\mathsf KP}&H_{\mathsf KC}&H_{\mathsf KN}&H_{\mathsf KK}
\end{pmatrix},
\qquad
H_{\mathsf XY}
=\frac{\vec\delta_{\mathsf Y}\vec\delta_{\mathsf X}}
{\delta\Xi_{\mathsf Y}\delta\Xi_{\mathsf X}}
(S_{0,R}^{\rm ren}+\mathbf s_R\Psi_R^{\rm pc})
+\tau_R^{-1}
\frac{\vec\delta_{\mathsf Y}\vec\delta_{\mathsf X}}
{\delta\Xi_{\mathsf Y}\delta\Xi_{\mathsf X}}
\log\boldsymbol\varpi_{\Psi,R}.}
\tag{3E.48a}
$$

An absent branch has a zero-dimensional \(\mathsf K\) block.  Higgs,
coupled FP--multiplier, density, arbitrary-doublet, and admitted BV--NK
mixings are precisely the off-diagonal blocks in (3E.48a).  For every
typed split

$$
\mathbb H_R=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad
S_A:=A-BD^{-1}C,
$$

ordered block multiplication gives

$$
\boxed{
\mathbb H_R^{-1}=
\begin{pmatrix}
S_A^{-1}&-S_A^{-1}BD^{-1}\\
-D^{-1}CS_A^{-1}&D^{-1}+D^{-1}CS_A^{-1}BD^{-1}
\end{pmatrix}.}
\tag{3E.48b}
$$

Equation (3E.48b) is applied recursively only when every displayed
inverse exists between the paired residual field and dual spaces.

Its Green kernel is defined by both compositions:

$$
\boxed{
\begin{aligned}
\int_{\mathscr H_{\Psi,R,\nu}^{\perp}}
d\mu_{R,\mathsf C}\,
\mathbb H_{R;\mathsf A\mathsf C}
\mathbb G_R^{\mathsf C\mathsf B}
&=(\widetilde{\mathbb P}_{\Psi,R,\nu}^{\perp})_{\mathsf A}{}^{\mathsf B}
\delta_{R,\varsigma(\mathsf A)},\\
\int_{\mathscr H_{\Psi,R,\nu}^{\perp}}
d\mu_{R,\mathsf C}\,
\mathbb G_R^{\mathsf A\mathsf C}
\mathbb H_{R;\mathsf C\mathsf B}
&=(\mathbb P_{\Psi,R,\nu}^{\perp})^{\mathsf A}{}_{\mathsf B}
\delta_{R,\varsigma(\mathsf B)}.
\end{aligned}}
\tag{3E.49}
$$

Here \(\mathbb P_{\Psi,R,\nu}^{\perp}\) acts on integrated fields and
\(\widetilde{\mathbb P}_{\Psi,R,\nu}^{\perp}\) acts on their duals.
They annihilate \(p=0\), FP stabilizers, cokernel representatives,
and every undeclared zero mode.

For an even Lorentzian block,

$$
\mathbb H_{L,\epsilon}
:=\mathbb H_L+i\hbar\epsilon\mathscr Q_{\Psi,L,\nu}'',
\qquad
\epsilon>0.
\tag{3E.50}
$$

The exact shift is

$$
\boxed{
\frac12\xi\mathbb H_R\xi+J\xi
=\frac12(\xi+\mathbb H_R^{-1}J)\mathbb H_R
(\xi+\mathbb H_R^{-1}J)
-\frac12J\mathbb H_R^{-1}J.}
\tag{3E.50a}
$$

Translation of the normalized cycle by the displayed source shift
gives

$$
\boxed{
\frac{Z_L[J]}{Z_L[0]}
=\exp\left[-\frac{i}{2\hbar}
J\mathbb H_{L,\epsilon}^{-1}J\right],
\qquad
\langle\xi\xi\rangle_{L,c}
=i\hbar\mathbb H_{L,\epsilon}^{-1}.}
\tag{3E.51}
$$

The independent Euclidean completion gives

$$
\boxed{
\frac{Z_E[J]}{Z_E[0]}
=\exp\left[+\frac1{2\hbar}J\mathbb H_E^{-1}J\right],
\qquad
\langle\xi\xi\rangle_{E,c}
=\hbar\mathbb H_E^{-1}.}
\tag{3E.52}
$$

The direct Euclidean coefficient cycle is the ordered product

$$
\boxed{
\mathfrak C_{E,\nu}
=\mathfrak C_{E,\nu}^{\rm even}
\times\mathfrak C_{E,\nu}^{\rm odd}
\times\mathfrak C_{\mathfrak n,E,\nu}
\times\mathfrak C_{{\rm nm},E,\nu}
\times\mathfrak C_{{\rm BV\!-!NK},E,\nu},}
\tag{3E.52a}
$$

with

$$
\operatorname{Re}\frac12x_E\mathbb H_{E,\rm even}x_E>0
\quad(x_E\ne0),
\qquad
\operatorname{Re}\langle f_E,\mathcal Y_E^{-1}f_E\rangle_E>0.
\tag{3E.52b}
$$

Odd coefficient blocks use the fixed Berezin orientation and require
no convergence inequality.  Every remaining even non-minimal or
BV--NK block obeys the first inequality after restriction to its
declared residual cycle.  If such a cycle does not exist, that
gauge-fermion branch is not in \(\mathfrak G_E^{\rm pc}\).

For the canonical direct-Euclidean free blocks, choose the real forms

$$
\mathsf Z_E=\mathsf Z_E^\dagger>0,
\qquad
\mathfrak h_E=\mathfrak h_E^\dagger>0,
\qquad
\mathcal Y_E=\mathcal Y_E^\dagger>0
\tag{3E.52c}
$$

on their declared finite residual spaces.  The bosonic chiral cycle
and its real orientation are

$$
\boxed{
\widetilde\phi_E=\phi_E^\dagger,
\qquad
\widetilde F_E=-F_E^\dagger,
\qquad
\operatorname{or}\mathfrak C_{E,\rm ch}
:=\bigwedge_\alpha^{\prec_\nu}(du^\alpha\wedge dv^\alpha)
\bigwedge_\beta^{\prec_\nu}(ds^\beta\wedge dt^\beta),}
\tag{3E.52d}
$$

where \(\phi=u+iv\) and \(F=s+it\).  The holomorphic coefficient
form has the fixed phase

$$
d\phi\wedge d\widetilde\phi=-2i\,du\wedge dv,
\qquad
dF\wedge d\widetilde F=2i\,ds\wedge dt,
\qquad
J_{E,\rm ch}
=\operatorname{sgn}(\pi_{\rm ch})
(-2i)^{N_\phi}(2i)^{N_F},
\tag{3E.52e}
$$

Here \(\pi_{\rm ch}\) is the permutation from the global
\(\prec_\nu\) coefficient order to the paired
\((\phi,\widetilde\phi;F,\widetilde F)\) order used in (3E.52d).

Using \(\varkappa_E=-1\), the bosonic restriction of (3E.79b) gives

$$
\boxed{
\left.\mathbb A_{C,E,\rm ch,bos}^{(2)}\right|_{\mathfrak C_{E,\rm ch}}
=\int_E\left[
\partial_m\phi^\dagger\mathsf Z_E\partial_m\phi
+F^\dagger\mathsf Z_EF\right]>0
\quad\text{for }(\phi,F)\ne(0,0).}
\tag{3E.52f}
$$

for every nonzero residual bosonic coefficient.  The independent odd
variables \((\psi_E,\widetilde\psi_E)\) carry the reversed Berezin
orientation \(\succ_\nu\).

For the ordinary Feynman-gauge vector block, choose

$$
\boxed{
(A_{E,m}^A)^\dagger=A_{E,m}^A=:a_m^A,
\qquad
\mathscr D_E^A=i d^A,
\qquad
a_m^A,d^A\in\mathbb R.}
\tag{3E.52g}
$$

With orientation
\(\bigwedge^{\prec_\nu}da_m^A\wedge
\bigwedge^{\prec_\nu}dd^A\), the auxiliary phase is
\(J_{E,\mathscr D}=i^{N_{\mathscr D}}\).  Equations
(3E.79e)--(3E.79f) give

$$
\boxed{
\left.\mathbb A_{C,E,V,\rm bos}^{(2)}\right|_{\mathfrak C_{E,V}}
=\frac12\sum_{p\in\Lambda_{E,\nu}^{\circ}}
a_m^A(-p)\mathfrak h_{E,AB}p_E^2a_m^B(p)
+\frac12\sum_{p\in\Lambda_{E,\nu}}
d^A(-p)\mathfrak h_{E,AB}d^B(p)>0
\quad\text{for }(a,d)\ne(0,0).}
\tag{3E.52h}
$$

The gauginos retain the \(\succ_\nu\) Berezin orientation.  On every
even multiplier coefficient set
\(f_E:=\mathcal Y_E^{-1}\mathcal F_E\) and choose the affine thimble

$$
\boxed{
\mathfrak n_E=f_E+i\beta,
\qquad \beta^\dagger=\beta,
\qquad
\operatorname{or}_{\rm fib}\mathfrak C_{\mathfrak n,E,\nu}
:=\bigwedge_\alpha^{\prec_\nu}d\beta^\alpha.}
\tag{3E.52i}
$$

Every odd multiplier coefficient retains \(\succ_\nu\) Berezin order.
Graded self-adjointness gives
\(\langle f_E,\mathcal Y_E\beta\rangle_E
=\langle\beta,\mathcal Y_Ef_E\rangle_E\) on the even block.  Its square
completion contains every cross term:

$$
\begin{aligned}
\langle f_E+i\beta,\mathcal Y_Ef_E\rangle_E
-\frac12\langle f_E+i\beta,
\mathcal Y_E(f_E+i\beta)\rangle_E
&=\langle f_E,\mathcal Y_Ef_E\rangle_E
+i\langle\beta,\mathcal Y_Ef_E\rangle_E\\
&\quad-\frac12\langle f_E,\mathcal Y_Ef_E\rangle_E
-i\langle\beta,\mathcal Y_Ef_E\rangle_E
+\frac12\langle\beta,\mathcal Y_E\beta\rangle_E\\
&=\frac12\langle\mathcal Y_E^{-1}\mathcal F_E,
\mathcal F_E\rangle_E
+\frac12\langle\beta,\mathcal Y_E\beta\rangle_E\ge0,
\end{aligned}
\tag{3E.52j}
$$

The last expression equals zero exactly when
\((\mathcal F_E,\beta)=(0,0)\).

All other even non-minimal blocks enter the admitted EC family only
after an equally explicit middle-dimensional cycle makes their finite
quadratic Hessian strictly positive.  No existential cycle is used to
assign a contact sign.

For any admitted finite even block, let \(c>0\) be the smallest
eigenvalue of its positive real Hessian.  For \(0\le t\le1\),

$$
\begin{aligned}
\operatorname{Re}\left[\frac12xH_Ex+tJx\right]
&\ge\frac c2\lVert x\rVert^2-\lVert J\rVert\lVert x\rVert\\
&\ge\frac c4\lVert x\rVert^2-\frac1c\lVert J\rVert^2,
\end{aligned}
\tag{3E.52k}
$$

because

$$
0\le\left(\frac{\sqrt c}{2}\lVert x\rVert
-\frac1{\sqrt c}\lVert J\rVert\right)^2
=\frac c4\lVert x\rVert^2-\lVert J\rVert\lVert x\rVert
+\frac1c\lVert J\rVert^2.
\tag{3E.52l}
$$

Hence

$$
\mathfrak C_E(t):=\mathfrak C_E+tH_E^{-1}J,
\qquad 0\le t\le1,
\tag{3E.52m}
$$

has unchanged orientation, unit translation Jacobian, no finite
singularity, and zero boundary flux.  Odd source shifts are finite
Berezin translations.

For an ordered odd pair

$$
S^{(2)}=\widetilde\psi K\psi,
\qquad
S_J=\widetilde\eta\psi+\widetilde\psi\eta,
\tag{3E.53}
$$

Its ordered shift expands exactly as

$$
\boxed{
(\widetilde\psi+\widetilde\eta K^{-1})
K(\psi+K^{-1}\eta)-\widetilde\eta K^{-1}\eta
=\widetilde\psi K\psi
+\widetilde\eta\psi+\widetilde\psi\eta.}
\tag{3E.53a}
$$

the same direct Gaussian gives

$$
\boxed{
\langle\psi\widetilde\psi\rangle_{L,c}
=i\hbar K_{L,\epsilon}^{-1},
\qquad
\langle\psi\widetilde\psi\rangle_{E,c}
=\hbar K_E^{-1}.}
\tag{3E.54}
$$

The insertion order is left differentiation by \(\widetilde\eta\)
followed by right differentiation by \(\eta\).

At finite \(\nu\), order all coefficient slots by (3D.18)--(3D.19).
At an even vacuum the graded Hessian has commuting and anticommuting
blocks

$$
\mathbb H_R^{\rm gr}
=A_R\oplus
\begin{pmatrix}0&-K_R^{\mathrm{sT}}\\K_R&0\end{pmatrix},
\qquad
\det
\begin{pmatrix}0&-K_R^{\mathrm{sT}}\\K_R&0\end{pmatrix}
=(\det K_R)^2.
\tag{3E.54a}
$$

The normalized Gaussian, with its square-root branch fixed by the
declared orientation and cycle, is

$$
\boxed{
\frac{Z_R^{(0)}[0;\mathbb H_R]}
{Z_R^{(0)}[0;\mathbb H_{R,0}]}
=\operatorname{Ber}
(\mathbb H_R^{\rm gr}(\mathbb H_{R,0}^{\rm gr})^{-1})^{-1/2}
=\det(A_RA_{R,0}^{-1})^{-1/2}
\det(K_RK_{R,0}^{-1}).}
\tag{3E.54b}
$$

Thus an even coefficient pair contributes determinant power
\(-1/2\), an odd complex pair contributes \(+1\), and a
parity-reversed superghost slot is assigned by
\(\epsilon_{\rm coefficient}=\epsilon_X+|m|\pmod2\), not by the
parity of the parent superfield alone.

For odd FP coefficients with
\(\langle\gamma_j\widetilde\gamma_i\rangle=C_{ji}\), the connected
two-vertex cycle is

$$
\begin{aligned}
&\left\langle
(\widetilde\gamma_iV_1{}^i{}_j\gamma^j)
(\widetilde\gamma_kV_2{}^k{}_l\gamma^l)
\right\rangle_c\\
&\quad
=-V_1{}^i{}_jC^j{}_kV_2{}^k{}_lC^l{}_i
=-\operatorname{Tr}(V_1CV_2C).
\end{aligned}
\tag{3E.54c}
$$

The minus sign is the single move of the first
\(\widetilde\gamma_i\) through the remaining three odd letters.  For
an \(n\)-vertex cycle it crosses \(2n-1\) odd letters and gives

$$
\boxed{
\left\langle\prod_{r=1}^n
(\widetilde\gamma V_r\gamma)\right\rangle_{c,\rm one\ cycle}
=-\operatorname{Tr}(V_1C\cdots V_nC).}
\tag{3E.54d}
$$

Thus every internal line and vertex factor is

$$
\boxed{
\mathcal C_L=i\hbar\mathbb G_{L,\epsilon},
\qquad
\mathcal C_E=\hbar\mathbb G_E,
\qquad
\mathcal U_R^{(n)}=\tau_R\mathbb V_R^{(n)}.}
\tag{3E.55}
$$

For a vertex species \(v\) of valence \(n_v\), and fixed
multiplicities \(N_v\), the exact graph coefficient from fully
labeled half-edge pairings is

$$
\boxed{
\mathcal A_\Gamma
=\left(\prod_v
\frac{(\tau_R\mathbb V_v)^{N_v}}
{N_v!\,(n_v!)^{N_v}}\right)
\sum_{P\,:\,P\to\Gamma}
(-1)^{\kappa(P;\epsilon)}
\prod_{e\in P}\mathcal C_{R,e}.}
\tag{3E.56}
$$

The pairing sum, not an imported graph factor, fixes every identical-leg
stabilizer, closed odd-loop sign, color order, and symmetry factor.

For fixed \(\{N_v\}\), define the labeled half-edge set and its full
slot-label group

$$
\boxed{
\mathscr H_{\rm lab}
:=\bigsqcup_v\{(v,k,r):1\le k\le N_v, 1\le r\le n_v\},
\qquad
\mathscr G_{\rm lab}
:=\prod_v\left(S_{N_v}\ltimes(S_{n_v})^{N_v}\right).}
\tag{3E.56b}
$$

A half-edge carries the complete decoration

$$
\boxed{
\mathfrak d(v,k,r)
:=(\mathsf A_{v,r},\varsigma_{v,r},o_{v,r},c_{v,r},
\mathscr D_{v,r},\epsilon_{v,r}),
\qquad
\mathscr G_{\rm lab}^{\rm typ}
:=\left\{g\in\mathscr G_{\rm lab}:
\begin{array}{l}
\mathfrak d(gh)=\mathfrak d(h),\\
g^*\mathbb V_v=(-1)^{\kappa(g;\epsilon)}\mathbb V_v
\end{array}
\ \forall h,v\right\}.}
\tag{3E.56b1}
$$

Here \(o\), \(c\), and \(\mathscr D\) are respectively orientation,
ordered color slot, and spinor-derivative word.  Thus
\(\mathscr G_{\rm lab}^{\rm typ}\) permutes vertex copies and only
those slots whose complete decorations agree; its action on an odd
vertex tensor includes the displayed Koszul character.

A labeled Wick pairing \(P\) is a type-compatible fixed-point-free
involution on the internal subset of \(\mathscr H_{\rm lab}\), together
with a type-compatible bijection from the remaining half-edges to the
labeled external legs.  The map \(P\mapsto\Gamma\) forgets
\((k,r)\) but retains vertex species, field type, orientation, color
word, derivative order, and external labels.  The typed pairing set
need not be one orbit.  Its exact decomposition is

$$
\boxed{
\begin{aligned}
\mathscr P_\Gamma^{\rm typ}
&:=\{P:P\mapsto\Gamma\}
=\bigsqcup_{\alpha\in I_\Gamma}\mathcal O_{\Gamma,\alpha},\\
\mathcal O_{\Gamma,\alpha}
&:=\mathscr G_{\rm lab}^{\rm typ}\!\cdot P_\alpha,
\qquad
\operatorname{Aut}_{\rm typ}(\Gamma,P_\alpha)
:=\operatorname{Stab}_{\mathscr G_{\rm lab}^{\rm typ}}(P_\alpha),\\
|\mathcal O_{\Gamma,\alpha}|
&=\frac{|\mathscr G_{\rm lab}^{\rm typ}|}
{|\operatorname{Aut}_{\rm typ}(\Gamma,P_\alpha)|},\\
\sum_{P\in\mathscr P_\Gamma^{\rm typ}}w(P)
&=\sum_{\alpha\in I_\Gamma}
\sum_{g\in
\mathscr G_{\rm lab}^{\rm typ}/
\operatorname{Aut}_{\rm typ}(\Gamma,P_\alpha)}
w(gP_\alpha),\qquad
w(P):=(-1)^{\kappa(P;\epsilon)}
\prod_{e\in P}\mathcal C_{R,e}.
\end{aligned}}
\tag{3E.56c}
$$

Equation (3E.56), together with (3E.56c), is the symmetry-factor
formula for mixed typed vertices.  A reduction to one
\(1/|\operatorname{Aut}\Gamma|\) factor is permitted only after
proving \(|I_\Gamma|=1\) and constancy of the complete tensor weight
on that orbit.  No such reduction is used below.

For \(\mathbb A_{\rm int}=\lambda\xi^4/4!\), one first-order vertex
with four labeled external contractions gives

$$
\boxed{
\frac{\tau_R\lambda}{4!}
\sum_{\pi\in S_4}1
=\frac{\tau_R\lambda}{4!}(4!)
=\tau_R\lambda.}
\tag{3E.56a}
$$

### 3E.6 Superspace quadratic kernels

Equations (3E.57)--(3E.72) are the translation-invariant flat-background
specialization on the finite regulator (3E.43d), with
\(\mathfrak B_{R,\nu}^{\rm flat}=1\).  Every displayed operator is its
restriction to \(\mathscr V_{R,\nu}^{\circ}\), every identity is the
projected identity of (3E.43f), the background connection has zero
curvature, and all remaining backgrounds are constant external
insertions.  For any other finite regulator, (3E.72a), not
(3E.58)--(3E.71a), defines the Hessian and its two-sided inverse.

For the canonical massless chiral pair, let

$$
\mathbb X_R:=(\Phi_R^I,\widetilde\Phi_{R,I}).
\tag{3E.57}
$$

The matter-index order follows directly from the ordered derivatives:

$$
\boxed{
\begin{aligned}
\frac{\vec\delta}{\delta\widetilde\Phi_J}
\frac{\vec\delta}{\delta\Phi^I}
(\widetilde\Phi_K\mathsf Z^K{}_L\Phi^L)
&=\mathsf Z^J{}_I=(\mathsf Z^{\mathsf T})_I{}^J,\\
\frac{\vec\delta}{\delta\Phi^J}
\frac{\vec\delta}{\delta\widetilde\Phi_I}
(\widetilde\Phi_K\mathsf Z^K{}_L\Phi^L)
&=\mathsf Z^I{}_J.
\end{aligned}}
\tag{3E.57a}
$$

Direct conversion of the mixed \(D\)-term to typed chiral and
antichiral pairings gives

$$
\boxed{
\mathbb H_{{\rm ch},R}
=\varkappa_R
\begin{pmatrix}
0&-\dfrac14\mathsf Z^{\mathsf T}\bar D_R^2\\[1mm]
-\dfrac14\mathsf ZD_R^2&0
\end{pmatrix}.}
\tag{3E.58}
$$

Its exact two-sided inverse is

$$
\boxed{
\mathbb H_{{\rm ch},R}^{-1}
=-\varkappa_R
\begin{pmatrix}
0&\dfrac14\mathsf Z^{-1}\bar D_R^2\Box_R^{-1}\\[1mm]
\dfrac14(\mathsf Z^{-1})^{\mathsf T}
D_R^2\Box_R^{-1}&0
\end{pmatrix}.}
\tag{3E.59}
$$

For example,

$$
\left(-\frac{\varkappa_R}{4}\mathsf Z^{\mathsf T}\bar D^2\right)
\left(-\frac{\varkappa_R}{4}(\mathsf Z^{-1})^{\mathsf T}
D^2\Box_R^{-1}\right)
=\frac{\bar D^2D^2}{16\Box_R}=\Pi_{R,+}.
\tag{3E.60}
$$

The other three left/right compositions give
\(\Pi_{R,+}\) or \(\Pi_{R,-}\).

Explicitly,

$$
\boxed{
\begin{aligned}
H_{12}G_{21}
&=\frac{\mathsf Z^{\mathsf T}(\mathsf Z^{-1})^{\mathsf T}
\bar D^2D^2}
{16\Box_R}=\Pi_{R,+},\\
H_{21}G_{12}
&=\frac{\mathsf Z\mathsf Z^{-1}D^2\bar D^2}
{16\Box_R}=\Pi_{R,-},\\
G_{12}H_{21}
&=\frac{\mathsf Z^{-1}\mathsf Z\bar D^2D^2}
{16\Box_R}=\Pi_{R,+},\\
G_{21}H_{12}
&=\frac{(\mathsf Z^{-1})^{\mathsf T}\mathsf Z^{\mathsf T}
D^2\bar D^2}
{16\Box_R}=\Pi_{R,-}.
\end{aligned}}
\tag{3E.60a}
$$

For the general stationary-vacuum chiral block,

$$
\boxed{
\mathbb H_{{\rm ch},R}(m,\widetilde m)
=\varkappa_R
\begin{pmatrix}
m&-\dfrac14\mathsf Z^{\mathsf T}\bar D_R^2\\[1mm]
-\dfrac14\mathsf ZD_R^2&\widetilde m
\end{pmatrix}.}
\tag{3E.61}
$$

Its propagator is (3E.51) or (3E.52) with the unique two-sided typed
inverse of (3E.61).  In any invertible diagonal Schur chart,

$$
\begin{aligned}
\mathbb S_{\widetilde m}
&:=\widetilde m
-\frac1{16}\mathsf ZD^2m^{-1}
\mathsf Z^{\mathsf T}\bar D^2,\\
\mathbb H_{{\rm ch},R}^{-1}
&=\varkappa_R
\begin{pmatrix}
m^{-1}+m^{-1}B\mathbb S_{\widetilde m}^{-1}Cm^{-1}
&-m^{-1}B\mathbb S_{\widetilde m}^{-1}\\
-\mathbb S_{\widetilde m}^{-1}Cm^{-1}
&\mathbb S_{\widetilde m}^{-1}
\end{pmatrix},\\
B&:=-\frac14\mathsf Z^{\mathsf T}\bar D^2,
\qquad
C:=-\frac14\mathsf ZD^2.
\end{aligned}
\tag{3E.62}
$$

Equation (3E.62) is used only when every displayed inverse exists.

At quadratic order,

$$
\mathcal W_{Ra}^{A}
=-\frac18\bar D_R^2D_{Ra}\mathcal V_R^A,
\qquad
\widetilde{\mathcal W}_{R\dot a}^{A}
=-\frac18D_R^2\bar D_{R\dot a}\mathcal V_R^A.
\tag{3E.63}
$$

Chirality gives

$$
\begin{aligned}
\mathcal W^{Aa}\mathcal W_a^B
&=\frac1{64}
(\bar D^2D^a\mathcal V^A)(\bar D^2D_a\mathcal V^B)\\
&=\frac1{64}\bar D^2
\left[(D^a\mathcal V^A)(\bar D^2D_a\mathcal V^B)\right]\\
&=-\frac14\bar D^2
\left[-\frac1{16}(D^a\mathcal V^A)
(\bar D^2D_a\mathcal V^B)\right].
\end{aligned}
\tag{3E.63a}
$$

Therefore, using the Project identities
\(\int_{R,+}(-\bar D^2Y/4)=\int_{R,8}Y\) and (3E.75),

$$
\begin{aligned}
\int_{R,+}\mathcal W^{Aa}\mathcal W_a^B
&=-\frac1{16}\int_{R,8}
(D^a\mathcal V^A)(\bar D^2D_a\mathcal V^B)\\
&=+\frac1{16}\int_{R,8}
\mathcal V^A D^a\bar D^2D_a\mathcal V^B.
\end{aligned}
\tag{3E.63b}
$$

The antichiral calculation is

$$
\begin{aligned}
\widetilde{\mathcal W}_{\dot a}^A
\widetilde{\mathcal W}^{B\dot a}
&=\frac1{64}D^2
\left[(\bar D_{\dot a}\mathcal V^A)
(D^2\bar D^{\dot a}\mathcal V^B)\right],\\
\int_{R,-}\widetilde{\mathcal W}_{\dot a}^A
\widetilde{\mathcal W}^{B\dot a}
&=-\frac1{16}\int_{R,8}
(\bar D_{\dot a}\mathcal V^A)
(D^2\bar D^{\dot a}\mathcal V^B)\\
&=+\frac1{16}\int_{R,8}
\mathcal V^AD^a\bar D^2D_a\mathcal V^B.
\end{aligned}
\tag{3E.63c}
$$

Full-to-chiral conversion and ordered integration by parts give

$$
\begin{aligned}
\int_{R,+}\mathcal W^{Aa}\mathcal W_a^B
&=\frac1{16}\int_{R,8}
\mathcal V^A D^a\bar D^2D_a\mathcal V^B,\\
\int_{R,-}\widetilde{\mathcal W}_{\dot a}^A
\widetilde{\mathcal W}^{B\dot a}
&=\frac1{16}\int_{R,8}
\mathcal V^A D^a\bar D^2D_a\mathcal V^B.
\end{aligned}
\tag{3E.64}
$$

$$
\boxed{
\frac{\varkappa_R}{4}\frac1{16}
(\kappa_{R,AB}+\widetilde\kappa_{R,AB})
=\frac{\varkappa_R}{64}(2\mathfrak h_{R,AB})
=\frac{\varkappa_R}{32}\mathfrak h_{R,AB}.}
\tag{3E.64a}
$$

Therefore

$$
\boxed{
\begin{aligned}
S_{V,R}^{(2)}
&=\frac{\varkappa_R}{32}
\int_{R,8}\mathcal V^A\mathfrak h_{R,AB}
D^a\bar D^2D_a\mathcal V^B\\
&=-\frac{\varkappa_R}{4}
\int_{R,8}\mathcal V^A\mathfrak h_{R,AB}
\Box_R\Pi_{R,T}\mathcal V^B.
\end{aligned}}
\tag{3E.65}
$$

With \(S^{(2)}=\frac12\int\mathcal V\mathbb H_V\mathcal V\),

$$
\boxed{
\mathbb H_{T,R}
=-\frac{\varkappa_R}{2}\mathfrak h_R\Box_R\Pi_{R,T},
\qquad
\mathbb H_{T,R}^{-1}
=-2\varkappa_R\mathfrak h_R^{-1}\Box_R^{-1}\Pi_{R,T}.}
\tag{3E.66}
$$

Retaining the multiplier gives the exact block

$$
\boxed{
\mathbb H_{(\mathcal V,\mathfrak n),R}
=
\begin{pmatrix}
\mathbb H_{T,R}&(\mathcal F_R^{(1)})^\sharp\\
\mathcal F_R^{(1)}&-\mathcal Y_R
\end{pmatrix}.}
\tag{3E.67}
$$

Define

$$
\mathbb S_{V,R}
:=\mathbb H_{T,R}
+(\mathcal F_R^{(1)})^\sharp
\mathcal Y_R^{-1}\mathcal F_R^{(1)}.
\tag{3E.68}
$$

Then

$$
\boxed{
\mathbb H_{(\mathcal V,\mathfrak n),R}^{-1}
=
\begin{pmatrix}
\mathbb S_{V,R}^{-1}
&\mathbb S_{V,R}^{-1}(\mathcal F_R^{(1)})^\sharp
\mathcal Y_R^{-1}\\
\mathcal Y_R^{-1}\mathcal F_R^{(1)}\mathbb S_{V,R}^{-1}
&-\mathcal Y_R^{-1}
+\mathcal Y_R^{-1}\mathcal F_R^{(1)}\mathbb S_{V,R}^{-1}
(\mathcal F_R^{(1)})^\sharp\mathcal Y_R^{-1}
\end{pmatrix}.}
\tag{3E.69}
$$

Both products with (3E.67) are the typed identity on the residual-free
complement.

After exact multiplier elimination,

$$
\mathbb H_{V,R}^{\rm red}
=\mathbb H_{T,R}
+(\mathcal F_R^{(1)})^\sharp
\mathcal Y_R^{-1}\mathcal F_R^{(1)}.
\tag{3E.70}
$$

On the present flat standard-gauge specialization,

$$
\mathcal F_R^{(1)}v
=\left(-\frac14\bar D_R^2v,-\frac14D_R^2v\right),
$$

and hence

$$
\boxed{
\mathcal F_R^{(1)}\Pi_{R,T}v
=\frac1{32\Box_R}
\left(
\bar D^2D^a\bar D^2D_av,
D^2D^a\bar D^2D_av
\right)=(0,0).}
\tag{3E.70a}
$$

Therefore

$$
\boxed{
(\mathbb H_{V,R}^{\rm red})^{-1}
=-2\varkappa_R\mathfrak h_R^{-1}\Box_R^{-1}\Pi_{R,T}
+\left[
\Pi_{R,0}(\mathcal F_R^{(1)})^\sharp\mathcal Y_R^{-1}
\mathcal F_R^{(1)}\Pi_{R,0}
\right]^{-1}_{\operatorname{Im}\Pi_{R,0}},
\quad
\Pi_{R,0}:=\Pi_{R,+}+\Pi_{R,-}.}
\tag{3E.71}
$$

With

$$
\mathbb L_R
:=\Pi_{R,0}(\mathcal F_R^{(1)})^\sharp\mathcal Y_R^{-1}
\mathcal F_R^{(1)}\Pi_{R,0},
$$

the final term in (3E.71) is the unique residual inverse satisfying

$$
\boxed{
\mathbb L_R\mathbb L_R^{-1}
=\widetilde{\mathbb P}_{\operatorname{Im}\Pi_0}^{\perp},
\qquad
\mathbb L_R^{-1}\mathbb L_R
=\mathbb P_{\operatorname{Im}\Pi_0}^{\perp}.}
\tag{3E.71a}
$$

No scalar gauge parameter replaces the operator \(\mathcal Y_R\).

The FP quadratic operator is obtained only from

$$
\boxed{
S_{{\rm FP},R}^{(2)}
=-\left\langle\mathfrak c'_R,
\mathcal M_{R}^{\rm FP,(0)}
\mathfrak c_R^{\rm pair}\right\rangle_R,
\qquad
\mathcal M_R^{\rm FP}=d\mathcal F_R\circ\mathscr R_{R,\rm q}.}
\tag{3E.72}
$$

Its line is (3E.54) with the exact inverse of
\(-\mathcal M_R^{\rm FP,(0)}\).  If
\(\mathbf s_R\mathcal Y_R\ne0\), the complete
\((\mathfrak c',\mathfrak c,\mathfrak n)\) Hessian is retained.

On the flat standard branch, set
\(X:=\operatorname{ad}_{\mathcal V_{R,\rm q}}\).  The tangent of the
exact BRST bridge law at the zero prepotential is

$$
\begin{aligned}
\left.\mathbf s_R\mathcal V_{R,\rm q}\right|_0
&=\left.
\frac{X}{1-e^{-X}}
\left(ie^{-X}\widetilde{\mathfrak c}_R-i\mathfrak c_R\right)
\right|_{X=0}\\
&=\left.
\left(1+\frac X2+\frac{X^2}{12}+\cdots\right)
\left[i\left(1-X+\frac{X^2}{2}+\cdots\right)
\widetilde{\mathfrak c}_R-i\mathfrak c_R\right]
\right|_{X=0}\\
&=i\widetilde{\mathfrak c}_R-i\mathfrak c_R.
\end{aligned}
\tag{3E.72b}
$$

Using \(\bar D_R\mathfrak c_R=0\),
\(D_R\widetilde{\mathfrak c}_R=0\), and the two entries of
\(\mathcal F_R^{(1)}\),

$$
\begin{aligned}
\left.\mathbf s_R\mathcal F_{R,+}\right|_0
&=-\frac14\bar D_R^2
(i\widetilde{\mathfrak c}_R-i\mathfrak c_R)
=-\frac i4\bar D_R^2\widetilde{\mathfrak c}_R,\\
\left.\mathbf s_R\mathcal F_{R,-}\right|_0
&=-\frac14D_R^2
(i\widetilde{\mathfrak c}_R-i\mathfrak c_R)
=+\frac i4D_R^2\mathfrak c_R.
\end{aligned}
\tag{3E.72c}
$$

In the ordered input \((\mathfrak c_+,\widetilde{\mathfrak c}_-)\)
and output \((\mathcal F_+,\mathcal F_-)\) bases,

$$
\boxed{
\mathcal M_R^{\rm FP,(0)}
=\begin{pmatrix}
0&-\dfrac i4\bar D_R^2\\[1mm]
+\dfrac i4D_R^2&0
\end{pmatrix},
\qquad
\mathcal G_R^{\rm FP,(0)}
:=(\mathcal M_R^{\rm FP,(0)})^{-1}
=\begin{pmatrix}
0&-\dfrac i4\bar D_R^2\Box_R^{-1}\\[1mm]
+\dfrac i4D_R^2\Box_R^{-1}&0
\end{pmatrix}.}
\tag{3E.72d}
$$

All four typed compositions are

$$
\boxed{
\begin{aligned}
\left(-\frac i4\bar D^2\right)
\left(+\frac i4D^2\Box^{-1}\right)
&=\frac{\bar D^2D^2}{16\Box}=\Pi_{R,+},\\
\left(+\frac i4D^2\right)
\left(-\frac i4\bar D^2\Box^{-1}\right)
&=\frac{D^2\bar D^2}{16\Box}=\Pi_{R,-},\\
\left(-\frac i4\bar D^2\Box^{-1}\right)
\left(+\frac i4D^2\right)
&=\frac{\bar D^2D^2}{16\Box}=\Pi_{R,+},\\
\left(+\frac i4D^2\Box^{-1}\right)
\left(-\frac i4\bar D^2\right)
&=\frac{D^2\bar D^2}{16\Box}=\Pi_{R,-}.
\end{aligned}}
\tag{3E.72e}
$$

On the flat finite gate (3E.43c), restriction by the commuting ghost
and gauge-condition projectors gives

$$
\boxed{
\begin{aligned}
\mathcal M_R^{\rm FP,(0),\perp}
&:=\widetilde{\mathbb P}_{\mathscr F,R,\nu}^{\perp}
\mathcal M_R^{\rm FP,(0)}
\mathbb P_{\mathscr G,R,\nu}^{\perp},\\
\mathcal G_R^{\rm FP,(0),\perp}
&:=\mathbb P_{\mathscr G,R,\nu}^{\perp}
\mathcal G_R^{\rm FP,(0)}
\widetilde{\mathbb P}_{\mathscr F,R,\nu}^{\perp},\\
\mathcal M_R^{\rm FP,(0),\perp}
\mathcal G_R^{\rm FP,(0),\perp}
&=\widetilde{\mathbb P}_{\mathscr F,R,\nu}^{\perp},\\
\mathcal G_R^{\rm FP,(0),\perp}
\mathcal M_R^{\rm FP,(0),\perp}
&=\mathbb P_{\mathscr G,R,\nu}^{\perp}.
\end{aligned}}
\tag{3E.72f}
$$

Since the FP quadratic kernel is
\(K_{{\rm FP},R}=-\mathcal M_R^{\rm FP,(0)}\), its two direct lines
are

$$
\boxed{
\langle\mathfrak c_L^{\rm pair}\,\mathfrak c'_L\rangle_c
=-i\hbar\mathcal G_{L,\epsilon}^{\rm FP,(0),\perp},
\qquad
\langle\mathfrak c_E^{\rm pair}\,\mathfrak c'_E\rangle_c
=-\hbar\mathcal G_E^{\rm FP,(0),\perp}.}
\tag{3E.72g}
$$

For an arbitrary background \(\overline Q_R\), curvature invalidates
the flat projector reduction.  The kernels are instead defined by

$$
\boxed{
\begin{aligned}
(\mathbb H_{\overline Q,R,\nu})_{\mathsf A\mathsf B}(z,z')
&:=\left.
\frac{\vec\delta}{\delta\Xi_{R,\rm int}^{\mathsf B}(z')}
\frac{\vec\delta}{\delta\Xi_{R,\rm int}^{\mathsf A}(z)}
\mathbb A_{R,\nu}[\Xi_{\rm int};\overline Q_R]
\right|_{\Xi_{\rm int}=\Xi_{\rm vac}},\\
\mathbb H_{\overline Q,R,\nu}\mathbb G_{\overline Q,R,\nu}
&=\widetilde{\mathbb P}_{\Psi,R,\nu}^{\perp},
\qquad
\mathbb G_{\overline Q,R,\nu}\mathbb H_{\overline Q,R,\nu}
=\mathbb P_{\Psi,R,\nu}^{\perp}.
\end{aligned}}
\tag{3E.72a}
$$

No flat \(\Pi_{R,+},\Pi_{R,-},\Pi_{R,T}\) is used in (3E.72a).
Momentum-diagonal kernels occur only in the flat specialization;
otherwise background fields remain external insertions of (3E.45).

### 3E.7 Complete superspace vertex generator

The gauge-fixed exponent is

$$
\boxed{
\begin{aligned}
\mathbb A_{R,\nu}
&=W_{\Psi,R,\nu}
+\tau_R^{-1}\log\boldsymbol\varpi_{\Psi,R,\nu},\\
\mathbb A_R^{(0)}
&:=S_{0,R}^{\rm ren}+\mathbf s_R\Psi_R^{\rm pc},\\
\mathbb A_{R,\nu}-\mathbb A_R^{(0)}
&=(W_{\Psi,R,\nu}-S_{0,R}^{\rm ren}
-\mathbf s_R\Psi_R^{\rm pc})
+\tau_R^{-1}\log\boldsymbol\varpi_{\Psi,R,\nu}.
\end{aligned}}
\tag{3E.73}
$$

On the admitted BV--NK branch, its trivial-pair term is already inside
\(W_{\Psi,R,\nu}\), and at classical order inside
\(\mathbf s_R\Psi_R^{\rm pc}\); it is not added a second time.
Because \(\tau_R^{-1}\) contains one power of \(\hbar\), a
field-dependent density contributes quantum vertices to
\(\mathbb A_{R,\nu}\), but never to the classical master functional
\(\mathbb A_R^{(0)}\).

Every physical, gauge-fixing, FP, multiplier, density, and admitted NK
vertex is the ordered derivative (3E.45) of (3E.73).

The separate all-valence sources are

$$
\begin{aligned}
\mathbb V^{\rm mat,(n)}
&:=\delta^n
\int_{R,8}\widetilde\Phi\mathsf Z e^{\mathcal V}\Phi,\\
\mathbb V^{\rm gauge,(n)}
&:=\delta^n\left\{
\frac{\varkappa_R}{4}\int_{R,+}\kappa_{AB}\mathcal W^{Aa}\mathcal W_a^B
+\frac{\varkappa_R}{4}\int_{R,-}
\widetilde\kappa_{AB}\widetilde{\mathcal W}_{\dot a}^A
\widetilde{\mathcal W}^{B\dot a}\right\},\\
\mathbb V^{\rm pot,(n)}
&:=\delta^n\left\{
\varkappa_R\int_{R,+}\mathscr U_{R,\rm ren}
+\varkappa_R\int_{R,-}\widetilde{\mathscr U}_{R,\rm ren}
\right\},\\
\mathbb V^{\rm nm,(n)}&:=\delta^n(\mathbf s_R\Psi_R^{\rm pc}),\\
\mathbb V^{\rm dens,(n)}&:=\tau_R^{-1}\delta^n
\log\boldsymbol\varpi_{\Psi,R}.
\end{aligned}
\tag{3E.74}
$$

Here every \(\delta^n\) means the ordered derivative in (3E.45); no
matrix word or spinor derivative is moved after differentiation.

$$
\boxed{
\mathbb V_{R;\mathsf A_1\cdots\mathsf A_n}
(p_1,\ldots,p_n)
:=(2\pi)^4\delta_R^{(4)}\!\left(\sum_{j=1}^np_j\right)
\widehat{\mathbb V}_{R;\mathsf A_1\cdots\mathsf A_n}
(p_1,\ldots,p_n),
\qquad
\partial_M^{(j)}\longmapsto ip_{jM}.}
\tag{3E.74a}
$$

The replacement in (3E.74a) is made at the original position of the
derivative acting on leg \(j\); spinor derivatives and color words
retain their ordered positions.

For a homogeneous \(A\), the allowed odd integrations by parts are

$$
\boxed{
\begin{aligned}
\int_{R,8}(D A)B
&=-(-1)^{\epsilon_A}\int_{R,8}A(DB),\\
\int_{R,8}(\bar D A)B
&=-(-1)^{\epsilon_A}\int_{R,8}A(\bar D B),\\
\int_{R,+}(D A)B
&=-(-1)^{\epsilon_A}\int_{R,+}A(DB),\\
\int_{R,-}(\bar D A)B
&=-(-1)^{\epsilon_A}\int_{R,-}A(\bar D B).
\end{aligned}}
\tag{3E.75}
$$

A \(\bar D\) transfer on \(\Sigma_+\), or a \(D\) transfer on
\(\Sigma_-\), is forbidden until the complete density has been
converted to \(\Sigma_8\) by the ordered Project Berezin projector.

Every \(D\)-algebra rewrite records the input order, the application
of (3E.37)--(3E.41), the Koszul sign, the momentum produced, and the
output order.  No sign is postponed.

### 3E.8 Full component generator and Wess--Zumino specialization

Use the Step-3D monomial bases

$$
\boxed{
\Theta_+:=\vartheta^a\vartheta_a,
\qquad
\Theta_-:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a},
\qquad
\mathscr M_+=(1,\vartheta^1,\vartheta^2,\Theta_+),
\qquad
\mathscr M_-=(1,\bar\vartheta_{\dot1},
\bar\vartheta_{\dot2},\Theta_-),
\qquad
\mathscr M_8=\mathscr M_+\mathscr M_-.}
\tag{3E.76}
$$

The ordered raw slots of an unconstrained vector prepotential are

$$
\boxed{
\begin{array}{c|c|c}
m_+&m_-&v_{m_+m_-}\\ \hline
1&1&C\\
\vartheta^a&1&\chi_a\\
1&\bar\vartheta_{\dot a}&\widetilde\chi^{\dot a}\\
\Theta_+&1&M\\
1&\Theta_-&\widetilde M\\
\vartheta^a&\bar\vartheta_{\dot a}&A_{a}{}^{\dot a}\\
\Theta_+&\bar\vartheta_{\dot a}&\widetilde\rho^{\dot a}\\
\vartheta^a&\Theta_-&\rho_a\\
\Theta_+&\Theta_-&D_0
\end{array}
\qquad(1+2+2+1+1+4+2+2+1=16).}
\tag{3E.76a}
$$

For every named superfield block \(X\), prefix the raw slots by \(X\)
and set

$$
\boxed{
\begin{aligned}
\mathscr S_+(X)
&:=(x_X,\chi_{X,1},\chi_{X,2},f_X),\\
\mathscr S_-(X)
&:=(\widetilde x_X,\widetilde\chi_{X,\dot1},
\widetilde\chi_{X,\dot2},\widetilde f_X),\\
\mathscr S_8(X)
&:=(c_X,\chi_{X,a},\widetilde\chi_X^{\dot a},m_X,
\widetilde m_X,a_{X,a}{}^{\dot a},
\widetilde\rho_X^{\dot a},\rho_{X,a},d_X).
\end{aligned}}
\tag{3E.76b}
$$

Thus the complete per-block slot ledger is

$$
\boxed{
\begin{array}{c|c}
X&\text{ordered coefficient tuple}\\ \hline
\mathcal V_{\rm q}&\mathscr S_8(\mathcal V_{\rm q})\\
\chi,\ \mathfrak c&\mathscr S_+(X)\\
\widetilde\chi,\ \widetilde{\mathfrak c}&\mathscr S_-(X)\\
\mathfrak u_\ell,\ \mathfrak v_\ell
&\mathscr S_{\varsigma_\ell}(X),\quad\ell\in\mathscr R_{\rm nm}\\
\overline Q_Y,\ \Omega_Y,\ Y^{\star{\rm ext}}
&\mathscr S_{\varsigma(Y)}(X)
\end{array}.}
\tag{3E.76c}
$$

The BV--NK rows are precisely the rows with
\(\ell\in\mathscr R_{\rm NK}^{\rm BV}\); they are not counted again.

A chiral or antichiral field uses the four raw slots of
\(\mathscr M_+\) or \(\mathscr M_-\); a full field uses the sixteen
slots of \(\mathscr M_8\).  This applies separately to every physical,
ghost, antighost, multiplier, arbitrary-doublet, and admitted BV--NK
superfield according to its declared domain.

For every superfield block,

$$
\boxed{
\Xi_{R,\nu}^{\mathsf A}(z)
=\sum_{r,m}
\xi_{R,rm}^{\mathsf A}
u_{R,\nu,\varsigma(\mathsf A)r}
(x_{R,\varsigma(\mathsf A)})m,
\qquad
\epsilon(\xi_{rm}^{\mathsf A})
=\epsilon_{\mathsf A}+|m|\pmod2,
\qquad
[\xi_{rm}^{\mathsf A}]=[\Xi^{\mathsf A}]+\frac{|m|}{2}.}
\tag{3E.77}
$$

Equation (3E.77) contains all \(16\) unconstrained-\(\mathcal V\)
slots and every ghost, antighost, multiplier, arbitrary-doublet, and
admitted NK slot.

Let \(m_R^\vee\) be the unique dual monomial satisfying

$$
\boxed{
\int_{R,\varsigma}m_R^\vee n=\delta_{mn},
\qquad
(\pi_{R,\nu}\Xi)_{rm}
=\int_{R,\varsigma}u_{R,\nu,\varsigma r}^{\vee}m_R^\vee\Xi,
\qquad
\pi_{R,\nu}\iota_{R,\nu}=\mathbf1.}
\tag{3E.77a}
$$

If \(m^{\ddagger_L}=\rho_{L,m}{}^n n\), Lorentz reality of an even
prepotential is the slot equation

$$
\boxed{
v_{L,n}
=\sum_m(-1)^{|m|}\rho_{L,m}{}^n(v_{L,m})^{\ddagger_L}.}
\tag{3E.77b}
$$

For a general paired block \(X_L^{\ddagger_L}=\kappa_X X_L^\dagger\),
the complete slot relation is

$$
\boxed{
x_{X^\dagger,n}
=\kappa_X\sum_m
(-1)^{|m|(\epsilon_X+|m|)}
\rho_{L,m}{}^n(x_{X,m})^{\ddagger_L}.}
\tag{3E.77c}
$$

Intrinsic Euclidean slots are independent before the cycle; its cycle
matrix replaces \(\rho_{L,m}{}^n\) only after the Euclidean integral
has been defined.

Define the component action by direct substitution before any inverse
is taken:

$$
\boxed{
\mathbb A_{C,R,\nu}(\xi)
:=\mathbb A_{R,\nu}[\iota_{R,\nu}\xi].}
\tag{3E.78}
$$

The ordinary component tensors are independently differentiated:

$$
\boxed{
\begin{aligned}
(\mathbb H_{C,R})_{\mathsf A rm,\mathsf B sn}
&:=\left.
\frac{\vec\partial}{\partial\xi^{\mathsf B}_{sn}}
\frac{\vec\partial}{\partial\xi^{\mathsf A}_{rm}}
\mathbb A_{C,R,\nu}\right|_{\xi=\xi_{\rm vac}},\\
(\mathbb V_{C,R}^{(n)})_{\mathsf A_1r_1m_1\cdots\mathsf A_nr_nm_n}
&:=\left.
\frac{\vec\partial}{\partial\xi^{\mathsf A_n}_{r_nm_n}}
\cdots
\frac{\vec\partial}{\partial\xi^{\mathsf A_1}_{r_1m_1}}
\mathbb A_{C,R,\nu}\right|_{\xi=\xi_{\rm vac}}.
\end{aligned}}
\tag{3E.79}
$$

As a direct component inversion, take the massless physical chiral
block and define

$$
\varrho_L:=i,
\qquad
\varrho_E:=-1,
\qquad
(\bar\sigma_R\!\cdot\!\partial)
(\sigma_R\!\cdot\!\partial)
=-\varkappa_R\Box_R\mathbf1_2.
\tag{3E.79a}
$$

Direct substitution of the Step-3A component definitions gives

$$
\boxed{
\mathbb A_{C,R,\rm ch}^{(2)}
=\varkappa_R\int d^4x_R\left[
-\partial_M\widetilde\phi\,\mathsf Z\partial^M\phi
+\varrho_R\widetilde\psi\,\mathsf Z
\bar\sigma_R^M\partial_M\psi
+\widetilde F\,\mathsf ZF\right].}
\tag{3E.79b}
$$

After one bosonic integration by parts, its three ordered kernels and
their direct two-sided inverses are

$$
\boxed{
\begin{array}{c|c|c}
\text{component pair}&K_R&K_R^{-1}\\ \hline
(\phi,\widetilde\phi)
&\varkappa_R\mathsf Z\Box_R
&\varkappa_R\mathsf Z^{-1}\Box_R^{-1}\\[1mm]
(\psi_a,\widetilde\psi_{\dot a})
&\varkappa_R\varrho_R\mathsf Z
(\bar\sigma_R\!\cdot\!\partial)^{\dot a a}
&-\varrho_R^{-1}\mathsf Z^{-1}
(\sigma_R\!\cdot\!\partial)_{a\dot a}\Box_R^{-1}\\[1mm]
(F,\widetilde F)&\varkappa_R\mathsf Z
&\varkappa_R\mathsf Z^{-1}
\end{array}.}
\tag{3E.79c}
$$

For the fermion row,

$$
(\varkappa_R\varrho_R\mathsf Z\bar\sigma\!\cdot\!\partial)
(-\varrho_R^{-1}\mathsf Z^{-1}
\sigma\!\cdot\!\partial\,\Box_R^{-1})
=-\varkappa_R(-\varkappa_R\Box_R)\Box_R^{-1}
=\mathbf1.
\tag{3E.79d}
$$

The reverse product is identical with dotted and undotted indices
exchanged.  Multiplication by \(i\hbar\) for LC and by \(\hbar\) for
EC gives the three component internal lines; the \(F\) line is an
exact contact kernel.

For a second direct check, choose \(b_{Y,C,R}=1\) and

$$
\mathcal F_{C,R,A}:=\mathfrak h_{R,AB}\partial^MA_M^B,
\qquad
(\mathbf s_{C,R}A_M^A)_{\rm lin}=\partial_Mc^A,
\qquad
(\mathcal Y_{C,R}^{-1})^{AB}
:=-\varkappa_R(\mathfrak h_R^{-1})^{AB},
\qquad
(\mathcal M_{C,R}^{\rm FP})_{AB}
:=\mathfrak h_{R,AB}\Box_R.
\tag{3E.79d1}
$$

The multiplier part completes as

$$
\begin{aligned}
b^A\mathcal F_{C,A}-\frac12b^A(\mathcal Y_C)_{AB}b^B
&=\frac12\mathcal F_{C,A}(\mathcal Y_C^{-1})^{AB}
\mathcal F_{C,B}\\
&\quad-\frac12
(b^A-(\mathcal Y_C^{-1})^{AC}\mathcal F_{C,C})
(\mathcal Y_C)_{AB}
(b^B-(\mathcal Y_C^{-1})^{BD}\mathcal F_{C,D}),\\
\frac12\mathcal F_{C,A}(\mathcal Y_C^{-1})^{AB}
\mathcal F_{C,B}
&=-\frac{\varkappa_R}{2}\mathfrak h_{R,AB}
(\partial^MA_M^A)(\partial^NA_N^B).
\end{aligned}
\tag{3E.79d2}
$$

The FP coefficient action and inverse are

$$
S_{C,R}^{\rm FP,(2)}
=-\int_R\bar c^A(\mathcal M_{C,R}^{\rm FP})_{AB}c^B
=-\int_R\bar c^A\mathfrak h_{R,AB}\Box_Rc^B,
\qquad
K_{C,R,AB}^{\rm FP}=-\mathfrak h_{R,AB}\Box_R,
\qquad
(K_{C,R}^{\rm FP,-1})^{AB}
=-(\mathfrak h_R^{-1})^{AB}\Box_R^{-1},
\qquad
K_{C,R,AB}^{\rm FP}(K_{C,R}^{\rm FP,-1})^{BC}
=\delta_A{}^C.
\tag{3E.79d3}
$$

After exact multiplier elimination, this is the ordinary Feynman gauge
on the massless Wess--Zumino vector block.  With
\(g_L^{MN}=\eta^{\mu\nu}\) and \(g_E^{MN}=\delta^{mn}\),

$$
\boxed{
\begin{aligned}
\left.
(\mathbb A_{C,R,V}^{(2)}+\mathbf s_{C,R}\Psi_{C,R}^{\rm Fey})
\right|_{\bar c=c=0,\,
b^A=(\mathcal Y_C^{-1})^{AB}\mathcal F_{C,B}}
=\varkappa_R\int d^4x_R\,\mathfrak h_{R,AB}\Big[&
-\frac14F_{MN}^AF^{B,MN}
-\frac12(\partial^MA_M^A)(\partial^NA_N^B)\\
&+\varrho_R\widetilde\lambda^A\bar\sigma_R^M\partial_M\lambda^B
+\frac12\mathscr D^A\mathscr D^B\Big].
\end{aligned}}
\tag{3E.79e}
$$

The two bosonic derivative terms expand as

$$
\begin{aligned}
-\frac14F_{MN}F^{MN}
&=-\frac12\partial_MA_N\partial^MA^N
+\frac12\partial_MA_N\partial^NA^M,\\
-\frac12(\partial^MA_M)^2
&=-\frac12\partial_MA^M\partial_NA^N,\\
\int_R(\cdots)
&=\frac12\int_R A_Mg_R^{MN}\Box_RA_N.
\end{aligned}
\tag{3E.79f}
$$

Thus the direct vector-multiplet kernels are

$$
\boxed{
\begin{array}{c|c|c}
\text{component pair}&K_R&K_R^{-1}\\ \hline
(A_M^A,A_N^B)
&\varkappa_R\mathfrak h_{R,AB}g_R^{MN}\Box_R
&\varkappa_R(\mathfrak h_R^{-1})^{AB}g_{R,MN}\Box_R^{-1}\\[1mm]
(\lambda_a^A,\widetilde\lambda_{\dot a}^B)
&\varkappa_R\varrho_R\mathfrak h_{R,AB}
(\bar\sigma_R\!\cdot\!\partial)^{\dot aa}
&-\varrho_R^{-1}(\mathfrak h_R^{-1})^{AB}
(\sigma_R\!\cdot\!\partial)_{a\dot a}\Box_R^{-1}\\[1mm]
(\mathscr D^A,\mathscr D^B)
&\varkappa_R\mathfrak h_{R,AB}
&\varkappa_R(\mathfrak h_R^{-1})^{AB}
\end{array}.}
\tag{3E.79g}
$$

On the explicit EC cycles (3E.52d), (3E.52g), and (3E.52i), the
ordered free lines are

$$
\boxed{
\begin{aligned}
\langle\phi^I(p)\widetilde\phi_J(-p)\rangle_E
&=\hbar(\mathsf Z_E^{-1})^I{}_J\frac1{p_E^2},\\
\langle A_m^A(p)A_n^B(-p)\rangle_E
&=\hbar(\mathfrak h_E^{-1})^{AB}
\frac{\delta_{mn}}{p_E^2},\\
\langle c^A(p)\bar c^B(-p)\rangle_E
&=\hbar(\mathfrak h_E^{-1})^{AB}\frac1{p_E^2},\\
\langle\psi_a^I(p)\widetilde\psi_{\dot a,J}(-p)\rangle_E
&=-i\hbar(\mathsf Z_E^{-1})^I{}_J
\frac{(\sigma_E\!\cdot p)_{a\dot a}}{p_E^2},\\
\langle\lambda_a^A(p)\widetilde\lambda_{\dot a}^B(-p)\rangle_E
&=-i\hbar(\mathfrak h_E^{-1})^{AB}
\frac{(\sigma_E\!\cdot p)_{a\dot a}}{p_E^2},\\
\langle F^I\widetilde F_J\rangle_E
&=-\hbar(\mathsf Z_E^{-1})^I{}_J,
\qquad
\langle F^I(F^\dagger)_J\rangle_E
=+\hbar(\mathsf Z_E^{-1})^I{}_J,\\
\langle\mathscr D^A\mathscr D^B\rangle_E
&=-\hbar(\mathfrak h_E^{-1})^{AB},
\qquad
\langle d^Ad^B\rangle_E
=+\hbar(\mathfrak h_E^{-1})^{AB}.
\end{aligned}}
\tag{3E.79g1}
$$

For \(B_E:=\mathfrak n_E-f_E=i\beta\),

$$
\boxed{
\langle B_E^\alpha B_E^\beta\rangle_E
=-\hbar(\mathcal Y_E^{-1})^{\alpha\beta},
\qquad
\langle\beta^\alpha\beta^\beta\rangle_E
=+\hbar(\mathcal Y_E^{-1})^{\alpha\beta}.}
\tag{3E.79g2}
$$

For the explicit LC pole prescription set

$$
\mathsf Z_L=\mathsf Z_L^\dagger>0,
\qquad
\mathfrak h_L=\mathfrak h_L^\dagger>0,
\qquad
q_2>0,
\quad [q_2]=2,
\qquad
q_0>0,
\quad [q_0]=0,
\qquad
\varepsilon_2:=\hbar\epsilon q_2>0,
\quad
\varepsilon_0:=\hbar\epsilon q_0>0,
\qquad
\Box_{L,\varepsilon_2}:=\Box_L+i\varepsilon_2.
\tag{3E.79g3}
$$

For the scalar block use
\(\widetilde\phi_L=\phi_L^\dagger\) and the positive damping form
\(\mathscr Q_{\phi,L}''=q_2\mathsf Z_L\).
Then

$$
K_{\phi,L,\epsilon}(p)
=\mathsf Z_L(-p_L^2+i\varepsilon_2),
\qquad
\boxed{
\langle\phi^I(p)\widetilde\phi_J(-p)\rangle_L
=i\hbar(\mathsf Z_L^{-1})^I{}_J
\frac1{-p_L^2+i0}.}
\tag{3E.79g4}
$$

The Lorentzian vector real form is \(A_M^\dagger=A_M\).  The
spacetime-isotropic positive choice
\(\mathscr Q_{A,L}''=q_2\mathfrak h_L\delta^{MN}\) gives

$$
K_{A,L,\epsilon}^{MN}(p)
=\mathfrak h_L\left[(-p_L^2)\eta^{MN}
+i\varepsilon_2\delta^{MN}\right].
\tag{3E.79g5}
$$

Its direct regulated inverse is

$$
\boxed{
\begin{aligned}
(K_{A,L,\epsilon}^{-1})_{00}
&=\mathfrak h_L^{-1}\frac1{p_L^2+i\varepsilon_2}
=-\mathfrak h_L^{-1}\frac1{-p_L^2-i\varepsilon_2},\\
(K_{A,L,\epsilon}^{-1})_{ij}
&=\mathfrak h_L^{-1}\delta_{ij}
\frac1{-p_L^2+i\varepsilon_2}.
\end{aligned}}
\tag{3E.79g6}
$$

Thus the direct all-real LC connected vector line is

$$
\boxed{
\begin{aligned}
\langle A_0^A(p)A_0^B(-p)\rangle_L^{\rm real}
&=i\hbar(\mathfrak h_L^{-1})^{AB}
\frac1{p_L^2+i0},\\
\langle A_i^A(p)A_j^B(-p)\rangle_L^{\rm real}
&=i\hbar(\mathfrak h_L^{-1})^{AB}\delta_{ij}
\frac1{-p_L^2+i0}.
\end{aligned}}
\tag{3E.79g6d}
$$

A single covariant denominator would require

$$
(K_{A,L,\epsilon}^{\rm cov})^{-1}
=\mathfrak h_L^{-1}\eta(-p_L^2+i\varepsilon_2)^{-1},
\qquad
\mathscr Q_{A,L}^{\prime\prime,\rm cov}=q_2\mathfrak h_L\eta.
\tag{3E.79g6a}
$$

For \(v=(v_0,0,0,0)\) and \(w=(0,w_1,0,0)\),

$$
v\mathscr Q_{A,L}^{\prime\prime,\rm cov}v
=-q_2v_0^A\mathfrak h_{L,AB}v_0^B<0,
\qquad
w\mathscr Q_{A,L}^{\prime\prime,\rm cov}w
=+q_2w_1^A\mathfrak h_{L,AB}w_1^B>0.
\tag{3E.79g6b}
$$

The obstruction is independent of the diagonal choice.  For any
positive real damping matrix \(Q\), set \(x:=-p_L^2\) and

$$
Q^{-1/2}\eta Q^{-1/2}
=O^{\mathrm T}\operatorname{diag}(\lambda_0,\lambda_1,
\lambda_2,\lambda_3)O,
\qquad
\#\{\lambda_r<0\}=1,
\quad
\#\{\lambda_r>0\}=3.
\tag{3E.79g6b1}
$$

Then

$$
\begin{aligned}
(x\eta+i\epsilon Q)^{-1}
&=Q^{-1/2}O^{\mathrm T}
\operatorname{diag}\left(
\frac1{x\lambda_r+i\epsilon}
\right)OQ^{-1/2},\\
\operatorname{Im}\lim_{\epsilon\downarrow0}
(x\eta+i\epsilon Q)^{-1}
&=-\pi Q^{-1/2}O^{\mathrm T}
\operatorname{diag}(|\lambda_r|^{-1})
OQ^{-1/2}\,\delta(x),\\
\operatorname{Im}\left[\frac{\eta}{x+i0}\right]
&=-\pi\eta\,\delta(x).
\end{aligned}
\tag{3E.79g6b2}
$$

The second line is negative definite on the coefficient space; the
third has inertia \((1,3)\).  They cannot be equal.  Thus the
Lorentzian real form, positive damping, and one covariant vector
denominator cannot hold simultaneously.  The alternative
cycle \(A_0=ia_0\), \(A_i=a_i\), \(a_M\in\mathbb R\) gives the
covariant candidate, but its temporal line differs from (3E.79g6):

$$
\begin{aligned}
\langle A_0A_0\rangle_L^{\rm real}
-\langle A_0A_0\rangle_L^{\rm cov}
&=i\hbar\left[
\frac1{p_L^2+i0}-\frac1{p_L^2-i0}\right]
\mathfrak h_L^{-1}\\
&=2\pi\hbar\,\delta(p_L^2)\mathfrak h_L^{-1}\ne0.
\end{aligned}
\tag{3E.79g6c}
$$

Therefore the covariant candidate is a distinct conditional cycle
ledger; it is not the direct LC rule derived from (3D.23)--(3D.24).

On the same residual complement, an additional spectral declaration is

$$
K_{\psi,L,\epsilon}
:=\Box_{L,\varepsilon_2}\Box_L^{-1}K_{\psi,L},
\qquad
K_{\psi,L,\epsilon}^{-1}
=-\varrho_L^{-1}\mathsf Z_L^{-1}
\sigma_L\!\cdot\!\partial\,\Box_{L,\varepsilon_2}^{-1}.
\tag{3E.79g7}
$$

This formula exists only on \(\mathscr V_{L,\nu}^{\circ}\), where
\(\Box_L^{-1}\) already exists.  Extension across
\(\ker\Box_L\) to the displayed (i0) boundary value is an additional
analytic prescription; it is not produced by the finite algebraic
factor \(\Box_{L,\varepsilon_2}\Box_L^{-1}\).

Direct multiplication gives

$$
\begin{aligned}
K_{\psi,L,\epsilon}K_{\psi,L,\epsilon}^{-1}
&=\Box_{L,\varepsilon_2}\Box_L^{-1}
(\varrho_L\mathsf Z_L\bar\sigma_L\!\cdot\!\partial)
(-\varrho_L^{-1}\mathsf Z_L^{-1}
\sigma_L\!\cdot\!\partial\,
\Box_{L,\varepsilon_2}^{-1})\\
&=\Box_{L,\varepsilon_2}\Box_L^{-1}
\Box_L\Box_{L,\varepsilon_2}^{-1}=\mathbf1.
\end{aligned}
\tag{3E.79g8}
$$

The reverse product is identical because every flat factor commutes
with \(\Box_L\).  This spectral prescription is conditional: it is
not derived from the positive vector damping in (3E.79g5).  Since
\(\varrho_L=i\) and
\(\partial_M\mapsto ip_M\),

$$
\boxed{
\begin{aligned}
\langle\psi_a^I(p)\widetilde\psi_{\dot a,J}(-p)\rangle_L
&=-i\hbar(\mathsf Z_L^{-1})^I{}_J
\frac{(\sigma_L\!\cdot p)_{a\dot a}}{-p_L^2+i0},\\
\langle\lambda_a^A(p)\widetilde\lambda_{\dot a}^B(-p)\rangle_L
&=-i\hbar(\mathfrak h_L^{-1})^{AB}
\frac{(\sigma_L\!\cdot p)_{a\dot a}}{-p_L^2+i0},\\
\langle c^A(p)\bar c^B(-p)\rangle_L
&=-i\hbar(\mathfrak h_L^{-1})^{AB}
\frac1{-p_L^2+i0}.
\end{aligned}}
\tag{3E.79g9}
$$

The last line follows from the explicit kernel

$$
K_{{\rm FP},L,\epsilon}
:=-\mathfrak h_L\Box_{L,\varepsilon_2},
\qquad
K_{{\rm FP},L,\epsilon}^{-1}
=-\mathfrak h_L^{-1}\Box_{L,\varepsilon_2}^{-1},
\qquad
KK^{-1}=K^{-1}K=\mathbf1.
\tag{3E.79g10}
$$

For the full ghost superfield, the same declaration is
\(\mathcal M_{L,\epsilon}^{\rm FP,(0)}
:=\Box_{L,\varepsilon_2}\Box_L^{-1}
\mathcal M_L^{\rm FP,(0)}\); its inverse is obtained from (3E.72d)
by replacing every \(\Box_L^{-1}\) with
\(\Box_{L,\varepsilon_2}^{-1}\).  The ordinary pair
\((c,\bar c)\) is odd and uses \(\succ_\nu\) Berezin order.  A full
parity-reversed ghost superfield also has commuting coefficient ends;
their reality relations, orientation, and positive thimbles depend on
the emitted matrix (3E.79m).  No universal commuting-superghost cycle
is asserted before those branch data are supplied.

For \(\varepsilon_0>0\), the regulated contact kernels and
their limits are

$$
\boxed{
\begin{aligned}
\langle F^I\widetilde F_J\rangle_{L,\epsilon}
&=i\hbar\left([(1+i\varepsilon_0)\mathsf Z_L]^{-1}\right)^I{}_J
\xrightarrow{\epsilon\downarrow0}i\hbar(\mathsf Z_L^{-1})^I{}_J,\\
\langle\mathscr D^A\mathscr D^B\rangle_{L,\epsilon}
&=i\hbar\left([(1+i\varepsilon_0)\mathfrak h_L]^{-1}\right)^{AB}
\xrightarrow{\epsilon\downarrow0}i\hbar(\mathfrak h_L^{-1})^{AB},\\
B_L&:=b_L-(\mathcal Y_{C,L}^{-1})\mathcal F_{C,L}
=b_L+\partial\!\cdot A_L,\\
\langle B_L^AB_L^B\rangle_{L,\epsilon}
&=i\hbar\left([(1+i\varepsilon_0)\mathfrak h_L]^{-1}\right)^{AB}
\xrightarrow{\epsilon\downarrow0}i\hbar(\mathfrak h_L^{-1})^{AB}.
\end{aligned}}
\tag{3E.79g11}
$$

These three limits are contact distributions and carry no momentum
pole.  The conditional spectral prescription (3E.79g7) and the
component-positive contact prescription (3E.79g11) are distinct
finite-\(\epsilon\) schemes; only their separately displayed
\(\epsilon\downarrow0\) limits are compared.  They are not asserted to
come from one common \(\mathscr Q_{\Psi,L,\nu}''\).

For the full arbitrary finite non-minimal theory, direct substitution
gives the finite component supermatrix

$$
\boxed{
\mathbb H_{C,R,\nu}=
\begin{pmatrix}
H_{\mathsf PP}^C&H_{\mathsf PC}^C&H_{\mathsf PN}^C&H_{\mathsf PK}^C\\
H_{\mathsf CP}^C&H_{\mathsf CC}^C&H_{\mathsf CN}^C&H_{\mathsf CK}^C\\
H_{\mathsf NP}^C&H_{\mathsf NC}^C&H_{\mathsf NN}^C&H_{\mathsf NK}^C\\
H_{\mathsf KP}^C&H_{\mathsf KC}^C&H_{\mathsf KN}^C&H_{\mathsf KK}^C
\end{pmatrix},
\qquad
H_{\mathsf XY}^C
:=\vec\partial_{\mathsf Y}\vec\partial_{\mathsf X}
\mathbb A_{C,R,\nu}\big|_{\xi=\xi_{\rm vac}}.}
\tag{3E.79h}
$$

The labels \((\mathsf P,\mathsf C,\mathsf N,\mathsf K)\) are the
component images of (3E.48a).  For every recursive split
\(\mathbb H_C=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\),
direct finite-matrix elimination gives

$$
\boxed{
\mathbb H_C^{-1}=
\begin{pmatrix}
S_A^{-1}&-S_A^{-1}BD^{-1}\\
-D^{-1}CS_A^{-1}&D^{-1}+D^{-1}CS_A^{-1}BD^{-1}
\end{pmatrix},
\qquad S_A=A-BD^{-1}C.}
\tag{3E.79i}
$$

Left and right multiplication of (3E.79i) gives the component dual
and field residual projectors.  Since the number and domain of
contractible doublets are arbitrary finite data, (3E.79h)--(3E.79i),
not one fixed-size numerical matrix, is the complete universal LC/EC
rule.

The fixed flat standard branch is

$$
\mathfrak B_{R,\nu}^{\rm flat}=1,
\qquad
\overline Q_R=0,
\qquad
\mathcal V_{R,\rm vac}=0,
\qquad
\boldsymbol\varpi_{\Psi,R,\nu}=1,
\qquad
\mathbf s_R\mathcal Y_R=0,
\qquad
\mathscr R_{\rm NK}^{\rm BV}=\varnothing.
\tag{3E.79i1}
$$

It has a fully typed finite emitter.  Per
momentum and adjoint color block, its raw slot count and order are

$$
16_{\mathcal V}+8_{\mathfrak n}+8_{\mathfrak c}
+8_{\mathfrak c'}=40,
\qquad
q_{C,R}:=(v_{16};n_+,\widetilde n_-;
c_+,\widetilde c_-;c'_+,\widetilde c'_-),
\tag{3E.79j}
$$

where

$$
\begin{aligned}
v_{16}:=(&C,\chi_1,\chi_2,
\widetilde\chi^{\dot1},\widetilde\chi^{\dot2},M,\widetilde M,
A_1{}^{\dot1},A_1{}^{\dot2},A_2{}^{\dot1},A_2{}^{\dot2},\\
&\widetilde\rho^{\dot1},\widetilde\rho^{\dot2},
\rho_1,\rho_2,D_0)^{\mathrm T},
\qquad
x_+(X):=(x_X,\chi_{X,1},\chi_{X,2},f_X)^{\mathrm T},\\
x_-(X)&:=(\widetilde x_X,\widetilde\chi_{X,\dot1},
\widetilde\chi_{X,\dot2},\widetilde f_X)^{\mathrm T}.
\end{aligned}
\tag{3E.79k}
$$

For \(p\in\Lambda_{R,\nu}^{\circ}\), let
\(e_{R,\varsigma;p,m}:=|p\rangle m\) and define every component entry
of a typed operator without suppressing any slot:

$$
\boxed{
[\mathcal O_R]^C_{p;mn}
:=\left\langle e_{R,\varsigma_{\rm out}}^{\vee;p,m},
\mathcal O_R(p)e_{R,\varsigma_{\rm in};p,n}\right\rangle_{R,\varsigma_{\rm out}}.}
\tag{3E.79l}
$$

Equation (3E.32) acting on the sixteen monomials of (3E.76a) now
gives the nonzero standard matrices entry by entry:

$$
\boxed{
\begin{aligned}
(H_{T,R}^C)_{p;Am,Bn}
&=-\frac{\varkappa_R}{2}\mathfrak h_{R,AB}
[\Box_R\Pi_{R,T}]^C_{p;mn},\\
(F_{R,+}^C)_{p;Am,Bn}
&=-\frac14\delta_A{}^B[\bar D_R^2]^C_{p;+m,8n},\\
(F_{R,-}^C)_{p;Am,Bn}
&=-\frac14\delta_A{}^B[D_R^2]^C_{p;-m,8n},
\qquad
F_R^C:=\begin{pmatrix}F_{R,+}^C\\F_{R,-}^C\end{pmatrix},\\
(Y_R^C)_{p;\alpha Am,\beta Bn}
&:=[(\mathcal Y_R)_{\alpha A,\beta B}]^C_{p;mn},
\qquad \alpha,\beta\in\{+,-\},\\
M_R^C
&:=\begin{pmatrix}
0&-\dfrac i4[\bar D_R^2]^C\\[1mm]
+\dfrac i4[D_R^2]^C&0
\end{pmatrix},
\qquad
(M_R^C)^{-1}
=\left[\begin{pmatrix}
0&-\dfrac i4\bar D_R^2\Box_R^{-1}\\[1mm]
+\dfrac i4D_R^2\Box_R^{-1}&0
\end{pmatrix}\right]^C.
\end{aligned}}
\tag{3E.79m}
$$

Set

$$
\begin{aligned}
H_{(V,n),R}^C
&:=\begin{pmatrix}
H_{T,R}^C&(F_R^C)^{\mathrm{sT}}\\
F_R^C&-Y_R^C
\end{pmatrix},\\
S_{V,R}^C
&:=H_{T,R}^C+(F_R^C)^{\mathrm{sT}}(Y_R^C)^{-1}F_R^C,\\
G_{(V,n),R}^C
&:=\begin{pmatrix}
(S_V^C)^{-1}&(S_V^C)^{-1}(F^C)^{\mathrm{sT}}(Y^C)^{-1}\\
(Y^C)^{-1}F^C(S_V^C)^{-1}
&-(Y^C)^{-1}+(Y^C)^{-1}F^C(S_V^C)^{-1}
(F^C)^{\mathrm{sT}}(Y^C)^{-1}
\end{pmatrix}.
\end{aligned}
\tag{3E.79n}
$$

The two products contain no omitted block:

$$
\begin{aligned}
H_{(V,n)}^CG_{(V,n)}^C
&=\begin{pmatrix}
S_V^C(S_V^C)^{-1}
&S_V^C(S_V^C)^{-1}(F^C)^{\mathrm{sT}}(Y^C)^{-1}
-(F^C)^{\mathrm{sT}}(Y^C)^{-1}\\
F^C(S_V^C)^{-1}-F^C(S_V^C)^{-1}
&\mathbf1+F^C(S_V^C)^{-1}(F^C)^{\mathrm{sT}}(Y^C)^{-1}
-F^C(S_V^C)^{-1}(F^C)^{\mathrm{sT}}(Y^C)^{-1}
\end{pmatrix}
=\begin{pmatrix}\mathbf1&0\\0&\mathbf1\end{pmatrix},\\
G_{(V,n)}^CH_{(V,n)}^C
&=\begin{pmatrix}
(S_V^C)^{-1}S_V^C
&(S_V^C)^{-1}(F^C)^{\mathrm{sT}}
-(S_V^C)^{-1}(F^C)^{\mathrm{sT}}\\
(Y^C)^{-1}F^C(S_V^C)^{-1}S_V^C-(Y^C)^{-1}F^C
&(Y^C)^{-1}F^C(S_V^C)^{-1}(F^C)^{\mathrm{sT}}
+\mathbf1-(Y^C)^{-1}F^C(S_V^C)^{-1}(F^C)^{\mathrm{sT}}
\end{pmatrix}
=\begin{pmatrix}\mathbf1&0\\0&\mathbf1\end{pmatrix}.
\end{aligned}
\tag{3E.79o}
$$

For the ordered ghost and antighost columns, with
\(K_R^C:=-M_R^C\),

$$
\begin{aligned}
H_{{\rm gh},R}^{C,{\rm gr}}
&:=\begin{pmatrix}0&-(K_R^C)^{\mathrm{sT}}\\K_R^C&0\end{pmatrix},
&
G_{{\rm gh},R}^{C,{\rm gr}}
&:=\begin{pmatrix}0&(K_R^C)^{-1}\\
-((K_R^C)^{-1})^{\mathrm{sT}}&0\end{pmatrix},\\
H_{{\rm gh},R}^{C,{\rm gr}}G_{{\rm gh},R}^{C,{\rm gr}}
&=\begin{pmatrix}
(K^C)^{\mathrm{sT}}((K^C)^{-1})^{\mathrm{sT}}&0\\
0&K^C(K^C)^{-1}
\end{pmatrix}=\mathbf1,
&
G_{{\rm gh},R}^{C,{\rm gr}}H_{{\rm gh},R}^{C,{\rm gr}}
&=\begin{pmatrix}
(K^C)^{-1}K^C&0\\
0&((K^C)^{-1})^{\mathrm{sT}}(K^C)^{\mathrm{sT}}
\end{pmatrix}=\mathbf1.
\end{aligned}
\tag{3E.79p}
$$

Thus the displayed standard \(40\)-slot inverse is

$$
\boxed{
H_{R,\rm std}^{C,{\rm gr}}
:=H_{(V,n),R}^C\oplus H_{{\rm gh},R}^{C,{\rm gr}},
\qquad
G_{R,\rm std}^{C,{\rm gr}}
:=G_{(V,n),R}^C\oplus G_{{\rm gh},R}^{C,{\rm gr}},
\qquad
HG=\widetilde{\mathbb P}_{C,R,\nu}^{\perp},
\quad GH=\mathbb P_{C,R,\nu}^{\perp}.}
\tag{3E.79q}
$$

For arbitrary finite doublet data
\(\mathfrak d_{R,\nu}:=(\Lambda_{R,\nu}^{\circ},\mathcal Y_R,
\mathscr R_{\rm nm},\mathscr R_{\rm NK}^{\rm BV},
\Xi_{R,\rm vac},\overline Q_R)\), the complete component rule is the
finite output

$$
\boxed{
\operatorname{Emit}_C(\mathfrak d_{R,\nu})
:=\left(H_{C,R,\nu},G_{C,R,\nu},
H_{C,R,\nu}G_{C,R,\nu},G_{C,R,\nu}H_{C,R,\nu}\right),}
\tag{3E.79r}
$$

where every entry is (3E.79l), every inverse is taken only on the
declared residual basis, and the last two outputs must equal the two
projectors in (3E.79q).  Thus (3E.79h)--(3E.79i) are the arbitrary
finite generating extension, not a claim that one fixed numerical
matrix covers every non-minimal choice.

The LC and EC propagators are the independent two-sided inverses of
\(\mathbb H_{C,L}\) and \(\mathbb H_{C,E}\), followed by (3E.51) and
(3E.52).  They are not defined by reading components from a
superpropagator.

Let \(\iota_{R,\nu}^{\vee}\) be the pullback on dual coefficient
spaces, \(\pi_{R,\nu}:=\iota_{R,\nu}^{-1}\), and
\(\pi_{R,\nu}^{\vee}:=(\iota_{R,\nu}^{\vee})^{-1}\).  The typed
component relations are

$$
\boxed{
\mathbb H_{C,R}
=\iota_{R,\nu}^{\vee}\mathbb H_R\iota_{R,\nu},
\qquad
\mathbb H_{C,R}^{-1}
=\pi_{R,\nu}\mathbb H_R^{-1}\pi_{R,\nu}^{\vee},
\qquad
\mathbb H_{C,R}\mathbb H_{C,R}^{-1}
=\widetilde{\mathbb P}_{C,R}^{\perp},
\qquad
\mathbb H_{C,R}^{-1}\mathbb H_{C,R}
=\mathbb P_{C,R}^{\perp}.}
\tag{3E.80}
$$

These identities use the complete regulated monomial bijection, not a
projection onto a proper subspace.  LC and EC Gaussian elimination is
performed directly on \(\mathbb H_{C,R}\); only afterward is its
inverse compared with the second expression in (3E.80).

For auxiliary and nonauxiliary component blocks \((a,d)\),

$$
\mathbb H_C=
\begin{pmatrix}
\mathbb H_{dd}&\mathbb H_{da}\\
\mathbb H_{ad}&\mathbb H_{aa}
\end{pmatrix}.
\tag{3E.81}
$$

Exact auxiliary integration gives

$$
\boxed{
\mathbb H_{C,\rm red}
=\mathbb H_{dd}
-\mathbb H_{da}\mathbb H_{aa}^{-1}\mathbb H_{ad}.}
\tag{3E.82}
$$

Every higher contact vertex is obtained by substituting the exact
solution

$$
\frac{\vec\partial\mathbb A_C}{\partial\xi^a}=0
\quad\Longrightarrow\quad
\xi^a=\xi^a[\xi^d]
\tag{3E.83}
$$

back into \(\mathbb A_C\) and applying (3E.79).  No contact term is
dropped.

The solution in (3E.83) exists as a unique local formal power series
on the chosen Lorentzian or Euclidean cycle when
\(\mathbb H_{aa}\) is a two-sided inverse on the residual auxiliary
complement.  Writing \(\xi^a=\sum_{n\ge1}\xi^a_{(n)}\),

$$
\boxed{
\xi^{a,\alpha}_{(1)}
=-(\mathbb H_{aa}^{-1})^{\alpha\beta}
(\mathbb H_{ad})_{\beta i}\xi^{d,i},
\qquad
\xi^{a,\alpha}_{(n)}
=-(\mathbb H_{aa}^{-1})^{\alpha\beta}
\left[
\frac{\vec\partial\mathbb A_C}{\partial\xi^{a,\beta}}
\left(\xi^d,\sum_{k=1}^{n-1}\xi^a_{(k)}\right)
\right]_{\deg n}.}
\tag{3E.83a}
$$

At quadratic order,

$$
\begin{aligned}
\mathbb A_C^{(2)}\big|_{\xi^a_{(1)}}
&=\frac12\xi^d\mathbb H_{dd}\xi^d
-\xi^d\mathbb H_{da}\mathbb H_{aa}^{-1}
\mathbb H_{ad}\xi^d\\
&\quad
+\frac12\xi^d\mathbb H_{da}\mathbb H_{aa}^{-1}
\mathbb H_{aa}\mathbb H_{aa}^{-1}\mathbb H_{ad}\xi^d\\
&=\frac12\xi^d
\left(\mathbb H_{dd}
-\mathbb H_{da}\mathbb H_{aa}^{-1}\mathbb H_{ad}\right)
\xi^d.
\end{aligned}
\tag{3E.83b}
$$

Wess--Zumino gauge is the later specialization

$$
\mathcal V_R\longmapsto\mathcal V_R^{\rm WZ}
\quad\text{of (3A.47)--(3A.48)}.
\tag{3E.84}
$$

It is not a replacement for (3E.77).  Its ordinary component rules
use the independent residual ordinary BRST system

$$
\boxed{
\mathbf s_{C,R}\bar c_R^A=b_R^A,
\qquad
\mathbf s_{C,R}b_R^A=0,
\qquad
\mathcal M_{C,R}^{\rm FP}
:=d\mathcal F_{C,R}\circ\mathscr R_{C,R}^{\rm g}.}
\tag{3E.84a}
$$

Choose an arbitrary finite component doublet set
\(\mathscr R_{{\rm nm},C}\) and impose

$$
\boxed{
\begin{gathered}
\mathbf s_{C,R}u_{R,\ell}=v_{R,\ell},
\qquad
\mathbf s_{C,R}v_{R,\ell}=0,
\qquad \ell\in\mathscr R_{{\rm nm},C},\\
\epsilon_{v_\ell}=\epsilon_{u_\ell}+1,
\qquad
\operatorname{gh}(v_\ell)=\operatorname{gh}(u_\ell)+1,
\qquad
[u_\ell]=[v_\ell]=d_{C,\ell},
\qquad 0\le d_{C,\ell}\le4.
\end{gathered}}
\tag{3E.84a1}
$$

The residual component symbol ledger is

$$
\boxed{
\begin{array}{c|c|c|c|c}
x&\epsilon_x&\operatorname{gh}x&[x]&\ddagger_L\\ \hline
c_R^A&1&1&0&(c_L^A)^{\ddagger_L}=c_L^A\\
\bar c_R^A&1&-1&2&(\bar c_L^A)^{\ddagger_L}=-\bar c_L^A\\
b_R^A&0&0&2&(b_L^A)^{\ddagger_L}=b_L^A\\
u_{R,\ell}&\epsilon_\ell&g_\ell&d_{C,\ell}
&(u_{L,\ell})^{\ddagger_L}=(-1)^{\epsilon_\ell}
u_{L,\ell^\ddagger}\\
v_{R,\ell}&\epsilon_\ell+1&g_\ell+1&d_{C,\ell}
&(v_{L,\ell})^{\ddagger_L}=v_{L,\ell^\ddagger}
\end{array}}
\tag{3E.84a2}
$$

All Euclidean entries are independent before their coefficient cycle.
The optional standard multiplier kernel obeys

$$
\boxed{
b_{Y,C,R}\in\{0,1\},
\qquad
[\mathcal Y_{C,R}]=0,
\qquad
\epsilon(\mathcal Y_{C,R})=0,
\qquad
\operatorname{gh}(\mathcal Y_{C,R})=0,
\qquad
\mathcal Y_{C,L}^{\ddagger_L}=\mathcal Y_{C,L},}
\tag{3E.84a3}
$$

and is local, algebraic, background-covariant,
graded-self-adjoint, and invertible on the declared multiplier
subspace.  For a general quadratic doublet word,

$$
\int_Ru_\ell\mathcal K_{C,R;\ell m}v_m:
\qquad
[\mathcal K_{C,R;\ell m}]=4-d_{C,\ell}-d_{C,m},
\quad
\operatorname{gh}(\mathcal K_{C,R;\ell m})=-2-g_\ell-g_m,
\quad
\epsilon(\mathcal K_{C,R;\ell m})=\epsilon_\ell+\epsilon_m.
\tag{3E.84a4}
$$

Let \(\mathfrak X_{C,R}\) contain every Step-3B physical component,
\(c,\bar c,b\), all pairs in (3E.84a1), and the declared background
components.  Let \(\operatorname{NF}_{C,R}\) quotient only by total
ordinary covariant derivatives, the exact covariant-derivative
commutators with curvature retained, representation identities, and
identically zero component densities.  It preserves field type,
parity, ghost number, dimension, and ordered color word.

Its most general power-counting-renormalizable gauge fermion is the
component normal-form word generator

$$
\boxed{
\Psi_{C,R}^{\rm WZ,pc}
:=-\frac{b_{Y,C,R}}2\int_R\bar c_R^A
(\mathcal Y_{C,R})_{AB}b_R^B
+\int_R
\sum_{\omega\in\operatorname{NF}_{C,R}
(\mathfrak W_{C,R}^{\rm pc,+})}
g_{C,R,\omega}\operatorname{Contr}_\omega
[(P_1x_1)\cdots(P_Nx_N)],}
\tag{3E.84b}
$$

Every word in \(\mathfrak W_{C,R}^{\rm pc,+}\) obeys

$$
[g_{C,R,\omega}]+\sum_jd(P_jx_j)=4,
\qquad
[g_{C,R,\omega}]\ge0,
\qquad
\sum_j\operatorname{gh}(x_j)=-1,
\qquad
\sum_j\epsilon(P_jx_j)=1\pmod2.
\tag{3E.84b1}
$$

where the nonnegative-dimension word sum contains
\(\int_R\bar c_R^A\mathcal F_{C,R,A}\), contains every admitted word
built from the finite doublet family (3E.84a1), and excludes the
already displayed \(\bar c\mathcal Y_Cb\) monomial when
\(b_{Y,C,R}=1\).  The admitted component family is

$$
\boxed{
\begin{aligned}
\mathfrak G_{C,R}^{\rm WZ,pc}:=\bigg\{\Psi_{C,R}^{\rm WZ,pc}:\;&
\mathcal M_{C,R}^{\rm FP,\perp}:
\mathscr G_{C,R}^{\perp}\overset{\cong}{\longrightarrow}
\mathscr F_{C,R}^{\perp},\\
&\operatorname{Hess}\mathbb A_{C,R}^{\rm WZ}\big|_{
\mathscr H_{C,R}^{\perp}}\text{ is nondegenerate},
\quad
\mathfrak C_{C,E,\nu}^{\perp}\text{ satisfies (3E.52b)}
\bigg\}.
\end{aligned}}
\tag{3E.84b2}
$$

The Wess--Zumino exponent is

$$
\boxed{
\mathbb A_{C,R}^{\rm WZ}
=S_{C,R}^{\rm Step\text{-}3B}
+\mathbf s_{C,R}\Psi_{C,R}^{\rm WZ,pc}
+\tau_R^{-1}\log\boldsymbol\varpi_{C,R}^{\rm WZ}.}
\tag{3E.84c}
$$

Its LC and EC Hessians and vertices follow by direct component
differentiation (3E.79).  Equality with the full unconstrained slice
is not asserted unless the complete change-of-slice Berezinian,
residual projectors, cycle, and FP determinant are separately equal.

### 3E.9 Lorentz--Euclidean and four-ledger checks

For each homogeneous field block \(Y\), the finite Wick matrix and its
supertranspose are

$$
\boxed{
\begin{aligned}
(M_\nu^{\rm W,Y})^{\beta,sn}{}_{\alpha,rm}
&:=\int_{E,\varsigma_Y}U_{E,Y}^{\vee\,\beta,sn}
\operatorname{Wick}_Y(U_{L,Y,\alpha,rm}).
\end{aligned}}
\tag{3E.84d}
$$

Let \(M_{C,\nu}^{\rm W,\perp}\) be the direct sum of (3E.84d) on
the residual component slots and

$$
\boxed{
M_{S,\nu}^{\rm W,\perp}
:=\iota_{E,\nu}^{\perp}M_{C,\nu}^{\rm W,\perp}
\pi_{L,\nu}^{\perp}.}
\tag{3E.84e}
$$

The external and antifield blocks are

$$
\boxed{
\begin{aligned}
M_{\overline Q^\star}^{\rm W}[\overline Q_L^\star]
&=-i\overline Q_L^\star(M_{\overline Q}^{\rm W})^{-1},\\
M_{\Omega^\star}^{\rm W}[\Omega_L^\star]
&=-i\Omega_L^\star(M_{\Omega}^{\rm W})^{-1},\\
M_{\star{\rm ext}}^{\rm W}[Q_L^{\star{\rm ext}}]
&=-iQ_L^{\star{\rm ext}}(M_{C,\nu}^{\rm W,\perp})^{-1},\\
M_{\nu,\rm ext}^{\rm W}
&:=M_{\overline Q}^{\rm W}\oplus M_{\Omega}^{\rm W}
\oplus M_{\overline Q^\star}^{\rm W}
\oplus M_{\Omega^\star}^{\rm W}
\oplus M_{\star{\rm ext}}^{\rm W}.
\end{aligned}}
\tag{3E.84f}
$$

For an input label \(\mathsf A\), define
\(M_{X,\mathsf A}=M_{X,\nu}^{\rm W,\perp}\) on internal slots and
the corresponding block of \(M_{\nu,\rm ext}^{\rm W}\) on external
or antifield slots.  The symbols
\(\pi_{R,\nu}^{\rm ext}\) and \(\iota_{R,\nu}^{\rm ext}\) denote the
same dual-monomial coefficient bijection (3E.77a) restricted to the
external list, with
\(\pi_{R,\nu}^{\rm ext}\iota_{R,\nu}^{\rm ext}=\mathbf1\).

For \(X\in\{S,C\}\), direct differentiation of
\(\mathbb A_{X,E,\nu}[x_E;q_E]
=-i\mathbb A_{X,L,\nu}[M_X^{-1}x_E;
(M_{\nu,\rm ext}^{\rm W})^{-1}q_E]
+\tau_E^{-1}\log\operatorname{Ber}(M_X)^{-1}\) gives

$$
\boxed{
\begin{aligned}
\mathbb H_{X,E,\nu}
&=-i(M_X^{-1})^{\rm sT}\mathbb H_{X,L,\nu}M_X^{-1},\\
\mathbb G_{X,E,\nu}
&=iM_X\mathbb G_{X,L,\nu}M_X^{\rm sT},\\
\mathbb V_{X,E,\nu;\mathsf A_1\cdots\mathsf A_n}^{(n)}
(y_1,\ldots,y_n)
&=-i\mathbb V_{X,L,\nu}^{(n)}
(M_{X,\mathsf A_1}^{-1}y_1,\ldots,
M_{X,\mathsf A_n}^{-1}y_n),
\end{aligned}}
\tag{3E.85}
$$

where \(M_X:=M_{X,\nu}^{\rm W,\perp}\).  For example,

$$
\begin{aligned}
\mathbb H_E\mathbb G_E
&=(-i)(i)(M^{-1})^{\rm sT}\mathbb H_L
M^{-1}M\mathbb G_LM^{\rm sT}\\
&=(M^{-1})^{\rm sT}\widetilde{\mathbb P}_L^{\perp}M^{\rm sT}
=\widetilde{\mathbb P}_E^{\perp},\\
\mathbb G_E\mathbb H_E
&=(i)(-i)M\mathbb G_LM^{\rm sT}(M^{-1})^{\rm sT}
\mathbb H_LM^{-1}\\
&=M\mathbb P_L^{\perp}M^{-1}
=\mathbb P_E^{\perp}.
\end{aligned}
\tag{3E.85a}
$$

Define the four route data

$$
\boxed{
\begin{array}{c|c|c|c}
\mathcal R&\text{source}&\text{target}
&(T_{\mathcal R}^{\rm int},T_{\mathcal R}^{\rm ext},a_{\mathcal R})\\ \hline
\mathrm{LS\to LC}&(S,L)&(C,L)
&(\pi_{L,\nu}^{\perp},\pi_{L,\nu}^{\rm ext},1)\\
\mathrm{ES\to EC}&(S,E)&(C,E)
&(\pi_{E,\nu}^{\perp},\pi_{E,\nu}^{\rm ext},1)\\
\mathrm{LS\to ES^{W}}&(S,L)&(S,E^{W})
&(M_{S,\nu}^{\rm W,\perp},M_{\nu,\rm ext}^{\rm W},-i)\\
\mathrm{LC\to EC^{W}}&(C,L)&(C,E^{W})
&(M_{C,\nu}^{\rm W,\perp},M_{\nu,\rm ext}^{\rm W},-i)
\end{array}.}
\tag{3E.86}
$$

The superscript \(W\) denotes the Wick-image Euclidean density,
projector, NK carrier, and integration cycle.  Intrinsic ES and EC
cycles remain independently defined data.

The NK carrier used by every route is the ordered tuple

$$
\boxed{
\begin{aligned}
\mathcal K_R^{\rm NK}
&:=\bigl(
\beta_{{\rm NK},R},
\mathscr R_{{\rm NK},R}^{\rm BV},
x_{{\rm NK},R},
\mathfrak F_{R,\nu}^{\rm NK},
\boldsymbol\varpi_{\Psi,R,\nu},
W_{\Psi,R,\nu},
[\mathfrak L_{\Psi,{\rm NK},R,\nu}^{\perp}],
\mathcal A_{R,\nu}^{\rm NK}
\bigr),\\
x_{{\rm NK},R}
&:=\{(\mathfrak u_{R,\ell},\mathfrak v_{R,\ell})
\}_{\ell\in\mathscr R_{{\rm NK},R}^{\rm BV}}
\big|_{\mathfrak L_{\Psi,{\rm NK},R,\nu}^{\perp}},\\
\mathcal A_{R,\nu}^{\rm NK}
&:=\bigl(
B_{R,\rm std},B_{R,\rm ext},B_{R,\rm BV},
\vartheta_{R,\nu}^{\rm NK},
\mathcal I_{{\rm NK},0,R,\nu},
\mathfrak R_{F,R,\nu},
\mathfrak R_{\Delta,R,\nu},
\mathfrak R_{O,R,\nu}
\bigr),\\
\mathfrak R_{F,R,\nu}
&:=\mathfrak F_{R,\nu}^{\rm NK,aux}
-\mathfrak F_{R,\nu}^{\rm NK,req},
\qquad
\mathfrak R_{\Delta,R,\nu}:=\Delta_{\rm ext,R,\nu}^{2},\\
\mathfrak R_{O,R,\nu}
&:=\mathfrak O_{R,\nu}^{\rm BV,ext}[W_{\rm ext,R,\nu}].
\end{aligned}}
\tag{3E.86a}
$$

For a route \(\mathcal R:s\to t\), write
\(T_i:=T_{\mathcal R}^{\rm int}\),
\(T_e:=T_{\mathcal R}^{\rm ext}\), and
\(a:=a_{\mathcal R}\).  Its componentwise pushforward is

$$
\boxed{
\begin{aligned}
\widehat x_{\rm NK}&:=T_i|_{\rm NK}\,x_{{\rm NK},s},
&
\widehat{\mathscr R}_{\rm NK}^{\rm BV}
&:=(T_i|_{\rm NK})_{\#}\mathscr R_{{\rm NK},s}^{\rm BV},\\
\widehat{\mathfrak F}^{\rm NK}(q_t)
&:=\mathfrak F_s^{\rm NK}(T_e^{-1}q_t),
&
\widehat W(y_t;q_t)
&:=aW_s(T_i^{-1}y_t;T_e^{-1}q_t),\\
\widehat{\boldsymbol\varpi}(y_t;q_t)
&:=\boldsymbol\varpi_s(T_i^{-1}y_t;T_e^{-1}q_t)
\operatorname{Ber}(T_i)^{-1},
&
[\widehat{\mathfrak L}_{\rm NK}^{\perp}]
&:=(T_i|_{\rm NK})_*[\mathfrak L_{{\rm NK},s}^{\perp}],\\
\widehat\vartheta^{\rm NK}
&:=T_i|_{\rm NK}\circ\vartheta_s^{\rm NK}
\circ(T_{\mathcal R}^{\Xi})^{-1},
&
\widehat{\mathcal I}_{{\rm NK},0}
&:=\mathcal I_{{\rm NK},0,s},\\
\widehat{\mathfrak R}_F(q_t)
&:=\mathfrak R_{F,s}(T_e^{-1}q_t),
&
\widehat{\mathfrak R}_\Delta
&:=\Delta[\widehat{\boldsymbol\varpi}]_{\rm ext}^{2},\\
\widehat{\mathfrak R}_O
&:=\mathfrak O_t^{\rm BV,ext}
[\widehat W_{\rm ext};\widehat{\boldsymbol\varpi}],
&
\widehat{\mathcal A}^{\rm NK}
&:=\bigl(B_{s,\rm std},B_{s,\rm ext},B_{s,\rm BV},
\widehat\vartheta^{\rm NK},\widehat{\mathcal I}_{{\rm NK},0},
\widehat{\mathfrak R}_F,
\widehat{\mathfrak R}_\Delta,
\widehat{\mathfrak R}_O\bigr).
\end{aligned}}
\tag{3E.86b}
$$

Here \(T_{\mathcal R}^{\Xi}\) is the same projection or Wick block
as \(T_i\), restricted to the auxiliary realization
\(\Xi^{\rm NK}\), and \((T_i|_{\rm NK})_\#\) transports the typed
doublet labels together with parity, ghost number, dimension, domain,
orientation, and cycle.  The numerical equality
\(\widehat{\mathcal I}_{{\rm NK},0}=\mathcal I_{{\rm NK},0,s}\)
follows because
\(\tau_ta=\tau_s\) and the normalized numerator and denominator are
changed by the same Berezinian.  Finally,

$$
\boxed{
\mathcal T_{\mathcal R}^{\rm NK}\mathcal K_s^{\rm NK}
:=\bigl(
\beta_{{\rm NK},s},
\widehat{\mathscr R}_{\rm NK}^{\rm BV},
\widehat x_{\rm NK},
\widehat{\mathfrak F}^{\rm NK},
\widehat{\boldsymbol\varpi},
\widehat W,
[\widehat{\mathfrak L}_{\rm NK}^{\perp}],
\widehat{\mathcal A}^{\rm NK}
\bigr).}
\tag{3E.86c}
$$

For a leg \(\mathsf A\), let
\(T_{\mathcal R,\mathsf A}\) be the internal or external block selected
by its role.  For each row, define the independently calculated defects

$$
\boxed{
\begin{aligned}
\mathfrak D_{H}^{\mathcal R}
&:=H_t-a_{\mathcal R}((T_{\mathcal R}^{\rm int})^{-1})^{\rm sT}
H_s(T_{\mathcal R}^{\rm int})^{-1},\\
\mathfrak D_{G}^{\mathcal R}
&:=G_t-a_{\mathcal R}^{-1}T_{\mathcal R}^{\rm int}G_s
(T_{\mathcal R}^{\rm int})^{\rm sT},\\
\mathfrak D_{V^{(n)}}^{\mathcal R}(y_1,\ldots,y_n)
&:=V_t^{(n)}(y_1,\ldots,y_n)
-a_{\mathcal R}V_s^{(n)}
(T_{\mathcal R,\mathsf A_1}^{-1}y_1,\ldots,
T_{\mathcal R,\mathsf A_n}^{-1}y_n),\\
\mathfrak D_{\varpi}^{\mathcal R}(y;q)
&:=\varpi_t(y;q)
-\varpi_s((T_{\mathcal R}^{\rm int})^{-1}y;
(T_{\mathcal R}^{\rm ext})^{-1}q)
\operatorname{Ber}(T_{\mathcal R}^{\rm int})^{-1},\\
\mathfrak D_P^{\mathcal R}
&:=P_t^{\perp}T_{\mathcal R}^{\rm int}
-T_{\mathcal R}^{\rm int}P_s^{\perp},\\
\mathfrak D_{\mathfrak L}^{\mathcal R}
&:=[\mathfrak L_t^{\perp}]-(T_{\mathcal R}^{\rm int})_*
[\mathfrak L_s^{\perp}],\\
\mathfrak D_{\rm NK}^{\mathcal R}
&:=\mathcal K_{t}^{\rm NK}
-\mathcal T_{\mathcal R}^{\rm NK}\mathcal K_s^{\rm NK}.
\end{aligned}}
\tag{3E.87}
$$

For the two projection routes, the chain rule applied to (3E.78)
uses \(\iota_R^{\rm tot}:=\iota_R^{\perp}\oplus
\iota_R^{\rm ext}\) and gives

$$
\begin{aligned}
\mathfrak D_H^{S R\to C R}
&=\vec\partial_{\rm int}^{2}
(\mathbb A_{S,R}\circ\iota_R^{\rm tot})
-(\iota_R^{\perp})^\vee
(\vec\delta_{\rm int}^{2}\mathbb A_{S,R})
\iota_R^{\perp}=0,\\
\mathfrak D_{V^{(n)}}^{S R\to C R}
&=\vec\partial_{\rm tot}^{n}
(\mathbb A_{S,R}\circ\iota_R^{\rm tot})
-(\vec\delta_{\rm tot}^{n}\mathbb A_{S,R})
\circ(\iota_R^{\rm tot})^{\otimes n}=0,\\
\mathfrak D_G^{S R\to C R}
&=H_{C,R}^{-1}
-\pi_R^{\perp}H_{S,R}^{-1}(\pi_R^{\perp})^\vee=0.
\end{aligned}
\tag{3E.87a0}
$$

The last equality follows by multiplying the candidate inverse on
both sides and using the complete coefficient bijection (3E.77a).
For the two Wick routes, direct substitution of (3E.85) into (3E.87)
gives

$$
\boxed{
\mathfrak D_H^{X L\to X E^{W}}
=\mathfrak D_G^{X L\to X E^{W}}
=\mathfrak D_{V^{(n)}}^{X L\to X E^{W}}=0,
\qquad X\in\{S,C\}.}
\tag{3E.87a1}
$$

For a projection route \(T=\pi_{R,\nu}^{\perp}\), define its admission
predicate by the four explicit equalities

$$
\boxed{
B_{\mathcal R}^{\rm proj}=1
\Longleftrightarrow
\begin{cases}
\boldsymbol\varpi_C(y;q)
=\boldsymbol\varpi_S(\iota_R^{\perp}y;
\iota_R^{\rm ext}q)\operatorname{Ber}(\pi_R^{\perp})^{-1},\\
P_C^{\perp}\pi_R^{\perp}=\pi_R^{\perp}P_S^{\perp},\\
[\mathfrak L_{C,R,\nu}^{\perp}]
=(\pi_R^{\perp})_*[\mathfrak L_{S,R,\nu}^{\perp}],\\
\mathcal K_{C,R}^{\rm NK}
=\mathcal T_{\pi_R}^{\rm NK}\mathcal K_{S,R}^{\rm NK}.
\end{cases}}
\tag{3E.87a2}
$$

Substitution of these four lines into (3E.87) gives

$$
\boxed{
B_{\mathcal R}^{\rm proj}=1
\Longrightarrow
\mathfrak D_{\varpi}^{\mathcal R}
=\mathfrak D_P^{\mathcal R}
=\mathfrak D_{\mathfrak L}^{\mathcal R}
=\mathfrak D_{\rm NK}^{\mathcal R}=0.}
\tag{3E.87a3}
$$

For \(X\in\{S,C\}\), the Wick-image Euclidean data are defined by

$$
\begin{aligned}
\boldsymbol\varpi_{X,E}^{W}(y_E;q_E)
&:=\boldsymbol\varpi_{X,L}(M_X^{-1}y_E;
(M_{\rm ext}^{W})^{-1}q_E)\operatorname{Ber}(M_X)^{-1},\\
P_{X,E}^{W,\perp}&:=M_XP_{X,L}^{\perp}M_X^{-1},\\
[\mathfrak L_{X,E,\nu}^{W,\perp}]
&:=(M_X)_*[\mathfrak L_{X,L,\nu}^{\perp}],\\
\mathcal K_{X,E}^{\rm NK,W}
&:=\mathcal T_{M_X}^{\rm NK}\mathcal K_{X,L}^{\rm NK}.
\end{aligned}
\tag{3E.87a4}
$$

Each difference in (3E.87) is then one expression minus itself, so

$$
\boxed{
\mathfrak D_{\varpi}^{XL\to XE^W}
=\mathfrak D_P^{XL\to XE^W}
=\mathfrak D_{\mathfrak L}^{XL\to XE^W}
=\mathfrak D_{\rm NK}^{XL\to XE^W}=0.}
\tag{3E.87a5}
$$

Tuple equality in every NK defect means componentwise equality of all
eight entries of (3E.86a), including all eight entries of
\(\mathcal A^{\rm NK}\).  If \(B_{\mathcal R}^{\rm proj}=0\), the
corresponding projection defect is retained.

The intrinsic Euclidean cycle defect is retained separately:

$$
\boxed{
\mathfrak D_{X,\Psi,E,\nu}^{\rm cyc}[j_E]
:=\mathcal Z_{X,\Psi,E,\nu}
[j_E;\mathfrak L_{X,\Psi,E,\nu}^{\perp}]
-\lim_{\epsilon\downarrow0}
\mathcal Z_{X,\Psi,E,\nu}^{\epsilon,\rm W}
[j_E;M_{X,\nu}^{\rm W,\perp}
\mathfrak L_{X,\Psi,L,\nu}^{\perp}].}
\tag{3E.87a}
$$

Let \(\Omega_{X,E,\nu}[j]\) be the complete finite-dimensional
holomorphic top form, including density, NK factor, action, and source.
An intrinsic-to-Wick-image cycle comparison is admitted only when
there is a smooth proper isotopy

$$
F_t:\mathfrak L_{X,E,\nu}^{W,\perp}\longrightarrow
\mathcal U_{X,E,\nu},
\qquad
\mathfrak L_t:=F_t(\mathfrak L_{X,E,\nu}^{W,\perp}),
\qquad
\mathfrak L_0=\mathfrak L^{W,\perp},
\quad
\mathfrak L_1=\mathfrak L^{\rm int,\perp}.
\tag{3E.87a6}
$$

For every source in a declared open neighborhood
\(\mathcal J\ni0\), require

$$
\boxed{
\begin{gathered}
d\Omega_{X,E,\nu}[j]=0\quad\text{on }\mathcal U_{X,E,\nu},\\
F_t\text{ crosses no pole, branch singularity, or zero of the chosen
density trivialization},\\
\lim_{r\to\infty}\sup_{t\in[0,1],\,j\in\mathcal J}
\left|\int_{\partial(\mathfrak L_t\cap B_r)}
\iota_{V_t}\Omega_{X,E,\nu}[j]\right|=0,
\qquad V_t:=\dot F_t\circ F_t^{-1},\\
\lim_{\epsilon\downarrow0}
\int_{\mathfrak L^{W,\perp}}e^{-\epsilon\mathscr Q^W}
\Omega[j]
=\int_{\mathfrak L^{W,\perp}}\Omega[j]
\quad\text{uniformly for }j\in\mathcal J.
\end{gathered}}
\tag{3E.87a7}
$$

Cartan's formula and Stokes' theorem now give the complete calculation

$$
\begin{aligned}
\frac d{dt}\int_{\mathfrak L_t}\Omega[j]
&=\int_{\mathfrak L_t}
(d\iota_{V_t}+\iota_{V_t}d)\Omega[j]\\
&=\lim_{r\to\infty}
\int_{\partial(\mathfrak L_t\cap B_r)}
\iota_{V_t}\Omega[j]=0,\\
\mathfrak D_{X,\Psi,E,\nu}^{\rm cyc}[j]
&=\int_{\mathfrak L_1}\Omega[j]-\int_{\mathfrak L_0}\Omega[j]\\
&=\int_0^1dt\,\frac d{dt}
\int_{\mathfrak L_t}\Omega[j]=0,
\qquad j\in\mathcal J.
\end{aligned}
\tag{3E.87a8}
$$

Thus \(\mathfrak D^{\rm cyc}[0]=0\) follows as the \(j=0\) case.
If any line of (3E.87a6)--(3E.87a7) fails, the intrinsic Euclidean
cycle is an independent ledger and (3E.87a) remains a recorded
nonzero or unevaluated defect.  The route scope is

$$
\boxed{
\begin{array}{c|c}
\text{route}&\text{admission}\\ \hline
\mathrm{LS\to LC},\ \mathrm{ES\to EC}
&B_{\mathcal R}^{\rm proj}=1\\
\mathrm{LS\to ES^W},\ \mathrm{LC\to EC^W}
&\text{exact finite change of variables (3E.87a4)}\\
\mathrm{LS\to ES^{\rm int}},\ \mathrm{LC\to EC^{\rm int}}
&\text{(3E.87a4) and (3E.87a6)--(3E.87a7)}\\
\mathrm{ES^{\rm int}},\ \mathrm{EC^{\rm int}}
&\text{independent Euclidean ledgers}
\end{array}.}
\tag{3E.87a9}
$$

The following calculation is on the untruncated ambient algebra:

$$
\boxed{
\begin{aligned}
\mathbf s_R^2\mathfrak c_R
&=i[(i\mathfrak c_R^2)\mathfrak c_R
-\mathfrak c_R(i\mathfrak c_R^2)]=0,\\
\mathbf s_R^2\Phi_R
&=i(i\mathfrak c_R^2)\Phi_R
-i\mathfrak c_R(i\mathfrak c_R\Phi_R)=0,\\
\mathbf s_R^2\mathfrak u_{R,\ell}
&=\mathbf s_R\mathfrak v_{R,\ell}=0,
\qquad
\mathbf s_R^2\mathfrak v_{R,\ell}=0,\\
\mathbf s_R^2e^{\mathcal V_R}
&=-\widetilde{\mathfrak c}_R^2e^{\mathcal V_R}
+\widetilde{\mathfrak c}_R^2e^{\mathcal V_R}
-\widetilde{\mathfrak c}_Re^{\mathcal V_R}\mathfrak c_R
+\widetilde{\mathfrak c}_Re^{\mathcal V_R}\mathfrak c_R\\
&\quad-e^{\mathcal V_R}\mathfrak c_R^2
+e^{\mathcal V_R}\mathfrak c_R^2=0.
\end{aligned}}
\tag{3E.87b}
$$

Hence

$$
\boxed{
\mathbf s_R(S_{0,R}^{\rm ren}+\mathbf s_R\Psi_R^{\rm pc})
=\mathbf s_RS_{0,R}^{\rm ren}+\mathbf s_R^2\Psi_R^{\rm pc}
=0.}
\tag{3E.87c}
$$

At finite \(\nu\), no nilpotency statement is substituted for the
regulated residual.  Define

$$
\boxed{
\begin{aligned}
\mathbf s_{R,\nu}&:=\pi_{R,\nu}\mathbf s_R\iota_{R,\nu},
\qquad
\mathfrak R_{R,\nu}^{\mathsf i}
:=\mathbf s_{R,\nu}^{2}Q_{R,\nu}^{\mathsf i},\\
\mathfrak D_{\rm CME,R,\nu}
&:=\mathbf s_{R,\nu}S_{0,R,\nu}
+\sum_{\mathsf i}(-1)^{\epsilon_{\mathsf i}}
Q_{R,\nu,\mathsf i}^{\star}\mathfrak R_{R,\nu}^{\mathsf i}\\
&=\frac12
(S_{\min,R,\nu},S_{\min,R,\nu})_{R,\nu},\\
\mathfrak C_{\rm ext,R,\nu}^{(0)}
&:=\frac12(S_{\rm ext,R,\nu},S_{\rm ext,R,\nu})_{\rm ext,R,\nu}.
\end{aligned}}
\tag{3E.87c1}
$$

Gauge fixing is a BV canonical transformation.  With
\(S_{\rm ext,\Psi,R,\nu}
:=e^{\operatorname{ad}_{\Psi_{R,\nu}}}S_{\rm ext,R,\nu}\),

$$
\boxed{
\begin{aligned}
\frac12(S_{\rm ext,\Psi,R,\nu},S_{\rm ext,\Psi,R,\nu})_{\rm ext,R,\nu}
&=e^{\operatorname{ad}_{\Psi_{R,\nu}}}
\mathfrak C_{\rm ext,R,\nu}^{(0)},\\
\mathcal S_{R,\nu}(S_{\rm ext,\Psi,R,\nu})
&:=\frac12(S_{\rm ext,\Psi,R,\nu},
S_{\rm ext,\Psi,R,\nu})_{\rm ext,R,\nu}.
\end{aligned}}
\tag{3E.87d}
$$

Thus the exact finite-cutoff tree identity is

$$
\boxed{
\vec\delta^{n}\mathcal S_{R,\nu}
(S_{\rm ext,\Psi,R,\nu})
=\vec\delta^{n}
e^{\operatorname{ad}_{\Psi_{R,\nu}}}
\mathfrak C_{\rm ext,R,\nu}^{(0)}.}
\tag{3E.87d1}
$$

Its right side is zero only after separately proving
\(\mathbf s_{R,\nu}S_{0,R,\nu}=0\) and
\(\mathfrak R_{R,\nu}^{\mathsf i}=0\) for every slot, together with
the finite split-sector equalities entering
\(\mathfrak C_{\rm ext,R,\nu}^{(0)}\).  The density
term in (3E.73) enters instead through
\(\mathfrak O_{R,\nu}^{\rm BV}[W]\) of (3D.64); it is never inserted
into (3E.87d).  Background covariance has the independent regulated
defect

$$
\boxed{
\begin{aligned}
\mathfrak D_{\rm bg,R,\nu}
&:=\mathcal W_{R,\rm bg}\mathbb A_{R,\nu}\\
&=\mathcal W_{R,\rm bg}W_{\Psi,R,\nu}
+\tau_R^{-1}\mathcal W_{R,\rm bg}
\log\boldsymbol\varpi_{\Psi,R,\nu},\\
\vec\delta^{n}\mathfrak D_{\rm bg,R,\nu}
&=\vec\delta^{n}\mathcal W_{R,\rm bg}\mathbb A_{R,\nu}.
\end{aligned}}
\tag{3E.87e}
$$

The background Ward identities are asserted only when both displayed
defects vanish for an invariant regulator, density, and residual
cycle.

On the standard factorized branch, write

$$
v_{R,\parallel}=\mathscr R_{R,\nu}^{\rm g,\perp}\gamma_R,
\qquad
\mathcal M_R:=\mathcal M_{R,\nu}^{\rm FP,\perp},
\tag{3E.87f}
$$

so the complete orbit-quartet quadratic exponent is

$$
\mathbb A_{R,\parallel}^{(2)}
=\langle\mathfrak n_R,\mathcal M_R\gamma_R\rangle_R
-\frac12\langle\mathfrak n_R,\mathcal Y_R\mathfrak n_R\rangle_R
-\langle\mathfrak c'_R,\mathcal M_R
\mathfrak c_R^{\rm pair}\rangle_R.
\tag{3E.87f1}
$$

Without reversing the typed pairing,

$$
\begin{aligned}
\langle\mathfrak n,\mathcal M\gamma\rangle
-\frac12\langle\mathfrak n,\mathcal Y\mathfrak n\rangle
&=\frac12\langle\mathcal Y^{-1}\mathcal M\gamma,
\mathcal M\gamma\rangle\\
&\quad-\frac12\langle
\mathfrak n-\mathcal Y^{-1}\mathcal M\gamma,
\mathcal Y(\mathfrak n-\mathcal Y^{-1}\mathcal M\gamma)
\rangle.
\end{aligned}
\tag{3E.87f2}
$$

Define the normalized longitudinal factor by the two endpoint cycles

$$
\mathfrak F_{R,\nu}^{\parallel}
:=\frac{
\displaystyle\int_{\mathfrak C_{\gamma,R,\nu}[\mathcal M_R,\mathcal Y_R]}
D'\gamma\,
e^{\frac{\tau_R}{2}\langle\mathcal Y_R^{-1}\mathcal M_R\gamma,
\mathcal M_R\gamma\rangle_R}}
{\displaystyle\int_{\mathfrak C_{\gamma,R,\nu}
[\mathcal M_{0,R},\mathcal Y_{0,R}]}
D'\gamma\,
e^{\frac{\tau_R}{2}\langle\mathcal Y_{0,R}^{-1}
\mathcal M_{0,R}\gamma,\mathcal M_{0,R}\gamma\rangle_R}}.
\tag{3E.87f3}
$$

The cycles are fixed, not independently chosen:

$$
\mathfrak C_{\gamma,R,\nu}[\mathcal M,\mathcal Y]
=\mathcal M^{-1}\mathfrak C_{f,R,\nu}[\mathcal Y],
\qquad
\mathfrak C_{\gamma,R,\nu}[\mathcal M_0,\mathcal Y_0]
=\mathcal M_0^{-1}\mathfrak C_{f,R,\nu}[\mathcal Y_0].
\tag{3E.87f4}
$$

The finite changes \(f=\mathcal M\gamma\) and
\(f_0=\mathcal M_0\gamma_0\) give every factor:

$$
\begin{aligned}
\mathfrak F_{R,\nu}^{\parallel}
&=\operatorname{Ber}_{\mathscr G_R^{\perp}}
(\mathcal M_0^{-1}\mathcal M)^{-1}
\frac{\mathcal N_{R,\nu}[\mathcal Y_R]}
{\mathcal N_{R,\nu}[\mathcal Y_{0,R}]}\\
&=(\mathfrak F_{R,\nu}^{\rm FP})^{-1}
(\mathfrak F_{R,\nu}^{\rm av})^{-1},\\
\mathfrak F_{R,\nu}^{\parallel}
\mathfrak F_{R,\nu}^{\rm FP}
\mathfrak F_{R,\nu}^{\rm nm}
\mathfrak F_{R,\nu}^{\rm NK,req}
&=(\mathfrak F^{\rm FP})^{-1}(\mathfrak F^{\rm av})^{-1}
\mathfrak F^{\rm FP}\mathfrak F^{\rm nm}
\frac{\mathfrak F^{\rm av}}{\mathfrak F^{\rm nm}}=1.
\end{aligned}
\tag{3E.87f5}
$$

Consequently the exact branch residuals are

$$
\boxed{
\begin{aligned}
\mathfrak D_{R,\nu}^{\rm det,ext}
&:=\mathfrak F^{\parallel}\mathfrak F^{\rm FP}
\mathfrak F^{\rm nm}\mathfrak F^{\rm NK,req}-1=0,
&&B_{\rm std}=1,\ B_{\rm ext}=1,\ B_{\rm BV}=0,\\
\mathfrak D_{R,\nu}^{\rm det,dens}[y]
&:=\mathfrak F^{\parallel}[y]\mathfrak F^{\rm FP}[y]
\mathfrak F^{\rm nm}[y]\mathfrak F^{\rm NK,req}[y]-1=0,
&&B_{\rm std}=1,\ B_{\rm ext}=0,\ B_{\rm BV}=0,\\
\mathfrak D_{R,\nu}^{\rm det,BV}[y]
&:=\mathfrak F^{\parallel}[y]\mathfrak F^{\rm FP}[y]
\mathfrak F^{\rm nm}[y]\mathfrak F^{\rm NK,aux}[y]-1=0,
&&B_{\rm BV}=1.
\end{aligned}}
\tag{3E.87f6}
$$

The density identity is fiberwise at fixed spectator \(y\).  The BV
identity uses exactly
\(\mathfrak F^{\rm NK,aux}=\mathfrak F^{\rm NK,req}\).

On the coupled branch these four factors do not exist separately.
For a finite coefficient space \(X\), \(\operatorname{Slot}(X)\) is
its set of fully typed coefficient labels.  Let
\(\mathscr H_{R,\nu}^{\rm BV-NK,act}\) be the integrated BV--NK
coefficient space present on the selected branch, and let
\(\Gamma_{R,\nu}\) be the undirected Hessian-support graph:

$$
\boxed{
\begin{aligned}
\mathscr I_{R,\nu}
&:=\operatorname{Slot}(\mathscr H_{\Psi,R,\nu}^{\perp}),\\
\mathsf A\!\!\mathrel{-}_{\Gamma_{R,\nu}}\!\!\mathsf B
&\Longleftrightarrow
\left.
\mathbb H_{R,\nu;\mathsf A\mathsf B}
\right|_{\Xi=\Xi_{\rm vac}}\ne0
\quad\text{or}\quad
\left.
\mathbb H_{R,\nu;\mathsf B\mathsf A}
\right|_{\Xi=\Xi_{\rm vac}}\ne0,\\
\mathscr S_{R,\nu}^{\rm seed}
&:=\operatorname{Slot}\!\left(
\gamma_R,\mathfrak c_R,\widetilde{\mathfrak c}_R,
\{\mathfrak u_{R,\ell},\mathfrak v_{R,\ell}\}_{\ell\ {\rm active}},
\mathscr H_{R,\nu}^{\rm BV-NK,act}
\right).
\end{aligned}}
\tag{3E.87f7a}
$$

With \([\mathsf A]_{\Gamma}\) the connected component of
\(\mathsf A\), set

$$
\boxed{
\begin{aligned}
\mathscr H_{R,\nu}^{\rm cpl}
&:=\operatorname{span}\left\{
e_{\mathsf A}:\mathsf A\in\mathscr I_{R,\nu},
[\mathsf A]_{\Gamma_{R,\nu}}
\cap\mathscr S_{R,\nu}^{\rm seed}\ne\varnothing
\right\},\\
\mathscr H_{R,\nu}^{\rm spec}
&:=\operatorname{span}\left\{
e_{\mathsf A}:\mathsf A\in\mathscr I_{R,\nu},
[\mathsf A]_{\Gamma_{R,\nu}}
\cap\mathscr S_{R,\nu}^{\rm seed}=\varnothing
\right\},\\
\mathscr H_{\Psi,R,\nu}^{\perp}
&=\mathscr H_{R,\nu}^{\rm cpl}
\oplus\mathscr H_{R,\nu}^{\rm spec},\\
\mathbb H_{R,\nu}
&=\mathbb H_{R,\nu}^{\rm cpl}
\oplus\mathbb H_{R,\nu}^{\rm spec}.
\end{aligned}}
\tag{3E.87f7b}
$$

The defining nondegeneracy in (3E.22a) gives, at the vacuum,

$$
\boxed{
\begin{aligned}
\mathbb H_{R,\nu}^{\rm cpl}x=0
&\Longrightarrow
\mathbb H_{R,\nu}(x,0)=0
\Longrightarrow x=0,\\
\mathbb H_{R,\nu}^{\rm spec}y=0
&\Longrightarrow
\mathbb H_{R,\nu}(0,y)=0
\Longrightarrow y=0.
\end{aligned}}
\tag{3E.87f7c}
$$

Let \(q_{\rm cpl}\) be the \(\prec_\nu\)-ordered coefficient basis of
\(\mathscr H_{R,\nu}^{\rm cpl}\).  On the domain
\(\operatorname{Ber}\mathbb H_{q_{\rm cpl},R,\nu}^{\rm cpl}[y]\ne0\),

$$
\boxed{
\begin{aligned}
\mathfrak F_{R,\nu}^{\rm cpl}[y]
&:=\frac{
\displaystyle\int_{\mathfrak C_{q_{\rm cpl},R,\nu}[y]}
D'q_{\rm cpl}\,
e^{\frac{\tau_R}{2}q_{\rm cpl}
\mathbb H_{q_{\rm cpl},R,\nu}^{\rm cpl}[y]q_{\rm cpl}}}
{\displaystyle\int_{\mathfrak C_{q_{\rm cpl},0,R,\nu}}
D'q_{\rm cpl}\,
e^{\frac{\tau_R}{2}q_{\rm cpl}
\mathbb H_{q_{\rm cpl},0,R,\nu}q_{\rm cpl}}}\\
&=\operatorname{Ber}
\left[\mathbb H_{q_{\rm cpl},R,\nu}^{\rm cpl,gr}[y]
(\mathbb H_{q_{\rm cpl},0,R,\nu}^{\rm gr})^{-1}
\right]^{-1/2},\\
\mathfrak D_{R,\nu}^{\rm det,cpl}[y]
&:=\mathfrak F_{R,\nu}^{\rm cpl}[y]-1.
\end{aligned}}
\tag{3E.87f7}
$$

The quartet
\((\gamma_R,\mathfrak c'_R,\mathfrak c_R^{\rm pair},\mathfrak n_R)\)
is the special case
\(\mathscr H_{R,\nu}^{\rm cpl}
=\operatorname{span}(\gamma_R,\mathfrak c'_R,
\mathfrak c_R^{\rm pair},\mathfrak n_R)\).  If no proper seeded closure
exists, \(\mathscr H_{R,\nu}^{\rm cpl}
=\mathscr H_{\Psi,R,\nu}^{\perp}\).

For a nonsingular oriented Hessian-cycle path,

$$
\frac d{dt}\log\mathfrak F_q(t)
=-\frac12\operatorname{Str}
(\mathbb H_q(t)^{-1}\dot{\mathbb H}_q(t))
+\mathfrak B_q(t).
\tag{3E.87f8}
$$

Hence \(\mathfrak D^{\rm det,cpl}=0\) only if the supertrace vanishes,
the boundary flux \(\mathfrak B_q(t)\) vanishes, and
\(\operatorname{Ber}\mathbb H_q(t)\ne0\) along the full path.  The
general coupled branch retains (3E.87f7); it is not assigned the value
zero.  Finally, the
Taylor-roundtrip residual is coefficientwise

$$
\boxed{
\mathfrak D_{\rm Taylor,R}
:=\mathbb A_R[\Xi_{\rm vac}+\xi]-\mathbb A_R[\Xi_{\rm vac}]
-\sum_{n\ge1}\frac1{n!}\xi^{\mathsf A_1}\cdots\xi^{\mathsf A_n}
\mathbb V_{R;\mathsf A_1\cdots\mathsf A_n}=0.}
\tag{3E.87g}
$$

The result of Step 3E is the generating system

$$
\boxed{
\mathfrak R_{R,\nu}
=\left(
\mathbb H_{R,\nu}^{-1},
\{\mathbb V_{R,\nu}^{(n)}\}_{n\ge3},
\boldsymbol\varpi_{\Psi,R,\nu},
\mathcal K_{R,\nu}^{\rm NK},
\mathscr H_{\Psi,R,\nu}^{\perp},
\mathfrak L_{\Psi,R,\nu}^{\perp}
\right).}
\tag{3E.88}
$$

A numerical propagator table is a specialization of (3E.88) to one
vacuum, one \(\Psi_R^{\rm pc}\), one \(\mathcal Y_R\), one density, one
residual complement, and one Lorentzian or Euclidean cycle.

### 3E.10 Candidate-source boundary

$$
\boxed{
\text{source conventions imported}=\mathrm{false},
\qquad
\text{source coefficients adopted}=\mathrm{false}.}
\tag{3E.88a}
$$

| Candidate family | Imported-page locator | Independent Project derivation |
|---|---|---|
| Gaussian | subset 15--19; PDF 364--368 | (3E.44)--(3E.56a) |
| Delta/projector | subset 17--23; PDF 366--372 | (3E.27)--(3E.43a) |
| Chiral inverse | subset 16--19; PDF 365--368 | (3E.57)--(3E.62) |
| Vector/gauge fixing | subset 10--12, 35--41; PDF 359--361, 393--399 | (3E.63)--(3E.72a) |
| FP/NK | subset 11--12, 34, 39; PDF 360--361, 392, 397 | (3E.22a)--(3E.26a), (3E.48a)--(3E.54d), (3E.72) |
| Ordered vertices | subset 15--20, 40--46; PDF 364--369, 398--404 | (3E.45)--(3E.56a), (3E.73)--(3E.75) |
| \(D\)-algebra | subset 21--30; PDF 370--379 | (3E.32)--(3E.43a), (3E.75) |

Every source propagator sign, factor of \(i\), determinant power,
projector coefficient, vertex coefficient, and \(D\)-transfer sign is
excluded from the derivation.  The page subset remains candidate
evidence only.
