# Step 5. Euclidean \(\mathcal N=4\) AWI supergraphs

## 5.0 Status

$$
\boxed{\texttt{FROZEN}:\quad
\text{notation, DRED, physical Euler operators, letters, tree descendants}.}
\tag{5.0}
$$

No one-loop coefficient is accepted in this status.

## 5.1 Spin frame, Fourier transform, order

$$
+\equiv1,
\qquad
-\equiv2,
\qquad
\epsilon^{+-}=+1,
\qquad
\epsilon_{+-}=-1.
\tag{5.1}
$$

$$
\chi^+=\chi_-,
\qquad
\chi^-=-\chi_+,
\qquad
\nabla^+=\nabla_-,
\qquad
\nabla^-=-\nabla_+.
\tag{5.2}
$$

$$
\nabla^2:=\nabla^a\nabla_a
=2\nabla_-\nabla_+,
\qquad
\bar\nabla^2:=\bar\nabla_{\dot a}\bar\nabla^{\dot a}.
\tag{5.3}
$$

$$
F(x)=\int\frac{d^dp}{(2\pi)^d}e^{ip\cdot x}F(p),
\qquad
\partial_mF(p)=ip_mF(p),
\qquad
d=4-2\epsilon.
\tag{5.4}
$$

Every vertex is all-incoming:

$$
\sum_{e\in\operatorname{Inc}(v)}p_e=0.
\tag{5.5}
$$

The loop measure is

$$
\int_k:=\mu^{2\epsilon}
\int\frac{d^dk}{(2\pi)^d}.
\tag{5.6}
$$

The DRED continuation of the Project superspace measures is

$$
\begin{aligned}
\int_{E,8}^{(d)}Y
&:=\int d^dx\,[Y]_D,\\
\int_{E,+}^{(d)}X
&:=\int d^dx\,[X]_F,\\
\int_{E,-}^{(d)}\widetilde X
&:=\int d^dx\,[\widetilde X]_{\widetilde F}.
\end{aligned}
\tag{5.6a}
$$

The \(\vartheta,\bar\vartheta\), sigma-matrix, and spinor-index algebra remains
four-dimensional.  This contract uses the stripped-vertex convention: no
\(\mu\)-power is attached to an action vertex or propagator, and exactly the
single factor \(\mu^{2\epsilon}\) in (5.6) is attached to each independent
loop-momentum integration.

Every \(\int_{E,8}\), \(\int_{E,+}\), and \(\int_{E,-}\) below denotes
(5.6a), and every vertex carries a \((2\pi)^d\delta^d(\sum p_e)\).

The Grassmann normal order is

$$
\vartheta^+\vartheta^-\bar\vartheta_{\dot+}
\bar\vartheta_{\dot-},
\tag{5.7}
$$

and every color word, flavor word, spinor word, field word, and
functional-derivative word retains its displayed order.

## 5.2 Euclidean bispinors

$$
p_{a\dot a}:=(\sigma_E^m)_{a\dot a}p_m,
\qquad
p_a{}^{\dot a}:=\epsilon^{\dot a\dot b}p_{a\dot b}.
\tag{5.8}
$$

From (1.52)--(1.54), without a Fierz rearrangement,

$$
(\sigma_E^m)_{a\dot a}
(\sigma_E^n)_b{}^{\dot a}
+(\sigma_E^n)_{a\dot a}
(\sigma_E^m)_b{}^{\dot a}
=-2\epsilon_{ab}\delta_{(4)}^{mn}.
\tag{5.9}
$$

Hence

$$
p_{+\dot a}p_-{}^{\dot a}
=-\epsilon_{+-}\delta_{(4)}^{mn}p_mp_n
=p_{(4)}^2.
\tag{5.10}
$$

The symbol on the right of (5.10) is a four-spin-metric contraction;
it is not replaced by an untyped \(p^2\).

## 5.3 DRED metric contract

$$
\delta_{(4)}^{mn}=\widehat\delta^{mn}+\widetilde\delta^{mn},
\qquad
\widehat\delta\widetilde\delta=0,
\qquad
\widehat\delta^2=\widehat\delta,
\qquad
\widetilde\delta^2=\widetilde\delta.
\tag{5.11}
$$

$$
\delta_{(4)m}{}^m=4,
\qquad
\widehat\delta_m{}^m=d=4-2\epsilon,
\qquad
\widetilde\delta_m{}^m=2\epsilon.
\tag{5.12}
$$

The loop momentum is restricted by

$$
k^m=\widehat\delta^m{}_nk^n,
\qquad
k_{\widehat{\ }}^2:=\widehat\delta^{mn}k_mk_n,
\qquad
k_{(4)}^2:=\delta_{(4)}^{mn}k_mk_n=k_{\widehat{\ }}^2.
\tag{5.13}
$$

Every routed loop and external momentum lies in the same regulated momentum
space:

$$
v^m=\widehat\delta^m{}_nv^n,
\qquad
v\in\{k,p,q,p+q,r_0,r_1,r_2,\ell\}.
\tag{5.13a}
$$

For these momenta only,

$$
v^2:=\widehat\delta^{mn}v_mv_n
=\delta_{(4)}^{mn}v_mv_n.
\tag{5.13b}
$$

Spinor and \(D\)-algebra use \(\delta_{(4)}\); tensor integration uses
\(\widehat\delta\):

$$
\int_k k^mk^n f(k^2)
=\frac{\widehat\delta^{mn}}d
\int_k k^2f(k^2).
\tag{5.14}
$$

If independently derived graph terms have tensor coefficients
\(+C\widehat\delta^{mn}\) and \(-C\delta_{(4)}^{mn}\), their sum is

$$
\widehat\delta^{mn}-\delta_{(4)}^{mn}
=-\widetilde\delta^{mn}.
\tag{5.15}
$$

The complete graph census determines whether this cancellation occurs; (5.15)
alone is not an anomaly calculation.

No factor of \(\epsilon\) is inserted into a bare numerator.

