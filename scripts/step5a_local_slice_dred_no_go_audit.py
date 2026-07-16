#!/usr/bin/env python3
"""Exact finite-cutoff audit of the Step-5A local Fermi--Feynman obstruction."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "audits/step5a-local-slice-dred-no-go.json"
MD_PATH = ROOT / "audits/step5a-local-slice-dred-no-go.md"
Matrix = list[list[Fraction]]


def q(value: int) -> Fraction:
    return Fraction(value, 1)


def eye(n: int) -> Matrix:
    return [[q(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(rows: int, cols: int) -> Matrix:
    return [[q(0) for _ in range(cols)] for _ in range(rows)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), q(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    aug = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [entry / scale for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [
                aug[row][j] - factor * aug[col][j] for j in range(2 * n)
            ]
    return [row[n:] for row in aug]


def block(a: Matrix, r0: int, r1: int, c0: int, c1: int) -> Matrix:
    return [row[c0:c1] for row in a[r0:r1]]


def block2(a00: Matrix, a01: Matrix, a10: Matrix, a11: Matrix) -> Matrix:
    return [a00[i] + a01[i] for i in range(len(a00))] + [
        a10[i] + a11[i] for i in range(len(a10))
    ]


def encode(a: Matrix) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in a]


def naive_localizer() -> dict:
    samples: list[Matrix] = [
        [[q(2), q(1)], [q(1), q(1)]],
        [[q(3), q(-1)], [q(2), q(4)]],
        [[q(1), q(0)], [q(0), q(5)]],
    ]
    rows = []
    for h in samples:
        i_n = eye(2)
        z_n = zeros(2, 2)
        y = block2(z_n, i_n, i_n, [[-x for x in row] for row in h])
        z_expected = block2(h, i_n, i_n, z_n)
        source = [[q(1)], [q(2)]]
        source_big = source + [[q(0)], [q(0)]]
        rows.append(
            {
                "H": encode(h),
                "Y_times_Z_is_identity": mul(y, z_expected) == eye(4),
                "inverse_matches": inverse(y) == z_expected,
                "physical_block_is_H": mul(inverse(y), source_big)[:2]
                == mul(h, source),
            }
        )
    return {
        "formula": "Y_local=[[0,I],[I,-H]], inverse=[[H,I],[I,0]]",
        "samples": rows,
        "all_pass": all(
            all(value for key, value in row.items() if key != "H") for row in rows
        ),
        "properness": (
            "FAIL: the new antighost has no gauge-condition row, is absent from "
            "s(Psi), and leaves an unsaturated odd zero mode."
        ),
    }


def proper_completion() -> dict:
    samples: list[Matrix] = [
        [
            [q(2), q(0), q(1), q(0)],
            [q(0), q(3), q(0), q(1)],
            [q(1), q(0), q(2), q(1)],
            [q(0), q(1), q(1), q(3)],
        ],
        [
            [q(3), q(1), q(1), q(-1)],
            [q(1), q(2), q(0), q(1)],
            [q(1), q(0), q(4), q(1)],
            [q(-1), q(1), q(1), q(5)],
        ],
        [
            [q(1), q(0), q(1), q(0)],
            [q(0), q(2), q(0), q(1)],
            [q(1), q(0), q(3), q(1)],
            [q(0), q(1), q(1), q(4)],
        ],
    ]
    rows = []
    for y in samples:
        z = inverse(y)
        z00 = block(z, 0, 2, 0, 2)
        z0a = block(z, 0, 2, 2, 4)
        za0 = block(z, 2, 4, 0, 2)
        zaa = block(z, 2, 4, 2, 4)
        schur = sub(z00, mul(mul(z0a, inverse(zaa)), za0))
        y00_inv = inverse(block(y, 0, 2, 0, 2))
        rows.append(
            {
                "Y": encode(y),
                "S": encode(schur),
                "Y00_inverse": encode(y00_inv),
                "S_equals_Y00_inverse": schur == y00_inv,
            }
        )
    return {
        "formula": "S=Z00-Z0a*Zaa^{-1}*Za0=Y00^{-1}, Z=Y^{-1}",
        "samples": rows,
        "all_pass": all(row["S_equals_Y00_inverse"] for row in rows),
    }


def build() -> dict:
    step5a = (
        ROOT
        / "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
    ).read_text()
    step3d = (
        ROOT / "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md"
    ).read_text()
    naive = naive_localizer()
    proper = proper_completion()
    checks = {
        "step5a_A_square": "§mathcal A_E^2=§Box_E§mathbf1".replace("§", chr(92))
        in step5a,
        "step5a_nonlocality": (
            "§mathcal Y_{E,§mathrm{FF}}§text{ is nonlocal}".replace("§", chr(92))
            in step5a
        ),
        "step3d_locality": "Let §(§mathcal Y_R§) be an even, invertible, local,".replace(
            "§", chr(92)
        )
        in step3d,
        "step3d_proper_hessian": "§operatorname{Hess}S_{§Psi,R,§nu}".replace(
            "§", chr(92)
        )
        in step3d,
        "step3d_nk_branch": (
            "A separated Nielsen--Kallosh factor exists only on the branch" in step3d
        ),
        "naive_block_identity": naive["all_pass"],
        "proper_completion_schur_identity": proper["all_pass"],
        "dred_trace_split": q(4) - q(4 - 2) == q(2),
    }
    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "artifact": "STEP5A-LOCAL-SLICE-DRED-NO-GO-PROPOSAL",
        "authority_status": "UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY",
        "scope": {
            "included": [
                "quadratic completions admitting the displayed residual-complement normal form",
                "the primary antighost row retains the Step-5A gauge condition F",
                "bijective physical and auxiliary FP maps on the residual complements",
                "invertible auxiliary inverse-multiplier block Z_aa",
                "all auxiliary trivial-pair coordinates integrated",
                "minimal physical action unchanged",
            ],
            "excluded": [
                "nonlocal gauge fermions",
                "new nontrivial minimal fields or a changed physical action",
                "unintegrated auxiliary coordinates",
                "an infinite tower without a finite-cutoff proper Hessian",
            ],
        },
        "checks": checks,
        "naive_localizer": naive,
        "proper_completion": proper,
        "result": (
            "NO_GO_WITHIN_FINITE_LOCAL_TRIVIAL_PAIR_NORMAL_FORM__"
            "DRED_LEDGER_LOCKABLE_SEPARATELY"
        ),
        "blocker": {
            "id": "BLOCKED_STEP5A_LOCAL_FERMI_FEYNMAN_PROPER_SLICE",
            "equation": "H=(h/2)A_E; H^{-1}=2*g^2*A_E/Box_E=Y_E,FF",
            "reason": (
                "Every completion in the audited normal-form class gives H_eff=Y_00^{-1}. "
                "H_eff=H forces Y_00=H^{-1}, exactly the nonlocal Step-5A.79 kernel."
            ),
        },
        "nk": {
            "result": "BLOCKED",
            "reason": (
                "The naive localizer has sY=0 but a rank-zero auxiliary FP row. "
                "A completion in the audited normal-form class restores Y_00=Y_E,FF, so no Step-3D.95b "
                "branch is admissible for the target Fermi--Feynman Hessian."
            ),
        },
        "dred_ledger": {
            "dimension": "d=4-2*epsilon",
            "metric_split": "delta4=hatdelta+brevedelta",
            "projectors": [
                "hatdelta^2=hatdelta",
                "brevedelta^2=brevedelta",
                "hatdelta*brevedelta=0",
                "tr(hatdelta)=d",
                "tr(brevedelta)=2*epsilon",
            ],
            "fourier": (
                "X(x)=integral_p exp(i*p.x)X(p); partial_m -> i*p_m; "
                "Box_E -> -hatp^2"
            ),
            "momenta": (
                "hatdelta*p=p and brevedelta*p=0 for loop and external momenta; "
                "all vertex momenta are incoming"
            ),
            "measure": "mu^(2*epsilon)*integral d^d(hatk)/(2*pi)^d",
            "sigma": (
                "sigma algebra contracts with delta4; no d-dimensional or breve "
                "sigma algebra is introduced"
            ),
            "tensor_pole": (
                "Res integral ell^m ell^n/(ell^2+Delta)^3="
                "hatdelta^(mn)/(64*pi^2)"
            ),
            "ww_numerator_pole": (
                "Res integral (2ell+...)^m(2ell+...)^n/(D0*D1*D2)="
                "hatdelta^(mn)/(16*pi^2)"
            ),
            "cut_mismatch": "hatdelta^(mn)-delta4^(mn)=-brevedelta^(mn)",
            "propagators": {
                "VV_conditional": (
                    "-(2*pi)^d delta^d(p+p') 2*hbar*g^2*kappa^(AB)/hatp^2 "
                    "delta^4(theta1-theta2)"
                ),
                "Phi_tildePhi": (
                    "+(2*pi)^d delta^d(p+p') hbar*g^2*kappa^(AB)/"
                    "(16*hatp^2) barD_1^2 D_1^2 delta^4(theta1-theta2)"
                ),
            },
            "status": (
                "EXACT_LEDGER_PROPOSAL_BUT_INSUFFICIENT_WITHOUT_AN_ADMISSIBLE_SLICE"
            ),
        },
    }


def render_markdown(data: dict) -> str:
    body = """# Step 5A local-slice and DRED no-go audit

