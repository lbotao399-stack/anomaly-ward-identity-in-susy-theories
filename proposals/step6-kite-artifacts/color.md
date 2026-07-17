# Color factor of the tip-日 graph (SPEC v1 §4 topology)

Worker: color. Inputs: SPEC §§2,4 (this file cites SPEC line numbers), seed audit
`audits/step5-canonical-superfield-ww-seed.md` §3–4 and §8 (propagator κ^{AB},
vertices c_{CUE}, one-loop 𝒞^{AB}{}_{DE}). Conventions:

  [T_A,T_B] = i c_{AB}{}^C T_C ,  tr_κ(T_A T_B) = κ_{AB} ,
  c_{ABC} := c_{AB}{}^D κ_{DC} totally antisymmetric,  propagator carries κ^{XY}
  (κ^{XY}κ_{YZ} = δ^X{}_Z, κ symmetric).

Topology (SPEC §4): O(insertion, free A on one leg and B on the other),
X₁ (legs L1,L3,L4), X₂ (legs L2,L3,L5), X₃ (legs L4,L5 + external leg, free G).
Internal lines: L1=O–X₁, L2=O–X₂, L3=X₁–X₂, L4=X₁–X₃, L5=X₂–X₃.

## 0. The graph's color word, in general

Each cubic vertex Xᵢ contributes one totally antisymmetric tensor c with its three
(lower) indices attached to the three incident legs, in whatever order the slot
assignment (C,U,E)→legs dictates. Each of the 5 propagators contributes one κ^{··}
joining the two lower indices at its ends. The insertion contributes the fixed upper
labels A (on the leg routed to L1 or L2) and B (the other); the external leg at X₃
leaves one vertex index free, contracted against the output field v^G, so G sits as
a lower index directly on X₃'s c.

