# 00 3+1d SUSY QFT — Convention Lock

## Step 4D. Majorana spinor system

### 4D.0 Scope, inputs, and branch declaration

This contract fixes the Project four-component (Majorana) spinor
system that equation (D.1.1) of the notation dictionary left
`UNFIXED`, and rebuilds every previously locked two-component (Weyl)
convention in a parallel four-component form.  All results are derived
from the locked Project contracts — Step 1 (spinor slots, sigma
system, supersymmetry algebra), Step 2A (superspace), Step 3B
(component reconstruction), Step 4 (extended-SYM slots), Step 4A
(\(\mathcal N=1\) SYM), and Step 4C (\(\mathcal N=4\) SYM).  The
Weinberg and Srednicki columns of the dictionary are used only for the
book comparison in Section 4D.17; no book formula enters any
derivation.

The Project Majorana branch is declared once, before any derivation:
it agrees with Srednicki and is opposite to Weinberg in every
branch-dependent choice,

$$
\boxed{
\begin{array}{l|c|c}
&\text{Project}=\text{Srednicki branch}&\text{Weinberg branch}\\ \hline
\{\gamma^\mu,\gamma^\nu\}
&-2\eta^{\mu\nu}\mathbf1_4
&+2\eta^{\mu\nu}\mathbf1_4\\
\gamma_5
&+i\gamma^0\gamma^1\gamma^2\gamma^3
&-i\gamma^0\gamma^1\gamma^2\gamma^3\\
\text{Majorana bar}
&\bar\Psi=+\Psi^{\rm T}\mathcal C
&\bar\Psi=-\Psi^{\rm T}\mathcal C\\
\text{Majorana reality}
&\Psi^*=-\beta\mathcal C\Psi
&\Psi^*=+\beta\mathcal C\Psi\\
\text{Majorana kinetic term}
&+\tfrac i2\bar\Psi\gamma^\mu\partial_\mu\Psi
&-\tfrac12\bar\Psi_W\gamma_W^\mu\partial_\mu\Psi_W
\end{array}}
\tag{4D.1}
$$

The right column is recorded from the locked dictionary equations
(D.3.1), (D.3.4), (D.3.16), (D.3.19) for comparison only; every entry
of the left column is derived below from Step-1 conventions and is
machine-checked by
`scripts/verify_step4d_majorana_spinor_system.py`.

### 4D.1 Four-component slots and gamma matrices

A four-component column carries the slot layout

$$
\Psi_\alpha
=\begin{pmatrix}\psi_a\\ \widetilde\chi^{\dot a}\end{pmatrix},
\qquad
\alpha=(a;\dot a),
\qquad
a=1,2,\quad \dot a=\dot1,\dot2,
\tag{4D.2}
$$

with a lower undotted Step-1 slot on top and an upper dotted Step-1
slot below.  All raising and lowering inside the blocks is the locked
Step-1 epsilon action (1.3)--(1.5).  The Lorentzian gamma matrices are
defined from the Step-1 sigma system (1.10)--(1.11),

$$
\boxed{
\gamma_L^\mu
:=\begin{pmatrix}
0&(\sigma_L^\mu)_{a\dot b}\\
(\bar\sigma_L^\mu)^{\dot ab}&0
\end{pmatrix}.}
\tag{4D.3}
$$

The Step-1 Clifford relations (1.12)--(1.13) give, blockwise,

$$
\boxed{
\{\gamma_L^\mu,\gamma_L^\nu\}
=-2\eta^{\mu\nu}\mathbf1_4.}
\tag{4D.4}
$$

The Euclidean gamma matrices are defined from the Step-1 Euclidean
sigma system (1.51)--(1.52),

$$
\boxed{
\gamma_E^m
:=\begin{pmatrix}
0&(\sigma_E^m)_{a\dot b}\\
(\bar\sigma_E^m)^{\dot ab}&0
\end{pmatrix},}
\tag{4D.5}
$$

and (1.54) gives

$$
\boxed{
\{\gamma_E^m,\gamma_E^n\}
=+2\delta^{mn}\mathbf1_4.}
\tag{4D.6}
$$

Because \(\sigma_E^j=-i\sigma_L^j\), \(\bar\sigma_E^j=-i\bar\sigma_L^j\),
\(\sigma_E^4=\sigma_L^0\), and \(\bar\sigma_E^4=\bar\sigma_L^0\), the
Wick relation of the two gamma systems is

$$
\gamma_E^j=-i\gamma_L^j\ (j=1,2,3),
\qquad
\gamma_E^4=\gamma_L^0 .
\tag{4D.7}
$$

Below, an unsubscripted \(\gamma^\mu\) in a Lorentzian formula means
\(\gamma_L^\mu\), and \(\gamma_E^m\) is always written explicitly.

### 4D.2 Chirality, projectors, and antisymmetric products

Define, on the Srednicki branch of (4D.1),

$$
\boxed{
\gamma_5:=+i\gamma_L^0\gamma_L^1\gamma_L^2\gamma_L^3 .}
\tag{4D.8}
$$

Blockwise,
\(\gamma^0\gamma^1\gamma^2\gamma^3
=\operatorname{diag}(\sigma^0\bar\sigma^1\sigma^2\bar\sigma^3,\;
\bar\sigma^0\sigma^1\bar\sigma^2\sigma^3)
=\operatorname{diag}(i\mathbf1_2,\,-i\mathbf1_2)\), hence

$$
\gamma_5
=\begin{pmatrix}-\delta_a{}^b&0\\0&+\delta^{\dot a}{}_{\dot b}\end{pmatrix},
\qquad
\gamma_5^2=\mathbf1_4,
\qquad
\{\gamma_5,\gamma_L^\mu\}=\{\gamma_5,\gamma_E^m\}=0 .
\tag{4D.9}
$$

The Euclidean chirality matrix is defined so that the chiral blocks
continue across the Wick map,

$$
\boxed{
\gamma_{5E}:=-\gamma_E^1\gamma_E^2\gamma_E^3\gamma_E^4=\gamma_5 ,}
\tag{4D.10}
$$

using (4D.7):
\(\gamma_E^1\gamma_E^2\gamma_E^3\gamma_E^4
=(-i\gamma^1)(-i\gamma^2)(-i\gamma^3)\gamma^0
=i\,\gamma^1\gamma^2\gamma^3\gamma^0
=-i\,\gamma^0\gamma^1\gamma^2\gamma^3
=-\gamma_5\),
the last step moving \(\gamma^0\) through three gamma matrices.
One chirality matrix therefore serves both signatures, and

$$
\boxed{
P_L:=\frac{1-\gamma_5}{2}
=\begin{pmatrix}\delta_a{}^b&0\\0&0\end{pmatrix},
\qquad
P_R:=\frac{1+\gamma_5}{2}
=\begin{pmatrix}0&0\\0&\delta^{\dot a}{}_{\dot b}\end{pmatrix},}
\tag{4D.11}
$$

$$
P_L^2=P_L,\qquad P_R^2=P_R,\qquad P_LP_R=0,\qquad P_L+P_R=\mathbf1_4 .
\tag{4D.12}
$$

\(P_L\) selects the lower-undotted (left-handed) block and \(P_R\)
the upper-dotted (right-handed) block of (4D.2).  Normalized
antisymmetric products carry the same normalization as the dictionary
symbol (D.3.9),

$$
\Gamma_\bullet^{\mu_1\cdots\mu_r}
:=\frac1{r!}\sum_{\pi\in S_r}\operatorname{sgn}(\pi)
\gamma_\bullet^{\mu_{\pi(1)}}\cdots\gamma_\bullet^{\mu_{\pi(r)}},
\tag{4D.13}
$$

so that, with the Step-1 products (1.14)--(1.15) and (1.55)--(1.56),

