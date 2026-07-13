# Step 5A frame-bridge intertwiner audit

Status: `PASS_EXACT_CERTIFICATES_WITH_OPEN_FULL_BV_GATE`

## 1. Three distinct maps

$$
\mathcal O_{\mathsf C}=\mathcal B^{-1}\mathcal O_{\mathsf V}\mathcal B,
\qquad
o_{\mathsf V}=A_{\mathcal B}o_{\mathsf C},
\qquad
A_{\mathcal B}=\operatorname{Ad}_{\mathcal B}.
$$

$$
\boldsymbol{\mathcal W}_{\mathsf V}
=\mathcal B\mathcal W_{\mathsf C}\mathcal B^{-1},
\qquad
\widetilde{\boldsymbol{\mathcal W}}_{\mathsf V}
=\widetilde{\mathcal B}^{-1}
\widetilde{\mathcal W}_{\mathsf A}
\widetilde{\mathcal B}.
$$

$$
\zeta_{\mathsf V}
=\mathbb T_{\rm q}(\overline Q_{\mathsf C},\zeta_{\mathsf C}),
\qquad
J_{\rm q}
=\left.\frac{\vec\partial\zeta_{\mathsf V}}
{\partial\zeta_{\mathsf C}}\right|_{\overline Q_{\mathsf C}}.
$$

$$
\boldsymbol\varpi_{\mathsf V}(x_{\mathsf V})
=\boldsymbol\varpi_{\mathsf C}(\mathbb T^{-1}x_{\mathsf V})
\operatorname{Ber}\!\left(
\frac{\vec\partial x_{\mathsf C}}{\partial x_{\mathsf V}}
\right).
$$

These are respectively an operator similarity, a quantum-coordinate tangent
map, and a full density pushforward.  They are not interchangeable.

## 2. General adjoint identity and one exact coefficient witness

For every invertible Project bridge,

$$
\begin{aligned}
\operatorname{Ad}_{\mathcal B}(X)
\operatorname{Ad}_{\mathcal B}(Y)
&=(\mathcal B X\mathcal B^{-1})(\mathcal B Y\mathcal B^{-1})\\
&=\mathcal B X(\mathcal B^{-1}\mathcal B)Y\mathcal B^{-1}\\
&=\mathcal B XY\mathcal B^{-1}
=\operatorname{Ad}_{\mathcal B}(XY),\\
[\operatorname{Ad}_{\mathcal B}(X),
\operatorname{Ad}_{\mathcal B}(Y)]
&=\operatorname{Ad}_{\mathcal B}([X,Y]).
\end{aligned}
$$

This ordered proof is independent of the gauge algebra.  The following
coefficient matrix is one exact
`SU2_NILPOTENT_WITNESS`; it is not a proof for every gauge algebra.

$$
\tau:=\vartheta^1\vartheta^2,
\qquad
\epsilon(\tau)=0,
\qquad
\tau^2=0,
\qquad
\mathcal B
=\begin{pmatrix}1+\tau/2&0\\0&1-\tau/2\end{pmatrix},
\qquad
\mathcal B^{-1}
=\begin{pmatrix}1-\tau/2&0\\0&1+\tau/2\end{pmatrix}.
$$

$$
A_{\mathcal B}
=\begin{pmatrix}
1&-i\tau&0\\
i\tau&1&0\\
0&0&1
\end{pmatrix},
\qquad
A_{\mathcal B}^{-1}=A_{\mathcal B}\big|_{\tau\mapsto-\tau},
\qquad
\det A_{\mathcal B}=1.
$$

On the displayed witness sector, the coefficient map acts on

$$
\operatorname{Adj}_{SU(2)}\otimes
\Lambda(\vartheta^1,\vartheta^2,
\bar\vartheta_{\dot1},\bar\vartheta_{\dot2}),
\qquad
\dim\!\left[
\operatorname{Adj}_{SU(2)}\otimes
\Lambda(\vartheta^1,\vartheta^2,
\bar\vartheta_{\dot1},\bar\vartheta_{\dot2})
\right]=48.
$$

It is parity preserving.  Its two parity blocks obey

