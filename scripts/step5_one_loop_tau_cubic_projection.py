#!/usr/bin/env python3
"""Exact feasibility certificate for the cubic open-tau one-loop projection.

The target is the unique raw DRED N=3 spurion word

    K^(AB)_(C[DE]) tau_(ab dotc dotd)
    W_c^C Wtilde^(D dotc) Wtilde^(E dotd),

symmetrized in (a,b,c).  This module enumerates all 26 polarized rooted
one-loop families at background order three and audits the executable Project
grammar needed to project them.  It fail-closes before amplitudes because the
current grammar has neither H_3 nor I_3 and has no open symmetric-traceless
tau projector.  No zero, nonzero, pole, or anomaly coefficient is inferred.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import inspect
import json
from math import prod
from pathlib import Path
import sys
from typing import get_args


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_dalgebra_compiler import (  # noqa: E402
    Collapse,
    Token,
    compile_scheduled_ww_rows,
)
from scripts.step5_one_loop_dred_evanescent_jets import (  # noqa: E402
    build_payload as build_dred_payload,
)
from scripts.step5_one_loop_hessian_insertion_census import (  # noqa: E402
    counterterm_rows,
    hessian_compositions,
    labeled_term_rows,
)
from scripts.step5_one_loop_n2_physical_hessian_family import (  # noqa: E402
    action_hessian_branches,
    source_kernel_branches,
)
from scripts.step5_project_composites import (  # noqa: E402
    insertion_terms_at_valence,
)
from scripts.step5_vertex_grammar import build_project_vertex_grammar  # noqa: E402


GENERATED = ROOT / "generated/step5/one-loop-tau-cubic-projection.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-tau-cubic-projection-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-tau-cubic-projection.md"


def exact_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def family_name(s: int, r_parts: tuple[int, ...]) -> str:
    suffix = "_".join(f"H{order}" for order in r_parts)
    return f"I{s}" + (f"_{suffix}" if suffix else "")


def topology(k: int) -> str:
    return {
        0: "INSERTION_TADPOLE",
        1: "CONTACT_BUBBLE",
        2: "ROOTED_TRIANGLE",
        3: "ROOTED_BOX",
    }[k]


def current_project_kernel_registry() -> dict[str, object]:
    source_counts = {order: len(source_kernel_branches(order)) for order in (0, 1, 2)}
    vector_hessian_counts = {
        order: sum(row["block_id"] == "V" for row in action_hessian_branches(order))
        for order in (1, 2)
    }

    insertion5_error: str | None = None
    try:
        insertion_terms_at_valence(5)
    except ValueError as error:
        insertion5_error = str(error)

    grammar = build_project_vertex_grammar()
    all_vector_action_monomials = [
        monomial
        for monomial in grammar.action_monomials
        if monomial.ordered_fields
        and all(field.field_name == "V" for field in monomial.ordered_fields)
    ]
    action_valence_counts = Counter(
        len(monomial.ordered_fields) for monomial in all_vector_action_monomials
    )
    field_strength_degrees = sorted(
        {term.degree_in_v for term in grammar.field_strength_terms}
    )
    connection_degrees = sorted({term.degree_in_v for term in grammar.connection_terms})

    return {
        "source_branch_counts": {
            f"I{order}": count for order, count in source_counts.items()
        },
        "vector_hessian_branch_counts": {
            f"H{order}": count for order, count in vector_hessian_counts.items()
        },
        "source_available_orders": [0, 1, 2],
        "hessian_available_orders": [1, 2],
        "I3": {
            "required_composite_valence": 5,
            "status": "BLOCKED_MISSING_PROJECT_I5_COMPOSITE_GRAMMAR",
            "direct_constructor_error": insertion5_error,
        },
        "H3": {
            "required_action_valence": 5,
            "current_all_vector_action_monomials_by_valence": {
                str(valence): action_valence_counts[valence]
                for valence in sorted(action_valence_counts)
            },
            "current_valence_five_monomial_count": action_valence_counts[5],
            "status": "BLOCKED_MISSING_PROJECT_QUINTIC_GAUGE_ACTION_GRAMMAR",
        },
        "current_connection_degrees": connection_degrees,
        "current_field_strength_degrees": field_strength_degrees,
        "minimal_degree_extension_for_H3_and_I3": {
            "Gamma": 4,
            "TildeGamma": 4,
            "W": 4,
            "TildeW": 4,
            "X": 4,
            "gauge_action_total_V_valence": 5,
            "source_insertion_total_V_valence": 5,
        },
    }


def rooted_family_census(registry: dict[str, object]) -> dict[str, object]:
    source_counts = {
        int(key[1:]): int(value)
        for key, value in registry["source_branch_counts"].items()  # type: ignore[union-attr]
    }
    hessian_counts = {
        int(key[1:]): int(value)
        for key, value in registry["vector_hessian_branch_counts"].items()  # type: ignore[union-attr]
    }
    polarized = labeled_term_rows(3)
    aggregate: list[dict[str, object]] = []
    polarized_rows: list[dict[str, object]] = []
    available_polarized_count = 0
    available_branch_path_count = 0

    for s, r_parts in hessian_compositions(3):
        r_tuple = tuple(r_parts)
        selected = [
            row
            for row in polarized
            if int(row["s"]) == s and tuple(row["r_parts"]) == r_tuple
        ]
        missing = ([] if s in source_counts else [f"I{s}"]) + [
            f"H{order}" for order in r_tuple if order not in hessian_counts
        ]
        per_polarized_branch_count: int | None = None
        if not missing:
            per_polarized_branch_count = source_counts[s] * prod(
                hessian_counts[order] for order in r_tuple
            )
            available_polarized_count += len(selected)
            available_branch_path_count += len(selected) * per_polarized_branch_count

        aggregate.append(
            {
                "family": family_name(s, r_tuple),
                "s": s,
                "r_parts": list(r_tuple),
                "k": len(r_tuple),
                "coefficient": exact_fraction(Fraction((-1) ** len(r_tuple), 2)),
                "topology": topology(len(r_tuple)),
                "polarized_row_count": len(selected),
                "required_kernels": [f"I{s}", *[f"H{order}" for order in r_tuple]],
                "missing_kernels": missing,
                "per_polarized_vector_branch_path_count": per_polarized_branch_count,
                "total_vector_branch_path_count": (
                    None
                    if per_polarized_branch_count is None
                    else len(selected) * per_polarized_branch_count
                ),
                "status": (
                    "KERNEL_BRANCH_GRAMMAR_AVAILABLE_PROJECTOR_NOT_AVAILABLE"
                    if not missing
                    else "BLOCKED_MISSING_KERNEL_GRAMMAR"
                ),
            }
        )

        for row in selected:
            polarized_rows.append(
                {
                    "term_id": row["term_id"],
                    "family": family_name(s, r_tuple),
                    "s": s,
                    "r_parts": list(r_tuple),
                    "k": len(r_tuple),
                    "coefficient": exact_fraction(Fraction((-1) ** len(r_tuple), 2)),
                    "insertion_background_labels": row["insertion_background_labels"],
                    "hessian_background_label_blocks": row[
                        "hessian_background_label_blocks"
                    ],
                    "missing_kernels": missing,
                    "vector_branch_path_count": per_polarized_branch_count,
                    "projection_status": (
                        "BLOCKED_OPEN_TAU_PROJECTOR"
                        if not missing
                        else "BLOCKED_MISSING_KERNEL_GRAMMAR"
                    ),
                }
            )

    return {
        "background_order": 3,
        "unpolarized_family_count": len(aggregate),
        "polarized_rooted_row_count": len(polarized_rows),
        "families": aggregate,
        "polarized_rows": polarized_rows,
        "kernel_branch_available_polarized_rows": available_polarized_count,
        "kernel_branch_blocked_polarized_rows": len(polarized_rows)
        - available_polarized_count,
        "available_vector_branch_path_count": available_branch_path_count,
    }


def target_and_projector_gate() -> dict[str, object]:
    dred = build_dred_payload()
    tau = dred["raw_traceless_tau_census"]
    witness = tau["explicit_N3_witness"]
    token_names = sorted(token.__name__ for token in get_args(Token))
    scheduled_source = inspect.getsource(compile_scheduled_ww_rows)
    triangle_only = (
        "graph.cycle_rank() != 1" in scheduled_source
        and "len(graph.vertices) != 3" in scheduled_source
        and "len(graph.internal_edges) != 3" in scheduled_source
    )
    color_gate = dred["Project_cross_certificates"]["source_color"]
    contracted = dred["contracted_endpoint_subledger"]

    return {
        "operator": witness["operator"],
        "source_pairing": witness["source_pairing"],
        "dimension": witness["dimension"],
        "spin4": "(3/2,0)",
        "parity": witness["parity"],
        "formal_r": witness["formal_r"],
        "tau_target_multiplicity_at_N3": witness["tau_target_multiplicity"],
        "physical_target_multiplicity_at_N3": witness["physical_target_multiplicity"],
        "color_carrier": witness["color_carrier"],
        "SU2_nonzero_component": witness["color_certificate"][
            "SU2_AB00_C0_full_DE_contraction"
        ],
        "raw_DRED_background_space": {
            "status": "ADMITTED_AS_REGULATOR_COEFFICIENT_SPURION_NOT_AS_NEW_BACKGROUND_FIELD",
            "background_fields": ["W", "TildeW"],
            "coefficient_spurion": "tau=tilde_delta-(epsilon/2)delta_(4)",
            "background_CE_covariant_submodule": dred["verdict"][
                "background_CE_covariant_submodule_injectivity"
            ],
            "full_quantum_BV_class": dred["verdict"][
                "full_quantum_BV_cohomology_class_of_witness"
            ],
        },
        "physical_4d_quotient": {
            "q4d_tau": "0",
            "q4d_E_tau": "0",
            "physical_4d_coefficient_reported": False,
        },
        "executable_projector": {
            "full_tau_projector_matrix_built": tau[
                "full_index_placement_projector_matrix_built"
            ],
            "open_tau_placements_in_contracted_ledger": contracted[
                "open_traceless_tau_placements_included"
            ],
            "D_algebra_token_types": token_names,
            "tau_tensor_token_present": any(
                "tau" in token_name.lower() for token_name in token_names
            ),
            "generic_collapse_token_present": Collapse.__name__ in token_names,
            "scheduled_WW_compiler_is_triangle_only": triangle_only,
            "rank_five_color_projection_covered": color_gate[
                "tau_rank_five_color_map_covered"
            ],
            "status": "BLOCKED_MISSING_OPEN_TAU_SPIN_COLOR_PROJECTOR",
        },
    }


def counterterm_gate() -> dict[str, object]:
    row = next(item for item in counterterm_rows() if item["counterterm_id"] == "CT_3")
    return {
        "abstract_row": row,
        "bare_loop_pole_requires_CT3": False,
        "renormalized_local_coefficient_requires_CT3": True,
        "status": "BLOCKED_UNRESOLVED_CT3_ONLY_AFTER_BARE_LOOP_PROJECTION",
    }


def build_payload() -> dict[str, object]:
    registry = current_project_kernel_registry()
    census = rooted_family_census(registry)
    target = target_and_projector_gate()
    ct3 = counterterm_gate()

    checks = {
        "eight_unpolarized_families": census["unpolarized_family_count"] == 8,
        "twenty_six_polarized_rows": census["polarized_rooted_row_count"] == 26,
        "family_partition_is_1_3_3_6_3_6_3_1": [
            row["polarized_row_count"] for row in census["families"]
        ]
        == [1, 3, 3, 6, 3, 6, 3, 1],
        "neumann_coefficients_are_exact": [
            row["coefficient"] for row in census["families"]
        ]
        == [
            exact_fraction(Fraction(-1, 2)),
            exact_fraction(Fraction(1, 2)),
            exact_fraction(Fraction(1, 2)),
            exact_fraction(Fraction(-1, 2)),
            exact_fraction(Fraction(-1, 2)),
            exact_fraction(Fraction(1, 2)),
            exact_fraction(Fraction(-1, 2)),
            exact_fraction(Fraction(1, 2)),
        ],
        "current_source_counts_are_4_60_720": registry["source_branch_counts"]
        == {"I0": 4, "I1": 60, "I2": 720},
        "current_vector_hessian_counts_are_24_144": registry[
            "vector_hessian_branch_counts"
        ]
        == {"H1": 24, "H2": 144},
        "exactly_H3_and_I3_kernel_families_are_missing": [
            row["family"] for row in census["families"] if row["missing_kernels"]
        ]
        == ["I0_H3", "I3"],
        "twenty_four_rows_have_existing_kernel_branches": census[
            "kernel_branch_available_polarized_rows"
        ]
        == 24,
        "available_branch_path_sum_is_699840": census[
            "available_vector_branch_path_count"
        ]
        == 699_840,
        "H3_is_absent_not_typed_zero": registry["H3"][
            "current_valence_five_monomial_count"
        ]
        == 0
        and registry["H3"]["status"].startswith("BLOCKED_MISSING"),
        "I3_constructor_fail_closes": registry["I3"]["direct_constructor_error"]
        == "the seed insertion grammar is I2, I3, I4",
        "raw_tau_target_is_nonzero_but_physical_quotient_is_zero": target[
            "tau_target_multiplicity_at_N3"
        ]
        == 1
        and target["physical_target_multiplicity_at_N3"] == 0
        and target["physical_4d_quotient"]["q4d_E_tau"] == "0",
        "open_tau_projector_and_rank_five_color_projection_are_missing": not target[
            "executable_projector"
        ]["tau_tensor_token_present"]
        and not target["executable_projector"]["rank_five_color_projection_covered"],
        "scheduled_compiler_is_triangle_only": target["executable_projector"][
            "scheduled_WW_compiler_is_triangle_only"
        ],
        "CT3_is_separated_from_bare_loop_pole": not ct3["bare_loop_pole_requires_CT3"]
        and ct3["renormalized_local_coefficient_requires_CT3"],
    }

    gaps = [
        {
            "gap_id": "G1[G-DEF]",
            "severity": "P0",
            "location": "Project gauge-action Hessian at background order three",
            "claim": "the I0_H3 rooted family is instantiated",
            "missing": "Gamma_4, TildeGamma_4, W_4, TildeW_4 and total-V-valence-five gauge kinetic monomials",
            "minimal_repair": "derive the quintic Project gauge action and its ordered VV Hessian H3",
        },
        {
            "gap_id": "G2[G-DEF]",
            "severity": "P0",
            "location": "Project source Hessian at background order three",
            "claim": "the I3 rooted family is instantiated",
            "missing": "X_4 and the valence-five expansion of nabla_-(X^A X^B)",
            "minimal_repair": "derive I_(5) and its three-background two-quantum ordered Hessian branches",
        },
        {
            "gap_id": "G3[G-PROJ]",
            "severity": "P0",
            "location": "DRED D-algebra target projection",
            "claim": "all 26 rows can be projected onto E_tau",
            "missing": "an open symmetric-traceless tau token, spin-(3/2,0) symmetrizer, and K^(AB)_(C[DE]) color projector",
            "minimal_repair": "add the typed spin-color projector without replacing tau by a closed scalar trace",
        },
        {
            "gap_id": "G4[G-OP]",
            "severity": "P0",
            "location": "n=3 GraphIR and D-algebra compiler",
            "claim": "box, contact, and pinch descendants have exact routings and signs",
            "missing": "26 physical GraphIRs, generalized cycle schedules, and a typed pinch-to-descendant map",
            "minimal_repair": "compile every polarized row before any family sum",
        },
        {
            "gap_id": "G5[G-PROJ]",
            "severity": "P0",
            "location": "open-rank DRED tensor integral",
            "claim": "a UV-local E_tau pole has been extracted",
            "missing": "a tensor-pole reducer retaining the open tau channel across the complete rooted/contact orbit",
            "minimal_repair": "reduce the exact routed numerators only after G1-G4 close",
        },
        {
            "gap_id": "G6[G-NORM]",
            "severity": "P1",
            "location": "CT3",
            "claim": "the renormalized cubic coefficient is fixed",
            "missing": "the local CT3 basis, coefficient, and renormalization condition",
            "minimal_repair": "derive CT3 after the bare loop pole; CT3 does not block the bare loop projection",
        },
    ]

    return {
        "schema": "Step5OneLoopTauCubicProjection.v1",
        "status": (
            "BLOCKED_MISSING_COMPLETE_N3_PROJECT_GRAMMAR"
            if all(checks.values())
            else "FAIL_CERTIFICATE_INCONSISTENT"
        ),
        "scope": "FIXED_VECTOR_FRAME_PURE_GAUGE_STEP5A_BACKGROUND_ORDER_N3",
        "target": target,
        "formal_rooted_expansion": (
            "Gamma_(J,3)^(1)=(1/2) sum_(s+sum r_j=3) "
            "(-1)^k STr[I_s G0 H_r1 G0 ... H_rk G0]+CT3"
        ),
        "kernel_registry": registry,
        "rooted_family_census": census,
        "counterterm_gate": ct3,
        "pinch_gate": {
            "generic_collapse_token_exists": target["executable_projector"][
                "generic_collapse_token_present"
            ],
            "n3_pinch_generation_exists": False,
            "status": "BLOCKED_MISSING_N3_EDGE_TAGGED_PINCH_ORBIT",
        },
        "coefficient_boundary": {
            "preintegration_amplitude": "NOT_CONSTRUCTED",
            "bare_UV_local_pole": "NOT_COMPUTED",
            "raw_DRED_E_tau_zero_or_nonzero": "NOT_DERIVED",
            "physical_4d_projection": "q4d(E_tau)=0",
            "renormalized_coefficient": "NOT_DEFINED_WITHOUT_CT3",
            "coefficient_accepted": False,
        },
        "gaps": gaps,
        "checks": checks,
        "external_result_imported": False,
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def render_markdown(payload: dict[str, object]) -> str:
    families = payload["rooted_family_census"]["families"]
    rows = "\n".join(
        "{}&{}&{}&{}&{}&{}\\\\".format(
            row["family"].replace("_", r"\,"),
            row["polarized_row_count"],
            row["k"],
            ("+" if row["coefficient"]["numerator"] > 0 else "-") + r"\frac12",
            (
                row["total_vector_branch_path_count"]
                if row["total_vector_branch_path_count"] is not None
                else r"\texttt{BLOCKED}"
            ),
            (
                r"\texttt{KERNEL\ READY}"
                if not row["missing_kernels"]
                else r"\texttt{MISSING\ }" + ",".join(row["missing_kernels"])
            ),
        )
        for row in families
    )
    return rf"""# Step 5A cubic open-$\tau$ projection feasibility

