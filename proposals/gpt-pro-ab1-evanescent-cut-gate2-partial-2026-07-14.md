# GPT Pro Gate 2 partial response — ordered \(AB_1\) parent triangles

Status: `NON_AUTHORITY_PRO_REVIEW__REJECTED_MISSING_OUTER_NABLA_MINUS_DESCENDANT`.

Model slug: `gpt-5-6-pro`.

The response was forced to answer after 79 minutes because the Gate-2 prompt omitted the AWI descendant

$$
\nabla_-(AB_1)=(\nabla_-A)B_1+A(\nabla_-B_1).
$$

Consequently every coefficient below is retained as a Pro parent-triangle proposal only.  It is not an accepted anomaly-sector calculation and must not be used to fill the holomorphic-twist target.

## Verbatim rendered response

## Notation

$$
\langle X^D,Y^E\rangle
:=
(P_{\dot\alpha}X^D)(P^{\dot\alpha}Y^E),
\qquad
P_{\dot\alpha}:=\sigma^m_{+\dot\alpha}\partial_m ,
$$

$$
\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E},
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

For every triangle,

$$
r_0=k,\qquad r_1=k-p,\qquad r_2=k-p-q,
\qquad
D_i=r_{i,d}^2 .
$$

Define the regulated triangle-minus-cut unit

$$
\mathcal E_e
:=
\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}
\left[
\frac{\bar r_e^{\,2}}{D_0D_1D_2}
-
\frac1{\prod_{j\neq e}D_j}
\right].
$$

The frozen regulator calculation gives

$$
\boxed{\mathcal E_e=\frac1{32\pi^2}}
$$

for every shifted edge $e$. No additional $4-d$ factor is inserted.

The strict four-dimensional $D$-algebra used below is

$$
\{D_+,\bar D_{\dot\alpha}\}=-2P_{\dot\alpha},
$$

$$
D^2\bar D^2D^2
=
16\bar r^{\,2}D^2,
\qquad
\bar D^2D^2\bar D^2
=
16\bar r^{\,2}\bar D^2,
$$

$$
D^2\theta^2=-4,
\qquad
\bar D^2\bar\theta^2=-4.
$$

The full and antichiral Berezin measures are included in the displayed $D$-words.

Canonical external letters are

$$
B_{1,c}=D_+\phi_1\big|,
$$

$$
D_{c,\dot\alpha}
=
g^{-1}\widetilde{\mathcal W}_{\dot\alpha}\big|
=
-\frac1{4\sqrt2}D^2\bar D_{\dot\alpha}u\big|,
$$

$$
C_{r,c}=\widetilde\phi_r\big|.
$$

Set

$$
X_{\dot\alpha}[u]
:=
D^2\bar D_{\dot\alpha}u\big|
=
-4\sqrt2\,D_{c,\dot\alpha}.
$$

Physical fields obey

$$
B_1=gB_{1,c},
\qquad
D=gD_c,
\qquad
C_r=gC_{r,c},
$$

hence

$$
\langle X_c,Y_c\rangle
=
g^{-2}\langle X,Y\rangle.
$$

# 1. Common exponential and Wick factors

The source is inserted directly:

$$
s_{\mathcal O}
=
-\frac{g^2}{4\sqrt2}.
$$

There is no source factor $1/\hbar$.

For two distinct interactions,

$$
\frac1{2!}
\left(
\mathfrak V_X\mathfrak V_Y
+
\mathfrak V_Y\mathfrak V_X
\right)
=
\mathfrak V_X\mathfrak V_Y.
$$

Therefore

$$
w_{G_1}=1,
\qquad
w_{G_{3,2}}=w_{G_{3,3}}=1.
$$

For $G_2$,

$$
\frac1{2!}
\times
\left[
(M_L,M_R)+(M_R,M_L)
\right]
=
\frac12(2)=1.
$$

All quantum superfields $u,\phi,\widetilde\phi$ are Grassmann-even integration variables. Therefore no independent closed-fermion-loop sign occurs.

