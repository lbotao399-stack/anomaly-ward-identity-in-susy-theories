---
status: GAP_REVIEW_ONLY_NO_FORMULA_AUTHORITY
authority: NONE
calculation_input: false
external_target_input: false
source_surface: GPT Pro browser conversation
captured_date: 2026-07-12
---

# Step 6 GPT Pro round 2 — raw architecture review

## Prompt

We now start a new, strictly isolated two-loop problem.

Goal: in Euclidean 4d N=4 SYM written in N=1 superspace, study the pure-gauge contribution to
  nabla_-[(nabla_+ W_+^A)(nabla_+ W_+^B)]
at two loops, initially focusing on the Chinese-character "日" topology. The eventual external comparison target is the classic holomorphic-twist Q_2(b^A b^B) result, but that literature coefficient/result must NEVER be used as an input to the Euclidean SYM derivation. Separate it into an EXTERNAL_TARGET ledger only.

Repository authority boundary: only verified origin/main conventions/actions may settle formulas. The current typed one-loop compiler branch is merely a proposal: immutable notation schema -> connected Wick-complete D-unreduced GraphIR -> factorized AmplitudeIR -> partial phased D-algebra. Do not assume its candidate one-loop coefficient or its unfinished contact orbit.

Act as a preliminary architecture and forensic calculation reviewer. Give an explicit, checkable two-loop plan, and do preliminary algebra only where conventions can remain symbolic. Required:

1. Define precisely which connected superspace graph is meant by the "日" graph: vertices, internal typed propagators, external legs, E-V-I identity, loop number, and all inequivalent derivative-port/orientation variants. State whether a literal two-rung ladder, theta/double-bubble, or sunset naming ambiguity exists.
2. Derive the perturbative-order equation and list exactly which action vertices S_(n), insertion terms I_(n), nonlinear W/Gamma/E_V terms, FP/NK graphs, quartic/seagull graphs, counterterms, and Schwinger-Dyson cut descendants occur at the same order. No topology-only omission.
3. Give a canonical two-loop momentum routing from an oriented incidence matrix, with two chord momenta k,l and every edge momentum; state how graph automorphisms and labeled Wick-pairing sums avoid double division.
4. Design the exact edge-tagged two-loop superspace D-algebra schedule. Separate scope expansion, endpoint transfer, pivoted IBP, mixed D-barD normalization, projector reduction, chirality, Grassmann saturation, and typed edge collapse. Identify new two-loop critical pairs and termination measures.
5. Specify the DRED treatment: four-dimensional spinor algebra, d-dimensional loop tensors, g4/ghat/gtilde separation at two loops, and exactly where evanescent numerators can arise. Never put epsilon into a bare numerator.
6. Treat UV subdivergences rigorously: forest formula/R-operation, one-loop counterterm insertions, IR-safe off-shell kinematics, overlapping vs nested subgraphs, and how to separate primitive two-loop poles from products of one-loop poles.
7. Identify the scalar/tensor integral families after D-algebra and the necessary IBP/master-integral certificate. State which data an IntegralPoleCompiler must retain.
8. Give the complete Schwinger-Dyson orbit needed before calling anything an anomaly: parent 日 graphs, propagator collapses, nonlinear-letter/contact children, bubble descendants, ghosts, counterterms, and quotient-space multiplicity equality. Explain the expected cancellation of ordinary terms without importing the twist answer.
9. Propose exact GraphIR/AmplitudeIR/DWordIR/PoleIR extensions and deterministic tests, with staged acceptance gates.
10. In a completely separate final section, identify the precise holomorphic-twist paper(s), equation number/page if known, and copy only the published Q_2(b^A b^B) 日-graph target formula with its source convention dictionary. Mark every such statement EXTERNAL_TARGET_NOT_DERIVATION. If you cannot verify an exact citation, say so rather than guessing.
11. Finish with a strict find-gap table using G-DEF/G-IDX/G-SIGN/G-ALG/G-OP/G-THM/G-PROJ/G-NORM/G-SCOPE and P0-P3.

Do not give a final Euclidean SYM coefficient unless you actually derive every factor. Distinguish proved topology identities, convention-dependent placeholders, conjectures, and external targets.Show moreShow less

## Response

0. Status labels and authority boundary
以下标签贯穿全文：
PROVED_TOPOLOGY纯图论、loop counting 或 incidence-matrix identityMAIN_DERIVED仅由 verified origin/main action/conventions 推导SYMBOLIC_PLACEHOLDER结构确定，但 normalization/sign 尚待 main-side compiler 输出PROOF_OBLIGATION不得作为已证明结果EXTERNAL_TARGET_NOT_DERIVATION仅用于最终 comparison，禁止进入 Euclidean derivation AST\begin{array}{c|l}
\texttt{PROVED\_TOPOLOGY}
&\text{纯图论、loop counting 或 incidence-matrix identity}
\\
\texttt{MAIN\_DERIVED}
&\text{仅由 verified }origin/main\text{ action/conventions 推导}
\\
\texttt{SYMBOLIC\_PLACEHOLDER}
&\text{结构确定，但 normalization/sign 尚待 main-side compiler 输出}
\\
\texttt{PROOF\_OBLIGATION}
&\text{不得作为已证明结果}
\\
\texttt{EXTERNAL\_TARGET\_NOT\_DERIVATION}
&\text{仅用于最终 comparison，禁止进入 Euclidean derivation AST}
\end{array}PROVED_TOPOLOGYMAIN_DERIVEDSYMBOLIC_PLACEHOLDERPROOF_OBLIGATIONEXTERNAL_TARGET_NOT_DERIVATION​纯图论、loop counting 或 incidence-matrix identity仅由 verified origin/main action/conventions 推导结构确定，但 normalization/sign 尚待 main-side compiler 输出不得作为已证明结果仅用于最终 comparison，禁止进入 Euclidean derivation AST​
Verified main 固定
h=g−2,cABC=κCDcABD=c[ABC],h=g^{-2},
\qquad
c_{ABC}=\kappa_{CD}c_{AB}{}^D=c_{[ABC]},h=g−2,cABC​=κCD​cAB​D=c[ABC]​,
以及 Euclidean N=4\mathcal N=4N=4 action 中彼此独立的 chiral gauge kinetic、antichiral gauge kinetic、matter bridge 和两套 cubic superpotential。
本回答不使用 proposal branch 的 one-loop coefficient，也不假定它的 aggregate contact identity。

1. “日” graph 的精确定义
1.1 推荐锁定的 underlying graph
把 “日” 定义为
Γ\日:=K4∖e\boxed{
\Gamma_{\日}:=K_4\setminus e
}Γ\日​:=K4​∖e​
即 four vertices、five internal edges、两个三角形共享一条 central edge：
                 v_I
               /  |  \
              /   |   \
       v_{\widetilde W} | v_W
              \   |   /
               \  |  /
                 v_C
顶点：
V(Γ\日)={vI,vC,vW~,vW}.V(\Gamma_{\日})
=
\{v_I,v_C,v_{\widetilde W},v_W\}.V(Γ\日​)={vI​,vC​,vW​,vW​}.
边：
e0=(vI,vC),central edge,e1=(vI,vW~),e2=(vW~,vC),e3=(vI,vW),e4=(vW,vC).\boxed{
\begin{aligned}
e_0&=(v_I,v_C),&&\text{central edge},\\
e_1&=(v_I,v_{\widetilde W}),\\
e_2&=(v_{\widetilde W},v_C),\\
e_3&=(v_I,v_W),\\
e_4&=(v_W,v_C).
\end{aligned}}e0​e1​e2​e3​e4​​=(vI​,vC​),=(vI​,vW​),=(vW​,vC​),=(vI​,vW​),=(vW​,vC​).​central edge,​
Internal degree sequence：
deg⁡int(vI,vC,vW~,vW)=(3,3,2,2).\deg_{\rm int}(v_I,v_C,v_{\widetilde W},v_W)
=
(3,3,2,2).degint​(vI​,vC​,vW​,vW​)=(3,3,2,2).
Euler identity：
L=Iint−V+1=5−4+1=2.\boxed{
L
=
I_{\rm int}-V+1
=
5-4+1
=
2.
}L=Iint​−V+1=5−4+1=2.​
Half-edge identity：
∑vval⁡total(v)=2Iint+Eext.\sum_{v}\operatorname{val}_{\rm total}(v)
=
2I_{\rm int}+E_{\rm ext}.v∑​valtotal​(v)=2Iint​+Eext​.
在 two-external form factor 中：
2Iint+Eext=2⋅5+2=12.2I_{\rm int}+E_{\rm ext}
=
2\cdot5+2
=
12.2Iint​+Eext​=2⋅5+2=12.
这就是需要锁入 schema 的 graph signature：
underlying_simple_graph = K4_MINUS_EDGE
vertices = 4
internal_edges = 5
external_legs = 2
loop_rank = 2
internal_degree_multiset = [3,3,2,2]

1.2 与其他 “two-loop” 昵称的区别
名称VVVIintI_{\rm int}Iint​LLL是否为本项目“日”theta / sunset232否figure-eight，共享一个 vertex342否K4∖eK_4\setminus eK4​∖e bitriangle452是literal multi-rung ladder通常 6通常 72否square-triangle sliding graph562否
外部 holomorphic 文献称同一个 K4∖eK_4\setminus eK4​∖e graph 为 bitriangle，并将其画成 diamond 加 central edge；这是纯 topology correspondence，不是 coefficient correspondence。arXiv

1.3 Provisional external probe
为了使 Euclidean form factor 可计算，需要先锁定 external probes。与 primitive w=0w=0w=0 seed 最接近的 provisional choice 是
Fα˙AB;DE(p,q)=⟨W~α˙D(q) W+E(p) IAB(P)⟩1PI,\boxed{
\mathscr F_{\dot\alpha}^{AB;DE}(p,q)
=
\left\langle
\widetilde W_{\dot\alpha}^{D}(q)\,
W_+^{E}(p)\,
\mathcal I^{AB}(P)
\right\rangle_{\rm 1PI},
}Fα˙AB;DE​(p,q)=⟨Wα˙D​(q)W+E​(p)IAB(P)⟩1PI​,​
IAB=∇− ⁣(XAXB),XA=(∇+W+)A,\mathcal I^{AB}
=
\nabla_-\!\left(X^AX^B\right),
\qquad
X^A=(\nabla_+W_+)^A,IAB=∇−​(XAXB),XA=(∇+​W+​)A,
P+p+q=0.P+p+q=0.P+p+q=0.
这是
SCOPE_LOCK_PROPOSAL,\texttt{SCOPE\_LOCK\_PROPOSAL},SCOPE_LOCK_PROPOSAL,
不是从 topology 自动推出的。若最终 holomorphic dictionary 对应其他 external survivors，必须重新生成 GraphIR，而不是重标这张图。

