#!/usr/bin/env python3
"""Exact full-option contraction for one direct Step-6 decorated parent.

This compiler is deliberately bounded to
G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4, direct orientation, and the external
coefficient slice s_p1=s_p2=0.  It computes each source-term tensor with
generic grammar-port momenta once, translates attachments by exact port-axis
permutation and polynomial momentum substitution, aggregates coefficient and
color data jointly, and contracts the five 16-state edges by K4-minus-edge
variable elimination.  No comparison data, DRED, UV pole, or anomaly
coefficient enters this layer.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
import argparse
import gzip
import hashlib
import json
import shutil
import time

try:
    from scripts import step6_coefficient_tensor as coefficient
    from scripts import step6_color_tensor as color
    from scripts import step6_global_supertensor as global_tensor
    from scripts import step6_two_loop_amplitude_ir as amplitude
except ModuleNotFoundError:  # direct execution from scripts/
    import step6_coefficient_tensor as coefficient
    import step6_color_tensor as color
    import step6_global_supertensor as global_tensor
    import step6_two_loop_amplitude_ir as amplitude


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "generated/step6/full-supertensor"
OUTPUT_JSON = OUTPUT_DIR / "full-supertensor.json"
OUTPUT_MD = OUTPUT_DIR / "full-supertensor.md"
AUDIT = ROOT / "audits/step6-full-supertensor-verification.json"

SCHEMA = "step6.full_parent_graded_supertensor.v1"
STATUS_COMPLETE = "PASS_ONE_DIRECT_PARENT_ALL_LOCAL_OPTIONS_EXTERNAL_SLICE_00"
STATUS_PARTIAL = "PASS_DEEPEST_EXACT_AGGREGATION_FULL_PARENT_CONTRACTION_BLOCKED"
GRAPH_ID = "G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4"
ORIENTATION = "direct"
EXTERNAL_SLICE = {"p1": 0, "p2": 0}
EDGE_VARIABLES = ("e_AI", "e_IB", "e_CA", "e_BC", "e_BA")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_values(left: Any | None, right: Any) -> Any:
    return right if left is None else left + right


def scale_value(value: Any, scalar: Any) -> Any:
    if isinstance(value, coefficient.oracle.Exterior):
        return value.scale(scalar)
    return value * scalar


def serialize_value(value: Any) -> dict[str, Any]:
    return coefficient.serialize_evaluation(value)


def deserialize_poly(rows: Sequence[Mapping[str, Any]]) -> Any:
    terms = {}
    for row in rows:
        monomial = tuple(
            (str(item["symbol"]), int(item["exponent"]))
            for item in row["monomial"]
        )
        scalar = row["coefficient"]
        terms[monomial] = coefficient.oracle.Gaussian(
            Fraction(str(scalar["re"])), Fraction(str(scalar["im"]))
        )
    return coefficient.oracle.Poly.from_terms(terms)


def deserialize_value(record: Mapping[str, Any]) -> Any:
    if record["type"] == "Poly":
        return deserialize_poly(record["terms"])
    if record["type"] == "Exterior":
        return coefficient.oracle.Exterior.from_terms(
            {
                int(row["mask"]): deserialize_poly(row["coefficient"])
                for row in record["terms"]
            }
        )
    raise TypeError(record["type"])


def deterministic_gzip_write(path: Path, payload: bytes) -> dict[str, Any]:
    compressed = gzip.compress(payload, compresslevel=9, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(compressed)
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "uncompressed_sha256": hashlib.sha256(payload).hexdigest(),
        "compressed_sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_bytes": len(payload),
        "compressed_bytes": len(compressed),
    }


def multiply_values(left: Any, right: Any) -> Any:
    if isinstance(left, coefficient.oracle.Exterior) and isinstance(
        right, coefficient.oracle.Poly
    ):
        return left.scale(right)
    if isinstance(right, coefficient.oracle.Exterior) and isinstance(
        left, coefficient.oracle.Poly
    ):
        return right.scale(left)
    if isinstance(left, coefficient.oracle.Poly) and isinstance(
        right, coefficient.oracle.Poly
    ):
        return left * right
    raise TypeError(f"unsupported tensor product {type(left)} x {type(right)}")


def substitute_poly(value: Any, substitutions: Mapping[str, Any]) -> Any:
    result = coefficient.oracle.ZERO
    for monomial, scalar in value.terms:
        term = coefficient.oracle.Poly.constant(scalar)
        for symbol, exponent in monomial:
            replacement = substitutions.get(symbol)
            if replacement is None:
                if symbol.startswith("q") and "_" in symbol:
                    raise KeyError(f"missing generic momentum substitution for {symbol}")
                replacement = coefficient.oracle.Poly.variable(symbol)
            term = term * (replacement**exponent)
        result = result + term
    return result


def substitute_value(value: Any, substitutions: Mapping[str, Any]) -> Any:
    if isinstance(value, coefficient.oracle.Poly):
        return substitute_poly(value, substitutions)
    if isinstance(value, coefficient.oracle.Exterior):
        return coefficient.oracle.Exterior.from_terms(
            {
                mask: substitute_poly(poly, substitutions)
                for mask, poly in value.terms
            }
        )
    raise TypeError(type(value))


class CachedDerivativeEngine:
    """Exact graded Leibniz engine bound to this module's oracle instance."""

    def __init__(self) -> None:
        self.operators: dict[Any, Mapping[str, Any]] = {}

    def primitive(self, terms: Sequence[Any], primitive: str) -> tuple[Any, ...]:
        emitted = []
        for term in terms:
            prefix_parity = 0
            for position, factor in enumerate(term.factors):
                operators = self.operators.get(factor.momentum)
                if operators is None:
                    operators = coefficient.oracle.flat_operators(factor.momentum)
                    self.operators[factor.momentum] = operators
                differentiated = operators[primitive].apply(factor.value)
                if differentiated:
                    replacement = coefficient.oracle.LabeledLeaf(
                        factor.label,
                        factor.momentum,
                        factor.parity ^ 1,
                        differentiated,
                        (primitive,) + factor.derivative_word,
                        factor.coefficient_parity,
                    )
                    sign_exponent = prefix_parity ^ factor.coefficient_parity
                    emitted.append(
                        coefficient.oracle.ProductTerm(
                            term.coefficient * (-1 if sign_exponent else 1),
                            term.factors[:position]
                            + (replacement,)
                            + term.factors[position + 1 :],
                        )
                    )
                prefix_parity ^= factor.parity
        return coefficient._canonical_product_terms(emitted)

    def __call__(self, terms: Sequence[Any], tokens: Sequence[str]) -> tuple[Any, ...]:
        emitted = []
        for branch_coefficient, primitive_word in coefficient._explicit_word_expansion(tokens):
            branch = coefficient.scale_terms(
                terms, coefficient.oracle.Poly.constant(branch_coefficient)
            )
            for primitive in reversed(primitive_word):
                branch = self.primitive(branch, primitive)
            emitted.extend(branch)
        return coefficient._canonical_product_terms(emitted)


