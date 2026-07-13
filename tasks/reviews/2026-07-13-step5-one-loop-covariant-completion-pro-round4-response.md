# Step 5 one-loop covariant completion — Pro review round 4 response

> Exact browser `innerText` capture. Rendered display formula spacing is preserved as returned by the browser; this file is gap-review evidence only and is not formula authority.

Audit status

The following Project-side statements are internally consistent, subject to the indicated normalization conventions:

O
+
BA
	​

=O
+
AB
	​

,

because

c
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

,

and the D,E-word in O
+
	​

 is symmetric after the exact reflected replay.

The family counts are also correct:

N
family
	​

(n)=1+
m=1
∑
n
	​

2
m−1
=2
n
.

For labeled external legs, writing

F
m
	​

:=
k=0
∑
m
	​

k!S(m,k)

for the ordered Bell number,

N
pol
	​

(n)=
s=0
∑
n
	​

(
s
n
	​

)F
n−s
	​

,

hence

N
pol
	​

(2)=6,N
pol
	​

(3)=26,N
pol
	​

(4)=150.

This assumes:

H
r
	​

[S], I
s
	​

[S]

are labeled functional derivatives with no hidden additional 1/r! or 1/s!, and the insertion I fixes the cyclic root.

1. What fixed-jet injectivity actually proves

Let

H
loc
	​

=
imB
Σ
	​

+I
EOM
	​

+I
IBP
	​

+I
ev
	​

kerB
Σ
	​

	​


be the fixed source/color/Spin sector, and let

ℓ
ˉ
2
	​

:H
loc
	​

⟶T
2
	​


be the induced quadratic-jet map.

The exact implication is

ker
ℓ
ˉ
2
	​

=0,
ℓ
ˉ
2
	​

[A
loc
(1)
	​

]=C
2
	​

ℓ
ˉ
2
	​

[O
⋆
	​

]⟹[A
loc
(1)
	​

]=C
2
	​

[O
⋆
	​

].
	​


The conclusion is an equality of cohomology classes, not necessarily bare local representatives:

A
loc
(1)
	​

=C
2
	​

O
⋆
	​

+B
Σ
	​

Ξ+E+dY+E
ev
	​

.
	​


After expanding in the background,

A
loc,n
(1)
	​

=C
2
	​

O
⋆,n
	​

+(B
Σ
	​

Ξ)
n
	​

+E
n
	​

+dY
n
	​

+E
ev,n
	​

.

Therefore injectivity proves

[A
loc,n
(1)
	​

]=C
2
	​

[O
⋆,n
	​

]∀n,
	​


provided the local functional is analytic in the background variables and all Taylor maps preserve the chosen quotient.

It does not prove the literal identity

Γ
I,n
(1)
	​

=C
2
	​

O
⋆,n
	​

.

The complete 1PI result can contain

Γ
I,n
(1)
	​

=Γ
I,n
nonlocal,transverse
	​

+C
2
	​

O
⋆,n
	​

+B
Σ
	​

Ξ
n
	​

+E
n
	​

+dY
n
	​

.
	​


Thus:

Injectivity fixes the nontrivial local covariant dressing, not every full box/pentagon/higher 1PI sum.
	​


Also, the datum being completed is not an isolated triangle topology. It is

ℓ
ˉ
2
	​

[A
loc
(1)
	​

],

extracted from the complete six-term quadratic family.

2. Fixed-ℓ
2
	​

 counterexample audit
2.1 Strict physical four-dimensional cubic sector

A class with vanishing quadratic jet that is not represented at lower order would have to start at field-strength degree N≥3.

At dimension 9/2, three field strengths exhaust the dimension:

3⋅
2
3
	​

=
2
9
	​

.

The formal grading equations are

n
W
	​

+n
W
	​

=3,
n
W
	​

−n
W
	​

=−1.

Hence uniquely

n
W
	​

