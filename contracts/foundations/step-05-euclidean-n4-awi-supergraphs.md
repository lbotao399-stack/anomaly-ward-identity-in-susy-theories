# Step 5. Euclidean \(\mathcal N=4\) AWI supergraphs

## 5.0 Status

$$
\boxed{
\begin{aligned}
5A&:\texttt{REGISTERED\_FIXED\_VECTOR\_WARD\_PROVED},\\
5B\ (WW,\ w=0)&:\texttt{FAIL\_CLOSED\_CONTACT\_AND\_INJECTIVITY\_OPEN},\\
5C&:\texttt{SPECIFIED}.
\end{aligned}}
\tag{5.0}
$$

This file is an unreviewed branch proposal until it reaches verified
\(origin/main\).

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

## 5A. PERTURBATIVE_FF_DRED_SUPERGRAPHS

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
statement below is on \(p^2\ne0\).  Step 5A uses

$$
\boxed{
D\mu_{5A}:=D'\widehat q,
\qquad
\mathfrak E_{\mathsf p}^{\rm measure}=0.}
\tag{5.42A}
$$

All FP and NK determinants in Step 5A are represented by explicit actions.
Equation (5.42A) is not an equality with the finite-BV density.  The Step-5C
density is

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

No flatness of (5.42) is assumed in Step 5C.

The physical vector Hessian obtained by differentiating (5.26) is

$$
K_{\mathcal V,AB}^{\rm phys}
=-\frac h{16}\kappa_{AB}D^a\bar D^2D_a
=-\frac h2\kappa_{AB}p^2\Pi_{1/2}.
\tag{5.43}
$$

The local Fermi--Feynman quadratic action is

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

If it is represented by the Step-3D local-\(\mathcal Y\) chart, it requires the
off-diagonal inverse multiplier map

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
Step-3D non-minimal class.  This is a Step-5C equivalence obligation; it does
not obstruct the fixed-gauge Step-5A Gaussian.  In Step 5A,

$$
\boxed{
\begin{aligned}
K_{\mathcal V,AB}^{\rm gf}
&=-\frac h2\kappa_{AB}p^2\Pi_0,\\
K_{\mathcal V,AB}^{\rm tot}
&=-\frac h2\kappa_{AB}p^2\mathbf1_{16},\\
G_{\mathcal V}^{AB}
&=-\frac{2g^2}{p^2}\kappa^{AB}\mathbf1_{16}.
\end{aligned}}
\tag{5.45}
$$

Since \(hg^2=1\), exact \(16\times16\) multiplication gives

$$
\boxed{
K_{\mathcal V,AB}^{\rm tot}G_{\mathcal V}^{BC}
=G_{\mathcal V}^{CB}K_{\mathcal V,BA}^{\rm tot}
=\delta_A{}^C\mathbf1_{16}.}
\tag{5.45A}
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

The Step-5A Wick kernel

$$
G_{\mathcal V,\rm target}^{AB}(p)
=-\frac{2g^2}{p^2}\kappa^{AB}\mathbf1_{16}
\tag{5.46}
$$

is admitted on \(p^2\ne0\).  Its equivalence to a finite local non-minimal
coefficient integral remains Step 5C.

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

Equation (5.47c) is the transverse restriction of the admitted Step-5A kernel
(5.46).  Equations (5.46) and (5.47b) are reference-flat Wick rules.  Every
coefficient of \(S_{\rm measure}\), the finite Berezinian, and the local-
\(\mathcal Y\) realization belongs only to Step 5C.

## 5.10 Source verdict surface

The imported conversation is chronological:

$$
\boxed{
\text{initial isolated-triangle }\epsilon k^2\text{ numerator}
\xrightarrow{\text{later explicit retraction}}
\texttt{REJECTED}.}
\tag{5.48}
$$

The imported scalar vector kernel is not adopted from the conversation.  It is
independently rederived and admitted only through (5.45)--(5.46).  The imported
single-line complete \(D\)-chain is not a substitute for the eight rows:

