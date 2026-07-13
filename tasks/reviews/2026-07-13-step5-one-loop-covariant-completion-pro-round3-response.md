# GPT Pro gap review, round 3: exact response

Status: `EXTERNAL_GAP_REVIEW_ONLY`

This transcript has no formula authority. Every usable claim requires an independent Project-frame derivation and executable certificate.

记号
A
DE
:=
W
a
˙
D
	​

Y
E
a
˙
,C
AB;DE
	​

:=c
ACD
	​

c
BCE
	​

.
τ
slot
	​

F
AB
(p,q):=F
BA
(q,p)

表示同时交换 ordered slots、color labels 和 momenta。

π
±
	​

F
AB
:=
2
1
	​

(F
AB
±F
BA
)

只交换 local output indices A,B，不交换 momentum/derivative placement。

Δ
R
∗
	​


表示从 ordered bilocal/ledger kernel 到 coincident local operator 的 renormalized diagonal map；其 kernel 包括在 coincident limit 消失或仅改变 finite contact convention 的 ordered expressions。

H
phys
	​


表示固定 source channel、quantum numbers 和 DRED temporary complex 后的 source-linear local BRST cohomology。

ℓ
2
	​

:H
phys
	​

⟶T
2
	​


表示 fixed quadratic jet induced on the physical quadratic-jet quotient；T
2
	​

 已除去 quadratic jets of BRST-exact、EOM、IBP 和 evanescent-trivial terms。

Audit verdict
O
−
BA
	​

=−O
−
AB
	​

	​


严格成立，不需要假定 c
ABC
	​

 全反对称。

I
BA
=I
AB
,S
J
	​

=∫d
8
zJ
(AB)
	​

I
AB
.
	​


所以：

π
+
	​

O
−
	​

=0,π
+
	​

O
+
	​

=O
+
	​

.
	​


因此，在给定 local source channel 中，minus tensor cannot be a nonzero physical completion。在两个 displayed possibilities 中，只有 plus tensor type-compatible：

O
+
AB
	​

=c
ACD
	​

c
BCE
	​

[
W
a
˙
D
	​

Y
E
a
˙
+Y
D
a
˙
W
a
˙
E
	​

].
	​


但这不等于证明 graph computation produces the plus sign。实际 reflected-orientation sign 仍需要 original pre-D cyclic word、endpoint-transfer log、supertranspose convention 和 GraphIR port semantics。若完整 graph calculation 真正给出 minus combination，则其 symmetric-source projection 为零，而不是一个 antisymmetric physical completion。

1. Literal dotted-index variance

采用

Y
a
˙
=ϵ
a
˙
b
˙
Y
b
˙
	​

,
W
a
˙
=ϵ
a
˙
b
˙
W
b
˙
	​

.

由于

∣Y∣=0,∣
W
∣=1,

保持 index heights 不变时：

Y
D
a
˙
W
a
˙
E
	​

=
W
a
˙
E
	​

Y
D
a
˙
.

没有 Koszul minus。故

O
−
AB
	​

	​

=C
AB;DE
	​

[
W
a
˙
D
	​

Y
E
a
˙
−
W
a
˙
E
	​

Y
D
a
˙
]
=C
AB;DE
	​

(A
DE
−A
ED
).
	​


因此 bracket 是 D,E-antisymmetric：

B
−
DE
	​

:=A
DE
−A
ED
,B
−
ED
	​

=−B
−
DE
	​

.

注意，不允许把第二项改写成 Y
a
˙
D
	​

W
E
a
˙
 而不加入额外 minus。事实上：

W
a
˙
	​

Y
a
˙
=Y
a
˙
W
a
˙
	​

=−Y
a
˙
	​

W
a
˙
=−
W
a
˙
Y
a
˙
	​

.
	​


证明：

Y
a
˙
	​

W
a
˙
	​

=Y
a
˙
	​

ϵ
a
˙
b
˙
W
b
˙
	​

=−ϵ
a
˙
b
˙
Y
b
˙
	​

W
a
˙
	​

=−
W
a
˙
	​

ϵ
a
˙
b
˙
Y
b
˙
	​

=−
W
a
˙
	​

Y
a
˙
.
	​


这里第三行仅使用 Y even。

给定 component witness：

Y
a
˙
	​

=(a,b),
W
a
˙
	​

