# Step 5 one-loop covariant-completion review — GPT Pro round 1 response

> External review only. No numerical coefficient or claimed theorem is imported into the Project. The response is preserved verbatim from the browser DOM readback for gap auditing.

记号与必须先固定的概念

z=(x,θ,
θ
ˉ
)，d
8
z=d
4
xd
2
θd
2
θ
ˉ
。

V：background prepotential；v：quantum prepotential。

∇
A
	​

：background-covariant superspace derivative；∇
A
	​

：full background-plus-quantum derivative。

L
X
	​

Y=[X,Y]：adjoint action。

J
I
	​

：coupled to O
I
	​

 的 external source；I denotes the complete Lorentz, color, R-symmetry representation。

Γ
O,m
	​

：one O-insertion 加 m 个 external background-V legs；因此

Γ
O,2
	​

=triangle level,Γ
O,3
	​

=box level,Γ
O,4
	​

=pentagon level.

Σ：source-extended classical BV action；B
Σ
	​

：linearized Slavnov–Taylor operator，满足 B
Σ
2
	​

=0。

H
loc
g
	​

(B
Σ
	​

∣d)：ghost number g 的 local BRST cohomology modulo total derivatives、equations of motion 和 BRST-exact terms。

ℓ
2
	​

[X]：local covariant functional X 的 quadratic-background term，即其 abelianized two-leg boundary。

H
r
	​

：quadratic quantum Hessian 中含 r 个 background legs 的 vertex。

I
s
	​

：quadratic insertion kernel 中含 s 个 background legs 的 vertex。

STr：包含 boson/fermion signs 的 functional supertrace。

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

 始终按 project convention 原样使用。

Core verdict

原始 statement 按照“每个 higher-leg one-loop 1PI amplitude 的全部内容都由 triangle 决定”理解，必须 refute：

Background Ward identity fixes longitudinal/contact parts, not arbitrary transverse nonlocal parts.
	​


正确而可能证明的命题只能是：

The complete local, cohomologically nontrivial anomaly term is fixed by the triangle coefficient
	​


并且还必须满足一个关键条件：

kerℓ
2
	​

=0
	​


即不存在一个允许的 local BRST cohomology class，它的 triangle term 为零、但从 box 或更高 background order 开始。

此外：

在 unconstrained V-prepotential expansion 中，completion 是 infinite。
	​


“triangle + box + pentagon”只可能是某个特定 component density，例如 F∧F，在 A
μ
	​

-variables 中的有限展开；它不是一般 superspace-V 结论。

1. Precise conditional theorem
1.1 Effective-action insertion

先引入 source：

S
J
	​

=∫dμ
O
	​

J
I
	​

O
I
,

并定义

Γ
O
I
	​

(z;V)=
δJ
I
	​

(z)
δΓ
	​

	​

J=0,quantum fields=0
	​

.

其 m-background-leg vertex 为

Γ
O,m
I;a
1
	​

…a
m
	​

	​

=
δV
a
1
	​

⋯δV
a
m
	​

δ
m
Γ
O
I
	​

	​

	​

V=0
	​

.

若 I=(A,B) 是 gauge indices，则 J
AB
	​

 必须属于 dual representation，使 pairing J
AB
	​

O
AB
 gauge invariant。若 A,B 是 R-symmetry indices，则 background-gauge action 不作用于它们。这个 distinction 必须先锁定。

1.2 Quantum ST identity

以 condensed BV notation：

S(Γ)=∫dμ
i
	​

δΦ
i
∗
	​

δ
r
	​

Γ
	​

δΦ
i
δ
l
	​

Γ
	​

+∫dμ
c
ˉ
	​

B
δ
c
ˉ
δ
l
	​

Γ
	​

+(sJ)
I
	​

δJ
I
	​

δ
l
	​

Γ
	​

=0.

Tree level：

S(Σ)=0,B
Σ
2
	​

=0.

Differentiating with respect to J gives composite-insertion ST equation：

B
Γ
	​

Γ
O
	​

+ρ
O
	​

(c)Γ
O
	​

=0,

provided sO=ρ
O
	​

(c)O is purely representation-covariant。若 sO contains EOM 或 nonlinear operator mixing，则必须再引入 source for sO。

1.3 Background Ward identity

令 K(z) 为 real background gauge parameter：

δ
K
	​

∇
A
	​

=i[K,∇
A
	​

],δ
K
	​

v=i[K,v],δ
K
	​

J=−Jρ
O
	​

(K).

则 source-extended effective action 必须满足

W
K
	​

Γ=0.

这条 identity 是 higher-background-leg recursion 的直接来源。

