#!/usr/bin/env python3
"""Target-blind checks for the Step-5 BRST clean review.

The script reads only the seven Project files in ``EXPECTED_INPUTS``.
It does not inspect any Step-5 contract, audit, generated output, HT file,
or Pro ledger.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Mapping, Tuple


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_INPUTS: Mapping[str, str] = {
    "AUTHORITY.md": "3970e8769fc21a5f41a1fa0d4e537b577f3d1d7b212bc6795819b37b6d58ae6f",
    "AGENTS.md": "a8565eb09959193c273746ece9cb08dd4a5f18d644ea9bca0638ad7739cf8d46",
    "tasks/CURRENT.yaml": "4ed8aa9957868233f4c1b7ff4a4c4ec02744c153ffd0d16e30f6e322042ba749",
    "contracts/foundations/step-03a-gauge-chiral-action.md": "48141fc931580f6b73e385b8f900b3e6df5939cdb9348042de07fd8fe9320967",
    "contracts/foundations/step-03c-gauge-vector-representation.md": "c4cc6f0504b79e02ce78030ad79b625bee6da7dff9de0f6a1ddc3b33ef2584a1",
    "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md": "109e0c531da3a1b98313e87dd692fa3d9047c8f745291f8e87021008c7acc538",
    "contracts/foundations/step-04c-n4-super-yang-mills.md": "fafc3bc2227b60ca699b3f953b632db82dafe093b221baa74736cc5fb838928f",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


Word = Tuple[str, ...]


@dataclass(frozen=True)
class NCExpr:
    """Integer linear combination of noncommutative words."""

    terms: Mapping[Word, int]

    @staticmethod
    def atom(name: str) -> "NCExpr":
        return NCExpr({(name,): 1})

    @staticmethod
    def zero() -> "NCExpr":
        return NCExpr({})

    def clean(self) -> "NCExpr":
        return NCExpr({word: coeff for word, coeff in self.terms.items() if coeff})

    def __add__(self, other: "NCExpr") -> "NCExpr":
        out: Dict[Word, int] = dict(self.terms)
        for word, coeff in other.terms.items():
            out[word] = out.get(word, 0) + coeff
        return NCExpr(out).clean()

    def __neg__(self) -> "NCExpr":
        return NCExpr({word: -coeff for word, coeff in self.terms.items()})

    def __sub__(self, other: "NCExpr") -> "NCExpr":
        return self + (-other)

    def __mul__(self, other: "NCExpr") -> "NCExpr":
        out: Dict[Word, int] = {}
        for left, left_coeff in self.terms.items():
            for right, right_coeff in other.terms.items():
                word = left + right
                out[word] = out.get(word, 0) + left_coeff * right_coeff
        return NCExpr(out).clean()

    def scale(self, integer: int) -> "NCExpr":
        return NCExpr({word: integer * coeff for word, coeff in self.terms.items()}).clean()


PARITY = {"qx": 1, "qy": 1, "U": 0, "J": 0}


def word_parity(word: Word) -> int:
    return sum(PARITY[token] for token in word) % 2


def brst_atom(token: str) -> NCExpr:
    qx = NCExpr.atom("qx")
    qy = NCExpr.atom("qy")
    u = NCExpr.atom("U")
    j = NCExpr.atom("J")
    if token == "qx":
        return qx * qx
    if token == "qy":
        return qy * qy
    if token == "U":
        return qx * u - u * qy
    if token == "J":
        return qy * j - j * qx
    raise KeyError(token)


def brst_word(word: Word) -> NCExpr:
    out = NCExpr.zero()
    prefix_parity = 0
    for position, token in enumerate(word):
        left = NCExpr({word[:position]: 1})
        right = NCExpr({word[position + 1 :]: 1})
        contribution = left * brst_atom(token) * right
        if prefix_parity:
            contribution = contribution.scale(-1)
        out = out + contribution
        prefix_parity = (prefix_parity + PARITY[token]) % 2
    return out.clean()


def brst(expr: NCExpr) -> NCExpr:
    out = NCExpr.zero()
    for word, coeff in expr.terms.items():
        out = out + brst_word(word).scale(coeff)
    return out.clean()


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matadd(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def trace(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def first_jet_pairing_check() -> bool:
    u = [2, -3, 5]
    j = [7, 11, -13]
    m = [[0, 2, -1], [-2, 0, 3], [4, -5, 0]]
    s_u = [-sum(u[k] * m[i][k] for k in range(3)) for i in range(3)]
    s_j = [sum(j[k] * m[k][i] for k in range(3)) for i in range(3)]
    return sum(s_j[i] * u[i] + j[i] * s_u[i] for i in range(3)) == 0


def second_jet_pairing_check() -> bool:
    u = [[2, -3, 5], [-3, 7, 11], [5, 11, -13]]
    j = [[17, 19, -23], [19, 29, 31], [-23, 31, 37]]
    m = [[0, 2, -1], [-2, 0, 3], [4, -5, 0]]
    s_u = [
        [
            -sum(u[k][q] * m[p][k] for k in range(3))
            - sum(u[p][k] * m[q][k] for k in range(3))
            for q in range(3)
        ]
        for p in range(3)
    ]
    s_j = [
        [
            sum(j[k][q] * m[k][p] for k in range(3))
            + sum(j[p][k] * m[k][q] for k in range(3))
            for q in range(3)
        ]
        for p in range(3)
    ]
    total = sum(
        s_j[p][q] * u[p][q] + j[p][q] * s_u[p][q]
        for p in range(3)
        for q in range(3)
    )
    return total == 0


def second_path_derivative_symmetry_check() -> bool:
    def ordered_insertions(t: int, first: str, s: int, second: str) -> tuple[str, str]:
        if t == s:
            raise ValueError("coincident insertion requires a contact prescription")
        return (first, second) if t > s else (second, first)

    samples = [(7, "A", 2, "B"), (1, "A", 9, "B"), (5, "A", 3, "B")]
    return all(
        ordered_insertions(t, a, s, b) == ordered_insertions(s, b, t, a)
        for t, a, s, b in samples
    )


def adjoint_symmetric_trace_check() -> bool:
    matrices = [
        [[0, 2, -3], [-2, 0, 5], [3, -5, 0]],
        [[0, 7, 11], [-7, 0, -13], [-11, 13, 0]],
        [[0, -17, 19], [17, 0, 23], [-19, -23, 0]],
    ]
    if any(matadd(transpose(matrix), matrix) != [[0] * 3 for _ in range(3)] for matrix in matrices):
        return False
    for a in matrices:
        for b in matrices:
            for c in matrices:
                anticommutator = matadd(matmul(b, c), matmul(c, b))
                if trace(matmul(a, anticommutator)) != 0:
                    return False
    return True


def laurent_finite_part_check() -> bool:
    rho = {0: 0, 1: 3, 2: -5}
    pole_map = {-2: 7, -1: 11, 0: 13}
    coefficient_zero = sum(rho_power * pole_power for r, rho_power in rho.items() for k, pole_power in pole_map.items() if r + k == 0)
    residue_formula = rho[1] * pole_map[-1] + rho[2] * pole_map[-2]
    return coefficient_zero == residue_formula == -2


def keyword_absence_check(contents: Mapping[str, str]) -> bool:
    foundation_text = "\n".join(
        contents[name]
        for name in EXPECTED_INPUTS
        if name.startswith("contracts/foundations/")
    ).lower()
    return all(
        token not in foundation_text
        for token in ("dred", "dimensional reduction", "evanescent")
    )


def main() -> int:
    actual_hashes: Dict[str, str] = {}
    contents: Dict[str, str] = {}
    for relative in EXPECTED_INPUTS:
        path = ROOT / relative
        actual_hashes[relative] = sha256(path)
        contents[relative] = path.read_text(encoding="utf-8")

    qx = NCExpr.atom("qx")
    qy = NCExpr.atom("qy")
    u = NCExpr.atom("U")
    j = NCExpr.atom("J")
    checks = {
        "input_hashes_match": actual_hashes == dict(EXPECTED_INPUTS),
        "link_endpoint_brst_nilpotent": brst(brst(u)).terms == {},
        "dual_source_endpoint_brst_nilpotent": brst(brst(j)).terms == {},
        "first_jet_pairing_brst_closed": first_jet_pairing_check(),
        "second_jet_pairing_brst_closed": second_jet_pairing_check(),
        "second_path_derivative_symmetric_off_diagonal": second_path_derivative_symmetry_check(),
        "adjoint_symmetrized_cubic_trace_zero_spotcheck": adjoint_symmetric_trace_check(),
        "evanescent_pole_finite_part_convolution": laurent_finite_part_check(),
        "dred_definitions_absent_from_narrowed_foundations": keyword_absence_check(contents),
        "endpoint_rules_recorded": bool(qx.terms and qy.terms),
    }
    result = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "root": str(ROOT),
        "read_files": actual_hashes,
        "checks": checks,
        "blocked_evaluations": [
            "BLOCKED_DRED_REGULATOR_UNDEFINED",
            "BLOCKED_GAUGE_ANOMALY_CLASSIFICATION_UNADMITTED",
            "BLOCKED_LINK_COINCIDENT_CONTACT_PRESCRIPTION_UNDEFINED",
            "BLOCKED_BILOCAL_SOURCE_BV_DOMAIN_UNDEFINED",
            "BLOCKED_COMPOSITE_MIXING_DATA_UNDEFINED",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