## 0. Status

$$
\boxed{{
\mathsf{{C}}_{{\tau,3}}
=\texttt{{BLOCKED\_MISSING\_COMPLETE\_N3\_PROJECT\_GRAMMAR}}
}}
$$

$$
\mathcal A_{{\tau,3}}^{{\rm pre}}
=\Gamma_{{\tau,3}}^{{\rm pole}}
=\texttt{{NOT\ COMPUTED}}.
$$

## 1. Target

$$
\mathscr E_{{abc}}^{{AB}}
=K^{{AB}}{{}}_{{C[DE]}}
\tau_{{(ab|\dot c\dot d|}}
W_{{c)}}^C
\widetilde W^{{D\dot c}}
\widetilde W^{{E\dot d}},
$$

$$
K^{{AB}}{{}}_{{C[DE]}}
=\delta^A{{}}_C c_{{DE}}{{}}^B
+\delta^B{{}}_C c_{{DE}}{{}}^A.
$$

$$
N_{{\tau,N=3}}=1,
\qquad
N_{{\mathrm{{physical}},N=3}}=0.
$$

$$
K^{{00}}{{}}_{{0[DE]}}B^{{DE}}=4B^{{12}}\ne0.
$$

The fields are $W,\widetilde W$; $\tau$ is a DRED coefficient spurion, not a
new background field.

