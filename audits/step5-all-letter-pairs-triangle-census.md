# Step 5 all ordered letter pairs: triangle and marked-cut census

Status: `BLOCKED_RAW_ALL_PAIR_TRIANGLE_AND_DESCENDANT_ORBITS`.

Authority base: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`, successful verify run `29306335742`.

The admitted holomorphic-twist claim is `HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE`; it is an external target only.  The table below is a target/status census.  No holomorphic-twist coefficient is used to determine a Project Feynman coefficient.  The current (AA) and (AB_1) strictification files are local proposals and do not change the authority state.

## 1. Letters, descendants, and target tensors

The nine ordered letters are

$$
\mathbb L=(A,B_1,B_2,B_3,C_1,C_2,C_3,D_{\dot1},D_{\dot2}),
$$

$$
A:=\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+,
\qquad
B_r:=\boldsymbol\nabla_+\boldsymbol\Phi_r,
\qquad
C_r:=\widetilde{\boldsymbol\Phi}_r,
\qquad
D_{\dot a}:=\widetilde{\boldsymbol{\mathcal W}}_{\dot a}.
$$

Their parities and exact tree descendants are

$$
|A|=|C_r|=0,
\qquad
|B_r|=|D_{\dot a}|=1,
$$

$$
\boldsymbol\nabla_-A
=-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s),
$$

$$
\boldsymbol\nabla_-B_r
=-2\mathscr E_{\widetilde r}
-\sqrt2\varepsilon_{rst}(C_s\times C_t),
\qquad
\boldsymbol\nabla_-C_r=\boldsymbol\nabla_-D_{\dot a}=0.
$$

For every ordered pair,

$$
\boldsymbol\nabla_-(L_iL_j)
=(\boldsymbol\nabla_-L_i)L_j
+(-1)^{|L_i|}L_i(\boldsymbol\nabla_-L_j).
$$

In the table, `L:X` is the left marked placement.  `R:+X` and `R:-X` are the right marked placements including the displayed graded-Leibniz sign.

Define the common Project-normalized conditional target coefficient

$$
\lambda_1:=\frac{\hbar g^2}{16\pi^2},
\qquad
\mathbb F^{AB}{}_{DE}
:=\kappa^{AU}\kappa^{BV}\kappa^{CC'}c_{UCD}c_{VC'E}.
$$

Every nonzero tensor label below means

$$
\Delta(L_i^AL_j^B)
=\lambda_1\mathbb F^{AB}{}_{DE}\,\mathcal T_{ij}^{DE}.
$$

The exact tensor-label dictionary is

$$
\begin{aligned}
Z^{DE}:={}&
\langle D^D,A^E\rangle-\langle A^D,D^E\rangle
+\sum_{r=1}^3
\left(\langle B_r^D,C_r^E\rangle-\langle C_r^D,B_r^E\rangle\right),\\
X_r^{DE}:={}&
\langle D^D,C_r^E\rangle-\langle C_r^D,D^E\rangle,\\
U^{DE}:={}&\langle D^D,D^E\rangle,\\
Y_r^{DE}:={}&
\langle B_r^D,D^E\rangle+\langle D^D,B_r^E\rangle
-i\sqrt2\varepsilon_{rst}\langle C_s^D,C_t^E\rangle.
\end{aligned}
$$

Define

$$
\mathbf e_1=(1,0),
\qquad
\mathbf e_2=(0,1).
$$

$$
J_{L,a}^{DE}
:=\frac13\langle\mathbb J_{\mathbf e_a}D^D,D^E\rangle
+\frac23\langle D^D,\mathbb J_{\mathbf e_a}D^E\rangle,
$$

$$
J_{R,a}^{DE}
:=\frac23\langle\mathbb J_{\mathbf e_a}D^D,D^E\rangle
+\frac13\langle D^D,\mathbb J_{\mathbf e_a}D^E\rangle.
$$

The table codes mean

$$
\begin{gathered}
\texttt{Z}=Z,
\qquad
\texttt{Yr}=Y_r,
\qquad
\texttt{Xr}=X_r,
\qquad
\texttt{U}=U,\\
\texttt{JLa}=J_{L,a},
\qquad
\texttt{JRa}=J_{R,a},
\qquad
\texttt{H+t}=-i\sqrt2X_t,
\qquad
\texttt{H-t}=+i\sqrt2X_t.
\end{gathered}
$$

Thus `H+3`, `H-2`, `H-3`, `H+1`, `H+2`, `H-1` are respectively the six ordered values of

$$
-i\sqrt2\varepsilon_{rst}X_t
$$

for

$$
(r,s)=(1,2),(1,3),(2,1),(2,3),(3,1),(3,2).
$$

The source prints two incompatible absolute normalizations.  Its shifted branch uses

$$
\kappa_H^2\mathcal T^{\mathrm{HT}}_{m,n}
$$

with

$$
\mathcal T^{\mathrm{HT}}_{0,0}=\frac12,
$$

while its separate zero-shift formulas print coefficient

$$
\kappa_H^2.
$$

The conditional Project dictionary records

$$
\mathcal K^P_{m,n}=2\mathcal T^{\mathrm{HT}}_{m,n}.
$$

Therefore the tensor labels are exact comparison data, while the absolute cross-frame equality remains `BLOCKED_REFERENCE_INTERNAL_NORMALIZATION` and `BLOCKED_HT_ROW_LEVEL_SOURCE_EXTRACTION_PROVENANCE`.

## 2. Parent triangle skeletons and cutting-failure unit

Let

$$
G:=\mathcal V_{VVV},
\qquad
M_r:=\mathcal V_{\widetilde\Phi_rV\Phi_r},
\qquad
H_{\widetilde\Phi^3}:=\mathcal V_{\widetilde\Phi_1\widetilde\Phi_2\widetilde\Phi_3}.
$$

For the ordered two-port insertion \(I_{XY}\), the four parent skeleton classes are

$$
T_{GG}:=(I_{XY},G,G),
\qquad
T_{GM}:=(I_{XY},G,M_r),
$$

$$
T_{MM}:=(I_{XY},M_r,M_s),
\qquad
T_{MH}:=(I_{XY},M_r,H_{\widetilde\Phi^3}).
$$

Table codes are `TGG`, `TGM`, `TMM`, and `TMH`.  `TMM[1,2,3]` retains three distinct matter flavors.  `TMH[epsilon=0]` is a port-compatible parent killed by `epsilon_{rrt}=0`.  `TMM[delta=0]` is killed by the flavor-diagonal matter propagator.  `T0[port]` means the first-order `bc-beta-gamma` port grammar admits no connected triangle parent.  None of these zero labels is yet a complete Project raw-graph absence theorem.

The flavor-resolved meaning of every nonzero family code is

$$
\begin{aligned}
A>A:\quad& T_{GG}+\sum_{r=1}^3T_{MM}^{(r,r)},\\
A>B_r,\ B_r>A:\quad&
T_{GM}^{(r)}+T_{MM}^{(r,r)}
+\sum_{s\ne r}T_{MH}^{(s)},\\
A>C_r,\ C_r>A:\quad&
T_{GM}^{(r)}+T_{MM}^{(r,r)},\\
A>D_{\dot a},\ D_{\dot a}>A:\quad& T_{GG},\\
B_r>B_s,\ r\ne s:\quad& T_{MH}^{(r)}+T_{MH}^{(s)},\\
B_r>C_r,\ C_r>B_r:\quad& T_{MM}^{(r,r)}.
\end{aligned}
$$

Here

$$
T_{GM}^{(r)}:=(I_{XY},G,M_r),
\qquad
T_{MM}^{(r,s)}:=(I_{XY},M_r,M_s),
\qquad
T_{MH}^{(r)}:=(I_{XY},M_r,H_{\widetilde\Phi^3}).
$$

For reversed ordered inputs the source attachments are reversed and retained as distinct rows; no graph coefficient or sign is copied by symmetry.

Every admitted parent must be expanded into all source attachments, cyclic action-vertex assignments, both action chiralities when present, all marked inverse-kernel edges, and the matching \(R_1,R_2,R_3\) collapsed/contact rows.  The parent code is not the completed Schwinger--Dyson orbit.

For every selected edge \(e\),

$$
D_i=r_{i,d}^2,
\qquad
\bar r_e^2=r_{e,d}^2+\mu_\ell^2,
\qquad
\mu_\ell^2:=\bar\ell^2-\ell_d^2=-\widetilde\ell^2,
$$

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
$$

$$
\lim_{\epsilon\to0}
\mu^{2\epsilon}\int\frac{d^{4-2\epsilon}\ell}{(2\pi)^{4-2\epsilon}}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

This finite scalar is the exact universal cutting-failure unit.  It does not supply any graph-dependent source, Wick, color, D-word, or marked-occurrence coefficient.

## 3. Ordered-family count

| family | ordered components | nonzero target | zero target | parent classes |
| --- | ---: | ---: | ---: | --- |
| (A>A) | 1 | 1 | 0 | `TGG+TMM[1,2,3]` |
| (A>B) | 3 | 3 | 0 | `TGM+TMM+TMH` |
| (A>C) | 3 | 3 | 0 | `TGM+TMM` |
| (A>D) | 2 | 2 | 0 | `TGG` |
| (B>A) | 3 | 3 | 0 | `TGM+TMM+TMH` |
| (B>B) | 9 | 6 | 3 | `TMH` |
| (B>C) | 9 | 3 | 6 | `TMM` |
| (B>D) | 6 | 0 | 6 | `T0[port]` |
| (C>A) | 3 | 3 | 0 | `TGM+TMM` |
| (C>B) | 9 | 3 | 6 | `TMM` |
| (C>C) | 9 | 0 | 9 | `T0[port]` |
| (C>D) | 6 | 0 | 6 | `T0[port]` |
| (D>A) | 2 | 2 | 0 | `TGG` |
| (D>B) | 6 | 0 | 6 | `T0[port]` |
| (D>C) | 6 | 0 | 6 | `T0[port]` |
| (D>D) | 4 | 0 | 4 | `T0[port]` |

Hence

$$
N_{\mathrm{ordered\ pairs}}=81=29+52,
\qquad
N_{D_-\text{-marked\ pairs}}=56,
\qquad
N_{D_-\text{-marked\ occurrences}}=72.
$$

## 4. Evidence codes

The current local \(A>B_1\) outer-product replay keeps the two marked branches separate.  Its selected-edge remainders are

$$
\Gamma_{G_1,A\text{-marked}}^{\mathrm{selected}}
=+\frac{2\lambda_1}{3}\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle,
$$

$$
\Gamma_{G_1,B\text{-marked}}^{\mathrm{selected}}
=-\frac{2\lambda_1}{3}\mathbb F^{AB}{}_{DE}
\langle D^D,B_1^E\rangle,
$$

$$
\Gamma_{G_1,A\text{-marked}}^{\mathrm{selected}}
+\Gamma_{G_1,B\text{-marked}}^{\mathrm{selected}}=0.
$$

This zero is the selected-edge sum, not the occurrence-tagged Schwinger--Dyson/contact completion.

| code | exact present evidence | unresolved gate |
| --- | --- | --- |
| `E_AA` | universal cutting unit; full transported matter orbit with coefficient magnitude (1); exact gauge marked occurrence; exact zero of the remaining pure-gauge source-expansion and (B_sC_s)-current rows | common orientation; complete auxiliary/ghost/NK/counterterm gauge census |
| `E_AB1` | outer product rule and both marked \(G_1\) selected-edge branches replayed; coefficients \(+2\lambda_1/3,-2\lambda_1/3\), sum \(0\); isolated \(G_2,G_{3,2},G_{3,3}\) D-words | `BLOCKED_AB1_G1_EDGE_TAGGED_SD_CONTACT_PAIRING`; full \(G_2,G_3\) Euler/nonlinear/contact orbit |
| `E_AB1R` | conditional compact target tensor only | reversed ordered source was not replayed; no symmetry quotient is used |
| `E_NZ` | conditional compact Project tensor and external-target classification | raw triangle occurrences, marked cuts, contacts, sign, normalization, renormalization |
| `E_ZF` | exact epsilon- or delta-zero in the conditional target tensor | complete Project source/port absence-or-cancellation proof |
| `E_ZD` | exact Project identity \(\nabla_-(XY)=0\) for \(X,Y\in\{C_r,D_{\dot a}\}\); 25 rows checked by `step5_no_descendant_pairs_exact_audit.py` | none in the DRED cutting-failure sector: there is no marked inverse-kernel occurrence |
| `E_ZP` | exact zero in the first-order external-target port grammar | complete Project nonlinear-letter/contact/ghost absence proof |

All seven codes remain proposals relative to the authority contract.  No pair is `ACCEPTED` as a complete one-loop Project result.

## 5. Complete ordered-pair ledger

| # | ordered pair | family | marked placements | parent triangles | target tensor | evidence |
| ---: | --- | --- | --- | --- | --- | --- |
| 001 | `A>A` | `A>A` | `L:A;R:+A` | `TGG+TMM[1,2,3]` | `Z` | `E_AA` |
| 002 | `A>B1` | `A>B` | `L:A;R:+B1` | `TGM+TMM+TMH` | `Y1` | `E_AB1` |
| 003 | `A>B2` | `A>B` | `L:A;R:+B2` | `TGM+TMM+TMH` | `Y2` | `E_NZ` |
| 004 | `A>B3` | `A>B` | `L:A;R:+B3` | `TGM+TMM+TMH` | `Y3` | `E_NZ` |
| 005 | `A>C1` | `A>C` | `L:A` | `TGM+TMM` | `X1` | `E_NZ` |
| 006 | `A>C2` | `A>C` | `L:A` | `TGM+TMM` | `X2` | `E_NZ` |
| 007 | `A>C3` | `A>C` | `L:A` | `TGM+TMM` | `X3` | `E_NZ` |
| 008 | `A>Ddot1` | `A>D` | `L:A` | `TGG` | `JL1` | `E_NZ` |
| 009 | `A>Ddot2` | `A>D` | `L:A` | `TGG` | `JL2` | `E_NZ` |
| 010 | `B1>A` | `B>A` | `L:B1;R:-A` | `TGM+TMM+TMH` | `Y1` | `E_AB1R` |
| 011 | `B1>B1` | `B>B` | `L:B1;R:-B1` | `TMH[epsilon=0]` | `0eps` | `E_ZF` |
| 012 | `B1>B2` | `B>B` | `L:B1;R:-B2` | `TMH` | `H+3` | `E_NZ` |
| 013 | `B1>B3` | `B>B` | `L:B1;R:-B3` | `TMH` | `H-2` | `E_NZ` |
| 014 | `B1>C1` | `B>C` | `L:B1` | `TMM` | `U` | `E_NZ` |
| 015 | `B1>C2` | `B>C` | `L:B1` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 016 | `B1>C3` | `B>C` | `L:B1` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 017 | `B1>Ddot1` | `B>D` | `L:B1` | `T0[port]` | `0port` | `E_ZP` |
| 018 | `B1>Ddot2` | `B>D` | `L:B1` | `T0[port]` | `0port` | `E_ZP` |
| 019 | `B2>A` | `B>A` | `L:B2;R:-A` | `TGM+TMM+TMH` | `Y2` | `E_NZ` |
| 020 | `B2>B1` | `B>B` | `L:B2;R:-B1` | `TMH` | `H-3` | `E_NZ` |
| 021 | `B2>B2` | `B>B` | `L:B2;R:-B2` | `TMH[epsilon=0]` | `0eps` | `E_ZF` |
| 022 | `B2>B3` | `B>B` | `L:B2;R:-B3` | `TMH` | `H+1` | `E_NZ` |
| 023 | `B2>C1` | `B>C` | `L:B2` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 024 | `B2>C2` | `B>C` | `L:B2` | `TMM` | `U` | `E_NZ` |
| 025 | `B2>C3` | `B>C` | `L:B2` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 026 | `B2>Ddot1` | `B>D` | `L:B2` | `T0[port]` | `0port` | `E_ZP` |
| 027 | `B2>Ddot2` | `B>D` | `L:B2` | `T0[port]` | `0port` | `E_ZP` |
| 028 | `B3>A` | `B>A` | `L:B3;R:-A` | `TGM+TMM+TMH` | `Y3` | `E_NZ` |
| 029 | `B3>B1` | `B>B` | `L:B3;R:-B1` | `TMH` | `H+2` | `E_NZ` |
| 030 | `B3>B2` | `B>B` | `L:B3;R:-B2` | `TMH` | `H-1` | `E_NZ` |
| 031 | `B3>B3` | `B>B` | `L:B3;R:-B3` | `TMH[epsilon=0]` | `0eps` | `E_ZF` |
| 032 | `B3>C1` | `B>C` | `L:B3` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 033 | `B3>C2` | `B>C` | `L:B3` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 034 | `B3>C3` | `B>C` | `L:B3` | `TMM` | `U` | `E_NZ` |
| 035 | `B3>Ddot1` | `B>D` | `L:B3` | `T0[port]` | `0port` | `E_ZP` |
| 036 | `B3>Ddot2` | `B>D` | `L:B3` | `T0[port]` | `0port` | `E_ZP` |
| 037 | `C1>A` | `C>A` | `R:+A` | `TGM+TMM` | `X1` | `E_NZ` |
| 038 | `C1>B1` | `C>B` | `R:+B1` | `TMM` | `U` | `E_NZ` |
| 039 | `C1>B2` | `C>B` | `R:+B2` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 040 | `C1>B3` | `C>B` | `R:+B3` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 041 | `C1>C1` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 042 | `C1>C2` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 043 | `C1>C3` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 044 | `C1>Ddot1` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 045 | `C1>Ddot2` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 046 | `C2>A` | `C>A` | `R:+A` | `TGM+TMM` | `X2` | `E_NZ` |
| 047 | `C2>B1` | `C>B` | `R:+B1` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 048 | `C2>B2` | `C>B` | `R:+B2` | `TMM` | `U` | `E_NZ` |
| 049 | `C2>B3` | `C>B` | `R:+B3` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 050 | `C2>C1` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 051 | `C2>C2` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 052 | `C2>C3` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 053 | `C2>Ddot1` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 054 | `C2>Ddot2` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 055 | `C3>A` | `C>A` | `R:+A` | `TGM+TMM` | `X3` | `E_NZ` |
| 056 | `C3>B1` | `C>B` | `R:+B1` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 057 | `C3>B2` | `C>B` | `R:+B2` | `TMM[delta=0]` | `0delta` | `E_ZF` |
| 058 | `C3>B3` | `C>B` | `R:+B3` | `TMM` | `U` | `E_NZ` |
| 059 | `C3>C1` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 060 | `C3>C2` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 061 | `C3>C3` | `C>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 062 | `C3>Ddot1` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 063 | `C3>Ddot2` | `C>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 064 | `Ddot1>A` | `D>A` | `R:-A` | `TGG` | `JR1` | `E_NZ` |
| 065 | `Ddot1>B1` | `D>B` | `R:-B1` | `T0[port]` | `0port` | `E_ZP` |
| 066 | `Ddot1>B2` | `D>B` | `R:-B2` | `T0[port]` | `0port` | `E_ZP` |
| 067 | `Ddot1>B3` | `D>B` | `R:-B3` | `T0[port]` | `0port` | `E_ZP` |
| 068 | `Ddot1>C1` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 069 | `Ddot1>C2` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 070 | `Ddot1>C3` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 071 | `Ddot1>Ddot1` | `D>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 072 | `Ddot1>Ddot2` | `D>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 073 | `Ddot2>A` | `D>A` | `R:-A` | `TGG` | `JR2` | `E_NZ` |
| 074 | `Ddot2>B1` | `D>B` | `R:-B1` | `T0[port]` | `0port` | `E_ZP` |
| 075 | `Ddot2>B2` | `D>B` | `R:-B2` | `T0[port]` | `0port` | `E_ZP` |
| 076 | `Ddot2>B3` | `D>B` | `R:-B3` | `T0[port]` | `0port` | `E_ZP` |
| 077 | `Ddot2>C1` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 078 | `Ddot2>C2` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 079 | `Ddot2>C3` | `D>C` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 080 | `Ddot2>Ddot1` | `D>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |
| 081 | `Ddot2>Ddot2` | `D>D` | `NONE` | `T0[port]` | `0port` | `E_ZD` |