$$
\boxed{
\begin{aligned}
&\text{conversation scalar vector kernel}
=\texttt{INDEPENDENTLY\_REDERIVED\_FOR\_5A},\\
&\text{conversation claimed complete }D\text{-chain}
=\texttt{REJECTED\_AS\_A\_COMPLETE\_TRACE}.
\end{aligned}}
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

## 5B. SD_COMPLETE_GRAPH_ORBIT

### 5.11 Graph and \(D\)-algebra data contract

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

Equation (5.53i) is one row, not the sum over two \(D_-\) placements and four
cubic endpoint assignments.  With the admitted Step-5A kernel, its
fixed-orientation, fixed-placement coefficient is

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

Equation (5.53j) is retained as the exact normalization of each explicit row.
It is never used as the complete \(D\)-factor.

### 5.11b Project composite insertion

The Euler core is

$$
\mathfrak E_{\Xi,A}^{\mathsf C}
=h\kappa_{AB}\left[
\frac12\nabla^a\mathcal W_a^B
-i(\Phi_r\times\widetilde\Phi_r)^B
\right].
\tag{5.53k}
$$

For

$$
F(z)=\frac{1-e^{-z}}z
=1-\frac12z+\frac16z^2-\frac1{24}z^3+O(z^4),
\qquad
(\operatorname{ad}_{\mathcal V})^{\mathsf T}
=-\operatorname{ad}_{\mathcal V},
\tag{5.53l}
$$

ordered transposition gives

$$
\boxed{
\mathfrak E_{\mathcal V}^{\rm phys}
=\left(
1+\frac12\operatorname{ad}_{\mathcal V}
+\frac16\operatorname{ad}_{\mathcal V}^2
+\frac1{24}\operatorname{ad}_{\mathcal V}^3
\right)\mathfrak E_{\Xi}^{\mathsf C}
+O(\mathcal V^4).}
\tag{5.53m}
$$

Therefore the proposed series with coefficients
\((1,-1/2,-1/6)\) is
\(\texttt{REJECTED\_BY\_5\_28\_TRANSPOSITION}\).  The physical SD insertion
uses (5.53m).

The Project composite recursion is

$$
\begin{aligned}
\Gamma_{(n)a}
&=\frac{(-1)^{n-1}}{n!}
\operatorname{ad}_{\mathcal V}^{n-1}(D_a\mathcal V),\\
\mathcal W_{(n)a}
&=-\frac18\bar D^2\Gamma_{(n)a},\\
X_{(n)}
&=D_+\mathcal W_{(n)+}
+\sum_{r=1}^{n-1}
[\Gamma_{(r)+},\mathcal W_{(n-r)+}].
\end{aligned}
\tag{5.53n}
$$

With every component commutator expanded through
\([T_A,T_B]=ic_{AB}{}^CT_C\), the exact coefficients are

$$
\begin{array}{c|ccc}
n&1&2&3\\ \hline
\Gamma_{(n)}&1&-i/2&-1/6\\
\mathcal W_{(n)}&-1/8&i/16&1/48
\end{array}.
\tag{5.53o}
$$

For \(X=\sum_{n\ge1}X_{(n)}\),

$$
\boxed{
\begin{aligned}
I_{(N)}^{AB}
={}&\sum_{r+s=N}D_-
\left(X_{(r)}^AX_{(s)}^B\right)\\
&+\sum_{t+r+s=N}
\left(
[\Gamma_{(t)-},X_{(r)}]^AX_{(s)}^B
+X_{(r)}^A[\Gamma_{(t)-},X_{(s)}]^B
\right),
\end{aligned}}
\tag{5.53p}
$$

where every sum has positive integer indices.  Ordered AST expansion gives

$$
|I_{(2)}|=2,
\qquad
|I_{(3)}|=10,
\qquad
|I_{(4)}|=30.
\tag{5.53q}
$$

### 5.11c Eight-row triangle trace

