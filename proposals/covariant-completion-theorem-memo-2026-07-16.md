# The covariant completion theorem: boxes and pentagons as dressings of the triangle bracket

Status: `NON_AUTHORITY_PROPOSAL` — derivation memo (Step-6 seed), owner-commissioned
2026-07-16. Numbered equations (T.$n$). Marking convention, per the owner's instruction
("先推导四边形试水,没彻底核查的暂时标注"):

- **[PROVED-HERE]** — derived in this memo, self-contained;
- **[REPO-LOCKED]** — already an accepted repository result, cited by tag;
- **[MACHINE-CHECK-$k$]** — a finite, precisely stated computation left for exact machine
  verification (consolidated list in §9);
- **[OPEN]** — genuinely open, with the intended proof route stated.

---

## 1. Statement

**Covariant Completion Theorem (CCT).** In the fixed Fermi–Feynman DRED slice, let
$\mathcal A_{ij}[V_{\rm B}]$ denote the complete one-loop anomaly of
$\boldsymbol\nabla_-(L_iL_j)$ as a functional of the background prepotential — i.e. the sum
of *all* one-loop supergraphs with the pair insertion, two uncontracted output letters, and
any number of additional external background legs (triangles, boxes, pentagons, …). Then

$$
\mathcal A_{ij}[V_{\rm B}]
=\lambda_1\,\mathbb F^{AB}{}_{DE}\;
\Delta(L_i,L_j)^{DE}\Big|_{\partial_{\dot a}\to\boldsymbol\nabla_{\dot a},\;
L\to L[V_{\rm B}]},
\tag{T.1}
$$

i.e. the $n$-gon graphs ($n\ge4$) contribute **exactly** the terms that covariantize the
output derivatives and dress the output letters of the flat-background triangle bracket — no
new independent multilinear structure. Consequence: census completeness at every valence
$\ge4$ follows from gauge covariance plus the flat-background result, replacing per-graph
enumeration by a symmetry argument. The remaining enumeration burden is confined to the
flat-background valence (the settled triangle+contact family) and the finite cohomology
check of §6.

## 2. The analytic heart: a universal threshold master integral [PROVED-HERE]

All quantum content sits in $\mu_\ell^2$ insertions. Define, for the $n$-gon,

$$
M_n^{(a)}
:=\mu^{2\epsilon}\!\int\!\frac{d^d\ell}{(2\pi)^d}
\frac{\mu_\ell^2\,(\ell^2)^a}{(\ell^2+\Delta)^n}
=\frac{2\epsilon}{d}\,
\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(a+1+\tfrac d2)}{\Gamma(\tfrac d2)}
\frac{\Gamma(n-a-1-\tfrac d2)}{\Gamma(n)}
\,\Delta^{a+1+\frac d2-n},
\tag{T.2}
$$

using $\int\mu_\ell^2 f(\ell^2)=\frac{4-d}{d}\int\ell^2f(\ell^2)$.

**Lemma 1 (threshold).** $M_n^{(a)}\to0$ as $\epsilon\to0$ unless $a\ge n-3$
(the explicit $\epsilon$ must be met by a pole of $\Gamma(n-a-1-\tfrac d2)$).
So an $n$-gon contributes an anomaly remainder only from numerator sectors of loop-momentum
degree $\ge2(n-3)$: the box needs $\ell\ell$, the pentagon needs $\ell^4$, and every
sub-threshold sector dies. Contact bubbles ($n=2$) sit above threshold trivially but produce
only $\Delta$-polynomial (dimension-shifted) locals — see Lemma 3.

**Lemma 2 (universality).** At threshold $a=n-3$, using
$\Gamma(n-2+\tfrac d2)/\Gamma(\tfrac d2)\big|_{d=4}=\Gamma(n)$ and
$\epsilon\Gamma(\epsilon)\to1$:

$$
\boxed{\;
M_n^{(n-3)}\;\xrightarrow{\epsilon\to0}\;
\frac{2}{d}\cdot\frac{\Gamma(n-2+\tfrac d2)}{\Gamma(\tfrac d2)\,\Gamma(n)}
\cdot\frac{1}{(4\pi)^{2}}\bigg|_{d=4}
=\frac{1}{32\pi^2}
\qquad\text{for every }n\ge3 .}
\tag{T.3}
$$

