# Step-5 DRED epsilon-scalar local mixing audit

Status: `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`. 本文件是 target-blind local proposal；不采用 HT coefficient。

## 1. DRED split

$$
d=4-2\epsilon,\qquad
\delta_4{}^m{}_n=\widehat\delta{}^m{}_n+\breve\delta{}^m{}_n,\qquad
\operatorname{tr}\widehat\delta=d,\qquad
\operatorname{tr}\breve\delta=N_\epsilon=2\epsilon.
$$

$$
\chi_i:=A_{\breve i},\qquad \partial_iX=0,\qquad
\mathcal D_iX=\chi_i\times X,\qquad
F_{\widehat\mu i}=\mathcal D_{\widehat\mu}\chi_i,\qquad
F_{ij}=\chi_i\times\chi_j.
$$

$$
\begin{aligned}
A_{hh}&=-i(\sigma^{mn})_{++}\widehat\delta_m{}^p\widehat\delta_n{}^qF_{pq},\\
A_{hb}&=-i(\sigma^{mn})_{++}(\widehat\delta_m{}^p\breve\delta_n{}^q+\breve\delta_m{}^p\widehat\delta_n{}^q)F_{pq}
=-2i(\sigma^{\widehat\mu i})_{++}\mathcal D_{\widehat\mu}\chi_i,\\
A_{bb}&=-i(\sigma^{mn})_{++}\breve\delta_m{}^i\breve\delta_n{}^jF_{ij}
=-i\Sigma^{ij}(\chi_i\times\chi_j),\qquad A=A_{hh}+A_{hb}+A_{bb},\\
P_{\dot a}&=P_{h,\dot a}+P_{b,\dot a}.
\end{aligned}
$$

## 2. Complete minimal projector split of $\mathscr Z$

$$
\mathscr Z_{\rm full}=\mathscr Z_{DA}(h,hh)+\mathscr Z_{BC}(h,h)+\sum_{u=1}^{8}\mathscr E_u.
$$

| row | operator | min breve degree | resolvent classes | finite |
|---|---|---:|---|---|
| `E_DA_h_hb` | $D_dot a^D*(P_h^dot a A_hb)^E-(P_h,dot a A_hb)^D*D^(E,dot a)$ | 1 | G1,G2,G3,G4 | `BLOCKED_NUMERICAL_PRIMITIVE_TRACE` |
| `E_DA_h_bb` | $D_dot a^D*(P_h^dot a A_bb)^E-(P_h,dot a A_bb)^D*D^(E,dot a)$ | 2 | G1,G2 | `ENUMERATED_DELTA_IJ_CLASSES_ZERO__FULL_ROW_BLOCKED` |
| `E_DA_b_hh` | $D_dot a^D*(P_b^dot a A_hh)^E-(P_b,dot a A_hh)^D*D^(E,dot a)$ | 1 | G1,G2 | `BLOCKED_NUMERICAL_PRIMITIVE_TRACE` |
| `E_DA_b_hb` | $D_dot a^D*(P_b^dot a A_hb)^E-(P_b,dot a A_hb)^D*D^(E,dot a)$ | 2 | G1,G2 | `BLOCKED_NUMERICAL_PRIMITIVE_TRACE` |
| `E_DA_b_bb` | $D_dot a^D*(P_b^dot a A_bb)^E-(P_b,dot a A_bb)^D*D^(E,dot a)$ | 3 | G1 | `EXACT_ZERO_AFTER_PI4_BY_EXTERNAL_CHI_COUNT` |
| `E_BC_b_h` | $sum_r[(P_b,dot a B_r^D)(P_h^dot a C_r^E)-(P_h,dot a C_r^D)(P_b^dot a B_r^E)]$ | 1 | G1,G2 | `BLOCKED_NUMERICAL_PRIMITIVE_TRACE` |
| `E_BC_h_b` | $sum_r[(P_h,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_h^dot a B_r^E)]$ | 1 | G1,G2 | `BLOCKED_NUMERICAL_PRIMITIVE_TRACE` |
| `E_BC_b_b` | $sum_r[(P_b,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_b^dot a B_r^E)]$ | 2 | G1 | `ZERO_FOR_MASSLESS_SCALARLESS_CONTACT_OTHERWISE_N_EPSILON_FINITE` |

每一 displayed row 均满足 $\pi_4(\mathscr E_u)=0$。五个 $DA$ rows 与三个 $BC$ rows 共八个；这是 $\mathscr Z$ 的完整 projector split，不是完整 BV/source/ghost/measure evanescent basis。

## 3. Residual-q orbit

$$
\Gamma_{i\dot a}:=(\sigma_E^m)_{+\dot a}\breve\delta_{mi},\qquad
q_r\chi_i=\frac1{\sqrt2}\Gamma_{i\dot a}\widetilde\psi_r^{\dot a}.
$$

$$
q_r(P_xX)=P_x(q_rX)+K_{x,r}(X),\qquad K_{h,r}+K_{b,r}=0.
$$

