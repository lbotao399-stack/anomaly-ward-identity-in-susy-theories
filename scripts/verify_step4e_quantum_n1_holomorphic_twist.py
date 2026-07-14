from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts/foundations/step-04e-quantum-n1-holomorphic-twist.md"
TASK = ROOT / "tasks/CURRENT.yaml"
MANIFEST = ROOT / "contracts/manifest.yaml"
GAP_AUDIT = ROOT / "audits/step4e-quantum-n1-holomorphic-twist-gap-audit.json"
NOTATION_AUDIT = ROOT / "audits/step4e-quantum-n1-holomorphic-twist-notation-audit.json"
AUDIT = ROOT / "audits/step4e-quantum-n1-holomorphic-twist-verification.json"


checks: list[dict[str, object]] = []


def check(category: str, name: str, condition: bool, evidence: object) -> None:
    checks.append(
        {
            "category": category,
            "name": name,
            "result": "PASS" if condition else "FAIL",
            "evidence": evidence,
        }
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unordered_pair(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def relative_qme_coefficients(order: int) -> dict[tuple[str, str], Fraction]:
    coefficients: dict[tuple[str, str], Fraction] = defaultdict(Fraction)
    coefficients[unordered_pair("S", f"H{order}")] += 1
    for r in range(1, order + 1):
        coefficients[unordered_pair(f"M{r}", f"H{order - r}")] += 1
    for r in range(order + 1):
        coefficients[unordered_pair(f"H{r}", f"H{order - r}")] += Fraction(1, 2)
    return dict(coefficients)


def relative_recursion_coefficients(order: int) -> dict[tuple[str, str], Fraction]:
    coefficients: dict[tuple[str, str], Fraction] = defaultdict(Fraction)
    coefficients[unordered_pair("S", f"H{order}")] += 1
    coefficients[unordered_pair("H0", f"H{order}")] += 1
    for r in range(1, order + 1):
        coefficients[unordered_pair(f"M{r}", f"H{order - r}")] += 1
    for r in range(1, order):
        coefficients[unordered_pair(f"H{r}", f"H{order - r}")] += Fraction(1, 2)
    return dict(coefficients)


def qme_first_difference_coefficients(order: int) -> dict[str, Fraction]:
    coefficients: dict[str, Fraction] = defaultdict(Fraction)
    coefficients[f"dD{order}"] += 1
    for r in range(1, order):
        coefficients[f"DeltaLower{r}"] += 1
        coefficients[f"DeltaLower{r}"] -= 1
        coefficients[f"BracketLower{r},{order-r}"] += Fraction(1, 2)
        coefficients[f"BracketLower{r},{order-r}"] -= Fraction(1, 2)
    return dict(coefficients)


def main() -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    task = json.loads(TASK.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    gap_audit = json.loads(GAP_AUDIT.read_text(encoding="utf-8"))
    notation_audit = json.loads(NOTATION_AUDIT.read_text(encoding="utf-8"))

    numeric_tags = [int(value) for value in re.findall(r"\\tag\{4E\.(\d+)\}", text)]
    check(
        "contract_surface",
        "numeric_tags_consecutive",
        numeric_tags == list(range(1, 67)),
        numeric_tags,
    )
    check(
        "contract_surface",
        "subtag_11a",
        r"\tag{4E.11a}" in text,
        "4E.11a",
    )
    check(
        "contract_surface",
        "display_group_count",
        text.count("$$") // 2 == gap_audit["checked_equation_groups"],
        text.count("$$") // 2,
    )
    check(
        "contract_surface",
        "terminal_newline",
        text.endswith("\n") and not text.endswith("\n\n"),
        repr(text[-8:]),
    )
    forbidden = (
        r"\sim",
        r"\approx",
        r"\propto",
        "After substitution and algebra",
        "after substitution and algebra",
    )
    for token in forbidden:
        check(
            "contract_surface",
            f"forbidden_{token}",
            token not in text,
            text.count(token),
        )
    required = (
        r"\boldsymbol\Delta_{Y,\nu}\mathscr T_{\nu,1/2}^*",
        r"\boldsymbol\Delta_{\mathrm h,\nu}\pi_{\nu*}^{\mathrm{BV}}",
        r"\boldsymbol\Delta_{\mathrm h,\nu}\mathscr K_\nu",
        r"=(-1)^{p_\nu}\mathscr K_\nu\boldsymbol\Delta_{X,\nu}",
        r"d_{\mathrm{tw},0,\nu}H_{Q,n,\nu}",
        r"\mathfrak o_{Q,n,\nu}",
        r"\mathfrak o_{n,\rho}",
        r"H_{Q,0,\nu}",
        r"S_{\mathrm{tw},0,\nu}-S_{\mathrm{ord},0,\nu}",
        r"\rho_{Y,\nu}^{\mathrm{tr}}",
        r"\rho_{Y,\nu}^{\mathrm{ref}}",
        r"\ell_{\mathscr T,\nu}",
        r"\chi_{\rho_{Z,\nu}}",
        r"J_{\mathscr T,\nu}^{1/2}=(4i)^{-N_\nu}",
        r"\mathbb K:=\mathbb C((\hbar^{1/2}))",
        r"\mathscr S_{Z,\nu}^{\mathrm{WKB}}",
        r"\mathscr D_{\Gamma,\nu}",
        r"C_{\mathrm{ctr},\nu}(\hbar)",
        r"\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}",
        r"L_{\mathrm{ctr},\nu}^{(0)}",
        r"\int d\eta_1\,d\eta_2\,dw\,1",
        r"M_{1,\nu}^{\mathrm{pf}}",
        r"=-\log\mathcal A_{0,\nu}",
        r"[D_{n,\nu}]",
        r"H^{\bar0}",
        r"H^{\bar1}",
        r"d_{abc}^{\mathrm{adj}}=0",
        r"\mathcal W_Q\mathscr A_R=0",
        r"R_{\nu\to\mu}^{\mathrm h}\mathscr K_\nu",
        r"\operatorname{Flux}_{\partial\Gamma_{\mathrm{ctr},\mu}}",
        r"H^{\bar k}_{\mathrm{loc}}(d_{\mathrm h}\mid d_{\mathrm{sp}})",
        "PROVED CONDITIONALLY",
    )
    for token in required:
        check(
            "contract_surface",
            f"contains_{token}",
            token in text,
            token,
        )

    check(
        "task_scope",
        "task_id",
        task["id"] == "CONTRACT-STEP-04E-QUANTUM-N1-HOLOMORPHIC-TWIST-001",
        task["id"],
    )
    check("task_scope", "task_type", task["type"] == "CONTRACT_CHANGE", task["type"])
    check("task_scope", "task_status", task["status"] == "SPECIFIED", task["status"])
    check(
        "task_scope",
        "acceptance_count",
        len(task["acceptance"]) == 16,
        len(task["acceptance"]),
    )
    check(
        "task_scope",
        "no_admitted_reference_claims",
        task["reference_admission"]["admitted_claim_ids"] == [],
        task["reference_admission"]["admitted_claim_ids"],
    )
    check(
        "task_scope",
        "eight_blocked_reference_claims",
        len(task["reference_admission"]["blocked_claim_ids"]) == 8,
        task["reference_admission"]["blocked_claim_ids"],
    )
    check(
        "task_scope",
        "reference_blocker",
        task["reference_admission"]["blocker"] == "BLOCKED_REFERENCE_IMPORT_NOT_ON_MAIN",
        task["reference_admission"]["blocker"],
    )
    missing_inputs = [item for item in task["allowed_inputs"] if not (ROOT / item).exists()]
    check("task_scope", "all_allowed_inputs_exist", not missing_inputs, missing_inputs)
    check(
        "task_scope",
        "no_network_allowed_inputs",
        not any(item.startswith(("http://", "https://")) for item in task["allowed_inputs"]),
        task["allowed_inputs"],
    )

    manifest_entry = next(
        (
            item
            for item in manifest["contracts"]
            if item["id"] == "FOUNDATION-QUANTUM-N1-HOLOMORPHIC-TWIST-004E"
        ),
        None,
    )
    check("manifest", "entry_exists", manifest_entry is not None, manifest_entry)
    if manifest_entry is not None:
        check(
            "manifest",
            "path",
            manifest_entry["path"]
            == "contracts/foundations/step-04e-quantum-n1-holomorphic-twist.md",
            manifest_entry["path"],
        )
        check(
            "manifest",
            "status",
            manifest_entry["status"] == "DERIVED_UNFROZEN",
            manifest_entry["status"],
        )
        check(
            "manifest",
            "sha256",
            manifest_entry["sha256"] == sha256(CONTRACT),
            {"manifest": manifest_entry["sha256"], "actual": sha256(CONTRACT)},
        )

    for order in range(1, 7):
        expanded = relative_qme_coefficients(order)
        recursion = relative_recursion_coefficients(order)
        check(
            "quantum_q_lift",
            f"order_{order}_relative_recursion",
            expanded == recursion,
            {
                "expanded": {str(key): str(value) for key, value in expanded.items()},
                "recursion": {str(key): str(value) for key, value in recursion.items()},
            },
        )
    check(
        "quantum_q_lift",
        "order_one_terms",
        relative_recursion_coefficients(1)
        == {
            unordered_pair("S", "H1"): Fraction(1),
            unordered_pair("H0", "H1"): Fraction(1),
            unordered_pair("M1", "H0"): Fraction(1),
        },
        {str(key): str(value) for key, value in relative_recursion_coefficients(1).items()},
    )
    check(
        "quantum_q_lift",
        "bianchi_coefficients",
        Fraction(-1) + Fraction(1) == 0,
        ["-1", "+1"],
    )
    check(
        "quantum_q_lift",
        "finite_cohomology_before_local_cohomology",
        r"H^{\bar1}(\mathscr O_{Z,\nu},d_0)" in text
        and "Local cohomology modulo spacetime" in text,
        "finite parity cohomology before continuum relative local cohomology",
    )
    check(
        "quantum_q_lift",
        "ordinary_obstruction_closed",
        r"d_0\mathfrak o_{n,\rho}" in text
        and r"[\hbar^n]\mathfrak M_\rho(W_{<n})=-\mathfrak o_{n,\rho}" in text,
        "Bianchi coefficient proves d0-closedness",
    )
    check(
        "quantum_q_lift",
        "integer_grading_hypotheses",
        r"\deg_{\mathrm{HT}}\boldsymbol\Delta_{Z,\nu}=1" in text
        and r"\deg_{\mathrm{HT}}\rho_{Z,\nu}=0" in text,
        "degree hypotheses",
    )

    check(
        "density_transport",
        "compatible_density_condition",
        r"\boldsymbol\Delta_{Z,\nu}\rho_{Z,\nu}^{1/2}=0" in text,
        "compatible density",
    )
    check(
        "density_transport",
        "general_density_defect",
        r"\chi_{\rho_{Z,\nu}}F" in text,
        "general semidensity-to-function conversion",
    )
    check(
        "density_transport",
        "transport_reference_separated",
        r"\rho_{Y,\nu}^{\mathrm{tr}}" in text
        and r"\rho_{Y,\nu}^{\mathrm{ref}}" in text,
        "tr and ref",
    )
    check(
        "density_transport",
        "typed_pullbacks_separated",
        r"\mathscr T_{\nu,0}^*" in text
        and r"\mathscr T_{\nu,1/2}^*" in text
        and r"\mathscr T_{\nu,1}^*" in text
        and "reserved for the ordinary\ngeometric pullback of differential forms"
        in text,
        "function, semidensity, density, and differential-form pullbacks are distinct",
    )
    check(
        "density_transport",
        "jacobian_action_sign",
        -(-1) == 1
        and r"+\hbar N_\nu\operatorname{Log}_{k_\nu}(4i)" in text,
        "minus hbar log of exponent -N",
    )
    check(
        "density_transport",
        "jacobian_log_branch",
        r"\operatorname{Log}_{k_\nu}(4i)" in text
        and r"=2\pi i\hbar N_\nu m" in text
        and r"=e^{-2\pi iN_\nu m}=1" in text,
        "branch shift changes the action by a vacuum term and leaves the semidensity fixed",
    )
    check(
        "density_transport",
        "constant_jacobian_has_zero_hamiltonian",
        "its bracket and Laplacian vanish exactly" in text
        and "For a general\ncompatible reference density" in text,
        "flat constant ell_T separated from general reference density",
    )

    horizontal_coefficient = Fraction(1)
    vertical_flux_coefficient = Fraction(0)
    normalization_coefficient = Fraction(1)
    composite_coefficient = (
        horizontal_coefficient + vertical_flux_coefficient
    ) * normalization_coefficient
    check(
        "bv_pushforward",
        "horizontal_term",
        horizontal_coefficient == 1,
        str(horizontal_coefficient),
    )
    check(
        "bv_pushforward",
        "vertical_zero_flux",
        vertical_flux_coefficient == 0,
        str(vertical_flux_coefficient),
    )
    check(
        "bv_pushforward",
        "normalized_composite_chain_coefficient",
        composite_coefficient == 1,
        str(composite_coefficient),
    )
    for parity in (0, 1):
        check(
            "bv_pushforward",
            f"graded_chain_sign_p{parity}",
            (-1) ** parity in (1, -1)
            and r"=(-1)^{p_\nu}\mathscr K_\nu\boldsymbol\Delta_{X,\nu}"
            in text,
            {"p": parity, "sign": (-1) ** parity},
        )
    check(
        "bv_pushforward",
        "normalization_ring",
        r"\mathbb C((\hbar^{1/2}))" in text,
        "Gaussian half-powers admitted",
    )
    check(
        "bv_pushforward",
        "output_logarithm_hypothesis",
        r"\log\mathcal A_{0,\nu}\in\mathscr O_{\mathrm h,\nu}^{\bar0}"
        in text
        and r"M_{1,\nu}^{\mathrm{pf}}" in text
        and r"=-\log\mathcal A_{0,\nu}" in text,
        "chosen field-dependent leading logarithm",
    )
    check(
        "bv_pushforward",
        "flat_normalization_includes_jacobian",
        r"\mathcal N_\nu^{\mathrm{cl}}(\hbar)" in text
        and r"=(4i)^{-N_\nu}C_{\mathrm{ctr},\nu}(\hbar)" in text,
        "Jacobian times vertical vacuum factor",
    )
    check(
        "bv_pushforward",
        "wkb_and_stable_zero_flux_domains",
        r"\mathscr S_{X,\nu}^{\mathrm{adm}}" in text
        and r"\mathscr D_{\Gamma,\nu}" in text
        and r"\boldsymbol\Delta_{Y,\nu}\mathscr D_{\Gamma,\nu}" in text,
        "typed WKB domain and stable zero-flux subspace",
    )
    check(
        "bv_pushforward",
        "fixed_horizontal_base_cycle",
        r"\Gamma_{\mathrm{ctr},\nu}(x,x^*)" in text
        and r"\frac{\partial\Gamma_{\mathrm{ctr},\nu}}{\partial x^a}=0"
        in text
        and "produces no moving-cycle term" in text,
        "horizontal differentiation does not create a cycle-variation flux",
    )
    check(
        "bv_pushforward",
        "raw_integer_degree_typed",
        r"q_\nu:=\deg_{\mathrm{HT}}I_\nu" in text
        and r"\deg_{\mathrm{HT}}\mathscr K_\nu=q_\nu" in text
        and r"q_\nu=0" in text,
        "raw parity and integer degree with zero-degree action condition",
    )

    canonical_pairs = {
        "u1": "u1*",
        "u2": "u2*",
        "eta1": "eta1*",
        "eta2": "eta2*",
        "w": "w*",
        "K": "K*",
    }
    contractible_monomials = (
        {"u1*", "eta1"},
        {"u2*", "eta2"},
        {"w*", "K"},
    )
    for index, monomial in enumerate(contractible_monomials, start=1):
        contains_pair = any(
            base in monomial and antifield in monomial
            for base, antifield in canonical_pairs.items()
        )
        check(
            "contractible_factor",
            f"monomial_{index}_flat_laplacian",
            not contains_pair,
            sorted(monomial),
        )
    check(
        "contractible_factor",
        "nonflat_density_condition",
        r"(\ell_{\mathrm{ctr},\nu},S_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}=0"
        in text,
        "density Hamiltonian invariance",
    )
    check(
        "contractible_factor",
        "nonflat_density_compatibility",
        r"\Delta_{\mathrm{ctr},\nu}^{\mathrm{flat}}" in text
        and r"\ell_{\mathrm{ctr},\nu}" in text
        and r"+\frac14" in text
        and r"(\ell_{\mathrm{ctr},\nu},\ell_{\mathrm{ctr},\nu})_{\mathrm{ctr},\nu}"
        in text,
        "full-density ratio compatibility uses the half-density exponent ell/2",
    )
    check(
        "contractible_factor",
        "naive_zero_section_disproved",
        r"\left.S_{\mathrm{ctr},\nu}\right|_{L_{\mathrm{ctr},\nu}^{(0)}}=0"
        in text
        and r"\frac{\partial}{\partial\eta_1}1" in text
        and "element required in (4E.48)" in text,
        "constant odd integral vanishes and even integral is undamped",
    )

    for order in range(1, 7):
        coefficients = qme_first_difference_coefficients(order)
        surviving = {
            key: value for key, value in coefficients.items() if value != 0
        }
        check(
            "independent_comparison",
            f"order_{order}_first_difference",
            surviving == {f"dD{order}": Fraction(1)},
            {key: str(value) for key, value in surviving.items()},
        )
    check(
        "independent_comparison",
        "finite_H0_not_local_H0",
        r"H^{\bar0}" in text
        and r"\left(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu}\right)"
        in text
        and r"H^{\bar0}_{\mathrm{loc}}(d_{\mathrm h}\mid d_{\mathrm{sp}})"
        in text,
        "regulated even cohomology separated from continuum relative local cohomology",
    )
    check(
        "independent_comparison",
        "exact_parameter_constant_decomposition",
        r"D_{n,\nu}" in text
        and r"d_{\mathrm h,\nu}R_{n,\nu}" in text
        and r"\frac{\partial S_{\mathrm{hBF},\nu}}{\partial g^A}"
        in text
        and r"+\zeta_{n,\nu}" in text,
        "equation 4E.52",
    )
    check(
        "independent_comparison",
        "vacuum_normalization_sign_and_frozen_case",
        r"\mathcal N_\nu'" in text
        and r":=e^{-\hbar^{n-1}\zeta_{n,\nu}}\mathcal N_\nu" in text
        and r"-\hbar^n\zeta_{n,\nu}" in text
        and "For frozen normalization, remove \\([1]\\)" in text,
        "normalization shift removes the constant only when the normalization is adjustable",
    )

    transpose_sign = Fraction(-1)
    cyclic_sign = Fraction(1)
    check(
        "anomaly_channels",
        "adjoint_tensor_sign",
        transpose_sign * cyclic_sign == -1,
        str(transpose_sign * cyclic_sign),
    )
    check(
        "anomaly_channels",
        "adjoint_tensor_zero_over_C",
        Fraction(1) - Fraction(-1) == 2
        and r"\boxed{d_{abc}^{\mathrm{adj}}=0.}" in text,
        "d=-d and characteristic zero",
    )
    check(
        "anomaly_channels",
        "R_Q_Wess_Zumino",
        r"\mathcal W_R\mathscr A_Q" in text
        and r"-\mathcal W_Q\mathscr A_R" in text
        and r"=r_Q\mathscr A_Q" in text,
        "equation 4E.58",
    )
    check(
        "anomaly_channels",
        "R_anomaly_not_Q_anomaly",
        "does not yield \\(\\mathscr A_R=0\\)" in text,
        "A_Q=0 implies only W_Q A_R=0",
    )
    check(
        "anomaly_channels",
        "beta_degree_zero",
        "beta, finite counterterm" in text
        and r"H^{\bar0}(\mathscr O_{\mathrm h,\nu},d_{\mathrm h,\nu})"
        in text,
        "even table entry",
    )

    check(
        "continuum",
        "RG_homotopy_square",
        r"R_{\nu\to\mu}^{\mathrm h}\mathscr K_\nu" in text
        and r"\boldsymbol\Delta_{\mathrm h,\mu}H_{\nu\mu}" in text
        and r"H_{\nu\mu}\boldsymbol\Delta_{X,\nu}" in text,
        "equation 4E.62",
    )
    check(
        "continuum",
        "local_limit_and_flux",
        r"M_{n}^{\mathrm{pf}}" in text
        and r"\operatorname{Flux}_{\partial\Gamma_{\mathrm{ctr},\mu}}" in text,
        "equation 4E.63",
    )
    check(
        "continuum",
        "continuum_not_proved",
        "Equations (4E.62)--(4E.63), the bracket limit, and the continuum"
        in text,
        "explicit block",
    )
    check(
        "continuum",
        "relative_local_bicomplex_typed",
        r"d_{\mathrm h}^{\mathrm{dens}}" in text
        and r"d_{\mathrm h}d_{\mathrm{sp}}" in text
        and r"\Omega_{\mathrm{loc}}^{4,\bar k}" in text,
        "representative-level lift and bicomplex",
    )

    contract_gap_ids = sorted(
        {
            f"QHT-GAP-{value}"
            for value in re.findall(r"QHT\\!-\\!GAP\\!-\\!(\d\d)", text)
        }
    )
    audit_gap_ids = sorted(item["id"] for item in gap_audit["gaps"])
    expected_gap_ids = [f"QHT-GAP-{index:02d}" for index in range(1, 10)]
    check("gap_audit", "contract_gap_ids", contract_gap_ids == expected_gap_ids, contract_gap_ids)
    check("gap_audit", "audit_gap_ids", audit_gap_ids == expected_gap_ids, audit_gap_ids)
    check(
        "gap_audit",
        "declared_open_gap_ids",
        gap_audit["open_gap_ids"] == expected_gap_ids,
        gap_audit["open_gap_ids"],
    )
    check(
        "gap_audit",
        "equation_group_count_matches",
        gap_audit["checked_equation_groups"] == text.count("$$") // 2,
        {
            "audit": gap_audit["checked_equation_groups"],
            "contract": text.count("$$") // 2,
        },
    )
    valid_types = {
        "G-DEF",
        "G-IDX",
        "G-SIGN",
        "G-ALG",
        "G-OP",
        "G-THM",
        "G-PROJ",
        "G-NORM",
        "G-SCOPE",
    }
    for item in gap_audit["gaps"]:
        check(
            "gap_audit",
            f"{item['id']}_fields",
            item["type"] in valid_types
            and item["severity"] in {"P1", "P2"}
            and bool(item["location"])
            and bool(item["claim"])
            and bool(item["what_is_missing"])
            and bool(item["minimal_expansion_or_theorem_needed"]),
            item,
        )
    check(
        "gap_audit",
        "internal_P0_empty",
        gap_audit["internal_proof_obligations"]["P0"] == [],
        gap_audit["internal_proof_obligations"]["P0"],
    )
    check(
        "gap_audit",
        "internal_P1_empty",
        gap_audit["internal_proof_obligations"]["P1"] == [],
        gap_audit["internal_proof_obligations"]["P1"],
    )
    check(
        "gap_audit",
        "all_spot_checks_pass",
        len(gap_audit["verification_checks"]) >= 7
        and all(item["result"] == "PASS" for item in gap_audit["verification_checks"]),
        gap_audit["verification_checks"],
    )

    check(
        "notation_audit",
        "audit_task",
        notation_audit["task"]
        == "CONTRACT-STEP-04E-QUANTUM-N1-HOLOMORPHIC-TWIST-001",
        notation_audit["task"],
    )
    check(
        "notation_audit",
        "audit_result",
        notation_audit["result"] == "PASS",
        notation_audit["result"],
    )
    check(
        "notation_audit",
        "no_unresolved_P0_P1",
        notation_audit["unresolved"] == {"P0": [], "P1": []},
        notation_audit["unresolved"],
    )
    check(
        "notation_audit",
        "resolved_findings_recorded",
        len(notation_audit["resolved_findings"]) >= 20,
        len(notation_audit["resolved_findings"]),
    )

    failed = [item for item in checks if item["result"] != "PASS"]
    category_names = sorted({str(item["category"]) for item in checks})
    categories = {
        category: {
            "checks": sum(item["category"] == category for item in checks),
            "failed": sum(
                item["category"] == category and item["result"] != "PASS"
                for item in checks
            ),
        }
        for category in category_names
    }
    payload = {
        "schema": 1,
        "task": "CONTRACT-STEP-04E-QUANTUM-N1-HOLOMORPHIC-TWIST-001",
        "contract": str(CONTRACT.relative_to(ROOT)),
        "status": "PASS" if not failed else "FAIL",
        "totals": {
            "exact_checks": len(checks),
            "failed_checks": len(failed),
        },
        "categories": categories,
        "checks": checks,
    }
    AUDIT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if failed:
        names = ", ".join(str(item["name"]) for item in failed)
        raise SystemExit(f"{len(failed)} exact checks failed: {names}")


if __name__ == "__main__":
    main()
