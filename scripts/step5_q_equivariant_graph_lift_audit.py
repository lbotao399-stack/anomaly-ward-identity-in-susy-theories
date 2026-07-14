#!/usr/bin/env python3
"""Target-blind audit of the proposed residual-q lift of Step-5 graph rows.

The audit separates two statements which must not be conflated:

1. the nine physical external letters are exact coefficient projections of a
   conditional compact U-complex, and therefore give 81 exact ordered
   component projectors with explicit Koszul signs;
2. the canonical WW triangle/cut graph has a raw q-equivariant lift to those
   81 projectors.

The first statement is checked exactly.  The second is fail-closed: the WW
seed is q-closed because q_r A=0, while the candidate graph IR contains no
q-action on quantum ports, vertices, edges, source words, or cuts.  No
external-target file is read.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
JSON_OUT = ROOT / "audits/step5-q-equivariant-graph-lift.json"
MD_OUT = ROOT / "audits/step5-q-equivariant-graph-lift.md"

PROJECT_PATH = ROOT / "scripts/step5_project_anomaly_engine.py"
RESIDUAL_Q_PATH = ROOT / "scripts/step5_residual_q_projection_audit.py"
SEED_PATH = ROOT / "scripts/step5_canonical_superfield_ww_seed.py"
GRAPH_PATH = ROOT / "scripts/step5_physical_graph_engine.py"


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PROJECT = load_module("step5_q_lift_project", PROJECT_PATH)
RESIDUAL_Q = load_module("step5_q_lift_residual", RESIDUAL_Q_PATH)
SEED = load_module("step5_q_lift_seed", SEED_PATH)
GRAPH = load_module("step5_q_lift_graph", GRAPH_PATH)


Exact = PROJECT.Exact
ZERO = PROJECT.ZERO
ONE = PROJECT.ONE
IMAGINARY_UNIT = PROJECT.IMAGINARY_UNIT
INV_SQRT2 = PROJECT.INV_SQRT2


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render_json(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def exact_payload(value: Exact) -> dict[str, Any]:
    return value.payload()


def exact_text(value: Exact) -> str:
    return PROJECT.exact_text(value)


def epsilon3(r: int, s: int, t: int) -> int:
    if {r, s, t} != {1, 2, 3}:
        return 0
    values = (r, s, t)
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def state_add(target: dict[str, Exact], field: str, coefficient: Exact) -> None:
    target[field] = target.get(field, ZERO) + coefficient
    if target[field].is_zero():
        del target[field]


def q_on_basis(r: int, field: str, *, q_a_override: bool = False) -> dict[str, Exact]:
    """Exact conditional U-complex action for one basis field."""
    if field == "U":
        return {f"C{r}": ONE}
    if field == "A":
        return ({"C1": ONE} if q_a_override and r == 1 else {})
    if field.startswith("B"):
        s = int(field[-1])
        return {"A": -IMAGINARY_UNIT} if r == s else {}
    if field.startswith("C"):
        s = int(field[-1])
        out: dict[str, Exact] = {}
        for t in (1, 2, 3):
            sign = epsilon3(r, s, t)
            if sign:
                out[f"B{t}"] = PROJECT.rational(-sign) * INV_SQRT2
        return out
    raise KeyError(field)


def apply_q(
    r: int,
    state: dict[str, Exact],
    *,
    q_a_override: bool = False,
) -> dict[str, Exact]:
    out: dict[str, Exact] = {}
    for field, coefficient in state.items():
        for target, q_coefficient in q_on_basis(
            r, field, q_a_override=q_a_override
        ).items():
            state_add(out, target, coefficient * q_coefficient)
    return out


def apply_q_path(
    path: list[int], *, q_a_override: bool = False
) -> dict[str, Exact]:
    state = {"U": ONE}
    for r in path:
        state = apply_q(r, state, q_a_override=q_a_override)
    return state


def canonical_lift_rows() -> list[dict[str, Any]]:
    # The path list is application order.  Thus [1,2,3] means q_3 q_2 q_1 U.
    specifications = (
        ("A", "A", 0, [1, 2, 3], None, -IMAGINARY_UNIT * INV_SQRT2),
        ("B1", "B", 1, [2, 3], None, INV_SQRT2),
        ("B2", "B", 1, [1, 3], None, -INV_SQRT2),
        ("B3", "B", 1, [1, 2], None, INV_SQRT2),
        ("C1", "C", 0, [1], None, ONE),
        ("C2", "C", 0, [2], None, ONE),
        ("C3", "C", 0, [3], None, ONE),
        ("Ddot1", "D", 1, [], 1, IMAGINARY_UNIT),
        ("Ddot2", "D", 1, [], 2, IMAGINARY_UNIT),
    )
    component_map = {row.id: row for row in PROJECT.COMPONENTS}
    rows = []
    for field, family, parity, path, dotted, expected in specifications:
        if dotted is None:
            state = apply_q_path(path)
            observed = state.get(field, ZERO)
            compact_component = component_map[field]
            theta_coefficient = compact_component.theta_coefficient
            compact_component_id = field
            operator = " ".join(f"q_{r}" for r in reversed(path))
            relation = (
                f"{operator} U={exact_text(observed)}*{field}"
                if len(path) > 1
                else f"q_{path[0]} U={field}"
            )
            input_scale = ONE
            flavour = int(field[-1]) if family in {"B", "C"} else None
            if family == "B":
                r, s = path
                flavour_permutation = {
                    "ordered_q_indices": path,
                    "output_flavour": flavour,
                    "epsilon_r_s_t": epsilon3(r, s, int(flavour)),
                    "formula": "q_s q_r U=(epsilon_rst/sqrt(2))*B_t for r<s",
                }
            elif family == "C":
                flavour_permutation = {
                    "ordered_q_indices": path,
                    "output_flavour": flavour,
                    "delta_r_t": 1,
                }
            else:
                flavour_permutation = {
                    "ordered_q_indices": path,
                    "epsilon_123": 1,
                }
        else:
            observed = IMAGINARY_UNIT
            theta_coefficient = ONE
            compact_component_id = "U"
            relation = f"P_dot{dotted} U=i*Ddot{dotted}"
            input_scale = -IMAGINARY_UNIT
            flavour = None
            flavour_permutation = {
                "ordered_q_indices": [],
                "dotted_index": dotted,
                "P_multiindex": [int(dotted == 1), int(dotted == 2)],
            }
        rows.append(
            {
                "field": field,
                "family": family,
                "parity": parity,
                "flavour": flavour,
                "dotted": dotted,
                "q_application_path": path,
                "q_operator_order": list(reversed(path)),
                "q_degree": len(path),
                "conditional_relation": relation,
                "observed_coefficient_on_physical_field": exact_payload(observed),
                "expected_coefficient_on_physical_field": exact_payload(expected),
                "compact_component": compact_component_id,
                "compact_theta_coefficient": exact_payload(theta_coefficient),
                "physical_input_scale_from_compact_jet": exact_payload(input_scale),
                "flavour_or_dotted_permutation": flavour_permutation,
                "path_check": "PASS" if observed == expected else "FAIL",
            }
        )
    return rows


def pair_rows(lifts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    lift_map = {row["field"]: row for row in lifts}
    component_map = {row.id: row for row in PROJECT.COMPONENTS}
    bundle = PROJECT.build_bundle()
    project_pairs = {
        row["id"]: row for row in bundle["project-result-ledger.json"]["pairs"]
    }
    rows = []
    for left in PROJECT.LETTERS:
        for right in PROJECT.LETTERS:
            left_lift = lift_map[left["id"]]
            right_lift = lift_map[right["id"]]
            left_component = component_map[left_lift["compact_component"]]
            right_component = component_map[right_lift["compact_component"]]
            _, observed_joint = PROJECT.component_product(
                left_component, right_component
            )
            koszul = -1 if (
                left_lift["parity"] * right_lift["q_degree"]
            ) % 2 else 1
            predicted_joint = (
                PROJECT.exact_from_payload(
                    left_lift["compact_theta_coefficient"]
                )
                * PROJECT.exact_from_payload(
                    right_lift["compact_theta_coefficient"]
                )
                * PROJECT.rational(koszul)
            )
            left_input_scale = PROJECT.exact_from_payload(
                left_lift["physical_input_scale_from_compact_jet"]
            )
            right_input_scale = PROJECT.exact_from_payload(
                right_lift["physical_input_scale_from_compact_jet"]
            )
            pair_id = f"{left['id']}__{right['id']}"
            project_pair = project_pairs[pair_id]
            project_input_scales = [
                PROJECT.exact_from_payload(payload)
                for payload in project_pair["input_scale_from_compact_jet"]
            ]
            rows.append(
                {
                    "pair_id": pair_id,
                    "family_channel": f"{left['family']}__{right['family']}",
                    "ordered_fields": [left["id"], right["id"]],
                    "left_q_path": left_lift["q_application_path"],
                    "right_q_path": right_lift["q_application_path"],
                    "left_index_map": left_lift["flavour_or_dotted_permutation"],
                    "right_index_map": right_lift["flavour_or_dotted_permutation"],
                    "koszul_formula": "(-1)^(parity(left)*q_degree(right))",
                    "koszul_exponent": left_lift["parity"]
                    * right_lift["q_degree"],
                    "koszul_sign": koszul,
                    "left_physical_input_scale_from_compact_jet": exact_payload(
                        left_input_scale
                    ),
                    "right_physical_input_scale_from_compact_jet": exact_payload(
                        right_input_scale
                    ),
                    "ordered_pair_physical_input_scale": exact_payload(
                        left_input_scale * right_input_scale
                    ),
                    "project_input_scale_check": (
                        "PASS"
                        if project_input_scales
                        == [left_input_scale, right_input_scale]
                        else "FAIL"
                    ),
                    "joint_compact_coefficient_observed": exact_payload(
                        observed_joint
                    ),
                    "joint_compact_coefficient_predicted": exact_payload(
                        predicted_joint
                    ),
                    "coefficient_check": (
                        "PASS" if observed_joint == predicted_joint else "FAIL"
                    ),
                    "project_exact_zero": project_pair["exact_zero"],
                    "project_zero_certificate": project_pair["zero_certificate"],
                    "project_output_count": len(project_pair["physical_outputs"]),
                    "graph_lift_state": "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
                }
            )
    return rows


def missing_raw_words() -> list[dict[str, Any]]:
    return [
        {
            "id": "RAW-Q-PARENT-UU",
            "state": "BLOCKED_U_SOURCE_VERTEX_UNDEFINED",
            "required_word": (
                "the ordered bare U>U insertion and all of its quantum-port "
                "functional derivatives"
            ),
            "reason": (
                "forward q paths start at U; the locked Project fields and the "
                "WW seed define no U field, source, propagator, or vertex"
            ),
        },
        {
            "id": "RAW-Q-INVERSE-DESCENT",
            "state": "BLOCKED_INVERSE_Q_DESCENT_UNDEFINED",
            "required_word": (
                "an explicit h_r on raw graph words with q_r h_r+h_r q_r "
                "equal to the required lower-letter projector"
            ),
            "reason": "q_r A=0, so forward q cannot leave the WW A>A seed",
        },
        {
            "id": "RAW-Q-QUANTUM-PORTS",
            "state": "BLOCKED_QUANTUM_Q_ACTION_UNDEFINED",
            "required_word": (
                "q_r on every background-split quantum port v, Phi_s, "
                "tildePhi_s, c, tilde-c, antighost, multiplier, and NK field"
            ),
            "reason": (
                "the bottom-letter q action does not define a derivation on "
                "the gauge-fixed quantum graph algebra"
            ),
        },
        {
            "id": "RAW-Q-WW-VERTICES",
            "state": "BLOCKED_VERTEX_Q_IMAGES_UNDEFINED",
            "required_word": (
                "q_r[+(i*g/2)c_UCD tildeW^D_dotgamma"
                "(barD_C^dotgamma-barD_U^dotgamma)] and "
                "q_r[-(i*g/2)c_VC'E W^{E gamma}"
                "(D_C',gamma-D_V,gamma)] resolved into the ordered "
                "gauge, tildePhi*V^n*Phi, Phi^3, and tildePhi^3 word basis"
            ),
            "reason": (
                "the candidate graph rows copy the two WW action vertices "
                "unchanged into every component pair"
            ),
        },
        {
            "id": "RAW-Q-EDGES",
            "state": "BLOCKED_EDGE_Q_INTERTWINER_UNDEFINED",
            "required_word": (
                "the endpoint identity q_r^(1)G+(-1)^epsilon G q_r^(2) "
                "for vector, chiral, antichiral, fermion, ghost, and mixed edges"
            ),
            "reason": (
                "the WW seed contains only three v-v edges; no transformed "
                "field type, numerator, arrow, or edge Koszul sign is emitted"
            ),
        },
        {
            "id": "RAW-Q-SOURCE",
            "state": "BLOCKED_SOURCE_Q_IMAGES_UNDEFINED",
            "required_word": (
                "q_r[(D_-K_+v^A)(K_+v^B)+(K_+v^A)(D_-K_+v^B)] "
                "together with nonlinear-letter, one-link, two-link, and "
                "endpoint source vertices"
            ),
            "reason": (
                "pair labels on ORDERED_BILOCAL_COMPONENT_PROJECTOR are not "
                "ordered functional derivatives of the source"
            ),
        },
        {
            "id": "RAW-Q-CUT",
            "state": "BLOCKED_CUT_Q_INTERTWINER_UNDEFINED",
            "required_word": (
                "q_r on each of the eight WW endpoint D-words and on every "
                "contact/link completion row, with [q_r,C_cut] evaluated"
            ),
            "reason": (
                "a metric replacement hat_delta->delta_4 does not prove "
                "q-equivariance of the raw Schwinger cut"
            ),
        },
        {
            "id": "RAW-Q-GAUGE-COMPLETION",
            "state": "BLOCKED_GAUGE_FIXING_COMPENSATOR_UNDEFINED",
            "required_word": (
                "the compensating BRST word, if nonzero, in q_r(S_gf+S_FP+S_NK+measure)"
            ),
            "reason": (
                "supersymmetry of the invariant action alone does not prove "
                "equivariance of the selected gauge-fixed graph complex"
            ),
        },
    ]


def graph_diagnostic(seed: dict[str, Any], ir: dict[str, Any]) -> dict[str, Any]:
    derivation = seed["derivation"]
    endpoint_rows = derivation["endpoint_rows"]
    members = [member for orbit in ir["orbits"] for member in orbit["members"]]
    action_signatures = {
        json.dumps(
            {
                "vertices": [
                    vertex
                    for vertex in member["vertices"]
                    if vertex["id"] != "I"
                ],
                "edges": member["edges"],
            },
            sort_keys=True,
        )
        for member in members
    }
    required_member_fields = {
        "q_path",
        "koszul_sign",
        "flavour_or_dotted_permutation",
        "vertex_transformations",
        "edge_transformations",
        "raw_derivative_words",
    }
    observed_member_fields = set.intersection(
        *(set(member) for member in members)
    ) if members else set()
    aa_orbits = [orbit for orbit in ir["orbits"] if orbit["pair_id"] == "A__A"]
    return {
        "ww_source": derivation["source_insertion"],
        "ww_action_vertices": derivation["vertices"]["exponent_vertices"],
        "ww_endpoint_word_count": len(endpoint_rows),
        "ww_endpoint_words": [row["raw_derivative_word"] for row in endpoint_rows],
        "q_action_on_seed_external_word": {
            "input": "A^A>A^B",
            "calculation": "q_r(A^A A^B)=(q_r A^A)A^B+A^A(q_r A^B)=0+0=0",
            "reachable_forward_q_words": ["A__A"],
            "unreachable_ordered_component_pairs": 80,
        },
        "candidate_compact_representatives": {
            "orbits": ir["cut_orbit_count"],
            "objects": ir["graph_object_count"],
            "aa_orbits": len(aa_orbits),
            "non_aa_orbits": len(ir["orbits"]) - len(aa_orbits),
            "distinct_action_vertex_edge_templates": len(action_signatures),
            "required_q_lift_fields": sorted(required_member_fields),
            "fields_present_on_every_member": sorted(
                required_member_fields & observed_member_fields
            ),
            "fields_missing_from_members": sorted(
                required_member_fields - observed_member_fields
            ),
            "classification": "COMPACT_KERNEL_CUT_REPRESENTATIVES_NOT_RAW_Q_LIFTED_GRAPHS",
        },
    }


def build_model() -> dict[str, Any]:
    residual = RESIDUAL_Q.build_result()
    seed = SEED.build_audit()
    ir = GRAPH.build_ir()
    lifts = canonical_lift_rows()
    pairs = pair_rows(lifts)
    missing = missing_raw_words()
    return {
        "q_a_zero": True,
        "lifts": lifts,
        "pairs": pairs,
        "ww_endpoint_words": seed["derivation"]["endpoint_rows"],
        "graph_transformations_claimed": [],
        "missing_raw_words": missing,
        "upstream": {
            "residual_q_verdict": residual["summary"]["verdict"],
            "residual_q_u_status": residual["conditional_completion"]["status"],
            "seed_status": seed["status"],
            "project_verification": PROJECT.build_bundle()[
                "project-verification.json"
            ]["status"],
        },
        "graph_diagnostic": graph_diagnostic(seed, ir),
    }


def validate_model(model: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    lift_map = {row["field"]: row for row in model["lifts"]}
    expected_fields = {
        "A", "B1", "B2", "B3", "C1", "C2", "C3", "Ddot1", "Ddot2"
    }
    if set(lift_map) != expected_fields or len(model["lifts"]) != 9:
        failures.append("LETTER_LIFT_COVERAGE")
    for row in model["lifts"]:
        observed_recorded = PROJECT.exact_from_payload(
            row["observed_coefficient_on_physical_field"]
        )
        expected_recorded = PROJECT.exact_from_payload(
            row["expected_coefficient_on_physical_field"]
        )
        if row["family"] == "D":
            observed_recomputed = IMAGINARY_UNIT
        else:
            observed_recomputed = apply_q_path(row["q_application_path"]).get(
                row["field"], ZERO
            )
        if (
            row["path_check"] != "PASS"
            or observed_recorded != expected_recorded
            or observed_recomputed != expected_recorded
        ):
            failures.append(f"Q_PATH::{row['field']}")
    pairs = model["pairs"]
    if len(pairs) != 81 or len({row["pair_id"] for row in pairs}) != 81:
        failures.append("PAIR_COVERAGE")
    channels = Counter(row["family_channel"] for row in pairs)
    expected_channels = {
        f"{left}__{right}" for left in "ABCD" for right in "ABCD"
    }
    if set(channels) != expected_channels:
        failures.append("FAMILY_CHANNEL_COVERAGE")
    for row in pairs:
        expected = -1 if row["koszul_exponent"] % 2 else 1
        observed = PROJECT.exact_from_payload(
            row["joint_compact_coefficient_observed"]
        )
        predicted = PROJECT.exact_from_payload(
            row["joint_compact_coefficient_predicted"]
        )
        if (
            row["koszul_sign"] != expected
            or row["coefficient_check"] != "PASS"
            or row["project_input_scale_check"] != "PASS"
            or observed != predicted
        ):
            failures.append(f"PAIR_KOSZUL::{row['pair_id']}")
    if not model["q_a_zero"]:
        failures.append("WW_SEED_Q_CLOSED")
    if len(model["ww_endpoint_words"]) != 8 or any(
        "raw_derivative_word" not in row for row in model["ww_endpoint_words"]
    ):
        failures.append("WW_ENDPOINT_WORD_COUNT")
    prerequisites = {row["id"] for row in model["missing_raw_words"]}
    if model["graph_transformations_claimed"] and prerequisites:
        failures.append("UNSUPPORTED_GRAPH_TRANSFORM")
    diagnostic = model["graph_diagnostic"]["candidate_compact_representatives"]
    if diagnostic["fields_present_on_every_member"]:
        failures.append("CANDIDATE_FIELD_DIAGNOSTIC")
    return sorted(set(failures))


def mutation_tests(base: dict[str, Any]) -> list[dict[str, Any]]:
    def flip_b2(model: dict[str, Any]) -> None:
        row = next(row for row in model["lifts"] if row["field"] == "B2")
        coefficient = PROJECT.exact_from_payload(
            row["expected_coefficient_on_physical_field"]
        )
        row["expected_coefficient_on_physical_field"] = exact_payload(-coefficient)

    def drop_d2(model: dict[str, Any]) -> None:
        model["lifts"] = [
            row for row in model["lifts"] if row["field"] != "Ddot2"
        ]

    def flip_pair_sign(model: dict[str, Any]) -> None:
        row = next(
            row for row in model["pairs"] if row["pair_id"] == "B1__C1"
        )
        row["koszul_sign"] *= -1

    def make_qa_nonzero(model: dict[str, Any]) -> None:
        model["q_a_zero"] = False

    def delete_endpoint(model: dict[str, Any]) -> None:
        model["ww_endpoint_words"].pop()

    def invent_transform(model: dict[str, Any]) -> None:
        model["graph_transformations_claimed"] = [
            {"source": "WW", "target": "B1__C1", "coefficient": "1"}
        ]

    mutations: list[tuple[str, str, Callable[[dict[str, Any]], None]]] = [
        ("FLIP_B2_EPSILON_SIGN", "Q_PATH::B2", flip_b2),
        ("DROP_DDOT2_LIFT", "LETTER_LIFT_COVERAGE", drop_d2),
        ("FLIP_B1_C1_KOSZUL", "PAIR_KOSZUL::B1__C1", flip_pair_sign),
        ("MAKE_qA_NONZERO", "WW_SEED_Q_CLOSED", make_qa_nonzero),
        ("DELETE_WW_ENDPOINT_WORD", "WW_ENDPOINT_WORD_COUNT", delete_endpoint),
        (
            "INVENT_VERTEX_TRANSFORM_WITHOUT_QUANTUM_q",
            "UNSUPPORTED_GRAPH_TRANSFORM",
            invent_transform,
        ),
    ]
    rows = []
    for mutation_id, expected, mutate in mutations:
        model = copy.deepcopy(base)
        mutate(model)
        observed = validate_model(model)
        rows.append(
            {
                "id": mutation_id,
                "expected_failure": expected,
                "observed_failures": observed,
                "status": "PASS" if expected in observed else "FAIL",
            }
        )
    return rows


def build_audit() -> dict[str, Any]:
    model = build_model()
    baseline_failures = validate_model(model)
    mutations = mutation_tests(model)
    pairs = model["pairs"]
    channels = Counter(row["family_channel"] for row in pairs)
    structural_pass = not baseline_failures and all(
        row["status"] == "PASS" for row in mutations
    )
    return {
        "schema": "awi.step5.q-equivariant-graph-lift-audit.v1",
        "authority_base_commit": PROJECT.AUTHORITY_BASE_COMMIT,
        "external_target_used": False,
        "candidate_inputs_under_audit": {
            str(path.relative_to(ROOT)): sha256_path(path)
            for path in (
                PROJECT_PATH,
                RESIDUAL_Q_PATH,
                SEED_PATH,
                GRAPH_PATH,
            )
        },
        "status": "BLOCKED_RAW_GRAPH_Q_EQUIVARIANT_LIFT",
        "structural_audit_status": "PASS" if structural_pass else "FAIL",
        "proved_scope": {
            "conditional_external_letter_paths": 9,
            "ordered_family_channels": len(channels),
            "ordered_component_pairs": len(pairs),
            "pair_koszul_rows": sum(
                row["coefficient_check"] == "PASS" for row in pairs
            ),
            "project_nonzero_pairs": sum(
                not row["project_exact_zero"] for row in pairs
            ),
            "project_zero_pairs": sum(
                row["project_exact_zero"] for row in pairs
            ),
            "claim": (
                "exact component coefficient extraction from the conditional "
                "compact U-complex; no raw graph lift is claimed"
            ),
        },
        "letter_lifts": model["lifts"],
        "family_channel_counts": dict(sorted(channels.items())),
        "ordered_pair_lifts": pairs,
        "raw_graph_diagnostic": model["graph_diagnostic"],
        "missing_raw_graph_words": model["missing_raw_words"],
        "baseline_failures": baseline_failures,
        "mutation_tests": mutations,
        "upstream_status": model["upstream"],
        "verdict": {
            "compact_covariant_component_ledger": "PROVED_CONDITIONAL_ON_U_COMPLETION",
            "ww_to_all_component_graph_lift": "REJECTED_AS_CURRENT_CLAIM",
            "physical_graph_census": "BLOCKED_RAW_GRAPH_Q_DATA_MISSING",
            "exact_reason": (
                "q_r A=0 makes the forward q-orbit of the raw A>A WW seed "
                "one-dimensional; the candidate 132 objects contain compact "
                "kernel labels but no q-transformed raw vertices, edges, source "
                "D-words, or cut intertwiners"
            ),
        },
    }


def markdown(audit: dict[str, Any]) -> str:
    lift_lines = []
    for row in audit["letter_lifts"]:
        path = ",".join(str(value) for value in row["q_application_path"]) or "-"
        lift_lines.append(
            f"| `{row['field']}` | `{path}` | "
            f"${row['conditional_relation']}$ | `{row['path_check']}` |"
        )
    blocker_lines = []
    for row in audit["missing_raw_graph_words"]:
        blocker_lines.append(
            f"| `{row['id']}` | `{row['state']}` | {row['required_word']} |"
        )
    mutation_lines = []
    for row in audit["mutation_tests"]:
        mutation_lines.append(
            f"| `{row['id']}` | `{row['expected_failure']}` | `{row['status']}` |"
        )
    graph = audit["raw_graph_diagnostic"]["candidate_compact_representatives"]
    return rf"""# Step-5 residual-$q$ graph-lift audit

