# Step 5 ordered $A>D_{dot1}$ and $D_{dot1}>A$ anomaly sector

Status: `TARGET_BLIND_CONDITIONAL_FF_ANOMALY_SECTOR_EDGEWISE_COMPLETE__ABSOLUTE_AUTHORITY_NORMALIZATION_AND_LOCAL_SLICE_BLOCKED`.

Machine ledger: `audits/step5-ad-da-gauge-family-raw-exact.json`.

GPT Pro Gate 1 is archived as non-authority review in
`proposals/gpt-pro-ad-da-edgewise-gauge-fp-gate1-response-2026-07-14.md`.
Every result below used in the ledger is replayed from the local Step-5A words;
no holomorphic-twist coefficient is read.

## 1. Notation

$$
r_0=\ell,
\qquad
r_1=\ell+p,
\qquad
r_2=\ell+p+q,
$$

$$
P_3=D_0D_1D_2,
\qquad
P_{\widehat e}=\prod_{j\ne e}D_j,
$$

$$
\mu_\ell^2=\bar r_e^{,2}-r_{e,d}^{,2}.
$$

The first incorrect operation was

$$
\det_4(r_e)\longrightarrow\mu_\ell^2
$$

inside `source_component_entry(marked_sector='evanescent')`, before the
occurrence-resolved Schwinger contact had been constructed.  The corrected
order is

$$
\text{four-dimensional parent}
\longrightarrow
\text{same-edge full-}d\text{ cut}
\longrightarrow
\mu_\ell^2\text{ remainder}.
$$

## 2. Source operator and gauge-fixing row

The exact source identity is

$$
D_-D_+\bar D^2D_+
=-8\bar r_e^{,2}D_+
-\frac12D_+\bar D^2D^2.
$$

The conditional Fermi--Feynman projector is

$$
\mathcal P_0
=\frac{\bar D^2D^2+D^2\bar D^2}{16\Box}.
$$

Hence

$$
\begin{aligned}
8D_+\Box\mathcal P_0
&=\frac12D_+\bar D^2D^2
+\frac12D_+D^2\bar D^2,\\
D_+D^2\bar D^2&=0,
\end{aligned}
$$

and therefore

$$
8D_+\Box\mathcal P_0
=\frac12D_+\bar D^2D^2.
$$

The longitudinal source row and the gauge-fixing Euler row cancel:

$$
-\frac12D_+\bar D^2D^2
+\frac12D_+\bar D^2D^2=0.
$$

The sparse algebra verifies the full/selected/longitudinal decomposition for
$32$ component masks and the gauge-fixing cancellation for another $32$
component masks.

## 3. Routewise parent-minus-cut quotient

For each route $\rho$, let

$$
R_\rho(\ell,p,q)
=a_\rho\ell_{+\dot1}
+b_\rho p_{+\dot1}
+c_\rho q_{+\dot1}.
$$

For $A>D_{\dot1}$ the marked edge is $e=0$.  Every one of the $36$ TGG
rows contains the two distinct fractions

$$
\frac{\bar r_0^{,2}R_\rho}{D_0D_1D_2},
\qquad
-\frac{R_\rho}{D_1D_2}.
$$

The full-$d$ family is

$$
R_\rho
\left[
\frac{r_{0,d}^{,2}}{D_0D_1D_2}
-\frac1{D_1D_2}
\right]=0.
$$

Only after this identity is recorded does DRED give

$$
R_\rho
\left[
\frac{\bar r_0^{,2}}{D_0D_1D_2}
-\frac1{D_1D_2}
\right]
=\frac{\mu_\ell^2R_\rho}{D_0D_1D_2}.
$$

For $D_{\dot1}>A$ the marked edge is $e=2$:

$$
\frac{\bar r_2^{,2}R_\rho}{D_0D_1D_2},
\qquad
-\frac{R_\rho}{D_0D_1},
$$

$$
R_\rho
\left[
\frac{r_{2,d}^{,2}}{D_0D_1D_2}
-\frac1{D_0D_1}
\right]=0,
$$

$$
R_\rho
\left[
\frac{\bar r_2^{,2}}{D_0D_1D_2}
-\frac1{D_0D_1}
\right]
=\frac{\mu_\ell^2R_\rho}{D_0D_1D_2}.
$$

The JSON ledger prints these four entries separately for all $72$ TGG rows.

## 4. TGG sums and exact integrals

The $36$ route sums are

$$
N_{AD}^{\rm ev}
=\frac{i}{16}\mu_\ell^2
\left(
\ell+p+\frac12q
\right)_{+\dot1},
$$

$$
N_{DA}^{\rm ev}
=-\frac{i}{16}\mu_\ell^2\ell_{+\dot1}.
$$

Feynman parameters give

