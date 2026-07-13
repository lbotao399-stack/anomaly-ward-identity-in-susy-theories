# GPT Pro architecture audit — Step 5 typed supergraph pipeline

Date: 2026-07-12
Status: external review input; not mathematical authority
Conversation: https://chatgpt.com/c/6a51b2b1-5870-83e8-ad8f-b1f8496be0fc

## Verbatim response

新记号
K:=Q[i,s]/(i
2
+1, s
2
−2),s=
2
	​


是 exact algebraic coefficient field。

R
phys
	​

:=K[g
±1
,h
±1
,ℏ
±1
]/(hg
2
−1)

是 Project perturbative coefficient ring。

Can(P)

表示 labeled Wick pairing P 的 typed graph canonicalization。

NF
D
	​

(A)

表示 amplitude A 的 deterministic D-algebra normal form。

Aut
typ
	​

(Γ)

表示保持 vertex species、ordered ports、external ordering、derivative scopes、index tensors 与 edge orientations 的 typed automorphism group。

总体审核结论

这套 architecture 的方向是正确的，但当前描述还不能作为 acceptance-ready contract。必须修正五个核心问题：

1.
2.
3.
4.
5.
	​

full N=4 coefficient ring 不能只是 Q(i);
physical graph 必须 Wick-complete，而不是 partially contracted;
pre-integration amplitude 不天然 unique，必须固定 canonical routing;
IBP 不能作为 unrestricted rewrite rule，否则不终止;
explicit/contact 与 collapsed/cut 通常不是 raw set bijection，
而是 quotient-space linear equivalence。
	​

	​


另外，三个 compiler 还不够。目标 equality 包含 UV pole

P
χ
mr
	​

,

所以必须增加第四个 stage：

IntegralPoleCompiler:NF
D
	​

(A)⟶UV-pole tensor IR.
	​


否则 architecture 可以生成 numerator，却无法 machine-check

χ∈SD(ρ)
∑
	​

P
χ
mr
	​

.

当前 repository 已经有可复用的 typed pairing census、GraphIR skeleton 和 IBP ledger；但 GraphIR 仍把 coefficient、propagator、color word 与 symmetry information 大量存成 strings/metadata，而不是 algebraic typed objects。 当前 DAlgebraEngine 实际实现的是 one-step global IBP branching，还没有 mixed anticommutator、nilpotence、chirality、projector collapse 与 confluence machinery。

A. Minimal immutable notation schema
A.1 Coefficient ring

Full N=4 不能只用 exact Q(i)，因为 superpotential vertices 含

2
	​

hε
rst
	​

c
ABC
	​

.

Repository 的 vertex grammar 本身也已经为 coefficients 保留 sqrt2_power。

因此最低要求是

K=Q[i,
2
	​

]
	​


的 exact implementation，例如 sparse basis

a+bi+c
2
	​

+di
2
	​

,a,b,c,d∈Q.

Coupling monomial 与 algebraic coefficient 分开：

C=C
alg
	​

g
n
g
	​

h
n
h
	​

ℏ
n
ℏ
	​

,hg
2
=1.

禁止把

g
6
h
2
=g
2

作为 string simplification；它必须由 quotient-ring reduction 完成。

A.2 Immutable NotationSpec

最低 schema：

NotationSpec
  schema_version
  canonical_json_hash

  scalar_ring
    algebraic_generators: [i, sqrt2]
    relations: [i^2 = -1, sqrt2^2 = 2]
    coupling_generators: [g, h, hbar]
    coupling_relations: [h*g^2 = 1]

  index_spaces
    ColorAdjoint(symbolic dimension)
    Flavor3
    Undotted2
    Dotted2
    Vector4
    VectorHat(trace = 4 - 2 epsilon)
    VectorTilde(trace = 2 epsilon)

  canonical_index_orders
  canonical_field_order
  canonical_external_word_order
  canonical_theta_point_order
  canonical_momentum_basis_order

  tensors
    kappa_AB
    kappaInv^AB
    c_AB^C
    epsilon_rs t
    epsilon_ab
    epsilon_dot a dot b
    sigmaE^m_a dot a
    barSigmaE^m^dot a a
    delta4^mn
    hatDelta^mn
    tildeDelta^mn

  tensor_relations
    kappaInv^AC kappa_CB = delta^A_B
    c_AB^C = -c_BA^C
    Jacobi
    kappa invariance
    epsilon antisymmetry
    delta4 = hatDelta + tildeDelta
    hatDelta*tildeDelta = 0

  derivative_algebra
  field_species
  propagator_kernels
  action_roots
  composite_roots
  regulator_spec
  renormalization_scheme

