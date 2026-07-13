#!/usr/bin/env python3

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from scripts.step6_two_loop_dword import (
    BLOCKED_STATUS,
    EXECUTOR_RESULT_VERSION,
    EXECUTOR_SCHEMA_VERSION,
    INPUT_SCHEMA_VERSION,
    MEASURE_COMPONENTS,
    MINUS_ONE,
    ONE,
    PHASE_ORDER,
    READY_STATUS,
    ExactLedgerEntry,
    GaussianRational,
    build_audit,
    build_payload,
    compile_schedule_contract,
    deterministic_missing_inputs,
    endpoint_square_polynomial,
    exact_executor_fixtures,
    execute_edge_tagged_dalgebra,
    graph_executor_endpoints,
    lexicographically_decreases,
    phase_measure_decreases,
    theta_decomposition,
    validate_derivative_token,
    validate_global_join_key,
    validate_polynomial_oracle,
)
from scripts.step6_two_loop_graphir import (
    build_bundle,
    build_direct_i2_s3_squared_s4,
    build_direct_i3_s3_cubed,
)


ROOT = Path(__file__).resolve().parents[1]


def qi(re: int | str = 0, im: int | str = 0) -> dict[str, str]:
    return {"domain": "Q(i)", "re": str(re), "im": str(im)}


def exact_identity() -> dict[str, object]:
    polynomial = {
        "terms": [
            {
                "powers": {"x": 1},
                "factor": qi(1),
            }
        ]
    }
    return {
        "proof_mode": "EXACT_SYMBOLIC_POLYNOMIAL_IDENTITY",
        "coefficient_domain": "Q(i)",
        "variables": ["x"],
        "identities": [
            {
                "identity_id": "TEST_ONLY_FORMAL_IDENTITY_X_EQUALS_X",
                "lhs": deepcopy(polynomial),
                "rhs": deepcopy(polynomial),
            }
        ],
    }


def typed_token(graph: dict[str, object], edge_id: str, endpoint: str) -> dict[str, object]:
    edge = next(edge for edge in graph["internal_edges"] if edge["edge_id"] == edge_id)
    return {
        "token_id": "TEST_ONLY_NONPHYSICAL_SCHEMA_TOKEN",
        "derivative_kind": "D",
        "spinor_index_space": "UNDOTTED",
        "spinor_indices": ["a_test"],
        "operator_parity": 1,
        "edge_id": edge_id,
        "endpoint_port_id": endpoint,
        "momentum": {
            "basis": list(graph["momentum_contract"]["basis"]),
            "coefficients": list(edge["momentum_vector"]),
            "orientation_sign_from_edge": 1,
            "space": graph["momentum_contract"]["square_space"],
        },
    }


def formal_complete_record(graph: dict[str, object]) -> dict[str, object]:
    """A nonphysical schema fixture; it asserts no Project derivative scope."""

    theta = theta_decomposition(graph)
    central = next(
        edge for edge in graph["internal_edges"] if edge["edge_id"] == theta["central_edge_id"]
    )
    token = typed_token(graph, central["edge_id"], central["source_port"])
    identity_id = "TEST_ONLY_FORMAL_IDENTITY_X_EQUALS_X"
    return {
        "schema_version": INPUT_SCHEMA_VERSION,
        "graph_id": graph["graph_id"],
        "graph_hash": graph["graph_hash"],
        "notation_schema_hash": "0" * 64,
        "wick_complete": True,
        "wick_pairings": [
            {
                "edge_id": edge["edge_id"],
                "endpoint_ports": [edge["source_port"], edge["target_port"]],
                "ordered_field_types": ["TEST_V_LEFT", "TEST_V_RIGHT"],
            }
            for edge in graph["internal_edges"]
        ],
        "wick_completeness_certificate": {
            "every_quantum_port_used_once": True,
            "connected": True,
            "pairing_edge_ids_equal_graph_edge_ids": True,
        },
        "ordered_derivative_scope_ast": {
            "node_type": "ORDERED_SCOPE",
            "scope_id": "TEST_ONLY_NONPHYSICAL_SCHEMA_SCOPE",
            "ordered_children": [
                {
                    "node_type": "DERIVATIVE_APPLICATION",
                    "token": token,
                    "argument": {
                        "node_type": "FIELD_PORT",
                        "port_id": central["source_port"],
                        "field_type": "TEST_V",
                        "parity": 0,
                    },
                }
            ],
        },
        "propagator_kernels": [
            {
                "edge_id": edge["edge_id"],
                "endpoint_ports": [edge["source_port"], edge["target_port"]],
                "ordered_field_types": ["TEST_V_LEFT", "TEST_V_RIGHT"],
                "ordered_kernel_ast": {
                    "node_type": "ORDERED_PROPAGATOR_KERNEL",
                    "ordered_derivative_tokens": [],
                    "grassmann_delta_ast": {"node_type": "TEST_FORMAL_DELTA"},
                    "scalar_denominator_ast": {"node_type": "TEST_FORMAL_DENOMINATOR"},
                },
                "oracle_identity_ids": [identity_id],
            }
            for edge in graph["internal_edges"]
        ],
        "exact_sign_koszul_ledger": [
            {
                "ledger_id": "TEST_ONLY_KOSZUL_ENTRY",
                "phase": "PRIMITIVE_NORMAL_ORDERING",
                "kind": "KOSZUL",
                "factor": qi(-1),
                "rule_id": "(-1)^(1*1)",
                "token_ids": [token["token_id"]],
                "moving_parity": 1,
                "crossed_parities": [1],
                "oracle_identity_id": None,
            }
        ],
        "polynomial_oracle": exact_identity(),
    }


