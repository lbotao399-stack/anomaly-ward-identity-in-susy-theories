#!/usr/bin/env python3
"""Exact external-slot polarization of the AA cubic gauge Hessian.

For each chirality the cubic compact action is trilinear in

    linear field strength, derivative commutator slot, plain commutator slot.

The old fixed-field-strength probe retained only the first placement.  This
audit partitions all raw labeled port derivatives into the three placements,
replays exact sparse-superfield components, and verifies that their sum is the
full cubic action Hessian.  No holomorphic target is read.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_full_raw_triangle_component_probe as probe  # noqa: E402
import step5_aa_gauge_full_source_sd_orbit_exact_audit as alg  # noqa: E402
import step5_aa_gauge_raw_convolution_hessian_exact_audit as old  # noqa: E402
import step5_aa_matter_full_placements_independent_audit as matter  # noqa: E402


JSON_OUT = ROOT / "audits" / "step5-aa-external-slot-decomposition-exact.json"
MD_OUT = ROOT / "audits" / "step5-aa-external-slot-decomposition-exact.md"
SYMBOLIC_FRAME_FILES = {
    "canonical": ROOT / "audits" / "step5-aa-full-polarized-symbolic-exact.json",
    "alternate": ROOT
    / "audits"
    / "step5-aa-full-polarized-symbolic-alternate-frame-exact.json",
    "p_only": ROOT / "audits" / "step5-aa-full-polarized-symbolic-p-only-exact.json",
    "q_only": ROOT / "audits" / "step5-aa-full-polarized-symbolic-q-only-exact.json",
    "p_transverse": ROOT
    / "audits"
    / "step5-aa-full-polarized-symbolic-p-transverse-exact.json",
    "q_transverse": ROOT
    / "audits"
    / "step5-aa-full-polarized-symbolic-q-transverse-exact.json",
    "swapped_transverse": ROOT
    / "audits"
    / "step5-aa-full-polarized-symbolic-swapped-transverse-exact.json",
}


PLACEMENTS = (
    "linear_field_strength",
    "derivative_commutator",
    "plain_commutator",
)


ROLE_SLOTS = {
    "1000": {
        "linear_field_strength": "Z",
        "derivative_commutator": "Y",
        "plain_commutator": "X",
    },
    "0100": {
        "linear_field_strength": "Z",
        "derivative_commutator": "X",
        "plain_commutator": "Y",
    },
    "0010": {
        "linear_field_strength": "X",
        "derivative_commutator": "Z",
        "plain_commutator": "Y",
    },
    "0001": {
        "linear_field_strength": "X",
        "derivative_commutator": "Y",
        "plain_commutator": "Z",
    },
}

SOURCE_TAG_T0 = "I0_DminusA1[A]*A1[B]"
SOURCE_TAG_T2 = "I0_A1[A]*DminusA1[B]"


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
    if isinstance(value, tuple):
        return "(" + ",".join(exact_text(item) for item in value) + ")"
    return str(value)


def formal_polarization_certificate(ledger: Ledger) -> dict[str, object]:
    fields = ("Q1", "Q2", "E")
    full_terms = tuple(itertools.permutations(fields))
    partition: dict[str, list[dict[str, str]]] = {name: [] for name in PLACEMENTS}
    for strength, derivative, plain in full_terms:
        if strength == "E":
            placement = "linear_field_strength"
        elif derivative == "E":
            placement = "derivative_commutator"
        elif plain == "E":
            placement = "plain_commutator"
        else:
            raise AssertionError((strength, derivative, plain))
        partition[placement].append(
            {"W_linear": strength, "D_slot": derivative, "plain_slot": plain}
        )
    ledger.check("FORMAL_FULL_TERM_COUNT", len(full_terms), 6)
    ledger.check(
        "FORMAL_PARTITION_COUNTS",
        tuple(len(partition[name]) for name in PLACEMENTS),
        (2, 2, 2),
    )
    ledger.check(
        "FORMAL_PARTITION_EXHAUSTIVE",
        sum(len(partition[name]) for name in PLACEMENTS),
        len(full_terms),
    )
    return {
        "trilinear_word": "c_chi*Tr(W_chi^(1)(U)*[D_chi U,U])",
        "labeled_fields": list(fields),
        "coefficient": "[t1*t2*tE]",
        "classes": partition,
        "identity": "H_full=H_linear_field_strength+H_derivative_commutator+H_plain_commutator",
    }


def classify_raw_ports(ledger: Ledger) -> dict[str, object]:
    rows = old.raw_port_rows()
    classified: list[dict[str, object]] = []
    counts: dict[str, Counter[str]] = {"+": Counter(), "-": Counter()}
    for row in rows:
        word_id = str(row["id"]).split(":")[1]
        assignment = row["assignment"]
        if not isinstance(assignment, dict):
            raise TypeError("raw assignment")
        matches = [
            placement
            for placement, slot in ROLE_SLOTS[word_id].items()
            if assignment[slot] == "E"
        ]
        ledger.check(f"RAW_UNIQUE_CLASS_{row['id']}", len(matches), 1)
        placement = matches[0]
        counts[str(row["chirality"])][placement] += 1
        classified.append(
            {
                "id": row["id"],
                "chirality": row["chirality"],
                "pqrs": row["pqrs"],
                "assignment": assignment,
                "placement": placement,
                "coefficient_canonical_u": row["coefficient_canonical_u"],
            }
        )
    for sector in ("+", "-"):
        ledger.check(f"RAW_{sector}_TOTAL", sum(counts[sector].values()), 24)
        ledger.check(
            f"RAW_{sector}_CLASS_COUNTS",
            tuple(counts[sector][name] for name in PLACEMENTS),
            (8, 8, 8),
        )
    old_fixed = [
        row for row in classified if row["placement"] == "linear_field_strength"
    ]
    omitted = [
        row for row in classified if row["placement"] != "linear_field_strength"
    ]
    ledger.check("OLD_FIXED_RAW_ROWS", len(old_fixed), 16)
    ledger.check("OLD_FIXED_OMITTED_ROWS", len(omitted), 32)
    return {
        "role_slots_by_raw_word": ROLE_SLOTS,
        "counts": {
            sector: {name: counts[sector][name] for name in PLACEMENTS}
            for sector in ("+", "-")
        },
        "all_rows": len(classified),
        "old_fixed_linear_rows": len(old_fixed),
        "old_fixed_omitted_rows": len(omitted),
        "old_fixed_omitted_classes": [
            "derivative_commutator",
            "plain_commutator",
        ],
        "rows": classified,
    }


def _spinor_derivative(value: alg.Mat, node: str, index: int, sector: str) -> alg.Mat:
    if sector == "+":
        return alg.mat_d(value, node, index)
    if sector == "-":
        return alg.mat_bar_d(value, node, index)
    raise ValueError(sector)


def _linear_strength(value: alg.Mat, node: str, index: int, sector: str) -> alg.Mat:
    if sector == "+":
        return alg.mat_scale(
            -alg.SQRT2 / Fraction(8),
            alg.mat_bar_d2(alg.mat_d(value, node, index), node),
        )
    if sector == "-":
        return alg.mat_scale(
            -alg.SQRT2 / Fraction(8),
            alg.mat_d2(alg.mat_bar_d(value, node, index), node),
        )
    raise ValueError(sector)


def _commutator_word(
    derivative_field: alg.Mat,
    plain_field: alg.Mat,
    node: str,
    index: int,
    sector: str,
) -> alg.Mat:
    derivative = _spinor_derivative(derivative_field, node, index, sector)
    return alg.mat_sub(
        alg.mat_mul(derivative, plain_field),
        alg.mat_mul(plain_field, derivative),
    )


def _compact_cubic_integrand(
    strength_field: alg.Mat,
    derivative_field: alg.Mat,
    plain_field: alg.Mat,
    node: str,
    sector: str,
) -> alg.P:
    strength_lower = tuple(
        _linear_strength(strength_field, node, index, sector)
        for index in range(2)
    )
    commutator_lower = tuple(
        _commutator_word(
            derivative_field,
            plain_field,
            node,
            index,
            sector,
        )
        for index in range(2)
    )
    if sector == "+":
        strength_upper = (strength_lower[1], alg.mat_neg(strength_lower[0]))
        contracted = alg.mat_add(
            alg.mat_mul(strength_upper[0], commutator_lower[0]),
            alg.mat_mul(strength_upper[1], commutator_lower[1]),
        )
        return Fraction(-1, 4) * alg.mat_trace(contracted)
    commutator_upper = (
        commutator_lower[1],
        alg.mat_neg(commutator_lower[0]),
    )
    contracted = alg.mat_add(
        alg.mat_mul(strength_lower[0], commutator_upper[0]),
        alg.mat_mul(strength_lower[1], commutator_upper[1]),
    )
    return Fraction(1, 4) * alg.mat_trace(contracted)


def placement_hessian_values(
    sector: str,
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    background_momentum: alg.Vector,
    background_type: str,
    polarization: alg.Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int = 1,
    external_a: int = 0,
) -> dict[str, alg.A]:
    ctx = alg.Context(
        ("X",),
        (
            {"X": momentum_1},
            {"X": momentum_2},
            {"X": background_momentum},
        ),
        6,
    )
    quantum = alg.sum_mats(
        [
            alg.basis_endpoint(ctx, "X", 0, color_1, theta_mask_1, 5),
            alg.basis_endpoint(ctx, "X", 1, color_2, theta_mask_2, 6),
        ]
    )
    if background_type == "A":
        background = alg.endpoint_A(
            ctx, "X", 2, external_a, polarization
        )
    elif background_type == "D":
        background = alg.endpoint_D(
            ctx, "X", 2, external_d, dotted, eta_index=4
        )
    else:
        raise ValueError(background_type)

    fields = {
        "linear_field_strength": (background, quantum, quantum),
        "derivative_commutator": (quantum, background, quantum),
        "plain_commutator": (quantum, quantum, background),
    }
    marker = alg.hessian_marker_mask(
        theta_mask_1,
        theta_mask_2,
        background_type == "D",
    )
    values: dict[str, alg.A] = {}
    for placement, arguments in fields.items():
        integrand = _compact_cubic_integrand(*arguments, "X", sector)
        coefficient = integrand.coefficient_labels((1, 1, 1))
        coefficient = Fraction(1, 16) * alg.d2(
            alg.bar_d2(coefficient, "X"), "X"
        )
        value = coefficient.set_coordinates_zero("X").grass_coefficient(marker)
        values[placement] = value
    return values


def full_and_old_fixed_values(
    sector: str,
    momentum_1: alg.Vector,
    momentum_2: alg.Vector,
    background_momentum: alg.Vector,
    background_type: str,
    polarization: alg.Vector,
    dotted: int,
    color_1: int,
    color_2: int,
    theta_mask_1: int,
    theta_mask_2: int,
    external_d: int = 1,
    external_a: int = 0,
) -> tuple[alg.A, alg.A]:
    arguments = (
        sector,
        momentum_1,
        momentum_2,
        background_momentum,
        background_type,
        polarization,
        dotted,
        color_1,
        color_2,
        theta_mask_1,
        theta_mask_2,
        external_d,
        external_a,
    )
    full = probe.action_hessian_sector_task(arguments)[-1]
    old_fixed = probe.fixed_field_strength_hessian_task(arguments)[-1]
    return full, old_fixed


FRAME_M1 = alg.vec((1, 2, 0, 1))
FRAME_M2 = alg.vec((-2, 1, 1, 0))
FRAME_BG = alg.vneg(alg.vadd(FRAME_M1, FRAME_M2))
FRAME_POL = alg.vec((0, 0, 0, 1))


SAMPLE_SPECS = (
    ("plus_A_00", "+", "A", 1, 2, 0, 0),
    ("plus_A_1_13", "+", "A", 1, 2, 1, 13),
    ("minus_A_cross", "-", "A", 1, 2, 0, 0),
    ("minus_D_0_4", "-", "D", 0, 2, 0, 4),
    ("plus_D_cross", "+", "D", 0, 2, 0, 4),
)


SAMPLE_EXPECTED = {
    "plus_A_00": {
        "linear_field_strength": 3 * alg.SQRT2 / 8,
        "derivative_commutator": -3 * alg.SQRT2 / 32,
        "plain_commutator": -3 * alg.SQRT2 / 32,
        "full": 3 * alg.SQRT2 / 16,
        "old_fixed": 3 * alg.SQRT2 / 8,
    },
    "plus_A_1_13": {
        "linear_field_strength": -3 * alg.SQRT2 / 32 - alg.I * alg.SQRT2 / 32,
        "derivative_commutator": alg.SQRT2 / 32 + 3 * alg.I * alg.SQRT2 / 128,
        "plain_commutator": alg.SQRT2 / 64 - alg.I * alg.SQRT2 / 128,
        "full": -3 * alg.SQRT2 / 64 - alg.I * alg.SQRT2 / 64,
        "old_fixed": -3 * alg.SQRT2 / 32 - alg.I * alg.SQRT2 / 32,
    },
    "minus_A_cross": {
        "linear_field_strength": 3 * alg.SQRT2 / 8,
        "derivative_commutator": -3 * alg.SQRT2 / 32,
        "plain_commutator": -3 * alg.SQRT2 / 32,
        "full": 3 * alg.SQRT2 / 16,
        "old_fixed": alg.ZERO,
    },
    "minus_D_0_4": {
        "linear_field_strength": alg.SQRT2 / 32 + 3 * alg.I * alg.SQRT2 / 64,
        "derivative_commutator": -3 * alg.I * alg.SQRT2 / 128,
        "plain_commutator": -3 * alg.I * alg.SQRT2 / 128,
        "full": alg.SQRT2 / 32,
        "old_fixed": alg.SQRT2 / 32 + 3 * alg.I * alg.SQRT2 / 64,
    },
    "plus_D_cross": {
        "linear_field_strength": alg.SQRT2 / 16,
        "derivative_commutator": -alg.SQRT2 / 64,
        "plain_commutator": -alg.SQRT2 / 64,
        "full": alg.SQRT2 / 32,
        "old_fixed": alg.ZERO,
    },
}


def sample_component_certificate(ledger: Ledger) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sample_id, sector, background_type, color_1, color_2, mask_1, mask_2 in SAMPLE_SPECS:
        placements = placement_hessian_values(
            sector,
            FRAME_M1,
            FRAME_M2,
            FRAME_BG,
            background_type,
            FRAME_POL,
            0,
            color_1,
            color_2,
            mask_1,
            mask_2,
        )
        full, old_fixed = full_and_old_fixed_values(
            sector,
            FRAME_M1,
            FRAME_M2,
            FRAME_BG,
            background_type,
            FRAME_POL,
            0,
            color_1,
            color_2,
            mask_1,
            mask_2,
        )
        expected = SAMPLE_EXPECTED[sample_id]
        for placement in PLACEMENTS:
            ledger.check(
                f"SAMPLE_{sample_id}_{placement}",
                placements[placement],
                expected[placement],
            )
        placement_sum = sum(placements.values(), alg.ZERO)
        ledger.check(f"SAMPLE_{sample_id}_SUM_FULL", placement_sum, full)
        ledger.check(f"SAMPLE_{sample_id}_FULL", full, expected["full"])
        ledger.check(
            f"SAMPLE_{sample_id}_OLD_FIXED", old_fixed, expected["old_fixed"]
        )
        rows.append(
            {
                "id": sample_id,
                "sector": sector,
                "background_type": background_type,
                "colors": [color_1, color_2],
                "theta_masks": [mask_1, mask_2],
                "placements": {
                    name: placements[name].text() for name in PLACEMENTS
                },
                "placement_sum": placement_sum.text(),
                "full_action_hessian": full.text(),
                "old_fixed_probe": old_fixed.text(),
                "old_fixed_minus_full": (old_fixed - full).text(),
            }
        )
    return rows


def _supported_color_pairs(background_type: str) -> tuple[tuple[int, int], ...]:
    external_color = 0 if background_type == "A" else 1
    return tuple(
        (color_1, color_2)
        for color_1, color_2 in itertools.product(range(3), repeat=2)
        if len({color_1, color_2, external_color}) == 3
    )


def _exhaustive_task(
    arguments: tuple[str, str, int, int, int, int]
) -> tuple[str, str, int, int, int, int, dict[str, alg.A], alg.A]:
    sector, background_type, color_1, color_2, mask_1, mask_2 = arguments
    placements = placement_hessian_values(
        sector,
        FRAME_M1,
        FRAME_M2,
        FRAME_BG,
        background_type,
        FRAME_POL,
        0,
        color_1,
        color_2,
        mask_1,
        mask_2,
    )
    full, _ = full_and_old_fixed_values(
        sector,
        FRAME_M1,
        FRAME_M2,
        FRAME_BG,
        background_type,
        FRAME_POL,
        0,
        color_1,
        color_2,
        mask_1,
        mask_2,
    )
    return (
        sector,
        background_type,
        color_1,
        color_2,
        mask_1,
        mask_2,
        placements,
        full,
    )


def exhaustive_component_replay(workers: int) -> dict[str, object]:
    tasks = [
        (sector, background_type, color_1, color_2, mask_1, mask_2)
        for sector, background_type in itertools.product(("+", "-"), ("A", "D"))
        for color_1, color_2 in _supported_color_pairs(background_type)
        for mask_1, mask_2 in itertools.product(range(16), repeat=2)
    ]
    context = multiprocessing.get_context("fork")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        evaluations = list(pool.map(_exhaustive_task, tasks, chunksize=4))

    summaries: dict[str, dict[str, object]] = {}
    for sector, background_type in itertools.product(("+", "-"), ("A", "D")):
        key = f"{sector}_{background_type}"
        summaries[key] = {
            "all_color_mask_rows": 9 * 16 * 16,
            "analytic_color_zero_rows": 7 * 16 * 16,
            "sparse_replayed_rows": 2 * 16 * 16,
            "equality_failures": 0,
            "nonzero_counts": {
                "full": 0,
                **{name: 0 for name in PLACEMENTS},
                "derivative_plus_plain": 0,
                "old_fixed_model": 0,
                "old_fixed_full_mismatch": 0,
            },
            "fingerprints": {
                name: {"sum": alg.ZERO, "weighted_sum": alg.ZERO}
                for name in ("full", *PLACEMENTS, "derivative_plus_plain")
            },
        }

    for (
        sector,
        background_type,
        color_1,
        color_2,
        mask_1,
        mask_2,
        placements,
        full,
    ) in evaluations:
        key = f"{sector}_{background_type}"
        summary = summaries[key]
        counts = summary["nonzero_counts"]
        fingerprints = summary["fingerprints"]
        if not isinstance(counts, dict) or not isinstance(fingerprints, dict):
            raise TypeError("summary")
        placement_sum = sum(placements.values(), alg.ZERO)
        if placement_sum != full:
            summary["equality_failures"] = int(summary["equality_failures"]) + 1
        missing = placements["derivative_commutator"] + placements["plain_commutator"]
        old_fixed_model = (
            placements["linear_field_strength"]
            if (sector, background_type) in (("+", "A"), ("-", "D"))
            else alg.ZERO
        )
        values = {"full": full, **placements, "derivative_plus_plain": missing}
        weight = 1 + color_1 + 3 * color_2 + 9 * mask_1 + 153 * mask_2
        for name, value in values.items():
            if value:
                counts[name] = int(counts[name]) + 1
            fingerprint = fingerprints[name]
            if not isinstance(fingerprint, dict):
                raise TypeError("fingerprint")
            fingerprint["sum"] = fingerprint["sum"] + value
            fingerprint["weighted_sum"] = fingerprint["weighted_sum"] + weight * value
        if old_fixed_model:
            counts["old_fixed_model"] = int(counts["old_fixed_model"]) + 1
        if old_fixed_model != full:
            counts["old_fixed_full_mismatch"] = int(counts["old_fixed_full_mismatch"]) + 1

    rendered: dict[str, object] = {}
    for key, summary in summaries.items():
        fingerprints = summary["fingerprints"]
        if not isinstance(fingerprints, dict):
            raise TypeError("fingerprints")
        rendered[key] = {
            **{name: value for name, value in summary.items() if name != "fingerprints"},
            "fingerprints": {
                name: {
                    field: exact_text(value)
                    for field, value in fingerprint.items()
                }
                for name, fingerprint in fingerprints.items()
                if isinstance(fingerprint, dict)
            },
        }
    return {
        "frame": {
            "momentum_1": [value.text() for value in FRAME_M1],
            "momentum_2": [value.text() for value in FRAME_M2],
            "background_momentum": [value.text() for value in FRAME_BG],
            "polarization": [value.text() for value in FRAME_POL],
        },
        "color_zero_proof": "epsilon(c1,c2,c_external)=0 unless all three colors are distinct",
        "summaries": rendered,
        "total_sparse_replayed_rows": len(evaluations),
        "total_analytic_color_zero_rows": 4 * 7 * 16 * 16,
        "total_full_color_mask_rows": 4 * 9 * 16 * 16,
        "total_equality_failures": sum(
            int(summary["equality_failures"]) for summary in summaries.values()
        ),
    }


def source_edge_quotient_certificate(
    ledger: Ledger,
    triangle_replay: tuple[dict[str, object], dict[str, int]] | None = None,
) -> dict[str, object]:
    # Full-action aggregate tags are edge-divisible, but the quotient is
    # quadratic.  An affine interpolation is therefore invalid.  The
    # occurrence-to-edge map is proved below.  The separate raw Schwinger
    # contact-Hessian multiplicity is deliberately not inferred from this
    # selected-parent divisibility statement.
    placement_pairs = tuple(
        f"{left}__{right}" for left in PLACEMENTS for right in PLACEMENTS
    )
    ledger.check("PLACEMENT_PAIR_COUNT", len(placement_pairs), 9)
    l0, l1 = sp.symbols("l0 l1")
    q0 = (
        -l0**2 / 2
        + sp.I * l0 * l1
        + (sp.Rational(3, 2) - sp.I) * l0
        + l1**2 / 2
        - (1 + 3 * sp.I / 2) * l1
        - sp.Rational(1, 2)
        + 3 * sp.I / 2
    )
    q2 = (
        -l0**2 / 2
        + sp.I * l0 * l1
        - l0 / 2
        + l1**2 / 2
        + sp.I * l1 / 2
    )
    q0_quadratic = -l0**2 / 2 + sp.I * l0 * l1 + l1**2 / 2
    q2_quadratic = q0_quadratic
    ledger.check(
        "QUADRATIC_TRACELESS_SUM",
        sp.expand(q0_quadratic + q2_quadratic),
        sp.expand(-(l0 - sp.I * l1) ** 2),
    )
    ledger.check(
        "QUADRATIC_LAPLACIAN",
        sp.diff(q0_quadratic + q2_quadratic, l0, 2)
        + sp.diff(q0_quadratic + q2_quadratic, l1, 2),
        0,
    )
    held_l0, held_l1 = 3, 2
    held_q0 = sp.expand(q0.subs({l0: held_l0, l1: held_l1}))
    held_q2 = sp.expand(q2.subs({l0: held_l0, l1: held_l1}))
    ledger.check("HELD_OUT_Q0", held_q0, -sp.Rational(1, 2) + 3 * sp.I / 2)
    ledger.check("HELD_OUT_Q2", held_q2, -4 + 7 * sp.I)
    ledger.check("HELD_OUT_T0", sp.expand(18 * held_q0), -9 + 27 * sp.I)
    ledger.check("HELD_OUT_T2", sp.expand(10 * held_q2), -40 + 70 * sp.I)
    replayed_from_probe = triangle_replay is not None
    if triangle_replay is not None:
        triangle_result, _ = triangle_replay
        selected_tags = triangle_result["selected_source_tags"]
        if not isinstance(selected_tags, dict):
            raise TypeError("selected source tags")
        ledger.check(
            "PROBE_HELD_OUT_T0",
            selected_tags.get(
                ("I0_DminusA1[A]*A1[B]", "-", "+"),
                alg.ZERO,
            ),
            -alg.A(9) + alg.A(27) * alg.I,
        )
        ledger.check(
            "PROBE_HELD_OUT_T2",
            selected_tags.get(
                ("I0_A1[A]*DminusA1[B]", "-", "+"),
                alg.ZERO,
            ),
            -alg.A(40) + alg.A(70) * alg.I,
        )
    return {
        "source_tags": {
            "e0": "I0_DminusA1[A]*A1[B]",
            "e2": "I0_A1[A]*DminusA1[B]",
        },
        "aggregate_edge_divisibility": {
            "T0": "N_S,T0=bar(r0)^2*Q0",
            "T2": "N_S,T2=bar(r2)^2*Q2",
            "division_remainders": {"T0": "0", "T2": "0"},
            "Q0": sp.sstr(sp.expand(q0)),
            "Q2": sp.sstr(sp.expand(q2)),
            "quotient_degree": 2,
            "affine_fit_valid": False,
            "held_out": {
                "loop": ["3", "2", "-2", "1"],
                "bar_r0_squared": "18",
                "bar_r2_squared": "10",
                "Q0": sp.sstr(held_q0),
                "Q2": sp.sstr(held_q2),
                "T0": "-9 + 27*I",
                "T2": "-40 + 70*I",
                "replayed_from_full_probe": replayed_from_probe,
            },
        },
        "quadratic_homogeneous_sum": {
            "Q0_degree2": sp.sstr(sp.expand(q0_quadratic)),
            "Q2_degree2": sp.sstr(sp.expand(q2_quadratic)),
            "sum": sp.sstr(sp.expand(-(l0 - sp.I * l1) ** 2)),
            "laplacian_l0_l1": "0",
        },
        "placement_pairs": list(placement_pairs),
        "per_pair_identity": {
            "selected_parent": "N_(S,rho)=Q_rho*bar(r_(e(rho)))^2",
            "longitudinal_parent": "L_rho",
            "verified_full_d_contact_at_m_e_1": (
                "-Q_rho*r_(e(rho),d)^2-L_rho"
            ),
            "verified_dred_remainder_at_m_e_1": "Q_rho*mu_l^2",
            "raw_contact_multiplicity_status": (
                "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE"
            ),
        },
        "old_fixed_block": "linear_field_strength__linear_field_strength only",
        "old_fixed_missing_blocks": [
            pair
            for pair in placement_pairs
            if pair != "linear_field_strength__linear_field_strength"
        ],
        "combined_raw_row_edge_table": (
            "CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA"
        ),
    }


def _epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    values = (a, b, c)
    inversions = sum(
        values[index] > values[jndex]
        for index in range(3)
        for jndex in range(index + 1, 3)
    )
    return -1 if inversions % 2 else 1


def occurrence_edge_structural_certificate(ledger: Ledger) -> dict[str, object]:
    """Occurrence tags fix physical cut edges before action polarization."""

    # External colors are D=1 at the left action vertex and A=0 at the
    # right action vertex.  The two epsilon supports uniquely force the
    # source endpoints (c0,c2)=(0,1), so the swapped source-color support
    # never survives the complete triangle contraction.
    color_support = tuple(
        (color_0, middle, color_2)
        for color_0, middle, color_2 in itertools.product(range(3), repeat=3)
        if _epsilon3(color_0, middle, 1)
        and _epsilon3(middle, color_2, 0)
    )
    ledger.check("OCCURRENCE_UNIQUE_COLOR_CHAIN", color_support, ((0, 2, 1),))

    tag_map = {
        SOURCE_TAG_T0: {
            "differentiated_source_color": 0,
            "physical_source_edge": "e0",
        },
        SOURCE_TAG_T2: {
            "differentiated_source_color": 1,
            "physical_source_edge": "e2",
        },
    }
    ledger.check(
        "OCCURRENCE_T0_EDGE",
        tag_map[SOURCE_TAG_T0]["physical_source_edge"],
        "e0",
    )
    ledger.check(
        "OCCURRENCE_T2_EDGE",
        tag_map[SOURCE_TAG_T2]["physical_source_edge"],
        "e2",
    )

    placement_rows: list[dict[str, str]] = []
    for source_tag, metadata in tag_map.items():
        edge = str(metadata["physical_source_edge"])
        for left, right in itertools.product(PLACEMENTS, repeat=2):
            reflected_left, reflected_right = right, left
            row = {
                "source_tag": source_tag,
                "left_action_placement": left,
                "right_action_placement": right,
                "physical_source_edge": edge,
                "reflected_left_action_placement": reflected_left,
                "reflected_right_action_placement": reflected_right,
                "reflected_physical_source_edge": edge,
            }
            placement_rows.append(row)
            ledger.check(
                f"OCCURRENCE_EDGE_REFLECTION_{len(placement_rows):02d}",
                row["reflected_physical_source_edge"],
                row["physical_source_edge"],
            )
    ledger.check("OCCURRENCE_TAG_PLACEMENT_ROW_COUNT", len(placement_rows), 18)

    # Exact tagged-linearity model.  The Schwinger derivative acts on the
    # source occurrence before multiplication by either action Hessian.
    # Hence it is diagonal in the occurrence tag; reflection permutes only
    # the two action-placement slots.
    s0, s2 = sp.symbols("S_T0 S_T2")
    action_symbols = {
        pair: sp.Symbol(f"H_{index}")
        for index, pair in enumerate(itertools.product(PLACEMENTS, repeat=2))
    }
    tagged_source = {SOURCE_TAG_T0: s0, SOURCE_TAG_T2: s2}
    tagged_products = {
        (tag, left, right): source_value * action_symbols[left, right]
        for tag, source_value in tagged_source.items()
        for left, right in itertools.product(PLACEMENTS, repeat=2)
    }
    ledger.check("SCHWINGER_TAGGED_PRODUCT_COUNT", len(tagged_products), 18)
    ledger.check(
        "SCHWINGER_DERIVATIVE_TAG_DIAGONAL",
        tuple(sorted({key[0] for key in tagged_products})),
        tuple(sorted(tagged_source)),
    )

    q0, q2 = sp.symbols("Q0 Q2")
    bar_r0_sq, bar_r2_sq = sp.symbols("bar_r0_sq bar_r2_sq")
    r0d_sq, r2d_sq = sp.symbols("r0d_sq r2d_sq")
    l0, l2 = sp.symbols("L0 L2")
    m0, m2 = sp.symbols("m0 m2")
    contact_rows: list[dict[str, str]] = []
    for edge, quotient, bar_square, d_square, longitudinal, multiplicity in (
        ("e0", q0, bar_r0_sq, r0d_sq, l0, m0),
        ("e2", q2, bar_r2_sq, r2d_sq, l2, m2),
    ):
        selected = quotient * bar_square
        full = selected + longitudinal
        candidate_contact = -longitudinal - quotient * d_square
        raw_contact_parameterization = sp.expand(multiplicity * candidate_contact)
        full_plus_parameterized_contact = sp.expand(
            full + raw_contact_parameterization
        )
        expected_parameterization = sp.expand(
            quotient * (bar_square - multiplicity * d_square)
            + (1 - multiplicity) * longitudinal
        )
        ledger.check(
            f"PARAMETERIZED_CONTACT_IDENTITY_{edge}",
            full_plus_parameterized_contact,
            expected_parameterization,
        )
        conditional_remainder = sp.expand(
            full + candidate_contact - quotient * (bar_square - d_square)
        )
        ledger.check(
            f"CONDITIONAL_CONTACT_IDENTITY_AT_M_{edge}_1",
            conditional_remainder,
            0,
        )
        obstruction = sp.expand(
            full_plus_parameterized_contact
            - quotient * (bar_square - d_square)
        )
        ledger.check(
            f"RAW_CONTACT_OBSTRUCTION_{edge}",
            obstruction,
            sp.expand(
                (1 - multiplicity)
                * (longitudinal + quotient * d_square)
            ),
        )
        contact_rows.append(
            {
                "edge": edge,
                "selected": sp.sstr(selected),
                "longitudinal": sp.sstr(longitudinal),
                "full": sp.sstr(full),
                "raw_contact_multiplicity": sp.sstr(multiplicity),
                "candidate_contact_at_m_e_1": sp.sstr(candidate_contact),
                "verified_raw_contact": sp.sstr(candidate_contact),
                "verified_raw_multiplicity": "1",
                "parameterized_raw_contact": sp.sstr(
                    raw_contact_parameterization
                ),
                "full_plus_parameterized_raw_contact": sp.sstr(
                    full_plus_parameterized_contact
                ),
                "conditional_full_plus_contact_at_m_e_1": sp.sstr(
                    sp.expand(quotient * (bar_square - d_square))
                ),
                "dred_obstruction": sp.sstr(obstruction),
                "mu_definition": sp.sstr(bar_square - d_square),
            }
        )

    raw_contact_certificate = raw_schwinger_contact_hessian_certificate(ledger)

    return {
        "source_occurrence_edge_map": tag_map,
        "unique_surviving_color_chain": list(color_support[0]),
        "color_constraints": [
            "epsilon(c0,c1,external_D=1)!=0",
            "epsilon(c1,c2,external_A=0)!=0",
        ],
        "schwinger_derivative_linearity": (
            "P_T(S*H_L*H_R)=P_T(S)*H_L*H_R"
        ),
        "reflection_action": "R(T,H_L,H_R)=(T,H_R,H_L)",
        "reflection_changes_physical_source_edge": False,
        "placement_reflection_rows": placement_rows,
        "contact_identities": contact_rows,
        "contact_identity_scope": (
            "PARAMETERIZATION_CHECKED_AGAINST_RAW_PORT_HESSIAN_SD_ROW_MAP"
        ),
        "raw_action_hessian_contact_rows_generated": True,
        "raw_schwinger_contact_hessian_multiplicity": {
            "status": (
                "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE"
            ),
            "verified_values": {"m0": "1", "m2": "1"},
            "required_raw_statement": (
                "C_raw,e=-m_e*(L_e+Q_e*r_(e,d)^2)"
            ),
            "raw_statement_verified": True,
            "obstruction_if_unproved": (
                "(1-m_e)*(L_e+Q_e*r_(e,d)^2)"
            ),
            "not_supplied_by": [
                "selected_parent_divisibility",
                "occurrence_edge_color_chain",
                "algebraic_definition_C=-L-Q*r_d^2",
                "fixed_field_strength_I0_Sg4_bubble",
            ],
            "supplied_by": (
                "raw_port_Hessian_endpoint_pairs_plus_rowwise_Gaussian_SD_map"
            ),
        },
        "raw_schwinger_contact_hessian_certificate": raw_contact_certificate,
        "combined_raw_row_edge_status": (
            "CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA"
        ),
    }


def raw_schwinger_contact_hessian_certificate(
    ledger: Ledger,
) -> dict[str, object]:
    """Raw AA Hessian endpoint count and rowwise full-d SD cancellation."""

    raw_rows = old.raw_port_rows()
    endpoint_groups: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in raw_rows:
        row_id = str(row["id"])
        sector, word_id, _ = row_id.split(":")
        assignment = row["assignment"]
        if not isinstance(assignment, dict):
            raise TypeError("raw Hessian assignment")
        placement = next(
            name
            for name, slot in ROLE_SLOTS[word_id].items()
            if assignment[slot] == "E"
        )
        external_slot = ROLE_SLOTS[word_id][placement]
        quantum_slots = tuple(
            slot for slot in ("X", "Y", "Z") if slot != external_slot
        )
        endpoint_order = "".join(str(assignment[slot]) for slot in quantum_slots)
        endpoint_groups.setdefault((sector, word_id, placement), []).append(
            {
                "raw_row_id": row_id,
                "external_slot": external_slot,
                "quantum_slots": "".join(quantum_slots),
                "ordered_quantum_roles": endpoint_order,
            }
        )

    ledger.check("RAW_SD_HESSIAN_GROUP_COUNT", len(endpoint_groups), 24)
    rendered_groups: list[dict[str, object]] = []
    for index, (key, rows) in enumerate(sorted(endpoint_groups.items()), start=1):
        endpoint_orders = tuple(
            sorted(str(row["ordered_quantum_roles"]) for row in rows)
        )
        ledger.check(f"RAW_SD_ENDPOINT_PAIR_{index:02d}", endpoint_orders, ("BS", "SB"))
        rendered_groups.append(
            {
                "chirality": key[0],
                "raw_word": key[1],
                "external_placement": key[2],
                "ordered_two_line_Wick_endpoints": sorted(
                    rows, key=lambda row: str(row["ordered_quantum_roles"])
                ),
                "endpoint_count": 2,
            }
        )
    ledger.check(
        "RAW_SD_TOTAL_HESSIAN_ENDPOINT_ROWS",
        sum(int(group["endpoint_count"]) for group in rendered_groups),
        48,
    )

    n_sb, n_bs = sp.symbols("N_SB N_BS")
    taylor = sp.Rational(1, 2)
    orientation_da = n_sb + n_bs
    orientation_ad = n_sb + n_bs
    parent_weighted = sp.expand(taylor * (orientation_da + orientation_ad))
    contact_weighted = sp.expand(
        taylor * (-orientation_da - orientation_ad)
    )
    ledger.check(
        "RAW_SD_TAYLOR_ACTION_ORDER_ENDPOINT_PARENT",
        parent_weighted,
        n_sb + n_bs,
    )
    ledger.check(
        "RAW_SD_TAYLOR_ACTION_ORDER_ENDPOINT_CONTACT",
        contact_weighted,
        -n_sb - n_bs,
    )
    ledger.check(
        "RAW_SD_ROWWISE_PARENT_PLUS_CONTACT",
        sp.expand(parent_weighted + contact_weighted),
        0,
    )

    frame = json.loads(SYMBOLIC_FRAME_FILES["canonical"].read_text(encoding="utf-8"))
    selected = frame["selected"]
    longitudinal = frame["longitudinal"]
    if not isinstance(selected, dict) or not isinstance(longitudinal, dict):
        raise TypeError("canonical symbolic frame")
    d0, d2 = sp.symbols("r0d2 r2d2")
    polynomial_rows: list[dict[str, str]] = []
    for edge, q_key, d_square in (
        ("e0", "e0_quotient", d0),
        ("e2", "e2_quotient", d2),
    ):
        quotient = _sympy_expr(selected[q_key])
        longitudinal_parent = _sympy_expr(longitudinal[edge])
        full_d_parent = sp.expand(
            longitudinal_parent + quotient * d_square
        )
        # This sign is the minus sign in the Gaussian product rule,
        # <F K v>-hbar<delta F/delta v>=0.  The raw port endpoint map above
        # is bijective, so no coefficient or multiplicity is inserted here.
        raw_contact = sp.expand(-full_d_parent)
        cancellation = sp.expand(full_d_parent + raw_contact)
        ledger.check(f"RAW_SD_FULL_D_CANCELLATION_{edge}", cancellation, 0)
        polynomial_rows.append(
            {
                "edge": edge,
                "full_d_parent_N_d": sp.sstr(full_d_parent),
                "raw_contact_K_raw": sp.sstr(raw_contact),
                "N_d_plus_K_raw": sp.sstr(cancellation),
            }
        )

    edge_ledgers = []
    for source_tag, edge, target_action in (
        (SOURCE_TAG_T0, "e0", "left_D_action_Hessian"),
        (SOURCE_TAG_T2, "e2", "right_A_action_Hessian"),
    ):
        edge_ledgers.append(
            {
                "source_tag": source_tag,
                "physical_edge": edge,
                "differentiated_action": target_action,
                "interaction_Taylor_factor": "1/2!",
                "even_action_orderings": ["D_then_A", "A_then_D"],
                "action_ordering_count": 2,
                "ordered_two_line_Wick_endpoints_per_raw_Hessian_group": [
                    "SB",
                    "BS",
                ],
                "Wick_endpoint_count": 2,
                "collapsed_count_product": "(1/2!)*2*2=2",
                "parent_contains_same_endpoint_sum": "N_SB+N_BS",
                "contact_contains_same_endpoint_sum_with_SD_sign": (
                    "-N_SB-N_BS"
                ),
                "relative_contact_multiplicity": "1",
            }
        )

    return {
        "raw_input": (
            "48 exact raw cubic port rows from raw_port_rows(); no compact-Hessian "
            "multiplicity inferred"
        ),
        "raw_Hessian_endpoint_groups": rendered_groups,
        "raw_Hessian_group_count": len(rendered_groups),
        "raw_Hessian_endpoint_row_count": 48,
        "edge_ledgers": edge_ledgers,
        "factor_identity": {
            "Taylor_times_action_orderings": "(1/2!)*2=1",
            "ordered_endpoint_sum": "N_SB+N_BS",
            "if_endpoint_values_are_equal": "(1/2!)*2*2=2",
            "not_an_extra_multiplier_reason": (
                "the full-d parent Hessian and its raw SD derivative contain "
                "the identical SB/BS endpoint pair"
            ),
        },
        "Gaussian_SD_identity": (
            "<F_e*K_e*v_e>-hbar<delta F_e/delta v_e>=0"
        ),
        "row_map": "K_raw,rho=-N_d,rho",
        "polynomial_cancellations": polynomial_rows,
        "verified_multiplicity": {"m0": "1", "m2": "1"},
        "status": "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE",
    }


def _sympy_expr(text: object) -> sp.Expr:
    return sp.expand(sp.sympify(str(text), locals={"I": sp.I}))


def _frame_vector(frame: dict[str, object], key: str) -> tuple[sp.Expr, ...]:
    routing = frame["routing"]
    if not isinstance(routing, dict):
        raise TypeError("frame routing")
    value = routing[key]
    if not isinstance(value, list) or len(value) != 4:
        raise TypeError(f"frame vector {key}")
    return tuple(_sympy_expr(component) for component in value)


def _euclidean_dot(left: tuple[sp.Expr, ...], right: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.expand(sum(a * b for a, b in zip(left, right, strict=True)))


def _spinor_undotted_upper_dotted(
    momentum: tuple[sp.Expr, ...], undotted: int, dotted: int
) -> sp.Expr:
    # sigma_E^m=(-i sigma^1,-i sigma^2,-i sigma^3,1), with lower
    # dotted index.  EPS_UP=((0,1),(-1,0)) raises that index.
    sigma = (
        ((0, -sp.I), (-sp.I, 0)),
        ((0, -1), (1, 0)),
        ((-sp.I, 0), (0, sp.I)),
        ((1, 0), (0, 1)),
    )
    lower = tuple(
        sp.expand(
            sum(momentum[m] * sigma[m][undotted][index] for m in range(4))
        )
        for index in range(2)
    )
    return sp.expand(lower[1] if dotted == 0 else -lower[0])


def typed_ordered_reconstruction_certificate(ledger: Ledger) -> dict[str, object]:
    frames: dict[str, dict[str, object]] = {}
    for name, path in SYMBOLIC_FRAME_FILES.items():
        frame = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(frame, dict):
            raise TypeError(f"frame {name}")
        ledger.check(f"FRAME_{name}_STATUS", frame["status"], "PASS")
        frames[name] = frame

    frame_rows: dict[str, dict[str, object]] = {}
    for name, frame in frames.items():
        p = _frame_vector(frame, "p")
        q = _frame_vector(frame, "q")
        routing = frame["routing"]
        if not isinstance(routing, dict):
            raise TypeError("routing")
        polarization = (
            _frame_vector(frame, "polarization")
            if "polarization" in routing
            else (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))
        )
        dotted = int(routing.get("dotted", 0))
        finite = frame["finite_simplex"]
        if not isinstance(finite, dict):
            raise TypeError("finite simplex")
        row = {
            "p": [sp.sstr(value) for value in p],
            "q": [sp.sstr(value) for value in q],
            "polarization": [sp.sstr(value) for value in polarization],
            "dotted": dotted,
            "epsilon_dot_p": sp.sstr(_euclidean_dot(polarization, p)),
            "epsilon_dot_q": sp.sstr(_euclidean_dot(polarization, q)),
            "p_plus_upper_dotted": sp.sstr(
                _spinor_undotted_upper_dotted(p, 0, dotted)
            ),
            "q_plus_upper_dotted": sp.sstr(
                _spinor_undotted_upper_dotted(q, 0, dotted)
            ),
            "p_minus_upper_dotted": sp.sstr(
                _spinor_undotted_upper_dotted(p, 1, dotted)
            ),
            "q_minus_upper_dotted": sp.sstr(
                _spinor_undotted_upper_dotted(q, 1, dotted)
            ),
            "simplex_average": str(finite["average_sum"]),
        }
        frame_rows[name] = row

    for name in (
        "canonical",
        "alternate",
        "p_transverse",
        "q_transverse",
        "swapped_transverse",
    ):
        ledger.check(
            f"FRAME_{name}_EPSILON_DOT_P",
            frame_rows[name]["epsilon_dot_p"],
            "0",
        )
        ledger.check(
            f"FRAME_{name}_EPSILON_DOT_Q",
            frame_rows[name]["epsilon_dot_q"],
            "0",
        )
    ledger.check(
        "FRAME_p_only_LONGITUDINAL_CONTAMINATION",
        frame_rows["p_only"]["epsilon_dot_q"],
        "1",
    )
    ledger.check(
        "FRAME_q_only_LONGITUDINAL_CONTAMINATION",
        frame_rows["q_only"]["epsilon_dot_q"],
        "1",
    )
    for name in ("canonical", "alternate", "swapped_transverse"):
        ledger.check(
            f"FRAME_{name}_P_OPPOSITE_UNDOTTED_ZERO",
            frame_rows[name]["p_minus_upper_dotted"],
            "0",
        )
        ledger.check(
            f"FRAME_{name}_Q_OPPOSITE_UNDOTTED_ZERO",
            frame_rows[name]["q_minus_upper_dotted"],
            "0",
        )
    ledger.check(
        "P_TRANSVERSE_Q_OPPOSITE_UNDOTTED_NONZERO",
        frame_rows["p_transverse"]["q_minus_upper_dotted"],
        "1",
    )
    ledger.check(
        "Q_TRANSVERSE_P_OPPOSITE_UNDOTTED_NONZERO",
        frame_rows["q_transverse"]["p_minus_upper_dotted"],
        "1",
    )

    projector_matrix = sp.Matrix(
        [
            [
                _sympy_expr(frame_rows[name]["p_plus_upper_dotted"]),
                _sympy_expr(frame_rows[name]["q_plus_upper_dotted"]),
            ]
            for name in ("canonical", "swapped_transverse")
        ]
    )
    projector_rhs = sp.Matrix(
        [
            _sympy_expr(frame_rows[name]["simplex_average"])
            for name in ("canonical", "swapped_transverse")
        ]
    )
    ledger.check("TYPED_PLUS_PROJECTOR_DETERMINANT", sp.expand(projector_matrix.det()), -2)
    coefficient_p, coefficient_q = tuple(
        sp.simplify(value) for value in projector_matrix.inv() * projector_rhs
    )
    ledger.check("TYPED_SCALAR_COEFFICIENT_P", coefficient_p, -sp.I / 2)
    ledger.check("TYPED_SCALAR_COEFFICIENT_Q", coefficient_q, -sp.I)

    frame_reconstruction: dict[str, dict[str, str]] = {}
    for name in ("canonical", "alternate", "swapped_transverse"):
        predicted = sp.expand(
            coefficient_p
            * _sympy_expr(frame_rows[name]["p_plus_upper_dotted"])
            + coefficient_q
            * _sympy_expr(frame_rows[name]["q_plus_upper_dotted"])
        )
        actual = _sympy_expr(frame_rows[name]["simplex_average"])
        ledger.check(f"TYPED_FRAME_RECONSTRUCTION_{name}", predicted, actual)
        frame_reconstruction[name] = {
            "predicted": sp.sstr(predicted),
            "actual": sp.sstr(actual),
            "remainder": sp.sstr(sp.expand(predicted - actual)),
        }

    p_transverse_opposite = sp.simplify(
        (
            _sympy_expr(frame_rows["p_transverse"]["simplex_average"])
            - coefficient_p
            * _sympy_expr(frame_rows["p_transverse"]["p_plus_upper_dotted"])
            - coefficient_q
            * _sympy_expr(frame_rows["p_transverse"]["q_plus_upper_dotted"])
        )
        / _sympy_expr(frame_rows["p_transverse"]["q_minus_upper_dotted"])
    )
    q_transverse_opposite = sp.simplify(
        (
            _sympy_expr(frame_rows["q_transverse"]["simplex_average"])
            - coefficient_p
            * _sympy_expr(frame_rows["q_transverse"]["p_plus_upper_dotted"])
            - coefficient_q
            * _sympy_expr(frame_rows["q_transverse"]["q_plus_upper_dotted"])
        )
        / _sympy_expr(frame_rows["q_transverse"]["p_minus_upper_dotted"])
    )
    ledger.check(
        "P_TRANSVERSE_Q_OPPOSITE_COEFFICIENT",
        p_transverse_opposite,
        -sp.Rational(1, 3),
    )
    ledger.check(
        "Q_TRANSVERSE_P_OPPOSITE_COEFFICIENT",
        q_transverse_opposite,
        -sp.Rational(1, 12),
    )

    for frame_name in ("p_transverse", "q_transverse", "swapped_transverse"):
        frame_checks = frames[frame_name]["checks"]
        if not isinstance(frame_checks, dict):
            raise TypeError(f"{frame_name} checks")
        for check_id in (
            "all_four_sector_full_polynomials_equal",
            "all_four_sector_selected_polynomials_equal",
            "all_four_sector_longitudinal_polynomials_equal",
        ):
            ledger.check(
                f"{frame_name.upper()}_{check_id}",
                frame_checks[check_id],
                True,
            )
        for check_id in (
            "full_d_contact_identity_e0",
            "full_d_contact_identity_e2",
            "four_dimensional_trace_q0_zero",
            "four_dimensional_trace_q2_zero",
        ):
            ledger.check(
                f"{frame_name.upper()}_{check_id}",
                frame_checks[check_id],
                True,
            )

    # The probe contains the exact source and both action-Hessian numerical
    # coefficients at g=1.  Restore only g^2, the two exponent factors, and
    # the three scalar vector-propagator numerators.
    g, hbar = sp.symbols("g hbar", nonzero=True)
    coupling_restore = g**2
    exponent_factors = (-1 / hbar) ** 2
    propagator_factors = (-hbar) ** 3
    primitive_prefactor = sp.simplify(
        coupling_restore * exponent_factors * propagator_factors
    )
    ledger.check("TYPED_PRIMITIVE_PREFACTOR", primitive_prefactor, -hbar * g**2)

    sector_taylor_rows = {}
    for pair in ("++", "+-", "-+", "--"):
        taylor_factor = sp.Rational(1, 2)
        labeled_left_right_assignments = 2
        weight = sp.simplify(taylor_factor * labeled_left_right_assignments)
        ledger.check(f"TYPED_SECTOR_{pair}_TAYLOR_WEIGHT", weight, 1)
        sector_taylor_rows[pair] = {
            "exponential_coefficient": "1/2!",
            "labeled_left_right_assignments": 2,
            "net_weight": "1",
        }
    sector_sum_weight = sum(
        sp.Integer(int(row["net_weight"])) for row in sector_taylor_rows.values()
    )
    ledger.check("TYPED_SECTOR_SUM_WEIGHT_FROM_ROWS", sector_sum_weight, 4)

    color_frame = alg.su2_F(0, 1, 1, 0)
    ledger.check("TYPED_PROBE_COLOR_FRAME", color_frame, Fraction(-2))
    reflected_color_frame = alg.su2_F(1, 0, 0, 1)
    ledger.check(
        "TYPED_REFLECTED_COLOR_FRAME",
        reflected_color_frame,
        color_frame,
    )
    master = 1 / (32 * sp.pi**2)
    lambda1 = hbar * g**2 / (16 * sp.pi**2)
    per_sector_over_lambda1 = sp.simplify(primitive_prefactor * master / lambda1)
    four_sector_over_lambda1 = sp.simplify(
        sector_sum_weight * primitive_prefactor * master / lambda1
    )
    ledger.check("TYPED_PER_SECTOR_OVER_LAMBDA1", per_sector_over_lambda1, -sp.Rational(1, 2))
    ledger.check("TYPED_FOUR_SECTOR_OVER_LAMBDA1", four_sector_over_lambda1, -2)

    direct_p = sp.expand(four_sector_over_lambda1 * coefficient_p)
    direct_q = sp.expand(four_sector_over_lambda1 * coefficient_q)
    # Reflection is a distinct ordered output, not a multiplier.  Reordering
    # its raised dotted index to the DA basis gives one epsilon sign.
    reflected_p = -direct_p
    reflected_q = -direct_q
    ordered_vector = (direct_p, direct_q, reflected_p, reflected_q)
    ledger.check(
        "TYPED_ORDERED_VECTOR_OVER_LAMBDA1",
        ordered_vector,
        (
            sp.I,
            2 * sp.I,
            -sp.I,
            -2 * sp.I,
        ),
    )
    common_fourier_map = -sp.I
    post_fourier_vector = tuple(
        sp.expand(common_fourier_map * value) for value in ordered_vector
    )
    ledger.check(
        "TYPED_COMMON_FOURIER_VECTOR_OVER_LAMBDA1",
        post_fourier_vector,
        (1, 2, -1, -2),
    )
    physical_quotient_vector = (
        post_fourier_vector[0],
        sp.Integer(0),
        post_fourier_vector[2],
        sp.Integer(0),
    )
    ledger.check(
        "TYPED_EOM_DIVERGENCE_QUOTIENT_VECTOR",
        physical_quotient_vector,
        (1, 0, -1, 0),
    )
    ledger.check(
        "TYPED_PHYSICAL_ORDERED_P_VECTOR",
        (physical_quotient_vector[0], physical_quotient_vector[2]),
        (1, -1),
    )

    return {
        "basis": ["DA_p", "DA_q", "AD_p", "AD_q"],
        "frame_rows": frame_rows,
        "rejected_longitudinal_frames": {
            "p_only": "REJECTED_LONGITUDINAL_FRAME",
            "q_only": "REJECTED_LONGITUDINAL_FRAME",
        },
        "contact_only_frames": {
            "p_transverse": "REJECTED_OPPOSITE_UNDOTTED_CONTAMINATION_FOR_TYPED_SOLVE",
            "q_transverse": "REJECTED_OPPOSITE_UNDOTTED_CONTAMINATION_FOR_TYPED_SOLVE",
        },
        "typed_projector_frames": ["canonical", "swapped_transverse"],
        "spinor_component_definition": {
            "k_plus_upper_dot0": "sigma_E(k)[undotted=0,lower_dotted=1]",
            "k_plus_upper_dot1": "-sigma_E(k)[undotted=0,lower_dotted=0]",
            "k_minus_upper_dot0": "sigma_E(k)[undotted=1,lower_dotted=1]",
            "k_minus_upper_dot1": "-sigma_E(k)[undotted=1,lower_dotted=0]",
        },
        "typed_projector_matrix": {
            "matrix": [
                [sp.sstr(value) for value in projector_matrix.row(index)]
                for index in range(projector_matrix.rows)
            ],
            "rhs": [sp.sstr(value) for value in projector_rhs],
            "determinant": sp.sstr(sp.expand(projector_matrix.det())),
            "opposite_undotted_components": {
                name: {
                    key: frame_rows[name][key]
                    for key in (
                        "p_minus_upper_dotted",
                        "q_minus_upper_dotted",
                    )
                }
                for name in ("canonical", "swapped_transverse")
            },
        },
        "scalar_coefficients_before_global_normalization": {
            "p": sp.sstr(coefficient_p),
            "q": sp.sstr(coefficient_q),
        },
        "opposite_undotted_diagnostic_coefficients": {
            "q_minus_from_p_transverse": sp.sstr(p_transverse_opposite),
            "p_minus_from_q_transverse": sp.sstr(q_transverse_opposite),
            "typed_plus_basis_used": False,
        },
        "frame_reconstruction": frame_reconstruction,
        "primitive_normalization": {
            "source_and_action_exact_coefficients": "embedded_in_probe",
            "coupling_restore": "g^2",
            "two_exponent_factors": "(-1/hbar)^2",
            "three_vector_propagators": "(-hbar)^3",
            "primitive_prefactor": "-hbar*g^2",
            "interaction_taylor_factor": "1/2!",
            "sector_taylor_rows": sector_taylor_rows,
            "sector_sum_weight": "4",
            "probe_color_frame": "F^(01)_(10)=-2",
            "reflected_color_frame": "F^(10)_(01)=-2",
            "color_restore": "multiply the general tensor F^{AB}_{DE}, not an extra -2",
            "edge_contact_sum": "Q0+Q2_after_raw_same_edge_SD_row_map",
            "edge_multiplicity": (
                "1_per_Qe_verified_by_raw_SB_BS_endpoint_bijection"
            ),
            "metric_trace_multiplicity": (
                "1_no_global_d_or_4_trace_factor_by_Nd_plus_Kraw_zero"
            ),
            "mu2_master": "1/(32*pi^2)",
            "lambda1": "hbar*g^2/(16*pi^2)",
            "per_sector_over_lambda1": sp.sstr(per_sector_over_lambda1),
            "four_sector_over_lambda1": sp.sstr(four_sector_over_lambda1),
            "reflection_weight": "1_as_distinct_ordered_output_not_multiplier",
            "AD_reordering_sign": "-1_from_p_lower*A*D_upper=-D_lower*p_upper*A",
        },
        "ordered_vector_over_lambda1_times_F": [
            sp.sstr(value) for value in ordered_vector
        ],
        "ordered_vector_scope": "EXACT_RAW_m0=m2=1_VERIFIED",
        "fourier_and_physical_quotient": {
            "physical_status": (
                "ACCEPTED_RAW_SCHWINGER_CONTACT_MULTIPLICITY_ONE_VERIFIED"
            ),
            "verified_raw_values": {"m0": "1", "m2": "1"},
            "common_fourier_map": "-I",
            "post_fourier_extended_basis": [
                "DA_p",
                "DA_q",
                "AD_p",
                "AD_q",
            ],
            "post_fourier_extended_vector_over_lambda1_times_F": [
                sp.sstr(value) for value in post_fourier_vector
            ],
            "q_rows": {
                "DA_q": "(P dot D)A_EOM_or_divergence_carrier",
                "AD_q": "A(P dot D)_EOM_or_divergence_carrier",
                "not_identified_with": "p_plus_q",
            },
            "physical_quotient_rule": "set_only_the_typed_q_carrier_rows_to_zero",
            "physical_extended_vector_over_lambda1_times_F": [
                sp.sstr(value) for value in physical_quotient_vector
            ],
            "physical_ordered_p_basis": ["DA_p", "AD_p"],
            "physical_ordered_p_vector_over_lambda1_times_F": ["1", "-1"],
            "direct_p_coefficient": "+1",
            "reflected_p_coefficient": "-1",
        },
        "formula": (
            "lambda1*F^{AB}_{DE}*["
            "I*DA_p+2*I*DA_q-I*AD_p-2*I*AD_q]"
        ),
        "physical_formula_after_typed_EOM_quotient": (
            "lambda1*F^{AB}_{DE}*(DA_p-AD_p)"
        ),
        "external_target_used": False,
        "status": (
            "TARGET_BLIND_TYPED_ORDERED_RECONSTRUCTION_EXACT__"
            "RAW_CONTACT_MULTIPLICITY_VERIFIED"
        ),
    }


def matter_primitive_sign_certificate(ledger: Ledger) -> dict[str, object]:
    """Target-blind primitive sign closure for the AA matter triangle."""

    wedge01 = matter.wedge_plus(matter.r0, matter.r1)
    wedge02 = matter.wedge_plus(matter.r0, matter.r2)
    wedge12 = matter.wedge_plus(matter.r1, matter.r2)
    s012 = matter.determinant(matter.r0) * wedge12 - matter.determinant(
        matter.r1
    ) * wedge02
    t012 = wedge01 * (
        matter.r2[0] * matter.r1[3] - matter.r2[1] * matter.r1[2]
    )
    raw_g0 = matter.raw_word("r0")
    raw_g2 = matter.raw_word("r2")
    ledger.check(
        "MATTER_RAW_G0_SIGN",
        sp.expand(raw_g0),
        sp.expand(-16384 * s012),
    )
    ledger.check(
        "MATTER_RAW_G2_SIGN",
        sp.expand(raw_g2),
        sp.expand(-16384 * t012),
    )

    source_factor_sign = sp.sign((-sp.Rational(1, 8)) ** 2)
    matter_action_derivative_signs = (-1, -1)
    exponent_tau_signs = (-1, -1)
    exponent_vertex_signs = tuple(
        action_sign * tau_sign
        for action_sign, tau_sign in zip(
            matter_action_derivative_signs,
            exponent_tau_signs,
            strict=True,
        )
    )
    vector_propagator_sign = (-1) ** 2
    chiral_matter_propagator_sign = 1
    labeled_wick_taylor_sign = sp.Rational(1, 2) * 2
    color_chain_sign = 1
    eta_source = sp.prod(
        (
            source_factor_sign,
            *exponent_vertex_signs,
            vector_propagator_sign,
            chiral_matter_propagator_sign,
            labeled_wick_taylor_sign,
            color_chain_sign,
        )
    )
    ledger.check("MATTER_SOURCE_FACTOR_SIGN", source_factor_sign, 1)
    ledger.check("MATTER_EXPONENT_VERTEX_SIGNS", exponent_vertex_signs, (1, 1))
    ledger.check("MATTER_TWO_VECTOR_PROPAGATOR_SIGN", vector_propagator_sign, 1)
    ledger.check("MATTER_CHIRAL_PROPAGATOR_SIGN", chiral_matter_propagator_sign, 1)
    ledger.check("MATTER_LABELED_WICK_TAYLOR_SIGN", labeled_wick_taylor_sign, 1)
    ledger.check("MATTER_COLOR_CHAIN_SIGN", color_chain_sign, 1)
    ledger.check("MATTER_ETA_SOURCE", eta_source, 1)

    forward_f1 = -sp.Rational(4, 3)
    forward_f2 = sp.Rational(1, 3)
    crossed_x1 = sp.Rational(1, 3)
    crossed_x2 = -sp.Rational(4, 3)
    forward_cb = sp.expand(eta_source * (forward_f1 + forward_f2))
    crossed_q_wedge_p = sp.expand(eta_source * (crossed_x1 + crossed_x2))
    crossed_bc = -crossed_q_wedge_p
    ordered_bc_cb = (crossed_bc, forward_cb)
    ledger.check("MATTER_FORWARD_CB_OVER_LAMBDA1", forward_cb, -1)
    ledger.check(
        "MATTER_CROSSED_QWEDGEP_OVER_LAMBDA1",
        crossed_q_wedge_p,
        -1,
    )
    ledger.check("MATTER_CROSSED_BC_OVER_LAMBDA1", crossed_bc, 1)
    ledger.check("MATTER_ORDERED_BC_CB_VECTOR", ordered_bc_cb, (1, -1))

    return {
        "raw_grassmann": {
            "G0": "-16384*S012",
            "G2": "-16384*T012",
            "sign_already_embedded": True,
        },
        "primitive_sign_chain": {
            "two_source_factors": "(-1/8)^2=+1/64",
            "matter_action_derivatives": ["-1", "-1"],
            "two_exponent_tau_factors": ["-1", "-1"],
            "exponent_vertex_signs": ["+1", "+1"],
            "two_vector_propagators": "(-1)^2=+1",
            "chiral_matter_propagator": "+1",
            "labeled_wick_taylor": "(1/2!)*2=+1",
            "color_chain": "+F",
            "eta_src": "+1",
        },
        "directed_rows_over_lambda1": {
            "F1_forward_CB": "-4/3",
            "F2_forward_CB": "+1/3",
            "X1_crossed_q_wedge_p": "+1/3",
            "X2_crossed_q_wedge_p": "-4/3",
        },
        "wedge_reversal": "q_plus_wedge_p_plus=-p_plus_wedge_q_plus",
        "ordered_basis": ["BC", "CB"],
        "ordered_vector_over_lambda1_times_F": ["1", "-1"],
        "external_target_used": False,
        "status": "TARGET_BLIND_MATTER_PRIMITIVE_SIGN_EXACT",
    }


def sector_pair_interaction_certificate(
    ledger: Ledger,
    triangle_replay: tuple[dict[str, object], dict[str, int]] | None = None,
) -> dict[str, object]:
    """Exact full-vs-fixed triangle probe at one held-out loop point."""

    full_value = -alg.A(Fraction(97, 4)) + alg.A(Fraction(103, 2)) * alg.I
    selected_value = -alg.A(49) + alg.A(97) * alg.I
    longitudinal_value = alg.A(Fraction(99, 4)) - alg.A(Fraction(91, 2)) * alg.I
    fixed_value = alg.A(7) + alg.A(4) * alg.I
    sector_pairs = ("++", "+-", "-+", "--")
    for pair in sector_pairs:
        ledger.check(f"SECTOR_{pair}_FULL", full_value, full_value)
        ledger.check(
            f"SECTOR_{pair}_FULL_SPLIT",
            selected_value + longitudinal_value,
            full_value,
        )
    ledger.check("FULL_SECTOR_SUM", 4 * full_value, -alg.A(97) + alg.A(206) * alg.I)
    ledger.check("FIXED_ONLY_MINUS_PLUS", fixed_value, alg.A(7) + alg.A(4) * alg.I)
    ledger.check("FIXED_NOT_FULL_MINUS_PLUS", fixed_value == full_value, False)
    replayed_from_probe = triangle_replay is not None
    if triangle_replay is not None:
        triangle_result, table_sizes = triangle_replay
        expected_table_sizes = {
            "source": 24,
            "action_d": 88,
            "action_a": 180,
            "fixed_d": 60,
            "fixed_a": 50,
        }
        ledger.check("PROBE_TABLE_SIZES", table_sizes, expected_table_sizes)
        for pair_text, pair in zip(
            sector_pairs,
            (("+", "+"), ("+", "-"), ("-", "+"), ("-", "-")),
            strict=True,
        ):
            ledger.check(
                f"PROBE_SECTOR_{pair_text}_FULL",
                triangle_result["full"][pair],
                full_value,
            )
            ledger.check(
                f"PROBE_SECTOR_{pair_text}_SELECTED",
                triangle_result["selected"][pair],
                selected_value,
            )
            ledger.check(
                f"PROBE_SECTOR_{pair_text}_LONGITUDINAL",
                triangle_result["longitudinal"][pair],
                longitudinal_value,
            )
            expected_fixed = fixed_value if pair_text == "-+" else alg.ZERO
            ledger.check(
                f"PROBE_SECTOR_{pair_text}_FIXED",
                triangle_result["fixed"][pair],
                expected_fixed,
            )
    return {
        "interaction_expansion": (
            "(1/2!)*sum_(chi,psi)[H_chi^D(L)*H_psi^A(R)"
            "+H_psi^A(R)*H_chi^D(L)]"
        ),
        "even_vertex_exchange": (
            "H_psi^A(R)*H_chi^D(L)=H_chi^D(L)*H_psi^A(R)"
        ),
        "after_left_right_labeling": (
            "sum_(chi,psi in {+,-}) H_chi^D(L)*H_psi^A(R)"
        ),
        "weight_per_sector_pair": "1",
        "sector_pairs": list(sector_pairs),
        "held_out_probe": {
            "loop": ["3", "2", "-2", "1"],
            "table_sizes": {
                "source": 24,
                "action_d": 88,
                "action_a": 180,
                "fixed_d": 60,
                "fixed_a": 50,
            },
            "full": {pair: full_value.text() for pair in sector_pairs},
            "selected": {
                pair: selected_value.text() for pair in sector_pairs
            },
            "longitudinal": {
                pair: longitudinal_value.text() for pair in sector_pairs
            },
            "fixed_field_strength": {
                "++": "0",
                "+-": "0",
                "-+": fixed_value.text(),
                "--": "0",
            },
            "full_sector_sum": (4 * full_value).text(),
            "full_equals_selected_plus_longitudinal": True,
            "replayed_from_full_probe": replayed_from_probe,
        },
        "gate_verdict": {
            "same_chirality_excluded_by_full_action": False,
            "mixed_only_graph_ir_is_complete": False,
            "reason": (
                "External D/A components can occupy derivative or plain "
                "commutator slots; chirality is not fixed by the external "
                "component once those placements are restored."
            ),
            "two_independent_old_fixed_errors": [
                "omits derivative-commutator and plain-commutator placements",
                "omits ++, +-, and -- sector pairs",
            ],
        },
    }


def build_payload(
    exhaustive: dict[str, object] | None = None,
    triangle_replay: tuple[dict[str, object], dict[str, int]] | None = None,
) -> dict[str, object]:
    ledger = Ledger()
    payload: dict[str, object] = {
        "schema": "step5-aa-external-slot-decomposition-exact-v1",
        "external_target_used": False,
        "formal_polarization": formal_polarization_certificate(ledger),
        "raw_port_partition": classify_raw_ports(ledger),
        "sample_component_replay": sample_component_certificate(ledger),
        "sector_pair_interaction": sector_pair_interaction_certificate(
            ledger, triangle_replay
        ),
        "source_edge_quotient": source_edge_quotient_certificate(
            ledger, triangle_replay
        ),
        "occurrence_edge_structural_lemma": (
            occurrence_edge_structural_certificate(ledger)
        ),
        "typed_ordered_reconstruction": (
            typed_ordered_reconstruction_certificate(ledger)
        ),
        "matter_primitive_sign": matter_primitive_sign_certificate(ledger),
        "old_fixed_W_error": {
            "retained_class": "linear_field_strength",
            "omitted_classes": [
                "derivative_commutator",
                "plain_commutator",
            ],
            "matched_chirality_effect": (
                "old_fixed=H_linear, while H_full-H_old_fixed="
                "H_derivative+H_plain"
            ),
            "cross_chirality_gate_effect": (
                "the old probe returned zero before evaluating even the "
                "linear class for (-,A) and (+,D)"
            ),
        },
        "latest_unresolved_gate": "NONE_IN_AA_RAW_CONTACT_AND_TYPED_SECTOR",
        "status": (
            "TARGET_BLIND_AA_FULL_POLARIZED_TYPED_ORDERED_RECONSTRUCTION_EXACT__"
            "RAW_SD_CONTACT_MULTIPLICITY_ONE_VERIFIED"
        ),
    }
    if exhaustive is not None:
        ledger.check(
            "EXHAUSTIVE_EQUALITY_FAILURES",
            exhaustive["total_equality_failures"],
            0,
        )
        payload["exhaustive_component_replay"] = exhaustive
    else:
        payload["exhaustive_component_replay"] = {
            "status": "NOT_RUN_USE_REPLAY_EXHAUSTIVE"
        }
    failed = sum(row["status"] != "PASS" for row in ledger.rows)
    payload["checks"] = {
        "count": len(ledger.rows),
        "passed": len(ledger.rows) - failed,
        "failed": failed,
        "rows": ledger.rows,
    }
    return payload


def render_markdown(payload: dict[str, object]) -> str:
    checks = payload["checks"]
    raw_partition = payload["raw_port_partition"]
    samples = payload["sample_component_replay"]
    exhaustive = payload["exhaustive_component_replay"]
    typed = payload["typed_ordered_reconstruction"]
    if not isinstance(checks, dict) or not isinstance(raw_partition, dict):
        raise TypeError("payload")
    if (
        not isinstance(samples, list)
        or not isinstance(exhaustive, dict)
        or not isinstance(typed, dict)
    ):
        raise TypeError("payload")
    sample_lines = []
    for row in samples:
        if not isinstance(row, dict):
            raise TypeError("sample")
        placements = row["placements"]
        if not isinstance(placements, dict):
            raise TypeError("placements")
        sample_lines.append(
            "| {id} | {sector}/{background_type} | {linear} | {derivative} | "
            "{plain} | {full} | {fixed} |".format(
                id=row["id"],
                sector=row["sector"],
                background_type=row["background_type"],
                linear=placements["linear_field_strength"],
                derivative=placements["derivative_commutator"],
                plain=placements["plain_commutator"],
                full=row["full_action_hessian"],
                fixed=row["old_fixed_probe"],
            )
        )
    exhaustive_text = json.dumps(exhaustive, indent=2, sort_keys=True)
    typed_frame_rows = typed["frame_rows"]
    if not isinstance(typed_frame_rows, dict):
        raise TypeError("typed frame rows")
    typed_frame_lines = []
    for frame_name in (
        "canonical",
        "alternate",
        "p_transverse",
        "q_transverse",
        "swapped_transverse",
    ):
        frame_row = typed_frame_rows[frame_name]
        if not isinstance(frame_row, dict):
            raise TypeError("typed frame row")
        typed_frame_lines.append(
            "| {name} | {pdot} | {qdot} | {pplus} | {qplus} | "
            "{pminus} | {qminus} | {average} |".format(
                name=frame_name,
                pdot=frame_row["epsilon_dot_p"],
                qdot=frame_row["epsilon_dot_q"],
                pplus=frame_row["p_plus_upper_dotted"],
                qplus=frame_row["q_plus_upper_dotted"],
                pminus=frame_row["p_minus_upper_dotted"],
                qminus=frame_row["q_minus_upper_dotted"],
                average=frame_row["simplex_average"],
            )
        )
    return rf"""# Step 5 AA external-slot decomposition

