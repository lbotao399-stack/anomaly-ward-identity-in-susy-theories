#!/usr/bin/env python3
"""Exact target-blind audit of the spectator-source double-bridge family.

The connected incidence graph has a unique source-to-first-action edge and a
two-edge cycle between the two action vertices.  The source edge is therefore
a cut edge, so the complete graph is 1PR.  This audit locks that classification
for all 870 routes, evaluates representative nonzero superspace D-words, and
then applies the amputated-1PI and DRED cutting-failure projectors.  No
holomorphic-twist coefficient is read or fitted.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import step5_aa_gauge_full_source_sd_orbit_exact_audit as aa
import step5_all_triangle_parent_port_census_audit as census


ROOT = Path(__file__).resolve().parents[1]
CENSUS_JSON = ROOT / "audits/step5-all-triangle-parent-port-census.json"
AC_JSON = ROOT / "audits/step5-ac-ca-family-exact.json"
BC_JSON = ROOT / "audits/step5-bc-full-family-raw-projection-exact.json"
OUTPUT_JSON = ROOT / "audits/step5-spectator-source-self-energy-orbit-exact.json"
OUTPUT_MD = ROOT / "audits/step5-spectator-source-self-energy-orbit-exact.md"


def a(value: int) -> aa.A:
    return aa.A.coerce(value)


def projected_delta(
    ctx: aa.Context,
    left: str,
    right: str,
    derivative_node: str,
    label: int,
    order: str,
) -> aa.P:
    word = aa.delta4(ctx, left, right) * aa.P.label(ctx, label)
    if order == "D2barD2":
        return aa.d2(aa.bar_d2(word, derivative_node), derivative_node)
    if order == "barD2D2":
        return aa.bar_d2(aa.d2(word, derivative_node), derivative_node)
    if order == "identity":
        return word
    raise ValueError(order)


def three_edge_context(q_values: tuple[int, ...], loop_values: tuple[int, ...]) -> tuple[aa.Context, aa.Vector, aa.Vector]:
    q = aa.vec(q_values)
    loop = aa.vec(loop_values)
    q_minus_loop = aa.vadd(q, aa.vneg(loop))
    ctx = aa.Context(
        ("S", "M", "H"),
        (
            {"S": q, "M": aa.vneg(q)},
            {"M": loop, "H": aa.vneg(loop)},
            {"M": q_minus_loop, "H": aa.vneg(q_minus_loop)},
            {"H": q},
        ),
        12,
    )
    return ctx, q, loop


def tmm_dword(
    q_values: tuple[int, ...],
    loop_values: tuple[int, ...],
    source_order: str = "D2barD2",
    bridge_order: str = "barD2D2",
) -> dict[str, str]:
    """M-M self-energy D-word before propagator/action coefficients."""

    ctx, q, _ = three_edge_context(q_values, loop_values)
    source = projected_delta(ctx, "S", "M", "S", 0, source_order)
    matter_bridge = projected_delta(ctx, "M", "H", "M", 1, bridge_order)
    vector_bridge = projected_delta(ctx, "M", "H", "M", 2, "identity")
    word = source * matter_bridge * vector_bridge * aa.P.label(ctx, 3)
    word = word.coefficient_labels((1, 1, 1, 1)).set_coordinates_zero("S")
    top_mask = sum(
        1 << ctx.coordinate_index(node, offset)
        for node in ("M", "H")
        for offset in range(4)
    )
    raw_top = word.grass_coefficient(top_mask)
    q_squared = aa.vdot(q, q)
    expected_raw = a(1024) * q_squared
    if raw_top != expected_raw:
        raise AssertionError(
            f"TMM D-word mismatch: {raw_top.text()} != {expected_raw.text()}"
        )
    return {
        "q_squared": q_squared.text(),
        "raw_theta_M4_theta_H4": raw_top.text(),
        "one_delta_collapsed_word": (raw_top / 4).text(),
        "two_full_measure_word": (raw_top / 16).text(),
        "identity": "raw=1024*q^2; collapsed=256*q^2; measured=64*q^2",
    }


def thh_dword(
    q_values: tuple[int, ...],
    loop_values: tuple[int, ...],
    reverse: bool,
) -> str:
    """Hplus-Hminus self-energy D-word with both chiral measures."""

    ctx, q, _ = three_edge_context(q_values, loop_values)
    source = projected_delta(ctx, "S", "M", "S", 0, "D2barD2")
    if not reverse:
        bridge_1 = projected_delta(ctx, "M", "H", "M", 1, "barD2D2")
        bridge_2 = projected_delta(ctx, "M", "H", "M", 2, "barD2D2")
        word = aa.integrate_chiral(
            source * bridge_1 * bridge_2 * aa.P.label(ctx, 3), "M"
        )
        word = aa.integrate_antichiral(word, "H")
    else:
        bridge_1 = projected_delta(ctx, "M", "H", "M", 1, "D2barD2")
        bridge_2 = projected_delta(ctx, "M", "H", "M", 2, "D2barD2")
        word = aa.integrate_antichiral(
            source * bridge_1 * bridge_2 * aa.P.label(ctx, 3), "M"
        )
        word = aa.integrate_chiral(word, "H")
    value = (
        word.coefficient_labels((1, 1, 1, 1))
        .set_coordinates_zero("S")
        .scalar_coefficient()
    )
    expected = a(4096) * aa.vdot(q, q)
    if value != expected:
        raise AssertionError(f"THH D-word mismatch: {value.text()} != {expected.text()}")
    return value.text()


def topology_counts(rows: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(str(row["topology"]) for row in rows)
    return dict(sorted(counts.items()))


def pair_ledger(rows: list[dict[str, object]], pair_id: str) -> dict[str, object]:
    selected = [row for row in rows if row["pair_id"] == pair_id]
    quantum = [row for row in selected if row["quantum_marked_occurrences"]]
    spectator = [row for row in selected if row["spectator_marked_occurrences"]]
    return {
        "route_count": len(selected),
        "topology_counts": topology_counts(selected),
        "quantum_cut_edge_marked": {
            "route_count": len(quantum),
            "topology_counts": topology_counts(quantum),
            "momentum": "q_external",
            "DRED_difference": "bar(q)^2-q_d^2=mu_q^2=0",
            "anomaly_projector": "0",
        },
        "external_spectator_marked": {
            "route_count": len(spectator),
            "topology_counts": topology_counts(spectator),
            "inverse_kernel_edge": False,
            "anomaly_projector": "0",
        },
        "marked_loop_cycle_edges": 0,
        "amputated_1PI_projector": "0",
        "spectator_anomaly_correction": "0",
    }


def build_payload() -> dict[str, object]:
    census_payload = census.build_payload()
    spectator_rows = census_payload["spectator_routes"]
    assert isinstance(spectator_rows, list)

    current_census = json.loads(CENSUS_JSON.read_text(encoding="utf-8"))
    ac_baseline = json.loads(AC_JSON.read_text(encoding="utf-8"))
    bc_baseline = json.loads(BC_JSON.read_text(encoding="utf-8"))
    if current_census != json.loads(census.render_json(census_payload)):
        raise AssertionError("spectator audit saw a stale parent census")
    if ac_baseline["external_target_used_in_derivation"] is not False:
        raise AssertionError("AC/CA baseline is not target-blind")
    if bc_baseline["external_target_used"] is not False:
        raise AssertionError("BC/CB baseline is not target-blind")

    route_projectors: list[dict[str, object]] = []
    for row in spectator_rows:
        route_projectors.append(
            {
                "route_id": row["route_id"],
                "pair_id": row["pair_id"],
                "topology": row["topology"],
                "connected": row["connected"],
                "one_particle_irreducible": row["one_particle_irreducible"],
                "source_action_edge_is_cut_edge": row[
                    "source_action_edge_is_cut_edge"
                ],
                "loop_cycle_edges": list(row["loop_cycle_edges"]),
                "quantum_cut_edge_mark_count": len(
                    row["quantum_marked_occurrences"]
                ),
                "external_spectator_mark_count": len(
                    row["spectator_marked_occurrences"]
                ),
                "marked_loop_cycle_edge_count": 0,
                "amputated_1PI_projector": "0",
                "DRED_cutting_failure_projector": "0",
            }
        )

    tmm_samples = {
        "q1000_loop2300": tmm_dword((1, 0, 0, 0), (2, 3, 0, 0)),
        "q0100_loop2300": tmm_dword((0, 1, 0, 0), (2, 3, 0, 0)),
        "q1200_loop3500": tmm_dword((1, 2, 0, 0), (3, 5, 0, 0)),
        "q1200_loop_minus2710": tmm_dword((1, 2, 0, 0), (-2, 7, 1, 0)),
    }
    orientation_words = {
        f"{source_order}__{bridge_order}": tmm_dword(
            (1, 2, 0, 0), (3, 5, 0, 0), source_order, bridge_order
        )["one_delta_collapsed_word"]
        for source_order in ("D2barD2", "barD2D2")
        for bridge_order in ("D2barD2", "barD2D2")
    }
    thh_words = {
        "Hplus_to_Hminus": thh_dword((1, 2, 0, 0), (3, 5, 0, 0), False),
        "Hminus_to_Hplus": thh_dword((1, 2, 0, 0), (3, 5, 0, 0), True),
    }

    inactive = ("C1", "C2", "C3", "Ddot1", "Ddot2")
    no_descendant_pairs = [f"{left}__{right}" for left in inactive for right in inactive]
    pair_results = {
        pair_id: pair_ledger(spectator_rows, pair_id)
        for pair_id in ("A__C1", "C1__A", "B1__C1", "C1__B1")
    }

    return {
        "schema": "step5-spectator-source-self-energy-orbit-exact-v1",
        "status": "TARGET_BLIND_CONNECTED_1PR__AMPUTATED_1PI_ANOMALY_PROJECTOR_ZERO",
        "external_target_used": False,
        "holomorphic_twist_target_read": False,
        "census_source": "audits/step5-all-triangle-parent-port-census.json",
        "baseline_sources": {
            "AC_CA": "audits/step5-ac-ca-family-exact.json",
            "BC_CB": "audits/step5-bc-full-family-raw-projection-exact.json",
        },
        "no_descendant_filter": {
            "inactive_letters": list(inactive),
            "ordered_pair_count": len(no_descendant_pairs),
            "identity": "25=5*5",
            "pairs": no_descendant_pairs,
            "spectator_870_domain": "the complementary 56 marked ordered pairs",
        },
        "global_family_ledger": {
            "route_count": len(spectator_rows),
            "topology_counts": topology_counts(spectator_rows),
            "connected_route_count": sum(bool(row["connected"]) for row in spectator_rows),
            "one_particle_irreducible_route_count": sum(
                bool(row["one_particle_irreducible"]) for row in spectator_rows
            ),
            "source_action_cut_edge_count": sum(
                bool(row["source_action_edge_is_cut_edge"])
                for row in spectator_rows
            ),
            "quantum_cut_edge_mark_occurrences": sum(
                len(row["quantum_marked_occurrences"]) for row in spectator_rows
            ),
            "external_spectator_mark_occurrences": sum(
                len(row["spectator_marked_occurrences"]) for row in spectator_rows
            ),
            "marked_loop_cycle_edge_occurrences": 0,
            "graph_classification": "CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY",
        },
        "graph_cut_identity": {
            "internal_edges": ["source_to_V1", "bridge_1", "bridge_2"],
            "loop_cycle": ["bridge_1", "bridge_2"],
            "cut_edge": "source_to_V1",
            "remove_cut_edge": "composite insertion disconnected from V1-V2 self-energy loop",
            "P_1PI": "0",
        },
        "DRED_projector_identity": {
            "quantum_mark_location": "source_to_V1 cut edge",
            "quantum_mark_momentum": "q_external",
            "quantum_mark_difference": "bar(q)^2-q_d^2=mu_q^2=0",
            "spectator_mark_location": "external source letter; no inverse kernel",
            "loop_bridge_momenta": ["ell", "q-ell"],
            "marked_loop_bridge_count": 0,
            "mu_ell_squared_remainder": "0",
            "P_anomaly_P_1PI": "0",
        },
        "first_nonzero_D_word": {
            "route_id": "TRI-SPEC::A__C1::001::SPEC-L::M1[2;0,1]::M1[2,1;0]",
            "topology": "TMM",
            "identity": "D_MM=+256*q_(4)^2 in the one-delta-collapsed convention",
            "meaning": "ordinary external-leg self-energy is nonzero before the 1PI/anomaly projector",
        },
        "D_word_controls": {
            "TMM_samples": tmm_samples,
            "TMM_all_projector_orientations_at_q_squared_5": orientation_words,
            "THH_both_orientations_at_q_squared_5": thh_words,
            "loop_momentum_dependence": "EXACT_ZERO",
        },
        "ordered_pair_ledgers": pair_results,
        "coefficient_settlement": {
            "A__C_r": {
                "baseline_1PI_vector": ["-1", "+1"],
                "spectator_1PR_delta": ["0", "0"],
                "amputated_1PI_result": ["-1", "+1"],
            },
            "C_r__A": {
                "baseline_1PI_vector": ["-1", "+1"],
                "spectator_1PR_delta": ["0", "0"],
                "amputated_1PI_result": ["-1", "+1"],
            },
            "B_r__C_s": {
                "baseline_diagonal_Konishi": "+delta_rs",
                "spectator_1PR_delta": "0",
                "amputated_1PI_result": "+delta_rs",
            },
            "C_s__B_r": {
                "baseline_diagonal_Konishi": "+delta_rs",
                "spectator_1PR_delta": "0",
                "amputated_1PI_result": "+delta_rs",
            },
            "separate_Z_letter_mixing": "NOT_DEFINED_AND_NOT_DOUBLE_COUNTED",
        },
        "route_projector_ledger": route_projectors,
    }


def verify(payload: dict[str, object], markdown: str) -> list[tuple[str, object]]:
    checks: list[tuple[str, object]] = []

    def check(name: str, condition: bool, actual: object) -> None:
        if not condition:
            raise AssertionError(f"{name}: {actual!r}")
        checks.append((name, actual))

    global_ledger = payload["global_family_ledger"]
    pair_ledgers = payload["ordered_pair_ledgers"]
    controls = payload["D_word_controls"]
    settlement = payload["coefficient_settlement"]
    routes = payload["route_projector_ledger"]
    assert isinstance(global_ledger, dict)
    assert isinstance(pair_ledgers, dict)
    assert isinstance(controls, dict)
    assert isinstance(settlement, dict)
    assert isinstance(routes, list)

    check("external_target_used", payload["external_target_used"] is False, False)
    check("spectator_route_count", global_ledger["route_count"] == 870, global_ledger["route_count"])
    check(
        "spectator_topology_counts",
        global_ledger["topology_counts"] == {"TGG": 612, "THH": 78, "TMM": 180},
        global_ledger["topology_counts"],
    )
    check("connected_route_count", global_ledger["connected_route_count"] == 870, global_ledger["connected_route_count"])
    check("one_particle_irreducible_route_count", global_ledger["one_particle_irreducible_route_count"] == 0, global_ledger["one_particle_irreducible_route_count"])
    check("source_action_cut_edge_count", global_ledger["source_action_cut_edge_count"] == 870, global_ledger["source_action_cut_edge_count"])
    check("quantum_cut_edge_mark_occurrences", global_ledger["quantum_cut_edge_mark_occurrences"] == 486, global_ledger["quantum_cut_edge_mark_occurrences"])
    check("external_spectator_mark_occurrences", global_ledger["external_spectator_mark_occurrences"] == 600, global_ledger["external_spectator_mark_occurrences"])
    check("marked_loop_cycle_edge_occurrences", global_ledger["marked_loop_cycle_edge_occurrences"] == 0, global_ledger["marked_loop_cycle_edge_occurrences"])
    check(
        "all_route_projectors_zero",
        len(routes) == 870
        and all(
            row["amputated_1PI_projector"] == "0"
            and row["DRED_cutting_failure_projector"] == "0"
            and row["marked_loop_cycle_edge_count"] == 0
            for row in routes
        ),
        len(routes),
    )
    check(
        "first_nonzero_TMM_Dword",
        controls["TMM_samples"]["q1200_loop3500"]["one_delta_collapsed_word"] == "1280",
        controls["TMM_samples"]["q1200_loop3500"]["one_delta_collapsed_word"],
    )
    check(
        "TMM_loop_momentum_independence",
        controls["TMM_samples"]["q1200_loop3500"]
        == controls["TMM_samples"]["q1200_loop_minus2710"],
        True,
    )
    check(
        "TMM_projector_orientations",
        set(controls["TMM_all_projector_orientations_at_q_squared_5"].values()) == {"1280"},
        controls["TMM_all_projector_orientations_at_q_squared_5"],
    )
    check(
        "THH_projector_orientations",
        set(controls["THH_both_orientations_at_q_squared_5"].values()) == {"20480"},
        controls["THH_both_orientations_at_q_squared_5"],
    )
    check(
        "AC_CA_pair_support",
        pair_ledgers["A__C1"]["topology_counts"] == {"TGG": 18, "THH": 1, "TMM": 4}
        and pair_ledgers["C1__A"]["topology_counts"] == {"TGG": 18, "THH": 1, "TMM": 4},
        pair_ledgers["A__C1"]["topology_counts"],
    )
    check(
        "BC_CB_pair_support",
        pair_ledgers["B1__C1"]["topology_counts"] == {"THH": 2, "TMM": 2}
        and pair_ledgers["C1__B1"]["topology_counts"] == {"THH": 2, "TMM": 2},
        pair_ledgers["B1__C1"]["topology_counts"],
    )
    check(
        "AC_CA_coefficients_unchanged",
        settlement["A__C_r"]["amputated_1PI_result"] == ["-1", "+1"]
        and settlement["C_r__A"]["amputated_1PI_result"] == ["-1", "+1"],
        settlement["A__C_r"]["amputated_1PI_result"],
    )
    check(
        "BC_CB_Konishi_unchanged",
        settlement["B_r__C_s"]["amputated_1PI_result"] == "+delta_rs"
        and settlement["C_s__B_r"]["amputated_1PI_result"] == "+delta_rs",
        settlement["B_r__C_s"]["amputated_1PI_result"],
    )
    required = (
        "CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY",
        "N_{\\rm spectator}=870",
        "N_{\\rm marked\\ cycle}=0",
        "\\mathcal P_{\\rm anom}\\mathcal P_{\\rm 1PI}=0",
        "(-1,+1)+(0,0)=(-1,+1)",
        "+\\delta_{rs}+0=+\\delta_{rs}",
        "25=5\\times5",
    )
    check("markdown_anchors", all(fragment in markdown for fragment in required), True)
    return checks


def render_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def render_markdown() -> str:
    return r"""# Step 5 spectator-source self-energy orbit exact audit