Background-field expansion term-by-term 保持 background covariance；标准 nonlinear split 与 background-covariantly chiral FP/Nielsen–Kallosh sectors 可按这一形式构造。
Department of Physics
+1

1.4 Global anomaly versus gauge anomaly

必须区分：

Case G：background gauge symmetry exact

异常属于另一个 global/supersymmetry Ward operator W
X
	​

：

W
X
	​

Γ=
ℓ≥1
∑
	​

ℏ
ℓ
Δ
X
(ℓ)
	​

.

At one loop：

B
Σ
	​

Δ
X
(1)
	​

=0.

引入 constant global ghost η
X
	​

 后，η
X
	​

Δ
X
(1)
	​

 属于 ghost-number-one cohomology。除去 η
X
	​

 后，anomaly density 属于 ghost number zero。

这是 ABJ-like gauge-covariant anomaly density 所需的 framework。

Case A：background gauge symmetry itself anomalous

则

S(Γ)=ℏA
(1)
+⋯,B
Σ
	​

A
(1)
=0,

且 A
(1)
 是 consistent anomaly，不是直接的 covariant anomaly。两者相差 Bardeen–Zumino local functional；superspace consistent anomaly 的 V-expression 一般 nonpolynomial，并存在 homotopy/local-counterterm ambiguity。
arXiv

因此，题设中的“gauge-covariant completion”只有在 Case G 中可以直接成立。

1.5 Exact local-completion theorem

固定：

ghost number；

engineering dimension；

Grassmann parity；

Lorentz +/− weights；

R-charges；

color representation R
O
	​

；

single-trace/multi-trace sector；

source degree J
1
。

令 H
q
	​

 为该 sector 中的 local cohomology，且

ℓ
2
	​

:H
q
	​

⟶{linearized two-background cocycles}

取 quadratic-background term。

Conditional theorem T
loc
	​

.
假定：

background gauge anomaly absent；

DRED-renormalized ST identity 可由 local counterterms 恢复；

one-loop Ward breaking 的 UV-local part 满足 Quantum Action Principle；

local function space restricted to analytic gauge-covariant expressions built from

W,
W
ˉ
,∇,

with bounded engineering dimension；

imℓ
2
	​

 为一维；

kerℓ
2
	​

=0；

BRST-exact、EOM 和 finite source-counterterm ambiguities 已由 normalization conditions 固定。

则存在唯一 cohomology generator C，使

[Δ
X
(1)
	​

]
nontrivial
	​

=c
△
	​

[C],

且

[Γ
O,m
(1)
	​

]
local,nontrivial
	​

=c
△
	​

C
m
	​

∀m≥2.

Proof 只有三步：

c
△
	​

由ℓ
2
	​

[Δ
X
(1)
	​

]=c
△
	​

ℓ
2
	​

[C]定义.

令

R=Δ
X
(1)
	​

−c
△
	​

C.

则

B
Σ
	​

R=0,ℓ
2
	​

[R]=0.

因此

[R]∈kerℓ
2
	​

=0,

从而

R=B
Σ
	​

Ξ+dY+
i
∑
	​

E
i
	​

δΦ
i
	​

δΣ
	​

.

Local BRST cohomology precisely classifies these admissible anomalies and operator counterterms；consistent DRED admits a Quantum Action Principle，but evanescent breakings must still be retained explicitly.
arXiv
+1

2. Finite or infinite completion
2.1 V-prepotential variables

由

e
−V
D
α
	​

e
V
=D
α
	​

+
r=0
∑
∞
	​

(r+1)!
(−1)
r
	​

L
V
r
	​

(D
α
	​

V)

得到

W
α
	​

=−
4
1
	​

D
ˉ
2
r=0
∑
∞
	​

(r+1)!
(−1)
r
	​

L
V
r
	​

(D
α
	​

V).

所以即使 covariant expression 只含两个 W，其 V-expansion 仍含任意多的 V。

V-supergraph completion is infinite.
	​


标准 chiral-representation formula 和其 exact gauge transformation 正是这一 nonpolynomial structure。
arXiv

2.2 Superconnection/field-strength variables

若把 connection Γ
A
	​

 当作 primitive variable：

W=dΓ+Γ
2

对 connection degree 至多为二次，而

∇X=DX+[Γ,X]

每个 covariant derivative 最多增加一个 connection。

对题设 seed

O
AB
=∇
−
	​

[(∇
+
	​

W
+
	​

)
A
(∇
+
	​

W
+
	​

)
B
]

有：

deg
Γ
	​

W∈{1,2},
deg
Γ
	​

(∇W)∈{1,2,3},
deg
Γ
	​