The propagator products are

$$
G_1:
\qquad
(-\hbar)^2
\left(\frac{\hbar}{16}\right)
=
+\frac{\hbar^3}{16},
$$

$$
G_2,\ G_{3,2},\ G_{3,3}:
\qquad
(-\hbar)
\left(\frac{\hbar}{16}\right)^2
=
-\frac{\hbar^3}{256}.
$$

The $1/16$ factors are retained in these scalar ledgers and are not repeated in the $D$-words. These propagator signs and the matter/Hessian vertices are precisely the Euclidean normalized-Wick primitives.

# 2. $G_1=(I[u,\phi_1],M_1,\mathcal V_{VVV})$

## 2.1 The twelve labeled gauge occurrences

Let $U$ denote the vector line from the source, $C$ the vector line from $M_1$, and $D$ the external gauge letter. Define

$$
K_1(X,Y,Z)
:=
c_{XYZ}
D^2(u_X\bar D_{\dot a}u_Y)
D^2\bar D^{\dot a}u_Z,
$$

$$
K_2(X,Y,Z)
:=
c_{XYZ}
D^2\bar D_{\dot a}u_X
D^2(u_Y\bar D^{\dot a}u_Z).
$$

The complete ordered Hessian consists of

$$
\begin{array}{c|c|c}
(X,Y,Z)&K_1(X,Y,Z)&K_2(X,Y,Z)\\ \hline
(U,C,D)&K_1(U,C,D)&K_2(U,C,D)\\
(U,D,C)&K_1(U,D,C)&K_2(U,D,C)\\
(C,U,D)&K_1(C,U,D)&K_2(C,U,D)\\
(C,D,U)&K_1(C,D,U)&K_2(C,D,U)\\
(D,U,C)&K_1(D,U,C)&K_2(D,U,C)\\
(D,C,U)&K_1(D,C,U)&K_2(D,C,U)
\end{array}
$$

with common exponent coefficient

$$
+\frac{i\sqrt2g}{256\hbar}.
$$

There is no additional $N_{VVV}$.

Using

$$
D^2(XY)
=
(D^2X)Y
+
X(D^2Y)
-
2(D_aX)(D^aY),
$$

and retaining exactly the term linear in

$$
X_{\dot a}[u_D]
=
D^2\bar D_{\dot a}u_D
=
-4\sqrt2\,D_{c,\dot a}^D,
$$

the twelve terms give

$$
\boxed{
\sum_{\pi\in S_3}
\Pi_{D_c^D}
\left[
K_1(U_{\pi1},U_{\pi2},U_{\pi3})
+
K_2(U_{\pi1},U_{\pi2},U_{\pi3})
\right]
=
32\sqrt2\,
c_{UCD}
D_{c,\dot a}^D
(\bar D_C^{\dot a}-\bar D_U^{\dot a}).
}
$$

Equivalently,

$$
\frac{i\sqrt2g}{256\hbar}(32\sqrt2)
=
\frac{ig}{4\hbar},
$$

so the exact external-$D_c$ gauge Hessian is

$$
\boxed{
\mathfrak V_{G,D}
=
+\frac{ig}{4\hbar}
c_{UCD}D_{c,\dot a}^D
(\bar D_C^{\dot a}-\bar D_U^{\dot a}).
}
$$

The $C_+$ cubic has zero projection onto the external antichiral bottom letter:

$$
\boxed{\Pi_{D_c}C_+=0.}
$$

## 2.2 Color route

The source vector contracts with the gauge index $U$; the $M_1$-vector contracts with $C,C'$; the external matter field has index $E$. Thus

