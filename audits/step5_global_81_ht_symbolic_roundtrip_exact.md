# Step-5 global 81 / HT symbolic round-trip exact audit

Status: `PASS_81_DIRECT_OUTPUT_WORDS_AND_ALL_MN_SYMBOLIC_KERNEL_EXACT`

## 1. Target-blind seal boundary

The Project ledger is read, validated, canonicalized, and sealed before the HT artifact is read:

$$
H_P=ec77327d838a45fc139ca90e73ec187c2df6d6f3b5f5318f1587d12a41b3016d.
$$

The HT read records the same prior seal.  No HT coefficient enters the Project derivation.

## 2. Direct 81-row coefficient/output-word equality

For every ordered physical letter pair, the Project ledger word, the independently expanded physical word, and the translated HT word are exactly equal over $\mathbb Q(i,\sqrt2)$:

Here $X[u_1,u_2]>Y[v_1,v_2]$ denotes the ordered component word in the universal contracted-$P_{\dot\alpha}$ kernel.  The displayed $u,v$ are extra jets; the universal contracted derivative inside $\langle X,Y\rangle$ is suppressed.

$$
N_{\rm pair}=81,
\qquad N_{\rm direct\ match}=81,
\qquad N_{\rm mismatch}=0,
$$

$$
81=29_{\rm nonzero}+52_{\rm zero}.
$$

| ordered input | coefficient and ordered output word | equality |
|---|---|---|
| A__A | -1 A[0,0]>D[0,0]; 1 B_1[0,0]>C_1[0,0]; 1 B_2[0,0]>C_2[0,0]; 1 B_3[0,0]>C_3[0,0]; -1 C_1[0,0]>B_1[0,0]; -1 C_2[0,0]>B_2[0,0]; -1 C_3[0,0]>B_3[0,0]; 1 D[0,0]>A[0,0] | EXACT |
| A__B_1 | 1 B_1[0,0]>D[0,0]; -i*sqrt(2) C_2[0,0]>C_3[0,0]; i*sqrt(2) C_3[0,0]>C_2[0,0]; 1 D[0,0]>B_1[0,0] | EXACT |
| A__B_2 | 1 B_2[0,0]>D[0,0]; i*sqrt(2) C_1[0,0]>C_3[0,0]; -i*sqrt(2) C_3[0,0]>C_1[0,0]; 1 D[0,0]>B_2[0,0] | EXACT |
| A__B_3 | 1 B_3[0,0]>D[0,0]; -i*sqrt(2) C_1[0,0]>C_2[0,0]; i*sqrt(2) C_2[0,0]>C_1[0,0]; 1 D[0,0]>B_3[0,0] | EXACT |
| A__C_1 | -1 C_1[0,0]>D[0,0]; 1 D[0,0]>C_1[0,0] | EXACT |
| A__C_2 | -1 C_2[0,0]>D[0,0]; 1 D[0,0]>C_2[0,0] | EXACT |
| A__C_3 | -1 C_3[0,0]>D[0,0]; 1 D[0,0]>C_3[0,0] | EXACT |
| A__D_dot1 | 2/3 D[0,0]>D[1,0]; 1/3 D[1,0]>D[0,0] | EXACT |
| A__D_dot2 | 2/3 D[0,0]>D[0,1]; 1/3 D[0,1]>D[0,0] | EXACT |
| B_1__A | 1 B_1[0,0]>D[0,0]; -i*sqrt(2) C_2[0,0]>C_3[0,0]; i*sqrt(2) C_3[0,0]>C_2[0,0]; 1 D[0,0]>B_1[0,0] | EXACT |
| B_1__B_1 | 0 | EXACT |
| B_1__B_2 | i*sqrt(2) C_3[0,0]>D[0,0]; -i*sqrt(2) D[0,0]>C_3[0,0] | EXACT |
| B_1__B_3 | -i*sqrt(2) C_2[0,0]>D[0,0]; i*sqrt(2) D[0,0]>C_2[0,0] | EXACT |
| B_1__C_1 | 1 D[0,0]>D[0,0] | EXACT |
| B_1__C_2 | 0 | EXACT |
| B_1__C_3 | 0 | EXACT |
| B_1__D_dot1 | 0 | EXACT |
| B_1__D_dot2 | 0 | EXACT |
| B_2__A | 1 B_2[0,0]>D[0,0]; i*sqrt(2) C_1[0,0]>C_3[0,0]; -i*sqrt(2) C_3[0,0]>C_1[0,0]; 1 D[0,0]>B_2[0,0] | EXACT |
| B_2__B_1 | -i*sqrt(2) C_3[0,0]>D[0,0]; i*sqrt(2) D[0,0]>C_3[0,0] | EXACT |
| B_2__B_2 | 0 | EXACT |
| B_2__B_3 | i*sqrt(2) C_1[0,0]>D[0,0]; -i*sqrt(2) D[0,0]>C_1[0,0] | EXACT |
| B_2__C_1 | 0 | EXACT |
| B_2__C_2 | 1 D[0,0]>D[0,0] | EXACT |
| B_2__C_3 | 0 | EXACT |
| B_2__D_dot1 | 0 | EXACT |
| B_2__D_dot2 | 0 | EXACT |
| B_3__A | 1 B_3[0,0]>D[0,0]; -i*sqrt(2) C_1[0,0]>C_2[0,0]; i*sqrt(2) C_2[0,0]>C_1[0,0]; 1 D[0,0]>B_3[0,0] | EXACT |
| B_3__B_1 | i*sqrt(2) C_2[0,0]>D[0,0]; -i*sqrt(2) D[0,0]>C_2[0,0] | EXACT |
| B_3__B_2 | -i*sqrt(2) C_1[0,0]>D[0,0]; i*sqrt(2) D[0,0]>C_1[0,0] | EXACT |
| B_3__B_3 | 0 | EXACT |
| B_3__C_1 | 0 | EXACT |
| B_3__C_2 | 0 | EXACT |
| B_3__C_3 | 1 D[0,0]>D[0,0] | EXACT |
| B_3__D_dot1 | 0 | EXACT |
| B_3__D_dot2 | 0 | EXACT |
| C_1__A | -1 C_1[0,0]>D[0,0]; 1 D[0,0]>C_1[0,0] | EXACT |
| C_1__B_1 | 1 D[0,0]>D[0,0] | EXACT |
| C_1__B_2 | 0 | EXACT |
| C_1__B_3 | 0 | EXACT |
| C_1__C_1 | 0 | EXACT |
| C_1__C_2 | 0 | EXACT |
| C_1__C_3 | 0 | EXACT |
| C_1__D_dot1 | 0 | EXACT |
| C_1__D_dot2 | 0 | EXACT |
| C_2__A | -1 C_2[0,0]>D[0,0]; 1 D[0,0]>C_2[0,0] | EXACT |
| C_2__B_1 | 0 | EXACT |
| C_2__B_2 | 1 D[0,0]>D[0,0] | EXACT |
| C_2__B_3 | 0 | EXACT |
| C_2__C_1 | 0 | EXACT |
| C_2__C_2 | 0 | EXACT |
| C_2__C_3 | 0 | EXACT |
| C_2__D_dot1 | 0 | EXACT |
| C_2__D_dot2 | 0 | EXACT |
| C_3__A | -1 C_3[0,0]>D[0,0]; 1 D[0,0]>C_3[0,0] | EXACT |
| C_3__B_1 | 0 | EXACT |
| C_3__B_2 | 0 | EXACT |
| C_3__B_3 | 1 D[0,0]>D[0,0] | EXACT |
| C_3__C_1 | 0 | EXACT |
| C_3__C_2 | 0 | EXACT |
| C_3__C_3 | 0 | EXACT |
| C_3__D_dot1 | 0 | EXACT |
| C_3__D_dot2 | 0 | EXACT |
| D_dot1__A | 1/3 D[0,0]>D[1,0]; 2/3 D[1,0]>D[0,0] | EXACT |
| D_dot1__B_1 | 0 | EXACT |
| D_dot1__B_2 | 0 | EXACT |
| D_dot1__B_3 | 0 | EXACT |
| D_dot1__C_1 | 0 | EXACT |
| D_dot1__C_2 | 0 | EXACT |
| D_dot1__C_3 | 0 | EXACT |
| D_dot1__D_dot1 | 0 | EXACT |
| D_dot1__D_dot2 | 0 | EXACT |
| D_dot2__A | 1/3 D[0,0]>D[0,1]; 2/3 D[0,1]>D[0,0] | EXACT |
| D_dot2__B_1 | 0 | EXACT |
| D_dot2__B_2 | 0 | EXACT |
| D_dot2__B_3 | 0 | EXACT |
| D_dot2__C_1 | 0 | EXACT |
| D_dot2__C_2 | 0 | EXACT |
| D_dot2__C_3 | 0 | EXACT |
| D_dot2__D_dot1 | 0 | EXACT |
| D_dot2__D_dot2 | 0 | EXACT |

