# Step 5 exact DRED cutting-failure audit

Status: LOCAL_PROPOSAL__EVANESCENT_EDGE_SQUARE_AND_FINITE_MASTER_REPRODUCED

Authority base: origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66.

This audit corrects the DRED gate in
audits/step5-ab1-standard-feynman-strictification.md. It proves the universal
anomaly-sector calculation for every massless one-loop triangle occurrence
whose four-dimensional superspace \(D\)-word produces an inverse kinetic
square on one internal edge. Source, vertex, color, Wick, orientation, and
residual external-word coefficients remain occurrence data.

## 1. Metric and momentum definitions

Use a four-dimensional spin-algebra projector \(\bar\delta\) and a formal
\((d-4)\)-dimensional projector \(\widetilde\delta\):

$$
d:=4-2\epsilon,
\qquad
\delta_d^{MN}=\bar\delta^{MN}+\widetilde\delta^{MN},
$$

$$
\operatorname{tr}\bar\delta=4,
\qquad
\operatorname{tr}\widetilde\delta=d-4=-2\epsilon,
\qquad
\bar\delta\widetilde\delta=0.
$$

For a full regulated loop momentum,

$$
\ell_d^2=\bar\ell^2+\widetilde\ell^2,
\qquad
\bar\ell^2:=\bar\delta^{MN}\ell_M\ell_N,
\qquad
\widetilde\ell^2:=\widetilde\delta^{MN}\ell_M\ell_N.
$$

Define the positive-trace anomaly numerator by

$$
\boxed{
\mu_\ell^2
:=-\widetilde\ell^2
=\bar\ell^2-\ell_d^2.}
$$

Thus the user's \(d-4\) square and the anomaly numerator obey

$$
\boxed{
\widehat\ell_{\rm user}^{\,2}:=\widetilde\ell^2,
\qquad
\mu_\ell^2=-\widehat\ell_{\rm user}^{\,2}.}
$$

Neither symbol is the hatted loop square in the older Project proposal.  The
older Q4S/QDS representation is

$$
\delta_4=\widehat\delta+\breve\delta,
\qquad
\breve\delta=\delta_4-\widehat\delta,
\qquad
\operatorname{tr}\breve\delta=4-d=2\epsilon.
$$

Together with \(\breve\delta^M{}_N\ell^N=0\), it gives

$$
\delta_4(\ell,\ell)=\widehat\delta(\ell,\ell)=\ell_d^2.
$$

Therefore \(\bar\delta\) is not \(\delta_4\), and
\(\widetilde\delta\) is not \(-\breve\delta\) as an operator identity.  The
scalar dimension-shift representation is a distinct regulator axiom: the
finite superspace spin word contracts with \(\bar\delta\), whereas the
propagator inverse contracts with \(\delta_d\).  The two representations must
not be combined to erase

$$
\mu_\ell^2=\bar\ell^2-\ell_d^2
$$

before the Schwinger family is summed.

All external momenta are four-dimensional:

$$
\widetilde p=\widetilde q=0.
$$

For any internal edge

$$
r_e=\ell+K_e,
\qquad
K_e\in\operatorname{im}\bar\delta,
$$

one has

$$
\widetilde r_e=\widetilde\ell,
\qquad
\bar r_e^{\,2}-r_{e,d}^{\,2}
=-\widetilde\ell^2
=\mu_\ell^2.
$$

## 2. Four-dimensional \(D\)-algebra square

The mixed derivative anticommutator and sigma contraction are
four-dimensional:

$$
\{D_a,\bar D_{\dot a}\}=2r_{a\dot a},
\qquad
r_{a\dot a}:=\sigma^M_{a\dot a}\bar\delta_M{}^Nr_N,
$$

$$
\sigma^M_{a\dot a}\bar\sigma^{N\dot a a}
=2\bar\delta^{MN}.
$$

Therefore

