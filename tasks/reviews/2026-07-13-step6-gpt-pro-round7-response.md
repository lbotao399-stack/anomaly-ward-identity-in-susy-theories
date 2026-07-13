# GPT Pro round 7 — focused repair response

- Date: `2026-07-13`
- Role: `EXTERNAL_GAP_REVIEW_ONLY`
- Imported mathematical authority: `false`
- Final coefficient requested: `false`
- Local Project audit remains decisive.

---

Worked for 15m 26s
Notation
Γ=(+,−,
+
˙
	​

,
−
˙
	​

),V
X
	​

=Λ(θ
X
γ
	​

)
γ∈Γ
	​

,dimV
X
	​

=16.

For S⊆Γ,

e
S
X
	​

=
γ∈S
∏
(+,−,
+
˙
	​

,
−
˙
	​

)
	​

θ
X
γ
	​

,∣e
S
	​

∣=∣S∣(mod2).

Π:V→V denotes the parity operator,

Πe
S
	​

=(−1)
∣S∣
e
S
	​

.

K denotes the repository’s exact coefficient field/ring; all equalities below are exact, with no floating-point rank decisions.

The already-certified

(SD)(Euler)(G
V
	​

)=+1

is upstream and remains untouched.

1. Minimal typed pre-aggregation record

The replay seed must be an ordered syntax object, not a canonical monomial.

DerivativeAtom:
    id                  unique immutable ID
    symbol              D_+, D_-, barD_dot+, barD_dot-, or atomic term thereof
    parity              1
    origin:
        Measure(projector_id, word_id, source_position)
        Euler(euler_term_id, word_id, source_position)
        Insertion(insertion_id, word_id, source_position)
    side                LeftDerivative | RightDerivative
    birth_endpoint      A | I
    current_endpoint    A | I | I.port(1..3)
    coordinate_scope:
        Theta(A)
        Theta(I)
        DeltaDifference(A,I)
        FieldPayload(factor_id)
        Momentum(endpoint,q_label)
        Coefficient(coefficient_id)
    target:
        Unassigned | Factor(factor_id) | Delta(e_AI) | Port(1..3)
FactorAtom:
    id
    kind                Field | Coefficient | DeltaAI | Contact | MomentumWord
    parity
    birth_endpoint
    current_endpoint
    coordinate_scope
    original_slot       immutable position in the original ordered product
History:
    parent_contact_id   one of the 608 primitive contacts
    source_basis_id     one of the 16 Grassmann source coordinates
    euler_term_id       one of the six Euler terms
    ast0                immutable ordered product/operator tree
    factor_order0       immutable ordered list of FactorAtom IDs
    derivative_words0  ordered lists of DerivativeAtom IDs
    event_log           append-only list of typed rewrite events
    exact_prefactor     element of K, excluding the audited ± sign
    seed_sign           ±1
    color_word          exact unreduced color expression
    status              LIVE | ALGEBRAIC_ZERO | MISSING_PROVENANCE

Each event must contain its own sign evidence:

SignEvent:
    kind:
        LeibnizCross
        CoefficientCross
        IBP
        WordReversal
        DeltaEndpointTransfer
        CanonicalPermutation
        PortPermutation
        LeftRightDerivativeConversion
    derivative_ids
    crossed_factor_ids
    before_scope
    after_scope
    exponent_mod_2
    exact_scalar        normally ±1, but may contain an exact operator coefficient

The total sign is reconstructed, never merely stored:

σ(H)=σ
seed
	​

(H)
E∈event_log(H)
∏
	​

(−1)
ν(E)
.

Required invariants:

	​

every derivative atom occurs exactly once in its birth word,
origin and source position are immutable,
the current AST is reproducible from (ast
0
	​

,event_log),
no histories are summed before Δ
AI
	​

 convolution and port binding,
nonhomogeneous coefficients are split into homogeneous terms first.
	​


In particular, the record must preserve both

birth_endpoint=A

and a later

current_endpoint=I.port(r).

仅保存 final derivative symbol 或 final canonical monomial 不够。

2. Exact A→I convolution and embedding into the 60 columns
2.1 Correct ordering of compiler stages

The repaired pipeline is

H
608
tagged
	​

⟶CutTransfer
AI
	​

⟶Bind
S
3
	​

	​

⟶TargetAggregate
60
	​

.
	​


The forbidden pipeline is

H
608
	​

⟶Aggregate
A,1568
	​