$$
q_rA_{bb}=-i\sqrt2\Sigma^{ij}[(\Gamma_i\widetilde\psi_r)\times\chi_j].
$$

令 $\Upsilon_r:=\Sigma^{ij}[(\Gamma_i\widetilde\psi_r)\times\chi_j]$，则

$$
q_s\Upsilon_r=\Sigma^{ij}\left[(\Gamma_i\varepsilon_{rst}\sigma_+^m\mathcal D_m\phi_t)\times\chi_j
-\frac1{\sqrt2}(\Gamma_i\widetilde\psi_r\times\Gamma_j\widetilde\psi_s)\right].
$$

$$
\mathcal K_{\rm ev}:=\operatorname{Span}\{q_R\mathscr E_u:u=1,\ldots,8,\ R\subset\{1,2,3\}\},\qquad
\pi_4q_r=q_r\pi_4.
$$

## 4. Double-breve exact zero

$$
\frac{\delta^2A_{bb}^E}{\delta\chi_i^M\delta\chi_j^N}=-2i\Sigma^{ij}c_{MN}{}^E,\qquad
\Sigma^{ji}c_{NM}{}^E=\Sigma^{ij}c_{MN}{}^E.
$$

$A_{\widehat\mu}\chi_k\chi_l$ vertex 的 species tensor 为 $\delta_{kl}$。两项 Wick pairing 分别为

$$
\Sigma^{ij}\delta_{ik}\delta_{jl}\delta_{kl}=\Sigma^{ij}\delta_{ij}=0,
$$

$$
\Sigma^{ij}\delta_{il}\delta_{jk}\delta_{kl}=\Sigma^{ij}\delta_{ij}=0.
$$

contact tadpole 同样为 $\Sigma^{ij}\delta_{ij}=0$；其余 Hessians 留下 external $\chi$，被 $\pi_4$ 消去。因此

$$
\boxed{\Pi_{\rm phys}\Gamma_{[2]}^{(1)}[\mathscr E_{DA}(h,bb)]=0.}
$$

Topological term 不增加 component bulk vertex。其 variation 为

$$
\begin{aligned}
\delta S_{\rm top}
&=-\frac{i}{2}\int\partial_m[\mathfrak k_{AB}\epsilon_E^{mnrs}\delta A_n^AF_{rs}^B]\\
&\quad+\frac{i}{2}\int\mathfrak k_{AB}\epsilon_E^{mnrs}\delta A_n^A(\mathcal D_mF_{rs})^B=0,
\end{aligned}
$$

其中第一项在 compact support/boundaryless 条件下为零，第二项由 Bianchi identity 为零。若先对 $\epsilon_E^{mnrs}$ 做 hat/breve continuation，则该 regulator rule 尚未锁定，记为 `BLOCKED_DRED_EPSILON_TENSOR_SPLIT`。

## 5. Mixed source and internal cycles

采用 $e^{ipx}$ 仅写 proposal momentum tensor：

$$
(P_hA_{hb})_{\dot a}^{(1)}
=2i(\sigma_h^\nu)_{+\dot a}(\sigma^{\widehat\mu i})_{++}p_\nu p_\mu\chi_i.
$$

$$
\boxed{I_{D^M_{\dot a},\chi_i^N}^{[0]}=2i(J_{MN}-J_{NM})
(\sigma_h^\nu)_{+\dot a}(\sigma^{\widehat\mu i})_{++}p_\nu p_\mu\ne0.}
$$

完整 degree-two one-loop source resolvent 为

$$
\Gamma_{J,[2]}^{(1)}=\frac{\hbar}{2}\operatorname{STr}[GI_{[2]}-GV_{[1]}GI_{[1]}-GV_{[2]}GI_{[0]}+GV_{[1]}GV_{[1]}GI_{[0]}].
$$

$I_{[0]}$ triangle 的 physical internal cycles 恰有三类：

1. $I_{D\chi}$--$V_{\chi\widetilde\Lambda\Lambda}$--$V_{A\chi\chi}$，external $(D,A)$；
2. $I_{D\chi}$--$V_{A\widetilde\Lambda\Lambda}$--$V_{\chi\widetilde\Lambda\Lambda}$，external $(A,D)$；
3. $I_{D\chi}$--$V_{\widetilde\varphi\Lambda\Lambda}$--$V_{\chi\widetilde\Lambda\Lambda}$，external $(C_r,B_r)$。

它们都必须闭合 source 的 breve index $i$，故带 $N_\epsilon$。

## 6. MS pole versus finite anomaly

物理 projection 无 external breve index。对 $O(N_\epsilon)$-covariant DRED contraction，

$$
\Pi_{\rm phys}\Gamma_{\mathscr E_u}^{(1)}
=\sum_\alpha P_{u\alpha}(N_\epsilon)I_{u\alpha}^{(1)},\qquad P_{u\alpha}(0)=0.
$$

对每个 independent closed-breve tensor/integral structure $\alpha$，

epsilon-scalar species kernel 的 tensor structure 为