Status: NO_GO_WITHIN_FINITE_LOCAL_TRIVIAL_PAIR_NORMAL_FORM__DRED_LEDGER_LOCKABLE_SEPARATELY

Authority: UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY

## 1. Definitions

$$
F:=(-§bar D_E^2V/4,-D_E^2V/4),§qquad
§mathcal A_E:=
§begin{pmatrix}
0&-§bar D_E^2/4§§
-D_E^2/4&0
§end{pmatrix},§qquad
§mathcal A_E^2=§Box_E§mathbf1,§qquad
H:=§frac h2§mathcal A_E.
$$

On the residual complement,

$$
H^{-1}=2g^2§frac{§mathcal A_E}{§Box_E}
=§mathcal Y_{E,§mathrm{FF}}.
$$

## 2. Naive localizer

Add

$$
§mathbf s_E§rho=w,§qquad §mathbf s_Ew=0,§qquad
§operatorname{gh}(§rho,w)=(-1,0),§qquad [§rho]=[w]=1.
$$

Then

$$
§mathcal Y_{§mathrm{loc}}
=§begin{pmatrix}0&§mathbf1§§§mathbf1&-H§end{pmatrix},
§qquad
§mathcal Y_{§mathrm{loc}}^{-1}
=§begin{pmatrix}H&§mathbf1§§§mathbf1&0§end{pmatrix}.
$$

