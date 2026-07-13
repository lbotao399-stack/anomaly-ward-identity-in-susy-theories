# GPT Pro gap review, round 2: exact response

Status: `EXTERNAL_GAP_REVIEW_ONLY`

This transcript has no formula authority. Every usable claim requires an independent Project-frame derivation and executable certificate.

记号与 assumptions
∇
ˉ
α
˙
	​

≡
∇
α
˙
	​

,F
αβ
	​

:=∇
(α
	​

W
β)
	​

,
F
α
˙
β
˙
	​

	​

:=
∇
ˉ
(
α
˙
	​

W
β
˙
	​

)
	​

,
E:=∇
α
W
α
	​

=
∇
ˉ
α
˙
	​

W
α
˙
.

采用

ε
+−
	​

=1,ε
+−
=−1,

以及 standard 4d N=1 gauge-covariant algebra

{∇
α
	​

,∇
β
	​

}=0,{
∇
ˉ
α
˙
	​

,
∇
ˉ
β
˙
	​

	​

}=0,
{∇
α
	​

,
∇
ˉ
β
˙
	​

	​

}=−2iD
α
β
˙
	​

	​

,
∇
ˉ
α
˙
	​

W
β
	​

=0,∇
α
	​

W
β
˙
	​

	​

=0.

以下涉及 c
ABC
	​

 symmetry 的结论使用：

c
ABC
	​

=f
ABC
	​

=f
[ABC]
	​

	​


with indices lowered by an invariant metric。若 c 不是 structure constant，则 candidate 的 A,B symmetry 本身仍是缺失 datum。标准 superspace identities 与 background-superfield quantization 可见经典 superspace construction。
arXiv

0. Immediate exact audit

存在两个独立的 algebraic obstructions。

0.1 Seed 是 pure-N=1 EOM descendant

由

E=∇
α
W
α
	​

=−∇
−
	​

W
+
	​

+∇
+
	​

W
−
	​

,

以及 ∇
+
2
	​

=0，得到

∇
+
	​

E=−∇
+
	​

∇
−
	​

W
+
	​

=∇
−
	​

∇
+
	​

W
+
	​

=∇
−
	​

X.

因此

I
AB
=(∇
+
	​

E)
A
X
B
+X
A
(∇
+
	​

E)
B
	​


且

I
AB
=I
BA
	​

.

所以若 physical quotient 确实除以 pure-gauge N=1 EOM

E=0,

则

[I]
EOM
	​

=0
	​

.

在 BV/Koszul–Tate complex 中，

E
A
=δ
KT
	​

V
∗A
,∇
+
	​

E
A
=δ
KT
	​

(∇
+
	​

V
∗A
)+connection-antifield terms,

故 source-linear seed 位于 EOM/BRST-exact ideal。

这产生一个二选一：

physical on-shell cohomology:
off-shell EOM Ward identity:
	​

[I]=0,
I must be retained, and one must not quotient by Q
EOM
	​

.
	​


不能同时把 I 当作 nontrivial boundary class，又在同一 complex 中 quotient by EOM。

0.2 Displayed candidate 与 seed 位于不同 A,B sectors

令

Y
α
˙
E
	​

:=D
+
	​

α
˙
	​

X
E
,∣Y∣=0,
B
DE
:=
W
α
˙
D
	​

Y
E
α
˙
−Y
D
α
˙
W
α
˙
E
	​

.

因为 Y even、
W
 odd，

B
ED
=−B
DE
.

再定义

T
AB;DE
	​

=f
ACD
	​

f
BCE
	​

.

则

T
BA;DE
	​

=f
BCD
	​

f
ACE
	​

=T
AB;ED
	​

.

故

O
cov
BA
	​

	​

=T
BA;DE
	​

B
DE
=T
AB;ED
	​

B
DE
=T
AB;DE
	​

B
ED
=−T
AB;DE
	​

B
DE
,
	​


即

O
cov
AB
	​

=−O
cov
BA
	​

	​

.

因此

J
AB
	​

I
AB
=J
(AB)
	​

I
AB
,

而

J
AB
	​

O
cov
AB
	​

=J
[AB]
	​

O
cov
AB
	​

.

Diagonal gauge action 与 flip A↔B commute，所以

Sym
2
Adj和Λ
2
Adj

是 invariant subcomplexes，不能通过 renormalization mixing 相互转换。

O
cov
	​

 cannot be the nonlinear completion of the displayed seed
	​


under the standard f
ABC
	​

 interpretation。

0.3 Spin projector is missing

若 + 和 − 是 literal undotted spinor components，则

