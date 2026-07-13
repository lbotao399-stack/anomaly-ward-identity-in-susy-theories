#!/usr/bin/env python3
"""Exact typed replay frontier for the primitive Step-5 WW contact family.

The module repairs the contact catalogue after the source/reflection/type
correction.  It closes only data that follow from the Project AST, the fixed
Euclidean Gaussian, and ordered GraphIR.  Shared-scope D-algebra, physical I4
projection, and the contact UV pole remain fail-closed.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_project_composites import (  # noqa: E402
    gauge_s4_terms,
    seed_port_assignment_payload,
)
from scripts.step5_one_loop_n2_physical_hessian_family import (  # noqa: E402
    counterterm_graph,
    double_contact_graph,
    insertion_contact_graph,
    seagull_graph,
)
from scripts.step5_supergraph_pipeline import graph_automorphism_order  # noqa: E402
from scripts.step5_ww_contact_quotient import (  # noqa: E402
    ExactMonomial,
    build_payload as build_contact_payload,
)
from scripts.step5_ww_seed import endpoint_rows, physical_triangle  # noqa: E402


OUT = ROOT / "generated/step5/contact-replay/ww-contact-replay.json"
AUDIT_JSON = ROOT / "audits/step5-ww-contact-replay-verification.json"
AUDIT_MD = ROOT / "audits/step5-ww-contact-replay.md"

DERIVATIVE_OPERATORS = {
    "FlatD": lambda attrs: f"D_{attrs['index']}",
    "FlatBarD": lambda attrs: f"barD_{attrs['index']}",
    "D2": lambda attrs: "D^2",
    "BarD2": lambda attrs: "barD^2",
}
COLOR_TRANSPARENT_OPERATORS = {
    "FreeColor",
    "FlatD",
    "FlatBarD",
    "D2",
    "BarD2",
    "SpinorRaise",
}
SUPPORTED_COLOR_OPERATORS = COLOR_TRANSPARENT_OPERATORS | {
    "V",
    "AdjointBracket",
    "OrderedProduct",
    "GaugeInvariantPairing",
}


def stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value: object) -> str:
    return hashlib.sha256(stable_json(value).encode()).hexdigest()


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def node_attrs(node: Mapping[str, object]) -> dict[str, object]:
    attrs = node.get("attrs")
    if not isinstance(attrs, dict):
        raise TypeError("AST attrs must be a dictionary")
    return attrs


def node_args(node: Mapping[str, object]) -> list[dict[str, object]]:
    args = node.get("args")
    if not isinstance(args, list) or any(not isinstance(item, dict) for item in args):
        raise TypeError("AST args must be a list of dictionaries")
    return args


def ast_operators(node: Mapping[str, object]) -> tuple[str, ...]:
    return (str(node["op"]),) + tuple(
        operator for child in node_args(node) for operator in ast_operators(child)
    )


def ast_v_slots(node: Mapping[str, object]) -> tuple[str, ...]:
    if node["op"] == "V":
        return (str(node_attrs(node)["color_slot"]),)
    return tuple(slot for child in node_args(node) for slot in ast_v_slots(child))


def ast_bracket_count(node: Mapping[str, object]) -> int:
    return int(node["op"] == "AdjointBracket") + sum(
        ast_bracket_count(child) for child in node_args(node)
    )


def derivative_scope_index(expression: Mapping[str, object]) -> dict[str, dict[str, object]]:
    """Record the exact support of every derivative ancestor of every V leaf."""

    output: dict[str, dict[str, object]] = {}

    def walk(
        node: Mapping[str, object],
        stack: tuple[dict[str, object], ...],
        spinor_raise_depth: int,
    ) -> None:
        op = str(node["op"])
        attrs = node_attrs(node)
        if op == "V":
            slot = str(attrs["color_slot"])
            output[slot] = {
                "word_outer_to_inner": [row["operator"] for row in stack],
                "scope_supports": [row["support"] for row in stack],
                "scope_support_sizes": [len(row["support"]) for row in stack],
                "singleton_scope": all(len(row["support"]) == 1 for row in stack),
                "spinor_raise_depth": spinor_raise_depth,
            }
            return
        next_stack = stack
        if op in DERIVATIVE_OPERATORS:
            next_stack += (
                {
                    "operator": DERIVATIVE_OPERATORS[op](attrs),
                    "support": list(ast_v_slots(node)),
                },
            )
        next_raise_depth = spinor_raise_depth + int(op == "SpinorRaise")
        for child in node_args(node):
            walk(child, next_stack, next_raise_depth)

    walk(expression, (), 0)
    return output


@dataclass(frozen=True)
class ColorFactor:
    kind: str
    indices: tuple[tuple[str, str], ...]

    def as_json(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "indices": [
                {"label": label, "variance": variance}
                for label, variance in self.indices
            ],
            "rendered": self.render(),
        }

    def render(self) -> str:
        labels = [label for label, _ in self.indices]
        if self.kind == "DELTA":
            return f"delta_{{{labels[0]}}}^{{{labels[1]}}}"
        if self.kind == "C":
            return f"c_{{{labels[0]} {labels[1]}}}^{{{labels[2]}}}"
        if self.kind == "KAPPA_LOWER":
            return f"kappa_{{{labels[0]} {labels[1]}}}"
        if self.kind == "KAPPA_UPPER":
            return f"kappa^{{{labels[0]} {labels[1]}}}"
        raise ValueError(self.kind)


class ColorASTCompiler:
    """Compile componentized Project color ASTs to c/kappa/delta tensors."""

    def __init__(self, port_colors: Mapping[str, str], prefix: str) -> None:
        self.port_colors = dict(port_colors)
        self.prefix = prefix
        self.counter = 0
        self.factors: list[ColorFactor] = []
        self.used_ports: list[str] = []

    def fresh(self) -> str:
        label = f"{self.prefix}d{self.counter}"
        self.counter += 1
        return label

    def compile(
        self,
        node: Mapping[str, object],
        desired_output: str | None = None,
    ) -> str | None:
        op = str(node["op"])
        attrs = node_attrs(node)
        args = node_args(node)
        if op not in SUPPORTED_COLOR_OPERATORS:
            raise ValueError(f"unsupported color AST operator {op}")
        if op == "V":
            slot = str(attrs["color_slot"])
            if slot not in self.port_colors:
                raise KeyError(f"unbound V color port {slot}")
            self.used_ports.append(slot)
            natural = self.port_colors[slot]
            if desired_output is not None and desired_output != natural:
                self.factors.append(
                    ColorFactor("DELTA", ((natural, "DOWN"), (desired_output, "UP")))
                )
                return desired_output
            return natural
        if op in COLOR_TRANSPARENT_OPERATORS:
            if len(args) != 1:
                raise ValueError(f"{op} must have one color-transparent child")
            return self.compile(args[0], desired_output)
        if op == "AdjointBracket":
            if len(args) != 2:
                raise ValueError("AdjointBracket must be binary")
            left = self.compile(args[0])
            right = self.compile(args[1])
            if not isinstance(left, str) or not isinstance(right, str):
                raise TypeError("bracket children need adjoint outputs")
            target = desired_output or self.fresh()
            self.factors.append(
                ColorFactor(
                    "C",
                    ((left, "DOWN"), (right, "DOWN"), (target, "UP")),
                )
            )
            return target
        if op == "OrderedProduct":
            if desired_output is not None:
                raise ValueError("OrderedProduct has two source outputs")
            order = attrs.get("factor_order")
            if not isinstance(order, list) or len(order) != len(args):
                raise TypeError("OrderedProduct needs one output label per factor")
            for child, target in zip(args, order, strict=True):
                self.compile(child, str(target))
            return None
        if op == "GaugeInvariantPairing":
            if desired_output is not None or len(args) != 2:
                raise ValueError("GaugeInvariantPairing is a binary scalar")
            left = self.compile(args[0])
            right = self.compile(args[1])
            if not isinstance(left, str) or not isinstance(right, str):
                raise TypeError("paired factors need adjoint outputs")
            self.factors.append(
                ColorFactor("KAPPA_LOWER", ((left, "DOWN"), (right, "DOWN")))
            )
            return None
        raise AssertionError(op)


def factor_ledger(factors: Sequence[ColorFactor]) -> dict[str, dict[str, int]]:
    ledger: dict[str, Counter[str]] = {}
    for factor in factors:
        for label, variance in factor.indices:
            ledger.setdefault(label, Counter())[variance] += 1
    return {
        label: {"UP": counts["UP"], "DOWN": counts["DOWN"]}
        for label, counts in sorted(ledger.items())
    }


def color_tensor_record(
    expression: Mapping[str, object],
    port_colors: Mapping[str, str],
    edge_pairs: Sequence[tuple[str, str]],
    *,
    prefix: str,
    expected_free: Mapping[str, tuple[int, int]],
) -> dict[str, object]:
    compiler = ColorASTCompiler(port_colors, prefix)
    compiler.compile(expression)
    factors = list(compiler.factors)
    for left_port, right_port in edge_pairs:
        factors.append(
            ColorFactor(
                "KAPPA_UPPER",
                ((port_colors[left_port], "UP"), (port_colors[right_port], "UP")),
            )
        )
    ledger = factor_ledger(factors)
    residual = {
        label: (counts["UP"], counts["DOWN"])
        for label, counts in ledger.items()
        if counts["UP"] != counts["DOWN"]
    }
    expected = dict(expected_free)
    checks = {
        "all_V_ports_consumed_once": Counter(compiler.used_ports)
        == Counter(ast_v_slots(expression)),
        "all_declared_ports_are_AST_ports": set(port_colors) == set(ast_v_slots(expression)),
        "one_c_tensor_per_AST_bracket": sum(factor.kind == "C" for factor in factors)
        == ast_bracket_count(expression),
        "only_expected_free_indices_survive": residual == expected,
    }
    payload = {
        "factors": [factor.as_json() for factor in factors],
        "rendered": " * ".join(factor.render() for factor in factors) or "1",
        "index_ledger": ledger,
        "free_index_residual": {
            key: {"UP": value[0], "DOWN": value[1]}
            for key, value in sorted(residual.items())
        },
        "checks": checks,
    }
    payload["sha256"] = sha256_json(payload)
    return payload


def combined_color_tensor_record(
    expressions: Sequence[Mapping[str, object]],
    port_colors: Mapping[str, str],
    edge_pairs: Sequence[tuple[str, str]],
    *,
    prefixes: Sequence[str],
    expected_free: Mapping[str, tuple[int, int]],
) -> dict[str, object]:
    """Compile a product of scalar/source-valued ASTs without inventing a pairing."""

    if len(expressions) != len(prefixes):
        raise ValueError("one internal-dummy prefix is required for each AST")
    compilers: list[ColorASTCompiler] = []
    factors: list[ColorFactor] = []
    for expression, prefix in zip(expressions, prefixes, strict=True):
        compiler = ColorASTCompiler(port_colors, prefix)
        compiler.compile(expression)
        compilers.append(compiler)
        factors.extend(compiler.factors)
    for left_port, right_port in edge_pairs:
        factors.append(
            ColorFactor(
                "KAPPA_UPPER",
                ((port_colors[left_port], "UP"), (port_colors[right_port], "UP")),
            )
        )
    ledger = factor_ledger(factors)
    residual = {
        label: (counts["UP"], counts["DOWN"])
        for label, counts in ledger.items()
        if counts["UP"] != counts["DOWN"]
    }
    ast_slots = tuple(
        slot for expression in expressions for slot in ast_v_slots(expression)
    )
    ast_brackets = sum(ast_bracket_count(expression) for expression in expressions)
    used_ports = [slot for compiler in compilers for slot in compiler.used_ports]
    checks = {
        "all_V_ports_consumed_once": Counter(used_ports) == Counter(ast_slots),
        "all_declared_ports_are_AST_ports": set(port_colors) == set(ast_slots),
        "one_c_tensor_per_AST_bracket": sum(
            factor.kind == "C" for factor in factors
        )
        == ast_brackets,
        "only_expected_free_indices_survive": residual == dict(expected_free),
    }
    payload = {
        "factors": [factor.as_json() for factor in factors],
        "rendered": " * ".join(factor.render() for factor in factors) or "1",
        "index_ledger": ledger,
        "free_index_residual": {
            key: {"UP": value[0], "DOWN": value[1]}
            for key, value in sorted(residual.items())
        },
        "checks": checks,
    }
    payload["sha256"] = sha256_json(payload)
    return payload


def without_kappa_placeholder(value: Mapping[str, object]) -> ExactMonomial:
    symbols = value["symbols"]
    if not isinstance(symbols, list):
        raise TypeError("coefficient symbols must be a list")
    return ExactMonomial(
        Fraction(str(value["rational"])),
        int(value["i_power"]),
        tuple(str(symbol) for symbol in symbols if symbol != "kappa^-1"),
    )


def reduce_h_g2(value: ExactMonomial) -> ExactMonomial:
    symbols = list(value.symbols)
    while "h" in symbols and "g^2" in symbols:
        symbols.remove("h")
        symbols.remove("g^2")
    return ExactMonomial(value.rational, value.i_power, tuple(symbols))


def histogram(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def source_factor(port_id: str) -> str:
    if ".L." in port_id:
        return "LEFT_SOURCE_FACTOR_A"
    if ".R." in port_id:
        return "RIGHT_SOURCE_FACTOR_B"
    if ".outer." in port_id:
        return "OUTER_CONNECTION_PORT"
    return "UNRESOLVED_SOURCE_FACTOR"


def orientation_from_factor(factor: str) -> str:
    if factor == "RIGHT_SOURCE_FACTOR_B":
        return "DIRECT"
    if factor == "LEFT_SOURCE_FACTOR_A":
        return "REFLECTED"
    return "PENDING_D_ALGEBRA"


def local_projection_record(
    term: Mapping[str, object],
    port: Mapping[str, object],
    expected_word: Sequence[str],
    target: str,
) -> dict[str, object]:
    scopes = derivative_scope_index(term["expression"])
    port_id = str(port["port_id"])
    scope = scopes[port_id]
    exact_word = list(expected_word) == scope["word_outer_to_inner"]
    singleton = bool(scope["singleton_scope"])
    exact_local = exact_word and singleton
    return {
        "port_id": port_id,
        "target": target,
        "expected_word": list(expected_word),
        **scope,
        "exact_word": exact_word,
        "exact_local_projection": exact_local,
        "status": (
            "EXACT_SINGLETON_PROJECTOR_SCOPE"
            if exact_local
            else "FAIL_CLOSED_REQUIRES_SHARED_SCOPE_D_ALGEBRA"
        ),
    }


def build_color_records(contact: Mapping[str, object]) -> dict[str, object]:
    source_terms = contact["source_terms"]
    if not isinstance(source_terms, dict):
        raise TypeError("contact source terms must be a dictionary")
    bubble_records: list[dict[str, object]] = []
    for graph in contact["I3_x_S3_graphs"]:
        i_ports = graph["port_provenance"]["I3"]
        s_ports = graph["port_provenance"]["S3"]
        i_background = [row for row in i_ports if row["role"] == "BACKGROUND_EXTERNAL"]
        s_background = [row for row in s_ports if row["role"] == "BACKGROUND_EXTERNAL"]
        i_quantum = [row for row in i_ports if row["role"] == "QUANTUM_WICK"]
        s_quantum = [row for row in s_ports if row["role"] == "QUANTUM_WICK"]
        if tuple(map(len, (i_background, s_background, i_quantum, s_quantum))) != (1, 1, 2, 2):
            raise ValueError("bubble port typing changed")
        port_colors = {
            str(i_background[0]["port_id"]): "E",
            str(s_background[0]["port_id"]): "D",
            **{str(row["port_id"]): f"Iq{index}" for index, row in enumerate(i_quantum)},
            **{str(row["port_id"]): f"Sq{index}" for index, row in enumerate(s_quantum)},
        }
        i_term = source_terms[graph["source_term_bindings"]["I3"]["term_id"]]
        s_term = source_terms[graph["source_term_bindings"]["S3"]["term_id"]]
        edge_pairs = [
            (str(pair["I3_port"]), str(pair["S3_port"]))
            for pair in graph["pairing"]["pairs"]
        ]
        tensor = combined_color_tensor_record(
            (i_term["expression"], s_term["expression"]),
            port_colors,
            edge_pairs,
            prefixes=("bi", "bs"),
            expected_free={"A": (1, 0), "B": (1, 0), "D": (0, 1), "E": (0, 1)},
        )
        bubble_records.append(
            {
                "labeled_graph_id": graph["labeled_graph_id"],
                "tensor_sha256": tensor["sha256"],
                "tensor": tensor,
            }
        )

    tadpole_records: list[dict[str, object]] = []
    for graph in contact["I4_tadpole_graphs"]:
        ports = graph["port_provenance"]
        backgrounds = [row for row in ports if row["role"] == "BACKGROUND_EXTERNAL"]
        quantum = [row for row in ports if row["role"] == "QUANTUM_WICK"]
        port_colors = {
            **{str(row["port_id"]): f"P{index}" for index, row in enumerate(backgrounds)},
            **{str(row["port_id"]): f"Iq{index}" for index, row in enumerate(quantum)},
        }
        term = source_terms[graph["source_term_binding"]["term_id"]]
        tensor = color_tensor_record(
            term["expression"],
            port_colors,
            [(str(quantum[0]["port_id"]), str(quantum[1]["port_id"]))],
            prefix="t",
            expected_free={"A": (1, 0), "B": (1, 0), "P0": (0, 1), "P1": (0, 1)},
        )
        tadpole_records.append(
            {
                "labeled_graph_id": graph["labeled_graph_id"],
                "tensor_sha256": tensor["sha256"],
                "tensor": tensor,
            }
        )
    return {
        "status": "INDEX_INCIDENCE_ONLY_PHYSICAL_COLOR_REDUCTION_OPEN",
        "scope_boundary": (
            "the compiler checks port/index incidence in the retained I3S3 and I4 rows; "
            "it does not reduce the coefficient-weighted color sum modulo antisymmetry, "
            "Jacobi, or kappa invariance, and it omits I0H2, cut children, and CT2"
        ),
        "physical_color_reduction": "FAIL_CLOSED_NOT_COMPUTED",
        "coefficient_type_repair": (
            "kappa^-1 is removed from the scalar monomial and emitted only as "
            "typed KAPPA_UPPER edge factors"
        ),
        "bubble_tensors": bubble_records,
        "tadpole_tensors": tadpole_records,
        "counts": {
            "bubble": len(bubble_records),
            "tadpole": len(tadpole_records),
            "total": len(bubble_records) + len(tadpole_records),
            "unique_tensor_hashes": len(
                {row["tensor_sha256"] for row in bubble_records + tadpole_records}
            ),
        },
    }


def build_projection_and_coefficients(contact: Mapping[str, object]) -> dict[str, object]:
    source_terms = contact["source_terms"]
    records: list[dict[str, object]] = []
    action_factor = ExactMonomial(Fraction(-1))
    extraction = ExactMonomial(Fraction(64))
    for graph in contact["I3_x_S3_graphs"]:
        i_term = source_terms[graph["source_term_bindings"]["I3"]["term_id"]]
        s_term = source_terms[graph["source_term_bindings"]["S3"]["term_id"]]
        i_background = next(
            row for row in graph["port_provenance"]["I3"] if row["role"] == "BACKGROUND_EXTERNAL"
        )
        s_background = next(
            row for row in graph["port_provenance"]["S3"] if row["role"] == "BACKGROUND_EXTERNAL"
        )
        i_projection = local_projection_record(
            i_term, i_background, ("D_+", "barD^2", "D_+"), "X"
        )
        s_projection = local_projection_record(
            s_term, s_background, ("D^2", "barD_dot_a"), "TILDE_W"
        )
        s_variance = (
            "UP"
            if s_projection["exact_local_projection"]
            and int(s_projection["spinor_raise_depth"]) % 2
            else "DOWN"
            if s_projection["exact_local_projection"]
            else "PENDING"
        )
        stripped = without_kappa_placeholder(
            graph["coefficient_provenance"]["known_product_excluding_open_factors"]
        )
        stripped_reduced = reduce_h_g2(stripped)
        wick_signed = stripped * action_factor
        wick_signed_reduced = reduce_h_g2(wick_signed)
        both_local = bool(
            i_projection["exact_local_projection"]
            and s_projection["exact_local_projection"]
        )
        local_coefficient = (
            reduce_h_g2(wick_signed * extraction) if both_local else None
        )
        factor = source_factor(str(i_background["port_id"]))
        records.append(
            {
                "labeled_graph_id": graph["labeled_graph_id"],
                "I3_term": i_term["term_id"],
                "S3_term": s_term["term_id"],
                "D_minus_or_connection_tags": [
                    tag
                    for tag in i_term["tags"]
                    if tag.startswith("D_MINUS_") or "CONNECTION" in tag
                ],
                "source_factor": factor,
                "orientation_candidate": orientation_from_factor(factor),
                "I3_X_projection": i_projection,
                "S3_TildeW_projection": s_projection,
                "TildeW_dotted_variance": s_variance,
                "both_external_projectors_local": both_local,
                "scalar_coefficient": {
                    "stripped_known_product": stripped.as_json(),
                    "stripped_after_hg2_reduction": stripped_reduced.as_json(),
                    "wick_representation_after_action_sign": wick_signed_reduced.as_json(),
                    "coefficient_usage": (
                        "WICK_REPRESENTATION_ONLY_DO_NOT_MULTIPLY_BY_HESSIAN_NEUMANN_SIGN"
                    ),
                    "automorphism_division": "NONE",
                    "color_metric_factors": "SEPARATE_TYPED_TENSOR",
                },
                "local_projector_extraction": (
                    {
                        "X": "D_+ barD^2 D_+ V=-8 X",
                        "TildeW": "D^2 barD_dot_a V=-8 TildeW_dot_a",
                        "product": "(-8)(-8)=64",
                        "scalar_after_extraction": local_coefficient.as_json(),
                    }
                    if local_coefficient is not None
                    else "NOT_APPLIED_TO_SHARED_SCOPE"
                ),
            }
        )
    counts = {
        "total_bubbles": len(records),
        "I3_exact_local_X": sum(row["I3_X_projection"]["exact_local_projection"] for row in records),
        "S3_exact_local_TildeW": sum(
            row["S3_TildeW_projection"]["exact_local_projection"] for row in records
        ),
        "both_exact_local": sum(row["both_external_projectors_local"] for row in records),
        "both_exact_local_TildeW_DOWN": sum(
            row["both_external_projectors_local"]
            and row["TildeW_dotted_variance"] == "DOWN"
            for row in records
        ),
        "both_exact_local_TildeW_UP": sum(
            row["both_external_projectors_local"]
            and row["TildeW_dotted_variance"] == "UP"
            for row in records
        ),
        "requires_shared_scope_D_algebra": sum(
            not row["both_external_projectors_local"] for row in records
        ),
    }
    return {
        "euclidean_action_expansion": {
            "identity": "exp[-S_int/hbar]=1-S3/hbar+O(S_int^2)",
            "single_S3_stripped_vertex_factor": "-1",
            "factorial": "1/1!=1",
            "representation": "WICK_EXPANSION_ONLY",
            "status": "EXACT_WICK_SIGN_HESSIAN_TRANSPORT_OPEN",
        },
        "single_sign_transport_obligation": {
            "identity": "C_Wick(I1,S3)=C_Hess(I1,H1)",
            "required_checks": [
                "supertrace_prefactor_1_over_2",
                "two_labeled_Wick_pairings",
                "H1_equals_second_functional_derivative_of_S3",
                "all_Koszul_signs",
            ],
            "rule": (
                "use the Wick action sign or the Hessian Neumann sign according to the "
                "chosen representation; never multiply the two"
            ),
            "status": "FAIL_CLOSED_NOT_DERIVED",
        },
        "projector_definitions": {
            "X_1": "-(1/8) D_+ barD^2 D_+ V",
            "TildeW_1_down": "-(1/8) D^2 barD_down V",
        },
        "records": records,
        "counts": counts,
        "wick_scalar_histogram_after_hg2": histogram(
            row["scalar_coefficient"]["wick_representation_after_action_sign"]["rendered"]
            for row in records
        ),
        "local_scalar_histogram_after_extraction": histogram(
            row["local_projector_extraction"]["scalar_after_extraction"]["rendered"]
            for row in records
            if isinstance(row["local_projector_extraction"], dict)
        ),
    }


def build_tadpole_certificate(contact: Mapping[str, object]) -> dict[str, object]:
    source_terms = contact["source_terms"]
    records: list[dict[str, object]] = []
    for graph in contact["I4_tadpole_graphs"]:
        term = source_terms[graph["source_term_binding"]["term_id"]]
        operators = ast_operators(term["expression"])
        ast_operator_whitelist = set(operators) <= SUPPORTED_COLOR_OPERATORS
        routing = graph["routing_classification"]
        no_scale = (
            routing["denominator"] == "k^2"
            and routing["external_momentum_in_denominator"] is False
        )
        raw = without_kappa_placeholder(
            graph["coefficient_provenance"]["known_product_excluding_open_factors"]
        )
        records.append(
            {
                "labeled_graph_id": graph["labeled_graph_id"],
                "source_term": term["term_id"],
                "raw_composite_has_NormalOrder_node": "NormalOrder" in operators,
                "two_quantum_ports_have_one_labeled_pairing": len(graph["pairing"]["pair"]) == 2,
                "AST_operator_whitelist_only": ast_operator_whitelist,
                "denominator_has_no_external_scale": no_scale,
                "missing_edge_tagged_locality_to_polynomial_proof": True,
                "conditional_DRED_scaleless_rule": (
                    "if edge-tagged D-algebra proves numerator P(k,p,q) polynomial and "
                    "no additional loop denominator, then Integral_k P(k,p,q)/k^2=0"
                ),
                "DRED_value": "CONDITIONAL_ZERO_PROOF_OBLIGATION_OPEN",
                "scalar_coefficient_before_zero": reduce_h_g2(raw).as_json(),
                "external_projection": "PENDING",
                "typed_automorphism_order_literal": 1,
                "automorphism_division": "NONE",
            }
        )
    return {
        "normal_order_policy": {
            "bare_insertion": "RAW_PROJECT_COMPOSITE_NOT_WICK_NORMAL_ORDERED",
            "self_contractions": "ADMITTED",
            "subtraction": "NONE_BEFORE_COMPOSITE_RENORMALIZATION",
            "reason": (
                "the Project AST contains no NormalOrder node, but absence of that node "
                "does not fix the bare-composite renormalization prescription"
            ),
            "status": "FAIL_CLOSED_BARE_COMPOSITE_RENORMALIZATION_PRESCRIPTION_OPEN",
        },
        "records": records,
        "counts": {
            "admitted_self_contractions": len(records),
            "conditional_DRED_zero": sum(
                row["DRED_value"] == "CONDITIONAL_ZERO_PROOF_OBLIGATION_OPEN"
                for row in records
            ),
            "certified_DRED_zero": 0,
            "projection_pending": sum(
                row["external_projection"].startswith("PENDING") for row in records
            ),
        },
        "scalar_histogram_before_zero": histogram(
            row["scalar_coefficient_before_zero"]["rendered"] for row in records
        ),
        "evanescent_tensor_statement": (
            "conditional only: the full tensor integral would vanish before delta4, "
            "tilde_delta, or tau decomposition after the missing edge-tagged "
            "locality-to-polynomial proof"
        ),
        "status": "FAIL_CLOSED_LOCALITY_TO_POLYNOMIAL_PROOF_OPEN",
    }


def build_i0_h2_certificate() -> dict[str, object]:
    terms = gauge_s4_terms()
    rows: list[dict[str, object]] = []
    for term in terms:
        attrs = dict(term.expression.attrs)
        rows.append(
            {
                "term_id": term.term_id,
                "family": term.family,
                "measure": attrs["measure"],
                "tags": list(term.tags),
                "field_strength_sector": (
                    "W_W" if "CHIRAL_EUCLIDEAN_SECTOR" in term.tags else "TILDEW_TILDEW"
                ),
            }
        )
    selected = seed_port_assignment_payload()["selected_for_seed"]["S4_mixed_X_TildeW"]
    graph = seagull_graph()
    return {
        "quadratic_family_word": "-I0 G0 H2[p1,p2] G0",
        "target_pair": ["X=nabla_+W_+", "TildeW_dot_a"],
        "quartic_action_terms": rows,
        "chiral_count": sum(row["field_strength_sector"] == "W_W" for row in rows),
        "antichiral_count": sum(
            row["field_strength_sector"] == "TILDEW_TILDEW" for row in rows
        ),
        "mixed_count": 0,
        "old_intrinsic_sector_selection": selected,
        "old_intrinsic_sector_selection_not_used_as_Hessian_zero": True,
        "reason": (
            "the H2 background Hessian acts on prepotential ports; intrinsic "
            "W/W or TildeW/TildeW chirality alone does not prove that the "
            "post-D-algebra X/TildeW projector vanishes"
        ),
        "physical_GraphIR": graph.canonical_dict(),
        "branch_path_literal": 576,
        "branch_path_literal_status": "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
        "target_projector": "FAIL_CLOSED_NOT_DERIVED",
        "local_UV_pole": "NOT_COMPUTED",
        "status": "FAIL_CLOSED_H2_PROJECTOR_DALGEBRA_NORMALIZATION_OPEN",
    }


def build_complete_contact_family(
    contact: Mapping[str, object],
    projection: Mapping[str, object],
    i0_h2: Mapping[str, object],
    collapsed: Mapping[str, object],
) -> dict[str, object]:
    direct = insertion_contact_graph("p1", "p2")
    reflected = insertion_contact_graph("p2", "p1")
    i2 = double_contact_graph()
    ct2 = counterterm_graph()
    orientation_counts = Counter(
        row["orientation_candidate"] for row in projection["records"]
    )
    source_factor_counts = Counter(row["source_factor"] for row in projection["records"])
    hessian_terms = {
        "minus_I0_G0_H2_G0": {
            "hessian_neumann_sign": -1,
            "sign_usage": "HESSIAN_REPRESENTATION_ONLY",
            "supertrace_prefactor": "1/2",
            "GraphIR": i0_h2["physical_GraphIR"],
            "branch_path_literal": 576,
            "branch_path_literal_status": "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
            "target_projector": i0_h2["target_projector"],
            "local_UV_pole": i0_h2["local_UV_pole"],
        },
        "minus_I1_p1_G0_H1_p2_G0": {
            "hessian_neumann_sign": -1,
            "sign_usage": "HESSIAN_REPRESENTATION_ONLY",
            "supertrace_prefactor": "1/2",
            "GraphIR": direct.canonical_dict(),
            "branch_path_literal": 1440,
            "branch_path_literal_status": "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
            "selected_composite_Wick_rows": orientation_counts["DIRECT"],
            "source_factor": "RIGHT_SOURCE_FACTOR_B",
            "target_projector": "PARTIAL_LOCAL_16_ROWS_REMAINDER_SHARED_SCOPE",
            "local_UV_pole": "NOT_COMPUTED",
        },
        "minus_I1_p2_G0_H1_p1_G0": {
            "hessian_neumann_sign": -1,
            "sign_usage": "HESSIAN_REPRESENTATION_ONLY",
            "supertrace_prefactor": "1/2",
            "GraphIR": reflected.canonical_dict(),
            "branch_path_literal": 1440,
            "branch_path_literal_status": "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
            "selected_composite_Wick_rows": orientation_counts["REFLECTED"],
            "source_factor": "LEFT_SOURCE_FACTOR_A",
            "target_projector": "PARTIAL_LOCAL_16_ROWS_REMAINDER_SHARED_SCOPE",
            "local_UV_pole": "NOT_COMPUTED",
        },
        "plus_I2_G0": {
            "hessian_neumann_sign": 1,
            "sign_usage": "HESSIAN_REPRESENTATION_ONLY",
            "supertrace_prefactor": "1/2",
            "GraphIR": i2.canonical_dict(),
            "branch_path_literal": 720,
            "branch_path_literal_status": "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT",
            "base_BQ_assignments": len(contact["I4_tadpole_graphs"]),
            "literal_relation": "720=180*(2 background labels)*(2 Hessian port orders)",
            "literal_relation_status": "ARITHMETIC_ONLY_NOT_A_BRANCH_GENERATION_PROOF",
            "target_projector": "FAIL_CLOSED_NOT_DERIVED",
            "DRED_scaleless_value": "CONDITIONAL_ZERO_LOCALITY_TO_POLYNOMIAL_OPEN",
            "ordinary_UV_pole": "NOT_SEPARATED_FROM_SCALELESS_UV_IR_PAIR",
        },
    }
    ct2_record = {
        "GraphIR": ct2.canonical_dict(),
        "renormalization_condition": "NOT_FIXED",
        "operator_mixing_basis": "NOT_FIXED",
        "coefficient": "OPEN",
        "local_term": "NOT_COMPUTED",
    }
    return {
        "Q_Hess": {
            "definition": (
                "-(1/2)STr[I0 G0 H2[p1,p2] G0]"
                "-(1/2)STr[I1[p1] G0 H1[p2] G0]"
                "-(1/2)STr[I1[p2] G0 H1[p1] G0]"
                "+(1/2)STr[I2[p1,p2] G0]"
            ),
            "terms": hessian_terms,
            "status": "FAIL_CLOSED_PROJECTORS_NORMALIZATIONS_AND_POLES_OPEN",
        },
        "Q_cut": collapsed,
        "CT2": ct2_record,
        "Q_phys": {
            "definition": "Q_phys^(2)=Q_Hess^(2)+Q_cut^(2)+CT2",
            "role": "REGROUPED_CONTACT_CUT_FAMILY_NOT_ADDED_TO_BARE_TRIANGLE",
            "cut_map": "Q_cut^(2)=R_cut Q_triangle^bare",
            "irreducible_triangle": "Q_triangle^irr=(1-R_cut)Q_triangle^bare",
            "full_quadratic_identity": "Gamma_2=Q_triangle^irr+Q_phys^(2)",
            "R_cut_status": "NOT_CONSTRUCTED_COEFFICIENT_TRANSPORT_OPEN",
            "cut_binding_count": collapsed["counts"]["trace_edge_bindings"],
            "unique_cut_child_GraphIR": collapsed["counts"]["unique_child_GraphIR"],
            "cut_coefficients": "OPEN",
            "CT2_coefficient": "OPEN",
            "local_UV_pole": "FAIL_CLOSED_NOT_COMPUTED",
            "status": "FAIL_CLOSED_COMPLETE_PHYSICAL_CONTACT_CUT_FAMILY",
        },
        "single_sign_transport": projection["single_sign_transport_obligation"],
        "selected_I3_S3_census": {
            "labeled_Wick_rows": len(contact["I3_x_S3_graphs"]),
            "orientation_candidates": dict(sorted(orientation_counts.items())),
            "source_factors": dict(sorted(source_factor_counts.items())),
            "exact_local_rows": projection["counts"]["both_exact_local"],
            "shared_scope_rows": projection["counts"][
                "requires_shared_scope_D_algebra"
            ],
        },
        "normalization_gates": {
            "H2_projector_and_D_algebra": "OPEN",
            "I1H1_shared_scope_D_algebra": "OPEN",
            "I2_functional_Hessian_normalization": "OPEN",
            "I2_edge_tagged_locality_to_polynomial": "OPEN",
            "cut_child_coefficient_transport": "OPEN",
            "CT2_renormalization_condition_and_mixing": "OPEN",
        },
        "post_projector_local_pole": "FAIL_CLOSED_NOT_COMPUTED",
        "status": "FAIL_CLOSED_COMPLETE_CONTACT_LOCAL_POLE_NOT_DERIVED",
    }


def build_collapsed_certificate() -> dict[str, object]:
    records: list[dict[str, object]] = []
    for orientation in ("DIRECT", "REFLECTED"):
        parent = physical_triangle(orientation)
        for trace in endpoint_rows(orientation):
            for edge_id in ("e0", "e1", "e2"):
                child = parent.collapse_edge(edge_id)
                graph = child.canonical_dict()
                records.append(
                    {
                        "binding_id": f"{trace['trace_id']}__collapse__{edge_id}",
                        "parent_graph_id": parent.graph_id,
                        "parent_trace_id": trace["trace_id"],
                        "orientation": orientation,
                        "orientation_sign": trace["total_orientation_sign"],
                        "D_minus_placement": trace["D_minus_placement"],
                        "barD_endpoint": trace["barD_endpoint"],
                        "D_endpoint": trace["D_endpoint"],
                        "collapsed_edge": edge_id,
                        "child_graph_id": child.graph_id,
                        "child_graph_sha256": sha256_json(graph),
                        "child_GraphIR": graph,
                        "remaining_edges": [
                            {"edge_id": edge["edge_id"], "momentum": edge["momentum"]}
                            for edge in graph["internal_edges"]
                        ],
                        "typed_port_GraphIR_audit_order": graph_automorphism_order(child),
                        "coefficient": "OPEN",
                        "coefficient_transport": (
                            "OPEN_REQUIRES_EDGE_COLLAPSE_D_ALGEBRA_AND_SINGLE_SIGN_TRANSPORT"
                        ),
                    }
                )
    unique_children = {
        row["child_graph_sha256"]: row["child_GraphIR"] for row in records
    }
    return {
        "records": records,
        "unique_children": [
            {"child_graph_sha256": digest, "GraphIR": unique_children[digest]}
            for digest in sorted(unique_children)
        ],
        "counts": {
            "trace_edge_bindings": len(records),
            "unique_child_GraphIR": len({row["child_graph_sha256"] for row in records}),
            "per_orientation": dict(Counter(row["orientation"] for row in records)),
            "per_collapsed_edge": dict(Counter(row["collapsed_edge"] for row in records)),
        },
        "status": "STRUCTURAL_48_BINDINGS_6_UNIQUE_CHILDREN_COEFFICIENTS_OPEN",
    }


def build_automorphism_certificate(contact: Mapping[str, object], collapsed: Mapping[str, object]) -> dict[str, object]:
    contact_rows = contact["I3_x_S3_graphs"] + contact["I4_tadpole_graphs"]
    return {
        "definition": "Aut_N preserves all notation-schema port decorations",
        "assigned_ordering_assumption": (
            "ordered port positions are treated as fixed labels in this replay; no physical "
            "stabilizer quotient or Taylor/Wick factorial matching is derived"
        ),
        "contact_record_count": len(contact_rows),
        "contact_typed_automorphism_order_literal": 1,
        "collapsed_typed_port_GraphIR_audit_orders": sorted(
            {row["typed_port_GraphIR_audit_order"] for row in collapsed["records"]}
        ),
        "physical_stabilizers": "FAIL_CLOSED_NOT_COMPUTED",
        "Taylor_Wick_factorial_matching": "FAIL_CLOSED_NOT_COMPUTED",
        "automorphism_division_applied": False,
        "status": "ASSIGNED_ORDER_ONE_AUDIT_ONLY_PHYSICAL_STABILIZER_OPEN",
    }


def obligation_ledger() -> list[dict[str, object]]:
    return [
        {
            "id": "OPEN_CONTACT_001",
            "status": "PARTIAL_32_LOCAL_328_SHARED_SCOPE_FAIL_CLOSED",
            "gap_type": "G-OP",
            "severity": "P1",
            "missing": "edge-tagged shared-scope Leibniz, pivoted IBP, and two-edge delta saturation",
        },
        {
            "id": "OPEN_CONTACT_002",
            "status": "PARTIAL_540_ROW_INDEX_INCIDENCE_PHYSICAL_COLOR_REDUCTION_OPEN",
            "gap_type": "G-IDX",
            "severity": "P1",
            "missing": (
                "coefficient-weighted Lie-identity reduction including I0H2, "
                "cut children, and CT2, plus kappa-token multiplicity"
            ),
        },
        {
            "id": "OPEN_CONTACT_003",
            "status": "FAIL_CLOSED_SINGLE_SIGN_WICK_TO_HESSIAN_TRANSPORT_OPEN",
            "gap_type": "G-SIGN",
            "severity": "P1",
            "missing": (
                "prove C_Wick(I1,S3)=C_Hess(I1,H1), including the supertrace "
                "factor, two labeled pairings, functional derivatives, and Koszul signs"
            ),
        },
        {
            "id": "OPEN_CONTACT_004",
            "status": "FAIL_CLOSED_I4_PROJECTOR_AND_LOCALITY_TO_POLYNOMIAL_OPEN",
            "gap_type": "G-PROJ",
            "severity": "P1",
            "missing": (
                "ordered X/TildeW projection and functional-Hessian "
                "normalization of both I4 background ports; edge-tagged proof that "
                "the numerator is polynomial with no additional loop denominator"
            ),
        },
        {
            "id": "OPEN_CONTACT_005",
            "status": "FAIL_CLOSED_BARE_COMPOSITE_RENORMALIZATION_PRESCRIPTION_OPEN",
            "gap_type": "G-DEF",
            "severity": "P2",
            "missing": (
                "state the Project bare-composite renormalization prescription; absence "
                "of an AST NormalOrder node does not fix Wick normal ordering"
            ),
        },
        {
            "id": "OPEN_CONTACT_006",
            "status": "FAIL_CLOSED_I4_CONDITIONAL_ZERO_I3S3_FIBER_AMPLITUDES_OPEN",
            "gap_type": "G-ALG",
            "severity": "P1",
            "missing": "OPEN_CONTACT_001 normal forms before fiber coefficient summation",
        },
        {
            "id": "OPEN_CONTACT_007",
            "status": "PARTIAL_48_COLLAPSE_BINDINGS_6_CHILDREN_COEFFICIENTS_OPEN",
            "gap_type": "G-PROJ",
            "severity": "P1",
            "missing": (
                "derive all 48 edge-collapse coefficients and map 360 bubble normal "
                "forms to the sixteen orientation/trace channels"
            ),
        },
        {
            "id": "OPEN_CONTACT_008",
            "status": "FAIL_CLOSED_PHYSICAL_STABILIZERS_AND_FACTORIAL_MATCHING_OPEN",
            "gap_type": "G-NORM",
            "severity": "P1",
            "missing": (
                "derive each contact stabilizer and match it to the Taylor and Wick "
                "factorials; the current order-one value is an audit literal"
            ),
        },
        {
            "id": "OPEN_QCONTACT_009",
            "status": "FAIL_CLOSED_H2_PROJECTOR_DALGEBRA_NORMALIZATION_OPEN",
            "gap_type": "G-ALG",
            "severity": "P1",
            "missing": (
                "generate rather than assume the 576 branch-path literal, compile the "
                "I0-H2 family to the X/TildeW target, and "
                "derive their routed local pole"
            ),
        },
        {
            "id": "OPEN_QCONTACT_010",
            "status": "FAIL_CLOSED_CT2_RENORMALIZATION_AND_MIXING_OPEN",
            "gap_type": "G-NORM",
            "severity": "P1",
            "missing": (
                "fix the local operator-mixing basis and renormalization "
                "condition before assigning the CT2 coefficient"
            ),
        },
    ]


def build_payload() -> dict[str, object]:
    contact = build_contact_payload()
    color = build_color_records(contact)
    projection = build_projection_and_coefficients(contact)
    tadpoles = build_tadpole_certificate(contact)
    i0_h2 = build_i0_h2_certificate()
    collapsed = build_collapsed_certificate()
    complete_contact = build_complete_contact_family(
        contact,
        projection,
        i0_h2,
        collapsed,
    )
    automorphisms = build_automorphism_certificate(contact, collapsed)
    obligations = obligation_ledger()
    return {
        "schema": "Step5WWContactReplay.v2",
        "scope": "FIXED_VECTOR_FRAME_PURE_GAUGE_WW_QUADRATIC_CONTACT_CUT_FAMILY",
        "authority_status": "UNMERGED_PROPOSAL_NOT_COMPUTATIONAL_EVIDENCE",
        "complete_quadratic_family": {
            "functional_identity": (
                "+G0 I0 G0 H1 G0 H1-G0 I0 G0 H2-G0 I1 G0 H1+G0 I2+CT2"
            ),
            "I0_H1_H1": {
                "triangles": 2,
                "edge_tagged_rows": 16,
                "collapsed_trace_edge_bindings": collapsed["counts"]["trace_edge_bindings"],
            },
            "I0_H2": i0_h2,
            "I1_H1": {
                "polarizations": 2,
                "labeled_Wick_contributions": len(contact["I3_x_S3_graphs"]),
                "direct": 168,
                "reflected": 168,
                "outer_connection_pending": 24,
            },
            "I2": {
                "raw_self_contractions": len(contact["I4_tadpole_graphs"]),
                "DRED_value": "CONDITIONAL_ZERO_LOCALITY_TO_POLYNOMIAL_OPEN",
            },
            "CT2": "BLOCKED_RENORMALIZATION_CONDITION_NOT_FIXED_BY_CONTACT_REPLAY",
        },
        "complete_Q_contact": complete_contact,
        "color_AST": color,
        "bubble_projection_and_coefficient": projection,
        "I4_tadpoles": tadpoles,
        "collapsed_triangle_children": collapsed,
        "typed_automorphisms": automorphisms,
        "DRED_tensor_basis": {
            "delta4": "delta_(4)^(mn)",
            "tilde_delta": "tilde_delta^(mn)",
            "tau": "tilde_delta^(mn)-(epsilon/2)delta_(4)^(mn)",
            "trace_tau": "0",
            "policy": "OPEN_TAU_CHANNEL_IS_NEVER_REPLACED_BY_2epsilon",
        },
        "proof_obligations": obligations,
        "open_proof_obligation_ids": [
            row["id"] for row in obligations if row["severity"] != "CLOSED"
        ],
        "pole_boundary": {
            "isolated_triangle_pole_recomputed_here": False,
            "complete_contact_ordinary_UV_pole": (
                "NOT_COMPUTED_H2_I1H1_PROJECTORS_AND_CT2_OPEN"
            ),
            "evanescent_tau_pole": "NOT_COMPUTED",
            "anomaly_coefficient": "NOT_ACCEPTED",
            "invalidated_coefficient_reused": False,
        },
        "external_results_imported": False,
    }


def scope_invariants(payload: Mapping[str, object]) -> dict[str, bool]:
    color = payload["color_AST"]
    projection = payload["bubble_projection_and_coefficient"]
    tadpoles = payload["I4_tadpoles"]
    collapsed = payload["collapsed_triangle_children"]
    quadratic = payload["complete_quadratic_family"]
    complete_contact = payload["complete_Q_contact"]
    obligations = payload["proof_obligations"]
    color_rows = color["bubble_tensors"] + color["tadpole_tensors"]
    hessian_terms = complete_contact["Q_Hess"]["terms"]
    branch_terms = tuple(hessian_terms.values())
    bubble_color_ids = sorted(row["labeled_graph_id"] for row in color["bubble_tensors"])
    bubble_scalar_ids = sorted(row["labeled_graph_id"] for row in projection["records"])
    tadpole_color_ids = sorted(row["labeled_graph_id"] for row in color["tadpole_tensors"])
    tadpole_scalar_ids = sorted(row["labeled_graph_id"] for row in tadpoles["records"])
    return {
        "schema_complete_quadratic_words_present": set(quadratic)
        == {"functional_identity", "I0_H1_H1", "I0_H2", "I1_H1", "I2", "CT2"},
        "schema_QHess_has_four_terms": set(hessian_terms)
        == {
            "minus_I0_G0_H2_G0",
            "minus_I1_p1_G0_H1_p2_G0",
            "minus_I1_p2_G0_H1_p1_G0",
            "plus_I2_G0",
        },
        "schema_Qphys_is_Hess_cut_CT2": complete_contact["Q_phys"]["definition"]
        == "Q_phys^(2)=Q_Hess^(2)+Q_cut^(2)+CT2",
        "Qphys_is_regrouping_not_double_counted_with_bare_triangle": complete_contact[
            "Q_phys"
        ]["role"]
        == "REGROUPED_CONTACT_CUT_FAMILY_NOT_ADDED_TO_BARE_TRIANGLE"
        and complete_contact["Q_phys"]["full_quadratic_identity"]
        == "Gamma_2=Q_triangle^irr+Q_phys^(2)"
        and complete_contact["Q_phys"]["R_cut_status"]
        == "NOT_CONSTRUCTED_COEFFICIENT_TRANSPORT_OPEN",
        "branch_numbers_are_tagged_input_literals_not_graph_counts": [
            hessian_terms[key]["branch_path_literal"]
            for key in (
                "minus_I0_G0_H2_G0",
                "minus_I1_p1_G0_H1_p2_G0",
                "minus_I1_p2_G0_H1_p1_G0",
                "plus_I2_G0",
            )
        ]
        == [576, 1440, 1440, 720]
        and all(
            row["branch_path_literal_status"]
            == "INPUT_LITERAL_NOT_GENERATED_NOT_A_GRAPH_COUNT"
            and "ordered_vector_branch_paths" not in row
            for row in branch_terms
        ),
        "cut_bindings_and_children_structurally_inside_complete_contact": complete_contact[
            "Q_cut"
        ]["counts"]
        == collapsed["counts"]
        and len(complete_contact["Q_cut"]["records"]) == 48
        and len(complete_contact["Q_cut"]["unique_children"]) == 6
        and all(row["coefficient"] == "OPEN" for row in complete_contact["Q_cut"]["records"]),
        "single_sign_transport_is_open_and_signs_are_representation_specific": complete_contact[
            "single_sign_transport"
        ]["status"]
        == "FAIL_CLOSED_NOT_DERIVED"
        and all(row["sign_usage"] == "HESSIAN_REPRESENTATION_ONLY" for row in branch_terms)
        and all(
            row["scalar_coefficient"]["coefficient_usage"]
            == "WICK_REPRESENTATION_ONLY_DO_NOT_MULTIPLY_BY_HESSIAN_NEUMANN_SIGN"
            for row in projection["records"]
        ),
        "I0H2_projector_remains_fail_closed": quadratic["I0_H2"]["status"]
        == "FAIL_CLOSED_H2_PROJECTOR_DALGEBRA_NORMALIZATION_OPEN",
        "color_scope_is_index_incidence_only": color["status"]
        == "INDEX_INCIDENCE_ONLY_PHYSICAL_COLOR_REDUCTION_OPEN"
        and color["physical_color_reduction"] == "FAIL_CLOSED_NOT_COMPUTED"
        and bubble_color_ids == bubble_scalar_ids
        and tadpole_color_ids == tadpole_scalar_ids,
        "retained_color_index_ledgers_close": all(
            all(row["tensor"]["checks"].values()) for row in color_rows
        ),
        "scalar_color_split_is_explicitly_scoped": all(
            "kappa" not in row["scalar_coefficient"]["stripped_after_hg2_reduction"]["rendered"]
            for row in projection["records"]
        )
        and all(
            "kappa" not in row["scalar_coefficient_before_zero"]["rendered"]
            for row in tadpoles["records"]
        ),
        "projector_scope_partition_reconstructed_from_rows": projection["counts"][
            "both_exact_local"
        ]
        == sum(row["both_external_projectors_local"] for row in projection["records"])
        and projection["counts"]["requires_shared_scope_D_algebra"]
        == sum(not row["both_external_projectors_local"] for row in projection["records"]),
        "I4_zero_is_conditional_not_certified": tadpoles["counts"]
        == {
            "admitted_self_contractions": 180,
            "conditional_DRED_zero": 180,
            "certified_DRED_zero": 0,
            "projection_pending": 180,
        }
        and all(row["missing_edge_tagged_locality_to_polynomial_proof"] for row in tadpoles["records"]),
        "automorphism_is_assigned_audit_only": payload["typed_automorphisms"]["status"]
        == "ASSIGNED_ORDER_ONE_AUDIT_ONLY_PHYSICAL_STABILIZER_OPEN"
        and payload["typed_automorphisms"]["physical_stabilizers"]
        == "FAIL_CLOSED_NOT_COMPUTED"
        and payload["typed_automorphisms"]["automorphism_division_applied"] is False,
        "collapsed_binding_partition_reconstructed": collapsed["counts"]
        == {
            "trace_edge_bindings": 48,
            "unique_child_GraphIR": 6,
            "per_orientation": {"DIRECT": 24, "REFLECTED": 24},
            "per_collapsed_edge": {"e0": 16, "e1": 16, "e2": 16},
        },
        "all_contact_obligations_are_fail_closed": all(
            row["severity"] != "CLOSED" and "missing" in row for row in obligations
        )
        and payload["open_proof_obligation_ids"] == [row["id"] for row in obligations],
        "tau_channel_retained_as_open": payload["DRED_tensor_basis"]["policy"]
        == "OPEN_TAU_CHANNEL_IS_NEVER_REPLACED_BY_2epsilon",
        "physical_contact_pole_and_anomaly_remain_unassigned": payload["pole_boundary"][
            "complete_contact_ordinary_UV_pole"
        ].startswith("NOT_COMPUTED")
        and payload["pole_boundary"]["anomaly_coefficient"] == "NOT_ACCEPTED"
        and payload["pole_boundary"]["invalidated_coefficient_reused"] is False,
        "external_result_import_flag_is_false": payload["external_results_imported"] is False,
    }


def render_markdown(payload: Mapping[str, object], invariants: Mapping[str, bool]) -> str:
    projection = payload["bubble_projection_and_coefficient"]
    replacements = {
        "@NX@": str(projection["counts"]["I3_exact_local_X"]),
        "@NTW@": str(projection["counts"]["S3_exact_local_TildeW"]),
        "@NBOTH@": str(projection["counts"]["both_exact_local"]),
        "@NSHARED@": str(projection["counts"]["requires_shared_scope_D_algebra"]),
        "@NINV@": str(len(invariants)),
        "@NFAIL@": str(sum(not value for value in invariants.values())),
    }
    text = r"""# Step 5 WW quadratic contact/cut replay

