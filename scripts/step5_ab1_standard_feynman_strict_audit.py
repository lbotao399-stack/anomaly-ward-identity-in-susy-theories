#!/usr/bin/env python3
"""Fail-closed exact checks for the ordered A B_1 one-loop audit.

A PASS certifies only the encoded convention, BCH, source-word, elementary
DRED, and external-kernel arithmetic.  It does not certify a complete
occurrence-resolved supergraph calculation.
"""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-ab1-standard-feynman-strictification.md"
PRO_INITIAL = ROOT / "proposals/gpt-pro-ab1-standard-feynman-2026-07-14.md"
PRO_DERIVATION = ROOT / "proposals/gpt-pro-ab1-derivation-correction-2026-07-14.md"
PRO_FINAL = ROOT / "proposals/gpt-pro-ab1-final-settlement-2026-07-14.md"
AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
AUTHORITY_VERIFY_RUN = 29306335742
STEP5A_RECEIPT = "audits/step5a-component-bv-brst-grammar-verification.json"
EXPECTED_PROMPT_HASHES = {
    "initial_pro": "2f8307295b028b317ca07ae29696eca93a8c3850f0c4fe3005584439add1b658",
    "derivation_pro": "059d7aa7bef7ac723ec8969ef1af172a983c2073233fe75dab32c198be45b3fd",
    "final_pro": "d179b8b7b80d902b7789cab3d7cfed13a6e96ef2ee152c82028883e57c88853c",
}

SCOPE = "CONDITIONAL_FF_Q4S_AB1_ARITHMETIC_ONLY"
CLAIM_BOUNDARY = (
    "PASS_DOES_NOT_CERTIFY_AB1_OCCURRENCE_CENSUS_DWORD_"
    "CUT_COMPLETION_OR_RENORMALIZED_MATCH"
)
FULL_STATUS = "BLOCKED_NO_ADMITTED_AB1_TREE_GRAPH_DRED_RESULT"

BLOCKERS = (
    "BLOCKED_NO_ADMITTED_AB1_TREE_GRAPH_DRED_RESULT",
    "BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE",
    "BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR",
    "BLOCKED_SOURCE_HESSIAN_LEFT_RIGHT_AND_TAYLOR_NORMALIZATION",
    "BLOCKED_LOCAL_PROPOSAL_LINK_CONNECTION_U_LIFT",
    "BLOCKED_VVV_ORDERED_HESSIAN",
    "BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE",
    "BLOCKED_AB1_OCCURRENCE_RESOLVED_DWORD_TRACES",
    "BLOCKED_EQUAL_CONTACT_AND_LONGITUDINAL_RESIDUES",
    "BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED",
    "BLOCKED_STEP5A_NK_BRANCH_UNSELECTED",
    "BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED",
    "BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION",
    "BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION",
    "BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX",
    "BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT",
    "BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER",
    "BLOCKED_AB1_SOURCE_OVERALL_G_NORMALIZATION",
    "BLOCKED_CHIRAL_TO_VECTOR_FRAME_SOURCE_BRIDGE",
    "BLOCKED_SOURCE_COUPLING_INSERTION_SIGN",
    "BLOCKED_TYPED_ORIENTED_EDGE_KERNEL_ASSIGNMENT",
    "BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED",
)


def git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def authority_text(path: str) -> str:
    return git("show", f"{AUTHORITY_COMMIT}:{path}")


def compact_tex(text: str) -> str:
    return re.sub(r"\s+", "", text)