$$
\boxed{
\Gamma_L^{\mu\nu}
=\frac12[\gamma_L^\mu,\gamma_L^\nu]
=\begin{pmatrix}2(\sigma_L^{\mu\nu})_a{}^b&0\\
0&2(\bar\sigma_L^{\mu\nu})^{\dot a}{}_{\dot b}\end{pmatrix},
\qquad
\Gamma_E^{mn}
=\begin{pmatrix}2(\sigma_E^{mn})_a{}^b&0\\
0&2(\bar\sigma_E^{mn})^{\dot a}{}_{\dot b}\end{pmatrix}.}
\tag{4D.14}
$$

The four-component spin matrix is

$$
\mathcal S_R^{MN}:=\frac12\Gamma_R^{MN}
=\operatorname{diag}(\sigma_R^{MN},\bar\sigma_R^{MN}),
\tag{4D.15}
$$

and the Step-1 Lorentz actions (1.29)--(1.31) and (1.63)--(1.64)
assemble to

$$
[J_L^{\mu\nu},\mathcal Q_\alpha^L]
=-i(\mathcal S_L^{\mu\nu}\mathcal Q^L)_\alpha,
\qquad
[J_E^{mn},\mathcal Q_\alpha^E]
=+i(\mathcal S_E^{mn}\mathcal Q^E)_\alpha,
\tag{4D.16}
$$

for the supercharge packages of Section 4D.11.

### 4D.3 Gamma technology

All identities in this section are stated at \(d=4\) and are exact
matrix identities over \(\mathbb Q(i)\); each is machine-checked
(check `gamma_clifford_chirality_traces`).  Contractions use
\(\eta_{\mu\nu}\) from (1.2):

$$
\gamma_L^\mu\gamma_{L\mu}=-4\cdot\mathbf1_4,
\qquad
\gamma_L^\mu\gamma_L^\nu\gamma_{L\mu}=+2\gamma_L^\nu,
\qquad
\gamma_L^\mu\gamma_L^\nu\gamma_L^\rho\gamma_{L\mu}
=+4\eta^{\nu\rho}\mathbf1_4,
\tag{4D.17}
$$

matching the dictionary family (D.3.25)--(D.3.26) at
\(\kappa_C=-1\).  The traces are

$$
\begin{gathered}
\operatorname{tr}\gamma_L^\mu
=\operatorname{tr}\gamma_5
=\operatorname{tr}(\gamma_5\gamma_L^\mu)=0,\\
\operatorname{tr}(\gamma_L^\mu\gamma_L^\nu)=-4\eta^{\mu\nu},
\qquad
\operatorname{tr}(\gamma_E^m\gamma_E^n)=+4\delta^{mn},\\
\operatorname{tr}(\gamma_L^\mu\gamma_L^\nu\gamma_L^\rho\gamma_L^\sigma)
=4(\eta^{\mu\nu}\eta^{\rho\sigma}
-\eta^{\mu\rho}\eta^{\nu\sigma}
+\eta^{\mu\sigma}\eta^{\nu\rho}),\\
\operatorname{tr}(\gamma_5\gamma_L^\mu\gamma_L^\nu\gamma_L^\rho\gamma_L^\sigma)
=-4i\epsilon_L^{\mu\nu\rho\sigma},
\qquad
\operatorname{tr}(\gamma_5\gamma_E^m\gamma_E^n\gamma_E^r\gamma_E^s)
=-4\epsilon_E^{mnrs},
\end{gathered}
\tag{4D.18}
$$

with \(\epsilon_L^{0123}=+1\) from (1.2) and
\(\epsilon_E^{1234}=+1\).  The duality identities are

$$
\Gamma_L^{\mu\nu\rho}
=i\epsilon_L^{\mu\nu\rho\sigma}\gamma_5\gamma_{L\sigma},
\qquad
\Gamma_L^{\mu\nu\rho\sigma}
=-i\epsilon_L^{\mu\nu\rho\sigma}\gamma_5,
\qquad
\gamma_5\Gamma_L^{\mu\nu}
=+\frac i2\epsilon_L^{\mu\nu\rho\sigma}\Gamma_{L,\rho\sigma},
\tag{4D.19}
$$

again the \(\kappa_C=-1\) branch of (D.3.30)--(D.3.31).

### 4D.4 \(\beta\) and hermiticity

Define, with distinct index structure from \(\gamma^0\)
(numerically equal),

$$
\boxed{
\beta:=\begin{pmatrix}0&\delta^{\dot a}{}_{\dot b}\\
\delta_a{}^b&0\end{pmatrix},}
\qquad
\beta^2=\mathbf1_4,
\qquad
\beta^\dagger=\beta .
\tag{4D.20}
$$

Direct conjugation of (4D.3) gives the \(\kappa_C=-1\) hermiticity
branch of (D.3.11),

$$
\boxed{
(\gamma_L^\mu)^\dagger=\beta\gamma_L^\mu\beta^{-1},}
\qquad
(\gamma_E^m)^\dagger=\gamma_E^m ,
\tag{4D.21}
$$

together with the derived table (check `beta_hermiticity`)

$$
\gamma_5^\dagger=\gamma_5=-\beta\gamma_5\beta^{-1},
\qquad
(\gamma_5\gamma_L^\mu)^\dagger=+\beta(\gamma_5\gamma_L^\mu)\beta^{-1},
\qquad
(\Gamma_L^{\mu\nu})^\dagger=-\beta\Gamma_L^{\mu\nu}\beta^{-1}.
\tag{4D.22}
$$

### 4D.5 Charge conjugation

The Project charge-conjugation matrix is fixed on the Srednicki
branch,

$$
\boxed{
\mathcal C
:=\begin{pmatrix}\epsilon_{ab}&0\\0&\epsilon^{\dot a\dot b}\end{pmatrix}
=\begin{pmatrix}0&-1&&\\1&0&&\\&&0&1\\&&-1&0\end{pmatrix},}
\tag{4D.23}
$$

with the Step-1 epsilon values (1.3)--(1.4).  Matrix multiplication
gives (check `charge_conjugation_majorana`)

$$
\boxed{
\mathcal C^{\rm T}=\mathcal C^\dagger=\mathcal C^{-1}=-\mathcal C,
\qquad
\mathcal C^2=-\mathbf1_4 .}
\tag{4D.24}
$$

Conjugating (4D.3) with (4D.23) turns every epsilon contraction into
a Step-1 raising or lowering on the first index, which produces one
sign per block, hence

$$
\boxed{
\mathcal C^{-1}\gamma_L^\mu\mathcal C=-(\gamma_L^\mu)^{\rm T},
\qquad
\mathcal C^{-1}\gamma_E^m\mathcal C=-(\gamma_E^m)^{\rm T}.}
\tag{4D.25}
$$

The complete transposition table, valid in both signatures, is

$$
\mathcal C^{-1}M\mathcal C=\eta_M M^{\rm T},
\qquad
\eta_M=
\begin{cases}
+1,&M\in\{\mathbf1,\ \gamma_5,\ \gamma_5\gamma^\mu\},\\[1mm]
-1,&M\in\{\gamma^\mu,\ \Gamma^{\mu\nu}\}.
\end{cases}
\tag{4D.26}
$$

One matrix \(\mathcal C\) serves the Lorentzian and the Euclidean
system; no second Euclidean conjugation matrix is introduced.

### 4D.6 Majorana packaging and reality (Lorentzian)

For a Lorentzian Weyl spinor \(\psi_a\) with conjugate
\(\bar\psi_{\dot a}:=(\psi_a)^\dagger\), define the Majorana package

$$
\boxed{
\Psi[\psi]
:=\begin{pmatrix}\psi_a\\ \bar\psi^{\dot a}\end{pmatrix},
\qquad
\bar\Psi:=\Psi^\dagger\beta .}
\tag{4D.27}
$$

Since \((\bar\psi^{\dot a})^\dagger=\psi^a\), the bar row is

