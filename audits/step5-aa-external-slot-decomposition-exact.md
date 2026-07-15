# Step 5 AA external-slot decomposition

Status: `TARGET_BLIND_AA_FULL_POLARIZED_TYPED_ORDERED_RECONSTRUCTION_EXACT__RAW_SD_CONTACT_MULTIPLICITY_ONE_VERIFIED`.

External target used: `false`.

AA raw-contact/typed-sector unresolved gate: `none`.

## 1. Notation

$$
Q=t_1Q_1+t_2Q_2,
\qquad
E=t_EE,
\qquad
U=Q+E.
$$

$$
\mathscr D_+=D_\alpha,
\qquad
\mathscr D_-=\bar D_{\dot\alpha},
$$

$$
W_+^{(1)}(U)_\alpha
=-\frac{\sqrt2}8\bar D^2D_\alpha U,
\qquad
W_-^{(1)}(U)_{\dot\alpha}
=-\frac{\sqrt2}8D^2\bar D_{\dot\alpha}U.
$$

The compact cubic word is

$$
S_\chi^{(3)}
=c_\chi\int
\operatorname{Tr}
\left(
W_\chi^{(1)}(U)
[\mathscr D_\chi U,U]
\right),
\qquad
c_+=-\frac14,
\qquad
c_-=+\frac14.
$$

## 2. Three external placements

The labeled Hessian is

$$
H_\chi^{\rm full}
=[t_1t_2t_E]S_\chi^{(3)}.
$$

Linear field-strength placement:

$$
\begin{aligned}
H_\chi^{W}
=c_\chi\operatorname{Tr}\bigl(&
W_\chi^{(1)}(E)[\mathscr D_\chi Q_1,Q_2]\\
&+W_\chi^{(1)}(E)[\mathscr D_\chi Q_2,Q_1]
\bigr).
\end{aligned}
$$

Derivative-commutator placement:

$$
\begin{aligned}
H_\chi^{\partial C}
=c_\chi\operatorname{Tr}\bigl(&
W_\chi^{(1)}(Q_1)[\mathscr D_\chi E,Q_2]\\
&+W_\chi^{(1)}(Q_2)[\mathscr D_\chi E,Q_1]
\bigr).
\end{aligned}
$$

Plain-commutator placement:

$$
\begin{aligned}
H_\chi^{C}
=c_\chi\operatorname{Tr}\bigl(&
W_\chi^{(1)}(Q_1)[\mathscr D_\chi Q_2,E]\\
&+W_\chi^{(1)}(Q_2)[\mathscr D_\chi Q_1,E]
\bigr).
\end{aligned}
$$

Therefore

$$
\boxed{
H_\chi^{\rm full}
=H_\chi^W+H_\chi^{\partial C}+H_\chi^C
}.
$$

## 3. Raw labeled-port partition

For each chirality,

$$
N_W=8,
\qquad
N_{\partial C}=8,
\qquad
N_C=8,
\qquad
N_{\rm full}=24.
$$

Across both chiralities,

$$
N_{\rm old\ fixed}=16,
\qquad
N_{\rm omitted}=32.
$$

The omitted classes are exactly derivative-commutator and
plain-commutator placements.

## 4. Exact sparse-component rows

| id | sector/type | (H^W) | (H^{\partial C}) | (H^C) | full | old fixed |
|---|---|---:|---:|---:|---:|---:|
| plus_A_00 | +/A | 3/8*sqrt(2) | -3/32*sqrt(2) | -3/32*sqrt(2) | 3/16*sqrt(2) | 3/8*sqrt(2) |
| plus_A_1_13 | +/A | -3/32*sqrt(2) - 1/32*i sqrt(2) | 1/32*sqrt(2) + 3/128*i sqrt(2) | 1/64*sqrt(2) - 1/128*i sqrt(2) | -3/64*sqrt(2) - 1/64*i sqrt(2) | -3/32*sqrt(2) - 1/32*i sqrt(2) |
| minus_A_cross | -/A | 3/8*sqrt(2) | -3/32*sqrt(2) | -3/32*sqrt(2) | 3/16*sqrt(2) | 0 |
| minus_D_0_4 | -/D | 1/32*sqrt(2) + 3/64*i sqrt(2) | -3/128*i sqrt(2) | -3/128*i sqrt(2) | 1/32*sqrt(2) | 1/32*sqrt(2) + 3/64*i sqrt(2) |
| plus_D_cross | +/D | 1/16*sqrt(2) | -1/64*sqrt(2) | -1/64*sqrt(2) | 1/32*sqrt(2) | 0 |

