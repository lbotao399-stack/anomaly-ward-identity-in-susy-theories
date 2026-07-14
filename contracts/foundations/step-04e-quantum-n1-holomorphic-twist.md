# 00 3+1d SUSY QFT — Convention Lock

## Step 4E. Quantum holomorphic twist of Euclidean pure \(\mathcal N=1\) gauge theory

### Abstract

This contract separates three statements:

1. a finite-regulator theorem for a quantum gauge-plus-\(Q\) BV semidensity;
2. comparison with an independently renormalized holomorphic-BF theory;
3. removal of the regulator and comparison of observables.

At fixed finite regulator, an odd-symplectic pullback followed by normalized
BV pushforward is an exact graded chain map for the canonical semidensity BV
operator.  Therefore it transports the quantum master equation to every
power of \(\hbar\).  This proves the commutation of twist and quantization
only when the holomorphic theory is defined by that pushforward.  Comparison
with an independently chosen holomorphic-BF quantization is an even
cohomological matching problem.  Existence of the ordinary
quantum \(Q\)-lift and existence of an independent holomorphic-BF
quantization are odd obstruction problems.  At finite regulator the
comparison and QME classes lie in \(H^{\bar0}\) and \(H^{\bar1}\).
They refine to \(H^0_{\mathrm{loc}}\) and \(H^1_{\mathrm{loc}}\) only after
an integer grading, locality, and regulator removal have been proved.  The
finite interacting regulator, quantum \(Q\)-lift, RG-compatible continuum
limit, vertical contour, source map, \(U(1)_R\)-equivariance, and global
Euclidean integration cycle are not constructed here.

### Final Result List

$$
\boxed{
\begin{gathered}
\boldsymbol\Delta_{Y,\nu}\mathscr T_{\nu,1/2}^*
=\mathscr T_{\nu,1/2}^*\boldsymbol\Delta_{X,\nu},\\
\boldsymbol\Delta_{\mathrm h,\nu}\pi_{\nu*}^{\mathrm{BV}}
=(-1)^{p_\nu}\pi_{\nu*}^{\mathrm{BV}}\boldsymbol\Delta_{Y,\nu},\\
\mathscr K_\nu
:=\mathcal N_\nu(\hbar)^{-1}
\pi_{\nu*}^{\mathrm{BV}}\mathscr T_{\nu,1/2}^*,
\qquad
\boldsymbol\Delta_{\mathrm h,\nu}\mathscr K_\nu
=(-1)^{p_\nu}\mathscr K_\nu\boldsymbol\Delta_{X,\nu},\\
\boldsymbol\Delta_{X,\nu}\Sigma_{X,\nu}=0
\quad\Longrightarrow\quad
\boldsymbol\Delta_{\mathrm h,\nu}\mathscr K_\nu\Sigma_{X,\nu}=0.
\end{gathered}}
\tag{4E.1}
$$

The theorem proved below is

$$
\boxed{
\operatorname{Quant}_{\mathrm{pf}}
\circ\operatorname{HT}
=
\operatorname{HT}_{\mathrm{BV\ pushforward}}
\circ\operatorname{Quant}
\quad
\text{at fixed }\nu,}
\tag{4E.2}
$$

where the left-hand quantization is defined by the right-hand pushforward.
The following stronger equations are not proved:

$$
\boxed{
\operatorname{Quant}_{\mathrm{ind}}\circ\operatorname{HT}
=
\operatorname{HT}\circ\operatorname{Quant},
\qquad
\exists\,\mathscr K_\infty
:=\lim_{\nu\to\infty}\mathscr K_\nu
\text{ on a common local domain},
\qquad
Z_{\mathcal N=1}^{E}=Z_{\mathrm{hBF}}.}
\tag{4E.3}
$$

### 4E.1 Symbols, operators, and cohomological degrees

For every regulator label \(\nu\), define

$$
\begin{gathered}
X_\nu:=\mathcal F_{\mathrm{ord},\nu}^{\mathrm{BV}},
\qquad
Y_\nu:=\mathcal F_{\mathrm h,\nu}^{\mathrm{BV}}
\times\mathcal F_{\mathrm{ctr},\nu}^{\mathrm{BV}},\\
\pi_\nu:Y_\nu\longrightarrow\mathcal F_{\mathrm h,\nu}^{\mathrm{BV}},
\qquad
\mathscr T_\nu:Y_\nu\longrightarrow X_\nu,\\
\mathscr T_\nu^*\omega_{X,\nu}
=\omega_{Y,\nu}
=\omega_{\mathrm h,\nu}\oplus\omega_{\mathrm{ctr},\nu}.
\end{gathered}
\tag{4E.4}
$$

Here \(\mathscr T_\nu\) is the regulated new-to-old map of Step 4D.
It is assumed to be an invertible odd-symplectic superdiffeomorphism, so
\(d\mathscr T_\nu\) is invertible at every point.  The symbols
\(\operatorname{Quant}_{\mathrm{pf}}\), \(\operatorname{Quant}_{\mathrm{ind}}\),
and \(\operatorname{HT}\) in (4E.2)--(4E.3) are labels for the
semidensity constructions (4E.18)--(4E.20), not additional maps.
The partition symbols in (4E.3) are schematic names for unconstructed
global Euclidean integrals, not defined quantities in this contract.
Let \(\rho_{Z,\nu}\) be a nowhere-vanishing even density on
$$
Z_\nu\in
\left\{
X_\nu,Y_\nu,
\mathcal F_{\mathrm h,\nu}^{\mathrm{BV}},
\mathcal F_{\mathrm{ctr},\nu}^{\mathrm{BV}}
\right\}.
$$
For a function \(F\), its Hamiltonian vector field and function BV
Laplacian are

$$
\iota_{X_F}\omega_{Z,\nu}=dF,
\qquad
\Delta_{\rho_{Z,\nu}}F
:=\frac12\operatorname{div}_{\rho_{Z,\nu}}X_F.
\tag{4E.5}
$$

The Hamiltonian-action convention is
\(X_F(G):=(G,F)_{Z,\nu}\).  This fixes the bracket order in every
density-change formula below.  The symbol
\(\epsilon(F)\in\mathbb Z_2\) denotes parity.  In (4E.11)--(4E.17),
\((\cdot,\cdot)_\nu:=(\cdot,\cdot)_{X,\nu}\).

The canonical semidensity BV operator is denoted
\(\boldsymbol\Delta_{Z,\nu}\), with
\(\boldsymbol\Delta_{Z,\nu}^2=0\).  A density is compatible when

$$
\boldsymbol\Delta_{Z,\nu}\rho_{Z,\nu}^{1/2}=0,
\qquad
\boldsymbol\Delta_{Z,\nu}
\left(\rho_{Z,\nu}^{1/2}F\right)
=\rho_{Z,\nu}^{1/2}\Delta_{\rho_{Z,\nu}}F,
\qquad
\Delta_{\rho_{Z,\nu}}^2=0.
\tag{4E.6}
$$

For the compatible input and horizontal densities, abbreviate

$$
\Delta_{X,\nu}:=\Delta_{\rho_{X,\nu}},
\qquad
\Delta_{\mathrm h,\nu}:=\Delta_{\rho_{\mathrm h,\nu}}.
$$

For an arbitrary density define

$$
\chi_{\rho_{Z,\nu}}
:=\rho_{Z,\nu}^{-1/2}
\boldsymbol\Delta_{Z,\nu}\rho_{Z,\nu}^{1/2}.
$$

Then the complete conversion formula is

$$
\boldsymbol\Delta_{Z,\nu}
\left(\rho_{Z,\nu}^{1/2}F\right)
=\rho_{Z,\nu}^{1/2}
\left(\Delta_{\rho_{Z,\nu}}F+\chi_{\rho_{Z,\nu}}F\right).
$$

Thus (4E.6), and not only nonvanishing of \(\rho_{Z,\nu}\), is required
for the standard function QME.  Set

$$
\mathscr O_{Z,\nu}:=\operatorname{Fun}(Z_\nu),
\qquad
\mathscr O_{Z,\nu}[[\hbar]]
:=\operatorname{Fun}(Z_\nu)\otimes\mathbb C[[\hbar]].
$$

Set

$$
\mathbb K:=\mathbb C((\hbar^{1/2})),
$$

and define the formal WKB semidensity space

$$
\mathscr S_{Z,\nu}^{\mathrm{WKB}}
:=
\operatorname{Span}_{\mathbb K}\left\{
\rho_{Z,\nu}^{1/2}e^{-S/\hbar}A(\hbar):
\begin{array}{l}
S\in\mathscr O_{Z,\nu}^{\bar0},\\
A(\hbar)\in
\mathscr O_{Z,\nu}\widehat\otimes\mathbb K
\end{array}
\right\}.
$$

The canonical operator acts
\(\boldsymbol\Delta_{Z,\nu}:
\mathscr S_{Z,\nu}^{\mathrm{WKB}}
\to\mathscr S_{Z,\nu}^{\mathrm{WKB}}\).
Pullbacks and pushforwards below are maps between explicitly declared
subdomains of these WKB semidensity spaces.

The coefficient type of the pullback is recorded in its second subscript:

$$
\mathscr T_{\nu,0}^*:
\mathscr O_{X,\nu}\longrightarrow\mathscr O_{Y,\nu},
\qquad
\mathscr T_{\nu,1/2}^*:
\mathscr S_{X,\nu}^{\mathrm{WKB}}\longrightarrow
\mathscr S_{Y,\nu}^{\mathrm{WKB}},
\qquad
\mathscr T_{\nu,1}^*:
\operatorname{Dens}(X_\nu)\longrightarrow
\operatorname{Dens}(Y_\nu).
$$

Here \(\operatorname{Dens}(Z_\nu)\) denotes the module of densities on
\(Z_\nu\).

The unsubscripted \(\mathscr T_\nu^*\) is reserved for the ordinary
geometric pullback of differential forms.  In particular, it is used for
\(\omega_{X,\nu}\), \(df\), and
\(\iota_{X_f}\omega_{X,\nu}\), but not for functions, densities, or
semidensities.

When an integer twisted grading is used, the additional hypotheses are

$$
\deg_{\mathrm{HT}}\hbar=0,
\qquad
\deg_{\mathrm{HT}}(F,G)=
\deg_{\mathrm{HT}}F+\deg_{\mathrm{HT}}G+1,
\qquad
\deg_{\mathrm{HT}}\boldsymbol\Delta_{Z,\nu}=1,
\qquad
\deg_{\mathrm{HT}}\rho_{Z,\nu}=0,
$$

$$
\deg_{\mathrm{HT}}S_n
=\deg_{\mathrm{HT}}H_{Q,n,\nu}=0,
\qquad
\deg_{\mathrm{HT}}d_0
=\deg_{\mathrm{HT}}d_{\mathrm{tw},0,\nu}=1.
$$

Without these hypotheses all finite-regulator obstruction groups below are
only \(\mathbb Z_2\)-graded.

In (4E.7)--(4E.10) only, the labels \(Z,\nu,\rho\) are suppressed:
\(\Delta=\Delta_{\rho_{Z,\nu}}\) and
\(\boldsymbol\Delta=\boldsymbol\Delta_{Z,\nu}\).

The bracket and Laplacian conventions are exactly

$$
\begin{aligned}
\Delta_\rho(FG)
&=(\Delta_\rho F)G
+(-1)^{\epsilon_F}F\Delta_\rho G
+(-1)^{\epsilon_F}(F,G),\\
\Delta_\rho e^{-W/\hbar}
&=\left[
-\hbar^{-1}\Delta_\rho W
+\frac12\hbar^{-2}(W,W)
\right]e^{-W/\hbar}.
\end{aligned}
\tag{4E.7}
$$

For

$$
\Sigma_W:=\rho^{1/2}e^{-W/\hbar},
\qquad
W=\sum_{n\geq0}\hbar^nS_n,
\tag{4E.8}
$$

the semidensity QME and function QME are equivalent:

$$
\boxed{
\boldsymbol\Delta\Sigma_W=0
\quad\Longleftrightarrow\quad
\frac12(W,W)-\hbar\Delta_\rho W=0.}
\tag{4E.9}
$$

Set \(d_0:=(S_0,\cdot)\) and
\(\mathfrak M_\rho(W):=\frac12(W,W)-\hbar\Delta_\rho W\).
The coefficient of \(\hbar^0\) in (4E.9) gives

$$
\frac12(S_0,S_0)=0,
\qquad
d_0^{\,2}F
=(S_0,(S_0,F))
=\frac12((S_0,S_0),F)=0.
$$

For \(n\geq1\), the coefficient equation is

$$
\boxed{
d_0S_n
=\Delta_\rho S_{n-1}
-\frac12\sum_{r=1}^{n-1}(S_r,S_{n-r}),
\qquad n\geq1,}
\tag{4E.10}
$$

where \(S_{-1}:=0\).  Its right-hand side is odd, but it defines an
obstruction class only after closedness is proved.  Define

$$
\mathfrak o_{n,\rho}
:=\Delta_\rho S_{n-1}
-\frac12\sum_{r=1}^{n-1}(S_r,S_{n-r}),
\qquad
W_{<n}:=\sum_{r=0}^{n-1}\hbar^rS_r.
$$

Assume (4E.10) through order \(n-1\).  Direct coefficient extraction gives

$$
[\hbar^r]\mathfrak M_\rho(W_{<n})=0
\quad(0\leq r<n),
\qquad
[\hbar^n]\mathfrak M_\rho(W_{<n})=-\mathfrak o_{n,\rho}.
$$

The Bianchi identity expanded in 4E.2 gives

$$
\begin{aligned}
0
&=[\hbar^n]\left[
(W_{<n},\mathfrak M_\rho(W_{<n}))
-\hbar\Delta_\rho\mathfrak M_\rho(W_{<n})
\right]\\
&=(S_0,-\mathfrak o_{n,\rho})
=-d_0\mathfrak o_{n,\rho}.
\end{aligned}
$$

Hence
\([\mathfrak o_{n,\rho}]
\in H^{\bar1}(\mathscr O_{Z,\nu},d_0)\).  When the integer grading above
is preserved, it has degree \(1\) and lies in
\(H^1(\mathscr O_{Z,\nu},d_0)\).  Local cohomology modulo spacetime
derivatives is not asserted at finite regulator.

### 4E.2 The quantum \(Q\)-Hamiltonian

Write the ordinary quantum BV master action and the quantum Hamiltonian of
the twisting supercharge as

$$
W_{\mathrm{ord},\nu}
=S_{\mathrm{ord},0,\nu}
+\sum_{n\geq1}\hbar^nM_{n,\nu},
\qquad
\widehat H_{Q,\nu}
=\sum_{n\geq0}\hbar^nH_{Q,n,\nu}.
\tag{4E.11}
$$

The classical term is tied to Step 4D rather than introduced abstractly:

$$
\boxed{
H_{Q,0,\nu}
=S_{\mathrm{tw},0,\nu}-S_{\mathrm{ord},0,\nu}
=\sum_\Phi(-1)^{\epsilon_\Phi}
\int d^4x_E\,
\operatorname{tr}_\kappa\left(\Phi^*Q\Phi\right)_\nu.}
\tag{4E.11a}
$$

Assume first that the ordinary action already satisfies

$$
\frac12(W_{\mathrm{ord},\nu},W_{\mathrm{ord},\nu})_\nu
-\hbar\Delta_{X,\nu}W_{\mathrm{ord},\nu}=0.
\tag{4E.12}
$$

The twisted action
\(W_{\mathrm{tw},\nu}:=W_{\mathrm{ord},\nu}+\widehat H_{Q,\nu}\)
satisfies the QME exactly when

$$
\boxed{
(W_{\mathrm{ord},\nu},\widehat H_{Q,\nu})_\nu
+\frac12(\widehat H_{Q,\nu},\widehat H_{Q,\nu})_\nu
-\hbar\Delta_{X,\nu}\widehat H_{Q,\nu}=0.}
\tag{4E.13}
$$

Define

$$
d_{\mathrm{tw},0,\nu}
:=(S_{\mathrm{ord},0,\nu}+H_{Q,0,\nu},\cdot)_\nu.
\tag{4E.14}
$$

The Step-4D twisted CME is an explicit nilpotency hypothesis:

$$
\frac12
(S_{\mathrm{ord},0,\nu}+H_{Q,0,\nu},
 S_{\mathrm{ord},0,\nu}+H_{Q,0,\nu})_\nu=0
\quad\Longrightarrow\quad
d_{\mathrm{tw},0,\nu}^{\,2}=0.
$$

The coefficient of \(\hbar^n\) in (4E.13), with every bracket term
retained, is

$$
\boxed{
\begin{aligned}
d_{\mathrm{tw},0,\nu}H_{Q,n,\nu}
={}&\Delta_{X,\nu}H_{Q,n-1,\nu}\\
&-\sum_{r=1}^{n}
(M_{r,\nu},H_{Q,n-r,\nu})_\nu\\
&-\frac12\sum_{r=1}^{n-1}
(H_{Q,r,\nu},H_{Q,n-r,\nu})_\nu,
\qquad n\geq1.
\end{aligned}}
\tag{4E.15}
$$

Define the right-hand side of (4E.15) by
\(\mathfrak o_{Q,n,\nu}\).  For an even action \(W\), set

$$
\mathfrak M_\nu(W)
:=\mathfrak M_{\rho_{X,\nu}}(W)
=\frac12(W,W)_\nu-\hbar\Delta_{X,\nu}W.
$$

The graded Jacobi identity, the BV derivation identity, and
\(\Delta_{X,\nu}^2=0\) give

$$
\Delta_{X,\nu}(W,W)_\nu
=(\Delta_{X,\nu}W,W)_\nu-(W,\Delta_{X,\nu}W)_\nu
=-2(W,\Delta_{X,\nu}W)_\nu.
$$

$$
\begin{aligned}
(W,\mathfrak M_\nu(W))_\nu
-\hbar\Delta_{X,\nu}\mathfrak M_\nu(W)
={}&-\hbar(W,\Delta_{X,\nu}W)_\nu\\
&-\frac{\hbar}{2}\Delta_{X,\nu}(W,W)_\nu
+\hbar^2\Delta_{X,\nu}^2W\\
={}&-\hbar(W,\Delta_{X,\nu}W)_\nu
+\hbar(W,\Delta_{X,\nu}W)_\nu
=0.
\end{aligned}
$$

