#!/usr/bin/env python3
"""Proposal-only Step-6 exact color-network compiler.

Input is restricted to the Project Step-6 grammar, GraphIR, typed Wick join,
and pre-D-algebra AmplitudeIR.  The compiler never reads review or external
target material.  It compiles only the adjoint color network; D-algebra,
integrals, graph sums, Jacobi reduction, and loop coefficients are absent.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
import json
from math import factorial, prod
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:
    from scripts import step6_two_loop_amplitude_ir as amplitude
    from scripts import step6_two_loop_grammar as grammar
    from scripts import step6_two_loop_graphir as graphir
    from scripts import step6_two_loop_wick as wick
except ModuleNotFoundError:  # direct execution
    import step6_two_loop_amplitude_ir as amplitude
    import step6_two_loop_grammar as grammar
    import step6_two_loop_graphir as graphir
    import step6_two_loop_wick as wick


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated/step6/two-loop-color-tensor"
GENERATED_JSON = GENERATED_DIR / "color-network.json"
GENERATED_MD = GENERATED_DIR / "color-network.md"
AUDIT = ROOT / "audits/step6-two-loop-color-tensor-verification.json"

SCHEMA_VERSION = "step6.color_tensor.v1"
STATUS = "PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE"
STAGE = "EXACT_COLOR_NETWORK_BEFORE_DALGEBRA"
FREE_INDEX_ORDER = ("A", "B", "R", "S")
COMPONENT_RULE = "[Y,Z]^C=i*c[A,B,C]*Y^A*Z^B"
ORDERED_C_POLICY = "ONE_ORDERED_C_NODE_NO_REVERSE_NO_EXTRA_I"
JACOBI_STATUS = "BLOCKED_UNRESOLVED_JACOBI_EQUIVALENCE"

_CANONICAL_NETWORK_CACHE: dict[tuple[str, tuple[str, ...], bool], dict[str, Any]] = {}
_METRIC_REDUCTION_CACHE: dict[str, dict[str, Any]] = {}


class ColorTensorError(ValueError):
    """Base fail-closed color compiler error."""


class ColorASTError(ColorTensorError):
    """Raised for an unsupported or malformed Project color AST."""


class PortSaturationError(ColorTensorError):
    """Raised for a missing, duplicate, or unjoined V port."""


class FreeIndexError(ColorTensorError):
    """Raised when the color network has free indices other than A,B,R,S."""


class OrderedBracketError(ColorTensorError):
    """Raised when one Project bracket is not one ordered c node."""


class MetricReductionError(ColorTensorError):
    """Raised when exact kappa--kappa-inverse contraction is ambiguous."""


class CanonicalizationError(ColorTensorError):
    """Raised when an exact dummy-index canonical form cannot be certified."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def permutation_parity(values: Sequence[str], sorted_values: Sequence[str]) -> int:
    """Return 0 for even and 1 for odd, with distinct entries required."""
    if len(values) != len(set(values)) or sorted(values) != sorted(sorted_values):
        raise CanonicalizationError("permutation parity requires two distinct equal sets")
    positions = {value: position for position, value in enumerate(sorted_values)}
    image = [positions[value] for value in values]
    inversions = sum(
        image[left] > image[right]
        for left in range(len(image))
        for right in range(left + 1, len(image))
    )
    return inversions % 2


def index_sort_key(index: str) -> tuple[int, int | str]:
    if index in FREE_INDEX_ORDER:
        return (0, FREE_INDEX_ORDER.index(index))
    if index.startswith("d") and index[1:].isdigit():
        return (1, int(index[1:]))
    return (2, index)


def tensor_projection(tensor: Mapping[str, Any]) -> dict[str, Any]:
    """Remove provenance while retaining the exact tensor and ordered c slots."""
    kind = str(tensor["kind"])
    if kind == "c":
        return {
            "kind": "c",
            "ordered_indices": list(tensor["ordered_indices"]),
        }
    if kind in {"kappa", "kappa_inverse"}:
        return {
            "kind": kind,
            "indices": list(tensor["indices"]),
            "variance": tensor["variance"],
        }
    raise ColorASTError(f"unsupported tensor kind {kind}")


def validate_ordered_c_node(tensor: Mapping[str, Any]) -> None:
    if tensor.get("kind") != "c":
        raise OrderedBracketError("ordered c validator received a non-c tensor")
    if tensor.get("component_rule") != COMPONENT_RULE:
        raise OrderedBracketError("Project bracket component rule changed")
    if len(tensor.get("ordered_indices", ())) != 3:
        raise OrderedBracketError("ordered c tensor must have three slots")
    if int(tensor.get("extra_i_power", -1)) != 0:
        raise OrderedBracketError("bracket i is already owned by the source Q(i)")
    if bool(tensor.get("reverse_bracket_term_emitted", True)):
        raise OrderedBracketError("a Project bracket is not forward-minus-reverse")
    if tensor.get("emission_policy") != ORDERED_C_POLICY:
        raise OrderedBracketError("ordered bracket emission policy changed")


TRANSPARENT_COLOR_OPS = {
    "FlatD",
    "FlatBarD",
    "BarD2",
    "D2",
    "SpinorRaise",
}