每一个 downstream artifact 都必须带

notation_hash
source_ast_hashes
compiler_version_hash

否则两个不同 convention 下生成的 GraphIR 可以被错误合并。

A.3 Field schema
FieldSpecies
  field_id
  parity
  superspace_domain: FULL | CHIRAL | ANTICHIRAL
  representation
  index_signature
  is_fundamental_quantum_field
  is_derived_composite
  conjugacy_policy

Project fields：

field
V
A
Φ
r
A
	​

Φ
r
A
	​

W
a
A
	​

W
a
˙
A
	​

X
A
Y
r
A
	​

Z
r
A
	​

T
a
˙
A
	​

	​

∣⋅∣
0
0
0
1
1
0
1
0
1
	​

domain
full
chiral
antichiral
chiral
antichiral
derived
derived
derived
derived
	​

quantum fundamental
yes
yes
yes
no
no
no
no
no
no
	​

	​


background/quantum/external 不是 FieldSpecies property，而是每个 port occurrence 的 role。

A.4 DRED schema

必须区分三个 vector spaces：

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
δ
m
	​

m
=4−2ϵ,
δ
m
	​

m
=2ϵ.

禁止一个 generic VECTOR index 同时代表 three metric spaces。当前 GraphIR 的 IndexSpace.VECTOR 太粗；新 schema 至少需要：

VECTOR_4
VECTOR_HAT
VECTOR_TILDE

Spinor algebra 只引用 VECTOR_4；loop tensor reduction 只产生 VECTOR_HAT。

B. GraphIR / AmplitudeIR / DWordIR
B.1 GraphIR

“connected but not fully contracted physical supergraph” 这个表述必须修改为：

connected, Wick-complete, D-unreduced physical supergraph.
	​


一个 quantum port 没有 Wick partner 时，它只是 GraphRequest 或 OpenTemplate，不是 graph。

Required fields
GraphIR
  graph_id
  notation_hash
  source_hashes
  perturbative_order
  loop_number
  orientation: DIRECT | REFLECTED
  ordered_external_word

  source_vertex_multiset
  vertex_instances
  ports
  internal_edges
  external_legs

  exact_graph_weight
  expansion_factor_proof
  wick_pairing_proof
  automorphism_proof
  momentum_routing_proof

  parent_orbit_id
  graph_classification
VertexInstance
VertexInstance
  vertex_id
  source_term_id
  source_ast_hash
  copy_number
  measure: FULL | CHIRAL | ANTICHIRAL
  exact_coefficient
  ordered_port_ids
  tensor_expression
  derivative_scope_ast
  superspace_point_id
Port
Port
  port_id
  vertex_id
  ordinal
  field_species_id
  role: QUANTUM | BACKGROUND_EXTERNAL | SOURCE_EXTERNAL
  parity
  chirality
  index_slots
  derivative_scope_path
  local_factor_order
InternalEdge
InternalEdge
  edge_id
  left_port
  right_port
  propagator_kernel_id
  orientation
  endpoint_order
  momentum_expr
  theta_kernel
  projector_kernel

propagator_kernel_id 必须解析到 typed object，不能是

"-2*g^2*kappa^{-1}*delta4theta/r0^2"

这样的 string。

GraphIR invariants

每个 accepted GraphIR 必须满足：

∀p∈Q(Γ),deg
internal
	​

(p)=1,
	​


即每个 quantum port 恰好属于一条 internal edge。

∀p∈E(Γ),deg
external
	​

(p)=1.
	​

Q(Γ)∩E(Γ)=∅.
E
int
	​

−V+1=L.

当前 scope 要求：

L=1.

Momentum incidence matrix B 满足

Br+p
ext
	​

=0.

还必须满足：

parity(p
L
	​

)=parity(p
R
	​

)

对每条 propagator edge。

对于 oriented matter edge：

Φ⟶
Φ

与 reverse edge 不是同一个 raw kernel。

Exact graph weight

不要同时自由输入

wick_multiplicity
symmetry_factor
automorphism_factor

然后相乘。正确 primary definition 是 labeled pairing sum：

C
Γ
	​

=
P:Can(P)=Γ
∑
	​

∏
v
	​

N
v
	​

!
(−1)
N
int
	​

(P)+κ(P)
	​

s
ext
	​

(P)
u∈V(P)
∏
	​

C
u
	​

.
	​


这里：