X=∇
+
	​

W
+
	​

=F
++
	​


是 (1,0) 的 highest-weight component，而不是 Lorentz scalar。于是

F
++
	​

F
++
	​


具有 m
L
	​

=2，作用 ∇
−
	​

 后具有 m
L
	​

=3/2，不能属于 j
L
	​

=1/2。

同样，

W
α
˙
	​

D
+
	​

α
˙
X

在乘上 X∈(1,0) 后包含

(
2
1
	​

,0)⊗(1,0)=(
2
3
	​

,0)⊕(
2
1
	​

,0),

但 displayed formula 没有给出 separating projector。

因此必须提供 project spinors u
±
α
	​

 及明确 intertwiner

P
proj
	​

:projected words⟶(
2
1
	​

,0).

以下 basis census 对 Spin projection 保留抽象 projector P
proj
	​

。

1. Complete covariant monomial census
1.1 Dimension/r/parity equations

假定 standard conjugate weight

r(
∇
ˉ
α
˙
	​

)=+1.

令

(n
W
	​

,n
W
	​

;n
∇
	​

,n
∇
ˉ
	​

;n
D
	​

)

分别计数 letters。约束为

3(n
W
	​

+n
W
	​

)+n
∇
	​

+n
∇
ˉ
	​

+2n
D
	​

=9,
n
W
	​

−n
W
	​

−n
∇
	​

+n
∇
ˉ
	​

=−1,
n
W
	​

+n
W
	​

+n
∇
	​

+n
∇
ˉ
	​

≡1(mod2),
n
W
	​

+n
W
	​

≥1.

全部 nonnegative integer solutions 为

(0,1;0,0;3),(0,1;1,1;2),(0,1;2,2;1),(0,1;3,3;0),
(0,2;0,1;1),(0,2;1,2;0),
(1,0;2,0;2),(1,0;3,1;1),(1,0;4,2;0),
(1,1;1,0;1),(1,1;2,1;0),
(1,2;0,0;0),(2,0;3,0;0).
	​

1.2 Normal-ordered skeletons

反复使用

∇
α
	​

∇
ˉ
α
˙
	​

=−
∇
ˉ
α
˙
	​

∇
α
	​

−2iD
α
α
˙
	​

,

并把 derivative commutators 产生的 W,
W
 放入 higher-field sectors，可取六个 canonical content sectors：

S
1
	​

S
2
	​

S
3
	​

S
4
	​

S
5
	​

S
6
	​

	​

W
D
3
W
2
∇
ˉ
D
W∇
2
D
2
W
W
∇D
W
W
2
W
2
∇
3
	​

	​


其中：

S
4
	​

⊃P
proj
	​

[
W
α
˙
	​

D
β
α
˙
F
αβ
	​

]

包含 displayed candidate 的 bilinear Lorentz skeleton；

S
6
	​

⊃P
proj
	​

[F∇F]

包含 seed；

S
5
	​


是所有 cubic field-strength candidates 的唯一 allowed chirality sector。

1.3 Cubic field-strength audit

三个 field strengths 已经耗尽 dimension：

3×
2
3
	​

=
2
9
	​

.

因此不允许额外 derivatives。

W
3
W
a
C
	​

W
Db
W
b
E
	​

:r=1+1+1=3.

虽然 dimension、parity、left-spinor index 均可匹配，但

r=3

=−1
	​


故严格排除。

W
2
W
r=1+1−1=1,

且保留一个 dotted spinor index，排除。

W
W
2
r=1−1−1=−1,
[W
α
	​

W
β
˙
	​

	​

W
β
˙
	​

]=(
2
1
	​

,0),
∣W
W
2
∣=1.

此外

W
β
˙
	​

D
	​

W
E
β
˙
	​

=
W
β
˙
	​

E
	​

W
D
β
˙
	​

,

所以 color tensor 只取 D,E symmetric part。

一个 universal symmetric-output candidate 为

Q
α
AB
	​

=f
(A
CD
	​

W
α
C
	​

(
W
β
˙
	​

B)
	​

W
D
β
˙
	​

)
	​


并满足

[Q]=
2
9
	​

,∣Q∣=1,r(Q)=−1,Q
AB
=Q
BA
.

它从三次 background order 开始：

ℓ
2
	​

[Q]=0
	​

.

因此任何 injectivity theorem 必须显式证明

[Q]=0mod EOM, exact, IBP, identities,

不能只检查 W
3
。

W
3
r=−3,

且没有 free left-spinor index，排除。

1.4 Exact abstract basis

对每个 skeleton S
s
	​

