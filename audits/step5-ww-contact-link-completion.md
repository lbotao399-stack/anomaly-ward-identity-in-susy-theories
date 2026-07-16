# Step 5 WW Schwinger cut/contact/link completion audit

Authority: 00000f748fe4bdd1b5d122663cc1fb814faace66; verify run 29306335742.
HT target 与 untracked Step-5 artifacts 未作为 evidence。

## 1. Locked inputs

| file | SHA-256 | check |
|---|---|---|
| contracts/foundations/step-03a-gauge-chiral-action.md | 48141fc931580f6b73e385b8f900b3e6df5939cdb9348042de07fd8fe9320967 | PASS |
| contracts/foundations/step-03c-gauge-vector-representation.md | c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1 | PASS |
| contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md | 109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538 | PASS |
| contracts/foundations/step-04c-n4-super-yang-mills.md | fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f | PASS |

## 2. Canonical connection and WW letter

由 (3A.3)、(3A.48)、(4C.1)、(4C.4)，

$$
A_{P,m}=g a_m,\qquad \mathcal V_P=2gv,\qquad
\mathcal W_P=gW_{\rm can}.
$$

令 $X=2gv$。逐项展开

$$
e^{-X}D_ae^X
=D_aX+\frac12\llbracket D_aX,X\rrbracket
+\frac16\llbracket\llbracket D_aX,X\rrbracket,X\rrbracket+O(g^4),
$$

$$
\Gamma_a
=2gD_av+2g^2\llbracket D_av,v\rrbracket
+\frac43g^3\llbracket\llbracket D_av,v\rrbracket,v\rrbracket+O(g^4).
$$

$$
W_{1a}=-\frac14\bar D^2D_av,\qquad
W_{2a}=-\frac14\bar D^2\llbracket D_av,v\rrbracket,
$$

$$
W_{3a}=-\frac16\bar D^2
\llbracket\llbracket D_av,v\rrbracket,v\rrbracket.
$$

定义 even letter

$$
L:=g^{-1}(\nabla_+\mathcal W_+)_P
=L_1+gL_2+g^2L_3+O(g^3),
$$

$$
L_1=D_+W_{1+},
$$

$$
L_2=D_+W_{2+}+2\llbracket D_+v,W_{1+}\rrbracket,
$$

$$
L_3=D_+W_{3+}
+2\llbracket D_+v,W_{2+}\rrbracket
+2\llbracket\llbracket D_+v,v\rrbracket,W_{1+}\rrbracket.
$$

## 3. Ordered covariant translation

$$
P:=w^m\partial_m,\qquad
\mathbb M^A{}_C:=w^m c_{BC}{}^Aa_m^B,\qquad
\tau_w=e^{P+g\mathbb M}.
$$

$$
T_0=e^P,
$$

$$
T_1=\int_0^1ds\ e^{(1-s)P}\mathbb M e^{sP},
$$

$$
T_2=\int_{0\le a\le b\le1}da\,db\;
e^{(1-b)P}\mathbb M e^{(b-a)P}\mathbb M e^{aP}.
$$

令 $t_1=1-b$、$t_2=1-a$，

$$
(T_1Y)^A(x)
=\int_0^1dt\ \mathbb M^A{}_B(x+tw)Y^B(x+w),
$$

$$
(T_2Y)^A(x)
=\int_{0\le t_1\le t_2\le1}dt_1dt_2\;
\mathbb M^A{}_B(x+t_1w)\mathbb M^B{}_C(x+t_2w)Y^C(x+w).
$$

$T_2$ 没有额外 $1/2!$；constant-$\mathbb M$ 时

$$
\int_{0\le t_1\le t_2\le1}dt_1dt_2=\frac12.
$$

## 4. Ordered bilocal source through $g^2$

$$
S_J=\int d^4x\,d^4\theta\,dw\;
J_{AB}L^A(x)(\tau_wL)^B(x).
$$

$$
\mathcal I_{-|}^{AB}
=(\nabla_-L)^A(\tau_wL)^B,\qquad
\mathcal I_{|-}^{AB}
=L^A\nabla_-(\tau_wL)^B.
$$

因为 $|L|=0$，Leibniz sign 为 $+1$。同时

$$
\nabla_-(\tau_wL)
=\tau_w(\nabla_-L)+[\nabla_-,\tau_w]L,
$$

$$
[\nabla_-,\tau_w]
=\int_0^1ds\ e^{(1-s)w\cdot\mathcal D}
[\nabla_-,w\cdot\mathcal D]e^{sw\cdot\mathcal D}.
$$

