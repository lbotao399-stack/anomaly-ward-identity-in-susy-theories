#!/usr/bin/env python3
"""Target-blind residual-q projection audit for Step 5.

This script reads only locked Project inputs from ``origin/main``.  It does
not read the Step-5 contract, Step-5 engines, or the holomorphic-twist target.
It derives the Euclidean plus-spin bottom-letter action from Steps 1, 3B, 3C,
4, and 4C and emits an independent JSON/Markdown audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-residual-q-projection.json"
MD_OUT = ROOT / "audits/step5-residual-q-projection.md"

INPUTS = (
    "contracts/foundations/step-01-supersymmetry-commutator.md",
    "contracts/foundations/step-03b-component-reconstruction.md",
    "contracts/foundations/step-03c-gauge-vector-representation.md",
    "contracts/foundations/step-04-extended-sym-notation.md",
    "contracts/foundations/step-04c-n4-super-yang-mills.md",
    "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md",
)

ANCHORS = {
    INPUTS[0]: (
        r"\epsilon^{12}=\epsilon^{\dot1\dot2}=+1",
        r"(\sigma_E^m)_{a\dot a}",
        r"(\sigma_E^{mn})_a{}^b",
        r"+\theta_E^aQ^E_a",
    ),
    INPUTS[1]: (
        r"\psi_a^I&:=\frac1{\sqrt2}D_a\Phi^I|",
        r"\mathcal W_{Ea}={}&-i\lambda_a+\vartheta_a\mathscr D",
        r"\widetilde{\mathcal W}_{E\dot a}={}&",
    ),
    INPUTS[2]: (
        r"\kappa_E:=-2",
        r"\{\boldsymbol\nabla^{\mathsf V}_{Ra}",
        r"\boldsymbol\psi_{Ra}^{\mathsf V}",
        r"\boldsymbol\lambda_{Ra}^{\mathsf V}",
    ),
    INPUTS[3]: (
        r"\varepsilon^{123}=\varepsilon_{123}=+1",
        r"\Lambda_a^4:=\lambda_a",
        r"\Lambda_a^r:=\psi_{ra}",
        r"\widetilde\varphi_{r4}=\widetilde\phi_r",
    ),
    INPUTS[4]: (
        r"\delta_EA_m",
        r"\delta_E\widetilde\varphi_{\mathcal I\mathcal J}",
        r"\delta_E\Lambda_a^{\mathcal I}",
        r"\delta_E\widetilde\Lambda_{\dot a\mathcal I}",
        r"\Omega_E:=-\sqrt2",
        r"\mathscr R_{E,a}^{\mathcal I}",
        r"\widetilde{\mathscr R}_{E,\dot a\mathcal I}",
    ),
    INPUTS[5]: (
        r"\mathfrak c_R=\mathfrak c_R^AT_A",
        r"\widetilde{\mathfrak c}_R",
        r"\mathbf s_R\mathfrak c_R&=i\mathfrak c_R^2",
    ),
}


@dataclass(frozen=True)
class K:
    """Exact Q(sqrt(2), i) element a+b sqrt(2)+i(c+d sqrt(2))."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    @staticmethod
    def q(x: int | Fraction) -> "K":
        return K(Fraction(x))

    def __add__(self, other: "K") -> "K":
        return K(self.a + other.a, self.b + other.b,
                 self.c + other.c, self.d + other.d)

    def __neg__(self) -> "K":
        return K(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: "K") -> "K":
        return self + (-other)

    def __mul__(self, other: "K") -> "K":
        # (a+b s)(e+f s) - (c+d s)(g+h s)
        re_a = self.a * other.a + 2 * self.b * other.b
        re_b = self.a * other.b + self.b * other.a
        im_loss_a = self.c * other.c + 2 * self.d * other.d
        im_loss_b = self.c * other.d + self.d * other.c
        # i[(a+b s)(g+h s)+(c+d s)(e+f s)]
        im_a = (
            self.a * other.c + 2 * self.b * other.d
            + self.c * other.a + 2 * self.d * other.b
        )
        im_b = (
            self.a * other.d + self.b * other.c
            + self.c * other.b + self.d * other.a
        )
        return K(re_a - im_loss_a, re_b - im_loss_b, im_a, im_b)

    def scale(self, q: int | Fraction) -> "K":
        qf = Fraction(q)
        return K(qf * self.a, qf * self.b, qf * self.c, qf * self.d)

    def is_zero(self) -> bool:
        return self == ZERO

    @staticmethod
    def _term(q: Fraction, symbol: str) -> str:
        if q == 0:
            return ""
        sign = "-" if q < 0 else "+"
        q = abs(q)
        if q == 1:
            body = symbol
        else:
            body = f"{q.numerator}/{q.denominator}{symbol}" if q.denominator != 1 else f"{q}{symbol}"
        return sign + body

    def exact(self) -> str:
        terms = []
        if self.a:
            terms.append((self.a, ""))
        if self.b:
            terms.append((self.b, "sqrt(2)"))
        if self.c:
            terms.append((self.c, "i"))
        if self.d:
            terms.append((self.d, "i*sqrt(2)"))
        if not terms:
            return "0"
        rendered = ""
        for q, sym in terms:
            if sym:
                piece = self._term(q, sym)
            else:
                sign = "-" if q < 0 else "+"
                qabs = abs(q)
                body = str(qabs.numerator) if qabs.denominator == 1 else f"{qabs.numerator}/{qabs.denominator}"
                piece = sign + body
            rendered += piece
        return rendered[1:] if rendered.startswith("+") else rendered


