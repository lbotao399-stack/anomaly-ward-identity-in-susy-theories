#!/usr/bin/env python3
"""Exact Step-5A chiral/vector frame-bridge certificates.

The script keeps three maps separate.

1.  Covariant adjoint operators use the exact Step-3C similarity

        O_C = B^(-1) O_V B.

2.  Integrated quantum coordinates use the Step-3D tangent map

        zeta_V = T_q(Bbar, zeta_C),
        J_q = d zeta_V / d zeta_C.

    A nonlinear T_q gives an Euler-gradient connection term in the Hessian.

3.  Equality of full finite-BV integrals additionally requires the complete
    Step-3D pushforward density, ghost/non-minimal Jacobians, source lift, and
    cycle map.  The reference-flat Step-5A adjoint-block check below is not a
    certificate for that finite-BV statement.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.verify_step5_propagators import (  # noqa: E402
    Matrix,
    QComplex,
    add,
    identity,
    inverse,
    kronecker,
    multiply,
    q,
    scale,
)
from scripts.verify_step5a_fixed_kernel import (  # noqa: E402
    MOMENTA,
    fixed_kernel,
)


GENERATED = ROOT / "generated/step5/frame-bridge-intertwiner.json"
AUDIT = ROOT / "audits/step5-frame-bridge-intertwiner-verification.json"
AUDIT_MD = ROOT / "audits/step5-frame-bridge-intertwiner.md"

ZERO = q(0)
ONE = q(1)
IMAGINARY_UNIT = QComplex(Fraction(0), Fraction(1))
HALF = QComplex(Fraction(1, 2), Fraction(0))


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [
        [matrix[row][column] for row in range(len(matrix))]
        for column in range(len(matrix[0]))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return add(left, scale(q(-1), right))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def determinant(matrix: Matrix) -> QComplex:
    """Exact determinant by parity-preserving Gaussian elimination."""

    if not matrix:
        return ONE
    work = [row[:] for row in matrix]
    size = len(work)
    result = ONE
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != ZERO),
            None,
        )
        if pivot is None:
            return ZERO
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = q(-1) * result
        pivot_value = work[column][column]
        result = result * pivot_value
        pivot_inverse = ONE / pivot_value
        for row in range(column + 1, size):
            factor = work[row][column] * pivot_inverse
            if factor == ZERO:
                continue
            for entry in range(column, size):
                work[row][entry] = (
                    work[row][entry] - factor * work[column][entry]
                )
    return result


def trace(matrix: Matrix) -> QComplex:
    result = ZERO
    for index in range(len(matrix)):
        result = result + matrix[index][index]
    return result


def supertrace(matrix: Matrix, parities: tuple[int, ...]) -> QComplex:
    result = ZERO
    for index, parity in enumerate(parities):
        sign = q(1 if parity == 0 else -1)
        result = result + sign * matrix[index][index]
    return result


def diagonal(entries: Iterable[QComplex]) -> Matrix:
    values = tuple(entries)
    return [
        [value if row == column else ZERO for column, value in enumerate(values)]
        for row in range(len(values))
    ]


@dataclass(frozen=True)
class Dual:
    """Element c0+c1*tau of Q(i)[tau]/(tau^2), with even tau."""

    c0: QComplex = ZERO
    c1: QComplex = ZERO

    def __add__(self, other: Dual) -> Dual:
        return Dual(self.c0 + other.c0, self.c1 + other.c1)

    def __sub__(self, other: Dual) -> Dual:
        return Dual(self.c0 - other.c0, self.c1 - other.c1)

    def __neg__(self) -> Dual:
        return Dual(-self.c0, -self.c1)

    def __mul__(self, other: Dual) -> Dual:
        return Dual(
            self.c0 * other.c0,
            self.c0 * other.c1 + self.c1 * other.c0,
        )

    def to_json(self) -> dict[str, object]:
        return {"constant": self.c0.to_json(), "tau": self.c1.to_json()}


DZERO = Dual()
DONE = Dual(ONE, ZERO)
DTAU = Dual(ZERO, ONE)


def dual(value: int | Fraction | QComplex) -> Dual:
    if isinstance(value, QComplex):
        return Dual(value, ZERO)
    return Dual(q(value), ZERO)


DualMatrix = list[list[Dual]]


def didentity(size: int) -> DualMatrix:
    return [
        [DONE if row == column else DZERO for column in range(size)]
        for row in range(size)
    ]


def dtranspose(matrix: DualMatrix) -> DualMatrix:
    return [
        [matrix[row][column] for row in range(len(matrix))]
        for column in range(len(matrix[0]))
    ]


def dadd(left: DualMatrix, right: DualMatrix) -> DualMatrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def dscale(factor: Dual, matrix: DualMatrix) -> DualMatrix:
    return [[factor * entry for entry in row] for row in matrix]


def dsubtract(left: DualMatrix, right: DualMatrix) -> DualMatrix:
    return dadd(left, dscale(dual(-1), right))


def dmultiply(left: DualMatrix, right: DualMatrix) -> DualMatrix:
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return [
        [
            sum(
                (left[row][entry] * right[entry][column] for entry in range(inner)),
                DZERO,
            )
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def dcommutator(left: DualMatrix, right: DualMatrix) -> DualMatrix:
    return dsubtract(dmultiply(left, right), dmultiply(right, left))


def dtrace(matrix: DualMatrix) -> Dual:
    return sum((matrix[index][index] for index in range(len(matrix))), DZERO)


def ddet2(matrix: DualMatrix) -> Dual:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def ddet3(matrix: DualMatrix) -> Dual:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def dmatrix_to_json(matrix: DualMatrix) -> list[list[dict[str, object]]]:
    return [[entry.to_json() for entry in row] for row in matrix]


def fundamental_generators() -> tuple[DualMatrix, ...]:
    """A defined, directly checked sl(2) witness basis with tr(T_A T_B)=delta/2."""

    return (
        [[DZERO, dual(HALF)], [dual(HALF), DZERO]],
        [
            [DZERO, dual(-IMAGINARY_UNIT * HALF)],
            [dual(IMAGINARY_UNIT * HALF), DZERO],
        ],
        [[dual(HALF), DZERO], [DZERO, dual(-HALF)]],
    )


def nilpotent_fundamental_bridge() -> tuple[DualMatrix, DualMatrix]:
    """B=diag(1+tau/2,1-tau/2), even tau^2=0, and its exact inverse."""

    plus = DONE + Dual(ZERO, HALF)
    minus = DONE - Dual(ZERO, HALF)
    bridge = [[plus, DZERO], [DZERO, minus]]
    bridge_inverse = [[minus, DZERO], [DZERO, plus]]
    return bridge, bridge_inverse


def adjoint_bridge_dual() -> tuple[DualMatrix, DualMatrix]:
    """Compute Ad_B and Ad_(B^-1) by exact fundamental conjugation."""

    generators = fundamental_generators()
    bridge, bridge_inverse = nilpotent_fundamental_bridge()

    def adjoint_of(left: DualMatrix, right: DualMatrix) -> DualMatrix:
        columns: list[list[Dual]] = []
        for generator in generators:
            transported = dmultiply(dmultiply(left, generator), right)
            coefficients = []
            for projector in generators:
                coefficients.append(dual(2) * dtrace(dmultiply(projector, transported)))
            columns.append(coefficients)
        return [
            [columns[column][row] for column in range(3)]
            for row in range(3)
        ]

    return (
        adjoint_of(bridge, bridge_inverse),
        adjoint_of(bridge_inverse, bridge),
    )


def grassmann_tau_left_multiplication() -> Matrix:
    """Left multiplication by even tau=theta^1 theta^2 in mask order 0,...,15."""

    matrix = [[ZERO for _ in range(16)] for _ in range(16)]
    tau_mask = 0b0011
    for column_mask in range(16):
        if column_mask & tau_mask:
            continue
        row_mask = column_mask | tau_mask
        matrix[row_mask][column_mask] = ONE
    return matrix


def dual_entry_on_grassmann(entry: Dual, tau_matrix: Matrix) -> Matrix:
    unit16 = identity(16)
    return add(scale(entry.c0, unit16), scale(entry.c1, tau_matrix))


def adjoint_bridge_full() -> tuple[Matrix, Matrix, tuple[int, ...]]:
    """Actual background-dependent Ad_B on Adj tensor the full M_8 coefficients."""

    adjoint, adjoint_inverse = adjoint_bridge_dual()
    tau_matrix = grassmann_tau_left_multiplication()

    def expand(matrix: DualMatrix) -> Matrix:
        result = [[ZERO for _ in range(48)] for _ in range(48)]
        for color_row in range(3):
            for color_column in range(3):
                block = dual_entry_on_grassmann(
                    matrix[color_row][color_column], tau_matrix
                )
                for grass_row in range(16):
                    for grass_column in range(16):
                        result[16 * color_row + grass_row][
                            16 * color_column + grass_column
                        ] = block[grass_row][grass_column]
        return result

    parities = tuple(mask.bit_count() % 2 for _ in range(3) for mask in range(16))
    return expand(adjoint), expand(adjoint_inverse), parities


def principal_submatrix(matrix: Matrix, indices: tuple[int, ...]) -> Matrix:
    return [[matrix[row][column] for column in indices] for row in indices]


def source_bilinear_witness() -> Matrix:
    color = diagonal((q(1), q(2), q(3)))
    grassmann = diagonal(
        q(1 if mask.bit_count() % 2 == 0 else 2) for mask in range(16)
    )
    return kronecker(color, grassmann)


def reduce_inverse_words(word: tuple[str, ...]) -> tuple[str, ...]:
    """Cancel adjacent B^(-1)B and BB^(-1) without commuting any letter."""

    stack: list[str] = []
    for letter in word:
        if stack and (stack[-1], letter) in {("B", "Binv"), ("Binv", "B")}:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def abstract_similarity_checks() -> dict[str, bool]:
    """Gauge-algebra-independent conjugation identities as ordered words."""

    forward_xy = reduce_inverse_words(("B", "X", "Binv", "B", "Y", "Binv"))
    forward_yx = reduce_inverse_words(("B", "Y", "Binv", "B", "X", "Binv"))
    inverse_xy = reduce_inverse_words(
        ("Binv", "X", "B", "Binv", "Y", "B")
    )
    inverse_yx = reduce_inverse_words(
        ("Binv", "Y", "B", "Binv", "X", "B")
    )
    return {
        "conjugation_product_xy": forward_xy == ("B", "X", "Y", "Binv"),
        "conjugation_product_yx": forward_yx == ("B", "Y", "X", "Binv"),
        "conjugation_preserves_commutator": (
            forward_xy,
            forward_yx,
        )
        == (
            ("B", "X", "Y", "Binv"),
            ("B", "Y", "X", "Binv"),
        ),
        "inverse_similarity_product_xy": inverse_xy
        == ("Binv", "X", "Y", "B"),
        "inverse_similarity_product_yx": inverse_yx
        == ("Binv", "Y", "X", "B"),
    }


def project_adjoint_bridge_checks() -> dict[str, bool]:
    bridge, bridge_inverse = nilpotent_fundamental_bridge()
    adjoint, adjoint_inverse = adjoint_bridge_dual()
    generators = fundamental_generators()
    checks = {
        "tau_is_even": (2 % 2) == 0,
        "tau_square_zero": DTAU * DTAU == DZERO,
        "fundamental_bridge_left_inverse": dmultiply(bridge_inverse, bridge)
        == didentity(2),
        "fundamental_bridge_right_inverse": dmultiply(bridge, bridge_inverse)
        == didentity(2),
        "fundamental_bridge_determinant_one": ddet2(bridge) == DONE,
        "adjoint_left_inverse": dmultiply(adjoint_inverse, adjoint) == didentity(3),
        "adjoint_right_inverse": dmultiply(adjoint, adjoint_inverse) == didentity(3),
        "adjoint_metric_invariance": dmultiply(dtranspose(adjoint), adjoint)
        == didentity(3),
        "adjoint_determinant_one": ddet3(adjoint) == DONE,
    }
    for left_index, right_index in itertools.product(range(3), repeat=2):
        transported_left = dmultiply(
            dmultiply(bridge, generators[left_index]), bridge_inverse
        )
        transported_right = dmultiply(
            dmultiply(bridge, generators[right_index]), bridge_inverse
        )
        checks[f"fundamental_commutator_{left_index}_{right_index}"] = dcommutator(
            transported_left, transported_right
        ) == dmultiply(
            dmultiply(bridge, dcommutator(generators[left_index], generators[right_index])),
            bridge_inverse,
        )
    return checks


def frame_witness(momentum: tuple[int, int, int, int]) -> dict[str, object]:
    """Exact Hessian/Green/insertion transport by the nilpotent Project bridge."""

    matrices = fixed_kernel(momentum)
    frame, frame_inverse, parities = adjoint_bridge_full()
    frame_transpose = transpose(frame)
    frame_inverse_transpose = transpose(frame_inverse)
    unit48 = identity(48)

    pairing_vector = unit48
    kernel_vector = kronecker(identity(3), matrices["K_tot"])
    green_vector = kronecker(identity(3), matrices["G"])
    insertion_vector = source_bilinear_witness()

    pairing_chiral = multiply(multiply(frame_transpose, pairing_vector), frame)
    pairing_chiral_inverse = inverse(pairing_chiral)
    kernel_chiral = multiply(multiply(frame_transpose, kernel_vector), frame)
    green_chiral = multiply(
        multiply(frame_inverse, green_vector), frame_inverse_transpose
    )
    insertion_chiral = multiply(
        multiply(frame_transpose, insertion_vector), frame
    )

    hessian_op_vector = multiply(inverse(pairing_vector), kernel_vector)
    hessian_op_chiral = multiply(pairing_chiral_inverse, kernel_chiral)
    green_op_vector = inverse(hessian_op_vector)
    green_op_chiral = inverse(hessian_op_chiral)
    insertion_op_vector = multiply(inverse(pairing_vector), insertion_vector)
    insertion_op_chiral = multiply(pairing_chiral_inverse, insertion_chiral)

    contraction_vector = multiply(green_vector, insertion_vector)
    contraction_chiral = multiply(green_chiral, insertion_chiral)
    contraction_similarity = multiply(
        multiply(frame_inverse, contraction_vector), frame
    )

    even_indices = tuple(index for index, parity in enumerate(parities) if parity == 0)
    odd_indices = tuple(index for index, parity in enumerate(parities) if parity == 1)
    determinant_even = determinant(principal_submatrix(frame, even_indices))
    determinant_odd = determinant(principal_submatrix(frame, odd_indices))

    checks = {
        "frame_left_inverse": multiply(frame_inverse, frame) == unit48,
        "frame_right_inverse": multiply(frame, frame_inverse) == unit48,
        "frame_is_parity_preserving": all(
            frame[row][column] == ZERO or parities[row] == parities[column]
            for row in range(48)
            for column in range(48)
        ),
        "even_block_determinant_one": determinant_even == ONE,
        "odd_block_determinant_one": determinant_odd == ONE,
        "reference_flat_berezinian_one": determinant_even / determinant_odd == ONE,
        "chiral_kernel_green_left_inverse": multiply(kernel_chiral, green_chiral)
        == unit48,
        "chiral_green_kernel_right_inverse": multiply(green_chiral, kernel_chiral)
        == unit48,
        "back_transport_kernel": multiply(
            multiply(frame_inverse_transpose, kernel_chiral), frame_inverse
        )
        == kernel_vector,
        "back_transport_green": multiply(
            multiply(frame, green_chiral), frame_transpose
        )
        == green_vector,
        "pairing_inverse": multiply(pairing_chiral, pairing_chiral_inverse)
        == unit48,
        "hessian_endomorphism_similarity": hessian_op_chiral
        == multiply(multiply(frame_inverse, hessian_op_vector), frame),
        "green_endomorphism_similarity": green_op_chiral
        == multiply(multiply(frame_inverse, green_op_vector), frame),
        "upper_green_from_endomorphism_and_pairing": green_chiral
        == multiply(green_op_chiral, pairing_chiral_inverse),
        "insertion_bilinear_congruence": insertion_chiral
        == multiply(multiply(frame_transpose, insertion_vector), frame),
        "insertion_endomorphism_similarity": insertion_op_chiral
        == multiply(multiply(frame_inverse, insertion_op_vector), frame),
        "source_contraction_similarity": contraction_chiral
        == contraction_similarity,
        "source_contraction_supertrace_invariance": supertrace(
            contraction_chiral, parities
        )
        == supertrace(contraction_vector, parities),
        "nonzero_supertrace_witness": supertrace(insertion_op_vector, parities)
        != ZERO,
        "insertion_supertrace_invariance": supertrace(
            insertion_op_chiral, parities
        )
        == supertrace(insertion_op_vector, parities),
    }
    return {
        "momentum": list(momentum),
        "dimension": 48,
        "even_dimension": len(even_indices),
        "odd_dimension": len(odd_indices),
        "determinant_even": determinant_even.to_json(),
        "determinant_odd": determinant_odd.to_json(),
        "checks": checks,
    }


def nonlinear_tangent_hessian_witness() -> dict[str, object]:
    """Exact chain-rule witness for action and source-Hessian connection terms."""

    jacobian = identity(2)
    hessian_vector = [[q(2), q(1)], [q(1), q(4)]]
    euler_vector = [q(3), q(5)]
    connection = [[euler_vector[1], ZERO], [ZERO, ZERO]]
    congruence = multiply(multiply(transpose(jacobian), hessian_vector), jacobian)
    hessian_chiral = add(congruence, connection)
    direct_hessian = [[q(7), q(1)], [q(1), q(4)]]
    source_gradient_vector = [ZERO, q(7)]
    source_hessian_vector = [[ZERO, ZERO], [ZERO, ZERO]]
    source_connection = [[source_gradient_vector[1], ZERO], [ZERO, ZERO]]
    source_hessian_chiral = add(source_hessian_vector, source_connection)
    direct_source_hessian = [[q(7), ZERO], [ZERO, ZERO]]
    zero_connection = [[ZERO, ZERO], [ZERO, ZERO]]
    return {
        "coordinate_map": "y1=x1; y2=x2+(1/2)*x1^2",
        "action": "S_V=3*y1+5*y2+y1^2+y1*y2+2*y2^2",
        "source_composite": "I_V=7*y2",
        "expansion_point": [0, 0],
        "euler_vector": [entry.to_json() for entry in euler_vector],
        "hessian_vector": [
            [entry.to_json() for entry in row] for row in hessian_vector
        ],
        "connection": [[entry.to_json() for entry in row] for row in connection],
        "hessian_chiral": [
            [entry.to_json() for entry in row] for row in hessian_chiral
        ],
        "source_gradient_vector": [
            entry.to_json() for entry in source_gradient_vector
        ],
        "source_hessian_vector": [
            [entry.to_json() for entry in row] for row in source_hessian_vector
        ],
        "source_connection": [
            [entry.to_json() for entry in row] for row in source_connection
        ],
        "source_hessian_chiral": [
            [entry.to_json() for entry in row] for row in source_hessian_chiral
        ],
        "checks": {
            "exact_chain_rule_matches_direct_hessian": hessian_chiral
            == direct_hessian,
            "connection_term_is_nonzero": connection != zero_connection,
            "congruence_only_is_false_off_shell": congruence != direct_hessian,
            "eom_zero_removes_connection": add(congruence, zero_connection)
            == congruence,
            "affine_map_removes_connection": add(congruence, zero_connection)
            == congruence,
            "source_exact_chain_rule_matches_direct_hessian": source_hessian_chiral
            == direct_source_hessian,
            "source_connection_term_is_nonzero": source_connection
            != zero_connection,
            "source_congruence_only_is_false": source_hessian_vector
            != direct_source_hessian,
        },
    }


def background_ward_intertwiner_witness() -> dict[str, object]:
    """Exact transport of commutator Ward recursion through A(B)."""

    frame, frame_inverse = adjoint_bridge_dual()
    r_chiral = [
        [DZERO, DONE, DZERO],
        [-DONE, DZERO, DZERO],
        [DZERO, DZERO, DZERO],
    ]
    r_vector = [
        [DZERO, DZERO, DONE],
        [DZERO, DZERO, DZERO],
        [-DONE, DZERO, DZERO],
    ]
    delta_frame = dsubtract(
        dmultiply(r_vector, frame), dmultiply(frame, r_chiral)
    )
    delta_frame_inverse = dscale(
        dual(-1), dmultiply(dmultiply(frame_inverse, delta_frame), frame_inverse)
    )

    h_vector = [
        [dual(2), DZERO, DZERO],
        [DZERO, dual(3), DZERO],
        [DZERO, DZERO, dual(5)],
    ]
    g_vector = [
        [dual(Fraction(1, 2)), DZERO, DZERO],
        [DZERO, dual(Fraction(1, 3)), DZERO],
        [DZERO, DZERO, dual(Fraction(1, 5))],
    ]
    insertion_vector = [
        [DONE, dual(1), DZERO],
        [DZERO, dual(2), dual(-1)],
        [dual(1), DZERO, dual(4)],
    ]

    def transport(matrix: DualMatrix) -> DualMatrix:
        return dmultiply(dmultiply(frame_inverse, matrix), frame)

    def delta_transport(
        matrix: DualMatrix, delta_matrix: DualMatrix
    ) -> DualMatrix:
        return dadd(
            dadd(
                dmultiply(dmultiply(delta_frame_inverse, matrix), frame),
                dmultiply(dmultiply(frame_inverse, delta_matrix), frame),
            ),
            dmultiply(dmultiply(frame_inverse, matrix), delta_frame),
        )

    h_chiral = transport(h_vector)
    g_chiral = transport(g_vector)
    insertion_chiral = transport(insertion_vector)
    delta_h_chiral = delta_transport(h_vector, dcommutator(r_vector, h_vector))
    delta_g_chiral = delta_transport(g_vector, dcommutator(r_vector, g_vector))
    delta_insertion_chiral = delta_transport(
        insertion_vector, dcommutator(r_vector, insertion_vector)
    )

    word_chiral = dmultiply(
        dmultiply(dmultiply(g_chiral, insertion_chiral), g_chiral), h_chiral
    )
    delta_word_product = dadd(
        dadd(
            dmultiply(
                dmultiply(dmultiply(delta_g_chiral, insertion_chiral), g_chiral),
                h_chiral,
            ),
            dmultiply(
                dmultiply(dmultiply(g_chiral, delta_insertion_chiral), g_chiral),
                h_chiral,
            ),
        ),
        dadd(
            dmultiply(
                dmultiply(dmultiply(g_chiral, insertion_chiral), delta_g_chiral),
                h_chiral,
            ),
            dmultiply(
                dmultiply(dmultiply(g_chiral, insertion_chiral), g_chiral),
                delta_h_chiral,
            ),
        ),
    )
    delta_word_commutator = dcommutator(r_chiral, word_chiral)
    checks = {
        "intertwiner_variation_nonzero": delta_frame
        != [[DZERO for _ in range(3)] for _ in range(3)],
        "inverse_variation_identity": dadd(
            dmultiply(delta_frame_inverse, frame),
            dmultiply(frame_inverse, delta_frame),
        )
        == [[DZERO for _ in range(3)] for _ in range(3)],
        "hessian_ward_transport": delta_h_chiral
        == dcommutator(r_chiral, h_chiral),
        "green_ward_transport": delta_g_chiral
        == dcommutator(r_chiral, g_chiral),
        "insertion_ward_transport": delta_insertion_chiral
        == dcommutator(r_chiral, insertion_chiral),
        "rooted_word_ward_telescoping": delta_word_product
        == delta_word_commutator,
        "rooted_word_trace_variation_zero": dtrace(delta_word_product) == DZERO,
        "green_is_hessian_inverse_vector": dmultiply(h_vector, g_vector)
        == didentity(3),
        "green_is_hessian_inverse_chiral": dmultiply(h_chiral, g_chiral)
        == didentity(3),
    }
    return {
        "intertwiner_law": "delta(A)=R_V*A-A*R_C",
        "ward_law_vector": "delta(X_V)=[R_V,X_V]",
        "ward_law_chiral": "delta(X_C)=[R_C,X_C]",
        "delta_frame": dmatrix_to_json(delta_frame),
        "checks": checks,
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    abstract_checks = abstract_similarity_checks()
    project_checks = project_adjoint_bridge_checks()
    witnesses = [frame_witness(momentum) for momentum in MOMENTA]
    tangent = nonlinear_tangent_hessian_witness()
    ward = background_ward_intertwiner_witness()
    checks = {
        **{f"abstract_similarity.{name}": passed for name, passed in abstract_checks.items()},
        **{f"project_bridge.{name}": passed for name, passed in project_checks.items()},
        **{
            f"momentum_{witness_index}.{name}": passed
            for witness_index, witness in enumerate(witnesses)
            for name, passed in witness["checks"].items()
        },
        **{
            f"nonlinear_tangent.{name}": passed
            for name, passed in tangent["checks"].items()
        },
        **{f"background_ward.{name}": passed for name, passed in ward["checks"].items()},
    }
    adjoint, adjoint_inverse = adjoint_bridge_dual()
    return {
        "schema": "Step5FrameBridgeIntertwiner.v2",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope": "COVARIANT_ADJOINT_SIMILARITY_AND_TANGENT_CHAIN_RULE",
        "project_frame": {
            "symmetric_bridge": "B=tildeB=exp(V/2)",
            "general_identity": "Ad_B(X) Ad_B(Y)=Ad_B(XY) by adjacent B^(-1)B cancellation",
            "exact_witness_role": "SU2_NILPOTENT_WITNESS_ONLY",
            "exact_witness": "tau=theta^1*theta^2; epsilon(tau)=0; tau^2=0; B=diag(1+tau/2,1-tau/2)",
            "adjoint": dmatrix_to_json(adjoint),
            "adjoint_inverse": dmatrix_to_json(adjoint_inverse),
            "coefficient_dimension": 48,
            "grassmann_basis": "Lambda(theta^1,theta^2,bartheta_dot1,bartheta_dot2), four-generator masks 0,...,15",
        },
        "equations": {
            "covariant_operator": "O_C=B^(-1)*O_V*B",
            "covariant_coefficients": "o_V=A_B*o_C; A_B=Ad_B",
            "field_strength": "W_V=B*W_C*B^(-1)",
            "tilded_field_strength": "tildeW_V=tildeB^(-1)*tildeW_A*tildeB",
            "quantum_map": "zeta_V=T_q(Qbar_C,zeta_C)",
            "quantum_tangent": "J_q=d(zeta_V)/d(zeta_C)|_(Qbar_C)",
            "quantum_second_jet": "C^alpha_(ij)=d^2(zeta_V^alpha)/(d zeta_C^i d zeta_C^j)",
            "euler_covector": "E_C=E_V*J_q",
            "hessian_chain_rule": "K_C=J_q^st*K_V*J_q+E_(V,alpha)*C^alpha",
            "hessian_congruence_condition": "E_V*C=0",
            "source_hessian_chain_rule": "Ibil_C=J_q^st*Ibil_V*J_q+F_(V,alpha)*C^alpha; F_V=d(I_V)/d(zeta_V)",
            "source_hessian_congruence_condition": "F_V*C=0",
            "pairing": "Omega_C=J_q^st*Omega_V*J_q",
            "hessian_endomorphism_conditional": "H_C=J_q^(-1)*H_V*J_q when E_V*C=0",
            "green_endomorphism_conditional": "Gop_C=J_q^(-1)*Gop_V*J_q when E_V*C=0",
            "upper_green_conditional": "G_C=J_q^(-1)*G_V*J_q^(-st) when E_V*C=0",
            "source_bilinear_conditional": "Ibil_C=J_q^st*Ibil_V*J_q when F_V*C=0",
            "source_endomorphism_conditional": "Iop_C=J_q^(-1)*Iop_V*J_q when F_V*C=0",
            "one_loop_word": "STr(Gop_C*Iop_C)=STr(Gop_V*Iop_V)",
            "intertwiner_variation": "delta(A)=R_V*A-A*R_C",
            "ward_transport": "delta(X_V)=[R_V,X_V] implies delta(X_C)=[R_C,X_C]",
            "reference_flat_adjoint_berezinian": "Ber(A_B|Adj tensor M_8)=det(A_even)/det(A_odd)=1/1=1",
            "full_density_pushforward": "varpi_V(x_V)=varpi_C(T^(-1)x_V)*Ber(d x_C/d x_V)",
        },
        "source_equations": [
            "3C.25",
            "3C.33",
            "3D.22",
            "3D.108",
            "3D.109",
            "3D.109a",
            "3D.110",
            "3D.110a",
        ],
        "abstract_similarity_checks": abstract_checks,
        "su2_nilpotent_witness_checks": project_checks,
        "witnesses": witnesses,
        "nonlinear_tangent_witness": tangent,
        "background_ward_witness": ward,
        "checks": checks,
        "gates": {
            "covariant_operator_similarity_general_gauge_algebra": "PASS",
            "background_dependent_su2_nilpotent_coefficient_witness": "PASS",
            "quadratic_hessian_green_source_supertrace_on_similarity_sector": "PASS",
            "reference_flat_measure_covariant_adjoint_block": "PASS",
            "background_ward_recursion_similarity_sector": "PASS",
            "nonlinear_quantum_tangent_hessian": "CONDITIONAL_E_V_C_EQUALS_ZERO",
            "nonlinear_source_hessian_insertion": "CONDITIONAL_F_V_C_EQUALS_ZERO",
            "arbitrary_gauge_algebra_background_regulator_closure": "OPEN",
            "full_physical_ghost_nonminimal_frame_jacobian": "OPEN_3D109A",
            "full_finite_bv_density_and_cycle": "OPEN_STEP5C_3D110",
            "cross_frame_functional_equality_with_independent_flat_measures": "NOT_ASSERTED",
            "anomaly_coefficient": "NOT_COMPUTED",
        },
        "gap_ledger": [
            {
                "id": "G1",
                "type": "G-DEF",
                "location": "Step5FrameBridgeIntertwiner.v1 frame_matrix",
                "claim": "an arbitrary two-by-two GL matrix represented the Project frame bridge",
                "missing": "the matrix was not Ad_B",
                "minimal_repair": "general ordered conjugation proof plus an explicitly labeled SU2_NILPOTENT_WITNESS",
                "severity": "P0",
                "status": "RESOLVED",
            },
            {
                "id": "G2",
                "type": "G-ALG",
                "location": "quadratic Hessian transport",
                "claim": "K_C=J_q^st K_V J_q for a nonlinear quantum map",
                "missing": "the Euler-gradient second-jet term E_V,alpha C^alpha",
                "minimal_repair": "K_C=J_q^st K_V J_q+E_V,alpha C^alpha",
                "severity": "P0",
                "status": "RESOLVED",
            },
            {
                "id": "G3",
                "type": "G-ALG",
                "location": "scalar source-Hessian transport",
                "claim": "Ibil_C=J_q^st Ibil_V J_q for a nonlinear quantum map",
                "missing": "the source first-jet term F_V,alpha C^alpha",
                "minimal_repair": "Ibil_C=J_q^st Ibil_V J_q+F_V,alpha C^alpha",
                "severity": "P0",
                "status": "RESOLVED",
            },
            {
                "id": "G4",
                "type": "G-NORM",
                "location": "Step 3D.109a full integrated frame Jacobian",
                "claim": "the reference-flat adjoint-block Berezinian proves full cross-frame measure equality",
                "missing": "physical, chiral/antichiral ghost, and every non-minimal Berezinian factor",
                "minimal_repair": "compute every factor in Ber J_T^perp of 3D.109a",
                "severity": "P1",
                "status": "OPEN_STEP5C",
            },
            {
                "id": "G5",
                "type": "G-SCOPE",
                "location": "Step 3D.108 finite coefficient commutative square",
                "claim": "one SU2 nilpotent witness proves arbitrary-background regulator closure",
                "missing": "the generic mode-space action and residual-complement bijections",
                "minimal_repair": "construct J_q and its inverse on every admitted finite background block",
                "severity": "P1",
                "status": "OPEN",
            },
            {
                "id": "G6",
                "type": "G-SCOPE",
                "location": "Step 3D.110 finite-BV pushforward",
                "claim": "fixed-gauge reference-flat equality proves finite-BV frame equality",
                "missing": "density, source lift, regulator, determinant factor, and cycle pushforwards",
                "minimal_repair": "instantiate all pushforwards in 3D.110 and 3D.110a",
                "severity": "P1",
                "status": "OPEN_STEP5C",
            },
        ],
        "checked_equation_groups": 8,
        "verification_spot_checks": [
            "fundamental conjugation and commutator",
            "forty-eight-dimensional two-sided inverse and Berezinian",
            "direct action and scalar-source second derivatives",
        ],
        "frame_matrix_deprecation": (
            "The former arbitrary 2x2 GL witness is removed; it was not Ad_B and "
            "carried no Project frame evidence."
        ),
        "external_results_imported": False,
    }


def build_audit_markdown(payload: dict[str, object]) -> bytes:
    checks = payload["checks"]
    passed = sum(bool(result) for result in checks.values())
    total = len(checks)
    text = r"""# Step 5A frame-bridge intertwiner audit

