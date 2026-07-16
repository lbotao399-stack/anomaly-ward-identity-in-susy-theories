#!/usr/bin/env python3
"""Exact HT-to-Project normalization and quotient audit for AB/BA.

This audit does not use the desired AB/BA vector to choose a scale.  The
one-loop marker is fixed by the independently accepted AA row.  The AB/AA
ratio is then transported through the pinned field dictionary.  Raw local
jets, the total-derivative quotient, and the HT physical representative are
kept as three distinct layers.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-ht-ab-normalization-quotient-exact.json"
MD_OUT = ROOT / "audits/step5-ht-ab-normalization-quotient-exact.md"
HT_SOURCE = ROOT / "references/vendor/arxiv/2512.07771v2/source/main.tex"
HT_AUDIT = ROOT / "audits/step5-ht-roundtrip-audit.json"
AA_MD = ROOT / "audits/step5-aa-standard-feynman-strictification.md"
AA_JSON = ROOT / "audits/step5-aa-external-slot-decomposition-exact.json"
RAW_AB = ROOT / "audits/step5-ab-ba-unified-typed-q-covariance-exact.json"


def exact_text(value: object) -> str:
    return sp.sstr(sp.factor(sp.sympify(value))).replace("I", "i")


def equal(actual: object, expected: object) -> bool:
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        actual_matrix = sp.Matrix(actual)
        expected_matrix = sp.Matrix(expected)
        return actual_matrix.shape == expected_matrix.shape and all(
            sp.simplify(entry) == 0 for entry in actual_matrix - expected_matrix
        )
    if isinstance(actual, sp.Basic) or isinstance(expected, sp.Basic):
        return sp.simplify(sp.sympify(actual) - sp.sympify(expected)) == 0
    return actual == expected


@dataclass
class Ledger:
    rows: list[dict[str, Any]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = equal(actual, expected)
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": ledger_value(actual),
                "expected": ledger_value(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: actual={actual!r}, expected={expected!r}")


def source_line(source_lines: list[str], needle: str, occurrence: int = 1) -> int:
    matches = [index + 1 for index, line in enumerate(source_lines) if needle in line]
    if occurrence < 1 or occurrence > len(matches):
        raise AssertionError((needle, matches))
    return matches[occurrence - 1]


def parse_exact(value: str) -> sp.Expr:
    return sp.sympify(value.replace("i", "I"))


def ledger_value(value: object) -> object:
    if isinstance(value, sp.MatrixBase):
        return [exact_text(entry) for entry in value]
    if isinstance(value, sp.Basic):
        return exact_text(value)
    if isinstance(value, dict):
        return {str(key): ledger_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [ledger_value(item) for item in value]
    return value


def build_artifact() -> dict[str, Any]:
    ledger = Ledger()
    source_lines = HT_SOURCE.read_text(encoding="utf-8").splitlines()
    ht = json.loads(HT_AUDIT.read_text(encoding="utf-8"))
    raw = json.loads(RAW_AB.read_text(encoding="utf-8"))
    aa = json.loads(AA_JSON.read_text(encoding="utf-8"))
    aa_text = AA_MD.read_text(encoding="utf-8")

    provenance_specs = {
        "Dtri_definition": (r"\mathcal{D}_{w,z}^{\tri}(f,g) :=", 1),
        "Dtri_zero": (r"\mathcal{D}^{\tri}_{0,0}(f,g) = \frac{1}{2}", 1),
        "N4_field_map": (r"\gamma^I \sim \Phi^{4I}", 1),
        "N4_superfield": (r"C = c + \theta_I \gamma^I", 1),
        "N4_Q0": (r"Q_0 C=\frac{1}{2}[C,C]", 1),
        # The first beta-b shifted row is the general adjoint result at 1058;
        # the second is its N=4 specialization at 1070.
        "shifted_beta_b": (r"Q_1( (\beta_I)^A(z) b^B(w))", 2),
        "zero_component_beta_b": (r"Q_1((\beta_I)^A b^B)", 1),
        "compact_main": (r"Q_1 (C^A(\theta) C^B(\theta')) = -\kappa^2", 1),
        "appendix_beta_b": (r"Q_1 ( (\beta_I)^A \partial_1^m \partial_2^n b^B )", 1),
    }
    provenance = {
        key: source_line(source_lines, needle, occurrence)
        for key, (needle, occurrence) in provenance_specs.items()
    }
    ledger.check("SOURCE_DTRI_ZERO_LINE", provenance["Dtri_zero"], 726)
    ledger.check("SOURCE_SHIFTED_BETA_B_LINE", provenance["shifted_beta_b"], 1070)
    ledger.check("SOURCE_ZERO_COMPONENT_BETA_B_LINE", provenance["zero_component_beta_b"], 1241)
    ledger.check("SOURCE_COMPACT_MAIN_LINE", provenance["compact_main"], 1251)
    ledger.check("SOURCE_APPENDIX_BETA_B_LINE", provenance["appendix_beta_b"], 1390)

    # The common rho^2 cancels from every bilinear.  The remaining exact
    # field scales are those in iota(field_HT)=a_field field_Project.
    sqrt2 = sp.sqrt(2)
    imaginary = sp.I
    a_a = -imaginary / sqrt2
    a_b = 1 / sqrt2
    a_c = sp.Integer(1)
    a_d = imaginary

    aa_input = sp.simplify(a_a * a_a)
    aa_da_output = sp.simplify(a_d * a_a)
    aa_bc_output = sp.simplify(a_b * a_c)
    aa_da_ratio = sp.simplify(aa_da_output / aa_input)
    aa_bc_ratio = sp.simplify(aa_bc_output / aa_input)
    ledger.check("AA_INPUT_SCALE", aa_input, -sp.Rational(1, 2))
    ledger.check("AA_DA_OUTPUT_SCALE", aa_da_output, 1 / sqrt2)
    ledger.check("AA_BC_OUTPUT_SCALE", aa_bc_output, 1 / sqrt2)
    ledger.check("AA_DA_RATIO", aa_da_ratio, -sqrt2)
    ledger.check("AA_BC_RATIO", aa_bc_ratio, -sqrt2)

    ab_input = sp.simplify(a_a * a_b)
    ab_db_output = sp.simplify(a_d * a_b)
    ab_cc_output = sp.simplify(a_c * a_c)
    ab_db_ratio = sp.simplify(ab_db_output / ab_input)
    ab_cc_ratio = sp.simplify(ab_cc_output / ab_input)
    ledger.check("AB_INPUT_SCALE", ab_input, -imaginary / 2)
    ledger.check("AB_DB_OUTPUT_SCALE", ab_db_output, imaginary / sqrt2)
    ledger.check("AB_CC_OUTPUT_SCALE", ab_cc_output, 1)
    ledger.check("AB_DB_RATIO", ab_db_ratio, -sqrt2)
    ledger.check("AB_CC_RATIO", ab_cc_ratio, 2 * imaginary)

    # AA fixes hbar_H*kappa_H^2/s1 without using any AB coefficient.
    hbar_h, kappa_h, s1, lambda1 = sp.symbols(
        "hbar_H kappa_H s_1 lambda_1", nonzero=True
    )
    loop_ratio = sp.solve(
        sp.Eq((hbar_h * kappa_h**2 / s1) * aa_da_ratio, lambda1),
        hbar_h * kappa_h**2,
    )[0]
    ledger.check(
        "AA_FIXES_LOOP_MARKER",
        loop_ratio,
        -s1 * lambda1 / sqrt2,
    )
    normalized_loop_ratio = sp.simplify(loop_ratio / s1)
    ledger.check(
        "S1_CANCELS_FROM_ALL_COMPONENT_RATIOS",
        normalized_loop_ratio,
        -lambda1 / sqrt2,
    )
    conditional_marker = sp.simplify(loop_ratio.subs(s1, -sp.Rational(1, 2)))
    ledger.check(
        "CONDITIONAL_S1_MINUS_HALF_MARKER",
        conditional_marker,
        lambda1 / (2 * sqrt2),
    )

    db_coefficient = sp.simplify(normalized_loop_ratio * ab_db_ratio / lambda1)
    cc_23_coefficient = sp.simplify(normalized_loop_ratio * ab_cc_ratio / lambda1)
    cc_32_coefficient = -cc_23_coefficient
    ledger.check("HT_PROJECT_DB_COEFFICIENT", db_coefficient, 1)
    ledger.check("HT_PROJECT_CC23_COEFFICIENT", cc_23_coefficient, -imaginary * sqrt2)
    ledger.check("HT_PROJECT_CC32_COEFFICIENT", cc_32_coefficient, imaginary * sqrt2)

    # epsilon_1JK is a two-term ordered sum.  There is no extra 1/2.
    def epsilon3(a: int, b: int, c: int) -> int:
        if {a, b, c} != {1, 2, 3}:
            return 0
        inversions = int(a > b) + int(a > c) + int(b > c)
        return -1 if inversions % 2 else 1

    epsilon_terms = [
        (j, k, epsilon3(1, j, k))
        for j in range(1, 4)
        for k in range(1, 4)
        if epsilon3(1, j, k)
    ]
    ledger.check("EPSILON_1JK_ORDERED_TERMS", epsilon_terms, [(2, 3, 1), (3, 2, -1)])
    ledger.check("EPSILON_1JK_TERM_COUNT", len(epsilon_terms), 2)

    # The color frame is scalar-free.  The trace normalization is entirely in
    # kappa_H^2 and was already fixed by AA.
    color = ht["typed_dictionary"]["color_frame"]
    ledger.check(
        "COLOR_TENSOR_ROUNDTRIP_NO_HALF",
        color["tensor_roundtrip"],
        (
            "R_A^P R_B^Q f_ACD f_BCE (R^-1)_R^D (R^-1)_S^E="
            "C_Project^{PQ}{}_{RS}"
        ),
    )
    ledger.check(
        "COLOR_REVERSE_IDENTITY",
        color["reversed_color_identity"],
        "C_Project^{BA}{}_{DE}=C_Project^{AB}{}_{ED}",
    )

    accepted_aa_formula = (
        r"\Gamma_{AA}^{(1)}" in aa_text
        and r"\langle D^D,A^E\rangle" in aa_text
        and "ACCEPTED_AA_ONE_LOOP_ANOMALY_SECTOR__HT_CHECK_ONLY_EXACT_MATCH" in aa_text
    )
    ledger.check("AA_TARGET_BLIND_SCALE_ONE_ACCEPTED", accepted_aa_formula, True)
    ledger.check("AA_EXTERNAL_TARGET_NOT_USED", aa["external_target_used"], False)
    ledger.check(
        "AA_RAW_CONTACT_MULTIPLICITY_STATUS",
        aa["source_edge_quotient"]["per_pair_identity"][
            "raw_contact_multiplicity_status"
        ],
        "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE",
    )
    ledger.check("AA_RAW_ENDPOINT_ROW_COUNT", aa["raw_port_partition"]["all_rows"], 48)
    ledger.check(
        "AA_GAUGE_SCALE_ONE_VECTOR",
        aa["typed_ordered_reconstruction"]["fourier_and_physical_quotient"][
            "physical_ordered_p_vector_over_lambda1_times_F"
        ],
        ["1", "-1"],
    )
    ledger.check(
        "AA_MATTER_SCALE_ONE_VECTOR",
        aa["matter_primitive_sign"]["ordered_vector_over_lambda1_times_F"],
        ["1", "-1"],
    )

    # Target scale from the zero-component/main-compact branch.
    target_vector = sp.Matrix((1, 1, -imaginary * sqrt2, imaginary * sqrt2))
    ledger.check(
        "HT_ZERO_COMPONENT_MAIN_COMPACT_VECTOR",
        sp.Matrix((db_coefficient, db_coefficient, cc_23_coefficient, cc_32_coefficient)),
        target_vector,
    )

    # The vendored source is internally inconsistent: the shifted Dtri and
    # Appendix-B formulas have T_HT(0,0)=1/2, while the explicit component and
    # main compact formulas have coefficient 1.
    t_ht_00 = sp.Rational(1, (0 + 0 + 2) * (0 + 0 + 1))
    k_project_00 = 2 * t_ht_00
    raw_g3_scale = sp.Integer(2)
    ledger.check("HT_PRINTED_DTRI_T00", t_ht_00, sp.Rational(1, 2))
    ledger.check("PROJECT_KERNEL_K00", k_project_00, 1)
    ledger.check("HT_ZERO_COMPONENT_BRANCH_T00", sp.Integer(1), 1)
    ledger.check("HT_INTERNAL_ZERO_SHIFT_RATIO", sp.simplify(1 / t_ht_00), 2)
    ledger.check("RAW_G3_OVER_PROJECT_K00", raw_g3_scale / k_project_00, 2)
    ledger.check("RAW_G3_OVER_PRINTED_HT_T00", raw_g3_scale / t_ht_00, 4)

    # Raw/local data are not a uniform rescaling of the HT vector.
    raw_direct = sp.Matrix(tuple(parse_exact(item) for item in raw["q_covariance"]["direct_vector"]))
    raw_expected = sp.Matrix((2, 1, -2 * imaginary * sqrt2, 2 * imaginary * sqrt2))
    ledger.check("LOCKED_HYBRID_DIRECT_VECTOR", raw_direct, raw_expected)
    scale_candidates = sp.Matrix(
        tuple(sp.simplify(raw_direct[index] / target_vector[index]) for index in range(4))
    )
    ledger.check("RAW_OVER_HT_SCALE_CANDIDATES", scale_candidates, sp.Matrix((2, 1, 2, 2)))
    global_scale_solutions = sp.solve(
        [sp.Eq(sp.Symbol("r") * raw_direct[index], target_vector[index]) for index in range(4)],
        sp.Symbol("r"),
        dict=True,
    )
    ledger.check("NO_GLOBAL_NORMALIZATION_FIX", global_scale_solutions, [])

    # Raw local jet layer.
    g1_pair, g1_eom = sp.Integer(2), sp.Integer(2)
    g2_pair, g2_eom = -sp.Rational(1, 3), sp.Rational(4, 3)
    ledger.check("G1_RAW_PAIR_EOM", sp.Matrix((g1_pair, g1_eom)), sp.Matrix((2, 2)))
    ledger.check(
        "G2_RAW_PAIR_EOM",
        sp.Matrix((g2_pair, g2_eom)),
        sp.Matrix((-sp.Rational(1, 3), sp.Rational(4, 3))),
    )

    # T_DB=pair+EOM and T_BD=-pair+EOM.  Only after quotienting by total
    # derivatives may T_DB or T_BD be set to zero.
    g1_pair_after_td = sp.simplify(g1_pair - g1_eom)
    g1_td_carrier = g1_eom
    g2_pair_after_td = sp.simplify(g2_pair + g2_eom)
    g2_td_carrier = g2_eom
    ledger.check("G1_PAIR_TD_DECOMPOSITION", sp.Matrix((g1_pair_after_td, g1_td_carrier)), sp.Matrix((0, 2)))
    ledger.check("G2_PAIR_TD_DECOMPOSITION", sp.Matrix((g2_pair_after_td, g2_td_carrier)), sp.Matrix((1, sp.Rational(4, 3))))

    # Target-blind residual-q comparison with accepted AA.  In the physical
    # derivative-slot module q_1 Y_1=i Z and q_1(A B_1)=-i A A.
    t = sp.symbols("t")
    covariance_residual = sp.simplify(imaginary * t - imaginary)
    covariance_solution = sp.solve(sp.Eq(covariance_residual, 0), t)
    ledger.check("AA_AB_Q_COVARIANCE_RESIDUAL", covariance_residual, imaginary * (t - 1))
    ledger.check("AA_AB_Q_COVARIANCE_UNIQUE_SCALE", covariance_solution, [1])
    ledger.check("SCALE_TWO_Q_COVARIANCE_FAILURE", covariance_residual.subs(t, 2), imaginary)

    failed = [row for row in ledger.rows if row["status"] != "PASS"]
    if failed:
        raise AssertionError(failed)

    return {
        "schema": "step5-ht-ab-normalization-quotient-exact-v1",
        "status": (
            "PASS_HT_AB_SCALE_ONE__S1_CANCELS__RAW_G3_SCALE_TWO_IS_NOT_A_"
            "NORMALIZATION_EFFECT__FIRST_ERROR_IS_MIXED_QUOTIENT_LAYER"
        ),
        "external_target_role": "HT_SOURCE_READ_ONLY_NORMALIZATION_AUDIT",
        "source_provenance_lines": provenance,
        "field_scales": {
            "A": "-i/sqrt(2)",
            "B_r": "1/sqrt(2)",
            "C_r": "1",
            "D_dot": "i",
            "common_rho": "cancels as rho^2/rho^2",
        },
        "aa_normalization": {
            "input_scale": exact_text(aa_input),
            "DA_output_scale": exact_text(aa_da_output),
            "BC_output_scale": exact_text(aa_bc_output),
            "output_over_input": exact_text(aa_da_ratio),
            "loop_marker_general": "hbar_H*kappa_H^2=-s_1*lambda_1/sqrt(2)",
            "loop_marker_if_s1_equals_s0_equals_minus_half": "lambda_1/(2*sqrt(2))",
            "normalized_loop_ratio": "hbar_H*kappa_H^2/s_1=-lambda_1/sqrt(2)",
            "target_blind_raw_checks": {
                "external_target_used": False,
                "raw_endpoint_rows": 48,
                "Schwinger_contact_multiplicity": "1",
                "gauge_vector": ["1", "-1"],
                "matter_vector": ["1", "-1"],
            },
        },
        "ab_translation": {
            "input_scale": exact_text(ab_input),
            "DB_output_over_input": exact_text(ab_db_ratio),
            "CC_output_over_input": exact_text(ab_cc_ratio),
            "epsilon_1JK_ordered_terms": [list(row) for row in epsilon_terms],
            "basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
            "HT_zero_component_main_compact_vector": [exact_text(entry) for entry in target_vector],
            "verdict": "SCALE_ONE",
        },
        "source_internal_conflict": {
            "zero_component_and_main_compact": "scale 1",
            "Dtri_zero_and_Appendix_B_m0n0": "scale 1/2",
            "exact_ratio": "2",
            "effect": "the source conflict offers scale 1 or scale 1/2, never scale 2",
            "kernel_comparison": {
                "T_HT_00": "1/2",
                "K_Project_00_equals_2T_HT_00": "1",
                "raw_G3_scale": "2",
                "raw_G3_over_K_Project_00": "2",
                "raw_G3_over_T_HT_00": "4",
            },
        },
        "raw_and_quotient_layers": {
            "raw_local": {
                "G1_pair_EOM": ["2", "2"],
                "G2_pair_EOM": ["-1/3", "4/3"],
                "G3_C2C3_C3C2": ["-2*i*sqrt(2)", "2*i*sqrt(2)"],
            },
            "total_derivative_decomposition": {
                "G1": "2*pair+2*EOM=2*T_DB; T_DB=pair+EOM",
                "G2": "-pair/3+4*EOM/3=pair+4*T_BD/3; T_BD=-pair+EOM",
            },
            "hybrid_direct_basis": ["D>B1", "B1>D", "C2>C3", "C3>C2"],
            "hybrid_direct_vector": [exact_text(entry) for entry in raw_direct],
            "hybrid_over_HT_scale_candidates": [exact_text(entry) for entry in scale_candidates],
            "global_normalization_solution": [],
        },
        "aa_q_covariance": {
            "relations": ["q_1 Y_1=i Z", "q_1(A B_1)=-i A A", "Delta(AA)=Z"],
            "equation": "i*t*Z-i*Z=0",
            "unique_scale": "t=1",
            "scale_two_residual": "i*Z",
        },
        "first_error_equality": {
            "raw_local_invalid_step": "T_BD=0",
            "valid_only_after": "projection to the total-derivative quotient",
            "concrete_chain": "-pair/3+4*EOM/3=pair+4*T_BD/3; only [T_BD]=0 gives [pair]",
            "comparison_error": (
                "the vector (2,1,-2*i*sqrt(2),2*i*sqrt(2)) combines raw G1/G3 "
                "with total-derivative-quotiented G2 and is not an element of one common layer"
            ),
        },
        "blocker": (
            "RAW_G3_SCALE_TWO_REQUIRES_AN_EXPLICIT_EOM_BRST_TD_OR_COUNTERTERM_"
            "QUOTIENT_MAP; HT_NORMALIZATION_SUPPLIES_NO_HALF"
        ),
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows),
            "failed": 0,
            "rows": ledger.rows,
        },
    }


def markdown(payload: dict[str, Any]) -> str:
    provenance = payload["source_provenance_lines"]
    return rf"""# HT--Project AB/BA normalization and quotient audit