For the fixed three-edge routing

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+p+q,
\tag{5.15a}
$$

set \(x+y+z=1\).  Direct expansion gives

$$
\begin{aligned}
xr_0^2+yr_1^2+zr_2^2
&=k^2+2k\cdot\big[yq+z(p+q)\big]
+yq^2+z(p+q)^2\\
&=\ell^2+\Delta,
\end{aligned}
\tag{5.15b}
$$

where

$$
\ell:=k+yq+z(p+q),
\qquad
\boxed{\Delta=xyq^2+xz(p+q)^2+yzp^2.}
\tag{5.15c}
$$

The integral derivation is first performed in the nonexceptional Euclidean
domain

$$
p^2>0,
\qquad
q^2>0,
\qquad
(p+q)^2>0,
\qquad
\Delta>0
\tag{5.15c.1}
$$

for every interior simplex point.  Other nonexceptional momenta are reached by
analytic continuation of the exact parameter integral.

The exact parameter identity is

$$
\frac1{r_0^2r_1^2r_2^2}
=2\int_0^1dx\int_0^{1-x}dy\,
\frac1{(\ell^2+\Delta)^3},
\qquad z=1-x-y.
\tag{5.15d}
$$

Define

$$
A_0:=\frac1{16\pi^2},
\qquad
L_\Delta:=\log\frac{4\pi\mu^2}{\Delta}-\gamma_E.
\tag{5.15e}
$$

The master integral is

$$
\boxed{
J_{a,n}(\Delta)
:=\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{(\ell^2)^a}{(\ell^2+\Delta)^n}
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(a+d/2)\Gamma(n-a-d/2)}
{\Gamma(d/2)\Gamma(n)}
\Delta^{a+d/2-n}.}
\tag{5.15e.1}
$$

Equation (5.15e.1) follows from

$$
\frac1{(\ell^2+\Delta)^n}
=\frac1{\Gamma(n)}\int_0^\infty ds\,
s^{n-1}e^{-s(\ell^2+\Delta)},
\tag{5.15e.2}
$$

$$
\int d^d\ell\,(\ell^2)^ae^{-s\ell^2}
=\pi^{d/2}s^{-a-d/2}
\frac{\Gamma(a+d/2)}{\Gamma(d/2)},
\tag{5.15e.3}
$$

followed by the remaining Gamma integral in \(s\).

The dimensionally regulated scalar integrals are

$$
J_{0,2}(\Delta)
:=\int_\ell\frac1{(\ell^2+\Delta)^2}
=A_0\left[\frac1\epsilon+L_\Delta+O(\epsilon)\right],
\tag{5.15f}
$$

$$
J_{0,3}(\Delta)
:=\int_\ell\frac1{(\ell^2+\Delta)^3}
=\frac{A_0}{\Delta}
\left[\frac12+\frac\epsilon2L_\Delta+O(\epsilon^2)\right],
\tag{5.15g}
$$

$$
\begin{aligned}
J_{1,3}(\Delta)
&:=\int_\ell\frac{\ell^2}{(\ell^2+\Delta)^3}\\
&=J_{0,2}(\Delta)-\Delta J_{0,3}(\Delta)\\
&=A_0\left[\frac1\epsilon+L_\Delta-\frac12+O(\epsilon)\right].
\end{aligned}
\tag{5.15h}
$$

Thus

$$
\boxed{
\int_\ell\frac{\ell^m\ell^n}{(\ell^2+\Delta)^3}
=\frac{\widehat\delta^{mn}}dJ_{1,3}(\Delta)
=\frac{A_0\widehat\delta^{mn}}4
\left[\frac1\epsilon+L_\Delta+O(\epsilon)\right].}
\tag{5.15i}
$$

## 5.4 Physical action and ordered Euler operators

Set

$$
h=g^{-2},
\qquad
f_{AB}=\widetilde f_{AB}=h\kappa_{AB},
\qquad
\mathfrak k_{AB}=0,
\tag{5.16}
$$

in the accepted Euclidean action (4C.4).  The intrinsic Euclidean pairs

$$
(\boldsymbol\Phi_r,\widetilde{\boldsymbol\Phi}_r),
\qquad
(\boldsymbol{\mathcal W}_a,
\widetilde{\boldsymbol{\mathcal W}}_{\dot a})
\tag{5.17}
$$

remain independent.

For

$$
\Xi:=\mathcal E^{-1}\delta\mathcal E,
\qquad
\boldsymbol\Xi:=\mathcal B\Xi\mathcal B^{-1},
\qquad
(X\times Y)^A:=c_{BC}{}^AX^BY^C,
\tag{5.18}
$$

Use the Step-3C bridge order

$$
\mathcal E=\widetilde{\mathcal B}\mathcal B,
\qquad
\boldsymbol\Phi=\mathcal B\Phi,
\qquad
\widetilde{\boldsymbol\Phi}
=\widetilde\Phi\widetilde{\mathcal B}.
\tag{5.18a}
$$

Then

$$
\widetilde{\boldsymbol\Phi}\boldsymbol\Phi
=\widetilde\Phi\mathcal E\Phi.
\tag{5.18b}
$$

Every gauge variation of the gauge-chiral action holds
\((\Phi,\widetilde\Phi)\) fixed:

$$
\begin{aligned}
\delta_{\mathcal E}
(\widetilde\Phi\mathcal E\Phi)
&=\widetilde\Phi\mathcal E\Xi\Phi\\
&=\widetilde{\boldsymbol\Phi}
(\mathcal B\Xi\mathcal B^{-1})
\boldsymbol\Phi\\
&=\widetilde{\boldsymbol\Phi}
\boldsymbol\Xi\boldsymbol\Phi.
\end{aligned}
\tag{5.18c}
$$

the full-superspace/chiral conversion is

$$
\int_{E,8}Y
=\int_{E,+}\left(-\frac14\bar\nabla^2Y\right)
=\int_{E,-}\left(-\frac14\nabla^2Y\right).
\tag{5.19}
$$