Moreover the full graph normalization is also universal: the parametrization factor
$\Gamma(n)$ times the simplex volume $\operatorname{Vol}(\Delta_{n-1})=\tfrac1{(n-1)!}$
equals $1$ for every $n$, and since the threshold value (T.3) is $\Delta$-independent the
parametric integral is trivial — every $n$-gon's threshold remainder carries the **same**
$\tfrac1{32\pi^2}$ as the triangle master. This is the analytic reason a uniform
covariantization with the triangle's normalization $\lambda_1$ is possible at all: had the
threshold master depended on $n$, (T.1) could not hold with one coefficient.

**Lemma 3 (dimension selection).** Above threshold ($a=n-2$),
$\epsilon\,\Gamma(-1+\epsilon)\to-1$ gives $M_n^{(n-2)}\to-\tfrac{n\,\Delta}{32\pi^2}$:
local but $\Delta$-linear, i.e. carrying two extra units of dimension. For the anomaly
output of fixed dimension (the $O(\Gamma)$ covariantization term
$-i[\Gamma_{\dot a},\cdot]$ has the *same* dimension as $\partial_{\dot a}$), only the
threshold sector can appear; super-threshold sectors belong to higher-dimension
EOM/total-derivative classes. **[MACHINE-CHECK-1]**: exhibit the explicit cancellation or
EOM-classification of the box's $a=2$ sector in the AA+soft-leg channel.

## 3. Proof architecture

The theorem follows from three statements:

**(S1) Localization.** The anomaly remainder of any one-loop graph is a sum of
$\mu^2$-insertions on marked lines (the repo-locked cut identity, settlement §2)
**[REPO-LOCKED]**, and by Lemmas 1–3 only the *leading-UV (threshold) numerator sector* of
each $n$-gon survives at fixed output dimension **[PROVED-HERE]**.

**(S2) Covariance of the generating trace.** The one-loop functional with the pair insertion
is a supertrace over the quadratic fluctuation operator in the background,
$\Gamma^{(1)}[V_{\rm B}]=\tfrac12\operatorname{STr}\!\big[\mathcal I\,G_0\,(1+H[V_{\rm
B}]G_0)^{-1}\big]$, whose expansion in $H$ generates precisely the triangle ($k=2$), box
($k=3$), pentagon ($k=4$), … as members of one trace; background-gauge covariance acts by
conjugation $H\to RHR^{-1}$, $\mathcal I\to R\mathcal IR^{-1}$ and the supertrace is
invariant. Hence the *full* functional is background-covariant, order by order in the legs.
The threshold (leading-UV) part of a covariant functional is the covariant heat-kernel
coefficient of the appropriate dimension (Seeley–DeWitt $a_2$-type), which is a **covariant
local operator**. The rooted-trace form of this statement was derived on the closed PR #46
branch and the bounded heat-kernel lemma admitted in the #71 audit; the trace covariance
itself must be re-hosted as an accepted contract statement. **[OPEN — re-host; proof is the
two-line conjugation-invariance of STr]**.

**(S3) Uniqueness of the completion.** A covariant local operator is determined by its
flat-background value **iff** no independent covariant operator with the same quantum
numbers vanishes at $V_{\rm B}=0$. Candidates for such "invisible primitives" are operators
with explicit field-strength insertions, schematically
$\mathbb F'\,(\text{letter})\,\mathcal W_+(\text{letter})$-type. This is a finite
classification at fixed dimension $\tfrac92+1$, ghost number, $SU(3)$ weight, and Grassmann
parity — the same conserved-quantity analysis that produced the 29/52 census, run one
dimension higher. §6 sets it up; the finite list is **[MACHINE-CHECK-2]**.

Given (S1)+(S2)+(S3): the surviving remainder is the threshold sector of a covariant
functional (S1,S2), hence a covariant local operator; its flat value is the settled triangle
bracket; (S3) says covariance then fixes everything — which is (T.1). $\square$-modulo the
marked items.

## 4. The box test, part I: kinematics and what must come out [PROVED-HERE at skeleton level]

