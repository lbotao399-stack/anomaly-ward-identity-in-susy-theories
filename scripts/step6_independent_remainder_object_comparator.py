#!/usr/bin/env python3
"""Clean-checkout independent remainder-object reconstruction and comparison."""

from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
import gzip
from hashlib import sha256
import inspect
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from scripts import step6_independent_selected_edge_word_dalgebra_gate as gate
    from scripts import step6_preaggregation_measure_delta_replay as replay
except ModuleNotFoundError:  # direct execution
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts import step6_independent_selected_edge_word_dalgebra_gate as gate
    from scripts import step6_preaggregation_measure_delta_replay as replay


ROOT = Path(__file__).resolve().parents[1]
SEED = (
    ROOT
    / "generated/step6/measure-tagged-delta-convolution/measure-tagged-delta-convolution.json"
)
GENERATED = (
    ROOT
    / "generated/step6/independent-remainder-object-comparator/independent-remainder-object-comparator.json.gz"
)
AUDIT = ROOT / "audits/step6-independent-remainder-object-comparator-verification.json"
TEST_PATH = ROOT / "tests/test_step6_independent_remainder_object_comparator.py"

SCHEMA = "step6.independent_remainder_object_comparator.v1"
STATUS = "PASS_1568_REMAINDER_OBJECTS_INDEPENDENT_LOCAL_EXTERIOR_RECONSTRUCTION"
TYPE_ID = "TYPE::IndependentLocalExteriorRemainderObjectComparator"
EXPECTED_SEED_SHA = "b5ecf1ac6a471f7a6d75158d502ec6a869fe5d0bce6599343f285b7cf404a940"
EXPECTED_GATE_COMMIT = "288329e"
EXPECTED_GATE_SOURCE_SHA = (
    "b8abf68e203cde926972e7871856f3fbd95a80ea7b78553615b48cd1c342b6a6"
)
EXPECTED_REPLAY_SOURCE_SHA = (
    "cab350456eb126fd517c4aada40a28dba2405e0aa1f4d539959517d7ee54af4d"
)
EXPECTED_REPLAY_PAYLOAD_SHA = (
    "fa7118bb2f672f12e372db16e752b388eee6b24459b6326edf7f434def9e2508"
)
EXPECTED_REPLAY_DEPENDENCY_MANIFEST_SHA = (
    "7ca5998d61f3693ecef7933d1e0f5febd84725af65602ec5743d8b6a04325526"
)