The second equality uses regulated test superfields with sufficient decay in the
\(d\)-dimensional momentum-coordinate domain:

$$
\int d^dx\,\partial_{\widehat m}Y^{\widehat m}=0.
\tag{5.19a}
$$

This spacetime condition is distinct from the finite coefficient-space cycle
condition used in the Schwinger equation.

The three ordered derivatives of (4C.13) give

$$
\begin{aligned}
\frac{\vec\partial\mathscr U_4}{\partial\Phi_u^D}
=-\frac{\sqrt2h}{6}\big(&
\varepsilon_{ust}c_{DBC}
+\varepsilon_{sut}c_{BDC}
+\varepsilon_{stu}c_{BCD}\big)\Phi_s^B\Phi_t^C\\
=-\frac{\sqrt2h}{2}
\varepsilon_{ust}c_{DBC}\Phi_s^B\Phi_t^C.
\end{aligned}
\tag{5.20}
$$

The three coefficients coincide because

$$
\varepsilon_{sut}c_{BDC}
=(-\varepsilon_{ust})(-c_{DBC})
=\varepsilon_{ust}c_{DBC},
\tag{5.20a}
$$

$$
\varepsilon_{stu}c_{BCD}
=\varepsilon_{ust}c_{DBC}.
\tag{5.20b}
$$

Thus

$$
\boxed{
\mathfrak E_{\Phi,uD}^{\rm phys}
=\frac h4\kappa_{DA}\bar\nabla^2\widetilde\Phi_u^A
+\frac{\sqrt2h}{2}\varepsilon_{ust}c_{DBC}
\Phi_s^B\Phi_t^C,}
\tag{5.21}
$$

$$
\boxed{
\widetilde{\mathfrak E}_{\Phi,uD}^{\rm phys}
=\frac h4\kappa_{DA}\nabla^2\Phi_u^A
+\frac{\sqrt2h}{2}\varepsilon_{ust}c_{DBC}
\widetilde\Phi_s^B\widetilde\Phi_t^C.}
\tag{5.22}
$$

The exact gauge-field variations are

$$
\delta\mathcal W_a
=-\frac18\bar\nabla^2\nabla_a\Xi,
\qquad
\delta\widetilde{\mathcal W}_{\dot a}
=-\frac18\nabla^2\bar\nabla_{\dot a}
(\delta\mathcal E\,\mathcal E^{-1}).
\tag{5.23}
$$

Using (3C.43), the two gauge kinetic terms give

$$
\begin{aligned}
\delta S_{W,+}
&=-\frac h2\int_{E,+}
\delta\mathcal W^a\mathcal W_a\\
&=-\frac h4\int_{E,8}
(\boldsymbol\nabla^a\boldsymbol\Xi)
\boldsymbol{\mathcal W}_a\\
&=+\frac h4\int_{E,8}
\boldsymbol\Xi\boldsymbol\nabla^a
\boldsymbol{\mathcal W}_a.
\end{aligned}
\tag{5.23a}
$$

For

$$
\widetilde{\boldsymbol\Xi}
:=\widetilde{\mathcal B}^{-1}
(\delta\mathcal E\,\mathcal E^{-1})
\widetilde{\mathcal B}
=\mathcal B\Xi\mathcal B^{-1}
=\boldsymbol\Xi,
\tag{5.23b}
$$

the tilded term is

$$
\begin{aligned}
\delta S_{W,-}
&=-\frac h4\int_{E,8}
(\bar{\boldsymbol\nabla}_{\dot a}
\widetilde{\boldsymbol\Xi})
\widetilde{\boldsymbol{\mathcal W}}^{\dot a}\\
&=+\frac h4\int_{E,8}
\widetilde{\boldsymbol\Xi}
\bar{\boldsymbol\nabla}_{\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\dot a}.
\end{aligned}
\tag{5.23c}
$$

Index raising and (3C.43) give

$$
\bar{\boldsymbol\nabla}_{\dot a}
\widetilde{\boldsymbol{\mathcal W}}^{\dot a}
=-\bar{\boldsymbol\nabla}^{\dot a}
\widetilde{\boldsymbol{\mathcal W}}_{\dot a}
=\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a.
\tag{5.23d}
$$

Equations (5.23a)--(5.23d) give

$$
\delta S_{W,E}
=\frac h2\int_{E,8}\kappa_{AB}
\boldsymbol\Xi^A
\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a^B.
\tag{5.24}
$$

The matter density gives

$$
\begin{aligned}
\delta_\Xi S_{K,E}
&=-h\int_{E,8}\kappa_{AB}
\widetilde{\boldsymbol\Phi}_r^A
\big(\boldsymbol\Xi^D T_D^{\rm ad}\big)^B{}_C
\boldsymbol\Phi_r^C\\
&=-ih\int_{E,8}\boldsymbol\Xi^D
c_{DCA}\widetilde{\boldsymbol\Phi}_r^A
\boldsymbol\Phi_r^C\\
&=-ih\int_{E,8}\kappa_{DB}\boldsymbol\Xi^D
(\boldsymbol\Phi_r\times
\widetilde{\boldsymbol\Phi}_r)^B.
\end{aligned}
\tag{5.24a}
$$

Here

$$
c_{DCA}=c_{CAD}=\kappa_{DB}c_{CA}{}^B,
\tag{5.24b}
$$

and both matter superfields are even.  Therefore

$$
\delta_\Xi S_{K,E}
=-ih\int_{E,8}\kappa_{AB}\boldsymbol\Xi^A
(\boldsymbol\Phi_r\times
\widetilde{\boldsymbol\Phi}_r)^B.
\tag{5.25}
$$

Therefore

$$
\boxed{
\boldsymbol{\mathfrak E}_{\boldsymbol\Xi,A}^{\rm phys}
=h\kappa_{AB}\left[
\frac12\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a^B
-i(\boldsymbol\Phi_r\times
\widetilde{\boldsymbol\Phi}_r)^B
\right].}
\tag{5.26}
$$

