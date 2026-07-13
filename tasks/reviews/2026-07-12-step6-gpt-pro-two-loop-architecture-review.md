# GPT Pro two-loop architecture review — raw capture

- Date: 2026-07-12 (America/Los_Angeles)
- Role: `GAP_REVIEW_ONLY_NO_FORMULA_AUTHORITY`
- Status: `PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE`
- Input boundary: the response may suggest checks, but no formula, sign, coefficient, graph count, target statement, or convention is admitted without an independent Project derivation.
- Capture: authenticated in-app ChatGPT DOM `innerText`; mathematical layout is preserved only to the extent exposed by that DOM.

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

Do not give a final Euclidean SYM coefficient unless you actually derive every factor. Distinguish proved topology identities, convention-dependent placeholders, conjectures, and external targets.

## Response

0. Status labels and authority boundary

以下标签贯穿全文：

PROVED_TOPOLOGY
MAIN_DERIVED
SYMBOLIC_PLACEHOLDER
PROOF_OBLIGATION
EXTERNAL_TARGET_NOT_DERIVATION
	​

纯图论、loop counting 或 incidence-matrix identity
仅由 verified origin/main action/conventions 推导
结构确定，但 normalization/sign 尚待 main-side compiler 输出
不得作为已证明结果
仅用于最终 comparison，禁止进入 Euclidean derivation AST
	​


Verified main 固定

h=g
−2
,c
ABC
	​

=κ
CD
	​

c
AB
	​

D
=c
[ABC]
	​

,

以及 Euclidean N=4 action 中彼此独立的 chiral gauge kinetic、antichiral gauge kinetic、matter bridge 和两套 cubic superpotential。

本回答不使用 proposal branch 的 one-loop coefficient，也不假定它的 aggregate contact identity。

1. “日” graph 的精确定义
1.1 推荐锁定的 underlying graph

把 “日” 定义为

Γ
\日
	​

:=K
4
	​

∖e
	​


即 four vertices、five internal edges、两个三角形共享一条 central edge：

                 v_I
               /  |  \
              /   |   \
       v_{\widetilde W} | v_W
              \   |   /
               \  |  /
                 v_C

顶点：

V(Γ
\日
	​

)={v
I
	​

,v
C
	​

,v
W
	​

,v
W
	​

}.

边：

e
0
	​

e
1
	​

e
2
	​

e
3
	​

e
4
	​

	​

=(v
I
	​

,v
C
	​

),
=(v
I
	​

,v
W
	​

),
=(v
W
	​

,v
C
	​

),
=(v
I
	​

,v
W
	​

),
=(v
W
	​

,v
C
	​

).
	​

central edge,
	​


Internal degree sequence：

deg
int
	​

(v
I
	​

,v
C
	​

,v
W
	​

,v
W
	​

)=(3,3,2,2).

Euler identity：

L=I
int
	​

−V+1=5−4+1=2.
	​


Half-edge identity：

v
∑
	​

val
total
	​

(v)=2I
int
	​

+E
ext
	​

.

在 two-external form factor 中：

2I
int
	​

+E
ext
	​

=2⋅5+2=12.

这就是需要锁入 schema 的 graph signature：

underlying_simple_graph = K4_MINUS_EDGE
vertices = 4
internal_edges = 5
external_legs = 2
loop_rank = 2
internal_degree_multiset = [3,3,2,2]
1.2 与其他 “two-loop” 昵称的区别
名称	V	I
int
	​

	L	是否为本项目“日”
theta / sunset	2	3	2	否
figure-eight，共享一个 vertex	3	4	2	否
K
4
	​

∖e bitriangle	4	5	2	是
literal multi-rung ladder	通常 6	通常 7	2	否
square-triangle sliding graph	5	6	2	否

外部 holomorphic 文献称同一个 K
4
	​

∖e graph 为 bitriangle，并将其画成 diamond 加 central edge；这是纯 topology correspondence，不是 coefficient correspondence。
arXiv

1.3 Provisional external probe

为了使 Euclidean form factor 可计算，需要先锁定 external probes。与 primitive w=0 seed 最接近的 provisional choice 是

F
α
˙
AB;DE
	​

(p,q)=⟨
W
α
˙
D
	​

(q)W
+
E
	​

(p)I
AB
(P)⟩
1PI
	​

,
	​

I
AB
=∇
−
	​

(X
A
X
B
),X
A
=(∇
+
	​

W
+
	​

)
A
,
P+p+q=0.

这是

SCOPE_LOCK_PROPOSAL,

不是从 topology 自动推出的。若最终 holomorphic dictionary 对应其他 external survivors，必须重新生成 GraphIR，而不是重标这张图。

1.4 同一个“日” topology 的两类 bare source realization

Two-loop、four-vertex graph 意味着有 one insertion vertex 和 three action vertices。由 §2 的 valence equation 可知，仅有：

I
(3)
	​

S
(3)
3
	​

	​


和

I
(2)
	​

S
(3)
2
	​

S
(4)
	​

	​


能够在 V=4,I=5,L=2 下 realization 成 K
4
	​

∖e。

因此必须区分：

RI-CUBIC:
    source family = I3 S3 S3 S3

RI-SEAGULL:
    source family = I2 S3 S3 S4

二者可能在 Schwinger–Dyson cut basis 中相互关联，因此不能把 “日 graph” 等同于单独的 I
3
	​

S
3
3
	​

。

对于 I
2
	​

S
3
2
	​

S
4
	​

，若 total valences 是

(2,3,3,4),

要得到 internal degrees (2,2,3,3)，external extraction 必须满足：

e
I
2
	​

	​

=0,

以及：

(e
S
4
	​

	​

,e
S
3a
	​

	​

,e
S
3b
	​

	​

)=(1,1,0)

或 permutation，或者

(2,0,0).

后一个 case 在独立 chiral/antichiral gauge-kinetic sectors 中通常会因不能由单个 gauge quartic vertex 同时承载 W 和 
W
 而成为 typed zero；该结论必须由 main-derived action AST 检查，而非 topology 推断。

1.5 全部 inequivalent variants 的正确定义

不能手写一个小整数作为 variant count。完整集合是

V
\日
	​