RANK = {
    "barD_dotplus": 0,
    "barD_dotminus": 1,
    "D_plus": 2,
    "D_minus": 3,
}
MIXED = {
    ("D_plus", "barD_dotplus"): "k_pp",
    ("D_plus", "barD_dotminus"): "k_pm",
    ("D_minus", "barD_dotplus"): "k_mp",
    ("D_minus", "barD_dotminus"): "k_mm",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qi(value: Mapping[str, Any]) -> gate.LocalGaussian:
    return gate.LocalGaussian(Fraction(str(value["re"])), Fraction(str(value["im"])))


def constant_poly_qi(value: Sequence[Mapping[str, Any]]) -> gate.LocalGaussian:
    if len(value) != 1 or value[0]["monomial"] != []:
        raise AssertionError("raw scalar is not constant")
    return qi(value[0]["coefficient"])


def dword_poly_to_local(rows: Sequence[Mapping[str, Any]]) -> gate.LocalPolynomial:
    terms = {}
    for row in rows:
        powers = [0, 0, 0, 0]
        for factor in row["monomial"]:
            powers[gate.MOMENTUM_VARIABLE_INDEX[str(factor["symbol"])]] += int(
                factor["exponent"]
            )
        terms[tuple(powers)] = qi(row["factor"])
    return gate.LocalPolynomial.from_terms(terms)


def _load_seed() -> dict[str, Any]:
    if file_sha256(SEED) != EXPECTED_SEED_SHA:
        raise AssertionError("seed file hash changed")
    payload = json.loads(SEED.read_text(encoding="utf-8"))
    if payload["payload_sha256"] != digest(
        {k: v for k, v in payload.items() if k != "payload_sha256"}
    ):
        raise AssertionError("seed self hash fails")
    return payload


def _measure_children(history: Mapping[str, Any]) -> list[dict[str, Any]]:
    expansions = (
        (gate.LOCAL_ONE_QI, ("barD_dotplus", "barD_dotminus")),
        (gate.LOCAL_MINUS_ONE_QI, ("barD_dotminus", "barD_dotplus")),
    )
    output = []
    for expansion_scalar, word in expansions:
        states = [(expansion_scalar, deepcopy(history["factors_in_raw_AST_order"]))]
        for primitive in reversed(word):
            emitted = []
            for scalar, factors in states:
                prefix = 0
                for position, factor in enumerate(factors):
                    coefficient_parity = int(factor["coefficient_parity"])
                    sign = -1 if prefix ^ coefficient_parity else 1
                    child = deepcopy(factors)
                    before = int(factor["derived_factor_parity"])
                    child[position]["derived_factor_parity"] = before ^ 1
                    child[position]["derivative_word_outer_to_inner"] = [
                        primitive,
                        *child[position]["derivative_word_outer_to_inner"],
                    ]
                    emitted.append((scalar * sign, child))
                    prefix ^= before
            states = emitted
        output.extend(
            {"relative_scalar": scalar * Fraction(-1, 4), "factors": factors}
            for scalar, factors in states
        )
    return output


def _reordering_sign(
    order: Sequence[str], target: Sequence[str], parities: Mapping[str, int]
) -> int:
    rank = {label: index for index, label in enumerate(target)}
    exponent = 0
    for left in range(len(order)):
        for right in range(left + 1, len(order)):
            if rank[order[left]] > rank[order[right]]:
                exponent ^= parities[order[left]] * parities[order[right]]
    return -1 if exponent else 1


def _extraction_sign(factors: Sequence[Mapping[str, Any]], contracted: set[str]) -> int:
    flags = [
        str(factor["grammar_port_id"]) in contracted
        for factor in factors
        for _ in factor["derivative_word_outer_to_inner"]
    ]
    inversions = sum(
        1
        for position, on_edge in enumerate(flags)
        if on_edge
        for earlier in flags[:position]
        if not earlier
    )
    return -1 if inversions & 1 else 1


@lru_cache(maxsize=None)
def _independent_normal_form(
    action_word: tuple[str, ...], insertion_word: tuple[str, ...]
) -> tuple[tuple[tuple[str, ...], gate.LocalPolynomial], ...]:
    queue = [
        (
            gate.LocalPolynomial.constant(-1 if len(insertion_word) & 1 else 1),
            action_word + insertion_word,
        )
    ]
    normal: dict[tuple[str, ...], gate.LocalPolynomial] = {}
    while queue:
        polynomial, word = queue.pop(0)
        rewritten = False
        for index in range(len(word) - 1):
            left, right = word[index], word[index + 1]
            if left == right:
                rewritten = True
                break
            if RANK[left] <= RANK[right]:
                continue
            swapped = word[:index] + (right, left) + word[index + 2 :]
            queue.append((polynomial.scale(-1), swapped))
            if (left, right) in MIXED:
                momentum = gate.LocalPolynomial.variable(MIXED[(left, right)])
                queue.append(
                    (
                        polynomial
                        * momentum.scale(gate.LocalGaussian(0, Fraction(-2))),
                        word[:index] + word[index + 2 :],
                    )
                )
            rewritten = True
            break
        if not rewritten:
            normal[word] = normal.get(word, gate.LOCAL_ZERO) + polynomial
    result = tuple(
        sorted((word, polynomial) for word, polynomial in normal.items() if polynomial)
    )

    evaluator = gate.LocalExteriorEvaluator()
    reconstructed = gate.LocalExteriorMatrix()
    for word, polynomial in result:
        reconstructed = reconstructed + evaluator.word_matrix(word).scale(polynomial)
    if reconstructed != evaluator.raw_delta_matrix(action_word, insertion_word):
        raise AssertionError("independent normal form fails LocalExterior matrix gate")
    return result


def _signature(
    factors: Sequence[Mapping[str, Any]], contracted: set[str]
) -> tuple[Any, ...]:
    return tuple(
        (
            str(factor["topology_port_id"]),
            tuple(str(token) for token in factor["derivative_word_outer_to_inner"]),
        )
        for factor in factors
        if str(factor["grammar_port_id"]) not in contracted
    )


def _key_json(key: tuple[Any, ...]) -> dict[str, Any]:
    signature, word = key
    return {
        "survivor_signature": [
            {"edge_id": edge, "word_outer_to_inner": list(tokens)}
            for edge, tokens in signature
        ],
        "remaining_e_AI_tokens": [
            {
                "derivative_kind": "BAR_D" if token.startswith("barD") else "D",
                "spinor_component": {
                    "barD_dotplus": "dot+",
                    "barD_dotminus": "dot-",
                    "D_plus": "+",
                    "D_minus": "-",
                }[token],
            }
            for token in word
        ],
    }


def _key_from_json(row: Mapping[str, Any]) -> tuple[Any, ...]:
    inverse = {
        ("BAR_D", "dot+"): "barD_dotplus",
        ("BAR_D", "dot-"): "barD_dotminus",
        ("D", "+"): "D_plus",
        ("D", "-"): "D_minus",
    }
    return (
        tuple(
            (str(item["edge_id"]), tuple(str(x) for x in item["word_outer_to_inner"]))
            for item in row["survivor_signature"]
        ),
        tuple(
            inverse[(str(item["derivative_kind"]), str(item["spinor_component"]))]
            for item in row["remaining_e_AI_tokens"]
        ),
    )


def _is_edge_square(polynomial: gate.LocalPolynomial) -> bool:
    pp, pm, mp, mm = (gate.LocalPolynomial.variable(x) for x in gate.MOMENTUM_VARIABLES)
    edge_square = pp * mm - pm * mp
    values = polynomial.as_dict()
    basis = edge_square.as_dict()
    if set(values) != set(basis):
        return False
    first = next(iter(basis))
    q = values[first] * basis[first]
    return all(values[key] == basis[key] * q for key in basis)


def _independent_objects() -> dict[tuple[Any, ...], dict[str, Any]]:
    seed = _load_seed()["measure_tagged_raw_replay"]
    histories = {str(row["history_id"]): row for row in seed["raw_histories"]}
    total: dict[tuple[Any, ...], gate.LocalPolynomial] = {}
    incidence: dict[tuple[Any, ...], dict[str, gate.LocalPolynomial]] = defaultdict(
        dict
    )
    for parent in seed["unaggregated_contact_provenance"]:
        action = histories[str(parent["action_raw_trace_history_id"])]
        insertion = histories[str(parent["insertion_raw_trace_history_id"])]
        insertion_factors = deepcopy(insertion["factors_in_raw_AST_order"])
        action_port = str(parent["contracted_action_port"])
        insertion_port = str(parent["contracted_insertion_port"])
        contracted = {action_port, insertion_port}
        old_reorder = int(
            parent["preaggregation_Koszul_ledger"]["coefficient_reordering_sign"]
        )
        old_extraction = int(
            parent["preaggregation_Koszul_ledger"]["derivative_extraction_sign"]
        )
        parent_scalar = qi(parent["preaggregation_exact_coefficient_before_measure"])
        canonical = [
            str(x)
            for x in parent["factor_order_ledger"]["canonical_preaggregation_order"]
        ]
        for child in _measure_children(action):
            factors = [*child["factors"], *insertion_factors]
            factor_by_port = {str(row["grammar_port_id"]): row for row in factors}
            order = [str(row["grammar_port_id"]) for row in factors]
            parities = {
                str(row["grammar_port_id"]): int(row["coefficient_parity"])
                for row in factors
            }
            scalar = parent_scalar * child["relative_scalar"]
            scalar = scalar * _reordering_sign(order, canonical, parities) * old_reorder
            scalar = scalar * _extraction_sign(factors, contracted) * old_extraction
            action_word = tuple(
                str(x)
                for x in factor_by_port[action_port]["derivative_word_outer_to_inner"]
            )
            insertion_word = tuple(
                str(x)
                for x in factor_by_port[insertion_port][
                    "derivative_word_outer_to_inner"
                ]
            )
            signature = _signature(factors, contracted)
            for word, polynomial in _independent_normal_form(
                action_word, insertion_word
            ):
                key = signature, word
                contribution = polynomial.scale(scalar)
                total[key] = total.get(key, gate.LOCAL_ZERO) + contribution
                pair_id = str(parent["provenance_id"])
                incidence[key][pair_id] = (
                    incidence[key].get(pair_id, gate.LOCAL_ZERO) + contribution
                )
    objects = {}
    for key, polynomial in sorted(total.items()):
        if not polynomial or _is_edge_square(polynomial):
            continue
        parents = [
            {"parent_pair_id": parent, "exact_polynomial": value.to_json()}
            for parent, value in sorted(incidence[key].items())
            if value
        ]
        parent_sum = gate.LOCAL_ZERO
        for row in parents:
            parent_sum = parent_sum + local_poly_from_local_json(
                row["exact_polynomial"]
            )
        if parent_sum != polynomial:
            raise AssertionError("independent incidence fails to reconstruct")
        objects[key] = {
            **_key_json(key),
            "exact_polynomial": polynomial.to_json(),
            "parent_incidence": parents,
        }
    return objects


def local_poly_from_local_json(
    rows: Sequence[Mapping[str, Any]],
) -> gate.LocalPolynomial:
    terms = {}
    for row in rows:
        powers = tuple(
            int(row["powers"].get(symbol, 0)) for symbol in gate.MOMENTUM_VARIABLES
        )
        terms[powers] = qi(row["coefficient"])
    return gate.LocalPolynomial.from_terms(terms)


def _replay_objects(
    replay_payload: Mapping[str, Any] | None = None,
) -> dict[tuple[Any, ...], dict[str, Any]]:
    replay_payload = (
        replay.build_payload() if replay_payload is None else replay_payload
    )
    rows = replay_payload["measure_tagged_delta_convolution_replay"]["aggregate_rows"]
    objects = {}
    for row in rows:
        if row["classification"] != "REMAINDER":
            continue
        key = _key_from_json(row)
        objects[key] = {
            **_key_json(key),
            "exact_polynomial": dword_poly_to_local(row["exact_polynomial"]).to_json(),
            "parent_incidence": [
                {
                    "parent_pair_id": str(parent["parent_pair_id"]),
                    "exact_polynomial": dword_poly_to_local(
                        parent["exact_polynomial"]
                    ).to_json(),
                }
                for parent in row["parent_incidence"]
            ],
        }
    return objects


def compare_maps(
    left: Mapping[Any, Mapping[str, Any]], right: Mapping[Any, Mapping[str, Any]]
) -> dict[str, Any]:
    rows = []
    for key in sorted(set(left) | set(right)):
        left_object, right_object = left.get(key), right.get(key)
        both = left_object is not None and right_object is not None
        poly_equal = both and local_poly_from_local_json(
            left_object["exact_polynomial"]
        ) == local_poly_from_local_json(right_object["exact_polynomial"])
        left_incidence = [] if not both else left_object["parent_incidence"]
        right_incidence = [] if not both else right_object["parent_incidence"]
        left_parent_ids = [str(x["parent_pair_id"]) for x in left_incidence]
        right_parent_ids = [str(x["parent_pair_id"]) for x in right_incidence]
        incidence_multiplicity_exact = (
            both
            and len(left_parent_ids) == len(set(left_parent_ids))
            and len(right_parent_ids) == len(set(right_parent_ids))
            and len(left_parent_ids) == len(right_parent_ids)
        )
        incidence_equal = incidence_multiplicity_exact and {
            str(x["parent_pair_id"]): local_poly_from_local_json(x["exact_polynomial"])
            for x in left_incidence
        } == {
            str(x["parent_pair_id"]): local_poly_from_local_json(x["exact_polynomial"])
            for x in right_incidence
        }
        rows.append(
            {
                "key_sha256": digest(_key_json(key)),
                "present_both": both,
                "polynomial_equal": bool(poly_equal),
                "incidence_multiplicity_exact": bool(incidence_multiplicity_exact),
                "incidence_equal": bool(incidence_equal),
            }
        )
    return {
        "left_count": len(left),
        "right_count": len(right),
        "key_sets_equal": set(left) == set(right),
        "all_polynomials_equal": all(x["polynomial_equal"] for x in rows),
        "all_incidence_multiplicities_exact": all(
            x["incidence_multiplicity_exact"] for x in rows
        ),
        "all_parent_incidence_equal": all(x["incidence_equal"] for x in rows),
        "rows": rows,
    }


@lru_cache(maxsize=1)
def build_payload() -> dict[str, Any]:
    left = _independent_objects()
    replay_payload = replay.build_payload()
    right = _replay_objects(replay_payload)
    comparison = compare_maps(left, right)
    replay_dependency_manifest = replay_payload["input_provenance"]["file_sha256"]
    replay_checks = replay.exact_checks(replay_payload)
    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "resolved_type_id": TYPE_ID,
        "independent_gate_commit": EXPECTED_GATE_COMMIT,
        "left_engine": "FROZEN_SEED_PLUS_LOCAL_EXTERIOR_NORMAL_FORM",
        "right_engine": "FRESH_PREAGGREGATION_REPLAY",
        "forbidden_imports": [
            "step6_grouped_e_v_i2_i3_ordered_port_normal_form",
            "step6_full_dword_bridge",
            "step6_ordered_sector_euler_normal_form",
        ],
        "independent_remainder_objects": [left[key] for key in sorted(left)],
        "replay_remainder_objects": [right[key] for key in sorted(right)],
        "objectwise_comparison": comparison,
        "input_sha256": {
            str(SEED.relative_to(ROOT)): file_sha256(SEED),
            "scripts/step6_independent_selected_edge_word_dalgebra_gate.py": file_sha256(
                ROOT / "scripts/step6_independent_selected_edge_word_dalgebra_gate.py"
            ),
            "scripts/step6_preaggregation_measure_delta_replay.py": file_sha256(
                ROOT / "scripts/step6_preaggregation_measure_delta_replay.py"
            ),
        },
        "replay_runtime_closure": {
            "payload_sha256": replay_payload["payload_sha256"],
            "dependency_manifest_sha256": digest(replay_dependency_manifest),
            "dependency_paths": sorted(replay_dependency_manifest),
            "replay_exact_checks": replay_checks,
        },
        "catalogs_separately_materialized": all(
            left[key] is not right[key] for key in set(left) & set(right)
        ),
        "external_result_used_as_input": False,
    }
    payload["payload_sha256"] = digest(payload)
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    c = payload["objectwise_comparison"]
    source = Path(__file__).read_text(encoding="utf-8")
    import_region = source.split("ROOT =", 1)[0]
    left_source = "\n".join(
        inspect.getsource(function)
        for function in (
            _load_seed,
            _measure_children,
            _reordering_sign,
            _extraction_sign,
            _independent_normal_form,
            _signature,
            _is_edge_square,
            _independent_objects,
        )
    )
    return {
        "schema_status_exact": payload["schema"] == SCHEMA
        and payload["status"] == STATUS,
        "clean_left_import_boundary": all(
            token not in import_region for token in payload["forbidden_imports"]
        ),
        "left_executor_does_not_call_replay_or_shared_dword": all(
            token not in left_source
            for token in ("replay.", "dword.", "grouped.", "trace.", "euler.")
        ),
        "frozen_seed_exact": payload["input_sha256"][str(SEED.relative_to(ROOT))]
        == EXPECTED_SEED_SHA,
        "committed_gate_source_exact": payload["input_sha256"][
            "scripts/step6_independent_selected_edge_word_dalgebra_gate.py"
        ]
        == EXPECTED_GATE_SOURCE_SHA,
        "replay_source_exact": payload["input_sha256"][
            "scripts/step6_preaggregation_measure_delta_replay.py"
        ]
        == EXPECTED_REPLAY_SOURCE_SHA,
        "replay_payload_exact": payload["replay_runtime_closure"]["payload_sha256"]
        == EXPECTED_REPLAY_PAYLOAD_SHA,
        "replay_dependency_manifest_exact": payload["replay_runtime_closure"][
            "dependency_manifest_sha256"
        ]
        == EXPECTED_REPLAY_DEPENDENCY_MANIFEST_SHA,
        "replay_internal_checks_pass": all(
            payload["replay_runtime_closure"]["replay_exact_checks"].values()
        ),
        "catalogs_separate": payload["catalogs_separately_materialized"],
        "exact_1568_key_sets": c["left_count"] == c["right_count"] == 1568
        and c["key_sets_equal"],
        "all_exact_polynomials_equal": c["all_polynomials_equal"],
        "all_incidence_multiplicities_exact": c["all_incidence_multiplicities_exact"],
        "all_parent_incidence_equal": c["all_parent_incidence_equal"],
        "payload_hash_valid": payload["payload_sha256"]
        == digest({k: v for k, v in payload.items() if k != "payload_sha256"}),
    }


def write_outputs(payload: Mapping[str, Any]) -> None:
    GENERATED.parent.mkdir(parents=True, exist_ok=True)
    with GENERATED.open("wb") as handle:
        with gzip.GzipFile(fileobj=handle, mode="wb", mtime=0) as archive:
            archive.write((canonical_json(payload) + "\n").encode())
    checks = exact_checks(payload)
    audit = {
        "schema": "step6.independent_remainder_object_comparator.audit.v1",
        "status": payload["status"],
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "counts": {
            "independent_remainder_objects": payload["objectwise_comparison"][
                "left_count"
            ],
            "replay_remainder_objects": payload["objectwise_comparison"]["right_count"],
            "objectwise_rows": len(payload["objectwise_comparison"]["rows"]),
        },
        "payload_sha256": payload["payload_sha256"],
        "artifact_sha256": file_sha256(GENERATED),
        "script_sha256": file_sha256(Path(__file__)),
        "test_sha256": file_sha256(TEST_PATH),
    }
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> None:
    payload = build_payload()
    failed = [name for name, passed in exact_checks(payload).items() if not passed]
    if failed:
        raise SystemExit(f"independent remainder comparator failed: {failed}")
    write_outputs(payload)


if __name__ == "__main__":
    main()
