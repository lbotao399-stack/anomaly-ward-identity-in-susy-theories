# Step 5 ordered $AA$ pure-gauge marked-occurrence recount

Status: `AA_GAUGE_FULL_MARKED_OCCURRENCE_RECOUNTED__DIRECTED_COEFFICIENT_UNCHANGED`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.

Scope: target-blind recount of the two source attachments, the two marked
$D_-$ placements, and all quantum-port derivative endpoints of the
canonical mixed-chirality gauge triangle.  This artifact is independent of
the main ordered-$AA$ audit.

## 1. Canonical cubic Hessians already contain the polarization sum

With canonical $V=\sqrt2g\,u$, the chiral and antichiral cubic actions are

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

For labeled quantum variations $u_1,u_2$,

$$
\delta_1\delta_2[Du,u]
=[Du_1,u_2]+[Du_2,u_1].
$$

Using total antisymmetry of $c_{ABC}$, this is the derivative difference
on the two labeled ports.  The exponent Hessians are

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

The raw all-label cubic polarization has

$$
6\times2=12
$$

ordered words in each chirality.  Fixing the background field-strength leg
and differentiating the remaining two labeled quantum legs sums those words
to the displayed Hessian.  The two terms of each derivative difference are
the two quantum-port assignments.  They are not an additional multiplicity:

$$
\boxed{\texttt{NO_EXTRA_POLARIZATION_MULTIPLICITY}.}
$$

The two chiral-order assignments in the interaction expansion obey

$$
\frac1{2!}
\left(S_{+,3}S_{-,3}+S_{-,3}S_{+,3}\right)
=S_{+,3}S_{-,3}.
$$

## 2. Sixteen raw occurrence rows

Fix external $\widetilde W^D(q)$ at vertex $1$ and $W_+^E(p)$ at vertex
$2$, with

$$
r_0=k,
\qquad
r_1=k-q,
\qquad
r_2=k-p-q.
$$

There are

$$
2_{\rm source\ attachments}
\times2_{\rm marked\ }D_-
\times2_{\bar D\rm\ endpoints}
\times2_{D\rm\ endpoints}
=16
$$

raw rows.  The four derivative endpoints for a fixed source attachment and
marked placement are

$$
(r_0,r_1),
\qquad
(r_0,r_2),
\qquad
(r_1,r_1),
\qquad
(r_1,r_2).
$$

No endpoint row is multiplied after expanding the two effective Hessians.

## 3. Exact two marked $D$-words

Set the source superspace coordinate to $\theta_0=0$.  Use

$$
K=-\frac1{4\sqrt2}D_+\bar D^2D_+,
$$

and the external bottom representatives

$$
\widetilde W_{\dot+}(q,\theta,\bar\theta)
=e^{-i\theta q\bar\theta}D_{\dot+}(q),
$$

$$
W_+(p,\theta,\bar\theta)
=e^{i\theta p\bar\theta}\theta^+A(p).
$$

Write

$$
\mathsf r_i=
\begin{pmatrix}
a_{i+}&b_{i+}\\
a_{i-}&b_{i-}
\end{pmatrix},
\qquad
W_{ij}:=a_{i+}b_{j+}-b_{i+}a_{j+}.
$$

For the attachment

$$
u_A\longrightarrow v_1(\widetilde W^D),
\qquad
u_B\longrightarrow v_2(W^E),
$$

the exact left-Berezin endpoint sum gives the following two words.

When $D_-$ marks the source occurrence attached to vertex $1$,

$$
\boxed{
\mathcal G_1
=(b_{0+}+b_{1+})W_{02}.}
$$

When $D_-$ marks the source occurrence attached to vertex $2$,

$$
\boxed{
\mathcal G_2
=(b_{0+}-b_{1+})W_{02}.}
$$

These are not assigned by reflection; both are emitted by the exact exterior
algebra checker.

Since

$$
b_{0+}-b_{1+}=q_{+\dot-},
$$