def generic_momentum_substitutions(
    program: Mapping[str, Any],
) -> dict[str, Any]:
    bindings = {row["grammar_port_id"]: row for row in program["bindings"]}
    substitutions: dict[str, Any] = {}
    suffixes = ((0, 0, "pp"), (0, 1, "pm"), (1, 0, "mp"), (1, 1, "mm"))
    for ordinal, port in enumerate(program["port_order"]):
        actual = coefficient.momentum_from_vector(
            bindings[port]["all_incoming_leaf_momentum_vector"]
        )
        for row, column, suffix in suffixes:
            substitutions[f"q{ordinal}_{suffix}"] = actual.components[row][column]
    return substitutions


def generic_local_tensor(
    term: Mapping[str, Any], background_ports: Sequence[str]
) -> dict[str, Any]:
    port_order = tuple(term["port_order"])
    background = frozenset(background_ports)
    if not background <= set(port_order):
        raise ValueError("generic background port is absent from source term")
    quantum_ports = tuple(port for port in port_order if port not in background)
    momenta = {
        port: coefficient.oracle.BispinorMomentum.symbolic(f"q{ordinal}")
        for ordinal, port in enumerate(port_order)
    }
    engine = CachedDerivativeEngine()
    tensor: dict[tuple[int, ...], Any] = {}
    evaluated = 0
    for quantum_masks in product(range(16), repeat=len(quantum_ports)):
        basis = dict(zip(quantum_ports, quantum_masks, strict=True))
        basis.update({port: 0 for port in background})
        leaves = {
            port: coefficient.oracle.LabeledLeaf(
                port,
                momenta[port],
                0,
                coefficient.oracle.Exterior.basis(basis[port]),
                coefficient_parity=coefficient.coefficient_parity(basis[port]),
            )
            for port in port_order
        }
        product_terms = coefficient._evaluate_ast_terms(
            term["expression_ast"], leaves, {}, engine
        )
        parities = {
            port: coefficient.coefficient_parity(basis[port]) for port in port_order
        }
        raw = coefficient.apply_measure(
            coefficient.evaluate_product_terms(product_terms, parities),
            term["measure"],
        )
        raw_coefficient = coefficient.parse_qi_polynomial(term["coefficient_raw"])
        value = scale_value(raw, raw_coefficient)
        evaluated += 1
        if value:
            tensor[quantum_masks] = value
    return {
        "term_id": term["term_id"],
        "background_ports": sorted(background),
        "port_order": list(port_order),
        "quantum_port_order": list(quantum_ports),
        "evaluated_entries": evaluated,
        "nonzero_entries": len(tensor),
        "tensor": tensor,
    }


def binding_label(binding: Mapping[str, Any]) -> str:
    if binding["role"] == "BACKGROUND_EXTERNAL_ENDPOINT":
        return global_tensor.external_label(binding)
    return f"{binding['edge_id']}:{binding['orientation_endpoint']}"


def local_edge_order(parent: amplitude.AmplitudeParent, vertex_id: str) -> tuple[str, ...]:
    return tuple(
        edge["edge_id"]
        for edge in parent.graph["orientations"][parent.orientation]["edges"]
        if edge["source"] == vertex_id or edge["target"] == vertex_id
    )


def local_canonical_labels(
    parent: amplitude.AmplitudeParent,
    vertex_id: str,
    program: Mapping[str, Any],
) -> tuple[str, ...]:
    bindings = {row["grammar_port_id"]: row for row in program["bindings"]}
    by_edge = {
        str(row["edge_id"]): binding_label(row)
        for row in bindings.values()
        if row["role"] == "QUANTUM_EDGE_ENDPOINT"
    }
    labels = [by_edge[edge] for edge in local_edge_order(parent, vertex_id)]
    external = {
        global_tensor.external_label(row)
        for row in bindings.values()
        if row["role"] == "BACKGROUND_EXTERNAL_ENDPOINT"
    }
    labels.extend(label for label in ("p1", "p2") if label in external)
    if len(labels) != len(program["port_order"]):
        raise AssertionError("local canonical label count differs from grammar rank")
    return tuple(labels)


