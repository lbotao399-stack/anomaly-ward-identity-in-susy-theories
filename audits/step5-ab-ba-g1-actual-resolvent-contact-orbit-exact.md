# AB/BA G1 actual vector-frame resolvent contact orbit

Status: `G1_VECTOR_FRAME_R1_R2_R3_ANOMALY_ZERO__NO_MISSING_MINUS_ONE__COMMON_LAYER_RAW_TWO_TWO__MOD_TOTAL_DERIVATIVE_ZERO`.

## 1. Vector-frame source

With

$$
V=\sqrt{2}\,g\,U,\qquad
{\cal B}_{\rm ad}=e^{\operatorname{ad}_V/2},\qquad
b_1(L)=\frac{1}{\sqrt{2}}[U,L],\qquad
b_2(L)=\frac{1}{4}[U,[U,L]],
$$

the source sectors needed for two external fields are

$$
I_{[0]}: A_1B_{11},
$$

$$
I_{[1]}:\quad
A_2B_{11}+A_1B_{12}+b_1(A_1)B_{11}+A_1b_1(B_{11}),
$$

$$
\begin{aligned}
I_{[2]}:\quad&
A_3B_{11}+b_1(A_2)B_{11}+b_2(A_1)B_{11}\\
&+A_2B_{12}+A_2b_1(B_{11})+b_1(A_1)B_{12}
+b_1(A_1)b_1(B_{11})\\
&+A_1B_{13}+A_1b_1(B_{12})+A_1b_2(B_{11}).
\end{aligned}
$$

Every $I_{[1]}$ word has species $(u,u,\phi_1)$; every $I_{[2]}$ word has
$(u,u,u,\phi_1)$.

## 2. Complete legal lower-resolvent classes

$$
R_1=G_0I_{[2]}:\quad
(u,u)_{\rm quantum}\longrightarrow\text{one massless tadpole}.
$$

$$
R_{2,G}=-G_0S_{g3}G_0I_{[1]}:\quad
(u,u)\leftrightarrow(u,u).
$$

$$
R_{2,M}=-G_0S_{m3}G_0I_{[1]}:\quad
(u,\phi_1)\leftrightarrow(u,\widetilde\phi_1).
$$

$$
R_{3,M}=-G_0S_{m4}G_0I_{[0]}:\quad
(u,\phi_1)\leftrightarrow(u,\widetilde\phi_1).
$$

Pure gauge, gauge-fixing, FP, NK, and measure $R_3$ vertices have no
$\widetilde\phi_1$ port and therefore cannot close the source $\phi_1$ port.

## 3. Exact symbolic bubbles

Define

$$
S(q)^{\dot0}=q_0-iq_1,qquad
S(q)^{\dot1}=-(q_2+iq_3).
$$

The complete $I_{[1]}S_{g3}$ result, for both AB and BA, is

$$
N_{R_{2,G}}^{\dot a}
=-\frac{\sqrt{2}}{4}S(q)^{\dot a}.
$$

Occurrence resolution gives

$$
N_{\rm nonbridge}=-\frac{\sqrt{2}}{2}S(q),\qquad
N_{\rm vector\ bridge}=+\frac{\sqrt{2}}{4}S(q),
$$

$$
N_{\rm complete}=-\frac{\sqrt{2}}{4}S(q).
$$

It contains neither $\ell$ nor $p$ and contains no four-dimensional inverse
square.  Hence

$$
{\cal A}_{R_{2,G}}=0.
$$

The complete symbolic exterior-algebra replays give

$$
N_{R_{2,M}}=0,qquad N_{R_{3,M}}=0.
$$

For $R_1$, every possible evanescent numerator remains a massless tadpole:

$$
\int d^d\ell\,
\frac{(\mu_\ell^2)^r(\ell^2)^s}{(\ell^2)^n}=0.
$$

Therefore

$$
\boxed{{\cal A}_{R_1}={\cal A}_{R_2}={\cal A}_{R_3}=0.}
$$

## 4. Longitudinal sector boundary

The ordinary longitudinal term has no occurrence-tagged
four-dimensional inverse square.  Therefore it has no
$p_{\rm full}^2-\bar p^2=\widehat p^2$ cutting defect:

$$
{\cal A}_{\rm longitudinal,\ no\ square}=0.
$$

This anomaly-sector statement is separate from the raw Ward/contact identity;
the latter is not claimed complete here.

## 5. Common layer

The occurrence-tagged $R_4$ selected squares remain

$$
A=\left(\frac43,\frac23\right),qquad
B=\left(\frac23,\frac43\right),
$$

$$
G_{1,\rm raw}=(2,2)_{(p,q)}.
$$

Let

$$
X=\langle D,B_1\rangle,qquad
Y=B_1(P\cdot D),qquad
T_{DB}=X+Y.
$$

Then

$$
2X+2Y=2T_{DB},qquad
(c_{\rm pair},c_T)=(0,2).
$$

Thus

$$
\boxed{[G_1]_{\rm total\ derivative}=0.}
$$

The vector-frame $R_1/R_2/R_3$ orbit supplies $(0,0)$, not a coefficient
$-1$ in the $D>B_1$ slot.  Since no target data enter this derivation, the
common-layer verdict is

$$
\boxed{\texttt{NO\_COMMON\_LAYER\_CLOSURE}.}
$$
