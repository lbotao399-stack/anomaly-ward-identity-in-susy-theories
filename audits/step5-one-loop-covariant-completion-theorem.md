# Step 5A one-loop covariant-completion theorem

Status: `CONDITIONAL_PHYSICAL4D_FAIL_EXPLICIT_FULL_DRED_KERNEL`

## 1. One-loop rooted functional

Let

$$
H_J[\mathcal B]
=H_{\mathcal B}+J I_{\mathcal B},
\qquad
G_{\mathcal B}=H_{\mathcal B}^{-1},
\qquad
|J|=|I_{\mathcal B}|=1.
$$

In the Step-5A reference-flat measure,

$$
\begin{aligned}
\Gamma_{\mathscr I,{\rm root,DRED}}^{(1),{\rm reg}}[\mathcal B]
&=
\left.
\frac{\vec\delta}{\delta J}
\frac12\operatorname{STr}_{\mathrm{DRED}}\log H_J[\mathcal B]
\right|_{J=0}\\
&=\frac12\operatorname{STr}_{\mathrm{DRED}}
\left(G_{\mathcal B}I_{\mathcal B}\right).
\end{aligned}
$$

Write

$$
H_{\mathcal B}=H_0+\sum_{r\ge1}H_r,
\qquad
I_{\mathcal B}=\sum_{s\ge0}I_s,
\qquad
G_0=H_0^{-1}.
$$

Then

$$
G_{\mathcal B}
=G_0\sum_{k=0}^{\infty}
\left(-H_+G_0\right)^k,
\qquad
H_+=\sum_{r\ge1}H_r,
$$

and the exact background-order-
\(n\) coefficient is

$$
\boxed{
\Gamma_{\mathscr I,{\rm root,DRED},n}^{(1),{\rm reg}}
=\frac12
\sum_{\substack{k\ge0,\ s\ge0,\ r_j\ge1\\
s+r_1+\cdots+r_k=n}}
(-1)^k
\operatorname{STr}_{\mathrm{DRED}}
\left[
I_sG_0H_{r_1}G_0\cdots H_{r_k}G_0
\right].}
$$

$$
\Gamma_{\mathscr I,{\rm ren,DRED},n}^{(1),{\rm reg}}
:=\Gamma_{\mathscr I,{\rm root,DRED},n}^{(1),{\rm reg}}
+\mathrm{CT}_n^{\rm reg}.
$$

The unlabeled and polarized family counts are

$$
N_{mathrm{family}}(n)=2^n,
$$

$$
N_{\mathrm{pol}}(n)
=\sum_{s=0}^n\binom ns
\sum_{k=0}^{n-s}k!\,S(n-s,k),
$$

$$
\begin{array}{c|cc}
n&N_{\mathrm{family}}(n)&N_{\mathrm{pol}}(n)\\ \hline
2&4&6\\
3&8&26\\
4&16&150
\end{array}.
$$

## 2. Complete quadratic seed

For labeled backgrounds \(\mathcal V_1,\mathcal V_2\),

$$
\boxed{
\begin{aligned}
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=\frac12\operatorname{STr}_{\mathrm{DRED}}\Big[&
+I_0G_0H_1[\mathcal V_1]G_0H_1[\mathcal V_2]G_0\\
&+I_0G_0H_1[\mathcal V_2]G_0H_1[\mathcal V_1]G_0\\
&-I_0G_0H_2[\mathcal V_1,\mathcal V_2]G_0\\
&-I_1[\mathcal V_1]G_0H_1[\mathcal V_2]G_0\\
&-I_1[\mathcal V_2]G_0H_1[\mathcal V_1]G_0\\
&+I_2[\mathcal V_1,\mathcal V_2]G_0
\Big]
+\mathrm{CT}_2^{\rm reg}.
\end{aligned}}
$$

$$
Q_{\triangle}^{\rm bare}
:=\frac12\operatorname{STr}_{\rm DRED}\!\left[
I_0G_0H_1[\mathcal V_1]G_0H_1[\mathcal V_2]G_0
+I_0G_0H_1[\mathcal V_2]G_0H_1[\mathcal V_1]G_0
\right],
$$

