# Step 5 WW topology-allocation invariance audit

Authority base: 00000f748fe4bdd1b5d122663cc1fb814faace66; verify run 29306335742.

## 1. Inputs

| input | SHA-256 | check |
|---|---|---|
| audits/step5-ww-contact-link-completion.json | 322a92140e557fee666df4bfb652dfb6472aa07a915fa1ea8a8501e5d18635cd | PASS |
| audits/step5-ww-physical-cut-pole.json | 92d1d87f6d667ff6e60016eead238bd68d3caf6ef4194d2e69795564e91d18c4 | PASS |

## 2. Declared normal form

| stage | name | exact rule | invariant |
|---:|---|---|---|
| 1 | ENDPOINT_TRANSFER | D_i delta_ij -> -D_j delta_ij and barD_i delta_ij -> -barD_j delta_ij, following the oriented edge toward its declared root. | edge tag, port order, color word, marked Dminus placement |
| 2 | D_LOOP_CLOSURE | Apply D^2 barD^2 D^2=16 Box D^2 only after all endpoint transfers; emit Box(r_i) without cancelling it. | ordered external derivative word |
| 3 | EDGE_COLLAPSE_AND_CLASSIFY | Box(r_i)/r_i^2 -> delta_edge(r_i); classify the result as COLLAPSED_Ri. If no Box tag exists, retain its origin label NONLINEAR_LETTER, QUARTIC_ACTION, ONE_LINK, TWO_LINK, ENDPOINT_LEFT, or ENDPOINT_RIGHT. | normalized occurrence word and total coefficient |
| 4 | LOOP_MOMENTUM_SHIFT | Only now perform k -> ell-y*q-z*P in the DRED integral; do not use a shift to choose a collapse edge. | Laurent residue and ordered external phase |

即：

$$
\boxed{
\text{endpoint transfer}
\longrightarrow D^2\bar D^2\text{ closure}
\longrightarrow\Box(r_i)/r_i^2\text{ collapse}
\longrightarrow\text{loop shift}}.
$$

ordered ports、reflection、marked $D_-$ placement 从不合并。

## 3. Exact allocation relations

| relation | zero relation | sector-label effect |
|---|---|---|
| REL-ENDPOINT | D_i delta_ij + D_j delta_ij=0; same for barD | moves a term between origin-labelled and collapsed-labelled rows |
| REL-CLOSURE | D^2 barD^2 D^2-16 Box D^2=0 | moves a closed D word into an edge-tagged Box representative |
| REL-CUT | Box(r_i) G(r_i)-delta_edge(r_i)=0 | moves a quartic/nonlinear representative into COLLAPSED_Ri |
| REL-DUHAMEL-1 | i w.(r-r') int_0^1 ds E(s)-E(r)+E(r')=0 | moves ONE_LINK bulk into endpoint representatives |
| REL-DUHAMEL-2A | i w.(r0-r1) int_{a<=b}E012-int db(E02-E12)=0 | moves TWO_LINK bulk into ONE_LINK representatives |
| REL-DUHAMEL-2B | i w.(r1-r2) int_{a<=b}E012-int da(E01-E02)=0 | moves TWO_LINK bulk into ONE_LINK representatives |
| REL-SHIFT | int d^d k [F(k+a)-F(k)]=0 in the declared translational DRED measure | changes routing notation after all edge labels are fixed |

这些 relations 改变 display label，不改变 normalized occurrence word、
color、external ordering 或 total coefficient。

## 4. Allocation complex for one occurrence

令

$$
\mathsf S_{\rm sector}
=\operatorname{span}\{
N,Q,C_0,C_1,C_2,L_1,L_2,E_L,E_R\}.
$$

令 summation map

$$
\Sigma:\mathsf S_{\rm sector}\to\mathsf N_{\rm aggregate},
\qquad
\Sigma(e_s)=1.
$$

选择 $C_1$ 为 canonical display label，并定义八个 allocation homotopies：

| generator | boundary |
|---|---|
| H::NONLINEAR_LETTER->COLLAPSED_R1 | NONLINEAR_LETTER-COLLAPSED_R1 |
| H::QUARTIC_ACTION->COLLAPSED_R1 | QUARTIC_ACTION-COLLAPSED_R1 |
| H::COLLAPSED_R0->COLLAPSED_R1 | COLLAPSED_R0-COLLAPSED_R1 |
| H::COLLAPSED_R2->COLLAPSED_R1 | COLLAPSED_R2-COLLAPSED_R1 |
| H::ONE_LINK->COLLAPSED_R1 | ONE_LINK-COLLAPSED_R1 |
| H::TWO_LINK->COLLAPSED_R1 | TWO_LINK-COLLAPSED_R1 |
| H::ENDPOINT_LEFT->COLLAPSED_R1 | ENDPOINT_LEFT-COLLAPSED_R1 |
| H::ENDPOINT_RIGHT->COLLAPSED_R1 | ENDPOINT_RIGHT-COLLAPSED_R1 |