1.4 同一个“日” topology 的两类 bare source realization
Two-loop、four-vertex graph 意味着有 one insertion vertex 和 three action vertices。由 §2 的 valence equation 可知，仅有：
I(3)S(3)3\boxed{
I_{(3)}S_{(3)}^3
}I(3)​S(3)3​​
和
I(2)S(3)2S(4)\boxed{
I_{(2)}S_{(3)}^2S_{(4)}
}I(2)​S(3)2​S(4)​​
能够在 V=4,I=5,L=2V=4,I=5,L=2V=4,I=5,L=2 下 realization 成 K4∖eK_4\setminus eK4​∖e。
因此必须区分：
RI-CUBIC:
    source family = I3 S3 S3 S3

RI-SEAGULL:
    source family = I2 S3 S3 S4
二者可能在 Schwinger–Dyson cut basis 中相互关联，因此不能把 “日 graph” 等同于单独的 I3S33I_3S_3^3I3​S33​。
对于 I2S32S4I_2S_3^2S_4I2​S32​S4​，若 total valences 是
(2,3,3,4),(2,3,3,4),(2,3,3,4),
要得到 internal degrees (2,2,3,3)(2,2,3,3)(2,2,3,3)，external extraction 必须满足：
eI2=0,e_{I_2}=0,eI2​​=0,
以及：
(eS4,eS3a,eS3b)=(1,1,0)(e_{S_4},e_{S_{3a}},e_{S_{3b}})
=
(1,1,0)(eS4​​,eS3a​​,eS3b​​)=(1,1,0)
或 permutation，或者
(2,0,0).(2,0,0).(2,0,0).
后一个 case 在独立 chiral/antichiral gauge-kinetic sectors 中通常会因不能由单个 gauge quartic vertex 同时承载 WWW 和 W~\widetilde WW 而成为 typed zero；该结论必须由 main-derived action AST 检查，而非 topology 推断。

1.5 全部 inequivalent variants 的正确定义
不能手写一个小整数作为 variant count。完整集合是
V\日={ω, s, ι, σC, ρI, ρC, ρW~, ρW, PWick}/Aut⁡typ.\boxed{
\mathfrak V_{\日}
=
\left\{
\omega,\,
\mathfrak s,\,
\iota,\,
\sigma_C,\,
\rho_I,\,
\rho_C,\,
\rho_{\widetilde W},\,
\rho_W,\,
P_{\rm Wick}
\right\}
/\operatorname{Aut}_{\rm typ}.
}V\日​={ω,s,ι,σC​,ρI​,ρC​,ρW​,ρW​,PWick​}/Auttyp​.​
其中：


ω∈{DIRECT,REFLECTED}\omega\in\{\mathrm{DIRECT},\mathrm{REFLECTED}\}ω∈{DIRECT,REFLECTED}；


s∈{RI ⁣− ⁣CUBIC,RI ⁣− ⁣SEAGULL}\mathfrak s\in\{\mathrm{RI\!-\!CUBIC},\mathrm{RI\!-\!SEAGULL}\}s∈{RI−CUBIC,RI−SEAGULL}；


ι\iotaι 是具体 I(2)I_{(2)}I(2)​ 或 I(3)I_{(3)}I(3)​ AST term；


σC\sigma_CσC​ 是 central cubic 的 chiral/antichiral sector；


ρv\rho_vρv​ 是该 vertex 的 ordered derivative-scope branch；


PWickP_{\rm Wick}PWick​ 是 complete typed Wick pairing；


quotient 只允许保持全部 vertex species、external ordering、derivative scopes、field orientations、color/flavor bindings 的 automorphisms。


Underlying undecorated K4∖eK_4\setminus eK4​∖e 有
Aut⁡(K4∖e)=Z2×Z2.\operatorname{Aut}(K_4\setminus e)
=
\mathbb Z_2\times\mathbb Z_2.Aut(K4​∖e)=Z2​×Z2​.
但对 side-probe decorated graph：


vI≠vCv_I\neq v_CvI​=vC​；


vW~≠vWv_{\widetilde W}\neq v_WvW​=vW​；


所以 typed automorphism group 通常是 trivial。不能预先除 444。

2. Two-loop perturbative-order equation
2.1 Exact valence equation
令：


insertion valence 为 nIn_InI​；


action vertices 为 n1,…,nNn_1,\ldots,n_Nn1​,…,nN​；


external legs 数为 222；


internal edges 数为 IintI_{\rm int}Iint​。


Half-edge counting：
nI+∑a=1Nna=2Iint+2.n_I+\sum_{a=1}^Nn_a
=
2I_{\rm int}+2.nI​+a=1∑N​na​=2Iint​+2.
Connected loop identity：
L=Iint−(N+1)+1=Iint−N.L
=
I_{\rm int}-(N+1)+1
=
I_{\rm int}-N.L=Iint​−(N+1)+1=Iint​−N.
消去 IintI_{\rm int}Iint​：
2L=(nI−2)+∑a=1N(na−2).\boxed{
2L
=
(n_I-2)
+
\sum_{a=1}^N(n_a-2).
}2L=(nI​−2)+a=1∑N​(na​−2).​
At two loops：
(nI−2)+∑a=1N(na−2)=4.\boxed{
(n_I-2)
+
\sum_{a=1}^N(n_a-2)
=
4.
}(nI​−2)+a=1∑N​(na​−2)=4.​
这是所有 bare graph census 的完整 combinatorial gate。

2.2 全部 bare physical families
对 genuine action vertices na≥3n_a\ge3na​≥3，所有非负整数解恰好是：
nIaction content2S34,S32S4,S42,S3S5,S63S33,S3S4,S54S32,S45S361\boxed{
\begin{array}{c|l}
n_I&\text{action content}\\ \hline
2&
S_3^4,\quad
S_3^2S_4,\quad
S_4^2,\quad
S_3S_5,\quad
S_6
\\[1mm]
3&
S_3^3,\quad
S_3S_4,\quad
S_5
\\[1mm]
4&
S_3^2,\quad
S_4
\\[1mm]
5&
S_3
\\[1mm]
6&
1
\end{array}}nI​23456​action contentS34​,S32​S4​,S42​,S3​S5​,S6​S33​,S3​S4​,S5​S32​,S4​S3​1​​​
即：
I2S34,I2S32S4,I2S42,I2S3S5,I2S6,I3S33,I3S3S4,I3S5,I4S32,I4S4,I5S3,I6.\boxed{
\begin{aligned}
&I_2S_3^4,\qquad
I_2S_3^2S_4,\qquad
I_2S_4^2,\qquad
I_2S_3S_5,\qquad
I_2S_6,
\\
&I_3S_3^3,\qquad
I_3S_3S_4,\qquad
I_3S_5,
\\
&I_4S_3^2,\qquad
I_4S_4,
\\
&I_5S_3,\qquad
I_6.
\end{aligned}}​I2​S34​,I2​S32​S4​,I2​S42​,I2​S3​S5​,I2​S6​,I3​S33​,I3​S3​S4​,I3​S5​,I4​S32​,I4​S4​,I5​S3​,I6​.​​
任何“只列 two-loop-looking topology”的 census 都不完整。

2.3 Euclidean interaction-expansion coefficients
写
Sint=∑n≥3S(n).S_{\rm int}
=
\sum_{n\ge3}S_{(n)}.Sint​=n≥3∑​S(n)​.
在
e−Sint/ℏe^{-S_{\rm int}/\hbar}e−Sint​/ℏ
中，具有 NnN_nNn​ 个 SnS_nSn​ vertices 的 combinatorial factor 是
(−1)∑nNn∏nNn!.\boxed{
\frac{(-1)^{\sum_nN_n}}
{\prod_nN_n!}.
}∏n​Nn​!(−1)∑n​Nn​​.​
因此 bare two-loop operator expansion 是
Γbare(2)=+14!⟨I2S34⟩c−12!⟨I2S32S4⟩c+12!⟨I2S42⟩c+⟨I2S3S5⟩c−⟨I2S6⟩c−13!⟨I3S33⟩c+⟨I3S3S4⟩c−⟨I3S5⟩c+12!⟨I4S32⟩c−⟨I4S4⟩c−⟨I5S3⟩c+⟨I6⟩c.\boxed{
\begin{aligned}
\Gamma_{\rm bare}^{(2)}
={}&
+\frac1{4!}\langle I_2S_3^4\rangle_c
-\frac1{2!}\langle I_2S_3^2S_4\rangle_c
+\frac1{2!}\langle I_2S_4^2\rangle_c
\\
&+\langle I_2S_3S_5\rangle_c
-\langle I_2S_6\rangle_c
\\
&-\frac1{3!}\langle I_3S_3^3\rangle_c
+\langle I_3S_3S_4\rangle_c
-\langle I_3S_5\rangle_c
\\
&+\frac1{2!}\langle I_4S_3^2\rangle_c
-\langle I_4S_4\rangle_c
\\
&-\langle I_5S_3\rangle_c
+\langle I_6\rangle_c.
\end{aligned}}Γbare(2)​=​+4!1​⟨I2​S34​⟩c​−2!1​⟨I2​S32​S4​⟩c​+2!1​⟨I2​S42​⟩c​+⟨I2​S3​S5​⟩c​−⟨I2​S6​⟩c​−3!1​⟨I3​S33​⟩c​+⟨I3​S3​S4​⟩c​−⟨I3​S5​⟩c​+2!1​⟨I4​S32​⟩c​−⟨I4​S4​⟩c​−⟨I5​S3​⟩c​+⟨I6​⟩c​.​​
这里每个 SnS_nSn​ 自身仍携带 main action 的原始 Euclidean sign。上式只表示 exponent expansion factor。

3. Main-derived nonlinear ingredients
3.1 Gauge connection and field strength
Verified main 在 gauge-chiral frame 定义
∇aC=e−VDaeV,Wa=−18Dˉ2[e−V(DaeV)],\nabla_a^{\mathsf C}
=
e^{-V}D_ae^V,
\qquad
W_a
=
-\frac18\bar D^2
\left[e^{-V}(D_ae^V)\right],∇aC​=e−VDa​eV,Wa​=−81​Dˉ2[e−V(Da​eV)],
而 antichiral strength 是
W~a˙=+18D2[eV(Dˉa˙e−V)].\widetilde W_{\dot a}
=
+\frac18D^2
\left[e^V(\bar D_{\dot a}e^{-V})\right].Wa˙​=+81​D2[eV(Dˉa˙​e−V)].
因此，直接由 BCH：
Γa:=e−VDaeV=∑n≥1Γ(n)a,\boxed{
\Gamma_a
:=
e^{-V}D_ae^V
=
\sum_{n\ge1}\Gamma_{(n)a},
}Γa​:=e−VDa​eV=n≥1∑​Γ(n)a​,​
Γ(n)a=(−1)n−1n!ad⁡Vn−1(DaV).\boxed{
\Gamma_{(n)a}
=
\frac{(-1)^{n-1}}{n!}
\operatorname{ad}_V^{n-1}(D_aV).
}Γ(n)a​=n!(−1)n−1​adVn−1​(Da​V).​
同理：
Γ~a˙:=eVDˉa˙e−V=−∑n≥11n!ad⁡Vn−1(Dˉa˙V).\boxed{
\widetilde\Gamma_{\dot a}
:=
e^V\bar D_{\dot a}e^{-V}
=
-\sum_{n\ge1}
\frac1{n!}
\operatorname{ad}_V^{n-1}(\bar D_{\dot a}V).
}Γa˙​:=eVDˉa˙​e−V=−n≥1∑​n!1​adVn−1​(Dˉa˙​V).​
然后：
W(n)a=−18Dˉ2Γ(n)a,\boxed{
W_{(n)a}
=
-\frac18\bar D^2\Gamma_{(n)a},
}W(n)a​=−81​Dˉ2Γ(n)a​,​
W~(n)a˙=+18D2Γ~(n)a˙.\boxed{
\widetilde W_{(n)\dot a}
=
+\frac18D^2\widetilde\Gamma_{(n)\dot a}.
}W(n)a˙​=+81​D2Γ(n)a˙​.​
所有 component iii-factors 只能在
[TA,TB]=icABCTC[T_A,T_B]=ic_{AB}{}^CT_C[TA​,TB​]=icAB​CTC​
实际展开时产生；禁止导入 canonical e2gVe^{2gV}e2gV coefficient。

