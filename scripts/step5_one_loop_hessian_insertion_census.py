#!/usr/bin/env python3
"""Exact abstract one-loop Hessian/source-insertion graph census.

The only field-theory input is the local Step-5 formal expansion

    H[J,V] = H0 + sum_(r>=1) H_r[V^r] + J sum_(s>=0) I_s[V^s],
    Gamma_I^(1) = (1/2) STr(H^{-1} I).

This module enumerates the rooted cyclic operator words, labeled background
polarizations, reflection metadata, and typed Gaussian-block paths at total
background orders n=2,3,4.  It proves combinatorial exhaustiveness only.  No
Hessian matrix element, amplitude, counterterm coefficient, or anomaly
coefficient is evaluated.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
from typing import Iterator, Sequence


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated/step5/one-loop-hessian-insertion-census.json"
AUDIT = ROOT / "audits/step5-one-loop-hessian-insertion-census-verification.json"


@dataclass(frozen=True)
class GaussianBlock:
    block_id: str
    sector: str
    carrier_fields: tuple[str, ...]
    canonical_quadratic_port_pairs: tuple[tuple[str, str], ...]
    grassmann_parity: int
    supertrace_weight: int


GAUSSIAN_BLOCKS = (
    GaussianBlock(
        block_id="V",
        sector="PHYSICAL_VECTOR",
        carrier_fields=("V",),
        canonical_quadratic_port_pairs=(("V", "V"),),
        grassmann_parity=0,
        supertrace_weight=1,
    ),
    GaussianBlock(
        block_id="PHI_PAIR_1",
        sector="PHYSICAL_ADJOINT_CHIRAL_PAIR",
        carrier_fields=("Phi_1", "TildePhi_1"),
        canonical_quadratic_port_pairs=(
            ("Phi_1", "TildePhi_1"),
            ("TildePhi_1", "Phi_1"),
        ),
        grassmann_parity=0,
        supertrace_weight=1,
    ),
    GaussianBlock(
        block_id="PHI_PAIR_2",
        sector="PHYSICAL_ADJOINT_CHIRAL_PAIR",
        carrier_fields=("Phi_2", "TildePhi_2"),
        canonical_quadratic_port_pairs=(
            ("Phi_2", "TildePhi_2"),
            ("TildePhi_2", "Phi_2"),
        ),
        grassmann_parity=0,
        supertrace_weight=1,
    ),
    GaussianBlock(
        block_id="PHI_PAIR_3",
        sector="PHYSICAL_ADJOINT_CHIRAL_PAIR",
        carrier_fields=("Phi_3", "TildePhi_3"),
        canonical_quadratic_port_pairs=(
            ("Phi_3", "TildePhi_3"),
            ("TildePhi_3", "Phi_3"),
        ),
        grassmann_parity=0,
        supertrace_weight=1,
    ),
    GaussianBlock(
        block_id="FP",
        sector="FADDEEV_POPOV",
        carrier_fields=(
            "cprime_plus",
            "tilde_c",
            "tilde_cprime_minus",
            "c",
        ),
        canonical_quadratic_port_pairs=(
            ("cprime_plus", "tilde_c"),
            ("tilde_c", "cprime_plus"),
            ("tilde_cprime_minus", "c"),
            ("c", "tilde_cprime_minus"),
        ),
        grassmann_parity=1,
        supertrace_weight=-1,
    ),
    GaussianBlock(
        block_id="NK",
        sector="NIELSEN_KALLOSH",
        carrier_fields=("b_NK", "tilde_b_NK"),
        canonical_quadratic_port_pairs=(
            ("b_NK", "tilde_b_NK"),
            ("tilde_b_NK", "b_NK"),
        ),
        grassmann_parity=0,
        supertrace_weight=1,
    ),
)

BLOCK_BY_ID = {block.block_id: block for block in GAUSSIAN_BLOCKS}
BLOCK_IDS = tuple(block.block_id for block in GAUSSIAN_BLOCKS)


def positive_compositions(total: int, length: int) -> Iterator[tuple[int, ...]]:
    """Yield ordered positive compositions of ``total`` into ``length`` parts."""

    if total < 0 or length < 0:
        raise ValueError("total and length must be nonnegative")
    if length == 0:
        if total == 0:
            yield ()
        return
    if total < length:
        return
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first, *tail)


def hessian_compositions(n: int) -> list[tuple[int, tuple[int, ...]]]:
    """Enumerate ``s+r_1+...+r_k=n`` with ``s>=0`` and every ``r_i>=1``."""

    if n < 0:
        raise ValueError("background order must be nonnegative")
    rows: list[tuple[int, tuple[int, ...]]] = []
    for s in range(n + 1):
        remaining = n - s
        if remaining == 0:
            rows.append((s, ()))
            continue
        for k in range(1, remaining + 1):
            rows.extend((s, parts) for parts in positive_compositions(remaining, k))
    return rows


def ordered_set_partitions(
    labels: Sequence[int],
    block_sizes: Sequence[int],
) -> Iterator[tuple[tuple[int, ...], ...]]:
    """Yield labeled set partitions into distinguished ordered blocks.

    The first block is the insertion block.  Subsequent blocks are the rooted,
    directed cyclic sequence of Hessian vertices.  A block is a set and is
    therefore stored in increasing order; blocks themselves are not quotiented.
    """

    labels_tuple = tuple(sorted(labels))
    if any(size < 0 for size in block_sizes):
        raise ValueError("block sizes must be nonnegative")
    if sum(block_sizes) != len(labels_tuple):
        raise ValueError("block sizes must exhaust the labels")
    if not block_sizes:
        if not labels_tuple:
            yield ()
        return

    first_size = block_sizes[0]
    for chosen in combinations(labels_tuple, first_size):
        chosen_set = set(chosen)
        remainder = tuple(label for label in labels_tuple if label not in chosen_set)
        for tail in ordered_set_partitions(remainder, block_sizes[1:]):
            yield (tuple(chosen), *tail)


def rendered_vertex(kind: str, order: int, labels: Sequence[int]) -> str:
    arguments = ",".join(f"V_{label}" for label in labels)
    return f"{kind}_{order}[{arguments}]" if arguments else f"{kind}_{order}"


def term_id(n: int, insertion_labels: Sequence[int], h_blocks: Sequence[Sequence[int]]) -> str:
    insertion = "_".join(map(str, insertion_labels)) or "EMPTY"
    h_part = "__".join("_".join(map(str, block)) for block in h_blocks) or "NONE"
    return f"N{n}__I_{insertion}__H_{h_part}"


def rooted_word_tokens(s: int, r_parts: Sequence[int]) -> list[str]:
    tokens = ["G0", f"I_{s}"]
    for r in r_parts:
        tokens.extend(("G0", f"H_{r}"))
    return tokens


def labeled_term_rows(n: int) -> list[dict[str, object]]:
    labels = tuple(range(1, n + 1))
    rows: list[dict[str, object]] = []
    for s, r_parts in hessian_compositions(n):
        k = len(r_parts)
        for partition in ordered_set_partitions(labels, (s, *r_parts)):
            insertion_labels = partition[0]
            h_blocks = partition[1:]
            reflected_h_blocks = tuple(reversed(h_blocks))
            reflected_r_parts = tuple(reversed(r_parts))
            direct_id = term_id(n, insertion_labels, h_blocks)
            reflected_id = term_id(n, insertion_labels, reflected_h_blocks)
            direct_vertices = [rendered_vertex("I", s, insertion_labels)]
            direct_vertices.extend(
                rendered_vertex("H", r, block)
                for r, block in zip(r_parts, h_blocks, strict=True)
            )
            reflected_vertices = [rendered_vertex("I", s, insertion_labels)]
            reflected_vertices.extend(
                rendered_vertex("H", r, block)
                for r, block in zip(reflected_r_parts, reflected_h_blocks, strict=True)
            )
            rows.append(
                {
                    "term_id": direct_id,
                    "background_order": n,
                    "s": s,
                    "r_parts": list(r_parts),
                    "k": k,
                    "neumann_sign": (-1) ** k,
                    "overall_rational_coefficient": {
                        "numerator": (-1) ** k,
                        "denominator": 2,
                    },
                    "insertion_background_labels": list(insertion_labels),
                    "hessian_background_label_blocks": [list(block) for block in h_blocks],
                    "rooted_operator_tokens": rooted_word_tokens(s, r_parts),
                    "rooted_decorated_vertices": direct_vertices,
                    "cyclic_root": f"I_{s}",
                    "orientation": "ROOTED_DIRECTED_CYCLE",
                    "reflection": {
                        "term_id": reflected_id,
                        "r_parts": list(reflected_r_parts),
                        "hessian_background_label_blocks": [
                            list(block) for block in reflected_h_blocks
                        ],
                        "rooted_decorated_vertices": reflected_vertices,
                        "relation": (
                            "SELF_REFLECTED"
                            if direct_id == reflected_id
                            else "FORMAL_REVERSE_PAIR"
                        ),
                        "sign_claim": "NO_REFLECTION_SIGN_ASSIGNED",
                    },
                    "typed_path_template_set": f"K{k}",
                    "classification": "ABSTRACT_ROOTED_ONE_LOOP_WORD",
                }
            )
    return rows


def source_block_support() -> list[dict[str, object]]:
    """Derive source-Hessian block support from the pure-vector grammar."""

    rows: list[dict[str, object]] = []
    for row_block in GAUSSIAN_BLOCKS:
        for column_block in GAUSSIAN_BLOCKS:
            vector_vector = row_block.block_id == column_block.block_id == "V"
            rows.append(
                {
                    "row_block": row_block.block_id,
                    "column_block": column_block.block_id,
                    "status": (
                        "FORMALLY_ADMITTED_I_s_BLOCK_VALUE_NOT_DERIVED"
                        if vector_vector
                        else "PROVED_ZERO_BY_PURE_VECTOR_FREE_FIELD_SUPPORT"
                    ),
                    "proof": (
                        "I_s is the second quantum derivative of the pure-vector "
                        "source grammar; a derivative with respect to a carrier "
                        "outside {V} is zero"
                        if not vector_vector
                        else "both quantum derivatives are with respect to V"
                    ),
                }
            )
    return rows


def typed_path_templates(max_k: int = 4) -> dict[str, list[dict[str, object]]]:
    """Enumerate block paths for a vector-supported distinguished insertion.

    For ``k`` Hessian vertices, the insertion fixes the initial and final block
    to ``V``.  The ``k-1`` intermediate Gaussian blocks are enumerated without
    importing any interaction vertex.  Since every ``H_r[V^r]`` is even, a
    parity-changing transition is rejected; every remaining transition stays
    unresolved until an ordered Project Hessian vertex is derived.
    """

    result: dict[str, list[dict[str, object]]] = {}
    for k in range(max_k + 1):
        paths: list[dict[str, object]] = []
        intermediate_products = product(BLOCK_IDS, repeat=max(0, k - 1))
        for intermediates in intermediate_products:
            h_path = ("V", *intermediates, "V") if k else ("V",)
            transitions: list[dict[str, object]] = []
            for index in range(k):
                left = BLOCK_BY_ID[h_path[index]]
                right = BLOCK_BY_ID[h_path[index + 1]]
                parity_compatible = left.grassmann_parity == right.grassmann_parity
                transitions.append(
                    {
                        "hessian_slot": index + 1,
                        "row_block": left.block_id,
                        "column_block": right.block_id,
                        "row_parity": left.grassmann_parity,
                        "column_parity": right.grassmann_parity,
                        "parity_compatible": parity_compatible,
                        "status": (
                            "H_BLOCK_VALUE_UNRESOLVED"
                            if parity_compatible
                            else "PROVED_ZERO_BY_EVEN_HESSIAN_PARITY"
                        ),
                    }
                )
            parity_valid = all(
                transition["parity_compatible"] for transition in transitions
            )
            paths.append(
                {
                    "path_id": f"K{k}__" + "__".join(h_path),
                    "k": k,
                    "source_insertion_block": {"row_block": "V", "column_block": "V"},
                    "hessian_block_path": list(h_path),
                    "hessian_transitions": transitions,
                    "root_supertrace_weight": BLOCK_BY_ID["V"].supertrace_weight,
                    "valid_under_even_hessian_parity": parity_valid,
                    "nonzero_status": (
                        "UNRESOLVED_H_BLOCK_VALUES"
                        if parity_valid
                        else "REJECTED_BY_GRADED_BLOCK_PARITY"
                    ),
                }
            )
        result[f"K{k}"] = paths
    return result


def counterterm_rows() -> list[dict[str, object]]:
    return [
        {
            "counterterm_id": f"CT_{n}",
            "background_order": n,
            "background_labels": list(range(1, n + 1)),
            "coefficient": "UNRESOLVED_LOCAL_COUNTERTERM_COEFFICIENT",
            "classification": "INDEPENDENT_ADDITIVE_LOCAL_COUNTERTERM",
            "included_in_hessian_neumann_sum": False,
        }
        for n in (2, 3, 4)
    ]


def canonical_json(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


def build_payload() -> dict[str, object]:
    terms_by_order = {str(n): labeled_term_rows(n) for n in (2, 3, 4)}
    paths = typed_path_templates(max_k=4)
    source_support = source_block_support()
    family_counts = {str(n): len(hessian_compositions(n)) for n in (2, 3, 4)}
    polarized_counts = {str(n): len(terms_by_order[str(n)]) for n in (2, 3, 4)}
    term_ids_by_order = {
        str(n): {row["term_id"] for row in terms_by_order[str(n)]} for n in (2, 3, 4)
    }

    reflection_involution = True
    for n in (2, 3, 4):
        rows_by_id = {row["term_id"]: row for row in terms_by_order[str(n)]}
        for row in terms_by_order[str(n)]:
            reflected_id = row["reflection"]["term_id"]
            if reflected_id not in term_ids_by_order[str(n)]:
                reflection_involution = False
                break
            if rows_by_id[reflected_id]["reflection"]["term_id"] != row["term_id"]:
                reflection_involution = False
                break

    n2_unpolarized = {
        (row["s"], tuple(row["r_parts"]), row["neumann_sign"])
        for row in terms_by_order["2"]
    }
    expected_n2 = {
        (0, (1, 1), 1),
        (0, (2,), -1),
        (1, (1,), -1),
        (2, (), 1),
    }
    absent_source_rows = [
        row
        for row in source_support
        if row["status"] == "PROVED_ZERO_BY_PURE_VECTOR_FREE_FIELD_SUPPORT"
    ]
    checks = {
        "family_counts_are_2_power_n": family_counts == {"2": 4, "3": 8, "4": 16},
        "polarized_counts_are_exact": polarized_counts == {"2": 6, "3": 26, "4": 150},
        "n2_has_exact_four_neumann_families_and_signs": n2_unpolarized == expected_n2,
        "every_partition_exhausts_each_label_once": all(
            sorted(
                row["insertion_background_labels"]
                + [
                    label
                    for block in row["hessian_background_label_blocks"]
                    for label in block
                ]
            )
            == list(range(1, n + 1))
            for n in (2, 3, 4)
            for row in terms_by_order[str(n)]
        ),
        "reflection_is_an_involution_without_quotient": reflection_involution,
        "source_support_has_one_admitted_and_35_proved_zero_blocks": len(source_support) == 36
        and len(absent_source_rows) == 35
        and sum(
            row["status"] == "FORMALLY_ADMITTED_I_s_BLOCK_VALUE_NOT_DERIVED"
            for row in source_support
        )
        == 1,
        "typed_path_template_counts_are_exact": {
            key: len(value) for key, value in paths.items()
        }
        == {"K0": 1, "K1": 1, "K2": 6, "K3": 36, "K4": 216},
        "fp_block_is_graded_and_present_in_registry": BLOCK_BY_ID["FP"].grassmann_parity == 1
        and BLOCK_BY_ID["FP"].supertrace_weight == -1,
        "three_adjoint_chiral_pairs_are_distinct": sum(
            block.sector == "PHYSICAL_ADJOINT_CHIRAL_PAIR" for block in GAUSSIAN_BLOCKS
        )
        == 3,
        "ct_2_ct_3_ct_4_are_retained": [
            row["counterterm_id"] for row in counterterm_rows()
        ]
        == ["CT_2", "CT_3", "CT_4"],
    }
    unresolved_obligations = [
        {
            "id": "SOURCE_PARTNER_AND_MEASURE",
            "status": "BLOCKED_UNFIXED_SOURCE_MULTIPLET",
            "effect": "the parity, chirality, projector, dimension, R-weight, and integration measure of the source partner are not fixed",
        },
        {
            "id": "GRADED_CYCLIC_SOURCE_SIGN",
            "status": "BLOCKED_UNFIXED_SOURCE_KERNEL_PARITY",
            "effect": "only the Neumann sign (-1)^k is accepted; no additional cyclic or reflection Koszul sign is assigned",
        },
        {
            "id": "FUNCTIONAL_HESSIAN_JACOBIAN",
            "status": "BLOCKED_UNPROVED_REGULATED_BEREZINIAN",
            "effect": "the abstract STr census does not prove equality of vector/chiral frames or a finite-BV density",
        },
        {
            "id": "ORDERED_HESSIAN_BLOCK_VALUES",
            "status": "BLOCKED_UNDERIVED_PROJECT_VERTICES",
            "effect": "parity-compatible typed paths are candidates, not nonzero graphs",
        },
        {
            "id": "COUNTERTERM_COEFFICIENTS",
            "status": "BLOCKED_UNFIXED_RENORMALIZATION_CONDITIONS",
            "effect": "CT_n is retained independently at n=2,3,4",
        },
    ]
    return {
        "schema": "Step5OneLoopHessianInsertionCensus.v1",
        "status": "PASS_COMBINATORICS_FAIL_CLOSED_PHYSICS"
        if all(checks.values())
        else "FAIL",
        "scope": "ABSTRACT_ONE_LOOP_HESSIAN_SOURCE_INSERTION_N_2_3_4",
        "formal_generator": {
            "hessian": "H[J,V]=H0+sum_(r>=1)H_r[V^r]+J sum_(s>=0)I_s[V^s]",
            "one_loop_insertion": "Gamma_I^(1)=(1/2)STr(H^{-1}I)",
            "coefficient_rule": "s+r1+...+rk=n; coefficient=(1/2)(-1)^k",
            "rooted_word": "STr[G0 I_s (G0 H_r1)...(G0 H_rk)]",
        },
        "enumeration_policy": {
            "cyclic_action": "the unique I_s is distinguished and fixes the cyclic root",
            "reflection_action": "reverse the ordered H blocks; retain as metadata and do not quotient or add a second summand",
            "background_labels": "{1,...,n} is partitioned into one insertion set and an ordered list of Hessian sets",
            "internal_order": "each background-label block is a set stored in increasing order",
            "operator_values": "not evaluated",
        },
        "gaussian_blocks": [asdict(block) for block in GAUSSIAN_BLOCKS],
        "pure_vector_insertion_grammar": {
            "free_quantum_field_support": ["V"],
            "source_block_support": source_support,
            "absence_policy": "a source block is absent only when a quantum derivative acts on a carrier outside {V}",
        },
        "typed_path_templates": paths,
        "family_counts": family_counts,
        "polarized_term_counts": polarized_counts,
        "terms_by_background_order": terms_by_order,
        "counterterms": counterterm_rows(),
        "checks": checks,
        "unresolved_obligations": unresolved_obligations,
        "result": "EXACT_ABSTRACT_CENSUS_ONLY; NO_FIELD_THEORY_AMPLITUDE_OR_COEFFICIENT_ACCEPTED",
        "external_results_imported": False,
    }


def write_artifacts() -> None:
    payload = build_payload()
    generated_bytes = canonical_json(payload)
    audit = {
        "schema": "Step5OneLoopHessianInsertionCensusAudit.v1",
        "status": payload["status"],
        "scope": payload["scope"],
        "totals": {
            "checks": len(payload["checks"]),
            "failed": sum(not value for value in payload["checks"].values()),
            "families": sum(payload["family_counts"].values()),
            "polarized_terms": sum(payload["polarized_term_counts"].values()),
            "typed_path_templates": sum(
                len(rows) for rows in payload["typed_path_templates"].values()
            ),
            "source_block_rows": len(
                payload["pure_vector_insertion_grammar"]["source_block_support"]
            ),
            "counterterms": len(payload["counterterms"]),
            "unresolved_obligations": len(payload["unresolved_obligations"]),
        },
        "generated_sha256": hashlib.sha256(generated_bytes).hexdigest(),
        "result": payload["result"],
    }
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    GENERATED.write_bytes(generated_bytes)
    AUDIT.write_bytes(canonical_json(audit))


if __name__ == "__main__":
    write_artifacts()