$$
\det A_{\bar0}=1,
\qquad
\det A_{\bar1}=1,
\qquad
\operatorname{Ber}A_{\mathcal B}=1.
$$

This proves reference-flat measure invariance only for this covariant adjoint
Step-5A block.

## 3. Quadratic tensors and source insertion

For an affine tangent map, or on a background satisfying both displayed
first-jet conditions,

$$
E_{\mathsf V,\alpha}C^\alpha{}_{ij}=0,
\qquad
F_{\mathsf V,\alpha}C^\alpha{}_{ij}=0,
\qquad
F_{\mathsf V,\alpha}
:=\frac{\vec\partial\mathscr I_{\mathsf V}}
{\partial\zeta_{\mathsf V}^{\alpha}},
$$

$$
\begin{aligned}
\Omega_{\mathsf C}&=J_{\rm q}^{\mathrm{st}}\Omega_{\mathsf V}J_{\rm q},\\
K_{\mathsf C}&=J_{\rm q}^{\mathrm{st}}K_{\mathsf V}J_{\rm q},\\
G_{\mathsf C}&=J_{\rm q}^{-1}G_{\mathsf V}J_{\rm q}^{-\mathrm{st}},\\
I^{\rm bil}_{\mathsf C}
&=J_{\rm q}^{\mathrm{st}}I^{\rm bil}_{\mathsf V}J_{\rm q},\\
H_{\mathsf C}&=J_{\rm q}^{-1}H_{\mathsf V}J_{\rm q},\\
I^{\rm op}_{\mathsf C}
&=J_{\rm q}^{-1}I^{\rm op}_{\mathsf V}J_{\rm q}.
\end{aligned}
$$

Therefore

$$
G_{\mathsf C}I^{\rm bil}_{\mathsf C}
=J_{\rm q}^{-1}
(G_{\mathsf V}I^{\rm bil}_{\mathsf V})J_{\rm q},
\qquad
\operatorname{STr}(G_{\mathsf C}I^{\rm bil}_{\mathsf C})
=\operatorname{STr}(G_{\mathsf V}I^{\rm bil}_{\mathsf V}).
$$

For a nonlinear quantum map the exact Hessian is

$$
K_{\mathsf C,ij}
=(J_{\rm q}^{\mathrm{st}})_i{}^\alpha
K_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+E_{\mathsf V,\alpha}C^\alpha{}_{ij}.
$$

For a scalar source composite its quadratic insertion obeys separately

$$
I^{\rm bil}_{\mathsf C,ij}
=(J_{\rm q}^{\mathrm{st}})_i{}^\alpha
I^{\rm bil}_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+F_{\mathsf V,\alpha}C^\alpha{}_{ij}.
$$

The executable counterexample gives

$$
K_{\mathsf V}=\begin{pmatrix}2&1\\1&4\end{pmatrix},
\qquad
E_{\mathsf V}=\begin{pmatrix}3&5\end{pmatrix},
\qquad
E_{\mathsf V,\alpha}C^\alpha
=\begin{pmatrix}5&0\\0&0\end{pmatrix},
$$

$$
K_{\mathsf C}
=\begin{pmatrix}2&1\\1&4\end{pmatrix}
+\begin{pmatrix}5&0\\0&0\end{pmatrix}
=\begin{pmatrix}7&1\\1&4\end{pmatrix}.
$$

For

$$
\mathscr I_{\mathsf V}=7y_2,
\qquad
F_{\mathsf V}=\begin{pmatrix}0&7\end{pmatrix},
\qquad
I^{\rm bil}_{\mathsf V}=0,
$$

the same nonlinear coordinate map gives

$$
I^{\rm bil}_{\mathsf C}
=0+\begin{pmatrix}7&0\\0&0\end{pmatrix}
=\begin{pmatrix}7&0\\0&0\end{pmatrix}.
$$

Hence an off-shell nonlinear quantum-coordinate bridge is not certified by a
pure congruence.

## 4. Background Ward recursion

$$
\delta A=R_{\mathsf V}A-AR_{\mathsf C},
\qquad
X_{\mathsf C}=A^{-1}X_{\mathsf V}A,
\qquad
\delta X_{\mathsf V}=[R_{\mathsf V},X_{\mathsf V}].
$$

