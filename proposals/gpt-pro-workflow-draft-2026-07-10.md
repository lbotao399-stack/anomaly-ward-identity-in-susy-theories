## 记号

* (q_0)：classical supersymmetry differential。
* (q_1)：renormalized local-operator complex 上的 one-loop correction。
* (i_H)：将 classical cohomology representative 嵌入 local-operator complex。
* (P_H)：投影到 BRST/EOM quotient 后的 (q_0)-cohomology。
* (\mu_q^2=-\widetilde q^2)：DRED 中的 positive evanescent momentum square。
* **PO**：proof obligation，一个必须独立完成、测试和审核的最小证明任务。

# 核心判断

你需要的不是“更长的 context”，而是：

[
\boxed{\text{stateless AI agents}+\text{stateful versioned proof repository}}
]

任何一次 ChatGPT/Codex session 都必须被视为**可随时丢失的临时进程**。真正的 memory 只能存在于：

[
\text{contracts}
+\text{code}
+\text{machine traces}
+\text{tests}
+\text{Git history}.
]

你当前体系首先存在一个必须立即修复的 authority contradiction：

[
\text{Notion root 是唯一 authority}
\neq
\text{local Markdown/code 是 source of truth}
\neq
\text{项目尚未进入 Git}.
]

这三个说法同时出现在当前项目中。对 Codex-first workflow 而言，这是致命的：agent 无法判断究竟哪个版本具有裁决权。

因此我建议：

[
\boxed{\text{Git repository 是唯一 authority；Notion 是 human-readable mirror/dashboard。}}
]

Notion 中只记录 commit、hash、test result、当前 blocker 和可读报告，不直接承载未经测试的计算源。

---

# 一、不要同时推进 Four Channels

你现在的 ES/EC/LS/LC 四通道设计适合作为 **final independent replication criterion**，不适合作为第一阶段 implementation scope。

推荐顺序：

[
\boxed{
\mathrm{EC}
\longrightarrow
\mathrm{ES}
\longrightarrow
\mathrm{LC/LS}
}
]

其中第一 primary channel 应当是：

[
\boxed{\text{Euclidean Component AWI}}
]

原因是 component formalism 中以下对象全部显式：

* EOM insertion；
* gauge-fixing 与 ghost terms；
* nonlinear part of composite operator；
* seagull/contact graphs；
* propagator cut；
* BRST completion；
* physical component representative。

Superspace 可以作为第二个 independent derivation，但不应继续作为 primary debugging surface。你目前的 ES 已经展示了 nonzero evanescent pole，却得到 zero canonical physical projection；EC 的 crossed-(T_{FF}) 又明确不满足 Ward identity，而 (T_{FA})、nonlinear insertions、EOM/ghost contacts 尚未完成。这说明当前 bottleneck 不是再算一个 triangle，而是 **graph completeness、contact generation 和 evanescent renormalization**。

四通道保留，但改成 maturity levels：

[
\begin{array}{c|l}
L_0 & \text{notation/algebra calibration}\
L_1 & \text{EC graph-complete result}\
L_2 & \text{ES independent reproduction}\
L_3 & \text{Euclidean formalism bridge}\
L_4 & \text{Lorentzian independent reproduction}\
L_5 & \text{final four-channel acceptance}
\end{array}
]

---

# 二、Repo architecture