If the ordinary QME holds through order \(n\), all relative equations below
order \(n\) hold, and the regulated complex preserves the displayed
grading, the coefficient of this identity gives

$$
d_{\mathrm{tw},0,\nu}\mathfrak o_{Q,n,\nu}=0.
$$

In particular,

$$
d_{\mathrm{tw},0,\nu}H_{Q,1,\nu}
=\Delta_{X,\nu}H_{Q,0,\nu}
-(M_{1,\nu},H_{Q,0,\nu})_\nu.
\tag{4E.16}
$$

Thus the first application-level obstruction is

$$
\boxed{
\left[
\Delta_{X,\nu}H_{Q,0,\nu}
-(M_{1,\nu},H_{Q,0,\nu})_\nu
\right]
\in H^{\bar1}
\left(\mathscr O_{X,\nu},d_{\mathrm{tw},0,\nu}\right).}
\tag{4E.17}
$$

If the integer twisted grading is preserved, the last group is
\(H^1(\mathscr O_{X,\nu},d_{\mathrm{tw},0,\nu})\).

No quantum \(Q\)-lift for the Project theory is asserted until all
equations (4E.15) are solved.

### 4E.3 The two compositions

The twist-after-quantization input is the regulated semidensity

$$
\Sigma_{X,\nu}^{Q}
:=\rho_{X,\nu}^{1/2}
\exp\left[
-\hbar^{-1}
\left(W_{\mathrm{ord},\nu}+\widehat H_{Q,\nu}\right)
\right].
\tag{4E.18}
$$

The pushforward-defined quantization-after-twist is

$$
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}}
:=\mathscr K_\nu\Sigma_{X,\nu}^{Q}.
\tag{4E.19}
$$

An independently renormalized holomorphic-BF quantization is separate data:

$$
\Sigma_{\mathrm h,\nu}^{\mathrm{ind}}
:=\rho_{\mathrm h,\nu}^{1/2}
\exp\left[
-\hbar^{-1}W_{\mathrm h,\nu}^{\mathrm{ind}}
\right],
\qquad
W_{\mathrm h,\nu}^{\mathrm{ind}}
=S_{\mathrm{hBF},\nu}
+\sum_{n\geq1}\hbar^nM_{n,\nu}^{\mathrm{ind}}.
\tag{4E.20}
$$

Equations (4E.19) and (4E.20) are not identified by definition.

### 4E.4 Odd-symplectic pullback

Let \(f\in C^\infty(X_\nu)\).  Since
\(\mathscr T_\nu^*\omega_{X,\nu}=\omega_{Y,\nu}\),

$$
\begin{aligned}
\iota_{X_{\mathscr T_{\nu,0}^*f}}\omega_{Y,\nu}
&=d(\mathscr T_{\nu,0}^*f)
=\mathscr T_\nu^*(df)\\
&=\mathscr T_\nu^*
(\iota_{X_f}\omega_{X,\nu})
=\iota_{(d\mathscr T_\nu)^{-1}X_f\circ\mathscr T_\nu}
\omega_{Y,\nu}.
\end{aligned}
\tag{4E.21}
$$

Nondegeneracy of \(\omega_{Y,\nu}\) gives

$$
d\mathscr T_\nu\,
X_{\mathscr T_{\nu,0}^*f}
=X_f\circ\mathscr T_\nu.
\tag{4E.22}
$$

Transport the density by
\(\rho_{Y,\nu}^{\mathrm{tr}}:=\mathscr T_{\nu,1}^*\rho_{X,\nu}\).
The defining Lie derivative of divergence gives

$$
\begin{aligned}
\mathcal L_{X_{\mathscr T_{\nu,0}^*f}}\rho_{Y,\nu}^{\mathrm{tr}}
&=\mathcal L_{X_{\mathscr T_{\nu,0}^*f}}
\mathscr T_{\nu,1}^*\rho_{X,\nu}\\
&=\mathscr T_{\nu,1}^*
\left(\mathcal L_{X_f}\rho_{X,\nu}\right)\\
&=\mathscr T_{\nu,1}^*
\left[
(\operatorname{div}_{\rho_{X,\nu}}X_f)\rho_{X,\nu}
\right]\\
&=
\left[
\mathscr T_{\nu,0}^*
(\operatorname{div}_{\rho_{X,\nu}}X_f)
\right]\rho_{Y,\nu}^{\mathrm{tr}}.
\end{aligned}
\tag{4E.23}
$$

Therefore

$$
\boxed{
\Delta_{\rho_{Y,\nu}^{\mathrm{tr}}}\mathscr T_{\nu,0}^*f
=\mathscr T_{\nu,0}^*\Delta_{\rho_{X,\nu}}f.}
\tag{4E.24}
$$

For canonical semidensities the same identity is density-free:

$$
\boxed{
\boldsymbol\Delta_{Y,\nu}\mathscr T_{\nu,1/2}^*
=\mathscr T_{\nu,1/2}^*\boldsymbol\Delta_{X,\nu}.}
\tag{4E.25}
$$

If a fixed reference density \(\rho_{Y,\nu}^{\mathrm{ref}}\) is used
instead of the transported density, define

$$
\mathscr T_{\nu,1/2}^*\rho_{X,\nu}^{1/2}
=J_{\mathscr T,\nu}^{1/2}
\left(\rho_{Y,\nu}^{\mathrm{ref}}\right)^{1/2},
\qquad
\ell_{\mathscr T,\nu}:=\log J_{\mathscr T,\nu}^{1/2}.
\tag{4E.26}
$$

The two function Laplacians then obey

$$
\Delta_{\rho_{Y,\nu}^{\mathrm{tr}}}F
=
\Delta_{\rho_{Y,\nu}^{\mathrm{ref}}}F
+(\ell_{\mathscr T,\nu},F)_{Y,\nu}.
$$

If both densities are compatible, then

$$
\begin{aligned}
0
&=\boldsymbol\Delta_{Y,\nu}
\left(\rho_{Y,\nu}^{\mathrm{tr}}\right)^{1/2}\\
&=\boldsymbol\Delta_{Y,\nu}
\left[
e^{\ell_{\mathscr T,\nu}}
\left(\rho_{Y,\nu}^{\mathrm{ref}}\right)^{1/2}
\right]\\
&=\left(\rho_{Y,\nu}^{\mathrm{ref}}\right)^{1/2}
e^{\ell_{\mathscr T,\nu}}
\left[
\Delta_{\rho_{Y,\nu}^{\mathrm{ref}}}\ell_{\mathscr T,\nu}
+\frac12(\ell_{\mathscr T,\nu},\ell_{\mathscr T,\nu})_{Y,\nu}
\right].
\end{aligned}
$$

Since both prefactors are invertible, this gives

$$
\Delta_{\rho_{Y,\nu}^{\mathrm{ref}}}\ell_{\mathscr T,\nu}
+\frac12(\ell_{\mathscr T,\nu},\ell_{\mathscr T,\nu})_{Y,\nu}=0.
$$

For
\(W_{X,\nu}\in\mathscr O_{X,\nu}^{\bar0}[[\hbar]]\), the pullback is

$$
\mathscr T_{\nu,1/2}^*
\left(\rho_{X,\nu}^{1/2}e^{-W_{X,\nu}/\hbar}\right)
=\left(\rho_{Y,\nu}^{\mathrm{ref}}\right)^{1/2}
\exp\left[
-\hbar^{-1}
\left(
\mathscr T_{\nu,0}^*W_{X,\nu}
-\hbar\log J_{\mathscr T,\nu}^{1/2}
\right)
\right].
\tag{4E.27}
$$

Now specialize \(\rho_{X,\nu}\) and \(\rho_{Y,\nu}^{\mathrm{ref}}\) to the
Step-4D flat coordinate densities.  For \(N_\nu\) regulated adjoint
spacetime coefficients, Step 4D gives

$$
\operatorname{Ber}(d\mathscr T_\nu)=(-16)^{-N_\nu},
\qquad
J_{\mathscr T,\nu}^{1/2}=(4i)^{-N_\nu}.
\tag{4E.28}
$$

Thus the exact quantum-action shift is

$$
\boxed{
W_{Y,\nu}
=\mathscr T_{\nu,0}^*W_{X,\nu}
+\hbar N_\nu\operatorname{Log}_{k_\nu}(4i).}
\tag{4E.29}
$$

Here \(N_\nu\in\mathbb Z_{\geq0}\), and one branch is fixed by

$$
\operatorname{Log}_{k_\nu}(4i)
:=\log 4+i\left(\frac\pi2+2\pi k_\nu\right),
\qquad
k_\nu\in\mathbb Z.
$$