Work in the AA channel. Triangle data (settlement §4): loop momenta $r_0=\ell$,
$r_1=\ell+p$, $r_2=\ell+p+q$; numerator $\propto T_{m\rho n}L_1^mp^\rho L_2^n$ with
$L_1,L_2=2\ell+\dots$; threshold sector $= \ell\ell$; master $\tfrac1{32\pi^2}$; output
$\lambda_1\mathbb F^{AB}{}_{DE}\,\partial_{\dot a}X^D\partial^{\dot a}Y^E$-structure.

Add **one** external background leg of momentum $k$, color index $F$, in the connection
component that enters $\boldsymbol\nabla_{+\dot a}=D_{+\dot a}-i\Gamma_{+\dot a}$. The box
prediction from (T.1), expanding
$\boldsymbol\nabla_{\dot a}X\,\boldsymbol\nabla^{\dot a}Y$ to $O(\Gamma)$:

$$
\mathcal A^{(\Gamma)}
=-i\lambda_1\,\mathbb F^{AB}{}_{DE}\Big(
c_{FD'}{}^{D}\,\Gamma_{\dot a}^F X^{D'}\,\partial^{\dot a}Y^E
+c_{FE'}{}^{E}\,\partial_{\dot a}X^D\,\Gamma^{F\dot a}Y^{E'}
\Big)
+\big(\text{letter-dressing terms }L\to L^{(1)}[V_{\rm B}]\big).
\tag{T.4}
$$

The box graphs at order $g^3$ that can produce this: the soft leg attaches to (i) one of the
three internal lines (three box topologies), (ii) an internal vertex (vertex-correction
topologies), (iii) the insertion word itself (letter-dressing topologies, these produce the
second bracket of (T.4) by construction of the dressed letters). Class (iii) is the
insertion's own expansion **[REPO-LOCKED as 5A.49–5A.52 words]**; the nontrivial content is
that classes (i)+(ii) produce exactly the first bracket of (T.4).

**Threshold filtering [PROVED-HERE].** At the new vertex the SYM cubic word contributes, after
D-algebra, a leading *eikonal* part (pure momentum flow, numerator degree $+1$) and
sub-eikonal parts in which derivatives land on external legs (numerator degree $+0$). By
Lemma 1 the box keeps only total degree $\ge2$: since the triangle chain already supplies
degree $2$ via $L_1^mL_2^n\to4\ell^m\ell^n$, the *eikonal part of the new vertex must spend
its momentum on the external factor*, or the $\ell$-degree stays at $2$ with the eikonal
denominator — both bookings survive; every sub-eikonal + sub-leading-chain combination falls
below threshold and dies. This is the diagrammatic mechanism by which "boxes are dressings":
the regulator only sees their eikonal skeleton. **[MACHINE-CHECK-3]**: the D-algebra
statement that sub-eikonal vertex parts lower the surviving $\ell$-degree (vertex word
5A.52 → edge-tagged transfer table).

## 5. The box test, part II: the longitudinal (Ward) half [PROVED-HERE]

Set the soft-leg polarization longitudinal, $\Gamma_{\dot a}\to$ gauge direction, momentum
$k$. The eikonal insertion on line $i$ replaces
$\frac1{D_i}\to\frac{2r_i\cdot k+k^2}{D_i\,D_i^{(k)}}$ with $D_i^{(k)}=(r_i+k)^2$. Using

$$
2r_i\cdot k+k^2=D_i^{(k)}-D_i
\;\;\Longrightarrow\;\;
\frac{2r_i\cdot k+k^2}{D_iD_i^{(k)}}
=\frac1{D_i}-\frac1{D_i^{(k)}},
\tag{T.5}
$$

