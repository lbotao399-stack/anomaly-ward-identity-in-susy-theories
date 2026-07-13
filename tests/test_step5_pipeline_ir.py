from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
from fractions import Fraction
import json
from pathlib import Path
import tempfile
import unittest

from scripts.step5_pipeline_ir import (
    AmplitudeIR,
    Chirality,
    DerivativeApplication,
    DerivativeRule,
    DerivativeSpec,
    DerivativeTerm,
    EXACT_I,
    EXACT_I_SQRT2,
    EXACT_ONE,
    EXACT_SQRT2,
    ExactScalar,
    FactorProvenance,
    FieldSpec,
    Flow,
    FourierDREDData,
    HashDriftError,
    LinearMomentum,
    MomentumConservationError,
    NotationSchema,
    OrderedDerivativeScope,
    PipelineEdge,
    PipelineGraph,
    PipelineIRError,
    PipelinePort,
    PipelineVertex,
    PortSector,
    PortSpec,
    PROJECT_WW_NOTATION_SCHEMA_SHA256,
    PROJECT_N4_SCALAR_RING,
    PropagatorPortError,
    PropagatorSpec,
    Qi,
    Statistics,
    SymbolKind,
    SymbolSpec,
    TensorOccurrence,
    TensorSpec,
    TopologyMetadata,
    TypedIndex,
    UndefinedSymbolError,
    Variance,
    project_notation_schema,
)


COLOR = "COLOR_ADJOINT"
UNDOTTED = "UNDOTTED"
DOTTED = "DOTTED"


def color(label: str, variance: Variance = Variance.UP) -> TypedIndex:
    return TypedIndex(COLOR, label, variance)