For \(k_\nu' = k_\nu+m\),

$$
W_{Y,\nu}^{(k_\nu')}-W_{Y,\nu}^{(k_\nu)}
=2\pi i\hbar N_\nu m,
\qquad
\exp\left[-\hbar^{-1}
\left(W_{Y,\nu}^{(k_\nu')}-W_{Y,\nu}^{(k_\nu)}\right)\right]
=e^{-2\pi iN_\nu m}=1.
$$

Thus the semidensity (4E.27) is branch-independent.  Since
\(\ell_{\mathscr T,\nu}
=-N_\nu\operatorname{Log}_{k_\nu}(4i)\) is constant in the Step-4D
flat coordinates, its bracket and Laplacian vanish exactly.  The resulting
term is a regulated vacuum normalization, not an odd QME anomaly.  Under
the integer grading it is not a degree-one anomaly.  For a general
compatible reference density, \(\ell_{\mathscr T,\nu}\) can be
field-dependent, so this vacuum-only conclusion does not follow.

### 4E.5 BV pushforward

Choose horizontal Darboux coordinates
\((x^a,x_a^*)\), vertical Darboux coordinates \((y^\alpha,y_\alpha^*)\),
and a gauge-fixed vertical Lagrangian \(L_{\mathrm{ctr},\nu}^{\Psi}\).
Choose the vertical Darboux chart adapted to it, so
\(L_{\mathrm{ctr},\nu}^{\Psi}=\{y^*=0\}\).
Set \(\epsilon_a:=\epsilon(x^a)\) and
\(\epsilon_\alpha:=\epsilon(y^\alpha)\), and set

$$
p_\nu:=\sum_\alpha\epsilon_\alpha\pmod 2.
$$

Let
\(I_\nu(c):=\int_{\Gamma_{\mathrm{ctr},\nu}}Dy\,c\).
Thus raw vertical Berezin integration has parity \(p_\nu\).  If the integer
grading is used, set

$$
q_\nu:=\deg_{\mathrm{HT}}I_\nu,
\qquad
q_\nu\pmod2=p_\nu.
$$

The graded semidensity theorem below is valid for arbitrary \(p_\nu\).
Every ordinary even-action extraction below assumes \(p_\nu=0\).  When the
integer grading is used, each integer-graded cohomological refinement
additionally assumes \(q_\nu=0\), which implies \(p_\nu=0\).  Write
\(\sigma\in\mathscr S_{Y,\nu}^{\mathrm{WKB}}\) as

$$
\sigma
=s(x,x^*,y,y^*)
\left|Dx\,Dx^*\,Dy\,Dy^*\right|^{1/2}.
\tag{4E.30}
$$

Its BV pushforward is

$$
\pi_{\nu*}^{\mathrm{BV}}\sigma
:=
\left[
\int_{\Gamma_{\mathrm{ctr},\nu}\subset L_{\mathrm{ctr},\nu}^{\Psi}}
Dy\,
s(x,x^*,y,0)
\right]
\left|Dx\,Dx^*\right|^{1/2}.
\tag{4E.31}
$$

The cycle in (4E.31) is fixed over the horizontal BV base in the chosen
trivialization:

$$
\Gamma_{\mathrm{ctr},\nu}(x,x^*)
\equiv\Gamma_{\mathrm{ctr},\nu},
\qquad
\frac{\partial\Gamma_{\mathrm{ctr},\nu}}{\partial x^a}=0,
\qquad
\frac{\partial\Gamma_{\mathrm{ctr},\nu}}{\partial x_a^*}=0.
$$

Hence differentiating (4E.31) produces no moving-cycle term.  A
horizontal-dependent cycle is not used here; it would require a separately
defined Gauss--Manin-flat family and a proof that its variation-flux term
vanishes on the full domain \(\mathscr D_{\Gamma,\nu}\).

The graded tensor-product convention fixes the sign.  For homogeneous
horizontal \(b\) and vertical \(c\), using \(I_\nu\) above,

$$
\begin{aligned}
\pi_{\nu*}^{\mathrm{BV}}(bc)
&=(-1)^{p_\nu\epsilon(b)}b\,I_\nu(c),\\
\mathfrak d_{\mathrm h,\nu}
\pi_{\nu*}^{\mathrm{BV}}(bc)
&=(-1)^{p_\nu\epsilon(b)}
(\mathfrak d_{\mathrm h,\nu}b)I_\nu(c),\\
\pi_{\nu*}^{\mathrm{BV}}
\mathfrak d_{\mathrm h,\nu}(bc)
&=(-1)^{p_\nu(\epsilon(b)+1)}
(\mathfrak d_{\mathrm h,\nu}b)I_\nu(c)\\
&=(-1)^{p_\nu}
\mathfrak d_{\mathrm h,\nu}
\pi_{\nu*}^{\mathrm{BV}}(bc).
\end{aligned}
$$

On coefficient functions define the Darboux operators

$$
\mathfrak d_{\mathrm h,\nu}
:=\sum_a(-1)^{\epsilon_a}
\frac{\partial}{\partial x^a}
\frac{\partial}{\partial x_a^*},
\qquad
\mathfrak d_{\mathrm{ctr},\nu}
:=\sum_\alpha(-1)^{\epsilon_\alpha}
\frac{\partial}{\partial y^\alpha}
\frac{\partial}{\partial y_\alpha^*}.
$$

In these coordinates the canonical semidensity operator acts by

$$
\boldsymbol\Delta_{Y,\nu}\sigma
=
\left(
\mathfrak d_{\mathrm h,\nu}s
+\mathfrak d_{\mathrm{ctr},\nu}s
\right)
\left|Dx\,Dx^*\,Dy\,Dy^*\right|^{1/2}.
\tag{4E.32}
$$

The horizontal term passes through the finite vertical integral:

$$
\left[
\int_{\Gamma_{\mathrm{ctr},\nu}}Dy\,
\mathfrak d_{\mathrm h,\nu}s(x,x^*,y,0)
\right]\left|Dx\,Dx^*\right|^{1/2}
=(-1)^{p_\nu}
\boldsymbol\Delta_{\mathrm h,\nu}
\pi_{\nu*}^{\mathrm{BV}}\sigma.
\tag{4E.33}
$$

The vertical term is

$$
\pi_{\nu*}^{\mathrm{BV}}
\left[
\left(\mathfrak d_{\mathrm{ctr},\nu}s\right)
\left|Dx\,Dx^*\,Dy\,Dy^*\right|^{1/2}
\right]
=
\left[
\sum_\alpha(-1)^{\epsilon_\alpha}
\int_{\Gamma_{\mathrm{ctr},\nu}}Dy\,
\frac{\partial}{\partial y^\alpha}
\left[
\left.
\frac{\partial s}{\partial y_\alpha^*}
\right|_{y^*=0}
\right]
\right]
\left|Dx\,Dx^*\right|^{1/2}.
\tag{4E.34}
$$

The exact hypothesis needed here is the BV--Stokes zero-flux condition

$$
\sum_\alpha(-1)^{\epsilon_\alpha}
\int_{\Gamma_{\mathrm{ctr},\nu}}Dy\,
\frac{\partial}{\partial y^\alpha}
\left[
\left.
\frac{\partial s}{\partial y_\alpha^*}
\right|_{y^*=0}
\right]
=0.
\tag{4E.35}
$$

Choose a universal zero-flux subspace
\(\mathscr D_{\Gamma,\nu}\subset
\mathscr S_{Y,\nu}^{\mathrm{WKB}}\) such that

$$
\boxed{
\begin{gathered}
\forall\sigma\in\mathscr D_{\Gamma,\nu}:\\
\pi_{\nu*}^{\mathrm{BV}}\sigma
\in\mathscr S_{\mathrm h,\nu}^{\mathrm{WKB}},\qquad
\pi_{\nu*}^{\mathrm{BV}}\boldsymbol\Delta_{Y,\nu}\sigma
\in\mathscr S_{\mathrm h,\nu}^{\mathrm{WKB}},\\
\text{equation (4E.35) holds for }\sigma,\\
\boldsymbol\Delta_{Y,\nu}\mathscr D_{\Gamma,\nu}
\subseteq\mathscr D_{\Gamma,\nu}.
\end{gathered}}
$$

The last line states stability under the differential.  Define the
admissible input domain

$$
\mathscr S_{X,\nu}^{\mathrm{adm}}
:=
\left\{
\tau\in\mathscr S_{X,\nu}^{\mathrm{WKB}}:
\mathscr T_{\nu,1/2}^*\tau\in\mathscr D_{\Gamma,\nu}
\right\}.
$$

For every \(\sigma\in\mathscr D_{\Gamma,\nu}\), equations
(4E.32)--(4E.35) give

$$
\boxed{
\boldsymbol\Delta_{\mathrm h,\nu}
\pi_{\nu*}^{\mathrm{BV}}\sigma
=(-1)^{p_\nu}
\pi_{\nu*}^{\mathrm{BV}}
\boldsymbol\Delta_{Y,\nu}\sigma.}
\tag{4E.36}
$$

Let \(\mathcal N_\nu(\hbar)\in\mathbb K^\times\) be independent of
all horizontal BV coordinates; it is even.  Define

$$
\mathscr K_\nu:
\mathscr S_{X,\nu}^{\mathrm{adm}}
\longrightarrow\mathscr S_{\mathrm h,\nu}^{\mathrm{WKB}},
\qquad
\mathscr K_\nu
:=\mathcal N_\nu(\hbar)^{-1}
\pi_{\nu*}^{\mathrm{BV}}\mathscr T_{\nu,1/2}^*.
\tag{4E.37}
$$

In the raw convention,
\(\epsilon(\pi_{\nu*}^{\mathrm{BV}})
=\epsilon(\mathscr K_\nu)=p_\nu\).
When the integer grading is used, the raw convention has
\(\deg_{\mathrm{HT}}\mathscr K_\nu=q_\nu\); the integer refinement below
restricts to \(q_\nu=0\).

Field independence of \(\mathcal N_\nu\) means that for every horizontal
semidensity \(\tau\),

$$
\boldsymbol\Delta_{\mathrm h,\nu}
\left(\mathcal N_\nu^{-1}\tau\right)
=\mathcal N_\nu^{-1}
\boldsymbol\Delta_{\mathrm h,\nu}\tau.
$$

Equations (4E.25) and (4E.36) therefore give, on
\(\mathscr S_{X,\nu}^{\mathrm{adm}}\), every intermediate equality:

$$
\boxed{
\begin{aligned}
\boldsymbol\Delta_{\mathrm h,\nu}\mathscr K_\nu
&=\mathcal N_\nu^{-1}
\boldsymbol\Delta_{\mathrm h,\nu}
\pi_{\nu*}^{\mathrm{BV}}\mathscr T_{\nu,1/2}^*\\
&=(-1)^{p_\nu}\mathcal N_\nu^{-1}
\pi_{\nu*}^{\mathrm{BV}}
\boldsymbol\Delta_{Y,\nu}\mathscr T_{\nu,1/2}^*\\
&=(-1)^{p_\nu}\mathcal N_\nu^{-1}
\pi_{\nu*}^{\mathrm{BV}}\mathscr T_{\nu,1/2}^*
\boldsymbol\Delta_{X,\nu}\\
&=(-1)^{p_\nu}\mathscr K_\nu\boldsymbol\Delta_{X,\nu}.
\end{aligned}}
\tag{4E.38}
$$

Consequently,

$$
\boxed{
\boldsymbol\Delta_{X,\nu}\Sigma_{X,\nu}^{Q}=0
\quad\Longrightarrow\quad
\boldsymbol\Delta_{\mathrm h,\nu}
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}}
=0.}
\tag{4E.39}
$$

If \(p_\nu=0\), the raw pushforward is even and the sign in
(4E.36)--(4E.38) is \(+1\).  For \(p_\nu=1\), (4E.39) still transports
QME closedness, but its output is an odd semidensity rather than an
ordinary even quantum action.

To write the output as an even quantum action, additionally require
\(p_\nu=0\), and \(q_\nu=0\) when the integer grading is used, a compatible
horizontal reference density, and the
integer-power normalization

$$
\mathcal N_\nu(\hbar)
\in\mathbb C^\times
\left(1+\hbar\mathbb C[[\hbar]]\right),
$$

together with the perturbative form

$$
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}}
=
\rho_{\mathrm h,\nu}^{1/2}
e^{-S_{\mathrm{hBF},\nu}/\hbar}
\mathcal A_{0,\nu}
\left(
1+\sum_{r\geq1}\hbar^ra_{r,\nu}
\right),
\qquad
\mathcal A_{0,\nu}
\in\left(\mathscr O_{\mathrm h,\nu}^{\bar0}\right)^\times,
\quad
a_{r,\nu}\in\mathscr O_{\mathrm h,\nu}^{\bar0},
\quad
\log\mathcal A_{0,\nu}\in\mathscr O_{\mathrm h,\nu}^{\bar0}.
$$

Under the integer grading, additionally require

$$
\deg_{\mathrm{HT}}\mathcal A_{0,\nu}
=\deg_{\mathrm{HT}}a_{r,\nu}=0.
$$

The leading constant of \(\mathcal N_\nu\) rescales
\(\mathcal A_{0,\nu}\); its \(1+\hbar\mathbb C[[\hbar]]\) part changes
only field-independent higher coefficients.  Neither removes a
field-dependent one-loop factor.  Using the separately chosen
\(\log\mathcal A_{0,\nu}\), the action is

$$
W_{\mathrm h,\nu}^{\mathrm{pf}}
=S_{\mathrm{hBF},\nu}
-\hbar\log\mathcal A_{0,\nu}
-\hbar\log\left(
1+\sum_{r\geq1}\hbar^ra_{r,\nu}
\right).
$$

Thus

$$
M_{1,\nu}^{\mathrm{pf}}
=-\log\mathcal A_{0,\nu},
\qquad
M_{n,\nu}^{\mathrm{pf}}
=-
\left[\hbar^{n-1}\right]
\log\left(
1+\sum_{r\geq1}\hbar^ra_{r,\nu}
\right),
\quad n\geq2.
$$

Writing this action as

$$
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}}
=\rho_{\mathrm h,\nu}^{1/2}
\exp\left[-W_{\mathrm h,\nu}^{\mathrm{pf}}/\hbar\right],
\qquad
W_{\mathrm h,\nu}^{\mathrm{pf}}
=S_{\mathrm{hBF},\nu}
+\sum_{n\geq1}\hbar^nM_{n,\nu}^{\mathrm{pf}},
\tag{4E.40}
$$

equation (4E.39) gives the complete coefficient recursion

$$
\boxed{
d_{\mathrm h,\nu}M_{n,\nu}^{\mathrm{pf}}
=\Delta_{\mathrm h,\nu}M_{n-1,\nu}^{\mathrm{pf}}
-\frac12\sum_{r=1}^{n-1}
(M_{r,\nu}^{\mathrm{pf}},M_{n-r,\nu}^{\mathrm{pf}})_{\mathrm h,\nu},
\quad n\geq1,}
\tag{4E.41}
$$

where
\(d_{\mathrm h,\nu}:=(S_{\mathrm{hBF},\nu},\cdot)_{\mathrm h,\nu}\)
and \(M_{0,\nu}^{\mathrm{pf}}:=S_{\mathrm{hBF},\nu}\).  The Step-4D
holomorphic-BF CME gives

$$
\frac12
(S_{\mathrm{hBF},\nu},S_{\mathrm{hBF},\nu})_{\mathrm h,\nu}=0
\quad\Longrightarrow\quad
d_{\mathrm h,\nu}^{\,2}=0.
$$

### 4E.6 The contractible factor

The Step-4D vertical action is

$$
S_{\mathrm{ctr},\nu}
=\int d^4x_E\,\operatorname{tr}_\kappa
\left(u_1^*\eta_1+u_2^*\eta_2-w^*K\right)_\nu.
\tag{4E.42}
$$

Let \(\rho_{\mathrm{ctr},\nu}^{\mathrm{flat}}\) be the flat vertical
density.  Its function Laplacian is

$$
\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}
=\sum_{i=1}^2
\left[
(-1)^{\epsilon_{u_i}}
\frac{\partial}{\partial u_i}
\frac{\partial}{\partial u_i^*}
+(-1)^{\epsilon_{\eta_i}}
\frac{\partial}{\partial\eta_i}
\frac{\partial}{\partial\eta_i^*}
\right]
+(-1)^{\epsilon_w}
\frac{\partial}{\partial w}
\frac{\partial}{\partial w^*}
+(-1)^{\epsilon_K}
\frac{\partial}{\partial K}
\frac{\partial}{\partial K^*}.
\tag{4E.43}
$$

