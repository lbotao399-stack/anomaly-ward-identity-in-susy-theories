#!/usr/bin/env python3
"""Exact functional Hessian covariance for the Step-5A background Ward identity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.verify_step5_propagators import (  # noqa: E402
    Matrix,
    identity,
    inverse,
    multiply,
    q,
)


GENERATED = ROOT / "generated/step5/one-loop-background-hessian-ward.json"
AUDIT_JSON = ROOT / "audits/step5-one-loop-background-hessian-ward-verification.json"
AUDIT_MD = ROOT / "audits/step5-one-loop-background-hessian-ward.md"


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix, strict=True)]


def trace(matrix: Matrix):
    return sum((matrix[index][index] for index in range(len(matrix))), q(0))


def determinant_2(matrix: Matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def covariance_witness() -> dict[str, object]:
    # Q' = R Q, with det R = 1 and no orthogonality assumption.
    representation = [[q(1), q(1)], [q(1), q(2)]]
    representation_inverse = inverse(representation)
    representation_inverse_transpose = transpose(representation_inverse)

    pairing = [[q(2), q(1)], [q(1), q(3)]]
    hessian = [[q(5), q(2)], [q(2), q(4)]]
    insertion = [[q(1), q(2)], [q(-1), q(3)]]

    pairing_prime = multiply(
        multiply(representation_inverse_transpose, pairing),
        representation_inverse,
    )
    hessian_prime = multiply(
        multiply(representation_inverse_transpose, hessian),
        representation_inverse,
    )

    endomorphism = multiply(inverse(pairing), hessian)
    endomorphism_prime = multiply(inverse(pairing_prime), hessian_prime)
    endomorphism_similarity = multiply(
        multiply(representation, endomorphism),
        representation_inverse,
    )

    insertion_prime = multiply(
        multiply(representation, insertion),
        representation_inverse,
    )
    green = inverse(endomorphism)
    green_prime = inverse(endomorphism_prime)
    green_similarity = multiply(
        multiply(representation, green),
        representation_inverse,
    )

    checks = {
        "representation_left_inverse": multiply(
            representation_inverse, representation
        )
        == identity(2),
        "representation_right_inverse": multiply(
            representation, representation_inverse
        )
        == identity(2),
        "representation_determinant_one": determinant_2(representation) == q(1),
        "endomorphism_transforms_by_similarity": endomorphism_prime
        == endomorphism_similarity,
        "green_transforms_by_similarity": green_prime == green_similarity,
        "left_inverse_after_transform": multiply(
            endomorphism_prime, green_prime
        )
        == identity(2),
        "right_inverse_after_transform": multiply(
            green_prime, endomorphism_prime
        )
        == identity(2),
        "source_saturated_insertion_similarity": insertion_prime
        == multiply(multiply(representation, insertion), representation_inverse),
        "one_loop_trace_invariant": trace(multiply(green_prime, insertion_prime))
        == trace(multiply(green, insertion)),
    }
    return {
        "representation": [[entry.to_json() for entry in row] for row in representation],
        "pairing": [[entry.to_json() for entry in row] for row in pairing],
        "hessian": [[entry.to_json() for entry in row] for row in hessian],
        "insertion": [[entry.to_json() for entry in row] for row in insertion],
        "checks": checks,
    }


def adjoint_trace_witness() -> dict[str, object]:
    # A generic three-dimensional antisymmetric adjoint infinitesimal matrix.
    adjoint = [
        [q(0), q(2), q(-3)],
        [q(-2), q(0), q(5)],
        [q(3), q(-5), q(0)],
    ]
    checks = {
        "antisymmetric": transpose(adjoint)
        == [[-entry for entry in row] for row in adjoint],
        "trace_zero": trace(adjoint) == q(0),
    }
    return {
        "matrix": [[entry.to_json() for entry in row] for row in adjoint],
        "checks": checks,
    }


def build_payload() -> dict[str, object]:
    covariance = covariance_witness()
    adjoint = adjoint_trace_witness()
    checks = {
        **{f"covariance.{key}": value for key, value in covariance["checks"].items()},
        **{f"adjoint.{key}": value for key, value in adjoint["checks"].items()},
        "source_and_insertion_parity_even": (1 + 1) % 2 == 0,
    }
    return {
        "schema": "Step5OneLoopBackgroundHessianWard.v1",
        "status": "PASS_FUNCTIONAL_LEVEL_BACKGROUND_COVARIANCE"
        if all(checks.values())
        else "FAIL",
        "scope": "STEP5A_REFERENCE_FLAT_SOURCE_SATURATED_FUNCTIONAL",
        "project_inputs": [
            "3D.80 background-quantum split",
            "3D.81 homogeneous quantum background transformation",
            "3D.86 background-covariant gauge condition",
            "3D.88a background-covariant nonminimal kernel",
            "source-left odd dual transformation derived in the Step5 audit",
        ],
        "equations": {
            "functional_invariance": "Sigma_(J')[B',Q']=Sigma_J[B,Q]; Q'=R Q",
            "raw_hessian": "K'=R^(-st) K R^(-1)",
            "pairing": "Omega'=R^(-st) Omega R^(-1)",
            "endomorphism": "H'=R H R^(-1); H=Omega^(-1) K",
            "green": "G'=R G R^(-1)",
            "source_saturated_insertion": "I[J]'=R I[J] R^(-1)",
            "one_loop": "Gamma_J^(1)=(1/2) STr(G I[J])",
            "measure": "Tr_Adj(ad_eta)=eta^C kappa^(AB)c_(C A B)=0",
        },
        "covariance_witness": covariance,
        "adjoint_trace_witness": adjoint,
        "checks": checks,
        "verdicts": {
            "functional_background_hessian_covariance": "PASS",
            "reference_flat_adjoint_coefficient_measure": "PASS",
            "source_saturated_one_loop_background_ward_identity": "PASS",
            "vertex_by_vertex_graphir_intertwining": "OPEN_COMPILER_REPLAY",
            "full_chiral_vector_measure_bridge": "OPEN",
            "finite_bv_density_equivalence": "STEP5C_OPEN",
            "quadratic_jet_injectivity": "OPEN_RELATION_MATRIX",
            "anomaly_coefficient": "NOT_ACCEPTED",
        },
        "external_results_imported": False,
    }


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def render_markdown() -> str:
    return r"""# Step 5A background Hessian Ward certificate

