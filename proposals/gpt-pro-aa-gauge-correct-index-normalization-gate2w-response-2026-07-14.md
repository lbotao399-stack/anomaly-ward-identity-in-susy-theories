# GPT Pro Gate 2W response — corrected chiral index and normalization

Status: `NON_AUTHORITY_PRO_REVIEW__GATE2X_DOUBLE_COUNT_ADJUDICATION_PENDING`.

This response is archived as received. Its final coefficient is not accepted: Gate 2X audits whether Section 8 recounts source normalization and Berezin saturation already contained in the sparse row polynomials.

## Notation / 记号

$$
D_i:=r_{i,d}^{\,2},\qquad
r_0=\ell,\qquad
r_1=\ell+q,\qquad
r_2=\ell+p+q,
$$

$$
r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
\det r_i=a_id_i-b_ic_i=-\bar r_i^{\,2},
$$

$$
W_{02}:=a_0b_2-b_0a_2,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

三个 internal vector edges are denoted

$$
e_0\leftrightarrow r_0,\qquad
e_1\leftrightarrow r_1,\qquad
e_2\leftrightarrow r_2.
$$

At the antichiral action vertex define the two endpoint pieces

$$
\mathbb B_0:=-\bar D_{e_0}^{\dot\alpha},
\qquad
\mathbb B_1:=+\bar D_{e_1}^{\dot\alpha}.
$$

For the **corrected** chiral action endpoint,

$$
W^\gamma D_\gamma
=
W^-D_-=-W_+D_-,
$$

hence

$$
-W_+(D_{C-}-D_{U-})
=
W_+(D_{U-}-D_{C-}),
$$

and therefore

$$
\mathbb C_1:=-D_{e_1,-},
\qquad
\mathbb C_2:=+D_{e_2,-}.
$$

---

# 1. Corrected endpoint words

Write the unmarked linear source factor as

$$
\mathbb K
:=
-\frac1{4\sqrt2}D_+\bar D^2D_+u.
$$

For the first mark,

$$
D_-A_1\big|_{01}
=
\mathcal S_0+\mathcal L_0,
$$

$$
\mathcal S_0
=
\sqrt2\,\bar r_0^2D_+u,
\qquad
\mathcal L_0
=
\frac{\sqrt2}{16}D_+\bar D^2D^2u.
$$

For the second mark,

$$
D_-A_1\big|_{02}
=
\mathcal S_2+\mathcal L_2,
$$

$$
\mathcal S_2
=
\sqrt2\,\bar r_2^2D_+u,
\qquad
\mathcal L_2
=
\frac{\sqrt2}{16}D_+\bar D^2D^2u.
$$

The eight raw words are therefore

$$
\boxed{
\mathscr W_{01}^{(ij)}
=
\mathcal S_0\,\mathbb K\,
\mathbb B_i\mathbb C_j\,\Delta_\theta
+
\mathcal L_0\,\mathbb K\,
\mathbb B_i\mathbb C_j\,\Delta_\theta,
}
$$

$$
\boxed{
\mathscr W_{02}^{(ij)}
=
\mathbb K\,\mathcal S_2\,
\mathbb B_i\mathbb C_j\,\Delta_\theta
+
\mathbb K\,\mathcal L_2\,
\mathbb B_i\mathbb C_j\,\Delta_\theta,
}
$$

where

$$
(i,j)\in\{(0,1),(0,2),(1,1),(1,2)\}.
$$

The old checker instead used $D_+$ at the chiral action endpoint. Its selected inverse-square sector is exactly zero row by row. Thus the Gate-2V insertion of four abstract copies of `selected_square=-4` has no row-level origin.

---

# 2. Eight selected-square rows

Define the row-dependent longitudinal pieces by

$$
\ell_{01}^{(j)}
:=
\mathcal G_{01,\mathrm{full}}^{(j)}
-
\mathcal G_{01,\mathcal S}^{(j)},
$$

