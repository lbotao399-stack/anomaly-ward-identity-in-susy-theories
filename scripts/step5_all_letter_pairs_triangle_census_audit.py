#!/usr/bin/env python3
"""Fail-closed audit for the complete Step-5 ordered letter-pair census.

This checker does not compute a Feynman coefficient and does not read the
holomorphic-twist target to repair a Project result.  It checks only that the
human-readable census contains the full Cartesian product of the nine locked
physical letters, the graded outer-D_- placements, the parent triangle
skeleton required by the typed primitive ports, the conditional external
target tensor label, and an honest evidence status.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUDIT = ROOT / "audits/step5-all-letter-pairs-triangle-census.md"
PROJECT_CLASSIFICATION_LEDGER = ROOT / "generated/step5/project-result-ledger.json"
HT_CLASSIFICATION_LEDGER = ROOT / "generated/step5/ht_ordered_pair_targets.json"

LETTERS = ("A", "B1", "B2", "B3", "C1", "C2", "C3", "Ddot1", "Ddot2")
ACTIVE_DESCENDANT = frozenset(("A", "B1", "B2", "B3"))
PARITY = {
    "A": 0,
    "B1": 1,
    "B2": 1,
    "B3": 1,
    "C1": 0,
    "C2": 0,
    "C3": 0,
    "Ddot1": 1,
    "Ddot2": 1,
}


def family(letter: str) -> str:
    return letter[0]


def component(letter: str) -> int:
    match = re.search(r"(\d+)$", letter)
    if not match:
        raise ValueError(letter)
    return int(match.group(1))


def epsilon3(i: int, j: int, k: int) -> int:
    if {i, j, k} != {1, 2, 3}:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


def marked_placements(left: str, right: str) -> str:
    marks: list[str] = []
    if left in ACTIVE_DESCENDANT:
        marks.append(f"L:{left}")
    if right in ACTIVE_DESCENDANT:
        sign = "+" if PARITY[left] == 0 else "-"
        marks.append(f"R:{sign}{right}")
    return ";".join(marks) if marks else "NONE"


def target_label(left: str, right: str) -> str:
    lf, rf = family(left), family(right)
    if left == "A" and right == "A":
        return "Z"
    if (lf, rf) in {("A", "B"), ("B", "A")}:
        b = component(right if rf == "B" else left)
        return f"Y{b}"
    if (lf, rf) in {("A", "C"), ("C", "A")}:
        c = component(right if rf == "C" else left)
        return f"X{c}"
    if lf == "A" and rf == "D":
        return f"JL{component(right)}"
    if lf == "D" and rf == "A":
        return f"JR{component(left)}"
    if lf == "B" and rf == "B":
        i, j = component(left), component(right)
        if i == j:
            return "0eps"
        k = 6 - i - j
        sign = "+" if epsilon3(i, j, k) == 1 else "-"
        return f"H{sign}{k}"
    if (lf, rf) in {("B", "C"), ("C", "B")}:
        b = component(left if lf == "B" else right)
        c = component(right if rf == "C" else left)
        return "U" if b == c else "0delta"
    return "0port"


def topology(left: str, right: str) -> str:
    lf, rf = family(left), family(right)
    if left == "A" and right == "A":
        return "TGG+TMM[1,2,3]"
    if (lf, rf) in {("A", "B"), ("B", "A")}:
        return "TGM+TMM+TMH"
    if (lf, rf) in {("A", "C"), ("C", "A")}:
        return "TGM+TMM"
    if (lf, rf) in {("A", "D"), ("D", "A")}:
        return "TGG"
    if lf == "B" and rf == "B":
        return "TMH" if component(left) != component(right) else "TMH[epsilon=0]"
    if (lf, rf) in {("B", "C"), ("C", "B")}:
        b = component(left if lf == "B" else right)
        c = component(right if rf == "C" else left)
        return "TMM" if b == c else "TMM[delta=0]"
    return "T0[port]"


def evidence(left: str, right: str, target: str) -> str:
    if left == "A" and right == "A":
        return "E_AA"
    if left == "A" and right == "B1":
        return "E_AB1"
    if left == "B1" and right == "A":
        return "E_AB1R"
    if not target.startswith("0"):
        return "E_NZ"
    if target in {"0eps", "0delta"}:
        return "E_ZF"
    if left not in ACTIVE_DESCENDANT and right not in ACTIVE_DESCENDANT:
        return "E_ZD"
    return "E_ZP"


@dataclass(frozen=True)
class Row:
    ordinal: int
    left: str
    right: str
    family_pair: str
    marks: str
    topology: str
    target: str
    evidence: str


def expected_rows() -> list[Row]:
    rows: list[Row] = []
    ordinal = 0
    for left in LETTERS:
        for right in LETTERS:
            ordinal += 1
            target = target_label(left, right)
            rows.append(
                Row(
                    ordinal=ordinal,
                    left=left,
                    right=right,
                    family_pair=f"{family(left)}>{family(right)}",
                    marks=marked_placements(left, right),
                    topology=topology(left, right),
                    target=target,
                    evidence=evidence(left, right, target),
                )
            )
    return rows


ROW_RE = re.compile(
    r"^\|\s*(?P<ordinal>\d{3})\s*"
    r"\|\s*`(?P<left>[^`]+)>(?P<right>[^`]+)`\s*"
    r"\|\s*`(?P<family>[^`]+)`\s*"
    r"\|\s*`(?P<marks>[^`]+)`\s*"
    r"\|\s*`(?P<topology>[^`]+)`\s*"
    r"\|\s*`(?P<target>[^`]+)`\s*"
    r"\|\s*`(?P<evidence>[^`]+)`\s*\|$"
)


def parse_rows(text: str) -> list[Row]:
    rows: list[Row] = []
    for line in text.splitlines():
        match = ROW_RE.match(line)
        if not match:
            continue
        fields = match.groupdict()
        rows.append(
            Row(
                ordinal=int(fields["ordinal"]),
                left=fields["left"],
                right=fields["right"],
                family_pair=fields["family"],
                marks=fields["marks"],
                topology=fields["topology"],
                target=fields["target"],
                evidence=fields["evidence"],
            )
        )
    return rows


REQUIRED_FRAGMENTS = (
    "Status: `BLOCKED_RAW_ALL_PAIR_TRIANGLE_AND_DESCENDANT_ORBITS`",
    "N_{\\mathrm{ordered\\ pairs}}=81=29+52",
    "N_{D_-\\text{-marked\\ occurrences}}=72",
    "T_{GG}:=(I_{XY},G,G)",
    "T_{GM}:=(I_{XY},G,M_r)",
    "T_{MM}:=(I_{XY},M_r,M_s)",
    "T_{MH}:=(I_{XY},M_r,H_{\\widetilde\\Phi^3})",
    "T_{MH}^{(r)}:=(I_{XY},M_r,H_{\\widetilde\\Phi^3})",
    "E_AA",
    "E_AB1",
    "E_AB1R",
    "E_NZ",
    "E_ZF",
    "E_ZD",
    "E_ZP",
    "-\\frac{2\\lambda_1}{3}",
    "+\\frac{2\\lambda_1}{3}",
    "BLOCKED_AB1_G1_EDGE_TAGGED_SD_CONTACT_PAIRING",
    "BLOCKED_REFERENCE_INTERNAL_NORMALIZATION",
    "BLOCKED_RAW_GRAPH_Q_EQUIVARIANT_LIFT",
    "HT-N4-ONE-LOOP-COMPONENT-PAIR-CANDIDATE",
)

FORBIDDEN_FRAGMENTS = (
    "BLOCKED_AB1_OUTER_NABLA_MINUS_DESCENDANT",
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def classification_crosscheck(rows: list[Row]) -> tuple[int, int]:
    """Compare pair ids and exact-zero flags only; never inspect coefficients."""

    expected = {
        (row.left, row.right): row.target.startswith("0")
        for row in rows
    }

    if not PROJECT_CLASSIFICATION_LEDGER.is_file():
        fail(f"missing Project classification ledger: {PROJECT_CLASSIFICATION_LEDGER}")
    project_payload = json.loads(PROJECT_CLASSIFICATION_LEDGER.read_text(encoding="utf-8"))
    if project_payload.get("external_target_used") is not False:
        fail("Project classification ledger is not target-blind")
    project = {
        (row["left"], row["right"]): bool(row["exact_zero"])
        for row in project_payload.get("pairs", [])
    }
    if project != expected:
        fail("Project exact-zero classification differs from census")

    if not HT_CLASSIFICATION_LEDGER.is_file():
        fail(f"missing HT classification ledger: {HT_CLASSIFICATION_LEDGER}")
    ht_payload = json.loads(HT_CLASSIFICATION_LEDGER.read_text(encoding="utf-8"))
    if ht_payload.get("authority_role") != "EXTERNAL_TARGET_ONLY":
        fail("HT classification ledger lost EXTERNAL_TARGET_ONLY role")
    ht_to_project = {
        "B": "A",
        "P1": "B1",
        "P2": "B2",
        "P3": "B3",
        "G1": "C1",
        "G2": "C2",
        "G3": "C3",
        "Hdot1": "Ddot1",
        "Hdot2": "Ddot2",
    }
    ht = {
        (ht_to_project[row["left"]], ht_to_project[row["right"]]): bool(row["exact_zero"])
        for row in ht_payload.get("pairs", [])
    }
    if ht != expected:
        fail("HT exact-zero classification differs from census")

    return len(project), len(ht)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    args = parser.parse_args()

    if not args.audit.is_file():
        fail(f"missing audit file: {args.audit}")
    text = args.audit.read_text(encoding="utf-8")
    controls = [
        (index, ord(character))
        for index, character in enumerate(text)
        if ord(character) < 32 and character not in {"\n", "\t"}
    ]
    if controls:
        fail(f"control characters present: {controls[:8]}")
    forbidden_shortcuts = ("\\sim", "\\approx", "After substitution", "after substitution")
    for shortcut in forbidden_shortcuts:
        if shortcut in text:
            fail(f"forbidden shortcut present: {shortcut}")
    for fragment in REQUIRED_FRAGMENTS:
        if fragment not in text:
            fail(f"missing required fragment: {fragment}")
    for fragment in FORBIDDEN_FRAGMENTS:
        if fragment in text:
            fail(f"obsolete fragment present: {fragment}")

    expected = expected_rows()
    actual = parse_rows(text)
    if len(actual) != 81:
        fail(f"parsed ordered rows={len(actual)}, expected 81")
    if actual != expected:
        for index, (got, want) in enumerate(zip(actual, expected, strict=False), start=1):
            if got != want:
                fail(f"row {index} mismatch\nactual={got}\nexpected={want}")
        fail("row ledger differs from expected Cartesian census")

    pair_ids = {(row.left, row.right) for row in actual}
    if len(pair_ids) != 81:
        fail(f"unique ordered pair ids={len(pair_ids)}, expected 81")

    nonzero = [row for row in actual if not row.target.startswith("0")]
    zero = [row for row in actual if row.target.startswith("0")]
    if (len(nonzero), len(zero)) != (29, 52):
        fail(f"classification count={(len(nonzero), len(zero))}, expected (29, 52)")

    marked_occurrences = sum(
        int(row.left in ACTIVE_DESCENDANT) + int(row.right in ACTIVE_DESCENDANT)
        for row in actual
    )
    marked_pairs = sum(row.marks != "NONE" for row in actual)
    if (marked_occurrences, marked_pairs) != (72, 56):
        fail(
            f"marked census={(marked_occurrences, marked_pairs)}, expected (72 occurrences, 56 pairs)"
        )

    expected_family_counts = {
        "A>A": (1, 0),
        "A>B": (3, 0),
        "A>C": (3, 0),
        "A>D": (2, 0),
        "B>A": (3, 0),
        "B>B": (6, 3),
        "B>C": (3, 6),
        "B>D": (0, 6),
        "C>A": (3, 0),
        "C>B": (3, 6),
        "C>C": (0, 9),
        "C>D": (0, 6),
        "D>A": (2, 0),
        "D>B": (0, 6),
        "D>C": (0, 6),
        "D>D": (0, 4),
    }
    actual_family_counts: dict[str, tuple[int, int]] = {}
    for family_pair in expected_family_counts:
        bucket = [row for row in actual if row.family_pair == family_pair]
        actual_family_counts[family_pair] = (
            sum(not row.target.startswith("0") for row in bucket),
            sum(row.target.startswith("0") for row in bucket),
        )
    if actual_family_counts != expected_family_counts:
        fail(f"family counts={actual_family_counts}, expected={expected_family_counts}")

    topology_counts = Counter(row.topology for row in actual)
    expected_topology_counts = Counter(
        {
            "TGG+TMM[1,2,3]": 1,
            "TGM+TMM+TMH": 6,
            "TGM+TMM": 6,
            "TGG": 4,
            "TMH": 6,
            "TMH[epsilon=0]": 3,
            "TMM": 6,
            "TMM[delta=0]": 12,
            "T0[port]": 37,
        }
    )
    if topology_counts != expected_topology_counts:
        fail(f"topology counts={topology_counts}, expected={expected_topology_counts}")

    status_counts = Counter(row.evidence for row in actual)
    expected_status_counts = Counter(
        {
            "E_AA": 1,
            "E_AB1": 1,
            "E_AB1R": 1,
            "E_NZ": 26,
            "E_ZF": 15,
            "E_ZD": 25,
            "E_ZP": 12,
        }
    )
    if status_counts != expected_status_counts:
        fail(f"evidence counts={status_counts}, expected={expected_status_counts}")

    project_crosscheck_count, ht_crosscheck_count = classification_crosscheck(actual)

    checks = (
        ("ordered_pair_count", 81),
        ("nonzero_count", 29),
        ("zero_count", 52),
        ("ordered_family_count", 16),
        ("marked_occurrence_count", 72),
        ("marked_pair_count", 56),
        ("topology_bucket_count", 9),
        ("evidence_bucket_count", 7),
    )
    for name, value in checks:
        print(f"PASS {name}={value}")
    print("PASS no_target_to_feynman_coefficient_inference=true")
    print(f"PASS project_exact_zero_classification_crosscheck={project_crosscheck_count}")
    print(f"PASS ht_exact_zero_classification_crosscheck={ht_crosscheck_count}")
    print("PASS classification_crosscheck_fields=left,right,exact_zero")
    print("PASS classification_crosscheck_uses_coefficients=false")
    print("PASS no_control_characters=true")
    print("PASS no_forbidden_shortcuts=true")
    print("PASS status=BLOCKED_RAW_ALL_PAIR_TRIANGLE_AND_DESCENDANT_ORBITS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