$$
\begin{aligned}
Q_{\rm Hess}^{(2)}
:={}&\frac12\operatorname{STr}_{\rm DRED}\!\Big[
-I_0G_0H_2[\mathcal V_1,\mathcal V_2]G_0\\
&-I_1[\mathcal V_1]G_0H_1[\mathcal V_2]G_0
-I_1[\mathcal V_2]G_0H_1[\mathcal V_1]G_0
+I_2[\mathcal V_1,\mathcal V_2]G_0\Big].
\end{aligned}
$$

Equivalently, before any propagator-collapse regrouping,

$$
\boxed{
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm bare}+Q_{\rm Hess}^{(2)}+\mathrm{CT}_2^{\rm reg}.}
$$

$$
Q_{\rm contact,Hess}^{(2)}
:=Q_{\rm Hess}^{(2)}+\mathrm{CT}_2^{\rm reg}.
$$

If a coefficient-valued cut map is constructed, then and only then

$$
Q_{\triangle}^{\rm bare}
=Q_{\triangle}^{\rm irr}+Q_{\triangle}^{\rm cut},
\qquad
Q_{\triangle}^{\rm cut}:=\mathcal R_{\rm cut}Q_{\triangle}^{\rm bare},
$$

$$
\boxed{
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm irr}
+\left(Q_{\triangle}^{\rm cut}+Q_{\rm Hess}^{(2)}+\mathrm{CT}_2^{\rm reg}\right),
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED}.}
$$

An isolated triangle is not the datum entering the completion theorem.

## 3. Background Ward identity

Let the finite background action on the Gaussian carrier be

$$
Q'=R Q.
$$

The source-extended quadratic functional gives

$$
H_{\mathcal B'}=R H_{\mathcal B}R^{-1},
\qquad
G_{\mathcal B'}=R G_{\mathcal B}R^{-1},
\qquad
I_{\mathcal B'}=R I_{\mathcal B}R^{-1}.
$$

Hence

$$
\begin{aligned}
\Gamma_{\mathscr I}^{(1)}[\mathcal B']
&=\frac12\operatorname{STr}_{\mathrm{DRED}}
\left(RG_{\mathcal B}I_{\mathcal B}R^{-1}\right)\\
&=\frac12\operatorname{STr}_{\mathrm{DRED}}
\left(G_{\mathcal B}I_{\mathcal B}\right)
=\Gamma_{\mathscr I}^{(1)}[\mathcal B].
\end{aligned}
$$

The regulated cyclic step follows from

$$
\operatorname{Tr}_{\mathrm{Adj}}(\operatorname{ad}_{\eta})
=\eta^C\kappa^{AB}c_{CAB}=0,
$$

$$
\int_kF(k+a)
=\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}F(k+a)
=\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}F(\ell),
\qquad
\ell=k+a,
$$

$$
\det\!\left(\frac{\partial\ell}{\partial k}\right)=1,
\qquad
\operatorname{STr}_{\mathrm{DRED}}[R,\mathcal M]=0.
$$

Therefore every triangle, box, pentagon, seagull, and contact term belongs to
one Taylor expansion of the same background-covariant rooted functional.

## 4. Physical-$4d$ conditional completion

Let

$$
\mathfrak H_{\mathrm{pg}}^{4d}
=\left\{
[\mathscr O]:
[\mathscr O]=\frac92,
\ (j_L,j_R)=\left(\frac32,0\right),
\ |\mathscr O|=1,
\ r_{\mathrm P}(\mathscr O)=-1,
\ \mathscr O\in\operatorname{Sym}^2(\operatorname{Adj})
\right\}
$$

be the physical-$4d$, fixed-vector-frame, background-covariant pure-gauge
local quotient, and define

$$
\ell_2[\mathscr O]
=\left.
\frac12
\frac{\vec\delta}{\delta\mathcal V_1}
\frac{\vec\delta}{\delta\mathcal V_2}
\mathscr O[\mathcal V]
\right|_{\mathcal V=0}.
$$

$$
\mathscr A_{{\rm loc,DRED}}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{\rm DRED}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}},
\qquad
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}}.
$$