$$
\mathcal O^{(0)}_{AB}=L_{1A}T_0L_{1B},
$$

$$
\mathcal O^{(1)}_{AB}
=L_{2A}T_0L_{1B}
+L_{1A}T_0L_{2B}
+L_{1A}T_1L_{1B}.
$$

$$
\begin{aligned}
\mathcal O^{(2)}_{AB}=L_{3A}T_0L_{1B} \\
&\quad+L_{1A}T_0L_{3B} \\
&\quad+L_{2A}T_0L_{2B} \\
&\quad+L_{2A}T_1L_{1B} \\
&\quad+L_{1A}T_1L_{2B} \\
&\quad+L_{1A}T_2L_{1B}.
\end{aligned}
$$

六项 product coefficient 均为 $1$。

## 5. Quartic/contact density

$$
S_{E,+}^{(4)}
=-\frac14\int
\left[W_1^aW_{3a}+W_2^aW_{2a}+W_3^aW_{1a}\right]_F.
$$

三个 ordered words 在 port differentiation 前不得合并。

## 6. Completion-sector obligations

以下 $11$ 个 sectors 对每个
$(\text{orientation},\text{marked }\nabla_-\text{ placement})$
均独立生成；JSON 共含 $2\times2\times11=44$ rows。

| sector | state | locked word |
|---|---|---|
| NONLINEAR_LETTER_LEFT | OPERATOR_WORD_DERIVED | L2_A T0 L1_B |
| NONLINEAR_LETTER_RIGHT | OPERATOR_WORD_DERIVED | L1_A T0 L2_B |
| QUARTIC_ACTION_CONTACT | DENSITY_WORD_DERIVED | W1 W3; W2 W2; W3 W1 |
| COLLAPSED_DALGEBRA_R0 | BLOCKED_AMPLITUDE_KERNEL | cut r0 |
| COLLAPSED_DALGEBRA_R1 | BLOCKED_AMPLITUDE_KERNEL | cut r1 |
| COLLAPSED_DALGEBRA_R2 | BLOCKED_AMPLITUDE_KERNEL | cut r2 |
| SCHWINGER_CUT_CONTACT | BLOCKED_AMPLITUDE_KERNEL | occurrence-decorated C_SD |
| ONE_LINK_BULK | OPERATOR_WORD_DERIVED | L1_A T1 L1_B |
| TWO_LINK_ORDERED | OPERATOR_WORD_DERIVED | L1_A T2 L1_B |
| EXTERNAL_ENDPOINT_LEFT | ENDPOINT_LAW_DERIVED | +omega(x)U |
| EXTERNAL_ENDPOINT_RIGHT | ENDPOINT_LAW_DERIVED | -U omega(y)+U delta Y(y) |

OPERATOR_WORD_DERIVED 与 DENSITY_WORD_DERIVED 不等于 physical amplitude
已闭合；BLOCKED_AMPLITUDE_KERNEL rows 不声明 graph coefficient。

## 7. Exact link/endpoint phase chain

$$
iw\cdot(r_0-r_1)
\int_0^1ds\ e^{iw\cdot[sr_0+(1-s)r_1]}
=e^{iw\cdot r_0}-e^{iw\cdot r_1}.
$$

同一 residue $C_\parallel$ 的 endpoint rows 为

$$
\begin{array}{c|c|c}
\text{triangle}&\text{one-link boundary}&\text{sum}\\ \hline
+C_\parallel e^{iw\cdot r_0}&-C_\parallel e^{iw\cdot r_0}&0\\
-C_\parallel e^{iw\cdot r_1}&+C_\parallel e^{iw\cdot r_1}&0
\end{array}.
$$

令

$$
E_{012}(a,b)
=e^{iw\cdot[ar_0+(b-a)r_1+(1-b)r_2]},\qquad0\le a\le b\le1.
$$

$$
iw\cdot(r_0-r_1)\int_0^1db\int_0^bda\,E_{012}
=\int_0^1db\,[E_{02}(b)-E_{12}(b)],
$$

$$
iw\cdot(r_1-r_2)\int_0^1da\int_a^1db\,E_{012}
=\int_0^1da\,[E_{01}(a)-E_{02}(a)].
$$

two-link longitudinal term 严格化为 one-link boundaries，再化为 endpoints。

$$
\delta U_{\rm adj}(x,y)
=\omega_{\rm adj}(x)U_{\rm adj}(x,y)
-U_{\rm adj}(x,y)\omega_{\rm adj}(y),
$$