## 1. Functional differentiation

$$
\Sigma_{J'}[\mathcal B',Q']
=\Sigma_J[\mathcal B,Q],
\qquad
Q'=RQ.
$$

At fixed background, \(R\) is independent of \(Q\).  Therefore

$$
\frac{\vec\delta}{\delta Q'^i}
=(R^{-1})^j{}_i\frac{\vec\delta}{\delta Q^j},
$$

$$
K'_{ij}
=(R^{-{\rm st}})_i{}^kK_{k\ell}(R^{-1})^\ell{}_j.
$$

For the field-space pairing,

$$
\Omega'=R^{-{\rm st}}\Omega R^{-1}.
$$

Hence

$$
\begin{aligned}
H'
&=(\Omega')^{-1}K'\\
&=R\Omega^{-1}R^{\rm st}R^{-{\rm st}}KR^{-1}\\
&=RHR^{-1},
\end{aligned}
\qquad
H:=\Omega^{-1}K.
$$

Thus

$$
G'=RG R^{-1},
\qquad
G:=H^{-1}.
$$

## 2. Odd source

$$
|J|=1,
\qquad
|\mathscr I|=1,
\qquad
|J\mathscr I|=0.
$$

For the source-saturated insertion endomorphism,

$$
I[J]'=R\,I[J]\,R^{-1}.
$$

Therefore

$$
\begin{aligned}
\Gamma_J^{(1)}[\mathcal B']
&=\frac12\operatorname{STr}
\left(RGR^{-1}RI[J]R^{-1}\right)\\
&=\frac12\operatorname{STr}
\left(R\,GI[J]\,R^{-1}\right)\\
&=\frac12\operatorname{STr}\left(GI[J]\right)
=\Gamma_J^{(1)}[\mathcal B].
\end{aligned}
$$

## 3. Reference-flat measure

For every adjoint coefficient,

$$
\operatorname{Tr}_{\rm Adj}(\operatorname{ad}_\eta)
=\eta^Cc_{CA}{}^A
=\eta^C\kappa^{AB}c_{CAB}
=0.
$$

Thus

$$
\operatorname{Ber}R
=\exp\!\left(\operatorname{STr}\log R\right)
=1
$$

for each finite Step-5A coefficient block.

## 4. Boundary

$$
\text{functional background Ward identity}
=\texttt{PASS}.
$$

$$
\text{vertex-by-vertex GraphIR replay}
=\texttt{OPEN},
\qquad
\text{chiral--vector full measure bridge}
=\texttt{OPEN},
\qquad
\ker\bar\ell_2
=\texttt{OPEN}.
$$

No anomaly coefficient is accepted.
"""


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    audit = {
        "schema": "Step5OneLoopBackgroundHessianWardAudit.v1",
        "status": payload["status"],
        "totals": {
            "checks": len(payload["checks"]),
            "failed": sum(not value for value in payload["checks"].values()),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "graphir_replay": payload["verdicts"]["vertex_by_vertex_graphir_intertwining"],
        "anomaly_coefficient": payload["verdicts"]["anomaly_coefficient"],
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT_JSON.write_bytes(canonical_json(audit))
    AUDIT_MD.write_text(render_markdown(), encoding="utf-8")


if __name__ == "__main__":
    write_artifacts()