N
v
	​

 是相同 action vertex species 的 copy number；

κ(P) 是 Wick/Koszul permutation；

s
ext
	​

 是 ordered external extraction sign；

action monomial 内已有的 1/3!、1/2 不得再次除。

Automorphism 只作为 independent audit：

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
	​


若已经 sum over labeled pairings，再除一次
∣Aut
typ
	​

∣，就会 double count symmetry division。

B.2 AmplitudeIR
AmplitudeIR
  amplitude_id
  graph_id
  notation_hash

  canonical_routing
  loop_basis
  overall_momentum_delta
  unresolved_theta_integrals

  ordered_factor_ledger
    insertion_factor
    expansion_factor
    vertex_factors
    propagator_factors
    external_factors
    wick_sign
    external_extraction_sign
    graph_weight

  exact_total_scalar
  color_tensor_expr
  flavor_tensor_expr
  spinor_tensor_expr

  initial_dword
  denominator_expr
  preintegration_integrand
Canonical routing is mandatory

“unique pre-integration amplitude” 在没有 routing convention 时是 false。

例如同一个 triangle 可以写成

k
2
(k+q)
2
(k+p+q)
2
N(k)
	​


也可以令

k
′
=k+q

得到不同 integrand string。

必须固定：

lexicographically first spanning tree；

lexicographically first chord orientation；

each chord defines one loop variable；

tree-edge momenta 由 Br+p
ext
	​

=0 解出；

loop variables ordered by chord ID。

这样才有

AmplitudeIR(Γ)

的唯一 canonical serialization。

Alternative routing 必须给出 unimodular affine map

k
ℓ
′
	​

=U
ℓ
	​

m
k
m
	​

+Q
ℓ
	​

(p
ext
	​

),detU=±1.
Factor-ledger invariant
C
total
	​

=C
graph
	​

C
insertion
	​

v
∏
	​

C
v
	​

e
∏
	​

C
e
	​

.
	​


Compiler 必须从 ledger 重新乘出 exact_total_scalar；禁止同时存一个无法追溯的 handwritten total。

每条 edge 在 denominator 中恰好出现一次：

#{denominator factor for e}=1.

除 overall momentum delta 外，所有 vertex deltas 必须被 routing solver 消去。

B.3 DWordIR

当前 DAlgebraBranch.coefficient 是 integer，而 full compiler 需要 exact algebraic sum；必须改为 ExactScalar。当前 derivative token 也缺少 endpoint/edge/momentum 的 structural typing。

DWordIR
  notation_hash
  amplitude_id
  terms: tuple[DTerm]

DTerm
  exact_coefficient
  ordered_factors
  theta_delta_factors
  derivative_operators
  vector_derivative_tokens
  tensor_expr
  external_derivative_tokens
  cut_tokens
  assumptions
  classification
Spinor derivative token
SpinorD
  op_id
  kind: D | BAR_D
  spinor_index
  theta_point
  endpoint_edge
  endpoint_side
  endpoint_momentum
  origin_scope_id
  route_history
Vector derivative token
VectorD
  undotted_index
  dotted_index
  momentum_expr
  fourier_i_power
  origin_pair: [D_id, barD_id]
Cut token
CutToken
  parent_edge_id
  kinetic_kernel_id
  propagator_kernel_id
  result_projector
  result_domain
  child_graph_id

Vector Feynman-gauge cut：

K
V
	​

G
V
	​

=1.

Matter cut 不是 unconstrained identity，而是

H
12
	​

G
21
	​

=Π
+
	​

,H
21
	​

G
12
	​

=Π
−
	​

.

Repository 的 chiral Hessian inverse 已明确产生这些 projectors。

C. Exact compilation sequence

需要四个 compiler，而不是三个。

C.1 SupergraphCompiler
Step C1. AST expansion

对每个 action/composite term：

F[V
B
	​

+v]=
ρ∈{B,Q}
n
F
	​

∑
	​

F
ρ
	​

.

Check：

ρ
∑
	​

F
ρ
	​

=F[V
B
	​

+v]
	​


作为 exact AST equality，而不是 numerical sample。

Step C2. Valence selection

Two-external, one-loop connected graph 满足

n
I
	​

+
a
∑
	​

n
a
	​

=2E+2,
1=E−(1+N
action
	​

)+1.

消去 E：

(n
I
	​

−2)+
a
∑
	​

(n
a
	​

−2)=2.
	​


因此只允许：

I
2
	​

S
3
	​

S
3
	​

,I
3
	​

S
3
	​

,I
2
	​