O∈{2,3,4,5,6,7}.

因此在 formal superconnection expansion 中，即使没有其他 identities，local completion 可从 triangle level 延伸至 seven-background-leg level，即 insertion 加七 legs 的 octagon level。

对该 seed，triangle+box+pentagon 并无一般 finite-completeness theorem。
	​


Superspace constraints、component projection 或特定 color symmetry 可以降低这个上界，但必须显式证明。

2.3 Component A
μ
	​

 variables

对于特定 characteristic density：

F
μν
	​

=∂
μ
	​

A
ν
	​

−∂
ν
	​

A
μ
	​

+[A
μ
	​

,A
ν
	​

],

故

F∧F

只含 A
2
,A
3
,A
4
。这正对应 triangle、box、pentagon completion。

但题设 O 含三个 covariant spinor derivatives；不能从 F∧F 的 degree-four truncation 推出同样结论。

2.4 Full one-loop effective action

即使 component local anomaly polynomial 有 finite degree，full one-loop 1PI effective action 仍含 arbitrary-n nonlocal gauge-invariant vertices。

因此：

Object	Background-leg expansion
F∧F in A
μ
	​

	finite, through four A's
seed O in formal superconnections	finite upper bound seven before reductions
covariant expression in W,∇	one finite abstract word
same expression in unconstrained V	infinite
complete one-loop nonlocal 1PI functional	infinite
3. Exact chiral–vector representation bridge

Euclidean signature 下，Ω 与 
Ω
ˉ
 在 algebraic stage 独立；reality condition 最后施加。

3.1 Vector representation

定义 bridge fields：

e
V
=e
Ω
e
Ω
ˉ
.

Background vector-representation derivatives：

∇
α
(v)
	​

=e
−Ω
D
α
	​

e
Ω
,
∇
ˉ
α
˙
(v)
	​

=e
Ω
ˉ
D
ˉ
α
˙
	​

e
−
Ω
ˉ
.

Gauge transformations：

e
Ω
⟶e
i
Λ
ˉ
e
Ω
e
−iK
,
e
Ω
ˉ
⟶e
iK
e
Ω
ˉ
e
−iΛ
,

where

D
α
	​

Λ
ˉ
=0,
D
ˉ
α
˙
	​

Λ=0,K
†
=K.

于是

∇
A
(v)
	​

⟶e
iK
∇
A
(v)
	​

e
−iK
,

并且

e
V
⟶e
i
Λ
ˉ
e
V
e
−iΛ
.
3.2 Chiral representation

定义 similarity bridge

S=e
−
Ω
ˉ
.

对任意 adjoint operator：

∇
A
(c)
	​

=S∇
A
(v)
	​

S
−1
.

于是

∇
α
(c)
	​

=e
−V
D
α
	​

e
V
,
∇
ˉ
α
˙
(c)
	​

=
D
ˉ
α
˙
	​

.

且

W
α
(c)
	​

=−
4
1
	​

D
ˉ
2
(e
−V
D
α
	​

e
V
).

若 X
v
	​

 是 adjoint covariant field：

X
c
	​

=SX
v
	​

S
−1
,

则 exact intertwining identity 为

∇
A
(c)
	​

X
c
	​

=S(∇
A
(v)
	​

X
v
	​

)S
−1
.

对 R
O
	​

=Adj⊗Adj：

O
c
	​

=(Ad
S
	​

⊗Ad
S
	​

)O
v
	​

.

上述 bridge 及 background/quantum split 是 standard background superspace construction。
Department of Physics
+1

3.3 Background/quantum splitting

在 quantum-chiral/background-vector representation：

∇
α
(v)
	​

=e
−gv
∇
α
(v)
	​

e
gv
,
∇
ˉ
α
˙
(v)
	​

=
∇
ˉ
α
˙
(v)
	​

.

Background transformation：

e
gv
⟶e
iK
e
gv
e
−iK
.

Total chiral prepotential exactly为

e
V
tot
	​

=e
Ω
e
gv
e
Ω
ˉ
	​


并且

∇
α
(c)
	​

=e
−V
tot
	​

D
α
	​

e
V
tot
	​

,
∇
ˉ
α
˙
(c)
	​

=
D
ˉ
α
˙
	​

.

Quantum BRST 可写成 exponential form：

s
q
	​

e
gv
=i
c
ˉ
e
gv
−ie
gv
c,
∇
ˉ
α
˙
	​

c=0,∇
α
	​

c
ˉ
=0,
s
q
	​

c=ic
2
,s
q
	​

c
ˉ
=i
c
ˉ
2
,