Every second derivative vanishes separately:

$$
\begin{gathered}
\frac{\partial}{\partial u_i}
\frac{\partial}{\partial u_i^*}(u_i^*\eta_i)=0,
\qquad
\frac{\partial}{\partial\eta_i}
\frac{\partial}{\partial\eta_i^*}(u_i^*\eta_i)=0,\\
\frac{\partial}{\partial w}
\frac{\partial}{\partial w^*}(-w^*K)=0,
\qquad
\frac{\partial}{\partial K}
\frac{\partial}{\partial K^*}(-w^*K)=0.
\end{gathered}
\tag{4E.44}
$$

Hence

$$
\boxed{
\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}
S_{\mathrm{ctr},\nu}=0.}
\tag{4E.45}
$$

For
\(\rho_{\mathrm{ctr},\nu}
=e^{\ell_{\mathrm{ctr},\nu}}
\rho_{\mathrm{ctr},\nu}^{\mathrm{flat}}\),

$$
\Delta_{\rho_{\mathrm{ctr},\nu}}S_{\mathrm{ctr},\nu}
=\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}S_{\mathrm{ctr},\nu}
+\frac12
(\ell_{\mathrm{ctr},\nu},S_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}.
\tag{4E.46}
$$

If both full densities are compatible, their half-density ratio is
\(e^{\ell_{\mathrm{ctr},\nu}/2}\), and compatibility expands without an
undetermined central term:

$$
\begin{aligned}
0
&=\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}
e^{\ell_{\mathrm{ctr},\nu}/2}\\
&=e^{\ell_{\mathrm{ctr},\nu}/2}
\left[
\frac12\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}
\ell_{\mathrm{ctr},\nu}
+\frac18
(\ell_{\mathrm{ctr},\nu},\ell_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}
\right].
\end{aligned}
$$

Since the exponential is invertible, the density-compatibility condition is

$$
\boxed{
\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}
\ell_{\mathrm{ctr},\nu}
+\frac14
(\ell_{\mathrm{ctr},\nu},\ell_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}
=0.}
$$

Therefore the non-flat condition for
\(\Delta_{\rho_{\mathrm{ctr},\nu}}S_{\mathrm{ctr},\nu}=0\) is exactly

$$
(\ell_{\mathrm{ctr},\nu},S_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}=0.
\tag{4E.47}
$$

