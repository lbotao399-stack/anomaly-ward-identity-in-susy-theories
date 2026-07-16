## Notation / 记号

$$
r_0=\ell,\qquad r_1=\ell+q,\qquad r_2=\ell+p+q,
$$

$$
D_i:=r_{i,d}^{\,2},\qquad
\bar r_i^{\,2}=r_{i,d}^{\,2}+\mu_\ell^2,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

三个 quantum-vector edges 为

$$
e_0=(0,1),\qquad e_1=(1,2),\qquad e_2=(2,0).
$$

令

$$
\Delta_\theta
:=
\delta_{01}^4(r_0)\,
\delta_{12}^4(r_1)\,
\delta_{20}^4(r_2),
$$

并把 source coefficients 暂时抽出，定义 raw operators

$$
\mathcal K_e
:=
\left.D_{0+}\bar D_0^2D_{0+}\right|_{e},
\qquad
\mathcal M_e
:=
\left.D_{0-}D_{0+}\bar D_0^2D_{0+}\right|_{e}.
$$

所有 operator words 中，**rightmost operator acts first**。

Ordered output carriers 定义为

$$
\langle D^D,A^E\rangle
:=
D_{\dot\alpha}^D\,P^{\dot\alpha}A^E,
$$

$$
\langle A^D,D^E\rangle
:=
(P_{\dot\alpha}A^D)\,D^{E\dot\alpha}.
$$

The four endpoint assignments are exactly

$$
(\bar e,d e)
=
(e_0,e_1),\ (e_0,e_2),\ (e_1,e_1),\ (e_1,e_2),
$$

with the raw derivative-word template recorded by the edge-tagged seed checker.

---

# 1. Canonical common factor

The two source factors are

$$
A_{c}^{(1)}
=
-\frac1{4\sqrt2}D_+\bar D^2D_+u,
$$

$$
\begin{aligned}
D_-A_c^{(1)}
&=
-\frac1{4\sqrt2}
D_-D_+\bar D^2D_+u\\
&=
-\frac1{4\sqrt2}
\left(\frac12D^2\right)\bar D^2D_+u\\
&=
-\frac1{8\sqrt2}D^2\bar D^2D_+u.
\end{aligned}
$$

Thus, for either marked placement,

$$
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=
\frac1{64}.
$$

The exponent-vertex and propagator product is

$$
\begin{aligned}
\mathcal C_{\mathrm{vp}}
&=
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&=
\frac{(-i)(+i)g^2}{16\hbar^2}
(-\hbar^3)\\
&=
\frac{(+1)g^2}{16\hbar^2}
(-\hbar^3)\\
&=
-\frac{\hbar g^2}{16}.
\end{aligned}
$$

The $1/2!$ in the two-action-vertex expansion cancels the two ordered placements:

$$
\frac1{2!}
\left(
\mathfrak V_{\widetilde W}\mathfrak V_W
+
\mathfrak V_W\mathfrak V_{\widetilde W}
\right)
=
\mathfrak V_{\widetilde W}\mathfrak V_W.
$$

The closed Grassmann loop is

$$
D^2\bar D^2\delta^4(\theta)\Big|_{\theta=0}
=
(-4)(-4)
=
16.
$$

Before extracting an inverse square, the exact common scalar is therefore

$$
\begin{aligned}
\mathcal C_{\rm common}
&=
\left(-\frac{\hbar g^2}{16}\right)
\left(\frac1{64}\right)(16)\\
&=
-\frac{\hbar g^2}{64}.
\end{aligned}
$$

---

# 2. Eight endpoint-tagged raw words

## 2.1 `mark01`: $D_-$ on the first source occurrence

The selected inverse-kernel occurrence is $e_0$, hence

$$
r_e=r_0.
$$

This agrees with the occurrence-level Schwinger map: the left marked source occurrence cuts $e_0$, while the right marked source occurrence cuts $e_2$.