3.2 X(n)X_{(n)}X(n)​
Matrix-adjoint notation 下：
X=∇+W+=D+W++[Γ+,W+].X=\nabla_+W_+
=
D_+W_++[\Gamma_+,W_+].X=∇+​W+​=D+​W+​+[Γ+​,W+​].
因此：
X(n)=D+W(n)++∑r+s=nr,s≥1[Γ(r)+,W(s)+].\boxed{
X_{(n)}
=
D_+W_{(n)+}
+
\sum_{\substack{r+s=n\\r,s\ge1}}
[\Gamma_{(r)+},W_{(s)+}].
}X(n)​=D+​W(n)+​+r+s=nr,s≥1​∑​[Γ(r)+​,W(s)+​].​
Two-loop census 需要：
Γ(n), W(n), Γ~(n), W~(n), X(n)1≤n≤5.\boxed{
\Gamma_{(n)},\,W_{(n)},\,\widetilde\Gamma_{(n)},\,
\widetilde W_{(n)},\,X_{(n)}
\qquad
1\le n\le5.
}Γ(n)​,W(n)​,Γ(n)​,W(n)​,X(n)​1≤n≤5.​
原因是：


S6S_6S6​ 中 WrWsW_rW_sWr​Ws​ 有 r+s=6r+s=6r+s=6，故 max⁡(r,s)=5\max(r,s)=5max(r,s)=5；


I6I_6I6​ 中 XrXsX_rX_sXr​Xs​ 有 r+s=6r+s=6r+s=6，故需要 X5X_5X5​。



3.3 I(2),…,I(6)I_{(2)},\ldots,I_{(6)}I(2)​,…,I(6)​
对 two-adjoint-slot tensor：
IAB=∇−(XAXB).\mathcal I^{AB}
=
\nabla_-(X^AX^B).IAB=∇−​(XAXB).
由于 XXX even：
I(N)AB=∑r+s=Nr,s≥1D− ⁣(X(r)AX(s)B)+∑t+r+s=Nt,r,s≥1([Γ(t)−,X(r)]AX(s)B+X(r)A[Γ(t)−,X(s)]B).\boxed{
\begin{aligned}
I_{(N)}^{AB}
={}&
\sum_{\substack{r+s=N\\r,s\ge1}}
D_-\!\left(X_{(r)}^AX_{(s)}^B\right)
\\
&+
\sum_{\substack{t+r+s=N\\t,r,s\ge1}}
\Big(
[\Gamma_{(t)-},X_{(r)}]^A X_{(s)}^B
+
X_{(r)}^A[\Gamma_{(t)-},X_{(s)}]^B
\Big).
\end{aligned}}I(N)AB​=​r+s=Nr,s≥1​∑​D−​(X(r)A​X(s)B​)+t+r+s=Nt,r,s≥1​∑​([Γ(t)−​,X(r)​]AX(s)B​+X(r)A​[Γ(t)−​,X(s)​]B).​​
Two-loop 要求完整生成：
I(2),I(3),I(4),I(5),I(6).\boxed{
I_{(2)},I_{(3)},I_{(4)},I_{(5)},I_{(6)}.
}I(2)​,I(3)​,I(4)​,I(5)​,I(6)​.​
例如：
I(3)AB=D− ⁣(X(1)AX(2)B+X(2)AX(1)B)+[Γ(1)−,X(1)]AX(1)B+X(1)A[Γ(1)−,X(1)]B.\boxed{
\begin{aligned}
I_{(3)}^{AB}
={}&
D_-\!\left(
X_{(1)}^AX_{(2)}^B
+
X_{(2)}^AX_{(1)}^B
\right)
\\
&+
[\Gamma_{(1)-},X_{(1)}]^AX_{(1)}^B
+
X_{(1)}^A[\Gamma_{(1)-},X_{(1)}]^B.
\end{aligned}}I(3)AB​=​D−​(X(1)A​X(2)B​+X(2)A​X(1)B​)+[Γ(1)−​,X(1)​]AX(1)B​+X(1)A​[Γ(1)−​,X(1)​]B.​​
这正是 all-cubic “日” parent insertion 的 source AST。

3.4 EVE_VEV​ / Schwinger–Dyson insertion
从
Ξ=e−VδeV\Xi=e^{-V}\delta e^VΞ=e−VδeV
得到
Ξ=F(ad⁡V)δV,F(z)=1−e−zz.\Xi
=
F(\operatorname{ad}_V)\delta V,
\qquad
F(z)=\frac{1-e^{-z}}z.Ξ=F(adV​)δV,F(z)=z1−e−z​.
Invariant color pairing 下：
(ad⁡V)T=−ad⁡V.(\operatorname{ad}_V)^T=-\operatorname{ad}_V.(adV​)T=−adV​.
所以：
EV=F(ad⁡V)TEΞ=F(−ad⁡V)EΞ=ead⁡V−1ad⁡VEΞ.\boxed{
E_V
=
F(\operatorname{ad}_V)^TE_\Xi
=
F(-\operatorname{ad}_V)E_\Xi
=
\frac{e^{\operatorname{ad}_V}-1}
{\operatorname{ad}_V}E_\Xi.
}EV​=F(adV​)TEΞ​=F(−adV​)EΞ​=adV​eadV​−1​EΞ​.​
即：
EV=∑n≥01(n+1)!ad⁡VnEΞ.\boxed{
E_V
=
\sum_{n\ge0}
\frac1{(n+1)!}
\operatorname{ad}_V^nE_\Xi.
}EV​=n≥0∑​(n+1)!1​adVn​EΞ​.​
对于 two-loop S6S_6S6​ cutting，需要 EVE_VEV​ 至 quantum-VVV degree 555。
其 root
EΞgauge=δ⃗SgaugeδΞE_\Xi^{\rm gauge}
=
\frac{\vec\delta S_{\rm gauge}}{\delta\Xi}EΞgauge​=δΞδSgauge​​
必须重新由 verified main action differentiation 生成；不得从 one-loop proposal branch 复制。

4. FP/NK、gauge fixing 和 counterterms
4.1 “Pure gauge” 必须拆成两个层次
PHYSICAL_GAUGE_SECTOR:
    internal V lines
    gauge-kinetic physical vertices

GAUGE_COMPLETION:
    gauge-fixing
    FP ghosts
    selected NK branch
    counterterms
只计算第一层可以称为 “physical-V contribution”，但通常不能单独称为 gauge-invariant two-loop anomaly。
另外，N=4\mathcal N=4N=4 gauge EOM 含 matter current。因此 pure-VVV sector 不自动对：


full N=4\mathcal N=4N=4 EOM；


operator mixing；


renormalized ∇−\nabla_-∇−​-cohomology


闭合。这是本项目最大的 scope caveat 之一。

4.2 Ghost-valence equation
一个 FP vertex 有：


one ghost；


one antighost；


rrr 个 quantum-VVV ports。


它的 total valence 是
nFP=r+2,n_{\rm FP}=r+2,nFP​=r+2,
所以对 loop equation 的贡献是
nFP−2=r.n_{\rm FP}-2=r.nFP​−2=r.
完整 two-loop equation 变成
(nI−2)+∑phys(nv−2)+∑FPrv+∑NK(nv−2)=4.\boxed{
(n_I-2)
+
\sum_{\rm phys}(n_v-2)
+
\sum_{\rm FP}r_v
+
\sum_{\rm NK}(n_v-2)
=
4.
}(nI​−2)+phys∑​(nv​−2)+FP∑​rv​+NK∑​(nv​−2)=4.​
然后必须：


saturate all ghost ports into oriented closed cycles；


apply one minus sign per closed odd cycle；


verify connectedness；


verify L=2L=2L=2。


Primitive one-loop XXXXXX ghost absence 不能推广到此处。
Verified main 的 FP/NK realization 是 branch-selected；BV–NK fields 只存在于指定 branch，其他 branch 中 RNKBV=∅\mathscr R_{\rm NK}^{\rm BV}=\varnothingRNKBV​=∅。 因此 two-loop compiler 必须把 NK_branch_id 作为 immutable notation datum，而不能写一个 universal NK graph list。

4.3 Counterterm grading
给每个 counterterm vertex 一个 loop grade：
ℓct(v)∈Z≥1.\ell_{\rm ct}(v)\in\mathbb Z_{\ge1}.ℓct​(v)∈Z≥1​.
总 perturbative order：
Ltotal=Lgeometric+∑vℓct(v)+ℓct(I).\boxed{
L_{\rm total}
=
L_{\rm geometric}
+
\sum_{v}\ell_{\rm ct}(v)
+
\ell_{\rm ct}(I).
}Ltotal​=Lgeometric​+v∑​ℓct​(v)+ℓct​(I).​
At total order two，必须包括：
Bare two-loop
Lgeometric=2,∑ℓct=0.L_{\rm geometric}=2,
\qquad
\sum\ell_{\rm ct}=0.Lgeometric​=2,∑ℓct​=0.
One-loop graph with one one-loop counterterm
Lgeometric=1,∑ℓct=1.L_{\rm geometric}=1,
\qquad
\sum\ell_{\rm ct}=1.Lgeometric​=1,∑ℓct​=1.
Counterterms 可替换或插入：
δ(1)KV,δ(1)S3,δ(1)S4,δ(1)I2,δ(1)I3,δ(1)I4,\delta^{(1)}K_V,
\quad
\delta^{(1)}S_3,
\quad
\delta^{(1)}S_4,
\quad
\delta^{(1)}I_2,
\quad
\delta^{(1)}I_3,
\quad
\delta^{(1)}I_4,δ(1)KV​,δ(1)S3​,δ(1)S4​,δ(1)I2​,δ(1)I3​,δ(1)I4​,
以及 FP/NK/gauge-fixing counterterms。
Tree graph with two-loop local counterterm
Lgeometric=0,∑ℓct=2.L_{\rm geometric}=0,
\qquad
\sum\ell_{\rm ct}=2.Lgeometric​=0,∑ℓct​=2.
包含：
δ(2)I,δ(2)S,δ(1)I δ(1)S,\delta^{(2)}I,
\qquad
\delta^{(2)}S,
\qquad
\delta^{(1)}I\,\delta^{(1)}S,δ(2)I,δ(2)S,δ(1)Iδ(1)S,
及 external-field renormalization，取决于所定义的是 amputated bare、1PI renormalized 还是 LSZ-normalized form factor。
Counterterm graphs 不是 Schwinger–Dyson descendants，必须使用独立 family ID。

