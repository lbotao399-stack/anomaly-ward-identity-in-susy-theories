# Step-5 local operator basis and one-loop mixing audit

Authority: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.  
本 audit 未读取 Step-5 contract、其他 Step-5 engine 或 HT target。

## 1. Typed derivative-slot chain

$$
d_{\dot a}:=D_{\dot a},\qquad
c_{r\dot a}:=P_{\dot a}C_r,\qquad
b_{r\dot a}:=P_{\dot a}B_r,\qquad
a_{\dot a}:=P_{\dot a}A.
$$

$$
[d,c_r,b_r,a]=\left(\frac32,2,\frac52,3\right),\qquad
(|d|,|c_r|,|b_r|,|a|)=(1,0,1,0).
$$

$$
d,a\in\mathbf1,\qquad b_r\in\mathbf3,\qquad c_r\in\overline{\mathbf3},\qquad
\operatorname{gh}(d,c,b,a)=0.
$$

Step 4C (4C.44)--(4C.47) gives

$$
q_rd_{\dot a}=-ic_{r\dot a},\qquad
q_rc_{s\dot a}=-\frac1{\sqrt2}\varepsilon_{rst}b_{t\dot a},\qquad
q_rb_{s\dot a}=-i\delta_{rs}a_{\dot a},\qquad
q_ra_{\dot a}=0.
$$

The connection term in $q_rP_{\dot a}$ vanishes exactly:

$$
\begin{aligned}
q_r(P_{\dot a}X)-P_{\dot a}(q_rX)
&=\frac1{\sqrt2}(\sigma_E^m)_{+\dot a}
(\sigma_{E,m})_{+\dot b}
(\widetilde\psi_r^{\dot b}\times X)\\
&=0,
\end{aligned}
$$

because $(\sigma_E^m)_{+\dot a}(\sigma_{E,m})_{+\dot b}=0$.

Use the exact rational chain basis

$$
e_\varnothing=i d,\quad e_r=c_r,\quad
e_{12}=-\frac{b_3}{\sqrt2},\quad
e_{13}=+\frac{b_2}{\sqrt2},\quad
e_{23}=-\frac{b_1}{\sqrt2},\quad
e_{123}=+\frac{i}{\sqrt2}a.
$$

Then $q_re_S=e_r\wedge e_S$.

## 2. Ordered open-color space and exact RREF

$$
\mathcal O_{XY}^{DE}:=X_{\dot a}^D Y^{E\dot a},\qquad
(D,E)\text{ remains ordered}.
$$

$$
\mathcal V=\operatorname{Span}\{e_S^D\otimes e_T^E:S,T\subset\{1,2,3\}\},\qquad
\dim\mathcal V=8^2=64.
$$

For $n=|S|+|T|$, $[\mathcal V^n]=3+n/2$ and $|\mathcal V^n|=n\bmod2$.  The stacked matrix is

$$
Q^{(n)}=(q_1,q_2,q_3):\mathcal V^n\longrightarrow(\mathcal V^{n+1})^{\oplus3}.
$$

| $n$ | $\dim\mathcal V^n$ | rows | rank $Q^{(n)}$ | $\dim\bigcap_r\ker q_r$ |
|---:|---:|---:|---:|---:|
| 0 | 1 | 18 | 1 | 0 |
| 1 | 6 | 45 | 6 | 0 |
| 2 | 15 | 60 | 15 | 0 |
| 3 | 20 | 45 | 19 | 1 |
| 4 | 15 | 18 | 12 | 3 |
| 5 | 6 | 3 | 3 | 3 |
| 6 | 1 | 0 | 0 | 1 |

Thus the dimension-$9/2$, odd, ghost-zero block has

$$
\dim\mathcal V^3=20,\qquad
\operatorname{rank}Q^{(3)}=19,\qquad
\dim\bigcap_{r=1}^3\ker q_r=1.
$$

Its twenty physical monomials are

$$
\{\langle d,a\rangle,\ \langle a,d\rangle,\
\langle c_r,b_s\rangle,\ \langle b_r,c_s\rangle:
r,s=1,2,3\}.
$$

The exact $SU(3)$ decomposition is

$$
\mathcal V^3=(\mathbf1\oplus\mathbf1)
\oplus(\overline{\mathbf3}\otimes\mathbf3)
\oplus(\mathbf3\otimes\overline{\mathbf3})
=4\,\mathbf1\oplus2\,\mathbf8.
$$

