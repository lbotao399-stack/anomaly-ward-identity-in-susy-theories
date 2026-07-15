# AB/BA G3 factor-two first-error audit

## 1. Original measure

$$
[\theta^2\bar\theta^2]_D=1,\qquad
\theta^2=-2\theta^+\theta^-,\qquad
\bar\theta^2=+2\bar\theta^{\dot+}\bar\theta^{\dot-}.
$$

Therefore the canonical monomial maps have magnitudes

$$
\left|\int d^4\theta\right|=\frac14,\qquad
\left|\int d^2\bar\theta\right|=\frac12.
$$

The direct sparse replay in the original measure gives

$$
T_A^{\rm raw}=32768(1-z),\qquad
T_B^{\rm raw}=32768z.
$$

Both matter propagator scalars remain outside the D-word:

$$
\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)=\frac{\hbar^2}{256}.
$$

No full/full endpoint conversion is used.  Direct canonical extraction gives

$$
32768\left(\frac14\right)\left(\frac12\right)=4096.
$$

## 2. Source and action factors

$$
\frac1{2!}(O_{u\phi}+O_{\phi u})=1,
$$

$$
\frac1{2!}(M_rH_-+H_-M_r)=1,
$$

$$
\frac1{3!}\sum_{\sigma\in S_3}1=1,
$$

$$
N_{\rm Wick}^{(1,r)}=1.
$$

The two product-rule marks have coefficients

$$
c_A=1,\qquad c_B=1,
$$

and original-measure moments

$$
w_A=\frac23,\qquad w_B=\frac13,\qquad w_A+w_B=1.
$$

Thus no common factor $1/2$ occurs.

## 3. BB internal calibration

The two per-raw conversion factors agree before color:

$$
K_{AB}=K_{BB}=-\frac{\sqrt2}{2048}.
$$

For the ordered BB component,

$$
R_{BB}^{\rm direct}=4096\left(\frac23-\frac13\right)
=\frac{4096}{3},
$$

$$
R_{BB}^{\rm transported}=2048\left(\frac23-\frac13\right)
=\frac{2048}{3},
$$

$$
R_{BB}^{\rm ordered}=2048.
$$

For AB,

$$
R_{AB}^{\rm ordered}=4096
\left(\frac23+\frac13\right)=4096.
$$

Hence

$$
\frac{R_{AB}^{\rm ordered}}{R_{BB}^{\rm ordered}}=2.
$$

The first factor-two difference is the channel-specific D-algebra occurrence
orbit, after all primitive normalizations.  The original measure and the
outer source marks do not generate a factor $1/2$.