with background bridges inert under s
q
	​

。

3.4 Measures

对于 fundamental chiral fields：

Φ
v
	​

=e
Ω
ˉ
Φ
c
	​

,
Φ
ˉ
v
	​

=
Φ
ˉ
c
	​

e
Ω
.

因此

∫d
8
z
Φ
ˉ
v
	​

Φ
v
	​

=∫d
8
z
Φ
ˉ
c
	​

e
V
Φ
c
	​

.

对于 adjoint traced full-superspace terms：

∫d
8
ztr(X
c
	​

Y
c
	​

)=∫d
8
ztr(X
v
	​

Y
v
	​

).

Covariantly chiral measure 应定义为 chiral bridge pullback；不能在 vector representation 中把 ordinary chirality 与 covariant chirality 混同。

3.5 Propagator and vertex conjugation

若 quadratic operators 满足

H
c
	​

=S
R
	​

H
v
	​

S
R
−1
	​

,

则

G
c
	​

=H
c
−1
	​

=S
R
	​

G
v
	​

S
R
−1
	​

.

Kernel form：

G
c
	​

(z,z
′
)=S
R
	​

(z)G
v
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

Insertion kernel：

I
c
	​

(z,z
′
)=S
R
	​

(z)I
v
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

因此

STr(G
c
	​

I
c
	​

)=STr(G
v
	​

I
v
	​

),

provided the regulated supertrace is cyclic and the field-redefinition Jacobian equals one。

这就是 physical covariant kernels 在两个 representations 中相等的 exact proof。该 Jacobian/cyclicity 必须成为 acceptance gate；不能仅口头假定。

4. Superspace Ward recursion
4.1 Connection-variable recursion

令 B
M
a
	​

(z) 为 background superconnection，ϵ
M
	​

 为其 Grassmann parity。

Background Ward operator：

W
a
(z)=(−1)
ϵ
M
	​

∇
M
ab
	​

δB
M
b
	​

(z)
δ
	​

−(ρ
O
a
	​

J)
I
	​

δJ
I
	​

(z)
δ
	​

.

由

W
a
(z)Γ=0

得到，at zero background：

(−1)
ϵ
M
1
	​

	​

D
M
1
	​

(1)
	​

Γ
O,m
a
1
	​

…a
m
	​

;I
	​

=
	​

−
j=2
∑
m
	​

(−1)
σ
1j
	​

f
a
1
	​

a
j
	​

b
	​

δ(z
1
	​

−z
j
	​

)
×Γ
O,m−1
a
2
	​

…b…a
m
	​

;I
	​

−δ(z
1
	​

−z
O
	​

)(ρ
O
a
1
	​

	​

)
I
J
	​

Γ
O,m−1
a
2
	​

…a
m
	​

;J
	​

.
	​


这是最干净的 non-Abelian superspace Ward recursion。

右边包含：

contracted gauge leg 与另一个 background leg collision；

contracted leg 与 composite insertion collision；

所有 graded signs (−1)
σ
1j
	​

。

在 connection variables 中 gauge transformation 只有 affine term 与 one-commutator term，因此没有 higher-Bernoulli contacts。

4.2 Exact V-gauge transformation

Chiral representation：

e
V
⟶e
i
Λ
ˉ
e
V
e
−iΛ
.

定义 covariant variation：

ΔV=e
−V
δe
V
=i(e
−L
V
	​

Λ
ˉ
−Λ).

由于

ΔV=
L
V
	​

1−e
−L
V
	​

	​

δV,

得到

δV=i
e
L
V
	​

−1
L
V
	​

	​

Λ
ˉ
−i
1−e
−L
V
	​

L
V
	​

	​

Λ
	​


以及 exact BCH expansion：

δV=
	​

i(
Λ
ˉ
−Λ)−
2
i
	​

[V,
Λ
ˉ
+Λ]
+
12
i
	​

[V,[V,
Λ
ˉ
−Λ]]
−
720
i
	​

[V,[V,[V,[V,
Λ
ˉ
−Λ]]]]+⋯.
	​


不存在 cubic-V gauge-variation term，因为相应 Bernoulli number 为零。

4.3 Integrated V-Ward identity
0=∫d
8
ztr(δ
Λ
	​

V
δV
δΓ
	​

)+δ
Λ
	​

J
I
	​

δJ
I
	​

δΓ
	​

.

At V=0，linear Ward operators 为

L
Λ
	​

X=
4
i
	​

D
ˉ
2
X,
L
Λ
ˉ
	​

X=−
4
i
	​

D
2
X.

项目中的 +-polarized contraction 之后，free-line pinching 必须继续使用

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

