# Follow-up obligation spec: workflow slimming (2026-07-16, owner-approved)

Status: `NON_AUTHORITY_PROPOSAL` — specification for the next infrastructure obligation
after `MIRROR-STEP-05-NOTION-001`. One reviewed PR, sized within the Derivation-first law.

Owner approval: 2026-07-16 session ("其余建议我都允许"). Items 1, 3, 6 of the optimization
list were executed immediately (paper layer, check budget, terminology law); this spec
carries the remaining approved items.

## 1. Policy-test slimming (law protects boundaries, not content shape)

Reduce `tests/test_repository_policy.py` to the provenance invariants: contract/reference
hash integrity, Notion write-only receipts, reference-import isolation, single-CURRENT
registration, no-legacy/no-symlink, UTF-8 surface. Remove the content-shape pins
(acceptance-clause counts, verbatim blocker lists, per-step formula-surface token counts) —
those duties now live in the Derivation-first law and human review. Every deleted check must
be listed in the PR body with its replacement (law clause or review step).

## 2. CI fast/slow split

Two parallel jobs in `verify.yml`: `policy-fast` (hashes, structure, registration, cheap
identities; target < 10 minutes) and `exact-replays` (the heavy sympy audits). Both block
merges (the authority gate is unchanged); the split exists for early failure signal. Requires
the test reorganization of item 1 (heavy replays currently live inside
`test_repository_policy.py`).

## 3. Euclidean-only foundations going forward

New contracts derive the Euclidean case only. The Lorentzian sector (including the
quarantined `BLOCKED_STEP3D_LC_VECTOR_CYCLE` and PR #42) becomes a named separate program,
reopened only by explicit owner instruction. Existing dual-signature contracts are left
untouched (no retroactive rewriting).

## 4. Channel-system removal

Delete `channels/{ec,es,lc,ls}/` and the "Channel isolation" law section. The one
cross-check of value (component vs superfield on a seed channel) becomes a labeled memo
section when needed. Remove `test_channel_sources_do_not_cross_read`.

## 5. Artifact-honesty repairs (conditional on the resumed census review)

If the resumed adversarial review confirms the `physical-graph-ir.json` template-stamping
allegation or any missing typed rows (see
`proposals/step5-census-review-addendum-2026-07-16.md`), repair the artifact or add the
typed ghost/absence rows in the same PR. Also remove or fix the obsolete equality-pinned
`scripts/step5_ht_roundtrip_audit.py` (not test-wired; carries a stale
`authority.base_commit` equality check).

## 6. Prose pass on the settlement contract

One editing pass over `contracts/foundations/step-05-euclidean-n4-awi-one-loop.md` applying
the terminology law (replace or define: occurrence-resolved, target-blind, raw-port functor
table, etc.). No mathematical content changes; hash update in the manifest.