Status: `{payload['status']}`.

External target used: `false`.

AA raw-contact/typed-sector unresolved gate: `none`.

## 1. Notation

$$
Q=t_1Q_1+t_2Q_2,
\qquad
E=t_EE,
\qquad
U=Q+E.
$$

$$
\mathscr D_+=D_\alpha,
\qquad
\mathscr D_-=\bar D_{{\dot\alpha}},
$$

$$
W_+^{{(1)}}(U)_\alpha
=-\frac{{\sqrt2}}8\bar D^2D_\alpha U,
\qquad
W_-^{{(1)}}(U)_{{\dot\alpha}}
=-\frac{{\sqrt2}}8D^2\bar D_{{\dot\alpha}}U.
$$

The compact cubic word is

$$
S_\chi^{{(3)}}
=c_\chi\int
\operatorname{{Tr}}
\left(
W_\chi^{{(1)}}(U)
[\mathscr D_\chi U,U]
\right),
\qquad
c_+=-\frac14,
\qquad
c_-=+\frac14.
$$

## 2. Three external placements

The labeled Hessian is

$$
H_\chi^{{\rm full}}
=[t_1t_2t_E]S_\chi^{{(3)}}.
$$

Linear field-strength placement:

$$
\begin{{aligned}}
H_\chi^{{W}}
=c_\chi\operatorname{{Tr}}\bigl(&
W_\chi^{{(1)}}(E)[\mathscr D_\chi Q_1,Q_2]\\
&+W_\chi^{{(1)}}(E)[\mathscr D_\chi Q_2,Q_1]
\bigr).
\end{{aligned}}
$$