and

$$
W_{02}
=r_{0+}\wedge r_{2+}
=(p+q)_+\wedge r_{2+},
$$

$\mathcal G_2$ contains at most one loop momentum.  A logarithmic triangle
pole requires a rank-two loop numerator.  Therefore

$$
\boxed{
\mathcal G_2\big|_{L_mL_n}=0,
\qquad
\texttt{NO_RANK_TWO_DRED_DEFECT}.}
$$

By contrast,

$$
b_{0+}+b_{1+}=2L_{+\dot-}+\text{external},
$$

so $\mathcal G_1$ contains the rank-two word.  In the nondegenerate frame
$p=e_1,\ q=e_4$, its exact diagonal coefficients are

$$
[\mathcal G_1]_{L_m^2}=(-2i,2i,0,0),
$$

whereas

$$
[\mathcal G_2]_{L_m^2}=(0,0,0,0).
$$

The first word is the component form of the covariant chain

$$
(r_0+r_1)_{+\dot\beta}
p^{\dot\beta\gamma}
(r_1+r_2)_\gamma{}^{\dot\alpha}.
$$

## 4. Crossed source attachment

For

$$
u_A\longrightarrow v_2(W^E),
\qquad
u_B\longrightarrow v_1(\widetilde W^D),
$$

the marked-$A$ row is geometrically $\mathcal G_2$ and has no rank-two
defect.  The marked-$B$ row is geometrically $\mathcal G_1$ and gives the
reflected ordered output.  Thus the complete four source/mark rows contain
exactly two anomaly-bearing rows:

| source attachment | marked source occurrence | rank-two defect | ordered output |
|---|---|---|---|
| $A\to\widetilde W,\ B\to W$ | $A$ | yes | $\langle D,A\rangle$ |
| $A\to\widetilde W,\ B\to W$ | $B$ | no | none |
| $A\to W,\ B\to\widetilde W$ | $A$ | no | none |
| $A\to W,\ B\to\widetilde W$ | $B$ | yes | $\langle A,D\rangle$ |

The two anomaly-bearing rows are the directed and reflected terms; they are
not two copies of either term.

## 5. Normalization and DRED remainder

For one anomaly-bearing row, the source and $D$-algebra weight is

$$
\left(\frac1{64}\right)(16)(2)(2)=1.
$$

The two Hessians and three vector propagators give

$$
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
=-\frac{\hbar g^2}{16}.
$$

The ordered odd-source integration by parts changes this to the parent
prefactor $+\hbar g^2/16$.  The rank-two finite spinor word reduces to

$$
-4(\bar L^2-L_d^2)
=-4\mu_L^2.
$$

With

$$
\int\frac{d^dL}{(2\pi)^d}
\frac{\mu_L^2}{(L^2+\Delta)^3}
=\frac1{32\pi^2},
$$

the directed coefficient is

$$
\frac{\hbar g^2}{16}(-4)
\frac1{32\pi^2}
=-\frac{\hbar g^2}{128\pi^2}
=-\frac{\lambda_1}{8}.
$$

The reflected row gives the reversed ordered tensor.  Therefore the complete
marked/source recount leaves the previous pure-gauge result unchanged:

$$
\boxed{
\Gamma_{AA,G}^{AB}
=-\frac{\lambda_1}{8}
\mathbb F^{AB}{}_{DE}
\left[
\langle D^D,A^E\rangle
-\langle A^D,D^E\rangle
\right].}
$$

There is no factor $2$, $4$, or $8$ from the primitive polarization,
Hessian endpoints, source attachments, marked placements, or interaction
expansion.

## 6. Executable check

Run

```text
python scripts/step5_aa_gauge_marked_occurrence_exact_audit.py
```

The checker constructs the two marked words by exact left Grassmann
differentiation, verifies all sixteen raw occurrence rows, checks the loop
ranks $2$ and $1$, and reproduces the coefficient
$-\lambda_1/8$.
