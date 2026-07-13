#!/usr/bin/env python3
"""Exact fail-closed pure-gauge covariant-jet census for Step 5."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated/step5/one-loop-pure-gauge-covariant-jet-census.json"
AUDIT = ROOT / "audits/step5-one-loop-pure-gauge-covariant-jet-census-verification.json"

TARGET_DIMENSION_TWICE = 9
TARGET_R = -1
TARGET_PARITY = 1
TARGET_JL_TWICE = 3
TARGET_JR_TWICE = 0


@dataclass(frozen=True)
class JetRow:
    n_w: int
    n_wtilde: int
    n_nabla: int
    n_barnabla: int
    n_vector: int
    dimension_twice: int
    r_charge: int
    parity: int
    target_spin_multiplicity_free_ordered: int

    @property
    def field_strength_degree(self) -> int:
        return self.n_w + self.n_wtilde


def su2_tensor_multiplicities(twice_spins: Iterable[int]) -> dict[int, int]:
    """Return exact SU(2) multiplicities, keyed by twice-spin."""
    multiplicities = {0: 1}
    for spin in twice_spins:
        updated: defaultdict[int, int] = defaultdict(int)
        for old_spin, old_multiplicity in multiplicities.items():
            for new_spin in range(abs(old_spin - spin), old_spin + spin + 1, 2):
                updated[new_spin] += old_multiplicity
        multiplicities = dict(sorted(updated.items()))
    return multiplicities


def target_spin_multiplicity(
    n_w: int,
    n_wtilde: int,
    n_nabla: int,
    n_barnabla: int,
    n_vector: int,
) -> int:
    left_fundamentals = n_w + n_nabla + n_vector
    right_fundamentals = n_wtilde + n_barnabla + n_vector
    left = su2_tensor_multiplicities([1] * left_fundamentals)
    right = su2_tensor_multiplicities([1] * right_fundamentals)
    return left.get(TARGET_JL_TWICE, 0) * right.get(TARGET_JR_TWICE, 0)


def enumerate_jets() -> list[JetRow]:
    rows: list[JetRow] = []
    for n_w in range(4):
        for n_wtilde in range(4 - n_w):
            for n_nabla in range(TARGET_DIMENSION_TWICE + 1):
                for n_barnabla in range(TARGET_DIMENSION_TWICE + 1):
                    for n_vector in range(TARGET_DIMENSION_TWICE // 2 + 1):
                        dimension_twice = (
                            3 * (n_w + n_wtilde)
                            + n_nabla
                            + n_barnabla
                            + 2 * n_vector
                        )
                        r_charge = n_w - n_wtilde - n_nabla + n_barnabla
                        parity = (n_w + n_wtilde + n_nabla + n_barnabla) % 2
                        if (
                            dimension_twice != TARGET_DIMENSION_TWICE
                            or r_charge != TARGET_R
                            or parity != TARGET_PARITY
                        ):
                            continue
                        rows.append(
                            JetRow(
                                n_w=n_w,
                                n_wtilde=n_wtilde,
                                n_nabla=n_nabla,
                                n_barnabla=n_barnabla,
                                n_vector=n_vector,
                                dimension_twice=dimension_twice,
                                r_charge=r_charge,
                                parity=parity,
                                target_spin_multiplicity_free_ordered=target_spin_multiplicity(
                                    n_w,
                                    n_wtilde,
                                    n_nabla,
                                    n_barnabla,
                                    n_vector,
                                ),
                            )
                        )
    return sorted(
        rows,
        key=lambda row: (
            row.field_strength_degree,
            row.n_w,
            row.n_wtilde,
            row.n_nabla,
            row.n_barnabla,
            row.n_vector,
        ),
    )


def _add_expression(
    target: defaultdict[tuple[str, ...], int],
    source: dict[tuple[str, ...], int],
    factor: int,
) -> None:
    for word, coefficient in source.items():
        target[word] += factor * coefficient
        if target[word] == 0:
            del target[word]


def _reduce_chiral_word(word: tuple[str, ...]) -> dict[tuple[str, ...], int]:
    """Use B N_a = -N_a B - 2 D_(a dot) and B W = 0."""
    for position in range(len(word) - 1):
        left, right = word[position], word[position + 1]
        if left == "B:dot" and right.startswith("N:"):
            index = right.split(":", maxsplit=1)[1]
            swapped = word[:position] + (right, left) + word[position + 2 :]
            collapsed = word[:position] + (f"D:{index},dot",) + word[position + 2 :]
            result: defaultdict[tuple[str, ...], int] = defaultdict(int)
            _add_expression(result, _reduce_chiral_word(swapped), -1)
            _add_expression(result, _reduce_chiral_word(collapsed), -2)
            return dict(sorted(result.items()))
    if word and word[-1] == "B:dot":
        return {}
    return {word: 1}


def _reduce_antichiral_word(word: tuple[str, ...]) -> dict[tuple[str, ...], int]:
    """Use N_a B = -B N_a - 2 D_(a dot) and N_a Wtilde = 0."""
    for position in range(len(word) - 1):
        left, right = word[position], word[position + 1]
        if left.startswith("N:") and right == "B:dot":
            index = left.split(":", maxsplit=1)[1]
            swapped = word[:position] + (right, left) + word[position + 2 :]
            collapsed = word[:position] + (f"D:{index},dot",) + word[position + 2 :]
            result: defaultdict[tuple[str, ...], int] = defaultdict(int)
            _add_expression(result, _reduce_antichiral_word(swapped), -1)
            _add_expression(result, _reduce_antichiral_word(collapsed), -2)
            return dict(sorted(result.items()))
    if word and word[-1].startswith("N:"):
        return {}
    return {word: 1}


def mixed_derivative_reductions() -> dict[str, object]:
    permutations = sorted(set(itertools.permutations(("N:a", "N:b", "B:dot"))))

    def encoded(reducer: object) -> list[dict[str, object]]:
        output: list[dict[str, object]] = []
        for word in permutations:
            reduced = reducer(word)  # type: ignore[operator]
            output.append(
                {
                    "input": list(word),
                    "output": [
                        {"coefficient": coefficient, "word": list(term)}
                        for term, coefficient in sorted(reduced.items())
                    ],
                }
            )
        return output

    return {
        "euclidean_mixed_anticommutator": "{N_a,B_dot}=-2 D_(a dot)",
        "chiral_terminal_rule": "B_dot W_c=0",
        "antichiral_terminal_rule": "N_a Wtilde_dotc=0",
        "chiral_terminal_words": encoded(_reduce_chiral_word),
        "antichiral_terminal_words": encoded(_reduce_antichiral_word),
        "local_word_span_closes_on": ["one N", "one D"],
        "product_leibniz_ibp_completion_certified": False,
    }


def eom_pigeonhole_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    derivative_labels = ("a", "b", "d")
    for assignment in itertools.product((1, 2), repeat=3):
        blocks = {
            field: [
                derivative_labels[position]
                for position, assigned_field in enumerate(assignment)
                if assigned_field == field
            ]
            for field in (1, 2)
        }
        carrier = 1 if len(blocks[1]) >= 2 else 2
        carrier_block = blocks[carrier]
        pair = carrier_block[-2:]
        outer = carrier_block[:-2]
        if outer:
            replacement = (
                f"N_{outer[0]} N_{pair[0]} N_{pair[1]} W_c"
                f"=-epsilon_{{{pair[0]}{pair[1]}}} N_{outer[0]} N_c E"
            )
        else:
            replacement = (
                f"N_{pair[0]} N_{pair[1]} W_c"
                f"=-epsilon_{{{pair[0]}{pair[1]}}} N_c E"
            )
        rows.append(
            {
                "assignment": list(assignment),
                "W1_derivatives": blocks[1],
                "W2_derivatives": blocks[2],
                "eom_carrier": f"W{carrier}",
                "local_replacement": replacement,
                "local_differential_E_ideal_membership": True,
                "full_ordered_product_coefficient_certified": False,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    rows = enumerate_jets()
    rows_by_degree = {
        str(degree): [asdict(row) | {"field_strength_degree": degree} for row in rows if row.field_strength_degree == degree]
        for degree in range(4)
    }
    n2_rows = [row for row in rows if row.field_strength_degree == 2]
    n3_rows = [row for row in rows if row.field_strength_degree == 3]
    candidate = next(
        row
        for row in n2_rows
        if (
            row.n_w,
            row.n_wtilde,
            row.n_nabla,
            row.n_barnabla,
            row.n_vector,
        )
        == (1, 1, 1, 0, 1)
    )
    return {
        "schema": "STEP5_ONE_LOOP_PURE_GAUGE_COVARIANT_JET_CENSUS_V1",
        "status": "FAIL_CLOSED_PARTIAL_REDUCTION",
        "target": {
            "dimension": "9/2",
            "dimension_twice": TARGET_DIMENSION_TWICE,
            "r_charge": TARGET_R,
            "parity": "odd",
            "spin": {"jL_twice": TARGET_JL_TWICE, "jR_twice": TARGET_JR_TWICE},
            "open_color_carrier": "ORDERED_ADJ_AB_UNRESOLVED",
            "quadratic_filtration": "field-strength degree N>=2",
        },
        "r_grading": {
            "status": "TEMPORARY_FORMAL_DEFINITION",
            "definition": "r_f(W,Wtilde,N,B,D)=(+1,-1,-1,+1,0)",
            "project_U1R_binding_certified": False,
        },
        "letters": {
            "W": {"dimension_twice": 3, "r": 1, "parity": 1, "spin_twice": [1, 0]},
            "Wtilde": {"dimension_twice": 3, "r": -1, "parity": 1, "spin_twice": [0, 1]},
            "N": {"dimension_twice": 1, "r": -1, "parity": 1, "spin_twice": [1, 0]},
            "B": {"dimension_twice": 1, "r": 1, "parity": 1, "spin_twice": [0, 1]},
            "D": {"dimension_twice": 2, "r": 0, "parity": 0, "spin_twice": [1, 1]},
        },
        "diophantine_system": {
            "dimension": "3(n_W+n_Wtilde)+n_N+n_B+2n_D=9",
            "r_charge": "n_W-n_Wtilde-n_N+n_B=-1",
            "parity": "n_W+n_Wtilde+n_N+n_B=1 mod 2",
            "solution_count": len(rows),
        },
        "solutions_by_field_strength_degree": rows_by_degree,
        "dimension_exclusion": {
            "N_ge_4_minimum_dimension_twice": 12,
            "target_dimension_twice": 9,
            "excluded": True,
        },
        "quadratic_filtration_boundary": {
            "N_0_and_N_1_are_outside_filtered_sector": True,
            "N_0_and_N_1_global_absence_proved": False,
        },
        "N3_proof": {
            "solution_count": len(n3_rows),
            "unique_content": "W Wtilde Wtilde",
            "free_ordered_target_spin_multiplicity": n3_rows[0].target_spin_multiplicity_free_ordered,
            "excluded_from_target_spin": n3_rows[0].target_spin_multiplicity_free_ordered == 0,
        },
        "N2_rows": [asdict(row) for row in n2_rows],
        "candidate_spin_proof": {
            "content": "W Wtilde N D",
            "left_decomposition": "(1/2) tensor (1/2) tensor (1/2) = (3/2) + 2(1/2)",
            "right_decomposition": "(1/2) tensor (1/2) = 0 + 1",
            "target_multiplicity": candidate.target_spin_multiplicity_free_ordered,
        },
        "mixed_derivative_reduction": mixed_derivative_reductions(),
        "WW_N3_eom_reduction": {
            "spinor_pair_identity": "N_a N_b W_c=(1/2)epsilon_ab N^2 W_c=-epsilon_ab N_c E",
            "eom_identity": "N_c E=-(1/2)N^2 W_c",
            "labeled_distributions": eom_pigeonhole_rows(),
            "local_block_E_ideal_membership_certified": True,
            "global_ordered_ibp_E_ideal_membership_certified": False,
        },
        "rank_statement": {
            "candidate_free_ordered_spin_multiplicity_is_one": candidate.target_spin_multiplicity_free_ordered == 1,
            "rank_one_is_only_a_post_quotient_candidate": True,
            "conditional_rank_one_theorem_certified": False,
            "full_local_cohomology_rank_one_certified": False,
        },
        "open_gates": [
            "DERIVATIVE_PLACEMENT_AND_GRADED_LEIBNIZ",
            "COVARIANT_IBP_WITH_OPERATOR_ORDER",
            "DERIVATIVE_COMMUTATOR_CURVATURE_CHILDREN",
            "ORDERED_ADJ_AB_COLOR_RELATIONS",
            "DRED_EVANESCENT_OPERATORS",
            "SOURCE_PARTNER_AND_BRST_RELATIONS",
            "PROJECT_R_WEIGHT_BINDING",
        ],
    }


def build_audit(payload: dict[str, object]) -> dict[str, object]:
    rows = enumerate_jets()
    n2 = [row for row in rows if row.field_strength_degree == 2]
    n3 = [row for row in rows if row.field_strength_degree == 3]
    expected_n2 = {
        (2, 0, 3, 0, 0): 4,
        (1, 1, 2, 1, 0): 1,
        (1, 1, 1, 0, 1): 1,
        (0, 2, 1, 2, 0): 0,
        (0, 2, 0, 1, 1): 0,
    }
    actual_n2 = {
        (row.n_w, row.n_wtilde, row.n_nabla, row.n_barnabla, row.n_vector): row.target_spin_multiplicity_free_ordered
        for row in n2
    }
    mixed = payload["mixed_derivative_reduction"]
    assert isinstance(mixed, dict)
    reduced_rows = mixed["chiral_terminal_words"] + mixed["antichiral_terminal_words"]  # type: ignore[operator]
    only_nd = all(
        all(
            all(token.startswith(("N:", "D:")) for token in term["word"])
            for term in row["output"]
        )
        for row in reduced_rows
    )
    eom_rows = payload["WW_N3_eom_reduction"]
    assert isinstance(eom_rows, dict)
    labeled = eom_rows["labeled_distributions"]
    checks = {
        "complete_diophantine_solution_count_18": len(rows) == 18,
        "all_rows_satisfy_target_equations": all(
            row.dimension_twice == 9 and row.r_charge == -1 and row.parity == 1 for row in rows
        ),
        "N_ge_4_dimension_excluded": 3 * 4 > 9,
        "N3_unique_W_Wtilde_Wtilde": len(n3) == 1
        and (n3[0].n_w, n3[0].n_wtilde) == (1, 2),
        "N3_target_spin_multiplicity_zero": len(n3) == 1
        and n3[0].target_spin_multiplicity_free_ordered == 0,
        "N2_multiset_and_spin_table_exact": actual_n2 == expected_n2,
        "candidate_target_spin_multiplicity_one": actual_n2[(1, 1, 1, 0, 1)] == 1,
        "mixed_terminal_words_reduce_to_ND_or_zero": only_nd,
        "eight_labeled_WW_N3_distributions_have_E_carrier": len(labeled) == 8
        and all(row["local_differential_E_ideal_membership"] for row in labeled),
        "full_rank_one_claim_fail_closed": payload["rank_statement"]["full_local_cohomology_rank_one_certified"] is False,  # type: ignore[index]
        "project_R_weight_binding_fail_closed": payload["r_grading"]["project_U1R_binding_certified"] is False,  # type: ignore[index]
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return {
        "schema": "STEP5_ONE_LOOP_PURE_GAUGE_COVARIANT_JET_CENSUS_AUDIT_V1",
        "status": "PASS_EXACT_PARTIAL_FAIL_CLOSED",
        "payload_sha256": hashlib.sha256(canonical).hexdigest(),
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
    }


def main() -> None:
    payload = build_payload()
    audit = build_audit(payload)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(OUT), "audit": audit}, sort_keys=True))


if __name__ == "__main__":
    main()
