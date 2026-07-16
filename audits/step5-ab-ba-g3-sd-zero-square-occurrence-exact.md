# AB/BA G3 Schwinger rows and zero-square occurrence audit

Status: `PASS_G3_THREE_SD_CUTS_AND_ZERO_SQUARE_I1_I2_FAMILIES_EXHAUSTED__NO_NET_CC_EXTERNAL_PORT_CORRECTION__PRECOHOMOLOGY_MAGNITUDE_TWO_RETAINED`.

## 1. Definitions

$$
I_1:=(\nabla_-A)B_1,
\qquad
I_2:=A(\nabla_-B_1),
$$

$$
D_e:=r_{e,d}^2,
\qquad
\bar r_e^2=D_e+\mu_\ell^2,
\qquad
P_3:=D_0D_1D_2.
$$

$$
W_0:=W_{12},
\qquad
W_1:=W_{(p+q)0},
\qquad
W_2:=W_{p0}=W_{01}.
$$

## 2. Explicit parent words

$$
N_A^{\rm raw}
=-1024\det_4(r_0)W_0+1024\det_4(r_1)W_1,
$$

$$
N_B^{\rm raw}=-1024\det_4(r_2)W_2.
$$

The cut cores are

$$
C_0^{\rm core}=+512W_0,
\qquad
C_1^{\rm core}=-128W_1,
\qquad
C_2^{\rm core}=-128W_2.
$$

Their operator multipliers are

$$
m_0=8,
$$

$$
m_1=\left(-\frac12\right)(16)(-4)=32,
$$

$$
m_2=\left(\frac12\right)(16)(-4)=-32.
$$

Thus

$$
K_0=+4096W_0,
\qquad
K_1=-4096W_1,
\qquad
K_2=+4096W_2.
$$

For $K_2$, the two ordered flavor/color Hessian summands obey

$$
\varepsilon_{123}(C_2\times C_3)
+\varepsilon_{132}(C_3\times C_2)
=(C_2\times C_3)+(-1)(-C_2\times C_3)
=2(C_2\times C_3).
$$

Hence

$$
m_2^{(1)}=m_2^{(2)}=\frac{-32}{2}=-16,
$$

$$
(-16)(-128W_2)+(-16)(-128W_2)
=2048W_2+2048W_2
=4096W_2.
$$

They are two algebraic summands of one $e_2$ cut.

## 3. Three full-$d$ Schwinger rows

$$
-\frac{4096(D_0+\mu_\ell^2)W_0}{P_3}
+\frac{4096W_0}{D_1D_2}
=-\frac{4096\mu_\ell^2W_0}{P_3},
$$

$$
+\frac{4096(D_1+\mu_\ell^2)W_1}{P_3}
-\frac{4096W_1}{D_0D_2}
=+\frac{4096\mu_\ell^2W_1}{P_3},
$$

$$
-\frac{4096(D_2+\mu_\ell^2)W_2}{P_3}
+\frac{4096W_2}{D_0D_1}
=-\frac{4096\mu_\ell^2W_2}{P_3}.
$$

At $\mu_\ell^2=0$, each displayed row equals zero.

The exact routed identity is

$$
-W_0+W_1-W_2=-p_+\wedge q_+,
$$

so

$$
\mathcal R_{G_3}
=-\frac{4096\mu_\ell^2(p_+\wedge q_+)}{P_3}.
$$

## 4. $I_1/I_2$ zero-square descendants

Write

$$
\mathscr E_V=\mathscr E_V^{\rm lin}-2i(\Phi_s\times C_s).
$$

Then

$$
-\nabla_+\mathscr E_V-2i(B_s\times C_s)
=-\nabla_+\mathscr E_V^{\rm lin}
+2i(B_s\times C_s)-2i(B_s\times C_s)
=-\nabla_+\mathscr E_V^{\rm lin}.
$$

The two separately tagged $I_1$ rows are

$$
JE=+\frac{512W_0}{D_1D_2},
\qquad
JX=-\frac{512W_0}{D_1D_2},
\qquad
JE+JX=0.
$$

Likewise

$$
\mathscr E_{\widetilde1}
=-\frac14\nabla^2\Phi_1
-\frac1{\sqrt2}\varepsilon_{1st}(C_s\times C_t),
$$

$$
-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1
+\sqrt2\varepsilon_{1st}(C_s\times C_t)
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1.
$$

