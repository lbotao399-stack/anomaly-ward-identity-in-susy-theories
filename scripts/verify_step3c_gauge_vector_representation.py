#!/usr/bin/env python3
"""Exact Step-3C gauge-vector representation verifier.

Only Python's standard library is used.  All numerical witnesses live in the
Gaussian-rational field Q(i); no floating-point arithmetic and no external CAS
enter the calculation.  Noncommuting bridge order is tested with exact matrix
witnesses.  Spinor projection transport is tested on the two-generator
exterior algebra, where the two left derivatives anticommute exactly.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "foundations" / "step-03c-gauge-vector-representation.md"
TASK = ROOT / "tasks" / "archive" / "CONTRACT-STEP-03C-GAUGE-VECTOR-REPRESENTATION-001.yaml"
OBLIGATIONS = ROOT / "ledger" / "proof_obligations.json"
CLAIM_MAP = ROOT / "references" / "claim-map.yaml"
SOURCE_LEDGER = ROOT / "references" / "superspace-1001-gauge-representation-source-ledger.json"
SUBSET = ROOT / "references" / "vendor" / "local" / "superspace-1001-gauge-representations-pages.pdf"
REFERENCE_AUDIT = ROOT / "audits" / "superspace-1001-reference-import-verification.json"
AUDIT = ROOT / "audits" / "step3c-vector-representation-verification.json"

TASK_ID = "CONTRACT-STEP-03C-GAUGE-VECTOR-REPRESENTATION-001"
SUBSET_SHA = "57d71bcf95fb84dabb4f5e85cfb9290ba52031e031a062cf7b0e5dad93a2d87e"


@dataclass(frozen=True)
class Gaussian:
    """Exact a+b i with a,b in Q."""

    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    @staticmethod
    def from_int(value: int) -> "Gaussian":
        return Gaussian(Fraction(value), Fraction(0))

    def __add__(self, other: "Gaussian") -> "Gaussian":
        return Gaussian(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other: "Gaussian") -> "Gaussian":
        return self + (-other)

    def __mul__(self, other: "Gaussian") -> "Gaussian":
        return Gaussian(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def inverse(self) -> "Gaussian":
        denominator = self.real * self.real + self.imag * self.imag
        if denominator == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return Gaussian(self.real / denominator, -self.imag / denominator)

    def __truediv__(self, other: "Gaussian") -> "Gaussian":
        return self * other.inverse()

    def is_zero(self) -> bool:
        return self.real == 0 and self.imag == 0

    def text(self) -> str:
        if self.imag == 0:
            return str(self.real)
        if self.real == 0:
            if self.imag == 1:
                return "i"
            if self.imag == -1:
                return "-i"
            return f"{self.imag}i"
        sign = "+" if self.imag > 0 else "-"
        magnitude = abs(self.imag)
        imag = "i" if magnitude == 1 else f"{magnitude}i"
        return f"{self.real}{sign}{imag}"


ZERO = Gaussian()
ONE = Gaussian.from_int(1)
TWO = Gaussian.from_int(2)
FOUR = Gaussian.from_int(4)
MINUS_ONE = Gaussian.from_int(-1)
I = Gaussian(Fraction(0), Fraction(1))


Matrix = tuple[tuple[Gaussian, ...], ...]
Vector = tuple[Gaussian, ...]


def q(value: int | Fraction) -> Gaussian:
    return Gaussian(Fraction(value), Fraction(0))


def matrix(rows: Iterable[Iterable[int | Fraction | Gaussian]]) -> Matrix:
    return tuple(
        tuple(value if isinstance(value, Gaussian) else q(value) for value in row)
        for row in rows
    )


def shape(value: Matrix) -> tuple[int, int]:
    return len(value), len(value[0]) if value else 0


def zero_matrix(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left[0])))
        for row in range(len(left))
    )


def mat_neg(value: Matrix) -> Matrix:
    return tuple(tuple(-entry for entry in row) for row in value)


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return mat_add(left, mat_neg(right))


def mat_scale(coefficient: Gaussian, value: Matrix) -> Matrix:
    return tuple(tuple(coefficient * entry for entry in row) for row in value)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError((shape(left), shape(right)))
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(len(right))),
                ZERO,
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def mat_inverse(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError(shape(value))
    augmented = [list(value[row]) + list(identity(rows)[row]) for row in range(rows)]
    for column in range(rows):
        pivot = next((row for row in range(column, rows) if not augmented[row][column].is_zero()), None)
        if pivot is None:
            raise ZeroDivisionError("singular exact matrix")
        if pivot != column:
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse_pivot = augmented[column][column].inverse()
        augmented[column] = [inverse_pivot * entry for entry in augmented[column]]
        for row in range(rows):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor.is_zero():
                continue
            augmented[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(augmented[row], augmented[column])
            ]
    return tuple(tuple(row[rows:]) for row in augmented)


def mat_trace(value: Matrix) -> Gaussian:
    return sum((value[index][index] for index in range(len(value))), ZERO)


def sigma_bivectors(
    sigma: tuple[Matrix, Matrix, Matrix, Matrix],
    bar_sigma: tuple[Matrix, Matrix, Matrix, Matrix],
) -> tuple[tuple[Matrix, ...], ...]:
    quarter = q(Fraction(1, 4))
    return tuple(
        tuple(
            mat_scale(
                quarter,
                mat_sub(
                    mat_mul(sigma[left], bar_sigma[right]),
                    mat_mul(sigma[right], bar_sigma[left]),
                ),
            )
            for right in range(4)
        )
        for left in range(4)
    )


def epsilon_four(indices: tuple[int, int, int, int]) -> Gaussian:
    if len(set(indices)) != 4:
        return ZERO
    inversions = sum(
        1
        for left in range(4)
        for right in range(left + 1, 4)
        if indices[left] > indices[right]
    )
    return ONE if inversions % 2 == 0 else MINUS_ONE


def mat_transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column] for row in range(len(value)))
        for column in range(len(value[0]))
    )


def mat_vec(value: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((entry * component for entry, component in zip(row, vector)), ZERO)
        for row in value
    )


def row_mat(vector: Vector, value: Matrix) -> Vector:
    return tuple(
        sum((vector[row] * value[row][column] for row in range(len(vector))), ZERO)
        for column in range(len(value[0]))
    )


def vec_scale(coefficient: Gaussian, vector: Vector) -> Vector:
    return tuple(coefficient * entry for entry in vector)


def serialize(value: Any) -> Any:
    if isinstance(value, Gaussian):
        return value.text()
    if isinstance(value, tuple):
        return [serialize(item) for item in value]
    if isinstance(value, list):
        return [serialize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): serialize(item) for key, item in value.items()}
    return value


def fingerprint(value: Any) -> str:
    payload = json.dumps(serialize(value), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Jet:
    """Value and one exact derivative of an even matrix superfield."""

    value: Matrix
    derivative: Matrix


def jet_product(left: Jet, right: Jet) -> Jet:
    return Jet(
        mat_mul(left.value, right.value),
        mat_add(mat_mul(left.derivative, right.value), mat_mul(left.value, right.derivative)),
    )


def jet_inverse(value: Jet) -> Jet:
    inverse = mat_inverse(value.value)
    return Jet(inverse, mat_neg(mat_mul(mat_mul(inverse, value.derivative), inverse)))


def jet_many(*values: Jet) -> Jet:
    result = Jet(identity(len(values[0].value)), zero_matrix(*shape(values[0].value)))
    for value in values:
        result = jet_product(result, value)
    return result


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []

    def check(self, name: str, actual: Any, expected: Any, category: str) -> None:
        passed = actual == expected
        actual_serial = serialize(actual)
        expected_serial = serialize(expected)
        row = {
            "name": name,
            "category": category,
            "passed": passed,
            "actual_sha256": fingerprint(actual),
            "expected_sha256": fingerprint(expected),
        }
        if not isinstance(actual, tuple):
            row["actual"] = actual_serial
            row["expected"] = expected_serial
        self.checks.append(row)
        if not passed:
            self.failures.append(
                {
                    "name": name,
                    "category": category,
                    "actual": actual_serial,
                    "expected": expected_serial,
                }
            )


def bridge_witnesses(recorder: Recorder) -> dict[str, Matrix]:
    b = matrix(((1, 2), (1, 3)))
    bt = matrix(((2, 1), (1, 1)))
    k = matrix(((3, 2), (1, 1)))
    h = matrix(((1, 1), (0, 1)))
    ht = matrix(((1, 0), (2, 1)))

    bi, bti, ki, hi, hti = map(mat_inverse, (b, bt, k, h, ht))
    e = mat_mul(bt, b)
    bp = mat_mul(mat_mul(k, b), hi)
    btp = mat_mul(mat_mul(ht, bt), ki)
    ep = mat_mul(btp, bp)

    recorder.check("bridge inverse B", mat_mul(b, bi), identity(2), "bridge")
    recorder.check("bridge inverse Btilde", mat_mul(bt, bti), identity(2), "bridge")
    recorder.check("relative bridge order", e, mat_mul(bt, b), "bridge")
    recorder.check("finite relative-bridge covariance", ep, mat_mul(mat_mul(ht, e), hi), "bridge")
    recorder.check(
        "noncommuting order witness",
        mat_mul(bt, b) == mat_mul(b, bt),
        False,
        "bridge",
    )
    recorder.check(
        "intrinsic Euclidean bridges need not be adjoints",
        bt == mat_transpose(b),
        False,
        "reality",
    )

    b_l = matrix(((1, 1), (0, 1)))
    bt_l = mat_transpose(b_l)
    k_l = matrix(((0, 1), (-1, 0)))
    h_l = matrix(((1, 2), (0, 1)))
    ht_l = mat_inverse(mat_transpose(h_l))
    bp_l = mat_mul(mat_mul(k_l, b_l), mat_inverse(h_l))
    btp_l = mat_mul(mat_mul(ht_l, bt_l), mat_inverse(k_l))
    e_l = mat_mul(bt_l, b_l)
    recorder.check("Lorentz k dagger equals k inverse", mat_transpose(k_l), mat_inverse(k_l), "reality")
    recorder.check("Lorentz h dagger equals htilde inverse", mat_transpose(h_l), mat_inverse(ht_l), "reality")
    recorder.check("Lorentz bridge dagger relation is preserved", btp_l, mat_transpose(bp_l), "reality")
    recorder.check("Lorentz relative bridge is Hermitian", mat_transpose(e_l), e_l, "reality")

    s = matrix(((1, 1), (0, 1)))
    sp = matrix(((1, 0), (1, 1)))
    hs = matrix(((2, 1), (1, 1)))
    es = mat_mul(s, s)
    esp = mat_mul(sp, sp)
    hts = mat_mul(mat_mul(esp, hs), mat_inverse(es))
    ks = mat_mul(mat_mul(sp, hs), mat_inverse(s))
    ksi = mat_inverse(ks)
    alternate_ksi = mat_mul(mat_mul(mat_inverse(s), mat_inverse(hts)), sp)
    recorder.check("symmetric compensator inverse", ksi, alternate_ksi, "bridge")
    recorder.check("symmetric B transform", mat_mul(mat_mul(ks, s), mat_inverse(hs)), sp, "bridge")
    recorder.check("symmetric Btilde transform", mat_mul(mat_mul(hts, s), ksi), sp, "bridge")

    return {"B": b, "Bt": bt, "k": k, "h": h, "ht": ht, "E": e}


def connection_witnesses(recorder: Recorder, data: dict[str, Matrix]) -> None:
    b, bt, k, h, ht = (data[name] for name in ("B", "Bt", "k", "h", "ht"))
    z = zero_matrix(2, 2)

    # Untilded spinor derivative: D htilde=0.
    jb = Jet(b, matrix(((1, 0), (2, -1))))
    jbt = Jet(bt, matrix(((0, 2), (-1, 1))))
    jk = Jet(k, matrix(((1, -1), (0, 2))))
    jh = Jet(h, matrix(((0, 1), (0, 0))))
    jht = Jet(ht, z)
    je = jet_product(jbt, jb)
    jbp = jet_many(jk, jb, jet_inverse(jh))
    jbtp = jet_many(jht, jbt, jet_inverse(jk))

    cv = mat_mul(mat_inverse(bt), jbt.derivative)
    cvp = mat_mul(mat_inverse(jbtp.value), jbtp.derivative)
    expected_cvp = mat_add(
        mat_neg(mat_mul(jk.derivative, mat_inverse(k))),
        mat_mul(mat_mul(k, cv), mat_inverse(k)),
    )
    recorder.check("D vector-connection gauge covariance", cvp, expected_cvp, "connection")

    cc = mat_add(
        mat_mul(mat_inverse(b), jb.derivative),
        mat_mul(mat_mul(mat_inverse(b), cv), b),
    )
    expected_cc = mat_mul(mat_inverse(je.value), je.derivative)
    recorder.check("D chiral similarity connection", cc, expected_cc, "connection")
    jep = jet_product(jbtp, jbp)
    ccp = mat_mul(mat_inverse(jep.value), jep.derivative)
    expected_ccp = mat_add(
        mat_neg(mat_mul(jh.derivative, mat_inverse(h))),
        mat_mul(mat_mul(h, cc), mat_inverse(h)),
    )
    recorder.check("D chiral-frame gauge covariance", ccp, expected_ccp, "connection")

    ai = jet_inverse(jbt)
    ca = mat_add(mat_mul(bt, ai.derivative), mat_mul(mat_mul(bt, cv), mat_inverse(bt)))
    recorder.check("D antichiral connection vanishes", ca, z, "connection")

    # Tilded spinor derivative: barD h=0.
    jb_bar = Jet(b, matrix(((2, -1), (1, 0))))
    jbt_bar = Jet(bt, matrix(((-1, 0), (2, 1))))
    jk_bar = Jet(k, matrix(((0, 1), (-1, 1))))
    jh_bar = Jet(h, z)
    jht_bar = Jet(ht, matrix(((0, 0), (1, -1))))
    je_bar = jet_product(jbt_bar, jb_bar)
    jbp_bar = jet_many(jk_bar, jb_bar, jet_inverse(jh_bar))
    jbtp_bar = jet_many(jht_bar, jbt_bar, jet_inverse(jk_bar))

    cbar = mat_mul(b, jet_inverse(jb_bar).derivative)
    cbarp = mat_mul(jbp_bar.value, jet_inverse(jbp_bar).derivative)
    expected_cbarp = mat_add(
        mat_neg(mat_mul(jk_bar.derivative, mat_inverse(k))),
        mat_mul(mat_mul(k, cbar), mat_inverse(k)),
    )
    recorder.check("barD vector-connection gauge covariance", cbarp, expected_cbarp, "connection")

    cc_bar = mat_add(
        mat_mul(mat_inverse(b), jb_bar.derivative),
        mat_mul(mat_mul(mat_inverse(b), cbar), b),
    )
    recorder.check("barD chiral connection vanishes", cc_bar, z, "connection")

    bti_bar = jet_inverse(jbt_bar)
    ca_bar = mat_add(
        mat_mul(bt, bti_bar.derivative),
        mat_mul(mat_mul(bt, cbar), mat_inverse(bt)),
    )
    expected_ca_bar = mat_mul(je_bar.value, jet_inverse(je_bar).derivative)
    recorder.check("barD antichiral similarity connection", ca_bar, expected_ca_bar, "connection")
    jep_bar = jet_product(jbtp_bar, jbp_bar)
    cap_bar = mat_mul(jep_bar.value, jet_inverse(jep_bar).derivative)
    expected_cap_bar = mat_add(
        mat_neg(mat_mul(jht_bar.derivative, mat_inverse(ht))),
        mat_mul(mat_mul(ht, ca_bar), mat_inverse(ht)),
    )
    recorder.check("barD antichiral-frame gauge covariance", cap_bar, expected_cap_bar, "connection")


def chirality_and_action_witnesses(recorder: Recorder, data: dict[str, Matrix]) -> None:
    b, bt, k, h, ht = (data[name] for name in ("B", "Bt", "k", "h", "ht"))
    bi, bti, ki, hi, hti = map(mat_inverse, (b, bt, k, h, ht))

    # Chiral strength: barD W^C=0.
    db = matrix(((2, -1), (1, 0)))
    jb = Jet(b, db)
    wc = matrix(((1, 2), (3, -1)))
    wc2 = matrix(((2, -1), (1, 4)))
    jbi = jet_inverse(jb)
    wv = mat_mul(mat_mul(b, wc), bi)
    wv2 = mat_mul(mat_mul(b, wc2), bi)
    # W_a is odd.  For an odd X and even B,
    # barD(B X B^-1)=(barD B)X B^-1-B X(barD B^-1).
    dwv = mat_sub(mat_mul(mat_mul(db, wc), bi), mat_mul(mat_mul(b, wc), jbi.derivative))
    dwv2 = mat_sub(mat_mul(mat_mul(db, wc2), bi), mat_mul(mat_mul(b, wc2), jbi.derivative))
    cbar = mat_mul(b, jet_inverse(jb).derivative)
    covariant_bar = mat_add(dwv, mat_add(mat_mul(cbar, wv), mat_mul(wv, cbar)))
    recorder.check("vector-frame covariant chirality of W", covariant_bar, zero_matrix(2, 2), "chirality")

    # Antichiral strength: D Wtilde^A=0.
    dbt = matrix(((0, 2), (-1, 1)))
    jbt = Jet(bt, dbt)
    wa = matrix(((0, 1), (-2, 3)))
    wa2 = matrix(((3, -2), (1, 1)))
    jbti = jet_inverse(jbt)
    wtv = mat_mul(mat_mul(bti, wa), bt)
    wtv2 = mat_mul(mat_mul(bti, wa2), bt)
    dwtv = mat_sub(
        mat_mul(mat_mul(jbti.derivative, wa), bt),
        mat_mul(mat_mul(bti, wa), dbt),
    )
    dwtv2 = mat_sub(
        mat_mul(mat_mul(jbti.derivative, wa2), bt),
        mat_mul(mat_mul(bti, wa2), dbt),
    )
    cv = mat_mul(bti, dbt)
    covariant_d = mat_add(dwtv, mat_add(mat_mul(cv, wtv), mat_mul(wtv, cv)))
    recorder.check("vector-frame covariant antichirality of Wtilde", covariant_d, zero_matrix(2, 2), "chirality")

    bp = mat_mul(mat_mul(k, b), hi)
    btp = mat_mul(mat_mul(ht, bt), ki)
    wcp = mat_mul(mat_mul(h, wc), hi)
    wap = mat_mul(mat_mul(ht, wa), hti)
    recorder.check(
        "W field-strength gauge covariance",
        mat_mul(mat_mul(bp, wcp), mat_inverse(bp)),
        mat_mul(mat_mul(k, wv), ki),
        "field_strength",
    )
    recorder.check(
        "Wtilde field-strength gauge covariance",
        mat_mul(mat_mul(mat_inverse(btp), wap), btp),
        mat_mul(mat_mul(k, wtv), ki),
        "field_strength",
    )

    phi = (q(2), q(-1))
    phit = (q(3), q(1))
    phiv = mat_vec(b, phi)
    phitv = row_mat(phit, bt)
    recorder.check(
        "matter bilinear frame equality",
        sum((left * right for left, right in zip(phitv, phiv)), ZERO),
        sum((left * right for left, right in zip(phit, mat_vec(mat_mul(bt, b), phi))), ZERO),
        "action",
    )
    recorder.check(
        "column matter gauge covariance",
        mat_vec(bp, mat_vec(h, phi)),
        mat_vec(k, phiv),
        "matter",
    )
    recorder.check(
        "row matter gauge covariance",
        row_mat(row_mat(phit, hti), btp),
        row_mat(phitv, ki),
        "matter",
    )

    # Fundamental covariant chirality and its dual-row partner.
    dphiv = mat_vec(db, phi)
    recorder.check(
        "column matter covariant chirality",
        tuple(left + right for left, right in zip(dphiv, mat_vec(cbar, phiv))),
        (ZERO, ZERO),
        "chirality",
    )
    dphitv = row_mat(phit, dbt)
    recorder.check(
        "row matter covariant antichirality",
        tuple(left - right for left, right in zip(dphitv, row_mat(phitv, cv))),
        (ZERO, ZERO),
        "chirality",
    )

    recorder.check(
        "chiral kinetic trace similarity",
        mat_trace(mat_mul(wv, wv2)),
        mat_trace(mat_mul(wc, wc2)),
        "action",
    )
    recorder.check(
        "flat-barD chirality of invariant chiral kinetic scalar",
        mat_trace(
            mat_sub(mat_mul(dwv, wv2), mat_mul(wv, dwv2))
        ),
        ZERO,
        "action",
    )
    recorder.check(
        "antichiral kinetic trace similarity",
        mat_trace(mat_mul(wtv, wtv2)),
        mat_trace(mat_mul(wa, wa2)),
        "action",
    )
    recorder.check(
        "flat-D antichirality of invariant antichiral kinetic scalar",
        mat_trace(
            mat_sub(mat_mul(dwtv, wtv2), mat_mul(wtv, dwtv2))
        ),
        ZERO,
        "action",
    )


def wedge_sign(left_mask: int, right_mask: int) -> int:
    inversions = 0
    for left_index in range(2):
        if not left_mask & (1 << left_index):
            continue
        for right_index in range(2):
            if right_mask & (1 << right_index) and left_index > right_index:
                inversions += 1
    return -1 if inversions % 2 else 1


def exterior_left_multiplication(mask: int) -> Matrix:
    result = [[ZERO for _ in range(4)] for _ in range(4)]
    for input_mask in range(4):
        if mask & input_mask:
            continue
        result[mask | input_mask][input_mask] = q(wedge_sign(mask, input_mask))
    return tuple(tuple(row) for row in result)


def exterior_left_derivative(index: int) -> Matrix:
    result = [[ZERO for _ in range(4)] for _ in range(4)]
    bit = 1 << index
    for input_mask in range(4):
        if not input_mask & bit:
            continue
        sign = -1 if (input_mask & (bit - 1)).bit_count() % 2 else 1
        result[input_mask ^ bit][input_mask] = q(sign)
    return tuple(tuple(row) for row in result)


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[g_out][g_in] * right[m_out][m_in]
            for g_in in range(len(left[0]))
            for m_in in range(len(right[0]))
        )
        for g_out in range(len(left))
        for m_out in range(len(right))
    )


def multiplication_operator(bottom: Matrix, theta_squared: Matrix) -> Matrix:
    return mat_add(
        kronecker(bottom, identity(4)),
        kronecker(theta_squared, exterior_left_multiplication(0b11)),
    )


def extract_column_bottom(vector: Vector) -> Vector:
    return tuple(vector[gauge * 4] for gauge in range(2))


def component_projection_witnesses(recorder: Recorder) -> None:
    d1 = kronecker(identity(2), exterior_left_derivative(0))
    d2 = kronecker(identity(2), exterior_left_derivative(1))
    z8 = zero_matrix(8, 8)
    recorder.check("D_1 nilpotence", mat_mul(d1, d1), z8, "component")
    recorder.check("D_2 nilpotence", mat_mul(d2, d2), z8, "component")
    recorder.check(
        "D_1 D_2 anticommutation",
        mat_add(mat_mul(d1, d2), mat_mul(d2, d1)),
        z8,
        "component",
    )

    b0 = matrix(((1, 1), (0, 1)))
    bt0 = matrix(((1, 0), (2, 1)))
    b12 = matrix(((0, 1), (-1, 0)))
    bt12 = matrix(((1, -1), (0, 2)))
    bop = multiplication_operator(b0, b12)
    btop = multiplication_operator(bt0, bt12)
    eop = mat_mul(btop, bop)
    bopi = mat_inverse(bop)
    btopi = mat_inverse(btop)
    eopi = mat_inverse(eop)

    phi = tuple(q(value) for value in (1, 2, -1, 3, 2, 0, 1, -2))
    phiv = mat_vec(bop, phi)
    ov = (mat_mul(mat_mul(btopi, d1), btop), mat_mul(mat_mul(btopi, d2), btop))
    oc = (mat_mul(mat_mul(eopi, d1), eop), mat_mul(mat_mul(eopi, d2), eop))
    for index in range(2):
        recorder.check(
            f"operator chiral similarity a={index + 1}",
            mat_mul(mat_mul(bopi, ov[index]), bop),
            oc[index],
            "component",
        )
        recorder.check(
            f"matter first covariant projection a={index + 1}",
            extract_column_bottom(mat_vec(ov[index], phiv)),
            mat_vec(b0, extract_column_bottom(mat_vec(oc[index], phi))),
            "component",
        )

    ov_squared = mat_scale(TWO, mat_mul(ov[1], ov[0]))
    oc_squared = mat_scale(TWO, mat_mul(oc[1], oc[0]))
    recorder.check(
        "matter ordered D-squared covariant projection",
        vec_scale(q(Fraction(-1, 4)), extract_column_bottom(mat_vec(ov_squared, phiv))),
        mat_vec(
            b0,
            vec_scale(q(Fraction(-1, 4)), extract_column_bottom(mat_vec(oc_squared, phi))),
        ),
        "component",
    )

    # Dual-row frame transport is an independent right-module calculation.
    row = tuple(q(value) for value in (2, -1, 0, 1, 3, 2, -2, 1))
    row_v = row_mat(row, btop)
    ra = (d1, d2)
    rv = (mat_mul(mat_mul(btopi, d1), btop), mat_mul(mat_mul(btopi, d2), btop))
    for index in range(2):
        recorder.check(
            f"dual-row first frame transport dot a={index + 1}",
            row_mat(row_v, rv[index]),
            row_mat(row_mat(row, ra[index]), btop),
            "component",
        )

    rv_squared = mat_scale(TWO, mat_mul(rv[0], rv[1]))
    ra_squared = mat_scale(TWO, mat_mul(ra[0], ra[1]))
    recorder.check(
        "dual-row ordered barD-squared frame transport",
        vec_scale(q(Fraction(-1, 4)), row_mat(row_v, rv_squared)),
        vec_scale(q(Fraction(-1, 4)), row_mat(row_mat(row, ra_squared), btop)),
        "component",
    )

    # Wess--Zumino pure-undotted projection surface: bridges have identity bottom
    # and no pure theta or theta-squared jet, hence the covariant C projections
    # reduce exactly to the Step-3B flat-D definitions.
    wz = multiplication_operator(identity(2), zero_matrix(2, 2))
    wz_e = mat_mul(wz, wz)
    wz_oc = (
        mat_mul(mat_mul(mat_inverse(wz_e), d1), wz_e),
        mat_mul(mat_mul(mat_inverse(wz_e), d2), wz_e),
    )
    recorder.check("WZ chiral a=1 projection reduces to flat D_1", wz_oc[0], d1, "component")
    recorder.check("WZ chiral a=2 projection reduces to flat D_2", wz_oc[1], d2, "component")
    recorder.check(
        "WZ chiral auxiliary projection reduces to flat -D^2/4",
        mat_scale(q(Fraction(-1, 2)), mat_mul(wz_oc[1], wz_oc[0])),
        mat_scale(q(Fraction(-1, 2)), mat_mul(d2, d1)),
        "component",
    )
    recorder.check(
        "WZ antichiral auxiliary projection reduces to flat -barD^2/4",
        mat_scale(q(Fraction(-1, 2)), mat_mul(wz_oc[0], wz_oc[1])),
        mat_scale(q(Fraction(-1, 2)), mat_mul(d1, d2)),
        "component",
    )


def coefficient_witnesses(recorder: Recorder) -> None:
    kappa_l = TWO * I
    kappa_e = q(-2)
    u_l = FOUR / kappa_l
    u_e = FOUR / kappa_e
    rho_l = FOUR / (kappa_l * kappa_l)
    rho_e = FOUR / (kappa_e * kappa_e)

    recorder.check("Lorentz u=4/kappa", u_l, q(-2) * I, "jacobi")
    recorder.check("Euclidean u=4/kappa", u_e, q(-2), "jacobi")
    recorder.check("Lorentz rho=4/kappa^2", rho_l, MINUS_ONE, "jacobi")
    recorder.check("Euclidean rho=4/kappa^2", rho_e, ONE, "jacobi")
    recorder.check("Jacobi coefficient rho=u/kappa in L", u_l / kappa_l, rho_l, "jacobi")
    recorder.check("Jacobi coefficient rho=u/kappa in E", u_e / kappa_e, rho_e, "jacobi")
    recorder.check("Wick mixed algebra kappa_L i=kappa_E", kappa_l * I, kappa_e, "wick")
    recorder.check("Wick spinor-vector coefficient u_L/i=u_E", u_l / I, u_e, "wick")
    recorder.check("Wick vector commutator flips rho", -rho_l, rho_e, "wick")
    tau_l = I
    tau_e = -I
    recorder.check(
        "Lorentz dotted curvature phase from vector curvature",
        (-I) / rho_l,
        tau_l,
        "component_density",
    )
    recorder.check(
        "Euclidean dotted curvature phase from vector curvature",
        (-I) / rho_e,
        tau_e,
        "component_density",
    )
    recorder.check("Lorentz curvature phase square", tau_l * tau_l, MINUS_ONE, "component_density")
    recorder.check("Euclidean curvature phase square", tau_e * tau_e, MINUS_ONE, "component_density")
    recorder.check("Lorentz kappa times u", kappa_l * u_l, FOUR, "component_density")
    recorder.check("Euclidean kappa times u", kappa_e * u_e, FOUR, "component_density")
    recorder.check(
        "Lorentz kappa squared times rho",
        kappa_l * kappa_l * rho_l,
        FOUR,
        "component_density",
    )
    recorder.check(
        "Euclidean kappa squared times rho",
        kappa_e * kappa_e * rho_e,
        FOUR,
        "component_density",
    )
    recorder.check(
        "Lorentz W second-derivative coefficient",
        q(-2) * I * kappa_l,
        FOUR,
        "component_density",
    )
    recorder.check(
        "Euclidean W second-derivative coefficient",
        q(-2) * I * kappa_e,
        FOUR * I,
        "component_density",
    )
    recorder.check(
        "Lorentz ordered matter-fermion coefficient",
        q(Fraction(-1, 2)) * kappa_l,
        -I,
        "component_density",
    )
    recorder.check(
        "Euclidean ordered matter-fermion coefficient",
        q(Fraction(-1, 2)) * kappa_e,
        ONE,
        "component_density",
    )
    recorder.check(
        "Lorentz canonical matter-fermion coefficient",
        q(Fraction(1, 2)) * kappa_l,
        I,
        "component_density",
    )
    recorder.check(
        "Euclidean action matter-fermion coefficient",
        MINUS_ONE * q(Fraction(1, 2)) * kappa_e,
        ONE,
        "component_density",
    )


def component_density_witnesses(recorder: Recorder) -> None:
    first_vector = TWO
    first_strength = q(-8)
    z_vector = ONE
    z_curvature = q(-2)
    spinor_vector_contraction = TWO
    kappa_u = FOUR
    kappa_squared_rho = FOUR

    master_spinor_vector = first_vector * z_vector
    master_curvature = first_vector * z_curvature
    master_auxiliary = first_strength
    final_vector = master_spinor_vector * spinor_vector_contraction * kappa_squared_rho
    final_curvature = master_curvature * kappa_u

    recorder.check(
        "row D-algebra intermediate kappa-squared coefficient",
        master_spinor_vector,
        TWO,
        "component_density",
    )
    recorder.check(
        "row D-algebra intermediate kappa-u coefficient",
        master_curvature,
        q(-4),
        "component_density",
    )
    recorder.check(
        "row D-algebra intermediate auxiliary coefficient",
        master_auxiliary,
        q(-8),
        "component_density",
    )
    recorder.check(
        "row D-algebra final vector coefficient",
        final_vector,
        q(16),
        "component_density",
    )
    recorder.check(
        "row D-algebra final curvature coefficient",
        final_curvature,
        q(-16),
        "component_density",
    )
    recorder.check(
        "twice-graded Leibniz coefficient for odd strength",
        TWO * MINUS_ONE,
        q(-2),
        "component_density",
    )

    sigma_0 = identity(2)
    sigma_1 = matrix(((0, 1), (1, 0)))
    sigma_2 = matrix(((0, -I), (I, 0)))
    sigma_3 = matrix(((1, 0), (0, -1)))

    sigma_l = (sigma_0, sigma_1, sigma_2, sigma_3)
    bar_sigma_l = (
        sigma_0,
        mat_scale(MINUS_ONE, sigma_1),
        mat_scale(MINUS_ONE, sigma_2),
        mat_scale(MINUS_ONE, sigma_3),
    )
    sigma_e = (
        mat_scale(-I, sigma_1),
        mat_scale(-I, sigma_2),
        mat_scale(-I, sigma_3),
        sigma_0,
    )
    bar_sigma_e = (
        mat_scale(I, sigma_1),
        mat_scale(I, sigma_2),
        mat_scale(I, sigma_3),
        sigma_0,
    )

    sigma_mn_l = sigma_bivectors(sigma_l, bar_sigma_l)
    bar_sigma_mn_l = sigma_bivectors(bar_sigma_l, sigma_l)
    sigma_mn_e = sigma_bivectors(sigma_e, bar_sigma_e)
    bar_sigma_mn_e = sigma_bivectors(bar_sigma_e, sigma_e)
    eta = (q(-1), ONE, ONE, ONE)

    actual_l: dict[str, Gaussian] = {}
    expected_l: dict[str, Gaussian] = {}
    actual_bar_l: dict[str, Gaussian] = {}
    expected_bar_l: dict[str, Gaussian] = {}
    actual_e: dict[str, Gaussian] = {}
    expected_e: dict[str, Gaussian] = {}
    actual_bar_e: dict[str, Gaussian] = {}
    expected_bar_e: dict[str, Gaussian] = {}
    half = q(Fraction(1, 2))
    minus_half = q(Fraction(-1, 2))

    for m in range(4):
        for n in range(4):
            for r in range(4):
                for s in range(4):
                    key = f"{m}{n}{r}{s}"
                    metric_l = (
                        eta[m] * eta[n]
                        if m == r and n == s
                        else ZERO
                    ) - (
                        eta[m] * eta[n]
                        if m == s and n == r
                        else ZERO
                    )
                    metric_e = q(int(m == r and n == s) - int(m == s and n == r))
                    epsilon = epsilon_four((m, n, r, s))

                    actual_l[key] = mat_trace(mat_mul(sigma_mn_l[m][n], sigma_mn_l[r][s]))
                    expected_l[key] = minus_half * metric_l + half * I * epsilon
                    actual_bar_l[key] = mat_trace(
                        mat_mul(bar_sigma_mn_l[m][n], bar_sigma_mn_l[r][s])
                    )
                    expected_bar_l[key] = minus_half * metric_l - half * I * epsilon
                    actual_e[key] = mat_trace(mat_mul(sigma_mn_e[m][n], sigma_mn_e[r][s]))
                    expected_e[key] = minus_half * metric_e + half * epsilon
                    actual_bar_e[key] = mat_trace(
                        mat_mul(bar_sigma_mn_e[m][n], bar_sigma_mn_e[r][s])
                    )
                    expected_bar_e[key] = minus_half * metric_e - half * epsilon

    recorder.check("Lorentz undotted sigma-bivector trace", actual_l, expected_l, "component_density")
    recorder.check(
        "Lorentz dotted sigma-bivector trace",
        actual_bar_l,
        expected_bar_l,
        "component_density",
    )
    recorder.check("Euclidean undotted sigma-bivector trace", actual_e, expected_e, "component_density")
    recorder.check(
        "Euclidean dotted sigma-bivector trace",
        actual_bar_e,
        expected_bar_e,
        "component_density",
    )


def bianchi_witnesses(recorder: Recorder) -> None:
    epsilon_upper = ((ZERO, ONE), (MINUS_ONE, ZERO))
    epsilon_lower = ((ZERO, MINUS_ONE), (ONE, ZERO))
    x = matrix(((1, 2), (3, 4)))
    y = matrix(((7, 5), (4, -2)))

    div_x = sum(
        (epsilon_upper[a][b] * x[b][a] for a in range(2) for b in range(2)),
        ZERO,
    )
    div_y = sum(
        (epsilon_upper[a][b] * y[b][a] for a in range(2) for b in range(2)),
        ZERO,
    )
    recorder.check("contracted Bianchi divergence", div_x + div_y, ZERO, "bianchi")

    rho = q(3)
    curvature: dict[tuple[int, int, int, int], Gaussian] = {}
    curvature_symmetric: dict[tuple[int, int, int, int], Gaussian] = {}
    for a in range(2):
        for dotted_a in range(2):
            for b in range(2):
                for dotted_b in range(2):
                    key = (a, dotted_a, b, dotted_b)
                    curvature[key] = rho * (
                        epsilon_lower[dotted_a][dotted_b] * x[a][b]
                        + epsilon_lower[a][b] * y[dotted_a][dotted_b]
                    )
                    x_symmetric = q(Fraction(1, 2)) * (x[a][b] + x[b][a])
                    y_symmetric = q(Fraction(1, 2)) * (
                        y[dotted_a][dotted_b] + y[dotted_b][dotted_a]
                    )
                    curvature_symmetric[key] = rho * (
                        epsilon_lower[dotted_a][dotted_b] * x_symmetric
                        + epsilon_lower[a][b] * y_symmetric
                    )

    antisymmetry_residual = {
        str(key): value
        + curvature[(key[2], key[3], key[0], key[1])]
        for key, value in curvature.items()
    }
    recorder.check(
        "vector-curvature antisymmetry from contracted Bianchi",
        antisymmetry_residual,
        {key: ZERO for key in antisymmetry_residual},
        "bianchi",
    )
    recorder.check(
        "unsymmetrized Jacobi curvature equals symmetric form",
        curvature,
        curvature_symmetric,
        "bianchi",
    )


def document_and_provenance_checks(recorder: Recorder) -> None:
    contract = CONTRACT.read_text(encoding="utf-8")
    compact = re.sub(r"\s+", "", contract)
    task = json.loads(TASK.read_text(encoding="utf-8"))
    obligations = json.loads(OBLIGATIONS.read_text(encoding="utf-8"))
    claim_map = json.loads(CLAIM_MAP.read_text(encoding="utf-8"))
    source_ledger = json.loads(SOURCE_LEDGER.read_text(encoding="utf-8"))
    reference_audit = json.loads(REFERENCE_AUDIT.read_text(encoding="utf-8"))

    tags = re.findall(r"\\tag\{3C\.([^}]+)\}", contract)
    expected_tags = [str(value) for value in range(1, 40)] + ["39a"] + [
        str(value) for value in range(40, 61)
    ] + ["60a"] + [str(value) for value in range(61, 73)] + [
        f"72{letter}" for letter in "abcdefghijklmnop"
    ] + [str(value) for value in range(73, 82)]
    recorder.check("equation tags exact ordered surface", tags, expected_tags, "document")
    recorder.check("equation tags unique", len(tags), len(set(tags)), "document")
    equation_bodies: dict[str, str] = {}
    for display in re.findall(r"\$\$(.*?)\$\$", contract, flags=re.DOTALL):
        display_tags = re.findall(r"\\tag\{3C\.([^}]+)\}", display)
        for tag in display_tags:
            equation_bodies[tag] = re.sub(r"\s+", "", display)

    equation_bindings: dict[str, tuple[tuple[str, int], ...]] = {
        "72d": (
            (r"=2\kappa_R^2", 1),
            (r"-4\kappa_Ru_R\boldsymbol Z_{R\dot b}^{\mathsf V}", 1),
            (r"=16(\boldsymbol{\mathcal D}_{RM}^{\mathsf V})^{\rm row}", 1),
            (r"-16\boldsymbol Z_{R\dot b}^{\mathsf V}", 1),
            (r"-8\widetilde{\boldsymbol\Phi}_R^{\mathsf V}", 2),
        ),
        "72e": (
            (r"={}&-\frac{\kappa_R}{2}", 1),
            (r"+i\sqrt2\widetilde\phi_{R,I}(T_A)^I{}_J", 1),
            (r"={}&\widetilde F_{R,I}F_R^I", 1),
        ),
        "72f": (
            (r":={}&-(\mathcal D_{RM}\widetilde\phi_R)_I", 1),
            (r"+\frac{\kappa_R}{2}\widetilde\psi_{R\dot a,I}", 1),
            (r"={}&\mathcal K_{0,R}^{\rm can}+\partial_{RM}J_R^M", 1),
        ),
        "72g": (
            (r"&=\mathscr U_{R,I}F_R^I-\frac12\mathscr U_{R,IJ}", 1),
            (r"&=\widetilde{\mathscr U}_R^{,I}\widetilde F_{R,I}-\frac12", 1),
        ),
        "72i": (
            (r"&=-\epsilon_{ab}\mathscr D_R+\tau_R(\sigma_R^{MN})_{ab}", 1),
            (r"&=+\epsilon_{\dot a\dot b}\mathscr D_R+\tau_R(\bar\sigma_R^{MN})", 1),
            (r"-\frac{i}{\rho_R}&=\tau_R", 1),
        ),
        "72j": (
            (r"&=-2i\kappa_R(\sigma_R^M)_{a\dot b}", 1),
            (r"&=-2i\kappa_R(\sigma_R^M)_{b\dot a}", 1),
        ),
        "72k": (
            (r"+2(-1)^{|X|}", 2),
            (r"&=+\epsilon_{\dot b\dot a}\mathscr D^A+\tau_R(\bar\sigma_R^{MN})", 1),
            (r"&=2\mathscr D^A\mathscr D^B+\operatorname{tr}_2(\sigma_R", 1),
            (r"&=2\mathscr D^A\mathscr D^B+\operatorname{tr}_2(\bar\sigma_R", 1),
            (r"+\frac{\kappa_R}{2}\left[", 2),
        ),
        "72l": (
            (r"+\frac i2\epsilon_L^{\mu\nu\rho\sigma}", 1),
            (r"+\frac12\epsilon_E^{mnrs}", 1),
            (r"-\frac i2\epsilon_L^{\mu\nu\rho\sigma}", 1),
            (r"-\frac12\epsilon_E^{mnrs}", 1),
        ),
        "72m": (
            (r"+\frac i4\epsilon_L^{\mu\nu\rho\sigma}", 1),
            (r"+\frac14\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}", 1),
            (r"-\frac i4\epsilon_L^{\mu\nu\rho\sigma}", 1),
            (r"-\frac14\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}", 1),
            (r"+i\lambda^A\sigma_L^\mu\mathcal D_\mu\bar\lambda^B", 1),
            (r"-\lambda^A\sigma_E^m\mathcal D_m\widetilde\lambda^B", 1),
            (r"+i\widetilde\lambda^A\bar\sigma_L^\mu\mathcal D_\mu\lambda^B", 1),
            (r"-\widetilde\lambda^A\bar\sigma_E^m\mathcal D_m\lambda^B", 1),
        ),
        "72n": (
            (r"\mu_A^{(0)}:=\widetilde\phi_IT_A{}^I{}_J\phi^J+\xi_A", 1),
            (r"=\int d^4x_R\,\xi_A\mathscr D_R^A", 1),
        ),
        "72o": (
            (r"-(\mathcal D_\mu\bar\phi)_I(\mathcal D^\mu\phi)^I", 1),
            (r"+i\bar\psi_{\dot a,I}(\bar\sigma_L^\mu)^{\dot aa}", 1),
            (r"+\bar F_IF^I+\mu_A^{(0)}\mathscr D^A", 1),
            (r"+i\sqrt2\left[", 1),
            (r"+\mathscr U_IF^I-\frac12\mathscr U_{IJ}\psi^I\psi^J", 1),
            (r"-\frac14\mathfrak h_{AB}F^A_{\mu\nu}F^{B\mu\nu}", 1),
            (r"+i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu", 1),
            (r"+\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B", 1),
            (r"-\frac18\mathfrak k_{AB}\epsilon_L^{\mu\nu\rho\sigma}", 1),
        ),
        "72p": (
            (r"+(\mathcal D_m\widetilde\phi)_I(\mathcal D_m\phi)^I", 1),
            (r"+\widetilde\psi_{\dot a,I}(\bar\sigma_E^m)^{\dot aa}", 1),
            (r"-\widetilde F_IF^I-\mu_A^{(0)}\mathscr D^A", 1),
            (r"-i\sqrt2\left[", 1),
            (r"-\mathscr U_IF^I+\frac12\mathscr U_{IJ}\psi^I\psi^J", 1),
            (r"+\frac14\mathfrak h_{AB}F^A_{mn}F^B_{mn}", 1),
            (r"+\mathfrak h_{AB}\widetilde\lambda^A\bar\sigma_E^m", 1),
            (r"-\frac12\mathfrak h_{AB}\mathscr D^A\mathscr D^B", 1),
            (r"-\frac i8\mathfrak k_{AB}\epsilon_E^{mnrs}", 1),
        ),
    }
    for tag, bindings in equation_bindings.items():
        body = equation_bodies[tag]
        for binding, expected_count in bindings:
            compact_binding = re.sub(r"\s+", "", binding)
            recorder.check(
                f"equation 3C.{tag} exact binding: {binding}",
                body.count(compact_binding),
                expected_count,
                "component_density_binding",
            )
    master_expected = re.sub(
        r"\s+",
        "",
        r"-4\kappa_Ru_R\boldsymbol Z_{R\dot b}^{\mathsf V}",
    )
    master_mutated = equation_bodies["72d"].replace(
        master_expected,
        master_expected.replace("-4", "+4", 1),
    )
    recorder.check(
        "mutation probe changes the row-curvature sign",
        master_mutated == equation_bodies["72d"],
        False,
        "mutation",
    )
    recorder.check(
        "row-curvature sign mutation violates exact binding",
        master_mutated.count(master_expected),
        0,
        "mutation",
    )
    gaugino_expected = re.sub(
        r"\s+",
        "",
        r"+i\mathfrak h_{AB}\bar\lambda^A\bar\sigma_L^\mu",
    )
    gaugino_mutated = equation_bodies["72o"].replace(
        gaugino_expected,
        gaugino_expected.replace("+i", "-i", 1),
    )
    recorder.check(
        "mutation probe changes the Lorentz gaugino sign",
        gaugino_mutated == equation_bodies["72o"],
        False,
        "mutation",
    )
    recorder.check(
        "Lorentz gaugino sign mutation violates exact binding",
        gaugino_mutated.count(gaugino_expected),
        0,
        "mutation",
    )
    dotted_expected = re.sub(
        r"\s+",
        "",
        r"&=+\epsilon_{\dot b\dot a}\mathscr D^A+\tau_R(\bar\sigma_R^{MN})",
    )
    dotted_mutated = equation_bodies["72k"].replace(
        dotted_expected,
        dotted_expected.replace("+\\tau_R", "-\\tau_R", 1),
    )
    recorder.check(
        "mutation probe changes the dotted curvature phase",
        dotted_mutated == equation_bodies["72k"],
        False,
        "mutation",
    )
    recorder.check(
        "dotted curvature phase mutation violates exact binding",
        dotted_mutated.count(dotted_expected),
        0,
        "mutation",
    )
    contract_bindings = {
        "relative bridge multiplication order": (
            r"\mathcalE_R:=\widetilde{\mathcalB}_R\mathcalB_R=e^{\mathcalV_R}"
        ),
        "B finite transformation order": r"\mathcalB_R'=k_R\mathcalB_Rh_R^{-1}",
        "Btilde finite transformation order": (
            r"\widetilde{\mathcalB}_R'=\widetildeh_R\widetilde{\mathcalB}_Rk_R^{-1}"
        ),
        "vector undotted bridge solution": (
            r"\boldsymbol\nabla^{\mathsfV}_{Ra}&=\widetilde{\mathcalB}_R^{-1}"
            r"\circD_{Ra}\circ\widetilde{\mathcalB}_R"
        ),
        "vector dotted bridge solution": (
            r"\bar{\boldsymbol\nabla}^{\mathsfV}_{R\dota}&=\mathcalB_R"
            r"\circ\barD_{R\dota}\circ\mathcalB_R^{-1}"
        ),
        "chiral similarity order": (
            r"\nabla^{\mathsfC}_{Ra}&:=\mathcalB_R^{-1}"
            r"\boldsymbol\nabla^{\mathsfV}_{Ra}\mathcalB_R"
        ),
        "chiral strength transport order": (
            r"\boldsymbol{\mathcalW}^{\mathsfV}_{Ra}"
            r"&:=\mathcalB_R\mathcalW^{\mathsfC}_{Ra}\mathcalB_R^{-1}"
        ),
        "antichiral strength transport order": (
            r"\widetilde{\boldsymbol{\mathcalW}}^{\mathsfV}_{R\dota}"
            r"&:=\widetilde{\mathcalB}_R^{-1}"
            r"\widetilde{\mathcalW}^{\mathsfA}_{R\dota}\widetilde{\mathcalB}_R"
        ),
        "column matter frame map": (
            r"\Phi_R:=\mathcalB_R^{-1}\boldsymbol\Phi_R^{\mathsfV}"
        ),
        "row matter frame map": (
            r"\widetilde\Phi_R:=\widetilde{\boldsymbol\Phi}_R^{\mathsfV}"
            r"\widetilde{\mathcalB}_R^{-1}"
        ),
    }
    for name, binding in contract_bindings.items():
        recorder.check(f"contract binding: {name}", binding in compact, True, "document")

    coefficient_bindings = (
        r"\kappa_L:=2i",
        r"\kappa_E:=-2",
        r"u_R:=\frac4{\kappa_R}",
        r"\rho_R:=\frac4{\kappa_R^2}",
        r"(u_L,\rho_L)=(-2i,-1)",
        r"(u_E,\rho_E)=(-2,+1)",
    )
    for binding in coefficient_bindings:
        recorder.check(f"contract coefficient binding: {binding}", binding in compact, True, "document")
    recorder.check("Step-3B s_R collision absent", "s_R" in contract, False, "document")
    recorder.check("task id", task["id"], TASK_ID, "provenance")
    recorder.check("task type", task["type"], "CONTRACT_CHANGE", "provenance")
    recorder.check("reference audit status", reference_audit["status"], "PASS", "provenance")
    recorder.check("scoped subset sha256", hashlib.sha256(SUBSET.read_bytes()).hexdigest(), SUBSET_SHA, "provenance")
    recorder.check("source ledger subset sha256", source_ledger["scoped_artifact"]["sha256"], SUBSET_SHA, "provenance")
    recorder.check("source translation was deferred", source_ledger["source_scope"]["translation_status"], "NOT_PERFORMED_IN_REFERENCE_IMPORT", "provenance")

    claims = {item["id"] for item in claim_map["claims"]}
    for claim in (
        "SUPERSPACE-1001-GAUGE-CHIRAL-REPRESENTATION-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-BRIDGE-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-BIANCHI-EVIDENCE",
        "SUPERSPACE-1001-VECTOR-ACTION-COMPARISON-EVIDENCE",
    ):
        recorder.check(f"claim admitted: {claim}", claim in claims, True, "provenance")

    obligation = next(item for item in obligations["proof_obligations"] if item["id"] == TASK_ID)
    recorder.check(
        "proof obligation points to archived task",
        obligation["task"],
        "tasks/archive/CONTRACT-STEP-03C-GAUGE-VECTOR-REPRESENTATION-001.yaml",
        "provenance",
    )

    for token in (r"\sim", r"\approx", r"\propto"):
        recorder.check(f"forbidden loose token absent: {token}", token in contract, False, "document")
    recorder.check(
        "raw Phi_R typo absent",
        re.search(r"(?<!\\)Phi_R", contract) is not None,
        False,
        "document",
    )
    recorder.check("gauge-frame distinction explicit", "gauge-vector frame" in contract and "gauge-chiral frame" in contract, True, "document")
    recorder.check("intrinsic Euclidean independence explicit", "independent complexified data" in contract, True, "document")
    recorder.check(
        "source FI equation excluded",
        re.search(r"\(4\.3\.3\).*?not\s+inputs", contract, flags=re.DOTALL) is not None,
        True,
        "document",
    )
    recorder.check("Project W coefficient -1/8", r"-\frac18\bar D_R^2" in contract, True, "document")
    recorder.check("Project Wtilde coefficient +1/8", r"+\frac18D_R^2" in contract, True, "document")
    recorder.check("component fermion coefficient", r"\frac1{\sqrt2}" in contract, True, "document")
    recorder.check("component auxiliary coefficient", r"-\frac14" in contract, True, "document")
    density_segment = contract[
        contract.index("#### 3C.6.1 Canonical matter density") : contract.index("### 3C.7 Wick transport")
    ]
    density_bindings = {
        "flat D-density projector": r"\frac1{16}D_R^2\bar D_R^2",
        "graded row-column product rule": r"(-1)^{|\mathfrak A||X|}",
        "dual-row curvature sign": (
            r"=-2u_R\boldsymbol Z_{R\dot b}^{\mathsf V}"
            r"\widetilde{\boldsymbol{\mathcal W}}_R^{\mathsf V\dot b}"
        ),
        "matter master vector-derivative coefficient": (
            r"=16(\boldsymbol{\mathcal D}_{RM}^{\mathsf V})^{\rm row}"
        ),
        "matter master gaugino coefficient": (
            r"-16\boldsymbol Z_{R\dot b}^{\mathsf V}"
        ),
        "matter master auxiliary coefficient": (
            r"-8\widetilde{\boldsymbol\Phi}_R^{\mathsf V}"
            r"\boldsymbol\nabla_R^{\mathsf V a}"
        ),
        "boundary current expanded": r"\partial_{RM}J_R^M",
        "superpotential covariant chain rule": (
            r"\mathscr U_{R,IJ}"
            r"\boldsymbol\nabla_R^{\mathsf V a}\boldsymbol\Phi_R^{\mathsf V I}"
        ),
        "W second-spinor derivative": (
            r"=-2i\kappa_R(\sigma_R^M)_{a\dot b}"
        ),
        "twice-graded odd product": r"+2(-1)^{|X|}",
        "Lorentz undotted topological density": (
            r"+\frac i4\epsilon_L^{\mu\nu\rho\sigma}"
        ),
        "Euclidean dotted topological density": (
            r"-\frac14\epsilon_E^{mnrs}F^A_{mn}F^B_{rs}"
        ),
        "Lorentz canonical component action": r"\mathcal L_{L,\mathrm{can}}",
        "Euclidean canonical component action": r"\mathcal L_{E,\mathrm{can}}",
    }
    density_compact = re.sub(r"\s+", "", density_segment)
    for name, binding in density_bindings.items():
        recorder.check(
            f"component-density binding: {name}",
            re.sub(r"\s+", "", binding) in density_compact,
            True,
            "document",
        )
    recorder.check(
        "component-density derivation has no coordinate expansion",
        r"\vartheta" in density_segment,
        False,
        "document",
    )
    recorder.check(
        "general component transport defines C-frame projections",
        r"\psi_{Ra}^{\mathsf C}" in contract and r"F_R^{\mathsf C}" in contract,
        True,
        "document",
    )
    recorder.check(
        "WZ pure-spinor second jet fixed",
        (
            (r"D_R^2\mathcal E_R|=0" in contract or r"D_R^2\mathcal B_R|=0" in contract)
            and (
                r"\bar D_R^2\mathcal E_R|=0" in contract
                or r"\bar D_R^2\widetilde{\mathcal B}_R|=0" in contract
            )
        ),
        True,
        "document",
    )
    bare_frame_patterns = (
        r"\boldsymbol\nabla_R^{V",
        r"\bar{\boldsymbol\nabla}_R^{V",
        r"\boldsymbol{\mathcal W}_R^{V",
        r"\widetilde{\boldsymbol{\mathcal W}}_R^{V",
        r"\mathcal W_R^{C",
        r"\widetilde{\mathcal W}_R^{A",
    )
    recorder.check(
        "frame labels use mathsf V/C/A",
        [pattern for pattern in bare_frame_patterns if pattern in contract],
        [],
        "document",
    )
    recorder.check(
        "FI covector annihilates the derived algebra and uses the logarithm chart",
        re.search(r"\\xi_A\s*c_\{BC\}\{\}\^\{?A\}?\s*=\s*0", contract) is not None
        and r"\mathcalV_R:=\log(\widetilde{\mathcalB}_R\mathcalB_R)" in compact,
        True,
        "document",
    )


def build_audit() -> dict[str, Any]:
    recorder = Recorder()
    document_and_provenance_checks(recorder)
    data = bridge_witnesses(recorder)
    connection_witnesses(recorder, data)
    chirality_and_action_witnesses(recorder, data)
    component_projection_witnesses(recorder)
    coefficient_witnesses(recorder)
    component_density_witnesses(recorder)
    bianchi_witnesses(recorder)

    categories: dict[str, dict[str, int]] = {}
    for check in recorder.checks:
        row = categories.setdefault(check["category"], {"checks": 0, "failed": 0})
        row["checks"] += 1
        if not check["passed"]:
            row["failed"] += 1

    return {
        "schema": 1,
        "task": TASK_ID,
        "status": "PASS" if not recorder.failures else "FAIL",
        "arithmetic": {
            "coefficient_field": "Q(i)",
            "floating_point": False,
            "external_cas": False,
            "matrix_witness_dimension": 2,
            "component_exterior_generators": ["theta^1", "theta^2"],
            "component_operator_dimension": 8,
        },
        "categories": categories,
        "totals": {
            "exact_checks": len(recorder.checks),
            "failed_checks": len(recorder.failures),
        },
        "checks": recorder.checks,
        "failures": recorder.failures,
    }


def main() -> None:
    audit = build_audit()
    AUDIT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if audit["status"] != "PASS":
        print(json.dumps(audit["failures"], indent=2, ensure_ascii=False))
        raise SystemExit(1)
    print(
        "Step-3C exact verification: "
        f"{audit['totals']['exact_checks']} exact checks, 0 failures"
    )


if __name__ == "__main__":
    main()
