# machine/ — isolated verification (not for human reading)

Holds the exact verifiers, audits, generated IR, and tests for the **component** project. Populated
in Phase 2 by relocating the relevant parts of the legacy `scripts/`, `audits/`, `tests/`,
`generated/` trees and repointing the hash manifests. The only contract with `../readable/`
is that each machine check names the equation it verifies. Do not read this tree for the
physics; read `../readable/`.
