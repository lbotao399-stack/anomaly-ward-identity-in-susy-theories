#!/usr/bin/env python3
"""Adjudicate the HT factor-two conflict against the target-blind Project simplex.

The source-internal part compares the exact master triangle, the differential
operator, Appendix B, and the zero-shift component/compact displays.  The
Project part then uses only the independently derived denominator identity

    1/(D0 D1 D2) = 2 int_Delta2 1/(L^2+Delta)^3

to decide which printed branch has the normalization of a complete Project
triangle amplitude.  No Project letter-family coefficient is used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references/vendor/arxiv/2512.07771v2/source/main.tex"
JSON_OUT = ROOT / "audits/step5-ht-zero-shift-factor-two-adjudication.json"
MD_OUT = ROOT / "audits/step5-ht-zero-shift-factor-two-adjudication.md"


class Ledger:
    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []

    def check(self, row_id: str, actual: object, expected: object) -> None:
        passed = actual == expected
        self.rows.append(
            {
                "id": row_id,
                "actual": str(actual),
                "expected": str(expected),
                "pass": passed,
            }
        )
        if not passed:
            raise AssertionError(f"{row_id}: {actual!r} != {expected!r}")


def require(text: str, anchor: str, ledger: Ledger, row_id: str) -> None:
    ledger.check(row_id, anchor in text, True)


def build() -> tuple[dict[str, object], str]:
    text = SOURCE.read_text(encoding="utf-8")
    ledger = Ledger()

    master_anchor = (
        r"\mathcal{I}_{\tri}[\lambda;0] &= \frac{1}{2}"
        r"\lambda_1\wedge \lambda_2"
    )
    differential_anchor = (
        r"\mathcal{D}^{\tri}_{0,0}(f,g) = \frac{1}{2} "
        r"\partial_{\dot\alpha} f \partial^{\dot\alpha}g"
    )
    appendix_anchor = r"m!n! C_{mn} = \frac{1}{m+n+2}"
    shifted_bgamma_anchor = (
        r"Q_1( b^A(z) (\gamma^I)^B(w) )"
        " \n        &= " + r"\kappa^2"
    )
    component_bgamma_anchor = (
        r"Q_1(b^A(\gamma^I)^B) "
        "\n        &= " + r"\kappa^2"
    )
    compact_anchor = r"Q_1 (C^A(\theta) C^B(\theta')) = -\kappa^2"

    require(text, master_anchor, ledger, "HTF2-01-master-triangle-half")
    require(text, differential_anchor, ledger, "HTF2-02-Dtri00-half")
    require(text, appendix_anchor, ledger, "HTF2-03-appendix-Cmn")
    require(text, shifted_bgamma_anchor, ledger, "HTF2-04-shifted-pair-anchor")
    require(text, component_bgamma_anchor, ledger, "HTF2-05-component-pair-anchor")
    require(text, compact_anchor, ledger, "HTF2-06-compact-anchor")

    master_zero = Fraction(1, 2)
    dtri_zero = Fraction(1, 2)
    appendix_c00 = Fraction(1, 0 + 0 + 2) * Fraction(1, 0 + 0 + 1)
    shifted_output_coefficient = dtri_zero
    component_output_coefficient = Fraction(1, 1)
    compact_component_coefficient = Fraction(1, 1)

    ledger.check("HTF2-07-master-equals-Dtri", master_zero, dtri_zero)
    ledger.check("HTF2-08-appendix-m0n0", appendix_c00, Fraction(1, 2))
    ledger.check(
        "HTF2-09-shifted-equals-appendix",
        shifted_output_coefficient,
        appendix_c00,
    )
    ledger.check(
        "HTF2-10-component-over-shifted",
        component_output_coefficient / shifted_output_coefficient,
        Fraction(2, 1),
    )
    ledger.check(
        "HTF2-11-compact-over-shifted",
        compact_component_coefficient / shifted_output_coefficient,
        Fraction(2, 1),
    )

    project_feynman_kernel_m0n0 = (
        Fraction(2, 1)
        * Fraction(1, 0 + 0 + 2)
        * Fraction(1, 0 + 0 + 1)
    )
    project_kernel_without_gamma3_m0n0 = (
        Fraction(1, 0 + 0 + 2) * Fraction(1, 0 + 0 + 1)
    )
    ledger.check(
        "HTF2-12-project-feynman-kernel",
        project_feynman_kernel_m0n0,
        1,
    )
    ledger.check(
        "HTF2-13-dropping-gamma3-gives-half",
        project_kernel_without_gamma3_m0n0,
        Fraction(1, 2),
    )

    passed = sum(bool(row["pass"]) for row in ledger.rows)
    artifact = {
        "schema": "step5-ht-zero-shift-factor-two-adjudication-v1",
        "status": "SOURCE_INTERNAL_FACTOR_TWO_PROVED__PROJECT_FEYNMAN_AND_COMPONENT_BRANCH_SELECTED",
        "source": str(SOURCE.relative_to(ROOT)),
        "external_project_coefficient_used": False,
        "values": {
            "master_triangle_zero_shift": "1/2",
            "Dtri_00": "1/2",
            "appendix_C00": "1/2",
            "zero_shift_component_display": "1",
            "compact_component_display": "1",
            "display_over_integral_ratio": "2",
        },
        "adjudication": {
            "selected_for_complete_project_comparison": "zero-shift component display + compact display",
            "reason": "the target-blind Project denominator identity contributes Gamma(3)=2 and 2*Vol(Delta2)=1",
            "ht_branches_missing_complete_amplitude_factor_two": "master triangle differential operator + generic shifted formulas + Appendix B",
            "project_kernel_prefactor": "retain the leading factor 2 in K^P_mn",
            "project_kernel": "2*sum_{k,l} binom(m,k)binom(n,l)/((m+n+2)(k+l+1))",
            "scope": "global HT normalization only; relative Project letter-family discrepancies remain independent",
        },
        "checks": ledger.rows,
        "summary": {"passed": passed, "total": len(ledger.rows)},
    }

    md = r"""# Step 5 HT zero-shift factor-two adjudication