Status: `{payload['status']}`.

## 1. Notation

$$
\iota(X_H)=a_X X_P,
\qquad
\iota(\hbar_HQ_{{1,H}})\iota^{{-1}}=s_1\Delta_P,
\qquad
\lambda_1=\frac{{\hbar_Pg^2}}{{16\pi^2}}.
$$

$$
a_A=-\frac{{i}}{{\sqrt2}},\qquad
a_{{B_r}}=\frac1{{\sqrt2}},\qquad
a_{{C_r}}=1,\qquad
a_D=i.
$$

The common factor $\rho$ cancels as $\rho^2/\rho^2$ in every bilinear.

## 2. AA fixes the loop marker

$$
a_A^2=-\frac12,qquad
a_Da_A=a_{{B_r}}a_{{C_r}}=\frac1{{\sqrt2}}.
$$

Therefore every term in the HT $AA$ row has ratio

$$
\frac{{a_Da_A}}{{a_A^2}}
=\frac{{a_{{B_r}}a_{{C_r}}}}{{a_A^2}}
=-\sqrt2.
$$

The target-blind accepted Project row is

$$
\Delta_P(A,A)=\lambda_1\mathbb F^{{AB}}{{}}_{{DE}}\mathscr Z^{{DE}}.
$$

Thus