=(c,d),
Y
a
˙
=(b,−a),
W
a
˙
=(d,−c),

确有

W
a
˙
	​

Y
a
˙
=cb−da=bc−ad,

而

Y
a
˙
	​

W
a
˙
=ad−bc=−(bc−ad).
A,B symmetry

不需要 c
ABC
	​

=c
[ABC]
	​

。数值 tensors commute，因此：

C
BA;DE
	​

	​

=c
BCD
	​

c
ACE
	​

=c
ACE
	​

c
BCD
	​

=C
AB;ED
	​

.
	​


于是

O
−
BA
	​

	​

=C
BA;DE
	​

B
−
DE
	​

=C
AB;ED
	​

B
−
DE
	​

=C
AB;DE
	​

B
−
ED
	​

=−O
−
AB
	​

.
	​


同理，定义

B
+
DE
	​

:=A
DE
+A
ED
,

则

O
+
BA
	​

=+O
+
AB
	​

	​

.
2. Ordered ledger → physical local source
2.1 两个不同的 exchange operations

必须区分：

Ordered-slot exchange
(τ
slot
	​

F)
AB
(p,q;k)=F
BA
(q,p;k),k+p+q=0.

因为两个 seed slots 都是 X，且

∣X∣=0,

所以没有 Koszul sign：

τ
slot
2
	​

=1.
Local source-index exchange
(σ
AB
	​

O)
AB
:=O
BA
.

它不交换 momenta 或 derivative placements。

这两个 involutions 在 point-split ledger 中不能混同。一个 kernel 可以是 τ
slot
	​

-even，却在 local A,B indices 上 antisymmetric，例如 color-antisymmetric × relative-momentum-antisymmetric structures。

2.2 Functional-derivative map

令 A
A∣B
AB
	​

(p,q) 是 ledger 中一个 ordered assignment。由于 fixed quadratic jet 定义含

2
1
	​

δV
1
	​

δ
	​

δV
2
	​

δ
	​

,

其 Bose-symmetrized kernel 是

P
slot
+
	​

A=
2
1
	​

[A
A∣B
AB
	​

(p,q)+A
B∣A
BA
	​

(q,p)].
	​


若 ledger 已经显式列出两个 assignments，则不能再次乘二或再次 symmetrize。

2.3 Local source quotient

由于 X
A
 even：

X
A
X
B
=X
B
X
A
.

Tensor-product covariant derivative obeys ordinary Leibniz here：

I
AB
=(∇
−
	​

X)
A
X
B
+X
A
(∇
−
	​

X)
B
,

故

I
AB
=I
BA
	​

.

Consequently,

S
J
	​

=∫d
8
zJ
AB
	​

I
AB
=∫d
8
zJ
(AB)
	​

I
AB
,

并且

J
[AB]
	​


是 null source direction。Oddness of J 不改变这一结论；这里只交换一个 source 的 representation indices，不是在交换两个 odd sources。

因此 physical source module 是

R
J
physical
	​

=(Sym
2
Adj)
∗
.
	​


不是 full Adj⊗Adj。

2.4 Point-split/contact version

若 ledger 真正实现为 point-split product，则 exact map 是

Q
phys
	​

=π
+
	​

∘Δ
R
∗
	​

∘P
slot
+
	​

.
	​


相应 physical local space：

L
phys
	​

≃L
ordered
	​

/kerQ
phys
	​

.
	​


所以三个描述分别对应不同 stages：

Stage
ordered graph ledger
point-split renormalized intermediate
given physical local source
	​

Carrier
Adj⊗Adj
L
ordered
	​

/kerΔ
R
∗
	​

Sym
2
Adj
	​

	​


若实际进行 gauge-covariant point splitting，还必须加入 parallel transporters：

X(z
i
	​

)⟼U(z,z
i
	​

)X(z
i
	​

)U(z
i
	​

,z),

否则两个 separated factors 不属于同一个 local gauge fiber。不同 path choices 的差异本身是 finite local curvature contact terms，必须包含在 Δ
R
∗
	​

 的 definition 中。

2.5 Application to the candidate

令

O
σ
AB
	​

=C
AB;DE
	​

(A
DE
+σA
ED
),σ=±1.

则

O
σ
BA
	​

=σO
σ
AB
	​

.

因此

π
+
	​

O
σ
	​

