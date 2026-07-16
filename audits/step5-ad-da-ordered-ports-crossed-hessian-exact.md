# Step 5 AD/DA ordered action ports and crossed Hessian

Status: `PASS_TARGET_BLIND_AD_DA_FULL_CHIRALITY_RAW_CONTACT_AND_LINK__HOLOMORPHIC_TWIST_COEFFICIENTS_MATCH`.

External target used: `false`.

## 1. Momentum routing

$$
r_0=\ell,\qquad r_1=\ell+p_{\rm raw},\qquad
r_2=\ell+p_{\rm raw}+q_{\rm raw}.
$$

$$
r_0-r_1+p_{\rm raw}=0,\qquad
-r_2+r_1+q_{\rm raw}=0.
$$

Generated graph IR fixes

$$
r_0=k,\qquad r_1=k+q_{\rm IR},\qquad
r_2=k+p_{\rm IR}+q_{\rm IR},
$$

therefore

$$
p_{\rm raw}=q_{\rm IR}=k_L,\qquad
q_{\rm raw}=p_{\rm IR}=k_R.
$$

The ordered background action ports are

$$
D^D_{\dot1}(q_{\rm IR})>D^{E\dot2}(p_{\rm IR}).
$$

The maps $$(q,-p-q)$$ and $$(-p-q,q)$$ use the source-insertion
momentum as an output momentum and are rejected.

## 2. Two color Hessians

$$
H_{AD}[u_1,u_2]
=N^A[u_1]D^B[u_2]+N^A[u_2]D^B[u_1],
$$

$$
H_{DA}[u_1,u_2]
=-D^A[u_1]N^B[u_2]-D^A[u_2]N^B[u_1].
$$

The two contractions carry

$$
\mathbb F^{AB}{}_{DE},\qquad \mathbb F^{BA}{}_{DE}.
$$

For the fixed odd component directions,

$$
H_{AD}^{\rm direct}=\frac i4,\qquad
H_{AD}^{\rm crossed}=-\frac i4,
$$

$$
H_{DA}^{\rm direct}=\frac14,\qquad
H_{DA}^{\rm crossed}=-\frac14.
$$

For $SU(2)$,

$$
(A,B;D,E)=(0,1;1,0):\quad
(\mathbb F^{AB}{}_{DE},\mathbb F^{BA}{}_{DE})=(-2,0),
$$

$$
(A,B;D,E)=(0,1;0,1):\quad
(\mathbb F^{AB}{}_{DE},\mathbb F^{BA}{}_{DE})=(0,-2).
$$

## 3. Exact D-algebra numerators

$$
R_1=\frac i{16}\mu_\ell^2
\left(\ell+p_{\rm raw}+\frac12q_{\rm raw}\right)_+,
\qquad
R_2=-\frac i{16}\mu_\ell^2\ell_+.
$$

$$
N_{AD}^{\rm ev}=\mathbb F^{AB}{}_{DE}R_1
+\mathbb F^{BA}{}_{DE}R_2,
$$

$$
N_{DA}^{\rm ev}=\mathbb F^{AB}{}_{DE}R_2
+\mathbb F^{BA}{}_{DE}R_1.
$$

## 4. Same-edge parent and cut

For every occurrence $\omega$ on edge $e$,

$$
\frac{R_\omega r_{e,d}^2}{D_0D_1D_2}
-\frac{R_\omega}{P_{\widehat e}}=0,
$$

$$
\frac{R_\omega\bar r_e^2}{D_0D_1D_2}
-\frac{R_\omega}{P_{\widehat e}}
=\frac{R_\omega\mu_\ell^2}{D_0D_1D_2}.
$$

O05/O06 are partial two-denominator contact members.  They must first be
combined with the same-edge, same-color kinetic/longitudinal/gauge-fixing/link
contacts.  Their affine numerator is not an anomaly-zero certificate.

The following equations are required same-edge constraints only.  Their
second summands are not declared generated contact amplitudes:

$$
\begin{aligned}
AD,\ e_0:\quad&
7iq_+
+\left[i\left(\ell+p+\frac12q\right)_+-7iq_+\right]
=i\left(\ell+p+\frac12q\right)_+,\\
AD,\ e_1:\quad&0+0=0,\\
AD,\ e_2:\quad&2iq_+-2iq_+=0,
\end{aligned}
$$

