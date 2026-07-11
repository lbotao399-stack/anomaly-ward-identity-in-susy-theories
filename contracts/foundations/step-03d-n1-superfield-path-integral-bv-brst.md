# 00 3+1d SUSY QFT — Convention Lock

## Step 3D. Regulated \(N=1\) superfield path integral and BV--BRST quantization

### 3D.1 Scope and exponent conventions

$$
R\in\{L,E\},
\qquad
\mathsf p,\mathsf q=1,\ldots,n_{R,\nu},
\qquad
\mathsf i,\mathsf j,\mathfrak a,\mathfrak b,
\underline\imath,\underline\jmath
=1,\ldots,N^{\rm fld}_{R,\nu},
\qquad
\mathsf r,\mathsf s=1,\ldots,N^{\rm int}_{R,\nu},
\qquad
\boldsymbol\alpha,\boldsymbol\beta=1,\ldots,g_{R,\nu},
\qquad
\nu\in\mathbb N.
\tag{3D.1}
$$

Here \(\mathsf p,\mathsf q\) are finite physical-field coefficients,
\(\mathsf i,\mathsf j\) are finite full-BV coefficients,
\(\mathfrak p,\mathfrak q\) are untruncated physical-field DeWitt
indices,
\(\mathfrak i,\mathfrak j\) are untruncated full-BV DeWitt indices,
\(\mathfrak a,\mathfrak b\) are quantum-split coefficients, and
\(\underline\imath,\underline\jmath\) are background coefficients.
The blockwise bijections in (3D.97a) identify the three displayed
finite ranges; \(\mathsf r\) labels only coordinates integrated on the
residual-transverse gauge-fixed slice.
The untruncated gauge-parameter DeWitt index is
\(\boldsymbol\lambda\).  None of these is a gauge-frame label or the
Step-3C collective superspace index \(\mathfrak A\).

For every homogeneous object \(X\),

$$
\epsilon_X\in\mathbb Z_2,
\qquad
\operatorname{gh}(X)\in\mathbb Z,
\qquad
[X]\in\frac12\mathbb Z.
\tag{3D.2}
$$

The symbol \(X^\star\) denotes the BV antifield and never denotes
complex conjugation:

$$
\boxed{
\epsilon_{X^\star}=\epsilon_X+1,
\qquad
\operatorname{gh}(X^\star)=-1-\operatorname{gh}(X).}
\tag{3D.3}
$$

Define the three superspace domains and their ordered integrals by

$$
\begin{aligned}
\Sigma_{R,8}&:=(x_R,\vartheta,\bar\vartheta),
&
\int_{R,8}Y
&:=\int d^4x_R\,[Y]_D,\\
\Sigma_{R,+}&:=(y_R,\vartheta),
&
\int_{R,+}X
&:=\int d^4x_R\,[X]_F,\\
\Sigma_{R,-}&:=(\widetilde y_R,\bar\vartheta),
&
\int_{R,-}\widetilde X
&:=\int d^4x_R\,[\widetilde X]_{\widetilde F}.
\end{aligned}
\tag{3D.4}
$$

The classical actions are fixed, not redefined:

$$
\boxed{
S_{0,L}:=S_L\ \text{of (3A.67)},
\qquad
S_{0,E}:=S_E\ \text{of (3A.93)}.}
\tag{3D.5}
$$

For the exponent and source signs define

$$
\boxed{
\tau_L:=\frac{i}{\hbar},
\qquad
\tau_E:=-\frac1{\hbar},
\qquad
\upsilon_L:=+1,
\qquad
\upsilon_E:=-1.}
\tag{3D.6}
$$

The source superfields obey

$$
\begin{gathered}
\langle T^{\vee A},T_B\rangle_{\mathfrak g}
=\delta^A{}_B,
\qquad
J_{\mathcal V,R}=J_{\mathcal V,R,A}T^{\vee A},
\qquad
\bar D_{R\dot a}J_{\Phi,R,I}=0,
\qquad
D_{Ra}\widetilde J_{\Phi,R}^{I}=0,\\
[J_{\mathcal V,R}]=2,
\qquad
[J_{\Phi,R}]=[\widetilde J_{\Phi,R}]=2,
\qquad
\epsilon(J^{\rm phys})=\operatorname{gh}(J^{\rm phys})=0.
\end{gathered}
\tag{3D.7}
$$

Their real forms are

$$
\boxed{
J_{\mathcal V,L}^{\ddagger_L}=J_{\mathcal V,L},
\qquad
\widetilde J_{\Phi,L}=J_{\Phi,L}^{\ddagger_L},
\qquad
(J_{\mathcal V,E},J_{\Phi,E},\widetilde J_{\Phi,E})
\text{ are independent before the Euclidean source cycle}.}
\tag{3D.7a}
$$

Their matrix order is

$$
\boxed{
\mathscr J_R^{\rm phys}
:=
\int_{R,8}J_{\mathcal V,R,A}\mathcal V_R^A
+\int_{R,+}J_{\Phi,R,I}\Phi_R^I
+\int_{R,-}\widetilde\Phi_{R,I}\widetilde J_{\Phi,R}^{I}.}
\tag{3D.8}
$$

Thus the two source exponents are exactly

$$
\boxed{
\begin{aligned}
\tau_L(S_{0,L}+\upsilon_L\mathscr J_L^{\rm phys})
&=\frac{i}{\hbar}(S_{0,L}+\mathscr J_L^{\rm phys}),\\
\tau_E(S_{0,E}+\upsilon_E\mathscr J_E^{\rm phys})
&=-\frac1{\hbar}S_{0,E}+\frac1{\hbar}\mathscr J_E^{\rm phys}.
\end{aligned}}
\tag{3D.9}
$$

### 3D.2 Cylindrical coordinates and measure

Define the quadratic monomials and the ordered Grassmann monomial sets

$$
\begin{aligned}
\Theta_+&:=\vartheta^a\vartheta_a,
&
\Theta_-&:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a},\\
\mathscr M_+
&:=(1,\vartheta^1,\vartheta^2,\Theta_+),\\
\mathscr M_-
&:=(1,\bar\vartheta_{\dot1},\bar\vartheta_{\dot2},
\Theta_-),\\
\mathscr M_8
&:=\{m_+m_-:m_+\in\mathscr M_+,\ m_-\in\mathscr M_-\}.
\end{aligned}
\tag{3D.10}
$$

The top-monomial normalization is

$$
\boxed{
[\Theta_+]_F=1,
\qquad
[\Theta_-]_{\widetilde F}=1,
\qquad
[\Theta_+\Theta_-]_D=1.}
\tag{3D.11}
$$

For
\(\varsigma\in\{8,+,-\}\), set
\(x_{R,8}:=x_R\),
\(x_{R,+}:=y_R\), and
\(x_{R,-}:=\widetilde y_R\).
Fix boundary conditions and separate mode/dual-mode systems

$$
\int d^4x_R\,
u_{R,\nu,\varsigma}^{\,r}(x_{R,\varsigma})
u_{R,\nu,\varsigma s}(x_{R,\varsigma})
=\delta^r{}_s,
\qquad
r,s=1,\ldots,N_{R,\nu,\varsigma}^{x}.
\tag{3D.12}
$$

The boundary datum is explicit:

$$
\boxed{
\begin{gathered}
\mathfrak X_R\Subset\mathbb R_R^4,
\qquad
u_{R,\nu,\varsigma r}\in C_c^\infty(\mathfrak X_R),
\qquad
u_{R,\nu,\varsigma}^{\,r}\in C_c^\infty(\mathfrak X_R),\\
\operatorname{supp}u_{R,\nu,\varsigma r},
\operatorname{supp}u_{R,\nu,\varsigma}^{\,r}
\ \cap\ \mathcal U(\partial\mathfrak X_R)=\varnothing,
\qquad
[u_{R,\nu,\varsigma r}]=0,
\qquad
[u_{R,\nu,\varsigma}^{\,r}]=4,\\
N^x_{L,\nu,+}=N^x_{L,\nu,-},\qquad
\rho_{\nu,8}^{\,2}=\mathbf1,\qquad
\rho_{\nu,-}=\rho_{\nu,+}^{-1},\\
(u_{L,\nu,8r})^{\ddagger_L}
=u_{L,\nu,8\rho_{\nu,8}(r)},\qquad
(u_{L,\nu,8}^{\,r})^{\ddagger_L}
=u_{L,\nu,8}^{\,\rho_{\nu,8}(r)},\\
(u_{L,\nu,+r})^{\ddagger_L}
=u_{L,\nu,-\rho_{\nu,+}(r)},\qquad
(u_{L,\nu,+}^{\,r})^{\ddagger_L}
=u_{L,\nu,-}^{\,\rho_{\nu,+}(r)},\\
(u_{L,\nu,-r})^{\ddagger_L}
=u_{L,\nu,+\rho_{\nu,-}(r)},\qquad
(u_{L,\nu,-}^{\,r})^{\ddagger_L}
=u_{L,\nu,+}^{\,\rho_{\nu,-}(r)},\\
P_{L,\nu,8}\ddagger_L=\ddagger_LP_{L,\nu,8},\qquad
P_{L,\nu,-}\ddagger_L=\ddagger_LP_{L,\nu,+},\qquad
P_{L,\nu,+}\ddagger_L=\ddagger_LP_{L,\nu,-},\\
b(t):=
\begin{cases}
\exp[-(1-t^2)^{-1}],&|t|<1,\\
0,&|t|\ge1,
\end{cases}\\
h_{\nu r}(s):=
\prod_{\mu=0}^{3}
b\!\left(\dfrac{s^\mu-a_{\nu r}^{\mu}}
{\ell_{\nu r}^{\mu}}\right),\qquad
c_{\nu r}:=\int_{\mathfrak X^{\rm par}}d^4s\,
h_{\nu r}(s)^2>0,\\
\mathfrak w_L^{\rm ctr}(s):\ x_L^0=s^0,\ \boldsymbol x_L=\boldsymbol s,\qquad
\mathfrak w_E^{\rm ctr}(s):\ x_L^0=-is^0
\Longleftrightarrow x_E^4=s^0,\quad
\boldsymbol x_E=\boldsymbol s,\\
u_{R,\nu,\varsigma r}\circ\mathfrak w_R^{\rm ctr}=h_{\nu r},\qquad
u_{R,\nu,\varsigma}^{\,r}\circ\mathfrak w_R^{\rm ctr}
=c_{\nu r}^{-1}h_{\nu r},\\
\operatorname{Wick}_{\nu,\varsigma}
\bigl(u_{L,\nu,\varsigma r}\circ\mathfrak w_L^{\rm ctr}\bigr)
=u_{E,\nu,\varsigma r}\circ\mathfrak w_E^{\rm ctr},\qquad
\operatorname{Wick}_{\nu,\varsigma}
\bigl(u_{L,\nu,\varsigma}^{\,r}\circ\mathfrak w_L^{\rm ctr}\bigr)
=u_{E,\nu,\varsigma}^{\,r}\circ\mathfrak w_E^{\rm ctr}.
\end{gathered}}
\tag{3D.12a}
$$

Thus every spacetime integration by parts has zero boundary term at
fixed \((R,\nu)\).  The exhaustion
\(\mathfrak X_R\nearrow\mathbb R_R^4\)
is a separate regulator limit.

The dagger rows of (3D.12a), together with the induced Grassmann
monomial order, make the Lorentzian cutoff space and its Berezin
orientation closed under \(\ddagger_L\).  The bump rows give a
nonzero paired regulator on the two real contour parameters; disjoint
support proves (3D.12), separates every support from the boundary,
and preserves zero boundary flux.  The same real \(h_{\nu r}\) in the
paired \(+/-\) domains realizes the displayed dagger conditions.

The corresponding projector is