=
2
1+σ
	​

O
+
	​

.
	​


即：

π
+
	​

O
−
	​

=0,π
+
	​

O
+
	​

=O
+
	​

.
3. Reflected orientation and endpoint signs
3.1 Parities
∣W∣=∣
W
∣=1,∣∇∣=∣
∇
ˉ
∣=1,∣D∣=0,
∣X∣=∣∇W∣=0,∣Y∣=∣DX∣=0.

因此

∣
W
a
˙
	​

Y
a
˙
∣=1,∣O
±
	​

∣=1.

Exchanging the final fields gives

(−1)
∣
W
∣∣Y∣
=(−1)
1⋅0
=+1.

所以 final field reordering 本身不能产生 displayed minus sign。

同样，两个 seed blocks：

∣X
A
∣∣X
B
∣=0,

故 reflected exchange of the two completed X-blocks also gives +1。

3.2 Odd derivative transfer

对于 odd derivative D 和 homogeneous F,G：

D(FG)=(DF)G+(−1)
∣F∣
F(DG).

Full-superspace integration by parts：

∫d
8
z(DF)G=−(−1)
∣F∣
∫d
8
zF(DG).
	​


因此一次 endpoint transfer 的 sign 是

η
transfer
	​

(F)=(−1)
∣F∣+1
.

具体：

η
transfer
	​

(W)=η
transfer
	​

(
W
)=+1,
η
transfer
	​

(X)=η
transfer
	​

(Y)=−1.

若 derivative 穿过一个 homogeneous prefix

P=Q
1
	​

⋯Q
s
	​

,

则

η
transfer
	​

(P)=(−1)
1+∑
i=1
s
	​

∣Q
i
	​

∣
.

因此不能只数 “one integration-by-parts minus”；必须同时记录 prefix parity。

3.3 General reflection certificate

设 original pre-D cyclic word 的 homogeneous atomic factors 为

Q
1
	​

Q
2
	​

⋯Q
m
	​

.

Super-reversal sign：

s
rev
	​

=
1≤i<j≤m
∑
	​

∣Q
i
	​

∣∣Q
j
	​

∣(mod2).

若 source/insertion port P 也作为 homogeneous factor 被反转：

s
rev
(P)
	​

=∣P∣
i
∑
	​

∣Q
i
	​

∣+s
rev
	​

.

若反转后再 cyclically 把 P 移回 anchor position，则附加

s
cyc
(P)
	​

=∣P∣
i
∑
	​

∣Q
i
	​

∣.

所以这两项相消：

s
rev
(P)
	​

+s
cyc
(P)
	​

=s
rev
	​

(mod2).

这说明：若 reflection includes the odd insertion and subsequently reanchors it, insertion-port oddness alone does not flip the orientation sign。

完整 relative sign 必须是

σ
ref
	​

=(−1)
s
rev
	​

+s
endpoint
	​

+s
ϵ
	​

+s
st
	​

+s
route
	​

+s
port
	​

η
prop
	​

η
vertex
	​

R
color
	​

.
	​


其中：

s
endpoint
	​

=
transfers r
∑
	​

(1+∣P
r
	​

∣),

P
r
	​

 是第 r 次 transfer 穿过的 prefix；

s
ϵ
	​

：raising/lowering 或交换 antisymmetric epsilon slots 产生的 sign；

s
st
	​

：supertranspose intrinsic signs；

s
route
	​

：momentum reversal acting on odd momentum numerators；

η
prop
	​

：oriented propagator transpose；

η
vertex
	​

：pre-D vertex convention；

R
color
	​

：reversed color word reduced by cyclicity/Jacobi 后的 map，未必只是一个 sign。

3.4 What is determined from the supplied data

Suppose reflection maps

A
DE
=
W
a
˙
D
	​

Y
E
a
˙

to the exchanged final tensor A
ED
。Then the orientation sum is

A
DE
+σ
ref
	​

A
ED
.

The supplied final parities determine only

σ
final field reorder
	​

=+1.

它们不决定：

s
endpoint
	​

,s
st
	​

,s
route
	​

,η
prop
	​

,η
vertex
	​

,R
color
	​

.

缺失的最小 graph datum 是：

the exact original pre-D cyclic word for each reflected graph, together with its ordered endpoint-transfer log.
	​