$$
\bar\Psi=(\psi^a,\ \bar\psi_{\dot a}).
\tag{4D.28}
$$

The same row follows from the transpose:
\(\psi_c\epsilon_{cb}=\psi^b\) and
\(\bar\psi^{\dot c}\epsilon^{\dot c\dot b}=\bar\psi_{\dot b}\)
by (1.3)--(1.5), hence the Project (Srednicki-branch) Majorana
condition

$$
\boxed{
\bar\Psi=\Psi^{\rm T}\mathcal C
\qquad\Longleftrightarrow\qquad
\Psi=\mathcal C\bar\Psi^{\rm T},}
\tag{4D.29}
$$

and, componentwise (check `charge_conjugation_majorana`),

$$
\boxed{\Psi^*=-\beta\mathcal C\Psi .}
\tag{4D.30}
$$

The locked dictionary records the opposite Weinberg branch,
\(\bar\Psi_{M,W}=-\Psi_{M,W}^{\rm T}\mathcal C\) and
\(\Psi_{M,W}^*=+\beta\mathcal C\Psi_{M,W}\) (D.3.16), with the
inter-branch phase \(\Psi_{M,W}=+i\Psi_{M,S}\) (D.3.18); Section
4D.17 fixes the Project column of that dictionary.

For two Weyl spinors \((\chi,\xi)\) the Dirac package is

$$
\Psi_D[\chi,\xi]
:=\begin{pmatrix}\chi_a\\ \bar\xi^{\dot a}\end{pmatrix},
\qquad
\bar\Psi_D=(\xi^a,\ \bar\chi_{\dot a}),
\qquad
\Psi_D^{\rm c}:=\mathcal C\bar\Psi_D^{\rm T}
=\begin{pmatrix}\xi_a\\ \bar\chi^{\dot a}\end{pmatrix},
\tag{4D.31}
$$

so charge conjugation exchanges \(\chi\leftrightarrow\xi\) and the
Majorana package (4D.27) is exactly its fixed point.

For an arbitrary four-component column \(X\) the transpose bar

$$
\bar X:=X^{\rm T}\mathcal C
\tag{4D.32}
$$

is defined without any conjugation.  On Lorentzian Majorana packages
(4D.29) states that the transpose bar and the dagger bar coincide;
the Euclidean system of Section 4D.7 uses only (4D.32).

### 4D.7 Euclidean Majorana-parallel packaging

In Euclidean signature the two Weyl families are independent — (1.68)
imposes no dagger relation, and (4.14) keeps
\((\lambda_a,\widetilde\lambda_{\dot a})\) independent.  The
Euclidean four-component package of an independent pair
\((\psi_a,\widetilde\psi_{\dot a})\) is

$$
\boxed{
\Psi_E[\psi,\widetilde\psi]
:=\begin{pmatrix}\psi_a\\ \widetilde\psi^{\dot a}\end{pmatrix},
\qquad
\bar\Psi_E:=\Psi_E^{\rm T}\mathcal C
=(\psi^a,\ \widetilde\psi_{\dot a}).}
\tag{4D.33}
$$

No Euclidean reality condition is imposed: (4D.33) is packaging, not
a contour.  Under the Lorentzian contour
\(\widetilde\psi\to\bar\psi=(\psi)^\dagger\) it reduces exactly to
(4D.27)--(4D.29).  Every Euclidean four-component formula below is
built from (4D.33), so all Euclidean statements remain
holomorphic in the independent fields, as required by the Step-4
Euclidean slot rules.

### 4D.8 Bilinear dictionary

For two independent packages
\(\Psi_1=\Psi[\chi]\), \(\Psi_2=\Psi[\psi]\) (Lorentzian) or their
tilde analogs (Euclidean), the sixteen bilinears reduce to Step-1
contractions (1.6) as follows (check `bilinear_dictionary`):

$$
\boxed{
\begin{aligned}
\bar\Psi_1\Psi_2&=\chi\psi+\bar\chi\bar\psi,\\
\bar\Psi_1\gamma_5\Psi_2&=-\chi\psi+\bar\chi\bar\psi,\\
\bar\Psi_1\gamma_L^\mu\Psi_2
&=\chi\sigma_L^\mu\bar\psi+\bar\chi\bar\sigma_L^\mu\psi,\\
\bar\Psi_1\gamma_L^\mu\gamma_5\Psi_2
&=\chi\sigma_L^\mu\bar\psi-\bar\chi\bar\sigma_L^\mu\psi,\\
\bar\Psi_1\Gamma_L^{\mu\nu}\Psi_2
&=2\chi\sigma_L^{\mu\nu}\psi+2\bar\chi\bar\sigma_L^{\mu\nu}\bar\psi,
\end{aligned}}
\tag{4D.34}
$$

where
\(\chi\sigma^\mu\bar\psi:=\chi^a(\sigma^\mu)_{a\dot b}\bar\psi^{\dot b}\),
\(\bar\chi\bar\sigma^\mu\psi:=\bar\chi_{\dot a}(\bar\sigma^\mu)^{\dot ab}\psi_b\),
\(\chi\sigma^{\mu\nu}\psi:=\chi^a(\sigma^{\mu\nu})_a{}^b\psi_b\), and
\(\bar\chi\bar\sigma^{\mu\nu}\bar\psi
:=\bar\chi_{\dot a}(\bar\sigma^{\mu\nu})^{\dot a}{}_{\dot b}\bar\psi^{\dot b}\).
The identical statements hold with
\(\sigma_E,\bar\sigma_E,\sigma_E^{mn},\bar\sigma_E^{mn}\) and tilde
fields in Euclidean signature.  Combining (4D.22) with the flip table
(4D.35) shows that, for Lorentzian Majorana packages,
\(\bar\Psi_1\Psi_2\), \(\bar\Psi_1\gamma_5\gamma^\mu\Psi_2\), and
\(\bar\Psi_1\Gamma^{\mu\nu}\Psi_2\) are hermitian while
\(\bar\Psi_1\gamma_5\Psi_2\) and \(\bar\Psi_1\gamma^\mu\Psi_2\) are
antihermitian; this is what makes (4D.42) hermitian up to a boundary
term.

### 4D.9 Flip and Fierz identities

For anticommuting Majorana packages (both signatures; check
`majorana_flips`),

$$
\boxed{
\bar\Psi_1M\Psi_2
=\begin{cases}
+\bar\Psi_2M\Psi_1,
&M\in\{\mathbf1,\ \gamma_5,\ \gamma_5\gamma^\mu\},\\[1mm]
-\bar\Psi_2M\Psi_1,
&M\in\{\gamma^\mu,\ \Gamma^{\mu\nu}\},
\end{cases}}
\tag{4D.35}
$$

which is the transposition table (4D.26) applied inside
\(\bar\Psi_1M\Psi_2=(\Psi_1)^{\rm T}\mathcal CM\Psi_2\).  In
particular, for a single package,

$$
\bar\Psi\gamma^\mu\Psi=0,
\qquad
\bar\Psi\gamma^\mu\gamma_5\Psi=-2\bar\psi\bar\sigma^\mu\psi
\quad(\text{and }=-2\widetilde\psi\bar\sigma_E^m\psi\ \text{in }E).
\tag{4D.36}
$$

The Project Majorana Fierz identity is the Srednicki branch of
(D.3.33), now a Project theorem (check `majorana_fierz`):

$$
\boxed{
s_\alpha s_\beta
=+\frac14\mathcal C_{\alpha\beta}(\bar ss)
+\frac14(\gamma_5\mathcal C)_{\alpha\beta}(\bar s\gamma_5s)
+\frac14(\gamma_5\gamma_{L\mu}\mathcal C)_{\alpha\beta}
(\bar s\gamma_5\gamma_L^\mu s).}
\tag{4D.37}
$$