$$
\boxed{
(P_{R,\nu,\varsigma}f)(x_{R,\varsigma})
:=
\sum_{r=1}^{N_{R,\nu,\varsigma}^{x}}
u_{R,\nu,\varsigma r}(x_{R,\varsigma})
\int d^4x_R'\,
u_{R,\nu,\varsigma}^{\,r}(x_{R,\varsigma}')
f(x_{R,\varsigma}').}
\tag{3D.13}
$$

Let \(\iota_{R,\nu}\) be the inclusion of the finite coefficient
space into the declared superfield space.  Let \(\pi_{R,\nu}\) be
coefficient extraction with

$$
\boxed{
\pi_{R,\nu}\iota_{R,\nu}=\mathbf1,
\qquad
P_{R,\nu}=\iota_{R,\nu}\pi_{R,\nu}.}
\tag{3D.12b}
$$

The regulated functions are

$$
\boxed{
S_{0,R,\nu}(q):=S_{0,R}[\iota_{R,\nu}q],
\qquad
\mathscr J_{R,\nu}^{\rm phys}(J,q)
:=\mathscr J_R^{\rm phys}[J,\iota_{R,\nu}q].}
\tag{3D.13a}
$$

The symbol \(P_{R,\nu}\) below denotes the block-diagonal operator

$$
\boxed{
P_{R,\nu}
:=
P_{R,\nu,8}\oplus P_{R,\nu,+}\oplus P_{R,\nu,-}.}
\tag{3D.13b}
$$

No Wess--Zumino gauge is imposed.  The independent regulated fields are

$$
\boxed{
\begin{aligned}
\mathcal V_{R,\nu}^A
&=
\sum_{r=1}^{N_{R,\nu,8}^{x}}
\sum_{m\in\mathscr M_8}
v_{R,rm}^{A}\,u_{R,\nu,8r}(x_R)\,m,\\
\Phi_{R,\nu}^{I}
&=
\sum_{r=1}^{N_{R,\nu,+}^{x}}
\sum_{m\in\mathscr M_+}
\phi_{R,rm}^{I}\,u_{R,\nu,+r}(y_R)\,m,\\
\widetilde\Phi_{R,\nu,I}
&=
\sum_{r=1}^{N_{R,\nu,-}^{x}}
\sum_{m\in\mathscr M_-}
\widetilde\phi_{R,rm,I}\,
u_{R,\nu,-r}(\widetilde y_R)\,m.
\end{aligned}}
\tag{3D.14}
$$

If \(|m|\) is the Grassmann degree, then

$$
\boxed{
\begin{aligned}
\epsilon(v_{R,rm}^{A})&=|m|\pmod2,
&
[v_{R,rm}^{A}]&=\frac{|m|}{2},\\
\epsilon(\phi_{R,rm}^{I})&=|m|\pmod2,
&
[\phi_{R,rm}^{I}]&=1+\frac{|m|}{2},\\
\epsilon(\widetilde\phi_{R,rm,I})&=|m|\pmod2,
&
[\widetilde\phi_{R,rm,I}]&=1+\frac{|m|}{2}.
\end{aligned}}
\tag{3D.15}
$$

Every minimal ghost, non-minimal field, background field, background
partner, determinant auxiliary, and antifield introduced below uses
the same cylindrical rule.  For a homogeneous superfield \(X_R\) on
\(\Sigma_{R,\varsigma}\),

$$
\boxed{
\begin{aligned}
X_{R,\nu}
&=\sum_{r,m}x_{R,rm}
u_{R,\nu,\varsigma r}m,\\
\epsilon(x_{R,rm})
&=\epsilon_X+|m|\pmod2,
&
[x_{R,rm}]&=[X_R]+\frac{|m|}{2},\\
\widehat x_{R,rm}
&:=\mu^{-[x_{R,rm}]}x_{R,rm}.
\end{aligned}}
\tag{3D.15a}
$$

The antifield uses the dual superspace domain and the same rule with
its dimension fixed by (3D.52).  One total order \(\prec_\nu\) and its
reversed odd-coordinate integration order \(\succ_\nu\) are used on
the union of all coefficient sets.

Collect the coefficients as

$$
q_{R,\nu}^{\mathsf p}
\in
\left(
v_{R,rm}^{A},
\phi_{R,rm}^{I},
\widetilde\phi_{R,rm,I}
\right),
\qquad
\mathscr P_{R,\nu}^{\bar0}
:=\{\mathsf p:\epsilon_{\mathsf p}=0\},
\qquad
\mathscr P_{R,\nu}^{\bar1}
:=\{\mathsf p:\epsilon_{\mathsf p}=1\}.
\tag{3D.16}
$$

With one fixed reference scale \(\mu>0\), define dimensionless
coordinates

$$
\widehat q_{R,\nu}^{\mathsf p}
:=
\mu^{-[q_{R,\nu}^{\mathsf p}]}
q_{R,\nu}^{\mathsf p}.
\tag{3D.17}
$$

Choose one total coefficient order \(\prec_\nu\).  The coordinate
Berezin measure is

$$
\boxed{
\begin{aligned}
d\mu_{R,\nu}(q)
:={}&
\boldsymbol\varpi_{R,\nu}(\widehat q)\,
\prod_{\mathsf p\in\mathscr P_{R,\nu}^{\bar0}}^{\prec_\nu}
d\widehat q^{\mathsf p}\\
&\times
\prod_{\mathsf q\in\mathscr P_{R,\nu}^{\bar1}}^{\succ_\nu}
d\widehat q^{\mathsf q},
\end{aligned}}
\tag{3D.18}
$$

where \(\boldsymbol\varpi_{R,\nu}\) is an even nowhere-vanishing
quantization datum.  In hatted coordinates,

$$
\epsilon(\boldsymbol\varpi_{R,\nu})=0,
\qquad
\operatorname{gh}(\boldsymbol\varpi_{R,\nu})=0,
\qquad
[\boldsymbol\varpi_{R,\nu}]=0.
\tag{3D.18a}
$$

It is not fixed by \(S_{0,R}\).

For odd coordinates
\(\eta^1\prec_\nu\eta^2\prec_\nu\cdots\prec_\nu\eta^{n_1}\),
the orientation is

$$
\boxed{
\int
d\eta^{n_1}\cdots d\eta^2d\eta^1\,
\eta^1\eta^2\cdots\eta^{n_1}=1.}
\tag{3D.19}
$$

Let \(U_{R,\nu,\varsigma\mathsf a}\) and
\(U_{R,\nu,\varsigma}^{\mathsf a}\) be the induced primal and dual
super-bases for
\(\varsigma\in\{8,+,-\}\).  Define

$$
\boxed{
\delta_{R,\nu,\varsigma}(z,z')
:=
\sum_{\mathsf a}
U_{R,\nu,\varsigma\mathsf a}(z)
U_{R,\nu,\varsigma}^{\mathsf a}(z'),
\qquad
\int_{R,\varsigma}'\!
\delta_{R,\nu,\varsigma}(z,z')X_\varsigma(z')
=P_{R,\nu,\varsigma}X_\varsigma(z).}
\tag{3D.20}
$$

All constrained functional derivatives mean coefficient derivatives:

$$
\frac{\vec\delta\Phi_{R,\nu}^{I}(z)}
{\delta\Phi_{R,\nu}^{J}(z')}
=\delta^I{}_J\delta_{R,\nu,+}(z,z'),
\qquad
\frac{\vec\delta\widetilde\Phi_{R,\nu,I}(z)}
{\delta\widetilde\Phi_{R,\nu,J}(z')}
=\delta_I{}^J\delta_{R,\nu,-}(z,z').
\tag{3D.21}
$$

For an invertible parity-preserving coordinate change
\(\widehat q'=\widehat q'(\widehat q)\),

$$
\boxed{
\boldsymbol\varpi'_{R,\nu}(\widehat q')
=
\boldsymbol\varpi_{R,\nu}(\widehat q)
\operatorname{Ber}
\left(
\frac{\vec\partial\widehat q}
{\partial\widehat q'}
\right).}
\tag{3D.22}
$$

Hence neither a basis change nor a gauge-frame change preserves a
flat density until its Berezinian has been calculated.

The Lorentzian field cycle is the real form

$$
\boxed{
\mathfrak L_{L,\nu}:
\qquad
\mathcal V_{L,\nu}^{\ddagger_L}=\mathcal V_{L,\nu},
\qquad
\widetilde\Phi_{L,\nu}=\Phi_{L,\nu}^{\ddagger_L}.}
\tag{3D.23}
$$

Choose an even positive quadratic convergence functional
\(\mathscr Q_{L,\nu}\) on the bosonic coefficient cycle.  The
gauge-redundant Lorentzian cylindrical integral is

$$
\boxed{
Z^{\mathrm{red},\epsilon}_{L,\nu}[J_L]
:=
\int_{\mathfrak L_{L,\nu}}
d\mu_{L,\nu}\,
\exp\left[
\frac{i}{\hbar}(S_{0,L,\nu}+\mathscr J_{L,\nu}^{\rm phys})
-\epsilon\mathscr Q_{L,\nu}
\right],
\qquad
\epsilon>0.}
\tag{3D.24}
$$

The symbol

$$
Z^{\mathrm{red}}_{L,\nu}[J_L]
:=
\lim_{\epsilon\downarrow0}
Z^{\mathrm{red},\epsilon}_{L,\nu}[J_L]
\tag{3D.25}
$$

is admitted only when the distributional limit exists.

Intrinsic Euclidean variables are independent:

$$
\boxed{
(\mathcal V_{E,\nu},\Phi_{E,\nu},\widetilde\Phi_{E,\nu})
\ \text{are independent before choosing }
\mathfrak L_{E,\nu}.}
\tag{3D.26}
$$

For a declared middle-dimensional cycle
\(\mathfrak L_{E,\nu}\),

$$
\boxed{
Z^{\mathrm{red}}_{E,\nu}[J_E;\mathfrak L_{E,\nu}]
:=
\int_{\mathfrak L_{E,\nu}}
d\mu_{E,\nu}\,
\exp\left[
-\frac1{\hbar}S_{0,E,\nu}
+\frac1{\hbar}\mathscr J_{E,\nu}^{\rm phys}
\right].}
\tag{3D.27}
$$

The positive physical-field contour of (3A.102)--(3A.103) is allowed
only when its stated positivity hypotheses hold.  Ghost and
non-minimal cycles are fixed separately below.

### 3D.3 Change of variables and gauge degeneracy

Let \(\lambda X\) be an even infinitesimal displacement:

$$
\widehat q^{\prime\mathsf p}
=\widehat q^{\mathsf p}
+\lambda X^{\mathsf p}(\widehat q),
\qquad
\epsilon_\lambda=\epsilon_X,
\qquad
\epsilon(X^{\mathsf p})=\epsilon_{\mathsf p}+\epsilon_X.
\tag{3D.28}
$$

To first order in \(\lambda\),

$$
\begin{aligned}
\operatorname{Ber}
\left(
\frac{\vec\partial\widehat q'}
{\partial\widehat q}
\right)
&=
1+\lambda\operatorname{Str}
\left(
\frac{\vec\partial X}{\partial\widehat q}
\right),\\
\operatorname{Str}
\left(
\frac{\vec\partial X}{\partial\widehat q}
\right)
&:=
\sum_{\mathsf p}
(-1)^{\epsilon_{\mathsf p}(\epsilon_X+1)}
\frac{\vec\partial X^{\mathsf p}}
{\partial\widehat q^{\mathsf p}}.
\end{aligned}
\tag{3D.29}
$$

Define the density divergence by

$$
\boxed{
\operatorname{div}_{R,\nu}X
:=
\boldsymbol\varpi_{R,\nu}^{-1}
\sum_{\mathsf p}
(-1)^{\epsilon_{\mathsf p}(\epsilon_X+1)}
\frac{\vec\partial}
{\partial\widehat q^{\mathsf p}}
\left(
\boldsymbol\varpi_{R,\nu}X^{\mathsf p}
\right).}
\tag{3D.30}
$$

Use the two regulated exponents

$$
\boxed{
\begin{aligned}
\mathscr E_{L,\nu}^{\epsilon}
&:=\tau_L(S_{0,L,\nu}+\mathscr J_{L,\nu}^{\rm phys})
-\epsilon\mathscr Q_{L,\nu},
&\epsilon&>0,\\
\mathscr E_{E,\nu}
&:=\tau_E(S_{0,E,\nu}+\upsilon_E\mathscr J_{E,\nu}^{\rm phys}).
\end{aligned}}
\tag{3D.30a}
$$

If the transformed cycle has no boundary contribution, the exact
finite-dimensional identity is

$$
\boxed{
\begin{aligned}
0&=\int_{\mathfrak L_{L,\nu}}d\mu_{L,\nu}\,
e^{\mathscr E_{L,\nu}^{\epsilon}}
\left[
\operatorname{div}_{L,\nu}X
+\tau_LX(S_{0,L,\nu}+\mathscr J_{L,\nu}^{\rm phys})
-\epsilon X\mathscr Q_{L,\nu}
\right],\\
0&=\int_{\mathfrak L_{E,\nu}}d\mu_{E,\nu}\,
e^{\mathscr E_{E,\nu}}
\left[
\operatorname{div}_{E,\nu}X
+\tau_EX(S_{0,E,\nu}+\upsilon_E\mathscr J_{E,\nu}^{\rm phys})
\right].
\end{aligned}}
\tag{3D.31}
$$

Left and right derivatives are related by

$$
F\frac{\overleftarrow\partial}
{\partial\widehat q^{\mathsf p}}
=
(-1)^{\epsilon_{\mathsf p}(\epsilon_F+1)}
\frac{\vec\partial F}
{\partial\widehat q^{\mathsf p}}.
\tag{3D.32}
$$

The two integration-by-parts statements are therefore

$$
\boxed{
\begin{aligned}
0&=
\int_{\mathfrak L_{R,\nu}}
\prod_{\mathsf q\in\mathscr P^{\bar0}_{R,\nu}}^{\prec_\nu}
d\widehat q^{\mathsf q}
\prod_{\mathsf q\in\mathscr P^{\bar1}_{R,\nu}}^{\succ_\nu}
d\widehat q^{\mathsf q}\,
\frac{\vec\partial}
{\partial\widehat q^{\mathsf p}}
\left[
\boldsymbol\varpi_{R,\nu}
e^{\mathscr E_{R,\nu}}
\right],\\
0&=
\int_{\mathfrak L_{R,\nu}}
\prod_{\mathsf q\in\mathscr P^{\bar0}_{R,\nu}}^{\prec_\nu}
d\widehat q^{\mathsf q}
\prod_{\mathsf q\in\mathscr P^{\bar1}_{R,\nu}}^{\succ_\nu}
d\widehat q^{\mathsf q}\,
\left[
\boldsymbol\varpi_{R,\nu}
e^{\mathscr E_{R,\nu}}
\right]
\frac{\overleftarrow\partial}
{\partial\widehat q^{\mathsf p}}.
\end{aligned}}
\tag{3D.33}
$$

Here \(\mathscr E_{R,\nu}=\mathscr E_{L,\nu}^{\epsilon}\) for
\(R=L\) and \(\mathscr E_{R,\nu}=\mathscr E_{E,\nu}\) for \(R=E\).

Equation (3D.33) gives the regulated Schwinger--Dyson equation

$$
\boxed{
0=\int_{\mathfrak L_{R,\nu}}d\mu_{R,\nu}\,
e^{\mathscr E_{R,\nu}}
\left[
\boldsymbol\varpi_{R,\nu}^{-1}
\frac{\vec\partial\boldsymbol\varpi_{R,\nu}}
{\partial\widehat q^{\mathsf p}}
+\frac{\vec\partial\mathscr E_{R,\nu}}
{\partial\widehat q^{\mathsf p}}
\right].}
\tag{3D.34}
$$

For an arbitrary source-dependent \(X\), (3D.31) is the general
source Ward identity; BRST, supersymmetry, background, and split Ward
identities are specializations of the same equality.

The infinitesimal supergauge tangent is fixed by (3A.32):

$$
\boxed{
\begin{aligned}
\delta_{\Lambda,\widetilde\Lambda}\mathcal E_R
&=
i\widetilde\Lambda_R\mathcal E_R
-i\mathcal E_R\Lambda_R,\\
\delta_{\Lambda,\widetilde\Lambda}\Phi_R
&=i\Lambda_R\Phi_R,\\
\delta_{\Lambda,\widetilde\Lambda}\widetilde\Phi_R
&=-i\widetilde\Phi_R\widetilde\Lambda_R.
\end{aligned}}
\tag{3D.35}
$$

Since

$$
\mathcal E_R^{-1}\delta\mathcal E_R
=
\frac{1-e^{-\operatorname{ad}_{\mathcal V_R}}}
{\operatorname{ad}_{\mathcal V_R}}
\delta\mathcal V_R,
\tag{3D.36}
$$

the exact prepotential tangent in the local exponential chart is

$$
\boxed{
\delta\mathcal V_R
=
\frac{\operatorname{ad}_{\mathcal V_R}}
{1-e^{-\operatorname{ad}_{\mathcal V_R}}}
\left(
i e^{-\operatorname{ad}_{\mathcal V_R}}
\widetilde\Lambda_R
-i\Lambda_R
\right).}
\tag{3D.37}
$$

Writing the untruncated physical-field tangent as
\(\delta\varphi^{\mathfrak p}
=R_{\boldsymbol\lambda}^{\mathfrak p}(\varphi)
\delta\gamma^{\boldsymbol\lambda}\), exact classical gauge invariance
gives

$$
\frac{\vec\delta S_{0,R}}
{\delta\varphi^{\mathfrak p}}
R_{\boldsymbol\lambda}^{\mathfrak p}=0.
\tag{3D.38}
$$

At a stationary point,

$$
\boxed{
\frac{\vec\delta^{\,2}S_{0,R}}
{\delta\varphi^{\mathfrak p}\delta\varphi^{\mathfrak q}}
R_{\boldsymbol\lambda}^{\mathfrak q}=0,}
\tag{3D.39}
$$

so the untruncated quadratic operator has gauge zero modes.  A generic
finite projector need not preserve (3D.38); its exact defect is retained
in (3D.60) below.

In a regular local dimensionless orbit chart
\(\widehat q=\widehat q(\widehat y,\widehat\gamma)\),

$$
d\mu_{R,\nu}(q)
=
\boldsymbol\varpi_{R,\nu}
(\widehat q(\widehat y,\widehat\gamma))
\operatorname{Ber}
\left(
\frac{\vec\partial\widehat q}
{\partial(\widehat y,\widehat\gamma)}
\right)
D_{\prec_\nu}\widehat y\,
D_{\prec_\nu}\widehat\gamma.
\tag{3D.40}
$$

An even noncompact orbit coordinate and an odd orbit coordinate obey

$$
\int_{\mathbb R}dt\,1\ \text{does not converge},
\qquad
\int d\eta_{\rm orb}\,1=0.
\tag{3D.41}
$$

Therefore neither expression is defined:

$$
\boxed{
\frac{Z^{\mathrm{red}}_{R,\nu}}
{\operatorname{Vol}\mathcal G_{R,\nu}},
\qquad
\frac{Z^{\mathrm{red}}_{R,\nu}[J]}
{Z^{\mathrm{red}}_{R,\nu}[0]}.}
\tag{3D.42}
$$

### 3D.4 Exact classical BRST differential

Introduce one chiral and one antichiral adjoint ghost:

$$
\boxed{
\begin{gathered}
\mathfrak c_R=\mathfrak c_R^AT_A,
\qquad
\widetilde{\mathfrak c}_R
=\widetilde{\mathfrak c}_R^AT_A,\\
\bar D_{R\dot a}\mathfrak c_R=0,
\qquad
D_{Ra}\widetilde{\mathfrak c}_R=0,\\
\epsilon_{\mathfrak c_R}
=\epsilon_{\widetilde{\mathfrak c}_R}=1,
\qquad
\operatorname{gh}(\mathfrak c_R)
=\operatorname{gh}(\widetilde{\mathfrak c}_R)=1,
\qquad
[\mathfrak c_R]
=[\widetilde{\mathfrak c}_R]=0.
\end{gathered}}
\tag{3D.43}
$$

The odd derivation \(\mathbf s_R\) is fixed by

$$
\boxed{
\epsilon(\mathbf s_R)=1,
\qquad
\operatorname{gh}(\mathbf s_R)=1,
\qquad
[\mathbf s_R]=0.}
\tag{3D.43a}
$$

$$
\boxed{
\begin{aligned}
\mathbf s_R\mathcal E_R
&=i\widetilde{\mathfrak c}_R\mathcal E_R
-i\mathcal E_R\mathfrak c_R,\\
\mathbf s_R\mathfrak c_R&=i\mathfrak c_R^2,
&
\mathbf s_R\widetilde{\mathfrak c}_R
&=i\widetilde{\mathfrak c}_R^2,\\
\mathbf s_R\Phi_R&=i\mathfrak c_R\Phi_R,
&
\mathbf s_R\widetilde\Phi_R
&=-i\widetilde\Phi_R\widetilde{\mathfrak c}_R.
\end{aligned}}
\tag{3D.44}
$$

The component ghost rule follows without an imported convention:

$$
\begin{aligned}
\mathfrak c_R^2
&=
\frac12\mathfrak c_R^A\mathfrak c_R^B[T_A,T_B]\\
&=
\frac i2c_{AB}{}^C
\mathfrak c_R^A\mathfrak c_R^BT_C,\\
\mathbf s_R\mathfrak c_R^C
&=
-\frac12c_{AB}{}^C
\mathfrak c_R^A\mathfrak c_R^B,\\
\mathbf s_R^2\mathfrak c_R
&=i\left[
(\mathbf s_R\mathfrak c_R)\mathfrak c_R
-\mathfrak c_R(\mathbf s_R\mathfrak c_R)
\right]\\
&=i\left[
i\mathfrak c_R^2\mathfrak c_R
-i\mathfrak c_R\mathfrak c_R^2
\right]=0,\\
\mathbf s_R^2\widetilde{\mathfrak c}_R
&=i\left[
i\widetilde{\mathfrak c}_R^2\widetilde{\mathfrak c}_R
-i\widetilde{\mathfrak c}_R
\widetilde{\mathfrak c}_R^2
\right]=0.
\end{aligned}
\tag{3D.45}
$$

Using the odd Leibniz rule, the bridge nilpotency is

$$
\begin{aligned}
\mathbf s_R^2\mathcal E_R
={}&
i(\mathbf s_R\widetilde{\mathfrak c}_R)\mathcal E_R
-i\widetilde{\mathfrak c}_R(\mathbf s_R\mathcal E_R)
-i(\mathbf s_R\mathcal E_R)\mathfrak c_R
-i\mathcal E_R(\mathbf s_R\mathfrak c_R)\\
={}&
-\widetilde{\mathfrak c}_R^2\mathcal E_R
+\widetilde{\mathfrak c}_R^2\mathcal E_R
-\widetilde{\mathfrak c}_R\mathcal E_R\mathfrak c_R
+\widetilde{\mathfrak c}_R\mathcal E_R\mathfrak c_R\\
&-\mathcal E_R\mathfrak c_R^2
+\mathcal E_R\mathfrak c_R^2\\
={}&0.
\end{aligned}
\tag{3D.46}
$$

The matter nilpotency is

$$
\boxed{
\begin{aligned}
\mathbf s_R^2\Phi_R
&=
i(i\mathfrak c_R^2)\Phi_R
-i\mathfrak c_R(i\mathfrak c_R\Phi_R)=0,\\
\mathbf s_R^2\widetilde\Phi_R
&=
-i(-i\widetilde\Phi_R\widetilde{\mathfrak c}_R)
\widetilde{\mathfrak c}_R
-i\widetilde\Phi_R(i\widetilde{\mathfrak c}_R^2)=0.
\end{aligned}}
\tag{3D.47}
$$

Equation (3D.36) converts the bridge rule to the exact
Lie-algebra-prepotential rule:

$$
\boxed{
\mathbf s_R\mathcal V_R
=
\frac{\operatorname{ad}_{\mathcal V_R}}
{1-e^{-\operatorname{ad}_{\mathcal V_R}}}
\left(
i e^{-\operatorname{ad}_{\mathcal V_R}}
\widetilde{\mathfrak c}_R
-i\mathfrak c_R
\right).}
\tag{3D.48}
$$

The inverse differential in (3D.48) is used only inside the connected
exponential chart.  Since \(\mathbf s_R^2\) is an even derivation,

$$
\boxed{
\mathbf s_R^2(XY)
=(\mathbf s_R^2X)Y+X(\mathbf s_R^2Y),
\qquad
\mathbf s_R^2\mathcal V_R
=\mathbf s_R^2(\log\mathcal E_R)=0.}
\tag{3D.48a}
$$

Lorentzian reality and intrinsic Euclidean independence are

$$
\boxed{
\begin{aligned}
\widetilde{\mathfrak c}_L
&=\mathfrak c_L^{\ddagger_L},
&
(\mathbf s_LX)^{\ddagger_L}
&=(-1)^{\epsilon_X}\mathbf s_L(X^{\ddagger_L}),\\
(\mathfrak c_E,\widetilde{\mathfrak c}_E)
&\text{ are independent before the Euclidean contour}.
\end{aligned}}
\tag{3D.49}
$$

The conditions (3A.68)--(3A.72) and the rules (3D.44) give

$$
\boxed{
\mathbf s_RS_{0,R}=0,
\qquad
\mathbf s_R^2=0
\quad\text{on the untruncated local field algebra}.}
\tag{3D.50}
$$

### 3D.5 Minimal BV space and classical master equation

The field--antifield ledger is

$$
\begin{array}{c|c|c|c|c|c}
X&\Sigma_X&\epsilon_X&\operatorname{gh}(X)&[X]&[X^\star]\\ \hline
\mathcal V&8&0&0&0&2\\
\Phi^I&+&0&0&1&2\\
\widetilde\Phi_I&-&0&0&1&2\\
\mathfrak c&+&1&1&0&3\\
\widetilde{\mathfrak c}&-&1&1&0&3
\end{array}.
\tag{3D.51}
$$

If \(d_8:=2\) and \(d_+=d_-:=3\) are the required integrand
dimensions, every row of (3D.51) obeys

$$
\boxed{
[X^\star]=d_{\Sigma_X}-[X],
\qquad
\epsilon_{X^\star}=\epsilon_X+1,
\qquad
\operatorname{gh}(X^\star)=-1-\operatorname{gh}(X).}
\tag{3D.52}
$$

The Lorentzian cotangent real form and intrinsic Euclidean
independence are

$$
\boxed{
(X_L^\star)^{\ddagger_L}
=-(X_L^{\ddagger_L})^\star,
\qquad
(X_E^\star,\widetilde X_E^\star)
\text{ are independent before the Euclidean cycle}.}
\tag{3D.52a}
$$

The ordered dual pairings are

$$
\boxed{
\begin{aligned}
\langle\mathcal V^\star,Y\rangle_{R,8}
&:=\int_{R,8}\mathcal V^\star_{R,A}Y_R^A,\\
\langle\Phi^\star,Y\rangle_{R,+}
&:=\int_{R,+}\Phi^\star_{R,I}Y_R^I,\\
\langle\widetilde\Phi^\star,\widetilde Y\rangle_{R,-}
&:=\int_{R,-}\widetilde\Phi_R^{\star I}\widetilde Y_{R,I},\\
\langle\mathfrak c^\star,\gamma\rangle_{R,+}
&:=\int_{R,+}\mathfrak c^\star_{R,A}\gamma_R^A,\\
\langle\widetilde{\mathfrak c}^\star,\widetilde\gamma\rangle_{R,-}
&:=\int_{R,-}\widetilde{\mathfrak c}^\star_{R,A}
\widetilde\gamma_R^A.
\end{aligned}}
\tag{3D.53}
$$

Let \(Q_R^{\mathfrak i}\) denote all untruncated fields and
\(Q_{R,\nu}^{\mathsf i}\) all regulated field coefficients; their
ordered duals are \(Q^\star_{R,\mathfrak i}\) and
\(Q^\star_{R,\nu,\mathsf i}\).  Set
\(\widehat Q^{\mathsf i}:=\mu^{-[Q^{\mathsf i}]}Q^{\mathsf i}\) and
\(\widehat Q^\star_{\mathsf i}
:=\mu^{-[Q^\star_{\mathsf i}]}Q^\star_{\mathsf i}\).
The functional and dimensionless coefficient antibrackets are

$$
\boxed{
\begin{aligned}
(F,G)_R
&:=\sum_X\int_{\Sigma_X}
\left[
F\frac{\overleftarrow\delta}{\delta X_R}
\frac{\vec\delta G}{\delta X_R^\star}
-F\frac{\overleftarrow\delta}{\delta X_R^\star}
\frac{\vec\delta G}{\delta X_R}
\right],\\
(F,G)_{R,\nu}
&:=
\sum_{\mathsf i}
\left[
F\frac{\overleftarrow\partial}
{\partial\widehat Q^{\mathsf i}}
\frac{\vec\partial G}
{\partial\widehat Q^\star_{\mathsf i}}
-
F\frac{\overleftarrow\partial}
{\partial\widehat Q^\star_{\mathsf i}}
\frac{\vec\partial G}
{\partial\widehat Q^{\mathsf i}}
\right].
\end{aligned}}
\tag{3D.54}
$$

It is pinned by

$$
\boxed{
\begin{gathered}
(\widehat Q^{\mathsf i},\widehat Q^\star_{\mathsf j})_{R,\nu}
=\delta^{\mathsf i}{}_{\mathsf j},
\qquad
\epsilon_{(F,G)}=\epsilon_F+\epsilon_G+1,\\
\operatorname{gh}(F,G)
=\operatorname{gh}(F)+\operatorname{gh}(G)+1,\\
(F,G)
=-(-1)^{(\epsilon_F+1)(\epsilon_G+1)}(G,F).
\end{gathered}}
\tag{3D.55}
$$

The untruncated minimal master action is

$$
\boxed{
\begin{aligned}
S_{\min,R}
:={}&S_{0,R}
+\langle\mathcal V^\star,\mathbf s_R\mathcal V\rangle_{R,8}\\
&+\langle\Phi^\star,\mathbf s_R\Phi\rangle_{R,+}
+\langle\widetilde\Phi^\star,\mathbf s_R\widetilde\Phi\rangle_{R,-}\\
&-\langle\mathfrak c^\star,\mathbf s_R\mathfrak c\rangle_{R,+}
-\langle\widetilde{\mathfrak c}^\star,
\mathbf s_R\widetilde{\mathfrak c}\rangle_{R,-}.
\end{aligned}}
\tag{3D.56}
$$

Equivalently, in collective DeWitt notation,

$$
S_{\min,R}
=S_{0,R}
+\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
Q^\star_{R,\mathfrak i}\mathbf s_RQ_R^{\mathfrak i}.
\tag{3D.56a}
$$

Direct differentiation gives

$$
\begin{aligned}
\frac12(S_{\min,R},S_{\min,R})_R
={}&
\mathbf s_RS_{0,R}
+\sum_{\mathfrak i}(-1)^{\epsilon_{\mathfrak i}}
Q^\star_{R,\mathfrak i}\mathbf s_R^2Q_R^{\mathfrak i}\\
={}&0.
\end{aligned}
\tag{3D.57}
$$

The BRST differential is therefore Hamiltonian:

$$
\boxed{
\mathbf s_RF=(S_{\min,R},F)_R,
\qquad
\mathbf s_R^2F
=\frac12((S_{\min,R},S_{\min,R})_R,F)_R=0.}
\tag{3D.58}
$$

For a generic finite projector define

$$
\boxed{
\mathbf s_{R,\nu}:=\pi_{R,\nu}\mathbf s_R\iota_{R,\nu},
\qquad
\mathfrak R_{R,\nu}^{\mathsf i}
:=\mathbf s_{R,\nu}^2Q_{R,\nu}^{\mathsf i}.}
\tag{3D.59}
$$

The regulated master action obtained from (3D.56) obeys the identity

$$
\boxed{
\frac12(S_{\min,R,\nu},S_{\min,R,\nu})_{R,\nu}
=
\mathbf s_{R,\nu}S_{0,R,\nu}
+
\sum_{\mathsf i}(-1)^{\epsilon_{\mathsf i}}
Q^\star_{R,\nu,\mathsf i}
\mathfrak R_{R,\nu}^{\mathsf i}.}
\tag{3D.60}
$$

Equation (3D.60), not zero, is the generic finite-cutoff statement.
Its right-hand side vanishes only after closure of the regulated
product, regulator invariance of \(S_{0,R,\nu}\), and
\(\mathbf s_{R,\nu}^2=0\) have each been proved.

### 3D.6 BV density, Laplacian, and quantum master equation

Choose an even BV density
\(\widehat{\boldsymbol\varpi}_{R,\nu}(Q,Q^\star)\) in the Darboux
chart.  It is nowhere vanishing, so its logarithm is defined, and

$$
\boxed{
\epsilon(\widehat{\boldsymbol\varpi}_{R,\nu})=0,
\qquad
\operatorname{gh}(\widehat{\boldsymbol\varpi}_{R,\nu})=0,
\qquad
[\widehat{\boldsymbol\varpi}_{R,\nu}]=0,
\qquad
\epsilon(\Delta_{R,\nu})=1,
\qquad
\operatorname{gh}(\Delta_{R,\nu})=1,
\qquad
[\Delta_{R,\nu}]=0.}
\tag{3D.60a}
$$

Define

$$
\boxed{
\begin{aligned}
\Delta_{0,R,\nu}F
&:=
\sum_{\mathsf i}
(-1)^{\epsilon_{\mathsf i}}
\frac{\vec\partial}{\partial\widehat Q^{\mathsf i}}
\frac{\vec\partial F}{\partial\widehat Q^\star_{\mathsf i}},\\
\Delta_{R,\nu}F
&:=
\Delta_{0,R,\nu}F
+\frac12
\left(
\log\widehat{\boldsymbol\varpi}_{R,\nu},F
\right)_{R,\nu}.
\end{aligned}}
\tag{3D.61}
$$

The sign of (3D.61) is fixed by the second-order identity

$$
\boxed{
\Delta(FG)
=(\Delta F)G
+(-1)^{\epsilon_F}F\Delta G
+(-1)^{\epsilon_F}(F,G).}
\tag{3D.62}
$$

A BV-compatible density satisfies

$$
\boxed{\Delta_{R,\nu}^2=0.}
\tag{3D.63}
$$

If (3D.63) fails, the modular defect
\(\mathfrak M_{R,\nu}:=\Delta_{R,\nu}^2\) is retained and the
quantum master equation is not asserted.

For an even quantum master action \(W_{R,\nu}\), the two QME
operators are

$$
\boxed{
\begin{aligned}
\mathfrak O^{\rm BV}_{L,\nu}[W]
&:=
\frac12(W_{L,\nu},W_{L,\nu})_{L,\nu}
-i\hbar\Delta_{L,\nu}W_{L,\nu},\\
\mathfrak O^{\rm BV}_{E,\nu}[W]
&:=
\frac12(W_{E,\nu},W_{E,\nu})_{E,\nu}
-\hbar\Delta_{E,\nu}W_{E,\nu}.
\end{aligned}}
\tag{3D.64}
$$

They follow directly from

$$
\boxed{
\begin{aligned}
\Delta_{L,\nu}e^{\,iW_{L,\nu}/\hbar}
&=
-\frac1{\hbar^2}
\mathfrak O^{\rm BV}_{L,\nu}[W]\,
e^{\,iW_{L,\nu}/\hbar},\\
\Delta_{E,\nu}e^{-W_{E,\nu}/\hbar}
&=
\frac1{\hbar^2}
\mathfrak O^{\rm BV}_{E,\nu}[W]\,
e^{-W_{E,\nu}/\hbar}.
\end{aligned}}
\tag{3D.65}
$$

Thus QME means

$$
\boxed{
\mathfrak O^{\rm BV}_{L,\nu}[W]=0,
\qquad
\mathfrak O^{\rm BV}_{E,\nu}[W]=0,}
\tag{3D.66}
$$

only for a regulator and density for which the two equalities have
been proved.  Otherwise \(\mathfrak O^{\rm BV}_{R,\nu}\) is the regulated BV
anomaly functional.

When \(\Delta_{R,\nu}^2=0\), the Jacobi identity and (3D.62) give

$$
\boxed{
\begin{aligned}
(W_{L,\nu},\mathfrak O^{\rm BV}_{L,\nu})_{L,\nu}
-i\hbar\Delta_{L,\nu}\mathfrak O^{\rm BV}_{L,\nu}&=0,\\
(W_{E,\nu},\mathfrak O^{\rm BV}_{E,\nu})_{E,\nu}
-\hbar\Delta_{E,\nu}\mathfrak O^{\rm BV}_{E,\nu}&=0.
\end{aligned}}
\tag{3D.67}
$$

For
\(W_{\min,R,\nu}=S_{\min,R,\nu}+\hbar M_{1,R,\nu}\),
the order-\(\hbar\) equations are

$$
\boxed{
\begin{aligned}
\mathbf s_{L,\nu}M_{1,L,\nu}
&=i\Delta_{L,\nu}S_{\min,L,\nu},\\
\mathbf s_{E,\nu}M_{1,E,\nu}
&=\Delta_{E,\nu}S_{\min,E,\nu},
\end{aligned}}
\tag{3D.68}
$$

after the classical defect (3D.60) vanishes.

Set
\(\mathfrak e_L^{\rm QME}:=i\),
\(\mathfrak e_E^{\rm QME}:=1\), and

$$
W_{\min,R,\nu}
=\sum_{n=0}^{\infty}\hbar^nM_{n,R,\nu},
\qquad
M_{0,R,\nu}:=S_{\min,R,\nu}.
\tag{3D.68a}
$$

After the classical defect (3D.60) vanishes, the exact
order-by-order anomaly-cancellation condition is

$$
\boxed{
\mathbf s_{R,\nu}M_{n,R,\nu}
=\mathfrak e_R^{\rm QME}\Delta_{R,\nu}M_{n-1,R,\nu}
-\frac12\sum_{k=1}^{n-1}
(M_{k,R,\nu},M_{n-k,R,\nu})_{R,\nu},
\qquad n\ge1.}
\tag{3D.69}
$$

together with a regulator-removal limit preserving the QME.  No
anomaly coefficient is imported into (3D.69).

### 3D.7 Arbitrary contractible non-minimal sector

Choose disjoint finite sets \(\mathscr R_{\rm nm}^{\rm base}\) and
\(\mathscr R_{\rm NK}^{\rm BV}\), and set
\(\mathscr R_{\rm nm}:=\mathscr R_{\rm nm}^{\rm base}
\sqcup\mathscr R_{\rm NK}^{\rm BV}\).  The second set is empty on
every branch except the admitted BV--NK branch of (3D.96b).  For every
\(\ell\in\mathscr R_{\rm nm}\), choose a superspace domain
\(\Sigma_{R,\ell}\in\{\Sigma_{R,8},\Sigma_{R,+},\Sigma_{R,-}\}\)
and a doublet

$$
\boxed{
\begin{gathered}
\mathbf s_R\mathfrak u_{R,\ell}=\mathfrak v_{R,\ell},
\qquad
\mathbf s_R\mathfrak v_{R,\ell}=0,
\qquad
\ell\in\mathscr R_{\rm nm},\\
\epsilon_{\mathfrak u_\ell}\in\mathbb Z_2,
\qquad
\operatorname{gh}(\mathfrak u_\ell)\in\mathbb Z,
\qquad
[\mathfrak u_\ell]\in\tfrac12\mathbb Z,\\
\epsilon_{\mathfrak v_\ell}=\epsilon_{\mathfrak u_\ell}+1,
\qquad
\operatorname{gh}(\mathfrak v_\ell)
=\operatorname{gh}(\mathfrak u_\ell)+1,
\qquad
[\mathfrak v_\ell]=[\mathfrak u_\ell].
\end{gathered}}
\tag{3D.70}
$$

The Lorentzian non-minimal index set carries an involution
\(\ell\mapsto\ell^{\ddagger}\) with
\(\Sigma_{L,+}^{\ddagger}=\Sigma_{L,-}\) and
\(\Sigma_{L,8}^{\ddagger}=\Sigma_{L,8}\).  Its cycle obeys

$$
\boxed{
(\mathfrak u_{L,\ell})^{\ddagger_L}
=(-1)^{\epsilon_{\mathfrak u_\ell}}
\mathfrak u_{L,\ell^{\ddagger}},
\qquad
(\mathfrak v_{L,\ell})^{\ddagger_L}
=\mathfrak v_{L,\ell^{\ddagger}},
\qquad
(\ell^{\ddagger})^{\ddagger}=\ell.}
\tag{3D.70a}
$$

Intrinsic Euclidean partners are independent before the cycle.

The stabilized master action is

$$
\boxed{
S_{\rm nm,R}
:=
S_{\min,R}
+
\sum_{\ell\in\mathscr R_{\rm nm}}
(-1)^{\epsilon_{\mathfrak u_\ell}}
\int_{\Sigma_{R,\ell}}
\mathfrak u^\star_{R,\ell}\mathfrak v_{R,\ell}.}
\tag{3D.71}
$$

Let

$$
\boxed{
\begin{aligned}
S_{\rm triv,R}
&:=S_{\rm triv,base,R}+S_{\rm triv,NK,R},\\
S_{\rm triv,base,R}
&:=\sum_{\ell\in\mathscr R_{\rm nm}^{\rm base}}
(-1)^{\epsilon_{\mathfrak u_\ell}}
\int_{\Sigma_{R,\ell}}
\mathfrak u^\star_{R,\ell}\mathfrak v_{R,\ell},\\
S_{\rm triv,NK,R}
&:=\sum_{\ell\in\mathscr R_{\rm NK}^{\rm BV}}
(-1)^{\epsilon_{\mathfrak u_\ell}}
\int_{\Sigma_{R,\ell}}
\mathfrak u^\star_{R,\ell}\mathfrak v_{R,\ell},\\
W_{\rm nm,R,\nu}
&:=W_{\min,R,\nu}+S_{\rm triv,R,\nu},\\
\mathfrak O_{R,\nu}^{\rm BV}[W_{\rm nm}]
&=\mathfrak O_{R,\nu}^{\rm BV}[W_{\min}]
-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm nm,R,\nu}S_{\rm triv,R,\nu}.
\end{aligned}}
\tag{3D.71b}
$$

The last term vanishes only for a density whose divergence on every
contractible pair vanishes; otherwise it is retained in the quantum
action recursion.

Choose the non-minimal BV density and Laplacian by

$$
\boxed{
\begin{aligned}
\widehat{\boldsymbol\varpi}_{\rm triv,R,\nu}
&:=\widehat{\boldsymbol\varpi}_{\rm triv,base,R,\nu}
\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu},\\
\widehat{\boldsymbol\varpi}_{\rm nm,R,\nu}
&:=\widehat{\boldsymbol\varpi}_{R,\nu}
\widehat{\boldsymbol\varpi}_{\rm triv,base,R,\nu}
\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu},\\
\Delta_{\rm nm,R,\nu}
&:=\Delta[\widehat{\boldsymbol\varpi}_{\rm nm,R,\nu}].
\end{aligned}}
\tag{3D.71c}
$$

Here \(\widehat{\boldsymbol\varpi}_{\rm triv,base,R,\nu}\) and
\(\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu}\) are even,
ghost-number-zero, dimensionless densities on their corresponding
doublets and antifield pairs.  On the admitted BV--NK branch the
normalization of \(\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu}\) is
fixed by the exact graph integral in (3D.96b); it is not an arbitrary
extra multiplicative constant.  On every non-BV--NK branch
\(\mathscr R_{\rm NK}^{\rm BV}=\varnothing\) and
\(\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu}=1\).
The notation \(\Delta[\rho]\) means the construction (3D.61) with
density \(\rho\).

On the full non-minimal BV polynomial algebra,

$$
\boxed{
\mathbf s_R\mathfrak u_\ell^\star=0,
\qquad
\mathbf s_R\mathfrak v_\ell^\star
=(-1)^{\epsilon_{\mathfrak u_\ell}}
\mathfrak u_\ell^\star.}
\tag{3D.71a}
$$

Define

$$
N_{\rm nm}
:=
\sum_{\ell}
\left(
\mathfrak u_\ell\frac{\vec\partial}{\partial\mathfrak u_\ell}
+\mathfrak v_\ell\frac{\vec\partial}{\partial\mathfrak v_\ell}
+\mathfrak u_\ell^\star
\frac{\vec\partial}{\partial\mathfrak u_\ell^\star}
+\mathfrak v_\ell^\star
\frac{\vec\partial}{\partial\mathfrak v_\ell^\star}
\right),
\qquad
h_{\rm nm}
:=
\sum_\ell\left[
\mathfrak u_\ell
\frac{\vec\partial}{\partial\mathfrak v_\ell}
+(-1)^{\epsilon_{\mathfrak u_\ell}}
\mathfrak v_\ell^\star
\frac{\vec\partial}{\partial\mathfrak u_\ell^\star}
\right].
\tag{3D.72}
$$

Direct action on each generator gives

$$
\boxed{
\{\mathbf s_R,h_{\rm nm}\}=N_{\rm nm},
\qquad
\mathbf s_RF=0,\quad N_{\rm nm}F=kF,\quad k>0
\ \Longrightarrow\
F=\mathbf s_R\!\left(\frac1k h_{\rm nm}F\right).}
\tag{3D.73}
$$

Thus adjoining (3D.70) changes no positive-nonminimal-degree BRST
cohomology.  Define the antighost subset and the gauge condition
encoded by a general gauge fermion by

$$
\boxed{
\begin{aligned}
\mathscr R_{\rm ag}
&:=\{\ell\in\mathscr R_{\rm nm}:
\epsilon_{\mathfrak u_\ell}=1,
\ \operatorname{gh}(\mathfrak u_\ell)=-1\},\\
(\mathcal F_{\Psi,R})_\ell
&:=\left.
\frac{\vec\delta\Psi_R}{\delta\mathfrak u_{R,\ell}}
\right|_{\mathfrak u=\mathfrak v=0},
\qquad \ell\in\mathscr R_{\rm ag},\\
(\mathscr R^{\rm g}_{R}\gamma)^{\mathfrak p}
&:=R_{\boldsymbol\lambda}^{\mathfrak p}(\varphi)
\gamma^{\boldsymbol\lambda},\\
\mathcal F_{\Psi,R,\nu}
&:=\pi_{\mathscr F,R,\nu}
\mathcal F_{\Psi,R}\iota_{R,\nu},\\
\mathscr R^{\rm g}_{R,\nu}
&:=\pi_{R,\nu}\mathscr R^{\rm g}_{R}
\iota_{\mathscr G,R,\nu},\\
\mathscr G_{\Psi,R,\nu}
&:=\operatorname{Im}\iota_{\mathscr G,R,\nu},
\qquad
\mathscr F_{\Psi,R,\nu}
:=\operatorname{Im}\pi_{\mathscr F,R,\nu},\\
\mathcal M_{\Psi,R,\nu}^{\rm FP}
&:=d\mathcal F_{\Psi,R,\nu}
\circ\mathscr R^{\rm g}_{R,\nu},
\qquad
\mathcal M_{\Psi,R,\nu}^{\rm FP}:
\mathscr G_{\Psi,R,\nu}
\longrightarrow\mathscr F_{\Psi,R,\nu},\\
\mathscr H_{\Psi,R,\nu}
:=\ker\mathcal M_{\Psi,R,\nu}^{\rm FP}.
\end{aligned}}
\tag{3D.73a}
$$

The admissible gauge-fermion family is defined by

$$
\boxed{
\begin{aligned}
\mathfrak G_R
:=\{\Psi_R:\;&
\epsilon_{\Psi_R}=1,\quad
\operatorname{gh}(\Psi_R)=-1,\quad
[\Psi_R]=0,\quad
\Psi_R\ \text{local},\\
&
\Psi_R\ \text{background scalar},\quad
\mathcal M_{\Psi,R,\nu}^{\rm FP,\perp}:
\mathscr G_{\Psi,R,\nu}^{\perp}
\overset{\cong}{\longrightarrow}
\mathscr F_{\Psi,R,\nu}^{\perp},\\
&
\operatorname{Hess}S_{\Psi,R,\nu}
\big|_{\mathscr H_{\Psi,R,\nu}^{\perp}}
\text{ is nondegenerate}\}.
\end{aligned}}
\tag{3D.74}
$$

The superscript \(\perp\) denotes chosen complements to the kernel and
cokernel.  For the standard family (3D.89),
\(\mathcal F_{\Psi,R}=\mathcal F_R\) and
\(\mathcal M_{\Psi,R,\nu}^{\rm FP}
=\mathcal M_{R,\nu}^{\rm FP}\).

Lorentzian and Euclidean conditions are

$$
\boxed{
\Psi_L^{\ddagger_L}=-\Psi_L,
\qquad
(\mathbf s_L\Psi_L)^{\ddagger_L}=\mathbf s_L\Psi_L,
\qquad
\Psi_E(\text{tilded},\text{untilded})
\ \text{contains independent Euclidean arguments}.}
\tag{3D.75}
$$

For \(\Psi_R\in\mathfrak G_R\), introduce independent external
Zinn--Justin antifield sources \(Q_R^{\star{\rm ext}}\).  The shifted
gauge-fixing Lagrangian submanifold is

$$
\boxed{
\epsilon(Q^{\star{\rm ext}}_{\mathsf i})
=\epsilon(Q^{\mathsf i})+1,
\qquad
\operatorname{gh}(Q^{\star{\rm ext}}_{\mathsf i})
=-1-\operatorname{gh}(Q^{\mathsf i}),
\qquad
[Q^{\star{\rm ext}}_{\mathsf i}]
=[Q^\star_{\mathsf i}],
\qquad
\widehat Q^{\star{\rm ext}}_{\mathsf i}
:=\mu^{-[Q^{\star{\rm ext}}_{\mathsf i}]}
Q^{\star{\rm ext}}_{\mathsf i},
\qquad
[Q^{\star{\rm ext}}_{\mathsf r}]=-[x^{\mathsf r}],
\qquad
(Q_L^{\star{\rm ext}})^{\ddagger_L}
=-(Q_L^{\ddagger_L})^{\star{\rm ext}},
\qquad
\text{all intrinsic Euclidean antifield-source blocks are independent
before the Euclidean cycle}.}
\tag{3D.75a}
$$

$$
\boxed{
\mathfrak L_{\Psi_R,Q^{\star{\rm ext}}}:
\qquad
X^\star_{\rm BV}
=X^{\star{\rm ext}}
-\frac{\vec\delta\Psi_R}{\delta X}
\quad\Longleftrightarrow\quad
\widehat X^\star_{\rm BV}
=\widehat X^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R}{\partial\widehat X}
\quad
\text{for every minimal and non-minimal field }X.}
\tag{3D.76}
$$

Define the gauge-fixed quantum action by exact restriction of the
extended action constructed in (3D.102):

$$
\boxed{
\begin{aligned}
W_{\Psi,R,\nu}
(Q,Q^{\star{\rm ext}};
\overline Q,\overline Q^\star,\Omega,\Omega^\star)
&:=W_{\rm ext,R,\nu}\!\left(
\overline Q,\overline Q^\star,\Omega,\Omega^\star;
Q,Q^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R}{\partial Q}
\right),\\
S_{\Psi,R}\big|_{Q^{\star{\rm ext}}=0,\Omega_R=0}
&:=S_{\rm ext,R}\big|_{\mathfrak L_{\Psi_R,0},\Omega_R=0}
=S_{0,R}+\mathbf s_R\Psi_R.
\end{aligned}}
\tag{3D.77}
$$

The \(W_{\rm ext,R,\nu}\) in (3D.77) is constructed from the
branch-selected \(W_{\rm nm,R,\nu}\) of (3D.71b).  Thus the admitted
BV--NK branch contains \(S_{\rm triv,NK,R,\nu}\) before gauge-fixing,
while \(\mathscr R_{\rm NK}^{\rm BV}=\varnothing\) on every other
branch.

The measure on
\(\mathfrak L_{\Psi_R,Q^{\star{\rm ext}},\nu}\) is not implicit.  If
\(\ell_{\Psi_R,Q^{\star{\rm ext}}}:
x\mapsto(Q(x),Q^\star_{\rm BV}(x))\) is its coefficient
parameterization, define

$$
\boxed{
d\mu_{\Psi,R,\nu}
:=
\boldsymbol\varpi_{\Psi,R,\nu}(x)
\prod_{\epsilon_x=0}^{\prec_\nu}d\widehat x
\prod_{\epsilon_x=1}^{\succ_\nu}d\widehat x,
\qquad
\boldsymbol\varpi_{\Psi,R,\nu}
:=\ell_{\Psi_R,Q^{\star{\rm ext}}}^{\,*}
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\,1/2}.}
\tag{3D.78}
$$

$$
\epsilon(\boldsymbol\varpi_{\Psi,R,\nu})=0,
\qquad
\operatorname{gh}(\boldsymbol\varpi_{\Psi,R,\nu})=0,
\qquad
[\boldsymbol\varpi_{\Psi,R,\nu}]=0.
\tag{3D.78a}
$$

The extended density in (3D.78) is the non-minimal/background density
constructed in (3D.71c) and (3D.102b).  On the admitted BV--NK branch
it already contains \(\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu}\), so
no second NK density is multiplied after restriction.  The equation
declares its BV semidensity restriction; it does not identify that
restriction with a flat field measure.

For a differentiable family \(\Psi_R(t)\), let \(\dot\ell_t\) be the
deformation vector of the transverse Lagrangian slice.  Define its
boundary flux by

$$
\boxed{
\mathfrak C^{\rm gf}_{R,\nu}(t)
:=\mathfrak F_{R,\nu}^{\rm NK}(t)
\int_{\partial\mathfrak L_{\Psi_R(t),0,\nu}^{\perp}}
\iota_{\dot\ell_t}
\left(d\mu_{\Psi_R(t),R,\nu}
e^{\mathscr E_{\Psi_R(t),R,\nu}|_{\widehat\jmath=0}}\right).}
\tag{3D.78b}
$$

At fixed integrated coordinates define

$$
\boxed{
\mathfrak b^{\rm gf}_{R,\nu}(t)
:=\frac d{dt}\log\boldsymbol\varpi_{\Psi_R(t),R,\nu}
+\tau_R\frac d{dt}W_{\Psi_R(t),R,\nu}
-\mathbf1_{R=L}\epsilon\,
\frac d{dt}\mathscr Q_{\Psi_L(t),L,\nu}.}
\tag{3D.78c}
$$

Direct differentiation of the same damped semidensity in every term
gives

$$
\boxed{
\begin{aligned}
\frac d{dt}\mathcal Z_{\Psi_R(t),R,\nu}
[0;Q^{\star{\rm ext}}=0]
={}&\mathfrak F_{R,\nu}^{\rm NK}(t)
\int_{\mathfrak L_{\Psi_R(t),0,\nu}^{\perp}}
 d\mu_{\Psi_R(t),R,\nu}\,
\mathfrak b^{\rm gf}_{R,\nu}(t)
e^{\mathscr E_{\Psi_R(t),R,\nu}|_{\widehat\jmath=0}}\\
&+\frac d{dt}\log\mathfrak F_{R,\nu}^{\rm NK}(t)\,
\mathcal Z_{\Psi_R(t),R,\nu}
+\mathfrak C^{\rm gf}_{R,\nu}(t).
\end{aligned}}
\tag{3D.79}
$$

For the minus graph (3D.76), the first term in (3D.79) equals
\(+\mathfrak F^{\rm NK}\int e^{-\epsilon\mathscr Q}
\Delta_{\rm ext}[\dot\Psi e^{\tau_RW_{\rm ext}}]\) only after the
semidensity deformation identity has been proved.  The right side is
zero only when the extended QME holds, the NK factor is constant, the
cycle flux vanishes, and the damped BV--Stokes integral has zero
boundary.  Every failed term in (3D.79) is retained.

### 3D.8 Background-covariant gauge and finite Berezinians

Use the Step-3C bridge order and split the total gauge bridge by

$$
\boxed{
\mathcal E_{R,\mathrm{tot}}
=
\widetilde{\mathcal B}_{R,\mathrm B}
 e^{\mathcal V_{R,\mathrm q}}
\mathcal B_{R,\mathrm B}.}
\tag{3D.80}
$$

A background transformation is

$$
\boxed{
\begin{aligned}
\mathcal B_{R,\mathrm B}'&=
 k_{R,\mathrm B}\mathcal B_{R,\mathrm B}h_{R,\mathrm B}^{-1},\\
\widetilde{\mathcal B}_{R,\mathrm B}'&=
 \widetilde h_{R,\mathrm B}
 \widetilde{\mathcal B}_{R,\mathrm B}k_{R,\mathrm B}^{-1},\\
e^{\mathcal V_{R,\mathrm q}'}
&=k_{R,\mathrm B}e^{\mathcal V_{R,\mathrm q}}
 k_{R,\mathrm B}^{-1}.
\end{aligned}}
\tag{3D.81}
$$

The matrix factors cancel in order:

$$
\mathcal E_{R,\mathrm{tot}}'
=
\widetilde h_{R,\mathrm B}
\mathcal E_{R,\mathrm{tot}}h_{R,\mathrm B}^{-1}.
\tag{3D.82}
$$

For a quantum transformation leaving the background bridges fixed,
define

$$
\boxed{
\begin{aligned}
\widehat h_R
&:=\mathcal B_{R,\mathrm B}h_R\mathcal B_{R,\mathrm B}^{-1},
&
\widehat{\widetilde h}_R
&:=\widetilde{\mathcal B}_{R,\mathrm B}^{-1}
 \widetilde h_R\widetilde{\mathcal B}_{R,\mathrm B},\\
\widehat{\mathfrak c}_R
&:=\mathcal B_{R,\mathrm B}\mathfrak c_R
 \mathcal B_{R,\mathrm B}^{-1},
&
\widehat{\widetilde{\mathfrak c}}_R
&:=\widetilde{\mathcal B}_{R,\mathrm B}^{-1}
 \widetilde{\mathfrak c}_R\widetilde{\mathcal B}_{R,\mathrm B}.
\end{aligned}}
\tag{3D.83}
$$

The exact quantum BRST rules are

$$
\boxed{
\begin{aligned}
\mathbf s_Re^{\mathcal V_{R,\mathrm q}}
&=i\widehat{\widetilde{\mathfrak c}}_R
 e^{\mathcal V_{R,\mathrm q}}
 -ie^{\mathcal V_{R,\mathrm q}}\widehat{\mathfrak c}_R,\\
\mathbf s_R\mathcal V_{R,\mathrm q}
&=
\frac{\operatorname{ad}_{\mathcal V_{R,\mathrm q}}}
 {1-e^{-\operatorname{ad}_{\mathcal V_{R,\mathrm q}}}}
\left(
 ie^{-\operatorname{ad}_{\mathcal V_{R,\mathrm q}}}
 \widehat{\widetilde{\mathfrak c}}_R
 -i\widehat{\mathfrak c}_R
\right),\\
\mathbf s_R\widehat{\mathfrak c}_R
&=i\widehat{\mathfrak c}_R^2,
&
\mathbf s_R\widehat{\widetilde{\mathfrak c}}_R
&=i\widehat{\widetilde{\mathfrak c}}_R^2,\\
\mathbf s_R^2e^{\mathcal V_{R,\mathrm q}}
&=\mathbf s_R^2\mathcal V_{R,\mathrm q}=0.
\end{aligned}}
\tag{3D.84}
$$

In the vector frame split matter linearly and pull the same split back
to the gauge-chiral frame:

$$
\boxed{
\begin{aligned}
\boldsymbol\Phi_{R,\mathrm{tot}}^{\mathsf V}
&=\boldsymbol\Phi_{R,\mathrm B}^{\mathsf V}+\chi_R,
&
\mathbf s_R\chi_R
&=i\widehat{\mathfrak c}_R
 (\boldsymbol\Phi_{R,\mathrm B}^{\mathsf V}+\chi_R),\\
\widetilde{\boldsymbol\Phi}_{R,\mathrm{tot}}^{\mathsf V}
&=\widetilde{\boldsymbol\Phi}_{R,\mathrm B}^{\mathsf V}
 +\widetilde\chi_R,
&
\mathbf s_R\widetilde\chi_R
&=-i(\widetilde{\boldsymbol\Phi}_{R,\mathrm B}^{\mathsf V}
 +\widetilde\chi_R)\widehat{\widetilde{\mathfrak c}}_R,\\
\Phi_{R,\mathrm{tot}}
&=\mathcal B_{R,\mathrm B}^{-1}
 (\boldsymbol\Phi_{R,\mathrm B}^{\mathsf V}+\chi_R),
&
\widetilde\Phi_{R,\mathrm{tot}}
&=(\widetilde{\boldsymbol\Phi}_{R,\mathrm B}^{\mathsf V}
 +\widetilde\chi_R)\widetilde{\mathcal B}_{R,\mathrm B}^{-1}.
\end{aligned}}
\tag{3D.85}
$$

The background-covariant gauge conditions are

$$
\boxed{
\begin{aligned}
\mathcal F_{R,+}(\mathcal V_{R,\mathrm q})
&:=-\frac14
 (\bar{\boldsymbol\nabla}^{\mathsf V}_{R,\mathrm B})^2
 \mathcal V_{R,\mathrm q},
&
\bar{\boldsymbol\nabla}^{\mathsf V}_{R,\mathrm B\dot a}
 \mathcal F_{R,+}&=0,\\
\mathcal F_{R,-}(\mathcal V_{R,\mathrm q})
&:=-\frac14
 (\boldsymbol\nabla^{\mathsf V}_{R,\mathrm B})^2
 \mathcal V_{R,\mathrm q},
&
\boldsymbol\nabla^{\mathsf V}_{R,\mathrm B a}
 \mathcal F_{R,-}&=0,\\
[\mathcal F_{R,+}]&=[\mathcal F_{R,-}]=1.
\end{aligned}}
\tag{3D.86}
$$

Choose the chiral and antichiral non-minimal doublets

$$
\boxed{
\begin{aligned}
\mathbf s_R\mathfrak c'_{R,+}&=\mathfrak n_{R,+},
&\mathbf s_R\mathfrak n_{R,+}&=0,\\
\mathbf s_R\widetilde{\mathfrak c}'_{R,-}
&=\widetilde{\mathfrak n}_{R,-},
&\mathbf s_R\widetilde{\mathfrak n}_{R,-}&=0,\\
\epsilon(\mathfrak c'_{R,+})
&=\epsilon(\widetilde{\mathfrak c}'_{R,-})=1,
&\operatorname{gh}(\mathfrak c'_{R,+})
&=\operatorname{gh}(\widetilde{\mathfrak c}'_{R,-})=-1,\\
\epsilon(\mathfrak n_{R,+})
&=\epsilon(\widetilde{\mathfrak n}_{R,-})=0,
&\operatorname{gh}(\mathfrak n_{R,+})
&=\operatorname{gh}(\widetilde{\mathfrak n}_{R,-})=0,\\
[\mathfrak c'_{R,+}]&=[\widetilde{\mathfrak c}'_{R,-}]=2,
&[\mathfrak n_{R,+}]&=[\widetilde{\mathfrak n}_{R,-}]=2,\\
\widetilde{\mathfrak c}'_{L,-}
&=-(\mathfrak c'_{L,+})^{\ddagger_L},
&\widetilde{\mathfrak n}_{L,-}
&=(\mathfrak n_{L,+})^{\ddagger_L}.
\end{aligned}}
\tag{3D.87}
$$

Intrinsic Euclidean tilded and untilded non-minimal fields are
independent.  Set

$$
\boxed{
\begin{gathered}
\mathfrak c'_R:=(\mathfrak c'_{R,+},
 \widetilde{\mathfrak c}'_{R,-}),
\qquad
\mathfrak n_R:=(\mathfrak n_{R,+},
 \widetilde{\mathfrak n}_{R,-}),\\
\mathcal F_R:=(\mathcal F_{R,+},\mathcal F_{R,-}),
\qquad
\mathfrak c_R^{\rm pair}:=(\widehat{\mathfrak c}_R,
 \widehat{\widetilde{\mathfrak c}}_R),\\
\langle A,B\rangle_R
:=\int_{R,+}A_{+,A}B_+^A
 +\int_{R,-}A_{-,A}B_-^A.
\end{gathered}}
\tag{3D.88}
$$

Let \(\mathcal Y_R\) be an even, invertible, local,
background-covariant, graded-self-adjoint map from the multiplier
space to the dual gauge-condition space with

$$
\epsilon(\mathcal Y_R)=0,
\qquad
\operatorname{gh}(\mathcal Y_R)=0,
\qquad
[\mathcal Y_R]=-1,
\qquad
\mathcal Y_L^{\ddagger_L}=\mathcal Y_L,
\qquad
\mathcal Y_E\text{ is intrinsic before its cycle}.
\tag{3D.88a}
$$

The gauge fermion is

$$
\boxed{
\Psi_{\mathcal F,\mathcal Y,R}
:=\langle\mathfrak c'_R,\mathcal F_R\rangle_R
 -\frac12\langle\mathfrak c'_R,
 \mathcal Y_R\mathfrak n_R\rangle_R.}
\tag{3D.89}
$$

The odd Leibniz rule gives

$$
\boxed{
\begin{aligned}
\mathbf s_R\Psi_{\mathcal F,\mathcal Y,R}
={}&\langle\mathfrak n_R,\mathcal F_R\rangle_R
 -\langle\mathfrak c'_R,
 \mathcal M_R^{\mathrm{FP}}\mathfrak c_R^{\rm pair}\rangle_R\\
&-\frac12\langle\mathfrak n_R,
 \mathcal Y_R\mathfrak n_R\rangle_R
 +\frac12\langle\mathfrak c'_R,
 (\mathbf s_R\mathcal Y_R)\mathfrak n_R\rangle_R.
\end{aligned}}
\tag{3D.90}
$$

Define the quantum gauge tangent and the even FP operator by

$$
\boxed{
\begin{aligned}
\mathscr R_{R,\mathrm q}(\mathcal V_{R,\mathrm q})
\mathfrak c_R^{\rm pair}
&:=\mathbf s_R\mathcal V_{R,\mathrm q},\\
\mathcal M_R^{\mathrm{FP}}
&:=d\mathcal F_R(\mathcal V_{R,\mathrm q})
 \circ\mathscr R_{R,\mathrm q}(\mathcal V_{R,\mathrm q}),\\
\mathbf s_R\mathcal F_R
&=\mathcal M_R^{\mathrm{FP}}\mathfrak c_R^{\rm pair},\\
\epsilon(\mathcal M_R^{\mathrm{FP}})&=0,
\qquad
\operatorname{gh}(\mathcal M_R^{\mathrm{FP}})=0,
\qquad
[\mathcal M_R^{\mathrm{FP}}]=1.
\end{aligned}}
\tag{3D.91}
$$

For the standard family (3D.89), separate the finite residual
stabilizer exactly:

$$
\boxed{
\begin{gathered}
\mathscr H_{R,\nu}:=\ker\mathcal M_{R,\nu}^{\mathrm{FP}},
\qquad
\mathscr G_{R,\nu}
=\mathscr H_{R,\nu}\oplus\mathscr G_{R,\nu}^{\perp},\\
\mathcal M_{R,\nu}^{\mathrm{FP},\perp}
:=\Pi_{\mathscr F}^{\perp}
 \mathcal M_{R,\nu}^{\mathrm{FP}}
 \Pi_{\mathscr G}^{\perp}:
\mathscr G_{R,\nu}^{\perp}
\overset{\cong}{\longrightarrow}
\mathscr F_{R,\nu}^{\perp}.
\end{gathered}}
\tag{3D.92}
$$

For a general \(\Psi_R\in\mathfrak G_R\), every primed measure below
excludes \(\mathscr H_{\Psi,R,\nu}\); the symbol
\(\mathscr H_{R,\nu}\) in (3D.92) is only its standard-family
specialization.
The residual orbit is not integrated.  It may be reinstated with
normalized Haar volume one only when
\(\mathscr H_{\Psi,R,\nu}\) is purely even and compact.  An odd or
noncompact residual direction requires a further local slice before
any generating functional is defined; no zero or divergent ``volume''
is divided out.

$$
\boxed{
\begin{aligned}
\mathfrak L_{\Psi,R,\nu}^{\perp}
&:=\mathfrak L_{\Psi,R,\nu}
\cap\{\text{the declared local slice transverse to }
\mathscr H_{\Psi,R,\nu}\},\\
\Psi_R=\Psi_{\mathcal F,\mathcal Y,R}
&\Longrightarrow
\mathscr H_{\Psi,R,\nu}=\mathscr H_{R,\nu}.
\end{aligned}}
\tag{3D.92a}
$$

If \(\mathbf s_R\mathcal Y_R=0\), completing the multiplier square
without reversing the pairing gives

$$
\boxed{
\begin{aligned}
&\langle\mathfrak n_R,\mathcal F_R\rangle_R
 -\frac12\langle\mathfrak n_R,
 \mathcal Y_R\mathfrak n_R\rangle_R\\
&=\frac12\langle\mathcal Y_R^{-1}\mathcal F_R,
 \mathcal F_R\rangle_R
 -\frac12\langle
 \mathfrak n_R-\mathcal Y_R^{-1}\mathcal F_R,
 \mathcal Y_R(
 \mathfrak n_R-\mathcal Y_R^{-1}\mathcal F_R)
 \rangle_R.
\end{aligned}}
\tag{3D.93}
$$

Let \(\mathfrak C_{\mathfrak n,R,\nu}(0)\) be a convergent oriented
multiplier cycle and require the translated cycle

$$
\mathfrak C_{\mathfrak n,R,\nu}(\mathcal F)
=\mathcal Y_R^{-1}\mathcal F_R
 +\mathfrak C_{\mathfrak n,R,\nu}(0)
\tag{3D.93a}
$$

to cross no singularity.  Ordered coefficient integration then gives

$$
\boxed{
\frac{
\int_{\mathfrak C_{\mathfrak n}(\mathcal F)}D'\mathfrak n\,
 e^{\tau_R[
 \langle\mathfrak n,\mathcal F\rangle_R
 -\frac12\langle\mathfrak n,\mathcal Y_R\mathfrak n\rangle_R]}
}{
\int_{\mathfrak C_{\mathfrak n}(0)}D'\mathfrak n\,
 e^{-\frac{\tau_R}{2}
 \langle\mathfrak n,\mathcal Y_R\mathfrak n\rangle_R}
}
=e^{\frac{\tau_R}{2}
 \langle\mathcal Y_R^{-1}\mathcal F_R,
 \mathcal F_R\rangle_R}.}
\tag{3D.93b}
$$

For \(R=E\), the bosonic multiplier cycle is the imaginary
steepest-descent cycle when \(\mathcal Y_E\) is positive on the
corresponding real form.  For \(R=L\), it is a Fresnel cycle with the
same \(i\epsilon\) orientation used in numerator and denominator.

Define the typed dimension-one reference FP map

$$
\boxed{
\mathcal M_{0,R,\nu}^{\perp}
:=\mu\mathcal I_{R,\nu}^{\perp},
\qquad
\mathcal I_{R,\nu}^{\perp}:
\mathscr G_{R,\nu}^{\perp}
\overset{\cong}{\longrightarrow}
\mathscr F_{R,\nu}^{\perp}.}
\tag{3D.93d}
$$

The parity-reversed ghost superfields contain commuting coefficient
blocks; \(\Pi\mathscr V\) denotes the parity reversal of a graded
space \(\mathscr V\).  Write the residual-free coefficient coordinates
of \(\mathfrak c'_R\) and \(\mathfrak c_R^{\rm pair}\) as
\(\mathfrak c_{R,\nu}^{\prime\perp}\) and
\(\mathfrak c_{{\rm FP},R,\nu}^{\perp}\), respectively.  Choose the
Lorentzian and Euclidean operator/cycle homotopies independently:

$$
\boxed{
\begin{gathered}
\mathfrak c_{R,\nu}^{\prime\perp}
\in\Pi(\mathscr F_{R,\nu}^{\perp})^\vee,
\qquad
\mathfrak c_{{\rm FP},R,\nu}^{\perp}
\in\Pi\mathscr G_{R,\nu}^{\perp},\\
D'_{{\rm FP},R,\nu}
:=\prod_{\substack{z\in
\Pi(\mathscr F_{R,\nu}^{\perp})^\vee
\oplus\Pi\mathscr G_{R,\nu}^{\perp}\\ \epsilon_z=0}}^{\prec_\nu}dz
\prod_{\substack{z\in
\Pi(\mathscr F_{R,\nu}^{\perp})^\vee
\oplus\Pi\mathscr G_{R,\nu}^{\perp}\\ \epsilon_z=1}}^{\succ_\nu}dz,\\
\mathcal M_{R,\nu}(0)=\mathcal M_{0,R,\nu}^{\perp},
\qquad
\mathcal M_{R,\nu}(1)
=\mathcal M_{R,\nu}^{\mathrm{FP},\perp},
\qquad
\operatorname{Ber}_{\mathscr G_{R,\nu}^{\perp}}
\left[(\mathcal M_{0,R,\nu}^{\perp})^{-1}
\mathcal M_{R,\nu}(t)\right]\ne0,\\
\mathfrak C^{\perp}_{\rm gh,E,\nu}(t)
\subset\Pi\mathscr G_{E,\nu}^{\perp}
\oplus\Pi(\mathscr F_{E,\nu}^{\perp})^\vee,\\
\operatorname{Re}\left[
-\tau_E\langle\mathfrak c_{E,\nu}^{\prime\perp},
\mathcal M_{E,\nu}(t)\mathfrak c_{{\rm FP},E,\nu}^{\perp}\rangle_E
\right]<0
\quad\text{on every commuting end},\\
\mathfrak C^{\perp}_{\rm gh,L,\nu}(t)
\subset\Pi\mathscr G_{L,\nu}^{\perp}
\oplus\Pi(\mathscr F_{L,\nu}^{\perp})^\vee,\\
\left.\mathscr Q_{\Psi,L,\nu}\right|_{\rm gh}>0,\qquad
\operatorname{Re}\left[
-\tau_L\langle\mathfrak c_{L,\nu}^{\prime\perp},
\mathcal M_{L,\nu}(t)\mathfrak c_{{\rm FP},L,\nu}^{\perp}\rangle_L
-\epsilon\left.\mathscr Q_{\Psi,L,\nu}\right|_{\rm gh}\right]<0
\quad\text{on every commuting end},\qquad \epsilon>0.
\end{gathered}}
\tag{3D.93c}
$$

Here the displayed restriction is the common Lorentzian convergence
quadratic form on the commuting ghost coefficients.  The Lorentzian
cycle is compatible with (3D.49) and
(3D.87) and carries its own Fresnel orientation; the Euclidean cycle
is chosen from its intrinsic independent variables.  Neither cycle
is defined as the Wick image of the other.  The first product in
\(D'_{{\rm FP},R,\nu}\) contains every even coefficient in
\(\prec_\nu\) order and the second every odd coefficient in
\(\succ_\nu\) order; every \(\mathscr H_{R,\nu}\) slot is absent.

No \(t\)-path may cross a zero, singularity, or nonzero boundary
term.  Numerator and reference denominator in (3D.94) use the
endpoint cycles of this homotopy; every anticommuting block uses the
order (3D.19).

The finite FP factor is

$$
\boxed{
\begin{aligned}
\mathfrak F_{R,\nu}^{\mathrm{FP}}
&:=\frac{
 \int D'_{{\rm FP},R,\nu}\,
 e^{-\tau_R\langle\mathfrak c_{R,\nu}^{\prime\perp},
 \mathcal M_{R,\nu}^{\mathrm{FP},\perp}
 \mathfrak c_{{\rm FP},R,\nu}^{\perp}\rangle_R}
 }{
 \int D'_{{\rm FP},R,\nu}\,
 e^{-\tau_R\langle\mathfrak c_{R,\nu}^{\prime\perp},
 \mathcal M_{0,R,\nu}^{\perp}
 \mathfrak c_{{\rm FP},R,\nu}^{\perp}\rangle_R}
 }\\
&=\operatorname{Ber}_{\Pi\mathscr G_{R,\nu}^{\perp}}
 \!\left(
 (\mathcal M_{0,R,\nu}^{\perp})^{-1}
 \mathcal M_{R,\nu}^{\mathrm{FP},\perp}
 \right)^{-1}\\
&=\operatorname{Ber}_{\mathscr G_{R,\nu}^{\perp}}
 \!\left(
 (\mathcal M_{0,R,\nu}^{\perp})^{-1}
 \mathcal M_{R,\nu}^{\mathrm{FP},\perp}
 \right).
\end{aligned}}
\tag{3D.94}
$$

The equality in (3D.94) is the result of the ordered finite
coefficient Gaussian; it is not an unregulated determinant identity.

Choose separately
\(\mathcal I_{\mathfrak n\to\mathscr F^\vee,R,\nu}\) between the
multiplier and dual gauge-condition spaces, set
\(\mathcal Y_{0,R,\nu}:=\mu^{-1}
\mathcal I_{\mathfrak n\to\mathscr F^\vee,R,\nu}\), and define
independently

$$
\boxed{
\begin{aligned}
\mathcal N_{R,\nu}[\mathcal Y]
&:=\int_{\mathfrak C_{f,R,\nu}[\mathcal Y]}D'f\,
 e^{\frac{\tau_R}{2}
 \langle f,\mathcal Y^{-1}f\rangle_R},\\
\mathfrak F_{R,\nu}^{\mathrm{av}}[\mathcal Y_R]
&:=\frac{\mathcal N_{R,\nu}[\mathcal Y_{0,R,\nu}]}
 {\mathcal N_{R,\nu}[\mathcal Y_R]},\\
\left.\mathscr Q_{\Psi,L,\nu}\right|_{f}
&>0,\\
\operatorname{Re}\left[
\frac{\tau_L}{2}\langle f,\mathcal Y_L^{-1}f\rangle_L
-\epsilon\left.\mathscr Q_{\Psi,L,\nu}\right|_{f}\right]
&<0\quad\text{on every commuting end},\qquad \epsilon>0.
\end{aligned}}
\tag{3D.95}
$$

The two gauge-average cycles are independent.  The commuting part of
\(\mathfrak C_{f,E,\nu}\) obeys
\(\operatorname{Re}\langle f,\mathcal Y_E^{-1}f\rangle_E>0\).
The Lorentzian cycle is instead chosen directly from the Lorentzian
real form of the gauge-condition pair and the Fresnel condition in
(3D.95).

The equality of these independently constructed cycles under Wick
transport is tested only in (3D.118b).

A separated Nielsen--Kallosh factor exists only on the branch

$$
\boxed{
\begin{aligned}
\Psi_R\ne\Psi_{\mathcal F,\mathcal Y,R}
&\Longrightarrow
\mathscr R_{\rm NK}^{\rm BV}=\varnothing,
\quad \mathfrak F_{R,\nu}^{\rm NK}=1,\\
\Psi_R=\Psi_{\mathcal F,\mathcal Y,R},\quad
\mathbf s_R\mathcal Y_R=0
&\Longrightarrow\text{use the factorization (3D.93)--(3D.96)},\\
\Psi_R=\Psi_{\mathcal F,\mathcal Y,R},\quad
\mathbf s_R\mathcal Y_R\ne0
&\Longrightarrow
\mathscr R_{\rm NK}^{\rm BV}=\varnothing,
\quad \mathfrak F_{R,\nu}^{\rm NK}=1,
\quad\text{retain the complete coupled }
(\mathfrak c'_R,\mathfrak c_R^{\rm pair},\mathfrak n_R)
\text{ integral from (3D.90)}.
\end{aligned}}
\tag{3D.95b}
$$

On the standard factorized line of (3D.95b), a Nielsen--Kallosh
representation is defined only after its required factor is fixed.
The multiplier measure contributes

$$
\boxed{
\begin{aligned}
\mathcal I^{\mathfrak n}_{R,\nu}[\mathcal Y]
&:=\int_{\mathfrak C_{\mathfrak n,R,\nu}(0;\mathcal Y)}
D'\mathfrak n\,
e^{-\frac{\tau_R}{2}
\langle\mathfrak n,\mathcal Y\mathfrak n\rangle_R},\\
\mathfrak F^{\rm nm}_{R,\nu}[\mathcal Y_R]
&:=\frac{\mathcal I^{\mathfrak n}_{R,\nu}[\mathcal Y_R]}
{\mathcal I^{\mathfrak n}_{R,\nu}[\mathcal Y_{0,R,\nu}]},\\
\mathfrak F^{\rm NK,req}_{R,\nu}
&:=\frac{\mathfrak F^{\rm av}_{R,\nu}[\mathcal Y_R]}
{\mathfrak F^{\rm nm}_{R,\nu}[\mathcal Y_R]}.
\end{aligned}}
\tag{3D.95a}
$$

Thus the multiplier Gaussian times the required NK factor equals the
declared gauge-average normalization exactly.  Let
\(\Xi_{R,\nu}^{\mathrm{NK}}\) be any finite
collection of superfields expanded by (3D.15a), with a declared action,
orientation, Lorentzian reality, and Euclidean cycle.  Define

$$
\boxed{
\begin{aligned}
\mathfrak F_{R,\nu}^{\mathrm{NK,aux}}
&:=\frac{
 \int_{\mathfrak C_{\Xi,R,\nu}[\mathcal Y_R]}
 D'\Xi\,e^{\tau_RS_{\mathrm{NK},R,\nu}[\Xi;\mathcal Y_R]}
 }{
 \int_{\mathfrak C_{\Xi,R,\nu}[\mathcal Y_{0,R,\nu}]}
 D'\Xi\,e^{\tau_RS_{\mathrm{NK},R,\nu}
 [\Xi;\mathcal Y_{0,R,\nu}]}
 },\\
\mathfrak F_{R,\nu}^{\mathrm{NK,aux}}
&=\mathfrak F_{R,\nu}^{\mathrm{NK,req}}.
\end{aligned}}
\tag{3D.96}
$$

The last line is the admission condition for an auxiliary-field
realization, not a universal Gaussian claim.  Without such a
realization the external measure-only branch selects
\(\mathscr R_{\rm NK}^{\rm BV}=\varnothing\) and
\(\mathfrak F_{R,\nu}^{\rm NK}
=\mathfrak F_{R,\nu}^{\rm NK,req}\); this factor is excluded from the
BV observable algebra.  If \(\Xi^{\mathrm{NK}}\) is included among BV
fields, every coordinate belongs to one of the typed contractible
multiplets indexed by \(\mathscr R_{\rm NK}^{\rm BV}\), with its
antifield included, and the BV--NK row of (3D.96b) is selected.

An external measure-only factor is admissible only when

$$
\boxed{
\frac{\vec\partial\mathcal Y_R}
{\partial x_{R,\nu}^{\mathsf r}}=0,
\qquad
\frac{\vec\partial\mathfrak F_{R,\nu}^{\rm NK,req}}
{\partial x_{R,\nu}^{\mathsf r}}=0.}
\tag{3D.96a}
$$

If (3D.96a) fails, place
\(\mathfrak F_{R,\nu}^{\rm NK,req}(x,\overline Q)\) inside the integral,
replace
\(\boldsymbol\varpi_{\Psi,R,\nu}\) everywhere by
\(\boldsymbol\varpi_{\Psi,R,\nu}
\mathfrak F_{R,\nu}^{\rm NK,req}\), select
\(\mathscr R_{\rm NK}^{\rm BV}=\varnothing\), and set
\(\mathfrak F_{R,\nu}^{\rm NK}=1\).
The complete branch selection and the BV--NK admission conditions are

$$
\boxed{
\begin{gathered}
\begin{array}{c|c|c}
\text{selected branch}&\mathscr R_{\rm NK}^{\rm BV}
&\mathfrak F_{R,\nu}^{\rm NK}\\ \hline
\Psi_R\ne\Psi_{\mathcal F,\mathcal Y,R}
\text{ or }(\Psi_R=\Psi_{\mathcal F,\mathcal Y,R},
\mathbf s_R\mathcal Y_R\ne0)
&\varnothing&1\\
\text{external measure-only}&\varnothing
&\mathfrak F_{R,\nu}^{\rm NK,req}\\
\text{density-absorbed after failure of (3D.96a)}&\varnothing&1\\
\text{admitted BV--NK}&\ne\varnothing&1
\end{array}\\[2mm]
\text{on the BV--NK row:}\qquad
\mathfrak F_{R,\nu}^{\rm NK,aux}
=\mathfrak F_{R,\nu}^{\rm NK,req},\\
\begin{aligned}
\vartheta_{R,\nu}^{\rm NK}[\mathcal Y]:
\mathfrak C_{\Xi,R,\nu}[\mathcal Y]
&\overset{\text{even graded superdiffeomorphism}}{\longrightarrow}
\mathfrak L_{\Psi,{\rm NK},R,\nu}^{\perp}[\mathcal Y]
=\{(\mathfrak u_\ell,\mathfrak v_\ell)_{
\ell\in\mathscr R_{\rm NK}^{\rm BV}}\}_{\Psi,\perp},\\
\operatorname{Ber}D\vartheta_{R,\nu}^{\rm NK}&\ne0,
\qquad
\vartheta_{R,\nu}^{\rm NK}
\text{ preserves parity, ghost number, dimension, superspace domain,
Lorentz reality or Euclidean cycle, and orientation},\\
S_{\rm triv,NK,R,\nu}\big|_{\mathfrak L_{\Psi,{\rm NK}}}
\circ\vartheta_{R,\nu}^{\rm NK}[\mathcal Y]
&=S_{\rm NK,R,\nu}[\Xi;\mathcal Y],\\
\mathcal I_{{\rm NK},0,R,\nu}
&:=\int_{\mathfrak C_{\Xi,R,\nu}[\mathcal Y_{0,R,\nu}]}
D'\Xi\,
e^{\tau_RS_{\rm NK,R,\nu}[\Xi;\mathcal Y_{0,R,\nu}]}
\ne0,\\
d\mu_{\Psi,{\rm NK},R,\nu}^{\rm BV}[\mathcal Y]
&:=\frac{(\vartheta_{R,\nu}^{\rm NK}[\mathcal Y])_*(D'\Xi)}
{\mathcal I_{{\rm NK},0,R,\nu}},\\
D_{\prec_\nu,\succ_\nu}^{\rm NK}
&:=\prod_{\substack{z\in\{\mathfrak u_\ell,\mathfrak v_\ell\}\\
\epsilon_z=0}}^{\prec_\nu}d\widehat z
\prod_{\substack{z\in\{\mathfrak u_\ell,\mathfrak v_\ell\}\\
\epsilon_z=1}}^{\succ_\nu}d\widehat z,\\
\ell_{\Psi,{\rm NK}}^*
\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu}^{1/2}
D_{\prec_\nu,\succ_\nu}^{\rm NK}
&=d\mu_{\Psi,{\rm NK},R,\nu}^{\rm BV}[\mathcal Y],\\
\int_{\mathfrak L_{\Psi,{\rm NK},R,\nu}^{\perp}[\mathcal Y_R]}
d\mu_{\Psi,{\rm NK},R,\nu}^{\rm BV}[\mathcal Y_R]\,
e^{\tau_RS_{\rm triv,NK,R,\nu}|_{\mathfrak L_{\Psi,{\rm NK}}}}
&=\frac{
\displaystyle\int_{\mathfrak C_{\Xi,R,\nu}[\mathcal Y_R]}
D'\Xi\,e^{\tau_RS_{\rm NK,R,\nu}[\Xi;\mathcal Y_R]}}
{\displaystyle\int_{\mathfrak C_{\Xi,R,\nu}[\mathcal Y_{0,R,\nu}]}
D'\Xi\,e^{\tau_RS_{\rm NK,R,\nu}[\Xi;\mathcal Y_{0,R,\nu}]}}
=\mathfrak F_{R,\nu}^{\rm NK,req},
\end{aligned}\\
S_{\rm NK,\Psi,R,\nu}
=S_{\rm triv,NK,R,\nu}\big|_{
X^\star=X^{\star{\rm ext}}-\vec\delta\Psi_R/\delta X},\\
W_{\rm nm,R,\nu}
=W_{\min,R,\nu}+S_{\rm triv,base,R,\nu}
+S_{\rm triv,NK,R,\nu},\\
\widehat{\boldsymbol\varpi}_{\rm nm,R,\nu}
=\widehat{\boldsymbol\varpi}_{R,\nu}
\widehat{\boldsymbol\varpi}_{\rm triv,base,R,\nu}
\widehat{\boldsymbol\varpi}_{\rm NK,R,\nu},
\qquad
\Delta_{\rm ext,R,\nu}^{2}=0,\\
\mathfrak O_{R,\nu}^{\rm BV,ext}[W_{\rm ext}]
:=\frac12(W_{\rm ext,R,\nu},W_{\rm ext,R,\nu})_{\rm ext,R,\nu}
-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}W_{\rm ext,R,\nu}=0.
\end{gathered}}
\tag{3D.96b}
$$

On the BV--NK row, the \(W_{\rm ext}\) constructed in (3D.102) uses
the displayed \(W_{\rm nm}\), and its density uses the displayed
\(\widehat{\boldsymbol\varpi}_{\rm nm}\).  Consequently (3D.77),
(3D.78), and (3D.125) contain the NK multiplets in their action,
gauge-fixing graph, density, and integration coordinates while the
external factor is exactly one.  The bijection, numerator and
reference-denominator equality, master restriction, density
nilpotency, and QME equality in (3D.96b) must all hold before this row
is admitted.

### 3D.9 Extended background BV sector

For every homogeneous BV field coordinate choose a local split chart

$$
\boxed{
Q_{R,\mathrm{tot}}^{\mathsf i}
=\Sigma_R^{\mathsf i}(\overline Q_R,\zeta_R),
\qquad
\mathbb J_R^{\mathsf i}{}_{\mathfrak a}
:=\Sigma_R^{\mathsf i}
 \frac{\overleftarrow\partial}{\partial\zeta_R^{\mathfrak a}},
\qquad
\operatorname{Ber}\mathbb J_R\ne0.}
\tag{3D.97}
$$

Let \(\beta:\mathsf i\mapsto\underline\imath(\mathsf i)\) and
\(\chi:\mathsf i\mapsto\mathfrak a(\mathsf i)\) be the displayed
blockwise bijections from total-field slots to background and quantum
slots.  They preserve parity, ghost number, dimension, superspace
domain, and representation.  The background partners and split
differential obey

$$
\boxed{
\begin{gathered}
\epsilon_{\overline Q^{\beta(\mathsf i)}}
=\epsilon_{\zeta^{\chi(\mathsf i)}}
=\epsilon_{Q^{\mathsf i}},
\qquad
\operatorname{gh}(\overline Q^{\beta(\mathsf i)})
=\operatorname{gh}(\zeta^{\chi(\mathsf i)})
=\operatorname{gh}(Q^{\mathsf i}),\\
[\overline Q^{\beta(\mathsf i)}]
=[\zeta^{\chi(\mathsf i)}]=[Q^{\mathsf i}],\\
\epsilon_{\Omega^{\underline\imath}}
=\epsilon_{\overline Q^{\underline\imath}}+1,
\qquad
\operatorname{gh}(\Omega^{\underline\imath})
=\operatorname{gh}(\overline Q^{\underline\imath})+1,
\qquad
[\Omega^{\underline\imath}]
=[\overline Q^{\underline\imath}],\\
\epsilon(\mathbf s_{\mathrm{sp},R})=1,
\qquad
\operatorname{gh}(\mathbf s_{\mathrm{sp},R})=1,
\qquad
[\mathbf s_{\mathrm{sp},R}]=0.
\end{gathered}}
\tag{3D.97a}
$$

For every admissible \(\Psi_R\), choose a source-independent local
tubular Darboux chart around the residual slice.  The actual
integrated coordinates are \(x_{R,\nu}^{\mathsf r}\); the normal
coordinates \(y_{R,\nu}^{\lambda}\) are introduced only to define the
ambient derivatives and are then fixed to zero.

$$
\boxed{
\begin{gathered}
\iota^{\rm int}_{\Psi,R,\nu}:
x^{\mathsf r}\longmapsto
\zeta^{\mathfrak a}
=\kappa_{\Psi,R,\nu}^{\mathfrak a}(x;\overline Q),
\qquad
\frac{\vec\partial\kappa_{\Psi,R,\nu}^{\mathfrak a}}
{\partial\widehat Q^{\star{\rm ext}}}=0,\\
\widehat\zeta^{\mathfrak a}
=\widehat\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
(\widehat x,\widehat y;\overline Q),
\qquad
\widehat\kappa_{\Psi,R,\nu}^{\rm tub}(\widehat x,0;\overline Q)
=\widehat\kappa_{\Psi,R,\nu}(\widehat x;\overline Q),\\
\zeta^{\mathfrak a}
=\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
(x,y;\overline Q),
\qquad
\kappa_{\Psi,R,\nu}^{\rm tub}(x,0;\overline Q)
=\kappa_{\Psi,R,\nu}(x;\overline Q),\\
\mathbb I_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}{}_{\mathsf r}
:=\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
\frac{\overleftarrow\partial}{\partial x^{\mathsf r}},
\qquad
\mathbb I_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathsf r}
:=\left.\mathbb I_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}{}_{\mathsf r}
\right|_{y=0},
\qquad
\widehat{\mathbb I}_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathsf r}
:=
\widehat\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
\frac{\overleftarrow\partial}{\partial\widehat x^{\mathsf r}}
=\mu^{-[\zeta^{\mathfrak a}]+[x^{\mathsf r}]}
\mathbb I_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}{}_{\mathsf r},\\
\widehat{\mathbb N}_{\Psi,R,\nu}^{\mathfrak a}{}_{\lambda}
:=
\widehat\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
\frac{\overleftarrow\partial}{\partial\widehat y^{\lambda}},
\qquad
\begin{pmatrix}\widehat{\mathbb P}\\
\widehat{\mathbb R}\end{pmatrix}_{\!\Psi,R,\nu}
\begin{pmatrix}\widehat{\mathbb I}&
\widehat{\mathbb N}\end{pmatrix}_{\!\Psi,R,\nu}
=\begin{pmatrix}\mathbf1&0\\0&\mathbf1\end{pmatrix},\\
\begin{pmatrix}\widehat{\mathbb I}&
\widehat{\mathbb N}\end{pmatrix}_{\!\Psi,R,\nu}
\begin{pmatrix}\widehat{\mathbb P}\\
\widehat{\mathbb R}\end{pmatrix}_{\!\Psi,R,\nu}
=\mathbf1,
\qquad
\widehat{\mathbb P}^{\mathsf r}{}_{\mathfrak a}
=\mu^{-[x^{\mathsf r}]+[\zeta^{\mathfrak a}]}
\mathbb P^{{\rm tub},\mathsf r}{}_{\mathfrak a},
\qquad
\mathbb P^{\mathsf r}{}_{\mathfrak a}
:=\left.\mathbb P^{{\rm tub},\mathsf r}{}_{\mathfrak a}
\right|_{y=0},\\
\alpha:\lambda\mapsto\mathfrak a(\lambda),
\qquad
\epsilon_{y^\lambda}=\epsilon_{\zeta^{\alpha(\lambda)}},
\qquad
\operatorname{gh}(y^\lambda)
=\operatorname{gh}(\zeta^{\alpha(\lambda)}),
\qquad
[y^\lambda]=[\zeta^{\alpha(\lambda)}],\\
\epsilon_{Q^{\star\bullet}_\lambda}
=\epsilon_{y^\lambda}+1,
\qquad
\operatorname{gh}(Q^{\star\bullet}_\lambda)
=-1-\operatorname{gh}(y^\lambda),
\qquad
[Q^{\star\bullet}_\lambda]=-[y^\lambda],\\
\epsilon_{\overline Q^{\star\bullet,{\rm ad}}_{\underline\imath}}
=\epsilon_{\overline Q^{\underline\imath}}+1,
\qquad
\operatorname{gh}(\overline Q^{\star\bullet,{\rm ad}}_{\underline\imath})
=-1-\operatorname{gh}(\overline Q^{\underline\imath}),
\qquad
[\overline Q^{\star\bullet,{\rm ad}}_{\underline\imath}]
=-[\overline Q^{\underline\imath}],\\
\operatorname{Ber}
\begin{pmatrix}\widehat{\mathbb I}&\widehat{\mathbb N}\end{pmatrix}
\ne0,
\qquad
\widehat{\mathbb I},\widehat{\mathbb N},
\widehat{\mathbb P},\widehat{\mathbb R}
\text{ preserve parity, ghost number, dimension, and superspace block},\\
\pi^{\rm int}_{\Psi,R,\nu}Y^{\mathfrak a}
:=\mathbb P_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak a}
Y^{\mathfrak a},
\qquad
\Pi_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathfrak b}
:=\mathbb I_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathsf r}
\mathbb P_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak b},\\
\widehat Q^{\star\bullet}_{R,\nu,\mathsf r}
:=\widehat Q^{\star\bullet}_{R,\nu,\mathfrak a}
\widehat{\mathbb I}_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathsf r},
\qquad
\widehat Q^{\star\bullet}_{R,\nu,\lambda}
:=\widehat Q^{\star\bullet}_{R,\nu,\mathfrak a}
\widehat{\mathbb N}_{\Psi,R,\nu}^{\mathfrak a}{}_{\lambda},
\quad
\bullet\in\{{\rm BV},{\rm ext}\},\\
\widehat Q^{\star\bullet}_{R,\nu,\mathfrak a}
=\widehat Q^{\star\bullet}_{R,\nu,\mathsf r}
\widehat{\mathbb P}_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak a}
+\widehat Q^{\star\bullet}_{R,\nu,\lambda}
\widehat{\mathbb R}_{\Psi,R,\nu}^{\lambda}{}_{\mathfrak a},
\qquad
\widehat Q^{\star{\rm ext}}_{R,\nu,\lambda}=0,\\
\begin{aligned}
\overline Q_{R,\underline\imath}^{\star\bullet,{\rm ad}}
&:=\overline Q_{R,\underline\imath}^{\star{\rm amb}}
+\widehat Q_{R,\nu,\mathfrak a}^{\star\bullet}
\left(
\widehat\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
\frac{\overleftarrow\partial}
{\partial\overline Q_R^{\underline\imath}}
\right)_{\widehat x,\widehat y},
\qquad
\bullet\in\{{\rm BV},{\rm ext}\},\\
\widehat Q_{\mathfrak a}^{\star\bullet}d\widehat\zeta^{\mathfrak a}
+\overline Q_{\underline\imath}^{\star{\rm amb}}
d\overline Q^{\underline\imath}
&=\widehat Q_{\mathsf r}^{\star\bullet}d\widehat x^{\mathsf r}
+\widehat Q_{\lambda}^{\star\bullet}d\widehat y^\lambda
+\overline Q_{\underline\imath}^{\star\bullet,{\rm ad}}
d\overline Q^{\underline\imath},\\
\Psi_R^{\rm ad}(\widehat x,\widehat y;\overline Q)
&:=\Psi_R\!\left(
\widehat\kappa_{\Psi,R,\nu}^{\rm tub}
(\widehat x,\widehat y;\overline Q);\overline Q\right),\\
\widehat Q_{{\rm BV},\mathsf r}^{\star}
&=\widehat Q_{\mathsf r}^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R^{\rm ad}}{\partial\widehat x^{\mathsf r}},
\qquad
\widehat Q_{{\rm BV},\lambda}^{\star}
=-\frac{\vec\partial\Psi_R^{\rm ad}}{\partial\widehat y^\lambda},\\
\overline Q_{\underline\imath}^{\star{\rm BV},{\rm ad}}
&=\overline Q_{\underline\imath}^{\star{\rm ext},{\rm ad}}
-\frac{\vec\partial\Psi_R}{\partial\widehat\zeta^{\mathfrak a}}
\left(
\widehat\kappa_{\Psi,R,\nu}^{{\rm tub},\mathfrak a}
\frac{\overleftarrow\partial}
{\partial\overline Q_R^{\underline\imath}}
\right)_{\widehat x,\widehat y},\\
(F,G)_{\Psi,R,\nu}^{\rm ad,\bullet}
&:=\sum_{(U,U^{\star\bullet})\in\mathscr D_{\rm ad}^{\bullet}}
\left[
F\frac{\overleftarrow\partial}{\partial U}
\frac{\vec\partial G}{\partial U^{\star\bullet}}
-F\frac{\overleftarrow\partial}{\partial U^{\star\bullet}}
\frac{\vec\partial G}{\partial U}
\right],\\
\mathscr D_{\rm ad}^{\bullet}
&:=\left\{
(\widehat x^{\mathsf r},\widehat Q_{\mathsf r}^{\star\bullet}),
(\widehat y^\lambda,\widehat Q_\lambda^{\star\bullet}),
(\overline Q^{\underline\imath},
\overline Q_{\underline\imath}^{\star\bullet,{\rm ad}}),
(\Omega^{\underline\imath},\Omega_{\underline\imath}^{\star})
\right\},\\
T_{\Psi,R,\nu}^{{\rm tub},\bullet}
&:(\widehat\zeta,\widehat Q^{\star\bullet};
\overline Q,\overline Q^{\star{\rm amb}},\Omega,\Omega^\star)
\longleftrightarrow
(\widehat x,\widehat y,
\widehat Q_{\mathsf r}^{\star\bullet},
\widehat Q_\lambda^{\star\bullet};
\overline Q,\overline Q^{\star\bullet,{\rm ad}},\Omega,\Omega^\star),\\
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\rm ad}
&:=(T_{\Psi,R,\nu}^{{\rm tub},{\rm BV}})_*
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu},
\qquad
\Delta_{\rm ext,R,\nu}
=\Delta[\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\rm ad}]
\quad\text{in the full adapted chart}.
\end{aligned}\\
\widehat Q^{\star{\rm ext}}_{\mathfrak a}
d\widehat\zeta^{\mathfrak a}\big|_{\mathfrak L_\Psi^{\perp}}
=\widehat Q^{\star{\rm ext}}_{\mathsf r}
d\widehat x^{\mathsf r},\\
\mathcal K_{\Psi,R,\nu,\underline\imath}^{{\rm rel},\mathfrak a}
:=\mathcal K_{R,\underline\imath}^{\mathfrak a}
+\left.
\frac{\vec\partial
\kappa_{\Psi,R,\nu}^{\mathfrak a}(x;\overline Q)}
{\partial\overline Q_R^{\underline\imath}}
\right|_{x},\\
\mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r}
:=\mathbb P_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak a}
\mathcal K_{\Psi,R,\nu,\underline\imath}^{{\rm rel},\mathfrak a},\\
\mathfrak N_{\Psi,R,\nu,\underline\imath}^{\mathfrak a}
:=\left(
\delta^{\mathfrak a}{}_{\mathfrak b}
-\Pi_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathfrak b}
\right)
\mathcal K_{\Psi,R,\nu,\underline\imath}^{{\rm rel},\mathfrak b},
\qquad
\Psi_R\in\mathfrak G_R^{\rm sp}
\Longleftrightarrow
\mathfrak N_{\Psi,R,\nu,\underline\imath}^{\mathfrak a}=0.
\end{gathered}}
\tag{3D.97c}
$$

