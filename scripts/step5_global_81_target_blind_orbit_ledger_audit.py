#!/usr/bin/env python3
"""Target-blind 9x9 Step-5 anomaly-sector ledger from proved local audits.

This script never reads either generated/step5/project-result-ledger.json or
generated/step5/ht_ordered_pair_targets.json.  A pair receives a coefficient
only when a named representative audit is target-blind and complete.  The
AB/BA Project result is sealed before its supporting audit opens HT check-only.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.json"
AUDIT_MD = ROOT / "audits/step5-global-81-target-blind-orbit-ledger.md"

STRUCTURAL_CENSUS = ROOT / "audits/step5-all-triangle-parent-port-census.json"
NO_DESCENDANT_AUDIT = ROOT / "audits/step5-no-descendant-pairs-exact.json"
AC_CA_AUDIT = ROOT / "audits/step5-ac-ca-family-exact.json"
BB_OFFDIAGONAL_AUDIT = ROOT / "audits/step5-bb-offdiagonal-family-exact.json"
BC_CB_AUDIT = ROOT / "audits/step5-bc-full-family-raw-projection-exact.json"
BB_DIAGONAL_BD_DB_ZERO_AUDIT = ROOT / "audits/step5-bbdiagonal-bd-db-exact-zero.json"
AA_AUDIT = ROOT / "audits/step5-aa-standard-feynman-strictification.md"
AA_EXACT_AUDIT = ROOT / "audits/step5-aa-external-slot-decomposition-exact.json"
AB_RENORMALIZATION_AUDIT = ROOT / "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json"
AB_VECTOR_FRAME_AUDIT = ROOT / "audits/step5-ab-ba-vector-frame-missing-orbit-exact.json"
AB_G1_AUDIT = ROOT / "audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json"
AB_G3_MEASURE_AUDIT = ROOT / "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json"
AB_G3_TYPED_AUDIT = ROOT / "audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json"
AD_DA_AUDIT = ROOT / "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json"
AD_DA_MD_AUDIT = ROOT / "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md"
AD_DA_RAW_CONTACT_AUDIT = ROOT / "audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json"
AD_DA_RAW_CONTACT_MD_AUDIT = ROOT / "audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md"

INPUT_PATHS = (
    STRUCTURAL_CENSUS,
    NO_DESCENDANT_AUDIT,
    AC_CA_AUDIT,
    BB_OFFDIAGONAL_AUDIT,
    BC_CB_AUDIT,
    BB_DIAGONAL_BD_DB_ZERO_AUDIT,
    AA_AUDIT,
    AA_EXACT_AUDIT,
    AB_RENORMALIZATION_AUDIT,
    AB_VECTOR_FRAME_AUDIT,
    AB_G1_AUDIT,
    AB_G3_MEASURE_AUDIT,
    AB_G3_TYPED_AUDIT,
    AD_DA_AUDIT,
    AD_DA_MD_AUDIT,
    AD_DA_RAW_CONTACT_AUDIT,
    AD_DA_RAW_CONTACT_MD_AUDIT,
)

FORBIDDEN_LEDGER_PATHS = {
    ROOT / "generated/step5/project-result-ledger.json",
    ROOT / "generated/step5/ht_ordered_pair_targets.json",
}

LETTERS = ("A", "B1", "B2", "B3", "C1", "C2", "C3", "Ddot1", "Ddot2")
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
ACTIVE_DESCENDANT = frozenset(("A", "B1", "B2", "B3"))
NO_DESCENDANT = frozenset(("C1", "C2", "C3", "Ddot1", "Ddot2"))


@dataclass(frozen=True)
class Evidence:
    structural: dict[str, Any]
    no_descendant: dict[str, Any]
    ac_ca: dict[str, Any]
    bb: dict[str, Any]
    bc_cb: dict[str, Any]
    bb_diagonal_bd_db_zero: dict[str, Any]
    aa: dict[str, Any]
    ab_renormalization: dict[str, Any]
    ab_vector_frame: dict[str, Any]
    ab_g1: dict[str, Any]
    ab_g3_measure: dict[str, Any]
    ab_g3_typed: dict[str, Any]
    ad_da: dict[str, Any]
    ad_da_raw_contact: dict[str, Any]
    aa_status: str
    ad_da_status: str
    ad_da_raw_contact_status: str


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        fail(f"missing evidence: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_status(path: Path) -> str:
    if not path.is_file():
        fail(f"missing evidence: {path.relative_to(ROOT)}")
    match = re.search(r"^Status:\s*`([^`]+)`", path.read_text(encoding="utf-8"), re.MULTILINE)
    if not match:
        fail(f"missing Status line: {path.relative_to(ROOT)}")
    return match.group(1)


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


def cyclic_flavor_map(target: int) -> tuple[int, int, int]:
    return {
        1: (1, 2, 3),
        2: (2, 3, 1),
        3: (3, 1, 2),
    }[target]


def distinct_flavor_map(first: int, second: int) -> tuple[int, int, int]:
    if first == second:
        raise ValueError((first, second))
    third = 6 - first - second
    return first, second, third


def dotted_map(target: int) -> str:
    if target not in {1, 2}:
        raise ValueError(target)
    return f"dot1->dot{target}"


def marked_terms(left: str, right: str) -> list[dict[str, Any]]:
    terms: list[dict[str, Any]] = []
    if left in ACTIVE_DESCENDANT:
        terms.append({"side": "L", "letter": left, "leibniz_sign": 1})
    if right in ACTIVE_DESCENDANT:
        terms.append(
            {
                "side": "R",
                "letter": right,
                "leibniz_sign": 1 if PARITY[left] == 0 else -1,
            }
        )
    return terms


def read_evidence() -> Evidence:
    if FORBIDDEN_LEDGER_PATHS.intersection(INPUT_PATHS):
        fail("forbidden Project/HT result ledger entered INPUT_PATHS")

    evidence = Evidence(
        structural=load_json(STRUCTURAL_CENSUS),
        no_descendant=load_json(NO_DESCENDANT_AUDIT),
        ac_ca=load_json(AC_CA_AUDIT),
        bb=load_json(BB_OFFDIAGONAL_AUDIT),
        bc_cb=load_json(BC_CB_AUDIT),
        bb_diagonal_bd_db_zero=load_json(BB_DIAGONAL_BD_DB_ZERO_AUDIT),
        aa=load_json(AA_EXACT_AUDIT),
        ab_renormalization=load_json(AB_RENORMALIZATION_AUDIT),
        ab_vector_frame=load_json(AB_VECTOR_FRAME_AUDIT),
        ab_g1=load_json(AB_G1_AUDIT),
        ab_g3_measure=load_json(AB_G3_MEASURE_AUDIT),
        ab_g3_typed=load_json(AB_G3_TYPED_AUDIT),
        ad_da=load_json(AD_DA_AUDIT),
        ad_da_raw_contact=load_json(AD_DA_RAW_CONTACT_AUDIT),
        aa_status=markdown_status(AA_AUDIT),
        ad_da_status=markdown_status(AD_DA_MD_AUDIT),
        ad_da_raw_contact_status=markdown_status(AD_DA_RAW_CONTACT_MD_AUDIT),
    )

    structural = evidence.structural
    if structural.get("external_target_used") is not False:
        fail("structural census is not target-blind")
    if structural.get("source_order") != "I0*S3*S3/(2*hbar^2)":
        fail("structural source order drift")
    if structural.get("ordered_pair_count") != 81:
        fail("structural ordered-pair count drift")
    if structural.get("marked_pair_count") != 56:
        fail("structural marked-pair count drift")
    if structural.get("no_descendant_pair_count") != 25:
        fail("structural no-descendant count drift")
    source_letters = tuple(structural.get("source_ports", {}).keys())
    if source_letters != LETTERS:
        fail(f"structural source order drift: {source_letters}")

    no_descendant = evidence.no_descendant
    if no_descendant.get("target_used") is not False:
        fail("no-descendant audit is not target-blind")
    if no_descendant.get("ordered_pair_count") != 25:
        fail("no-descendant row count drift")
    no_descendant_pairs = {row["pair_id"] for row in no_descendant.get("rows", [])}
    expected_no_descendant_pairs = {f"{left}__{right}" for left in NO_DESCENDANT for right in NO_DESCENDANT}
    if no_descendant_pairs != expected_no_descendant_pairs:
        fail("no-descendant pair set drift")
    if any(row.get("anomaly_sector") != "0" for row in no_descendant.get("rows", [])):
        fail("nonzero row entered no-descendant audit")

    ac_ca = evidence.ac_ca
    if ac_ca.get("external_target_used_in_derivation") is not False:
        fail("AC/CA representative used external target in derivation")
    if ac_ca.get("status") != "TARGET_BLIND_COMPLETE_ORDER_G2_ORBIT__HT_UNIT_MATCH":
        fail("AC/CA representative is not complete")
    if ac_ca.get("ordered_results", {}).get("A__C_r") != {"C_r^D>D^E": "-1", "D^D>C_r^E": "+1"}:
        fail("AC forward target-blind result drift")
    if ac_ca.get("ordered_results", {}).get("C_r__A") != {"C_r^D>D^E": "-1", "D^D>C_r^E": "+1"}:
        fail("CA reverse target-blind result drift")

    bb = evidence.bb
    if bb.get("external_target_used_as_input") is not False:
        fail("BB representative used external target as input")
    if bb.get("status") != "PASS_BB_OFFDIAGONAL_DRED_SD_ORBIT_EXACT_HT_MATCH":
        fail("BB off-diagonal representative is not complete")
    if len(bb.get("triangle_result", {}).get("SU3_lift", [])) != 6:
        fail("BB SU(3) lift does not contain six ordered off-diagonal pairs")

    bc_cb = evidence.bc_cb
    if bc_cb.get("external_target_used") is not False:
        fail("BC/CB representative used external target")
    if bc_cb.get("status") != "PASS_BC_CB_REGULATED_SD_KONISHI_EXACT":
        fail("BC/CB representative is not complete")
    if bc_cb.get("blockers") != []:
        fail("BC/CB representative has blockers")

    zero_families = evidence.bb_diagonal_bd_db_zero
    if zero_families.get("external_target_used") is not False:
        fail("BB diagonal / BD / DB exact-zero representative used external target")
    if zero_families.get("project_result_ledger_used") is not False:
        fail("BB diagonal / BD / DB exact-zero representative used Project result ledger")
    if zero_families.get("status") != "PASS_BB_DIAGONAL_BD_DB_TARGET_BLIND_EXACT_ZERO":
        fail("BB diagonal / BD / DB exact-zero representative is not complete")
    if zero_families.get("summary", {}).get("exact_zero_pairs") != 15:
        fail("BB diagonal / BD / DB exact-zero pair count drift")
    if {row["pair_id"] for row in zero_families.get("pair_results", [])} != {
        "B1__B1", "B2__B2", "B3__B3",
        "B1__Ddot1", "B1__Ddot2", "B2__Ddot1", "B2__Ddot2", "B3__Ddot1", "B3__Ddot2",
        "Ddot1__B1", "Ddot1__B2", "Ddot1__B3", "Ddot2__B1", "Ddot2__B2", "Ddot2__B3",
    }:
        fail("BB diagonal / BD / DB exact-zero pair set drift")

    if evidence.aa_status != "ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH":
        fail("AA acceptance status drift")
    aa = evidence.aa
    if aa.get("external_target_used") is not False:
        fail("AA exact representative used external target")
    if aa.get("status") != (
        "TARGET_BLIND_AA_FULL_POLARIZED_TYPED_ORDERED_RECONSTRUCTION_EXACT__"
        "RAW_SD_CONTACT_MULTIPLICITY_ONE_VERIFIED"
    ):
        fail("AA exact representative status drift")
    if aa.get("checks", {}).get("failed") != 0:
        fail("AA exact representative has failed checks")
    typed_aa = aa.get("typed_ordered_reconstruction", {})
    if typed_aa.get("fourier_and_physical_quotient", {}).get(
        "physical_ordered_p_vector_over_lambda1_times_F"
    ) != ["1", "-1"]:
        fail("AA ordered gauge vector drift")
    if aa.get("matter_primitive_sign", {}).get("ordered_vector_over_lambda1_times_F") != ["1", "-1"]:
        fail("AA ordered matter vector drift")
    exhaustive_aa = aa.get("exhaustive_component_replay", {})
    if (
        exhaustive_aa.get("total_full_color_mask_rows"),
        exhaustive_aa.get("total_sparse_replayed_rows"),
        exhaustive_aa.get("total_equality_failures"),
    ) != (9216, 2048, 0):
        fail("AA exhaustive component replay drift")
    ab = evidence.ab_renormalization
    if ab.get("external_target_used_in_derivation") is not False:
        fail("AB/BA finite-renormalization derivation used external target")
    if ab.get("status") != (
        "PASS_TARGET_BLIND_FINITE_PROJECT_WARD_RENORMALIZATION__"
        "AB_BA_HT_CHECK_ONLY_EXACT_MATCH"
    ):
        fail("AB/BA finite-renormalization status drift")
    if ab.get("checks", {}).get("failed") != 0:
        fail("AB/BA finite-renormalization audit has failed checks")
    project_ab = ab.get("project_derivation", {})
    expected_ab_vector = ["1", "1", "-sqrt(2)*i", "sqrt(2)*i"]
    if project_ab.get("basis") != ["D>B1", "B1>D", "C2>C3", "C3>C2"]:
        fail("AB/BA Project basis drift")
    if project_ab.get("renormalized_vector") != expected_ab_vector:
        fail("AB/BA Project-Ward vector drift")
    if project_ab.get("AA_scale") != "1":
        fail("AB/BA target-blind AA scale drift")
    renormalized_ab = ab.get("renormalized_result", {})
    if renormalized_ab.get("AB") != expected_ab_vector or renormalized_ab.get("BA") != expected_ab_vector:
        fail("AB/BA ordered renormalized result drift")
    if ab.get("finite_normal_product", {}).get("independent_anomaly_graph") is not False:
        fail("AB/BA finite normal product was misclassified as an independent graph")
    if ab.get("after_check_only", {}).get("read_after_project_seal") != ab.get("project_seal_sha256"):
        fail("AB/BA HT check was not read after the Project seal")

    g1 = evidence.ab_g1
    if g1.get("external_target_used") is not False or g1.get("checks", {}).get("failed") != 0:
        fail("AB/BA G1 support is not target-blind and exact")
    if g1.get("common_layer", {}).get("new_R1_R2_R3_anomaly_raw_p_q") != ["0", "0"]:
        fail("AB/BA G1 lower-resolvent anomaly drift")

    vector = evidence.ab_vector_frame
    if vector.get("external_target_used") is not False or vector.get("checks", {}).get("failed") != 0:
        fail("AB/BA vector-frame support is not target-blind and exact")
    if vector.get("status") != (
        "PASS_VECTOR_FRAME_ORBIT_HAS_ONLY_DB_BD_SUPPORT__CANNOT_SUPPLY_REQUESTED_CC_HALF"
    ):
        fail("AB/BA vector-frame support status drift")

    g3_measure = evidence.ab_g3_measure
    if g3_measure.get("external_target_used") is not False or g3_measure.get("checks", {}).get("failed") != 0:
        fail("AB/BA G3 measure support is not target-blind and exact")
    if g3_measure.get("verdict", {}).get("c_G3") != "4096":
        fail("AB/BA G3 full-measure normalization drift")

    g3_typed = evidence.ab_g3_typed
    if g3_typed.get("external_target_used") is not False or g3_typed.get("checks", {}).get("failed") != 0:
        fail("AB/BA G3 typed support is not target-blind and exact")
    if g3_typed.get("corrected_coefficients_lambda1", {}).get("G32_typed_C2_gt_C3") != "-2*sqrt(2)*i":
        fail("AB/BA G3 C2>C3 typed coefficient drift")
    if g3_typed.get("corrected_coefficients_lambda1", {}).get("G33_typed_C3_gt_C2") != "2*sqrt(2)*i":
        fail("AB/BA G3 C3>C2 typed coefficient drift")
    if evidence.ad_da.get("external_target_used") is not False:
        fail("AD/DA representative used external target")
    if evidence.ad_da.get("status") != (
        "PASS_TARGET_BLIND_AD_DA_FULL_CHIRALITY_RAW_CONTACT_AND_LINK__"
        "HOLOMORPHIC_TWIST_COEFFICIENTS_MATCH"
    ):
        fail("AD/DA completed representative status drift")
    if evidence.ad_da_status != evidence.ad_da.get("status"):
        fail("AD/DA JSON/Markdown status mismatch")
    if evidence.ad_da.get("checks", {}).get("failed") != 0:
        fail("AD/DA completed representative has failed checks")
    ad_da_result = evidence.ad_da.get("result", {})
    if ad_da_result.get("canonical_physical_AD") != (
        "lambda1*F^{AB}_{DE}*[(1/3)<P_dot_a D^D,D^E>+(2/3)<D^D,P_dot_a D^E>]"
    ):
        fail("AD ordered result drift")
    if ad_da_result.get("canonical_physical_DA") != (
        "lambda1*F^{AB}_{DE}*[(2/3)<P_dot_a D^D,D^E>+(1/3)<D^D,P_dot_a D^E>]"
    ):
        fail("DA ordered result drift")
    ad_da_contact = evidence.ad_da_raw_contact
    if ad_da_contact.get("external_target_used") is not False:
        fail("AD/DA raw-contact representative used external target")
    if ad_da_contact.get("status") != (
        "PASS_RAW_LOCAL_CONTACT_MULTIPLICITY_ONE__FINITE_W_LINK_LONGITUDINAL_ZERO"
    ):
        fail("AD/DA raw-contact multiplicity status drift")
    if evidence.ad_da_raw_contact_status != ad_da_contact.get("status"):
        fail("AD/DA raw-contact JSON/Markdown status mismatch")
    if ad_da_contact.get("checks", {}).get("failed") != 0:
        fail("AD/DA raw-contact representative has failed checks")
    if ad_da_contact.get("normalization_consequence", {}).get("m_contact") != "1":
        fail("AD/DA raw Schwinger contact multiplicity drift")

    return evidence


def base_transport(*, letter_index: str, coefficient_sign: str = "+1") -> dict[str, str]:
    return {
        "letter_index": letter_index,
        "source_slot_map": "L->L;R->R;ORDER_REVERSAL_NOT_USED",
        "koszul_sign": "+1 (no source-slot exchange)",
        "color_map": "(A,B,D,E)->(A,B,D,E); F^(AB)_(DE) unchanged",
        "coefficient_sign": coefficient_sign,
    }


def open_row(
    *,
    ordinal: int,
    left: str,
    right: str,
    orbit_id: str,
    representative: str,
    maturity: str,
    blocker: str,
    evidence: list[str],
    transport: dict[str, str],
) -> dict[str, Any]:
    return {
        "ordinal": ordinal,
        "pair_id": f"{left}__{right}",
        "left": left,
        "right": right,
        "family_pair": f"{family(left)}>{family(right)}",
        "parities": [PARITY[left], PARITY[right]],
        "marked_terms": marked_terms(left, right),
        "orbit_id": orbit_id,
        "representative": representative,
        "transport": transport,
        "final_state": "OPEN",
        "representative_maturity": maturity,
        "resolution": "UNRESOLVED",
        "result": None,
        "cutting_failure_certificate": None,
        "blocker": blocker,
        "evidence": evidence,
    }


def complete_row(
    *,
    ordinal: int,
    left: str,
    right: str,
    orbit_id: str,
    representative: str,
    resolution: str,
    result: dict[str, Any],
    cutting_failure_certificate: str,
    evidence: list[str],
    transport: dict[str, str],
) -> dict[str, Any]:
    return {
        "ordinal": ordinal,
        "pair_id": f"{left}__{right}",
        "left": left,
        "right": right,
        "family_pair": f"{family(left)}>{family(right)}",
        "parities": [PARITY[left], PARITY[right]],
        "marked_terms": marked_terms(left, right),
        "orbit_id": orbit_id,
        "representative": representative,
        "transport": transport,
        "final_state": "COMPLETE_EXACT",
        "representative_maturity": "COMPLETED",
        "resolution": resolution,
        "result": result,
        "cutting_failure_certificate": cutting_failure_certificate,
        "blocker": None,
        "evidence": evidence,
    }


def classify_pair(ordinal: int, left: str, right: str, evidence: Evidence) -> dict[str, Any]:
    lf, rf = family(left), family(right)
    pair_id = f"{left}__{right}"

    if left in NO_DESCENDANT and right in NO_DESCENDANT:
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"NO_DESCENDANT::{lf}>{rf}",
            representative="(X,Y) in {C1,C2,C3,Ddot1,Ddot2}^2",
            resolution="EXACT_ZERO",
            result={"basis": ["anomaly_sector"], "coefficients_over_lambda1": ["0"], "formula": "0"},
            cutting_failure_certificate="nabla_-X=nabla_-Y=0; marked_inverse_kernel_count=0",
            evidence=["audits/step5-no-descendant-pairs-exact.json"],
            transport=base_transport(letter_index="DIRECT_UNIVERSAL_LEMMA; no coefficient transport"),
        )

    if (lf, rf) in {("A", "C"), ("C", "A")}:
        r = component(right if rf == "C" else left)
        perm = cyclic_flavor_map(r)
        orientation = "A__C1" if lf == "A" else "C1__A"
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"AC_CA::{lf}>{rf}",
            representative=orientation,
            resolution="EXACT_NONZERO",
            result={
                "basis": ["(P_dot C_r)^D D^(E dot)", "D_dot^D (P^dot C_r)^E"],
                "coefficients_over_lambda1": ["-1", "+1"],
                "formula": "lambda1*F^(AB)_(DE)*[D_dot^D(P^dot C_r)^E-(P_dot C_r)^D D^(E dot)]",
            },
            cutting_failure_certificate="single completed TMM metric-pole orbit; J_mu2=1/(32*pi^2)",
            evidence=["audits/step5-ac-ca-family-exact.json"],
            transport=base_transport(letter_index=f"flavor pi:(1,2,3)->{perm}; C1->C{r}"),
        )

    if lf == "B" and rf == "B":
        r, s = component(left), component(right)
        if r != s:
            t = 6 - r - s
            eps = epsilon3(r, s, t)
            bb_lift = {
                row["pair"]: row for row in evidence.bb["triangle_result"]["SU3_lift"]
            }
            source = bb_lift[pair_id]
            if source["epsilon"] != eps:
                fail(f"BB epsilon drift for {pair_id}")
            return complete_row(
                ordinal=ordinal,
                left=left,
                right=right,
                orbit_id="BB_OFFDIAGONAL",
                representative="B1__B2",
                resolution="EXACT_NONZERO",
                result={
                    "basis": ["<D^D,C_t^E>", "<C_t^D,D^E>"],
                    "coefficients_over_lambda1": [
                        source["triangle_DC_over_lambda1"],
                        source["triangle_CD_over_lambda1"],
                    ],
                    "formula": "epsilon_rst*lambda1*F^(AB)_(DE)*[-i*sqrt(2)<D^D,C_t^E>+i*sqrt(2)<C_t^D,D^E>]",
                },
                cutting_failure_certificate="completed direct plus transported marked-edge DRED SD orbit",
                evidence=["audits/step5-bb-offdiagonal-family-exact.json"],
                transport=base_transport(
                    letter_index=f"flavor pi:(1,2,3)->{distinct_flavor_map(r,s)}; (B1,B2,C3)->(B{r},B{s},C{t})",
                    coefficient_sign=f"epsilon_{r}{s}{t}={eps}; Koszul source-order sign not used",
                ),
            )
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id="BB_DIAGONAL_EXACT_ZERO",
            representative="B1__B1",
            resolution="EXACT_ZERO",
            result={"basis": ["anomaly_sector"], "coefficients_over_lambda1": ["0"], "formula": "0"},
            cutting_failure_certificate="TMM left/right projected D-words vanish; epsilon_rru=epsilon_rtr=0; all spectator parents 1PR",
            evidence=["audits/step5-bbdiagonal-bd-db-exact-zero.json"],
            transport=base_transport(letter_index=f"flavor pi:(1,2,3)->{cyclic_flavor_map(r)}; B1->B{r}"),
        )

    if (lf, rf) in {("B", "C"), ("C", "B")}:
        r = component(left if lf == "B" else right)
        s = component(right if rf == "C" else left)
        delta = int(r == s)
        if r == s:
            index_map = f"diagonal flavor pi:(1,2,3)->{cyclic_flavor_map(r)}; (B1,C1)->(B{r},C{s})"
            representative = "B1__C1" if lf == "B" else "C1__B1"
        else:
            index_map = f"off-diagonal flavor pi:(1,2,3)->{distinct_flavor_map(r,s)}; (B1,C2)->(B{r},C{s})"
            representative = "B1__C2" if lf == "B" else "C2__B1"
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"BC_CB::{lf}>{rf}::delta={delta}",
            representative=representative,
            resolution="EXACT_NONZERO" if delta else "EXACT_ZERO",
            result={
                "basis": ["<D^D,D^E>"],
                "coefficients_over_lambda1": [str(delta)],
                "formula": "delta_rs*lambda1*F^(AB)_(DE)*<D^D,D^E>",
            },
            cutting_failure_certificate=(
                "regulated antichiral density divergence leaves mu_l^2/D0 and J_mu2=1/(32*pi^2)"
                if delta
                else "functional derivative flavor factor delta_rs=0 before integration"
            ),
            evidence=["audits/step5-bc-full-family-raw-projection-exact.json"],
            transport=base_transport(letter_index=index_map),
        )

    if left == "A" and right == "A":
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id="AA_FULL_TARGET_BLIND",
            representative="A__A",
            resolution="EXACT_NONZERO",
            result={
                "basis": [
                    "<D^D,A^E>",
                    "<A^D,D^E>",
                    "<B1^D,C1^E>",
                    "<C1^D,B1^E>",
                    "<B2^D,C2^E>",
                    "<C2^D,B2^E>",
                    "<B3^D,C3^E>",
                    "<C3^D,B3^E>",
                ],
                "coefficients_over_lambda1": ["1", "-1", "1", "-1", "1", "-1", "1", "-1"],
                "formula": (
                    "lambda1*F^(AB)_(DE)*[<D^D,A^E>-<A^D,D^E>"
                    "+sum_r(<B_r^D,C_r^E>-<C_r^D,B_r^E>)]"
                ),
            },
            cutting_failure_certificate=(
                "raw Schwinger contact multiplicity m0=m2=1; "
                "N_full,e+K_raw,e=Q_e*(bar(r_e)^2-r_(e,d)^2)=Q_e*mu_l^2"
            ),
            evidence=[
                "audits/step5-aa-standard-feynman-strictification.md",
                "audits/step5-aa-external-slot-decomposition-exact.json",
            ],
            transport=base_transport(letter_index="identity"),
        )

    if (lf, rf) in {("A", "B"), ("B", "A")}:
        r = component(right if rf == "B" else left)
        _, s, t = cyclic_flavor_map(r)
        representative = "A__B1" if lf == "A" else "B1__A"
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"AB_BA_PROJECT_WARD_RENORMALIZED::{lf}>{rf}",
            representative=representative,
            resolution="EXACT_NONZERO",
            result={
                "basis": [
                    f"<D^D,B{r}^E>",
                    f"<B{r}^D,D^E>",
                    f"<C{s}^D,C{t}^E>",
                    f"<C{t}^D,C{s}^E>",
                ],
                "coefficients_over_lambda1": ["1", "1", "-sqrt(2)*I", "sqrt(2)*I"],
                "formula": (
                    "lambda1*F^(AB)_(DE)*[<D^D,B_r^E>+<B_r^D,D^E>"
                    "-i*sqrt(2)*epsilon_rst*<C_s^D,C_t^E>]"
                ),
            },
            cutting_failure_certificate=(
                "raw G1/G2/G3 carriers arise from DRED mu_l^2 cutting failures; "
                "the unique finite Project-Ward normal-product change is not an independent anomaly graph"
            ),
            evidence=[
                "audits/step5-ab-ba-project-ward-finite-renormalization-exact.json",
                "audits/step5-ab-ba-vector-frame-missing-orbit-exact.json",
                "audits/step5-ab-ba-g1-actual-resolvent-contact-orbit-exact.json",
                "audits/step5-ab-ba-g3-original-full-measure-equivalence-exact.json",
                "audits/step5-ab-ba-g3-gate7-normalization-first-error-exact.json",
            ],
            transport=base_transport(letter_index=f"flavor pi:(1,2,3)->{cyclic_flavor_map(r)}; B1->B{r}"),
        )

    if (lf, rf) in {("A", "D"), ("D", "A")}:
        dot = component(right if rf == "D" else left)
        representative = "A__Ddot1" if lf == "A" else "Ddot1__A"
        coefficients = ["1/3", "2/3"] if lf == "A" else ["2/3", "1/3"]
        formula = (
            "lambda1*F^(AB)_(DE)*[(1/3)<P_dot_a D^D,D^E>+(2/3)<D^D,P_dot_a D^E>]"
            if lf == "A"
            else "lambda1*F^(AB)_(DE)*[(2/3)<P_dot_a D^D,D^E>+(1/3)<D^D,P_dot_a D^E>]"
        )
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"AD_DA_FULL::{lf}>{rf}",
            representative=representative,
            resolution="EXACT_NONZERO",
            result={
                "basis": ["<P_dot_a D^D,D^E>", "<D^D,P_dot_a D^E>"],
                "coefficients_over_lambda1": coefficients,
                "formula": formula,
            },
            cutting_failure_certificate=(
                "raw local Schwinger contact multiplicity m_parent=m_contact=1; "
                "R*bar(r_e)^2/P3-R/P_hat_e=R*mu_l^2/P3 and the full-d gate is zero"
            ),
            evidence=[
                "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.json",
                "audits/step5-ad-da-ordered-ports-crossed-hessian-exact.md",
                "audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.json",
                "audits/step5-ad-da-raw-contact-hessian-multiplicity-exact.md",
            ],
            transport=base_transport(letter_index=f"dotted S:{dotted_map(dot)}; Ddot1->Ddot{dot}"),
        )

    if (lf, rf) in {("B", "D"), ("D", "B")}:
        r = component(left if lf == "B" else right)
        dot = component(right if rf == "D" else left)
        representative = "B1__Ddot1" if lf == "B" else "Ddot1__B1"
        return complete_row(
            ordinal=ordinal,
            left=left,
            right=right,
            orbit_id=f"BD_DB_EXACT_ZERO::{lf}>{rf}",
            representative=representative,
            resolution="EXACT_ZERO",
            result={"basis": ["anomaly_sector"], "coefficients_over_lambda1": ["0"], "formula": "0"},
            cutting_failure_certificate="TGM/TMM/TMH/quartic projected D-words vanish; potential pair cancels; spectator parents 1PR",
            evidence=["audits/step5-bbdiagonal-bd-db-exact-zero.json"],
            transport=base_transport(
                letter_index=f"flavor pi:(1,2,3)->{cyclic_flavor_map(r)}; B1->B{r}; dotted S:{dotted_map(dot)}"
            ),
        )

    fail(f"unclassified pair {pair_id}")
    raise AssertionError(pair_id)


def representative_table(evidence: Evidence) -> list[dict[str, Any]]:
    return [
        {
            "family": "AA",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "full gauge-plus-three-flavor matter ordered vector (1,-1,1,-1,1,-1,1,-1)",
            "blocker": None,
            "status_source": evidence.aa_status,
        },
        {
            "family": "AB/BA",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "six flavor-covariant ordered rows on the Project-Ward-renormalized vector (1,1,-i*sqrt(2),+i*sqrt(2))",
            "blocker": None,
            "status_source": evidence.ab_renormalization["status"],
        },
        {
            "family": "AC/CA",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "full order-g^2 orbit",
            "blocker": None,
            "status_source": evidence.ac_ca["status"],
        },
        {
            "family": "AD/DA",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "four dotted ordered pairs with raw contact multiplicity one and finite W-link longitudinal zero",
            "blocker": None,
            "status_source": evidence.ad_da["status"],
        },
        {
            "family": "BB off-diagonal",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "six ordered epsilon_rst components",
            "blocker": None,
            "status_source": evidence.bb["status"],
        },
        {
            "family": "BB diagonal",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "three exact zeros; TMM D-words zero and epsilon repeated-index H routes zero",
            "blocker": None,
            "status_source": evidence.bb_diagonal_bd_db_zero["status"],
        },
        {
            "family": "BC/CB",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "all eighteen delta_rs components",
            "blocker": None,
            "status_source": evidence.bc_cb["status"],
        },
        {
            "family": "BD/DB",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "twelve exact zeros; 399 typed routes and 117 symbolic D-word checks",
            "blocker": None,
            "status_source": evidence.bb_diagonal_bd_db_zero["status"],
        },
        {
            "family": "CC/CD/DC/DD",
            "maturity": "COMPLETED",
            "final_state": "COMPLETE_EXACT",
            "locally_proved_subresult": "twenty-five no-descendant exact zeros",
            "blocker": None,
            "status_source": evidence.no_descendant["status"],
        },
    ]


def build_payload() -> dict[str, Any]:
    evidence = read_evidence()
    rows: list[dict[str, Any]] = []
    ordinal = 0
    for left in LETTERS:
        for right in LETTERS:
            ordinal += 1
            rows.append(classify_pair(ordinal, left, right, evidence))

    final_states = Counter(row["final_state"] for row in rows)
    resolutions = Counter(row["resolution"] for row in rows)
    maturities = Counter(row["representative_maturity"] for row in rows)
    family_states: dict[str, dict[str, int]] = {}
    for family_pair in sorted({row["family_pair"] for row in rows}):
        bucket = [row for row in rows if row["family_pair"] == family_pair]
        family_states[family_pair] = dict(sorted(Counter(row["final_state"] for row in bucket).items()))

    payload = {
        "schema": "awi.step5.global-81-target-blind-representative-orbit-ledger.v1",
        "authority_status": "LOCAL_PROPOSAL_FROM_DIRTY_WORKTREE; NOT_ORIGIN_MAIN_AUTHORITY",
        "frozen_base": "origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66",
        "proposal_start_head": "6bb93d8df5a05af709a364be0d387795a5e18842",
        "external_target_used": False,
        "project_result_ledger_used": False,
        "coefficient_policy": "coefficient only from completed target-blind representative audit; every unresolved result is null",
        "letters": [
            {
                "id": letter,
                "family": family(letter),
                "parity": PARITY[letter],
                "has_outer_nabla_minus_descendant": letter in ACTIVE_DESCENDANT,
            }
            for letter in LETTERS
        ],
        "graded_leibniz": "nabla_-(L_i L_j)=(nabla_-L_i)L_j+(-1)^|L_i| L_i(nabla_-L_j)",
        "symmetry_maps": {
            "FLAVOR": {
                "letter_index": "B_r->B_pi(r), C_r->C_pi(r)",
                "epsilon": "epsilon_123=+1 -> epsilon_pi(1)pi(2)pi(3)=sgn(pi)",
                "delta": "delta_rs -> delta_pi(r)pi(s)=delta_rs",
                "koszul_sign": "+1 because source slots are not exchanged",
                "color": "identity on (A,B,D,E)",
            },
            "DOTTED": {
                "letter_index": "D_dota->S_dota^dotb D_dotb",
                "coefficient": "scalar coefficient unchanged",
                "koszul_sign": "+1 because source slots are not exchanged",
                "color": "identity on (A,B,D,E)",
            },
            "ORDER_REBASE_RECORDED_BUT_NOT_USED": {
                "source": "(L_i^A,L_j^B)->(L_j^B,L_i^A)",
                "source_koszul": "(-1)^(|L_i||L_j|)",
                "descendant_marks": "left sign=+1; right sign=(-1)^|L_i|",
                "color": "(A,B,D,E)->(B,A,E,D)",
                "rule": "no reverse coefficient inferred; completed reverse orientations have independent representative rows",
            },
        },
        "representatives": representative_table(evidence),
        "rows": rows,
        "summary": {
            "ordered_pairs": len(rows),
            "unique_pairs": len({row["pair_id"] for row in rows}),
            "final_state_counts": dict(sorted(final_states.items())),
            "resolution_counts": dict(sorted(resolutions.items())),
            "representative_maturity_counts": dict(sorted(maturities.items())),
            "family_state_counts": family_states,
            "structural_marked_pairs": evidence.structural["marked_pair_count"],
            "structural_no_descendant_pairs": evidence.structural["no_descendant_pair_count"],
            "structural_directed_parent_routes": evidence.structural["directed_parent_route_count"],
        },
        "evidence_inputs": [str(path.relative_to(ROOT)) for path in INPUT_PATHS],
    }
    validate_payload(payload)
    return payload


def validate_payload(payload: dict[str, Any]) -> None:
    rows = payload["rows"]
    if len(rows) != 81:
        fail(f"ledger rows={len(rows)}, expected 81")
    if len({row["pair_id"] for row in rows}) != 81:
        fail("ordered pair ids are not unique")
    expected_pairs = {f"{left}__{right}" for left in LETTERS for right in LETTERS}
    if {row["pair_id"] for row in rows} != expected_pairs:
        fail("ledger is not the full 9x9 Cartesian product")
    if [row["ordinal"] for row in rows] != list(range(1, 82)):
        fail("ordinal sequence drift")

    final_states = Counter(row["final_state"] for row in rows)
    if final_states != Counter({"COMPLETE_EXACT": 81}):
        fail(f"final-state counts drift: {final_states}")
    resolutions = Counter(row["resolution"] for row in rows)
    if resolutions != Counter({"EXACT_ZERO": 52, "EXACT_NONZERO": 29}):
        fail(f"resolution counts drift: {resolutions}")
    maturities = Counter(row["representative_maturity"] for row in rows)
    if maturities != Counter({"COMPLETED": 81}):
        fail(f"representative maturity counts drift: {maturities}")

    for row in rows:
        if row["final_state"] == "OPEN":
            if row["result"] is not None:
                fail(f"OPEN row has a result: {row['pair_id']}")
            if not row["blocker"].startswith("OPEN_"):
                fail(f"OPEN row lacks OPEN blocker: {row['pair_id']}")
        else:
            if row["result"] is None:
                fail(f"complete row lacks result: {row['pair_id']}")
            if row["blocker"] is not None:
                fail(f"complete row has blocker: {row['pair_id']}")

    no_descendant_rows = [row for row in rows if row["left"] in NO_DESCENDANT and row["right"] in NO_DESCENDANT]
    if len(no_descendant_rows) != 25 or any(row["resolution"] != "EXACT_ZERO" for row in no_descendant_rows):
        fail("no-descendant exact-zero closure drift")

    by_pair = {row["pair_id"]: row for row in rows}
    aa_row = by_pair["A__A"]
    if aa_row["result"]["coefficients_over_lambda1"] != ["1", "-1", "1", "-1", "1", "-1", "1", "-1"]:
        fail("AA exact ordered vector drift")
    for dot in (1, 2):
        if by_pair[f"A__Ddot{dot}"]["result"]["coefficients_over_lambda1"] != ["1/3", "2/3"]:
            fail(f"AD exact ordered vector drift for dot{dot}")
        if by_pair[f"Ddot{dot}__A"]["result"]["coefficients_over_lambda1"] != ["2/3", "1/3"]:
            fail(f"DA exact ordered vector drift for dot{dot}")
    ab_rows = [
        row for row in rows
        if (family(row["left"]), family(row["right"])) in {("A", "B"), ("B", "A")}
    ]
    if len(ab_rows) != 6 or any(row["final_state"] != "COMPLETE_EXACT" for row in ab_rows):
        fail("AB/BA completed-family boundary drift")
    if any(
        row["result"]["coefficients_over_lambda1"] != ["1", "1", "-sqrt(2)*I", "sqrt(2)*I"]
        for row in ab_rows
    ):
        fail("AB/BA completed ordered-vector drift")

    bb_offdiagonal = [
        row
        for row in rows
        if family(row["left"]) == family(row["right"]) == "B" and row["left"] != row["right"]
    ]
    if len(bb_offdiagonal) != 6 or any(row["resolution"] != "EXACT_NONZERO" for row in bb_offdiagonal):
        fail("BB off-diagonal closure drift")
    bb_diagonal = [
        row
        for row in rows
        if family(row["left"]) == family(row["right"]) == "B" and row["left"] == row["right"]
    ]
    if len(bb_diagonal) != 3 or any(row["resolution"] != "EXACT_ZERO" for row in bb_diagonal):
        fail("BB diagonal exact-zero closure drift")

    for path in payload["evidence_inputs"]:
        if path in {
            "generated/step5/project-result-ledger.json",
            "generated/step5/ht_ordered_pair_targets.json",
        }:
            fail(f"forbidden result ledger used: {path}")
    if payload["external_target_used"] is not False or payload["project_result_ledger_used"] is not False:
        fail("target/result-engine boundary drift")


def compact_result(row: dict[str, Any]) -> str:
    if row["result"] is None:
        return "null"
    coefficients = ",".join(row["result"]["coefficients_over_lambda1"])
    return f"[{coefficients}]"


def compact_transport(row: dict[str, Any]) -> str:
    transport = row["transport"]
    return f"{transport['letter_index']}; K={transport['koszul_sign']}; color={transport['color_map']}; sign={transport['coefficient_sign']}"


def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload["summary"]
    lines = [
        "# Step 5 target-blind global 9x9 representative-orbit ledger",
        "",
        "Status: `LOCAL_PROPOSAL__81_COMPLETE_EXACT__0_OPEN__NO_TARGET_FILL`.",
        "",
        "Authority: `origin/main@00000f748fe4bdd1b5d122663cc1fb814faace66` is the frozen authority base; this dirty-worktree ledger is not authoritative.",
        "",
        "## 1. Definitions",
        "",
        "$$",
        "\\mathbb L=(A,B_1,B_2,B_3,C_1,C_2,C_3,D_{\\dot1},D_{\\dot2}),",
        "\\qquad",
        "|A|=|C_r|=0,\\quad |B_r|=|D_{\\dot a}|=1.",
        "$$",
        "",
        "$$",
        "\\nabla_-(L_iL_j)=(\\nabla_-L_i)L_j+(-1)^{|L_i|}L_i(\\nabla_-L_j).",
        "$$",
        "",
        "$$",
        "\\mu_\\ell^2:=\\bar\\ell^2-\\ell_d^2,\\qquad",
        "J_{\\mu^2}=\\mu^{2\\epsilon}\\int\\frac{d^d\\ell}{(2\\pi)^d}",
        "\\frac{\\mu_\\ell^2}{(\\ell_d^2+\\Delta)^3}=\\frac1{32\\pi^2}.",
        "$$",
        "",
        "Coefficient policy: only completed target-blind representative audits may populate a result. Every incomplete pair has `result=null` and `final_state=OPEN`.",
        "",
        "Forbidden inputs: `generated/step5/project-result-ledger.json` and `generated/step5/ht_ordered_pair_targets.json`.",
        "",
        "## 2. Symmetry and transport maps",
        "",
        "| map | letter/index transport | Koszul/sign | color transport | inference rule |",
        "|---|---|---|---|---|",
        "| `FLAVOR` | `B_r->B_pi(r)`, `C_r->C_pi(r)`; `epsilon_123->epsilon_pi(1)pi(2)pi(3)`; `delta_rs->delta_pi(r)pi(s)` | `+1`; source slots fixed; `epsilon` component supplies `sgn(pi)` | `(A,B,D,E)` fixed; `F^(AB)_(DE)` fixed | allowed only for a completed flavor-covariant representative |",
        "| `DOTTED` | `D_dota->S_dota^dotb D_dotb` | `+1`; source slots fixed; scalar coefficient fixed | `(A,B,D,E)` fixed | allowed only for a completed dotted-spinor representative |",
        "| `ORDER_REBASE` | `(L_i^A,L_j^B)->(L_j^B,L_i^A)` | source exchange `(-1)^(|L_i||L_j|)`; right descendant sign `(-1)^|L_i|` | `(A,B,D,E)->(B,A,E,D)` | recorded only; never used here to infer a reverse coefficient |",
        "",
        "Completed `AC/CA` and `BC/CB` reverse orders are independently routed in their audits. Completed reverse off-diagonal `BB` rows come from fixed-slot flavor transport, not source-slot reversal.",
        "",
        "## 3. Representative gates",
        "",
        "| family | maturity | final | proved local subresult | blocker |",
        "|---|---|---|---|---|",
    ]
    for rep in payload["representatives"]:
        lines.append(
            "| `{family}` | `{maturity}` | `{final_state}` | {proved} | {blocker} |".format(
                family=rep["family"],
                maturity=rep["maturity"],
                final_state=rep["final_state"],
                proved=f"`{rep['locally_proved_subresult']}`" if rep["locally_proved_subresult"] else "`null`",
                blocker=f"`{rep['blocker']}`" if rep["blocker"] else "`null`",
            )
        )
    lines.extend(
        [
            "",
            "## 4. Exact completed formulas",
            "",
            "$$",
            "\\Delta(A,A)=\\lambda_1\\mathbb F^{AB}{}_{DE}\\Big[",
            "\\langle D^D,A^E\\rangle-\\langle A^D,D^E\\rangle",
            "+\\sum_{r=1}^3(\\langle B_r^D,C_r^E\\rangle-\\langle C_r^D,B_r^E\\rangle)\\Big].",
            "$$",
            "",
            "$$",
            "\\Delta(A,B_r)=\\Delta(B_r,A)",
            "=\\lambda_1\\mathbb F^{AB}{}_{DE}\\left[",
            "\\langle D^D,B_r^E\\rangle+\\langle B_r^D,D^E\\rangle",
            "-i\\sqrt2\\,\\epsilon_{rst}\\langle C_s^D,C_t^E\\rangle\\right].",
            "$$",
            "",
            "$$",
            "\\Delta(A,C_r)=\\Delta(C_r,A)",
            "=\\lambda_1\\mathbb F^{AB}{}_{DE}",
            "\\left[D_{\\dot a}^D(P^{\\dot a}C_r)^E-(P_{\\dot a}C_r)^D D^{E\\dot a}\\right].",
            "$$",
            "",
            "$$",
            "\\Delta(B_r,B_s)_{r\\ne s}",
            "=\\epsilon_{rst}\\lambda_1\\mathbb F^{AB}{}_{DE}",
            "\\left[-i\\sqrt2\\langle D^D,C_t^E\\rangle+i\\sqrt2\\langle C_t^D,D^E\\rangle\\right].",
            "$$",
            "",
            "$$",
            "\\Delta(B_r,C_s)=\\Delta(C_s,B_r)",
            "=\\delta_{rs}\\lambda_1\\mathbb F^{AB}{}_{DE}\\langle D^D,D^E\\rangle.",
            "$$",
            "",
            "$$",
            "\\Delta(A,D_{\\dot a})=\\lambda_1\\mathbb F^{AB}{}_{DE}",
            "\\left[\\frac13\\langle P_{\\dot a}D^D,D^E\\rangle",
            "+\\frac23\\langle D^D,P_{\\dot a}D^E\\rangle\\right].",
            "$$",
            "",
            "$$",
            "\\Delta(D_{\\dot a},A)=\\lambda_1\\mathbb F^{AB}{}_{DE}",
            "\\left[\\frac23\\langle P_{\\dot a}D^D,D^E\\rangle",
            "+\\frac13\\langle D^D,P_{\\dot a}D^E\\rangle\\right].",
            "$$",
            "",
            "$$",
            "\\Delta(B_r,B_r)=\\Delta(B_r,D_{\\dot a})=\\Delta(D_{\\dot a},B_r)=0.",
            "$$",
            "",
            "$$",
            "\\Delta(X,Y)=0,\\qquad X,Y\\in\\{C_1,C_2,C_3,D_{\\dot1},D_{\\dot2}\\}.",
            "$$",
            "",
            "## 5. All 81 ordered pairs",
            "",
            "`result` lists the coefficient vector divided by `lambda1`; `null` is not a zero.",
            "",
            "| # | pair | marks `(side,sign)` | orbit / representative | transport | maturity | final / resolution | result | blocker/evidence |",
            "|---:|---|---|---|---|---|---|---|---|",
        ]
    )
    for row in payload["rows"]:
        marks = ",".join(f"{mark['side']}:{mark['leibniz_sign']:+d}" for mark in row["marked_terms"]) or "none"
        blocker_evidence = row["blocker"] or ",".join(row["evidence"])
        lines.append(
            f"| {row['ordinal']:03d} | `{row['pair_id']}` | `{marks}` | `{row['orbit_id']}` / `{row['representative']}` | "
            f"`{compact_transport(row)}` | `{row['representative_maturity']}` | "
            f"`{row['final_state']}` / `{row['resolution']}` | `{compact_result(row)}` | `{blocker_evidence}` |"
        )
    lines.extend(
        [
            "",
            "## 6. Deterministic counts",
            "",
            "$$",
            "81=81_{\\mathrm{COMPLETE\\_EXACT}}+0_{\\mathrm{OPEN}}.",
            "$$",
            "",
            "$$",
            "81=29_{\\mathrm{EXACT\\_NONZERO}}+52_{\\mathrm{EXACT\\_ZERO}}.",
            "$$",
            "",
            "$$",
            "81=81_{\\mathrm{COMPLETED}}+0_{\\mathrm{UNRESOLVED}}.",
            "$$",
            "",
            f"Structural census: `{summary['structural_marked_pairs']}` marked pairs, `{summary['structural_no_descendant_pairs']}` no-descendant pairs, `{summary['structural_directed_parent_routes']}` directed parent routes.",
            "",
            "Verification:",
            "",
            "```text",
            "python scripts/step5_global_81_target_blind_orbit_ledger_audit.py --check",
            "python -m unittest tests.test_step5_global_81_target_blind_orbit_ledger",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def render_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def check_artifacts(payload: dict[str, Any]) -> None:
    expected_json = render_json(payload)
    expected_md = render_markdown(payload)
    if not AUDIT_JSON.is_file() or AUDIT_JSON.read_text(encoding="utf-8") != expected_json:
        fail(f"stale generated artifact: {AUDIT_JSON.relative_to(ROOT)}")
    if not AUDIT_MD.is_file() or AUDIT_MD.read_text(encoding="utf-8") != expected_md:
        fail(f"stale generated artifact: {AUDIT_MD.relative_to(ROOT)}")


def write_artifacts(payload: dict[str, Any]) -> None:
    AUDIT_JSON.write_text(render_json(payload), encoding="utf-8")
    AUDIT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    payload = build_payload()
    if args.write:
        write_artifacts(payload)
    else:
        check_artifacts(payload)

    summary = payload["summary"]
    print(f"PASS ordered_pairs={summary['ordered_pairs']}")
    print(f"PASS unique_pairs={summary['unique_pairs']}")
    print(f"PASS complete_exact={summary['final_state_counts']['COMPLETE_EXACT']}")
    print(f"PASS open={summary['final_state_counts'].get('OPEN', 0)}")
    print(f"PASS exact_nonzero={summary['resolution_counts']['EXACT_NONZERO']}")
    print(f"PASS exact_zero={summary['resolution_counts']['EXACT_ZERO']}")
    print(f"PASS unresolved={summary['resolution_counts'].get('UNRESOLVED', 0)}")
    print(f"PASS completed_representatives={summary['representative_maturity_counts']['COMPLETED']}")
    print(f"PASS conditional_representatives={summary['representative_maturity_counts'].get('CONDITIONAL', 0)}")
    print(f"PASS unresolved_representatives={summary['representative_maturity_counts'].get('UNRESOLVED', 0)}")
    print("PASS external_target_used=false")
    print("PASS project_result_ledger_used=false")
    print("PASS all_rows_have_exact_results=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