## 0. Notation

$$
X:=\nabla_+W_+,\qquad
\mathscr I^{AB}:=\nabla_-(X^AX^B),\qquad
\tau^{mn}:=\widetilde\delta^{mn}-\frac\epsilon2\delta_{(4)}^{mn},\qquad
\delta_{(4)mn}\tau^{mn}=0.
$$

## 1. Hessian and physical contact families

$$
\begin{aligned}
Q_{\rm Hess}^{(2)}={}&
-\frac12\operatorname{STr}_{\rm DRED}(I_0G_0H_2G_0)
-\frac12\operatorname{STr}_{\rm DRED}(I_1[p_1]G_0H_1[p_2]G_0)\\
&-\frac12\operatorname{STr}_{\rm DRED}(I_1[p_2]G_0H_1[p_1]G_0)
+\frac12\operatorname{STr}_{\rm DRED}(I_2G_0),\\
Q_{\rm cut}^{(2)}={}&
\sum_{o\in\{\mathrm D,\mathrm R\}}
\sum_{t=1}^{8}\sum_{e\in\{e_0,e_1,e_2\}}
C_{o,t,e}\operatorname{Collapse}_e(\Gamma_{\triangle,o,t}),\\
Q_{\rm phys}^{(2)}={}&Q_{\rm Hess}^{(2)}+Q_{\rm cut}^{(2)}+\mathrm{CT}_2.
\end{aligned}
$$