The tubular matrices in (3D.97c) are full
\((\widehat x,\widehat y,\overline Q)\)-dependent matrices.  Every
unmarked occurrence after restriction means their value at
\(\widehat y=0\).  In gauge-fixed expressions
\(\overline Q^\star\) abbreviates
\(\overline Q^{\star{\rm ext},{\rm ad}}\); the symbols
\(\overline Q^{\star{\rm amb}}\) and
\(\overline Q^{\star{\rm BV},{\rm ad}}\) are written explicitly when
used.

All ordered derivatives with respect to
\(\widehat Q^{\star{\rm ext}}_{\mathsf r}\) below hold
\(\widehat Q^{\star{\rm ext}}_\lambda=0\) fixed.  The last equality is
the moving-slice split-tangency condition.  The split Ward
identities below are asserted only on the subfamily
\(\mathfrak G_R^{\rm sp}\subset\mathfrak G_R\) satisfying it; a
nonzero \(\mathfrak N_{\Psi}\) is retained and those identities are
not asserted.

At fixed \(\overline Q_R\), restrict \(\mathbb J_R\) to the physical
slots and denote it by \(\mathbb J_R^{\rm phys}\).  The finite physical
background--quantum change of variables carries (3D.18) to

$$
\boxed{
\begin{aligned}
d\mu_{\zeta,R,\nu}^{\rm phys}
&:=\boldsymbol\varpi_{R,\nu}
 (\Sigma_R^{\rm phys}(\overline Q_R,\zeta_R))
 \operatorname{Ber}\mathbb J_{R,\nu}^{\rm phys}\,
 D_{\prec_\nu}\widehat\zeta_R^{\rm phys},\\
\mathfrak L_{\zeta,R,\nu}^{\rm phys}(\overline Q_R)
&:=(\Sigma_{R,\nu}^{\rm phys}(\overline Q_R,\cdot))^{-1}
 (\mathfrak L_{R,\nu}).
\end{aligned}}
\tag{3D.97b}
$$