因此无法从当前 prompt 独立重建 numerical value of σ
ref
	​

。

但 physical source projection gives an exact acceptance rule：

σ
ref
	​

=+1⇒nonzero type-compatible O
+
	​

,
	​

σ
ref
	​

=−1⇒π
+
	​

O
−
	​

=0.
	​


所以 minus 不能被解释为 symmetric seed 的 physical completion。

4. Fixed-ℓ
2
	​

 injectivity audit
4.1 Formal grading forces r
f
	​

(
∇
ˉ
)=+1

由

{∇
a
	​

,
∇
ˉ
b
˙
	​

}=−2D
a
b
˙
	​


和

r
f
	​

(∇)=−1,r
f
	​

(D)=0,

必须有

r
f
	​

(
∇
ˉ
)=+1
	​

.

但是 r
f
	​

 目前只是 formal grading。要将 basis 限制在固定 r
f
	​

 sector，还必须证明：

[B
Σ
	​

,r
f
	​

]=0,[EOM relations,r
f
	​

]=0,[DRED mixing,r
f
	​

]=0.

若不存在 corresponding Ward identity，r
f
	​

 只能作为 filtration，不能自动禁止 cross-grade operator mixing。

4.2 Complete content census

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

记录 letters。以 half-dimension 为单位：

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

=−1.

完整 nonnegative solutions：

Field-strength degree 0: five rows
	​

(0,0;1,0;4),
(0,0;2,1;3),
(0,0;3,2;2),
(0,0;4,3;1),
(0,0;5,4;0).
	​

Field-strength degree 1: seven rows
	​

(0,1;0,0;3),
(0,1;1,1;2),
(0,1;2,2;1),
(0,1;3,3;0),
	​

	​

(1,0;2,0;2),
(1,0;3,1;1),
(1,0;4,2;0).
	​

Field-strength degree 2: five rows
(0,2;0,1;1),(0,2;1,2;0),
(1,1;1,0;1),(1,1;2,1;0),
(2,0;3,0;0).
Field-strength degree 3: one row
(1,2;0,0;0).

Field-strength degree 4 is impossible：

4⋅
2
3
	​

=6>
2
9
	​

.

这些是 content rows，不是已经 reduced 的 monomial basis。每一行仍包含：

all derivative orderings；

all derivative placements on J and fields；

all Lorentz intertwiners；

all invariant color tensors；

all commutator-generated lower/higher-filtration relations。

4.3 Cubic sector

唯一 cubic content 是

W
W
W
.

取 j
R
	​

=0 时，两只 dotted field strengths 必须 scalar-contract：

W
a
˙
	​

W
a
˙
.

剩余 left spin 仅来自 W
a
	​

：

j
L
	​

=
2
1
	​

.

因此

[W
W
W
]
(j
L
	​

,j
R
	​

)=(3/2,0)
	​

=0.
	​


这次修正后的 spin assignment 排除了 round-2 中的 cubic obstruction。

4.4 Quadratic 
W
W
 rows

其 left-spin factors 数目为：

n
L
	​

=n
∇
	​

+n
D
	​

=1.

所以最大

j
L
	​

=
2
1
	​

.

故两行均不含 target：

[
W
2
∇
ˉ
D]
(3/2,0)
	​

=[
W
2
∇
∇
ˉ
2
]
(3/2,0)
	​

=0.
	​

4.5 Quadratic WW∇
3
 family

采用

∇
2
:=∇
a
∇
a
	​

.

从

{∇
a
	​

,∇
b
	​

}=0

和 epsilon conventions 得

∇
a
	​

∇
b
	​

=
2
1
	​

ϵ
ab
	​

∇
2
.
	​


再用 certificate：

∇
b
	​

E=−
2
1
	​

∇
2
W
b
	​

,

有

∇
a
	​

∇
b
	​

W
c
	​

=−ϵ
ab
	​

∇
c
	​

E.
	​


Modulo source derivatives，Leibniz expansion 后任何 three-∇, two-W term 均为

(∇
k
W)(∇
3−k
W),k=0,1,2,3.

对每个 k：

max(k,3−k)≥2.

因此至少一个 W 被两只 ∇ 作用，故该项属于 differential EOM ideal：

WW∇
3
∈⟨E,∇E,∇
2
E,…⟩.
	​


但这是 operator-level statement。对 local source：