$$
\begin{aligned}
\mathcal C_{G_1}
&=
\kappa^{AU}\kappa^{CC'}
c_{UC'D}(T_C)^B{}_E
\\
&=
i\kappa^{AU}\kappa^{CC'}\kappa^{BV}
c_{UC'D}c_{CEV}
\\
&=
i\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}
\\
&=
\boxed{i\mathbb F^{AB}{}_{DE}}.
\end{aligned}
$$

The external order is therefore

$$
(D_c^D,B_{1,c}^E).
$$

## 2.3 Two endpoint $D$-words

The line $C$ is the $M_1$-to-gauge vector edge $r_1$; the line $U$ is the source-to-gauge vector edge $r_2$.

For the bare $\bar D_C$ occurrence,

$$
\begin{aligned}
\mathfrak D_{1,C}
&=
64\,\bar r_1^{\,2}
\left(D_+\bar D_{\dot\alpha}D_c^D\right)
\left(D_+\bar D^{\dot\alpha}B_{1,c}^E\right)
\\
&=
64\,\bar r_1^{\,2}
(-2P_{\dot\alpha}D_c^D)
(-2P^{\dot\alpha}B_{1,c}^E)
\\
&=
\boxed{
+256\,\bar r_1^{\,2}
\langle D_c^D,B_{1,c}^E\rangle.
}
\end{aligned}
$$

For the bare $\bar D_U$ occurrence, transporting the odd derivative to the common directed word gives one minus:

$$
\begin{aligned}
\mathfrak D_{1,U}
&=
-64\,\bar r_2^{\,2}
\left(D_+\bar D_{\dot\alpha}D_c^D\right)
\left(D_+\bar D^{\dot\alpha}B_{1,c}^E\right)
\\
&=
\boxed{
-256\,\bar r_2^{\,2}
\langle D_c^D,B_{1,c}^E\rangle.
}
\end{aligned}
$$

The gauge Hessian contains

$$
\bar D_C-\bar D_U,
$$

so the two actual triangle-minus-cut contributions are

$$
+256\,\mathcal E_1
\langle D_c^D,B_{1,c}^E\rangle
$$

and

$$
(-1)(-256)\,\mathcal E_2
\langle D_c^D,B_{1,c}^E\rangle.
$$

Hence

$$
\boxed{
\mathfrak D_{G_1}^{\rm orbit}
=
512\left(\frac1{32\pi^2}\right)
\langle D_c^D,B_{1,c}^E\rangle.
}
$$

## 2.4 Scalar coefficient

$$
\begin{aligned}
S_{G_1}
&=
\left(-\frac{g^2}{4\sqrt2}\right)
\left(+\frac{\sqrt2g}{\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
\left(+\frac{\hbar^3}{16}\right)
\\
&=
-\frac{i\hbar g^4}{256}.
\end{aligned}
$$

Multiplying the color route,

$$
\left(-\frac{i\hbar g^4}{256}\right)
(i\mathbb F)
=
+\frac{\hbar g^4}{256}\mathbb F.
$$

Physical-field conversion gives

$$
\frac{\hbar g^4}{256}\,
\langle D_c,B_{1,c}\rangle
=
\frac{\hbar g^2}{256}\,
\langle D,B_1\rangle.
$$

Therefore

$$
\begin{aligned}
\Gamma_{G_1}^{AB}
&=
\frac{\hbar g^2}{256}
(512)
\left(\frac1{32\pi^2}\right)
\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle
\\
&=
\boxed{
\lambda_1
\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle.
}
\end{aligned}
$$

# 3. $G_2=(I[u,\phi_1],M_1,M_1)$

## 3.1 Labeled Wick orientations

Let $M_L,M_R$ be the two labeled matter vertices.

Orientation $a$:

$$
\phi_{1,s}^B
\longrightarrow
\widetilde\phi_{1,L},
\qquad
\phi_{1,L}
\longrightarrow
\widetilde\phi_{1,R},
\qquad
u_s^A
\longrightarrow
u_R.
$$

The uncontracted fields are

$$
u_L^E,
\qquad
\phi_{1,R}^D.
$$

Orientation $b$ exchanges $L\leftrightarrow R$. Therefore

$$
w_{G_2}
=
\frac1{2!}(1_a+1_b)=1.
$$

The reversed chiral kernel is used in orientation $b$; $b$ is the label exchange of $a$, not an additional graph factor.

## 3.2 Complete $D$-word

Let

$$
\Delta_{ij}:=\delta^4(\theta_i-\theta_j),
\qquad
\mathscr P_{ij}:=\bar D_i^2D_i^2\Delta_{ij}.
$$

With the $1/16$ factors kept in the scalar propagator ledger, the orientation-$a$ word is

$$
\begin{aligned}
\mathfrak W_2
={}&
\int d^4\theta_L\,d^4\theta_R\,
\Bigl[
D_{s+}\bar D_s^2D_{s+}\Delta_{sR}
\Bigr]
\Bigl[
D_{s+}\mathscr P_{sL}
\Bigr]
\mathscr P_{LR}
\\
&\hspace{25mm}\times
u_L^E\phi_{1,R}^D
\Big|_{\theta_s=0}.
\end{aligned}
$$

The two chiral projector chains select the internal matter edge $e=1$:

$$
\mathfrak W_2
=
64\,\bar r_1^{\,2}
\left(D_+\bar D_{\dot\alpha}B_{1,c}^D\right)
\left(D_+\bar D^{\dot\alpha}X^E\right).
$$

Using

$$
D_+\bar D_{\dot\alpha}B_{1,c}
=
-2P_{\dot\alpha}B_{1,c},
$$

$$
D_+\bar D_{\dot\alpha}X
=
-2P_{\dot\alpha}X,
$$

gives

$$
\mathfrak W_2
=
256\,\bar r_1^{\,2}
(P_{\dot\alpha}B_{1,c}^D)
(P^{\dot\alpha}X^E).
$$

Since

$$
X^E=-4\sqrt2\,D_c^E,
$$

$$
\boxed{
\mathfrak W_2
=
-1024\sqrt2\,
\bar r_1^{\,2}
\langle B_{1,c}^D,D_c^E\rangle.
}
$$

The label-exchanged word has the same value:

$$
\mathfrak W_2^{(b)}
=
\mathfrak W_2^{(a)}.
$$

The exponential factor $1/2!$ and the two labeled words leave exactly the displayed coefficient, not twice that coefficient.

## 3.3 Color route

The external vector is $E$, the external matter field is $D$. The ordered route is

$$
\begin{aligned}
\mathcal C_{G_2}
&=
\kappa^{AU}
(T_E)^B{}_C
(T_U)^C{}_D
\\
&=
-\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{ECV}c_{UDC'}
\\
&=
-\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{VCE}c_{UC'D}
\\
&=
\boxed{-\mathbb F^{AB}{}_{DE}}.
\end{aligned}
$$

## 3.4 Scalar coefficient

$$
\begin{aligned}
S_{G_2}
&=
\left[\frac1{2!}(2)\right]
\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)^2
\left(-\frac{\hbar^3}{256}\right)
\\
&=
+\frac{\hbar g^4}{512\sqrt2}.
\end{aligned}
$$

Including color and physical-field conversion,

$$
S_{G_2}\mathcal C_{G_2}\,g^{-2}
=
-\frac{\hbar g^2}{512\sqrt2}
\mathbb F^{AB}{}_{DE}.
$$

Therefore

$$
\begin{aligned}
\Gamma_{G_2}^{AB}
&=
\left(-\frac{\hbar g^2}{512\sqrt2}\right)
\left(-1024\sqrt2\right)
\left(\frac1{32\pi^2}\right)
\mathbb F^{AB}{}_{DE}
\langle B_1^D,D^E\rangle
\\
&=
\boxed{
\lambda_1
\mathbb F^{AB}{}_{DE}
\langle B_1^D,D^E\rangle.
}
\end{aligned}
$$

# 4. $G_{3,r}=(I[u,\phi_1],M_r,H_-)$

Let

$$
(r,s)=(2,3)
\quad\text{or}\quad
(r,s)=(3,2).
$$

The unique flavor-directed contractions are

$$
u_s^A\longrightarrow u_{M_r},
$$

$$
\phi_{1,s}^B
\longrightarrow
\widetilde\phi_{1,H},
$$

$$
\phi_{r,M}
\longrightarrow
\widetilde\phi_{r,H}.
$$

The uncontracted fields are

$$
\widetilde\phi_{r,M}^D=C_{r,c}^D,
\qquad
\widetilde\phi_{s,H}^E=C_{s,c}^E.
$$

The vertices are distinct, so

$$
\frac1{2!}
\left(
\mathfrak V_{M_r}\mathfrak V_H
+
\mathfrak V_H\mathfrak V_{M_r}
\right)
=
\mathfrak V_{M_r}\mathfrak V_H.
$$

No further flavor factorial occurs: the differentiated $H_-$ vertex already contains the ordered $\varepsilon_{1rs}$.

## 4.1 Complete $D$-word

Let $M$ be the full-superspace matter vertex and $H$ the antichiral vertex. The antichiral measure

$$
\int d^2\bar\theta_H
=
-\frac14\bar D_H^2\Big|
$$

is included below:

$$
\begin{aligned}
\mathfrak W_{3,r}
={}&
\int d^4\theta_M\,d^2\bar\theta_H\,
\Bigl[
D_{s+}\bar D_s^2D_{s+}\Delta_{sM}
\Bigr]
\Bigl[
D_{s+}\mathscr P_{sH}
\Bigr]
\mathscr P_{MH}
\\
&\hspace{25mm}\times
\widetilde\phi_{r,M}^D
\widetilde\phi_{s,H}^E
\Big|_{\theta_s=0}.
\end{aligned}
$$

The $M$-to-$H$ chiral edge is $e=1$. Direct reduction gives

$$
\mathfrak W_{3,r}
=
512\,\bar r_1^{\,2}
\left(D_+\bar D_{\dot\alpha}C_{r,c}^D\right)
\left(D_+\bar D^{\dot\alpha}C_{s,c}^E\right).
$$

Since $C_{r,c}$ is antichiral,

$$
D_+C_{r,c}=0,
$$

and therefore

$$
D_+\bar D_{\dot\alpha}C_{r,c}
=
-2P_{\dot\alpha}C_{r,c}.
$$

Thus

$$
\boxed{
\mathfrak W_{3,r}
=
2048\,\bar r_1^{\,2}
\langle C_{r,c}^D,C_{s,c}^E\rangle.
}
$$

## 4.2 Color route

At the matter vertex,

$$
\kappa_{DX}(T_U)^X{}_C
=
ic_{UCD}.
$$

The $H_-$ color contraction gives

$$
\kappa^{BV}\kappa^{CC'}c_{VC'E}.
$$

Hence

$$
\begin{aligned}
\mathcal C_{G_{3,r}}
&=
\kappa^{AU}
\kappa_{DX}(T_U)^X{}_C
\kappa^{CC'}
\kappa^{BV}
c_{VC'E}
\\
&=
\boxed{
i\mathbb F^{AB}{}_{DE}.
}
\end{aligned}
$$

## 4.3 Scalar coefficient

The exponent vertices are

$$
+\frac{\sqrt2g}{\hbar}T_U,
\qquad
-\frac{\sqrt2g}{\hbar}
\varepsilon_{1rs}c.
$$

Therefore

$$
\begin{aligned}
S_{G_{3,r}}
&=
\left(-\frac{g^2}{4\sqrt2}\right)
\left(+\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\varepsilon_{1rs}\right)
\left(-\frac{\hbar^3}{256}\right)
\\
&=
-\varepsilon_{1rs}
\frac{\hbar g^4}{512\sqrt2}.
\end{aligned}
$$

Including color and physical-field conversion,

$$
S_{G_{3,r}}\mathcal C_{G_{3,r}}\,g^{-2}
=
-i\varepsilon_{1rs}
\frac{\hbar g^2}{512\sqrt2}
\mathbb F^{AB}{}_{DE}.
$$

Thus

$$
\begin{aligned}
\Gamma_{G_{3,r}}^{AB}
&=
-i\varepsilon_{1rs}
\frac{\hbar g^2}{512\sqrt2}
(2048)
\left(\frac1{32\pi^2}\right)
\mathbb F^{AB}{}_{DE}
\langle C_r^D,C_s^E\rangle
\\
&=
\boxed{
-i\sqrt2\,\varepsilon_{1rs}\lambda_1
\mathbb F^{AB}{}_{DE}
\langle C_r^D,C_s^E\rangle.
}
\end{aligned}
$$

### $G_{3,2}$

$$
\varepsilon_{123}=+1,
$$

so

$$
\boxed{
\Gamma_{G_{3,2}}^{AB}
=
-i\sqrt2\,\lambda_1
\mathbb F^{AB}{}_{DE}
\langle C_2^D,C_3^E\rangle.
}
$$

### $G_{3,3}$

$$
\varepsilon_{132}=-1,
$$

so

$$
\boxed{
\Gamma_{G_{3,3}}^{AB}
=
+i\sqrt2\,\lambda_1
\mathbb F^{AB}{}_{DE}
\langle C_3^D,C_2^E\rangle.
}
$$

# 5. Ordered-basis result

In the requested basis

$$
\left(
\langle B_1^D,D^E\rangle,\,
\langle D^D,B_1^E\rangle,\,
\langle C_3^D,C_2^E\rangle,\,
\langle C_2^D,C_3^E\rangle
\right),
$$

the four graph families give

$$
\begin{array}{c|c|c}
\text{Graph}&\text{Ordered structure}&\text{Coefficient}\\ \hline
G_2&
\langle B_1^D,D^E\rangle
&
+\lambda_1
\\[1mm]
G_1&
\langle D^D,B_1^E\rangle
&
+\lambda_1
\\[1mm]
G_{3,3}&
\langle C_3^D,C_2^E\rangle
&
+i\sqrt2\,\lambda_1
\\[1mm]
G_{3,2}&
\langle C_2^D,C_3^E\rangle
&
-i\sqrt2\,\lambda_1
\end{array}
$$

Therefore

$$
\boxed{
\begin{aligned}
\Gamma_{AB_1}^{AB}
=
\lambda_1\mathbb F^{AB}{}_{DE}
\Big[
&\langle B_1^D,D^E\rangle
+
\langle D^D,B_1^E\rangle
\\
&+
i\sqrt2\langle C_3^D,C_2^E\rangle
-
i\sqrt2\langle C_2^D,C_3^E\rangle
\Big].
\end{aligned}
}
$$

# 6. Post-calculation twist check

The independently calculated coefficient vector is

$$
\boxed{
(c_{B_1D},c_{DB_1},c_{C_3C_2},c_{C_2C_3})
=
\lambda_1(1,1,i\sqrt2,-i\sqrt2).
}
$$

Opening the supplied twist row only now gives the same vector.

No line requires repair or final rescaling.

| Audit location | Exact value |
| --- | --- |
| Source normalization | $-g^2/(4\sqrt2)$ |
| Distinct-vertex exponential factor | $1/2!\times2=1$ |
| $G_2$ identical-vertex factor | $1/2!\times2_{\rm labeled}=1$ |
| $G_1$ propagators | $+\hbar^3/16$ |
| $G_2,G_3$ propagators | $-\hbar^3/256$ |
| Gauge twelve-term Hessian | $+ig\,D_c(\bar D_C-\bar D_U)/(4\hbar)$ |
| $G_1$ $D$-word | $256\mathcal E_1+256\mathcal E_2$ |
| $G_2$ $D$-word | $-1024\sqrt2\,\mathcal E_1$ |
| $G_3$ $D$-word | $+2048\,\mathcal E_1$ |
| $G_1$ color | $+i\mathbb F$ |
| $G_2$ color | $-\mathbb F$ |
| $G_3$ color | $+i\mathbb F$ |
| Canonical-to-physical pair | $g^{-2}$ |
| Graph-specific $4-d$ | $0$ additional factors |