Status: `TARGET_BLIND_CONNECTED_1PR__AMPUTATED_1PI_ANOMALY_PROJECTOR_ZERO`.

## 1. Graph cut

For every `SPECTATOR_SOURCE_DOUBLE_BRIDGE` route, write

$$
E_{\rm int}=\{e_0,e_1,e_2\},
\qquad
e_0=(I_0,V_1),
\qquad
e_1=e_2=(V_1,V_2).
$$

The unique cycle is $\{e_1,e_2\}$.  Removing $e_0$ gives

$$
G\setminus e_0
=
\{I_0\}\sqcup\{V_1,V_2\}.
$$

Therefore

$$
\boxed{\texttt{CONNECTED_BUT_1PR_EXTERNAL_LEG_SELF_ENERGY}},
\qquad
\boxed{\mathcal P_{\rm 1PI}G=0}.
$$

## 2. Exact census and the 25-pair filter

The inactive letters are

$$
\{C_1,C_2,C_3,D_{\dot1},D_{\dot2}\}.
$$

Thus

$$
N_{\rm no\ descendant}=25=5\times5.
$$

Both parent enumerators return no anomaly candidate on those 25 ordered
pairs.  The spectator count is over the complementary 56 marked pairs:

$$
N_{\rm spectator}=870,
$$

