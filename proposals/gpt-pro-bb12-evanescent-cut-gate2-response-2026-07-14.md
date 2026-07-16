# GPT Pro BB12 evanescent cut — Gate 2 response

Status: `NON_AUTHORITY_PRO_REVIEW__PENDING_LOCAL_ADJUDICATION`

Captured: 2026-07-14

Conversation: https://chatgpt.com/c/6a5699d2-4e74-83e8-994f-2a50eeb0c043

---

0. Notation / 记号
A
DC
	​

:=⟨D
D
,C
3
E
	​

⟩,A
CD
	​

:=⟨C
3
D
	​

,D
E
⟩,
v(k):=(−k
+
2
˙
	​

,k
+
1
˙
	​

),detk=k
+
1
˙
	​

k
−
2
˙
	​

−k
+
2
˙
	​

k
−
1
˙
	​

=−
k
ˉ
2
.

Route 002 使用

r
0
	​

=ℓ,r
1
	​

=ℓ−p,r
2
	​

=ℓ−p−q,D
i
	​

=r
i,d
2
	​

.

Route 003 必须 independently reroute：

r
0
	​

=ℓ,
r
1
	​

=ℓ−q,
r
2
	​

=ℓ−p−q,
D
i
	​

=
r
i,d
2
	​

.

定义两个已经完全展开的 scalar prefactors：

P
△
	​

=g
2
(
ℏ
2
	​

g
	​

)(−
ℏ
2
	​

g
	​

)(
16
ℏ
	​

)
3
2!
1
	​

(1+1)=−
2048
ℏg
4
	​

	​


和

P
I
1
	​

H
	​

=g
2
(g
2
	​

)(−
ℏ
2
	​

g
	​

)(
16
ℏ
	​

)
2
=−
128
ℏg
4
	​

.
	​


这里 g
2
	​

 是 gB
r,1
	​

 的 coefficient。固定的 H
−
	​

 flavor port 已经选择了唯一的 ordered monomial；没有额外 2 或 3!。

外场 map：

M
ext
	​

=
−2
−4
2
	​

/g
	​

⋅
g
1
	​

=
g
2
2
2
	​

	​

.
	​

1. Exact first failure: statement 1

令 Π
b
	​

 为到达 H
−
	​

 的 bridge projector，Π
s
	​

 为 outer-marked source-edge projector。二者均为 Grassmann-even。由

D
2
=2D
−
	​

D
+
	​


直接展开：

D
2
(Π
b
	​

Π
s
	​

)=
	​

(D
2
Π
b
	​

)Π
s
	​

+Π
b
	​

(D
2
Π
s
	​

)
+2(D
−
	​

Π
b
	​

)(D
+
	​

Π
s
	​

)−2(D
+
	​

Π
b
	​

)(D
−
	​

Π
s
	​

).
	​

	​


在 route 002,R 的 ordered u,C
3
	​

 projection 中：

(D
2
Π
b
	​

)Π
s
	​

=0

因为 D
2
Π
b
	​

 最终含 D
2
D
2
=0；

2(D
−
	​

Π
b
	​

)(D
+
	​

Π
s
	​

)=0

因为 outer B
2
	​

 source 已含 D
+
	​

，于是产生 D
+
	​

D
+
	​

=0。

剩余两项是：

Π
b
	​

(D
2
Π
s
	​

)

和

−2(D
+
	​

Π
b
	​

)(D
−
	​

Π
s
	​

).

第一项在 pure-antichiral endpoint 上给出

D
2
θ
2
=−4.

第二项通过 superspace IBP 穿过相邻 chiral projector，并由

D
2
D
ˉ
2
D
2
=16
□
ˉ
D
2

产生 bridge inverse kernel。

有限 Grassmann collapse 给出共同的 1024v(r
0
	​

) core：

Π
b
	​

(D
2
Π
s
	​

)⟶(−4)1024v(r
0
	​

)detr
2
	​

=4096v(r
0
	​

)
r
ˉ
2
2
	​

,
−2(D
+
	​

Π
b
	​

)(D
−
	​

Π
s
	​

)⟶(−2)1024v(r
0
	​

)detr
1
	​

=2048v(r
0
	​

)
r
ˉ
1
2
	​

.

因此存在两个不同的 occurrence：