RREF gives the unique joint cocycle

$$
\boxed{
\mathscr Z^{DE}
=\langle d^D,a^E\rangle-\langle a^D,d^E\rangle
+\sum_{r=1}^3\left(
\langle b_r^D,c_r^E\rangle-\langle c_r^D,b_r^E\rangle
\right),\qquad q_s\mathscr Z^{DE}=0.}
$$

## 3. Complete degree-four counterterm precursor

The even dimension-four precursor space is

$$
\mathcal V^2=\operatorname{Span}\{
\langle d,b_r\rangle,\ \langle b_r,d\rangle,\
\langle c_r,c_s\rangle:r,s=1,2,3\},\qquad
\dim\mathcal V^2=15.
$$

$$
\mathcal V^2=\mathbf3\oplus\mathbf3\oplus\mathbf3
\oplus\overline{\mathbf6}.
$$

For

$$
Y_r(\alpha,\beta,\gamma)
=\alpha\langle d,b_r\rangle
+\beta\langle b_r,d\rangle
+\gamma\varepsilon_{rst}\langle c_s,c_t\rangle,
$$

write $\gamma=-i\sqrt2\eta$.  The off-diagonal equations $q_sY_r=0$ for $s\ne r$ have RREF

$$
\operatorname{RREF}
\begin{pmatrix}1&0&-1\\0&1&-1\end{pmatrix}
=\begin{pmatrix}1&0&-1\\0&1&-1\end{pmatrix},
\qquad\alpha=\beta=\eta.
$$

Therefore the covariant triplet is unique:

$$
\boxed{
\mathscr Y_r^{DE}
=\langle d^D,b_r^E\rangle+\langle b_r^D,d^E\rangle
-i\sqrt2\varepsilon_{rst}\langle c_s^D,c_t^E\rangle,
\qquad q_s\mathscr Y_r^{DE}=i\delta_{sr}\mathscr Z^{DE}.}
$$

For the explicitly declared Koszul quotient

$$
H_{\rm joint}^n
:=\frac{\bigcap_r\ker(q_r:\mathcal V^n\to\mathcal V^{n+1})}
{\operatorname{im}(q_1q_2q_3:\mathcal V^{n-3}\to\mathcal V^n)},
$$

the kernel and image dimensions for $n=3,4,5,6$ are respectively

$$
(1,3,3,1)=(1,3,3,1),\qquad H_{\rm joint}^n=0.
$$

This equality applies only to the 64-dimensional derivative-slot module.  It does not perform the BV/EOM/total-derivative/DRED quotient.

## 4. Required enlarged local space

At the same dimension, parity, ghost number, $SU(3)$ type and ordered color-source type, the subtraction space must be

$$
\mathcal V_{\rm loc}
=\mathcal V_{\rm phys}
\oplus\mathcal N_{\rm EOM}
\oplus\mathcal N_{\rm BRST}
\oplus\mathcal N_{\rm TD}
\oplus\mathcal V_{\rm ev}.
$$

With the Step-4C Euler operators, the exact module forms are

$$
\begin{aligned}
\mathcal N_{\rm EOM}
&=\operatorname{Span}\{
\mathscr A_E^mR_m,\ \mathscr P_{E,\mathcal I\mathcal J}R^{\mathcal I\mathcal J},\
\widetilde{\mathscr P}_E^{\mathcal I\mathcal J}\widetilde R_{\mathcal I\mathcal J},\
\mathcal E_{E,a\mathcal I}S^{a\mathcal I},\
\widetilde{\mathcal E}_{E,\dot a}^{\mathcal I}
\widetilde S_{\mathcal I}^{\dot a}\}_{\rm typed},\\
\mathcal N_{\rm BRST}
&=\{\mathbf s_EK:[K]=9/2,\ |K|=0,\operatorname{gh}K=-1\}_{\rm typed},\\
\mathcal N_{\rm TD}
&=\{\partial_mJ^m:[J^m]=7/2,\ |J^m|=1,\operatorname{gh}J^m=0\}_{\rm typed},\\
\mathcal V_{\rm ev}
&=\{E_u:E_u|_{\breve\delta=0}=0,\ [E_u]=9/2,\ |E_u|=1,\operatorname{gh}E_u=0\}_{\rm typed}.
\end{aligned}
$$

