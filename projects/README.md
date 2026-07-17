# Projects — monorepo folder-split

New working layout (owner-authorized 2026-07-17). Five projects sharing one notation spine;
each cleanly separates a human-readable paper from isolated machine verification.

```
projects/
  notation/            0. shared formalism spine — every project imports it, none redefines it
  superspace/          1. superspace supergraph Feynman diagrams   (the completed project)
  component/           2. component-field Feynman diagrams
  heat-kernel/         3. non-perturbative heat-kernel / full-BV
  holomorphic-twist/   4. is the holomorphic twist legitimate (quantum legality)
```

Inside every project:

- **`readable/`** — human-only, paper-format markdown. Pure theory and calculation: action →
  Feynman rules → worked example → rendered diagram → Wick → amplitude → D-algebra →
  anomaly sector → loop integral → result → comparison. No machinery, no review gates.
- **`machine/`** — not for human reading. Verifiers, audits, generated IR, tests. Isolated;
  its only contract with `readable/` is "this check corresponds to equation (X.n)".

**Machine layout (option C, chosen 2026-07-17):** the machine tree physically stays at the
repository root (`scripts/`, `audits/`, `tests/`, `generated/`) so the single CI `verify`
gate runs it as one unit; each project's `machine/INDEX.md` records which root files belong
to it. Reading isolation is already complete (you read `readable/`, never the machine tree).
A future true repo-split (`git filter-repo`) would relocate each cluster physically then.

## Status of the split

- **Phase 1 (done / in progress):** scaffold + `readable/` populated from the accepted
  contracts. Additive; the legacy top-level tree (`contracts/`, `audits/`, `scripts/`,
  `tests/`, `generated/`) is untouched and still the CI authority.
- **Phase 2 (done — option C):** machine files grouped per project via `machine/INDEX.md`
  without physically moving them (near-zero risk; reading isolation already complete). Only
  `notation` and `superspace` have large machine clusters on `main`; `heat-kernel` and
  `holomorphic-twist` have a couple of files each; `component` has none dedicated yet.
- **Phase 3 (optional):** physically relocate a cluster under its `machine/` only if/when a
  true repo-split is scheduled — done together with the manifest/test path rewrite.
- **Phase 4 (optional):** `git filter-repo --path projects/<p>` to spin any project into its
  own repository, carrying history, with `notation/` vendored or submoduled.

## Legacy → project map

| Legacy (accepted on `main`) | Project |
|---|---|
| `contracts/foundations/step-01…04c`, `05a`; `contracts/dictionaries/*` | `notation/` |
| `contracts/foundations/step-05`, `step-06`; `paper/awi-n4-one-loop.md` | `superspace/` |
| `contracts/foundations/step-03b`; component actions in `05a` | `component/` |
| `proposals/heat-kernel-*`; the Full-BV heat-kernel line | `heat-kernel/` |
| `step-04d`, `step-04e`; HT reference import; `references/vendor/arxiv/2512.07771` | `holomorphic-twist/` |