@dataclass
class ASTCompileState:
    vertex_id: str
    source_term_id: str
    port_bindings: dict[str, dict[str, Any]]
    tensors: list[dict[str, Any]]
    leaf_records: list[dict[str, Any]]
    free_color_outputs: list[dict[str, Any]]
    bracket_outputs: list[dict[str, Any]]

    def compile_node(
        self,
        node: Mapping[str, Any],
        path: tuple[int, ...] = (),
        requested_output: str | None = None,
    ) -> str:
        op = str(node["op"])
        args = list(node.get("args", ()))
        attrs = dict(node.get("attrs", {}))
        path_text = "root" if not path else ".".join(map(str, path))

        if op == "V":
            if args:
                raise ColorASTError("V leaf cannot have arguments")
            port_id = str(attrs.get("port_id"))
            binding = self.port_bindings.get(port_id)
            if binding is None:
                raise PortSaturationError(f"unbound grammar V port {port_id}")
            if any(row["grammar_port_id"] == port_id for row in self.leaf_records):
                raise PortSaturationError(f"grammar V port {port_id} occurs twice")
            fixed = binding.get("fixed_external_color")
            if fixed is not None and requested_output is not None and fixed != requested_output:
                raise FreeIndexError(
                    f"background color {fixed} cannot be rebound to {requested_output}"
                )
            output = str(fixed or requested_output or binding["default_index"])
            self.leaf_records.append(
                {
                    "vertex_id": self.vertex_id,
                    "source_term_id": self.source_term_id,
                    "grammar_port_id": port_id,
                    "topology_port_id": binding["topology_port_id"],
                    "port_kind": binding["port_kind"],
                    "color_index": output,
                    "external_momentum": binding.get("external_momentum"),
                    "ast_path": list(path),
                }
            )
            return output

        if op in TRANSPARENT_COLOR_OPS:
            if len(args) != 1:
                raise ColorASTError(f"transparent color op {op} must be unary")
            return self.compile_node(args[0], path + (0,), requested_output)

        if op == "FreeColor":
            if len(args) != 1:
                raise ColorASTError("FreeColor must be unary")
            child_output = self.compile_node(args[0], path + (0,), requested_output)
            self.free_color_outputs.append(
                {
                    "ast_path": list(path),
                    "declared_source_color": attrs.get("color"),
                    "resolved_color_index": child_output,
                    "requested_external_output": requested_output,
                }
            )
            return child_output

        if op == "AdjointBracket":
            if len(args) != 2:
                raise OrderedBracketError("AdjointBracket must have two ordered arguments")
            if attrs.get("component_rule") != COMPONENT_RULE:
                raise OrderedBracketError("AdjointBracket component rule changed")
            output = requested_output or f"o::{self.vertex_id}::{path_text}"
            left = self.compile_node(args[0], path + (0,), None)
            right = self.compile_node(args[1], path + (1,), None)
            tensor = {
                "kind": "c",
                "ordered_indices": [left, right, output],
                "ordered_leg_roles": ["left_input", "right_input", "bracket_output"],
                "component_rule": COMPONENT_RULE,
                "source_color_tensor": attrs.get("color_tensor"),
                "source_output_color": attrs.get("output_color"),
                "source_ast_path": list(path),
                "source_term_id": self.source_term_id,
                "vertex_id": self.vertex_id,
                "extra_i_power": 0,
                "reverse_bracket_term_emitted": False,
                "emission_policy": ORDERED_C_POLICY,
                "coefficient_i_owner": "SOURCE_TERM_QI",
            }
            validate_ordered_c_node(tensor)
            self.tensors.append(tensor)
            self.bracket_outputs.append(
                {
                    "ast_path": list(path),
                    "resolved_color_index": output,
                    "ordered_input_indices": [left, right],
                }
            )
            return output

        raise ColorASTError(f"unsupported nested color op {op}")


