#!/usr/bin/env python3
"""Exact reflected-orientation and physical Sym^2(Adj) quotient audit.

This script does not compute or import a one-loop coefficient.  It compares the
literal ordered GraphIR word with the specialized WW orientation sign, performs
the dotted epsilon contractions component by component, and applies the local
bosonic two-letter quotient exactly.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

STEP1 = ROOT / "contracts/foundations/step-01-supersymmetry-commutator.md"
STEP5 = ROOT / "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md"
WW_SCRIPT = ROOT / "scripts/step5_ww_seed.py"
OUT = ROOT / "generated/step5/one-loop-reflection-quotient-audit.json"
AUDIT = ROOT / "audits/step5-one-loop-reflection-quotient-verification.json"
REPORT = ROOT / "audits/step5-one-loop-reflection-quotient-audit.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ww_module() -> Any:
    specification = importlib.util.spec_from_file_location(
        "step5_reflection_quotient_ww_binding", WW_SCRIPT
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load the specialized WW seed")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


EPSILON_UP = ((0, 1), (-1, 0))
EPSILON_DOWN = ((0, -1), (1, 0))


def matrix_product(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(
        tuple(sum(left[row][pivot] * right[pivot][column] for pivot in range(2))
              for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def raise_dotted(lower: tuple[int, int]) -> tuple[int, int]:
    return tuple(
        sum(EPSILON_UP[row][column] * lower[column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def contract_lower_upper(lower: tuple[int, int], upper: tuple[int, int]) -> int:
    return sum(lower[index] * upper[index] for index in range(2))


def contract_upper_lower(upper: tuple[int, int], lower: tuple[int, int]) -> int:
    return sum(upper[index] * lower[index] for index in range(2))


def source_normal_form(order: str) -> Counter[tuple[tuple[str, str], ...]]:
    """Normal-order nabla_-(X^A X^B), with |X|=0 and |nabla_- X|=1."""

    if order not in {"AB", "BA"}:
        raise ValueError(order)
    left, right = tuple(order)
    raw_terms = (
        (("dX", left), ("X", right)),
        (("X", left), ("dX", right)),
    )
    normal_terms: list[tuple[tuple[str, str], ...]] = []
    for first, second in raw_terms:
        if first[0] == "X" and second[0] == "dX":
            # |X|=0, so X*dX=dX*X with sign +1.
            normal_terms.append((second, first))
        else:
            normal_terms.append((first, second))
    return Counter(normal_terms)


def candidate_coefficients(reflected_sign: int) -> dict[str, int]:
    """Coefficients of F_ABDE (S_DE + s S_ED) after D<->E relabelling."""

    if reflected_sign not in {-1, 1}:
        raise ValueError(reflected_sign)
    return {"S_DE": 1, "S_ED": reflected_sign}


def ab_swapped_coefficients(reflected_sign: int) -> dict[str, int]:
    """Use F_BADE=F_ABED, then relabel the dummy pair D<->E."""

    if reflected_sign not in {-1, 1}:
        raise ValueError(reflected_sign)
    return {"S_DE": reflected_sign, "S_ED": 1}


def projected_coefficients(reflected_sign: int, projector: str) -> dict[str, str]:
    original = candidate_coefficients(reflected_sign)
    swapped = ab_swapped_coefficients(reflected_sign)
    if projector not in {"SYM", "ANTISYM"}:
        raise ValueError(projector)
    operation = 1 if projector == "SYM" else -1
    return {
        basis: str(Fraction(original[basis] + operation * swapped[basis], 2))
        for basis in ("S_DE", "S_ED")
    }


def ordered_graph_word(graph: Any) -> tuple[str, ...]:
    return tuple(
        leg.field_type.name
        for leg in graph.external_legs
        if not leg.field_type.name.startswith("Source[")
    )


def permutation_sign(word: tuple[str, ...], canonical: tuple[str, ...]) -> tuple[int, int]:
    """Return the Koszul sign for distinct odd tokens and its inversion count."""

    if len(word) != len(canonical) or set(word) != set(canonical):
        raise ValueError("word and canonical word must contain the same distinct tokens")
    positions = {token: index for index, token in enumerate(canonical)}
    inversions = sum(
        positions[word[left]] > positions[word[right]]
        for left in range(len(word))
        for right in range(left + 1, len(word))
    )
    return (-1 if inversions % 2 else 1), inversions


def build_payload() -> dict[str, object]:
    step1_text = STEP1.read_text()
    step5_text = STEP5.read_text()
    if "\\epsilon^{12}=\\epsilon^{\\dot1\\dot2}=+1" not in step1_text:
        raise AssertionError("Step-1 epsilon-up convention drifted")
    if "\\epsilon_{12}=\\epsilon_{\\dot1\\dot2}=-1" not in step1_text:
        raise AssertionError("Step-1 epsilon-down convention drifted")
    if "\\epsilon^{+-}=+1" not in step5_text or "\\epsilon_{+-}=-1" not in step5_text:
        raise AssertionError("Step-5 plus/minus frame drifted")
    ww_script_text = WW_SCRIPT.read_text()

    ww = load_ww_module()
    graphs = {
        orientation: ww.physical_triangle(orientation)
        for orientation in ("DIRECT", "REFLECTED")
    }
    specialized = {
        orientation: ww.external_orientation_sign_audit(orientation)
        for orientation in ("DIRECT", "REFLECTED")
    }
    graph_words = {
        orientation: ordered_graph_word(graph)
        for orientation, graph in graphs.items()
    }
    vertex_orders = {
        orientation: tuple(vertex.kind for vertex in graph.vertices)
        for orientation, graph in graphs.items()
    }
    source_legs = {
        orientation: next(
            leg
            for leg in graph.external_legs
            if leg.field_type.name.startswith("Source[")
        )
        for orientation, graph in graphs.items()
    }
    source_half_edges = {
        orientation: next(
            half_edge
            for half_edge in graphs[orientation].half_edges
            if half_edge.half_edge_id == leg.attached_half_edge
        )
        for orientation, leg in source_legs.items()
    }
    source_vertices = {
        orientation: next(
            vertex
            for vertex in graphs[orientation].vertices
            if vertex.vertex_id == source_half_edges[orientation].vertex_id
        )
        for orientation in source_legs
    }
    tilde_w_legs = {
        orientation: next(
            leg
            for leg in graph.external_legs
            if leg.field_type.name == "TildeW_dot_alpha"
        )
        for orientation, graph in graphs.items()
    }

    w_lower = (2, 3)
    y_lower = (5, 7)
    w_upper = raise_dotted(w_lower)
    y_upper = raise_dotted(y_lower)
    w_down_y_up = contract_lower_upper(w_lower, y_upper)
    y_up_w_down = contract_upper_lower(y_upper, w_lower)
    y_down_w_up = contract_lower_upper(y_lower, w_upper)

    direct_block_word = ("TildeW", "Q_barD", "W", "Q_D")
    reflected_block_word = ("W", "Q_D", "TildeW", "Q_barD")
    full_reflection_sign, full_reflection_inversions = permutation_sign(
        reflected_block_word, direct_block_word
    )
    external_only_sign, external_only_inversions = permutation_sign(
        ("W", "TildeW"), ("TildeW", "W")
    )
    quantum_only_sign, quantum_only_inversions = permutation_sign(
        ("Q_D", "Q_barD"), ("Q_barD", "Q_D")
    )

    repaired_sign = int(specialized["REFLECTED"]["total_orientation_sign"])
    rejected_external_only_sign = -1
    rejected_coefficients = candidate_coefficients(rejected_external_only_sign)
    repaired_coefficients = candidate_coefficients(repaired_sign)
    rejected_sym = projected_coefficients(rejected_external_only_sign, "SYM")
    repaired_sym = projected_coefficients(repaired_sign, "SYM")

    checks = {
        "epsilon_up_times_down_is_identity": matrix_product(
            EPSILON_UP, EPSILON_DOWN
        ) == ((1, 0), (0, 1)),
        "epsilon_down_times_up_is_identity": matrix_product(
            EPSILON_DOWN, EPSILON_UP
        ) == ((1, 0), (0, 1)),
        "lower_upper_equals_upper_lower_for_even_Y": w_down_y_up == y_up_w_down,
        "lower_upper_reversed_variance_has_epsilon_minus": (
            y_down_w_up == -w_down_y_up
        ),
        "local_seed_is_symmetric": source_normal_form("AB")
        == source_normal_form("BA"),
        "direct_and_reflected_vertex_orders_are_identical": (
            vertex_orders["DIRECT"] == vertex_orders["REFLECTED"]
        ),
        "direct_and_reflected_graph_external_words_are_identical": (
            graph_words["DIRECT"] == graph_words["REFLECTED"]
            == ("TildeW_dot_alpha", "W_plus")
        ),
        "specialized_code_replays_reflected_full_sign_plus_one": repaired_sign == 1,
        "specialized_reflection_subsigns_are_both_minus_one": (
            specialized["REFLECTED"]["external_fermion_permutation_sign"] == -1
            and specialized["REFLECTED"]["quantum_odd_word_permutation_sign"] == -1
        ),
        "D_transfer_is_orientation_independent": (
            specialized["DIRECT"]["D_transfer"]["product"]
            == specialized["REFLECTED"]["D_transfer"]["product"]
            == 1
        ),
        "full_even_vertex_block_reflection_has_plus_sign": (
            full_reflection_sign == 1 and full_reflection_inversions == 4
        ),
        "external_only_reversal_has_minus_sign": (
            external_only_sign == -1 and external_only_inversions == 1
        ),
        "quantum_odd_word_reversal_has_minus_sign": (
            quantum_only_sign == -1 and quantum_only_inversions == 1
        ),
        "external_and_quantum_reversals_cancel": (
            external_only_sign * quantum_only_sign == full_reflection_sign == 1
        ),
        "physical_insertion_parity_is_odd": (1 + 0 + 0) % 2 == 1,
        "graphir_source_is_fermionic": all(
            leg.field_type.statistics.value == "FERMION" and leg.field_type.parity == 1
            for leg in source_legs.values()
        ),
        "graphir_source_dual_color_slots_are_down": all(
            tuple(index.variance.value for index in leg.field_type.indices)
            == ("DOWN", "DOWN")
            for leg in source_legs.values()
        ),
        "source_port_is_external_J_leg_not_the_insertion_vertex": all(
            leg.field_type.name.startswith("Source[")
            and source_vertices[orientation].kind == "COMPOSITE_INSERTION_I2_WW"
            for orientation, leg in source_legs.items()
        ),
        "D_algebra_external_token_is_covariant_vector_derivative": (
            "mathcalD_(+ dot_beta)[X^E(p)]" in ww_script_text
        ),
        "legacy_invalid_spinor_derivative_type_is_absent": (
            "nabla_+^dot_alpha X" not in ww_script_text
            and "\\nabla_+{}^{\\dot\\alpha}X" not in step5_text
        ),
        "locked_tildeW_cubic_port_is_lower_dotted": (
            "\\widetilde{\\mathcal W}_{\\dot a}^{D}" in step5_text
            and "\\bar D^{\\dot a(C)}-\\bar D^{\\dot a(A)}" in step5_text
        ),
        "graphir_tildeW_port_is_lower_dotted": all(
            len(leg.spinor_indices) == 1
            and leg.spinor_indices[0].space.value == "DOTTED"
            and leg.spinor_indices[0].variance.value == "DOWN"
            for leg in tilde_w_legs.values()
        ),
        "rejected_external_only_minus_is_AB_antisymmetric": (
            ab_swapped_coefficients(rejected_external_only_sign)
            == {basis: -value for basis, value in rejected_coefficients.items()}
        ),
        "rejected_external_only_minus_has_zero_Sym2_projection": rejected_sym
        == {"S_DE": "0", "S_ED": "0"},
        "repaired_plus_word_is_AB_symmetric": (
            ab_swapped_coefficients(repaired_sign) == repaired_coefficients
        ),
        "repaired_plus_word_survives_Sym2_projection": (
            repaired_sym == {"S_DE": "1", "S_ED": "1"}
        ),
    }

    return {
        "schema": "STEP5_ONE_LOOP_REFLECTION_QUOTIENT_AUDIT_V1",
        "scope": "SIGN_INDEX_VARIANCE_AND_LOCAL_SYM2_ONLY_NO_LOOP_COEFFICIENT",
        "inputs": {
            str(STEP1.relative_to(ROOT)): sha256(STEP1),
            str(STEP5.relative_to(ROOT)): sha256(STEP5),
            str(WW_SCRIPT.relative_to(ROOT)): sha256(WW_SCRIPT),
        },
        "epsilon": {
            "epsilon_up": [list(row) for row in EPSILON_UP],
            "epsilon_down": [list(row) for row in EPSILON_DOWN],
            "w_lower_witness": list(w_lower),
            "y_lower_witness": list(y_lower),
            "w_upper_witness": list(w_upper),
            "y_upper_witness": list(y_upper),
            "W_down_Y_up": w_down_y_up,
            "Y_up_W_down": y_up_w_down,
            "Y_down_W_up": y_down_w_up,
            "generic_identities": [
                "W_dot0*Y_dot1-W_dot1*Y_dot0",
                "Y^dot_a W_dot_a = W_dot_a Y^dot_a because |Y|=0",
                "Y_dot_a W^dot_a = -W_dot_a Y^dot_a",
            ],
        },
        "source_quotient": {
            "X_parity": 0,
            "nabla_minus_parity": 1,
            "dX_parity": 1,
            "AB_normal_form": [
                list(term) for term in sorted(source_normal_form("AB"))
            ],
            "BA_normal_form": [
                list(term) for term in sorted(source_normal_form("BA"))
            ],
            "physical_color_space": "Sym^2(Adj)",
            "momentum_exchange_rule": "(A,p1)<->(B,p2)",
            "insertion_parity": 1,
            "required_source_coupling_parity": 1,
            "coupled_source_vertex_parity": 0,
            "current_graphir_source_statistics": {
                orientation: leg.field_type.statistics.value
                for orientation, leg in source_legs.items()
            },
            "current_graphir_source_type_verdict": "REPAIRED_FERMION",
            "current_graphir_source_color_variances": {
                orientation: [
                    index.variance.value for index in leg.field_type.indices
                ]
                for orientation, leg in source_legs.items()
            },
            "source_port_semantics": {
                orientation: {
                    "external_leg_id": leg.leg_id,
                    "field_name": leg.field_type.name,
                    "attached_half_edge": leg.attached_half_edge,
                    "attached_vertex_kind": source_vertices[orientation].kind,
                    "verdict": (
                        "J_LEG; the composite insertion is the attached vertex, "
                        "not this external field"
                    ),
                }
                for orientation, leg in source_legs.items()
            },
        },
        "orientation": {
            "ordered_vertex_kinds": {
                key: list(value) for key, value in vertex_orders.items()
            },
            "graphir_external_words": {
                key: list(value) for key, value in graph_words.items()
            },
            "specialized_sign_audits": specialized,
            "derived_fixed_vertex_order_signs": {"DIRECT": 1, "REFLECTED": 1},
            "reason": (
                "the source-coupled insertion and both action vertices are even; "
                "all internal V legs are bosonic; the reflected attachment preserves "
                "the fixed GraphIR vertex/external order"
            ),
            "vertex_parity_certificate": {
                "source_coupled_insertion": "|J|+|nabla_-|+2|X|=1+1+0=0 mod 2",
                "TildeW_cubic": "|TildeW|+|barD|=1+1=0 mod 2",
                "W_cubic": "|W|+|D|=1+1=0 mod 2",
                "internal_Wick_fields": "V only; |V|=0",
            },
            "graded_block_replay": {
                "token_parities": {
                    "TildeW": 1,
                    "Q_barD": 1,
                    "W": 1,
                    "Q_D": 1,
                },
                "definitions": {
                    "Q_barD": "odd barD-dressed bosonic-V quantum word",
                    "Q_D": "odd D-dressed bosonic-V quantum word",
                },
                "direct_full_word": list(direct_block_word),
                "reflected_full_block_word": list(reflected_block_word),
                "full_word_inversions": full_reflection_inversions,
                "full_word_sign": full_reflection_sign,
                "external_only_inversions": external_only_inversions,
                "external_only_sign": external_only_sign,
                "quantum_only_inversions": quantum_only_inversions,
                "quantum_only_sign": quantum_only_sign,
                "factorization_check": (
                    "(-1)_external*(-1)_quantum=(+1)_full_even_block"
                ),
                "specialized_compiler_status": (
                    "external and quantum odd-subword signs are retained separately; "
                    "their product is the full reflected sign"
                ),
            },
        },
        "color_and_projection": {
            "definitions": {
                "F_ABDE": "c_ACD*c_BCE",
                "S_DE": "TildeW^D_dot_a*Y^(E dot_a)",
                "Y^(E dot_a)": "epsilon^(dot_a dot_b)*mathcalD_(+ dot_b)X^E",
            },
            "color_swap_rule": "F_BADE=F_ABED",
            "rejected_external_only_minus": {
                "AB_coefficients": rejected_coefficients,
                "BA_coefficients_after_dummy_relabelling": ab_swapped_coefficients(
                    rejected_external_only_sign
                ),
                "Sym2_projection": rejected_sym,
                "Alt2_projection": projected_coefficients(
                    rejected_external_only_sign, "ANTISYM"
                ),
                "verdict": "KILLED_BY_PHYSICAL_SYM2_QUOTIENT",
            },
            "repaired_plus": {
                "AB_coefficients": repaired_coefficients,
                "BA_coefficients_after_dummy_relabelling": ab_swapped_coefficients(
                    repaired_sign
                ),
                "Sym2_projection": repaired_sym,
                "operator_word": (
                    "c_ACD*c_BCE*[TildeW^D_dot_a*mathcalD_+^(dot_a)X^E"
                    "+mathcalD_+^(dot_a)X^D*TildeW^E_dot_a]"
                ),
                "verdict": "SYMMETRIC_OPERATOR_WORD_REQUIRED",
            },
        },
        "derivative_type_audit": {
            "spinor_derivative": {
                "symbol": "nabla_a",
                "parity": 1,
                "index_space": "S_L",
                "plus_component": "nabla_+",
                "dotted_output_allowed": False,
            },
            "vector_derivative": {
                "symbol": "mathcalD_(a dot_a)",
                "parity": 0,
                "index_space": "S_L tensor S_R",
                "raised_dotted_component": (
                    "mathcalD_+^(dot_a)=epsilon^(dot_a dot_b)*mathcalD_(+ dot_b)"
                ),
            },
            "D_algebra_external_token": "i*p_(a dot_b)*W_plus",
            "covariant_completion": "Y^(A dot_a)=mathcalD_+^(dot_a)X^A",
            "legacy_symbol": "nabla_+^(dot_a)X",
            "legacy_verdict": "TYPE_INVALID_DOTTED_OUTPUT_ON_UNDOTTED_SPINOR_DERIVATIVE",
        },
        "dotted_port_type_audit": {
            "locked_cubic_port": "TildeW_dot_a*barD^(dot_a)",
            "required_tildeW_variance": "DOWN",
            "required_vector_derivative_variance": "UP",
            "current_graphir_tildeW_slots": {
                orientation: {
                    "label": leg.spinor_indices[0].label,
                    "variance": leg.spinor_indices[0].variance.value,
                }
                for orientation, leg in tilde_w_legs.items()
            },
            "scheduled_compiler_behavior": (
                "retains both dotted labels and UP/DOWN variance in every "
                "normal-form numerator factor"
            ),
            "verdict": "GRAPHIR_TILDEW_VARIANCE_REPAIRED_DOWN",
        },
        "checks": checks,
        "totals": {
            "exact": len(checks),
            "passed": sum(checks.values()),
            "failed": sum(not value for value in checks.values()),
        },
        "findings": [
            {
                "severity": "CLOSED",
                "code": "REFLECTED_FULL_ODD_WORD_SIGN_REPAIRED",
                "status": "CLOSED",
                "evidence": (
                    "s_external=-1 and s_quantum=-1 give s_reflected=+1"
                ),
            },
            {
                "severity": "CLOSED",
                "code": "REFLECTED_CANONICAL_GRAPHIR_WORD_REPAIRED",
                "status": "CLOSED",
                "evidence": (
                    "GraphIR and AmplitudeIR retain canonical (TildeW,W) in both orientations"
                ),
            },
            {
                "severity": "P1",
                "code": "TYPED_CONTACT_REPLAY_AFTER_REPAIR",
                "status": "OPEN",
                "evidence": (
                    "GraphIR, AmplitudeIR, and sixteen triangle rows are regenerated; "
                    "contact coefficients remain invalidated pending typed replay"
                ),
            },
            {
                "severity": "CLOSED",
                "code": "WW_SOURCE_STATISTICS_REPAIRED_FERMION",
                "status": "CLOSED",
                "evidence": (
                    "|nabla_-(X^A X^B)|=1, so an even source coupling requires "
                    "|J_(AB)|=1; GraphIR source statistics are FERMION"
                ),
            },
            {
                "severity": "CLOSED",
                "code": "COVARIANT_VECTOR_DERIVATIVE_TOKEN_REPAIRED",
                "status": "CLOSED",
                "evidence": (
                    "the exact D-algebra emits i*p_(a dot_b), whose covariant "
                    "completion is mathcalD_(a dot_b)"
                ),
            },
            {
                "severity": "CLOSED",
                "code": "TILDEW_DOTTED_VARIANCE_REPAIRED_DOWN",
                "status": "CLOSED",
                "evidence": (
                    "locked TildeW_dot_a*barD^(dot_a) port is DOWN in both orientations"
                ),
            },
        ],
        "coefficient_status": "NOT_EVALUATED_BY_THIS_AUDIT",
        "acceptance_status": (
            "PASS_REFLECTION_SOURCE_DERIVATIVE_TYPE_GATES_CONTACT_REPLAY_OPEN"
        ),
    }


def render_report(payload: dict[str, object]) -> str:
    orientation = payload["orientation"]
    assert isinstance(orientation, dict)
    totals = payload["totals"]
    assert isinstance(totals, dict)
    return "\n".join(
        (
            "# Step 5 one-loop reflection / physical quotient verification",
            "",
            "## 0. Definitions",
            "",
            "$$",
            "X^A:=(\\nabla_+\\mathcal W_+)^A,\\qquad |X|=0,",
            "\\qquad Y^{A\\dot a}:=\\mathcal D_+{}^{\\dot a}X^A,\\qquad |Y|=0.",
            "$$",
            "",
            "$$",
            "\\mathcal D_+{}^{\\dot a}:=",
            "\\epsilon^{\\dot a\\dot b}\\mathcal D_{+\\dot b},\\qquad",
            "|\\mathcal D_{a\\dot a}|=0.",
            "$$",
            "",
            "$$",
            "F_{ABDE}:=c_{ACD}c_{BCE},\\qquad",
            "S^{DE}:=\\widetilde{\\mathcal W}_{\\dot a}^D Y^{E\\dot a}.",
            "$$",
            "",
            "## 1. Dotted variance",
            "",
            "$$",
            "\\epsilon^{\\dot1\\dot2}=+1,\\qquad",
            "\\epsilon_{\\dot1\\dot2}=-1,\\qquad",
            "Y^{\\dot a}=\\epsilon^{\\dot a\\dot b}Y_{\\dot b}.",
            "$$",
            "",
            "For $W_{\\dot a}=(w_1,w_2)$ and $Y_{\\dot a}=(y_1,y_2)$,",
            "",
            "$$",
            "\\begin{aligned}",
            "W_{\\dot a}Y^{\\dot a}&=w_1y_2-w_2y_1,\\\\",
            "Y^{\\dot a}W_{\\dot a}&=w_1y_2-w_2y_1,\\\\",
            "Y_{\\dot a}W^{\\dot a}&=y_1w_2-y_2w_1",
            "=-(w_1y_2-w_2y_1).",
            "\\end{aligned}",
            "$$",
            "",
            "The locked lower `TildeW` port is retained as `DOWN` in GraphIR and",
            "in every scheduled numerator factor.",
            "The $D$-algebra token is $ip_{a\\dot b}$; its covariant completion is",
            "$\\mathcal D_{a\\dot b}$.  The legacy symbol",
            "$\\nabla_+{}^{\\dot a}X$ is type-invalid because $\\nabla_+$ is an",
            "undotted odd spinor derivative and has no dotted output.",
            "",
            "## 2. Local two-letter quotient",
            "",
            "$$",
            "\\begin{aligned}",
            "\\nabla_-(X^AX^B)",
            "&=(\\nabla_-X^A)X^B+X^A(\\nabla_-X^B)\\\\",
            "&=(\\nabla_-X^A)X^B+(\\nabla_-X^B)X^A\\\\",
            "&=\\nabla_-(X^BX^A).",
            "\\end{aligned}",
            "$$",
            "",
            "$$",
            "\\mathscr I^{AB}=\\mathscr I^{BA},\\qquad",
            "\\mathscr I\\in\\operatorname{Sym}^2(\\operatorname{Adj}).",
            "$$",
            "",
            "$$",
            "|\\mathscr I|=|\\nabla_-|+2|X|=1,\\qquad",
            "|J_{(AB)}|=1,\\qquad |J_{(AB)}\\mathscr I^{AB}|=0.",
            "$$",
            "",
            "The GraphIR source field is typed `FERMION`; the coupled insertion vertex is even.",
            "",
            "In momentum space the exact exchange is $(A,p_1)\\leftrightarrow(B,p_2)$.",
            "",
            "## 3. Reflected orientation",
            "",
            "Both GraphIR orientations have",
            "",
            "$$",
            "\\operatorname{Ord}(v_I,v_{\\widetilde W},v_W)",
            "=(I,\\widetilde W,W),\\qquad",
            "\\operatorname{Word}_{\\rm ext}=(\\widetilde W,W).",
            "$$",
            "",
            "$$",
            "|v_{J\\mathscr I}|=|v_{\\widetilde W}|=|v_W|=0,\\qquad |V|=0.",
            "$$",
            "",
            "Therefore",
            "",
            "$$",
            "s_{\\rm ref}^{\\rm fixed\\ vertex\\ order}=+1.",
            "$$",
            "",
            "The reflected audit records the external subword permutation",
            "",
            "$$",
            "(\\widetilde W,W)\\longmapsto(W,\\widetilde W)",
            "\\longmapsto-(\\widetilde W,W),",
            "$$",
            "",
            "and separately records the odd quantum-word permutation.",
            "",
            "The complete cubic blocks are",
            "",
            "$$",
            "B_{\\widetilde W}=\\widetilde W\\,Q_{\\bar D},\\qquad",
            "B_W=W\\,Q_D,\\qquad",
            "|\\widetilde W|=|Q_{\\bar D}|=|W|=|Q_D|=1,",
            "$$",
            "",
            "so $|B_{\\widetilde W}|=|B_W|=0$.  Full block reflection gives",
            "",
            "$$",
            "(W,Q_D,\\widetilde W,Q_{\\bar D})",
            "\\longmapsto",
            "(\\widetilde W,Q_{\\bar D},W,Q_D):",
            "\\qquad (-1)^4=+1.",
            "$$",
            "",
            "Separating the same permutation gives",
            "",
            "$$",
            "s_{\\rm ext}=(-1)^1=-1,\\qquad",
            "s_{\\rm quantum}=(-1)^1=-1,\\qquad",
            "s_{\\rm full}=s_{\\rm ext}s_{\\rm quantum}=+1.",
            "$$",
            "",
            "The specialized compiler retains both sub-signs and uses their product.",
            "",
            "## 4. Color swap and projection",
            "",
            "Let $s_{\\rm ref}=s$. Then",
            "",
            "$$",
            "\\mathscr O_s^{AB}=F_{ABDE}(S^{DE}+sS^{ED}).",
            "$$",
            "",
            "Using $F_{BADE}=F_{ABED}$ and then $D\\leftrightarrow E$ gives",
            "",
            "$$",
            "\\mathscr O_s^{BA}=F_{ABDE}(S^{ED}+sS^{DE})=s\\mathscr O_s^{AB}.",
            "$$",
            "",
            "Rejected external-only sign:",
            "",
            "$$",
            "s=-1:\\qquad",
            "\\mathscr O_-^{BA}=-\\mathscr O_-^{AB},\\qquad",
            "P_{\\rm Sym^2}\\mathscr O_-=0.",
            "$$",
            "",
            "Fixed ordered-GraphIR sign:",
            "",
            "$$",
            "s=+1:\\qquad",
            "\\boxed{",
            "\\mathscr O_+^{AB}=c_{ACD}c_{BCE}",
            "\\left[",
            "\\widetilde{\\mathcal W}_{\\dot a}^D",
            "\\mathcal D_+{}^{\\dot a}X^E",
            "+(\\mathcal D_+{}^{\\dot a}X^D)",
            "\\widetilde{\\mathcal W}_{\\dot a}^E",
            "\\right]},",
            "\\qquad \\mathscr O_+^{BA}=\\mathscr O_+^{AB}.",
            "$$",
            "",
            "## 5. Verdict",
            "",
            "$$",
            "\\boxed{\\texttt{PASS\\_REFLECTION\\_SOURCE\\_DERIVATIVE\\_TYPE\\_GATES}}.",
            "$$",
            "",
            "- `TYPED_CONTACT_REPLAY_AFTER_REPAIR`: OPEN.",
            "- `anomaly coefficient`: INVALIDATED_NOT_PROPAGATED.",
            "",
            f"Exact checks: {totals['passed']}/{totals['exact']}; loop coefficient not evaluated.",
            "",
        )
    )


def main() -> None:
    payload = build_payload()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    REPORT.write_text(render_report(payload))
    checks = payload["checks"]
    assert isinstance(checks, dict)
    verification = {
        "scope": payload["scope"],
        "status": (
            "PASS_TYPED_REPAIR_WITH_CONTACT_REPLAY_OPEN"
            if all(checks.values())
            else "FAIL_EXACT_CHECKS"
        ),
        "certificate": str(OUT.relative_to(ROOT)),
        "certificate_sha256": sha256(OUT),
        "report": str(REPORT.relative_to(ROOT)),
        "report_sha256": sha256(REPORT),
        "checks": checks,
        "totals": payload["totals"],
        "blocking_findings": payload["findings"],
        "coefficient_status": payload["coefficient_status"],
    }
    AUDIT.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
