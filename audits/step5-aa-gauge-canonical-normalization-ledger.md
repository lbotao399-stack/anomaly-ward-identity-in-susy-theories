# Step 5 ordered $AA$ pure-gauge canonical normalization ledger

Status: `AA_GAUGE_CANONICAL_NORMALIZATION_REDERIVED_TARGET_BLIND__MINUS_ONE_EIGHT_GENUINE_ON_CONDITIONAL_SLICE`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.

Scope: reconstruction from the exact all-order action and conditional
Fermi--Feynman inverse in `origin/main`.  No previous $AA$ coefficient and no
holomorphic-twist target enters the arithmetic.

## 1. Canonical coordinate and propagator

The Euclidean gauge coupling and exponent are

$$
h=g^{-2},
\qquad
\tau_E=-\frac1\hbar.
$$

The locked quadratic vector inverse is

$$
K_{E,AB}^{V}
=\frac h2\kappa_{AB}\Box_E.
$$

Define

$$
V=\sqrt2g\,u.
$$

Since $\Box_E\mapsto-p^2$, the canonical vector propagator is

$$
\boxed{
\langle u^A(p,1)u^B(-p,2)\rangle
=-\frac{\hbar\kappa^{AB}}{p^2}
\delta^4(\theta_1-\theta_2).}
$$

The former coordinate

$$
v_{\rm old}:=\frac{V}{2g}=\frac{u}{\sqrt2}
$$

therefore obeys

$$
\boxed{
\langle v_{\rm old}v_{\rm old}\rangle
=-\frac{\hbar}{2p^2}\delta^4(\theta_1-\theta_2),}
$$

not a unit vector propagator.

## 2. Linear canonical letter

The exact exponential derivative gives

$$
\Gamma_+
=\sqrt2g\,D_+u
+g^2\bigl[(D_+u)u-u(D_+u)\bigr]
+O(g^3).
$$

Using

$$
\mathcal W_+=-\frac18\bar D^2\Gamma_+,
$$

one obtains

$$
\mathcal W_+
=-\frac{\sqrt2}{8}g\bar D^2D_+u
+O(g^2).
$$

Define

$$
A_c:=g^{-1}\nabla_+\mathcal W_+.
$$

At linear order the connection term is quadratic, hence

$$
\boxed{
A_c^{(1)}
=-\frac{\sqrt2}{8}D_+\bar D^2D_+u
=-\frac1{4\sqrt2}D_+\bar D^2D_+u
=:Ku.}
$$

There is no additional $g$, $\sqrt2$, or source factor.

The physical and canonical bilinears scale in the same way:

$$
\mathcal O_{\rm phys}
=(\nabla_+\mathcal W_+)^A(\nabla_+\mathcal W_+)^B
=g^2A_c^AA_c^B,
$$

$$
D_{\rm phys}A_{\rm phys}
=(gD_c)(gA_c)
=g^2D_cA_c.
$$

Thus the conversion from canonical to physical letters cannot multiply the
loop coefficient by $8$.

## 3. Ordered source insertion

The source is ordered:

$$
S_J=\int J_{AB}A_c^AA_c^B.
$$

There is no $1/2$ in $S_J$.  Since $A_c^{(1)}$ is even,

$$
D_-\bigl(A_c^{(1),A}A_c^{(1),B}\bigr)
=(D_-A_c^{(1),A})A_c^{(1),B}
+A_c^{(1),A}(D_-A_c^{(1),B}).
$$

These are two different marked occurrences, not a multiplicity of either
one.  With the locked spinor conventions

$$
D^2=2D_-D_+,
\qquad
\bar D^2=2\bar D_{\dot+}\bar D_{\dot-},
$$

one marked source factor is

$$
D_-K
=-\frac1{4\sqrt2}D_-D_+\bar D^2D_+
=-\frac1{8\sqrt2}D^2\bar D^2D_+.
$$

Multiplication by the unmarked factor gives

$$
\left(-\frac1{8\sqrt2}\right)
\left(-\frac1{4\sqrt2}\right)
=\boxed{\frac1{64}}.
$$

The closed superspace word and the two mixed anticommutators give

$$
\left[D^2\bar D^2\delta^4(\theta)\right]_{\theta=0}=16,
$$

$$
\{D,\bar D\}=2\mathsf p,
$$

and therefore

$$
\boxed{
\left(\frac1{64}\right)(16)(2)(2)=1.}
$$

This is a $D$-algebra factor.  It is not four additional Wick
contractions.

## 4. Canonical cubic actions and Hessians

Substitution of $V=\sqrt2g\,u$ and
$W_c=g^{-1}\mathcal W$ into the exact gauge convolution gives

$$
S_{+,3}
=-\frac g4\int d^8z\,
\kappa_{AB}W_c^{Aa}[D_au,u]^B,
$$

$$
S_{-,3}
=+\frac g4\int d^8z\,
\kappa_{AB}\widetilde W_{c\dot a}^{A}
[\bar D^{\dot a}u,u]^B.
$$