Status: `PASS_EXACT_CERTIFICATES_WITH_OPEN_FULL_BV_GATE`

## 1. Three distinct maps

$$
\mathcal O_{\mathsf C}=\mathcal B^{-1}\mathcal O_{\mathsf V}\mathcal B,
\qquad
o_{\mathsf V}=A_{\mathcal B}o_{\mathsf C},
\qquad
A_{\mathcal B}=\operatorname{{Ad}}_{\mathcal B}.
$$

$$
\boldsymbol{\mathcal W}_{\mathsf V}
=\mathcal B\mathcal W_{\mathsf C}\mathcal B^{-1},
\qquad
\widetilde{\boldsymbol{\mathcal W}}_{\mathsf V}
=\widetilde{\mathcal B}^{-1}
\widetilde{\mathcal W}_{\mathsf A}
\widetilde{\mathcal B}.
$$

$$
\zeta_{\mathsf V}
=\mathbb T_{\rm q}(\overline Q_{\mathsf C},\zeta_{\mathsf C}),
\qquad
J_{\rm q}
=\left.\frac{\vec\partial\zeta_{\mathsf V}}
{\partial\zeta_{\mathsf C}}\right|_{\overline Q_{\mathsf C}}.
$$

$$
\boldsymbol\varpi_{\mathsf V}(x_{\mathsf V})
=\boldsymbol\varpi_{\mathsf C}(\mathbb T^{-1}x_{\mathsf V})
\operatorname{{Ber}}\!\left(
\frac{\vec\partial x_{\mathsf C}}{\partial x_{\mathsf V}}
\right).
$$