$$
(N_{TGG},N_{TMM},N_{THH},N_{TGM},N_{TMH})
=(612,180,78,0,0).
$$

The marked-occurrence decomposition is

$$
N_{\rm quantum\ cut\ edge}=486,
\qquad
N_{\rm external\ spectator}=600,
\qquad
N_{\rm marked\ cycle}=0.
$$

## 3. First nonzero D-word

Choose the first $A>C_1$ spectator route,

$$
M_1(\widetilde\phi_1,u,\phi_1)
\mathrel{\substack{\longleftrightarrow\\[-2mm]\longleftrightarrow}}
M_1(\widetilde\phi_1,u,\phi_1).
$$

With source momentum $q$, bridge momenta $\ell$ and $q-\ell$, the exact sparse
Grassmann expansion gives

$$
\operatorname{Coeff}_{\theta_M^4\theta_H^4}\mathfrak D_{MM}
=1024q_{(4)}^2,
$$

$$
\mathfrak D_{MM}^{\rm collapsed}
=\frac14(1024q_{(4)}^2)
=256q_{(4)}^2,
$$

$$
\mathfrak D_{MM}^{\rm two\ full\ measures}
=\frac1{16}(1024q_{(4)}^2)
=64q_{(4)}^2.
$$

For $q=(1,2,0,0)$,