=1,n
W
	​

=2.

The Lorentz decomposition is

(
2
1
	​

,0)⊗(0,
2
1
	​

)⊗(0,
2
1
	​

)
	​

=(
2
1
	​

,0)⊗[(0,0)⊕(0,1)]
=(
2
1
	​

,0)⊕(
2
1
	​

,1).
	​


Therefore

[W
W
W
]
(3/2,0)
	​

=0.
	​


Four field strengths are excluded because

4⋅
2
3
	​

=6>
2
9
	​

.

Hence there is no ordinary four-dimensional field-strength-degree-≥3 counterexample in the fixed target representation.

2.2 The intended filtration proof

Let gr
N
	​

H denote the associated graded space in field-strength degree. The required argument is:

gr
0
	​

H=0,
gr
1
	​

H=0,
gr
2
	​

H=span{C
K
	​

},
ker(ℓ
2
	​

:gr
2
	​

H→T
2
	​

)=0,
gr
3
	​

H=0,gr
N≥4
	​

H=0.

Then any [O]∈ker
ℓ
ˉ
2
	​

 can successively be represented in higher filtration:

[O]∈F
≥2
	​

,

injectivity at degree two gives

[O]∈F
≥3
	​

,

and

F
≥3
	​

=0.

This would prove

ker
ℓ
ˉ
2
	​

=0.

The quoted ranks establish substantial pieces of this argument, but they do not yet certify the passage from the free associated-graded calculation to the physical BRST/DRED quotient.

2.3 No certified physical counterexample

From the supplied data I do not obtain an indexed, strictly four-dimensional, physical pure-gauge counterexample that survives:

Bianchi+EOM+IBP+color+source-BRST.

Accordingly:

No counterexample is supplied, but injectivity is not certified.
	​


The first missing local-algebra obligation is

M
D−D pairing
	​

,
	​


because a difference of quadratic derivative placements can have zero free quadratic symbol while producing curvature children through

[D,D],[∇,D],[
∇
ˉ
,D].

One must prove that every such child either:

lands in the already identified C
K
	​

 carrier,

or lies in

I
EOM
	​

+I
Bianchi
	​

+I
IBP
	​

.

For the actual physical theorem, however, the minimal certificate is not one scalar rank. It is the combined induced-kernel identity

{v∈kerC
full
	​

:L
full
	​

v∈imB
2,full
	​

}=imB
full
	​

,
	​


where B
full
	​

 includes all four missing blocks:

M
D−D
	​

,M
source−BRST
	​

,M
color−Sym
2
Adj
	​

,M
DRED−evanescent
	​

.
2.4 A DRED kernel candidate, not a certified counterexample

If the DRED background includes epsilon-scalar components, define

D
a
a
˙
(ϵ)
	​

:=σ
a
a
˙
μ
	​

δ
μ
	​

ν
D
ν
	​

.

Then an evanescent symmetric-source operator is

E
abc
AB
	​

:=δ
(A
C
	​

δ
B)
D
	​

[
	​

W
α
˙
C
	​

D
(a
(ϵ)
	​

α
˙
X
bc)
D
	​

+D
(a
(ϵ)
	​

α
˙
X
bc)
C
	​

W
α
˙
D
	​

].
	​

	​


It has

[E]=
2
9
	​

,∣E∣=1,r
f
	​

(E)=−1,(j
L
	​

,j
R
	​

)=(
2
3
	​

,0),

and

E
AB
=E
BA
.

At quadratic order,

D
ν
	​

⟶ip
ν
	​

,
δ
μ
	​

ν
p
ν
	​

=0,

so

ℓ
2
	​

[E]=0.
	​


At nonlinear order,

D
(ϵ)
X=σ
μ
δ
μ
	​

ν
(∂
ν
	​

X+[A
ν
	​

,X]),

and the A
ϵ
	​

-commutator need not vanish.