S
4
	​

,I
4
	​

.

这个 equation 应在 graph generation 前 pruning，而不是生成 arbitrary valence Cartesian product。

Step C3. Ordered external extraction

对于 ordered word

F
1
	​

F
2
	​

⋯F
n
	​


抽取第 j 个 odd factor 的 sign：

s
j
	​

=(−1)
∣F
j
	​

∣∑
k<j
	​

∣F
k
	​

∣
.

两个 external probes 按用户指定 external word sequentially 抽取。

Check：

δJ
2
	​

δ
	​

δJ
1
	​

δ
	​

F=
emitted assignments
∑
	​

C
assignment
	​

F
remaining
	​

.
Step C4. Complete typed Wick pairing

对所有剩余 quantum ports 生成 perfect matchings：

P:Q(Γ)⟶Q(Γ)

满足 propagator grammar。

只在所有 quantum ports saturated 后才允许生成 GraphIR。

Step C5. Connectedness and loop rank
components(Γ)=1,E−V+1=1.
Step C6. Typed canonicalization

Canonicalization 必须保持：

insertion vertex distinguished；

external leg order；

ordered port order；

field species；

chirality；

derivative scope；

color/flavor tensor bindings；

edge orientation；

direct/reflected label。

然后 aggregate labeled pairings，生成 exact graph coefficient。

当前 census 已经枚举 external assignments、typed pairings、connectedness 与 L=1，可以作为基础；但其输出还是 labeled TopologyCandidate，没有 typed automorphism quotient 与 exact graph-weight aggregation。

C.2 AmplitudeCompiler
Step C7. Canonical routing

求解

Br+p
ext
	​

=0.

Check：

r
e,L
	​

+r
e,R
	​

=0

对每条 edge，且每个 vertex：

e∋v
∑
	​

r
v,e
	​

+p
v,ext
	​

=0.
Step C8. Factor assembly

从 GraphIR references 依次装配：

A
Γ
	​

=C
Γ
	​

∫
ℓ=1
∏
L
	​

(2π)
d
d
d
k
ℓ
	​

	​

I
Γ
	​

v
∏
	​

V
v
	​

e
∏
	​

G
e
	​

.

不允许 compiler 接受 handwritten numerator field。

Step C9. Theta/delta initialization

每条 propagator 生成：

momentum denominator；

endpoint theta kernel；

projector operators；

color/flavor delta；

edge orientation。

所有 vertex derivative scopes 生成 initial DWordIR。

C.3 DAlgebraCompiler
Step C10. Derivative-scope expansion

每个 derivative scope 按 graded Leibniz 展开。例如

D(FG)=(DF)G+(−1)
∣F∣
F(DG).

输出 port-assignment branches。

Step C11. Endpoint routing and theta reduction

选择 canonical root superspace point，按 spanning tree 消去其他 theta points。

Step C12. Core D-algebra normal form

使用 §D 的 oriented rules。

Step C13. Classification

每个 term 进入唯一 primary class：

UV_TENSOR_CANDIDATE
EXTERNAL_DERIVATIVE
COLLAPSED_EDGE
CHIRAL_ZERO
NILPOTENT_ZERO
EOM_EXACT
SCALARLESS
FINITE_NONLOCAL
UNCLASSIFIED

UNCLASSIFIED 非空则 compilation fail。

C.4 IntegralPoleCompiler

这个 stage 是当前 plan 缺失的必要部分。

Input：

NF
D
	​

(A
Γ
	​

).

Output：

PoleIR
  graph_id
  d = 4 - 2 epsilon
  uv_degree
  ir_status
  feynman_parameter_domain
  loop_shift
  tensor_reduction
  pole_scalar
  pole_tensor_space: HAT | FOUR | TILDE
  finite_remainder

必须在

p
2
>0,q
2
>0,(p+q)
2
>0

完成 UV extraction，避免 scaleless UV/IR cancellation 被误认作 zero。

D. Rewrite ordering, termination, critical pairs
D.1 Unrestricted IBP 不终止

若把

∫(DF)G⟶−(−1)
∣F∣
∫F(DG)

和 reverse application 都允许，则：

∫(DF)G⟶−(−1)
∣F∣
∫F(DG)⟶∫(DF)G.

这是 exact two-cycle。

Endpoint transfer 也一样：

D
i
	​

(r)Δ
ij
	​

(r)⟶−D
j
	​

(−r)Δ
ij
	​

(r)⟶D
i
	​

(r)Δ
ij
	​

(r).

所以：

