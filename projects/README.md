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

## Status of the split

- **Phase 1 (done / in progress):** scaffold + `readable/` populated from the accepted
  contracts. Additive; the legacy top-level tree (`contracts/`, `audits/`, `scripts/`,
  `tests/`, `generated/`) is untouched and still the CI authority.
- **Phase 2 (next):** migrate the machine tree under each project's `machine/`, updating hash
  manifests and test paths per project so `verify` stays green.
- **Phase 3:** retire the legacy top-level tree once every path has moved.
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
