# Step-5 Project--holomorphic-twist typed round-trip audit

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`. HT is `EXTERNAL_TARGET_ONLY`.

## 1. Typed dictionary

Let \(R_A{}^P\) be a color frame, \(U_I{}^r\) a flavor frame, \(S_{\dot a}{}^{\dot b}\) a dotted-spin frame, and \(\rho\ne0\). The exact field map is

$$
\begin{aligned}
b^A&\mapsto-\frac{i\rho}{\sqrt2}R_A{}^P A^P,\\
\beta_I^A&\mapsto\frac{\rho}{\sqrt2}R_A{}^P U_I{}^rB_r^P,\\
\gamma^{IA}&\mapsto\rho R_A{}^P(U^{-1})_r{}^I C_r^P,\\
\partial_{\dot a}c^A&\mapsto i\rho R_A{}^P S_{\dot a}{}^{\dot b}D_{\dot b}^P.
\end{aligned}
$$

The formal slot is odd:

$$
|U|=1,\qquad q_rU=C_r,\qquad P_{\dot a}U=iD_{\dot a}.
$$

Then

$$
C_{HT}(\theta)\mapsto\rho\left[U+\theta_rC_r+
\frac1{2\sqrt2}\varepsilon_{rst}\theta_r\theta_sB_t
-\frac i{\sqrt2}\theta_1\theta_2\theta_3A\right].
$$

Color/trace equations are

$$
R_A{}^P R_B{}^Q\kappa_{PQ}=\delta_{AB},\qquad
t_A=-iR_A{}^PT_P,
$$

$$
f_{AB}{}^C=R_A{}^PR_B{}^Qc_{PQ}{}^R(R^{-1})_R{}^C,
\qquad \operatorname{Tr}_H=-\kappa_H\operatorname{tr}_\kappa.
$$

## 2. Project coefficient and loop scale

The target-blind cut audit gives

$$
\lambda_P=\frac{\hbar_Pg^2}{16\pi^2}.
$$

For

$$
\iota(\hbar_HT Q_{1,HT})\iota^{-1}=s_1\Delta_P,
$$

the WW component fixes

$$
\hbar_HT\kappa_H^2=-\frac{s_1}{\sqrt2}\lambda_P.
$$

Under the conditional total-differential scale \(s_1=s_0=-1/2\),

$$
\hbar_HT\kappa_H^2=\frac{\hbar_Pg^2}{32\sqrt2\pi^2}.
$$

## 3. Compact 64-component round trip

The following is exact within the pinned vendored manual transcription; it is not yet a row-level source-extraction proof.

Exact count:

$$
64=27_{\rm nonzero}+37_{\rm zero},\qquad N_{\rm mismatch}=0.
$$

| ordered pair | Project normalized output |
|---|---|
| U__U | 0 |
| U__C_1 | 0 |
| U__C_2 | 0 |
| U__C_3 | 0 |
| U__B_1 | 0 |
| U__B_2 | 0 |
| U__B_3 | 0 |
| U__A | -i U U |
| C_1__U | 0 |
| C_1__C_1 | 0 |
| C_1__C_2 | 0 |
| C_1__C_3 | 0 |
| C_1__B_1 | -1 U U |
| C_1__B_2 | 0 |
| C_1__B_3 | 0 |
| C_1__A | i C_1 U; -i U C_1 |
| C_2__U | 0 |
| C_2__C_1 | 0 |
| C_2__C_2 | 0 |
| C_2__C_3 | 0 |
| C_2__B_1 | 0 |
| C_2__B_2 | -1 U U |
| C_2__B_3 | 0 |
| C_2__A | i C_2 U; -i U C_2 |
| C_3__U | 0 |
| C_3__C_1 | 0 |
| C_3__C_2 | 0 |
| C_3__C_3 | 0 |
| C_3__B_1 | 0 |
| C_3__B_2 | 0 |
| C_3__B_3 | -1 U U |
| C_3__A | i C_3 U; -i U C_3 |
| B_1__U | 0 |
| B_1__C_1 | -1 U U |
| B_1__C_2 | 0 |
| B_1__C_3 | 0 |
| B_1__B_1 | 0 |
| B_1__B_2 | sqrt(2) C_3 U; -sqrt(2) U C_3 |
| B_1__B_3 | -sqrt(2) C_2 U; sqrt(2) U C_2 |
| B_1__A | -i B_1 U; -i*sqrt(2) C_2 C_3; i*sqrt(2) C_3 C_2; -i U B_1 |
| B_2__U | 0 |
| B_2__C_1 | 0 |
| B_2__C_2 | -1 U U |
| B_2__C_3 | 0 |
| B_2__B_1 | -sqrt(2) C_3 U; sqrt(2) U C_3 |
| B_2__B_2 | 0 |
| B_2__B_3 | sqrt(2) C_1 U; -sqrt(2) U C_1 |
| B_2__A | -i B_2 U; i*sqrt(2) C_1 C_3; -i*sqrt(2) C_3 C_1; -i U B_2 |
| B_3__U | 0 |
| B_3__C_1 | 0 |
| B_3__C_2 | 0 |
| B_3__C_3 | -1 U U |
| B_3__B_1 | sqrt(2) C_2 U; -sqrt(2) U C_2 |
| B_3__B_2 | -sqrt(2) C_1 U; sqrt(2) U C_1 |
| B_3__B_3 | 0 |
| B_3__A | -i B_3 U; -i*sqrt(2) C_1 C_2; i*sqrt(2) C_2 C_1; -i U B_3 |
| A__U | -i U U |
| A__C_1 | i C_1 U; -i U C_1 |
| A__C_2 | i C_2 U; -i U C_2 |
| A__C_3 | i C_3 U; -i U C_3 |
| A__B_1 | -i B_1 U; -i*sqrt(2) C_2 C_3; i*sqrt(2) C_3 C_2; -i U B_1 |
| A__B_2 | -i B_2 U; i*sqrt(2) C_1 C_3; -i*sqrt(2) C_3 C_1; -i U B_2 |
| A__B_3 | -i B_3 U; -i*sqrt(2) C_1 C_2; i*sqrt(2) C_2 C_1; -i U B_3 |
| A__A | i A U; 1 B_1 C_1; 1 B_2 C_2; 1 B_3 C_3; -1 C_1 B_1; -1 C_2 B_2; -1 C_3 B_3; -i U A |

## 4. Physical 81-pair round trip

The following is exact within the pinned vendored manual transcription; every-row equation/line provenance remains blocked.

$$
81=29_{\rm nonzero}+52_{\rm zero}.
$$

| ordered pair | rule | Project output coefficient and extra holomorphic jets |
|---|---|---|
| A__A | BB | 1 D[[0, 0]] A[[0, 0]]; -1 A[[0, 0]] D[[0, 0]]; 1 B_1[[0, 0]] C_1[[0, 0]]; -1 C_1[[0, 0]] B_1[[0, 0]]; 1 B_2[[0, 0]] C_2[[0, 0]]; -1 C_2[[0, 0]] B_2[[0, 0]]; 1 B_3[[0, 0]] C_3[[0, 0]]; -1 C_3[[0, 0]] B_3[[0, 0]] |
| A__B_1 | BETA_B | 1 D[[0, 0]] B_1[[0, 0]]; 1 B_1[[0, 0]] D[[0, 0]]; i*sqrt(2) C_3[[0, 0]] C_2[[0, 0]]; -i*sqrt(2) C_2[[0, 0]] C_3[[0, 0]] |
| A__B_2 | BETA_B | 1 D[[0, 0]] B_2[[0, 0]]; 1 B_2[[0, 0]] D[[0, 0]]; -i*sqrt(2) C_3[[0, 0]] C_1[[0, 0]]; i*sqrt(2) C_1[[0, 0]] C_3[[0, 0]] |
| A__B_3 | BETA_B | 1 D[[0, 0]] B_3[[0, 0]]; 1 B_3[[0, 0]] D[[0, 0]]; i*sqrt(2) C_2[[0, 0]] C_1[[0, 0]]; -i*sqrt(2) C_1[[0, 0]] C_2[[0, 0]] |
| A__C_1 | B_GAMMA | 1 D[[0, 0]] C_1[[0, 0]]; -1 C_1[[0, 0]] D[[0, 0]] |
| A__C_2 | B_GAMMA | 1 D[[0, 0]] C_2[[0, 0]]; -1 C_2[[0, 0]] D[[0, 0]] |
| A__C_3 | B_GAMMA | 1 D[[0, 0]] C_3[[0, 0]]; -1 C_3[[0, 0]] D[[0, 0]] |
| A__D_dot1 | BC | 2/3 D[[0, 0]] D[[1, 0]]; 1/3 D[[1, 0]] D[[0, 0]] |
| A__D_dot2 | BC | 2/3 D[[0, 0]] D[[0, 1]]; 1/3 D[[0, 1]] D[[0, 0]] |
| B_1__A | BETA_B | 1 B_1[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] B_1[[0, 0]]; -i*sqrt(2) C_2[[0, 0]] C_3[[0, 0]]; i*sqrt(2) C_3[[0, 0]] C_2[[0, 0]] |
| B_1__B_2 | BETA_BETA | -i*sqrt(2) D[[0, 0]] C_3[[0, 0]]; i*sqrt(2) C_3[[0, 0]] D[[0, 0]] |
| B_1__B_3 | BETA_BETA | i*sqrt(2) D[[0, 0]] C_2[[0, 0]]; -i*sqrt(2) C_2[[0, 0]] D[[0, 0]] |
| B_1__C_1 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| B_2__A | BETA_B | 1 B_2[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] B_2[[0, 0]]; i*sqrt(2) C_1[[0, 0]] C_3[[0, 0]]; -i*sqrt(2) C_3[[0, 0]] C_1[[0, 0]] |
| B_2__B_1 | BETA_BETA | i*sqrt(2) D[[0, 0]] C_3[[0, 0]]; -i*sqrt(2) C_3[[0, 0]] D[[0, 0]] |
| B_2__B_3 | BETA_BETA | -i*sqrt(2) D[[0, 0]] C_1[[0, 0]]; i*sqrt(2) C_1[[0, 0]] D[[0, 0]] |
| B_2__C_2 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| B_3__A | BETA_B | 1 B_3[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] B_3[[0, 0]]; -i*sqrt(2) C_1[[0, 0]] C_2[[0, 0]]; i*sqrt(2) C_2[[0, 0]] C_1[[0, 0]] |
| B_3__B_1 | BETA_BETA | -i*sqrt(2) D[[0, 0]] C_2[[0, 0]]; i*sqrt(2) C_2[[0, 0]] D[[0, 0]] |
| B_3__B_2 | BETA_BETA | i*sqrt(2) D[[0, 0]] C_1[[0, 0]]; -i*sqrt(2) C_1[[0, 0]] D[[0, 0]] |
| B_3__C_3 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| C_1__A | B_GAMMA | -1 C_1[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] C_1[[0, 0]] |
| C_1__B_1 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| C_2__A | B_GAMMA | -1 C_2[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] C_2[[0, 0]] |
| C_2__B_2 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| C_3__A | B_GAMMA | -1 C_3[[0, 0]] D[[0, 0]]; 1 D[[0, 0]] C_3[[0, 0]] |
| C_3__B_3 | BETA_GAMMA | 1 D[[0, 0]] D[[0, 0]] |
| D_dot1__A | BC | 2/3 D[[1, 0]] D[[0, 0]]; 1/3 D[[0, 0]] D[[1, 0]] |
| D_dot2__A | BC | 2/3 D[[0, 1]] D[[0, 0]]; 1/3 D[[0, 0]] D[[0, 1]] |

The 52 zero rows are:

`B_1__B_1, B_1__C_2, B_1__C_3, B_1__D_dot1, B_1__D_dot2, B_2__B_2, B_2__C_1, B_2__C_3, B_2__D_dot1, B_2__D_dot2, B_3__B_3, B_3__C_1, B_3__C_2, B_3__D_dot1, B_3__D_dot2, C_1__B_2, C_1__B_3, C_1__C_1, C_1__C_2, C_1__C_3, C_1__D_dot1, C_1__D_dot2, C_2__B_1, C_2__B_3, C_2__C_1, C_2__C_2, C_2__C_3, C_2__D_dot1, C_2__D_dot2, C_3__B_1, C_3__B_2, C_3__C_1, C_3__C_2, C_3__C_3, C_3__D_dot1, C_3__D_dot2, D_dot1__B_1, D_dot1__B_2, D_dot1__B_3, D_dot1__C_1, D_dot1__C_2, D_dot1__C_3, D_dot1__D_dot1, D_dot1__D_dot2, D_dot2__B_1, D_dot2__B_2, D_dot2__B_3, D_dot2__C_1, D_dot2__C_2, D_dot2__C_3, D_dot2__D_dot1, D_dot2__D_dot2`.

## 5. Arbitrary derivative tower

The displayed comparison is exact within the pinned vendored manual transcription.

For \(m,n\ge0\), \(0\le k\le m\), \(0\le\ell\le n\),

$$
T^{HT}_{m,n;k,\ell}
=\frac{\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)},
$$

$$
K^P_{m,n;k,\ell}
=\frac{2\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}
=2T^{HT}_{m,n;k,\ell}.
$$

The factor \(2\) is the Feynman-parameter prefactor in

$$
\frac1{D_0D_1D_2}=2\int_{\Delta_2}
\frac{1}{(r^2+\Delta)^3},
$$

not an orientation multiplicity. Therefore \(K^P_{0,0}=1\) and \(T^{HT}_{0,0}=1/2\).

## 6. Two HT source conflicts

$$
\frac{-\kappa_H^2}{\kappa_H^2}=-1,
\qquad
\frac{-1/4}{\kappa_H^2}=-\frac1{4\kappa_H^2}.
$$

The independently fixed Project/component ratio selects the same numerical branch as the main compact display and rejects the intro display unless \(\kappa_H^2=1/4\).  This classifies the conflict; it does not repair the HT source.

$$
K^P_{m,n}=2T^{HT}_{m,n}
$$

for every derivative degree. Thus the printed zero-component branch matches Project, while printed \(\mathcal D^{\rm tri}\) and Appendix-B branches require the missing factor \(2\).  Until a source-side directed Wick derivation or erratum fixes one branch, the target status is `BLOCKED_REFERENCE_INTERNAL_NORMALIZATION`.

## 7. Explicit blockers

- `BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE`: The 64 compact rows, 81 physical rows, and derivative rule are checked against a pinned manual transcription. They do not yet carry equation/line provenance for every row, and no source-coefficient mutation is parsed through to the target comparison.
- `BLOCKED_REFERENCE_INTERNAL_NORMALIZATION`: The printed HT source assigns unequal coefficients to identically typed zero-shift and compact statements. Project can classify both branches but cannot turn the inconsistent source into one equality target.
- `BLOCKED_U_NOT_DEFINED_BY_LOCKED_PROJECT_INPUTS`: The c/U slot and total Q0 round trip remain conditional; all physical A,B,C,D rows are unaffected.
- `BLOCKED_TREE_INTERTWINER_REQUIRES_FORMAL_U_AND_FULL_TREE_EOM_MAP`: s_0=-1/2 and hence s_1=s_0 are a typed conditional dictionary, not a locked Project theorem.
- `BLOCKED_SINGLE_KAPPA_H_FOR_GENERAL_REDUCTIVE_GAUGE_ALGEBRA`: The displayed color/trace map is total factorwise for simple factors; CURRENT does not restrict the Project gauge algebra to one simple factor.

Checks: `47/47` PASS.