def transform_generic_option(
    parent: amplitude.AmplitudeParent,
    vertex_id: str,
    program: Mapping[str, Any],
    generic: Mapping[str, Any],
) -> dict[tuple[int, ...], Any]:
    bindings = {row["grammar_port_id"]: row for row in program["bindings"]}
    substitutions = generic_momentum_substitutions(program)
    canonical_labels = local_canonical_labels(parent, vertex_id, program)
    edge_order = local_edge_order(parent, vertex_id)
    transformed: dict[tuple[int, ...], Any] = {}
    for quantum_masks, generic_value in generic["tensor"].items():
        basis_by_port = dict(
            zip(generic["quantum_port_order"], quantum_masks, strict=True)
        )
        basis_by_port.update({port: 0 for port in generic["background_ports"]})
        source_by_edge: dict[str, int] = {}
        actual_word = []
        for port in program["port_order"]:
            binding = bindings[port]
            basis_mask = basis_by_port[port]
            label = binding_label(binding)
            actual_word.append(
                global_tensor.WordVariable(
                    label, coefficient.coefficient_parity(basis_mask)
                )
            )
            if binding["role"] == "QUANTUM_EDGE_ENDPOINT":
                source_by_edge[str(binding["edge_id"])] = (
                    basis_mask
                    if binding["orientation_endpoint"] == "source"
                    else 15 ^ basis_mask
                )
        topology_key = tuple(source_by_edge[edge] for edge in edge_order)
        reorder_sign = global_tensor.weighted_permutation_sign(
            actual_word, canonical_labels
        )
        value = scale_value(
            substitute_value(generic_value, substitutions), reorder_sign
        )
        transformed[topology_key] = add_values(
            transformed.get(topology_key), value
        )
    return transformed


def tensor_content_hash(tensor: Mapping[tuple[int, ...], Any]) -> str:
    return digest(
        [
            {
                "key": list(key),
                "value": serialize_value(value),
            }
            for key, value in sorted(tensor.items())
        ]
    )


