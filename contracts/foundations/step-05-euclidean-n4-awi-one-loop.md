# Step 5. Euclidean N=4 one-loop anomaly Ward identity

Status: `ACCEPTED_PHYSICAL_ONE_LOOP_ANOMALY_SECTOR__81_COMPLETE_EXACT__HT_CORRECTED_ROUNDTRIP_EXACT`

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`; physical settlement evidence 是 Section 11 列出的 target-blind exact audits。

Acceptance scope 是 physical bottom-letter one-loop anomaly sector、其 PBW jet tower 与 corrected holomorphic-twist round-trip。Project coefficients 在 target-blind seal 前已固定；holomorphic-twist 只作 check-only comparison。

General raw-graph \(q\)-equivariant functor、complete BV/Wess--Zumino/open-color evanescent-module theorem、formal \(U/Q_0\) absolute intertwiner 与 general reductive color-frame inverse 不属于此 acceptance scope，并在下文标为 `OUT_OF_SCOPE`；它们不是 physical 81-row result 的 blockers。

## Final Result List

定义

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}
:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}.
$$

每个 occurrence-resolved triangle 的 D-algebra numerator 使用 four-dimensional inverse square \(\bar r_e^{\,2}\)，Schwinger cut 使用 full regulated inverse \(r_{e,d}^{\,2}\)。因此 exact cutting failure 为

$$
\boxed{
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.}
$$

若 numerator 被替换为 full \(r_{e,d}^{\,2}\)，左端严格为零。Finite scalar remainder 为

$$
\boxed{
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2}{(\ell_d^2+\Delta)^3}
=\frac1{32\pi^2}.}
$$

所有 bare graph anomalies 都由这一 occurrence-wise \(\mu_\ell^2\) cutting failure 产生；没有额外 graph-specific \((4-d)\) factor。Section 7 给出 finite normal-product settlement 后的完整 physical formulas。

Exact physical census:

$$
N_{\mathrm{ordered\ pairs}}=81
=N_{\mathrm{COMPLETE\_EXACT}},
\qquad
N_{\mathrm{nonzero}}=29,
\qquad
N_{\mathrm{zero}}=52,
$$

$$
N_{\mathrm{HT\ direct\ match}}=81,
\qquad
N_{\mathrm{HT\ mismatch}}=0.
$$

对任意 \(m,n\in\mathbb Z_{\ge0}\)，derivative kernel exact equality 为

$$
\boxed{
\mathcal K^P_{m,n}
=\mathcal T^{\mathrm{HT,corr}}_{m,n}
=2\mathcal T^{\mathrm{HT,printed}}_{m,n}.}
$$

## 1. Notation and DRED

四类 bottom letters 定义为

$$
A^A:=(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+)^A,
\qquad
B_r^A:=(\boldsymbol\nabla_+\boldsymbol\Phi_r)^A,
$$

$$
C_r^A:=\widetilde{\boldsymbol\Phi}_r^A,
\qquad
D_{\dot a}^A:=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}^A,
\qquad
r=1,2,3,
\qquad
\dot a=\dot1,\dot2.
$$

Grassmann parities:

$$
|A|=|C_r|=0,
\qquad
|B_r|=|D_{\dot a}|=1.
$$

Holomorphic covariant derivatives 与 dotted raising 为

$$
P_{\dot a}:=\boldsymbol{\mathcal D}_{+\dot a},
\qquad
P^{\dot a}:=\epsilon^{\dot a\dot b}P_{\dot b},
\qquad
\epsilon^{\dot1\dot2}=+1,
\qquad
\epsilon_{\dot1\dot2}=-1.
$$

Fourier convention:

$$
X(x)=\int\frac{d^dp}{(2\pi)^d}e^{ip\cdot x}X(p),
\qquad
\partial_m\longmapsto ip_m,
$$

且每个 vertex 的 momentum 都取 incoming。

DRED definitions:

$$
d=4-2\epsilon,
\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},
$$

$$
\widehat\delta^m{}_m=d,
\qquad
\breve\delta^m{}_m=4-d=2\epsilon,
\qquad
\widehat\delta^m{}_r\breve\delta^r{}_n=0.
$$

Loop momentum 只有 hatted components：

$$
\ell^m=\widehat\delta^m{}_n\ell^n,
\qquad
\breve\delta^m{}_n\ell^n=0,
\qquad
\int_{\ell}^{\mathrm{DRED}}
:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}.
$$

The dimension-shift scalar representation must be kept separate from the
preceding Q4S/QDS projector representation.
Introduce a four-dimensional spin projector $\bar\delta$ and a formal
$(d-4)$ projector $\widetilde\delta$:

$$
\delta_d^{MN}=\bar\delta^{MN}+\widetilde\delta^{MN},
\qquad
\operatorname{tr}\bar\delta=4,
\qquad
\operatorname{tr}\widetilde\delta=d-4=-2\epsilon.
$$

Then

$$
\ell_d^2=\bar\ell^2+\widetilde\ell^2,
\qquad
\boxed{
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2.}
$$

In the Q4S/QDS representation,

$$
\delta_4=\widehat\delta+\breve\delta,
\qquad
\breve\delta\ell=0,
\qquad
\delta_4(\ell,\ell)=\widehat\delta(\ell,\ell)=\ell_d^2.
$$

Consequently $\bar\delta$ is not $\delta_4$, and $\widetilde\delta$ is not
$-\breve\delta$ as an operator identity.  The additional scalar-regulator
axiom is

$$
\boxed{
\text{finite superspace spin words use }\bar\delta,
\qquad
\text{propagator inverses use }\delta_d.}
$$

This is the sole meaning of $\mu_\ell^2=\bar\ell^2-\ell_d^2$.  Combining the
two representations before the regulated Schwinger family is summed would set
the scalar difference to zero and erase the anomaly.

In the scalar dimension-shift representation, spin algebra is
four-dimensional:

$$
\sigma_m\bar\sigma_n+\sigma_n\bar\sigma_m
=2\bar\delta_{mn}\mathbf1_2.
$$

The older Q4S notation writes the same finite spin word with
\(\delta_{4,mn}\); the two regulator representations are never contracted
with each other.

## 2. Step-5 source representative and cut

Physical one-loop graph audit 使用 Step-5A.64--5A.74 的 fixed Fermi--Feynman representative。令

$$
\mathcal A_E=
\begin{pmatrix}0&-\bar D_E^2/4\\-D_E^2/4&0\end{pmatrix},
\qquad
\mathcal A_E^2=\Box_E\mathbf1,
\qquad
H:=\frac h2\mathcal A_E.
$$

考虑满足下列条件的 quadratic completion class：保留 primary gauge-condition row \(F\)；residual physical/auxiliary FP blocks bijective；\(Z_{aa}\) invertible；所有 auxiliary trivial-pair coordinates 被积分；minimal action 不变。其 multiplier block 记为 \(\mathcal Y\)，令 \(Z=\mathcal Y^{-1}\)。在这个 normal-form class 内，physical Schur block 满足

$$
H_{\rm eff}=Z_{00}-Z_{0a}Z_{aa}^{-1}Z_{a0}=\mathcal Y_{00}^{-1}.
$$

故要求 \(H_{\rm eff}=H\) 强制

$$
\mathcal Y_{00}=H^{-1}
=2g^2\frac{\mathcal A_E}{\Box_E}
=\mathcal Y_{E,\rm FF},
$$

它正是 Step-5A.79 的 nonlocal kernel。因此

$$
\boxed{\texttt{OUT\_OF\_SCOPE\_LOCAL\_BV\_FERMI\_FEYNMAN\_PROPER\_SLICE}.}
$$

Wess--Zumino component fallback 也不是 current BV system 的 reduction：

$$
(\mathbf s_E\mathcal V_E^{\rm WZ})\big|
=i(\widetilde{\mathfrak c}_E\big|-\mathfrak c_E\big|),
$$

$$
D_{Ea}(\mathbf s_E\mathcal V_E^{\rm WZ})\big|=-iD_{Ea}\mathfrak c_E\big|,
\qquad
\bar D_{E\dot a}(\mathbf s_E\mathcal V_E^{\rm WZ})\big|
=i\bar D_{E\dot a}\widetilde{\mathfrak c}_E\big|.
$$

Euclidean chiral/antichiral ghosts 独立，故 WZ surface 不被 \(\mathbf s_E\) 保持：

$$
\boxed{\texttt{OUT\_OF\_SCOPE\_WZ\_BV\_REDUCTION}.}
$$

因此 WZ component triangle 与 fixed superfield representative 的 general BV equivalence 不属于 physical graph settlement：

$$
\boxed{\texttt{OUT\_OF\_SCOPE\_COMPONENT\_TO\_SUPERFIELD\_BV\_EQUIVALENCE}.}
$$

以下 source、propagator 与 cut algebra 定义 fixed physical graph representative。

Formal bilocal source 定义为

$$
S_J=\int d^4x\,
J_{AB}\,L^A(x)
\left(e^{w_{\dot a}\mathcal D_{\mathrm{adj}}^{\dot a}}L\right)^B(x),
\qquad
L:=g^{-1}\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+.
$$

Dual endpoint BRST rule 为

$$
\begin{aligned}
sJ_{AB}(x,w)={}&
-J_{CB}(x,w)\rho(c(x))^C{}_A\\
&-J_{AC}(x,w)\rho(c(x+w))^C{}_B.
\end{aligned}
$$

令

$$
X:=w_{\dot a}\partial^{\dot a},
\qquad
Y:=w_{\dot a}\operatorname{ad}_{v}^{\dot a}.
$$

则 ordered Duhamel expansion through quadratic order in g 为

$$
e^{X+gY}=e^X
+g\int_0^1ds\,e^{(1-s)X}Ye^{sX}
$$

$$
\quad
+g^2\int_0^1ds_1\int_0^{s_1}ds_2\,
e^{(1-s_1)X}Ye^{(s_1-s_2)X}Ye^{s_2X}
+O(g^3).
$$

Coincident link prescription 定义为

$$
\Theta(0)=\frac12.
$$

对于 occurrence-decorated field slot，Schwinger cut 为

$$
\mathcal C_{\mathrm{cut}}:
K_{IJ}q^J\,G^{JK}q^K_{\mathfrak o}
\longleftrightarrow
\frac{\vec\partial}{\partial q^I_{\mathfrak o}},
$$

$$
K_{IJ}G^{JK}=\delta_I{}^K,
\qquad
\mathcal C_{\mathrm{cut}}^2=1.
$$

Under DRED the superspace identity produces the four-dimensional inverse
kernel, whereas the regulated propagator is inverted by the full
$d$-dimensional kernel.  On an internal edge $e$,

$$
\bar r_e^{\,2}=r_{e,d}^{\,2}+\mu_\ell^2,
\qquad
r_e=\ell+Q_e,
\qquad
\widetilde Q_e=0,
$$

because every external momentum shift has zero evanescent component.  Hence

$$
\frac{\bar r_e^{\,2}}{r_{e,d}^{\,2}}
=1+\frac{\mu_\ell^2}{r_{e,d}^{\,2}}.
$$

The first term is exactly the Schwinger cut.  For a triangle with denominators
$D_i=r_{i,d}^2$,

$$
\begin{aligned}
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
&=\frac{\bar r_e^{\,2}-r_{e,d}^{\,2}}
{D_0D_1D_2}\\
&=\boxed{\frac{\mu_\ell^2}{D_0D_1D_2}}.
\end{aligned}
$$

Replacing $\bar r_e^{\,2}$ by $r_{e,d}^{\,2}$ before this subtraction makes
the same expression identically zero and removes the anomaly.

## 3. Tree descendants

定义 ordered Euler operators

$$
\mathscr E_V
:=\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a
-2i(\boldsymbol\Phi_s\times\widetilde{\boldsymbol\Phi}_s),
$$

$$
\mathscr E_{\widetilde r}
:=-\frac14\boldsymbol\nabla^2\boldsymbol\Phi_r
-\frac1{\sqrt2}\varepsilon_{rst}(C_s\times C_t).
$$

使用

$$
\boldsymbol\nabla^2=2\boldsymbol\nabla_-\boldsymbol\nabla_+
$$

得到

$$
\boxed{
\begin{aligned}
\boldsymbol\nabla_-A
&=-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s),\\
\boldsymbol\nabla_-B_r
&=-2\mathscr E_{\widetilde r}
-\sqrt2\varepsilon_{rst}(C_s\times C_t),\\
\boldsymbol\nabla_-C_r&=0,\\
\boldsymbol\nabla_-D_{\dot a}&=0.
\end{aligned}}
$$

每个 ordered pair 使用

$$
\boldsymbol\nabla_-(L_iL_j)
=(\boldsymbol\nabla_-L_i)L_j
+(-1)^{|L_i|}L_i(\boldsymbol\nabla_-L_j).
$$

## 4. Canonical WW seed

定义 fixed orientation 与 marked placement：

$$
\mathfrak o=(A\to\widetilde W,\ B\to W),
\qquad
\mathfrak p\in\{A,B\}.
$$

固定 \((\mathfrak o,\mathfrak p)\)。Action expansion 的两个 labelled assignments 给出

$$
w_{\mathrm{Wick}}
=\frac1{2!}(1+1)=1.
$$

Closed-loop mixed (D)-algebra weight 为

$$
w_D=\frac1{32}\cdot16\cdot2\cdot2=2.
$$

Full external-slot D-word replay 同时包含 three external placements、four action-chirality pairs、two marked source edges 与 raw Schwinger contact Hessian。Exact counts 为

$$
N_{\rm external\ slot\ check}=269,
\qquad
N_{\rm external\ slot\ failure}=0,
$$

$$
N_{\rm full\ color\ mask}=9216,
\qquad
N_{\rm sparse\ replay}=2048,
\qquad
N_{\rm equality\ failure}=0.
$$

两个 ordered cubic vertices 给出

$$
\left(+\frac{ig}{2}\right)
\left(-\frac{ig}{2}\right)
=\frac{g^2}{4}.
$$

故 loop integral 前 coefficient 为

$$
w_{\mathrm{Wick}}\frac{g^2}{4}w_D
=1\cdot\frac{g^2}{4}\cdot2
=\frac{g^2}{2}.
$$

令

$$
D_0=\ell^2,
\qquad
D_1=(\ell+p)^2,
\qquad
D_2=(\ell+p+q)^2.
$$

Feynman parameters 给出

$$
\frac1{D_0D_1D_2}
=2\int_{x,y,z\geq0}dx\,dy\,dz\,
\delta(1-x-y-z)
\frac1{(r^2+\Delta)^3},
$$

$$
\int_{x,y,z\geq0}dx\,dy\,dz\,
\delta(1-x-y-z)=\frac12.
$$

定义

$$
J_n(\Delta)
:=\mu^{2\epsilon}\int\frac{d^dr}{(2\pi)^d}
\frac1{(r^2+\Delta)^n}.
$$

Schwinger parameter integration 为

$$
J_n(\Delta)
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}{\Gamma(n)}
\Delta^{d/2-n}.
$$

因此

$$
\Delta J_3=\frac\epsilon2J_2,
\qquad
\operatorname*{Res}_{\epsilon=0}J_2=\frac1{16\pi^2}.
$$

Hatted rotational reduction 给出

$$
\begin{aligned}
\int_r\frac{r_mr_n}{(r^2+\Delta)^3}
&=\frac{\widehat\delta_{mn}}d(J_2-\Delta J_3)\\
&=\frac{\widehat\delta_{mn}}{4}J_2.
\end{aligned}
$$

所以

$$
\operatorname*{Pole}_{\epsilon=0}
\int_{\ell}\frac{L_1^mL_2^n}{D_0D_1D_2}
=\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}.
$$

令

$$
T_{m\rho n}:=\sigma_m\bar\sigma_\rho\sigma_n.
$$

Triangle pole 为

$$
\Gamma_{T,\mathfrak o,\mathfrak p}
=\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}\widehat\delta^{mn}T_{m\rho n}p^\rho.
$$

## 5. Contact rows and cutting failure

在同一 recorded arithmetic ledger 中，每个 contact row 的 sign chain 为

$$
\left(-\frac14\right)_{K}
(-1)_{\mathrm{endpoint}}
\left(\frac12\right)_{D_-D_+=D^2/2}
(2)_{\mathrm{mixed}}
(2)_{\mathrm{Wick}}
\left(-\frac12\right)_{p_+}
=-\frac14.
$$

因此单 row 为

$$
\Gamma_{C,j,\mathfrak o,\mathfrak p}
=-\frac14\cdot\frac{\hbar g^2}{2}
\cdot\frac1{16\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}\delta_4^{mn}T_{m\rho n}p^\rho
$$

$$
=-\frac{\hbar g^2}{128\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}\delta_4^{mn}T_{m\rho n}p^\rho.
$$

四个 occurrence-resolved rows 给出

$$
\Gamma_{C,\mathfrak o,\mathfrak p}
=\sum_{j=1}^{4}\Gamma_{C,j,\mathfrak o,\mathfrak p}
=-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}\delta_4^{mn}T_{m\rho n}p^\rho.
$$

于是 four-dimensional metric part exact cancel：

$$
\Gamma_{T,\mathfrak o,\mathfrak p}
+\Gamma_{C,\mathfrak o,\mathfrak p}
=-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}\breve\delta^{mn}T_{m\rho n}p^\rho.
$$

External momentum 为 hatted，因此必须先与 \(p^\rho\) contraction：

$$
p^\rho\breve\delta^{mn}\sigma_m\bar\sigma_\rho\sigma_n
=2p^\rho\breve\delta_\rho{}^n\sigma_n
-p^\rho\sigma_\rho\breve\delta^{mn}\bar\sigma_m\sigma_n
$$

$$
=0-(\breve\delta^m{}_m)p^\rho\sigma_\rho
=-2\epsilon p^\rho\sigma_\rho.
$$

故

$$
\begin{aligned}
\Gamma_{T,\mathfrak o,\mathfrak p}
+\Gamma_{C,\mathfrak o,\mathfrak p}
&=-\frac{\hbar g^2}{32\pi^2\epsilon}(-2\epsilon)
\mathbb F^{AB}{}_{DE}\sigma_\rho p^\rho\\
&=\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}\sigma_\rho p^\rho.
\end{aligned}
$$

在 fixed FF graph representative 内，WW remainder 全部来自 regulated cut 中

$$
\widehat\delta^{mn}-\delta_4^{mn}=-\breve\delta^{mn}.
$$

All physical families 的 occurrence-resolved audits 使用同一 identity

$$
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

Named nonlinear-letter/quartic/collapsed/link objects 的 universal raw-port functor table 不用于 81-row coefficient extraction，标为 `OUT_OF_SCOPE_RAW_PORT_FUNCTOR_TABLE`。

## 6. Residual q and compact kernel

Bottom-letter residual supercharges 定义为

$$
q_r:=\frac1{\sqrt2}Q^r_{E,+}.
$$

其 exact action 为

$$
q_rA=0,
\qquad
q_rB_s=-i\delta_{rs}A,
$$

$$
q_rC_s=-\frac1{\sqrt2}\varepsilon_{rst}B_t,
\qquad
q_rD_{\dot a}=-iP_{\dot a}C_r.
$$

但是

$$
q_r(A^AA^B)=0.
$$

所以 raw WW \(A>A\) seed 的 forward-\(q\) orbit 只有自身，不能生成其余 80 ordered pairs。Physical families 已分别直接计算；把全部 quantum ports、vertices、edges、sources 与 cuts 升级成一个 raw graph \(q\)-equivariant functor 是更强命题：

$$
\boxed{\texttt{OUT\_OF\_SCOPE\_RAW\_GRAPH\_Q\_EQUIVARIANT\_FUNCTOR}.}
$$

Physical compact letter 为

$$
\mathcal C_{\mathrm{phys}}(\theta)
=\theta_rC_r
+\frac1{2\sqrt2}\varepsilon_{rst}\theta_r\theta_sB_t
-\frac i{\sqrt2}\theta_1\theta_2\theta_3A.
$$

Formal jet extension 定义

$$
q_rU=C_r,
\qquad
P_{\dot a}U=iD_{\dot a},
$$

$$
\mathcal C_P(\theta)
=U+\mathcal C_{\mathrm{phys}}(\theta).
$$

Diagonal (q)-covariance 的 degree-three Grassmann kernel 满足

$$
(\partial_{\theta_r}+\partial_{\theta'_r})K(\theta,\theta')=0.
$$

Degree-three invariant space 的 matrix rank 为 (19)，domain dimension 为 (20)，故 nullity 为 (1)，并且

$$
K(\theta,\theta')
=\prod_{r=1}^{3}(\theta_r-\theta'_r).
$$

## 7. Ordered component ledger

对 multiindex

$$
\mathbf u=(u_1,u_2)\in\mathbb Z_{\geq0}^2,
$$

先定义 normalized PBW jet

$$
\mathbb J_{\mathbf u}(X)
:=\binom{u_1+u_2}{u_1}^{-1}
\sum_{w\in\operatorname{Sh}(1^{u_1},2^{u_2})}P_wX.
$$

再定义 typed contracted factor

$$
\mathfrak p_{\dot\alpha}X
:=
\begin{cases}
D_{\dot\alpha},&X=D,\\
(\mathbb J_{\mathbf u}D)_{\dot\alpha},
&X=\mathbb J_{\mathbf u}D,\\
P_{\dot\alpha}X,&X\notin
\{\mathbb J_{\mathbf u}D:\mathbf u\in\mathbb Z_{\geq0}^2\},
\end{cases}
$$

以及 ordered bilinear

$$
\langle X^D,Y^E\rangle
:=(\mathfrak p_{\dot\alpha}X^D)
(\mathfrak p^{\dot\alpha}Y^E).
$$

所有下式右端都乘同一 ordered coefficient

$$
\lambda_1\mathbb F^{AB}{}_{DE}.
$$

非零 family formulas 为

$$
\begin{aligned}
\Delta(A,A)={}&
\langle D^D,A^E\rangle-\langle A^D,D^E\rangle\\
&+\sum_{r=1}^{3}
\left(\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle\right),
\end{aligned}
$$

$$
\Delta(A,C_r)=\Delta(C_r,A)
=\langle D^D,C_r^E\rangle-\langle C_r^D,D^E\rangle,
$$

$$
\Delta(B_r,C_s)=\Delta(C_s,B_r)
=\delta_{rs}\langle D^D,D^E\rangle,
$$

$$
\Delta(B_r,B_s)
=-i\sqrt2\varepsilon_{rst}
\left(\langle D^D,C_t^E\rangle
-\langle C_t^D,D^E\rangle\right),
$$

$$
\begin{aligned}
\Delta(A,B_r)=\Delta(B_r,A)={}&
\langle B_r^D,D^E\rangle
+\langle D^D,B_r^E\rangle\\
&-i\sqrt2\varepsilon_{rst}
\langle C_s^D,C_t^E\rangle.
\end{aligned}
$$

定义

$$
\mathbf e_1=(1,0),
\qquad
\mathbf e_2=(0,1).
$$

Intrinsic-D rows 为

$$
\Delta(A,D_{\dot a})
=\frac13\langle\mathbb J_{\mathbf e_a}D^D,D^E\rangle
+\frac23\langle D^D,\mathbb J_{\mathbf e_a}D^E\rangle,
$$

$$
\Delta(D_{\dot a},A)
=\frac23\langle\mathbb J_{\mathbf e_a}D^D,D^E\rangle
+\frac13\langle D^D,\mathbb J_{\mathbf e_a}D^E\rangle.
$$

Exact-zero pairs 为

$$
(B_r,B_r),
\qquad
(B_r,C_s),(C_s,B_r)\quad(r\ne s),
$$

$$
(B,D),(C,C),(C,D),(D,B),(D,C),(D,D).
$$

上列逐 component 展开后给出 29 nonzero 与 52 zero；reversed ordering 不被 quotient。

## 8. Holomorphic jets and PBW

对任意 nonnegative integers m,n，Project ordered kernel 为

$$
\boxed{
\begin{aligned}
\mathcal K^P_{m,n}(f^D,g^E)
={}&\sum_{k=0}^{m}\sum_{\ell=0}^{n}
\frac{2\binom mk\binom n\ell}
{(m+n+2)(k+\ell+1)}\\
&\times
P_1^kP_2^\ell P_{\dot\alpha}f^D\,
P_1^{m-k}P_2^{n-\ell}P^{\dot\alpha}g^E.
\end{aligned}}
$$

Numerator factor (2) 来自

$$
\frac1{D_0D_1D_2}
=2\int_{\Delta_2}\frac1{(r^2+\Delta)^3},
$$

不是 orientation multiplicity。Examples:

$$
\mathcal K^P_{0,0}=\langle f,g\rangle,
$$

$$
\mathcal K^P_{1,0}
=\frac13\langle P_1f,g\rangle
+\frac23\langle f,P_1g\rangle,
$$

$$
\mathcal K^P_{2,0}
=\frac16\langle P_1^2f,g\rangle
+\frac12\langle P_1f,P_1g\rangle
+\frac12\langle f,P_1^2g\rangle,
$$

$$
\begin{aligned}
\mathcal K^P_{1,1}={}&
\frac16\langle P_1P_2f,g\rangle
+\frac14\langle P_1f,P_2g\rangle\\
&+\frac14\langle P_2f,P_1g\rangle
+\frac12\langle f,P_1P_2g\rangle.
\end{aligned}
$$

First-input recursion 为

$$
\Delta(P^{\mathbf u}f,P^{\mathbf v}g)
=\sum_{\mathbf r\leq\mathbf u}
(-1)^{|\mathbf r|}
\binom{\mathbf u}{\mathbf r}
P^{\mathbf u-\mathbf r}
\Delta(f,P^{\mathbf v+\mathbf r}g).
$$

Covariant derivatives 满足

$$
[P_1,P_2]=-\operatorname{ad}_A.
$$

Normalized PBW jet 定义为

$$
\boxed{
\mathbb J_{m,n}(X)
:=\binom{m+n}{m}^{-1}
\sum_{w\in\operatorname{Sh}(1^m,2^n)}P_wX.}
$$

特别地

$$
\mathbb J_{1,1}(X)
=\frac12(P_1P_2+P_2P_1)X
=P_1P_2X+\frac12\operatorname{ad}_A X.
$$

PBW map 是 filtered linear isomorphism，不是 ordinary-product algebra map。定义

$$
f\star g
:=\operatorname{PBW}^{-1}
\left(\operatorname{PBW}(f)\operatorname{PBW}(g)\right).
$$

Exact audits 给出 degree zero through four 双向 inverse、129 intertwining pairs、351 associative triples；link exponential 与 PBW shuffle 的 Taylor intertwiner through degree eight 有 47 checks 全部通过。

## 9. Finite normal-product settlement

Physical dimension 9/2 odd SU(3)-singlet residual-q kernel 为 one-dimensional：

$$
\boxed{
\mathscr Z^{DE}
=\langle D^D,A^E\rangle-\langle A^D,D^E\rangle
+\sum_{r=1}^{3}
\left(\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle\right).}
$$

其 unique triplet primitive 为

$$
\boxed{
\mathscr Y_r^{DE}
=\langle D^D,B_r^E\rangle
+\langle B_r^D,D^E\rangle
-i\sqrt2\varepsilon_{rst}\langle C_s^D,C_t^E\rangle,}
$$

$$
q_s\mathscr Y_r=i\delta_{sr}\mathscr Z.
$$

对 \(AB_1/B_1A\) 使用 common ordered basis

$$
(D>B_1,\ B_1>D,\ C_2>C_3,\ C_3>C_2).
$$

Raw graph carriers 的 two quotient maps 为

$$
G_1:(2,2)_{(X,E)}\longmapsto(0,2)_{(X,T)},
\qquad
T_{DB}=X_{DB}+E_{DB},
$$

$$
G_2:\left(-\frac13,\frac43\right)_{(X,E)}
\longmapsto\left(1,\frac43\right)_{(X,T)},
\qquad
T_{BD}=-X_{BD}+E_{BD}.
$$

因此 common total-derivative layer 为

$$
\boxed{v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).}
$$

Gate 13 的 hybrid vector

$$
v_{\rm hybrid}=(2,1,-2i\sqrt2,+2i\sqrt2)
$$

不是 common quotient。First false equality 是

$$
\pi_{G_1,\mathrm{EOM}}(2,2)=2
\quad\text{被识别为}\quad
\pi_{G_1,\mathrm{TD}}(2,2)=0.
$$

Residual Ward matrix 与 kernel 为

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
\qquad
\ker M_q=\mathbb C k_q,
$$

$$
k_q=(1,1,-i\sqrt2,+i\sqrt2).
$$

Bare common-TD residual 为

$$
M_qv_{\rm TD}=(-1,-2i\sqrt2,+2i\sqrt2)^T.
$$

Missing vector-frame graph 的 ordered \(CC\) support 为零；若错误地把 finite completion 限制为 graph support，则得到 \(2k_q\)。Finite composite-source normal product 不受这一 topology restriction。由

$$
\Delta(A,A)=\mathscr Z,
\qquad
q_s\mathscr Y_r=i\delta_{sr}\mathscr Z
$$

固定 kernel ray 的 scale 为 one。Unique finite shift 与 renormalized vector 为

$$
\boxed{
\delta v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2),
\qquad
v_{\rm ren}=v_{\rm TD}+\delta v_{\rm fin}
=(1,1,-i\sqrt2,+i\sqrt2)=k_q.}
$$

直接乘法给出

$$
\boxed{M_qv_{\rm ren}=0.}
$$

对应 finite normal-product term 为

$$
\boxed{
\delta_{\rm fin}\Gamma_{AB_1}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\langle D^D,B_1^E\rangle
+i\sqrt2\langle C_2^D,C_3^E\rangle
-i\sqrt2\langle C_3^D,C_2^E\rangle
\right].}
$$

这是 finite scheme term，不是额外 anomaly graph；所有 bare graph anomaly 仍只来自 \(\mu_\ell^2\) cutting failure。GPT Pro Gate 14 独立复核了 two quotient maps、Gate 13 的 first false equality、AA scale-one condition 与 \(M_qv_{\rm ren}=0\)。

### 9.1 Broader evanescent/BV theorem: `OUT_OF_SCOPE`

在 physical/evanescent MS basis 中，general one-loop mixing 为

$$
\begin{pmatrix}O^0\\E^0\end{pmatrix}
=\left[
\mathbf1+\frac{\hbar g^2}{16\pi^2\epsilon}
\begin{pmatrix}
z_{OO}&z_{OE}\\
z_{EO}&z_{EE}
\end{pmatrix}
\right]
\begin{pmatrix}O^R\\E^R\end{pmatrix}.
$$

Trivial evanescent row \(E_{\mathrm{triv}}=2\epsilon\mathscr Z\) 显示 four-dimensional finiteness 或 residual-\(q\) covariance 本身不能推出 \(z_{EO}=0\)。

定义

$$
P=P_h+P_b,
\qquad
A=A_{hh}+A_{hb}+A_{bb},
$$

$$
(P_hX)_{\dot a}:=(\sigma_E^m)_{+\dot a}\widehat\delta_m{}^n\mathcal D_nX,
\qquad
(P_bX)_{\dot a}:=(\sigma_E^m)_{+\dot a}\breve\delta_m{}^n\mathcal D_nX.
$$

$$
A_{hb}:=-i(\sigma_E^{mn})_{++}
(\widehat\delta_m{}^p\breve\delta_n{}^q+\breve\delta_m{}^p\widehat\delta_n{}^q)F_{pq},
$$

$$
A_{bb}:=-i(\sigma_E^{mn})_{++}
\breve\delta_m{}^p\breve\delta_n{}^qF_{pq}.
$$

为避免与 Section 7 的 \(\langle X,Y\rangle\) 再微分记号混淆，projector rows 直接定义为 raw slots：

$$
\mathscr E_{DA(x,y)}^{DE}
:=D_{\dot a}^D(P_x^{\dot a}A_y)^E
-(P_{x,\dot a}A_y)^D D^{E,\dot a},
$$

$$
\mathscr E_{BC(x,y)}^{DE}
:=\sum_{r=1}^{3}\left[
(P_{x,\dot a}B_r^D)(P_y^{\dot a}C_r^E)
-(P_{x,\dot a}C_r^D)(P_y^{\dot a}B_r^E)
\right].
$$

Physical cocycle 的 Cartesian projector expansion 给出五个 \(DA\) genuine rows

$$
(h,hb),\ (h,bb),\ (b,hh),\ (b,hb),\ (b,bb),
$$

以及三个 \(BC\) genuine rows

$$
(b,h),\ (h,b),\ (b,b).
$$

这八项只证明 \(\mathscr Z\) 的 hat/breve expansion；它们尚未 exhaust complete local BV/source evanescent module。

令 \(\chi_i:=A_{\breve i}\) 与

$$
\Sigma^{ij}:=(\sigma_E^{mn})_{++}\breve\delta_m{}^i\breve\delta_n{}^j.
$$

Double-breve source Hessian 为

$$
\frac{\delta^2A_{bb}^E}{\delta\chi_i^M\delta\chi_j^N}
=-2i\Sigma^{ij}c_{MN}{}^E.
$$

The \(A_{\widehat\mu}\chi_k\chi_l\) vertex carries \(\delta_{kl}\)。Direct、exchange 与 tadpole species contractions 都给出

$$
\Sigma^{ij}\delta_{ik}\delta_{jl}\delta_{kl}
=\Sigma^{ij}\delta_{ij}=0,
$$

$$
\Sigma^{ij}\delta_{il}\delta_{jk}\delta_{kl}
=\Sigma^{ij}\delta_{ij}=0.
$$

因此只对已枚举的 \(\chi\) tadpole 与 \(A_{\widehat\mu}\chi\chi\) direct/exchange classes，

$$
\left.\Pi_{\rm phys}\Gamma_{\mathscr E_{DA(h,bb)}}^{(1)}
\right|_{\rm enumerated\ \delta_{ij}\ classes}=0.
$$

这不推出完整的 \(\Pi_{\rm phys}\Gamma_{\mathscr E_{DA(h,bb)}}^{(1)}=0\)。所有 compatible source Hessians 与 G1--G4 vertex/edge words 的 general theorem 标为 `OUT_OF_SCOPE_COMPLETE_BV_DRED_EVANESCENT_MODULE`。

Mixed row \(\mathscr E_{DA(h,hb)}\) 的 ordered source Hessian 非零：

$$
J_{MN}^{DE}:=\delta_M^D\delta_N^E,
\qquad
I_{D^M_{\dot a},\chi_i^N}^{[0],DE}
=2i(J_{MN}^{DE}-J_{NM}^{DE})(\sigma_h^\nu)_{+\dot a}
(\sigma^{\widehat\mu i})_{++}p_\nu p_\mu.
$$

若 regulator rules 保持 \(O(N_\epsilon)\) covariance、species kernels 无 \(N_\epsilon^{-1}\)、UV/IR 已分离且 one-loop primitive 只有 simple UV pole，则每个 independent tensor/integral structure \(\alpha\) 可写为

$$
N_\epsilon=2\epsilon,
\qquad
\Pi_{\rm phys}\Gamma_{\mathscr E_u}^{(1)}
=\sum_\alpha P_{u\alpha}(N_\epsilon)I_{u\alpha}^{(1)},
\qquad
P_{u\alpha}(0)=0,
$$

$$
I_{u\alpha}^{(1)}
=\frac{r_{u\alpha,-1}}\epsilon+r_{u\alpha,0}+O(\epsilon),
\qquad
P_{u\alpha}(2\epsilon)
=2\epsilon P'_{u\alpha}(0)+O(\epsilon^2).
$$

在这些 explicitly `OUT_OF_SCOPE` assumptions 下，formal lemma 为

$$
\operatorname{Res}_{1/\epsilon}
\sum_\alpha P_{u\alpha}(2\epsilon)I_{u\alpha}^{(1)}=0,
\qquad
z_{E_uO}^{\rm MS}=0,
$$

$$
\operatorname{Fin}_{\epsilon^0}
\sum_\alpha P_{u\alpha}(2\epsilon)I_{u\alpha}^{(1)}
=2\sum_\alpha P'_{u\alpha}(0)r_{u\alpha,-1}.
$$

MS pole mixing 与 finite physical anomaly 必须区分。General BV source basis、all-regulator UV/IR separation 与 arbitrary mixed primitive theorem 标为

$$
\boxed{\texttt{OUT\_OF\_SCOPE\_GENERAL\_BV\_MIXED\_PRIMITIVE\_THEOREM}.}
$$

同一个 source/graph `origin_id` 内，no-double-count projector identity 为

$$
r\widehat\delta^{mn}T_{mn}-r\delta_4^{mn}T_{mn}
=-r\breve\delta^{mn}T_{mn}.
$$

General mixed-source graphs 与 WW complement 的 source-derived multiset bijection 也标为 `OUT_OF_SCOPE_GENERAL_BV_NO_DOUBLE_COUNT_THEOREM`。这些 stronger claims 不改变 Section 7 的 physical 81-row settlement。

## 10. Holomorphic-twist corrected round-trip

Physical comparison dictionary 为

$$
c\longleftrightarrow U,
\qquad
\gamma^r\longleftrightarrow C_r,
\qquad
\beta_r\longleftrightarrow\frac1{\sqrt2}B_r,
$$

$$
b\longleftrightarrow-\frac i{\sqrt2}A,
\qquad
\partial_{\dot a}c\longleftrightarrow iD_{\dot a},
\qquad
Q_{0,\mathrm{HT}}\longleftrightarrow-\frac12\boldsymbol\nabla_-.
$$

Project 81-row ledger 在读取 HT artifact 前已 canonicalize 并 seal：

$$
\boxed{
H_P=
\texttt{ec77327d838a45fc139ca90e73ec187c2df6d6f3b5f5318f1587d12a41b3016d}.}
$$

逐 ordered physical pair 比较 Project ledger word、independent physical expansion 与 translated HT word，得到

$$
N_{\mathrm{physical\ pairs}}=81,
\qquad
N_{\mathrm{direct\ three\ way\ match}}=81,
\qquad
N_{\mathrm{mismatch}}=0,
$$

$$
81=29_{\mathrm{nonzero}}+52_{\mathrm{zero}}.
$$

对

$$
m,n\in\mathbb Z_{\ge0},
\qquad
0\le k\le m,
\qquad
0\le\ell\le n,
$$

printed HT 与 Project coefficients 分别为

$$
T^{\mathrm{HT,printed}}_{m,n;k,\ell}
=\frac{\binom mk\binom n\ell}
{(m+n+2)(k+\ell+1)},
$$

$$
K^P_{m,n;k,\ell}
=\frac{2\binom mk\binom n\ell}
{(m+n+2)(k+\ell+1)}.
$$

定义 corrected HT coefficient

$$
T^{\mathrm{HT,corr}}_{m,n;k,\ell}
:=2T^{\mathrm{HT,printed}}_{m,n;k,\ell}.
$$

因

$$
m+n+2\ge2,
\qquad
k+\ell+1\ge1,
$$

逐 coefficient exact equality 为

$$
\boxed{
K^P_{m,n;k,\ell}
=T^{\mathrm{HT,corr}}_{m,n;k,\ell}
=2T^{\mathrm{HT,printed}}_{m,n;k,\ell}}
$$

对全部 allowed \(m,n,k,\ell\) 成立。Finite independent rectangle check 为

$$
0\le m\le8,
\qquad
0\le n\le8,
\qquad
N_{\mathrm{coefficient\ check}}=2025,
\qquad
N_{\mathrm{mismatch}}=0.
$$

因此 corrected holomorphic-twist result 与完整 physical 81-row PBW jet tower exact match。Printed derivative kernel 缺少的 factor \(2\) 来自 Project triangle Feynman-parameter identity

$$
\frac1{D_0D_1D_2}
=2\int_{\Delta_2}\frac1{(r^2+\Delta)^3},
$$

不是第二个 loop orientation。

Absolute formal \(U/Q_0\) intertwiner、general color-frame inverse、general trace normalization 与原始 HT source 的 editorial provenance 标为

$$
\boxed{
\texttt{OUT\_OF\_SCOPE\_FORMAL\_U\_Q0\_COLOR\_AND\_SOURCE\_PROVENANCE}.}
$$

它们不进入 sealed physical coefficient/output-word equality。

## 11. Machine gates

Physical acceptance gates:

$$
81/81\ \text{ordered pairs COMPLETE\_EXACT},
\qquad
29\ \text{EXACT\_NONZERO},
\qquad
52\ \text{EXACT\_ZERO},
$$

$$
81/81\ \text{direct HT output-word matches},
\qquad
0\ \text{HT mismatch},
\qquad
2025/2025\ \text{finite jet-kernel checks},
$$

$$
31/31\ \text{AB/BA finite Project-Ward checks},
\qquad
269/269\ \text{AA external-slot checks},
$$

$$
N_{\rm AA\ full\ color\ mask}=9216,
\qquad
N_{\rm AA\ sparse\ replay}=2048,
\qquad
N_{\rm AA\ equality\ failure}=0.
$$

Acceptance evidence:

`audits/step5-global-81-target-blind-orbit-ledger.json`,
`audits/step5_global_81_ht_symbolic_roundtrip_exact.json`,
`audits/step5-ab-ba-project-ward-finite-renormalization-exact.json`,
`audits/step5-aa-external-slot-decomposition-exact.json`.

The obsolete `step5-ab-ba-full-1pi-quotient` artifact is historical and is not acceptance evidence.

Broader claims retained outside the physical acceptance scope:

$$
\texttt{OUT\_OF\_SCOPE\_RAW\_GRAPH\_Q\_EQUIVARIANT\_FUNCTOR},
\qquad
\texttt{OUT\_OF\_SCOPE\_GENERAL\_BV\_WZ\_REDUCTION},
$$

$$
\texttt{OUT\_OF\_SCOPE\_OPEN\_COLOR\_SOURCE\_BV\_EXTENSION},
\qquad
\texttt{OUT\_OF\_SCOPE\_COMPLETE\_BV\_DRED\_EVANESCENT\_MODULE},
$$

$$
\texttt{OUT\_OF\_SCOPE\_GENERAL\_DRED\_EPSILON\_TENSOR\_THEOREM},
\qquad
\texttt{OUT\_OF\_SCOPE\_GENERAL\_BV\_MOMENTUM\_LEDGER},
$$

$$
\texttt{OUT\_OF\_SCOPE\_FORMAL\_U\_Q0\_ABSOLUTE\_INTERTWINER},
\qquad
\texttt{OUT\_OF\_SCOPE\_GENERAL\_REDUCTIVE\_COLOR\_FRAME}.
$$