$$
q_{4d}\operatorname{Loc}_{\rm UV}^{\rm DRED}
=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\qquad\texttt{NOT\_PROVED}.
$$

Let \(P\) be the registered operator-presentation space.  Let

$$
C:P\longrightarrow Z,
\qquad
B:U\longrightarrow P,
\qquad
L_{\ell_2}:P\longrightarrow T_{2,{\rm reg}}^{4d},
$$

denote respectively the closure, boundary, and quadratic-jet matrices, and
let \(B_2\subset T_{2,{\rm reg}}^{4d}\) be the quadratic boundary subspace.

$$
T_{2,{\rm reg}}^{4d,\epsilon}
:=T_{2,{\rm reg}}^{4d}\otimes_{\mathbb Q}\mathbb Q(\epsilon),
\qquad
\overline T_{2,{\rm reg}}^{4d,\epsilon}
:=\left(T_{2,{\rm reg}}^{4d}/B_2\right)
\otimes_{\mathbb Q}\mathbb Q(\epsilon),
$$

$$
\rho_2^\epsilon:T_{2,{\rm reg}}^{4d,\epsilon}
\longrightarrow\overline T_{2,{\rm reg}}^{4d,\epsilon}.
$$

The induced map is

$$
\bar\ell_2^{4d}:
\ker C/\operatorname{im}B
\longrightarrow\overline T_{2,{\rm reg}}^{4d,\epsilon}.
$$

Assume the exact matrix identity

$$
\boxed{
\{v\in\ker C:L_{\ell_2}v\in B_2\}
=\operatorname{im}B.}
$$

Equivalently,

$$
\ker\bar\ell_2^{4d}=0.
$$

Choose \(0\ne[\mathscr O_\star]\in\mathfrak H_{\mathrm{pg}}^{4d}\), set

$$
\bar t_\star:=\bar\ell_2^{4d}[\mathscr O_\star]\ne0,
$$

$$
\overline T_{2,{\rm reg}}^{4d,\epsilon}
=\mathbb Q(\epsilon)\bar t_\star
\oplus\overline T_{2,\perp}^{4d,\epsilon},
\qquad
\bar\pi_\star^{4d}:
\overline T_{2,{\rm reg}}^{4d,\epsilon}\longrightarrow\mathbb Q(\epsilon),
\qquad
\bar\pi_\star^{4d}(\alpha\bar t_\star+\bar t_\perp)=\alpha,
$$

$$
C_{2,{\rm reg}}
:=\bar\pi_\star^{4d}\!\left(
\bar\ell_2^{4d}[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}]
\right).
$$

Suppose the complete quadratic calculation gives

$$
\bar\ell_2^{4d}\!\left[
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}\right]
=C_{2,{\rm reg}}\,\bar\ell_2^{4d}[\mathscr O_\star].
$$

Then

$$
\bar\ell_2^{4d}\!\left[
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
-C_{2,{\rm reg}}\mathscr O_\star
\right]=0,
$$

$$
\boxed{
\left[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}\right]
=C_{2,{\rm reg}}[\mathscr O_\star]
\quad\text{in }\mathfrak H_{\mathrm{pg}}^{4d}.}
$$

The current indexed event matrix does not establish the premise.  It has

$$
M_{1\to2}\in\operatorname{Mat}_{126\times4866}(\mathbb Q),
$$

but the $4866$ columns are ordered-word/event coordinates.  They are not
independent $N=1$ generators.  The missing parent incidence is

$$
C_1:\mathbb Q^{20}\longrightarrow\mathbb Q^{4866}.
$$

In one fixed parent fiber,

$$
(q_{\rm PBW}M_{1\to2})_0=-2,
\qquad
(q_{\rm PBW}M_{1\to2})_6=0.
$$

