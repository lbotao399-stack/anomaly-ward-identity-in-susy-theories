# GPT Pro ordered-AA standard-Feynman calculation — 2026-07-14

Status: `NON_AUTHORITY_PRO_REVIEW`.

Chat: https://chatgpt.com/c/6a563e16-0d68-83e8-aaef-928c89fe0b6b

Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-aa-pair-standard-feynman/initial-prompt.md`

Prompt SHA-256: `48314dda34aaba5c2afd433c3dc2e31b5f8fd8f41e3266fef7f4659dd2531977`.

Elapsed: `35m57s`.

The following is the completed visible response exported from the rendered DOM, with TeX recovered from the page's MathML annotations. Interface labels such as `Pasted text` are retained.

## 1. `Notation and chosen gauge/regulator`

计算对象仅为 ordered pair $A^AA^B$ 的 $G$-triangle 与三个 $M_r$-triangles；anomaly 定义为 DRED 中 $d$-dimensional loop projector 与 four-dimensional cut projector 之差。Pasted text

### Notation

$$
P_{\dot\alpha}:=\sigma^m_{+\dot\alpha}\partial_m,
\qquad
D_{\dot\alpha}:=P_{\dot\alpha}U.
$$

$$
\operatorname{PP}_{\epsilon=0}F(\epsilon)
:=F(\epsilon)\text{ 的全部 }1/\epsilon\text{ pole}.
$$

$$
\Delta_2
:=\{(x,y,z)\in\mathbb R_{\geq0}^3\mid x+y+z=1\},
\qquad
\int_{\Delta_2}:=\int_0^1dy\int_0^{1-y}dz,
$$

$$
\int_{\Delta_2}1=\frac12.
$$

$\Pi_A,\Pi_D,\Pi_{B_r},\Pi_{C_r}$ denote the component/letter projectors converting background superfields into the Project letters $A,D,B_r,C_r$. These projectors, including their phases and parities, are not specified in the supplied conventions. Their only unresolved one-loop trace is denoted by $\chi_M$ below.

### Canonical quantum fields

I choose

$$
V=\sqrt2\,g\,v,
\qquad
\Phi_r=g\,\varphi_r,
\qquad
\widetilde\Phi_r=g\,\widetilde\varphi_r .
$$

Hence

$$
\langle v^A(p,1)v^B(-p,2)\rangle
=
-\frac{\hbar\kappa^{AB}}{p^2}\,
\delta^4(\theta_1-\theta_2),
$$

$$
\langle\phi_r^A(p,1)\widetilde\phi_s^B(-p,2)\rangle
=
\delta_{rs}\frac{\hbar\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_1-\theta_2),
$$

$$
\langle\widetilde\phi_r^A(p,1)\phi_s^B(-p,2)\rangle
=
\delta_{rs}\frac{\hbar\kappa^{AB}}{16p^2}
D_1^2\bar D_1^2\delta^4(\theta_1-\theta_2).
$$

These follow directly from the supplied unrescaled propagators.Pasted text

Define

$$
K_+:=-\frac14D_+\bar D^2D_+.
$$

From

$$
W_+^{(1)}
=-\frac18\bar D^2D_+V,
$$

one obtains

$$
A_{(1)}^A
=
-\frac18D_+\bar D^2D_+V^A
=
\frac{g}{\sqrt2}K_+v^A.
$$

It is convenient to calculate with

$$
X^A:=\frac{\sqrt2}{g}A^A,
\qquad
X_{(1)}^A=K_+v^A.
$$

All final bilinears are converted back consistently; one must not rescale the insertion without rescaling the output letters.

### Gauge vertices

I adopt the conditional Fermi–Feynman branch

$$
\mathscr V_{\widetilde W}
=
+\frac{ig}{2\hbar}
c_{UCD}\widetilde W^D_{\dot\gamma}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}),
$$

$$
\mathscr V_W
=
-\frac{ig}{2\hbar}
c_{VC'E}W^{E\gamma}
(D_{C'\gamma}-D_{V\gamma}).
$$

The factor $1/\hbar$ means these are perturbative insertions in $e^{-S/\hbar}$, not terms in $S$.

### Matter vertices

Write

$$
\varphi_r=\varphi_{r,\mathrm b}+\phi_r,
\qquad
\widetilde\varphi_r
=\widetilde\varphi_{r,\mathrm b}+\widetilde\phi_r.
$$

Since

$$
\kappa_{AB}(T_M)^B{}_C
=i\,c_{MCA},
$$

the mixed background–quantum terms are

$$
S_{M,\mathrm{mix}}
=
-i\sqrt2\,g
\sum_r\int d^8z\,
c_{MCA}
\left(
\widetilde\varphi_{r,\mathrm b}^{A}v^M\phi_r^C
+
\widetilde\phi_r^A v^M\varphi_{r,\mathrm b}^{C}
\right).
$$

Thus

$$
\mathscr V_{\widetilde\varphi v\phi}
=
+\frac{i\sqrt2g}{\hbar}c_{MCA},
\qquad
\mathscr V_{\widetilde\phi v\varphi}
=
+\frac{i\sqrt2g}{\hbar}c_{MCA}.
$$

### Fourier and DRED

$$
X(x)=\int\frac{d^dp}{(2\pi)^d}e^{ipx}X(p),
\qquad
\partial_m\longmapsto ip_m,
$$

$$
d=4-2\epsilon,
\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},
$$

$$
\widehat\delta^m{}_m=d,
\qquad
\breve\delta^m{}_m=2\epsilon,
\qquad
\ell^m=\widehat\delta^m{}_n\ell^n,
\qquad
\breve\delta^m{}_n\ell^n=0.
$$

This standard DRED separation is used only as regulator kinematics; it does not fix any Project-specific vertex sign. [arXiv](https://arxiv.org/abs/0710.2490)

---

## 2. `Insertion expansion and graph census`

From

$$
\Gamma_a
=
D_aV+\frac12[(D_aV),V]+O(V^3),
$$

one obtains

$$
W_a^{(1)}
=
-\frac18\bar D^2D_aV,
$$

$$
W_a^{(2)}
=
-\frac1{16}\bar D^2[(D_aV),V].
$$

Taking $\nabla_aY=D_aY+[\Gamma_a,Y]$,

$$
A^{(1)}
=
-\frac18D_+\bar D^2D_+V,
$$

$$
A^{(2)}
=
-\frac1{16}D_+\bar D^2[(D_+V),V]
-\frac18[D_+V,\bar D^2D_+V].
$$

For vanishing insertion-side background,

$$
\nabla_-(A^AA^B)
=
D_-\!\left(A_{(1)}^AA_{(1)}^B\right)
+O(v^3).
$$

Indeed,

$$
D_-(A_{(2)}A_{(1)})=O(v^3),
$$

$$
[\Gamma_-^{(1)},A_{(1)}A_{(1)}]=O(v^3).
$$

Therefore

$$
I_{(2),X}^{AB}
=
(D_-K_+v^A)(K_+v^B)
+
(K_+v^A)(D_-K_+v^B).
$$

Using $D_-D_+=\frac12D^2$,

$$
D_-K_+
=
-\frac18D^2\bar D^2D_+.
$$

### One-loop graph census

| Sector | Triangle | Required contact/cut graphs |
| --- | --- | --- |
| $G$ | insertion $v^Av^B$, one $\widetilde Wvv$, one $Wvv$ | four endpoint cuts from $(\bar D_C-\bar D_U)(D_{C'}-D_V)$ |
| $M_r$ | insertion $v^Av^B$, two $\widetilde\varphi v\varphi$ vertices | cuts of either $v$-line, cut of the matter line, and the $n=2$ seagull $\widetilde\varphi v^2\varphi$ |
| Ghost | none in the stated vertex grammar | none |
| Gauge-fixing | chosen Fermi–Feynman gauge-fixing is quadratic | none |
| Nielsen–Kallosh | no external $W,\widetilde W,\Phi,\widetilde\Phi$ vertex in the chosen branch | none |
| Nonlinear letter | insertion begins at $v^3$ | either two-loop or contains a scaleless tadpole |
| Ordinary counterterm | common $d$- and $4$-projector pole | cancels from the difference |
| Evanescent counterterm | not specified | set to zero in the minimal-DRED branch |

For $A_{(2)}A_{(1)}$, connecting three insertion legs to one cubic interaction produces

$$
L=I-V+1=3-2+1=2
$$

loops, counting the composite insertion as a vertex. Contracting two legs and closing the third at the insertion gives a massless tadpole, which is zero in DRED.

---

## 3. `G sector`

### Routing and Wick contractions

Take external momenta $q$ at the $\widetilde W^D$-vertex and $p$ at the $W^E$-vertex:

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+p+q.
$$

$$
D_0D_1D_2
=
k^2(k+q)^2(k+p+q)^2.
$$

The first labeled contraction is

$$
\langle v_0^A v_1^U\rangle
\langle v_0^B v_2^V\rangle
\langle v_1^C v_2^{C'}\rangle .
$$

Its color factor is

$$
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

The exchanged labeling of the two interaction vertices gives the same expression after relabeling dummy indices. Hence

$$
w_{\rm Wick}
=
\frac1{2!}(1+1)=1.
$$

Define

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.
$$

### Noncommutative D-word

For the first $D_-$-placement, the insertion contributes

$$
\left(-\frac18D^2\bar D^2D_+\right)
\left(-\frac14D_+\bar D^2D_+\right),
$$

hence the scalar coefficient

$$
\frac1{32}.
$$

The four endpoint terms are:

| endpoint term | vertex sign | transfer-to-oriented-loop sign | product |
| --- | --- | --- | --- |
| $\bar D_C D_{C'}$ | $+1$ | $+1$ | $+1$ |
| $-\bar D_C D_V$ | $-1$ | $-1$ | $+1$ |
| $-\bar D_U D_{C'}$ | $-1$ | $-1$ | $+1$ |
| $+\bar D_U D_V$ | $+1$ | $+1$ | $+1$ |

The closed $\theta$-chain gives

$$
D^2\bar D^2\delta^4(\theta)\big|_{\theta=0}
=
(-4)(-4)=16.
$$

Moving the final odd derivative into the common oriented D-word contributes one minus sign. Therefore

$$
\mathscr W_G\big|_{\log}
=
-\frac1{32}(16)(2)(2)\,N_{+\dot\alpha}
=
-2N_{+\dot\alpha}.
$$

The three momentum-producing anticommutators give

$$
N_{+\dot\alpha}
=
(r_0+r_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_1+r_2)_{\gamma\dot\alpha}.
$$

Equivalently,

$$
N_{+\dot\alpha}
=
T_{m\rho n,+}{}^{\dot\alpha}
L_1^mp^\rho L_2^n,
$$

where

$$
T_{m\rho n}
=
\sigma_m\bar\sigma_\rho\sigma_n,
$$

$$
L_1=2k+q,
\qquad
L_2=2k+p+2q.
$$

### Overall sign and coefficient

The product of the perturbative factors is

$$
\left(\frac{ig}{2\hbar}\right)
\left(-\frac{ig}{2\hbar}\right)
=
\frac{g^2}{4\hbar^2}.
$$

The three vector propagators give

$$
(-\hbar)^3=-\hbar^3.
$$

Including the D-word,

$$
\frac{g^2}{4\hbar^2}
(-\hbar^3)(-2)
=
\frac{\hbar g^2}{2}.
$$

Thus the unintegrated triangle is

$$
\Gamma_{T,G}
=
\frac{\hbar g^2}{2}
\mathbb F^{AB}{}_{DE}
T_{m\rho n}p^\rho
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}.
$$

### Feynman parameters and loop shift

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}
\frac1{[xD_0+yD_1+zD_2]^3}.
$$

Since $x=1-y-z$,

$$
xD_0+yD_1+zD_2
=
\ell^2+\Delta,
$$

with

$$
\ell=k+yq+z(p+q),
$$

$$
\Delta
=
xy\,q^2+xz\,(p+q)^2+yz\,p^2.
$$

Furthermore,

$$
L_1
=
2\ell-2zp+(x-y-z)q,
$$

$$
L_2
=
2\ell+(1-2z)p+2xq.
$$

Therefore

$$
L_1^mL_2^n
=
4\ell^m\ell^n
+
2\ell^m[(1-2z)p+2xq]^n
$$

$$
\qquad
+
2[-2zp+(x-y-z)q]^m\ell^n
$$

$$
\qquad
+
[-2zp+(x-y-z)q]^m
[(1-2z)p+2xq]^n.
$$

The second and third terms are odd in $\ell$. The fourth term has no logarithmic UV pole. Hence

$$
\operatorname{PP}
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}
=
8\int_{\Delta_2}
\operatorname{PP}
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}.
$$

Now

$$
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=
\frac{\widehat\delta^{mn}}{d}
\int_\ell
\frac{\ell^2}{(\ell^2+\Delta)^3},
$$

and

$$
\frac{\ell^2}{(\ell^2+\Delta)^3}
=
\frac1{(\ell^2+\Delta)^2}
-
\frac{\Delta}{(\ell^2+\Delta)^3}.
$$

Only the first term has a pole:

$$
\operatorname{PP}
\int_\ell\frac1{(\ell^2+\Delta)^2}
=
\frac1{16\pi^2\epsilon}.
$$

Therefore

$$
\operatorname{PP}
\int_\ell
\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=
\frac{\widehat\delta^{mn}}{64\pi^2\epsilon}.
$$

Using $\int_{\Delta_2}1=\frac12$,

$$
\operatorname{PP}
\int_k
\frac{L_1^mL_2^n}{D_0D_1D_2}
=
8\left(\frac12\right)
\frac{\widehat\delta^{mn}}{64\pi^2\epsilon}
=
\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}.
$$

Thus

$$
\boxed{
\Gamma_{T,G}
=
+\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\widehat\delta^{mn}
T_{m\rho n}p^\rho
}.
$$

### Four cut/contact rows

For a cut graph,

$$
B(P)
=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{\ell^2(\ell+P)^2}.
$$

Using

$$
\frac1{\ell^2(\ell+P)^2}
=
\int_0^1da\,
\frac1{[(\ell+aP)^2+a(1-a)P^2]^2},
$$

one obtains

$$
\operatorname{PP}B(P)=\frac1{16\pi^2\epsilon}.
$$

Each endpoint row contributes

$$
-\frac{\hbar g^2}{128\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}T_{m\rho n}p^\rho.
$$

Summing four rows,

$$
\boxed{
\Gamma_{C,G}
=
-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}T_{m\rho n}p^\rho
}.
$$

### Evanescent remainder

$$
\Gamma_{T,G}+\Gamma_{C,G}
=
-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\breve\delta^{mn}T_{m\rho n}p^\rho.
$$

Use

$$
\sigma_m\bar\sigma_\rho\sigma_n
+
\sigma_n\bar\sigma_\rho\sigma_m
=
2\delta_{m\rho}\sigma_n
+
2\delta_{n\rho}\sigma_m
-
2\delta_{mn}\sigma_\rho.
$$

Because $\breve\delta^{mn}$ is symmetric,

$$
\breve\delta^{mn}T_{m\rho n}
=
2\breve\delta_\rho{}^n\sigma_n
-
\breve\delta^m{}_m\sigma_\rho.
$$

For a physical external momentum $p^\rho$,

$$
\breve\delta_\rho{}^np^\rho=0,
\qquad
\breve\delta^m{}_m=2\epsilon.
$$

Hence

$$
\breve\delta^{mn}T_{m\rho n}p^\rho
=
-2\epsilon\,\sigma_\rho p^\rho.
$$

Therefore

$$
\boxed{
\Gamma_{\mathrm{defect},G}
=
+\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\sigma_\rho p^\rho
}.
$$

This reproduces the conditional pure-gauge candidate without using the HT answer.Pasted text

After including the exchanged orientation and the two $D_-$-placements,

$$
\boxed{
\mathcal A_G^{AB}
=
\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^D(P^{\dot\alpha}A)^E
-
(P_{\dot\alpha}A)^D D^{E\dot\alpha}
\right].
}
$$

The last component identification uses the chosen Project projection branch.

---

## 4. `M sector`

Fix one flavor $r$.

### Internal lines and arrows

For the orientation

$\widetilde\varphi_{r,\mathrm b}^D\to\varphi_{r,\mathrm b}^E$,

$$
v_0^A
\longleftrightarrow
v_1^U
\quad(r_0),
$$

$$
\phi_{r,1}^{C}
\longrightarrow
\widetilde\phi_{r,2}^{C'}
\quad(r_1),
$$

$$
v_2^V
\longleftrightarrow
v_0^B
\quad(r_2).
$$

The reversed orientation contains

$$
\widetilde\phi_{r,1}^{C}
\longrightarrow
\phi_{r,2}^{C'}
$$

and the projector $D^2\bar D^2/16$.

### Wick, flavor, and color

The forward contraction is

$$
\langle v_0^A v_1^U\rangle
\langle\phi_{r,1}^{C}
\widetilde\phi_{s,2}^{C'}\rangle
\langle v_0^B v_2^V\rangle .
$$

The matter propagator gives

$$
\delta_{rs}\kappa^{CC'}.
$$

Hence the loop is flavor diagonal:

$$
s=r.
$$

The vertex containing external $\widetilde\varphi^D$ has color

$$
c_{UCD}.
$$

The vertex containing external $\varphi^E$ has color

$$
c_{VEC'}=-c_{VC'E}.
$$

Its two perturbative vertex factors multiply to

$$
\left(+\frac{i\sqrt2g}{\hbar}c_{UCD}\right)
\left(+\frac{i\sqrt2g}{\hbar}c_{VEC'}\right)
$$

$$
=
-\frac{2g^2}{\hbar^2}
c_{UCD}c_{VEC'}
=
+\frac{2g^2}{\hbar^2}
c_{UCD}c_{VC'E}.
$$

Thus the color factor is again

$$
\mathbb F^{AB}{}_{DE}.
$$

The two interaction vertices are labeled. Their exchange cancels $1/2!$:

$$
w_{\rm Wick,M}
=
\frac1{2!}(1+1)=1.
$$

The chiral superfields are Grassmann-even integration variables. Therefore there is no independent closed-fermion-loop minus sign. Component-fermion signs are contained in the superspace D-algebra.

The two vector propagators and one matter propagator give

$$
(-\hbar)^2(+\hbar)=+\hbar^3.
$$

Consequently the prefactor before D-algebra is

$$
\frac{2g^2}{\hbar^2}\hbar^3
=
2\hbar g^2.
$$

### Complete superspace D-words

Let

$$
\Delta_{ij}:=\delta^4(\theta_i-\theta_j).
$$

For the forward arrow,

$$
\mathfrak D_{\rightarrow}^{DE}
=
\frac1{512}
\Pi_{B_r^DC_r^E}
\int d^4\theta_1d^4\theta_2
$$

$$
\quad\times
\left[
D_0^2\bar D_0^2D_{0+}\Delta_{01}
\right]
\left[
D_{0+}\bar D_0^2D_{0+}\Delta_{02}
\right]
$$

$$
\quad\times
\widetilde\varphi_{r,\mathrm b}^{D}(1)
\left[
\bar D_1^2D_1^2\Delta_{12}
\right]
\varphi_{r,\mathrm b}^{E}(2).
$$

The factor is

$$
\frac1{512}
=
\left(\frac18\right)
\left(\frac14\right)
\left(\frac1{16}\right).
$$

For the reversed arrow,

$$
\mathfrak D_{\leftarrow}^{DE}
=
\frac1{512}
\Pi_{C_r^DB_r^E}
\int d^4\theta_1d^4\theta_2
$$

$$
\quad\times
\left[
D_0^2\bar D_0^2D_{0+}\Delta_{01}
\right]
\left[
D_{0+}\bar D_0^2D_{0+}\Delta_{02}
\right]
$$

$$
\quad\times
\varphi_{r,\mathrm b}^{D}(1)
\left[
D_1^2\bar D_1^2\Delta_{12}
\right]
\widetilde\varphi_{r,\mathrm b}^{E}(2).
$$

Before integration, divide the D-algebra numerator by the propagator ideal

$$
\mathcal I_{\rm cut}
=
\langle D_0,D_1,D_2\rangle,
\qquad
D_i=r_i^2.
$$

Thus

$$
N_{M,\rightarrow}
=
N_{M,\rightarrow}^{\rm irr}
+
D_0C_0+D_1C_1+D_2C_2.
$$

The $D_iC_i$ are precisely the three cut contributions. The irreducible triangle numerator has the unique logarithmically divergent decomposition

$$
N_{M,\rightarrow}^{\rm irr}
=
L_1^mL_2^n
\mathcal R^{\rightarrow}_{mn}[B_r^D,C_r^E]
+
L_1^m\mathcal R_m
+
L_2^n\widetilde{\mathcal R}_n
+
\mathcal R_0.
$$

The last three terms have zero pole. Therefore

$$
\operatorname{PP}
\int_k
\frac{N_{M,\rightarrow}^{\rm irr}}
{D_0D_1D_2}
=
\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}
\mathcal R^{\rightarrow}_{mn}.
$$

The forward triangle is

$$
\boxed{
\Gamma_{T,M_r}^{\rightarrow}
=
\frac{\hbar g^2}{8\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\widehat\delta^{mn}
\mathcal R^{\rightarrow}_{mn}[B_r^D,C_r^E].
}
$$

The reverse triangle has the analogous expression with

$\mathcal R^{\leftarrow}_{mn}[C_r^D,B_r^E]$.

### Matter seagull/contact graph

The $n=2$ action is

$$
S_{M,n=2}
=
-g^2
\sum_r\int d^8z\,
\kappa_{AB}
\widetilde\varphi_r^A
v^Mv^N
(T_MT_N)^B{}_C
\varphi_r^C.
$$

The color identity is

$$
\kappa_{AB}(T_MT_N)^B{}_C
=
-\kappa_{AB}c_{MR}{}^B c_{NC}{}^R
$$

$$
=
-c_{MRA}\kappa^{RS}c_{NCS}
=
+c_{MRA}\kappa^{RS}c_{NSC}.
$$

Thus the ordered seagull has the same

$c_{MRA}c_{NSC}$ color chain as the triangle.

Adding:

1. the $D_0$-cut,
2. the $D_1$-cut,
3. the $D_2$-cut,
4. the $n=2$ seagull,

ordinary Schwinger integration by parts gives

$$
\boxed{
\Gamma_{C,M_r}^{\rightarrow}
=
-\frac{\hbar g^2}{8\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\delta_4^{mn}
\mathcal R^{\rightarrow}_{mn}[B_r^D,C_r^E].
}
$$

This equation does not reuse the gauge-sector tensor $T_{m\rho n}$ or its D-weight.

### Matter evanescent trace

The omitted Project data are precisely the maps

$\Pi_{B_r},\Pi_{C_r}$. Define the signed, dimensionless trace $\chi_M$ at this step by

$$
\boxed{
\breve\delta^{mn}
\mathcal R^{\rightarrow}_{mn}[B_r^D,C_r^E]
=
-\frac{\epsilon}{2}\chi_M
(P_{\dot\alpha}B_r)^D
(P^{\dot\alpha}C_r)^E.
}
$$

For the reverse arrow, the ordered conjugate projector is defined by

$$
\boxed{
\breve\delta^{mn}
\mathcal R^{\leftarrow}_{mn}[C_r^D,B_r^E]
=
+\frac{\epsilon}{2}\chi_M
(P_{\dot\alpha}C_r)^D
(P^{\dot\alpha}B_r)^E.
}
$$

Then

$$
\Gamma_{\mathrm{defect},M_r}^{\rightarrow}
=
-\frac{\hbar g^2}{8\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\breve\delta^{mn}\mathcal R^{\rightarrow}_{mn}
$$

$$
=
+\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
(P_{\dot\alpha}B_r)^D
(P^{\dot\alpha}C_r)^E,
$$

and

$$
\Gamma_{\mathrm{defect},M_r}^{\leftarrow}
=
-\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
(P_{\dot\alpha}C_r)^D
(P^{\dot\alpha}B_r)^E.
$$

Therefore

$$
\boxed{
\mathcal A_{M_r}^{AB}
=
\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\left[
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right].
}
$$

The HT relative normalization requires

$$
\chi_M=1.
$$

That value is **not** selected here: it is the unevaluated component trace created exactly where the definitions of $B_r,C_r$ are absent.

---

## 5. `Sum and zero-shift map`

For three flavors,

$$
\boxed{
\mathcal A_M^{AB}
=
\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right].
}
$$

Thus

$$
\boxed{
\mathcal A_{AA}^{AB}
=
\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\Bigg[
D_{\dot\alpha}^D(P^{\dot\alpha}A)^E
-
(P_{\dot\alpha}A)^D D^{E\dot\alpha}
\Bigg.
}
$$

$$
\boxed{
\Bigg.
+
\chi_M\sum_{r=1}^3
\left(
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right)
\Bigg].
}
$$

### HT field factors

The dictionary gives

$$
\partial_{\dot\alpha}c
\longleftrightarrow
iD_{\dot\alpha},
$$

$$
\partial_{\dot\alpha}b
\longleftrightarrow
-\frac{i}{\sqrt2}P_{\dot\alpha}A.
$$

Hence

$$
(iD_{\dot\alpha}^D)
\left(-\frac{i}{\sqrt2}P^{\dot\alpha}A^E\right)
=
\frac1{\sqrt2}D_{\dot\alpha}^D
P^{\dot\alpha}A^E,
$$

$$
-
\left(-\frac{i}{\sqrt2}P_{\dot\alpha}A^D\right)
(iD^{E\dot\alpha})
=
-\frac1{\sqrt2}
(P_{\dot\alpha}A)^D D^{E\dot\alpha}.
$$

For matter,

$$
\partial_{\dot\alpha}\beta_r
\longleftrightarrow
\frac1{\sqrt2}P_{\dot\alpha}B_r,
\qquad
\partial_{\dot\alpha}\gamma^r
\longleftrightarrow
P_{\dot\alpha}C_r,
$$

so each HT bracket maps to $1/\sqrt2$ times the Project bracket.

Moreover,

$$
b^Ab^B
\longleftrightarrow
\left(-\frac{i}{\sqrt2}\right)^2
A^AA^B
=
-\frac12A^AA^B.
$$

Define the free loop map by

$$
\mathfrak M\!\left(Q_{1,\mathrm{HT}}\mathcal O\right)
=
\mathcal N_{P\to HT}\,
\nabla_-^{(1)}\mathfrak M(\mathcal O).
$$

Then

$$
\mathfrak M\!\left(Q_{1,\mathrm{HT}}(b^Ab^B)\right)
=
-\frac{\mathcal N_{P\to HT}}2
\mathcal A_{AA}^{AB}.
$$

The HT tensor has the same color ordering because

$$
\mathbb F^{AB}{}_{DE}
\longleftrightarrow
f_{A C D}f_{B C E}.
$$

No color reversal or additional $i$ remains.

---

## 6. `Separated shifts and derivative tower`

Let

$$
\Delta:=w-z.
$$

The triangle Feynman simplex gives the coordinate kernel

$$
\mathscr K_{w,z}(f,g)
:=
\int_0^1du\int_0^{1-u}dv\,
$$

$$
\qquad
e^{(z+u\Delta)\cdot\partial}
P_{\dot\alpha}f(0)\,
e^{(w-v\Delta)\cdot\partial}
P^{\dot\alpha}g(0).
$$

Since

$$
e^{u\Delta\cdot\partial}
=
\sum_{n=0}^{\infty}
\frac{u^n}{n!}
(\Delta\cdot\partial)^n,
$$

$$
e^{-v\Delta\cdot\partial}
=
\sum_{m=0}^{\infty}
\frac{v^m}{m!}
(-\Delta\cdot\partial)^m,
$$

and

$$
\int_0^1du\int_0^{1-u}dv\,u^nv^m
=
\int_0^1du\,
u^n\frac{(1-u)^{m+1}}{m+1},
$$

$$
=
\frac1{m+1}
\frac{\Gamma(n+1)\Gamma(m+2)}
{\Gamma(m+n+3)}
=
\frac{n!m!}{(m+n+2)!},
$$

one obtains exactly

$$
\boxed{
\mathscr K_{w,z}(f,g)
=
\mathcal D^\triangle_{w,z}(f,g).
}
$$

Explicitly,

$$
\mathcal D^\triangle_{w,z}(f,g)
=
\sum_{m,n\geq0}
\frac1{(m+n+2)!}
e^{z\cdot\partial}
((w-z)\cdot\partial)^n
P_{\dot\alpha}f
$$

$$
\qquad\times
e^{w\cdot\partial}
((z-w)\cdot\partial)^m
P^{\dot\alpha}g
\Big|_{0}.
$$

At coincident shifts,

$$
\boxed{
\mathcal D^\triangle_{0,0}(f,g)
=
\frac12P_{\dot\alpha}f\,P^{\dot\alpha}g.
}
$$

Therefore the separated Project anomaly is

$$
\boxed{
\mathcal A_{AA}^{AB}(z,w)
=
\frac{\hbar g^2}{8\pi^2}
\mathbb F^{AB}{}_{DE}
\Big[
\mathcal D^\triangle_{w,z}(U^D,A^E)
-
\mathcal D^\triangle_{w,z}(A^D,U^E)
}
$$

$$
\boxed{
\qquad
+
\chi_M\sum_{r=1}^3
\big(
\mathcal D^\triangle_{w,z}(B_r^D,C_r^E)
-
\mathcal D^\triangle_{w,z}(C_r^D,B_r^E)
\big)
\Big].
}
$$

At $w=z=0$, the factor $1/2$ converts the prefactor

$\hbar g^2/(8\pi^2)$ into

$\hbar g^2/(16\pi^2)$.

### Derivative tower

Differentiate $m$ times with respect to $w_1$ and $n$ times with respect to $w_2$. If $k$ of the $w_1$-derivatives and $l$ of the $w_2$-derivatives act on the first field, then

$$
u^{k+l}
$$

is produced from the first argument, while

$$
(1-v)^{m+n-k-l}
$$

is produced from the second argument.

Set

$$
a=k+l,
\qquad
b=m+n-k-l.
$$

Then

$$
\int_0^1du\int_0^{1-u}dv\,
u^a(1-v)^b
$$

$$
=
\frac1{b+1}
\int_0^1du\,u^a(1-u^{b+1})
$$

$$
=
\frac1{b+1}
\left(
\frac1{a+1}
-
\frac1{a+b+2}
\right)
$$

$$
=
\frac1{(a+1)(a+b+2)}
$$

$$
=
\frac1{(k+l+1)(m+n+2)}.
$$

Therefore

$$
\boxed{
\mathcal A_{AA}^{AB}
\!\left(
A^A\partial_1^m\partial_2^nA^B
\right)
=
\frac{\hbar g^2}{8\pi^2}
\frac{\mathbb F^{AB}{}_{DE}}{m+n+2}
}
$$

$$
\boxed{
\quad\times
\sum_{k=0}^m\sum_{l=0}^n
\frac{\binom mk\binom nl}{k+l+1}
\,
\mathcal B^{P,DE}_{k,l;m,n},
}
$$

where

$$
\mathcal B^{P,DE}_{k,l;m,n}
=
\partial_1^k\partial_2^lD_{\dot\alpha}^D\,
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}A)^E
$$

$$
\quad
-
\partial_1^k\partial_2^l
(P_{\dot\alpha}A)^D\,
\partial_1^{m-k}\partial_2^{n-l}
D^{E\dot\alpha}
$$

$$
\quad
+
\chi_M\sum_{r=1}^3
\Big[
\partial_1^k\partial_2^l
(P_{\dot\alpha}B_r)^D\,
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}C_r)^E
$$

$$
\qquad\qquad
-
\partial_1^k\partial_2^l
(P_{\dot\alpha}C_r)^D\,
\partial_1^{m-k}\partial_2^{n-l}
(P^{\dot\alpha}B_r)^E
\Big].
$$

At $m=n=0$,

$$
\frac{\hbar g^2}{8\pi^2}
\frac1{2}
=
\frac{\hbar g^2}{16\pi^2},
$$

so the derivative tower agrees with the regulated coincident limit.

---

## 7. `Mismatch ledger`

| Item | Independent result | Earliest mismatch |
| --- | --- | --- |
| Gauge triangle pole | $+\hbar g^2/(32\pi^2\epsilon)\,\widehat\delta^{mn}T_{m\rho n}p^\rho$ | none in the adopted candidate gauge branch |
| Gauge contact | $-\hbar g^2/(32\pi^2\epsilon)\,\delta_4^{mn}T_{m\rho n}p^\rho$ | none; four endpoint rows add |
| Gauge finite defect | $+\hbar g^2/(16\pi^2)\sigma\!\cdot p$ | matches conditional candidate |
| Requested $A$ versus candidate $X$ | $X=\sqrt2A/g$ | candidate insertion silently changes normalization unless every output letter is rescaled simultaneously |
| Matter color | $\mathbb F^{AB}{}_{DE}$ | matches HT ordering |
| Matter flavor | one diagonal loop per $r$, then $\sum_{r=1}^3$ | matches HT multiplicity |
| Matter closed-loop sign | no independent minus | any extra “fermion-loop minus” would begin at the Wick ledger and is incorrect in superfield variables |
| Matter D-weight | $\chi_M$ | $B_r,C_r$ projectors and parities are absent from the supplied Project conventions |
| Reusing $T_{m\rho n}$ in $M$ | not done | would first fail at the superspace D-word |
| Reusing $w_D=2$ in $M$ | not done | $M$ has $1/512$ insertion/projector word and different cuts |
| HT shifted kernel | simplex kernel derived exactly | matches |
| HT derivative tower | coefficient $1/[(m+n+2)(k+l+1)]$ derived exactly | matches |
| HT zero-shift component coefficient | simplex gives $1/2$ | separate zero-shift formula is larger by $2$ |
| HT intro $-1/4$ versus main $-\kappa_H^2$ | not resolvable by graph algebra | source-level overall-normalization conflict |
| Gauge-action normalization | candidate $ig/2$ adopted | authoritative input states no unique gauge branch |
| Evanescent counterterm | zero in minimal branch | a nonzero finite evanescent counterterm would shift the answer |

The source explicitly records the two HT normalization conflicts.Pasted text

Let

$$
C_P:=\frac{\hbar g^2}{16\pi^2}.
$$

For the shifted/tower branch, whose external coefficient is $2C_P$,

$$
\boxed{
\kappa_H^2
=
-\sqrt2\,\mathcal N_{P\to HT}\,C_P
}
$$

when $\chi_M=1$.

For the separate zero-shift branch,

$$
\boxed{
\kappa_H^2
=
-\frac{\mathcal N_{P\to HT}}{\sqrt2}\,C_P.
}
$$

These differ by exactly a factor $2$.

---

## 8. `Final exact formulas`

### G contribution

$$
\boxed{
\mathcal A_G^{AB}
=
\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\left[
D_{\dot\alpha}^D(P^{\dot\alpha}A)^E
-
(P_{\dot\alpha}A)^D D^{E\dot\alpha}
\right].
}
$$

### One-flavor M contribution

$$
\boxed{
\mathcal A_{M_r}^{AB}
=
\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\left[
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right].
}
$$

### Three-flavor M sum

$$
\boxed{
\mathcal A_M^{AB}
=
\chi_M\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\sum_{r=1}^3
\left[
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right].
}
$$

### Total ordered $AA$ anomaly

$$
\boxed{
\nabla_-^{(1)}(A^AA^B)
=
\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\Bigg[
D_{\dot\alpha}^D(P^{\dot\alpha}A)^E
-
(P_{\dot\alpha}A)^D D^{E\dot\alpha}
}
$$

$$
\boxed{
\qquad
+
\chi_M\sum_{r=1}^3
\left(
(P_{\dot\alpha}B_r)^D(P^{\dot\alpha}C_r)^E
-
(P_{\dot\alpha}C_r)^D(P^{\dot\alpha}B_r)^E
\right)
\Bigg].
}
$$

### Full derivative tower

$$
\boxed{
\nabla_-^{(1)}
\!\left(
A^A\partial_1^m\partial_2^nA^B
\right)
=
\frac{\hbar g^2}{8\pi^2}
\frac{\mathbb F^{AB}{}_{DE}}{m+n+2}
}
$$

$$
\boxed{
\quad\times
\sum_{k=0}^m\sum_{l=0}^n
\frac{\binom mk\binom nl}{k+l+1}
\,
\mathcal B^{P,DE}_{k,l;m,n}.
}
$$

The independently fixed result is

$$
\boxed{\chi_G=1.}
$$

The remaining matter coefficient is

$$
\boxed{\chi_M
=
-\frac{2}{\epsilon}\,
\frac{
\breve\delta^{mn}\mathcal R^{\rightarrow}_{mn}[B_r,C_r]
}{
(P_{\dot\alpha}B_r)(P^{\dot\alpha}C_r)
}.}
$$

The HT relative branch corresponds to

$$
\boxed{\chi_M=1,}
$$

but that equality requires the missing explicit definitions of

$\Pi_{B_r}$ and $\Pi_{C_r}$; it has not been imposed from the target.
