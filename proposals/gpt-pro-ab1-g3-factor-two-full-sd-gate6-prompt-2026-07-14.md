# GPT Pro Gate 6: AB/BA G3 absolute normalization and complete SD orbit

Work target-blind.  The earlier claim $G_{32}=+i\sqrt2\lambda_1$,
$G_{33}=-i\sqrt2\lambda_1$ is rejected because it multiplied the exact
simplex weight by a compact Project result instead of reconstructing the
absolute Feynman normalization.

## Locked conventions

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},
\qquad
r_0=\ell,quad r_1=\ell-p,quad r_2=\ell-p-q,
$$

$$
\bar r_e^2-r_{e,d}^2=\mu_\ell^2,
\qquad
\int\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

For $G_{32}$ the exact primitive factors currently give

$$
C_I=-\frac{g^2}{4\sqrt2},
\qquad
C_M=\frac{\sqrt2g}{\hbar},
\qquad
C_{H_-}=-\frac{\sqrt2g}{\hbar},
$$

$$
C_{\rm prop}
=(-\hbar)\left(\frac{\hbar}{16}\right)^2
=-\frac{\hbar^3}{256},
$$

$$
\frac1{2!}(S_MS_H+S_HS_M)=1,
\qquad
\frac1{3!}\sum_{\sigma\in S_3}
\operatorname{sgn}_{\rm flavor}(\sigma)
\operatorname{sgn}_{\rm color}(\sigma)=1.
$$

Thus before D-algebra

$$
C_{\rm preD}^{32}=-\frac{\sqrt2\hbar g^4}{1024},
\qquad
C_{\rm preD}^{33}=+\frac{\sqrt2\hbar g^4}{1024}.
$$

The exact original-measure replay has raw top coefficient $32768$.  Its
displayed conversion is

$$
32768
\left(\frac14\right)_{d^4\theta_M}
\left(\frac12\right)_{d^2\bar\theta_H}
\left(-\frac12\right)_{\rm rank\ extraction}
(2)_{\rm trace/metric}
=-4096.
$$

The three occurrence-resolved square branches have normalized simplex moment
$1/3$ each.  With external $C$ map $g^{-2}$ and color $+i$, each branch gives

$$
\frac{C_{\rm preD}^{32}(-4096)(1/3)(32\pi^2)^{-1}g^{-2}(+i)}{\lambda_1}
=\frac23i\sqrt2,
$$

and the current full three-edge sum is

$$
G_{32}^{\rm isolated}=+2i\sqrt2\lambda_1,
\qquad
G_{33}^{\rm isolated}=-2i\sqrt2\lambda_1.
$$

The three branches are

$$
G3\text{-}A\text{-}E0:\quad -1024\det(r_0)W_{12},
$$

$$
G3\text{-}A\text{-}L1:\quad +1024\det(r_1)W_{P0},
$$

$$
G3\text{-}B\text{-}E2:\quad -1024\det(r_2)W_{p0}.
$$

The descendant also contains the same-occurrence pairs

$$
G3\text{-}A\text{-}JE:+512W_{12},
\qquad
G3\text{-}A\text{-}JX:-512W_{12},
$$

$$
G3\text{-}B\text{-}PE:-128W_{p0},
\qquad
G3\text{-}B\text{-}PX:+128W_{p0}.
$$

Earlier code declared each pair pointwise zero and treated all three square
branches as independent DRED remainders.  This must be rechecked from the
full Schwinger-Dyson derivative, not from a compact target.

## Required replay

1. Re-derive every primitive scalar above from the actual labeled source and
action derivatives.  Audit the source mixed-Hessian factorial, action Taylor
factorial, six $H_-$ flavor/color permutations, unique Wick pairing, both
Berezin measures, rank extraction, and trace/metric conversion.  Locate any
exact missing factor $1/2$; do not insert one.

2. For every $r_0,r_1,r_2$ square occurrence, write its parent, full-$d$
Schwinger contact, and sole $\mu_\ell^2$ remainder.  Decide whether the
transported $r_1$ term is a second parent remainder or part of the induced
contact of the $r_0$ occurrence.

3. Derive JE/JX and PE/PX directly as derivative-of-action contacts with their
denominators and routing.  A zero standalone bubble is not enough: test their
sum with the parent on the same occurrence before and after
$\bar r_e^2\to r_{e,d}^2$.

4. Sum the complete G3 orbit for both $AB$ and $BA$, including Koszul/color
reflection.  Give the final target-blind coefficients before reading HT.

5. Only then compare with the physical holomorphic-twist vector
$\pm i\sqrt2$.  If a factor-two remains, identify the first exact equality
where the Project and HT calculations differ.

Forbidden: using the HT coefficient as a normalization, deleting affine
contacts, counting integration-by-parts presentations as graphs, or stopping
at the isolated triangle.
