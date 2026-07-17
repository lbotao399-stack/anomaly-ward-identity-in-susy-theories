# SPEC — Two-loop 日 (kite / K4−e) supergraph for ∇₋(∇₊W₊^A ∇₊W₊^B): anomaly sector

Status: exploratory computation on branch `claude/2-loop-superspace-anomaly-3havuv`.
This SPEC is the single shared input for all workers. Everything here is either
(a) quoted from locked project contracts (cited by path), or (b) a declared scheme
choice labeled `[D-choice]`. Workers must not silently change either kind; if you
believe an item is wrong, SAY SO explicitly in your report with the corrected
version and evidence, and continue with both variants if cheap.

Repo root: /home/user/anomaly-ward-identity-in-susy-theories

## 0. Authoritative source files (read these, cite by line)

- `audits/step5-canonical-superfield-ww-seed.md` — THE one-loop calibration document.
  Contains: canonical conventions (§1), canonical dictionary V_P=2gv, W_P=gW_can (§2),
  FF propagator ⟨v^A v^B⟩ = ħ κ^{AB}/p² δ⁴(θ₁₂) (§3), cubic vertices (§4),
  insertion word (§5), the 8-row D-word table (§6), D-algebra weight (§7),
  fixed-orientation preintegral Γ_{T,A} (§8), UV pole (§9).
- `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` — settlement:
  §1 regulator ledger (DRED, hatted/breve vs bar/tilde, μ_ℓ² := ℓ̄²−ℓ_d²),
  §4–5 seed + contact rows + cutting identity, §3 tree descendants (∇₋ on letters).
- `proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md` — F.1 projectors,
  F.4/F.5 propagators, F.6 loop saturation δ⁴(θ₁₂)D²D̄²δ⁴(θ₁₂)=16δ⁴(θ₁₂).
- `contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md`
  — (5A.49)–(5A.63): exponential derivatives, gauge word S^g (5A.52), Koszul/ordered
  functional differentiation (5A.61)–(5A.62), graph weight (5A.63) with τ_E = −1/ħ.
- `contracts/foundations/step-01-supersymmetry-commutator.md` (1.51)–(1.54):
  σ_E^m = (−iσ¹,−iσ²,−iσ³,𝟙)_{aȧ}, σ̄_E^m = (+iσ¹,+iσ²,+iσ³,𝟙)^{ȧa} = εε σ_E,
  σ_E^m σ̄_E^n + σ_E^n σ̄_E^m = 2δ^{mn}𝟙.
- `contracts/foundations/step-02a-flat-superspace.md` — flat D-algebra (2A.41)–(2A.43),
  left Grassmann calculus (2A.4)–(2A.8).

## 1. Locked conventions (operative frame = seed audit §1)

