# FeynArts/FeynCalc capability port — AWIGraphs diagram-engine design

Status: `NON_AUTHORITY_PROPOSAL`
Date: 2026-07-16
Authorization context: 2026-07-16 session — the owner asked to port the FeynArts/FeynCalc
capability set (standard component diagrams and supergraphs, operator insertions with
uncontracted legs, automated evaluation) into this repository under Project notation.
Owner decisions recorded in §2.4.

This document is a design specification only. It states no mathematical result, locks no
convention, and is not evidence for any obligation. Every physics claim referenced here
lives in the cited contract; every new physics claim this design needs is assigned to a
future obligation whose memo will derive it.

---

## 1. Substrate findings that constrain the design

The design follows a code study (2026-07-16) of the four relevant systems. Only the
facts that constrain the architecture are recorded here.

### 1.1 FeynArts 3.12 (local install, and the FCFAPatch-ed copy inside FeynCalc)

- Topology generation (`CreateTopologies`, `Topology.m`) is pure graph combinatorics:
  recursive leg-adding from hard-coded starting topologies, canonical-sort duplicate
  elimination, symmetry factors `Topology[s]` meaning `1/s`. It is self-contained
  (~850 lines) and independent of any model file, so using it introduces no external
  physics claim.
- Field insertion (`InsertFields`) and amplitude assembly (`CreateFeynAmp`) read a
  two-tier model format: `.gen` files carry generic Lorentz structures as
  G-vector · kinematic-vector; `.mod` files carry particle classes and coupling
  matrices. These files embed propagators and vertices as data. Under the Project
  rigor law (AGENTS.md: never quote a propagator, vertex, sign, or multiplicity)
  they are inadmissible as input; any insertion rules must be Project-derived.
- FeynArts has no native composite-operator insertion or open-leg mechanism. The
  standard idiom is: an auxiliary non-propagating source class
  (`InsertOnly -> {External}`) carries the operator momentum; each uncontracted
  operator field is an ordinary external leg; `Truncated -> True` amputates external
  wavefunctions, yielding off-shell amputated Green functions. This idiom is
  structurally identical to the MVP's `OPERATOR_SOURCE` + `UNCONTRACTED_FIELD`
  representation (§1.3), which validates keeping that representation.
- Two copies exist on the development machine (vanilla and the FeynCalc-bundled
  FCFAPatch-ed copy, both 3.12). Loading both causes context clashes. This design
  standardizes on the FeynCalc-bundled copy.

### 1.2 FeynCalc 10.1.0

- Its three-tier typed dimension system (4-dim `SP`, D-dim `SPD`, (D−4)-dim `SPE`,
  with the dimension carried on every `Momentum`/`LorentzIndex`) demonstrates the
  right mechanism for the Project law "never use an untyped momentum square":
  make untyped squares inexpressible at the constructor level.
- FeynCalc implements BMHV (4-dim space embedded in D-dim; `Pair[4, D−4] -> 0`
  fires globally as an upvalue and cannot be disabled locally). The Project scheme
  is DRED with a two-representation evanescent ledger
  (`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` §1: finite spin
  words use the bar/tilde split, propagator inverses use the d-dim delta,
  `mu_l^2 := bar-l^2 − l_d^2`; combining the representations early erases the
  anomaly). These two algebras are different and must not be mixed. Consequence:
  the Project's dimensional algebra is implemented in Project code with its own
  heads; FeynCalc's heads and automatic contraction rules are never used inside
  authoritative computations.
- FeynCalc is four-component-Dirac, mostly-minus, Lorentzian only; the Project is
  two-component Srednicki index placement with Weinberg phases, mostly-plus,
  intrinsically Euclidean for the accepted sector. Any FeynCalc comparison
  therefore needs an explicit, non-authoritative translation dictionary and is
  possible only where the schemes overlap (e.g. gamma5-free tensor reduction).
- Useful as a cross-check target: FeynCalc's shipped Pi→GaGa example reproduces
  the ABJ anomaly from the evanescent `(D−4)·C0` term under BMHV + `TID` — an
  independent (different-scheme) route to compare one-loop anomaly structures
  against, never as evidence.

### 1.3 The existing N1Supergraphs MVP (branch `codex/step5-n1-supergraph-mvp`, unmerged)

A fail-closed representation and verification layer, not a calculator. It establishes
three patterns this design keeps:

1. Substrate non-authority: FeynArts used only for bare topologies and layout,
   FeynCalc loaded only as a pinned runtime substrate
   (`substrate_role = RUNTIME_API_ONLY_NOT_MATHEMATICAL_AUTHORITY`).
2. Content addressing and fail-closed semantics: SHA-256 certificates over canonical
   string payloads, four-value result semantics
   (`VALID | ZERO | BLOCKED | INCONSISTENT`), explicit blocker ledgers, validators
   that recompute every certificate, and a stdlib-Python verifier that re-derives
   certificates, combinatorics, and algebra from the exported artifacts with no
   Mathematica dependency.
3. Open legs as first-class objects: every unmatched field occurrence of a compiled
   operator becomes an explicit external leg (`contraction_status: UNMATCHED`,
   leg status `FORMAL_PROVISIONAL_UNCONTRACTED`); the operator insertion attaches
   through a non-Wick `OPERATOR_SOURCE` external source that never counts as a
   topology edge.

Known defects the port must not inherit: hardcoded `base_commit` and repository-slug
pins inside certificates (invalidated by any rebase); one opaque
`operator_ast_hash` computed with Wolfram's internal `Hash[expr]` (not recomputable
outside WL); brute-force `Permutations` canonical labeling (factorial blowup beyond
3 vertices); over-tight environment assertions (Wolfram "14.2" in the WL tests vs
"14.2.1" in the Python verifier); single-operator hardcoding throughout builders,
validators, tests, and census driver; 100 machine checks and ~17k changed lines,
which conflict with the derivation-first law of 2026-07-16.

### 1.4 Governance constraints (binding on this design)

- One active mathematical obligation at a time; contracts change only under
  `CONTRACT_CHANGE` or `AUTHORITY_REPAIR` tasks (AGENTS.md).
- Derivation-first law (AGENTS.md, 2026-07-16): the primary artifact of every
  obligation is a human-readable memo with numbered equations; at most ~3000
  hand-written lines per reviewed PR; at most 10 exact machine checks per
  obligation, chosen for load-bearing factors; `generated/` artifacts are marked
  generated and are not acceptance evidence by themselves.
- CI (`.github/workflows/verify.yml`) installs only sympy and PyYAML; there is no
  Wolfram kernel in CI, and none will be added (owner decision, §2.4).
- Vertices must be derived by ordered functional differentiation from the locked
  action; every Wick pairing, fermion permutation, color ordering, and symmetry
  factor must be emitted; every symbolic rewrite must log input, rule, conditions,
  sign, output, and invariant checks (AGENTS.md rigor law).
- The vertex layer is locked to all orders in coordinate superspace
  (step-05a §5A.9: gauge-word coefficients, ordered adjoint color chains, N=4
  cubic primitives, Bernoulli ghost words, Koszul-sign ordered differentiation
  5A.61–5A.62, graph weights and the automorphism symmetry-factor definition
  5A.63). The superspace propagator layer is deliberately not locked
  (5A.80 blockers: unique perturbative slice, Nielsen–Kallosh branch,
  momentum/Fourier/DRED ledger); the Euclidean Fermi–Feynman set 5A.64–5A.74 is
  conditional. The staging proposal for locking it is
  `proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md`.
- The accepted physical anchor: the Step-5 Euclidean N=4 one-loop AWI settlement
  (`contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`) with the 81-pair
  target-blind ledger (29 `EXACT_NONZERO`, 52 `EXACT_ZERO`) and the
  `1/(32 pi^2)` cutting-failure master integral.
- The archived Step-5 task's acceptance clauses already fix the required engine
  architecture: a deterministic Wick-contraction enumerator produces a
  machine-readable graph IR; rendered diagrams are generated from the same IR as
  amplitudes, so no drawn edge exists without an algebraic object; the D-algebra
  engine records every rewrite with its Koszul sign.

---

## 2. Architecture

### 2.1 Components

One Wolfram package, `wolfram/AWIGraphs/`, with four modules and one Python
verification layer:

| Unit | Purpose | Depends on |
|---|---|---|
| `AWIGraphs`IR` | The shared graph IR (`awi.graph.v1`): builders, validators, certificates, canonical labeling | contracts (anchors only) |
| `AWIGraphs`Substrate` | FeynArts adapter: bare-topology import, layout/rendering, runtime pinning report | FeynArts (FCFA copy), IR |
| `AWIGraphs`Rules` | Rule-bundle format, the rule gate, ordered functional differentiation engine | IR, locked actions |
| `AWIGraphs`Eval` | Typed DRED momentum algebra, Wick enumerator, evaluation pipelines (component first, D-algebra later) | IR, Rules |
| `scripts/verify_awigraphs_*.py` + `tests/test_awigraphs_*.py` | Per-obligation stdlib-Python re-verification and CI receipts | exported JSON/SVG artifacts |

Roles: FeynArts and FeynCalc are pinned runtime substrates
(`RUNTIME_API_ONLY_NOT_MATHEMATICAL_AUTHORITY`), recorded by entry-point SHA-256
and version string in every runtime report. They never supply a propagator,
vertex, sign, multiplicity, or scheme identity. All physics content enters
through Project-derived, memo-pinned rule bundles.

### 2.2 Data flow

```
operator expression (inert surface syntax)
        │  compile
        ▼
insertion seed (COMPOSITE_INSERTION vertex, open legs)      ┐
        │                                                    │ IR objects,
FeynArts CreateTopologies ──adapter──► bare topologies       │ each carrying a
        │  merge + canonical labeling                        │ recomputable
        ▼                                                    │ SHA-256
census candidates (topology-level)                           │ certificate
        │  rule gate: verified rule bundle only              │
        ▼                                                    │
Wick-enumerated labeled graphs (pairings, signs, factors)    │
        │  evaluation pipeline (typed DRED momenta)          │
        ▼                                                    │
amplitudes / ledger rows ──────► generated/ JSON + receipts  ┘
        │
        └──► rendering (same IR) ──► SVG/PNG with injected semantic metadata
```

CI re-verifies the exported artifacts in pure Python (certificates, combinatorics,
algebra, byte-identity of receipts). Wolfram runs only on the development machine.

### 2.3 Obligation sequence

The port is four obligations, each a single task with its own memo, each
independently reviewable, executed in this order (the separate Step-5B
propagator contract change, already staged by its memo, interposes between C
and D):

- **Obligation A — shared graph IR and substrate adapter** (§3). Representation and
  combinatorics only; no physics claims.
- **Obligation B — component rule bundle** (§4). Derives the Euclidean component
  vertex tables and adopts the accepted Step-5 propagator representative as a
  machine-readable, memo-pinned rule bundle.
- **Obligation C — component diagram engine and 81-pair round trip** (§5).
  Wick enumeration, census, automated evaluation; regression target = the accepted
  81-pair ledger and the `1/(32 pi^2)` master.
- **Obligation D — supergraph engine** (§6). Superspace dialect vertex letters
  (5A.52–5A.59), D-algebra engine; propagator layer gated on a prior Step-5B
  contract change resolving the 5A.80 blockers.

### 2.4 Owner decisions recorded (2026-07-16 session)

1. Milestone order: shared IR first, component ("standard") diagrams second,
   supergraphs third.
2. The `codex/step5-n1-supergraph-mvp` branch is not merged. Its IR schema,
   open-leg/operator-source conventions, certificate patterns, and Python
   re-verification pattern are inherited into the new obligations; the branch is
   retained read-only as reference until Obligation A supersedes it, then closed.
3. CI runtime: keep the local-Wolfram → committed-receipt → pure-Python
   re-verification pattern. No Wolfram kernel in CI.

---

## 3. Obligation A — shared graph IR (`awi.graph.v1`) and substrate adapter

### 3.1 IR schema

One schema, two dialects, distinguished by a top-level field
`dialect: COMPONENT | SUPERSPACE`. Kept from `awi.n1-supergraph.v0`:

- Vertex kinds `COMPOSITE_INSERTION` and `ACTION_VERTEX` (the placeholder kind
  `ACTION_VERTEX_PLACEHOLDER` becomes `ACTION_VERTEX` with `rule_id: Null` while
  unbound, `rule_id: <verified id>` once a rule bundle binds it).
- Ports, one per field occurrence, carrying field letter, color/index space,
  chirality/representation, parity, contract-anchor certificate, and
  `contraction_status`.
- The partition invariant: every port belongs to exactly one internal edge or
  exactly one external leg, never both, never neither.
