#!/usr/bin/env python3
"""Build the notation-bound WW graph/amplitude/D-word pipeline artifacts.

The builder is deliberately honest about the current boundary.  Connected
Wick-complete GraphIR and factorized AmplitudeIR pass.  The physical WW
triangle has a topology-bound scheduled eight-row compiler per orientation.
Generic mixed external words outside that exact schedule still fail closed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
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
    compare_scheduled_ww_to_legacy,
    compile_job,
    compile_scheduled_ww_rows,
)
from scripts.step5_pipeline_ir import NotationSchema, project_notation_schema
from scripts.step5_ww_seed import endpoint_rows
from scripts import verify_step5_propagators as step5_matrix_oracle
from scripts.step5_supergraph_pipeline import (
    AmplitudeRecord,
    CompilationResult,
    compile_request,
    render_textbook_markdown,
    ww_reflected_seed_request,
    ww_seed_request,
)
from scripts.verify_step5_dred_integrals import (
    FOURIER_PHASE,
    LOOP_MEASURE,
    SIGNATURE,
    build_audit as build_dred_integral_audit,
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
    "scripts/step5_ww_seed.py",
    "scripts/verify_step5_dred_integrals.py",
    "scripts/verify_step5_propagators.py",
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


def _specialized_row_pole_binding(
    amplitude: AmplitudeRecord,
    dred_audit: dict[str, object],
) -> dict[str, object]:
    """Bind every exact specialized WW row to the Project DRED master.

    This is deliberately narrower than a generic D-word compilation.  The
    row D-chain remains the exact specialized certificate emitted by
    ``step5_ww_seed.endpoint_rows``.  The binding proves that its coefficient,
    graph provenance, and rank-two UV master compose without an untyped or
    floating-point step.
    """

    if dred_audit["status"] != "PASS":
        raise AssertionError("the independent DRED integral audit must pass")
    integrals = dred_audit["integrals"]
    if not isinstance(integrals, dict):
        raise AssertionError("the DRED audit has no typed integral payload")
    laurent = integrals["laurent_in_units_of_A0"]
    if not isinstance(laurent, dict):
        raise AssertionError("the DRED audit has no Laurent coefficient map")
    tensor_pole = laurent["coefficient_of_hat_g_in_T"]
    if not isinstance(tensor_pole, dict) or tensor_pole.get("-1") != "1/4":
        raise AssertionError("the rank-two DRED master pole must be A0/4")

    coefficient = amplitude.exact_coefficient_reduced
    if (
        coefficient.sqrt2_power != 0
        or coefficient.i_power % 4 != 0
        or coefficient.symbols != ("g2",)
    ):
        raise AssertionError("the primitive WW amplitude must lie in Q*g2")
    graph_prefactor = coefficient.rational
    d_chain = Fraction(-1, 2)
    row_prefactor = graph_prefactor * d_chain
    expected_row_prefactor = Fraction(1, 16)
    if row_prefactor != expected_row_prefactor:
        raise AssertionError("typed amplitude times the WW D-chain has the wrong sign")

    master_pole_in_A0 = Fraction(1, 4)
    row_pole_in_A0 = row_prefactor * master_pole_in_A0
    row_pole_in_pi = row_pole_in_A0 / 16
    orientation_pole_in_pi = 8 * row_pole_in_pi
    expected_orientation_pole = Fraction(1, 128)
    if orientation_pole_in_pi != expected_orientation_pole:
        raise AssertionError("eight row poles do not sum to the orientation pole")

    rows = endpoint_rows(amplitude.orientation)
    if len(rows) != 8:
        raise AssertionError("one WW orientation must have exactly eight rows")
    row_certificates: list[dict[str, object]] = []
    for row in rows:
        exact_checks = row["exact_checks"]
        if not isinstance(exact_checks, dict) or not all(exact_checks.values()):
            raise AssertionError(f"specialized row {row['trace_id']} failed")
        exact_chain = row["exact_D_chain"]
        if not isinstance(exact_chain, dict) or exact_chain["product"] != "-1/2":
            raise AssertionError(f"row {row['trace_id']} has an unbound D-chain")
        expected_text = "+g^2/(1024*pi^2*epsilon)"
        if expected_text not in str(row["triangle_metric_pole"]):
            raise AssertionError(f"row {row['trace_id']} pole sign disagrees")
        row_certificates.append(
            {
                "trace_id": row["trace_id"],
                "notation_hash": amplitude.schema_hash,
                "graph_hash": amplitude.canonical_key,
                "amplitude_id": amplitude.amplitude_id,
                "specialized_D_chain": exact_chain,
                "endpoint_sign": row["total_endpoint_sign"],
                "mixed_anticommutator_momenta": row[
                    "mixed_anticommutator_momenta"
                ],
                "external_leg_derivative_tokens": row[
                    "external_leg_derivative_tokens"
                ],
                "row_prefactor_in_g2": str(row_prefactor),
                "rank_two_master_pole_in_A0": str(master_pole_in_A0),
                "row_pole_in_A0_g2": str(row_pole_in_A0),
                "row_pole_in_pi2_g2": str(row_pole_in_pi),
                "metric_space": "hat_delta^(mu nu)",
                "status": "PASS",
            }
        )

    dred_sha256 = hashlib.sha256(
        json.dumps(dred_audit, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
    ).hexdigest()
    return {
        "status": "PASS_ISOLATED_TRIANGLE_8_ROW_DRED_MASTER_BINDING",
        "scope": (
            "SPECIALIZED_WW_ROW_CERTIFICATE_NOT_GENERIC_DWORD_PHASE_COMPLETION"
        ),
        "notation_hash": amplitude.schema_hash,
        "graph_hash": amplitude.canonical_key,
        "amplitude_id": amplitude.amplitude_id,
        "dred_audit_sha256": dred_sha256,
        "dred_audit_exact_checks": dred_audit["totals"],
        "arithmetic": "EXACT_Q_AND_Q_I_NO_FLOATING_POINT",
        "derivation": [
            f"C_graph={graph_prefactor}*g2",
            "C_D=-1/2",
            f"C_row=C_graph*C_D={row_prefactor}*g2",
            "Pole[T^(mu nu)]=A0*hat_delta^(mu nu)/(4*epsilon)",
            f"Pole[row]={row_pole_in_A0}*A0*g2/epsilon",
            f"A0=1/(16*pi^2) gives Pole[row]={row_pole_in_pi}*g2/(pi^2*epsilon)",
            f"sum_8 Pole[row]={orientation_pole_in_pi}*g2/(pi^2*epsilon)",
        ],
        "row_certificates": row_certificates,
        "orientation_pole_in_pi2_g2": str(orientation_pole_in_pi),
        "generic_Dword_phase_completion": False,
        "basis_resolved_contact_quotient": False,
        "contact_pole_status": "INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY",
        "anomaly_coefficient_status": "INVALIDATED_NOT_PROPAGATED",
    }


def _one_orientation_payload(
    result: CompilationResult,
    dred_audit: dict[str, object],
    schema: NotationSchema,
) -> dict[str, object]:
    if len(result.amplitudes) != 1:
        raise AssertionError("the primitive WW request must have one graph class")
    amplitude = result.amplitudes[0]
    projector_job = _projector_job(amplitude)
    mixed_job = _mixed_external_phase_job(amplitude)
    projector_result = compile_job(projector_job)
    mixed_result = compile_job(mixed_job)
    scheduled = compile_scheduled_ww_rows(amplitude, schema, step5_matrix_oracle)
    legacy_oracle = compare_scheduled_ww_to_legacy(
        scheduled, endpoint_rows(amplitude.orientation)
    )
    if projector_result.status != "PASS":
        raise AssertionError("the graph-bound local projector job must pass")
    if mixed_result.status != "UNIMPLEMENTED_PHASE_SEQUENCE":
        raise AssertionError("the unsafe mixed-external phase must fail closed")
    if legacy_oracle["status"] != "PASS":
        raise AssertionError(
            "the independently scheduled WW rows disagree with the legacy oracle"
        )
    return {
        "orientation": amplitude.orientation,
        "graph_amplitude": result.canonical_dict(),
        "d_algebra": {
            "local_projector_job": projector_job.to_json(),
            "local_projector_result": projector_result.to_json(),
            "mixed_external_phase_job": mixed_job.to_json(),
            "mixed_external_phase_result": mixed_result.to_json(),
            "scheduled_ww_result": scheduled.to_json(),
            "legacy_endpoint_equality_oracle": legacy_oracle,
        },
        "specialized_row_pole_binding": _specialized_row_pole_binding(
            amplitude, dred_audit
        ),
    }


def build_payload(schema: NotationSchema | None = None) -> dict[str, object]:
    schema = schema or project_notation_schema()
    direct = compile_request(ww_seed_request(schema), schema)
    reflected = compile_request(ww_reflected_seed_request(schema), schema)
    dred_audit = build_dred_integral_audit(
        FOURIER_PHASE,
        LOOP_MEASURE,
        SIGNATURE,
    )
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
            _one_orientation_payload(direct, dred_audit, schema),
            _one_orientation_payload(reflected, dred_audit, schema),
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
                "PASS_PHYSICAL_16_ROW_PHASE_SEQUENCE_FAIL_CLOSED_ELSEWHERE"
            ),
            "integral_pole_binding": (
                "PASS_ISOLATED_TRIANGLE_16_ROW_DRED_MASTER_BINDING_"
                "NOT_GENERIC_DWORD_COMPLETION"
            ),
            "basis_resolved_sd_contact_orbit": (
                "INVALIDATED_REQUIRES_TYPED_CONTACT_REPLAY"
            ),
            "anomaly_coefficient": "INVALIDATED_NOT_PROPAGATED",
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
            r"\left.D\bar D\,W_{\rm ext}\right|_{\rm physical\ WW\ schedule}"
            r"\quad\Longrightarrow\quad"
            r"\texttt{PASS\_PHYSICAL\_16\_ROW\_PHASE\_SEQUENCE},",
            "$$",
            "",
            "$$",
            r"\texttt{scope}\prec\texttt{endpoint}\prec\texttt{IBP}"
            r"\prec\texttt{normal\ order}\prec\texttt{projector}"
            r"\prec\texttt{chirality}\prec\texttt{saturation}"
            r"\prec\texttt{collapse}.",
            "$$",
            "",
            "## Specialized row-to-pole binding",
            "",
            "$$",
            r"C_{G}^{\rm D}=-\frac{g^2}{8},\qquad "
            r"C_{G}^{\rm R}=-\frac{g^2}{8},\qquad C_D=-\frac12,",
            "$$",
            "",
            "$$",
            r"C_{\rm row}^{\rm D}=+\frac{g^2}{16},\qquad "
            r"C_{\rm row}^{\rm R}=+\frac{g^2}{16},",
            "$$",
            "",
            "$$",
            r"\operatorname{Pole}\!\left["
            r"\int\frac{d^d\ell}{(2\pi)^d}"
            r"\frac{\ell^\mu\ell^\nu}{(\ell^2+\Delta)^3}\right]"
            r"=\frac{1}{16\pi^2}\frac{\widehat\delta^{\mu\nu}}{4\epsilon},",
            "$$",
            "",
            "$$",
            r"\sum_{r=1}^{8}P_{r}^{\rm D}="
            r"+\frac{g^2}{128\pi^2\epsilon}\widehat\delta^{\mu\nu},\qquad "
            r"\sum_{r=1}^{8}P_{r}^{\rm R}="
            r"+\frac{g^2}{128\pi^2\epsilon}\widehat\delta^{\mu\nu}.",
            "$$",
            "",
            r"Status: \texttt{PASS\_ISOLATED\_TRIANGLE\_16\_ROW\_DRED\_MASTER\_BINDING}; "
            r"generic out-of-scope $D$-words still fail closed.",
            "",
            "$$",
            r"\Gamma_{C,\mathrm{pole}}:\ \texttt{INVALIDATED\_REQUIRES\_TYPED\_CONTACT\_REPLAY},",
            "$$",
            "",
            "$$",
            r"\Gamma_{\rm anomaly}:\ \texttt{INVALIDATED\_NOT\_PROPAGATED}.",
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