,

不能预先把它替换成 □。

4.4 First recursive levels

定义

C
b
(1)
	​

[Λ,
Λ
ˉ
]=−
2
i
	​

[T
b
,
Λ
ˉ
+Λ],

以及

C
bc
(2)
	​

[Λ,
Λ
ˉ
]=
12
i
	​

(
+
	​

[T
b
,[T
c
,
Λ
ˉ
−Λ]]
[T
c
,[T
b
,
Λ
ˉ
−Λ]]).
	​


则：

Triangle level
L
1
	​

Γ
O,2
	​

=−C
12
(1)
	​

Γ
O,1
	​

−C
1O
	​

Γ
O,1
	​

.

因此 primitive triangle 只有在

Γ
O,1
	​

=0

被显式证明后才是 transverse boundary datum。

Box level
L
1
	​

Γ
O,3
	​

=−
j=2
∑
3
	​

C
1j
(1)
	​

Γ
O,2
	​

−C
1O
	​

Γ
O,2
	​

.
Pentagon level
L
1
	​

Γ
O,4
	​

=
	​

−
j=2
∑
4
	​

C
1j
(1)
	​

Γ
O,3
	​

−
2≤j<k≤4
∑
	​

C
1jk
(2)
	​

Γ
O,2
	​

−C
1O
	​

Γ
O,3
	​

.
	​


其中第二行是 V-representation 特有的 double-contact/BCH seagull。

更高 orders 包含 V
4
,V
6
,… Bernoulli contacts，因此 recursion infinite。

4.5 Primitive form factor as boundary datum

令 P
coh
	​

 annihilate：

longitudinal terms；

BRST-exact terms；

EOM insertions；

total derivatives；

chosen finite-counterterm directions。

则

c
△
	​

=
P
coh
	​

C
2
	​

P
coh
	​

[Γ
O,2
(1)
	​

]
local
	​

	​

	​


这里 numerator 必须是 complete two-background graph family，而不是单独的 geometric triangle topology。

Ward recursion supplies only an inhomogeneous solution。每一级仍可加 homogeneous solution：

L
1
	​

H
m
	​

=0.

排除 local H
m
	​

 正是 kerℓ
2
	​

=0 的职责；nonlocal transverse H
m
	​

 不会被该 theorem 排除。

5. Graph-complete one-loop census
5.1 Universal Hessian formula

把 complex fields doubled 成 real field space 后：

Γ
(1)
=
2
1
	​

STrlogH.

若 source dependence 为

H[J,V]=H[V]+JI[V],

则

Γ
O
(1)
	​

=
2
1
	​

STr(G[V]I[V]),G=H
−1
.

展开

H=H
0
	​

+
r≥1
∑
	​

H
r
	​

,I=
s≥0
∑
	​

I
s
	​

,

得到 exact graph generator：

Γ
O,n
(1)
	​

=
2
1
	​

k≥0
∑
	​

(−1)
k
s+r
1
	​

+⋯+r
k
	​

=n
r
i
	​

≥1
	​

∑
	​

Sym
n
	​

STr(G
0
	​

I
s
	​

G
0
	​

H
r
1
	​

	​

⋯G
0
	​

H
r
k
	​

	​

)
	​


加上 one-loop local counterterm vertex CT
n
	​

。

这条 formula 包含所有 polygons、seagulls、insertion contacts、tadpoles 和 mixed Hessian-block cycles。

5.2 Triangle level: n=2

必须生成：

I
0
	​

H
1
	​

H
1
	​

true triangle,
I
0
	​

H
2
	​

ordinary-action seagull,
I
1
	​

H
1
	​

insertion contact,
I
2
	​

double insertion contact/tadpole,

以及

CT
2
	​

.

即使某些项因 color、D-algebra 或 scaleless DRED integrals 等于零，也必须先生成再证明为零。

5.3 Box level: n=3

Cyclic word classes：

I
0
	​

H
1
3
	​

,
I
0
	​

H
2
	​

H
1
	​

all cyclicly inequivalent orderings,
I
1
	​

H
1
2
	​

,
I
0
	​

H
3
	​

,I
1
	​

H
2
	​

,I
2
	​

H
1
	​

,I
3
	​

,

以及

CT
3
	​

.
5.4 Pentagon level: n=4

Cyclic word classes：

I
0
	​

H
1
4
	​

,
I
0
	​

H
2
	​

H
1
2
	​

,I
1
	​

H
1
3
	​

,
I
0
	​

H
2
2
	​

,I
0
	​

H
3
	​

H
1
	​

,I
1
	​

H
2
	​

H
1
	​

