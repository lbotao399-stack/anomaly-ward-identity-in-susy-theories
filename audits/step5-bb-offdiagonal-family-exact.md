# Step 5 ordered off-diagonal \(BB\) one-loop DRED audit

Status: PASS_BB_OFFDIAGONAL_DRED_SD_ORBIT_EXACT_HT_MATCH.

Authority base: origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66.

## 1. Notation

For route \(002\),

$$
r_0=\ell,\qquad r_1=\ell-p,\qquad r_2=\ell-p-q.
$$

For the independently oriented route \(003\),

$$
\rho_0=\ell,\qquad \rho_1=\ell-q,\qquad \rho_2=\ell-p-q.
$$

Its canonical loop rebase is

$$
k_0=-\rho_2,\qquad k_1=-\rho_1=k_0-p,\qquad
k_2=-\rho_0=k_0-p-q.
$$

Set

$$
D_i=r_{i,d}^2,\qquad
\bar r_i^2=r_{i,d}^2+\mu_\ell^2,\qquad
\det r_i=-\bar r_i^2,
$$

$$
v(k)=\left(-k_{+\dot2},k_{+\dot1}\right),\qquad
\lambda_1=\frac{\hbar g^2}{16\pi^2},
$$

$$
A_{DC}=\langle D^D,C_3^E\rangle,\qquad
A_{CD}=\langle C_3^D,D^E\rangle.
$$

## 2. Source and resolvent

$$
B_{r,c}=B_{r,0}+gB_{r,1}+g^2B_{r,2},
$$

$$
B_{r,0}=D_+\phi_r,\qquad
B_{r,1}=\sqrt2[D_+u,\phi_r],
$$

$$
B_{r,2}=[(D_+u)u-u(D_+u),\phi_r].
$$

Therefore

$$
N(O_0,O_1,O_2)=(1,2,3),\qquad
N(I_0,I_1,I_2)=(2,6,12),
$$

$$
\Gamma_{g^2}^{(1)}
=\langle I_2\rangle_0
-\frac1\hbar\langle I_1S_3\rangle_{0,c}
-\frac1\hbar\langle I_0S_4\rangle_{0,c}
+\frac1{2\hbar^2}\langle I_0S_3S_3\rangle_{0,c}.
$$

## 3. Split-source cubic parents

Parent IDs: BB-TMM-001, BB-TMH-002, BB-TMH-003.

For \(B_1>B_2\),

$$
\begin{array}{c|c|c|c}
\mathrm{id}&\mathrm{vertices}&\mathrm{external\ ports}&\mathrm{topology}\\ \hline
\mathrm{BB\!-\!TMM\!-\!001}&M_1,M_2&(\phi_1,\phi_2)&TMM\\
\mathrm{BB\!-\!TMH\!-\!002}&M_1,H_-&(u,\widetilde\phi_3)&TMH\\
\mathrm{BB\!-\!TMH\!-\!003}&H_-,M_2&(\widetilde\phi_3,u)&TMH
\end{array}
$$

Sparse Grassmann integration gives

$$
R_{001,L}=R_{001,R}=0,\qquad R_{002,L}=R_{003,R}=0,
$$

$$
R_{002,R}
=128v(r_0)
=\left(-128r_{0,+\dot2},128r_{0,+\dot1}\right).
$$

For route \(003\), the independent sparse collapse gives

$$
R_{003,L}=-128v(\rho_2)=128v(k_0).
$$

The direct cores before the pure-antichiral endpoint are

$$
N_{\mathrm{core},002}^{\mathrm{dir}}
=1024v(r_0)\det r_2,
$$

$$
N_{\mathrm{core},003}^{\mathrm{dir}}
=-1024v(\rho_2)\det\rho_0
=1024v(k_0)\det k_2.
$$

## 4. Exact first error: endpoint product rule

Let \(\Pi_b\) be the bridge projector and \(\Pi_s\) the source-edge projector. Both are Grassmann-even. Since

$$
D^2=2D_-D_+,
$$

the complete identity is

$$
\begin{aligned}
D^2(\Pi_b\Pi_s)
={}&(D^2\Pi_b)\Pi_s+\Pi_b(D^2\Pi_s)\\
&+2(D_-\Pi_b)(D_+\Pi_s)
-2(D_+\Pi_b)(D_-\Pi_s).
\end{aligned}
$$