The gauge-chiral-frame Euler operator used for ordered prepotential
differentiation is

$$
\mathfrak E_\Xi^{\mathsf C}
:=\mathcal B^{-1}
\boldsymbol{\mathfrak E}_{\boldsymbol\Xi}^{\rm phys}
\mathcal B.
\tag{5.26a}
$$

Define normalized Euler operators

$$
\widetilde{\boldsymbol{\mathfrak E}}_{\Phi,uD}
:=\mathcal B
\widetilde{\mathfrak E}_{\Phi,uD}^{\rm phys}
\mathcal B^{-1},
\tag{5.26b}
$$

where the coadjoint color slot is identified with the adjoint slot by
\(\kappa^{AB}\).  Then

$$
\begin{aligned}
\mathcal G^A
&:=2h^{-1}\kappa^{AB}
\boldsymbol{\mathfrak E}_{\boldsymbol\Xi,B}^{\rm phys}
=\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a^A
-2i(\boldsymbol\Phi_r\times
\widetilde{\boldsymbol\Phi}_r)^A,\\
\widetilde{\mathcal C}_u^A
&:=4h^{-1}\kappa^{AD}
\widetilde{\boldsymbol{\mathfrak E}}_{\Phi,uD}
=\boldsymbol\nabla^2\boldsymbol\Phi_u^A
+2\sqrt2\varepsilon_{ust}
(\widetilde{\boldsymbol\Phi}_s\times
\widetilde{\boldsymbol\Phi}_t)^A.
\end{aligned}
\tag{5.27}
$$

The prepotential Euler operator retains every insertion vertex:

$$
\Xi
=F(\operatorname{ad}_{\mathcal V})\delta\mathcal V,
\qquad
F(z):=\frac{1-e^{-z}}z.
\tag{5.28a}
$$

Invariant color pairing gives, in the displayed order,

$$
\operatorname{tr}_\kappa
\big(X\operatorname{ad}_{\mathcal V}Y\big)
=-\operatorname{tr}_\kappa
\big((\operatorname{ad}_{\mathcal V}X)Y\big),
\tag{5.28b}
$$

therefore

$$
F(\operatorname{ad}_{\mathcal V})^{\mathsf T}
=F(-\operatorname{ad}_{\mathcal V})
=\frac{e^{\operatorname{ad}_{\mathcal V}}-1}
{\operatorname{ad}_{\mathcal V}}.
\tag{5.28c}
$$

Thus

$$
\delta S_E
=\operatorname{tr}_\kappa
\left(\mathfrak E_\Xi^{\mathsf C}
F(\operatorname{ad}_{\mathcal V})\delta\mathcal V\right)
=\operatorname{tr}_\kappa
\left(F(-\operatorname{ad}_{\mathcal V})
\mathfrak E_\Xi^{\mathsf C}\,\delta\mathcal V\right).
\tag{5.28d}
$$

$$
\boxed{
\mathfrak E_{\mathcal V}^{\rm phys}
=\frac{e^{\operatorname{ad}_{\mathcal V}}-1}
{\operatorname{ad}_{\mathcal V}}
\mathfrak E_\Xi^{\mathsf C}
=\sum_{n=0}^{\infty}\frac1{(n+1)!}
\operatorname{ad}_{\mathcal V}^{n}\mathfrak E_\Xi^{\mathsf C}.}
\tag{5.28}
$$

At lowest components, (5.21), (5.22), and (5.26) give exactly (4C.42b).

## 5.5 Four letter families

All letters are in the Project vector frame:

$$
\widetilde{\boldsymbol\Phi}_r^A
:=\kappa^{AB}\widetilde{\boldsymbol\Phi}_{r,B},
\qquad
(\boldsymbol\nabla_a
\widetilde{\boldsymbol\Phi}_r)^A
:=\kappa^{AB}
\left[(\boldsymbol\nabla_a)^{\rm row}
\widetilde{\boldsymbol\Phi}_r\right]_B.
\tag{5.28e}
$$

Using (4.6) in the connection term gives

$$
(\boldsymbol\nabla_a
\widetilde{\boldsymbol\Phi}_r)^A
=D_a\widetilde{\boldsymbol\Phi}_r^A
-i\llbracket\boldsymbol{\mathcal A}_a,
\widetilde{\boldsymbol\Phi}_r\rrbracket^A
=0.
\tag{5.28f}
$$

$$
\begin{array}{c|c|c|c}
i&\mathbb L_i&|\mathbb L_i|&\text{free indices}\\ \hline
W&(\boldsymbol\nabla_+
\boldsymbol{\mathcal W}_+)^A&0&A\\
\Phi&(\boldsymbol\nabla_+
\boldsymbol\Phi_r)^A&1&(r,A)\\
\widetilde\Phi&\widetilde{\boldsymbol\Phi}_r^A&0&(r,A)\\
\widetilde W&\widetilde{\boldsymbol{\mathcal W}}_{\dot a}^A&1&(\dot a,A)
\end{array}
\tag{5.29}
$$

No reversed ordered product is identified with its original ordering.

## 5.6 Single-letter \(\nabla_-\) descendants

Since \(\{\boldsymbol\nabla_+,\boldsymbol\nabla_-\}=0\),

$$
\boldsymbol\nabla_-\boldsymbol\nabla_+
\boldsymbol\Phi_r
=\frac12\boldsymbol\nabla^2\boldsymbol\Phi_r.
\tag{5.30}
$$

Moreover,

$$
\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a
=\boldsymbol\nabla_-\boldsymbol{\mathcal W}_+
-\boldsymbol\nabla_+\boldsymbol{\mathcal W}_-,
\tag{5.31}
$$

so

$$
\boldsymbol\nabla_-\boldsymbol\nabla_+
\boldsymbol{\mathcal W}_+
=-\boldsymbol\nabla_+
(\boldsymbol\nabla^a\boldsymbol{\mathcal W}_a).
\tag{5.32}
$$

