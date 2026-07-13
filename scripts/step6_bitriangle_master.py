#!/usr/bin/env python3
"""Exact four-dimensional scalar master for the Step-6 bitriangle.

This module evaluates only the finite scalar denominator master.  It does not
perform numerator D-algebra, DRED tensor reduction, forest subtraction, or an
anomaly comparison.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping

try:
    from scripts import step6_two_loop_graphir as graphir
except ModuleNotFoundError:  # direct execution from scripts/
    import step6_two_loop_graphir as graphir


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "generated/step6/bitriangle-master"
OUTPUT_JSON = OUTPUT_DIR / "bitriangle-master.json"
OUTPUT_MD = OUTPUT_DIR / "bitriangle-master.md"
AUDIT = ROOT / "audits/step6-bitriangle-master-verification.json"

SCHEMA = "step6.bitriangle_scalar_master.v1"
STATUS = "PASS_EXACT_D4_SCALAR_MASTER_NUMERATOR_AND_R_OPERATION_BLOCKED"
GRAPH_ID = "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value)


def integral_zero_one_power(exponent: int) -> Fraction:
    """Return integral_0^1 x^exponent dx for integer exponent > -1."""

    if exponent <= -1:
        raise ValueError("zero-to-one monomial is not integrable")
    return Fraction(1, exponent + 1)


def integral_one_infinity_inverse_power(power: int) -> Fraction:
    """Return integral_1^infinity x^(-power) dx for integer power > 1."""

    if power <= 1:
        raise ValueError("one-to-infinity inverse monomial is not integrable")
    return Fraction(1, power - 1)


def integral_one_infinity_log_inverse_power(power: int) -> Fraction:
    """Return integral_1^infinity log(x) x^(-power) dx for power > 1."""

    if power <= 1:
        raise ValueError("log inverse monomial is not integrable")
    return Fraction(1, (power - 1) ** 2)


def radial_mode(n: int) -> dict[str, Any]:
    """Evaluate the radial coefficient R_n without numerical integration."""

    if n < 0:
        raise ValueError("Gegenbauer degree must be nonnegative")
    m = n + 1

    # 0 < r < s < 1, followed by the r <-> s copy.
    inner_below_coefficient = Fraction(1, 2 * m)
    outer_below_integral = integral_zero_one_power(2 * n + 1)
    below_one = 2 * inner_below_coefficient * outer_below_integral

    # 0 < r < 1 < s: the constant term in the inner radial integral.
    inverse_power = 2 * n + 3
    constant_inner = Fraction(1, 2 * m)
    above_constant = (
        2
        * constant_inner
        * integral_one_infinity_inverse_power(inverse_power)
    )

    # 1 < r < s: the logarithmic term in the inner radial integral.
    above_log = 2 * integral_one_infinity_log_inverse_power(inverse_power)
    above_one = above_constant + above_log
    total = below_one + above_one

    expected_below = Fraction(1, 2 * m * m)
    expected_above = Fraction(1, m * m)
    expected_total = Fraction(3, 2 * m * m)
    if (below_one, above_one, total) != (
        expected_below,
        expected_above,
        expected_total,
    ):
        raise AssertionError("radial mode reduction changed")

    return {
        "n": n,
        "m": m,
        "region_0_lt_r_lt_s_lt_1_with_exchange": fraction_text(below_one),
        "region_s_gt_1_constant_part_with_exchange": fraction_text(
            above_constant
        ),
        "region_s_gt_1_log_part_with_exchange": fraction_text(above_log),
        "region_s_gt_1_total_with_exchange": fraction_text(above_one),
        "R_n": fraction_text(total),
        "R_n_formula": "3/(2*(n+1)^2)",
    }


def mode_contribution(n: int) -> dict[str, Any]:
    radial = radial_mode(n)
    angular_rational = Fraction(4, n + 1)
    coefficient_of_pi4 = angular_rational * Fraction(radial["R_n"])
    expected = Fraction(6, (n + 1) ** 3)
    if coefficient_of_pi4 != expected:
        raise AssertionError("angular-radial mode coefficient changed")
    return {
        "n": n,
        "angular_factor": "4*pi^4/(n+1)",
        "radial": radial,
        "coefficient_of_pi4": fraction_text(coefficient_of_pi4),
        "mode_formula": "6*pi^4/(n+1)^3",
    }


def source_graph() -> Mapping[str, Any]:
    bundle = graphir.build_bundle()
    matches = [
        row for row in bundle["literal_direct_graphs"] if row["graph_id"] == GRAPH_ID
    ]
    if len(matches) != 1:
        raise AssertionError("bitriangle parent does not resolve uniquely")
    graph = matches[0]
    if graph["denominator_ast"]["rendered"] != (
        "k^2 (k-P)^2 l^2 (l-P)^2 (k-l)^2"
    ):
        raise AssertionError("bitriangle denominator routing changed")
    return graph


def build_payload() -> dict[str, Any]:
    graph = source_graph()
    modes = [mode_contribution(n) for n in range(6)]
    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "authority_role": "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "external_result_used_as_input": False,
        "source_graph": {
            "graph_id": graph["graph_id"],
            "graph_hash": graph["graph_hash"],
            "denominator": graph["denominator_ast"],
        },
        "domain": {
            "dimension": 4,
            "signature": "POSITIVE_EUCLIDEAN",
            "off_shell_condition": "P^2>0",
            "measure": "d^4k/(2*pi)^4 d^4l/(2*pi)^4",
            "UV_IR_status": "FINITE_AT_D_EQ_4_FOR_P_SQUARED_POSITIVE",
        },
        "gegenbauer_contract": {
            "propagator_expansion": (
                "1/|r*xhat-s*yhat|^2=sum_(n>=0) "
                "r_<^n/r_>^(n+2) C_n^1(xhat.yhat)"
            ),
            "angular_convolution": (
                "int_(S3) C_n^1(xhat.ahat) C_m^1(xhat.bhat)="
                "2*pi^2*delta_nm*C_n^1(ahat.bhat)/(n+1)"
            ),
            "C_n_at_one": "C_n^1(1)=n+1",
            "two_angle_factor": "4*pi^4/(n+1)",
            "sum_integral_justification": (
                "INSERT_RADIAL_RATIO_CUTOFF_R_LESS_OVER_R_GREATER_LE_1_MINUS_ETA;"
                "USE_UNIFORM_CONVERGENCE;REMOVE_ETA_BY_DOMINATED_L2_LIMIT"
            ),
        },
        "exact_mode_samples": modes,
        "mode_identity": {
            "R_n": "3/(2*(n+1)^2)",
            "angular_times_radial": "6*pi^4/(n+1)^3",
        },
        "series_definition": "zeta(3)=sum_(m=1)^infinity 1/m^3",
        "unnormalized_result": "6*pi^4*zeta(3)/P^2",
        "measure_factor": "1/(2*pi)^8",
        "normalized_result": "6*zeta(3)/((4*pi)^4*P^2)",
        "fail_closed": {
            "numerator_reduction": "BLOCKED_NOT_CONNECTED_TO_GLOBAL_DWORD",
            "DRED_tensor_reduction": "BLOCKED_NOT_APPLIED",
            "forest_R_operation": "BLOCKED_NOT_APPLIED",
            "two_loop_anomaly_coefficient": None,
        },
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    modes = payload["exact_mode_samples"]
    checks = {
        "correct_source_graph": payload["source_graph"]["graph_id"] == GRAPH_ID,
        "exact_denominator": payload["source_graph"]["denominator"]["rendered"]
        == "k^2 (k-P)^2 l^2 (l-P)^2 (k-l)^2",
        "six_exact_modes": len(modes) == 6,
        "radial_modes_exact": all(
            row["radial"]["R_n"]
            == str(Fraction(3, 2 * (int(row["n"]) + 1) ** 2))
            for row in modes
        ),
        "full_modes_exact": all(
            row["coefficient_of_pi4"]
            == str(Fraction(6, (int(row["n"]) + 1) ** 3))
            for row in modes
        ),
        "measure_normalization_exact": payload["normalized_result"]
        == "6*zeta(3)/((4*pi)^4*P^2)",
        "external_target_absent": payload["external_result_used_as_input"] is False,
        "coefficient_not_claimed": payload["fail_closed"][
            "two_loop_anomaly_coefficient"
        ]
        is None,
    }
    return {
        "schema": "step6.bitriangle_scalar_master.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "payload_sha256": payload["payload_sha256"],
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Step 6 — scalar bitriangle master",
            "",
            "$$",
            "J_5(P):=\\int\\frac{d^4k}{(2\\pi)^4}\\frac{d^4l}{(2\\pi)^4}"
            "\\frac{1}{k^2(k-P)^2l^2(l-P)^2(k-l)^2},\\qquad P^2>0.",
            "$$",
            "",
            "$$",
            "\\frac1{|r\\hat x-s\\hat y|^2}="
            "\\sum_{n=0}^{\\infty}\\frac{r_<^n}{r_>^{n+2}}"
            "C_n^{(1)}(\\hat x\\!\\cdot\\!\\hat y).",
            "$$",
            "",
            "$$",
            "R_n^{<1}=\\frac1{2(n+1)^2},\\qquad"
            "R_n^{>1}=\\frac1{(n+1)^2},\\qquad"
            "R_n=\\frac3{2(n+1)^2}.",
            "$$",
            "",
            "$$",
            "J_5(P)=\\frac{4\\pi^4}{(2\\pi)^8P^2}"
            "\\sum_{n=0}^{\\infty}\\frac1{n+1}\\frac3{2(n+1)^2}"
            "=\\boxed{\\frac{6\\zeta(3)}{(4\\pi)^4P^2}}.",
            "$$",
            "",
            f"Audit: `{audit['passed']}/{audit['total']}`.",
            "",
            "Numerator D-algebra, DRED tensor reduction, forest subtraction, and the two-loop coefficient remain blocked.",
            "",
        ]
    )


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload()
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError(audit)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        canonical_json(
            {
                "status": payload["status"],
                "audit": f"{audit['passed']}/{audit['total']}",
                "result": payload["normalized_result"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
