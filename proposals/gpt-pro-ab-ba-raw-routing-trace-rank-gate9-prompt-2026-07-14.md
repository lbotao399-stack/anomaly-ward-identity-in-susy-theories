# GPT Pro Gate 9 — AB/BA raw routing, trace/rank, and EOM-contact correction

Your Gate 8 result is a trial, not accepted. Recompute from the supplied raw superspace data. Do not use the holomorphic-twist vector, residual-q uniqueness, or reflection of a different topology to determine a coefficient.

## 1. Frozen DRED mechanism

For every actual marked inverse-kernel occurrence (e), use

$$
\frac{r_{e,d}^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}=0,
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\int_\ell\frac{\mu_\ell^2}{D_0D_1D_2}=\frac1{32\pi^2}.
$$

No graph-specific (4-d) factor and no fitted contact multiplier are allowed.

## 2. Correct G2 external routing

The executable raw replay is `scripts/step5_ab1_g2_g3_dword_replay.py`, lines 383--445:

```python
phi_r = chiral_b_plus(H, q)
probe = vector_dotted_component(M, dotted)
```

and its loop routing obeys

$$
r_0-r_1=p,
\qquad
r_1-r_2=q.
$$

Thus the external vector probe is (D(p)) at (M), while the external chiral endpoint is (B_1(q)) at (H). The old comment `B1(p)>D(q)` is false. The replayed ordered word is

$$
\frac{\lambda_1}{3}
B_1(q)(4p-q)^{\dot\alpha}D_{\dot\alpha}(p).
$$

Do not relabel this as (B_1(p)D(q)). Determine the exact incoming/outgoing Fourier signs from the endpoint exponentials in the executable D-word, then map

$$
(p_D,q_B)\longrightarrow
(\text{divergence/EOM carrier},\text{ordered pair carrier}).
$$

The raw metric decomposition is

$$
c_1=1-z,
\qquad
c_{2,\det}=z,
\qquad
c_{2,\Omega}=-\frac12.
$$

The (Omega)-term is a genuine transported (r_1) inverse-kernel occurrence:

$$
P_\Omega=-\frac12\bar L^2W,
\qquad
C_\Omega=+\frac12L_d^2W,
\qquad
P_\Omega+C_\Omega=-\frac12\mu_L^2W.
$$

Retain its rank-zero completion

$$
\frac{L_d^2}{(L_d^2+\Delta)^3}
=\frac1{(L_d^2+\Delta)^2}
-\frac{\Delta}{(L_d^2+\Delta)^3}.
$$

The simplex values before any quotient are

$$
2\int_{\Delta_2}c_1=\frac23,
\qquad
2\int_{\Delta_2}c_{2,\det}=\frac13,
\qquad
2\int_{\Delta_2}c_{2,\Omega}=-\frac12.
$$

Construct the external vector-Euler Schwinger contact from the raw action/source Hessian. Decide, by an explicit functional-derivative and collapsed-denominator calculation, what happens to the (B_1(P\!\cdot D)) carrier. It is forbidden merely to declare a total derivative zero: the Project authority still had `BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT`, so the quotient itself must be derived here.

## 3. G1 must be recomputed from its own VVV rows

The current replay enumerates

$$
6_{S_3}\times2_{QL/LQ}\times2_{\rm chirality}=24
$$

polarized VVV rows and two source marks. Gate 8 replaced the G1 topology by a reflected G2 polynomial. This is invalid: VVV and (M_1M_1) have different action Hessians.

Use the actual G1 raw rows in

- `scripts/step5_ab1_g1_vvv_dword_replay.py`,
- `scripts/step5_ab1_marked_sd_orbit_exact_audit.py`,
- `scripts/step5_ab_ba_g1_longitudinal_contact_exact_audit.py`.

Determine whether the two source marks are two parent occurrences, two presentations of one transported occurrence, or parent plus induced contact. Exhibit the raw Hessian coefficient, source/action factorial, Wick multiplicity, and the exact denominator attached to every retained square. Derive the generic ((p_B,q_D)) typed pair/EOM vector and its reflected BA vector without using G2 or HT.

## 4. Common trace/rank factor-of-two audit for G1 and G3

The corrected raw typed vector currently produced by the local scripts is

$$
(D>B_1,\ B_1>D,\ C_2>C_3,\ C_3>C_2)
=
(2,-\tfrac13,-2i\sqrt2,+2i\sqrt2)
$$

before closing the G2 external Euler contact. G1 and G3 therefore share a factor-two suspicion.

For a numerator

$$
N(L)=c\,\bar L^2W+\cdots,
$$

the two-axis diagonal trace already gives

$$
\sum_{a=1}^{2}[L_a^2]N=2cW,
\qquad
c=\frac{\operatorname{trace}_{12}N}{2W}.
$$

After this division, multiplying another `trace_per_metric=2` would double count the same two-axis trace. Audit the original Berezin word before any metric extraction and print one exact nonzero monomial coefficient. Decide whether the correct raw conversion is

$$
32768\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)=-2048
$$

or

$$
32768\left(\frac14\right)
\left(\frac12\right)
\left(-\frac12\right)(2)=-4096.
$$

The answer must explain whether the final (2) is already used in `trace/(2W)`. Apply the same convention consistently to G1, G2, G3, and compare with the independently closed AD/DA fact: its old trace normalization was (chi_{\rm old}=2), while the raw Hessian contact calculation gives (chi=1), hence exactly one rank/trace factor (1/2).

## 5. Required output

Produce:

1. A raw occurrence table for G1, G2-det, G2-(Omega), G32, and G33, with source/action Hessians, factorials, Wick counts, marked edge, parent numerator, full-(d) cut, and finite (mu_\ell^2) remainder.
2. The exact pre-quotient basis

$$
(\langle D,B_1\rangle,
(P\!\cdot D)B_1,
\langle B_1,D\rangle,
B_1(P\!\cdot D),
\langle C_2,C_3\rangle,
\langle C_3,C_2\rangle).
$$

3. The explicit EOM/BRST/total-derivative contact matrix derived from the local action, not postulated.
4. The final AB and BA ordered vectors only after sealing the target-blind raw result.
5. The first false equality in Gate 8 and the first false equality in the current local scripts.

Do not stop at a covariance argument. Do not infer G1 from G2. Do not use HT to choose between (-2048) and (-4096).
