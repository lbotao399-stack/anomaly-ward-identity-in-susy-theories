# Step 5 ordered \(AA\) raw gauge convolution and occurrence-tagged cut

Status: `REJECTED_FIXED_FIELD_STRENGTH_SLOT_ONLY__SUPERSEDED_BY_FULL_POLARIZED_SYMBOLIC_AUDIT`.

This artifact differentiates only the rows where the external background is
the linear field-strength slot.  It omits the differentiated and
undifferentiated commutator slots.  Therefore its compact Hessian and
ordered vector are not the full AA triangle.  The exact counterexample is

$$
N_{\rm full}(2,-1,1,3)=6-\frac{19}{2}i,
\qquad
N_{\rm fixed\ strength}(2,-1,1,3)=-5.
$$

The superseding calculation is
`audits/step5-aa-full-polarized-symbolic-exact.json`.

Authority: Step 5A (5A.52). No holomorphic-twist or Project coefficient enters this audit.

## 1. Raw cubic words

Define

$$
K(X,Y;Z):=\kappa_{AB}(XY)^A Z^B,
$$

$$
K(X,Y;Z)-K(Y,X;Z)=i\,c_{XYZ}.
$$

For

$$
p+q+r+s=1,\qquad
\eta_E=-1,\qquad
f_{AB}=\widetilde f_{AB}=h\kappa_{AB},
$$

the chiral words are

$$
S_{E,+}^{(3)}
=\frac{h\kappa_{AB}}{512}\int_+
(\mathcal P_+-\mathcal Q_++\mathcal R_+-\mathcal S_+),
$$

$$
\begin{aligned}
\mathcal P_+
&=[\bar D^2(V_XD^aV_Y)]^A[\bar D^2D_aV_Z]^B,
&(p,q,r,s)&=(1,0,0,0),\\
\mathcal Q_+
&=[\bar D^2(D^aV_XV_Y)]^A[\bar D^2D_aV_Z]^B,
&(p,q,r,s)&=(0,1,0,0),\\
\mathcal R_+
&=[\bar D^2D^aV_X]^A[\bar D^2(V_YD_aV_Z)]^B,
&(p,q,r,s)&=(0,0,1,0),\\
\mathcal S_+
&=[\bar D^2D^aV_X]^A[\bar D^2(D_aV_YV_Z)]^B,
&(p,q,r,s)&=(0,0,0,1).
\end{aligned}
$$

The antichiral words are

$$
S_{E,-}^{(3)}
=\frac{h\kappa_{AB}}{512}\int_-
(-\mathcal P_-+\mathcal Q_--\mathcal R_-+\mathcal S_-),
$$

$$
\begin{aligned}
\mathcal P_-
&=[D^2(V_X\bar D_{\dot a}V_Y)]^A[D^2\bar D^{\dot a}V_Z]^B,\\
\mathcal Q_-
&=[D^2(\bar D_{\dot a}V_XV_Y)]^A[D^2\bar D^{\dot a}V_Z]^B,\\
\mathcal R_-
&=[D^2\bar D_{\dot a}V_X]^A[D^2(V_Y\bar D^{\dot a}V_Z)]^B,\\
\mathcal S_-
&=[D^2\bar D_{\dot a}V_X]^A[D^2(\bar D^{\dot a}V_YV_Z)]^B.
\end{aligned}
$$

For every row,

$$
256\,p!q!r!s!(p+q+1)(r+s+1)=512.
$$

## 2. All labeled port derivatives

Here \(S\), \(B\), \(E\) denote source, bridge, external port. For every raw word use all six assignments:

| row | \(X\) | \(Y\) | \(Z\) |
|---:|---:|---:|---:|
| 1 | \(S\) | \(B\) | \(E\) |
| 2 | \(S\) | \(E\) | \(B\) |
| 3 | \(B\) | \(S\) | \(E\) |
| 4 | \(B\) | \(E\) | \(S\) |
| 5 | \(E\) | \(S\) | \(B\) |
| 6 | \(E\) | \(B\) | \(S\) |

Thus

$$
N_{\mathrm{raw},+}=4\cdot6=24,\qquad
N_{\mathrm{raw},-}=4\cdot6=24,\qquad
N_{\mathrm{raw}}=48.
$$

Every row has

$$
c_V=\frac{s\,h}{512},
$$

$$
c_u=\frac{s\,h(\sqrt2g)^3}{512}
=\frac{s\sqrt2g}{256},
\qquad
s\in\{+1,-1\}.
$$

The JSON ledger records all \(48\) tuples

$$
(\text{chirality},p,q,r,s,X,Y,Z,c_V,c_u,K).
$$

## 3. Compact Hessians

The linear canonical field strengths obey

$$
W_c^{(1)}=-\frac{\sqrt2}{8}\bar D^2Du,\qquad
\widetilde W_c^{(1)}=-\frac{\sqrt2}{8}D^2\bar Du,
$$