$$
\delta[U_{\rm adj}(x,y)Y(y)]
=\omega_{\rm adj}(x)U_{\rm adj}(x,y)Y(y),
$$

因为 right endpoint coefficient 为 $-1+1=0$。

## 8. Cut involution and multiplicity

每个 root 保留 orientation、marked $\nabla_-$ placement、derivative endpoints、
color/link word 与 ordered output word。定义

$$
\mathfrak C_{SD}(T_\mathfrak r)=C_\mathfrak r,\qquad
\mathfrak C_{SD}(C_\mathfrak r)=T_\mathfrak r.
$$

脚本得到 $16$ 个 parent roots 与 $16$ 个 contact partners，并验证

$$
\mathfrak C_{SD}^2=1.
$$

固定 orientation 的 action-order weight 为

$$
\frac1{2!}(1+1)=1.
$$

reflected orientation 与另一个 marked $\nabla_-$ placement 是不同 output
words，不乘入同一 coefficient。

## 9. Conditional metric algebra

若 Project graph calculation 独立得到共同 residue $C_T$，

$$
\Gamma_{T,\rm UV}^{mn}
=+\frac{C_T}\epsilon\widehat\delta^{mn},\qquad
\Gamma_{C,\rm UV}^{mn}
=-\frac{C_T}\epsilon\delta_4^{mn}.
$$

由

$$
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},
$$

严格得到

$$
\Gamma_{T,\rm UV}^{mn}+\Gamma_{C,\rm UV}^{mn}
=-\frac{C_T}\epsilon\breve\delta^{mn}.
$$

locked foundations 尚未导出 contact 的共同 residue $C_T$。

## 10. Exact blockers

| blocker | missing | exact reason |
|---|---|---|
| BLOCKED_EXPLICIT_WW_D_ALGEBRA_WORD_DERIVATION | One complete superspace D-word, the four endpoint integration-by-parts chains, and the declared exchange map for the second marked placement. | The current endpoint signs and mixed anticommutator factors are recorded arithmetic primitives rather than rewrite-engine outputs. |
| BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE | Contract admission of S_J, its superspace/source measure, Fourier phase, dual Adj tensor Adj source law, and reversed-order rule. | Step 3D permits general sources but does not select this Step-5 operator. |
| BLOCKED_LOCKED_STEP5_DRED_CONTRACT | Verified d=4-2 epsilon, loop measure, delta_4=hat_delta+breve_delta, and regulator action on all blocks. | Steps 3A/3C/3D/4C contain no dimensional-reduction metric split. |
| BLOCKED_LOCKED_GAUGE_KERNEL_AND_PROPAGATORS | A chosen Y_E in (3D.88a)--(3D.93), residual-free Hessian, and exact vector/chiral/FP/NK/multiplier inverses. | The Schwinger cut K*G=delta cannot be evaluated while the gauge-fixing map and density are arbitrary. |
| BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR | Ordered derivatives of this bilocal source and the full background-split N=4 action through g^2, including ghost and measure ports. | BCH fixes operator words, but not background/quantum/external port type, identical-leg factors, or contraction signs. |
| BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES | Edge-tagged D-algebra and loop reduction of every nonlinear, quartic, collapsed, one-link, two-link, and endpoint graph. | Phase telescoping proves cancellation only after the graph residues are independently equal. |
| BLOCKED_RENORMALIZED_COMPOSITE_MIXING | Local composite/counterterm basis and evanescent-to-physical one-loop mixing matrix. | An O(epsilon) operator can multiply a 1/epsilon pole. |

## 11. Checks

| check | status |
|---|---|
| foundation_hash::contracts/foundations/step-03a-gauge-chiral-action.md | PASS |
| foundation_hash::contracts/foundations/step-03c-gauge-vector-representation.md | PASS |
| foundation_hash::contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md | PASS |
| foundation_hash::contracts/foundations/step-04c-n4-super-yang-mills.md | PASS |
| two_link_boundary::a=b | PASS |
| two_link_boundary::a=0 | PASS |
| two_link_boundary::b=1 | PASS |
| two_link_boundary::b=a | PASS |
| external_endpoint_covariance | PASS |
| cut_involution_C_squared | PASS |
| sixteen_occurrence_decorated_roots | PASS |
| fixed_orientation_wick_weight | PASS |
| no_orientation_or_Dminus_double_count | PASS |
| conditional_metric_basis_algebra | PASS |

$$
\boxed{\text{overall status}=\texttt{CONDITIONAL_FF_ARITHMETIC__BLOCKED_EXPLICIT_D_WORD_AND_STEP5_COMPLETION_KERNELS}}.
$$