- Open legs as first-class objects: uncontracted operator fields are external
  legs (`UNCONTRACTED_FIELD`); the operator source is a non-Wick external
  attachment (`OPERATOR_SOURCE`, `counts_as_topology_edge: False`, double-line
  render). External legs are amputated by construction: the IR attaches no
  wavefunction object to a leg, which is the IR-level form of the FeynArts
  `Truncated -> True` idiom.
- `topological_loop_number` (Euler formula, always computable) kept separate from
  `perturbative_loop_order` (Null until a rule bundle binds the graph).
- Four-value result semantics and explicit blocker ledgers on every artifact.

Added in v1:

- `dialect` and per-dialect field alphabets bound to contract anchors
  (COMPONENT: the Step-5A component letters; SUPERSPACE: V, Phi, tilde-Phi, W
  letters of the 5A grammar).
- Wick-pairing records (Obligation C fills them): ordered list of pairings, each
  with the fermion-permutation sign, color word, and the automorphism-quotient
  symmetry factor, so that "emit every Wick pairing" is a schema field, not prose.
- Momentum-routing slots with typed momentum labels (§5.2 types), Null until
  evaluation binds them.

Blocker vocabulary: `awi.graph.v1` artifacts use the Step-5A blocker tokens
(5A.80 family). The MVP's older Step-3E token ledger is not carried over; the
supersession note in the Obligation A memo states this explicitly.

### 3.2 Substrate adapter

- `CreateTopologies` output (bare topologies + FeynArts symmetry-factor
  candidates) is mapped bijectively into IR topology candidates. The adapter
  imports only: vertex degrees, edge incidences, external attachment points, and
  the combinatorial factor as a *candidate* value. Nothing model-related is read.
- The Project symmetry factor is computed independently from the 5A.63
  automorphism definition (automorphisms preserving field type, chirality, edge
  orientation, derivative slot, and ordered color word; divide exactly once).
  The FeynArts candidate value is compared as a cross-check on bare topologies
  (where the two definitions coincide) and discarded where they do not.
- Rendering: FeynArts `Paint`/`MmaRender` produce the layout; the Project overlay
  injects semantic identity (`<metadata id="awi-ir-object-ids">` in SVG, as in
  the MVP) so that every drawn edge and vertex names its IR object. Rendering
  reads only the IR; a graph that fails validation cannot be rendered (fail
  closed, MVP behavior kept).