∫d
8
zJ∇F=∫d
8
z(∇J)F

因为 ∣J∣=1。所以在 full source-jet complex 中，不能在未加入 ∇J monomials 时直接用 IBP 把全部 derivatives 分配到 W 上。

4.6 Quadratic W
W
∇D family

Raw Lorentz tensor product：

(
2
1
	​

,0)
W
	​

⊗(0,
2
1
	​

)
W
	​

⊗(
2
1
	​

,0)
∇
	​

⊗(
2
1
	​

,
2
1
	​

)
D
	​

.

Left side：

2
1
	​

⊗
2
1
	​

⊗
2
1
	​

=
2
3
	​

⊕
2
1
	​

⊕
2
1
	​

.

Target j
L
	​

=3/2 occurs once。

Right side：

2
1
	​

⊗
2
1
	​

=0⊕1.

Target j
R
	​

=0 occurs once。因此：

mult
(3/2,0)
	​

(W
W
∇D)=1.
	​


这是 Lorentz multiplicity one；它不意味着：

derivative-placement rank one；

color rank one；

BRST-cohomology rank one。

第二个 quadratic row

W
W
∇
2
∇
ˉ

必须通过 normal ordering：

∇
ˉ
∇=−∇
∇
ˉ
−2D

归约到 W
W
∇D、EOM terms 和 commutator-generated higher-field terms。没有完整

[∇,D],[
∇
ˉ
,D],[D,D]

coefficients 时，不能完成该 reduction matrix。

4.7 Degree-zero and degree-one rows
Degree zero

若 derivatives 只允许作用于 gauge fields，则 field-strength-degree-zero covariant word 最终作用于 identity，normal ordering 后：

derivative-only word=commutator curvatures

或零。因此它没有真正的 degree-zero gauge-field leading term。

但在 source-linear functional 中，IBP 产生：

∇J,
∇
ˉ
J,DJ,…

所以五个 degree-zero rows 是 genuine source-jet/contact candidates，除非显式施加 normalization quotient。

不能仅写 “pure gauge hence zero”；必须决定：

Are source-only/source-jet counterterms retained, normalized to zero, or placed in BRST doublets?
	​

Degree one: W-rows

在 associated field-strength filtration 中，将所有 
∇
ˉ
 normal-order 到 W 右边：

∇
ˉ
a
˙
	​

W
b
	​

=0.

Anticommutators {∇,
∇
ˉ
} 产生 D，而 [
∇
ˉ
,D] 产生额外 field strength，进入 degree two。因此 degree-one leading part reduces to

W∇
2
D
2
.

其 ∇
2
W part 属于 EOM：

∇
2
W
b
	​

=−2∇
b
	​

E.
Degree one: 
W
-rows

将所有 ∇ normal-order 到 
W
 右边：

∇
a
	​

W
b
˙
	​

=0.

Degree-one leading normal form 是

D
3
W
.

由

∇
ˉ
a
˙
	​

W
a
˙
=E

和

{∇
a
	​

,
∇
ˉ
a
˙
	​

}=−2D
a
a
˙
	​


得

−2D
a
a
˙
	​

W
a
˙
	​

=∇
a
	​

(
∇
ˉ
a
˙
	​

W
a
˙
)+
∇
ˉ
a
˙
	​

(∇
a
	​

W
a
˙
)
=∇
a
	​

E.
	​


故

D
a
a
˙
	​

W
a
˙
=−
2
1
	​

∇
a
	​

E.
	​


在 j
R
	​

=0 contraction 中，四个 dotted indices 的 invariant pairings 由 Schouten identity 联系。每一项要么：

将一只 D dotted index 与 
W
 contraction，因而为 EOM；要么

contraction 两只 D dotted indices。

第二种在 commuting associated-graded level 给出

D
(a∣
a
˙
∣
	​

D
b)
	​

a
˙
∝ϵ
ab
	​

□

并被 j
L
	​

=3/2 symmetrizer annihilate；covariant commutator remainder 属于 field-strength degree two。

因此，在 source-free associated graded：

H
gr
(0)
	​

=H
gr
(1)
	​

=0mod EOM.

这不是 full source-complex proof，因为 source jets、commutator remainders 和 color maps 尚未处理。

4.8 Mandatory missing relation data

在声称 ker
ℓ
2
	​