For labeled variations,

$$
\delta_1\delta_2[Du,u]
=[Du_1,u_2]+[Du_2,u_1].
$$

After using $c_{ABC}=c_{[ABC]}$, the ordered action Hessians are

$$
\boxed{
H_W
=+\frac{ig}{4}c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),}
$$

$$
\boxed{
H_{\widetilde W}
=-\frac{ig}{4}c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).}
$$

Multiplication by $\tau_E=-1/\hbar$ gives the exponent vertices

$$
\boxed{
\mathfrak V_W
=-\frac{ig}{4\hbar}c_{UCE}W_c^{E\gamma}
(D_{C\gamma}-D_{U\gamma}),}
$$

$$
\boxed{
\mathfrak V_{\widetilde W}
=+\frac{ig}{4\hbar}c_{UCD}\widetilde W_{c\dot\gamma}^{D}
(\bar D_C^{\dot\gamma}-\bar D_U^{\dot\gamma}).}
$$

The second variation already contains the two labeled quantum-port
assignments.  No $2!$ remains.

## 5. Interaction and Wick factors

The mixed-chirality term in the exponential is

$$
\frac1{2!}
\left(S_{+,3}S_{-,3}+S_{-,3}S_{+,3}\right)
=S_{+,3}S_{-,3}.
$$

Hence the action-order factor is exactly $1$.  For one fixed directed source
attachment, the port-preserving Wick factor is also $1$.

The two exponent vertices and three canonical vector propagators give

$$
\begin{aligned}
\mathfrak V_W\mathfrak V_{\widetilde W}
\langle uu\rangle^3
&=
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3\\
&=-\frac{\hbar g^2}{16}.
\end{aligned}
$$

The exact ordered exterior-algebra trace has one odd source-loop
integration-by-parts sign $-1$.  Thus the rank-two parent prefactor is

$$
\boxed{+\frac{\hbar g^2}{16}.}
$$

## 6. Selected four-dimensional square

Let the UV-leading parts of both vertex momenta be $2L$.  The finite
four-dimensional spinor identity is

$$
\sigma\!\cdot\!L\,
\bar\sigma\!\cdot\!p\,
\sigma\!\cdot\!L
=2(L\!\cdot\!p)\sigma\!\cdot\!L
-\bar L^2\sigma\!\cdot\!p.
$$

The two factors of $2L$ give

$$
4\sigma\!\cdot\!L\,
\bar\sigma\!\cdot\!p\,
\sigma\!\cdot\!L
=8(L\!\cdot\!p)\sigma\!\cdot\!L
-4\bar L^2\sigma\!\cdot\!p.
$$

The first term belongs to the full-$d$ Schwinger-exact tensor reduction.
The selected inverse-square parent and its cut differ by

$$
\boxed{
-4(\bar L^2-L_d^2)\sigma\!\cdot\!p
=-4\mu_L^2\sigma\!\cdot\!p.}
$$

If $\bar L^2$ is replaced by $L_d^2$ before the cut subtraction, this line is
exactly zero.

The shifted rank-two coefficient is independent of the simplex parameters,
so

$$
2\int_{\Sigma_2}1
=2\left(\frac12\right)=1.
$$

Using

$$
\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{(L^2+\Delta)^3}
=\frac1{32\pi^2},
$$

one obtains

$$
\begin{aligned}
\Gamma_{G,\mathrm{directed}}
&=\left(\frac{\hbar g^2}{16}\right)
(-4)\left(\frac1{32\pi^2}\right)\\
&=-\frac{\hbar g^2}{128\pi^2}\\
&=\boxed{-\frac{\lambda_1}{8}}.
\end{aligned}
$$

## 7. Independent factor-eight diagnosis

The current coefficient follows directly from the canonical action:

$$
\boxed{
\frac1{64}
\times16
\times2
\times2
\times
\left[
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
\right]
\times(-1)
\times(-4)
\times\frac1{32\pi^2}
=-\frac{\lambda_1}{8}.}
$$

The earlier unit-propagator treatment of $v_{\rm old}=u/\sqrt2$ omitted

$$
\left(\frac12\right)^3=\frac18
$$

from the three vector lines.  Its result was therefore larger by

$$
2^3=8.
$$

The present $-\lambda_1/8$ was not inherited from that correction: it is an
independent reconstruction from $A_c^{(1)}$, both action Hessians, all three
canonical propagators, the ordered source, the interaction factorial, the
exact $D$-word, and the evanescent master.

## 8. Scope boundary

The calculation is conditional on the same local residual-free
Fermi--Feynman slice as the locked propagator inverse.  It proves the
normalization on that slice.  It does not prove that the slice, local
composite mixing, or Project-to-target component intertwiner is the final
renormalized choice.

## 9. Executable check

Run

```text
python scripts/step5_aa_gauge_canonical_normalization_audit.py
```

The checker verifies every rational, $g$, $\hbar$, $\sqrt2$, factorial,
propagator, and selected-square factor displayed above.
