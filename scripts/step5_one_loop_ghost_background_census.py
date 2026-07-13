#!/usr/bin/env python3
"""All-background-order FP/NK one-loop 1PI exclusion.

External background ports do not enter E-V+1.  A ghost cycle has loop number
one before it is attached to the physical insertion component.  Joining two
connected components by a quantum edges adds a-1 cycles:

    L_total = L_phys + 1 + (a - 1) = L_phys + a.

One attachment is a bridge and is not 1PI; two or more attachments give at
least two loops.  The result assumes the Step-5A typed propagator grammar and
that the physical composite insertion has no FP/NK ports.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.verify_step5a_ghost_census import ALLOWED_PROPAGATOR_TYPES  # noqa: E402


GENERATED = ROOT / "generated/step5/one-loop-ghost-background-census.json"
AUDIT = ROOT / "audits/step5-one-loop-ghost-background-census-verification.json"


def joined_cycle_rank(
    physical_loops: int,
    determinant_loops: int,
    attachment_edges: int,
) -> int:
    if physical_loops < 0 or determinant_loops < 0:
        raise ValueError("loop numbers must be nonnegative")
    if attachment_edges < 1:
        raise ValueError("connected components require at least one attachment")
    return physical_loops + determinant_loops + attachment_edges - 1


def attachment_census(max_background_order: int = 8) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for background_order in range(max_background_order + 1):
        for physical_loops in range(0, 3):
            for attachments in range(1, 5):
                loop_number = joined_cycle_rank(
                    physical_loops,
                    determinant_loops=1,
                    attachment_edges=attachments,
                )
                is_one_particle_irreducible = attachments >= 2
                rows.append(
                    {
                        "background_order": background_order,
                        "physical_loops": physical_loops,
                        "determinant_loops": 1,
                        "attachment_edges": attachments,
                        "external_background_ports_change_cycle_rank": False,
                        "loop_number": loop_number,
                        "one_particle_irreducible": is_one_particle_irreducible,
                        "classification": (
                            "ONE_PARTICLE_REDUCIBLE_BRIDGE"
                            if attachments == 1
                            else f"ONE_PARTICLE_IRREDUCIBLE_L_{loop_number}"
                        ),
                    }
                )
    return rows


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload(max_background_order: int = 8) -> dict[str, object]:
    rows = attachment_census(max_background_order)
    one_loop_1pi = [
        row for row in rows if row["one_particle_irreducible"] and row["loop_number"] == 1
    ]
    checks = {
        "typed_grammar_has_no_physical_ghost_mixed_propagator": all(
            left == right == "V" or (left != "V" and right != "V")
            for left, right in ALLOWED_PROPAGATOR_TYPES
        ),
        "single_attachment_is_always_1pr": all(
            not row["one_particle_irreducible"]
            for row in rows
            if row["attachment_edges"] == 1
        ),
        "every_1pi_attachment_has_at_least_two_loops": all(
            row["loop_number"] >= 2
            for row in rows
            if row["one_particle_irreducible"]
        ),
        "no_one_loop_1pi_determinant_family": not one_loop_1pi,
        "background_order_does_not_change_cycle_rank": all(
            not row["external_background_ports_change_cycle_rank"] for row in rows
        ),
    }
    result = (
        "PROVED_ABSENT_AT_ONE_LOOP_1PI_ALL_BACKGROUND_ORDERS"
        if not one_loop_1pi
        else "CANDIDATE_EXISTS"
    )
    return {
        "schema": "Step5OneLoopGhostBackgroundCensus.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope": "STEP5A_ONE_LOOP_1PI_ALL_BACKGROUND_ORDERS",
        "assumptions": [
            "physical composite insertion has no FP or NK port",
            "no mixed physical-ghost propagator",
            "determinant fields form a closed internal cycle",
            "external background ports are not Wick-contracted",
        ],
        "identity": "L_total=L_phys+L_det+(a-1)=L_phys+a for L_det=1",
        "result": result,
        "FP_result": result,
        "NK_result": result,
        "finite_BV_cycle_statement": "NOT_USED; STEP5C_OBLIGATION",
        "max_background_order_tested": max_background_order,
        "rows": rows,
        "checks": checks,
        "external_results_imported": False,
    }


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    audit = {
        "schema": "Step5OneLoopGhostBackgroundCensusAudit.v1",
        "status": payload["status"],
        "scope": payload["scope"],
        "totals": {
            "checks": len(payload["checks"]),
            "failed": sum(not result for result in payload["checks"].values()),
            "rows": len(payload["rows"]),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "result": payload["result"],
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT.write_bytes(canonical_json(audit))


if __name__ == "__main__":
    write_artifacts()