$$
\bar D^2Du=-4\sqrt2\,W_c^{(1)},\qquad
D^2\bar Du=-4\sqrt2\,\widetilde W_c^{(1)}.
$$

For each cross-term group,

$$
\left(\frac{\sqrt2g}{256}\right)(-4\sqrt2)(-4)
=\frac g8.
$$

Hence

$$
\begin{aligned}
S_{E,+}^{(3)}
&=-\frac g8\int d^8z\,W_c^a[D_au,u]
-\frac g8\int d^8z\,W_c^a[D_au,u]\\
&=-\frac g4\int d^8z\,W_c^a[D_au,u],
\end{aligned}
$$

$$
\begin{aligned}
S_{E,-}^{(3)}
&=+\frac g8\int d^8z\,\widetilde W_{c\dot a}
[\bar D^{\dot a}u,u]
+\frac g8\int d^8z\,\widetilde W_{c\dot a}
[\bar D^{\dot a}u,u]\\
&=+\frac g4\int d^8z\,\widetilde W_{c\dot a}
[\bar D^{\dot a}u,u].
\end{aligned}
$$

Using

$$
[D_au,u]^B=i\,c_{XY}{}^B(D_au^X)u^Y,
$$

$$
\frac{\delta^2[D_au,u]^B}{\delta u^U\delta u^C}
=i\,c_{UC}{}^B(D_{Ua}-D_{Ca}),
$$

gives

$$
\boxed{
H_W^{UC}
=+\frac{ig}{4}c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}).}
$$

$$
\boxed{
H_{\widetilde W}^{UC}
=-\frac{ig}{4}c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).}
$$

Since \(\tau_E=-1/\hbar\),

$$
\boxed{
\mathfrak V_W
=-\frac{ig}{4\hbar}c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),}
$$

$$
\boxed{
\mathfrak V_{\widetilde W}
=+\frac{ig}{4\hbar}c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).}
$$

## 4. The two exact counts equal to \(72\)

The structural census gives

$$
N_{AA,TGG}=6\cdot6=36,\qquad
N_{AA,TGG}^{\mathrm{marked}}=2\cdot36=72.
$$

Refining by two action orderings gives

$$
N_{(+,-)}+N_{(-,+)}=36+36=72.
$$

But

$$
\frac1{2!}
\left(S_{+,3}S_{-,3}+S_{-,3}S_{+,3}\right)
=S_{+,3}S_{-,3},
$$

and

$$
\begin{aligned}
\sum_{\rho=1}^{6}\sum_{\sigma=1}^{6}
V_{+,\rho}V_{-,\sigma}
&=
\left(\sum_{\rho=1}^{6}V_{+,\rho}\right)
\left(\sum_{\sigma=1}^{6}V_{-,\sigma}\right)\\
&=H_WH_{\widetilde W}.
\end{aligned}
$$

Therefore

$$
\boxed{
w_{\mathrm{route\ after\ Hessian}}
=w_{\mathrm{mark\ after\ occurrence\ sum}}
=1,}
$$

$$
\boxed{\texttt{NO_ROUTE_COUNT_MULTIPLIER}.}
$$

## 5. Corrected \(D\)-algebra

Use

$$
r_i=
\begin{pmatrix}
a_i&b_i\\
c_i&d_i
\end{pmatrix},
\qquad
\det r_i=a_id_i-b_ic_i=-\bar r_i^2.
$$

For external lower \(W_+\),

$$
W^\gamma D_\gamma\big|_{W_+}
=W^-D_-
=-W_+D_-.
$$

The wrong \(D_+\) reflected control is zero in all eight rows.

For direct \(DA\),

$$
\mathcal S_{DA,01}
=b_2\bar r_0^2(1,-1,-1,-1),
$$

$$
\mathcal S_{DA,02}
=b_0\bar r_2^2(-1,1,-1,-1).
$$

Define

$$
W_{02}:=a_0b_2-b_0a_2,
$$

$$
X:=a_0b_2d_1-a_2b_0d_2-b_0b_2c_1+b_0b_2c_2,
$$

$$
Y:=a_2d_1-a_2d_2-b_2c_1+b_2c_2.
$$

The direct longitudinal rows are

$$
\begin{aligned}
\mathcal L_{DA,01}={}&\bigl(
X,\,
-d_1W_{02},\\
&-a_0b_2d_0+a_2b_0d_0-a_2b_0d_1+a_2b_0d_2
+b_0b_2c_1-b_0b_2c_2,\,
-d_0W_{02}
\bigr),
\end{aligned}
$$

$$
\mathcal L_{DA,02}=(0,-b_0Y,0,+b_0Y).
$$

The independently replayed reflected \(AD\) rows are

$$
\mathcal S_{AD,01}
=b_2\bar r_0^2(1,1,1,-1),
$$

$$
\mathcal S_{AD,02}
=b_0\bar r_2^2(1,1,-1,1),
$$