## 1. Notation

$$
q_r:=Q^r_{{E,+}}/\sqrt2,
\qquad
P_{{\dot a}}:=(\sigma_E^m)_{{+\dot a}}\mathcal D_m.
$$

The path `[1,2,3]` means $q_3q_2q_1U$.

## 2. Exact conditional external paths

$$
\begin{{aligned}}
q_rU&=C_r,\\
q_sq_rU&=\frac1{{\sqrt2}}\varepsilon_{{rst}}B_t\quad(r<s),\\
q_3q_2q_1U&=-\frac i{{\sqrt2}}A,\\
P_{{\dot a}}U&=iD_{{\dot a}}.
\end{{aligned}}
$$

| field | application path | exact relation | check |
|---|---|---|---|
{chr(10).join(lift_lines)}

$$
(-1)^{{\kappa(X,Y)}}=(-1)^{{\epsilon_X|I_Y|}}.
$$

The emitted JSON contains all {audit['proved_scope']['ordered_component_pairs']} ordered pair rows and all {audit['proved_scope']['ordered_family_channels']} family channels.  Every joint compact coefficient obeys

$$
c_{{X,Y}}=(-1)^{{\epsilon_X|I_Y|}}c_Xc_Y.
$$

## 3. Raw WW obstruction

$$
q_r(A^AA^B)
=(q_rA^A)A^B+A^A(q_rA^B)
=0+0
=0.
$$