### 4D.10 Free Majorana dynamics

The free Lorentzian Majorana density on the Project branch is

$$
\boxed{
\mathcal L_M
=\frac i2\bar\Psi\gamma_L^\mu\partial_\mu\Psi
-\frac12m\bar\Psi\Psi .}
\tag{4D.38}
$$

Its exact two-component content is fixed by the boxed kinetic
identity (check `kinetic_equivalence`)

$$
\boxed{
i\bar\psi\bar\sigma_L^\mu\partial_\mu\psi
=\frac i2\bar\Psi\gamma_L^\mu\partial_\mu\Psi
-\frac i4\partial_\mu
\left(\bar\Psi\gamma_L^\mu\gamma_5\Psi\right),}
\tag{4D.39}
$$

together with \(\bar\Psi\Psi=\psi\psi+\bar\psi\bar\psi\), so that
(4D.38) equals the locked Weyl density
\(i\bar\psi\bar\sigma^\mu\partial_\mu\psi
-\tfrac12m(\psi\psi+\bar\psi\bar\psi)\)
up to the displayed total derivative.  The Euler operator of (4D.38)
is the block pair

$$
(-i\gamma_L^\mu\partial_\mu+m)\Psi=0
\quad\Longleftrightarrow\quad
\begin{cases}
-i(\sigma_L^\mu)_{a\dot b}\partial_\mu\bar\psi^{\dot b}+m\psi_a=0,\\
-i(\bar\sigma_L^\mu)^{\dot ab}\partial_\mu\psi_b+m\bar\psi^{\dot a}=0,
\end{cases}
\tag{4D.40}
$$

read off directly from (4D.3).  The Euclidean parallel, with the
independent package (4D.33) and no \(i\), is

$$
\boxed{
\widetilde\psi\bar\sigma_E^m\partial_m\psi
=\frac12\bar\Psi_E\gamma_E^m\partial_m\Psi_E
-\frac14\partial_m
\left(\bar\Psi_E\gamma_E^m\gamma_5\Psi_E\right).}
\tag{4D.41}
$$

### 4D.11 Majorana supercharges and the algebra

Package the Step-1 supercharges as

$$
\boxed{
\mathcal Q_R
:=\begin{pmatrix}Q_a^R\\ \bar Q_R^{\dot a}\end{pmatrix},
\qquad
\bar{\mathcal Q}_R:=\mathcal Q_R^{\rm T}\mathcal C
=(Q_R^a,\ \bar Q^R_{\dot a}),
\qquad R\in\{L,E\}.}
\tag{4D.42}
$$

In Lorentzian signature (1.25) makes (4D.42) a genuine Majorana
package; in Euclidean signature it is the packaging (4D.33) of the
two independent families.  The Step-1 algebras (1.39) and (1.68)
assemble blockwise — using
\(\{Q_a,Q_b\}=\{\bar Q_{\dot a},\bar Q_{\dot b}\}=0\) and
\((\bar\sigma_R^M)^{\dot ab}
=\epsilon^{bd}\epsilon^{\dot a\dot c}(\sigma_R^M)_{d\dot c}\) — into
one four-component statement each (check
`susy_algebra_superspace`):

$$
\boxed{
\{\mathcal Q_{L\alpha},\bar{\mathcal Q}_L^{\ \beta}\}
=-2(\gamma_L^\mu)_\alpha{}^\beta P^L_\mu,
\qquad
\{\mathcal Q_{E\alpha},\bar{\mathcal Q}_E^{\ \beta}\}
=-2(\gamma_E^m)_\alpha{}^\beta P^E_m .}
\tag{4D.43}
$$

For a Lorentzian Majorana parameter package
\(E=(\varepsilon_a,\bar\varepsilon^{\dot a})^{\rm T}\) with
\(\bar\varepsilon=(\varepsilon)^\dagger\), the Step-1 exponent (1.18)
takes the Weinberg-style one-term form

$$
\left.U_L\right|_{\rm ferm}
=1-i\varepsilon Q_L-i\bar\varepsilon\bar Q_L
=1-i\bar E\mathcal Q_L,
\tag{4D.44}
$$

since \(\bar E\mathcal Q=\varepsilon^aQ_a+\bar\varepsilon_{\dot a}\bar Q^{\dot a}\)
by (1.6).  The Euclidean exponent (1.58), with the independent pair
\(\Xi=(\theta_a,\bar\eta^{\dot a})^{\rm T}\), is
\(1+\bar\Xi\mathcal Q_E\); no Euclidean conjugation links the two
halves of \(\Xi\).

### 4D.12 Majorana superspace package

Package the Step-2A coordinates, coordinate generators (2A.21), and
covariant derivatives (2A.28) as

$$
\boxed{
\Theta:=\begin{pmatrix}\vartheta_a\\ \bar\vartheta^{\dot a}\end{pmatrix},
\qquad
\bar\Theta:=\Theta^{\rm T}\mathcal C=(\vartheta^a,\ \bar\vartheta_{\dot a}),
\qquad
\mathsf Q_R^{(4)}
:=\begin{pmatrix}\mathsf Q_a^R\\ \bar{\mathsf Q}_R^{\dot a}\end{pmatrix},
\qquad
\mathbb D_R
:=\begin{pmatrix}D_a^R\\ \bar D_R^{\dot a}\end{pmatrix}.}
\tag{4D.45}
$$

The same block assembly as (4D.43), applied to (2A.25), (2A.29), and
their Euclidean rows (2A.38 ff.; dictionary (D.5.2)), gives

$$
\{\mathbb D_{L\alpha},\bar{\mathbb D}_L^{\ \beta}\}
=+2i(\gamma_L^\mu)_\alpha{}^\beta\partial_\mu^L
=-2(\gamma_L^\mu)_\alpha{}^\beta\mathsf P^L_\mu,
\qquad
\{\mathbb D_{E\alpha},\bar{\mathbb D}_E^{\ \beta}\}
=-2(\gamma_E^m)_\alpha{}^\beta\partial_m^E .
\tag{4D.46}
$$

Chirality is projector-diagonal: for any superfield \(\Phi\),

$$
\bar D_{R\dot a}\Phi=0
\ \Longleftrightarrow\
(P_R\,\mathbb D_R)\Phi=0,
\qquad
D_{Ra}\widetilde\Phi=0
\ \Longleftrightarrow\
(P_L\,\mathbb D_R)\widetilde\Phi=0 .
\tag{4D.47}
$$

The Grassmann monomial dictionary — with
\(\vartheta\vartheta:=\vartheta^a\vartheta_a\),
\(\bar\vartheta\bar\vartheta:=\bar\vartheta_{\dot a}\bar\vartheta^{\dot a}\),
and \(B_R^M=\vartheta\sigma_R^M\bar\vartheta\) from (2A.7) — is
(check `susy_algebra_superspace`)

$$
\boxed{
\begin{gathered}
\bar\Theta P_L\Theta=\vartheta\vartheta,
\qquad
\bar\Theta P_R\Theta=\bar\vartheta\bar\vartheta,
\qquad
\bar\Theta\gamma_5\Theta
=\bar\vartheta\bar\vartheta-\vartheta\vartheta,\\
\bar\Theta\gamma_5\gamma_R^M\Theta=-2B_R^M,
\qquad
(\bar\Theta\gamma_5\Theta)^2
=-2\,\vartheta\vartheta\,\bar\vartheta\bar\vartheta,
\qquad
(\bar\Theta P_L\Theta)(\bar\Theta P_R\Theta)
=\vartheta\vartheta\,\bar\vartheta\bar\vartheta .
\end{gathered}}
\tag{4D.48}
$$

The chiral coordinates (2A.31) and their Euclidean partners
(dictionary (D.5.3)) therefore read

