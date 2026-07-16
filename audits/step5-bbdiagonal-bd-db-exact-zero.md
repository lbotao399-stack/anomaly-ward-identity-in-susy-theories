# Step 5 diagonal `BB` and `BD/DB` target-blind exact-zero audit

Status: `PASS_BB_DIAGONAL_BD_DB_TARGET_BLIND_EXACT_ZERO`.

Authority status: `LOCAL_PROPOSAL_FROM_DIRTY_WORKTREE` on frozen base `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66`.

## 1. Projectors and graded source signs

$$
\mathcal P_{D_{\dot a}}=D^2\bar D_{\dot a},
\qquad
\mathcal P_{B,\mathrm{mark}}=D_-D_+\bar D^2D^2.
$$

$$
\nabla_-(B_rB_r)=(\nabla_-B_r)B_r-B_r(\nabla_-B_r),
$$

$$
\nabla_-(B_rD_{\dot a})=(\nabla_-B_r)D_{\dot a},
\qquad
\nabla_-(D_{\dot a}B_r)=-D_{\dot a}(\nabla_-B_r).
$$

A DRED cutting remainder requires a nonzero four-dimensional scalar loop square on a marked inverse kernel. The symbolic projected words below vanish before color contraction; therefore no `bar(r)^2-r_d^2` remainder exists.

## 2. Diagonal `BB`

The unique split-source route for each flavor is `TMM`. Its two marked words are

$$
K_L=\int d^8z_Ld^8z_R
[D_-D_+\bar D^2D^2\delta_{SL}]
[D_+\bar D^2D^2\delta_{SR}]
\delta_{LR}B_r(L)B_r(R)=0,
$$

$$
K_R=\int d^8z_Ld^8z_R
[D_+\bar D^2D^2\delta_{SL}]
[D_-D_+\bar D^2D^2\delta_{SR}]
\delta_{LR}B_r(L)B_r(R)=0,
$$

$$
K_L-K_R=0.
$$

For every possible `Hminus`/Yukawa attachment of the spectator `B_r`, the propagator flavor delta forces one potential flavor to equal `r`:

$$
\epsilon_{rtu}\delta_{rt}=\epsilon_{rru}=0,
\qquad
\epsilon_{rtu}\delta_{ru}=\epsilon_{rtr}=0.
$$

A matter quartic has ports `(tildephi_r,u,u,phi_r)` and cannot absorb two `B_r` source legs. Pure gauge, gauge-fixing, FP and NK vertices have no `tildephi_r` port. All twelve spectator parents are 1PR.

## 3. `BD/DB`

The exact symbolic sparse-Grassmann replay gives

$$
K_{TGM}^{\dot a\dot b}(\mathrm{chirality},\pi,\mathrm{placement})=0
$$

for `2*2*2*6*2=96` source-dot/output-dot/chirality/gauge-permutation/derivative-placement words, and

$$
K_{TMM}^{\dot a\dot b}=0\quad(4/4),
\qquad
K_{TMH}^{\dot a}(A)=K_{TMH}^{\dot a}(B)=0\quad(4/4),
$$

$$
K_{M^{(2)}}^{\dot a\dot b}=0\quad(4/4).
$$

The Euler-potential and explicit-potential occurrences cancel before integration:

$$
+\sqrt2\epsilon_{rtu}(C_t\times C_u)D_{\dot a}
-\sqrt2\epsilon_{rtu}(C_t\times C_u)D_{\dot a}=0.
$$

For reverse order both terms carry the common Leibniz sign `-1`. The regulated Schwinger Jacobian is independently zero:

$$
\frac{\vec\delta D_{\dot a}^B}{\delta\widetilde\Phi_r^A}=0,
$$

because `D_dot` is a functional of `V` only. All 276 `BD/DB` spectator parents are 1PR.

## 4. Pair results

| pair | source mark/Koszul | split | spectator | result |
|---|---|---:|---:|---|
| `B1__B1` | `L:+1,R:-1` | 1 | 4 | `0` |
| `B2__B2` | `L:+1,R:-1` | 1 | 4 | `0` |
| `B3__B3` | `L:+1,R:-1` | 1 | 4 | `0` |
| `B1__Ddot1` | `L:+1` | 9 | 23 | `0` |
| `B1__Ddot2` | `L:+1` | 9 | 23 | `0` |
| `B2__Ddot1` | `L:+1` | 9 | 23 | `0` |
| `B2__Ddot2` | `L:+1` | 9 | 23 | `0` |
| `B3__Ddot1` | `L:+1` | 9 | 23 | `0` |
| `B3__Ddot2` | `L:+1` | 9 | 23 | `0` |
| `Ddot1__B1` | `R:-1` | 9 | 23 | `0` |
| `Ddot1__B2` | `R:-1` | 9 | 23 | `0` |
| `Ddot1__B3` | `R:-1` | 9 | 23 | `0` |
| `Ddot2__B1` | `R:-1` | 9 | 23 | `0` |
| `Ddot2__B2` | `R:-1` | 9 | 23 | `0` |
| `Ddot2__B3` | `R:-1` | 9 | 23 | `0` |

## 5. All typed parent routes

