# Step-5 target-blind residual-\(q\) projection audit

Authority input: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`.  本 audit 未读取 Step-5 contract、Step-5 engines、HT target。

## 1. Notation

$$
+\equiv 1,\qquad -\equiv 2,\qquad
\epsilon^{+-}=+1,\qquad \epsilon_{+-}=-1.
$$

$$
\varepsilon^{r+}=\eta^r,\qquad
\varepsilon^r_-=\epsilon_{-+}\varepsilon^{r+}=\eta^r,
\qquad \varepsilon^r_+=0,qquad
\widetilde\varepsilon_{\mathcal I\dot a}=0.
$$

\(Q^r_{E,+}\) denotes the locked Euclidean generator selected by this parameter.  Define the compact normalization

$$
q_r:=\frac1{\sqrt2}Q^r_{E,+}.
$$

This factor is a declared convention: it is the unique positive rescaling for which \(q_rB_s=-i\delta_{rs}A\).  Step 4C fixes \(Q^r_{E,+}\), not this extra rescaling.

For adjoint color \(A\), define vector-frame bottom letters

$$
\begin{aligned}
A^A&:=\left.\boldsymbol\nabla^{\mathsf V}_{E,+}
\boldsymbol{\mathcal W}^{\mathsf V,A}_{E,+}\right|,\\
B_r^A&:=\left.\boldsymbol\nabla^{\mathsf V}_{E,+}
\boldsymbol\Phi^{\mathsf V,A}_r\right|,\\
C_r^A&:=\left.\widetilde{\boldsymbol\Phi}^{\mathsf V,A}_r\right|,\\
D_{\dot a}^A&:=\left.\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V,A}_{E,\dot a}\right|,\\
P_{\dot a}X^A&:=(\sigma_E^m)_{+\dot a}(\mathcal D_mX)^A.
\end{aligned}
$$

Thus, without suppressed color contraction,

$$
(P_{\dot a}C_r)^A
=(\sigma_E^m)_{+\dot a}
\left(\partial_mC_r^A+c_{BC}{}^AA_m^BC_r^C\right).
$$

The vertical bar is essential.  Sources: Step 1 lines 20--44, 475--543; Step 3B lines 30--40, 488--515; Step 3C lines 291--304, 1080--1215; Step 3D (3D.43)--(3D.44); Step 4 lines 268--366, 413--447; Step 4C lines 827--894.

## 2. Exact component projections

Step 3B gives

$$
B_r=\sqrt2\,\psi_{r+},\qquad
C_r=\widetilde\phi_r,\qquad
D_{\dot a}=i\widetilde\lambda_{\dot a}.
$$

Lower the second index of \(\sigma_E^{mn}\):

$$
(\sigma_E^{mn})_{ab}
:=(\sigma_E^{mn})_a{}^c\epsilon_{cb}.
$$

Direct multiplication of the locked matrices gives

$$
\begin{array}{c|rrrrrr}
mn&12&13&14&23&24&34\\ \hline
(\sigma_E^{mn})_{++}
&0&-\frac12&-\frac i2&\frac i2&-\frac12&0
\end{array}
$$

Since both ordered \((m,n)\) slots are summed,

$$
\begin{aligned}
A
&=-i(\sigma_E^{mn})_{++}F_{mn}\\
&=-2i\left[
-\frac12F_{13}-\frac i2F_{14}
+\frac i2F_{23}-\frac12F_{24}
\right]\\
&=iF_{13}-F_{14}+F_{23}+iF_{24}.
\end{aligned}
$$

The same matrices give, for every \(m,\dot a\),

$$
\sum_{n=1}^4(\sigma_E^{mn})_{++}(\sigma_E^n)_{+\dot a}=0.
$$

The two dotted derivative slots are

$$
P_{\dot1}=\mathcal D_4-i\mathcal D_3,
\qquad
P_{\dot2}=-i\mathcal D_1-\mathcal D_2.
$$

## 3. Raw locked-generator action

### 3.1 \(Q^r_{E,+}A=0\)

With \(\widetilde\varepsilon=0\), (4C.44) gives

$$
\delta F_{mn}
=\eta^r\left[(\sigma_{E,n})_{+\dot a}
\mathcal D_m\widetilde\psi_r^{\dot a}
-(\sigma_{E,m})_{+\dot a}
\mathcal D_n\widetilde\psi_r^{\dot a}\right].
$$

Therefore

$$
\delta A
=-2i\eta^r(\sigma_E^{mn})_{++}
(\sigma_{E,n})_{+\dot a}
\mathcal D_m\widetilde\psi_r^{\dot a}=0.
$$

### 3.2 \(Q^r_{E,+}B_s=-i\sqrt2\delta_{rs}A\)

Equation (4C.46), at \(a=+\), gives

$$
\delta\psi_{s+}
=-(\sigma_E^{mn})_+{}^b\varepsilon_b^sF_{mn}
+\mathcal M^s{}_t\varepsilon_+^t.
$$

The selected parameter has \(\varepsilon_-^r=\eta^r\) and \(\varepsilon_+^r=0\).  Hence

$$
\delta\psi_{s+}
=-\eta^r\delta_{rs}(\sigma_E^{mn})_+{}^-
F_{mn}
=-\eta^r\delta_{rs}(\sigma_E^{mn})_{++}F_{mn}.
$$

The nonlinear \(\mathcal M\)-term vanishes exactly.  Using \((\sigma_E^{mn})_{++}F_{mn}=iA\),

$$
Q^r_{E,+}B_s
=\sqrt2Q^r_{E,+}\psi_{s+}
=-i\sqrt2\delta_{rs}A.
$$

### 3.3 \(Q^r_{E,+}C_s=-\varepsilon_{rst}B_t\)

From (4C.45a), \(C_s=\widetilde\varphi_{s4}\), and \(\epsilon_{s4rt}=\varepsilon_{srt}=-\varepsilon_{rst}\),

$$
\begin{aligned}
\delta C_s
&=\sqrt2\epsilon_{s4rt}\eta^r\Lambda_+^t\\
&=\epsilon_{s4rt}\eta^rB_t\\
&=-\eta^r\varepsilon_{rst}B_t.
\end{aligned}
$$

### 3.4 \(Q^r_{E,+}D_{\dot a}=-i\sqrt2P_{\dot a}C_r\)

For \(\mathcal I=4\), (4C.47) and \(\widetilde\varphi_{4r}=-C_r\) give

$$
\delta\widetilde\lambda_{\dot a}
=-\sqrt2\eta^r(\sigma_E^m)_{+\dot a}
\mathcal D_mC_r.
$$

Thus

$$
Q^r_{E,+}D_{\dot a}
=iQ^r_{E,+}\widetilde\lambda_{\dot a}
=-i\sqrt2P_{\dot a}C_r.
$$

## 4. Compact-normalized action and closure

Dividing the four raw identities by \(\sqrt2\),

$$
\boxed{
\begin{aligned}
q_rA&=0,\\
q_rB_s&=-i\delta_{rs}A,\\
q_rC_s&=-\frac1{\sqrt2}\varepsilon_{rst}B_t,\\
q_rD_{\dot a}&=-iP_{\dot a}C_r.
\end{aligned}}
$$

For \(A,B,C\), direct composition gives

$$
\begin{aligned}
\{q_r,q_s\}A&=0,\\
\{q_r,q_s\}B_t&=0,\\
\{q_r,q_s\}C_t
&=\frac i{\sqrt2}
(\varepsilon_{str}+\varepsilon_{rts})A=0.
\end{aligned}
$$

For \(D_{\dot a}\), use the complete closure (4C.69b)--(4C.69g), not an assumed commutation with \(\mathcal D_m\).  The selected parameters obey

$$
\widetilde\varepsilon=0,\qquad
\varepsilon_1^a\varepsilon_{2a}=0,\qquad
\varepsilon_+=0.
$$

Consequently

$$
v_E^m=0,\qquad
\Omega_E=0,\qquad
\mathscr R_{E,+}^{\mathcal I}=0,\qquad
\widetilde{\mathscr R}_{E,\dot a\mathcal I}=0,
$$

and therefore

$$
\boxed{\{q_r,q_s\}=0}
$$

on all four bottom-letter families, without auxiliary or fermion EOM.  This is exact restricted letter-off-shell closure.  It is not a finite off-shell \(SU(4)_R\)-covariant completion of the full \(\mathcal N=4\) multiplet; Step 4C.10 explicitly does not assert such a completion.

## 5. Compact physical weights

Let \(\theta_r\) be inert odd variables, \(\partial_r^L\theta_s=\delta_{rs}\), and let \(q_r\) be an odd left derivation.  Write

$$
\mathcal C_{\rm phys}(\theta)
=a\theta_sC_s
+\frac b2\varepsilon_{stu}\theta_s\theta_tB_u
+c\theta_1\theta_2\theta_3A.
$$

Then

$$
q_r\mathcal C_{\rm phys}
=\partial_r^L\mathcal C_{\rm phys}-aC_r
$$

requires

$$
q_rC_s=-\frac ba\varepsilon_{rst}B_t,
\qquad
q_rB_s=\frac cb\delta_{rs}A.
$$

Set \(a=1\).  The proved action gives the unique pair

$$
b=\frac1{\sqrt2},
\qquad
c=-\frac i{\sqrt2}.
$$

Hence

$$
\boxed{
\mathcal C_{\rm phys}(\theta)
=\theta_rC_r
+\frac1{2\sqrt2}\varepsilon_{rst}
\theta_r\theta_sB_t
-\frac i{\sqrt2}\theta_1\theta_2\theta_3A.}
$$

## 6. Exact boundary

The following completion is conditional:

$$
q_rU=C_r,
\qquad
P_{\dot a}U=iD_{\dot a},
\qquad
[q_r,P_{\dot a}]U=0.
$$

Under these three assumptions,

$$
\mathcal C(\theta)
=U+\theta_rC_r
+\frac1{2\sqrt2}\varepsilon_{rst}
\theta_r\theta_sB_t
-\frac i{\sqrt2}\theta_1\theta_2\theta_3A
$$

satisfies \(q_r\mathcal C=\partial_r^L\mathcal C\), and \(q_rD_{\dot a}=-iP_{\dot a}C_r\).  Step 3D defines \((\mathfrak c_R,\widetilde{\mathfrak c}_R,\mathbf s_R)\) in (3D.43)--(3D.44), but no \(U\), \(q_rU\), or \(P_{\dot a}U\).  This completion is `BLOCKED_U_NOT_DEFINED_BY_LOCKED_INPUTS`.

The boxed four-arrow action is not a full \(N=1\) superfield identity.  Equation (4C.35a) makes \(\delta_E\widetilde\Phi_r\) antichiral, while

$$
\bar{\boldsymbol\nabla}_{E,\dot a}
\boldsymbol\nabla_{E,+}\boldsymbol\Phi_r
=\{\bar{\boldsymbol\nabla}_{E,\dot a},
\boldsymbol\nabla_{E,+}\}\boldsymbol\Phi_r
=-2(\sigma_E^m)_{+\dot a}
\boldsymbol{\mathcal D}_{E,m}\boldsymbol\Phi_r
$$

is generically nonzero by (3C.23).  Therefore the full-superfield lift is `PROVED_REJECTED`; only the bottom/twisted-letter projection is proved.

## 7. Machine audit

$$
N_{\rm pass}=22,
\qquad
N_{\rm fail}=0.
$$

Verdict: `PROVED_BOTTOM_PROJECTION_WITH_CONDITIONAL_COMPACT_COMPLETION`.

Input SHA-256:

- `contracts/foundations/step-01-supersymmetry-commutator.md`: `a73d8017c2d07de578f4f98ea25054033b0384ebffb6b426650a22f404c3231b`
- `contracts/foundations/step-03b-component-reconstruction.md`: `4b3ae678463747cc78d3c7e594904647620d919eae769c5b5bfd16d5b556a75b`
- `contracts/foundations/step-03c-gauge-vector-representation.md`: `c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1`
- `contracts/foundations/step-04-extended-sym-notation.md`: `3fcf7e242928d3512c02059d8c28d9551b5cb86156f9d6259cd2bba713211d27`
- `contracts/foundations/step-04c-n4-super-yang-mills.md`: `fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f`
- `contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md`: `109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538`
