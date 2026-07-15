# AB/BA Project-Ward finite renormalization

Status: `PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__AB_BA_HT_CHECK_ONLY_EXACT_MATCH`.

## 1. Common quotient layer

$$
G_1:(2,2)_{(\mathrm{pair},\mathrm{EOM})}
\longmapsto(0,2)_{(\mathrm{pair},T_{DB})},
\qquad T_{DB}=\mathrm{pair}+\mathrm{EOM},
$$

$$
G_2:\left(-\frac13,\frac43\right)_{(\mathrm{pair},\mathrm{EOM})}
\longmapsto\left(1,\frac43\right)_{(\mathrm{pair},T_{BD})},
\qquad T_{BD}=-\mathrm{pair}+\mathrm{EOM}.
$$

Thus the common compact total-derivative layer is

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2).
$$

The old vector $(2,1,-2i\sqrt2,+2i\sqrt2)$ is not a common quotient: it
identifies the G1 EOM projection $2$ with the G1 TD projection $0$.

## 2. Project Ward equation

In the basis $(D>B_1,B_1>D,C_2>C_3,C_3>C_2)$,

$$
M_q=
\begin{pmatrix}
1&-1&0&0\\
i\sqrt2&0&1&0\\
-i\sqrt2&0&0&1
\end{pmatrix},
\qquad
\ker M_q=\mathbb C(1,1,-i\sqrt2,+i\sqrt2).
$$

A missing vector-frame graph has zero ordered $CC$ support.  Imposing that
support gives the scale-two completion

$$
v_{\rm TD}+(2,1,0,0)=2(1,1,-i\sqrt2,+i\sqrt2),
$$

which conflicts with the target-blind AA normalization $\Delta(A,A)=\mathscr Z$.

A finite composite-source counterterm is not restricted by missing-graph
external support.  The equations

$$
M_q(v_{\rm TD}+v_{\rm fin})=0,
\qquad
q_1\mathscr Y_1=i\mathscr Z,
\qquad
\Delta(A,A)=\mathscr Z
$$

have the unique solution

$$
v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2).
$$

Therefore

$$
\boxed{
v_{\rm ren}=(1,1,-i\sqrt2,+i\sqrt2).}
$$

Equivalently,

$$
\delta_{\rm fin}\Gamma_{AB_1}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\langle D^D,B_1^E\rangle
+i\sqrt2\langle C_2^D,C_3^E\rangle
-i\sqrt2\langle C_3^D,C_2^E\rangle
\right].
$$

## 3. Check-only target comparison

The Project payload is sealed before the holomorphic-twist artifact is read.
The ordered AB and BA vectors agree exactly.