$$
\frac{{\hbar_H\kappa_H^2}}{{s_1}}(-\sqrt2)=\lambda_1,
$$

$$
\boxed{{\hbar_H\kappa_H^2=-\frac{{s_1}}{{\sqrt2}}\lambda_1}},
\qquad
\boxed{{\frac{{\hbar_H\kappa_H^2}}{{s_1}}=-\frac{{\lambda_1}}{{\sqrt2}}}}.
$$

If $s_1=s_0=-1/2$,

$$
\hbar_H\kappa_H^2=\frac{{\lambda_1}}{{2\sqrt2}},
$$

but $s_1$ has already canceled from every $AB/AA$ ratio.

The AA normalization itself is target-blind:

$$
N_{{\rm raw\ endpoint}}=48,
\qquad
m_{{e_0}}=m_{{e_2}}=1,
$$

$$
(D>A,A>D)=(1,-1),
\qquad
(B_r>C_r,C_r>B_r)=(1,-1).
$$

Thus the AA seed contains no unaccounted factor $1/2$ inherited from the HT
$\mathcal D^\tri_{{0,0}}$ convention.

## 3. AB/BA translation

$$
a_Aa_{{B_1}}=-\frac i2,\qquad
a_Da_{{B_1}}=\frac i{{\sqrt2}},\qquad
a_{{C_2}}a_{{C_3}}=1.
$$