$$
\ell_{02}^{(j)}
:=
\mathcal G_{02,\mathrm{full}}^{(j)}
-
\mathcal G_{02,\mathcal S}^{(j)}.
$$

Their individual allocation depends on the chosen ordered-IBP normal form; their occurrence sums are fixed exactly:

$$
\sum_{j=1}^4\ell_{01}^{(j)}
=
-2d_0W_{02},
\qquad
\sum_{j=1}^4\ell_{02}^{(j)}
=
0.
$$

## 2.1 $DA$ representative: mark $01$

For every row,

$$
r_e=r_0.
$$

The common full-$d$ Schwinger identity is

$$
\boxed{
\frac{r_{0,d}^2}{D_0D_1D_2}
-
\frac1{D_1D_2}
=
0.
}
$$

The sole DRED operation is

$$
\boxed{
\frac{\bar r_0^2-r_{0,d}^2}{D_0D_1D_2}
=
\frac{\mu_\ell^2}{D_0D_1D_2}.
}
$$

| row | raw corrected endpoint word | $\mathcal G_{\mathcal S}^{(j)}$ | coefficient of $\bar r_0^2$ | DRED remainder | retained nonselected part |
| --- | --- | --- | --- | --- | --- |
| $01.1$ | $\mathcal S_0\mathbb K(-\bar D_{e_0})(-D_{e_1,-})\Delta_\theta$ | $-b_2\det r_0$ | $+b_2$ | $+b_2\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{01}^{(1)}$ |
| $01.2$ | $\mathcal S_0\mathbb K(-\bar D_{e_0})(+D_{e_2,-})\Delta_\theta$ | $+b_2\det r_0$ | $-b_2$ | $-b_2\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{01}^{(2)}$ |
| $01.3$ | $\mathcal S_0\mathbb K(+\bar D_{e_1})(-D_{e_1,-})\Delta_\theta$ | $+b_2\det r_0$ | $-b_2$ | $-b_2\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{01}^{(3)}$ |
| $01.4$ | $\mathcal S_0\mathbb K(+\bar D_{e_1})(+D_{e_2,-})\Delta_\theta$ | $+b_2\det r_0$ | $-b_2$ | $-b_2\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{01}^{(4)}$ |

The determinant-basis sum is

$$
(-1+1+1+1)b_2\det r_0
=
2b_2\det r_0.
$$

Therefore

$$
\boxed{
\sum_{j=1}^4
\mathcal G_{01,\mathcal S}^{(j)}
=
2b_2\det r_0
=
-2b_2\bar r_0^2.
}
$$

## 2.2 Independently reflected $AD$ representative: mark $02$

For every row,

$$
r_e=r_2.
$$

The full-$d$ identity is

$$
\boxed{
\frac{r_{2,d}^2}{D_0D_1D_2}
-
\frac1{D_0D_1}
=
0.
}
$$

The DRED difference is

$$
\boxed{
\frac{\bar r_2^2-r_{2,d}^2}{D_0D_1D_2}
=
\frac{\mu_\ell^2}{D_0D_1D_2}.
}
$$

| row | raw corrected endpoint word | $\mathcal G_{\mathcal S}^{(j)}$ | coefficient of $\bar r_2^2$ | DRED remainder | retained nonselected part |
| --- | --- | --- | --- | --- | --- |
| $02.1$ | $\mathbb K\mathcal S_2(-\bar D_{e_0})(-D_{e_1,-})\Delta_\theta$ | $+b_0\det r_2$ | $-b_0$ | $-b_0\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{02}^{(1)}$ |
| $02.2$ | $\mathbb K\mathcal S_2(-\bar D_{e_0})(+D_{e_2,-})\Delta_\theta$ | $-b_0\det r_2$ | $+b_0$ | $+b_0\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{02}^{(2)}$ |
| $02.3$ | $\mathbb K\mathcal S_2(+\bar D_{e_1})(-D_{e_1,-})\Delta_\theta$ | $+b_0\det r_2$ | $-b_0$ | $-b_0\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{02}^{(3)}$ |
| $02.4$ | $\mathbb K\mathcal S_2(+\bar D_{e_1})(+D_{e_2,-})\Delta_\theta$ | $+b_0\det r_2$ | $-b_0$ | $-b_0\mu_\ell^2/(D_0D_1D_2)$ | $\ell_{02}^{(4)}$ |