```text
awi/
├── AGENTS.md
├── pyproject.toml
├── Makefile
│
├── contracts/                     # Human-locked inputs
│   ├── trusted_kernel.yaml
│   ├── notation.yaml
│   ├── index_spaces.yaml
│   ├── field_content.yaml
│   ├── operator_basis.yaml
│   ├── dred.yaml
│   ├── renormalization_scheme.yaml
│   ├── acceptance.yaml
│   │
│   ├── ec/
│   │   ├── action.yaml
│   │   ├── gauge_fixing.yaml
│   │   ├── susy_qminus.yaml
│   │   └── fourier_sigma.yaml
│   └── es/
│       ├── action.yaml
│       ├── superspace.yaml
│       └── fourier_sigma.yaml
│
├── channels/
│   ├── ec/
│   │   ├── AGENTS.md
│   │   ├── src/
│   │   └── tests/
│   ├── es/
│   │   ├── AGENTS.md
│   │   ├── src/
│   │   └── tests/
│   ├── lc/
│   └── ls/
│
├── tasks/                         # One task = one proof obligation
│   ├── EC-R1-ACTION-001.yaml
│   ├── EC-R1-TFA-001.yaml
│   └── ...
│
├── ledger/
│   ├── proof_obligations.json
│   ├── graph_inventory.json
│   ├── cut_contact_pairs.json
│   └── status.json
│
├── generated/
│   ├── rules/
│   ├── graphs/
│   ├── traces/
│   ├── integrals/
│   └── reports/
│
├── audits/
├── tests/
└── legacy/                        # Never readable by calculation agents
```

关键 restriction：

[
\boxed{
\texttt{channels/ec}
\text{ 不得 import 或读取 }
\texttt{channels/es}
}
]

各 channel 只能读取 `contracts/`，最后只能输出统一格式的：

```text
result.json
trace_manifest.json
verification_report.md
```

这样 independence 不再依赖 prompt 中的一句“不要参考另一通道”，而由 filesystem dependency tests 强制实现。

---

# 三、Notation 必须成为 machine-readable contract

