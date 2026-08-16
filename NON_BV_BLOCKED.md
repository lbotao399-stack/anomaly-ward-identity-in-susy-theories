# BLOCKED — CONTAMINATED LEGACY NON-BV CALCULATION

千万不要引用、复用或作为参考。含有污染。

Effective 2026-08-15. This quarantine supersedes earlier labels such as `ACCEPTED`, `DERIVED_UNFROZEN`, `PASS`, `verified`, graph-census completion, test success, PDF completion, and Notion mirror completion whenever the underlying object is listed below. Files remain only as provenance. Nothing is deleted.

## Protected boundary

The following material is excluded from this bulk non-BV block:

- exact source snapshots under `references/vendor/notion/weinberg/` for Weinberg Chapters 26 and 27;
- the user's locked Notion 30.4 source notation, which is an external source boundary and is not reconstructed from this repository's legacy calculations;
- `contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md`;
- `contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md`.

The two BV files are protected as the latest BV-centered work. “Protected” does not mean that every coefficient, dependency, or quantum claim in them is independently certified.

`AUTHORITY.md`, `AGENTS.md`, repository policy, build plumbing, hashes, and mirror receipts may be used only as administrative metadata. They do not validate physics.

## Blocked paths

The following derived material is blocked recursively:

- `contracts/foundations/step-01-supersymmetry-commutator.md`;
- `contracts/foundations/step-02a-flat-superspace.md`;
- `contracts/foundations/step-02b-superconformal-superspace.md`;
- `contracts/foundations/step-02c-complete-superconformal-covariance.md`;
- `contracts/foundations/step-03a-gauge-chiral-action.md`;
- `contracts/foundations/step-03b-component-reconstruction.md`;
- `contracts/foundations/step-03c-gauge-vector-representation.md`;
- `contracts/foundations/step-04-extended-sym-notation.md` and `step-04a` through `step-04c`;
- `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md`;
- `contracts/dictionaries/**`;
- `paper/**`, `audits/**`, `generated/step5/**`, `proposals/**`, and `ledger/**`;
- `Current work日志.md`;
- legacy non-BV entries in `tasks/archive/**` and any current task whose allowed inputs point to the blocked paths above;
- `scripts/step5*.py`, the non-BV `scripts/verify_step2*`, `scripts/verify_step3a*`, `scripts/verify_step3b*`, `scripts/verify_step3c*`, `scripts/verify_step4*`, and `scripts/verify_step5_euclidean_n4_awi.py`;
- `tests/test_step5*.py` and tests whose expected values are fixtures from the blocked AWI/supergraph layer;
- `references/vendor/chatgpt/**` and local proposal/reference packets derived from earlier LLM calculations.

Other source snapshots, including Srednicki, Superspace, holomorphic-anomaly papers, and Weinberg sections outside the protected boundary, remain source archives only. They are not declared false, but they are outside the current trust boundary and must not be used to revive a blocked derived result.

## Pollution diagnoses

### 1. Convention and notation pollution

The legacy layer mixes exact Weinberg notation with project dictionaries, Srednicki/Wess–Bagger translations, Euclidean continuations, custom field rescalings, and later repair conventions. A dictionary or a passing symbol audit does not prove that signs, dotted-index order, measures, propagator normalization, or source normalization were transported correctly. Derived formulas that depend on those translations are blocked.

### 2. Incomplete graph and Wick closure

The Step-5 catalogue and its descendants reproduce selected triangle families while contact, ghost, seagull, operator-intrinsic, Hermitian-conjugate, regulator-generated, and counterterm sectors were pending or represented by coverage rows. A graph census is not a compute-or-zero proof. Full component Wick contractions and the complete Slavnov–Taylor/BV closure were not established.

### 3. Target-shaped and regulator-shaped inference

Several audits freeze desired local structures, normalization bridges, HT kernels, DRED evanescent remnants, or expected coefficients before an independent full calculation. This makes agreement with a target or a coded fixture circular. Endpoint/contact terms, total-versus-edgewise Schwinger-time prescriptions, operator mixing, and finite local counterterms were not controlled by one regulated BV construction.

### 4. BRST vocabulary without BV quantum control

A BRST action, ghost list, or Ward identity alone does not supply a regulated BV action, antibracket, BV Laplacian, measure term, quantum master equation, or renormalized composite-operator map. Consequently the old non-BV supergraph/AWI results cannot be promoted by citing BRST labels.

### 5. Tests and gates validate artifacts, not physics

The scripts and tests check internal identities, manifests, hashes, graph IDs, serialization, and agreement with stored expected values. They do not independently derive the physics. `PASS`, `81/81`, a rendered atlas, or a successful workflow therefore cannot remove this block.

### 6. Transcript and proposal contamination

ChatGPT/GPT Pro transcripts, proposals, work logs, Notion mirrors, and generated papers repeatedly restate the same unclosed assumptions. Repetition across artifacts is not independent corroboration and can re-inject the same error into later work.

## Use rule

When a protected BV file depends on a blocked non-BV formula, that dependency must be rederived inside the current Weinberg 26/27 plus Notion 30.4 notation and a regulated BV framework. Do not cite the blocked file as a lemma, benchmark, normalization target, or cross-check.