，完整 basis 必须写成

M
s,λ,τ,π
	​

=∫dμ
J
	​

J
AB
	​

T
τ
AB
	​

C
1
	​

⋯C
m
	​

	​

P
λ
	​

[W
C
1
	​

⋯W
C
m
	​

;π].

其中：

P
λ
	​

 是

Hom
Spin(4)
	​

(R
S
s
	​

	​

,(
2
1
	​

,0))

的 basis；

T
τ
	​

 是

Hom
G
	​

(Adj
⊗m
,R
J
∗
	​

)

的 invariant-color basis；

π 标记 covariant derivatives 的 distributions 和 orderings；

R
J
	​

=Sym
2
Adj、Λ
2
Adj 或 full tensor product。

例如：

S
1
	​

:T
τ
	​

∈Hom
G
	​

(Adj,R
J
∗
	​

),
S
4
	​

:T
τ
	​

∈Hom
G
	​

(Adj
⊗2
,R
J
∗
	​

),
S
5
	​

:T
τ
	​

∈Hom
G
	​

(Adj⊗Sym
2
Adj,R
J
∗
	​

).

因此 gauge algebra 未指定时，basis dimension 本身未定义。例如：

f
AB
	​

C

提供 Adj→Λ
2
Adj，而某些 groups 另有

d
AB
	​

C
:Adj→Sym
2
Adj.
1.5 IBP is not closed without source jets

对 odd spinor derivative d=∇
α
	​

，因为 ∣J∣=1，

0=∫dμ
J
	​

d(JO)=∫dμ
J
	​

[(dJ)O−J(dO)],

所以

∫J∇
α
	​

O=∫(∇
α
	​

J)O
	​

.

对 even vector derivative：

∫JD
α
α
˙
	​

O=−∫(D
α
α
˙
	​

J)O
	​

.

因此对 local source，单纯的 “pure-gauge monomial basis” 在 IBP 下不闭合；必须加入

J,∇J,
∇
ˉ
J,DJ,…

的 source-jet module。

若假定

∇J=
∇
ˉ
J=DJ=0,

则这是 constant spurion，而不是用于定义 local insertion 的一般 source。

2. Closed, exact and EOM matrices
2.1 Source BRST transformation

采用 left-ordered ghost convention：

sY
I
=c
a
(t
a
	​

)
I
J
	​

Y
J
.

由于 J odd，

s(J
I
	​

Y
I
)=(sJ
I
	​

)Y
I
−J
I
	​

sY
I
.

Gauge invariance 要求

sJ
I
	​

=−c
a
J
J
	​

(t
a
	​

)
J
I
	​

	​

.

对 tensor source：

sJ
AB
	​

=−c
a
[(t
a
	​

)
C
A
	​

J
CB
	​

+(t
a
	​

)
C
B
	​

J
AC
	​

].
	​

2.2 Matrix complex

先取 raw source-linear ghost-zero basis M
i
	​

，并以 relation matrix

R
alg
	​

=[R
graded
	​

,R
Bianchi
	​

,R
Jacobi
	​

,R
projector
	​

,R
IBP
	​

]

形成

V
ˉ
0
	​

=V
0
	​

/imR
alg
	​

.

取 ghost-one basis N
μ
	​

。Closed matrix 定义为

B
Σ
	​

M
i
	​

=C
μi
	​

N
μ
	​

mod d.

故

Z
0
=kerC.

取 ghost-minus-one、nonminimal/source-doublet generators K
p
	​

：

B
Σ
	​

K
p
	​

=E
ip
	​

M
i
	​

mod EOM,d.

取 EOM generators

E
q
	​

=∫dμ
J
	​

JR
q
	​

r
δΦ
r
δΣ
	​

,

并展开

E
q
	​

=Q
iq
	​

M
i
	​

mod d.

于是 physical quotient 为

H
phys
	​

=
imE+imQ
kerC
	​

	​

.

在完整 BV complex 中 Q 是 Koszul–Tate part of exactness；若把 E,Q 分开 bookkeeping，必须避免 double counting。Local BRST cohomology precisely uses this closed/exact/Koszul–Tate structure。
arXiv
+1

若 relations 已经消元且

C[E Q]=0,

则

dimH
phys
	​

=n
0
	​

−rankC−rank[E Q]
	​

.
2.3 DRED temporary complex

写

M
I
	​

=(P
i
	​

,E
i
^
	​

),

其中 P
i
	​

 physical，E
i
^
	​

 evanescent。若

E
i
^
	​

=ϵR
i
^
	​

j
P
j
	​