5. Canonical two-loop momentum routing
5.1 Oriented incidence matrix
顶点顺序：
(vI,vC,vW~,vW).(v_I,v_C,v_{\widetilde W},v_W).(vI​,vC​,vW​,vW​).
边顺序：
(e0,e1,e2,e3,e4).(e_0,e_1,e_2,e_3,e_4).(e0​,e1​,e2​,e3​,e4​).
Orientations：
e0:vI→vC,e1:vI→vW~,e2:vW~→vC,e3:vI→vW,e4:vW→vC.\begin{aligned}
e_0&:v_I\to v_C,\\
e_1&:v_I\to v_{\widetilde W},\\
e_2&:v_{\widetilde W}\to v_C,\\
e_3&:v_I\to v_W,\\
e_4&:v_W\to v_C.
\end{aligned}e0​e1​e2​e3​e4​​:vI​→vC​,:vI​→vW​,:vW​→vC​,:vI​→vW​,:vW​→vC​.​
Incidence matrix：
B=(−1−10−10+10+10+10+1−100000+1−1).\boxed{
B=
\begin{pmatrix}
-1&-1&0&-1&0\\
+1&0&+1&0&+1\\
0&+1&-1&0&0\\
0&0&0&+1&-1
\end{pmatrix}.
}B=​−1+100​−10+10​0+1−10​−100+1​0+10−1​​.​
External incoming injections：
j=(−(p+q)0qp).j=
\begin{pmatrix}
-(p+q)\\
0\\
q\\
p
\end{pmatrix}.j=​−(p+q)0qp​​.
Momentum conservation：
Br+j=0.Br+j=0.Br+j=0.

5.2 Spanning tree and chords
Choose canonical spanning tree
T={e0,e2,e4},T=\{e_0,e_2,e_4\},T={e0​,e2​,e4​},
and chords
C={e1,e3}.C=\{e_1,e_3\}.C={e1​,e3​}.
Define chord momenta：
r1=k,r3=ℓ.r_1=k,
\qquad
r_3=\ell.r1​=k,r3​=ℓ.
Solving Br+j=0Br+j=0Br+j=0 gives：
r0=−(k+ℓ+p+q),r1=k,r2=k+q,r3=ℓ,r4=ℓ+p.\boxed{
\begin{aligned}
r_0&=-(k+\ell+p+q),\\
r_1&=k,\\
r_2&=k+q,\\
r_3&=\ell,\\
r_4&=\ell+p.
\end{aligned}}r0​r1​r2​r3​r4​​=−(k+ℓ+p+q),=k,=k+q,=ℓ,=ℓ+p.​​
Checks：
−r0−r1−r3−(p+q)=0,-r_0-r_1-r_3-(p+q)=0,−r0​−r1​−r3​−(p+q)=0,
r0+r2+r4=0,r_0+r_2+r_4=0,r0​+r2​+r4​=0,
r1−r2+q=0,r_1-r_2+q=0,r1​−r2​+q=0,
r3−r4+p=0.r_3-r_4+p=0.r3​−r4​+p=0.
Canonical denominator：
D\日=(k+ℓ+p+q)2 k2 (k+q)2 ℓ2 (ℓ+p)2.\boxed{
\mathcal D_{\日}
=
(k+\ell+p+q)^2
\,k^2
\,(k+q)^2
\,\ell^2
\,(\ell+p)^2.
}D\日​=(k+ℓ+p+q)2k2(k+q)2ℓ2(ℓ+p)2.​

5.3 Automorphism 与 symmetry factor
Primary graph coefficient 必须定义为 labeled Wick-pairing sum：
CΓ=∑P:Can⁡(P)=Γ(−1)κ(P)+Nodd cycles(P)∏nNn! CI(P)∏vCv(P)∏eCe(P).\boxed{
C_\Gamma
=
\sum_{P:\operatorname{Can}(P)=\Gamma}
\frac{
(-1)^{\kappa(P)+N_{\rm odd\,cycles}(P)}
}{
\prod_nN_n!
}
\,
C_I(P)
\prod_vC_v(P)
\prod_eC_e(P).
}CΓ​=P:Can(P)=Γ∑​∏n​Nn​!(−1)κ(P)+Noddcycles​(P)​CI​(P)v∏​Cv​(P)e∏​Ce​(P).​
Typed automorphism group 只作 independent audit：
∣Orb⁡lab(Γ)∣=∣Glab∣∣Aut⁡typ(Γ)∣.|\operatorname{Orb}_{\rm lab}(\Gamma)|
=
\frac{|\mathscr G_{\rm lab}|}
{|\operatorname{Aut}_{\rm typ}(\Gamma)|}.∣Orblab​(Γ)∣=∣Auttyp​(Γ)∣∣Glab​∣​.
若已经 sum over labeled pairings，再除一次
∣Aut⁡typ(Γ)∣|\operatorname{Aut}_{\rm typ}(\Gamma)|∣Auttyp​(Γ)∣
会产生 double division。

5.4 Coupling order
对于 bare physical graph：
Iint=Naction+L=Naction+2.I_{\rm int}=N_{\rm action}+L=N_{\rm action}+2.Iint​=Naction​+L=Naction​+2.
每个 physical action vertex 带 hhh，每个 VVV-propagator 带 g2g^2g2。因此 symbolic coupling power：
(g2)Naction+2hNaction=g2Naction+4g−2Naction=g4.(g^2)^{N_{\rm action}+2}h^{N_{\rm action}}
=
g^{2N_{\rm action}+4}g^{-2N_{\rm action}}
=
\boxed{g^4}.(g2)Naction​+2hNaction​=g2Naction​+4g−2Naction​=g4​.
这只是 absorbed-basis order check，不包含 numerical propagator normalization、vertex fraction 或 iii-sign。

6. Two-loop edge-tagged DDD-algebra schedule
Verified main Euclidean flat algebra是
{Da,Dˉb˙}=−2(σEm)ab˙∂m,\boxed{
\{D_a,\bar D_{\dot b}\}
=
-2(\sigma_E^m)_{a\dot b}\partial_m,
}{Da​,Dˉb˙​}=−2(σEm​)ab˙​∂m​,​
{Da,Db}={Dˉa˙,Dˉb˙}=0.\{D_a,D_b\}
=
\{\bar D_{\dot a},\bar D_{\dot b}\}
=
0.{Da​,Db​}={Dˉa˙​,Dˉb˙​}=0.
Fourier conversion 必须单独应用：
∂m⟼irm.\partial_m\longmapsto ir_m.∂m​⟼irm​.
所以 mixed pair 产生的 sign 是：
−2i(σE⋅r)ab˙,-2i(\sigma_E\cdot r)_{a\dot b},−2i(σE​⋅r)ab˙​,
除非 derivative order 已经先交换并带额外 minus。

6.1 Theta spanning tree
使用与 momentum routing 相同的 tree：
Tθ={e0,e2,e4},T_\theta=\{e_0,e_2,e_4\},Tθ​={e0​,e2​,e4​},
root：
vI.v_I.vI​.
Deterministic post-order：
vW⟶e4vC,vW~⟶e2vC,vC⟶e0vI.v_W
\stackrel{e_4}{\longrightarrow}
v_C,
\qquad
v_{\widetilde W}
\stackrel{e_2}{\longrightarrow}
v_C,
\qquad
v_C
\stackrel{e_0}{\longrightarrow}
v_I.vW​⟶e4​​vC​,vW​⟶e2​​vC​,vC​⟶e0​​vI​.
Chord theta kernels：
e1,e3e_1,\quad e_3e1​,e3​
在 root 上留下 two independent cycle delta structures，必须由 DDD-operators saturation；不得写成裸 δ4(0)2\delta^4(0)^2δ4(0)2。

6.2 Eight phases
Phase 1 — derivative-scope expansion
展开：


every DDD- or Dˉ\bar DDˉ-difference；


every graded Leibniz branch；


D−D_-D−​ placement；


nonlinear X(n)X_{(n)}X(n)​ branches；


chiral/antichiral projector scopes。


Termination count：
M1=Nunexpanded scopes.M_1=N_{\rm unexpanded\ scopes}.M1​=Nunexpanded scopes​.

Phase 2 — endpoint canonicalization
每条 edge 选择 canonical endpoint，例如 tail endpoint。
只允许：
Dnoncan(r)Δe⟶−Dcan(−r)Δe,D_{\rm noncan}(r)\Delta_e
\longrightarrow
-D_{\rm can}(-r)\Delta_e,Dnoncan​(r)Δe​⟶−Dcan​(−r)Δe​,
Dˉnoncan(r)Δe⟶−Dˉcan(−r)Δe.\bar D_{\rm noncan}(r)\Delta_e
\longrightarrow
-\bar D_{\rm can}(-r)\Delta_e.Dˉnoncan​(r)Δe​⟶−Dˉcan​(−r)Δe​.
禁止 reverse rule。
M2=Nderivatives on noncanonical endpoints.M_2
=
N_{\rm derivatives\ on\ noncanonical\ endpoints}.M2​=Nderivatives on noncanonical endpoints​.

Phase 3 — pivoted superspace IBP
对于 ordered factors F1⋯FnF_1\cdots F_nF1​⋯Fn​：
0=∑j(−1)Pj∫F1⋯(DFj)⋯Fn,0
=
\sum_j
(-1)^{P_j}
\int
F_1\cdots(DF_j)\cdots F_n,0=j∑​(−1)Pj​∫F1​⋯(DFj​)⋯Fn​,
Pj=∑k<j∣Fk∣.P_j=\sum_{k<j}|F_k|.Pj​=k<j∑​∣Fk​∣.
若 source 是 sss：
Ts=−∑j≠s(−1)Pj+PsTj.\boxed{
T_s
=
-\sum_{j\ne s}
(-1)^{P_j+P_s}T_j.
}Ts​=−j=s∑​(−1)Pj​+Ps​Tj​.​
每个 theta point 固定一个 pivot；derivative 只允许离开 active pivot 一次，不能反向 IBP。
M3=Nderivatives on active pivots.M_3=N_{\rm derivatives\ on\ active\ pivots}.M3​=Nderivatives on active pivots​.