The Step-4D classical action contains no monomial with both a horizontal
variable and a vertical variable.  Define
\(\operatorname{Res}_{L_{\mathrm{ctr},\nu}^{\Psi}}\) as the canonical restriction
of a BV semidensity to a density on the vertical Lagrangian.  To extract a
scalar in \(\mathbb K^\times\), assume \(p_\nu=0\), and \(q_\nu=0\) when
the integer grading is used.  The pure classical vertical factor is then
the even scalar

$$
C_{\mathrm{ctr},\nu}(\hbar)
:=
\int_{\Gamma_{\mathrm{ctr},\nu}}
\operatorname{Res}_{L_{\mathrm{ctr},\nu}^{\Psi}}
\left[
\rho_{\mathrm{ctr},\nu}^{1/2}
e^{-S_{\mathrm{ctr},\nu}/\hbar}
\right],
\qquad
C_{\mathrm{ctr},\nu}(\hbar)\in\mathbb K^\times,
\tag{4E.48}
$$

provided the contour, orientation, convergence, and zero-flux hypotheses
hold.  To test the Step-4D flat measure, take
\(\rho_{\mathrm{ctr},\nu}=\rho_{\mathrm{ctr},\nu}^{\mathrm{flat}}\).
The original antifield-zero Lagrangian is

$$
L_{\mathrm{ctr},\nu}^{(0)}
:=\{u_i^*=\eta_i^*=w^*=K^*=0\}.
$$

On this Lagrangian,

$$
\left.S_{\mathrm{ctr},\nu}\right|_{L_{\mathrm{ctr},\nu}^{(0)}}=0,
\qquad
\left.e^{-S_{\mathrm{ctr},\nu}/\hbar}
\right|_{L_{\mathrm{ctr},\nu}^{(0)}}=1.
$$

In the corresponding flat chart,

$$
\operatorname{Res}_{L_{\mathrm{ctr},\nu}^{(0)}}
\left[
\left(\rho_{\mathrm{ctr},\nu}^{\mathrm{flat}}\right)^{1/2}
e^{-S_{\mathrm{ctr},\nu}/\hbar}
\right]
\quad\text{has coefficient }1.
$$

The Step-4D parity table gives

$$
\epsilon(u_1)=\epsilon(u_2)=\epsilon(K)=0,
\qquad
\epsilon(\eta_1)=\epsilon(\eta_2)=\epsilon(w)=1.
$$

For every regulated coefficient,

$$
\int d\eta_1\,d\eta_2\,dw\,1
=
\frac{\partial}{\partial w}
\frac{\partial}{\partial\eta_2}
\frac{\partial}{\partial\eta_1}1
=0.
$$

Hence every remaining odd integral of this flat constant integrand is zero,
whereas every noncompact even integral lacks damping.  Therefore the pair
\((L_{\mathrm{ctr},\nu}^{(0)},
\rho_{\mathrm{ctr},\nu}^{\mathrm{flat}})\) cannot produce the nonzero
element required in (4E.48).  One must construct either a different
gauge-fixed \(L_{\mathrm{ctr},\nu}^{\Psi}\) with a nondegenerate restricted
action, or a compatible non-flat density whose restriction supplies both
the Berezin top coefficient and even-direction damping.  Only after that
construction may the scalar normalization be chosen as

$$
\mathcal N_\nu^{\mathrm{cl}}(\hbar)
=(4i)^{-N_\nu}C_{\mathrm{ctr},\nu}(\hbar).
$$

For the integer-power action extraction following (4E.39), this scalar
must additionally lie in
\(\mathbb C^\times(1+\hbar\mathbb C[[\hbar]])\).  A general element of
\(\mathbb K^\times\) defines the semidensity chain map but not the displayed
integer-power action expansion.

Equation (4E.48) is a hypothesis, not a canonical evaluation.  The quantum
terms \(\mathscr T_{\nu,0}^*M_{n,\nu}\) and
\(\mathscr T_{\nu,0}^*H_{Q,n,\nu}\) may mix horizontal and vertical variables.
Therefore \(C_{\mathrm{ctr},\nu}\) is not asserted to factor from the full
quantum pushforward.  The chain identity (4E.38) does not require such a
factorization.

### 4E.7 Comparison with independent holomorphic-BF quantization

Assume that \(W_{\mathrm h,\nu}^{\mathrm{pf}}\) and
\(W_{\mathrm h,\nu}^{\mathrm{ind}}\) belong to the same regulated BV
algebra \(\mathscr O_{\mathrm h,\nu}\), use the same bracket and compatible
Laplacian, satisfy

$$
\frac12
(W_{\mathrm h,\nu}^{a},W_{\mathrm h,\nu}^{a})_{\mathrm h,\nu}
-\hbar\Delta_{\mathrm h,\nu}W_{\mathrm h,\nu}^{a}=0,
\qquad
a\in\{\mathrm{pf},\mathrm{ind}\},
$$

and agree through order \(\hbar^{n-1}\).  Define their first difference by

$$
D_{n,\nu}
:=M_{n,\nu}^{\mathrm{pf}}-M_{n,\nu}^{\mathrm{ind}}.
\tag{4E.49}
$$

Thus \(D_{n,\nu}\in\mathscr O_{\mathrm h,\nu}^{\bar0}\).

Subtracting their order-\(\hbar^n\) QME recursions cancels the Laplacian
term and every lower-order bracket term:

$$
\begin{aligned}
0
={}&d_{\mathrm h,\nu}M_{n,\nu}^{\mathrm{pf}}
-\Delta_{\mathrm h,\nu}M_{n-1,\nu}^{\mathrm{pf}}
+\frac12\sum_{r=1}^{n-1}
(M_{r,\nu}^{\mathrm{pf}},M_{n-r,\nu}^{\mathrm{pf}})_{\mathrm h,\nu}\\
&-d_{\mathrm h,\nu}M_{n,\nu}^{\mathrm{ind}}
+\Delta_{\mathrm h,\nu}M_{n-1,\nu}^{\mathrm{ind}}
-\frac12\sum_{r=1}^{n-1}
(M_{r,\nu}^{\mathrm{ind}},M_{n-r,\nu}^{\mathrm{ind}})_{\mathrm h,\nu}\\
={}&d_{\mathrm h,\nu}D_{n,\nu}.
\end{aligned}
\tag{4E.50}
$$

Therefore

$$
\boxed{
[D_{n,\nu}]
\in H^{\bar0}
\left(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu}\right),}
\tag{4E.51}
$$

If the integer twisted grading is preserved, this is
\(H^0(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu})\).

Equality up to an order-\(\hbar^n\) regulated canonical transformation,
allowed parameter redefinition, and vacuum normalization requires

$$
\boxed{
D_{n,\nu}
=d_{\mathrm h,\nu}R_{n,\nu}
+\sum_A\delta g_{n,\nu}^{A}
\frac{\partial S_{\mathrm{hBF},\nu}}{\partial g^A}
+\zeta_{n,\nu},
\qquad
R_{n,\nu}\in\mathscr O_{\mathrm h,\nu}^{\bar1},
\quad
\delta g_{n,\nu}^{A}\in\mathbb C,
\quad
\zeta_{n,\nu}\in\mathbb C\cdot1.}
\tag{4E.52}
$$

When the integer twisted grading exists,
\(\deg_{\mathrm{HT}}R_{n,\nu}=-1\).

The constant in (4E.52) is removable only while the normalization remains
adjustable.  With the orientation

$$
W_{\mathrm h,\nu}^{\mathrm{pf}}
-W_{\mathrm h,\nu}^{\mathrm{ind}}
=\hbar^n\zeta_{n,\nu}
$$

after the canonical and parameter terms have been removed, set

$$
\mathcal N_\nu'
:=e^{-\hbar^{n-1}\zeta_{n,\nu}}\mathcal N_\nu.
$$

Then every sign is fixed by

$$
\begin{aligned}
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}\prime}
&=(\mathcal N_\nu')^{-1}
\pi_{\nu*}^{\mathrm{BV}}
\mathscr T_{\nu,1/2}^*\Sigma_{X,\nu}^{Q}\\
&=e^{\hbar^{n-1}\zeta_{n,\nu}}
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}},\\
W_{\mathrm h,\nu}^{\mathrm{pf}\prime}
&=-\hbar\log\left[
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}\prime}/
\rho_{\mathrm h,\nu}^{1/2}
\right]\\
&=W_{\mathrm h,\nu}^{\mathrm{pf}}
-\hbar^n\zeta_{n,\nu}.
\end{aligned}
$$

If \(\mathcal N_\nu\) is frozen, normalized-semidensity equality requires
\(\zeta_{n,\nu}=0\); in that case the quotient below does not divide by
\([1]\).

For adjustable normalization, the residual comparison defect is the quotient
class

$$
\left[D_{n,\nu}\right]_{\mathrm{comp}}
\in
\frac{H^{\bar0}
\left(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu}\right)}
{\operatorname{span}
\left\{
\left[
\partial S_{\mathrm{hBF},\nu}/\partial g^A
\right],[1]
\right\}}.
\tag{4E.53}
$$

For frozen normalization, remove \([1]\) from the denominator of (4E.53)
and require \(\zeta_{n,\nu}=0\) in (4E.52).

The exact chain-map theorem makes the odd QME defect of the
pushforward-defined output vanish once the input QME exists.  Under the
integer grading this is the vanishing of its degree-one defect.  It does
not annihilate (4E.53).