+O(ϵ
2
)

且 one-loop mixing 为

Z=(
Z
PP
	​

Z
EP
	​

	​

Z
PE
	​

Z
EE
	​

	​

),

则 finite physical mixing 包含

Z
phys
(0)
	​

=Z
PP
(0)
	​

+Z
PE
(−1)
	​

R
	​

.

所以 C,E,Q 必须先在 physical-plus-evanescent module 上计算，再执行 finite projection。Consistent DRED admits a Quantum Action Principle，但 symmetry breaking 和 evanescent insertions 必须保留到 renormalized limit。
arXiv
+1

2.4 Rank verdict

从给定 data 不能计算实际 rank。

接受声明的 Project spin 为外部 axiom 后，第一个缺失的 algebraic datum 是

g及允许的 invariant tensor algebra
	​


因为没有它，连 n
0
	​

=dim
V
ˉ
0
	​

 都未定义。

其后仍需：

P
proj
	​

,dμ
J
	​

,J-jet constraints,R
J
	​

=Sym
2
Adj or full,pure N=1 versus full N=4 EOM
	​


以及完整 evanescent basis。

因此：

rankH
phys
	​

 is not determined by the locked data.
	​


并且不存在依据支持 “rank one generated by O
cov
	​

”：

[I]
EOM
	​

=0,I∈Sym
2
Adj,O
cov
	​

∈Λ
2
Adj.
3. Fixed quadratic jet and injectivity

令 L 为 fixed quadratic-jet matrix：

ℓ
2
	​

[M
i
	​

]=L
ρi
	​

q
ρ
	​

,

其中 q
ρ
	​

 是 two-background local-jet basis。

Exact/EOM/IBP jets 在 target 中形成 trivial subspace

B
2
	​

=im[ℓ
2
	​

E,ℓ
2
	​

Q,ℓ
2
	​

R
alg
	​

].

诱导 map 为

L
ˉ
:H
phys
	​

⟶Q
2
	​

/B
2
	​

.

精确 injectivity condition：

ker
L
ˉ
=0⟺{v∈kerC:Lv∈B
2
	​

}=im[E Q].
	​


若选择 canonical representatives 使

L[E Q]=0,

则简化为

kerC∩kerL=im[E Q].
	​


进一步，若 n
0
	​

=dim
V
ˉ
0
	​

：

rank(
C
L
	​

)=n
0
	​

−rank[E Q]
	​


等价于 injectivity。

3.1 Explicit quadratic jets

定义 linearized fields

w
α
	​

[V]=−
4
1
	​

D
ˉ
2
D
α
	​

V,
w
α
˙
	​

[V]=−
4
1
	​

D
2
D
ˉ
α
˙
	​

V,
x[V]=D
+
	​

w
+
	​

[V],e[V]=D
α
w
α
	​

[V].

Seed：

ℓ
2
	​

[I]
AB
(V
1
	​

,V
2
	​

)=
2
1
	​

σ∈S
2
	​

∑
	​

D
−
	​

[x
A
[V
σ(1)
	​

]x
B
[V
σ(2)
	​

]]
	​


并且

D
−
	​

x=D
+
	​

e,

所以其 quadratic jet 本身也是 linearized EOM descendant。

Candidate：

ℓ
2
	​

[O
cov
	​

]
AB
(V
1
	​

,V
2
	​

)=
	​

2
1
	​

f
ACD
	​

f
BCE
	​

σ∈S
2
	​

∑
	​

[
w
α
˙
D
	​

[V
σ(1)
	​

]∂
+
	​

α
˙
x
E
[V
σ(2)
	​

]
−∂
+
	​

α
˙
x
D
[V
σ(1)
	​

]
w
α
˙
E
	​

[V
σ(2)
	​

]].
	​

	​


该 jet 位于 Λ
2
Adj output sector。

Cubic family 满足

ℓ
2
	​

[Q]=0
	​


identically。故证明 kerℓ
2
	​

=0 必须证明所有这类 cubic classes 属于 exact/EOM ideal。

3.2 “Lowest nonzero jet” does not prove injectivity

定义

ν(O)=min{n:ℓ
n
	​

[O]

=0}.

则 ν 不是 linear：

ν(O
1
	​

+O
2
	​

)

可因 leading-jet cancellation 跳变。因此 class-dependent map

[O]↦ℓ
ν(O)
	​

[O]

不是 fixed linear map，也不能排除

ν(O)=3,4,…

的 nontrivial classes。

唯一相关 map 是预先固定的

ℓ
2
	​

	​

.
4. Odd-source one-loop formula