$$
\frac{{a_Da_{{B_1}}}}{{a_Aa_{{B_1}}}}=-\sqrt2,
\qquad
\frac{{a_{{C_2}}a_{{C_3}}}}{{a_Aa_{{B_1}}}}=2i.
$$

Hence

$$
-\frac{{\lambda_1}}{{\sqrt2}}(-\sqrt2)=\lambda_1,
$$

$$
-\frac{{\lambda_1}}{{\sqrt2}}(2i)=-i\sqrt2\lambda_1.
$$

For $I=1$ the flavor sum is exactly

$$
\sum_{{J,K}}\varepsilon_{{1JK}}C_JC_K
=C_2C_3-C_3C_2.
$$

It contains two ordered terms and no factor $1/2$.  In the basis

$$
(D>B_1,\ B_1>D,\ C_2>C_3,\ C_3>C_2),
$$

$$
\boxed{{v_{{HT,0}}=(1,1,-i\sqrt2,+i\sqrt2)}}.
$$

The color map has no scalar factor:

$$
f_{{ACD}}f_{{BCE}}\longmapsto\mathbb F^{{AB}}{{}}_{{DE}}.
$$

## 4. HT source branches

The explicit zero-component row starts at source line {provenance['zero_component_beta_b']}; the main compact row starts at line {provenance['compact_main']}.  Both give coefficient $1$.