Phase 4 — primitive D,DˉD,\bar DD,Dˉ normal order
固定：
D−<D+<Dˉ−˙<Dˉ+˙.D_-<D_+<\bar D_{\dot-}<\bar D_{\dot+}.D−​<D+​<Dˉ−˙​​<Dˉ+˙​​.
Rules：
DbDa⟶−DaDb(b>a),D_bD_a\longrightarrow-D_aD_b
\quad (b>a),Db​Da​⟶−Da​Db​(b>a),
DaDa⟶0,Dˉa˙Dˉa˙⟶0,D_aD_a\longrightarrow0,
\qquad
\bar D_{\dot a}\bar D_{\dot a}\longrightarrow0,Da​Da​⟶0,Dˉa˙​Dˉa˙​⟶0,
Dˉb˙Da⟶−DaDˉb˙−2(σEm)ab˙∂m.\boxed{
\bar D_{\dot b}D_a
\longrightarrow
-D_a\bar D_{\dot b}
-2(\sigma_E^m)_{a\dot b}\partial_m.
}Dˉb˙​Da​⟶−Da​Dˉb˙​−2(σEm​)ab˙​∂m​.​
Measure：
M4=(Noperator inversions,ND+NDˉ).M_4=
\left(
N_{\rm operator\ inversions},
N_D+N_{\bar D}
\right).M4​=(Noperator inversions​,ND​+NDˉ​).

Phase 5 — projector reduction
Coordinate-space identities：
D2Dˉ2D2⟶16□D2,D^2\bar D^2D^2
\longrightarrow
16\Box D^2,D2Dˉ2D2⟶16□D2,
Dˉ2D2Dˉ2⟶16□Dˉ2.\bar D^2D^2\bar D^2
\longrightarrow
16\Box\bar D^2.Dˉ2D2Dˉ2⟶16□Dˉ2.
□→−p2\Box\to-p^2□→−p2 的 Fourier sign 必须来自 notation schema，而不是 baked into rewrite rule。

Phase 6 — chirality
只在 derivative 已 structurally attached 到 external field 后应用：
Dˉa˙Wb=0,Dˉa˙Φ=0,\bar D_{\dot a}W_b=0,
\qquad
\bar D_{\dot a}\Phi=0,Dˉa˙​Wb​=0,Dˉa˙​Φ=0,
DaW~b˙=0,DaΦ~=0.D_a\widetilde W_{\dot b}=0,
\qquad
D_a\widetilde\Phi=0.Da​Wb˙​=0,Da​Φ=0.
“未来可能 IBP 到 chiral field” 不能作为提前置零的理由。

Phase 7 — Grassmann saturation
Tree theta points 按 post-order 消除。最终 closed-loop identities 由 exact Grassmann oracle 验证，例如：
[D2Dˉ2δ4(θ)]θ=0=16.\left[
D^2\bar D^2\delta^4(\theta)
\right]_{\theta=0}
=16.[D2Dˉ2δ4(θ)]θ=0​=16.
Two-loop oracle 必须使用 polynomial momentum entries：
Mat⁡16(Q(i)[p++˙,p+−˙,p−+˙,p−−˙]),\operatorname{Mat}_{16}
\left(
\mathbb Q(i)
[p_{+\dot+},p_{+\dot-},p_{-\dot+},p_{-\dot-}]
\right),Mat16​(Q(i)[p++˙​​,p+−˙​​,p−+˙​​,p−−˙​​]),
不能只测试有限个 numerical momenta。

Phase 8 — typed edge collapse
只有当同一 edge 上出现 matching pair：
KeGeK_eG_eKe​Ge​
时才 collapse。
Vector edge：
KVGV=1full superspace.K_VG_V=\mathbf1_{\rm full\ superspace}.KV​GV​=1full superspace​.
Chiral matter edge 一般只给 projector：
HΦΦ~GΦ~Φ=Πchiral.H_{\Phi\widetilde\Phi}G_{\widetilde\Phi\Phi}
=
\Pi_{\rm chiral}.HΦΦ​GΦΦ​=Πchiral​.
Collapse 必须 emit child GraphIR，并记录：
parent_graph_id
parent_DWord_id
cut_edge_id
kinetic_kernel_id
propagator_kernel_id
result_projector

6.3 Two-loop critical pairs
必须逐个做 joinability test：
Critical pairRequired equalitycentral-edge endpoint transfer / left-loop reduction两条 path 的 momentum-reversed NF 相同central-edge endpoint transfer / right-loop reduction同上two mixed anticommutators sharing one DDDoperator provenance 不丢失projector macro / primitive DDˉD\bar DDDˉ reordering都得到相同 16□D216\Box D^216□D2 formcollapse eie_iei​ then eje_jej​ / reverse order若 cuts compatible，child common NF 相同central-edge collapse / theta-tree eliminationre-rooted theta tree 给同一 childchirality / mixed anticommutator必须先 mixed normalization，再 chiralityforest contraction / DDD-collapsecounterterm subgraph ancestry 保持loop rerouting / endpoint momentum reversalaffine routing certificate 相容external derivative token / EOM projectiontoken 先保留，再进入 cohomology phase
全局 termination measure：
M=(M1,M2,M3,Ninversions,Nprojector redex,Nθ≠θI,Ncuttable pairs,∣E∣,∣V∣)\boxed{
M=
\left(
M_1,M_2,M_3,
N_{\rm inversions},
N_{\rm projector\ redex},
N_{\theta\ne\theta_I},
N_{\rm cuttable\ pairs},
|E|,
|V|
\right)
}M=(M1​,M2​,M3​,Ninversions​,Nprojector redex​,Nθ=θI​​,Ncuttable pairs​,∣E∣,∣V∣)​
lexicographically，并通过 phase barriers 禁止前一 phase 的规则重新生成。

7. DRED at two loops
7.1 Metric typing
δ(4)mn=δ^mn+δ~mn,\boxed{
\delta_{(4)}^{mn}
=
\widehat\delta^{mn}
+
\widetilde\delta^{mn},
}δ(4)mn​=δmn+δmn,​
δ^mm=d=4−2ϵ,δ~mm=2ϵ.\widehat\delta_m{}^m=d=4-2\epsilon,
\qquad
\widetilde\delta_m{}^m=2\epsilon.δm​m=d=4−2ϵ,δm​m=2ϵ.
要求：
VECTOR4
VECTOR_HAT
VECTOR_TILDE
是三个不同 index types。


spinor/DDD-algebra 只产生 VECTOR4；


loop tensor integration 只产生 VECTOR_HAT；


两者相减后才允许产生 VECTOR_TILDE。


External and loop momenta：
δ~mnpn=δ~mnqn=δ~mnkn=δ~mnℓn=0.\widetilde\delta^m{}_np^n
=
\widetilde\delta^m{}_nq^n
=
\widetilde\delta^m{}_nk^n
=
\widetilde\delta^m{}_n\ell^n
=0.δmn​pn=δmn​qn=δmn​kn=δmn​ℓn=0.

7.2 Tensor reduction
Rank two：
∫kmknF=A δ^mn+∑u,v∈{p,q}Buv umvn.\boxed{
\int k^mk^nF
=
A\,\widehat\delta^{mn}
+
\sum_{u,v\in\{p,q\}}
B_{uv}\,u^mv^n.
}∫kmknF=Aδmn+u,v∈{p,q}∑​Buv​umvn.​
Mixed rank two：
∫kmℓnF=C δ^mn+∑u,v∈{p,q}Duv umvn.\int k^m\ell^nF
=
C\,\widehat\delta^{mn}
+
\sum_{u,v\in\{p,q\}}
D_{uv}\,u^mv^n.∫kmℓnF=Cδmn+u,v∈{p,q}∑​Duv​umvn.
Rank four：
∫kmknℓrℓsF=A1δ^mnδ^rs+A2δ^mrδ^ns+A3δ^msδ^nr+terms containing external momenta.\begin{aligned}
\int k^mk^n\ell^r\ell^sF
={}&
A_1\widehat\delta^{mn}\widehat\delta^{rs}
+A_2\widehat\delta^{mr}\widehat\delta^{ns}
+A_3\widehat\delta^{ms}\widehat\delta^{nr}
\\
&+\text{terms containing external momenta}.
\end{aligned}∫kmknℓrℓsF=​A1​δmnδrs+A2​δmrδns+A3​δmsδnr+terms containing external momenta.​

7.3 Evanescent numerator 的唯一合法来源
Bare DDD-algebra numerator 中禁止出现手写 ϵ\epsilonϵ。
Evanescent structures 只能在 independently compiled terms 相加后出现，例如：
δ^mn−δ(4)mn=−δ~mn.\widehat\delta^{mn}
-
\delta_{(4)}^{mn}
=
-\widetilde\delta^{mn}.δmn−δ(4)mn​=−δmn.
At rank four：
δ^mnδ^rs−δ(4)mnδ(4)rs=−δ~mnδ(4)rs−δ^mnδ~rs.\boxed{
\widehat\delta^{mn}\widehat\delta^{rs}
-
\delta_{(4)}^{mn}\delta_{(4)}^{rs}
=
-\widetilde\delta^{mn}\delta_{(4)}^{rs}
-\widehat\delta^{mn}\widetilde\delta^{rs}.
}δmnδrs−δ(4)mn​δ(4)rs​=−δmnδ(4)rs​−δmnδrs.​
右侧自动包含 single- 和 double-evanescent sectors。
Two-loop finite contributions 可来自：
δ~×1ϵ,\widetilde\delta\times\frac1\epsilon,δ×ϵ1​,
或
δ~ δ~×1ϵ2.\widetilde\delta\,\widetilde\delta
\times
\frac1{\epsilon^2}.δδ×ϵ21​.
Single δ~\widetilde\deltaδ 乘 1/ϵ21/\epsilon^21/ϵ2 会先产生 residual 1/ϵ1/\epsilon1/ϵ，必须由 forest subtraction/counterterms 处理；不能直接称为 anomaly。

8. UV subdivergences and RRR-operation
8.1 Off-shell domain
必须先工作在：
p2>0,q2>0,(p+q)2>0.\boxed{
p^2>0,\qquad
q^2>0,\qquad
(p+q)^2>0.
}p2>0,q2>0,(p+q)2>0.​
禁止在 subtraction 前设置：
p=0,q=0,p+q=0.p=0,\quad q=0,\quad p+q=0.p=0,q=0,p+q=0.
否则：
0DRED=1ϵUV−1ϵIR0_{\rm DRED}
=
\frac1{\epsilon_{\rm UV}}
-
\frac1{\epsilon_{\rm IR}}0DRED​=ϵUV​1​−ϵIR​1​
会伪装成 UV cancellation。

8.2 Forest formula
定义 KKK 为 chosen DR‾\overline{\mathrm{DR}}DR pole projector。
Proper-subgraph subtraction：
RˉΓ=Γ+∑F∈Fproper(Γ)F≠∅[∏γ∈FC(γ)]Γ/F,\boxed{
\bar R\Gamma
=
\Gamma
+
\sum_{\substack{
F\in\mathcal F_{\rm proper}(\Gamma)\\
F\ne\varnothing
}}
\left[
\prod_{\gamma\in F}
C(\gamma)
\right]
\Gamma/F,
}RˉΓ=Γ+F∈Fproper​(Γ)F=∅​∑​​γ∈F∏​C(γ)​Γ/F,​
其中
C(γ)=−K Rˉγ.\boxed{
C(\gamma)
=
-K\,\bar R\gamma.
}C(γ)=−KRˉγ.​
Full renormalized graph：
RΓ=(1−K)RˉΓ.\boxed{
R\Gamma
=
(1-K)\bar R\Gamma.
}RΓ=(1−K)RˉΓ.​