### `mark01-1`

$$
\boxed{
\mathscr W_{01;01}
=
\mathcal M_{e_0}\mathcal K_{e_2}
(\bar D_1^{\dot\alpha})_{e_0}
(D_{2\alpha})_{e_1}
\Delta_\theta
}
$$

The exact exterior-algebra normal form is zero **before** any four-dimensional Clifford or metric identity:

$$
\operatorname{NF}(\mathscr W_{01;01})=0.
$$

Hence

$$
\text{inverse-square coefficient}=0,
\qquad
\text{Schwinger contact}=0,
\qquad
\text{DRED remainder}=0.
$$

### `mark01-2`

$$
\boxed{
\mathscr W_{01;02}
=
\mathcal M_{e_0}\mathcal K_{e_2}
(\bar D_1^{\dot\alpha})_{e_0}
(D_{2\alpha})_{e_2}
\Delta_\theta
}
$$

Its displayed component projection is

$$
+b_1W_{02},
\qquad
W_{02}:=a_0b_2-b_0a_2.
$$

The selected edge is

$$
r_e=r_0.
$$

### `mark01-3`

$$
\boxed{
\mathscr W_{01;11}
=
\mathcal M_{e_0}\mathcal K_{e_2}
(\bar D_1^{\dot\alpha})_{e_1}
(D_{2\alpha})_{e_1}
\Delta_\theta
}
$$

Again the complete exterior normal form vanishes before a four-dimensional metric contraction:

$$
\operatorname{NF}(\mathscr W_{01;11})=0.
$$

Therefore

$$
\text{inverse-square coefficient}=0,
\qquad
\text{Schwinger contact}=0,
\qquad
\text{DRED remainder}=0.
$$

### `mark01-4`

$$
\boxed{
\mathscr W_{01;12}
=
\mathcal M_{e_0}\mathcal K_{e_2}
(\bar D_1^{\dot\alpha})_{e_1}
(D_{2\alpha})_{e_2}
\Delta_\theta
}
$$

Its displayed component projection is

$$
+b_0W_{02}.
$$

The selected edge remains

$$
r_e=r_0.
$$

---

## 2.2 `mark02`: $D_-$ on the second source occurrence

Now the selected inverse-kernel occurrence is $e_2$:

$$
r_e=r_2.
$$

### `mark02-1`

$$
\boxed{
\mathscr W_{02;01}
=
\mathcal K_{e_0}\mathcal M_{e_2}
(\bar D_1^{\dot\alpha})_{e_0}
(D_{2\alpha})_{e_1}
\Delta_\theta
}
$$

Its exact exterior normal form is

$$
\operatorname{NF}(\mathscr W_{02;01})=0,
$$

so no square or contact is generated.

### `mark02-2`

$$
\boxed{
\mathscr W_{02;02}
=
\mathcal K_{e_0}\mathcal M_{e_2}
(\bar D_1^{\dot\alpha})_{e_0}
(D_{2\alpha})_{e_2}
\Delta_\theta
}
$$

Its displayed component projection is

$$
-b_1W_{02},
$$

but its selected inverse-kernel edge is

$$
r_e=r_2.
$$

The minus sign in the untagged component projection is not the selected-square coefficient; it also contains transported $e_0,e_1$ pieces.

### `mark02-3`

$$
\boxed{
\mathscr W_{02;11}
=
\mathcal K_{e_0}\mathcal M_{e_2}
(\bar D_1^{\dot\alpha})_{e_1}
(D_{2\alpha})_{e_1}
\Delta_\theta
}
$$

The exact exterior normal form is zero:

$$
\operatorname{NF}(\mathscr W_{02;11})=0.
$$

### `mark02-4`

$$
\boxed{
\mathscr W_{02;12}
=
\mathcal K_{e_0}\mathcal M_{e_2}
(\bar D_1^{\dot\alpha})_{e_1}
(D_{2\alpha})_{e_2}
\Delta_\theta
}
$$

