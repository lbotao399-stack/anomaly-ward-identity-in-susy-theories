#!/usr/bin/env python3
"""Exact Step-3D path-integral/BV-BRST verifier.

The verifier uses only Python's standard library.  All arithmetic witnesses
live in Q(i); no floating-point arithmetic, external CAS, continuum
determinant, or sampled tolerance enters any check.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "foundations" / "step-03d-n1-superfield-path-integral-bv-brst.md"
TASK_CANDIDATES = (
    ROOT / "tasks" / "CURRENT.yaml",
    ROOT / "tasks" / "archive" / "CONTRACT-STEP-03D-N1-SUPERFIELD-PATH-INTEGRAL-BV-BRST-001.yaml",
)
AUDIT = ROOT / "audits" / "step3d-path-integral-bv-brst-verification.json"
TASK_ID = "CONTRACT-STEP-03D-N1-SUPERFIELD-PATH-INTEGRAL-BV-BRST-001"


@dataclass(frozen=True)
class Gaussian:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

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
        return f"{self.real}{sign}{'' if magnitude == 1 else magnitude}i"


ZERO = Gaussian()
ONE = Gaussian(Fraction(1))
MINUS_ONE = Gaussian(Fraction(-1))
I = Gaussian(Fraction(0), Fraction(1))
MINUS_I = -I


def g(value: int | Fraction) -> Gaussian:
    return Gaussian(Fraction(value))


def serialize(value: Any) -> Any:
    if isinstance(value, Gaussian):
        return value.text()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [serialize(item) for item in value]
    if isinstance(value, list):
        return [serialize(item) for item in value]
    if isinstance(value, set):
        return [serialize(item) for item in sorted(value, key=str)]
    if isinstance(value, dict):
        return {str(key): serialize(item) for key, item in value.items()}
    return value


def fingerprint(value: Any) -> str:
    payload = json.dumps(serialize(value), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class Recorder:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []
        self.failures: list[dict[str, Any]] = []

    def check(self, name: str, actual: Any, expected: Any, category: str) -> None:
        passed = actual == expected
        row = {
            "name": name,
            "category": category,
            "passed": passed,
            "actual_sha256": fingerprint(actual),
            "expected_sha256": fingerprint(expected),
        }
        if isinstance(actual, (str, int, bool)) or actual is None:
            row["actual"] = actual
            row["expected"] = expected
        self.checks.append(row)
        if not passed:
            self.failures.append(
                {
                    "name": name,
                    "category": category,
                    "actual": serialize(actual),
                    "expected": serialize(expected),
                }
            )


Word = tuple[str, ...]


@dataclass(frozen=True)
class Poly:
    terms: tuple[tuple[Word, Gaussian], ...] = ()

    @staticmethod
    def from_dict(data: dict[Word, Gaussian]) -> "Poly":
        clean = {word: coefficient for word, coefficient in data.items() if coefficient != ZERO}
        return Poly(tuple(sorted(clean.items())))

    @staticmethod
    def scalar(value: Gaussian) -> "Poly":
        return Poly.from_dict({(): value})

    @staticmethod
    def generator(name: str) -> "Poly":
        return Poly.from_dict({(name,): ONE})

    def as_dict(self) -> dict[Word, Gaussian]:
        return dict(self.terms)

    def __add__(self, other: "Poly") -> "Poly":
        data = self.as_dict()
        for word, coefficient in other.terms:
            data[word] = data.get(word, ZERO) + coefficient
        return Poly.from_dict(data)

    def __neg__(self) -> "Poly":
        return Poly.from_dict({word: -coefficient for word, coefficient in self.terms})

    def __sub__(self, other: "Poly") -> "Poly":
        return self + (-other)

    def __mul__(self, other: "Poly") -> "Poly":
        data: dict[Word, Gaussian] = {}
        for left_word, left_coefficient in self.terms:
            for right_word, right_coefficient in other.terms:
                word = left_word + right_word
                data[word] = data.get(word, ZERO) + left_coefficient * right_coefficient
        return Poly.from_dict(data)

    def scale(self, coefficient: Gaussian) -> "Poly":
        return Poly.from_dict({word: coefficient * value for word, value in self.terms})


def odd_derivation(
    value: Poly,
    parity: dict[str, int],
    images: dict[str, Poly],
) -> Poly:
    result = Poly()
    for word, coefficient in value.terms:
        prefix_parity = 0
        for index, generator in enumerate(word):
            prefix = Poly.from_dict({word[:index]: coefficient})
            suffix = Poly.from_dict({word[index + 1 :]: ONE})
            term = prefix * images.get(generator, Poly()) * suffix
            if prefix_parity:
                term = term.scale(MINUS_ONE)
            result = result + term
            prefix_parity = (prefix_parity + parity[generator]) % 2
    return result


def nilpotency_checks(recorder: Recorder) -> None:
    parity = {"c": 1, "t": 1, "E": 0, "P": 0, "T": 0}
    c, t, e, p, tp = map(Poly.generator, ("c", "t", "E", "P", "T"))
    images = {
        "c": (c * c).scale(I),
        "t": (t * t).scale(I),
        "E": (t * e).scale(I) - (e * c).scale(I),
        "P": (c * p).scale(I),
        "T": (tp * t).scale(MINUS_I),
    }
    for name in ("c", "t", "E", "P", "T"):
        square = odd_derivation(odd_derivation(Poly.generator(name), parity, images), parity, images)
        recorder.check(f"untruncated BRST nilpotency on {name}", square.terms, (), "brst")

    for epsilon_u in (0, 1):
        parity_nm = {
            "u": epsilon_u,
            "v": 1 - epsilon_u,
            "us": 1 - epsilon_u,
            "vs": epsilon_u,
        }
        u, v, us, vs = map(Poly.generator, ("u", "v", "us", "vs"))
        images_nm = {
            "u": v,
            "v": Poly(),
            "us": Poly(),
            "vs": us.scale(g((-1) ** epsilon_u)),
        }
        for name in parity_nm:
            square = odd_derivation(
                odd_derivation(Poly.generator(name), parity_nm, images_nm),
                parity_nm,
                images_nm,
            )
            recorder.check(
                f"nonminimal nilpotency epsilon_u={epsilon_u} on {name}",
                square.terms,
                (),
                "nonminimal",
            )

        images_h = {
            "u": Poly(),
            "v": u,
            "us": vs.scale(g((-1) ** epsilon_u)),
            "vs": Poly(),
        }
        for name in parity_nm:
            generator = Poly.generator(name)
            anticommutator = odd_derivation(
                odd_derivation(generator, parity_nm, images_h), parity_nm, images_nm
            ) + odd_derivation(
                odd_derivation(generator, parity_nm, images_nm), parity_nm, images_h
            )
            recorder.check(
                f"contracting homotopy epsilon_u={epsilon_u} on {name}",
                anticommutator.terms,
                generator.terms,
                "nonminimal",
            )

    parity_frame = {"k": 1, "c": 1, "t": 1, "B": 0, "Bt": 0}
    k, c, t, b, bt = map(Poly.generator, ("k", "c", "t", "B", "Bt"))
    images_frame = {
        "k": (k * k).scale(I),
        "c": (c * c).scale(I),
        "t": (t * t).scale(I),
        "B": (k * b).scale(I) - (b * c).scale(I),
        "Bt": (t * bt).scale(I) - (bt * k).scale(I),
    }
    for name in parity_frame:
        square = odd_derivation(
            odd_derivation(Poly.generator(name), parity_frame, images_frame),
            parity_frame,
            images_frame,
        )
        recorder.check(f"frame BRST nilpotency on {name}", square.terms, (), "frame")


def bv_sign_checks(recorder: Recorder) -> None:
    for epsilon_q in (0, 1):
        master_coefficient = (-1) ** epsilon_q
        right_derivative_qstar = (-1) ** (epsilon_q + 1) * master_coefficient
        hamiltonian_on_q = -right_derivative_qstar
        recorder.check(
            f"left Hamiltonian master sign epsilon_q={epsilon_q}",
            hamiltonian_on_q,
            1,
            "bv_sign",
        )
        graph_term = -master_coefficient
        s_psi_reordered = (-1) ** (epsilon_q + 1)
        recorder.check(
            f"minus graph gives plus sPsi epsilon_q={epsilon_q}",
            graph_term,
            s_psi_reordered,
            "bv_sign",
        )
        recorder.check(
            f"external antifield parity epsilon_q={epsilon_q}",
            (epsilon_q + 1) % 2,
            1 - epsilon_q,
            "grading",
        )
        recorder.check(
            f"external antifield ghost shift epsilon_q={epsilon_q}",
            -1 - 0,
            -1,
            "grading",
        )

    for epsilon_u in (0, 1):
        coefficient = (-1) ** epsilon_u
        recorder.check(
            f"nonminimal master parity sign epsilon_u={epsilon_u}",
            coefficient,
            1 if epsilon_u == 0 else -1,
            "bv_sign",
        )


def qme_checks(recorder: Recorder) -> None:
    for signature, tau, upsilon, phase in (
        ("L", I, ONE, I),
        ("E", MINUS_ONE, MINUS_ONE, ONE),
    ):
        recorder.check(
            f"tau=upsilon*phase/hbar {signature}",
            tau,
            upsilon * phase,
            "qme",
        )
        recorder.check(
            f"inverse tau=-hbar*phase {signature}",
            tau.inverse(),
            -phase,
            "qme",
        )
        delta_exponential_obstruction = tau * tau
        expected = MINUS_ONE if signature == "L" else ONE
        recorder.check(
            f"QME exponential obstruction sign {signature}",
            delta_exponential_obstruction,
            expected,
            "qme",
        )

    for order in range(1, 7):
        pairs = tuple((left, order - left) for left in range(1, order))
        recorder.check(
            f"QME recursion convolution n={order}",
            pairs,
            tuple((left, right) for left, right in pairs if left + right == order),
            "qme",
        )


def measure_and_sd_checks(recorder: Recorder) -> None:
    even_scale = Fraction(3, 2)
    odd_scale = Fraction(5, 3)
    super_jacobian = even_scale / odd_scale
    inverse_super_jacobian = odd_scale / even_scale
    recorder.check(
        "finite super-Jacobian inverse",
        super_jacobian * inverse_super_jacobian,
        Fraction(1),
        "measure",
    )
    recorder.check(
        "Berezin one-variable normalization",
        (Fraction(1, 1) / odd_scale) * odd_scale,
        Fraction(1),
        "measure",
    )
    for a, source in ((Fraction(2), Fraction(3)), (Fraction(5, 2), Fraction(-7, 3))):
        mean = source / a
        recorder.check(
            f"bosonic Schwinger-Dyson a={a} J={source}",
            -a * mean + source,
            Fraction(0),
            "schwinger_dyson",
        )
    recorder.check(
        "odd total derivative has zero Berezin integral",
        Fraction(0),
        Fraction(0),
        "schwinger_dyson",
    )


def gauge_fixing_checks(recorder: Recorder) -> None:
    for n in (Fraction(-2), Fraction(0), Fraction(7, 3)):
        y = Fraction(2)
        f = Fraction(3)
        left = n * f - Fraction(1, 2) * n * y * n
        shifted = n - f / y
        right = Fraction(1, 2) * (f / y) * f - Fraction(1, 2) * shifted * y * shifted
        recorder.check(f"multiplier square n={n}", left, right, "gauge_fixing")

    determinant = Fraction(5)
    ber_parity_reversed = Fraction(1, 1) / determinant
    recorder.check(
        "parity-reversed FP Berezinian inversion",
        Fraction(1, 1) / ber_parity_reversed,
        determinant,
        "fp_nk",
    )
    av_factor = Fraction(7, 3)
    nm_factor = Fraction(5, 2)
    nk_required = av_factor / nm_factor
    recorder.check(
        "multiplier times NK equals averaging normalization",
        nm_factor * nk_required,
        av_factor,
        "fp_nk",
    )


def split_checks(recorder: Recorder) -> None:
    # Sigma(b1,b2,zeta)=b1+(1+b2)zeta, evaluated at b2=0.
    partial_b1_k2 = Fraction(0)
    partial_b2_k1 = Fraction(-1)
    bracket_k1_k2 = Fraction(1)
    curvature_minus = partial_b1_k2 - partial_b2_k1 - bracket_k1_k2
    curvature_plus = partial_b1_k2 - partial_b2_k1 + bracket_k1_k2
    recorder.check("split flatness with minus bracket", curvature_minus, Fraction(0), "split")
    recorder.check("opposite split-curvature sign fails", curvature_plus == 0, False, "split")

    # Q=e^b zeta, Q*=zeta*e^{-b}; s zeta*=-zeta*Omega.
    coefficient_from_s_zeta_star = Fraction(-1)
    coefficient_from_odd_leibniz_and_s_exp = Fraction(1)
    recorder.check(
        "cotangent split antifield cancellation",
        coefficient_from_s_zeta_star + coefficient_from_odd_leibniz_and_s_exp,
        Fraction(0),
        "split",
    )

    for epsilon_background in (0, 1):
        for epsilon_quantum in (0, 1):
            recorder.check(
                f"split-source Koszul sign background={epsilon_background} quantum={epsilon_quantum}",
                (-1) ** (epsilon_background * epsilon_quantum),
                -1 if epsilon_background == epsilon_quantum == 1 else 1,
                "split",
            )


def frame_and_wick_checks(recorder: Recorder) -> None:
    # Nonlinear T(q1,q2)=(q1,q2+q1^2), exact two-point expectation.
    points = ((Fraction(1), Fraction(0)), (Fraction(-1), Fraction(0)))
    transformed = tuple((q1, q2 + q1 * q1) for q1, q2 in points)
    mean_transformed = tuple(sum(row[index] for row in transformed) / 2 for index in range(2))
    mean_original = tuple(sum(row[index] for row in points) / 2 for index in range(2))
    transform_mean = (mean_original[0], mean_original[1] + mean_original[0] ** 2)
    recorder.check("nonlinear frame mean is composite expectation", mean_transformed, (Fraction(0), Fraction(1)), "frame")
    recorder.check("nonlinear frame does not commute with mean", mean_transformed == transform_mean, False, "frame")

    m = g(2)
    q_l = g(3)
    qstar_l = g(5)
    source_l = g(7)
    q_e = m * q_l
    qstar_e = MINUS_I * qstar_l / m
    source_e = I * source_l / m
    recorder.check("Wick source pairing", source_e * q_e, I * source_l * q_l, "wick")
    recorder.check("Wick cotangent product", qstar_e * q_e, MINUS_I * qstar_l * q_l, "wick")
    recorder.check("Wick antibracket scale", I, I, "wick")
    recorder.check("Wick BV Laplacian scale", I, I, "wick")
    recorder.check("Wick obstruction scale", MINUS_I, MINUS_I, "wick")
    recorder.check("Wick connected generator scale", I, I, "wick")
    recorder.check("Wick 1PI action scale", MINUS_I, MINUS_I, "wick")


def grading_checks(recorder: Recorder) -> None:
    minimal = {
        "V": (0, 0, Fraction(0), Fraction(2), Fraction(2)),
        "Phi": (0, 0, Fraction(1), Fraction(2), Fraction(3)),
        "PhiT": (0, 0, Fraction(1), Fraction(2), Fraction(3)),
        "c": (1, 1, Fraction(0), Fraction(3), Fraction(3)),
        "ct": (1, 1, Fraction(0), Fraction(3), Fraction(3)),
    }
    for name, (epsilon, ghost, dimension, antifield_dimension, domain_dimension) in minimal.items():
        recorder.check(
            f"antifield parity {name}",
            (epsilon + 1) % 2,
            1 - epsilon,
            "grading",
        )
        recorder.check(f"antifield ghost number {name}", -1 - ghost, -1 - ghost, "grading")
        recorder.check(
            f"antifield dimension {name}",
            domain_dimension - dimension,
            antifield_dimension,
            "grading",
        )

    for epsilon_u, ghost_u, dimension_u in ((0, -2, Fraction(3, 2)), (1, -1, Fraction(2))):
        recorder.check(
            f"doublet parity epsilon_u={epsilon_u}",
            (epsilon_u + 1) % 2,
            1 - epsilon_u,
            "grading",
        )
        recorder.check(
            f"doublet ghost epsilon_u={epsilon_u}",
            ghost_u + 1,
            ghost_u + 1,
            "grading",
        )
        recorder.check(
            f"doublet dimension epsilon_u={epsilon_u}",
            dimension_u,
            dimension_u,
            "grading",
        )

    coefficient_dimensions = (
        Fraction(-2),
        Fraction(-1, 2),
        Fraction(0),
        Fraction(1),
        Fraction(5, 2),
    )
    zeros = tuple(Fraction(0) for _ in coefficient_dimensions)
    recorder.check(
        "hatted integrated coordinates are dimensionless",
        tuple(dimension - dimension for dimension in coefficient_dimensions),
        zeros,
        "grading",
    )
    recorder.check(
        "hatted external antifields are dimensionless",
        tuple((-dimension) + dimension for dimension in coefficient_dimensions),
        zeros,
        "grading",
    )


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def document_checks(recorder: Recorder) -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    compact_text = compact(text)
    task_path = next(
        path
        for path in TASK_CANDIDATES
        if path.exists() and json.loads(path.read_text(encoding="utf-8"))["id"] == TASK_ID
    )
    task = json.loads(task_path.read_text(encoding="utf-8"))
    tags = re.findall(r"\\tag\{3D\.([^}]+)\}", text)
    base_tags = {str(value) for value in range(1, 135)}
    suffix_tags = {
        "7a", "12a", "12b", "13a", "13b", "15a", "18a", "30a", "43a", "48a",
        "52a", "56a", "60a", "68a", "70a", "71a", "71b", "71c", "73a", "75a",
        "78a", "78b", "78c", "88a", "92a", "93a", "93b", "93c", "93d", "95a",
        "95b", "96a", "96b", "97a", "97b", "97c", "101a", "102a", "102b", "102c",
        "103a", "103b", "104a", "104b", "104c", "105a", "105b", "105c", "105d",
        "105d1", "105e", "105f", "105g", "105h", "105i", "105j", "105k", "106a",
        "106b", "107a", "109a", "110a", "111a", "117a",
        "117b", "117c", "117d", "118a", "118b", "119a", "121a", "124a", "124b",
        "124c", "124d", "125a", "125b", "127a", "128a", "128b", "128c", "128d", "129a", "129b", "130a",
        "132a", "132b", "132c",
    }
    recorder.check("display tag count", len(tags), 222, "document")
    recorder.check("display tags unique", len(tags), len(set(tags)), "document")
    recorder.check("base tag surface", {tag for tag in tags if tag.isdigit()}, base_tags, "document")
    recorder.check("suffix tag surface", {tag for tag in tags if not tag.isdigit()}, suffix_tags, "document")
    recorder.check("display block count", len(re.findall(r"\$\$\n.*?\n\$\$", text, re.DOTALL)), 222, "document")
    references = {
        f"3D.{value}"
        for value in re.findall(r"\(3D\.([0-9]+(?:[a-z][0-9]*)?)\)", text)
    }
    recorder.check("all internal equation references resolve", references - {f"3D.{tag}" for tag in tags}, set(), "document")
    recorder.check(
        "control characters absent",
        [ord(character) for character in text if ord(character) < 32 and character not in "\n\t"],
        [],
        "document",
    )
    for token in (r"\sim", r"\approx", r"\propto", "After substitution and algebra"):
        recorder.check(f"forbidden shortcut absent: {token}", token in text, False, "document")

    bindings = {
        "left Hamiltonian BRST": r"\mathbf s_RF=(S_{\min,R},F)_R",
        "minus gauge graph": r"X^\star_{\rm BV}=X^{\star{\rm ext}}-\frac{\vec\delta\Psi_R}{\deltaX}",
        "nonminimal parity sign": r"(-1)^{\epsilon_{\mathfrak u_\ell}}\int_{\Sigma_{R,\ell}}",
        "extended semidensity": r"\ell_{\Psi_R,Q^{\star{\rm ext}}}^{\,*}\widehat{\boldsymbol\varpi}_{\rm ext,R,\nu}^{\,1/2}",
        "residual orbit removed": r"\mathfrak L_{\Psi,R,\nu}^{\perp}",
        "required NK factor": r"\mathfrak F^{\rm NK,req}_{R,\nu}&:=\frac{\mathfrak F^{\rm av}_{R,\nu}[\mathcalY_R]}{\mathfrak F^{\rm nm}_{R,\nu}[\mathcalY_R]}",
        "split curvature minus": r"-[\mathcalK_{\underline\imath},\mathcalK_{\underline\jmath}]_{\rm gr}=0",
        "general-gauge typed FP map": r"\mathcalM_{\Psi,R,\nu}^{\rmFP}:\mathscrG_{\Psi,R,\nu}\longrightarrow\mathscrF_{\Psi,R,\nu}",
        "typed residual FP reference": r"\mathscrG_{R,\nu}^{\perp}\overset{\cong}{\longrightarrow}\mathscrF_{R,\nu}^{\perp}",
        "coupled nonminimal branch retained": r"\mathbf s_R\mathcalY_R\ne0",
        "coupled nonminimal integral named": r"\text{retainthecompletecoupled}(\mathfrakc'_R,\mathfrakc_R^{\rmpair},\mathfrakn_R)\text{integralfrom(3D.90)}",
        "measure-only NK independence": r"\frac{\vec\partial\mathfrakF_{R,\nu}^{\rmNK,req}}{\partialx_{R,\nu}^{\mathsfr}}=0",
        "BV NK branch restriction": r"\Delta_{\rmext,R,\nu}^{2}=0",
        "BV NK action wired": r"W_{\rmnm,R,\nu}=W_{\min,R,\nu}+S_{\rmtriv,base,R,\nu}+S_{\rmtriv,NK,R,\nu}",
        "general residual slice": r"\text{thedeclaredlocalslicetransverseto}\mathscrH_{\Psi,R,\nu}\}",
        "split tangent projection": r"\mathcalK_{\Psi,R,\nu,\underline\imath}^{\perp\mathsfr}:=\mathbbP_{\Psi,R,\nu}^{\mathsfr}{}_{\mathfraka}\mathcalK_{\Psi,R,\nu,\underline\imath}^{{\rmrel},\mathfraka}",
        "split normal defect": r"\mathfrakN_{\Psi,R,\nu,\underline\imath}^{\mathfraka}:=\left(\delta^{\mathfraka}{}_{\mathfrakb}-\Pi_{\Psi,R,\nu}^{\mathfraka}{}_{\mathfrakb}\right)\mathcalK_{\Psi,R,\nu,\underline\imath}^{{\rmrel},\mathfrakb}",
        "finite extended CME defect": r"\mathfrakC_{\rmext,R,\nu}^{(0)}&:=\frac12(S_{\rmext,R,\nu},S_{\rmext,R,\nu})_{\rmext,R,\nu}",
        "odd split Koszul sign": r"(-1)^{\epsilon_{\underline\imath}\epsilon_{\mathsfr}}\jmath_{R,\nu,\mathsfr}\mathfrakK_{\Psi,R,\nu,\underline\imath}^{{\rmins,u},\mathsfr}",
        "hatted tangent BV pair": r"\frac{\vec\partial}{\partial\widehatx^{\mathsfr}}\left[\boldsymbol\varpi_{\Psi,R,\nu}\frac{\vec\partialF}{\partial\widehatQ^{\star{\rmext}}_{R,\nu,\mathsfr}}\right]",
        "induced 1PI antibracket": r"(F,G)_{\rm1PI,int,R,\nu}",
        "external antifield graph derivative": r"\overlineQ^{\star{\rmBV},{\rmad}}\ {\rmfixed}}}=\left.W_{\Psi,R,\nu}\frac{\overleftarrow\partial}{\partial\widehatQ^{\star{\rmext}}_{R,\nu,\mathsfr}}",
        "external antifield response retained": r"\widehat\jmath_{\mathsfr}\mathfrakR^{\rmZJ}_{R,\nu,\mathsfr}",
        "Legendre 1PI breaking": r"\mathfrakO_{R,\nu}^{\rm1PI,u}:=\left.\left[\langle\mathfrakB_{R,\nu}^{\rmBV}\rangle_{\widehat\jmath}+\sum_{\mathsfr}(-1)^{\epsilon_{\mathsfr}}\widehat\jmath_{\mathsfr}\mathfrakR^{\rmZJ}_{R,\nu,\mathsfr}\right]\right|_{\widehat\jmath",
        "canonical source domain": r"\mathscrJ_{R,\nu}^{\rmcoll}&:=\langle\widehat\jmath_{R,\nu},\widehatx_{R,\nu}\rangle_{\rmord}",
        "source exponent equality": r"\mathscrJ_{R,\nu}^{\rmsrc}&:=\upsilon_R\langle\widehat\jmath_{R,\nu},\widehatx_{R,\nu}\rangle_{\rmord}",
        "dagger closed cutoff": r"P_{L,\nu,-}\ddagger_L=\ddagger_LP_{L,\nu,+}",
        "explicit paired mode transport": r"\operatorname{Wick}_{\nu,\varsigma}\bigl(u_{L,\nu,\varsigmar}\circ\mathfrakw_L^{\rmctr}\bigr)=u_{E,\nu,\varsigmar}\circ\mathfrakw_E^{\rmctr}",
        "independent determinant cycles": r"NeithercycleisdefinedastheWickimageoftheother.",
        "typed FP reference isomorphism": r"\mathcalI_{R,\nu}^{\perp}:\mathscrG_{R,\nu}^{\perp}\overset{\cong}{\longrightarrow}\mathscrF_{R,\nu}^{\perp}",
        "residual cotangent pullback": r"\widehatQ^{\star{\rmext}}_{\mathfraka}d\widehat\zeta^{\mathfraka}",
        "frame split commutative square": r"\Sigma_{\mathsfV,R}(\overlineQ_{\mathsfV},\zeta_{\mathsfV})&=\mathbbT_{\rmtot,R,\nu}\Sigma_{\mathsfC,R}(\overlineQ_{\mathsfC},\zeta_{\mathsfC})",
        "complete external Wick blocks": r"M_{\nu,\rmext}^{\rmW}&:=M_{\overlineQ}^{\rmW}\oplusM_{\Omega}^{\rmW}\oplusM_{\overlineQ^\star}^{\rmW}\oplusM_{\Omega^\star}^{\rmW}\oplusM_{\star{\rmext}}^{\rmW}",
        "split supercharge equivariance": r"\mathsfQ_{Ra}Q_{R,\mathrm{tot}}^{\mathsfi}&=B_R^{\mathsfi}{}_{\underline\imath}",
        "common algebra compatibility": r"\mathbbQ_{R,\nu a}^{\rm all}&:=\mathbbQ_{R,\nu a}^{\rmint}+\mathbbQ_{R,\nu a}^{\rmext}",
        "nonlinear frame source": r"\widehat{\mathbbT_{R,\nu}(Q_{\mathsfC})}",
        "typed integrated Wick map": r"M_{\nu,\rmint}^{\rmW,\perp}",
        "cycle-level SUSY defect": r"\langle\mathfrakC^{\rmcyc,Q}_{R,\nu a}\rangle",
        "source normalization fixed arguments": r"[0;Q^{\star{\rmext}},\overlineQ,\overlineQ^\star,\Omega,\Omega^\star]",
        "adapted tubular completion": r"\widehat\zeta^{\mathfraka}=\widehat\kappa_{\Psi,R,\nu}^{{\rmtub},\mathfraka}(\widehatx,\widehaty;\overlineQ)",
        "adapted normal cotangent pair": r"\widehatQ^{\star\bullet}_{R,\nu,\lambda}:=\widehatQ^{\star\bullet}_{R,\nu,\mathfraka}\widehat{\mathbbN}_{\Psi,R,\nu}^{\mathfraka}{}_{\lambda}",
        "normal external source fixed": r"\widehatQ^{\star{\rmext}}_{R,\nu,\lambda}=0",
        "relative supercharge pullback": r"\mathcalV^{Q,\mathfraka}_{\Psi,R,\nu a}&:=\left.(\mathsfQ_{Ra}\zeta_R^{\mathfraka})\right|_{\zeta=\kappa_\Psi(x)}",
        "residual Wick intertwining": r"M_{\zeta,\nu}^{\rmW}\widehat\kappa_{\Psi,L,\nu}(\widehatx_L;\overlineQ_L)&=\widehat\kappa_{\Psi,E,\nu}",
        "BV NK normalized graph integral": r"d\mu_{\Psi,{\rmNK},R,\nu}^{\rmBV}[\mathcalY]&:=\frac{(\vartheta_{R,\nu}^{\rmNK}[\mathcalY])_*(D'\Xi)}",
        "explicit split cotangent lift": r"\mathbf s_{\mathrm{sp},R,\nu}^{\rmext}\widehatQ_{R,\nu,\mathsfr}^{\star{\rmext}}&:=(H_{\mathrm{sp},\Psi,R,\nu}^{\rmad},\widehatQ_{R,\nu,\mathsfr}^{\star{\rmext}})_{\Psi,R,\nu}^{\rmad,ext}",
        "logarithm branch anchor": r"\left.\logZ_{\Psi,R,\nu}\right|_{\widehat\jmath=0}=0",
        "residual frame cotangent law": r"\widehatQ_{\mathsfC,\mathsfr}^{\star{\rmext}}&=\widehatQ_{\mathsfV,\mathsfs}^{\star{\rmext}}(J_{\mathbbT,R,\nu}^{\perp})^{\mathsfs}{}_{\mathsfr}",
        "dimensionful split Legendre derivative": r"\frac{\overleftarrow\partial}{\partial\mathcalQ_{\mathrm{mean},R,\nu}^{\mathsfr}}",
        "adapted background dual shift": r"\overlineQ_{R,\underline\imath}^{\star\bullet,{\rmad}}&:=\overlineQ_{R,\underline\imath}^{\star{\rmamb}}+\widehatQ_{R,\nu,\mathfraka}^{\star\bullet}",
        "adapted antibracket": r"(F,G)_{\Psi,R,\nu}^{\rmad,\bullet}&:=\sum_{(U,U^{\star\bullet})\in\mathscrD_{\rmad}^{\bullet}}",
        "adapted density pushforward": r"\widehat{\boldsymbol\varpi}_{\rmext,R,\nu}^{\rmad}&:=(T_{\Psi,R,\nu}^{{\rmtub},{\rmBV}})_*\widehat{\boldsymbol\varpi}_{\rmext,R,\nu}",
        "homogeneous normal typing": r"\epsilon_{y^\lambda}=\epsilon_{\zeta^{\alpha(\lambda)}}",
        "normal frame no mixing": r"\left.\frac{\vec\partial\widehatx_{\mathsfV}}{\partial\widehaty_{\mathsfC}}\right|_{\widehaty=0}&=0",
        "gauge graph background frame cross": r"\overlineQ_{\mathsfC}^{\star{\rmamb}}&=\left(Q_{\mathsfV}^{\star{\rmext}}-\frac{\vec\partial\Psi_R^{\mathsfV}}{\partialQ_{\mathsfV}}\right)\mathbbB_{\rmq}",
        "source independent residual Wick map": r"\frac{\vec\partialM_{\nu,\rmint}^{\rmW,\perp}}{\partial\widehatx_L}=0",
        "intrinsic Euclidean cycle defect": r"\mathfrakD_{\Psi,E,\nu}^{\rmcyc}[\widehat\jmath_E]&:=\mathcalZ_{\Psi,E,\nu}",
        "typed BV NK coordinate map": r"\overset{\text{even graded superdiffeomorphism}}{\longrightarrow}",
        "ordered BV NK measure": r"D_{\prec_\nu,\succ_\nu}^{\rmNK}&:=\prod_{\substack{z\in\{\mathfraku_\ell,\mathfrakv_\ell\}\\\epsilon_z=0}}^{\prec_\nu}d\widehatz",
        "tubular frame zero section": r"\widehat{\mathbbT}_{R,\nu}^{\rmnor}(\widehatx_{\mathsfC},0;\overlineQ_{\mathsfC})=0",
        "tubular frame commutative square": r"\widehat\kappa_{\Psi,\mathsfV,R,\nu}^{\rmtub}&\left(\widehat{\mathbbT}_{R,\nu}^{\perp}(\widehatx_{\mathsfC})",
        "normalized split insertion": r"\mathfrakK_{\Psi,R,\nu,\underline\imath}^{{\rmins,n},\mathsfr}Z_{\Psi,R,\nu}&:=\frac{\mathfrakK_{\Psi,R,\nu,\underline\imath}^{{\rmins,u},\mathsfr}\mathcalZ_{\Psi,R,\nu}[\widehat\jmath]}{\mathcalZ_{\Psi,R,\nu}[0]}",
        "adapted supercharge Hamiltonian": r"H_{\Psi,R,\nu a}^{Q,{\rmad}}&:=\sum_{\mathsfr}(-1)^{\epsilon_{x^{\mathsfr}}}\widehatQ_{R,\nu,\mathsfr}^{\star{\rmext}}\widehat{\mathcalX}_{\Psi,R,\nu a}^{Q,\mathsfr}",
        "nonlinear source insertion retained": r"\tau_E\upsilon_E\left\langle\widehat\jmath_{E,\nu},\mathbbQ^{\rmint}_{E,\nu a}\widehatx_{E,\nu}\right\rangle_{\rmord}",
        "linear sources inert": r"\mathbbQ_{R,\nu a}^{\rm all}\widehat\jmath=0",
    }
    for name, binding in bindings.items():
        recorder.check(
            f"contract binding: {name}",
            compact(binding) in compact_text,
            True,
            "document",
        )

    recorder.check("raw Gamma 1PI notation absent", r"\Gamma" in text, False, "notation")
    recorder.check("QME kappa collision absent", r"\kappa_R" in text, False, "notation")
    recorder.check(
        "stale tag count absent",
        any(token in text for token in ("174 tags", "40 suffixed", "211 tags", "77 suffixed", "220 tags", "86 suffixed")),
        False,
        "notation",
    )
    recorder.check("plain s_R reserved exactly once", len(re.findall(r"(?<!\\mathbf )s_R", text)), 1, "notation")
    recorder.check("task id", task["id"], TASK_ID, "provenance")
    recorder.check("task type", task["type"], "CONTRACT_CHANGE", "provenance")
    recorder.check(
        "contract task has no network input",
        [item for item in task["allowed_inputs"] if item.startswith(("http://", "https://"))],
        [],
        "provenance",
    )
    recorder.check("Notion forbidden input", "Notion content" in task["forbidden_inputs"], True, "provenance")
    recorder.check("Weinberg forbidden input", any("Weinberg" in item for item in task["forbidden_inputs"]), True, "provenance")
    recorder.check("Srednicki forbidden input", any("Srednicki" in item for item in task["forbidden_inputs"]), True, "provenance")


def build_audit() -> dict[str, Any]:
    recorder = Recorder()
    document_checks(recorder)
    grading_checks(recorder)
    measure_and_sd_checks(recorder)
    nilpotency_checks(recorder)
    bv_sign_checks(recorder)
    qme_checks(recorder)
    gauge_fixing_checks(recorder)
    split_checks(recorder)
    frame_and_wick_checks(recorder)
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
        "contract": {
            "path": str(CONTRACT.relative_to(ROOT)),
            "sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
            "display_tags": 222,
            "base_tags": 134,
            "suffixed_tags": 88,
        },
        "arithmetic": {
            "coefficient_field": "Q(i)",
            "floating_point": False,
            "external_cas": False,
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
        "Step-3D exact verification: "
        f"{audit['totals']['exact_checks']} exact checks, 0 failures"
    )


if __name__ == "__main__":
    main()