IBP 与 endpoint transfer 必须是 scheduled compiler phases， 不能是 unrestricted bidirectional rewrites。
	​

D.2 Deterministic phase order
Phase 1 — scope expansion

展开 derivative difference 与 product Leibniz。

Termination measure：

M
1
	​

=N
unexpanded scopes
	​

.
Phase 2 — endpoint canonicalization

固定每条 edge 的 canonical endpoint，例如 smaller theta-point ID。

只允许：

D
noncan
	​

(r)Δ⟶−D
can
	​

(−r)Δ.

Termination：

M
2
	​

=
D
∑
	​

1
noncanonical endpoint
	​

.
Phase 3 — pivoted IBP

对每个 superspace integration point 固定一个 pivot factor。只把 derivatives 从 pivot 移出一次；从 target 不再反向移动。

精确 formula：

0=
j=1
∑
n
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

:=
k<j
∑
	​

∣F
k
	​

∣.

若 source 为 s：

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


Termination：

M
3
	​

=N
derivatives on active pivot
	​

.
Phase 4 — primitive normal ordering

取 canonical order

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
+
	​

D
−
	​

⟶−D
−
	​

D
+
	​

,
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
a
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
a
˙
	​

−2D
a
a
˙
	​

.
	​


Fourier conversion：

D
a
a
˙
	​

⟶ip
a
a
˙
	​


只在 momentum owner 已确定后执行。

Termination measure：

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

)

lexicographically。

Phase 5 — projector identities

Coordinate-space rule：

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

在 Project Fourier convention 中：

□(p)=−p
2
.

这一 distinction 必须存在于 schema，不能直接把 projector rule 写成带固定 p
2
 sign 的 universal rule。

Phase 6 — chirality and external tokens

仅当 derivative 已经 structurally attached 到 external factor 时：

D
ˉ
a
˙
	​

Φ=0,
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
a
	​

Φ
=0,D
a
	​

W
b
˙
	​

=0.

不能因为某个 derivative 最终“可能”移动到 chiral field，就提前置零。

Phase 7 — Grassmann saturation
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
Phase 8 — typed edge collapse

只有当 □
e
	​

 与同一 edge 的 inverse kernel 匹配时才 cut。

Vector：

K
V
	​

G
V
	​

=1.

Matter：

H
12
	​

G
21
	​

=Π
+
	​

,H
21
	​

G
12
	​

=Π
−
	​

.

Collapse 生成 child GraphIR，不返回一个裸 scalar 1。

D.3 Critical-pair audit

至少需要以下 overlaps：

Critical pair	Required joinability
endpoint transfer / mixed anticommutator	momentum reversal r↔−r 后 normal forms 相同
same-chirality reorder / nilpotence
D
ˉ
D
+
	​

D
+
	​

 两条路径都给 0
mixed reorder / vector-derivative commutation	D
a
a
˙
	​

 不重新产生 spinor inversion
primitive expansion / D
2
D
ˉ
2
D
2
 macro	两条路径均给 16□D
2

IBP / chirality	先 IBP 再 chirality；提前 chirality path 必须被禁止
projector / edge collapse	vector 得 identity，matter 得 Π
±
	​


collapse / endpoint routing	child 的 derivative owner 与先 routing 后 collapse 一致
external-token creation / EOM projection	token 先保留，再进入独立 cohomology phase

Termination 加 local confluence 后，可以用 Newman’s lemma 得到 confluence。

D.4 16×16 oracle 的限制

当前 exact oracle 在若干具体 rational momentum 上检查 16×16 matrices。 这适合作 regression test，但不是 polynomial identity proof。

因为一个非零 polynomial 可以在有限 sample points 全部为零：

f(p)=
j=1
∏
N
	​

(p−p
j
	​

).

Production oracle 应使用：

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

]).
	​


或者：

compiler 给出 degree bound D
max
	​

；

exact interpolation 使用超过 polynomial-space dimension 的 rational points；

输出 interpolation certificate。

Matrix oracle 只能检查 spinor/Grassmann algebra；它不能证明：

edge provenance；

color/flavor contractions；

automorphism factor；

graph connectivity；

SD double-counting absence。

这些必须由 structural IR invariants 单独证明。

E. Connected graph census
E.1 Exact algorithm

对每个 ordered channel (L
i
A
	​

,L
j
B
	​

)：

由 valence equation 枚举 vertex multiplicity solutions；

实例化 labeled insertion/action vertex copies；

展开 background/quantum assignments；

按 ordered external probe word 抽取 external ports；

