# Step-5 one-loop covariant-completion gap audit

## 1. Typed objects

$$
X^{\mathsf V,A}
:=
\left(
\boldsymbol\nabla^{\mathsf V}_{E+}
\boldsymbol{\mathcal W}^{\mathsf V}_{E+}
\right)^A,
\qquad
\mathcal D^{\mathsf V}_{E+\dot\alpha}
:=
(\sigma_E^m)_{+\dot\alpha}
\boldsymbol{\mathcal D}^{\mathsf V}_{Em}.
$$

$$
\mathscr I^{AB}
:=
\boldsymbol\nabla^{\mathsf V}_{E-}
\left(X^{\mathsf V,A}X^{\mathsf V,B}\right).
$$

The open labels are Project gauge-adjoint labels.  Since \(|X|=0\),

$$
\begin{aligned}
X^AX^B&=X^BX^A,\\
\mathscr I^{AB}
&=\left(\boldsymbol\nabla_{E-}X\right)^AX^B
+X^A\left(\boldsymbol\nabla_{E-}X\right)^B
=\mathscr I^{BA}.
\end{aligned}
$$

Therefore

$$
\boxed{
\mathscr I\in\operatorname{Sym}^2(\operatorname{Adj}),
\qquad
J^{\mathrm{loc}}_{(AB)}
\in\operatorname{Sym}^2(\operatorname{Adj})^\vee.}
$$

The graph ledger instead stores ordered orientations \(A|B\) in
\(\operatorname{Adj}\otimes\operatorname{Adj}\).  Denote its dual source by
\(J_{A|B}^{\mathrm{ord}}\).  The quotient

$$
\pi_{\mathrm{loc}}:
\operatorname{Adj}\otimes\operatorname{Adj}
\longrightarrow
\operatorname{Sym}^2(\operatorname{Adj})
$$

has not been implemented on the reflected graph sum.  Every formula below
with \(J_{(AB)}\) is the conditional physical-local-source formula; it does
not identify \(J_{A|B}^{\mathrm{ord}}\) with \(J_{(AB)}^{\mathrm{loc}}\).

The outer derivative is the tensor-product connection.  Since
\(|X|=0\),

$$
\begin{aligned}
\left(\boldsymbol\nabla_{E-}^{(2)}(X\otimes X)\right)^{AB}
={}&
\left(\boldsymbol\nabla_{E-}X\right)^A X^B
+X^A\left(\boldsymbol\nabla_{E-}X\right)^B,\\
\left.\boldsymbol\nabla_{E-}^{(2)}
\right|_{\operatorname{Sym}^2(\operatorname{Adj})}
:={}&D_{E-}
+\Gamma_{E-}^{\operatorname{Adj}}\otimes\mathbf1
+\mathbf1\otimes\Gamma_{E-}^{\operatorname{Adj}}.
\end{aligned}
$$

For

$$
i[\omega,Y]^A
=-\omega^C c_{CD}{}^A Y^D
=:\left(\rho_{\rm ad}(\omega)Y\right)^A,
$$

define

$$
\rho_2(\omega)
:=\rho_{\rm ad}(\omega)\otimes\mathbf1
+\mathbf1\otimes\rho_{\rm ad}(\omega).
$$

The exchange map commutes with \(\rho_2\), so this action preserves
\(\operatorname{Sym}^2(\operatorname{Adj})\).

Introduce a source-left odd dual source

$$
|J_{(AB)}|=1,
\qquad
\mathbf s_E\mathscr I=\rho_2(\mathfrak c_E)\mathscr I,
\qquad
\left\langle\mathbf s_EJ,\mathscr I\right\rangle
=
\left\langle J,\rho_2(\mathfrak c_E)\mathscr I\right\rangle.
$$

The odd Leibniz sign is then explicit:

$$
\begin{aligned}
\mathbf s_E\langle J,\mathscr I\rangle
&=\langle\mathbf s_EJ,\mathscr I\rangle
-\langle J,\mathbf s_E\mathscr I\rangle\\
&=\langle J,\rho_2(\mathfrak c_E)\mathscr I\rangle
-\langle J,\rho_2(\mathfrak c_E)\mathscr I\rangle
=0.
\end{aligned}
$$

The admissible source coupling is the full-superspace pairing

$$
S_J
:=
\int_{E,8}
J_{(AB)}\mathscr I^{(AB)},
$$

conditional on using the physical local quotient.  The ordered-ledger source
remains \(J_{A|B}^{\mathrm{ord}}\) until
\(\pi_{\mathrm{loc}}\) is fixed.

Since

$$
[d^8z]=-2,
\qquad
[\mathscr I]=\frac92,
\qquad
r_{\mathrm f}(d^8z)=0,
\qquad
r_{\mathrm f}(\mathscr I)=-1,
$$

where `r_f` denotes the temporary formal grading

$$
r_{\mathrm f}(\nabla_a)=-1,
\qquad
r_{\mathrm f}(\mathcal W_a)=+1,
\qquad
r_{\mathrm f}(\widetilde{\mathcal W}_{\dot a})=-1,
\qquad
r_{\mathrm f}(\mathcal D_{a\dot a})=0.
$$

Its identification with the Project (U(1)_R) charge is an open contract
binding and is not used as an accepted physical (R)-symmetry statement.

the source is an unconstrained odd dual superfield with

$$
\boxed{
[J]=-\frac52,
\qquad
r_{\mathrm f}(J)=+1,
\qquad
|J|=1.}
$$

The source carries the dual of the fixed Lorentz/twisted weight of
\(\mathscr I\).  A chiral \(d^6z\) coupling is forbidden without an explicit
chiral projector because

$$
\bar{\boldsymbol\nabla}_{E\dot a}X
=
\{\bar{\boldsymbol\nabla}_{E\dot a},
\boldsymbol\nabla_{E+}\}\boldsymbol{\mathcal W}_{E+}
\ne0,
$$

and therefore \(\mathscr I\) is not covariantly chiral.

The fixed-gauge Step-5A functional

$$
Z[\mathcal B_{\mathrm B},J]
:=
\int d\mu_{\mathrm{flat}}\,
\exp\left[
-\frac1{\hbar}
\left(
S_{\mathrm{gf}}[\mathcal B_{\mathrm B},Q]
+S_{\mathrm{FP}}[\mathcal B_{\mathrm B},Q,c,\widetilde c]
+S_{\mathrm{NK}}[\mathcal B_{\mathrm B},b,\widetilde b]
+S_J
\right)
\right].
$$

The 1PI insertion is

$$
\Gamma_{\mathscr I}^{AB}
:=
\left.
\frac{\vec\delta\Gamma[\mathcal B_{\mathrm B},J]}
{\delta J_{(AB)}}
\right|_{J=0},
\qquad
\Gamma_{\mathscr I}^{AB}
=
\sum_{\ell=0}^{\infty}
\hbar^\ell\Gamma_{\mathscr I}^{(\ell),AB}.
$$

$$
\mathscr A_{\mathrm{loc}}^{(1),AB}[\mathcal B_{\mathrm B}]
:=
\operatorname{Loc}_{\mathrm{UV}}
\Gamma_{\mathscr I}^{(1),AB}[\mathcal B_{\mathrm B}].
$$

`Loc_UV` retains only the renormalized local UV jet.  It does not retain the
full nonlocal one-loop 1PI amplitude.

From (3A.65),