=0 前，以下每项必须成为 explicit finite matrix。

(a) Source-jet IBP matrix

对 odd J：

∫J∇
a
	​

F=∫(∇
a
	​

J)F,
∫J
∇
ˉ
a
˙
	​

F=∫(
∇
ˉ
a
˙
	​

J)F,
∫JD
a
a
˙
	​

F=−∫(D
a
a
˙
	​

J)F.

必须包含所有允许的

∇
m
∇
ˉ
n
D
r
J

或给出一个 BRST-compatible normalization quotient 将其删除。

(b) Derivative-placement matrix

每个 content row 需要列出：

D
1
	​

⋯D
k
	​

(F
1
	​

F
2
	​

)

展开后的所有 placements，以及 graded Leibniz coefficients。特别是

W
W
∇D

中的 derivatives 可作用于：

W,
W
,J,W
W
 product,

不能仅保留 
W
D∇W。

(c) Full commutator algebra

除已给出的 algebra 外，至少需要 exact conventions for

{
∇
ˉ
a
˙
	​

,
∇
ˉ
b
˙
	​

},
[∇
a
	​

,D
b
b
˙
	​

],[
∇
ˉ
a
˙
	​

,D
b
b
˙
	​

],
[D
a
a
˙
	​

,D
b
b
˙
	​

],

包括所有 coefficients、epsilon placements、E-trace pieces 和 signs。它们决定 degree-one ↔ degree-two filtration mixing。

(d) Chirality/Bianchi matrix

需要：

∇
ˉ
a
˙
	​

W
b
	​

=0,∇
a
	​

W
b
˙
	​

=0,
∇
a
W
a
	​

=
∇
ˉ
a
˙
	​

W
a
˙
,
∇
(a
	​

X
bc)
	​

=0,

以及 dotted analogues、vector derivative Bianchi identities 和所有 derivative consequences。

(e) Graded field-symmetry matrix

例如：

W
a
C
	​

W
b
D
	​

=−W
b
D
	​

W
a
C
	​

,
W
a
˙
C
	​

W
D
a
˙
=
W
a
˙
D
	​

W
C
a
˙
.

这些必须与 color-tensor symmetries simultaneously reduced。

(f) Color matrix

必须固定：

g,Sym
2
Adj=
λ
⨁
	​

R
λ
	​

,

以及允许的 invariant tensors：

Hom
G
	​

(Adj
⊗m
,Sym
2
Adj).

还需决定：

trace versus traceless source；

single-trace versus multi-trace sector；

ff、dd、δδ identities；

Jacobi and group-specific identities；

which irreducible R
λ
	​

 is the target channel。

Lorentz multiplicity one 不约束 color multiplicity。

(g) EOM/Koszul–Tate matrix

Pure-gauge EOM ideal 必须包含：

E,∇E,
∇
ˉ
E,DE,…

及其 products。若通过 antifields 实现，则需要 exact Koszul–Tate differential。

特别地：

I
AB
=−(∇
+
	​

E
A
)X
B
−X
A
(∇
+
	​

E
B
)
	​


本身属于 pure-gauge EOM ideal。故必须区分：

anomaly density cohomology modulo EOM；

quantum EOM insertion/contact Ward identity。

不能一方面把 seed 当作 nontrivial cohomology generator，另一方面在同一 quotient 中令 E=0。

(h) BRST source partners

需要决定 J 是：

merely covariant external source；

member of a BRST doublet；

accompanied by sources for sI；

accompanied by antifield/source-jet partners。

不同选择会改变 source-linear exact matrix。

(i) DRED evanescent matrix

Temporary basis 必须包括所有 
g
	​

-decorated operators：

g
(4)
μν
	​

=
g
	​

μν
+
g
	​

μν
,
g
	​

μ
μ
	​

=4−2ϵ,
g
	​

μ
μ
	​

=2ϵ,
g
	​

g
	​

=0.

若 E
i
^
	​

 是 evanescent operators：

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
),

则 finite physical mixing 包含

Z
PE
(−1)
	​

R.

因此 relation matrix 必须先在

{P
i
	​

,E
i
^
	​

}

上计算，不能先令 
g
	​

=0。

还需要明确：

external background momenta 是否 restricted to the d-subspace；

epsilon-scalar background components 是否存在；

quasi-four-dimensional sigma-matrix contractions；