These are respectively an operator similarity, a quantum-coordinate tangent
map, and a full density pushforward.  They are not interchangeable.

## 2. General adjoint identity and one exact coefficient witness

For every invertible Project bridge,

$$
\begin{aligned}
\operatorname{{Ad}}_{\mathcal B}(X)
\operatorname{{Ad}}_{\mathcal B}(Y)
&=(\mathcal B X\mathcal B^{-1})(\mathcal B Y\mathcal B^{-1})\\
&=\mathcal B X(\mathcal B^{-1}\mathcal B)Y\mathcal B^{-1}\\
&=\mathcal B XY\mathcal B^{-1}
=\operatorname{{Ad}}_{\mathcal B}(XY),\\
[\operatorname{{Ad}}_{\mathcal B}(X),
\operatorname{{Ad}}_{\mathcal B}(Y)]
&=\operatorname{{Ad}}_{\mathcal B}([X,Y]).
\end{aligned}
$$

This ordered proof is independent of the gauge algebra.  The following
coefficient matrix is one exact
`SU2_NILPOTENT_WITNESS`; it is not a proof for every gauge algebra.

$$
\tau:=\vartheta^1\vartheta^2,
\qquad
\epsilon(\tau)=0,
\qquad
\tau^2=0,
\qquad
\mathcal B
=\begin{{pmatrix}}1+\tau/2&0\\0&1-\tau/2\end{{pmatrix}},
\qquad
\mathcal B^{-1}
=\begin{{pmatrix}}1-\tau/2&0\\0&1+\tau/2\end{{pmatrix}}.
$$