class Step6TwoLoopDWordTests(unittest.TestCase):
    def setUp(self) -> None:
        self.i3 = build_direct_i3_s3_cubed()
        self.i2 = build_direct_i2_s3_squared_s4()

    def test_real_graphs_fail_closed_with_deterministic_missing_inputs(self) -> None:
        payload = build_payload()
        self.assertEqual(tuple(payload["phase_order"]), PHASE_ORDER)
        self.assertEqual(tuple(payload["termination_measure"]["components"]), MEASURE_COMPONENTS)
        literal_graphs = build_bundle()["literal_direct_graphs"]
        self.assertEqual(len(payload["graph_contracts"]), len(literal_graphs))
        self.assertGreater(len(literal_graphs), 0)
        for graph, contract in zip(literal_graphs, payload["graph_contracts"]):
            self.assertEqual(contract["status"], BLOCKED_STATUS)
            self.assertEqual(contract["missing_inputs"], sorted(contract["missing_inputs"]))
            self.assertEqual(
                tuple(contract["missing_inputs"]),
                deterministic_missing_inputs(graph, None),
            )
            self.assertIsNone(contract["phase_execution"])

    def test_rooted_theta_tree_central_edge_and_chords_are_exact(self) -> None:
        i3 = theta_decomposition(self.i3)
        self.assertEqual(i3["root_vertex_id"], "I")
        self.assertEqual(i3["central_edge_id"], "e_CI")
        self.assertEqual(i3["spanning_tree_edge_ids"], ["e_AI", "e_BI", "e_CI"])
        self.assertEqual(i3["chord_edge_ids"], ["e_CA", "e_CB"])
        i2 = theta_decomposition(self.i2)
        self.assertEqual(i2["root_vertex_id"], "I")
        self.assertEqual(i2["central_edge_id"], "e_BC")
        self.assertEqual(i2["spanning_tree_edge_ids"], ["e_BA", "e_BC", "e_BI"])
        self.assertEqual(i2["chord_edge_ids"], ["e_AC", "e_IC"])
        for theta in (i3, i2):
            self.assertEqual(theta["cycle_rank_certificate"]["I_minus_V_plus_1"], 2)
            self.assertEqual(theta["cycle_rank_certificate"]["chord_count"], 2)
            self.assertTrue(theta["cycle_rank_certificate"]["passed"])

    def test_lexicographic_measure_is_exact_and_requires_natural_numbers(self) -> None:
        before = (1, 9, 9, 9, 9, 9, 9, 9)
        after = (0, 100, 100, 100, 100, 100, 100, 100)
        self.assertTrue(lexicographically_decreases(before, after))
        self.assertFalse(lexicographically_decreases(after, before))
        self.assertFalse(lexicographically_decreases(before, before))
        self.assertTrue(
            phase_measure_decreases(
                "ENDPOINT_CANONICALIZATION",
                (0, 2, 9, 9, 9, 9, 9, 9),
                (0, 1, 100, 100, 100, 100, 100, 100),
            )
        )
        self.assertFalse(
            phase_measure_decreases(
                "ENDPOINT_CANONICALIZATION",
                (1, 2, 9, 9, 9, 9, 9, 9),
                (0, 1, 0, 0, 0, 0, 0, 0),
            )
        )
        with self.assertRaisesRegex(ValueError, "wrong arity"):
            lexicographically_decreases((1,), (0,))
        with self.assertRaisesRegex(ValueError, r"N\^8"):
            lexicographically_decreases((0,) * 8, (-1,) + (0,) * 7)

    def test_exact_qi_and_koszul_ledger(self) -> None:
        self.assertEqual(
            GaussianRational(Fraction(1, 2), Fraction(1, 3))
            * GaussianRational(Fraction(1, 2), Fraction(-1, 3)),
            GaussianRational(Fraction(13, 36), Fraction(0)),
        )
        entry = ExactLedgerEntry(
            ledger_id="K",
            phase="PIVOTED_IBP",
            kind="KOSZUL",
            factor=MINUS_ONE,
            rule_id="(-1)^(1*1)",
            token_ids=("t",),
            moving_parity=1,
            crossed_parities=(1,),
        )
        self.assertEqual(entry.factor, MINUS_ONE)
        with self.assertRaisesRegex(ValueError, "Koszul factor"):
            ExactLedgerEntry(
                ledger_id="bad",
                phase="PIVOTED_IBP",
                kind="KOSZUL",
                factor=ONE,
                rule_id="wrong",
                token_ids=("t",),
                moving_parity=1,
                crossed_parities=(1,),
            )

    def test_polynomial_oracle_uses_exact_coefficients_not_samples(self) -> None:
        certificate = validate_polynomial_oracle(exact_identity())
        self.assertFalse(certificate["numerical_sampling_used"])
        self.assertEqual(certificate["checks"][0]["method"], "EXACT_MONOMIAL_COEFFICIENT_COMPARISON")
        unequal = exact_identity()
        unequal["identities"][0]["rhs"]["terms"][0]["factor"] = qi(2)
        with self.assertRaisesRegex(ValueError, "identity fails"):
            validate_polynomial_oracle(unequal)
        sampled = exact_identity()
        sampled["sample_points"] = [0, 1]
        with self.assertRaisesRegex(ValueError, "sampling is forbidden"):
            validate_polynomial_oracle(sampled)

    def test_derivative_token_carries_exact_edge_endpoint_and_momentum(self) -> None:
        theta = theta_decomposition(self.i3)
        central = next(
            edge for edge in self.i3["internal_edges"] if edge["edge_id"] == theta["central_edge_id"]
        )
        token = typed_token(self.i3, central["edge_id"], central["source_port"])
        normalized = validate_derivative_token(token, self.i3)
        self.assertEqual(normalized["edge_id"], "e_CI")
        self.assertEqual(normalized["endpoint_port_id"], central["source_port"])
        broken = deepcopy(token)
        broken["momentum"]["coefficients"][0] += 1
        with self.assertRaisesRegex(ValueError, "exact oriented copy"):
            validate_derivative_token(broken, self.i3)

    def test_formal_complete_record_emits_only_pending_phase_contract(self) -> None:
        record = formal_complete_record(self.i3)
        result = compile_schedule_contract(self.i3, record)
        self.assertEqual(result["status"], READY_STATUS)
        self.assertEqual([phase["phase"] for phase in result["phase_execution"]], list(PHASE_ORDER))
        self.assertTrue(all(phase["status"] == "PENDING_EXACT_REWRITE_EXECUTION" for phase in result["phase_execution"]))
        self.assertTrue(all(phase["before_measure"] is None for phase in result["phase_execution"]))
        self.assertTrue(all(phase["after_measure"] is None for phase in result["phase_execution"]))
        self.assertIsNone(result["evaluated_word"])
        self.assertFalse(result["global_confluence_claimed"])

    def test_graph_executor_endpoints_cover_internal_external_and_composite(self) -> None:
        endpoints = graph_executor_endpoints(self.i3)
        kinds = {endpoint["endpoint_kind"] for endpoint in endpoints}
        self.assertEqual(
            kinds,
            {
                "INTERNAL_SOURCE",
                "INTERNAL_TARGET",
                "EXTERNAL_BACKGROUND",
                "COMPOSITE_SOURCE",
            },
        )
        by_id = {endpoint["endpoint_id"]: endpoint for endpoint in endpoints}
        for edge in self.i3["internal_edges"]:
            source = by_id[edge["source_port"]]
            target = by_id[edge["target_port"]]
            self.assertEqual(
                target["momentum"]["coefficients"],
                [-value for value in source["momentum"]["coefficients"]],
            )
            self.assertEqual(source["paired_endpoint_id"], target["endpoint_id"])
            self.assertEqual(target["paired_endpoint_id"], source["endpoint_id"])

    def test_exact_graded_ibp_retains_external_composite_token_and_sign(self) -> None:
        fixtures = exact_executor_fixtures(self.i3)
        result = next(
            item
            for item in fixtures["results"]
            if item["program_id"] == "FIXTURE_GRADED_IBP_EXTERNAL_TO_COMPOSITE"
        )
        self.assertEqual(result["schema_version"], EXECUTOR_RESULT_VERSION)
        self.assertEqual(len(result["terms"]), 2)
        by_component = {
            term["ordered_tokens"][0]["spinor_component"]: term for term in result["terms"]
        }
        self.assertEqual(by_component["+"]["polynomial"], [{"monomial": [], "factor": qi(-1)}])
        self.assertEqual(by_component["-"]["polynomial"], [{"monomial": [], "factor": qi(1)}])
        for term in result["terms"]:
            self.assertEqual(term["ordered_tokens"][0]["endpoint_id"], "fixture.composite")
            self.assertEqual(
                set(term["classifications"]),
                {"COMPOSITE_SOURCE_DERIVATIVE", "D_ALGEBRA_REMAINDER", "EOM_REMAINDER"},
            )
            ledger_kinds = {
                ledger["kind"]
                for provenance in term["provenance"]
                for ledger in provenance["ledger"]
            }
            self.assertEqual(ledger_kinds, {"ENDPOINT_TRANSFER", "KOSZUL"})
        odd_koszul = [
            ledger
            for provenance in by_component["-"]["provenance"]
            for ledger in provenance["ledger"]
            if ledger["kind"] == "KOSZUL"
        ]
        self.assertEqual(odd_koszul[0]["factor"], qi(-1))

    def test_internal_endpoint_transfer_and_mixed_anticommutator_execute(self) -> None:
        fixtures = exact_executor_fixtures(self.i3)
        result = next(
            item
            for item in fixtures["results"]
            if item["program_id"] == "FIXTURE_INTERNAL_TARGET_TRANSFER_AND_MIXED_MOMENTUM"
        )
        scalar = next(term for term in result["terms"] if not term["ordered_tokens"])
        self.assertEqual(scalar["classifications"], ["SCALAR_REMAINDER"])
        self.assertTrue(scalar["polynomial"])
        ledger = [
            entry
            for provenance in scalar["provenance"]
            for entry in provenance["ledger"]
        ]
        self.assertEqual(
            sum(entry["kind"] == "ENDPOINT_TRANSFER" for entry in ledger),
            2,
        )
        self.assertEqual(
            sum(entry["kind"] == "MIXED_ANTICOMMUTATOR" for entry in ledger),
            1,
        )
        self.assertEqual(result["mixed_anticommutator"], "{D_a,barD_dota}=-2*i*p_(a,dota)")

    def test_nilpotence_chirality_and_eom_are_typed_classifications(self) -> None:
        fixtures = exact_executor_fixtures(self.i3)
        result = next(
            item
            for item in fixtures["results"]
            if item["program_id"] == "FIXTURE_NILPOTENCE_CHIRALITY_EOM"
        )
        classes = [zero["classification"] for zero in result["zero_terms"]]
        self.assertEqual(classes.count("NILPOTENT_ZERO"), 1)
        self.assertEqual(classes.count("CHIRALITY_ZERO"), 2)
        self.assertTrue(any("EOM_REMAINDER" in term["classifications"] for term in result["terms"]))

    def test_exact_momentum_determinant_collapses_one_propagator(self) -> None:
        fixtures = exact_executor_fixtures(self.i3)
        result = next(
            item
            for item in fixtures["results"]
            if item["program_id"] == "FIXTURE_EXACT_R_SQUARE_PROPAGATOR_COLLAPSE"
        )
        collapsed = [
            term for term in result["terms"] if "PROPAGATOR_COLLAPSE" in term["classifications"]
        ]
        self.assertEqual(len(collapsed), 1)
        self.assertEqual(collapsed[0]["polynomial"], [{"monomial": [], "factor": qi(-4)}])
        self.assertEqual(collapsed[0]["remaining_denominator_edges"], [])
        self.assertEqual(collapsed[0]["collapsed_edges"][0]["quotient"], qi(-4))
        self.assertFalse(result["DRED_performed"])
        self.assertFalse(result["IBP_integral_reduction_performed"])
        self.assertIsNone(result["UV_pole"])
        self.assertIsNone(result["two_loop_coefficient"])

    def test_executor_rejects_unknown_endpoint_and_schema(self) -> None:
        program = {
            "schema_version": EXECUTOR_SCHEMA_VERSION,
            "program_id": "bad",
            "program_kind": "FIXTURE",
            "left_coefficient_order": True,
            "endpoints": [],
            "branches": [
                {
                    "branch_id": "b",
                    "coefficient": qi(1),
                    "ordered_tokens": [
                        {
                            "token_id": "D",
                            "derivative_kind": "D",
                            "spinor_component": "+",
                            "endpoint_id": "missing",
                            "carrier": "FIELD",
                        }
                    ],
                    "denominator_edges": [],
                }
            ],
            "ibp_transfers": [],
        }
        with self.assertRaisesRegex(ValueError, "unknown endpoint"):
            execute_edge_tagged_dalgebra(program)
        program["schema_version"] = "wrong"
        with self.assertRaisesRegex(ValueError, "schema version"):
            execute_edge_tagged_dalgebra(program)

    def test_global_numerator_join_key_preserves_option_tuple_and_left_word(self) -> None:
        join_key = {
            "parent_id": "PARENT_FIXTURE",
            "parent_vertex_order": ["I", "A", "B", "C"],
            "ordered_local_amplitude_option_ids": ["I.opt", "A.opt", "B.opt", "C.opt"],
            "global_left_coefficient_word": [
                {
                    "coefficient_id": f"x{index}",
                    "basis_index": index,
                    "parity": index.bit_count() & 1,
                }
                for index in range(10)
            ],
            "fixed_edge_pairing_order": [
                {
                    "edge_id": f"e{edge}",
                    "source_coefficient_id": f"x{2 * edge}",
                    "target_coefficient_id": f"x{2 * edge + 1}",
                }
                for edge in range(5)
            ],
        }
        normalized = validate_global_join_key(join_key)
        self.assertEqual(
            normalized["ordered_local_amplitude_option_ids"],
            ["I.opt", "A.opt", "B.opt", "C.opt"],
        )
        self.assertEqual(
            [entry["coefficient_id"] for entry in normalized["global_left_coefficient_word"]],
            [f"x{index}" for index in range(10)],
        )
        self.assertEqual(len(normalized["join_key_hash"]), 64)
        broken = deepcopy(join_key)
        broken["global_left_coefficient_word"][1]["parity"] = 0
        with self.assertRaisesRegex(ValueError, "popcount"):
            validate_global_join_key(broken)

    def test_missing_one_kernel_never_compiles(self) -> None:
        record = formal_complete_record(self.i2)
        missing_edge = record["propagator_kernels"].pop()["edge_id"]
        result = compile_schedule_contract(self.i2, record)
        self.assertEqual(result["status"], BLOCKED_STATUS)
        self.assertIn(f"wick_record.propagator_kernels[{missing_edge}]", result["missing_inputs"])
        self.assertIsNone(result["phase_execution"])

    def test_central_critical_pairs_are_declared_but_not_joined(self) -> None:
        payload = build_payload()
        for contract in payload["graph_contracts"]:
            central = contract["theta_decomposition"]["central_edge_id"]
            pairs = contract["critical_pairs"]
            self.assertEqual({pair["central_edge_id"] for pair in pairs}, {central})
            self.assertEqual(
                {pair["status"] for pair in pairs},
                {"DECLARED_UNJOINED_UNTIL_EXACT_WORD_INPUT"},
            )
            self.assertTrue(all(value is None for pair in pairs for value in pair["required_certificate"].values()))
            self.assertFalse(contract["global_confluence_claimed"])

    def test_exact_internal_audit_passes(self) -> None:
        audit = build_audit(build_payload())
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["failed"], 0)
        self.assertEqual(audit["passed"], len(audit["checks"]))

    def test_generated_artifacts_match_contract(self) -> None:
        payload = json.loads(
            (ROOT / "generated/step6/two-loop-dword/dword-contract.json").read_text()
        )
        schema = json.loads(
            (ROOT / "generated/step6/two-loop-dword/wick-input-schema.json").read_text()
        )
        audit = json.loads(
            (ROOT / "audits/step6-two-loop-dword-verification.json").read_text()
        )
        self.assertEqual(payload, build_payload())
        self.assertEqual(schema["schema_version"], INPUT_SCHEMA_VERSION)
        self.assertEqual(len(schema["graph_schemas"]), len(build_bundle()["literal_direct_graphs"]))
        self.assertEqual(audit, build_audit(payload))


if __name__ == "__main__":
    unittest.main()