$$
[\boldsymbol{\mathcal W}_a]=\frac32,
\qquad
[\boldsymbol\nabla_a]=\frac12,
\qquad
[\boldsymbol{\mathcal D}_{a\dot a}]=1.
$$

Hence

$$
[X]=2,
\qquad
[\mathscr I]=\frac12+2+2=\frac92,
\qquad
|\mathscr I|=1.
$$

The candidate sector obeys

$$
\left[
\widetilde{\boldsymbol{\mathcal W}}_{\dot\alpha}
\mathcal D_+{}^{\dot\alpha}X
\right]
=
\frac32+1+2
=
\frac92,
\qquad
\left|
\widetilde{\boldsymbol{\mathcal W}}_{\dot\alpha}
\mathcal D_+{}^{\dot\alpha}X
\right|
=1.
$$

In the fixed spin frame (5.1)--(5.2), lower \(+\) has
\(m_L=+\tfrac12\) and lower \(-\) has \(m_L=-\tfrac12\).  Therefore

$$
\begin{aligned}
(m_L,m_R)(X)
&=\left(\frac12+\frac12,0\right)=(1,0),\\
(m_L,m_R)(\mathscr I)
&=\left(-\frac12+1+1,0\right)
=\left(\frac32,0\right),\\
(m_L,m_R)
\left(
\widetilde{\boldsymbol{\mathcal W}}_{\dot\alpha}
\mathcal D_+{}^{\dot\alpha}X
\right)
&=\left(\frac12+1,0\right)
=\left(\frac32,0\right).
\end{aligned}
$$

Define the Lorentz lift

$$
X_{ab}:=\boldsymbol\nabla_{E(a}\boldsymbol{\mathcal W}_{Eb)},
\qquad
T_{bcde}:=X^A_{(bc}X^B_{de)},
\qquad
U_{a;bcde}:=\boldsymbol\nabla_{Ea}T_{bcde},
$$

and its trace

$$
t_{cde}:=\epsilon^{ab}U_{a;bcde}.
$$

scripts/step5_one_loop_spin_projector.py constructs exact rational
projectors

$$
S_L\otimes\operatorname{Sym}^4S_L
=
\operatorname{Sym}^5S_L
\oplus
\operatorname{Sym}^3S_L,
\qquad
10=6+4.
$$

For

$$
A:=U_{-;++++},
\qquad
B:=U_{+;-+++},
\qquad
t_{+++}=B-A,
$$

the exact component decomposition is

$$
H_{-++++}=\frac15A+\frac45B,
\qquad
\boxed{
U_{-;++++}
=
H_{-++++}-\frac45t_{+++}.}
$$

Here \(H_{-++++}\) is the \(j_L=\tfrac52\), \(m_L=\tfrac32\)
component, while \(t_{+++}\) is the \(j_L=\tfrac32\) component.  The
candidate

$$
C_{abc}
:=
\widetilde{\boldsymbol{\mathcal W}}_{\dot\alpha}
\mathcal D_{E(a}{}^{\dot\alpha}X_{bc)}
$$

belongs to \(\operatorname{Sym}^3S_L\), with
\(C_{+++}=
\widetilde{\boldsymbol{\mathcal W}}_{\dot\alpha}
\mathcal D_{E+}{}^{\dot\alpha}X_{++}\).
Thus \(\operatorname{Spin}(4)=(\tfrac12,0)\) is rejected.

The chiral Bianchi identity gives

$$
\begin{aligned}
\boldsymbol\nabla_{E(a}X_{bc)}
&=
\frac16\big(
\nabla_a\nabla_b\mathcal W_c
+\nabla_b\nabla_a\mathcal W_c
+\nabla_a\nabla_c\mathcal W_b\\
&\hspace{16mm}
+\nabla_c\nabla_a\mathcal W_b
+\nabla_b\nabla_c\mathcal W_a
+\nabla_c\nabla_b\mathcal W_a
\big)=0.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
H_{abcde}
&:=\nabla_{(a}T_{bcde)}\\
&=
\operatorname{Sym}_5\!\left[
(\nabla_{(a}X^A_{bc)})X^B_{de}
+X^A_{bc}(\nabla_{(a}X^B_{de)})
\right]=0,
\end{aligned}
$$

and hence

$$
\boxed{
H_{-++++}=0,
\qquad
U_{-;++++}=-\frac45t_{+++}.}
$$

The \(j_L=\tfrac52\) removal is exact.  Moreover, with

$$
\mathcal E:=\nabla^a\mathcal W_a,
\qquad
\nabla_-X=-\nabla_+\mathcal E,
$$

the tree insertion obeys

$$
\boxed{
\mathscr I^{AB}
=-(\nabla_+\mathcal E^A)X^B
-X^A(\nabla_+\mathcal E^B),
\qquad
t_{+++}=-\frac54\mathscr I^{AB}.}
$$

The certificate passes 35/35 exact checks.  Quantum cohomological triviality
of \(t_{+++}\), full \(\mathcal N=4\) EOM-ideal membership, and coefficient
matching to a symmetry-compatible candidate remain open.

## 2. Frame bridge

From (3C.25), (3C.28), and (3C.33),

$$
\nabla^{\mathsf C}_{E\mathfrak A}
=
\mathcal B_E^{-1}
\boldsymbol\nabla^{\mathsf V}_{E\mathfrak A}
\mathcal B_E,
\qquad
\mathcal W^{\mathsf C}_{Ea}
=
\mathcal B_E^{-1}
\boldsymbol{\mathcal W}^{\mathsf V}_{Ea}
\mathcal B_E.
$$

Hence

$$
X^{\mathsf C}
=
\mathcal B_E^{-1}X^{\mathsf V}\mathcal B_E,
\qquad
\mathcal D^{\mathsf C}_{E+\dot\alpha}X^{\mathsf C}
=
\mathcal B_E^{-1}
\left(
\mathcal D^{\mathsf V}_{E+\dot\alpha}X^{\mathsf V}
\right)
\mathcal B_E.
$$

For two open adjoint slots,