the sum over the three insertion points **telescopes**: interior differences cancel
pairwise, leaving only the two boundary terms in which the momentum shift $k$ has been pushed
onto the two *output slots*, plus the marked-line term where the shift crosses the
$\mu^2$-cut. The boundary terms are, by inspection, the gauge variation of the triangle
result's external structure — i.e. exactly the longitudinal part of (T.4), since under a
gauge transformation $\delta\Gamma_{\dot a}=\partial_{\dot a}\omega+\dots$ the covariantized
output transforms homogeneously while the flat $\partial X\partial Y$ does not, the
difference being the telescoped boundary. Color routing: each insertion on line $i$
multiplies the triangle's color word by $c_{F\,\cdot}{}^{\cdot}$ at position $i$; the
telescoped boundary lands the structure constant on the output-slot color indices —
precisely the adjoint action in (T.4). **Conclusion: the longitudinal box sum equals the
longitudinal part of the covariantization, exactly, with no leftover.** (This is the
supergraph avatar of the textbook soft–gauge Ward identity; the only novelty is checking it
survives inside the $\mu^2$-remainder, which it does because (T.5) is an algebraic identity
of the denominators and the cut identity is linear in them.)

What this proves: the box family is *consistent* with (T.1) and any box-level violation of
CCT must be purely transverse.

## 6. The box test, part III: the transverse half and the invisible-primitive check

The transverse part of the soft box is fixed by (i) the threshold sector's tensor average
$\ell^m\ell^n\to\tfrac{\widehat\delta^{mn}}{d}\ell^2$, (ii) the universal master (T.3) with
one doubled denominator (the eikonal line), and (iii) the $\sigma$-chain contraction with
the extra polarization slot. Assembling (i)–(iii) for the three insertion points gives a
finite vector of coefficients multiplying the two independent transverse structures

$$
t_1=\Gamma_{\dot a}^F\,\text{(slot-1 commutator)},\qquad
t_2=\Gamma_{\dot a}^F\,\text{(slot-2 commutator)} .
\tag{T.6}
$$

**Prediction from (T.1):** $(t_1,t_2)$ coefficients $=(-i\lambda_1,-i\lambda_1)$ times the
adjoint color routing, and **zero** coefficient for any third structure — in particular for
the field-strength primitive

$$
t_W=\mathbb F'\,(\text{letter})\,\mathcal W_+(\text{letter})\text{-type},
\tag{T.7}
$$

which is the unique dimension-allowed "invisible primitive" candidate at this order (it
vanishes at $V_{\rm B}=0$, so the flat triangle cannot see it; the box is the first place it
could appear). Charge screening: $t_W$ must be an $SU(3)$ singlet, Grassmann-odd output of
dimension $\tfrac{11}2$… the systematic finite list at this level is
**[MACHINE-CHECK-2]**; the explicit transverse box evaluation deciding
$(t_1,t_2,t_W)=(-i\lambda_1,-i\lambda_1,0)$ is **[MACHINE-CHECK-4]** — this is the single
most valuable machine computation, the box analogue of the settled AA seed: three insertion
points × threshold tensor average × doubled-denominator masters, all ingredients already
derived here.

Doubled-denominator masters needed for [MACHINE-CHECK-4], derived from (T.2) by
$\partial/\partial\Delta$ **[PROVED-HERE]**:

$$
M_{3+1_i}^{(1)}:
\int\!\frac{\mu_\ell^2\,\ell^m\ell^n}{D_0D_1D_2D_i}
=\frac{\Gamma(4)}{\Gamma(2)}\!\int_{\Delta_2}\!x_i\;
\Big[\mu^2\text{-integral at power }4\Big]
\;\xrightarrow{\epsilon\to0}\;
\frac{\widehat\delta^{mn}}{4}\cdot\frac{1}{32\pi^2},
\tag{T.8}
$$

because the doubled line $D_i^2$ parametrizes over the *two*-simplex with weight $x_i$
($1/(A^2BC)=\tfrac{\Gamma(4)}{\Gamma(2)}\int_{\Delta_2}x\,[xA+yB+zC]^{-4}$), the threshold
value is $\Delta$-independent, and
$\Gamma(4)\int_{\Delta_2}x=6\cdot\operatorname{Vol}(\Delta_2)\langle x\rangle
=6\cdot\tfrac12\cdot\tfrac13=1$ **[PROVED-HERE]**. So the doubled-denominator threshold
master is *also* $\tfrac{\widehat\delta^{mn}}{4}\cdot\tfrac1{32\pi^2}$ — the universality of
(T.3) extends to the eikonal boxes.

## 6b. Transverse sector decomposition of the box [PROVED-HERE at sector level]