Every row obeys

$$
H^W+H^{\partial C}+H^C-H^{\rm full}=0.
$$

For matched ((+,A)) and ((-,D)), the old probe equals (H^W), not the
full Hessian.  Its explicit early gate also sets ((-,A)) and ((+,D)) to
zero before evaluating even (H^W).

## 5. Full interaction sector-pair sum

Let (H_\chi^D(L)) and (H_\psi^A(R)) be the fully polarized action
Hessians at the left and right labeled vertices.  Since both cubic action
vertices are even,

$$
\begin{aligned}
&\frac1{2!}
\sum_{\chi,\psi\in\{+,-\}}
\left[
H_\chi^D(L)H_\psi^A(R)
+H_\psi^A(R)H_\chi^D(L)
\right]\\
&=\sum_{\chi,\psi\in\{+,-\}}
H_\chi^D(L)H_\psi^A(R).
\end{aligned}
$$

Thus the (1/2!) is cancelled by the two left/right action-label
assignments; every sector pair has weight one:

$$
(++),\qquad (+-),\qquad (-+),\qquad (--).
$$

At the exact held-out point

$$
\ell=(3,2,-2,1),
$$

the full probe gives

$$
N_{++}=N_{+-}=N_{-+}=N_{--}
=-\frac{97}4+\frac{103}2i,
$$

$$
N_{\rm full\ sector\ sum}=-97+206i.
$$

For every sector pair,

$$
N_{\rm selected}=-49+97i,
\qquad
N_{\rm longitudinal}=\frac{99}4-\frac{91}2i,
$$

$$
N_{\rm selected}+N_{\rm longitudinal}
=-\frac{97}4+\frac{103}2i.
$$

The old fixed-strength probe instead gives

$$
(N_{++},N_{+-},N_{-+},N_{--})_{\rm fixed}
=(0,0,7+4i,0).
$$

Hence same-chirality rows cannot be removed by the old fixed-(W) graph
typing.  It omitted both two external-position classes and three sector
pairs.

## 6. Same-edge source quotient

Define

$$
T_0=I0\_DminusA1[A]*A1[B],
\qquad
T_2=I0\_A1[A]*DminusA1[B].
$$

The full-action aggregate selected numerators are exactly edge-divisible:

$$
N_{S,T_0}=\bar r_0^2Q_0,
\qquad
N_{S,T_2}=\bar r_2^2Q_2,
$$

with zero polynomial-division remainders and

$$
\begin{aligned}
Q_0={}&-\frac12l_0^2+il_0l_1
+\left(\frac32-i\right)l_0+\frac12l_1^2\\
&-\left(1+\frac32i\right)l_1-\frac12+\frac32i,
\end{aligned}
$$

$$
Q_2=-\frac12l_0^2+il_0l_1-\frac12l_0
+\frac12l_1^2+\frac i2l_1.
$$

The quotient is quadratic, not affine.  Its homogeneous quadratic sum is

$$
Q_0^{(2)}+Q_2^{(2)}
=-(l_0-il_1)^2,
\qquad
(\partial_{l_0}^2+\partial_{l_1}^2)
\left(Q_0^{(2)}+Q_2^{(2)}\right)=0.
$$

For each selected-parent row

$$
\rho=(T_s,R_L,R_R,\text{Wick pairing}),
$$

the exact statement already proved is

$$
N_{S,\rho}=Q_\rho\bar r_{e(\rho)}^2,
\qquad
N_{{\rm full},\rho}=N_{S,\rho}+L_\rho.
$$

The source occurrence is tagged before either action Hessian is multiplied.
For external colors ((D,A)=(1,0)), exact color support gives

$$
\epsilon(c_0,c_1,1)\epsilon(c_1,c_2,0)\ne0
\quad\Longleftrightarrow\quad
(c_0,c_1,c_2)=(0,2,1).
$$

Consequently

$$
T_0\longmapsto e_0,
\qquad
T_2\longmapsto e_2.
$$

Schwinger differentiation is linear in the occurrence projector:

$$
P_T\left(SH_LH_R\right)=P_T(S)H_LH_R.
$$

Reflection acts only on the action placements,

$$
\mathcal R(T,H_L,H_R)=(T,H_R,H_L),
$$