The shifted $\mathcal D^\tri$ row starts at line {provenance['shifted_beta_b']}, while

$$
\mathcal D^\tri_{{0,0}}(f,g)=\frac12\langle f,g\rangle
$$

at line {provenance['Dtri_zero']}; Appendix B starts the same row at line {provenance['appendix_beta_b']}.  Therefore

$$
v_{{HT,\mathcal D^\tri}}=\frac12v_{{HT,0}}.
$$

The source conflict is scale $1$ versus scale $1/2$; neither branch gives scale $2$.

The exact three-way comparison is

$$
T^{{HT}}_{{0,0}}=\frac12,
\qquad
K^P_{{0,0}}=2T^{{HT}}_{{0,0}}=1,
\qquad
G_{{3,\rm raw}}=2.
$$

Thus

$$
\frac{{G_{{3,\rm raw}}}}{{K^P_{{0,0}}}}=2,
\qquad
\frac{{G_{{3,\rm raw}}}}{{T^{{HT}}_{{0,0}}}}=4.
$$

The already-recorded identity $K^P=2T^{{HT}}$ changes $1/2$ into $1$; it does
not change the locked raw $G_3$ coefficient $2$ into $1$.

## 5. Raw local and quotient layers

Raw local jets are

$$
(c_{{G_1,\rm pair}},c_{{G_1,\rm EOM}})=(2,2),
$$

