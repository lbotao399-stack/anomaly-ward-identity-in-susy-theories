# User-supplied GPT Pro diagnosis — external gap review

- Date received: `2026-07-13`
- Authority role: `EXTERNAL_GAP_REVIEW_ONLY`
- Mathematical import: `FORBIDDEN`
- Final two-loop coefficient: `NOT_SUPPLIED`
- Use: type-boundary and missing-proof-obligation audit only

---
According to a document from 2026-07-13，当前 blocker 不是某个 isolated sign error，而是 **certificate boundary/type error**：

[
\mathfrak D
]

只是 pre-integration (D)-algebra proof object；但 anomaly coefficient 属于 integration、SD-contact closure、operator quotient 之后的对象。当前 pipeline 试图从信息不足的 type 读出 anomaly，因此 `NOT_ACCEPTED` 是正确结果。近期 finite-basis checker 已经验证 local (D/\bar D) algebra、endpoint transfer、delta convolution、(16^3=4096) transfer grid、SD edge normalization 以及 six-slot coefficient maps，可直接作为新 compiler 的 semantic oracle。

## 新引入记号

[
\mathfrak I=\text{master-integral IR},\qquad
\mathfrak C_{\mathrm{SD}}=\text{SD/contact-term IR},
]

[
\mathbf B=(B_1,\ldots ,B_m)^{\mathsf T}
=\text{固定的 local contact/operator basis},
]

[
\mathbf v_d,\mathbf v_r\in\mathbb K^m
=\text{direct/reflected orientation 的 basis vectors},
]

[
R\in M_m(\mathbb K)
=\text{reflection 在 basis 上的 exact matrix},
]

[
L_{\mathrm{UV}}
:=\frac{1}{(4\pi)^2}\frac1\varepsilon
=\text{标准 Euclidean bubble pole atom},
]

[
Q_{\mathrm{triv}}
=\text{BRST-exact/EOM/total-derivative vectors 组成的 matrix},
\qquad
\mathbf b_{\mathcal A}
=\text{normalized anomaly basis vector}.
]

(L_{\mathrm{UV}}) 不是 (\mathbb K) 的元素；它应当是 typed integral atom，其 algebraic coefficient 仍严格位于

[
\mathbb K=\mathbb Q(i,\sqrt2).
]

---

# 1. 正确的完整 pipeline

当前

[
\mathfrak N\to\mathfrak G\to\mathfrak A\to\mathfrak D
]

应扩充为

[
\boxed{
\mathfrak N
\longrightarrow\mathfrak G
\longrightarrow\mathfrak A
\longrightarrow\mathfrak D_{\mathrm{NF}}
\longrightarrow
\bigl(\mathfrak I\oplus\mathfrak C_{\mathrm{SD}}\bigr)
\longrightarrow
\bigl(\mathfrak P_{\mathrm{UV}}\oplus H_{\mathrm{SD}}\bigr)
\longrightarrow
\mathfrak C_{\mathrm{anomaly}}
}
]

其中：

[
\mathfrak D_{\mathrm{NF}}
=\text{phase-complete canonical (D)-normal form},
]

[
H_{\mathrm{SD}}
===============

\mathfrak C_{\mathrm{SD}}
\big/
\bigl(
\text{exact}+\text{EOM}+\text{total derivative}
\bigr).
]

不存在合法的 implicit cast

[
\boxed{
\mathfrak P_{\mathrm{UV}}
\not\Longrightarrow
\text{anomaly coefficient}.
}
]

必须经过 renormalized AWI/cohomology projection。一个非零 graph 或 UV pole 本身不能定义 anomaly；还需要 graph/contact completeness、operator mixing quotient 与 cohomology reduction。

---

# 2. 修复 `UNIMPLEMENTED_PHASE_SEQUENCE`

约定 operator word 中 **rightmost operator acts first**。同一 endpoint、同一 momentum (r) 上，