def archive_integrity_checks(label: str, path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    exists = path.is_file()
    rows.append(check(f"{label}_archive_exists", exists, exists, True))
    if not exists:
        return rows

    text = path.read_text(encoding="utf-8")
    rows.append(
        check(
            f"{label}_archive_non_authority_status",
            re.search(r"^Status: `NON_AUTHORITY_PRO_REVIEW`\.?$", text, re.MULTILINE) is not None,
            re.search(r"^Status: `NON_AUTHORITY_PRO_REVIEW`\.?$", text, re.MULTILINE) is not None,
            True,
        )
    )
    prompt_match = re.search(r"Prompt SHA-256: `([0-9a-f]{64})`\.?", text)
    rows.append(
        check(
            f"{label}_archive_prompt_hash_declared",
            prompt_match is not None,
            prompt_match.group(1) if prompt_match else None,
            "64 lowercase hexadecimal digits",
        )
    )
    expected_prompt_hash = EXPECTED_PROMPT_HASHES.get(label)
    if expected_prompt_hash is not None:
        actual_prompt_hash = prompt_match.group(1) if prompt_match else None
        rows.append(
            check(
                f"{label}_archive_prompt_hash",
                actual_prompt_hash == expected_prompt_hash,
                actual_prompt_hash,
                expected_prompt_hash,
            )
        )

    body_match = re.search(r"Rendered(?:-response body|-body) SHA-256: `([0-9a-f]{64})`\.?", text)
    export_marker = (
        "The following is the completed visible response exported from the rendered DOM, "
        "with TeX recovered from the page's MathML annotations."
    )
    if body_match is not None:
        if export_marker in text:
            body_raw = text.split(export_marker, 1)[1]
        elif "\n---\n\n" in text:
            body_raw = text.split("\n---\n\n", 1)[1]
        else:
            body_raw = ""
        marker_present = bool(body_raw)
        rows.append(
            check(
                f"{label}_archive_body_marker",
                marker_present,
                marker_present,
                True,
            )
        )
        if marker_present:
            body = body_raw.strip()
            candidates = {
                hashlib.sha256(body.encode("utf-8")).hexdigest(),
                hashlib.sha256((body + "\n").encode("utf-8")).hexdigest(),
            }
            expected_hash = body_match.group(1)
            rows.append(
                check(
                    f"{label}_archive_body_hash",
                    expected_hash in candidates,
                    sorted(candidates),
                    expected_hash,
                )
            )
    return rows


@dataclass(frozen=True)
class Q2:
    """Exact a+b sqrt(2)."""

    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: "Q2") -> "Q2":
        return Q2(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __neg__(self) -> "Q2":
        return Q2(-self.rational, -self.sqrt2)

    def __sub__(self, other: "Q2") -> "Q2":
        return self + (-other)

    def __mul__(self, other: "Q2") -> "Q2":
        return Q2(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )

    def scale(self, value: int | Fraction) -> "Q2":
        value = Fraction(value)
        return Q2(value * self.rational, value * self.sqrt2)

    def __str__(self) -> str:
        return f"({self.rational})+({self.sqrt2})*sqrt(2)"


ZERO = Q2()
ONE = Q2(Fraction(1), Fraction(0))
SQRT2 = Q2(Fraction(0), Fraction(1))


def qpow(base: Q2, exponent: int) -> Q2:
    result = ONE
    for _ in range(exponent):
        result = result * base
    return result


Polynomial = dict[str, Q2]


def add_term(poly: Polynomial, word: str, coefficient: Q2) -> None:
    poly[word] = poly.get(word, ZERO) + coefficient
    if poly[word] == ZERO:
        del poly[word]


def scale_poly(poly: Polynomial, coefficient: int | Fraction) -> Polynomial:
    return {word: value.scale(coefficient) for word, value in poly.items()}


def gamma_word(order: int) -> Polynomial:
    """Coefficient of g**order in e^-V D e^V, V=sqrt(2) g u."""
    degree = order - 1
    result: Polynomial = {}
    for p in range(degree + 1):
        q = degree - p
        coefficient = Fraction((-1) ** p, 1)
        coefficient /= Fraction(1, 1)
        # p! q! (p+q+1) in the exact Step-5A word.
        p_factorial = 1
        q_factorial = 1
        for value in range(2, p + 1):
            p_factorial *= value
        for value in range(2, q + 1):
            q_factorial *= value
        coefficient /= p_factorial * q_factorial * (degree + 1)
        word = "u" * p + "X" + "u" * q
        add_term(result, word, qpow(SQRT2, order).scale(coefficient))
    return result


def w_word(order: int) -> Polynomial:
    return {f"B[{word}]": coefficient.scale(Fraction(-1, 8)) for word, coefficient in gamma_word(order).items()}


def a_word(power: int) -> Polynomial:
    """Coefficient of g**power in g^-1 nabla_+ W_+."""
    result: Polynomial = {}
    for word, coefficient in w_word(power + 1).items():
        add_term(result, f"D[{word}]", coefficient)
    for i in range(1, power + 1):
        j = power + 1 - i
        for left, left_coefficient in gamma_word(i).items():
            for right, right_coefficient in w_word(j).items():
                product = left_coefficient * right_coefficient
                # Gamma and W are odd: the graded bracket is an anticommutator.
                add_term(result, f"{left}.{right}", product)
                add_term(result, f"{right}.{left}", product)
    return result


def b_word(power: int) -> Polynomial:
    if power == 0:
        return {"Dphi": ONE}
    result: Polynomial = {}
    for word, coefficient in gamma_word(power).items():
        add_term(result, f"{word}.phi", coefficient)
        add_term(result, f"phi.{word}", -coefficient)
    return result


def check(identifier: str, condition: bool, actual: object, expected: object) -> dict[str, object]:
    return {
        "id": identifier,
        "status": "PASS" if condition else "FAIL",
        "actual": str(actual),
        "expected": str(expected),
        "scope": SCOPE,
        "certifies_full_diagram_derivation": False,
    }


def polynomial_checks(prefix: str, actual: Polynomial, expected: Polynomial) -> list[dict[str, object]]:
    rows = [check(f"{prefix}_word_set", set(actual) == set(expected), sorted(actual), sorted(expected))]
    for word in sorted(set(actual) | set(expected)):
        rows.append(check(f"{prefix}_{word}", actual.get(word, ZERO) == expected.get(word, ZERO), actual.get(word, ZERO), expected.get(word, ZERO)))
    return rows


def ht_coefficient(m: int, n: int, k: int, ell: int) -> Fraction:
    return Fraction(comb(m, k) * comb(n, ell), (m + n + 2) * (k + ell + 1))


def coarse_source_product_count(order: int) -> int:
    # Triples (i,j,k)>=0 with i+j+k=order for A_i T_k B_j.
    return sum(1 for i in range(order + 1) for j in range(order + 1 - i) for k in [order - i - j])


def coarse_ordered_port_pair_count(order: int) -> int:
    ports = order + 2
    return coarse_source_product_count(order) * ports * (ports - 1)


def degree_two_resolvent_terms() -> dict[str, int]:
    """Neumann-series words of total background degree two.

    Every action-Hessian insertion has positive background degree.  A word
    with k such insertions has coefficient (-1)**k in (K+V)^-1 I.
    """
    terms: dict[str, int] = {}
    total_degree = 2
    for vertex_count in range(total_degree + 1):
        for vertex_degrees in product(range(1, total_degree + 1), repeat=vertex_count):
            insertion_degree = total_degree - sum(vertex_degrees)
            if insertion_degree < 0:
                continue
            name = "G" + "".join(f"V{degree}G" for degree in vertex_degrees) + f"I{insertion_degree}"
            terms[name] = (-1) ** vertex_count
    return terms


def levi_civita_three(indices: tuple[int, int, int]) -> int:
    if set(indices) != {1, 2, 3}:
        return 0
    inversions = sum(indices[i] > indices[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def all_checks() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    expected_gamma = {
        1: {"X": SQRT2},
        2: {"Xu": ONE, "uX": -ONE},
        3: {"Xuu": SQRT2.scale(Fraction(1, 3)), "uXu": SQRT2.scale(Fraction(-2, 3)), "uuX": SQRT2.scale(Fraction(1, 3))},
    }
    expected_a = {
        0: {"D[B[X]]": SQRT2.scale(Fraction(-1, 8))},
        1: {
            "D[B[Xu]]": Q2(Fraction(-1, 8)),
            "D[B[uX]]": Q2(Fraction(1, 8)),
            "X.B[X]": Q2(Fraction(-1, 4)),
            "B[X].X": Q2(Fraction(-1, 4)),
        },
        2: {
            "D[B[Xuu]]": SQRT2.scale(Fraction(-1, 24)),
            "D[B[uXu]]": SQRT2.scale(Fraction(1, 12)),
            "D[B[uuX]]": SQRT2.scale(Fraction(-1, 24)),
            "X.B[Xu]": SQRT2.scale(Fraction(-1, 8)),
            "B[Xu].X": SQRT2.scale(Fraction(-1, 8)),
            "X.B[uX]": SQRT2.scale(Fraction(1, 8)),
            "B[uX].X": SQRT2.scale(Fraction(1, 8)),
            "Xu.B[X]": SQRT2.scale(Fraction(-1, 8)),
            "B[X].Xu": SQRT2.scale(Fraction(-1, 8)),
            "uX.B[X]": SQRT2.scale(Fraction(1, 8)),
            "B[X].uX": SQRT2.scale(Fraction(1, 8)),
        },
    }
    expected_b = {
        0: {"Dphi": ONE},
        1: {"X.phi": SQRT2, "phi.X": -SQRT2},
        2: {"Xu.phi": ONE, "uX.phi": -ONE, "phi.Xu": -ONE, "phi.uX": ONE},
    }

    for order in (1, 2, 3):
        rows.extend(polynomial_checks(f"gamma_{order}", gamma_word(order), expected_gamma[order]))
    for power in (0, 1, 2):
        rows.extend(polynomial_checks(f"A_{power + 1}", a_word(power), expected_a[power]))
        rows.extend(polynomial_checks(f"B1_{power + 1}", b_word(power), expected_b[power]))

    expected_source_counts = (1, 3, 6)
    expected_port_pair_counts = (2, 18, 72)
    for order in range(3):
        source_count = coarse_source_product_count(order)
        port_pair_count = coarse_ordered_port_pair_count(order)
        rows.append(check(f"coarse_source_product_count_g{order}", source_count == expected_source_counts[order], source_count, expected_source_counts[order]))
        rows.append(check(f"coarse_ordered_port_pair_count_I{order}", port_pair_count == expected_port_pair_counts[order], port_pair_count, expected_port_pair_counts[order]))
    port_pair_total = sum(coarse_ordered_port_pair_count(order) for order in range(3))
    rows.append(check("coarse_ordered_port_pair_total", port_pair_total == 92, port_pair_total, 92))
    nonlink = sum((order + 1) * (order + 2) * (order + 1) for order in range(3))
    rows.append(check("coarse_ordered_port_pair_nonlink", nonlink == 50, nonlink, 50))
    rows.append(check("coarse_ordered_port_pair_link_dependent", 92 - nonlink == 42, 92 - nonlink, 42))

    expected_resolvent = {"GI2": 1, "GV1GI1": -1, "GV2GI0": -1, "GV1GV1GI0": 1}
    derived_resolvent = degree_two_resolvent_terms()
    rows.append(check("degree_two_resolvent_neumann_words", derived_resolvent == expected_resolvent, derived_resolvent, expected_resolvent))

    epsilon_123 = levi_civita_three((1, 2, 3))
    epsilon_132 = levi_civita_three((1, 3, 2))
    rows.append(check("epsilon_123", epsilon_123 == 1, epsilon_123, 1))
    rows.append(check("epsilon_132", epsilon_132 == -1, epsilon_132, -1))
    rows.append(check("primitive_CC_ordered_sign_pair", (epsilon_123, epsilon_132) == (1, -1), (epsilon_123, epsilon_132), (1, -1)))

    simplex_area = Fraction(1, 1) - Fraction(1, 2)
    tensor_reduction_factor = Fraction(1, 2)
    inverse_four_pi_squared_without_pi = Fraction(1, 16)
    rank_two_pole_without_pi = tensor_reduction_factor * simplex_area * inverse_four_pi_squared_without_pi
    rows.append(check("dred_simplex_area", simplex_area == Fraction(1, 2), simplex_area, Fraction(1, 2)))
    rows.append(check("rank_two_A_pole_coefficient", rank_two_pole_without_pi == Fraction(1, 64), rank_two_pole_without_pi, Fraction(1, 64)))
    four_minus_d_coefficient = 2
    trace_residue_without_pi = four_minus_d_coefficient * rank_two_pole_without_pi
    rows.append(check("conditional_Q4S_trace_unit", trace_residue_without_pi == Fraction(1, 32), trace_residue_without_pi, Fraction(1, 32)))
    rows.append(check("reverse_trace_unit", -trace_residue_without_pi == Fraction(-1, 32), -trace_residue_without_pi, Fraction(-1, 32)))

    special_ht = {(0, 0, 0, 0): Fraction(1, 2), (1, 0, 0, 0): Fraction(1, 3), (1, 0, 1, 0): Fraction(1, 6), (1, 1, 1, 1): Fraction(1, 12)}
    for key, expected in special_ht.items():
        rows.append(check(f"ht_special_{'_'.join(map(str, key))}", ht_coefficient(*key) == expected, ht_coefficient(*key), expected))
    rows.append(check("ht_factor_two_fork", Fraction(1, 1) / ht_coefficient(0, 0, 0, 0) == 2, Fraction(1, 1) / ht_coefficient(0, 0, 0, 0), 2))

    origin_main = git("rev-parse", "origin/main")
    pinned_object_type = git("cat-file", "-t", AUTHORITY_COMMIT)
    step3d = authority_text("contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md")
    step5a = authority_text("contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md")
    step5a_receipt = json.loads(authority_text(STEP5A_RECEIPT))
    rows.append(check("authority_origin_main_pin", origin_main == AUTHORITY_COMMIT, origin_main, AUTHORITY_COMMIT))
    rows.append(check("authority_pinned_object_type", pinned_object_type == "commit", pinned_object_type, "commit"))
    rows.append(check("authority_step5a_receipt_status", step5a_receipt.get("status") == "PASS_EXACT_PARTIAL_SCOPE", step5a_receipt.get("status"), "PASS_EXACT_PARTIAL_SCOPE"))
    rows.append(check("authority_step5a_receipt_contract", step5a_receipt.get("contract_path") == "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md", step5a_receipt.get("contract_path"), "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"))
    rows.append(check("authority_tau_E", r"\tau_E:=-\frac1{\hbar}" in step3d, r"\tau_E:=-\frac1{\hbar}" in step3d, True))
    rows.append(check("authority_euclidean_source_exponent", r"-\frac1{\hbar}S_{0,E}+\frac1{\hbar}\mathscr J_E^{\rm phys}" in step3d, r"-\frac1{\hbar}S_{0,E}+\frac1{\hbar}\mathscr J_E^{\rm phys}" in step3d, True))
    step5a_compact = compact_tex(step5a)
    exact_vector_anchor = compact_tex(r"\langle V^A(p,\vartheta_1)V^B(p',\vartheta_2)\rangle_E&=-(2\pi)^4\delta^4(p+p')\frac{2\hbar g^2\kappa^{AB}}{p^2}\delta^4(\vartheta_1-\vartheta_2)")
    exact_matter_anchor = compact_tex(r"\langle\Phi^A(p,1)\widetilde\Phi^B(p',2)\rangle_E&=(2\pi)^4\delta^4(p+p')\frac{\hbar g^2\kappa^{AB}}{16p^2}\bar D_1^2D_1^2\delta^4(\vartheta_1-\vartheta_2)")
    vector_anchor_found = exact_vector_anchor in step5a_compact
    matter_anchor_found = exact_matter_anchor in step5a_compact
    rows.append(check("authority_exact_vector_momentum_rule", vector_anchor_found, vector_anchor_found, True))
    rows.append(check("authority_exact_matter_momentum_rule", matter_anchor_found, matter_anchor_found, True))
    vector_rescaled_sign = Fraction(-2, 2)
    matter_rescaled_coefficient = Fraction(1, 16)
    rows.append(check("rescaled_vector_propagator_sign", vector_anchor_found and vector_rescaled_sign == -1, vector_rescaled_sign, -1))
    rows.append(check("rescaled_matter_propagator_sign", matter_anchor_found and matter_rescaled_coefficient == Fraction(1, 16), matter_rescaled_coefficient, Fraction(1, 16)))

    rows.extend(archive_integrity_checks("initial_pro", PRO_INITIAL))
    rows.extend(archive_integrity_checks("derivation_pro", PRO_DERIVATION))
    rows.extend(archive_integrity_checks("final_pro", PRO_FINAL))
    rows.append(check("strictification_audit", AUDIT.is_file(), AUDIT.is_file(), True))
    if AUDIT.is_file():
        audit_text = AUDIT.read_text(encoding="utf-8")
        authority_receipt = f"Authority: verified `origin/main@{AUTHORITY_COMMIT}`, workflow run `{AUTHORITY_VERIFY_RUN}`."
        rows.append(check("audit_authority_workflow_receipt_metadata", authority_receipt in audit_text, authority_receipt in audit_text, True))
        audit_compact = compact_tex(audit_text)
        audit_vector_anchor = compact_tex(r"\boxed{-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12})}")
        audit_matter_anchor = compact_tex(r"\boxed{+\delta_{rs}\frac{\hbar\kappa^{AB}}{16p^2}\bar D_1^2D_1^2\delta^4(\theta_{12})}")
        rows.append(check("audit_exact_rescaled_vector_rule", audit_vector_anchor in audit_compact, audit_vector_anchor in audit_compact, True))
        rows.append(check("audit_exact_rescaled_matter_rule", audit_matter_anchor in audit_compact, audit_matter_anchor in audit_compact, True))
        for blocker in BLOCKERS:
            rows.append(check(f"audit_blocker_{blocker}", blocker in audit_text, blocker in audit_text, True))
    return rows


def main() -> None:
    rows = all_checks()
    failed = [row for row in rows if row["status"] != "PASS"]
    result = {
        "scope": SCOPE,
        "claim_boundary": CLAIM_BOUNDARY,
        "certifies_full_diagram_derivation": False,
        "authority": {
            "commit": AUTHORITY_COMMIT,
            "origin_main_at_check": git("rev-parse", "origin/main"),
            "verify_run": AUTHORITY_VERIFY_RUN,
            "verify_run_receipt_kind": "RECORDED_METADATA_NOT_LIVE_GITHUB_QUERY",
            "foundation_reads": "PINNED_GIT_OBJECTS_ONLY",
        },
        "coarse_port_pair_count": {
            "status": "COARSE_ORDERED_PORT_PAIR_COUNT_ONLY__NOT_SOURCE_HESSIAN_CENSUS",
            "count_kind": "ORDERED_DISTINCT_COARSE_PORT_PAIRS",
            "certifies_source_hessian_census": False,
            "I0": 2,
            "I1": 18,
            "I2": 72,
            "total": 92,
            "nonlink": 50,
            "link_dependent": 42,
        },
        "dword_coverage": {"status": "BLOCKED", "required": None, "replayed": 0},
        "cut_coverage": {"status": "BLOCKED", "coarse_candidate_edge_positions": 12, "oriented_edge_kernels": 0, "paired": 0},
        "ht_coverage": {"status": "EXTERNAL_TARGET_ARITHMETIC_ONLY", "special_values_checked": 4, "source_roundtrip_certified": False},
        "full_diagram_derivation": {"status": FULL_STATUS, "pass_from_this_script_implies_completion": False},
        "blockers": list(BLOCKERS),
        "checks": rows,
        "summary": {"status": "FAIL" if failed else "PASS", "passed": len(rows) - len(failed), "failed": len(failed), "scope": SCOPE},
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