This is an explicit temporary evanescent kernel candidate. It is not yet a cohomological counterexample because the following are unspecified:

epsilon-scalar EOM,
DRED Bianchi completion,
source-jet IBP involving D
(ϵ)
J,
BRST exactness in the enlarged DRED complex.

If Project external backgrounds are restricted by

δ
μ
	​

ν
A
ν
	​

=0,

then E vanishes and is not a direction at all.

3. Free symbolic color injectivity versus physical color quotient

Suppose the free result genuinely factorizes as

ℓ
2
free
	​

=L
Lor
	​

⊗id
K
free
	​

	​

,

with

L
Lor
	​

(1)=(
1
−1
	​

),kerL
Lor
	​

=0.

For any vector-space quotient

q:K
free
	​

→K
phys
	​

,

if the induced physical map is exactly

ℓ
2,phys
	​

=L
Lor
	​

⊗id
K
phys
	​

	​

,

then

kerℓ
2,phys
	​

=0
	​


without any separate scalar color-rank calculation:

L
Lor
	​

⊗K=0⟹K=0.

However, the free symbolic calculation does not by itself prove that the domain and quadratic-jet target undergo the same color quotient.

The required commutative square is

H
free
	​

q
H
	​

↓
⏐
	​

H
phys
	​

	​

ℓ
2
free
	​

	​

ℓ
2,phys
	​

	​

	​

T
2,free
	​

↓
⏐
	​

q
T
	​

T
2,phys
	​

.
	​


The required color condition is

q
T
	​

ℓ
2
free
	​

(x)=0⟹q
H
	​

(x)=0.
	​

3.1 Exact physical color module

Before using the plus-word identification, the safe definition is

K
phys
	​

=
R
g
	​

+kerP
exchange
+
	​

{K
AB
CD
	​

:K
AB
CD
	​

=K
BA
CD
	​

,K is a g-intertwiner}
	​

.

Gauge covariance requires, for every generator t
x
	​

,

0=
	​

(t
x
	​

)
A
A
′
	​

K
A
′
B
CD
	​

+(t
x
	​

)
B
B
′
	​

K
AB
′
CD
	​

−K
AB
C
′
D
	​

(t
x
	​

)
C
′
C
	​

−K
AB
CD
′
	​

(t
x
	​

)
D
′
D
	​

.
	​


The combined exchange projector acts simultaneously on color and the two field-species orientations:

P
exchange
+
	​

(K
CD
	​

⊗e
1
	​

)=
2
1
	​

(K
CD
	​

⊗e
1
	​

+K
DC
	​

⊗e
2
	​

).

After identifying the plus carrier with one orientation, this is equivalent to

K
phys
	​

≃Hom
g
	​

(Sym
2
Adj,Sym
2
Adj)
	​


modulo the selected trace/single-trace/multi-trace restrictions.

The color matrix must impose:

Jacobi,metric invariance,group-specific trace identities,
J
AB
	​

=J
BA
	​

,
trace versus traceless source,
single-trace versus multi-trace channel.
Consequence

A separate scalar color-rank computation is:

not needed for injectivity, if the identity-factorization survives this quotient;

still needed for a rank-one or one-scalar-coefficient corollary, because one must determine

dimK
phys
	​


or its irreducible-channel multiplicities.

If

Sym
2
Adj=
λ
⨁
	​

m
λ
	​

R
λ
	​

,

then

End
g
	​

(Sym
2
Adj)≃
λ
⨁
	​

Mat
m
λ
	​

	​

.

A scalar C
2
	​

 is justified only after selecting a channel for which the relevant multiplicity is one.

4. DRED evanescent local-jet directions

Set

n
ϵ
	​

:=
δ
μ
μ
	​

=2ϵ,

and decompose the evanescent projector into its four-dimensional trace and traceless spurion:

δ
μν
	​

=
4
n
ϵ
	​

	​

δ
(4)μν
	​