Hence the forward $q$-orbit of the raw WW external word contains only `A__A`; the other $80$ ordered component pairs are not generated.

The WW seed has exactly eight endpoint $D$-words.  The candidate IR has

$$
N_{{\rm orbit}}={graph['orbits']},
\qquad
N_{{\rm object}}={graph['objects']},
\qquad
N_{{\rm non-AA\ orbit}}={graph['non_aa_orbits']},
$$

but only {graph['distinct_action_vertex_edge_templates']} action-vertex/edge template and no common member field among

`{', '.join(graph['required_q_lift_fields'])}`.

Therefore these are compact-kernel/cut representatives, not raw $q$-lifted graphs.

## 4. Missing raw words

| id | state | required word |
|---|---|---|
{chr(10).join(blocker_lines)}

## 5. Falsification

| mutation | required failure | result |
|---|---|---|
{chr(10).join(mutation_lines)}

$$
\boxed{{\mathrm{{status}}=
\mathrm{{BLOCKED\_RAW\_GRAPH\_Q\_EQUIVARIANT\_LIFT}}}}
$$
"""


def write_outputs(audit: dict[str, Any]) -> dict[str, str]:
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSON_OUT: render_json(audit),
        MD_OUT: markdown(audit),
    }
    hashes = {}
    for path, body in payloads.items():
        data = body.encode()
        path.write_bytes(data)
        hashes[str(path.relative_to(ROOT))] = hashlib.sha256(data).hexdigest()
    return hashes


def check_outputs(audit: dict[str, Any]) -> list[str]:
    expected = {JSON_OUT: render_json(audit), MD_OUT: markdown(audit)}
    errors = []
    for path, body in expected.items():
        if not path.exists():
            errors.append(f"missing:{path.relative_to(ROOT)}")
        elif path.read_text() != body:
            errors.append(f"stale:{path.relative_to(ROOT)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("one of --write or --check is required")
    audit = build_audit()
    errors = []
    hashes: dict[str, str] = {}
    if args.write:
        hashes = write_outputs(audit)
    if args.check:
        errors = check_outputs(audit)
    structural_ok = audit["structural_audit_status"] == "PASS" and not errors
    print(
        json.dumps(
            {
                "scientific_status": audit["status"],
                "structural_audit_status": audit["structural_audit_status"],
                "output_errors": errors,
                "hashes": hashes,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if structural_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