The two separately tagged $I_2$ rows are

$$
PE=-\frac{128W_2}{D_0D_1},
\qquad
PX=+\frac{128W_2}{D_0D_1},
\qquad
PE+PX=0.
$$

None of $JE,JX,PE,PX$ contains a parent $\bar r_e^2$.  Therefore

$$
\partial_{\mu_\ell^2}JE
=\partial_{\mu_\ell^2}JX
=\partial_{\mu_\ell^2}PE
=\partial_{\mu_\ell^2}PX
=0.
$$

$K_0$ and $JE$ have the same routed core but different provenance tags;
$K_2$ and $PE$ also have different provenance tags.  They are not aliased.

Hence the net $I_1/I_2$ correction to the $C_2C_3$ external ports is

$$
\boxed{\Delta_{I_1/I_2}^{C_2C_3}=0.}
$$

The occurrences themselves are retained.

## 5. Contact-family exhaustion

$$
e_0:\ I_1\times H_-,
\qquad
e_1:\ \text{transported }M-H_-\text{ bridge},
\qquad
e_2:\ I_2\times M.
$$

$$
\{e_0,e_1,e_2\}_{\rm cut}
=\{e_0,e_1,e_2\}_{\rm triangle}.
$$

The ten top-level local occurrences are

$$
P_0,K_0,P_1,K_1,P_2,K_2,JE,JX,PE,PX.
$$

The bare source is

$$
I_0^{AB}=C_{AB}u^A\phi_1^B.
$$

In the field basis $(u,\phi_1,\widetilde\phi_2,\widetilde\phi_3)$,

$$
I_0''=
\begin{pmatrix}
0&C_{AB}&0&0\\
C_{AB}&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

Thus no additional bare-source $(\widetilde\phi_2,\widetilde\phi_3)$ Hessian
exists.  The descended $I_2$ rows are exactly the retained $PE/PX$ pair above.

## 6. Simplex and coefficients

For

$$
r_0=L+(y+z)p+zq,
$$

the loop-even external words are

$$
W_0=(1-y-z)(p_+\wedge q_+),
$$

$$
W_1=-y(p_+\wedge q_+),
$$

$$
W_2=z(p_+\wedge q_+).
$$

Therefore

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,(1-y-z)=\frac13,
$$

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,(-y)=-\frac13,
$$

$$
2\int_{0}^{1}dy\int_{0}^{1-y}dz\,z=\frac13,
$$

and

$$
-4096\left(\frac13\right)
+4096\left(-\frac13\right)
-4096\left(\frac13\right)
=-4096.
$$

The resolvent and direct-Wick cycle counts are two representations of the
same two correlated rows:

$$
\left(\frac12\right)_{\rm resolvent}
(2)_{\rm correlated\ cycles}=1,
$$

$$
\left(\frac1{2!}\right)_{\rm action}
(2)_{MH_-,H_-M}
(1)_{\rm unique\ Wick}=1.
$$

They are not multiplied as independent raw factors.  Including the fixed
$H_-$ Hessian coefficient gives

$$
(1)_{\rm cycle}
\left[\frac1{3!}(6)_{H_-\ {\rm Hessian}}\right]
=1.
$$

Before total-divergence or cohomology quotient,

$$
G_{32}^{\rm raw}=+2i\sqrt2\lambda_1,
\qquad
G_{33}^{\rm raw}=-2i\sqrt2\lambda_1,
$$

$$
G_{32}^{\rm typed}=-2i\sqrt2\lambda_1,
\qquad
G_{33}^{\rm typed}=+2i\sqrt2\lambda_1.
$$

In the basis $(C_2>C_3,C_3>C_2)$,

$$
v_{AB}=(-2i\sqrt2,+2i\sqrt2),
$$

$$
v_{BA}=(+2i\sqrt2,-2i\sqrt2).
$$

## 7. Quotient layers

| layer | operation | result |
|---|---|---|
| local jet | retain all ten provenance-tagged occurrences | $JE+JX=PE+PX=0$, magnitude $2\sqrt2$ |
| EOM/SD | pair $P_e$ only with $K_e$ | full-$d$ zero edgewise; DRED remainder retained |
| total divergence | not applied | no identification |
| cohomology/HT | not applied | no target coefficient used |

$$
N_{\rm pass}=73,
\qquad
N_{\rm fail}=0.
$$
