from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import step6_dred_reducer as dred


def vector(name: str, variance: dred.Variance = dred.Variance.UPPER) -> dred.TensorIndex:
    return dred.TensorIndex(name, dred.IndexSpace.VECTOR_4, variance)


def external(names=("m", "n")) -> dred.ExternalOperatorTensor:
    return dred.ExternalOperatorTensor(
        "O_WW",
        tuple(vector(name, dred.Variance.LOWER) for name in names),
        {"op": "O_WW", "ordered_indices": list(names), "colors": ["A", "B"]},
        "UNIT_TEST_DERIVATION",
    )


def rank2_bare() -> dred.BareTensorNumerator:
    m, n = vector("m"), vector("n")
    q = dred.MomentumVector("q", dred.MomentumRole.CENTERED_LOOP)
    return dred.BareTensorNumerator(
        "N2",
        external(),
        (dred.MomentumFactor(q, m), dred.MomentumFactor(q, n)),
        dred.ExactCoefficient(1, Fraction(1, 7), (dred.ScalarAtom("C"),)),
        dred.ScalarAtom("I_q2"),
        (),
        "G2",
    )


class Step6DREDReducerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.audit = dred.write_outputs()

    def test_audit_passes(self):
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["totals"]["failed"], 0)
        self.assertGreaterEqual(self.audit["totals"]["checks"], 12)

    def test_rank2_averaging_is_hat_over_exact_d(self):
        row = dred.rank2_average(rank2_bare())
        term = row["terms"][0]
        self.assertEqual(term["metric_product"][0]["kind"], "hat_delta")
        self.assertEqual(term["metric_product"][0]["stage"], "LOOP_TENSOR_AVERAGING")
        self.assertEqual(term["coefficient"]["denominator_factors"], ["d"])
        self.assertFalse(term["coefficient"]["epsilon_expansion_performed"])
        self.assertEqual(dred.rank2_coefficient_exact(Fraction(7, 3)), Fraction(3, 7))

    def test_rank2_preserves_external_operator_tensor_exactly(self):
        bare = rank2_bare()
        row = dred.rank2_average(bare)
        self.assertEqual(
            row["external_operator_tensor"], bare.external_tensor.as_json()
        )
        self.assertEqual(
            row["external_operator_tensor_preserved_sha256"],
            bare.external_tensor.identity_sha256,
        )

    def test_rank4_generic_linear_system_and_pairings(self):
        m, n, r, s = (vector(name) for name in ("m", "n", "r", "s"))
        q = dred.MomentumVector("q", dred.MomentumRole.CENTERED_LOOP)
        bare = dred.BareTensorNumerator(
            "N4",
            external(("m", "n", "r", "s")),
            tuple(dred.MomentumFactor(q, index) for index in (m, n, r, s)),
            dred.ExactCoefficient(),
            dred.ScalarAtom("I4"),
            (),
            "G4",
        )
        contractions = dred.Rank4Contractions(
            dred.ScalarAtom("X"), dred.ScalarAtom("Y"), dred.ScalarAtom("Z")
        )
        row = dred.rank4_average(bare, contractions)
        self.assertEqual([term["channel"] for term in row["terms"]], ["A", "B", "C"])
        self.assertEqual(
            [
                [(metric["indices"][0]["name"], metric["indices"][1]["name"]) for metric in term["metric_product"]]
                for term in row["terms"]
            ],
            [[("m", "n"), ("r", "s")], [("m", "r"), ("n", "s")], [("m", "s"), ("n", "r")]],
        )
        self.assertEqual(
            row["terms"][0]["coefficient"]["numerator_terms"],
            [
                {"dimension_factor": "d+1", "scalar_moment": {"name": "X", "kind": "PHYSICAL"}},
                {"dimension_factor": "-1", "scalar_moment": {"name": "Y", "kind": "PHYSICAL"}},
                {"dimension_factor": "-1", "scalar_moment": {"name": "Z", "kind": "PHYSICAL"}},
            ],
        )

        d = Fraction(7, 2)
        X, Y, Z = Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13)
        A, B, C = dred.rank4_coefficients_exact(d, X, Y, Z)
        self.assertEqual(d * d * A + d * B + d * C, X)
        self.assertEqual(d * A + d * d * B + d * C, Y)
        self.assertEqual(d * A + d * B + d * d * C, Z)

    def test_rank4_identical_specialization_has_d_dplus2(self):
        fixture = self.payload["fixtures"]["rank4_identical_average"]
        self.assertEqual(len(fixture["terms"]), 3)
        for term in fixture["terms"]:
            self.assertEqual(term["coefficient"]["denominator_factors"], ["d", "d+2"])
            self.assertEqual([metric["kind"] for metric in term["metric_product"]], ["hat_delta", "hat_delta"])

    def test_bare_regulator_atom_is_rejected(self):
        bare = rank2_bare()
        with self.assertRaises(dred.BareNumeratorError):
            dred.BareTensorNumerator(
                bare.numerator_id,
                bare.external_tensor,
                bare.momentum_factors,
                dred.ExactCoefficient(
                    atoms=(dred.ScalarAtom("epsilon_DRED", dred.ScalarAtomKind.DRED_REGULATOR),)
                ),
                bare.radial_scalar_moment,
                (),
                bare.source_graph_id,
            )

    def test_mislabeled_dred_scalar_and_untyped_external_token_are_rejected(self):
        for name in ("d", "epsilon", "epsilon_DRED", "4-2*epsilon"):
            with self.subTest(name=name):
                with self.assertRaises(dred.BareNumeratorError):
                    dred.ScalarAtom(name, dred.ScalarAtomKind.PHYSICAL)
        with self.assertRaises(dred.BareNumeratorError):
            dred.ExternalOperatorTensor(
                "bad",
                (),
                {"op": "multiply", "factor": "epsilon_DRED"},
                "UNIT_TEST",
            )

    def test_spinor_epsilon_inside_typed_external_ast_is_not_dred_epsilon(self):
        ext = dred.ExternalOperatorTensor(
            "spinor_tensor",
            (),
            {"op": "epsilon_spinor", "indices": ["a", "b"]},
            "UNIT_TEST",
        )
        self.assertIn("epsilon_spinor", dred.canonical_json(ext.as_json()))

    def test_metric_stage_ownership_fails_closed(self):
        m, n = vector("m"), vector("n")
        illegal = (
            (dred.MetricKind.HAT, dred.MetricStage.SPIN_DALGEBRA),
            (dred.MetricKind.DELTA4, dred.MetricStage.LOOP_TENSOR_AVERAGING),
            (dred.MetricKind.TILDE, dred.MetricStage.LOOP_TENSOR_AVERAGING),
        )
        for kind, stage in illegal:
            with self.subTest(kind=kind, stage=stage):
                with self.assertRaises(dred.MetricProvenanceError):
                    dred.MetricTensor(kind, (m, n), stage, "bad", "bad")

    def test_spinor_vector_index_mixing_fails_closed(self):
        m = vector("m")
        a = dred.TensorIndex("a", dred.IndexSpace.SPINOR_UNDOTTED, dred.Variance.UPPER)
        q = dred.MomentumVector("q", dred.MomentumRole.CENTERED_LOOP)
        with self.assertRaises(dred.TypeSpaceError):
            dred.MomentumFactor(q, a)
        with self.assertRaises(dred.TypeSpaceError):
            dred.MetricTensor(
                dred.MetricKind.DELTA4,
                (a, m),
                dred.MetricStage.SPIN_DALGEBRA,
                "bad",
                "bad",
            )

    def test_momentum_outside_regulated_hat_space_fails_closed(self):
        with self.assertRaises(dred.TypeSpaceError):
            dred.MomentumVector(
                "q",
                dred.MomentumRole.CENTERED_LOOP,
                dred.MomentumSupport.FOUR_SPIN,
            )

    def _contact_terms(self):
        m, n = vector("m"), vector("n")
        ext = external()
        coefficient = dred.ExactCoefficient(atoms=(dred.ScalarAtom("C"),))
        triangle = dred.IndependentMetricTerm(
            "triangle",
            "G_triangle",
            dred.digest({"independent": "triangle"}),
            coefficient,
            dred.MetricTensor(
                dred.MetricKind.HAT,
                (m, n),
                dred.MetricStage.LOOP_TENSOR_AVERAGING,
                "triangle",
                "CENTERED_HAT_SPACE_ISOTROPIC_AVERAGE",
            ),
            ext,
        )
        contact = dred.IndependentMetricTerm(
            "contact",
            "G_contact",
            dred.digest({"independent": "contact"}),
            coefficient.negated(),
            dred.MetricTensor(
                dred.MetricKind.DELTA4,
                (m, n),
                dred.MetricStage.CONTACT_DALGEBRA,
                "contact",
                "INDEPENDENT_SD_CONTACT_DALGEBRA",
            ),
            ext,
            "SD_COMPLETE_CONTACT_FAMILY",
        )
        return triangle, contact

    def test_contact_subtraction_is_only_tilde_constructor(self):
        triangle, contact = self._contact_terms()
        row = dred.validated_contact_subtraction(triangle, contact)
        self.assertEqual(row["result"]["coefficient"]["sign"], -1)
        self.assertEqual(row["result"]["metric"]["kind"], "tilde_delta")
        self.assertEqual(
            row["result"]["metric"]["proof_sha256"], row["proof_sha256"]
        )
        self.assertFalse(row["epsilon_trace_applied"])

    def test_incomplete_contact_census_is_rejected(self):
        triangle, contact = self._contact_terms()
        bad = dred.IndependentMetricTerm(
            contact.term_id,
            contact.source_graph_id,
            contact.derivation_sha256,
            contact.coefficient,
            contact.metric,
            contact.external_tensor,
            None,
        )
        with self.assertRaises(dred.ContactSubtractionError):
            dred.validated_contact_subtraction(triangle, bad)

    def test_changed_external_tensor_is_rejected(self):
        triangle, contact = self._contact_terms()
        changed = dred.IndependentMetricTerm(
            contact.term_id,
            contact.source_graph_id,
            contact.derivation_sha256,
            contact.coefficient,
            contact.metric,
            dred.ExternalOperatorTensor(
                "O_changed",
                contact.external_tensor.ordered_indices,
                {"op": "changed"},
                "UNIT_TEST",
            ),
            contact.contact_census_status,
        )
        with self.assertRaises(dred.ContactSubtractionError):
            dred.validated_contact_subtraction(triangle, changed)

    def test_wrong_contact_sign_and_magnitude_are_rejected(self):
        triangle, contact = self._contact_terms()
        for coefficient in (
            dred.ExactCoefficient(atoms=(dred.ScalarAtom("C"),)),
            dred.ExactCoefficient(-1, Fraction(2, 1), (dred.ScalarAtom("C"),)),
        ):
            changed = dred.IndependentMetricTerm(
                contact.term_id,
                contact.source_graph_id,
                contact.derivation_sha256,
                coefficient,
                contact.metric,
                contact.external_tensor,
                contact.contact_census_status,
            )
            with self.subTest(coefficient=coefficient):
                with self.assertRaises(dred.ContactSubtractionError):
                    dred.validated_contact_subtraction(triangle, changed)

    def test_same_derivation_source_is_rejected(self):
        triangle, contact = self._contact_terms()
        changed = dred.IndependentMetricTerm(
            contact.term_id,
            triangle.source_graph_id,
            triangle.derivation_sha256,
            contact.coefficient,
            contact.metric,
            contact.external_tensor,
            contact.contact_census_status,
        )
        with self.assertRaises(dred.ContactSubtractionError):
            dred.validated_contact_subtraction(triangle, changed)

    def test_metric_traces_are_audit_only_and_exact(self):
        self.assertEqual(dred.metric_trace(dred.MetricKind.DELTA4)["expression"], "4")
        self.assertEqual(dred.metric_trace(dred.MetricKind.HAT)["expression"], "d")
        self.assertEqual(
            dred.metric_trace(dred.MetricKind.TILDE)["expression"],
            "2*epsilon_DRED",
        )
        self.assertTrue(
            all(
                not dred.metric_trace(kind)["bare_numerator_mutated"]
                for kind in dred.MetricKind
            )
        )

    def test_output_contains_no_master_or_uv_result(self):
        terminal = self.payload["terminal_blocks"]
        self.assertIsNone(terminal["master_integrals"])
        self.assertIsNone(terminal["UV_poles"])
        self.assertIsNone(terminal["renormalized_coefficients"])
        self.assertIsNone(terminal["external_target_comparison"])


if __name__ == "__main__":
    unittest.main()
