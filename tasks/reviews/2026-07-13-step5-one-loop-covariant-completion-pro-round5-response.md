# GPT Pro round 5 response — one-loop covariant-completion gap review

Conversation: https://chatgpt.com/c/6a553e0b-0918-83e8-8839-727b3bc94905

Notation used below. P: true physical N=1 parent-generator space; T: terminal normal-order word space; A:P→T: parent-incidence map; R
T
	​

: terminal relation matrix; Q
T
	​

: quotient map with kerQ
T
	​

=imR
T
	​

; D,B: CE/BRST differential and boundary maps; J
2
	​

: quadratic-jet map.
P0 means theorem-blocking; P1 means required for a complete verification or broader claim.

1. Physical-4d versus full-DRED

Yes, at the level of complexes/modules; 尚未 automatically at the renormalized-class level.

The required commuting structure is

q
4d,2
	​

∘ℓ
2
DRED
	​

=ℓ
2
4d
	​

∘q
4d
	​

,q
4d
	​

∘d
CE
	​

=d
CE
	​

∘q
4d
	​

.

With the evanescent ideal

E
ev
	​

:=kerq
4d
	​

,C
4d
	​

=C
DRED
	​

/E
ev
	​

,

one may have

0

=E∈kerℓ
2
DRED
	​

∩E
ev
	​


while nevertheless

ker
ℓ
ˉ
2
4d
	​

=0.

Therefore failure of full-DRED injectivity does not imply failure of physical-4d injectivity, and physical-4d injectivity does not imply full-DRED injectivity.

However, the bifurcation is sufficient for the renormalized local class only after proving that:

the evanescent ideal is stable under CE/BRST and all terminal relations;

subtraction/pole extraction descends to the quotient;

1/ϵ-enhanced evanescent operators cannot generate a surviving physical local term after contraction or operator mixing.

Without item 3, “project to 4d” and “renormalize” need not commute.

2. Status of the explicit τ word
Raw carrier

Yes, conditionally. If τ is an allowed generator of the full-DRED coefficient tensor algebra and the displayed word is nonzero after all raw algebraic relations, then

ℓ
2
	​

(E)=0,∂
t
3
	​

E(tB)
	​

t=0
	​


=0

is an explicit kernel element. It refutes raw carrier-level quadratic-jet injectivity.

CE/cohomological map

It does not yet refute injectivity of an induced map 
ℓ
ˉ
2
	​

 unless one also proves

d
CE
	​

E=0,

and

E∈
/
imd
CE
	​

+R
terminal
	​

+I
IBP
	​

+I
EOM
	​

.

A nonzero SU(2) color evaluation proves that the displayed polynomial is not universally color-zero. It does not by itself prove nontriviality in the CE/normal-order quotient.

There is also an admissibility issue. The two contractions

δ
(4)mn
	​

τ
mn
=0,τ
mn
	​

τ
mn
=2ϵ−ϵ
2

do not by themselves show that τ belongs to the actual DRED tensor algebra. One must identify it with the genuine DRED projector decomposition and verify the full projector, orthogonality, and spinor-conversion relations—not merely its trace and norm.

Possible exclusion axiom

No listed dimension, parity, R-weight, source symmetry, or spurionic Spin(4) weight excludes it.

It is excluded only by an explicit axiom such as

R
admissible
	​

=R
physical
	​

,

meaning that local functionals may contain physical invariant tensors only, with no explicit 
δ
, τ, or other regulator spurions; or by defining the domain only after quotienting by kerq
4d
	​

.

A fixed τ is not a Spin(4) singlet. Treating it as a transforming spurion makes the resulting word covariant. Thus “Spin(4) covariance” excludes it only when the theory explicitly forbids regulator spurions. Calling such a restricted domain “raw full-DRED” would be misleading.

3. Minimal non-tautological matrix certificate

The 4866 normal-order event/branch-path coordinates cannot be used as the parent basis. The minimal certificate requires the following exact presentation.

Source presentation

Let

A:P⟶T

map the true independent N=1 parent generators to terminal normal-order coordinates.

Let

R
T
	​

:U
T
	​

⟶T

have image equal to all terminal relations. An independently constructed canonical normal-form map Q
T
	​

 must satisfy

Q
T
	​

R
T
	​

=0,rankQ
T
	​

+rankR
T
	​

