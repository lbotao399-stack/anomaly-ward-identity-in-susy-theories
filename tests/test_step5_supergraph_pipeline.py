from __future__ import annotations

from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_graph_ir import (
    Chirality,
    FieldType,
    Flow,
    GraphIR,
    HalfEdge,
    Statistics,
    Vertex,
    InternalEdge,
)
from scripts.step5_pipeline_ir import (
    Chirality as SchemaChirality,
    FieldSpec as SchemaFieldSpec,
    Flow as SchemaFlow,
    HashDriftError,
    PortSector,
    PortSpec as SchemaPortSpec,
    PropagatorPortError,
    PropagatorSpec as SchemaPropagatorSpec,
    Qi,
    Statistics as SchemaStatistics,
    SymbolKind,
    SymbolSpec,
    TensorSpec,
    UndefinedSymbolError,
    Variance as SchemaVariance,
    project_notation_schema,
)
from scripts.step5_supergraph_pipeline import (
    ValenceOnlyRequestError,
    build_demo_payload,
    compile_request,
    graph_automorphism_order,
    graph_canonical_key,
    matter_edge_structural_request,
    render_textbook_markdown,
    valence_only_fixture,
    ww_reflected_seed_request,
    ww_seed_request,
)
from scripts.step5_vertex_grammar import ExactCoefficient


def matter_test_schema():
    """Explicit structural extension; the frozen Project factory is WW-only."""

    base = project_notation_schema()
    color = "COLOR_ADJOINT"
    flavor = "FLAVOR"
    return replace(
        base,
        schema_id="STEP5_SUPERGRAPH_PIPELINE_MATTER_STRUCTURAL_TEST_V1",
        index_spaces=base.index_spaces + (flavor,),
        symbols=base.symbols
        + (SymbolSpec("G_PhiTildePhi", SymbolKind.OTHER),),
        fields=base.fields
        + (
            SchemaFieldSpec(
                "Phi", SchemaStatistics.BOSON, SchemaChirality.CHIRAL, (color,)
            ),
            SchemaFieldSpec(
                "TildePhi",
                SchemaStatistics.BOSON,
                SchemaChirality.ANTICHIRAL,
                (color,),
            ),
        ),
        ports=base.ports
        + (
            SchemaPortSpec(
                "Phi_Q",
                "Phi",
                (PortSector.QUANTUM,),
                (SchemaFlow.IN, SchemaFlow.OUT),
            ),
            SchemaPortSpec(
                "TildePhi_Q",
                "TildePhi",
                (PortSector.QUANTUM,),
                (SchemaFlow.IN, SchemaFlow.OUT),
            ),
        ),
        propagators=base.propagators
        + (
            SchemaPropagatorSpec(
                "P_PHI_TILDEPHI_STRUCTURAL",
                "Phi_Q",
                "TildePhi_Q",
                Qi.rational(1),
                symbol_factors=("G_PhiTildePhi",),
                tensor_factors=("kappa", "delta_flavor"),
                symmetric=False,
            ),
        ),
        tensors=base.tensors
        + (
            TensorSpec(
                "delta_flavor",
                "FLAVOR_KRONECKER",
                (flavor, flavor),
                (SchemaVariance.UP, SchemaVariance.DOWN),
            ),
        ),
        required_tensors=base.required_tensors + ("delta_flavor",),
    )


