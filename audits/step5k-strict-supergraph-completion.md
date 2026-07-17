# Step 5K strict one-loop bi-letter supergraph completion

Status: `ACCEPTED_STEP5K_STRICT_SUPERGRAPH_COMPLETION`.

Authority base: `origin/main@06601a0ed4e6060e2d872980509e1b949e61506c`.

External holomorphic-twist data are not used in Sections 1--10.  They enter
only the final dictionary check in Section 11.

## 1. Symbols and fixed conventions / 记号

The canonical quantum fields are

$$
u^A:=\frac{V^A}{\sqrt2g},
\qquad
\Phi_{c,r}^A:=g^{-1}\Phi_r^A,
\qquad
\widetilde\Phi_{c,r}^A:=g^{-1}\widetilde\Phi_r^A.
\tag{K.1}
$$

The canonical external letters are

$$
A^A:=g^{-1}(\nabla_+\mathcal W_+)^A,
\qquad
B_r^A:=g^{-1}(\nabla_+\Phi_r)^A,
\tag{K.2}
$$

$$
C_r^A:=g^{-1}\widetilde\Phi_r^A,
\qquad
D_{\dot\alpha}^A:=g^{-1}\widetilde{\mathcal W}_{\dot\alpha}^A.
\tag{K.3}
$$

Their parities are

$$
|A|=|C_r|=0,
\qquad
|B_r|=|D_{\dot\alpha}|=1.
\tag{K.4}
$$

The Lie-algebra and one-loop normalizations are

$$
[T_A,T_B]=ic_{AB}{}^CT_C,
\qquad
c_{ABC}:=\kappa_{CD}c_{AB}{}^D=c_{[ABC]},
\qquad
h:=g^{-2},
\tag{K.5}
$$

$$
\mathbb F^{AB}{}_{DE}
:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
\tag{K.6}
$$

Every momentum is incoming:

$$
X(x)=\int\frac{d^dp}{(2\pi)^d}e^{ip\cdot x}X(p),
\qquad
\partial_m\mapsto ip_m,
\qquad
d=4-2\epsilon.
\tag{K.7}
$$

The two scalar squares required by dimensional reduction are not identified:

$$
\bar\Box_Ee^{ipx}=-\bar p^2e^{ipx},
\qquad
\Box_de^{ipx}=-p_d^2e^{ipx},
\qquad
\mu_p^2:=\bar p^2-p_d^2.
\tag{K.8}
$$

Finite spinor words use the four-spin square $\bar p^2$; regulated
propagators use $p_d^2$.  Hence

$$
\frac{\bar p^2}{p_d^2}=1+\frac{\mu_p^2}{p_d^2}.
\tag{K.9}
$$

## 2. Euclidean $\mathcal N=4$ action in $\mathcal N=1$ superspace

With $f_{AB}=\widetilde f_{AB}=h\kappa_{AB}$ on the perturbative branch,
the locked invariant action is

$$
\begin{aligned}
S_{E,\mathrm{inv}}^{(4)}=-\int d^4x_E\Bigg\{&
h\kappa_{AB}
[\widetilde\Phi_r^A(e^{V^CT_C})^B{}_D\Phi_r^D]_D\\
&+\frac h4[\kappa_{AB}\mathcal W^{Aa}\mathcal W_a^B]_F
+\frac h4[\kappa_{AB}\widetilde{\mathcal W}_{\dot a}^A
\widetilde{\mathcal W}^{B\dot a}]_{\widetilde F}\\
&-\frac{\sqrt2h}{6}
[\varepsilon_{rst}c_{ABC}\Phi_r^A\Phi_s^B\Phi_t^C]_F\\
&-\frac{\sqrt2h}{6}
[\varepsilon_{rst}c_{ABC}
\widetilde\Phi_r^A\widetilde\Phi_s^B\widetilde\Phi_t^C]_{\widetilde F}
\Bigg\}.
\end{aligned}
\tag{K.10}
$$

The gauge-fixed action is

$$
S_E=S_{E,\mathrm{inv}}^{(4)}+\mathbf s_E\Psi_{\mathcal F,\mathcal Y,E},
\tag{K.11}
$$

$$
\Psi_{\mathcal F,\mathcal Y,E}
=\langle\mathfrak c'_E,\mathcal F_E\rangle_E
-\frac12\langle\mathfrak c'_E,\mathcal Y_E\mathfrak n_E\rangle_E,
\tag{K.12}
$$

$$
\mathcal F_+=-\frac14\bar D^2V,
\qquad
\mathcal F_-=-\frac14D^2V.
\tag{K.13}
$$

In the fixed Fermi--Feynman representative, completing the multiplier square
gives the quadratic averaging term

$$
S_{E,V,\mathrm{gf}}^{(2)}
=\frac h4\int d^8z\,V\cdot\bar\Box_E
\left(\mathcal P_+^{\bar4}+\mathcal P_-^{\bar4}\right)V.
\tag{K.14}
$$

This is the exact four-spin action kernel; $\Box_d^{-1}$ enters only in the
regulated propagator.  The gauge-fixing term has no cubic or quartic
interaction at trivial background.  The separated
Nielsen--Kallosh factor is a field-independent measure constant:

$$
\frac{\delta^n}{\delta X_1\cdots\delta X_n}
\log\mathfrak F_E^{\mathrm{NK}}=0,
\qquad n\ge1.
\tag{K.15}
$$

Thus there is no NK propagator and no NK interaction vertex in this
representative.

## 3. Complete momentum-space super-Feynman rules through $g^2$

The derivation, including the odd FP inverse, is recorded in
`audits/step5k-momentum-rules-and-fp-inverse.md`.  The complete rule surface is
reproduced here.

### 3.1 Graph-factor rule

For an ordered action Hessian

$$
\mathcal C_E[X_1,\ldots,X_n]
:=\frac{\vec\delta}{\delta X_n}\cdots
\frac{\vec\delta}{\delta X_1}S_E,
\tag{K.16}
$$

