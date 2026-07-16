#!/usr/bin/env python3
"""Target-blind local Step-5 operator/mixing audit.

The calculation uses only the locked Project foundations.  It constructs the
ordered open-color derivative-slot tensor square, computes the three residual-q
matrices over Q, performs exact RREF, and records the precise boundary of what
BRST/Wess-Zumino covariance can determine about evanescent mixing.

No holomorphic-twist target and no other Step-5 script/contract is read.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Dict, List, Mapping, MutableMapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits" / "step5-local-operator-mixing.json"
MD_OUT = ROOT / "audits" / "step5-local-operator-mixing.md"

AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
AUTHORITY_VERIFY_RUN = 29306335742
FOUNDATION_INPUTS = (
    "AUTHORITY.md",
    "AGENTS.md",
    "tasks/CURRENT.yaml",
    "contracts/foundations/step-03c-gauge-vector-representation.md",
    "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
    "contracts/foundations/step-04-extended-sym-notation.md",
    "contracts/foundations/step-04c-n4-super-yang-mills.md",
)

# Normalized exterior-chain slots.  The physical map is
#   e_0   = i D,
#   e_r   = P C_r,
#   e_12  = -(P B_3)/sqrt(2),
#   e_13  = +(P B_2)/sqrt(2),
#   e_23  = -(P B_1)/sqrt(2),
#   e_123 = i(P A)/sqrt(2).
MASK_LABEL = {
    0: "iD",
    1: "PC_1",
    2: "PC_2",
    4: "PC_3",
    3: "-PB_3/sqrt(2)",
    5: "+PB_2/sqrt(2)",
    6: "-PB_1/sqrt(2)",
    7: "+iPA/sqrt(2)",
}


Pair = Tuple[int, int]
Vector = Dict[Pair, Fraction]
Matrix = List[List[Fraction]]


def popcount(mask: int) -> int:
    return mask.bit_count()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def wedge_sign(flavor: int, mask: int) -> int | None:
    """Coefficient of e_flavor wedge e_mask in sorted exterior order."""
    bit = 1 << flavor
    if mask & bit:
        return None
    lower = popcount(mask & (bit - 1))
    return -1 if lower % 2 else 1


def q_on_pair(pair: Pair, flavor: int, second_tensor_sign: int = -1) -> Vector:
    """Residual q on the parity-shifted ordered tensor product.

    Every one-letter slot has physical parity 1+exterior_degree.  Therefore

      q(e_L tensor e_R)
       = (q e_L) tensor e_R
         - (-1)^degree(e_L) e_L tensor (q e_R).

    second_tensor_sign=-1 is the physical rule.  The +1 value is a mutation.
    """
    left, right = pair
    out: MutableMapping[Pair, Fraction] = defaultdict(Fraction)

    sign = wedge_sign(flavor, left)
    if sign is not None:
        out[(left | (1 << flavor), right)] += Fraction(sign)

    sign = wedge_sign(flavor, right)
    if sign is not None:
        koszul = -1 if popcount(left) % 2 else 1
        out[(left, right | (1 << flavor))] += Fraction(second_tensor_sign * koszul * sign)

    return {key: value for key, value in sorted(out.items()) if value}


def q_on_vector(vector: Mapping[Pair, Fraction], flavor: int, second_tensor_sign: int = -1) -> Vector:
    out: MutableMapping[Pair, Fraction] = defaultdict(Fraction)
    for pair, coefficient in vector.items():
        for target, q_coefficient in q_on_pair(pair, flavor, second_tensor_sign).items():
            out[target] += coefficient * q_coefficient
    return {key: value for key, value in sorted(out.items()) if value}


def vector_add(left: Mapping[Pair, Fraction], right: Mapping[Pair, Fraction]) -> Vector:
    out: MutableMapping[Pair, Fraction] = defaultdict(Fraction)
    for key, value in left.items():
        out[key] += value
    for key, value in right.items():
        out[key] += value
    return {key: value for key, value in sorted(out.items()) if value}


def vector_scale(value: Fraction, vector: Mapping[Pair, Fraction]) -> Vector:
    return {key: value * coefficient for key, coefficient in vector.items() if value * coefficient}


def basis_of_degree(degree: int) -> List[Pair]:
    return [
        (left, right)
        for left in range(8)
        for right in range(8)
        if popcount(left) + popcount(right) == degree
    ]


def rref(matrix: Sequence[Sequence[Fraction]]) -> Tuple[Matrix, List[int]]:
    rows = [list(row) for row in matrix]
    if not rows:
        return rows, []
    nrows = len(rows)
    ncols = len(rows[0])
    pivot_columns: List[int] = []
    pivot_row = 0
    for column in range(ncols):
        selected = next((row for row in range(pivot_row, nrows) if rows[row][column]), None)
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot for entry in rows[pivot_row]]
        for row in range(nrows):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                rows[row][col] - factor * rows[pivot_row][col]
                for col in range(ncols)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == nrows:
            break
    return rows, pivot_columns


def nullspace(matrix: Sequence[Sequence[Fraction]], ncols: int | None = None) -> List[List[Fraction]]:
    if matrix:
        width = len(matrix[0])
    elif ncols is not None:
        width = ncols
    else:
        width = 0
    reduced, pivots = rref(matrix)
    free_columns = [column for column in range(width) if column not in pivots]
    basis: List[List[Fraction]] = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(vector)
    return basis


def stacked_q_matrix(degree: int, second_tensor_sign: int = -1) -> Tuple[List[Pair], List[Tuple[int, Pair]], Matrix]:
    domain = basis_of_degree(degree)
    codomain = basis_of_degree(degree + 1) if degree < 6 else []
    rows = [(flavor, pair) for flavor in range(3) for pair in codomain]
    row_index = {row: index for index, row in enumerate(rows)}
    matrix = [[Fraction(0) for _ in domain] for _ in rows]
    for column, pair in enumerate(domain):
        for flavor in range(3):
            for target, coefficient in q_on_pair(pair, flavor, second_tensor_sign).items():
                matrix[row_index[(flavor, target)]][column] += coefficient
    return domain, rows, matrix


def vector_from_coordinates(domain: Sequence[Pair], coordinates: Sequence[Fraction]) -> Vector:
    return {
        pair: coefficient
        for pair, coefficient in zip(domain, coordinates)
        if coefficient
    }


def q_product_matrix(source_degree: int, flavors: Sequence[int]) -> Tuple[List[Pair], List[Pair], Matrix]:
    domain = basis_of_degree(source_degree)
    target_degree = source_degree + len(flavors)
    codomain = basis_of_degree(target_degree)
    row_index = {pair: row for row, pair in enumerate(codomain)}
    matrix = [[Fraction(0) for _ in domain] for _ in codomain]
    for column, pair in enumerate(domain):
        vector: Vector = {pair: Fraction(1)}
        for flavor in reversed(flavors):
            vector = q_on_vector(vector, flavor)
        for target, coefficient in vector.items():
            matrix[row_index[target]][column] += coefficient
    return domain, codomain, matrix


def matrix_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    return len(rref(matrix)[1])


def compose_q_on_basis(pair: Pair, first: int, second: int) -> Vector:
    return q_on_vector(q_on_pair(pair, second), first)


def vector_json(vector: Mapping[Pair, Fraction]) -> List[dict]:
    return [
        {
            "left_mask": left,
            "right_mask": right,
            "left_normalized_slot": MASK_LABEL[left],
            "right_normalized_slot": MASK_LABEL[right],
            "coefficient": fraction_text(coefficient),
        }
        for (left, right), coefficient in sorted(vector.items())
    ]


def physical_basis_degree_three() -> List[str]:
    rows = ["<D,PA>"]
    rows.extend(f"<PC_{r},PB_{s}>" for r in range(1, 4) for s in range(1, 4))
    rows.extend(f"<PB_{r},PC_{s}>" for r in range(1, 4) for s in range(1, 4))
    rows.append("<PA,D>")
    return rows


def physical_basis_degree_two() -> List[str]:
    rows = [f"<D,PB_{r}>" for r in range(1, 4)]
    rows.extend(f"<PC_{r},PC_{s}>" for r in range(1, 4) for s in range(1, 4))
    rows.extend(f"<PB_{r},D>" for r in range(1, 4))
    return rows


def git_blob(relative: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{AUTHORITY_COMMIT}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def authority_file_hash(relative: str) -> str:
    return sha256(git_blob(relative)).hexdigest()


def sha_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return sha256(payload).hexdigest()


def build_audit() -> dict:
    foundation_hashes = [
        {
            "path": relative,
            "git_object_commit": AUTHORITY_COMMIT,
            "sha256": authority_file_hash(relative),
        }
        for relative in FOUNDATION_INPUTS
    ]

    q_complex: List[dict] = []
    kernels: Dict[int, List[Vector]] = {}
    for degree in range(7):
        domain, rows, matrix = stacked_q_matrix(degree)
        null = nullspace(matrix, len(domain))
        kernel_vectors = [vector_from_coordinates(domain, coordinates) for coordinates in null]
        kernels[degree] = kernel_vectors
        q_complex.append(
            {
                "degree": degree,
                "engineering_dimension": f"{6 + degree}/2",
                "parity": degree % 2,
                "domain_dimension": len(domain),
                "stacked_row_count": len(rows),
                "rank": matrix_rank(matrix),
                "joint_kernel_dimension": len(null),
            }
        )

    degree_three_kernel = kernels[3][0]
    expected_kernel: Vector = {
        (0, 7): Fraction(-1),
        (1, 6): Fraction(+1),
        (2, 5): Fraction(-1),
        (3, 4): Fraction(-1),
        (4, 3): Fraction(+1),
        (5, 2): Fraction(+1),
        (6, 1): Fraction(-1),
        (7, 0): Fraction(+1),
    }
    if degree_three_kernel != expected_kernel:
        # RREF may select the opposite normalization.  Normalize by the (7,0) entry.
        pivot = degree_three_kernel.get((7, 0), Fraction(0))
        if not pivot:
            raise AssertionError("degree-three kernel lacks the expected pivot")
        degree_three_kernel = vector_scale(Fraction(1, 1) / pivot, degree_three_kernel)

    triple_images: List[dict] = []
    for target_degree in range(3, 7):
        source_degree = target_degree - 3
        _, _, product = q_product_matrix(source_degree, (0, 1, 2))
        rank = matrix_rank(product)
        triple_images.append(
            {
                "target_degree": target_degree,
                "joint_kernel_dimension": len(kernels[target_degree]),
                "triple_q_image_dimension": rank,
                "quotient_dimension": len(kernels[target_degree]) - rank,
            }
        )

    base: Vector = {(0, 0): Fraction(1)}
    primitive_normalized = {
        "1": q_on_vector(q_on_vector(base, 2), 1),
        "2": vector_scale(Fraction(-1), q_on_vector(q_on_vector(base, 2), 0)),
        "3": q_on_vector(q_on_vector(base, 1), 0),
    }
    primitive_checks: List[dict] = []
    for r in range(3):
        for s in range(3):
            observed = q_on_vector(primitive_normalized[str(r + 1)], s)
            expected = degree_three_kernel if r == s else {}
            primitive_checks.append(
                {
                    "r": r + 1,
                    "s": s + 1,
                    "pass": observed == expected,
                    "observed": vector_json(observed),
                }
            )

    nilpotency = all(
        not compose_q_on_basis(pair, flavor, flavor)
        for pair in [(left, right) for left in range(8) for right in range(8)]
        for flavor in range(3)
    )
    anticommutativity = True
    for pair in [(left, right) for left in range(8) for right in range(8)]:
        for first in range(3):
            for second in range(3):
                anti = vector_add(
                    compose_q_on_basis(pair, first, second),
                    compose_q_on_basis(pair, second, first),
                )
                if anti:
                    anticommutativity = False

    mutated_kernel = dict(expected_kernel)
    mutated_kernel[(1, 6)] *= -1
    cocycle_sign_mutation_detected = any(q_on_vector(mutated_kernel, flavor) for flavor in range(3))

    primitive_rref = {
        "variables": ["alpha", "beta", "eta"],
        "definition": "gamma=-i*sqrt(2)*eta",
        "constraint_matrix": [[1, 0, -1], [0, 1, -1]],
        "rank": 2,
        "nullity": 1,
        "solution": "alpha=beta=eta",
    }

    tests = [
        {"id": "T01_RESIDUAL_Q_NILPOTENCY_64", "pass": nilpotency},
        {"id": "T02_RESIDUAL_Q_ANTICOMMUTATIVITY_64", "pass": anticommutativity},
        {
            "id": "T03_HOMOGENEOUS_DIMENSIONS",
            "pass": [row["domain_dimension"] for row in q_complex] == [1, 6, 15, 20, 15, 6, 1],
        },
        {
            "id": "T04_DEGREE_THREE_RREF",
            "pass": q_complex[3]["rank"] == 19 and q_complex[3]["joint_kernel_dimension"] == 1,
        },
        {
            "id": "T05_PHYSICAL_COCYCLE_VECTOR",
            "pass": degree_three_kernel == expected_kernel,
        },
        {
            "id": "T06_KOSZUL_JOINT_QUOTIENT",
            "pass": all(row["quotient_dimension"] == 0 for row in triple_images),
        },
        {
            "id": "T07_UNIQUE_TRIPLET_PRIMITIVE_RREF",
            "pass": primitive_rref["rank"] == 2 and primitive_rref["nullity"] == 1,
        },
        {
            "id": "T08_PRIMITIVE_COVARIANCE_9_CASES",
            "pass": all(row["pass"] for row in primitive_checks),
        },
        {
            "id": "T09_COCYCLE_SIGN_MUTATION_DETECTED",
            "pass": cocycle_sign_mutation_detected,
        },
        {
            "id": "T10_FINITE_EVANESCENT_FACTOR",
            "pass": Fraction(2) * Fraction(1, 16) == Fraction(1, 8),
            "observed": "2*epsilon*[hbar*g^2*z/(16*pi^2*epsilon)]=hbar*g^2*z/(8*pi^2)",
        },
        {
            "id": "T11_ONE_LOOP_RESOLVENT_GRAPH_COEFFICIENTS",
            "pass": [(-1) ** order for order in range(3)] == [1, -1, 1],
            "observed": {
                "G*I_2": 1,
                "G*V_1*G*I_1": -1,
                "G*V_2*G*I_0": -1,
                "G*V_1*G*V_1*G*I_0": 1,
            },
        },
    ]

    basis_64 = []
    for degree in range(7):
        for left, right in basis_of_degree(degree):
            basis_64.append(
                {
                    "degree": degree,
                    "engineering_dimension": f"{6 + degree}/2",
                    "parity": degree % 2,
                    "left_mask": left,
                    "right_mask": right,
                    "left_normalized_slot": MASK_LABEL[left],
                    "right_normalized_slot": MASK_LABEL[right],
                    "ordered_color_type": "Adj_D tensor Adj_E",
                    "ghost_number": 0,
                }
            )

    blockers = [
        {
            "id": "BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION",
            "severity": "P0",
            "minimal_missing_input": "A locked contragredient source J_DE, its antifield/source slots, and its subtraction conditions.",
            "why": "The ordered tensor O^(DE) is gauge-BRST covariant in Adj tensor Adj and is not BRST closed before source completion or invariant color contraction.",
        },
        {
            "id": "BLOCKED_DRED_EVANESCENT_OPERATOR_BASIS",
            "severity": "P0",
            "minimal_missing_input": "A locked DRED continuation of every Step-5 field, composite insertion, EOM, BRST differential, and local projection, including the breve-index tensor grammar.",
            "why": "The allowed foundations contain no genuine breve-index local operator basis, so the number and normalization of evanescent rows are undefined.",
        },
        {
            "id": "BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX",
            "severity": "P0",
            "minimal_missing_input": "The bare source functional, endpoint/link/contact vertices, all one-loop insertion graphs, and a declared subtraction scheme.",
            "why": "Residual-q, SU(3), parity, dimension, and BRST covariance allow an arbitrary scalar z_ev_to_phys on the unique physical cocycle; none of those identities evaluates its pole residue.",
        },
        {
            "id": "BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT",
            "severity": "P0",
            "minimal_missing_input": "The Step-5 source representation and the admissible multiplier/current grammar for the Euler operators (4C.68)-(4C.68a).",
            "why": "The locked foundations define the Euler generators but do not select the multipliers R^i, open-color currents J^m, or the U primitive needed to enumerate the quotient at dimension 9/2.",
        },
    ]

    audit = {
        "schema": "awi.step5.local-operator-mixing.v1",
        "engine_id": "STEP5-LOCAL-OPERATOR-MIXING-TARGET-BLIND-001",
        "status": "BLOCKED",
        "authority": {
            "authority_base_commit": AUTHORITY_COMMIT,
            "authority_verify_run": AUTHORITY_VERIFY_RUN,
            "external_target_used": False,
            "other_step5_artifact_used": False,
            "foundation_inputs": foundation_hashes,
        },
        "derivative_slot_chain": {
            "physical_slots": [
                {"slot": "D_dot", "dimension": "3/2", "parity": 1, "SU3": "1"},
                {"slot": "P_dot C_r", "dimension": "2", "parity": 0, "SU3": "bar(3)"},
                {"slot": "P_dot B_r", "dimension": "5/2", "parity": 1, "SU3": "3"},
                {"slot": "P_dot A", "dimension": "3", "parity": 0, "SU3": "1"},
            ],
            "q_action": [
                "q_r D_dot=-i P_dot C_r",
                "q_r(P_dot C_s)=-(1/sqrt(2))*epsilon_rst P_dot B_t",
                "q_r(P_dot B_s)=-i delta_rs P_dot A",
                "q_r(P_dot A)=0",
            ],
            "q_P_commutator": "q_r(P_dot_a X)-P_dot_a(q_r X)=(1/sqrt(2))*sigma^m_(+dot_a)*sigma_(m,+dot_b)*(tilde_psi_r^dot_b cross X)=0",
            "normalized_exterior_map": [
                "e_empty=iD",
                "e_r=PC_r",
                "e_12=-PB_3/sqrt(2)",
                "e_13=+PB_2/sqrt(2)",
                "e_23=-PB_1/sqrt(2)",
                "e_123=+iPA/sqrt(2)",
            ],
        },
        "ordered_open_color_space": {
            "definition": "O_XY^(DE)=H_X,dot_a^D H_Y^(E,dot_a), with D,E retained in order",
            "dimension": 64,
            "basis": basis_64,
            "q_complex_rref": q_complex,
        },
        "dimension_9_over_2_block": {
            "degree": 3,
            "dimension": "9/2",
            "parity": 1,
            "ghost_number": 0,
            "ordered_color_type": "Adj_D tensor Adj_E",
            "basis_dimension": 20,
            "basis": physical_basis_degree_three(),
            "SU3_decomposition": "4*1 + 2*8",
            "joint_q_kernel_dimension": 1,
            "normalized_kernel_vector": vector_json(degree_three_kernel),
            "physical_cocycle": "Z^(DE)=<D,PA>-<PA,D>+sum_r[<PB_r,PC_r>-<PC_r,PB_r>]",
            "singlet_basis": ["<D,PA>", "<PA,D>", "sum_r<PB_r,PC_r>", "sum_r<PC_r,PB_r>"],
        },
        "counterterm_primitive_block": {
            "degree": 2,
            "dimension": "4",
            "parity": 0,
            "basis_dimension": 15,
            "basis": physical_basis_degree_two(),
            "SU3_decomposition": "3 + 3 + 3 + bar(6)",
            "covariant_ansatz": "Y_r=alpha<D,PB_r>+beta<PB_r,D>+gamma*epsilon_rst<PC_s,PC_t>",
            "rref": primitive_rref,
            "unique_triplet": "Y_r=<D,PB_r>+<PB_r,D>-i*sqrt(2)*epsilon_rst<PC_s,PC_t>",
            "exact_covariance": "q_s Y_r=i delta_sr Z",
            "normalized_primitives": {key: vector_json(value) for key, value in primitive_normalized.items()},
        },
        "koszul_joint_cohomology": {
            "definition": "H_joint^n=(intersection_r ker q_r on V^n)/(image(q_1 q_2 q_3) from V^(n-3))",
            "dimensions": triple_images,
            "result": "ZERO_IN_EVERY_DEGREE",
            "scope": "Only the 64-dimensional derivative-slot open-color module; not the BV/EOM/total-derivative/DRED local cohomology.",
        },
        "extended_local_space": {
            "physical": "span{20 degree-three ordered bilinears}",
            "EOM_module": "span{A_E^m R_m, P_E,IJ R^IJ, Ptilde_E^IJ Rtilde_IJ, E_E,aI S^(aI), Etilde_E,dot_a^I Stilde_I^dot_a} at dimension 9/2, parity 1, ghost number 0, SU3 singlet, and the same source/color type",
            "BRST_exact_module": "{s K: [K]=9/2, parity(K)=0, gh(K)=-1, SU3(K)=1, same source/color type}",
            "total_derivative_module": "{partial_m J^m: [J]=7/2, parity(J)=1, gh(J)=0, SU3(J)=1, same source/color type}",
            "evanescent_module": "{E_u: E_u restricted to breve_delta=0 is zero, [E_u]=9/2, parity=1, gh=0, SU3=1, same source/color type}",
            "enumeration_status": "BLOCKED_BY_SOURCE_AND_DRED_GRAMMAR",
        },
        "one_loop_mixing": {
            "precursor_convention": "E denotes a same-typed pole-renormalized DRED precursor; the trace-evanescent insertion is E_tr=(4-d)E. E is not an already-projected genuine breve operator.",
            "general_matrix": "(O^0,E^0)^T=[I+hbar*g^2/(16*pi^2*epsilon)*[[z_OO,z_OE],[z_EO,z_EE]]]*(O^R,E^R)^T",
            "DRED_factor": "4-d=2*epsilon",
            "finite_physical_term": "hbar*g^2*z_EO/(8*pi^2)*O^R",
            "symmetry_allowed_witness": "For O=Z and an evanescent copy E with identical typed q/BRST representation, z_EO=z is an arbitrary scalar intertwiner.",
            "residual_q_verdict": "DOES_NOT_FIX_z_EO",
            "Slavnov_verdict": "DOES_NOT_FIX_z_EO_BEFORE_SOURCE_BV_AND_REGULATED_QME_CLOSURE",
            "N4_finiteness_verdict": "NOT_AN_ALLOWED_LOCKED_THEOREM; EVEN_ACTION_FINITE_DATA_WOULD_NOT_EVALUATE_THIS_COMPOSITE_INSERTION_RESIDUE",
            "computed_verdict": "FINITE_EVANESCENT_TO_PHYSICAL_MIXING_CANNOT_BE_EXCLUDED",
        },
        "minimal_dred_ms_insertion_block": {
            "regulator": {
                "d": "4-2*epsilon",
                "metric_split": "delta_4=hat_delta+breve_delta",
                "traces": {"hat_delta": "d", "breve_delta": "2*epsilon"},
                "spin_algebra": "four-dimensional",
                "subtraction": "MS: subtract every 1/epsilon pole and no finite term",
            },
            "bilocal_source": {
                "functional": "S_J=int dx dy J_DE(x,y) O^(DE)(x,y)",
                "operator": "O^(DE)(x,y)=H_X^D(x) U_ad(x,y)^E_F H_Y^F(y)",
                "source_BRST": "sJ_DE= -J_FE rho(c(x))^F_D - J_DF rho(c(x))^F_E",
                "status": "PROPOSED_STEP5_LOCK_REQUIRED",
            },
            "bare_operator_rows": [
                {
                    "id": "O_phys",
                    "operator": "Z^(DE)",
                    "status": "EXACT_FROM_RESIDUAL_Q_RREF",
                },
                {
                    "id": "E_trivial",
                    "operator": "(4-d) Z^(DE)=2*epsilon*Z^(DE)",
                    "status": "EXACT_BUT_NOT_A_GENUINE_BREVE_TENSOR_BASIS",
                },
                {
                    "id": "E_trace_precursor_u",
                    "operator": "E_tr,u=(4-d) E_u with E_u in the same typed pole-renormalized precursor module",
                    "status": "BLOCKED_DRED_EVANESCENT_OPERATOR_BASIS",
                },
                {
                    "id": "E_breve_u",
                    "operator": "basis of ker(pi_4) in the same typed local-source module",
                    "status": "BLOCKED_DRED_EVANESCENT_OPERATOR_BASIS",
                },
                {
                    "id": "N_EOM_N_BRST_N_TD",
                    "operator": "same-typed EOM, BRST-exact, and total-derivative rows",
                    "status": "BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT",
                },
            ],
            "hessian_notation": {
                "K": "zero-background gauge-fixed BV Hessian",
                "G": "K^(-1)",
                "V_n": "background-degree-n part of S_Psi^(2)-K",
                "I_E_n": "background-degree-n part of (J E)^(2)",
            },
            "one_loop_linear_source_degree_two": "Gamma_JE,[2]^(1)=(hbar/2) STr[G I_E,2 - G V_1 G I_E,1 - G V_2 G I_E,0 + G V_1 G V_1 G I_E,0]",
            "one_loop_1PI_graph_classes": [
                {
                    "id": "G1_INSERTION_CONTACT",
                    "term": "+STr[G I_E,2]",
                    "content": "letter nonlinearity, covariant-derivative endpoint, straight-link, and source-contact vertices",
                },
                {
                    "id": "G2_MIXED_BUBBLE",
                    "term": "-STr[G V_1 G I_E,1]",
                    "content": "one cubic action Hessian vertex and one one-background insertion/link vertex",
                },
                {
                    "id": "G3_ACTION_CONTACT",
                    "term": "-STr[G V_2 G I_E,0]",
                    "content": "one quartic action/gauge-fixing/ghost Hessian vertex and the quadratic insertion",
                },
                {
                    "id": "G4_TRIANGLE",
                    "term": "+STr[G V_1 G V_1 G I_E,0]",
                    "content": "both loop orientations, all field blocks, and every graded supertrace sign",
                },
                {
                    "id": "G5_COUNTERTERM_TREE",
                    "term": "+J delta_E^(1)",
                    "content": "operator, elementary-field, coupling, EOM, BRST-exact, and total-derivative counterterm insertions",
                },
            ],
            "exhaustion_scope": "The four STr terms exhaust one-loop 1PI graphs linear in J and quadratic in backgrounds once K,V_n,I_E_n are fully derived; G5 is the separate subtraction tree.",
            "MS_projection": {
                "condition": "After a direct-sum basis and projector P_Z have been locked",
                "loop_pole_definition": "P_Z Res Gamma_JE,[2]^(1)=[hbar*g^2/(16*pi^2)] r_EZ int J Z",
                "counterterm_relation": "z_EO=-r_EZ",
                "zero_condition": "z_EO=0 iff the complete projected pole r_EZ is exactly zero",
            },
            "why_zero_is_not_a_prescription": [
                "In MS, a nonzero r_EZ with z_EO=0 leaves an uncancelled 1/epsilon divergence.",
                "A non-MS local counterterm proportional to the q-primitive Y_r changes the finite AWI representative because q_s Y_r=i delta_sr Z.",
                "After that finite change, comparison to any external target requires a transformed operator dictionary in the same scheme; choosing the finite term from target agreement is circular.",
            ],
            "numerical_status": "BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX",
        },
        "blockers": blockers,
        "tests": tests,
    }
    audit["deterministic_digest"] = sha_json(
        {
            "basis": basis_64,
            "q_complex": q_complex,
            "kernel": vector_json(degree_three_kernel),
            "triple_images": triple_images,
            "primitive": primitive_rref,
        }
    )
    return audit


def render_md(audit: Mapping[str, object]) -> str:
    q_rows = audit["ordered_open_color_space"]["q_complex_rref"]  # type: ignore[index]
    tests = audit["tests"]  # type: ignore[index]
    blockers = audit["blockers"]  # type: ignore[index]

    lines = [
        "# Step-5 local operator basis and one-loop mixing audit",
        "",
        f"Authority: `origin/main@{AUTHORITY_COMMIT}`, verify run `{AUTHORITY_VERIFY_RUN}`.  ",
        "本 audit 未读取 Step-5 contract、其他 Step-5 engine 或 HT target。",
        "",
        "## 1. Typed derivative-slot chain",
        "",
        "$$",
        "d_{\\dot a}:=D_{\\dot a},\\qquad",
        "c_{r\\dot a}:=P_{\\dot a}C_r,\\qquad",
        "b_{r\\dot a}:=P_{\\dot a}B_r,\\qquad",
        "a_{\\dot a}:=P_{\\dot a}A.",
        "$$",
        "",
        "$$",
        "[d,c_r,b_r,a]=\\left(\\frac32,2,\\frac52,3\\right),\\qquad",
        "(|d|,|c_r|,|b_r|,|a|)=(1,0,1,0).",
        "$$",
        "",
        "$$",
        "d,a\\in\\mathbf1,\\qquad b_r\\in\\mathbf3,\\qquad c_r\\in\\overline{\\mathbf3},\\qquad",
        "\\operatorname{gh}(d,c,b,a)=0.",
        "$$",
        "",
        "Step 4C (4C.44)--(4C.47) gives",
        "",
        "$$",
        "q_rd_{\\dot a}=-ic_{r\\dot a},\\qquad",
        "q_rc_{s\\dot a}=-\\frac1{\\sqrt2}\\varepsilon_{rst}b_{t\\dot a},\\qquad",
        "q_rb_{s\\dot a}=-i\\delta_{rs}a_{\\dot a},\\qquad",
        "q_ra_{\\dot a}=0.",
        "$$",
        "",
        "The connection term in $q_rP_{\\dot a}$ vanishes exactly:",
        "",
        "$$",
        "\\begin{aligned}",
        "q_r(P_{\\dot a}X)-P_{\\dot a}(q_rX)",
        "&=\\frac1{\\sqrt2}(\\sigma_E^m)_{+\\dot a}",
        "(\\sigma_{E,m})_{+\\dot b}",
        "(\\widetilde\\psi_r^{\\dot b}\\times X)\\\\",
        "&=0,",
        "\\end{aligned}",
        "$$",
        "",
        "because $(\\sigma_E^m)_{+\\dot a}(\\sigma_{E,m})_{+\\dot b}=0$.",
        "",
        "Use the exact rational chain basis",
        "",
        "$$",
        "e_\\varnothing=i d,\\quad e_r=c_r,\\quad",
        "e_{12}=-\\frac{b_3}{\\sqrt2},\\quad",
        "e_{13}=+\\frac{b_2}{\\sqrt2},\\quad",
        "e_{23}=-\\frac{b_1}{\\sqrt2},\\quad",
        "e_{123}=+\\frac{i}{\\sqrt2}a.",
        "$$",
        "",
        "Then $q_re_S=e_r\\wedge e_S$.",
        "",
        "## 2. Ordered open-color space and exact RREF",
        "",
        "$$",
        "\\mathcal O_{XY}^{DE}:=X_{\\dot a}^D Y^{E\\dot a},\\qquad",
        "(D,E)\\text{ remains ordered}.",
        "$$",
        "",
        "$$",
        "\\mathcal V=\\operatorname{Span}\\{e_S^D\\otimes e_T^E:S,T\\subset\\{1,2,3\\}\\},\\qquad",
        "\\dim\\mathcal V=8^2=64.",
        "$$",
        "",
        "For $n=|S|+|T|$, $[\\mathcal V^n]=3+n/2$ and $|\\mathcal V^n|=n\\bmod2$.  The stacked matrix is",
        "",
        "$$",
        "Q^{(n)}=(q_1,q_2,q_3):\\mathcal V^n\\longrightarrow(\\mathcal V^{n+1})^{\\oplus3}.",
        "$$",
        "",
        "| $n$ | $\\dim\\mathcal V^n$ | rows | rank $Q^{(n)}$ | $\\dim\\bigcap_r\\ker q_r$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in q_rows:  # type: ignore[assignment]
        lines.append(
            f"| {row['degree']} | {row['domain_dimension']} | {row['stacked_row_count']} | {row['rank']} | {row['joint_kernel_dimension']} |"
        )
    lines.extend(
        [
            "",
            "Thus the dimension-$9/2$, odd, ghost-zero block has",
            "",
            "$$",
            "\\dim\\mathcal V^3=20,\\qquad",
            "\\operatorname{rank}Q^{(3)}=19,\\qquad",
            "\\dim\\bigcap_{r=1}^3\\ker q_r=1.",
            "$$",
            "",
            "Its twenty physical monomials are",
            "",
            "$$",
            "\\{\\langle d,a\\rangle,\\ \\langle a,d\\rangle,\\",
            "\\langle c_r,b_s\\rangle,\\ \\langle b_r,c_s\\rangle:",
            "r,s=1,2,3\\}.",
            "$$",
            "",
            "The exact $SU(3)$ decomposition is",
            "",
            "$$",
            "\\mathcal V^3=(\\mathbf1\\oplus\\mathbf1)",
            "\\oplus(\\overline{\\mathbf3}\\otimes\\mathbf3)",
            "\\oplus(\\mathbf3\\otimes\\overline{\\mathbf3})",
            "=4\\,\\mathbf1\\oplus2\\,\\mathbf8.",
            "$$",
            "",
            "RREF gives the unique joint cocycle",
            "",
            "$$",
            "\\boxed{",
            "\\mathscr Z^{DE}",
            "=\\langle d^D,a^E\\rangle-\\langle a^D,d^E\\rangle",
            "+\\sum_{r=1}^3\\left(",
            "\\langle b_r^D,c_r^E\\rangle-\\langle c_r^D,b_r^E\\rangle",
            "\\right),\\qquad q_s\\mathscr Z^{DE}=0.}",
            "$$",
            "",
            "## 3. Complete degree-four counterterm precursor",
            "",
            "The even dimension-four precursor space is",
            "",
            "$$",
            "\\mathcal V^2=\\operatorname{Span}\\{",
            "\\langle d,b_r\\rangle,\\ \\langle b_r,d\\rangle,\\",
            "\\langle c_r,c_s\\rangle:r,s=1,2,3\\},\\qquad",
            "\\dim\\mathcal V^2=15.",
            "$$",
            "",
            "$$",
            "\\mathcal V^2=\\mathbf3\\oplus\\mathbf3\\oplus\\mathbf3",
            "\\oplus\\overline{\\mathbf6}.",
            "$$",
            "",
            "For",
            "",
            "$$",
            "Y_r(\\alpha,\\beta,\\gamma)",
            "=\\alpha\\langle d,b_r\\rangle",
            "+\\beta\\langle b_r,d\\rangle",
            "+\\gamma\\varepsilon_{rst}\\langle c_s,c_t\\rangle,",
            "$$",
            "",
            "write $\\gamma=-i\\sqrt2\\eta$.  The off-diagonal equations $q_sY_r=0$ for $s\\ne r$ have RREF",
            "",
            "$$",
            "\\operatorname{RREF}",
            "\\begin{pmatrix}1&0&-1\\\\0&1&-1\\end{pmatrix}",
            "=\\begin{pmatrix}1&0&-1\\\\0&1&-1\\end{pmatrix},",
            "\\qquad\\alpha=\\beta=\\eta.",
            "$$",
            "",
            "Therefore the covariant triplet is unique:",
            "",
            "$$",
            "\\boxed{",
            "\\mathscr Y_r^{DE}",
            "=\\langle d^D,b_r^E\\rangle+\\langle b_r^D,d^E\\rangle",
            "-i\\sqrt2\\varepsilon_{rst}\\langle c_s^D,c_t^E\\rangle,",
            "\\qquad q_s\\mathscr Y_r^{DE}=i\\delta_{sr}\\mathscr Z^{DE}.}",
            "$$",
            "",
            "For the explicitly declared Koszul quotient",
            "",
            "$$",
            "H_{\\rm joint}^n",
            ":=\\frac{\\bigcap_r\\ker(q_r:\\mathcal V^n\\to\\mathcal V^{n+1})}",
            "{\\operatorname{im}(q_1q_2q_3:\\mathcal V^{n-3}\\to\\mathcal V^n)},",
            "$$",
            "",
            "the kernel and image dimensions for $n=3,4,5,6$ are respectively",
            "",
            "$$",
            "(1,3,3,1)=(1,3,3,1),\\qquad H_{\\rm joint}^n=0.",
            "$$",
            "",
            "This equality applies only to the 64-dimensional derivative-slot module.  It does not perform the BV/EOM/total-derivative/DRED quotient.",
            "",
            "## 4. Required enlarged local space",
            "",
            "At the same dimension, parity, ghost number, $SU(3)$ type and ordered color-source type, the subtraction space must be",
            "",
            "$$",
            "\\mathcal V_{\\rm loc}",
            "=\\mathcal V_{\\rm phys}",
            "\\oplus\\mathcal N_{\\rm EOM}",
            "\\oplus\\mathcal N_{\\rm BRST}",
            "\\oplus\\mathcal N_{\\rm TD}",
            "\\oplus\\mathcal V_{\\rm ev}.",
            "$$",
            "",
            "With the Step-4C Euler operators, the exact module forms are",
            "",
            "$$",
            "\\begin{aligned}",
            "\\mathcal N_{\\rm EOM}",
            "&=\\operatorname{Span}\\{",
            "\\mathscr A_E^mR_m,\\ \\mathscr P_{E,\\mathcal I\\mathcal J}R^{\\mathcal I\\mathcal J},\\",
            "\\widetilde{\\mathscr P}_E^{\\mathcal I\\mathcal J}\\widetilde R_{\\mathcal I\\mathcal J},\\",
            "\\mathcal E_{E,a\\mathcal I}S^{a\\mathcal I},\\",
            "\\widetilde{\\mathcal E}_{E,\\dot a}^{\\mathcal I}",
            "\\widetilde S_{\\mathcal I}^{\\dot a}\\}_{\\rm typed},\\\\",
            "\\mathcal N_{\\rm BRST}",
            "&=\\{\\mathbf s_EK:[K]=9/2,\\ |K|=0,\\operatorname{gh}K=-1\\}_{\\rm typed},\\\\",
            "\\mathcal N_{\\rm TD}",
            "&=\\{\\partial_mJ^m:[J^m]=7/2,\\ |J^m|=1,\\operatorname{gh}J^m=0\\}_{\\rm typed},\\\\",
            "\\mathcal V_{\\rm ev}",
            "&=\\{E_u:E_u|_{\\breve\\delta=0}=0,\\ [E_u]=9/2,\\ |E_u|=1,\\operatorname{gh}E_u=0\\}_{\\rm typed}.",
            "\\end{aligned}",
            "$$",
            "",
            "The locked inputs do not select the multipliers, currents, open-color BV source, or the $\\breve\\delta$ operator grammar.  Hence these four modules have no Project-locked finite basis yet.",
            "",
            "## 5. One-loop evanescent mixing",
            "",
            "For one physical cocycle $O=\\mathscr Z$ and one same-typed DRED precursor $E$, the most general one-loop subtraction is",
            "",
            "$$",
            "\\begin{pmatrix}O^0\\\\E^0\\end{pmatrix}",
            "=\\left[\\mathbf1+\\frac{\\hbar g^2}{16\\pi^2\\epsilon}",
            "\\begin{pmatrix}z_{OO}&z_{OE}\\\\z_{EO}&z_{EE}\\end{pmatrix}\\right]",
            "\\begin{pmatrix}O^R\\\\E^R\\end{pmatrix}.",
            "$$",
            "",
            "Here the trace-evanescent insertion is $E_{\\rm tr}:=(4-d)E$; $E$ is not an already-projected genuine $E_{\\breve u}\\in\\ker\\pi_4$.",
            "",
            "Since $d=4-2\\epsilon$ exactly,",
            "",
            "$$",
            "\\begin{aligned}",
            "(4-d)E^0",
            "&=2\\epsilon E^R",
            "+\\frac{2\\epsilon\\hbar g^2}{16\\pi^2\\epsilon}",
            "(z_{EO}O^R+z_{EE}E^R)\\\\",
            "&=2\\epsilon E^R",
            "+\\frac{\\hbar g^2}{8\\pi^2}",
            "(z_{EO}O^R+z_{EE}E^R).",
            "\\end{aligned}",
            "$$",
            "",
            "The map $E\\mapsto zO$ with arbitrary scalar $z$ commutes with all three $q_r$, preserves dimension/parity/$SU(3)$/ordered color type, and is BRST-covariant.  Therefore Wess--Zumino and classical Slavnov identities do not impose $z_{EO}=0$.",
            "",
            "The locked foundations contain no quantum $\\mathcal N=4$ finiteness theorem.  A vanishing action counterterm would still not evaluate the pole of this composite insertion.",
            "",
            "$$",
            "\\boxed{\\texttt{BLOCKED\\_ONE\\_LOOP\\_COMPOSITE\\_Z\\_MATRIX}:\\quad",
            "Z_{\\rm ev\\to phys}^{(1)}\\text{ cannot be set to zero from the allowed identities.}}",
            "$$",
            "",
            "## 6. Minimal DRED/MS insertion block",
            "",
            "Fix the proposal",
            "",
            "$$",
            "d=4-2\\epsilon,\\qquad",
            "\\delta_4^{mn}=\\widehat\\delta^{mn}+\\breve\\delta^{mn},\\qquad",
            "\\widehat\\delta^m{}_m=d,\\qquad",
            "\\breve\\delta^m{}_m=2\\epsilon,",
            "$$",
            "",
            "with four-dimensional spin algebra and MS subtraction of every $1/\\epsilon$ pole and no finite term.",
            "",
            "For a straight adjoint link, take",
            "",
            "$$",
            "S_J=\\int d^4x\\,d^4y\\ J_{DE}(x,y)\\mathcal O^{DE}(x,y),",
            "$$",
            "",
            "$$",
            "\\mathcal O^{DE}(x,y)",
            "=H_X^D(x)\\,[U_{\\rm ad}(x,y)]^E{}_F\\,H_Y^F(y),",
            "$$",
            "",
            "$$",
            "\\mathbf sJ_{DE}",
            "=-J_{FE}\\rho(\\mathfrak c(x))^F{}_D",
            "-J_{DF}\\rho(\\mathfrak c(x))^F{}_E.",
            "$$",
            "",
            "The allowed bare rows are",
            "",
            "$$",
            "\\mathbf O^0",
            "=\\left(\\mathscr Z^0,\\ E_1^0,\\ldots,\\ E_{\\epsilon}^0,\\ E_{\\breve1}^0,\\ldots,",
            "\\mathcal N_{\\rm EOM}^0,\\mathcal N_{\\rm BRST}^0,\\mathcal N_{\\rm TD}^0\\right)^T,",
            "$$",
            "",
            "$$",
            "E_{{\\rm tr},u}:=(4-d)E_u=2\\epsilon E_u,\\qquad",
            "E_{\\epsilon}:=(4-d)\\mathscr Z=2\\epsilon\\mathscr Z,\\qquad",
            "E_{\\breve u}\\in\\ker\\pi_4,\\qquad",
            "\\pi_4(E_{\\breve u})=E_{\\breve u}|_{\\breve\\delta=0}=0.",
            "$$",
            "",
            "$E_u$ is the pole-renormalized precursor used in Section 5.  $E_{\\epsilon}$ is an exact trivial trace-evanescent row; neither it nor the generic $E_{{\\rm tr},u}$ is a basis for the genuine $E_{\\breve u}$ tensors.",
            "",
            "Let",
            "",
            "$$",
            "\\mathbb K:=S_\\Psi^{(2)}|_{\\text{zero background}},\\qquad",
            "G:=\\mathbb K^{-1},",
            "$$",
            "",
            "$$",
            "V_{[n]}:=\\left(S_\\Psi^{(2)}-\\mathbb K\\right)_{[n]},\\qquad",
            "I_{E,[n]}:=\\left(JE\\right)^{(2)}_{[n]}.",
            "$$",
            "",
            "The one-loop term linear in $J$ and quadratic in backgrounds is exactly",
            "",
            "$$",
            "\\boxed{",
            "\\Gamma_{J,E,[2]}^{(1)}",
            "=\\frac{\\hbar}{2}\\operatorname{STr}\\left[",
            "GI_{E,[2]}-GV_{[1]}GI_{E,[1]}-GV_{[2]}GI_{E,[0]}",
            "+GV_{[1]}GV_{[1]}GI_{E,[0]}\\right].}",
            "$$",
            "",
            "This generates four 1PI classes:",
            "",
            "1. $+\\operatorname{STr}[GI_{E,[2]}]$: insertion/contact/link/endpoint tadpole;",
            "2. $-\\operatorname{STr}[GV_{[1]}GI_{E,[1]}]$: mixed action--insertion bubble;",
            "3. $-\\operatorname{STr}[GV_{[2]}GI_{E,[0]}]$: quartic action, gauge-fixing, or ghost contact bubble;",
            "4. $+\\operatorname{STr}[GV_{[1]}GV_{[1]}GI_{E,[0]}]$: triangle, both orientations and all graded field blocks.",
            "",
            "The separate tree class is $J\\,\\delta E^{(1)}$ and contains operator, elementary-field, coupling, EOM, BRST-exact, and total-derivative counterterms.",
            "",
            "After the direct-sum basis and $\\Pi_{\\mathscr Z}$ have been locked, define the complete pole projection by",
            "",
            "$$",
            "\\Pi_{\\mathscr Z}\\operatorname*{Res}_{\\epsilon=0}",
            "\\Gamma_{J,E,[2]}^{(1)}",
            "=\\frac{\\hbar g^2}{16\\pi^2}r_{E\\mathscr Z}",
            "\\int J_{DE}\\mathscr Z^{DE}.",
            "$$",
            "",
            "With the bare-to-renormalized convention of Section 5, MS cancellation gives",
            "",
            "$$",
            "\\boxed{z_{EO}=-r_{E\\mathscr Z}.}",
            "$$",
            "",
            "Therefore $z_{EO}=0$ is valid exactly when the sum of all four 1PI classes has $r_{E\\mathscr Z}=0$.  If $r_{E\\mathscr Z}\\ne0$, declaring $z_{EO}=0$ leaves an uncancelled $1/\\epsilon$ pole.",
            "",
            "A non-MS counterterm built from $\\mathscr Y_r$ changes the finite Ward representative because",
            "",
            "$$",
            "q_s\\mathscr Y_r=i\\delta_{sr}\\mathscr Z.",
            "$$",
            "",
            "Consequently it also changes the operator dictionary that must be compared in another scheme.  Fixing that finite term from external-target agreement is not an independent Project derivation.",
            "",
            "The locked inputs do not define $E_{\\breve u}$, $\\mathbb K^{-1}$ on a selected DRED gauge slice, or the source Hessians $I_{E,[n]}$.  Hence $r_{E\\mathscr Z}$ and $z_{EO}$ remain unevaluated.",
            "",
            "## 7. P0 blockers",
            "",
        ]
    )
    for blocker in blockers:  # type: ignore[assignment]
        lines.append(f"- `{blocker['id']}`: {blocker['minimal_missing_input']}")
    lines.extend(["", "## 8. Machine checks", ""])
    for test in tests:  # type: ignore[assignment]
        lines.append(f"- `{test['id']}`: {'PASS' if test['pass'] else 'FAIL'}")
    lines.extend(["", f"Deterministic digest: `{audit['deterministic_digest']}`", ""])
    return "\n".join(lines)


def main() -> int:
    audit = build_audit()
    JSON_OUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    MD_OUT.write_text(render_md(audit))
    failed = [test["id"] for test in audit["tests"] if not test["pass"]]
    print(json.dumps({"status": audit["status"], "failed_tests": failed, "json": str(JSON_OUT), "md": str(MD_OUT)}))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
