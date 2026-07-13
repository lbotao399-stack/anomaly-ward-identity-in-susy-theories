#!/usr/bin/env python3

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from scripts.step6_two_loop_dword import (
    BLOCKED_STATUS,
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
    lexicographically_decreases,
    phase_measure_decreases,
    theta_decomposition,
    validate_derivative_token,
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