which four-dimensional Fierz identities commute with the DRED tensor reduction。

4.9 Exact injectivity condition

令 source-linear local cocycle basis 为 M
i
	​

，closed matrix 为 C，exact/EOM/IBP matrix 为

B=[B
BRST
	​

B
EOM
	​

B
IBP
	​

B
ev
	​

].

令 fixed quadratic-jet matrix 为

L
ρi
	​

,ℓ
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

.

Quadratic trivial subspace：

B
2
	​

=im[ℓ
2
	​

B
BRST
	​

,ℓ
2
	​

B
EOM
	​

,ℓ
2
	​

B
IBP
	​

,ℓ
2
	​

B
ev
	​

].

Then

ker
ℓ
2
	​

=0
	​


iff

{v∈kerC:Lv∈B
2
	​

}=imB.
	​


若 canonical representatives 已满足 LB=0，则简化为

kerC∩kerL=imB.
	​


The census suggests a possible finite proof：

degree 0,1→0,WW∇
3
→EOM,
W
W
W

⊃(3/2,0),m≥4 forbidden,

leaving only W
W
∇D。但 injectivity follows only after the remaining quadratic placement/color matrix has full column rank under L。

目前：

ker
ℓ
2
	​

=0 has not yet been proved.
	​

5. Correct conditional theorem

令

H=H
loc,phys
source-linear
	​


是固定：

(j
L
	​

,j
R
	​

)=(3/2,0)；

r
f
	​

=−1 filtration sector；

J
(AB)
	​

 source channel；

chosen irreducible color representation；

physical-plus-evanescent DRED quotient；

后的 local BRST cohomology。

令

ℓ
2
	​

:H→T
2
	​


为 well-defined fixed quadratic-jet map。

Conditional injective-completion theorem.
Assume:

ker
ℓ
2
	​

=0.

Let Δ
loc
(1)
	​

 be a source-linear local one-loop Ward breaking and C a local covariant cocycle. If

[Δ
loc
(1)
	​

]∈H,[C]∈H,

and

ℓ
2
	​

[Δ
loc
(1)
	​

]=
ℓ
2
	​

[C],

then

[Δ
loc
(1)
	​

]=[C].
	​


Proof：

ℓ
2
	​

([Δ
loc
(1)
	​

]−[C])=0,

injectivity gives

[Δ
loc
(1)
	​

]−[C]=0.

Two qualifications：

Injectivity gives uniqueness, not existence

Given a computed quadratic jet t
2
	​

∈T
2
	​

，a local completion exists only if

t
2
	​

∈im
ℓ
2
	​

.

Injectivity only says it is unique if it exists。

Injectivity does not imply a single scalar coefficient

若

dimT
2
	​

>1,

the primitive calculation produces a vector of independent quadratic form factors。A single projected triangle coefficient cannot reconstruct the class。

A rank-one corollary is valid only after fixing a color/source irrep R
λ
	​

 and proving

dimim
ℓ
2,λ
	​

=1.

Then injectivity implies

dimH
λ
	​

≤1.

若另有一个 nonzero class，则

dimH
λ
	​

=1.
6. Exact Hessian/source census

采用 left derivative with respect to odd J。Since

∣J∣=1,∣JI∣=0,

有

∣I
s
	​

∣=1,∣G
0
	​

∣=∣H
s
	​

∣=0.

The retained two-background formula is

Γ
I,2
(1)
	​

=
2
1
	​

STr[
	​

+G
0
	​

I
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
1
	​

−G
0
	​

I
0
	​

G
0
	​

H
2
	​

−G
0
	​

I
1
	​

G
0
	​

H
1
	​

+G
0
	​

I
2
	​

]+CT
2
	​

.
	​

	​


这里必须把 compact notation 解释为 labeled-background completion：

G
0
	​

I
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
1
	​


包含

G
0
	​

I
0
	​

G
0
	​

H
{1}
	​

G
0
	​

H
{2}
	​

+G
0
	​

I
0
	​

G
0
	​

H
{2}
	​

G
0
	​

H
{1}
	​

,

而

G
0
	​

I
1
	​

G
0
	​

H
1
	​


包含

G
0
	​

I
{1}
	​

G
0
	​

H
{2}
	​

+G
0
	​

I
{2}
	​

G
0
	​