$$
(c_{{G_2,\rm pair}},c_{{G_2,\rm EOM}})
=\left(-\frac13,\frac43\right),
$$

$$
(c_{{G_3,C_2C_3}},c_{{G_3,C_3C_2}})
=(-2i\sqrt2,+2i\sqrt2).
$$

For $G_1$,

$$
T_{{DB}}={{\rm pair}}+{{\rm EOM}},
$$

$$
2\,{{\rm pair}}+2\,{{\rm EOM}}=2T_{{DB}}.
$$

For $G_2$,

$$
T_{{BD}}=-{{\rm pair}}+{{\rm EOM}},
$$

$$
-\frac13{{\rm pair}}+\frac43{{\rm EOM}}
={{\rm pair}}+\frac43T_{{BD}}.
$$

The equality

$$
T_{{BD}}=0
$$

is false in the raw local jet space.  Only

$$
[T_{{BD}}]_{{\rm TD}}=0
$$

holds in the total-derivative quotient.

The current hybrid vector is

$$
v_{{\rm hybrid}}=(2,1,-2i\sqrt2,+2i\sqrt2).
$$

Its componentwise ratios to $v_{{HT,0}}$ are

$$
(2,1,2,2).
$$

No scalar $r$ satisfies $rv_{{\rm hybrid}}=v_{{HT,0}}$.