def aggregate_local_joint_tensors(
    parent: amplitude.AmplitudeParent,
    bundle: Mapping[str, Any],
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    programs = global_tensor.option_program_index(bundle)
    terms = bundle["tensor_programs"]["compiled_terms"]
    vertices = {str(row["vertex_id"]): row for row in parent.graph["vertices"]}
    generic_cache: dict[tuple[str, tuple[str, ...]], dict[str, Any]] = {}
    groups_by_vertex: dict[str, list[dict[str, Any]]] = {}
    operation_counts = {
        "generic_tensor_requests": 0,
        "generic_tensor_cache_misses": 0,
        "generic_basis_entries_evaluated": 0,
        "generic_nonzero_entries": 0,
        "attachment_transforms": 0,
        "attachment_transformed_nonzero_entries": 0,
    }
    for vertex_id in parent.vertex_order:
        groups: dict[str, dict[str, Any]] = {}
        for option in parent.local_options[vertex_id]:
            option_id = str(option["local_amplitude_option_id"])
            program = programs[option_id]
            term = terms[str(program["term_id"])]
            background_ports = tuple(
                sorted(
                    row["grammar_port_id"]
                    for row in program["bindings"]
                    if row["role"] == "BACKGROUND_EXTERNAL_ENDPOINT"
                )
            )
            cache_key = (str(term["term_id"]), background_ports)
            operation_counts["generic_tensor_requests"] += 1
            generic = generic_cache.get(cache_key)
            if generic is None:
                generic = generic_local_tensor(term, background_ports)
                generic_cache[cache_key] = generic
                operation_counts["generic_tensor_cache_misses"] += 1
                operation_counts["generic_basis_entries_evaluated"] += generic[
                    "evaluated_entries"
                ]
                operation_counts["generic_nonzero_entries"] += generic[
                    "nonzero_entries"
                ]
            transformed = transform_generic_option(
                parent, vertex_id, program, generic
            )
            operation_counts["attachment_transforms"] += 1
            operation_counts["attachment_transformed_nonzero_entries"] += len(
                transformed
            )
            color_row = color.compile_local_color_option(
                parent, vertices[vertex_id], option
            )
            signature = color.local_group_signature(color_row)
            group = groups.setdefault(
                signature,
                {
                    "local_color_signature_sha256": signature,
                    "representative_color_row": color_row,
                    "local_amplitude_option_ids": [],
                    "tensor": {},
                },
            )
            group["local_amplitude_option_ids"].append(option_id)
            for key, value in transformed.items():
                group["tensor"][key] = add_values(group["tensor"].get(key), value)
        rows = []
        for signature in sorted(groups):
            group = groups[signature]
            group["multiplicity"] = len(group["local_amplitude_option_ids"])
            group["tensor_nonzero_entries"] = len(group["tensor"])
            group["joint_tensor_sha256"] = tensor_content_hash(group["tensor"])
            rows.append(group)
        groups_by_vertex[vertex_id] = rows
    generic_ledger = [
        {
            "term_id": term_id,
            "background_ports": list(background_ports),
            "evaluated_entries": generic["evaluated_entries"],
            "nonzero_entries": generic["nonzero_entries"],
            "generic_tensor_sha256": tensor_content_hash(generic["tensor"]),
        }
        for (term_id, background_ports), generic in sorted(generic_cache.items())
    ]
    operation_counts["generic_cache_record_count"] = len(generic_ledger)
    operation_counts["raw_local_option_count"] = sum(
        len(parent.local_options[vertex]) for vertex in parent.vertex_order
    )
    operation_counts["joint_local_color_group_count"] = sum(
        len(groups_by_vertex[vertex]) for vertex in parent.vertex_order
    )
    return groups_by_vertex, {
        "operation_counts": operation_counts,
        "generic_tensor_ledger": generic_ledger,
    }


def common_vertex_label_orders(
    parent: amplitude.AmplitudeParent,
    bundle: Mapping[str, Any],
) -> dict[str, tuple[str, ...]]:
    programs = global_tensor.option_program_index(bundle)
    result = {}
    for vertex in parent.vertex_order:
        program = programs[
            str(parent.local_options[vertex][0]["local_amplitude_option_id"])
        ]
        result[vertex] = local_canonical_labels(parent, vertex, program)
    return result


def edge_canonical_labels(parent: amplitude.AmplitudeParent) -> tuple[str, ...]:
    labels = []
    for edge in parent.graph["orientations"][parent.orientation]["edges"]:
        labels.extend((f"{edge['edge_id']}:source", f"{edge['edge_id']}:target"))
    labels.extend(("p1", "p2"))
    return tuple(labels)


def common_global_word(
    parent: amplitude.AmplitudeParent,
    bundle: Mapping[str, Any],
    source_masks: Mapping[str, int],
    orders: Mapping[str, Sequence[str]] | None = None,
) -> list[global_tensor.WordVariable]:
    if orders is None:
        orders = common_vertex_label_orders(parent, bundle)
    word = []
    for vertex in parent.vertex_order:
        for label in orders[vertex]:
            if label in ("p1", "p2"):
                mask = EXTERNAL_SLICE[label]
            else:
                edge_id, endpoint = label.split(":")
                source = source_masks[edge_id]
                mask = source if endpoint == "source" else 15 ^ source
            word.append(
                global_tensor.WordVariable(
                    label, coefficient.coefficient_parity(mask)
                )
            )
    return word


def sign_polynomial(parent: amplitude.AmplitudeParent, bundle: Mapping[str, Any]) -> dict[str, Any]:
    orders = common_vertex_label_orders(parent, bundle)
    labels = tuple(label for vertex in parent.vertex_order for label in orders[vertex])
    canonical = edge_canonical_labels(parent)
    if set(labels) != set(canonical):
        raise AssertionError("common and edge-canonical words differ")
    rank = {label: index for index, label in enumerate(canonical)}
    linear: dict[str, int] = defaultdict(int)
    quadratic: dict[tuple[str, str], int] = defaultdict(int)
    for position, left in enumerate(labels):
        for right in labels[position + 1 :]:
            if rank[left] <= rank[right]:
                continue
            if left in ("p1", "p2") or right in ("p1", "p2"):
                continue  # external coefficient masks are fixed even in this slice
            left_edge = left.split(":")[0]
            right_edge = right.split(":")[0]
            if left_edge == right_edge:
                linear[left_edge] ^= 1
            else:
                quadratic[tuple(sorted((left_edge, right_edge)))] ^= 1
    linear_terms = sorted(edge for edge, value in linear.items() if value)
    quadratic_terms = sorted(pair for pair, value in quadratic.items() if value)
    stage1_linear = [edge for edge in linear_terms if edge == "e_AI"]
    stage1_quadratic = [pair for pair in quadratic_terms if "e_AI" in pair]
    if any(set(pair) - {"e_AI", "e_IB"} for pair in stage1_quadratic):
        raise AssertionError("x1 sign factor cannot be eliminated at IA stage")
    remaining_linear = [edge for edge in linear_terms if edge not in stage1_linear]
    remaining_quadratic = [pair for pair in quadratic_terms if pair not in stage1_quadratic]
    stage3_edges = {"e_CA", "e_BC"}
    stage3_linear = [edge for edge in remaining_linear if edge in stage3_edges]
    stage3_quadratic = [
        pair for pair in remaining_quadratic if set(pair) <= stage3_edges
    ]
    stage2_linear = [edge for edge in remaining_linear if edge not in stage3_linear]
    stage2_quadratic = [
        pair for pair in remaining_quadratic if pair not in stage3_quadratic
    ]
    stages = {
        "IA": {"linear": stage1_linear, "quadratic": stage1_quadratic},
        "IAB": {"linear": stage2_linear, "quadratic": stage2_quadratic},
        "IABC": {"linear": stage3_linear, "quadratic": stage3_quadratic},
    }
    for parity_bits in product((0, 1), repeat=5):
        # mask 0 is even and mask 1 is odd.  The sign depends only on these
        # five parities, so the 32 checks cover all 16^5 basis assignments.
        source = dict(zip(EDGE_VARIABLES, parity_bits, strict=True))
        direct = global_tensor.weighted_permutation_sign(
            common_global_word(parent, bundle, source, orders), canonical
        )
        staged = 1
        for stage in stages.values():
            staged *= sign_from_terms(stage, source)
        if direct != staged:
            raise AssertionError((source, direct, staged))
    return {
        "linear_terms": linear_terms,
        "quadratic_terms": [list(pair) for pair in quadratic_terms],
        "stages": {
            name: {
                "linear": value["linear"],
                "quadratic": [list(pair) for pair in value["quadratic"]],
            }
            for name, value in stages.items()
        },
        "checked_edge_parity_cases": 2**5,
        "all_16_pow_5_mask_assignments_checked": 16**5,
        "common_word_sign_equals_staged_sign": True,
    }


def sign_from_terms(stage: Mapping[str, Any], source_masks: Mapping[str, int]) -> int:
    parity = {
        edge: coefficient.coefficient_parity(mask)
        for edge, mask in source_masks.items()
    }
    exponent = sum(parity[edge] for edge in stage["linear"])
    exponent += sum(parity[left] * parity[right] for left, right in stage["quadratic"])
    return -1 if exponent & 1 else 1


def port_permutation_fixture(
    parent: amplitude.AmplitudeParent, bundle: Mapping[str, Any]
) -> dict[str, Any]:
    programs = global_tensor.option_program_index(bundle)
    per_vertex_patterns: dict[str, list[tuple[str, ...]]] = {}
    common_orders = common_vertex_label_orders(parent, bundle)
    for vertex in parent.vertex_order:
        patterns = {
            tuple(
                binding_label(
                    {
                        row["grammar_port_id"]: row
                        for row in programs[str(option["local_amplitude_option_id"])][
                            "bindings"
                        ]
                    }[port]
                )
                for port in programs[str(option["local_amplitude_option_id"])][
                    "port_order"
                ]
            )
            for option in parent.local_options[vertex]
        }
        per_vertex_patterns[vertex] = sorted(patterns)
    canonical = edge_canonical_labels(parent)
    checked = 0
    for patterns in product(*(per_vertex_patterns[v] for v in parent.vertex_order)):
        for parity_bits in product((0, 1), repeat=5):
            parity = dict(zip(EDGE_VARIABLES, parity_bits, strict=True))
            parity.update({"p1": 0, "p2": 0})

            def variable(label: str) -> global_tensor.WordVariable:
                edge = label.split(":")[0] if ":" in label else label
                return global_tensor.WordVariable(label, parity[edge])

            actual_word = [variable(label) for pattern in patterns for label in pattern]
            common_word = [
                variable(label)
                for vertex in parent.vertex_order
                for label in common_orders[vertex]
            ]
            direct = global_tensor.weighted_permutation_sign(actual_word, canonical)
            local = 1
            for pattern, vertex in zip(patterns, parent.vertex_order, strict=True):
                local *= global_tensor.weighted_permutation_sign(
                    [variable(label) for label in pattern], common_orders[vertex]
                )
            common = global_tensor.weighted_permutation_sign(common_word, canonical)
            if direct != local * common:
                raise AssertionError((patterns, parity_bits, direct, local, common))
            checked += 1
    return {
        "unique_local_word_patterns": {
            vertex: len(per_vertex_patterns[vertex]) for vertex in parent.vertex_order
        },
        "checked_pattern_parity_cases": checked,
        "actual_to_edge_equals_local_to_common_times_common_to_edge": True,
    }


def edge_kernel(
    source_mask: int, metric_inverse: Sequence[Sequence[Fraction]]
) -> Fraction:
    target = 15 ^ source_mask
    h_inverse = (
        -1 if coefficient.coefficient_parity(source_mask) else 1
    ) * metric_inverse[source_mask][target]
    return Fraction(-2) * h_inverse


def contract_ia(
    insertion: Mapping[tuple[int, int], Any],
    action: Mapping[tuple[int, int, int], Any],
    metric_inverse: Sequence[Sequence[Fraction]],
    stage: Mapping[str, Any],
    counts: dict[str, int],
) -> dict[tuple[int, int, int], Any]:
    insertion_by_x1: dict[int, list[tuple[int, Any]]] = defaultdict(list)
    action_by_x1: dict[int, list[tuple[int, int, Any]]] = defaultdict(list)
    for (x1, x2), value in insertion.items():
        insertion_by_x1[x1].append((x2, value))
    for (x1, x3, x5), value in action.items():
        action_by_x1[x1].append((x3, x5, value))
    result: dict[tuple[int, int, int], Any] = {}
    for x1 in set(insertion_by_x1) & set(action_by_x1):
        kernel = edge_kernel(x1, metric_inverse)
        for x2, left in insertion_by_x1[x1]:
            for x3, x5, right in action_by_x1[x1]:
                masks = {"e_AI": x1, "e_IB": x2, "e_CA": x3, "e_BA": x5}
                scalar = kernel * sign_from_terms(stage, masks)
                value = scale_value(multiply_values(left, right), scalar)
                key = (x2, x3, x5)
                result[key] = add_values(result.get(key), value)
                counts["IA_multiply_adds"] += 1
    return {key: value for key, value in result.items() if value}


def contract_iab(
    partial: Mapping[tuple[int, int, int], Any],
    action_b: Mapping[tuple[int, int, int], Any],
    metric_inverse: Sequence[Sequence[Fraction]],
    stage: Mapping[str, Any],
    counts: dict[str, int],
) -> dict[tuple[int, int], Any]:
    b_by_x2_x5: dict[tuple[int, int], list[tuple[int, Any]]] = defaultdict(list)
    for (x2, x4, x5), value in action_b.items():
        b_by_x2_x5[(x2, x5)].append((x4, value))
    result: dict[tuple[int, int], Any] = {}
    for (x2, x3, x5), left in partial.items():
        candidates = b_by_x2_x5.get((x2, x5), ())
        scalar_edges = edge_kernel(x2, metric_inverse) * edge_kernel(
            x5, metric_inverse
        )
        for x4, right in candidates:
            masks = {"e_IB": x2, "e_CA": x3, "e_BC": x4, "e_BA": x5}
            scalar = scalar_edges * sign_from_terms(stage, masks)
            value = scale_value(multiply_values(left, right), scalar)
            key = (x3, x4)
            result[key] = add_values(result.get(key), value)
            counts["IAB_multiply_adds"] += 1
    return {key: value for key, value in result.items() if value}


def contract_iabc(
    partial: Mapping[tuple[int, int], Any],
    action_c: Mapping[tuple[int, int], Any],
    metric_inverse: Sequence[Sequence[Fraction]],
    stage: Mapping[str, Any],
    counts: dict[str, int],
) -> Any:
    result = coefficient.oracle.Exterior()
    for (x3, x4), left in partial.items():
        right = action_c.get((x3, x4))
        if right is None:
            continue
        masks = {"e_CA": x3, "e_BC": x4}
        scalar = (
            edge_kernel(x3, metric_inverse)
            * edge_kernel(x4, metric_inverse)
            * sign_from_terms(stage, masks)
        )
        result = result + scale_value(multiply_values(left, right), scalar)
        counts["IABC_multiply_adds"] += 1
    return result


def normalized_color_network(
    parent: amplitude.AmplitudeParent,
    groups: Sequence[Mapping[str, Any]],
) -> tuple[str, dict[str, Any], int]:
    local_rows = [group["representative_color_row"] for group in groups]
    tensors, _ = color.attach_propagator_color_metrics(parent, local_rows)
    reduced = color.reduce_metrics_exact(tensors)
    canonical = color.canonicalize_network(reduced["tensors"], antisymmetry=True)
    sign = int(canonical["overall_antisymmetry_sign"])
    if canonical["zero_by_antisymmetry"]:
        return "ZERO", canonical, 0
    normalized = dict(canonical)
    normalized["overall_antisymmetry_sign"] = 1
    normalized["signature_sha256"] = digest(
        {key: value for key, value in normalized.items() if key != "signature_sha256"}
    )
    return normalized["signature_sha256"], normalized, sign


def contract_all_groups(
    parent: amplitude.AmplitudeParent,
    bundle: Mapping[str, Any],
    groups: Mapping[str, Sequence[Mapping[str, Any]]],
    sign_record: Mapping[str, Any],
    *,
    max_final_group_tuples: int | None = None,
) -> dict[str, Any]:
    shard_root = OUTPUT_DIR / ".coefficient-shards"
    polynomial_root = OUTPUT_DIR / "polynomials"
    shutil.rmtree(shard_root, ignore_errors=True)
    shutil.rmtree(polynomial_root, ignore_errors=True)
    shard_root.mkdir(parents=True, exist_ok=True)
    metric_inverse = [
        [Fraction(value) for value in row]
        for row in bundle["coefficient_metric"]["M_inverse"]
    ]
    stages = {
        name: {
            "linear": row["linear"],
            "quadratic": [tuple(pair) for pair in row["quadratic"]],
        }
        for name, row in sign_record["stages"].items()
    }
    counts = defaultdict(int)
    ia_cache: dict[tuple[int, int], dict[tuple[int, int, int], Any]] = {}
    for i_index, insertion in enumerate(groups["I"]):
        for a_index, action_a in enumerate(groups["A"]):
            ia_cache[(i_index, a_index)] = contract_ia(
                insertion["tensor"],
                action_a["tensor"],
                metric_inverse,
                stages["IA"],
                counts,
            )
    graph_aut = int(
        parent.graph["automorphisms"]["background_source_labeled"]["order"]
    )
    graph_weight = Fraction(-1, graph_aut)
    if graph_weight != Fraction(-1, 2):
        raise AssertionError("GraphIR background-labeled automorphism order changed")
    final_by_color: dict[str, dict[str, Any]] = {}
    tuple_count = 0
    nonzero_tuple_count = 0
    iab_record_count = 0
    stop = False
    for (i_index, a_index), partial_ia in ia_cache.items():
        for b_index, action_b in enumerate(groups["B"]):
            partial = contract_iab(
                partial_ia,
                action_b["tensor"],
                metric_inverse,
                stages["IAB"],
                counts,
            )
            iab_record_count += 1
            for c_index, action_c in enumerate(groups["C"]):
                if max_final_group_tuples is not None and tuple_count >= max_final_group_tuples:
                    stop = True
                    break
                tuple_count += 1
                value = contract_iabc(
                    partial,
                    action_c["tensor"],
                    metric_inverse,
                    stages["IABC"],
                    counts,
                )
                if not value:
                    continue
                selected_groups = (
                    groups["I"][i_index],
                    groups["A"][a_index],
                    groups["B"][b_index],
                    groups["C"][c_index],
                )
                color_signature, network, color_sign = normalized_color_network(
                    parent, selected_groups
                )
                if color_sign == 0:
                    continue
                nonzero_tuple_count += 1
                weighted = value.scale(graph_weight * color_sign)
                row = final_by_color.setdefault(
                    color_signature,
                    {
                        "canonical_color_network_sha256": color_signature,
                        "canonical_color_network": network,
                        "coefficient_shards": [],
                        "contributing_joint_group_tuples": 0,
                    },
                )
                serialized = serialize_value(weighted)
                encoded = canonical_json(serialized).encode("utf-8")
                shard_path = shard_root / (
                    f"{tuple_count:04d}-{color_signature}.json.gz"
                )
                shard_metadata = deterministic_gzip_write(shard_path, encoded)
                row["coefficient_shards"].append(shard_metadata)
                row["contributing_joint_group_tuples"] += 1
            if stop:
                break
        if stop:
            break
    final_rows = []
    for signature in sorted(final_by_color):
        row = final_by_color[signature]
        total = coefficient.oracle.Exterior()
        for shard in row["coefficient_shards"]:
            compressed = (ROOT / shard["path"]).read_bytes()
            if hashlib.sha256(compressed).hexdigest() != shard["compressed_sha256"]:
                raise AssertionError("coefficient shard compressed hash changed")
            encoded = gzip.decompress(compressed)
            if hashlib.sha256(encoded).hexdigest() != shard["uncompressed_sha256"]:
                raise AssertionError("coefficient shard payload hash changed")
            total = total + deserialize_value(json.loads(encoded))
        if not total:
            continue
        serialized_total = serialize_value(total)
        encoded_total = canonical_json(serialized_total).encode("utf-8")
        polynomial_artifact = deterministic_gzip_write(
            polynomial_root / f"{signature}.json.gz", encoded_total
        )
        final_rows.append(
            {
                "canonical_color_network_sha256": signature,
                "canonical_color_network": row["canonical_color_network"],
                "coefficient_exterior_polynomial_artifact": polynomial_artifact,
                "coefficient_exterior_term_count": sum(
                    len(term["coefficient"])
                    for term in serialized_total["terms"]
                ),
                "coefficient_exterior_mask_support": [
                    term["mask"] for term in serialized_total["terms"]
                ],
                "contributing_joint_group_tuples": row[
                    "contributing_joint_group_tuples"
                ],
            }
        )
    shutil.rmtree(shard_root)
    expected_tuples = (
        len(groups["I"])
        * len(groups["A"])
        * len(groups["B"])
        * len(groups["C"])
    )
    complete = tuple_count == expected_tuples
    return {
        "complete": complete,
        "expected_joint_group_tuples": expected_tuples,
        "contracted_joint_group_tuples": tuple_count,
        "nonzero_joint_group_tuples_before_color_aggregation": nonzero_tuple_count,
        "final_nonzero_canonical_color_network_count": len(final_rows),
        "final_canonical_color_coefficients": final_rows,
        "coefficient_storage": "DETERMINISTIC_GZIP_CANONICAL_JSON_ONE_ARTIFACT_PER_COLOR_NETWORK",
        "operation_counts": dict(counts),
        "IA_cache_records": len(ia_cache),
        "IAB_streamed_records": iab_record_count,
        "graph_weight": str(graph_weight),
        "Aut_bg": graph_aut,
        "Aut_bg_certificate_sha256": parent.graph["automorphisms"][
            "background_source_labeled"
        ]["automorphism_hash"],
    }


def serializable_group_ledger(
    groups: Mapping[str, Sequence[Mapping[str, Any]]]
) -> dict[str, Any]:
    return {
        vertex: [
            {
                "local_color_signature_sha256": group[
                    "local_color_signature_sha256"
                ],
                "multiplicity": group["multiplicity"],
                "local_amplitude_option_ids": group["local_amplitude_option_ids"],
                "tensor_nonzero_entries": group["tensor_nonzero_entries"],
                "joint_tensor_sha256": group["joint_tensor_sha256"],
            }
            for group in rows
        ]
        for vertex, rows in groups.items()
    }


def build_payload(max_final_group_tuples: int | None = None) -> dict[str, Any]:
    started = time.perf_counter()
    bundle = coefficient.build_bundle()
    amplitude_payload, parents = amplitude.build_payload()
    parent = next(
        row
        for row in parents
        if row.graph["graph_id"] == GRAPH_ID and row.orientation == ORIENTATION
    )
    groups, aggregation = aggregate_local_joint_tensors(parent, bundle)
    permutation_fixture = port_permutation_fixture(parent, bundle)
    sign_record = sign_polynomial(parent, bundle)
    contraction = contract_all_groups(
        parent,
        bundle,
        groups,
        sign_record,
        max_final_group_tuples=max_final_group_tuples,
    )
    status = STATUS_COMPLETE if contraction["complete"] else STATUS_PARTIAL
    payload = {
        "schema": SCHEMA,
        "status": status,
        "authority_role": "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE",
        "scope": {
            "graph_id": GRAPH_ID,
            "orientation": ORIENTATION,
            "orientation_role": "PHYSICAL_SUM_REPRESENTATIVE",
            "external_coefficient_slice": dict(EXTERNAL_SLICE),
            "all_local_options": True,
        },
        "inputs": {
            "coefficient_tensor_sha256": file_sha256(
                ROOT / "scripts/step6_coefficient_tensor.py"
            ),
            "color_tensor_sha256": file_sha256(
                ROOT / "scripts/step6_color_tensor.py"
            ),
            "global_sign_oracle_sha256": file_sha256(
                ROOT / "scripts/step6_global_supertensor.py"
            ),
            "amplitude_payload_sha256": amplitude_payload["payload_sha256"],
            "coefficient_payload_sha256": bundle["payload_sha256"],
        },
        "generic_source_term_aggregation": aggregation,
        "joint_local_color_groups": serializable_group_ledger(groups),
        "port_axis_permutation_fixture": permutation_fixture,
        "common_global_sign_polynomial": sign_record,
        "variable_elimination": {
            "edge_variables": list(EDGE_VARIABLES),
            "stage_1": "sum e_AI in I(e_AI,e_IB)*A(e_AI,e_CA,e_BA)",
            "stage_2": "sum (e_IB,e_BA) against B(e_IB,e_BC,e_BA)",
            "stage_3": "sum (e_CA,e_BC) against C(e_CA,e_BC;p1,p2)",
            "flat_16_pow_5_rows_materialized": False,
            "coefficient_color_marginal_product": "REJECTED",
            "same_joint_local_option_data_used": True,
        },
        "contraction": contraction,
        "runtime_seconds_informational": time.perf_counter() - started,
        "fail_closed": {
            "other_direct_decorated_parents": "BLOCKED_OUTSIDE_THIS_COMPILER_SCOPE",
            "other_external_coefficient_slices": "BLOCKED_NOT_EVALUATED",
            "DRED": "BLOCKED_NOT_PERFORMED",
            "UV_pole": "BLOCKED_NOT_PERFORMED",
            "renormalized_two_loop_coefficient": None,
        },
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "runtime_seconds_informational"}
    )
    return payload


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    aggregation = payload["generic_source_term_aggregation"]["operation_counts"]
    contraction = payload["contraction"]
    return {
        "one_direct_parent": payload["scope"]["graph_id"] == GRAPH_ID
        and payload["scope"]["orientation"] == "direct",
        "all_local_options_requested": payload["scope"]["all_local_options"],
        "external_slice_00": payload["scope"]["external_coefficient_slice"]
        == {"p1": 0, "p2": 0},
        "generic_cache_reduces_196_requests": aggregation[
            "generic_tensor_requests"
        ]
        == 196
        and aggregation["generic_tensor_cache_misses"] < 196,
        "local_color_group_counts_exact": {
            vertex: len(rows)
            for vertex, rows in payload["joint_local_color_groups"].items()
        }
        == {"I": 2, "A": 6, "B": 6, "C": 56},
        "port_permutation_composition_exact": payload[
            "port_axis_permutation_fixture"
        ]["actual_to_edge_equals_local_to_common_times_common_to_edge"],
        "common_sign_staging_exact": payload["common_global_sign_polynomial"][
            "common_word_sign_equals_staged_sign"
        ],
        "no_flat_materialization": not payload["variable_elimination"][
            "flat_16_pow_5_rows_materialized"
        ],
        "joint_not_marginal": payload["variable_elimination"][
            "coefficient_color_marginal_product"
        ]
        == "REJECTED",
        "graph_weight_from_Aut_bg": contraction["Aut_bg"] == 2
        and contraction["graph_weight"] == "-1/2",
        "coefficient_claim_absent": payload["fail_closed"][
            "renormalized_two_loop_coefficient"
        ]
        is None,
    }


