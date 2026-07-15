# AB/BA G3 absolute normalization and first difference

Status: `PASS_G3_COLOR_PLUS_I__RAW_32768_TO_4096__FIRST_SCALE_ONE_ERROR_IS_DOUBLE_TRANSVERSE_HALF__G1_HAS_NO_ADDITIONAL_HALF`.

## 1. SU(2) color

Use

$$
T_a=\frac{\sigma_a}{2},\qquad
\kappa_{ab}=\frac12\delta_{ab},\qquad
c_{ab}{}^c=\varepsilon_{abc},\qquad
c_{abc}=\frac12\varepsilon_{abc}.
$$

The literal shorthand without propagator metrics is

$$
(T_A)^D{}_Xc_{BXE}
=\frac{i}{2}\sum_X\varepsilon_{AXD}\varepsilon_{BXE}
=\frac{i}{4}\mathbb F^{AB}{}_{DE}.
$$

It is not the graph color.  The matter vertex is lower in the external
antichiral slot,

$$
(T_U)_{DX}:=\kappa_{DR}(T_U)^R{}_X=ic_{UXD}.
$$

The three propagators supply three inverse metrics.  Therefore

$$
\begin{aligned}
\mathcal C^{AB}{}_{DE}
&=\kappa^{AU}\kappa^{BP}\kappa^{XY}
(T_U)_{DX}c_{PYE}\\
&=i\kappa^{AU}\kappa^{BP}\kappa^{XY}
c_{UXD}c_{PYE}\\
&=i\mathbb F^{AB}{}_{DE}.
\end{aligned}
$$

For $(A,B,D,E)=(0,1,1,0)$,

$$
\mathbb F^{01}{}_{10}=-2,\qquad
(T_0)^1{}_Xc_{1X0}=-\frac i2,\qquad
\mathcal C^{01}{}_{10}=-2i.
$$

Thus the complete color is exactly $+i\mathbb F$ and contains no $1/2$.

## 2. Old normalized trace versus raw trace

The retained Berezin mask is

$$
m=(15\ll4M)\,|\,(12\ll4H)=3312.
$$

At every affine sample,

$$
T^{\rm raw}_{A,B}=32768T^{\rm old}_{A,B}.
$$

With $W=p_+\wedge q_+=-i$,

$$
T_A^{\rm old}=-2i(1-z),\qquad
T_B^{\rm old}=-2iz,
$$

$$
c_A^{\rm old}=\frac{T_A^{\rm old}}{2W}=1-z,\qquad
c_B^{\rm old}=\frac{T_B^{\rm old}}{2W}=z,
$$

whereas

$$
c_A^{\rm raw}=32768(1-z),\qquad
c_B^{\rm raw}=32768z.
$$

The old function divides by $32768$ before returning.  This is the first
loss of absolute normalization, not itself a false equality.

## 3. Berezin and DRED restoration

For the canonical monomials,

$$
\mathcal B_M=-\frac14,\qquad
\mathcal B_H=+\frac12,\qquad
|\mathcal B_M\mathcal B_H|=\frac18.
$$

Hence the absolute metric coefficient is

$$
c=32768\left(\frac18\right)=4096.
$$

Since the two-axis transverse trace is $T_\perp=2cW$,

$$
\mathcal R_{\rm DRED}
=-\frac12T_\perp
=-\frac12(2cW)
=-cW
=-4096W.
$$

The scale-one completion instead uses

$$
-\frac12cW=-2048W,
$$

after $c=T_\perp/(2W)$ has already consumed the trace factor $2$.  This is
the first algebraic factor-two error.  The old G3 replay itself never derives
the scale-one output; its quotient routine imports it from the Project engine.

## 4. Primitive and finite chain

$$
C_I=-\frac{g^2}{4\sqrt2},\qquad
C_M=\frac{\sqrt2g}{\hbar},\qquad
C_{H,32}=-\frac{\sqrt2g}{\hbar},\qquad
C_{H,33}=+\frac{\sqrt2g}{\hbar},
$$

$$
C_{\rm prop}=(-\hbar)
\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)
=-\frac{\hbar^3}{256}.
$$

$$
\left[\frac12(2)_{\rm source\ cycle}\right]
\left[\frac1{2!}(2)_{MH\ orders}\right]
\left[\frac1{3!}(6)_{H_-\ Hessian}\right]
(1)_{\rm Wick}=1.
$$

Therefore

$$
C_{32}^{\rm preD}=-\frac{\sqrt2\hbar g^4}{1024},\qquad
C_{33}^{\rm preD}=+\frac{\sqrt2\hbar g^4}{1024}.
$$

Using

$$
\widetilde\phi_2\widetilde\phi_3=g^{-2}C_2C_3,\qquad
\mathcal C_{\rm color}=+i\mathbb F,qquad
I_{\mu^2}=\frac1{32\pi^2},\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},
$$

one obtains

$$
\frac{C_{32}^{\rm preD}(-4096)g^{-2}iI_{\mu^2}}{\lambda_1}
=+2i\sqrt2,
$$

$$
\frac{C_{33}^{\rm preD}(-4096)g^{-2}iI_{\mu^2}}{\lambda_1}
=-2i\sqrt2.
$$

The ordered spinor map gives

$$
G_{32}:\ C_2>C_3=-2i\sqrt2,\qquad
G_{33}:\ C_3>C_2=+2i\sqrt2.
$$

## 5. G1 half check

The sparse engine gives

$$
D_-D_+\theta^2=-2,\qquad
D^2\theta^2=-4,\qquad
D^2=2D_-D_+.
$$

Thus the source replay already uses $D_-D_+=D^2/2$.  No further factor
$1/2$ may be applied.

Its endpoint probes obey

$$
D_+\phi_{\rm probe}=\eta_B,\qquad
D^2\bar D_{\dot a}u_{\rm probe}=\eta_D,
$$

and the physical map is

$$
D_+\phi_1=\frac1gB_1,\qquad
D^2\bar D_{\dot a}u=-\frac{4\sqrt2}{g}D_{\dot a}.
$$

There is no component-map half.  The selected marked rows remain

$$
G_{1,A}=\frac23,\qquad G_{1,B}=-\frac23.
$$