so it cannot exchange the physical source edge.

The raw cubic port table contains, for every chirality, raw word, and
external placement, exactly two ordered quantum-role rows,

$$
(S,B),
\qquad
(B,S).
$$

These are the two-line Wick endpoints inside the same ordered Hessian.  For
each physical edge the exact count is

$$
\frac1{2!}
\times 2_{\rm action\ ordering}
\times 2_{\rm Wick\ endpoint}
=2_{\rm endpoint\ rows}.
$$

The parent Hessian contains the same two endpoint rows.  Writing their
full-((d)) numerators as ((N_{SB})) and ((N_{BS})),

$$
\frac1{2!}
\left[(N_{SB}+N_{BS})+(N_{SB}+N_{BS})\right]
=N_{SB}+N_{BS}.
$$

The Gaussian product rule is

$$
\left\langle F_eK_ev_e\right\rangle
-\hbar\left\langle\frac{\delta F_e}{\delta v_e}\right\rangle
=0.
$$

It maps each endpoint row bijectively with the relative minus sign,

$$
K_{\mathrm{raw},SB}=-N_{d,SB},
\qquad
K_{\mathrm{raw},BS}=-N_{d,BS}.
$$

Therefore, separately on ((e_0)) and ((e_2)),

$$
N_{d,e}=L_e+Q_er_{e,d}^2,
\qquad
K_{\mathrm{raw},e}=-L_e-Q_er_{e,d}^2,
$$

$$
\boxed{N_{d,e}+K_{\mathrm{raw},e}=0},
\qquad
m_0=m_2=1.
$$

The DRED residue is consequently

$$
\boxed{
N_{{\rm full},e}+K_{\mathrm{raw},e}
=Q_e\left(\bar r_e^2-r_{e,d}^2\right)
=Q_e\mu_\ell^2
}.
$$

Thus the combined source/action/Wick row edge map is
`CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA`.  The old fixed-(W) audit
computed only the ((W,W)) block.  No affine fit or target coefficient is
used.  The raw normalization status is
`CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE`.

## 7. Target-blind typed reconstruction

The dotted-index convention used by the component engine is

$$
k_+^{\dot0}=\sigma_E(k)_{0\dot1},
\qquad
k_+^{\dot1}=-\sigma_E(k)_{0\dot0}.
$$

$$
k_-^{\dot0}=\sigma_E(k)_{1\dot1},
\qquad
k_-^{\dot1}=-\sigma_E(k)_{1\dot0}.
$$

| frame | $\epsilon\cdot p$ | $\epsilon\cdot q$ | $p_+^{\dot a}$ | $q_+^{\dot a}$ | $p_-^{\dot a}$ | $q_-^{\dot a}$ | $2\int(Q_0+Q_2)$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| canonical | 0 | 0 | -I | -1 | 0 | 0 | -1/2 + I |
| alternate | 0 | 0 | -1 | I | 0 | 0 | 1 + I/2 |
| p_transverse | 0 | 0 | -I | 0 | 0 | 1 | -5/6 |
| q_transverse | 0 | 0 | 0 | -I | 1 | 0 | -13/12 |
| swapped_transverse | 0 | 0 | -1 | -I | 0 | 0 | -1 + I/2 |

The former `p_only` and `q_only` frames both obey

$$
\epsilon\cdot q=1,
$$

and are rejected as `REJECTED_LONGITUDINAL_FRAME`.

Although `p_transverse` and `q_transverse` obey

$$
p_-^{\dot a}q_-^{\dot a}\ne0,
$$

on one unselected momentum, they contain the exact opposite-undotted
coefficients ((-1/3)) and ((-1/12)).  They are retained for edge/contact
checks and rejected from the typed solve as
`REJECTED_OPPOSITE_UNDOTTED_CONTAMINATION_FOR_TYPED_SOLVE`.

The canonical and swapped-transverse rows instead give

$$
\begin{pmatrix}
-i&-1\\
-1&-i
\end{pmatrix}
\begin{pmatrix}c_p\\c_q\end{pmatrix}
=
\begin{pmatrix}
-\frac12+i\\
-1+\frac i2
\end{pmatrix},
$$

$$
\det
\begin{pmatrix}
-i&-1\\
-1&-i
\end{pmatrix}
=-2,
\qquad
c_p=-\frac i2,
\qquad
c_q=-i.
$$

