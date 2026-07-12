from __future__ import annotations

import json
import unittest
from dataclasses import replace
from fractions import Fraction

from scripts.step5_graph_ir import (
    AllowedContraction,
    Chirality,
    DAlgebraBranch,
    DAlgebraEngine,
    DAlgebraFactor,
    DescendantCoefficient,
    DescendantNodeType,
    DerivativeKind,
    DerivativeToken,
    ExternalLeg,
    FactorRole,
    FieldType,
    Flow,
    GraphIR,
    HalfEdge,
    IndexSlot,
    IndexSpace,
    InternalEdge,
    LetterFamily,
    PropagatorGrammar,
    Statistics,
    Variance,
    Vertex,
    canonical_channel_catalog_json,
    emit_ordered_family_channels,
    enumerate_wick_pairings,
)


def color(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.COLOR_ADJOINT, label, Variance.UP)


def undotted(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.UNDOTTED, label, Variance.DOWN)


def dotted(label: str) -> IndexSlot:
    return IndexSlot(IndexSpace.DOTTED, label, Variance.UP)


class Step5GraphIRTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phi = FieldType(
            "Phi",
            Statistics.BOSON,
            Chirality.CHIRAL,
            (color("A"),),
        )
        self.tilde_phi = FieldType(
            "TildePhi",
            Statistics.BOSON,
            Chirality.ANTICHIRAL,
            (color("B"),),
        )
        self.ghost = FieldType(
            "ghost",
            Statistics.FERMION,
            Chirality.CHIRAL,
            (color("C"),),
        )

    def _two_vertex_graph(self) -> GraphIR:
        half_edges = (
            HalfEdge("h0", "v0", 0, self.phi, Flow.OUT, "k0"),
            HalfEdge("h1", "v0", 1, self.tilde_phi, Flow.OUT, "p1"),
            HalfEdge("h2", "v1", 0, self.tilde_phi, Flow.IN, "-k0"),
            HalfEdge("h3", "v1", 1, self.phi, Flow.OUT, "p2"),
        )
        return GraphIR(
            graph_id="G_seed",
            vertices=(
                Vertex("v0", "ACTION_VERTEX", ("h0", "h1"), "V_0", ("A", "B"), "z0", "k0+p1"),
                Vertex("v1", "INSERTION_VERTEX", ("h2", "h3"), "I_0", ("B", "A"), "z1", "-k0+p2"),
            ),
            half_edges=half_edges,
            internal_edges=(InternalEdge("e0", "h0", "h2", "P_PhiTildePhi", "k0", Flow.OUT),),
            external_legs=(
                ExternalLeg("L1", "h1", self.tilde_phi, "p1", "B"),
                ExternalLeg("L2", "h3", self.phi, "p2", "A"),
            ),
            loop_momenta=(),
            metadata=(("symmetry_factor", "S_G_seed"), ("wick_sign", "+1")),
        )

    def test_graph_is_typed_and_canonical_serialization_is_deterministic(self) -> None:
        graph = self._two_vertex_graph()
        first = graph.canonical_json()
        second = graph.canonical_json()
        self.assertEqual(first, second)
        parsed = json.loads(first)
        self.assertEqual(parsed["half_edges"][0]["field_type"]["statistics"], "BOSON")
        self.assertEqual(parsed["external_legs"][0]["momentum"], "p1")
        self.assertEqual(parsed["loop_momenta"], [])

    def test_every_half_edge_must_terminate_exactly_once(self) -> None:
        graph = self._two_vertex_graph()
        with self.assertRaisesRegex(ValueError, "exactly once"):
            GraphIR(
                graph_id="bad",
                vertices=graph.vertices,
                half_edges=graph.half_edges,
                internal_edges=graph.internal_edges,
                external_legs=graph.external_legs + (
                    ExternalLeg("duplicate", "h1", self.tilde_phi, "p1", "B"),
                ),
            )

    def test_same_ir_emits_mermaid_dot_and_amplitude_skeleton(self) -> None:
        graph = self._two_vertex_graph()
        mermaid = graph.to_mermaid()
        dot = graph.to_dot()
        amplitude = graph.amplitude_skeleton()
        for vertex_id in ("v0", "v1"):
            self.assertIn(vertex_id, mermaid)
            self.assertIn(vertex_id, dot)
        self.assertIn("e0:P_PhiTildePhi(k0)", mermaid)
        self.assertIn("e0:P_PhiTildePhi(k0)", dot)
        self.assertIn("P_PhiTildePhi", amplitude)
        self.assertIn("V_0", amplitude)
        self.assertIn("I_0", amplitude)
        self.assertNotIn("1/(8", amplitude)
        self.assertNotIn("1/(16", amplitude)

    def test_half_edge_derivative_placement_survives_every_ir_emitter(self) -> None:
        graph = self._two_vertex_graph()
        derivative = DerivativeToken("D_edge", DerivativeKind.D, undotted("gamma"), "action:v0")
        half_edges = tuple(
            replace(half_edge, derivatives=(derivative,))
            if half_edge.half_edge_id == "h0"
            else half_edge
            for half_edge in graph.half_edges
        )
        dressed = replace(graph, half_edges=half_edges)
        expected = "h0{D[gamma]}"
        self.assertIn(expected, dressed.to_mermaid())
        self.assertIn(expected, dressed.to_dot())
        self.assertIn(expected, dressed.amplitude_skeleton())

    def test_collapsed_propagator_generates_valid_contact_child(self) -> None:
        graph = self._two_vertex_graph()
        self.assertEqual(graph.cycle_rank(), 0)
        self.assertNotIn("Integral[d^d", graph.amplitude_skeleton())
        child = graph.collapse_edge("e0")
        self.assertEqual(child.graph_id, "G_seed__collapse__e0")
        self.assertEqual(len(child.vertices), 1)
        self.assertEqual(child.vertices[0].kind, "CONTACT_CHILD")
        self.assertEqual(child.vertices[0].ordered_half_edges, ("h1", "h3"))
        self.assertEqual(child.internal_edges, ())
        self.assertEqual(dict(child.metadata)["parent_graph_id"], "G_seed")
        self.assertEqual(dict(child.metadata)["collapsed_edge_id"], "e0")
        self.assertEqual(child.cycle_rank(), 0)
        self.assertEqual(child.loop_momenta, ())
        self.assertEqual(dict(child.metadata)["loop_basis_rule"], "RECOMPUTE_BY_E_MINUS_V_PLUS_C")
        self.assertIn("ContactFrom[P_PhiTildePhi]", child.amplitude_skeleton())
        contact = child.vertices[0]
        expected_factors = (
            *graph.vertices[0].effective_coefficient_factors,
            *graph.vertices[1].effective_coefficient_factors,
            "ContactFrom[P_PhiTildePhi]",
        )
        self.assertEqual(contact.effective_coefficient_factors, expected_factors)
        self.assertEqual(
            contact.coefficient_symbol,
            "OrderedProduct[V_0,I_0,ContactFrom[P_PhiTildePhi]]",
        )
        amplitude = child.amplitude_skeleton()
        for factor in expected_factors:
            self.assertEqual(amplitude.count(factor), 1)

    def test_triangle_edge_collapse_preserves_one_loop_basis(self) -> None:
        half_edges = (
            HalfEdge("h01", "v0", 0, self.phi, Flow.NONE, "k0"),
            HalfEdge("h02", "v0", 1, self.phi, Flow.NONE, "k0+p0"),
            HalfEdge("h10", "v1", 0, self.phi, Flow.NONE, "-k0"),
            HalfEdge("h12", "v1", 1, self.phi, Flow.NONE, "k0+p1"),
            HalfEdge("h20", "v2", 0, self.phi, Flow.NONE, "-k0-p0"),
            HalfEdge("h21", "v2", 1, self.phi, Flow.NONE, "-k0-p1"),
        )
        graph = GraphIR(
            "triangle",
            (
                Vertex("v0", "ACTION", ("h01", "h02"), "V0", (), "z0", "delta0"),
                Vertex("v1", "ACTION", ("h10", "h12"), "V1", (), "z1", "delta1"),
                Vertex("v2", "INSERTION", ("h20", "h21"), "I", (), "z2", "delta2"),
            ),
            half_edges,
            (
                InternalEdge("e01", "h01", "h10", "P", "k0"),
                InternalEdge("e12", "h12", "h21", "P", "k0+p1"),
                InternalEdge("e20", "h20", "h02", "P", "k0+p0"),
            ),
            (),
            ("k0",),
        )
        self.assertEqual(graph.cycle_rank(), 1)
        child = graph.collapse_edge("e01")
        self.assertEqual(child.cycle_rank(), 1)
        self.assertEqual(child.loop_momenta, ("k0",))
        self.assertEqual(dict(child.metadata)["loop_basis_parent"], "k0")
        self.assertEqual(dict(child.metadata)["loop_basis_child"], "k0")
        self.assertIn("Integral[d^d k0]", child.amplitude_skeleton())

    def test_self_loop_collapse_removes_obsolete_loop_basis(self) -> None:
        half_edges = (
            HalfEdge("ha", "v0", 0, self.phi, Flow.NONE, "k0"),
            HalfEdge("hb", "v0", 1, self.phi, Flow.NONE, "-k0"),
        )
        graph = GraphIR(
            "tadpole",
            (Vertex("v0", "ACTION", ("ha", "hb"), "V", (), "z0", "delta0"),),
            half_edges,
            (InternalEdge("loop", "ha", "hb", "P", "k0"),),
            (),
            ("k0",),
        )
        routing = graph.validate_linear_momentum_routing()
        self.assertTrue(routing["passed"])
        self.assertTrue(routing["edge_checks"]["loop"]["endpoint_opposition"])
        self.assertTrue(routing["vertex_conservation"]["v0"])
        bad_half_edges = tuple(
            replace(half_edge, momentum="-k0+p1")
            if half_edge.half_edge_id == "hb"
            else half_edge
            for half_edge in graph.half_edges
        )
        bad = replace(graph, half_edges=bad_half_edges)
        self.assertFalse(bad.validate_linear_momentum_routing()["passed"])
        with self.assertRaisesRegex(ValueError, "momentum routing failed"):
            bad.assert_linear_momentum_routing()
        child = graph.collapse_edge("loop")
        self.assertEqual(child.cycle_rank(), 0)
        self.assertEqual(child.loop_momenta, ())
        self.assertNotIn("Integral[d^d k0]", child.amplitude_skeleton())

    def test_graph_rejects_loop_basis_not_equal_to_cycle_rank(self) -> None:
        graph = self._two_vertex_graph()
        with self.assertRaisesRegex(ValueError, r"E-V\+C"):
            replace(graph, loop_momenta=("spurious_k",))

    def test_deterministic_wick_pairings_keep_every_fermion_permutation(self) -> None:
        half_edges = tuple(
            HalfEdge(f"g{position}", f"v{position}", 0, self.ghost, Flow.NONE, f"q{position}")
            for position in range(4)
        )
        grammar = PropagatorGrammar(
            (AllowedContraction("ghost-line", "ghost", "ghost", "P_ghost", False),)
        )
        pairings = enumerate_wick_pairings(half_edges, grammar)
        self.assertEqual(len(pairings), 3)
        self.assertTrue(all(pairing.declared_field_word == ("g0", "g1", "g2", "g3") for pairing in pairings))
        self.assertEqual([pairing.koszul_sign for pairing in pairings], [1, -1, 1])
        self.assertEqual(
            [pairing.signature() for pairing in pairings],
            sorted(pairing.signature() for pairing in pairings),
        )
        self.assertEqual(
            [step.odd_factors_crossed for step in pairings[1].fermion_permutation],
            [1, 0],
        )

    def test_wick_koszul_sign_is_invariant_under_opaque_id_renaming(self) -> None:
        grammar = PropagatorGrammar(
            (AllowedContraction("ghost-line", "ghost", "ghost", "P_ghost", False),)
        )

        def pairing_by_positions(ids: tuple[str, ...]) -> dict[tuple[tuple[int, int], ...], int]:
            word = tuple(
                HalfEdge(opaque_id, f"v{position}", 0, self.ghost, Flow.NONE, f"q{position}")
                for position, opaque_id in enumerate(ids)
            )
            position_of = {opaque_id: position for position, opaque_id in enumerate(ids)}
            result: dict[tuple[tuple[int, int], ...], int] = {}
            for pairing in enumerate_wick_pairings(word, grammar):
                positional_pairs = tuple(
                    sorted(
                        tuple(sorted((position_of[pair.left_half_edge], position_of[pair.right_half_edge])))
                        for pair in pairing.pairs
                    )
                )
                result[positional_pairs] = pairing.koszul_sign
            return result

        original = pairing_by_positions(("a", "b", "c", "d"))
        renamed = pairing_by_positions(("zeta", "alpha", "mu", "beta"))
        self.assertEqual(original, renamed)
        self.assertEqual(
            original,
            {
                ((0, 1), (2, 3)): 1,
                ((0, 2), (1, 3)): -1,
                ((0, 3), (1, 2)): 1,
            },
        )

    def test_oriented_wick_rule_retains_field_orientation(self) -> None:
        half_edges = (
            HalfEdge("a", "v0", 0, self.tilde_phi, Flow.NONE, "q"),
            HalfEdge("b", "v1", 0, self.phi, Flow.NONE, "-q"),
        )
        grammar = PropagatorGrammar(
            (AllowedContraction("matter", "Phi", "TildePhi", "P_matter", True),)
        )
        pairing = enumerate_wick_pairings(half_edges, grammar)[0]
        self.assertEqual(pairing.pairs[0].left_half_edge, "b")
        self.assertEqual(pairing.pairs[0].right_half_edge, "a")

    def test_ibp_trace_has_exact_branches_signs_and_external_derivative_ledger(self) -> None:
        derivative = DerivativeToken("D0", DerivativeKind.D, undotted("alpha"), "vertex:v0")
        branch = DAlgebraBranch(
            coefficient=3,
            factors=(
                DAlgebraFactor("A", "A", 1, FactorRole.INTERNAL),
                DAlgebraFactor("B", "B", 0, FactorRole.INTERNAL, derivatives=(derivative,)),
                DAlgebraFactor("C", "C_ext", 0, FactorRole.EXTERNAL, external_leg_id="L1"),
            ),
        )
        engine = DAlgebraEngine()
        branches, trace = engine.integrate_by_parts(
            branch,
            source_factor_id="B",
            derivative_id="D0",
            step_id="IBP-001",
        )
        self.assertEqual([item.coefficient for item in branches], [3, -3])
        self.assertEqual(trace.koszul_sign, (1, -1))
        self.assertEqual(trace.assumptions, DAlgebraEngine.ASSUMPTIONS)
        self.assertEqual(branches[0].factors[0].derivatives, (derivative,))
        self.assertEqual(branches[1].factors[2].derivatives, (derivative,))
        self.assertEqual(branches[1].external_derivative_ledger[-1].external_leg_id, "L1")
        self.assertEqual(branches[1].external_derivative_ledger[-1].koszul_sign, -1)
        self.assertTrue(all(trace.invariants[key] for key in (
            "derivative_id_conservation",
            "factor_order_conservation",
            "total_parity_conservation",
            "external_leg_ledger_complete",
        )))
        payload = json.loads(trace.canonical_json())
        self.assertEqual(
            set(payload),
            {"step_id", "input", "rule", "assumptions", "koszul_sign", "output", "invariants"},
        )

    def test_bar_d_index_type_is_checked(self) -> None:
        token = DerivativeToken("BD0", DerivativeKind.BAR_D, dotted("dot_alpha"), "edge:e0")
        self.assertEqual(token.render(), "barD[dot_alpha]")
        with self.assertRaisesRegex(ValueError, "DOTTED"):
            DerivativeToken("bad", DerivativeKind.BAR_D, undotted("alpha"), "edge:e0")

    def test_bar_d_uses_the_same_lossless_ibp_trace(self) -> None:
        derivative = DerivativeToken("BD0", DerivativeKind.BAR_D, dotted("dot_alpha"), "edge:e0")
        branch = DAlgebraBranch(
            coefficient=1,
            factors=(
                DAlgebraFactor("source", "X", 0, FactorRole.INTERNAL, derivatives=(derivative,)),
                DAlgebraFactor("target", "Y_ext", 0, FactorRole.EXTERNAL, external_leg_id="L2"),
            ),
        )
        routed, trace = DAlgebraEngine().integrate_by_parts(
            branch,
            source_factor_id="source",
            derivative_id="BD0",
            step_id="IBP-BARD",
        )
        self.assertEqual(trace.koszul_sign, (-1,))
        self.assertEqual(routed[0].factors[1].derivatives, (derivative,))
        self.assertEqual(routed[0].external_derivative_ledger[0].external_leg_id, "L2")

    def test_external_derivative_ledger_is_applied_to_graph_without_loss(self) -> None:
        graph = self._two_vertex_graph()
        derivative = DerivativeToken("D0", DerivativeKind.D, undotted("alpha"), "vertex:v0")
        branch = DAlgebraBranch(
            coefficient=1,
            factors=(
                DAlgebraFactor("source", "X", 0, FactorRole.INTERNAL, derivatives=(derivative,)),
                DAlgebraFactor("external", "Phi_ext", 0, FactorRole.EXTERNAL, external_leg_id="L1"),
            ),
        )
        routed, _ = DAlgebraEngine().integrate_by_parts(
            branch,
            source_factor_id="source",
            derivative_id="D0",
            step_id="IBP-EXT",
        )
        updated = graph.with_external_derivatives_from_branch(routed[0])
        leg = next(leg for leg in updated.external_legs if leg.leg_id == "L1")
        self.assertEqual(tuple(token.op_id for token in leg.operator_derivatives), ("D0",))
        self.assertIn("D[alpha] TildePhi", updated.amplitude_skeleton())

    def test_ibp_rejects_moving_an_inner_derivative_without_a_commutation_trace(self) -> None:
        outer = DerivativeToken("D_outer", DerivativeKind.D, undotted("alpha"), "vertex:v0")
        inner = DerivativeToken("D_inner", DerivativeKind.D, undotted("beta"), "vertex:v0")
        branch = DAlgebraBranch(
            coefficient=1,
            factors=(
                DAlgebraFactor(
                    "source",
                    "X",
                    0,
                    FactorRole.INTERNAL,
                    derivatives=(outer, inner),
                ),
                DAlgebraFactor("target", "Y", 0, FactorRole.INTERNAL),
            ),
        )
        with self.assertRaisesRegex(ValueError, "outermost"):
            DAlgebraEngine().integrate_by_parts(
                branch,
                source_factor_id="source",
                derivative_id="D_inner",
                step_id="IBP-INNER-FORBIDDEN",
            )

    def test_ordered_family_emitter_has_sixteen_unquotiented_channels(self) -> None:
        channels = emit_ordered_family_channels()
        self.assertEqual(len(channels), 16)
        self.assertEqual([channel.ordinal for channel in channels], list(range(1, 17)))
        by_id = {channel.channel_id: channel for channel in channels}
        self.assertEqual(len(by_id), 16)
        self.assertIn("W__Phi", by_id)
        self.assertIn("Phi__W", by_id)
        self.assertEqual(by_id["W__Phi"].reverse_channel_id, "Phi__W")
        self.assertEqual(by_id["Phi__W"].reverse_channel_id, "W__Phi")
        self.assertNotEqual(
            by_id["W__Phi"].ordered_expression,
            by_id["W__Phi"].reversed_expression,
        )
        self.assertEqual(by_id["Phi__TildePhi"].left.flavor_label, "r")
        self.assertEqual(by_id["Phi__TildePhi"].right.flavor_label, "s")
        self.assertEqual(by_id["TildeW__W"].left.spinor_slots[0].space, IndexSpace.DOTTED)
        self.assertEqual(by_id["W__W"].left.color_label, "A")
        self.assertEqual(by_id["W__W"].right.color_label, "B")
        self.assertEqual(by_id["W__W"].left.family, LetterFamily.W)

    def test_sixteen_descendant_asts_expand_5_33_through_5_35_exactly(self) -> None:
        by_id = {channel.channel_id: channel for channel in emit_ordered_family_channels()}
        expected_term_counts = {
            "W__W": 4,
            "W__Phi": 4,
            "W__TildePhi": 2,
            "W__TildeW": 2,
            "Phi__W": 4,
            "Phi__Phi": 4,
            "Phi__TildePhi": 2,
            "Phi__TildeW": 2,
            "TildePhi__W": 2,
            "TildePhi__Phi": 2,
            "TildePhi__TildePhi": 0,
            "TildePhi__TildeW": 0,
            "TildeW__W": 2,
            "TildeW__Phi": 2,
            "TildeW__TildePhi": 0,
            "TildeW__TildeW": 0,
        }
        self.assertEqual(
            {channel_id: len(channel.descendant.terms) for channel_id, channel in by_id.items()},
            expected_term_counts,
        )
        self.assertTrue(by_id["TildePhi__TildePhi"].descendant.is_zero)
        self.assertTrue(by_id["TildeW__TildeW"].descendant.is_zero)

        phi_w = by_id["Phi__W"].descendant.terms
        self.assertEqual(
            [term.coefficient for term in phi_w],
            [
                DescendantCoefficient(Fraction(1, 2)),
                DescendantCoefficient(Fraction(-1), sqrt2_power=1),
                DescendantCoefficient(Fraction(1)),
                DescendantCoefficient(Fraction(2), i_power=1),
            ],
        )
        self.assertEqual([term.koszul_sign for term in phi_w], [1, 1, -1, -1])
        self.assertEqual(
            [term.intrinsic_coefficient for term in phi_w],
            [
                DescendantCoefficient(Fraction(1, 2)),
                DescendantCoefficient(Fraction(-1), sqrt2_power=1),
                DescendantCoefficient(Fraction(-1)),
                DescendantCoefficient(Fraction(-2), i_power=1),
            ],
        )
        for term in phi_w:
            canonical = term.canonical_dict()
            self.assertFalse(canonical["intrinsic_coefficient_includes_koszul_sign"])
            self.assertTrue(canonical["total_coefficient_includes_koszul_sign"])
            self.assertEqual(
                canonical["total_coefficient"],
                term.total_coefficient.canonical_dict(),
            )
            self.assertEqual(
                canonical["coefficient_schema"],
                "TOTAL_EQUALS_KOSZUL_SIGN_TIMES_INTRINSIC",
            )
        epsilon_factor, c_left = phi_w[1].tensor_factors
        self.assertEqual(epsilon_factor.symbol, "epsilon")
        self.assertEqual(
            [(index.space, index.label, index.variance) for index in epsilon_factor.ordered_indices],
            [
                (IndexSpace.FLAVOR, "r", Variance.DOWN),
                (IndexSpace.FLAVOR, "u", Variance.DOWN),
                (IndexSpace.FLAVOR, "v", Variance.DOWN),
            ],
        )
        self.assertEqual(
            [binding.node_path for binding in epsilon_factor.bindings],
            ["descendant_output", "cross.child[0]", "cross.child[1]"],
        )
        self.assertEqual(c_left.symbol, "c")
        self.assertEqual(
            [(index.space, index.label, index.variance) for index in c_left.ordered_indices],
            [
                (IndexSpace.COLOR_ADJOINT, "C", Variance.DOWN),
                (IndexSpace.COLOR_ADJOINT, "D", Variance.DOWN),
                (IndexSpace.COLOR_ADJOINT, "A", Variance.UP),
            ],
        )
        cross_left = phi_w[1].ordered_factors[0]
        self.assertEqual(cross_left.node_type, DescendantNodeType.COLOR_CROSS)
        self.assertEqual(cross_left.tensor_factor, c_left)
        self.assertEqual(
            [(binding.node_path, binding.node_index_label) for binding in c_left.bindings],
            [("child[0]", "C"), ("child[1]", "D"), ("output", "A")],
        )
        (c_right,) = phi_w[3].tensor_factors
        self.assertEqual(
            [(index.label, index.variance) for index in c_right.ordered_indices],
            [("E", Variance.DOWN), ("F", Variance.DOWN), ("B", Variance.UP)],
        )
        right_cross = phi_w[3].ordered_factors[1].children[0]
        self.assertEqual(right_cross.tensor_factor, c_right)

        tilde_w_phi = by_id["TildeW__Phi"].descendant.terms
        self.assertEqual(
            [term.coefficient for term in tilde_w_phi],
            [
                DescendantCoefficient(Fraction(-1, 2)),
                DescendantCoefficient(Fraction(1), sqrt2_power=1),
            ],
        )
        self.assertEqual([term.koszul_sign for term in tilde_w_phi], [-1, -1])
        self.assertEqual(tilde_w_phi[0].ordered_factors[0].token, "TildeW")
        self.assertEqual(tilde_w_phi[0].ordered_factors[1].node_type, DescendantNodeType.EULER_TOKEN)

    def test_channel_canonical_serialization_covers_indices_and_reversed_word(self) -> None:
        channels = emit_ordered_family_channels()
        payloads = [channel.canonical_json() for channel in channels]
        self.assertEqual(len(payloads), 16)
        self.assertEqual(len(set(payloads)), 16)
        parsed = [json.loads(payload) for payload in payloads]
        catalog = json.loads(canonical_channel_catalog_json())
        self.assertEqual(catalog, parsed)
        self.assertEqual(len(catalog), 16)
        self.assertTrue(all(set(item) == {
            "ordinal",
            "channel_id",
            "left",
            "right",
            "reverse_channel_id",
            "ordered_expression",
            "reversed_expression",
            "descendant",
            "reversed_descendant",
        } for item in parsed))

        by_id = {item["channel_id"]: item for item in parsed}
        w_phi = by_id["W__Phi"]
        self.assertEqual(w_phi["left"]["color_label"], "A")
        self.assertEqual(w_phi["right"]["color_label"], "B")
        self.assertEqual(w_phi["right"]["flavor_label"], "s")
        self.assertEqual(w_phi["reversed_descendant"]["channel_id"], "reverse_of__W__Phi")
        reversed_first_factor = w_phi["reversed_descendant"]["terms"][0]["ordered_factors"][0]
        reversed_first_indices = {
            (index["space"], index["label"]) for index in reversed_first_factor["indices"]
        }
        self.assertIn(("COLOR_ADJOINT", "B"), reversed_first_indices)
        self.assertIn(("FLAVOR", "s"), reversed_first_indices)

        tilde_w_tilde_w = by_id["TildeW__TildeW"]
        self.assertEqual(
            tilde_w_tilde_w["left"]["spinor_slots"][0]["label"],
            "dot_alpha",
        )
        self.assertEqual(
            tilde_w_tilde_w["right"]["spinor_slots"][0]["label"],
            "dot_beta",
        )


if __name__ == "__main__":
    unittest.main()