O
002,R
dir
	​

:4096v(r
0
	​

)
r
ˉ
2
2
	​

,e
dir
	​

=2,
	​

O
002,R
tr
	​

:2048v(r
0
	​

)
r
ˉ
1
2
	​

,e
tr
	​

=1.
	​


它们的 coefficient ratio 是严格的

−4
−2
	​

=
2
1
	​

.

它们不能合并，因为 full-d contacts 分别是

D
0
	​

D
1
	​

4096v(r
0
	​

)
	​

,
D
0
	​

D
2
	​

2048v(r
0
	​

)
	​

.

分母集合和 selected edge 均不同。

Statement 1 is the first failed statement.
	​


transported bridge word 是第二个 neighboring-edge occurrence，不是 direct endpoint occurrence 的另一种写法。

2. Pointwise full-d Schwinger pairs
2.1 Route 002: direct source edge
	​

P
△
	​

(+iF
AB
DE
	​

)[
D
0
	​

D
1
	​

D
2
	​

4096
r
ˉ
2
2
	​

v(r
0
	​

)
	​

−
D
0
	​

D
1
	​

4096v(r
0
	​

)
	​

]
=−
2048
ℏg
4
	​

(+iF
AB
DE
	​

)4096[
D
0
	​

D
1
	​

D
2
	​

r
ˉ
2
2
	​

v(r
0
	​

)
	​

−
D
0
	​

D
1
	​

v(r
0
	​

)
	​

]
=−2iℏg
4
F
AB
DE
	​

D
0
	​

D
1
	​

D
2
	​

μ
ℓ
2
	​

v(r
0
	​

)
	​

.
	​


这里 color contraction 是

(T
U
	​

)c
H
−
	​

	​

⟶+iF
AB
DE
	​

.

如果
r
ˉ
2
2
	​

 替换为 r
2,d
2
	​

，方括号逐点为零。

2.2 Route 002: transported bridge edge

transported parent：

P
△
	​

(+iF)
D
0
	​

D
1
	​

D
2
	​

2048
r
ˉ
1
2
	​

v(r
0
	​

)
	​

.

对应的 I
1
	​

S
H
−
	​

	​

 contact D-word 是

−128
D
0
	​

D
2
	​

v(r
0
	​

)
	​

.

其 normalization：

P
I
1
	​

H
	​

(−128)=(−
128
ℏg
4
	​

)(−128)=+ℏg
4
,

而 transported parent 的 normalization 是

P
△
	​

(2048)=(−
2048
ℏg
4
	​

)(2048)=−ℏg
4
.

所以：

	​

P
△
	​

(+iF)
D
0
	​

D
1
	​

D
2
	​

2048
r
ˉ
1
2
	​

v(r
0
	​

)
	​

+P
I
1
	​

H
	​

(+iF)
D
0
	​

D
2
	​

−128v(r
0
	​

)
	​

=−iℏg
4
F[
D
0
	​

D
1
	​

D
2
	​

r
ˉ
1
2
	​

v(r
0
	​

)
	​

−
D
0
	​

D
2
	​

v(r
0
	​

)
	​

]
=
−iℏg
4
F
D
0
	​

D
1
	​

D
2
	​

μ
ℓ
2
	​

v(r
0
	​

)
	​

.
	​

	​


这正是 direct occurrence 的 1/2，但它携带独立的 bridge tag e=1。

2.3 Independently routed route 003

ordered reflection 改变 color word：

(T
V
	​

)c
H
−
	​

	​

⟶−iF
AB
DE
	​

.

相同 D-algebra 给出

+2iℏg
4
F
D
0
	​

D
1
	​

D
2
	​

μ
ℓ
2
	​

v(
r
0
	​

)
	​

	​


和 transported remainder

+iℏg
4
F
D
0
	​

D
1
	​

D
2
	​

μ
ℓ
2
	​

v(
r
0
	​

)
	​

.
	​


这里不是将 route 002 作图形 reflection；使用的是独立 routing

r
1
	​

=
r
0
	​

−q,
r
2
	​

=
r
0
	​

−p−q.
3. Feynman-simplex rank-one moments
3.1 Route 002
D
0
	​

D
1
	​

D
2
	​

1
	​

=2∫
0
1
	​

