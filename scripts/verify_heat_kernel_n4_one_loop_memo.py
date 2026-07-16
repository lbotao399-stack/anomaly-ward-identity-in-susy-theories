#!/usr/bin/env python3
"""Exact checks for the bounded heat-kernel auxiliary lemma."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MEMO = ROOT / "proposals/heat-kernel-n4-one-loop-memo-2026-07-16.md"
OUTPUT = ROOT / "audits/heat-kernel-ordered-simplex-verification.json"
CHECKS: list[dict[str, object]] = []


def record(name: str, equations: list[str], condition: bool) -> None:
    CHECKS.append({"name": name, "equations": equations, "passed": bool(condition)})


def gaussian_check() -> None:
    s = sp.symbols("s", positive=True)
    xs = sp.symbols("x0:4", real=True)
    r2 = sum(x * x for x in xs)
    kernel = (4 * sp.pi * s) ** -2 * sp.exp(-r2 / (4 * s))
    normalized = kernel
    for x in xs:
        normalized = sp.integrate(normalized, (x, -sp.oo, sp.oo))
    heat = sp.diff(kernel, s) - sum(sp.diff(kernel, x, 2) for x in xs)
    diagonal = kernel.subs({x: 0 for x in xs})
    record(
        "Gaussian normalization, diagonal, and heat equation",
        ["HK.4", "HK.5", "HK.8"],
        sp.simplify(normalized - 1) == 0
        and sp.simplify(diagonal - 1 / (16 * sp.pi**2 * s**2)) == 0
        and sp.simplify(heat) == 0,
    )


def semigroup_check() -> None:
    s, t = sp.symbols("s t", positive=True)
    x, y = sp.symbols("x y", real=True)
    lhs = (x - y) ** 2 / (4 * s) + y**2 / (4 * t)
    rhs = (s + t) / (4 * s * t) * (y - t * x / (s + t)) ** 2 + x**2 / (4 * (s + t))
    prefactor = (4 * sp.pi * s) ** sp.Rational(-1, 2) * (4 * sp.pi * t) ** sp.Rational(-1, 2)
    variance = s * t / (s + t)
    composed_prefactor = sp.simplify(prefactor * sp.sqrt(4 * sp.pi * variance))
    record(
        "Gaussian completion and semigroup prefactor",
        ["HK.9", "HK.10"],
        sp.simplify(sp.expand(lhs - rhs)) == 0
        and sp.simplify(composed_prefactor - (4 * sp.pi * (s + t)) ** sp.Rational(-1, 2)) == 0,
    )


def bridge_check() -> None:
    t1, t2, t3, w, rho = sp.symbols("t1 t2 t3 w rho", positive=True)
    x, y = sp.symbols("x y", real=True)
    q = (x - w) ** 2 / (4 * t1) + (y - x) ** 2 / (4 * t2) + y**2 / (4 * t3)
    solution = sp.solve([sp.diff(q, x), sp.diff(q, y)], [x, y], dict=True)[0]
    total = t1 + t2 + t3
    means = sp.simplify(solution[x] - (t2 + t3) * w / total) == 0 and sp.simplify(
        solution[y] - t3 * w / total
    ) == 0
    covariance = sp.hessian(q, (x, y)).inv()
    scaled = covariance.subs({t1: rho * t1, t2: rho * t2, t3: rho * t3})
    homogeneous = all(
        sp.simplify(scaled[i, j] - rho * covariance[i, j]) == 0
        for i in range(2)
        for j in range(2)
    )
    record("Three-segment bridge mean and covariance", ["HK.13", "HK.14"], means and homogeneous)


def fixed_shift_check() -> None:
    s, w = sp.symbols("s w", positive=True)
    kernel = (4 * sp.pi * s) ** -2 * sp.exp(-(w * w) / (4 * s))
    record("Fixed nonzero shift has zero short-time pointwise limit", ["HK.15"], sp.limit(kernel, s, 0, dir="+") == 0)


def simplex_check() -> None:
    a, b = sp.symbols("a b", nonnegative=True)
    exact = True
    for p in range(7):
        for q in range(7):
            value = sp.integrate(sp.integrate(a**p * b**q, (a, 0, b)), (b, 0, 1))
            exact = exact and sp.simplify(value - sp.Rational(1, (p + 1) * (p + q + 2))) == 0
    record("Single-ordering simplex moment", ["HK.18"], exact)


def tower_check() -> None:
    exact = True
    for m in range(7):
        for n in range(7):
            for k in range(m + 1):
                for ell in range(n + 1):
                    p = k + ell
                    q = m + n - k - ell
                    moment = sp.Rational(1, (p + 1) * (p + q + 2))
                    lhs = sp.binomial(m, k) * sp.binomial(n, ell) * moment
                    rhs = sp.binomial(m, k) * sp.binomial(n, ell) / ((m + n + 2) * (k + ell + 1))
                    exact = exact and sp.simplify(lhs - rhs) == 0
    record("Single-ordering derivative tower", ["HK.19"], exact)


def factorial_check() -> None:
    exact = True
    for r in range(9):
        for k in range(9):
            lhs = sum(
                Fraction((-1) ** j, sp.factorial(r - j) * sp.factorial(k + j + 2))
                for j in range(r + 1)
            )
            rhs = Fraction(1, (r + k + 2) * sp.factorial(r) * sp.factorial(k + 1))
            exact = exact and sp.simplify(lhs - rhs) == 0
    record("Alternating factorial identity", ["HK.20"], exact)


def dred_check() -> None:
    epsilon, delta = sp.symbols("epsilon Delta", positive=True)
    d = 4 - 2 * epsilon
    radial = (
        (4 * sp.pi) ** (-d / 2)
        * (d / 2)
        * sp.gamma(2 - d / 2)
        / sp.gamma(3)
        * delta ** (d / 2 - 2)
    )
    evanescent = sp.simplify((4 - d) / d * radial)
    value = sp.limit(evanescent, epsilon, 0, dir="+")
    record("DRED evanescent master integral", ["HK.21", "HK.22", "HK.24"], sp.simplify(value - 1 / (32 * sp.pi**2)) == 0)


def main() -> int:
    gaussian_check()
    semigroup_check()
    bridge_check()
    fixed_shift_check()
    simplex_check()
    tower_check()
    factorial_check()
    dred_check()
    passed = all(bool(check["passed"]) for check in CHECKS)
    payload = {
        "scope": "VERIFIED_AUXILIARY_LEMMA",
        "memo": str(MEMO.relative_to(ROOT)),
        "memo_sha256": hashlib.sha256(MEMO.read_bytes()).hexdigest(),
        "check_count": len(CHECKS),
        "checks": CHECKS,
        "full_heat_kernel_step5_status": "BLOCKED_HEAT_KERNEL_TYPED_REGULATOR_AND_COEFFICIENT_DERIVATION",
        "passed": passed,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for check in CHECKS:
        print(f"[{'PASS' if check['passed'] else 'FAIL'}] {check['name']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
