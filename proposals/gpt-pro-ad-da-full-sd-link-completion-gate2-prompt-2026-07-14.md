# GPT Pro Gate 2 — AD/DA full-SD named-link completion

We need a target-blind, occurrence-resolved closure of the standard one-loop AD/DA gauge triangles in Euclidean N=4 SYM. Do not use the holomorphic-twist coefficient to choose a normalization. Do not use a global `(4-d)` trace. Every anomaly remainder must be a marked inverse-kernel failure

$$
\bar r_e^2-r_{e,d}^2=\mu_\ell^2.
$$

## Locked conventions

$$
d=4-2\epsilon,\qquad
D_e=r_{e,d}^2,\qquad
r_0=\ell,\quad r_1=\ell-q,\quad r_2=\ell-p-q,
$$

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},\qquad
\int\frac{d^d\ell}{(2\pi)^d}\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

Canonical linear letters:

$$
A_c^{(1)}=-\frac1{4\sqrt2}D_+\bar D^2D_+u,
\qquad
D_{c,\dot a}^{(1)}=-\frac1{4\sqrt2}D^2\bar D_{\dot a}u.
$$

The marked AD source acts only on the `A` occurrence because

$$
\nabla_-D_{\dot a}=0,
$$

and the exact marked operator split is

$$
D_-D_+\bar D^2D_+
=-8(\det r_e)D_+-\frac12D_+\bar D^2D^2.
$$

The source-longitudinal term and gauge-fixing Euler term have already been replayed from raw D-words and cancel occurrence by occurrence:

$$
L_{\omega,e}^{\rm source}+L_{\omega,e}^{\rm gf}=0.
$$

## Already exact raw results

The complete functional Hessian includes every external placement in the field-strength slot, commutator differentiated slot, and undifferentiated commutator slot. There are four action-chirality sectors

$$
(++),(+-),(-+),(--).
$$

Their Taylor/action weights are each exactly one:

$$
\frac1{2!}\sum_{\chi,\psi}
\big[H_\chi(L)H_\psi(R)+H_\psi(R)H_\chi(L)\big]
=\sum_{\chi,\psi}H_\chi(L)H_\psi(R).
$$

The full raw numerical Hessian replay gives the same polynomial in all four sectors:

$$
AD_{\rm direct}=DA_{\rm crossed}=R_1,
\qquad
AD_{\rm crossed}=DA_{\rm direct}=R_2.
$$

For one sector, after exact simplex integration, in the raw `(p_+,q_+)` basis,

$$
R_1=\left(\frac{i}{48},\frac{i}{96}\right),
\qquad
R_2=\left(\frac{i}{24},\frac{i}{48}\right).
$$

For every marked edge, introduce an unfixed trace/metric reconstruction factor `chi`. The parent and the single same-occurrence inverse-kernel cut are

$$
\frac{\chi R_{\omega,e}\bar r_e^2}{D_0D_1D_2},
\qquad
-\frac{R_{\omega,e}}{\prod_{j\ne e}D_j}.
$$

At `mu_l^2=0`, full-d Schwinger-Dyson gives

$$
\frac{(\chi-1)R_{\omega,e}}{\prod_{j\ne e}D_j}=0,
$$

so for generic nonzero routed word

$$
\chi=1.
$$

The old replay used `chi=2`; hence the corrected rank/trace normalization is exactly `1/2`. Together with four chirality sectors, the corrected one-sector-to-full factor is

$$
4\times\frac12=2.
$$

The explicit two-denominator O05/O06 partial contacts are:

$$
\begin{array}{c|ccc}
&e_0&e_1&e_2\\ \hline
AD&7i\,q_+&0&2i\,q_+\\
DA&-\frac i2q_+&i(p+q)_+&i(p+q)_+
\end{array}
$$

and crossed color routing swaps `AD <-> DA`. These are partial contact members only. They may not be added to an already formed `mu_l^2` remainder, and a residual may not be defined by subtracting them from the desired answer.

## Required calculation

1. Construct an explicit same-edge occurrence ledger for every `e=0,1,2` separating:

$$
K_e,\quad L_e^{\rm source},\quad L_e^{\rm gf},\quad O05_e,\quad O06_e,
\quad \text{all named link/contact continuations}.
$$

Show the actual rational coefficient and routed spinor word of each named link continuation. Do not write only “the rest cancels”.

2. Prove directly, before integration and independently for AD direct, AD crossed, DA direct, DA crossed,

$$
N_e^{(d)}+C_{e,d}=0,
$$

and after DRED replacement,

$$
N_e+C_{e,d}=\frac{\mu_\ell^2R_{\omega,e}}{D_0D_1D_2}.
$$

3. Determine whether the O05/O06 affine pieces cancel entirely inside the full same-edge orbit or survive only as the `q_+` divergence/EOM carrier. Keep the physical `p_+` coefficient and `q_+` carrier distinct.

4. Starting from the supplied one-sector integrals, show every multiplication leading to the full coefficients. The expected target-blind arithmetic to audit is

$$
4\left(\frac12\right)(-8)R_1
=\left(-\frac i3,-\frac i6\right),
$$

$$
4\left(\frac12\right)(-8)R_2
=\left(-\frac{2i}{3},-\frac i3\right).
$$

Here `-8` is the old raw-integral-to-lambda1 conversion prior to the `chi=1/2` correction. Audit whether it has been counted exactly once.

5. Only after steps 1–4, convert the common spinor Fourier factor and state the ordered physical coefficients. The proposed result to confirm or refute target-blindly is

$$
\Delta(A,D_{\dot a})
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac13\langle P_{\dot a}D^D,D^E\rangle
+\frac23\langle D^D,P_{\dot a}D^E\rangle
\right],
$$

$$
\Delta(D_{\dot a},A)
=\lambda_1\mathbb F^{AB}{}_{DE}
\left[
\frac23\langle P_{\dot a}D^D,D^E\rangle
+\frac13\langle D^D,P_{\dot a}D^E\rangle
\right].
$$

If the supplied data are insufficient to reconstruct a named link, stop at the first missing functional derivative and write its exact mathematical definition. Do not infer it from holomorphic twist.