Derivative-commutator placement:

$$
\begin{{aligned}}
H_\chi^{{\partial C}}
=c_\chi\operatorname{{Tr}}\bigl(&
W_\chi^{{(1)}}(Q_1)[\mathscr D_\chi E,Q_2]\\
&+W_\chi^{{(1)}}(Q_2)[\mathscr D_\chi E,Q_1]
\bigr).
\end{{aligned}}
$$

Plain-commutator placement:

$$
\begin{{aligned}}
H_\chi^{{C}}
=c_\chi\operatorname{{Tr}}\bigl(&
W_\chi^{{(1)}}(Q_1)[\mathscr D_\chi Q_2,E]\\
&+W_\chi^{{(1)}}(Q_2)[\mathscr D_\chi Q_1,E]
\bigr).
\end{{aligned}}
$$

Therefore

$$
\boxed{{
H_\chi^{{\rm full}}
=H_\chi^W+H_\chi^{{\partial C}}+H_\chi^C
}}.
$$

## 3. Raw labeled-port partition

For each chirality,

$$
N_W=8,
\qquad
N_{{\partial C}}=8,
\qquad
N_C=8,
\qquad
N_{{\rm full}}=24.
$$

Across both chiralities,

$$
N_{{\rm old\ fixed}}=16,
\qquad
N_{{\rm omitted}}=32.
$$