令所有 quantum fields 在 doubled field bundle 中，使

Γ
(1)
=
2
1
	​

STrlogH

是统一 formula。设

H=H
B
	​

+JI,H
B
	​

=H
0
	​

+H
+
	​

[V].

因为 J odd 而 JI even，

∣I∣=1,∣H
B
	​

∣=∣G
B
	​

∣=0.

定义 left/right derivatives：

δΓ=δJ
δJ
δ
Γ
	​

=
δJ
Γ
δ
	​

δJ.

由于 Γ even、J odd，

δJ
Γ
δ
	​

=−
δJ
δ
Γ
	​

.
	​

4.1 Source derivative
δH=δJI.

于是

δΓ
(1)
=
2
1
	​

STr(G
B
	​

δJI).

G
B
	​

 even，故 cyclically：

STr(G
B
	​

δJI)=δJSTr(IG
B
	​

).

所以

δJ
δ
Γ
(1)
	​

	​

J=0
	​

=
2
1
	​

STr(IG
B
	​

)
	​


以及

δJ
Γ
(1)
δ
	​

	​

J=0
	​

=−
2
1
	​

STr(IG
B
	​

).
	​

4.2 All-background expansion
G
B
	​

=G
0
	​

−G
0
	​

H
+
	​

G
0
	​

+G
0
	​

H
+
	​

G
0
	​

H
+
	​

G
0
	​

−⋯.

因此

Γ
J
(1),L
	​

=
2
1
	​

k=0
∑
∞
	​

(−1)
k
STr[IG
0
	​

(H
+
	​

G
0
	​

)
k
].
	​


没有额外 1/(k+1)：它由 log expansion 中 1/(k+1) 与 unique J-vertex 的 k+1 个 cyclic positions 精确抵消。

Graded cyclicity 为

STr(A
1
	​

⋯A
m
	​

)=(−1)
∣A
1
	​

∣(∣A
2
	​

∣+⋯+∣A
m
	​

∣)
STr(A
2
	​

⋯A
m
	​

A
1
	​

).

这里 unique I odd，而所有 G
0
	​

,H
r
	​

 even，所以移动 I 绕 loop：

(−1)
1⋅0
=+1.

唯一 universal expansion sign 是

(−1)
k
	​

.

Species statistics、fermion-loop signs 和 mixed-block Koszul signs 已包含于 STr 与 supermatrix composition，不得再手工附加第二个 “fermion-loop minus”。

4.3 Exact labeled n-background formula

对 S⊂{1,…,n} 定义

H
S
	​

=
i∈S
∏
	​

δV
i
	​

δ
	​

H
+
	​

[V]
	​

V=0
	​

,
I
S
	​

=
i∈S
∏
	​

δV
i
	​

δ
	​

I[V]
	​

V=0
	​

.

则

Γ
J;n
(1),L
	​

(1,…,n)=
	​

2
1
	​

k=0
∑
n
	​

(−1)
k
S
0
	​

⊔S
1
	​

⊔⋯⊔S
k
	​

=[n]
S
i
	​


=∅, i≥1
	​

∑
	​

STr[I
S
0
	​

	​

G
0
	​

H
S
1
	​

	​

G
0
	​

⋯H
S
k
	​

	​

G
0
	​

].
	​

	​


这是 ordered set-partition sum；因此 symmetry factors 已完全固定。

4.4 Complete two-background family

令 1,2 为 labeled external backgrounds：

Γ
J;12
(1),L
	​

=
2
1
	​

STr[
	​

I
12
	​

G
0
	​

−I
1
	​

G
0
	​

H
2
	​

G
0
	​

−I
2
	​

G
0
	​

H
1
	​

G
0
	​

−I
0
	​

G
0
	​

H
12
	​

G
0
	​

+I
0
	​

G
0
	​

H
1
	​

G
0
	​

H
2
	​

G
0
	​

+I
0
	​

G
0
	​

H
2
	​

G
0
	​

H
1
	​

G
0
	​

]
+CT
12
	​

+Jac
12
	​

.
	​

	​


对应 topology classes：

I
0
	​

H
1
	​

H
1
	​

,I
0
	​

H
2
	​

,I
1
	​

H
1
	​

,I
2
	​

,CT
2
	​

.

这五类在以下条件下 exhaustive：

H 是 full doubled Hessian endomorphism；

vector、matter、auxiliary、gauge-fixing、FP、NK、source-partner fields 全部包含在 field bundle；

所有 mixed Hessian blocks 均保留；

H 对 J 的 source-linear part 确实是 JI；

