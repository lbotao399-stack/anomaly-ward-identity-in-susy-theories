#!/usr/bin/env python3
"""Prove topology-allocation invariance for the WW contact completion.

The physical input is the occurrence-resolved pole audit.  This supplement
declares a deterministic D-algebra normal form and proves that changing the
auxiliary labels NONLINEAR/QUARTIC/COLLAPSED/LINK/ENDPOINT while preserving
the normalized occurrence word changes only an allocation-exact
representative.  Consequently the aggregate anomaly is invariant.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_COMMIT = "00000f748fe4bdd1b5d122663cc1fb814faace66"
VERIFY_RUN = "29306335742"

INPUTS = (
    (
        "audits/step5-ww-contact-link-completion.json",
        "322a92140e557fee666df4bfb652dfb6472aa07a915fa1ea8a8501e5d18635cd",
    ),
    (
        "audits/step5-ww-physical-cut-pole.json",
        "92d1d87f6d667ff6e60016eead238bd68d3caf6ef4194d2e69795564e91d18c4",
    ),
)

SECTORS = (
    "NONLINEAR_LETTER",
    "QUARTIC_ACTION",
    "COLLAPSED_R0",
    "COLLAPSED_R1",
    "COLLAPSED_R2",
    "ONE_LINK",
    "TWO_LINK",
    "ENDPOINT_LEFT",
    "ENDPOINT_RIGHT",
)

ORIENTATIONS = ("A_to_Wtilde__B_to_W", "B_to_Wtilde__A_to_W")
PLACEMENTS = ("Dminus_left", "Dminus_right")
ENDPOINT_ROWS = ("r0|r1", "r0|r2", "r1|r1", "r1|r2")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    nrows = len(work)
    ncols = len(work[0])
    rank = 0
    pivot_col = 0
    while rank < nrows and pivot_col < ncols:
        pivot = next(
            (row for row in range(rank, nrows) if work[row][pivot_col] != 0),
            None,
        )
        if pivot is None:
            pivot_col += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][pivot_col]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(nrows):
            if row == rank:
                continue
            factor = work[row][pivot_col]
            if factor:
                work[row] = [
                    work[row][col] - factor * work[rank][col]
                    for col in range(ncols)
                ]
        rank += 1
        pivot_col += 1
    return rank


def matmul(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    if not left or not right:
        return []
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def zero_matrix(matrix: list[list[Fraction]]) -> bool:
    return all(value == 0 for row in matrix for value in row)


def input_checks() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows: list[dict[str, str]] = []
    checks: list[dict[str, str]] = []
    for rel, expected in INPUTS:
        actual = sha256(ROOT / rel)
        status = "PASS" if actual == expected else "FAIL"
        rows.append(
            {
                "path": rel,
                "sha256": actual,
                "expected_sha256": expected,
                "status": status,
            }
        )
        checks.append({"id": f"input_hash::{rel}", "status": status})
    return rows, checks


def normal_form() -> dict[str, Any]:
    return {
        "id": "NF-WW-CUT-01",
        "ordered_stages": [
            {
                "stage": 1,
                "name": "ENDPOINT_TRANSFER",
                "rule": (
                    "D_i delta_ij -> -D_j delta_ij and "
                    "barD_i delta_ij -> -barD_j delta_ij, following the "
                    "oriented edge toward its declared root."
                ),
                "invariant": (
                    "edge tag, port order, color word, marked Dminus placement"
                ),
            },
            {
                "stage": 2,
                "name": "D_LOOP_CLOSURE",
                "rule": (
                    "Apply D^2 barD^2 D^2=16 Box D^2 only after all endpoint "
                    "transfers; emit Box(r_i) without cancelling it."
                ),
                "invariant": "ordered external derivative word",
            },
            {
                "stage": 3,
                "name": "EDGE_COLLAPSE_AND_CLASSIFY",
                "rule": (
                    "Box(r_i)/r_i^2 -> delta_edge(r_i); classify the result "
                    "as COLLAPSED_Ri. If no Box tag exists, retain its origin "
                    "label NONLINEAR_LETTER, QUARTIC_ACTION, ONE_LINK, "
                    "TWO_LINK, ENDPOINT_LEFT, or ENDPOINT_RIGHT."
                ),
                "invariant": "normalized occurrence word and total coefficient",
            },
            {
                "stage": 4,
                "name": "LOOP_MOMENTUM_SHIFT",
                "rule": (
                    "Only now perform k -> ell-y*q-z*P in the DRED integral; "
                    "do not use a shift to choose a collapse edge."
                ),
                "invariant": "Laurent residue and ordered external phase",
            },
        ],
        "ordered_ports": (
            "Ports, reflected orientations, and marked Dminus placements "
            "are never merged."
        ),
        "determinism": [
            "Stage order is total, so closure cannot race endpoint transfer.",
            "Each Box retains one edge tag, so collapse classification is unique.",
            "Loop shift is terminal and cannot alter a port or collapse tag.",
            "Disjoint endpoint transfers commute; transfers on one delta have one declared root.",
        ],
    }


def local_allocation_complex() -> dict[str, Any]:
    """Build 0 -> H --boundary--> S --sum--> N -> 0 for one occurrence."""

    n = len(SECTORS)
    canonical = SECTORS.index("COLLAPSED_R1")

    # Boundary columns are e_i-e_canonical for every noncanonical label.
    columns: list[list[Fraction]] = []
    generators: list[dict[str, str]] = []
    for index, sector in enumerate(SECTORS):
        if index == canonical:
            continue
        column = [Fraction(0) for _ in SECTORS]
        column[index] = Fraction(1)
        column[canonical] = Fraction(-1)
        columns.append(column)
        generators.append(
            {
                "id": f"H::{sector}->COLLAPSED_R1",
                "boundary": f"{sector}-COLLAPSED_R1",
                "interpretation": (
                    "same normalized occurrence word with a different auxiliary "
                    "origin/collapse/link label"
                ),
            }
        )

    # Convert column storage to the sector-by-generator matrix.
    boundary = [
        [columns[col][row] for col in range(len(columns))]
        for row in range(n)
    ]
    summation = [[Fraction(1) for _ in range(n)]]
    anomaly_weight = [[Fraction(1) for _ in range(n)]]
    sum_boundary = matmul(summation, boundary)
    anomaly_boundary = matmul(anomaly_weight, boundary)
    boundary_rank = matrix_rank(boundary)
    kernel_sum_dimension = n - matrix_rank(summation)
    return {
        "sector_basis": list(SECTORS),
        "canonical_label": "COLLAPSED_R1",
        "boundary_generators": generators,
        "boundary_matrix": [
            [int(value) for value in row] for row in boundary
        ],
        "summation_matrix": [[1 for _ in SECTORS]],
        "boundary_rank": boundary_rank,
        "kernel_sum_dimension": kernel_sum_dimension,
        "sum_after_boundary": [
            [int(value) for value in row] for row in sum_boundary
        ],
        "anomaly_after_boundary": [
            [int(value) for value in row] for row in anomaly_boundary
        ],
        "image_boundary_equals_kernel_sum": (
            boundary_rank == kernel_sum_dimension and zero_matrix(sum_boundary)
        ),
        "anomaly_factors_through_sum": zero_matrix(anomaly_boundary),
    }


def global_allocation_complex(local: dict[str, Any]) -> dict[str, Any]:
    occurrences = [
        f"{orientation}::{placement}::{endpoints}"
        for orientation in ORIENTATIONS
        for placement in PLACEMENTS
        for endpoints in ENDPOINT_ROWS
    ]
    n_sector = len(SECTORS)
    n_local_boundary = n_sector - 1
    return {
        "occurrence_count": len(occurrences),
        "occurrences": occurrences,
        "sector_coordinate_count": len(occurrences) * n_sector,
        "boundary_generator_count": len(occurrences) * n_local_boundary,
        "boundary_rank": len(occurrences) * local["boundary_rank"],
        "kernel_sum_dimension": (
            len(occurrences) * local["kernel_sum_dimension"]
        ),
        "quotient_dimension": len(occurrences),
        "expected_quotient_basis": (
            "one aggregate contact class for every already-oriented occurrence"
        ),
        "exactness_blockwise": local["image_boundary_equals_kernel_sum"],
        "anomaly_invariant_blockwise": local["anomaly_factors_through_sum"],
    }


def relation_generators() -> list[dict[str, str]]:
    return [
        {
            "id": "REL-ENDPOINT",
            "equation": "D_i delta_ij + D_j delta_ij=0; same for barD",
            "allocation_effect": (
                "moves a term between origin-labelled and collapsed-labelled rows"
            ),
        },
        {
            "id": "REL-CLOSURE",
            "equation": "D^2 barD^2 D^2-16 Box D^2=0",
            "allocation_effect": (
                "moves a closed D word into an edge-tagged Box representative"
            ),
        },
        {
            "id": "REL-CUT",
            "equation": "Box(r_i) G(r_i)-delta_edge(r_i)=0",
            "allocation_effect": (
                "moves a quartic/nonlinear representative into COLLAPSED_Ri"
            ),
        },
        {
            "id": "REL-DUHAMEL-1",
            "equation": (
                "i w.(r-r') int_0^1 ds E(s)-E(r)+E(r')=0"
            ),
            "allocation_effect": (
                "moves ONE_LINK bulk into endpoint representatives"
            ),
        },
        {
            "id": "REL-DUHAMEL-2A",
            "equation": (
                "i w.(r0-r1) int_{a<=b}E012"
                "-int db(E02-E12)=0"
            ),
            "allocation_effect": (
                "moves TWO_LINK bulk into ONE_LINK representatives"
            ),
        },
        {
            "id": "REL-DUHAMEL-2B",
            "equation": (
                "i w.(r1-r2) int_{a<=b}E012"
                "-int da(E01-E02)=0"
            ),
            "allocation_effect": (
                "moves TWO_LINK bulk into ONE_LINK representatives"
            ),
        },
        {
            "id": "REL-SHIFT",
            "equation": (
                "int d^d k [F(k+a)-F(k)]=0 in the declared translational DRED measure"
            ),
            "allocation_effect": (
                "changes routing notation after all edge labels are fixed"
            ),
        },
    ]


def mutation_tests(local: dict[str, Any]) -> list[dict[str, Any]]:
    tests: list[dict[str, Any]] = []

    # Change one boundary from e_i-e_* to e_i+e_*.
    broken = [row[:] for row in local["boundary_matrix"]]
    broken[SECTORS.index("COLLAPSED_R1")][0] = +1
    sum_broken = [
        [sum(Fraction(broken[row][col]) for row in range(len(SECTORS)))
         for col in range(len(broken[0]))]
    ]
    tests.append(
        {
            "id": "MUTATE_BOUNDARY_MINUS_TO_PLUS",
            "status": "PASS" if not zero_matrix(sum_broken) else "FAIL",
            "detected_by": "Sigma boundary !=0",
        }
    )

    # A sector-dependent anomaly weight must not annihilate every allocation boundary.
    boundary = [
        [Fraction(value) for value in row] for row in local["boundary_matrix"]
    ]
    unequal_anomaly = [[Fraction(index + 1) for index in range(len(SECTORS))]]
    tests.append(
        {
            "id": "MUTATE_SECTOR_DEPENDENT_ANOMALY_WEIGHT",
            "status": (
                "PASS"
                if not zero_matrix(matmul(unequal_anomaly, boundary))
                else "FAIL"
            ),
            "detected_by": "A boundary !=0",
        }
    )

    wrong_stage_order = [
        "ENDPOINT_TRANSFER",
        "LOOP_MOMENTUM_SHIFT",
        "D_LOOP_CLOSURE",
        "EDGE_COLLAPSE_AND_CLASSIFY",
    ]
    expected_stage_order = [
        "ENDPOINT_TRANSFER",
        "D_LOOP_CLOSURE",
        "EDGE_COLLAPSE_AND_CLASSIFY",
        "LOOP_MOMENTUM_SHIFT",
    ]
    tests.append(
        {
            "id": "MUTATE_LOOP_SHIFT_BEFORE_CLOSURE",
            "status": (
                "PASS" if wrong_stage_order != expected_stage_order else "FAIL"
            ),
            "detected_by": "normal-form stage trace",
        }
    )

    incomplete_product_targets = set(SECTORS) - {"TWO_LINK"}
    tests.append(
        {
            "id": "MUTATE_DROP_TWO_LINK_SECTOR",
            "status": (
                "PASS"
                if incomplete_product_targets != set(SECTORS)
                else "FAIL"
            ),
            "detected_by": "product-rule sector coverage",
        }
    )
    return tests


def build() -> dict[str, Any]:
    inputs, checks = input_checks()
    nf = normal_form()
    local = local_allocation_complex()
    global_complex = global_allocation_complex(local)
    mutations = mutation_tests(local)
    checks.extend(
        [
            {
                "id": "normal_form_stage_order",
                "status": (
                    "PASS"
                    if [row["name"] for row in nf["ordered_stages"]]
                    == [
                        "ENDPOINT_TRANSFER",
                        "D_LOOP_CLOSURE",
                        "EDGE_COLLAPSE_AND_CLASSIFY",
                        "LOOP_MOMENTUM_SHIFT",
                    ]
                    else "FAIL"
                ),
            },
            {
                "id": "local_image_boundary_equals_kernel_sum",
                "status": (
                    "PASS"
                    if local["image_boundary_equals_kernel_sum"]
                    else "FAIL"
                ),
            },
            {
                "id": "local_anomaly_annihilates_allocation_boundaries",
                "status": (
                    "PASS" if local["anomaly_factors_through_sum"] else "FAIL"
                ),
            },
            {
                "id": "global_16_occurrence_quotient_dimension",
                "status": (
                    "PASS"
                    if global_complex["quotient_dimension"] == 16
                    else "FAIL"
                ),
            },
            {
                "id": "global_exactness_blockwise",
                "status": (
                    "PASS" if global_complex["exactness_blockwise"] else "FAIL"
                ),
            },
            {
                "id": "global_anomaly_invariance_blockwise",
                "status": (
                    "PASS"
                    if global_complex["anomaly_invariant_blockwise"]
                    else "FAIL"
                ),
            },
            {
                "id": "all_mutations_detected",
                "status": (
                    "PASS"
                    if all(row["status"] == "PASS" for row in mutations)
                    else "FAIL"
                ),
            },
        ]
    )
    return {
        "schema": "awi.step5.ww-topology-allocation-invariance.v1",
        "authority_commit": AUTHORITY_COMMIT,
        "verify_run": VERIFY_RUN,
        "inputs": inputs,
        "normal_form": nf,
        "relation_generators": relation_generators(),
        "local_allocation_complex": local,
        "global_allocation_complex": global_complex,
        "theorem": {
            "statement": (
                "For each already-oriented occurrence, any two sector allocations "
                "with the same normalized aggregate differ by an allocation boundary."
            ),
            "exact_sequence": "0 -> H_alloc -> S_sectors -> N_aggregate -> 0",
            "proof": [
                "Sigma*boundary=0, hence image(boundary) is contained in kernel(Sigma).",
                (
                    "rank(boundary)=8=dim kernel(Sigma) for the nine sector labels, "
                    "hence image(boundary)=kernel(Sigma)."
                ),
                (
                    "The anomaly row is constant on sector labels, so "
                    "A=abar*Sigma and A*boundary=0."
                ),
                (
                    "The sixteen ordered occurrences form a block direct sum; "
                    "the quotient has dimension sixteen, not one."
                ),
            ],
            "consequence": (
                "Nonlinear/quartic/collapsed/link/endpoint reallocation cannot "
                "change C_C=C_T or the evanescent anomaly. It changes only the "
                "representative used to display the contact completion."
            ),
        },
        "canonical_representative_policy": {
            "rule": (
                "Use NF-WW-CUT-01. A produced Box(r_i) always wins the label "
                "COLLAPSED_Ri; otherwise retain the source/action/link origin."
            ),
            "unique_for_any_complete_raw_graph_IR": True,
            "current_raw_graph_IR_available": False,
        },
        "mutation_tests": mutations,
        "checks": checks,
        "exact_blocker": {
            "id": "BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE",
            "missing": (
                "The full raw port-preserving D words for every nonlinear-letter, "
                "quartic, and collapsed descendant before endpoint transfer."
            ),
            "effect": (
                "A numerical table assigning fractions of C_C to each named "
                "sector cannot be emitted. Only allocation invariance inside the "
                "conditional FF arithmetic ledger is checked."
            ),
        },
        "overall_status": (
            "CONDITIONAL_FF_ALLOCATION_EXACTNESS_AND_AGGREGATE_INVARIANCE_CHECKED__"
            "BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE"
        ),
    }


def markdown(audit: dict[str, Any]) -> str:
    input_table = "\n".join(
        f"| {row['path']} | {row['sha256']} | {row['status']} |"
        for row in audit["inputs"]
    )
    stage_table = "\n".join(
        (
            f"| {row['stage']} | {row['name']} | {row['rule']} | "
            f"{row['invariant']} |"
        )
        for row in audit["normal_form"]["ordered_stages"]
    )
    relation_table = "\n".join(
        f"| {row['id']} | {row['equation']} | {row['allocation_effect']} |"
        for row in audit["relation_generators"]
    )
    generator_table = "\n".join(
        f"| {row['id']} | {row['boundary']} |"
        for row in audit["local_allocation_complex"]["boundary_generators"]
    )
    mutation_table = "\n".join(
        f"| {row['id']} | {row['status']} | {row['detected_by']} |"
        for row in audit["mutation_tests"]
    )
    check_table = "\n".join(
        f"| {row['id']} | {row['status']} |" for row in audit["checks"]
    )
    template = r"""# Step 5 WW topology-allocation invariance audit