def compile_root_color_ast(
    expression: Mapping[str, Any],
    *,
    vertex_id: str,
    source_term_id: str,
    topology_role: str,
    port_bindings: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    state = ASTCompileState(
        vertex_id=vertex_id,
        source_term_id=source_term_id,
        port_bindings={key: dict(value) for key, value in port_bindings.items()},
        tensors=[],
        leaf_records=[],
        free_color_outputs=[],
        bracket_outputs=[],
    )
    op = str(expression["op"])
    args = list(expression.get("args", ()))
    if topology_role == "COMPOSITE_INSERTION":
        if op != "OrderedProduct" or len(args) != 2:
            raise ColorASTError("two-letter insertion root must be OrderedProduct(A,B)")
        outputs = [
            state.compile_node(args[0], (0,), "A"),
            state.compile_node(args[1], (1,), "B"),
        ]
        if outputs != ["A", "B"]:
            raise FreeIndexError("insertion FreeColor outputs are not ordered A,B")
        root = {
            "kind": "ordered_free_color_product",
            "free_index_order": ["A", "B"],
        }
    elif topology_role == "ACTION_VERTEX":
        if op != "GaugeInvariantPairing" or len(args) != 2:
            raise ColorASTError("gauge action vertex root must be GaugeInvariantPairing")
        left = state.compile_node(args[0], (0,), None)
        right = state.compile_node(args[1], (1,), None)
        state.tensors.append(
            {
                "kind": "kappa",
                "indices": [left, right],
                "variance": "lower",
                "symmetric": True,
                "source_ast_path": [],
                "source_term_id": source_term_id,
                "vertex_id": vertex_id,
            }
        )
        root = {
            "kind": "gauge_invariant_pairing",
            "indices": [left, right],
            "source_color_pairing": expression.get("attrs", {}).get("color_pairing"),
        }
    else:
        raise ColorASTError(f"unsupported topology role {topology_role}")

    expected_ports = set(port_bindings)
    actual_ports = [row["grammar_port_id"] for row in state.leaf_records]
    if len(actual_ports) != len(set(actual_ports)):
        raise PortSaturationError("one grammar V port compiled more than once")
    if set(actual_ports) != expected_ports:
        missing = sorted(expected_ports - set(actual_ports))
        extra = sorted(set(actual_ports) - expected_ports)
        raise PortSaturationError(f"grammar V port mismatch missing={missing} extra={extra}")
    for tensor in state.tensors:
        if tensor["kind"] == "c":
            validate_ordered_c_node(tensor)
    return {
        "root": root,
        "tensors": state.tensors,
        "leaf_records": state.leaf_records,
        "free_color_outputs": state.free_color_outputs,
        "bracket_outputs": state.bracket_outputs,
    }


def _permutation_from_orders(source: Sequence[str], target: Sequence[str]) -> list[int]:
    if len(source) != len(target) or set(source) != set(target):
        raise PortSaturationError("external topology port orders are not permutations")
    positions = {value: position for position, value in enumerate(target)}
    return [positions[value] for value in source]


def local_option_port_bindings(
    parent: amplitude.AmplitudeParent,
    option: Mapping[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    bindings: dict[str, dict[str, Any]] = {}
    for attachment in option["quantum_attachment"]:
        grammar_port = str(attachment["grammar_port_id"])
        topology_port = str(attachment["topology_port_id"])
        if grammar_port in bindings:
            raise PortSaturationError("duplicate quantum grammar port")
        bindings[grammar_port] = {
            "port_kind": "QUANTUM_V",
            "topology_port_id": topology_port,
            "default_index": f"v::{topology_port}",
            "fixed_external_color": None,
        }

    projection_ref = option["background_projection"]
    candidate_id = projection_ref["projection_candidate_id"]
    background_rows: list[Mapping[str, Any]] = []
    if candidate_id is not None:
        candidate = parent.projection_dictionary.get(candidate_id)
        if candidate is None:
            raise PortSaturationError("missing AmplitudeIR projection candidate")
        background_rows = list(candidate["background_port_projections"])
    external_by_momentum = {"p1": "R", "p2": "S"}
    for row in background_rows:
        grammar_port = str(row["grammar_port_id"])
        topology_port = str(row["topology_port_id"])
        momentum = str(row["external_momentum"])
        if grammar_port in bindings:
            raise PortSaturationError("grammar port is both background and quantum")
        if momentum not in external_by_momentum:
            raise FreeIndexError(f"unsupported external momentum label {momentum}")
        bindings[grammar_port] = {
            "port_kind": "BACKGROUND_V",
            "topology_port_id": topology_port,
            "default_index": external_by_momentum[momentum],
            "fixed_external_color": external_by_momentum[momentum],
            "external_momentum": momentum,
        }

    source_order = [str(row["topology_port_id"]) for row in background_rows]
    topology_order = sorted(
        source_order,
        key=lambda port: (
            0 if next(
                str(row["external_momentum"])
                for row in background_rows
                if str(row["topology_port_id"]) == port
            ) == "p1" else 1,
            port,
        ),
    )
    if source_order:
        permutation = _permutation_from_orders(source_order, topology_order)
        parity = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        ) % 2
    else:
        permutation = []
        parity = 0
    ledger = {
        "source_assignment_topology_ports": source_order,
        "p1_p2_topology_port_order": topology_order,
        "permutation": permutation,
        "permutation_parity": parity,
        "external_label_permutation_sign": 1,
        "sign_certificate": "ALL_EXTERNAL_BACKGROUND_V_LEAVES_HAVE_PARITY_ZERO",
        "fermion_sign_inferred": False,
    }
    return bindings, ledger


def compile_local_color_option(
    parent: amplitude.AmplitudeParent,
    vertex: Mapping[str, Any],
    option: Mapping[str, Any],
) -> dict[str, Any]:
    term = parent.term_dictionary[option["source_term_id"]]
    bindings, external_ledger = local_option_port_bindings(parent, option)
    source_ports = {str(port["port_id"]) for port in term["ports"]}
    if set(bindings) != source_ports:
        raise PortSaturationError("AmplitudeIR B/Q split does not cover the source AST ports")
    compiled = compile_root_color_ast(
        term["expression_ast"],
        vertex_id=str(vertex["vertex_id"]),
        source_term_id=str(option["source_term_id"]),
        topology_role=str(vertex["role"]),
        port_bindings=bindings,
    )
    topology_to_index: dict[str, str] = {}
    for leaf in compiled["leaf_records"]:
        topology_port = str(leaf["topology_port_id"])
        if topology_port in topology_to_index:
            raise PortSaturationError("two V leaves occupy one topology port")
        topology_to_index[topology_port] = str(leaf["color_index"])
    expected_topology_ports = {
        str(port) for port in vertex["quantum_ports"]
    } | {str(port["port_id"]) for port in vertex["background_ports"]}
    if set(topology_to_index) != expected_topology_ports:
        raise PortSaturationError("compiled V leaves do not saturate topology vertex ports")
    row = {
        "local_amplitude_option_id": option["local_amplitude_option_id"],
        "source_term_id": option["source_term_id"],
        "vertex_id": vertex["vertex_id"],
        "topology_role": vertex["role"],
        "orientation": option["orientation"],
        "source_coefficient_Qi": option["coefficient_raw"],
        "source_coefficient_i_power": int(option["coefficient_raw"]["i_power_reduced"]),
        "ordered_c_node_count": sum(t["kind"] == "c" for t in compiled["tensors"]),
        "color_i_factor_added_by_compiler": 0,
        "reverse_bracket_terms_added_by_compiler": 0,
        "topology_port_to_color_index": dict(sorted(topology_to_index.items())),
        "external_label_permutation_ledger": external_ledger,
        **compiled,
    }
    row["local_color_option_sha256"] = digest(row)
    return row


def all_indices(tensors: Sequence[Mapping[str, Any]]) -> list[str]:
    result: list[str] = []
    for tensor in tensors:
        if tensor["kind"] == "c":
            result.extend(map(str, tensor["ordered_indices"]))
        else:
            result.extend(map(str, tensor["indices"]))
    return result


def tensor_indices(tensor: Mapping[str, Any]) -> list[str]:
    return list(
        map(
            str,
            tensor["ordered_indices"] if tensor["kind"] == "c" else tensor["indices"],
        )
    )


def validate_free_indices(
    tensors: Sequence[Mapping[str, Any]],
    *,
    expected: Sequence[str] = FREE_INDEX_ORDER,
) -> dict[str, Any]:
    counts = Counter(all_indices(tensors))
    free = tuple(index for index in expected if counts[index] == 1)
    wrong_expected = {index: counts[index] for index in expected if counts[index] != 1}
    unexpected_free = sorted(
        index for index, count in counts.items() if count == 1 and index not in expected
    )
    overused = sorted(index for index, count in counts.items() if count not in {1, 2})
    if wrong_expected or unexpected_free or overused:
        raise FreeIndexError(
            "invalid free/dummy incidence "
            f"expected={wrong_expected} unexpected={unexpected_free} overused={overused}"
        )
    return {
        "free_index_order": list(free),
        "each_free_index_occurs_once": True,
        "each_dummy_index_occurs_twice": all(
            count == 2 for index, count in counts.items() if index not in expected
        ),
        "incidence_count": dict(sorted(counts.items())),
    }


def attach_propagator_color_metrics(
    parent: amplitude.AmplitudeParent,
    local_rows: Sequence[Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_vertex = {str(row["vertex_id"]): row for row in local_rows}
    if set(by_vertex) != {str(vertex["vertex_id"]) for vertex in parent.graph["vertices"]}:
        raise PortSaturationError("one local color option per topology vertex is required")
    endpoint_seen: list[str] = []
    propagators: list[dict[str, Any]] = []
    for edge in parent.graph["internal_edges"]:
        source_vertex = str(edge["source"])
        target_vertex = str(edge["target"])
        source_port = str(edge["source_port"])
        target_port = str(edge["target_port"])
        try:
            source_index = by_vertex[source_vertex]["topology_port_to_color_index"][
                source_port
            ]
            target_index = by_vertex[target_vertex]["topology_port_to_color_index"][
                target_port
            ]
        except KeyError as exc:
            raise PortSaturationError("propagator endpoint has no compiled V leaf") from exc
        endpoint_seen.extend([source_port, target_port])
        propagators.append(
            {
                "kind": "kappa_inverse",
                "indices": [source_index, target_index],
                "variance": "upper",
                "symmetric": True,
                "edge_id": edge["edge_id"],
                "source_topology_port": source_port,
                "target_topology_port": target_port,
                "orientation": parent.orientation,
            }
        )
    expected_quantum = sorted(
        str(port)
        for vertex in parent.graph["vertices"]
        for port in vertex["quantum_ports"]
    )
    if sorted(endpoint_seen) != expected_quantum or len(endpoint_seen) != len(set(endpoint_seen)):
        raise PortSaturationError("each topology quantum V leaf must join one propagator")
    tensors = [
        tensor
        for row in local_rows
        for tensor in row["tensors"]
    ] + propagators
    return tensors, propagators


def _substitute_index(
    tensors: Sequence[Mapping[str, Any]], old: str, new: str
) -> list[dict[str, Any]]:
    if old == new:
        return [dict(tensor) for tensor in tensors]
    if old in FREE_INDEX_ORDER and new in FREE_INDEX_ORDER:
        raise MetricReductionError("metric contraction cannot identify two free indices")
    output: list[dict[str, Any]] = []
    for tensor in tensors:
        row = dict(tensor)
        key = "ordered_indices" if row["kind"] == "c" else "indices"
        row[key] = [new if str(index) == old else str(index) for index in row[key]]
        output.append(row)
    return output


def _metric_contraction_successors(
    tensors: Sequence[Mapping[str, Any]],
) -> list[tuple[list[dict[str, Any]], dict[str, Any]]]:
    successors: list[tuple[list[dict[str, Any]], dict[str, Any]]] = []
    lowers = [i for i, tensor in enumerate(tensors) if tensor["kind"] == "kappa"]
    uppers = [
        i for i, tensor in enumerate(tensors) if tensor["kind"] == "kappa_inverse"
    ]
    for lower_index in lowers:
        lower = tensor_indices(tensors[lower_index])
        for upper_index in uppers:
            upper = tensor_indices(tensors[upper_index])
            shared = sorted(set(lower) & set(upper))
            if not shared:
                continue
            if len(shared) != 1:
                raise MetricReductionError(
                    "closed kappa trace requires an explicit adjoint-dimension node"
                )
            shared_index = shared[0]
            lower_other = next(index for index in lower if index != shared_index)
            upper_other = next(index for index in upper if index != shared_index)
            remaining = [
                dict(tensor)
                for position, tensor in enumerate(tensors)
                if position not in {lower_index, upper_index}
            ]
            if lower_other in FREE_INDEX_ORDER:
                old, new = upper_other, lower_other
            elif upper_other in FREE_INDEX_ORDER:
                old, new = lower_other, upper_other
            else:
                old, new = sorted((lower_other, upper_other), reverse=True)
            reduced = _substitute_index(remaining, old, new)
            successors.append(
                (
                    reduced,
                    {
                        "rule": "kappa_ab*kappa_inverse^ac=delta_b^c",
                        "shared_index": shared_index,
                        "identified": {"old": old, "new": new},
                        "removed_tensor_positions": [lower_index, upper_index],
                    },
                )
            )
    return successors


def _incidence_refinement_cells(
    tensors: Sequence[Mapping[str, Any]],
    dummy: Sequence[str],
    *,
    antisymmetry: bool = False,
) -> list[list[str]]:
    indices = sorted(set(all_indices(tensors)))
    colors: dict[str, str] = {
        index: (f"F{FREE_INDEX_ORDER.index(index)}" if index in FREE_INDEX_ORDER else "D")
        for index in indices
    }
    for _ in range(len(indices) + 2):
        signatures: dict[str, str] = {}
        for index in indices:
            incidences: list[Any] = []
            for tensor in tensors:
                slots = tensor_indices(tensor)
                for slot, value in enumerate(slots):
                    if value != index:
                        continue
                    if tensor["kind"] == "c" and not antisymmetry:
                        descriptor = (
                            "c",
                            slot,
                            tuple(colors[other] for other in slots),
                        )
                    elif tensor["kind"] == "c":
                        descriptor = (
                            "c_antisymmetric",
                            tuple(sorted(colors[other] for other in slots)),
                        )
                    else:
                        descriptor = (
                            tensor["kind"],
                            tuple(sorted(colors[other] for other in slots)),
                        )
                    incidences.append(descriptor)
            signatures[index] = canonical_json((colors[index], sorted(incidences)))
        palette = {value: f"C{n}" for n, value in enumerate(sorted(set(signatures.values())))}
        refined = {index: palette[signatures[index]] for index in indices}
        for free in FREE_INDEX_ORDER:
            if free in refined:
                refined[free] = f"F{FREE_INDEX_ORDER.index(free)}"
        if refined == colors:
            break
        colors = refined
    grouped: dict[str, list[str]] = defaultdict(list)
    for index in dummy:
        grouped[colors[index]].append(index)
    return [sorted(grouped[color]) for color in sorted(grouped)]


def _canonical_tensor_rows(
    tensors: Sequence[Mapping[str, Any]],
    mapping: Mapping[str, str],
    *,
    antisymmetry: bool,
) -> tuple[list[dict[str, Any]], int, bool]:
    rows: list[dict[str, Any]] = []
    sign = 1
    zero = False
    for tensor in tensors:
        projected = tensor_projection(tensor)
        if projected["kind"] == "c":
            ordered = [mapping.get(index, index) for index in projected["ordered_indices"]]
            if antisymmetry:
                if len(set(ordered)) != 3:
                    zero = True
                    continue
                canonical = sorted(ordered, key=index_sort_key)
                if permutation_parity(ordered, canonical):
                    sign *= -1
                projected["canonical_indices"] = canonical
                projected["ordered_indices_before_antisymmetry"] = ordered
                projected["antisymmetry_sign"] = (
                    -1 if permutation_parity(ordered, canonical) else 1
                )
                projected.pop("ordered_indices")
            else:
                projected["ordered_indices"] = ordered
        else:
            projected["indices"] = sorted(
                [mapping.get(index, index) for index in projected["indices"]],
                key=index_sort_key,
            )
        rows.append(projected)
    rows.sort(key=canonical_json)
    return rows, sign, zero


def canonicalize_network(
    tensors: Sequence[Mapping[str, Any]],
    *,
    fixed_indices: Sequence[str] = FREE_INDEX_ORDER,
    antisymmetry: bool,
) -> dict[str, Any]:
    cache_key = (
        digest([tensor_projection(tensor) for tensor in tensors]),
        tuple(fixed_indices),
        antisymmetry,
    )
    cached = _CANONICAL_NETWORK_CACHE.get(cache_key)
    if cached is not None:
        return deepcopy(cached)
    indices = sorted(set(all_indices(tensors)))
    fixed = tuple(index for index in fixed_indices if index in indices)
    dummy = [index for index in indices if index not in fixed]
    cells = _incidence_refinement_cells(
        tensors, dummy, antisymmetry=antisymmetry
    )
    if not cells:
        cells = [[]]
    enumeration_size = prod(factorial(len(cell)) for cell in cells)
    if enumeration_size > 200_000:
        raise CanonicalizationError(
            f"dummy-index canonical enumeration {enumeration_size} exceeds certified bound"
        )
    cell_permutations = [list(permutations(cell)) for cell in cells]
    best_serialization: str | None = None
    best_rows: list[dict[str, Any]] | None = None
    best_signs: set[int] = set()
    best_zero = False
    for choices in product(*cell_permutations):
        mapping: dict[str, str] = {}
        ordinal = 0
        for original_cell, chosen_order in zip(cells, choices, strict=True):
            if set(original_cell) != set(chosen_order):
                raise CanonicalizationError("dummy permutation cell changed")
            for original in chosen_order:
                mapping[original] = f"d{ordinal}"
                ordinal += 1
        rows, sign, zero = _canonical_tensor_rows(
            tensors, mapping, antisymmetry=antisymmetry
        )
        serialization = canonical_json(rows)
        if best_serialization is None or serialization < best_serialization:
            best_serialization = serialization
            best_rows = rows
            best_signs = {sign}
            best_zero = zero
        elif serialization == best_serialization:
            best_signs.add(sign)
            best_zero = best_zero or zero
    if best_rows is None or best_serialization is None:
        raise CanonicalizationError("no dummy-index canonical candidate")
    antisymmetric_automorphism_zero = antisymmetry and best_signs == {-1, 1}
    zero = best_zero or antisymmetric_automorphism_zero
    sign = 0 if zero else next(iter(best_signs))
    signature_record = {
        "free_index_order": list(FREE_INDEX_ORDER),
        "canonical_tensors": [] if zero else best_rows,
        "overall_antisymmetry_sign": sign,
        "zero_by_antisymmetry": zero,
        "dummy_index_count": len(dummy),
        "canonical_enumeration_size": enumeration_size,
        "jacobi_rewrite_applied": False,
    }
    result = {
        **signature_record,
        "signature_sha256": digest(signature_record),
    }
    _CANONICAL_NETWORK_CACHE[cache_key] = deepcopy(result)
    return result


def reduce_metrics_exact(tensors: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    cache_key = digest([tensor_projection(tensor) for tensor in tensors])
    cached = _METRIC_REDUCTION_CACHE.get(cache_key)
    if cached is not None:
        return deepcopy(cached)
    terminals: dict[str, tuple[list[dict[str, Any]], list[dict[str, Any]]]] = {}

    def visit(current: list[dict[str, Any]], ledger: list[dict[str, Any]]) -> None:
        successors = _metric_contraction_successors(current)
        if not successors:
            canonical = canonicalize_network(current, antisymmetry=False)
            key = canonical["signature_sha256"]
            terminals.setdefault(key, (current, ledger))
            return
        for successor, step in successors:
            visit(successor, [*ledger, step])

    visit([dict(tensor) for tensor in tensors], [])
    if len(terminals) != 1:
        raise MetricReductionError(
            f"metric rewrite paths have {len(terminals)} inequivalent terminal networks"
        )
    terminal, ledger = next(iter(terminals.values()))
    if any(
        lower["kind"] == "kappa"
        and upper["kind"] == "kappa_inverse"
        and set(tensor_indices(lower)) & set(tensor_indices(upper))
        for lower in terminal
        for upper in terminal
    ):
        raise MetricReductionError("reducible kappa--kappa-inverse pair remains")
    result = {
        "tensors": terminal,
        "rewrite_ledger": ledger,
        "rewrite_count": len(ledger),
        "all_rewrite_paths_same_terminal": True,
        "terminal_path_count": len(terminals),
    }
    _METRIC_REDUCTION_CACHE[cache_key] = deepcopy(result)
    return result


def local_group_signature(row: Mapping[str, Any]) -> str:
    interface_indices = sorted(
        set(row["topology_port_to_color_index"].values()) | set(FREE_INDEX_ORDER)
    )
    canonical = canonicalize_network(
        row["tensors"], fixed_indices=interface_indices, antisymmetry=False
    )
    record = {
        "canonical_local_network": canonical,
        "topology_port_to_color_index": row["topology_port_to_color_index"],
        "external_label_permutation_ledger": row[
            "external_label_permutation_ledger"
        ],
        "ordered_c_node_count": row["ordered_c_node_count"],
        "color_i_factor_added_by_compiler": row["color_i_factor_added_by_compiler"],
        "reverse_bracket_terms_added_by_compiler": row[
            "reverse_bracket_terms_added_by_compiler"
        ],
    }
    return digest(record)


def group_local_options(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[local_group_signature(row)].append(row)
    return [
        {
            "local_color_signature_sha256": signature,
            "multiplicity": len(groups[signature]),
            "representative": dict(groups[signature][0]),
            "local_amplitude_option_ids": sorted(
                str(row["local_amplitude_option_id"]) for row in groups[signature]
            ),
        }
        for signature in sorted(groups)
    ]


def compile_parent(parent: amplitude.AmplitudeParent) -> dict[str, Any]:
    vertex_by_id = {
        str(vertex["vertex_id"]): vertex for vertex in parent.graph["vertices"]
    }
    local_catalog: dict[str, list[dict[str, Any]]] = {}
    grouped_catalog: dict[str, list[dict[str, Any]]] = {}
    for vertex_id in parent.vertex_order:
        rows = [
            compile_local_color_option(parent, vertex_by_id[vertex_id], option)
            for option in parent.local_options[vertex_id]
        ]
        local_catalog[vertex_id] = rows
        grouped_catalog[vertex_id] = group_local_options(rows)

    reduced_hist: dict[str, dict[str, Any]] = {}
    unreduced_hist: dict[str, dict[str, Any]] = {}
    factorized_hist: dict[str, dict[str, Any]] = {}
    external_ledger_dictionary: dict[str, list[dict[str, Any]]] = {}
    grouped_tuple_count = 0
    for choices in product(*(grouped_catalog[v] for v in parent.vertex_order)):
        grouped_tuple_count += 1
        multiplicity = prod(int(choice["multiplicity"]) for choice in choices)
        representatives = [choice["representative"] for choice in choices]
        tensors, propagators = attach_propagator_color_metrics(parent, representatives)
        incidence_before = validate_free_indices(tensors)
        unreduced = canonicalize_network(tensors, antisymmetry=False)
        metric_reduction = reduce_metrics_exact(tensors)
        incidence_after = validate_free_indices(metric_reduction["tensors"])
        reduced = canonicalize_network(
            metric_reduction["tensors"], antisymmetry=True
        )
        external_ledgers = [
            row["external_label_permutation_ledger"]
            for row in representatives
            if row["external_label_permutation_ledger"][
                "source_assignment_topology_ports"
            ]
        ]
        ledger_signature = digest(external_ledgers)
        external_ledger_dictionary.setdefault(ledger_signature, external_ledgers)
        ordered_group_ids = [
            choice["local_color_signature_sha256"] for choice in choices
        ]
        ordered_join_factorization_sha256 = digest(ordered_group_ids)
        for histogram, network in ((unreduced_hist, unreduced), (reduced_hist, reduced)):
            key = network["signature_sha256"]
            if key not in histogram:
                histogram[key] = {
                    "color_network_signature_sha256": key,
                    "multiplicity": 0,
                    "network": network,
                }
            histogram[key]["multiplicity"] += multiplicity
        factorized_key = digest(
            {
                "reduced_color_network": reduced["signature_sha256"],
                "external_label_ledger": ledger_signature,
                "ordered_local_option_factor_sets": (
                    ordered_join_factorization_sha256
                ),
            }
        )
        if factorized_key not in factorized_hist:
            factorized_hist[factorized_key] = {
                "factorized_signature_sha256": factorized_key,
                "multiplicity": 0,
                "reduced_color_network_signature_sha256": reduced[
                    "signature_sha256"
                ],
                "unreduced_color_network_signature_sha256": unreduced[
                    "signature_sha256"
                ],
                "external_label_permutation_ledger_ref": ledger_signature,
                "bosonic_external_permutation_sign": 1,
                "fermion_sign_inferred": False,
                "ordered_local_color_group_ids_in_vertex_order": ordered_group_ids,
                "ordered_local_amplitude_option_join_factorization_sha256": (
                    ordered_join_factorization_sha256
                ),
                "metric_rewrite_count": metric_reduction["rewrite_count"],
            }
        factorized_hist[factorized_key]["multiplicity"] += multiplicity

    cardinality = sum(row["multiplicity"] for row in factorized_hist.values())
    if cardinality != parent.cardinality:
        raise ColorTensorError(
            f"factorized color histogram {cardinality} != amplitude {parent.cardinality}"
        )
    parent_row = {
        "graph_id": parent.graph["graph_id"],
        "graph_hash": parent.graph["graph_hash"],
        "orientation": parent.orientation,
        "orientation_hash": parent.graph["orientations"][parent.orientation][
            "orientation_hash"
        ],
        "vertex_order": list(parent.vertex_order),
        "free_index_order": list(FREE_INDEX_ORDER),
        "labeled_amplitude_cardinality": parent.cardinality,
        "local_option_counts": {
            vertex: len(local_catalog[vertex]) for vertex in parent.vertex_order
        },
        "local_color_group_counts": {
            vertex: len(grouped_catalog[vertex]) for vertex in parent.vertex_order
        },
        "local_color_option_catalog": local_catalog,
        "factorized_local_color_catalog": {
            vertex: [
                {
                    "local_color_signature_sha256": group[
                        "local_color_signature_sha256"
                    ],
                    "multiplicity": group["multiplicity"],
                    "representative_local_amplitude_option_id": group[
                        "representative"
                    ]["local_amplitude_option_id"],
                    "local_amplitude_option_ids": group[
                        "local_amplitude_option_ids"
                    ],
                }
                for group in grouped_catalog[vertex]
            ]
            for vertex in parent.vertex_order
        },
        "factorized_group_tuple_count": grouped_tuple_count,
        "factorized_signature_histogram": [
            factorized_hist[key] for key in sorted(factorized_hist)
        ],
        "factorized_histogram_multiplicity": cardinality,
        "external_label_permutation_ledger_dictionary": dict(
            sorted(external_ledger_dictionary.items())
        ),
        "factorized_histogram_policy": {
            "vertex_order": list(parent.vertex_order),
            "ordered_group_id_tuple_resolves_exact_option_factor_sets": True,
            "future_exact_option_tuple_key": (
                "SHA256(ordered local_amplitude_option_id tuple)"
            ),
            "color_histogram_is_a_marginal_not_a_downstream_product": True,
            "independent_marginal_multiplication_forbidden": True,
        },
        "unreduced_color_network_histogram": [
            unreduced_hist[key] for key in sorted(unreduced_hist)
        ],
        "reduced_color_network_histogram": [
            reduced_hist[key] for key in sorted(reduced_hist)
        ],
        "unique_unreduced_color_network_count": len(unreduced_hist),
        "unique_reduced_color_network_count": len(reduced_hist),
        "port_and_free_index_validation": {
            "every_factorized_group_tuple_checked": True,
            "factorized_group_tuple_count": grouped_tuple_count,
            "each_quantum_leaf_used_exactly_once": True,
            "five_kappa_inverse_metrics_per_tuple": True,
            "free_index_order_before_metric_reduction": incidence_before[
                "free_index_order"
            ],
            "free_index_order_after_metric_reduction": incidence_after[
                "free_index_order"
            ],
        },
        "jacobi_policy": {
            "rewrite_implemented": False,
            "equivalence_status": JACOBI_STATUS,
            "histogram_is_not_Jacobi_quotiented": True,
            "no_Jacobi_related_networks_are_merged_by_claim": True,
        },
        "downstream_fail_closed": {
            "global_supertensor_join": {
                "status": "BLOCKED_COLOR_MARGINAL_REQUIRES_EXACT_OPTION_TUPLE_JOIN",
                "value": None,
            },
            "D_algebra": {"status": "NOT_COMPUTED", "value": None},
            "integral": {"status": "NOT_COMPUTED", "value": None},
            "Jacobi_quotient": {"status": JACOBI_STATUS, "value": None},
            "renormalized_coefficient": {"status": "NOT_COMPUTED", "value": None},
        },
    }
    parent_row["parent_color_payload_sha256"] = digest(parent_row)
    return parent_row


def build_payload() -> dict[str, Any]:
    amplitude_provenance, parents, _ = amplitude.build_runtime()
    rows = [compile_parent(parent) for parent in parents]
    network_dictionary: dict[str, dict[str, Any]] = {
        "unreduced": {},
        "reduced": {},
    }
    for row in rows:
        for stage_key, histogram_key in (
            ("unreduced", "unreduced_color_network_histogram"),
            ("reduced", "reduced_color_network_histogram"),
        ):
            for item in row[histogram_key]:
                signature = item["color_network_signature_sha256"]
                network = item.pop("network")
                prior = network_dictionary[stage_key].setdefault(signature, network)
                if prior != network:
                    raise CanonicalizationError(
                        "one canonical color signature resolved to two networks"
                    )
                item["network_dictionary_ref"] = signature
    total = sum(row["labeled_amplitude_cardinality"] for row in rows)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": STATUS,
        "stage": STAGE,
        "scope": "PURE_GAUGE_TWO_LOOP_THREE_DECORATED_K4_MINUS_EDGE_PARENTS",
        "authority_role": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "external_result_used_as_calculation_input": False,
        "input_firewall": {
            "allowed_modules": [
                "scripts/step6_two_loop_grammar.py",
                "scripts/step6_two_loop_graphir.py",
                "scripts/step6_two_loop_wick.py",
                "scripts/step6_two_loop_amplitude_ir.py",
            ],
            "review_or_external_target_reads": False,
        },
        "input_provenance": {
            "amplitude_runtime_provenance_sha256": digest(amplitude_provenance),
            "generator_sha256": {
                path: file_sha256(ROOT / path)
                for path in (
                    "scripts/step6_two_loop_grammar.py",
                    "scripts/step6_two_loop_graphir.py",
                    "scripts/step6_two_loop_wick.py",
                    "scripts/step6_two_loop_amplitude_ir.py",
                )
            },
        },
        "component_rule": COMPONENT_RULE,
        "ordered_bracket_policy": {
            "emission": ORDERED_C_POLICY,
            "one_c_node_per_AdjointBracket": True,
            "forward_minus_reverse_expansion": False,
            "extra_i_factor": 0,
            "i_factor_owner": "SOURCE_QI_COEFFICIENT",
        },
        "free_index_order": list(FREE_INDEX_ORDER),
        "parents": rows,
        "canonical_color_network_dictionary": network_dictionary,
        "parent_count": len(rows),
        "exact_total_labeled_amplitudes": total,
        "global_unique_unreduced_color_network_count_by_oriented_parent": sum(
            row["unique_unreduced_color_network_count"] for row in rows
        ),
        "global_unique_reduced_color_network_count_by_oriented_parent": sum(
            row["unique_reduced_color_network_count"] for row in rows
        ),
        "Jacobi_equivalence_status": JACOBI_STATUS,
        "global_downstream_fail_closed": {
            "global_supertensor_join": {
                "status": "BLOCKED_COLOR_MARGINAL_REQUIRES_EXACT_OPTION_TUPLE_JOIN",
                "value": None,
            },
            "D_algebra": {"status": "NOT_COMPUTED", "value": None},
            "integral": {"status": "NOT_COMPUTED", "value": None},
            "Jacobi_quotient": {"status": JACOBI_STATUS, "value": None},
            "renormalized_coefficient": {"status": "NOT_COMPUTED", "value": None},
        },
    }
    payload["payload_sha256"] = digest(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    )
    return payload


def gamma2_w2_regression() -> dict[str, Any]:
    gamma_terms = grammar.gamma_terms(2)
    w_terms = grammar.w_terms(2)
    gamma2 = next(term for term in gamma_terms if term.total_v_degree == 2)
    w2 = next(term for term in w_terms if term.total_v_degree == 2)

    def compile_term(term: grammar.Term, label: str) -> dict[str, Any]:
        record = term.as_json()
        bindings = {
            str(port["port_id"]): {
                "port_kind": "REGRESSION_V",
                "topology_port_id": f"{label}.q{ordinal}",
                "default_index": f"v::{label}.q{ordinal}",
                "fixed_external_color": None,
            }
            for ordinal, port in enumerate(record["ports"], start=1)
        }
        state = ASTCompileState(
            vertex_id=label,
            source_term_id=record["term_id"],
            port_bindings=bindings,
            tensors=[],
            leaf_records=[],
            free_color_outputs=[],
            bracket_outputs=[],
        )
        output = state.compile_node(record["expression_ast"])
        c_nodes = [tensor for tensor in state.tensors if tensor["kind"] == "c"]
        if len(c_nodes) != 1:
            raise OrderedBracketError(f"{label} must emit exactly one c node")
        validate_ordered_c_node(c_nodes[0])
        if int(record["coefficient"]["i_power_reduced"]) != 1:
            raise OrderedBracketError(f"{label} Q(i) does not own one i power")
        return {
            "source_term_id": record["term_id"],
            "source_coefficient_Qi": record["coefficient"],
            "resolved_output": output,
            "ordered_c_node": c_nodes[0],
            "leaf_order": [row["grammar_port_id"] for row in state.leaf_records],
            "one_ordered_c": True,
            "extra_i": 0,
            "reverse_bracket_term": False,
        }

    return {
        "Gamma2": compile_term(gamma2, "Gamma2"),
        "W2": compile_term(w2, "W2"),
    }


def exact_checks(payload: Mapping[str, Any]) -> dict[str, bool]:
    parents = payload["parents"]
    local_rows = [
        option
        for parent in parents
        for options in parent["local_color_option_catalog"].values()
        for option in options
    ]
    factorized_rows = [
        row for parent in parents for row in parent["factorized_signature_histogram"]
    ]
    regression = gamma2_w2_regression()
    return {
        "six_oriented_parents_preserved": len(parents) == 6,
        "exact_2985984_labeled_amplitudes": payload[
            "exact_total_labeled_amplitudes"
        ] == 2_985_984,
        "all_parent_histograms_have_exact_cardinality": all(
            parent["factorized_histogram_multiplicity"]
            == parent["labeled_amplitude_cardinality"]
            for parent in parents
        ),
        "one_ordered_c_per_bracket_no_extra_i_no_reverse": all(
            option["color_i_factor_added_by_compiler"] == 0
            and option["reverse_bracket_terms_added_by_compiler"] == 0
            and all(
                tensor["kind"] != "c"
                or (
                    tensor["extra_i_power"] == 0
                    and tensor["reverse_bracket_term_emitted"] is False
                    and tensor["emission_policy"] == ORDERED_C_POLICY
                )
                for tensor in option["tensors"]
            )
            for option in local_rows
        ),
        "Gamma2_W2_ordered_bracket_regression": all(
            row["one_ordered_c"]
            and row["extra_i"] == 0
            and row["reverse_bracket_term"] is False
            and row["source_coefficient_Qi"]["i_power_reduced"] == 1
            for row in regression.values()
        ),
        "only_A_B_R_S_free": all(
            parent["port_and_free_index_validation"][
                "free_index_order_before_metric_reduction"
            ]
            == list(FREE_INDEX_ORDER)
            and parent["port_and_free_index_validation"][
                "free_index_order_after_metric_reduction"
            ]
            == list(FREE_INDEX_ORDER)
            for parent in parents
        ),
        "all_external_permutation_signs_bosonic_plus_one": all(
            row["bosonic_external_permutation_sign"] == 1
            and row["fermion_sign_inferred"] is False
            for row in factorized_rows
        ),
        "direct_reflected_not_merged": {
            (parent["graph_id"], parent["orientation"]) for parent in parents
        }
        == {
            (parent["graph_id"], orientation)
            for parent in parents
            for orientation in ("direct", "reflected")
        },
        "Jacobi_not_applied_and_fail_closed": payload[
            "Jacobi_equivalence_status"
        ] == JACOBI_STATUS
        and all(
            parent["jacobi_policy"]["rewrite_implemented"] is False
            and parent["jacobi_policy"]["histogram_is_not_Jacobi_quotiented"]
            for parent in parents
        ),
        "no_Dalgebra_integral_or_coefficient": all(
            value["value"] is None
            for value in payload["global_downstream_fail_closed"].values()
        ),
        "input_firewall_has_no_review_or_target_read": payload["input_firewall"][
            "review_or_external_target_reads"
        ]
        is False,
    }


def build_audit(
    payload: Mapping[str, Any], artifact_hashes: Mapping[str, str] | None = None
) -> dict[str, Any]:
    checks = exact_checks(payload)
    return {
        "schema_version": "step6.color_tensor.audit.v1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "totals": {
            "checks": len(checks),
            "passed": sum(checks.values()),
            "failed": sum(not value for value in checks.values()),
        },
        "Gamma2_W2_regression": gamma2_w2_regression(),
        "parent_count": payload["parent_count"],
        "exact_total_labeled_amplitudes": payload[
            "exact_total_labeled_amplitudes"
        ],
        "payload_sha256": payload["payload_sha256"],
        "artifact_sha256": dict(artifact_hashes or {}),
    }


def render_markdown(payload: Mapping[str, Any], audit: Mapping[str, Any]) -> str:
    lines = [
        "# Step 6 — exact color-network compiler",
        "",
        f"Status: `{payload['status']}`",
        "",
        "$$",
        "[Y,Z]^C=i\\,c_{ABC}Y^AZ^B,\\qquad N_c(\\operatorname{ad})=1,",
        "\\qquad i_{\\mathrm{color\\ compiler}}=1.",
        "$$",
        "",
        "The last identity means multiplicative factor one: no additional $i$ is emitted.",
        "",
        "$$",
        "\\kappa_{ab}\\kappa^{ac}=\\delta_b{}^c,\\qquad",
        "\\operatorname{Free}= (A,B,R,S).",
        "$$",
        "",
        "| GraphIR | orientation | labeled rows | local group tuples | unreduced networks | reduced networks |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for parent in payload["parents"]:
        lines.append(
            f"| `{parent['graph_id']}` | `{parent['orientation']}` | "
            f"{parent['labeled_amplitude_cardinality']} | "
            f"{parent['factorized_group_tuple_count']} | "
            f"{parent['unique_unreduced_color_network_count']} | "
            f"{parent['unique_reduced_color_network_count']} |"
        )
    lines.extend(
        [
            "",
            "$$",
            f"\\sum_{{\\mathrm{{hist}}}}m={payload['exact_total_labeled_amplitudes']}.",
            "$$",
            "",
            f"Jacobi: `{payload['Jacobi_equivalence_status']}`.",
            "",
            f"Verification: `{audit['status']}`; "
            f"{audit['totals']['passed']}/{audit['totals']['checks']} checks.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs() -> tuple[dict[str, Any], dict[str, Any]]:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    provisional = build_audit(payload)
    GENERATED_JSON.write_text(
        canonical_json(payload) + "\n",
        encoding="utf-8",
    )
    GENERATED_MD.write_text(render_markdown(payload, provisional), encoding="utf-8")
    hashes = {
        str(GENERATED_JSON.relative_to(ROOT)): file_sha256(GENERATED_JSON),
        str(GENERATED_MD.relative_to(ROOT)): file_sha256(GENERATED_MD),
    }
    audit = build_audit(payload, hashes)
    GENERATED_MD.write_text(render_markdown(payload, audit), encoding="utf-8")
    hashes[str(GENERATED_MD.relative_to(ROOT))] = file_sha256(GENERATED_MD)
    audit = build_audit(payload, hashes)
    AUDIT.write_text(
        json.dumps(audit, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload, audit


def main() -> int:
    payload, audit = write_outputs()
    print(
        json.dumps(
            {
                "status": audit["status"],
                "parents": payload["parent_count"],
                "labeled_amplitudes": payload["exact_total_labeled_amplitudes"],
                "checks": audit["totals"],
                "output": str(GENERATED_JSON.relative_to(ROOT)),
            },
            sort_keys=True,
        )
    )
    return 0 if audit["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