⇢Target
60
	​

.

All histories which previously cancelled must remain separate until after target-port binding.

2.2 Bare Grassmann convolution

Define the fixed-basis matrices

(C
L
	​

)
ba
	​

=[e
b
I
	​

]∫d
4
θ
A
	​

Δ
AI
	​

e
a
A
	​

,
(C
R
	​

)
ba
	​

=[e
b
I
	​

]∫d
4
θ
A
	​

e
a
A
	​

Δ
AI
	​

.

The existing certificate is

C
L
	​

=C
R
	​

=1
16
	​

.
	​


For a general history, one must nevertheless preserve the actual factor order. Do not commute Δ
AI
	​

 to the left or right merely because both bare matrices are identity.

The exact direct implementation is coefficient extraction:

Conv
AI
	​

[P]=∫d
4
θ
A
	​

P(θ
A
	​

,θ
I
	​

),

where P contains

Δ
AI
	​

=−4(θ
A
+
	​

−θ
I
+
	​

)(θ
A
−
	​

−θ
I
−
	​

)(θ
A
+
˙
	​

	​

−θ
I
+
˙
	​

	​

)(θ
A
−
˙
	​

	​

−θ
I
−
˙
	​

	​

)

in its original ordered position. Every reordering needed to extract the top θ
A
	​

 coefficient produces a recorded Koszul event.

2.3 Measure-word transfer

Let the tagged action-measure word be

W
M
	​

=d
1
	​

d
2
	​

⋯d
m
	​

,

with the convention that d
m
	​

 acts first.

The production rewrite replaces the action-measure node by its one-cut graded transpose,

W
M
	​

⟼σ
cut
	​

(W
M
	​

)W
M,I
rev
	​

,W
M,I
rev
	​

=d
m,I
cut
	​

⋯d
1,I
cut
	​

.

Only atoms with

origin(d
j
	​

)=Measure

are moved by this rule. Euler and insertion atoms obey their original AST scopes; they are not selected by symbol matching.

For plain coordinate derivatives,

∂
θ
A
γ
	​

	​

Δ
AI
	​

=−∂
θ
I
γ
	​

	​

Δ
AI
	​

.

For full D,
D
ˉ
 atoms, including momentum terms, the endpoint-transferred operator must be derived from the locked 16×16 operator matrices. It must not be inferred from the coordinate-derivative formula.

2.4 Distribution over three ordered child ports

For an odd operator d, its exact action on the ordered tensor product

V
p
1
	​

	​

⊗V
p
2
	​

	​

⊗V
p
3
	​

	​


is

d
(1)
=d⊗1⊗1,
d
(2)
=Π⊗d⊗1,
d
(3)
=Π⊗Π⊗d.

Hence the graded Leibniz operator is

L
3
	​

(d)=d⊗1⊗1+Π⊗d⊗1+Π⊗Π⊗d.
	​


For an arbitrary word,

L
3
	​

(W
M
rev
	​

)=L
3
	​

(d
m
cut
	​

)⋯L
3
	​

(d
1
cut
	​

).
	​


This automatically generates all port assignments and all dynamic Koszul signs. No assumption m=4 appears.

A derivative already typed to a specific survivor factor is not expanded with L
3
	​

; after binding that factor to port r, use d
(r)
.

2.5 Six port bijections

For π∈S
3
	​

, define the graded permutation

P
π
	​

(v
1
	​

⊗v
2
	​

⊗v
3
	​

)=(−1)
χ(π;v)
v
π
−1
(1)
	​

⊗v
π
−1
(2)
	​

⊗v
π
−1
(3)
	​

,

where

χ(π;v)=
i<j
π(i)>π(j)
	​

∑
	​

∣v
i
	​

∣∣v
j
	​

∣(mod2).

The bijection acts on immutable survivor IDs, not on their later canonical order.

