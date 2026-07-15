# AB/BA G3 Gate-7 normalization first-error audit

Status: `GATE7_REJECTED__KINETIC_CUTS_CHI2_FOURIER_SIGN_FIXED__G2_DEFICIT_LOCALIZED`.

## 1. First error

$$
\mathscr E_{\widetilde1}
=-\frac14\nabla^2\Phi_1
-\frac1{\sqrt2}\varepsilon_{1st}(C_s\times C_t),
$$

$$
-2\mathscr E_{\widetilde1}
-\sqrt2\varepsilon_{1st}(C_s\times C_t)
=\frac12\nabla^2\Phi_1.
$$

Hence the nonlinear occurrences are

$$
PE=-128W_{p0},\qquad PX=+128W_{p0},\qquad PE+PX=0.
$$

Gate 7 first uses $c_{IJK}=-c_{IKJ}$ to canonicalize the PX color slots and
then, in Section 4.2, reverses the dotted contraction again,
$W_{01}\mapsto W_{10}$.  This is a second unsupported exchange:

$$
(-128)(-2W_{p0})+(+128)(+2W_{p0})=512W_{p0}\ne0.
$$

Thus $PE/PX$ are zero-square nonlinear rows; they are not the kinetic cut
$K_2$.

## 2. Same-unit kinetic cuts

$$
m_{K_0}=8,
$$

$$
m_{K_1}=\left(-\frac12\right)(16)(-4)=+32,
$$

$$
m_{K_2}=\left(+\frac12\right)(16)(-4)=-32.
$$

With the directly replayed cores,

$$
K_0=8(512W_0)=+4096W_0,
$$

$$
K_1=32(-128W_1)=-4096W_1,
$$

$$
K_2=(-32)(-128W_2)=+4096W_2.
$$

The parent words in the same endpoint normalization are

$$
P_0=-4096(D_0+\mu_\ell^2)W_0,
$$

$$
P_1=+4096(D_1+\mu_\ell^2)W_1,
$$

$$
P_2=-4096(D_2+\mu_\ell^2)W_2.
$$

Therefore

$$
\frac{P_0}{D_0D_1D_2}+\frac{K_0}{D_1D_2}
=-4096\frac{\mu_\ell^2W_0}{D_0D_1D_2},
$$

$$
\frac{P_1}{D_0D_1D_2}+\frac{K_1}{D_0D_2}
=+4096\frac{\mu_\ell^2W_1}{D_0D_1D_2},
$$

$$
\frac{P_2}{D_0D_1D_2}+\frac{K_2}{D_0D_1}
=-4096\frac{\mu_\ell^2W_2}{D_0D_1D_2}.
$$

At $\mu_\ell^2=0$, all three equations are exactly zero.

## 3. Trace and Fourier signs

Let the two-axis transverse trace be

$$
T_\perp=2cW.
$$

The original measure gives

$$
c=32768\left(\frac14\right)\left(\frac12\right)=4096.
$$

Hence

$$
-\frac12T_\perp=-cW=-4096W.
$$

Gate 7 instead used

$$
-\frac12cW=-2048W,
$$

which applies the rank projector a second time after dividing the trace by
$2W$.

For the locked phase $e^{ipx}$,

$$
(ip)_+\wedge(iq)_+=-(p_+\wedge q_+).
$$

Therefore

$$
G_{3,2}^{\mathrm{raw}}=+2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\mathrm{raw}}=-2i\sqrt2\lambda_1,
$$

$$
\boxed{
G_{3,2}^{\mathrm{typed}}=-2i\sqrt2\lambda_1,
\qquad
G_{3,3}^{\mathrm{typed}}=+2i\sqrt2\lambda_1.}
$$

The same trace rule leaves

$$
G_1=(2,2)_{\mathrm{pair,EOM}},
\qquad
(c_p,c_q)_{G_2}=\left(\frac43,-\frac13\right).
$$

The actual G2 graph has $D(p)$ and $B_1(q)$, hence

$$
G_2=\left(-\frac13,\frac43\right)_{\mathrm{pair,EOM}}.
$$

In the basis

$$
(D>B_1,B_1>D,C_2>C_3,C_3>C_2),
$$

the corrected vector and residual are

$$
v=\left(2,-\frac13,-2i\sqrt2,+2i\sqrt2\right),
$$

$$
Qv=\left(\frac73,0,0\right).
$$

Thus G1 and G3 have common scale $2$; the only remaining coefficient defect
is the routed G2 pair deficit $7/3$.