[
{D_\alpha[r],\bar D_{\dot\alpha}[r]}
=-2ir_{\alpha\dot\alpha}.
]

因此两种 rewrite 都必须实现：

[
\bar D_{\dot\alpha}D_\alpha
===========================

-D_\alpha\bar D_{\dot\alpha}
-2ir_{\alpha\dot\alpha},
]

[
D_\alpha\bar D_{\dot\alpha}
===========================

-\bar D_{\dot\alpha}D_\alpha
-2ir_{\alpha\dot\alpha}.
]

令

[
\bar D_{\dot\alpha}\Phi_c=0,
\qquad
D_\alpha\bar\Phi_a=0.
]

则 mixed-order 的四个 exact results 为

[
\begin{array}{c|cc}
& D_\alpha\bar D_{\dot\alpha}
&\bar D_{\dot\alpha}D_\alpha\
\hline
\Phi_c
&0
&-2ir_{\alpha\dot\alpha}\Phi_c[1mm]
\bar\Phi_a
&-2ir_{\alpha\dot\alpha}\bar\Phi_a
&0
\end{array}
]

所以不应再把 mixed chirality sequence 视为 unsupported。它只能产生三类结果：

[
\boxed{
0,\qquad
\text{normal-ordered derivative word},\qquad
-2ir_{\alpha\dot\alpha}\times\text{shorter word}.
}
]

### Canonical ordering

对 chiral target，取

[
D\cdots D,\bar D\cdots\bar D
]

为 normal order，使 (\bar D) 位于最右侧并立即执行 chirality annihilation。

对 antichiral target，取

[
\bar D\cdots\bar D,D\cdots D.
]

令 rewrite complexity 为

[
\mu(w)=
\bigl(
N_{\mathrm{mixed\ inversion}}(w),\ |w|
\bigr)
]

并使用 lexicographic order。每次 mixed swap：

* swapped branch 减少 (N_{\mathrm{mixed\ inversion}})；
* anticommutator branch 将 (|w|) 减少 (2)。

故 rewrite termination 是严格的。

Confluence 不要只靠 syntactic critical-pair test；应把每个 word 编译为 local (16\times16) Grassmann representation，验证两个 normal-order path 给出同一 matrix。现有 checker 已经以 symbolic momentum 验证完整 local superderivative algebra，可直接成为 oracle。

---

# 3. 每个 orientation 的 eight-row ledger

不要手写 specialized equations。每个 orientation 自动生成以下八个 semantic phases：

| Row | Phase                 | Exact obligation                                 |
| --: | --------------------- | ------------------------------------------------ |
|   1 | `SEED`                | 保存 (C_o)、routing、ordered factors                 |
|   2 | `PROJECTOR_ATTACH`    | 插入 typed local projector                         |
|   3 | `ENDPOINT_TRANSFER`   | 执行 (D,\bar D,K_+) endpoint identities            |
|   4 | `MEASURE_IBP`         | 执行 graded integration by parts 与 Koszul sign     |
|   5 | `MIXED_NORMALIZE`     | 使用 ({D,\bar D}=-2ir) normal ordering             |
|   6 | `CHIRALITY_COLLAPSE`  | 应用 chiral/antichiral annihilator                 |
|   7 | `DELTA_SD_COLLAPSE`   | delta convolution、edge collapse、contact emission |
|   8 | `BASIS_INTEGRAL_EMIT` | 输出 basis vector 与 integral fingerprints          |

每行必须保存

[
(\texttt{before},\texttt{rule_id},
\Delta_{\mathrm{Koszul}},
\texttt{routing_before},
\texttt{routing_after},
\texttt{after},
\texttt{parent_hash}).
]

已有 checker 证明

[
K_{+,0}[p]\Delta_{01}
=====================

-K_{+,1}[-p]\Delta_{01},
]

以及

[
\int d^4\theta_1,\Delta_{01}\Delta_{12}
=\Delta_{02},
]