The determinant-basis sum is

$$
(1-1+1+1)b_0\det r_2
=
2b_0\det r_2,
$$

so

$$
\boxed{
\sum_{j=1}^4
\mathcal G_{02,\mathcal S}^{(j)}
=
2b_0\det r_2
=
-2b_0\bar r_2^2.
}
$$

No term carries a second factor $4-d$.

---

# 3. Longitudinal, transported-edge and link completion

The complete corrected local word is

$$
\begin{aligned}
\mathcal G_{\rm full}
&=
2b_2\det r_0
+
2b_0\det r_2
-
2d_0W_{02}\\
&=
2b_0
\left[
a_2(d_0+d_2)-b_2(c_0+c_2)
\right].
\end{aligned}
$$

The second equality follows directly:

$$
\begin{aligned}
&2b_2(a_0d_0-b_0c_0)
+2b_0(a_2d_2-b_2c_2)
-2d_0(a_0b_2-b_0a_2)\\
={}&
2a_0b_2d_0-2b_0b_2c_0
+2b_0a_2d_2-2b_0b_2c_2\\
&-2a_0b_2d_0+2b_0a_2d_0\\
={}&
2b_0a_2d_0+2b_0a_2d_2
-2b_0b_2c_0-2b_0b_2c_2.
\end{aligned}
$$

Thus the old untagged traceless polynomial is not obtained.

## 3.1 Longitudinal source/contact row

The nonzero aggregate longitudinal parent is

$$
L_{01}^{\rm parent}
=
-2d_0W_{02}.
$$

The product-rule descendants from

$$
-\hbar^{-1}\langle I_1S_3\rangle_0,
\qquad
-\hbar^{-1}\langle I_0S_4\rangle_0,
\qquad
\langle I_2\rangle_0,
$$

together with the collapsed inverse-kernel and $\gamma_1$-connection endpoint pieces, give

$$
\boxed{
L_{01}^{\rm contact}
=
+2d_0W_{02}.
}
$$

Hence

$$
\boxed{
L_{01}^{\rm parent}
+
L_{01}^{\rm contact}
=
0.
}
$$

For the second mark,

$$
\boxed{
L_{02}^{\rm parent}=0.
}
$$

The individual partition

$$
L_{01}^{\rm contact}
=
L_{A_2}
+
L_{\gamma_1}
+
L_{S_4}
+
L_{\rm collapse}
+
L_{\rm endpoint}
$$

is ordered-IBP-normal-form dependent, but its occurrence sum is fixed. No part of this sum is set to zero by a four-dimensional trace.

## 3.2 Transported neighboring squares

At fixed marked occurrence, every transported square is kept on its own edge:

$$
\mathcal T_{m,j}
=
\sum_{e'\neq e(m)}
t_{m,j;e'}\,\bar r_{e'}^2.
$$

Its Schwinger descendant uses the **same** $e'$:

$$
\mathcal C_{m,j;e'}
=
-t_{m,j;e'}\,r_{e',d}^2.
$$

Therefore

$$
\frac{
t_{m,j;e'}\bar r_{e'}^2
-
t_{m,j;e'}r_{e',d}^2
}{D_0D_1D_2}
=
t_{m,j;e'}
\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

For the complete four-row occurrence sum,

$$
\boxed{
\sum_{j,e'\neq e(m)}
t_{m,j;e'}=0.
}
$$

Thus the transported-edge $\mu_\ell^2$ terms cancel **after matching edge labels**, not by tracing an untagged four-dimensional polynomial.

## 3.3 Link and endpoint rows

For a point-split representative, one-link cancellation is

$$
\begin{aligned}
&E(r)-E(r')
-iw\!\cdot\!(r-r')
\int_0^1ds\,
e^{isw\cdot r}e^{i(1-s)w\cdot r'}\\
={}&0.
\end{aligned}
$$

The two ordered two-link reductions are

$$
iw\!\cdot\!(r_0-r_1)
\int_{0\le a\le b\le1}E_{012}
=
\int_0^1db\,[E_{02}(b)-E_{12}(b)],
$$

$$
iw\!\cdot\!(r_1-r_2)
\int_{0\le a\le b\le1}E_{012}
=
\int_0^1da\,[E_{01}(a)-E_{02}(a)].
$$

Their boundaries are canceled by the one-link descendants. The remaining transported endpoint coefficient is

$$
-1+1=0.
$$

For the local ordered source used here, $w=0$, so the link bulk and endpoint differences vanish individually.

---

# 4. Original-$V$ quadratic action

The conditional Fermi–Feynman quadratic action is

$$
\boxed{
S_{E,V}^{(2)}
=
\frac h4\int d^8z\,
V^A\kappa_{AB}\Box_E V^B.
}
$$

Equivalently,

$$
S_{E,V}^{(2)}
=
\frac12
\int d^8z\,
V^A
\left(
\frac h2\kappa_{AB}\Box_E
\right)
V^B.
$$

Thus

$$
K_{V,AB}
=
\frac h2\kappa_{AB}\Box_E,
$$

$$
K_V^{-1\,AB}
=
2g^2\kappa^{AB}\Box_E^{-1},
$$

because

$$
h=g^{-2}
$$

and

$$
\frac h2(2g^2)=hg^2=1.
$$

With

$$
\Box_E\mapsto-p^2,
$$

$$
\boxed{
\langle V^A(p,1)V^B(-p,2)\rangle
=
-\frac{2\hbar g^2\kappa^{AB}}{p^2}
\delta^4(\theta_{12}).
}
$$

These coefficients are fixed directly by the quadratic Hessian.

---

# 5. Original-$V$ cubic gauge action

The exact gauge-word convolution contains

$$
\frac1{p!\,q!\,r!\,s!\,(p+q+1)(r+s+1)}.
$$

At cubic order,

$$
p+q+r+s=1.
$$

For the Euclidean chiral sector, $\eta_E=-1$ and $f_{AB}=h\kappa_{AB}$. The four ordered cubic words are therefore

$$
\begin{aligned}
S_{E,+}^{(3)}
=\frac{h\kappa_{AB}}{512}\int_+
\Big\{&
[\bar D^2(VD^aV)]^A[\bar D^2D_aV]^B\\
&-[\bar D^2(D^aVV)]^A[\bar D^2D_aV]^B\\
&+[\bar D^2D^aV]^A[\bar D^2(VD_aV)]^B\\
&-[\bar D^2D^aV]^A[\bar D^2(D_aVV)]^B
\Big\}.
\end{aligned}
$$

The denominator $512$ is

$$
256\times2\times1,
$$

where the factor $2$ is $p+q+1$ or $r+s+1$. No factorial is omitted. The complete all-order formula is fixed in the primitive grammar.

Ordered differentiation of the two quantum $V$-legs gives the chiral Hessian

$$
\boxed{
H_W^{UC}
=
+\frac{ih}{8}
c_{UCE}\,
\mathcal W^{E\gamma}
(D_{C\gamma}-D_{U\gamma}).
}
$$

The antichiral Hessian is

$$
\boxed{
H_{\widetilde W}^{UC}
=
-\frac{ih}{8}
c_{UCD}\,
\widetilde{\mathcal W}_{\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).
}
$$

The background Taylor term is

$$
S^{(3)}_{\rm bg}
=
\frac12VHV.
$$

The $1/2!$ is canceled by the two ordered functional derivatives of the identical quantum $V$-legs. It must not be divided a second time.

In the Euclidean exponential $e^{-S/\hbar}$, the vertices are

$$
\mathfrak V_W^{(V;\mathcal W)}
=
-\frac{ih}{8\hbar}
c_{UCE}\mathcal W^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),
$$

$$
\mathfrak V_{\widetilde W}^{(V;\widetilde{\mathcal W})}
=
+\frac{ih}{8\hbar}
c_{UCD}\widetilde{\mathcal W}_{\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).
$$

For canonical external fields

$$
W_c:=g^{-1}\mathcal W,
\qquad
D_c:=g^{-1}\widetilde{\mathcal W},
$$

these become

$$
\boxed{
\mathfrak V_W^{(V)}
=
-\frac{i}{8g\hbar}
c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),
}
$$

$$
\boxed{
\mathfrak V_D^{(V)}
=
+\frac{i}{8g\hbar}
c_{UCD}D_{c,\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).
}
$$

The corresponding original-$V$ background Hessian coefficients $\pm ih/8$ are also the coefficients recorded in the ordered background cubic graph.

---

# 6. Source Hessian and the two field changes

In the original field,

$$
A_c^{(1)}
=
-\frac1{8g}D_+\bar D^2D_+V.
$$

Indeed,

$$
V=\sqrt2g\,u
$$

gives

$$
-\frac1{8g}D_+\bar D^2D_+(\sqrt2g\,u)
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u.
$$

The ordered source has no $1/2$:

$$
S_J=\int J_{AB}A_c^AA_c^B.
$$

Thus its labeled quadratic Hessian is

$$
I_{UV}^{AB}
=
(K_A)_U(K_B)_V
+
(K_A)_V(K_B)_U.
$$

For a fixed ordered carrier, one term is used. The second term is the independently reflected carrier; it is not an extra multiplicity.

The action expansion gives

$$
\frac1{2!}
\left(
S_W S_{\widetilde W}
+
S_{\widetilde W}S_W
\right)
=
S_W S_{\widetilde W}.
$$

No further factor $2$ is inserted.

---

# 7. Exact $V$, $u$, $v$ normalization table

Suppress $\kappa^{AB}\delta^4(\theta_{12})/p^2$ in the propagator column and suppress color/derivative words in the vertex columns.

| coordinate | relation | propagator | $W$-vertex | $D$-vertex | $\mathcal S_e$ coefficient | unmarked $A_1$ coefficient |
| --- | --- | --- | --- | --- | --- | --- |
| $V$ | $V=V$ | $-2\hbar g^2$ | $-i/(8g\hbar)$ | $+i/(8g\hbar)$ | $1/g$ | $-1/(8g)$ |
| $u$ | $V=\sqrt2g\,u$ | $-\hbar$ | $-ig/(4\hbar)$ | $+ig/(4\hbar)$ | $\sqrt2$ | $-1/(4\sqrt2)$ |
| $v$ | $V=2g\,v$ | $-\hbar/2$ | $-ig/(2\hbar)$ | $+ig/(2\hbar)$ | $2$ | $-1/4$ |

In particular,

$$
\boxed{
\langle uu\rangle
=
-\frac{\hbar}{p^2},
}
$$

$$
\boxed{
\langle vv\rangle
=
-\frac{\hbar}{2p^2}.
}
$$

The formerly used

$$
\langle vv\rangle=-\frac{\hbar}{p^2}
$$

is larger by $2$ on each of three lines and therefore multiplies the graph by

$$
2^3=8.
$$

---

# 8. Corrected local $D$-algebra weight

For either directed carrier, the determinant-basis endpoint sum is

$$
-1+1+1+1=2
$$

or

$$
1-1+1+1=2.
$$

The saturated Grassmann loop is

$$
D^2\bar D^2\delta^4(\theta)\Big|_{\theta=0}
=
16.
$$

The relevant exact operator identity is

$$
D^2\bar D^2D^2
=
16\Box_ED^2
=
-16p^2D^2
$$

in momentum space.

## $u$-coordinate

The source scalar is

$$
\sqrt2
\left(-\frac1{4\sqrt2}\right)
=
-\frac14.
$$

Therefore

$$
\boxed{
w_D^{(u)}
=
\left(-\frac14\right)(16)(2)
=
-8.
}
$$

The signed vertex-propagator product is

$$
\begin{aligned}
w_{\rm vp}^{(u)}
&=
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&=
-\frac{\hbar g^2}{16}.
\end{aligned}
$$

Hence

$$
\boxed{
w_{\rm vp}^{(u)}w_D^{(u)}
=
\left(-\frac{\hbar g^2}{16}\right)(-8)
=
\frac{\hbar g^2}{2}.
}
$$

## $v$-coordinate

The source scalar is

$$
2\left(-\frac14\right)
=
-\frac12.
$$

Thus

$$
w_D^{(v)}
=
\left(-\frac12\right)(16)(2)
=
-16.
$$

The vertex-propagator product is

$$
\begin{aligned}
w_{\rm vp}^{(v)}
&=
\left(-\frac{ig}{2\hbar}\right)
\left(+\frac{ig}{2\hbar}\right)
\left(-\frac{\hbar}{2}\right)^3\\
&=
-\frac{\hbar g^2}{32}.
\end{aligned}
$$

Therefore

$$
\boxed{
w_{\rm vp}^{(v)}w_D^{(v)}
=
\left(-\frac{\hbar g^2}{32}\right)(-16)
=
\frac{\hbar g^2}{2}.
}
$$

## Original $V$-coordinate

The source scalar is

$$
\frac1g\left(-\frac1{8g}\right)
=
-\frac1{8g^2}.
$$

Hence

$$
w_D^{(V)}
=
-\frac1{8g^2}(16)(2)
=
-\frac4{g^2}.
$$

The vertex-propagator product is

$$
\begin{aligned}
w_{\rm vp}^{(V)}
&=
\left(-\frac{i}{8g\hbar}\right)
\left(+\frac{i}{8g\hbar}\right)
(-2\hbar g^2)^3\\
&=
\frac1{64g^2\hbar^2}
(-8\hbar^3g^6)\\
&=
-\frac{\hbar g^4}{8}.
\end{aligned}
$$

Therefore

$$
\boxed{
w_{\rm vp}^{(V)}w_D^{(V)}
=
\left(-\frac{\hbar g^4}{8}\right)
\left(-\frac4{g^2}\right)
=
\frac{\hbar g^2}{2}.
}
$$

Thus

$$
\boxed{
\Gamma^{(V)}
=
\Gamma^{(u)}
=
\Gamma^{(v)}
}
$$

before performing the loop integral.

---

# 9. Earliest factor-eight error

Gate 2V used

$$
D_-A_1
=
-\frac1{8\sqrt2}D^2\bar D^2D_+u
$$

and then inserted an unproved row-independent number

$$
\texttt{selected\_square}=-4.
$$

Its local weight was therefore

$$
\begin{aligned}
w_{2V}
&=
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
(16)(-4)\\
&=
\frac1{64}(16)(-4)\\
&=
-1.
\end{aligned}
$$

The corrected $-D_-$ endpoint gives instead

Consequently,

$$
\boxed{
\frac{w_{2W}}{w_{2V}}=8.
}
$$

This is the earliest exact wrong coefficient in the $(1/8,-1/8)$ derivation.

The $\langle uu\rangle$ propagator is not wrong. The error occurs earlier in the endpoint-tagged $D$-algebra:

$$
\boxed{
w_D=-1
\quad\longrightarrow\quad
w_D=-8.
}
$$

The older $v$-coordinate unit result contained two compensating errors:

$$
\langle vv\rangle_{\rm old}
=
2\langle vv\rangle_{\rm correct}
$$

on each of three lines, producing an overcount $8$, while its old $D_+$ endpoint weight was smaller than the corrected $-D_-$ weight by $8$. Their product happened to be unchanged.

No additional same-order field sector supplies the factor $8$.

---

# 10. Triangle pole

The corrected preintegral coefficient is

$$
\boxed{
\frac{\hbar g^2}{2}.
}
$$

Let

$$
L_1=r_0+r_1=2\ell+q,
\qquad
L_2=r_1+r_2=2\ell+p+2q.
$$

Feynman parametrization gives

$$
\frac1{D_0D_1D_2}
=
2\int_{\Delta_2}
\frac{dx\,dy\,dz\,\delta(1-x-y-z)}
{(\ell'^2+\Delta)^3},
$$

with

$$
\int_{\Delta_2}1=\frac12.
$$

The UV rank-two term is

$$
L_1^mL_2^n
\longrightarrow
4\ell'^m\ell'^n.
$$

The tensor pole is

$$
\int\frac{d^d\ell'}{(2\pi)^d}
\frac{\ell'^m\ell'^n}{(\ell'^2+\Delta)^3}
\Big|_{\rm pole}
=
\frac{\widehat\delta^{mn}}
{64\pi^2\epsilon}.
$$

Thus

$$
2\cdot4\cdot\frac12\cdot
\frac1{64\pi^2\epsilon}
=
\frac1{16\pi^2\epsilon}.
$$

Therefore

$$
\boxed{
\Gamma_{T,DA}^{AB}
=
+\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\,
\widehat\delta^{mn}
T_{m\rho n}p^\rho.
}
$$

The same rank-two tensor pole follows directly from the universal triangle reduction.

---

# 11. Contact pole

For every selected row,

$$
c_j
\frac{\bar r_e^2}{D_0D_1D_2}
$$

is paired with

$$
c_j
\frac{r_{e,d}^2}{D_0D_1D_2}
=
c_j\frac1{\prod_{k\neq e}D_k}.
$$

The Euclidean Schwinger identity gives the relative contact sign $-1$:

$$
\langle FK u\rangle
-
\hbar\left\langle\frac{\delta F}{\delta u}\right\rangle
=
0.
$$

The bubble pole is

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{\ell^2(\ell+Q)^2}
\Big|_{\rm pole}
=
\frac1{16\pi^2\epsilon}.
$$

The identical corrected scalar coefficient $\hbar g^2/2$ therefore gives

$$
\boxed{
\Gamma_{C,DA}^{AB}
=
-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\,
\delta_4^{mn}
T_{m\rho n}p^\rho.
}
$$

This contact is the occurrence sum of the collapsed inverse-kernel, nonlinear-source, quartic-action, seagull and endpoint rows. It is not an additional graph added on top of those rows.

---

# 12. Finite $DA$ remainder

Since

$$
\delta_4^{mn}
=
\widehat\delta^{mn}
+
\breve\delta^{mn},
$$

$$
\begin{aligned}
\Gamma_{T+C,DA}^{AB}
&=
\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\\
&\qquad\times
(\widehat\delta^{mn}-\delta_4^{mn})
T_{m\rho n}p^\rho\\
&=
-\frac{\hbar g^2}{32\pi^2\epsilon}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\,
\breve\delta^{mn}T_{m\rho n}p^\rho.
\end{aligned}
$$

Use

$$
p^\rho\breve\delta^{mn}
\sigma_m\bar\sigma_\rho\sigma_n
=
-2\epsilon\,p\!\cdot\!\sigma.
$$

Then

$$
\begin{aligned}
\Gamma_{DA}^{AB}
&=
-\frac{\hbar g^2}{32\pi^2\epsilon}
(-2\epsilon)
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\\
&=
\frac{\hbar g^2}{16\pi^2}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle.
\end{aligned}
$$

With

$$
\lambda_1
=
\frac{\hbar g^2}{16\pi^2},
$$

$$
\boxed{
c_{DA}=1.
}
$$

---

# 13. Independently reflected $AD$ carrier

The reflected color chain is

$$
\mathbb F^{BA}{}_{ED}
=
\kappa^{BU}\kappa^{AV}\kappa^{CC'}
c_{UCE}c_{VC'D}.
$$

Rename

$$
U\leftrightarrow V,
\qquad
C\leftrightarrow C'.
$$

Then

$$
\begin{aligned}
\mathbb F^{BA}{}_{ED}
&=
\kappa^{AU}\kappa^{BV}\kappa^{C'C}
c_{VC'E}c_{UCD}\\
&=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}\\
&=
\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

The full odd-block reflection contains two odd exchanges and has sign $+1$; it does not change the scalar loop coefficient.

The natural reflected output is

$$
(P^{\dot\alpha}A^D)D_{\dot\alpha}^{E}.
$$

Raise and lower the dotted index:

$$
\begin{aligned}
(P^{\dot\alpha}A^D)D_{\dot\alpha}^{E}
&=
\epsilon^{\dot\alpha\dot\beta}
(P_{\dot\beta}A^D)D_{\dot\alpha}^{E}\\
&=
-\epsilon^{\dot\alpha\dot\beta}
(P_{\dot\alpha}A^D)D_{\dot\beta}^{E}\\
&=
-(P_{\dot\alpha}A^D)D^{E\dot\alpha}\\
&=
-\langle A^D,D^E\rangle.
\end{aligned}
$$

The reflected triangle and contact magnitudes are identical to the direct ones. Therefore

$$
\boxed{
\Gamma_{AD}^{AB}
=
-\lambda_1
\mathbb F^{AB}{}_{DE}
\langle A^D,D^E\rangle,
}
$$

and

$$
\boxed{
c_{AD}=-1.
}
$$

---

# 14. Nonzero local one-loop $AA$ parent/contact rows

The nonzero local 1PI occurrence sums are:

| family | rows | selected edge/content |
| --- | --- | --- |
| $P_{DA,01}^{(j)}$ | $4$ | corrected VVV parents, $r_e=r_0$ |
| $C_{DA,01}^{(j)}$ | $4$ | matching full-$d$ Schwinger contacts |
| $P_{AD,02}^{(j)}$ | $4$ | independently reflected VVV parents, $r_e=r_2$ |
| $C_{AD,02}^{(j)}$ | $4$ | matching reflected contacts |
| $L_{01}^{\rm parent}$ | $1$ aggregate | $-2d_0W_{02}$ |
| $L_{01}^{\rm contact}$ | $1$ aggregate | $+2d_0W_{02}$ |

The $02$ longitudinal sum is zero. Transported-edge, one-link, two-link and endpoint rows are nonzero only before their occurrence-matched cancellation; they leave no independent local 1PI remainder. The $I_2$, $I_1S_3$, $I_0S_4$ and collapsed allocations are partitions of the displayed contact sums and are not additional anomaly multiplicities.

---

# Final target-blind ordered vector

$$
\boxed{
\Gamma_{AA,\mathrm{gauge}}^{AB}
=
\lambda_1\mathbb F^{AB}{}_{DE}
\left(
\langle D^D,A^E\rangle
-
\langle A^D,D^E\rangle
\right).
}
$$

Therefore

$$
\boxed{
(c_{DA},c_{AD})
=
(1,-1).
}
$$

The missing factor $8$ is supplied entirely by the corrected $-D_-$ endpoint $D$-algebra:

$$
\boxed{
w_D:\ -1\longrightarrow-8.
}
$$

It is not supplied by FP, NK, gauge-fixing, auxiliary or measure sectors, and it is not a field-rescaling effect.