={ω,s,ι,σ
C
	​

,ρ
I
	​

,ρ
C
	​

,ρ
W
	​

,ρ
W
	​

,P
Wick
	​

}/Aut
typ
	​

.
	​


其中：

ω∈{DIRECT,REFLECTED}；

s∈{RI−CUBIC,RI−SEAGULL}；

ι 是具体 I
(2)
	​

 或 I
(3)
	​

 AST term；

σ
C
	​

 是 central cubic 的 chiral/antichiral sector；

ρ
v
	​

 是该 vertex 的 ordered derivative-scope branch；

P
Wick
	​

 是 complete typed Wick pairing；

quotient 只允许保持全部 vertex species、external ordering、derivative scopes、field orientations、color/flavor bindings 的 automorphisms。

Underlying undecorated K
4
	​

∖e 有

Aut(K
4
	​

∖e)=Z
2
	​

×Z
2
	​

.

但对 side-probe decorated graph：

v
I
	​


=v
C
	​

；

v
W
	​


=v
W
	​

；

所以 typed automorphism group 通常是 trivial。不能预先除 4。

2. Two-loop perturbative-order equation
2.1 Exact valence equation

令：

insertion valence 为 n
I
	​

；

action vertices 为 n
1
	​

,…,n
N
	​

；

external legs 数为 2；

internal edges 数为 I
int
	​

。

Half-edge counting：

n
I
	​

+
a=1
∑
N
	​

n
a
	​

=2I
int
	​

+2.

Connected loop identity：

L=I
int
	​

−(N+1)+1=I
int
	​

−N.

消去 I
int
	​

：

2L=(n
I
	​

−2)+
a=1
∑
N
	​

(n
a
	​

−2).
	​


At two loops：

(n
I
	​

−2)+
a=1
∑
N
	​

(n
a
	​

−2)=4.
	​


这是所有 bare graph census 的完整 combinatorial gate。

2.2 全部 bare physical families

对 genuine action vertices n
a
	​

≥3，所有非负整数解恰好是：

n
I
	​

2
3
4
5
6
	​

action content
S
3
4
	​

,S
3
2
	​

S
4
	​

,S
4
2
	​

,S
3
	​

S
5
	​

,S
6
	​

S
3
3
	​

,S
3
	​

S
4
	​

,S
5
	​

S
3
2
	​

,S
4
	​

S
3
	​

1
	​

	​

	​


即：

	​

I
2
	​

S
3
4
	​

,I
2
	​

S
3
2
	​

S
4
	​

,I
2
	​

S
4
2
	​

,I
2
	​

S
3
	​

S
5
	​

,I
2
	​

S
6
	​

,
I
3
	​

S
3
3
	​

,I
3
	​

S
3
	​

S
4
	​

,I
3
	​

S
5
	​

,
I
4
	​

S
3
2
	​

,I
4
	​

S
4
	​

,
I
5
	​

S
3
	​

,I
6
	​

.
	​

	​


任何“只列 two-loop-looking topology”的 census 都不完整。

2.3 Euclidean interaction-expansion coefficients

写

S
int
	​

=
n≥3
∑
	​

S
(n)
	​

.

在

e
−S
int
	​

/ℏ

中，具有 N
n
	​

 个 S
n
	​

 vertices 的 combinatorial factor 是

∏
n
	​

N
n
	​

!
(−1)
∑
n
	​

N
n
	​

	​

.
	​


因此 bare two-loop operator expansion 是

Γ
bare
(2)
	​

=
	​

+
4!
1
	​

⟨I
2
	​

S
3
4
	​

⟩
c
	​

−
2!
1
	​

⟨I
2
	​

S
3
2
	​

S
4
	​

⟩
c
	​

+
2!
1
	​

⟨I
2
	​

S
4
2
	​

⟩
c
	​

+⟨I
2
	​

S
3
	​

S
5
	​

⟩
c
	​

−⟨I
2
	​

S
6
	​

⟩
c
	​

−
3!
1
	​

⟨I
3
	​

S
3
3
	​

⟩
c
	​

+⟨I
3
	​

S
3
	​

S
4
	​

⟩
c
	​

−⟨I
3
	​

S
5
	​

⟩
c
	​

+
2!
1
	​

⟨I
4
	​

S
3
2
	​

⟩
c
	​

−⟨I
4
	​

S
4
	​

⟩
c
	​

−⟨I
5
	​

S
3
	​

⟩
c
	​

+⟨I
6
	​

⟩
c
	​

.
	​

	​


这里每个 S
n
	​

 自身仍携带 main action 的原始 Euclidean sign。上式只表示 exponent expansion factor。

3. Main-derived nonlinear ingredients
3.1 Gauge connection and field strength

Verified main 在 gauge-chiral frame 定义

∇
a
C
	​

=e
−V
D
a
	​

e
V
,W
a
	​

=−
8
1
	​

D
ˉ
2
[e
−V
(D
a
	​

e
V
)],

而 antichiral strength 是

W
a
˙
	​

=+
8
1
	​

D
2
[e
V
(
D
ˉ
a
˙
	​

e
−V
)].

因此，直接由 BCH：

Γ
a
	​

:=e
−V
D
a
	​

e
V
=
n≥1
∑
	​

Γ
(n)a
	​

,
	​

Γ
(n)a
	​

=
n!
(−1)
n−1
	​

ad
V
n−1
	​

(D
a
	​

V).
	​


同理：

Γ
a
˙
	​

:=e
V
D
ˉ
a
˙
	​

e
−V
=−
n≥1
∑
	​

n!
1
	​

ad
V
n−1
	​

(
D
ˉ
a
˙
	​

V).
	​


然后：

W
(n)a
	​

=−
8
1
	​

D
ˉ
2
Γ
(n)a
	​

,
	​

W
(n)
a
˙
	​

=+
8
1
	​

D
2
Γ
(n)
a
˙
	​

.
	​


所有 component i-factors 只能在

[T
A
	​

,T
B
	​

]=ic
AB
	​

C
T
C
	​


实际展开时产生；禁止导入 canonical e
2gV
 coefficient。

3.2 X
(n)
	​


Matrix-adjoint notation 下：

X=∇
+
	​

W
+
	​

=D
+
	​

W
+
	​

+[Γ
+
	​

,W
+
	​

].

因此：

X
(n)
	​

=D
+
	​

