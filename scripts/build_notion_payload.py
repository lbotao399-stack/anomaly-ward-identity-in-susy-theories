from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "lbotao399-stack/anomaly-ward-identity-in-susy-theories"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()

    source = (ROOT / args.source).resolve()
    source.relative_to(ROOT)
    body = source.read_text(encoding="utf-8").rstrip() + "\n"
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()

    print("> **Git authority — output-only Notion mirror**")
    print(">")
    print(f"> Repository: [{REPOSITORY}](https://github.com/{REPOSITORY})")
    print(f"> Commit: [`{args.commit}`](https://github.com/{REPOSITORY}/commit/{args.commit})")
    print(f"> Source: `{args.source}`")
    print(f"> SHA-256: `{digest}`")
    print("> Manual Notion edits are non-authoritative. Notion content is never read back as project input.")
    print()
    print(body, end="")


if __name__ == "__main__":
    main()