$$
\begin{aligned}
\delta X_{\mathsf C}
={}&-A^{-1}(\delta A)A^{-1}X_{\mathsf V}A
+A^{-1}[R_{\mathsf V},X_{\mathsf V}]A
+A^{-1}X_{\mathsf V}(\delta A)\\
={}&R_{\mathsf C}X_{\mathsf C}-X_{\mathsf C}R_{\mathsf C}
=[R_{\mathsf C},X_{\mathsf C}].
\end{aligned}
$$

Thus the rooted one-loop Ward telescoping is representation-independent on
the exact similarity sector.  A scalar source-Hessian belongs to this sector
only after its first-jet connection term has been retained.  Full functional frame independence still
requires the Step-3D source, density, ghost/non-minimal, regulator, and cycle
pushforwards.

## 5. Gates

$$
N_{\rm exact}=100,
\qquad
N_{\rm failed}=0.
$$

$$
\begin{array}{c|c}
\text{gate}&\text{status}\\ \hline
\text{general-gauge-algebra covariant operator similarity}&\mathrm{PASS}\\
\text{SU2 nilpotent coefficient witness}
&\mathrm{PASS}\\
\text{quadratic Hessian/Green/source on similarity sector}&\mathrm{PASS}\\
\text{reference-flat adjoint-block measure}&\mathrm{PASS}\\
\text{background Ward recursion on similarity sector}&\mathrm{PASS}\\
\text{nonlinear tangent Hessian}&
E_{\mathsf V,\alpha}C^\alpha{}_{ij}=0\ \mathrm{required}\\
\text{nonlinear source Hessian}&
F_{\mathsf V,\alpha}C^\alpha{}_{ij}=0\ \mathrm{required}\\
\text{arbitrary-gauge-algebra background regulator closure}&\mathrm{OPEN}\\
\text{full physical+ghost+nonminimal Jacobian}&\mathrm{OPEN}\\
\text{finite-BV density and cycle}&\mathrm{OPEN\ in\ Step\ 5C}\\
\text{anomaly coefficient}&\mathrm{NOT\ COMPUTED}
\end{array}
$$

## 6. Gap ledger

$$
\begin{array}{c|c|c|c}
\text{id}&\text{type}&\text{result}&\text{severity}\\ \hline
G1&\mathrm{G\!\!\!-DEF}&
A_{\mathcal B}=\operatorname{Ad}_{\mathcal B}
&P0\ \mathrm{RESOLVED}\\
G2&\mathrm{G\!\!\!-ALG}&
K_{\mathsf C}=J_{\rm q}^{\mathrm{st}}K_{\mathsf V}J_{\rm q}+E_{\mathsf V}C
&P0\ \mathrm{RESOLVED}\\
G3&\mathrm{G\!\!\!-ALG}&
I^{\rm bil}_{\mathsf C}=J_{\rm q}^{\mathrm{st}}I^{\rm bil}_{\mathsf V}J_{\rm q}+F_{\mathsf V}C
&P0\ \mathrm{RESOLVED}\\
G4&\mathrm{G\!\!\!-NORM}&
\operatorname{Ber}J_{\mathbb T}^{\perp}\text{ including ghosts and nonminimal blocks}
&P1\ \mathrm{OPEN}\\
G5&\mathrm{G\!\!\!-SCOPE}&
\text{arbitrary-background projector/regulator closure}
&P1\ \mathrm{OPEN}\\
G6&\mathrm{G\!\!\!-SCOPE}&
\text{finite-BV density and cycle pushforward}
&P1\ \mathrm{OPEN\ IN\ STEP\ 5C}
\end{array}
$$

Checked equation groups: operator similarity; adjoint bridge; tangent chain
rule; pairing/Hessian/Green; scalar source insertion; supertrace; reference-flat
Berezinian; background Ward telescoping.

Verification spot checks: exact fundamental conjugation; exact two-sided
inverse in coefficient dimension forty-eight; direct second differentiation
of the action and source counterexamples.