source-dependent measure/Jacobian 被包括在 Jac
2
	​

 或 CT
2
	​

；

CT
2
	​

 包含 physical、evanescent、source-renormalization 和 symmetry-restoring counterterms。

Mixed blocks 不产生新的 word topology；它们产生相同 words 上不同的 closed species paths。

FP/NK contribution 的 exact criterion 是：

∃ closed block path containing I
s
	​

 and an FP/NK block.
	​


若

I
FP
	​

=I
NK
	​

=0

且 ghost number 禁止 physical–ghost mixed Hessian blocks，则

δJ
δ
	​

Γ
FP/NK
(1)
	​

=0.

若 source-extended gauge fixing 或 BRST partners 使 I 具有 ghost/NK blocks，则必须计入。

在 +-sector 中 inverse 必须由

K
+
	​

G
+
	​

=δ
+
	​

,K
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


定义；在完成 D-algebra 前不能把 K
+
	​

 非条件地替换成 scalar □。

5. Global/SUSY anomaly versus consistent gauge anomaly
5.1 Exact background gauge Ward identity

设 s
g
	​

 为 background-gauge BRST，q 为 global/supersymmetry Ward differential。

若

S
g
	​

(Γ)=0,

而

S
q
	​

(Γ)=ℏΔ
q
(1)
	​

+O(ℏ
2
),

则 mixed consistency gives

B
g
	​

Δ
q
(1)
	​

+B
q
	​

Δ
g
(1)
	​

=0.

由于

Δ
g
(1)
	​

=0,

有

B
g
	​

Δ
q
(1)
	​

=0.
	​


因此 global/SUSY anomaly 可以选择为 background-gauge covariant local cocycle。

Gauge-preserving counterterm C 只改变

Δ
q
(1)
	​

⟶Δ
q
(1)
	​

+B
q
	​

C,

不会把 exact background Ward identity 变成 gauge anomaly。

5.2 Consistent gauge anomaly

若

S
g
	​

(Γ)=ℏA
cons
(1)
	​

,

则

B
g
	​

A
cons
(1)
	​

=0
	​


是 Wess–Zumino consistency condition。

Consistent current 是 functional derivative：

J
cons
	​

=
δV
δΓ
	​

.

Covariant current 定义为

J
cov
	​

=J
cons
	​

+K
BZ
	​

[V].

K
BZ
	​

 是 local Bardeen–Zumino current；通常 J
cov
	​

 不再是某个 effective action 的 integrable functional derivative。Consistent/covariant currents 及其 BZ difference 正是这一区分。
arXiv

5.3 When box/pentagon representatives may shift

若引入 current source J，current redefinition

Γ
J
	​

⟶Γ
J
	​

+∫dμ
J
	​

JK
BZ
	​

[V]

导致

δ
BZ
	​

Γ
J,3
	​

=ℓ
3
	​

[K
BZ
	​

],
δ
BZ
	​

Γ
J,4
	​

=ℓ
4
	​

[K
BZ
	​

].

所以 box/pentagon local representatives 改变当且仅当

ℓ
3
	​

[K
BZ
	​

]

=0orℓ
4
	​

[K
BZ
	​

]

=0.
	​


这种 shift 在本问题中只合法于：

background gauge symmetry 本身 anomalous；或

正在把 consistent gauge-current insertion 改定义成 covariant current；或

global/SUSY Ward identity 因另一个 gauge anomaly 通过 mixed consistency 被迫包含 BZ term。

若 background gauge Ward identity exact：

S
g
	​

(Γ)=0,

则 gauge-noncovariant BZ shift 会破坏该 identity，不能作为 ordinary scheme choice。此时允许的只是 gauge-invariant local counterterms；它们是 global-exact/BRST-exact representative changes，不是 consistent-to-covariant BZ conversion。

6. Chiral–vector representation bridge
6.1 Raw Hessian transforms by congruence

令 quantum fluctuations 满足

Ψ
C
	​

=S
R
	​

Ψ
V
	​

,S
R
	​

 independent of J.

对 two-lower-index Hessian

H
MN
	​

=
δΨ
M
δ
	​

S
δΨ
N
δ
	​

,

正确 transformation 是

H
C
	​

=S
R
−st
	​

H
V
	​

S
R
−1
	​

.
	​


因此对 raw second derivative，单纯 similarity statement 一般不成立。

令 field-space pairing G 满足

G
C
	​

=S
R
−st
	​

G
V
	​

S
R
−1
	​

.

定义 one-up-one-down endomorphism Hessian

H:=G
−1
H.

则

H
C
	​

=S
R
	​

