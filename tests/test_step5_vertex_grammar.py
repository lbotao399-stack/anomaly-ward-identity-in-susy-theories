from __future__ import annotations

from fractions import Fraction
import unittest

from scripts.step5_graph_ir import Chirality, IndexSpace, Statistics, Variance
from scripts.step5_vertex_grammar import (
    ActionMonomial,
    CensusContractionRule,
    CompositeKind,
    DerivativeRequest,
    ExactCoefficient,
    FieldOccurrence,
    GrammarStatus,
    build_project_vertex_grammar,
    census_one_loop_candidates,
    chiral_cubic_monomials,
    connection_expansion,
    field_strength_expansion,
    fp_ghost_monomials,
    fp_ghost_typed_zeros,
    gauge_kinetic_monomials,
    matter_bridge_monomials,
    ordered_functional_derivative,
    prepotential_euler_insertion_terms,
)


class Step5VertexGrammarTest(unittest.TestCase):
    def test_exact_coefficient_normalizes_i_and_sqrt2_without_float(self) -> None:
        coefficient = ExactCoefficient(Fraction(1, 3), sqrt2_power=3, i_power=3, symbols=("h",))
        self.assertEqual(coefficient.rational, Fraction(-2, 3))
        self.assertEqual(coefficient.sqrt2_power, 1)
        self.assertEqual(coefficient.i_power, 1)
        self.assertEqual(coefficient.render(), "-2/3*sqrt(2)*i*h")
        product = ExactCoefficient(Fraction(1, 2), i_power=1) * ExactCoefficient(
            Fraction(1, 3), i_power=1
        )
        self.assertEqual(product, ExactCoefficient(Fraction(-1, 6)))

    def test_matter_bridge_is_exactly_expanded_through_v_squared(self) -> None:
        monomials = matter_bridge_monomials()
        self.assertEqual(len(monomials), 3)
        self.assertEqual([len(item.ordered_fields) for item in monomials], [2, 3, 4])
        self.assertEqual(monomials[0].coefficient, ExactCoefficient(-1, symbols=("h",)))
        self.assertEqual(monomials[0].color_word, ("kappa[A,B]", "delta[B,C]"))
        self.assertEqual(monomials[1].coefficient, ExactCoefficient(-1, i_power=1, symbols=("h",)))
        self.assertEqual(monomials[2].coefficient, ExactCoefficient(Fraction(1, 2), symbols=("h",)))
        self.assertEqual(
            [item.field_name for item in monomials[2].ordered_fields],
            ["TildePhi", "V", "V", "Phi"],
        )
        self.assertEqual(monomials[2].color_word[-2:], ("c[D,E,B]", "c[F,C,E]"))

    def test_euclidean_superpotential_sign_and_coefficient_follow_4c4_4c13(self) -> None:
        chiral, tilded = chiral_cubic_monomials()
        expected = ExactCoefficient(Fraction(1, 6), sqrt2_power=1, symbols=("h",))
        self.assertEqual(chiral.coefficient, expected)
        self.assertEqual(tilded.coefficient, expected)
        self.assertEqual(chiral.measure, "E,+")
        self.assertEqual(tilded.measure, "E,-")
        self.assertEqual(chiral.color_word, ("epsilon[r,s,t]", "c[A,B,C]"))

    def test_gamma_bch_and_field_strength_coefficients_through_v_cubed(self) -> None:
        gamma = connection_expansion(CompositeKind.GAMMA)
        tilde_gamma = connection_expansion(CompositeKind.TILDE_GAMMA)
        self.assertEqual(
            [item.coefficient for item in gamma],
            [
                ExactCoefficient(1),
                ExactCoefficient(Fraction(-1, 2), i_power=1),
                ExactCoefficient(Fraction(1, 6), i_power=2),
            ],
        )
        self.assertEqual(
            [item.coefficient for item in tilde_gamma],
            [
                ExactCoefficient(-1),
                ExactCoefficient(Fraction(-1, 2), i_power=1),
                ExactCoefficient(Fraction(-1, 6), i_power=2),
            ],
        )
        w = field_strength_expansion(CompositeKind.W)
        tilde_w = field_strength_expansion(CompositeKind.TILDE_W)
        self.assertEqual(
            [item.coefficient for item in w],
            [ExactCoefficient(Fraction(-1, 8)), ExactCoefficient(Fraction(1, 16), i_power=1), ExactCoefficient(Fraction(1, 48))],
        )
        self.assertEqual(
            [item.coefficient for item in tilde_w],
            [ExactCoefficient(Fraction(-1, 8)), ExactCoefficient(Fraction(-1, 16), i_power=1), ExactCoefficient(Fraction(1, 48))],
        )
        self.assertEqual(w[2].color_word, ("c[A2,A3,M1]", "c[A1,M1,X]"))
        self.assertEqual(w[2].derivative_scopes[0].operators, ("barD^2",))
        self.assertEqual(tilde_w[2].derivative_scopes[0].operators, ("D^2",))

    def test_gauge_kinetic_action_contains_every_ordered_pair_through_quartic(self) -> None:
        monomials = gauge_kinetic_monomials()
        chiral = [item for item in monomials if item.sector == "GAUGE_KINETIC_W"]
        tilded = [item for item in monomials if item.sector == "GAUGE_KINETIC_TILDE_W"]
        self.assertEqual(len(chiral), 6)
        self.assertEqual(len(tilded), 6)
        self.assertEqual(sorted(len(item.ordered_fields) for item in chiral), [2, 3, 3, 4, 4, 4])
        quadratic = next(item for item in chiral if len(item.ordered_fields) == 2)
        self.assertEqual(quadratic.coefficient, ExactCoefficient(Fraction(-1, 256), symbols=("h",)))
        self.assertEqual(quadratic.color_word[-1], "kappa[X,Y]")
        self.assertEqual(len(quadratic.derivative_scopes), 2)
        self.assertEqual(len(quadratic.spinor_contractions), 1)
        contraction = quadratic.spinor_contractions[0]
        self.assertEqual(contraction.index_space, IndexSpace.UNDOTTED)
        self.assertEqual(contraction.left_variance, Variance.UP)
        self.assertEqual(contraction.right_variance, Variance.DOWN)
        self.assertEqual(
            [item.direct_derivatives for item in quadratic.ordered_fields],
            [("D_a_up",), ("D_a_down",)],
        )
        tilde_quadratic = next(item for item in tilded if len(item.ordered_fields) == 2)
        self.assertEqual(tilde_quadratic.spinor_contractions[0].index_space, IndexSpace.DOTTED)
        self.assertEqual(tilde_quadratic.spinor_contractions[0].left_variance, Variance.DOWN)
        self.assertEqual(tilde_quadratic.spinor_contractions[0].right_variance, Variance.UP)
        self.assertEqual(
            [item.direct_derivatives for item in tilde_quadratic.ordered_fields],
            [("barD_dot_a_down",), ("barD_dot_a_up",)],
        )

    def test_prepotential_euler_insertion_is_the_exact_5_28_series(self) -> None:
        terms = prepotential_euler_insertion_terms()
        self.assertEqual(len(terms), 4)
        self.assertEqual(
            [item.coefficient for item in terms],
            [
                ExactCoefficient(1),
                ExactCoefficient(Fraction(1, 2), i_power=1),
                ExactCoefficient(Fraction(1, 6), i_power=2),
                ExactCoefficient(Fraction(1, 24), i_power=3),
            ],
        )
        self.assertEqual([len(item.ordered_fields) for item in terms], [1, 2, 3, 4])
        self.assertTrue(all(item.ordered_fields[-1].field_name == "E_Xi" for item in terms))
        self.assertTrue(all(item.source_equations == ("5.26", "5.28") for item in terms))

    def test_fp_ghost_normalization_is_derived_and_not_blocked(self) -> None:
        monomials = fp_ghost_monomials()
        self.assertEqual(len(monomials), 10)
        self.assertTrue(all(item.status is GrammarStatus.PROVED_FROM_PROJECT for item in monomials))
        self.assertTrue(all(item.source_equations == ("3D.84", "3D.86", "3D.90", "3D.91") for item in monomials))
        plus_tilde_v0 = next(item for item in monomials if item.monomial_id == "fp_plus_tilde_c_v0")
        plus_tilde_v1 = next(item for item in monomials if item.monomial_id == "fp_plus_tilde_c_v1")
        self.assertEqual(plus_tilde_v0.coefficient, ExactCoefficient(Fraction(1, 4), i_power=1))
        self.assertEqual(plus_tilde_v1.coefficient, ExactCoefficient(Fraction(1, 8)))
        self.assertEqual(plus_tilde_v0.derivative_scopes[0].operators, ("barNabla_B^2",))
        self.assertNotIn("fp_plus_c_v0", {item.monomial_id for item in monomials})
        self.assertNotIn("fp_minus_tilde_c_v0", {item.monomial_id for item in monomials})
        zeros = fp_ghost_typed_zeros()
        self.assertEqual(
            {item.monomial_id for item in zeros},
            {"fp_plus_c_v0", "fp_minus_tilde_c_v0"},
        )
        self.assertTrue(all("chirality" in item.zero_reason for item in zeros))
        bundle = build_project_vertex_grammar()
        self.assertEqual(bundle.ghost_status, GrammarStatus.PROVED_FROM_PROJECT)
        self.assertEqual(bundle.insertion_chart_status, GrammarStatus.PROVED_FROM_PROJECT)
        self.assertEqual(
            bundle.insertion_core_status,
            GrammarStatus.BLOCKED_UNINSTANTIATED_E_XI_CORE,
        )
        self.assertEqual(bundle.blockers, ("BLOCKED_UNINSTANTIATED_E_XI_CORE",))
        self.assertEqual(len(bundle.action_monomials), 27)
        self.assertEqual(len(bundle.insertion_monomials), 4)
        self.assertEqual(len(bundle.action_vertices), 27)
        self.assertEqual(len(bundle.insertion_vertices), 4)
        self.assertEqual(bundle.typed_zero_monomials, zeros)
        cubic_vertex = next(
            vertex for vertex in bundle.action_vertices if vertex.source_monomial_id == "n4_chiral_cubic"
        )
        self.assertEqual(len(cubic_vertex.terms), 6)
        self.assertEqual(len({term.permutation_id for term in cubic_vertex.terms}), 6)

    def test_typed_spinor_contraction_and_quadratic_hessian_regression(self) -> None:
        bundle = build_project_vertex_grammar()
        monomial = next(
            item
            for item in bundle.action_monomials
            if item.monomial_id == "gauge_kinetic_w_v1_1"
        )
        vertex = next(
            item
            for item in bundle.action_vertices
            if item.source_monomial_id == monomial.monomial_id
        )
        self.assertEqual(len(monomial.spinor_contractions), 1)
        self.assertEqual(vertex.spinor_contractions, monomial.spinor_contractions)
        self.assertEqual(len(vertex.terms), 2)
        self.assertEqual(
            {term.permutation_id for term in vertex.terms},
            {
                (monomial.ordered_fields[0].occurrence_id, monomial.ordered_fields[1].occurrence_id),
                (monomial.ordered_fields[1].occurrence_id, monomial.ordered_fields[0].occurrence_id),
            },
        )
        summed = sum((term.coefficient.rational for term in vertex.terms), Fraction(0))
        self.assertEqual(summed, Fraction(-1, 128))
        self.assertTrue(all(term.coefficient.symbols == ("h",) for term in vertex.terms))

    def test_ordered_functional_derivative_retains_all_identical_leg_permutations(self) -> None:
        chiral = chiral_cubic_monomials()[0]
        vertex = ordered_functional_derivative(
            chiral,
            (
                DerivativeRequest("Phi", "leg1"),
                DerivativeRequest("Phi", "leg2"),
                DerivativeRequest("Phi", "leg3"),
            ),
        )
        self.assertEqual(len(vertex.terms), 6)
        self.assertEqual(len({term.permutation_id for term in vertex.terms}), 6)
        self.assertTrue(all(term.koszul_sign == 1 for term in vertex.terms))
        self.assertTrue(all(term.coefficient == chiral.coefficient for term in vertex.terms))
        self.assertTrue(all(term.remaining_fields == () for term in vertex.terms))

    def test_ordered_left_derivative_records_fermionic_koszul_sign(self) -> None:
        odd = lambda occurrence_id: FieldOccurrence(
            occurrence_id,
            "ghost",
            Statistics.FERMION,
            Chirality.CHIRAL,
            occurrence_id.upper(),
        )
        monomial = ActionMonomial(
            "ghost_word",
            "TEST",
            "E,+",
            ExactCoefficient(1),
            (odd("g1"), odd("g2")),
            ("kappa[G1,G2]",),
            source_equations=("3D.90",),
        )
        vertex = ordered_functional_derivative(monomial, (DerivativeRequest("ghost", "leg"),))
        signs = {term.permutation_id: term.koszul_sign for term in vertex.terms}
        self.assertEqual(signs[("g1",)], 1)
        self.assertEqual(signs[("g2",)], -1)

    def test_one_loop_census_exhaustively_emits_labelled_triangle_candidates(self) -> None:
        def x(occurrence_id: str) -> FieldOccurrence:
            return FieldOccurrence(
                occurrence_id,
                "X",
                Statistics.BOSON,
                Chirality.UNCONSTRAINED,
                occurrence_id.upper(),
            )

        insertion = ActionMonomial(
            "I2",
            "TEST_INSERTION",
            "E,8",
            ExactCoefficient(1),
            (x("i1"), x("i2")),
            ("delta",),
            source_equations=("5.28",),
        )
        cubic = ActionMonomial(
            "A3",
            "TEST_ACTION",
            "E,8",
            ExactCoefficient(1),
            (x("a1"), x("a2"), x("a3")),
            ("tensor",),
            source_equations=("4C.4",),
        )
        census = census_one_loop_candidates(
            (insertion,),
            (cubic,),
            (CensusContractionRule("XX", "X", "X"),),
            ("X", "X"),
            min_action_vertices=2,
            max_action_vertices=2,
        )
        self.assertGreater(len(census.candidates), 0)
        self.assertTrue(all(candidate.connected for candidate in census.candidates))
        self.assertTrue(all(candidate.loop_number == 1 for candidate in census.candidates))
        self.assertTrue(all(candidate.topology == "TRIANGLE" for candidate in census.candidates))
        self.assertEqual(
            [candidate.candidate_id for candidate in census.candidates],
            [f"candidate_{position:06d}" for position in range(len(census.candidates))],
        )
        signatures = [
            (
                candidate.action_monomial_ids,
                candidate.external_assignment,
                tuple(
                    (pair.left_occurrence, pair.right_occurrence, pair.rule_id)
                    for pair in candidate.internal_pairs
                ),
            )
            for candidate in census.candidates
        ]
        self.assertEqual(signatures, sorted(signatures))

    def test_bundle_contains_no_anomaly_coefficient(self) -> None:
        bundle = build_project_vertex_grammar()
        coefficient_symbols = {
            symbol
            for monomial in bundle.action_monomials + bundle.insertion_monomials
            for symbol in monomial.coefficient.symbols
        }
        self.assertEqual(coefficient_symbols, {"h"})
        self.assertTrue(all("anomaly" not in monomial.monomial_id.lower() for monomial in bundle.action_monomials))


if __name__ == "__main__":
    unittest.main()