Status: `SOURCE_INTERNAL_FACTOR_TWO_PROVED__PROJECT_FEYNMAN_AND_COMPONENT_BRANCH_SELECTED`.

No Project letter-family coefficient is used.

## 1. Three integral-derived statements

The evaluated master triangle gives

$$
\mathcal I_{\rm tri}[\lambda;0]
=\frac12\lambda_1\wedge\lambda_2.
$$

The differential operator therefore obeys

$$
\mathcal D^{\rm tri}_{0,0}(f,g)
=\frac12\partial_{\dot\alpha}f\,\partial^{\dot\alpha}g.
$$

Appendix B gives

$$
m!n!C_{mn}
=\frac1{m+n+2}
\sum_{k=0}^{m}\sum_{l=0}^{n}
\frac1{k+l+1}
\binom mk\binom nl
(\lambda_1)_1^k(\lambda_1)_2^l
(\lambda_2)_1^{m-k}(\lambda_2)_2^{n-l}.
$$

At $m=n=0$,

$$
C_{00}=\frac1{2}\frac1{1}=\frac12.
$$

Hence

$$
\boxed{
\mathcal I_{\rm tri}[\lambda;0]
=\mathcal D^{\rm tri}_{0,0}
=C_{00}
=\frac12.}
$$

## 2. Conflict

The zero-shift component block and the compact-superfield block print unit
coefficients.  Therefore

$$
\frac{c_{\rm component}}{c_{\rm triangle}}
=\frac{1}{1/2}=2,
\qquad
\frac{c_{\rm compact}}{c_{\rm triangle}}
=\frac{1}{1/2}=2.
$$

The Project denominator identity is

$$
\frac1{D_0D_1D_2}
=2\int_{\Delta_2}\frac1{(L^2+\Delta)^3},
\qquad
2\int_{\Delta_2}1=1.
$$

Therefore the complete Project parameter kernel is

$$
\boxed{
\mathcal K^P_{m,n}(f^D,g^E)
=2\sum_{k=0}^{m}\sum_{l=0}^{n}
\frac{\binom mk\binom nl}
{(m+n+2)(k+l+1)}
(P_1^kP_2^lf^D)
(P_1^{m-k}P_2^{n-l}g^E).}
$$

Thus $\mathcal K^P_{0,0}=1$.  The source's zero-shift component and compact
branches have the complete-amplitude normalization.  Its master-integral,
generic shifted, and Appendix-B branches are uniformly smaller by $2$ and
must be multiplied by $2$ before comparison with the complete Project
amplitude.  This does not alter relative discrepancies among Project letter
families.
"""
    return artifact, md


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    artifact, md = build()
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if args.write:
        JSON_OUT.write_text(rendered, encoding="utf-8")
        MD_OUT.write_text(md, encoding="utf-8")
    if args.check:
        if JSON_OUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"FAIL stale {JSON_OUT}")
        if MD_OUT.read_text(encoding="utf-8") != md:
            raise SystemExit(f"FAIL stale {MD_OUT}")
    passed = artifact["summary"]["passed"]
    total = artifact["summary"]["total"]
    print(f"SUMMARY {passed}/{total} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