This is a regrouping, not an additional contribution:

$$
Q_{\rm cut}^{(2)}=\mathcal R_{\rm cut}Q_{\triangle}^{\rm bare},
\qquad
Q_{\triangle}^{\rm irr}
=(1-\mathcal R_{\rm cut})Q_{\triangle}^{\rm bare},
$$

$$
\Gamma_{\mathscr I,{\rm ren,DRED},2}^{(1),{\rm reg}}
=Q_{\triangle}^{\rm irr}+Q_{\rm phys}^{(2)},
\qquad
\mathcal R_{\rm cut}=\texttt{NOT\_CONSTRUCTED}.
$$

$$
N_{\rm collapse\ bindings}=48,\qquad
N_{\rm unique\ cut\ GraphIR}=6,\qquad
C_{o,t,e}=\texttt{OPEN},\qquad
C_{\mathrm{CT}_2}=\texttt{OPEN}.
$$

The following numbers are branch-path input literals, not graph counts:

$$
(B_{I_0H_2},B_{I_1H_1;p_1p_2},B_{I_1H_1;p_2p_1},B_{I_2})
=(576,1440,1440,720),\qquad
B_r=\texttt{NOT\_GENERATED}.
$$

## 2. Single-sign transport

$$
e^{-S_3/\hbar}=1-\frac{S_3}{\hbar}+\frac{S_3^2}{2\hbar^2}+\cdots,
\qquad C_{\rm Wick}(I_1,S_3)=-1.
$$