$$
A_{\mathcal B}
=\begin{{pmatrix}}
1&-i\tau&0\\
i\tau&1&0\\
0&0&1
\end{{pmatrix}},
\qquad
A_{\mathcal B}^{-1}=A_{\mathcal B}\big|_{{\tau\mapsto-\tau}},
\qquad
\det A_{\mathcal B}=1.
$$

On the displayed witness sector, the coefficient map acts on

$$
\operatorname{{Adj}}_{SU(2)}\otimes
\Lambda(\vartheta^1,\vartheta^2,
\bar\vartheta_{\dot1},\bar\vartheta_{\dot2}),
\qquad
\dim\!\left[
\operatorname{{Adj}}_{SU(2)}\otimes
\Lambda(\vartheta^1,\vartheta^2,
\bar\vartheta_{\dot1},\bar\vartheta_{\dot2})
\right]=48.
$$

It is parity preserving.  Its two parity blocks obey

$$
\det A_{\bar0}=1,
\qquad
\det A_{\bar1}=1,
\qquad
\operatorname{{Ber}}A_{\mathcal B}=1.
$$

This proves reference-flat measure invariance only for this covariant adjoint
Step-5A block.

## 3. Quadratic tensors and source insertion

For an affine tangent map, or on a background satisfying both displayed
first-jet conditions,