dy∫
0
1−y
	​

dz
(L
2
+Δ)
3
1
	​

,
r
0
	​

=L+yp+z(p+q).

Odd L integral is zero。并且

2∫
Σ
2
	​

	​

y
	​

=2∫
0
1
	​

y(1−y)dy
=2[
2
1
	​

−
3
1
	​

]=
3
1
	​

,
	​

2∫
Σ
2
	​

	​

z
	​

=2∫
0
1
	​

dy∫
0
1−y
	​

zdz
=2∫
0
1
	​

2
(1−y)
2
	​

dy
=∫
0
1
	​

(1−2y+y
2
)dy
=1−1+
3
1
	​

=
3
1
	​

.
	​


因此

2∫
Σ
2
	​

	​

r
0
	​

=(
3
1
	​

+
3
1
	​

)p+
3
1
	​

q=
3
2
	​

p+
3
1
	​

q.
	​


在 route 002 port assignment 中：

p⟶A
DC
	​

,q⟶A
CD
	​

.

所以

2∫
Σ
2
	​

	​

v(r
0
	​

)⟶
3
2
	​

A
DC
	​

+
3
1
	​

A
CD
	​

.
3.2 Route 003
r
0
	​

=
L
+yq+z(p+q),

故

2∫
Σ
2
	​

	​

r
0
	​

=
3
1
	​

p+
3
2
	​

q.
	​


独立的 reversed ports 给出

2∫
Σ
2
	​

	​

v(
r
0
	​

)⟶
3
1
	​

A
DC
	​

+
3
2
	​

A
CD
	​

.
3.3 Statement 2

p-term 没有乘以任何 external inverse kernel：

p
ˉ
	​

2
,p
d
2
	​

,
q
ˉ
	​

2
,q
d
2
	​


均未出现。因此 2p/3 不是 EOM carrier。

EOM rows 是下文带显式 external square 的 rows；由于 external momenta 是 four-dimensional，

p
ˉ
	​

2
−p
d
2
	​

=0,
q
ˉ
	​

2
−q
d
2
	​

=0

逐点成立。

Statement 2 is false.
	​

4. Normalized parent outputs

共同 external/master factor：

M
ext
	​

I
μ
2
	​

=
g
2
2
2
	​

	​

32π
2
1
	​

.
Direct occurrence
(−2iℏg
4
)
g
2
2
2
	​

	​

32π
2
1
	​

	​

=−
32π
2
4i
2
	​

ℏg
2
	​

=−
8π
2
i
2
	​

ℏg
2
	​

=−2i
2
	​

λ
1
	​

.
	​


因此

Γ
002
dir
	​

=−2i
2
	​

λ
1
	​

F(
3
2
	​

A
DC
	​

+
3
1
	​

A
CD
	​

),
	​

Γ
003
dir
	​

=+2i
2
	​

λ
1
	​

F(
3
1
	​

A
DC
	​

+
3
2
	​

A
CD
	​

).
	​


两者之和：

Γ
△
dir
	​

=λ
1
	​

F(−
3
2i
2
	​

	​

A
DC
	​

+
3
2i
2
	​

	​

A
CD
	​

).
	​


这重现了题目中锁定的 cubic-parent result。

Transported occurrence
(−iℏg
4
)
g
2
2
2
	​

	​

32π
2
1
	​

	​

=−
32π
2
2i
2
	​

ℏg
2
	​

=−
16π
2
i
2
	​

ℏg
2
	​

=−i
2
	​

λ
1
	​

.
	​


所以

Γ
002
tr
	​

=−i
2
	​

λ
1
	​

F(
3
2
	​

A
DC
	​

+
3
1
	​

A
CD
	​

),
	​

Γ
003
tr
	​

=+i
2
	​

λ
1
	​

F(
3
1
	​

A
DC
	​

+
3
2
	​

A
CD
	​

).
	​


合计：

Γ
△
tr
	​

=λ
1
	​

F(−
3
i
2
	​

	​

A
DC
	​

+
3
i
2
	​

	​

A
CD
	​

).
	​


这正是 missing one-third，且由 endpoint product rule 的 −2/−4=1/2 导出。

5. Nonzero occurrence table
id	source occurrence	field loop / ports	vertex–Wick–Koszul factor	raw endpoint-complete D-word	r
e
	​

	full-d contact	μ