=dimT.

These equations certify

kerQ
T
	​

=imR
T
	​

.

The same data are required in the quadratic target:

R
2
	​

:U
2
	​

→T
2
	​

,Q
2
	​

R
2
	​

=0,kerQ
2
	​

=imR
2
	​

.
CE/BRST restriction

Let D be the closure matrix and B the boundary/exact matrix. Let Q
C
	​

 quotient any relations in the CE target.

Choose matrices whose columns span

imN
P
	​

=ker(Q
T
	​

A)

and

imK=ker[
Q
C
	​

D
Q
2
	​

J
2
	​

	​

].

Well-definedness requires

Q
2
	​

J
2
	​

B=0,Q
2
	​

J
2
	​

N
P
	​

=0.

Injectivity is certified by explicit matrices X,Y satisfying

K=BX+N
P
	​

Y.
	​


This proves that every CE-closed element with vanishing quadratic jet is either CE-exact or terminally zero.

Equivalently, choose a genuine basis U of

H=
imB+ker(Q
T
	​

A)
ker(Q
C
	​

D)
	​


and form

M
2
	​

=Q
2
	​

J
2
	​

U.

An explicit exact left inverse

LM
2
	​

=1
dimH
	​

	​


is a compact injectivity certificate.

All ranks and nullspaces must be computed in exact arithmetic over the stated coefficient field. Floating-point rank or an identity block on branch-history coordinates is not a certificate.

Without CE/boundary quotients, the certificate reduces to: for a complete basis K of ker(Q
2
	​

J
2
	​

), exhibit X such that

AK=R
T
	​

X.
4. Stronger theorem presently justified?

No stronger anomaly-identification theorem is justified.

Even the displayed implication needs the matching-quadratic-jet premise. The logically complete statement is

ker
ℓ
ˉ
2
4d
	​

=0,
ℓ
ˉ
2
4d
	​

([A
loc
(1)
	​

]−C
2
	​

[O
⋆
	​

])=0

imply

[A
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

Only then does coefficientwise equality follow:

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

].

At present the second premise is not established because the complete quadratic contact contribution and CT
2
	​

 are unresolved.

The rooted functional gives a structural graph-generation statement and, under additional covariance assumptions, background-Ward closure. Those are orthogonal statements, not a stronger uniqueness theorem.

Nothing presently establishes:

full nonlocal 1PI box/pentagon form factors,

or

higher-loop vanishing.
5. Remaining P0/P1 gaps
P0 — theorem-blocking

Definition of the two complexes.
Specify the full-DRED coefficient ring, admissible background/source space, evanescent ideal, physical quotient, filtration, and whether explicit 
δ
/τ spurions are admitted.

Evanescent mixing under renormalization.
Prove that subtraction and physical projection descend consistently. Terms involving an evanescent tensor multiplied by a pole may contribute after tensor reduction or operator mixing.

Cohomological status of E.
Either prove

d
CE
	​

E=0,[E]

=0,

in the actual DRED quotient, or state the precise axiom excluding it.

Physical-4d injectivity certificate.
Missing: true N=1 carrier, parent-incidence matrix, complete terminal relation matrix, quadratic-target relations, CE boundaries, and an exact left-inverse/nullspace witness. The matrix

[1
4866
	​

∣−C
1→2
T
	​

]

does not supply these objects.

Full quadratic post-projector pole.
There are exactly six polarized rows:

2(I
0
	​

H
1
	​

H
1
	​

)+1(I
0
	​

H
2
	​

)+2(I
1
	​

H
1
	​

)+1(I
2
	​

)=6.

The four nontriangle/contact rows must be evaluated after all projectors and D-algebra. No chirality-sector label proves that the I
0
	​

H
2
	​

 row vanishes.

Counterterm contribution.
CT
2
	​

 and CT
n
	​

 must be Taylor coefficients of one source-dependent local counterterm functional, not independently selected terms. Required ingredients include:

composite-operator/source renormalization;

mixing with BRST-exact, EOM, total-derivative, and evanescent operators;

possible finite Slavnov-restoring counterterms;

proof that allowed finite counterterms cannot arbitrarily shift the projected nontrivial class.

Source-BRST/BV formulation.
Missing:

the source coupled to I
AB
;

its BRST transformation and statistics;

the extended Slavnov–Taylor identity;

