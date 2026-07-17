#!/usr/bin/env python3
"""Exact SU(2) component check of main-memo equations (K3.31)--(K3.32)."""

from itertools import permutations, product


def delta(a: int, b: int) -> int:
    return int(a == b)


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) != 3:
        return 0
    return 1 if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)} else -1


def color_from_half_ladders(a: int, b: int, c: int, d: int, e: int) -> int:
    """Equation (K3.31), with f_ABC=epsilon_ABC for SU(2)."""
    total = 0
    for x, y, z in permutations((a, b, c)):
        total += 4 * sum(
            epsilon3(d, x, m) * epsilon3(m, y, n) * epsilon3(n, z, e)
            for m, n in product(range(3), repeat=2)
        )
    return total


def color_closed_form(a: int, b: int, c: int, d: int, e: int) -> int:
    """Equation (K3.32)."""
    return -8 * (
        delta(a, b) * epsilon3(d, c, e)
        + delta(a, c) * epsilon3(d, b, e)
        + delta(b, c) * epsilon3(d, a, e)
    )


def main() -> None:
    components = {}
    max_deviation = 0
    for indices in product(range(3), repeat=5):
        actual = color_from_half_ladders(*indices)
        expected = color_closed_form(*indices)
        components[indices] = actual
        max_deviation = max(max_deviation, abs(actual - expected))

    abc_symmetry_max = 0
    de_antisymmetry_max = 0
    for (a, b, c, d, e), value in components.items():
        for rho in permutations((a, b, c)):
            abc_symmetry_max = max(
                abc_symmetry_max,
                abs(value - components[(*rho, d, e)]),
            )
        de_antisymmetry_max = max(
            de_antisymmetry_max,
            abs(value + components[(a, b, c, e, d)]),
        )

    nonzero_components = sum(value != 0 for value in components.values())
    print("CP6_COLOR_RANK5_SU2_EXACT")
    print(f"components={len(components)}")
    print(f"max_deviation_K3_32={max_deviation}")
    print(f"nonzero_components={nonzero_components}")
    print(f"abc_symmetry_max_deviation={abc_symmetry_max}")
    print(f"de_antisymmetry_max_deviation={de_antisymmetry_max}")
    if (max_deviation, nonzero_components, abc_symmetry_max, de_antisymmetry_max) != (
        0,
        42,
        0,
        0,
    ):
        raise SystemExit("FAIL")
    print("PASS")


if __name__ == "__main__":
    main()