For either \(D_-\) placement, the four endpoint rows are

$$
\begin{array}{c|c|c|c}
\bar D\text{ edge}&D\text{ edge}
&s_{\rm vertex}s_{\rm transfer}\big|_{\bar D}
&s_{\rm vertex}s_{\rm transfer}\big|_D\\ \hline
e_0(r_0)&e_1(r_1)&(-1)(-1)&(+1)(+1)\\
e_0(r_0)&e_2(r_2)&(-1)(-1)&(-1)(-1)\\
e_1(r_1)&e_1(r_1)&(+1)(+1)&(+1)(+1)\\
e_1(r_1)&e_2(r_2)&(+1)(+1)&(-1)(-1)
\end{array}.
\tag{5.53r}
$$

All four endpoint signs are (+1).  Since both letters are even, moving
\(D_-\) from the left placement to the right placement adds no Leibniz sign.
The eight row numerators sum to

$$
\sum_{P\in\{A,B\}}
\sum_{\bar e,e}
r_{\bar e,+}{}^{\dot b}p_{a\dot b}r_e^{a\dot c}
=2(L_1)_+{}^{\dot b}p_{a\dot b}(L_2)^{a\dot c}.
\tag{5.53s}
$$

Before the closed \(D\)-chain, the three propagators and two cubic vertices give

$$
(-2g^2)^3
\left(-\frac{ih}{8}\right)
\left(\frac{ih}{8}\right)
=-\frac{g^2}{8}.
\tag{5.53t}
$$

Thus every row has coefficient

$$
\left(-\frac{g^2}{8}\right)
\left(-\frac12\right)
=\frac{g^2}{16},
\tag{5.53u}
$$

and the fixed orientation triangle is

$$
\boxed{
\begin{aligned}
\Gamma_{\triangle}^{A|B}
={}&\frac{g^2}{8}c_{ACD}c_{BCE}
\widetilde{\mathcal W}_{\dot\alpha}^{D}(q)
(ip^n)X^E(p)
(\sigma_E^m\bar\sigma_E^n\sigma_E^r)_+{}^{\dot\alpha}\\
&\times\int\frac{d^dk}{(2\pi)^d}
\frac{L_{1m}L_{2r}}
{k^2(k+q)^2(k+p+q)^2}.
\end{aligned}}
\tag{5.53v}
$$

No \(\epsilon\) occurs in the numerator of (5.53v).

### 5.11d Triangle/contact poles

For each bosonic quantum-prepotential coefficient \(v_i\), the reference-flat
integral gives

$$
0=\int D'v\,
\frac{\vec\partial}{\partial v_i}
\left(I[v]e^{-S[v]/\hbar}\right)
=\left\langle\frac{\vec\partial I}{\partial v_i}\right\rangle
-\frac1\hbar
\left\langle I\frac{\vec\partial S}{\partial v_i}\right\rangle.
\tag{5.53V}
$$

At quadratic order,

$$
\frac{\vec\partial S_2}{\partial v_i}=K^{\rm tot}_{ij}v_j,
\qquad
K^{\rm tot}_{ij}G^{jk}=\delta_i{}^k.
\tag{5.53W}
$$

The typed source and antichiral external port are

$$
|J_{AB}|=1,
\qquad
|\nabla_-(X^AX^B)|=1,
\qquad
|J_{AB}\nabla_-(X^AX^B)|=0,
\qquad
\widetilde{\mathcal W}_{\dot\alpha}.
\tag{5.53w}
$$

The complete odd blocks are

$$
\mathbb B_{\widetilde W}=\widetilde{\mathcal W}Q_{\bar D},
\qquad
\mathbb B_W=\mathcal WQ_D,
\qquad
|\mathbb B_{\widetilde W}|=|\mathbb B_W|=0.
\tag{5.53x}
$$

For the reflected orientation,

