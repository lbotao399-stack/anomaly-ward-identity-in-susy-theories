#!/usr/bin/env python3
"""Cross-review the complete Step-5 evanescent projector sector."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
WW_PATH = ROOT / "audits" / "step5-ww-physical-cut-pole.json"
MIX_PATH = ROOT / "audits" / "step5-local-operator-mixing.json"
Q_LIFT_PATH = ROOT / "audits" / "step5-q-equivariant-graph-lift.json"
DRED_PATH = ROOT / "audits" / "step5-dred-epsilon-scalar-mixing.json"
JSON_OUT = ROOT / "audits" / "step5-evanescent-closure-review.json"
MD_OUT = ROOT / "audits" / "step5-evanescent-closure-review.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    ww = load(WW_PATH)
    mix = load(MIX_PATH)
    q_lift = load(Q_LIFT_PATH)
    dred = load(DRED_PATH)

    ww_blocker_ids = {row["id"] for row in ww["exact_blockers"]}
    mix_blockers = {row["id"] for row in mix["blockers"]}
    q3 = next(
        row
        for row in mix["ordered_open_color_space"]["q_complex_rref"]
        if row["degree"] == 3
    )
    genuine_rows = dred["minimal_projector_split"]["rows"]

    checks = [
        {
            "id": "WW_SINGLE_BREVE_THREE_SIGMA_CHAIN",
            "pass": ww["result"]["breve_contraction"]
            == "brevedelta^mu nu*T_mu rho nu*p^rho=-2*epsilon*sigma_rho*p^rho",
        },
        {
            "id": "WW_BARE_METRIC_MISMATCH_FIXED",
            "pass": ww["result"]["metric_sum"].startswith("-hbar*g^2/(32*pi^2*epsilon)"),
        },
        {
            "id": "WW_RENORMALIZED_MIXING_EXPLICITLY_BLOCKED",
            "pass": "BLOCKED_RENORMALIZED_COMPOSITE_MIXING" in ww_blocker_ids,
        },
        {
            "id": "PHYSICAL_Q_KERNEL_ONE_DIMENSIONAL",
            "pass": q3["rank"] == 19 and q3["joint_kernel_dimension"] == 1,
        },
        {
            "id": "GLOBAL_CUT_CENSUS_NOT_COMPLETE",
            "pass": q_lift["status"] == "BLOCKED_RAW_GRAPH_Q_EQUIVARIANT_LIFT",
        },
        {
            "id": "GLOBAL_CENSUS_MIXING_BLOCKER_PRESENT",
            "pass": "BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX" in mix_blockers,
        },
        {
            "id": "COMPLETE_MINIMAL_PROJECTOR_SPLIT_EIGHT_ROWS",
            "pass": dred["minimal_projector_split"]["projector_evanescent_piece_count"] == 8
            and len(genuine_rows) == 8
            and len([row for row in genuine_rows if row["family"] == "DA"]) == 5
            and len([row for row in genuine_rows if row["family"] == "BC"]) == 3,
        },
        {
            "id": "MIXED_HAT_BREVE_ROW_INCLUDED",
            "pass": any(row["id"] == "E_DA_h_hb" for row in genuine_rows),
        },
        {
            "id": "DOUBLE_BREVE_ENUMERATED_DELTA_CLASSES_ZERO",
            "pass": set(dred["A_bb_enumerated_delta_zero"]["scope"])
            == {
                "CHI_TADPOLE",
                "A_HAT_CHICHI_DIRECT",
                "A_HAT_CHICHI_EXCHANGE",
            }
            and dred["A_bb_enumerated_delta_zero"]["full_row_status"]
            == "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES",
        },
        {
            "id": "CONDITIONAL_EIGHT_PROJECTOR_ROWS_MS_POLE_MIXING_ZERO",
            "pass": "=0 for u in the eight-row" in dred["one_loop_pole_vs_finite"]["MS_mixing"],
        },
        {
            "id": "FINITE_MIXED_COEFFICIENT_BLOCKED",
            "pass": dred["status"] == "BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES",
        },
        {
            "id": "NO_DOUBLE_COUNT_RETAINS_ORIGIN_BOUNDARY",
            "pass": "origin_id" in dred["no_double_count"]["rule"]
            and "provenance" in dred["no_double_count"]["boundary"],
        },
    ]

    status = "BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES"
    audit = {
        "schema": "awi.step5.evanescent-closure-review.v2",
        "status": status,
        "authority_role": "CROSS_REVIEW_OF_LOCAL_PROPOSALS_USING_VERIFIED_ORIGIN_MAIN_FOUNDATION",
        "inputs": [
            {"path": str(WW_PATH.relative_to(ROOT)), "sha256": digest(WW_PATH)},
            {"path": str(MIX_PATH.relative_to(ROOT)), "sha256": digest(MIX_PATH)},
            {"path": str(Q_LIFT_PATH.relative_to(ROOT)), "sha256": digest(Q_LIFT_PATH)},
            {"path": str(DRED_PATH.relative_to(ROOT)), "sha256": digest(DRED_PATH)},
        ],
        "checked_scope": {
            "bare_WW_rank_two_projection": "ONLY_TRIVIAL_-2epsilon_TIMES_THE_FIXED_WW_WORD",
            "all_channel_physical_q_image": "ONE_DIMENSIONAL_IF_REGULATED_Q_INTERTWINING_IS_PROVED",
            "complete_minimal_projector_split": "FIVE_DA_PLUS_THREE_BC_ROWS_WITH_Q_DESCENDANTS",
            "one_loop_MS_pole_mixing_eight_rows": "CONDITIONAL_z_EuO_MS=0_AFTER_UV_IR_SEPARATION_SIMPLE_POLE_AND_NO_INVERSE_N_EPSILON_FOR_THE_DISPLAYED_COMPONENT_ROWS",
            "double_breve_DA_row": "THREE_ENUMERATED_DELTA_IJ_CONTRACTION_CLASSES_ZERO__FULL_ROW_BLOCKED",
        },
        "not_proved_scope": {
            "local_evanescent_kernel": "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS",
            "finite_mixed_coefficient": "the three mixed I_[0] triangle traces and G1-G3 contact/bubble traces are not numerically evaluated",
            "all_channel_cut_exhaustion": "raw port-preserving q-equivariant graph lift remains BLOCKED",
            "full_superspace_origin_link": "the graph IR has not yet proved that each explicit epsilon-scalar realization and WW complement share one origin_id",
            "complete_BV_DRED_evanescent_basis": "ghost, NK, measure, EOM, BRST-exact, total-derivative, and general source rows are not enumerated",
            "topological_DRED_split": "the unsplit Chern-Weil bulk variation vanishes, but a separate hat/breve epsilon_E continuation is not locked",
        },
        "conditional_closure_theorem": {
            "assumptions": [
                "the graph/source/counterterm census is complete",
                "the UV residue is separated from possible IR poles and every one-loop primitive has at most a simple UV pole",
                "the DRED tensor grammar is O(N_epsilon)-covariant and contains no inverse N_epsilon",
                "the regulated graph and cut maps are separately residual-q equivariant",
                "every explicit epsilon-scalar realization is linked to its full-superspace seed by the same graph/source origin_id",
            ],
            "derivation": [
                "the genuine projector basis contains five DA rows and three BC rows",
                "a physical projection decomposes as sum_alpha P_(u,alpha)(N_epsilon)I_(u,alpha), with P_(u,alpha)(0)=0 for every independent structure",
                "Fin sum_alpha P_(u,alpha)(2epsilon)I_(u,alpha)=2 sum_alpha P'_(u,alpha)(0)r_(u,alpha,-1), and the 1/epsilon coefficient vanishes",
                "the physical residual-q kernel at dimension 9/2 is span{Z}",
            ],
            "conclusion": "z_(E_u O)^MS=0 for the eight projector-generated component rows, while their total finite projected image is c_fin*Z with c_fin determined by the complete primitive traces; no theorem is asserted for the unenumerated BV/source basis",
        },
        "minimal_projector_split": dred["minimal_projector_split"],
        "explicit_unexcluded_genuine_row": {
            "id": "E_DA_h_hb",
            "operator": next(row["operator"] for row in genuine_rows if row["id"] == "E_DA_h_hb"),
            "compatibility_note": "Legacy verifier witness key; this row belongs to the minimal projector split and is not asserted to span the complete BV/DRED kernel.",
        },
        "residual_q_orbit": dred["residual_q_orbit"],
        "double_breve_enumerated_delta_zero": dred["A_bb_enumerated_delta_zero"],
        "mixed_hat_breve_source": dred["mixed_A_hb_source"],
        "pole_vs_finite": dred["one_loop_pole_vs_finite"],
        "topological_sector": dred["topological_sector"],
        "unfixed_bv_source_rows": dred["unfixed_bv_source_rows"],
        "no_double_count": {
            **dred["no_double_count"],
            "condition": "Apply multiplicity one only after the full-superspace seed and explicit epsilon-scalar realization carry the same graph/source origin_id.",
        },
        "verdict": {
            "bare_WW": "CLOSED_TO_TRIVIAL_EPSILON_Z",
            "renormalized_all_channel": status,
            "z_EuO_MS_eight_projector_rows": "CONDITIONAL_ZERO_UNDER_UV_IR_SEPARATION_SIMPLE_POLE_AND_NO_INVERSE_N_EPSILON",
            "z_EO_MS_complete_BV_basis": "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS",
            "z_EO": "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS",
            "finite_mixed_term": "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES",
            "reason": "The closed breve polynomials remove the 1/epsilon pole but retain the graph- and tensor-dependent finite 2*sum_alpha P'_(u,alpha)(0)r_(u,alpha,-1); Step 5A does not lock the complete BV/DRED basis, epsilon-tensor split, or numerical primitive rules.",
        },
        "checks": checks,
    }
    return audit


def render(audit: Mapping[str, object]) -> str:
    checks = audit["checks"]  # type: ignore[index]
    rows = audit["minimal_projector_split"]["rows"]  # type: ignore[index]
    lines = [
        "# Step-5 evanescent-sector closure cross-review",
        "",
        "Status: `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`. Foundation pin: verified `origin/main@00000f7`, run `29306335742`.",
        "",
        "## 1. Bare WW remainder",
        "",
        "$$",
        "R_T^{mn}=r\\widehat\\delta^{mn},\\qquad R_C^{mn}=-r\\delta_4^{mn},",
        "$$",
        "",
        "$$",
        "R_T^{mn}+R_C^{mn}=-r\\breve\\delta^{mn},\\qquad",
        "p^\\rho\\breve\\delta^{mn}\\sigma_m\\bar\\sigma_\\rho\\sigma_n=-2\\epsilon p^\\rho\\sigma_\\rho.",
        "$$",
        "",
        "## 2. Complete minimal projector split of $\\mathscr Z$",
        "",
        "$$",
        "\\mathscr Z_{\\rm full}=\\mathscr Z_{DA}(h,hh)+\\mathscr Z_{BC}(h,h)+\\sum_{u=1}^{8}\\mathscr E_u.",
        "$$",
        "",
        "| row | operator | min breve degree |",
        "|---|---|---:|",
    ]
    for row in rows:  # type: ignore[assignment]
        lines.append(f"| `{row['id']}` | ${row['operator']}$ | {row['minimal_breve_degree']} |")
    lines.extend(
        [
            "",
            "Residual-$q$ descendants are $q_R\\mathscr E_u$, $R\\subset\\{1,2,3\\}$, with $\\pi_4q_r=q_r\\pi_4$.",
            "",
            "## 3. Pole mixing and finite anomaly",
            "",
            "$$",
            "\\Pi_{\\rm phys}\\Gamma_{\\mathscr E_u}^{(1)}",
            "=\\sum_\\alpha P_{u\\alpha}(N_\\epsilon)I_{u\\alpha}^{(1)},\\qquad",
            "P_{u\\alpha}(0)=0,\\qquad N_\\epsilon=2\\epsilon.",
            "$$",
            "",
            "After UV/IR separation, a one-loop primitive has at most a simple UV pole:",
            "",
            "$$",
            "\\operatorname{Fin}_{\\epsilon^0}\\sum_\\alpha P_{u\\alpha}(2\\epsilon)I_{u\\alpha}^{(1)}",
            "=2\\sum_\\alpha P_{u\\alpha}'(0)r_{u\\alpha,-1}.",
            "$$",
            "",
            "$$",
            "\\boxed{z_{\\mathscr E_uO}^{\\rm MS}=0\\quad\\text{under the displayed assumptions}},\\qquad",
            "\\boxed{\\operatorname{Fin}_{\\epsilon^0}=2\\sum_\\alpha P_{u\\alpha}'(0)r_{u\\alpha,-1}}.",
            "$$",
            "",
            "第一式只对上述八个 component projector rows 已证明；第二式的 numerical coefficient 未闭合。完整 BV/source evanescent basis 仍未枚举。",
            "",
            "## 4. Double-breve and mixed representatives",
            "",
            "$$",
            "A_{bb}=-i\\Sigma^{ij}(\\chi_i\\times\\chi_j),\\qquad",
            "\\frac{\\delta^2A_{bb}^E}{\\delta\\chi_i^M\\delta\\chi_j^N}=-2i\\Sigma^{ij}c_{MN}{}^E.",
            "$$",
            "",
            "已枚举的 $\\chi$ tadpole 与 $A_{\\widehat\\mu}\\chi\\chi$ direct/exchange contractions 都含 $\\Sigma^{ij}\\delta_{ij}=0$，故其 restricted projection 为零。尚未穷举的 compatible action/BV/source vertices 保持 `BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES`。",
            "",
            "$$",
            "A_{hb}=-2i(\\sigma^{\\widehat\\mu i})_{++}\\mathcal D_{\\widehat\\mu}\\chi_i,",
            "$$",
            "",
            "$$",
            "I_{D^M_{\\dot a},\\chi_i^N}^{[0]}=2i(J_{MN}-J_{NM})(\\sigma_h^\\nu)_{+\\dot a}(\\sigma^{\\widehat\\mu i})_{++}p_\\nu p_\\mu\\ne0.",
            "$$",
            "",
            "Its three physical $I_{[0]}$ triangles use $V_{\\chi\\widetilde\\Lambda\\Lambda}$ with $V_{A\\chi\\chi}$, $V_{A\\widetilde\\Lambda\\Lambda}$, and $V_{\\widetilde\\varphi\\Lambda\\Lambda}$. Step 5A does not lock unique propagators, integration cycle, or Fourier/DRED numerical rules; therefore $r_{u,-1}$ remains blocked.",
            "",
            "## 5. No-double-count boundary",
            "",
            "$$",
            "r\\widehat\\delta^{mn}T_{mn}-r\\delta_4^{mn}T_{mn}=-r\\breve\\delta^{mn}T_{mn}.",
            "$$",
            "",
            "Only when the full-superspace seed and explicit epsilon-scalar realization share one graph/source `origin_id` is the latter this complement rather than an additional term. This provenance link is not closed.",
            "",
            "## 6. Verdict",
            "",
            "$$",
            "\\boxed{z_{E_uO}^{\\rm MS}=0\\ \\text{ for the eight projector rows};\\qquad",
            "c_{\\rm fin}^{\\rm mixed}=\\texttt{BLOCKED\\_COMPLETE\\_BV\\_DRED\\_BASIS\\_DRED\\_EPSILON\\_SPLIT\\_FINITE\\_RESIDUES}.}",
            "$$",
            "",
            "## 7. Checks",
            "",
        ]
    )
    lines.extend(f"- `{row['id']}`: {'PASS' if row['pass'] else 'FAIL'}" for row in checks)  # type: ignore[index]
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    audit = build()
    JSON_OUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    MD_OUT.write_text(render(audit))
    failed = [row["id"] for row in audit["checks"] if not row["pass"]]
    print(json.dumps({"status": audit["status"], "failed_tests": failed}))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