Write the eikonal insertion on line $i$ as $2r_i\cdot\varepsilon=2\ell\cdot\varepsilon
+2Q_i\cdot\varepsilon$ ($r_i=\ell+Q_i$, $Q_i\in\{0,p,p+q\}$) against the triangle chain
$L_1^mp^\rho L_2^n\,T_{m\rho n}$ with $L_{1,2}=2\ell+(\text{ext})$. Loop-momentum parity at
threshold splits the surviving numerator into exactly two sectors:

- **Slot-insertion sector** (chain-$\ell$ × eikonal-$\ell$): the $\widehat\delta$-average
  pairs the eikonal momentum with one chain slot,
  $\ell^m\ell^\alpha\to\tfrac{\widehat\delta^{m\alpha}}4$, so the polarization
  $\varepsilon_\alpha$ **enters the $\sigma$-chain exactly where an output derivative
  sat** — mechanically producing the $-i[\Gamma_{\dot a},\cdot]$ insertion on output slot 1
  or 2, normalized by the doubled-line master (T.8),
  $\tfrac{\widehat\delta}{4}\cdot\tfrac1{32\pi^2}$, per insertion point.
- **Weighted sector** (chain-$\ell\ell$ × $2Q_i\cdot\varepsilon$, and chain-external ×
  eikonal-$\ell$): external-momentum-weighted terms; these carry precisely the $p,q$
  weights that the momentum-space form of the covariantized output
  ($\partial^{\dot a}Y\to$ momentum factor) and the letter-dressing words demand.

So the covariantization structure is not imposed — it *emerges from the tensor average*.
What remains open is pure bookkeeping: summing the slot-insertion sector over the three
insertion points with per-line color routing and checking the total coefficient
$(t_1,t_2,t_W)=(-i\lambda_1,-i\lambda_1,0)$ — [MACHINE-CHECK-4] — and matching the weighted
sector against the dressing words — part of the same check.

## 6c. The Wess–Zumino consistency condition and the ABJ precedent

**Consistency condition [strengthens S3].** The $L_\infty$/Maurer–Cartan relation of the
loop-corrected supercharge gives, at one loop,

$$
\{Q_0,\,Q_1\}=0
\qquad\Longlongleftrightarrow\qquad
Q_0\,\mathcal A_{ij}
=\;\mathcal A\big(Q_0\text{-descendants of }L_iL_j\big)_{\rm Koszul},
\tag{T.9}
$$

i.e. the anomaly must be a **cocycle of the classical letter differential** — the exact
analogue of the Wess–Zumino consistency condition for the ABJ/Bardeen anomaly. Two
consequences: (a) the correct arena for the uniqueness step S3 is the $Q_0$-cohomology
$H(Q_0)$ on covariant local bilinears (cocycles that are coboundaries are removable by
finite normal-product redefinitions — the scheme freedom already used in the AB/BA
settlement); (b) any invisible primitive $t_W$ must be an independent $Q_0$-cocycle at its
quantum numbers, a far stronger constraint than charge counting. Crucially, **(T.9) is
verifiable letter-algebraically, with no loop integrals**, on all 81 settled rows —
[MACHINE-CHECK-7].

**ABJ precedent (historical guidance, not imported input).** The theorem being proved here
is the superspace/DRED avatar of a classical result chain:

1. *Adler (Phys. Rev. 177, 1969); Bell–Jackiw (1969)*: the divergent AVV triangle carries
   the anomaly $\partial A\partial A$.
2. *Bardeen (Phys. Rev. 184, 1969)*: the non-abelian anomaly computed **including the AVVV
   box and AVVVV pentagon**; the boxes/pentagons contribute exactly the $A^2\partial A$ and
   $A^4$ terms that complete $\partial A\partial A$ into the gauge-covariant
   $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ — the original covariant
   completion computation, done by honest diagram evaluation.
3. *Adler–Bardeen (1969)*: the completed coefficient receives no higher-order corrections.
4. *Wess–Zumino (1971); Bardeen–Zumino (1984)*: the consistency conditions and the
   consistent/covariant dictionary that fix the completion's form cohomologically.