+e
μν
	​

,δ
(4)
μν
	​

e
μν
	​

=0.
	​


Under formal Spin(4),

4
n
ϵ
	​

	​

δ
(4)μν
	​

∈(0,0),e
μν
	​

∈(1,1).

The scalar n
ϵ
	​

 is therefore only one evanescent direction. The traceless e
μν
	​

 directions cannot be replaced by 2ϵ.

4.1 Maximum projector degree

The raw census contains at most four vector-derivative slots. Therefore a local dimension-9/2 jet can contain at most two independent pairwise evanescent projector insertions:

q=1, 2.

For one projector, the spurion representations are

S
1
	​

=(0,0)⊕(1,1).
	​


For two commuting projector insertions,

Sym
2
S
1
	​

=2(0,0)⊕2(1,1)⊕(2,0)⊕(0,2)⊕(2,2).

Thus the temporary evanescent target module is

E
(3/2,0)
	​

=
q=1
⨁
2
	​

λ⊂S
q
	​

⨁
	​

Hom
Spin(4)
	​

[(
2
3
	​

,0),R
raw
	​

⊗λ]⊗K
phys
	​

,
	​


followed by quotienting by DRED Bianchi, EOM, IBP and source-BRST relations.

This is the exact classification formula. A numerical dimension cannot be extracted from the supplied data because R
raw
	​

, including every vector-slot placement, has not been supplied.

4.2 Independent structural families

The temporary basis must separately include:

Scalar-trace directions
n
ϵ
	​

M
i
	​

,n
ϵ
2
	​

M
i
	​

.

At primitive one loop only terms linear in n
ϵ
	​

 can combine with a simple 1/ϵ pole to produce a finite term, but n
ϵ
2
	​

 may be discarded only after complete index reduction establishes its order.

Single nontrace-projector directions
e
μν
	​

M
i
μν
	​

.
Double-projector directions
δ
μν
	​

δ
ρσ
	​

M
i
μνρσ
	​

,

including the inequivalent slot pairings

(μν)(ρσ),(μρ)(νσ),(μσ)(νρ).
Epsilon-scalar covariant letters
D
μ
	​

	​

,F
μ
	​

ν
	​

,F
μ
	​

ν
	​

,

and their superspace descendants.

Evanescent sigma-chain/Fierz directions

All independent words containing

σ
a
a
˙
μ
	​

:=
δ
μ
ν
	​

σ
a
a
˙
ν
	​

,

or multiple projected sigma matrices, before using four-dimensional Fierz identities.

4.3 Effect of 
p
	​

-routing

For every external momentum,

p
μ
=
p
	​

μ
,

hence

δ
μν
	​

p
ν
=0.
	​


This eliminates any branch in which a free evanescent projector acts directly on an external momentum.

It does not eliminate projectors acting on:

background polarizations,
epsilon-scalar connections,
internal sigma chains,
commutator-generated vector indices.

Therefore the scalar replacement

δ
μ
μ
	​

=2ϵ

is justified only if the Project additionally proves

δ
μ
ν
	​

B
ν
=0

for every external background and proves that every remaining closed sigma chain reduces to the scalar trace.

The smallest missing DRED datum is consequently:

the exact DRED lift of the external background multiplet: are epsilon-scalar background components retained or projected out?
	​


Without that datum, a complete independent evanescent basis cannot be numerically classified.

5. Chiral/vector quantum tangent intertwiner

Start from the exact operator relation

∇
C
=B
−1
∇
V
B.

Hold the background bridge fixed and vary only quantum fields:

δ
q
	​

∇
C
=B
−1
(δ
q
	​

∇
V
)B.

Represent the quantum tangent by an adjoint-valued even field υ:

δ
q
	​

∇
V
=[∇
V
,υ
V
	​

],
δ
q
	​

∇
C
=[∇
C
,υ
C
	​

].

Then