并穷尽检查了所有 (16^3) local monomial triples 的 transfer-and-measure-IBP identity。该 checker 应从 standalone audit 转为每一行 ledger 的 replay backend。

旧 16-row ledger 只能作为 regression oracle：

[
\operatorname{NF}_{\mathrm{new}}(\text{seed})
=============================================

\operatorname{canonicalize}
\bigl(\operatorname{output}_{\mathrm{legacy}}\bigr),
]

但新 certificate 的 provenance graph 不得引用 legacy output。

---

# 4. `IntegralPoleCompiler` 的 exact binding

定义

[
D_0=k^2,\qquad
D_1=(k+q)^2,\qquad
D_2=(k+p+q)^2,
]

[
T[N]
====

\mu^{2\varepsilon}
\int\frac{d^{4-2\varepsilon}k}{(2\pi)^{4-2\varepsilon}}
\frac{N(k,p,q)}{D_0D_1D_2}.
]

精确 denominator identities：

[
2k\cdot q=D_1-D_0-q^2,
]

[
2k\cdot(p+q)
=D_2-D_0-(p+q)^2,
]

[
2k\cdot p
=D_2-D_1-(p+q)^2+q^2.
]

Superficial UV degree 为

[
\omega_{\mathrm{UV}}
====================

# 4+\deg_kN-6

\deg_kN-2.
]

所以：

[
\deg_kN=0,1
\quad\Longrightarrow\quad
\operatorname{Pole}_{\varepsilon}T[N]=0
]

在 external momenta non-exceptional 时成立。

对于 denominator-cancelling terms，

[
T[D_0]
======

\mu^{2\varepsilon}
\int\frac{d^{4-2\varepsilon}\ell}{(2\pi)^{4-2\varepsilon}}
\frac1{\ell^2(\ell+p)^2},
]

[
T[D_1]
======

\mu^{2\varepsilon}
\int\frac{d^{4-2\varepsilon}\ell}{(2\pi)^{4-2\varepsilon}}
\frac1{\ell^2(\ell+p+q)^2},
]

[
T[D_2]
======

\mu^{2\varepsilon}
\int\frac{d^{4-2\varepsilon}\ell}{(2\pi)^{4-2\varepsilon}}
\frac1{\ell^2(\ell+q)^2}.
]

使用

[
B(P^2)
======

\frac{\mu^{2\varepsilon}}{(4\pi)^{2-\varepsilon}}
\Gamma(\varepsilon)
\int_0^1dx,
[x(1-x)P^2]^{-\varepsilon},
]

得到

[
\boxed{
\operatorname{Pole}_{\varepsilon}B(P^2)
=======================================

# L_{\mathrm{UV}}

\frac1{(4\pi)^2}\frac1\varepsilon
}
\qquad(P^2\neq0).
]

因此

[
\boxed{
\operatorname{Pole}_{\varepsilon}T[D_0]
=======================================

# \operatorname{Pole}_{\varepsilon}T[D_1]

# \operatorname{Pole}_{\varepsilon}T[D_2]

L_{\mathrm{UV}}.
}
]

若 numerator reduction 给出

[
N=a_0D_0+a_1D_1+a_2D_2+N_{\mathrm{UV-fin}},
]

且 compiler 已证明

[
\operatorname{Pole}*{\varepsilon}T[N*{\mathrm{UV-fin}}]=0,
]

则

[
\boxed{
\operatorname{Pole}_{\varepsilon}T[N]
=====================================

(a_0+a_1+a_2)L_{\mathrm{UV}}.
}
]

`UVPoleCertificate` 至少保存：

[
\left(
\texttt{routing_hash},
\texttt{numerator_hash},
\texttt{master_ids},
\texttt{reduction_proof},
r_{-1},
\texttt{UV/IR_status},
\texttt{basis_vector}
\right).
]

遇到 scaleless master 时，不得直接用“DR 中等于零”作为 UV certificate；应返回

```text
UV_IR_SEPARATION_REQUIRED
```

