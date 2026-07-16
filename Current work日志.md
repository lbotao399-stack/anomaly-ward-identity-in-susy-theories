# Current Work

## Active obligation (2026-07-16): Step 4D Majorana spinor system

- 新契约 `contracts/foundations/step-04d-majorana-spinor-system.md`：把此前 (D.1.1) 标记为
  `UNFIXED` 的四分量 (Majorana) 记号体系全部锁定，取 **Srednicki 分支、与 Weinberg 相反**
  （(4D.1) 分支表）：$\{\gamma^\mu,\gamma^\nu\}=-2\eta^{\mu\nu}$、
  $\gamma_5=+i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3}$、$\bar\Psi=+\Psi^{\rm T}\mathcal C$、
  $\Psi^*=-\beta\mathcal C\Psi$、动能项 $+\tfrac i2\bar\Psi\gamma^\mu\partial_\mu\Psi$。
- 过去的 Weyl 记号体系全部建立了 Majorana 平行（完备性表 (4D.75)）：Step-1 代数、Step-2A
  超空间（Majorana $\Theta$、$\mathsf Q$、$\mathbb D$ 包）、Step-3B 手征/WZ 矢量超场投影、
  Step-4A 的 $\mathcal N=1$、Step-4 的 $\mathcal N=2$ 打包，以及 **完备的 $\mathcal N=4$**：
  Lorentzian/Euclidean 作用量 (4D.62)-(4D.63)、全部十六个超对称变换 (4D.64)-(4D.65)、
  费米子 Euler 算子 (4D.67)、超对称流打包 (4D.68)-(4D.70)，逐分量等于锁定的 4C 方程。
- Euclidean 侧无实性条件：四分量对象只是独立 $(\psi,\widetilde\psi)$ 的打包，bar 仅由
  转置定义 (4D.33)，与 Step-5 的独立 tilde 场约定一致。
- 10 项精确机器检查全部通过（`audits/step4d-majorana-verification.json`），词典新增 §12
  关闭 (D.1.1)。Step-5 已接受的一切结果不变。

## Current Difficulty

- **LATEST — physical one-loop anomaly sector:** no unresolved row.  The target-blind ledger has `81 COMPLETE_EXACT`, `29 EXACT_NONZERO`, `52 EXACT_ZERO`, `0 OPEN`, and `0 UNRESOLVED`.
- `OUT_OF_SCOPE`: general raw-graph (q)-equivariant functor, complete BV/Wess--Zumino/open-color evanescent-module theorem, formal (U/Q_0) absolute intertwiner, and general reductive-color inverse.  None is used in the accepted physical result.

## Certain

- Every bare graph residue is the occurrence-wise DRED cutting failure

$$
\frac{\bar r_e^2}{D_0D_1D_2}
-\frac1{\prod_{j\ne e}D_j}
=\frac{\mu_\ell^2}{D_0D_1D_2},
\qquad
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2}{D_0D_1D_2}
=\frac1{32\pi^2}.
$$

- Ordered (AB_r/BA_r) is closed by

$$
v_{\rm raw}
=\left(2,2,-\frac13,\frac43,-2i\sqrt2,+2i\sqrt2\right),
$$

$$
v_{\rm TD}=(0,1,-2i\sqrt2,+2i\sqrt2),
$$

$$
\delta v_{\rm fin}=(1,0,+i\sqrt2,-i\sqrt2),
\qquad
v_{\rm ren}=(1,1,-i\sqrt2,+i\sqrt2),
\qquad
M_qv_{\rm ren}=0.
$$

The finite shift is a composite-source normal-product scheme term, not a new anomaly graph.

- Project data were canonicalized and SHA-256 sealed before HT read.  Direct comparison gives `81/81` coefficient/output-word matches.  For every (m,n\in\mathbb Z_{\ge0}),

$$
K^P_{m,n;k,\ell}
=2T^{HT,\mathrm{printed}}_{m,n;k,\ell}
=T^{HT,\mathrm{corrected}}_{m,n;k,\ell}.
$$

The executable rectangle gives `2025/2025` exact kernel checks and `141750/141750` lifted coefficient checks.

- The obsolete full-1PI scale-one audit is retracted; the exact (G_3) full-measure normalization is

$$
32768\left(\frac14\right)\left(\frac12\right)
=65536\left(\frac14\right)\left(\frac14\right)
=4096.
$$

- Physical verifier: `ACCEPTED`, scope `PHYSICAL_ONE_LOOP_ANOMALY_SECTOR`, `33/33 PASS`.  GPT Pro Gate 15 independently returned `FINAL_ONE_LOOP_HT_SETTLEMENT_ACCEPTED`.

- Primary artifacts: `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`, `audits/step5-global-81-target-blind-orbit-ledger.md`, `audits/step5_global_81_ht_symbolic_roundtrip_exact.md`, `audits/step5-euclidean-n4-awi-verification.json`, and `proposals/gpt-pro-final-one-loop-ht-settlement-gate15-response-2026-07-14.md`.
