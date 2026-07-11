#!/usr/bin/env python3
"""Build the machine-readable section verdict index from the three source audits."""

from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "audits/ws-dictionary/draft-section-verdicts.json"
TASK = "CONTRACT-WEINBERG-SREDNICKI-CODEX-DICTIONARY-001"
ALLOWED_STATUSES = {
    "VERIFIED",
    "CORRECTED",
    "FALSE",
    "NOT_IN_SCOPE",
    "SOURCE_INSUFFICIENT",
}

REPORTS = (
    ROOT / "audits/ws-dictionary/sections-00-25-spinor-gamma.md",
    ROOT / "audits/ws-dictionary/sections-26-39-superspace-chiral.md",
    ROOT / "audits/ws-dictionary/sections-40-54-gauge-action.md",
)

SOURCES = {
    "P1": {
        "source": "PROJECT",
        "path": "contracts/foundations/step-01-supersymmetry-commutator.md",
    },
    "P2A": {
        "source": "PROJECT",
        "path": "contracts/foundations/step-02a-flat-superspace.md",
    },
    "P2B": {
        "source": "PROJECT",
        "path": "contracts/foundations/step-02b-superconformal-superspace.md",
    },
    "W54": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/05-04-dirac-formalism-34cee2b74b3f8115a5a1fac623c31862.md",
        "page_id": "34cee2b74b3f8115a5a1fac623c31862",
    },
    "W261": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-01-direct-field-supermultiplets-34cee2b74b3f81efaf28fa4031d4303e.md",
        "page_id": "34cee2b74b3f81efaf28fa4031d4303e",
    },
    "W26.1": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-01-direct-field-supermultiplets-34cee2b74b3f81efaf28fa4031d4303e.md",
        "page_id": "34cee2b74b3f81efaf28fa4031d4303e",
    },
    "W26.2": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-02-general-superfields-34cee2b74b3f8182a538e629f277c1e7.md",
        "page_id": "34cee2b74b3f8182a538e629f277c1e7",
    },
    "W26.3": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-03-chiral-linear-superfields-34cee2b74b3f8163b3b3fa265e1815b0.md",
        "page_id": "34cee2b74b3f8163b3b3fa265e1815b0",
    },
    "W26.4": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-04-renormalizable-chiral-theories-34cee2b74b3f81f6bba1c92f1c61727b.md",
        "page_id": "34cee2b74b3f81f6bba1c92f1c61727b",
    },
    "W26A": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/26-appendix-majorana-spinors-34cee2b74b3f81349f82dd4d257ba62c.md",
        "page_id": "34cee2b74b3f81349f82dd4d257ba62c",
    },
    "W27.1": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/27-01-gauge-invariant-chiral-action-34cee2b74b3f81b6b72bd47d34df4d88.md",
        "page_id": "34cee2b74b3f81b6b72bd47d34df4d88",
    },
    "W27.2": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/27-02-abelian-gauge-superfield-action-34cee2b74b3f8131b10edd7a1dad0172.md",
        "page_id": "34cee2b74b3f8131b10edd7a1dad0172",
    },
    "W27.3": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/27-03-general-gauge-superfield-action-34cee2b74b3f812f97c2d0aa902aba5d.md",
        "page_id": "34cee2b74b3f812f97c2d0aa902aba5d",
    },
    "W27.4": {
        "source": "WEINBERG",
        "path": "references/vendor/notion/weinberg/27-04-renormalizable-gauge-theory-34cee2b74b3f81949500f3f35884f580.md",
        "page_id": "34cee2b74b3f81949500f3f35884f580",
    },
    "S34": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/34-left-right-spinor-fields-812622be5c2d466faeb4a613eabad116.md",
        "page_id": "812622be5c2d466faeb4a613eabad116",
    },
    "S35": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/35-spinor-indices-1da2841c4cda42669598313359e3d07d.md",
        "page_id": "1da2841c4cda42669598313359e3d07d",
    },
    "S36": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/36-spinor-lagrangians-b41fbf43fd9247d280fe27cace58ea52.md",
        "page_id": "b41fbf43fd9247d280fe27cace58ea52",
    },
    "S38": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/38-spinor-technology-19f10ddaf77242df946f54f8c3f99be6.md",
        "page_id": "19f10ddaf77242df946f54f8c3f99be6",
    },
    "S47": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/47-gamma-matrix-technology-22607397de1a4af2bc9610b320426208.md",
        "page_id": "22607397de1a4af2bc9610b320426208",
    },
    "S49": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/49-majorana-feynman-rules-1707531df3dd440bbd490a9e2b963de8.md",
        "page_id": "1707531df3dd440bbd490a9e2b963de8",
    },
    "S95": {
        "source": "SREDNICKI",
        "path": "references/vendor/notion/srednicki/95-supersymmetry-0151805c7e85457a9928fcfd0e83da2a.md",
        "page_id": "0151805c7e85457a9928fcfd0e83da2a",
    },
}

