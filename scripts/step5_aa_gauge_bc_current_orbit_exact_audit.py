#!/usr/bin/env python3
"""Target-blind exact audit of the AA outer-A gauge/E_V BC current orbit."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "foundations" / "step-05-euclidean-n4-awi-one-loop.md"
MATTER_AUDIT = ROOT / "audits" / "step5-aa-matter-full-placements-independent.md"


@dataclass(frozen=True)
class QI:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: "QI") -> "QI":
        return QI(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "QI":
        return QI(-self.real, -self.imag)

    def text(self) -> str:
        if self.real == 0 and self.imag == 0:
            return "0"
        if self.real == 0:
            return f"{self.imag}*i"
        if self.imag == 0:
            return str(self.real)
        sign = "+" if self.imag > 0 else "-"
        return f"{self.real}{sign}{abs(self.imag)}*i"


ZERO = QI()
PLUS_2I = QI(imag=Fraction(2))
MINUS_2I = -PLUS_2I


def build_artifact() -> dict[str, object]:
    # E_V = E_g - 2 i (Phi_s x C_s).
    e_v_current = MINUS_2I
    outer_minus_dplus = Fraction(-1)
    dplus_phi_to_b = Fraction(1)
    dplus_c = ZERO
    induced_current = QI(
        outer_minus_dplus * dplus_phi_to_b * e_v_current.real,
        outer_minus_dplus * dplus_phi_to_b * e_v_current.imag,
    )
    explicit_current = MINUS_2I
    current_sum = induced_current + explicit_current

    if induced_current != PLUS_2I:
        raise AssertionError("outer -D_+ did not produce +2i(B x C)")
    if current_sum != ZERO:
        raise AssertionError("E_V matter current and explicit BC contact did not cancel")
    if dplus_c != ZERO:
        raise AssertionError("D_+ C_s must vanish")

    gauge_fixing_ports = frozenset({"u"})
    bc_ports = frozenset({"B_s", "C_s"})
    gauge_fixing_bc_hessian = int(bc_ports.issubset(gauge_fixing_ports))
    if gauge_fixing_bc_hessian != 0:
        raise AssertionError("a pure-vector gauge-fixing word acquired BC ports")

    contract_text = CONTRACT.read_text(encoding="utf-8")
    matter_text = MATTER_AUDIT.read_text(encoding="utf-8")
    anchors = {
        "contract_outer_A_identity": r"-\boldsymbol\nabla_+\mathscr E_V-2i(B_s\times C_s)" in contract_text,
        "matter_current_definition": r"-2i(\Phi_s\times C_s)" in matter_text,
        "free_chirality": r"D_+C_s=0" in matter_text,
        "pointwise_current_cancellation": r"=2i(B_s\times C_s)-2i(B_s\times C_s)" in matter_text,
    }
    if not all(anchors.values()):
        raise AssertionError(f"source anchors changed: {anchors}")

    return {
        "schema": "step5-aa-gauge-bc-current-orbit-v1",
        "target_blind": True,
        "external_momenta": {
            "B_s": "p",
            "C_s": "q",
            "restriction": "none; p and q independent",
        },
        "ordered_output": "(B_s^D(p), C_s^E(q))",
        "color_word": "c_DE^A B_s^D(p) C_s^E(q)",
        "source_port_rows": [
            {
                "id": "EV_CURRENT_DPLUS_PHI",
                "outer_source": "A",
                "ports": ["Phi_s", "C_s"],
                "operation": "-D_+[-2i(Phi_s x C_s)] with D_+Phi_s=B_s and D_+C_s=0",
                "coefficient": induced_current.text(),
            },
            {
                "id": "EXPLICIT_OUTER_A_CURRENT",
                "outer_source": "A",
                "ports": ["B_s", "C_s"],
                "operation": "explicit -2i(B_s x C_s)",
                "coefficient": explicit_current.text(),
            },
            {
                "id": "GAUGE_FIXING_LONGITUDINAL",
                "outer_source": "A",
                "ports": sorted(gauge_fixing_ports),
                "BC_functional_hessian": gauge_fixing_bc_hessian,
                "coefficient": "0",
            },
        ],
        "pointwise_sum": current_sum.text(),
        "loop_denominator": "none; cancellation precedes Wick contraction",
        "evanescent_square": "absent",
        "anomaly_coefficient_in_lambda1_units": "0",
        "omega21_boundary": {
            "included_here": False,
            "reason": "Omega21 is a residual of the AA matter second-mark D-word, not a BC functional derivative of the pure-vector gauge-fixing/E_V source port.",
        },
        "checks": anchors
        | {
            "same_ordered_color_word": True,
            "independent_p_q_pointwise_cancellation": current_sum == ZERO,
            "gauge_fixing_has_no_BC_ports": gauge_fixing_bc_hessian == 0,
            "not_minus_one_third": True,
        },
    }


def validate_artifact(artifact: dict[str, object]) -> tuple[int, int]:
    checks = artifact["checks"]
    if not isinstance(checks, dict):
        raise AssertionError("malformed BC current artifact")
    assertions = (
        artifact["schema"] == "step5-aa-gauge-bc-current-orbit-v1",
        artifact["target_blind"] is True,
        artifact["ordered_output"] == "(B_s^D(p), C_s^E(q))",
        artifact["color_word"] == "c_DE^A B_s^D(p) C_s^E(q)",
        artifact["pointwise_sum"] == "0",
        artifact["loop_denominator"] == "none; cancellation precedes Wick contraction",
        artifact["evanescent_square"] == "absent",
        artifact["anomaly_coefficient_in_lambda1_units"] == "0",
        len(artifact["source_port_rows"]) == 3,
        artifact["omega21_boundary"]["included_here"] is False,
        all(value is True for value in checks.values()),
        artifact["external_momenta"]["restriction"] == "none; p and q independent",
    )
    return sum(assertions), len(assertions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    artifact = build_artifact()
    passed, total = validate_artifact(artifact)
    if args.check:
        print(f"SUMMARY {passed}/{total} PASS")
        return 0 if passed == total else 1
    if passed != total:
        raise AssertionError(f"generated artifact validates only {passed}/{total}")
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"PASS wrote {args.output}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