ℓ
2
	​

 remainder	moment	normalized output
002-R-dir	I
0,R
kin
	​

	ϕ
1
	​

,ϕ
1
	​

,ϕ
2
	​

; u
D
,C
3
E
	​

	P
△
	​

(+iF)	4096v(r
0
	​

)
r
ˉ
2
2
	​

	r
2
	​

	−4096v(r
0
	​

)/(D
0
	​

D
1
	​

)	4096μ
ℓ
2
	​

v(r
0
	​

)	(2/3,1/3)	−2i
2
	​

λ
1
	​

(2A
DC
	​

/3+A
CD
	​

/3)
002-R-tr	cross term of D
H
2
	​

(Π
1
	​

Π
2
	​

)	same ports	P
△
	​

(+iF)	2048v(r
0
	​

)
r
ˉ
1
2
	​

	r
1
	​

	I
1
	​

S
H
	​

:T
2
	​

=−128v(r
0
	​

)/(D
0
	​

D
2
	​

) with P
I
1
	​

H
	​

	2048μ
ℓ
2
	​

v(r
0
	​

)	(2/3,1/3)	−i
2
	​

λ
1
	​

(2A
DC
	​

/3+A
CD
	​

/3)
003-L-dir	independently routed I
0,L
kin
	​

	ϕ
2
	​

,ϕ
2
	​

,ϕ
1
	​

; C
3
D
	​

,u
E
	P
△
	​

(−iF)	4096v(
r
0
	​

)
r
ˉ
2
2
	​


r
2
	​

	−4096v(
r
0
	​

)/(
D
0
	​

D
1
	​

)	4096μ
ℓ
2
	​

v(
r
0
	​

)	(1/3,2/3)	+2i
2
	​

λ
1
	​

(A
DC
	​

/3+2A
CD
	​

/3)
003-L-tr	transported cross term	same reversed ports	P
△
	​

(−iF)	2048v(
r
0
	​

)
r
ˉ
1
2
	​


r
1
	​

	I
1
	​

S
H
	​

:T
4
	​

=−128v(
r
0
	​

)/(
D
0
	​

D
2
	​

) with P
I
1
	​

H
	​

	2048μ
ℓ
2
	​

v(
r
0
	​

)	(1/3,2/3)	+i
2
	​

λ
1
	​

(A
DC
	​

/3+2A
CD
	​

/3)
6. Six I
1
	​

S
H
−
	​

	​

 rows

展开两个 order-g source words：

2
	​

(D
+
	​

u)ϕ
1
	​

D
+
	​

ϕ
2
	​

,
2
	​

D
+
	​

ϕ
1
	​

(D
+
	​

u)ϕ
2
	​

.

∇
−
	​

 对三个 primitive factors 分别作用，给出六个 occurrence：

X
1
	​

X
2
	​

X
3
	​

X
4
	​

X
5
	​

X
6
	​

	​

=(D
−
	​

D
+
	​

u)ϕ
1
	​

D
+
	​

ϕ
2
	​

,
=−(D
+
	​

u)(D
−
	​

ϕ
1
	​

)D
+
	​

ϕ
2
	​

,
=−(D
+
	​

u)ϕ
1
	​

(D
−
	​

D
+
	​

ϕ
2
	​

),
=(D
−
	​

D
+
	​

ϕ
1
	​

)(D
+
	​

u)ϕ
2
	​

,
=−D
+
	​

ϕ
1
	​

(D
−
	​

D
+
	​

u)ϕ
2
	​

,
=+D
+
	​

ϕ
1
	​

(D
+
	​

u)(D
−
	​

ϕ
2
	​

).
	​

row	source word	regulated D-word result	status
T
1
	​

	X
1
	​

	IBP gives D
+
	​

D
+
	​

Π=0	0
E
1
	​

	X
2
	​

	contains external
q
ˉ
	​

2
;
q
ˉ
	​

2
−q
d
2
	​

=0	EOM row, 0
T
2
	​

	X
3
	​

	−128v(r
0
	​

)/(D
0
	​

D
2
	​

), bridge tag r
1
	​

	nonzero contact
T
4
	​

	X