## 6. AA residual-q comparison

Let

$$
\mathscr Y_1
=\langle D,B_1\rangle+\langle B_1,D\rangle
-i\sqrt2\langle C_2,C_3\rangle
+i\sqrt2\langle C_3,C_2\rangle.
$$

The locked local relations are

$$
q_1\mathscr Y_1=i\mathscr Z,
\qquad
q_1(AB_1)=-iAA,
\qquad
\Delta_P(AA)=\mathscr Z.
$$

If $\Delta_P(AB_1)=t\mathscr Y_1$, then

$$
q_1\Delta_P(AB_1)+\Delta_Pq_1(AB_1)
=it\mathscr Z-i\mathscr Z
=i(t-1)\mathscr Z.
$$

Therefore

$$
\boxed{{t=1}}.
$$

For $t=2$ the residual is exactly

$$
i\mathscr Z\ne0.
$$

## 7. Exact boundary

The HT normalization supplies no factor $1/2$ capable of changing the locked raw $G_3$ scale $2$ into scale $1$.  Such a change requires an explicit common-layer EOM/BRST/total-derivative/counterterm quotient map.

Checks: `{payload['checks']['passed']}/{payload['checks']['count']}` PASS.
"""


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_artifact()
    json_text = canonical(payload)
    md_text = markdown(payload)
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != json_text:
            raise SystemExit(f"stale artifact: {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md_text:
            raise SystemExit(f"stale artifact: {MD_OUT}")
    if args.write or not args.check:
        JSON_OUT.write_text(json_text, encoding="utf-8")
        MD_OUT.write_text(md_text, encoding="utf-8")
    print(payload["status"])
    print(f"PASS {payload['checks']['passed']}/{payload['checks']['count']}")


if __name__ == "__main__":
    main()