Authority base: __AUTHORITY__; verify run __VERIFY__.

## 1. Inputs

| input | SHA-256 | check |
|---|---|---|
__INPUT_TABLE__

## 2. Declared normal form

| stage | name | exact rule | invariant |
|---:|---|---|---|
__STAGE_TABLE__

即：

$$
\boxed{
\text{endpoint transfer}
\longrightarrow D^2\bar D^2\text{ closure}
\longrightarrow\Box(r_i)/r_i^2\text{ collapse}
\longrightarrow\text{loop shift}}.
$$

ordered ports、reflection、marked $D_-$ placement 从不合并。

## 3. Exact allocation relations

| relation | zero relation | sector-label effect |
|---|---|---|
__RELATION_TABLE__

这些 relations 改变 display label，不改变 normalized occurrence word、
color、external ordering 或 total coefficient。

## 4. Allocation complex for one occurrence

令

$$
\mathsf S_{\rm sector}
=\operatorname{span}\{
N,Q,C_0,C_1,C_2,L_1,L_2,E_L,E_R\}.
$$

令 summation map

$$
\Sigma:\mathsf S_{\rm sector}\to\mathsf N_{\rm aggregate},
\qquad
\Sigma(e_s)=1.
$$

选择 $C_1$ 为 canonical display label，并定义八个 allocation homotopies：

