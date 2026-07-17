# Repository split architecture — 2026-07-17

Status: `NON_AUTHORITY_PROPOSAL`. Owner-requested: split the monolith into related-but-
independent projects, with a shared notation core, and — in every project — isolate
machine-verification from a human-readable paper-format derivation.

## Target: five projects, human/machine split inside each

```
0  notation/              (shared formalism: the spine everything imports)
1  superspace/            (superspace supergraph Feynman diagrams)   ← the done project
2  component/             (component-field Feynman diagrams)
3  heat-kernel/           (non-perturbative heat-kernel / full-BV)
4  holomorphic-twist/     (is the HT even legitimate — quantum legality)
```

Inside **every** project:

```
<project>/
    readable/     human-only, paper-format markdown. Pure theory + calculation.
                  The 11-point style: action → Feynman rules → worked example →
                  rendered triangle → Wick → amplitude → D-algebra → anomaly sector →
                  loop integral → result → HT comparison. No machinery, no gates.
    machine/      NOT for human reading. Verifiers, audits, generated IR, tests.
                  Isolated; its only contract with readable/ is "this checks eq. (X.n)".
```

**0. notation/** holds the shared spine — the complete buildup the user named: Lorentzian
and Euclidean signatures; Weyl and Majorana (the Weinberg/Srednicki dictionary); covariant
derivative definitions; the θ-expansion (component) form of superfields; vector and chiral
representations; through the BV–BRST formalism. Projects 1–4 import it, never redefine it.

## Mapping the current repo into the buckets

| Bucket | Current material (accepted on `main`) |
|---|---|
| **0 notation** | `step-01, 02a, 02b, 02c, 03a, 03c, 03d`, `04, 04a, 04b, 04c`, `05a` (BV–BRST + Feynman-rule grammar), `contracts/dictionaries/*` (Weinberg–Srednicki–Majorana) |
| **1 superspace** | `step-05` (the settlement), `step-06` (covariant completion), `paper/awi-n4-one-loop.md`, the supergraph parts of `05a`, the bi-letter reports |
| **2 component** | `step-03b` (component reconstruction), the component actions in `05a`, the audited Claude component/BRST/Noether routes |
| **3 heat-kernel** | `proposals/heat-kernel-n4-one-loop-memo`, the #71-admitted heat-kernel lemma, the "Full-BV Heat Kernel" line |
| **4 holomorphic-twist** | `step-04d` (classical HT), `step-04e` (quantum HT), the N=1 HT BV program (closed branches), `references/vendor/arxiv/2512.07771`, the HT dictionary + reference import |

Every one of the five already has real accepted material here — the split is a
reorganization, not new derivation.

## The decision: separate repos vs monorepo folders

**Recommendation: monorepo folder-split now, designed so a true multi-repo split is a later
one-command step.**

| | Separate GitHub repos | Monorepo folder-split (recommended) |
|---|---|---|
| Independence | maximal | high (each top folder self-contained) |
| Shared notation | needs submodule (painful) / package / copy-drift | just a shared folder — zero friction |
| CI | one gate per repo (5 gates) | one gate, path-filtered per project |
| Provenance web | must be rebuilt 5× (hash manifests, ledgers) | preserved; migrate paths once |
| Cost / risk now | very high, partly irreversible | moderate, git-reversible |
| Later escape hatch | — | `git filter-repo --path <project>` splits any folder into its own repo cleanly |

The heavy machinery you have suffered from is exactly what multiplies by 5 in the separate-
repo option. Folder-split gets the independence and the human/machine isolation immediately,
keeps the shared notation frictionless, and leaves the door open to spin any project into its
own repo later without redoing the work.

## Phased migration (each phase git-reversible, CI stays green)

1. **Scaffold + readable-first (highest value, lowest risk).** Create the five folders each
   with `readable/` and `machine/`. Populate `readable/` from the accepted contracts as
   paper-format markdown (project 1's is essentially `paper/awi-n4-one-loop.md` + the
   bi-letter reports; project 0's is a notation paper distilled from the step contracts).
   Additive — nothing deleted, CI untouched.
2. **Move machine/.** Relocate `scripts/ audits/ tests/ generated/` under each project's
   `machine/`, updating the hash manifests and test paths in one pass. This is the delicate
   step; done per project so CI is re-greened incrementally.
3. **Retire the old top-level tree** once every path is migrated and `verify` is green on the
   new layout.
4. **(Optional, later)** `git filter-repo` any project folder into its own repo, carrying its
   history, with `notation/` vendored or submoduled.

## What the user gets

- Five independent project spaces, each opening to a clean paper you can read start to finish.
- Machine verification quarantined under `machine/`, never in your way.
- A shared notation spine no project can drift from.
- The freedom to later cut any project loose into its own repo — or not.