The independent alternate frame obeys

$$
-c_p+ic_q=1+\frac i2.
$$

The exact global factor omitted by the normalized probe is

$$
g^2\left(-\frac1\hbar\right)^2(-\hbar)^3
=-\hbar g^2.
$$

For every sector pair,

$$
\frac1{2!}\times2=1,
$$

and all four sector polynomials are equal.  Therefore

$$
4\left(-\hbar g^2\right)
\left(\frac1{32\pi^2}\right)
\left(\frac{16\pi^2}{\hbar g^2}\right)
=-2
$$

in ((\lambda_1)) units.  Reflection is a distinct ordered output with
weight one, and dotted-index reordering gives

$$
p_{+\dot\alpha}A D^{\dot\alpha}
=-D_{\dot\alpha}p_+^{\dot\alpha}A.
$$

The raw contact multiplicities ((m_0=m_2=1)) are now verified.  In the
ordered basis

$$
(DA_p,DA_q,AD_p,AD_q),
$$

$$
\boxed{
\frac{\Gamma_{AA,g}^{(1)}}
{\lambda_1\mathbb F^{AB}_{DE}}
=\left(
i,
2i,
-i,
-2i
\right)
}.
$$

The common Fourier map is

$$
\mathcal F_{\rm common}=-i,
$$

so the extended ordered vector becomes

$$
(1,2,-1,-2).
$$

The two ((q)) rows are separately typed as

$$
DA_q=(P\!\cdot\!D)A,
\qquad
AD_q=A(P\!\cdot\!D),
$$

and are EOM/divergence carriers.  They are not identified with ((p+q)).
Only after this typed quotient,

$$
(DA_p,DA_q,AD_p,AD_q)
\longmapsto
(DA_p,0,AD_p,0),
$$

$$
\boxed{
\frac{\Gamma_{AA,g}^{(1),\rm phys}}
{\lambda_1\mathbb F^{AB}_{DE}}
=DA_p-AD_p
},
$$

so the direct and reflected physical coefficients are ((+1)) and ((-1)).

The two Wick endpoints occur in both ((N_d)) and ((K_{\rm raw})); they do
not multiply their ratio.  Hence there is no extra edge factor two and no
global metric-trace factor ((d)) or ((4)).

No holomorphic-twist target is used.

## 8. Matter primitive sign

The exact finite Grassmann words are

$$
\mathcal G_0=-16384\mathcal S_{012},
\qquad
\mathcal G_2=-16384\mathcal T_{012}.
$$

All remaining primitive signs give

$$
\eta_{\rm src}
=\operatorname{sgn}\left(-\frac18\right)^2
\left[(-1)(-1)\right]^2
(-1)^2(+1)
\left(\frac1{2!}2\right)(+1)
=+1.
$$

Hence

$$
C^D>B^E=-\lambda_1,
\qquad
B^D>C^E=+\lambda_1,
$$

$$
\boxed{(c_{BC},c_{CB})=(1,-1)}.
$$

## 9. Exhaustive replay record