Define

$$
\boxed{
\begin{aligned}
B_R^{\mathsf i}{}_{\underline\imath}
&:=\Sigma_R^{\mathsf i}
 \frac{\overleftarrow\partial}
 {\partial\overline Q_R^{\underline\imath}},\\
L_R^{\mathfrak a}{}_{\mathsf i}
&:=(\mathbb J_R^{-1})^{\mathfrak a}{}_{\mathsf i},\\
\mathcal K_{R,\underline\imath}^{\mathfrak a}
&:=L_R^{\mathfrak a}{}_{\mathsf i}
 B_R^{\mathsf i}{}_{\underline\imath},\\
B_R^{\mathsf i}{}_{\underline\imath}
-\mathbb J_R^{\mathsf i}{}_{\mathfrak a}
 \mathcal K_{R,\underline\imath}^{\mathfrak a}&=0.
\end{aligned}}
\tag{3D.98}
$$

The split differential is

$$
\boxed{
\begin{aligned}
\mathbf s_{\mathrm{sp},R}\overline Q_R^{\underline\imath}
&=\Omega_R^{\underline\imath},\\
\mathbf s_{\mathrm{sp},R}\Omega_R^{\underline\imath}&=0,\\
\mathbf s_{\mathrm{sp},R}\zeta_R^{\mathfrak a}
&=-\mathcal K_{R,\underline\imath}^{\mathfrak a}
 \Omega_R^{\underline\imath}.
\end{aligned}}
\tag{3D.99}
$$

Its action on the total field is calculated without omission:

$$
\boxed{
\begin{aligned}
\mathbf s_{\mathrm{sp},R}Q_{R,\mathrm{tot}}^{\mathsf i}
&=B_R^{\mathsf i}{}_{\underline\imath}
 \Omega_R^{\underline\imath}
 -\mathbb J_R^{\mathsf i}{}_{\mathfrak a}
 \mathcal K_{R,\underline\imath}^{\mathfrak a}
 \Omega_R^{\underline\imath}\\
&=0.
\end{aligned}}
\tag{3D.100}
$$

For the standard graded commutator of vertical vector fields,
equality of the mixed derivatives of \(\Sigma_R\) gives

$$
\boxed{
\partial_{\underline\imath}\mathcal K_{\underline\jmath}
-(-1)^{\epsilon_{\underline\imath}
 \epsilon_{\underline\jmath}}
 \partial_{\underline\jmath}\mathcal K_{\underline\imath}
-[\mathcal K_{\underline\imath},
 \mathcal K_{\underline\jmath}]_{\rm gr}=0.}
\tag{3D.101}
$$

Thus \(\mathbf s_{\mathrm{sp},R}^2=0\).
Introduce the canonical pairs

$$
(\overline Q,\overline Q^\star),
\qquad
(\zeta,\zeta^\star),
\qquad
(\Omega,\Omega^\star),
\tag{3D.101a}
$$

with antifield gradings fixed by (3D.3).  At fixed background the
cotangent map and pulled-back master action are

$$
\boxed{
\begin{aligned}
Q^\star_{R,\mathrm{tot},\mathsf i}
&=\zeta^\star_{R,\mathfrak a}
 L_R^{\mathfrak a}{}_{\mathsf i},\\
\widetilde S_{\rm nm,R}
 (\overline Q,\zeta,\zeta^\star)
&:=S_{\rm nm,R}\!\left(
 \Sigma_R(\overline Q,\zeta),
 \zeta^\star L_R(\overline Q,\zeta)
 \right),\\
\widetilde W_{\rm nm,R,\nu}
&:=W_{\rm nm,R,\nu}\!\left(
 \Sigma_R(\overline Q,\zeta),
 \zeta^\star L_R(\overline Q,\zeta)
 \right),\\
H_{\mathrm{sp},R}
&:=\sum_{\underline\imath}
(-1)^{\epsilon_{\overline Q^{\underline\imath}}}
\overline Q^\star_{R,\underline\imath}
 \Omega_R^{\underline\imath}\\
&\quad-
\sum_{\mathfrak a}
(-1)^{\epsilon_{\zeta^{\mathfrak a}}}
\zeta^\star_{R,\mathfrak a}
 \mathcal K_{R,\underline\imath}^{\mathfrak a}
 \Omega_R^{\underline\imath},\\
S_{\rm ext,R}&:=\widetilde S_{\rm nm,R}+H_{\mathrm{sp},R},\\
W_{\rm ext,R,\nu}^{\rm cand}
&:=\widetilde W_{\rm nm,R,\nu}+H_{\mathrm{sp},R},\\
W_{\rm ext,R,\nu}
&:=W_{\rm ext,R,\nu}^{\rm cand}
+\sum_{n=1}^{\infty}\hbar^nC_{n,R,\nu}^{\rm ext}.
\end{aligned}}
\tag{3D.102}
$$

Differentiating \(\mathbb J_RL_R=\mathbf1\) and
\(B_R-\mathbb J_R\mathcal K_R=0\) gives the cotangent cancellations

$$
\boxed{
\mathbf s_{\mathrm{sp},R}
\left(\zeta^\star_{R,\mathfrak a}
L_R^{\mathfrak a}{}_{\mathsf i}\right)=0,
\qquad
\mathbf s_{\mathrm{sp},R}\widetilde S_{\rm nm,R}
=S_{\rm nm,R}\frac{\overleftarrow\delta}
{\delta Q_{\rm tot}^{\mathsf i}}
\mathbf s_{\mathrm{sp},R}Q_{\rm tot}^{\mathsf i}
+S_{\rm nm,R}\frac{\overleftarrow\delta}
{\delta Q^\star_{\rm tot,\mathsf i}}
\mathbf s_{\mathrm{sp},R}Q^\star_{\rm tot,\mathsf i}
=0.}
\tag{3D.102a}
$$

The cotangent split pushes the non-minimal BV density forward and is
completed by a declared density on
\((\overline Q,\overline Q^\star,\Omega,\Omega^\star)\):

$$
\boxed{
\begin{aligned}
T_{\rm split,R,\nu}(\overline Q_R):
(Q_{\rm tot},Q^\star_{\rm tot})
&\longleftrightarrow(\zeta,\zeta^\star)
\quad\text{by (3D.97) and (3D.102)},\\
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}
&:=(T_{\rm split,R,\nu}(\overline Q_R))_*
\widehat{\boldsymbol\varpi}_{\rm nm,R,\nu}\,
\widehat{\boldsymbol\varpi}_{\overline Q,\Omega,R,\nu},
\\
\Delta_{\rm ext,R,\nu}
&:=\Delta[\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}].
\end{aligned}}
\tag{3D.102b}
$$

Every density in (3D.102b) is even, ghost-number zero, and
dimensionless in hatted coordinates.  Nilpotency of
\(\Delta_{\rm ext,R,\nu}\) is checked rather than assumed.

The Lorentzian extended cycle additionally requires