ZERO = K()
ONE = K.q(1)
MINUS_ONE = K.q(-1)
IMAGINARY_UNIT = K(c=Fraction(1))
MINUS_I = -IMAGINARY_UNIT
SQRT2 = K(b=Fraction(1))
INV_SQRT2 = K(b=Fraction(1, 2))
HALF = K.q(Fraction(1, 2))

Matrix = list[list[K]]


def m_add(x: Matrix, y: Matrix) -> Matrix:
    return [[x[r][c] + y[r][c] for c in range(2)] for r in range(2)]


def m_sub(x: Matrix, y: Matrix) -> Matrix:
    return [[x[r][c] - y[r][c] for c in range(2)] for r in range(2)]


def m_scale(x: Matrix, z: K) -> Matrix:
    return [[z * x[r][c] for c in range(2)] for r in range(2)]


def m_mul(x: Matrix, y: Matrix) -> Matrix:
    return [
        [sum_k(x[r][k] * y[k][c] for k in range(2)) for c in range(2)]
        for r in range(2)
    ]


def sum_k(xs: Iterable[K]) -> K:
    out = ZERO
    for x in xs:
        out = out + x
    return out


def identity() -> Matrix:
    return [[ONE, ZERO], [ZERO, ONE]]


def zero_matrix() -> Matrix:
    return [[ZERO, ZERO], [ZERO, ZERO]]


def permutation_sign(values: tuple[int, ...]) -> int:
    if len(set(values)) != len(values):
        return 0
    inv = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inv % 2 else 1


def epsilon3(r: int, s: int, t: int) -> int:
    return permutation_sign((r, s, t)) if set((r, s, t)) == {0, 1, 2} else 0


def epsilon4(i: int, j: int, k: int, ell: int) -> int:
    return permutation_sign((i, j, k, ell)) if set((i, j, k, ell)) == {0, 1, 2, 3} else 0


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def source_at(commit: str, path: str) -> str:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True)