## 3. Arbitrary nonnegative jet theorem

For $m,n\in\mathbb Z_{\ge0}$, $0\le k\le m$, $0\le\ell\le n$,

$$
T^{HT,\mathrm{printed}}_{m,n;k,\ell}
=\frac{\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)},
$$

$$
K^P_{m,n;k,\ell}
=\frac{2\binom mk\binom n\ell}{(m+n+2)(k+\ell+1)}.
$$

Define the corrected HT coefficient by

$$
T^{HT,\mathrm{corrected}}_{m,n;k,\ell}
:=2T^{HT,\mathrm{printed}}_{m,n;k,\ell}.
$$

Since $m+n+2\ge2$ and $k+\ell+1\ge1$,

$$
\boxed{K^P_{m,n;k,\ell}
=2T^{HT,\mathrm{printed}}_{m,n;k,\ell}
=T^{HT,\mathrm{corrected}}_{m,n;k,\ell}}
$$

for all allowed $m,n,k,\ell$.  The exact finite rectangle is

$$
0\le m\le 8,\qquad
0\le n\le 8,
$$

$$
N_{\rm coefficient\ check}=2025,
\qquad N_{\rm mismatch}=0.
$$

Multiplication by each of the 70 matched base output coefficients proves the full 81-row jet tower; the 52 exact-zero rows remain zero.

## 4. Intrinsic AD/DA jets

| ordered input | exact output distribution |
|---|---|
| A__D_dot1 | 2/3 D[0,0]>D[1,0]; 1/3 D[1,0]>D[0,0] |
| D_dot1__A | 1/3 D[0,0]>D[1,0]; 2/3 D[1,0]>D[0,0] |
| A__D_dot2 | 2/3 D[0,0]>D[0,1]; 1/3 D[0,1]>D[0,0] |
| D_dot2__A | 1/3 D[0,0]>D[0,1]; 2/3 D[0,1]>D[0,0] |

For a unit dotted jet $e_{\dot a}$,

$$
K^P_{e_{\dot a};0}=\frac23,
\qquad
K^P_{e_{\dot a};e_{\dot a}}=\frac13.
$$

Hence

$$
\Delta(P_{\dot a}U,A)
=P_{\dot a}\Delta(U,A)-\Delta(U,P_{\dot a}A)
$$

gives

$$
(1,1)-\left(\frac13,\frac23\right)
=\left(\frac23,\frac13\right),
$$

while the right-intrinsic distribution is $(1/3,2/3)$.