$$
\boxed{
\begin{gathered}
(\mathbf s_{\mathrm{sp},L}X)^{\ddagger_L}
=(-1)^{\epsilon_X}
\mathbf s_{\mathrm{sp},L}(X^{\ddagger_L}),\\
\Sigma_L(\overline Q_L,\zeta_L)^{\ddagger_L}
=\Sigma_L(\overline Q_L^{\ddagger_L},
\zeta_L^{\ddagger_L}),\\
W_{\rm nm,L,\nu}^{\ddagger_L}=W_{\rm nm,L,\nu},
\qquad
H_{\mathrm{sp},L}^{\ddagger_L}=H_{\mathrm{sp},L},
\qquad
W_{\rm ext,L,\nu}^{\ddagger_L}=W_{\rm ext,L,\nu}.
\end{gathered}}
\tag{3D.102c}
$$

Failure of any line in (3D.102c) is retained as a contour-reality
defect.  Intrinsic Euclidean split variables are independent before
their cycle.

Let \((\ ,\ )_{\rm ext,R}\) be the direct sum of the three
antibrackets in (3D.101a), so that
\(\mathbf s_{\mathrm{sp},R}F
=(H_{\mathrm{sp},R},F)_{\rm ext,R}\).
The CME expands into exactly three terms:

$$
\boxed{
\begin{aligned}
\frac12(S_{\rm ext,R},S_{\rm ext,R})_{\rm ext,R}
={}&\frac12(\widetilde S_{\rm nm,R},
 \widetilde S_{\rm nm,R})_{\zeta,R}\\
&+(\widetilde S_{\rm nm,R},H_{\mathrm{sp},R})_{\rm ext,R}
 +\frac12(H_{\mathrm{sp},R},H_{\mathrm{sp},R})_{\rm ext,R}\\
={}&0+\mathbf s_{\mathrm{sp},R}\widetilde S_{\rm nm,R}+0
=0.
\end{aligned}}
\tag{3D.103}
$$

The extended quantum obstruction is therefore defined, not set to
zero:

$$
\boxed{
\begin{aligned}
\mathfrak O_{R,\nu}^{\rm BV,ext}
&:=\frac12(W_{\rm ext,R,\nu},W_{\rm ext,R,\nu})_{\rm ext,R,\nu}
-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}W_{\rm ext,R,\nu},\\
\mathfrak C_{\rm ext,R,\nu}^{(0)}
&:=\frac12(S_{\rm ext,R,\nu},S_{\rm ext,R,\nu})_{\rm ext,R,\nu}.
\end{aligned}}
\tag{3D.103a}
$$

Writing
\(W_{\rm ext,R,\nu}
=\sum_{n\ge0}\hbar^nM^{\rm ext}_{n,R,\nu}\),
\(M^{\rm ext}_{0,R,\nu}:=S_{\rm ext,R,\nu}\), the exact
finite-cutoff expansion and the conditional recursion are

$$
\boxed{
\begin{aligned}
\mathbf s_{\rm ext,R,\nu}F
&:=(S_{\rm ext,R,\nu},F)_{\rm ext,R,\nu},\\
\mathfrak O_{R,\nu}^{\rm BV,ext}
&=\mathfrak C_{\rm ext,R,\nu}^{(0)}
+\sum_{n=1}^{\infty}\hbar^n\left[
\mathbf s_{\rm ext,R,\nu}M^{\rm ext}_{n,R,\nu}
+\frac12\sum_{k=1}^{n-1}
(M^{\rm ext}_{k,R,\nu},
M^{\rm ext}_{n-k,R,\nu})_{\rm ext,R,\nu}
-\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}M^{\rm ext}_{n-1,R,\nu}
\right],\\
\mathfrak C_{\rm ext,R,\nu}^{(0)}=0\quad\Longrightarrow\quad
\mathbf s_{\rm ext,R,\nu}M^{\rm ext}_{n,R,\nu}
&=\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}M^{\rm ext}_{n-1,R,\nu}\\
&\quad-\frac12\sum_{k=1}^{n-1}
(M^{\rm ext}_{k,R,\nu},
M^{\rm ext}_{n-k,R,\nu})_{\rm ext,R,\nu},
\qquad n\ge1.
\end{aligned}}
\tag{3D.103b}
$$

The equality \(\mathfrak C_{\rm ext,R,\nu}^{(0)}=0\) is asserted only
after the finite regulator closure conditions extending (3D.60) have
been proved.  If it is nonzero, it remains as the order-\(\hbar^0\)
term of (3D.103b); no counterterm with \(n\ge1\) can cancel it.  If the
conditional recursion has no local solution at a higher order, that
nonzero obstruction is likewise retained in every Ward identity.

The first zero follows from the cotangent pullback of (3D.57), the
second from (3D.100), and the third from (3D.101).  Consequently
\(\{\mathbf s_R,\mathbf s_{\mathrm{sp},R}\}=0\) on the pulled-back
algebra.

Let \(\mathcal R_{R,\mathrm B,\nu}(\omega)\) be the even finite
coefficient matrix of (3D.81) on every integrated coordinate.  The
collective source and external antifield source transform by

$$
\boxed{
\begin{aligned}
\delta_{\mathrm B}\widehat x^{\mathsf r}
&=(\mathcal R_{R,\mathrm B,\nu})^{\mathsf r}{}_{\mathsf s}
 \widehat x^{\mathsf s},\\
\delta_{\mathrm B}\widehat\jmath_{\mathsf r}
&=-\widehat\jmath_{\mathsf s}
 (\mathcal R_{R,\mathrm B,\nu})^{\mathsf s}{}_{\mathsf r},\\
\delta_{\mathrm B}\widehat Q^{\star{\rm ext}}_{\mathsf r}
&=-\widehat Q^{\star{\rm ext}}_{\mathsf s}
 (\mathcal R_{R,\mathrm B,\nu})^{\mathsf s}{}_{\mathsf r},\\
\delta_{\mathrm B}Y^{\mathsf i}
&=(\mathcal R^{Y}_{R,\mathrm B,\nu})^{\mathsf i}{}_{\mathsf j}
Y^{\mathsf j},
\quad Y\in\{\overline Q,\Omega\},\\
\delta_{\mathrm B}Y^\star_{\mathsf i}
&=-Y^\star_{\mathsf j}
(\mathcal R^{Y}_{R,\mathrm B,\nu})^{\mathsf j}{}_{\mathsf i},\\
\mathcal W_{R,\mathrm B,\nu}^{\rm ext+\jmath}
&:=\sum_{Y\in\{\widehat Q^{\star{\rm ext}},
\overline Q,\overline Q^\star,\Omega,\Omega^\star,
\widehat\jmath\}}
(\delta_{\mathrm B}Y)\frac{\vec\partial}{\partial Y},\\
\mathbb W_{R,\mathrm B,\nu}^{\rm all}
&:=(\delta_{\mathrm B}\widehat x^{\mathsf r})
\frac{\vec\partial}{\partial\widehat x^{\mathsf r}}
+\mathcal W_{R,\mathrm B,\nu}^{\rm ext+\jmath},\\
\delta_{\mathrm B}
 \langle\widehat\jmath,\widehat x\rangle_{\rm ord}
&=0.
\end{aligned}}
\tag{3D.104}
$$

For the unnormalized functional \(\mathcal Z\) and normalized
functional \(Z\) defined in (3D.125), the change of variables gives

$$
\boxed{
\begin{aligned}
\mathcal W_{R,\mathrm B,\nu}^{\rm ext+\jmath}(\omega)
\mathcal Z_{\Psi,R,\nu}
&=\langle\mathfrak B_{R,\mathrm B,\nu}(\omega)
 \rangle_{\widehat\jmath}\,\mathcal Z_{\Psi,R,\nu},\\
\mathcal W_{R,\mathrm B,\nu}^{\rm ext+\jmath}(\omega)
Z_{\Psi,R,\nu}
&=\left[
 \langle\mathfrak B_{R,\mathrm B,\nu}(\omega)\rangle_{\widehat\jmath}
 -\langle\mathfrak B_{R,\mathrm B,\nu}(\omega)\rangle_{0}
 \right]Z_{\Psi,R,\nu}.
\end{aligned}}
\tag{3D.104a}
$$

For \(A=\mathrm B(\omega)\) or
\(A=(\mathrm{sp},\underline\imath)\), define the integrated and
external vector fields by

$$
\boxed{
\begin{aligned}
V_{A,R,\nu}^{\mathfrak a}
&:=\left.(\delta_A\zeta_R^{\mathfrak a})
\right|_{\zeta=\kappa_\Psi}
-\left.\delta_A^{\rm ext}
\kappa_{\Psi,R,\nu}^{\mathfrak a}(x;\overline Q)
\right|_x,\\
X_{A,R,\nu}^{\mathsf r}
&:=\mathbb P_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak a}
V_{A,R,\nu}^{\mathfrak a},
\qquad
\mathfrak N_{A,R,\nu}^{\mathfrak a}
:=(\mathbf1-\Pi_{\Psi,R,\nu})^{\mathfrak a}{}_{\mathfrak b}
V_{A,R,\nu}^{\mathfrak b},\\
X_{R,\mathrm B,\nu}^{\mathsf r}(\omega)
&=(\mathcal R_{R,\mathrm B,\nu}(\omega))^{\mathsf r}{}_{\mathsf s}
x_{R,\nu}^{\mathsf s},
\qquad
\mathfrak N_{\mathrm B,R,\nu}=0,\\
X_{R,\mathrm{sp},\nu,\underline\imath}^{\mathsf r}
&=-\mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r},
\qquad
\mathfrak N_{\mathrm{sp},R,\nu,\underline\imath}
=-\mathfrak N_{\Psi,R,\nu,\underline\imath},\\
\widehat X_{A,R,\nu}^{\mathsf r}
&:=\mu^{-[x^{\mathsf r}]}
X_{A,R,\nu}^{\mathsf r},\\
\delta_A^{\rm tot}
&:=\widehat X_A^{\mathsf r}
\frac{\vec\partial}{\partial\widehat x^{\mathsf r}}
+\delta_A^{\rm ext+\jmath},\\
\delta_{\mathrm B}^{\rm ext+\jmath}
&:=\mathcal W_{R,\mathrm B,\nu}^{\rm ext+\jmath},
\qquad
\delta_{\mathrm{sp},\underline\imath}^{\rm ext+\jmath}
:=\frac{\vec\partial}{\partial\overline Q_R^{\underline\imath}},\\
\mathfrak b_{A,R,\nu}
&:=\operatorname{div}_{\Psi,R,\nu}^{\rm int}\widehat X_A
+\delta_A^{\rm ext+\jmath}\log\boldsymbol\varpi_{\Psi,R,\nu}
+\tau_R\delta_A^{\rm tot}W_{\Psi,R,\nu}\\
&\quad-\mathbf1_{R=L}\epsilon\,
\delta_A^{\rm tot}\mathscr Q_{\Psi,L,\nu}.
\end{aligned}}
\tag{3D.104b}
$$

Equation (3D.97c) makes the split vector a typed tangent vector on the
integrated residual slice.
Define the
cycle flux and the complete expectation-level defect by

$$
\boxed{
\begin{aligned}
\mathfrak C^{\rm cyc}_{A,R,\nu}\mathcal Z_{\Psi,R,\nu}
&:=\mathfrak F_{R,\nu}^{\rm NK}
\int_{\partial\mathfrak L_{\Psi,R,\nu}^{\perp}}
\iota_{\widehat X_A}
\left(d\mu_{\Psi,R,\nu}e^{\mathscr E_{\Psi,R,\nu}}\right),\\
\langle\mathfrak B_{A,R,\nu}\rangle_{\widehat\jmath}
\mathcal Z_{\Psi,R,\nu}
&:=\langle\mathfrak b_{A,R,\nu}\rangle_{\widehat\jmath}
\mathcal Z_{\Psi,R,\nu}
+(\delta_A^{\rm ext+\jmath}\log\mathfrak F_{R,\nu}^{\rm NK})
\mathcal Z_{\Psi,R,\nu}\\
&\quad+\mathfrak C^{\rm cyc}_{A,R,\nu}
\mathcal Z_{\Psi,R,\nu}.
\end{aligned}}
\tag{3D.104c}
$$

Thus density, regulator, action, NK, and cycle defects have distinct
types and are all retained.

The nonlinear split connection remains a composite insertion.  Define
its exact action on the unnormalized functional by

$$
\boxed{
\begin{aligned}
\mathfrak K_{\Psi,R,\nu,\underline\imath}^{{\rm ins,u},\mathsf r}
\mathcal Z_{\Psi,R,\nu}
&:=\mathfrak F_{R,\nu}^{\rm NK}
\int_{\mathfrak L_{\Psi,R,\nu}^{\perp}}d\mu_{\Psi,R,\nu}\,
\mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r}
(\overline Q_R,\zeta_R)
e^{\mathscr E_{\Psi,R,\nu}},\\
\mathfrak K_{\Psi,R,\nu,\underline\imath}^{{\rm ins,n},\mathsf r}
Z_{\Psi,R,\nu}
&:=\frac{
\mathfrak K_{\Psi,R,\nu,\underline\imath}^{{\rm ins,u},\mathsf r}
\mathcal Z_{\Psi,R,\nu}[\widehat\jmath]}
{\mathcal Z_{\Psi,R,\nu}[0]}
=\left\langle
\mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r}
\right\rangle_{\widehat\jmath}Z_{\Psi,R,\nu}.
\end{aligned}}
\tag{3D.105}
$$

No derivative is hidden in either insertion operator in (3D.105).
The source-level split
identity, including the ordered-pairing Koszul sign, is

$$
\boxed{
\left[
\frac{\vec\partial}{\partial\overline Q_R^{\underline\imath}}
+\tau_R\upsilon_R
\sum_{\mathsf r}
(-1)^{\epsilon_{\underline\imath}\epsilon_{\mathsf r}}
\jmath_{R,\nu,\mathsf r}
 \mathfrak K_{\Psi,R,\nu,\underline\imath}^{{\rm ins,u},\mathsf r}
\right]\mathcal Z_{\Psi,R,\nu}
=\langle\mathfrak B_{R,\mathrm{sp},\nu,\underline\imath}
 \rangle_{\widehat\jmath}\mathcal Z_{\Psi,R,\nu}.}
\tag{3D.105a}
$$

For the normalized functional this becomes

$$
\boxed{
\left[
\frac{\vec\partial}{\partial\overline Q_R^{\underline\imath}}
+\tau_R\upsilon_R
\sum_{\mathsf r}
(-1)^{\epsilon_{\underline\imath}\epsilon_{\mathsf r}}
\jmath_{R,\nu,\mathsf r}
\mathfrak K_{\Psi,R,\nu,\underline\imath}^{{\rm ins,n},\mathsf r}
\right]Z_{\Psi,R,\nu}
=\left[
\langle\mathfrak B_{R,\mathrm{sp},\nu,\underline\imath}
\rangle_{\widehat\jmath}
-\langle\mathfrak B_{R,\mathrm{sp},\nu,\underline\imath}
\rangle_0
\right]Z_{\Psi,R,\nu}.}
\tag{3D.105b}
$$

For the external antifield paired with every integrated coordinate,
set

$$
\boxed{
\begin{aligned}
\widehat x&=\widehat x(\widehat\zeta;\overline Q),
&\widehat y&=\widehat y(\widehat\zeta;\overline Q),\\
\mathscr J_{R,\nu}^{\rm src}
&:=\upsilon_R\langle\widehat\jmath_{R,\nu},
\widehat x_{R,\nu}\rangle_{\rm ord}
=\upsilon_R\langle\jmath_{R,\nu},x_{R,\nu}\rangle_{\rm ord},
&\left.
\frac{\vec\partial\mathscr J_{R,\nu}^{\rm src}}
{\partial\widehat y^\lambda}\right|_{\widehat x}
&=0,\qquad \widehat\jmath_\lambda=0,\\
\tau_R&=\frac{\upsilon_R\mathfrak e_R^{\rm QME}}{\hbar},
&\frac1{\tau_R}&=-\hbar\mathfrak e_R^{\rm QME}.
\end{aligned}}
\tag{3D.105c}
$$

Equation (3D.105c) is the declared off-slice extension in the adapted
chart; it is independent of the normal coordinate.  Expressing
\(\Delta_{\rm ext,R,\nu}\) in the adapted Darboux pairs
\((\widehat x,\widehat y;\widehat Q_{\rm BV,\mathsf r}^\star,
\widehat Q_{\rm BV,\lambda}^\star)\), the second-order identity
(3D.62) gives, before integration,

$$
\boxed{
\begin{aligned}
\Delta_{\rm ext,R,\nu}
e^{\tau_R(W_{\rm ext,R,\nu}+\mathscr J_{R,\nu}^{\rm src})}
=\tau_R^2\bigl[&
\mathfrak O_{R,\nu}^{\rm BV,ext}
{}+(W_{\rm ext,R,\nu},\mathscr J_{R,\nu}^{\rm src})
_{\Psi,R,\nu}^{\rm ad,BV}\\
&-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}\mathscr J_{R,\nu}^{\rm src}
\bigr]
e^{\tau_R(W_{\rm ext,R,\nu}+\mathscr J_{R,\nu}^{\rm src})},\\
 (W_{\rm ext,R,\nu},\mathscr J_{R,\nu}^{\rm src})
_{\Psi,R,\nu}^{\rm ad,BV}
&=-\upsilon_R\sum_{\mathsf r}
(-1)^{\epsilon_{\mathsf r}}\widehat\jmath_{R,\nu,\mathsf r}
\left(W_{\rm ext,R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star}_{\rm BV,R,\nu,\mathsf r}}
\right).
\end{aligned}}
\tag{3D.105d}
$$

Since \(\Psi_R\) is independent of
\(\widehat Q^{\star{\rm ext}}\), restriction to (3D.76) gives

$$
\boxed{
\left.
W_{\rm ext,R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star}_{\rm BV,R,\nu,\mathsf r}}
\right|_{\substack{
\mathfrak L_{\Psi_R,Q^{\star{\rm ext}},\nu}^{\perp}\\
\widehat Q^{\star}_{\rm BV,\lambda},
\ \overline Q^{\star{\rm BV},{\rm ad}}\ {\rm fixed}}}
=\left.
W_{\Psi,R,\nu}
\frac{\overleftarrow\partial}
 {\partial\widehat Q^{\star{\rm ext}}_{R,\nu,\mathsf r}}
\right|_{\substack{
\widehat Q^{\star{\rm ext}}_\lambda=0\\
\overline Q^{\star{\rm ext},{\rm ad}}\ {\rm fixed}}}.}
\tag{3D.105d1}
$$

The difference
\(\overline Q^{\star{\rm BV},{\rm ad}}
-\overline Q^{\star{\rm ext},{\rm ad}}\) in (3D.97c) is independent
of \(Q^{\star{\rm ext}}\).  Therefore the two fixed-background-dual
derivatives in (3D.105d1) are identical.

The tangent odd divergence on the gauge-fixed graph is

$$
\boxed{
\Delta_{\Psi,R,\nu}^{\rm tan}F
:=\boldsymbol\varpi_{\Psi,R,\nu}^{-1}
\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\frac{\vec\partial}{\partial\widehat x^{\mathsf r}}
\left[
\boldsymbol\varpi_{\Psi,R,\nu}
\frac{\vec\partial F}
{\partial\widehat Q^{\star{\rm ext}}_{R,\nu,\mathsf r}}
\right].}
\tag{3D.105e}
$$

Define the exact projection/density/damping mismatch and tangent
Stokes flux by

$$
\boxed{
\begin{aligned}
\mathfrak D_{R,\nu}^{\rm BV}
:={}&\tau_R^{-2}e^{-\mathscr E_{\Psi,R,\nu}}
\Delta_{\Psi,R,\nu}^{\rm tan}
e^{\mathscr E_{\Psi,R,\nu}}\\
&-\left.
\left[
\mathfrak O_{R,\nu}^{\rm BV,ext}
+(W_{\rm ext,R,\nu},\mathscr J_{R,\nu}^{\rm src})_{\rm ext,R,\nu}
-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}\mathscr J_{R,\nu}^{\rm src}
\right]\right|_{
\mathfrak L_{\Psi_R,Q^{\star{\rm ext}},\nu}^{\perp}},\\
\mathfrak S_{R,\nu}^{\rm tan}
:={}&\frac{\mathfrak F_{R,\nu}^{\rm NK}}
{\mathcal Z_{\Psi,R,\nu}}
\int_{\mathfrak L_{\Psi,R,\nu}^{\perp}}
d\mu_{\Psi,R,\nu}\,
\Delta_{\Psi,R,\nu}^{\rm tan}
e^{\mathscr E_{\Psi,R,\nu}},\\
\langle\mathfrak B_{R,\nu}^{\rm BV}\rangle_{\widehat\jmath}
:={}&\left\langle
\left.
\left[
\mathfrak O_{R,\nu}^{\rm BV,ext}
-\hbar\mathfrak e_R^{\rm QME}
\Delta_{\rm ext,R,\nu}\mathscr J_{R,\nu}^{\rm src}
\right]\right|_{
\mathfrak L_{\Psi_R,Q^{\star{\rm ext}},\nu}^{\perp}}
+\mathfrak D_{R,\nu}^{\rm BV}
\right\rangle_{\widehat\jmath}
-\tau_R^{-2}\mathfrak S_{R,\nu}^{\rm tan}.
\end{aligned}}
\tag{3D.105f}
$$

Thus no source-Laplacian, projection, density, damping, or cycle term
is silently discarded.  Define

$$
\boxed{
\begin{aligned}
\mathscr W_{R,\nu}^{\rm u}
&:=\frac{\upsilon_R}{\tau_R}
\log\mathcal Z_{\Psi,R,\nu},\\
\mathscr V_{R,\nu}
&:=\frac{\upsilon_R}{\tau_R}
\log\mathcal Z_{\Psi,R,\nu}
[0;Q^{\star{\rm ext}},\overline Q,\overline Q^\star,
\Omega,\Omega^\star],\\
\mathscr W_{c,R,\nu}&=\mathscr W_{R,\nu}^{\rm u}-\mathscr V_{R,\nu}.
\end{aligned}}
\tag{3D.105g}
$$

The external-antifield derivative also acts on the pulled-back
density, damping, measure-only factor, and moving cycle.  Define

$$
\boxed{
\begin{aligned}
\langle\mathfrak C^{\rm ZJ}_{R,\nu,\mathsf r}\rangle
\mathcal Z_{\Psi,R,\nu}
&:=\mathfrak F_{R,\nu}^{\rm NK}
\int_{\partial\mathfrak L_{\Psi,R,\nu}^{\perp}}
\iota_{\partial_{\widehat Q^{\star{\rm ext}}_{\mathsf r}}\ell_\Psi}
\left(d\mu_{\Psi,R,\nu}e^{\mathscr E_{\Psi,R,\nu}}\right),\\
\mathfrak R^{\rm ZJ}_{R,\nu,\mathsf r}
&:=\frac{\upsilon_R}{\tau_R}
\left\langle
\boldsymbol\varpi_{\Psi,R,\nu}^{-1}
\left(\boldsymbol\varpi_{\Psi,R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right)
-\mathbf1_{R=L}\epsilon
\left(\mathscr Q_{\Psi,L,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right)
\right\rangle_{\widehat\jmath}\\
&\quad+\frac{\upsilon_R}{\tau_R}
\left(\log\mathfrak F_{R,\nu}^{\rm NK}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right)
+\frac{\upsilon_R}{\tau_R}
\langle\mathfrak C^{\rm ZJ}_{R,\nu,\mathsf r}\rangle,\\
\mathscr W_{R,\nu}^{\rm u}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}
&=\upsilon_R\left\langle
W_{\Psi,R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}
\right\rangle_{\widehat\jmath}
+\mathfrak R^{\rm ZJ}_{R,\nu,\mathsf r}.
\end{aligned}}
\tag{3D.105k}
$$

Equations (3D.105d)--(3D.105f) give the unnormalized and normalized
connected identities

$$
\boxed{
\begin{aligned}
\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}
\left(\mathscr W_{R,\nu}^{\rm u}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right)
&=\langle\mathfrak B_{R,\nu}^{\rm BV}
\rangle_{\widehat\jmath}
+\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}\mathfrak R^{\rm ZJ}_{R,\nu,\mathsf r},\\
\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}
\left(\mathscr W_{c,R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right)
&=\langle\mathfrak B_{R,\nu}^{\rm BV}
\rangle_{\widehat\jmath}
+\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}\mathfrak R^{\rm ZJ}_{R,\nu,\mathsf r}
-\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}
\left(\mathscr V_{R,\nu}
\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}\right).
\end{aligned}}
\tag{3D.105h}
$$

The antibracket induced by the partial Legendre transform is

$$
\boxed{
\begin{aligned}
(F,G)_{\rm 1PI,int,R,\nu}
:={}&\sum_{\mathsf r}\left[
F\frac{\overleftarrow\partial}
{\partial\widehat{\mathcal Q}_{\mathrm{mean}}^{\mathsf r}}
\frac{\vec\partial G}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}
-F\frac{\overleftarrow\partial}
{\partial\widehat Q^{\star{\rm ext}}_{\mathsf r}}
\frac{\vec\partial G}
{\partial\widehat{\mathcal Q}_{\mathrm{mean}}^{\mathsf r}}
\right].
\end{aligned}}
\tag{3D.105i}
$$

Let \(\mathscr S_{R,\nu}^{\rm 1PI,u}\) be the Legendre transform of
\(\mathscr W_{R,\nu}^{\rm u}\), and define the genuine 1PI breaking
by

$$
\boxed{
\begin{aligned}
\mathscr S_{R,\nu}^{\rm 1PI,u}
&:=\upsilon_R\left(
\mathscr W_{R,\nu}^{\rm u}
-\langle\jmath_{R,\nu},
\mathcal Q_{\mathrm{mean},R,\nu}\rangle_{\rm ord}
\right),\\
\mathfrak O_{R,\nu}^{\rm 1PI,u}
:=\left.
\left[
\langle\mathfrak B_{R,\nu}^{\rm BV}\rangle_{\widehat\jmath}
+\sum_{\mathsf r}(-1)^{\epsilon_{\mathsf r}}
\widehat\jmath_{\mathsf r}\mathfrak R^{\rm ZJ}_{R,\nu,\mathsf r}
\right]
\right|_{\widehat\jmath
=\widehat\jmath(\widehat{\mathcal Q}_{\mathrm{mean}},
\widehat Q^{\star{\rm ext}},
\overline Q,\overline Q^\star,\Omega,\Omega^\star)}.
\end{aligned}}
\tag{3D.105j}
$$

Since
\(\mathscr S_{R,\nu}^{\rm 1PI}
=\mathscr S_{R,\nu}^{\rm 1PI,u}-\upsilon_R\mathscr V_{R,\nu}\),
the normalized integrated Zinn--Justin Slavnov--Taylor identity is

$$
\boxed{
\begin{aligned}
\frac12(\mathscr S_{R,\nu}^{\rm 1PI},
\mathscr S_{R,\nu}^{\rm 1PI})_{\rm 1PI,int,R,\nu}
={}&\mathfrak O_{R,\nu}^{\rm 1PI,u}
-\upsilon_R(\mathscr S_{R,\nu}^{\rm 1PI},
\mathscr V_{R,\nu})_{\rm 1PI,int,R,\nu}\\
&-\frac12(\mathscr V_{R,\nu},\mathscr V_{R,\nu})_{\rm 1PI,int,R,\nu}.
\end{aligned}}
\tag{3D.106}
$$

The right side of (3D.106) is a Legendre-transformed normalized
insertion.  It is never identified with the bare functional
\(\mathfrak O_{R,\nu}^{\rm BV,ext}\).
The background canonical pairs are governed separately by
(3D.104a)--(3D.106b); no un-derived
\((\overline Q,\overline Q^\star)\) or
\((\Omega,\Omega^\star)\) bracket is appended to (3D.106).

The independent split identity is

$$
\boxed{
\frac{\vec\partial\mathscr S_{R,\nu}^{\rm 1PI}}
 {\partial\overline Q_R^{\underline\imath}}
-\sum_{\mathsf r}
(-1)^{\epsilon_{\underline\imath}\epsilon_{\mathsf r}}
 \left(
 \mathscr S_{R,\nu}^{\rm 1PI}
 \frac{\overleftarrow\partial}
 {\partial\mathcal Q_{\mathrm{mean},R,\nu}^{\mathsf r}}
 \right)
 \left\langle
 \mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r}
 \right\rangle_{\widehat\jmath}
=\mathfrak B^{\rm 1PI}_{R,\mathrm{sp},\nu,\underline\imath}.}
\tag{3D.106a}
$$

Its right side is not an undefined local functional.  It is

$$
\boxed{
\mathfrak B^{\rm 1PI}_{R,\mathrm{sp},\nu,\underline\imath}
:=\frac1{\tau_R}
\left.
\left[
\langle\mathfrak B_{R,\mathrm{sp},\nu,\underline\imath}
\rangle_{\widehat\jmath}
-\langle\mathfrak B_{R,\mathrm{sp},\nu,\underline\imath}
\rangle_0
\right]
\right|_{\widehat\jmath
=\widehat\jmath[\widehat{\mathcal Q}_{\mathrm{mean}},
\widehat Q^{\star{\rm ext}},\overline Q,\overline Q^\star,
\Omega,\Omega^\star]} .}
\tag{3D.106b}
$$

The expectation in (3D.106a) is not replaced by a split connection
evaluated on the mean field.  A local
composite Legendre sector is required before such a replacement can
be tested.

### 3D.10 Gauge-chiral and gauge-vector BV frames

In the local symmetric bridge section of (3C.29), define the full
coordinate map by

$$
\boxed{
\mathcal B_R=\widetilde{\mathcal B}_R=e^{\mathcal V_R/2},
\qquad
\mathscr T_R^{\mathsf C\to\mathsf V}:
\begin{cases}
\mathcal V_R^{\mathsf V}=\mathcal V_R^{\mathsf C},
\quad \mathcal E_R=e^{\mathcal V_R},\\
\boldsymbol\Phi_R^{\mathsf V}=\mathcal B_R\Phi_R,\\
\widetilde{\boldsymbol\Phi}_R^{\mathsf V}
=\widetilde\Phi_R\widetilde{\mathcal B}_R,\\
\widehat{\mathfrak c}_R
=\mathcal B_R\mathfrak c_R\mathcal B_R^{-1},\\
\widehat{\widetilde{\mathfrak c}}_R
=\widetilde{\mathcal B}_R^{-1}
 \widetilde{\mathfrak c}_R\widetilde{\mathcal B}_R.
\end{cases}}
\tag{3D.107}
$$

For a non-minimal coordinate transformation
\(\mathfrak u_{\ell}^{\mathsf V}
=F_\ell(Q_{\mathsf C},\mathfrak u_{\ell}^{\mathsf C})\), its partner
is not chosen independently:

$$
\boxed{
\mathfrak v_{\ell}^{\mathsf V}
:=(\mathbb T_{R,\nu*}\mathbf s_R^{\mathsf C})
\mathfrak u_{\ell}^{\mathsf V}.
}
\tag{3D.107a}
$$