for source in SOURCES.values():
    page_id = source.get("page_id")
    if page_id:
        source["url"] = f"https://app.notion.com/p/{page_id}"

HEADING = re.compile(
    r"^###\s+§?(\d+)\.?\s+(.*?)\s+(?:--|—)\s+`?([A-Z_]+)`?\s*$"
)
CITATION = re.compile(r"(?<![A-Za-z0-9.])([WSP][A-Za-z0-9.]*):(\d+)(?:-(\d+))?")


def parse_report(path: Path) -> list[dict[str, object]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    headings: list[tuple[int, int, str, str]] = []
    for index, line in enumerate(lines):
        match = HEADING.match(line)
        if not match:
            continue
        number, title, status = match.groups()
        headings.append((index, int(number), title.strip(), status))

    sections: list[dict[str, object]] = []
    for position, (start, number, title, status) in enumerate(headings):
        end = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
        body = "\n".join(lines[start:end])
        citations: list[dict[str, object]] = []
        seen: set[tuple[str, int, int]] = set()
        for match in CITATION.finditer(body):
            key = match.group(1)
            first = int(match.group(2))
            last = int(match.group(3) or match.group(2))
            identity = (key, first, last)
            if identity in seen:
                continue
            seen.add(identity)
            citations.append({"source_key": key, "first_line": first, "last_line": last})
        sections.append(
            {
                "section": number,
                "title": title,
                "status": status,
                "audit_path": str(path.relative_to(ROOT)),
                "audit_heading_line": start + 1,
                "citations": citations,
            }
        )
    return sections


def main() -> None:
    sections = [section for report in REPORTS for section in parse_report(report)]
    sections.sort(key=lambda item: int(item["section"]))
    errors: list[str] = []
    numbers = [int(item["section"]) for item in sections]
    if numbers != list(range(55)):
        errors.append(f"section coverage is {numbers!r}, expected 0..54")
    for section in sections:
        if section["status"] not in ALLOWED_STATUSES:
            errors.append(f"section {section['section']} has invalid status {section['status']}")
        if not section["citations"]:
            errors.append(f"section {section['section']} has no exact source anchor")
        for citation in section["citations"]:
            if citation["source_key"] not in SOURCES:
                errors.append(
                    f"section {section['section']} has unknown source key {citation['source_key']}"
                )

    result = {
        "schema": 1,
        "task": TASK,
        "section_range": {"first": 0, "last": 54, "count": 55},
        "allowed_statuses": sorted(ALLOWED_STATUSES),
        "source_registry": SOURCES,
        "sections": sections,
        "errors": errors,
        "result": "PASS" if not errors else "FAIL",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if errors:
        raise SystemExit("; ".join(errors))
    print(json.dumps({"sections": len(sections), "result": result["result"]}))


if __name__ == "__main__":
    main()