$$
\mathscr E_\tau\in\mathcal V_{{\rm DRED,raw}}^{{\rm CE}},
\qquad
q_{{4d}}(\tau)=0,
\qquad
q_{{4d}}(\mathscr E_\tau)=0.
$$

## 2. Complete rooted census

$$
\Gamma_{{J,3}}^{{(1)}}
=\frac12
\sum_{{s+\sum_jr_j=3}}
(-1)^k\operatorname{{STr}}
\left[I_sG_0H_{{r_1}}G_0\cdots H_{{r_k}}G_0\right]
+\mathrm{{CT}}_3.
$$

$$
N_{{\rm family}}=8,
\qquad
N_{{\rm polarized}}=26.
$$

$$
\begin{{array}}{{c|c|c|c|c|c}}
\text{{family}}&N_{{\rm pol}}&k&\text{{coefficient}}&N_{{\rm branch}}&\text{{gate}}\\ \hline
{rows}
\end{{array}}
$$

$$
N_{{\rm kernel\ ready\ rows}}=24,
\qquad
N_{{\rm kernel\ blocked\ rows}}=2,
$$

$$
N_{{\rm available\ vector\ branch\ paths}}
=699840.
$$

## 3. Missing kernels

$$
N(H_1^{{VV}})=24,
\qquad
N(H_2^{{VV}})=144,
\qquad
N(H_3^{{VV}})=\texttt{{BLOCKED}}.
$$