$$
\mathscr I^{\mathsf C,AB}
=
(\operatorname{Ad}_{\mathcal B_E^{-1}})^A{}_{A'}
(\operatorname{Ad}_{\mathcal B_E^{-1}})^B{}_{B'}
\mathscr I^{\mathsf V,A'B'}.
$$

The underlying Step-3C similarity, chirality, connection, field-strength,
action, matter, component, Jacobi, Wick, and Bianchi identities pass 106/106
exact \(\mathbb Q(i)\) checks.

The background/quantum split is fixed by (3D.80)--(3D.82):

$$
\mathcal E_{E,\mathrm{tot}}
=
\widetilde{\mathcal B}_{E,\mathrm B}
e^{\mathcal V_{E,\mathrm q}}
\mathcal B_{E,\mathrm B},
\qquad
e^{\mathcal V_{E,\mathrm q}'}
=
k_{E,\mathrm B}e^{\mathcal V_{E,\mathrm q}}
k_{E,\mathrm B}^{-1}.
$$

Set

$$
S:=\operatorname{Ad}_{\mathcal B_E^{-1}},
\qquad
A:=S^{-1}=\operatorname{Ad}_{\mathcal B_E}.
$$

For a coefficient column and an endomorphism,

$$
v_{\mathsf C}=Sv_{\mathsf V},
\qquad
v_{\mathsf V}=Av_{\mathsf C},
\qquad
H_{\mathsf C}=A^{-1}H_{\mathsf V}A,
\qquad
\mathsf G_{\mathsf C}=A^{-1}\mathsf G_{\mathsf V}A.
$$

The lower-index quadratic kernel and upper-index two-point covariance are
different tensor types:

$$
K_{\mathsf C}=A^{\mathsf T}K_{\mathsf V}A,
\qquad
G_{\mathsf C}=A^{-1}G_{\mathsf V}A^{-\mathsf T}.
$$

Hence

$$
\begin{aligned}
K_{\mathsf C}G_{\mathsf C}
&=
A^{\mathsf T}K_{\mathsf V}
\left(AA^{-1}\right)
G_{\mathsf V}A^{-\mathsf T}\\
&=
A^{\mathsf T}\mathbf1 A^{-\mathsf T}
=
\mathbf1,\\
G_{\mathsf C}K_{\mathsf C}
&=
A^{-1}G_{\mathsf V}
\left(A^{-\mathsf T}A^{\mathsf T}\right)
K_{\mathsf V}A\\
&=
A^{-1}\mathbf1 A
=
\mathbf1.
\end{aligned}
$$

Thus the similarity formula belongs to \(H\) and \(\mathsf G=H^{-1}\),
whereas the transpose formula belongs to \(K_{ij}\) and \(G^{ij}\).
They must not be denoted by the same kernel symbol.

For an insertion endomorphism,

$$
I_{\mathsf C}=A^{-1}I_{\mathsf V}A.
$$

Consequently

$$
\operatorname{STr}(\mathsf G_{\mathsf C}I_{\mathsf C})
=
\operatorname{STr}(A^{-1}\mathsf G_{\mathsf V}I_{\mathsf V}A)
=
\operatorname{STr}(\mathsf G_{\mathsf V}I_{\mathsf V})
$$

requires regulated graded cyclicity.  The coefficient density transforms as

$$
\boldsymbol\varpi_{\mathsf C}(v_{\mathsf C})
=
\boldsymbol\varpi_{\mathsf V}(Av_{\mathsf C})
\operatorname{Ber}(A).
$$

Therefore the perturbative frame bridge is accepted only after vertex
intertwining, regulated supertrace cyclicity, and the full-species regulated
Berezinian are proved.  Quadratic inverse transport alone proves none of
these three statements.

scripts/step5_frame_bridge_intertwiner.py verifies these identities in the
full color--Grassmann \(32\times32\) representation for three nonzero momentum
witnesses: 18/18 exact checks pass.  This proves the quadratic bridge only.

## 3. Candidate local covariant tensor

Set

$$
Y^A_{\dot\alpha}
:=
\mathcal D^{\mathsf V}_{E+\dot\alpha}X^{\mathsf V,A},
\qquad
Y^{A\dot\alpha}
:=
\epsilon^{\dot\alpha\dot\beta}Y^A_{\dot\beta},
\qquad
|Y|=0.
$$

The literal index positions of (5.54A) give

$$
\mathscr O_-^{AB}
=
c_{ACD}c_{BCE}
\left[
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V,D}_{E\dot\alpha}
Y^{E\dot\alpha}
-
Y^{D\dot\alpha}
\widetilde{\boldsymbol{\mathcal W}}^{\mathsf V,E}_{E\dot\alpha}
\right].
$$

Define

$$
S^{DE}
:=
\widetilde{\boldsymbol{\mathcal W}}^D_{\dot\alpha}
Y^{E\dot\alpha}.
$$

Since \(Y\) is even,

$$
\begin{aligned}
Y^{D\dot\alpha}
\widetilde{\boldsymbol{\mathcal W}}^E_{\dot\alpha}
&=
\widetilde{\boldsymbol{\mathcal W}}^E_{\dot\alpha}
Y^{D\dot\alpha}
=S^{ED},\\
K_-^{DE}
&:=S^{DE}-S^{ED},\\
K_-^{ED}&=-K_-^{DE}.
\end{aligned}
$$

Thus

$$
\begin{aligned}
\mathscr O_-^{BA}
&=c_{BCD}c_{ACE}K_-^{DE}\\
&=c_{BCE}c_{ACD}K_-^{ED}\\
&=-\mathscr O_-^{AB},\\
\boxed{
\mathscr O_-^{(AB)}=0.}
\end{aligned}
$$

The raising/lowering sign is fixed by the exact two-component witness

$$
\epsilon^{+-}=1,
\qquad
Y_{\dot\alpha}=(a,b),
\qquad
\widetilde{\mathcal W}_{\dot\alpha}=(c,d),
$$

$$
Y^{\dot\alpha}=(b,-a),
\qquad
\widetilde{\mathcal W}^{\dot\alpha}=(d,-c),
$$

$$
\begin{aligned}
Y^{\dot\alpha}\widetilde{\mathcal W}_{\dot\alpha}
&=bc-ad
=\widetilde{\mathcal W}_{\dot\alpha}Y^{\dot\alpha},\\
Y_{\dot\alpha}\widetilde{\mathcal W}^{\dot\alpha}
&=ad-bc
=-\widetilde{\mathcal W}_{\dot\alpha}Y^{\dot\alpha}.
\end{aligned}
$$

Therefore replacing the literal
\(Y^{D\dot\alpha}\widetilde{\mathcal W}^E_{\dot\alpha}\) by
\(Y^D_{\dot\alpha}\widetilde{\mathcal W}^{E\dot\alpha}\) changes its sign; the
two formulas are not interchangeable.

The ordered-to-local exchange map is

$$
\pi_{\rm loc}\Gamma^{A|B}(p_1,p_2)
:=
\frac12\left[
\Gamma^{A|B}(p_1,p_2)
+\Gamma^{B|A}(p_2,p_1)
\right].
$$

The exact reflected-word replay gives

$$
s_{\rm ext}=(-1)^1=-1,
\qquad
s_{\rm quantum}=(-1)^1=-1,
\qquad
s_{\rm ref}=s_{\rm ext}s_{\rm quantum}=+1.
$$

Equivalently, the complete odd word has four inversions,

$$
(W,Q_D,\widetilde W,Q_{\bar D})
\longrightarrow
(\widetilde W,Q_{\bar D},W,Q_D),
\qquad
(-1)^4=+1.
$$

Therefore the symmetry-compatible tensor is

$$
\boxed{
\mathscr O_+^{AB}
=c_{ACD}c_{BCE}
\left[
\widetilde{\mathcal W}_{\dot a}^D
\mathcal D_+{}^{\dot a}X^E
+
(\mathcal D_+{}^{\dot a}X^D)
\widetilde{\mathcal W}_{\dot a}^E
\right],
\qquad
\mathscr O_+^{BA}=\mathscr O_+^{AB}.}
$$

The old compiler inserted only the external permutation sign while retaining
the same internal ordered derivative word.  It also types the external source
port as bosonic, types the lower dotted \(\widetilde{\mathcal W}_{\dot a}\) port as
upper, and writes the vector derivative as the type-invalid
\(\nabla_+{}^{\dot a}\).  Hence

$$
\boxed{
\texttt{BLOCKED\_REFLECTION\_SOURCE\_AND\_DERIVATIVE\_TYPES}.}
$$

The sign and quotient are fixed; GraphIR, amplitude, D-algebra, pole, and
SD-contact artifacts must be regenerated before any coefficient is reused.

## 4. Conditional theorem form

After adjoining the full-superspace source to a source-extended BV action
\(\Sigma_J\), require

$$
\mathcal S(\Sigma_J)=0,
\qquad
\mathcal B_{\Sigma_J}^2=0.
$$

Only then define the temporary DRED complex

$$
\widehat{\mathcal V}_{\mathrm{loc}}^{J^1}
:=
\left\{
\int_{E,8}J_{(AB)}\mathscr O^{(AB)}:
\text{physical or evanescent, local, and linear in }J
\right\}
=
\mathcal V_{\mathrm{phys}}^{J^1}
\oplus
\mathcal V_{\mathrm{ev}}^{J^1},
$$

The evanescent summand is retained until pole subtraction and finite
renormalization are complete.  It is not quotiented out before the
\(\epsilon\times\epsilon^{-1}\) finite part is computed.

The source-linear cohomology is

$$
\mathfrak H_{\mathscr I}
:=
\frac{
\ker\!\left(
\mathcal B_{\Sigma_J}:
\widehat{\mathcal V}_{\mathrm{loc}}^{J^1}
\to
\widehat{\mathcal V}_{\mathrm{loc}}^{J^1}
\right)
}{
\operatorname{im}\mathcal B_{\Sigma_J}
+d\widehat{\mathcal V}_{\mathrm{loc}}^{J^1}
+\mathrm{EOM}
}.
$$

Finite source counterterms are not removed by this quotient.  A fixed
normalization condition chooses their representative after the closed,
exact, EOM, and evanescent mixing matrices have been computed.

The quotient is restricted to

$$
[\mathscr O]=\frac92,
\qquad
|\mathscr O|=1,
\qquad
\left(m_L,m_R\right)_{\mathscr O}
=
\left(\frac32,0\right),
\qquad
\mathrm{gh}(J\mathscr O)=0,
$$

and the fixed Project \(R\)-weight of
\(J_{(AB)}\mathscr I^{(AB)}\).

The fixed component does not yet define one irreducible
\(\operatorname{Spin}(4)\) representation.  Before an irreducible
cohomology sector is claimed, an explicit Lorentz projector must be supplied.

Define the fixed quadratic-background-jet map

$$
\ell_2:
\mathfrak H_{\mathscr I}
\longrightarrow
\mathcal T_{m=0},
\qquad
\ell_2[\mathscr O]
:=
\left.
\frac12
\frac{\vec\delta}{\delta\mathcal V_{\mathrm B,1}}
\frac{\vec\delta}{\delta\mathcal V_{\mathrm B,2}}
\mathscr O[\mathcal V_{\mathrm B}]
\right|_{\mathcal V_{\mathrm B}=0}.
$$

The general injective-completion theorem requires

$$
\boxed{
\left.
\mathscr W_{\mathrm B}
\left(
\Gamma_{5A}^{(1)}+\Gamma_{\rm restore}^{(1)}
\right)
\right|_{J^1}=0,
\qquad
\ker\ell_2=0.}
$$

Indeed, for two local covariant classes with the same complete tensor-valued
quadratic jet,

$$
\ell_2[\mathscr O_1]=\ell_2[\mathscr O_2]
\quad\Longrightarrow\quad
[\mathscr O_1-\mathscr O_2]\in\ker\ell_2
\quad\Longrightarrow\quad
[\mathscr O_1]=[\mathscr O_2].
$$

Thus injectivity, not \(\dim\mathfrak H_{\mathscr I}=1\), determines all local
dressings from the complete quadratic jet.  Without injectivity, a covariant
class whose expansion begins at cubic or higher field order is invisible to
the primitive triangle.

The rank-one candidate-channel corollary is stronger.  Define

$$
\mathfrak H_{\mathrm{sym},\,3/2,\,r_{\mathrm f}=-1}
:=
\left.
\mathfrak H_{\mathscr I}
\right|_{
\operatorname{Sym}^2(\operatorname{Adj}),
\;j_L=3/2,\;j_R=0,\;r_{\mathrm f}=-1}.
$$

Only if

$$
\dim\mathfrak H_{\mathrm{sym},\,3/2,\,r_{\mathrm f}=-1}=1,
\qquad
[\mathscr O_\star]\ne0,
\qquad
\mathscr O_\star\in
\mathfrak H_{\mathrm{sym},\,3/2,\,r_{\mathrm f}=-1},
$$

may the tensor-valued result be reduced to one scalar coefficient multiplying
\(\mathscr O_\star\).  This rank-one condition is not part of the
general injective-completion theorem.

The sharp pure-gauge route to this gate is the following conditional
filtration statement:

$$
\ker\ell_2
\subset
F_{\mathcal W}^{\ge3}\mathfrak H_{\mathscr I}^{\mathrm{gauge}}
\quad
\text{modulo derivative commutators}.
$$

If this associated-graded inclusion follows from the Project covariant-jet
grammar, then dimension and \(r_{\mathrm f}\) give

$$
3\cdot\frac32=\frac92,
\qquad
n_{\mathcal W}+n_{\widetilde{\mathcal W}}=3,
\qquad
n_{\mathcal W}-n_{\widetilde{\mathcal W}}=-1,
$$

and hence

$$
n_{\mathcal W}=1,
\qquad
n_{\widetilde{\mathcal W}}=2.
$$

Contracting the two dotted indices to \(j_R=0\) leaves

$$
\mathcal W_a
\left(
\widetilde{\mathcal W}_{\dot b}
\widetilde{\mathcal W}^{\dot b}
\right)
\in
\left(\frac12,0\right),
$$

not the required \(j_L=\tfrac32\) sector, while four field strengths have
dimension \(6>\tfrac92\).  The associated-graded inclusion itself is not
proved; therefore \(\ker\ell_2=0\) remains open.  The full
\(\mathcal N=4\) matter sector is a separate gate.

The complete free ordered dimension--\(r_{\mathrm f}\)--parity census gives

$$
\#\mathcal S_N=(5,7,5,1),
\qquad
\sum_{N=0}^{3}\#\mathcal S_N=18.
$$

In particular, the filtration lemma must eliminate the five degree-zero rows
and seven degree-one rows in the local BRST/EOM/IBP quotient; their absence
does not follow from the quadratic jet.

At field-strength degree \(N=2\),

$$
\begin{array}{c|ccccc}
&WW\nabla^3&W\widetilde W\nabla^2\bar\nabla&
W\widetilde W\nabla\mathcal D&
\widetilde W^2\nabla\bar\nabla^2&
\widetilde W^2\bar\nabla\mathcal D\\ \hline
\operatorname{mult}_{(3/2,0)}&4&1&1&0&0
\end{array}.
$$

The multiplicity-one entry is before graded Leibniz, covariant IBP,
\([\nabla,\mathcal D]\) curvature children, color, evanescent, and BRST/source
quotients.  Therefore it is not a rank-one cohomology result.

The two quotients are distinct:

$$
\mathfrak H_{\mathscr I}^{\mathrm{gauge}}
:=
\left.
\mathfrak H_{\mathscr I}^{\mathcal N=4}
\right|_{\boldsymbol\Phi_r=
\widetilde{\boldsymbol\Phi}_r=0},
\qquad
\mathfrak H_{\mathscr I}^{\mathcal N=4}.
$$

A pure-gauge triangle can determine only
\(\mathfrak H_{\mathscr I}^{\mathrm{gauge}}\) until all matter-containing
classes and their quadratic jets are enumerated.

If \(\mathcal B_{\Sigma_J}\mathscr I\) contains operator mixing or an EOM
term, the
single source is not closed.  One must instead introduce a source multiplet
\(J_I\) satisfying

$$
\Sigma_J
=
\Sigma[0]
+\int_{E,8}J_I\mathscr O^I,
\qquad
\mathcal S(\Sigma_J)=0,
\qquad
\mathcal B_{\Sigma_J}^{2}=0,
$$

and compute the cohomology of the complete source multiplet.  The one-source
formula above is admitted only after the direct check

$$
\mathcal B_{\Sigma_J}\mathscr I^{AB}
=
\rho_2(\mathfrak c)^{AB}{}_{CD}\mathscr I^{CD}
$$

with no additional local operator.

If the rank-one corollary is proved, then

$$
\boxed{
\mathscr A_{\mathrm{loc}}^{(1),AB}
=
C_{\triangle}
\mathscr O_\star^{AB}.}
$$

The literal \(\mathscr O_-^{AB}\) of Section 3 cannot be
\(\mathscr O_\star^{AB}\), because
\(\mathscr O_-^{(AB)}=0\).  \(C_{\triangle}\) is fixed only by the accepted
primitive triangle plus its complete \(m=0\) Schwinger--Dyson contact orbit.

The Step-3D finite-BV density defect
\(\mathfrak B_{E,\mathrm B,\nu}\) belongs to Step 5C and is not a Step-5A
blocker.  Step 5A instead requires locality of the regularized
background-Ward breaking and an explicit local restoration counterterm.

The algebraic gauge-anomaly tensor vanishes for every adjoint species.  In
the \(\kappa\)-orthonormal adjoint basis,

$$
(T_{\rm ad}^A)^{\mathsf T}=-T_{\rm ad}^A,
\qquad
\{T_{\rm ad}^B,T_{\rm ad}^C\}^{\mathsf T}
=\{T_{\rm ad}^B,T_{\rm ad}^C\},
$$

because \(c_{ABC}=c_{[ABC]}\).  Hence

$$
\begin{aligned}
d_{\rm Adj}^{ABC}
&:=\operatorname{Tr}_{\rm Adj}
\left(T_{\rm ad}^A\{T_{\rm ad}^B,T_{\rm ad}^C\}\right)\\
&=\operatorname{Tr}_{\rm Adj}
\left[
\left(T_{\rm ad}^A
\{T_{\rm ad}^B,T_{\rm ad}^C\}
\right)^{\mathsf T}
\right]\\
&=-\operatorname{Tr}_{\rm Adj}
\left(
\{T_{\rm ad}^B,T_{\rm ad}^C\}T_{\rm ad}^A
\right)\\
&=-\operatorname{Tr}_{\rm Adj}
\left(T_{\rm ad}^A
\{T_{\rm ad}^B,T_{\rm ad}^C\}\right)
=-d_{\rm Adj}^{ABC},\\
\boxed{d_{\rm Adj}^{ABC}}&=0.
\end{aligned}
$$

This removes the adjoint cubic gauge-anomaly obstruction.  It does not
construct \(\Gamma_{\rm restore}^{(1)}\), prove the required local Quantum
Action Principle in this regulator, or prove the Step-5C Jacobian.

The intended anomaly is not a background-gauge anomaly.  Its Ward pair is

$$
\mathscr W_{\mathrm B}\Gamma=0,
\qquad
\mathscr W_{-}\Gamma
=
\hbar\Delta_{-}^{(1)}+O(\hbar^2),
$$

so a constant even global shadow ghost \(\eta_-\) gives

$$
|\eta_-|=0,
\qquad
\operatorname{gh}(\eta_-)=1,
\qquad
|\Delta_-^{(1)}|=1,
\qquad
|\eta_-\Delta_-^{(1)}|=1,
$$

$$
\mathcal B_{\Sigma_J}
\left(\eta_-\Delta_{-}^{(1)}\right)=0.
$$

The background-gauge identity therefore selects a gauge-covariant density.
If \(\mathscr W_{\mathrm B}\Gamma\ne0\), the calculation instead enters the
consistent-gauge-anomaly complex and a Bardeen--Zumino finite local shift is
required; that case is outside this theorem.

Only manifest \(\mathcal N=1\) identities are presently used.  Any reduction
of \(\dim\mathfrak H_{\mathscr I}\) by hidden \(\mathcal N=4\) supersymmetry
requires its transformations, sources, and extended Slavnov--Taylor operator
to be added before the rank statement is accepted.

## 5. All-order background Ward recursion

Write the group-valued background variable as

$$
\mathcal E_{\mathrm B}'
=
\widetilde h_{\mathrm B}
\mathcal E_{\mathrm B}
h_{\mathrm B}^{-1},
$$

with the infinitesimal paths

$$
\widetilde h_{\mathrm B}(t)
=
\mathbf1+t\eta_{\mathrm L},
\qquad
h_{\mathrm B}(t)
=
\mathbf1+t\eta_{\mathrm R},
\qquad
\delta
:=
\left.\frac d{dt}\right|_{t=0}.
$$

For \(\mathcal E_{\mathrm B}=e^{\mathcal V_{\mathrm B}}\),

$$
\delta e^{\mathcal V_{\mathrm B}}e^{-\mathcal V_{\mathrm B}}
=
\frac{
e^{\operatorname{ad}_{\mathcal V_{\mathrm B}}}-1
}{
\operatorname{ad}_{\mathcal V_{\mathrm B}}
}\,
\delta\mathcal V_{\mathrm B}
=
\eta_{\mathrm L}
-
e^{\operatorname{ad}_{\mathcal V_{\mathrm B}}}
\eta_{\mathrm R}.
$$

Therefore the exact nonlinear prepotential variation is

$$
\boxed{
\delta\mathcal V_{\mathrm B}
=
\frac{
\operatorname{ad}_{\mathcal V_{\mathrm B}}
}{
e^{\operatorname{ad}_{\mathcal V_{\mathrm B}}}-1
}
\left(
\eta_{\mathrm L}
-
e^{\operatorname{ad}_{\mathcal V_{\mathrm B}}}
\eta_{\mathrm R}
\right).}
$$

Its Taylor coefficients are generated by

$$
\frac z{e^z-1}
=
\sum_{n=0}^{\infty}\frac{B_n}{n!}z^n,
\qquad
B_0=1,\quad B_1=-\frac12,\quad B_2=\frac16.
$$

The exact coefficient-left words begin as

$$
\begin{aligned}
\delta\mathcal V_{\mathrm B}\big|_{\eta_{\mathrm L}}
&=
\eta_{\mathrm L}
-\frac12[\mathcal V_{\mathrm B},\eta_{\mathrm L}]
+\frac1{12}
[\mathcal V_{\mathrm B},[\mathcal V_{\mathrm B},\eta_{\mathrm L}]]
-\frac1{720}
\operatorname{ad}_{\mathcal V_{\mathrm B}}^4(\eta_{\mathrm L})
+\cdots,\\
\delta\mathcal V_{\mathrm B}\big|_{\eta_{\mathrm R}}
&=
-\eta_{\mathrm R}
-\frac12[\mathcal V_{\mathrm B},\eta_{\mathrm R}]
-\frac1{12}
[\mathcal V_{\mathrm B},[\mathcal V_{\mathrm B},\eta_{\mathrm R}]]
+\frac1{720}
\operatorname{ad}_{\mathcal V_{\mathrm B}}^4(\eta_{\mathrm R})
+\cdots.
\end{aligned}
$$

For the vector subgroup \(\eta_{\mathrm L}=\eta_{\mathrm R}=\eta\),

$$
\boxed{
\delta\mathcal V_{\mathrm B}
=
-\operatorname{ad}_{\mathcal V_{\mathrm B}}(\eta)
=
[\eta,\mathcal V_{\mathrm B}].}
$$

The exact finite-order convolution proof is generated by
scripts/step5_background_ward_recursion.py; 8 independent tests pass through
order \(\operatorname{ad}_{\mathcal V}^{12}\).

The finite equation compatible with the same
\((\widetilde h_{\mathrm B},h_{\mathrm B})\) variables is the
gauge-chiral-frame equation

$$
\boxed{
\mathscr A_{\mathrm{loc}}^{\mathsf C,(1)}
[\mathcal E_{\mathrm B}']
=
\left(\operatorname{Ad}_{h_{\mathrm B}}\otimes
\operatorname{Ad}_{h_{\mathrm B}}\right)
\mathscr A_{\mathrm{loc}}^{\mathsf C,(1)}
[\mathcal E_{\mathrm B}].}
$$

Indeed \(X^{\mathsf C}=\mathcal B^{-1}X^{\mathsf V}\mathcal B\) and
\(\mathcal B'=k\mathcal B h^{-1}\) give
\(X^{\mathsf C\prime}=hX^{\mathsf C}h^{-1}\).  A vector-frame formula would
instead contain the compensator \(k(\mathcal V;h,\widetilde h)\); treating
that compensator as a fixed representation matrix would omit contact terms.

Let

$$
\mathscr A_{(m)}
:=
\left.
\frac{\delta^m\mathscr A_{\mathrm{loc}}^{(1)}}
{\delta\mathcal V_{\mathrm B,1}\cdots
\delta\mathcal V_{\mathrm B,m}}
\right|_{\mathcal V_{\mathrm B}=0}.
$$

Define the polarized Taylor maps by

$$
\begin{aligned}
R(\mathcal V_{\mathrm B};\eta_{\mathrm L},\eta_{\mathrm R})
&=
\sum_{r=0}^{\infty}
\frac1{r!}
R_r(\mathcal V_{\mathrm B}^{\otimes r};\eta),\\
\mathscr A_{\mathrm{loc}}^{(1)}
[\mathcal V_{\mathrm B}]
&=
\sum_{m=0}^{\infty}
\frac1{m!}
\mathscr A_m(
\mathcal V_{\mathrm B}^{\otimes m}).
\end{aligned}
$$

The first variation maps are

$$
\begin{aligned}
R_0(\eta_{\mathrm L},\eta_{\mathrm R})
&=
\eta_{\mathrm L}-\eta_{\mathrm R},\\
R_1(\mathcal V_1;\eta_{\mathrm L},\eta_{\mathrm R})
&=
-\frac12[\mathcal V_1,\eta_{\mathrm L}]
-\frac12[\mathcal V_1,\eta_{\mathrm R}],\\
R_2(\mathcal V_1,\mathcal V_2;\eta_{\mathrm L},\eta_{\mathrm R})
&=
\frac1{12}
\left(
[\mathcal V_1,[\mathcal V_2,\eta_{\mathrm L}]]
+[\mathcal V_2,[\mathcal V_1,\eta_{\mathrm L}]]
\right)\\
&\quad
-\frac1{12}
\left(
[\mathcal V_1,[\mathcal V_2,\eta_{\mathrm R}]]
+[\mathcal V_2,[\mathcal V_1,\eta_{\mathrm R}]]
\right).
\end{aligned}
$$

Let \(\rho_2(\eta_{\mathrm R})\) act on the two open adjoint slots and every
explicit gauge-chiral-frame covariant probe.  The exact formal level-\(n\)
recursion is

$$
\boxed{
\sum_{S\subseteq\{1,\ldots,n\}}
\mathscr A_{n-|S|+1}
\left(
R_{|S|}(\mathcal V_S;\eta_{\mathrm L},\eta_{\mathrm R}),
\mathcal V_{S^c}
\right)
-
\rho_2(\eta_{\mathrm R})\,
\mathscr A_n(\mathcal V_1,\ldots,\mathcal V_n)
=0.}
$$

The first three levels are

$$
\begin{aligned}
n=0:\quad&
\mathscr A_1(R_0(\eta_{\mathrm L},\eta_{\mathrm R}))
-
\rho_2(\eta_{\mathrm R})\mathscr A_0
=0,\\
n=1:\quad&
\mathscr A_2(R_0,\mathcal V_1)
+\mathscr A_1(R_1(\mathcal V_1;\eta))
-
\rho_2(\eta_{\mathrm R})\mathscr A_1(\mathcal V_1)
=0,\\
n=2:\quad&
\mathscr A_3(R_0,\mathcal V_1,\mathcal V_2)
+\mathscr A_2(R_1(\mathcal V_1;\eta),\mathcal V_2)\\
&+
\mathscr A_2(R_1(\mathcal V_2;\eta),\mathcal V_1)
+\mathscr A_1(R_2(\mathcal V_1,\mathcal V_2;\eta))\\
&-
\rho_2(\eta_{\mathrm R})
\mathscr A_2(\mathcal V_1,\mathcal V_2)
=0.
\end{aligned}
$$

For the vector subgroup
\(\eta_{\mathrm L}=\eta_{\mathrm R}=\eta\),

$$
R_0=0,
\qquad
R_1(\mathcal V;\eta)=[\eta,\mathcal V],
\qquad
R_{r\ge2}=0.
$$

Therefore it is level-preserving:

$$
\boxed{
\sum_{j=1}^{n}
\mathscr A_n
\left(
\mathcal V_1,\ldots,[\eta,\mathcal V_j],\ldots,\mathcal V_n
\right)
-\rho_2(\eta)\mathscr A_n(\mathcal V_1,\ldots,\mathcal V_n)
=0.}
$$

It contains no \(\mathscr A_{n+1}\) term and cannot determine higher
background levels.  Level mixing comes from the independent chiral and
antichiral transformations for which \(R_0\ne0\).

The exact recursion is the coefficient identity

$$
\boxed{
\left.
\frac{\delta^m}{
\delta\mathcal V_{\mathrm B,1}\cdots
\delta\mathcal V_{\mathrm B,m}}
\left[
\mathscr W_{\omega}^{\mathrm B}
-\delta_{\omega}^{AB}
\right]
\mathscr A_{\mathrm{loc}}^{(1)}
\right|_{\mathcal V_{\mathrm B}=0}
=0.}
$$

All seagull/contact terms are the terms in which at least two functional
derivatives act on the nonlinear background transformation
\(\delta_\omega\mathcal V_{\mathrm B}\).  They are generated from the finite
group equation; none is discarded.

For an independent left/right transformation with \(R_0\ne0\), the
\(R_0\) term constrains the longitudinal projection of
\(\mathscr A_{n+1}\).  The vector subgroup has \(R_0=0\) and supplies only
same-level covariance.  In either case a homogeneous local transverse
solution with vanishing quadratic jet remains possible until
\(\ker\ell_2=0\) is proved.

## 6. Finite versus infinite completion

From (5.53n),

$$
\Gamma_{(n)a}
=
\frac{(-1)^{n-1}}{n!}
\operatorname{ad}_{\mathcal V}^{n-1}(D_a\mathcal V),
\qquad n\ge1.
$$

Therefore

$$
\mathcal W_a
=
-\frac18\bar D^2
\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}{n!}
\operatorname{ad}_{\mathcal V}^{n-1}(D_a\mathcal V),
$$

so the unconstrained-prepotential completion contains every
\(m\ge0\) background-leg order.

$$
\boxed{
\text{triangle}+
\text{box}+
\text{pentagon}
\ne
\text{all-order prepotential completion}.}
$$

Triangle, box, and pentagon are the \(m=0,1,2\) Taylor checks.  All-order
completion requires the Ward-recursion certificate.

For an independent connection \(\mathcal A\), define the exact filtration

$$
\deg_{\mathcal A}\mathcal A=1,
\qquad
\deg_{\mathcal A}\mathcal F\le2,
\qquad
\deg_{\mathcal A}(\mathcal D Y)
\le
\deg_{\mathcal A}Y+1.
$$

Then

$$
\deg_{\mathcal A}\widetilde{\mathcal W}\le2,
\qquad
\deg_{\mathcal A}X
=
\deg_{\mathcal A}(\nabla_+\mathcal W_+)
\le3,
$$

$$
\deg_{\mathcal A}(\mathcal D_+X)\le4,
\qquad
\boxed{
\deg_{\mathcal A}\mathscr O_-\le6.}
$$

The classical insertion and the candidate anomaly are different words.  For
the seed itself,

$$
\deg_{\mathcal A}X\le3,
\qquad
\deg_{\mathcal A}(X^AX^B)\le6,
\qquad
\boxed{
\deg_{\mathcal A}\mathscr I^{AB}
=
\deg_{\mathcal A}\nabla_-(X^AX^B)
\le7.}
$$

Thus \(7\) is the unreduced classical-seed bound, whereas \(6\) is the bound
for the displayed anomaly candidate.  Equality at either bound still
requires a nonzero color--spinor word after Bianchi, Jacobi, and graded
symmetry reduction.

Thus the connection-variable local polynomial is finite, but triangle,
cycle-4 box, and cycle-5 pentagon are not by themselves a completeness proof
for this derivative-rich operator.  The prepotential-\(\mathcal V\) expansion
remains infinite.

## 7. One-loop Hessian generator and first three graph levels

Double every complex quantum field into the real BV Gaussian carrier and
define

$$
H[J,\mathcal V]
:=
\frac{\vec\delta}{\delta Q}
\frac{\overleftarrow\delta}{\delta Q}
\Sigma_J[\mathcal V,Q]
=
H_0+H_+[\mathcal V]+J I[\mathcal V],
$$

$$
H_+[\mathcal V]
=
\sum_{r\ge1}H_r[\mathcal V^r],
\qquad
I[\mathcal V]
=
\sum_{s\ge0}I_s[\mathcal V^s],
\qquad
G_0:=H_0^{-1}.
$$

Then

$$
\Gamma^{(1)}
=
\frac12\operatorname{STr}\log H,
\qquad
\Gamma_{\mathscr I}^{(1)}
=
\frac12\operatorname{STr}\!\left(H^{-1}I\right),
$$

and the exact background expansion is

$$
\boxed{
\Gamma_{\mathscr I,n}^{(1)}
=
\frac12[\mathcal V^n]
\sum_{k=0}^{\infty}(-1)^k
\operatorname{STr}\!\left[
G_0 I[\mathcal V]
\left(G_0H_+[\mathcal V]\right)^k
\right]
+\mathrm{CT}_n.}
$$

Here \([\mathcal V^n]\) includes all labeled external-leg polarizations and
all cyclically inequivalent graded words.  At the primitive two-background
level,

$$
\boxed{
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\Big[
&G_0I_0G_0H_1G_0H_1
-G_0I_0G_0H_2\\
&-G_0I_1G_0H_1
+G_0I_2
\Big]_{[\mathcal V_1\mathcal V_2]}
+\mathrm{CT}_2.
\end{aligned}}
$$

Consequently the isolated geometric triangle is not the complete primitive
boundary.  The seagull, insertion-contact, double-contact, collapsed SD, and
counterterm families must be generated before any class projection.

With labeled backgrounds \((\mathcal V_1,\mathcal V_2)\), the six exact
polarizations are

$$
\boxed{
\begin{aligned}
\Gamma_{\mathscr I,2}^{(1)}
=\frac12\operatorname{STr}\Big[&
+G_0I_0G_0H_1[\mathcal V_1]G_0H_1[\mathcal V_2]\\
&+G_0I_0G_0H_1[\mathcal V_2]G_0H_1[\mathcal V_1]\\
&-G_0I_0G_0H_2[\mathcal V_1,\mathcal V_2]\\
&-G_0I_1[\mathcal V_1]G_0H_1[\mathcal V_2]\\
&-G_0I_1[\mathcal V_2]G_0H_1[\mathcal V_1]\\
&+G_0I_2[\mathcal V_1,\mathcal V_2]
\Big]+\mathrm{CT}_2.
\end{aligned}}
$$

scripts/step5_one_loop_hessian_insertion_census.py independently enumerates

$$
N_{\rm family}(2,3,4)=(4,8,16),
\qquad
N_{\rm polarized}(2,3,4)=(6,26,150),
$$

with the exact rooted signs

$$
+I_0H_1H_1,
\qquad
-I_0H_2,
\qquad
-I_1H_1,
\qquad
+I_2.
$$

Its status is
\(\mathrm{PASS\_COMBINATORICS\_FAIL\_CLOSED\_PHYSICS}\).  The full
source multiplet, graded cyclic source sign, ordered nonzero Project Hessian
blocks, frame-functional Jacobian, and counterterm coefficients remain
unresolved.  The full-superspace source measure is fixed in Section 1; this
does not close the source-partner obligation.

$$
\begin{array}{c|l}
m&\text{connected one-loop families}\\
\hline
0&\triangle+I_{(3)}\widetilde S_{(3)}+I_{(4)}+
\text{all propagator collapses}\\
1&\text{background-dressed triangles}+\text{cycle-4 boxes}+
\text{seagulls}+\text{pinches}\\
2&\text{twice-dressed triangles}+\text{dressed boxes}+
\text{cycle-5 pentagons}+\text{seagulls}+\text{pinches}
\end{array}
$$

For each \(m\), GraphIR must include physical, gauge-fixing, FP, NK,
insertion, and counterterm ports before a family is marked absent.

Let \(H_{\mathrm{phys}}\) be the connected physical/insertion component and
\(H_{\mathrm{det}}\) one connected FP or NK cycle.  If \(a\) quantum edges
join the two components, then

$$
\begin{aligned}
L_{\mathrm{joined}}
&=
L_{\mathrm{phys}}
+L_{\mathrm{det}}
+a-1\\
&=
L_{\mathrm{phys}}+1+a-1\\
&=
L_{\mathrm{phys}}+a.
\end{aligned}
$$

For \(a=1\), the unique joining edge is a bridge and the graph is 1PR.  For
\(a\ge2\),

$$
L_{\mathrm{joined}}\ge2.
$$

External background ports change neither the internal-edge count nor the
vertex count.  Therefore, under the Step-5A typed propagator grammar and the
absence of FP/NK ports on the physical insertion,

$$
\boxed{
\Gamma_{\mathscr I,\mathrm{FP/NK}}^{(1),\mathrm{1PI}}
[\,\mathcal V_{\mathrm B}\,]
=0
\qquad
\text{at every background order}.}
$$

scripts/step5_one_loop_ghost_background_census.py verifies 108 topology rows;
5/5 checks pass.  This statement does not use the finite-BV coefficient-space
cycles, which remain Step-5C obligations.

## 8. Acceptance gates

$$
\begin{array}{c|c}
\text{gate}&\text{status}\\
\hline
\texttt{BACKGROUND_PREPOTENTIAL_VARIATION}&\texttt{PASS}\\
\texttt{CHIRAL\_FRAME\_WARD\_SUBSET\_COMBINATORICS}&\texttt{PASS}\\
\texttt{VECTOR\_SUBGROUP\_LEVEL\_PRESERVING}&\texttt{PASS}\\
\texttt{SOURCE\_FULL\_SUPERSPACE\_MEASURE}&\texttt{PASS}\\
\texttt{PROJECT\_R\_WEIGHT\_BINDING}&\texttt{OPEN}\\
\texttt{SEED\_OPEN\_COLOR\_SYMMETRY}&
\texttt{PASS\;(\operatorname{Sym}^2\operatorname{Adj})}\\
\texttt{ORDERED\_A|B\_TO\_LOCAL\_SYM2\_QUOTIENT}&
\texttt{PASS\_MAP;\ PIPELINE\_UNAPPLIED}\\
\texttt{LITERAL\_5.54A\_SYM2\_PROJECTION}&\texttt{FAIL\;(ZERO)}\\
\texttt{REFLECTED\_DOTTED\_INDEX\_VARIANCE}&
\texttt{PASS\_AUDIT;\ GRAPHIR\_REPAIR\_OPEN}\\
\texttt{WW\_SOURCE\_GRAPHIR\_PARITY}&\texttt{FAIL\;(BOSON\to FERMION)}\\
\texttt{TILDEW\_GRAPHIR\_DOTTED\_VARIANCE}&
\texttt{FAIL\;(UP\to DOWN)}\\
\texttt{EXTERNAL\_VECTOR\_DERIVATIVE\_TYPE}&
\texttt{FAIL\;(\nabla_+{}^{\dot a}\to\mathcal D_+{}^{\dot a})}\\
\texttt{SOURCE\_BV\_MULTIPLET\_CLOSURE}&\texttt{UNCOMPUTED}\\
\texttt{FIXED\_TWIST\_WEIGHT\_(3/2,0)}&\texttt{PASS}\\
\texttt{LORENTZ\_IRREP\_PROJECTOR}&\texttt{PASS\;(10=6+4)}\\
\texttt{SEED\_J\_5/2\_CHIRAL\_BIANCHI\_REMOVAL}&\texttt{PASS}\\
\texttt{SEED\_TREE\_EOM\_IDENTITY}&\texttt{PASS}\\
\texttt{SEED\_J\_3/2\_QUANTUM\_COHOMOLOGY/CANDIDATE\_MATCH}&
\texttt{OPEN}\\
\texttt{CONNECTION\_DEGREE\_SEED/CANDIDATE}&\texttt{PASS\;(7/6)}\\
\texttt{HESSIAN\_INSERTION\_ABSTRACT\_CENSUS}&
\texttt{PASS\_COMBINATORICS}\\
\texttt{ORDERED\_HESSIAN\_BLOCK\_VALUES}&\texttt{UNCOMPUTED}\\
\texttt{FRAME_BRIDGE_QUADRATIC_KERNEL}&\texttt{PASS}\\
\texttt{FRAME_BRIDGE_VERTEX_INTERTWINER}&\texttt{UNCOMPUTED}\\
\texttt{FRAME_BRIDGE_REGULATED_SUPERTRACE}&\texttt{UNPROVED}\\
\texttt{STEP5A\_ADJOINT\_GAUGE\_ANOMALY\_TENSOR}&\texttt{PASS\;(ZERO)}\\
\texttt{STEP5A\_WARD\_RESTORATION\_COUNTERTERM}&\texttt{UNCOMPUTED}\\
\texttt{STEP5C\_FINITE\_BV\_DENSITY/JACOBIAN}&\texttt{UNPROVED}\\
\texttt{LOCAL_COVARIANT_BASIS_RANK_ONE}&
\texttt{PARTIAL\;(FREE\ ORDERED\ MULTIPLICITY\ ONE)}\\
\texttt{FULL_N4_MATTER_CLASS_CENSUS}&\texttt{UNCOMPUTED}\\
\texttt{QUADRATIC_COVARIANT_JET_INJECTIVE}&\texttt{UNCOMPUTED}\\
\texttt{PURE\_GAUGE\_ASSOCIATED\_GRADED\_FILTRATION}&
\texttt{PARTIAL\;(QUOTIENTS\ OPEN)}\\
\texttt{M0_SD_ORBIT_ACCEPTED}&\texttt{OPEN\;(5.54B)}\\
\texttt{BACKGROUND_PORT_CENSUS_M1_M2}&\texttt{UNCOMPUTED}\\
\texttt{BOX_LAYER_EQUALS_TARGET_TAYLOR_1}&\texttt{UNCOMPUTED}\\
\texttt{PENTAGON_LAYER_EQUALS_TARGET_TAYLOR_2}&\texttt{UNCOMPUTED}\\
\texttt{SD_TAYLOR_COMMUTATOR_ZERO}&\texttt{UNCOMPUTED}\\
\texttt{FP_NK_BACKGROUND_CENSUS}&\texttt{PASS\;(STEP5A\;1PI)}\\
\texttt{QUANTUM\_INSERTION\_WARD\_RECURSION}&\texttt{UNPROVED}
\end{array}
$$

## 9. Fail-closed conclusion

The primitive triangle coefficient does not yet determine the complete local
covariant answer.  The exact blockers are

$$
\boxed{
\left.
\mathscr W_{\mathrm B}
\left(
\Gamma_{5A}^{(1)}+\Gamma_{\rm restore}^{(1)}
\right)
\right|_{J^1}=0,
\qquad
\ker\ell_2=0,
\qquad
\mathcal A_{\triangle}^{(4)}
+\mathcal A_{I_{(3)}\widetilde S_{(3)}}^{(4)}
+\mathcal A_{I_{(4)}}^{(4)}
+\mathcal A_{\mathrm{collapsed}}^{(4)}=0.}
$$

In addition, the repaired ordered \(A|B\)-to-local quotient and reflected
sign must be propagated through GraphIR, amplitude, D-algebra, poles, and the
contact orbit.  Source-extended BV closure, quantum cohomological status of
\(t_{+++}\in(\tfrac32,0)\), and its coefficient matching to a nonzero
symmetric candidate must be proved.  The \(j_L=\tfrac52\) component is
already removed exactly by the chiral Bianchi identity.  Rank one is required
only for the scalar-coefficient corollary.  The finite-BV density/Jacobian
remains a Step-5C gate and does not block the fixed-vector-frame Step-5A
calculation.  No box/pentagon coefficient is accepted before the Step-5A
identities above are proved.