- Runtime pinning: a runtime report records Wolfram version, FeynCalc and
  patched-FeynArts entry-point SHA-256s and version strings. Version identity is
  *recorded*, not *asserted*: verification compares artifacts against the
  recorded report rather than hard-coding version literals in two places (the
  MVP's 14.2 vs 14.2.1 defect class).

### 3.3 Canonical labeling

Replace the MVP's brute-force `Permutations` canonicalization with
iterative-refinement canonical labeling (degree/color-class refinement with
backtracking, insertion vertex pinned first), which is exact and scales past
3-vertex graphs. The canonical-key string format
(`P<grade>_<sourceTuple>|A=<upper-triangle>|X=<attachments>`) and the
independent-oracle bijection check are kept unchanged, because the Python/CI
layer keys on those strings. The Obligation A memo defines the refinement
algorithm with numbered equations and proves key stability (same graph, same
key) on the existing census bucket.

### 3.4 Certificates

All certificates are SHA-256 over canonical newline-joined `key=value` string
payloads (the MVP's `AWI_SEED_CORE_V1` pattern), recomputable byte-exactly in
stdlib Python. Two repairs relative to the MVP:

- No Wolfram-internal `Hash[expr]` anywhere; operator ASTs are hashed via their
  canonical string serialization.
- No hardcoded `base_commit` or repository slug inside certificate payloads;
  provenance (commit, branch) lives in the receipt envelope, injected at export
  time, so certificates survive rebases.

### 3.5 Obligation A deliverables and checks

Deliverables: memo (IR definitions, canonical labeling, symmetry-factor
definition per 5A.63, supersession statement for the MVP branch), the
`AWIGraphs`IR` + `AWIGraphs`Substrate` modules, one example census bucket
regenerated (the existing 1-loop P2/E2 bucket), one Python verifier + receipt.

Machine checks (≤10, load-bearing): certificate cross-language round trip;
port-partition and Euler-loop identities on exported graphs; canonical-key
oracle bijection on the regenerated bucket; canonical-form idempotence under a
nontrivial relabeling; byte-determinism of repeated JSON/SVG export; receipt
`--check` byte-identity.

---

## 4. Obligation B — component rule bundle

### 4.1 Content

A machine-readable rule bundle for the Euclidean component dialect:

- **Vertices**: derived in the memo by ordered functional differentiation from
  the locked Euclidean component actions (step-05a §5A.2–5A.4), with every
  Koszul sign logged per 5A.61–5A.62. The engine implements the differentiation
  (a Project-side analogue of FeynArts' ModelMaker) and the memo's numbered
  equations are the authority; the code reproduces them.
- **Propagators**: the accepted Step-5 physical representative (Fermi–Feynman
  representative, Fourier all-incoming convention, DRED two-representation
  evanescent ledger), imported by contract reference from
  `step-05-euclidean-n4-awi-one-loop.md` — within its accepted scope only.
  No new propagator claim is made; scope limits are recorded in the bundle.

### 4.2 Bundle format

Inherits the MVP's rule-gate design: a bundle is a list of rules, each with
`rule_id`, kind (`VERTEX | PROPAGATOR`), dialect, field letters, the exact
coefficient, the memo equation number(s) that derive it, contract anchors, and a
certificate. `N1EnumerateN4InsertionGraphs`-style enumeration entry points accept
only bundles whose every rule is verified (present in the bundle registry with a
green receipt); unverified rules keep the census `BLOCKED` — the gate logic is
ported, then finally fed.

### 4.3 Checks (≤10)

One seed-coefficient chain per action sector (gauge, matter, ghost) recomputed
exactly in Python from the memo equations; bundle-certificate round trip;
closure of each vertex table under the field permutations its symmetry claims;
receipt byte-identity.

---

## 5. Obligation C — component diagram engine and 81-pair round trip

### 5.1 Wick enumerator

Deterministic enumeration of labeled graphs from (insertion seed × rule bundle ×
topology census): every Wick pairing emitted as an IR record with its fermion
permutation sign, ordered color word, and 5A.63 symmetry factor. The enumerator
is target-blind: it never reads expected results. Output = the component graph
family for the AWI one-loop sector, in `generated/` with receipts.

### 5.2 Typed DRED momentum algebra

Project-side implementation (no FeynCalc heads) of the Step-5 two-representation
ledger, following FeynCalc's *mechanism* (dimension tag on every momentum and
index) but the Project's *algebra*:

- Momentum types: `4`, `d`, `bar`, `hat`, `breve`, `tilde` per Step-5 §1; the
  constructor for a momentum square requires both factors' types and applies only
  the contract-derived contraction table; an untyped square is unrepresentable.
- The two representations (spin words vs propagator inverses) are separate types
  that no automatic rule merges; `mu_l^2 := bar-l^2 − l_d^2` exists only as an
  explicit rewrite whose every application is logged (rigor law).
- Evaluation pipeline: Schwinger-cut evaluation of the enumerated family,
  reproducing the occurrence-wise cutting-failure mechanism.

### 5.3 Round-trip anchor and checks (≤10)

The external regression targets are the two accepted results: exact equality of
the regenerated ledger with the 81-pair target-blind ledger (29 nonzero /
52 zero), and the `1/(32 pi^2)` master coefficient. Remaining checks: one
end-to-end seed-graph weight chain (the accepted WW seed), zero-pair
certificates spot-recomputation in Python, receipt byte-identity. A FeynCalc
BMHV cross-comparison (Pi→GaGa-style, on an overlap step with no gamma5
ambiguity) is run and reported in the memo as non-authoritative corroboration —
it is not one of the machine checks.

---

## 6. Obligation D — supergraph engine

- Superspace dialect rule bundle: vertex letters bound directly to the locked
  all-order grammar (5A.52 gauge-word coefficients, 5A.53a/5A.54 ordered adjoint
  color chains, 5A.55 N=4 cubic primitives, 5A.57–5A.59 Bernoulli ghost words).
  These are already contract-locked; the bundle memo only transcribes and pins
  them (no new derivation), plus derives any finite-order specializations used.
- Propagator layer: remains `BLOCKED` until a Step-5B contract change resolves
  the 5A.80 blockers (unique perturbative slice, Nielsen–Kallosh branch,
  momentum/Fourier/DRED ledger). Step-5B is a separate, prior obligation seeded
  by the existing Step-5B memo; Obligation D consumes its contract. Until then
  the conditional Fermi–Feynman family (5A.64–5A.74) may be wired only under the
  existing `CONDITIONAL_STRUCTURAL_LABEL` convention.
- D-algebra engine: reduction of covariant-derivative words on supergraph edges,
  with every rewrite logged as (input, rule, conditions, Koszul sign, output,
  invariant checks) per the rigor law and the archived Step-5 acceptance clause.
- The not-fully-contracted mechanism needs no new design here: it is the same
  `COMPOSITE_INSERTION`/open-leg IR of Obligation A, with superspace letters.
- Checks (≤10): D-algebra invariant conservation on a worked reduction chain;
  supergraph census bijection against the component-dialect census where the two
  dialects must agree (bottom components); rule-bundle and receipt round trips.

---

## 7. Notation layer

- Every IR field letter, index space, and phase convention is bound to the
  Weinberg–Srednicki project notation dictionary
  (`contracts/dictionaries/weinberg-srednicki-project-notation-dictionary.md`):
  Srednicki index placement, Weinberg quantities and phases (no silent
  rephasing), mostly-plus metric, Euclidean column for the accepted sector.
  New contracts remain Euclidean-first per the owner-approved slimming spec.
- Rendering and any LaTeX export emit Project notation only. FeynCalc's broken
  `FeynCalcToLaTeX` is not used; if LaTeX export is needed it is generated from
  the IR directly.
- The FeynCalc↔Project translation dictionary exists only inside Obligation C's
  cross-check module, is marked non-authoritative, and covers exactly the overlap
  used by the cross-check (metric sign map, momentum-square type map, trace
  normalization, Levi-Civita sign).

### 7.1 Local interactive workflow

The development machine keeps the FeynCalc-style ergonomics: a shim package
`~/Library/Wolfram/Applications/AWIGraphs/Kernel/init.m` containing a single
`Get` of the repository package (the same pattern as the current N1Supergraphs
shim), so notebooks load the engine with ``Needs["AWIGraphs`"]``. The shim is
machine-local and never part of the repository.

---

## 8. Verification, error handling, and testing strategy

- **Fail-closed everywhere**: builders and validators return `BLOCKED` with a
  named blocker token on any missing input, unverified rule, failed certificate,
  or unsupported shape — never a partial result. Export refuses invalid graphs.
  Renderers refuse unexported semantics. (MVP behavior, kept.)
- **Two-layer verification per obligation**: (1) a Wolfram test driver run
  locally, asserting the obligation's invariants and writing a receipt that pins
  source-file SHA-256s; (2) a stdlib-Python verifier that recomputes
  certificates, combinatorics, and the load-bearing algebra from the committed
  artifacts, run by CI via one `tests/test_awigraphs_*.py` module with the
  `--write`/`--check` byte-identity pattern.
- **Check budget**: each obligation's machine checks are listed in its section
  above and capped at 10; everything else is human-verified derivation in the
  memo, per the derivation-first law. The Wolfram-side test driver asserts the
  same named checks (each naming its memo equations) plus nothing else; only
  the Python re-verification is acceptance evidence.
- **Artifacts**: engine outputs live under `generated/awigraphs/`, marked
  generated, never acceptance evidence by themselves; receipts live in
  `audits/`; the paper file is updated in the same PR whenever an obligation
  changes a stated result or convention.

---

## 9. Explicitly deferred decisions

Deferred to the named obligation's memo (none blocks Obligation A's start):

1. Final package name (`AWIGraphs` is the working name) — Obligation A memo,
   first section.
2. The exact refinement/backtracking variant for canonical labeling —
   Obligation A memo (§3.3 fixes the requirements: exact, deterministic,
   key-format-stable).
3. Step-5B propagator contract content (5A.80 resolutions) — the Step-5B
   obligation, before Obligation D.
4. The supergraph operator alphabet beyond the MVP's single operator shape —
   Obligation D memo (Obligation A only requires that the compiled-operator
   surface syntax not hardcode one shape).
5. Whether the two-loop program (`agent/step6-pure-gauge-two-loop`) consumes
   this engine or keeps its own route — out of scope for all four obligations.