class Step5PipelineIRTest(unittest.TestCase):
    def schema(self, *, bad_propagator_symbol: bool = False, reverse: bool = False) -> NotationSchema:
        symbols = (
            SymbolSpec("g", SymbolKind.COUPLING),
            SymbolSpec("h", SymbolKind.NORMALIZATION),
            SymbolSpec("k", SymbolKind.MOMENTUM),
            SymbolSpec("p", SymbolKind.MOMENTUM),
            SymbolSpec("q", SymbolKind.MOMENTUM),
            SymbolSpec("p2", SymbolKind.OTHER),
            SymbolSpec("epsilon", SymbolKind.REGULATOR),
            SymbolSpec("mu", SymbolKind.SCALE),
            SymbolSpec("delta4", SymbolKind.METRIC),
            SymbolSpec("hat_delta", SymbolKind.METRIC),
            SymbolSpec("tilde_delta", SymbolKind.METRIC),
        )
        derivatives = (
            DerivativeSpec("D_+", 1, UNDOTTED),
            DerivativeSpec("barD_dot+", 1, DOTTED),
        )
        fields = (
            FieldSpec(
                "V", Statistics.BOSON, Chirality.REAL, (COLOR,), (Variance.UP,)
            ),
            FieldSpec(
                "Phi", Statistics.BOSON, Chirality.CHIRAL, (COLOR,), (Variance.UP,)
            ),
            FieldSpec(
                "TildePhi",
                Statistics.BOSON,
                Chirality.ANTICHIRAL,
                (COLOR,),
                (Variance.UP,),
            ),
            FieldSpec(
                "X", Statistics.BOSON, Chirality.CHIRAL, (COLOR,), (Variance.UP,)
            ),
            FieldSpec(
                "TildeW",
                Statistics.FERMION,
                Chirality.ANTICHIRAL,
                (COLOR,),
                (Variance.UP,),
            ),
            FieldSpec(
                "Source",
                Statistics.FERMION,
                Chirality.UNCONSTRAINED,
                (COLOR,),
                (Variance.UP,),
            ),
        )
        ports = (
            PortSpec("V_Q", "V", (PortSector.QUANTUM,), (Flow.IN, Flow.OUT)),
            PortSpec("Phi_Q", "Phi", (PortSector.QUANTUM,), (Flow.IN, Flow.OUT)),
            PortSpec(
                "TildePhi_Q",
                "TildePhi",
                (PortSector.QUANTUM,),
                (Flow.IN, Flow.OUT),
            ),
            PortSpec("X_B", "X", (PortSector.BACKGROUND,), (Flow.IN, Flow.OUT)),
            PortSpec(
                "TildeW_B",
                "TildeW",
                (PortSector.BACKGROUND,),
                (Flow.IN, Flow.OUT),
            ),
            PortSpec(
                "Source_B",
                "Source",
                (PortSector.BACKGROUND,),
                (Flow.IN, Flow.OUT),
            ),
        )
        propagators = (
            PropagatorSpec(
                "P_V",
                "V_Q",
                "V_Q",
                Qi.rational(-2),
                symbol_factors=("g", "p2_missing" if bad_propagator_symbol else "p2"),
                symmetric=True,
            ),
            PropagatorSpec(
                "P_Phi",
                "Phi_Q",
                "TildePhi_Q",
                Qi.rational(1),
                symbol_factors=("g", "p2"),
                symmetric=True,
            ),
        )
        schema = NotationSchema(
            "STEP5_PIPELINE_TEST_V1",
            (COLOR, UNDOTTED, DOTTED),
            tuple(reversed(symbols)) if reverse else symbols,
            tuple(reversed(derivatives)) if reverse else derivatives,
            (
                DerivativeRule(
                    ("D_+", "barD_dot+"),
                    (
                        DerivativeTerm(Qi.rational(-1), ("barD_dot+", "D_+")),
                        DerivativeTerm(Qi.imaginary(2), symbol_factors=("p",)),
                    ),
                    ("all incoming momentum",),
                ),
            ),
            tuple(reversed(fields)) if reverse else fields,
            tuple(reversed(ports)) if reverse else ports,
            tuple(reversed(propagators)) if reverse else propagators,
            (
                TensorSpec(
                    "c",
                    "COLOR_STRUCTURE_CONSTANT",
                    (COLOR, COLOR, COLOR),
                    (Variance.DOWN, Variance.DOWN, Variance.UP),
                ),
            ),
            FourierDREDData(
                "exp(+i p.x)",
                "partial -> +i p",
                "d=4-2 epsilon",
                "mu^(2 epsilon) d^d k/(2 pi)^d",
                "delta4",
                "hat_delta",
                "tilde_delta",
                "epsilon",
                "mu",
            ),
        )
        return schema

    def graph(self, schema: NotationSchema) -> PipelineGraph:
        k = LinearMomentum.symbol("k")
        p = LinearMomentum.symbol("p")
        q = LinearMomentum.symbol("q")
        kpq = k + p + q
        kq = k + q
        ports = (
            PipelinePort("I0", "I", 0, "V_Q", PortSector.QUANTUM, Flow.OUT, k, (color("C"),)),
            PipelinePort("I1", "I", 1, "V_Q", PortSector.QUANTUM, Flow.IN, -kpq, (color("D"),)),
            PipelinePort(
                "IS", "I", 2, "Source_B", PortSector.BACKGROUND, Flow.IN, p + q, (color("S"),)
            ),
            PipelinePort("A0", "A", 0, "V_Q", PortSector.QUANTUM, Flow.IN, -k, (color("C"),)),
            PipelinePort("A1", "A", 1, "V_Q", PortSector.QUANTUM, Flow.OUT, kq, (color("E"),)),
            PipelinePort(
                "AT", "A", 2, "TildeW_B", PortSector.BACKGROUND, Flow.IN, -q, (color("A"),)
            ),
            PipelinePort("B0", "B", 0, "V_Q", PortSector.QUANTUM, Flow.IN, -kq, (color("E"),)),
            PipelinePort("B1", "B", 1, "V_Q", PortSector.QUANTUM, Flow.OUT, kpq, (color("D"),)),
            PipelinePort("BX", "B", 2, "X_B", PortSector.BACKGROUND, Flow.IN, -p, (color("B"),)),
        )
        factors = (
            FactorProvenance("fI", "INSERTION", Qi.rational(1, 128), "D_-K_+K_+", "5.53b"),
            FactorProvenance(
                "fA", "VERTEX", Qi.imaginary(-1, 8), "-i h/8", "5.53e", ("h",)
            ),
            FactorProvenance(
                "fB", "VERTEX", Qi.imaginary(1, 8), "+i h/8", "5.53e", ("h",)
            ),
        )
        color_tensor_a = TensorOccurrence(
            "cA", "c", (color("A", Variance.DOWN), color("C", Variance.DOWN), color("E"))
        )
        color_tensor_b = TensorOccurrence(
            "cB", "c", (color("B", Variance.DOWN), color("E", Variance.DOWN), color("D"))
        )
        graph = PipelineGraph(
            "WW_TRIANGLE_DIRECT",
            schema.canonical_hash,
            (
                PipelineVertex("I", "COMPOSITE", ("I0", "I1", "IS"), ("fI",)),
                PipelineVertex(
                    "A",
                    "ANTICHIRAL_CUBIC",
                    ("A0", "A1", "AT"),
                    ("fA",),
                    (
                        OrderedDerivativeScope(
                            "bar_scope",
                            (
                                DerivativeApplication("bar0", "barD_dot+", "A0"),
                                DerivativeApplication("bar1", "barD_dot+", "A1"),
                            ),
                        ),
                    ),
                    (color_tensor_a,),
                ),
                PipelineVertex(
                    "B",
                    "CHIRAL_CUBIC",
                    ("B0", "B1", "BX"),
                    ("fB",),
                    (
                        OrderedDerivativeScope(
                            "d_scope",
                            (
                                DerivativeApplication("d0", "D_+", "B0"),
                                DerivativeApplication("d1", "D_+", "B1"),
                            ),
                        ),
                    ),
                    (color_tensor_b,),
                ),
            ),
            ports,
            (
                PipelineEdge("e0", "I0", "A0", "P_V", k),
                PipelineEdge("e1", "A1", "B0", "P_V", kq),
                PipelineEdge("e2", "B1", "I1", "P_V", kpq),
            ),
            factors,
            ("IS", "AT", "BX"),
            TopologyMetadata(True, 1, 1, Fraction(1), "DIRECT"),
        )
        graph.validate(schema)
        return graph

    def test_qi_arithmetic_is_exact(self) -> None:
        left = Qi(Fraction(1, 3), Fraction(2, 5))
        right = Qi(Fraction(7, 11), Fraction(-3, 7))
        product = left * right
        self.assertEqual(product.real, Fraction(1, 3) * Fraction(7, 11) + Fraction(2, 5) * Fraction(3, 7))
        self.assertEqual(product.imag, -Fraction(1, 3) * Fraction(3, 7) + Fraction(2, 5) * Fraction(7, 11))
        self.assertEqual((left / right) * right, left)
        self.assertEqual(left.conjugate().imag, Fraction(-2, 5))

    def test_exact_scalar_defining_relations(self) -> None:
        self.assertEqual(EXACT_I * EXACT_I, ExactScalar.rational(-1))
        self.assertEqual(EXACT_SQRT2 * EXACT_SQRT2, ExactScalar.rational(2))
        self.assertEqual(EXACT_I * EXACT_SQRT2, EXACT_I_SQRT2)
        self.assertEqual(EXACT_SQRT2 * EXACT_I, EXACT_I_SQRT2)
        self.assertEqual(EXACT_I_SQRT2 * EXACT_I_SQRT2, ExactScalar.rational(-2))

    def test_exact_scalar_superpotential_like_sqrt2_factor(self) -> None:
        sqrt2_over_six = ExactScalar.sqrt2(1, 6)
        minus_i_over_eight = ExactScalar.imaginary(-1, 8)
        self.assertEqual(
            sqrt2_over_six * minus_i_over_eight,
            ExactScalar.i_sqrt2(-1, 48),
        )

    def test_amplitude_ir_promotes_qi_factors_to_full_scalar_ring(self) -> None:
        schema = replace(self.schema(), scalar_ring=PROJECT_N4_SCALAR_RING)
        graph = self.graph(schema)
        sqrt2_factor = FactorProvenance(
            "sqrt2_like",
            "ALGEBRAIC_NORMALIZATION",
            ExactScalar.sqrt2(1, 6),
            "sqrt2/6",
            "exact-ring-test",
        )
        amplitude = AmplitudeIR.from_factors(
            "A_WITH_SQRT2",
            schema,
            graph,
            graph.factors + (sqrt2_factor,),
            ("p2",),
            "typed external operator",
        )
        self.assertEqual(amplitude.exact_coefficient, ExactScalar.sqrt2(1, 49152))
        amplitude.validate(schema, graph)

    def test_exact_scalar_division_conjugation_and_json_are_exact(self) -> None:
        value = ExactScalar(
            Fraction(1, 3),
            Fraction(2, 5),
            Fraction(-3, 7),
            Fraction(4, 11),
        )
        self.assertEqual(value / value, EXACT_ONE)
        self.assertEqual(
            value.conjugate(),
            ExactScalar(Fraction(1, 3), Fraction(-2, 5), Fraction(-3, 7), Fraction(-4, 11)),
        )
        self.assertEqual(ExactScalar.from_dict(value.canonical_dict()), value)
        with self.assertRaises(ZeroDivisionError):
            value / ExactScalar()

    def test_qi_is_exact_ww_subring_adapter(self) -> None:
        qi = Qi(Fraction(5, 13), Fraction(-7, 17))
        self.assertEqual(qi.to_exact_scalar(), ExactScalar.from_qi(qi))
        self.assertEqual(qi.to_exact_scalar().to_qi(), qi)
        with self.assertRaisesRegex(PipelineIRError, "outside the Q\\(i\\)"):
            EXACT_SQRT2.to_qi()

    def test_schema_hash_is_order_independent_and_immutable(self) -> None:
        first = self.schema()
        second = self.schema(reverse=True)
        self.assertEqual(first.canonical_hash, second.canonical_hash)
        self.assertEqual(len(first.canonical_hash), 64)
        with self.assertRaises(FrozenInstanceError):
            first.schema_id = "mutated"  # type: ignore[misc]

    def test_notation_schema_is_a_canonical_json_input(self) -> None:
        schema = self.schema()
        rebuilt = NotationSchema.from_dict(schema.canonical_dict())
        self.assertEqual(rebuilt.canonical_dict(), schema.canonical_dict())
        self.assertEqual(rebuilt.canonical_hash, schema.canonical_hash)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "notation.json"
            schema.write_json(path)
            loaded = NotationSchema.load_json(path)
        self.assertEqual(loaded.canonical_dict(), schema.canonical_dict())
        self.assertEqual(loaded.canonical_hash, schema.canonical_hash)

    def test_notation_json_shape_drift_is_rejected(self) -> None:
        payload = self.schema().canonical_dict()
        payload.pop("derivative_rules")
        with self.assertRaisesRegex(PipelineIRError, "shape mismatch"):
            NotationSchema.from_dict(payload)

    def test_valid_triangle_has_strong_typed_invariants(self) -> None:
        schema = self.schema()
        graph = self.graph(schema)
        self.assertEqual(graph.topology.loop_number, 1)
        self.assertEqual(len(graph.edges), 3)
        self.assertEqual(len(graph.canonical_hash), 64)

    def test_amplitude_coefficient_is_product_of_provenance_factors(self) -> None:
        schema = self.schema()
        graph = self.graph(schema)
        amplitude = AmplitudeIR.from_factors(
            "A_WW_DIRECT",
            schema,
            graph,
            graph.factors,
            ("p2",),
            "TildeW_dot_alpha^D (i p_+^dot_alpha) X^E",
        )
        expected = Qi.rational(1, 128) * Qi.imaginary(-1, 8) * Qi.imaginary(1, 8)
        self.assertEqual(amplitude.exact_coefficient, expected)
        amplitude.validate(schema, graph)

    def test_undefined_symbol_is_rejected(self) -> None:
        with self.assertRaisesRegex(UndefinedSymbolError, "p2_missing"):
            self.schema(bad_propagator_symbol=True)

    def test_invalid_propagator_ports_are_rejected(self) -> None:
        schema = self.schema()
        graph = self.graph(schema)
        bad_ports = tuple(
            replace(port, port_spec="Phi_Q") if port.port_id == "I0" else port
            for port in graph.ports
        )
        bad = replace(graph, ports=bad_ports)
        with self.assertRaisesRegex(PropagatorPortError, "cannot connect"):
            bad.validate(schema)

    def test_broken_vertex_momentum_conservation_is_rejected(self) -> None:
        schema = self.schema()
        graph = self.graph(schema)
        bad_ports = tuple(
            replace(port, momentum=LinearMomentum.symbol("p", -1))
            if port.port_id == "AT"
            else port
            for port in graph.ports
        )
        bad = replace(graph, ports=bad_ports)
        with self.assertRaisesRegex(MomentumConservationError, "vertex A"):
            bad.validate(schema)

    def test_hash_drift_is_rejected(self) -> None:
        schema = self.schema()
        wrong_hash = "0" * 64
        with self.assertRaises(HashDriftError):
            schema.assert_canonical_hash(wrong_hash)
        graph = self.graph(schema)
        with self.assertRaises(HashDriftError):
            replace(graph, notation_hash=wrong_hash).validate(schema)

    def test_amplitude_factor_tampering_is_rejected(self) -> None:
        schema = self.schema()
        graph = self.graph(schema)
        amplitude = AmplitudeIR.from_factors(
            "A_WW_DIRECT",
            schema,
            graph,
            graph.factors,
            ("p2",),
            "TildeW X",
        )
        with self.assertRaisesRegex(PipelineIRError, "exact coefficient"):
            replace(amplitude, exact_coefficient=Qi.rational(7)).validate(schema, graph)

    def test_project_ww_factory_has_exact_request_vocabulary(self) -> None:
        schema = project_notation_schema()
        self.assertEqual(
            {item.name for item in schema.symbols},
            {"h", "g2", "k", "p", "q", "pi", "epsilon", "mu", "g4", "ghat"},
        )
        self.assertEqual(
            {item.name for item in schema.fields},
            {"V", "W_plus", "TildeW_dot_alpha", "Source[nabla_-(X^A X^B)]"},
        )
        self.assertEqual(
            {item.name for item in schema.ports},
            {"V_Q", "W_plus_B", "TildeW_B", "WW_source_B"},
        )
        self.assertEqual({item.name for item in schema.propagators}, {"P_VV"})
        self.assertEqual(
            {item.name for item in schema.derivatives},
            {
                "D_+",
                "D_-",
                "D_a",
                "barD_dot_alpha",
                "D2",
                "barD2",
                "K_+",
                "nabla_+",
                "nabla_-",
            },
        )
        self.assertEqual(
            {item.name for item in schema.tensors},
            {"kappa", "c", "delta4theta"},
        )
        self.assertEqual(schema.canonical_hash, PROJECT_WW_NOTATION_SCHEMA_SHA256)
        self.assertEqual(schema.scalar_ring, PROJECT_N4_SCALAR_RING)
        self.assertEqual(
            schema.field_map["Source[nabla_-(X^A X^B)]"].index_variances,
            (Variance.DOWN, Variance.DOWN),
        )
        self.assertEqual(
            schema.field_map["TildeW_dot_alpha"].index_variances,
            (Variance.UP, Variance.DOWN),
        )
        self.assertEqual(
            schema.scalar_ring.relations,
            ("i^2=-1", "sqrt2^2=2", "i*sqrt2=sqrt2*i"),
        )

    def test_project_ww_canonical_json_roundtrip_preserves_hash(self) -> None:
        schema = project_notation_schema()
        encoded = schema.canonical_json()
        decoded = NotationSchema.from_canonical_json(encoded)
        self.assertEqual(decoded.canonical_json(), encoded)
        self.assertEqual(decoded.canonical_hash, PROJECT_WW_NOTATION_SCHEMA_SHA256)

    def test_project_ww_missing_field_is_rejected(self) -> None:
        payload = json.loads(project_notation_schema().canonical_json())
        payload["fields"] = [item for item in payload["fields"] if item["name"] != "V"]
        with self.assertRaisesRegex(UndefinedSymbolError, "undefined field V"):
            NotationSchema.from_canonical_dict(payload)

    def test_project_ww_missing_field_variance_is_rejected(self) -> None:
        payload = json.loads(project_notation_schema().canonical_json())
        source = next(
            item
            for item in payload["fields"]
            if item["name"] == "Source[nabla_-(X^A X^B)]"
        )
        source.pop("index_variances")
        with self.assertRaisesRegex(PipelineIRError, "explicit index_spaces"):
            NotationSchema.from_canonical_dict(payload)

    def test_project_ww_missing_derivative_is_rejected(self) -> None:
        payload = json.loads(project_notation_schema().canonical_json())
        payload["derivatives"] = [
            item for item in payload["derivatives"] if item["name"] != "D_+"
        ]
        with self.assertRaisesRegex(UndefinedSymbolError, r"undefined symbol D_\+"):
            NotationSchema.from_canonical_dict(payload)

    def test_project_ww_missing_tensor_is_rejected(self) -> None:
        payload = json.loads(project_notation_schema().canonical_json())
        payload["tensors"] = [item for item in payload["tensors"] if item["name"] != "c"]
        with self.assertRaisesRegex(UndefinedSymbolError, "undefined symbol c"):
            NotationSchema.from_canonical_dict(payload)


if __name__ == "__main__":
    unittest.main()