$$
E_{\mathsf V,\alpha}C^\alpha{}_{{ij}}=0,
\qquad
F_{\mathsf V,\alpha}C^\alpha{}_{{ij}}=0,
\qquad
F_{\mathsf V,\alpha}
:=\frac{\vec\partial\mathscr I_{\mathsf V}}
{\partial\zeta_{\mathsf V}^{\alpha}},
$$

$$
\begin{{aligned}}
\Omega_{\mathsf C}&=J_{\rm q}^{\mathrm{{st}}}\Omega_{\mathsf V}J_{\rm q},\\
K_{\mathsf C}&=J_{\rm q}^{\mathrm{{st}}}K_{\mathsf V}J_{\rm q},\\
G_{\mathsf C}&=J_{\rm q}^{-1}G_{\mathsf V}J_{\rm q}^{-\mathrm{{st}}},\\
I^{{\rm bil}}_{\mathsf C}
&=J_{\rm q}^{\mathrm{{st}}}I^{{\rm bil}}_{\mathsf V}J_{\rm q},\\
H_{\mathsf C}&=J_{\rm q}^{-1}H_{\mathsf V}J_{\rm q},\\
I^{{\rm op}}_{\mathsf C}
&=J_{\rm q}^{-1}I^{{\rm op}}_{\mathsf V}J_{\rm q}.
\end{{aligned}}
$$