H
V
	​

S
R
−1
	​

.
	​


所以题中 bridge statement 必须理解为 endomorphism Hessian，而不是 raw bilinear kernel。

6.2 Insertion kernel

因为 S
R
	​

 与 J 无关，

I
C
	​

=
δJ
δ
H
C
	​

	​

	​

J=0
	​

=S
R
	​

δJ
δ
H
V
	​

	​

	​

J=0
	​

S
R
−1
	​

.

故

I
C
	​

=S
R
	​

I
V
	​

S
R
−1
	​

.
	​


若 S
R
	​

 依赖 J，则会多出

[(δ
J
	​

S
R
	​

)S
R
−1
	​

,H
C
	​

]

型 commutator，题中 formula 不再成立。

6.3 Propagator kernel

由

H
C
	​

G
C
	​

=1

得到

G
C
	​

=S
R
	​

G
V
	​

S
R
−1
	​

.
	​


Kernel form：

G
C
	​

(z,z
′
)=S
R
	​

(z)G
V
	​

(z,z
′
)S
R
−1
	​

(z
′
).
	​


所有 endpoint bridges 在 closed loop 中 telescope。

6.4 Regulated-supertrace conditions

需要 exact similarity invariance：

STr
reg
	​

(S
R
	​

AS
R
−1
	​

)=STr
reg
	​

A.
	​


等价 acceptance conditions：

STr
reg
	​

(AB)=(−1)
∣A∣∣B∣
STr
reg
	​

(BA),

并且 regulator 本身 intertwines：

R
C
	​

=S
R
	​

R
V
	​

S
R
−1
	​

.

在 DRED 实现中必须检查：

loop-momentum routing invariance,
superspace integration by parts,
finite color-trace cyclicity,
all ϵ/ϵ remnants retained,
no regulator-induced endpoint term.

若 regulated trace 的 cyclicity defect 为

Δ
cyc
	​

(A,B):=STr
reg
	​

(AB)−(−1)
∣A∣∣B∣
STr
reg
	​

(BA),

则 representation bridge proof 需要

Δ
cyc
	​

=0
	​


或证明该 defect 是相同的 source-independent local counterterm。

6.5 Jacobian condition

Field redefinition 的 Berezinian 为

J[S
R
	​

]=exp(STr
reg
	​

logS
R
	​

).

Full effective-action equality 要求

STr
reg
	​

logS
R
	​

=0
	​


modulo a common local counterterm。

对于 source-linear insertion equality，较弱条件足够：

δJ
δ
	​

logJ[S
R
	​

]=0.
	​


此外 gauge-fixing、FP、NK operators 也必须分别 obey the same bridge。若两种 representations 使用不相互 conjugate 的 gauge-fixing fermions，则只能证明 BRST-equivalence，不能证明 Hessian-by-Hessian similarity。

7. Independent-connection filtration

定义

deg
A
	​

∂=0,deg
A
	​

A=1,
deg
A
	​

W≤2,deg
A
	​

(∇Y)≤deg
A
	​

Y+1,
deg
A
	​

(YZ)=deg
A
	​

Y+deg
A
	​

Z.
7.1 Classical seed
deg
A
	​

X=deg
A
	​

(∇
+
	​

W
+
	​

)≤3.

所以

deg
A
	​

(X
A
X
B
)≤6,
deg
A
	​

I≤7.
	​


Leading symbol 为

σ
7
	​

(I)=ad
A
−
	​

Adj⊗Adj
	​

(σ
3
	​

(X)⊗σ
3
	​

(X)).

Jacobi/Bianchi alone 不普遍令此 symbol 为零。因此作为 off-shell connection polynomial，bound 7 不被 mandatory identities 降低。

但是在 pure-N=1 EOM quotient 中：

[I]=0.

这是 whole-class elimination，不是把 degree 7 降到 degree 6。

7.2 Candidate
deg
A
	​

W
≤2,
deg
A
	​

(DX)≤4.

故

deg
A
	​

O
cov
	​

≤6.
	​


其 leading symbol 为

σ
6
	​

(O
cov
	​

)
AB
=f
ACD
	​

f
BCE
	​

[
−
	​

σ
2
	​

(
W
)
D
ad
A
+
α
˙
	​

	​

σ
3
	​

(X)
E
ad
A
+
α
˙
	​

	​

σ
3
	​

(X)
D
σ
2
	​

(
W
)
E
].
	​


其 color tensor 不因 Jacobi 普遍消失。例如对 SU(2)：

ε
ACD
	​

ε
BCE
	​

=δ
AB
	​

