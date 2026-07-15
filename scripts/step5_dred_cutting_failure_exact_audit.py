#!/usr/bin/env python3
"""Exact audit of the DRED triangle versus Schwinger-cut remainder."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits" / "step5-dred-cutting-failure-exact.md"


@dataclass(frozen=True)
class Check:
    name: str
    actual: object
    expected: object

    @property
    def passed(self) -> bool:
        if isinstance(self.actual, sp.Basic) or isinstance(self.expected, sp.Basic):
            return sp.simplify(self.actual - self.expected) == 0
        return self.actual == self.expected


def main() -> int:
    epsilon = sp.symbols("epsilon", positive=True)
    mu, Delta = sp.symbols("mu Delta", positive=True)
    hbar, g = sp.symbols("hbar g", nonzero=True)
    D0, D1, D2 = sp.symbols("D0 D1 D2", nonzero=True)
    d = 4 - 2 * epsilon

    i2 = (
        mu ** (2 * epsilon)
        * sp.gamma(epsilon)
        * Delta ** (-epsilon)
        / (4 * sp.pi) ** (2 - epsilon)
    )
    delta_i3 = epsilon * i2 / 2
    l2_i3 = i2 - delta_i3
    ev_i3 = (4 - d) * l2_i3 / d
    finite_one_denominator = sp.limit(ev_i3, epsilon, 0, dir="+")
    simplex_area = sp.integrate(1 - sp.symbols("y"), (sp.symbols("y"), 0, 1))
    triangle_finite = 2 * simplex_area * finite_one_denominator
    source_prefactor = -g**2 / (4 * sp.sqrt(2))
    g2_propagators = -hbar**3 / 256
    g2_vertices = 2 * g**2 / hbar**2
    g2_pred = source_prefactor * g2_vertices * g2_propagators
    g3_pred = source_prefactor * (-g2_vertices) * g2_propagators
    g1_plus_pred = source_prefactor * (g**2 / (128 * hbar**2)) * (hbar**3 / 16)

    checks = [
        Check("dimension_split", d, 4 - 2 * epsilon),
        Check("positive_evanescent_trace", 4 - d, 2 * epsilon),
        Check("negative_formal_d_minus_four_trace", d - 4, -2 * epsilon),
        Check("gamma_recurrence", sp.gamma(1 + epsilon), epsilon * sp.gamma(epsilon)),
        Check("delta_I3_relation", delta_i3 / i2, epsilon / 2),
        Check("l2_I3_reduction", l2_i3 / i2, d / 4),
        Check("evanescent_tensor_fraction", ev_i3 / i2, epsilon / 2),
        Check("finite_one_denominator", finite_one_denominator, 1 / (32 * sp.pi**2)),
        Check("simplex_area", simplex_area, sp.Rational(1, 2)),
        Check("feynman_factor_times_area", 2 * simplex_area, 1),
        Check("finite_triangle", triangle_finite, 1 / (32 * sp.pi**2)),
        Check("reverse_finite_triangle", -triangle_finite, -1 / (32 * sp.pi**2)),
        Check("full_square_cut_edge_0", D0 / (D0 * D1 * D2) - 1 / (D1 * D2), 0),
        Check("full_square_cut_edge_1", D1 / (D0 * D1 * D2) - 1 / (D0 * D2), 0),
        Check("full_square_cut_edge_2", D2 / (D0 * D1 * D2) - 1 / (D0 * D1), 0),
        Check("AB1_G2_direct_Wick_preD", g2_pred, sp.sqrt(2) * hbar * g**4 / 1024),
        Check("AB1_G32_direct_Wick_preD", g3_pred, -sp.sqrt(2) * hbar * g**4 / 1024),
        Check("AB1_G33_direct_Wick_preD", -g3_pred, sp.sqrt(2) * hbar * g**4 / 1024),
        Check("AB1_G1_plus_per_word_preD", g1_plus_pred, -hbar * g**4 / (8192 * sp.sqrt(2))),
    ]

    text = AUDIT.read_text(encoding="utf-8")
    required = {
        "metric_split": r"\delta_d^{MN}=\bar\delta^{MN}+\widetilde\delta^{MN}",
        "user_evanescent_square": r"\widehat\ell_{\rm user}^{\,2}",
        "positive_anomaly_square": r"\mu_\ell^2=-\widehat\ell_{\rm user}^{\,2}",
        "project_notation_map": r"\breve\delta=\delta_4-\widehat\delta",
        "projector_nonidentity": r"\widetilde\delta\) is not \(-\breve\delta\)",
        "distinct_scalar_regulator": "scalar dimension-shift representation is a distinct regulator axiom",
        "four_dimensional_d_square": r"\frac18",
        "pointwise_zero": r"\Gamma_{G,i}^{(d)}",
        "finite_master": r"\frac1{32\pi^2}",
        "graph_specific_residual": r"C_G\mathcal R_G",
        "premature_continuation_error": "premature dimensional-continuation error",
        "open_graph_dword": "DRED-CUT-G5",
        "direct_Wick_prefactor": r"C_{G_2}^{\rm preD}",
    }
    checks.extend(
        Check(f"audit_anchor_{name}", anchor in text, True)
        for name, anchor in required.items()
    )

    failed = [check for check in checks if not check.passed]
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"{status} {check.name}: {check.actual}")
    print(f"SUMMARY {len(checks) - len(failed)}/{len(checks)} PASS")

    if failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