class Step5SupergraphPipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ww_schema = project_notation_schema()
        cls.matter_schema = matter_test_schema()
        cls.ww = compile_request(ww_seed_request(cls.ww_schema), cls.ww_schema)
        cls.ww_reflected = compile_request(
            ww_reflected_seed_request(cls.ww_schema), cls.ww_schema
        )
        cls.matter = compile_request(
            matter_edge_structural_request(cls.matter_schema), cls.matter_schema
        )

    def test_valence_only_request_is_rejected_before_graph_construction(self) -> None:
        with self.assertRaisesRegex(ValenceOnlyRequestError, "cannot be promoted to GraphIR"):
            compile_request(valence_only_fixture(self.ww_schema), self.ww_schema)

    def test_ww_typed_pairing_census_is_complete_and_endpoint_exact(self) -> None:
        self.assertEqual(self.ww.typed_pairings, 8)
        self.assertEqual(self.ww.endpoint_admissible_pairings, 1)
        self.assertEqual(self.ww.rejected_disconnected, 0)
        self.assertEqual(self.ww.rejected_non_one_loop, 0)
        self.assertEqual(self.ww.isomorphism_classes, 1)
        self.assertEqual(self.ww.accepted_pairings_reconstructed, 1)
        self.assertEqual(sum(item.class_multiplicity for item in self.ww.amplitudes), 1)

    def test_ww_graph_and_exact_pre_d_coefficient_match_project_seed(self) -> None:
        (amplitude,) = self.ww.amplitudes
        graph = amplitude.graph
        self.assertEqual(graph.cycle_rank(), 1)
        self.assertTrue(graph.validate_linear_momentum_routing()["passed"])
        self.assertEqual({edge.edge_id for edge in graph.internal_edges}, {"e0", "e1", "e2"})
        self.assertEqual(amplitude.wick_koszul_sign, 1)
        self.assertEqual(amplitude.automorphism_order, 1)
        self.assertEqual(amplitude.automorphism_symmetry_factor, Fraction(1))
        self.assertEqual(amplitude.exact_coefficient_raw.render(), "-1/8*g2*g2*g2*h*h")
        self.assertEqual(amplitude.exact_coefficient_reduced.render(), "-1/8*g2")
        self.assertEqual(
            amplitude.coefficient_reduction_trace,
            ("used (h)*(g2)=1 exactly 2 time(s)",),
        )
        self.assertEqual(amplitude.normalization_status, "EXACT_PROJECT_NORMALIZATION")
        self.assertEqual(self.ww.schema_hash, self.ww_schema.canonical_hash)
        self.assertEqual(amplitude.schema_hash, self.ww_schema.canonical_hash)
        self.assertEqual(
            dict(amplitude.graph.metadata)["notation_schema_hash"],
            self.ww_schema.canonical_hash,
        )

    def test_direct_and_reflected_ww_orientations_are_separate_exact_amplitudes(self) -> None:
        direct = self.ww.amplitudes[0]
        reflected = self.ww_reflected.amplitudes[0]
        self.assertEqual(
            direct.external_fermion_word,
            ("TildeW_dot_alpha", "W_plus"),
        )
        self.assertEqual(
            reflected.external_fermion_word,
            ("W_plus", "TildeW_dot_alpha"),
        )
        self.assertEqual(direct.external_koszul_sign, 1)
        self.assertEqual(reflected.external_koszul_sign, -1)
        self.assertEqual(
            direct.orientation_signature,
            (
                "e0:V--V:k",
                "e1:V--V:k+q",
                "e2:V--V:k+p+q",
            ),
        )
        self.assertEqual(reflected.orientation_signature, direct.orientation_signature)
        self.assertEqual(direct.exact_coefficient_reduced.render(), "-1/8*g2")
        self.assertEqual(reflected.exact_coefficient_reduced.render(), "1/8*g2")
        self.assertNotEqual(direct.canonical_key, reflected.canonical_key)

    def test_hash_drift_is_rejected_before_wick_enumeration(self) -> None:
        request = replace(
            ww_seed_request(self.ww_schema),
            schema_hash="0" * 64,
        )
        with self.assertRaisesRegex(HashDriftError, "notation hash drift"):
            compile_request(request, self.ww_schema)

    def test_missing_exact_symbol_is_rejected_before_wick_enumeration(self) -> None:
        request = ww_seed_request(self.ww_schema)
        vertex = request.vertices[1]
        bad_vertex = replace(
            vertex,
            coefficient=vertex.coefficient
            * ExactCoefficient(symbols=("missing_exact_symbol",)),
        )
        request = replace(
            request,
            vertices=(request.vertices[0], bad_vertex, request.vertices[2]),
        )
        with self.assertRaisesRegex(UndefinedSymbolError, "missing_exact_symbol"):
            compile_request(request, self.ww_schema)

    def test_missing_derivative_and_bad_vv_ports_are_rejected(self) -> None:
        request = ww_seed_request(self.ww_schema)
        bad_insertion = replace(
            request.vertices[0],
            operator_factors=request.vertices[0].operator_factors + ("D_missing(V)",),
        )
        with self.assertRaisesRegex(UndefinedSymbolError, "D_missing"):
            compile_request(
                replace(request, vertices=(bad_insertion,) + request.vertices[1:]),
                self.ww_schema,
            )

        vector = replace(
            request.propagators[0],
            left_notation_port_spec="W_plus_B",
        )
        with self.assertRaisesRegex(PropagatorPortError, "disagree"):
            compile_request(
                replace(request, propagators=(vector,)),
                self.ww_schema,
            )

    def test_amplitude_is_factorized_without_hidden_vertex_or_edge(self) -> None:
        (amplitude,) = self.ww.amplitudes
        categories = [factor.category for factor in amplitude.factors]
        self.assertEqual(categories.count("INSERTION"), 1)
        self.assertEqual(categories.count("ACTION_VERTEX"), 2)
        self.assertEqual(categories.count("PROPAGATOR"), 3)
        self.assertEqual(categories.count("VERTEX_DELTA"), 3)
        self.assertEqual(categories.count("LOOP_MEASURE"), 1)
        self.assertEqual(categories.count("EXTERNAL_LEG"), 3)
        self.assertTrue(all(factor.origins for factor in amplitude.factors))
        payload = amplitude.canonical_dict()
        self.assertIn("F_vertex_vI", payload["preintegration_product"])
        self.assertIn("F_prop_e0", payload["preintegration_product"])
        self.assertIn("c_{ACD}", json.dumps(payload))
        self.assertIn("delta(-k+(k+q)-q)", json.dumps(payload))

    def test_matter_edge_is_connected_oriented_and_explicitly_structural(self) -> None:
        self.assertEqual(self.matter.typed_pairings, 1)
        self.assertEqual(self.matter.endpoint_admissible_pairings, 1)
        self.assertEqual(self.matter.isomorphism_classes, 1)
        (amplitude,) = self.matter.amplitudes
        self.assertEqual(amplitude.graph.cycle_rank(), 1)
        self.assertTrue(amplitude.graph.validate_linear_momentum_routing()["passed"])
        self.assertIn(
            "eM:Phi->TildePhi:p-k",
            amplitude.orientation_signature,
        )
        self.assertEqual(
            amplitude.normalization_status,
            "EXACT_PROJECT_NORMALIZATION+STRUCTURAL_SYMBOL_NOT_EVALUATED",
        )
        self.assertEqual(amplitude.exact_coefficient_raw.render(), "2*G_PhiTildePhi*g2*h*h")
        self.assertEqual(amplitude.exact_coefficient_reduced.render(), "2*G_PhiTildePhi*h")
        matter_factor = next(
            factor for factor in amplitude.factors if factor.factor_id == "F_prop_eM"
        )
        self.assertEqual(matter_factor.expression, "P_PhiTildePhi[p-k]")
        self.assertEqual(
            dict(matter_factor.metadata)["normalization_status"],
            "STRUCTURAL_SYMBOL_NOT_EVALUATED",
        )

    def test_vertex_order_changes_do_not_change_canonical_isomorphism_key(self) -> None:
        request = matter_edge_structural_request(self.matter_schema)
        reversed_request = replace(request, vertices=tuple(reversed(request.vertices)))
        original = compile_request(request, self.matter_schema).amplitudes[0]
        reversed_amplitude = compile_request(
            reversed_request, self.matter_schema
        ).amplitudes[0]
        self.assertEqual(original.canonical_key, reversed_amplitude.canonical_key)
        self.assertEqual(original.exact_coefficient_reduced, reversed_amplitude.exact_coefficient_reduced)

    def test_automorphism_order_is_computed_not_inserted(self) -> None:
        field = FieldType("X", Statistics.BOSON, Chirality.REAL)
        half_edges = (
            HalfEdge("a0", "a", 0, field, Flow.OUT, "k"),
            HalfEdge("a1", "a", 1, field, Flow.OUT, "k+p"),
            HalfEdge("b0", "b", 0, field, Flow.IN, "-k"),
            HalfEdge("b1", "b", 1, field, Flow.IN, "-k-p"),
        )
        graph = GraphIR(
            "COMBINATORIAL_AUT_TEST",
            (
                Vertex("a", "IDENTICAL", ("a0", "a1"), "1", (), "z0", "delta", "-2*k-p"),
                Vertex("b", "IDENTICAL", ("b0", "b1"), "1", (), "z1", "delta", "2*k+p"),
            ),
            half_edges,
            (
                InternalEdge("e0", "a0", "b0", "P_X", "k", Flow.NONE),
                InternalEdge("e1", "a1", "b1", "P_X", "k+p", Flow.NONE),
            ),
            (),
            ("k",),
        )
        self.assertEqual(graph_automorphism_order(graph), 2)

        amplitude = self.ww.amplitudes[0]
        audit = next(
            factor
            for factor in amplitude.factors
            if factor.factor_id == "F_aut"
        )
        self.assertEqual(audit.category, "AUTOMORPHISM_AUDIT_ONLY")
        self.assertEqual(audit.coefficient.render(), "1")
        self.assertEqual(
            dict(audit.metadata)["coefficient_policy"],
            "AUDIT_ONLY_CLASS_ALREADY_SUMS_LABELED_PAIRINGS",
        )
        self.assertNotIn("F_aut", amplitude.canonical_dict()["preintegration_product"])

    def test_markdown_and_graph_renderers_are_human_readable_and_lossless(self) -> None:
        markdown = render_textbook_markdown(self.ww)
        self.assertIn("N_{\\rm typed}=8", markdown)
        self.assertIn("\\mathcal A_G=", markdown)
        self.assertIn("C_G^{\\rm Project}=-1/8*g2", markdown)
        self.assertIn("| factor | category | exact expression | coefficient | origin |", markdown)
        self.assertIn("```dot", markdown)
        self.assertIn("```mermaid", markdown)
        (amplitude,) = self.ww.amplitudes
        self.assertIn("digraph", amplitude.graph.to_dot())
        self.assertIn("graph LR", amplitude.graph.to_mermaid())

    def test_demo_payload_has_no_duplicate_canonical_class(self) -> None:
        payload = build_demo_payload(self.ww_schema, self.matter_schema)
        self.assertEqual(len(payload["pipelines"]), 3)
        for pipeline in payload["pipelines"]:
            completeness = pipeline["completeness"]
            self.assertTrue(completeness["no_double_count"])
            keys = [item["canonical_key"] for item in pipeline["amplitudes"]]
            self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