```json
{
  "color_zero_proof": "epsilon(c1,c2,c_external)=0 unless all three colors are distinct",
  "frame": {
    "background_momentum": [
      "1",
      "-3",
      "-1",
      "-1"
    ],
    "momentum_1": [
      "1",
      "2",
      "0",
      "1"
    ],
    "momentum_2": [
      "-2",
      "1",
      "1",
      "0"
    ],
    "polarization": [
      "0",
      "0",
      "0",
      "1"
    ]
  },
  "summaries": {
    "+_A": {
      "all_color_mask_rows": 2304,
      "analytic_color_zero_rows": 1792,
      "equality_failures": 0,
      "fingerprints": {
        "derivative_commutator": {
          "sum": "0",
          "weighted_sum": "-5/32*sqrt(2) - 3/8*i sqrt(2)"
        },
        "derivative_plus_plain": {
          "sum": "0",
          "weighted_sum": "-11/16*sqrt(2) - 5/8*i sqrt(2)"
        },
        "full": {
          "sum": "0",
          "weighted_sum": "9/16*sqrt(2) - 5/8*i sqrt(2)"
        },
        "linear_field_strength": {
          "sum": "0",
          "weighted_sum": "5/4*sqrt(2)"
        },
        "plain_commutator": {
          "sum": "0",
          "weighted_sum": "-17/32*sqrt(2) - 1/4*i sqrt(2)"
        }
      },
      "nonzero_counts": {
        "derivative_commutator": 112,
        "derivative_plus_plain": 104,
        "full": 88,
        "linear_field_strength": 66,
        "old_fixed_full_mismatch": 104,
        "old_fixed_model": 66,
        "plain_commutator": 112
      },
      "sparse_replayed_rows": 512
    },
    "+_D": {
      "all_color_mask_rows": 2304,
      "analytic_color_zero_rows": 1792,
      "equality_failures": 0,
      "fingerprints": {
        "derivative_commutator": {
          "sum": "0",
          "weighted_sum": "-1/4*sqrt(2)"
        },
        "derivative_plus_plain": {
          "sum": "0",
          "weighted_sum": "-9/16*sqrt(2) - 1/16*i sqrt(2)"
        },
        "full": {
          "sum": "0",
          "weighted_sum": "7/16*sqrt(2) + 3/16*i sqrt(2)"
        },
        "linear_field_strength": {
          "sum": "0",
          "weighted_sum": "sqrt(2) + 1/4*i sqrt(2)"
        },
        "plain_commutator": {
          "sum": "0",
          "weighted_sum": "-5/16*sqrt(2) - 1/16*i sqrt(2)"
        }
      },
      "nonzero_counts": {
        "derivative_commutator": 44,
        "derivative_plus_plain": 44,
        "full": 52,
        "linear_field_strength": 40,
        "old_fixed_full_mismatch": 52,
        "old_fixed_model": 0,
        "plain_commutator": 40
      },
      "sparse_replayed_rows": 512
    },
    "-_A": {
      "all_color_mask_rows": 2304,
      "analytic_color_zero_rows": 1792,
      "equality_failures": 0,
      "fingerprints": {
        "derivative_commutator": {
          "sum": "0",
          "weighted_sum": "-45/32*sqrt(2) - 1/8*i sqrt(2)"
        },
        "derivative_plus_plain": {
          "sum": "0",
          "weighted_sum": "-39/16*sqrt(2) - 3/8*i sqrt(2)"
        },
        "full": {
          "sum": "0",
          "weighted_sum": "9/16*sqrt(2) - 5/8*i sqrt(2)"
        },
        "linear_field_strength": {
          "sum": "0",
          "weighted_sum": "3*sqrt(2) - 1/4*i sqrt(2)"
        },
        "plain_commutator": {
          "sum": "0",
          "weighted_sum": "-33/32*sqrt(2) - 1/4*i sqrt(2)"
        }
      },
      "nonzero_counts": {
        "derivative_commutator": 108,
        "derivative_plus_plain": 100,
        "full": 88,
        "linear_field_strength": 66,
        "old_fixed_full_mismatch": 88,
        "old_fixed_model": 0,
        "plain_commutator": 104
      },
      "sparse_replayed_rows": 512
    },
    "-_D": {
      "all_color_mask_rows": 2304,
      "analytic_color_zero_rows": 1792,
      "equality_failures": 0,
      "fingerprints": {
        "derivative_commutator": {
          "sum": "0",
          "weighted_sum": "-1/8*sqrt(2) - 1/16*i sqrt(2)"
        },
        "derivative_plus_plain": {
          "sum": "0",
          "weighted_sum": "-3/16*sqrt(2) - 1/16*i sqrt(2)"
        },
        "full": {
          "sum": "0",
          "weighted_sum": "7/16*sqrt(2) + 3/16*i sqrt(2)"
        },
        "linear_field_strength": {
          "sum": "0",
          "weighted_sum": "5/8*sqrt(2) + 1/4*i sqrt(2)"
        },
        "plain_commutator": {
          "sum": "0",
          "weighted_sum": "-1/16*sqrt(2)"
        }
      },
      "nonzero_counts": {
        "derivative_commutator": 52,
        "derivative_plus_plain": 48,
        "full": 52,
        "linear_field_strength": 64,
        "old_fixed_full_mismatch": 48,
        "old_fixed_model": 64,
        "plain_commutator": 44
      },
      "sparse_replayed_rows": 512
    }
  },
  "total_analytic_color_zero_rows": 7168,
  "total_equality_failures": 0,
  "total_full_color_mask_rows": 9216,
  "total_sparse_replayed_rows": 2048
}
```

$$
N_{\rm pass}=269,
\qquad
N_{\rm fail}=0.
$$
