# Codex 交接提示词 — 2-loop 日字图 anomaly sector（复制本文件全文给 Codex）

---

我们在研究 N=4 SYM（N=1 superspace 表述，Euclidean，Fermi–Feynman 规范，DRED 正规化）的
anomaly Ward identity 的 **2-loop 修正**。能有 2-loop 修正的最低算符是 3-letter 词。我们研究纯
gauge sector 的

$$\boldsymbol\nabla_-\big(\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^A\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^B\,\boldsymbol\nabla_+\boldsymbol{\mathcal W}_+^C\big),$$

的**日字图**（kite，$K_4$ 减去一条边：4 顶点 5 传播子，唯一的 2-loop Laman 拓扑）。目标是复现
HT（arXiv:2512.07771v2，Budzik–Kulp）框架对 2-loop 的预期。注意：HT 原文**没有印出显式 2-loop
系数**，它给出的是 (i) 2-loop bracket 只支持在这个拓扑上；(ii) $Q_1^2+\{Q_0,Q_2\}=0$；
(iii) 长度-$n$ 词的修正预计截断于 $Q_{n-1}$（长度-2 为零、长度-3 首次非零）。所以"复现"的
操作含义是：**在项目已锁定的超空间/DRED 方案里，把这一张图的 anomaly sector 完整算出来**，
并核对上述三条结构性预期。只 focus 这一张图。这需要很仔细：分子很复杂，D-algebra 很长。

最终交付（全部写进 memo，人类可读、编号公式）：
1. 把图画出来（ASCII + TikZ）；
2. 从图写出完整 amplitude（所有 $\hbar,g,i$、有理系数、颜色词、D-词、$\theta$-积分、分母）；
3. D-algebra 分步积分过程省略，但给出**化简后的行表**（reduced rows）；
4. 识别出 anomaly sector（DRED evanescent $\mu^2$ 机制）；
5. 用 Feynman parameter 把积分做掉，给出最终结果（系数 × 输出词）。

## 0. 仓库现状（你的起点，全部已推送到分支 `claude/2-loop-superspace-anomaly-3havuv`）

- **主 memo 骨架（你要填完的文件）**：`proposals/step6-two-loop-kite-aaa-anomaly-memo-2026-07-17.md`
  — 图、动量路由 (K3.3)、pre-D-algebra 振幅 (K3.4)、evanescent 线字典 (K3.5)、archetype master
  (K3.7) 已写好；`<!-- ...-SLOT -->` 标记处等你填入：D-algebra 行表、master 表、最终装配、验证清单。
- **伴随 memo（长度-2 基线，已完成分析）**：`proposals/step6-two-loop-kite-aa-anomaly-memo-2026-07-16.md`
  — 含 $\mu^2$-插入引理 (K.11)、单字母输出消失定理 (K §8)。
- **共享规范 SPEC（v1=长度2，v2 附录=长度3 主目标）**：`proposals/step6-kite-artifacts/SPEC.md`。
- **已完成并验证的部件**（`proposals/step6-kite-artifacts/`）：
  - `color.md` + `color_check.py`：AA-图颜色因子完全证明 + su(2)/su(3) 数值验证（432/432）；
    关键可复用结论：c 全反对称 ⇒ 每个 slot 置换的颜色词 = $\mathrm{sgn}(\sigma_1)\mathrm{sgn}(\sigma_2)\mathrm{sgn}(\sigma_3)\times$(固定词)，
    颜色和运动学可分离；Jacobi+Casimir 归约技术直接搬到 AAA 图。
  - `vertex_audit.md`：顶点/插入算符/前因子全部独立复核（结论：SPEC §2 全对；总前因子
    $-(i/256)\hbar^2 g^3\chi_1\chi_2\chi_3$；注意其 D2–D5 号更正与 R1–R5 残余约定歧义清单）。
  - `my_masters_check.py`：引理 (K.11) 与 $M_1=-p^2/3072\pi^4$ 的 sympy 验证（已通过）。
  - `my_vanishing_check.py`：长度-2 消失定理的穷举验证（已通过，ALL ZERO）。
  - `engine_A/`：上一个 agent 的 D-algebra 引擎（**能用但太慢**：sympy 热循环，每个手征 sector
    约 30–40 分钟；`l1_per_assignment_rows.txt` 是它 1-loop 校准的逐 assignment 行表，可参考）。