$$
\boxed{
y_L^\mu=x_L^\mu+\frac i2\bar\Theta\gamma_5\gamma_L^\mu\Theta,
\qquad
\bar y_L^\mu=x_L^\mu-\frac i2\bar\Theta\gamma_5\gamma_L^\mu\Theta,}
\tag{4D.49}
$$

$$
y_E^m=x_E^m-\frac12\bar\Theta\gamma_5\gamma_E^m\Theta,
\qquad
\bar y_E^m=x_E^m+\frac12\bar\Theta\gamma_5\gamma_E^m\Theta .
\tag{4D.50}
$$

### 4D.13 Superfield projections in Majorana form

With the fermion package \(\Psi=\Psi[\psi]\) (Lorentzian) or
\(\Psi_E[\psi,\widetilde\psi]\) (Euclidean), the locked Step-3B
chiral expansions take the Weinberg-parallel form

$$
\boxed{
\Phi=\phi(y_R)+\sqrt2\,\bar\Theta P_L\Psi(y_R)
+(\bar\Theta P_L\Theta)F(y_R),}
\tag{4D.51}
$$

$$
\boxed{
\widetilde\Phi=\widetilde\phi(\bar y_R)
+\sqrt2\,\bar\Theta P_R\Psi(\bar y_R)
+(\bar\Theta P_R\Theta)\widetilde F(\bar y_R),}
\tag{4D.52}
$$

since \(\bar\Theta P_L\Psi=\vartheta\psi\) and
\(\bar\Theta P_R\Psi=\bar\vartheta\bar\psi\)
(\(=\bar\vartheta\widetilde\psi\) in \(E\)); both identities are
machine-checked.  The Wess--Zumino vector superfields (3B.27) become

$$
\boxed{
\begin{aligned}
\mathcal V_L={}&(\bar\Theta\gamma_5\gamma_L^\mu\Theta)A_\mu
+2i(\bar\Theta P_L\Theta)(\bar\Theta P_R\Psi_\lambda)
-2i(\bar\Theta P_R\Theta)(\bar\Theta P_L\Psi_\lambda)\\
&+(\bar\Theta P_L\Theta)(\bar\Theta P_R\Theta)\mathscr D,\\[1mm]
\mathcal V_E={}&i(\bar\Theta\gamma_5\gamma_E^m\Theta)A_m
+2i(\bar\Theta P_L\Theta)(\bar\Theta P_R\Psi_\lambda)
-2i(\bar\Theta P_R\Theta)(\bar\Theta P_L\Psi_\lambda)\\
&+(\bar\Theta P_L\Theta)(\bar\Theta P_R\Theta)\mathscr D,
\end{aligned}}
\tag{4D.53}
$$

with \(\Psi_\lambda:=\Psi[\lambda]\) in \(L\) and
\(\Psi_\lambda:=\Psi_E[\lambda,\widetilde\lambda]\) in \(E\).  The
\(F\)- and \(D\)-projections of Step 3B are unchanged: \([\,\cdot\,]_F\)
is the coefficient of \(\bar\Theta P_L\Theta\) in the chiral frame and
\([\,\cdot\,]_D\) the coefficient of
\((\bar\Theta P_L\Theta)(\bar\Theta P_R\Theta)\), by (4D.48).

### 4D.14 \(\mathcal N=1\) vector multiplet in Majorana form

For the \(\mathcal N=1\) multiplet (4.12) define

$$
\Psi_\lambda^A:=
\begin{cases}
(\lambda_a^A,\ \bar\lambda^{A\dot a})^{\rm T},&R=L,\\[1mm]
(\lambda_a^A,\ \widetilde\lambda^{A\dot a})^{\rm T},&R=E .
\end{cases}
\tag{4D.54}
$$

The pure-\(\mathcal N=1\) restriction (\(\Phi_r=0\)) of the locked
component actions (4C.14) and (4C.42a), rewritten with (4D.39) and
(4D.41), is

$$
\boxed{
\begin{aligned}
\mathcal L_L^{(1)}
={}&h\operatorname{tr}_\kappa\Big[
-\frac14F_{\mu\nu}F^{\mu\nu}
+\frac i2\bar\Psi_\lambda\gamma_L^\mu\mathcal D_\mu\Psi_\lambda
+\frac12\mathscr D\mathscr D\Big]
-\frac18\mathfrak k_{AB}
\epsilon_L^{\mu\nu\rho\sigma}F^A_{\mu\nu}F^B_{\rho\sigma}\\
&-\frac i4\partial_\mu\left[h\operatorname{tr}_\kappa
(\bar\Psi_\lambda\gamma_L^\mu\gamma_5\Psi_\lambda)\right],\\[1mm]
\mathcal L_E^{(1)}
={}&h\operatorname{tr}_\kappa\Big[
+\frac14F_{mn}F_{mn}
+\frac12\bar\Psi_\lambda\gamma_E^m\mathcal D_m\Psi_\lambda
-\frac12\mathscr D\mathscr D\Big]
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}\\
&-\frac14\partial_m\left[h\operatorname{tr}_\kappa
(\bar\Psi_\lambda\gamma_E^m\gamma_5\Psi_\lambda)\right],
\end{aligned}}
\tag{4D.55}
$$

with every boundary term displayed.  The locked transformations
(4A.26)--(4A.27) assemble, using the bilinear dictionary (4D.34) and
the raising lemma of Section 4D.16, into

$$
\boxed{
\begin{aligned}
\delta_LA_\mu&=-i\bar E\gamma_{L\mu}\Psi_\lambda,\\
\delta_L\Psi_\lambda
&=\frac12F_{\mu\nu}\Gamma_L^{\mu\nu}E+i\gamma_5E\,\mathscr D,\\
\delta_L\mathscr D
&=-\bar E\gamma_L^\mu\gamma_5\mathcal D_\mu\Psi_\lambda,
\end{aligned}}
\qquad
\boxed{
\begin{aligned}
\delta_EA_m&=\bar E\gamma_{E m}\Psi_\lambda,\\
\delta_E\Psi_\lambda
&=-\frac12F_{mn}\Gamma_E^{mn}E+i\gamma_5E\,\mathscr D,\\
\delta_E\mathscr D
&=-i\bar E\gamma_E^m\gamma_5\mathcal D_m\Psi_\lambda .
\end{aligned}}
\tag{4D.56}
$$

Here \(E\) is the parameter package of (4D.44) in \(L\) and the
independent-pair package in \(E\).  Equations (4D.56) are the
\(\mathcal I=4\), \(\varphi=0\) restriction of the machine-checked
\(\mathcal N=4\) statements (4D.64)--(4D.66); the \(\mathscr D\)-rows
follow from the axial row of (4D.34).

### 4D.15 \(\mathcal N=2\) doublet packaging

For the \(\mathcal N=2\) fermions (4.16)--(4.17) define the chirally
split doublet packages

$$
\Psi_i:=
\begin{cases}
(\chi_{ia},\ \bar\chi^{i\dot a})^{\rm T},&R=L,\\[1mm]
(\chi_{ia},\ \widetilde\chi^{i\dot a})^{\rm T},&R=E,
\end{cases}
\qquad i=1,2,
\tag{4D.57}
$$

with the \(SU(2)_R\) label lower on the \(P_L\) half and upper on the
\(P_R\) half; \(SU(2)_R\) acts on the two halves in conjugate
representations, and epsilon raising (4.15) acts inside each half.
This is the same chirally split label rule declared in (4D.59) for
\(\mathcal N=4\); all \(\mathcal N=2\) bilinears then reduce by
(4D.34).  The full \(\mathcal N=2\) action and transformation rewrite
is the \(\mathcal I\in\{3,4\}\)-restriction pattern of Section 4D.16
and is not duplicated here.

### 4D.16 \(\mathcal N=4\) super Yang--Mills in Majorana form

#### 4D.16.1 Chirally split packages