$$
\deg_V(\Gamma,W,\widetilde\Gamma,\widetilde W)\in\{{1,2,3\}},
\qquad
[V^5]S_{{\rm gauge}}=\texttt{{ABSENT\ FROM\ GRAMMAR}}.
$$

$$
N(I_0)=4,
\qquad
N(I_1)=60,
\qquad
N(I_2)=720,
\qquad
N(I_3)=\texttt{{BLOCKED}}.
$$

$$
I_3
=\left[V_{{\rm B}}^3v^2\right]
\nabla_-\left(X^AX^B\right)
=I_{{(5)}}[V_{{\rm B}}^3,v,v],
$$

$$
I_{{(5)}}=\texttt{{ABSENT\ FROM\ GRAMMAR}}.
$$

## 4. Missing projection

$$
P_\tau:
\mathcal A_{{J,3}}
\longrightarrow
K^{{AB}}{{}}_{{C[DE]}}
\tau_{{(ab|\dot c\dot d|}}
W_{{c)}}^C\widetilde W^{{D\dot c}}\widetilde W^{{E\dot d}}
$$

is not an executable Project map.

$$
\texttt{{tau\ token}}=0,
\qquad
\texttt{{rank-five\ color\ projector}}=0,
\qquad
\texttt{{n=3\ pinch\ orbit}}=0.
$$