对 remaining quantum ports 枚举所有 typed perfect matchings；

构造 multigraph；

检查 connectedness；

检查 E−V+1=1；

求解 momentum incidence equations；

canonicalize decorated graph；

sum all labeled preimages into exact graph weight；

emit GraphIR。

E.2 Completeness proof

每个 perturbative Wick term 唯一给出：

(vertex multiset,external assignment,perfect matching).

Compiler 枚举这三个 finite sets 的 Cartesian product，并仅删除：

type-incompatible pairings；

unsaturated pairings；

disconnected pairings；

wrong loop rank；

inconsistent routing。

因此每个 legal graph 至少出现一次。

若两个 labeled terms canonicalize 到同一 typed graph，则它们进入同一个 graph-weight sum。于是 output 没有漏图，也没有重复 physical GraphIR。

E.3 防止 valence requests 冒充 graph

类型层面禁止 cast：

ValenceRequest
  insertion_valence
  action_valences
  requested_external_species

不能直接转换为 GraphIR。

只有：

CompleteWickPairing
  all_quantum_ports_saturated = true
  connected = true
  loop_rank = 1
  routing_solved = true

才能调用：

GraphIR.from_complete_pairing(...)

当前 repository census 已经执行 complete pairing、connectedness 与 one-loop filtering，这部分逻辑可以保留。

F. Explicit SD basis 与 collapsed basis
F.1 Literal bijection 通常不是正确要求

Raw explicit terms：

I
3
	​

S
3
	​

,I
2
	​

S
4
	​

,I
4
	​


与 collapsed/cut representatives 的数量通常不同。

当前 WW repository 本身就是例子：存在大量 ordered basis terms，但 aggregate metric contacts 只有 row-level representatives；repository 明确承认目前不是 basis-resolved sum。

因此不能要求 raw-set bijection

E
explicit
	​

↔E
cut
	​

.

正确对象是 common quotient normal form。

F.2 SDOrbitProof
SDOrbitProof
  orbit_id
  parent_graph_id
  parent_row_id

  explicit_basis_graph_ids
  collapsed_basis_ids

  common_contact_nf_basis

  M_explicit_to_nf
  M_collapsed_to_nf

  explicit_coefficient_vector
  collapsed_coefficient_vector

  explicit_kernel_relations
  collapsed_kernel_relations
  matrix_ranks
  equality_certificate

  counting_basis: EXPLICIT | COLLAPSED

令

c
E
	​


是 explicit graph coefficients，

c
C
	​


是 collapsed representatives coefficients。

Acceptance condition：

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


若 M
E
	​

,M
C
	​

 均 square 且 invertible，才可以声明 literal basis bijection。

若不是，则必须给出：

kerM
E
	​

,kerM
C
	​


的 generators，并证明 quotient-space equivalence。

F.3 Double-counting prohibition

Amplitude sum 只能选择一个 counting basis：

A
SD
	​

=
⎩
⎨
⎧
	​

χ∈E
explicit
	​

∑
	​

A
χ
	​

,
η∈E
cut
	​

∑
	​

A
η
	​

,
	​

counting_basis=EXPLICIT,
counting_basis=COLLAPSED.
	​

	​


禁止：

χ∈E
explicit
	​

∑
	​

A
χ
	​

+
η∈E
cut
	​

∑
	​

A
η
	​

.

Collapsed basis 是 proof witness，不是额外 graph family。

Counterterm insertions 也不属于 SD descendant basis；它们必须进入独立：

RENORMALIZATION_COUNTERTERM

family。

F.4 Row target

对每个 WW row ρ，真正需要证明的是：

χ∈E
explicit
	​

(ρ)
∑
	​

P
χ
mr
	​

=−
1024π
2
ϵ
g
2
	​

δ
(4)
mr
	​

.
	​


右侧不能作为 SDOrbitProof input；它只能是 IntegralPoleCompiler 对 explicit graphs 求和后的 expected test。

Repository 目前只证明了 aggregate SD identity，还没有完成 explicit basis graph sum，因此保持 conditional 是正确的。

G. Textbook-style renderer

Renderer 不参与数学推导，只消费 immutable GraphIR/AmplitudeIR。

每个 graph 最少输出两个版本。

G.1 Clean publication panel

必须显示：

graph ID；

insertion node；

action vertex species；

external field names 与 indices；

internal field species；

momentum arrows；

direct/reflected orientation；

loop momentum；

chiral/antichiral edge direction；

color/flavor tensor summary。

例如 edge label 不是单纯 k，而是：

