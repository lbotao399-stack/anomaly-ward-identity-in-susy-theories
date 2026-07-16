# AB/BA G1 Gate10 longitudinal first-equality exact audit

Status: `GATE10_FIRST_EQUALITY_REJECTED__EXACT_LA_ALREADY_INCLUDED__NO_R1_SQUARE_DIVISOR__METRIC_PROJECTION_IS_Q_OVER_2_NOT_MINUS_P_PLUS_Q`.

## 1. Definitions

$$
r_0=\ell,\qquad r_1=\ell-p,\qquad r_2=\ell-p-q,
$$

$$
L_A=-\frac12D_+\bar D^2D^2,
\qquad L_A=L_{A,+}-L_{A,-}.
$$

Gate10 claims

$$
L_A\stackrel{?}{=}-\bar r_1^2(r_0-r_2)^{\dot a}
=-\bar r_1^2(p+q)^{\dot a}.
$$

## 2. First equality

The complete 24-word exact exterior-algebra replay gives, in both generic
external frames,

$$
[L_A^{\dot0}]_3=-4096(\ell_0-i\ell_1)\bar\ell^2,
$$

$$
[L_A^{\dot1}]_3=+4096(\ell_2+i\ell_3)\bar\ell^2.
$$

Therefore

$$
\deg_\ell L_A=3,
\qquad
\deg_\ell\left[-\bar r_1^2(p+q)^{\dot a}\right]=2,
$$

$$
\boxed{L_A\ne-\bar r_1^2(p+q)^{\dot a}.}
$$

Equivalently,

$$
\Delta_{\ell_0}^3L_A^{\dot0}=-24576,
\qquad
\Delta_{\ell_1}^3L_A^{\dot0}=24576i,
$$

$$
\Delta_{\ell_2}^3L_A^{\dot1}=24576,
\qquad
\Delta_{\ell_3}^3L_A^{\dot1}=24576i,
$$

while all third differences of the Gate10 polynomial vanish.

## 3. Two generic full-polynomial frames

### generic_1

$$
p=(1, 2, -1, 1),\qquad q=(-2, 1, 3, 0),\qquad P=(-1, 3, 2, 1).
$$

$$
L^{\dot 0}(\ell)=-4096*(ell0**3 - i*ell0**2*ell1 + ell0**2*(2 + 5*i) + ell0*ell1**2 + ell0*ell1*(4 - 2*i) + ell0*ell2**2 + ell0*ell2*(-1 - i) + ell0*ell3**2 + ell0*ell3*(1 - i) + ell0*(-11 + 2*i) - i*ell1**3 + i*ell1**2 - i*ell1*ell2**2 + ell1*ell2*(-1 + i) - i*ell1*ell3**2 + ell1*ell3*(-1 - i) + ell1*(2 + 11*i) + ell2**2*(1 + 3*i) + ell2*(-1 - 13*i) + ell3**2*(1 + 3*i) + ell3*(13 - i)).
$$

$$
[L^{\dot 0}]_3=-4096*(ell0 - i*ell1)*(ell0**2 + ell1**2 + ell2**2 + ell3**2).
$$

Nonzero rows: `12`; rows divisible by $\bar r_1^2$: `0`; aggregate divisible: `False`.

$$
\mathscr M[L^{\dot 0}]=-1 - i/2,\qquad -S(P)^{\dot 0}=1 + 3*i.
$$

$$
L^{\dot 1}(\ell)=4096*(ell0**2*ell2 + i*ell0**2*ell3 + ell0**2*(-2 - i) + ell0*ell2*(1 + 2*i) + ell0*ell3*(-2 + i) + ell0*(-5 - 5*i) + ell1**2*ell2 + i*ell1**2*ell3 + ell1**2*(-2 - i) + ell1*ell2*(2 - i) + ell1*ell3*(1 + 2*i) + ell1*(-5 + 5*i) + ell2**3 + i*ell2**2*ell3 + ell2**2*(-3 - 2*i) + ell2*ell3**2 + ell2*ell3*(2 - 2*i) + ell2*(-4 - 2*i) + i*ell3**3 - ell3**2 + ell3*(2 - 4*i)).
$$

$$
[L^{\dot 1}]_3=4096*(ell2 + i*ell3)*(ell0**2 + ell1**2 + ell2**2 + ell3**2).
$$