Equations (5.27), (3C.35), (5.30), and (5.32) give

$$
\boxed{
\begin{aligned}
\mathfrak d\mathbb L_W^A
&:=\boldsymbol\nabla_-\mathbb L_W^A
=-\boldsymbol\nabla_+\mathcal G^A
-2i\boldsymbol\nabla_+
(\boldsymbol\Phi_s\times
\widetilde{\boldsymbol\Phi}_s)^A,\\
\mathfrak d\mathbb L_{\Phi,r}^A
&:=\boldsymbol\nabla_-\mathbb L_{\Phi,r}^A
=\frac12\widetilde{\mathcal C}_r^A
-\sqrt2\varepsilon_{rst}
(\widetilde{\boldsymbol\Phi}_s\times
\widetilde{\boldsymbol\Phi}_t)^A,\\
\mathfrak d\mathbb L_{\widetilde\Phi,r}^A&=0,\\
\mathfrak d\mathbb L_{\widetilde W,\dot a}^A&=0.
\end{aligned}}
\tag{5.33}
$$

The nonlinear terms in (5.33) are the \(\mathcal N=4\) classical differential;
they are not deleted by the physical EOM.

## 5.7 Sixteen ordered tree channels

For every ordered pair,

$$
\boxed{
\mathfrak d(\mathbb L_i\mathbb L_j)
=(\mathfrak d\mathbb L_i)\mathbb L_j
+(-1)^{|\mathbb L_i|}
\mathbb L_i(\mathfrak d\mathbb L_j).}
\tag{5.34}
$$

Writing \(d_W:=\mathfrak d\mathbb L_W\) and
\(d_\Phi:=\mathfrak d\mathbb L_\Phi\), the complete family table is

$$
\begin{array}{c|cccc}
\mathfrak d(\mathbb L_i\mathbb L_j)
&W&\Phi&\widetilde\Phi&\widetilde W\\ \hline
W&d_W\mathbb L_W+\mathbb L_Wd_W
&d_W\mathbb L_\Phi+\mathbb L_Wd_\Phi
&d_W\mathbb L_{\widetilde\Phi}
&d_W\mathbb L_{\widetilde W}\\
\Phi&d_\Phi\mathbb L_W-\mathbb L_\Phi d_W
&d_\Phi\mathbb L_\Phi-\mathbb L_\Phi d_\Phi
&d_\Phi\mathbb L_{\widetilde\Phi}
&d_\Phi\mathbb L_{\widetilde W}\\
\widetilde\Phi&\mathbb L_{\widetilde\Phi}d_W
&\mathbb L_{\widetilde\Phi}d_\Phi
&0&0\\
\widetilde W&-\mathbb L_{\widetilde W}d_W
&-\mathbb L_{\widetilde W}d_\Phi
&0&0
\end{array}.
\tag{5.35}
$$

Every suppressed index in (5.35) is restored by the channel emitter.  A sum is
present only when the index is explicitly bound by
\(\varepsilon_{rst}\), \(c_{AB}{}^C\), \(\kappa_{AB}\), or an
upper/lower spinor contraction.

## 5.8 Project-side flat-superspace operator check

At fixed nonzero Euclidean momentum, represent left multiplication and left
Grassmann differentiation on

$$
\Lambda(\vartheta^+,\vartheta^-,
\bar\vartheta_{\dot+},\bar\vartheta_{\dot-}),
\qquad \dim\Lambda=16.
\tag{5.36}
$$

Direct multiplication of the resulting \(16\times16\) matrices gives

$$
\boxed{
D^a\bar D^2D_a
=8p^2\mathbf1
+\frac12(D^2\bar D^2+\bar D^2D^2),}
\tag{5.37}
$$

$$
\boxed{
D^2\bar D^2D^2=-16p^2D^2,
\qquad
\bar D^2D^2\bar D^2=-16p^2\bar D^2.}
\tag{5.38}
$$

Consequently

$$
\Pi_{1/2}:=\frac{D^a\bar D^2D_a}{8p^2},
\qquad
\Pi_0:=-\frac{D^2\bar D^2+\bar D^2D^2}{16p^2},
\tag{5.39}
$$

satisfy

$$
\Pi_{1/2}^2=\Pi_{1/2},
\qquad
\Pi_0^2=\Pi_0,
\qquad
\Pi_{1/2}\Pi_0=0,
\qquad
\Pi_{1/2}+\Pi_0=\mathbf1.
\tag{5.40}
$$

## 5.9 Perturbative slice and exact current blockers

The perturbative slice is

$$
\mathcal B_{E,\mathrm B}=\widetilde{\mathcal B}_{E,\mathrm B}=1,
\qquad
\mathcal F_+=-\frac14\bar D^2\mathcal V,
\qquad
\mathcal F_-=-\frac14D^2\mathcal V,
\qquad
\alpha=1.
\tag{5.41}
$$

The free Hessian point is

$$
\mathcal V_{\mathrm B}=0,
\qquad
\boldsymbol\Phi_{r,\mathrm B}
=\widetilde{\boldsymbol\Phi}_{r,\mathrm B}=0,
\qquad
\boldsymbol{\mathcal W}_{\mathrm B}
=\widetilde{\boldsymbol{\mathcal W}}_{\mathrm B}=0.
\tag{5.41a}
$$

Outgoing fields are introduced as source/external-leg insertions, not as a
nonzero background in the free Hessian.

The residual constant gauge orbit is removed at \(p=0\); every propagator
statement below is on \(p^2\ne0\).  The actual gauge-fixed density is

$$
\boldsymbol\varpi_{\Psi,E,\nu}
:=\ell_{\Psi,E,\nu}^{*}
\widehat{\boldsymbol\varpi}_{\rm ext,E,\nu}^{1/2},
\qquad
\mathfrak E^{\rm measure}_{\mathsf p}
:=\boldsymbol\varpi_{\Psi,E,\nu}^{-1}
\frac{\vec\partial\boldsymbol\varpi_{\Psi,E,\nu}}
{\partial\widehat q^{\mathsf p}}.
\tag{5.42}
$$