Hence, for a given attachment η of the insertion legs (η=+1: A-leg→L1, B-leg→L2;
η=−1: swapped) and slot assignments (σ₁,σ₂,σ₃) ∈ S₃³ at (X₁,X₂,X₃), the color word is

  W = κ^{AA'} κ^{BB'} κ^{MM'} κ^{S₁S₁'} κ^{S₂S₂'}
      c_{σ₁(A',M,S₁)} c_{σ₂(B',M',S₂)} c_{σ₃(G,S₁',S₂')}          (η=+1 shown)

with M,M' on L3, S₁,S₁' on L4, S₂,S₂' on L5, A' on L1's X₁-end, B' on L2's X₂-end,
and σᵢ(·,·,·) denoting the three indices written into the (C,U,E) slots in the
assignment's order.

## 1. Reduction of every slot assignment to one contraction

Because each c is TOTALLY antisymmetric, c_{σ(i,j,k)} = sgn(σ) c_{ijk}. Therefore
every one of the 2·6³ = 432 assignment words equals a signed multiple of the single
base contraction

  C3^{AB}{}_G := κ^{AA'} κ^{BB'} C3_{A'B'G},
  C3_{ABG}   := κ^{MM'} κ^{S₁S₁'} κ^{S₂S₂'} c_{A M S₁} c_{B M' S₂} c_{G S₁' S₂'} ,

(the task's "κ-raised c_{AMS₁} c_{BMS₂} c_{GS₁S₂}"; the outer κ^{AA'}κ^{BB'} are the
L1/L2 propagator factors and are inert for everything below since κ is symmetric):

  W(η; σ₁,σ₂,σ₃) = η · sgn(σ₁) sgn(σ₂) sgn(σ₃) · C3^{AB}{}_G .

Proof of the η factor: the η=−1 word is C3^{BA}{}_G, which equals −C3^{AB}{}_G by §2
below. So the multiple per assignment class is exactly the parity
η·sgn(σ₁)sgn(σ₂)sgn(σ₃) ∈ {+1,−1}: 216 assignments carry +1 and 216 carry −1
(verified numerically for su(2) and su(3), see §5). No second independent contraction
pattern exists: the topology fixes which index sits on which vertex, so slot freedom
is exhausted by the in-vertex permutations already counted.

(Terms 𝔞/𝔟 of SPEC §3 carry the SAME color: both put A on leg 1 and B on leg 2;
they differ only in D-operators. The ± multiplicities above are per (term, chirality)
choice.)

## 2. A↔B parity: C3 is antisymmetric (proved)

In C3_{ABG} swap A↔B, then rename the dummy pairs (M,M')→(M',M) and
(S₁,S₁')↔(S₂,S₂') (allowed, κ symmetric):

  C3_{BAG} = κ^{MM'}κ^{S₁S₁'}κ^{S₂S₂'} c_{B M S₁} c_{A M' S₂} c_{G S₁' S₂'}
           = κ^{MM'}κ^{S₁S₁'}κ^{S₂S₂'} c_{A M S₁} c_{B M' S₂} c_{G S₂' S₁'}
           = − C3_{ABG} ,

using only c_{G S₂' S₁'} = −c_{G S₁' S₂'}. Hence

  **C3^{AB}{}_G = − C3^{BA}{}_G .   (antisymmetric under A↔B — claim (V2) parity holds)**

Combined with a kinematic sum that is A↔B symmetric after the relabeling
(ℓ↔p−ℓ, k↔−k, X₁↔X₂), this forces the tip-日 total to vanish — the color side of
SPEC §9 (V2).

## 3. Reduction to c_{ABG}: Jacobi + adjoint Casimir (derived, not quoted)

Step 1 (Jacobi). The Jacobi identity [T_A,[T_B,T_C]] + cyc = 0 gives, in index form
with the dummy raised by κ,

  c_{ABM} c^{M}{}_{S₁S₂} + c_{BS₁M} c^{M}{}_{AS₂} + c_{S₁AM} c^{M}{}_{BS₂} = 0 ,
  (c^{M}{}_{XY} := κ^{MM'} c_{M'XY}).

Using total antisymmetry to rewrite the last two terms
(c_{BS₁M}c^{M}{}_{AS₂} = +κ^{MM'}c_{AM'S₂}c_{BMS₁},
 c_{S₁AM}c^{M}{}_{BS₂} = −κ^{MM'}c_{AMS₁}c_{BM'S₂}) this is exactly

  κ^{MM'} ( c_{AMS₁} c_{BM'S₂} − c_{AMS₂} c_{BM'S₁} ) = c_{ABM} κ^{MM'} c_{M'S₁S₂} .  (J)

Step 2. In C3_{ABG} the last factor c_{G S₁' S₂'} is antisymmetric in (S₁',S₂'), so
only the (S₁,S₂)-antisymmetric part of κ^{MM'}c_{AMS₁}c_{BM'S₂} survives; by (J)

  C3_{ABG} = ½ c_{ABM} κ^{MM'} · [ κ^{S₁S₁'}κ^{S₂S₂'} c_{M'S₁S₂} c_{G S₁'S₂'} ] .

Step 3 (adjoint Casimir). The bracket is an invariant symmetric bilinear form in
(M',G); for a simple algebra Schur forces it proportional to κ:

  κ^{S S'} κ^{T T'} c_{M S T} c_{G S' T'} =: C₂(adj) · κ_{MG} .

Therefore, for ANY simple gauge algebra in project conventions,

  **C3_{ABG} = ½ C₂(adj) · c_{ABG} ,  i.e.  C3^{AB}{}_G = ½ C₂(adj) · κ^{AA'}κ^{BB'} c_{A'B'G} .**

Step 4 (su(N), project conventions). Take the fundamental T_A with
tr(T_A T_B) = κ_{AB}; in the standard basis (su(2): T=σ/2, su(3): T=λ/2, generalized
Gell-Mann for higher N) κ_{AB} = ½δ_{AB} and c_{AB}{}^C = f_{ABC}, the real structure
constants. Then c_{ABC} = ½ f_{ABC}, κ^{AB} = 2δ^{AB}, and the Casimir contraction is

  C₂(adj) κ_{MG} = 2·2·(½)(½) f_{MST} f_{GST} = f_{MST} f_{GST} .

f f is evaluated from fundamental completeness, (T^S)_{ij}(T^S)_{kl}
= ½(δ_{il}δ_{jk} − N^{-1}δ_{ij}δ_{kl}): with f_{MST} = −2i tr([T_M,T_S]T_T),

  f_{MST} f_{GST} = −4 Σ_{S,T} tr([T_M,T_S]T_T) tr([T_G,T_S]T_T)
                  = −2 Σ_S tr([T_M,T_S][T_G,T_S])            (T-sum by completeness,
                                                              commutators traceless)
                  = −2 tr( T_M Σ_S T_S T_G T_S − T_M T_G Σ_S T_S T_S
                           − T_M Σ_S T_S T_G T_S + T_G T_M Σ_S T_S T_S )   (cyclicity)
                  = −4 tr( T_M [ Σ_S T_S T_G T_S − (Σ_S T_S T_S) T_G ] )
                  = −4 tr( T_M [ −(2N)^{-1} T_G − (N²−1)(2N)^{-1} T_G ] )
                  = (4·N/2) tr(T_M T_G) = N δ_{MG} ,

  using the completeness corollaries Σ_S T_S X T_S = ½(tr X)𝟙 − (2N)^{-1}X (so
  Σ_S T_S T_G T_S = −(2N)^{-1}T_G, T_G traceless) and Σ_S T_S T_S = (N²−1)(2N)^{-1}𝟙,
  and −(2N)^{-1} − (N²−1)(2N)^{-1} = −N/2. Verified numerically to 1e−15.

So f_{MST}f_{GST} = N δ_{MG} = 2N κ_{MG}, i.e. **C₂(adj) = 2N** w.r.t. the
fundamental-trace κ, and

  **C3_{ABG} = N · c_{ABG}     (su(N), κ = fundamental trace form, tr TT = ½δ).**

Equivalently, in pure-δ form this is the requested f f f identity,

  **f_{A M S₁} f_{B M S₂} f_{G S₁ S₂} = (N/2) f_{ABG}**   (all repeated indices δ-summed),

which follows from (J) + f f = Nδ: antisymmetrizing the S₁,S₂ contraction against
f_{GS₁S₂} and applying (J) gives ½ f_{ABM}·(f_{MST}f_{GST}) = ½ f_{ABM}·Nδ_{MG}.
General normalization: if κ_{AB} = x·δ_{AB} in the standard-f basis (x = index of the
trace rep; x = ½ for the fundamental), then C₂(adj) = N/x and C3_{ABG} = (N/2x) c_{ABG}.

## 4. Cross-check against the one-loop settlement color 𝒞^{AB}{}_{DE}

Seed §8 / settlement define F^{AB}{}_{DE} ≡ 𝒞^{AB}{}_{DE} = κ^{AU}κ^{BV}κ^{CC'} c_{UCD} c_{VC'E}.

(a) Symmetry: relabel dummies U↔V, C↔C' and use κ symmetric:
    F^{AB}{}_{DE} = F^{BA}{}_{ED} — symmetric under the simultaneous swap (A,D)↔(B,E),
    exactly the pair-exchange symmetry the one-loop WW seed needs (the two external
    letters W̃^D, X^E swap together with the insertion labels A,B). Note F is NOT
    symmetric or antisymmetric under A↔B alone.

(b) Consistency of conventions: the tip-日 word is the c_G-trace of the one-loop word,

    C3^{AB}{}_G = κ^{DD'} κ^{EE'} F^{AB}{}_{DE} c_{G D'E'} ,

    (identify the settlement's internal C with our L3-index M and (D,E) with the
    L4/L5 indices). Its (D,E)-antisymmetric part, by the same Jacobi step (J),

    F^{AB}{}_{[DE]} = ½ c^{AB}{}_M κ^{MM'} c_{M'DE} ,

    is what survives the trace, reproducing §3. Both relations verified numerically.
    So the tip-日 color factor and the locked one-loop 𝒞^{AB}{}_{DE} come from the
    same convention set with no sign mismatch.

(c) A↔B parity is consistent: under A↔B at fixed (D,E), F splits into a symmetric
    part (the c_{DE}-symmetric "d-like" piece) and the antisymmetric Jacobi piece;
    only the latter has a c_G-trace, which is why the length-2 tip graph is forced
    into the single antisymmetric structure C3, while the one-loop 2-letter output
    keeps the full F.

## 5. Numeric verification (su(2), su(3); code: color_check.py, same directory)

Realization: fundamental generators, κ_{AB} = tr(T_AT_B) = ½δ_{AB} computed
numerically, c_{AB}{}^C from −2i tr([T_A,T_B]T_C)·κ^{-1}, all contractions by einsum.
All checks pass at machine precision (max deviations ≤ 2e−15):

| check | su(2) | su(3) |
|---|---|---|
| c_{ABC} totally antisymmetric | OK | OK |
| (1) all 432 = 2·6³ slot words = ±C3, sign = η·∏sgn(σᵢ); 216 each sign | OK | OK |
| (2) C3_{ABG} + C3_{BAG} = 0 | 0.0 | 0.0 |
| (J) Jacobi rearrangement | 0.0 | 6e−17 |
| (3a) c_{AMN}c_B{}^{MN} = C₂κ_{AB}, C₂ = 2N | 4.000000 | 6.000000 |
| (3b) C3_{ABG} = (C₂/2)c_{ABG} = N c_{ABG} | ratio 2.0000 | ratio 3.0000 |
| (3c) f f f = (N/2) f | 0.0 | 4e−16 |
| (4a) F^{AB}{}_{DE} = F^{BA}{}_{ED} | 0.0 | 0.0 |
| (4b) C3^{AB}{}_G = κκ F^{AB}{}_{DE} c_{GD'E'} | 0.0 | 2e−15 |
| (4c) F^{AB}{}_{[DE]} = ½c^{AB}{}_M κ^{MM'}c_{M'DE} | 0.0 | 1e−16 |

## 6. Summary for the engine / verifiers

- Every tip-日 row's color factor is η·sgn(σ₁)sgn(σ₂)sgn(σ₃) · C3^{AB}{}_G; there is
  exactly ONE independent color structure for this graph.
- C3^{AB}{}_G = −C3^{BA}{}_G (exact, any algebra). ⇒ SPEC §9 (V2) parity claim HOLDS.
  If the engine's kinematic sum is A↔B symmetric under (ℓ↔p−ℓ, k↔−k, X₁↔X₂), the
  total vanishes by color alone.
- C3_{ABG} = ½C₂(adj) c_{ABG}; su(N) with fundamental-trace κ (project tr_κ):
  C3_{ABG} = N c_{ABG}, equivalent to δ-form f f f = (N/2) f. (If a different trace
  rep normalizes κ, scale by ½/x: C3 = (N/2x) c.)
- Conventions cross-checked against the settlement's 𝒞^{AB}{}_{DE}
  ((A,D)↔(B,E)-symmetric; its Jacobi/antisymmetric part is what feeds C3).