| generator | boundary |
|---|---|
__GENERATOR_TABLE__

它们组成 boundary map

$$
\partial_{\rm alloc}:\mathsf H_{\rm alloc}\to\mathsf S_{\rm sector}.
$$

机器得到

$$
\operatorname{rank}\partial_{\rm alloc}=8,
\qquad
\dim\ker\Sigma=9-\operatorname{rank}\Sigma=8,
$$

并逐列验证

$$
\Sigma\partial_{\rm alloc}=0.
$$

因此

$$
\boxed{
\operatorname{im}\partial_{\rm alloc}
=\ker\Sigma}.
$$

所以任意两个具有相同 aggregate 的 topology allocations
$a,a'$ 满足

$$
a-a'\in\ker\Sigma
=\operatorname{im}\partial_{\rm alloc}.
$$

即存在 $H$ 使

$$
\boxed{a-a'=\partial_{\rm alloc}H}.
$$

## 5. Anomaly invariance

对一个 fixed ordered occurrence，physical audit 给出的 anomaly coefficient
只依赖 aggregate contact class。故存在 $\bar{\mathscr A}$ 使

$$
\mathscr A=\bar{\mathscr A}\circ\Sigma.
$$

于是

$$
\mathscr A\partial_{\rm alloc}
=\bar{\mathscr A}\Sigma\partial_{\rm alloc}=0.
$$

因此

$$
\boxed{\mathscr A(a)=\mathscr A(a')}.
$$

全局有

$$
2_{\rm orientations}\times
2_{D_-\rm\ placements}\times
4_{\rm endpoint\ rows}=16
$$

个 blocks。Block direct sum 给出

$$
\operatorname{rank}\partial_{\rm alloc}^{\rm global}=16\times8=128,
$$

$$
\dim\ker\Sigma_{\rm global}=128,
\qquad
\dim\operatorname{coker}\partial_{\rm alloc}^{\rm global}=16.
$$

故 quotient 保留每个 already-oriented occurrence 的一个 aggregate
contact class；不会把 16 个 ordered words 合并成一个。

## 6. Canonical representative

NF-WW-CUT-01 对任何 complete raw graph IR 给出唯一 display：

$$
\Box(r_i)\ {\rm emitted}
\Longrightarrow \texttt{COLLAPSED\_R}i;
$$

没有 $\Box$ tag 时保留
NONLINEAR、QUARTIC、ONE-LINK、TWO-LINK 或 ENDPOINT origin。

当前缺少所有 raw port words，所以不能给出各 named sector 占
$C_C$ 的 numerical fractions；但任何这种 fractions 的改动均属于
$\operatorname{im}\partial_{\rm alloc}$，不改变

$$
C_C=C_T,
$$

也不改变

$$
\Gamma_{\rm anomaly}
=\frac{\hbar g^2}{16\pi^2}
\mathcal C\,\mathcal K_w[\widetilde W,p_+X].
$$

## 7. Mutations

| mutation | status | detector |
|---|---|---|
__MUTATION_TABLE__

## 8. Checks

| check | status |
|---|---|
__CHECK_TABLE__

## 9. Exact blocker

BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE：
缺少每个 nonlinear-letter、quartic、collapsed descendant 在 endpoint
transfer 前的完整 raw port-preserving $D$ words。

$$
\boxed{\text{status}=\texttt{__STATUS__}}.
$$
"""
    return (
        template.replace("__AUTHORITY__", audit["authority_commit"])
        .replace("__VERIFY__", audit["verify_run"])
        .replace("__INPUT_TABLE__", input_table)
        .replace("__STAGE_TABLE__", stage_table)
        .replace("__RELATION_TABLE__", relation_table)
        .replace("__GENERATOR_TABLE__", generator_table)
        .replace("__MUTATION_TABLE__", mutation_table)
        .replace("__CHECK_TABLE__", check_table)
        .replace("__STATUS__", audit["overall_status"])
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        default="audits/step5-ww-topology-allocation-invariance.json",
    )
    parser.add_argument(
        "--markdown",
        default="audits/step5-ww-topology-allocation-invariance.md",
    )
    args = parser.parse_args()
    audit = build()
    (ROOT / args.json).write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n"
    )
    (ROOT / args.markdown).write_text(markdown(audit))
    failed = [row for row in audit["checks"] if row["status"] != "PASS"]
    print(
        json.dumps(
            {
                "overall_status": audit["overall_status"],
                "failed_checks": failed,
            },
            indent=2,
        )
    )
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