Therefore the event map does not factor through the naive skeleton/copy map.
The exact present boundary is

$$
\boxed{
\operatorname{status}\!\left(\ker\bar\ell_2^{\,4d}=0\right)
=\texttt{FAIL\_CLOSED\_MISSING\_TRUE\_N1\_PARENT\_INCIDENCE}.}
$$

Define

$$
C_{\triangle,{\rm bare,reg}}
:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\triangle}^{\rm bare}\right),
\qquad
C_{{\rm contact,Hess},{\rm reg}}
:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\rm contact,Hess}^{(2)}\right).
$$

Then

$$
C_{2,{\rm reg}}
=C_{\triangle,{\rm bare,reg}}+C_{{\rm contact,Hess},{\rm reg}}.
$$

The equality

$$
C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}
$$

is equivalent to \(C_{{\rm contact,Hess},{\rm reg}}=0\).  It requires the explicit
seagull/contact/collapse and \(\mathrm{CT}_2\) calculation; it does not follow
from covariance.

Only if the missing physical-$4d$ premise is proved, then for every $n\ge3$,

$$
\boxed{
\left[\mathscr A_{{\rm loc},4d,n}^{(1),{\rm reg}}\right]
=C_{2,{\rm reg}}\left[
\left.
\frac1{n!}
\frac{\vec\delta^n\mathscr O_\star}
{\delta\mathcal V_1\cdots\delta\mathcal V_n}
\right|_{\mathcal V=0}\right].}
$$

This is an equality of local quotient classes.  It is not an equality of the
complete nonlocal box, pentagon, or higher one-loop 1PI amplitudes.

## 5. Full-DRED counterexample

Define

$$
\widetilde\delta^{mn}
=\frac\epsilon2\delta_{(4)}^{mn}+\tau^{mn},
\qquad
\delta_{(4)mn}\tau^{mn}=0.
$$

The exact projector algebra gives

$$
\tau_{mn}\tau^{mn}=2\epsilon-\epsilon^2
\notin(\epsilon^2)\mathbb Q[\epsilon].
$$

The raw DRED background-CE module contains

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d},
$$

$$
K^{AB}{}_{C[DE]}
=\delta^A{}_Cc_{DE}{}^B
+\delta^B{}_Cc_{DE}{}^A.
$$

It obeys

$$
\ell_2(\mathscr E)=0,
\qquad
\left.\partial_t^3\mathscr E(t\mathcal B)\right|_{t=0}\ne0,
\qquad
q_{4d}(\mathscr E)=0.
$$

Hence

$$
\boxed{
\ker\!\left(\ell_2\big|_{\rm DRED,raw}^{\rm CE}\right)\ne0.}
$$

At cubic background order,

$$
N_{\rm family}(3)=8,
\qquad
N_{\rm pol}(3)=26.
$$

Current kernels cover $24$ polarized rows.  The two missing rows are

$$
I_0H_3,
\qquad
I_3,
$$

because $[V^5]S_{\rm gauge}$ and the valence-five insertion $I_{(5)}$ are not
in the Project grammar.  Therefore