$$
\begin{aligned}
DA,\ e_0:\quad&-\frac i2q_++\frac i2q_+=0,\\
DA,\ e_1:\quad&i(p+q)_+-i(p+q)_+=0,\\
DA,\ e_2:\quad&i(p+q)_+
+\left[-i\ell_+-i(p+q)_+\right]
=-i\ell_+.
\end{aligned}
$$

The independent crossed-color replay gives, edge by edge,

$$
\mathcal C^{BA}_{AD,e}=\mathcal C^{AB}_{DA,e},
\qquad
\mathcal C^{BA}_{DA,e}=\mathcal C^{AB}_{AD,e},
\qquad e=0,1,2.
$$

Thus the same six displayed balances with $AD\leftrightarrow DA$ give all
six $\mathbb F^{BA}{}_{DE}$ rows.  The JSON ledger retains all twelve rows
separately.

The raw same-occurrence functional Hessian gives

$$
c_{\rm parent}=(-2)^3=-8,
\qquad
c_{\rm contact}=(-1)_{\rm SD}(-2)_{\rm Euler}(-2)^2=+8.
$$

Its complete combinatorial multiplicity is

$$
m_{\rm contact}
=\left(\frac1{2!}\,2_{\rm action\ order}\right)
 \left(\frac1{2!}\,2_{\rm cut\ endpoint}\right)
 \left(\frac1{2!}\,2_{\rm remaining\ Wick}\right)=1.
$$

Consequently, occurrence by occurrence and in each chirality sector,

$$
N^{\rm parent}_{d,\omega}+K^{\rm contact}_{\rm raw,\omega}=0,
$$

while the four-dimensional D-algebra numerator leaves

$$
N^{\rm parent}_{4,\omega}+K^{\rm contact}_{\rm raw,\omega}
=\frac{R_\omega\mu_\ell^2}{D_0D_1D_2}.
$$

For finite $w$, define

$$
(M_1)^B{}_C=w^m c_{LC}{}^B a_m^L,
\qquad
a_m^L=\frac{i\sqrt2}{8}\bar\sigma_m^{\dot ba}
[D_a,\bar D_{\dot b}]_{\rm ord}u^L\big|.
$$

The first Duhamel derivative is

$$
\frac{\delta(T_1Y)^B}{\delta a_n^J}
=w^n c_{JC}{}^B\int_0^1ds\,
e^{iw[sr+(1-s)r']}Y^C.
$$

With $x=iwr$ and $y=iwr'$,

$$
(x-y)\int_0^1ds\,e^{sx+(1-s)y}=e^x-e^y.
$$

Thus the one-link term and the two endpoint terms cancel before loop
integration.  This finite-$w$ sector is longitudinal in arbitrary $d$ and its
$\mu_\ell^2$ coefficient is exactly zero.

## 5. Full four-chirality TGG result

$$
\boxed{
\Gamma_{AD}
=-i\lambda_1\left[
\mathbb F^{AB}{}_{DE}\left(\frac13q_{\rm IR}+\frac16p_{\rm IR}\right)
+\mathbb F^{BA}{}_{DE}\left(\frac23q_{\rm IR}+\frac13p_{\rm IR}\right)
\right]_+
},
$$

$$
\boxed{
\Gamma_{DA}
=-i\lambda_1\left[
\mathbb F^{AB}{}_{DE}\left(\frac23q_{\rm IR}+\frac13p_{\rm IR}\right)
+\mathbb F^{BA}{}_{DE}\left(\frac13q_{\rm IR}+\frac16p_{\rm IR}\right)
\right]_+
}.
$$

The absolute conversion is

$$
4_{\rm chirality}\left(\frac12\right)_{\rm rank/trace}(-8)_{\rm legacy}
=-16.
$$

The factor $1/2$ is inserted exactly once; $m_{\rm contact}=1$ supplies no
second factor.  In canonical physical ordering,

$$
\boxed{
\mathcal A_{AD}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac13\langle P_{\dot a}D^D,D^E\rangle
+\frac23\langle D^D,P_{\dot a}D^E\rangle
\right]
},
$$

$$
\boxed{
\mathcal A_{DA}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac23\langle P_{\dot a}D^D,D^E\rangle
+\frac13\langle D^D,P_{\dot a}D^E\rangle
\right]
}.
$$

The independent $p$-only and $q$-only polarized replays pass $112/112$
checks each.  The raw local-contact and finite-$w$ link replay passes $255/255$
checks.

The former canonical artifact is `REJECTED_OUTPUT_ROUTING_AND_CROSSED_HESSIAN_OMISSION`.

$$
N_{\rm pass}=94,\qquad N_{\rm fail}=0.
$$
