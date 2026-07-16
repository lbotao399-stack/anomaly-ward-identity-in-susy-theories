# Gate AA-G: complete gauge-fixed ordered-AA DRED orbit

Work target-blind.  Do not use the holomorphic-twist coefficient, residual
supersymmetry, or any desired final answer to set a coefficient.

## 1. Locked Project data

Repository:

`/Users/libotao/Desktop/awi-step5-all-channels`

Authority base:

`origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`

Read first:

- `contracts/foundations/step-03a-gauge-chiral-action.md`
- `contracts/foundations/step-03c-gauge-vector-representation.md`
- `contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md`
- `contracts/foundations/step-04c-n4-super-yang-mills.md`
- `contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md`
- `audits/step5-aa-gauge-canonical-normalization-ledger.md`
- `audits/step5-aa-gauge-full-source-sd-orbit-exact.md`
- `audits/step5-aa-gauge-marked-occurrence-recount.md`
- `audits/step5-ww-physical-cut-pole.md`
- `audits/step5-dred-cutting-failure-exact.md`

Use

$$
d=4-2\epsilon,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2.
$$

On every selected edge (e), the only anomaly operation is

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac{r_{e,d}^2}{D_0D_1D_2}
=\frac{\mu_\ell^2}{D_0D_1D_2},
$$

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

Do not insert a second graph-specific (4-d) factor.  If the D-algebra had
produced (r_{e,d}^2), parent minus Schwinger cut would be identically zero.

Canonical vector coordinate and letter:

$$
V=\sqrt2g\,u,
\qquad
\langle u^A(p,1)u^B(-p,2)\rangle_E
=-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12}),
$$

$$
A_c:=g^{-1}\nabla_+\mathcal W_+,
\qquad
A_c^{(1)}=-\frac1{4\sqrt2}D_+\bar D^2D_+u.
$$

The ordered source is

$$
S_J=\int J_{AB}A_c^AA_c^B
$$

with no (1/2).  Expand

$$
A_c=A_1+gA_2+g^2A_3,
\qquad
\Gamma_-=g\gamma_1+g^2\gamma_2.
$$

The complete order-(g^2) source/resolvent support is

$$
\langle I_2\rangle_0
-\hbar^{-1}\langle I_1S_3\rangle_0
-\hbar^{-1}\langle I_0S_4\rangle_0
+(2\hbar^2)^{-1}\langle I_0S_3S_3\rangle_0.
$$

Do not restrict (S_3,S_4) to the two classical (W^2) self-interaction
vertices.  Use the selected residual-free Fermi--Feynman gauge and include
every same-order field in the gauge-fixed measure:

1. quantum vector (u);
2. FP ghost/antighost and their Nielsen--Kallosh partners;
3. multiplier/non-minimal/auxiliary blocks required by the locked slice;
4. gauge-fixing Hessian and its cubic/quartic background ports;
5. measure/Jacobian occurrences;
6. collapsed inverse-kernel, nonlinear-source, seagull, and endpoint rows.

## 2. Conflict to adjudicate, not to inherit

The current isolated directed VVV replay gives

$$
C^{\rm isolated}_{AA,\mathrm{VVV}}
=-\frac18\lambda_1,
\qquad
\lambda_1:=\frac{\hbar g^2}{16\pi^2}.
$$

Its displayed non-triangle (I_2,I_1S_{g3},I_0S_{g4}) vector-only rows have
zero scalar four-dimensional trace.  That calculation does not enumerate an
FP/NK/gauge-fixing determinant orbit.

An older conditional WW cut/contact calculation instead has four endpoint
rows whose aggregate finite defect is (+lambda_1).  It used a different
intermediate vector coordinate and is not authority for the present answer.

The separately recomputed matter part of ordered (AA) gives unit
coefficient in its own output slots.  This is only a normalization diagnostic;
it may not be used to force the gauge answer.

Your task is to decide by explicit gauge-fixed Feynman calculation whether

$$
C^{\rm complete}_{AA,\mathrm{gauge}}
=-\frac18\lambda_1+C_{\rm FP}+C_{\rm NK}
+C_{\rm gf}+C_{\rm aux}+C_{\rm contact}
$$

has any nonzero completion.  If a (+9\lambda_1/8) remainder exists, derive
it; do not assume it.  If it does not, leave the mismatch explicit and name
the first missing or inconsistent normalization line.

## 3. Required directed calculation

Compute both ordered output carriers independently:

$$
\langle D^D,A^E\rangle,
\qquad
\langle A^D,D^E\rangle.
$$

For every occurrence give a row containing

$$
(\text{id},\text{field loop},\text{source mark},\text{ports},
\text{vertex coefficient},\text{Wick/Koszul sign},
\text{raw D-word},r_e,
\text{full-}d\text{ contact},\mu_\ell^2\text{ remainder},
\text{simplex moment},\text{normalized output}).
$$

Required checks:

1. derive all vector, FP, NK, gauge-fixing, multiplier, and auxiliary
   propagators from the locked quadratic Hessian;
2. derive their cubic and quartic background vertices by ordered functional
   differentiation, including every (1/2!), identical-leg factor, and
   orientation;
3. enumerate every closed one-loop triangle, bubble/contact, seagull, and
   tadpole at order (g^2);
4. prove absent sectors absent from typed ports rather than omitting them;
5. retain the two outer (D_-) placements separately;
6. carry every four-dimensional inverse square to its matching full-(d)
   Schwinger contact before taking the difference;
7. retain transported neighboring squares and longitudinal metric terms;
8. integrate rank-zero, rank-one, and rank-two remainders with exact rational
   simplex moments;
9. reduce the color chain to
   (\mathbb F^{AB}{}_{DE}) without using a target coefficient;
10. state the final ordered coefficient vector in units of
   (\lambda_1\mathbb F^{AB}{}_{DE}).

No use of `proportional to`, `approximately`, an unexplained overall
constant, a fitted field rescaling, or an inherited target coefficient is
allowed.

## 4. Sealed comparison target

Only after the complete gauge-fixed coefficient has been derived, compare it
with the conditional component target

$$
\Delta(A^A,A^B)\big|_{\rm gauge}
=\lambda_1\mathbb F^{AB}{}_{DE}
\left(
\langle D^D,A^E\rangle
-\langle A^D,D^E\rangle
\right).
$$

A mismatch is a valid result only if the complete occurrence table and the
first unresolved line are displayed.  Do not repair a mismatch by invoking
supersymmetry or the holomorphic twist.