an action vertex and a source vertex are

$$
\mathfrak v_E=-\frac1\hbar\mathcal C_E,
\qquad
\mathfrak v_{J,E}=+\frac1\hbar\mathcal C_{J,E}.
\tag{K.17}
$$

Every internal edge is $\hbar K^{-1}$.  The exact full-to-half identities are

$$
\int_{E,8}U
=\int_{E,+}\left(-\frac14\bar D^2\right)U
=\int_{E,-}\left(-\frac14D^2\right)U.
\tag{K.18a}
$$

Conversely, on the residual-free four-spin complement,

$$
\int_{E,+}X_+
=\int_{E,8}\left(-\frac{D^2}{4\bar\Box_E}\right)X_+,
\qquad
\int_{E,-}X_-
=\int_{E,8}\left(-\frac{\bar D^2}{4\bar\Box_E}\right)X_-.
\tag{K.18b}
$$

The chiral composition is

$$
\left(-\frac14\bar D^2\right)
\left(-\frac{D^2}{4\bar\Box_E}\right)X_+
=\frac{\bar D^2D^2}{16\bar\Box_E}X_+
=X_+,
\tag{K.18c}
$$

with the antichiral order reversed.  Replacing $\bar\Box_E^{-1}$ by
$\Box_d^{-1}$ produces the regulated defect (K.9); a graph uses one measure
representation and never attaches both conversion operators.

### 3.2 Propagators

The canonical vector line is