The locked inputs do not select the multipliers, currents, open-color BV source, or the $\breve\delta$ operator grammar.  Hence these four modules have no Project-locked finite basis yet.

## 5. One-loop evanescent mixing

For one physical cocycle $O=\mathscr Z$ and one same-typed DRED precursor $E$, the most general one-loop subtraction is

$$
\begin{pmatrix}O^0\\E^0\end{pmatrix}
=\left[\mathbf1+\frac{\hbar g^2}{16\pi^2\epsilon}
\begin{pmatrix}z_{OO}&z_{OE}\\z_{EO}&z_{EE}\end{pmatrix}\right]
\begin{pmatrix}O^R\\E^R\end{pmatrix}.
$$

Here the trace-evanescent insertion is $E_{\rm tr}:=(4-d)E$; $E$ is not an already-projected genuine $E_{\breve u}\in\ker\pi_4$.

Since $d=4-2\epsilon$ exactly,

$$
\begin{aligned}
(4-d)E^0
&=2\epsilon E^R
+\frac{2\epsilon\hbar g^2}{16\pi^2\epsilon}
(z_{EO}O^R+z_{EE}E^R)\\
&=2\epsilon E^R
+\frac{\hbar g^2}{8\pi^2}
(z_{EO}O^R+z_{EE}E^R).
\end{aligned}
$$

The map $E\mapsto zO$ with arbitrary scalar $z$ commutes with all three $q_r$, preserves dimension/parity/$SU(3)$/ordered color type, and is BRST-covariant.  Therefore Wess--Zumino and classical Slavnov identities do not impose $z_{EO}=0$.

The locked foundations contain no quantum $\mathcal N=4$ finiteness theorem.  A vanishing action counterterm would still not evaluate the pole of this composite insertion.

$$
\boxed{\texttt{BLOCKED\_ONE\_LOOP\_COMPOSITE\_Z\_MATRIX}:\quad
Z_{\rm ev\to phys}^{(1)}\text{ cannot be set to zero from the allowed identities.}}
$$

## 6. Minimal DRED/MS insertion block

Fix the proposal

$$
d=4-2\epsilon,\qquad
\delta_4^{mn}=\widehat\delta^{mn}+\breve\delta^{mn},\qquad
\widehat\delta^m{}_m=d,\qquad
\breve\delta^m{}_m=2\epsilon,
$$

with four-dimensional spin algebra and MS subtraction of every $1/\epsilon$ pole and no finite term.

For a straight adjoint link, take

$$
S_J=\int d^4x\,d^4y\ J_{DE}(x,y)\mathcal O^{DE}(x,y),
$$

$$
\mathcal O^{DE}(x,y)
=H_X^D(x)\,[U_{\rm ad}(x,y)]^E{}_F\,H_Y^F(y),
$$

$$
\mathbf sJ_{DE}
=-J_{FE}\rho(\mathfrak c(x))^F{}_D
-J_{DF}\rho(\mathfrak c(x))^F{}_E.
$$

The allowed bare rows are

$$
\mathbf O^0
=\left(\mathscr Z^0,\ E_1^0,\ldots,\ E_{\epsilon}^0,\ E_{\breve1}^0,\ldots,
\mathcal N_{\rm EOM}^0,\mathcal N_{\rm BRST}^0,\mathcal N_{\rm TD}^0\right)^T,
$$

$$
E_{{\rm tr},u}:=(4-d)E_u=2\epsilon E_u,\qquad
E_{\epsilon}:=(4-d)\mathscr Z=2\epsilon\mathscr Z,\qquad
E_{\breve u}\in\ker\pi_4,\qquad
\pi_4(E_{\breve u})=E_{\breve u}|_{\breve\delta=0}=0.
$$

$E_u$ is the pole-renormalized precursor used in Section 5.  $E_{\epsilon}$ is an exact trivial trace-evanescent row; neither it nor the generic $E_{{\rm tr},u}$ is a basis for the genuine $E_{\breve u}$ tensors.

Let

$$
\mathbb K:=S_\Psi^{(2)}|_{\text{zero background}},\qquad
G:=\mathbb K^{-1},
$$

$$
V_{[n]}:=\left(S_\Psi^{(2)}-\mathbb K\right)_{[n]},\qquad
I_{E,[n]}:=\left(JE\right)^{(2)}_{[n]}.
$$