直到加入 non-exceptional kinematics、mass regulator 或 (R^\ast)-type separation。

---

# 5. DRED 的 evanescent data 不能丢

(\mathbb K) 保持不变。Laurent degree 应作为 metadata：

[
c(\varepsilon)=c_0+\varepsilon c_1,
\qquad
c_0,c_1\in\mathbb K,
]

[
I(\varepsilon)
==============

\varepsilon^{-1}r_{-1}+r_0.
]

所需 finite coefficient 为

[
\boxed{
[c(\varepsilon)I(\varepsilon)]_{\varepsilon^0}
==============================================

c_0r_0+c_1r_{-1}.
}
]

其中

[
c_1r_{-1}
]

正是 evanescent factor 与 UV pole 相乘产生的 finite local contribution。若 (\mathfrak D) 只保存 four-dimensional (c_0)，即使 (\mathfrak P_{\mathrm{UV}}) 已知，anomaly coefficient 仍不能认证。

因此 `DTerm` 应包含

```text
epsilon_degree: int
coefficient: KElement
```

而不是把 (\varepsilon) 或 (\pi) 塞入 (\mathbb K)。DRED contract 还必须固定 momentum measure、four-dimensional spinor algebra 与 (d)-dimensional metric contraction 的 separation rule、evanescent basis 和 finite restoration counterterms。

---

# 6. 闭合 basis-resolved SD contact orbit

对当前 six-slot basis，令

[
\mathbf B=(B_1,\ldots ,B_6)^{\mathsf T}.
]

对每个 contact rewrite generator (T_j)，要求存在

[
M_j\in M_6(\mathbb K)
]

使

[
T_j(\mathbf B)=M_j\mathbf B.
]

从 direct/reflected seeds 开始：

[
V_0=\operatorname{span}_{\mathbb K}
{\mathbf v_d,\mathbf v_r},
]

[
V_{n+1}
`=======`

V_n+\sum_jM_jV_n.
]

当

[
\dim_{\mathbb K}V_{n+1}
=======================

\dim_{\mathbb K}V_n
]

时，orbit 严格闭合。因为 ambient dimension 为 (6)，严格维数增长最多发生 (6) 次。

现有 checker 已验证：

[
\text{SD}\times\text{Euler}\times\text{propagator}
=I_2,
]

并验证 grouped (4\times6) map 与 converted PLUS/MINUS map 都给出

[
(1,1,1,1,1,1).
]

这些应成为 (M_j) calibration tests，而不是最终 anomaly proof。

---

# 7. 两个 orientation 的 exact combination

完成八行 reduction 与 integral/contact projection 后，定义

[
\mathcal P_o
============

L_{\mathrm{UV}},
\mathbf B^{\mathsf T}\mathbf v_o,
\qquad
o\in{d,r}.
]

总 UV-local vector 为

[
\begin{aligned}
\mathcal P_{\mathrm{tot}}
&=
C_d\mathcal P_d+C_r\mathcal P_r\
&=
-\frac{g^2}{8}
L_{\mathrm{UV}}\mathbf B^{\mathsf T}\mathbf v_d
+
\frac{g^2}{8}
L_{\mathrm{UV}}\mathbf B^{\mathsf T}\mathbf v_r\
&=
\boxed{
\frac{g^2}{8}
L_{\mathrm{UV}}
\mathbf B^{\mathsf T}
(\mathbf v_r-\mathbf v_d)
}.
\end{aligned}
]

若 reflection compiler 证明

[
\mathbf v_r=R\mathbf v_d,
]

则

[
\boxed{
\mathcal P_{\mathrm{tot}}
=========================

\frac{g^2}{8}
L_{\mathrm{UV}}
\mathbf B^{\mathsf T}
(R-I_m)\mathbf v_d.
}
]

两个重要 special cases：

[
R\mathbf v_d=\mathbf v_d
\quad\Longrightarrow\quad
\mathcal P_{\mathrm{tot}}=0,
]