$$
\begin{aligned}
\frac18
\{D_a,\bar D_{\dot a}\}
\{D^a,\bar D^{\dot a}\}
&=\frac18(2r_{a\dot a})(2r^{a\dot a})\\
&=\frac12r_{a\dot a}r^{a\dot a}\\
&=\frac12
\left(2\bar\delta^{MN}r_Mr_N\right)\\
&=\boxed{\bar r^{\,2}}.
\end{aligned}
$$

Equivalently,

$$
\bar D^2D^2\bar D^2
=16\bar\Box\,\bar D^2,
\qquad
D^2\bar D^2D^2
=16\bar\Box\,D^2,
$$

where

$$
\bar\Box\longmapsto-\bar r^{\,2}.
$$

Replacing \(\bar\Box\) by the full \(d\)-dimensional \(\Box_d\) inside
the \(D\)-algebra is the premature dimensional-continuation error.

For the \(B_1\)-descendant placement on a chiral edge,

$$
\nabla_-\nabla_+=\frac12\nabla^2,
$$

and the edge word reduces as

$$
\begin{aligned}
\frac1{16r_{e,d}^2}
D_-D_+\bar D^2D^2\delta
&=\frac1{32r_{e,d}^2}
D^2\bar D^2D^2\delta\\
&=\frac{\bar\Box_e}{2r_{e,d}^2}D^2\delta\\
&=-\frac12
\frac{\bar r_e^{\,2}}{r_{e,d}^2}D^2\delta\\
&=-\frac12D^2\delta
-\frac12
\frac{\mu_\ell^2}{r_{e,d}^2}D^2\delta.
\end{aligned}
$$

The first term is the exact Schwinger cut. The second is the anomaly-sector
edge word.

## 3. Occurrence-by-occurrence Schwinger cut

Let

$$
D_i:=r_{i,d}^{\,2},
\qquad
\{i,j,k\}=\{0,1,2\}.
$$

After the graph-specific \(D\)-word has selected edge \(i\), factor out its
complete residual coefficient and external word as \(C_G\mathcal R_G\). The
parent and its Schwinger cut are

$$
\Gamma_{G,i}^{\rm parent}
=C_G\mathcal R_G
\int_\ell
\frac{\bar r_i^{\,2}}{D_0D_1D_2},
$$

$$
\Gamma_{G,i}^{\rm cut}
=-C_G\mathcal R_G
\int_\ell
\frac1{D_jD_k}.
$$

The relative sign and equal coefficient are fixed by the regulated local
Schwinger equation, not by a separate contact-residue hypothesis. If the
numerator were the full inverse propagator, the cancellation would be
pointwise:

$$
\begin{aligned}
\Gamma_{G,i}^{(d)}
&=C_G\mathcal R_G
\int_\ell
\left[
\frac{D_i}{D_0D_1D_2}
-\frac1{D_jD_k}
\right]\\
&=C_G\mathcal R_G
\int_\ell
\left[
\frac1{D_jD_k}
-\frac1{D_jD_k}
\right]\\
&=\boxed{0}.
\end{aligned}
$$

The actual four-dimensional \(D\)-algebra gives

$$
\begin{aligned}
\Gamma_{G,i}^{\rm parent+cut}
&=C_G\mathcal R_G
\int_\ell
\left[
\frac{\bar r_i^{\,2}}{D_0D_1D_2}
-\frac1{D_jD_k}
\right]\\
&=C_G\mathcal R_G
\int_\ell
\frac{\bar r_i^{\,2}-r_{i,d}^{\,2}}
{D_0D_1D_2}\\
&=\boxed{
C_G\mathcal R_G
\int_\ell
\frac{\mu_\ell^2}
{D_0D_1D_2}}.
\end{aligned}
$$

Thus one cuts only the edge selected by the actual \(D\)-word. An untyped
three-cuts-per-skeleton table is not the anomaly derivation.

For the four current \(AB_1\) parents, the species routes are

$$
G_1:(\Phi_1,V,V),
\qquad
G_2:(\Phi_1,\Phi_1,V),
$$

$$
G_{3,2}:(V,\Phi_2,\Phi_1),
\qquad
G_{3,3}:(V,\Phi_3,\Phi_1).
$$