$$
K_{\chi_i^A\chi_j^B}=h\kappa_{AB}\widehat p^2\delta_{ij},\qquad
K^{-1}_{\chi_i^A\chi_j^B}\text{ carries }\delta^{ij}\text{ and no }N_\epsilon^{-1}.
$$

因此 primitive contractions 是 $N_\epsilon$ 的 polynomial。对 nonexceptional Euclidean $\Delta$，Schwinger/Feynman parameter integral 为

$$
I_{r,s}(\Delta)=\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(r+2-\epsilon)\Gamma(s-r-2+\epsilon)}{\Gamma(2-\epsilon)\Gamma(s)}
\Delta^{r+2-s-\epsilon}.
$$

$\Gamma(s-r-2+\epsilon)$ 至多有 simple pole；one-loop primitive 无 UV subdivergence。先分离 IR 后，

$$
I_{u\alpha}^{(1)}=\frac{r_{u\alpha,-1}}{\epsilon}+r_{u\alpha,0}+\epsilon r_{u\alpha,1},\qquad
\operatorname{Fin}_{\epsilon^0}\sum_\alpha P_{u\alpha}(2\epsilon)I_{u\alpha}^{(1)}
=2\sum_\alpha P_{u\alpha}'(0)r_{u\alpha,-1}.
$$

因此在 UV/IR separation 后的 one-loop simple-pole sector，

$$
\boxed{\operatorname{Res}_{1/\epsilon}\Pi_{\rm phys}\Gamma_{\mathscr E_u}^{(1)}=0,\qquad z_{\mathscr E_uO}^{\rm MS}=0,}
$$

但

$$
\boxed{\operatorname{Fin}_{\epsilon^0}\sum_\alpha P_{u\alpha}(N_\epsilon)I_{u\alpha}^{(1)}
=2\sum_\alpha P_{u\alpha}'(0)r_{u\alpha,-1}.}
$$

$P_{u\alpha}(N)=N$ 给 $2r_{u\alpha,-1}$；$P_{u\alpha}(N)=N^2$ 给 $0$；$P_{u\alpha}(N)=N(N-1)$ 给 $-2r_{u\alpha,-1}$。所以必须逐 graph、逐 tensor structure 记录 $P_{u\alpha}$。三个 one-index mixed $I_{[0]}$ cycles 在进一步 Clifford reduction 前有 $P_{u\alpha}=N_\epsilon$；multi-breve rows 不能统一写成 $2r_{u,-1}$。$A_{bb}$ 只在三类已枚举 $\delta_{ij}$ contractions 中为零；full row 仍被 `BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES` 阻塞。

## 7. No-double-count identity

$$
r\widehat\delta^{mn}T_{mn}-r\delta_4^{mn}T_{mn}
=-r\breve\delta^{mn}T_{mn}.
$$

仅当 full-superspace seed 与 explicit epsilon-scalar realization 的 graph/source `origin_id` 及 coefficient provenance 已证明相同，后者才是右侧 complement，不能再次相加。此时正确 multiplicity 为 $(\widehat\delta,\breve\delta)=(1,1)$；double-count mutation 为 $(1,2)$。

## 8. Unfixed BV/source sectors

Ghost/gauge-fixing 依赖未选 local perturbative slice；Nielsen--Kallosh branch 未选；BV density/measure 的 DRED continuation 未定义；EOM、BRST-exact、total derivative、counterterm source multipliers 未枚举。因此这些 sectors 不适用本节八个 component projector rows 的 $z_{EO}^{\rm MS}=0$ theorem。

## 9. Remaining blocker

Step 5A 明确不锁定 complete BV/DRED basis、hat/breve epsilon-tensor continuation、unique propagators、integration cycle、Fourier/DRED momentum rules。故状态为 `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`；本 audit 不伪造 coefficient。

## 10. Tests

- `T01_CARTESIAN_PROJECTOR_SPLIT`: PASS
- `T02_EVERY_PROJECTOR_PIECE_VANISHES_UNDER_PI4`: PASS
- `T03_A_BB_SOURCE_HESSIAN_SYMMETRY`: PASS
- `T04_A_BB_DIRECT_WICK_ZERO`: PASS
- `T05_A_BB_EXCHANGE_WICK_ZERO`: PASS
- `T06_A_BB_TADPOLE_ZERO`: PASS
- `T07_MIXED_SOURCE_HESSIAN_NONZERO`: PASS
- `T09_N_EPSILON_TIMES_SIMPLE_POLE_HAS_NO_POLE`: PASS
- `T10_N_EPSILON_MUTATION_DETECTED`: PASS
- `T11_RESOLVENT_SIGNS`: PASS
- `T12_TYPED_LEG_MATCHING_TRIANGLE_CENSUS`: PASS
- `T13_NO_DOUBLE_COUNT_PROJECTOR_IDENTITY`: PASS
- `T15_STEP5A_NUMERICAL_RULE_BLOCKER_RETAINED`: PASS
- `T16_CHERN_WEIL_VARIATION_USES_BIANCHI`: PASS
- `T17_DOUBLE_POLE_MUTATION_DETECTED`: PASS