e
1
	​

:V
C
,r
1
	​

=k+q.
G.2 Audit panel

额外显示：

port IDs；

derivative scope IDs；

D,
D
ˉ
 endpoint markers；

background/quantum roles；

propagator kernel ID；

Wick pairing ID；

automorphism orbit ID；

SD parent/cut site；

child GraphIR IDs。

G.3 Accompanying factor table

每张图必须附：

factor
expansion
insertion
vertex 1
vertex 2
propagators
Wick sign
external sign
graph total
	​

exact value/source
⋯
⋯
⋯
⋯
⋯
⋯
⋯
⋯
	​

	​

G.4 D-algebra strip

最少显示：

initial D-word
→ endpoint transfer
→ pivoted IBP
→ mixed anticommutators
→ closed theta loop
→ external derivative tokens / cut tokens
→ final normal form

PDF、SVG、TikZ 必须由同一 GraphIR hash 生成。

H. Minimal acceptance tests
H.1 NOTATION-001

验证：

i
2
=−1,s
2
=2,hg
2
=1.

并验证 N=4 superpotential coefficient 可被 exact ring 表示。

H.2 AST-ROUNDTRIP-001

对每个 source term：

F[V
B
	​

+v]−
ρ∈{B,Q}
n
∑
	​

F
ρ
	​

=0

作为 AST identity。

H.3 CENSUS-SATURATION-001

每个 emitted GraphIR：

∀p∈Q,deg(p)=1,
components=1,E−V+1=1.

任一 unsaturated template 必须保持 ValenceRequest type。

H.4 AUTOMORPHISM-001

选择一个含两个 identical cubic vertices 的 graph。

验证：

C
Γ
	​

=
labeled preimages
∑
	​

C
P
	​


与 typed orbit-stabilizer computation 一致。

同时验证：

C
Γ
	​


=
∣Aut
typ
	​

∣
1
	​

labeled preimages
∑
	​

C
P
	​


在已经完成 labeled sum 的 convention 下。

H.5 一个 WW row 的 end-to-end test

选择：

orientation = DIRECT
D_minus_placement = LEFT
barD_endpoint = e0
D_endpoint = e1

Repository Project rules给出：

D
−
	​

K
+
	​

=−
16
1
	​

D
2
D
ˉ
2
D
+
	​

,
K
+
	​

=−
8
1
	​

D
+
	​

D
ˉ
2
D
+
	​

.

因此 insertion scalar：

C
I
	​

=(−
16
1
	​

)(−
8
1
	​

)=
128
1
	​

.

Graph factor before D-chain：

C
graph
	​

	​

=(−2g
2
)
3
(−
8
ih
	​

)(
8
ih
	​

)
=−8g
6
64
h
2
	​

=−
8
g
6
h
2
	​

=−
8
g
2
	​

.
	​


D-chain：

C
D
	​

	​

=
128
1
	​

(16)(2i)(2i)
=
128
16
	​

(−4)
=−
2
1
	​

.
	​


Row scalar：

C
row
	​

=(−
8
g
2
	​

)(−
2
1
	​

)=
16
g
2
	​

.
	​


这只是 row acceptance，不是 anomaly coefficient。Repository 已有相同 Project row normalization，可作为 golden oracle。

Routing test：

r
0
	​

=k,r
1
	​

=k+q,r
2
	​

=k+p+q.

DWord result：

(r
0
	​

)
+
	​

β
˙
	​

(ip)
a
β
˙
	​

	​

(r
1
	​

)
a
α
˙
.
	​


Test assertions：

denominator 自动生成：

k
2
(k+q)
2
(k+p+q)
2
;

numerator 不存在于 GraphIR input；

numerator 只由两次 mixed anticommutator 生成；

external derivative token 记录到正确 external leg；

exact symbolic 16×16 oracle 与 DWord normal form 相等；

bare numerator 不含 ϵ；

该 test 不断言任何 contact pole 或 finite remainder。

当前 repository 的 eight-row construction 与 summed triangle structure可作为 regression surface。

H.6 Matter-edge test

使用 ordered chiral block：

H
ch
	​

=ϰ
E
	​

	​

0
−
4
1
	​

κD
2
	​

−
4
1
	​

κ
D
ˉ
2
0
	​

	​

,
G
ch
	​

=−ϰ
E
	​

	​

0
4
1
	​

κ
−1
D
2
□
−1
	​

4
1
	​

κ
−1
D
ˉ
2
□
−1
0
	​

	​

.