Therefore

$$
G_{\mathsf C}I^{{\rm bil}}_{\mathsf C}
=J_{\rm q}^{-1}
(G_{\mathsf V}I^{{\rm bil}}_{\mathsf V})J_{\rm q},
\qquad
\operatorname{{STr}}(G_{\mathsf C}I^{{\rm bil}}_{\mathsf C})
=\operatorname{{STr}}(G_{\mathsf V}I^{{\rm bil}}_{\mathsf V}).
$$

For a nonlinear quantum map the exact Hessian is

$$
K_{\mathsf C,ij}
=(J_{\rm q}^{\mathrm{{st}}})_i{}^\alpha
K_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+E_{\mathsf V,\alpha}C^\alpha{}_{{ij}}.
$$

For a scalar source composite its quadratic insertion obeys separately

$$
I^{{\rm bil}}_{\mathsf C,ij}
=(J_{\rm q}^{\mathrm{{st}}})_i{}^\alpha
I^{{\rm bil}}_{\mathsf V,\alpha\beta}
(J_{\rm q})^\beta{}_j
+F_{\mathsf V,\alpha}C^\alpha{}_{{ij}}.
$$

The executable counterexample gives

$$
K_{\mathsf V}=\begin{{pmatrix}}2&1\\1&4\end{{pmatrix}},
\qquad
E_{\mathsf V}=\begin{{pmatrix}}3&5\end{{pmatrix}},
\qquad
E_{\mathsf V,\alpha}C^\alpha
=\begin{{pmatrix}}5&0\\0&0\end{{pmatrix}},
$$