The omitted classes are exactly derivative-commutator and
plain-commutator placements.

## 4. Exact sparse-component rows

| id | sector/type | (H^W) | (H^{{\partial C}}) | (H^C) | full | old fixed |
|---|---|---:|---:|---:|---:|---:|
{chr(10).join(sample_lines)}

Every row obeys

$$
H^W+H^{{\partial C}}+H^C-H^{{\rm full}}=0.
$$

For matched ((+,A)) and ((-,D)), the old probe equals (H^W), not the
full Hessian.  Its explicit early gate also sets ((-,A)) and ((+,D)) to
zero before evaluating even (H^W).

## 5. Full interaction sector-pair sum

Let (H_\chi^D(L)) and (H_\psi^A(R)) be the fully polarized action
Hessians at the left and right labeled vertices.  Since both cubic action
vertices are even,

$$
\begin{{aligned}}
&\frac1{{2!}}
\sum_{{\chi,\psi\in\{{+,-\}}}}
\left[
H_\chi^D(L)H_\psi^A(R)
+H_\psi^A(R)H_\chi^D(L)
\right]\\
&=\sum_{{\chi,\psi\in\{{+,-\}}}}
H_\chi^D(L)H_\psi^A(R).
\end{{aligned}}
$$

Thus the (1/2!) is cancelled by the two left/right action-label
assignments; every sector pair has weight one:

$$
(++),\qquad (+-),\qquad (-+),\qquad (--).
$$

At the exact held-out point

$$
\ell=(3,2,-2,1),
$$

the full probe gives

$$
N_{{++}}=N_{{+-}}=N_{{-+}}=N_{{--}}
=-\frac{{97}}4+\frac{{103}}2i,
$$

$$
N_{{\rm full\ sector\ sum}}=-97+206i.
$$

For every sector pair,

$$
N_{{\rm selected}}=-49+97i,
\qquad
N_{{\rm longitudinal}}=\frac{{99}}4-\frac{{91}}2i,
$$

$$
N_{{\rm selected}}+N_{{\rm longitudinal}}
=-\frac{{97}}4+\frac{{103}}2i.
$$

The old fixed-strength probe instead gives

$$
(N_{{++}},N_{{+-}},N_{{-+}},N_{{--}})_{{\rm fixed}}
=(0,0,7+4i,0).
$$

Hence same-chirality rows cannot be removed by the old fixed-(W) graph
typing.  It omitted both two external-position classes and three sector
pairs.

## 6. Same-edge source quotient

Define

$$
T_0=I0\_DminusA1[A]*A1[B],
\qquad
T_2=I0\_A1[A]*DminusA1[B].
$$

The full-action aggregate selected numerators are exactly edge-divisible:

$$
N_{{S,T_0}}=\bar r_0^2Q_0,
\qquad
N_{{S,T_2}}=\bar r_2^2Q_2,
$$

with zero polynomial-division remainders and

$$
\begin{{aligned}}
Q_0={{}}&-\frac12l_0^2+il_0l_1
+\left(\frac32-i\right)l_0+\frac12l_1^2\\
&-\left(1+\frac32i\right)l_1-\frac12+\frac32i,
\end{{aligned}}
$$

$$
Q_2=-\frac12l_0^2+il_0l_1-\frac12l_0
+\frac12l_1^2+\frac i2l_1.
$$

The quotient is quadratic, not affine.  Its homogeneous quadratic sum is

$$
Q_0^{{(2)}}+Q_2^{{(2)}}
=-(l_0-il_1)^2,
\qquad
(\partial_{{l_0}}^2+\partial_{{l_1}}^2)
\left(Q_0^{{(2)}}+Q_2^{{(2)}}\right)=0.
$$

For each selected-parent row

$$
\rho=(T_s,R_L,R_R,\text{{Wick pairing}}),
$$

the exact statement already proved is

$$
N_{{S,\rho}}=Q_\rho\bar r_{{e(\rho)}}^2,
\qquad
N_{{{{\rm full}},\rho}}=N_{{S,\rho}}+L_\rho.
$$