W
(n)+
	​

+
r+s=n
r,s≥1
	​

∑
	​

[Γ
(r)+
	​

,W
(s)+
	​

].
	​


Two-loop census 需要：

Γ
(n)
	​

,W
(n)
	​

,
Γ
(n)
	​

,
W
(n)
	​

,X
(n)
	​

1≤n≤5.
	​


原因是：

S
6
	​

 中 W
r
	​

W
s
	​

 有 r+s=6，故 max(r,s)=5；

I
6
	​

 中 X
r
	​

X
s
	​

 有 r+s=6，故需要 X
5
	​

。

3.3 I
(2)
	​

,…,I
(6)
	​


对 two-adjoint-slot tensor：

I
AB
=∇
−
	​

(X
A
X
B
).

由于 X even：

I
(N)
AB
	​

=
	​

r+s=N
r,s≥1
	​

∑
	​

D
−
	​

(X
(r)
A
	​

X
(s)
B
	​

)
+
t+r+s=N
t,r,s≥1
	​

∑
	​

([Γ
(t)−
	​

,X
(r)
	​

]
A
X
(s)
B
	​

+X
(r)
A
	​

[Γ
(t)−
	​

,X
(s)
	​

]
B
).
	​

	​


Two-loop 要求完整生成：

I
(2)
	​

,I
(3)
	​

,I
(4)
	​

,I
(5)
	​

,I
(6)
	​

.
	​


例如：

I
(3)
AB
	​

=
	​

D
−
	​

(X
(1)
A
	​

X
(2)
B
	​

+X
(2)
A
	​

X
(1)
B
	​

)
+[Γ
(1)−
	​

,X
(1)
	​

]
A
X
(1)
B
	​

+X
(1)
A
	​

[Γ
(1)−
	​

,X
(1)
	​

]
B
.
	​

	​


这正是 all-cubic “日” parent insertion 的 source AST。

3.4 E
V
	​

 / Schwinger–Dyson insertion

从

Ξ=e
−V
δe
V

得到

Ξ=F(ad
V
	​

)δV,F(z)=
z
1−e
−z
	​

.

Invariant color pairing 下：

(ad
V
	​

)
T
=−ad
V
	​

.

所以：

E
V
	​

=F(ad
V
	​

)
T
E
Ξ
	​

=F(−ad
V
	​

)E
Ξ
	​

=
ad
V
	​

e
ad
V
	​

−1
	​

E
Ξ
	​

.
	​


即：

E
V
	​

=
n≥0
∑
	​

(n+1)!
1
	​

ad
V
n
	​

E
Ξ
	​

.
	​


对于 two-loop S
6
	​

 cutting，需要 E
V
	​

 至 quantum-V degree 5。

其 root

E
Ξ
gauge
	​

=
δΞ
δ
S
gauge
	​

	​


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

另外，N=4 gauge EOM 含 matter current。因此 pure-V sector 不自动对：

full N=4 EOM；

operator mixing；

renormalized ∇
−
	​

-cohomology

闭合。这是本项目最大的 scope caveat 之一。

4.2 Ghost-valence equation

一个 FP vertex 有：

one ghost；

one antighost；

r 个 quantum-V ports。

它的 total valence 是

n
FP
	​

=r+2,

所以对 loop equation 的贡献是

n
FP
	​

−2=r.

完整 two-loop equation 变成

(n
I
	​

−2)+
phys
∑
	​

(n
v
	​

−2)+
FP
∑
	​

r
v
	​

+
NK
∑
	​

(n
v
	​

−2)=4.
	​


然后必须：

saturate all ghost ports into oriented closed cycles；

apply one minus sign per closed odd cycle；

verify connectedness；

verify L=2。

Primitive one-loop XX ghost absence 不能推广到此处。

Verified main 的 FP/NK realization 是 branch-selected；BV–NK fields 只存在于指定 branch，其他 branch 中 R
NK
BV
	​

=∅。 因此 two-loop compiler 必须把 NK_branch_id 作为 immutable notation datum，而不能写一个 universal NK graph list。

4.3 Counterterm grading

给每个 counterterm vertex 一个 loop grade：

ℓ
ct
	​

(v)∈Z
≥1
	​

.

总 perturbative order：

L
total
	​

=L
geometric
	​

+
v
∑
	​

ℓ
ct
	​

(v)+ℓ
ct
	​

(I).
	​


At total order two，必须包括：

Bare two-loop
L
geometric
	​

=2,∑ℓ
ct
	​

=0.
One-loop graph with one one-loop counterterm
L
geometric
	​

=1,∑ℓ
ct
	​

=1.

Counterterms 可替换或插入：

δ
(1)
K
V
	​

,δ
(1)
S
3
	​

,δ
(1)
S
4
	​

,δ
(1)
I
2
	​

,δ
(1)
I
3
	​

,δ
(1)
I
4
	​

,

以及 FP/NK/gauge-fixing counterterms。

Tree graph with two-loop local counterterm
L
geometric
	​

=0,∑ℓ
ct
	​

=2.

包含：

δ
(2)
I,δ
(2)
S,δ
(1)
Iδ
(1)
S,

及 external-field renormalization，取决于所定义的是 amputated bare、1PI renormalized 还是 LSZ-normalized form factor。

Counterterm graphs 不是 Schwinger–Dyson descendants，必须使用独立 family ID。

5. Canonical two-loop momentum routing
5.1 Oriented incidence matrix

顶点顺序：

(v
I
	​

,v
C
	​

,v
W
	​

,v
W
	​

).

边顺序：

(e
0
	​

,e
1
	​

,e
2
	​

,e
3
	​

,e
4
	​

).

Orientations：

e
0
	​

e
1
	​

e
2
	​

e
3
	​

e
4
	​

	​

:v
I
	​

→v
C
	​

,
:v
I
	​

→v
W
	​

,
:v
W
	​

→v
C
	​

,
:v
I
	​

→v
W
	​

,
:v
W
	​

→v
C
	​

.
	​


Incidence matrix：

B=
	​

−1
+1
0
0
	​

−1
0
+1
0
	​

0
+1
−1
0
	​

−1
0
0
+1
	​

0
+1
0
−1
	​

	​

.
	​


External incoming injections：

j=
	​

−(p+q)
0
q
p
	​

	​

