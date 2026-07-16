# AB/BA complete G1+G2+G3 target-blind one-loop family

## 1. Definitions

$$
d=4-2\epsilon,\qquad
\mu_\ell^2=\bar\ell^2-\ell_d^2,
\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2}.
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

## 2. G1

$$
A:\ \left(\frac43,\frac23\right),\qquad
B:\ \left(\frac23,\frac43\right).
$$

$$
G_1^{\rm generic}=2(p_L+q_R).
$$

$$
p_L+q_R=0\quad\Longrightarrow\quad G_1^{\rm physical}=0.
$$

For AB the ordered word is $D>B_1$; for BA it is $B_1>D$.  The separately
drawn source-resolvent bubbles are not added: they are presentations of the
same induced derivative-of-action contact.

## 3. G2

$$
C_I=-\frac{g^2}{4\sqrt2},\qquad
C_M=\frac{\sqrt2g}{\hbar},\qquad
C_{\rm prop}=-\frac{\hbar^3}{256}.
$$

$$
\frac1{2!}\times2_{\rm labeled\ action\ assignments}=1.
$$

$$
C_{G_2}^{\rm preD}=\frac{\sqrt2\hbar g^4}{1024}.
$$

$$
\Gamma_{G_2}^{D\text{-first}}
=\frac{\lambda_1}{3}D(q_R-4p_L)B_1,
$$

$$
\Gamma_{G_2}^{\rm ordered}
=\frac{\lambda_1}{3}B_1(4p_L-q_R)D.
$$

$$
c_{G_2}=\frac43-\frac13=1.
$$

The output is $B_1>D$ for AB and $D>B_1$ for BA.

## 4. G3 labeled factorial census

$$
\frac1{2!}(O_{u\phi}u\phi+O_{\phi u}\phi u)=1,
$$

$$
\frac1{2!}(M_rH_-+H_-M_r)=1,
$$

$$
\frac1{3!}\sum_{\sigma\in S_3}
\operatorname{sgn}_{\rm flavor}(\sigma)
\operatorname{sgn}_{\rm color}(\sigma)
=\frac16\sum_{\sigma\in S_3}1=1.
$$

For G32 the internal flavors are $(1,2)$; for G33 they are $(1,3)$.
They are distinct, so the fixed-flavor Wick pairing count is one.

The raw $32768$ word is one labeled route.  It contains neither the BA
reflection nor a second Wick matching.  Its exact original-measure conversion is

$$
32768\left(\frac14\right)_{d^4\theta_M}
\left(\frac12\right)_{d^2\bar\theta_H}
\left(-\frac12\right)_{\mu^2\text{ extraction}}
(2)_{\rm trace/metric}
=-4096.
$$

The factor $2_{\rm trace/metric}$ is algebraic and is canceled by the
$-1/2$ rank extraction; it is not a graph multiplicity.

$$
C_{32}^{\rm preD}=-\frac{\sqrt2\hbar g^4}{1024},\qquad
C_{33}^{\rm preD}=+\frac{\sqrt2\hbar g^4}{1024}.
$$

$$
c_{32}^{\rm unit}=+2i\sqrt2,\qquad
c_{33}^{\rm unit}=-2i\sqrt2.
$$

$$
w_A=\frac23,\qquad w_B=\frac13,qquad w_A+w_B=1.
$$

Thus G32 and G33 remain $+2i\sqrt2$ and $-2i\sqrt2$ respectively.

## 5. G3 full Schwinger--Dyson occurrence orbit

The current occurrences are not used as induced cuts:

$$
G3\text{-}A\text{-}JE:
\frac{+512S_AW_{12}}{D_1D_2},\qquad
G3\text{-}A\text{-}JX:
\frac{-512S_AW_{12}}{D_1D_2},
$$

$$
G3\text{-}B\text{-}PE:
\frac{-128S_BW_{p0}}{D_0D_1},\qquad
G3\text{-}B\text{-}PX:
\frac{+128S_BW_{p0}}{D_0D_1}.
$$

Therefore

$$
I_{JE}+I_{JX}=0,\qquad I_{PE}+I_{PX}=0.
$$

None of these four words contains a four-dimensional inverse square; each
DRED defect is zero.

Set

$$
\det_4(r_e)=-(D_e+\mu_\ell^2),\qquad
P_D=D_0D_1D_2.
$$

The three independent parent--cut pairs are

$$
\frac{4096\det_4(r_0)W_{12}}{P_D}
+\frac{4096W_{12}}{D_1D_2}
=-\frac{4096\mu_\ell^2W_{12}}{P_D},
$$

$$
-\frac{4096\det_4(r_1)W_{P0}}{P_D}
-\frac{4096W_{P0}}{D_0D_2}
=+\frac{4096\mu_\ell^2W_{P0}}{P_D},
$$

$$
\frac{4096\det_4(r_2)W_{p0}}{P_D}
+\frac{4096W_{p0}}{D_0D_1}
=-\frac{4096\mu_\ell^2W_{p0}}{P_D}.
$$

The transported $r_1$ square is an independent edge branch inside the same
outer-$A$ occurrence; it is not an $r_0$ contact and not a new outer mark.

$$
-W_{12}+W_{P0}-W_{p0}=-p_+\wedge q_+.
$$

Hence

$$
\mathcal R_{G_3}^{\rm full\ SD}
=-\frac{4096\mu_\ell^2(p_+\wedge q_+)}{D_0D_1D_2}.
$$

The full descendant orbit supplies no factor $1/2$.

## 6. Target-blind AB/BA vectors

Use the ordered basis

$$
(B_1>D,\ D>B_1,\ C_3>C_2,\ C_2>C_3).
$$

$$
\Gamma_{AB}^{\rm full\ SD}/\lambda_1
=(1,0,-2*sqrt(2)i,2*sqrt(2)i).
$$

$$
\Gamma_{BA}^{\rm full\ SD}/\lambda_1
=(0,1,2*sqrt(2)i,-2*sqrt(2)i).
$$

## 7. Check-only comparison

The direct payload is sealed before reading the HT artifact.  The comparison
status is `MISMATCH`.  No HT coefficient enters Sections 1--6.