In the ordered \(u,C_3\) projection,

$$
(D^2\Pi_b)\Pi_s=0,\qquad
2(D_-\Pi_b)(D_+\Pi_s)=0.
$$

The two surviving terms are

$$
\Pi_b(D^2\Pi_s),\qquad
-2(D_+\Pi_b)(D_-\Pi_s).
$$

The pure-antichiral endpoint is

$$
\theta^2=-2\theta^+\theta^-,
\qquad
\boxed{D^2\theta^2=-4}.
$$

The exact sparse collapse is

$$
\Pi_b(D^2\Pi_s)
\longmapsto
(-4)1024v(r_0)\det r_2
=4096v(r_0)\bar r_2^2,
$$

$$
-2(D_+\Pi_b)(D_-\Pi_s)
\longmapsto
-2048v(r_0)\det r_1
=2048v(r_0)\bar r_1^2.
$$

Thus BB-TRANSPORTED-EDGE is a second occurrence:

$$
O^{\mathrm{dir}}:\quad 4096v(r_0)\bar r_2^2,\quad e=2,
$$

$$
O^{\mathrm{tr}}:\quad 2048v(r_0)\bar r_1^2,\quad e=1,
$$

$$
\frac{O^{\mathrm{tr}}}{O^{\mathrm{dir}}}
=\frac{-2}{-4}=\frac12.
$$

The independently oriented route \(003\) gives

$$
N_{\mathrm{core},003}^{\mathrm{dir}}
=-1024v(\rho_2)\det\rho_0,
$$

$$
N_{\mathrm{core},003}^{\mathrm{tr}}
=+2048v(\rho_2)\det\rho_1.
$$

Using \(v(\rho_2)=-v(k_0)\) and \(\det\rho_j=\det k_{2-j}\),

$$
N_{\mathrm{endpoint},003}^{\mathrm{dir}}
=4096v(k_0)\bar k_2^2,
$$

$$
N_{\mathrm{endpoint},003}^{\mathrm{tr}}
=2048v(k_0)\bar k_1^2.
$$

The single-projector identity

$$
D^2\bar D^2D^2\delta^4=16\det(r)D^2\delta^4
$$

does not delete the neighboring occurrence, because

$$
D_+\bar D^2D^2\delta^4
=16\det(r)D_+\delta^4
-D^2\bar D^2D_+\delta^4.
$$

## 5. Full-\(d\) Schwinger–Dyson pairs

For every selected edge \(e\),

$$
\frac{r_{e,d}^2R_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\ne e}D_j}=0.
$$

In DRED,

$$
\frac{\bar r_e^2R_e}{D_0D_1D_2}
-\frac{R_e}{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2R_e}{D_0D_1D_2}.
$$

The triangle and nonlinear-contact prefactors are

$$
P_\triangle
=g^2\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(\frac\hbar{16}\right)^3
\frac1{2!}(1+1)
=-\frac{\hbar g^4}{2048},
$$

$$
P_{I_1H}
=g^2(\sqrt2g)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left(\frac\hbar{16}\right)^2
=-\frac{\hbar g^4}{128}.
$$

For the transported edge,

$$
P_\triangle(2048)+P_{I_1H}(-128)
=-\hbar g^4+\hbar g^4=0.
$$

Therefore its full-\(d\) orbit is pointwise zero:

$$
P_\triangle\frac{2048r_{1,d}^2v(r_0)}{D_0D_1D_2}
+P_{I_1H}\frac{-128v(r_0)}{D_0D_2}=0.
$$

Its DRED remainder is

$$
P_\triangle\frac{2048\mu_\ell^2v(r_0)}{D_0D_1D_2}.
$$

The direct and transported evanescent words are

$$
N^{\mathrm{ev}}_{\mathrm{dir}}
=4096\mu_\ell^2v(r_0),
\qquad
N^{\mathrm{ev}}_{\mathrm{tr}}
=2048\mu_\ell^2v(r_0).
$$

## 6. \(I_1S_{H_-}\) contact rows

BB-I1-HMINUS-CONTACTS consists of six tagged rows:

$$
\begin{array}{c|c|c}
\mathrm{row}&\mathrm{regulated\ D\!-\!word}&\mathrm{status}\\ \hline
T_1&0&D_+^2=0\\
E_1&\bar q^2-q_d^2=0&\mathrm{external\ EOM}\\
T_2&-128v(r_0)/(D_0D_2)&\mathrm{route\ 002,\ bridge}\ r_1\\
T_4&-128v(k_0)/(K_0K_2)&\mathrm{route\ 003,\ bridge}\ k_1\\
T_3&0&D_+^2=0\\
E_2&\bar p^2-p_d^2=0&\mathrm{external\ EOM}
\end{array}
$$

Although the uncolored local polynomials in \(T_2,T_4\) agree, their complete occurrence data are

$$
\begin{array}{c|c|c|c}
&\mathrm{color}&\mathrm{ports}&\mathrm{selected\ edge}\\ \hline
T_2&+i\mathbb F^{AB}{}_{DE}&(u^D,C_3^E)&r_1\\
T_4&-i\mathbb F^{AB}{}_{DE}&(C_3^D,u^E)&k_1
\end{array}
$$

and hence they cannot be subtracted as one untagged polynomial.

## 7. Simplex moments

$$
2\int_{\Sigma_2}1=1,\qquad
2\int_{\Sigma_2}y=\frac13,\qquad
2\int_{\Sigma_2}z=\frac13.
$$

For route \(002\),

$$
r_0=L+yp+z(p+q),\qquad
2\int_{\Sigma_2}r_0=\frac23p+\frac13q.
$$

For route \(003\), first rebase the independently oriented loop:

$$
k_0=-\rho_2,\qquad
k_1=k_0-p,\qquad
k_2=k_0-p-q,
$$

$$
k_0=L+yp+z(p+q),\qquad
2\int_{\Sigma_2}k_0=\frac23p+\frac13q.
$$

The route-\(003\) external ports are reversed, so \(q/3\) multiplies \(A_{DC}\) and \(2p/3\) multiplies \(A_{CD}\). No factor \(p^2,\bar p^2,q^2,\bar q^2\) multiplies these rank-one carriers. Therefore neither \(p/3\) nor \(q/3\) is an external-EOM term.

The scalar master is

$$
\int_\ell^{\mathrm{DRED}}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

## 8. External maps, signs, and normalized outputs

For the source probe \(u_{\dot a}=\theta^+\theta^-\bar\theta_{\dot a}\),

$$
D^2\bar D_{\dot a}u_{\dot a}\big|=-2,
\qquad
D^2\bar D_{\dot a}u\big|=-\frac{4\sqrt2}{g}D_{\dot a},
\qquad
C_3=g\widetilde\phi_3.
$$

Therefore

$$
M_{\mathrm{ext}}=\frac{2\sqrt2}{g^2}.
$$

The exact color contractions are

$$
\sum_X\epsilon_{DXA}\epsilon_{XBE}=\mathbb F^{AB}{}_{DE},
\qquad
\sum_X\epsilon_{EXB}\epsilon_{AXD}=-\mathbb F^{AB}{}_{DE}.
$$

Including product Koszul and source-attachment signs gives

$$
s_{002}=-i,\qquad s_{003}=+i.
$$

The direct rows are

$$
\Gamma_{002}^{\mathrm{dir}}
=-2i\sqrt2\lambda_1\mathbb F
\left(\frac23A_{DC}+\frac13A_{CD}\right),
$$

$$
\Gamma_{003}^{\mathrm{dir}}
=+2i\sqrt2\lambda_1\mathbb F
\left(\frac13A_{DC}+\frac23A_{CD}\right).
$$

Hence

$$
\Gamma_{\mathrm{dir}}
=\lambda_1\mathbb F
\left(-\frac{2i\sqrt2}{3}A_{DC}
+\frac{2i\sqrt2}{3}A_{CD}\right).
$$

The transported rows are

$$
\Gamma_{002}^{\mathrm{tr}}
=-i\sqrt2\lambda_1\mathbb F
\left(\frac23A_{DC}+\frac13A_{CD}\right),
$$

$$
\Gamma_{003}^{\mathrm{tr}}
=+i\sqrt2\lambda_1\mathbb F
\left(\frac13A_{DC}+\frac23A_{CD}\right).
$$

Thus

$$
\Gamma_{\mathrm{tr}}
=\lambda_1\mathbb F
\left(-\frac{i\sqrt2}{3}A_{DC}
+\frac{i\sqrt2}{3}A_{CD}\right),
$$