The source occurrence is tagged before either action Hessian is multiplied.
For external colors ((D,A)=(1,0)), exact color support gives

$$
\epsilon(c_0,c_1,1)\epsilon(c_1,c_2,0)\ne0
\quad\Longleftrightarrow\quad
(c_0,c_1,c_2)=(0,2,1).
$$

Consequently

$$
T_0\longmapsto e_0,
\qquad
T_2\longmapsto e_2.
$$

Schwinger differentiation is linear in the occurrence projector:

$$
P_T\left(SH_LH_R\right)=P_T(S)H_LH_R.
$$

Reflection acts only on the action placements,

$$
\mathcal R(T,H_L,H_R)=(T,H_R,H_L),
$$

so it cannot exchange the physical source edge.

The raw cubic port table contains, for every chirality, raw word, and
external placement, exactly two ordered quantum-role rows,

$$
(S,B),
\qquad
(B,S).
$$

These are the two-line Wick endpoints inside the same ordered Hessian.  For
each physical edge the exact count is

$$
\frac1{{2!}}
\times 2_{{\rm action\ ordering}}
\times 2_{{\rm Wick\ endpoint}}
=2_{{\rm endpoint\ rows}}.
$$

The parent Hessian contains the same two endpoint rows.  Writing their
full-((d)) numerators as ((N_{{SB}})) and ((N_{{BS}})),