For the Step-4 fermions (4.27)--(4.27a) define the chiral halves and
the Majorana package

$$
\boxed{
\lambda^{\mathcal I}
:=\begin{pmatrix}\Lambda_a^{\mathcal I}\\ 0\end{pmatrix},
\qquad
\lambda_{\mathcal I}
:=\begin{cases}
(0,\ \bar\Lambda_{\mathcal I}^{\dot a})^{\rm T},&R=L,\\[1mm]
(0,\ \widetilde\Lambda_{\mathcal I}^{\dot a})^{\rm T},&R=E,
\end{cases}
\qquad
\Psi^{\mathcal I}:=\lambda^{\mathcal I}+\lambda_{\mathcal I},}
\tag{4D.58}
$$

with transpose bars (4D.32)

$$
\bar\lambda^{\mathcal I}
=(\Lambda^{\mathcal Ia},\ 0),
\qquad
\bar\lambda_{\mathcal I}
=(0,\ \bar\Lambda_{\dot a\mathcal I})
\ \big[=(0,\ \widetilde\Lambda_{\dot a\mathcal I})\ \text{in }E\big],
\qquad
\bar\Psi_{\mathcal I}
:=\bar\lambda^{\mathcal I}+\bar\lambda_{\mathcal I}.
\tag{4D.59}
$$

The **chirally split label rule** is declared here once: on a
four-component \(\mathcal N=4\) object the \(SU(4)_R\) label sits
upper on the \(P_L\) half and lower on the \(P_R\) half (and the bars
reverse both); \(SU(4)_R\) acts on the two halves in conjugate
representations, exactly as on
\((\Lambda^{\mathcal I},\bar\Lambda_{\mathcal I})\) in (4.30).  In
Lorentzian signature (4.30) makes each \(\Psi^{\mathcal I}\) a
Majorana package,
\(\bar\Psi_{\mathcal I}=(\Psi^{\mathcal I})^\dagger\beta
=(\Psi^{\mathcal I})^{\rm T}\mathcal C\); in Euclidean signature
(4D.58) is the independent packaging (4D.33).  The projected
bilinears are exactly the Step-4C contractions (check
`n4_action_fermion_sector`):

$$
\boxed{
\bar\lambda^{\mathcal I}\lambda^{\mathcal J}
=\Lambda^{\mathcal I}\Lambda^{\mathcal J},
\qquad
\bar\lambda_{\mathcal I}\lambda_{\mathcal J}
=\bar\Lambda_{\mathcal I}\bar\Lambda_{\mathcal J},
\qquad
\bar\lambda^{\mathcal I}\lambda_{\mathcal J}
=\bar\lambda_{\mathcal I}\lambda^{\mathcal J}=0,
\qquad
\bar\lambda_{\mathcal I}\gamma_R^M\mathcal D_M\lambda^{\mathcal I}
=\bar\Lambda_{\mathcal I}\bar\sigma_R^M\mathcal D_M\Lambda^{\mathcal I}.}
\tag{4D.60}
$$

#### 4D.16.2 The action

The fermion kinetic identity, summed over the multiplet (check
`n4_action_fermion_sector`), is

$$
\boxed{
\begin{aligned}
ih\operatorname{tr}_\kappa\!\left(
\bar\Lambda_{\mathcal I}\bar\sigma_L^\mu
\mathcal D_\mu\Lambda^{\mathcal I}\right)
&=\frac i2h\operatorname{tr}_\kappa\!\left(
\bar\Psi_{\mathcal I}\gamma_L^\mu\mathcal D_\mu\Psi^{\mathcal I}\right)
-\frac i4\partial_\mu\!\left[h\operatorname{tr}_\kappa\!\left(
\bar\Psi_{\mathcal I}\gamma_L^\mu\gamma_5\Psi^{\mathcal I}\right)\right],\\
h\operatorname{tr}_\kappa\!\left(
\widetilde\Lambda_{\mathcal I}\bar\sigma_E^m
\mathcal D_m\Lambda^{\mathcal I}\right)
&=\frac12h\operatorname{tr}_\kappa\!\left(
\bar\Psi_{\mathcal I}\gamma_E^m\mathcal D_m\Psi^{\mathcal I}\right)
-\frac14\partial_m\!\left[h\operatorname{tr}_\kappa\!\left(
\bar\Psi_{\mathcal I}\gamma_E^m\gamma_5\Psi^{\mathcal I}\right)\right].
\end{aligned}}
\tag{4D.61}
$$

Substituting (4D.60)--(4D.61) into the locked on-shell actions
(4C.22) and (4C.43) gives the complete Majorana forms

$$
\boxed{
\begin{aligned}
\mathcal L_L^{(4)}={}&
h\kappa_{AB}\Big[
-\frac14F_{\mu\nu}^AF^{B\mu\nu}
-\frac14(\mathcal D_\mu\varphi^{\mathcal I\mathcal J})^A
(\mathcal D^\mu\widetilde\varphi_{\mathcal I\mathcal J})^B
+\frac i2\bar\Psi_{\mathcal I}^A\gamma_L^\mu
(\mathcal D_\mu\Psi^{\mathcal I})^B\\
&\qquad
-\frac1{16}
(\varphi^{\mathcal I\mathcal J}\times\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B\Big]\\
&+\frac h{\sqrt2}c_{ABC}\left(
\widetilde\varphi_{\mathcal I\mathcal J}^A\,
\bar\lambda^{\mathcal IB}\lambda^{\mathcal JC}
+\varphi^{\mathcal I\mathcal J,A}\,
\bar\lambda_{\mathcal I}^B\lambda_{\mathcal J}^C\right)
-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}
F^A_{\mu\nu}F^B_{\rho\sigma}\\
&-\frac i4\partial_\mu\!\left[h\operatorname{tr}_\kappa\!
\left(\bar\Psi_{\mathcal I}\gamma_L^\mu\gamma_5
\Psi^{\mathcal I}\right)\right],
\end{aligned}}
\tag{4D.62}
$$

$$
\boxed{
\begin{aligned}
\mathcal L_E^{(4)}={}&
h\kappa_{AB}\Big[
+\frac14F_{mn}^AF_{mn}^B
+\frac14(\mathcal D_m\varphi^{\mathcal I\mathcal J})^A
(\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J})^B
+\frac12\bar\Psi_{\mathcal I}^A\gamma_E^m
(\mathcal D_m\Psi^{\mathcal I})^B\\
&\qquad
+\frac1{16}
(\varphi^{\mathcal I\mathcal J}\times\varphi^{\mathcal K\mathcal L})^A
(\widetilde\varphi_{\mathcal I\mathcal J}\times
\widetilde\varphi_{\mathcal K\mathcal L})^B\Big]\\
&-\frac h{\sqrt2}c_{ABC}\left(
\widetilde\varphi_{\mathcal I\mathcal J}^A\,
\bar\lambda^{\mathcal IB}\lambda^{\mathcal JC}
+\varphi^{\mathcal I\mathcal J,A}\,
\bar\lambda_{\mathcal I}^B\lambda_{\mathcal J}^C\right)
-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}\\
&-\frac14\partial_m\!\left[h\operatorname{tr}_\kappa\!
\left(\bar\Psi_{\mathcal I}\gamma_E^m\gamma_5
\Psi^{\mathcal I}\right)\right],
\end{aligned}}
\tag{4D.63}
$$

with the total-derivative remainders displayed, never suppressed.
The scalar sector keeps its Step-4 packaging
(4.27)--(4.31) unchanged: no four-component object is needed there.

#### 4D.16.3 The sixteen transformations