The scheduled compiler requires

$$
N_{{\rm vertex}}=N_{{\rm edge}}=3,
$$

so it rejects the $k=3$ box and every $n=3$ contact topology.

## 5. Counterterm boundary

$$
\Gamma_{{J,3}}^{{\rm ren}}
=\Gamma_{{J,3}}^{{\rm loop}}+\mathrm{{CT}}_3.
$$

$$
\Gamma_{{J,3}}^{{\rm loop,pole}}
\text{{ does not require }}\mathrm{{CT}}_3,
\qquad
\Gamma_{{J,3}}^{{\rm ren}}
\text{{ requires }}\mathrm{{CT}}_3.
$$

$$
\mathrm{{CT}}_3=\texttt{{UNRESOLVED}}.
$$

## 6. Exact checks

$$
1+3+3+6+3+6+3+1=26.
$$

$$
\begin{{aligned}}
N_{{\rm available}}
={{}}&3(4\cdot24\cdot144)
+3(4\cdot144\cdot24)
+6(4\cdot24^3)\\
&+3(60\cdot144)
+6(60\cdot24^2)
+3(720\cdot24)\\
={{}}&41472+41472+331776+25920+207360+51840\\
={{}}&699840.
\end{{aligned}}
$$

## 7. Gap table

$$
\begin{{array}}{{c|c|c|c}}
\text{{gap}}&\text{{type}}&\text{{missing object}}&\text{{severity}}\\ \hline
G1&\mathrm{{G\!\!-DEF}}&H_3&P0\\
G2&\mathrm{{G\!\!-DEF}}&I_3&P0\\
G3&\mathrm{{G\!\!-PROJ}}&P_\tau\ \text{{and }}P_K&P0\\
G4&\mathrm{{G\!\!-OP}}&26\ \mathrm{{GraphIRs}}\ \text{{and pinch orbit}}&P0\\
G5&\mathrm{{G\!\!-PROJ}}&\text{{open-rank DRED pole reducer}}&P0\\
G6&\mathrm{{G\!\!-NORM}}&\mathrm{{CT}}_3&P1
\end{{array}}
$$

## 8. Result

$$
\boxed{{
\mathsf C_{{\tau,3}}^{{\rm raw\ DRED}}
=\texttt{{NOT\ DERIVED}},
\qquad
q_{{4d}}(\mathscr E_\tau)=0.
}}
$$
"""


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    checks = payload["checks"]
    audit = {
        "schema": "Step5OneLoopTauCubicProjectionVerification.v1",
        "status": "PASS_FAIL_CLOSED_FEASIBILITY_CERTIFICATE"
        if all(checks.values())
        else "FAIL",
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "check_count": len(checks),
        "passed_count": sum(bool(value) for value in checks.values()),
        "checks": checks,
        "preintegration_amplitude_computed": False,
        "UV_local_pole_computed": False,
        "coefficient_accepted": False,
    }
    GENERATED.write_bytes(generated_bytes)
    AUDIT_JSON.write_bytes(canonical_json(audit))
    AUDIT_MD.write_text(render_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    write_artifacts()