8.3 “日” graph 的 overlapping one-loop subgraphs
定义：
γL={vI,vC,vW~;e0,e1,e2},\gamma_L
=
\{v_I,v_C,v_{\widetilde W};e_0,e_1,e_2\},γL​={vI​,vC​,vW​;e0​,e1​,e2​},
γR={vI,vC,vW;e0,e3,e4}.\gamma_R
=
\{v_I,v_C,v_W;e_0,e_3,e_4\}.γR​={vI​,vC​,vW​;e0​,e3​,e4​}.
两者各自满足：
I=3,V=3,L=1.I=3,\qquad V=3,\qquad L=1.I=3,V=3,L=1.
它们共享：
{vI,vC,e0},\{v_I,v_C,e_0\},{vI​,vC​,e0​},
因此：
γL⊄γR,γR⊄γL,\gamma_L\not\subset\gamma_R,
\qquad
\gamma_R\not\subset\gamma_L,γL​⊂γR​,γR​⊂γL​,
且并非 disjoint。
所以不存在 forest：
{γL,γR}∉F(Γ\日).\boxed{
\{\gamma_L,\gamma_R\}
\notin
\mathcal F(\Gamma_{\日}).
}{γL​,γR​}∈/F(Γ\日​).​
Allowed forests 至少包括：
∅,{γL},{γR}.\varnothing,
\qquad
\{\gamma_L\},
\qquad
\{\gamma_R\}.∅,{γL​},{γR​}.
每个 candidate subgraph 是否真的 superficially divergent，仍须由 its compiled numerator 和 operator dimension 判定。

8.4 Operator versus action subdivergences
含 insertion vertex 的 divergent subgraph产生：
composite-operator counterterm.\text{composite-operator counterterm}.composite-operator counterterm.
不含 insertion 的 divergent subgraph产生：
action/field/coupling counterterm.\text{action/field/coupling counterterm}.action/field/coupling counterterm.
两者不可放进同一个 undifferentiated counterterm type。

8.5 Double and single poles
Bare two-loop graph：
Γbare(2)=a−2ϵ2+a−1ϵ+a0+⋯ .\Gamma_{\rm bare}^{(2)}
=
\frac{a_{-2}}{\epsilon^2}
+
\frac{a_{-1}}{\epsilon}
+
a_0+\cdots.Γbare(2)​=ϵ2a−2​​+ϵa−1​​+a0​+⋯.
Rˉ\bar RRˉ 后：
RˉΓ=b−1ϵ+b0+⋯ .\bar R\Gamma
=
\frac{b_{-1}}{\epsilon}
+b_0+\cdots.RˉΓ=ϵb−1​​+b0​+⋯.


a−2a_{-2}a−2​ 主要由 one-loop subdivergence products 产生；


b−1b_{-1}b−1​ 是 subdivergence-subtracted overall pole；


primitive two-loop local term 只能从 RˉΓ\bar R\GammaRˉΓ 分析；


anomaly candidate 只能从完整 RRR-renormalized SD orbit 的 finite evanescent remainder 分析。



9. Integral families and IBP certificate
9.1 Canonical five-denominator family
设：
P=p+q,P=p+q,P=p+q,
D0=(k+ℓ+P)2,D1=k2,D2=(k+q)2,D3=ℓ2,D4=(ℓ+p)2.\boxed{
\begin{aligned}
D_0&=(k+\ell+P)^2,\\
D_1&=k^2,\\
D_2&=(k+q)^2,\\
D_3&=\ell^2,\\
D_4&=(\ell+p)^2.
\end{aligned}}D0​D1​D2​D3​D4​​=(k+ℓ+P)2,=k2,=(k+q)2,=ℓ2,=(ℓ+p)2.​​
定义：
Jν[N]=μ4ϵ∫ddk ddℓ(2π)2dN(k,ℓ,p,q)D0ν0D1ν1D2ν2D3ν3D4ν4.\boxed{
\mathcal J_{\boldsymbol\nu}[N]
=
\mu^{4\epsilon}
\int
\frac{d^dk\,d^d\ell}{(2\pi)^{2d}}
\frac{
N(k,\ell,p,q)
}{
D_0^{\nu_0}
D_1^{\nu_1}
D_2^{\nu_2}
D_3^{\nu_3}
D_4^{\nu_4}
}.
}Jν​[N]=μ4ϵ∫(2π)2dddkddℓ​D0ν0​​D1ν1​​D2ν2​​D3ν3​​D4ν4​​N(k,ℓ,p,q)​.​
Independent loop-dependent scalar products 数：
L(L+1)2+LE=2⋅32+2⋅2=7.\frac{L(L+1)}2+LE
=
\frac{2\cdot3}{2}+2\cdot2
=
7.2L(L+1)​+LE=22⋅3​+2⋅2=7.
五个 denominators 留下 two irreducible scalar products，可取：
ρ1=k⋅p,ρ2=ℓ⋅q.\boxed{
\rho_1=k\cdot p,
\qquad
\rho_2=\ell\cdot q.
}ρ1​=k⋅p,ρ2​=ℓ⋅q.​
因此 scalar family 可写为：
Jν0⋯ν4;a,b=Jν[(k⋅p)a(ℓ⋅q)b].\mathcal J_{\nu_0\cdots\nu_4;a,b}
=
\mathcal J_{\boldsymbol\nu}
[(k\cdot p)^a(\ell\cdot q)^b].Jν0​⋯ν4​;a,b​=Jν​[(k⋅p)a(ℓ⋅q)b].

9.2 Pinches and descendants
νi=0\nu_i=0νi​=0
表示 edge eie_iei​ 被 pinched/collapsed 后的 subtopology。
这些 pinches 必须保留 parent edge provenance，不能只作为 anonymous lower-sector integral。

9.3 IBP equations
生成：
0=∫ddk ddℓ ∂∂km[vmN∏iDiνi],0
=
\int d^dk\,d^d\ell\,
\frac{\partial}{\partial k_m}
\left[
v_m
\frac{N}{\prod_iD_i^{\nu_i}}
\right],0=∫ddkddℓ∂km​∂​[vm​∏i​Diνi​​N​],
0=∫ddk ddℓ ∂∂ℓm[vmN∏iDiνi],0
=
\int d^dk\,d^d\ell\,
\frac{\partial}{\partial \ell_m}
\left[
v_m
\frac{N}{\prod_iD_i^{\nu_i}}
\right],0=∫ddkddℓ∂ℓm​∂​[vm​∏i​Diνi​​N​],
其中：
v∈{k,ℓ,p,q}.v\in\{k,\ell,p,q\}.v∈{k,ℓ,p,q}.

9.4 IBPCertificate
必须保存：
family_id
routing_hash
denominator_definitions
ISP_basis
sector_order
IBP_equation_hashes
reduction_matrix
master_integral_ids
rational_coefficients_in(d,p2,q2,P2)
boundary/scaleless assumptions
independent_check
不能仅保存最终 master = ... string。

9.5 Laurent-depth analysis
IntegralPoleCompiler 必须先计算每项的 ϵ\epsilonϵ-valuation。
若：
E(ϵ)=ϵsEs+⋯ ,E(\epsilon)
=
\epsilon^sE_s+\cdots,E(ϵ)=ϵsEs​+⋯,
而 master：
M(ϵ)=∑r=−R∞mrϵr,M(\epsilon)
=
\sum_{r=-R}^{\infty}m_r\epsilon^r,M(ϵ)=r=−R∑∞​mr​ϵr,
finite term 需要所有：
s+r=0.s+r=0.s+r=0.
At two loops：


non-evanescent double-pole sector需要 master 至 finite order；


one-loop counterterm × one-loop graph 常要求 one-loop master 至 O(ϵ)O(\epsilon)O(ϵ)；


double-evanescent × 1/ϵ21/\epsilon^21/ϵ2 需要准确保留 metric contraction 至 O(ϵ2)O(\epsilon^2)O(ϵ2)。



9.6 PoleIR
PoleIR
  graph_id
  amplitude_hash
  dword_nf_hash

  integral_family
  sector
  canonical_routing
  tensor_basis
  metric_provenance: FOUR | HAT | TILDE

  UV_degree
  IR_status
  candidate_divergent_subgraphs
  accepted_forest_set

  bare_laurent_series
  forest_counterterms
  Rbar_laurent_series
  overall_counterterm
  renormalized_series

  IBP_certificate_hash
  master_expansion_hashes
  scheme_id

10. Complete two-loop Schwinger–Dyson orbit
10.1 Parent families
完整 parent pool 至少包含 §2 的十二类：
I2S34,…,I6.I_2S_3^4,\ldots,I_6.I2​S34​,…,I6​.
“日” subset 包含：
I3S33I_3S_3^3I3​S33​
和
I2S32S4I_2S_3^2S_4I2​S32​S4​
中 canonicalize 到 K4∖eK_4\setminus eK4​∖e 的 graphs。

10.2 Edge collapses
每个 Γ\日\Gamma_{\日}Γ\日​ 有五个 tagged cuts：
Cut⁡eiΓ\日,i=0,…,4.\operatorname{Cut}_{e_i}\Gamma_{\日},
\qquad
i=0,\ldots,4.Cutei​​Γ\日​,i=0,…,4.
重要修正：
ordinary edge contraction preserves loop rank.\boxed{
\text{ordinary edge contraction preserves loop rank}.
}ordinary edge contraction preserves loop rank.​
因为：
I′ ⁣=I−1,V′ ⁣=V−1,I'\!=I-1,\qquad
V'\!=V-1,I′=I−1,V′=V−1,
所以：
L′=(I−1)−(V−1)+1=L=2.L'
=
(I-1)-(V-1)+1
=
L
=
2.L′=(I−1)−(V−1)+1=L=2.
特别地，central edge e0e_0e0​ collapse 后：


vIv_IvI​ 和 vCv_CvC​ fuse；


e1,e2e_1,e_2e1​,e2​ 变成一对 parallel edges；


e3,e4e_3,e_4e3​,e4​ 变成另一对 parallel edges；


得到 two-loop figure-eight/double-bubble child：
V′=3,I′=4,L′=2.V'=3,\qquad I'=4,\qquad L'=2.V′=3,I′=4,L′=2.
因此任何 test 写成 “central collapse gives L=1L=1L=1” 都是错误的。

10.3 Explicit SD basis
Explicit physical basis 包含：


nonlinear I3,I4,I5,I6I_3,I_4,I_5,I_6I3​,I4​,I5​,I6​ insertion graphs；


quartic/quintic/sextic action graphs；


I2S32S4I_2S_3^2S_4I2​S32​S4​ seagull realizations；


I2S42I_2S_4^2I2​S42​、I3S3S4I_3S_3S_4I3​S3​S4​、I4S32I_4S_3^2I4​S32​ bubble/double-bubble families；


gauge-fixing/FP/NK descendants；


