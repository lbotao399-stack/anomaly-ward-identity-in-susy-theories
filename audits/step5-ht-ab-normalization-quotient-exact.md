# HT--Project AB/BA normalization and quotient audit

Status: `PASS_HT_AB_SCALE_ONE__S1_CANCELS__RAW_G3_SCALE_TWO_IS_NOT_A_NORMALIZATION_EFFECT__FIRST_ERROR_IS_MIXED_QUOTIENT_LAYER`.

## 1. Notation

$$
\iota(X_H)=a_X X_P,
\qquad
\iota(\hbar_HQ_{1,H})\iota^{-1}=s_1\Delta_P,
\qquad
\lambda_1=\frac{\hbar_Pg^2}{16\pi^2}.
$$

$$
a_A=-\frac{i}{\sqrt2},\qquad
a_{B_r}=\frac1{\sqrt2},\qquad
a_{C_r}=1,\qquad
a_D=i.
$$

The common factor $\rho$ cancels as $\rho^2/\rho^2$ in every bilinear.

## 2. AA fixes the loop marker

$$
a_A^2=-\frac12,qquad
a_Da_A=a_{B_r}a_{C_r}=\frac1{\sqrt2}.
$$

Therefore every term in the HT $AA$ row has ratio

$$
\frac{a_Da_A}{a_A^2}
=\frac{a_{B_r}a_{C_r}}{a_A^2}
=-\sqrt2.
$$

The target-blind accepted Project row is

$$
\Delta_P(A,A)=\lambda_1\mathbb F^{AB}{}_{DE}\mathscr Z^{DE}.
$$

Thus

$$
\frac{\hbar_H\kappa_H^2}{s_1}(-\sqrt2)=\lambda_1,
$$

$$
\boxed{\hbar_H\kappa_H^2=-\frac{s_1}{\sqrt2}\lambda_1},
\qquad
\boxed{\frac{\hbar_H\kappa_H^2}{s_1}=-\frac{\lambda_1}{\sqrt2}}.
$$

If $s_1=s_0=-1/2$,

$$
\hbar_H\kappa_H^2=\frac{\lambda_1}{2\sqrt2},
$$

but $s_1$ has already canceled from every $AB/AA$ ratio.

The AA normalization itself is target-blind:

$$
N_{\rm raw\ endpoint}=48,
\qquad
m_{e_0}=m_{e_2}=1,
$$

$$
(D>A,A>D)=(1,-1),
\qquad
(B_r>C_r,C_r>B_r)=(1,-1).
$$

Thus the AA seed contains no unaccounted factor $1/2$ inherited from the HT
$\mathcal D^\tri_{0,0}$ convention.

## 3. AB/BA translation

$$
a_Aa_{B_1}=-\frac i2,\qquad
a_Da_{B_1}=\frac i{\sqrt2},\qquad
a_{C_2}a_{C_3}=1.
$$

$$
\frac{a_Da_{B_1}}{a_Aa_{B_1}}=-\sqrt2,
\qquad
\frac{a_{C_2}a_{C_3}}{a_Aa_{B_1}}=2i.
$$

Hence

$$
-\frac{\lambda_1}{\sqrt2}(-\sqrt2)=\lambda_1,
$$

$$
-\frac{\lambda_1}{\sqrt2}(2i)=-i\sqrt2\lambda_1.
$$

For $I=1$ the flavor sum is exactly

$$
\sum_{J,K}\varepsilon_{1JK}C_JC_K
=C_2C_3-C_3C_2.
$$

It contains two ordered terms and no factor $1/2$.  In the basis

$$
(D>B_1,\ B_1>D,\ C_2>C_3,\ C_3>C_2),
$$

$$
\boxed{v_{HT,0}=(1,1,-i\sqrt2,+i\sqrt2)}.
$$

The color map has no scalar factor:

$$
f_{ACD}f_{BCE}\longmapsto\mathbb F^{AB}{}_{DE}.
$$

## 4. HT source branches

The explicit zero-component row starts at source line 1241; the main compact row starts at line 1251.  Both give coefficient $1$.

The shifted $\mathcal D^\tri$ row starts at line 1070, while

$$
\mathcal D^\tri_{0,0}(f,g)=\frac12\langle f,g\rangle
$$

at line 726; Appendix B starts the same row at line 1390.  Therefore

$$
v_{HT,\mathcal D^\tri}=\frac12v_{HT,0}.
$$

The source conflict is scale $1$ versus scale $1/2$; neither branch gives scale $2$.

The exact three-way comparison is

$$
T^{HT}_{0,0}=\frac12,
\qquad
K^P_{0,0}=2T^{HT}_{0,0}=1,
\qquad
G_{3,\rm raw}=2.
$$

Thus

$$
\frac{G_{3,\rm raw}}{K^P_{0,0}}=2,
\qquad
\frac{G_{3,\rm raw}}{T^{HT}_{0,0}}=4.
$$

The already-recorded identity $K^P=2T^{HT}$ changes $1/2$ into $1$; it does
not change the locked raw $G_3$ coefficient $2$ into $1$.

## 5. Raw local and quotient layers

Raw local jets are

$$
(c_{G_1,\rm pair},c_{G_1,\rm EOM})=(2,2),
$$

$$
(c_{G_2,\rm pair},c_{G_2,\rm EOM})
=\left(-\frac13,\frac43\right),
$$

$$
(c_{G_3,C_2C_3},c_{G_3,C_3C_2})
=(-2i\sqrt2,+2i\sqrt2).
$$

For $G_1$,

$$
T_{DB}={\rm pair}+{\rm EOM},
$$

$$
2\,{\rm pair}+2\,{\rm EOM}=2T_{DB}.
$$

For $G_2$,

$$
T_{BD}=-{\rm pair}+{\rm EOM},
$$

$$
-\frac13{\rm pair}+\frac43{\rm EOM}
={\rm pair}+\frac43T_{BD}.
$$

The equality

$$
T_{BD}=0
$$

is false in the raw local jet space.  Only

$$
[T_{BD}]_{\rm TD}=0
$$

holds in the total-derivative quotient.

The current hybrid vector is

$$
v_{\rm hybrid}=(2,1,-2i\sqrt2,+2i\sqrt2).
$$

Its componentwise ratios to $v_{HT,0}$ are

$$
(2,1,2,2).
$$

No scalar $r$ satisfies $rv_{\rm hybrid}=v_{HT,0}$.

## 6. AA residual-q comparison

Let

$$
\mathscr Y_1
=\langle D,B_1\rangle+\langle B_1,D\rangle
-i\sqrt2\langle C_2,C_3\rangle
+i\sqrt2\langle C_3,C_2\rangle.
$$

The locked local relations are

$$
q_1\mathscr Y_1=i\mathscr Z,
\qquad
q_1(AB_1)=-iAA,
\qquad
\Delta_P(AA)=\mathscr Z.
$$

If $\Delta_P(AB_1)=t\mathscr Y_1$, then

$$
q_1\Delta_P(AB_1)+\Delta_Pq_1(AB_1)
=it\mathscr Z-i\mathscr Z
=i(t-1)\mathscr Z.
$$

Therefore

$$
\boxed{t=1}.
$$

For $t=2$ the residual is exactly

$$
i\mathscr Z\ne0.
$$

## 7. Exact boundary

The HT normalization supplies no factor $1/2$ capable of changing the locked raw $G_3$ scale $2$ into scale $1$.  Such a change requires an explicit common-layer EOM/BRST/total-derivative/counterterm quotient map.

Checks: `48/48` PASS.
