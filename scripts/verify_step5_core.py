#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5-core-verification.json"
CONTRACT = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
SOURCE_LEDGER = ROOT / "audits/step5-source-translation-ledger.json"


@dataclass(frozen=True)
class QComplex:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QComplex":
        rhs = q(other)
        return QComplex(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "QComplex":
        return QComplex(-self.re, -self.im)

    def __sub__(self, other: object) -> "QComplex":
        return self + (-q(other))

    def __rsub__(self, other: object) -> "QComplex":
        return q(other) - self

    def __mul__(self, other: object) -> "QComplex":
        rhs = q(other)
        return QComplex(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "QComplex":
        rhs = q(other)
        denominator = rhs.re * rhs.re + rhs.im * rhs.im
        if denominator == 0:
            raise ZeroDivisionError
        return QComplex(
            (self.re * rhs.re + self.im * rhs.im) / denominator,
            (self.im * rhs.re - self.re * rhs.im) / denominator,
        )


def q(value: object) -> QComplex:
    if isinstance(value, QComplex):
        return value
    if isinstance(value, Fraction):
        return QComplex(value)
    if isinstance(value, int):
        return QComplex(Fraction(value))
    raise TypeError(value)


ZERO = QComplex()
ONE = q(1)
I = QComplex(Fraction(0), Fraction(1))


Matrix = list[list[QComplex]]


def zeros(rows: int, columns: int) -> Matrix:
    return [[ZERO for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    result = zeros(size, size)
    for index in range(size):
        result[index][index] = ONE
    return result


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def scale(coefficient: object, matrix: Matrix) -> Matrix:
    return [[q(coefficient) * value for value in row] for row in matrix]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    result = zeros(len(left), len(right[0]))
    for row in range(len(left)):
        for pivot in range(len(right)):
            if left[row][pivot] == ZERO:
                continue
            for column in range(len(right[0])):
                result[row][column] = (
                    result[row][column] + left[row][pivot] * right[pivot][column]
                )
    return result


def equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def left_multiply(variable: int) -> Matrix:
    result = zeros(16, 16)
    for monomial in range(16):
        if (monomial >> variable) & 1:
            continue
        sign = -1 if sum((monomial >> lower) & 1 for lower in range(variable)) % 2 else 1
        result[monomial | (1 << variable)][monomial] = q(sign)
    return result


def left_derivative(variable: int) -> Matrix:
    result = zeros(16, 16)
    for monomial in range(16):
        if not ((monomial >> variable) & 1):
            continue
        sign = -1 if sum((monomial >> lower) & 1 for lower in range(variable)) % 2 else 1
        result[monomial ^ (1 << variable)][monomial] = q(sign)
    return result


def grassmann_checks() -> dict[str, bool]:
    theta_plus, theta_minus, bar_plus, bar_minus = [left_multiply(i) for i in range(4)]
    d_theta_plus, d_theta_minus, d_bar_plus, d_bar_minus = [
        left_derivative(i) for i in range(4)
    ]

    # p_m=(0,0,0,1), so p_{a dot-a}=delta_{a dot-a}.
    d_plus = add(d_theta_plus, scale(I, bar_minus))
    d_minus = add(d_theta_minus, scale(-I, bar_plus))
    bar_d_plus = add(scale(-1, d_bar_minus), scale(-I, theta_plus))
    bar_d_minus = add(d_bar_plus, scale(-I, theta_minus))
    zero = zeros(16, 16)
    unit = identity(16)

    d_square = scale(2, multiply(d_minus, d_plus))
    bar_d_square = scale(2, multiply(bar_d_plus, bar_d_minus))
    d_bar_d_d = add(
        multiply(multiply(d_minus, bar_d_square), d_plus),
        scale(-1, multiply(multiply(d_plus, bar_d_square), d_minus)),
    )
    square_sum = add(
        multiply(d_square, bar_d_square),
        multiply(bar_d_square, d_square),
    )
    pi_half = scale(Fraction(1, 8), d_bar_d_d)
    pi_zero = scale(Fraction(-1, 16), square_sum)

    return {
        "D_plus_squared_zero": equal(multiply(d_plus, d_plus), zero),
        "D_minus_squared_zero": equal(multiply(d_minus, d_minus), zero),
        "barD_plus_squared_zero": equal(multiply(bar_d_plus, bar_d_plus), zero),
        "barD_minus_squared_zero": equal(multiply(bar_d_minus, bar_d_minus), zero),
        "mixed_plus_plus": equal(
            add(multiply(d_plus, bar_d_plus), multiply(bar_d_plus, d_plus)),
            scale(-2 * I, unit),
        ),
        "mixed_minus_minus": equal(
            add(multiply(d_minus, bar_d_minus), multiply(bar_d_minus, d_minus)),
            scale(-2 * I, unit),
        ),
        "mixed_plus_minus_zero": equal(
            add(multiply(d_plus, bar_d_minus), multiply(bar_d_minus, d_plus)),
            zero,
        ),
        "mixed_minus_plus_zero": equal(
            add(multiply(d_minus, bar_d_plus), multiply(bar_d_plus, d_minus)),
            zero,
        ),
        "project_identity_5_37": equal(
            d_bar_d_d,
            add(scale(8, unit), scale(Fraction(1, 2), square_sum)),
        ),
        "triple_D_identity_5_38": equal(
            multiply(multiply(d_square, bar_d_square), d_square),
            scale(-16, d_square),
        ),
        "triple_barD_identity_5_38": equal(
            multiply(multiply(bar_d_square, d_square), bar_d_square),
            scale(-16, bar_d_square),
        ),
        "pi_half_idempotent": equal(multiply(pi_half, pi_half), pi_half),
        "pi_zero_idempotent": equal(multiply(pi_zero, pi_zero), pi_zero),
        "projectors_orthogonal_left": equal(multiply(pi_half, pi_zero), zero),
        "projectors_orthogonal_right": equal(multiply(pi_zero, pi_half), zero),
        "projectors_complete": equal(add(pi_half, pi_zero), unit),
    }


def matrix2_multiply(left: Matrix, right: Matrix) -> Matrix:
    return multiply(left, right)


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def spinor_checks() -> dict[str, bool]:
    sigma1 = [[ZERO, ONE], [ONE, ZERO]]
    sigma2 = [[ZERO, -I], [I, ZERO]]
    sigma3 = [[ONE, ZERO], [ZERO, -ONE]]
    sigma_e = [scale(-I, sigma1), scale(-I, sigma2), scale(-I, sigma3), identity(2)]
    epsilon_up = [[ZERO, ONE], [-ONE, ZERO]]

    # Raise the dotted index on the second sigma: sigma_b{}^{dot-a}
    sigma_raised = [matrix2_multiply(sigma, transpose(epsilon_up)) for sigma in sigma_e]
    component_identity = True
    for m in range(4):
        for n in range(4):
            for a in range(2):
                for b in range(2):
                    lhs = ZERO
                    for dotted in range(2):
                        lhs += (
                            sigma_e[m][a][dotted] * sigma_raised[n][b][dotted]
                            + sigma_e[n][a][dotted] * sigma_raised[m][b][dotted]
                        )
                    epsilon_lower = [[ZERO, -ONE], [ONE, ZERO]]
                    rhs = -2 * epsilon_lower[a][b] * (1 if m == n else 0)
                    component_identity = component_identity and lhs == rhs

    p4 = [ZERO, ZERO, ZERO, ONE]
    p_bispinor = zeros(2, 2)
    for m in range(4):
        p_bispinor = add(p_bispinor, scale(p4[m], sigma_e[m]))
    p_minus_raised = [
        sum((epsilon_up[dotted][other] * p_bispinor[1][other] for other in range(2)), ZERO)
        for dotted in range(2)
    ]
    contraction = sum(
        (p_bispinor[0][dotted] * p_minus_raised[dotted] for dotted in range(2)),
        ZERO,
    )
    return {
        "sigma_identity_5_9_all_64_components": component_identity,
        "p_plus_p_minus_5_10_axis_check": contraction == ONE,
    }


def channel_checks() -> tuple[dict[str, bool], list[dict[str, object]]]:
    parities = {"W": 0, "Phi": 1, "TildePhi": 0, "TildeW": 1}
    nonzero = {"W": "dW", "Phi": "dPhi", "TildePhi": None, "TildeW": None}
    channels: list[dict[str, object]] = []
    for left in parities:
        for right in parities:
            terms: list[dict[str, object]] = []
            if nonzero[left] is not None:
                terms.append({"sign": 1, "word": [nonzero[left], right]})
            if nonzero[right] is not None:
                terms.append(
                    {
                        "sign": -1 if parities[left] else 1,
                        "word": [left, nonzero[right]],
                    }
                )
            channels.append(
                {
                    "id": f"{left}__{right}",
                    "left": left,
                    "right": right,
                    "left_parity": parities[left],
                    "tree_terms": terms,
                    "one_loop_seed_state": (
                        "DERIVED_WW_SEED_G2_OVER_64PI2"
                        if left == right == "W"
                        else "DEFERRED_NOT_GENERATED_BEFORE_SEED_ACCEPTANCE"
                    ),
                }
            )
    identifiers = [entry["id"] for entry in channels]
    return (
        {
            "sixteen_ordered_channels": len(channels) == 16,
            "sixteen_unique_ids": len(set(identifiers)) == 16,
            "reversed_orders_distinct": all(
                f"{right}__{left}" in identifiers
                for left in parities
                for right in parities
            ),
            "four_exact_zero_tree_rows": sum(not entry["tree_terms"] for entry in channels) == 4,
            "only_WW_seed_is_evaluated": sum(
                entry["one_loop_seed_state"] == "DERIVED_WW_SEED_G2_OVER_64PI2"
                for entry in channels
            ) == 1,
            "remaining_channels_are_deferred": sum(
                entry["one_loop_seed_state"]
                == "DEFERRED_NOT_GENERATED_BEFORE_SEED_ACCEPTANCE"
                for entry in channels
            ) == 15,
        },
        channels,
    )


def source_checks() -> dict[str, bool]:
    ledger = json.loads(SOURCE_LEDGER.read_text(encoding="utf-8"))
    messages = ledger["chat"]["messages"]
    all_claims = [claim for message in messages for claim in message["claims"]]
    verdicts = set(ledger["verdicts"])
    return {
        "seven_visible_messages": len(messages) == 7,
        "orders_exact": [message["order"] for message in messages] == list(range(7)),
        "hidden_turns_not_claimed": ledger["chat"]["hidden_turns_read"] is False,
        "all_claims_have_known_verdict": all(claim["verdict"] in verdicts for claim in all_claims),
        "initial_epsilon_numerator_rejected": next(
            claim for claim in all_claims if claim["id"] == "M2_EPSILON_NUMERATOR"
        )["verdict"]
        == "REJECTED",
        "later_contact_pole_conditional": next(
            claim for claim in all_claims if claim["id"] == "M3_CONTACT_POLE"
        )["verdict"]
        == "CONDITIONAL",
        "later_dalgebra_chain_rejected": next(
            claim for claim in all_claims if claim["id"] == "M3_DALGEBRA_CHAIN"
        )["verdict"]
        == "REJECTED",
        "later_vertex_momentum_magnitudes_proved": next(
            claim for claim in all_claims if claim["id"] == "M3_DALGEBRA_VERTEX_MOMENTA"
        )["verdict"]
        == "PROVED",
        "workflow_coefficient_rejected": next(
            claim for claim in all_claims if claim["id"] == "M7_EXPECTED_COEFFICIENT"
        )["verdict"]
        == "REJECTED",
        "weinberg_groups_present": len(ledger["weinberg_chapter_30"]["claim_groups"]) == 9,
        "superspace_groups_present": len(ledger["superspace_1001"]["claim_groups"]) == 6,
        "no_source_formula_adopted": ledger["accepted_project_formulas_from_sources"] == [],
    }


def contract_checks() -> dict[str, bool]:
    text = CONTRACT.read_text(encoding="utf-8")
    return {
        "scope_states_present": all(
            state in text
            for state in (
                "\\texttt{EVALUATED}",
                "\\texttt{EVALUATED\\_UV\\_METRIC\\_MISMATCH}",
                "\\texttt{SPECIFIED}",
            )
        ),
        "spin_frame_locked": "+\\equiv1" in text and "-\\equiv2" in text,
        "dred_split_locked": "\\widehat\\delta^{mn}+\\widetilde\\delta^{mn}" in text,
        "physical_euler_present": (
            "\\boldsymbol{\\mathfrak E}_{\\boldsymbol\\Xi,A}^{\\rm phys}" in text
        ),
        "sixteen_tree_table_present": "\\tag{5.35}" in text,
        "source_chronology_present": "\\tag{5.48}" in text,
        "source_rejected_conditional_split_present": (
            "conversation claimed complete }D" in text
            and "\\tag{5.49a}" in text
        ),
        "scope_split_present": all(
            scope in text
            for scope in (
                "5A. PERTURBATIVE_FF_DRED_SUPERGRAPHS",
                "5B. SD_COMPLETE_GRAPH_ORBIT",
                "5C. FINITE_BV_DENSITY_AND_CYCLES",
            )
        ),
        "multiplier_block_inverse_present": all(
            tag in text for tag in ("\\tag{5.45b}", "\\tag{5.45c}", "\\tag{5.45g}")
        ),
        "nonlocality_obstruction_derived": (
            "\\mathcal Y_{\\rm target}" in text
            and "violates the locality condition (3D.88a)" in text
        ),
        "measure_vertex_split_present": (
            "S_{\\rm measure}" in text and "\\tag{5.47a}" in text
        ),
        "reference_flat_matter_kernels_present": (
            "\\langle\\phi_r^A(p)\\widetilde\\phi_s^B(-p)\\rangle_{0,{\\rm ref}}"
            in text
            and "\\tag{5.47b}" in text
        ),
        "step5a_vector_wick_kernel_admitted": (
            "\\tag{5.45A}" in text
            and "is admitted on \\(p^2\\ne0\\)" in text
        ),
        "step5a_reference_flat_measure": (
            "\\mathfrak E_{\\mathsf p}^{\\rm measure}=0" in text
            and "\\tag{5.42A}" in text
        ),
        "seed_project_dalgebra_audit_present": all(
            tag in text for tag in ("\\tag{5.53a}", "\\tag{5.53i}", "\\tag{5.53j}")
        ),
        "seed_metric_mismatch_and_coefficient_present": all(
            tag in text for tag in ("\\tag{5.53x}", "\\tag{5.54}", "\\tag{5.54A}")
        ),
        "ordinary_triangle_bubble_cancellation_open": "\\tag{5.54B}" in text,
        "resolved_gaussian_blocker_absent": (
            "BLOCKED\\_EUCLIDEAN\\_GAUSSIAN\\_CYCLE\\_AND\\_SOURCE\\_ORDER"
            not in text
        ),
        "forbidden_approximation_tokens_absent": all(
            token not in text for token in ("\\sim", "\\approx", "\\propto")
        ),
    }


def main() -> None:
    channel_result, channels = channel_checks()
    sections = {
        "contract": contract_checks(),
        "spinor": spinor_checks(),
        "grassmann_operator": grassmann_checks(),
        "channels": channel_result,
        "sources": source_checks(),
    }
    checks = sum(len(section) for section in sections.values())
    failures = [
        f"{section}.{name}"
        for section, values in sections.items()
        for name, passed in values.items()
        if not passed
    ]
    audit = {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "source_ledger_sha256": hashlib.sha256(SOURCE_LEDGER.read_bytes()).hexdigest(),
        "status": "PASS" if not failures else "FAIL",
        "stage": "EVALUATED",
        "stage_qualifier": "WW_UV_METRIC_MISMATCH_DERIVED_ORDINARY_ORBIT_OPEN",
        "totals": {"checks": checks, "failed": len(failures)},
        "failures": failures,
        "sections": sections,
        "channel_ledger": channels,
    }
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(audit["totals"], sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