EOM insertion graphs；


scaleless candidates，在 individual routing 检查后分类；


one-loop counterterm insertions。



10.4 Collapsed/cut basis
Cut basis 由：
KeGeK_eG_eKe​Ge​
对 parent edge 的作用生成。
它是同一 SD orbit 的另一组 representatives，不是另一组额外 amplitude。

10.5 Quotient-space equality
Raw explicit graph 数量和 cut representatives 数量通常不同，不能要求 naive set bijection。
定义 common contact normal-form space NSD\mathcal N_{\rm SD}NSD​：
ME:KNE→NSD,M_E:
\mathbb K^{N_E}\to\mathcal N_{\rm SD},ME​:KNE​→NSD​,
MC:KNC→NSD.M_C:
\mathbb K^{N_C}\to\mathcal N_{\rm SD}.MC​:KNC​→NSD​.
令 cE,cCc_E,c_CcE​,cC​ 是 exact coefficient vectors。Required proof：
MEcE=MCcC.\boxed{
M_Ec_E=M_Cc_C.
}ME​cE​=MC​cC​.​
同时保存：
ker⁡ME,ker⁡MC,rank⁡ME,rank⁡MC.\ker M_E,
\qquad
\ker M_C,
\qquad
\operatorname{rank}M_E,
\qquad
\operatorname{rank}M_C.kerME​,kerMC​,rankME​,rankMC​.
只有当两个 matrices square 且 invertible 时，才可称为 literal bijection。

10.6 Double-counting prohibition
选择：
counting_basis = EXPLICIT
则：
ASD=∑χ∈BexplicitAχ.\mathcal A_{\rm SD}
=
\sum_{\chi\in\mathcal B_{\rm explicit}}
\mathcal A_\chi.ASD​=χ∈Bexplicit​∑​Aχ​.
Cut basis 只作为 proof witness。
或者选择：
counting_basis = COLLAPSED
则只 sum cut basis。
绝不允许：
∑explicitAχ+∑cutAη.\sum_{\rm explicit}\mathcal A_\chi
+
\sum_{\rm cut}\mathcal A_\eta.explicit∑​Aχ​+cut∑​Aη​.

10.7 Ordinary cancellation 的正确 proof target
在 forest subtraction 后，定义：
SSD(2)=∑Γ∈OSD(2)RDR‾AΓ.\boxed{
\mathcal S_{\rm SD}^{(2)}
=
\sum_{\Gamma\in\mathfrak O_{\rm SD}^{(2)}}
R_{\overline{\rm DR}}\mathcal A_\Gamma.
}SSD(2)​=Γ∈OSD(2)​∑​RDR​AΓ​.​
将其分解为：
SSD(2)=Sordinary+Sevanescent+SEOM+Stotal deriv.+Sscheme.\mathcal S_{\rm SD}^{(2)}
=
\mathcal S_{\rm ordinary}
+
\mathcal S_{\rm evanescent}
+
\mathcal S_{\rm EOM}
+
\mathcal S_{\rm total\ deriv.}
+
\mathcal S_{\rm scheme}.SSD(2)​=Sordinary​+Sevanescent​+SEOM​+Stotal deriv.​+Sscheme​.
Required equality：
Sordinary=0\boxed{
\mathcal S_{\rm ordinary}=0
}Sordinary​=0​
必须由 explicit graph/counterterm sum 证明。
只有随后才定义：
Acandidate(2)=Fin⁡ϵ→0ΠH∇−Sevanescent.\boxed{
\mathcal A_{\rm candidate}^{(2)}
=
\operatorname{Fin}_{\epsilon\to0}
\Pi_{H_{\nabla_-}}
\mathcal S_{\rm evanescent}.
}Acandidate(2)​=Finϵ→0​ΠH∇−​​​Sevanescent​.​
这一步不能借用 twist answer。

11. IR extensions and staged acceptance
11.1 GraphIR extensions
TwoLoopGraphIR
  notation_hash
  source_AST_hashes
  graph_id
  graph_family
  source_family: RI_CUBIC | RI_SEAGULL | ...

  vertices
  typed_ports
  internal_edges
  external_legs

  incidence_matrix
  momentum_spanning_tree
  momentum_chords
  theta_spanning_tree
  theta_chords
  loop_basis

  exact_labeled_pairing_weight
  automorphism_certificate
  external_extraction_certificate

  candidate_UV_subgraphs
  SD_orbit_id
  basis_role: EXPLICIT | CUT_WITNESS
  counterterm_grade

11.2 AmplitudeIR extensions
TwoLoopAmplitudeIR
  graph_hash
  exact_factor_ledger
  hbar_grade
  coupling_grade

  canonical_routing
  routing_solution_certificate
  overall_momentum_delta

  denominator_family
  theta_kernel_product
  color_tensor_AST
  spinor_tensor_AST
  flavor_tensor_AST

  initial_DWordIR

11.3 DWordIR extensions
TwoLoopDWordIR
  amplitude_hash
  exact_coefficient

  theta_point_graph
  ordered_factors
  edge_endpoint_derivatives
  vector_derivative_tokens
  external_derivative_tokens

  projector_tokens
  cut_tokens
  cut_ancestry
  forest_context

  rewrite_trace
  deterministic_normal_form

11.4 Additional proof IRs
ForestIR
IBPCertificateIR
SDOrbitProofIR
CountertermIR
MetricProvenanceIR
ExternalTargetLedger

11.5 Acceptance gates
Gate T0 — Authority lock


all source equations from verified main；


external target files inaccessible to derivation compiler；


notation hash frozen。


Gate T1 — AST completion
Generate exactly：
Γ,Γ~,W,W~,Xthrough degree 5,\Gamma,\widetilde\Gamma,W,\widetilde W,X
\quad\text{through degree }5,Γ,Γ,W,W,Xthrough degree 5,
I2,…,I6,I_2,\ldots,I_6,I2​,…,I6​,
S2,…,S6,S_2,\ldots,S_6,S2​,…,S6​,
and FP/NK vertices required by the selected branch。
Gate T2 — Exhaustive census


all twelve bare source families；


every quantum port saturated；


connected；


L=2L=2L=2；


no ValenceRequest cast to graph。


Gate T3 — “日” topology
Verify：
V=4,I=5,L=2,V=4,\qquad I=5,\qquad L=2,V=4,I=5,L=2,
degree multiset：
[3,3,2,2],[3,3,2,2],[3,3,2,2],
incidence matrix rank：
rank⁡B=V−1=3.\operatorname{rank}B=V-1=3.rankB=V−1=3.
Gate T4 — Canonical amplitude
Verify routing：
(r0,…,r4)=(−(k+ℓ+p+q),k,k+q,ℓ,ℓ+p).(r_0,\ldots,r_4)
=
(-(k+\ell+p+q),k,k+q,\ell,\ell+p).(r0​,…,r4​)=(−(k+ℓ+p+q),k,k+q,ℓ,ℓ+p).
No handwritten numerator field exists。
Gate T5 — Two-loop DDD-algebra


local confluence；


termination；


polynomial 16×1616\times1616×16 oracle；


central-edge critical pairs；


external tokens preserved。


Gate T6 — RRR-operation and IBP


overlapping γL,γR\gamma_L,\gamma_RγL​,γR​ never appear in same forest；


all subdivergences subtracted；


master reduction certificate；


nonexceptional IR status。


Gate T7 — SD quotient equality
MEcE=MCcC.M_Ec_E=M_Cc_C.ME​cE​=MC​cC​.
No explicit/cut double counting。
Gate T8 — anomaly/cohomology projection
Only after T0–T7：
Fin⁡ϵ→0ΠH∇−∑ΓRAΓ.\operatorname{Fin}_{\epsilon\to0}
\Pi_{H_{\nabla_-}}
\sum_\Gamma R\mathcal A_\Gamma.Finϵ→0​ΠH∇−​​​Γ∑​RAΓ​.
Gate T9 — external comparison
Euclidean result is compared to twist ledger without allowing reverse dependency。

11.6 Deterministic tests
RI-TOPOLOGY-001
I−V+1=5−4+1=2.I-V+1=5-4+1=2.I−V+1=5−4+1=2.
RI-ROUTING-001
Directly verify：
Br+j=0.Br+j=0.Br+j=0.
RI-SOURCE-FAMILIES-001
Only：
I3S33,I2S32S4I_3S_3^3,
\qquad
I_2S_3^2S_4I3​S33​,I2​S32​S4​
may canonicalize to four-vertex five-edge “日” graphs。
RI-COUPLING-001
For NNN physical action vertices：
(g2)N+2hN=g4.(g^2)^{N+2}h^N=g^4.(g2)N+2hN=g4.
RI-AUTOMORPHISM-001
Compare labeled pairing sum with orbit-stabilizer count；确认不重复除 ∣Aut⁡typ∣|\operatorname{Aut}_{\rm typ}|∣Auttyp​∣。
RI-CENTRAL-COLLAPSE-001
(V,I,L)=(4,5,2)⟶(3,4,2).(V,I,L)=(4,5,2)
\longrightarrow
(3,4,2).(V,I,L)=(4,5,2)⟶(3,4,2).
RI-FOREST-OVERLAP-001
Reject：
{γL,γR}.\{\gamma_L,\gamma_R\}.{γL​,γR​}.
RI-DRED-001
Bare DWord AST contains no symbol ϵ\epsilonϵ。
RI-METRIC-001
Loop tensor reduction cannot emit VECTOR4; DDD-algebra cannot emit VECTOR_HAT。
RI-IBP-001
Every reduction coefficient is rational in：
d,p2,q2,(p+q)2.d,p^2,q^2,(p+q)^2.d,p2,q2,(p+q)2.
RI-SD-BASIS-001
Exactly one of EXPLICIT or COLLAPSED contributes to amplitude sum。
EXTERNAL-ISOLATION-001
任何 EXTERNAL_TARGET_NOT_DERIVATION hash 出现在：
NotationSpec
ActionAST
CompositeAST
GraphIR
AmplitudeIR
DWordIR
PoleIR
中都必须 fail CI。

12. EXTERNAL TARGET LEDGER — not derivation
12.1 Bitriangle topology
EXTERNAL_TARGET_NOT_DERIVATION
K. Budzik, D. Gaiotto, J. Kulp, J. Wu, M. Yu, Feynman Diagrams in Four-Dimensional Holomorphic Theories and the Operatope, arXiv:2207.14321 / JHEP 07 (2023) 127。
该文 §4.5、Eq. (4.34)、paper page 27 把 four-vertex five-edge graph 称为 bitriangle，并称其为唯一 two-loop Laman graph。其 topology 正是 K4∖eK_4\setminus eK4​∖e。arXiv+1
其 leading universal bitriangle function 为 Eq. (4.44)：
f[λ1,λ2,λ3;0,0]=124(λ1∧(λ2+2λ3))(λ2∧(λ1+2λ3)).\boxed{
f[\lambda_1,\lambda_2,\lambda_3;0,0]
=
\frac1{24}
\Big(
\lambda_1\wedge(\lambda_2+2\lambda_3)
\Big)
\Big(
\lambda_2\wedge(\lambda_1+2\lambda_3)
\Big).
}f[λ1​,λ2​,λ3​;0,0]=241​(λ1​∧(λ2​+2λ3​))(λ2​∧(λ1​+2λ3​)).​
这是 holomorphic universal integral target，不是 Euclidean SYM coefficient。arXiv

