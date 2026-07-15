# Step 5 AA matter triangle: independent four-occurrence audit

Status:
SECOND_MARK_FULL_SD_REPAIRED__FOUR_OCCURRENCES_TARGET_BLIND_UNIT_MAGNITUDE

Authority base:
origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66.

Scope: the two marked \(D_-\) placements, the two source attachments, the
full transported Schwinger--Dyson orbit, and the explicit
\(-2i(B_s\times C_s)\) current contacts in
\(\boldsymbol\nabla_-(A^AA^B)\). No holomorphic-twist coefficient is used.

## 1. Notation

For

$$
r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
u_i:=(a_i,b_i),
\qquad
v_i:=(c_i,d_i),
$$

define

$$
W_{ij}:=u_i\wedge u_j=a_ib_j-b_ia_j,
\qquad
\det r_i:=a_id_i-b_ic_i.
$$

The routing is

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q,
$$

$$
q=r_0-r_1,
\qquad
p=r_1-r_2.
$$

The endpoints are

$$
v_1:C^D(q),
\qquad
v_2:B^E(p).
$$

Define

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2},
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

The single common source-transpose orientation sign is denoted by

$$
\eta_{\mathrm{src}}\in\{+1,-1\}.
$$

It multiplies every row and does not affect any magnitude below.

## 2. Source kernels and endpoint transport

From (5A.49) and (5A.33),

$$
\Gamma_+^{(1)}=D_+V,
\qquad
\mathcal W_+^{(1)}=-\frac18\bar D^2D_+V,
$$

$$
\boxed{
A^{(1)}=-\frac18D_+\bar D^2D_+V.}
$$

Since \(D^2=2D_-D_+\),

$$
\boxed{
D_-A^{(1)}
=-\frac18D_-D_+\bar D^2D_+V
=-\frac1{16}D^2\bar D^2D_+V.}
$$

The two source factors in the fixed routing are

$$
\mathcal A_0(r_0)\delta^4_{01},
\qquad
\mathcal A_0(-r_2)\delta^4_{02},
$$

where

$$
\mathcal A(r):=D_+(r)\bar D^2(r)D_+(r),
\qquad
\mathcal M(r):=D_-(r)\mathcal A(r).
$$

For the internal chiral edge,

$$
\frac1{16D_1}
\bar D_1^2(r_1)D_1^2(r_1)\delta^4_{12}
$$

is the forward representation. Direct left-Grassmann differentiation gives

$$
D_{1a}(r_1)\delta^4_{12}
=-D_{2a}(-r_1)\delta^4_{12},
$$

$$
\bar D_{1\dot a}(r_1)\delta^4_{12}
=-\bar D_{2\dot a}(-r_1)\delta^4_{12}.
$$

Transferring all four derivatives reverses the projector order:

$$
\boxed{
\bar D_1^2(r_1)D_1^2(r_1)\delta^4_{12}
=D_2^2(-r_1)\bar D_2^2(-r_1)\delta^4_{12}.}
$$

Thus \(P_+\) at the chiral endpoint transfers to \(P_-\) at the antichiral
endpoint. It does not transfer to a second \(P_+\).

The external tests are

$$
\widetilde\Phi_C(1)
=e^{-i\vartheta_1q\bar\vartheta_1}C^D(q),
$$

$$
\Phi_B(2)
=e^{+i\vartheta_2p\bar\vartheta_2}
\vartheta_2^+B^E(p).
$$

## 3. Exact finite Grassmann words

At \(\vartheta_0=0\), define

$$
\begin{aligned}
\mathcal G_0:={}&
\int d^4\vartheta_1d^4\vartheta_2\,
\widetilde\Phi_C(1)\Phi_B(2)\\
&\times
\mathcal M_0(r_0)\delta^4_{01}\,
\mathcal A_0(-r_2)\delta^4_{02}\,
\bar D_1^2(r_1)D_1^2(r_1)\delta^4_{12},
\end{aligned}
$$

$$
\begin{aligned}
\mathcal G_2:={}&
\int d^4\vartheta_1d^4\vartheta_2\,
\widetilde\Phi_C(1)\Phi_B(2)\\
&\times
\mathcal A_0(r_0)\delta^4_{01}\,
\mathcal M_0(-r_2)\delta^4_{02}\,
\bar D_1^2(r_1)D_1^2(r_1)\delta^4_{12}.
\end{aligned}
$$

The finite Grassmann engine gives

$$
\boxed{
\mathcal G_0=-16384\,\mathcal S_{012},}
$$

$$
\boxed{
\mathcal G_2=-16384\,\mathcal T_{012},}
$$

with

$$
\mathcal S_{012}
=(\det r_0)W_{12}-(\det r_1)W_{02},
$$