4
	​

	−128v(
r
0
	​

)/(
D
0
	​

D
2
	​

), bridge tag
r
1
	​

	nonzero contact
T
3
	​

	X
5
	​

	IBP gives D
+
	​

D
+
	​

Π=0	0
E
2
	​

	X
6
	​

	contains external
p
ˉ
	​

2
;
p
ˉ
	​

2
−p
d
2
	​

=0	EOM row, 0

虽然未标记的 four-dimensional local polynomials obey T
2
	​

=T
4
	​

，两行的完整 occurrence data 是

T
2
	​

T
4
	​

	​

color word
+iF
−iF
	​

two denominators
D
0
	​

D
2
	​

D
0
	​

D
2
	​

	​

selected edge
r
1
	​

r
1
	​

	​

external routing
(u
D
,C
3
E
	​

)
(C
3
D
	​

,u
E
)
	​

	​


因此不能写

T
2
	​

−T
4
	​

=0.

它们分别是 route 002 和 route 003 transported parents 的 full-d contacts。

Statement 3 is false.
	​


它的错误是 statement 1 的直接后果。

7. Euler potential versus explicit contact

对 r=1：

−2E
1
pot
	​

=+
2
	​

ε
123
	​

(C
2
	​

×C
3
	​

),

而 descendant 中另有

−
2
	​

ε
123
	​

(C
2
	​

×C
3
	​

).

二者具有相同 flavor、color、kernel 和 occurrence tag：

(+
2
	​

−
2
	​

)ε
123
	​

(C
2
	​

×C
3
	​

)B
2
	​

=0.

对 r=2，记住右 outer mark 的 graded minus：

−B
1
	​

[+
2
	​

ε
231
	​

(C
3
	​

×C
1
	​

)]−B
1
	​

[−
2
	​

ε
231
	​

(C
3
	​

×C
1
	​

)]=0.

这些 cancellation 均在相同 regulated kernel 上逐点发生。它们不消除 transported bridge rows，因为 transported rows 的 selected edges 是 r
1
	​

,
r
1
	​

，而非 source edges r
2
	​

,
r
2
	​

。

8. Exact-zero parent and resolvent ledger
8.1 Cubic route 001
R
001,L
	​

=R
001,R
	​

=0.

两个 outer marks 的 endpoint words 分别含

D
+
	​

D
+
	​

Π=0

或一个 unsaturated
D
ˉ
a
˙
	​

δ，后者在 coincident endpoint 上为零。因此

Γ
001
	​

=0.
	​

8.2 Twelve I
2
	​

 occurrences

令

Q
20
	​

Q
11
	​

Q
02
	​

	​

=[(D
+
	​

u)u−u(D
+
	​

u),ϕ
1
	​

]D
+
	​

ϕ
2
	​

,
=[D
+
	​

u,ϕ
1
	​

][D
+
	​

u,ϕ
2
	​

],
=D
+
	​

ϕ
1
	​

[(D
+
	​

u)u−u(D
+
	​

u),ϕ
2
	​

].
	​


每个 word 有四个 outer marks：

ids	source	marked factors	exact Wick obstruction
I2−20.1–20.4	Q
20
	​

	two u's, ϕ
1
	​

,ϕ
2
	​

	no
ϕ
	​

3
	​

; every connected pairing contains ⟨ϕ
i
	​

ϕ
j
	​

⟩
0
	​

=0
I2−11.1–11.4	Q
11
	​

	two u's, ϕ
1
	​

,ϕ
2
	​

	same exact zero
I2−02.1–02.4	Q
02
	​

	two u's, ϕ
1
	​

,ϕ
2
	​

	same exact zero

所以

⟨I
2
	​

⟩
0
	​

	​

D,C
3
	​

	​

=0.
	​

8.3 I
0
	​

S
4
	​

quartic occurrence	field content	exact zero
M
1
(2)
	​


ϕ
	​

1
	​

uuϕ
1
	​

	source ϕ
2
	​

 has no
ϕ
	​

2
	​

 partner
M
2
(2)
	​


ϕ
	​

2
	​

uuϕ
2
	​

	source ϕ
1
	​

 has no
ϕ
	​

1
	​

 partner
M
3
(2)
	​


ϕ
	​

3
	​

uuϕ
3
	​

	neither source flavor contracts with flavor 3