必须验证四个 compositions：

H
12
	​

G
21
	​

H
21
	​

G
12
	​

G
12
	​

H
21
	​

G
21
	​

H
12
	​

	​

=Π
+
	​

,
=Π
−
	​

,
=Π
+
	​

,
=Π
−
	​

,
	​

	​


其中

Π
+
	​

=
16□
D
ˉ
2
D
2
	​

,Π
−
	​

=
16□
D
2
D
ˉ
2
	​

.

再验证：

D
ˉ
a
˙
	​

Π
+
	​

=0,D
a
	​

Π
−
	​

=0,

而 generic nonzero momentum 下：

D
+
	​

Π
+
	​


=0,
D
ˉ
+
˙
	​

	​

Π
−
	​


=0.

这个 test 可以抓出四种错误：

把 Φ
Φ
 propagator 当 scalar delta；

忽略 edge orientation；

在错误 endpoint 使用 chirality；

把 matter cut 错写成 unconstrained identity。

Repository 当前 typed chiral inverse 已给出上述 projector compositions。

H.7 IBP-TERMINATION-001

构造

∫(DF)G.

确认 compiler 只执行一次 pivoted IBP，不允许生成：

(DF)G→F(DG)→(DF)G.
H.8 CRITICAL-PAIR-001

对所有实际出现的 overlap words，验证：

NF
D
(1)
	​

(w)=NF
D
(2)
	​

(w)

既在 symbolic rewrite tree 中成立，也在 polynomial 16×16 oracle 中成立。

H.9 SD-BASIS-SEPARATION-001

确认：

counting_basis = EXPLICIT

时 collapsed representatives 不进入 amplitude sum。

并验证：

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


是 proof obligation，而不是 metadata assertion。

H.10 POLE-STAGE-001

任何进入目标 equality 的 P
χ
mr
	​

 必须带：

uv_pole_derived = true
ir_nonexceptional = true
tensor_space = FOUR | HAT | TILDE
source_normal_form_hash

没有 IntegralPoleCompiler certificate 的 graph 不得进入 SD pole sum。

会直接导致不严谨的 gaps
1. Q(i) coefficient claim

Full N=4 含
2
	​

。只用 Q(i) 会迫使
2
	​

 退化为 string，破坏 exact cancellation。

2. “partially contracted physical graph”

若存在 unsaturated quantum port，它不是 graph。必须改成 Wick-complete、D-unreduced。

3. Graph coefficient 与 symmetry factor 双重输入

若 labeled pairings 已求和，再除 automorphism factor，会重复除 symmetry。

4. unique amplitude 没有 canonical routing

Loop shift 产生多个不同 integrand serialization。必须固定 spanning tree/chord routing。

5. Generic IBP rewrite

IBP 本身生成 exact two-cycle，无法 termination。

6. Numeric matrix oracle 被当作 proof

有限 momentum samples 不能证明 symbolic polynomial identity。

7. Matter collapse 写成 identity

Chiral edge cut 给 Π
±
	​

，不是 full superspace identity。

8. Literal explicit/cut bijection

Raw term counts 不相等时，set bijection 不存在。需要 quotient-space linear equivalence。

9. Explicit 与 collapsed 同时求和

这是直接 double counting。

10. 缺少 PoleCompiler

三个 proposed compilers 停在 pre-integration numerator，不能证明目标 pole equality。

11. Chirality 与 IBP phase 混合

提前使用 chirality 会错误删除本应先作用于 propagator/projector 的 derivative。

12. Scaleless tadpole 直接记为零

必须先记录其 UV/IR status；不能让

0
DRED
	​


参与 ordinary UV pole cancellation proof。

Final architecture verdict
SupergraphCompiler
AmplitudeCompiler
DAlgebraCompiler
IntegralPoleCompiler
SD basis proof
	​

: viable after Wick-complete typing and graph-weight repair,
: viable after canonical routing and exact factor ledger,
: viable only as phased terminating compiler, not generic IBP rewrite,
: mandatory additional stage,
: must be linear quotient equivalence, not assumed raw bijection.
	​

	​


不存在已知的 genuine mathematical obstruction。剩余困难是 finite combinatorics、graded rewriting、typed kernel composition 与 basis-equivalence certification；这些都可 machine-check。但在 explicit I
3
	​

S
3
	​

/I
2
	​

S
4
	​

/I
4
	​

 graphs 被真正编译、其 coefficients 被逐项求出、并通过

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


之前，aggregate contact equality 仍不能提升为 basis-resolved Ward closure。