Assume that the horizontal bracket is independent of every allowed
parameter \(g^A\), and that the hBF CME holds for every allowed value of
those parameters.  The parameter representatives in (4E.52) are then
closed because

$$
d_{\mathrm h,\nu}
\frac{\partial S_{\mathrm{hBF},\nu}}{\partial g^A}
=
\frac{\partial}{\partial g^A}
\left[
\frac12(S_{\mathrm{hBF},\nu},S_{\mathrm{hBF},\nu})_{\mathrm h,\nu}
\right]
=0,
\qquad
d_{\mathrm h,\nu}1=0.
$$

The list of allowed parameters must be fixed and proved exhaustive before
vanishing of the quotient class can be concluded.

### 4E.8 Distinct anomaly channels

Let \(\mathsf A_a:=\operatorname{ad}_{T_a}\) be the
adjoint-representation matrix of \(T_a\).  For any endomorphism
\(\mathsf B\), its \(\kappa\)-transpose is defined by
\(\kappa(\mathsf Bu,v)=\kappa(u,\mathsf B^{T_\kappa}v)\).  Invariance of
\(\kappa\) gives

$$
\mathsf A_a^{T_\kappa}=-\mathsf A_a,
\qquad
\{\mathsf A_b,\mathsf A_c\}^{T_\kappa}
=\mathsf A_c^{T_\kappa}\mathsf A_b^{T_\kappa}
+\mathsf A_b^{T_\kappa}\mathsf A_c^{T_\kappa}
=\{\mathsf A_b,\mathsf A_c\}.
\tag{4E.54}
$$

The symmetric adjoint gauge-anomaly tensor obeys

$$
\begin{aligned}
d_{abc}^{\mathrm{adj}}
&:=\frac12\operatorname{Tr}_{\mathrm{adj}}
\left(\mathsf A_a\{\mathsf A_b,\mathsf A_c\}\right)\\
&=\frac12\operatorname{Tr}_{\mathrm{adj}}
\left[
\left(\mathsf A_a\{\mathsf A_b,\mathsf A_c\}\right)^{T_\kappa}
\right]\\
&=-\frac12\operatorname{Tr}_{\mathrm{adj}}
\left(\{\mathsf A_b,\mathsf A_c\}\mathsf A_a\right)\\
&=-\frac12\operatorname{Tr}_{\mathrm{adj}}
\left(\mathsf A_a\{\mathsf A_b,\mathsf A_c\}\right)
=-d_{abc}^{\mathrm{adj}}.
\end{aligned}
\tag{4E.55}
$$

Over \(\mathbb C\),

$$
\boxed{d_{abc}^{\mathrm{adj}}=0.}
\tag{4E.56}
$$

Equation (4E.56) removes this candidate tensor only; it does not prove that
the continuum local gauge-plus-\(Q\) \(H^{\bar1}_{\mathrm{loc}}\)
classification contains no other cocycle.  With the integer grading this
refines to \(H^1_{\mathrm{loc}}\).

For Ward operators \(\mathcal W_R,\mathcal W_Q\), let \(\Gamma\) denote
the renormalized 1PI effective action in the chosen scheme, let \(r_Q\) be
the \(R\)-charge of \(Q\), and assume

$$
\mathcal W_R\Gamma=\hbar\mathscr A_R,
\qquad
\mathcal W_Q\Gamma=\hbar\mathscr A_Q,
\qquad
[\mathcal W_R,\mathcal W_Q]=r_Q\mathcal W_Q.
\tag{4E.57}
$$

Acting on \(\Gamma\) gives the Wess--Zumino relation

$$
\boxed{
\mathcal W_R\mathscr A_Q
-\mathcal W_Q\mathscr A_R
=r_Q\mathscr A_Q.}
\tag{4E.58}
$$

If \(\mathscr A_Q=0\), equation (4E.58) yields

$$
\mathcal W_Q\mathscr A_R=0,
\tag{4E.59}
$$

and does not yield \(\mathscr A_R=0\).  A continuous \(U(1)_R\) anomaly
blocks \(R\)-equivariance, twisted rotations, and an \(R\)-derived integer
grading.  It enters the master-equation \(H^1\) problem only after the
\(R\)-symmetry is coupled to its own background ghost.

The obstruction ledger is

$$
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{degree or mechanism}&\text{statement affected}\\ \hline
\text{ordinary gauge-plus-}Q\text{ QME}
&H^{\bar1}(\mathscr O_{X,\nu},d_{\mathrm{tw},0,\nu})
&\text{existence of }\Sigma_{X,\nu}^{Q}\\
\text{independent hBF QME}
&H^{\bar1}(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu})
&\text{existence of }\Sigma_{\mathrm h,\nu}^{\mathrm{ind}}\\
\text{scheme, beta, finite counterterm}
&H^{\bar0}(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu})
&\text{comparison class (4E.53)}\\
U(1)_R\text{ Ward identity}
&R\text{-equivariant complex}&R\text{-grading and twisted rotations}\\
\text{regulator breaking}
&H^{\bar1}\text{ or chain-map failure}&\text{regulated theorem}\\
\text{vertical boundary flux}
&\text{failure of (4E.35)}&\text{BV pushforward chain map}\\
\text{source and state mismatch}
&\text{missing map}&\text{normalized correlators}\\
\text{global Euclidean cycle}
&\text{analytic and topological data}&\text{actual integral}
\end{array}}
\tag{4E.60}
$$

At finite regulator the bars in (4E.60) denote parity.  If the integer
twisted grading is preserved, \(H^{\bar0},H^{\bar1}\) refine to
\(H^0,H^1\).  These groups become
local cohomology modulo spacetime derivatives only after (4E.62)--(4E.63)
and locality are proved.  In particular, a nonzero beta function is not by
itself an odd QME obstruction; under the integer grading it is not a
degree-one obstruction.

### 4E.9 Regulator removal

For \(\nu\geq\mu\), let

$$
R_{\nu\to\mu}^{X}:
\mathscr S_{X,\nu}^{\mathrm{adm}}
\longrightarrow
\mathscr S_{X,\mu}^{\mathrm{adm}},
\qquad
R_{\nu\to\mu}^{\mathrm h}:
\mathscr S_{\mathrm h,\nu}^{\mathrm{WKB}}
\longrightarrow
\mathscr S_{\mathrm h,\mu}^{\mathrm{WKB}}
\tag{4E.61}
$$

be even regulated BV effective-theory maps satisfying

$$
\boldsymbol\Delta_{X,\mu}R_{\nu\to\mu}^{X}
=R_{\nu\to\mu}^{X}\boldsymbol\Delta_{X,\nu},
\qquad
\boldsymbol\Delta_{\mathrm h,\mu}R_{\nu\to\mu}^{\mathrm h}
=R_{\nu\to\mu}^{\mathrm h}\boldsymbol\Delta_{\mathrm h,\nu}.
$$

For the comparison below, require \(p_\nu=0\) at every regulator, so every
\(\mathscr K_\nu\) is even on the displayed unshifted target.  When the
integer grading is used, additionally require \(q_\nu=0\), so every
\(\mathscr K_\nu\) has degree \(0\).  The chain homotopy then has type

$$
H_{\nu\mu}:
\mathscr S_{X,\nu}^{\mathrm{adm}}
\longrightarrow
\mathscr S_{\mathrm h,\mu}^{\mathrm{WKB}},
\qquad
\epsilon(H_{\nu\mu})=1.
$$

If the integer grading exists, \(\deg_{\mathrm{HT}}H_{\nu\mu}=-1\).
The required homotopy-commuting square is

$$
\boxed{
R_{\nu\to\mu}^{\mathrm h}\mathscr K_\nu
-\mathscr K_\mu R_{\nu\to\mu}^{X}
=
\boldsymbol\Delta_{\mathrm h,\mu}H_{\nu\mu}
+H_{\nu\mu}\boldsymbol\Delta_{X,\nu}.}
\tag{4E.62}
$$

Let \(\Omega_{\mathrm{loc}}^{p,\bar k}\) be local spacetime \(p\)-form
densities of BV parity \(\bar k\), let
\(d_{\mathrm{sp}}:\Omega_{\mathrm{loc}}^{p,\bar k}
\to\Omega_{\mathrm{loc}}^{p+1,\bar k}\) be the spacetime exterior
differential, and let \(\mathscr O_{\mathrm{loc}}\) denote the associated
integrated local functionals.  Let
\(\operatorname{Flux}_{\partial\Gamma_{\mathrm{ctr},\mu}}(\sigma)\)
denote the boundary functional appearing on the left-hand side of
(4E.35).  In addition, every coefficient must have a local limit:

$$
\forall n\geq0:\qquad
\lim_{\mu\to\infty}M_{n,\mu}^{\mathrm{pf}}
=M_{n}^{\mathrm{pf}}
\in\mathscr O_{\mathrm{loc}},
\qquad
\lim_{\mu\to\infty}
\operatorname{Flux}_{\partial\Gamma_{\mathrm{ctr},\mu}}
\left(\mathscr T_{\mu,1/2}^*\Sigma_{X,\mu}^{Q}\right)=0.
\tag{4E.63}
$$

In addition, assume that compatible local representatives admit the
bracket limit

$$
(F,G)_{\mathrm h}
:=\lim_{\mu\to\infty}(F_\mu,G_\mu)_{\mathrm h,\mu},
$$