[
R\mathbf v_d=-\mathbf v_d
\quad\Longrightarrow\quad
\mathcal P_{\mathrm{tot}}
=========================

-\frac{g^2}{4}
L_{\mathrm{UV}}
\mathbf B^{\mathsf T}\mathbf v_d.
]

已验证的 (K_+) endpoint transfer 提供一个 minus sign，但它不单独决定 (R=-I_m)；Wick/Koszul、factor reversal、spinor-index permutation 和 routing substitution 也必须包含在 (R) 中。

---

# 8. anomaly coefficient 的唯一合法 extraction

令

[
\mathbf u
=========

\frac{g^2}{8}
(\mathbf v_r-\mathbf v_d).
]

在 operator quotient 中解 exact linear system：

[
\boxed{
\mathbf u
=========

Q_{\mathrm{triv}}\mathbf x
+
a_{\mathcal A}\mathbf b_{\mathcal A}.
}
]

若

[
\operatorname{rank}
\begin{pmatrix}
Q_{\mathrm{triv}}&\mathbf b_{\mathcal A}
\end{pmatrix}
=============

\operatorname{rank}
\begin{pmatrix}
Q_{\mathrm{triv}}&\mathbf b_{\mathcal A}&\mathbf u
\end{pmatrix}
]

且

[
\mathbf b_{\mathcal A}
\notin\operatorname{im}Q_{\mathrm{triv}},
]

则 (a_{\mathcal A}) 唯一，并可返回

[
\boxed{
\texttt{ANOMALY_ACCEPTED}
\quad\text{with coefficient}\quad
a_{\mathcal A}.
}
]

若 quotient dimension 大于 (1)，则输出必须是 anomaly vector

[
(a_1,\ldots ,a_s),
]

不能伪装成单一 coefficient。

---

# 9. 最终 acceptance predicate

[
\boxed{
\begin{aligned}
\mathrm{Accept}
={}&
\mathrm{GraphComplete}
\land
\mathrm{EightRows}(d)
\land
\mathrm{EightRows}(r)\
&\land
\mathrm{DReplayable}
\land
\mathrm{MixedSequenceComplete}
\land
\mathrm{SDOrbitClosed}\
&\land
\mathrm{AllIntegralsBound}
\land
\mathrm{UVIRSeparated}
\land
\mathrm{EvanescentClosed}\
&\land
\mathrm{OperatorBasisClosed}
\land
\mathrm{CohomologyProjectionUnique}\
&\land
\mathrm{NoLegacyProvenance}.
\end{aligned}
}
]

在此之前，正确输出仍为

```text
anomaly_coefficient:
  status: NOT_ACCEPTED
  missing:
    - direct eight-row D-ledger
    - reflected eight-row D-ledger
    - IntegralPoleCompiler binding
    - closed SD contact orbit
    - evanescent/pole finite-part binding
    - unique cohomology projection
```

## 结论

当前系统已经正确完成

[
\mathfrak N\to\mathfrak G\to\mathfrak A\to\mathfrak D,
]

但 anomaly 的真实 computational boundary 是

[
\boxed{
\mathfrak D
\to
(\mathfrak I,\mathfrak C_{\mathrm{SD}})
\to
(\mathfrak P_{\mathrm{UV}},H_{\mathrm{SD}})
\to
a_{\mathcal A}.
}
]

给定现有信息，不能严格算出 numeric (a_{\mathcal A})，因为缺少实际的

[
\mathbf v_d,\qquad \mathbf v_r
]

以及它们的 integral/contact/cohomology certificates。可以严格确定的是最终 coefficient 必须由

[
\boxed{
\mathbf u=\frac{g^2}{8}(\mathbf v_r-\mathbf v_d),
\qquad
\mathbf u=Q_{\mathrm{triv}}\mathbf x+a_{\mathcal A}\mathbf b_{\mathcal A}
}
]

这两个 exact equations 唯一决定。