The one-loop term linear in $J$ and quadratic in backgrounds is exactly

$$
\boxed{
\Gamma_{J,E,[2]}^{(1)}
=\frac{\hbar}{2}\operatorname{STr}\left[
GI_{E,[2]}-GV_{[1]}GI_{E,[1]}-GV_{[2]}GI_{E,[0]}
+GV_{[1]}GV_{[1]}GI_{E,[0]}\right].}
$$

This generates four 1PI classes:

1. $+\operatorname{STr}[GI_{E,[2]}]$: insertion/contact/link/endpoint tadpole;
2. $-\operatorname{STr}[GV_{[1]}GI_{E,[1]}]$: mixed action--insertion bubble;
3. $-\operatorname{STr}[GV_{[2]}GI_{E,[0]}]$: quartic action, gauge-fixing, or ghost contact bubble;
4. $+\operatorname{STr}[GV_{[1]}GV_{[1]}GI_{E,[0]}]$: triangle, both orientations and all graded field blocks.

The separate tree class is $J\,\delta E^{(1)}$ and contains operator, elementary-field, coupling, EOM, BRST-exact, and total-derivative counterterms.

After the direct-sum basis and $\Pi_{\mathscr Z}$ have been locked, define the complete pole projection by

$$
\Pi_{\mathscr Z}\operatorname*{Res}_{\epsilon=0}
\Gamma_{J,E,[2]}^{(1)}
=\frac{\hbar g^2}{16\pi^2}r_{E\mathscr Z}
\int J_{DE}\mathscr Z^{DE}.
$$

With the bare-to-renormalized convention of Section 5, MS cancellation gives

$$
\boxed{z_{EO}=-r_{E\mathscr Z}.}
$$

Therefore $z_{EO}=0$ is valid exactly when the sum of all four 1PI classes has $r_{E\mathscr Z}=0$.  If $r_{E\mathscr Z}\ne0$, declaring $z_{EO}=0$ leaves an uncancelled $1/\epsilon$ pole.

A non-MS counterterm built from $\mathscr Y_r$ changes the finite Ward representative because

$$
q_s\mathscr Y_r=i\delta_{sr}\mathscr Z.
$$

Consequently it also changes the operator dictionary that must be compared in another scheme.  Fixing that finite term from external-target agreement is not an independent Project derivation.

The locked inputs do not define $E_{\breve u}$, $\mathbb K^{-1}$ on a selected DRED gauge slice, or the source Hessians $I_{E,[n]}$.  Hence $r_{E\mathscr Z}$ and $z_{EO}$ remain unevaluated.

## 7. P0 blockers

- `BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION`: A locked contragredient source J_DE, its antifield/source slots, and its subtraction conditions.
- `BLOCKED_DRED_EVANESCENT_OPERATOR_BASIS`: A locked DRED continuation of every Step-5 field, composite insertion, EOM, BRST differential, and local projection, including the breve-index tensor grammar.
- `BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX`: The bare source functional, endpoint/link/contact vertices, all one-loop insertion graphs, and a declared subtraction scheme.
- `BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT`: The Step-5 source representation and the admissible multiplier/current grammar for the Euler operators (4C.68)-(4C.68a).

## 8. Machine checks

- `T01_RESIDUAL_Q_NILPOTENCY_64`: PASS
- `T02_RESIDUAL_Q_ANTICOMMUTATIVITY_64`: PASS
- `T03_HOMOGENEOUS_DIMENSIONS`: PASS
- `T04_DEGREE_THREE_RREF`: PASS
- `T05_PHYSICAL_COCYCLE_VECTOR`: PASS
- `T06_KOSZUL_JOINT_QUOTIENT`: PASS
- `T07_UNIQUE_TRIPLET_PRIMITIVE_RREF`: PASS
- `T08_PRIMITIVE_COVARIANCE_9_CASES`: PASS
- `T09_COCYCLE_SIGN_MUTATION_DETECTED`: PASS
- `T10_FINITE_EVANESCENT_FACTOR`: PASS
- `T11_ONE_LOOP_RESOLVENT_GRAPH_COEFFICIENTS`: PASS

Deterministic digest: `e4faa19082459a740b15b257e26a50adfc4baa530cae50bb2c9181dd5c63351b`