- **1-loop 锁定校准文档（强制 gate）**：`audits/step5-canonical-superfield-ww-seed.md`。
- 项目契约：`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`（DRED ledger §1、
  cutting identity §5、字母与 $\boldsymbol\nabla_-$ 树作用 §3、1-loop 通道表 §7），
  `step-05a-...supergraph-grammar.md`（5A.49–5A.63 顶点词与图权重），
  `proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md`（F.1–F.6），
  `step-01-supersymmetry-commutator.md`（1.51–1.54 σ_E 代数）。

## 1. 锁定约定（不得改动；全部有契约出处，见 SPEC §1–§3）

- $\epsilon^{+-}=1$，$\epsilon_{+-}=-1$，$D^+=D_-$，$D^-=-D_+$；$D^2=2D_-D_+$；
  $(D^2\theta^2)|=(\bar D^2\bar\theta^2)|=-4$，$\delta^4(\theta)=\theta^2\bar\theta^2$，
  $[D^2\bar D^2\delta^4]|=16$；loop 饱和 $\delta^4_{12}D^2\bar D^2\delta^4_{12}=16\delta^4_{12}$，
  少于 $D^2\bar D^2$ 的闭 $\theta$-loop 为零。
- 动量空间：$e^{ip\cdot x}$，所有顶点动量流入；$\{D_a,\bar D_{\dot a}\}=2\mathsf p_{a\dot a}$，
  $\mathsf p_{a\dot a}(q)=-i(\sigma_E^m)_{a\dot a}q_m$，$\sigma_E^m=(-i\sigma^1,-i\sigma^2,-i\sigma^3,\mathbf 1)$。
- 传播子（canonical 归一化，$\mathcal V_P=2gv$）：$\langle v^Av^B\rangle=\hbar\kappa^{AB}p^{-2}\delta^4(\theta_{12})$。
- 三次顶点（每个顶点乘 $-1/\hbar$；参 seed §4 与 vertex_audit）：
  $S_{(3),+}=-\tfrac{ig}2 c_{CUE}\int(-\tfrac14\bar D^2D^av^E)(D_av^C)v^U$，
  $S_{(3),-}=+\tfrac{ig}2 c_{CUE}\int(-\tfrac14 D^2\bar D_{\dot a}v^E)(\bar D^{\dot a}v^C)v^U$。
- 插入（canonical）：$\mathcal I_3^{ABC}=D_-[(K_+v^A)(K_+v^B)(K_+v^C)]$，$K_+=-\tfrac14D_+\bar D^2D_+$，
  $D_-K_+=-\tfrac18D^2\bar D^2D_+$；三个 $\boldsymbol\nabla_-$-placement（Leibniz）。
  项目字母换算：LHS 乘 $g^3$，每个 canonical 场强输出字母乘 $g$（bare-$v$ jet 乘 $1/2g$），
  总阶 $\hbar^2g^4$。
- DRED：$d=4-2\epsilon$，自旋词分子四维、分母 $d$ 维；$\mu_\ell^2=\bar\ell^2-\ell_d^2$；
  2-loop 扩展 [D3]：三个 evanescent 不变量 $\mu_\ell^2,\mu_k^2,\mu_{\ell k}$，外动量严格 hatted，
  保留子积分的所有 $O(\epsilon)$ 项。
- 锚点积分：$\int_\ell\mu_\ell^2/(\ell^2+\Delta)^3=1/32\pi^2$（与 $\Delta$ 无关）；一般引理 (K.11)：
  $\int_k\mu_k^2/(k^2+\Delta)^n=\epsilon\,(4\pi)^{-d/2}\Gamma(n{-}1{-}\tfrac d2)\Gamma(n)^{-1}\Delta^{d/2+1-n}\mu^{2\epsilon}$。