Its displayed component projection is

$$
+b_0W_{02},
$$

and the selected edge is

$$
r_e=r_2.
$$

The same eight raw endpoint words, with the two $D_-$ placements kept distinct, are the ordered seed rows; they must not be collapsed into an overall multiplicity.

---

# 3. Derivation of `selected_square = -4`

For every one of the four nonzero endpoint words, normal ordering to the selected edge produces

$$
\operatorname{NF}_{e}(\mathscr W)
=
\frac14
D_e^2\bar D_e^2D_e^2\,
\mathcal R_e
+
\mathcal T_e.
$$

Here:

- $\mathcal R_e$ is the remaining external carrier;

- $\mathcal T_e$ is defined as the sum of all terms whose momentum-square tag is an edge $e'\neq e$, together with rank-one and longitudinal words.

The factor $1/4$ is not inserted. It comes from the two ordered same-chirality pair reductions:

$$
D_\alpha D_\beta
=
-\frac12\epsilon_{\alpha\beta}D^2,
$$

$$
\bar D_{\dot\alpha}\bar D_{\dot\beta}
=
-\frac12\epsilon_{\dot\alpha\dot\beta}\bar D^2,
$$

hence

$$
\left(-\frac12\right)
\left(-\frac12\right)
=
\frac14.
$$

The exact Euclidean operator identity is

$$
D_e^2\bar D_e^2D_e^2
=
-16\,\bar r_e^{\,2}D_e^2.
$$

The exact $16\times16$ superspace operator checker verifies precisely

$$
D^2\bar D^2D^2=-16p^2D^2.
$$

Therefore

$$
\begin{aligned}
\frac14D_e^2\bar D_e^2D_e^2
&=
\frac14(-16\bar r_e^{\,2})D_e^2\\
&=
-4\bar r_e^{\,2}D_e^2.
\end{aligned}
$$

Thus the endpoint-local scalar is

$$
\boxed{\texttt{selected\_square}=-4}
$$

**for each nonzero endpoint occurrence**:

$$
\boxed{
(-4,-4,-4,-4)
}
$$

for

$$
(01;02),\quad(01;12),\quad(02;02),\quad(02;12).
$$

It is not one $-4$ attached to the already-summed polynomial $G_1$ or $G_2$.

---

# 4. Why the four-dimensional trace zero does not remove these terms

With

$$
a_i=-r_{i3}-ir_{i4},
\qquad
b_i=-r_{i1}+ir_{i2},
$$

and

$$
p=(1,0,0,0),
\qquad
q=(0,0,0,1),
$$

we have

$$
b_1=b_0.
$$

The untagged sums are

$$
G_1
=
(b_0+b_1)W_{02}
=
2b_0W_{02},
$$

$$
G_2
=
(b_0-b_1)W_{02}
=
0.
$$

Writing $r_0=(\ell_1,\ell_2,\ell_3,\ell_4)$, the rank-two part of $iG_1$ is

$$
\begin{aligned}
(iG_1)_{\operatorname{rank}2}
={}&
-2\ell_1^2+2\ell_2^2
+2\ell_1\ell_4-2\ell_2\ell_3\\
&+i\left(
4\ell_1\ell_2
-2\ell_1\ell_3
-2\ell_2\ell_4
\right).
\end{aligned}
$$

Hence its diagonal coefficients are

$$
(-2,+2,0,0)
$$

and

$$
-2+2+0+0=0.
$$

But this trace is taken **after deleting the edge tags**. In the edge-tagged normal form:

$$
G_1
=
\underbrace{
(-4\bar r_0^2)+(-4\bar r_0^2)
}_{\text{selected }e_0}
+
\underbrace{\mathcal T_{01;02}+\mathcal T_{01;12}}
_{\text{transported }e_1,e_2},
$$

while

