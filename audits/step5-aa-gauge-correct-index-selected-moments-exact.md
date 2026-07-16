# Step 5 ordered AA gauge corrected-index selected moments

Status: `AA_GAUGE_TWO_SELECTED_EDGES_EXACT__LONGITUDINAL_QUOTIENT_PENDING`.

No holomorphic-twist coefficient enters this audit.

Use

$$
r_0=\ell,
\qquad
r_1=\ell-q,
\qquad
r_2=\ell-p-q,
\qquad
P=p+q.
$$

The corrected lower-index projection

$$
W^\gamma D_\gamma\big|_{W_+}=-W_+D_-
$$

gives the two selected marked-edge sums

$$
\mathcal S_{01}
=-2(r_2)_{+\dot-}\bar r_0^2,
\qquad
\mathcal S_{02}
=-2(r_0)_{+\dot-}\bar r_2^2.
$$

For each edge separately,

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}=0,
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2}.
$$

Therefore

$$
\mathcal S_{01}^{\rm anom}
=-2(r_2)_{+\dot-}\mu_\ell^2,
\qquad
\mathcal S_{02}^{\rm anom}
=-2(r_0)_{+\dot-}\mu_\ell^2.
$$

Feynman parametrization gives

$$
\frac1{D_0D_1D_2}
=2\int_0^1dy\int_0^{1-y}dz
\frac1{(L^2+\Delta)^3},
\qquad
L=\ell-yq-zP.
$$

The exact simplex moments are

$$
2\int_0^1dy\int_0^{1-y}dz=1,
$$

$$
2\int_0^1dy\int_0^{1-y}dz\,y
=2\int_0^1dy\int_0^{1-y}dz\,z
=\frac13.
$$

Hence

$$
\langle r_0\rangle
=\frac{q+P}{3}
=\frac{p+2q}{3},
$$

$$
\langle r_2\rangle
=\frac{q+P}{3}-P
=-\frac{2p+q}{3}.
$$

Writing

$$
J_{\mu^2}
:=\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2},
$$

the two raw selected moments are

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mathcal S_{01}^{\rm anom}}{D_0D_1D_2}
=\frac{4p+2q}{3}_{+\dot-}J_{\mu^2},
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mathcal S_{02}^{\rm anom}}{D_0D_1D_2}
=-\frac{2p+4q}{3}_{+\dot-}J_{\mu^2}.
$$

Thus the unquotiented selected sum is

$$
\boxed{
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mathcal S_{01}^{\rm anom}+\mathcal S_{02}^{\rm anom}}
{D_0D_1D_2}
=\frac{2}{3}(p-q)_{+\dot-}J_{\mu^2}.}
$$

This is not the physical completed orbit.  Its non-total-momentum word proves that the longitudinal, transported-edge, link, and explicit-contact quotient cannot be discarded.  No signed AA gauge coefficient is assigned here.