[∇
C
,υ
C
	​

]
	​

=B
−1
[∇
V
,υ
V
	​

]B
=[∇
C
,B
−1
υ
V
	​

B].
	​


Thus

υ
C
	​

−B
−1
υ
V
	​

B

is covariantly constant. After removing the stabilizer/central zero mode by gauge fixing,

υ
C
	​

=Ad
B
−1
	​

υ
V
	​

.
	​


Therefore the linearized quantum tangent map is

T
B
	​

=Ad
B
−1
	​

.
	​


For a field in representation R,

T
B,R
	​

=ρ
R
	​

(B
−1
),

while dual or antichiral blocks use the corresponding inverse/right action or 
B
, according to their representation.

5.1 Endomorphism similarity

For a covariant endomorphism acting on tangent sections,

H
C
	​

=T
B
	​

H
V
	​

T
B
−1
	​

.
	​


Likewise,

I
C
	​

=T
B
	​

I
V
	​

T
B
−1
	​

,
G
C
	​

(z,z
′
)=T
B
	​

(z)G
V
	​

(z,z
′
)T
B
−1
	​

(z
′
).

This is distinct from the transformation of a raw two-lower-index Hessian, which is a congruence after transforming the field-space pairing.

5.2 Nonlinear background-split map

Let the actual prepotential coordinates be related by

ϕ
C
	​

=F
B
	​

(ϕ
V
	​

),

with

DF
B
	​

	​

ϕ=0
	​

=T
B
	​

.

The bridge similarity determines DF∣
0
	​

, but not the full nonlinear function F
B
	​

.

For the actions,

S
V
	​

(ϕ
V
	​

)=S
C
	​

(F
B
	​

(ϕ
V
	​

)),

the raw Hessians satisfy

H
V
	​

=T
B
st
	​

H
C
	​

T
B
	​

+⟨S
C
(1)
	​

,D
2
F
B
	​

⟩.
	​


The second term vanishes only at a stationary quantum background or after an appropriate covariant Hessian construction.

The nonlinear change of variables has Jacobian

logJ
F
	​

=STr
DRED
	​

logDF
B
	​

[ϕ].
	​


The linear adjoint conjugation has unit Jacobian if

Tr
Adj
	​

(ad
η
	​

)=0

and regulated cyclicity is exact. This does not prove that the full nonlinear F
B
	​

 has unit Jacobian.

Consequence
The nonlinear Jacobian blocks cross-frame functional equality only.
	​


It does not obstruct the fixed Step-5A vector-frame theorem, because that theorem uses neither F
B
	​

 nor a chiral-frame measure comparison.

6. Finite background covariance certificate

For finite R, the appropriate proof is a path argument. Let R
t
	​

 interpolate between 1 and R. Then

dt
d
	​

STr
DRED
	​

(R
t
	​

MR
t
−1
	​

)=STr
DRED
	​

[
R
˙
t
	​

R
t
−1
	​

,R
t
	​

MR
t
−1
	​

].

If the regulated commutator trace vanishes, including routing translation and boundary terms,

dt
d
	​

STr
DRED
	​

(R
t
	​

MR
t
−1
	​

)=0.

Therefore

STr
DRED
	​

(RMR
−1
)=STr
DRED
	​

M.

Applying this to

M=GI

gives background covariance of the rooted functional in the fixed vector frame.

This certificate does not replace the vertex-level GraphIR Ward replay; it proves the functional identity but not that the current graph generator contains every required pinched/contact graph with the correct local routing metadata.

7. C
2
	​

=C
△
	​

 is a separate calculation

Define the complete polygonal triangle family

Q
△
	​

:=
2
1
	​

STr[
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

[1]G
0
	​

H
1
	​

[2]G
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

[2]G
0
	​

H
1
	​

[1]G
0
	​

].
	​

	​


Define the complete quadratic contact family

Q
contact
	​

:=
2
1
	​

