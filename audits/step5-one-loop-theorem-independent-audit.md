# Step-5 one-loop theorem independent audit

## Scope

Audited equation groups:

1. source measure and BRST dual action;
2. open-color and dotted-index typing;
3. Lorentz projector and tree EOM identity;
4. vector/chiral frame bridge;
5. source-linear Hessian expansion;
6. background Ward recursion;
7. connection filtration;
8. quadratic-jet completion theorem.

No loop coefficient is imported or accepted.

On the pure-gauge letter set, the Project $U(1)_R$ certificate fixes

$$
r_{\rm P}(W,\widetilde W,\nabla,\bar\nabla,\mathcal D)
=(+1,-1,-1,+1,0).
$$

## Exact results

$$
\begin{gathered}
[\mathscr I]=\frac92,\qquad
[d^8z]=-2,\qquad
[J]=-\frac52,\qquad
r_{\mathrm P}(J)=1,\qquad
|J|=1,\\
\rho_2(c)=\rho_{\rm ad}(c)\otimes\mathbf1
+\mathbf1\otimes\rho_{\rm ad}(c),\\
\mathbf s\langle J,\mathscr I\rangle
=\langle\mathbf sJ,\mathscr I\rangle
-\langle J,\mathbf s\mathscr I\rangle=0.
\end{gathered}
$$

$$
X^AX^B=X^BX^A,
\qquad
\mathscr I^{AB}=\mathscr I^{BA}.
$$

For the literal (5.54A) index order,

$$
K_-^{DE}
=
\widetilde{\mathcal W}^D_{\dot\alpha}Y^{E\dot\alpha}
-Y^{D\dot\alpha}\widetilde{\mathcal W}^E_{\dot\alpha},
\qquad
K_-^{ED}=-K_-^{DE},
$$

$$
\mathscr O_-^{BA}=-\mathscr O_-^{AB},
\qquad
\boxed{\mathscr O_-^{(AB)}=0.}
$$

The complete reflected block replay gives

$$
s_{\rm ref}=(-1)_{\rm external}(-1)_{\rm quantum}=+1,
$$

$$
\boxed{
\mathscr O_+^{AB}
=c_{ACD}c_{BCE}
\left[
\widetilde{\mathcal W}_{\dot a}^{D}\mathcal D_+{}^{\dot a}X^E
+(\mathcal D_+{}^{\dot a}X^D)\widetilde{\mathcal W}_{\dot a}^{E}
\right],
\qquad
\mathscr O_+^{BA}=\mathscr O_+^{AB}.}
$$

The exact component witness is

$$
Y_{\dot\alpha}=(a,b),\quad
\widetilde{\mathcal W}_{\dot\alpha}=(c,d),\quad
Y^{\dot\alpha}=(b,-a),\quad
\widetilde{\mathcal W}^{\dot\alpha}=(d,-c),
$$

$$
Y^{\dot\alpha}\widetilde{\mathcal W}_{\dot\alpha}=bc-ad,
\qquad
Y_{\dot\alpha}\widetilde{\mathcal W}^{\dot\alpha}=ad-bc.
$$

$$
S_L\otimes\operatorname{Sym}^4S_L
=
\operatorname{Sym}^5S_L
\oplus
\operatorname{Sym}^3S_L,
\qquad
10=6+4,
$$

$$
U_{-;++++}=H_{-++++}-\frac45t_{+++},
\qquad
\nabla_{(a}X_{bc)}=0,
\qquad
H_{abcde}=0,
$$

$$
\boxed{
U_{-;++++}=-\frac45t_{+++},
\qquad
\mathscr I^{AB}
=-(\nabla_+\mathcal E^A)X^B
-X^A(\nabla_+\mathcal E^B).}
$$

For the source-linear Hessian,

$$
\frac12\operatorname{STr}\!\left[
+G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2
-G_0I_1G_0H_1
+G_0I_2
\right],
$$

with rooted-family counts and polarized counts

$$
(N_2,N_3,N_4)_{\rm rooted}=(4,8,16),
\qquad
(N_2,N_3,N_4)_{\rm polarized}=(6,26,150).
$$

The complete quadratic contact replay has vector-branch counts

$$
N_{I_0H_2}=576,
\qquad
N_{I_1[1]H_1[2]}=N_{I_1[2]H_1[1]}=1440,
\qquad
N_{I_2}=720.
$$

