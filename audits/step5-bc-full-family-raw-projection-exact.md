# Step 5 ordered $(B_r>C_s)$ and $(C_s>B_r)$: regulated Schwinger orbit

Status: `PASS_BC_CB_REGULATED_SD_KONISHI_EXACT`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`.

No holomorphic-twist coefficient or compact-result coefficient is used.

## 1. Notation and parity

$$
B_r^A:=(\boldsymbol\nabla_+\boldsymbol\Phi_r)^A|,
\qquad
C_s^B:=\widetilde{\boldsymbol\Phi}_s^B|,
\qquad
D_{\dot a}^D:=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}^D|.
$$

$$
|B_r|=1,
\qquad
|C_s|=0,
\qquad
|\boldsymbol\nabla_-|=1.
$$

$$
d=4-2\epsilon,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2,
\qquad
D_i:=r_{i,d}^2.
$$

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}
:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}.
$$

For odd dotted spinors,

$$
\langle X^D,Y^E\rangle
:=X_{\dot a}^D Y^{E\dot a}
=X_{\dot2}^D Y_{\dot1}^E-X_{\dot1}^D Y_{\dot2}^E.
$$

## 2. Ordered action variation and the three occurrence tags

The matter and antichiral-superpotential terms of the Euclidean action are

$$
S_{E,m}
=-h\int d^8z\,
\kappa_{AB}\widetilde\Phi_t^A(\mathcal E_{\rm ad})^B{}_C\Phi_t^C,
$$

$$
S_{E,\widetilde U}
=+\frac{\sqrt2h}{6}\int d^6\bar z\,
\varepsilon_{tuv}c_{ABC}
\widetilde\Phi_t^A\widetilde\Phi_u^B\widetilde\Phi_v^C.
$$

For an antichiral variation,

$$
\begin{aligned}
\delta S_{E,m}
&=-h\int d^8z\,\delta\widetilde\Phi_r^A
(\mathcal E_{\rm ad}\Phi_r)_A\\
&=+\frac h4\int d^6\bar z\,
\delta\widetilde\Phi_r^A(\boldsymbol\nabla^2\boldsymbol\Phi_r)_A,
\end{aligned}
$$

and direct ordered differentiation of all three cubic slots gives

$$
\begin{aligned}
\frac{\vec\delta S_{E,\widetilde U}}
{\delta\widetilde\Phi_r^A}
&=\frac{\sqrt2h}{6}(1+1+1)
\varepsilon_{rtu}c_{ABC}
\widetilde\Phi_t^B\widetilde\Phi_u^C\\
&=\frac h{\sqrt2}\varepsilon_{rtu}
(\widetilde\Phi_t\times\widetilde\Phi_u)_A.
\end{aligned}
$$

Hence

$$
\boxed{
\frac{\vec\delta S_E}{\delta\widetilde\Phi_r^A}
=-h\,\mathscr E_{\widetilde r,A}}
$$

with

$$
\boxed{
\mathscr E_{\widetilde r}^A
=-\frac14(\boldsymbol\nabla^2\boldsymbol\Phi_r)^A
-\frac1{\sqrt2}\varepsilon_{rtu}
(C_t\times C_u)^A.}
$$

The kinetic source must be expanded covariantly before graph enumeration.  With

$$
\Gamma_a:=e^{-V}D_ae^V
=D_aV+\frac12[D_aV,V]+O(V^3),
\qquad
\nabla_a=D_a+\Gamma_a,
$$

graded Leibniz expansion on the even column $\Phi_r$ gives

$$
\begin{aligned}
\nabla^2\Phi_r
&=(D^a+\Gamma^a)(D_a\Phi_r+\Gamma_a\Phi_r)\\
&=D^2\Phi_r
+(D^a\Gamma_a)\Phi_r
-\Gamma_aD^a\Phi_r
+\Gamma^aD_a\Phi_r
+\Gamma^a\Gamma_a\Phi_r\\
&=\boxed{
D^2\Phi_r
+2\Gamma^aD_a\Phi_r
+(D^a\Gamma_a)\Phi_r
+\Gamma^a\Gamma_a\Phi_r}.
\end{aligned}
$$

Here

$$
\Gamma_aD^a=-\Gamma^aD_a.
$$

Therefore

$$
\frac12(\nabla^2\Phi_r)C_s
=\mathcal I_0+\mathcal I_1+\mathcal I_2+O(V^3),
$$

with

$$
\mathcal I_0
=\frac12(D^2\Phi_r)C_s,
$$

$$
\mathcal I_1
=\left[
(D^aV)D_a\Phi_r
+\frac12(D^2V)\Phi_r
\right]C_s,
$$

$$
\begin{aligned}
\mathcal I_2
=\Big[&
\frac12[D^aV,V]D_a\Phi_r
+\frac14D^a[D_aV,V]\Phi_r\\
&+\frac12(D^aV)(D_aV)\Phi_r
\Big]C_s.
\end{aligned}
$$

The complete order-$V^2$ regulated orbit is

$$
\boxed{
\mathcal I_0\frac1{2!}M_1M_1
\;\oplus\;
\mathcal I_1M_1
\;\oplus\;
\mathcal I_0M_2
\;\oplus\;
\mathcal I_2,}
$$

where $M_1$ and $M_2$ are respectively the $V$ and $V^2/2$ terms of $\widetilde\Phi e^V\Phi$.  These are the triangle parent, nonlinear-source/collapsed contact, matter seagull, and source seagull rows.  Their covariant sum is the coincident kernel $K_-$ computed below.

The tree descendant is

$$
\boldsymbol\nabla_-B_r^A
=-2\mathscr E_{\widetilde r}^A
-\sqrt2\varepsilon_{rtu}(C_t\times C_u)^A.
$$

It must be expanded into three separately tagged occurrences:

$$
\begin{aligned}
\mathcal I_{E,\mathrm{kin}}^{AB}
&:=+\frac12(\boldsymbol\nabla^2\boldsymbol\Phi_r)^A C_s^B,\\
\mathcal I_{E,\mathrm{pot}}^{AB}
&:=+\sqrt2\varepsilon_{rtu}(C_t\times C_u)^A C_s^B,\\
\mathcal I_{X,\mathrm{pot}}^{AB}
&:=-\sqrt2\varepsilon_{rtu}(C_t\times C_u)^A C_s^B.
\end{aligned}
$$

The last two rows have identical regulated contact kernels and opposite source coefficients.  Neither contains an inverse kinetic square.  Therefore, only after both rows have been retained,

$$
\mathcal R_\epsilon\mathcal I_{E,\mathrm{pot}}^{AB}
+\mathcal R_\epsilon\mathcal I_{X,\mathrm{pot}}^{AB}
=\sqrt2K_{\mathrm{pot}}-\sqrt2K_{\mathrm{pot}}=0.
$$

The kinetic Euler occurrence cannot be deleted with them.

## 3. Regulated Schwinger equation

For the ordered $(B_r^A>C_s^B)$ source define the even configuration-space vector field

$$
X_{rs}^{AB}
:=\widetilde\Phi_s^B(z)
\frac{\vec\delta}{\delta\widetilde\Phi_r^A(z)}.
$$

$X_{rs}^{AB}$ has support only on the integrated $\widetilde\Phi$ block.  Its vector, FP, NK, and non-minimal components are identically zero, so no gauge or ghost Jacobian is part of this ordered channel.

The Euclidean exponent has $\tau_E=-1/\hbar$.  Equation (3D.34) gives

$$
0=\left\langle
\operatorname{div}_{E,\epsilon}X_{rs}^{AB}
-\frac1\hbar X_{rs}^{AB}(S_E)
\right\rangle.
$$

Using $\vec\delta S_E/\delta\widetilde\Phi_r=-h\mathscr E_{\widetilde r}$,

$$
\begin{aligned}
0
&=\left\langle
\operatorname{div}_{E,\epsilon}X_{rs}^{AB}
+\frac h\hbar C_s^B\mathscr E_{\widetilde r}^A
\right\rangle,\\
\left\langle C_s^B\mathscr E_{\widetilde r}^A\right\rangle
&=-\hbar g^2
\left\langle\operatorname{div}_{E,\epsilon}X_{rs}^{AB}\right\rangle.
\end{aligned}
$$

The differentiated insertion fixes the flavor tensor before any loop calculation:

$$
\frac{\vec\delta\widetilde\Phi_s^B}
{\delta\widetilde\Phi_r^A}
=\delta_{rs}\delta_A{}^B\delta_-,
$$

so

$$
\operatorname{div}_{E,\epsilon}X_{rs}^{AB}
=\delta_{rs}K_{-,\epsilon}^{AB}(z,z).
$$

Thus $r\ne s$ is zero independently of any external target.

## 4. Exact antichiral symbol trace

The coefficient of the symbol is fixed by the locked covariant projector, not imported from a heat-kernel formula.  Equation (3A.78), divided by its closed-projector factor $16$, gives

$$
\boxed{
\frac1{16}\nabla_E^{\leftarrow2}\bar D_E^2U_E
=\mathcal D_{E,m}^{\leftarrow}\mathcal D_E^{m\leftarrow}U_E
{}-(\bar D_{E\dot b}U_E)
\widehat{\widetilde{\mathcal W}}_E^{\dot b}
{}-\frac12U_E\nabla_E^a\mathcal W_{Ea}.}
$$

The $\widetilde{\mathcal W}^2$ coefficient has exactly two copies of the middle term.  Its squared coefficient is

$$
(-1)(-1)=+1.
$$

The last term contains no odd antichiral Fourier variable and cannot saturate the $d^2\bar\pi$ trace contributing to $\widetilde{\mathcal W}^2$.  Therefore the normalized ultraviolet symbol is exactly $\Xi_D$ below, with no unrecorded factor.

Let $\bar\pi^{\dot1},\bar\pi^{\dot2}$ be the odd Fourier variables of the antichiral delta.  Define the even symbol

$$
\Xi_D
:=\widetilde{\mathcal W}_{\dot a}^D\bar\pi^{\dot a}
=\widetilde{\mathcal W}_{\dot1}^D\bar\pi^{\dot1}
+\widetilde{\mathcal W}_{\dot2}^D\bar\pi^{\dot2}.
$$

All four $\widetilde{\mathcal W}$ and $\bar\pi$ generators are odd.  Hence

$$
\begin{aligned}
\Xi_D\Xi_E
={}&
\widetilde{\mathcal W}_{\dot1}^D\bar\pi^{\dot1}
\widetilde{\mathcal W}_{\dot2}^E\bar\pi^{\dot2}
+
\widetilde{\mathcal W}_{\dot2}^D\bar\pi^{\dot2}
\widetilde{\mathcal W}_{\dot1}^E\bar\pi^{\dot1}\\
={}&
\left(
-\widetilde{\mathcal W}_{\dot1}^D
\widetilde{\mathcal W}_{\dot2}^E
+\widetilde{\mathcal W}_{\dot2}^D
\widetilde{\mathcal W}_{\dot1}^E
\right)
\bar\pi^{\dot1}\bar\pi^{\dot2}\\
={}&
\left\langle
\widetilde{\mathcal W}^D,
\widetilde{\mathcal W}^E
\right\rangle
\bar\pi^{\dot1}\bar\pi^{\dot2}.
\end{aligned}
$$

With

$$
\int d\bar\pi^{\dot2}d\bar\pi^{\dot1}
\bar\pi^{\dot1}\bar\pi^{\dot2}=1,
$$

the exact dotted trace is

$$
\boxed{
\int d^2\bar\pi\,\Xi_D\Xi_E
=\left\langle
\widetilde{\mathcal W}^D,
\widetilde{\mathcal W}^E
\right\rangle.}
$$

For one color label,

$$
\Xi_D^2
=-2\widetilde{\mathcal W}_{\dot1}^D
\widetilde{\mathcal W}_{\dot2}^D
\bar\pi^{\dot1}\bar\pi^{\dot2}
=\widetilde{\mathcal W}^{D\dot a}
\widetilde{\mathcal W}_{\dot a}^D
\bar\pi^{\dot1}\bar\pi^{\dot2}.
$$

The quadratic Dyson coefficient is $1/2!$.  The four-dimensional Gaussian is

$$
\int\frac{d^4L}{(2\pi)^4}e^{-L^2/M^2}
=\frac{M^4}{16\pi^2}.
$$

Therefore the coincident quadratic coefficient is

$$
\frac1{2M^4}\frac{M^4}{16\pi^2}
=\frac1{32\pi^2}.
$$

This fixes the normalization of the same coefficient obtained below from the DRED cutting failure.

## 5. DRED cutting failure

The marked linear $B$ source has the exact edge word

$$
\begin{aligned}
\mathcal M_B(r_e)\delta_e
&:=D_-D_+\bar D^2D^2\delta_e\\
&=\frac12D^2\bar D^2D^2\delta_e\\
&=8\bar r_e^2D^2\delta_e.
\end{aligned}
$$

Including the constrained matter-propagator factor gives

$$
\frac{\mathcal M_B(r_e)\delta_e}{16D_0}
=\frac12\frac{\bar r_e^2}{D_0}D^2\delta_e.
$$

The full-$d$ Schwinger contact is

$$
\frac12D^2\delta_e
=\frac12\frac{r_{e,d}^2}{D_0}D^2\delta_e.
$$

Their difference is

$$
\boxed{
\frac12\frac{\mu_\ell^2}{D_0}D^2\delta_e.}
$$

With the antichiral constrained delta

$$
\delta_-:=-\frac14D^2\delta_e,
$$

this is

$$
-2\frac{\mu_\ell^2}{D_0}\delta_-.
$$

The factor $2$ is the same factor obtained from the descendant $-2\mathscr E_{\widetilde r}$ in the Schwinger equation; it is not an additional graph multiplicity.

On the selected Euler edge,

$$
\bar r_e^2=r_{e,d}^2+\mu_\ell^2,
\qquad
D_0=r_{e,d}^2.
$$

If the $D$-algebra square were the full loop square, the Schwinger cut would vanish exactly:

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{D_1D_2}
=0.
$$

The spinor $D$-algebra supplies the four-dimensional square instead.  Thus

$$
\begin{aligned}
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{D_1D_2}
&=\frac{\bar r_e^2-r_{e,d}^2}{D_0D_1D_2}\\
&=\boxed{
\frac{\mu_\ell^2}{D_0D_1D_2}}.
\end{aligned}
$$

Feynman parametrization and the shift $L=\ell+xp+yq$ give

$$
\begin{aligned}
J_{\mu^2}(\epsilon,\Delta)
&:=\mu_R^{2\epsilon}
\int\frac{d^{4-2\epsilon}L}{(2\pi)^{4-2\epsilon}}
\frac{\mu_L^2}{(L^2+\Delta)^3}\\
&=\frac{\epsilon\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\left(\frac{\mu_R^2}{\Delta}\right)^\epsilon.
\end{aligned}
$$

Since

$$
\epsilon\Gamma(\epsilon)=\Gamma(1+\epsilon),
\qquad
\Gamma(1)=1,
$$

one obtains

$$
\boxed{
\lim_{\epsilon\to0}J_{\mu^2}(\epsilon,\Delta)
=\frac1{32\pi^2}.}
$$

There is no graph-specific factor $4-d$.  The finite number is entirely the evanescent square multiplying the logarithmic ultraviolet residue.

## 6. Color and ordered source factors

For $(B_r^A>C_s^B)$ the open adjoint chain is

$$
\begin{aligned}
(T_D)^A{}_Z(T_E)^Z{}_C\kappa^{CB}
&=-c_{DZA}c_{EBZ}\\
&=c_{AZD}c_{BZE}\\
&=\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

For the independently routed reverse source $(C_s^A>B_r^B)$,

$$
\begin{aligned}
(T_E)^B{}_Z(T_D)^Z{}_C\kappa^{CA}
&=-c_{EZB}c_{DAZ}\\
&=c_{BZE}c_{AZD}\\
&=\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

The interaction-copy factor is

$$
\frac1{2!}(1+1)=1.
$$

Combining the dotted symbol, color chain, and DRED master,

$$
\boxed{
K_{-,\epsilon}^{AB}(z,z)\big|_{\widetilde{\mathcal W}^2}
=\frac1{32\pi^2}\mathbb F^{AB}{}_{DE}
\left\langle
\widetilde{\mathcal W}^D,
\widetilde{\mathcal W}^E
\right\rangle.}
$$

## 7. Ordered results

For $(B_r^A>C_s^B)$,

$$
\begin{aligned}
\left\langle-2\mathscr E_{\widetilde r}^A C_s^B\right\rangle_{\rm ev}
&=+2\delta_{rs}\hbar g^2
K_{-,\epsilon}^{AB}(z,z)\big|_{\widetilde{\mathcal W}^2}\\
&=2\delta_{rs}\hbar g^2
\frac1{32\pi^2}
\mathbb F^{AB}{}_{DE}
\left\langle
\widetilde{\mathcal W}^D,
\widetilde{\mathcal W}^E
\right\rangle\\
&=\delta_{rs}\lambda_1
\mathbb F^{AB}{}_{DE}
\left\langle
\widetilde{\mathcal W}^D,
\widetilde{\mathcal W}^E
\right\rangle.
\end{aligned}
$$

Using $\widetilde{\mathcal W}_{\dot a}|=D_{\dot a}$,

$$
\boxed{
\Delta(B_r^A,C_s^B)
=\delta_{rs}\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,D^E\rangle.}
$$

Because $|C_s|=0$ and $\boldsymbol\nabla_-C_s=0$,

$$
\boldsymbol\nabla_-(C_s^AB_r^B)
=C_s^A\boldsymbol\nabla_-B_r^B.
$$

The independent reverse Schwinger vector field and reverse color chain therefore give

$$
\boxed{
\Delta(C_s^A,B_r^B)
=\delta_{rs}\lambda_1\mathbb F^{AB}{}_{DE}
\langle D^D,D^E\rangle.}
$$

Thus

$$
r=s:\quad c_{BC}=c_{CB}=1,
$$

$$
r\ne s:\quad c_{BC}=c_{CB}=0.
$$

## 8. Exact location of the old error

The ordinary bottom-component two-Yukawa census remains correct:

$$
G_{\phi_r\widetilde\psi_s}=0,
\qquad
G_{\psi_r\widetilde\phi_s}=0,
$$

so there is no ordinary component triangle made from two external-$D$ Yukawa vertices and the bottom sources $(B_r,C_s)$.

That statement does not evaluate the Schwinger occurrence.  The latter first differentiates the coincident insertion:

$$
\widetilde\Phi_s^B
\frac{\vec\delta}{\delta\widetilde\Phi_r^A}
\longrightarrow
\delta_{rs}K_{-,\epsilon}^{AB}(z,z),
$$

and only then takes the bottom projection

$$
K_{-,\epsilon}\big|_{\widetilde{\mathcal W}^2}
\longrightarrow
\langle D,D\rangle.
$$

No $\phi\!\to\!\widetilde\psi$ or $\psi\!\to\!\widetilde\phi$ propagator occurs in this orbit.  The previous zero incorrectly promoted an ordinary-Wick-parent obstruction to a statement about the regulated density divergence.

The second error was the pre-regulator replacement

$$
-2\mathscr E_{\widetilde r}
-\sqrt2\varepsilon_{rtu}(C_t\times C_u)
\longrightarrow
\frac12\boldsymbol\nabla^2\boldsymbol\Phi_r.
$$

This replacement erases the occurrence tag on the Euler operator before the Schwinger derivative acts.  The correct order is

$$
\boxed{
\text{Euler occurrence}
\;\oplus\;
\text{Euler-potential occurrence}
\;\oplus\;
\text{explicit-potential occurrence}
\xrightarrow{\ \mathrm{SD}+\mathcal R_\epsilon\ }
\text{pair the two potential rows}
\;\oplus\;
K_{-,\epsilon}.}
$$

Verification:

    python scripts/step5_bc_full_family_raw_projection_audit.py --check

Expected:

    84/84 PASS
    PASS_BC_CB_REGULATED_SD_KONISHI_EXACT