No flatness of (5.42) is assumed.

The physical vector Hessian obtained by differentiating (5.26) is

$$
K_{\mathcal V,AB}^{\rm phys}
=-\frac h{16}\kappa_{AB}D^a\bar D^2D_a
=-\frac h2\kappa_{AB}p^2\Pi_{1/2}.
\tag{5.43}
$$

The Fermi--Feynman target would require

$$
\begin{aligned}
S_{\rm gf,target}^{(2)}
&=\frac h{64}\int_{E,8}
\kappa_{AB}\mathcal V^A
(D^2\bar D^2+\bar D^2D^2)\mathcal V^B\\
&=\frac h2\int_{E,8}\kappa_{AB}
\mathcal F_-^A\mathcal F_+^B,
\end{aligned}
\tag{5.44}
$$

which, through (3D.93), requires the off-diagonal inverse multiplier map

$$
\begin{aligned}
(\mathcal Y^{-1}\mathcal F)_{+,A}
&=-\frac h8\kappa_{AB}\bar D^2\mathcal F_-^B,\\
(\mathcal Y^{-1}\mathcal F)_{-,A}
&=-\frac h8\kappa_{AB}D^2\mathcal F_+^B.
\end{aligned}
\tag{5.44a}
$$

On constrained chiral/antichiral slots, (5.38) gives

$$
\begin{aligned}
(\mathcal YG)_+^A
&=\frac1{2hp^2}\kappa^{AB}\bar D^2G_{-,B},\\
(\mathcal YG)_-^A
&=\frac1{2hp^2}\kappa^{AB}D^2G_{+,B}.
\end{aligned}
\tag{5.44b}
$$

Thus \(\mathcal Y\) in (5.44b) is nonlocal and is not admitted by the local
Step-3D non-minimal class.  Consequently

$$
\boxed{
K_{\mathcal V}^{\rm gf},\quad
K_{\mathcal V}^{\rm tot},\quad
G_{\mathcal V}
=\texttt{BLOCKED\_LOCAL\_NONMINIMAL\_GAUGE\_KERNEL}.}
\tag{5.45}
$$

This is a locality obstruction, not a block-rank obstruction.  Before
eliminating the multipliers, define

$$
 (\mathsf L\mathcal V)_\sigma^A
:=\begin{pmatrix}-\frac14\bar D^2\mathcal V^A\\[1mm]-\frac14D^2\mathcal V^A\end{pmatrix}_{\!\sigma},
\qquad
(\mathsf L^\vee\mathfrak n)_A
:=\mathfrak n_{+,A}+\mathfrak n_{-,A}.
\tag{5.45a}
$$

The exact multiplier--prepotential Hessian is

$$
\mathbb H_{\mathcal Y}
=\begin{pmatrix}
K_{\mathcal V}^{\rm phys}&\mathsf L^\vee\\
\mathsf L&-\mathcal Y
\end{pmatrix},
\qquad
\mathsf S_{\mathcal Y}
:=K_{\mathcal V}^{\rm phys}
+\mathsf L^\vee\mathcal Y^{-1}\mathsf L.
\tag{5.45b}
$$

For invertible \(\mathcal Y\) and \(\mathsf S_{\mathcal Y}\), direct block
multiplication gives

$$
\boxed{
\mathbb H_{\mathcal Y}^{-1}
=\begin{pmatrix}
\mathsf S_{\mathcal Y}^{-1}
&\mathsf S_{\mathcal Y}^{-1}\mathsf L^\vee\mathcal Y^{-1}\\
\mathcal Y^{-1}\mathsf L\mathsf S_{\mathcal Y}^{-1}
&-\mathcal Y^{-1}
+\mathcal Y^{-1}\mathsf L\mathsf S_{\mathcal Y}^{-1}
\mathsf L^\vee\mathcal Y^{-1}
\end{pmatrix}.}
\tag{5.45c}
$$

For the target (5.44), the required multiplier inverse is

$$
\begin{aligned}
(\mathcal Y^{-1}_{\rm target}G)_{+,A}
&=-\frac h8\kappa_{AB}\bar D^2G_-^B,\\
(\mathcal Y^{-1}_{\rm target}G)_{-,A}
&=-\frac h8\kappa_{AB}D^2G_+^B.
\end{aligned}
\tag{5.45d}
$$

Indeed,

$$
\begin{aligned}
(\mathsf L^\vee\mathcal Y^{-1}_{\rm target}\mathsf L)_{AB}
&=-\frac h8\kappa_{AB}
\begin{pmatrix}1&1\end{pmatrix}
\begin{pmatrix}0&\bar D^2\\D^2&0\end{pmatrix}
\begin{pmatrix}-\frac14\bar D^2\\-\frac14D^2\end{pmatrix}\\
&=\frac h{32}\kappa_{AB}
\left(\bar D^2D^2+D^2\bar D^2\right)
=-\frac h2\kappa_{AB}p^2\Pi_0.
\end{aligned}
\tag{5.45e}
$$

On the chiral/antichiral multiplier pair,

$$
\begin{pmatrix}0&\bar D^2\\D^2&0\end{pmatrix}^{\!2}
=-16p^2\mathbf1,
\qquad
\begin{aligned}
(\mathcal Y_{\rm target}G)_+^A
&=\frac1{2hp^2}\kappa^{AB}\bar D^2G_{-,B},\\
(\mathcal Y_{\rm target}G)_-^A
&=\frac1{2hp^2}\kappa^{AB}D^2G_{+,B}.
\end{aligned}
\tag{5.45f}
$$

The factor \(p^{-2}\) in (5.45f) violates the locality condition (3D.88a).
If that condition is temporarily removed, (5.45c) becomes the conditional
identity