$$
\boxed{
\langle u^A(p,1)u^B(p',2)\rangle_E
=-(2\pi)^d\delta^{(d)}(p+p')
\frac{\hbar\kappa^{AB}}{p_d^2}\delta^4(\theta_{12}).}
\tag{K.19}
$$

The oriented chiral line is

$$
\boxed{
\begin{aligned}
\langle\Phi_{c,r}^A(p,1)\widetilde\Phi_{c,s}^B(p',2)\rangle_E
={}&(2\pi)^d\delta^{(d)}(p+p')\delta_{rs}
\frac{\hbar\kappa^{AB}}{16p_d^2}\\
&\times\bar D_1^2(p)D_1^2(p)\delta^4(\theta_{12}).
\end{aligned}}
\tag{K.20}
$$

The reversed orientation contains $D^2\bar D^2/(16p_d^2)$.  Its regulated
composition is

$$
K_E^{\Phi\widetilde\Phi}(K_E^{\Phi\widetilde\Phi})^{-1}_d
=\left(1+\frac{\mu_p^2}{p_d^2}\right)\mathbf1_+.
\tag{K.21}
$$

For the ghost columns

$$
\mathbf c=\begin{pmatrix}\mathfrak c_+\\
\widetilde{\mathfrak c}_-\end{pmatrix},
\qquad
\mathbf c'=\begin{pmatrix}\mathfrak c'_+\\
\widetilde{\mathfrak c}'_-\end{pmatrix},
\tag{K.22}
$$

the free action kernel is

$$
K_E^{\rm FP}
=\begin{pmatrix}
0&+\dfrac i4\bar D^2\\[2mm]
-\dfrac i4D^2&0
\end{pmatrix}.
\tag{K.23}
$$

On the residual-free chiral/antichiral complements,

$$
(K_E^{\rm FP})^{-1}_{\bar4}
=\begin{pmatrix}
0&+\dfrac i4\bar\Box_E^{-1}\bar D^2\\[2mm]
-\dfrac i4\bar\Box_E^{-1}D^2&0
\end{pmatrix}.
\tag{K.24}
$$

Both typed compositions are explicit:

$$
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_{\bar4}
=\begin{pmatrix}\mathcal P_+^{\bar4}&0\\0&\mathcal P_-^{\bar4}\end{pmatrix}
=\mathbf1_{\mathscr F^\perp},
\tag{K.25}
$$

$$
(K_E^{\rm FP})^{-1}_{\bar4}K_E^{\rm FP}
=\begin{pmatrix}\mathcal P_+^{\bar4}&0\\0&\mathcal P_-^{\bar4}\end{pmatrix}
=\mathbf1_{\mathscr G^\perp}.
\tag{K.26}
$$

The regulated inverse replaces $\bar\Box_E^{-1}$ by $\Box_d^{-1}$ and
obeys

$$
K_E^{\rm FP}(K_E^{\rm FP})^{-1}_d-1
=(K_E^{\rm FP})^{-1}_dK_E^{\rm FP}-1
=\frac{\mu_p^2}{p_d^2}.
\tag{K.27}
$$

The two nonzero oriented ghost contractions are

$$
\boxed{
\begin{aligned}
\langle\mathfrak c_+^A(p,1)\widetilde{\mathfrak c}'_{-,B}(p',2)\rangle_E
&=(2\pi)^d\delta^{(d)}(p+p')\delta^A{}_B
\left[-\frac{i\hbar}{4p_d^2}\bar D_1^2(p)\right],\\
\langle\widetilde{\mathfrak c}_-^A(p,1)\mathfrak c'_{+,B}(p',2)\rangle_E
&=(2\pi)^d\delta^{(d)}(p+p')\delta^A{}_B
\left[+\frac{i\hbar}{4p_d^2}D_1^2(p)\right].
\end{aligned}}
\tag{K.28}
$$

Reversing an ordered ghost contraction changes its sign.  Every closed FP
loop has one cyclic odd-permutation sign $-1$.  All other free ghost
contractions vanish.

### 3.3 Interaction vertices

The two canonical background-field-strength Hessians used by the gauge
triangle are

$$
\boxed{
\mathfrak V_W
=-\frac{ig}{4\hbar}c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),}
\tag{K.29}
$$

$$
\boxed{
\mathfrak V_{\widetilde W}
=+\frac{ig}{4\hbar}c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).}
\tag{K.30}
$$

All cubic and quartic pure-gauge vertices are generated without a hidden
symmetrization by

$$
\Gamma_a
=\sum_{p,q\ge0}\frac{(-1)^p}{p!q!(p+q+1)}
V^p(D_aV)V^q,
\tag{K.31}
$$

$$
\widetilde\Gamma_{\dot a}
=\sum_{p,q\ge0}\frac{(-1)^{q+1}}{p!q!(p+q+1)}
V^p(\bar D_{\dot a}V)V^q,
\tag{K.32}
$$

followed by labeled differentiation of the two gauge kinetic words.  The
matrix order in (K.31)--(K.32) is retained.

The complete raw and labeled dispatcher is the checked artifact
`generated/step5k-momentum-rule-ledger.json`.  Its exact row counts are

$$
N_{\rm raw}=2(4+10)=28,
\qquad
N_{\rm labeled}=2(4)(3!)+2(10)(4!)=528,
\qquad
N_{\rm unresolved}=0.
\tag{K.32a}
$$

Every row retains $(p,q,r,s)$, chirality, the factor obtained from
$(\sqrt2g)^nh\kappa_{AB}$ with $h=g^{-2}$, both ordered color words, the
half-measure conversion, the labeled derivative order, and the momentum of
each derivative's own ordered subword.

The canonical matter vertices through $g^2$ are

$$
S_E^{\rm mat}
=-\sum_{r=1}^3\int d^8z\,
\widetilde\Phi_{c,r}
\left[1+\sqrt2g\,u^AT_A
+g^2u^Au^BT_AT_B\right]\Phi_{c,r}+O(g^3),
\tag{K.33}
$$

$$
\mathcal C_E[\widetilde\Phi_{c,r}^A,u^M,\Phi_{c,s}^C]
=-\sqrt2g\,\delta_{rs}\kappa_{AB}(T_M)^B{}_C,
\tag{K.34}
$$

$$
\begin{aligned}
\mathcal C_E[\widetilde\Phi_{c,r}^A,u^{M_1},u^{M_2},\Phi_{c,s}^C]
=-g^2\delta_{rs}\kappa_{AB}\Big[&(T_{M_1}T_{M_2})^B{}_C\\
&+(T_{M_2}T_{M_1})^B{}_C\Big].
\end{aligned}
\tag{K.35}
$$

The two canonical superpotential Hessians are

$$
\mathcal C_E[\Phi_{c,r_1}^{A_1},\Phi_{c,r_2}^{A_2},\Phi_{c,r_3}^{A_3}]
=+\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3},
\tag{K.36}
$$

$$
\mathcal C_E[\widetilde\Phi_{c,r_1}^{A_1},
\widetilde\Phi_{c,r_2}^{A_2},\widetilde\Phi_{c,r_3}^{A_3}]
=+\sqrt2g\,\varepsilon_{r_1r_2r_3}c_{A_1A_2A_3}.
\tag{K.37}
$$

For

$$
d:=\widetilde{\mathfrak c}_--\mathfrak c_+,
\qquad
s:=\widetilde{\mathfrak c}_-+\mathfrak c_+,
\tag{K.38}
$$

the BRST word through $V^2$ is

$$
\mathbf s_EV=id-\frac i2[V,s]+\frac i{12}[V,[V,d]]+O(V^4).
\tag{K.39}
$$

Therefore the FP action vertices through $g^2$ are

$$
\begin{aligned}
S_{E,{\rm FP}}^{(1u)}
=-\frac{i\sqrt2g}{8}\Big[&
\int_{E,+}\mathfrak c'_+\bar D^2[u,s]
+\int_{E,-}\widetilde{\mathfrak c}'_-D^2[u,s]\Big],
\end{aligned}
\tag{K.40}
$$

$$
\begin{aligned}
S_{E,{\rm FP}}^{(2u)}
=+\frac{ig^2}{24}\Big[&
\int_{E,+}\mathfrak c'_+\bar D^2[u,[u,d]]
+\int_{E,-}\widetilde{\mathfrak c}'_-D^2[u,[u,d]]\Big].
\end{aligned}
\tag{K.41}
$$

There is no three-vector FP vertex because $B_3=0$.

### 3.4 Composite WW insertion

The linear canonical letter is

$$
A_{(1)}^A=K_+^cu^A,
\qquad
K_+^c:=-\frac1{4\sqrt2}D_+\bar D^2D_+.
\tag{K.42}
$$

The marked kernel is

$$
D_-K_+^c
=-\frac1{8\sqrt2}D^2\bar D^2D_+.
\tag{K.43}
$$

The ordered translated bilocal insertion at the linear-linear level is

$$
\boxed{
\begin{aligned}
\mathcal I_{0,w}^{AB}
={}&(D_-K_+^cu^A)e^{w\cdot\partial}(K_+^cu^B)\\
&+(K_+^cu^A)e^{w\cdot\partial}(D_-K_+^cu^B).
\end{aligned}}
\tag{K.44}
$$

In momentum space, the translated $B$ occurrence carries

$$
e^{iw\cdot r_2}.
\tag{K.45}
$$

The nonlinear insertion classes are retained in the resolvent as

$$
\boxed{
\Gamma_{g^2}
=\langle\mathcal I_2\rangle
-\hbar^{-1}\langle\mathcal I_1S_3\rangle
-\hbar^{-1}\langle\mathcal I_0S_4\rangle
+\frac1{2\hbar^2}\langle\mathcal I_0S_3S_3\rangle.}
\tag{K.46}
$$

No class in (K.46) is silently identified with another topology.

## 4. Two distinct triangle graphs

The graph source of truth is `audits/step5k-diagram-ir.json`.

Gauge graph `G-WW-GAUGE-01` contains

$$
u\longleftrightarrow u,
\qquad
u\longleftrightarrow u,
\qquad
u\longleftrightarrow u,
\tag{K.47}
$$

and the derivative-difference vertices (K.29)--(K.30).

Matter graph `G-WW-MATTER-01` contains

$$
u\longleftrightarrow u,
\qquad
\Phi_{c,r}\longleftrightarrow\widetilde\Phi_{c,r},
\qquad
u\longleftrightarrow u,
\tag{K.48}
$$

and two nondifferential matter vertices (K.34).  It cannot produce the gauge
sigma-chain numerator.

The rendered figures are

- `paper/figures/step5k-gauge-vector-triangle.pdf` and `.svg`;
- `paper/figures/step5k-adjoint-matter-triangle.pdf` and `.svg`.

## 5. Gauge triangle: Wick contraction to the pre-integral amplitude

Use

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+p+q,
\tag{K.49}
$$

$$
D_0=r_{0,d}^2,
\qquad
D_1=r_{1,d}^2,
\qquad
D_2=r_{2,d}^2.
\tag{K.50}
$$

Fix the first source occurrence at the $\widetilde W$ vertex and the
translated second occurrence at the $W$ vertex.  The two action orders give

$$
\frac1{2!}
\left(S_{\widetilde W}S_W+S_WS_{\widetilde W}\right)
=S_{\widetilde W}S_W.
\tag{K.51}
$$

The port-preserving Wick word is

$$
\mathcal W_{\rm dir}
=\langle u_I^Au_{\widetilde W}^{U}\rangle
\langle u_{\widetilde W}^{C}u_W^{C'}\rangle
\langle u_W^{V}u_I^B\rangle.
\tag{K.52}
$$

Substitution of the three propagators gives

$$
\begin{aligned}
\mathcal W_{\rm dir}
={}&(-\hbar)^3
\kappa^{AU}\kappa^{CC'}\kappa^{VB}
\frac{e^{iw\cdot r_2}}{D_0D_1D_2}\\
&\times
\delta^4(\theta_I-\theta_{\widetilde W})
\delta^4(\theta_{\widetilde W}-\theta_W)
\delta^4(\theta_W-\theta_I).
\end{aligned}
\tag{K.53}
$$

The color contraction is not suppressed:

$$
\begin{aligned}
&\kappa^{AU}\kappa^{CC'}\kappa^{VB}
c_{UCD}c_{VC'E}\\
&\hspace{20mm}
=\mathbb F^{AB}{}_{DE}.
\end{aligned}
\tag{K.54}
$$

The source kernels give

$$
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=\frac1{64}.
\tag{K.55}
$$

The closed delta loop gives $16$.  Each same-edge mixed anticommutator has
the common normalization $-2ir_i$ from (2A.42).  Extracting this common
factor at the left and right derivative-difference vertices gives

$$
\boxed{
\left(\frac1{64}\right)(16)(2)(2)=1.}
\tag{K.56}
$$

The left endpoint sum is $r_0+r_1=L_1$ and the right endpoint sum is
$r_1+r_2=L_2$.  Thus the factors $2$ are the two anticommutator
normalizations; $L_1,L_2$ contain only the endpoint-momentum sums.

The two exponent vertices and the three propagator coefficients give

$$
\begin{aligned}
&\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)(-\hbar)^3\\
&\quad=
\left(\frac{g^2}{16\hbar^2}\right)(-\hbar^3)
=-\frac{\hbar g^2}{16}.
\end{aligned}
\tag{K.57}
$$

The ordered odd source-loop integration by parts contributes $-1$:

$$
\begin{aligned}
0
&=\int d^4\theta\,D_-\!\left[(K_+^cu)X\right]\\
&=\int d^4\theta\,
\left[(D_-K_+^cu)X+(K_+^cu)D_-X\right],
\qquad |K_+^cu|=0,
\end{aligned}
\tag{K.57a}
$$

so

$$
\int d^4\theta\,(D_-K_+^cu)X
=-\int d^4\theta\,(K_+^cu)D_-X.
\tag{K.57b}
$$

Consequently

$$
\left(-\frac{\hbar g^2}{16}\right)(-1)
=+\frac{\hbar g^2}{16}.
\tag{K.58}
$$

Define

$$
L_1:=r_0+r_1=2k+q,
\qquad
L_2:=r_1+r_2=2k+p+2q.
\tag{K.59}
$$

The selected noncollapsed numerator is

$$
\boxed{
N_{G,+}{}^{\dot\alpha}
=(L_1)_{+\dot\beta}(ip)^{\dot\beta\gamma}
(L_2)_\gamma{}^{\dot\alpha}.}
\tag{K.60}
$$

Thus the corrected spinor-form pre-integral amplitude is

$$
\boxed{
\begin{aligned}
\Gamma_{T,G}^{A|B}(w)
={}&\frac{\hbar g^2}{16}\mathbb F^{AB}{}_{DE}
D_{\dot\alpha}^D(q)A^E(p)\\
&\times\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\frac{e^{iw\cdot r_2}N_{G,+}{}^{\dot\alpha}}
{D_0D_1D_2}
+\Gamma_{\rm coll}+\Gamma_{\rm EOM}.
\end{aligned}}
\tag{K.61}
$$

For

$$
T_{\mu\rho\nu,+}{}^{\dot\alpha}
:=(\sigma_\mu\bar\sigma_\rho\sigma_\nu)_+{}^{\dot\alpha},
\tag{K.62}
$$

equation (K.60) is

$$
N_{G,+}{}^{\dot\alpha}
=iL_1^\mu p^\rho L_2^\nu
T_{\mu\rho\nu,+}{}^{\dot\alpha}.
\tag{K.63}
$$

Therefore the Lorentz-tensor form carries $i\hbar g^2/16$, not
$\hbar g^2/16$.

The formerly displayed coefficient is rejected:

$$
\boxed{
\mathrm{REJECTED\_LEGACY\_PREFACTOR}:
\qquad
\frac{\hbar g^2}{2}
=8\left(\frac{\hbar g^2}{16}\right).}
\tag{K.64}
$$

Its factor $8$ came from assigning a unit propagator to
$v_{\rm old}=V/(2g)=u/\sqrt2$ on three internal vector lines.

## 6. Edge-tagged noncommutative $D$-algebra

The generated machine trace is `generated/step5k-ww-gauge-dword.json`; the readable trace
is `audits/step5k-ww-gauge-triangle-dword.md`.

For one marked occurrence, the ordered endpoint word is

$$
\mathscr D_G
=(D^{[e_0]}-D^{[e_1]})K_+^c
(\bar D^{[e_1]}-\bar D^{[e_2]}).
\tag{K.65}
$$

It is expanded before any endpoint transfer:

$$
\begin{aligned}
\mathscr D_G={}&
+D^{[e_0]}K_+^c\bar D^{[e_1]}
-D^{[e_0]}K_+^c\bar D^{[e_2]}\\
&-D^{[e_1]}K_+^c\bar D^{[e_1]}
+D^{[e_1]}K_+^c\bar D^{[e_2]}.
\end{aligned}
\tag{K.66}
$$

The edge-tagged endpoint identities are

$$
D_1^{[e_0]}\delta_{01}^{[e_0]}
=-D_0^{[e_0]}\delta_{01}^{[e_0]},
\tag{K.67}
$$

$$
\bar D_2^{[e_2]}\delta_{20}^{[e_2]}
=-\bar D_0^{[e_2]}\delta_{20}^{[e_2]}.
\tag{K.68}
$$

Hence the four raw and transport signs are

$$
s_{\rm raw}=(+1,-1,-1,+1),
\tag{K.69}
$$

$$
s_{\rm transport}=(-1,+1,+1,-1),
\tag{K.70}
$$

$$
s_{\rm raw}s_{\rm transport}=(-1,-1,-1,-1).
\tag{K.71}
$$

The closed loop is saturated in fixed order:

$$
\delta_{01}\delta_{12}\delta_{20}
D^2\bar D^2
\longrightarrow16\,\delta_{\rm closed}.
\tag{K.72}
$$

For a single edge, (2A.41)--(2A.42) gives

$$
\{D_+(r_i),\bar D_{\dot\beta}(r_i)\}
=-2i(r_i)_{+\dot\beta}.
\tag{K.73}
$$

Summing the two allowed endpoint rows at each derivative-difference vertex
gives

$$
\begin{aligned}
\mathscr A_{L,+\dot\beta}
&:=\sum_{i=0}^{1}\{D_+(r_i),\bar D_{\dot\beta}(r_i)\}
=-2i(L_1)_{+\dot\beta},\\
\mathscr A_{R,\gamma}{}^{\dot\alpha}
&:=\sum_{j=1}^{2}\{D_\gamma(r_j),\bar D^{\dot\alpha}(r_j)\}
=-2i(L_2)_\gamma{}^{\dot\alpha}.
\end{aligned}
\tag{K.74}
$$

After extracting the two explicit same-edge anticommutator factors in (K.74),
multiplying one normalized ordered pair without commuting it as an ordinary
variable gives four terms:

$$
\begin{aligned}
&[D_+\bar D_{\dot\beta}](ip)^{\dot\beta\gamma}
[D_\gamma\bar D^{\dot\alpha}]\\
={}&
[\bar D_{\dot\beta}D_+](ip)^{\dot\beta\gamma}
[\bar D^{\dot\alpha}D_\gamma]\\
&+i[\bar D_{\dot\beta}D_+](ip)^{\dot\beta\gamma}
(L_2)_\gamma{}^{\dot\alpha}\\
&+i(L_1)_{+\dot\beta}(ip)^{\dot\beta\gamma}
[\bar D^{\dot\alpha}D_\gamma]\\
&-(L_1)_{+\dot\beta}(ip)^{\dot\beta\gamma}
(L_2)_\gamma{}^{\dot\alpha}.
\end{aligned}
\tag{K.75}
$$

The first term is the longitudinal/contact word; the middle two are
EOM/divergence words; the last is the selected parent.  Multiplication by
the common row sign in (K.71) changes the last sign to $+1$.  Therefore

$$
N_{ij,+}{}^{\dot\alpha}
:=(r_i)_{+\dot\beta}(ip)^{\dot\beta\gamma}
(r_j)_\gamma{}^{\dot\alpha},
\qquad i\in\{0,1\},\quad j\in\{1,2\},
$$

$$
\sum_{i=0}^{1}\sum_{j=1}^{2}
(s_{\rm raw}s_{\rm transport})_{ij}
\left[-4N_{ij,+}{}^{\dot\alpha}\right]
=4\sum_{i=0}^{1}\sum_{j=1}^{2}N_{ij,+}{}^{\dot\alpha}
=4N_{G,+}{}^{\dot\alpha}
=(2)(2)N_{G,+}{}^{\dot\alpha}.
\tag{K.75a}
$$

This proves the two factors in (K.56) without double counting $L_1L_2$.
The external remnant is exactly

$$
D_{\dot\alpha}^D(q)
N_{G,+}{}^{\dot\alpha}A^E(p).
\tag{K.76}
$$

The second $D_-$ mark is a distinct source occurrence.  It is not an
additional copy of the first mark.  The full token stream contains every
external placement, chirality pair, marked physical edge, and ordered
source/background endpoint row.

The translation phase is retained.  With $x+y+z=1$ and the shift (K.78),
define

$$
a:=x=1-y-z,
\qquad
b:=x+y=1-z,
\qquad
0\le a\le b\le1.
\tag{K.76a}
$$

Then

$$
r_2=\ell+aq+bp,
\qquad
e^{iw\cdot r_2}
=e^{iw\cdot\ell}e^{iw\cdot(aq+bp)}.
\tag{K.76b}
$$

Here $w^{\dot\alpha}\ell_{+\dot\alpha}=\omega_m\ell^m$ with
$\omega_{a\dot\alpha}=\delta_a{}^+w_{\dot\alpha}$.  Consequently

$$
\omega^2
=\epsilon^{ab}\epsilon^{\dot\alpha\dot\beta}
\omega_{a\dot\alpha}\omega_{b\dot\beta}
=\epsilon^{++}\epsilon^{\dot\alpha\dot\beta}
w_{\dot\alpha}w_{\dot\beta}
=0.
\tag{K.76c}
$$

For every rotational scalar $F(\ell^2)$,

$$
\int_\ell(\omega\!\cdot\!\ell)^{2n+1}F(\ell^2)=0,
\tag{K.76d}
$$

$$
\int_\ell(\omega\!\cdot\!\ell)^{2n}F(\ell^2)
=c_n(\omega^2)^n\int_\ell(\ell^2)^nF(\ell^2)=0,
\qquad n\ge1.
\tag{K.76e}
$$

Thus, coefficient by coefficient in the formal holomorphic jet,

$$
\int_\ell e^{iw\cdot\ell}F(\ell^2)
=\int_\ell F(\ell^2),
\tag{K.76f}
$$

while $e^{iw\cdot(aq+bp)}$ remains.  No $w=0$ limit is imposed.

## 7. DRED anomaly sector and loop integration

Feynman parameterization gives

$$
\frac1{D_0D_1D_2}
=2\int_{x,y,z\ge0}dx\,dy\,dz\,
\delta(1-x-y-z)
\frac1{(\ell^2+\Delta)^3},
\tag{K.77}
$$

$$
\ell=k+yq+z(p+q),
\tag{K.78}
$$

$$
\Delta=xyq^2+xz(p+q)^2+yzp^2.
\tag{K.79}
$$

The shifted numerator vectors are

$$
L_1=2\ell+(1-2y)q-2z(p+q),
\tag{K.80}
$$

$$
L_2=2\ell+(1-2y)q+(1-2z)(p+q).
\tag{K.81}
$$

Odd powers of $\ell$ integrate to zero.  The rank-two integral is

$$
\int_\ell\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=\frac{\widehat\delta^{mn}}d
\left[I_2(\Delta)-\Delta I_3(\Delta)\right],
\tag{K.82}
$$

$$
I_n(\Delta)
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}{\Gamma(n)}
\Delta^{d/2-n}.
\tag{K.83}
$$

Since

$$
\Delta I_3
=\frac{\Gamma(3-d/2)}{2\Gamma(2-d/2)}I_2
=\frac{2-d/2}{2}I_2
=\frac\epsilon2I_2,
\tag{K.84}
$$

and

$$
\frac1d\left(1-\frac\epsilon2\right)
=\frac1{4-2\epsilon}\frac{2-\epsilon}{2}
=\frac14,
\tag{K.85}
$$

the pole is

$$
\operatorname*{Pole}
\int_k\frac{L_1^mL_2^n}{D_0D_1D_2}
=\frac{\widehat\delta^{mn}}{16\pi^2\epsilon}.
\tag{K.86}
$$

The Schwinger cut uses the four-spin inverse square on the marked edge:

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\bar r_e^2-r_{e,d}^2}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
\tag{K.87}
$$

The selected finite spinor square is

$$
\sigma\cdot L\,\bar\sigma\cdot p\,\sigma\cdot L
=2(L\cdot p)\sigma\cdot L-\bar L^2\sigma\cdot p.
\tag{K.88}
$$

The two UV-leading factors are $2L$, so the parent-minus-cut remainder is

$$
-4(\bar L^2-L_d^2)\sigma\cdot p
=-4\mu_L^2\sigma\cdot p.
\tag{K.89}
$$

The evanescent master is evaluated without dropping $\epsilon$ before the
pole.  Rotational reduction gives

$$
\int_\ell\mu_\ell^2f(\ell^2)
=\frac{4-d}{d}\int_\ell\ell^2f(\ell^2)
=\frac{2\epsilon}{d}\int_\ell\ell^2f(\ell^2).
\tag{K.90}
$$

Therefore

$$
\begin{aligned}
J_\mu(\Delta)
&:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{(\ell^2+\Delta)^3}\\
&=\frac{2\epsilon}{d}
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\ell^2}{(\ell^2+\Delta)^3}\\
&=\frac{2\epsilon}{d}
\left[I_2(\Delta)-\Delta I_3(\Delta)\right]\\
&=\frac{2\epsilon}{4-2\epsilon}
\left(1-\frac\epsilon2\right)I_2(\Delta)\\
&=\frac\epsilon2I_2(\Delta).
\end{aligned}
\tag{K.91}
$$

Using

$$
I_2(\Delta)
=\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
\tag{K.92}
$$

$$
\Gamma(\epsilon)=\frac1\epsilon-\gamma_E+O(\epsilon),
\tag{K.93}
$$

one obtains

$$
\boxed{
\lim_{\epsilon\to0}J_\mu(\Delta)
=\frac1{32\pi^2}.}
\tag{K.94}
$$

The simplex normalization is

$$
2\int_{\Sigma_2}1
=2\int_0^1dy\int_0^{1-y}dz\,1
=2\int_0^1(1-y)dy
=1.
\tag{K.95}
$$

The isolated directed gauge triangle and its cut therefore give

$$
\begin{aligned}
\Gamma_{G,\mathrm{directed}}
&=\left(\frac{\hbar g^2}{16}\right)
(-4)\left(\frac1{32\pi^2}\right)\\
&=-\frac{\hbar g^2}{128\pi^2}\\
&=\boxed{-\frac{\lambda_1}{8}}.
\end{aligned}
\tag{K.96}
$$

Equation (K.96) is an isolated canonical directed seed.  It is not the full
gauge external-slot/contact orbit.

## 8. Matter triangle: separate Wick and $D$-algebra calculation

The order-$g^2$ matter resolvent is

$$
\Gamma^{(1)}_{g^2,\mathrm{mat}}
=\langle\mathcal I_2\rangle
-\hbar^{-1}\langle\mathcal I_1S_{m3}\rangle
-\hbar^{-1}\langle\mathcal I_0S_{m4}\rangle
+\frac1{2\hbar^2}\langle\mathcal I_0S_{m3}S_{m3}\rangle.
\tag{K.97}
$$

The first three terms are respectively two-loop/no-$BC$-port, a scaleless
self-edge, and an odd shifted seagull.  Only the last term supports the
one-loop matter triangle.

Use the matter routing

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q.
\tag{K.98}
$$

For external $C_r^D(q)$ at vertex $1$ and $B_r^E(p)$ at vertex $2$, the
Wick substitution is

$$
\begin{aligned}
&\langle u_I^Au_1^U\rangle
\langle\Phi_{c,r}(1)\widetilde\Phi_{c,r}(2)\rangle
\langle u_2^Vu_I^B\rangle\\
&=(-\hbar)^2\hbar\,
\mathbb F^{AB}{}_{DE}\delta_{rs}
\frac{e^{iw\cdot r_2}\bar D_1^2D_1^2}{16D_0D_1D_2}
\delta_{01}^4\delta_{12}^4\delta_{20}^4.
\end{aligned}
\tag{K.99}
$$

For this routing, the same simplex change gives
$r_2=\ell-aq-bp$.  Equations (K.76c)--(K.76f) remove only the null loop
phase and retain $e^{-iw\cdot(aq+bp)}$.  The sign is fixed by the incoming
matter momenta in (K.98).

The two matter exponent vertices give

$$
\frac1{2!}
\left(\frac{\sqrt2g}{\hbar}\right)^2(1+1)
=\frac{2g^2}{\hbar^2}.
\tag{K.100}
$$

There is no derivative-difference vertex and no gauge sigma chain.  Set

$$
a_{i+}:=r_{i,+\dot+},
\quad
b_{i+}:=r_{i,+\dot-},
\quad
a_{i-}:=r_{i,-\dot+},
\quad
b_{i-}:=r_{i,-\dot-}.
\tag{K.101}
$$

Define

$$
W_{ij}:=a_{i+}b_{j+}-b_{i+}a_{j+},
\qquad
\det r_i:=a_{i+}b_{i-}-b_{i+}a_{i-}.
\tag{K.102}
$$

Direct left-Berezin differentiation of the first marked word gives

$$
\mathscr D_{M,CB}^{(A)}=-2\mathcal S_{012},
\tag{K.103}
$$

$$
\boxed{
\mathcal S_{012}
=(\det r_0)W_{12}-(\det r_1)W_{02}.}
\tag{K.104}
$$

The second marked word is distinct:

$$
\boxed{
\mathcal S_2
=W_{01}(a_{2+}b_{1-}-a_{1-}b_{2+}).}
\tag{K.105}
$$

Its longitudinal transport is retained:

$$
D_{0+}\bar D_0^2D_0^2\delta_{02}^4
=-D_2^2\bar D_2^2D_{2+}\delta_{02}^4,
\tag{K.106}
$$

$$
D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)
=-16(\det r_1)D_2^2(-r_1).
\tag{K.107}
$$

Thus the adjacent $r_1$ cut is not lost.

The exact simplex moments are

$$
2\int_{\Sigma_2}x
=2\int_{\Sigma_2}y
=2\int_{\Sigma_2}z
=\frac13.
\tag{K.108}
$$

For the first mark,

$$
4\hbar g^2
\left[-2\int_{\Sigma_2}(x+y)\right]
\frac1{32\pi^2}
=-\frac43\lambda_1.
\tag{K.109}
$$

For the second mark,

$$
2\int_{\Sigma_2}(y-z)=0,
\tag{K.110}
$$

$$
2\int_{\Sigma_2}\left(\frac12-y\right)=\frac16,
\tag{K.111}
$$

$$
2\int_{\Sigma_2}\left(\frac12-z\right)=\frac16,
\tag{K.112}
$$

$$
4\hbar g^2
\left[2\int_{\Sigma_2}\left(\frac12-z\right)\right]
\frac1{32\pi^2}
=+\frac13\lambda_1.
\tag{K.113}
$$

The four occurrence-tagged Wick routes are

$$
\begin{array}{c|c|c|c}
\text{route}&\text{source attachment}&\text{marked edge}&
\text{raw anomaly coefficient}\\ \hline
\texttt{MW-F1}&A\to C,\ B\to B&e_0&
-\eta_{\rm src}\dfrac43\lambda_1\mathbb F^{AB}{}_{DE}\\[2mm]
\texttt{MW-F2}&A\to C,\ B\to B&e_2&
+\eta_{\rm src}\dfrac13\lambda_1\mathbb F^{AB}{}_{DE}\\[2mm]
\texttt{MW-X1}&A\to B,\ B\to C&e_2&
+\eta_{\rm src}\dfrac13\lambda_1\mathbb F^{AB}{}_{ED}\\[2mm]
\texttt{MW-X2}&A\to B,\ B\to C&e_0&
-\eta_{\rm src}\dfrac43\lambda_1\mathbb F^{AB}{}_{ED}.
\end{array}
\tag{K.114}
$$

For each directed matter parent,

$$
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1.
\tag{K.115}
$$

In the opposite $+\mathcal S_1,+\mathcal S_2$ orientation,

$$
+\frac43\lambda_1-\frac13\lambda_1=+\lambda_1.
\tag{K.116}
$$

The matter calculation therefore has unit magnitude per directed flavor
output; it is not the gauge result $-\lambda_1/8$.

## 9. Four previously deferred physics routings

The independent topology/Wick derivation is
`audits/step5k-graph-census-and-four-routes-review.md`.  The four rows are
identified by the stable IDs `BC-TMG-TAIL`, `AC-SOURCE-CYCLE-TAIL`,
`ADDA-I0-SM4`, and `T_(H+H-)`:

$$
\begin{array}{c|c|c}
\text{route}&\text{graph test}&\text{anomaly verdict}\\ \hline
\texttt{BC-TMG-TAIL}&\text{unique vector bridge}&0\\
\texttt{AC-SOURCE-CYCLE-TAIL}&\text{unique source bridge}&0\\
\texttt{ADDA-I0-SM4}&L=2\text{ or one-particle reducible}&0\\
\texttt{T\_(H+H-)}&\text{ordinary nonzero self-energy word; marked bridge}&0.
\end{array}
\tag{K.117}
$$

The last row is not declared zero at the level of its ordinary $D$-word.
Its anomaly projector vanishes because the marked bridge carries only an
external momentum $q$:

$$
\mu_q^2=\bar q^2-q_d^2=0.
\tag{K.118}
$$

## 10. Seventeen-candidate adversarial census

The machine source is `audits/step5k-graph-census-17.json`.  The count is

$$
N_{\rm ghost/FP/NK/measure}=10,
\qquad
N_{\rm artifact}=3,
\qquad
N_{\rm deferred\ routing}=4,
\tag{K.119}
$$

$$
10+3+4=17.
\tag{K.120}
$$

The ten ghost/FP/NK/measure observations are closed by the typed FP incidence
rules, loop number, 1PI bridge test, constant measure density, or absence of
an NK field.  The three artifact observations are repaired by the separate
gauge/matter graph IR and explicit resolvent rows.  The final four are
evaluated individually in Section 9.  No holomorphic-twist coefficient is
used to decide a row.

The census status is

$$
\boxed{
N_{\rm candidates}=17,
\qquad
N_{\rm unresolved}=0.}
\tag{K.121}
$$

## 11. Full accepted $AA$ result and the HT dictionary

The isolated directed gauge seed (K.96), the 48-row local $D$-word/contact
stream, the complete gauge source/contact/external-slot orbit, and the four
matter placements are kept as different objects.  The 48-row stream does
not by itself prove the full gauge coefficient.  That coefficient is the
accepted target-blind typed reconstruction in
`audits/step5-aa-external-slot-decomposition-exact.json`, whose physical
EOM quotient is $\lambda_1(DA_p-AD_p)$.  Combining it with the separately
derived matter rows gives

$$
\boxed{
\begin{aligned}
\Gamma_{AA}^{(1)}
=\lambda_1\mathbb F^{AB}{}_{DE}\Bigg[{}&
\langle D^D,A^E\rangle-\langle A^D,D^E\rangle\\
&+\sum_{r=1}^3
\left(\langle B_r^D,C_r^E\rangle
-\langle C_r^D,B_r^E\rangle\right)
\Bigg].
\end{aligned}}
\tag{K.122}
$$

Let $R_A{}^P$ be the color frame, $U_I{}^r$ the flavor frame,
$S_{\dot a}{}^{\dot b}$ the dotted-spin frame, and $\rho\ne0$ the common
field scale.  The typed Project-to-HT dictionary is

$$
\begin{aligned}
b^A&\mapsto-\frac{i\rho}{\sqrt2}R_A{}^P A^P,\\
\beta_I^A&\mapsto\frac{\rho}{\sqrt2}R_A{}^PU_I{}^rB_r^P,\\
\gamma^{IA}&\mapsto\rho R_A{}^P(U^{-1})_r{}^IC_r^P,\\
\partial_{\dot a}c^A
&\mapsto i\rho R_A{}^PS_{\dot a}{}^{\dot b}D_{\dot b}^P.
\end{aligned}
\tag{K.123}
$$

The formal odd slot $U_{\rm form}$ is defined by

$$
|U_{\rm form}|=1,
\qquad
q_rU_{\rm form}=C_r,
\qquad
P_{\dot a}U_{\rm form}=iD_{\dot a}.
\tag{K.123a}
$$

The differential scale is

$$
Q_{0,\rm HT}\mapsto-\frac12\nabla_-,
\tag{K.123b}
$$

and the frame equations are

$$
R_A{}^PR_B{}^Q\kappa_{PQ}=\delta_{AB},
\qquad
f_{AB}{}^C
=R_A{}^PR_B{}^Qc_{PQ}{}^R(R^{-1})_R{}^C.
\tag{K.123c}
$$

with

$$
C_{\rm Project}^{AB}{}_{DE}=\mathbb F^{AB}{}_{DE}.
\tag{K.124}
$$

In the ordered basis

$$
(D>A,A>D,B_1>C_1,C_1>B_1,
B_2>C_2,C_2>B_2,B_3>C_3,C_3>B_3),
\tag{K.125}
$$

the Project vector is

$$
(1,-1,1,-1,1,-1,1,-1).
\tag{K.126}
$$

The independently translated HT vector is the same:

$$
(1,-1,1,-1,1,-1,1,-1)_{\rm HT}.
\tag{K.127}
$$

Therefore

$$
\boxed{
\Gamma_{AA,\rm one\ loop}^{(1)}
-\Gamma_{AA,\rm HT}^{(1)}=0.}
\tag{K.128}
$$

For $m,n\ge0$ and $0\le k\le m$, $0\le\ell\le n$, the translated
phase in (K.76f) assigns $k$ of the first $m$ derivatives and $\ell$ of the
second $n$ derivatives to the $a$ endpoint.  The number of such choices is
$\binom mk\binom n\ell$; the phase monomial is
$a^{k+\ell}b^{m+n-k-\ell}$.  Therefore the derivative kernel is

$$
\begin{aligned}
K^P_{m,n;k,\ell}
&=2\binom mk\binom n\ell
\int_0^1db\int_0^bda\,
a^{k+\ell}b^{m+n-k-\ell}\\
&=\frac{2\binom mk\binom n\ell}
{(m+n+2)(k+\ell+1)}\\
&=T^{\rm HT,corrected}_{m,n;k,\ell}
=2T^{\rm HT,printed}_{m,n;k,\ell}.
\end{aligned}
\tag{K.129}
$$

This equality is a final comparison only; it is not used as the graph-census
completeness proof.