.

Momentum conservation：

Br+j=0.
5.2 Spanning tree and chords

Choose canonical spanning tree

T={e
0
	​

,e
2
	​

,e
4
	​

},

and chords

C={e
1
	​

,e
3
	​

}.

Define chord momenta：

r
1
	​

=k,r
3
	​

=ℓ.

Solving Br+j=0 gives：

r
0
	​

r
1
	​

r
2
	​

r
3
	​

r
4
	​

	​

=−(k+ℓ+p+q),
=k,
=k+q,
=ℓ,
=ℓ+p.
	​

	​


Checks：

−r
0
	​

−r
1
	​

−r
3
	​

−(p+q)=0,
r
0
	​

+r
2
	​

+r
4
	​

=0,
r
1
	​

−r
2
	​

+q=0,
r
3
	​

−r
4
	​

+p=0.

Canonical denominator：

D
\日
	​

=(k+ℓ+p+q)
2
k
2
(k+q)
2
ℓ
2
(ℓ+p)
2
.
	​

5.3 Automorphism 与 symmetry factor

Primary graph coefficient 必须定义为 labeled Wick-pairing sum：

C
Γ
	​

=
P:Can(P)=Γ
∑
	​

∏
n
	​

N
n
	​

!
(−1)
κ(P)+N
oddcycles
	​

(P)
	​

C
I
	​

(P)
v
∏
	​

C
v
	​

(P)
e
∏
	​

C
e
	​

(P).
	​


Typed automorphism group 只作 independent audit：

∣Orb
lab
	​

(Γ)∣=
∣Aut
typ
	​

(Γ)∣
∣G
lab
	​

∣
	​

.

若已经 sum over labeled pairings，再除一次

∣Aut
typ
	​

(Γ)∣

会产生 double division。

5.4 Coupling order

对于 bare physical graph：

I
int
	​

=N
action
	​

+L=N
action
	​

+2.

每个 physical action vertex 带 h，每个 V-propagator 带 g
2
。因此 symbolic coupling power：

(g
2
)
N
action
	​

+2
h
N
action
	​

=g
2N
action
	​

+4
g
−2N
action
	​

=
g
4
	​

.

这只是 absorbed-basis order check，不包含 numerical propagator normalization、vertex fraction 或 i-sign。

6. Two-loop edge-tagged D-algebra schedule

Verified main Euclidean flat algebra是

{D
a
	​

,
D
ˉ
b
˙
	​

}=−2(σ
E
m
	​

)
a
b
˙
	​

∂
m
	​

,
	​

{D
a
	​

,D
b
	​

}={
D
ˉ
a
˙
	​

,
D
ˉ
b
˙
	​

}=0.

Fourier conversion 必须单独应用：

∂
m
	​

⟼ir
m
	​

.

所以 mixed pair 产生的 sign 是：

−2i(σ
E
	​

⋅r)
a
b
˙
	​

,

除非 derivative order 已经先交换并带额外 minus。

6.1 Theta spanning tree

使用与 momentum routing 相同的 tree：

T
θ
	​

={e
0
	​

,e
2
	​

,e
4
	​

},

root：

v
I
	​

.

Deterministic post-order：

v
W
	​

⟶
e
4
	​

	​

v
C
	​

,v
W
	​

⟶
e
2
	​

	​

v
C
	​

,v
C
	​

⟶
e
0
	​

	​

v
I
	​

.

Chord theta kernels：

e
1
	​

,e
3
	​


在 root 上留下 two independent cycle delta structures，必须由 D-operators saturation；不得写成裸 δ
4
(0)
2
。

6.2 Eight phases
Phase 1 — derivative-scope expansion

展开：

every D- or 
D
ˉ
-difference；

every graded Leibniz branch；

D
−
	​

 placement；

nonlinear X
(n)
	​

 branches；

chiral/antichiral projector scopes。

Termination count：

M
1
	​

=N
unexpanded scopes
	​

.
Phase 2 — endpoint canonicalization

每条 edge 选择 canonical endpoint，例如 tail endpoint。

只允许：

D
noncan
	​

(r)Δ
e
	​

⟶−D
can
	​

(−r)Δ
e
	​

,
D
ˉ
noncan
	​

(r)Δ
e
	​

⟶−
D
ˉ
can
	​

(−r)Δ
e
	​

.

禁止 reverse rule。

M
2
	​

=N
derivatives on noncanonical endpoints
	​

.
Phase 3 — pivoted superspace IBP

对于 ordered factors F
1
	​

⋯F
n
	​

：

0=
j
∑
	​

(−1)
P
j
	​

∫F
1
	​

⋯(DF
j
	​

)⋯F
n
	​

,
P
j
	​

=
k<j
∑
	​

∣F
k
	​

∣.

若 source 是 s：

T
s
	​

=−
j

=s
∑
	​

(−1)
P
j
	​

+P
s
	​

T
j
	​

.
	​


每个 theta point 固定一个 pivot；derivative 只允许离开 active pivot 一次，不能反向 IBP。

M
3
	​

=N
derivatives on active pivots
	​

.
Phase 4 — primitive D,
D
ˉ
 normal order

固定：

D
−
	​

<D
+
	​

<
D
ˉ
−
˙
	​

	​

<
D
ˉ
+
˙
	​

	​

.

Rules：

D
b
	​

D
a
	​

⟶−D
a
	​

D
b
	​

(b>a),
D
a
	​

D
a
	​

⟶0,
D
ˉ
a
˙
	​

D
ˉ
a
˙
	​

⟶0,
D
ˉ
b
˙
	​

D
a
	​

⟶−D
a
	​

D
ˉ
b
˙
	​

−2(σ
E
m
	​

)
a
b
˙
	​

∂
m
	​

.
	​


Measure：

M
4
	​

=(N
operator inversions
	​

,N
D
	​

+N
D
ˉ
	​

).
Phase 5 — projector reduction

Coordinate-space identities：

D
2
D
ˉ
2
D
2
⟶16□D
2
,
D
ˉ
2
D
2
D
ˉ
2
⟶16□
D
ˉ
2
.

□→−p
2
 的 Fourier sign 必须来自 notation schema，而不是 baked into rewrite rule。

Phase 6 — chirality