$$
§frac12(F,0)§mathcal Y_{§mathrm{loc}}^{-1}§binom F0
=§frac12FHF.
$$

But

$$
§Psi_{§mathrm{loc}}^{(2)}
=§langle§mathfrak c',F§rangle
-§frac12§langle§mathfrak c',w§rangle
-§frac12§langle§rho,§mathfrak n§rangle
+§frac12§langle§rho,Hw§rangle
$$

gives

$$
§mathbf s_E§Psi_{§mathrm{loc}}^{(2)}
=§langle§mathfrak n,F§rangle
-§langle§mathfrak c',§mathbf s_EF§rangle
-§langle w,§mathfrak n§rangle
+§frac12§langle w,Hw§rangle.
$$

There is no §(§rho§) term. The auxiliary FP row has rank zero, the odd
integral is unsaturated, and Step 3D.74 fails.

## 3. Proper finite completion

Every completion in the audited normal-form class has the residual-complement form

$$
§Psi_E^{(2)}
=§langle u_0,F§rangle+§langle u_a,G§rangle
-§frac12§left§langle(u_0,u_a),
§mathcal Y§binom{v_0}{v_a}§right§rangle,
§qquad
G=KX+BF,
§qquad
§mathbf s_EX=§eta,
§qquad
§mathbf s_E§eta=0.
$$

The ghost Hessian is

$$
-§left§langle(u_0,u_a),
§begin{pmatrix}
§mathcal M&0§§
B§mathcal M&K
§end{pmatrix}
§binom c§eta
§right§rangle.
$$

Properness requires §(§mathcal M§) and §(K§) to be bijective.
Set §(Z:=§mathcal Y^{-1}§). Integrating multipliers and the proper
auxiliary coordinate gives

$$
H_{§mathrm{eff}}
=Z_{00}-Z_{0a}Z_{aa}^{-1}Z_{a0}.
$$

The ordered factorization is

$$
Z=
§begin{pmatrix}§mathbf1&Z_{0a}Z_{aa}^{-1}§§0&§mathbf1§end{pmatrix}
§begin{pmatrix}H_{§mathrm{eff}}&0§§0&Z_{aa}§end{pmatrix}
§begin{pmatrix}§mathbf1&0§§Z_{aa}^{-1}Z_{a0}&§mathbf1§end{pmatrix}.
$$