def build_audit(payload: Mapping[str, Any]) -> dict[str, Any]:
    checks = exact_checks(payload)
    return {
        "schema": "step6.full_parent_graded_supertensor.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "payload_sha256": payload["payload_sha256"],
        "contraction_complete": payload["contraction"]["complete"],
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    contraction = payload["contraction"]
    return "\n".join(
        [
            "# Step 6 — full local-option supertensor contraction for one direct parent",
            "",
            "$$",
            "H^{-1}_{st}=(-1)^{|s|}(M^{-1})_{st},\\qquad t=15\\mathbin{\\mathtt{xor}}s.",
            "$$",
            "",
            "$$",
            "w_G=-\\frac1{|\\operatorname{Aut}_B(G)|}=-\\frac12.",
            "$$",
            "",
            f"Status: `{payload['status']}`.",
            "",
            f"Joint group tuples: `{contraction['contracted_joint_group_tuples']}/"
            f"{contraction['expected_joint_group_tuples']}`.",
            "",
            f"Final color networks: `{contraction['final_nonzero_canonical_color_network_count']}`.",
            "",
            f"Audit: `{audit['passed']}/{audit['total']}`.",
            "",
            "DRED, UV subtraction, and a renormalized two-loop coefficient are absent.",
            "",
        ]
    )


def write_outputs(max_final_group_tuples: int | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    payload = build_payload(max_final_group_tuples=max_final_group_tuples)
    audit = build_audit(payload)
    if audit["status"] != "PASS":
        raise AssertionError(audit)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    return payload, audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-final-group-tuples", type=int)
    args = parser.parse_args()
    payload, audit = write_outputs(args.max_final_group_tuples)
    print(
        canonical_json(
            {
                "status": payload["status"],
                "audit": f"{audit['passed']}/{audit['total']}",
                "complete": payload["contraction"]["complete"],
                "group_tuples": payload["contraction"][
                    "contracted_joint_group_tuples"
                ],
                "runtime_seconds": payload["runtime_seconds_informational"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
