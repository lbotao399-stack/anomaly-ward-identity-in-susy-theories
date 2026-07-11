# AWI Proof Repository

## Authority

- Read `AUTHORITY.md` first.
- Only files reachable from `origin/main` with a successful `verify` workflow are authoritative.
- Direct pushes after the bootstrap commits are forbidden; use one proof-obligation branch and review.
- An unpushed local commit is a proposal.
- Do not read outside this repository except runtime executables required by repository code.
- Do not read Notion, chat history, Codex memory, attachments, Desktop notes, other repositories,
  or web pages as calculation input, except for the exact external handles of a user-authorized
  REFERENCE_IMPORT task under the scoped exception in AUTHORITY.md.
- During that import task, vendor raw source snapshots and metadata only.  Mathematical comparison
  begins in a later CONTRACT_CHANGE after the import reaches verified origin/main.
- Do not create a `legacy/` directory. Legacy material remains outside the authoritative checkout.

## Scope

- Execute exactly one task from `tasks/CURRENT.yaml`.
- Read only that task's `allowed_inputs`.
- Missing input must produce `BLOCKED_<REASON>`; never infer or import it.
- Modify `contracts/` only for a task whose type is `CONTRACT_CHANGE` or `AUTHORITY_REPAIR`.

## Channel isolation

- A channel may read shared `contracts/` and its own directory only.
- A channel must not read or import another channel.
- Cross-channel comparison occurs only at final canonical `result.json` level.

## Mathematical rigor

- Every symbol and index space must resolve through a contract.
- Keep all spinor indices and every raising/lowering operation explicit.
- Never use an untyped momentum square.
- Never quote a propagator, vertex, sign, graph multiplicity, or loop coefficient.
- Derive vertices by ordered functional differentiation from the locked action.
- Emit every Wick pairing, fermion permutation, color ordering, and symmetry factor.
- Every symbolic rewrite must emit its input, rule, conditions, sign, output, and invariant checks.

## State machine

`SPECIFIED -> FROZEN -> RULES_DERIVED -> ENUMERATED -> EVALUATED -> CUT_COMPLETE -> RENORMALIZED -> WARD_CLOSED -> COHOMOLOGY_PROJECTED -> ACCEPTED`

No stage may be skipped.

## Notion publishing

- Notion is write-only from this repository.
- Build the payload from the committed source named in `mirror/page_map.yaml`.
- Never fetch Notion content before or after publishing.
- Record Git commit and source SHA-256 in the rendered mirror banner.