,I
2
	​

H
1
2
	​

,
I
0
	​

H
4
	​

,I
1
	​

H
3
	​

,I
2
	​

H
2
	​

,I
3
	​

H
1
	​

,I
4
	​

,

以及

CT
4
	​

.

每一 class 必须包含：

all labeled external-leg partitions；

all admissible loop species；

all orientations；

graded cyclic signs；

reflection-related color orderings。

5.5 Extra V-representation families

因为 V dimension 为零且指数展开 infinite：

H
r
	​


=0,I
s
	​


=0

可对任意 r,s 成立。

额外 families 包括：

arbitrary-valence gauge-prepotential vertices；

arbitrary-valence matter e
V
 vertices；

nonlinear FP vertices；

background-only NK vertices；

source-bridge contact vertices；

evanescent DRED counterterm vertices；

BRST-exact source-renormalization vertices。

5.6 Ghost and Nielsen–Kallosh sectors

在 background superspace gauge fixing 中，FP ghosts 与 Nielsen–Kallosh ghost 均与 background field 耦合；NK determinant 只产生 one-loop contributions。
Department of Physics
+1

但它们是否贡献当前 insertion 由

δJ
δH
ghost
	​

	​

,
δJ
δH
NK
	​

	​


决定：

若 S
J
	​

 只含 physical W,∇，且 source-extended gauge fixing 与 J 无关，则

I
ghost
	​

=I
NK
	​

=0,

因而没有 direct ghost/NK insertion loop。

若 Ward insertion contains gauge-fixing variation、BRST-exact completion 或 source-dependent ghost terms，则 ghosts 必须计入。

对 N=4 用 N=1 superfields，three adjoint chirals、vector、FP 和 NK blocks 都必须出现在 full Hessian；不能先使用 cancellation assumption。

6. Machine-checkable acceptance gates
Gate	Exact test	Pass condition
G0 Convention lock	固定 D-algebra、Euclidean conjugation、generator normalization、A,B representation、source measure	无 undefined sign/index convention
G1 GraphIR closure	对 graph census 中每个 graph 应用 gauge-variation map	variation 后的每个 pinched/contact graph 都存在于 GraphIR；formal coefficients 精确相消
G2 D-algebra	使用 {D
α
	​

,
D
ˉ
α
˙
	​

}=−2i∂
α
α
˙
	​

、delta-function IBP、graded Leibniz、K
+
	​

	两侧 canonical normal forms 完全相同
G3 Propagator pinching	H
0
	​

G
0
	​

=1，对 +-sector 使用 K
+
	​

G
+
	​

=δ
+
	​

	Ward contraction 精确产生相邻 propagator cancellation
G4 Routing/reflection	固定 loop routing；比较 ℓ↦−ℓ−P 后 denominator tuple、numerator、color reversal	reflected pair 包含正确 statistics 和 trace-reversal sign
G5 ST recursion	检查 triangle、box、pentagon equations，包括 C
(1)
,C
(2)
 和 insertion contacts	residual GraphIR expression 等于零
G6 Representation bridge	H
c
	​

−S
R
	​

H
v
	​

S
R
−1
	​

=0，同样检查 I,G	endpoint bridges telescope；regulated supertraces 相同
G7 Cohomology uniqueness	构造 local monomial basis，计算 closed/exact matrices 与 ℓ
2
	​

	dimimℓ
2
	​

=1，kerℓ
2
	​

=0
G8 Nonlinear reconstruction	展开 candidate C[W,∇] 的 BCH series	每一级 computed local term 与 c
△
	​

C
n
	​

 之差为 BRST-exact/EOM/total derivative
G9 DRED evanescents	保留 
g
^
	​

,
g
~
	​

 split 与全部 ϵ/ϵ terms	ST residual 在 renormalized four-dimensional limit 为零
G10 IR separation	在 nonexceptional momenta 或独立 IR regulator 下提取 UV-local part	local coefficient 与 IR prescription 无关

DRED gate 必须采用：

g
(4)
μν
	​

=
g
^
	​

(d)
μν
	​

+
g
~
	​

(2ϵ)
μν
	​

,
g
^
	​

μ
μ
	​

=d=4−2ϵ,
g
~
	​

μ
μ
	​

=2ϵ,ℓ
μ
g
~
	​

μν
	​

=0,

以及 exact tensor reduction：

∫d
d
ℓℓ
μ
ℓ
ν
f(ℓ
2
)=
d
g
^
	​

μν
	​

∫d
d
ℓℓ
2
f(ℓ
2
).

Spinor/sigma algebra 使用 g
(4)
	​

，loop tensor integral 使用 
g
^
	​