Thus \(\mathfrak v_\ell^{\mathsf V}=\mathbf s_R
F_\ell(Q_{\mathsf C},\mathfrak u_\ell^{\mathsf C})\).  In the special
linear form \(F_\ell=\rho_\ell(Q_{\mathsf C})\mathfrak u_\ell^{\mathsf C}\),
this retains \((\mathbf s_R\rho_\ell)\mathfrak u_\ell^{\mathsf C}\).
A nonlinear map neither preserves a linear cutoff nor acts on a
quantum fluctuation independently of its background.  Let
\(\mathbb T_{\rm tot,R,\nu}\) be the coefficient map induced by
(3D.107) on total fields, let \(\mathbb T_{\rm B,R,\nu}\) be the same
frame map on background fields, and use the independently declared
split charts \(\Sigma_{\mathsf C,R}\) and \(\Sigma_{\mathsf V,R}\).
Define the quantum map by the commutative square itself:

$$
\boxed{
\begin{aligned}
\overline Q_{\mathsf V}
&:=\mathbb T_{\rm B,R,\nu}(\overline Q_{\mathsf C}),\\
\zeta_{\mathsf V}
&:=\mathbb T_{\rm q,R,\nu}
(\overline Q_{\mathsf C},\zeta_{\mathsf C})\\
&:=\Sigma_{\mathsf V,R}
(\overline Q_{\mathsf V},\cdot)^{-1}
\mathbb T_{\rm tot,R,\nu}
\Sigma_{\mathsf C,R}
(\overline Q_{\mathsf C},\zeta_{\mathsf C}),\\
\Sigma_{\mathsf V,R}
(\overline Q_{\mathsf V},\zeta_{\mathsf V})
&=\mathbb T_{\rm tot,R,\nu}
\Sigma_{\mathsf C,R}
(\overline Q_{\mathsf C},\zeta_{\mathsf C}),\\
\mathbb J_{\rm B}
&:=\frac{\vec\partial\overline Q_{\mathsf V}}
{\partial\overline Q_{\mathsf C}},
&
\mathbb J_{\rm q}
&:=\frac{\vec\partial\zeta_{\mathsf V}}
{\partial\zeta_{\mathsf C}},
&
\mathbb B_{\rm q}
&:=\frac{\vec\partial\zeta_{\mathsf V}}
{\partial\overline Q_{\mathsf C}},\\
\Omega_{\mathsf V}
&:=\mathbb J_{\rm B}\Omega_{\mathsf C},\\
\mathscr X_{\mathsf C,R,\nu}^{\perp}
&:=\{\widehat x_{R,\nu}^{\mathsf C}
\text{ on the complete field-coordinate slice transverse to }
\mathscr H_{\Psi,\mathsf C,R,\nu}\},\\
\mathscr X_{\mathsf V,R,\nu}^{\perp}
&:=\mathbb T_{\rm q,R,\nu}
(\mathscr X_{\mathsf C,R,\nu}^{\perp}),\\
\mathbb T_{R,\nu}
&:=\mathbb T_{\rm q,R,\nu}
\big|_{\mathscr X_{\mathsf C,R,\nu}^{\perp}}:
\mathscr X_{\mathsf C,R,\nu}^{\perp}
\overset{\cong}{\longrightarrow}
\mathscr X_{\mathsf V,R,\nu}^{\perp},\\
\mathbb T_{R,\nu}^{\rm ext}
&:(\overline Q_{\mathsf C},\Omega_{\mathsf C})
\longmapsto
(\overline Q_{\mathsf V},\mathbb J_{\rm B}\Omega_{\mathsf C}),\\
\mathbf s_{R,\nu}^{\mathsf V}
&:=d\mathbb T_{R,\nu}
 \mathbf s_{R,\nu}^{\mathsf C}
 \mathbb T_{R,\nu}^{-1},\\
d\mathbb T_{\rm tot}\,\mathbb J_{\mathsf C}
&=\mathbb J_{\mathsf V}\mathbb J_{\rm q},\\
d\mathbb T_{\rm tot}\,B_{\mathsf C}
&=B_{\mathsf V}\mathbb J_{\rm B}
 +\mathbb J_{\mathsf V}\mathbb B_{\rm q},\\
\mathcal K_{\mathsf V}\mathbb J_{\rm B}
&=\mathbb J_{\rm q}\mathcal K_{\mathsf C}
-\mathbb B_{\rm q},\\
\mathbf s_{\rm sp,\mathsf V}\overline Q_{\mathsf V}
&=\Omega_{\mathsf V},\qquad
\mathbf s_{\rm sp,\mathsf V}\Omega_{\mathsf V}=0,\qquad
\mathbf s_{\rm sp,\mathsf V}\zeta_{\mathsf V}
=-\mathcal K_{\mathsf V}\Omega_{\mathsf V},\\
\operatorname{Ad}_{\mathcal B}\mathscr H_{\Psi,\mathsf C,R,\nu}^{+}
&=\mathscr H_{\Psi,\mathsf V,R,\nu}^{+},\qquad
\operatorname{Ad}_{\mathcal B}
\mathscr G_{\Psi,\mathsf C,R,\nu}^{+,\perp}
=\mathscr G_{\Psi,\mathsf V,R,\nu}^{+,\perp},\\
\operatorname{Ad}_{\widetilde{\mathcal B}^{-1}}
\mathscr H_{\Psi,\mathsf C,R,\nu}^{-}
&=\mathscr H_{\Psi,\mathsf V,R,\nu}^{-},\qquad
\operatorname{Ad}_{\widetilde{\mathcal B}^{-1}}
\mathscr G_{\Psi,\mathsf C,R,\nu}^{-,\perp}
=\mathscr G_{\Psi,\mathsf V,R,\nu}^{-,\perp},\\
A_{\mathcal B,R,\nu}^{+,\perp}
&:=\operatorname{Ad}_{\mathcal B}
\big|_{\mathscr G_{\Psi,\mathsf C,R,\nu}^{+,\perp}},\qquad
A_{\widetilde{\mathcal B}^{-1},R,\nu}^{-,\perp}
:=\operatorname{Ad}_{\widetilde{\mathcal B}^{-1}}
\big|_{\mathscr G_{\Psi,\mathsf C,R,\nu}^{-,\perp}}.
\end{aligned}}
\tag{3D.108}
$$

Ordered differentiation of the commutative square and the induced
split-connection identity are recorded in (3D.108).  Thus the
standard vector split (3D.80), rather than the generally
false replacement
\(\mathbb T_{\rm q}(\overline Q,\zeta)=\mathscr T(\zeta)\), is the
frame image of the chiral split.

The final four subspace equalities in (3D.108) are imposed separately
on the chiral and antichiral ghost blocks.  Failure of any one is a frame defect;
the residual-free frame equality is then not asserted.

Thus no projection back to an independently chosen vector-frame mode
space occurs.  In the physical block order
\((\mathcal V,\Phi,\widetilde\Phi)\), the coefficient Jacobian is
block triangular:

$$
\boxed{
\begin{aligned}
\mathcal J_{R,\nu}^{\mathsf C\to\mathsf V,\perp}
&:=\frac{\vec\partial q_{R,\nu}^{\mathsf V,\perp}}
 {\partial q_{R,\nu}^{\mathsf C,\perp}}
=\begin{pmatrix}
\mathbf1&0&0\\
\dfrac{\vec\partial(\mathcal B\Phi)}{\partial\mathcal V}
&L_{\mathcal B}^{\perp}&0\\
\dfrac{\vec\partial(\widetilde\Phi\widetilde{\mathcal B})}
 {\partial\mathcal V}
&0&R_{\widetilde{\mathcal B}}^{\perp}
\end{pmatrix},\\
\operatorname{Ber}\mathcal J_{R,\nu}^{\mathsf C\to\mathsf V,\perp}
&=\operatorname{Ber}L_{\mathcal B,R,\nu}^{\perp}\,
 \operatorname{Ber}R_{\widetilde{\mathcal B},R,\nu}^{\perp}.
\end{aligned}}
\tag{3D.109}
$$

The ghost blocks use only the two displayed residual complements.  If
\(J_{\ell,\rm nm}^{\perp}\) is the derivative of the complete doublet
map (3D.107a) restricted to the actual integrated tangent slice, the
full integrated Jacobian is

$$
\boxed{
\begin{aligned}
J_{\mathbb T,R,\nu}^{\perp}
&:=\frac{\vec\partial x_{R,\nu}^{\mathsf V,\perp}}
{\partial x_{R,\nu}^{\mathsf C,\perp}},\\
\operatorname{Ber}J_{\mathbb T,R,\nu}^{\perp}
&=\operatorname{Ber}\mathcal J_{R,\nu}^{\mathsf C\to\mathsf V,\perp}
\operatorname{Ber}_{\Pi\mathscr G_{\Psi,\mathsf C,R,\nu}^{+,\perp}}
(A_{\mathcal B,R,\nu}^{+,\perp})
\operatorname{Ber}_{\Pi\mathscr G_{\Psi,\mathsf C,R,\nu}^{-,\perp}}
(A_{\widetilde{\mathcal B}^{-1},R,\nu}^{-,\perp})
\prod_{\ell\in\mathscr R_{\rm nm}}
\operatorname{Ber}J_{\ell,\rm nm}^{\perp},
\qquad
\operatorname{Ber}_{\Pi\mathscr V}A
=(\operatorname{Ber}_{\mathscr V}A)^{-1}.
\end{aligned}}
\tag{3D.109a}
$$

No ghost or non-minimal factor is omitted.  The full vector-frame BV
density, gauge-fixed measure, and measure-only NK factor are the
pushforwards

$$
\boxed{
\begin{aligned}
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\mathsf V}
&:=(\widehat{\mathbb T}_{\rm all,R,\nu})_*
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\mathsf C},\\
d\mu_{\Psi,R,\nu}^{\mathsf V}
&:=(\mathbb T_{R,\nu})_*d\mu_{\Psi,R,\nu}^{\mathsf C},\\
\boldsymbol\varpi_{\Psi,R,\nu}^{\mathsf V}(x^{\mathsf V})
&=\boldsymbol\varpi_{\Psi,R,\nu}^{\mathsf C}
(\mathbb T_{R,\nu}^{-1}x^{\mathsf V})
 \operatorname{Ber}
 \left(
 \frac{\vec\partial x^{\mathsf C}}
 {\partial x^{\mathsf V}}
 \right),\\
\mathfrak F_{R,\nu}^{\rm NK,\mathsf V}(\overline Q_{\mathsf V})
&:=\mathfrak F_{R,\nu}^{\rm NK,\mathsf C}
(\mathbb T_{\rm B,R,\nu}^{-1}\overline Q_{\mathsf V}).
\end{aligned}}
\tag{3D.110}
$$

For a general source functional define
\(\mathscr J_{\mathsf V}:=
\mathscr J_{\mathsf C}\circ\mathbb T_{R,\nu}^{-1}\).  Finite change
of variables gives

$$
\boxed{
\begin{aligned}
Z_{R,\nu}^{\mathsf V}[\mathscr J_{\mathsf V}]
&=Z_{R,\nu}^{\mathsf C}[\mathscr J_{\mathsf C}],\\
Z_{R,\nu}^{\mathsf V}[\widehat\jmath_{\mathsf V}]
&=Z_{R,\nu}^{\mathsf C}
\left[\langle\widehat\jmath_{\mathsf V},
\widehat{\mathbb T_{R,\nu}(Q_{\mathsf C})}\rangle_{\rm ord}\right],\\
\widehat{\mathcal Q}_{\mathrm{mean},\mathsf V}
&=\left\langle
\widehat{\mathbb T_{R,\nu}(Q_{\mathsf C})}
\right\rangle_{\widehat\jmath_{\mathsf V}}.
\end{aligned}}
\tag{3D.110a}
$$

The last line is not replaced by
\(\mathbb T(\langle Q_{\mathsf C}\rangle)\) without a composite
Legendre sector.

In (3D.111), \(Q=\zeta\) is the ambient split coordinate of (3D.97);
the actual integrated coordinate is \(x\) in (3D.97c).  Collect the
ambient tangent coordinates as
\(\mathbf Y:=(Q,\overline Q,\Omega)\).  The ambient cotangent lift and
its induced residual law are

$$
\boxed{
\begin{aligned}
\mathbf Y_{\mathsf V}
&:=\mathbb T_{\rm all,R,\nu}(\mathbf Y_{\mathsf C})
=\left(
\mathbb T_{\rm q}(\overline Q_{\mathsf C},Q_{\mathsf C}),
\mathbb T_{\rm B}(\overline Q_{\mathsf C}),
\mathbb J_{\rm B}(\overline Q_{\mathsf C})\Omega_{\mathsf C}
\right),\\
\mathbb J_{\rm all}
&:=\frac{\vec\partial\mathbf Y_{\mathsf V}}
{\partial\mathbf Y_{\mathsf C}}
=\begin{pmatrix}
\mathbb J_{\rm q}&\mathbb B_{\rm q}&0\\
0&\mathbb J_{\rm B}&0\\
0&
\dfrac{\vec\partial(\mathbb J_{\rm B}\Omega_{\mathsf C})}
{\partial\overline Q_{\mathsf C}}
&\mathbb J_{\rm B}
\end{pmatrix},\\
\mathbf Y_{\mathsf C}^{\star}
&=\mathbf Y_{\mathsf V}^{\star}\mathbb J_{\rm all},\\
Q_{\mathsf C}^{\star}
&=Q_{\mathsf V}^{\star}\mathbb J_{\rm q},\\
\overline Q_{\mathsf C}^{\star}
&=Q_{\mathsf V}^{\star}\mathbb B_{\rm q}
+\overline Q_{\mathsf V}^{\star}\mathbb J_{\rm B}
+\Omega_{\mathsf V}^{\star}
\frac{\vec\partial(\mathbb J_{\rm B}\Omega_{\mathsf C})}
{\partial\overline Q_{\mathsf C}},\\
\Omega_{\mathsf C}^{\star}
&=\Omega_{\mathsf V}^{\star}\mathbb J_{\rm B},\\
Q_{\mathsf C}^{\star{\rm ext}}
&=Q_{\mathsf V}^{\star{\rm ext}}\mathbb J_{\rm q},\qquad
Q_{\mathsf V}^{\star{\rm ext}}
=Q_{\mathsf C}^{\star{\rm ext}}\mathbb J_{\rm q}^{-1},\\
\widehat x_{\mathsf V}
&=\widehat{\mathbb T}_{R,\nu}^{\perp}(\widehat x_{\mathsf C}),
\qquad
J_{\mathbb T,R,\nu}^{\perp}
=\frac{\vec\partial\widehat x_{\mathsf V}}
{\partial\widehat x_{\mathsf C}},\\
\widehat y_{\mathsf V}
&=\widehat{\mathbb T}_{R,\nu}^{\rm nor}
(\widehat x_{\mathsf C},\widehat y_{\mathsf C};
\overline Q_{\mathsf C}),
\qquad
\widehat{\mathbb T}_{R,\nu}^{\rm nor}
(\widehat x_{\mathsf C},0;\overline Q_{\mathsf C})=0,
\qquad
J_{\mathbb T,R,\nu}^{\rm nor}
:=\left.
\frac{\vec\partial\widehat y_{\mathsf V}}
{\partial\widehat y_{\mathsf C}}\right|_{\widehat y=0},
\qquad
\operatorname{Ber}J_{\mathbb T,R,\nu}^{\rm nor}\ne0,\\
\widehat\kappa_{\Psi,\mathsf V,R,\nu}^{\rm tub}
&\left(
\widehat{\mathbb T}_{R,\nu}^{\perp}(\widehat x_{\mathsf C}),
\widehat{\mathbb T}_{R,\nu}^{\rm nor}
(\widehat x_{\mathsf C},\widehat y_{\mathsf C};
\overline Q_{\mathsf C});
\mathbb T_{\rm B,R,\nu}\overline Q_{\mathsf C}
\right)\\
&=\mathbb T_{\rm q,R,\nu}\left(
\overline Q_{\mathsf C},
\widehat\kappa_{\Psi,\mathsf C,R,\nu}^{\rm tub}
(\widehat x_{\mathsf C},\widehat y_{\mathsf C};
\overline Q_{\mathsf C})\right),\\
\left.
\frac{\vec\partial\widehat x_{\mathsf V}}
{\partial\widehat y_{\mathsf C}}\right|_{\widehat y=0}
&=0,
\qquad
\widehat Q_{\mathsf C,\lambda}^{\star{\rm ext}}
=\widehat Q_{\mathsf V,\rho}^{\star{\rm ext}}
(J_{\mathbb T,R,\nu}^{\rm nor})^\rho{}_\lambda=0,\\
\widehat Q_{\mathsf C,\mathsf r}^{\star{\rm ext}}
&=\widehat Q_{\mathsf V,\mathsf s}^{\star{\rm ext}}
(J_{\mathbb T,R,\nu}^{\perp})^{\mathsf s}{}_{\mathsf r},
\qquad
\widehat Q_{\mathsf V,\mathsf r}^{\star{\rm ext}}
=\widehat Q_{\mathsf C,\mathsf s}^{\star{\rm ext}}
\bigl((J_{\mathbb T,R,\nu}^{\perp})^{-1}\bigr)
^{\mathsf s}{}_{\mathsf r},\\
\mathbf Y_{\mathsf C}^{\star}d\mathbf Y_{\mathsf C}
&=\mathbf Y_{\mathsf V}^{\star}d\mathbf Y_{\mathsf V}.
\end{aligned}}
\tag{3D.111}
$$

All products in (3D.111) have the displayed row/column order.
\(\widehat{\mathbb T}_{\rm all,R,\nu}\) denotes this cotangent lift,
on the ambient BV covectors.  The gauge-fixed source lift is the
affine map \(\widehat{\mathbb T}_{\rm src,\Psi,R,\nu}\) defined in
(3D.111a); it is not obtained by replacing every \(Q^\star\) in the
background cross term by \(Q^{\star{\rm ext}}\).

The gauge fermion is a scalar on the complete tangent space and the
minus graph (3D.76) is carried into itself:

$$
\boxed{
\begin{aligned}
\mathcal E_{\mathsf V}
&:=(Q_{\mathsf V}^{\star{\rm ext}};
\overline Q_{\mathsf V},\overline Q_{\mathsf V}^{\star},
\Omega_{\mathsf V},\Omega_{\mathsf V}^{\star}),\\
(Q_{\mathsf C},\mathcal E_{\mathsf C})
&:=\widehat{\mathbb T}_{\rm src,\Psi,R,\nu}^{-1}
(Q_{\mathsf V},\mathcal E_{\mathsf V}),\\
\Psi_R^{\mathsf V}
&:=\Psi_R^{\mathsf C}\circ\mathbb T_{\rm all,R,\nu}^{-1},\\
\frac{\vec\partial\Psi_R^{\mathsf V}}
{\partial Q_{\mathsf V}}
&=\frac{\vec\partial\Psi_R^{\mathsf C}}
{\partial Q_{\mathsf C}}\mathbb J_{\rm q}^{-1},\\
Q_{\mathsf V}^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R^{\mathsf V}}
{\partial Q_{\mathsf V}}
&=\left(
Q_{\mathsf C}^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R^{\mathsf C}}
{\partial Q_{\mathsf C}}
\right)\mathbb J_{\rm q}^{-1},\\
\overline Q_{\mathsf C}^{\star{\rm amb}}
&=\left(
Q_{\mathsf V}^{\star{\rm ext}}
-\frac{\vec\partial\Psi_R^{\mathsf V}}
{\partial Q_{\mathsf V}}
\right)\mathbb B_{\rm q}
+\overline Q_{\mathsf V}^{\star{\rm amb}}\mathbb J_{\rm B}
+\Omega_{\mathsf V}^{\star}
\frac{\vec\partial(\mathbb J_{\rm B}\Omega_{\mathsf C})}
{\partial\overline Q_{\mathsf C}},\\
\mathfrak L_{\Psi,\mathsf V,R,\nu}^{\perp}
&=\widehat{\mathbb T}_{\rm all,R,\nu}
\mathfrak L_{\Psi,\mathsf C,R,\nu}^{\perp},\\
W_{\Psi,\mathsf V,R,\nu}
(Q_{\mathsf V},Q_{\mathsf V}^{\star{\rm ext}};
\overline Q_{\mathsf V},\overline Q_{\mathsf V}^{\star},
\Omega_{\mathsf V},\Omega_{\mathsf V}^{\star})
&=W_{\Psi,\mathsf C,R,\nu}
(Q_{\mathsf C},Q_{\mathsf C}^{\star{\rm ext}};
\overline Q_{\mathsf C},\overline Q_{\mathsf C}^{\star},
\Omega_{\mathsf C},\Omega_{\mathsf C}^{\star}).
\end{aligned}}
\tag{3D.111a}
$$

It preserves the odd symplectic form and antibracket:

$$
\boxed{
\sum_{Y\in\{Q,\overline Q,\Omega\}}dY_{\mathsf C}^\star
 \wedge dY_{\mathsf C}
=
\sum_{Y\in\{Q,\overline Q,\Omega\}}dY_{\mathsf V}^\star
 \wedge dY_{\mathsf V},
\qquad
(F,G)^{\mathsf C}_{\rm ext,R,\nu}
=(F,G)^{\mathsf V}_{\rm ext,R,\nu}.}
\tag{3D.112}
$$

If \(\mathcal B_R\) and \(\widetilde{\mathcal B}_R\) are integrated
independently, the \(k_R\)-frame redundancy of (3C.7) requires a full
unconstrained ghost \(\mathfrak k_R\):

$$
\boxed{
\begin{gathered}
\Sigma_{\mathcal B_R}=\Sigma_{\widetilde{\mathcal B}_R}
=\Sigma_{R,8},
\qquad
\epsilon_{\mathcal B_R}
=\epsilon_{\widetilde{\mathcal B}_R}=0,
\qquad
\operatorname{gh}(\mathcal B_R)
=\operatorname{gh}(\widetilde{\mathcal B}_R)=0,\\
[\mathcal B_R]=[\widetilde{\mathcal B}_R]=0,
\qquad
[\mathcal B_R^\star]
=[\widetilde{\mathcal B}_R^\star]=2,\\
\Sigma_{\mathfrak k_R}=\Sigma_{R,8},
\qquad
\epsilon_{\mathfrak k_R}=1,
\qquad
\operatorname{gh}(\mathfrak k_R)=1,
\qquad
[\mathfrak k_R]=0,
\qquad
[\mathfrak k_R^\star]=2,\\
\mathbf s_R\mathcal B_R
=i\mathfrak k_R\mathcal B_R-i\mathcal B_R\mathfrak c_R,\\
\mathbf s_R\widetilde{\mathcal B}_R
=i\widetilde{\mathfrak c}_R\widetilde{\mathcal B}_R
-i\widetilde{\mathcal B}_R\mathfrak k_R,
\qquad
\mathbf s_R\mathfrak k_R=i\mathfrak k_R^2,\\
\widetilde{\mathcal B}_L=\mathcal B_L^{\ddagger_L},
\qquad
\mathfrak k_L^{\ddagger_L}=\mathfrak k_L,
\qquad
(\mathcal B_E,\widetilde{\mathcal B}_E,\mathfrak k_E)
\text{ are independent before the Euclidean cycle}.
\end{gathered}}
\tag{3D.113}
$$

Direct use of the odd Leibniz rule gives

$$
\boxed{
\begin{aligned}
\mathbf s_R(\widetilde{\mathcal B}_R\mathcal B_R)
&=i\widetilde{\mathfrak c}_R\mathcal E_R
 -i\mathcal E_R\mathfrak c_R,\\
\mathbf s_R^2\mathcal B_R
&=\mathbf s_R^2\widetilde{\mathcal B}_R
=\mathbf s_R^2\mathfrak k_R=0.
\end{aligned}}
\tag{3D.114}
$$

The enlarged master action contains

$$
\boxed{
\begin{aligned}
\langle\mathcal B_R^\star,Y_R\rangle_{R,8}
&:=\int_{R,8}\operatorname{tr}
(\mathcal B_R^\star Y_R),\\
\langle\widetilde{\mathcal B}_R^\star,
\widetilde Y_R\rangle_{R,8}
&:=\int_{R,8}\operatorname{tr}
(\widetilde{\mathcal B}_R^\star\widetilde Y_R),\\
\langle\mathfrak k_R^\star,Y_{\mathfrak k,R}\rangle_{R,8}
&:=\int_{R,8}\operatorname{tr}
(\mathfrak k_R^\star Y_{\mathfrak k,R}),\\
S_{\rm frame,R}
&:=\langle\mathcal B_R^\star,
\mathbf s_R\mathcal B_R\rangle_{R,8}
+\langle\widetilde{\mathcal B}_R^\star,
\mathbf s_R\widetilde{\mathcal B}_R\rangle_{R,8}
-\langle\mathfrak k_R^\star,
\mathbf s_R\mathfrak k_R\rangle_{R,8}.
\end{aligned}}
\tag{3D.115}
$$

The independent-bridge cycle is the Lorentzian real form in
(3D.113), or an intrinsic Euclidean middle-dimensional cycle carrying
the ordered coefficient orientation (3D.19); its antifields obey
(3D.52a).  Omitting (3D.115) while integrating both bridges
double-counts the frame orbit.  In the symmetric composite section
(3D.107), these three independent blocks are absent.  Equations
(3D.113)--(3D.115) are a typing condition, not a second functional:
the present \(W_{\rm ext}\), \(W_\Psi\), density, gauge fermion, and
\(Z\) use only the symmetric composite branch.  Independently
integrated bridges are not admitted until their frame-gauge
non-minimal sector, counterterm recursion, BV density, and
residual-transverse cycle are added by a separate contract.

### 3D.11 Exact Lorentz--Euclidean transport

The locked physical-field and action map is

$$
\boxed{
\begin{gathered}
x_E^4=ix_L^0,
\qquad
d^4x_L=-i\,d^4x_E,\\
(\mathcal V_L,\Phi_L,\widetilde\Phi_L)
\big|_{\rm Wick}
=(\mathcal V_E,\Phi_E,\widetilde\Phi_E),\\
S_{0,E}=-iS_{0,L}\big|_{\rm Wick},
\qquad
i\mathscr J_L^{\rm phys}\big|_{\rm Wick}
=\mathscr J_E^{\rm phys}.
\end{gathered}}
\tag{3D.116}
$$

Exact finite-cutoff transport requires a paired regulator.  Define
\(M_\nu^{\rm W}\) by

$$
\boxed{
\begin{gathered}
N_{E,\nu,\varsigma}^{x}=N_{L,\nu,\varsigma}^{x},
\qquad
\iota_{E,\nu}M_\nu^{\rm W}
=\operatorname{Wick}\,\iota_{L,\nu},\\
\pi_{E,\nu}\operatorname{Wick}
=M_\nu^{\rm W}\pi_{L,\nu},
\qquad
P_{E,\nu}\operatorname{Wick}
=\operatorname{Wick}P_{L,\nu},\\
\mathfrak L_{E,\nu}^{\rm phys,W}
:=M_\nu^{\rm W,phys}\mathfrak L_{L,\nu}^{\rm phys}.
\end{gathered}}
\tag{3D.117}
$$

The boundary data, primal bases, and dual bases in (3D.12a) are mapped
by the same equations.  For every field block \(X\), the coefficient
matrix is calculated from the dual basis:

$$
\boxed{
\begin{aligned}
(M_{\nu}^{\rm W,X})^{\beta_X,sn}{}_{\alpha_X,rm}
&:=\int_{E,\varsigma_X}
 U_{E,X}^{\vee\,\beta_X,sn}
 \operatorname{Wick}_X
 (U_{L,X,\alpha_X,rm}),\\
&=(w_X)^{\beta_X}{}_{\alpha_X}\,
\delta^s{}_r\,
(w_{\varsigma_X})^n{}_m,\qquad
\operatorname{Ber}w_X\ne0,\qquad
\operatorname{Ber}w_{\varsigma_X}\ne0.
\end{aligned}}
\tag{3D.117a}
$$

Here \(\alpha_X,\beta_X\) contain every adjoint, matter,
row/column, and multiplicity index of the block.  Blockwise,
\(\pi_{E,X}\operatorname{Wick}_X
=M_\nu^{\rm W,X}\pi_{L,X}\) and
\(P_{E,X}\operatorname{Wick}_X
=\operatorname{Wick}_XP_{L,X}\).
For the explicit bump regulator in (3D.12a), let \(w_X\) be the
locked finite matrix on the displayed internal indices and let
\(w_{\varsigma_X}\) be the finite Grassmann-monomial Wick matrix.
Then (3D.117a) is nonzero and invertible.  Its mode factor is exactly
the identity, so compact supports remain
away from both boundaries and every spacetime boundary flux remains
zero.

Define the named total-field types and the independent split blocks by

$$
\boxed{
\begin{aligned}
\mathscr B_{\rm fld}
:={}&\{\mathcal V,\Phi,\widetilde\Phi,
\mathfrak c,\widetilde{\mathfrak c}\}
\sqcup\{\mathfrak u_\ell,\mathfrak v_\ell\}_{\ell\in\mathscr R_{\rm nm}},
\\
X\in{}&
\{\zeta_Y:Y\in\mathscr B_{\rm fld}\}_{\rm integrated}
\sqcup
\{\overline Q_Y,\Omega_Y:Y\in\mathscr B_{\rm fld}\}_{\rm external}\\
&\sqcup\{\Xi^{\rm NK}\}_{\rm external\ determinant\text{-}auxiliary},
\qquad
X_E:=X_L\big|_{\rm Wick}.
\end{aligned}}
\tag{3D.117b}
$$

For every \(Y\in\mathscr B_{\rm fld}\),
\(Q_{{\rm tot},Y}=\Sigma_Y(\overline Q_Y,\zeta_Y)\) is composite and
is not an additional direct-sum coordinate.  Thus (3D.117b) never
counts both \(Q_{\rm tot}\) and \(\zeta\).
The named \((\mathfrak c',\widetilde{\mathfrak c}',
\mathfrak n,\widetilde{\mathfrak n})\) are aliases of selected
\((\mathfrak u_\ell,\mathfrak v_\ell)\) blocks and are not counted
again.  The \(\Xi^{\rm NK}\) entry is present only when the external
measure-only factor has the admitted auxiliary realization (3D.96);
it is not a main-integral BV coordinate.  BV--NK doublets instead
belong to \(\mathscr R_{\rm NK}^{\rm BV}\subset\mathscr R_{\rm nm}\)
and already occur among the integrated \(\zeta_Y\) blocks.  The blocks
\((\mathcal B,\widetilde{\mathcal B},\mathfrak k)\) are added only in
the independent-bridge extension (3D.113)--(3D.115); they are absent
in the symmetric composite section.  The matrix \(M_\nu^{\rm W}\) is
even, ghost-number
preserving, and block diagonal in the domains.  If any equality in
(3D.117) fails, retain

$$
\mathfrak D_{\nu}^{\rm W}
:=P_{E,\nu}\operatorname{Wick}
 -\operatorname{Wick}P_{L,\nu}