$$
\mathcal T_{012}
=W_{01}(u_2\wedge v_1).
$$

The exact Schouten identity is

$$
\boxed{
\mathcal T_{012}
=-\mathcal S_{012}
+W_{12}(u_0\wedge q_-),}
$$

where \(q_-:=v_0-v_1\).

This identity is algebraic. It does not preserve the occurrence label of an
inverse kernel and therefore does not determine the Schwinger cut.

For comparison only, replacing the fixed second endpoint
\(\mathcal A_0(-r_2)\delta^4_{02}\) by
\(\mathcal A_0(+r_2)\delta^4_{02}\) gives

$$
\mathcal G_0^{(+r_2)}
=+16384\,\mathcal S_{012},
$$

$$
\mathcal G_2^{(+r_2)}
=+16384\,W_{01}(u_2\wedge p_-),
$$

and the collapsed words become

$$
\mathcal C_0^{(+r_2)}=+1024W_{02},
\qquad
\mathcal C_2^{(+r_2)}=-1024W_{02}.
$$

These four sign-reversed diagnostic words are not the fixed routing. They
show that changing \(r_2\) to \(-r_2\) after the Grassmann calculation is
invalid.

## 4. Four source occurrences and color

The two ordered color chains are

$$
\begin{aligned}
(T_A)^D{}_X(T_B)^X{}_E
&=(ic_{AX}{}^D)(ic_{BE}{}^X)\\
&=-c_{AX}{}^Dc_{BE}{}^X\\
&=c_{AX}{}^Dc_{BX}{}^E\\
&=\mathbb F^{AB}{}_{DE},
\end{aligned}
$$

$$
(T_B)^D{}_X(T_A)^X{}_E
=\mathbb F^{BA}{}_{DE}
=\mathbb F^{AB}{}_{ED}.
$$

The occurrence table is

| row | attachment | marked edge | raw word | color | endpoint wedge |
|---|---|---|---|---|---|
| \(F_1\) | \(u_A\to v_1,\ u_B\to v_2\) | \(r_0\) | \(-\mathcal S_{012}\) | \(\mathbb F^{AB}{}_{DE}\) | \(p_+\wedge q_+\) |
| \(F_2\) | \(u_A\to v_1,\ u_B\to v_2\) | \(r_2\) | \(-\mathcal T_{012}\) | \(\mathbb F^{AB}{}_{DE}\) | \(p_+\wedge q_+\) |
| \(X_1\) | \(u_A\to v_2,\ u_B\to v_1\) | \(r_2\) | \(-\mathcal T_{012}\) | \(\mathbb F^{AB}{}_{ED}\) | \(q_+\wedge p_+\) |
| \(X_2\) | \(u_A\to v_2,\ u_B\to v_1\) | \(r_0\) | \(-\mathcal S_{012}\) | \(\mathbb F^{AB}{}_{ED}\) | \(q_+\wedge p_+\) |

Here

$$
q_+\wedge p_+=-p_+\wedge q_+.
$$

The two action-copy assignments give

$$
w_{\mathrm{Wick}}
=\frac1{2!}(1+1)=1.
$$

The primitive graph factor is

$$
\frac{h^2}{\hbar^2}
(-2\hbar g^2)^2
\left(\frac{\hbar g^2}{16}\right)
=\frac{\hbar g^2}{4}.
$$

The two source factors, two Berezin measures, and raw Grassmann factor give

$$
\left(-\frac18\right)^2
\left(-\frac14\right)^2
(16384)=16.
$$

Thus every normalized parent word carries

$$
\boxed{
\eta_{\mathrm{src}}\,
\frac{\hbar g^2}{4}(16)
=4\eta_{\mathrm{src}}\hbar g^2.}
$$

## 5. Explicit matter-current contact

The tree identity contains

$$
\mathscr E_V
=\nabla^a\mathcal W_a
-2i(\Phi_s\times C_s),
$$

$$
\nabla_-A
=-\nabla_+\mathscr E_V
-2i(B_s\times C_s).
$$

At the free endpoint,

$$
D_+C_s=0,
$$

and therefore

$$
-D_+\bigl[-2i(\Phi_s\times C_s)\bigr]
-2i(B_s\times C_s)
=2i(B_s\times C_s)-2i(B_s\times C_s)
=0.
$$

The equality fixes the current-contact normalization relative to the
matter-edge Schwinger cut.

The collapsed-current Grassmann words are obtained by replacing the internal
projector word by \(\delta^4_{12}\):

$$
\begin{aligned}
\mathcal C_0^{\mathrm{raw}}
:={}&
\int d^4\vartheta_1d^4\vartheta_2\,
\widetilde\Phi_C(1)\Phi_B(2)\\
&\times
\mathcal M_0(r_0)\delta^4_{01}\,
\mathcal A_0(-r_2)\delta^4_{02}\,
\delta^4_{12},
\end{aligned}
$$

