from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import unittest

from scripts.step6_two_loop_graphir import build_bundle as build_graph_bundle
from scripts.step6_two_loop_integrals import (
    EXTERNAL_INVARIANT_BASIS,
    IBP_DOT_VECTORS,
    INTERNAL_SCALAR_BASIS,
    LOOP_VECTORS,
    SCALAR_BASIS,
    TWO_LOOP_MEASURE,
    build_audit,
    build_integral_bundle,
    direct_denominator_derivative,
    directional_derivative_numerator,
    directional_derivative_polynomial,
    instantiate_ibp_identity,
    polynomial,
    polynomial_is_zero,
    quadratic_form_row,
    reduce_routing_after_P,
    render_polynomial,
    rref,
    tensor_polynomial,
    variable_polynomial,
)


ROOT = Path(__file__).resolve().parents[1]


class Step6TwoLoopIntegralFamilyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_bundle = build_graph_bundle()
        self.bundle = build_integral_bundle()
        self.families = self.bundle["integral_families"]
        self.by_graph = {family["source_graph_id"]: family for family in self.families}

    def test_graph_selection_is_dynamic_and_exactly_matches_current_literal_parents(self) -> None:
        expected = [
            graph["graph_id"]
            for graph in self.graph_bundle["literal_direct_graphs"]
            if graph["classification"] == "LITERAL_K4_MINUS_EDGE_DIRECT_PARENT"
            and graph["topology"] == "K4_MINUS_ONE_EDGE"
        ]
        selection = self.bundle["dynamic_graph_selection"]
        self.assertFalse(selection["hardcoded_graph_count"])
        self.assertEqual(selection["source_graph_ids"], expected)
        self.assertEqual(selection["source_graph_count"], len(expected))
        self.assertEqual([family["source_graph_id"] for family in self.families], expected)

    def test_P_substitution_and_first_family_quadratic_forms_are_exact(self) -> None:
        self.assertEqual(reduce_routing_after_P((1, 0, -1, 0, 0)), (1, 0, 1, 1))
        family = self.by_graph["G6_DIRECT_K4ME_I3_S3CUBED"]
        rows = {item["edge_id"]: item["quadratic_form_row"] for item in family["denominators"]}
        self.assertEqual(rows["e_CI"], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(rows["e_CA"], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(rows["e_AI"], [0, 1, 0, 0, 0, -2, 0, 1, 0, 0])
        self.assertEqual(rows["e_CB"], [1, 1, 2, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(rows["e_BI"], [1, 1, 2, 0, 2, 0, 2, 0, 1, 0])
        for denominator in family["denominators"]:
            self.assertEqual(
                denominator["quadratic_form_row"],
                list(quadratic_form_row(denominator["reduced_routing_vector"])),
            )
            self.assertNotIn("P", denominator["quadratic_form_rendered"])

    def test_source_shifted_denominators_include_all_external_invariants(self) -> None:
        family = self.by_graph["G6_DIRECT_K4ME_I2_S3SQ_S4"]
        by_edge = {item["edge_id"]: item for item in family["denominators"]}
        self.assertEqual(by_edge["e_IC"]["reduced_routing_vector"], [1, 0, 1, 1])
        self.assertEqual(
            by_edge["e_IC"]["quadratic_form_row"],
            [1, 0, 0, 2, 2, 0, 0, 1, 1, 2],
        )
        self.assertEqual(tuple(family["internal_scalar_basis"]), INTERNAL_SCALAR_BASIS)
        self.assertEqual(tuple(family["external_invariant_basis"]), EXTERNAL_INVARIANT_BASIS)
        self.assertEqual(tuple(family["scalar_basis"]), SCALAR_BASIS)

    def test_exact_rref_rank_and_isp_count(self) -> None:
        for family in self.families:
            certificate = family["rank_certificate"]
            reduced, pivots = rref(certificate["loop_scalar_matrix"])
            self.assertEqual(certificate["loop_scalar_rank"], len(pivots))
            self.assertEqual(certificate["loop_scalar_rank"], 5)
            self.assertEqual(certificate["isp_count"], 2)
            self.assertEqual(
                certificate["loop_scalar_rank"] + certificate["isp_count"],
                len(INTERNAL_SCALAR_BASIS),
            )
            self.assertEqual(
                certificate["canonical_free_isp_variables"],
                [
                    INTERNAL_SCALAR_BASIS[index]
                    for index in certificate["canonical_free_isp_columns"]
                ],
            )
            self.assertEqual(len(reduced), len(family["denominators"]))

    def test_all_sector_and_pinch_ids_exist_without_connectivity_claim(self) -> None:
        for family in self.families:
            sectors = family["sectors"]
            denominator_count = len(family["denominators"])
            self.assertEqual(len(sectors), 2**denominator_count)
            self.assertEqual(len({item["sector_id"] for item in sectors}), len(sectors))
            self.assertEqual(len({item["pinch_id"] for item in sectors}), len(sectors))
            self.assertIn(f"SECTOR_{'0' * denominator_count}", {item["sector_id"] for item in sectors})
            self.assertIn(f"SECTOR_{'1' * denominator_count}", {item["sector_id"] for item in sectors})
            for sector in sectors:
                self.assertEqual(
                    sector["graph_connectivity_status"],
                    "NOT_EVALUATED_BY_INTEGRAL_SECTOR_ENUMERATION",
                )
                self.assertEqual(
                    set(sector["active_edge_ids"]) | set(sector["pinched_edge_ids"]),
                    set(family["edge_order"]),
                )
                self.assertFalse(
                    set(sector["active_edge_ids"]) & set(sector["pinched_edge_ids"])
                )

    def test_eight_standard_ibp_generators_and_exact_denominator_derivatives(self) -> None:
        expected = {(loop, vector) for loop in LOOP_VECTORS for vector in IBP_DOT_VECTORS}
        for family in self.families:
            generators = family["ibp_generators"]
            self.assertEqual(len(generators), 8)
            self.assertEqual(
                {(item["derivative_loop"], item["dot_vector"]) for item in generators},
                expected,
            )
            for generator in generators:
                for derivative in generator["denominator_directional_derivatives"]:
                    self.assertTrue(derivative["exact_match"])
                    self.assertEqual(
                        derivative["by_quadratic_form"]["polynomial_hash"],
                        derivative["by_routed_vector"]["polynomial_hash"],
                    )

    def test_polynomial_leibniz_derivative_is_fully_expanded(self) -> None:
        numerator = polynomial(((1, {"k2": 1, "kl": 1}),))
        derivative = directional_derivative_polynomial(numerator, "k", "p1")
        expected = polynomial(
            ((2, {"kp1": 1, "kl": 1}), (1, {"k2": 1, "lp1": 1}))
        )
        self.assertEqual(derivative["polynomial_hash"], expected["polynomial_hash"])
        self.assertEqual(render_polynomial(derivative), render_polynomial(expected))
        self.assertTrue(
            polynomial_is_zero(
                directional_derivative_polynomial(variable_polynomial("p1sq"), "k", "l")
            )
        )

    def test_direct_routed_denominator_derivative_has_exact_signs(self) -> None:
        derivative = direct_denominator_derivative((0, 1, -1, 0), "l", "p1")
        expected = polynomial(((2, {"lp1": 1}), (-2, {"p1sq": 1})))
        self.assertEqual(derivative["polynomial_hash"], expected["polynomial_hash"])
        self.assertEqual(render_polynomial(derivative), "2*lp1-2*p1sq")

    def test_tensor_numerator_directional_derivative_is_exact_and_hat_typed(self) -> None:
        scalar = polynomial(((1, {"k2": 1}),))
        numerator = tensor_polynomial(((scalar, (("k", "mu"), ("l", "nu"))),))
        derivative = directional_derivative_numerator(numerator, "k", "p1")
        terms = {
            tuple((factor["vector"], factor["index"]) for factor in term["tensor_word"]): term[
                "scalar_polynomial"
            ]
            for term in derivative["terms"]
        }
        self.assertEqual(
            terms[(("k", "mu"), ("l", "nu"))]["polynomial_hash"],
            polynomial(((2, {"kp1": 1}),))["polynomial_hash"],
        )
        self.assertEqual(
            terms[(("p1", "mu"), ("l", "nu"))]["polynomial_hash"],
            scalar["polynomial_hash"],
        )
        for term in derivative["terms"]:
            for factor in term["tensor_word"]:
                self.assertEqual(factor["metric_type"], "hat_delta")
                self.assertEqual(
                    factor["index_space"], "DRED_ROUTED_MOMENTUM_HAT_SUBSPACE"
                )
        with self.assertRaises(ValueError):
            tensor_polynomial(
                (
                    (scalar, (("k", "mu"),)),
                    (scalar, (("l", "nu"),)),
                )
            )
        zero = directional_derivative_numerator(
            tensor_polynomial(((polynomial(((1, {}),)), (("p1", "mu"),)),)),
            "k",
            "l",
        )
        self.assertEqual(zero["free_indices"], ["mu"])
        self.assertEqual(zero["terms"], [])

    def test_general_integer_power_ibp_identity_has_exact_shifts(self) -> None:
        family = self.by_graph["G6_DIRECT_K4ME_I3_S3CUBED"]
        numerator = polynomial(((1, {}),))
        identity = instantiate_ibp_identity(family, "k", "p1", numerator)
        self.assertEqual(identity["general_power_domain"], "Z^number_of_denominators")
        self.assertEqual(
            [item["domain"] for item in identity["general_propagator_powers"]],
            ["Z"] * len(family["edge_order"]),
        )
        terms = identity["equation"]["left"]["terms"]
        self.assertFalse(any(item["term_role"] == "VECTOR_DIVERGENCE" for item in terms))
        self.assertFalse(
            any(item["term_role"] == "NUMERATOR_DIRECTIONAL_DERIVATIVE" for item in terms)
        )
        denominator_terms = [
            item for item in terms if item["term_role"] == "DENOMINATOR_LOG_DERIVATIVE"
        ]
        self.assertEqual({item["edge_id"] for item in denominator_terms}, {"e_CI", "e_CB", "e_BI"})
        for term in denominator_terms:
            self.assertEqual(sum(term["power_shift"].values()), 1)
            self.assertEqual(term["power_shift"][term["edge_id"]], 1)
            self.assertEqual(term["coefficient_ast"]["op"], "negative_power_symbol")

    def test_polynomial_schema_rejects_epsilon_unknown_variables_and_negative_powers(self) -> None:
        with self.assertRaises(ValueError):
            polynomial(((1, {"epsilon": 1}),))
        with self.assertRaises(ValueError):
            polynomial(((1, {"k2": -1}),))
        malformed = variable_polynomial("k2")
        malformed["coefficient_domain"] = "Q(epsilon)"
        with self.assertRaises(ValueError):
            directional_derivative_polynomial(malformed, "k", "k")
        exact = polynomial(((Fraction(7, 11), {"kp2": 3}),))
        self.assertEqual(exact["terms"][0]["coefficient"], {"numerator": 7, "denominator": 11})

    def test_metric_measure_offshell_and_ir_contracts_are_separate(self) -> None:
        dred = self.bundle["dred_integral_contract"]
        metrics = dred["metric_types"]
        self.assertEqual(dred["measure"]["two_loop"], TWO_LOOP_MEASURE)
        self.assertEqual(metrics["spin_dalgebra_metric"], "delta_(4)")
        self.assertEqual(metrics["loop_integral_metric"], "hat_delta")
        self.assertEqual(metrics["evanescent_metric"], "tilde_delta=delta_(4)-hat_delta")
        self.assertTrue(metrics["pairwise_distinct_types"])
        self.assertEqual(dred["bare_numerator_epsilon_status"], "FORBIDDEN")
        domain = self.bundle["external_kinematic_domain"]
        self.assertEqual(
            render_polynomial(domain["definitions"]["Psq"]),
            "p1sq+p2sq+2*p1p2",
        )
        self.assertEqual(
            render_polynomial(domain["definitions"]["Gram_p1_p2"]),
            "p1sq*p2sq-p1p2^2",
        )
        self.assertTrue(domain["ir_pole_status"].startswith("UNKNOWN_"))

    def test_ibp_certificate_gates_refuse_every_uncomputed_output(self) -> None:
        self.assertFalse(self.bundle["external_target_used_as_input"])
        for family, certificate in zip(self.families, self.bundle["ibp_certificates"]):
            self.assertEqual(certificate["source_graph_hash"], family["source_graph_hash"])
            self.assertEqual(
                certificate["source_forest_record_hash"], family["source_forest_record_hash"]
            )
            self.assertIsNotNone(family["source_forest_record_hash"])
            self.assertEqual(certificate["integral_family_hash"], family["integral_family_hash"])
            self.assertEqual(
                certificate["compiled_dword_numerator"]["status"],
                "BLOCKED_COMPILED_DWORD_NUMERATOR_ABSENT",
            )
            self.assertEqual(certificate["master_laurent_contract"]["status"], "UNCOMPUTED_FAIL_CLOSED")
            self.assertTrue(all(value is None for value in certificate["outputs"].values()))
            self.assertTrue(certificate["gates"]["master_basis"].startswith("BLOCKED_"))
            self.assertTrue(certificate["gates"]["laurent_depth"].startswith("BLOCKED_"))
        self.assertTrue(
            all(
                value is None
                for key, value in self.bundle["global_fail_closed"].items()
                if key != "status"
            )
        )

    def test_generated_artifacts_and_audit_read_back(self) -> None:
        generated = ROOT / "generated" / "step6" / "two-loop-integrals"
        for name in (
            "two-loop-integrals.json",
            "integral-families.json",
            "ibp-certificates.json",
            "two-loop-integrals.md",
        ):
            self.assertTrue((generated / name).exists(), name)
        payload = json.loads((generated / "two-loop-integrals.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["bundle_hash"], self.bundle["bundle_hash"])
        audit = json.loads(
            (ROOT / "audits" / "step6-two-loop-integrals-verification.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["failure_count"], 0)
        rebuilt = build_audit(self.bundle)
        self.assertEqual(rebuilt["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