$$
C_{\rm Wick}(I_1,S_3)=C_{\rm Hess}(I_1,H_1)
=\texttt{NOT\_DERIVED}.
$$

$$
C_{\rm row}\neq
C_{\rm Wick}\,C_{\rm Neumann}\,C_{\rm stripped};
\qquad
\text{exactly one representation sign is used.}
$$

## 3. Projector census

$$
X_{(1)}=-\frac18D_+\bar D^2D_+V,\qquad
\widetilde W_{(1)\dot a}=-\frac18D^2\bar D_{\dot a}V.
$$

$$
N_{X,\rm local}=@NX@,\qquad
N_{\widetilde W,\rm local}=@NTW@,\qquad
N_{\rm both,local}=@NBOTH@,\qquad
N_{\rm shared}=@NSHARED@.
$$

$$
\Pi_{X\widetilde W}H_2=\texttt{NOT\_DERIVED},\qquad
\Pi_{X\widetilde W}I_2=\texttt{NOT\_DERIVED}.
$$

## 4. Conditional I4 statement

$$
\left[
P(k,p_1,p_2)\in\mathbb Q[k,p_1,p_2]
\ \land\
\mathrm{Den}(k)=k^2
\right]
\Longrightarrow
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}\frac{P(k,p_1,p_2)}{k^2}=0.
$$

