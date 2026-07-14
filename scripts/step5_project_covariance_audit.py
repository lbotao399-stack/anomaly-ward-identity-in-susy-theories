#!/usr/bin/env python3
"""Independent Project-side covariance audit for the Step-5 kernel.

This program intentionally reads no holomorphic-twist reference and imports no
other Step-5 implementation.  It proves the finite Grassmann-algebra statements
that follow from diagonal odd-translation invariance, emits the conditional
weighted-superletter expansion, and records every Project-side statement that
cannot be proved from the locked inputs.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Dict, List, Mapping, MutableMapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits" / "step5-project-covariance-kernel.json"
MD_OUT = ROOT / "audits" / "step5-project-covariance-kernel.md"

AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
AUTHORITY_VERIFY_RUN = 29306335742

VARIABLES = ("theta_1", "theta_2", "theta_3", "theta'_1", "theta'_2", "theta'_3")
UNPRIMED = (0, 1, 2)
PRIMED = (3, 4, 5)


def popcount(mask: int) -> int:
    return mask.bit_count()


def masks_of_degree(n: int, degree: int) -> List[int]:
    return [m for m in range(1 << n) if popcount(m) == degree]


def mask_names(mask: int) -> List[str]:
    return [VARIABLES[i] for i in range(6) if mask & (1 << i)]


def monomial_text(mask: int) -> str:
    names = mask_names(mask)
    return "1" if not names else " ".join(names)


def exterior_multiply(left: int, right: int) -> Tuple[int, int] | None:
    if left & right:
        return None
    inversions = 0
    for i in range(6):
        if left & (1 << i):
            inversions += popcount(right & ((1 << i) - 1))
    return (-1 if inversions % 2 else 1, left | right)


def left_derivative(mask: int, variable: int) -> Tuple[int, int] | None:
    if not (mask & (1 << variable)):
        return None
    lower = popcount(mask & ((1 << variable) - 1))
    return (-1 if lower % 2 else 1, mask ^ (1 << variable))


Polynomial = Dict[int, Fraction]


def clean(poly: MutableMapping[int, Fraction]) -> Polynomial:
    return {m: c for m, c in sorted(poly.items()) if c}


def poly_multiply(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Polynomial:
    out: MutableMapping[int, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            product = exterior_multiply(lm, rm)
            if product is None:
                continue
            sign, mask = product
            out[mask] += lc * rc * sign
    return clean(out)


def diagonal_derivative(poly: Mapping[int, Fraction], flavor: int, sign: int = 1) -> Polynomial:
    out: MutableMapping[int, Fraction] = defaultdict(Fraction)
    for mask, coefficient in poly.items():
        for variable, slot_sign in ((flavor, 1), (flavor + 3, sign)):
            derived = left_derivative(mask, variable)
            if derived is None:
                continue
            koszul, target = derived
            out[target] += coefficient * slot_sign * koszul
    return clean(out)


def kernel_polynomial(relative_sign: int = -1) -> Polynomial:
    result: Polynomial = {0: Fraction(1)}
    for flavor in range(3):
        factor = {
            1 << flavor: Fraction(1),
            1 << (flavor + 3): Fraction(relative_sign),
        }
        result = poly_multiply(result, factor)
    return result


def rref(matrix: Sequence[Sequence[Fraction]]) -> Tuple[List[List[Fraction]], List[int]]:
    rows = [list(row) for row in matrix]
    if not rows:
        return rows, []
    nrows = len(rows)
    ncols = len(rows[0])
    pivot_columns: List[int] = []
    pivot_row = 0
    for col in range(ncols):
        selected = next((r for r in range(pivot_row, nrows) if rows[r][col]), None)
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        pivot = rows[pivot_row][col]
        rows[pivot_row] = [x / pivot for x in rows[pivot_row]]
        for r in range(nrows):
            if r == pivot_row or not rows[r][col]:
                continue
            factor = rows[r][col]
            rows[r] = [rows[r][c] - factor * rows[pivot_row][c] for c in range(ncols)]
        pivot_columns.append(col)
        pivot_row += 1
        if pivot_row == nrows:
            break
    return rows, pivot_columns


def nullspace(matrix: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    reduced, pivots = rref(matrix)
    ncols = len(matrix[0]) if matrix else 0
    free = [c for c in range(ncols) if c not in pivots]
    basis: List[List[Fraction]] = []
    for free_col in free:
        vector = [Fraction(0) for _ in range(ncols)]
        vector[free_col] = Fraction(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -reduced[row][free_col]
        basis.append(vector)
    return basis


def invariant_matrix(degree: int, derivative_sign: int = 1) -> Tuple[List[int], List[Tuple[int, int]], List[List[Fraction]]]:
    domain = masks_of_degree(6, degree)
    codomain = masks_of_degree(6, degree - 1) if degree else []
    rows = [(flavor, mask) for flavor in range(3) for mask in codomain]
    row_index = {row: index for index, row in enumerate(rows)}
    matrix = [[Fraction(0) for _ in domain] for _ in rows]
    for col, source in enumerate(domain):
        for flavor in range(3):
            for variable, slot_sign in ((flavor, 1), (flavor + 3, derivative_sign)):
                result = left_derivative(source, variable)
                if result is None:
                    continue
                sign, target = result
                matrix[row_index[(flavor, target)]][col] += sign * slot_sign
    return domain, rows, matrix


def vector_to_polynomial(domain: Sequence[int], vector: Sequence[Fraction]) -> Polynomial:
    return clean(defaultdict(Fraction, {mask: coefficient for mask, coefficient in zip(domain, vector)}))


def proportional(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Tuple[bool, Fraction | None]:
    support = sorted(set(left) | set(right))
    ratio: Fraction | None = None
    for mask in support:
        lc = left.get(mask, Fraction(0))
        rc = right.get(mask, Fraction(0))
        if not rc:
            if lc:
                return False, None
            continue
        current = lc / rc
        if ratio is None:
            ratio = current
        elif current != ratio:
            return False, None
    return True, ratio


def epsilon3(i: int, j: int, k: int) -> int:
    if len({i, j, k}) < 3:
        return 0
    inversions = int(i > j) + int(i > k) + int(j > k)
    return -1 if inversions % 2 else 1


COMPACT_COMPONENTS = (
    (0b000, "U", "a", 1),
    (0b001, "C_1", "b", 1),
    (0b010, "C_2", "b", 1),
    (0b100, "C_3", "b", 1),
    (0b110, "B_1", "c", 1),
    (0b101, "B_2", "c", -1),
    (0b011, "B_3", "c", 1),
    (0b111, "A", "d", 1),
)
COMPONENT_BY_MASK = {mask: (name, weight, sign) for mask, name, weight, sign in COMPACT_COMPONENTS}


def formal_ratio(numerator: Sequence[str], denominator: Sequence[str]) -> str:
    num = "*".join(numerator) if numerator else "1"
    den = "*".join(denominator) if denominator else "1"
    return num if den == "1" else f"({num})/({den})"


def compact_pair_expansion(kernel: Mapping[int, Fraction]) -> List[dict]:
    grouped: Dict[Tuple[int, int], List[dict]] = defaultdict(list)
    for input_left, left_name, left_weight, left_weight_sign in COMPACT_COMPONENTS:
        for input_right, right_name, right_weight, right_weight_sign in COMPACT_COMPONENTS:
            lhs_pbw = -1 if (popcount(input_left) * popcount(input_right)) % 2 else 1
            lhs_weight_sign = left_weight_sign * right_weight_sign * lhs_pbw
            for output_left, out_left_name, out_left_weight, out_left_weight_sign in COMPACT_COMPONENTS:
                for output_right, out_right_name, out_right_weight, out_right_weight_sign in COMPACT_COMPONENTS:
                    shifted_right = output_right << 3
                    output_theta = output_left | shifted_right
                    out_pbw = -1 if (popcount(output_left) * popcount(output_right)) % 2 else 1
                    out_weight_sign = out_left_weight_sign * out_right_weight_sign * out_pbw
                    for kernel_mask, kernel_coefficient in kernel.items():
                        product = exterior_multiply(kernel_mask, output_theta)
                        if product is None:
                            continue
                        exterior_sign, target_mask = product
                        target_left = target_mask & 0b111
                        target_right = (target_mask >> 3) & 0b111
                        if target_left != input_left or target_right != input_right:
                            continue
                        coefficient = kernel_coefficient * exterior_sign * out_weight_sign * lhs_weight_sign
                        if not coefficient:
                            continue
                        grouped[(input_left, input_right)].append(
                            {
                                "output_left": out_left_name,
                                "output_right": out_right_name,
                                "word": f"P({out_left_name})>P({out_right_name})",
                                "integer_sign": int(coefficient),
                                "weight_ratio": formal_ratio(
                                    [out_left_weight, out_right_weight],
                                    [left_weight, right_weight],
                                ),
                                "kernel_monomial": monomial_text(kernel_mask),
                            }
                        )
    ledger: List[dict] = []
    for left_mask, left_name, _, _ in COMPACT_COMPONENTS:
        for right_mask, right_name, _, _ in COMPACT_COMPONENTS:
            terms = sorted(
                grouped.get((left_mask, right_mask), []),
                key=lambda term: (term["output_left"], term["output_right"], term["kernel_monomial"]),
            )
            ledger.append(
                {
                    "input_left": left_name,
                    "input_right": right_name,
                    "ordered_input_word": f"{left_name}>{right_name}",
                    "state": "CONDITIONAL_WEIGHTED_COMPACT_ANSATZ" if terms else "CONDITIONAL_EXACT_ZERO",
                    "terms": terms,
                }
            )
    return ledger


def q_matrices(a: Fraction, b: Fraction, c: Fraction, d: Fraction) -> List[List[List[Fraction]]]:
    labels = [entry[1] for entry in COMPACT_COMPONENTS]
    index = {label: i for i, label in enumerate(labels)}
    matrices: List[List[List[Fraction]]] = []
    for r in range(1, 4):
        matrix = [[Fraction(0) for _ in labels] for _ in labels]
        matrix[index[f"C_{r}"]][index["U"]] = b / a
        for s in range(1, 4):
            for t in range(1, 4):
                eps = epsilon3(r, s, t)
                if eps:
                    matrix[index[f"B_{t}"]][index[f"C_{s}"]] = Fraction(eps) * c / b
            if r == s:
                matrix[index["A"]][index[f"B_{s}"]] = d / c
        matrices.append(matrix)
    return matrices


def matrix_multiply(left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    n = len(left)
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), Fraction(0)) for j in range(n)]
        for i in range(n)
    ]


def matrix_add(left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]) -> List[List[Fraction]]:
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def is_zero_matrix(matrix: Sequence[Sequence[Fraction]]) -> bool:
    return all(not entry for row in matrix for entry in row)


def q_algebra_holds(matrices: Sequence[Sequence[Sequence[Fraction]]]) -> bool:
    for r in range(3):
        for s in range(3):
            anti = matrix_add(matrix_multiply(matrices[r], matrices[s]), matrix_multiply(matrices[s], matrices[r]))
            if not is_zero_matrix(anti):
                return False
    return True


def physical_pair_ledger() -> List[dict]:
    letters = (
        "nabla_+W_+",
        "nabla_+Phi_1",
        "nabla_+Phi_2",
        "nabla_+Phi_3",
        "tildePhi_1",
        "tildePhi_2",
        "tildePhi_3",
        "tildeW_dot1",
        "tildeW_dot2",
    )
    return [
        {
            "left": left,
            "right": right,
            "ordered_word": f"{left}>{right}",
            "reversed_word": f"{right}>{left}",
            "state": "BLOCKED_TYPED_COMPONENT_MAP",
            "reason": "No locked Project map from the nine Step-5 component letters to the eight weighted compact slots and the holomorphic derivative operator exists.",
        }
        for left in letters
        for right in letters
    ]


def fraction_json(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_json(poly: Mapping[int, Fraction]) -> List[dict]:
    return [
        {"mask": mask, "monomial": monomial_text(mask), "coefficient": fraction_json(coefficient)}
        for mask, coefficient in sorted(poly.items())
    ]


def sha_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return sha256(payload).hexdigest()


def build_audit() -> dict:
    hilbert: Dict[str, int] = {}
    for degree in range(7):
        if degree == 0:
            hilbert[str(degree)] = 1
            continue
        _, _, matrix = invariant_matrix(degree)
        hilbert[str(degree)] = len(nullspace(matrix))

    domain3, rows3, matrix3 = invariant_matrix(3)
    null3 = nullspace(matrix3)
    derived_kernel = vector_to_polynomial(domain3, null3[0])
    expected_kernel = kernel_polynomial(-1)
    same_span, ratio = proportional(derived_kernel, expected_kernel)
    derivatives = {f"D_{r + 1}": poly_json(diagonal_derivative(expected_kernel, r)) for r in range(3)}

    compact_ledger = compact_pair_expansion(expected_kernel)
    physical_ledger = physical_pair_ledger()
    nonzero_compact = sum(bool(row["terms"]) for row in compact_ledger)
    zero_compact = len(compact_ledger) - nonzero_compact

    generic_q = q_matrices(Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    unit_q = q_matrices(Fraction(1), Fraction(1), Fraction(1), Fraction(1))
    mutated_q = [[list(row) for row in matrix] for matrix in generic_q]
    labels = [entry[1] for entry in COMPACT_COMPONENTS]
    mutated_q[0][labels.index("B_3")][labels.index("C_2")] *= -1

    plus_kernel = kernel_polynomial(+1)
    deleted_kernel = dict(expected_kernel)
    deleted_kernel.pop(next(iter(deleted_kernel)))
    conditional_digest_1 = sha_json(compact_ledger)
    conditional_digest_2 = sha_json(compact_pair_expansion(expected_kernel))

    tests = [
        {
            "id": "T01_DEGREE3_KERNEL_DIMENSION",
            "pass": len(domain3) == 20 and len(rows3) == 45 and len(null3) == 1,
            "observed": {"domain": len(domain3), "stacked_rows": len(rows3), "nullity": len(null3)},
        },
        {
            "id": "T02_KERNEL_EQUALS_PRODUCT_OF_DIFFERENCES",
            "pass": same_span and ratio is not None,
            "observed": {"same_span": same_span, "basis_to_product_ratio": fraction_json(ratio or Fraction(0))},
        },
        {
            "id": "T03_DIAGONAL_TRANSLATION_CLOSURE",
            "pass": all(not diagonal_derivative(expected_kernel, r) for r in range(3)),
            "observed": {f"D_{r + 1}_term_count": len(diagonal_derivative(expected_kernel, r)) for r in range(3)},
        },
        {
            "id": "T04_PLUS_MUTATION_DETECTED",
            "pass": any(diagonal_derivative(plus_kernel, r) for r in range(3)),
            "observed": {f"D_{r + 1}_term_count": len(diagonal_derivative(plus_kernel, r)) for r in range(3)},
        },
        {
            "id": "T05_TERM_DELETION_MUTATION_DETECTED",
            "pass": any(diagonal_derivative(deleted_kernel, r) for r in range(3)),
            "observed": {f"D_{r + 1}_term_count": len(diagonal_derivative(deleted_kernel, r)) for r in range(3)},
        },
        {
            "id": "T06_WEIGHTED_Q_ANTICOMMUTATOR",
            "pass": q_algebra_holds(generic_q),
            "observed": "a=2,b=3,c=5,d=7",
        },
        {
            "id": "T07_Q_INDEX_SIGN_MUTATION_DETECTED",
            "pass": not q_algebra_holds(mutated_q),
            "observed": "sign of q_1(C_2)->B_3 reversed",
        },
        {
            "id": "T08_COMPACT_ORDERED_PAIR_CENSUS",
            "pass": len(compact_ledger) == 64 and nonzero_compact + zero_compact == 64,
            "observed": {"total": len(compact_ledger), "conditional_nonzero": nonzero_compact, "conditional_zero": zero_compact},
        },
        {
            "id": "T09_PHYSICAL_ORDERED_PAIR_CENSUS",
            "pass": len(physical_ledger) == 81 and len({row["ordered_word"] for row in physical_ledger}) == 81,
            "observed": {"total": len(physical_ledger), "distinct_ordered_words": len({row["ordered_word"] for row in physical_ledger})},
        },
        {
            "id": "T10_REVERSED_WORDS_RETAINED",
            "pass": all(
                any(other["ordered_word"] == row["reversed_word"] for other in physical_ledger)
                for row in physical_ledger
            ),
            "observed": {"off_diagonal_directional_rows": sum(row["left"] != row["right"] for row in physical_ledger)},
        },
        {
            "id": "T11_DETERMINISTIC_EXPANSION",
            "pass": conditional_digest_1 == conditional_digest_2,
            "observed": conditional_digest_1,
        },
        {
            "id": "T12_NORMALIZATION_UNDERDETERMINATION_WITNESS",
            "pass": q_algebra_holds(unit_q) and q_algebra_holds(generic_q) and unit_q != generic_q,
            "observed": {
                "normalization_1": "(a,b,c,d)=(1,1,1,1)",
                "normalization_2": "(a,b,c,d)=(2,3,5,7)",
                "representations_are_distinct": unit_q != generic_q,
            },
        },
    ]

    blockers = [
        {
            "id": "BLOCKED_STEP5_LETTER_PROJECTIONS_ABSENT",
            "claim_blocked": "Normalized identification of U,C_r,B_r,A with the four Step-5 Project letter families.",
            "evidence": "The locked contracts define N=4 component fields and vector/chiral representations, while tasks/CURRENT.yaml only names nabla_+W_+, nabla_+Phi_r, tildePhi_r, tildeW_dot-a; it does not define their plus-spin-frame projections or compact-slot map.",
        },
        {
            "id": "BLOCKED_RESIDUAL_Q_SELECTION_AND_NORMALIZATION",
            "claim_blocked": "Physical q_r action and the numerical compact weights a,b,c,d.",
            "evidence": "Step 4C equations (4C.44)-(4C.47) provide all epsilon and tilde-epsilon transformations, but no locked input selects the three residual components q_r, their spinor slots, or their normalization after the Step-5 projection.",
        },
        {
            "id": "BLOCKED_TREE_EULER_TO_COMPACT_DESCENDANT_MAP",
            "claim_blocked": "Derivation of the compact weights from tree Euler descendants.",
            "evidence": "Step 4C equations (4C.68)-(4C.69a1) fix component Euler operators, but no locked input derives the specific Schwinger descendants of the four Step-5 letters or maps them to U,C_r,B_r,A and P_dot.",
        },
        {
            "id": "BLOCKED_DRED_CUT_OPERATOR_NOT_LOCKED",
            "claim_blocked": "Unconditional intertwining of the physical DRED-minus-cut commutator with q_r.",
            "evidence": "No allowed Project contract defines the DRED field continuation, regulated cut operator, or their action on the projected Step-5 letter complex.",
        },
        {
            "id": "BLOCKED_LOCAL_COHOMOLOGY_COMPLEX_NOT_LOCKED",
            "claim_blocked": "Uniqueness of the full local bilinear two-holomorphic-derivative cocycle.",
            "evidence": "Diagonal theta-translation invariance fixes the Grassmann polynomial, but the locked inputs do not specify the Step-5 local-operator space, color-tensor sector, derivative-weight restriction, BRST/EOM quotient, or admissible counterterm coboundaries.",
        },
    ]

    return {
        "schema": "step5-project-covariance-kernel-v1",
        "authority": {
            "commit": AUTHORITY_COMMIT,
            "verify_run": AUTHORITY_VERIFY_RUN,
            "verified": True,
            "project_inputs_only": True,
            "holomorphic_twist_read": False,
            "unmerged_step5_filesystem_read": False,
            "inputs": [
                "AUTHORITY.md",
                "AGENTS.md",
                "tasks/CURRENT.yaml",
                "contracts/foundations/step-01-supersymmetry-commutator.md",
                "contracts/foundations/step-02a-flat-superspace.md",
                "contracts/foundations/step-03a-gauge-chiral-action.md",
                "contracts/foundations/step-03b-component-reconstruction.md",
                "contracts/foundations/step-03c-gauge-vector-representation.md",
                "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
                "contracts/foundations/step-04-extended-sym-notation.md",
                "contracts/foundations/step-04a-n1-super-yang-mills.md",
                "contracts/foundations/step-04b-n2-super-yang-mills.md",
                "contracts/foundations/step-04c-n4-super-yang-mills.md",
            ],
        },
        "verdict": "BLOCKED_PROJECT_NORMALIZATION_AND_PHYSICAL_INTERTWINING",
        "proved": [
            "The degree-three diagonal odd-translation invariant subspace is one-dimensional.",
            "Its generator is exactly (theta_1-theta'_1)(theta_2-theta'_2)(theta_3-theta'_3).",
            "A weighted eight-slot compact superletter has the conditional q_r index map displayed in weighted_superletter.",
            "That conditional q_r representation satisfies q_r q_s+q_s q_r=0 for arbitrary nonzero weights.",
            "The conditional kernel expansion has 64 ordered compact input pairs and preserves output word order.",
            "The named physical alphabet has 81 ordered pairs and preserves both directions.",
        ],
        "not_proved": [blocker["claim_blocked"] for blocker in blockers],
        "grassmann_invariants": {
            "variable_order": list(VARIABLES),
            "diagonal_generators": ["D_r=left_d/dtheta_r+left_d/dtheta'_r" for _ in range(3)],
            "degree3_domain_dimension": len(domain3),
            "stacked_constraint_rows": len(rows3),
            "rank": len(domain3) - len(null3),
            "nullity": len(null3),
            "invariant_hilbert_dimensions_degrees_0_to_6": hilbert,
            "generator": poly_json(expected_kernel),
            "rref_basis": poly_json(derived_kernel),
            "rref_basis_to_generator_ratio": fraction_json(ratio or Fraction(0)),
            "derivatives": derivatives,
        },
        "weighted_superletter": {
            "definition": "C(theta)=a U+b theta_r C_r+(c/2) epsilon_rst theta_r theta_s B_t+d theta_1 theta_2 theta_3 A",
            "weights_required_nonzero": ["a", "b", "c", "d"],
            "conditional_action": [
                "q_r U=(b/a) C_r",
                "q_r C_s=(c/b) epsilon_rst B_t",
                "q_r B_s=(d/c) delta_rs A",
                "q_r A=0",
            ],
            "derivation": "Coefficient comparison in q_r C(theta)=left_d C(theta)/dtheta_r.",
            "normalization_status": "BLOCKED_RESIDUAL_Q_SELECTION_AND_NORMALIZATION",
            "underdetermination_witness": "Every nonzero quadruple (a,b,c,d) gives an isomorphic nilpotent exterior-algebra representation; nilpotency alone cannot select numerical weights.",
        },
        "conditional_intertwiner": {
            "ansatz": "Omega=kappa_color K(theta,theta') P C(theta) P C(theta')",
            "identity": "q_r Omega-Omega(q_r tensor 1+1 tensor q_r)=(D_r K) P C P C+K([q_r,P]C P C+P C [q_r,P]C)",
            "conditional_zero_if": [
                "q_r C(theta)=left_d C(theta)/dtheta_r",
                "D_r K=0",
                "[q_r,P]=0",
                "the color tensor is q_r-inert",
                "the regulator and cut are separately q_r-equivariant",
            ],
            "physical_status": "BLOCKED_DRED_CUT_OPERATOR_NOT_LOCKED",
        },
        "compact_64": compact_ledger,
        "compact_counts": {"total": 64, "conditional_nonzero": nonzero_compact, "conditional_zero": zero_compact},
        "physical_81": physical_ledger,
        "physical_counts": {"total": 81, "blocked": 81},
        "blockers": blockers,
        "mutation_tests": tests,
        "test_summary": {"passed": sum(test["pass"] for test in tests), "total": len(tests)},
    }


def markdown(audit: Mapping[str, object]) -> str:
    grassmann = audit["grassmann_invariants"]
    counts = audit["compact_counts"]
    blockers = audit["blockers"]
    tests = audit["mutation_tests"]
    generator_terms = []
    for term in grassmann["generator"]:
        coefficient = term["coefficient"]
        monomial = term["monomial"].replace("theta", r"\theta")
        generator_terms.append(f"{coefficient}\\,{monomial}")
    generator_expansion = " + ".join(generator_terms).replace("+ -", "- ")

    blocker_lines = "\n".join(
        f"- `{item['id']}`: {item['claim_blocked']} {item['evidence']}" for item in blockers
    )
    test_lines = "\n".join(
        f"- `{item['id']}`: {'PASS' if item['pass'] else 'FAIL'}; `{json.dumps(item['observed'], sort_keys=True)}`"
        for item in tests
    )
    compact_lines = []
    for row in audit["compact_64"]:
        if row["terms"]:
            rhs = " + ".join(
                f"{term['integer_sign']} {term['weight_ratio']} {term['word']}"
                for term in row["terms"]
            )
        else:
            rhs = "0"
        compact_lines.append(f"- `{row['ordered_input_word']}`: `{rhs}`")
    physical_lines = "\n".join(
        f"- `{row['ordered_word']}`: `{row['state']}`" for row in audit["physical_81"]
    )

    template = r"""# Step 5 Project covariance-kernel audit