pure u
4
	four gauge fields	no matter contraction and no C
3
	​

 port
gauge-fixing quartic	gauge fields only	no C
3
	​

 port
ghost quartic	ghost/gauge fields	no matter-flavor port
on-shell scalar quartic	auxiliary-elimination image	canceled exactly by the corresponding auxiliary-exchange row

因此

−ℏ
−1
⟨I
0
	​

S
4
	​

⟩
0,c
	​

	​

D,C
3
	​

	​

=0.
	​

8.4 Other I
1
	​

S
3
	​

 bubbles
cubic vertex	reason
M
1
	​

	only one
ϕ
	​

1
	​

; the source ϕ
2
	​

 remains uncontracted
M
2
	​

	only one
ϕ
	​

2
	​

; the source ϕ
1
	​

 remains uncontracted
M
3
	​

	source flavors 1,2 have no partners
VVV	no C
3
	​

 port
gauge-fixing cubic	no C
3
	​

 port
ghost cubic	no matter-flavor port

唯一 nonzero I
1
	​

S
3
	​

 sector 是上面的 I
1
	​

S
H
−
	​

	​

 contact pair。

8.5 Auxiliary and Jacobian rows

Off-shell propagator blocks obey

⟨F
r
	​

ϕ
	​

s
	​

⟩
0
	​

=0,⟨
F
r
	​

ϕ
s
	​

⟩
0
	​

=0,

所以 auxiliary rows 无 D,C
3
	​

 carrier。

Connection-expansion Jacobian：

STr(ad
u
	​

)=ic
UA
	​

A
=0.

因此 coincident Jacobian 是逐点零：

Γ
Jac
	​

=0.
	​


由此 statement 4 成立。

Statement 4 is true.
	​

9. Canonical normalization adjudication

现有 canonical factors 给出：

P
△
	​

=−
2048
ℏg
4
	​

,P
I
1
	​

H
	​

=−
128
ℏg
4
	​

,
P
△
	​

P
I
1
	​

H
	​

	​

=16.

contact D-words 满足

2048
−128
	​

=−
16
1
	​

.

所以：

P
I
1
	​

H
	​

(−128)=−P
△
	​

(2048),

exactly matching the transported full-d cut。

外场 map：

−2
−4
2
	​

/g
	​

g
1
	​

=
g
2
2
2
	​

	​


也完整；未缺少 flavor factorial、Wick factor 或 field conversion。

Statement 5 is true.
	​

10. Target-blind Project coefficient

先加 direct rows：

c
dir
	​

=(−
3
2i
2
	​

	​

,+
3
2i
2
	​

	​

).

再加 transported neighboring-edge rows：

c
tr
	​

=(−
3
i
2
	​

	​

,+
3
i
2
	​

	​

).

其他 resolvent sectors 全部为零。因此

c
Project
	​

	​

=c
dir
	​

+c
tr
	​

=(−
3
2i
2
	​

	​

−
3
i
2
	​

	​

,
3
2i
2
	​

	​

+
3
i
2
	​

	​

)
=
(−i
2
	​

,+i
2
	​

).
	​

	​


即

Γ
B
1
	​

>B
2
	​

(1)
	​

=λ
1
	​

F
AB
DE
	​

[−i
2
	​

⟨D
D
,C
3
E
	​

⟩+i
2
	​

⟨C
3
D
	​

,D
E
⟩].
	​

11. Sealed comparison

现在读取题目末尾的 conditional row：

λ
1
	​

F
AB
DE
	​

[−i
2
	​

A
DC
	​

+i
2
	​

A
CD
	​

].

Project calculation 给出的 coefficient vector 是

(−i
2
	​

,+i
2
	​

),
	​


与 sealed row 完全相同。

缺失的 one-third 来自

−2(D
+
	​

Π
bridge
	​

)(D
−
	​

Π
source
	​

)
	​


这一 antichiral-endpoint cross term。其系数相对 direct endpoint 的 −4 为

−4
−2
	​

=
2
1
	​

	​

,

其 inverse-kernel tag 从 source edge 移至 neighboring bridge edge，并由 I
1
	​

S
H
−
	​

	​

 的 T
2
	​

/T
4
	​

 contacts 逐点匹配。