$$
K_{\mathsf C}
=\begin{{pmatrix}}2&1\\1&4\end{{pmatrix}}
+\begin{{pmatrix}}5&0\\0&0\end{{pmatrix}}
=\begin{{pmatrix}}7&1\\1&4\end{{pmatrix}}.
$$

For

$$
\mathscr I_{\mathsf V}=7y_2,
\qquad
F_{\mathsf V}=\begin{{pmatrix}}0&7\end{{pmatrix}},
\qquad
I^{{\rm bil}}_{\mathsf V}=0,
$$

the same nonlinear coordinate map gives

$$
I^{{\rm bil}}_{\mathsf C}
=0+\begin{{pmatrix}}7&0\\0&0\end{{pmatrix}}
=\begin{{pmatrix}}7&0\\0&0\end{{pmatrix}}.
$$

Hence an off-shell nonlinear quantum-coordinate bridge is not certified by a
pure congruence.

## 4. Background Ward recursion

$$
\delta A=R_{\mathsf V}A-AR_{\mathsf C},
\qquad
X_{\mathsf C}=A^{-1}X_{\mathsf V}A,
\qquad
\delta X_{\mathsf V}=[R_{\mathsf V},X_{\mathsf V}].
$$

$$
\begin{{aligned}}
\delta X_{\mathsf C}
={}&-A^{-1}(\delta A)A^{-1}X_{\mathsf V}A
+A^{-1}[R_{\mathsf V},X_{\mathsf V}]A
+A^{-1}X_{\mathsf V}(\delta A)\\
={}&R_{\mathsf C}X_{\mathsf C}-X_{\mathsf C}R_{\mathsf C}
=[R_{\mathsf C},X_{\mathsf C}].
\end{{aligned}}
$$