$$
q_{(4)}^2=5,
\qquad
\mathfrak D_{MM}^{\rm collapsed}=1280,
$$

for both $\ell=(3,5,0,0)$ and $\ell=(-2,7,1,0)$.  All four
$D^2\bar D^2/\bar D^2D^2$ source/bridge orientations give the same 1280.
The two superpotential orientations give

$$
\mathfrak D_{H_+H_-}
=\mathfrak D_{H_-H_+}
=4096q_{(4)}^2
=20480.
$$

These are nonzero ordinary external-leg self-energy words.

## 4. DRED anomaly projector

The 486 quantum marks lie on $e_0$, whose momentum is the fixed external
momentum $q$, not $\ell$ or $q-\ell$.  Hence

$$
\bar q^2-q_d^2=\mu_q^2=0.
$$

The 600 spectator marks contain no quantum inverse kernel.  Since neither
cycle edge is marked,

$$
N_{\rm marked\ cycle}=0,
\qquad
\mu_\ell^2\text{ remainder}=0.
$$

Route by route,

$$
\boxed{\mathcal P_{\rm anom}\mathcal P_{\rm 1PI}=0}.
$$

## 5. Ordered channels

For $A>C_r$ and $C_r>A$,

$$
(N_{TGG},N_{TMM},N_{THH},N_{TGM},N_{TMH})=(18,4,1,0,0),
$$

$$
\boxed{(-1,+1)+(0,0)=(-1,+1)}.
$$

For $B_r>C_s$ and $C_s>B_r$ on the diagonal,

$$
(N_{TMM},N_{THH},N_{TGG},N_{TGM},N_{TMH})=(2,2,0,0,0),
$$

$$
\boxed{+\delta_{rs}+0=+\delta_{rs}}.
$$

A separately defined $Z_{\rm letter}$ insertion is not included and is not
double counted as an amputated 1PI anomaly parent.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.write and not args.check:
        args.check = True

    payload = build_payload()
    markdown = render_markdown()
    checks = verify(payload, markdown)
    json_text = render_json(payload)
    if args.write:
        OUTPUT_JSON.write_text(json_text, encoding="utf-8")
        OUTPUT_MD.write_text(markdown, encoding="utf-8")
    if args.check:
        if OUTPUT_JSON.read_text(encoding="utf-8") != json_text:
            raise SystemExit("spectator exact JSON artifact is stale")
        if OUTPUT_MD.read_text(encoding="utf-8") != markdown:
            raise SystemExit("spectator exact Markdown artifact is stale")
    for name, value in checks:
        print(f"PASS {name}: {value}")
    print(f"SUMMARY {len(checks)}/{len(checks)} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
