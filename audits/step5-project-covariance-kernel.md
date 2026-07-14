# Step 5 Project covariance-kernel audit

Authority: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, verify run `29306335742`.  本 audit 只使用 locked Project inputs；没有读取 holomorphic-twist target，也没有读取任何 unmerged Step-5 derivation file.

## 1. Exact Grassmann calculation

令 exterior-variable order 为

$$
\theta_1<\theta_2<\theta_3<\theta'_1<\theta'_2<\theta'_3,
\qquad
D_r:=\frac{\vec\partial}{\partial\theta_r}
+\frac{\vec\partial}{\partial\theta'_r}.
$$

Degree-three space dimension 与 stacked constraint 为

$$
\dim\Lambda^3(K^6)=\binom63=20,
\qquad
(D_1,D_2,D_3):\Lambda^3(K^6)\longrightarrow
\Lambda^2(K^6)^{\oplus3}.
$$

Exact rational RREF gives

$$
\operatorname{rank}(D_1,D_2,D_3)=19,
\qquad
\dim\bigcap_{r=1}^3\ker D_r=20-19=1.
$$

Its generator is

$$
K(\theta,\theta')
=(\theta_1-\theta'_1)(\theta_2-\theta'_2)(\theta_3-\theta'_3),
$$

with fully normal-ordered expansion

$$
K=1\,\theta_1 \theta_2 \theta_3 - 1\,\theta_2 \theta_3 \theta'_1 + 1\,\theta_1 \theta_3 \theta'_2 + 1\,\theta_3 \theta'_1 \theta'_2 - 1\,\theta_1 \theta_2 \theta'_3 - 1\,\theta_2 \theta'_1 \theta'_3 + 1\,\theta_1 \theta'_2 \theta'_3 - 1\,\theta'_1 \theta'_2 \theta'_3.
$$

The exact program output is

$$
D_1K=D_2K=D_3K=0.
$$

All invariant dimensions are

$$
(\dim I^0,\ldots,\dim I^6)=(1,3,3,1,0,0,0).
$$

因此 degree-three diagonal-translation invariant polynomial space 恰为

$$
\operatorname{Span}_{K}\!\left\{K(\theta,\theta')\right\}.
$$

## 2. Conditional weighted superletter algebra

不预设 numerical normalization，写

$$
\mathcal C(\theta)
=aU+b\theta_rC_r
+\frac c2\varepsilon_{rst}\theta_r\theta_sB_t
+d\theta_1\theta_2\theta_3A,
\qquad abcd\ne0.
$$

若 physical residual action 已另行证明满足

$$
q_r\mathcal C(\theta)
=\frac{\vec\partial}{\partial\theta_r}\mathcal C(\theta),
$$

then coefficient comparison gives

$$
q_rU=\frac baC_r,
\qquad
q_rC_s=\frac cb\varepsilon_{rst}B_t,
\qquad
q_rB_s=\frac dc\delta_{rs}A,
\qquad
q_rA=0.
$$

Hence

$$
\{q_r,q_s\}U
=\frac ca(\varepsilon_{srt}+\varepsilon_{rst})B_t=0,
$$

$$
\{q_r,q_s\}C_t
=\frac db(\varepsilon_{str}+\varepsilon_{rts})A=0,
$$

and the anticommutator vanishes on (B_t,A) directly.  This proves the abstract index/sign map for arbitrary (a,b,c,d\ne0); it does not select the Project normalization.

## 3. Conditional intertwiner

For

$$
\Omega(\mathcal C^A,\mathcal C^B)
=\kappa_{\rm color}^{AB}{}_{DE}
K(\theta,\theta')P\mathcal C^D(\theta)P\mathcal C^E(\theta'),
$$

direct graded Leibniz expansion gives

$$
\begin{aligned}
q_r\Omega-\Omega(q_r\otimes1+1\otimes q_r)
={}&\kappa_{\rm color}(D_rK)P\mathcal C\,P\mathcal C\\
&+\kappa_{\rm color}K
\left([q_r,P]\mathcal C\,P\mathcal C
+P\mathcal C\,[q_r,P]\mathcal C\right).
\end{aligned}
$$

Thus it vanishes exactly if (D_rK=0), ([q_r,P]=0), color is inert, and both regulated and cut maps are separately (q_r)-equivariant.  The first condition is proved above; the remaining physical conditions are not present in the locked inputs.

## 4. Ordered-pair census

The conditional weighted compact ansatz emits exactly

$$
64=8\times8,
\qquad
N_{\rm conditional\ nonzero}=27,
\qquad
N_{\rm conditional\ zero}=37.
$$

Every coefficient below is a formal ratio of (a,b,c,d); no numerical value is inferred.

- `U>U`: `0`
- `U>C_1`: `0`
- `U>C_2`: `0`
- `U>C_3`: `0`
- `U>B_1`: `0`
- `U>B_2`: `0`
- `U>B_3`: `0`
- `U>A`: `-1 (a*a)/(a*d) P(U)>P(U)`
- `C_1>U`: `0`
- `C_1>C_1`: `0`
- `C_1>C_2`: `0`
- `C_1>C_3`: `0`
- `C_1>B_1`: `1 (a*a)/(b*c) P(U)>P(U)`
- `C_1>B_2`: `0`
- `C_1>B_3`: `0`
- `C_1>A`: `-1 (b*a)/(b*d) P(C_1)>P(U) + -1 (a*b)/(b*d) P(U)>P(C_1)`
- `C_2>U`: `0`
- `C_2>C_1`: `0`
- `C_2>C_2`: `0`
- `C_2>C_3`: `0`
- `C_2>B_1`: `0`
- `C_2>B_2`: `1 (a*a)/(b*c) P(U)>P(U)`
- `C_2>B_3`: `0`
- `C_2>A`: `-1 (b*a)/(b*d) P(C_2)>P(U) + -1 (a*b)/(b*d) P(U)>P(C_2)`
- `C_3>U`: `0`
- `C_3>C_1`: `0`
- `C_3>C_2`: `0`
- `C_3>C_3`: `0`
- `C_3>B_1`: `0`
- `C_3>B_2`: `0`
- `C_3>B_3`: `1 (a*a)/(b*c) P(U)>P(U)`
- `C_3>A`: `-1 (b*a)/(b*d) P(C_3)>P(U) + -1 (a*b)/(b*d) P(U)>P(C_3)`
- `B_1>U`: `0`
- `B_1>C_1`: `-1 (a*a)/(c*b) P(U)>P(U)`
- `B_1>C_2`: `0`
- `B_1>C_3`: `0`
- `B_1>B_1`: `0`
- `B_1>B_2`: `1 (b*a)/(c*c) P(C_3)>P(U) + 1 (a*b)/(c*c) P(U)>P(C_3)`
- `B_1>B_3`: `-1 (b*a)/(c*c) P(C_2)>P(U) + -1 (a*b)/(c*c) P(U)>P(C_2)`
- `B_1>A`: `-1 (c*a)/(c*d) P(B_1)>P(U) + 1 (b*b)/(c*d) P(C_2)>P(C_3) + -1 (b*b)/(c*d) P(C_3)>P(C_2) + -1 (a*c)/(c*d) P(U)>P(B_1)`
- `B_2>U`: `0`
- `B_2>C_1`: `0`
- `B_2>C_2`: `-1 (a*a)/(c*b) P(U)>P(U)`
- `B_2>C_3`: `0`
- `B_2>B_1`: `-1 (b*a)/(c*c) P(C_3)>P(U) + -1 (a*b)/(c*c) P(U)>P(C_3)`
- `B_2>B_2`: `0`
- `B_2>B_3`: `1 (b*a)/(c*c) P(C_1)>P(U) + 1 (a*b)/(c*c) P(U)>P(C_1)`
- `B_2>A`: `-1 (c*a)/(c*d) P(B_2)>P(U) + -1 (b*b)/(c*d) P(C_1)>P(C_3) + 1 (b*b)/(c*d) P(C_3)>P(C_1) + -1 (a*c)/(c*d) P(U)>P(B_2)`
- `B_3>U`: `0`
- `B_3>C_1`: `0`
- `B_3>C_2`: `0`
- `B_3>C_3`: `-1 (a*a)/(c*b) P(U)>P(U)`
- `B_3>B_1`: `1 (b*a)/(c*c) P(C_2)>P(U) + 1 (a*b)/(c*c) P(U)>P(C_2)`
- `B_3>B_2`: `-1 (b*a)/(c*c) P(C_1)>P(U) + -1 (a*b)/(c*c) P(U)>P(C_1)`
- `B_3>B_3`: `0`
- `B_3>A`: `-1 (c*a)/(c*d) P(B_3)>P(U) + 1 (b*b)/(c*d) P(C_1)>P(C_2) + -1 (b*b)/(c*d) P(C_2)>P(C_1) + -1 (a*c)/(c*d) P(U)>P(B_3)`
- `A>U`: `1 (a*a)/(d*a) P(U)>P(U)`
- `A>C_1`: `-1 (b*a)/(d*b) P(C_1)>P(U) + -1 (a*b)/(d*b) P(U)>P(C_1)`
- `A>C_2`: `-1 (b*a)/(d*b) P(C_2)>P(U) + -1 (a*b)/(d*b) P(U)>P(C_2)`
- `A>C_3`: `-1 (b*a)/(d*b) P(C_3)>P(U) + -1 (a*b)/(d*b) P(U)>P(C_3)`
- `A>B_1`: `1 (c*a)/(d*c) P(B_1)>P(U) + -1 (b*b)/(d*c) P(C_2)>P(C_3) + 1 (b*b)/(d*c) P(C_3)>P(C_2) + 1 (a*c)/(d*c) P(U)>P(B_1)`
- `A>B_2`: `1 (c*a)/(d*c) P(B_2)>P(U) + 1 (b*b)/(d*c) P(C_1)>P(C_3) + -1 (b*b)/(d*c) P(C_3)>P(C_1) + 1 (a*c)/(d*c) P(U)>P(B_2)`
- `A>B_3`: `1 (c*a)/(d*c) P(B_3)>P(U) + -1 (b*b)/(d*c) P(C_1)>P(C_2) + 1 (b*b)/(d*c) P(C_2)>P(C_1) + 1 (a*c)/(d*c) P(U)>P(B_3)`
- `A>A`: `-1 (d*a)/(d*d) P(A)>P(U) + -1 (c*b)/(d*d) P(B_1)>P(C_1) + -1 (c*b)/(d*d) P(B_2)>P(C_2) + -1 (c*b)/(d*d) P(B_3)>P(C_3) + -1 (b*c)/(d*d) P(C_1)>P(B_1) + -1 (b*c)/(d*d) P(C_2)>P(B_2) + -1 (b*c)/(d*d) P(C_3)>P(B_3) + -1 (a*d)/(d*d) P(U)>P(A)`

The named physical alphabet contains

$$
1+3+3+2=9,
\qquad 9\times9=81
$$

ordered pairs.  Reversed words are retained as different records:

- `nabla_+W_+>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+W_+>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_1>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_2>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `nabla_+Phi_3>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_1>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_2>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildePhi_3>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot1>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>nabla_+W_+`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>nabla_+Phi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>nabla_+Phi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>nabla_+Phi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>tildePhi_1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>tildePhi_2`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>tildePhi_3`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>tildeW_dot1`: `BLOCKED_TYPED_COMPONENT_MAP`
- `tildeW_dot2>tildeW_dot2`: `BLOCKED_TYPED_COMPONENT_MAP`

## 5. Exact blockers

- `BLOCKED_STEP5_LETTER_PROJECTIONS_ABSENT`: Normalized identification of U,C_r,B_r,A with the four Step-5 Project letter families. The locked contracts define N=4 component fields and vector/chiral representations, while tasks/CURRENT.yaml only names nabla_+W_+, nabla_+Phi_r, tildePhi_r, tildeW_dot-a; it does not define their plus-spin-frame projections or compact-slot map.
- `BLOCKED_RESIDUAL_Q_SELECTION_AND_NORMALIZATION`: Physical q_r action and the numerical compact weights a,b,c,d. Step 4C equations (4C.44)-(4C.47) provide all epsilon and tilde-epsilon transformations, but no locked input selects the three residual components q_r, their spinor slots, or their normalization after the Step-5 projection.
- `BLOCKED_TREE_EULER_TO_COMPACT_DESCENDANT_MAP`: Derivation of the compact weights from tree Euler descendants. Step 4C equations (4C.68)-(4C.69a1) fix component Euler operators, but no locked input derives the specific Schwinger descendants of the four Step-5 letters or maps them to U,C_r,B_r,A and P_dot.
- `BLOCKED_DRED_CUT_OPERATOR_NOT_LOCKED`: Unconditional intertwining of the physical DRED-minus-cut commutator with q_r. No allowed Project contract defines the DRED field continuation, regulated cut operator, or their action on the projected Step-5 letter complex.
- `BLOCKED_LOCAL_COHOMOLOGY_COMPLEX_NOT_LOCKED`: Uniqueness of the full local bilinear two-holomorphic-derivative cocycle. Diagonal theta-translation invariance fixes the Grassmann polynomial, but the locked inputs do not specify the Step-5 local-operator space, color-tensor sector, derivative-weight restriction, BRST/EOM quotient, or admissible counterterm coboundaries.

Therefore the full Project cocycle uniqueness, numerical superletter normalization, physical (q_r) intertwining, and the 81 physical results are not proved by this audit.  The exact verdict is `BLOCKED_PROJECT_NORMALIZATION_AND_PHYSICAL_INTERTWINING`.

## 6. Mutation tests

- `T01_DEGREE3_KERNEL_DIMENSION`: PASS; `{"domain": 20, "nullity": 1, "stacked_rows": 45}`
- `T02_KERNEL_EQUALS_PRODUCT_OF_DIFFERENCES`: PASS; `{"basis_to_product_ratio": "-1", "same_span": true}`
- `T03_DIAGONAL_TRANSLATION_CLOSURE`: PASS; `{"D_1_term_count": 0, "D_2_term_count": 0, "D_3_term_count": 0}`
- `T04_PLUS_MUTATION_DETECTED`: PASS; `{"D_1_term_count": 4, "D_2_term_count": 4, "D_3_term_count": 4}`
- `T05_TERM_DELETION_MUTATION_DETECTED`: PASS; `{"D_1_term_count": 1, "D_2_term_count": 1, "D_3_term_count": 1}`
- `T06_WEIGHTED_Q_ANTICOMMUTATOR`: PASS; `"a=2,b=3,c=5,d=7"`
- `T07_Q_INDEX_SIGN_MUTATION_DETECTED`: PASS; `"sign of q_1(C_2)->B_3 reversed"`
- `T08_COMPACT_ORDERED_PAIR_CENSUS`: PASS; `{"conditional_nonzero": 27, "conditional_zero": 37, "total": 64}`
- `T09_PHYSICAL_ORDERED_PAIR_CENSUS`: PASS; `{"distinct_ordered_words": 81, "total": 81}`
- `T10_REVERSED_WORDS_RETAINED`: PASS; `{"off_diagonal_directional_rows": 72}`
- `T11_DETERMINISTIC_EXPANSION`: PASS; `"e1e3acf6382eae2be7657e0a1af48bd72faba20033478b828dfd9caeb46c2f04"`
- `T12_NORMALIZATION_UNDERDETERMINATION_WITNESS`: PASS; `{"normalization_1": "(a,b,c,d)=(1,1,1,1)", "normalization_2": "(a,b,c,d)=(2,3,5,7)", "representations_are_distinct": true}`