H
{1}
	​

.

H
2
	​

,I
2
	​

 必须采用与 fixed

2
1
	​

δ
1
	​

δ
2
	​


jet 相同的 normalization。

Mixed Hessian blocks、gauge fixing、FP、Nielsen–Kallosh sectors 不产生新的 cyclic-word topology；它们产生这些 words 中不同的 allowed closed block paths。该 census exhaustive provided：

H
0
	​

,H
1
	​

,H
2
	​

,I
0
	​

,I
1
	​

,I
2
	​


是 full doubled field-space matrices，包括：

vector and matter blocks；

all off-diagonal mixed blocks；

gauge-fixing blocks；

FP and NK blocks；

source partners；

evanescent blocks；

source-dependent measure/Jacobian terms，或将后者放入 CT
2
	​

。

但该 determinant census 只枚举 graph families。它不执行

Q
phys
	​

=π
+
	​

Δ
R
∗
	​

P
slot
+
	​

.

因此不能由 Hessian formula 跳过 ordered-to-physical exchange sign。

7. GraphIR source-port typing

有四种不同 objects：

GraphIR object	Parity	Koszul treatment
inert insertion anchor	none	excluded from Koszul algebra
odd source J	1	fermionic
differentiated insertion kernel I=δH/δJ	1	fermionic
complete source vertex JI	0	bosonic

因此 label

Source[∇
−
	​

(XX)]

本身不足以决定 type。必须检查 schema semantics。

Case A: inert marker

若该 port 只用于：

graph anchoring；

preventing cyclic overcounting；

associating metadata；

并且不进入 ordered factor list、supertranspose 或 koszul_sign，则它可以是 parityless。将其显示为 “bosonic” 不改变 signs，但最好改成：

statistics = inert

而不是 physical boson。

Case B: complete JI vertex

在 source differentiation 前：

∣JI∣=1+1=0.

此 node 可以 bosonic，但其 payload 必须明确包含 both J and I。

Case C: source leg J

若 port 是 external source J，则：

∣J∣=1.

每穿过一个 odd atomic factor Q：

JQ=−QJ.
Case D: insertion after differentiation

Given

Γ
I
	​

=
δJ
δ
Γ
	​

,

the remaining insertion kernel is odd：

∣I
s
	​

∣=1.

在 Hessian-level word 中，其余 G
0
	​

,H
s
	​

 均 even，所以：

(−1)
∣I
s
	​

∣(∣G
0
	​

∣+∣H
s
	​

∣+⋯)
=+1.

Thus correcting the port from bosonic to odd does not by itself change cyclic signs at the block-Hessian level。

但在 microscopic pre-D word 中，若 the port is moved through individual odd W,
W
,∇,
∇
ˉ
 factors，必须计算 correction。

设旧 schema 将 port 当作 even，而实际 parity 是 one。若某 operation 使它穿过 N
odd
	​

 个 odd factors，则

σ
corrected
	​

=σ
old
	​

(−1)
N
odd
	​

.
	​


对于 “reflection followed by cyclic reanchoring”，port 通常穿过同一组 factors 两次：

N
odd
	​

=2
i
∑
	​

∣Q
i
	​

∣=0(mod2),

所以 correction 为 +1。若 implementation 只反转而不 reanchor，或 marker 固定但 constituents 穿过它一次，则可能产生 minus。

最后必须避免 double counting：

Either treat I as one odd atomic node, or expand its constituents and derive their parity; do not do both.
	​

Final acceptance conditions
O
−
AB
	​

 is exactly antisymmetric and is annihilated by the given source.
	​

The ordered ledger is Adj⊗Adj, but the final local source channel is Sym
2
Adj.
	​

Among the two displayed local tensors, only O
+
	​

 can be a nonzero completion of this seed.
	​

The actual graph reflection sign remains uncomputed without the pre-D word and transfer log.
	​

ker
ℓ
2
	​

=0 is plausible only after a finite quadratic reduction, but is not presently established.
	​


The decisive remaining calculations are:

R
IBP/source jets
	​

,R
placements
	​

,R
commutators
	​

,R
color
	​

,R
evanescent
	​

,L
ℓ
2
	​

	​

.

Only after these matrices satisfy

{v∈kerC:Lv∈B
2
	​

}=imB

may one assert fixed-quadratic-jet injectivity.