Whenever the \(B_1\)-descendant word acts on its chiral edge, Section 2 gives
the displayed edge split directly. For the \(A\)-descendant placement,

$$
\nabla_-A=-\nabla_+\mathscr E_V-2i(B_s\times C_s),
$$

and the \(\mathscr E_V\)-adjacent vector edge gives the same
\(\bar\Box_e/\Box_{d,e}\) split. The nonlinear \(B_s\times C_s\) term belongs
to the matched contact family.

### 3.1 Direct-Wick prefactors for the ordered \(AB_1\) parents

For the direct normalized expectation value, no odd source derivative is
introduced.  The leading physical insertion is

$$
\begin{aligned}
\mathcal O_{\rm phys}^{(0),AB}
&=g^2A_c^{(0),A}B_{1,c}^{(0),B}\\
&=-\frac{g^2}{4\sqrt2}
\bigl(D_+\bar D^2D_+u\bigr)^A
\bigl(D_+\phi_1\bigr)^B.
\end{aligned}
$$

Hence

$$
C_I=-\frac{g^2}{4\sqrt2}.
$$

For two distinct labeled action vertices,

$$
\frac1{2!}\left(S_1S_2+S_2S_1\right)=S_1S_2,
\qquad
w_{\rm Wick}=1.
$$

The \(G_2\) propagator product is

$$
(-\hbar)
\left(\frac{\hbar}{16}\right)
\left(\frac{\hbar}{16}\right)
=-\frac{\hbar^3}{256}.
$$

The two matter exponent vertices give

$$
\left(\frac{\sqrt2g}{\hbar}\right)^2
=\frac{2g^2}{\hbar^2}.
$$

Therefore, before the \(D\)-word and color reduction,

$$
\begin{aligned}
C_{G_2}^{\rm preD}
&=\left(-\frac{g^2}{4\sqrt2}\right)
\left(\frac{2g^2}{\hbar^2}\right)
\left(-\frac{\hbar^3}{256}\right)\\
&=\boxed{\frac{\sqrt2\,\hbar g^4}{1024}}.
\end{aligned}
$$

For \(G_{3,r}\), the matter and antichiral-cubic exponent vertices give

$$
\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\varepsilon_{1rt}\right)
=-\frac{2g^2}{\hbar^2}\varepsilon_{1rt}.
$$

Thus

$$
\begin{aligned}
C_{G_{3,r}}^{\rm preD}
&=\left(-\frac{g^2}{4\sqrt2}\right)
\left(-\frac{2g^2}{\hbar^2}\varepsilon_{1rt}\right)
\left(-\frac{\hbar^3}{256}\right)\\
&=\boxed{-\frac{\sqrt2\,\hbar g^4}{1024}
\varepsilon_{1rt}}.
\end{aligned}
$$

Consequently,

$$
\boxed{
C_{G_{3,2}}^{\rm preD}
=-\frac{\sqrt2\,\hbar g^4}{1024},
\qquad
C_{G_{3,3}}^{\rm preD}
=+\frac{\sqrt2\,\hbar g^4}{1024}.}
$$

The exact adjoint color reductions are

$$
\boxed{
(T_E)^B{}_X(T_A)^X{}_D
=-\mathbb F^{AB}{}_{DE},}
$$

$$
\boxed{
(T_A)^D{}_Xc_{BXE}
=i\mathbb F^{AB}{}_{DE}.}
$$

For one labeled term in the \(+\)-chiral ordered \(VVV\) Hessian,

$$
\left(\frac{i\sqrt2g}{\hbar}\right)
\left(-\frac{i\sqrt2g}{256\hbar}\right)
=\frac{g^2}{128\hbar^2},
$$

while two vector and one chiral propagator give

$$
(-\hbar)^2\left(\frac{\hbar}{16}\right)
=\frac{\hbar^3}{16}.
$$

Therefore

$$
\boxed{
C_{G_1,+,\pi,a}^{\rm preD}
=-\frac{\hbar g^4}{8192\sqrt2}}
$$

for each \(\pi\in S_3\) and each of the two displayed derivative placements
\(a\).  The antichiral Hessian reverses this sign:

$$
\boxed{
C_{G_1,-,\pi,a}^{\rm preD}
=+\frac{\hbar g^4}{8192\sqrt2}.}
$$

There is no additional \(N_{VVV}\): the six label permutations and two
placements are the ordered Hessian itself.  These prefactors do not yet
replace the occurrence-resolved residual \(D\)-words.

## 4. Exact finite master integral

Define

$$
I_n(\Delta)
:=\mu^{2\epsilon}
\int\frac{d^dL}{(2\pi)^d}
\frac1{(L^2+\Delta)^n}.
$$

Schwinger parametrization gives

$$
I_n(\Delta)
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}{\Gamma(n)}
\Delta^{d/2-n}.
$$

In particular,

$$
I_2
=\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon},
$$

$$
\begin{aligned}
\Delta I_3
&=\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(1+\epsilon)}2\Delta^{-\epsilon}\\
&=\frac\epsilon2
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\Delta^{-\epsilon}\\
&=\frac\epsilon2I_2.
\end{aligned}
$$

Rotational reduction gives

$$
\int_L
\frac{L^ML^N}{(L^2+\Delta)^3}
=\frac{\delta_d^{MN}}d
\left(I_2-\Delta I_3\right).
$$

Contracting with \(-\widetilde\delta_{MN}\),

$$
\begin{aligned}
J_{\rm ev}(\Delta)
&:=\int_L
\frac{\mu_L^2}
{(L^2+\Delta)^3}\\
&=\frac{4-d}{d}
\left(I_2-\Delta I_3\right)\\
&=\frac{2\epsilon}{4-2\epsilon}
\left(1-\frac\epsilon2\right)I_2\\
&=\frac{2\epsilon}{4-2\epsilon}
\frac{2-\epsilon}{2}I_2\\
&=\frac\epsilon2I_2\\
&=\frac{\Gamma(1+\epsilon)}
{2(4\pi)^{2-\epsilon}}
\left(\frac{\mu^2}{\Delta}\right)^\epsilon.
\end{aligned}
$$

Hence

$$
\boxed{
\lim_{\epsilon\to0}J_{\rm ev}(\Delta)
=\frac1{32\pi^2}.}
$$

For

$$
D_0=\ell^2,
\qquad
D_1=(\ell+p)^2,
\qquad
D_2=(\ell+p+q)^2,
$$

Feynman parametrization gives

$$
\frac1{D_0D_1D_2}
=2\int_0^1dy\int_0^{1-y}dz
\frac1{(L^2+\Delta)^3}.
$$

The shift \(L=\ell+K(y,z;p,q)\) is four-dimensional, so

$$
\mu_L^2=\mu_\ell^2.
$$

Since

$$
2\int_0^1dy\int_0^{1-y}dz\,1
=2\int_0^1(1-y)dy
=2\left(1-\frac12\right)
=1,
$$

the complete triangle unit is

$$
\boxed{
\lim_{\epsilon\to0}
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}
{D_0D_1D_2}
=\frac1{32\pi^2}.}
$$

For the reverse subtraction, cut minus parent, the unit is

$$
-\frac1{32\pi^2}.
$$

### 4.1 Rank-one and rank-two moments

For the centered denominator, rotational invariance gives

$$
\int_L\frac{\mu_L^2L^\mu}{(L^2+\Delta)^3}=0.
$$

For the rank-two moment, the fourth-moment reduction is

$$
\int_L
\frac{L^ML^NL^PL^Q}{(L^2+\Delta)^3}
=\frac{\delta_d^{MN}\delta_d^{PQ}
+\delta_d^{MP}\delta_d^{NQ}
+\delta_d^{MQ}\delta_d^{NP}}
{d(d+2)}
\int_L\frac{(L^2)^2}{(L^2+\Delta)^3}.
$$

Contracting the first pair with $-\widetilde\delta_{MN}$ and taking
$\mu,\nu$ in the four-dimensional spin space gives