只在 derivative 已 structurally attached 到 external field 后应用：

D
ˉ
a
˙
	​

W
b
	​

=0,
D
ˉ
a
˙
	​

Φ=0,
D
a
	​

W
b
˙
	​

=0,D
a
	​

Φ
=0.

“未来可能 IBP 到 chiral field” 不能作为提前置零的理由。

Phase 7 — Grassmann saturation

Tree theta points 按 post-order 消除。最终 closed-loop identities 由 exact Grassmann oracle 验证，例如：

[D
2
D
ˉ
2
δ
4
(θ)]
θ=0
	​

=16.

Two-loop oracle 必须使用 polynomial momentum entries：

Mat
16
	​

(Q(i)[p
+
+
˙
	​

	​

,p
+
−
˙
	​

	​

,p
−
+
˙
	​

	​

,p
−
−
˙
	​

	​

]),

不能只测试有限个 numerical momenta。

Phase 8 — typed edge collapse

只有当同一 edge 上出现 matching pair：

K
e
	​

G
e
	​


时才 collapse。

Vector edge：

K
V
	​

G
V
	​

=1
full superspace
	​

.

Chiral matter edge 一般只给 projector：

H
Φ
Φ
	​

G
Φ
Φ
	​

=Π
chiral
	​

.

Collapse 必须 emit child GraphIR，并记录：

parent_graph_id
parent_DWord_id
cut_edge_id
kinetic_kernel_id
propagator_kernel_id
result_projector
6.3 Two-loop critical pairs

必须逐个做 joinability test：

Critical pair	Required equality
central-edge endpoint transfer / left-loop reduction	两条 path 的 momentum-reversed NF 相同
central-edge endpoint transfer / right-loop reduction	同上
two mixed anticommutators sharing one D	operator provenance 不丢失
projector macro / primitive D
D
ˉ
 reordering	都得到相同 16□D
2
 form
collapse e
i
	​

 then e
j
	​

 / reverse order	若 cuts compatible，child common NF 相同
central-edge collapse / theta-tree elimination	re-rooted theta tree 给同一 child
chirality / mixed anticommutator	必须先 mixed normalization，再 chirality
forest contraction / D-collapse	counterterm subgraph ancestry 保持
loop rerouting / endpoint momentum reversal	affine routing certificate 相容
external derivative token / EOM projection	token 先保留，再进入 cohomology phase

全局 termination measure：

M=(M
1
	​

,M
2
	​

,M
3
	​

,N
inversions
	​

,N
projector redex
	​

,N
θ

=θ
I
	​

	​

,N
cuttable pairs
	​

,∣E∣,∣V∣)
	​


lexicographically，并通过 phase barriers 禁止前一 phase 的规则重新生成。

7. DRED at two loops
7.1 Metric typing
δ
(4)
mn
	​

=
δ
mn
+
δ
mn
,
	​

δ
m
	​

m
=d=4−2ϵ,
δ
m
	​

m
=2ϵ.

要求：

VECTOR4
VECTOR_HAT
VECTOR_TILDE

是三个不同 index types。

spinor/D-algebra 只产生 VECTOR4；

loop tensor integration 只产生 VECTOR_HAT；

两者相减后才允许产生 VECTOR_TILDE。

External and loop momenta：

δ
m
n
	​

p
n
=
δ
m
n
	​

q
n
=
δ
m
n
	​

k
n
=
δ
m
n
	​

ℓ
n
=0.
7.2 Tensor reduction

Rank two：

∫k
m
k
n
F=A
δ
mn
+
u,v∈{p,q}
∑
	​

B
uv
	​

u
m
v
n
.
	​


Mixed rank two：

∫k
m
ℓ
n
F=C
δ
mn
+
u,v∈{p,q}
∑
	​

D
uv
	​

u
m
v
n
.

Rank four：

∫k
m
k
n
ℓ
r
ℓ
s
F=
	​

A
1
	​

δ
mn
δ
rs
+A
2
	​

δ
mr
δ
ns
+A
3
	​

δ
ms
δ
nr
+terms containing external momenta.
	​

7.3 Evanescent numerator 的唯一合法来源

Bare D-algebra numerator 中禁止出现手写 ϵ。

Evanescent structures 只能在 independently compiled terms 相加后出现，例如：

δ
mn
−δ
(4)
mn
	​

=−
δ
mn
.

At rank four：

δ
mn
δ
rs
−δ
(4)
mn
	​

δ
(4)
rs
	​

=−
δ
mn
δ
(4)
rs
	​

−
δ
mn
δ
rs
.
	​


右侧自动包含 single- 和 double-evanescent sectors。

Two-loop finite contributions 可来自：

δ
×
ϵ
1
	​

,

或

δ
δ
×
ϵ
2
1
	​

.

Single 
δ
 乘 1/ϵ
2
 会先产生 residual 1/ϵ，必须由 forest subtraction/counterterms 处理；不能直接称为 anomaly。

8. UV subdivergences and R-operation
8.1 Off-shell domain

必须先工作在：

p
2
>0,q
2
>0,(p+q)
2
>0.
	​


禁止在 subtraction 前设置：

p=0,q=0,p+q=0.

否则：

0
DRED
	​

=
ϵ
UV
	​

1
	​

−
ϵ
IR
	​

1
	​


会伪装成 UV cancellation。

8.2 Forest formula

定义 K 为 chosen 
DR
 pole projector。

Proper-subgraph subtraction：

R
ˉ
Γ=Γ+
F∈F
proper
	​

(Γ)
F

=∅
	​

∑
	​

	​

γ∈F
∏
	​

C(γ)
	​

Γ/F,
	​


其中

C(γ)=−K
R
ˉ
γ.
	​


Full renormalized graph：

RΓ=(1−K)
R
ˉ
Γ.
	​

8.3 “日” graph 的 overlapping one-loop subgraphs

定义：

γ
L
	​

={v
I
	​

,v
C
	​

,v
W
	​

;e
0
	​

,e
1
	​

,e
2
	​

},
γ
R
	​

={v
I
	​

,v
C
	​

,v
W
	​

;e
0
	​

,e
3
	​

,e
4
	​

}.

两者各自满足：

I=3,V=3,L=1.

它们共享：

{v
I
	​

,v
C
	​

,e
0
	​

},