The mechanism-level correspondence: in the ABJ analysis, box contributions to the *new*
tensor structures are superficially convergent, hence shift-unambiguous and anomaly-free;
only the sectors tied to the divergent triangle by the vector Ward identities survive — and
those are fixed to be the covariantization. Lemma 1 is the DRED version: the
$\mu^2$-remainder is supported exactly on the UV-marginal (threshold) sectors, which the
Ward telescoping (§5) ties to the triangle. If Bardeen's box/pentagon evaluation is wanted
as a working reference, it must enter through a `REFERENCE_IMPORT` with claims classified
`EXTERNAL_METHOD_PRECEDENT` — method admitted, coefficients never.

## 7. Pentagon and beyond [sketch]

At $O(\Gamma^2)$ (pentagons / two soft legs): threshold $a\ge2$, universality (T.3) again
gives $\tfrac1{32\pi^2}$; the longitudinal double-telescoping reproduces the
$O(\Gamma^2)$ gauge completion ($\Gamma\Gamma$ terms of
$\boldsymbol\nabla\boldsymbol\nabla$), and the new invisible-primitive slots are
$\mathcal W$-squared and $\boldsymbol\nabla\mathcal W$ insertions — again a finite charge
classification. Induction on the number of legs with (S2) covariance closes all valences
once the box case is settled: covariance relates the $n$-leg transverse coefficient to the
$(n-1)$-leg one, so [MACHINE-CHECK-4] at the box level is the only *independent* transverse
check. **[OPEN]**: write the induction as a contract-grade statement (the $R$-conjugation
Ward identity of the rooted trace, re-hosted from the closed PR #46 material).

## 8. What this buys the census

With CCT proved: every graph at valence $\ge4$ is accounted for by symmetry; the
flat-background enumeration (triangle + contact family, settled) plus the finite
[MACHINE-CHECK-2] cohomology list *is* the complete census. The remaining typed-absence rows
(ghost sector) are the separate two-line argument already recorded: ghost-vertex spectator
legs are never letters, and closing a ghost loop at $g^2$ consumes all insertion ports,
leaving no letter-bilinear output; ghost self-energy dressings are $g^4$. **[MACHINE-CHECK-6]**:
transcribe that argument as a target-blind typed row from the FP words 5A.58–5A.60.

## 9. Consolidated machine-check list (for Codex)

1. Box $a=2$ super-threshold sector in AA+soft: cancels or classifies as EOM/TD
   (dimension bookkeeping of Lemma 3).
2. Finite cohomology list of covariant completions vanishing at $V_{\rm B}=0$ at output
   dimension $\tfrac92+1$ (and $+2$ for pentagons): quantum-number classification, then
   emptiness/basis.
3. Sub-eikonal vertex parts fall below threshold: edge-tagged D-algebra degree count for the
   5A.52 cubic word.
4. **The transverse box coefficient**: three insertion points, threshold tensor average,
   masters (T.3)/(T.8) ⇒ $(t_1,t_2,t_W)=(-i\lambda_1,-i\lambda_1,0)$.
5. Doubled-line parametric weight in (T.8) equals $1$.
6. Ghost typed-absence row from 5A.58–5A.60 (two-line argument, transcribe target-blind).

7. Consistency condition (T.9) on all 81 settled rows: verify
   $Q_0\Delta(L_i,L_j) = \Delta(Q_0\text{-descendants})_{\rm Koszul}$ letter-algebraically —
   loop-integral-free, and independently valuable as a global cross-check of the ledger.

Item 4 is the decisive one; 1 and 3 are its supporting arithmetic (5 is now proved in T.8);
2 closes uniqueness and is now sharpened to an $H(Q_0)$ classification by (T.9); 6 is
independent of CCT; 7 is free of loop integrals and should run first.

## 10. Honest summary

Proved here: the threshold/universality/dimension lemmas (T.2)–(T.3) — the analytic reason
CCT can hold — and the longitudinal half of the box test, exactly. Set up with proof route:
trace covariance (S2, two-line re-host) and completion uniqueness (S3, finite
classification). Deferred to machine verification: the transverse box coefficient and five
supporting checks, each finite and precisely specified. Nothing here modifies the accepted
Step-5 coefficient ledger; CCT is the instrument that will convert its census status from
"enumerated + externally corroborated" to "protected by gauge covariance".