$$
G_2
=
\underbrace{
(-4\bar r_2^2)+(-4\bar r_2^2)
}_{\text{selected }e_2}
+
\underbrace{\mathcal T_{02;02}+\mathcal T_{02;12}}
_{\text{transported }e_0,e_1}.
$$

The ordinary trace zero mixes

$$
e_0,\ e_1,\ e_2
$$

before each inverse square has been paired with its own Schwinger contact. It therefore cannot be used to set the selected-edge coefficients to zero.

The transported terms satisfy their own full-$d$ product-rule contacts. Their parent-minus-contact sums vanish before the selected-edge DRED operation:

$$
\sum\mathcal T_{\rm parent}
-
\sum\mathcal T_{\rm contact}
=
0.
$$

No transported square is silently discarded.

---

# 5. Full-$d$ Schwinger contacts endpoint by endpoint

## 5.1 `mark01-2` and `mark01-4`

For both rows,

$$
e=e_0,
\qquad
r_e=r_0.
$$

The exact full-$d$ contact is

$$
\boxed{
\frac{r_{0,d}^2}{D_0D_1D_2}
-
\frac1{D_1D_2}
=
0
}
$$

because

$$
D_0=r_{0,d}^2.
$$

The four-dimensional parent square is

$$
-4\frac{\bar r_0^2}{D_0D_1D_2}.
$$

The corresponding full-$d$ cut is

$$
-4\frac{r_{0,d}^2}{D_0D_1D_2}.
$$

Therefore, separately for `mark01-2` and `mark01-4`,

$$
\begin{aligned}
\mathscr A_{01;i}
&=
-4
\left[
\frac{\bar r_0^2}{D_0D_1D_2}
-
\frac{r_{0,d}^2}{D_0D_1D_2}
\right]\\
&=
-4
\frac{\bar r_0^2-r_{0,d}^2}
{D_0D_1D_2}\\
&=
\boxed{
-4\frac{\mu_\ell^2}{D_0D_1D_2}
},
\qquad i=2,4.
\end{aligned}
$$

## 5.2 `mark02-2` and `mark02-4`

For both rows,

$$
e=e_2,
\qquad
r_e=r_2.
$$

The exact full-$d$ contact is

$$
\boxed{
\frac{r_{2,d}^2}{D_0D_1D_2}
-
\frac1{D_0D_1}
=
0
}
$$

because

$$
D_2=r_{2,d}^2.
$$

Thus, independently for `mark02-2` and `mark02-4`,

$$
\begin{aligned}
\mathscr A_{02;i}
&=
-4
\left[
\frac{\bar r_2^2}{D_0D_1D_2}
-
\frac{r_{2,d}^2}{D_0D_1D_2}
\right]\\
&=
-4
\frac{\bar r_2^2-r_{2,d}^2}
{D_0D_1D_2}\\
&=
\boxed{
-4\frac{\mu_\ell^2}{D_0D_1D_2}
},
\qquad i=2,4.
\end{aligned}
$$

There is exactly one DRED mismatch:

$$
\bar r_e^2-r_{e,d}^2=\mu_\ell^2.
$$

There is no additional factor $4-d$.

---

# 6. Scalar coefficient per endpoint

For each of the four nonzero endpoint occurrences,

$$
\begin{aligned}
\mathcal C_{\rm endpoint}
&=
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&\quad\times
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
(16)(-4).
\end{aligned}
$$

Calculate every factor:

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
=
-\frac{\hbar g^2}{16},
$$

$$
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=
\frac1{64},
$$

$$
\frac1{64}(16)(-4)
=
-1.
$$

Hence

$$
\boxed{
\mathcal C_{\rm endpoint}
=
+\frac{\hbar g^2}{16}.
}
$$

The finite endpoint contribution is

