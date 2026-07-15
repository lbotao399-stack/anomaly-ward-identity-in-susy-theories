#!/usr/bin/env python3
"""Locate the first AA-gauge D-algebra error without an external target.

The old endpoint checker contracted an external lower-index W_+ with D_+.
The cubic Hessian contains W^gamma D_gamma, however, so
W^-=-W_+ selects -D_-.  The wrong projection used the same undotted row on
both sides and manufactured a traceless rank-two word.  This checker replays
both projections, splits the marked source into selected-square and
longitudinal pieces, and proves that the corrected projection contains the
expected determinant/inverse-kernel squares.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import step5_aa_gauge_marked_occurrence_exact_audit as aa  # noqa: E402


DEFAULT_JSON = ROOT / "audits/step5-aa-gauge-longitudinal-first-error-exact.json"


def longitudinal_mark(word, point, momentum):
    """(sqrt(2)/16) D_+ barD^2 D^2 acting on one source endpoint."""

    return (
        sp.sqrt(2)
        / 16
        * aa.d_operator(
            aa.bar_d_square(
                aa.d_square(word, point, momentum), point, momentum
            ),
            point,
            0,
            momentum,
        )
    )


def projected_rows(
    source_01,
    source_02,
    external_d,
    external_w,
    middle,
    r0,
    r1,
    r2,
    *,
    chiral_lower_index,
    raised_external_sign,
):
    bar_01 = lambda word: aa.bar_d_upper(word, 1, 0, aa.negative(r0))
    bar_12 = lambda word: aa.bar_d_upper(word, 1, 0, r1)
    d_02 = lambda word: raised_external_sign * aa.d_operator(
        word, 2, chiral_lower_index, r2
    )
    d_12 = lambda word: raised_external_sign * aa.d_operator(
        word, 2, chiral_lower_index, aa.negative(r1)
    )
    words = (
        source_01 * bar_12(middle) * d_02(source_02),
        -source_01 * d_12(bar_12(middle)) * source_02,
        -bar_01(source_01) * middle * d_02(source_02),
        bar_01(source_01) * d_12(middle) * source_02,
    )
    integrated_mask = sum(1 << index for index in range(4, 13))
    return tuple(
        sp.factor((external_d * external_w * word).terms.get(integrated_mask, 0))
        for word in words
    )


def expression(value):
    return sp.sstr(sp.factor(value))


def build_payload():
    momenta = [sp.symbols(f"a{i} b{i} c{i} d{i}") for i in range(3)]
    r0, r1, r2 = momenta
    q = tuple(r0[index] - r1[index] for index in range(4))
    p = tuple(r1[index] - r2[index] for index in range(4))

    external_d = aa.grassmann_exponential(aa.plane_wave_bilinear(1, q)) * aa.variable(12)
    external_w = (
        aa.grassmann_exponential(-aa.plane_wave_bilinear(2, p))
        * aa.variable(aa.coordinate(2, 0))
    )
    middle = aa.theta_delta(1, 2)

    delta_01 = aa.theta_delta(0, 1)
    delta_02 = aa.theta_delta(0, 2)
    unmarked_01 = aa.source_bottom(aa.source_k(delta_01, 0, r0))
    unmarked_02 = aa.source_bottom(aa.source_k(delta_02, 0, aa.negative(r2)))

    full_01 = aa.source_bottom(aa.marked_source_k(delta_01, 0, r0))
    full_02 = aa.source_bottom(
        aa.marked_source_k(delta_02, 0, aa.negative(r2))
    )
    long_01 = aa.source_bottom(longitudinal_mark(delta_01, 0, r0))
    long_02 = aa.source_bottom(
        longitudinal_mark(delta_02, 0, aa.negative(r2))
    )
    selected_01 = full_01 - long_01
    selected_02 = full_02 - long_02

    def replay(source_01, source_02, *, correct):
        return projected_rows(
            source_01,
            source_02,
            external_d,
            external_w,
            middle,
            r0,
            r1,
            r2,
            chiral_lower_index=1 if correct else 0,
            raised_external_sign=-1 if correct else 1,
        )

    sectors = {
        "mark01_full": replay(full_01, unmarked_02, correct=True),
        "mark01_selected": replay(selected_01, unmarked_02, correct=True),
        "mark01_longitudinal": replay(long_01, unmarked_02, correct=True),
        "mark02_full": replay(unmarked_01, full_02, correct=True),
        "mark02_selected": replay(unmarked_01, selected_02, correct=True),
        "mark02_longitudinal": replay(unmarked_01, long_02, correct=True),
    }
    wrong_sectors = {
        "mark01_selected": replay(selected_01, unmarked_02, correct=False),
        "mark02_selected": replay(unmarked_01, selected_02, correct=False),
    }

    zero = (sp.Integer(0),) * 4
    assert wrong_sectors["mark01_selected"] == zero
    assert wrong_sectors["mark02_selected"] == zero
    assert all(
        sp.simplify(
            sectors[f"mark{mark}_full"][index]
            - sectors[f"mark{mark}_selected"][index]
            - sectors[f"mark{mark}_longitudinal"][index]
        )
        == 0
        for mark in ("01", "02")
        for index in range(4)
    )

    a0, b0, c0, d0 = r0
    _, _, _, _ = r1
    a2, b2, c2, d2 = r2
    wedge_02 = a0 * b2 - b0 * a2
    det_0 = a0 * d0 - b0 * c0
    det_2 = a2 * d2 - b2 * c2
    expected_selected_01 = (-b2 * det_0, b2 * det_0, b2 * det_0, b2 * det_0)
    expected_selected_02 = (b0 * det_2, -b0 * det_2, b0 * det_2, b0 * det_2)
    assert all(
        sp.simplify(
            sectors["mark01_selected"][index] - expected_selected_01[index]
        )
        == 0
        for index in range(4)
    )
    assert all(
        sp.simplify(
            sectors["mark02_selected"][index] - expected_selected_02[index]
        )
        == 0
        for index in range(4)
    )
    sums = {name: sp.factor(sum(values)) for name, values in sectors.items()}
    assert sp.simplify(sums["mark01_selected"] - 2 * b2 * det_0) == 0
    assert sp.simplify(sums["mark02_selected"] - 2 * b0 * det_2) == 0
    assert sp.simplify(sums["mark01_longitudinal"] + 2 * d0 * wedge_02) == 0
    assert sums["mark02_longitudinal"] == 0

    return {
        "schema": "awi.step5.aa-gauge-longitudinal-first-error-exact.v2",
        "status": "AA_GAUGE_WRONG_CHIRAL_INDEX_PROVED__FULL_EDGE_ORBIT_PENDING",
        "external_target_used": False,
        "index_correction": (
            "W^gamma D_gamma with external W_plus selects "
            "W^minus=-W_plus and therefore -D_minus; the old D_plus endpoint is rejected"
        ),
        "marked_identity": (
            "Dminus*A1=selected+longitudinal; "
            "selected=sqrt(2)*bar(r_e)^2*Dplus*u; "
            "longitudinal=sqrt(2)/16*Dplus*barD2*D2*u"
        ),
        "rows": {
            name: [expression(value) for value in values]
            for name, values in sectors.items()
        },
        "row_sums": {name: expression(value) for name, value in sums.items()},
        "wrong_Dplus_control": {
            name: [expression(value) for value in values]
            for name, values in wrong_sectors.items()
        },
        "conclusion": {
            "old_same_undotted_row_projection": "zero selected square row by row",
            "correct_selected_mark01": "2*b2*det(r0)=-2*b2*bar(r0)^2",
            "correct_selected_mark02": "2*b0*det(r2)=-2*b0*bar(r2)^2",
            "rejected_inference": (
                "the former traceless rank-two conclusion came from contracting "
                "lower W_plus with D_plus instead of -D_minus"
            ),
            "required_completion": (
                "pair det(r0) and det(r2) with their own full-d Schwinger contacts, "
                "then complete the transported longitudinal and link orbit"
            ),
        },
        "checks": [
            "old_Dplus_mark01_selected_zero_4_of_4",
            "old_Dplus_mark02_selected_zero_4_of_4",
            "correct_full_equals_selected_plus_longitudinal_8_of_8",
            "correct_mark01_selected_rows_exact",
            "correct_mark02_selected_rows_exact",
            "correct_selected_sums_are_r0_and_r2_determinants",
            "correct_longitudinal_sums_exact",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for check in payload["checks"]:
        print(f"PASS {check}")
    print(f"SUMMARY {len(payload['checks'])}/{len(payload['checks'])} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