Package the parameters chirally,
\(e^{\mathcal I}:=(\varepsilon_a^{\mathcal I},0)^{\rm T}\),
\(e_{\mathcal I}:=(0,\bar\varepsilon_{\mathcal I}^{\dot a})^{\rm T}\)
(Lorentzian; \(\widetilde\varepsilon\) in \(E\) by (4.34a)), with
transpose bars \(\bar e^{\mathcal I}=(\varepsilon^{\mathcal Ia},0)\),
\(\bar e_{\mathcal I}=(0,\bar\varepsilon_{\dot a\mathcal I})\), and
\(E^{\mathcal I}:=e^{\mathcal I}+e_{\mathcal I}\).  The raising lemma
used throughout is: for every \(\bar\sigma_R^{MN}\) the matrix
\((\bar\sigma_R^{MN})^{\dot a}{}_{\dot c}\epsilon^{\dot c\dot b}\) is
symmetric, so a left-acting lowered dotted row assembles into the
right-acting raised column of the same \(\Gamma\)-block; it is checked
inside `n4_sixteen_transformations`.  The locked transformations
(4C.24)--(4C.27) are then exactly (all sixteen components machine-checked)

$$
\boxed{
\begin{aligned}
\delta_LA_\mu
&=-i\left(\bar e^{\mathcal I}\gamma_{L\mu}\lambda_{\mathcal I}
+\bar e_{\mathcal I}\gamma_{L\mu}\lambda^{\mathcal I}\right),\\
\delta_L\varphi^{\mathcal I\mathcal J}
&=\sqrt2\left(\bar e^{\mathcal I}\lambda^{\mathcal J}
-\bar e^{\mathcal J}\lambda^{\mathcal I}\right)
+\sqrt2\,\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}\,
\bar e_{\mathcal K}\lambda_{\mathcal L},\\
\delta_L\Psi^{\mathcal I}
&=\frac12F_{\mu\nu}\Gamma_L^{\mu\nu}E^{\mathcal I}
+i\sqrt2\,\gamma_L^\mu\!\left(
e_{\mathcal J}\,\mathcal D_\mu\varphi^{\mathcal I\mathcal J}
+e^{\mathcal J}\,\mathcal D_\mu\widetilde\varphi_{\mathcal I\mathcal J}
\right)\\
&\quad
+\mathcal M^{\mathcal I}{}_{\mathcal K}\,e^{\mathcal K}
+\widetilde{\mathcal M}_{\mathcal I}{}^{\mathcal K}\,e_{\mathcal K},
\end{aligned}}
\tag{4D.64}
$$

$$
\boxed{
\begin{aligned}
\delta_EA_m
&=\bar e^{\mathcal I}\gamma_{Em}\lambda_{\mathcal I}
+\bar e_{\mathcal I}\gamma_{Em}\lambda^{\mathcal I},\\
\delta_E\varphi^{\mathcal I\mathcal J}
&=\sqrt2\left(\bar e^{\mathcal I}\lambda^{\mathcal J}
-\bar e^{\mathcal J}\lambda^{\mathcal I}\right)
+\sqrt2\,\epsilon^{\mathcal I\mathcal J\mathcal K\mathcal L}\,
\bar e_{\mathcal K}\lambda_{\mathcal L},\\
\delta_E\Psi^{\mathcal I}
&=-\frac12F_{mn}\Gamma_E^{mn}E^{\mathcal I}
-\sqrt2\,\gamma_E^m\!\left(
e_{\mathcal J}\,\mathcal D_m\varphi^{\mathcal I\mathcal J}
+e^{\mathcal J}\,\mathcal D_m\widetilde\varphi_{\mathcal I\mathcal J}
\right)\\
&\quad
+\mathcal M^{\mathcal I}{}_{\mathcal K}\,e^{\mathcal K}
+\widetilde{\mathcal M}_{\mathcal I}{}^{\mathcal K}\,e_{\mathcal K},
\end{aligned}}
\tag{4D.65}
$$

with \(\mathcal M^{\mathcal I}{}_{\mathcal K}\) from (4C.23) and
\(\widetilde{\mathcal M}_{\mathcal I}{}^{\mathcal K}
=-\mathcal M^{\mathcal K}{}_{\mathcal I}\) from (4C.55).  The scalar
variations \(\delta\widetilde\varphi_{\mathcal I\mathcal J}\) remain
fixed by duality, (4C.25a) and (4C.45a).  The equivalence statement
is exact:

$$
\text{(4D.64)}\equiv\text{(4C.24)--(4C.27)},
\qquad
\text{(4D.65)}\equiv\text{(4C.44)--(4C.47)},
\quad\text{componentwise.}
\tag{4D.66}
$$

#### 4D.16.4 Euler operators

The locked fermion Euler operators (4C.39)--(4C.40) and
(4C.68) assemble into single Dirac-form packages,

$$
\boxed{
\begin{aligned}
\mathfrak E_L^{\mathcal I}
&:=-i\gamma_L^\mu\mathcal D_\mu\Psi^{\mathcal I}
+\sqrt2\left(
\widetilde\varphi_{\mathcal I\mathcal J}\times\lambda^{\mathcal J}
+\varphi^{\mathcal I\mathcal J}\times\lambda_{\mathcal J}\right)
=\begin{pmatrix}
\mathcal E_{a\mathcal I}\\[1mm]
\epsilon^{\dot a\dot b}\,
\widetilde{\mathcal E}^{\mathcal I}_{\dot b}
\end{pmatrix},\\
\mathfrak E_E^{\mathcal I}
&:=\gamma_E^m\mathcal D_m\Psi^{\mathcal I}
+\sqrt2\left(
\widetilde\varphi_{\mathcal I\mathcal J}\times\lambda^{\mathcal J}
+\varphi^{\mathcal I\mathcal J}\times\lambda_{\mathcal J}\right)
=\begin{pmatrix}
\mathcal E_{E,a\mathcal I}\\[1mm]
\epsilon^{\dot a\dot b}\,
\widetilde{\mathcal E}_{E,\dot b}^{\mathcal I}
\end{pmatrix},
\end{aligned}}
\tag{4D.67}
$$

where the dotted rows use
\(\epsilon^{\dot a\dot b}(\bar\sigma_R^M)_{\dot bc}
=\epsilon_{ce}(\bar\sigma_R^M)^{\dot ae}\) and
\(\epsilon_{ce}\Lambda^c=-\Lambda_e\) from (1.5).  The on-shell
surface \(\mathcal E=\widetilde{\mathcal E}=0\) of (4C.56)--(4C.57)
and (4C.69f)--(4C.69g) is thus the single Majorana statement
\(\mathfrak E_R^{\mathcal I}=0\).

#### 4D.16.5 Supersymmetry-current packaging

Package the locked unimproved currents — (4C.59) with its conjugate
(4C.64b) in \(L\), and the boundary primitives (4C.66c3),
(4C.67b2) in \(E\) — as chirally split four-component columns
\(\mathcal J_{R,\mathcal I}^M
:=(j^M_{R,a\mathcal I},\ \bar j_R^{M\dot a\mathcal I})^{\rm T}\).
Both assemble into single gamma-matrix expressions (checked inside
`n4_sixteen_transformations`):

$$
\boxed{
\begin{aligned}
\mathcal J_{L,\mathcal I}^\mu
=h\operatorname{tr}_\kappa\Big[&
-\frac i2F_{\rho\sigma}\Gamma_L^{\rho\sigma}\gamma_L^\mu\gamma_5
\Psi^{\mathcal I}
+\sqrt2\,\gamma_L^\nu\gamma_L^\mu\!\left(
(\mathcal D_\nu\widetilde\varphi_{\mathcal I\mathcal J})
\lambda^{\mathcal J}
+(\mathcal D_\nu\varphi^{\mathcal I\mathcal J})
\lambda_{\mathcal J}\right)\\
&+i\gamma_L^\mu\!\left(
\mathcal M^{\mathcal J}{}_{\mathcal I}\lambda_{\mathcal J}
+\mathcal M^{\mathcal I}{}_{\mathcal J}\lambda^{\mathcal J}\right)
\Big],
\end{aligned}}
\tag{4D.68}
$$