它们组成 boundary map

$$
\partial_{\rm alloc}:\mathsf H_{\rm alloc}\to\mathsf S_{\rm sector}.
$$

机器得到

$$
\operatorname{rank}\partial_{\rm alloc}=8,
\qquad
\dim\ker\Sigma=9-\operatorname{rank}\Sigma=8,
$$

并逐列验证

$$
\Sigma\partial_{\rm alloc}=0.
$$

因此

$$
\boxed{
\operatorname{im}\partial_{\rm alloc}
=\ker\Sigma}.
$$

所以任意两个具有相同 aggregate 的 topology allocations
$a,a'$ 满足

$$
a-a'\in\ker\Sigma
=\operatorname{im}\partial_{\rm alloc}.
$$

即存在 $H$ 使

$$
\boxed{a-a'=\partial_{\rm alloc}H}.
$$

## 5. Anomaly invariance

对一个 fixed ordered occurrence，physical audit 给出的 anomaly coefficient
只依赖 aggregate contact class。故存在 $\bar{\mathscr A}$ 使

$$
\mathscr A=\bar{\mathscr A}\circ\Sigma.
$$

于是

$$
\mathscr A\partial_{\rm alloc}
=\bar{\mathscr A}\Sigma\partial_{\rm alloc}=0.
$$

因此

$$
\boxed{\mathscr A(a)=\mathscr A(a')}.
$$

全局有

$$
2_{\rm orientations}\times
2_{D_-\rm\ placements}\times
4_{\rm endpoint\ rows}=16
$$

个 blocks。Block direct sum 给出

$$
\operatorname{rank}\partial_{\rm alloc}^{\rm global}=16\times8=128,
$$

$$
\dim\ker\Sigma_{\rm global}=128,
\qquad
\dim\operatorname{coker}\partial_{\rm alloc}^{\rm global}=16.
$$

故 quotient 保留每个 already-oriented occurrence 的一个 aggregate
contact class；不会把 16 个 ordered words 合并成一个。

## 6. Canonical representative

NF-WW-CUT-01 对任何 complete raw graph IR 给出唯一 display：

$$
\Box(r_i)\ {\rm emitted}
\Longrightarrow \texttt{COLLAPSED\_R}i;
$$

没有 $\Box$ tag 时保留
NONLINEAR、QUARTIC、ONE-LINK、TWO-LINK 或 ENDPOINT origin。

当前缺少所有 raw port words，所以不能给出各 named sector 占
$C_C$ 的 numerical fractions；但任何这种 fractions 的改动均属于
$\operatorname{im}\partial_{\rm alloc}$，不改变

$$
C_C=C_T,
$$

也不改变

$$
\Gamma_{\rm anomaly}
=\frac{\hbar g^2}{16\pi^2}
\mathcal C\,\mathcal K_w[\widetilde W,p_+X].
$$

## 7. Mutations

| mutation | status | detector |
|---|---|---|
| MUTATE_BOUNDARY_MINUS_TO_PLUS | PASS | Sigma boundary !=0 |
| MUTATE_SECTOR_DEPENDENT_ANOMALY_WEIGHT | PASS | A boundary !=0 |
| MUTATE_LOOP_SHIFT_BEFORE_CLOSURE | PASS | normal-form stage trace |
| MUTATE_DROP_TWO_LINK_SECTOR | PASS | product-rule sector coverage |

## 8. Checks

| check | status |
|---|---|
| input_hash::audits/step5-ww-contact-link-completion.json | PASS |
| input_hash::audits/step5-ww-physical-cut-pole.json | PASS |
| normal_form_stage_order | PASS |
| local_image_boundary_equals_kernel_sum | PASS |
| local_anomaly_annihilates_allocation_boundaries | PASS |
| global_16_occurrence_quotient_dimension | PASS |
| global_exactness_blockwise | PASS |
| global_anomaly_invariance_blockwise | PASS |
| all_mutations_detected | PASS |

## 9. Exact blocker

BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE：
缺少每个 nonlinear-letter、quartic、collapsed descendant 在 endpoint
transfer 前的完整 raw port-preserving $D$ words。

$$
\boxed{\text{status}=\texttt{CONDITIONAL_FF_ALLOCATION_EXACTNESS_AND_AGGREGATE_INVARIANCE_CHECKED__BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE}}.
$$
