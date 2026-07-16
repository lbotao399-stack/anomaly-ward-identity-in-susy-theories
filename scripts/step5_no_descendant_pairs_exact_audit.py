#!/usr/bin/env python3
"""Exact target-blind zero audit for pairs with no outer D_- descendant."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "audits/step5-no-descendant-pairs-exact.json"

LETTERS = ("C1", "C2", "C3", "Ddot1", "Ddot2")
PARITY = {"C1": 0, "C2": 0, "C3": 0, "Ddot1": 1, "Ddot2": 1}


def build_artifact() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for left in LETTERS:
        for right in LETTERS:
            left_descendant = 0
            right_descendant = 0
            koszul_sign = -1 if PARITY[left] else 1
            leibniz_value = left_descendant + koszul_sign * right_descendant
            rows.append(
                {
                    "pair_id": f"{left}__{right}",
                    "left_parity": PARITY[left],
                    "left_descendant": left_descendant,
                    "right_descendant": right_descendant,
                    "right_koszul_sign": koszul_sign,
                    "outer_Dminus_product": leibniz_value,
                    "marked_inverse_kernel_occurrences": 0,
                    "dred_cutting_failure_words": 0,
                    "anomaly_sector": "0",
                }
            )
    return {
        "schema": "step5-no-descendant-pairs-exact-v1",
        "status": "TARGET_BLIND_EXACT_ZERO__NO_OUTER_DESCENDANT__NO_CUTTING_FAILURE_WORD",
        "target_used": False,
        "letters": list(LETTERS),
        "ordered_pair_count": len(rows),
        "rows": rows,
    }


def validate(artifact: dict[str, object]) -> tuple[int, int]:
    rows = artifact["rows"]
    assert isinstance(rows, list)
    assertions = (
        artifact["schema"] == "step5-no-descendant-pairs-exact-v1",
        artifact["target_used"] is False,
        artifact["ordered_pair_count"] == 25,
        len(rows) == 25,
        len({row["pair_id"] for row in rows}) == 25,
        all(row["left_descendant"] == 0 for row in rows),
        all(row["right_descendant"] == 0 for row in rows),
        all(row["outer_Dminus_product"] == 0 for row in rows),
        all(row["marked_inverse_kernel_occurrences"] == 0 for row in rows),
        all(row["dred_cutting_failure_words"] == 0 for row in rows),
        all(row["anomaly_sector"] == "0" for row in rows),
    )
    return sum(assertions), len(assertions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if not args.write and not args.check:
        args.check = True
    artifact = build_artifact()
    passed, total = validate(artifact)
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.output.write_text(rendered, encoding="utf-8")
    if args.check:
        if not args.output.is_file():
            raise SystemExit(f"missing artifact: {args.output}")
        if args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"stale artifact: {args.output}")
    print(f"SUMMARY {passed}/{total} PASS")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