12.2 关于 Q2(bAbB)Q_2(b^Ab^B)Q2​(bAbB) 的 citation mismatch
EXTERNAL_TARGET_NOT_DERIVATION — TARGET NOT VERIFIED AS STATED
K. Budzik et al., Semi-Chiral Operators in 4d N=1\mathcal N=1N=1 Gauge Theories, arXiv:2306.01039，明确写出：
Qn:V(n+1,0,J1,J2)⟶V(1,1,J1+n,J2+n).Q_n:
V(n+1,0,J_1,J_2)
\longrightarrow
V(1,1,J_1+n,J_2+n).Qn​:V(n+1,0,J1​,J2​)⟶V(1,1,J1​+n,J2​+n).
因此在该文 convention 中，primitive Q2Q_2Q2​ 作用于 three bbb-letters，不是 two bbb-letters。该文同时说明唯一 two-loop diagram 非零。arXiv+1
我没有核验到一条 published equation：
Q2(bAbB)=⋯ .Q_2(b^Ab^B)=\cdots.Q2​(bAbB)=⋯.
因此不能猜测或伪造该公式。

12.3 已核验到的 published Q2Q_2Q2​ example
EXTERNAL_TARGET_NOT_DERIVATION
同一文 Appendix C，Eq. (C.8)，paper page 61，给出 pure SU(2)SU(2)SU(2) bootstrap example：
Q2(bAbAbBbB)=20C123ϵABC bA∂α∂βbB ∂α∂βcC.\boxed{
Q_2
\left(
b_A b^A b_B b^B
\right)
=
\frac{20C_1^2}{3}
\epsilon_{ABC}\,
b^A
\partial_\alpha\partial_\beta b^B\,
\partial^\alpha\partial^\beta c^C.
}Q2​(bA​bAbB​bB)=320C12​​ϵABC​bA∂α​∂β​bB∂α∂βcC.​
arXiv
Source convention dictionary：
bA,cAholomorphic BF semi-chiral fieldsA,B,CSU(2) adjoint indicesϵABCSU(2) structure tensorα,β=1,2holomorphic derivative indicesC1one-loop bootstrap normalization\begin{array}{c|l}
b^A,c^A
&\text{holomorphic BF semi-chiral fields}
\\
A,B,C
&SU(2)\text{ adjoint indices}
\\
\epsilon_{ABC}
&SU(2)\text{ structure tensor}
\\
\alpha,\beta=1,2
&\text{holomorphic derivative indices}
\\
C_1
&\text{one-loop bootstrap normalization}
\end{array}bA,cAA,B,CϵABC​α,β=1,2C1​​holomorphic BF semi-chiral fieldsSU(2) adjoint indicesSU(2) structure tensorholomorphic derivative indicesone-loop bootstrap normalization​
Appendix 前一页说明，和 direct one-loop result 比较可取 C1=−2C_1=-2C1​=−2，但后续 formulas 保持 C1C_1C1​ symbolic。arXiv
这个 formula：


输入是 four bbb-letters；


是 SU(2)SU(2)SU(2) gauge-invariant composite example；


不是已核验的 open-index Q2(bAbB)Q_2(b^Ab^B)Q2​(bAbB)；


不得作为 Euclidean two-loop derivation input。



13. Strict find-gap table
Severity：
P0对象或 authority 未定义，阻塞计算开始P1阻塞任何 two-loop coefficient/anomaly claimP2不阻塞单个 symbolic seed，但阻塞 completeness/automationP3documentation/rendering/reproducibility defect\begin{array}{c|l}
P0&\text{对象或 authority 未定义，阻塞计算开始}\\
P1&\text{阻塞任何 two-loop coefficient/anomaly claim}\\
P2&\text{不阻塞单个 symbolic seed，但阻塞 completeness/automation}\\
P3&\text{documentation/rendering/reproducibility defect}
\end{array}P0P1P2P3​对象或 authority 未定义，阻塞计算开始阻塞任何 two-loop coefficient/anomaly claim不阻塞单个 symbolic seed，但阻塞 completeness/automationdocumentation/rendering/reproducibility defect​
IDLevelGapExact failure modeRequired resolutionG-DEF-01P0“日” topology 未锁定sunset、figure-eight、bitriangle 混用Commit K4_MINUS_EDGE, V=4,I=5,L=2V=4,I=5,L=2V=4,I=5,L=2G-DEF-02P0External form factor 未锁定同图可对应不同 operator tensorFreeze external probes、ordering、amputation conventionG-SCOPE-01P0“pure gauge” 含义不清physical VVV-only 与 gauge-completed sector 混淆分开 PHYSICAL_GAUGE / GAUGE_COMPLETIONG-SCOPE-02P1Pure-gauge subset 非 N=4\mathcal N=4N=4 EOM-closedmatter-current/operator mixing 被遗漏明确它只是 sector contribution；最终加入 matter orbitG-NORM-01P1Two-loop fixed-gauge propagator normalization 未由 main 重建任何 numerical prefactor 不可信从 main action/gauge choice 重新 invert HessianG-ALG-01P1Γ,W,W~,X\Gamma,W,\widetilde W,XΓ,W,W,X 未生成至 degree 5S5,S6,I5,I6S_5,S_6,I_5,I_6S5​,S6​,I5​,I6​ 缺失Exact BCH compilerG-ALG-02P1S2,…,S6S_2,\ldots,S_6S2​,…,S6​、I2,…,I6I_2,\ldots,I_6I2​,…,I6​ AST 不完整graph census 漏 familyAST round-trip identitiesG-SIGN-01P1Exponent factorial 与 Wick multiplicity 可能双计错除 Nv!N_v!Nv​! 或 automorphismLabeled-pairing primary weightG-SIGN-02P1Direct/reflected odd external ordering 未审计relative sign ambiguityExternal-word permutation certificateG-IDX-01P1Central edge derivative provenance 不完整左右 loops 的 DDD-operators 混合Edge+endpoint+momentum typed tokensG-IDX-02P1VECTOR4/HAT/TILDE 未分型非法提前识别 δ4=δ^\delta_4=\widehat\deltaδ4​=δThree distinct index typesG-OP-01P1Unrestricted IBP 不终止exact two-cyclePhase-scheduled pivoted IBPG-OP-02P1Two-loop critical pairs 未 joinresult 依 rewrite orderLocal confluence certificateG-PROJ-01P1Matter/vector cut projector 未分型KGK GKG 被错误统一成 identityTyped collapse resultG-PROJ-02P1Final ∇−\nabla_-∇−​-cohomology projection 未定义EOM/total derivative/anomaly 混合Explicit quotient basisG-THM-01P1RRR-operation 未实现subdivergence 被误当 primitive poleForestIR + R,Rˉ,KR,\bar R,KR,Rˉ,K certificatesG-THM-02P1Overlapping triangles 未编码非法 forest {γL,γR}\{\gamma_L,\gamma_R\}{γL​,γR​}Forest compatibility predicateG-THM-03P1Explicit/cut SD bases 未证明等价double counting 或 missing contactMEcE=MCcCM_Ec_E=M_Cc_CME​cE​=MC​cC​ proofG-NORM-02P1Counterterm scheme 未锁定finite evanescent term scheme-dependentFreeze DR‾\overline{\rm DR}DR and finite-CT policyG-SCOPE-03P1FP/NK branch 未锁定ghost graph census 非唯一Immutable branch ID from mainG-ALG-03P1Two-loop IBP/master reduction 缺失pole coefficient 无 certificateLaporta/IBP exact reduction + mastersG-ALG-04P2Master Laurent depth 未自动推断ϵ×1/ϵ2\epsilon\times1/\epsilon^2ϵ×1/ϵ2 finite term 丢失Valuation-driven expansion depthG-OP-03P216×1616\times1616×16 oracle 仅 numerical samplesfinite samples 非 polynomial proofPolynomial matrix oracle/interpolation certificateG-SCOPE-04P2Scaleless tadpole 直接置零风险UV/IR poles 相消被隐藏UV/IR typed status or R∗R^\astR∗G-DEF-03P2Holomorphic target 被写成 Q2(bAbB)Q_2(b^Ab^B)Q2​(bAbB)published convention 要求 Q2Q_2Q2​ primitive input length 3Resolve target operator dictionaryG-SCOPE-05P2N=1 holomorphic pure gauge 与 N=4 pure-gauge sector dictionary 未证comparison category errorExplicit twist/field/operator mapG-PROJ-03P2External-target data 可反向进入 compilercircular derivationHash-based import firewallG-SCOPE-06P3Publication renderer 未绑定 IR hash图和 amplitude 可能失配Same-hash TikZ/SVG/PDF generationG-NORM-03P3Formula provenance 未逐因子展示auditability 差Factor ledger beside each graph

Final verdict
“日” two-loop problem 在数学上没有已知 structural obstruction。\boxed{
\text{“日” two-loop problem 在数学上没有已知 structural obstruction。}
}“日” two-loop problem 在数学上没有已知 structural obstruction。​
但在以下四项完成前，不能输出 Euclidean coefficient：
1.S2…6,I2…6 从 main 完整生成;2.Γ\日 的全部 RI-CUBIC 和 RI-SEAGULL graphs 完整 census;3.R-operation + two-loop D-algebra + IBP masters;4.MEcE=MCcC 的 SD quotient proof.\boxed{
\begin{aligned}
1.&\quad
S_{2\ldots6},I_{2\ldots6}
\text{ 从 main 完整生成};
\\
2.&\quad
\Gamma_{\日}\text{ 的全部 RI-CUBIC 和 RI-SEAGULL graphs 完整 census};
\\
3.&\quad
R\text{-operation + two-loop }D\text{-algebra + IBP masters};
\\
4.&\quad
M_Ec_E=M_Cc_C
\text{ 的 SD quotient proof}.
\end{aligned}}1.2.3.4.​S2…6​,I2…6​ 从 main 完整生成;Γ\日​ 的全部 RI-CUBIC 和 RI-SEAGULL graphs 完整 census;R-operation + two-loop D-algebra + IBP masters;ME​cE​=MC​cC​ 的 SD quotient proof.​​
当前可接受的第一阶段 deliverable 应是：
一个 coefficient-symbolic、Wick-complete、五边、四顶点、 两圈的 K4∖e GraphIR family，\boxed{
\text{一个 coefficient-symbolic、Wick-complete、五边、四顶点、
两圈的 }K_4\setminus e\text{ GraphIR family，}
}一个 coefficient-symbolic、Wick-complete、五边、四顶点、 两圈的 K4​∖e GraphIR family，​
连同 exact incidence/routing、source-family proof、automorphism certificate 和 forest candidates；而不是任何预先写入的 numerator、pole 或 anomaly coefficient。