$$
\frac1{D_0D_1D_2}
=2\int_0^1dy\int_0^{1-y}dz
\frac1{(L^2+\Delta)^3},
$$

$$
L=\ell+(y+z)p+zq,
\qquad
\ell=L-(y+z)p-zq.
$$

The exact simplex moments are

$$
2\int_0^1dy\int_0^{1-y}dz=1,
$$

$$
2\int_0^1dy\int_0^{1-y}dz\,(y+z)=\frac23,
\qquad
2\int_0^1dy\int_0^{1-y}dz\,z=\frac13.
$$

The DRED masters are

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2},
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2\ell_{+\dot1}}{D_0D_1D_2}
=-\frac{(2p+q)_{+\dot1}}{96\pi^2}.
$$

Thus

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{N_{AD}^{\rm ev}}{D_0D_1D_2}
=\frac1{32\pi^2}
\left(
\frac{i}{48}p_{+\dot1}
+\frac{i}{96}q_{+\dot1}
\right),
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{N_{DA}^{\rm ev}}{D_0D_1D_2}
=\frac1{32\pi^2}
\left(
\frac{i}{24}p_{+\dot1}
+\frac{i}{48}q_{+\dot1}
\right).
$$

With the local conditional normalization

$$
D_{\dot a}[u]= -\frac{\sqrt2}{8}\eta_{\dot a},
\qquad
F_{01;10}=-2,
$$

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},
\qquad
\text{raw integrated}\longrightarrow\lambda_1\text{ coefficient}=-8,
$$

one obtains

$$
\Gamma_{AD}^{\rm cond}
=-i\lambda_1
\left(
\frac16p_{+\dot1}
+\frac1{12}q_{+\dot1}
\right),
$$

$$
\Gamma_{DA}^{\rm cond}
=-i\lambda_1
\left(
\frac13p_{+\dot1}
+\frac16q_{+\dot1}
\right).
$$

## 5. Ordered external momenta

The raw loop variables $p,q$ are not the ordered external jets.

For $A>D$,

$$
(k_L,k_R)=(q,-p-q),
$$

$$
p=-k_L-k_R,
\qquad
q=k_L.
$$

Therefore

$$
\frac16p+\frac1{12}q
=-\frac1{12}k_L-\frac16k_R
=-\frac14
\left(
\frac13k_L+\frac23k_R
\right),
$$

$$
\Gamma_{AD}^{\rm cond}
=\frac{i\lambda_1}{4}
\left(
\frac13k_L+\frac23k_R
\right)_{+\dot1}.
$$

For $D>A$,

$$
(k_L,k_R)=(-p-q,q),
$$

$$
p=-k_L-k_R,
\qquad
q=k_R.
$$

Therefore

$$
\frac13p+\frac16q
=-\frac13k_L-\frac16k_R
=-\frac12
\left(
\frac23k_L+\frac13k_R
\right),
$$

$$
\Gamma_{DA}^{\rm cond}
=\frac{i\lambda_1}{2}
\left(
\frac23k_L+\frac13k_R
\right)_{+\dot1}.
$$

Thus the target-blind external shapes are

$$
AD:\left(\frac13,\frac23\right),
\qquad
DA:\left(\frac23,\frac13\right),
$$

while the local conditional overall ratio is

$$
\frac{\mathcal N_{AD}}{\mathcal N_{DA}}=\frac12.
$$

The ordered-source authority normalization is not locked, so this last ratio
is not promoted to the Project coefficient.

## 6. O05, O06, and O07

O05 is resolved before edge aggregation.  For $A>D$,

$$
\begin{array}{c|c|c}
\text{source tag}&\text{edge}&\text{numerator}\\ \hline
I1\_N1A2[A]D1[B]&r_0&5iq_{+\dot1}\\
I1\_N1\gamma1[A]D1[B]&r_0&2iq_{+\dot1}\\
I1\_N0[A]D2[B]&r_2&2iq_{+\dot1}
\end{array}
$$

Hence

$$
\mathcal C_{AD}^{O05}
=\frac{7iq_{+\dot1}}{D_1D_2}
+\frac{2iq_{+\dot1}}{D_0D_1}.
$$

For $D>A$,

$$
\begin{array}{c|c|c}
\text{source tag}&\text{edge}&\text{numerator}\\ \hline
I1\_{-D2[A]N0[B]}&r_0&-\dfrac i2q_{+\dot1}\\
I1\_{-D1[A]N1A2[B]}&r_2&i(p+q)_{+\dot1}
\end{array}
$$

$$
\mathcal C_{DA}^{O05}
=-\frac{iq_{+\dot1}}{2D_1D_2}
+\frac{i(p+q)_{+\dot1}}{D_0D_1}.
$$

Each O05 occurrence has

$$
\frac{\partial^2N_{O05}}{\partial\ell_m\partial\ell_n}=0.
$$