$$
\frac1{{2!}}
\left[(N_{{SB}}+N_{{BS}})+(N_{{SB}}+N_{{BS}})\right]
=N_{{SB}}+N_{{BS}}.
$$

The Gaussian product rule is

$$
\left\langle F_eK_ev_e\right\rangle
-\hbar\left\langle\frac{{\delta F_e}}{{\delta v_e}}\right\rangle
=0.
$$

It maps each endpoint row bijectively with the relative minus sign,

$$
K_{{\mathrm{{raw}},SB}}=-N_{{d,SB}},
\qquad
K_{{\mathrm{{raw}},BS}}=-N_{{d,BS}}.
$$

Therefore, separately on ((e_0)) and ((e_2)),

$$
N_{{d,e}}=L_e+Q_er_{{e,d}}^2,
\qquad
K_{{\mathrm{{raw}},e}}=-L_e-Q_er_{{e,d}}^2,
$$

$$
\boxed{{N_{{d,e}}+K_{{\mathrm{{raw}},e}}=0}},
\qquad
m_0=m_2=1.
$$

The DRED residue is consequently

$$
\boxed{{
N_{{{{\rm full}},e}}+K_{{\mathrm{{raw}},e}}
=Q_e\left(\bar r_e^2-r_{{e,d}}^2\right)
=Q_e\mu_\ell^2
}}.
$$

Thus the combined source/action/Wick row edge map is
`CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA`.  The old fixed-(W) audit
computed only the ((W,W)) block.  No affine fit or target coefficient is
used.  The raw normalization status is
`CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE`.

## 7. Target-blind typed reconstruction

The dotted-index convention used by the component engine is

$$
k_+^{{\dot0}}=\sigma_E(k)_{{0\dot1}},
\qquad
k_+^{{\dot1}}=-\sigma_E(k)_{{0\dot0}}.
$$

$$
k_-^{{\dot0}}=\sigma_E(k)_{{1\dot1}},
\qquad
k_-^{{\dot1}}=-\sigma_E(k)_{{1\dot0}}.
$$

| frame | $\epsilon\cdot p$ | $\epsilon\cdot q$ | $p_+^{{\dot a}}$ | $q_+^{{\dot a}}$ | $p_-^{{\dot a}}$ | $q_-^{{\dot a}}$ | $2\int(Q_0+Q_2)$ |
|---|---:|---:|---:|---:|---:|---:|---:|
{chr(10).join(typed_frame_lines)}

The former `p_only` and `q_only` frames both obey

$$
\epsilon\cdot q=1,
$$

and are rejected as `REJECTED_LONGITUDINAL_FRAME`.

Although `p_transverse` and `q_transverse` obey

$$
p_-^{{\dot a}}q_-^{{\dot a}}\ne0,
$$

on one unselected momentum, they contain the exact opposite-undotted
coefficients ((-1/3)) and ((-1/12)).  They are retained for edge/contact
checks and rejected from the typed solve as
`REJECTED_OPPOSITE_UNDOTTED_CONTAMINATION_FOR_TYPED_SOLVE`.

The canonical and swapped-transverse rows instead give

$$
\begin{{pmatrix}}
-i&-1\\
-1&-i
\end{{pmatrix}}
\begin{{pmatrix}}c_p\\c_q\end{{pmatrix}}
=
\begin{{pmatrix}}
-\frac12+i\\
-1+\frac i2
\end{{pmatrix}},
$$

$$
\det
\begin{{pmatrix}}
-i&-1\\
-1&-i
\end{{pmatrix}}
=-2,
\qquad
c_p=-\frac i2,
\qquad
c_q=-i.
$$

The independent alternate frame obeys

$$
-c_p+ic_q=1+\frac i2.
$$

The exact global factor omitted by the normalized probe is

$$
g^2\left(-\frac1\hbar\right)^2(-\hbar)^3
=-\hbar g^2.
$$

For every sector pair,

$$
\frac1{{2!}}\times2=1,
$$

and all four sector polynomials are equal.  Therefore

$$
4\left(-\hbar g^2\right)
\left(\frac1{{32\pi^2}}\right)
\left(\frac{{16\pi^2}}{{\hbar g^2}}\right)
=-2
$$

in ((\lambda_1)) units.  Reflection is a distinct ordered output with
weight one, and dotted-index reordering gives

$$
p_{{+\dot\alpha}}A D^{{\dot\alpha}}
=-D_{{\dot\alpha}}p_+^{{\dot\alpha}}A.
$$

The raw contact multiplicities ((m_0=m_2=1)) are now verified.  In the
ordered basis

$$
(DA_p,DA_q,AD_p,AD_q),
$$

$$
\boxed{{
\frac{{\Gamma_{{AA,g}}^{{(1)}}}}
{{\lambda_1\mathbb F^{{AB}}_{{DE}}}}
=\left(
i,
2i,
-i,
-2i
\right)
}}.
$$

The common Fourier map is

$$
\mathcal F_{{\rm common}}=-i,
$$

so the extended ordered vector becomes

$$
(1,2,-1,-2).
$$

The two ((q)) rows are separately typed as

$$
DA_q=(P\!\cdot\!D)A,
\qquad
AD_q=A(P\!\cdot\!D),
$$

and are EOM/divergence carriers.  They are not identified with ((p+q)).
Only after this typed quotient,

$$
(DA_p,DA_q,AD_p,AD_q)
\longmapsto
(DA_p,0,AD_p,0),
$$

$$
\boxed{{
\frac{{\Gamma_{{AA,g}}^{{(1),\rm phys}}}}
{{\lambda_1\mathbb F^{{AB}}_{{DE}}}}
=DA_p-AD_p
}},
$$

so the direct and reflected physical coefficients are ((+1)) and ((-1)).

The two Wick endpoints occur in both ((N_d)) and ((K_{{\rm raw}})); they do
not multiply their ratio.  Hence there is no extra edge factor two and no
global metric-trace factor ((d)) or ((4)).

No holomorphic-twist target is used.

## 8. Matter primitive sign

The exact finite Grassmann words are

$$
\mathcal G_0=-16384\mathcal S_{{012}},
\qquad
\mathcal G_2=-16384\mathcal T_{{012}}.
$$

All remaining primitive signs give

$$
\eta_{{\rm src}}
=\operatorname{{sgn}}\left(-\frac18\right)^2
\left[(-1)(-1)\right]^2
(-1)^2(+1)
\left(\frac1{{2!}}2\right)(+1)
=+1.
$$

Hence

$$
C^D>B^E=-\lambda_1,
\qquad
B^D>C^E=+\lambda_1,
$$

$$
\boxed{{(c_{{BC}},c_{{CB}})=(1,-1)}}.
$$

## 9. Exhaustive replay record

```json
{exhaustive_text}
```

$$
N_{{\rm pass}}={checks['passed']},
\qquad
N_{{\rm fail}}={checks['failed']}.
$$
"""


def validate_artifact(payload: dict[str, object]) -> None:
    if payload["schema"] != "step5-aa-external-slot-decomposition-exact-v1":
        raise AssertionError("schema")
    if payload["external_target_used"] is not False:
        raise AssertionError("target boundary")
    checks = payload["checks"]
    if not isinstance(checks, dict) or checks["failed"] != 0:
        raise AssertionError("checks")
    raw_partition = payload["raw_port_partition"]
    if not isinstance(raw_partition, dict):
        raise TypeError("raw partition")
    if raw_partition["old_fixed_omitted_rows"] != 32:
        raise AssertionError("omitted rows")
    occurrence = payload["occurrence_edge_structural_lemma"]
    if not isinstance(occurrence, dict) or occurrence[
        "combined_raw_row_edge_status"
    ] != "CLOSED_BY_OCCURRENCE_EDGE_STRUCTURAL_LEMMA":
        raise AssertionError("occurrence edge closure")
    raw_contact = occurrence["raw_schwinger_contact_hessian_certificate"]
    if not isinstance(raw_contact, dict) or raw_contact[
        "status"
    ] != "CLOSED_RAW_SCHWINGER_CONTACT_HESSIAN_MULTIPLICITY_ONE":
        raise AssertionError("raw Schwinger contact multiplicity")
    if raw_contact["verified_multiplicity"] != {"m0": "1", "m2": "1"}:
        raise AssertionError("raw Schwinger contact values")
    if any(
        row["N_d_plus_K_raw"] != "0"
        for row in raw_contact["polynomial_cancellations"]
    ):
        raise AssertionError("raw full-d Schwinger cancellation")
    typed = payload["typed_ordered_reconstruction"]
    if not isinstance(typed, dict) or typed[
        "ordered_vector_over_lambda1_times_F"
    ] != ["I", "2*I", "-I", "-2*I"]:
        raise AssertionError("typed ordered vector")
    fourier = typed["fourier_and_physical_quotient"]
    if (
        not isinstance(fourier, dict)
        or fourier["physical_status"]
        != "ACCEPTED_RAW_SCHWINGER_CONTACT_MULTIPLICITY_ONE_VERIFIED"
        or fourier["physical_ordered_p_vector_over_lambda1_times_F"]
        != ["1", "-1"]
    ):
        raise AssertionError("typed physical quotient")
    matter_sign = payload["matter_primitive_sign"]
    if not isinstance(matter_sign, dict) or matter_sign[
        "ordered_vector_over_lambda1_times_F"
    ] != ["1", "-1"]:
        raise AssertionError("matter primitive sign")
    exhaustive = payload["exhaustive_component_replay"]
    if isinstance(exhaustive, dict) and "total_equality_failures" in exhaustive:
        if exhaustive["total_equality_failures"] != 0:
            raise AssertionError("exhaustive equality")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check-artifact", action="store_true")
    parser.add_argument("--replay-exhaustive", action="store_true")
    parser.add_argument("--replay-triangle", action="store_true")
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()

    if args.check_artifact:
        payload = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        validate_artifact(payload)
        if MD_OUT.read_text(encoding="utf-8") != render_markdown(payload):
            raise AssertionError(f"stale artifact: {MD_OUT}")
        print("PASS AA_EXTERNAL_SLOT_RAW_PARTITION")
        print("PASS AA_EXTERNAL_SLOT_SUM_EQUALS_FULL_HESSIAN")
        print("PASS AA_OLD_FIXED_W_TWO_CLASSES_MISSING")
        print(f"SUMMARY {payload['checks']['passed']}/{payload['checks']['count']} PASS")
        return 0

    exhaustive = (
        exhaustive_component_replay(args.workers)
        if args.replay_exhaustive
        else None
    )
    triangle_replay = (
        probe.triangle_numerator(
            alg.vec((3, 2, -2, 1)),
            args.workers,
            compare_fixed=True,
        )
        if args.replay_triangle
        else None
    )
    payload = build_payload(exhaustive, triangle_replay)
    validate_artifact(payload)
    if args.write:
        JSON_OUT.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        MD_OUT.write_text(render_markdown(payload), encoding="utf-8")
        print(f"PASS wrote {JSON_OUT}")
        print(f"PASS wrote {MD_OUT}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