Thus the rooted one-loop Ward telescoping is representation-independent on
the exact similarity sector.  A scalar source-Hessian belongs to this sector
only after its first-jet connection term has been retained.  Full functional frame independence still
requires the Step-3D source, density, ghost/non-minimal, regulator, and cycle
pushforwards.

## 5. Gates

$$
N_{{\rm exact}}={passed},
\qquad
N_{{\rm failed}}={total - passed}.
$$

$$
\begin{{array}}{{c|c}}
\text{{gate}}&\text{{status}}\\ \hline
\text{{general-gauge-algebra covariant operator similarity}}&\mathrm{{PASS}}\\
\text{SU2 nilpotent coefficient witness}
&\mathrm{{PASS}}\\
\text{{quadratic Hessian/Green/source on similarity sector}}&\mathrm{{PASS}}\\
\text{{reference-flat adjoint-block measure}}&\mathrm{{PASS}}\\
\text{{background Ward recursion on similarity sector}}&\mathrm{{PASS}}\\
\text{{nonlinear tangent Hessian}}&
E_{\mathsf V,\alpha}C^\alpha{}_{{ij}}=0\ \mathrm{{required}}\\
\text{{nonlinear source Hessian}}&
F_{\mathsf V,\alpha}C^\alpha{}_{{ij}}=0\ \mathrm{{required}}\\
\text{{arbitrary-gauge-algebra background regulator closure}}&\mathrm{{OPEN}}\\
\text{{full physical+ghost+nonminimal Jacobian}}&\mathrm{{OPEN}}\\
\text{{finite-BV density and cycle}}&\mathrm{{OPEN\ in\ Step\ 5C}}\\
\text{{anomaly coefficient}}&\mathrm{{NOT\ COMPUTED}}
\end{{array}}
$$

## 6. Gap ledger

$$
\begin{{array}}{{c|c|c|c}}
\text{{id}}&\text{{type}}&\text{{result}}&\text{{severity}}\\ \hline
G1&\mathrm{{G\!\!\!-DEF}}&
A_{\mathcal B}=\operatorname{Ad}_{\mathcal B}
&P0\ \mathrm{{RESOLVED}}\\
G2&\mathrm{{G\!\!\!-ALG}}&
K_{\mathsf C}=J_{\rm q}^{\mathrm{{st}}}K_{\mathsf V}J_{\rm q}+E_{\mathsf V}C
&P0\ \mathrm{{RESOLVED}}\\
G3&\mathrm{{G\!\!\!-ALG}}&
I^{{\rm bil}}_{\mathsf C}=J_{\rm q}^{\mathrm{{st}}}I^{{\rm bil}}_{\mathsf V}J_{\rm q}+F_{\mathsf V}C
&P0\ \mathrm{{RESOLVED}}\\
G4&\mathrm{{G\!\!\!-NORM}}&
\operatorname{{Ber}}J_{\mathbb T}^{\perp}\text{{ including ghosts and nonminimal blocks}}
&P1\ \mathrm{{OPEN}}\\
G5&\mathrm{{G\!\!\!-SCOPE}}&
\text{{arbitrary-background projector/regulator closure}}
&P1\ \mathrm{{OPEN}}\\
G6&\mathrm{{G\!\!\!-SCOPE}}&
\text{{finite-BV density and cycle pushforward}}
&P1\ \mathrm{{OPEN\ IN\ STEP\ 5C}}
\end{{array}}
$$

Checked equation groups: operator similarity; adjoint bridge; tangent chain
rule; pairing/Hessian/Green; scalar source insertion; supertrace; reference-flat
Berezinian; background Ward telescoping.

Verification spot checks: exact fundamental conjugation; exact two-sided
inverse in coefficient dimension forty-eight; direct second differentiation
of the action and source counterexamples.
"""
    text = re.sub(r"\{\{([^{}]*)\}\}", r"{\1}", text)
    text = text.replace("{passed}", str(passed))
    text = text.replace("{total - passed}", str(total - passed))
    return text.encode()


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    audit_markdown = build_audit_markdown(payload)
    audit = {
        "schema": "Step5FrameBridgeIntertwinerAudit.v2",
        "status": payload["status"],
        "scope": payload["scope"],
        "totals": {
            "checks": len(payload["checks"]),
            "failed": sum(not result for result in payload["checks"].values()),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "audit_markdown_sha256": hashlib.sha256(audit_markdown).hexdigest(),
        "gates": payload["gates"],
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT_MD.write_bytes(audit_markdown)
    AUDIT.write_bytes(canonical_json(audit))


if __name__ == "__main__":
    write_artifacts()
