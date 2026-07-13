#!/usr/bin/env python3
"""Exact Step-5A Fermi--Feynman vector Wick-kernel verification.

The Grassmann operators are the Project 16-dimensional left-regular
representation already derived in ``verify_step5_propagators.py``.  This
verifier changes only the admission scope: the local fixed-gauge perturbative
Gaussian belongs to Step 5A, while equivalence to the finite BV/non-minimal
coefficient integral is a separate Step-5C obligation.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audits/step5a-fixed-kernel.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.verify_step5_propagators import (
    Matrix,
    QComplex,
    add,
    flat_operators,
    identity,
    kronecker,
    momentum_square,
    multiply,
    q,
    scale,
)


H = Fraction(3, 2)
G_SQUARED = Fraction(2, 3)
KAPPA = [[q(2), q(1)], [q(1), q(1)]]
KAPPA_INVERSE = [[q(1), q(-1)], [q(-1), q(2)]]
MOMENTA = ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3))


def sparse_matrix(matrix: Matrix) -> list[dict[str, object]]:
    """Serialize every nonzero exact entry; zero entries are implicit."""

    return [
        {
            "row": row,
            "column": column,
            "re": str(value.re),
            "im": str(value.im),
        }
        for row, entries in enumerate(matrix)
        for column, value in enumerate(entries)
        if value
    ]


def fixed_kernel(momentum: tuple[int, int, int, int]) -> dict[str, Matrix]:
    operators = flat_operators(momentum)
    p_squared = momentum_square(momentum)
    pi_half = operators["Pi_half"]
    pi_zero = operators["Pi_zero"]
    unit = operators["identity"]

    k_phys = scale(-H * p_squared / 2, pi_half)
    k_gf = scale(-H * p_squared / 2, pi_zero)
    k_tot = add(k_phys, k_gf)
    k_tot_expected = scale(-H * p_squared / 2, unit)
    green = scale(-2 * G_SQUARED / p_squared, unit)
    return {
        "Pi_half": pi_half,
        "Pi_zero": pi_zero,
        "K_phys": k_phys,
        "K_gf": k_gf,
        "K_tot": k_tot,
        "K_tot_expected": k_tot_expected,
        "G": green,
        "K_G": multiply(k_tot, green),
        "G_K": multiply(green, k_tot),
        "identity": unit,
    }


def fixed_kernel_checks(momentum: tuple[int, int, int, int]) -> dict[str, bool]:
    matrices = fixed_kernel(momentum)
    p_squared = momentum_square(momentum)
    full_kernel = kronecker(KAPPA, matrices["K_tot"])
    full_green = kronecker(KAPPA_INVERSE, matrices["G"])
    return {
        "grassmann_dimension_is_16": len(matrices["identity"]) == 16
        and all(len(row) == 16 for row in matrices["identity"]),
        "projector_sum_is_identity": add(matrices["Pi_half"], matrices["Pi_zero"])
        == matrices["identity"],
        "K_phys_equals_minus_h_over_2_p2_Pi_half": matrices["K_phys"]
        == scale(-H * p_squared / 2, matrices["Pi_half"]),
        "K_gf_equals_minus_h_over_2_p2_Pi_zero": matrices["K_gf"]
        == scale(-H * p_squared / 2, matrices["Pi_zero"]),
        "K_tot_equals_minus_h_over_2_p2_identity": matrices["K_tot"]
        == matrices["K_tot_expected"],
        "h_equals_g_inverse_squared": H * G_SQUARED == 1,
        "K_tot_G_left_is_identity_16": matrices["K_G"] == matrices["identity"],
        "G_K_tot_right_is_identity_16": matrices["G_K"] == matrices["identity"],
        "kappa_left_inverse": multiply(KAPPA, KAPPA_INVERSE) == identity(2),
        "kappa_right_inverse": multiply(KAPPA_INVERSE, KAPPA) == identity(2),
        "color_Grassmann_left_inverse_32": multiply(full_kernel, full_green)
        == identity(32),
        "color_Grassmann_right_inverse_32": multiply(full_green, full_kernel)
        == identity(32),
    }


def run_verification() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    witnesses: list[dict[str, object]] = []
    for momentum in MOMENTA:
        label = "p_" + "_".join(str(value).replace("-", "m") for value in momentum)
        local_checks = fixed_kernel_checks(momentum)
        checks.extend(
            {"id": f"{label}.{name}", "passed": passed}
            for name, passed in local_checks.items()
        )
        matrices = fixed_kernel(momentum)
        witnesses.append(
            {
                "momentum": list(momentum),
                "p_(4)^2": str(momentum_square(momentum)),
                "basis_order": "1,theta+,theta-,theta+theta-,...,theta+theta-bartheta_dot+bartheta_dot- (bit masks 0..15)",
                "sparse_exact_matrices": {
                    name: sparse_matrix(matrices[name])
                    for name in (
                        "Pi_half",
                        "Pi_zero",
                        "K_phys",
                        "K_gf",
                        "K_tot",
                        "G",
                        "K_G",
                        "G_K",
                    )
                },
            }
        )
    failed = [entry for entry in checks if not entry["passed"]]
    return {
        "schema": 1,
        "scope": "5A.PERTURBATIVE_FF_DRED_SUPERGRAPHS",
        "status": "PASS" if not failed else "FAIL",
        "admission_status": "STEP5A_WICK_KERNEL_ADMITTED" if not failed else "STEP5A_KERNEL_MISMATCH",
        "arithmetic": "EXACT_Q_I_NO_FLOATING_POINT",
        "normalization": {
            "h": str(H),
            "g^2": str(G_SQUARED),
            "identity": "h*g^2=1; equivalently h=g^(-2)",
            "color_metric": [[value.to_json() for value in row] for row in KAPPA],
            "inverse_color_metric": [[value.to_json() for value in row] for row in KAPPA_INVERSE],
        },
        "derived_equations": {
            "K_V^phys": "-(h/2)*kappa_AB*p_(4)^2*Pi_(1/2)",
            "K_V^gf": "-(h/2)*kappa_AB*p_(4)^2*Pi_0",
            "K_V^tot": "-(h/2)*kappa_AB*p_(4)^2*1_16",
            "G_V": "-2*g^2*kappa^AB*1_16/p_(4)^2",
            "left_product": "K_(AB)^tot*G^(BC)=delta_A^C*1_16",
            "right_product": "G^(AB)*K_(BC)^tot=delta^A_C*1_16",
        },
        "perturbative_measure": {
            "density_insertion": "E_measure",
            "value": "0",
            "scope": "REFERENCE_FLAT_STEP5A_ONLY",
            "finite_BV_density_equality": "NOT_CLAIMED; STEP5C_OBLIGATION",
        },
        "totals": {"checks": len(checks), "failed": len(failed)},
        "checks": checks,
        "matrix_witnesses": witnesses,
    }


def main() -> int:
    result = run_verification()
    AUDIT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["totals"], sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
