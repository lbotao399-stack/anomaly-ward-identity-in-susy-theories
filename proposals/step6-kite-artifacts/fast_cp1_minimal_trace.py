#!/usr/bin/env python3
"""Exact minimal WW-DA-01 trace for the Step-6 CP1 blocker.

This diagnostic imports the independent bitmask engine, fixes the first endpoint
assignment and one spin branch, and prints every operator action on the three delta
lines.  It does not choose an unrecorded external-jet/EOM projection.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path

import fast_cp0_cp1_engine as e


def stats(g: e.GP) -> dict[str, int]:
    return {
        "grassmann_masks": len(g),
        "coefficient_terms": sum(len(p) for p in g.values()),
        "max_grassmann_degree": max((m.bit_count() for m in g), default=0),
    }


def word_text(word: e.Word) -> str:
    return f"{e.qstr(word[0])} " + " ".join(f"{k}_{i}" for k, i in word[1])


def traced_line(
    name: str,
    left_point: int,
    right_point: int,
    left_word: e.Word,
    right_word: e.Word,
    left_momentum: e.Matrix,
    right_momentum: e.Matrix,
) -> tuple[e.GP, dict[str, object]]:
    value = e.delta4_pair(left_point, right_point)
    stages: list[dict[str, object]] = [
        {"action": "delta4", **stats(value)}
    ]
    for kind, idx in reversed(right_word[1]):
        value = e.apply_letter(value, (kind, idx), right_point, right_momentum)
        stages.append({"action": f"right:{kind}_{idx}", **stats(value)})
    value = e.gscale(value, right_word[0])
    stages.append({"action": f"right:coefficient={e.qstr(right_word[0])}", **stats(value)})
    for kind, idx in reversed(left_word[1]):
        value = e.apply_letter(value, (kind, idx), left_point, left_momentum)
        stages.append({"action": f"left:{kind}_{idx}", **stats(value)})
    value = e.gscale(value, left_word[0])
    stages.append({"action": f"left:coefficient={e.qstr(left_word[0])}", **stats(value)})
    return value, {
        "line": name,
        "left_word_operator_order": word_text(left_word),
        "right_word_operator_order": word_text(right_word),
        "evaluation_order": "right word from rightmost letter to leftmost, then left word from rightmost letter to leftmost",
        "stages": stages,
    }


def main() -> int:
    # WW-DA-01: placement A, bar-D endpoint r0, D endpoint r1.
    # Minimal spin branch: dot-alpha=0 and a=0 (external W^+ branch).
    _, cbar = e.vertex_realization("-", 0)
    _, cd = e.vertex_realization("+", 0)

    t1, trace1 = traced_line(
        "T1:r0",
        0,
        1,
        e.W_OALPHA,
        cbar,
        e.M_R0_O,
        e.M_R0_Y1,
    )
    t2, trace2 = traced_line(
        "T2:r1",
        1,
        2,
        e.W_ID,
        cd,
        e.M_R1_Y1,
        e.M_R1_Y2,
    )
    t3, trace3 = traced_line(
        "T3:r2",
        0,
        2,
        e.W_OBETA,
        e.W_ID,
        e.M_R2_O,
        e.M_R2_Y2,
    )

    wt_y1, _ = e.external_letters(1)
    _, w_y2 = e.external_letters(2)
    value = e.gmul(t1, t2)
    multiplication = [{"action": "T1*T2", **stats(value)}]
    value = e.gmul(value, t3)
    multiplication.append({"action": "T1*T2*T3", **stats(value)})
    value = e.gmul(value, wt_y1[0])
    multiplication.append({"action": "*Wtilde_dot0(q)", **stats(value)})
    value = e.gmul(value, w_y2[0])
    multiplication.append({"action": "*W^+(p)", **stats(value)})

    source = [
        e.Factor(0, 1, word=e.W_OALPHA, point=0),
        e.Factor(1, 0, word=e.W_OBETA, point=0),
        e.Factor(2, 1, external=wt_y1[0]),
        e.Factor(3, 1, word=cbar, point=1),
        e.Factor(4, 0, word=e.W_ID, point=1),
        e.Factor(5, 1, external=w_y2[0]),
        e.Factor(6, 1, word=cd, point=2),
        e.Factor(7, 0, word=e.W_ID, point=2),
    ]
    target_ids = [0, 3, 4, 6, 1, 7, 2, 5]
    odd_source = [f.fid for f in source if f.parity]
    odd_target = [fid for fid in target_ids if next(f for f in source if f.fid == fid).parity]
    source_pos = {f.fid: i for i, f in enumerate(source)}
    inversions = [
        [odd_target[i], odd_target[j]]
        for i in range(len(odd_target))
        for j in range(i + 1, len(odd_target))
        if source_pos[odd_target[i]] > source_pos[odd_target[j]]
    ]
    koszul = e.koszul_sign(source, target_ids)
    if koszul < 0:
        value = e.gscale(value, (F(-1), F(0)))
    value = e.berezin(value, 1)
    multiplication.append({"action": "Koszul then int d4theta_1", **stats(value)})
    value = e.berezin(value, 2)
    multiplication.append({"action": "int d4theta_2", **stats(value)})
    # Vertex product +1/4; WW-DA-01 color canonicalization sign is -1.
    value = e.gscale(value, (F(-1, 4), F(0)))
    multiplication.append({"action": "vertex product (+1/4) * color sign (-1)", **stats(value)})

    actual = e.cp1_assignment("a", "r0", "r1")
    base = e.cp1_seed_structure(e.MOM[0], e.MOM[1])
    dictionary = {
        label: e.geq(actual, e.gscale(base, weight))
        for label, weight in {
            "+1/2": (F(1, 2), F(0)),
            "-1/2": (F(-1, 2), F(0)),
            "+i/2": (F(0), F(1, 2)),
            "-i/2": (F(0), F(-1, 2)),
        }.items()
    }
    difference = e.gadd(actual, e.gscale(base, (F(0), F(1, 2))))

    report = {
        "generated_artifact": True,
        "generated_by": "proposals/step6-kite-artifacts/fast_cp1_minimal_trace.py",
        "checkpoint": "CP1/WW-DA-01",
        "memo_tags": ["seed-6", "seed-7", "seed-8"],
        "endpoint_word": "(D_-K_+)_A K_{+,B} barD[r0] D[r1]",
        "source_factor_order": [0, 1, 2, 3, 4, 5, 6, 7],
        "source_factor_labels": {
            "0": "(D_-K_+) on r0",
            "1": "K_+ on r2",
            "2": "Wtilde_dot0 external",
            "3": "barD^dot0 on r0",
            "4": "identity on r1 at Y1",
            "5": "W^+ external",
            "6": "D_+ on r1",
            "7": "identity on r2 at Y2",
        },
        "target_factor_order": target_ids,
        "odd_source_order": odd_source,
        "odd_target_order": odd_target,
        "koszul_inversions": inversions,
        "koszul_sign": koszul,
        "line_traces": [trace1, trace2, trace3],
        "multiplication_and_berezin_trace": multiplication,
        "spin_branch_result": stats(value),
        "full_spin_sum_actual": stats(actual),
        "seed_structure": stats(base),
        "overall_dictionary_scan": dictionary,
        "first_symbolic_difference_examples_against_minus_i_over_2": e.symbolic_difference_examples(difference, 8),
        "internal_leibniz_check_from_engine_A": "R_a+R_b = +D_- T exactly; the mismatch is not a failure of the ordinary Leibniz rule.",
        "missing_typed_rule": "No allowed input defines the IBP/external-jet/EOM projection that deletes Wtilde*D_+W^+, Wtilde*D_-W^-, and (barD Wtilde)*(D^2 W) branches and converts the surviving branch into r_i*p*r_j.",
    }
    out = Path(__file__).with_name("generated") / "cp0_cp4_cp1_minimal_trace.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    print(f"REPORT {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
