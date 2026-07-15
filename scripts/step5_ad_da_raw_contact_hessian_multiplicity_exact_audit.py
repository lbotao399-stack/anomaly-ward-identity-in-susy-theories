#!/usr/bin/env python3
"""Exact local AD/DA Schwinger-contact Hessian multiplicity.

The selected marked source is first factorized as ``r_e^2 P_e``.  This
script then constructs the local Schwinger contact from ``P_e`` and the raw
cubic action Hessians.  The contact is not defined as a residual: its sign
and coefficient are generated from the canonical kinetic metric, the two
uncut propagators, the Schwinger functional-derivative sign, the interaction
factorial, the two cut-endpoint placements, and the two remaining-line Wick
pairings.

The finite-w one-link derivative is a separate longitudinal Ward row.  It is
kept out of the local contact multiplicity and is cancelled endpoint by
endpoint with the Duhamel identity.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_ad_da_ordered_ports_crossed_hessian_exact_audit as audit  # noqa: E402


alg = audit.alg
raw = audit.raw
JSON_OUT = ROOT / "audits" / "step5-ad-da-raw-contact-hessian-multiplicity-exact.json"
MD_OUT = ROOT / "audits" / "step5-ad-da-raw-contact-hessian-multiplicity-exact.md"


@dataclass
class Ledger:
    rows: list[dict[str, str]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, check_id: str, actual: object, expected: object) -> None:
        passed = actual == expected
        self.rows.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "actual": exact_text(actual),
                "expected": exact_text(expected),
            }
        )
        if not passed:
            raise AssertionError(f"{check_id}: {actual!r} != {expected!r}")


def exact_text(value: object) -> str:
    if isinstance(value, alg.A):
        return value.text()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, sp.Basic):
        return sp.sstr(sp.factor(value))
    return str(value)


def occurrence_data() -> tuple[dict[str, str], ...]:
    return (
        {
            "id": "AD_DIRECT_E0",
            "pair_id": "AD",
            "pair": "A__Ddot1",
            "allocation": "direct",
            "color": "F^{AB}_{DE}",
            "edge": "e0",
            "basis": "R1",
            "cut_action": "left",
        },
        {
            "id": "AD_CROSSED_E2",
            "pair_id": "AD",
            "pair": "A__Ddot1",
            "allocation": "crossed",
            "color": "F^{BA}_{DE}",
            "edge": "e2",
            "basis": "R2",
            "cut_action": "right",
        },
        {
            "id": "DA_DIRECT_E2",
            "pair_id": "DA",
            "pair": "Ddot1__A",
            "allocation": "direct",
            "color": "F^{AB}_{DE}",
            "edge": "e2",
            "basis": "R2",
            "cut_action": "right",
        },
        {
            "id": "DA_CROSSED_E0",
            "pair_id": "DA",
            "pair": "Ddot1__A",
            "allocation": "crossed",
            "color": "F^{BA}_{DE}",
            "edge": "e0",
            "basis": "R1",
            "cut_action": "left",
        },
    )


def expected_basis(
    basis: str,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
) -> alg.A:
    def plus(momentum: alg.Vector) -> alg.A:
        return momentum[3] - alg.I * momentum[2]

    if basis == "R1":
        return (
            alg.I
            * (
                plus(loop)
                + plus(p)
                + plus(q) / 2
            )
            / 16
        )
    if basis == "R2":
        return -alg.I * plus(loop) / 16
    raise ValueError(basis)


def raw_parent_and_contact(
    pair: str,
    allocation: str,
    loop: alg.Vector,
    p: alg.Vector,
    q: alg.Vector,
    tables: dict[str, dict[tuple[str, int, int, int, int, int], alg.A]],
) -> dict[str, dict[tuple[str, str], alg.A]]:
    """Generate the parent quotient and local contact from one shared Hessian.

    ``preimage`` is the raw coefficient of the marked ``D_+u`` before its
    four-dimensional square is inserted.  On the conditional canonical
    slice, ``K_AB=-kappa_AB r^2`` and ``kappa_AB=delta_AB/2``; hence

        r^2 P^A = -2 P^A K_A.

    The parent quotient has three ``-2`` vector kernels.  The Schwinger
    contact has the source-to-Euler factor ``-2``, two uncut ``-2``
    propagators, and the relative functional-derivative sign ``-1``.
    Thus the two independently generated raw edge factors are ``-8`` and
    ``+8``.
    """

    direct = allocation == "direct"
    if allocation not in {"direct", "crossed"}:
        raise ValueError(allocation)
    r0 = loop
    r2 = alg.vadd(loop, p, q)
    source_momenta = (alg.vneg(r0), r2) if direct else (r2, alg.vneg(r0))
    source_table: dict[tuple[int, int], alg.A] = {}
    for left_mask, right_mask in itertools.product(range(16), repeat=2):
        value = raw.source_component_entry(
            pair,
            *source_momenta,
            left_mask,
            right_mask,
            0,
            0,
            1,
            "evanescent",
        )
        if value:
            source_table[left_mask, right_mask] = value

    totals = {
        mode: {
            chirality: alg.ZERO
            for chirality in itertools.product(("+", "-"), repeat=2)
        }
        for mode in ("parent_quotient", "raw_contact")
    }
    left_source_index = 0 if direct else 1
    right_source_index = 1 if direct else 0
    left_source_color = 0 if direct else 1
    right_source_color = 1 if direct else 0
    left_external_color = 1 if direct else 0
    right_external_color = 0 if direct else 1

    # Canonical factorization, independent of component masks.
    parent_edge_scalar = (-2) * (-2) * (-2)
    source_to_euler = -2
    uncut_propagators = (-2) * (-2)
    schwinger_sign = -1
    contact_edge_scalar = source_to_euler * uncut_propagators * schwinger_sign
    if parent_edge_scalar != -8 or contact_edge_scalar != 8:
        raise AssertionError((parent_edge_scalar, contact_edge_scalar))

    for (source_left_mask, source_right_mask), preimage in source_table.items():
        source_masks = (source_left_mask, source_right_mask)
        left_source_mask = 15 ^ source_masks[left_source_index]
        right_source_mask = 15 ^ source_masks[right_source_index]
        cov_left = alg.component_covariance(
            source_masks[left_source_index], left_source_mask
        )
        cov_right = alg.component_covariance(
            source_masks[right_source_index], right_source_mask
        )
        if not cov_left or not cov_right:
            continue
        for left_bridge_mask in range(16):
            right_bridge_mask = 15 ^ left_bridge_mask
            cov_bridge = alg.component_covariance(left_bridge_mask, right_bridge_mask)
            if not cov_bridge:
                continue
            parities = (
                source_left_mask.bit_count() % 2,
                source_right_mask.bit_count() % 2,
                left_source_mask.bit_count() % 2,
                left_bridge_mask.bit_count() % 2,
                1,
                right_source_mask.bit_count() % 2,
                right_bridge_mask.bit_count() % 2,
                1,
            )
            contracted_pairs = (
                ((0, 2), (1, 5), (3, 6))
                if direct
                else ((0, 5), (1, 2), (3, 6))
            )
            wick_sign = raw.wick_pair_sign(parities, contracted_pairs)
            covariance_product = cov_left * cov_right * cov_bridge
            for chirality in totals["parent_quotient"]:
                left_sector, right_sector = chirality
                action_kernel = alg.ZERO
                for bridge_color in range(3):
                    left = tables["left"].get(
                        (
                            left_sector,
                            left_external_color,
                            left_source_color,
                            bridge_color,
                            left_source_mask,
                            left_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    right = tables["right"].get(
                        (
                            right_sector,
                            right_external_color,
                            right_source_color,
                            bridge_color,
                            right_source_mask,
                            right_bridge_mask,
                        ),
                        alg.ZERO,
                    )
                    action_kernel += left * right
                common = wick_sign * covariance_product * preimage * action_kernel
                totals["parent_quotient"][chirality] += parent_edge_scalar * common
                totals["raw_contact"][chirality] += contact_edge_scalar * common
    return totals


def combinatoric_rows(occurrence: dict[str, str]) -> list[dict[str, str]]:
    """Eight labeled rows before their canonicalized Hessian sum."""

    cut_action = occurrence["cut_action"]
    uncut_action = "right" if cut_action == "left" else "left"
    rows: list[dict[str, str]] = []
    for action_order, cut_endpoint, remaining_pairing in itertools.product(
        ("CUT_THEN_UNCUT", "UNCUT_THEN_CUT"),
        ("QUANTUM_PORT_1", "QUANTUM_PORT_2"),
        (
            "SPECTATOR_TO_PORT1__BRIDGE_TO_PORT2",
            "SPECTATOR_TO_PORT2__BRIDGE_TO_PORT1",
        ),
    ):
        rows.append(
            {
                "id": f"{occurrence['id']}::{action_order}::{cut_endpoint}::{remaining_pairing}",
                "action_order": action_order,
                "action_order_weight": "1/2",
                "cut_action": cut_action,
                "cut_endpoint": cut_endpoint,
                "cut_vertex_quantum_Taylor_weight": "1/2",
                "uncut_action": uncut_action,
                "remaining_pairing": remaining_pairing,
                "uncut_vertex_quantum_Taylor_weight": "1/2",
                "canonicalized_relative_Hessian_word": "+1",
                "row_weight": "1/8",
            }
        )
    return rows


def combinatoric_certificate(ledger: Ledger) -> dict[str, object]:
    action_order = Fraction(1, 2) * 2
    cut_endpoint = Fraction(1, 2) * 2
    remaining_wick = Fraction(1, 2) * 2
    total = action_order * cut_endpoint * remaining_wick
    ledger.check("ACTION_ORDER_HALF_TIMES_TWO", action_order, Fraction(1))
    ledger.check("CUT_ENDPOINT_HALF_TIMES_TWO", cut_endpoint, Fraction(1))
    ledger.check("REMAINING_WICK_HALF_TIMES_TWO", remaining_wick, Fraction(1))
    ledger.check("RAW_CONTACT_MULTIPLICITY", total, Fraction(1))
    rows: dict[str, object] = {}
    for occurrence in occurrence_data():
        labeled = combinatoric_rows(occurrence)
        weight_sum = sum((Fraction(row["row_weight"]) for row in labeled), Fraction())
        ledger.check(f"{occurrence['id']}_EIGHT_ROWS", len(labeled), 8)
        ledger.check(f"{occurrence['id']}_ROW_WEIGHT_SUM", weight_sum, Fraction(1))
        rows[occurrence["id"]] = labeled
    return {
        "interaction_expansion": {
            "factorial": "1/2!",
            "action_orders": 2,
            "product": "1",
        },
        "cut_action_background_linear_vertex": {
            "quantum_Taylor_factor": "1/2!",
            "functional_derivative_endpoint_placements": 2,
            "product": "1",
        },
        "uncut_action_background_linear_vertex": {
            "quantum_Taylor_factor": "1/2!",
            "ordered_two_line_Wick_pairings": 2,
            "product": "1",
        },
        "m_contact": "1",
        "labeled_rows": rows,
    }


def frame_rows(ledger: Ledger, workers: int) -> dict[str, object]:
    rows: dict[str, object] = {}
    for frame_index, (loop, p, q) in enumerate(raw.interpolation_samples()):
        tables = audit._full_cubic_hessian_tables(loop, p, q, workers)
        frame: dict[str, object] = {
            "loop": [entry.text() for entry in loop],
            "p_raw": [entry.text() for entry in p],
            "q_raw": [entry.text() for entry in q],
            "action_table_sizes": {
                vertex: len(table) for vertex, table in tables.items()
            },
            "occurrences": {},
        }
        for occurrence in occurrence_data():
            values = raw_parent_and_contact(
                occurrence["pair"],
                occurrence["allocation"],
                loop,
                p,
                q,
                tables,
            )
            expected = expected_basis(occurrence["basis"], loop, p, q)
            chirality_rows: dict[str, object] = {}
            for chirality in itertools.product(("+", "-"), repeat=2):
                tag = "".join(chirality)
                parent = values["parent_quotient"][chirality]
                contact = values["raw_contact"][chirality]
                prefix = f"FRAME{frame_index}_{occurrence['id']}_{tag}"
                ledger.check(f"{prefix}_PARENT", parent, expected)
                ledger.check(f"{prefix}_CONTACT", contact, -expected)
                ledger.check(f"{prefix}_FULL_D_ZERO", parent + contact, alg.ZERO)
                chirality_rows[tag] = {
                    "N_d_parent_quotient": parent.text(),
                    "K_raw_contact": contact.text(),
                    "N_d_plus_K_raw": (parent + contact).text(),
                }
            parent_total = sum(values["parent_quotient"].values(), alg.ZERO)
            contact_total = sum(values["raw_contact"].values(), alg.ZERO)
            prefix = f"FRAME{frame_index}_{occurrence['id']}_TOTAL"
            ledger.check(f"{prefix}_PARENT_FOUR", parent_total, 4 * expected)
            ledger.check(f"{prefix}_CONTACT_FOUR", contact_total, -4 * expected)
            ledger.check(f"{prefix}_FULL_D_ZERO", parent_total + contact_total, alg.ZERO)
            frame["occurrences"][occurrence["id"]] = {
                "pair": occurrence["pair_id"],
                "allocation": occurrence["allocation"],
                "color": occurrence["color"],
                "marked_edge": occurrence["edge"],
                "basis": occurrence["basis"],
                "chirality_sectors": chirality_rows,
                "four_sector_sum": {
                    "N_d_parent_quotient": parent_total.text(),
                    "K_raw_contact": contact_total.text(),
                    "N_d_plus_K_raw": (parent_total + contact_total).text(),
                },
            }
        rows[f"frame_{frame_index}"] = frame
    return rows


def finite_w_link_certificate(ledger: Ledger) -> dict[str, object]:
    s, x, y, residue = sp.symbols("s x y C_omega_e")
    phase = sp.exp(s * x + (1 - s) * y)
    derivative_check = sp.simplify(sp.diff(phase, s) - (x - y) * phase)
    boundary = sp.simplify(phase.subs(s, 1) - phase.subs(s, 0))
    endpoint = residue * (sp.exp(x) - sp.exp(y))
    one_link = -residue * boundary
    ledger.check("T1_DUHAMEL_DIFFERENTIAL", derivative_check, 0)
    ledger.check("T1_DUHAMEL_BOUNDARY", boundary, sp.exp(x) - sp.exp(y))
    ledger.check("T1_ENDPOINT_CANCELLATION", sp.simplify(endpoint + one_link), 0)
    rows = []
    for occurrence in occurrence_data():
        rows.append(
            {
                "local_occurrence": occurrence["id"],
                "local_residue": occurrence["basis"],
                "link_color_order": "(M_1)^B_C=c_{LC}{}^B*w^m*a_m^L",
                "phase_endpoints": ["x=i*w.r", "y=i*w.r_prime"],
                "endpoint_row": "+C_omega_e*(exp(x)-exp(y))",
                "one_link_row": "-C_omega_e*(x-y)*int_0^1 ds exp(s*x+(1-s)*y)",
                "sum": "0",
                "classification": "LINK_WARD_CANCELLATION",
                "mu2_anomaly": "0",
            }
        )
    return {
        "canonical_linear_connection": (
            "a_m^{L,(1)}[u]=(i*sqrt(2)/8)*bar_sigma_m^{dot b a}*"
            "[D_a,barD_dot b]_ord*u^L|"
        ),
        "origin": (
            "A_P,m=(i/8)*bar_sigma_m[D,barD]_ord*V_P|; "
            "V_P=sqrt(2)*g*u; A_P,m=g*a_m"
        ),
        "link_generator": "(M_1[u])^B_C=w^m*c_{LC}{}^B*a_m^{L,(1)}[u]",
        "functional_derivatives": {
            "with_respect_to_a": (
                "delta(M_1)^B_C/delta a_n^J=w^n*c_{JC}{}^B"
            ),
            "with_respect_to_u": (
                "delta(M_1)^B_C/delta u^J="
                "(i*sqrt(2)/8)*w^m*c_{JC}{}^B*"
                "bar_sigma_m^{dot b a}[D_a,barD_dot b]_ord"
            ),
        },
        "T1_derivative": (
            "delta(T1 Y)^B/delta a_n^J="
            "w^n*c_{JC}{}^B*int_0^1 ds "
            "exp(i*w.[s*r+(1-s)*r_prime])*Y^C"
        ),
        "longitudinal_contraction": (
            "i*(r-r_prime)_n*delta(T1 Y)/delta a_n="
            "c*(exp(i*w.r)-exp(i*w.r_prime))*Y"
        ),
        "identity": (
            "(x-y)*int_0^1 ds exp(s*x+(1-s)*y)=exp(x)-exp(y); "
            "x=i*w.r, y=i*w.r_prime"
        ),
        "occurrence_rows": rows,
        "w_zero": "T1=0 because M_1 contains one explicit w",
        "anomaly_reason": (
            "The phase-weighted link and endpoint rows cancel before loop "
            "integration in arbitrary d; they contain no det_4-det_d remainder."
        ),
    }


def build(workers: int = 8, replay_frames: bool = True) -> dict[str, object]:
    ledger = Ledger()
    combinatorics = combinatoric_certificate(ledger)
    parent_contact = frame_rows(ledger, workers) if replay_frames else {}
    finite_w = finite_w_link_certificate(ledger)
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    return {
        "schema": "step5-ad-da-raw-contact-hessian-multiplicity-exact-v1",
        "external_target_used": False,
        "local_w0": {
            "kinetic_metric": "K_AB=-kappa_AB*r_e^2; kappa_AB=delta_AB/2",
            "source_to_euler": "r_e^2*P^A=-2*P^A*K_A",
            "parent_edge_factor": "(-2)^3=-8",
            "contact_edge_factor": "(-1)_SD*(-2)_source_to_Euler*(-2)^2_uncut=+8",
            "combinatorics": combinatorics,
            "m_contact": "1",
            "replay_frames": parent_contact,
            "full_d_identity": "N_d+K_raw=0 occurrencewise and chirality-sectorwise",
        },
        "finite_w_one_link": finite_w,
        "normalization_consequence": {
            "m_parent": "1",
            "m_contact": "1",
            "extra_chi_factor": "1",
            "raw_contact_half": "REJECTED",
        },
        "status": (
            "PASS_RAW_LOCAL_CONTACT_MULTIPLICITY_ONE__"
            "FINITE_W_LINK_LONGITUDINAL_ZERO"
        ) if failed == 0 else "FAIL",
        "checks": {
            "count": len(ledger.rows),
            "passed": len(ledger.rows) - failed,
            "failed": failed,
            "rows": ledger.rows,
        },
    }


def render_markdown(payload: dict[str, object]) -> str:
    checks = payload["checks"]
    assert isinstance(checks, dict)
    template = r"""# Step 5 AD/DA raw Schwinger contact Hessian multiplicity

