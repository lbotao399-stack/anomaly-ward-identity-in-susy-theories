# Authority Contract

Effective: 2026-07-10.

## Sole authority

Only Git objects reachable from the default branch `origin/main` of
`lbotao399-stack/anomaly-ward-identity-in-susy-theories` **and** carrying a successful `verify`
workflow result are admissible computational evidence.

Local uncommitted changes, unpushed commits, branches, pull requests, chats, memories, attachments,
Notion pages, and other repositories are proposals or transport surfaces. They cannot settle a
formula, sign, normalization, coefficient, graph census, or proof status.

## Allowed inputs

A calculation run may read only:

1. this repository at a recorded commit;
2. the single task named by `tasks/CURRENT.yaml`;
3. files explicitly allowed by that task;
4. runtime executables needed to run repository code.

An external reference becomes admissible only through a `REFERENCE_IMPORT` task that vendors the
required material into this repository, records its cryptographic hash, and classifies every imported
claim. A URL alone is never an authority.

## Notion boundary

Notion is an output-only human-readable mirror.

- Git to Notion publishing is allowed.
- Notion search, fetch, export, or copy-back is forbidden as a project input.
- Manual Notion edits are non-authoritative and may be overwritten.
- Publishing receipts and target page identifiers are transport metadata, not mathematical evidence.

### User-authorized Notion reference-import exception

A user may explicitly authorize named Notion book pages as external references for one
REFERENCE_IMPORT task.  The exception is valid only when all of the following hold:

1. tasks/CURRENT.yaml records the exact search queries and forbids every unrelated Notion page;
2. search is used only to identify the named book roots and their descendants;
3. every fetched page is stored verbatim in references/vendor/ with page id, URL, title, and
   SHA-256 in references/manifest.yaml;
4. the imported snapshot is a reference, not a contract: it cannot settle a project sign or
   normalization until a later reviewed CONTRACT_CHANGE derives the translation;
5. after the import task is accepted, the default output-only Notion boundary resumes.

No attachment, draft dictionary, or fetched Notion page is authoritative before its vendored
snapshot and hash reach origin/main with a successful verify workflow.

## Bootstrap exception

The Step-1 supersymmetry-commutator foundation is admitted once from the exact payload authored in the
immediately preceding construction session. No other Notion page, descendant, legacy note, or local
repository is imported. After the bootstrap commit, this exception closes permanently.

## Legacy boundary

No legacy file or Git history is imported into this repository. Historical AWI remotes may be archived
for provenance, but calculation agents must not clone, search, or read them.

## Enforcement limitation

Server-side branch protection for this private repository is unavailable on the current GitHub plan.
The exact infrastructure state is `BLOCKED_GITHUB_PLAN_BRANCH_PROTECTION`. Until the account plan
changes, direct pushes are forbidden by project law, and the successful `verify` workflow is the
mandatory authority gate.