因此：

γ
L
	​


⊂γ
R
	​

,γ
R
	​


⊂γ
L
	​

,

且并非 disjoint。

所以不存在 forest：

{γ
L
	​

,γ
R
	​

}∈
/
F(Γ
\日
	​

).
	​


Allowed forests 至少包括：

∅,{γ
L
	​

},{γ
R
	​

}.

每个 candidate subgraph 是否真的 superficially divergent，仍须由 its compiled numerator 和 operator dimension 判定。

8.4 Operator versus action subdivergences

含 insertion vertex 的 divergent subgraph产生：

composite-operator counterterm.

不含 insertion 的 divergent subgraph产生：

action/field/coupling counterterm.

两者不可放进同一个 undifferentiated counterterm type。

8.5 Double and single poles

Bare two-loop graph：

Γ
bare
(2)
	​

=
ϵ
2
a
−2
	​

	​

+
ϵ
a
−1
	​

	​

+a
0
	​

+⋯.

R
ˉ
 后：

R
ˉ
Γ=
ϵ
b
−1
	​

	​

+b
0
	​

+⋯.

a
−2
	​

 主要由 one-loop subdivergence products 产生；

b
−1
	​

 是 subdivergence-subtracted overall pole；

primitive two-loop local term 只能从 
R
ˉ
Γ 分析；

anomaly candidate 只能从完整 R-renormalized SD orbit 的 finite evanescent remainder 分析。

9. Integral families and IBP certificate
9.1 Canonical five-denominator family

设：

P=p+q,
D
0
	​

D
1
	​

D
2
	​

D
3
	​

D
4
	​

	​

=(k+ℓ+P)
2
,
=k
2
,
=(k+q)
2
,
=ℓ
2
,
=(ℓ+p)
2
.
	​

	​


定义：

J
ν
	​

[N]=μ
4ϵ
∫
(2π)
2d
d
d
kd
d
ℓ
	​

D
0
ν
0
	​

	​

D
1
ν
1
	​

	​

D
2
ν
2
	​

	​

D
3
ν
3
	​

	​

D
4
ν
4
	​

	​

N(k,ℓ,p,q)
	​

.
	​


Independent loop-dependent scalar products 数：

2
L(L+1)
	​

+LE=
2
2⋅3
	​

+2⋅2=7.

五个 denominators 留下 two irreducible scalar products，可取：

ρ
1
	​

=k⋅p,ρ
2
	​

=ℓ⋅q.
	​


因此 scalar family 可写为：

J
ν
0
	​

⋯ν
4
	​

;a,b
	​

=J
ν
	​

[(k⋅p)
a
(ℓ⋅q)
b
].
9.2 Pinches and descendants
ν
i
	​

=0

表示 edge e
i
	​

 被 pinched/collapsed 后的 subtopology。

这些 pinches 必须保留 parent edge provenance，不能只作为 anonymous lower-sector integral。

9.3 IBP equations

生成：

0=∫d
d
kd
d
ℓ
∂k
m
	​

∂
	​

[v
m
	​

∏
i
	​

D
i
ν
i
	​

	​

N
	​

],
0=∫d
d
kd
d
ℓ
∂ℓ
m
	​

∂
	​

[v
m
	​

∏
i
	​

D
i
ν
i
	​

	​

N
	​

],

其中：

v∈{k,ℓ,p,q}.
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

IntegralPoleCompiler 必须先计算每项的 ϵ-valuation。

若：

E(ϵ)=ϵ
s
E
s
	​

+⋯,

而 master：

M(ϵ)=
r=−R
∑
∞
	​

m
r
	​

ϵ
r
,

finite term 需要所有：

s+r=0.

At two loops：

non-evanescent double-pole sector需要 master 至 finite order；

one-loop counterterm × one-loop graph 常要求 one-loop master 至 O(ϵ)；

double-evanescent × 1/ϵ
2
 需要准确保留 metric contraction 至 O(ϵ
2
)。

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

I
2
	​

S
3
4
	​

,…,I
6
	​

.

“日” subset 包含：

I
3
	​

S
3
3
	​


和

I
2
	​

S
3
2
	​

S
4
	​


中 canonicalize 到 K
4
	​

∖e 的 graphs。

10.2 Edge collapses

每个 Γ
\日
	​

 有五个 tagged cuts：

Cut
e
i
	​

	​

Γ
\日
	​

,i=0,…,4.

重要修正：

ordinary edge contraction preserves loop rank.
	​


因为：

I
′
=I−1,V
′
=V−1,

所以：

L
′
=(I−1)−(V−1)+1=L=2.

特别地，central edge e
0
	​

 collapse 后：

v
I
	​

 和 v
C
	​

 fuse；

e
1
	​

,e
2
	​

 变成一对 parallel edges；

e
3
	​

,e
4
	​

 变成另一对 parallel edges；

得到 two-loop figure-eight/double-bubble child：

V
′
=3,I
′
=4,L
′
=2.

因此任何 test 写成 “central collapse gives L=1” 都是错误的。

10.3 Explicit SD basis

Explicit physical basis 包含：

nonlinear I
3
	​

,I
4
	​

,I
5
	​

,I
6
	​

 insertion graphs；

quartic/quintic/sextic action graphs；

I
2
	​

S
3
2
	​

S
4
	​

 seagull realizations；

I
2
	​

S
4
2
	​

、I
3
	​

S
3
	​

S
4
	​

、I
4
	​

S
3
2
	​

 bubble/double-bubble families；

gauge-fixing/FP/NK descendants；

EOM insertion graphs；

scaleless candidates，在 individual routing 检查后分类；

one-loop counterterm insertions。

10.4 Collapsed/cut basis

Cut basis 由：

K
e
	​

G
e
	​


对 parent edge 的作用生成。

它是同一 SD orbit 的另一组 representatives，不是另一组额外 amplitude。

10.5 Quotient-space equality

Raw explicit graph 数量和 cut representatives 数量通常不同，不能要求 naive set bijection。

定义 common contact normal-form space N
SD
	​

：

M
E
	​

:K
N
E
	​

→N
SD
	​

,
M
C
	​

:K
N
C
	​

→N
SD
	​

.

令 c
E
	​

,c
C
	​

 是 exact coefficient vectors。Required proof：