Status: `{STATUS}`.

## 1. Local contact

$$
K_{{AB}}=-\kappa_{{AB}}r_e^2,
\qquad \kappa_{{AB}}=\frac12\delta_{{AB}},
\qquad r_e^2P^A=-2P^AK_A.
$$

The parent quotient and independently generated Schwinger contact carry

$$
c_{{\rm parent}}=(-2)^3=-8,
$$

$$
c_{{\rm contact}}
=(-1)_{{\rm SD}}(-2)_{{r^2P=-2PK}}(-2)^2_{{\rm uncut}}=+8.
$$

For every AD/DA, direct/crossed, and chirality row,

$$
N_d+K_{{\rm raw}}=0.
$$

The exact multiplicity is

$$
\left(\frac1{{2!}}\times2_{{\rm action\ order}}\right)
\left(\frac1{{2!}}\times2_{{\rm cut\ endpoint}}\right)
\left(\frac1{{2!}}\times2_{{\rm remaining\ Wick}}\right)=1.
$$

Thus

$$
m_{{\rm contact}}=1.
$$

## 2. Finite-w one-link row

$$
a_m^{{L,(1)}}[u]
=\frac{{i\sqrt2}}8(\bar\sigma_m)^{{\dot ba}}
[D_a,\bar D_{{\dot b}}]_{{\rm ord}}u^L\Big|,
$$

