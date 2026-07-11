from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "references" / "manifest.yaml"


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for entry in data["entries"]:
        source = (ROOT / entry["path"]).resolve()
        source.relative_to(ROOT)
        entry["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    MANIFEST.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