$$
C_{\mathscr E,{\rm reg}}
:=\operatorname{Coeff}_{\mathscr E}
\operatorname{Loc}_{\rm UV}^{\rm DRED}
\Gamma_{\mathscr I,{\rm ren,DRED},3}^{(1),{\rm reg}},
\qquad
\operatorname{status}\!\left(C_{\mathscr E,{\rm reg}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
$$

## 6. Prepotential expansion

For

$$
\Gamma_a
=e^{-\mathcal V}D_ae^{\mathcal V}
=\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}{n!}
\operatorname{ad}_{\mathcal V}^{n-1}(D_a\mathcal V),
$$

$$
\mathcal W_a=-\frac18\bar D^2\Gamma_a,
$$

the covariant answer has infinitely many prepotential Taylor coefficients.
Thus triangle, box, and pentagon are the first three rooted cycle lengths;
they do not terminate the completion.

## 7. Chiral/vector frame boundary

For covariant operators,

$$
\mathcal O_{\mathsf C}
=\mathcal B^{-1}\mathcal O_{\mathsf V}\mathcal B.
$$

For a quantum-coordinate map

$$
\zeta_{\mathsf V}
=\mathbb T_{\rm q}(\overline Q_{\mathsf C},\zeta_{\mathsf C}),
\qquad
J_{\rm q}
=\left.
\frac{\vec\partial\zeta_{\mathsf V}}
{\partial\zeta_{\mathsf C}}
\right|_{\overline Q_{\mathsf C}},
\qquad
C^\alpha{}_{ij}
=\frac{\vec\partial^2\zeta_{\mathsf V}^{\alpha}}
{\partial\zeta_{\mathsf C}^{i}\partial\zeta_{\mathsf C}^{j}},
$$

$$
E_{\mathsf V,\alpha}
:=\frac{\vec\partial S_{\mathsf V}}
{\partial\zeta_{\mathsf V}^{\alpha}},
\qquad
F_{\mathsf V,\alpha}
:=\frac{\vec\partial\mathscr I_{\mathsf V}}
{\partial\zeta_{\mathsf V}^{\alpha}},
$$

the exact second derivatives are

$$
K_{\mathsf C,ij}
=(J_{\rm q}^{\rm st})_i{}^\alpha
K_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+E_{\mathsf V,\alpha}C^\alpha{}_{ij},
$$

$$
I^{\rm bil}_{\mathsf C,ij}
=(J_{\rm q}^{\rm st})_i{}^\alpha
I^{\rm bil}_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+F_{\mathsf V,\alpha}C^\alpha{}_{ij}.
$$

Therefore pure similarity requires

$$
E_{\mathsf V,\alpha}C^\alpha{}_{ij}=0,
\qquad
F_{\mathsf V,\alpha}C^\alpha{}_{ij}=0.
$$

The fixed vector-frame rooted functional does not invoke this nonlinear
cross-frame coordinate change.  Cross-frame functional equality additionally
requires the density, ghost/nonminimal, regulator, and finite-cycle
pushforwards.

## 8. Acceptance boundary

$$
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\Gamma_{\mathscr I,{\rm root,DRED}}^{(1),{\rm reg}}
=\frac12\operatorname{STr}_{\rm DRED}(GI)
&\texttt{PASS\_REGISTERED}\\
\text{all-order rooted family and signs}&\texttt{PASS}\\
\text{DRED supertrace cyclicity}&\texttt{PASS\_PROJECT\_TEST\_DOMAIN\_ONLY}\\
\text{functional background covariance}&\texttt{PASS\_FUNCTIONAL}\\
\text{vertex-by-vertex Ward replay}&\texttt{OPEN}\\
\text{complete quadratic physical coefficient}&\texttt{OPEN}\\
\ker\bar\ell_2^{\,4d}=0\text{ in the physical pure-gauge quotient}&
\texttt{FAIL\_CLOSED\_MISSING\_C1}\\
\ker\ell_2\text{ in the raw full-DRED CE module}&
\texttt{FAIL\_EXPLICIT\_TAU\_KERNEL}\\
\operatorname{Coeff}_{\mathscr E}\Gamma_{\mathscr I,3}^{(1),\rm pole}&
\texttt{NOT\_COMPUTED\_MISSING\_H3/I3}\\
\text{fixed vector-frame theorem}&
\texttt{NOT BLOCKED BY CROSS-FRAME MAP}\\
\text{chiral--vector nonlinear functional bridge}&\texttt{OPEN}\\
\text{full }\mathcal N=4\text{ matter-class extension}&\texttt{OPEN\_SEPARATE}\\
q_{4d}\operatorname{Loc}_{\rm UV}=\operatorname{Loc}_{\rm UV}q_{4d}
&\texttt{OPEN}\\
\text{nonexceptional UV/IR separation}&\texttt{OPEN}\\
\text{one-loop covariant completion}&\texttt{CONDITIONAL}
\end{array}
$$

No anomaly coefficient is accepted in this theorem file.