Nonzero rows: `12`; rows divisible by $\bar r_1^2$: `0`; aggregate divisible: `False`.

$$
\mathscr M[L^{\dot 1}]=-3/2,\qquad -S(P)^{\dot 1}=2 + i.
$$


### generic_2

$$
p=(0, 1, 1, 0),\qquad q=(1, 0, 0, -1),\qquad P=(1, 1, 1, -1).
$$

$$
L^{\dot 0}(\ell)=-4096*(ell0**3 - i*ell0**2*ell1 + ell0**2*(-1 + 2*i) + ell0*ell1**2 + 2*ell0*ell1 + ell0*ell2**2 + ell0*ell2 + ell0*ell3**2 + i*ell0*ell3 + ell0*(-2 - 2*i) - i*ell1**3 - ell1**2 - i*ell1*ell2**2 - i*ell1*ell2 - i*ell1*ell3**2 + ell1*ell3 + ell1*(-2 + 2*i) + ell2**2*(-1 + i) + 2*i*ell2 + ell3**2*(-1 + i) - 2*ell3).
$$

$$
[L^{\dot 0}]_3=-4096*(ell0 - i*ell1)*(ell0**2 + ell1**2 + ell2**2 + ell3**2).
$$

Nonzero rows: `12`; rows divisible by $\bar r_1^2$: `0`; aggregate divisible: `False`.

$$
\mathscr M[L^{\dot 0}]=1/2,\qquad -S(P)^{\dot 0}=-1 + i.
$$

$$
L^{\dot 1}(\ell)=4096*(ell0**2*ell2 + i*ell0**2*ell3 + ell0**2*(-1 + i) + i*ell0*ell2 - ell0*ell3 - 2*i*ell0 + ell1**2*ell2 + i*ell1**2*ell3 + ell1**2*(-1 + i) + ell1*ell2 + i*ell1*ell3 - 2*ell1 + ell2**3 + i*ell2**2*ell3 + i*ell2**2 + ell2*ell3**2 + 2*i*ell2*ell3 + ell2*(-2 + 2*i) + i*ell3**3 + ell3**2*(-2 + i) + ell3*(-2 - 2*i)).
$$

$$
[L^{\dot 1}]_3=4096*(ell2 + i*ell3)*(ell0**2 + ell1**2 + ell2**2 + ell3**2).
$$

Nonzero rows: `12`; rows divisible by $\bar r_1^2$: `0`; aggregate divisible: `False`.

$$
\mathscr M[L^{\dot 1}]=i/2,\qquad -S(P)^{\dot 1}=1 - i.
$$


The exact centered metric diagnostic is

$$
\mathscr M[L]^{\dot a}
:=\frac{2}{4096}\int_{y,z\ge0\atop y+z\le1}dy\,dz\,
\frac18\Delta_\ell L^{\dot a}
\left(yp+z(p+q)\right)
=S\!\left(\frac q2\right)^{\dot a},
$$

not $-S(p+q)^{\dot a}$.  This metric projection is not an exact
$\bar r_1^2$ divisor: every frame has twelve nonzero longitudinal rows per
dotted component, zero of which is divisible by $\bar r_1^2$, and their sum
is also not divisible.

## 4. Matching source-resolvent cut

The complete symbolic $I_{[1]}S_{m3}$ replay contains the $A_2B_{11}$,
$A_1B_{12}$, outer-connection, and vector-frame bridge terms.  It gives

$$
K_{L,R_2}^{AB}=0,
$$

with BA obtained by the exact graded mirror
$-B_1(D_-A)=+(D_-A)B_1$.  Thus the claimed

$$
K_L=+D_0D_2(r_0-r_2)
$$

is not a raw Hessian result.

## 5. Adjudication

$$
\boxed{
N_L\text{ is not a new graph, no exact hidden }\bar r_1^2\text{ factor exists,}
}
$$

$$
\boxed{
(2,2)\longrightarrow(1,1)\text{ is rejected at the first parent equality.}
}
$$

The earlier formal contact $C_L=-L_A$ is not thereby proved as a raw
$R_2$ Hessian: the complete $I_{[1]}S_{m3}$ word is zero.  Hence the G1 raw
contact closure remains open, while the Gate10 $-(p+q)$ correction is closed.