| # | route | pair | family/topology | mark | ports | classification |
|---:|---|---|---|---|---|---|
| 001 | `TRI::B1__B1::001::M1[0,1]::M1[0,1]` | `B1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1,R:-1` | `src=['tildephi1', 'tildephi1'];bridge=['u', 'u'];ext=['phi1', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 002 | `TRI::B1__Ddot1::001::M1[0,1]::G[0,1]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 003 | `TRI::B1__Ddot1::002::M1[0,1]::G[0,2]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 004 | `TRI::B1__Ddot1::003::M1[0,1]::G[1,0]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 005 | `TRI::B1__Ddot1::004::M1[0,1]::G[1,2]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 006 | `TRI::B1__Ddot1::005::M1[0,1]::G[2,0]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 007 | `TRI::B1__Ddot1::006::M1[0,1]::G[2,1]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 008 | `TRI::B1__Ddot1::007::M1[0,2]::M1[1,0]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi1', 'u'];bridge=['phi1', 'tildephi1'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 009 | `TRI::B1__Ddot1::008::Hminus[0,1]::M2[1,2]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi1', 'u'];bridge=['tildephi2', 'phi2'];ext=['tildephi3', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 010 | `TRI::B1__Ddot1::009::Hminus[0,2]::M3[1,2]` | `B1__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi1', 'u'];bridge=['tildephi3', 'phi3'];ext=['tildephi2', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 011 | `TRI::B1__Ddot2::001::M1[0,1]::G[0,1]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 012 | `TRI::B1__Ddot2::002::M1[0,1]::G[0,2]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 013 | `TRI::B1__Ddot2::003::M1[0,1]::G[1,0]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 014 | `TRI::B1__Ddot2::004::M1[0,1]::G[1,2]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 015 | `TRI::B1__Ddot2::005::M1[0,1]::G[2,0]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 016 | `TRI::B1__Ddot2::006::M1[0,1]::G[2,1]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi1', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 017 | `TRI::B1__Ddot2::007::M1[0,2]::M1[1,0]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi1', 'u'];bridge=['phi1', 'tildephi1'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 018 | `TRI::B1__Ddot2::008::Hminus[0,1]::M2[1,2]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi1', 'u'];bridge=['tildephi2', 'phi2'];ext=['tildephi3', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 019 | `TRI::B1__Ddot2::009::Hminus[0,2]::M3[1,2]` | `B1__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi1', 'u'];bridge=['tildephi3', 'phi3'];ext=['tildephi2', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 020 | `TRI::B2__B2::001::M2[0,1]::M2[0,1]` | `B2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1,R:-1` | `src=['tildephi2', 'tildephi2'];bridge=['u', 'u'];ext=['phi2', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 021 | `TRI::B2__Ddot1::001::M2[0,1]::G[0,1]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 022 | `TRI::B2__Ddot1::002::M2[0,1]::G[0,2]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 023 | `TRI::B2__Ddot1::003::M2[0,1]::G[1,0]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 024 | `TRI::B2__Ddot1::004::M2[0,1]::G[1,2]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 025 | `TRI::B2__Ddot1::005::M2[0,1]::G[2,0]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 026 | `TRI::B2__Ddot1::006::M2[0,1]::G[2,1]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 027 | `TRI::B2__Ddot1::007::M2[0,2]::M2[1,0]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi2', 'u'];bridge=['phi2', 'tildephi2'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 028 | `TRI::B2__Ddot1::008::Hminus[1,0]::M1[1,2]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi2', 'u'];bridge=['tildephi1', 'phi1'];ext=['tildephi3', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 029 | `TRI::B2__Ddot1::009::Hminus[1,2]::M3[1,2]` | `B2__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi2', 'u'];bridge=['tildephi3', 'phi3'];ext=['tildephi1', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 030 | `TRI::B2__Ddot2::001::M2[0,1]::G[0,1]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 031 | `TRI::B2__Ddot2::002::M2[0,1]::G[0,2]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 032 | `TRI::B2__Ddot2::003::M2[0,1]::G[1,0]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 033 | `TRI::B2__Ddot2::004::M2[0,1]::G[1,2]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 034 | `TRI::B2__Ddot2::005::M2[0,1]::G[2,0]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 035 | `TRI::B2__Ddot2::006::M2[0,1]::G[2,1]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi2', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 036 | `TRI::B2__Ddot2::007::M2[0,2]::M2[1,0]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi2', 'u'];bridge=['phi2', 'tildephi2'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 037 | `TRI::B2__Ddot2::008::Hminus[1,0]::M1[1,2]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi2', 'u'];bridge=['tildephi1', 'phi1'];ext=['tildephi3', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 038 | `TRI::B2__Ddot2::009::Hminus[1,2]::M3[1,2]` | `B2__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi2', 'u'];bridge=['tildephi3', 'phi3'];ext=['tildephi1', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 039 | `TRI::B3__B3::001::M3[0,1]::M3[0,1]` | `B3__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1,R:-1` | `src=['tildephi3', 'tildephi3'];bridge=['u', 'u'];ext=['phi3', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 040 | `TRI::B3__Ddot1::001::M3[0,1]::G[0,1]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 041 | `TRI::B3__Ddot1::002::M3[0,1]::G[0,2]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 042 | `TRI::B3__Ddot1::003::M3[0,1]::G[1,0]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 043 | `TRI::B3__Ddot1::004::M3[0,1]::G[1,2]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 044 | `TRI::B3__Ddot1::005::M3[0,1]::G[2,0]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 045 | `TRI::B3__Ddot1::006::M3[0,1]::G[2,1]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 046 | `TRI::B3__Ddot1::007::M3[0,2]::M3[1,0]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi3', 'u'];bridge=['phi3', 'tildephi3'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 047 | `TRI::B3__Ddot1::008::Hminus[2,0]::M1[1,2]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi3', 'u'];bridge=['tildephi1', 'phi1'];ext=['tildephi2', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 048 | `TRI::B3__Ddot1::009::Hminus[2,1]::M2[1,2]` | `B3__Ddot1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi3', 'u'];bridge=['tildephi2', 'phi2'];ext=['tildephi1', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 049 | `TRI::B3__Ddot2::001::M3[0,1]::G[0,1]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g0]'];bridge=['u', 'u[g1]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 050 | `TRI::B3__Ddot2::002::M3[0,1]::G[0,2]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g0]'];bridge=['u', 'u[g2]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 051 | `TRI::B3__Ddot2::003::M3[0,1]::G[1,0]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g1]'];bridge=['u', 'u[g0]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 052 | `TRI::B3__Ddot2::004::M3[0,1]::G[1,2]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g1]'];bridge=['u', 'u[g2]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 053 | `TRI::B3__Ddot2::005::M3[0,1]::G[2,0]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g2]'];bridge=['u', 'u[g0]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 054 | `TRI::B3__Ddot2::006::M3[0,1]::G[2,1]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `L:+1` | `src=['tildephi3', 'u[g2]'];bridge=['u', 'u[g1]'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 055 | `TRI::B3__Ddot2::007::M3[0,2]::M3[1,0]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `L:+1` | `src=['tildephi3', 'u'];bridge=['phi3', 'tildephi3'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 056 | `TRI::B3__Ddot2::008::Hminus[2,0]::M1[1,2]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi3', 'u'];bridge=['tildephi1', 'phi1'];ext=['tildephi2', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 057 | `TRI::B3__Ddot2::009::Hminus[2,1]::M2[1,2]` | `B3__Ddot2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `L:+1` | `src=['tildephi3', 'u'];bridge=['tildephi2', 'phi2'];ext=['tildephi1', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 058 | `TRI::Ddot1__B1::001::G[0,1]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi1'];bridge=['u[g1]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 059 | `TRI::Ddot1__B1::002::G[0,2]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi1'];bridge=['u[g2]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 060 | `TRI::Ddot1__B1::003::G[1,0]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi1'];bridge=['u[g0]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 061 | `TRI::Ddot1__B1::004::G[1,2]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi1'];bridge=['u[g2]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 062 | `TRI::Ddot1__B1::005::G[2,0]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi1'];bridge=['u[g0]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 063 | `TRI::Ddot1__B1::006::G[2,1]::M1[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi1'];bridge=['u[g1]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 064 | `TRI::Ddot1__B1::007::M1[1,0]::M1[0,2]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi1'];bridge=['tildephi1', 'phi1'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 065 | `TRI::Ddot1__B1::008::M2[1,2]::Hminus[0,1]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi1'];bridge=['phi2', 'tildephi2'];ext=['tildephi2', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 066 | `TRI::Ddot1__B1::009::M3[1,2]::Hminus[0,2]` | `Ddot1__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi1'];bridge=['phi3', 'tildephi3'];ext=['tildephi3', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 067 | `TRI::Ddot1__B2::001::G[0,1]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi2'];bridge=['u[g1]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 068 | `TRI::Ddot1__B2::002::G[0,2]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi2'];bridge=['u[g2]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 069 | `TRI::Ddot1__B2::003::G[1,0]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi2'];bridge=['u[g0]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 070 | `TRI::Ddot1__B2::004::G[1,2]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi2'];bridge=['u[g2]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 071 | `TRI::Ddot1__B2::005::G[2,0]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi2'];bridge=['u[g0]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 072 | `TRI::Ddot1__B2::006::G[2,1]::M2[0,1]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi2'];bridge=['u[g1]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 073 | `TRI::Ddot1__B2::007::M1[1,2]::Hminus[1,0]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi2'];bridge=['phi1', 'tildephi1'];ext=['tildephi1', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 074 | `TRI::Ddot1__B2::008::M2[1,0]::M2[0,2]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi2'];bridge=['tildephi2', 'phi2'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 075 | `TRI::Ddot1__B2::009::M3[1,2]::Hminus[1,2]` | `Ddot1__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi2'];bridge=['phi3', 'tildephi3'];ext=['tildephi3', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 076 | `TRI::Ddot1__B3::001::G[0,1]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi3'];bridge=['u[g1]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 077 | `TRI::Ddot1__B3::002::G[0,2]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi3'];bridge=['u[g2]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 078 | `TRI::Ddot1__B3::003::G[1,0]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi3'];bridge=['u[g0]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 079 | `TRI::Ddot1__B3::004::G[1,2]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi3'];bridge=['u[g2]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 080 | `TRI::Ddot1__B3::005::G[2,0]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi3'];bridge=['u[g0]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 081 | `TRI::Ddot1__B3::006::G[2,1]::M3[0,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi3'];bridge=['u[g1]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 082 | `TRI::Ddot1__B3::007::M1[1,2]::Hminus[2,0]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi3'];bridge=['phi1', 'tildephi1'];ext=['tildephi1', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 083 | `TRI::Ddot1__B3::008::M2[1,2]::Hminus[2,1]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi3'];bridge=['phi2', 'tildephi2'];ext=['tildephi2', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 084 | `TRI::Ddot1__B3::009::M3[1,0]::M3[0,2]` | `Ddot1__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi3'];bridge=['tildephi3', 'phi3'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 085 | `TRI::Ddot2__B1::001::G[0,1]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi1'];bridge=['u[g1]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 086 | `TRI::Ddot2__B1::002::G[0,2]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi1'];bridge=['u[g2]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 087 | `TRI::Ddot2__B1::003::G[1,0]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi1'];bridge=['u[g0]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 088 | `TRI::Ddot2__B1::004::G[1,2]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi1'];bridge=['u[g2]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 089 | `TRI::Ddot2__B1::005::G[2,0]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi1'];bridge=['u[g0]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 090 | `TRI::Ddot2__B1::006::G[2,1]::M1[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi1'];bridge=['u[g1]', 'u'];ext=['u', 'phi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 091 | `TRI::Ddot2__B1::007::M1[1,0]::M1[0,2]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi1'];bridge=['tildephi1', 'phi1'];ext=['phi1', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 092 | `TRI::Ddot2__B1::008::M2[1,2]::Hminus[0,1]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi1'];bridge=['phi2', 'tildephi2'];ext=['tildephi2', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 093 | `TRI::Ddot2__B1::009::M3[1,2]::Hminus[0,2]` | `Ddot2__B1` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi1'];bridge=['phi3', 'tildephi3'];ext=['tildephi3', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 094 | `TRI::Ddot2__B2::001::G[0,1]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi2'];bridge=['u[g1]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 095 | `TRI::Ddot2__B2::002::G[0,2]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi2'];bridge=['u[g2]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 096 | `TRI::Ddot2__B2::003::G[1,0]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi2'];bridge=['u[g0]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 097 | `TRI::Ddot2__B2::004::G[1,2]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi2'];bridge=['u[g2]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 098 | `TRI::Ddot2__B2::005::G[2,0]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi2'];bridge=['u[g0]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 099 | `TRI::Ddot2__B2::006::G[2,1]::M2[0,1]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi2'];bridge=['u[g1]', 'u'];ext=['u', 'phi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 100 | `TRI::Ddot2__B2::007::M1[1,2]::Hminus[1,0]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi2'];bridge=['phi1', 'tildephi1'];ext=['tildephi1', 'tildephi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 101 | `TRI::Ddot2__B2::008::M2[1,0]::M2[0,2]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi2'];bridge=['tildephi2', 'phi2'];ext=['phi2', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 102 | `TRI::Ddot2__B2::009::M3[1,2]::Hminus[1,2]` | `Ddot2__B2` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi2'];bridge=['phi3', 'tildephi3'];ext=['tildephi3', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 103 | `TRI::Ddot2__B3::001::G[0,1]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi3'];bridge=['u[g1]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 104 | `TRI::Ddot2__B3::002::G[0,2]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g0]', 'tildephi3'];bridge=['u[g2]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 105 | `TRI::Ddot2__B3::003::G[1,0]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi3'];bridge=['u[g0]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 106 | `TRI::Ddot2__B3::004::G[1,2]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g1]', 'tildephi3'];bridge=['u[g2]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 107 | `TRI::Ddot2__B3::005::G[2,0]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi3'];bridge=['u[g0]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 108 | `TRI::Ddot2__B3::006::G[2,1]::M3[0,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TGM` | `R:-1` | `src=['u[g2]', 'tildephi3'];bridge=['u[g1]', 'u'];ext=['u', 'phi3']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 109 | `TRI::Ddot2__B3::007::M1[1,2]::Hminus[2,0]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi3'];bridge=['phi1', 'tildephi1'];ext=['tildephi1', 'tildephi2']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 110 | `TRI::Ddot2__B3::008::M2[1,2]::Hminus[2,1]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMH` | `R:-1` | `src=['u', 'tildephi3'];bridge=['phi2', 'tildephi2'];ext=['tildephi2', 'tildephi1']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 111 | `TRI::Ddot2__B3::009::M3[1,0]::M3[0,2]` | `Ddot2__B3` | `SPLIT_SOURCE_SINGLE_BRIDGE/TMM` | `R:-1` | `src=['u', 'tildephi3'];bridge=['tildephi3', 'phi3'];ext=['phi3', 'u']` | `EXACT_ZERO_PROJECTED_DWORD` |
| 112 | `TRI-SPEC::B1__B1::001::SPEC-L::M1[0;1,2]::M1[1,0;2]` | `B1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=L:phi1;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 113 | `TRI-SPEC::B1__B1::002::SPEC-L::Hminus[0;1,2]::Hplus[1,2;0]` | `B1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=L:phi1;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 114 | `TRI-SPEC::B1__B1::003::SPEC-R::M1[0;1,2]::M1[1,0;2]` | `B1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=R:phi1;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 115 | `TRI-SPEC::B1__B1::004::SPEC-R::Hminus[0;1,2]::Hplus[1,2;0]` | `B1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=R:phi1;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 116 | `TRI-SPEC::B1__Ddot1::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 117 | `TRI-SPEC::B1__Ddot1::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 118 | `TRI-SPEC::B1__Ddot1::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 119 | `TRI-SPEC::B1__Ddot1::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 120 | `TRI-SPEC::B1__Ddot1::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 121 | `TRI-SPEC::B1__Ddot1::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 122 | `TRI-SPEC::B1__Ddot1::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 123 | `TRI-SPEC::B1__Ddot1::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 124 | `TRI-SPEC::B1__Ddot1::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 125 | `TRI-SPEC::B1__Ddot1::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 126 | `TRI-SPEC::B1__Ddot1::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 127 | `TRI-SPEC::B1__Ddot1::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 128 | `TRI-SPEC::B1__Ddot1::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 129 | `TRI-SPEC::B1__Ddot1::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 130 | `TRI-SPEC::B1__Ddot1::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 131 | `TRI-SPEC::B1__Ddot1::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 132 | `TRI-SPEC::B1__Ddot1::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 133 | `TRI-SPEC::B1__Ddot1::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 134 | `TRI-SPEC::B1__Ddot1::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 135 | `TRI-SPEC::B1__Ddot1::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 136 | `TRI-SPEC::B1__Ddot1::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 137 | `TRI-SPEC::B1__Ddot1::022::SPEC-R::M1[0;1,2]::M1[1,0;2]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 138 | `TRI-SPEC::B1__Ddot1::023::SPEC-R::Hminus[0;1,2]::Hplus[1,2;0]` | `B1__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 139 | `TRI-SPEC::B1__Ddot2::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 140 | `TRI-SPEC::B1__Ddot2::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 141 | `TRI-SPEC::B1__Ddot2::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 142 | `TRI-SPEC::B1__Ddot2::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 143 | `TRI-SPEC::B1__Ddot2::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 144 | `TRI-SPEC::B1__Ddot2::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 145 | `TRI-SPEC::B1__Ddot2::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 146 | `TRI-SPEC::B1__Ddot2::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 147 | `TRI-SPEC::B1__Ddot2::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 148 | `TRI-SPEC::B1__Ddot2::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 149 | `TRI-SPEC::B1__Ddot2::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 150 | `TRI-SPEC::B1__Ddot2::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 151 | `TRI-SPEC::B1__Ddot2::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 152 | `TRI-SPEC::B1__Ddot2::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 153 | `TRI-SPEC::B1__Ddot2::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 154 | `TRI-SPEC::B1__Ddot2::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 155 | `TRI-SPEC::B1__Ddot2::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 156 | `TRI-SPEC::B1__Ddot2::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 157 | `TRI-SPEC::B1__Ddot2::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 158 | `TRI-SPEC::B1__Ddot2::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 159 | `TRI-SPEC::B1__Ddot2::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 160 | `TRI-SPEC::B1__Ddot2::022::SPEC-R::M1[0;1,2]::M1[1,0;2]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 161 | `TRI-SPEC::B1__Ddot2::023::SPEC-R::Hminus[0;1,2]::Hplus[1,2;0]` | `B1__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 162 | `TRI-SPEC::B2__B2::001::SPEC-L::M2[0;1,2]::M2[1,0;2]` | `B2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=L:phi2;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 163 | `TRI-SPEC::B2__B2::002::SPEC-L::Hminus[1;0,2]::Hplus[0,2;1]` | `B2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=L:phi2;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 164 | `TRI-SPEC::B2__B2::003::SPEC-R::M2[0;1,2]::M2[1,0;2]` | `B2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=R:phi2;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 165 | `TRI-SPEC::B2__B2::004::SPEC-R::Hminus[1;0,2]::Hplus[0,2;1]` | `B2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=R:phi2;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 166 | `TRI-SPEC::B2__Ddot1::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 167 | `TRI-SPEC::B2__Ddot1::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 168 | `TRI-SPEC::B2__Ddot1::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 169 | `TRI-SPEC::B2__Ddot1::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 170 | `TRI-SPEC::B2__Ddot1::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 171 | `TRI-SPEC::B2__Ddot1::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 172 | `TRI-SPEC::B2__Ddot1::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 173 | `TRI-SPEC::B2__Ddot1::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 174 | `TRI-SPEC::B2__Ddot1::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 175 | `TRI-SPEC::B2__Ddot1::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 176 | `TRI-SPEC::B2__Ddot1::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 177 | `TRI-SPEC::B2__Ddot1::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 178 | `TRI-SPEC::B2__Ddot1::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 179 | `TRI-SPEC::B2__Ddot1::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 180 | `TRI-SPEC::B2__Ddot1::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 181 | `TRI-SPEC::B2__Ddot1::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 182 | `TRI-SPEC::B2__Ddot1::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 183 | `TRI-SPEC::B2__Ddot1::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 184 | `TRI-SPEC::B2__Ddot1::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 185 | `TRI-SPEC::B2__Ddot1::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 186 | `TRI-SPEC::B2__Ddot1::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 187 | `TRI-SPEC::B2__Ddot1::022::SPEC-R::M2[0;1,2]::M2[1,0;2]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 188 | `TRI-SPEC::B2__Ddot1::023::SPEC-R::Hminus[1;0,2]::Hplus[0,2;1]` | `B2__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 189 | `TRI-SPEC::B2__Ddot2::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 190 | `TRI-SPEC::B2__Ddot2::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 191 | `TRI-SPEC::B2__Ddot2::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 192 | `TRI-SPEC::B2__Ddot2::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 193 | `TRI-SPEC::B2__Ddot2::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 194 | `TRI-SPEC::B2__Ddot2::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 195 | `TRI-SPEC::B2__Ddot2::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 196 | `TRI-SPEC::B2__Ddot2::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 197 | `TRI-SPEC::B2__Ddot2::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 198 | `TRI-SPEC::B2__Ddot2::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 199 | `TRI-SPEC::B2__Ddot2::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 200 | `TRI-SPEC::B2__Ddot2::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 201 | `TRI-SPEC::B2__Ddot2::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 202 | `TRI-SPEC::B2__Ddot2::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 203 | `TRI-SPEC::B2__Ddot2::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 204 | `TRI-SPEC::B2__Ddot2::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 205 | `TRI-SPEC::B2__Ddot2::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 206 | `TRI-SPEC::B2__Ddot2::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 207 | `TRI-SPEC::B2__Ddot2::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 208 | `TRI-SPEC::B2__Ddot2::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 209 | `TRI-SPEC::B2__Ddot2::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 210 | `TRI-SPEC::B2__Ddot2::022::SPEC-R::M2[0;1,2]::M2[1,0;2]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 211 | `TRI-SPEC::B2__Ddot2::023::SPEC-R::Hminus[1;0,2]::Hplus[0,2;1]` | `B2__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 212 | `TRI-SPEC::B3__B3::001::SPEC-L::M3[0;1,2]::M3[1,0;2]` | `B3__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=L:phi3;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 213 | `TRI-SPEC::B3__B3::002::SPEC-L::Hminus[2;0,1]::Hplus[0,1;2]` | `B3__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=L:phi3;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 214 | `TRI-SPEC::B3__B3::003::SPEC-R::M3[0;1,2]::M3[1,0;2]` | `B3__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1,R:-1` | `spectator=R:phi3;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 215 | `TRI-SPEC::B3__B3::004::SPEC-R::Hminus[2;0,1]::Hplus[0,1;2]` | `B3__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1,R:-1` | `spectator=R:phi3;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 216 | `TRI-SPEC::B3__Ddot1::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 217 | `TRI-SPEC::B3__Ddot1::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 218 | `TRI-SPEC::B3__Ddot1::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 219 | `TRI-SPEC::B3__Ddot1::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 220 | `TRI-SPEC::B3__Ddot1::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 221 | `TRI-SPEC::B3__Ddot1::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 222 | `TRI-SPEC::B3__Ddot1::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 223 | `TRI-SPEC::B3__Ddot1::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 224 | `TRI-SPEC::B3__Ddot1::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 225 | `TRI-SPEC::B3__Ddot1::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 226 | `TRI-SPEC::B3__Ddot1::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 227 | `TRI-SPEC::B3__Ddot1::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 228 | `TRI-SPEC::B3__Ddot1::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 229 | `TRI-SPEC::B3__Ddot1::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 230 | `TRI-SPEC::B3__Ddot1::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 231 | `TRI-SPEC::B3__Ddot1::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 232 | `TRI-SPEC::B3__Ddot1::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 233 | `TRI-SPEC::B3__Ddot1::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 234 | `TRI-SPEC::B3__Ddot1::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 235 | `TRI-SPEC::B3__Ddot1::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 236 | `TRI-SPEC::B3__Ddot1::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 237 | `TRI-SPEC::B3__Ddot1::022::SPEC-R::M3[0;1,2]::M3[1,0;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 238 | `TRI-SPEC::B3__Ddot1::023::SPEC-R::Hminus[2;0,1]::Hplus[0,1;2]` | `B3__Ddot1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 239 | `TRI-SPEC::B3__Ddot2::001::SPEC-L::G[0;1,2]::G[0,1;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 240 | `TRI-SPEC::B3__Ddot2::002::SPEC-L::G[0;1,2]::G[0,2;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 241 | `TRI-SPEC::B3__Ddot2::003::SPEC-L::G[0;1,2]::G[1,0;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 242 | `TRI-SPEC::B3__Ddot2::004::SPEC-L::G[0;1,2]::G[1,2;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 243 | `TRI-SPEC::B3__Ddot2::005::SPEC-L::G[0;1,2]::G[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 244 | `TRI-SPEC::B3__Ddot2::006::SPEC-L::G[0;1,2]::G[2,1;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 245 | `TRI-SPEC::B3__Ddot2::007::SPEC-L::G[1;0,2]::G[0,1;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 246 | `TRI-SPEC::B3__Ddot2::008::SPEC-L::G[1;0,2]::G[0,2;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 247 | `TRI-SPEC::B3__Ddot2::009::SPEC-L::G[1;0,2]::G[1,0;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 248 | `TRI-SPEC::B3__Ddot2::010::SPEC-L::G[1;0,2]::G[1,2;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 249 | `TRI-SPEC::B3__Ddot2::011::SPEC-L::G[1;0,2]::G[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 250 | `TRI-SPEC::B3__Ddot2::012::SPEC-L::G[1;0,2]::G[2,1;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 251 | `TRI-SPEC::B3__Ddot2::013::SPEC-L::G[2;0,1]::G[0,1;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 252 | `TRI-SPEC::B3__Ddot2::014::SPEC-L::G[2;0,1]::G[0,2;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 253 | `TRI-SPEC::B3__Ddot2::015::SPEC-L::G[2;0,1]::G[1,0;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 254 | `TRI-SPEC::B3__Ddot2::016::SPEC-L::G[2;0,1]::G[1,2;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 255 | `TRI-SPEC::B3__Ddot2::017::SPEC-L::G[2;0,1]::G[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 256 | `TRI-SPEC::B3__Ddot2::018::SPEC-L::G[2;0,1]::G[2,1;0]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 257 | `TRI-SPEC::B3__Ddot2::019::SPEC-L::M1[1;0,2]::M1[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 258 | `TRI-SPEC::B3__Ddot2::020::SPEC-L::M2[1;0,2]::M2[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 259 | `TRI-SPEC::B3__Ddot2::021::SPEC-L::M3[1;0,2]::M3[2,0;1]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=L:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 260 | `TRI-SPEC::B3__Ddot2::022::SPEC-R::M3[0;1,2]::M3[1,0;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `L:+1` | `spectator=R:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 261 | `TRI-SPEC::B3__Ddot2::023::SPEC-R::Hminus[2;0,1]::Hplus[0,1;2]` | `B3__Ddot2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `L:+1` | `spectator=R:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 262 | `TRI-SPEC::Ddot1__B1::001::SPEC-L::M1[0;1,2]::M1[1,0;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 263 | `TRI-SPEC::Ddot1__B1::002::SPEC-L::Hminus[0;1,2]::Hplus[1,2;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 264 | `TRI-SPEC::Ddot1__B1::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 265 | `TRI-SPEC::Ddot1__B1::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 266 | `TRI-SPEC::Ddot1__B1::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 267 | `TRI-SPEC::Ddot1__B1::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 268 | `TRI-SPEC::Ddot1__B1::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 269 | `TRI-SPEC::Ddot1__B1::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 270 | `TRI-SPEC::Ddot1__B1::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 271 | `TRI-SPEC::Ddot1__B1::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 272 | `TRI-SPEC::Ddot1__B1::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 273 | `TRI-SPEC::Ddot1__B1::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 274 | `TRI-SPEC::Ddot1__B1::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 275 | `TRI-SPEC::Ddot1__B1::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 276 | `TRI-SPEC::Ddot1__B1::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 277 | `TRI-SPEC::Ddot1__B1::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 278 | `TRI-SPEC::Ddot1__B1::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 279 | `TRI-SPEC::Ddot1__B1::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 280 | `TRI-SPEC::Ddot1__B1::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 281 | `TRI-SPEC::Ddot1__B1::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 282 | `TRI-SPEC::Ddot1__B1::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 283 | `TRI-SPEC::Ddot1__B1::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 284 | `TRI-SPEC::Ddot1__B1::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot1__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 285 | `TRI-SPEC::Ddot1__B2::001::SPEC-L::M2[0;1,2]::M2[1,0;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 286 | `TRI-SPEC::Ddot1__B2::002::SPEC-L::Hminus[1;0,2]::Hplus[0,2;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 287 | `TRI-SPEC::Ddot1__B2::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 288 | `TRI-SPEC::Ddot1__B2::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 289 | `TRI-SPEC::Ddot1__B2::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 290 | `TRI-SPEC::Ddot1__B2::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 291 | `TRI-SPEC::Ddot1__B2::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 292 | `TRI-SPEC::Ddot1__B2::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 293 | `TRI-SPEC::Ddot1__B2::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 294 | `TRI-SPEC::Ddot1__B2::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 295 | `TRI-SPEC::Ddot1__B2::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 296 | `TRI-SPEC::Ddot1__B2::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 297 | `TRI-SPEC::Ddot1__B2::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 298 | `TRI-SPEC::Ddot1__B2::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 299 | `TRI-SPEC::Ddot1__B2::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 300 | `TRI-SPEC::Ddot1__B2::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 301 | `TRI-SPEC::Ddot1__B2::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 302 | `TRI-SPEC::Ddot1__B2::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 303 | `TRI-SPEC::Ddot1__B2::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 304 | `TRI-SPEC::Ddot1__B2::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 305 | `TRI-SPEC::Ddot1__B2::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 306 | `TRI-SPEC::Ddot1__B2::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 307 | `TRI-SPEC::Ddot1__B2::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot1__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 308 | `TRI-SPEC::Ddot1__B3::001::SPEC-L::M3[0;1,2]::M3[1,0;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 309 | `TRI-SPEC::Ddot1__B3::002::SPEC-L::Hminus[2;0,1]::Hplus[0,1;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 310 | `TRI-SPEC::Ddot1__B3::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 311 | `TRI-SPEC::Ddot1__B3::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 312 | `TRI-SPEC::Ddot1__B3::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 313 | `TRI-SPEC::Ddot1__B3::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 314 | `TRI-SPEC::Ddot1__B3::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 315 | `TRI-SPEC::Ddot1__B3::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 316 | `TRI-SPEC::Ddot1__B3::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 317 | `TRI-SPEC::Ddot1__B3::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 318 | `TRI-SPEC::Ddot1__B3::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 319 | `TRI-SPEC::Ddot1__B3::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 320 | `TRI-SPEC::Ddot1__B3::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 321 | `TRI-SPEC::Ddot1__B3::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 322 | `TRI-SPEC::Ddot1__B3::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 323 | `TRI-SPEC::Ddot1__B3::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 324 | `TRI-SPEC::Ddot1__B3::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 325 | `TRI-SPEC::Ddot1__B3::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 326 | `TRI-SPEC::Ddot1__B3::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 327 | `TRI-SPEC::Ddot1__B3::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 328 | `TRI-SPEC::Ddot1__B3::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 329 | `TRI-SPEC::Ddot1__B3::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 330 | `TRI-SPEC::Ddot1__B3::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot1__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 331 | `TRI-SPEC::Ddot2__B1::001::SPEC-L::M1[0;1,2]::M1[1,0;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 332 | `TRI-SPEC::Ddot2__B1::002::SPEC-L::Hminus[0;1,2]::Hplus[1,2;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi1;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 333 | `TRI-SPEC::Ddot2__B1::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 334 | `TRI-SPEC::Ddot2__B1::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 335 | `TRI-SPEC::Ddot2__B1::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 336 | `TRI-SPEC::Ddot2__B1::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 337 | `TRI-SPEC::Ddot2__B1::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 338 | `TRI-SPEC::Ddot2__B1::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 339 | `TRI-SPEC::Ddot2__B1::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 340 | `TRI-SPEC::Ddot2__B1::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 341 | `TRI-SPEC::Ddot2__B1::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 342 | `TRI-SPEC::Ddot2__B1::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 343 | `TRI-SPEC::Ddot2__B1::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 344 | `TRI-SPEC::Ddot2__B1::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 345 | `TRI-SPEC::Ddot2__B1::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 346 | `TRI-SPEC::Ddot2__B1::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 347 | `TRI-SPEC::Ddot2__B1::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 348 | `TRI-SPEC::Ddot2__B1::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 349 | `TRI-SPEC::Ddot2__B1::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 350 | `TRI-SPEC::Ddot2__B1::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 351 | `TRI-SPEC::Ddot2__B1::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 352 | `TRI-SPEC::Ddot2__B1::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 353 | `TRI-SPEC::Ddot2__B1::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot2__B1` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi1;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 354 | `TRI-SPEC::Ddot2__B2::001::SPEC-L::M2[0;1,2]::M2[1,0;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 355 | `TRI-SPEC::Ddot2__B2::002::SPEC-L::Hminus[1;0,2]::Hplus[0,2;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi2;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 356 | `TRI-SPEC::Ddot2__B2::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 357 | `TRI-SPEC::Ddot2__B2::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 358 | `TRI-SPEC::Ddot2__B2::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 359 | `TRI-SPEC::Ddot2__B2::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 360 | `TRI-SPEC::Ddot2__B2::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 361 | `TRI-SPEC::Ddot2__B2::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 362 | `TRI-SPEC::Ddot2__B2::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 363 | `TRI-SPEC::Ddot2__B2::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 364 | `TRI-SPEC::Ddot2__B2::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 365 | `TRI-SPEC::Ddot2__B2::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 366 | `TRI-SPEC::Ddot2__B2::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 367 | `TRI-SPEC::Ddot2__B2::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 368 | `TRI-SPEC::Ddot2__B2::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 369 | `TRI-SPEC::Ddot2__B2::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 370 | `TRI-SPEC::Ddot2__B2::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 371 | `TRI-SPEC::Ddot2__B2::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 372 | `TRI-SPEC::Ddot2__B2::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 373 | `TRI-SPEC::Ddot2__B2::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 374 | `TRI-SPEC::Ddot2__B2::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 375 | `TRI-SPEC::Ddot2__B2::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 376 | `TRI-SPEC::Ddot2__B2::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot2__B2` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi2;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 377 | `TRI-SPEC::Ddot2__B3::001::SPEC-L::M3[0;1,2]::M3[1,0;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=L:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 378 | `TRI-SPEC::Ddot2__B3::002::SPEC-L::Hminus[2;0,1]::Hplus[0,1;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/THH` | `R:-1` | `spectator=L:u;output=phi3;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 379 | `TRI-SPEC::Ddot2__B3::003::SPEC-R::G[0;1,2]::G[0,1;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 380 | `TRI-SPEC::Ddot2__B3::004::SPEC-R::G[0;1,2]::G[0,2;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 381 | `TRI-SPEC::Ddot2__B3::005::SPEC-R::G[0;1,2]::G[1,0;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 382 | `TRI-SPEC::Ddot2__B3::006::SPEC-R::G[0;1,2]::G[1,2;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 383 | `TRI-SPEC::Ddot2__B3::007::SPEC-R::G[0;1,2]::G[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 384 | `TRI-SPEC::Ddot2__B3::008::SPEC-R::G[0;1,2]::G[2,1;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 385 | `TRI-SPEC::Ddot2__B3::009::SPEC-R::G[1;0,2]::G[0,1;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 386 | `TRI-SPEC::Ddot2__B3::010::SPEC-R::G[1;0,2]::G[0,2;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 387 | `TRI-SPEC::Ddot2__B3::011::SPEC-R::G[1;0,2]::G[1,0;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 388 | `TRI-SPEC::Ddot2__B3::012::SPEC-R::G[1;0,2]::G[1,2;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 389 | `TRI-SPEC::Ddot2__B3::013::SPEC-R::G[1;0,2]::G[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 390 | `TRI-SPEC::Ddot2__B3::014::SPEC-R::G[1;0,2]::G[2,1;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 391 | `TRI-SPEC::Ddot2__B3::015::SPEC-R::G[2;0,1]::G[0,1;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 392 | `TRI-SPEC::Ddot2__B3::016::SPEC-R::G[2;0,1]::G[0,2;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 393 | `TRI-SPEC::Ddot2__B3::017::SPEC-R::G[2;0,1]::G[1,0;2]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 394 | `TRI-SPEC::Ddot2__B3::018::SPEC-R::G[2;0,1]::G[1,2;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 395 | `TRI-SPEC::Ddot2__B3::019::SPEC-R::G[2;0,1]::G[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 396 | `TRI-SPEC::Ddot2__B3::020::SPEC-R::G[2;0,1]::G[2,1;0]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TGG` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 397 | `TRI-SPEC::Ddot2__B3::021::SPEC-R::M1[1;0,2]::M1[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 398 | `TRI-SPEC::Ddot2__B3::022::SPEC-R::M2[1;0,2]::M2[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |
| 399 | `TRI-SPEC::Ddot2__B3::023::SPEC-R::M3[1;0,2]::M3[2,0;1]` | `Ddot2__B3` | `SPECTATOR_SOURCE_DOUBLE_BRIDGE/TMM` | `R:-1` | `spectator=R:phi3;output=u;cut_edge=True` | `EXACT_ZERO_1PR_EXCLUDED` |

## 6. Counts

$$
399=111_{\mathrm{split}}+288_{\mathrm{spectator}},
$$

$$
111=72_{TGM}+15_{TMM}+24_{TMH}.
$$

$$
15=3_{BB\,\mathrm{diag}}+6_{BD}+6_{DB},
\qquad
\Gamma_{\mathrm{ev}}=0\quad\text{for all fifteen pairs}.
$$

Verification:

```text
python scripts/step5_bbdiagonal_bd_db_exact_zero_audit.py --check
python -m unittest tests.test_step5_bbdiagonal_bd_db_exact_zero
```