independently of the representatives.  When the \(n=0\) limit exists,
define \(S_{\mathrm{hBF}}:=M_0^{\mathrm{pf}}\) and
\(d_{\mathrm h}:=(S_{\mathrm{hBF}},\cdot)_{\mathrm h}\) on integrated
functionals.  Additionally require a representative-level lift

$$
d_{\mathrm h}^{\mathrm{dens}}:
\Omega_{\mathrm{loc}}^{p,\bar k}
\longrightarrow
\Omega_{\mathrm{loc}}^{p,\overline{k+1}},
\qquad
d_{\mathrm h}\!\left(\int a\right)
=\int d_{\mathrm h}^{\mathrm{dens}}a
\quad
\left(a\in\Omega_{\mathrm{loc}}^{4,\bar k}\right).
$$

Below suppress the superscript \(\mathrm{dens}\).  Require the continuum
CME and bicomplex identities

$$
\frac12(S_{\mathrm{hBF}},S_{\mathrm{hBF}})_{\mathrm h}=0,
\qquad
d_{\mathrm h}^{\,2}=0,
\qquad
d_{\mathrm{sp}}^{\,2}=0,
\qquad
d_{\mathrm h}d_{\mathrm{sp}}
+d_{\mathrm{sp}}d_{\mathrm h}=0.
$$

For parity \(\bar k\), the relative local cohomology used below is

$$
H^{\bar k}_{\mathrm{loc}}(d_{\mathrm h}\mid d_{\mathrm{sp}})
:=
\frac{
\left\{
a\in\Omega_{\mathrm{loc}}^{4,\bar k}:
d_{\mathrm h}a+d_{\mathrm{sp}}b=0
\text{ for some }
b\in\Omega_{\mathrm{loc}}^{3,\overline{k+1}}
\right\}
}{
\left\{
a=d_{\mathrm h}r+d_{\mathrm{sp}}h:
r\in\Omega_{\mathrm{loc}}^{4,\overline{k-1}},
\ h\in\Omega_{\mathrm{loc}}^{3,\bar k}
\right\}
}.
$$

Equations (4E.62)--(4E.63), the bracket limit, and the continuum
CME/bicomplex identities are not proved.

### 4E.10 Theorems and non-theorems

**Finite-regulator theorem.**  Assume:

1. a finite interacting regulator preserving the odd symplectic structures;
2. the WKB semidensity modules and canonical operators declared in 4E.1;
3. a full quantum gauge-plus-\(Q\) semidensity
   \(\Sigma_{X,\nu}^{Q}\in\mathscr S_{X,\nu}^{\mathrm{adm}}\)
   satisfying (4E.9);
4. the invertible odd symplectomorphism \(\mathscr T_\nu\);
5. a vertical Lagrangian cycle and stable domain
   \(\mathscr D_{\Gamma,\nu}\) satisfying convergence, the fixed-base-cycle
   condition following (4E.31), and (4E.35) for every element;
6. a nonzero field-independent normalization
   \(\mathcal N_\nu(\hbar)\);
7. \(p_\nu=0\), and \(q_\nu=0\) for the integer refinement, a compatible
   horizontal density, and an invertible output factor
   \(\mathcal A_{0,\nu}\) with a chosen logarithm, as displayed before
   (4E.40), when a function master action is extracted.

Then (4E.38) is an exact all-order graded chain identity and (4E.39) proves the
QME for the pushforward-defined holomorphic theory.  The proof is exactly
(4E.21)--(4E.39), with no loop-order truncation.

$$
\boxed{
\text{fixed }\nu:
\quad
\boldsymbol\Delta_{X,\nu}\Sigma_{X,\nu}^Q=0
\Longrightarrow
\boldsymbol\Delta_{\mathrm h,\nu}
\Sigma_{\mathrm h,\nu}^{\mathrm{pf}}=0.}
\tag{4E.64}
$$

**Independent-quantization criterion.**  Equality with an independently
renormalized holomorphic-BF theory holds through order \(\hbar^n\) only if
every first mismatch through that order has vanishing class (4E.53).

**Blocked extensions.**  The continuum local perturbative theorem requires
(4E.62)--(4E.63).  The normalized-correlator theorem additionally requires
a chain map on observables, sources, composite-operator counterterms, and
states.  The \(R\)-equivariant theorem requires cancellation or controlled
incorporation of \(\mathscr A_R\).  The actual Euclidean and nonperturbative
theorem requires a real cycle, convergence, global bundle sectors,
instantons, and boundary data.

### 4E.11 Derivation-gap audit

The abstract finite-regulator implication (4E.64) has a complete proof
conditional on its seven displayed hypotheses.  Application to Euclidean
pure \(\mathcal N=1\) gauge theory has the following open obligations:

$$
\boxed{
\begin{array}{c|c|c|p{4.8cm}|p{5.7cm}}
\mathrm{id}&\mathrm{type}&\mathrm{severity}&\mathrm{claim\ not\ made}
&\mathrm{minimal\ missing\ construction}\\ \hline
\mathrm{QHT\!-\!GAP\!-\!01}&\mathrm{G\!-\!OP}&\mathrm{P1}
&Existence of a finite interacting regulator satisfying the classical and
quantum BV identities.
&Construct a finite model closed under the nonlinear bracket and prove its
CME, odd symplectic nondegeneracy, and compatible BV operator.\\
\mathrm{QHT\!-\!GAP\!-\!02}&\mathrm{G\!-\!THM}&\mathrm{P1}
&Existence of the full quantum gauge-plus-\(Q\) master action.
&Solve (4E.15) at every order or compute a nonzero class (4E.17).\\
\mathrm{QHT\!-\!GAP\!-\!03}&\mathrm{G\!-\!SCOPE}&\mathrm{P1}
&Use of the imported quantum-BV and holomorphic-renormalization references
as Project authority.
&Merge the reference-import proposal into verified origin/main and perform
the required source-to-Project translation.\\
\mathrm{QHT\!-\!GAP\!-\!04}&\mathrm{G\!-\!THM}&\mathrm{P1}
&Removal of the regulator while retaining locality and the QME.
&Construct \(R_{\nu\to\mu}^{X},R_{\nu\to\mu}^{\mathrm h},H_{\nu\mu}\)
and prove (4E.62)--(4E.63).\\
\mathrm{QHT\!-\!GAP\!-\!05}&\mathrm{G\!-\!THM}&\mathrm{P1}
&Existence and equality of an independently renormalized holomorphic-BF
quantization.
&First solve every independent hBF \(H^{\bar1}\) QME obstruction; compute
\(H^{\bar0}(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu})\);
then prove locality and compute
\(H^{\bar0}_{\mathrm{loc}}(d_{\mathrm h}\mid d_{\mathrm{sp}})\), refining
to \(H^0_{\mathrm{loc}}\) when the integer grading survives, with every comparison class
(4E.53) vanishing modulo allowed parameters and constants.\\
\mathrm{QHT\!-\!GAP\!-\!06}&\mathrm{G\!-\!NORM}&\mathrm{P1}
&Existence and canonical normalization of the vertical integral.
&Prove \(p_\nu=0\) for the regulated fiber and, for the integer refinement,
prove \(q_\nu=0\), or construct an explicit shifted target complex;
construct either \(L_{\mathrm{ctr},\nu}^{\Psi}\neq
L_{\mathrm{ctr},\nu}^{(0)}\) with a nondegenerate restricted action or a
compatible non-flat density with a saturating, damped restriction; choose a
convergent cycle and orientation, prove
the fixed-base-cycle condition following (4E.31), prove (4E.35), and evaluate a nonzero
\(C_{\mathrm{ctr},\nu}(\hbar)\).\\
\mathrm{QHT\!-\!GAP\!-\!07}&\mathrm{G\!-\!PROJ}&\mathrm{P2}
&Equality of normalized correlation functions.
&Construct the source, observable, composite-operator, and state chain maps
and prove compatibility with \(\mathscr K_\nu\).\\
\mathrm{QHT\!-\!GAP\!-\!08}&\mathrm{G\!-\!SCOPE}&\mathrm{P2}
&Continuous \(U(1)_R\)-equivariance and the induced integer grading.
&Introduce the \(R\)-background complex and solve its Ward identity without
identifying \(\mathscr A_R\) with \(\mathscr A_Q\).\\
\mathrm{QHT\!-\!GAP\!-\!09}&\mathrm{G\!-\!SCOPE}&\mathrm{P2}
&Actual Euclidean, global, instanton-sector, or nonperturbative equality.
&Specify the Euclidean reality cycle, convergence, bundle sectors,
boundary conditions, and a BV--BFV completion when required.
\end{array}}
\tag{4E.65}
$$

The exact status is

$$
\boxed{
\begin{gathered}
\text{abstract finite-regulator semidensity theorem:
PROVED CONDITIONALLY},\\
\text{application to Project pure }\mathcal N=1\text{ theory:
BLOCKED BY QHT-GAP-01,02,06},\\
\text{independent hBF comparison:
BLOCKED BY QHT-GAP-03,05},\\
\text{continuum theorem:
BLOCKED BY QHT-GAP-04},\\
\text{correlator, equivariant, and global extensions:
BLOCKED BY QHT-GAP-07,08,09}.
\end{gathered}}
\tag{4E.66}
$$
