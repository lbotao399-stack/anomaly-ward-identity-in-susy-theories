# One-way Notion Mirror

Direction is strictly Git to Notion.

1. Resolve the committed source through `page_map.yaml`.
2. For a contract source, verify its SHA-256 against `contracts/manifest.yaml`. For the standing
   paper source `paper/awi-n4-one-loop.md`, verify the direct committed SHA-256 and keep its cited
   contracts as the legal mathematical layer.
3. Generate the payload with `scripts/build_notion_payload.py`.
4. Replace the mapped Notion page through a write operation.
5. Do not search, fetch, export, or read back Notion content.
6. Keep the write receipt as transport evidence; Git remains the only content authority.