$$
\boxed{
\begin{aligned}
\mathcal J_{E,\mathcal I}^m
=h\operatorname{tr}_\kappa\Big[&
+\frac12F_{rs}\Gamma_E^{rs}\gamma_E^m\gamma_5\Psi^{\mathcal I}
+\sqrt2\,\gamma_E^n\gamma_E^m\!\left(
(\mathcal D_n\widetilde\varphi_{\mathcal I\mathcal J})
\lambda^{\mathcal J}
+(\mathcal D_n\varphi^{\mathcal I\mathcal J})
\lambda_{\mathcal J}\right)\\
&+\gamma_E^m\!\left(
\mathcal M^{\mathcal J}{}_{\mathcal I}\lambda_{\mathcal J}
+\mathcal M^{\mathcal I}{}_{\mathcal J}\lambda^{\mathcal J}\right)
\Big].
\end{aligned}}
\tag{4D.69}
$$

The constant-parameter boundary contraction of (4C.58e) and
(4C.64b0) is then the single pairing
\(\mathcal S^\mu_{a\mathcal I}\varepsilon^{\mathcal Ia}
+\bar{\mathcal S}^{\mu\dot a\mathcal I}\bar\varepsilon_{\dot a\mathcal I}\),
i.e. the chirally split \(\bar{(\cdot)}E\)-pairing of
\(\mathcal J^\mu\) with the parameter package.  The topological
coefficient (4C.64)/(4C.64d) packages as the single vector bilinear

$$
\mathcal J_{\vartheta,L,\mathcal I}^\mu
=-i\mathfrak k_{AB}({}^{\star}F_L^A)^{\mu\nu}
\gamma_{L\nu}\Psi^{B\mathcal I},
\tag{4D.70}
$$

by the vector row of (4D.34).

### 4D.17 Book opposition and dictionary closure

The following rows fix the symbols left `UNFIXED` in (D.1.1) and
close the four-component column of the notation dictionary.
Numerically, with (D.2.4)--(D.2.5),

$$
\boxed{
\gamma_C^\mu:=\gamma_L^\mu=\gamma_S^\mu,
\qquad
\gamma_{5C}:=\gamma_5=\gamma_{5S}=-\gamma_{5W},
\qquad
\beta_C:=\beta=\beta_S,
\qquad
\mathcal C_C:=\mathcal C=\mathcal C_S=\mathcal C_W,}
\tag{4D.71}
$$

$$
\gamma_W^\mu=-i\gamma_C^\mu,
\qquad
P_+^W=P_L,
\qquad
P_-^W=P_R,
\tag{4D.72}
$$

by (D.3.2), (D.3.5), (D.3.6), (D.3.12).  The Project Majorana field
convention is the Srednicki branch of (D.3.15), so by (D.3.18)

$$
\Psi_C[\psi]=\Psi_{M,S},
\qquad
\Psi_{M,W}=+i\,\Psi_C[\psi],
\qquad
\bar\Psi_{M,W}=-i\,\bar\Psi_C[\psi],
\tag{4D.73}
$$

and the free densities correspond by (D.3.19):
\(\mathcal L_{M,C}=\mathcal L_{M,S}\) in the form (4D.38), against
Weinberg's
\(-\tfrac12\bar\Psi_W\gamma_W^\mu\partial_\mu\Psi_W
-\tfrac12m\bar\Psi_W\Psi_W\).
The Majorana superspace coordinate corresponds by (D.7.7):
\(\Theta_C=\Theta_S^{(4)}\), \(\Theta_W=-i\,\Theta_C\).  The flip
table (4D.35) reproduces (D.3.22); the Fierz identity (4D.37)
reproduces (D.3.33).  Every remaining dictionary row of (D.3.x) is
now two-sided: the Project column is fixed by this contract, and both
book columns remain as recorded.

### 4D.18 Verification anchors and completeness

The ten exact machine checks of
`scripts/verify_step4d_majorana_spinor_system.py`
(audit `audits/step4d-majorana-verification.json`) anchor the memo as
follows; every unlisted equation is a definition or a displayed
one-line consequence of listed ones.

$$
\begin{array}{l|l}
\text{check}&\text{memo equations}\\ \hline
\texttt{gamma\_clifford\_chirality\_traces}
&(4D.3)\text{--}(4D.14),\ (4D.17)\text{--}(4D.19)\\
\texttt{beta\_hermiticity}&(4D.20)\text{--}(4D.22)\\
\texttt{charge\_conjugation\_majorana}
&(4D.23)\text{--}(4D.30)\\
\texttt{bilinear\_dictionary}&(4D.34)\\
\texttt{majorana\_flips}&(4D.35)\text{--}(4D.36)\\
\texttt{majorana\_fierz}&(4D.37)\\
\texttt{kinetic\_equivalence}&(4D.38)\text{--}(4D.41)\\
\texttt{susy\_algebra\_superspace}
&(4D.43),\ (4D.46),\ (4D.48)\text{--}(4D.53)\\
\texttt{n4\_action\_fermion\_sector}&(4D.60)\text{--}(4D.63)\\
\texttt{n4\_sixteen\_transformations}
&(4D.56),\ (4D.64)\text{--}(4D.66),\ (4D.68)\text{--}(4D.69)
\end{array}
\tag{4D.74}
$$

The Weyl-to-Majorana completeness map over the locked contracts is:

$$
\begin{array}{l|l|l}
\text{locked Weyl object}&\text{equations}&\text{Majorana parallel}\\ \hline
\text{spinor slots, }\epsilon,\ \sigma_R
&(1.1)\text{--}(1.16),\ (1.51)\text{--}(1.57)
&(4D.2)\text{--}(4D.15)\\
\text{SUSY algebra}&(1.39),\ (1.68)&(4D.43)\\
\text{group exponent}&(1.18),\ (1.58)&(4D.44)\\
\text{superspace }\mathsf Q,D,y
&(2A.21),\ (2A.28),\ (2A.31),\ (D.5.2)\text{--}(D.5.3)
&(4D.45)\text{--}(4D.50)\\
\text{chiral/antichiral expansion}&(3B),\ (4C.30)\text{--}(4C.31)
&(4D.51)\text{--}(4D.52)\\
\text{Wess--Zumino vector}&(3B.27)&(4D.53)\\
\mathcal N=1\text{ action, transformations}
&(4C.14)|_{\Phi_r=0},\ (4C.42a)|_{\Phi_r=0},\ (4A.26)\text{--}(4A.27)
&(4D.54)\text{--}(4D.56)\\
\mathcal N=2\text{ fermion slots}&(4.16)\text{--}(4.17)&(4D.57)\\
\mathcal N=4\text{ fermion slots}&(4.27),\ (4.27a),\ (4.30)
&(4D.58)\text{--}(4D.60)\\
\mathcal N=4\text{ actions}&(4C.22),\ (4C.43)
&(4D.62)\text{--}(4D.63)\\
\mathcal N=4\text{ sixteen transformations}
&(4C.24)\text{--}(4C.27),\ (4C.44)\text{--}(4C.47)
&(4D.64)\text{--}(4D.65)\\
\mathcal N=4\text{ Euler operators}
&(4C.39)\text{--}(4C.40),\ (4C.68)&(4D.67)\\
\mathcal N=4\text{ currents}
&(4C.59),\ (4C.64b),\ (4C.66c3),\ (4C.67b2)
&(4D.68)\text{--}(4D.70)
\end{array}
\tag{4D.75}
$$

Superfield-level contracts (3A, 3D, 5, 5A) carry no independent
spinor-convention content beyond the objects listed above; their
two-component formulas translate through (4D.34) and
(4D.51)--(4D.53) without further choices.  The scalar and auxiliary
sectors of Steps 4, 4B, 4C are unchanged by this contract.