$$
s_{\rm ext}=-1,
\qquad
s_{\rm quantum}=-1,
\qquad
s_{\rm reflected}=s_{\rm ext}s_{\rm quantum}=+1.
\tag{5.53x$'$}
$$

Thus every isolated-triangle row in both orientations gives

$$
P_{\triangle,{\rm row}}^{mr}
=\frac{g^2}{1024\pi^2\epsilon}\widehat\delta^{mr}.
\tag{5.53x$''$}
$$

The Project background/quantum split gives

$$
\begin{gathered}
I_{(3)}[X_{\rm ext};v,v]:30,
\qquad
\widetilde S_{(3)}[\widetilde W_{\rm ext};v,v]:6,\\
I_{(4)}[V_{\rm B},V_{\rm B};v,v]:180,
\\
N_{I_0H_2}=576,
\qquad
N_{I_1[p_1]H_1[p_2]}=N_{I_1[p_2]H_1[p_1]}=1440,
\qquad
N_{I_2}=720.
\end{gathered}
\tag{5.53y}
$$

These four numbers count generated branch paths, not quotient graph classes.
All objects through (5.54B) are restricted to the registered fixed-vector
sector.  The Hessian contact operator is

$$
\begin{aligned}
Q_{\rm Hess}^{(2)}
:={}&\frac12\operatorname{STr}_{\rm DRED}\!\Big[
-I_0G_0H_2[p_1,p_2]G_0\\
&-I_1[p_1]G_0H_1[p_2]G_0
-I_1[p_2]G_0H_1[p_1]G_0
+I_2[p_1,p_2]G_0\Big].
\end{aligned}
\tag{5.53z}
$$

The exact quadratic functional is

$$
Q_{\triangle}^{\rm bare}
:=\frac12\operatorname{STr}_{\rm DRED}\!\left[
I_0G_0H_1[p_1]G_0H_1[p_2]G_0
+I_0G_0H_1[p_2]G_0H_1[p_1]G_0
\right].
\tag{5.53z$_0$}
$$

$$
\boxed{
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm bare}
+\underbrace{\left(Q_{\rm Hess}^{(2)}+\mathrm{CT}_2[p_1,p_2]\right)}_{
Q_{\rm contact,Hess}^{(2)}}.}
\tag{5.53z$'$}
$$

A later numerator decomposition requires a constructed map
\(\mathcal R_{\rm cut}\) selecting terms that cancel one triangle propagator:

$$
Q_{\triangle}^{\rm cut}
:=\mathcal R_{\rm cut}Q_{\triangle}^{\rm bare},
\qquad
Q_{\triangle}^{\rm irr}
:=(1-\mathcal R_{\rm cut})Q_{\triangle}^{\rm bare}.
\tag{5.53z$''$}
$$

Only after this map and its coefficients are derived may one rewrite

$$
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm irr}
+\underbrace{
\left(Q_{\triangle}^{\rm cut}+Q_{\rm contact,Hess}^{(2)}\right)}_{
Q_{\rm contact,eff}^{(2)}}.
\tag{5.53z$'''$}
$$

Intrinsic chirality of one gauge-kinetic monomial does not imply
\(\Pi_{X\widetilde W}H_2=0\) after connection expansion and edge-tagged
\(D\)-algebra.  The exact present status is

$$
\begin{gathered}
\Pi_{X\widetilde W}H_2=\texttt{NOT\_DERIVED},
\qquad
\Pi_{X\widetilde W}I_2=\texttt{NOT\_DERIVED},
\qquad
\mathrm{CT}_2=\texttt{NOT\_FIXED},\\
N_{\rm collapse\ bindings}=48,
\qquad
N_{\rm collapse\ GraphIR}=6,
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED},
\qquad
Q_{\triangle}^{\rm cut}=\texttt{COEFFICIENT\_TRANSPORT\_OPEN}.
\end{gathered}
\tag{5.53z$''''$}
$$

For an \(I_{(4)}\) row satisfying

$$
\mathcal A_{I_{(4)},r}
=\int_k\frac{P_r(k,p_1,p_2)}{k^2},
\qquad
P_r\in\mathbb Q[k,p_1,p_2],
$$

DRED scalelessness gives \(\mathcal A_{I_{(4)},r}=0\).  The edge-tagged
locality-to-polynomial proof for all \(180\) rows, their separated ordinary
UV/IR poles, the \(H_2\) projector, the \(328\) shared-scope \(I_1H_1\)
branches, and the \(I_2\) normalization remain open.

The symmetric source quotient and dotted-index variance select the following
quadratic target candidate:

$$
\boxed{
\mathscr O_{\star,AB}
=c_{ACD}c_{BCE}
\left[
\widetilde{\mathcal W}_{\dot\alpha}^{D}
\mathcal D_+{}^{\dot\alpha}X^E
+(\mathcal D_+{}^{\dot\alpha}X^D)
\widetilde{\mathcal W}_{\dot\alpha}^{E}
\right],
\qquad
X^E=(\nabla_+\mathcal W_+)^E.}
\tag{5.54}
$$

Its coefficient is not propagated:

$$
\boxed{
\operatorname{status}\!\left(\Gamma_{C,{\rm pole}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},
\qquad
\operatorname{status}\!\left(\Gamma_{\tau,{\rm pole}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},
\qquad
\operatorname{status}\!\left(C_{\rm anomaly}\text{ accepted}\right)
=\texttt{NOT\_ACCEPTED}.}
\tag{5.54A}
$$

Equation (5.54) is a type-and-quotient statement, not a Ward-identity
coefficient.  Define

$$
\ell_2[\mathscr O]
:=\left.\frac12\frac{d^2}{dt^2}\right|_{t=0}
\mathscr O(t\mathcal B).
\tag{5.54A$'$}
$$

Let \(\mathcal T_{2,{\rm reg}}^{4d}\) denote the registered physical-\(4d\)
quadratic typed target and \(B_2\subset\mathcal T_{2,{\rm reg}}^{4d}\) its
quadratic boundary subspace.  Extend scalars and form the quotient:

$$
t_\star:=q_{4d}\ell_2(\mathscr O_\star)\ne0,
\qquad
\mathcal T_{2,{\rm reg}}^{4d,\epsilon}
:=\mathcal T_{2,{\rm reg}}^{4d}\otimes_{\mathbb Q}\mathbb Q(\epsilon),
\qquad
\overline{\mathcal T}_{2,{\rm reg}}^{4d,\epsilon}
:=\left(\mathcal T_{2,{\rm reg}}^{4d}/B_2\right)
\otimes_{\mathbb Q}\mathbb Q(\epsilon),
$$

$$
\rho_2^\epsilon:\mathcal T_{2,{\rm reg}}^{4d,\epsilon}
\longrightarrow\overline{\mathcal T}_{2,{\rm reg}}^{4d,\epsilon},
\qquad
\bar t_\star:=\rho_2^\epsilon(t_\star).
\tag{5.54A$''$}
$$

Conditionally on \(\bar t_\star\ne0\), fix

$$
\overline{\mathcal T}_{2,{\rm reg}}^{4d,\epsilon}
=\mathbb Q(\epsilon)\bar t_\star
\oplus\overline{\mathcal T}_{2,\perp}^{4d,\epsilon},
\qquad
\bar\pi_\star^{4d}:
\overline{\mathcal T}_{2,{\rm reg}}^{4d,\epsilon}
\longrightarrow\mathbb Q(\epsilon),
\qquad
\bar\pi_\star^{4d}(\alpha\bar t_\star+\bar t_\perp)=\alpha.
\tag{5.54A$''_1$}
$$

$$
\operatorname{status}\!\left(\bar t_\star\ne0\right)
=\texttt{OPEN\_PHYSICAL4D\_RELATION\_MATRIX}.
\tag{5.54A$''_2$}
$$

Define separately the DRED-local and physical-\(4d\) quadratic insertions

$$
\mathscr A_{{\rm loc,DRED},2}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{\rm DRED}
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}},
\qquad
\mathscr A_{{\rm loc},4d,2}^{(1),{\rm reg}}
:=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}.
\tag{5.54A$'''$}
$$

The interchange

$$
q_{4d}\operatorname{Loc}_{\rm UV}^{\rm DRED}
=\operatorname{Loc}_{\rm UV}^{4d}q_{4d}
\qquad\texttt{NOT\_PROVED}
\tag{5.54A$''''$}
$$

is not used.  Conditionally on \(\bar t_\star\ne0\), in the registered
fixed-vector sector,

$$
\boxed{
C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}+C_{{\rm contact,Hess},{\rm reg}},
\qquad
C_{2,{\rm reg}}:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\mathscr A_{{\rm loc},4d,2}^{(1),{\rm reg}}\right),
\qquad
C_{\triangle,{\rm bare,reg}}:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\triangle}^{\rm bare}\right),
\qquad
C_{{\rm contact,Hess},{\rm reg}}:=\bar\pi_\star^{4d}\rho_2^\epsilon\!\left(
\operatorname{Loc}_{\rm UV}^{4d}q_{4d}Q_{\rm contact,Hess}^{(2)}\right)
.}
\tag{5.54B}
$$