## 6. Fail-closed blockers

The full census is not a completed calculation.  Its global gates are

$$
\texttt{BLOCKED\_STEP5A\_LOCAL\_FERMI\_FEYNMAN\_PROPER\_SLICE},
$$

$$
\texttt{BLOCKED\_RAW\_GRAPH\_Q\_EQUIVARIANT\_LIFT},
\qquad
\texttt{BLOCKED\_COMPLETE\_RAW\_PORT\_WORDS\_FOR\_NAMED\_SECTOR\_TABLE},
$$

$$
\texttt{BLOCKED\_FINITE\_MIXED\_PRIMITIVE\_RESIDUES},
\qquad
\texttt{BLOCKED\_TOTAL\_TYPED\_HT\_ROUNDTRIP}.
$$

Machine-readable gates: `BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE`, `BLOCKED_RAW_GRAPH_Q_EQUIVARIANT_LIFT`, `BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE`, `BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES`, `BLOCKED_TOTAL_TYPED_HT_ROUNDTRIP`, `BLOCKED_AB1_G1_EDGE_TAGGED_SD_CONTACT_PAIRING`.

The \(AA\) local proposal additionally remains blocked by its complete pure-gauge source/contact orbit and the matter global orientation sign.  The \(A>B_1\) local proposal has the outer product rule and both \(G_1\) selected-edge branches replayed; it remains blocked by `BLOCKED_AB1_G1_EDGE_TAGGED_SD_CONTACT_PAIRING` and the full \(G_2,G_3\) Euler/nonlinear/contact orbit.  The 25 pairs in \(\{C_r,D_{\dot a}\}^2\) are exact zero because the outer descendant vanishes before Wick contraction.  The remaining 54 pairs outside \(AA\), \(A>B_1\), and this 25-row zero block have no occurrence-resolved raw Project triangle calculation.