antifield terms required by nonlinear transformations;

the differentiated source identity producing insertion contact terms;

Wess–Zumino/CE consistency of the renormalized local breaking.

Background covariance is not equivalent to source-BRST closure.

Ward closure of the renormalized sum.
The rooted formula gives

s
B
	​

Γ
I
(1)
	​

=
2
1
	​

STr([Ω,G
B
	​

I
B
	​

])+s
B
	​

CT

only when G
B
	​

 and I
B
	​

 transform homogeneously. Vanishing requires regulated supertrace cyclicity and a covariant counterterm functional. These hypotheses remain to be demonstrated.

Quadratic matching with O
⋆
	​

.
One must prove, in the quadratic target quotient,

[A
loc,2
(1)
	​

]=C
2
	​

[O
⋆,2
	​

]

using the complete six-row result plus CT
2
	​

. The isolated triangle pole does not establish this premise.

Completeness of the local CE carrier.
The basis must include or rigorously exclude all allowed:

covariant-derivative words;

Bianchi-related words;

integration-by-parts classes;

equations-of-motion terms;

Fierz/Schouten and statistics relations;

color/Jacobi relations;

evanescent tensors;

source-dependent contact operators.

UV versus IR separation.
A Taylor expansion at exceptional or zero external momentum can turn an IR pole into an apparent UV-local pole. An independent IR regulator, nonexceptional kinematics, or an R
∗
-type subtraction is required.

Completeness of the rooted supertrace.
Verify that G
B
	​

 and I
B
	​

 include every fluctuating sector affected by the source: gauge fields, matter, FP ghosts, Nielsen–Kallosh ghosts where present, gauge-fixing terms, and any source-dependent measure/Jacobian contribution.

Cubic coefficient, for any explicit n=3 claim.
The polarized count is

6(I
0
	​

H
1
3
	​

)+6(I
0
	​

H
1
	​

H
2
	​

)+6(I
1
	​

H
1
2
	​

)+1(I
0
	​

H
3
	​

)+3(I
1
	​

H
2
	​

)+3(I
2
	​

H
1
	​

)+1(I
3
	​

)=26.

The missing singleton rows are precisely I
0
	​

H
3
	​

 and I
3
	​

; CT
3
	​

 is also unresolved. This blocks any statement that the present diagrammatic calculation determines the cubic coefficient. It is not logically required by the bare injectivity implication once that implication and the full quadratic matching are independently proved.

Vector/chiral cross-frame use.
From

K
C
	​

=J
q
st
	​

K
V
	​

J
q
	​

+E
V,α
	​

C
α
ij
	​

,

determinant or density equivalence does not follow off shell. Any cross-frame transfer requires:

treatment of the EOM Hessian term in the BV/EOM quotient;

the functional Berezinian of the nonlinear change of variables;

matching of gauge fixing and ghost operators;

transformation of the composite source insertion;

regulator compatibility;

matching of counterterms and evanescent operators.

Staying entirely within one frame avoids this P0.

P1 — required for a complete or publication-grade result

Fix all Taylor-coefficient conventions, factorials, polarization multiplicities, graded signs, and supertrace cyclic reorderings.

Supply the full DRED projector algebra and the coefficient ring in ϵ; trace and norm relations for τ alone are insufficient.

Verify the τ-word witness after terminal normal ordering, not only before normal-order relations.

State gauge-group scope. A nonzero SU(2) witness disproves a universal algebraic zero, but it does not classify exceptional groups, Abelian factors, or representation-dependent cancellations.

Check reality/Hermiticity and the parity-conjugate sector of the candidate evanescent word.

Establish gauge-parameter independence, or identify the precise Nielsen-identity class in which the result is invariant.

Control zero modes, boundary conditions, and the domain on which G
B
	​

 and the regulated supertrace are defined.

Make all rank/nullspace computations reproducible in exact arithmetic, including machine-readable parent and relation matrices.

Derive higher-valence H
r
	​

 and I
s
	​

 kernels if direct checks at n≥4 are intended. A local cohomology theorem would not determine the nonlocal momentum dependence of those amplitudes.

Keep the scope statement explicit: the strongest prospective conclusion is equality of one-loop UV-local cohomology classes. It contains no result about finite/nonlocal box or pentagon amplitudes and no result about higher loops.