δ
DE
	​

−δ
AE
	​

δ
DB
	​

.

与 antisymmetric B
DE
 contraction 后：

ε
ACD
	​

ε
BCE
	​

B
DE
=B
AB
,

generically nonzero。因此 degree-six bound 在 Λ
2
Adj sector 中是 sharp。

但对 seed-relevant source J
(AB)
	​

：

J
(AB)
	​

O
cov
AB
	​

=0.

所以 candidate 在 relevant symmetric source sector 不是 “degree reduced”，而是整个 functional absent。

8. Manifest N=1 versus hidden N=4

Manifest-N=1 proof 只可使用：

V,Φ
i
,
Φ
ˉ
i
	​


的 manifest superspace transformations、background gauge BRST、N=1 superfield identities 和 source-extended ST identity。

不能以 hidden N=4 去删除 Q 等 classes，除非先构造 extended complex。

必须增加：

全部 fields 的 antifields：

V
∗
,Φ
i
∗
	​

,
Φ
ˉ
∗i
,c
∗
,…;

hidden-supersymmetry constant ghosts：

ϵ
iα
,
ϵ
ˉ
i
α
˙
	​

;

translation ghost：

ξ
α
α
˙
;

必要时 SU(4)
R
	​

 ghosts/sources；

每个 nonlinear hidden-SUSY variation 的 external source：

K
δ
Q
	​

V
	​

,K
δ
Q
	​

Φ
	​

,K
δ
Q
	​

c
	​

,…;

encoding on-shell closure 的 quadratic-antifield terms；

separating gauge BRST 与 supersymmetry ST identities 的 shadow fields/BRST doublets；

I 的完整 hidden-N=4 source multiplet：

J,J
Φ
	​

,J
ΦΦ
	​

,…;

matter-containing operator basis，因为 hidden supersymmetry 将 pure-gauge monomials 映到 matter monomials；

DRED-induced hidden-SUSY breaking insertion

Δ
Q
ev
	​


及 restoring counterterms。

需要证明 extended algebra：

S
s
	​

(Γ)=0,S
Q
	​

(Γ)=0,
{B
s
	​

,B
Q
	​

}=0,
B
Q
2
	​

=translation+gauge transformation+controlled EOM terms.

Shadow-field formalism正是用于把 gauge 与 supersymmetry Slavnov–Taylor identities 分离，并处理 N=4 的 nonlinear/on-shell closure。
arXiv
+1

特别地，full N=4 vector EOM schematic form 为

E=M(Φ,
Φ
ˉ
).

故

I=(∇
+
	​

M)
A
X
B
+X
A
(∇
+
	​

M)
B

在 full theory 中成为 matter-containing operator。因而：

pure-gauge EOM quotient is not closed under hidden N=4.
	​

Final gap table
Issue	Exact status
Seed A,B symmetry	I
AB
=I
BA

Candidate A,B symmetry	O
cov
AB
	​

=−O
cov
BA
	​

, assuming c=f
Seed modulo pure-N=1 EOM	[I]=0
W
3
 family	excluded by r=3
W
W
2
 family	allowed; fixed quadratic jet vanishes
Physical cohomology rank	undetermined
First missing rank datum	specified g and invariant-tensor module
Additional missing data	Project spin projector, source measure/jets, EOM choice, evanescent basis
Two-leg graph topology list	exhaustive conditionally, with full Hessian and Jac
2
	​

 included
Bridge	similarity only for endomorphism Hessian; raw Hessian transforms by congruence
Connection bounds	7 and 6 remain sharp off shell; seed dies by EOM, candidate dies in symmetric source sector
Hidden N=4	unavailable until extended ST/source complex is constructed
Conditional theorem that remains logically available

令 R
J
	​

=Sym
2
Adj，并构造完整 physical-plus-evanescent source complex。若显式计算证明

dimH
phys
	​

=1,

且 fixed quadratic-jet map 满足

ker
ℓ
ˉ
2
	​

=0,

则任意 local source-linear anomaly class 满足

[Δ
(1)
]=c
△
	​

[C].

但该 theorem 还要求：

[I]

=0

in the chosen complex，以及

C∈Sym
2
Adj.

当前 locked setup 在 standard interpretation 下不满足这两个 prerequisites：

[I]
EOM
	​

=0,O
cov
	​

∈
/
Sym
2
Adj.
	​


因此目前能严格得到的是：

No rank-one or “one triangle determines all dressings” theorem has yet been established for this seed.
	​


并且 displayed O
cov
	​

 不能作为该 symmetric seed 的 proposed unique covariant completion。