M
E
	​

c
E
	​

=M
C
	​

c
C
	​

.
	​


同时保存：

kerM
E
	​

,kerM
C
	​

,rankM
E
	​

,rankM
C
	​

.

只有当两个 matrices square 且 invertible 时，才可称为 literal bijection。

10.6 Double-counting prohibition

选择：

counting_basis = EXPLICIT

则：

A
SD
	​

=
χ∈B
explicit
	​

∑
	​

A
χ
	​

.

Cut basis 只作为 proof witness。

或者选择：

counting_basis = COLLAPSED

则只 sum cut basis。

绝不允许：

explicit
∑
	​

A
χ
	​

+
cut
∑
	​

A
η
	​

.
10.7 Ordinary cancellation 的正确 proof target

在 forest subtraction 后，定义：

S
SD
(2)
	​

=
Γ∈O
SD
(2)
	​

∑
	​

R
DR
	​

A
Γ
	​

.
	​


将其分解为：

S
SD
(2)
	​

=S
ordinary
	​

+S
evanescent
	​

+S
EOM
	​

+S
total deriv.
	​

+S
scheme
	​

.

Required equality：

S
ordinary
	​

=0
	​


必须由 explicit graph/counterterm sum 证明。

只有随后才定义：

A
candidate
(2)
	​

=Fin
ϵ→0
	​

Π
H
∇
−
	​

	​

	​

S
evanescent
	​

.
	​


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

Γ,
Γ
,W,
W
,Xthrough degree 5,
I
2
	​

,…,I
6
	​

,
S
2
	​

,…,S
6
	​

,

and FP/NK vertices required by the selected branch。

Gate T2 — Exhaustive census

all twelve bare source families；

every quantum port saturated；

connected；

L=2；

no ValenceRequest cast to graph。

Gate T3 — “日” topology

Verify：

V=4,I=5,L=2,

degree multiset：

[3,3,2,2],

incidence matrix rank：

rankB=V−1=3.
Gate T4 — Canonical amplitude

Verify routing：

(r
0
	​

,…,r
4
	​

)=(−(k+ℓ+p+q),k,k+q,ℓ,ℓ+p).

No handwritten numerator field exists。

Gate T5 — Two-loop D-algebra

local confluence；

termination；

polynomial 16×16 oracle；

central-edge critical pairs；

external tokens preserved。

Gate T6 — R-operation and IBP

overlapping γ
L
	​

,γ
R
	​

 never appear in same forest；

all subdivergences subtracted；

master reduction certificate；

nonexceptional IR status。

Gate T7 — SD quotient equality
M
E
	​

c
E
	​

=M
C
	​

c
C
	​

.

No explicit/cut double counting。

Gate T8 — anomaly/cohomology projection

Only after T0–T7：

Fin
ϵ→0
	​

Π
H
∇
−
	​

	​

	​

Γ
∑
	​

RA
Γ
	​

.
Gate T9 — external comparison

Euclidean result is compared to twist ledger without allowing reverse dependency。

11.6 Deterministic tests
RI-TOPOLOGY-001
I−V+1=5−4+1=2.
RI-ROUTING-001

Directly verify：

Br+j=0.
RI-SOURCE-FAMILIES-001

Only：

I
3
	​

S
3
3
	​

,I
2
	​

S
3
2
	​

S
4
	​


may canonicalize to four-vertex five-edge “日” graphs。

RI-COUPLING-001

For N physical action vertices：

(g
2
)
N+2
h
N
=g
4
.
RI-AUTOMORPHISM-001

Compare labeled pairing sum with orbit-stabilizer count；确认不重复除 ∣Aut
typ
	​

∣。

RI-CENTRAL-COLLAPSE-001
(V,I,L)=(4,5,2)⟶(3,4,2).
RI-FOREST-OVERLAP-001

Reject：

{γ
L
	​

,γ
R
	​

}.
RI-DRED-001

Bare DWord AST contains no symbol ϵ。

RI-METRIC-001

Loop tensor reduction cannot emit VECTOR4; D-algebra cannot emit VECTOR_HAT。

RI-IBP-001

Every reduction coefficient is rational in：

d,p
2
,q
2
,(p+q)
2
.
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

该文 §4.5、Eq. (4.34)、paper page 27 把 four-vertex five-edge graph 称为 bitriangle，并称其为唯一 two-loop Laman graph。其 topology 正是 K
4
	​

∖e。
arXiv
+1

其 leading universal bitriangle function 为 Eq. (4.44)：

f[λ
1
	​

,λ
2
	​

,λ
3
	​

;0,0]=
24
1
	​

(λ
1
	​

∧(λ
2
	​

+2λ
3
	​

))(λ
2
	​

∧(λ
1
	​

+2λ
3
	​

)).
	​


这是 holomorphic universal integral target，不是 Euclidean SYM coefficient。
arXiv

12.2 关于 Q
2
	​

(b
A
b
B
) 的 citation mismatch

EXTERNAL_TARGET_NOT_DERIVATION — TARGET NOT VERIFIED AS STATED

K. Budzik et al., Semi-Chiral Operators in 4d N=1 Gauge Theories, arXiv:2306.01039，明确写出：

Q
n
	​

:V(n+1,0,J
1
	​

,J
2
	​

)⟶V(1,1,J
1
	​

+n,J
2
	​

+n).

因此在该文 convention 中，primitive Q
2
	​

 作用于 three b-letters，不是 two b-letters。该文同时说明唯一 two-loop diagram 非零。
arXiv
+1

我没有核验到一条 published equation：

Q
2
	​

(b
A
b
B
)=⋯.

因此不能猜测或伪造该公式。

12.3 已核验到的 published Q
2
	​

 example

EXTERNAL_TARGET_NOT_DERIVATION

同一文 Appendix C，Eq. (C.8)，paper page 61，给出 pure SU(2) bootstrap example：

Q
2
	​

(b
A
	​

b
A
b
B
	​

b
B
)=
3
20C
1
2
	​

	​

ϵ
ABC
	​

b
A
∂
α
	​

∂
β
	​

b
B
∂
α
∂
β
c
C
.
	​


arXiv

Source convention dictionary：

b
A
,c
A
A,B,C
ϵ
ABC
	​

α,β=1,2
C
1
	​

	​