- Undotted spinor indices a ∈ {+,−}; dotted ȧ ∈ {˙1,˙2} (equivalently ˙+,˙−).
- ε^{+−}=1, ε_{+−}=−1; D^+ = D₋, D^− = −D₊ (same raising rule for θ's; mirror for dotted).
- D² := 2D₋D₊;  D̄² is the dotted mirror, normalized so that (D̄²θ̄²)| = −4.
- Momentum space: fields carry e^{ip·x}, ∂_m ↦ ip_m, all vertex momenta incoming.
  𝗉_{aȧ}(q) := −i(σ_E^m)_{aȧ} q_m.  Locked anticommutator: {D_a, D̄_ȧ} = 2𝗉_{aȧ}.
- Anchors that any concrete realization MUST satisfy (calibration level 0):
  (D²θ²)| = −4, (D̄²θ̄²)| = −4, [D²D̄²δ⁴(θ)]| = 16 with δ⁴(θ)=θ²θ̄²,
  δ⁴(θ₁₂) D²D̄² δ⁴(θ₁₂) = 16 δ⁴(θ₁₂)   (F.6),
  δ⁴(θ₁₂) [any word with <2 D's and <2 D̄'s] δ⁴(θ₁₂) = 0.
- Suggested explicit realization (verify anchors; adjust only if an anchor fails):
  at superspace point i, acting on a line function carrying momentum q INTO point i:
  D_a = ∂/∂θ_i^a + 𝗉_{aḃ}(q) θ̄_i^ḃ,  D̄_ḃ = ∂/∂θ̄_i^ḃ + θ_i^c 𝗉_{cḃ}(q),
  which gives {D_a, D̄_ḃ} = 2𝗉_{aḃ}(q). Direction convention for q must be fixed
  globally and validated by calibration level 1 below.
- Berezin: ∫d⁴θ_i normalized so ∫d⁴θ δ⁴(θ) = 1.
- Euclidean canonical propagator (seed §3): ⟨v^A(p,θ₁)v^B(−p,θ₂)⟩ = ħ κ^{AB}/p² · δ⁴(θ₁−θ₂).
- Canonical linearized field strengths:
  W_(1)a = −¼ D̄² D_a v   (seed §2),
  W̃_(1)ȧ = −¼ D² D̄_ȧ v   (from 5A.33 with 𝒱_P = 2gv; verify this sign yourself).

## 2. Canonical interaction vertices (from seed §4; re-derive, do not just quote)

S_(3),+ = −(g/2) ∫ d^dx d⁴θ tr_κ( W_(1)^a ⟦D_a v, v⟧ ),  ⟦X,Y⟧ := XY − YX,
        = −(ig/2) c_{CUE} ∫ d^dx d⁴θ (−¼ D̄²D^a v^E)(D_a v^C) v^U ,
S_(3),− = +(g/2) ∫ d^dx d⁴θ tr_κ( W̃_(1)ȧ ⟦D̄^ȧ v, v⟧ )
        = +(ig/2) c_{CUE} ∫ d^dx d⁴θ (−¼ D²D̄_ȧ v^E)(D̄^ȧ v^C) v^U .
Color: [T_A,T_B] = i c_{AB}{}^C T_C, tr_κ(T_A T_B) = κ_{AB}, c_{ABC} totally antisym.
Vertex insertion factor in the expansion: each vertex enters as (−1/ħ)·S_(3),χ
(Euclidean τ_E = −1/ħ, 5A.63). The seed's boxed 𝒱_W = −(ig/2)c_{UCE}W^{Eγ}(D_{Cγ}−D_{Uγ})
and 𝒱_W̃ = +(ig/2)c_{UCD}W̃^D_γ̇(D̄_C^γ̇−D̄_U^γ̇) already include that minus sign
(seed §4: "再乘 e^{−S_int/ħ} 的 minus sign"). Wick weight for vertex-label assignments
is 1 (seed §5 mechanism: 1/n! cancels against n! assignments of S-factors to vertices).

## 3. Insertion (the word)

Canonical insertion at point O (θ₀ NOT integrated), total incoming momentum q_ins = −p
(so that the single output leg carries outgoing momentum p):

  ℐ₂^{AB} = D₋[ (K₊ v^A)(K₊ v^B) ],  K₊ := −¼ D₊D̄²D₊,
  D₋K₊ = −⅛ D²D̄²D₊  (verify).

Two terms (Leibniz, K₊v bosonic):
  term 𝔞: leg-1 operator = −⅛ D²D̄²D₊ (color A), leg-2 operator = −¼ D₊D̄²D₊ (color B);
  term 𝔟: leg-1 operator = −¼ D₊D̄²D₊ (A),   leg-2 operator = −⅛ D²D̄²D₊ (B).
Project letters: A_P = ∇₊𝒲₊ = g·(D₊W_can,₊) + O(g²) so ∇₋(A^A A^B)_P = g²·ℐ₂^{AB} + O(g³);
final conversion to project normalization multiplies the canonical result by g² on the
LHS-word side and one factor g per canonical output letter on the RHS.

## 4. The two-loop graph (fixed labeled topology = 日 / kite / K4 minus edge O–X₃)

Vertices: O(θ₀) [insertion], X₁(θ₁), X₂(θ₂), X₃(θ₃) [cubic gauge vertices, each
independently of chirality type χ_i ∈ {+,−}].
Internal lines (all vector v-propagators), with directed momenta:
  L1: O→X₁ momentum ℓ,      denominator D₁ = ℓ²
  L2: O→X₂ momentum p−ℓ,    D₂ = (p−ℓ)²
  L3: X₁→X₂ momentum k,     D₃ = k²
  L4: X₁→X₃ momentum ℓ−k,   D₄ = (ℓ−k)²
  L5: X₂→X₃ momentum p−ℓ+k, D₅ = (p−ℓ+k)²
External: ONE uncontracted v-leg at X₃ with outgoing momentum p (all momentum
conservation checks pass at each vertex).
Loop integrals (NOT to be performed by the engine): μ^{4ε}∫ d^dℓ d^dk/(2π)^{2d}.

Contractions to sum: for each (term 𝔞/𝔟) × (χ₁,χ₂,χ₃) ∈ {±}³ × all assignments of each
vertex's three field slots (E/W-slot, C-slot, U-slot) to its three incident legs
(for X₁, X₂: legs = 3 internal lines; for X₃: legs = 2 internal lines + 1 external leg).
No self-contractions at a vertex (topology is fixed). Fermion/Koszul signs per
(5A.61)–(5A.62); all v's and K₊v's are bosonic, D-operator words may be odd — track
signs of moving odd operators past each other exactly.

Prefactor bookkeeping (report it factored, don't lump):
  ħ⁵ (5 propagators) × (−1/ħ)³·(vertex S-coefficients) × insertion-leg coefficients.
Expected overall order: ħ² g³ (canonical) = ħ² g⁴ in project letters after conversion.

## 5. What the engine must output

After all Berezin integrations ∫d⁴θ₁ d⁴θ₂ d⁴θ₃ (θ₀ kept), the amplitude reduces to

  Γ^{AB;G}_日(p) = Σ_rows  𝒩_row · [color word]_row · [𝗉-polynomial]_row
                   × [output jet]_row (θ₀, θ̄₀-dependence explicit)
                   / (D₁D₂D₃D₄D₅)   (under the loop integrals)

Output as BOTH:
 (a) machine-readable JSON at scratchpad/kite/engine_<yourname>_rows.json:
     rows = list of {term: "a"|"b", chirality: "+/−/±±±", slotperm: ...,
     coeff: exact rational×i-power, color: ordered string like "c[C1,U1,E1]c[...]...",
     with explicit index contraction pattern,
     numerator: polynomial in symbols pl[a,ad], pk[a,ad], pp[a,ad] (entries of
     𝗉(ℓ),𝗉(k),𝗉(p)) with output-jet basis word,
     outjet: one of {v, Dav[a], Dbv[ad], D2v, DaDbv[a,ad], Db2v, D2Dbv[ad], Db2Dav[a],
     DaDb2Dav-type longer words...}, theta0: monomial in θ₀,θ̄₀},
 (b) a human-readable markdown summary: the reduced numerator organized covariantly
     as far as you can (σ-words), the count of nonvanishing rows, which chirality
     assignments survive, and any exact cancellations you can prove.

Also report: the A↔B exchange property of the total (under relabeling ℓ↔p−ℓ, k↔−k and
swapping X₁↔X₂), and the total's output-jet content (which jets actually appear).

## 6. CALIBRATION GATES (mandatory, in order; do not proceed past a failed gate)

Level 0: the D-algebra anchors of §1.
Level 1 (one-loop locked seed, MUST match `audits/step5-canonical-superfield-ww-seed.md`
§§5–9 exactly): triangle O(θ₀)–Y₁(θ₁)–Y₂(θ₂); lines O→Y₁ (mom r₀=k), Y₁→Y₂, Y₂→O;
insertion term 𝔞 at O as in §3; Y₁ = ANTIchiral vertex (χ=−) with its E-slot (W̃-slot)
leg EXTERNAL carrying the letter W̃^D_ȧ(q) [external momentum q incoming at Y₁];
Y₂ = chiral vertex (χ=+) with its E-slot (W-slot) leg EXTERNAL as X^E := D₊W₊(p)
[the vertex's W-leg dressed with the extra D₊ ... reproduce the seed's 𝒪_{A,μν}];
internal momenta r₀ = k, r₁ = k+q, r₂ = k+P with P = p+q.
REQUIRED result (seed §8): Γ_{T,A} = (ħg²/2) 𝒞^{AB}{}_{DE} 𝒪^{DE}_{A,μν}
· μ^{2ε}∫ d^dk/(2π)^d L₁^μ L₂^ν/(k²(k+q)²(k+P)²), with L₁ = 2k+q, L₂ = 2k+p+2q,
𝒪_{A,μν} = W̃^D_α̇(q) p^ρ X^E(p) T_{μρν,+}{}^{α̇}, T_{μρν} = σ_{E,μ}σ̄_{E,ρ}σ_{E,ν};
equivalently reproduce the 8-row endpoint table of seed §6 and w_D = 2 of §7.
If your realization reproduces this up to an overall sign/isomorphic relabeling,
document the exact dictionary between your realization and the seed's.
Level 2 (2-loop internal consistency): momentum-relabeling invariance
(ℓ→p−ℓ, k→−k, X₁↔X₂ must map the row set to itself up to the A↔B swap);
D̄-counting selection rules (chirality assignments that cannot saturate both loops
must come out exactly zero from the engine, not be pruned by hand).

## 7. DRED / anomaly-sector definitions (for the integral workers)

From the settlement §1 (all locked at one loop; the 2-loop extension below is
[D-choice D3], flag it as such):
- d = 4−2ε. Loop momenta are d-dimensional in propagators. Spin-word numerators
  produced by the 4-dimensional D/σ-algebra carry 4-dim (bar) squares.
- μ_ℓ² := ℓ̄² − ℓ_d² (= −ℓ̃², the evanescent square); μ_p² = 0 for the external p
  (external momenta strictly 4-dim/hatted).
- [D-choice D3] Two-loop extension: both loop momenta split ℓ_d = ℓ̄ + ℓ̃, k_d = k̄ + k̃
  with a COMMON 2ε-dimensional evanescent subspace; the three evanescent invariants are
  μ_ℓ² = −ℓ̃², μ_k² = −k̃², μ_{ℓk} := −ℓ̃·k̃. Angular averages in the evanescent
  subspace: ⟨ℓ̃^μ ℓ̃^ν⟩ = (ℓ̃²/(2ε)) δ̃^{μν} (use with care: produces 1/(2ε)
  enhancements on μ_{ℓk}² terms; keep all O(ε) pieces of sub-integrals).
- One-loop anchor (must be reproduced by your integral technology):
  μ^{2ε} ∫ d^dℓ/(2π)^d · μ_ℓ²/(ℓ²+Δ)³ = 1/(32π²) + O(ε), Δ-independent;
  via μ_ℓ²-insertion rule ∫ μ_ℓ² f(ℓ²) = ((4−d)/d)∫ ℓ² f(ℓ²) (settlement/HK.21).
- Anomaly sector := the μ-dependent part of the reduced numerator after writing every
  4-dim spin-word square r̄² over d-dim denominators as r̄² = r_d² + μ_r², i.e. the
  occurrence-wise cutting failure  r̄_e²/(∏D) − 1/(∏_{j≠e}D_j) = μ_e²/(∏D),
  applied per marked edge, plus (at two loops) the double-failure terms.

## 8. Kite μ-masters wanted (Feynman-parameter evaluation, then numeric check)

With K := D₁D₂D₃D₄D₅ as in §4 (Euclidean), compute through O(ε⁰), keeping exact
Γ-function/parametric forms at intermediate steps:
  M1 := ∫∫ μ_ℓ² μ_k² / K
  M2 := ∫∫ μ_k² / K          (has a 1/ε from the outer subgraph — exhibit it)
  M3 := ∫∫ μ_ℓ² / K
  M4 := ∫∫ μ_{ℓk} / K,  M5 := ∫∫ μ_{ℓk}² / K
  and the contact daughters with one denominator removed:
  M1/j := ∫∫ μ_ℓ²μ_k²/(K/D_j) for j=1..5, similarly M2/j, M3/j as needed.
  (∫∫ := μ^{4ε}∫ d^dℓ d^dk/(2π)^{2d}.)
Method: inner loop first with Feynman parameters and the μ-insertion lemmas; derive
the general lemma for ∫ d^dk μ_k^{2m}/((k²+Δ)^n); then outer loop. Present every step.
Numeric cross-check: for 2–3 masters, verify the parametric formula by direct numeric
integration of the Feynman-parameter representation at small ε (e.g. ε ∈ {0.02, 0.01},
Richardson-extrapolate to 0) at p² = 1.

## 9. Known structural claims to TEST (do not assume)

(V1) Charge/parity claim: every single-field output jet, after ∫∫ and index
contraction with only one external p available, assembles into words
𝗉_{+ȧ}(p)𝗉_{+ḃ}(p)𝗉_{+ċ}(p)×(jet) whose full ε-contractions vanish identically
(𝗉_{+ȧ}𝗉_{+ḃ}ε^{ȧḃ} = 0 for a single p). Hence the graph's total local output at
ε→0 is zero — the superspace image of HT's expected truncation (arXiv:2512.07771v2
line 222: corrections on length-n words expected to truncate at Q_{n−1}).
(V2) Color parity claim: the tip-日 color word reduces to
𝒞₃^{AB}{}_G ∝ κ-raised c_{AMS₁}c_{BMS₂}c_{GS₁S₂}, antisymmetric under A↔B, while the
kinematic sum is A↔B symmetric after relabeling; independently forces zero total.
(V3) The μ_{ℓk}²/(2ε) enhancement cannot generate a finite escape from (V1)/(V2)
because the final tensor structures are unchanged.
Each verifier must genuinely attempt to REFUTE these using the engine row output.

---
---

# SPEC v2 ADDENDUM (2026-07-17) — PRIMARY TARGET IS NOW THE LENGTH-3 WORD

The owner refined the task: in N=4 SYM the first nonvanishing two-loop correction
requires a length-3 word. NEW primARY target: the pure-gauge insertion

   ℐ₃^{ABC} = D₋[ (K₊v^A)(K₊v^B)(K₊v^C) ],   K₊ = −¼D₊D̄²D₊,  D₋K₊ = −⅛D²D̄²D₊,

i.e. project ∇₋(A^A A^B A^C), A = ∇₊𝒲₊. THREE ∇₋-placements 𝔞/𝔟/𝔠 (Leibniz on the
three bosonic legs). The length-2 tip graph of SPEC v1 §4 is DEMOTED to a secondary
validation run (its total local output must vanish by the single-letter theorem —
run it to confirm the machinery, then move on).

## v2.4 The AAA 日 graph (K4−e with the insertion at a degree-3 corner)

Vertices: O(θ₀) [insertion, degree 3], X_mid(θ₃) [cubic, degree 3],
X_a(θ₁), X_b(θ₂) [cubic, degree 2, one external letter each].
Missing K4 edge: X_a–X_b. The 日 rectangle is O, X_a, X_mid, X_b with middle bar O–X_mid.

Momenta (all incoming at O equals q₁+q₂ =: Q; outputs carry q₁ out at X_a, q₂ out at X_b):
  L1: O→X_a  momentum ℓ,        D₁ = ℓ²
  L2: O→X_b  momentum k,        D₂ = k²
  L3: O→X_mid momentum Q−ℓ−k,   D₃ = (Q−ℓ−k)²
  L4: X_mid→X_a momentum q₁−ℓ,  D₄ = (q₁−ℓ)²
  L5: X_mid→X_b momentum q₂−k,  D₅ = (q₂−k)²
Momentum conservation holds at every vertex; loops (ℓ,k).

Sum over: 3 ∇₋-placements × 3! assignments of the color-labeled insertion legs
{A,B,C} to lines {L1,L2,L3} × chirality (χ_mid,χ_a,χ_b) ∈ {±}³ × slot assignments
(X_mid: 3! internal; X_a, X_b: 3! over {2 internal lines + 1 external leg}).
Vertices and all factors exactly as SPEC v1 §2; propagator (K.2); Koszul signs 5A.61–62.

Engine deliverables: as v1 §5 but for this graph, files
  engine_<name>_rows3.json / engine_<name>_summary3.md.
The reduced numerator now retains TWO output jets (at X_a: jet₁(q₁); at X_b: jet₂(q₂)).
Organize rows by (jet₁, jet₂) pairs. Expected (TEST, do not assume): after loop
integration the local output lives in P-dressed two-letter words; the leading
gauge-covariant family is 𝗉(q)³-dressed (W̃-jet ⊗ (D₊W₊)-jet)-type; U/ghost-type
non-covariant jets (bare v, D_a v jets) may appear per-graph and should be reported,
not discarded. NONZERO total expected (two independent external momenta:
ε^{ȧḃ}𝗉_{+ȧ}(q₁)𝗉_{+ḃ}(q₂) ≠ 0 — the v1 §9 vanishing theorem does NOT apply).

## v2.5 Color (3-c word)

Insertion legs carry free A,B,C onto L1/L2/L3 per assignment; vertex c's:
X_mid: c over (L3,L4,L5)-slots; X_a: c over (L1,L4,output-D); X_b: c over (L2,L5,output-E).
All internal contractions through κ. Generic word:
  𝕋^{ABC}{}_{DE}-family: κ-raised c_{C M N} c_{A M D} c_{B N E}-type (and its
  slot-permutation images). Color worker: enumerate the distinct contraction patterns,
  reduce each to the basis {c_{ABX}c-type words}, give su(2)/su(3) numeric checks, and
  the symmetry properties under (A,q₁-leg)↔(B,q₂-leg) exchange etc.

## v2.6 Masters for the AAA kite (K' := D₁D₂D₃D₄D₅ of v2.4)

Archetype (derive + verify; my hand result to cross-check):
  N1 := ∫∫ μ_ℓ² μ_k² / K'
      = (1/32π²)·∫_ℓ μ_ℓ²/(ℓ²(q₁−ℓ)²) + O(ε)      [inner-k μ²-triangle is Δ-independent]
      = (1/32π²)(−q₁²/96π²) = −q₁²/3072π⁴ + O(ε).
  N1' (ℓ↔k mirror) = −q₂²/3072π⁴.
Full list needed: N2 := ∫∫μ_ℓ²μ_{ℓk}/K', N3 := ∫∫μ_{ℓk}²/K', N4 := ∫∫μ_{ℓk}/K',
N5 := ∫∫μ_k²/K', N6 := ∫∫μ_ℓ²/K' (exhibit any 1/ε), the middle-line marking uses
μ_{L3}² = μ_ℓ² + 2μ_{ℓk} + μ_k² (external Q strictly hatted), plus the
one-denominator-removed daughters and the ℓ^μ/k^μ-numerator-dressed versions via
tensor reduction lemmas. Numeric spot checks at q₁², q₂², q₁·q₂ generic (e.g.
q₁²=1, q₂²=2, q₁·q₂=0.3), same method as v1 §8.