$$
\operatorname{status}\!\left(
C_{{\rm contact,Hess},{\rm reg}}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
\tag{5.54B$'$}
$$

For the full theory,

$$
C_2^{\mathcal N=4}
:=\sum_{\alpha\in\{V,\Phi_r,\widetilde\Phi_r,{\rm FP},{\rm NK}\}}
C_{2,\alpha},
\qquad
\operatorname{status}\!\left(C_2^{\mathcal N=4}\text{ evaluated}\right)
=\texttt{NOT\_ESTABLISHED}.
\tag{5.54C}
$$

Therefore \(C_{2,{\rm reg}}=C_{\triangle,{\rm bare,reg}}\), uniqueness of the nonlinear
completion of \(\mathscr O_\star\), and a one-loop anomaly coefficient are not
established.

### 5.11e FP/NK one-loop census

Let \(m_n\) count FP vertices with \(n\) quantum-\(\mathcal V\) ports.  Port
saturation gives

$$
E=\frac{2+m_1+2m_2}{2}+N_{\rm FP},
\qquad
V=1+N_{\rm FP},
\qquad
L=1+\frac{m_1}{2}+m_2.
\tag{5.54a}
$$

Connectivity requires \(m_1+2m_2\ge2\), and saturation requires even \(m_1\).
The first connected FP families have \(L=2\); the flat NK action has no
quantum-\(\mathcal V\) port.  Therefore

$$
\boxed{
\mathrm{FP}_{WW}^{L=1}
=\mathrm{NK}_{WW}^{L=1}
=\texttt{PROVED\_ABSENT\_AT\_THIS\_ORDER}.}
\tag{5.54b}
$$

## 5.12 Typed compiler contract

Define one immutable notation object

$$
\mathfrak N=
\left(
\mathcal F,\mathcal I,\mathcal D,\mathcal P,
\mathcal V,\mathcal M,\mathcal R_{\rm DRED}
\right),
\qquad
h_{\mathfrak N}:=\operatorname{SHA256}
\bigl(\operatorname{CanonicalJSON}(\mathfrak N)\bigr).
\tag{5.54P1}
$$

The exact scalar and Project coefficient rings are

$$
\mathbb K
=
\mathbb Q[i,s]\big/(i^2+1,s^2-2),
\qquad
\mathbb R_{\rm Project}
=
\mathbb K[h,g^2,\hbar]\big/(hg^2-1).
\tag{5.54P1a}
$$

The primitive \(WW\) seed lies in

$$
\mathbb Q(i)[h,g^2]\big/(hg^2-1)
\subset\mathbb R_{\rm Project},
\tag{5.54P1b}
$$

while the full \(\mathcal N=4\) grammar retains \(s=\sqrt2\) exactly.

Here \(\mathcal F\) is the typed field set, \(\mathcal I\) the index spaces,
\(\mathcal D\) the ordered derivative algebra, \(\mathcal P\) the propagator
relation, \(\mathcal V\) the ordered vertex set, \(\mathcal M\) the Fourier and
momentum conventions, and \(\mathcal R_{\rm DRED}\) the regulator split.  The
three heavy symbolic compiler maps and the pole compiler are

$$
\boxed{
\mathfrak N\xrightarrow{\ C_G\ }
\mathfrak G\xrightarrow{\ C_A\ }
\mathfrak A\xrightarrow{\ C_D\ }
\mathfrak D\xrightarrow{\ C_{\rm pole}\ }
\mathfrak P_{\rm UV}.}
\tag{5.54P2}
$$

\(\mathfrak G\) is Wick-complete and \(D\)-unreduced: every quantum port is
contracted once, while its superspace derivative words remain unevaluated.

For a fixed insertion and ordered interaction multiset, let \(Q\) be the set
of quantum half-edges and let

$$
\mathcal P\subset Q\times Q
\tag{5.54P3}
$$

be the typed propagator relation.  The physical parent set is

$$
\mathcal G_{\rm phys}
=
\left\{
M\subset\mathcal P:
\begin{array}{l}
M\text{ is a perfect matching of }Q,\\
G(M)\text{ is connected},\\
b_1(G(M))=|E|-|V|+1=1,\\
P_v^{\rm in}=0\text{ at every vertex}
\end{array}
\right}\Big/\operatorname{Aut}_{\mathfrak N}.
\tag{5.54P4}
$$

Consequently a valence request is not a graph:

$$
Q\text{ specified},\quad M\text{ absent}
\quad\Longrightarrow\quad
\texttt{VALENCE\_REQUEST\_NOT\_GRAPH}.
\tag{5.54P5}
$$

For \(G\in\mathcal G_{\rm phys}\), let \(P\) run through the labeled Wick
pairings with \(\operatorname{Can}(P)=G\).  Define the graph coefficient by

$$
C_G
=
\sum_{P:\operatorname{Can}(P)=G}
s_{\rm Wick}(P)s_{\rm Koszul}(P)s_{\rm ext}(P)
C_{\rm exp}(P)
\prod_{u\in V(P)}C_u.
\tag{5.54P5a}
$$

\(\lvert\operatorname{Aut}_{\mathfrak N}(G)\rvert\) is an independent orbit
audit; it is not divided into (5.54P5a) a second time.  The amplitude compiler
emits the ordered factorization

$$
\boxed{
\mathcal A_G
=
C_G
\int\prod_{j=1}^{b_1(G)}\frac{d^dk_j}{(2\pi)^d}
\left[
\prod_{v\in V(G)}\delta^{(d)}(P_v)\,\mathcal O_v
\right]
\left[
\prod_{e\in E(G)}G_e(r_e)
\right]
\left[
\prod_{x\in X(G)}\mathcal L_x(p_x)
\right].}
\tag{5.54P6}
$$

Every factor in (5.54P6) retains its source vertex, port, edge, ordered slot,
momentum, and \(h_{\mathfrak N}\).  The compiler rejects

$$
\begin{gathered}
\sum_{h\ni v}p_h\ne0,
\qquad
|E|-|V|+1\ne1,
\qquad
\exists h\in Q:\deg_M(h)\ne1,\\
\text{undefined coefficient},
\qquad
\text{undefined derivative scope}.
\end{gathered}
\tag{5.54P7}
$$

An edge-tagged derivative word is

$$
w=c\prod_{j=1}^{N_D}
\mathsf D_j[a_j,e_j,\partial_j]
\prod_{f=1}^{N_F}\mathcal F_f,
\qquad
c\in\mathbb K.
\tag{5.54P8}
$$

Every rewrite is stored as

$$
(w_n,R_n,\mathcal C_n,s_n,w_{n+1}),
\qquad
w_{n+1}=s_nR_n(w_n),
\qquad
s_n\in\{+1,-1\},
\tag{5.54P9}
$$

where \(\mathcal C_n\) contains chirality, endpoint, momentum, and parity
conditions.  Reduction is scheduled in the irreversible phase order

$$
\boxed{
\text{scope expansion}
\prec\text{endpoint canonicalization}
\prec\text{pivoted IBP}
\prec\text{primitive normal ordering}
\prec\text{projector reduction}
\prec\text{chirality}
\prec\text{Grassmann saturation}
\prec\text{typed edge collapse}.}
\tag{5.54P10}
$$

The phase measures are

$$
\begin{aligned}
M_1&=N_{\rm unexpanded\ scope},
&M_2&=N_{\rm noncanonical\ endpoint},\\
M_3&=N_{\rm derivative\ on\ active\ pivot},
&M_4&=(N_{\rm operator\ inversion},N_D+N_{\bar D}),\\
M_5&=N_{\rm reducible\ projector},
&M_6&=N_{\rm applicable\ chirality\ condition},\\
M_7&=N_{\rm unsaturated\ Grassmann\ delta},
&M_8&=N_{\rm matched\ kinetic\ propagator\ pair}.
\end{aligned}
\tag{5.54P11}
$$

Each rule is admitted only in its phase and strictly lowers that phase's
measure.  IBP and endpoint transfer are not bidirectional rewrite rules.

The local operator rules are

$$
\{D_a,\bar D_{\dot b}\}=-2D_{a\dot b},
\qquad
D^2\bar D^2D^2=-16p_{(4)}^2D^2,
\qquad
\bar D^2D^2\bar D^2=-16p_{(4)}^2\bar D^2.
\tag{5.54P12}
$$

For every registered critical pair \((R_i,R_j)\) in a finite audit suite,
acceptance of that suite requires

$$
\operatorname{NF}(R_iR_jw)
=
\operatorname{NF}(R_jR_iw)
\tag{5.54P13}
$$

symbolically.  The exact \(16\times16\) exterior-algebra representation at
registered nonzero momenta is a regression oracle, not a polynomial-identity
proof.  A finite registered suite does not prove global confluence; that
status requires an exhaustive overlap certificate.  The human renderer is a
pure map

$$
C_R:(\mathfrak N,\mathfrak G,\mathfrak A,\mathfrak D)
\longrightarrow
\left(
\text{supergraph},
\text{factorized amplitude},
\text{rewrite ledger},
\text{status}
\right),
\tag{5.54P14}
$$

and may not introduce a coefficient absent from \(\mathfrak A\) or
\(\mathfrak D\).

The pole compiler emits

$$
\mathfrak P_{\rm UV}
=
\left(
d=4-2\epsilon,\,
\omega_{\rm UV},\,
\text{IR status},\,
\text{loop shift},\,
\text{tensor reduction},\,
\operatorname{Pole}_{1/\epsilon},\,
\text{metric space}
\right).
\tag{5.54P15}
$$

No graph enters an SD pole sum without this certificate.

## 5C. FINITE_BV_DENSITY_AND_CYCLES

The finite-BV Step-5C obligations are

$$
\boxed{
\begin{gathered}
\texttt{FINITE\_COEFFICIENT\_SPACE\_DENSITY\_AND\_BEREZINIAN},\\
\texttt{FINITE\_VECTOR\_COEFFICIENT\_CYCLE},\\
\texttt{FINITE\_FP\_AND\_NK\_CYCLES},\\
\texttt{GLOBAL\_LOCAL\_NONMINIMAL\_REALIZATION}.
\end{gathered}}
\tag{5.54c}
$$

These are not used in (5.53v)--(5.54b).  Equality between the reference-flat
Step-5A Gaussian and the finite-BV formulation is not claimed.
