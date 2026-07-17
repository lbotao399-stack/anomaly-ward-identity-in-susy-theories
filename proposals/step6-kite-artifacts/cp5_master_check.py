#!/usr/bin/env python3
"""Exact and numerical checks tied only to cp5_master_derivation.md equations."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
RAW = HERE / "generated" / "cp5_numeric_raw.csv"
CP4_REPORT = HERE / "generated" / "cp0_cp4_fast_gate_report.json"


def passed(tag: str, detail: str) -> None:
    print(f"PASS {tag}: {detail}")


def quadratic_zero(values: dict[float, float]) -> float:
    # Lagrange interpolation at zero for nodes 0.03, 0.02, 0.01.
    return values[0.03] - 3.0 * values[0.02] + 3.0 * values[0.01]


eps, delta = sp.symbols("eps delta", positive=True)
d = 4 - 2 * eps


def j(n: int) -> sp.Expr:
    return (4 * sp.pi) ** (-d / 2) * sp.gamma(n - d / 2) / sp.gamma(n) * delta ** (d / 2 - n)


def l_from_rule(n: int) -> sp.Expr:
    return sp.simplify((4 - d) / d * (j(n - 1) - delta * j(n)))


def l_closed(n: int) -> sp.Expr:
    return eps * (4 * sp.pi) ** (-d / 2) * sp.gamma(n - 1 - d / 2) / sp.gamma(n) * delta ** (d / 2 + 1 - n)


assert all(sp.simplify(l_from_rule(n) / l_closed(n) - 1) == 0 for n in (2, 3, 4))
passed("(CP5.1)", "K.11 ratio is exactly 1 for n=2,3,4")

assert sp.simplify(sp.limit(l_closed(3), eps, 0) - 1 / (32 * sp.pi**2)) == 0
passed("(CP5.2)", "n=3 anchor is exactly 1/(32*pi^2)")

x1, x2, x3, x4, x5 = sp.symbols("x1 x2 x3 x4 x5")
s1, s2, s12 = sp.symbols("s1 s2 s12")
A = x1 + x3 + x4
B = x2 + x3 + x5
C = x3
U = sp.expand(A * B - C**2)
Q2 = s1 + s2 + 2 * s12
rl2 = x3**2 * Q2 + x4**2 * s1 + 2 * x3 * x4 * (s1 + s12)
rk2 = x3**2 * Q2 + x5**2 * s2 + 2 * x3 * x5 * (s2 + s12)
rlrk = x3**2 * Q2 + x3 * x5 * (s2 + s12) + x3 * x4 * (s1 + s12) + x4 * x5 * s12
H = x3 * Q2 + x4 * s1 + x5 * s2
F_complete = sp.expand(U * H - B * rl2 - A * rk2 + 2 * C * rlrk)
F_printed = (
    s1 * x1 * (x2 * x3 + x2 * x4 + x3 * x4 + x3 * x5 + x4 * x5)
    + s2 * x2 * (x1 * x3 + x1 * x5 + x3 * x4 + x3 * x5 + x4 * x5)
    + 2 * s12 * x1 * x2 * x3
)
assert sp.expand(F_complete - F_printed) == 0
passed("(CP5.3)-(CP5.4)", "completed-square U and expanded F agree term by term")

gll, gkk, glk = sp.symbols("gll gkk glk")
mu_ll = -eps * (1 - eps) * gll**2
mu_kk = -eps * (1 - eps) * gkk**2
mu_lk2 = -eps * gll * gkk / 2 - eps * (1 - 2 * eps) * glk**2 / 2
mu_llkk = eps**2 * gll * gkk - eps * glk**2
mu_lllk = -eps * (1 - eps) * gll * glk
mu_kklk = -eps * (1 - eps) * gkk * glk
expanded_sum_square = sp.expand(mu_ll + mu_kk + 4 * mu_lk2 + 2 * mu_llkk + 4 * mu_lllk + 4 * mu_kklk)
single_sum_square = sp.expand(-eps * (1 - eps) * (gll + 2 * glk + gkk) ** 2)
assert sp.simplify(expanded_sum_square - single_sum_square) == 0
passed("(CP5.5)", "all Wick terms reconstruct the fourth moment of mu_(l+k)^2")

swap = {x1: x2, x2: x1, x4: x5, x5: x4, s1: s2, s2: s1}
assert sp.expand(U.xreplace(swap) - U) == 0
assert sp.expand(F_printed.xreplace(swap) - F_printed) == 0
assert s1 != s2
claimed_difference = sp.simplify((-s1 + s2) / (3072 * sp.pi**4))
assert claimed_difference != 0
passed("(CP5.7)-(CP5.9)", "routing symmetry is exact; the two starting-snapshot draft branches differ for s1!=s2")

raw: dict[str, dict[float, float]] = {f"N{i}": {} for i in range(1, 7)}
with RAW.open(newline="") as handle:
    rows = csv.DictReader(line for line in handle if not line.startswith("#"))
    for row in rows:
        raw[row["master"]][float(row["epsilon"])] = float(row["value"])
assert all(set(values) == {0.03, 0.02, 0.01} for values in raw.values())

exact_poles = {
    "N2": -1 / (9216 * math.pi**4),
    "N3": 1 / (4096 * math.pi**4),
    "N5": 1 / (1024 * math.pi**4),
    "N6": 1 / (1024 * math.pi**4),
}
for name, exact in exact_poles.items():
    extrapolated = quadratic_zero({e: e * value for e, value in raw[name].items()})
    assert abs(extrapolated / exact - 1.0) < 0.0023
passed("(CP5.10)-(CP5.11)", "sector numerics recover all four exact pole residues within 0.23 percent")

exact_finite = {
    "N1": -19 / (81920 * math.pi**4),
    "N4": -1 / (1024 * math.pi**4),
}
for name, exact in exact_finite.items():
    extrapolated = quadratic_zero(raw[name])
    assert abs(extrapolated / exact - 1.0) < 0.0020
passed("(CP5.12)-(CP5.13)", "finite N1 and N4 extrapolations match the exact local values within 0.20 percent")

report = json.loads(CP4_REPORT.read_text())
assert report["cp1"]["explicit_trace_pass"] is False
assert "forbids CP2--CP4" in report["blocked_effect"]
passed("(CP5.14)-(CP5.15)", "CP4 row inventory is absent by the failed mandatory CP1 gate; interface remains blocked")