$$
\begin{aligned}
\mathcal C_2^{\mathrm{raw}}
:={}&
\int d^4\vartheta_1d^4\vartheta_2\,
\widetilde\Phi_C(1)\Phi_B(2)\\
&\times
\mathcal A_0(r_0)\delta^4_{01}\,
\mathcal M_0(-r_2)\delta^4_{02}\,
\delta^4_{12}.
\end{aligned}
$$

Direct expansion gives

$$
\boxed{
\mathcal C_0^{\mathrm{raw}}=-1024W_{02},
\qquad
\mathcal C_2^{\mathrm{raw}}=+1024W_{02}.}
$$

The projector collapse supplies

$$
\frac{16384}{1024}=16.
$$

Hence the occurrence-tagged current cuts are

$$
\boxed{
\mathcal C_0=-W_{02},
\qquad
\mathcal C_2=+W_{02}.}
$$

## 6. Primary-edge cuts and exact DRED defects

Use

$$
\det r_i=-\bar r_i^2,
\qquad
\bar r_i^2-r_{i,d}^2=\mu_\ell^2.
$$

### 6.1 Marked edge \(r_0\)

The exact occurrence decomposition is

$$
-\mathcal S_{012}
=\underbrace{-(\det r_0)W_{12}}_{\text{primary }r_0}
+\underbrace{(\det r_1)W_{02}}_{\text{current contact}}.
$$

The two cutting failures are

$$
\Delta_{0,\mathrm{primary}}
=\mu_\ell^2W_{12},
$$

$$
\Delta_{0,\mathrm{current}}
=-\mu_\ell^2W_{02}.
$$

Thus

$$
\boxed{
\Delta_0
=\mu_\ell^2(W_{12}-W_{02}).}
$$

### 6.2 Marked edge \(r_2\)

The exact marked-source operator split is

$$
D_-D_+\bar D^2D_+
=-8(\det r_2)D_+
-\frac12D_+\bar D^2D^2.
$$

The longitudinal endpoint transport is

$$
D_{0+}\bar D_0^2D_0^2\delta^4_{02}
=-D_2^2\bar D_2^2D_{2+}\delta^4_{02}.
$$

The adjacent chiral projector then gives

$$
D_2^2(-r_1)\bar D_2^2(-r_1)D_2^2(-r_1)
=-16(\det r_1)D_2^2(-r_1).
$$

Thus the longitudinal term produces a post-transport \(r_1\) inverse-kernel
cut. Define

$$
M_{21}:=a_2d_1-b_2c_1,
$$

$$
\Omega_{21}
:=a_2d_1-a_1d_2-b_2c_1+b_1c_2.
$$

Then

$$
\boxed{
2M_{21}
=\det r_1+\det r_2-\det p+\Omega_{21}.}
$$

For the raw word \(-\mathcal T_{012}\), the primary/current truncation gives

$$
\Delta_{2,\mathrm{pc}}
=\mu_\ell^2(W_{01}+W_{02})
\longmapsto
(y-z)\mu_\ell^2(p_+\wedge q_+).
$$

The transported longitudinal and mixed \(\Omega_{21}\) contact give

$$
\Delta_{2,\mathrm{long}}
\longmapsto
\left(\frac12-y\right)
\mu_\ell^2(p_+\wedge q_+).
$$

Therefore

$$
\boxed{
\Delta_2^{\mathrm{full}}
=\left(\frac12-z\right)
\mu_\ell^2(p_+\wedge q_+).}
$$

In the opposite \(+\mathcal T_{012}\) orientation,

$$
\boxed{
\mathcal R_2^{\mathrm{full}}
=\left(z-\frac12\right)
\mu_\ell^2(p_+\wedge q_+).}
$$

## 7. Location of the discarded-longitudinal error

The previous truncation used

$$
\Delta_{2,\mathrm{pc}}
\longmapsto
(y-z)\mu_\ell^2(p_+\wedge q_+)
$$

and discarded the remaining longitudinal word because its original tag was
no longer visible. Exact endpoint transport instead gives

$$
\Delta_{2,\mathrm{long}}
\longmapsto
\left(\frac12-y\right)
\mu_\ell^2(p_+\wedge q_+).
$$

Their sum is

$$
\boxed{
(y-z)+\left(\frac12-y\right)
=\frac12-z.}
$$

The longitudinal \(\Omega_{21}\) contact is fixed by

$$
\boxed{
\frac{L_d^2}{(L_d^2+\Delta)^3}
=\frac1{(L_d^2+\Delta)^2}
-\frac{\Delta}{(L_d^2+\Delta)^3}.}
$$

