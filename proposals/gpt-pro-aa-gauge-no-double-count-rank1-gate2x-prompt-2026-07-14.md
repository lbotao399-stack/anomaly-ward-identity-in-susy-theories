# GPT Pro Gate 2X — remove duplicated source saturation and compute the actual rank-one DRED moments

Your Gate 2W final vector is not accepted.  Recompute before comparing with any external target.

Your own exact sparse-Grassmann evaluation defines each row as the fully differentiated and Berezin-integrated word

$$
\mathscr W_{01}^{(ij)}
=\mathcal S_0\mathbb K\mathbb B_i\mathbb C_j\Delta_\theta,
\qquad
\mathscr W_{02}^{(ij)}
=\mathbb K\mathcal S_2\mathbb B_i\mathbb C_j\Delta_\theta.
$$

It then gives

$$
\mathcal G_{01,\mathcal S}
=(-b_2\det r_0,+b_2\det r_0,+b_2\det r_0,+b_2\det r_0),
$$

$$
\mathcal G_{02,\mathcal S}
=(+b_0\det r_2,-b_0\det r_2,+b_0\det r_2,+b_0\det r_2).
$$

These row coefficients already contain

$$
\mathcal S_e=\sqrt2\bar r_e^2D_+u,
\qquad
\mathbb K=-\frac1{4\sqrt2}D_+\bar D^2D_+u,
$$

all four action-endpoint derivatives, and the complete Berezin extraction.  Therefore the sums

$$
2b_2\det r_0,
\qquad
2b_0\det r_2
$$

are final local $D$-word polynomials.  Gate 2W Section 8 incorrectly treated their numerical endpoint sum $2$ as a new bare multiplicity and multiplied it again by

$$
\sqrt2\left(-\frac1{4\sqrt2}\right)(16).
$$

That double-counts the source scalar and the same derivative saturation already used to obtain the sparse rows.  Indeed, relative to the source product $-1/4$, the exact final coefficient $+2$ already means that the remaining differentiated endpoint word contributed $-8$; multiplying by $(-1/4)16(2)$ again is not allowed.

There is a second incompatible step.  The exact full-$d$ subtraction gives finite rank-one numerators

$$
-2(r_2)_{+\dot-}\mu_\ell^2,
\qquad
-2(r_0)_{+\dot-}\mu_\ell^2.
$$

Gate 2W Section 10 discarded these and restored the old unrelated rank-two tensor pole $L_1^mL_2^n/\epsilon$.  Do not do that.  Use one fixed outgoing routing

$$
r_0=\ell,
\qquad
r_1=\ell+q,
\qquad
r_2=\ell+p+q,
\qquad
P=p+q,
$$

and keep $p,q$ independent.  With

$$
L=\ell+yq+zP,
$$

the exact simplex moments are

$$
2\int_{\Sigma_2}y
=2\int_{\Sigma_2}z
=\frac13.
$$

Hence derive explicitly

$$
2\int_{\Sigma_2}r_2
=\frac{2p+q}{3},
\qquad
2\int_{\Sigma_2}r_0
=-\frac{p+2q}{3},
$$

with the signs checked from the declared shift.  Do not set $q=-p$, discard a $q$ term, or invoke an external equation of motion without deriving its typed operator quotient.

Required correction:

1. Start from the eight final sparse row polynomials exactly as printed.  Factor out only the two action Hessian couplings, three propagators, interaction Taylor factor, color tensor, and external component normalization that are not already in those rows.  Print this common prefactor once.
2. For every row print the full-$d$ parent-minus-cut zero and its $\mu_\ell^2(r_e)_{+\dot-}$ remainder.
3. Integrate every rank-one remainder with independent $p,q$.  Preserve which external derivative acts on $A$ and which momentum contracts the external $D_{\dot a}$.
4. Insert the longitudinal/contact cancellation only after verifying it does not transport a new inverse square or external momentum term.  An aggregate assertion $L_{01}^{\rm contact}=+2d_0W_{02}$ is insufficient; give the rowwise operator map or leave it open.
5. Explain explicitly why Gate 2W Section 8 is or is not a double count.  A new scalar $w_D$ may not be introduced after the final sparse polynomials are known.
6. End with the genuinely derived target-blind $(c_{DA},c_{AD})$.  If the remaining external-momentum or normalization map is not fixed, state the first exact blocker.  Do not restore $(1,-1)$ from the old tensor pole.