$$
J_{\rm ev}^{\mu\nu}(\Delta)
:=\int_L\frac{\mu_L^2L^\mu L^\nu}{(L^2+\Delta)^3}
=\frac{4-d}{d(d+2)}\bar\delta^{\mu\nu}
\left(I_1-2\Delta I_2+\Delta^2I_3\right).
$$

Since

$$
\frac{I_1-2\Delta I_2+\Delta^2I_3}{\Delta I_2}
=\frac{(\epsilon-3)(\epsilon-2)}{2(\epsilon-1)},
$$

one obtains

$$
\boxed{
\lim_{\epsilon\to0}J_{\rm ev}^{\mu\nu}(\Delta)
=-\frac{\Delta}{64\pi^2}\bar\delta^{\mu\nu}.}
$$

For the routing

$$
D_0=\ell^2,
\qquad
D_1=(\ell+p)^2,
\qquad
D_2=(\ell+p+q)^2,
$$

set

$$
x:=1-y-z,
\qquad
K:=(y+z)p+zq,
\qquad
L:=\ell+K,
$$

$$
\Delta=xy,p^2+xz,(p+q)^2+yz,q^2.
$$

Then

$$
\boxed{
\int_\ell\frac{\mu_\ell^2\ell^\mu}{D_0D_1D_2}
=-\frac{2p^\mu+q^\mu}{96\pi^2}.}
$$

The complete rank-two result is

$$
\boxed{
\begin{aligned}
\int_\ell\frac{\mu_\ell^2\ell^\mu\ell^\nu}{D_0D_1D_2}
={}&\frac{p^\mu p^\nu}{64\pi^2}
+\frac{p^\mu q^\nu+q^\mu p^\nu}{128\pi^2}
+\frac{q^\mu q^\nu}{192\pi^2}\\
&-\frac{\bar\delta^{\mu\nu}}{384\pi^2}
\left(p^2+p\cdot q+q^2\right).
\end{aligned}}
$$

The signs of the rank-one coefficients change only when the graph routing
defines its unshifted loop momentum with the opposite sign.

## 5. Correction of the AB1 gate

The old gate asserted that an occurrence must independently produce a scalar
\(4-d\) numerator. The correct implication is

$$
\boxed{
\text{four-dimensional }D\text{-algebra square}
\quad+\quad
\text{full }d\text{-dimensional Schwinger cut}
\quad\Longrightarrow\quad
\mu_\ell^2.}
$$

The factor \(4-d\) is generated automatically when the evanescent square is
integrated:

$$
-\operatorname{tr}\widetilde\delta=4-d=2\epsilon.
$$

The graph-specific calculation must still determine

$$
C_G\mathcal R_G
=C_{\rm source}C_{\rm vertices}C_{\rm Wick}
C_{\rm color}C_{\rm orientation}C_{D,\rm residual}
\mathcal R_G,
$$

and must identify which internal edge receives \(\bar r_e^{\,2}\). It does
not have to manufacture an additional \(4-d\) scalar.

## 6. Derivation-gap verdicts

| ID | class | severity | finding | verdict |
| --- | --- | --- | --- | --- |
| DRED-CUT-G1 | G-PROJ | P0 | the AB1 audit made \(4-d\) conditional on a graph-specific scalar trace | FIXED_BY_EDGE_SQUARE_DERIVATION |
| DRED-CUT-G2 | G-DEF | P0 | the older hatted/breve notation was conflated with the user's \(d-4\) square | FIXED_BY_EXPLICIT_NOTATION_MAP |
| DRED-CUT-G3 | G-ALG | P0 | the full inverse-propagator cancellation was not displayed before integration | FIXED_POINTWISE |
| DRED-CUT-G4 | G-NORM | P0 | the Feynman factor \(2\), simplex area \(1/2\), and finite unit were not kept in one chain | FIXED_EXACTLY |
| DRED-CUT-G5 | G-OP | P0 | the occurrence-resolved \(G_1,G_2,G_{3,2},G_{3,3}\) residual words and coefficients are not all reduced | OPEN |

The universal anomaly-sector mechanism and its finite master integral are
reproduced. A complete ordered \(AB_1\) coefficient still requires the last
row.