O06 lies on $r_1$:

$$
N_{AD}^{O06}=0,
$$

$$
N_{DA}^{O06,+}
=\frac i2(p+q)_{+\dot1},
\qquad
N_{DA}^{O06,-}
=\frac i2(p+q)_{+\dot1},
$$

$$
\mathcal C_{DA}^{O06}
=\frac{i(p+q)_{+\dot1}}{D_0D_2}.
$$

Thus O06 also has zero loop Hessian.  O05 and O06 remain ordinary contact
members, but neither contains a four-dimensional scalar loop square; their
standalone extra-dimensional anomaly sectors are zero.

For O07 the exact component/color contraction vanishes on eight independent
rational pair samples.  Its only possible integral has one massless
propagator:

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{P(\ell)}{\ell^2}=0
$$

by DRED scalelessness.  Hence the integrated O07 anomaly sector is zero.

## 7. Matter current pair

The common DD word is

$$
K_{\dot1}=ir_{+\dot2},
\qquad
K_{\dot2}=-ir_{+\dot1}.
$$

The two separate Schwinger members are

$$
\mathcal M_{\rm Euler}=2iK_{\dot a},
\qquad
\mathcal M_{\rm explicit}=-2iK_{\dot a}.
$$

Therefore

$$
\mathcal M_{\rm Euler}
+\mathcal M_{\rm explicit}=0.
$$

Both words are affine in loop momentum, so

$$
\mathcal M_{\mu^2}=0.
$$

## 8. FP Euler bubble

From $B_1=-1/2$ in Step 5A.57,

$$
sV
=i(\widetilde c-c)
+\frac i2
\left(
[\widetilde c,V]+[c,V]
\right)
+O(V^2).
$$

The free kernels and constrained inverses are

$$
K_+=\frac i4\bar D^2,
\qquad
K_+^{-1}=-\frac i4\frac{D^2}{\Box},
$$

$$
K_-=-\frac i4D^2,
\qquad
K_-^{-1}=\frac i4\frac{\bar D^2}{\Box},
$$

$$
K_+K_+^{-1}=\mathcal P_+,
\qquad
K_-K_-^{-1}=\mathcal P_-.
$$

The two connected cubic vertices are

$$
\mathcal V_+
=\frac i8\int_+c'_+\bar D^2[c,V],
$$

$$
\mathcal V_-
=\frac i8\int_-\widetilde c'_-D^2[\widetilde c,V].
$$

The closed Grassmann loop sign is $-1$.  A representative ordered word is

$$
\Pi_{\dot1}^{(-)}
\operatorname{Tr}_D
\left[
\bar D^2\operatorname{ad}_{V_L}
\frac{\bar D^2}{\Box_{s_0}}
D^2\operatorname{ad}_{V_R}
\frac{D^2}{\Box_{s_1}}
\right]
\Pi_{\dot2}^{(-)}.
$$

With

$$
s_0=\ell,
\qquad
s_1=\ell+K,
$$

the two exact full-$d$ cuts are

$$
\frac{s_{0,d}^2}{s_0^2s_1^2}
-\frac1{s_1^2}=0,
$$

$$
\frac{s_{1,d}^2}{s_0^2s_1^2}
-\frac1{s_0^2}=0.
$$

The FP quadratic inverse is the full-$d$ $\Box$ kernel; it is not the
four-dimensional marked spin determinant.  Therefore

$$
\Gamma_{\rm FP,Euler}^{DD}=\mathcal B_{\rm FP}^{DD},
$$

$$
\Gamma_{\rm FP,cut}^{DD}=-\mathcal B_{\rm FP}^{DD},
$$

$$
\Gamma_{\rm FP,full\ SD}^{DD}=0,
\qquad
R_{\rm FP}^{\mu^2}=0.
$$

The separated Nielsen--Kallosh branch is absent from the selected conditional
graph set.  No independent zero or numerical weight is assigned to it.

## 9. Spectator routes and remaining authority gate

For each ordering,

$$
N_{\rm connected}=84
=42_{\rm split\ source}+42_{\rm spectator}.
$$

Cutting the unique source-to-action stem of every spectator route disconnects
the insertion from the self-energy loop.  Hence

$$
\Pi_{1PI}^{\rm amputated}G_{\rm spectator}=0.
$$

The independent control component gives

$$
F_{01;10}^{\rm spectator}=0.
$$

The conditional anomaly sector is exhausted.  The two authority blockers are

$$
\boxed{
\texttt{BLOCKED\_AD\_DA\_AUTHORITY\_ORDERED\_SOURCE\_HESSIAN\_NORMALIZATION}}
$$

and

$$
\boxed{
\texttt{BLOCKED\_STEP5A\_LOCAL\_FERMI\_FEYNMAN\_PROPER\_SLICE}.}
$$