STr[
	​

−I
0
	​

G
0
	​

H
2
	​

[1,2]G
0
	​

−I
1
	​

[1]G
0
	​

H
1
	​

[2]G
0
	​

−I
1
	​

[2]G
0
	​

H
1
	​

[1]G
0
	​

+I
2
	​

[1,2]G
0
	​

]+CT
2
	​

.
	​

	​


Then

Γ
I,2
(1)
	​

=Q
△
	​

+Q
contact
	​

.

Let

P
⋆
	​

:T
2
	​

⟶C

be the fixed quadratic cohomological projector in a one-dimensional selected color channel. Define

C
△
	​

=
P
⋆
	​

ℓ
2
	​

[O
⋆
	​

]
P
⋆
	​

[Q
△
	​

]
loc
	​

	​

,
C
contact
	​

=
P
⋆
	​

ℓ
2
	​

[O
⋆
	​

]
P
⋆
	​

[Q
contact
	​

]
loc
	​

	​

.

Then

C
2
	​

=C
△
	​

+C
contact
	​

.
	​


Therefore

C
2
	​

=C
△
	​

⟺P
⋆
	​

[Q
contact
	​

]
loc
	​

=0.
	​


More invariantly, without assuming a scalar target:

C
2
	​

=C
△
	​

⟺[Q
contact
	​

]
T
2
	​

	​

=0.
	​


Background covariance proves only that the sum

Q
△
	​

+Q
contact
	​


obeys the background Ward identity. It does not prove

[Q
contact
	​

]
T
2
	​

	​

=0.

The contact family can contain the same transverse local covariant tensor as the triangle.

The required independent cancellation calculation must include:

I
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

,

and all:

mixed Hessian species paths,
gauge-fixing contributions,
FP/Nielsen–Kallosh blocks,
source-partner blocks,
ϵ/ϵ evanescent remnants,
routing/reflection signs,
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

 pinches.

A vanishing tadpole or scaleless-integral argument must be made separately for every contact class; it cannot be inferred from covariance.

Also, C
△
	​

 must mean the sum of both labeled triangle orientations and all allowed internal species paths. A single geometric orientation does not define a representation-independent coefficient.

Final fail-closed conclusions
Question 1
Yes for the nontrivial local cohomology class; no for the complete 1PI box/pentagon/higher sums.
	​


The exact conclusion is

[A
loc,n
(1)
	​

]=C
2
	​

[O
⋆,n
	​

],

not an equality including nonlocal transverse and trivial local terms.

Question 2
No certified strict four-dimensional counterexample is obtained.
	​


The cubic representation is empty, but the missing D−D, source-BRST, color and DRED matrices prevent an injectivity claim. An epsilon-scalar operator provides a concrete temporary DRED kernel candidate if such backgrounds are retained.

Question 3
Free symbolic-color injectivity removes a scalar color-rank test only if ℓ
2
	​

=L
Lor
	​

⊗id
K
phys
	​

	​

 survives the physical quotient.
	​


The required quotient is the gauge-intertwiner space for the combined plus-exchange channel, equivalently

Hom
g
	​

(Sym
2
Adj,Sym
2
Adj)

with all group and trace relations imposed.

Question 4
The evanescent module contains scalar and nontrace projector spurions up to projector degree two.
	​


A numerical independent basis is impossible until the DRED lift of the external background multiplet and epsilon-scalar policy is fixed.

Question 5
T
B
	​

=Ad
B
−1
	​

	​


on the adjoint quantum tangent, modulo stabilizer modes. The nonlinear split Jacobian affects cross-frame equality only, not the fixed-vector-frame Step-5A theorem.

Question 6
C
2
	​

=C
△
	​

	​


remains an independent quadratic contact-cancellation statement:

[Q
contact
	​

]
T
2
	​

	​

=0.

It does not follow from covariance, injectivity, or the all-order Ward certificate.

