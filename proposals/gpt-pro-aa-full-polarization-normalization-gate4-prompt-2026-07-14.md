# GPT Pro Gate 4: reject the retracted affine quotient and locate the AA primitive normalization error

Your Gate 3 answer is not accepted.  It reused the explicitly retracted affine fits

$$
R_0(\ell),\qquad R_2(\ell),
$$

and therefore obtained the spurious coefficient $-\lambda_1/64$.  The Gate 3 prompt explicitly stated that the held-out sample rejects those fits and required occurrence-resolved polynomial quotients.  Do not use the Gate 3 affine formulas again.

The exact full-polarization component engine now gives, in the canonical transverse frame

$$
p=e_0,\qquad q=e_1,\qquad \varepsilon=e_3,\qquad \dot\alpha=0,
$$

for the two surviving occurrence edges

$$
N_{S,0}=\bar r_0^2Q_0,\qquad N_{S,2}=\bar r_2^2Q_2,
$$

with zero exact polynomial remainder and

$$
Q_0=-\frac12\ell_0^2+i\ell_0\ell_1+
\left(\frac32-i\right)\ell_0+\frac12\ell_1^2-
\left(1+\frac32i\right)\ell_1-\frac12+\frac32i,
$$

$$
Q_2=-\frac12\ell_0^2+i\ell_0\ell_1-
\frac12\ell_0+\frac12\ell_1^2+\frac i2\ell_1.
$$

Both satisfy the exact four-dimensional harmonic checks

$$
\partial_{\ell_\mu}\partial_{\ell_\mu}Q_0=0,
\qquad
\partial_{\ell_\mu}\partial_{\ell_\mu}Q_2=0.
$$

With

$$
C_{e,d}=-L_e-r_{e,d}^2Q_e,
$$

the exact identities are

$$
N_{{\rm full},e}+C_{e,d}=\mu_\ell^2Q_e,
\qquad
N_{{\rm full},e}^{(d)}+C_{e,d}=0.
$$

The exact Feynman-parameter integrals in this frame are

$$
2\int_{x+y+z=1}Q_0=-\frac12+\frac5{12}i,
$$

$$
2\int_{x+y+z=1}Q_2=\frac7{12}i,
$$

$$
2\int_{x+y+z=1}(Q_0+Q_2)=-\frac12+i.
$$

These $Q_e$ already include the exact source coefficient, Berezin saturation, all three external-position families, both endpoint orderings, and all four action chirality pairs.  They do not include the two exponent-vertex prefactors, three propagator prefactors, color contraction, or the universal loop master.

Required correction:

1. Explicitly acknowledge that Gate 3 used retracted data and discard every conclusion derived from the affine $R_e$.
2. Reproduce the displayed quadratic $Q_0,Q_2$ from raw external-slot families or identify the first raw row on which you disagree.  A one-point numerical check is insufficient.
3. Derive the occurrence-preserving Schwinger contact and the full-$d$ zero row by row.  Do not introduce any graph-specific $4-d$.
4. Redo the absolute coefficient from the original action and source measures.  List, without combining them prematurely: source Hessian coefficient, each cubic exponent vertex, each of three vector propagators including the $\kappa^{-1}$ factors, Taylor factor, labeled Wick multiplicity, color contraction, and loop master $1/(32\pi^2)$.
5. Use two independent transverse spinor frames to reconstruct the four ordered structures.  Do not infer the reflected sign from one color component.
6. Compare with

$$
\Delta(A^A,A^B)=
\langle D^A,A^B\rangle-\langle A^A,D^B\rangle
+\sum_r\bigl(\langle B_r^A,C_r^B\rangle-\langle C_r^A,B_r^B\rangle\bigr)
$$

only after the primitive ledger is closed.  Do not target-fit a missing factor.

The goal is to locate the first primitive equality responsible for Gate 3's factor $64$ and sign, not to restate the target.