不要把完整 conventions 塞进 `AGENTS.md`。Codex 会在每次 run 开始时读取 hierarchical `AGENTS.md`，越靠近工作目录的 instruction 优先；默认 combined instruction size 有限制，因此 root 文件只应保存 operational law，数学定义应放入独立 contracts。修改 `AGENTS.md` 后需要开启新 run 才能可靠加载。([[OpenAI Developers](https://developers.openai.com/codex/guides/agents-md)][1])

`notation.yaml` 至少包含：

```yaml
symbols:
  q_loop:
    latex: q
    type: momentum
    domain: dred_loop
    dimension: 1
    aliases_forbidden: [k, ell]

  q_dim_square:
    latex: q_d^2
    type: scalar
    definition: DimMetric(mu,nu) * q(mu) * q(nu)

  mu_q_square:
    latex: \mu_q^2
    type: scalar
    definition: -RawEvanescentMetric(mu,nu) * q(mu) * q(nu)

  f_pp:
    latex: f_{++}
    type: field
    statistics: bosonic
    engineering_dimension: 2
    ghost_number: 0
```

每个 symbol 必须具有：

[
(\text{name},\text{type},\text{index spaces},
\text{statistics},\Delta,\text{ghost number},
\text{definition},\text{scope}).
]

然后建立 `notation_lint`，拒绝：

* 未定义符号；
* 同一个 (q^2) 未注明 (4)-dimensional、(d)-dimensional 或 evanescent；
* implicit index raising；
* 同一 equation 中混合两套 (\epsilon_{\alpha\beta}) conventions；
* (\widehat g)、(\widetilde g)、(\mu^2) 混用；
* 未注明 Fourier convention 的 momentum-space vertex；
* 未注明 Grassmann order 的 fermionic product。

任何 convention 修改都必须生成新的：

```text
contract_hash
```

所有旧 trace 自动变为 `STALE`，不能继续沿用。

---

# 四、Calculation state machine

不能允许 Codex 从“定义作用量”直接跳到“最终系数”。

[
\boxed{
\texttt{SPECIFIED}
\to
\texttt{FROZEN}
\to
\texttt{RULES_DERIVED}
\to
\texttt{ENUMERATED}
\to
\texttt{EVALUATED}
\to
\texttt{CUT_COMPLETE}
\to
\texttt{RENORMALIZED}
\to
\texttt{WARD_CLOSED}
\to
\texttt{COHOMOLOGY_PROJECTED}
\to
\texttt{ACCEPTED}
}
]

| Stage                  | Mandatory artifact             | Blocking condition      |
| ---------------------- | ------------------------------ | ----------------------- |
| `FROZEN`               | notation/action/SUSY hashes    | undefined convention    |
| `RULES_DERIVED`        | ordered functional derivatives | quoted vertex           |
| `ENUMERATED`           | complete graph census          | unclassified topology   |
| `EVALUATED`            | Wick/color/spinor trace        | unexplained sign        |
| `CUT_COMPLETE`         | cut-contact ledger             | unmatched (q_d^2) cut   |
| `RENORMALIZED`         | physical–evanescent (Z)-matrix | unspecified scheme      |
| `WARD_CLOSED`          | Ward/ST/(\xi)-tests            | nonzero violation       |
| `COHOMOLOGY_PROJECTED` | BRST/EOM subtraction           | raw representative only |
| `ACCEPTED`             | independent channel comparison | normalization mismatch  |

`BLOCKED` 必须是合法结果，例如：

```text
BLOCKED_UNDEFINED_SYMBOL
BLOCKED_UNDERIVED_VERTEX
BLOCKED_GRAPH_INCOMPLETE
BLOCKED_UNPAIRED_CUT
BLOCKED_WARD_FAILURE
BLOCKED_SCHEME_UNFIXED
```

禁止 Codex 为了“完成任务”自动猜测缺失 convention。

---

# 五、把 EOM-cut intuition 写成 algorithm，而不是口头原则

你的核心物理 intuition 应当编码为一个 exact transformation：

[
q_{(4)}^2=q_d^2+\mu_q^2.
]

因此每一个相关 integrand 必须被重写为

[
\frac{q_{(4)}^2R(q)}
{q_d^2D_1D_2}
=============

\underbrace{
\frac{R(q)}{D_1D_2}
}*{\texttt{CutRecord}}
+
\underbrace{
\frac{\mu_q^2R(q)}
{q_d^2D_1D_2}
}*{\texttt{EvanescentRecord}}.
]

对每个 `CutRecord`：

[
\Gamma_{\mathrm{cut},a}
+
\Gamma_{\mathrm{contact},a}=0
]

必须由 action-derived contact graph 验证；不能由程序直接宣布“这是 Schwinger–Dyson cancellation”。

你当前 engine 已经能够验证 candidate pair，但尚不能从 action 自动生成 contact graph，这正是最优先的 software blocker。

完整 anomaly candidate 应写为

[
q_{1,\mathrm{ren}}O
===================

P_{\mathrm{loc}}
\left[
\sum_{G\in\mathfrak G_{\mathrm{complete}}}
\Gamma_G^{\mathrm{ev}}
+
\delta Z_{PP}O_P
+
\delta Z_{PE}E
+
\delta Z_{\mathrm{BRST}}
+
\delta Z_{\mathrm{EOM}}
\right].
]

因此更严格的结论是：

[
\boxed{
\text{anomaly is organized by the failure of the naive cut identity,}
}
]

但不能在完成 physical–evanescent mixing 之前直接断言：

[
\text{physical anomaly}=\text{single }\mu^2\text{ triangle}.
]

---

# 六、必须显式建立 physical–evanescent operator space

定义

[
\mathcal V_{\mathrm{ext}}
=========================

\mathcal V_{\mathrm{phys}}
\oplus
\mathcal V_{\mathrm{ev}}
\oplus
\operatorname{im}s_{\mathrm{BRST}}
\oplus
\langle\mathcal E_X\rangle .
]

Renormalization matrix 必须包含

[
\begin{pmatrix}
O_P^{B}\
E^{B}
\end{pmatrix}
=============

\begin{pmatrix}
Z_{PP}&Z_{PE}\
Z_{EP}&Z_{EE}
\end{pmatrix}
\begin{pmatrix}
O_P^{R}\
E^{R}
\end{pmatrix}.
]

Raw (q_1) 可以依赖 finite renormalization。令

[
O_R'=(1+\hbar r)O_R,
]

则

[
q_1'=q_1+[r,q_0].
]

但是在允许的 basis change 下，

[
\begin{aligned}
d_1'-d_1
&=
P_H[r,q_0]i_H\
&=
P_Hr q_0i_H-P_Hq_0ri_H\
&=
P_Hr(0)-(0)ri_H\
&=0.
\end{aligned}
]

所以最终 acceptance object 必须始终是

[
\boxed{d_1=P_Hq_1i_H,}
]

而不是某个裸 triangle coefficient。你当前 ES 的“nonzero evanescent pole、zero canonical physical projection”正说明必须严格区分这两个层次。

---

# 七、Codex / ChatGPT / Human 的固定分工

| Actor              | Allowed responsibility                                               | Forbidden responsibility   |
| ------------------ | -------------------------------------------------------------------- | -------------------------- |
| **Human PI**       | freeze conventions、选择 renormalization scheme、裁决 physical equivalence | 手工修改 generated coefficient |
| **ChatGPT Pro**    | design proof obligations、physics audit、检查遗漏图、审核 trace、比较 channels    | 成为 coefficient authority   |
| **Codex Builder**  | 实现一个 bounded task、运行 tests、输出完整 trace                                | 发明 convention、引用另一 channel |
| **Codex Reviewer** | fresh-context `/review`、只读 diff、找错误                                  | 修改 builder branch          |
| **Notion**         | dashboard、报告、状态、链接 commit/hash                                       | 保存唯一计算源                    |

Codex 官方支持 hierarchical `AGENTS.md`、project-local instructions、CLI 中的 repeatable command execution；`/review` 可以启动独立 reviewer，在不修改 working tree 的情况下检查 changes。([[OpenAI Developers](https://developers.openai.com/codex/cli)][2])

ChatGPT Project 只保存 curated context：

```text
PROJECT_STATE.md
notation.generated.md
current_task.yaml
latest_audit.md
result_ledger.md
```

不要把所有 graph traces 都塞进 ChatGPT context。Projects 适合组织长期使用的 chats、files、instructions 和 sources，但真正可执行状态仍应位于 repo。([[Learn ChatGPT](https://learn.chatgpt.com/codex/projects)][3])

---

# 八、每一次 Codex run 的 rigid protocol

## Start

```text
1. Verify clean Git worktree.
2. Print loaded AGENTS.md files.
3. Load exactly one task packet.
4. Print allowed and forbidden inputs.
5. Verify contract hashes.
6. Run baseline tests.
7. Refuse execution if any prerequisite is not PASS.
```

## During

```text
1. One proof obligation only.
2. No contract modification.
3. No reading legacy/ or another channel.
4. No unlogged simplify().
5. Every rewrite emits:
   rule_id
   input
   conditions
   sign
   output
   invariant_checks
6. Every coefficient carries a provenance DAG.
```

## End

```text
1. Run task tests.
2. Run global invariant tests.
3. Generate canonical JSON trace.
4. Generate human-readable report from JSON.
5. Write manifest with all hashes.
6. Write exact blocker/next obligation.
7. Commit atomically.
8. Launch fresh-context reviewer.
```

新的 session 不需要“回忆上一次聊天”，只需读取：

[
\texttt{current_task.yaml}
+
\texttt{status.json}
+
\texttt{trace_manifest.json}.
]

Codex 的 long-running workflow 本身也强调 goal 必须包含 **Outcome、Constraints、Verification**；并行任务不应修改同一文件，可通过 Git worktrees 隔离。([[Learn ChatGPT](https://learn.chatgpt.com/codex/long-running-work)][4])

---

# 九、建议的 root `AGENTS.md`

```markdown
# AWI Proof Repository

## Authority
- Git-tracked contracts, source files, generated traces, and tests are the
  only admissible computational evidence.
- Notion, literature, legacy notes, chat messages, and another calculation
  channel are not coefficient authorities.

## Scope
- Execute exactly one task from tasks/CURRENT.yaml.
- Do not modify contracts/ unless the task type is CONTRACT_CHANGE.
- Do not read legacy/ or another channel directory.

## Mathematical rigor
- Every symbol must resolve through contracts/notation.yaml.
- Never use an untyped q^2.
- Never import a propagator, vertex, sign, graph multiplicity, or coefficient.
- Derive vertices by ordered functional differentiation from the locked action.
- Emit every Wick pairing, fermion permutation, color order, and symmetry factor.
- Black-box simplification without an input/output trace is forbidden.

## DRED
- Split every four-dimensional loop scalar product before tensor reduction.
- Emit a CutRecord for every dimensional denominator cancellation.
- An unmatched CutRecord is a hard failure.
- Retain all evanescent terms through pole expansion.

## Completion
- A calculation is incomplete unless graph inventory, Ward/ST tests,
  renormalization, and cohomological projection pass.
- Missing information must produce BLOCKED_<reason>; never guess.
```

---

# 十、实际执行顺序

[
\boxed{\text{在完成 Task 0--2 之前，不再新增任何 Feynman graph。}}
]

### Task 0 — Authority repair

* 初始化 Git；
* 将 local repo 设为唯一 source of truth；
* Notion 改为 mirror；
* archive 所有 legacy result；
* 为每个现有公式标记 `DERIVED / TARGET / WITHDRAWN / UNVERIFIED`。

### Task 1 — Convention compiler

完成：

```text
notation.yaml
index_spaces.yaml
fourier_sigma.yaml
dred.yaml
notation_lint
convention_hash
```

并通过：

[
\text{propagator inversion},
\quad
\sigma\text{-identities},
\quad
\text{tree-level SUSY/Ward tests}.
]

### Task 2 — Proof-state engine

实现：

```text
proof_obligations.json
state transitions
provenance DAG
canonical trace format
staleness propagation
```

### Task 3 — EC action-to-rule compiler

只从 Euclidean component action 生成：

* Hessian；
* propagators；
* cubic/quartic vertices；
* EOM vertices；
* gauge-fixing/ghost vertices；
* nonlinear composite vertices。

### Task 4 — Graph census and contact generator

这是你现在最需要补的模块：

[
\text{action}
\longrightarrow
\text{all EOM/contact graphs}
\longrightarrow
\text{cut-contact ledger}.
]

### Task 5 — Complete one self-contained benchmark

先完成：

[
\mathcal N=1\ \text{pure SYM},\qquad
q_1(f_{++}^Af_{++}^B),
]

要求 graph-complete、Ward-closed，即使最终 physical projection 为零也接受为 calibration。

随后依次：

[
\mathcal N=1+\text{one adjoint chiral}
\longrightarrow
\mathcal N=4\ R1
\longrightarrow
\mathcal N=4\ R2.
]

### Task 6 — ES independent replication

EC 的 canonical result 被锁定后，ES 才能启动。ES agent 不得读取 EC intermediate results，只能在最终 `result.json` 层比较。

---

最终原则可以压缩为三条：

[
\boxed{\text{One task = one proof obligation = one branch = one gate.}}
]

[
\boxed{\text{No model context is trusted; only versioned artifacts are trusted.}}
]

[
\boxed{\text{The anomaly coefficient is accepted only after cut completion, renormalization, Ward closure, and }P_H.}
]

[1]: https://developers.openai.com/codex/guides/agents-md "
  Custom instructions with AGENTS.md | ChatGPT Learn
"
[2]: https://developers.openai.com/codex/cli "
  Codex CLI | ChatGPT Learn
"
[3]: https://learn.chatgpt.com/codex/projects "
  Projects, chats, and tasks | ChatGPT Learn
"
[4]: https://learn.chatgpt.com/codex/long-running-work "
  Long-running work | ChatGPT Learn
"
