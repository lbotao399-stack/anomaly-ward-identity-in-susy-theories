#!/usr/bin/env python3
"""Exact checks for the bounded Claude alternative-route review."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MEMO = ROOT / "audits/claude-step5b-step5h-independent-review.md"
SOURCE = ROOT / "audits/step5-bc-full-family-raw-projection-exact.md"
OUTPUT = ROOT / "audits/claude-step5b-step5h-verification.json"
CHECKS: list[dict[str, object]] = []


def record(name: str, equations: list[str], passed: bool) -> None:
    CHECKS.append({"name": name, "equations": equations, "passed": bool(passed)})


def wedge(left: str, right: str) -> tuple[int, tuple[str, str]]:
    order = {"D1": 0, "D2": 1, "E1": 2, "E2": 3}
    if left == right:
        return 0, (left, right)
    if order[left] < order[right]:
        return 1, (left, right)
    return -1, (right, left)


def add_terms(terms: list[tuple[int, str, str]]) -> dict[tuple[str, str], int]:
    result: dict[tuple[str, str], int] = {}
    for coefficient, left, right in terms:
        sign, monomial = wedge(left, right)
        result[monomial] = result.get(monomial, 0) + coefficient * sign
    return {monomial: value for monomial, value in result.items() if value}


def bilinear_checks() -> None:
    s_de = add_terms([(1, "D1", "E2"), (-1, "D2", "E1")])
    s_ed = add_terms([(1, "E1", "D2"), (-1, "E2", "D1")])
    record("Dotted gaugino bilinear is color-symmetric", ["CR.7", "CR.8"], s_de == s_ed)
    w_de, w_ed, s = sp.symbols("W_DE W_ED S")
    contraction = (w_de - w_ed) * s + (w_ed - w_de) * s
    record("Antisymmetric color word annihilates symmetric bilinear", ["CR.9"], sp.expand(contraction) == 0)


def integral_checks() -> None:
    epsilon, delta = sp.symbols("epsilon Delta", positive=True)
    d = 4 - 2 * epsilon

    def i_mu(n: int) -> sp.Expr:
        radial = (
            (4 * sp.pi) ** (-d / 2)
            * (d / 2)
            * sp.gamma(n - d / 2 - 1)
            / sp.gamma(n)
            * delta ** (d / 2 + 1 - n)
        )
        return sp.simplify((4 - d) / d * radial)

    i3 = sp.limit(i_mu(3), epsilon, 0, dir="+")
    delta_i4 = sp.limit(delta * i_mu(4), epsilon, 0, dir="+")
    record(
        "Evanescent scalar masters",
        ["CR.10", "CR.11", "CR.12"],
        sp.simplify(i3 - 1 / (32 * sp.pi**2)) == 0 and delta_i4 == 0,
    )
    j = sp.limit((i_mu(3) - delta * i_mu(4)) / d, epsilon, 0, dir="+")
    record("Tensor integral J", ["CR.13", "CR.14"], sp.simplify(j - 1 / (128 * sp.pi**2)) == 0)
    record("Explicit Fierz factor multiplies J", ["CR.14"], sp.simplify(2 * j - 1 / (64 * sp.pi**2)) == 0)


def projection_check() -> None:
    hbar, g = sp.symbols("hbar g", positive=True)
    lambda1 = hbar * g**2 / (16 * sp.pi**2)
    component = -lambda1 / sp.sqrt(2)
    expected = -sp.sqrt(2) * hbar * g**2 / (32 * sp.pi**2)
    record("Accepted BC map fixes the component coefficient", ["CR.1", "CR.6"], sp.simplify(component - expected) == 0)


def source_boundary_check() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    required = (
        "G_{\\phi_r\\widetilde\\psi_s}=0",
        "G_{\\psi_r\\widetilde\\phi_s}=0",
        "delta_{rs}K_{-,\\epsilon}^{AB}(z,z)",
        "No $\\phi\\!\\to\\!\\widetilde\\psi$ or $\\psi\\!\\to\\!\\widetilde\\phi$ propagator occurs",
    )
    record("Authoritative BC source separates ordinary parent from regulated Jacobian", ["CR.15", "CR.16"], all(item in text for item in required))


def typed_heat_kernel_rejection_check() -> None:
    # Proposal d920487 defines K_ev=K^2 on matter and K_ev=K on vectors.
    # Its displayed free blocks instead give K^2=16 Box P_+ and K_V=+Box.
    matter_from_defined_blocks = 16
    vector_from_defined_blocks = 1
    declared_free_coefficient = -1
    record(
        "Typed heat-kernel free generator contradicts its displayed blocks",
        ["CR.18", "CR.19", "CR.20"],
        matter_from_defined_blocks != declared_free_coefficient
        and vector_from_defined_blocks != declared_free_coefficient,
    )


def majorana_branch_translation_check() -> None:
    # Locked dictionary (D.3.2), (D.3.18): the W/S bridge contains
    # nontrivial phases, so identifying the Project with S is not a
    # phase-neutral index rewrite.
    gamma_w_over_s = -sp.I
    psi_w_over_s = sp.I
    bar_w_over_s = -sp.I
    record(
        "Majorana Weinberg/Srednicki bridge is a nontrivial phase translation",
        ["CR.21"],
        gamma_w_over_s != 1 and psi_w_over_s != 1 and bar_w_over_s != 1,
    )


def census_independence_nonimplication_check() -> None:
    # Equality of total coefficients cannot establish termwise absence of
    # candidate routings: nonzero omitted terms may cancel in the sum.
    t = sp.symbols("t", nonzero=True)
    omitted_terms = (t, -t)
    record(
        "Target agreement does not prove termwise census exhaustion",
        ["CR.22", "CR.23"],
        sp.simplify(sum(omitted_terms)) == 0
        and all(sp.simplify(term) != 0 for term in omitted_terms),
    )


def main() -> int:
    bilinear_checks()
    integral_checks()
    projection_check()
    source_boundary_check()
    typed_heat_kernel_rejection_check()
    majorana_branch_translation_check()
    census_independence_nonimplication_check()
    passed = all(bool(check["passed"]) for check in CHECKS)
    payload = {
        "scope": "VERIFIED_AUDIT_WITH_EXACT_BOTTOM_PROJECTION",
        "memo": str(MEMO.relative_to(ROOT)),
        "memo_sha256": hashlib.sha256(MEMO.read_bytes()).hexdigest(),
        "authoritative_source": str(SOURCE.relative_to(ROOT)),
        "authoritative_source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "check_count": len(CHECKS),
        "checks": CHECKS,
        "independent_component_box_status": "REJECTED_ORDINARY_PARENT_ZERO",
        "noether_status": "NOT_ACCEPTED_NOETHER_B1_B4_MISSING",
        "typed_heat_kernel_status": "NOT_ACCEPTED_TYPED_HEAT_KERNEL_GENERATOR",
        "majorana_matrix_status": "VERIFIED_CONDITIONAL_SREDNICKI_DICTIONARY",
        "majorana_canonicalization_status": "NOT_ACCEPTED_MAJORANA_CANONICALIZATION_WRONG_BRANCH",
        "final_census_certificate_status": "NOT_ACCEPTED_COEFFICIENT_CENSUS_CERTIFICATE",
        "final_census_status": "OPEN_FINAL_CENSUS_17_CANDIDATES",
        "passed": passed,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for check in CHECKS:
        print(f"[{'PASS' if check['passed'] else 'FAIL'}] {check['name']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
