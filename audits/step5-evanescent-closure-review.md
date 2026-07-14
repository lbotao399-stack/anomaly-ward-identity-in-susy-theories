# Step-5 evanescent-sector closure cross-review

Status: `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`. Foundation pin: verified `origin/main@00000f7`, run `29306335742`.

## 1. Bare WW remainder

$$
R_T^{mn}=r\widehat\delta^{mn},\qquad R_C^{mn}=-r\delta_4^{mn},
$$

$$
R_T^{mn}+R_C^{mn}=-r\breve\delta^{mn},\qquad
p^\rho\breve\delta^{mn}\sigma_m\bar\sigma_\rho\sigma_n=-2\epsilon p^\rho\sigma_\rho.
$$

## 2. Complete minimal projector split of $\mathscr Z$

$$
\mathscr Z_{\rm full}=\mathscr Z_{DA}(h,hh)+\mathscr Z_{BC}(h,h)+\sum_{u=1}^{8}\mathscr E_u.
$$

| row | operator | min breve degree |
|---|---|---:|
| `E_DA_h_hb` | $D_dot a^D*(P_h^dot a A_hb)^E-(P_h,dot a A_hb)^D*D^(E,dot a)$ | 1 |
| `E_DA_h_bb` | $D_dot a^D*(P_h^dot a A_bb)^E-(P_h,dot a A_bb)^D*D^(E,dot a)$ | 2 |
| `E_DA_b_hh` | $D_dot a^D*(P_b^dot a A_hh)^E-(P_b,dot a A_hh)^D*D^(E,dot a)$ | 1 |
| `E_DA_b_hb` | $D_dot a^D*(P_b^dot a A_hb)^E-(P_b,dot a A_hb)^D*D^(E,dot a)$ | 2 |
| `E_DA_b_bb` | $D_dot a^D*(P_b^dot a A_bb)^E-(P_b,dot a A_bb)^D*D^(E,dot a)$ | 3 |
| `E_BC_b_h` | $sum_r[(P_b,dot a B_r^D)(P_h^dot a C_r^E)-(P_h,dot a C_r^D)(P_b^dot a B_r^E)]$ | 1 |
| `E_BC_h_b` | $sum_r[(P_h,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_h^dot a B_r^E)]$ | 1 |
| `E_BC_b_b` | $sum_r[(P_b,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_b^dot a B_r^E)]$ | 2 |

Residual-$q$ descendants are $q_R\mathscr E_u$, $R\subset\{1,2,3\}$, with $\pi_4q_r=q_r\pi_4$.

## 3. Pole mixing and finite anomaly

$$
\Pi_{\rm phys}\Gamma_{\mathscr E_u}^{(1)}
=\sum_\alpha P_{u\alpha}(N_\epsilon)I_{u\alpha}^{(1)},\qquad
P_{u\alpha}(0)=0,\qquad N_\epsilon=2\epsilon.
$$

After UV/IR separation, a one-loop primitive has at most a simple UV pole:

$$
\operatorname{Fin}_{\epsilon^0}\sum_\alpha P_{u\alpha}(2\epsilon)I_{u\alpha}^{(1)}
=2\sum_\alpha P_{u\alpha}'(0)r_{u\alpha,-1}.
$$

$$
\boxed{z_{\mathscr E_uO}^{\rm MS}=0\quad\text{under the displayed assumptions}},\qquad
\boxed{\operatorname{Fin}_{\epsilon^0}=2\sum_\alpha P_{u\alpha}'(0)r_{u\alpha,-1}}.
$$

第一式只对上述八个 component projector rows 已证明；第二式的 numerical coefficient 未闭合。完整 BV/source evanescent basis 仍未枚举。

## 4. Double-breve and mixed representatives

$$
A_{bb}=-i\Sigma^{ij}(\chi_i\times\chi_j),\qquad
\frac{\delta^2A_{bb}^E}{\delta\chi_i^M\delta\chi_j^N}=-2i\Sigma^{ij}c_{MN}{}^E.
$$

已枚举的 $\chi$ tadpole 与 $A_{\widehat\mu}\chi\chi$ direct/exchange contractions 都含 $\Sigma^{ij}\delta_{ij}=0$，故其 restricted projection 为零。尚未穷举的 compatible action/BV/source vertices 保持 `BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES`。

$$
A_{hb}=-2i(\sigma^{\widehat\mu i})_{++}\mathcal D_{\widehat\mu}\chi_i,
$$

$$
I_{D^M_{\dot a},\chi_i^N}^{[0]}=2i(J_{MN}-J_{NM})(\sigma_h^\nu)_{+\dot a}(\sigma^{\widehat\mu i})_{++}p_\nu p_\mu\ne0.
$$

Its three physical $I_{[0]}$ triangles use $V_{\chi\widetilde\Lambda\Lambda}$ with $V_{A\chi\chi}$, $V_{A\widetilde\Lambda\Lambda}$, and $V_{\widetilde\varphi\Lambda\Lambda}$. Step 5A does not lock unique propagators, integration cycle, or Fourier/DRED numerical rules; therefore $r_{u,-1}$ remains blocked.

## 5. No-double-count boundary

$$
r\widehat\delta^{mn}T_{mn}-r\delta_4^{mn}T_{mn}=-r\breve\delta^{mn}T_{mn}.
$$

Only when the full-superspace seed and explicit epsilon-scalar realization share one graph/source `origin_id` is the latter this complement rather than an additional term. This provenance link is not closed.

## 6. Verdict

$$
\boxed{z_{E_uO}^{\rm MS}=0\ \text{ for the eight projector rows};\qquad
c_{\rm fin}^{\rm mixed}=\texttt{BLOCKED\_COMPLETE\_BV\_DRED\_BASIS\_DRED\_EPSILON\_SPLIT\_FINITE\_RESIDUES}.}
$$

## 7. Checks

- `WW_SINGLE_BREVE_THREE_SIGMA_CHAIN`: PASS
- `WW_BARE_METRIC_MISMATCH_FIXED`: PASS
- `WW_RENORMALIZED_MIXING_EXPLICITLY_BLOCKED`: PASS
- `PHYSICAL_Q_KERNEL_ONE_DIMENSIONAL`: PASS
- `GLOBAL_CUT_CENSUS_NOT_COMPLETE`: PASS
- `GLOBAL_CENSUS_MIXING_BLOCKER_PRESENT`: PASS
- `COMPLETE_MINIMAL_PROJECTOR_SPLIT_EIGHT_ROWS`: PASS
- `MIXED_HAT_BREVE_ROW_INCLUDED`: PASS
- `DOUBLE_BREVE_ENUMERATED_DELTA_CLASSES_ZERO`: PASS
- `CONDITIONAL_EIGHT_PROJECTOR_ROWS_MS_POLE_MIXING_ZERO`: PASS
- `FINITE_MIXED_COEFFICIENT_BLOCKED`: PASS
- `NO_DOUBLE_COUNT_RETAINS_ORIGIN_BOUNDARY`: PASS