Authority: `origin/main@__AUTHORITY_COMMIT__`, verify run `__AUTHORITY_VERIFY_RUN__`.  本 audit 只使用 locked Project inputs；没有读取 holomorphic-twist target，也没有读取任何 unmerged Step-5 derivation file.

## 1. Exact Grassmann calculation

令 exterior-variable order 为

$$
\theta_1<\theta_2<\theta_3<\theta'_1<\theta'_2<\theta'_3,
\qquad
D_r:=\frac{\vec\partial}{\partial\theta_r}
+\frac{\vec\partial}{\partial\theta'_r}.
$$

Degree-three space dimension 与 stacked constraint 为

$$
\dim\Lambda^3(K^6)=\binom63=20,
\qquad
(D_1,D_2,D_3):\Lambda^3(K^6)\longrightarrow
\Lambda^2(K^6)^{\oplus3}.
$$

Exact rational RREF gives

$$
\operatorname{rank}(D_1,D_2,D_3)=19,
\qquad
\dim\bigcap_{r=1}^3\ker D_r=20-19=1.
$$

Its generator is

$$
K(\theta,\theta')
=(\theta_1-\theta'_1)(\theta_2-\theta'_2)(\theta_3-\theta'_3),
$$

with fully normal-ordered expansion

$$
K=@@GENERATOR_EXPANSION@@.
$$

The exact program output is

$$
D_1K=D_2K=D_3K=0.
$$

All invariant dimensions are

$$
(\dim I^0,\ldots,\dim I^6)=(@@HILBERT_DIMENSIONS@@).
$$

因此 degree-three diagonal-translation invariant polynomial space 恰为

$$
\operatorname{Span}_{K}\!\left\{K(\theta,\theta')\right\}.
$$

## 2. Conditional weighted superletter algebra

不预设 numerical normalization，写

$$
\mathcal C(\theta)
=aU+b\theta_rC_r
+\frac c2\varepsilon_{rst}\theta_r\theta_sB_t
+d\theta_1\theta_2\theta_3A,
\qquad abcd\ne0.
$$

若 physical residual action 已另行证明满足

$$
q_r\mathcal C(\theta)
=\frac{\vec\partial}{\partial\theta_r}\mathcal C(\theta),
$$

then coefficient comparison gives

$$
q_rU=\frac baC_r,
\qquad
q_rC_s=\frac cb\varepsilon_{rst}B_t,
\qquad
q_rB_s=\frac dc\delta_{rs}A,
\qquad
q_rA=0.
$$

Hence

$$
\{q_r,q_s\}U
=\frac ca(\varepsilon_{srt}+\varepsilon_{rst})B_t=0,
$$

$$
\{q_r,q_s\}C_t
=\frac db(\varepsilon_{str}+\varepsilon_{rts})A=0,
$$

and the anticommutator vanishes on (B_t,A) directly.  This proves the abstract index/sign map for arbitrary (a,b,c,d\ne0); it does not select the Project normalization.

## 3. Conditional intertwiner

For

$$
\Omega(\mathcal C^A,\mathcal C^B)
=\kappa_{\rm color}^{AB}{}_{DE}
K(\theta,\theta')P\mathcal C^D(\theta)P\mathcal C^E(\theta'),
$$

direct graded Leibniz expansion gives

$$
\begin{aligned}
q_r\Omega-\Omega(q_r\otimes1+1\otimes q_r)
={}&\kappa_{\rm color}(D_rK)P\mathcal C\,P\mathcal C\\
&+\kappa_{\rm color}K
\left([q_r,P]\mathcal C\,P\mathcal C
+P\mathcal C\,[q_r,P]\mathcal C\right).
\end{aligned}
$$

Thus it vanishes exactly if (D_rK=0), ([q_r,P]=0), color is inert, and both regulated and cut maps are separately (q_r)-equivariant.  The first condition is proved above; the remaining physical conditions are not present in the locked inputs.

## 4. Ordered-pair census

The conditional weighted compact ansatz emits exactly

$$
64=8\times8,
\qquad
N_{\rm conditional\ nonzero}=@@CONDITIONAL_NONZERO@@,
\qquad
N_{\rm conditional\ zero}=@@CONDITIONAL_ZERO@@.
$$

Every coefficient below is a formal ratio of (a,b,c,d); no numerical value is inferred.

@@COMPACT_LINES@@

The named physical alphabet contains

$$
1+3+3+2=9,
\qquad 9\times9=81
$$

ordered pairs.  Reversed words are retained as different records:

@@PHYSICAL_LINES@@

## 5. Exact blockers

@@BLOCKER_LINES@@

Therefore the full Project cocycle uniqueness, numerical superletter normalization, physical (q_r) intertwining, and the 81 physical results are not proved by this audit.  The exact verdict is `@@VERDICT@@`.

## 6. Mutation tests

@@TEST_LINES@@
"""
    return (
        template.replace("__AUTHORITY_COMMIT__", AUTHORITY_COMMIT)
        .replace("__AUTHORITY_VERIFY_RUN__", str(AUTHORITY_VERIFY_RUN))
        .replace("@@GENERATOR_EXPANSION@@", generator_expansion)
        .replace(
            "@@HILBERT_DIMENSIONS@@",
            ",".join(
                str(grassmann["invariant_hilbert_dimensions_degrees_0_to_6"][str(i)])
                for i in range(7)
            ),
        )
        .replace("@@CONDITIONAL_NONZERO@@", str(counts["conditional_nonzero"]))
        .replace("@@CONDITIONAL_ZERO@@", str(counts["conditional_zero"]))
        .replace("@@COMPACT_LINES@@", "\n".join(compact_lines))
        .replace("@@PHYSICAL_LINES@@", physical_lines)
        .replace("@@BLOCKER_LINES@@", blocker_lines)
        .replace("@@VERDICT@@", str(audit["verdict"]))
        .replace("@@TEST_LINES@@", test_lines)
    )


def main() -> int:
    audit = build_audit()
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    MD_OUT.write_text(markdown(audit), encoding="utf-8")
    failed = [test["id"] for test in audit["mutation_tests"] if not test["pass"]]
    print(json.dumps({"verdict": audit["verdict"], "tests": audit["test_summary"], "failed": failed}, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