$$
\boxed{
\Gamma_{B_1>B_2}^{(1)}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[-i\sqrt2\,A_{DC}+i\sqrt2\,A_{CD}\right].
}
$$

## 9. Spectator-source double-bridge family

The complete SPECTATOR_SOURCE_DOUBLE_BRIDGE census for \(B_1>B_2\) is

$$
\begin{array}{c|c|c|c}
\mathrm{id}&\mathrm{spectator}&(V_1,V_2)&\mathrm{external\ ports}\\ \hline
\mathrm{BB\!-\!SPEC\!-\!001}&B_1&(H_-,H_+)&(\phi_1,\phi_2)\\
\mathrm{BB\!-\!SPEC\!-\!002}&B_1&(M_2,M_2)&(\phi_1,\phi_2)\\
\mathrm{BB\!-\!SPEC\!-\!003}&B_2&(H_-,H_+)&(\phi_2,\phi_1)\\
\mathrm{BB\!-\!SPEC\!-\!004}&B_2&(M_1,M_1)&(\phi_2,\phi_1)
\end{array}
$$

For each row,

$$
\mathsf P_{(u,\widetilde\phi_3)}(\phi_1,\phi_2)=0,
\qquad
\mathsf P_{(\widetilde\phi_3,u)}(\phi_1,\phi_2)=0,
$$

$$
\mathsf P_{(u,\widetilde\phi_3)}(\phi_2,\phi_1)=0,
\qquad
\mathsf P_{(\widetilde\phi_3,u)}(\phi_2,\phi_1)=0.
$$

Thus all four spectator-source parents have exact zero \(A_{DC},A_{CD}\) projection.

For every row, the three internal edges are

$$
e_s=(S,V_1),\qquad e_{b,1}=(V_1,V_2),\qquad e_{b,2}=(V_1,V_2).
$$

The loop number is

$$
L=I-V+1=3-3+1=1.
$$

Deleting \(e_s\) disconnects the source external leg from \(V_1,V_2\). Hence

$$
e_s\ \text{is an articulation edge},\qquad
\mathrm{1PI}=0.
$$

All four rows are external self-energy attachments and do not enter the amputated \(BB\) coefficient.

## 10. Remaining resolvent rows

The Euler potential and explicit contact have identical regulated kernels:

Occurrence IDs: BB-E-POT, BB-X-POT.

$$
\mathrm{BB\!-\!E\!-\!POT}=+\sqrt2K_{\mathrm{potential}},
\qquad
\mathrm{BB\!-\!X\!-\!POT}=-\sqrt2K_{\mathrm{potential}},
$$

$$
\mathrm{BB\!-\!E\!-\!POT}
+\mathrm{BB\!-\!X\!-\!POT}=0.
$$

The twelve \(I_2\) rows have no \(\widetilde\phi_3\) port. The \(I_0S_4\) matter rows cannot absorb both flavors \(1,2\); \(H_-\) has no quartic vertex. Gauge-fixing and ghost rows have no pair of matter-flavor ports. The off-diagonal coincident Jacobian contains \(\delta_{12}=0\).

## 11. \(SU(3)\) lift and sealed comparison

For every ordered \(r\ne s\), with \(\epsilon_{rst}\ne0\),

$$
\boxed{
\Gamma_{B_r>B_s}^{(1)}
=\epsilon_{rst}\lambda_1\mathbb F^{AB}{}_{DE}
\left[
-i\sqrt2\langle D^D,C_t^E\rangle
+i\sqrt2\langle C_t^D,D^E\rangle
\right].
}
$$

The target-blind Project vector is

$$
c_{\mathrm{Project}}=(-i\sqrt2,+i\sqrt2).
$$

Only now reading the sealed holomorphic-twist row gives

$$
c_{\mathrm{HT}}=(-i\sqrt2,+i\sqrt2),
\qquad
c_{\mathrm{HT}}-c_{\mathrm{Project}}=(0,0).
$$

GPT Pro Gate 1 is rejected. Gate 2, SHA-256 31f8906d79cd5f824191eb9d09c7733f4723a2916e45e5bac3c2f826f2e7d2e0, is accepted only after the independent local sparse-Grassmann, contact-normalization, routing, and spectator-parent checks above.