The first term is the collapsed bubble; the second is the rank-zero triangle
completion. Omitting either term breaks the full-\(d\) Schwinger identity.
The error was therefore discarding a tag generated after graded transport,
not the existence of the full rank-two trace.

## 8. Simplex moments

Use

$$
\frac1{D_0D_1D_2}
=2\int_{x,y,z\geq0}dx\,dy\,dz\,
\delta(1-x-y-z)
\frac1{(L^2+\Delta)^3},
$$

$$
k=L+(y+z)q+zp.
$$

The even parts are

$$
W_{01}\longmapsto-z(p_+\wedge q_+),
$$

$$
W_{02}\longmapsto+y(p_+\wedge q_+),
$$

$$
W_{12}\longmapsto-x(p_+\wedge q_+).
$$

The exact moments are

$$
2\int_{\Sigma_2}x
=2\int_{\Sigma_2}y
=2\int_{\Sigma_2}z
=\frac13.
$$

The evanescent master is

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

For the \(r_0\)-marked word,

$$
\Delta_{0,\mathrm{primary}}
\longmapsto-x\mu_\ell^2(p_+\wedge q_+),
$$

$$
\Delta_{0,\mathrm{current}}
\longmapsto-y\mu_\ell^2(p_+\wedge q_+).
$$

Therefore

$$
4\hbar g^2
\left[-2\int_{\Sigma_2}(x+y)\right]
\frac1{32\pi^2}
=-\frac43\lambda_1.
$$

For the \(r_2\)-marked word,

$$
\Delta_{2,\mathrm{pc}}
\longmapsto(y-z)\mu_\ell^2(p_+\wedge q_+),
$$

$$
\Delta_{2,\mathrm{long}}
\longmapsto
\left(\frac12-y\right)\mu_\ell^2(p_+\wedge q_+).
$$

Therefore

$$
2\int_{\Sigma_2}(y-z)=0,
$$

$$
2\int_{\Sigma_2}\left(\frac12-y\right)
=\frac16,
$$

$$
2\int_{\Sigma_2}\left(\frac12-z\right)
=\frac16,
$$

$$
\boxed{
4\hbar g^2
\left[2\int_{\Sigma_2}\left(\frac12-z\right)\right]
\frac1{32\pi^2}
=\frac13\lambda_1.}
$$

## 9. Four-row anomaly sector

With the common orientation sign retained,

$$
\boxed{
\begin{array}{c|c}
\text{row}&\text{anomaly-sector coefficient}\\ \hline
F_1&-\eta_{\mathrm{src}}\dfrac43\lambda_1\,
\mathbb F^{AB}{}_{DE}(p_+\wedge q_+)\\[2mm]
F_2&+\eta_{\mathrm{src}}\dfrac13\lambda_1\,
\mathbb F^{AB}{}_{DE}(p_+\wedge q_+)\\[2mm]
X_1&+\eta_{\mathrm{src}}\dfrac13\lambda_1\,
\mathbb F^{AB}{}_{ED}(q_+\wedge p_+)\\[2mm]
X_2&-\eta_{\mathrm{src}}\dfrac43\lambda_1\,
\mathbb F^{AB}{}_{ED}(q_+\wedge p_+)
\end{array}}
$$

For the forward attachment,

$$
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1.
$$

For the crossed attachment,

$$
-\frac43\lambda_1+\frac13\lambda_1=-\lambda_1
$$

in the displayed \(q_+\wedge p_+\) basis.  Thus each directed matter parent
has exact unit magnitude.  In the opposite \(+\mathcal S_1,+\mathcal S_2\)
orientation, the two coefficients are \(+4\lambda_1/3\) and
\(-\lambda_1/3\).

## 10. Gap verdicts

| id | type | priority | claim | missing operation | verdict |
|---|---|---:|---|---|---|
| AA-M4-G1 | G-OP | P0 | \(P_+\) transfers to \(P_+\) at the other endpoint | reverse the derivative order: \(P_+\to P_-\) | rejected |
| AA-M4-G2 | G-PROJ | P0 | only inverse kernels tagged before transport enter the SD orbit | transport the longitudinal word and apply \(D^2\bar D^2D^2=-16(\det r_1)D^2\) | rejected |
| AA-M4-G3 | G-ALG | P0 | the second placement is zero | add \((y-z)+(1/2-y)=1/2-z\) before the simplex integral | repaired to \(+\lambda_1/3\) in the raw orientation |
| AA-M4-G4 | G-IDX | P1 | \(\mathbb F^{AB}{}_{ED}\) and \(\mathbb F^{AB}{}_{DE}\) are one ordered slot | exchange \(D,E\) together with both endpoint fields | repaired |

Verification command:

    python scripts/step5_aa_matter_full_placements_independent_audit.py

Expected result:

    40/40 PASS