$$
\mathcal L_{AD,01}=(0,0,0,0),
$$

$$
\mathcal L_{AD,02}=(-X,-X,+X,-X).
$$

Every row satisfies

$$
\mathcal G_{\mathrm{full}}^{m,j}
=\mathcal S^{m,j}+\mathcal L^{m,j}.
$$

## 6. Occurrence-tagged Schwinger contact

Write

$$
\mathcal S^{m,j}
=\alpha_{m,j}k_{m,j}\bar r_{e(m)}^2,
\qquad
e(01)=0,
\qquad
e(02)=2.
$$

At the same functional occurrence,

$$
0=
\int\mathcal Du\,
\frac{\delta}{\delta u_{e(m)}}
\left(
\mathcal R_{m,j}[u]e^{-S_0[u]/\hbar}
\right).
$$

Thus

$$
\boxed{
\mathcal C_d^{m,j}
=-\mathcal L^{m,j}
-\alpha_{m,j}k_{m,j}r_{e(m),d}^2.}
$$

Row by row,

$$
\begin{aligned}
\mathcal S^{m,j}+\mathcal L^{m,j}+\mathcal C_d^{m,j}
&=\alpha_{m,j}k_{m,j}
\left(\bar r_{e(m)}^2-r_{e(m),d}^2\right)\\
&=\alpha_{m,j}k_{m,j}\mu_\ell^2.
\end{aligned}
$$

No decomposition of \(\mathcal L^{m,j}\) among \(e_0,e_1,e_2\) is used. The exact coefficient sums are

$$
\sum_j\alpha_{DA,01,j}k_{DA,01,j}=-2b_2,\qquad
\sum_j\alpha_{DA,02,j}k_{DA,02,j}=-2b_0,
$$

$$
\sum_j\alpha_{AD,01,j}k_{AD,01,j}=+2b_2,\qquad
\sum_j\alpha_{AD,02,j}k_{AD,02,j}=+2b_0.
$$

## 7. Rank-one moments

For direct \(DA\), let \(p\) be the \(A\)-momentum and \(q\) the \(D\)-momentum:

$$
r_0=\ell,\qquad
r_1=\ell+q,\qquad
r_2=\ell+p+q.
$$

With

$$
L=\ell+yq+z(p+q),
$$

$$
2\int_{\Sigma_2}1=1,\qquad
2\int_{\Sigma_2}y
=2\int_{\Sigma_2}z
=\frac13,
$$

one gets

$$
\langle r_0\rangle=-\frac{p+2q}{3},\qquad
\langle r_2\rangle=+\frac{2p+q}{3},
$$

$$
-2\langle r_2\rangle-2\langle r_0\rangle
=-\frac23(p-q).
$$

For reflected \(AD\),

$$
q_{\mathrm{engine}}=p,\qquad
p_{\mathrm{engine}}=q,
$$

and the independent replay gives

$$
+2\langle r_2\rangle_{\mathrm{refl}}
+2\langle r_0\rangle_{\mathrm{refl}}
=-\frac23(p-q).
$$

The common factor is

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
=-\frac{\hbar g^2}{16}.
$$

Therefore

$$
\left(-\frac{\hbar g^2}{16}\right)
\left(-\frac23\right)
\left(\frac1{32\pi^2}\right)
=\frac{\lambda_1}{48},
$$

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

## 8. Target-blind ordered result

Define

$$
DA_p:=D_{\dot\alpha}^D(q)p_+{}^{\dot\alpha}A^E(p),\qquad
DA_q:=D_{\dot\alpha}^D(q)q_+{}^{\dot\alpha}A^E(p),
$$

$$
AD_p:=p_{+\dot\alpha}A^D(p)D^{E\dot\alpha}(q),\qquad
AD_q:=q_{+\dot\alpha}A^D(p)D^{E\dot\alpha}(q).
$$

Since

$$
\epsilon^{\dot1\dot2}=+1,\qquad
p_{\dot\alpha}A\,D^{\dot\alpha}
=-D_{\dot\alpha}p^{\dot\alpha}A,
$$

the exact extended vector is

$$
\boxed{
(c_{DA,p},c_{DA,q},c_{AD,p},c_{AD,q})
=
\left(
\frac1{48},
-\frac1{48},
-\frac1{48},
\frac1{48}
\right).}
$$

Equivalently,

$$
\boxed{
\Gamma_{AA,g}^{(1)}
=\frac{\lambda_1}{48}\mathbb F^{AB}{}_{DE}
\left[(DA_p-DA_q)-(AD_p-AD_q)\right].}
$$

Before an explicit EOM, total-derivative, or source-derivative quotient,

$$
DA_q,\qquad AD_q
$$

are independent typed structures. Hence

$$
\boxed{
(c_{DA},c_{AD})
=(\mathrm{UNDEFINED},\mathrm{UNDEFINED}).}
$$

Verification:

    python scripts/step5_aa_gauge_raw_convolution_hessian_exact_audit.py --check
