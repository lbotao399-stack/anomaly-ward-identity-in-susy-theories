#!/usr/bin/env python3
"""Build the notation-bound WW graph/amplitude/D-word pipeline artifacts.

The builder is deliberately honest about the current boundary.  Connected
Wick-complete GraphIR and factorized AmplitudeIR pass.  The local projector
word passes the new D-word compiler.  A mixed D/barD word attached to an
external chiral leg is retained as UNIMPLEMENTED_PHASE_SEQUENCE until the
scheduled pivoted-IBP and external-token phases are implemented.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_dalgebra_compiler import (
    BarD,
    BarD2,
    Chirality,
    D,
    D2,
    DAlgebraJob,
    EdgeDeclaration,
    EndpointTag,
    ExternalLeg as DExternalLeg,
    LegDeclaration,
    Propagator,
    PropagatorDeclaration,
    compile_job,
)
from scripts.step5_pipeline_ir import NotationSchema, project_notation_schema
from scripts.step5_supergraph_pipeline import (
    AmplitudeRecord,
    CompilationResult,
    compile_request,
    render_textbook_markdown,
    ww_reflected_seed_request,
    ww_seed_request,
)


OUT = ROOT / "generated" / "step5" / "typed-pipeline"
PROVENANCE_PATHS = (
    "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md",
    "scripts/build_step5_typed_pipeline.py",
    "scripts/step5_graph_ir.py",
    "scripts/step5_pipeline_ir.py",
    "scripts/step5_supergraph_pipeline.py",
    "scripts/step5_dalgebra_compiler.py",
    "scripts/step5_vertex_grammar.py",
)


def _source_hashes() -> dict[str, str]:
    return {
        relative: hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        for relative in PROVENANCE_PATHS
    }


def _edge_declarations(amplitude: AmplitudeRecord) -> tuple[EdgeDeclaration, ...]:
    return tuple(
        EdgeDeclaration(
            edge.edge_id,
            (edge.left_half_edge, edge.right_half_edge),
            edge.momentum,
        )
        for edge in sorted(amplitude.graph.internal_edges, key=lambda item: item.edge_id)
    )


def _propagator_declarations(
    amplitude: AmplitudeRecord,
) -> tuple[PropagatorDeclaration, ...]:
    return tuple(
        PropagatorDeclaration(edge.edge_id, edge.momentum, "P_VV")
        for edge in sorted(amplitude.graph.internal_edges, key=lambda item: item.edge_id)
    )


def _adjacent_tag_for_external_leg(
    amplitude: AmplitudeRecord,
    field_name: str,
) -> tuple[str, EndpointTag, str]:
    leg = next(
        item
        for item in amplitude.graph.external_legs
        if item.field_type.name == field_name
    )
    half_edges = {
        item.half_edge_id: item for item in amplitude.graph.half_edges
    }
    vertex_id = half_edges[leg.attached_half_edge].vertex_id
    candidates: list[tuple[str, EndpointTag, str]] = []
    for edge in amplitude.graph.internal_edges:
        for endpoint in (edge.left_half_edge, edge.right_half_edge):
            if half_edges[endpoint].vertex_id == vertex_id:
                candidates.append(
                    (leg.leg_id, EndpointTag(edge.edge_id, endpoint), edge.momentum)
                )
    if not candidates:
        raise AssertionError(f"external leg {leg.leg_id} has no adjacent internal edge")
    return sorted(candidates, key=lambda item: (item[1].edge_id, item[1].endpoint))[0]


def _projector_job(amplitude: AmplitudeRecord) -> DAlgebraJob:
    edge = sorted(amplitude.graph.internal_edges, key=lambda item: item.edge_id)[0]
    tag = EndpointTag(edge.edge_id, edge.left_half_edge)
    return DAlgebraJob(
        job_id=f"D_PROJECTOR_{amplitude.orientation}",
        notation_hash=amplitude.schema_hash,
        graph_hash=amplitude.canonical_key,
        amplitude_id=amplitude.amplitude_id,
        coefficient=1,
        edges=_edge_declarations(amplitude),
        legs=(),
        propagators=_propagator_declarations(amplitude),
        operator_word=(
            D2(tag, edge.momentum),
            BarD2(tag, edge.momentum),
            D2(tag, edge.momentum),
            Propagator(edge.edge_id, edge.momentum),
        ),
    )


def _mixed_external_phase_job(amplitude: AmplitudeRecord) -> DAlgebraJob:
    leg_id, tag, momentum = _adjacent_tag_for_external_leg(amplitude, "W_plus")
    return DAlgebraJob(
        job_id=f"D_MIXED_EXTERNAL_{amplitude.orientation}",
        notation_hash=amplitude.schema_hash,
        graph_hash=amplitude.canonical_key,
        amplitude_id=amplitude.amplitude_id,
        coefficient=1,
        edges=_edge_declarations(amplitude),
        legs=(LegDeclaration(leg_id, Chirality.CHIRAL, 1, tag),),
        propagators=_propagator_declarations(amplitude),
        operator_word=(
            D("+", tag, momentum),
            BarD("-", tag, momentum),
            DExternalLeg(leg_id, Chirality.CHIRAL, 1, tag),
        ),
    )


def _one_orientation_payload(result: CompilationResult) -> dict[str, object]:
    if len(result.amplitudes) != 1:
        raise AssertionError("the primitive WW request must have one graph class")
    amplitude = result.amplitudes[0]
    projector_job = _projector_job(amplitude)
    mixed_job = _mixed_external_phase_job(amplitude)
    projector_result = compile_job(projector_job)
    mixed_result = compile_job(mixed_job)
    if projector_result.status != "PASS":
        raise AssertionError("the graph-bound local projector job must pass")
    if mixed_result.status != "UNIMPLEMENTED_PHASE_SEQUENCE":
        raise AssertionError("the unsafe mixed-external phase must fail closed")
    return {
        "orientation": amplitude.orientation,
        "graph_amplitude": result.canonical_dict(),
        "d_algebra": {
            "local_projector_job": projector_job.to_json(),
            "local_projector_result": projector_result.to_json(),
            "mixed_external_phase_job": mixed_job.to_json(),
            "mixed_external_phase_result": mixed_result.to_json(),
        },
    }


def build_payload(schema: NotationSchema | None = None) -> dict[str, object]:
    schema = schema or project_notation_schema()
    direct = compile_request(ww_seed_request(schema), schema)
    reflected = compile_request(ww_reflected_seed_request(schema), schema)
    source_hashes = _source_hashes()
    compiler_hash = hashlib.sha256(
        json.dumps(source_hashes, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "schema": 1,
        "scope": "PRIMITIVE_WW_TYPED_PIPELINE",
        "notation_hash": schema.canonical_hash,
        "compiler_hash": compiler_hash,
        "source_sha256": source_hashes,
        "scalar_ring": schema.scalar_ring.canonical_dict(),
        "orientations": [
            _one_orientation_payload(direct),
            _one_orientation_payload(reflected),
        ],
        "stage_status": {
            "notation": "PASS",
            "connected_wick_complete_supergraph": "PASS",
            "factorized_preintegration_amplitude": "PASS",
            "vertex_input": "TYPED_EXPLICIT_SEED_REQUEST",
            "canonical_routing": "EXPLICIT_BINDING_VALIDATED_NOT_SOLVED",
            "generic_identical_action_vertex_expansion": "OPEN",
            "local_dword_rules": "PASS",
            "full_scheduled_eight_row_dalgebra_per_orientation": (
                "UNIMPLEMENTED_PHASE_SEQUENCE"
            ),
            "integral_pole_binding": "NOT_BOUND_TO_NEW_DWORD_IR",
            "basis_resolved_sd_contact_orbit": "OPEN",
            "anomaly_coefficient": "NOT_ACCEPTED",
        },
        "no_imported_anomaly_coefficient": True,
    }


def _orientation_results(
    schema: NotationSchema | None = None,
) -> tuple[CompilationResult, CompilationResult]:
    schema = schema or project_notation_schema()
    return (
        compile_request(ww_seed_request(schema), schema),
        compile_request(ww_reflected_seed_request(schema), schema),
    )


def _coefficient_tex(payload: dict[str, object]) -> str:
    numerator = int(payload["numerator"])
    denominator = int(payload["denominator"])
    sqrt2_power = int(payload["sqrt2_power"])
    i_power = int(payload["i_power"]) % 4
    symbols = [str(item) for item in payload["symbols"]]
    sign = "-" if numerator < 0 else ""
    magnitude = abs(numerator)
    factors: list[str] = []
    if denominator == 1:
        if magnitude != 1 or (not symbols and sqrt2_power == 0 and i_power == 0):
            factors.append(str(magnitude))
    else:
        factors.append(r"\frac{" + str(magnitude) + "}{" + str(denominator) + "}")
    if i_power == 1:
        factors.append("i")
    elif i_power == 2:
        sign = "" if sign else "-"
    elif i_power == 3:
        sign = "" if sign else "-"
        factors.append("i")
    if sqrt2_power:
        factors.append(r"(\sqrt2)^{" + str(sqrt2_power) + "}")
    symbol_tex = {"g2": "g^2"}
    factors.extend(symbol_tex.get(symbol, symbol) for symbol in symbols)
    return sign + "".join(factors or ["1"])


def render_summary(payload: dict[str, object]) -> str:
    orientations = payload["orientations"]
    assert isinstance(orientations, list)
    lines = [
        "# Step 5A — Typed WW supergraph pipeline",
        "",
        "## Notation",
        "",
        "$$",
        r"\mathbb K=\mathbb Q(i,\sqrt2),\qquad "
        r"h_{\mathfrak N}=\texttt{" + str(payload["notation_hash"]) + r"}.",
        "$$",
        "",
        "## Compiler",
        "",
        "$$",
        r"\mathfrak N\xrightarrow{C_G}\mathfrak G"
        r"\xrightarrow{C_A}\mathfrak A"
        r"\xrightarrow{C_D}\mathfrak D.",
        "$$",
        "",
        "## Graph census",
        "",
    ]
    for item in orientations:
        assert isinstance(item, dict)
        graph_amplitude = item["graph_amplitude"]
        assert isinstance(graph_amplitude, dict)
        completeness = graph_amplitude["completeness"]
        amplitudes = graph_amplitude["amplitudes"]
        assert isinstance(completeness, dict) and isinstance(amplitudes, list)
        amplitude = amplitudes[0]
        assert isinstance(amplitude, dict)
        coefficient = amplitude["exact_coefficient_reduced"]
        assert isinstance(coefficient, dict)
        orientation = str(item["orientation"])
        exact_coefficient = _coefficient_tex(coefficient)
        lines.extend(
            [
                f"### {orientation}",
                "",
                "$$",
                r"N_{\rm typed}="
                + str(completeness["typed_pairings"])
                + r",\qquad N_{\rm admitted}="
                + str(completeness["endpoint_admissible_pairings"])
                + r",\qquad b_1=1.",
                "$$",
                "",
                "$$",
                r"(r_0,r_1,r_2)=(k,k+q,k+p+q),\qquad "
                r"C_G=" + exact_coefficient + ".",
                "$$",
                "",
            ]
        )
    lines.extend(
        [
            "## D-algebra status",
            "",
            "$$",
            r"D^2\bar D^2D^2=-16p_{(4)}^2D^2"
            r"\quad\Longrightarrow\quad"
            r"\texttt{local projector job = PASS}.",
            "$$",
            "",
            "$$",
            r"D\bar D\,W_{\rm ext}"
            r"\quad\Longrightarrow\quad"
            r"\texttt{UNIMPLEMENTED\_PHASE\_SEQUENCE},",
            "$$",
            "",
            "$$",
            r"\texttt{MIXED\_D\_BARD\_NORMALIZATION}"
            r"\prec\texttt{PIVOTED\_IBP}"
            r"\prec\texttt{EXTERNAL\_CHIRALITY}.",
            "$$",
            "",
            "$$",
            r"\Gamma_{\rm anomaly}:\ \texttt{NOT\_ACCEPTED}.",
            "$$",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(
    payload: dict[str, object],
    schema: NotationSchema | None = None,
) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    schema = schema or project_notation_schema()
    schema.write_json(OUT / "project-notation.json")
    (OUT / "ww-typed-pipeline.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (OUT / "ww-typed-pipeline.md").write_text(
        render_summary(payload),
        encoding="utf-8",
    )
    for result in _orientation_results(schema):
        orientation = result.amplitudes[0].orientation.lower()
        (OUT / f"ww-{orientation}.md").write_text(
            render_textbook_markdown(result),
            encoding="utf-8",
        )
        amplitude = result.amplitudes[0]
        (OUT / f"ww-{orientation}.dot").write_text(
            amplitude.graph.to_dot(),
            encoding="utf-8",
        )
        (OUT / f"ww-{orientation}.mermaid").write_text(
            amplitude.graph.to_mermaid(),
            encoding="utf-8",
        )


def main(argv: Sequence[str] = ()) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--notation",
        type=Path,
        help="canonical NotationSchema JSON; omitted uses the frozen Project WW schema",
    )
    arguments = parser.parse_args(list(argv))
    schema = (
        NotationSchema.load_json(arguments.notation)
        if arguments.notation is not None
        else project_notation_schema()
    )
    payload = build_payload(schema)
    write_outputs(payload, schema)
    statuses = payload["stage_status"]
    assert isinstance(statuses, dict)
    print(
        "Step-5 typed pipeline: "
        f"schema={payload['notation_hash']} "
        f"graph={statuses['connected_wick_complete_supergraph']} "
        f"amplitude={statuses['factorized_preintegration_amplitude']} "
        f"D={statuses['full_scheduled_eight_row_dalgebra_per_orientation']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