$$
\begin{aligned}
\Gamma_{\rm endpoint}
&=
\frac{\hbar g^2}{16}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}\\
&=
\frac{\hbar g^2}{16}
\frac1{32\pi^2}\\
&=
\frac{\hbar g^2}{512\pi^2}.
\end{aligned}
$$

Since

$$
\lambda_1
=
\frac{\hbar g^2}{16\pi^2},
$$

we obtain

$$
\frac{\hbar g^2}{512\pi^2}
=
\frac1{32}
\frac{\hbar g^2}{16\pi^2}
=
\boxed{\frac{\lambda_1}{32}}.
$$

Thus every nonzero endpoint contributes

$$
\boxed{
+\frac{\lambda_1}{32}
}
$$

in its natural directed carrier.

---

# 7. Direct $DA$ carrier

For the direct orientation

$$
A\longrightarrow\widetilde W^D,
\qquad
B\longrightarrow W^E,
$$

the two source marks and their two nonzero endpoint rows are distinct:

$$
(01;02),\quad(01;12),\quad
(02;02),\quad(02;12).
$$

Therefore

$$
\begin{aligned}
\Gamma_{DA}^{AB}
&=
4\left(\frac{\lambda_1}{32}\right)
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle\\
&=
\boxed{
\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}
\langle D^D,A^E\rangle
}.
\end{aligned}
$$

Hence

$$
\boxed{c_{DA}=\frac18}.
$$

---

# 8. Independently reflected $AD$ carrier

The reflected color chain is

$$
\mathbb F^{BA}{}_{ED}
=
\kappa^{BU}\kappa^{AV}\kappa^{CC'}
c_{UCE}c_{VC'D}.
$$

Exchange the dummy labels

$$
U\leftrightarrow V,
\qquad
C\leftrightarrow C':
$$

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
\boxed{\mathbb F^{AB}{}_{DE}}.
\end{aligned}
$$

The four reflected endpoint rows have the same natural scalar contribution,

$$
4\left(\frac{\lambda_1}{32}\right)
=
\frac{\lambda_1}{8}.
$$

Their natural dotted-spinor ordering is

$$
(P^{\dot\alpha}A^D)D_{\dot\alpha}^E.
$$

Convert it to the declared $AD$ carrier:

$$
\begin{aligned}
(P^{\dot\alpha}A^D)D_{\dot\alpha}^E
&=
\epsilon^{\dot\alpha\dot\beta}
(P_{\dot\beta}A^D)D_{\dot\alpha}^E\\
&=
-\epsilon^{\dot\alpha\dot\beta}
(P_{\dot\alpha}A^D)D_{\dot\beta}^E\\
&=
-(P_{\dot\alpha}A^D)D^{E\dot\alpha}\\
&=
-\langle A^D,D^E\rangle.
\end{aligned}
$$

Therefore

$$
\boxed{
\Gamma_{AD}^{AB}
=
-\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}
\langle A^D,D^E\rangle
}
$$

and

$$
\boxed{c_{AD}=-\frac18}.
$$

---

# 9. Gate 2V result

Combining the independently calculated carriers,

$$
\boxed{
\Gamma_{AA,\mathrm{VVV+SD}}^{AB}
=
\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac18\langle D^D,A^E\rangle
-
\frac18\langle A^D,D^E\rangle
\right].
}
$$

Thus the target-blind ordered coefficient vector is

$$
\boxed{
(c_{DA},c_{AD})
=
\left(
\frac18,-\frac18
\right).
}
$$

The isolated value

$$
-\frac18
$$

for the directed $DA$ row comes from applying a global odd-$D$ sign or the untagged four-dimensional trace before performing the occurrence-resolved Schwinger pairing. The corrected first line is

$$
\boxed{
\texttt{selected\_square}
=
(-4,-4,-4,-4)
}
$$

on the four nonzero endpoint occurrences, which reverses the directed isolated sign:

$$
\boxed{
c_{DA}^{\rm orbit}=+\frac18.
}
$$