holomorphic BF semi-chiral fields
SU(2) adjoint indices
SU(2) structure tensor
holomorphic derivative indices
one-loop bootstrap normalization
	​


Appendix 前一页说明，和 direct one-loop result 比较可取 C
1
	​

=−2，但后续 formulas 保持 C
1
	​

 symbolic。
arXiv

这个 formula：

输入是 four b-letters；

是 SU(2) gauge-invariant composite example；

不是已核验的 open-index Q
2
	​

(b
A
b
B
)；

不得作为 Euclidean two-loop derivation input。

13. Strict find-gap table

Severity：

P0
P1
P2
P3
	​

对象或 authority 未定义，阻塞计算开始
阻塞任何 two-loop coefficient/anomaly claim
不阻塞单个 symbolic seed，但阻塞 completeness/automation
documentation/rendering/reproducibility defect
	​

ID	Level	Gap	Exact failure mode	Required resolution
G-DEF-01	P0	“日” topology 未锁定	sunset、figure-eight、bitriangle 混用	Commit K4_MINUS_EDGE, V=4,I=5,L=2
G-DEF-02	P0	External form factor 未锁定	同图可对应不同 operator tensor	Freeze external probes、ordering、amputation convention
G-SCOPE-01	P0	“pure gauge” 含义不清	physical V-only 与 gauge-completed sector 混淆	分开 PHYSICAL_GAUGE / GAUGE_COMPLETION
G-SCOPE-02	P1	Pure-gauge subset 非 N=4 EOM-closed	matter-current/operator mixing 被遗漏	明确它只是 sector contribution；最终加入 matter orbit
G-NORM-01	P1	Two-loop fixed-gauge propagator normalization 未由 main 重建	任何 numerical prefactor 不可信	从 main action/gauge choice 重新 invert Hessian
G-ALG-01	P1	Γ,W,
W
,X 未生成至 degree 5	S
5
	​

,S
6
	​

,I
5
	​

,I
6
	​

 缺失	Exact BCH compiler
G-ALG-02	P1	S
2
	​

,…,S
6
	​

、I
2
	​

,…,I
6
	​

 AST 不完整	graph census 漏 family	AST round-trip identities
G-SIGN-01	P1	Exponent factorial 与 Wick multiplicity 可能双计	错除 N
v
	​

! 或 automorphism	Labeled-pairing primary weight
G-SIGN-02	P1	Direct/reflected odd external ordering 未审计	relative sign ambiguity	External-word permutation certificate
G-IDX-01	P1	Central edge derivative provenance 不完整	左右 loops 的 D-operators 混合	Edge+endpoint+momentum typed tokens
G-IDX-02	P1	VECTOR4/HAT/TILDE 未分型	非法提前识别 δ
4
	​

=
δ
	Three distinct index types
G-OP-01	P1	Unrestricted IBP 不终止	exact two-cycle	Phase-scheduled pivoted IBP
G-OP-02	P1	Two-loop critical pairs 未 join	result 依 rewrite order	Local confluence certificate
G-PROJ-01	P1	Matter/vector cut projector 未分型	KG 被错误统一成 identity	Typed collapse result
G-PROJ-02	P1	Final ∇
−
	​

-cohomology projection 未定义	EOM/total derivative/anomaly 混合	Explicit quotient basis
G-THM-01	P1	R-operation 未实现	subdivergence 被误当 primitive pole	ForestIR + R,
R
ˉ
,K certificates
G-THM-02	P1	Overlapping triangles 未编码	非法 forest {γ
L
	​

,γ
R
	​

}	Forest compatibility predicate
G-THM-03	P1	Explicit/cut SD bases 未证明等价	double counting 或 missing contact	M
E
	​

c
E
	​

=M
C
	​

c
C
	​

 proof
G-NORM-02	P1	Counterterm scheme 未锁定	finite evanescent term scheme-dependent	Freeze 
DR
 and finite-CT policy
G-SCOPE-03	P1	FP/NK branch 未锁定	ghost graph census 非唯一	Immutable branch ID from main
G-ALG-03	P1	Two-loop IBP/master reduction 缺失	pole coefficient 无 certificate	Laporta/IBP exact reduction + masters
G-ALG-04	P2	Master Laurent depth 未自动推断	ϵ×1/ϵ
2
 finite term 丢失	Valuation-driven expansion depth
G-OP-03	P2	16×16 oracle 仅 numerical samples	finite samples 非 polynomial proof	Polynomial matrix oracle/interpolation certificate
G-SCOPE-04	P2	Scaleless tadpole 直接置零风险	UV/IR poles 相消被隐藏	UV/IR typed status or R
∗

G-DEF-03	P2	Holomorphic target 被写成 Q
2
	​

(b
A
b
B
)	published convention 要求 Q
2
	​

 primitive input length 3	Resolve target operator dictionary
G-SCOPE-05	P2	N=1 holomorphic pure gauge 与 N=4 pure-gauge sector dictionary 未证	comparison category error	Explicit twist/field/operator map
G-PROJ-03	P2	External-target data 可反向进入 compiler	circular derivation	Hash-based import firewall
G-SCOPE-06	P3	Publication renderer 未绑定 IR hash	图和 amplitude 可能失配	Same-hash TikZ/SVG/PDF generation
G-NORM-03	P3	Formula provenance 未逐因子展示	auditability 差	Factor ledger beside each graph
Final verdict
“日” two-loop problem 在数学上没有已知 structural obstruction。
	​


但在以下四项完成前，不能输出 Euclidean coefficient：

1.
2.
3.
4.
	​

S
2…6
	​

,I
2…6
	​

 从 main 完整生成;
Γ
\日
	​

 的全部 RI-CUBIC 和 RI-SEAGULL graphs 完整 census;
R-operation + two-loop D-algebra + IBP masters;
M
E
	​

c
E
	​

=M
C
	​

c
C
	​

 的 SD quotient proof.
	​

	​


当前可接受的第一阶段 deliverable 应是：

一个 coefficient-symbolic、Wick-complete、五边、四顶点、 两圈的 K
4
	​

∖e GraphIR family，
	​


连同 exact incidence/routing、source-family proof、automorphism certificate 和 forest candidates；而不是任何预先写入的 numerator、pole 或 anomaly coefficient。