$$
\mathbb H_{\mathcal Y_{\rm target}}^{-1}
=\begin{pmatrix}
-\dfrac{2g^2\kappa^{AB}}{p^2}\mathbf1
&\dfrac{\delta^A{}_B}{4p^2}\begin{pmatrix}D^2&\bar D^2\end{pmatrix}\\[4mm]
-\dfrac{\delta_A{}^B}{16p^2}
\begin{pmatrix}\bar D^2D^2\\D^2\bar D^2\end{pmatrix}
&0_{\sigma A}{}^{\tau B}
\end{pmatrix}.
\tag{5.45g}
$$

The formal target inverse

$$
G_{\mathcal V,\rm target}^{AB}(p)
=-\frac{2g^2}{p^2}\kappa^{AB}\mathbf1_{16}
\tag{5.46}
$$

is retained only as a rejected-slice regression value, not as a Wick
contraction.

For every finite coefficient \(\widehat q^{\mathsf p}\), define with the same
ordered left derivative

$$
\begin{aligned}
\mathfrak E_{\mathsf p}^{\rm phys}
&:=\frac{\vec\partial S_{\rm phys}}
{\partial\widehat q^{\mathsf p}},\\
\mathfrak E_{\mathsf p}^{\rm gf+gh}
&:=\frac{\vec\partial S_{\rm gf+gh}}
{\partial\widehat q^{\mathsf p}},\\
J_{\mathsf p}
&:=\frac{\vec\partial\mathscr J^{\rm coll}}
{\partial\widehat q^{\mathsf p}},\\
\mathfrak E_{\mathsf p}^{\rm measure}
&:=\boldsymbol\varpi_{\Psi,E,\nu}^{-1}
\frac{\vec\partial\boldsymbol\varpi_{\Psi,E,\nu}}
{\partial\widehat q^{\mathsf p}}.
\end{aligned}
\tag{5.46a}
$$

The exact regulated Schwinger equation is

$$
\boxed{
\left\langle
\mathfrak E_{\mathsf p}^{\rm phys}
+\mathfrak E_{\mathsf p}^{\rm gf+gh}
-J_{\mathsf p}
-\hbar\mathfrak E_{\mathsf p}^{\rm measure}
\right\rangle=0.}
\tag{5.47}
$$

It is not replaced by a flat continuum functional-derivative slogan.

Separate the actual density from the reference coefficient measure by

$$
d\mu_{\Psi,E,\nu}
=D'\widehat q\,\boldsymbol\varpi_{\Psi,E,\nu}(0)
\exp\left[-\frac1\hbar S_{\rm measure}(\widehat q)\right],
\qquad
S_{\rm measure}
:=-\hbar\log\frac{\boldsymbol\varpi_{\Psi,E,\nu}(\widehat q)}
{\boldsymbol\varpi_{\Psi,E,\nu}(0)}.
\tag{5.47a}
$$

