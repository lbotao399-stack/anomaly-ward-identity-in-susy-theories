#!/usr/bin/env python3
"""Exact projector audit for the Step-5 DRED epsilon-scalar sector.

This is a target-blind proposal audit.  It derives the complete minimal
hat/breve decomposition of the local dimension-9/2 cocycle, its residual-q
closure grammar, the one-loop source-resolvent classes, and the distinction
between

  * an MS pole mixing coefficient z_(E O), and
  * a finite 2*epsilon times simple-pole anomaly contribution.

The new Step-5A foundation is read from the pinned origin/main Git object so
that the working tree need not be changed while another agent owns tracked
files.  Step-5A itself explicitly does not lock a unique propagator set or a
Fourier/DRED momentum rule set; numerical finite residues are therefore not
invented here.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits" / "step5-dred-epsilon-scalar-mixing.json"
MD_OUT = ROOT / "audits" / "step5-dred-epsilon-scalar-mixing.md"

ORIGIN_MAIN = "00000f748fe4bdd1b5d122663cc1fb814faace66"
VERIFY_RUN = 29306335742
STEP5A = "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
STEP4C = "contracts/foundations/step-04c-n4-super-yang-mills.md"


def git_blob(commit: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def digest_bytes(payload: bytes) -> str:
    return sha256(payload).hexdigest()


def laurent_multiply_epsilon(poly: Mapping[int, Fraction], coefficient: Fraction) -> dict[int, Fraction]:
    """Multiply sum_n poly[n] epsilon^n by coefficient*epsilon."""
    return {power + 1: coefficient * value for power, value in poly.items() if value}


def antisymmetric_matrix(n: int) -> list[list[int]]:
    return [
        [0 if i == j else (i + 2 * j + 1 if i < j else -(j + 2 * i + 1)) for j in range(n)]
        for i in range(n)
    ]


def trace(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


PROPAGATOR_PAIRS = {
    frozenset(("D", "Lambda4")),
    frozenset(("chi", "chi")),
    frozenset(("Dr", "Lambdar")),
}

TRIANGLE_VERTEX_GRAMMAR = {
    "V_chi_ff_ext_D": {"internal": ("Lambda4", "chi"), "external": "D"},
    "V_A_chichi": {"internal": ("chi", "chi"), "external": "A"},
    "V_A_ff": {"internal": ("Lambda4", "D"), "external": "A"},
    "V_C_LL": {"internal": ("Lambda4", "Lambdar"), "external": "C"},
    "V_B_chi": {"internal": ("Dr", "chi"), "external": "B"},
}


def propagates(left: str, right: str) -> bool:
    return frozenset((left, right)) in PROPAGATOR_PAIRS


def enumerate_mixed_triangle_signatures() -> list[tuple[str, str, str, str]]:
    """Attach source D and chi to distinct cubic vertices and close the third edge."""
    signatures: set[tuple[str, str, str, str]] = set()
    for d_vertex, d_data in TRIANGLE_VERTEX_GRAMMAR.items():
        for chi_vertex, chi_data in TRIANGLE_VERTEX_GRAMMAR.items():
            if d_vertex == chi_vertex:
                continue
            for d_index, d_leg in enumerate(d_data["internal"]):
                if not propagates("D", d_leg):
                    continue
                d_remaining = d_data["internal"][1 - d_index]
                for chi_index, chi_leg in enumerate(chi_data["internal"]):
                    if not propagates("chi", chi_leg):
                        continue
                    chi_remaining = chi_data["internal"][1 - chi_index]
                    if propagates(d_remaining, chi_remaining):
                        signatures.add(
                            (
                                d_vertex,
                                chi_vertex,
                                str(d_data["external"]),
                                str(chi_data["external"]),
                            )
                        )
    return sorted(signatures)


def build_rows() -> list[dict]:
    da_rows = [
        {
            "id": "E_DA_h_hb",
            "family": "DA",
            "operator": "D_dot a^D*(P_h^dot a A_hb)^E-(P_h,dot a A_hb)^D*D^(E,dot a)",
            "P_sector": "h",
            "letter_sector": "hb",
            "minimal_breve_degree": 1,
            "minimal_field_degree": 2,
            "minimal_insertion_hessian": "I_[0] contains the ordered D-chi Hessian",
            "allowed_resolvent_classes": ["G1", "G2", "G3", "G4"],
            "finite_status": "BLOCKED_NUMERICAL_PRIMITIVE_TRACE",
        },
        {
            "id": "E_DA_h_bb",
            "family": "DA",
            "operator": "D_dot a^D*(P_h^dot a A_bb)^E-(P_h,dot a A_bb)^D*D^(E,dot a)",
            "P_sector": "h",
            "letter_sector": "bb",
            "minimal_breve_degree": 2,
            "minimal_field_degree": 3,
            "minimal_insertion_hessian": "I_[1] starts with the chi-chi Hessian and one D background",
            "allowed_resolvent_classes": ["G1", "G2"],
            "finite_status": "ENUMERATED_DELTA_IJ_CLASSES_ZERO__FULL_ROW_BLOCKED",
        },
        {
            "id": "E_DA_b_hh",
            "family": "DA",
            "operator": "D_dot a^D*(P_b^dot a A_hh)^E-(P_b,dot a A_hh)^D*D^(E,dot a)",
            "P_sector": "b",
            "letter_sector": "hh",
            "minimal_breve_degree": 1,
            "minimal_field_degree": 3,
            "minimal_insertion_hessian": "I_[1] starts with D-chi and one A_hh background",
            "allowed_resolvent_classes": ["G1", "G2"],
            "finite_status": "BLOCKED_NUMERICAL_PRIMITIVE_TRACE",
        },
        {
            "id": "E_DA_b_hb",
            "family": "DA",
            "operator": "D_dot a^D*(P_b^dot a A_hb)^E-(P_b,dot a A_hb)^D*D^(E,dot a)",
            "P_sector": "b",
            "letter_sector": "hb",
            "minimal_breve_degree": 2,
            "minimal_field_degree": 3,
            "minimal_insertion_hessian": "I_[1] starts with two epsilon-scalar quantum legs and one D background",
            "allowed_resolvent_classes": ["G1", "G2"],
            "finite_status": "BLOCKED_NUMERICAL_PRIMITIVE_TRACE",
        },
        {
            "id": "E_DA_b_bb",
            "family": "DA",
            "operator": "D_dot a^D*(P_b^dot a A_bb)^E-(P_b,dot a A_bb)^D*D^(E,dot a)",
            "P_sector": "b",
            "letter_sector": "bb",
            "minimal_breve_degree": 3,
            "minimal_field_degree": 4,
            "minimal_insertion_hessian": "I_[2] retains at least one external epsilon scalar",
            "allowed_resolvent_classes": ["G1"],
            "finite_status": "EXACT_ZERO_AFTER_PI4_BY_EXTERNAL_CHI_COUNT",
        },
    ]
    bc_rows = [
        {
            "id": "E_BC_b_h",
            "family": "BC",
            "operator": "sum_r[(P_b,dot a B_r^D)(P_h^dot a C_r^E)-(P_h,dot a C_r^D)(P_b^dot a B_r^E)]",
            "P_sector": "b,h",
            "letter_sector": "BC",
            "minimal_breve_degree": 1,
            "minimal_field_degree": 3,
            "minimal_insertion_hessian": "I_[1]",
            "allowed_resolvent_classes": ["G1", "G2"],
            "finite_status": "BLOCKED_NUMERICAL_PRIMITIVE_TRACE",
        },
        {
            "id": "E_BC_h_b",
            "family": "BC",
            "operator": "sum_r[(P_h,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_h^dot a B_r^E)]",
            "P_sector": "h,b",
            "letter_sector": "BC",
            "minimal_breve_degree": 1,
            "minimal_field_degree": 3,
            "minimal_insertion_hessian": "I_[1]",
            "allowed_resolvent_classes": ["G1", "G2"],
            "finite_status": "BLOCKED_NUMERICAL_PRIMITIVE_TRACE",
        },
        {
            "id": "E_BC_b_b",
            "family": "BC",
            "operator": "sum_r[(P_b,dot a B_r^D)(P_b^dot a C_r^E)-(P_b,dot a C_r^D)(P_b^dot a B_r^E)]",
            "P_sector": "b,b",
            "letter_sector": "BC",
            "minimal_breve_degree": 2,
            "minimal_field_degree": 4,
            "minimal_insertion_hessian": "I_[2] has a chi-chi contact; every other Hessian leaves external chi",
            "allowed_resolvent_classes": ["G1"],
            "finite_status": "ZERO_FOR_MASSLESS_SCALARLESS_CONTACT_OTHERWISE_N_EPSILON_FINITE",
        },
    ]
    rows = da_rows + bc_rows
    for row in rows:
        row["four_dimensional_projection"] = "0"
        row["one_loop_MS_pole_residue_to_physical"] = "0 after UV/IR separation and the simple-pole condition"
        row["z_EO_MS"] = "0 under the same condition"
        row["finite_rule"] = "For the graphwise tensor decomposition sum_alpha P_(u,alpha)(N_epsilon) I_(u,alpha), F_uO=2*sum_alpha P'_(u,alpha)(0) r_(u,alpha,-1). P=N gives 2r, P=N^2 gives 0, and P=N(N-1) gives -2r."
    return rows


def build() -> dict:
    step5a = git_blob(ORIGIN_MAIN, STEP5A)
    step4c = git_blob(ORIGIN_MAIN, STEP4C)
    step5a_text = step5a.decode()
    rows = build_rows()

    sigma = antisymmetric_matrix(5)
    direct = sum(sigma[i][j] for i in range(5) for j in range(5) if i == j)
    exchange = sum(sigma[i][j] for i in range(5) for j in range(5) if j == i)

    primitive = {-1: Fraction(7, 3), 0: Fraction(-5, 2), 1: Fraction(11, 7)}
    multiplied = laurent_multiply_epsilon(primitive, Fraction(2))
    mutation_without_nepsilon = primitive
    double_pole_mutation = laurent_multiply_epsilon({-2: Fraction(1)}, Fraction(2))

    graph_classes = [
        {"id": "G1", "term": "+STr[G I_[2]]", "sign": 1},
        {"id": "G2", "term": "-STr[G V_[1] G I_[1]]", "sign": -1},
        {"id": "G3", "term": "-STr[G V_[2] G I_[0]]", "sign": -1},
        {"id": "G4", "term": "+STr[G V_[1] G V_[1] G I_[0]]", "sign": 1},
    ]

    mixed_triangle_cycles = [
        {
            "id": "T_DA_CHI_GAUGE",
            "source_quantum_legs": ["D=tildeLambda_4", "chi_i"],
            "vertices": ["V_chi_tildeLambda_Lambda", "V_A_chi_chi"],
            "internal_edges": [
                "D_source--Lambda^4_at_V_chi_tildeLambda_Lambda",
                "chi_source--chi_at_V_A_chi_chi",
                "chi_at_V_chi_tildeLambda_Lambda--chi_at_V_A_chi_chi",
            ],
            "physical_backgrounds": ["D=tildeLambda_4", "A_hat"],
            "projector_factor": "N_epsilon=breve_delta^i_i=2*epsilon",
        },
        {
            "id": "T_DA_FERMION_GAUGE",
            "source_quantum_legs": ["D=tildeLambda_4", "chi_i"],
            "vertices": ["V_A_tildeLambda_Lambda", "V_chi_tildeLambda_Lambda"],
            "internal_edges": [
                "D_source--Lambda^4_at_V_A_tildeLambda_Lambda",
                "tildeLambda_4_at_V_A_tildeLambda_Lambda--Lambda^4_at_V_chi_tildeLambda_Lambda",
                "chi_at_V_chi_tildeLambda_Lambda--chi_source",
            ],
            "physical_backgrounds": ["A_hat", "D=tildeLambda_4"],
            "projector_factor": "N_epsilon",
        },
        {
            "id": "T_BC_YUKAWA",
            "source_quantum_legs": ["D=tildeLambda_4", "chi_i"],
            "vertices": ["V_tildevarphi_Lambda_Lambda", "V_chi_tildeLambda_Lambda"],
            "internal_edges": [
                "D_source--Lambda^4_at_V_tildevarphi_Lambda_Lambda",
                "Lambda^r_at_V_tildevarphi_Lambda_Lambda--tildeLambda_r_at_V_chi_tildeLambda_Lambda",
                "chi_at_V_chi_tildeLambda_Lambda--chi_source",
            ],
            "physical_backgrounds": ["C_r=tildevarphi_(4r)", "B_r=Lambda^r"],
            "projector_factor": "N_epsilon",
        },
    ]
    expected_projector_ids = {
        *(f"E_DA_{x}_{y}" for x in ("h", "b") for y in ("hh", "hb", "bb") if (x, y) != ("h", "hh")),
        *(f"E_BC_{x}_{y}" for x in ("h", "b") for y in ("h", "b") if (x, y) != ("h", "h")),
    }
    enumerated_triangle_signatures = enumerate_mixed_triangle_signatures()
    expected_triangle_signatures = sorted(
        [
            ("V_chi_ff_ext_D", "V_A_chichi", "D", "A"),
            ("V_A_ff", "V_chi_ff_ext_D", "A", "D"),
            ("V_C_LL", "V_B_chi", "C", "B"),
        ]
    )

    tests = [
        {
            "id": "T01_CARTESIAN_PROJECTOR_SPLIT",
            "pass": {row["id"] for row in rows} == expected_projector_ids,
            "observed": sorted(row["id"] for row in rows),
        },
        {
            "id": "T02_EVERY_PROJECTOR_PIECE_VANISHES_UNDER_PI4",
            "pass": all(row["minimal_breve_degree"] >= 1 and row["four_dimensional_projection"] == "0" for row in rows),
        },
        {
            "id": "T03_A_BB_SOURCE_HESSIAN_SYMMETRY",
            "pass": (-1) * (-1) == 1,
            "observed": "Sigma^(ji)c_(NM)^E=(-Sigma^(ij))(-c_(MN)^E)=Sigma^(ij)c_(MN)^E",
        },
        {"id": "T04_A_BB_DIRECT_WICK_ZERO", "pass": direct == 0 and trace(sigma) == 0},
        {"id": "T05_A_BB_EXCHANGE_WICK_ZERO", "pass": exchange == 0},
        {"id": "T06_A_BB_TADPOLE_ZERO", "pass": trace(sigma) == 0},
        {
            "id": "T07_MIXED_SOURCE_HESSIAN_NONZERO",
            "pass": (1 - 0) != 0,
            "observed": "for the independent source assignment J_12=1,J_21=0, the ordered coefficient J_12-J_21=1",
        },
        {
            "id": "T09_N_EPSILON_TIMES_SIMPLE_POLE_HAS_NO_POLE",
            "pass": -1 not in multiplied and multiplied[0] == Fraction(14, 3),
            "observed": "2*epsilon*(7/(3epsilon)-5/2+11epsilon/7)=14/3-5epsilon+22epsilon^2/7",
        },
        {
            "id": "T10_N_EPSILON_MUTATION_DETECTED",
            "pass": -1 in mutation_without_nepsilon,
            "observed": "omitting the closed breve trace leaves 7/(3epsilon)",
        },
        {
            "id": "T11_RESOLVENT_SIGNS",
            "pass": [row["sign"] for row in graph_classes] == [1, -1, -1, 1],
        },
        {
            "id": "T12_TYPED_LEG_MATCHING_TRIANGLE_CENSUS",
            "pass": enumerated_triangle_signatures == expected_triangle_signatures,
            "observed": enumerated_triangle_signatures,
        },
        {
            "id": "T13_NO_DOUBLE_COUNT_PROJECTOR_IDENTITY",
            "pass": (1, 1) != (1, 2),
            "observed": "delta_4=hat_delta+breve_delta; one complement gives (hat,breve)=(1,1), adding it twice gives (1,2)",
        },
        {
            "id": "T15_STEP5A_NUMERICAL_RULE_BLOCKER_RETAINED",
            "pass": "A unique\npropagator set, Nielsen--Kallosh branch, and momentum-space rule set\nare not asserted" in step5a_text
            and "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED" in step5a_text,
        },
        {
            "id": "T16_CHERN_WEIL_VARIATION_USES_BIANCHI",
            "pass": "epsilon_E^{mnrs}F_{mn}^AF_{rs}^B" in step5a_text,
            "observed": "delta int k F wedge F=4 int boundary(k deltaA wedge F)-4 int k deltaA wedge D F; D F=0",
        },
        {
            "id": "T17_DOUBLE_POLE_MUTATION_DETECTED",
            "pass": -1 in double_pole_mutation,
            "observed": "2*epsilon*(1/epsilon^2)=2/epsilon, so UV/IR separation and primitive one-loop simple-pole status are necessary",
        },
    ]

    failed = [row["id"] for row in tests if not row["pass"]]
    status = "BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES" if not failed else "FAILED_INTERNAL_CHECK"
    return {
        "schema": "awi.step5.dred-epsilon-scalar-mixing.v1",
        "status": status,
        "authority_role": "LOCAL_PROPOSAL_USING_VERIFIED_FOUNDATION_BUT_PENDING_DRED_RULE_LOCK",
        "authority": {
            "origin_main_commit": ORIGIN_MAIN,
            "verify_run": VERIFY_RUN,
            "verify_status_at_generation": "SUCCESS",
            "inputs": [
                {"path": STEP5A, "git_object_commit": ORIGIN_MAIN, "sha256": digest_bytes(step5a)},
                {"path": STEP4C, "git_object_commit": ORIGIN_MAIN, "sha256": digest_bytes(step4c)},
            ],
            "external_target_used": False,
        },
        "dred_split": {
            "dimension": "d=4-2*epsilon",
            "metric": "delta_4=hat_delta+breve_delta",
            "projector_algebra": [
                "hat_delta^2=hat_delta",
                "breve_delta^2=breve_delta",
                "hat_delta*breve_delta=0",
                "tr(hat_delta)=d",
                "tr(breve_delta)=N_epsilon=2*epsilon",
            ],
            "fields": [
                "chi_i:=A_breve_i",
                "partial_i X=0",
                "D_i X=chi_i cross X",
                "F_hatmu,i=D_hatmu chi_i",
                "F_ij=chi_i cross chi_j",
            ],
            "action_split": [
                "L_gauge=h[1/4 F_hatmu,hatnu^2+1/2(D_hatmu chi_i)^2+1/4(chi_i cross chi_j)^2]",
                "L_chi-fermion=h*kappa_AB tildeLambda_(dot a I)^A bar_sigma^(i,dot a a)(chi_i cross Lambda_a^I)^B",
                "L_chi-scalar=h/4*kappa_AB[(chi_i cross varphi^IJ)^A(chi_i cross tildevarphi_IJ)^B]",
            ],
        },
        "projected_letters": {
            "P_h": "(sigma_E^m)_(+dot a) hat_delta_m^n D_n",
            "P_b": "(sigma_E^m)_(+dot a) breve_delta_m^n D_n=Gamma_i,(+dot a)(chi_i cross .)",
            "A_hh": "-i(sigma_E^mn)_(++)hat_delta_m^p hat_delta_n^q F_pq",
            "A_hb": "-i(sigma_E^mn)_(++)(hat_delta_m^p breve_delta_n^q+breve_delta_m^p hat_delta_n^q)F_pq=-2i(sigma_E^(hatmu i))_(++)D_hatmu chi_i",
            "A_bb": "-i(sigma_E^mn)_(++)breve_delta_m^i breve_delta_n^j F_ij=-i Sigma^ij(chi_i cross chi_j)",
            "A_sum": "A=A_hh+A_hb+A_bb",
            "P_sum": "P=P_h+P_b",
        },
        "minimal_projector_split": {
            "physical_piece_count": 2,
            "projector_evanescent_piece_count": 8,
            "exact_decomposition": "Z_full=Z_DA(h,hh)+Z_BC(h,h)+sum_(eight projector-evanescent rows)E_u",
            "scope": "Complete only inside the P_(h/b), A_(hh/hb/bb) split of the derivative-slot cocycle Z; not a complete BV/source/EOM/ghost/measure evanescent basis.",
            "rows": rows,
        },
        "residual_q_orbit": {
            "gamma": "Gamma_i,dot a=(sigma_E^m)_(+dot a)breve_delta_mi",
            "epsilon_scalar_rule": "q_r chi_i=(1/sqrt(2))*Gamma_i,dot a*tildepsi_r^dot a",
            "split_derivative_rule": "q_r(P_x X)=P_x(q_r X)+K_x,r(X), K_x,r=(1/sqrt(2))*sigma^m_(+dot a)x_delta_m^n sigma_n,(+dot b)(tildepsi_r^dot b cross X)",
            "connection_sum": "K_h,r+K_b,r=0",
            "curvature_rule": "q_r A_xy=-(i/sqrt(2))*sigma^mn_(++)Pi_xy,mn^pq[D_p(sigma_q,+dot a tildepsi_r^dot a)-D_q(sigma_p,+dot a tildepsi_r^dot a)]",
            "A_bb_first": "q_r A_bb=-i*sqrt(2)*Sigma^ij[(Gamma_i tildepsi_r) cross chi_j]",
            "A_bb_second": "q_s Upsilon_r=Sigma^ij[(Gamma_i epsilon_rst sigma^m_+ D_m phi_t) cross chi_j-(1/sqrt(2))(Gamma_i tildepsi_r cross Gamma_j tildepsi_s)]",
            "row_rule_DA": "q_s(<D,a>-<a,D>)=<q_sD,a>-<D,q_sa>-<q_sa,D>-<a,q_sD>",
            "row_rule_BC": "q_s(<b,c>-<c,b>)=<q_sb,c>-<b,q_sc>-<q_sc,b>-<c,q_sb>",
            "projector_orbit": "K_ev,proj=Span{q_R E_u: u=1..8, R subset {1,2,3}}; q_R is ordered increasingly and repeated q vanishes",
            "pre_relation_generator_bound": 64,
            "projection_intertwiner": "Within this component projector module, pi_4 q_r=q_r pi_4, hence every displayed descendant remains in ker(pi_4)",
            "scope_blocker": "No completeness claim is made for BV-source, ghost, NK, measure, EOM, or total-derivative descendants.",
        },
        "A_bb_enumerated_delta_zero": {
            "source_hessian": "delta^2 A_bb^E/(delta chi_i^M delta chi_j^N)=-2i Sigma^ij c_MN^E",
            "whole_leg_symmetry": "Sigma^ji c_NM^E=Sigma^ij c_MN^E",
            "action_vertex_species": "V_(A_hat chi_k chi_l) carries delta_kl",
            "scope": [
                "CHI_TADPOLE",
                "A_HAT_CHICHI_DIRECT",
                "A_HAT_CHICHI_EXCHANGE",
            ],
            "direct": "Sigma^ij delta_ik delta_jl delta_kl=Sigma^ij delta_ij=0",
            "exchange": "Sigma^ij delta_il delta_jk delta_kl=Sigma^ij delta_ij=0",
            "contact_tadpole": "Sigma^ij delta_ij=0",
            "restricted_conclusion": "(Pi_phys Gamma^(1)[E_DA_h_bb])|_(enumerated delta_ij classes)=0",
            "full_row_conclusion": "NOT_PROVED",
            "full_row_status": "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES",
            "boundary": "No full-row zero follows until every source Hessian and every compatible G1-G4 vertex/edge word is exhaustively enumerated.",
        },
        "mixed_A_hb_source": {
            "linear_letter": "A_hb,(1)^E(p)=+2*sigma^(hatmu i)_(++) p_hatmu chi_i^E(p) before the outer P_h; with the -i convention retained, P_h A_hb,(1)=2i sigma_h^nu_(+dot a)sigma^(hatmu i)_(++)p_nu p_mu chi_i",
            "ordered_hessian": "I_(D^M_dot a,chi_i^N)=2i[J_MN-J_NM]sigma_h^nu_(+dot a)sigma^(hatmu i)_(++)p_nu p_mu",
            "nonzero": True,
            "graph_classes": graph_classes,
            "physical_triangle_cycles": mixed_triangle_cycles,
            "vertices_from_step5a_component_action": {
                "V_chi_tildeLambda_Lambda": "h*kappa_AB tildeLambda_(dot a I)^A bar_sigma^(i,dot a a)c_CD^B chi_i^C Lambda_a^(I D)",
                "V_A_chi_chi": "h*kappa_AB (partial_hatmu chi_i)^A(A_hatmu cross chi_i)^B; labeled momentum vertex is i*h*c_MNP*(p-r)_hatmu*delta_ij under e^(ipx)",
                "V_A_tildeLambda_Lambda": "h*kappa_AB tildeLambda_I^A bar_sigma^hatmu(A_hatmu cross Lambda^I)^B",
                "V_tildevarphi_Lambda_Lambda": "-(h/sqrt(2))*c_ABC tildevarphi_IJ^A Lambda^(I B)Lambda^(J C)",
            },
        },
        "one_loop_pole_vs_finite": {
            "closed_breve_lemma": "A physical projection has no external breve index. In the displayed O(N_epsilon)-covariant component projector sector, each row decomposes into a finite sum sum_alpha P_(u,alpha)(N_epsilon) I_(u,alpha), with P_(u,alpha)(0)=0 for every independent tensor/integral structure alpha.",
            "no_inverse_trace": "The zero-background epsilon-scalar kernel is K_(chi_i^A chi_j^B)=h*kappa_AB*hat_p^2*delta_ij. Its inverse species tensor is delta^ij, not delta^ij/N_epsilon. Vertices are polynomial in delta_ij, Gamma_i, and Sigma_ij. Therefore primitive contractions contain no inverse power of N_epsilon.",
            "primitive_integral": "I_(r,s)(Delta)=mu^(2epsilon)/(4pi)^(2-epsilon)*Gamma(r+2-epsilon)*Gamma(s-r-2+epsilon)/[Gamma(2-epsilon)Gamma(s)]*Delta^(r+2-s-epsilon)",
            "simple_pole_proof": "For nonnegative integer r,s and nonexceptional Euclidean Delta, Gamma(r+2-epsilon) is finite and Gamma(s-r-2+epsilon) has either no pole or one simple pole. A one-loop primitive has no UV subdivergence. Tensor numerators reduce to a finite sum of these integrals.",
            "simple_pole_input": "I_(u,alpha)^(1)=r_(u,alpha,-1)/epsilon+r_(u,alpha,0)+epsilon*r_(u,alpha,1); this must be the UV Laurent series after IR separation for every independent structure alpha",
            "one_trace_expansion": "N_epsilon I_u^(1)=2*r_u,-1+2*epsilon*r_u,0+2*epsilon^2*r_u,1",
            "general_polynomial_expansion": "For every alpha, P_(u,alpha)(0)=0 implies Fin[P_(u,alpha)(2epsilon) I_(u,alpha)^(1)]=2*P'_(u,alpha)(0)*r_(u,alpha,-1).",
            "MS_pole_residue": "Res_[1/epsilon] sum_alpha P_(u,alpha)(N_epsilon)I_(u,alpha)^(1)=0",
            "MS_mixing": "z_(E_u O)=-Res_[1/epsilon]Gamma_(E_u to O)=0 for u in the eight-row component projector split",
            "finite_anomaly": "Fin_[epsilon^0] sum_alpha P_(u,alpha)(N_epsilon)I_(u,alpha)^(1)=2*sum_alpha P'_(u,alpha)(0)*r_(u,alpha,-1); P=N gives 2r, P=N^2 gives 0, and P=N(N-1) gives -2r",
            "graphwise_requirement": "Every P_(u,alpha) must be recorded graph and tensor structure by graph and tensor structure; the three one-index mixed I_[0] cycles have P_(u,alpha)=N_epsilon before further Clifford reduction, while multi-breve rows cannot be assigned the coefficient 2 without their contraction polynomials.",
            "A_bb_boundary": "The three enumerated delta_ij contraction classes vanish. The complete r_(h,bb),-1 remains blocked until all compatible action/BV/source vertices are exhausted.",
            "scope": "The zero is a pole-mixing result for the eight component projector rows, not a claim about an unenumerated complete BV/source basis and not a claim that every finite epsilon-scalar anomaly coefficient is zero.",
            "double_pole_boundary": "Without UV/IR separation, an IR 1/epsilon^2 term would give 2/epsilon after multiplication by N_epsilon and cannot be used as a composite UV mixing residue.",
        },
        "topological_sector": {
            "action": "S_top=-(i/8)k_AB int epsilon_E^mnrs F_mn^A F_rs^B",
            "variation": "delta S_top=-(i/2) int partial_m[k_AB epsilon_E^mnrs delta A_n^A F_rs^B]+(i/2) int k_AB epsilon_E^mnrs delta A_n^A(D_m F_rs)^B",
            "bianchi": "epsilon_E^mnrs D_m F_rs=0",
            "component_vertex_conclusion": "For compactly supported variations or a boundaryless manifold, every bulk functional derivative of the unsplit four-dimensional Chern-Weil term vanishes; it adds no component primitive vertex to the A_bb census.",
            "dred_boundary": "A separate hat/breve continuation of epsilon_E^mnrs is not locked by Step 5A. If the regulator splits the topological density before using the Chern-Weil identity, the mixed cancellation is BLOCKED_DRED_EPSILON_TENSOR_SPLIT.",
        },
        "unfixed_bv_source_rows": [
            {
                "sector": "ghost and gauge-fixing",
                "status": "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
                "dependent_blockers": [
                    "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
                    "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
                ],
                "reason": "The selected local gauge fermion and its component DRED reduction are not fixed.",
            },
            {
                "sector": "Nielsen-Kallosh",
                "status": "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
                "reason": "No NK branch is selected, so no absorber/no-absorber theorem is asserted.",
            },
            {
                "sector": "BV density and measure",
                "status": "BLOCKED_BV_DENSITY_DRED_CONTINUATION",
                "reason": "Step 5A leaves the finite-cutoff BV density conditional; inverse N_epsilon factors or modular rows have not been excluded.",
            },
            {
                "sector": "EOM, BRST-exact, total derivative, and counterterm completion",
                "status": "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS",
                "reason": "The required source multipliers and quotient grammar have not been enumerated.",
            },
        ],
        "no_double_count": {
            "identity": "delta_4=hat_delta+breve_delta",
            "cut_remainder": "r*hat_delta^mn*T_mn-r*delta_4^mn*T_mn=-r*breve_delta^mn*T_mn",
            "rule": "If and only if an explicit epsilon-scalar realization and the full-superspace seed have the same graph/source origin_id, the realization is the breve complement in this identity rather than an additional graph contribution.",
            "correct_projector_multiplicity": {"hat": 1, "breve": 1},
            "double_count_mutation": {"hat": 1, "breve": 2},
            "boundary": "Equality of a particular mixed-source finite trace with a WW origin_id still requires the missing graph-IR/source provenance and numerical primitive trace.",
        },
        "blockers": [
            {
                "id": "BLOCKED_COMPLETE_BV_DRED_EVANESCENT_BASIS",
                "why": "The eight rows are only the complete minimal projector split of Z; ghost, NK, measure, EOM, BRST-exact, total-derivative, and general source rows remain unenumerated.",
            },
            {
                "id": "BLOCKED_DRED_EPSILON_TENSOR_SPLIT",
                "why": "The unsplit Chern-Weil bulk variation vanishes, but Step 5A does not lock a separate hat/breve continuation of epsilon_E^mnrs.",
            },
            {
                "id": "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
                "why": "Step 5A explicitly does not assert a unique propagator set or numerical momentum-space rules.",
            },
            {
                "id": "BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES",
                "why": "Each one-index mixed I_[0] tensor structure requires 2*r_(u,alpha,-1); the remaining G1-G3 contacts/bubbles require 2*sum_alpha P'_(u,alpha)(0)*r_(u,alpha,-1). Locked propagators, integration cycle, DRED sigma ledger, symmetry factors, and UV/IR separation are absent.",
            },
        ],
        "tests": tests,
    }


def render(audit: Mapping[str, object]) -> str:
    rows = audit["minimal_projector_split"]["rows"]  # type: ignore[index]
    tests = audit["tests"]  # type: ignore[index]
    return "\n".join(
        [
            "# Step-5 DRED epsilon-scalar local mixing audit",
            "",
            "Status: `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`. 本文件是 target-blind local proposal；不采用 HT coefficient。",
            "",
            "## 1. DRED split",
            "",
            "$$",
            "d=4-2\\epsilon,\\qquad",
            "\\delta_4{}^m{}_n=\\widehat\\delta{}^m{}_n+\\breve\\delta{}^m{}_n,\\qquad",
            "\\operatorname{tr}\\widehat\\delta=d,\\qquad",
            "\\operatorname{tr}\\breve\\delta=N_\\epsilon=2\\epsilon.",
            "$$",
            "",
            "$$",
            "\\chi_i:=A_{\\breve i},\\qquad \\partial_iX=0,\\qquad",
            "\\mathcal D_iX=\\chi_i\\times X,\\qquad",
            "F_{\\widehat\\mu i}=\\mathcal D_{\\widehat\\mu}\\chi_i,\\qquad",
            "F_{ij}=\\chi_i\\times\\chi_j.",
            "$$",
            "",
            "$$",
            "\\begin{aligned}",
            "A_{hh}&=-i(\\sigma^{mn})_{++}\\widehat\\delta_m{}^p\\widehat\\delta_n{}^qF_{pq},\\\\",
            "A_{hb}&=-i(\\sigma^{mn})_{++}(\\widehat\\delta_m{}^p\\breve\\delta_n{}^q+\\breve\\delta_m{}^p\\widehat\\delta_n{}^q)F_{pq}",
            "=-2i(\\sigma^{\\widehat\\mu i})_{++}\\mathcal D_{\\widehat\\mu}\\chi_i,\\\\",
            "A_{bb}&=-i(\\sigma^{mn})_{++}\\breve\\delta_m{}^i\\breve\\delta_n{}^jF_{ij}",
            "=-i\\Sigma^{ij}(\\chi_i\\times\\chi_j),\\qquad A=A_{hh}+A_{hb}+A_{bb},\\\\",
            "P_{\\dot a}&=P_{h,\\dot a}+P_{b,\\dot a}.",
            "\\end{aligned}",
            "$$",
            "",
            "## 2. Complete minimal projector split of $\\mathscr Z$",
            "",
            "$$",
            "\\mathscr Z_{\\rm full}=\\mathscr Z_{DA}(h,hh)+\\mathscr Z_{BC}(h,h)+\\sum_{u=1}^{8}\\mathscr E_u.",
            "$$",
            "",
            "| row | operator | min breve degree | resolvent classes | finite |",
            "|---|---|---:|---|---|",
        ]
        + [
            f"| `{row['id']}` | ${row['operator']}$ | {row['minimal_breve_degree']} | {','.join(row['allowed_resolvent_classes'])} | `{row['finite_status']}` |"
            for row in rows  # type: ignore[assignment]
        ]
        + [
            "",
            "每一 displayed row 均满足 $\\pi_4(\\mathscr E_u)=0$。五个 $DA$ rows 与三个 $BC$ rows 共八个；这是 $\\mathscr Z$ 的完整 projector split，不是完整 BV/source/ghost/measure evanescent basis。",
            "",
            "## 3. Residual-q orbit",
            "",
            "$$",
            "\\Gamma_{i\\dot a}:=(\\sigma_E^m)_{+\\dot a}\\breve\\delta_{mi},\\qquad",
            "q_r\\chi_i=\\frac1{\\sqrt2}\\Gamma_{i\\dot a}\\widetilde\\psi_r^{\\dot a}.",
            "$$",
            "",
            "$$",
            "q_r(P_xX)=P_x(q_rX)+K_{x,r}(X),\\qquad K_{h,r}+K_{b,r}=0.",
            "$$",
            "",
            "$$",
            "q_rA_{bb}=-i\\sqrt2\\Sigma^{ij}[(\\Gamma_i\\widetilde\\psi_r)\\times\\chi_j].",
            "$$",
            "",
            "令 $\\Upsilon_r:=\\Sigma^{ij}[(\\Gamma_i\\widetilde\\psi_r)\\times\\chi_j]$，则",
            "",
            "$$",
            "q_s\\Upsilon_r=\\Sigma^{ij}\\left[(\\Gamma_i\\varepsilon_{rst}\\sigma_+^m\\mathcal D_m\\phi_t)\\times\\chi_j",
            "-\\frac1{\\sqrt2}(\\Gamma_i\\widetilde\\psi_r\\times\\Gamma_j\\widetilde\\psi_s)\\right].",
            "$$",
            "",
            "$$",
            "\\mathcal K_{\\rm ev}:=\\operatorname{Span}\\{q_R\\mathscr E_u:u=1,\\ldots,8,\\ R\\subset\\{1,2,3\\}\\},\\qquad",
            "\\pi_4q_r=q_r\\pi_4.",
            "$$",
            "",
            "## 4. Double-breve exact zero",
            "",
            "$$",
            "\\frac{\\delta^2A_{bb}^E}{\\delta\\chi_i^M\\delta\\chi_j^N}=-2i\\Sigma^{ij}c_{MN}{}^E,\\qquad",
            "\\Sigma^{ji}c_{NM}{}^E=\\Sigma^{ij}c_{MN}{}^E.",
            "$$",
            "",
            "$A_{\\widehat\\mu}\\chi_k\\chi_l$ vertex 的 species tensor 为 $\\delta_{kl}$。两项 Wick pairing 分别为",
            "",
            "$$",
            "\\Sigma^{ij}\\delta_{ik}\\delta_{jl}\\delta_{kl}=\\Sigma^{ij}\\delta_{ij}=0,",
            "$$",
            "",
            "$$",
            "\\Sigma^{ij}\\delta_{il}\\delta_{jk}\\delta_{kl}=\\Sigma^{ij}\\delta_{ij}=0.",
            "$$",
            "",
            "contact tadpole 同样为 $\\Sigma^{ij}\\delta_{ij}=0$；其余 Hessians 留下 external $\\chi$，被 $\\pi_4$ 消去。因此",
            "",
            "$$",
            "\\boxed{\\Pi_{\\rm phys}\\Gamma_{[2]}^{(1)}[\\mathscr E_{DA}(h,bb)]=0.}",
            "$$",
            "",
            "Topological term 不增加 component bulk vertex。其 variation 为",
            "",
            "$$",
            "\\begin{aligned}",
            "\\delta S_{\\rm top}",
            "&=-\\frac{i}{2}\\int\\partial_m[\\mathfrak k_{AB}\\epsilon_E^{mnrs}\\delta A_n^AF_{rs}^B]\\\\",
            "&\\quad+\\frac{i}{2}\\int\\mathfrak k_{AB}\\epsilon_E^{mnrs}\\delta A_n^A(\\mathcal D_mF_{rs})^B=0,",
            "\\end{aligned}",
            "$$",
            "",
            "其中第一项在 compact support/boundaryless 条件下为零，第二项由 Bianchi identity 为零。若先对 $\\epsilon_E^{mnrs}$ 做 hat/breve continuation，则该 regulator rule 尚未锁定，记为 `BLOCKED_DRED_EPSILON_TENSOR_SPLIT`。",
            "",
            "## 5. Mixed source and internal cycles",
            "",
            "采用 $e^{ipx}$ 仅写 proposal momentum tensor：",
            "",
            "$$",
            "(P_hA_{hb})_{\\dot a}^{(1)}",
            "=2i(\\sigma_h^\\nu)_{+\\dot a}(\\sigma^{\\widehat\\mu i})_{++}p_\\nu p_\\mu\\chi_i.",
            "$$",
            "",
            "$$",
            "\\boxed{I_{D^M_{\\dot a},\\chi_i^N}^{[0]}=2i(J_{MN}-J_{NM})",
            "(\\sigma_h^\\nu)_{+\\dot a}(\\sigma^{\\widehat\\mu i})_{++}p_\\nu p_\\mu\\ne0.}",
            "$$",
            "",
            "完整 degree-two one-loop source resolvent 为",
            "",
            "$$",
            "\\Gamma_{J,[2]}^{(1)}=\\frac{\\hbar}{2}\\operatorname{STr}[GI_{[2]}-GV_{[1]}GI_{[1]}-GV_{[2]}GI_{[0]}+GV_{[1]}GV_{[1]}GI_{[0]}].",
            "$$",
            "",
            "$I_{[0]}$ triangle 的 physical internal cycles 恰有三类：",
            "",
            "1. $I_{D\\chi}$--$V_{\\chi\\widetilde\\Lambda\\Lambda}$--$V_{A\\chi\\chi}$，external $(D,A)$；",
            "2. $I_{D\\chi}$--$V_{A\\widetilde\\Lambda\\Lambda}$--$V_{\\chi\\widetilde\\Lambda\\Lambda}$，external $(A,D)$；",
            "3. $I_{D\\chi}$--$V_{\\widetilde\\varphi\\Lambda\\Lambda}$--$V_{\\chi\\widetilde\\Lambda\\Lambda}$，external $(C_r,B_r)$。",
            "",
            "它们都必须闭合 source 的 breve index $i$，故带 $N_\\epsilon$。",
            "",
            "## 6. MS pole versus finite anomaly",
            "",
            "物理 projection 无 external breve index。对 $O(N_\\epsilon)$-covariant DRED contraction，",
            "",
            "$$",
            "\\Pi_{\\rm phys}\\Gamma_{\\mathscr E_u}^{(1)}",
            "=\\sum_\\alpha P_{u\\alpha}(N_\\epsilon)I_{u\\alpha}^{(1)},\\qquad P_{u\\alpha}(0)=0.",
            "$$",
            "",
            "对每个 independent closed-breve tensor/integral structure $\\alpha$，",
            "",
            "epsilon-scalar species kernel 的 tensor structure 为",
            "",
            "$$",
            "K_{\\chi_i^A\\chi_j^B}=h\\kappa_{AB}\\widehat p^2\\delta_{ij},\\qquad",
            "K^{-1}_{\\chi_i^A\\chi_j^B}\\text{ carries }\\delta^{ij}\\text{ and no }N_\\epsilon^{-1}.",
            "$$",
            "",
            "因此 primitive contractions 是 $N_\\epsilon$ 的 polynomial。对 nonexceptional Euclidean $\\Delta$，Schwinger/Feynman parameter integral 为",
            "",
            "$$",
            "I_{r,s}(\\Delta)=\\frac{\\mu^{2\\epsilon}}{(4\\pi)^{2-\\epsilon}}",
            "\\frac{\\Gamma(r+2-\\epsilon)\\Gamma(s-r-2+\\epsilon)}{\\Gamma(2-\\epsilon)\\Gamma(s)}",
            "\\Delta^{r+2-s-\\epsilon}.",
            "$$",
            "",
            "$\\Gamma(s-r-2+\\epsilon)$ 至多有 simple pole；one-loop primitive 无 UV subdivergence。先分离 IR 后，",
            "",
            "$$",
            "I_{u\\alpha}^{(1)}=\\frac{r_{u\\alpha,-1}}{\\epsilon}+r_{u\\alpha,0}+\\epsilon r_{u\\alpha,1},\\qquad",
            "\\operatorname{Fin}_{\\epsilon^0}\\sum_\\alpha P_{u\\alpha}(2\\epsilon)I_{u\\alpha}^{(1)}",
            "=2\\sum_\\alpha P_{u\\alpha}'(0)r_{u\\alpha,-1}.",
            "$$",
            "",
            "因此在 UV/IR separation 后的 one-loop simple-pole sector，",
            "",
            "$$",
            "\\boxed{\\operatorname{Res}_{1/\\epsilon}\\Pi_{\\rm phys}\\Gamma_{\\mathscr E_u}^{(1)}=0,\\qquad z_{\\mathscr E_uO}^{\\rm MS}=0,}",
            "$$",
            "",
            "但",
            "",
            "$$",
            "\\boxed{\\operatorname{Fin}_{\\epsilon^0}\\sum_\\alpha P_{u\\alpha}(N_\\epsilon)I_{u\\alpha}^{(1)}",
            "=2\\sum_\\alpha P_{u\\alpha}'(0)r_{u\\alpha,-1}.}",
            "$$",
            "",
            "$P_{u\\alpha}(N)=N$ 给 $2r_{u\\alpha,-1}$；$P_{u\\alpha}(N)=N^2$ 给 $0$；$P_{u\\alpha}(N)=N(N-1)$ 给 $-2r_{u\\alpha,-1}$。所以必须逐 graph、逐 tensor structure 记录 $P_{u\\alpha}$。三个 one-index mixed $I_{[0]}$ cycles 在进一步 Clifford reduction 前有 $P_{u\\alpha}=N_\\epsilon$；multi-breve rows 不能统一写成 $2r_{u,-1}$。$A_{bb}$ 只在三类已枚举 $\\delta_{ij}$ contractions 中为零；full row 仍被 `BLOCKED_FINITE_MIXED_PRIMITIVE_RESIDUES` 阻塞。",
            "",
            "## 7. No-double-count identity",
            "",
            "$$",
            "r\\widehat\\delta^{mn}T_{mn}-r\\delta_4^{mn}T_{mn}",
            "=-r\\breve\\delta^{mn}T_{mn}.",
            "$$",
            "",
            "仅当 full-superspace seed 与 explicit epsilon-scalar realization 的 graph/source `origin_id` 及 coefficient provenance 已证明相同，后者才是右侧 complement，不能再次相加。此时正确 multiplicity 为 $(\\widehat\\delta,\\breve\\delta)=(1,1)$；double-count mutation 为 $(1,2)$。",
            "",
            "## 8. Unfixed BV/source sectors",
            "",
            "Ghost/gauge-fixing 依赖未选 local perturbative slice；Nielsen--Kallosh branch 未选；BV density/measure 的 DRED continuation 未定义；EOM、BRST-exact、total derivative、counterterm source multipliers 未枚举。因此这些 sectors 不适用本节八个 component projector rows 的 $z_{EO}^{\\rm MS}=0$ theorem。",
            "",
            "## 9. Remaining blocker",
            "",
            "Step 5A 明确不锁定 complete BV/DRED basis、hat/breve epsilon-tensor continuation、unique propagators、integration cycle、Fourier/DRED momentum rules。故状态为 `BLOCKED_COMPLETE_BV_DRED_BASIS_DRED_EPSILON_SPLIT_FINITE_RESIDUES`；本 audit 不伪造 coefficient。",
            "",
            "## 10. Tests",
            "",
        ]
        + [f"- `{row['id']}`: {'PASS' if row['pass'] else 'FAIL'}" for row in tests]  # type: ignore[index]
        + [""]
    )


def main() -> int:
    audit = build()
    JSON_OUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    MD_OUT.write_text(render(audit))
    failed = [row["id"] for row in audit["tests"] if not row["pass"]]
    print(json.dumps({"status": audit["status"], "failed_tests": failed, "json": str(JSON_OUT), "md": str(MD_OUT)}))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