(d)
	​

。所有

g
~
	​

μ
μ
	​

ϵ
1
	​

=2

型 finite remnants 必须保留。

7. Genuine obstructions and gap audit
7.1 Literal full-amplitude statement is false

任何 gauge-invariant nonlocal transverse functional，其 expansion 从 four-point 或更高开始，均满足 homogeneous Ward identity，并且不改变 triangle。

因此一般结构只能写成

Γ
O,m
(1)
	​

=c
△
	​

C
m
	​

+T
m
nonlocal,transverse
	​

+B
Σ
	​

X
m
	​

+E
m
	​

+dY
m
	​

.

T
m
	​

 不由 triangle 决定。

同样，individual supergraph 也不是 gauge-covariant completion；只有 polygon 加所有 contacts 的 graph-complete sum 才可能满足 Ward identity。

7.2 Specific higher-order local cohomology may exist

Standard engineering dimensions：

[W
α
	​

]=
2
3
	​

,[∇
α
	​

]=
2
1
	​

,

故

[O
AB
]=
2
1
	​

+2(
2
1
	​

+
2
3
	​

)=
2
9
	​

.

Grassmann parities：

∣W
+
	​

∣=1,∣∇
+
	​

W
+
	​

∣=0,∣O∣=1.

存在 dimension/parity-compatible cubic candidate family：

Q
AB
=C
AB
CDE
	​

W
+
C
	​

W
+
D
	​

W
+
E
	​

,

满足

[Q]=
2
9
	​

,∣Q∣=1,

且其 background expansion 从 cubic order 开始：

ℓ
2
	​

[Q]=0.

它是否被 Lorentz weights、R-charge、color representation 或 trace sector 排除，必须显式判断。若未被排除，则

kerℓ
2
	​


=0,

triangle 不能决定 box coefficient。

这不是形式上的小问题，而是对当前 seed 最直接的 potential obstruction。

7.3 Operator measure/chirality is unresolved

在 ordinary N=1 superspace algebra 中：

∇
ˉ
α
˙
	​

W
+
	​

=0,

但

∇
ˉ
α
˙
	​

(∇
+
	​

W
+
	​

)=[
∇
ˉ
α
˙
	​

,∇
+
	​

]W
+
	​

=−2i∇
+
α
˙
	​

W
+
	​

,

一般不等于零。

因此

O
AB

一般不是 covariantly chiral。故以下选择不能自动使用：

∫d
6
zJ
AB
	​

O
AB
.

必须明确：

full superspace measure；

reduced/twisted measure；

额外 chiral projector；

或使用 equations of motion 后的 constrained identity。

Measure 未锁定时，cohomology sector 也未定义。

7.4 Meaning of A,B is essential

三种不同问题不能混合：

A,B 为 gauge-adjoint indices，O∈Adj⊗Adj；

A,B 为 R-symmetry indices；

(∇W)
A
(∇W)
B
 实际上是 matrix product，整体仅为 adjoint 或 singlet。

对应的：

source transformation；

color tensor basis；

BRST cohomology；

possible cubic classes；

single/multi-trace mixing

全部不同。

7.5 Tensor-product derivative must be specified

若 O
AB
∈Adj⊗Adj，则外层 derivative 必须是 tensor-product connection：

∇
−
Adj⊗Adj
	​

=D
−
	​

+Γ
−
a
	​

(ρ
Adj
a
	​

⊗1+1⊗ρ
Adj
a
	​

).

因为 ∇
+
	​

W
+
	​

 是 even：

O
AB
=
	​

(∇
−
	​

∇
+
	​

W
+
	​

)
A
(∇
+
	​

W
+
	​

)
B
+(∇
+
	​

W
+
	​

)
A
(∇
−
	​

∇
+
	​

W
+
	​

)
B
.
	​


若实际 intended ordering 是 matrix multiplication，则不能使用该 formula。

7.6 Composite-operator mixing

即使 gauge covariance exact，也可能有

[O]
R
	​

=Z
OO
	​

O+
i
∑
	​

Z
Oi
	​

O
i
	​

+B
Σ
	​

X+
j
∑
	​

E
j
	​

δΦ
j
	​

δΣ
	​

+dY.

必须 enumerate 所有具有相同：

(
2
9
	​

,parity,Lorentz weight,R
O
	​

,R-charge)

的 O
i
	​

。

没有这一 operator-mixing matrix，不能定义“the triangle coefficient”属于哪个 renormalized operator。

7.7 Consistent versus covariant current

