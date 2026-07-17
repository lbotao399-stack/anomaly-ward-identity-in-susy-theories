# Repository status snapshot — 2026-07-17

One-glance state of the AWI repository. Regenerate by re-reading
`ledger/proof_obligations.json` and the directory counts.

## Obligations: 33 ACCEPTED / 2 open (35 total)

| Step | Contract | State |
|---|---|---|
| 01 | supersymmetry commutator | ACCEPTED |
| 02a | flat superspace | ACCEPTED |
| 02b / 02c | superconformal superspace / covariance | ACCEPTED |
| 03a–03d | gauge–chiral action, components, vector rep, BV–BRST path integral | ACCEPTED |
| 03e | N=1 Feynman rules | **open** — `BLOCKED_STEP3D_LC_VECTOR_CYCLE` (Lorentzian only) |
| 04 / 04a / 04b / 04c | extended-SYM notation, N=1 / N=2 / N=4 | ACCEPTED |
| dict | Weinberg–Srednicki–Project, extended-SYM | ACCEPTED |
| 05a | component BV–BRST supergraph grammar | ACCEPTED |
| **05** | **Euclidean N=4 one-loop AWI settlement (81 channels, HT match)** | **ACCEPTED** |
| 06 | covariant completion (2-loop / n-gon) | **open** — current; `BLOCKED_PHASE0_CHAIN_MAP_ACTION_NOT_LOCKED` (25 PASS / 56 BLOCKED) |

Plus reference-imports and Notion mirrors, all ACCEPTED.

## Current obligation

`tasks/CURRENT.yaml` → `CONTRACT-STEP-06-COVARIANT-COMPLETION-001` (SPECIFIED). Work order:
`tasks/instructions/2026-07-16-covariant-completion-proof.md`.

## What is proven vs. open (physics)

**Proven / accepted:** the one-loop anomaly coefficient for all 81 ordered letter pairs; the
cutting-failure mechanism ($\mu_\ell^2$, master $1/32\pi^2$, $-2\epsilon$ trace); the 29/52
selection census; the full holomorphic-derivative tower; exact match to Budzik–Kulp after the
factor-2 correction; the generalized-Konishi $(B,C)$ channel with its bottom projection.

**Open:** graph-census exhaustiveness as a theorem (the covariant completion, Step 6);
target-blind typed absence rows for the ghost/NK sector and four specific Wick routings; the
two-loop $Q_2$ (required by $Q_1^2+\{Q_0,Q_2\}=0$); the Lorentzian sector.

## Scale (what makes it look like a mess, and why)

- `contracts/` 17 files ≈ 24k lines of hand-written derivation — the real content.
- `audits/` 201, `scripts/` 141, `tests/` 88 — exact-verification scaffolding (the `verify`
  gate re-runs it). Ratio of scaffolding to derivation is high by design; the Derivation-first
  law (`AGENTS.md`, 2026-07-16) now caps it going forward.
- `proposals/` 76, of which **67 are legacy GPT-Pro per-gate files** — the single largest
  clutter source. Consolidation is queued (`workflow-slim-obligation-spec`).

## Notion

17 pages mirrored under the root page `39e80ed3…` (write-only), including the core-theory
paper, the Step-5 settlement, and the per-pair bi-letter report.