The finite Euclidean chiral-matter Gaussian with reference measure
\(D'\widehat q\) fixes

$$
\begin{aligned}
\langle\phi_r^A(p)\widetilde\phi_s^B(-p)\rangle_{0,{\rm ref}}
&=\frac{\hbar g^2\kappa^{AB}\delta_{rs}}{p^2},\\
\langle\psi_{ra}^A(p)\widetilde\psi_{s\dot b}^B(-p)\rangle_{0,{\rm ref}}
&=-\frac{i\hbar g^2\kappa^{AB}\delta_{rs}p_{a\dot b}}{p^2},\\
\langle F_r^A(p)\widetilde F_s^B(-p)\rangle_{0,{\rm ref}}
&=-\hbar g^2\kappa^{AB}\delta_{rs}.
\end{aligned}
\tag{5.47b}
$$

For the vector sector, exact matrix multiplication proves only the algebraic
transverse pseudoinverse

$$
K_{\mathcal V,AB}^{\rm phys}
G_T^{BC}
=G_T^{CB}K_{\mathcal V,BA}^{\rm phys}
=\delta_A{}^C\Pi_{1/2},
\qquad
G_T^{AB}:=-\frac{2g^2\kappa^{AB}}{p^2}\Pi_{1/2}.
\tag{5.47c}
$$

Equation (5.47c) is not promoted to a \(\mathcal V_T\) Wick contraction before
the complete vector coefficient cycle, its Berezinian, and ordered vector-source
derivatives are fixed.  The longitudinal \(\Pi_0\) contraction is also absent.
The kernels (5.47b) are reference-flat Wick rules only; every coefficient of
\(S_{\rm measure}\) is a separate measure vertex in the regulated Schwinger
equation (5.47).

## 5.10 Source verdict surface

The imported conversation is chronological:

$$
\boxed{
\text{initial isolated-triangle }\epsilon k^2\text{ numerator}
\xrightarrow{\text{later explicit retraction}}
\texttt{REJECTED}.}
\tag{5.48}
$$

The imported scalar vector propagator and complete \(D\)-chain disagree with
(5.45) and (5.53):

$$
\boxed{
\text{conversation scalar vector propagator and complete }D\text{-chain}
=\texttt{REJECTED}.}
\tag{5.49}
$$

The later contact sum, graph census, and anomaly coefficient remain unproved:

$$
\boxed{
\text{conversation cubic normalization, contact kernel, graph census,
and later anomaly coefficient}=\texttt{CONDITIONAL}.}
\tag{5.49a}
$$

Weinberg Chapter 30 and the admitted *Superspace* pages establish only the
candidate structures

$$
K\Delta=\Pi,
\qquad
D\text{-operators transfer across edge deltas},
\qquad
D\text{-operators transferred to external legs survive}.
\tag{5.50}
$$

Their signs, factors, gauge normalization, Euclidean phase, and propagators are
not Project formulas.

## 5.11 Graph and \(D\)-algebra data contract

Each graph object contains

$$
\begin{gathered}
\text{typed vertices, ordered half-edges, oriented internal edges,
external legs, loop momenta,}\\
\text{color words, flavor words, spinor words, symmetry factor,
fermion permutation, and parent/cut relation}.
\end{gathered}
\tag{5.51}
$$

Each \(D\)-algebra rewrite contains

$$
(\text{input},\text{rule},\text{assumptions},
\text{Koszul sign},\text{output},\text{invariants}).
\tag{5.52}
$$

For superspace integration by parts,

$$
\int d^4\vartheta\,(\mathscr D F)G
=-(-1)^{|\mathscr D||F|}
\int d^4\vartheta\,F(\mathscr D G).
\tag{5.53}
$$

If \(G\) is external, the output is an external-leg derivative token; it is never
deleted.  If a derived \(p^2\) cancels an internal denominator, a new contact child
graph is emitted and linked to its parent.

### 5.11a Seed \((W,W)\) Project-only \(D\)-algebra audit

The linear Project letter is

$$
K_+:=-\frac18D_+\bar D^2D_+,
\qquad
\mathbb L_W^{(1)}=K_+\mathcal V.
\tag{5.53a}
$$

Hence

$$
\boxed{
D_-K_+
=-\frac18D_-D_+\bar D^2D_+
=-\frac1{16}D^2\bar D^2D_+.}
\tag{5.53b}
$$

For an edge of incoming momentum \(r\), endpoint transfer is

$$
\boxed{
D_i(r)\Delta_{ij}(r)=-D_j(-r)\Delta_{ij}(r),
\qquad
\bar D_i(r)\Delta_{ij}(r)
=-\bar D_j(-r)\Delta_{ij}(r).}
\tag{5.53c}
$$

The momentum labels \((r,-r)\) in (5.53c) are part of the rule.  The normalized
Grassmann delta obeys

$$
\boxed{
\left[D^2\bar D^2
(\vartheta^2\bar\vartheta^2)\right]_{\vartheta=0}=16.}
\tag{5.53d}
$$

Ordered expansion of the two gauge-kinetic terms gives the fixed-background
cubic ports

$$
\begin{aligned}
\mathcal V_{\mathcal W}^{E;BC}
&=\frac{ih}{8}c_{BCE}\mathcal W^{Ea}
\left(D_a^{(C)}-D_a^{(B)}\right),\\
\mathcal V_{\widetilde{\mathcal W}}^{D;AC}
&=-\frac{ih}{8}c_{ACD}\widetilde{\mathcal W}_{\dot a}^{D}
\left(\bar D^{\dot a(C)}-\bar D^{\dot a(A)}\right).
\end{aligned}
\tag{5.53e}
$$

For

$$
r_0=k,
\qquad
r_1=k+q,
\qquad
r_2=k+p+q,
\tag{5.53f}
$$

the raw derivative-difference momenta are

$$
\begin{aligned}
p_C-p_A&=-r_1-r_0=-(2k+q)=-L_1,\\
p_C-p_B&=r_1+r_2=2k+p+2q=L_2.
\end{aligned}
\tag{5.53g}
$$

The ordered spinor contraction is

$$
(L_1)_+{}^{\dot b}p_{a\dot b}(L_2)^{a\dot c}
=(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot c}
L_{1m}p_nL_{2r}.
\tag{5.53h}
$$

For one fixed \(D_-\) placement, the claimed delta-only skeleton has the exact
Project coefficient chain

$$
\frac1{128}\times16\times(2i)\times(2i)
=-\frac12,
\qquad
-\frac12\{D_a(p),\bar D_{\dot b}(p)\}
=ip_{a\dot b}.
\tag{5.53i}
$$

Thus the imported \(+2\) \(D\)-factor and its \(g^2/2\) numerator coefficient
are rejected.  Even with the rejected scalar target kernel, the fixed-orientation,
fixed-placement magnitude is

$$
\left|
(-2g^2)^3
\left(-\frac{ih}{8}\right)
\left(\frac{ih}{8}\right)
\left[\frac{16}{128}(2i)^2\right]
\right|
=\frac{g^2}{16}.
\tag{5.53j}
$$

Equation (5.53j) is a rejected-slice diagnostic.  The accepted transverse
pseudoinverse carries \(\Pi_{1/2}\) on every internal edge; the raw cubic ports
have not been proved to lie in its image.  Therefore no delta-only triangle
amplitude or one-loop coefficient follows from (5.53a)--(5.53j).

## 5.12 One-loop result ledger

The sixteen tree rows are exact by (5.33)--(5.35).  The renormalized one-loop
rows remain

$$
\boxed{
\begin{gathered}
\texttt{BLOCKED\_LOCAL\_NONMINIMAL\_GAUGE\_KERNEL},\\
\texttt{BLOCKED\_GAUGE\_FIXED\_DENSITY\_BEREZINIAN},\\
\texttt{BLOCKED\_VECTOR\_TRANSVERSE\_FINITE\_GAUSSIAN\_RECONSTRUCTION},\\
\texttt{BLOCKED\_FP\_GHOST\_CYCLE\_UNDECLARED},\\
\texttt{BLOCKED\_NK\_BRANCH\_AND\_KERNEL\_UNFIXED},\\
\texttt{BLOCKED\_UNINSTANTIATED\_E\_XI\_CORE},\\
\texttt{BLOCKED\_COMPOSITE\_DESCENDANT\_INSERTION\_UNINSTANTIATED},\\
\texttt{BLOCKED\_EDGE\_TAGGED\_PROJECTOR\_DALGEBRA\_TRACE},\\
\texttt{BLOCKED\_CHANNEL\_GRAPH\_INSTANTIATION\_AND\_DALGEBRA}
\end{gathered}}
\tag{5.54}
$$

until all interaction and composite vertices are produced by ordered functional
differentiation of (4C.4), (5.28), and the BRST-fixed action, and the reverse-order
Wick census agrees.  In particular, the seed \((W,W)\) coefficient is not copied
from any imported conversation.