Its local projector census is

$$
N_{\rm bubble}=360,
\qquad
N_{X,{\rm local}}=96,
\qquad
N_{\widetilde W,{\rm local}}=120,
\qquad
N_{\rm both}=32,
\qquad
N_{\rm shared}=328.
$$

Therefore, before any propagator-cancellation regrouping,

$$
C_{2,{\rm reg}}
=C_{\triangle,{\rm bare,reg}}+C_{{\rm contact,Hess},{\rm reg}},
\qquad
\operatorname{status}\!\left(
C_{{\rm contact,Hess},{\rm reg}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
$$

The candidate collapse carrier has

$$
N_{\rm binding}=48,
\qquad
N_{\rm GraphIR}=6,
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED}.
$$

At cubic background order,

$$
N_{\rm pol}(3)=26,
\qquad
N_{\rm kernel\ ready}=24,
$$

while $I_0H_3$ and $I_3$ are absent from the current grammar.

$$
\deg_{\mathcal A}\mathscr I\le7,
\qquad
\deg_{\mathcal A}\mathscr O_-\le6.
$$

$$
d_{\rm Adj}^{ABC}
=\operatorname{Tr}_{\rm Adj}
\left(T_{\rm ad}^A\{T_{\rm ad}^B,T_{\rm ad}^C\}\right)
=-d_{\rm Adj}^{ABC}
=0.
$$

## Theorem split

General completion:

$$
\ell_2[\mathscr O_1]=\ell_2[\mathscr O_2],
\qquad
\ker\ell_2=0
\quad\Longrightarrow\quad
[\mathscr O_1]=[\mathscr O_2].
$$

The physical-$4d$ total filtered premise is not certified:

$$
\ker\bar\ell_2^{\,4d}
=\texttt{FAIL\_CLOSED\_MISSING\_TRUE\_N1\_PARENT\_INCIDENCE}.
$$

The raw full-DRED premise is false.  With

$$
\widetilde\delta^{mn}
=\frac\epsilon2\delta_{(4)}^{mn}+\tau^{mn},
\qquad
\delta_{(4)mn}\tau^{mn}=0,
$$

$$
\mathscr E_{abc}^{AB}
=K^{AB}{}_{C[DE]}
\tau_{(ab|\dot c\dot d|}
W_{c)}^C\widetilde W^{D\dot c}\widetilde W^{E\dot d},
$$

$$
\ell_2(\mathscr E)=0,
\qquad
\left.\partial_t^3\mathscr E(t\mathcal B)\right|_{t=0}\ne0,
\qquad
q_{4d}(\mathscr E)=0.
$$

Rank-one corollary:

$$
\dim\mathfrak H_{\mathrm{sym},\,3/2,\,r_{\mathrm P}=-1}=1,
\qquad
[\mathscr O_\star]\ne0
\quad\Longrightarrow\quad
[\mathscr A_{{\rm loc},4d}^{(1),{\rm reg},AB}]
=C_{2,{\rm reg}}[\mathscr O_\star^{AB}],
\qquad
\mathscr A_{{\rm loc},4d}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\Gamma_{\mathscr I,{\rm ren,DRED}}^{(1),{\rm reg}}.
$$

Rank one is not required for the general injective-completion theorem.

## Gaps

| ID/type | location | claim | missing; minimal repair | severity/status |
|---|---|---|---|---|
| G1[G-PROJ] | Sections 1, 3 | ordered `A|B` ledger represents the local symmetric seed | the Sym2 map passes on the triangle; the contact replay is typed but its post-projector pole is open | P1/PASS_MAP_TRIANGLE; CONTACT_POLE_OPEN |
| G2[G-SIGN] | Section 3, old (5.54A) | reflected orientation has sign `-1` | exact full-block replay gives `(-1)_ext(-1)_quantum=+1`; isolated-triangle artifacts are regenerated | P0/PASS; CONTACT_OPEN |
| G3[G-IDX] | Section 3 | old dotted slots and derivative output are typed | `TildeW` is DOWN and the external token is the covariant vector derivative | P0/PASS |
| G4[G-DEF] | Section 1, GraphIR source port | insertion-source port is bosonic | odd `J`, odd insertion, and even `JI` are distinct; the external source port is FERMION | P0/PASS |
| G5[G-OP] | Section 4 | one source closes under the linearized Slavnov operator | background-CE source nilpotence passes; the complete quantum BV source multiplet is absent | P1/PASS_BACKGROUND_CE; FULL_BV_OPEN |
| G6[G-ALG] | Section 7 | the abstract Hessian census equals the physical primitive family | all six quadratic rooted words are present; $H_2$ projector, shared-scope D algebra, (48)-binding cut-map transport, $I_2$ normalization, and $\mathrm{CT}_2$ mixing remain open | P1/PARTIAL_FAIL_CLOSED |
| G7[G-THM] | Sections 2, 5 | vector/chiral frames give the same regulated insertion | fixed-vector-frame similarity and DRED cyclicity pass; the actual nonlinear chiral-vector tangent map and cross-frame measure remain open | P1/PASS_FIXED_FRAME; CROSS_FRAME_OPEN |
| G8[G-THM] | Section 4 | the quantum background Ward identity is exact | the functional Hessian Ward identity passes; vertex-by-vertex replay and any restoration counterterm remain open | P1/PASS_FUNCTIONAL; REPLAY_OPEN |
| G9[G-THM] | Section 4 | the fixed quadratic jet is injective | $N=2$ candidate block has zero kernel; total physical-$4d$ proof lacks $C_1:\mathbb Q^{20}\to\mathbb Q^{4866}$; raw full-DRED has explicit $\tau$ kernel | P0/FAIL_CLOSED_4D; FAIL_EXPLICIT_DRED |
| G10[G-DEF] | Sections 1, 4 | the formal grading is Project `U(1)_R` | pure-gauge Project charge action is derived and executable | PASS_PURE_GAUGE |
| G11[G-THM] | Section 4 | the physical candidate channel has rank one | $R_2^{\rm cand}$ has one class per symbolic color module and the actual $K_S$ line survives combined exchange; full source/color cohomology remains open | P1/PARTIAL_COROLLARY |
| G12[G-SCOPE] | Section 4 | pure-gauge injectivity settles full N=4 | enumerate matter-containing source classes and their quadratic jets separately | P1/OPEN |

The sharp physical-$4d$ route to G9 is the total filtered relation matrix.
The missing incidence is

$$
C_1:\mathbb Q^{20}\longrightarrow\mathbb Q^{4866}.
$$

The $4866$ coordinates are event paths, not parent generators.  In one parent
fiber,

$$
(q_{\rm PBW}M_{1\to2})_0=-2,
\qquad
(q_{\rm PBW}M_{1\to2})_6=0.
$$

Thus the naive skeleton/copy parent map does not close the filtration.  Full
$\mathcal N=4$ matter is separate.

## Spot checks

Take the lower dotted component vectors

$$
W_{\dot a}=(2,3),
\qquad
Y_{\dot a}=(5,7),
\qquad
Y^{\dot a}=(7,-5),
\qquad
W_{\dot a}Y^{\dot a}=2\cdot7+3\cdot(-5)=-1,
$$

$$
W^{\dot a}=(3,-2),
\qquad
Y_{\dot a}W^{\dot a}=5\cdot3+7\cdot(-2)=1.
$$

For the background variation through quadratic order,

$$
\left(1+\frac z2+\frac{z^2}{6}\right)
\left(1-\frac z2+\frac{z^2}{12}\right)
=1
+\left(-\frac12+\frac12\right)z
+\left(\frac1{12}-\frac14+\frac16\right)z^2
=1.
$$

For the source-linear two-background Hessian term,

$$
H^{-1}
=G_0-G_0H_+G_0+G_0H_+G_0H_+G_0+O(H_+^3),
$$

$$
[\mathcal V^2]H^{-1}I
=G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2
-G_0I_1G_0H_1
+G_0I_2.
$$

## Verification

$$
N_{\rm equation\ groups}=27.
$$

$$
N_{\rm type}=22/22,
\qquad
N_{\rm spin}=35/35,
\qquad
N_{\rm bridge}=18/18,
\qquad
N_{\rm focused\ tests}=45/45.
$$

$$
\texttt{ruff}=0,
\qquad
\texttt{py\_compile}=0,
\qquad
\texttt{diff-check}=0.
$$
