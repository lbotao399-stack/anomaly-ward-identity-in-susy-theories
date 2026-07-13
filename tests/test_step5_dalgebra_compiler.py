from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_dalgebra_compiler.py"
MATRIX_ENGINE = ROOT / "scripts/verify_step5_propagators.py"


def load(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


class Step5DAlgebraCompilerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.d = load(SCRIPT, "step5_dalgebra_compiler")
        cls.engine = load(MATRIX_ENGINE, "step5_dalgebra_matrix_oracle")
        cls.compiler = cls.d.DAlgebraCompiler()
        cls.tag = cls.d.EndpointTag("e0", "loop")
        cls.p = "k"

    def compile_word(self, *word):
        return self.compiler.compile((self.d.Term(1, tuple(word)),))

    def sample_job(self):
        external_tag = self.d.EndpointTag("e0", "external")
        return self.d.DAlgebraJob(
            job_id="DA-JOB-001",
            notation_hash="a" * 64,
            graph_hash="b" * 64,
            amplitude_id="AMP-WW-DIRECT-001",
            coefficient=self.d.GaussianRational(Fraction(1, 3), Fraction(2, 5)),
            edges=(self.d.EdgeDeclaration("e0", ("loop", "external"), "k"),),
            legs=(
                self.d.LegDeclaration(
                    "L0", self.d.Chirality.CHIRAL, 0, external_tag
                ),
            ),
            propagators=(self.d.PropagatorDeclaration("e0", "k", "VECTOR"),),
            operator_word=(
                self.d.D2(self.tag, self.p),
                self.d.BarD2(self.tag, self.p),
                self.d.D2(self.tag, self.p),
                self.d.Propagator("e0", "k"),
                self.d.D("+", external_tag, "k"),
                self.d.ExternalLeg("L0", self.d.Chirality.CHIRAL, 0, external_tag),
            ),
        )

    def ambiguous_mixed_external_job(self):
        external_tag = self.d.EndpointTag("e0", "external")
        return self.d.DAlgebraJob(
            job_id="DA-JOB-MIXED-UNIMPLEMENTED",
            notation_hash="c" * 64,
            graph_hash=None,
            amplitude_id="AMP-MIXED-EXTERNAL",
            coefficient=self.d.ONE,
            edges=(self.d.EdgeDeclaration("e0", ("external",), "p"),),
            legs=(
                self.d.LegDeclaration(
                    "L0", self.d.Chirality.CHIRAL, 0, external_tag
                ),
            ),
            propagators=(),
            operator_word=(
                self.d.D("+", external_tag, "p"),
                self.d.BarD("-", external_tag, "p"),
                self.d.ExternalLeg("L0", self.d.Chirality.CHIRAL, 0, external_tag),
            ),
        )

    def test_gaussian_rational_arithmetic_is_exact(self) -> None:
        z = self.d.GaussianRational(Fraction(1, 3), Fraction(2, 5))
        w = self.d.GaussianRational(Fraction(-7, 11), Fraction(3, 2))
        self.assertEqual((z * w) / w, z)
        self.assertNotIn("float", type((z * w).re).__name__.lower())

    def test_same_chirality_order_and_nilpotence(self) -> None:
        d_minus_plus = self.compile_word(
            self.d.D("-", self.tag, self.p), self.d.D("+", self.tag, self.p)
        )
        self.assertEqual(len(d_minus_plus.outputs), 1)
        self.assertEqual(d_minus_plus.outputs[0].coefficient, self.d.gaussian(Fraction(1, 2)))
        self.assertEqual(d_minus_plus.outputs[0].word, (self.d.D2(self.tag, self.p),))

        bar_minus_plus = self.compile_word(
            self.d.BarD("-", self.tag, self.p), self.d.BarD("+", self.tag, self.p)
        )
        self.assertEqual(bar_minus_plus.outputs[0].coefficient, self.d.gaussian(Fraction(-1, 2)))
        self.assertEqual(bar_minus_plus.outputs[0].word, (self.d.BarD2(self.tag, self.p),))

        nilpotent = self.compile_word(
            self.d.D("+", self.tag, self.p), self.d.D("+", self.tag, self.p)
        )
        self.assertEqual(nilpotent.outputs, ())

    def test_mixed_anticommutator_is_a_two_branch_exact_rewrite(self) -> None:
        trace = self.compile_word(
            self.d.D("+", self.tag, self.p), self.d.BarD("-", self.tag, self.p)
        )
        self.assertEqual(len(trace.outputs), 2)
        by_type = {tuple(type(token).__name__ for token in term.word): term for term in trace.outputs}
        self.assertEqual(by_type[("BarD", "D")].coefficient, self.d.gaussian(-1))
        mixed = by_type[("MixedMomentum",)]
        self.assertEqual(mixed.coefficient, self.d.gaussian(-2))
        self.assertEqual(mixed.word[0].fourier_factor, self.d.I)

    def test_projector_words_use_repository_minus_sixteen_convention(self) -> None:
        forward = self.compile_word(
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
            self.d.D2(self.tag, self.p),
        )
        reverse = self.compile_word(
            self.d.BarD2(self.tag, self.p),
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
        )
        self.assertEqual(forward.outputs[0].coefficient, self.d.gaussian(-16))
        self.assertEqual(
            forward.outputs[0].word,
            (self.d.MomentumSquare(self.tag, self.p), self.d.D2(self.tag, self.p)),
        )
        self.assertEqual(reverse.outputs[0].coefficient, self.d.gaussian(-16))
        self.assertEqual(
            reverse.outputs[0].word,
            (self.d.MomentumSquare(self.tag, self.p), self.d.BarD2(self.tag, self.p)),
        )

    def test_chirality_external_derivative_and_collapse_tokens_are_typed(self) -> None:
        chiral = self.d.ExternalLeg("X", self.d.Chirality.CHIRAL, 0, self.tag)
        killed = self.compile_word(self.d.BarD("+", self.tag, self.p), chiral)
        self.assertEqual(killed.outputs, ())
        retained = self.compile_word(self.d.D("+", self.tag, self.p), chiral)
        self.assertIsInstance(retained.outputs[0].word[0], self.d.ExternalDerivative)
        self.assertEqual(retained.outputs[0].word[0].derivative_kind, "D")

        collapsed = self.compile_word(
            self.d.MomentumSquare(self.tag, self.p), self.d.Propagator("e0", self.p)
        )
        self.assertEqual(len(collapsed.outputs), 1)
        self.assertIsInstance(collapsed.outputs[0].word[0], self.d.Collapse)
        self.assertEqual(collapsed.outputs[0].word[0].edge_id, "e0")

    def test_endpoint_transfer_records_ibp_and_koszul_separately(self) -> None:
        source = self.d.Term(1, (self.d.D("-", self.tag, self.p),))
        target = self.d.EndpointTag("e1", "external")
        moved = self.d.transfer_endpoint(source, 0, target, (1,))
        self.assertEqual(moved.coefficient, self.d.ONE)
        self.assertEqual(
            [entry.kind for entry in moved.sign_ledger],
            [self.d.LedgerKind.IBP, self.d.LedgerKind.KOSZUL],
        )
        self.assertEqual([entry.factor for entry in moved.sign_ledger], [self.d.gaussian(-1)] * 2)
        self.assertEqual(moved.word[0].tag, target)

    def test_every_rewrite_strictly_decreases_the_declared_measure(self) -> None:
        trace = self.compile_word(
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
        )
        self.assertTrue(trace.terminated)
        self.assertTrue(trace.steps)
        for step in trace.steps:
            self.assertTrue(all(after < step.measure_before for after in step.measures_after))
        first = trace.deterministic_json()
        second = self.compile_word(
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
            self.d.D2(self.tag, self.p),
            self.d.BarD2(self.tag, self.p),
        ).deterministic_json()
        self.assertEqual(first, second)
        json.loads(first)

    def test_declared_critical_pairs_are_joinable(self) -> None:
        audits = self.d.critical_pair_suite()
        self.assertGreaterEqual(len(audits), 3)
        self.assertTrue(all(audit.joinable for audit in audits), [audit.to_json() for audit in audits])
        self.assertEqual(
            self.d.DECLARED_CRITICAL_PAIR_SCOPE,
            "DECLARED_FINITE_CRITICAL_PAIR_SUITE_NOT_GLOBAL_CONFLUENCE",
        )

    def test_job_json_round_trip_is_canonical_and_exact(self) -> None:
        job = self.sample_job()
        decoded = self.d.DAlgebraJob.from_json(json.loads(job.canonical_json()))
        self.assertEqual(decoded, job)
        self.assertEqual(decoded.canonical_json(), job.canonical_json())
        self.assertEqual(decoded.sha256(), job.sha256())
        self.assertEqual(decoded.coefficient.re, Fraction(1, 3))
        self.assertEqual(decoded.coefficient.im, Fraction(2, 5))

    def test_compile_job_preserves_provenance_binding(self) -> None:
        job = self.sample_job()
        result = self.d.compile_job(job)
        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.job_id, job.job_id)
        self.assertEqual(result.notation_hash, job.notation_hash)
        self.assertEqual(result.graph_hash, job.graph_hash)
        self.assertEqual(result.amplitude_id, job.amplitude_id)
        self.assertEqual(result.input_job_sha256, job.sha256())
        self.assertEqual(
            result.critical_pair_scope,
            "DECLARED_FINITE_CRITICAL_PAIR_SUITE_NOT_GLOBAL_CONFLUENCE",
        )
        self.assertEqual(result.canonical_json(), self.d.compile_job(job).canonical_json())
        payload = json.loads(result.canonical_json())
        self.assertEqual(payload["normal_form"]["arithmetic"], "EXACT_Q_I")
        self.assertEqual(result.implementation_status, "PARTIAL_DECLARED_PHASES_ONLY")
        self.assertEqual(result.implemented_phases, self.d.IMPLEMENTED_PHASES)
        self.assertNotIn("AUTOMATIC_ENDPOINT_TRANSFER", result.implemented_phases)
        self.assertNotIn("MULTI_OPERATOR_EXTERNAL_CHIRALITY", result.implemented_phases)

    def test_job_boundary_rejects_unknown_edges_and_legs(self) -> None:
        payload = self.sample_job().to_json()
        payload["operator_word"][0]["tag"]["edge_id"] = "unknown-edge"
        with self.assertRaisesRegex(ValueError, "unknown endpoint"):
            self.d.DAlgebraJob.from_json(payload)

        payload = self.sample_job().to_json()
        payload["operator_word"][-1]["leg_id"] = "unknown-leg"
        with self.assertRaisesRegex(ValueError, "unknown leg"):
            self.d.DAlgebraJob.from_json(payload)

    def test_exact_qi_gaussian_adapter_round_trip(self) -> None:
        source = self.engine.QComplex(Fraction(-7, 9), Fraction(11, 13))
        gaussian = self.d.gaussian_from_qi(source)
        restored = self.d.gaussian_to_qi(gaussian, self.engine.QComplex)
        self.assertEqual(restored, source)

    def test_mixed_external_factor_is_rejected_before_chirality(self) -> None:
        job = self.ambiguous_mixed_external_job()
        source = self.d.Term(job.coefficient, job.operator_word)
        self.assertLess(
            self.d.RULE_PRIORITY["MIXED_ANTICOMMUTATOR"],
            self.d.RULE_PRIORITY["EXTERNAL_LEG_ACTION"],
        )
        with self.assertRaises(self.d.UnimplementedPhaseSequenceError) as captured:
            self.compiler.compile((source,))
        self.assertEqual(captured.exception.code, "UNIMPLEMENTED_PHASE_SEQUENCE")
        self.assertEqual(captured.exception.leg_id, "L0")
        self.assertEqual(captured.exception.operator_types, ("D", "BarD"))

        result = self.d.compile_job(job)
        self.assertEqual(result.status, "UNIMPLEMENTED_PHASE_SEQUENCE")
        self.assertIsNone(result.normal_form)
        self.assertEqual(result.error["code"], "UNIMPLEMENTED_PHASE_SEQUENCE")
        self.assertEqual(
            result.error["required_order"],
            ["MIXED_D_BARD_NORMALIZATION", "EXTERNAL_CHIRALITY"],
        )
        self.assertEqual(result.input_job_sha256, job.sha256())
        self.assertEqual(result.amplitude_id, job.amplitude_id)

    def test_compile_never_invokes_unrestricted_endpoint_transfer(self) -> None:
        original = self.d.transfer_endpoint

        def forbidden(*_args, **_kwargs):
            raise AssertionError("compile invoked unrestricted endpoint transfer")

        self.d.transfer_endpoint = forbidden
        try:
            result = self.d.compile_job(self.sample_job())
        finally:
            self.d.transfer_endpoint = original
        self.assertEqual(result.status, "PASS")
        self.assertEqual(
            result.endpoint_transfer_policy,
            "EXPLICIT_API_ONLY_NEVER_INVOKED_BY_COMPILE",
        )

    def test_single_operator_chirality_jobs_remain_valid(self) -> None:
        external_tag = self.d.EndpointTag("e0", "external")
        chiral = self.d.ExternalLeg("L0", self.d.Chirality.CHIRAL, 0, external_tag)
        trace = self.compiler.compile(
            (self.d.Term(1, (self.d.BarD("+", external_tag, "p"), chiral)),)
        )
        self.assertTrue(trace.terminated)
        self.assertEqual(trace.outputs, ())
        self.assertEqual(trace.implemented_phases, self.d.IMPLEMENTED_PHASES)

    def oracle_adapter(self, momentum):
        engine = self.engine
        operators = engine.flat_operators(momentum)
        sigma_p = engine.sigma_e(momentum)
        identity = operators["identity"]
        zero = operators["zero"]

        def scalar(value):
            return engine.QComplex(value.re, value.im)

        def operator(token):
            if isinstance(token, self.d.D):
                return operators["D_plus" if token.index == "+" else "D_minus"]
            if isinstance(token, self.d.BarD):
                return operators["barD_plus" if token.index == "+" else "barD_minus"]
            if isinstance(token, self.d.D2):
                return operators["D2"]
            if isinstance(token, self.d.BarD2):
                return operators["barD2"]
            if isinstance(token, self.d.MomentumSquare):
                return engine.scale(engine.momentum_square(momentum), identity)
            if isinstance(token, self.d.MixedMomentum):
                indices = {"+": 0, "-": 1}
                component = sigma_p[indices[token.undotted]][indices[token.dotted]]
                return engine.scale(engine.I * component, identity)
            raise TypeError(f"oracle has no map for {token!r}")

        return self.d.MatrixOracleAdapter(
            identity,
            zero,
            engine.add,
            engine.multiply,
            engine.scale,
            scalar,
            operator,
        )

    def assert_matrix_preserved(self, word, momentum=(1, 2, 3, 4)) -> None:
        source = self.d.Term(1, tuple(word))
        trace = self.compiler.compile((source,))
        adapter = self.oracle_adapter(momentum)
        before = self.d.evaluate_terms_with_oracle((source,), adapter)
        after = self.d.evaluate_terms_with_oracle(trace.outputs, adapter)
        self.assertEqual(before, after)

    def test_rewrites_match_existing_exact_16_by_16_matrices(self) -> None:
        words = (
            (
                self.d.D2(self.tag, self.p),
                self.d.BarD2(self.tag, self.p),
                self.d.D2(self.tag, self.p),
            ),
            (
                self.d.BarD2(self.tag, self.p),
                self.d.D2(self.tag, self.p),
                self.d.BarD2(self.tag, self.p),
            ),
            (self.d.D("-", self.tag, self.p), self.d.D("+", self.tag, self.p)),
            (self.d.BarD("-", self.tag, self.p), self.d.BarD("+", self.tag, self.p)),
            (self.d.D("+", self.tag, self.p), self.d.BarD("-", self.tag, self.p)),
        )
        for momentum in ((0, 0, 0, 1), (1, 2, 3, 4), (2, -1, 0, 3)):
            for word in words:
                with self.subTest(momentum=momentum, word=word):
                    self.assert_matrix_preserved(word, momentum)


if __name__ == "__main__":
    unittest.main()
