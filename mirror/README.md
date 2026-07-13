# One-way Notion Mirror

Direction is strictly Git to Notion.

1. Resolve the committed source through `page_map.yaml`.
2. Verify its SHA-256 against `contracts/manifest.yaml`.
3. Generate the payload with `scripts/build_notion_payload.py`.
4. Replace the mapped Notion page through a write operation.
5. Do not search, fetch, export, or read back Notion content.
6. Keep the write receipt as transport evidence; Git remains the only content authority.
7. For unfinished work, publish only committed machine-verified sections and mark the page
   `UNMERGED_PROPOSAL` when the source is not accepted `origin/main`.
8. List every open proof obligation and every `UNCOMPUTED` coefficient on the same partial page.