Thus

$$
§boxed{§mathcal Y_{00}=H_{§mathrm{eff}}^{-1}}.
$$

The target §(H_{§mathrm{eff}}=H§) forces

$$
§boxed{
§mathcal Y_{00}=H^{-1}
=2g^2§frac{§mathcal A_E}{§Box_E}
=§mathcal Y_{E,§mathrm{FF}}}.
$$

This is Step 5A.79. Within the audited normal-form class, a completion with
bijective residual FP blocks and invertible §(Z_{aa}§) reproduces the same
nonlocal primary block.

## 4. Nielsen--Kallosh

The naive block obeys §(§mathbf s_E§mathcal Y_{§mathrm{loc}}=0§), but
its auxiliary FP row has rank zero. A completion in the audited normal-form class forces
§(§mathcal Y_{00}=§mathcal Y_{E,§mathrm{FF}}§). Therefore no Step
3D.95b NK branch is selected for the target Fermi--Feynman Hessian.

## 5. DRED momentum ledger proposal

$$
d:=4-2§epsilon,§qquad
§delta_4^{mn}=§widehat§delta^{mn}+§breve§delta^{mn},
§qquad
§operatorname{tr}§widehat§delta=d,
§qquad
§operatorname{tr}§breve§delta=2§epsilon.
$$

$$
§widehat§delta^2=§widehat§delta,
§qquad
§breve§delta^2=§breve§delta,
§qquad
§widehat§delta§breve§delta=0.
$$

$$
X(x)=§int§frac{d^dp}{(2§pi)^d}e^{ip§cdot x}X(p),
§qquad
§partial_m§mapsto ip_m,
§qquad
§Box_E§mapsto-§widehat p^2,
§qquad
§widehat§delta^m{}_np^n=p^m,
§qquad
§breve§delta^m{}_np^n=0.
$$

$$
§int_{§widehat k}
:=§mu^{2§epsilon}§int§frac{d^d§widehat k}{(2§pi)^d},
§qquad
§widehat k^2
:=§widehat§delta_{mn}§widehat k^m§widehat k^n.
$$

Every vertex is all-incoming. The spinor algebra is four-dimensional:

$$
§sigma_E^m§bar§sigma_E^n+§sigma_E^n§bar§sigma_E^m
=2§delta_4^{mn}§mathbf1.
$$

$$
§operatorname*{Res}_{§epsilon=0}
§int_{§widehat§ell}
§frac{§widehat§ell^m§widehat§ell^n}
{(§widehat§ell^2+§Delta)^3}
=§frac{§widehat§delta^{mn}}{64§pi^2}.
$$

$$
§operatorname*{Res}_{§epsilon=0}
§int_{§widehat§ell}
§frac{(2§widehat§ell+§cdots)^m(2§widehat§ell+§cdots)^n}
{D_0D_1D_2}
=§frac{§widehat§delta^{mn}}{16§pi^2}.
$$

The cut contact carries §(§delta_4^{mn}§), so

$$
§boxed{
§widehat§delta^{mn}-§delta_4^{mn}
=-§breve§delta^{mn}}.
$$

The conditional propagators are

$$
§langle V^A(p,§vartheta_1)V^B(p',§vartheta_2)§rangle_E
=-(2§pi)^d§delta^d(p+p')
§frac{2§hbar g^2§kappa^{AB}}{§widehat p^2}
§delta^4(§vartheta_1-§vartheta_2),
$$

$$
§langle§Phi^A(p,1)§widetilde§Phi^B(p',2)§rangle_E
=(2§pi)^d§delta^d(p+p')
§frac{§hbar g^2§kappa^{AB}}{16§widehat p^2}
§bar D_1^2D_1^2§delta^4(§vartheta_1-§vartheta_2).
$$

They remain conditional because the local proper slice is absent.

## 6. Exact checks

| check | result |
|---|---|
"""
    rows = "\n".join(
        "| " + name + " | " + ("PASS" if passed else "FAIL") + " |"
        for name, passed in data["checks"].items()
    )
    return body.replace("§", chr(92)) + rows + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = build()
    if not all(data["checks"].values()):
        print(json.dumps(data, indent=2, sort_keys=True))
        return 1
    if args.write:
        JSON_PATH.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        MD_PATH.write_text(render_markdown(data))
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