## 2. 图（已定形，见主 memo §3）

插入 $\mathcal O$ 在 $K_4-e$ 的一个 **3 度角**；缺失边为 $X_a$–$X_b$；日字的中横杠是 $O$–$X_{\rm mid}$；
输出字母在两个 2 度角 $X_a$（外动量 $q_1$ 流出）与 $X_b$（$q_2$ 流出）；$Q=q_1+q_2$ 流入 $O$：

```
  L1: O→X_a (ℓ),  D₁=ℓ²          L2: O→X_b (k),  D₂=k²
  L3: O→X_mid (Q−ℓ−k), D₃=(Q−ℓ−k)²
  L4: X_mid→X_a (q₁−ℓ), D₄=(q₁−ℓ)²   L5: X_mid→X_b (q₂−k), D₅=(q₂−k)²
```

求和范围：3 个 placement × 3!（颜色腿 {A,B,C}→{L1,L2,L3}）× 手征 $(\chi_{\rm mid},\chi_a,\chi_b)\in\{\pm\}^3$
× 各顶点 slot 置换（$X_{\rm mid}$: 3!；$X_a,X_b$: 3!，含哪个 slot 当外腿）。Koszul 符号按 5A.61–62。
**可用的关键分解**（省 10× 计算量）：(a) 运动学只依赖"$D_-$-dressed 腿落在哪条线"（3 类），
不依赖颜色标签本身 ⇒ 颜色和 × 运动学类分离；(b) c 全反对称 ⇒ slot 置换的颜色词
= $\mathrm{sgn}(\sigma)$ × 固定词（color.md 已证）。

## 3. 分阶段 CHECKPOINTS（每个都要打印人类可读的输出，过不了就停下修，不许跳）

**CP0 — D-algebra 锚点**：实现 Grassmann 引擎后打印 §1 全部锚点的机器验证
（$(D^2\theta^2)|=-4$ 等 5 条）。⚠️ 工程要求：**禁止在热循环用 sympy**（上一个引擎因此每
sector 30–40 分钟）；用 bitmask 单项式 + `Fraction` 系数 + 抽象 $\mathsf p$-符号字典，目标：
每 sector 秒级。参考但不要照抄 `engine_A/galg.py, model.py`。

**CP1 — 1-loop 强制校准门（go/no-go）**：完整复现 `audits/step5-canonical-superfield-ww-seed.md`
§5–§9：8 行 endpoint 表、$w_D=2$、$\Gamma_{T,A}=\frac{\hbar g^2}2\mathcal C^{AB}{}_{DE}\,
\widetilde W^D_{\dot\alpha}(q)p^\rho X^E(p)T_{\mu\rho\nu,+}{}^{\dot\alpha}\int L_1^\mu L_2^\nu/(k^2(k{+}q)^2(k{+}P)^2)$，
$L_1=2k{+}q$，$L_2=2k{+}p{+}2q$。用随机数值动量逐分量比对。若差一个整体符号/同构重标记，
把你的"约定字典"写成表（vertex_audit.md 的 R1–R5 是已知的残余歧义清单）。**没过 CP1 的
任何 2-loop 数字一律无效。**

**CP2 — 长度-2 基线**：跑 SPEC v1 §4 的 AA tip-图，总局域输出必须恒为零
（`my_vanishing_check.py` 的定理）。这是引擎在 2-loop 拓扑上的第一个物理自检。

**CP3 — AAA 日字图 D-algebra 化简行表（主计算）**：跑 §2 的图。输出：
(a) 机器可读 JSON（逐行：placement/手征/slot、精确有理系数、$\mathsf p(\ell),\mathsf p(k),\mathsf p(q_1),\mathsf p(q_2)$
多项式、输出 jet 对、$\theta_0$-依赖）；(b) 人类可读 markdown 行表，按输出 jet 对组织，并尽量
装配成 σ-协变形式。自检：哪些手征 sector 非零；量子数账
（维度 $\tfrac{13}2$、undotted 荷 $+\tfrac52$、费米宇称 ⇒ 协变输出族只能是
$\mathsf p^3$-dressed $\langle D\text{-letter},A\text{-letter}\rangle$ 型，memo (K3.2)）；
颜色-运动学分离是否如 §2(b) 成立。