2.6 Production pseudocode
compile_first_cut():

    emitted_histories = []

    for parent in PrimitiveContacts608:

        require parent.stage == PRE_MEASURE_DISTRIBUTION
        require parent.measure_word is complete
        require parent.factor_order0 is complete
        require every derivative has origin and source_position

        # Preserve the complete AST ordering.
        rewritten = graded_cut_transfer(
            ast              = parent.ast0,
            selected_origin  = Measure,
            edge             = e_AI,
            delta            = Delta_AI
        )

        # Exact theta_A integration; Delta is not commuted by hand.
        at_I = exact_delta_convolution(rewritten, integrate_endpoint=A)

        require no remaining Theta(A) scope

        survivor_ids = ordered_survivor_ids_from_ast(parent.ast0)
        require len(survivor_ids) == 3

        for pi in S3:

            bound = bind_survivor_ids_to_I3_ports(
                at_I,
                survivor_ids,
                pi,
                use_graded_permutation=True
            )

            # Apply the transferred measure word by the graded coproduct.
            # Euler/insertion words are evaluated in their original AST order.
            branches = evaluate_tagged_ast_without_aggregation(bound)

            for branch in branches:
                require no derivative targets I.q1
                emitted_histories.append(branch)

    # Only here may histories be canonicalized and summed.
    source_operators = aggregate_after_port_binding(emitted_histories)

    return source_operators

A second, independent oracle must replay the original measure distribution branch-by-branch, retaining the tags:

oracle_branchwise():

    replay all 608 parents
    distribute the measure projector on the A side with origin tags
    perform the theta_A IBP with full event logs
    do not aggregate
    convolve every raw history across Delta_AI
    bind each history to all six port bijections
    sum only after binding

Production and oracle must agree on the full child-port grid:

Ev(production)=Ev(oracle).
	​

2.7 Embedding into the 60 target columns

Let

T
t,π
	​

,t=1,…,10,π∈S
3
	​

,

be the 60 actual ordered Project I
3
	​

 operator ASTs.

Let

G={0,…,15}
3
.

For a trilinear operator F, define

Ev(F)=(F(e
a
1
	​

	​

,e
a
2
	​

	​

,e
a
3
	​

	​

))
(a
1
	​

,a
2
	​

,a
3
	​

)∈G
	​

.

All root-Grassmann and color components are retained. After flattening these finite components, define

T=[
vecEv(T
1
	​

)
	​

⋯
	​

vecEv(T
60
	​

)
	​

],
Y=[
vecEv(S
1
	​

)
	​

⋯
	​

vecEv(S
16
	​

)
	​

].

The desired matrix C∈K
16×60
 is defined only by

Y=TC
T
.
	​


Let J
col
	​

⊂{1,…,60} be the exactly color-compatible columns, with

∣J
col
	​

∣=10.

Write

T
J
	​

=T[:,J
col
	​

].

A unique coordinate matrix requires an exact left inverse

L
J
	​

T
J
	​

=1
10
	​


and the residual equality

T
J
	​

L
J
	​

Y=Y.
	​


Then, and only then,

X=L
J
	​

Y

defines the compatible part by

(C
T
)
J
col
	​

,:
	​

=X.

No numerical entries are supplied here.

3. Arbitrary odd-word sign formula

Let

W=d
1
	​

d
2
	​

⋯d
m
	​

,∣d
j
	​

∣=1,

and let F be homogeneous. For left derivatives,

∫(dF)G=(−1)
∣F∣+1
∫F(dG).

Repeated integration by parts gives

∫(WF)G=(−1)
m∣F∣+
2
m(m+1)
	​

∫FW
rev
G.
	​


Since

2
m(m+1)
	​

=m+(
2
m
	​

),

the exponent decomposes as

m∣F∣+m+(
2
m
	​

).

These are respectively:

payload-parity crossings,one IBP minus per derivative,reversal of m odd operators.
Coefficient crossings

Let X
j
	​

 be the set of homogeneous coefficients or factors crossed by d
j
	​

 without being differentiated. Then

χ
cross
	​

=
j=1
∑
m
	​

c∈X
j
	​

∑
	​

∣c∣(mod2).

If the complete word crosses a homogeneous coefficient product C, then

χ
cross
	​

=m∣C∣.

Let the endpoint identity for each atomic operator be

d
j,A
	​

Δ
AI
	​

=η
j
	​

d
j,I
cut
	​

Δ
AI
	​

,η
j
	​

∈{±1},

or its exact operator-valued analogue for covariant D,
D
ˉ
.

For one cut transfer,

σ
cut
	​

=σ
0
	​

(−1)
m(1+∣F∣)+(
2
m
	​

)+χ
cross
	​

j=1
∏
m
	​

η
j
	​

.
	​


The transferred word is reversed:

W
I
cut,rev
	​

=d
m,I
cut
	​

⋯d
1,I
cut
	​

.

For plain θ-derivatives, η
j
	​

=−1, hence

σ
cut
	​

=σ
0
	​