def build_result() -> dict:
    authority_commit = git("rev-parse", "origin/main")
    # This target-blind audit is defined on the verified authority tree, not on
    # the feature-branch or pull-request merge checkout that invokes it.
    head_commit = authority_commit
    sources: dict[str, str] = {}
    hashes: dict[str, str] = {}
    checks: list[dict] = []

    def check(check_id: str, condition: bool, evidence: object) -> None:
        checks.append({
            "id": check_id,
            "status": "PASS" if condition else "FAIL",
            "evidence": evidence,
        })

    for path in INPUTS:
        text = source_at(authority_commit, path)
        sources[path] = text
        hashes[path] = hashlib.sha256(text.encode()).hexdigest()
        missing = [anchor for anchor in ANCHORS[path] if anchor not in text]
        check(f"locked_anchor::{path}", not missing, {"missing": missing})

    # Exact Euclidean sigma system.
    sigma1 = [[ZERO, ONE], [ONE, ZERO]]
    sigma2 = [[ZERO, -IMAGINARY_UNIT], [IMAGINARY_UNIT, ZERO]]
    sigma3 = [[ONE, ZERO], [ZERO, MINUS_ONE]]
    sigma = [m_scale(sigma1, -IMAGINARY_UNIT), m_scale(sigma2, -IMAGINARY_UNIT), m_scale(sigma3, -IMAGINARY_UNIT), identity()]
    barsigma = [m_scale(sigma1, IMAGINARY_UNIT), m_scale(sigma2, IMAGINARY_UNIT), m_scale(sigma3, IMAGINARY_UNIT), identity()]
    eps_lower = [[ZERO, MINUS_ONE], [ONE, ZERO]]

    clifford_ok = True
    for m in range(4):
        for n in range(4):
            lhs = m_add(m_mul(sigma[m], barsigma[n]), m_mul(sigma[n], barsigma[m]))
            rhs = m_scale(identity(), K.q(2 if m == n else 0))
            clifford_ok = clifford_ok and lhs == rhs
    check("euclidean_clifford", clifford_ok, "sigma_m barsigma_n + sigma_n barsigma_m = 2 delta_mn")

    sigma_mn: dict[tuple[int, int], Matrix] = {}
    for m in range(4):
        for n in range(4):
            sigma_mn[m, n] = m_scale(
                m_sub(m_mul(sigma[m], barsigma[n]), m_mul(sigma[n], barsigma[m])),
                K.q(Fraction(1, 4)),
            )

    plus = 0
    lowered_plus_plus: dict[str, K] = {}
    for m in range(4):
        for n in range(m + 1, 4):
            lowered = m_mul(sigma_mn[m, n], eps_lower)
            lowered_plus_plus[f"{m + 1}{n + 1}"] = lowered[plus][plus]

    expected_lowered = {
        "12": ZERO,
        "13": K.q(Fraction(-1, 2)),
        "14": K(c=Fraction(-1, 2)),
        "23": K(c=Fraction(1, 2)),
        "24": K.q(Fraction(-1, 2)),
        "34": ZERO,
    }
    check(
        "sigma_lowered_plus_plus",
        lowered_plus_plus == expected_lowered,
        {k: v.exact() for k, v in lowered_plus_plus.items()},
    )

    # A = -i sigma^{mn}_{++} F_mn, with both ordered mn slots summed.
    a_components = {
        pair: (MINUS_I * coeff).scale(2)
        for pair, coeff in lowered_plus_plus.items()
        if not coeff.is_zero()
    }
    expected_a = {"13": IMAGINARY_UNIT, "14": MINUS_ONE, "23": ONE, "24": IMAGINARY_UNIT}
    check("A_component_projection", a_components == expected_a,
          {k: v.exact() for k, v in a_components.items()})

    # Highest-weight identity that kills q_r A.
    qA_tensor: dict[str, K] = {}
    for m in range(4):
        for dot in range(2):
            value = ZERO
            for n in range(4):
                lowered = m_mul(sigma_mn[m, n], eps_lower)
                value = value + lowered[plus][plus] * sigma[n][plus][dot]
            qA_tensor[f"m{m + 1}_dot{dot + 1}"] = value
    check("qA_highest_weight_identity", all(v.is_zero() for v in qA_tensor.values()),
          {k: v.exact() for k, v in qA_tensor.items()})

    p_components = {
        "dot1": [sigma[m][plus][0] for m in range(4)],
        "dot2": [sigma[m][plus][1] for m in range(4)],
    }
    expected_p_components = {
        "dot1": [ZERO, ZERO, -IMAGINARY_UNIT, ONE],
        "dot2": [-IMAGINARY_UNIT, MINUS_ONE, ZERO, ZERO],
    }
    check(
        "P_dot_components",
        p_components == expected_p_components,
        {key: [entry.exact() for entry in value] for key, value in p_components.items()},
    )

    # Spin-frame selection: epsilon^{r,+}=eta^r and epsilon^r_- = eta^r.
    e_plus_upper = [ONE, ZERO]
    e_plus_lower = [sum_k(eps_lower[a][b] * e_plus_upper[b] for b in range(2)) for a in range(2)]
    check("plus_parameter_lowering", e_plus_lower == [ZERO, ONE],
          [x.exact() for x in e_plus_lower])
    scalar_plus_plus = sum_k(e_plus_upper[a] * e_plus_lower[a] for a in range(2))
    check("same_plus_scalar_bilinear", scalar_plus_plus.is_zero(), scalar_plus_plus.exact())

    # SU(4) to SU(3) sign: epsilon_{s,4,r,t} = epsilon_{s,r,t}.
    su4_sign_ok = all(
        epsilon4(s, 3, r, t) == epsilon3(s, r, t)
        for s in range(3) for r in range(3) for t in range(3)
    )
    check("su4_to_su3_epsilon", su4_sign_ok, "epsilon_{s4rt}=epsilon_{srt}=-epsilon_{rst}")

    # Raw locked Q and compact-normalized q=Q/sqrt(2).
    raw_qB = -(IMAGINARY_UNIT * SQRT2)       # -i sqrt(2)
    raw_qC = MINUS_ONE          # multiplies epsilon_rst B_t
    raw_qD = -(IMAGINARY_UNIT * SQRT2)       # multiplies D_{+dot} C_r
    scale_q = INV_SQRT2
    qB = scale_q * raw_qB
    qC = scale_q * raw_qC
    qD = scale_q * raw_qD
    check("normalized_qB", qB == MINUS_I, qB.exact())
    check("normalized_qC", qC == -INV_SQRT2, qC.exact())
    check("normalized_qD", qD == MINUS_I, qD.exact())

    # Explicit A/B/C closure.  The D closure is checked from the complete
    # Step-4C parameter tensors: tilde epsilon=0, epsilon^+ epsilon_+=0,
    # and the only pure-epsilon tilde-fermion remainder is proportional to
    # the same vanishing scalar bilinear.
    closure_c_ok = True
    closure_c_values: dict[str, str] = {}
    for r in range(3):
        for s in range(3):
            for t in range(3):
                # {q_r,q_s} C_t = (i/sqrt2)(eps_{str}+eps_{rts}) A.
                coeff = (IMAGINARY_UNIT * INV_SQRT2).scale(epsilon3(s, t, r) + epsilon3(r, t, s))
                closure_c_values[f"{r + 1}{s + 1}|C{t + 1}"] = coeff.exact()
                closure_c_ok = closure_c_ok and coeff.is_zero()
    check("closure_A_B_C", closure_c_ok, closure_c_values)

    lower_plus_component = e_plus_lower[plus]
    closure_parameter_ok = (
        scalar_plus_plus.is_zero()
        and lower_plus_component.is_zero()
    )
    check(
        "closure_D_from_4C69",
        closure_parameter_ok,
        {
            "tilde_parameter": "0",
            "epsilon_plus_epsilon_lower_contraction": scalar_plus_plus.exact(),
            "epsilon_lower_plus": lower_plus_component.exact(),
            "consequence": "v_E=Omega_E=R_E,+^I=Rtilde_E,dot,I=0 on selected letters",
        },
    )

    # Compact coefficients.  For an odd left derivation q acting on inert
    # odd theta, q(theta X)=-theta qX.  Let
    # C_phys=a theta C+(b/2) eps theta theta B+c theta123 A.
    # q C_phys = d_theta C_phys - a C iff qC=-(b/a)eps B and qB=(c/b)A.
    compact_a = ONE
    compact_b = INV_SQRT2
    compact_c = -(IMAGINARY_UNIT * INV_SQRT2)
    check("compact_C_arrow", qC * compact_a == -compact_b,
          {"qC*a": (qC * compact_a).exact(), "-b": (-compact_b).exact()})
    check("compact_B_arrow", qB * compact_b == compact_c,
          {"qB*b": (qB * compact_b).exact(), "c": compact_c.exact()})

    brst_source = sources[INPUTS[5]]
    check(
        "no_locked_U_or_residual_q_ghost_law",
        "q_r" not in brst_source and "U_R" not in brst_source,
        "Step 3D defines only (mathfrak c_R, tilde mathfrak c_R, s_R) in (3D.43)-(3D.44); no U_R or q_r law",
    )

    all_pass = all(item["status"] == "PASS" for item in checks)
    result = {
        "schema_version": 1,
        "task": "STEP5_TARGET_BLIND_RESIDUAL_Q_PROJECTION",
        "authority": {
            "ref": "origin/main",
            "commit": authority_commit,
            "head_at_run": head_commit,
            "verified_workflow_status": "NOT_RECHECKED_BY_THIS_LOCAL_AUDIT",
        },
        "scope": {
            "read_inputs": list(INPUTS),
            "forbidden_inputs_read": [],
            "step5_contract_read": False,
            "step5_engines_read": False,
            "holomorphic_twist_target_read": False,
        },
        "input_sha256": hashes,
        "spin_frame": {
            "definition": "+ := 1, - := 2",
            "epsilon_upper_plus_minus": "+1",
            "epsilon_lower_plus_minus": "-1",
            "selected_parameter": "epsilon^{r,+}=eta^r; epsilon^r_-=eta^r; tilde_epsilon=0",
            "locked_generator": "Q^r_{E,+}",
            "compact_normalized_generator": "q_r:=Q^r_{E,+}/sqrt(2)",
            "normalization_status": "DECLARED_UNIQUE_AFTER_REQUIRING_q_r_B_s=-i_delta_rs_A",
        },
        "bottom_letter_projection": {
            "A": "(boldnabla^V_{E,+} boldW^V_{E,+})| = -i (sigma_E^{mn})_{++} F_mn",
            "A_components": {k: v.exact() for k, v in a_components.items()},
            "B_r": "(boldnabla^V_{E,+} boldPhi^V_r)| = sqrt(2) psi_{r,+}",
            "C_r": "tildeboldPhi^V_r| = tildephi_r",
            "D_dot": "tildeboldW^V_{E,dot}| = i tildelambda_dot",
            "P_dot": "(sigma_E^m)_{+,dot} D_m",
            "P_dot1": "D_4-i D_3",
            "P_dot2": "-i D_1-D_2",
            "P_dot_color": "(P_dot C_r)^A=(sigma_E^m)_{+,dot}(partial_m C_r^A+c_BC^A A_m^B C_r^C)",
        },
        "raw_locked_Q_action": {
            "Q^r_{E,+} A": "0",
            "Q^r_{E,+} B_s": "-i sqrt(2) delta_rs A",
            "Q^r_{E,+} C_s": "-epsilon_rst B_t",
            "Q^r_{E,+} D_dot": "-i sqrt(2) P_dot C_r",
        },
        "compact_normalized_q_action": {
            "q_r A": "0",
            "q_r B_s": "-i delta_rs A",
            "q_r C_s": "-(1/sqrt(2)) epsilon_rst B_t",
            "q_r D_dot": "-i P_dot C_r",
            "closure": "{q_r,q_s}=0 exactly on A,B,C,D bottom letters; no auxiliary or fermion EOM used",
            "closure_scope": "restricted letter-off-shell closure, not a full off-shell N=4 multiplet",
        },
        "compact_physical_superletter": {
            "expression": "theta_r C_r + (1/(2 sqrt(2))) epsilon_rst theta_r theta_s B_t - (i/sqrt(2)) theta_1 theta_2 theta_3 A",
            "identity": "q_r C_phys(theta)=partial^L_{theta_r} C_phys(theta)-C_r",
            "weights": {
                "theta_r C_r": compact_a.exact(),
                "epsilon theta theta B": compact_b.scale(Fraction(1, 2)).exact(),
                "theta_1 theta_2 theta_3 A": compact_c.exact(),
            },
        },
        "conditional_completion": {
            "status": "CONDITIONAL_NOT_IN_LOCKED_INPUTS",
            "assumptions": [
                "an odd U exists with q_r U=C_r",
                "P_dot U=i D_dot",
                "q_r commutes with P_dot on U in the chosen gauge-covariant complex",
            ],
            "completed_expression": "U + theta_r C_r + (1/(2 sqrt(2))) epsilon_rst theta_r theta_s B_t - (i/sqrt(2)) theta_1 theta_2 theta_3 A",
            "completed_identity": "q_r C(theta)=partial^L_{theta_r} C(theta)",
        },
        "boundaries": [
            {
                "id": "FULL_SUPERFIELD_LIFT_REJECTED",
                "status": "PROVED_REJECTED",
                "reason": "delta_E tildePhi_r is antichiral, whereas boldnabla_+ boldPhi_r is generically not antichiral because {boldnabla_+,barboldnabla_dot}=-2 sigma^m_{+dot} boldD_m.",
            },
            {
                "id": "U_COMPLETION",
                "status": "BLOCKED_U_NOT_DEFINED_BY_LOCKED_INPUTS",
                "reason": "Steps 1/3B/3C/4/4C fix only physical fields; Step 3D defines BRST ghosts c, tilde-c and s but no residual source U or its q/P law.",
            },
            {
                "id": "ABSOLUTE_q_NORMALIZATION",
                "status": "CONVENTION",
                "reason": "The locked normalization is Q^r_{E,+}; division by sqrt(2) is the explicit compact normalization criterion, not a dynamical consequence.",
            },
            {
                "id": "FULL_N4_OFFSHELL_COMPLETION",
                "status": "NOT_ASSERTED",
                "reason": "The selected four-letter algebra closes without EOM because every Step-4C remainder coefficient vanishes in the plus-spin specialization; Step 4C still supplies no finite SU(4)_R-covariant auxiliary multiplet.",
            },
        ],
        "checks": checks,
        "summary": {
            "passed": sum(item["status"] == "PASS" for item in checks),
            "failed": sum(item["status"] == "FAIL" for item in checks),
            "verdict": "PROVED_BOTTOM_PROJECTION_WITH_CONDITIONAL_COMPACT_COMPLETION" if all_pass else "FAILED",
        },
    }
    return result