$$
N_{I_4,\rm conditional\ zero}=180,\qquad
N_{I_4,\rm certified\ zero}=0.
$$

The edge-tagged locality-to-polynomial implication is open.

## 5. Color and automorphism scope

$$
N_{\rm compiled\ incidence\ rows}=360+180=540,
\qquad
\mathcal C_{\rm red}
:=\left[\sum_r C_rT_r^{AB}{}_{DE}\right]
\Big/(\text{Jacobi},\text{antisymmetry},\kappa\text{-invariance}),
$$

$$
\operatorname{status}\!\left(\mathcal C_{\rm red}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED}.
$$

$$
|\operatorname{Aut}_{\mathfrak N}|_{\rm assigned}=1,\qquad
\operatorname{status}\!\left(
|\operatorname{Aut}_{\rm physical}|\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(\text{Taylor/Wick factorial matching proved}\right)
=\texttt{NOT\_COMPUTED}.
$$

## 6. Boundary

$$
\operatorname{status}\!\left(Q_{\rm phys,pole}^{(2)}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(Q_{\tau,\rm pole}^{(2)}\text{ evaluated}\right)
=\texttt{NOT\_COMPUTED},\qquad
\operatorname{status}\!\left(C_{\rm anomaly}\text{ accepted}\right)
=\texttt{NOT\_ACCEPTED}.
$$

Schema invariants: @NINV@ checked, @NFAIL@ failed.  They certify serialization and fail-closed scope only.
"""
    for marker, value in replacements.items():
        text = text.replace(marker, value)
    return text


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def write_outputs(payload: Mapping[str, object], invariants: Mapping[str, bool]) -> None:
    payload_bytes = canonical_bytes(payload)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(payload_bytes)
    AUDIT_MD.write_text(render_markdown(payload, invariants), encoding="utf-8")
    failed = sorted(key for key, value in invariants.items() if not value)
    obligations = payload["proof_obligations"]
    resolved_gates = [
        row["id"] for row in obligations if row["severity"] == "CLOSED"
    ]
    fail_closed_gates = [
        row["id"] for row in obligations if row["severity"] != "CLOSED"
    ]
    audit = {
        "schema": "Step5WWContactReplayAudit.v2",
        "status": (
            "FAIL_CLOSED_PHYSICAL_CONTACT_FAMILY_WITH_SCHEMA_INVARIANTS"
            if not failed
            else "INVALID_SCHEMA_INVARIANTS"
        ),
        "generated_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "scope_of_invariants": (
            "serialization, row incidence, structural census, and fail-closed boundaries; "
            "not a contact amplitude proof"
        ),
        "totals": {"schema_invariants": len(invariants), "failed": len(failed)},
        "failed_schema_invariants": failed,
        "resolved_gates": resolved_gates,
        "fail_closed_gates": fail_closed_gates,
        "ordinary_contact_UV_pole": "NOT_COMPUTED",
        "tau_channel": "RETAINED_OPEN",
        "anomaly_coefficient": "NOT_ACCEPTED",
    }
    AUDIT_JSON.write_bytes(canonical_bytes(audit))


def main() -> int:
    payload = build_payload()
    invariants = scope_invariants(payload)
    write_outputs(payload, invariants)
    failed = [key for key, value in invariants.items() if not value]
    print(
        json.dumps(
            {
                "schema_invariants": {"total": len(invariants), "failed": len(failed)},
                "open": payload["open_proof_obligation_ids"],
                "projection_counts": payload["bubble_projection_and_coefficient"]["counts"],
            },
            sort_keys=True,
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