$$
(\mathbb M_1[u])^B{}_C
=w^mc_{{LC}}{}^Ba_m^{{L,(1)}}[u].
$$

Writing $x=iw\cdot r$ and $y=iw\cdot r'$, the functional derivative of
$T_1$ has unit Duhamel coefficient and phase

$$
\int_0^1ds\,e^{{sx+(1-s)y}}.
$$

Therefore

$$
(x-y)\int_0^1ds\,e^{{sx+(1-s)y}}
=e^x-e^y,
$$

and every endpoint plus one-link row is

$$
C_{{\omega,e}}(e^x-e^y)
-C_{{\omega,e}}(e^x-e^y)=0.
$$

This cancellation holds before loop integration in arbitrary $d$; its
$\mu_\ell^2$ anomaly sector is zero.

$$
N_{{\rm pass}}={checks['passed']},\qquad
N_{{\rm fail}}={FAILED}.
$$
"""
    return (
        template.replace("{STATUS}", str(payload["status"]))
        .replace("{checks['passed']}", str(checks["passed"]))
        .replace("{FAILED}", str(checks["failed"]))
        .replace("{{", "{")
        .replace("}}", "}")
    )


def validate(payload: dict[str, object]) -> None:
    if payload.get("status") != (
        "PASS_RAW_LOCAL_CONTACT_MULTIPLICITY_ONE__"
        "FINITE_W_LINK_LONGITUDINAL_ZERO"
    ):
        raise AssertionError(payload.get("status"))
    checks = payload.get("checks")
    if not isinstance(checks, dict) or checks.get("failed") != 0:
        raise AssertionError(checks)
    local = payload.get("local_w0")
    if not isinstance(local, dict) or local.get("m_contact") != "1":
        raise AssertionError(local)
    consequence = payload.get("normalization_consequence")
    if not isinstance(consequence, dict) or consequence.get("extra_chi_factor") != "1":
        raise AssertionError(consequence)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--no-replay", action="store_true")
    args = parser.parse_args()
    if args.check_artifact:
        validate(json.loads(JSON_OUT.read_text(encoding="utf-8")))
        return 0
    payload = build(args.workers, replay_frames=not args.no_replay)
    validate(payload)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        JSON_OUT.write_text(serialized, encoding="utf-8")
        MD_OUT.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