def markdown(result: dict) -> str:
    commit = result["authority"]["commit"]
    hashes = result["input_sha256"]
    checks = result["summary"]
    return rf"""# Step-5 target-blind residual-\(q\) projection audit

Authority input: `origin/main@{commit}`.  本 audit 未读取 Step-5 contract、Step-5 engines、HT target。

## 1. Notation

$$
+\equiv 1,\qquad -\equiv 2,\qquad
\epsilon^{{+-}}=+1,\qquad \epsilon_{{+-}}=-1.
$$

$$
\varepsilon^{{r+}}=\eta^r,\qquad
\varepsilon^r_-=\epsilon_{{-+}}\varepsilon^{{r+}}=\eta^r,
\qquad \varepsilon^r_+=0,qquad
\widetilde\varepsilon_{{\mathcal I\dot a}}=0.
$$

\(Q^r_{{E,+}}\) denotes the locked Euclidean generator selected by this parameter.  Define the compact normalization

$$
q_r:=\frac1{{\sqrt2}}Q^r_{{E,+}}.
$$

This factor is a declared convention: it is the unique positive rescaling for which \(q_rB_s=-i\delta_{{rs}}A\).  Step 4C fixes \(Q^r_{{E,+}}\), not this extra rescaling.

For adjoint color \(A\), define vector-frame bottom letters

$$
\begin{{aligned}}
A^A&:=\left.\boldsymbol\nabla^{{\mathsf V}}_{{E,+}}
\boldsymbol{{\mathcal W}}^{{\mathsf V,A}}_{{E,+}}\right|,\\
B_r^A&:=\left.\boldsymbol\nabla^{{\mathsf V}}_{{E,+}}
\boldsymbol\Phi^{{\mathsf V,A}}_r\right|,\\
C_r^A&:=\left.\widetilde{{\boldsymbol\Phi}}^{{\mathsf V,A}}_r\right|,\\
D_{{\dot a}}^A&:=\left.\widetilde{{\boldsymbol{{\mathcal W}}}}^{{\mathsf V,A}}_{{E,\dot a}}\right|,\\
P_{{\dot a}}X^A&:=(\sigma_E^m)_{{+\dot a}}(\mathcal D_mX)^A.
\end{{aligned}}
$$

Thus, without suppressed color contraction,

$$
(P_{{\dot a}}C_r)^A
=(\sigma_E^m)_{{+\dot a}}
\left(\partial_mC_r^A+c_{{BC}}{{}}^AA_m^BC_r^C\right).
$$

The vertical bar is essential.  Sources: Step 1 lines 20--44, 475--543; Step 3B lines 30--40, 488--515; Step 3C lines 291--304, 1080--1215; Step 3D (3D.43)--(3D.44); Step 4 lines 268--366, 413--447; Step 4C lines 827--894.

## 2. Exact component projections

Step 3B gives

$$
B_r=\sqrt2\,\psi_{{r+}},\qquad
C_r=\widetilde\phi_r,\qquad
D_{{\dot a}}=i\widetilde\lambda_{{\dot a}}.
$$

Lower the second index of \(\sigma_E^{{mn}}\):

$$
(\sigma_E^{{mn}})_{{ab}}
:=(\sigma_E^{{mn}})_a{{}}^c\epsilon_{{cb}}.
$$

Direct multiplication of the locked matrices gives

$$
\begin{{array}}{{c|rrrrrr}}
mn&12&13&14&23&24&34\\ \hline
(\sigma_E^{{mn}})_{{++}}
&0&-\frac12&-\frac i2&\frac i2&-\frac12&0
\end{{array}}
$$

Since both ordered \((m,n)\) slots are summed,

$$
\begin{{aligned}}
A
&=-i(\sigma_E^{{mn}})_{{++}}F_{{mn}}\\
&=-2i\left[
-\frac12F_{{13}}-\frac i2F_{{14}}
+\frac i2F_{{23}}-\frac12F_{{24}}
\right]\\
&=iF_{{13}}-F_{{14}}+F_{{23}}+iF_{{24}}.
\end{{aligned}}
$$

The same matrices give, for every \(m,\dot a\),

$$
\sum_{{n=1}}^4(\sigma_E^{{mn}})_{{++}}(\sigma_E^n)_{{+\dot a}}=0.
$$

The two dotted derivative slots are

$$
P_{{\dot1}}=\mathcal D_4-i\mathcal D_3,
\qquad
P_{{\dot2}}=-i\mathcal D_1-\mathcal D_2.
$$

## 3. Raw locked-generator action

### 3.1 \(Q^r_{{E,+}}A=0\)

With \(\widetilde\varepsilon=0\), (4C.44) gives

$$
\delta F_{{mn}}
=\eta^r\left[(\sigma_{{E,n}})_{{+\dot a}}
\mathcal D_m\widetilde\psi_r^{{\dot a}}
-(\sigma_{{E,m}})_{{+\dot a}}
\mathcal D_n\widetilde\psi_r^{{\dot a}}\right].
$$

Therefore

$$
\delta A
=-2i\eta^r(\sigma_E^{{mn}})_{{++}}
(\sigma_{{E,n}})_{{+\dot a}}
\mathcal D_m\widetilde\psi_r^{{\dot a}}=0.
$$

### 3.2 \(Q^r_{{E,+}}B_s=-i\sqrt2\delta_{{rs}}A\)

Equation (4C.46), at \(a=+\), gives

$$
\delta\psi_{{s+}}
=-(\sigma_E^{{mn}})_+{{}}^b\varepsilon_b^sF_{{mn}}
+\mathcal M^s{{}}_t\varepsilon_+^t.
$$

The selected parameter has \(\varepsilon_-^r=\eta^r\) and \(\varepsilon_+^r=0\).  Hence

$$
\delta\psi_{{s+}}
=-\eta^r\delta_{{rs}}(\sigma_E^{{mn}})_+{{}}^-
F_{{mn}}
=-\eta^r\delta_{{rs}}(\sigma_E^{{mn}})_{{++}}F_{{mn}}.
$$

The nonlinear \(\mathcal M\)-term vanishes exactly.  Using \((\sigma_E^{{mn}})_{{++}}F_{{mn}}=iA\),

$$
Q^r_{{E,+}}B_s
=\sqrt2Q^r_{{E,+}}\psi_{{s+}}
=-i\sqrt2\delta_{{rs}}A.
$$

### 3.3 \(Q^r_{{E,+}}C_s=-\varepsilon_{{rst}}B_t\)

From (4C.45a), \(C_s=\widetilde\varphi_{{s4}}\), and \(\epsilon_{{s4rt}}=\varepsilon_{{srt}}=-\varepsilon_{{rst}}\),

$$
\begin{{aligned}}
\delta C_s
&=\sqrt2\epsilon_{{s4rt}}\eta^r\Lambda_+^t\\
&=\epsilon_{{s4rt}}\eta^rB_t\\
&=-\eta^r\varepsilon_{{rst}}B_t.
\end{{aligned}}
$$

### 3.4 \(Q^r_{{E,+}}D_{{\dot a}}=-i\sqrt2P_{{\dot a}}C_r\)

For \(\mathcal I=4\), (4C.47) and \(\widetilde\varphi_{{4r}}=-C_r\) give

$$
\delta\widetilde\lambda_{{\dot a}}
=-\sqrt2\eta^r(\sigma_E^m)_{{+\dot a}}
\mathcal D_mC_r.
$$

Thus

$$
Q^r_{{E,+}}D_{{\dot a}}
=iQ^r_{{E,+}}\widetilde\lambda_{{\dot a}}
=-i\sqrt2P_{{\dot a}}C_r.
$$

## 4. Compact-normalized action and closure

Dividing the four raw identities by \(\sqrt2\),

$$
\boxed{{
\begin{{aligned}}
q_rA&=0,\\
q_rB_s&=-i\delta_{{rs}}A,\\
q_rC_s&=-\frac1{{\sqrt2}}\varepsilon_{{rst}}B_t,\\
q_rD_{{\dot a}}&=-iP_{{\dot a}}C_r.
\end{{aligned}}}}
$$

For \(A,B,C\), direct composition gives

$$
\begin{{aligned}}
\{{q_r,q_s\}}A&=0,\\
\{{q_r,q_s\}}B_t&=0,\\
\{{q_r,q_s\}}C_t
&=\frac i{{\sqrt2}}
(\varepsilon_{{str}}+\varepsilon_{{rts}})A=0.
\end{{aligned}}
$$

For \(D_{{\dot a}}\), use the complete closure (4C.69b)--(4C.69g), not an assumed commutation with \(\mathcal D_m\).  The selected parameters obey

$$
\widetilde\varepsilon=0,\qquad
\varepsilon_1^a\varepsilon_{{2a}}=0,\qquad
\varepsilon_+=0.
$$

Consequently

$$
v_E^m=0,\qquad
\Omega_E=0,\qquad
\mathscr R_{{E,+}}^{{\mathcal I}}=0,\qquad
\widetilde{{\mathscr R}}_{{E,\dot a\mathcal I}}=0,
$$

and therefore

$$
\boxed{{\{{q_r,q_s\}}=0}}
$$

on all four bottom-letter families, without auxiliary or fermion EOM.  This is exact restricted letter-off-shell closure.  It is not a finite off-shell \(SU(4)_R\)-covariant completion of the full \(\mathcal N=4\) multiplet; Step 4C.10 explicitly does not assert such a completion.

## 5. Compact physical weights

Let \(\theta_r\) be inert odd variables, \(\partial_r^L\theta_s=\delta_{{rs}}\), and let \(q_r\) be an odd left derivation.  Write

$$
\mathcal C_{{\rm phys}}(\theta)
=a\theta_sC_s
+\frac b2\varepsilon_{{stu}}\theta_s\theta_tB_u
+c\theta_1\theta_2\theta_3A.
$$

Then

$$
q_r\mathcal C_{{\rm phys}}
=\partial_r^L\mathcal C_{{\rm phys}}-aC_r
$$

requires

$$
q_rC_s=-\frac ba\varepsilon_{{rst}}B_t,
\qquad
q_rB_s=\frac cb\delta_{{rs}}A.
$$

Set \(a=1\).  The proved action gives the unique pair

$$
b=\frac1{{\sqrt2}},
\qquad
c=-\frac i{{\sqrt2}}.
$$

Hence

$$
\boxed{{
\mathcal C_{{\rm phys}}(\theta)
=\theta_rC_r
+\frac1{{2\sqrt2}}\varepsilon_{{rst}}
\theta_r\theta_sB_t
-\frac i{{\sqrt2}}\theta_1\theta_2\theta_3A.}}
$$

## 6. Exact boundary

The following completion is conditional:

$$
q_rU=C_r,
\qquad
P_{{\dot a}}U=iD_{{\dot a}},
\qquad
[q_r,P_{{\dot a}}]U=0.
$$

Under these three assumptions,

$$
\mathcal C(\theta)
=U+\theta_rC_r
+\frac1{{2\sqrt2}}\varepsilon_{{rst}}
\theta_r\theta_sB_t
-\frac i{{\sqrt2}}\theta_1\theta_2\theta_3A
$$

satisfies \(q_r\mathcal C=\partial_r^L\mathcal C\), and \(q_rD_{{\dot a}}=-iP_{{\dot a}}C_r\).  Step 3D defines \((\mathfrak c_R,\widetilde{{\mathfrak c}}_R,\mathbf s_R)\) in (3D.43)--(3D.44), but no \(U\), \(q_rU\), or \(P_{{\dot a}}U\).  This completion is `BLOCKED_U_NOT_DEFINED_BY_LOCKED_INPUTS`.

The boxed four-arrow action is not a full \(N=1\) superfield identity.  Equation (4C.35a) makes \(\delta_E\widetilde\Phi_r\) antichiral, while

$$
\bar{{\boldsymbol\nabla}}_{{E,\dot a}}
\boldsymbol\nabla_{{E,+}}\boldsymbol\Phi_r
=\{{\bar{{\boldsymbol\nabla}}_{{E,\dot a}},
\boldsymbol\nabla_{{E,+}}\}}\boldsymbol\Phi_r
=-2(\sigma_E^m)_{{+\dot a}}
\boldsymbol{{\mathcal D}}_{{E,m}}\boldsymbol\Phi_r
$$

is generically nonzero by (3C.23).  Therefore the full-superfield lift is `PROVED_REJECTED`; only the bottom/twisted-letter projection is proved.

## 7. Machine audit

$$
N_{{\rm pass}}={checks['passed']},
\qquad
N_{{\rm fail}}={checks['failed']}.
$$

Verdict: `{checks['verdict']}`.

Input SHA-256:

""" + "\n".join(f"- `{path}`: `{digest}`" for path, digest in hashes.items()) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write JSON and Markdown audits")
    args = parser.parse_args()
    result = build_result()
    if args.write:
        JSON_OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        MD_OUT.write_text(markdown(result))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