**CP4 — anomaly sector 识别**：对每条 marked edge 用 cutting identity
$\bar r_e^2/K' - \prod_{j\ne e}D_j^{-1}=\mu_{r_e}^2/K'$ 把 CP3 行表分成 contact/EOM sector 与
cutting-failure；用线字典（memo K3.5）：$\mu_{L_1}^2=\mu_{L_4}^2=\mu_\ell^2$，
$\mu_{L_2}^2=\mu_{L_5}^2=\mu_k^2$，$\mu_{L_3}^2=\mu_\ell^2+2\mu_{\ell k}+\mu_k^2$
（中横杠是混合不变量唯一来源）。打印：$N_\ell,N_k,N_{\ell k},N_{\ell\ell kk}$ 各自的行数与表达式。

**CP5 — masters（Feynman parameter，全过程展示）**：先符号验证引理 (K.11)（n=2,3,4）；
再逐个算 $K'$ 上的 masters：$N_1=\int\!\!\int\mu_\ell^2\mu_k^2/K'$ 必须复现
$-q_1^2/3072\pi^4$（内圈 $\mu_k^2$-三角与 $\Delta$ 无关 ⇒ $\tfrac1{32\pi^2}\int_0^1dx\,L(2,x(1{-}x)q_1^2)$；
镜像 $-q_2^2/3072\pi^4$）；然后 $N_2..N_6$（$\mu_{\ell k}$、单 $\mu^2$ 类——明确展示哪些带
$1/\epsilon$、哪些有限局域）、去一条分母的 daughters、以及 CP4 实际需要的带分子版本。
每个 master：参数化步骤编号展示 + 通用动量数值交叉验证（$q_1^2=1,q_2^2=2,q_1\!\cdot\!q_2=0.3$，
$\epsilon\in\{0.03,0.02,0.01\}$ 外推，3 位有效数字）。

**CP6 — 装配与最终结果**：CP4 的 $\mu$-行 × CP5 的 masters × 颜色词（用 color.md 的技术把
AAA 的 3-c 词归约到 $c\,c$-基，su(N) 显式化），装配成

$$\boldsymbol\nabla_-(A^AA^BA^C)\big|^{\rm anomaly}_{\text{2-loop},\,\text{日}}
=\frac{\hbar^2g^4}{(16\pi^2)^2}\times\big[\text{有理系数}\big]\times\big[\text{颜色张量}\big]
\times\big[\mathsf p^3\text{-dressed 两字母词}(q_1,q_2)\big]+\dots$$

自检：(i) 量子数账 (K3.2)；(ii) 长度-2 通道为零、长度-3 非零 ⇔ HT 截断 $Q_{n-1}$；
(iii) 拓扑 = HT 唯一 2-loop Laman 图；(iv) 陈述（不要求本图单独满足）全通道验收目标
$\{Q_0,Q_2\}=-Q_1^2$，RHS 用 settlement §7 已锁定的 1-loop 核。

**CP7 — 写回与提交**：把 CP3–CP6 填进主 memo 的四个 `SLOT`，验证部件放
`proposals/step6-kite-artifacts/`，commit + push 到 `claude/2-loop-superspace-anomaly-3havuv`。

## 4. 纪律（项目法则，必须遵守）

- Derivation-first：交付物是人类可读、编号公式的 memo；脚本只是从属证据。每个机器检查
  必须对应 memo 的编号公式。
- 不许引用未推导的传播子/顶点/符号/系数（AGENTS.md）；一切从锁定契约出发，出处标 tag。
- 单图范围诚实声明：ghost 路由、quartic 顶点路由、matter 圈、插入非线性路由、normal-product
  项全部列入 census 边界（memo §10），不算进本图结果。
- HT 是 external target：只对照,不作为计算输入。
- 遇到锚点定不下来的约定（R1–R5 类），写成明确的 decision 项放进 memo §10,不许悄悄选。