\tag{3D.117c}
$$

and do not assert the equalities below.

Separate the residual-free integrated and external blocks:

$$
\boxed{
\begin{aligned}
M_{\zeta,\nu}^{\rm W}
&:=\bigoplus_{Y\in\mathscr B_{\rm fld}}
M_\nu^{\rm W,\zeta_Y},\\
M_{\zeta,\nu}^{\rm W}
\widehat\kappa_{\Psi,L,\nu}(\widehat x_L;\overline Q_L)
&=\widehat\kappa_{\Psi,E,\nu}\!\left(
M_{\nu,\rm int}^{\rm W,\perp}\widehat x_L;
M_{\overline Q}^{\rm W}\overline Q_L\right),\\
M_{\nu,\rm int}^{\rm W,\perp}
&:=\widehat{\mathbb P}_{\Psi,E,\nu}
M_{\zeta,\nu}^{\rm W}
\widehat{\mathbb I}_{\Psi,L,\nu},\\
\widehat x_E
&=M_{\nu,\rm int}^{\rm W,\perp}\widehat x_L,
\qquad
\frac{\vec\partial M_{\nu,\rm int}^{\rm W,\perp}}
{\partial\widehat x_L}=0,
\qquad
\frac{\vec\partial M_{\nu,\rm int}^{\rm W,\perp}}
{\partial\overline Q_L}=0,\\
M_{\zeta,\nu}^{\rm W}\widehat{\mathbb I}_{\Psi,L,\nu}
&=\widehat{\mathbb I}_{\Psi,E,\nu}
M_{\nu,\rm int}^{\rm W,\perp},
\qquad
M_{\nu,\rm int}^{\rm W,\perp}
\widehat{\mathbb P}_{\Psi,L,\nu}
=\widehat{\mathbb P}_{\Psi,E,\nu}M_{\zeta,\nu}^{\rm W},\\
M_{\zeta,\nu}^{\rm W}\widehat{\mathbb N}_{\Psi,L,\nu}
&=\widehat{\mathbb N}_{\Psi,E,\nu}M_{\nu,\rm nor}^{\rm W},
\qquad
M_{\nu,\rm nor}^{\rm W}\widehat{\mathbb R}_{\Psi,L,\nu}
=\widehat{\mathbb R}_{\Psi,E,\nu}M_{\zeta,\nu}^{\rm W},\\
M_{\overline Q^\star}^{\rm W}[\overline Q_L^\star]
&:=-i\overline Q_L^\star(M_{\overline Q}^{\rm W})^{-1},\\
M_{\Omega^\star}^{\rm W}[\Omega_L^\star]
&:=-i\Omega_L^\star(M_{\Omega}^{\rm W})^{-1},\\
M_{\star{\rm ext}}^{\rm W}[Q_L^{\star{\rm ext}}]
&:=-iQ_L^{\star{\rm ext}}
(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
M_{\nu,\rm ext}^{\rm W}
&:=M_{\overline Q}^{\rm W}\oplus M_{\Omega}^{\rm W}
\oplus M_{\overline Q^\star}^{\rm W}
\oplus M_{\Omega^\star}^{\rm W}
\oplus M_{\star{\rm ext}}^{\rm W}.
\end{aligned}}
\tag{3D.117d}
$$

The collective source, field density, and cycle map are

$$
\boxed{
\begin{aligned}
\widehat\jmath_{E,\nu}
&=i\widehat\jmath_{L,\nu}
(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
\boldsymbol\varpi_{E,\nu}(q_E)
&=\boldsymbol\varpi_{L,\nu}
 ((M_\nu^{\rm W,phys})^{-1}q_E)
 \operatorname{Ber}(M_\nu^{\rm W,phys})^{-1},\\
\mathfrak L_{E,\nu}^{\rm phys,W}
&=M_\nu^{\rm W,phys}\mathfrak L_{L,\nu}^{\rm phys}.
\end{aligned}}
\tag{3D.118}
$$

The full gauge-fixed and external-source transport is

$$
\boxed{
\begin{aligned}
Q_{E,\nu}^{\star{\rm ext}}
&=-iQ_{L,\nu}^{\star{\rm ext}}
(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
\overline Q_E&=M_{\overline Q}^{\rm W}\overline Q_L,
&\Omega_E&=M_{\Omega}^{\rm W}\Omega_L,\\
\overline Q_E^\star
&=-i\overline Q_L^\star(M_{\overline Q}^{\rm W})^{-1},
&\Omega_E^\star
&=-i\Omega_L^\star(M_{\Omega}^{\rm W})^{-1},\\
\Psi_E&=-i\Psi_L\big|_{\rm Wick},
&W_{\Psi,E,\nu}&=-iW_{\Psi,L,\nu}\big|_{\rm Wick},\\
\frac{\vec\partial\Psi_E}{\partial x_E}
&=-i\frac{\vec\partial\Psi_L}{\partial x_L}
(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
Q_E^{\star{\rm ext}}-
\frac{\vec\partial\Psi_E}{\partial x_E}
&=-i\left(Q_L^{\star{\rm ext}}-
\frac{\vec\partial\Psi_L}{\partial x_L}\right)
(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
\mathfrak L_{\Psi,E,\nu}^{\perp,{\rm W}}
&=M_{\nu,\rm int}^{\rm W,\perp}
\mathfrak L_{\Psi,L,\nu}^{\perp},\\
\boldsymbol\varpi_{\Psi,E,\nu}(x_E)
&=\boldsymbol\varpi_{\Psi,L,\nu}
((M_{\nu,\rm int}^{\rm W,\perp})^{-1}x_E)
\operatorname{Ber}(M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
d\mu_{\Psi,E,\nu}
&=(M_{\nu,\rm int}^{\rm W,\perp})_*d\mu_{\Psi,L,\nu},\\
\mathscr Q_{\Psi,E,\nu}^{\rm W}
&:=\mathscr Q_{\Psi,L,\nu}\big|_{\rm Wick}.
\end{aligned}}
\tag{3D.118a}
$$

Let \(M_{\mathscr G}^\mathrm W,M_{\mathscr F}^\mathrm W,
M_{\mathscr F^\vee}^\mathrm W,M_{\mathfrak n}^\mathrm W\) be the
corresponding blocks of (3D.117a).  Exact determinant-sector transport
requires

$$
\boxed{
\begin{aligned}
M_{\mathscr F}^{\rm W}\mathcal M_L^{\rm FP}
=\mathcal M_E^{\rm FP}M_{\mathscr G}^{\rm W},
\qquad
M_{\mathscr F^\vee}^{\rm W}\mathcal Y_L
=\mathcal Y_EM_{\mathfrak n}^{\rm W},\\
M_{\mathscr F}^{\rm W}\mathcal M_{0,L}^{\perp}
=\mathcal M_{0,E}^{\perp}M_{\mathscr G}^{\rm W},
\qquad
M_{\mathscr F^\vee}^{\rm W}\mathcal Y_{0,L}
=\mathcal Y_{0,E}M_{\mathfrak n}^{\rm W},\\
M_{\mathscr G}^{\rm W}\mathscr H_{L,\nu}
=\mathscr H_{E,\nu},
\qquad
M_{\mathscr G}^{\rm W}\mathscr G_{L,\nu}^{\perp}
=\mathscr G_{E,\nu}^{\perp},\\
\mathfrak C_{\rm gh,E,\nu}^{\perp}(t)
&=(M_{\Pi\mathscr G}^{\rm W}
\oplus M_{\Pi\mathscr F^\vee}^{\rm W})
\mathfrak C_{\rm gh,L,\nu}^{\perp}(t),
\qquad
\mathfrak C_{\mathfrak n,E,\nu}
=M_{\mathfrak n}^{\rm W}\mathfrak C_{\mathfrak n,L,\nu},\\
\mathfrak C_{f,E,\nu}
&=M_{\mathscr F}^{\rm W}\mathfrak C_{f,L,\nu},
\qquad
\mathfrak C_{\Xi,E,\nu}
=M_{\Xi}^{\rm W}\mathfrak C_{\Xi,L,\nu},\\
\mathfrak F_{E,\nu}^{\rm FP}
=\mathfrak F_{L,\nu}^{\rm FP}\big|_{\rm Wick},
\qquad
\mathfrak F_{E,\nu}^{\rm NK}
=\mathfrak F_{L,\nu}^{\rm NK}\big|_{\rm Wick}.
\end{aligned}}
\tag{3D.118b}
$$

If any line of (3D.118a)--(3D.118b) fails, its mismatch is retained
and the full gauge-fixed Wick equality is not asserted.

With the Lorentzian damping functional transported to the Wick-image
cycle, finite change of variables gives

$$
\boxed{
\mathcal Z_{\Psi,L,\nu}^{\epsilon}
 [\widehat\jmath_L]\big|_{\rm Wick}
=\mathcal Z_{\Psi,E,\nu}^{\epsilon,\rm W}
 [\widehat\jmath_E;
 \mathfrak L_{\Psi,E,\nu}^{\perp,\rm W}].}
\tag{3D.119}
$$

The right side is the explicit integral

$$
\boxed{
\begin{aligned}
\mathcal Z_{\Psi,E,\nu}^{\epsilon,\rm W}
[\widehat\jmath_E]
&:=\mathfrak F_{E,\nu}^{\rm NK}
\int_{\mathfrak L_{\Psi,E,\nu}^{\perp,\rm W}}
d\mu_{\Psi,E,\nu}\,
\exp\left[
\tau_E\left(W_{\Psi,E,\nu}
+\upsilon_E\mathscr J_{E,\nu}^{\rm coll}\right)
-\epsilon\mathscr Q_{\Psi,E,\nu}^{\rm W}
\right],\\
\mathfrak D_{\Psi,E,\nu}^{\rm cyc}[\widehat\jmath_E]
&:=\mathcal Z_{\Psi,E,\nu}
[\widehat\jmath_E;\mathfrak L_{\Psi,E,\nu}^{\perp}]
-\lim_{\epsilon\downarrow0}
\mathcal Z_{\Psi,E,\nu}^{\epsilon,\rm W}
[\widehat\jmath_E;
\mathfrak L_{\Psi,E,\nu}^{\perp,\rm W}],\\
\mathfrak D_{\Psi,E,\nu}^{\rm cyc}[\widehat\jmath_E]
&=\mathfrak D_{\Psi,E,\nu}^{\rm cyc}[0]=0
\quad\text{is the intrinsic-cycle admission condition}.
\end{aligned}}
\tag{3D.119a}
$$

The \(\epsilon\downarrow0\) equality is admitted only when both
limits exist.  The last line of (3D.119a) is proved by a homotopy from
\(\mathfrak L_{\Psi,E,\nu}^{\perp,\rm W}\) to
\(\mathfrak L_{\Psi,E,\nu}^{\perp}\) only when the integrand is
holomorphic throughout, no singularity is crossed, and the integrated
boundary flux vanishes.  Otherwise
\(\mathfrak D_{\Psi,E,\nu}^{\rm cyc}\) is retained and no intrinsic
Lorentz--Euclidean equality is asserted.

For the full BV coefficient space define

$$
\boxed{
\begin{aligned}
\widehat Q_{E,\nu}&=M_\nu^{\rm W}\widehat Q_{L,\nu},\\
\widehat Q^\star_{E,\nu}
&=-i\widehat Q^\star_{L,\nu}(M_\nu^{\rm W})^{-1},\\
W_{E,\nu}&=-iW_{L,\nu}\big|_{\rm Wick},\\
T_\nu^{\rm W}(\widehat Q_L,\widehat Q_L^\star)
&:=\left(M_\nu^{\rm W}\widehat Q_L,
 -i\widehat Q_L^\star(M_\nu^{\rm W})^{-1}\right),\\
\widehat{\boldsymbol\varpi}_{\rm ext,E,\nu}
&:=(T_\nu^{\rm W})_*
 \widehat{\boldsymbol\varpi}_{\rm ext,L,\nu}.
\end{aligned}}
\tag{3D.120}
$$

The ordered coefficient derivatives are

$$
\boxed{
\frac{\vec\partial}{\partial\widehat Q_E^{\mathsf i}}
=((M_\nu^{\rm W})^{-1})^{\mathsf j}{}_{\mathsf i}
 \frac{\vec\partial}{\partial\widehat Q_L^{\mathsf j}},
\qquad
\frac{\vec\partial}{\partial\widehat Q^\star_{E,\mathsf i}}
=i(M_\nu^{\rm W})^{\mathsf i}{}_{\mathsf j}
 \frac{\vec\partial}{\partial\widehat Q^\star_{L,\mathsf j}}.}
\tag{3D.121}
$$

For

$$
F_E:=F_L\circ(T_\nu^{\rm W})^{-1},
\qquad
G_E:=G_L\circ(T_\nu^{\rm W})^{-1},
\tag{3D.121a}
$$

equations (3D.54), (3D.61), (3D.120), and (3D.121) give

$$
\boxed{
(F_E,G_E)_{\rm ext,E,\nu}
=i(F_L,G_L)_{\rm ext,L,\nu}\big|_{\rm Wick},
\qquad
\Delta_{\rm ext,E,\nu}F_E
=i(\Delta_{\rm ext,L,\nu}F_L)\big|_{\rm Wick}.}
\tag{3D.122}
$$

For \(W_E=-iW_L|_{\rm Wick}\),

$$
\Delta_{\rm ext,E,\nu}W_{E,\nu}
=(\Delta_{\rm ext,L,\nu}W_{L,\nu})\big|_{\rm Wick}.
\tag{3D.123}
$$

The QME maps term by term:

$$
\boxed{
\begin{aligned}
\mathfrak O^{\rm BV,ext}_{E,\nu}[W_E]
&=\frac12(W_E,W_E)_{\rm ext,E,\nu}
-\hbar\Delta_{\rm ext,E,\nu}W_E\\
&=-\frac i2(W_L,W_L)_{\rm ext,L,\nu}\big|_{\rm Wick}
 -\hbar(\Delta_{\rm ext,L,\nu}W_L)\big|_{\rm Wick}\\
&=-i\,\mathfrak O^{\rm BV,ext}_{L,\nu}[W_L]
 \big|_{\rm Wick}.
\end{aligned}}
\tag{3D.124}
$$

The paired supercharge matrices and their gauge-fixed defect obey

$$
\boxed{
\begin{aligned}
\mathbb Q^{\rm int}_{E,\nu a}
&=-iM_{\nu,\rm int}^{\rm W,\perp}
\mathbb Q^{\rm int}_{L,\nu a}
 (M_{\nu,\rm int}^{\rm W,\perp})^{-1},\\
\mathbb Q^{\rm ext}_{E,\nu a}
&=-i\operatorname{Wick}\mathbb Q^{\rm ext}_{L,\nu a}
\operatorname{Wick}^{-1},\\
\mathfrak b^{Q,\epsilon,\rm W}_{E,\nu a}
&=-i\mathfrak b^{Q,\epsilon}_{L,\nu a}\big|_{\rm Wick},\\
\langle\mathfrak C^{\rm cyc,Q}_{E,\nu a}\rangle
&=-i\langle\mathfrak C^{\rm cyc,Q}_{L,\nu a}\rangle
\big|_{\rm Wick}.
\end{aligned}}
\tag{3D.124a}
$$

and identically for the dotted supercharge.  Lorentzian reality is
part of \(\mathfrak L_{L,\nu}\); intrinsic Euclidean tilded and
untilded variables remain independent until the Euclidean cycle is
chosen.

### 3D.12 Gauge-fixed, connected, and one-particle-irreducible functionals

For the hatted integrated residual-slice coordinates define the
ordered collective source pairing

$$
\boxed{
\begin{aligned}
\mathscr J_{R,\nu}^{\rm coll}
&:=\langle\widehat\jmath_{R,\nu},
 \widehat x_{R,\nu}\rangle_{\rm ord},\\
\jmath_{R,\nu,\mathsf r}
&:=\mu^{-[x^{\mathsf r}]}
\widehat\jmath_{R,\nu,\mathsf r},
\qquad
x_{R,\nu}^{\mathsf r}
:=\mu^{[x^{\mathsf r}]}
\widehat x_{R,\nu}^{\mathsf r},\\
\langle\widehat\jmath,\widehat x\rangle_{\rm ord}
&=\langle\jmath,x\rangle_{\rm ord},\\
\epsilon(\widehat\jmath_{\mathsf r})
&=\epsilon(\widehat x^{\mathsf r}),
&
\operatorname{gh}(\widehat\jmath_{\mathsf r})
&=-\operatorname{gh}(\widehat x^{\mathsf r}),
&[\widehat\jmath_{\mathsf r}]&=0,
&[\jmath_{\mathsf r}]&=-[x^{\mathsf r}].
\end{aligned}}
\tag{3D.124b}
$$

The source real forms are fixed by nondegeneracy of the ordered
pairing:

$$
\boxed{
\langle\widehat\jmath_{L,\nu},\widehat x_{L,\nu}
\rangle_{\rm ord}^{\ddagger_L}
=\langle\widehat\jmath_{L,\nu},\widehat x_{L,\nu}
\rangle_{\rm ord},
\qquad
\widehat\jmath_{E,\nu}\text{ has independent conjugate-paired blocks
before the Euclidean source cycle}.}
\tag{3D.124d}
$$

The antichiral row order in (3D.8) is retained inside
\(\langle\ ,\ \rangle_{\rm ord}\).  Let
\(\mathscr Q_{\Psi,L,\nu}\) be an even positive convergence
functional on every oscillatory bosonic coefficient, including
multiplier and admitted NK coefficients.  Define

$$
\boxed{
\begin{aligned}
\mathscr E_{\Psi,L,\nu}^{\epsilon}
&:=\tau_L\left(
 W_{\Psi,L,\nu}
 +\mathscr J_{L,\nu}^{\rm coll}\right)
 -\epsilon\mathscr Q_{\Psi,L,\nu},\\
\mathscr E_{\Psi,E,\nu}
&:=\tau_E\left(
 W_{\Psi,E,\nu}
 +\upsilon_E\mathscr J_{E,\nu}^{\rm coll}\right).
\end{aligned}}
\tag{3D.124c}
$$

Use the shorthand \(\mathscr E_{\Psi,R,\nu}\) for \(\mathscr E_{\Psi,L,\nu}^{\epsilon}\) at \(R=L\) and for \(\mathscr E_{\Psi,E,\nu}\) at \(R=E\).

The Euclidean cycle must make the bosonic ends of
\(\mathscr E_{\Psi,E,\nu}\) convergent; its multiplier component is
the cycle in (3D.93a).  Write
\(\mathfrak F_{R,\nu}^{\rm NK}=1\) outside the standard family
(3D.89), on the coupled branch of (3D.95b), on the density-absorbed
branch following failure of (3D.96a), and on the admitted BV--NK row
of (3D.96b).  Only the quantum-field-independent external
measure-only row has
\(\mathfrak F_{R,\nu}^{\rm NK}
=\mathfrak F_{R,\nu}^{\rm NK,req}\).  On the BV--NK row,
\(W_{\Psi,R,\nu}\), \(d\mu_{\Psi,R,\nu}\), and the integrated
coordinate list already contain the selected NK doublets through
(3D.71b), (3D.71c), (3D.77), and (3D.78).  The unnormalized
functionals are

$$
\boxed{
\begin{aligned}
\mathcal Z_{\Psi,L,\nu}^{\epsilon}
[\widehat\jmath;Q^{\star{\rm ext}},\overline Q,
 \overline Q^\star,\Omega,\Omega^\star]
&:=\mathfrak F_{L,\nu}^{\rm NK}
 \int_{\mathfrak L_{\Psi,L,\nu}^{\perp}}
 d\mu_{\Psi,L,\nu}\,e^{\mathscr E_{\Psi,L,\nu}^{\epsilon}},\\
\mathcal Z_{\Psi,E,\nu}
[\widehat\jmath;Q^{\star{\rm ext}},\overline Q,
 \overline Q^\star,\Omega,\Omega^\star]
&:=\mathfrak F_{E,\nu}^{\rm NK}
 \int_{\mathfrak L_{\Psi,E,\nu}^{\perp}}
 d\mu_{\Psi,E,\nu}\,e^{\mathscr E_{\Psi,E,\nu}}.
\end{aligned}}
\tag{3D.125}
$$

The variables \(\overline Q,\overline Q^\star,\Omega,\Omega^\star\)
and the integrated-field antifield sources \(Q^{\star{\rm ext}}\) are
external arguments and are never integrated in (3D.125).  The symbols
\(\mathcal Z_{\Psi,R,\nu}\) and
\(Z_{\Psi,R,\nu}\) below mean the corresponding Lorentzian regulated
object before the \(\epsilon\downarrow0\) limit, or the Euclidean
object on its declared cycle.

If the source-zero denominator is finite and nonzero, define

$$
\boxed{
\begin{aligned}
Z_{\Psi,E,\nu}[\widehat\jmath]
&:=\frac{\mathcal Z_{\Psi,E,\nu}
[\widehat\jmath;Q^{\star{\rm ext}},\overline Q,
\overline Q^\star,\Omega,\Omega^\star]}
 {\mathcal Z_{\Psi,E,\nu}
[0;Q^{\star{\rm ext}},\overline Q,
\overline Q^\star,\Omega,\Omega^\star]},\\
Z_{\Psi,L,\nu}[\widehat\jmath]
&:=\lim_{\epsilon\downarrow0}
 \frac{\mathcal Z_{\Psi,L,\nu}^{\epsilon}
[\widehat\jmath;Q^{\star{\rm ext}},\overline Q,
\overline Q^\star,\Omega,\Omega^\star]}
 {\mathcal Z_{\Psi,L,\nu}^{\epsilon}
[0;Q^{\star{\rm ext}},\overline Q,
\overline Q^\star,\Omega,\Omega^\star]}.
\end{aligned}}
\tag{3D.125a}
$$

All external arguments are held fixed in each ratio.  The residual
orbit is absent from both integrals in (3D.125a).  For
any insertion \(\mathcal O\),

$$
\boxed{
\langle\mathcal O\rangle_{\widehat\jmath}
:=\frac{
 \int_{\mathfrak L_{\Psi,R,\nu}^{\perp}}d\mu_{\Psi,R,\nu}\,
 \mathcal Oe^{\mathscr E_{\Psi,R,\nu}}
}{
 \int_{\mathfrak L_{\Psi,R,\nu}^{\perp}}d\mu_{\Psi,R,\nu}\,
 e^{\mathscr E_{\Psi,R,\nu}}
}.}
\tag{3D.125b}
$$

For \(R=L\), (3D.125b) denotes the regulated ratio before its proved
\(\epsilon\downarrow0\) limit.

The connected generator has the unified definition

$$
\boxed{
\begin{gathered}
Z_{\Psi,R,\nu}[0]=1,
\qquad
\left.\log Z_{\Psi,R,\nu}\right|_{\widehat\jmath=0}=0,\\
\mathscr W_{c,R,\nu}
:=\frac{\upsilon_R}{\tau_R}
 \log Z_{\Psi,R,\nu},
\qquad
\mathscr W_{c,L,\nu}=-i\hbar\log Z_{\Psi,L,\nu},
\qquad
\mathscr W_{c,E,\nu}=+\hbar\log Z_{\Psi,E,\nu}.
\end{gathered}}
\tag{3D.126}
$$

The logarithm is the unique local branch through
\((Z,\log Z)=(1,0)\); (3D.128a) transports this branch.

Define mean fields and the action-like Legendre transform by

$$
\boxed{
\begin{aligned}
\widehat{\mathcal Q}_{\mathrm{mean},R,\nu}^{\mathsf r}
&:=\frac{\vec\partial\mathscr W_{c,R,\nu}}
 {\partial\widehat\jmath_{R,\nu,\mathsf r}},\\
\mathcal Q_{\mathrm{mean},R,\nu}^{\mathsf r}
&:=\mu^{[x^{\mathsf r}]}
\widehat{\mathcal Q}_{\mathrm{mean},R,\nu}^{\mathsf r},\\
\mathscr S_{R,\nu}^{\rm 1PI}
&:=\upsilon_R\left(
 \mathscr W_{c,R,\nu}
 -\langle\jmath_{R,\nu},
 \mathcal Q_{\mathrm{mean},R,\nu}\rangle_{\rm ord}
 \right).
\end{aligned}}
\tag{3D.127}
$$

The partial Legendre chart is used only on a source neighborhood where

$$
\boxed{
\operatorname{Ber}\left(
\frac{\vec\partial
\widehat{\mathcal Q}_{\mathrm{mean},R,\nu}^{\mathsf r}}
{\partial\widehat\jmath_{R,\nu,\mathsf s}}
\right)\ne0.}
\tag{3D.127a}
$$

Direct differentiation gives

$$
\boxed{\begin{aligned}
\mathscr S_{R,\nu}^{\rm 1PI}
 \frac{\overleftarrow\partial}
 {\partial\widehat{\mathcal Q}_{\mathrm{mean},R,\nu}^{\mathsf r}}
=-\upsilon_R\widehat\jmath_{R,\nu,\mathsf r},
\qquad
\mathscr S_{R,\nu}^{\rm 1PI}
 \frac{\overleftarrow\partial}
 {\partial\mathcal Q_{\mathrm{mean},R,\nu}^{\mathsf r}}
=-\upsilon_R\jmath_{R,\nu,\mathsf r},\\
(
\mathscr S_R^{\rm 1PI})^{(0)}[\mathcal Q]
=S_{\Psi,R}[\iota^{\rm int}_{\Psi,R,\nu}\mathcal Q]
-S_{\Psi,R}[\iota^{\rm int}_{\Psi,R,\nu}\mathcal Q_{\rm vac}].
\end{aligned}}
\tag{3D.128}
$$

On the restriction of every ghost, arbitrary non-minimal doublet,
conditional frame doublet, and admitted BV--NK multiplet to zero, and
with \(Q^{\star{\rm ext}}=\Omega=0\), this becomes
\(S_{0,R}[\iota^{\rm int}_{\Psi,R,\nu}\mathcal Q]
-S_{0,R}[\iota^{\rm int}_{\Psi,R,\nu}\mathcal Q_{\rm vac}]\); no vacuum
constant is silently set to zero.

Under (3D.117)--(3D.119a), including
\(\mathfrak D_{\Psi,E,\nu}^{\rm cyc}[\widehat\jmath_E]
=\mathfrak D_{\Psi,E,\nu}^{\rm cyc}[0]=0\),

$$
\boxed{
\mathcal Q_{\mathrm{mean},E,\nu}
=M_{\nu,\rm int}^{\rm W,\perp}
\mathcal Q_{\mathrm{mean},L,\nu},
\qquad
\mathscr W_{c,E,\nu}
=i\mathscr W_{c,L,\nu}\big|_{\rm Wick},
\qquad
\mathscr S_{E,\nu}^{\rm 1PI}
=-i\mathscr S_{L,\nu}^{\rm 1PI}\big|_{\rm Wick}.}
\tag{3D.128a}
$$

Equation (3D.128a) also requires
\(\mathcal Q_{\rm vac,E}
=M_{\nu,\rm int}^{\rm W,\perp}\mathcal Q_{\rm vac,L}\) and
\(S_{\Psi,E}[\mathcal Q_{\rm vac,E}]
=-iS_{\Psi,L}[\mathcal Q_{\rm vac,L}]|_{\rm Wick}\).

Let \(x_{R,\nu}^{\mathsf r}\) denote only the integrated
coordinates on \(\mathfrak L_{\Psi,R,\nu}^{\perp}\).  The integrated
and external supercharge vector fields are

$$
\boxed{
\begin{aligned}
\mathcal V^{Q,\mathfrak a}_{\Psi,R,\nu a}
&:=\left.(\mathsf Q_{Ra}\zeta_R^{\mathfrak a})
\right|_{\zeta=\kappa_\Psi(x)}
-\left.
(\mathsf Q_{Ra}\overline Q_R^{\underline\imath})
\frac{\vec\partial
\kappa_{\Psi,R,\nu}^{\mathfrak a}(x;\overline Q)}
{\partial\overline Q_R^{\underline\imath}}
\right|_x,\\
\mathcal X^{Q,\mathsf r}_{\Psi,R,\nu a}
&:=\mathbb P_{\Psi,R,\nu}^{\mathsf r}{}_{\mathfrak a}
\mathcal V^{Q,\mathfrak a}_{\Psi,R,\nu a},
\qquad
\widehat{\mathcal X}^{Q,\mathsf r}_{\Psi,R,\nu a}
:=\mu^{-[x^{\mathsf r}]}
\mathcal X^{Q,\mathsf r}_{\Psi,R,\nu a},\\
\mathbb Q^{\rm int}_{R,\nu a}
&:=\widehat{\mathcal X}^{Q,\mathsf r}_{\Psi,R,\nu a}
\frac{\vec\partial}{\partial\widehat x^{\mathsf r}},\\
\mathbb Q^{\rm ext}_{R,\nu a}
&:=(\mathsf Q_{Ra}\overline Q_R^{\underline\imath})
 \frac{\vec\partial}{\partial\overline Q_R^{\underline\imath}}
 +(\mathsf Q_{Ra}\Omega_R^{\underline\imath})
 \frac{\vec\partial}{\partial\Omega_R^{\underline\imath}}\\
&\quad+(\mathsf Q_{Ra}\overline Q^\star_{R,\underline\imath})
 \frac{\vec\partial}{\partial\overline Q^\star_{R,\underline\imath}}
 +(\mathsf Q_{Ra}\Omega^\star_{R,\underline\imath})
 \frac{\vec\partial}{\partial\Omega^\star_{R,\underline\imath}}\\
&\quad+(\mathsf Q_{Ra}\widehat Q_{R,\mathsf r}^{\star{\rm ext}})
 \frac{\vec\partial}
 {\partial\widehat Q_{R,\mathsf r}^{\star{\rm ext}}},\\
\mathbb Q^{\rm tot}_{R,\nu a}
&:=\mathbb Q^{\rm int}_{R,\nu a}
 +\mathbb Q^{\rm ext}_{R,\nu a},
\end{aligned}}
\tag{3D.128b}
$$

The cotangent action is the full adapted Hamiltonian lift; the
ordinary linear source is inert.

$$
\boxed{
\begin{aligned}
H_{\Psi,R,\nu a}^{Q,{\rm ad}}
&:=\sum_{\mathsf r}(-1)^{\epsilon_{x^{\mathsf r}}}
\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}}
\widehat{\mathcal X}_{\Psi,R,\nu a}^{Q,\mathsf r}\\
&\quad+\sum_{\underline\imath}
(-1)^{\epsilon_{\overline Q^{\underline\imath}}}
\overline Q_{R,\underline\imath}^{\star{\rm ext},{\rm ad}}
(\mathsf Q_{Ra}\overline Q_R^{\underline\imath})\\
&\quad+\sum_{\underline\imath}
(-1)^{\epsilon_{\Omega^{\underline\imath}}}
\Omega^\star_{R,\underline\imath}
(\mathsf Q_{Ra}\Omega_R^{\underline\imath}),\\
\mathsf Q_{Ra}\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}}
&:=(H_{\Psi,R,\nu a}^{Q,{\rm ad}},
\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\Psi,R,\nu a}^{Q,{\rm ad}}
\frac{\overleftarrow\partial}{\partial\widehat x^{\mathsf r}},\\
\mathsf Q_{Ra}\overline Q_{R,\underline\imath}^{\star{\rm ext},{\rm ad}}
&:=(H_{\Psi,R,\nu a}^{Q,{\rm ad}},
\overline Q_{R,\underline\imath}^{\star{\rm ext},{\rm ad}})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\Psi,R,\nu a}^{Q,{\rm ad}}
\frac{\overleftarrow\partial}
{\partial\overline Q_R^{\underline\imath}},\\
\mathsf Q_{Ra}\Omega^\star_{R,\underline\imath}
&:=(H_{\Psi,R,\nu a}^{Q,{\rm ad}},
\Omega^\star_{R,\underline\imath})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\Psi,R,\nu a}^{Q,{\rm ad}}
\frac{\overleftarrow\partial}{\partial\Omega_R^{\underline\imath}},\\
\mathbb Q^{\rm int}_{R,\nu a}+\mathbb Q^{\rm ext}_{R,\nu a}
&=(H_{\Psi,R,\nu a}^{Q,{\rm ad}},\,\cdot\,)
_{\Psi,R,\nu}^{\rm ad,ext},
\qquad
\mathbb Q^{\rm tot}_{R,\nu a}\widehat\jmath_{R,\nu,\mathsf r}=0.
\end{aligned}}
\tag{3D.128c}
$$