若 triangle coefficient 来自 consistent current，而 nonlinear target 写成 covariant current，则两者相差 Bardeen–Zumino term。Box/pentagon coefficients会发生 finite local shift，同时 triangle anomaly class 可保持不变。

必须选择并固定：

consistent currentorcovariant current.
7.8 DRED evanescent obstruction

Strictly four-dimensional cohomology 不能自动排除：

ϵ×
ϵ
1
	​


产生的 finite local operators。需要扩大 temporary operator basis，包含：

g
~
	​

μν
	​

-dependent terms；

ϵ-scalar structures；

evanescent source operators。

随后证明它们在 physical quotient 中为 zero、exact，或由 symmetry-restoring counterterm 移除。

7.9 N=4 hidden supersymmetry

在 N=1 superfield background gauge 中只 manifestly control N=1 supersymmetry。

若 uniqueness proof 使用 full N=4：

hidden supersymmetry transformations；

their antifields or shadow sources；

extended ST identity；

DRED restoration counterterms

必须纳入。

否则 theorem 只能声明为 N=1-cohomological theorem，不能使用 N=4 symmetry 排除额外 classes。

Minimal exact proof architecture
Phase 0 — Convention closure

明确：

R
O
	​

,dμ
O
	​

,∣J∣,R(J),A,B meaning,

以及 consistent/covariant current choice。

Explicit calculation required: check chirality and tensor-product action of ∇
−
	​

。

Phase 1 — Source-extended BV action

构造

Σ=S
SYM
	​

+S
gf
	​

+S
FP
	​

+S
NK
	​

+S
antifield
	​

+S
J
	​

.

证明

S(Σ)=0,W
K
	​

Σ=0.

Explicit calculation required: sO and possible source partners。

Phase 2 — Local cohomology and injectivity

生成所有 admissible local monomials，计算：

H
loc
0
	​

orH
loc
1
	​

,

并计算

ℓ
2
	​

.

Acceptance condition：

dimimℓ
2
	​

=1,kerℓ
2
	​

=0.

This is the decisive theorem-level calculation.

Phase 3 — Representation bridge

逐 species 证明：

H
c
	​

=S
R
	​

H
v
	​

S
R
−1
	​

,
I
c
	​

=S
R
	​

I
v
	​

S
R
−1
	​

,
G
c
	​

(z,z
′
)=S
R
	​

(z)G
v
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

检查 regulated Jacobian 与 supertrace cyclicity。

Phase 4 — GraphIR generation

由 Hessian formula 自动生成 n=2,3,4 全部 cyclic words、contacts、ghost blocks、counterterms。

不允许手工只选 triangle/box/pentagon polygons。

Phase 5 — Primitive boundary calculation

独立计算 complete n=2 set：

{I
0
	​

H
1
2
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

}.

提取

c
△
	​

=
P
coh
	​

C
2
	​

P
coh
	​

Γ
O,2
(1)
	​

	​

.

No known coefficient is imported.

Phase 6 — Box and pentagon validation

显式计算或至少 integrand-level reduce：

Γ
O,3
	​

,Γ
O,4
	​

,

并验证：

L
1
	​

Γ
O,3
	​

=all Γ
O,2
	​

 contacts,
L
1
	​

Γ
O,4
	​

=all Γ
O,3
	​

+Γ
O,2
	​

 contacts.

这两级是 graph generator、D-algebra、routing 和 bridge 的 mandatory validation，不是 uniqueness proof 的替代。

Phase 7 — All-order V-leg proof

取

R
(1)
=[Δ
(1)
]
local
	​

−c
△
	​

C.

由 ST：

B
Σ
	​

R
(1)
=0.

由 triangle matching：

ℓ
2
	​

[R
(1)
]=0.

由 injectivity：

[R
(1)
]=0.

因此所有 V-orders 的 nontrivial local coefficients 等于 c
△
	​

C
n
	​

。Infinite V-completion 由 BCH expansion 自动生成，无需逐个计算任意高 polygon。

Final status
Literal “every higher-leg 1PI amplitude is only triangle completion” is false.
	​

A local nontrivial completion theorem is valid only conditionally on kerℓ
2
	​

=0.
	​

For unconstrained V, the completion is infinite.
	​


当前真正未闭合的三处是：

R
O
	​

、source measure 与 precise Ward identity 尚未固定；

dimension-
2
9
	​

 sector 的 local BRST cohomology 与 kerℓ
2
	​

 尚未计算；

complete triangle boundary，包括 all insertion/action contacts 与 DRED evanescent terms，尚未独立计算。

在这三项通过之前，不能严谨声称“one triangle coefficient determines all dressings”；通过之后，该结论可由上述三行 cohomological argument 精确证明。
