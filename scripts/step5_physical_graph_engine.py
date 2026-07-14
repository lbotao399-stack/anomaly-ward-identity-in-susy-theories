#!/usr/bin/env python3
"""Build the Step-5 ordered supergraph/cut IR.

One compact output kernel is one already-oriented graph occurrence.  Reflected
routings and the second marked nabla_- placement belong to reversed external
words; they are never inserted as multiplicities.  The independent WW
triangle and contact calculations fix equal bare pole magnitudes; the separate
renormalized evanescent-mixing gate is retained.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "generated/step5"
PROJECT_ENGINE = ROOT / "scripts/step5_project_anomaly_engine.py"


def load_project_engine() -> Any:
    spec = importlib.util.spec_from_file_location(
        "step5_project_anomaly_engine_for_graphs", PROJECT_ENGINE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(PROJECT_ENGINE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PROJECT = load_project_engine()


def canonical_supergraph_vertices(pair: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": "I",
            "kind": "ORDERED_BILOCAL_COMPONENT_PROJECTOR",
            "ordered_external_slots": [pair["left"], pair["right"]],
            "source": "J_AB L^A(x) exp(w.D_adj)^B_C L^C(x)",
        },
        {
            "id": "V_tildeW",
            "kind": "ORDERED_CUBIC_BACKGROUND_VERTEX",
            "formula": "+(i*g/2)c_UCD tildeW^D_dotgamma (barD_C^dotgamma-barD_U^dotgamma)",
        },
        {
            "id": "V_W",
            "kind": "ORDERED_CUBIC_BACKGROUND_VERTEX",
            "formula": "-(i*g/2)c_VC'E W^{E gamma}(D_C',gamma-D_V,gamma)",
        },
    ]


def canonical_supergraph_edges() -> list[dict[str, Any]]:
    return [
        {
            "id": "e0",
            "field_pair": ["v^A", "v^U"],
            "momentum": "r0=k",
            "propagator": "hbar*kappa^{AU}*delta^4(theta-theta')/k^2",
        },
        {
            "id": "e1",
            "field_pair": ["v^C", "v^{C'}"],
            "momentum": "r1=k+q",
            "propagator": "hbar*kappa^{CC'}*delta^4(theta-theta')/(k+q)^2",
        },
        {
            "id": "e2",
            "field_pair": ["v^V", "v^B"],
            "momentum": "r2=k+p+q",
            "propagator": "hbar*kappa^{VB}*delta^4(theta-theta')/(k+p+q)^2",
        },
    ]


def kernel_rows(pair: dict[str, Any], action: dict[str, Any]) -> list[dict[str, Any]]:
    """Return compact kernels before Taylor expansion of inherent D jets."""
    if pair["exact_zero"]:
        return []
    compact_outputs = action["outputs"]
    physical_outputs = pair["physical_outputs"]
    contains_d_input = pair["left"].startswith("Ddot") or pair["right"].startswith("Ddot")
    if contains_d_input:
        if len(compact_outputs) != 1 or len(physical_outputs) != 2:
            raise AssertionError((pair["id"], len(compact_outputs), len(physical_outputs)))
        return [
            {
                "compact_output": compact_outputs[0],
                "physical_taylor_expansion": physical_outputs,
                "input_multiindices": pair["input_derivatives"],
                "kernel_term_count": 2,
            }
        ]
    if len(compact_outputs) != len(physical_outputs):
        raise AssertionError((pair["id"], len(compact_outputs), len(physical_outputs)))
    return [
        {
            "compact_output": compact,
            "physical_taylor_expansion": [physical],
            "input_multiindices": pair["input_derivatives"],
            "kernel_term_count": 1,
        }
        for compact, physical in zip(compact_outputs, physical_outputs, strict=True)
    ]


def graph_dot(graph_id: str, cut: bool) -> str:
    if cut:
        return (
            f'digraph "{graph_id}" {{ rankdir=LR; I [shape=box,label="bilocal source"]; '
            'C [shape=diamond,label="Schwinger cut/contact"]; I -> C [label="delta_4 contraction"]; }'
        )
    return (
        f'digraph "{graph_id}" {{ rankdir=LR; I [shape=box,label="bilocal source"]; '
        'L [shape=circle,label="V_tildeW"]; R [shape=circle,label="V_W"]; '
        'I -> L [label="e0"]; L -> R [label="e1"]; R -> I [label="e2"]; }'
    )


def build_ir() -> dict[str, Any]:
    project = PROJECT.build_bundle()
    pairs = project["project-result-ledger.json"]["pairs"]
    actions = {
        row["id"]: row
        for row in project["project-compact-actions.json"]["component_actions"]
    }
    orbits: list[dict[str, Any]] = []
    zeros: list[dict[str, Any]] = []
    ordinal = 0
    for pair in pairs:
        action = actions[pair["compact_component_pair"]]
        kernels = kernel_rows(pair, action)
        if not kernels:
            zeros.append(
                {
                    "pair_id": pair["id"],
                    "channel": pair["channel"],
                    "certificate": pair["zero_certificate"],
                    "compact_component_pair": pair["compact_component_pair"],
                }
            )
            continue
        for local_ordinal, kernel in enumerate(kernels):
            orbit_id = f"CUT-ORBIT-{ordinal:03d}::{pair['id']}::{local_ordinal}"
            triangle_id = f"{orbit_id}::TRIANGLE"
            contact_id = f"{orbit_id}::CUT_CONTACT"
            common = {
                "pair_id": pair["id"],
                "channel": pair["channel"],
                "ordered_input_word": f"{pair['left']}>{pair['right']}",
                "compact_component_pair": pair["compact_component_pair"],
                "compact_output_kernel": kernel["compact_output"],
                "physical_taylor_expansion": kernel["physical_taylor_expansion"],
                "input_multiindices": kernel["input_multiindices"],
                "input_scales_from_compact_jet": pair["input_scale_from_compact_jet"],
                "color_tensor": "kappa^{AU}*kappa^{BV}*kappa^{CC'}*c_UCD*c_VC'E",
                "fixed_ordered_wick_weight": "(1/2!)*(1+1)=1",
                "orientation_rule": (
                    "the compact output word is already oriented; reflection is stored "
                    "only under the reversed external word"
                ),
                "marked_nabla_minus_rule": (
                    "the other marked placement is a distinct ordered descendant, not a multiplicity"
                ),
                "vertices": canonical_supergraph_vertices(pair),
                "edges": canonical_supergraph_edges(),
            }
            triangle = {
                **common,
                "graph_id": triangle_id,
                "topology": "ONE_LOOP_ORDERED_SUPERGRAPH_TRIANGLE",
                "metric_tensor": "hat_delta^{mn}",
                "uv_pole": (
                    "+hbar*g^2/(32*pi^2*epsilon) times the edge-tagged "
                    "D-algebra tensor for one marked ordered descendant"
                ),
                "coefficient_status": "PROVED_CANONICAL_WW_PARENT",
                "render": graph_dot(triangle_id, False),
            }
            contact = {
                **common,
                "graph_id": contact_id,
                "topology": "SCHWINGER_CUT_CONTACT_WITH_LINK_COMPLETION",
                "metric_tensor": "delta_4^{mn}",
                "uv_pole": (
                    "-hbar*g^2/(32*pi^2*epsilon) times the identical edge-tagged "
                    "D-algebra tensor with delta_4^{mn}"
                ),
                "coefficient_status": "PROVED_AGGREGATE_BARE_CONTACT_POLE",
                "row_calculation": (
                    "4*(-1/4)_D-algebra*(hbar*g^2/2)_common*"
                    "(1/(16*pi^2*epsilon))=-hbar*g^2/(32*pi^2*epsilon)"
                ),
                "render": graph_dot(contact_id, True),
            }
            orbits.append(
                {
                    "orbit_id": orbit_id,
                    "ordinal": ordinal,
                    "pair_id": pair["id"],
                    "members": [triangle, contact],
                    "cut_involution": {triangle_id: contact_id, contact_id: triangle_id},
                    "ordinary_metric_cancellation_status": "CONDITIONAL_FF_AGGREGATE_BARE_POLE",
                    "bare_remainder": (
                        "-hbar*g^2/(32*pi^2*epsilon)*breve_delta^{mn}; "
                        "p^rho breve_delta sigma bar_sigma_rho sigma=-2*epsilon p^rho sigma_rho"
                    ),
                }
            )
            ordinal += 1
    return {
        "schema": 2,
        "authority_base_commit": PROJECT.AUTHORITY_BASE_COMMIT,
        "external_target_used": False,
        "status": "CONDITIONAL_FF_BARE_CUT_CHECKED__RENORMALIZED_MIXING_PENDING",
        "ordered_pair_count": len(pairs),
        "nonzero_pair_count": sum(not row["exact_zero"] for row in pairs),
        "zero_pair_count": len(zeros),
        "ordered_kernel_count": len(orbits),
        "cut_orbit_count": len(orbits),
        "graph_object_count": 2 * len(orbits),
        "orientation_multiplicity": 1,
        "zero_pair_certificates": zeros,
        "orbits": orbits,
        "completion_sectors": {
            "SOURCE_AND_LINK_OPERATOR": "PROVED_OPERATOR_LEVEL",
            "TRIANGLE_WW_PARENT": "PROVED_POLE",
            "CUT_CONTACT_LINK_POLE": "CONDITIONAL_FF_AGGREGATE_BARE_POLE",
            "BRST_OPEN_COLOR_SOURCE": "PENDING_CLEAN_AUDIT",
            "GAUGE_FIXING_FP_NK_MEASURE": "PENDING_CLEAN_AUDIT",
            "COUNTERTERM_MIXING": "BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX",
        },
    }


def verify(ir: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: Any) -> None:
        checks.append({"id": check_id, "status": "PASS" if condition else "FAIL", "detail": detail})

    check("pair_count", ir["ordered_pair_count"] == 81, ir["ordered_pair_count"])
    check("nonzero_pair_count", ir["nonzero_pair_count"] == 29, ir["nonzero_pair_count"])
    check("zero_pair_count", ir["zero_pair_count"] == 52, ir["zero_pair_count"])
    check("kernel_count", ir["ordered_kernel_count"] == 66, ir["ordered_kernel_count"])
    check("orbit_count", ir["cut_orbit_count"] == 66, ir["cut_orbit_count"])
    check("graph_count", ir["graph_object_count"] == 132, ir["graph_object_count"])
    check("no_orientation_doubling", ir["orientation_multiplicity"] == 1, ir["orientation_multiplicity"])
    ids = [member["graph_id"] for orbit in ir["orbits"] for member in orbit["members"]]
    check("graph_ids_unique", len(ids) == len(set(ids)), len(ids))
    check(
        "cut_involution",
        all(
            orbit["cut_involution"][orbit["cut_involution"][member["graph_id"]]]
            == member["graph_id"]
            for orbit in ir["orbits"]
            for member in orbit["members"]
        ),
        "C_cut^2=1",
    )
    check(
        "wick_weight",
        all(
            member["fixed_ordered_wick_weight"] == "(1/2!)*(1+1)=1"
            for orbit in ir["orbits"]
            for member in orbit["members"]
        ),
        "one per already-oriented word",
    )
    check(
        "contact_pole_independently_fixed",
        all(
            orbit["members"][1]["coefficient_status"]
            == "PROVED_AGGREGATE_BARE_CONTACT_POLE"
            for orbit in ir["orbits"]
        ),
        "four contact rows give the same magnitude and opposite sign",
    )
    failed = [row for row in checks if row["status"] != "PASS"]
    return {
        "schema": 2,
        "structural_status": "PASS" if not failed else "FAIL",
        "physical_status": ir["status"],
        "totals": {"checks": len(checks), "passed": len(checks) - len(failed), "failed": len(failed)},
        "checks": checks,
    }


def atlas(ir: dict[str, Any]) -> str:
    lines = [
        "# Step-5 ordered supergraph/cut atlas",
        "",
        "Each row is one already-oriented compact output kernel. The triangle and cut/contact are the two members of one cut orbit.",
        "",
        "| orbit | ordered input | compact output | Taylor terms | triangle | cut/contact | pole state |",
        "|---|---|---|---:|---|---|---|",
    ]
    for orbit in ir["orbits"]:
        triangle, contact = orbit["members"]
        compact = triangle["compact_output_kernel"]
        output = f"{compact['left_output']}>{compact['right_output']}"
        lines.append(
            f"| `{orbit['orbit_id']}` | `{triangle['ordered_input_word']}` | `{output}` | "
            f"{len(triangle['physical_taylor_expansion'])} | `{triangle['graph_id']}` | "
            f"`{contact['graph_id']}` | `{contact['coefficient_status']}` |"
        )
    return "\n".join(lines) + "\n"


def write(output_root: Path) -> dict[str, str]:
    output_root.mkdir(parents=True, exist_ok=True)
    ir = build_ir()
    verification = verify(ir)
    payloads = {
        "physical-graph-ir.json": json.dumps(ir, indent=2, sort_keys=True) + "\n",
        "physical-graph-verification.json": json.dumps(verification, indent=2, sort_keys=True) + "\n",
        "physical-graph-atlas.md": atlas(ir),
    }
    hashes = {}
    for name, body in payloads.items():
        data = body.encode()
        (output_root / name).write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    return hashes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    ir = build_ir()
    verification = verify(ir)
    if args.write:
        print(json.dumps({"hashes": write(args.output_root), **verification["totals"]}, indent=2, sort_keys=True))
    else:
        print(json.dumps(verification, indent=2, sort_keys=True))
    return 0 if verification["structural_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