(−1)
m∣F∣+(
2
m
	​

)+χ
cross
	​

.

The compiler should not use this simplified form internally; the IBP, reversal, crossing, and endpoint signs should remain separate ledger events.

Explicit branchwise Leibniz sign

Suppose

F
1
	​

F
2
	​

⋯F
n
	​


is the original ordered product, and derivative d
j
	​

 acts on factor F
r
j
	​

	​

. Since d
m
	​

 acts first, the exact branch exponent is

χ
Leib
	​

(r
1
	​

,…,r
m
	​

)=
j=1
∑
m
	​

s<r
j
	​

∑
	​

	​

∣F
s
	​

∣+
k=j+1
∑
m
	​

1
r
k
	​

=s
	​

	​

(mod2).
	​


The inner counting term accounts for parity changes caused by derivatives which have already acted.

The final canonical reordering contributes

χ
can
	​

=
i<j
ρ(i)>ρ(j)
	​

∑
	​

∣x
i
	​

∣∣x
j
	​

∣.

Thus every branch has

χ
total
	​

=χ
seed
	​

+χ
IBP
	​

+χ
reverse
	​

+χ
endpoint
	​

+χ
cross
	​

+χ
Leib
	​

+χ
can
	​

+χ
port
	​

(mod2).
4. The 1568-survivor carrier is information-theoretically insufficient

Let

A:K[H
typed
	​

]⟶C
1568
	​


be the old untyped aggregation map, and let

T:K[H
typed
	​

]⟶Hom(V
⊗3
,R)

be the required cut-transfer plus port-binding map.

The aggregated carrier would be sufficient exactly when there existed a map
T
ˉ
 satisfying

T=
T
ˉ
∘A.

This requires

kerA⊆kerT.
	​


That inclusion fails.

Take two typed histories whose final A-local canonical monomial is identical but in which the same displayed odd derivative has different provenance:

h
M
	​

:origin(d)=Measure,
h
E
	​

:origin(d)=Euler.

After origin erasure,

A(h
M
	​

)=A(h
E
	​

),

so

h
M
	​

−h
E
	​

∈kerA.

But the cut policy moves and redistributes the measure derivative over the bound I
3
	​

 product, while the Euler derivative remains attached to its original typed factor. On a child triple for which the derivative is zero on the original Euler factor but nonzero on another port,

T(h
M
	​

−h
E
	​

)

=0.

Therefore

kerA⊈kerT.

The loss of original factor order gives a second independent obstruction: two histories which become the same canonical A-local product after a graded swap need not produce the same port-labelled operator under the six bijections.

Hence no algorithm can reconstruct the required map from the 1568 aggregated survivors alone.

Earliest object that must be replayed

The minimal lossless replay point is

the 608 primitive edge-square contact ASTs, before measure-projector distribution.
	​


All branches must be regenerated with tags, including histories which later contributed to the 448 old zero-sum certificates.

The 2432 raw objects are sufficient only if they are regenerated with:

measure origin,source word position,original factor IDs/order,complete sign ledger.

The currently retained later-θ
A
	​

-IBP histories are too late.

If the stored “608 object” is only a count or already lacks the undistributed measure word, then the replay must begin one stage earlier from the six Euler-term ASTs which generated those contacts.

5. Finite machine certificates
5.1 Replay coverage

Let P
rh
	​

 be the exact parent-incidence matrix between the 608 primitive contacts and the regenerated raw histories.

Required:

P
T
1
608
	​

=1
raw
	​

,

meaning every raw history has exactly one parent.

The row-sum vector

b=P1
raw
	​


must be computed from the actual AST branching rules, with

r=1
∑
608
	​

b
r
	​

=2432.

One must not infer b
r
	​

=4 merely from 2432/608=4.

5.2 Exact regression to the old carrier

Let F
forget
	​

 erase the new provenance tags and let R
old
	​

 implement the old canonical reduction. Then require exact equality of coefficient-labelled carriers:

R
old
	​

F
forget
	​

(H
replay
	​

)=C
1568
stored
	​

.
	​


Matching only

2432,1568,448

is not a certificate.

Every stored zero-sum relation z
α
	​

 must satisfy its exact old equality, for example

R
old
	​

z
α
	​

=0,

with its original coefficients and signs.

5.3 Delta certificates

Retain the existing equalities

C
L
	​

=C
R
	​

=1
16
	​

.
	​


For every distinct derivative word and every left/right placement encountered in the 608 replay, compute:

K
direct
	​

(W)

by direct Grassmann expansion and θ
A
	​

 integration, and

K
ledger
	​

(W)

from the reversal/crossing/endpoint rules.

Require

K
direct
	​

(W)=K
ledger
	​

(W)
	​


as exact 16×16 matrices.

5.4 Three-port Leibniz certificate

Let L
3
branch
	​

(W) be the matrix obtained by explicit branch enumeration.

Require

L
3
branch
	​

(W)=L
3
	​

(d
1
	​

)⋯L
3
	​

(d
m
	​

)
	​


as exact 4096×4096 matrices for every word used.

5.5 Port-permutation certificate

For all π,σ∈S
3
	​

,

P
id
	​

=1
4096
	​

,P
π
	​

P
σ
	​

=P
πσ
	​

.
	​


For every target term,

Ev(T
t,π
	​

)

must equal the exact graded-permutation evaluation of the identity-port ordering, according to the repository’s declared convention.

5.6 Complete 16
3
 operator equality

For every source basis index a=1,…,16 and every child triple

(i,j,k)∈{0,…,15}
3
,

require

S
a
	​

(e
i
	​

,e
j
	​

,e
k
	​

)=
c=1
∑
60
	​

C
ac
	​

T
c
	​

(e
i
	​

,e
j
	​

,e
k
	​

).
	​


All root Grassmann and color components must agree exactly.

This check is complete because

{e
i
	​

⊗e
j
	​

⊗e
k
	​

}
i,j,k=0
15
	​


is a basis of V
⊗3
. Equality on the 16
3
 grid is therefore equality of trilinear operators, not a dimension heuristic.

5.7 Exact target-span and uniqueness certificate

For the ten exactly compatible columns,

rankT
J
	​

=10,
	​

rank[
T
J
	​

	​

Y
	​

]=10.
	​


Prefer the stronger explicit certificate

L
J
	​

T
J
	​

=1
10
	​

,T
J
	​

L
J
	​

Y=Y.
	​


If

kerT
J
	​


=0,

the 16×60 coefficient matrix is not unique. The compiler must return

FAIL_TARGET_COORDINATES_NONUNIQUE

unless an independently specified quotient and canonical section are supplied.

5.8 Forbidden I.q1 action

This must hold at event level:

∀H,∀d∈H:target(d)

=I.q1.
	​


A cancellation of I.q1-derivative terms after summation is weaker and is not acceptable.

6. Genuine zero versus missing provenance

Each of the 60 columns must carry one of the following states.

State	Meaning
COMPUTED	Complete replay gives an exact coefficient vector
PROVEN_ZERO_COLOR	Exact color typing proves no admissible color morphism
PROVEN_ZERO_SUM	Complete typed preimage was enumerated and its exact sum is zero
TARGET_NULL	The target operator itself vanishes on the full 16
3
 grid
MISSING_PROVENANCE	At least one required history lacks measure/order/sign data
OUT_OF_TARGET_SPAN	Replayed source operator is not in the 60-column span

Only

PROVEN_ZERO_COLOR
PROVEN_ZERO_SUM

may be serialized as coefficient-zero columns.

TARGET_NULL means the target carrier has a null/redundant generator; it does not determine its coefficient.

“No graph incidence” is not a zero certificate. A column with no routed history is zero only when exhaustive typed enumeration proves that its preimage is empty.

The 50 color-incompatible columns are genuine typed zeros only after an exact color-algebra certificate, such as

Hom
color
	​

(C
cut
	​

,C
j
	​

)=0,

not merely because the formal graph matcher omitted them.

Fail-closed acceptance condition

A 16×60 matrix may be emitted only if

ACCEPT=
	​

CompleteTags∧Complete608Replay∧OldCarrierRegression
∧(C
L
	​

=C
R
	​

=1
16
	​

)∧AllWordTransferChecks
∧AllPortGridChecks∧ExactColorTyping
∧TargetSpan∧TargetCoordinateUniqueness
∧NoMissingProvenance∧NoUnresolvedColumns.
	​

	​


Otherwise:

return failure_status
do_not_allocate_numeric_16x60_matrix
do_not_replace_unknown_entries_by_zero

For the currently described repository state, the correct result remains

MISSING_TYPE::MeasureTaggedDeltaConvolutionBeforeContactAggregation

and the minimal repair is the tagged replay from the 608 pre-distribution primitive contacts.