The split chart is supercharge-equivariant by definition:

$$
\boxed{
\begin{aligned}
\mathsf Q_{Ra}\zeta_R^{\mathfrak a}
&:=L_R^{\mathfrak a}{}_{\mathsf i}
\left[
\mathsf Q_{Ra}Q_{R,\mathrm{tot}}^{\mathsf i}
-B_R^{\mathsf i}{}_{\underline\imath}
 \mathsf Q_{Ra}\overline Q_R^{\underline\imath}
\right],\\
\mathsf Q_{Ra}Q_{R,\mathrm{tot}}^{\mathsf i}
&=B_R^{\mathsf i}{}_{\underline\imath}
 \mathsf Q_{Ra}\overline Q_R^{\underline\imath}
+\mathbb J_R^{\mathsf i}{}_{\mathfrak a}
 \mathsf Q_{Ra}\zeta_R^{\mathfrak a},\\
\mathsf Q_{Ra}\Omega_R^{\underline\imath}
&:=-\mathbf s_{\mathrm{sp},R}
 (\mathsf Q_{Ra}\overline Q_R^{\underline\imath}),\\
\mathfrak D^{Q}_{\Psi,R,\nu a}{}^{\mathfrak a}
&:=\left(
\delta^{\mathfrak a}{}_{\mathfrak b}
-\Pi_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathfrak b}
\right)
\mathcal V^{Q,\mathfrak b}_{\Psi,R,\nu a},\\
\left.(\mathsf Q_{Ra}\zeta_R^{\mathfrak a})
\right|_{\zeta=\kappa_\Psi(x)}
&=\left.
(\mathsf Q_{Ra}\overline Q_R^{\underline\imath})
\frac{\vec\partial\kappa_{\Psi,R,\nu}^{\mathfrak a}}
{\partial\overline Q_R^{\underline\imath}}
\right|_x
+\mathbb I_{\Psi,R,\nu}^{\mathfrak a}{}_{\mathsf r}
\mathcal X^{Q,\mathsf r}_{\Psi,R,\nu a}
+\mathfrak D^{Q,\mathfrak a}_{\Psi,R,\nu a}.
\end{aligned}}
\tag{3D.128d}
$$

The dotted rules are identical.  Exact supersymmetry on the residual
slice additionally requires \(\mathfrak D^Q_{\Psi,R,\nu a}=0\); a
nonzero value is a retained projection defect.

Ghosts and non-minimal fields inside \(x^{\mathsf r}\) transform as
superfields; the
background partner and external antifield source are not integrated.
The full gauge-fixed divergence is

$$
\boxed{
\operatorname{div}_{\Psi,R,\nu}^{\rm int}X
:=\boldsymbol\varpi_{\Psi,R,\nu}^{-1}
 \sum_{\mathsf r}
 (-1)^{\epsilon_{\mathsf r}(\epsilon_X+1)}
 \frac{\vec\partial}{\partial\widehat x^{\mathsf r}}
 \left(
 \boldsymbol\varpi_{\Psi,R,\nu}X^{\mathsf r}
 \right).}
\tag{3D.129}
$$

Define the cycle-boundary insertion by

$$
\boxed{
\left\langle\mathfrak C^{\rm cyc,Q}_{R,\nu a}\right\rangle
\mathcal Z_{\Psi,R,\nu}
:=\mathfrak F_{R,\nu}^{\rm NK}
\int_{\partial\mathfrak L_{\Psi,R,\nu}^{\perp}}
\iota_{\mathbb Q^{\rm int}_{R,\nu a}}
\left(d\mu_{\Psi,R,\nu}
 e^{\mathscr E_{\Psi,R,\nu}}\right).}
\tag{3D.129a}
$$

For a measure-only NK factor, its supercharge acts on the external
background data.  The finite-cutoff defects are

$$
\boxed{
\begin{aligned}
\mathfrak b^{Q,\epsilon}_{L,\nu a}
:={}&\operatorname{div}_{\Psi,L,\nu}^{\rm int}
 \mathbb Q^{\rm int}_{L,\nu a}
 +(\mathbb Q^{\rm ext}_{L,\nu a}
 \log\boldsymbol\varpi_{\Psi,L,\nu})\\
&+\tau_L\mathbb Q^{\rm tot}_{L,\nu a}W_{\Psi,L,\nu}
+\tau_L\upsilon_L
\left\langle\widehat\jmath_{L,\nu},
\mathbb Q^{\rm int}_{L,\nu a}\widehat x_{L,\nu}
\right\rangle_{\rm ord}
 -\epsilon\mathbb Q^{\rm tot}_{L,\nu a}
 \mathscr Q_{\Psi,L,\nu}\\
&+\mathbb Q^{\rm ext}_{L,\nu a}
 \log\mathfrak F_{L,\nu}^{\rm NK},\\
\mathfrak b^{Q,\epsilon,\rm W}_{E,\nu a}
:={}&\operatorname{div}_{\Psi,E,\nu}^{\rm int}
 \mathbb Q^{\rm int}_{E,\nu a}
 +(\mathbb Q^{\rm ext}_{E,\nu a}
 \log\boldsymbol\varpi_{\Psi,E,\nu})\\
&+\tau_E\mathbb Q^{\rm tot}_{E,\nu a}W_{\Psi,E,\nu}
+\tau_E\upsilon_E
\left\langle\widehat\jmath_{E,\nu},
\mathbb Q^{\rm int}_{E,\nu a}\widehat x_{E,\nu}
\right\rangle_{\rm ord}
 -\epsilon\mathbb Q^{\rm tot}_{E,\nu a}
 \mathscr Q_{\Psi,E,\nu}^{\rm W}\\
&+\mathbb Q^{\rm ext}_{E,\nu a}
 \log\mathfrak F_{E,\nu}^{\rm NK}.
\end{aligned}}
\tag{3D.129b}
$$

The intrinsic undamped Euclidean defect is the proved
\(\epsilon\downarrow0\) limit of the second expression.  The linear
source is inert; its nonlinear variation is the explicit composite
insertion in (3D.129b).  Define

$$
\boxed{
\mathcal W^{Q,\rm tot}_{R,\nu a}
:=\mathbb Q^{\rm ext}_{R,\nu a},
\qquad
\mathcal W^{Q,\rm tot}_{R,\nu a}
\widehat\jmath_{R,\nu,\mathsf r}=0.}
\tag{3D.130}
$$

No derivation on the ordinary linear-source algebra is inferred from
the nonlinear composite
\(\mathbb Q^{\rm int}\widehat x\).

The unnormalized and normalized Ward identities are

$$
\boxed{
\begin{aligned}
\mathcal W^{Q,\rm tot}_{R,\nu a}\mathcal Z_{\Psi,R,\nu}
&=\left[
\langle\mathfrak b^Q_{R,\nu a}\rangle_{\widehat\jmath}
+\langle\mathfrak C^{\rm cyc,Q}_{R,\nu a}\rangle
\right]\mathcal Z_{\Psi,R,\nu},\\
\mathcal W^{Q,\rm tot}_{R,\nu a}Z_{\Psi,R,\nu}
&=\left[
 \langle\mathfrak b^Q_{R,\nu a}\rangle_{\widehat\jmath}
 -\langle\mathfrak b^Q_{R,\nu a}\rangle_0
+\langle\mathfrak C^{\rm cyc,Q}_{R,\nu a}\rangle_{\widehat\jmath}
-\langle\mathfrak C^{\rm cyc,Q}_{R,\nu a}\rangle_0
 \right]Z_{\Psi,R,\nu}.
\end{aligned}}
\tag{3D.130a}
$$

Here \(\mathfrak b^Q\) denotes the relevant bulk expression in
(3D.129b), followed by its proved limit.  The cycle term is defined
only at expectation level by (3D.129a); the dotted identities are
identical.

Exact finite-cutoff supersymmetry is asserted only if

$$
\boxed{
[P_{R,\nu},\mathsf Q_{Ra}]=0,
\qquad
[P_{R,\nu},\bar{\mathsf Q}_{R\dot a}]=0,
\qquad
\mathfrak D^Q_{\Psi,R,\nu a}
=\widetilde{\mathfrak D}^Q_{\Psi,R,\nu\dot a}=0,
\qquad
\mathfrak b^Q_{R,\nu a}
=\widetilde{\mathfrak b}^Q_{R,\nu\dot a}=0,
\qquad
\langle\mathfrak C^{\rm cyc,Q}_{R,\nu a}\rangle
=\langle\widetilde{\mathfrak C}^{\rm cyc,Q}_{R,\nu\dot a}\rangle
=0.}
\tag{3D.131}
$$

On the untruncated local algebra,

$$
\boxed{
\begin{gathered}
\{\mathbf s_R,\mathsf Q_{Ra}\}=0,
\qquad
\{\mathbf s_R,\bar{\mathsf Q}_{R\dot a}\}=0,\\
[\delta_{R,\mathrm B},\mathsf Q_{Ra}]=0,
\qquad
[\delta_{R,\mathrm B},\bar{\mathsf Q}_{R\dot a}]=0,\\
\{\mathbf s_{\mathrm{sp},R},\mathsf Q_{Ra}\}=0,
\qquad
\{\mathbf s_{\mathrm{sp},R},\bar{\mathsf Q}_{R\dot a}\}=0.
\end{gathered}}
\tag{3D.132}
$$

Here \(\delta_{R,\mathrm B}\) is the infinitesimal untruncated
background transformation obtained from (3D.81).  At finite cutoff
put every operator on the same integrated--external--source algebra:

$$
\boxed{
\begin{aligned}
\mathbf s_{R,\nu}^{\rm int}
&:=\pi^{\rm int}_{\Psi,R,\nu}\mathbf s_R
\iota^{\rm int}_{\Psi,R,\nu},\\
\mathbf s_{R,\nu}^{\rm all}
&:=\mathbf s_{R,\nu}^{\rm int},
\qquad
\mathbf s_{R,\nu}^{\rm all}\widehat\jmath=0,\\
\mathbb Q_{R,\nu a}^{\rm all}
&:=\mathbb Q_{R,\nu a}^{\rm int}
+\mathbb Q_{R,\nu a}^{\rm ext},
\qquad
\mathbb Q_{R,\nu a}^{\rm all}\widehat\jmath=0,\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm all}
&:=\mathbf s_{\mathrm{sp},R,\nu}^{\rm int}
+\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext},
\qquad
\mathbf s_{\mathrm{sp},R,\nu}^{\rm all}\widehat\jmath=0.
\end{aligned}}
\tag{3D.132c}
$$

The zero source components in (3D.132c) are definitions.  For a
nonlinear residual vector \(X(x)\), the term
\(\langle\widehat\jmath,X(\widehat x)\rangle_{\rm ord}\) remains a
composite insertion, as in (3D.105) and (3D.129b); it is never
replaced by a derivation on the ordinary linear-source algebra.

The residual split lift is the adapted cotangent lift written in
(3D.132b).  Retain the three independent compatibility defects

$$
\boxed{
\mathfrak C^{sQ}_{R,\nu a}
:=\{\mathbf s_{R,\nu}^{\rm all},
\mathbb Q^{\rm all}_{R,\nu a}\},
\qquad
\mathfrak C^{BQ}_{R,\nu a}
:=[\mathbb W_{R,\mathrm B,\nu}^{\rm all},
\mathbb Q^{\rm all}_{R,\nu a}],
\qquad
\mathfrak C^{{\rm sp}Q}_{R,\nu a}
:=\{\mathbf s_{\mathrm{sp},R,\nu}^{\rm all},
\mathbb Q^{\rm all}_{R,\nu a}\}.}
\tag{3D.132a}
$$

The dotted defects are defined identically.

$$
\boxed{
\begin{aligned}
\widehat{\mathcal K}_{\Psi,R,\nu,\underline\imath}
^{\perp\mathsf r}
&:=\mu^{-[x^{\mathsf r}]}
\mathcal K_{\Psi,R,\nu,\underline\imath}^{\perp\mathsf r},\\
H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad}
&:=\sum_{\underline\imath}
(-1)^{\epsilon_{\overline Q^{\underline\imath}}}
\overline Q^{\star{\rm ext},{\rm ad}}_{R,\underline\imath}
\Omega_R^{\underline\imath}
-\sum_{\mathsf r}
(-1)^{\epsilon_{x^{\mathsf r}}}
\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}}
\widehat{\mathcal K}_{\Psi,R,\nu,\underline\imath}
^{\perp\mathsf r}\Omega_R^{\underline\imath},\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm int}
&:=-\widehat{\mathcal K}_{\Psi,R,\nu,\underline\imath}
^{\perp\mathsf r}\Omega_R^{\underline\imath}
\frac{\vec\partial}{\partial\widehat x^{\mathsf r}},\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}\overline Q_R^{\underline\imath}
&=\Omega_R^{\underline\imath},
\qquad
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}\Omega_R^{\underline\imath}=0,\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}
\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}}
&:=(H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad},
\widehat Q_{R,\nu,\mathsf r}^{\star{\rm ext}})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad}
\frac{\overleftarrow\partial}{\partial\widehat x^{\mathsf r}},\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}
\overline Q^{\star{\rm ext},{\rm ad}}_{R,\underline\imath}
&:=(H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad},
\overline Q^{\star{\rm ext},{\rm ad}}_{R,\underline\imath})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad}
\frac{\overleftarrow\partial}
{\partial\overline Q_R^{\underline\imath}},\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}
\Omega^\star_{R,\underline\imath}
&:=(H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad},
\Omega^\star_{R,\underline\imath})
_{\Psi,R,\nu}^{\rm ad,ext}
=H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad}
\frac{\overleftarrow\partial}{\partial\Omega_R^{\underline\imath}},\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm int}
+\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}
&=(H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad},\,\cdot\,)
_{\Psi,R,\nu}^{\rm ad,ext},
\qquad
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext}
\widehat Q_{R,\nu,\lambda}^{\star{\rm ext}}=0.
\end{aligned}}
\tag{3D.132b}
$$

They vanish only after closure of the paired regulator, density,
cycle, gauge fermion, and determinant sector has been proved.

### 3D.13 Notation and source ledger

$$
\boxed{
\begin{array}{c|l}
\text{symbol}&\text{unique role}\\ \hline
s_R&\text{Step-3B chiral-coordinate coefficient; never BRST}\\
\mathbf s_R,\mathbf s_{R,\nu}&\text{untruncated and projected gauge BRST differentials}\\
\mathbf s_{\mathrm{sp},R}&\text{background-split differential}\\
\mathsf C,\mathsf V,\mathsf A&\text{Step-3C gauge frames only}\\
\mathfrak A&\text{Step-3C collective superspace index only}\\
\mathsf p,\mathsf q&\text{finite physical-field coefficient indices}\\
\mathsf i,\mathsf j&\text{finite full-BV coefficient indices}\\
\mathsf r,\mathsf s&\text{integrated residual-transverse coefficient indices}\\
\lambda,\rho&\text{homogeneous adapted normal-coordinate indices; their coordinates are fixed to zero}\\
\alpha&\text{normal-slot map preserving all homogeneous gradings}\\
\mathfrak p,\mathfrak q&\text{untruncated physical-field DeWitt indices}\\
\mathfrak i,\mathfrak j&\text{untruncated full-BV DeWitt indices}\\
\mathfrak a,\mathfrak b&\text{quantum-split coefficient indices}\\
\underline\imath,\underline\jmath&\text{background coefficient indices}\\
\mathfrak X_R&\text{compact spacetime cutoff domain}\\
\mathfrak w_R^{\rm ctr}&\text{real contour-parameter embedding for the paired regulator}\\
\mathscr P_{R,\nu}^{\bar0},\mathscr P_{R,\nu}^{\bar1}
&\text{even and odd physical coefficient sets}\\
\beta,\chi&\text{background and quantum blockwise slot bijections}\\
\mathcal V_R&\text{gauge-prepotential bridge exponent}\\
\mathcal V_{R,\mathrm q}&\text{background-split quantum prepotential}\\
\mathcal E_R=e^{\mathcal V_R}&\text{relative gauge bridge}\\
\mathcal F_R&\text{background-covariant gauge-condition pair}\\
\mathcal F_{\Psi,R}&\text{gauge condition extracted from a general gauge fermion}\\
\mathscr R_R^{\rm g}&\text{untruncated infinitesimal gauge-orbit map}\\
\mathscr G_{\Psi,R,\nu},\mathscr F_{\Psi,R,\nu}
&\text{finite gauge-parameter and gauge-condition spaces}\\
\mathcal M_{\Psi,R,\nu}^{\rm FP},\mathscr H_{\Psi,R,\nu}
&\text{general-gauge FP map and its kernel}\\
F_R^I,\widetilde F_{R,I}&\text{chiral-multiplet auxiliary fields only}\\
\mathfrak c_R,\widetilde{\mathfrak c}_R&\text{minimal gauge ghosts}\\
\mathfrak c'_R,\mathfrak n_R&\text{antighost and multiplier doublets}\\
\mathfrak c_R^{\rm pair}&\text{ordered chiral/antichiral ghost pair}\\
\mathfrak c_{{\rm FP},R,\nu}^{\perp}
&\text{residual-free FP ghost coefficient coordinate}\\
\mathscr R_{\rm nm}^{\rm base},\mathscr R_{\rm NK}^{\rm BV},\mathscr R_{\rm ag}
&\text{base, admitted BV--NK, and antighost index sets}\\
\mathcal M_R^{\rm FP},\mathscr H_{R,\nu}
&\text{standard-gauge FP operator and residual kernel}\\
\mathcal I_{R,\nu}^{\perp}
&\text{chosen reference isomorphism from gauge to condition space}\\
\mathfrak e_R^{\rm QME}&\text{Lorentzian/Euclidean QME phase}\\
W_{\min,R,\nu},W_{\rm nm,R,\nu},W_{\rm ext,R,\nu}
&\text{minimal, stabilized, and background-extended quantum actions}\\
W_{\Psi,R,\nu}&\text{exact gauge-fixed restriction of }W_{\rm ext,R,\nu}\\
\mathfrak C_{\rm ext,R,\nu}^{(0)}
&\text{finite-cutoff order-zero extended CME defect}\\
M_\nu^{\rm W}&\text{Lorentz--Euclidean coefficient map}\\
M_{\nu,\rm int}^{\rm W,\perp},M_{\nu,\rm ext}^{\rm W}
&\text{integrated residual-free and external Wick blocks}\\
M_{\zeta,\nu}^{\rm W},M_{\nu,\rm nor}^{\rm W}
&\text{ambient split-coordinate and adapted normal Wick blocks}\\
\mathscr T_R^{\mathsf C\to\mathsf V}&\text{gauge-chiral to gauge-vector coordinate map}\\
\mathbb T_{\rm tot},\mathbb T_{\rm B},\mathbb T_{\rm q}
&\text{total, background, and split-quantum frame maps}\\
\mathbb T_{R,\nu}&\text{full residual-free finite frame map}\\
\widehat{\mathbb T}_{R,\nu}^{\perp},J_{\mathbb T,R,\nu}^{\perp}
&\text{residual coordinate frame map and its ordered Jacobian}\\
\widehat{\mathbb T}_{R,\nu}^{\rm nor},J_{\mathbb T,R,\nu}^{\rm nor}
&\text{compatible normal frame map and its invertible Jacobian}\\
\mathbb T_{R,\nu}^{\rm ext}&\text{external background-pair frame map}\\
\widehat{\mathbb T}_{\rm all,R,\nu}
&\text{ambient BV cotangent frame lift}\\
\widehat{\mathbb T}_{\rm src,\Psi,R,\nu}
&\text{affine gauge-fixed external-source frame lift}\\
X^\star&\text{BV antifield}\\
X^{\star{\rm ext}}&\text{external Zinn--Justin antifield source}\\
\widehat X^\star,\widehat X^{\star{\rm ext}}
&\text{dimensionless Darboux antifield coordinates}\\
\overline Q^{\star{\rm amb}},
\overline Q^{\star{\rm BV},{\rm ad}},
\overline Q^{\star{\rm ext},{\rm ad}}
&\text{ambient, BV-adapted, and external-source-adapted background duals}\\
\widehat Q_\lambda^{\star\bullet},\widehat\jmath_\lambda
&\text{normal antifield coordinate and identically zero normal source}\\
\boldsymbol\varpi_{R,\nu}&\text{physical cylindrical density}\\
\widehat{\boldsymbol\varpi}_{R,\nu}&\text{BV Darboux density}\\
\widehat{\boldsymbol\varpi}_{\rm nm,R,\nu}
&\text{non-minimal stabilized BV density}\\
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}
&\text{background-extended BV density}\\
\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\rm ad}
&\text{full tubular-cotangent pushforward of the extended BV density}\\
\boldsymbol\varpi_{\Psi,R,\nu}&\text{gauge-fixed Lagrangian density}\\
\mathscr J_R^{\rm phys}&\text{physical superfield source pairing}\\
\mathscr J_{R,\nu}^{\rm src}&\text{integrated BV-source exponent pairing}\\
\widehat\jmath_{R,\nu}&\text{integrated residual-slice coefficient source}\\
\jmath_{R,\nu}&\text{dimensionful source dual to }x_{R,\nu}\\
\mathscr J_{R,\nu}^{\rm coll}&\text{ordered collective source pairing}\\
\mathscr E_{\Psi,R,\nu}&\text{complete regulated gauge-fixed exponent}\\
\mathcal Z_{\Psi,R,\nu}&\text{unnormalized gauge-fixed functional}\\
Z_{\Psi,R,\nu}&\text{normalized gauge-fixed functional}\\
\mathscr W_{c,R,\nu}&\text{connected generator}\\
\mathscr W_{R,\nu}^{\rm u},\mathscr V_{R,\nu}
&\text{unnormalized connected generator and vacuum normalization}\\
\widehat{\mathcal Q}_{\rm mean},\mathcal Q_{\rm mean}
&\text{dimensionless and reconstructed dimensionful mean coefficients}\\
\mathscr S_{R,\nu}^{\rm 1PI}&\text{action-like one-particle-irreducible effective action}\\
\mathscr S_{R,\nu}^{\rm 1PI,u}&\text{unnormalized partial Legendre transform}\\
(-,-)_{\rm 1PI,int,R,\nu}&\text{integrated-field induced 1PI antibracket}\\
\mathfrak O_{R,\nu}^{\rm 1PI,u}
&\text{Legendre image of the regulated BV breaking}\\
\Delta_{\Psi,R,\nu}^{\rm tan},\mathfrak D_{R,\nu}^{\rm BV},
\mathfrak S_{R,\nu}^{\rm tan}
&\text{tangent BV divergence, projection mismatch, and flux}\\
\mathfrak B_{R,\nu}^{\rm BV}
&\text{complete gauge-fixed BV breaking insertion}\\
\mathfrak R_{R,\nu}^{\rm ZJ},\mathfrak C_{R,\nu}^{\rm ZJ}
&\text{external-antifield response and moving-cycle flux}\\
\overline Q_R,\zeta_R,\Omega_R&\text{background, quantum, and background-partner coordinates}\\
\mathbb J_R,L_R,B_R&\text{split Jacobian, inverse, and background derivative}\\
\mathcal K_{R,\underline\imath}^{\mathfrak a}&\text{exact split connection}\\
\mathbb I_{\Psi,R,\nu},\mathbb P_{\Psi,R,\nu}
&\text{residual-slice tangent inclusion and left inverse}\\
\kappa_{\Psi,R,\nu},\widehat\kappa_{\Psi,R,\nu}^{\rm tub}
&\text{residual embedding and its source-independent tubular completion}\\
\mathbb I_{\Psi,R,\nu}^{\rm tub},\mathbb P_{\Psi,R,\nu}^{\rm tub}
&\text{full off-slice tangent Jacobian and inverse row}\\
\widehat{\mathbb N}_{\Psi,R,\nu},\widehat{\mathbb R}_{\Psi,R,\nu}
&\text{adapted normal inclusion and inverse row}\\
\mathscr D_{\rm ad}^{\bullet},(-,-)_{\Psi,R,\nu}^{\rm ad,\bullet}
&\text{full adapted Darboux pairs and their ordered antibracket}\\
T_{\Psi,R,\nu}^{{\rm tub},\bullet}
&\text{full tubular field-cotangent canonical map}\\
\Psi_R^{\rm ad}
&\text{gauge fermion expressed in the full tubular coordinates}\\
\Pi_{\Psi,R,\nu},\mathfrak G_R^{\rm sp}
&\text{tangent projector and moving-slice split-tangent gauge family}\\
\mathcal K_{\Psi,R,\nu}^{\perp},\mathfrak N_{\Psi,R,\nu}
&\text{relative tangent split connection and normal projection defect}\\
\mathcal K_{\Psi,R,\nu}^{\rm rel}
&\text{ambient split connection plus the moving-embedding derivative}\\
\mathfrak K_{\Psi,R,\nu}^{\rm ins,u},
\mathfrak K_{\Psi,R,\nu}^{\rm ins,n}
&\text{unnormalized and normalized split-connection insertion operators}\\
\mathcal V_{A,R,\nu},X_{A,R,\nu},\mathfrak N_{A,R,\nu}
&\text{relative ambient vector, residual vector, and normal defect for symmetry }A\\
\mathcal V_{\Psi,R,\nu}^{Q},\mathcal X_{\Psi,R,\nu}^{Q}
&\text{relative ambient and integrated residual supercharge vectors}\\
\Xi_{R,\nu}^{\rm NK}&\text{conditional Nielsen--Kallosh determinant coordinates}\\
\vartheta_{R,\nu}^{\rm NK},d\mu_{\Psi,{\rm NK},R,\nu}^{\rm BV}
&\text{BV--NK coordinate bijection and reference-normalized graph measure}\\
\mathcal I_{{\rm NK},0,R,\nu},D_{\prec_\nu,\succ_\nu}^{\rm NK}
&\text{nonzero BV--NK reference integral and graded ordered coordinate measure}\\
\mathfrak F_{R,\nu}^{\rm FP},\mathfrak F_{R,\nu}^{\rm NK,req},
\mathfrak F_{R,\nu}^{\rm NK},\mathfrak F_{R,\nu}^{\rm NK,aux}
&\text{finite FP, required NK, selected external NK, and auxiliary factors}\\
\mathfrak b_{R,\nu}^{\rm gf},\mathfrak C_{R,\nu}^{\rm gf}
&\text{gauge-fermion bulk derivative and moving-cycle flux}\\
M_{\star{\rm ext}}^{\rm W}
&\text{external-antifield Wick cotangent block}\\
\mathbb Q_{R,\nu}^{\rm int},\mathbb Q_{R,\nu}^{\rm ext},
\mathbb Q_{R,\nu}^{\rm tot}
&\text{integrated, external, and total supercharge vector fields}\\
\mathbb Q_{R,\nu}^{\rm all},\mathbb W_{R,\mathrm B,\nu}^{\rm all}
&\text{common-algebra supercharge and background lifts}\\
H_{\Psi,R,\nu}^{Q,{\rm ad}}
&\text{full adapted supercharge cotangent Hamiltonian}\\
\mathcal W_{R,\nu}^{Q,\rm tot}
&\text{external-argument supercharge Ward operator with inert linear source}\\
\widehat\jmath_{R,\nu}\text{ under nonlinear residual symmetries}
&\text{inert linear source; every nonlinear variation is an explicit insertion}\\
\mathbf s_{R,\nu}^{\rm int},\mathbf s_{R,\nu}^{\rm all}
&\text{integrated and common-algebra gauge-BRST lifts}\\
\mathbf s_{\mathrm{sp},R,\nu}^{\rm int},
\mathbf s_{\mathrm{sp},R,\nu}^{\rm ext},
\mathbf s_{\mathrm{sp},R,\nu}^{\rm all}
&\text{adapted integrated, cotangent, and common-algebra split lifts}\\
H_{\mathrm{sp},\Psi,R,\nu}^{\rm ad}
&\text{adapted residual split Hamiltonian}\\
\mathfrak D^Q_{\Psi,R,\nu}&\text{supercharge normal projection defect}\\
\mathfrak b^Q_{R,\nu},\mathfrak C^{\rm cyc,Q}_{R,\nu}
&\text{bulk supersymmetry defect and expectation-level cycle flux}\\
\mathfrak D_{\Psi,E,\nu}^{\rm cyc}
&\text{intrinsic-Euclidean versus Wick-image cycle defect}
\end{array}}
\tag{3D.133}
$$

No Weinberg or Srednicki formula, symbol, sign, normalization, path
integral, ghost rule, or BV rule is used in this contract.  No new
Project--Srednicki--Weinberg dictionary row is admitted.  No Notion,
web, external book, local note, or attachment is a calculation input.

The acceptance predicate is

$$
\boxed{
\begin{gathered}
\text{the 222 tags, consisting of (3D.1)--(3D.134) and 88 suffixed
 tags, occur exactly once},\\
\text{every field, source, antifield, density, differential, index,
 cycle, parity, ghost number, and dimension resolves uniquely},\\
\text{(3D.31), (3D.34), (3D.45)--(3D.48a), (3D.57), (3D.60),
 (3D.62)--(3D.69), and (3D.73) hold exactly},\\
\text{(3D.78c), (3D.90)--(3D.97c), (3D.100)--(3D.106b),
 (3D.107)--(3D.112), and (3D.117)--(3D.124d) hold exactly},\\
\text{(3D.127)--(3D.132c), including (3D.127a), (3D.128c),
 (3D.128d),
 (3D.105d1), and (3D.105k), retain every nonzero regulator, density,
 cycle, split, BRST, and supersymmetry defect},\\
P0=P1=0.
\end{gathered}}
\tag{3D.134}
$$
