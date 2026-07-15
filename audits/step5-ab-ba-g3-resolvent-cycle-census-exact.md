# AB/BA G3 resolvent cycle census

Status: `PASS_G3_RESOLVENT_TWO_NONZERO_CYCLES_CORRELATED__OUTER_HALF_CANCELLED_ONCE__CURRENT_PRED_NO_DOUBLE_COUNT`.

## 1. Field blocks

For fixed $s=2$ or $s=3$, use

$$
\mathcal B=(u,\phi_1,\widetilde\phi_1,\phi_s,\widetilde\phi_s).
$$

The nonzero propagator blocks are

$$
G_{uu}=G_u,
$$

$$
G_{\phi_1\widetilde\phi_1}
=G_{\widetilde\phi_1\phi_1}=G_1,
$$

$$
G_{\phi_s\widetilde\phi_s}
=G_{\widetilde\phi_s\phi_s}=G_s.
$$

The oriented Hessian blocks are

$$
I_0'':quad I_{u1},I_{1u},
$$

$$
V_M'':quad M_{us},M_{su},
$$

$$
V_H'':quad H_{1s},H_{s1}.
$$

All five quantum superfields in this block are even, so

$$
\operatorname{STr}_{\mathcal B}=\operatorname{Tr}_{\mathcal B}.
$$

## 2. Complete oriented census

Expand

$$
\Gamma_{I_0}^{(1)}
=-\frac{\hbar}{2}
\operatorname{STr}
\left[G(V_M+V_H)G(V_M+V_H)GI_0''\right].
$$

There are

$$
2_{\rm action\ order}
\cdot2_{I_0''}
\cdot2_{V_M''}
\cdot2_{V_H''}
=16
$$

oriented block candidates.  Exactly two are nonzero:

$$
\begin{aligned}
\mathcal C_u
&=\operatorname{Tr}
\left[GV_MGV_HGI_{1u}\right]\\
&=G_uM_{us}G_sH_{s1}G_1I_{1u},
\end{aligned}
$$

$$
\begin{aligned}
\mathcal C_{\phi_1}
&=\operatorname{Tr}
\left[GV_HGV_MGI_{u1}\right]\\
&=G_1H_{1s}G_sM_{su}G_uI_{u1}.
\end{aligned}
$$

Every other oriented block product is zero.

For even ordered Hessians,

$$
I_{u1}=I_{1u}=I_0,
\qquad
M_{us}=M_{su}=V_M,
\qquad
H_{1s}=H_{s1}=V_H.
$$

Hence

$$
\mathcal C_u
=\mathcal C_{\phi_1}
=G_uG_1G_sI_0V_MV_H
=:\mathcal C.
$$

The four resolvent words are

$$
\operatorname{STr}[GV_MGV_MGI_0'']=0,
$$

$$
\operatorname{STr}[GV_MGV_HGI_0'']=\mathcal C,
$$

$$
\operatorname{STr}[GV_HGV_MGI_0'']=\mathcal C,
$$

$$
\operatorname{STr}[GV_HGV_HGI_0'']=0.
$$

Therefore

$$
-\frac{\hbar}{2}(\mathcal C+\mathcal C)
=-\hbar\mathcal C.
$$

## 3. The two labels are correlated

The nonzero map is

$$
I_{1u}\longleftrightarrow (V_M,V_H),
$$

$$
I_{u1}\longleftrightarrow (V_H,V_M).
$$

Fixing the source block fixes the action order, and fixing the action order
fixes the source block.  Thus

$$
N_{\rm nonzero}=2,
\qquad
N_{\rm nonzero}\ne2_{\rm source}\cdot2_{\rm action}=4.
$$

The overall resolvent factor is canceled once:

$$
\boxed{
\left(\frac12\right)_{\rm resolvent}
(2)_{\rm correlated\ closed\ cycles}=1.}
$$

The source reverse block and the action-order swap are two names for the same
two nonzero rows.

## 4. Direct Wick representation

The direct expansion gives

$$
\boxed{
\left(\frac1{2!}\right)_{\rm action}
(2)_{V_MV_H,V_HV_M}
(1)_{\rm species\ Wick}=1.}
$$

This is an alternative representation of the resolvent count.  It is not an
additional multiplier.

With

$$
C_I=-\frac{g^2}{4\sqrt2},
\qquad
V_M=\frac{\sqrt2g}{\hbar},
$$

$$
V_{H,32}=-\frac{\sqrt2g}{\hbar},
\qquad
V_{H,33}=+\frac{\sqrt2g}{\hbar},
$$

$$
G_uG_1G_s
=(-\hbar)\left(\frac{\hbar}{16}\right)^2
=-\frac{\hbar^3}{256},
$$

the current direct-Wick scalars are

$$
C_{G32}^{\rm preD}
=\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\hbar^3}{256}\right)
=-\frac{\sqrt2\hbar g^4}{1024},
$$

$$
C_{G33}^{\rm preD}
=+\frac{\sqrt2\hbar g^4}{1024}.
$$

The resolvent cycle weight gives the same two scalars.  No raw source-Hessian
factor $2$ is multiplied into the current pre-D expression.

An additional factor $2$ would give

$$
2C_{G32}^{\rm preD}
=-\frac{\sqrt2\hbar g^4}{512},
$$

which is not the current pre-D scalar.

$$
N_{\rm pass}=30,
\qquad
N_{\rm fail}=0.
$$
