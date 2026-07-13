from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_reflection_quotient_audit.py"
OUTPUT = ROOT / "generated/step5/one-loop-reflection-quotient-audit.json"
AUDIT = ROOT / "audits/step5-one-loop-reflection-quotient-verification.json"
REPORT = ROOT / "audits/step5-one-loop-reflection-quotient-audit.md"


def load_module():
    specification = importlib.util.spec_from_file_location(
        "step5_one_loop_reflection_quotient_test_binding", SCRIPT
    )
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load reflection quotient audit")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5OneLoopReflectionQuotientAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        cls.payload = json.loads(OUTPUT.read_text())

    def test_epsilon_matrices_and_variance_are_exact(self) -> None:
        epsilon = self.payload["epsilon"]
        self.assertEqual(epsilon["epsilon_up"], [[0, 1], [-1, 0]])
        self.assertEqual(epsilon["epsilon_down"], [[0, -1], [1, 0]])
        self.assertEqual(epsilon["W_down_Y_up"], epsilon["Y_up_W_down"])
        self.assertEqual(epsilon["Y_down_W_up"], -epsilon["W_down_Y_up"])

    def test_local_bosonic_seed_is_in_sym2_adjoint(self) -> None:
        source = self.payload["source_quotient"]
        self.assertEqual(source["X_parity"], 0)
        self.assertEqual(source["AB_normal_form"], source["BA_normal_form"])
        self.assertEqual(source["physical_color_space"], "Sym^2(Adj)")
        self.assertEqual(source["momentum_exchange_rule"], "(A,p1)<->(B,p2)")
        self.assertEqual(source["insertion_parity"], 1)
        self.assertEqual(source["required_source_coupling_parity"], 1)
        self.assertEqual(source["coupled_source_vertex_parity"], 0)
        self.assertEqual(
            source["current_graphir_source_statistics"],
            {"DIRECT": "FERMION", "REFLECTED": "FERMION"},
        )
        self.assertEqual(
            source["current_graphir_source_type_verdict"], "REPAIRED_FERMION"
        )
        self.assertEqual(
            source["current_graphir_source_color_variances"],
            {"DIRECT": ["DOWN", "DOWN"], "REFLECTED": ["DOWN", "DOWN"]},
        )
        for port in source["source_port_semantics"].values():
            self.assertEqual(port["attached_vertex_kind"], "COMPOSITE_INSERTION_I2_WW")
            self.assertTrue(port["verdict"].startswith("J_LEG;"))

    def test_graphir_keeps_the_same_order_in_both_orientations(self) -> None:
        orientation = self.payload["orientation"]
        self.assertEqual(
            orientation["ordered_vertex_kinds"]["DIRECT"],
            orientation["ordered_vertex_kinds"]["REFLECTED"],
        )
        self.assertEqual(
            orientation["graphir_external_words"],
            {
                "DIRECT": ["TildeW_dot_alpha", "W_plus"],
                "REFLECTED": ["TildeW_dot_alpha", "W_plus"],
            },
        )
        self.assertEqual(
            orientation["derived_fixed_vertex_order_signs"],
            {"DIRECT": 1, "REFLECTED": 1},
        )

    def test_specialized_full_sign_replays_both_odd_subwords(self) -> None:
        specialized = self.payload["orientation"]["specialized_sign_audits"]
        self.assertEqual(specialized["REFLECTED"]["total_orientation_sign"], 1)
        self.assertEqual(
            specialized["REFLECTED"]["declared_pre_D_word"], ["W", "TildeW"]
        )
        self.assertEqual(
            specialized["REFLECTED"]["external_fermion_permutation_sign"], -1
        )
        self.assertEqual(
            specialized["REFLECTED"]["quantum_odd_word_permutation_sign"], -1
        )
        self.assertEqual(specialized["REFLECTED"]["D_transfer"]["product"], 1)
        self.assertEqual(
            self.payload["acceptance_status"],
            "PASS_REFLECTION_SOURCE_DERIVATIVE_TYPE_GATES_CONTACT_REPLAY_OPEN",
        )

    def test_full_odd_word_replay_cancels_external_only_minus(self) -> None:
        replay = self.payload["orientation"]["graded_block_replay"]
        self.assertEqual(
            replay["direct_full_word"], ["TildeW", "Q_barD", "W", "Q_D"]
        )
        self.assertEqual(
            replay["reflected_full_block_word"],
            ["W", "Q_D", "TildeW", "Q_barD"],
        )
        self.assertEqual(replay["full_word_inversions"], 4)
        self.assertEqual(replay["full_word_sign"], 1)
        self.assertEqual(replay["external_only_sign"], -1)
        self.assertEqual(replay["quantum_only_sign"], -1)
        self.assertIn(
            "their product is the full reflected sign",
            replay["specialized_compiler_status"],
        )

    def test_current_minus_is_antisymmetric_and_sym2_projection_is_zero(self) -> None:
        current = self.payload["color_and_projection"]["rejected_external_only_minus"]
        self.assertEqual(current["AB_coefficients"], {"S_DE": 1, "S_ED": -1})
        self.assertEqual(
            current["BA_coefficients_after_dummy_relabelling"],
            {"S_DE": -1, "S_ED": 1},
        )
        self.assertEqual(current["Sym2_projection"], {"S_DE": "0", "S_ED": "0"})
        self.assertEqual(current["verdict"], "KILLED_BY_PHYSICAL_SYM2_QUOTIENT")

    def test_required_plus_is_symmetric_and_survives_sym2(self) -> None:
        corrected = self.payload["color_and_projection"]["repaired_plus"]
        self.assertEqual(corrected["AB_coefficients"], {"S_DE": 1, "S_ED": 1})
        self.assertEqual(
            corrected["BA_coefficients_after_dummy_relabelling"],
            corrected["AB_coefficients"],
        )
        self.assertEqual(corrected["Sym2_projection"], {"S_DE": "1", "S_ED": "1"})
        self.assertIn(
            "+mathcalD_+^(dot_a)X^D*TildeW^E_dot_a", corrected["operator_word"]
        )

    def test_external_derivative_is_vector_typed(self) -> None:
        typed = self.payload["derivative_type_audit"]
        self.assertEqual(typed["spinor_derivative"]["parity"], 1)
        self.assertFalse(typed["spinor_derivative"]["dotted_output_allowed"])
        self.assertEqual(typed["vector_derivative"]["parity"], 0)
        self.assertEqual(typed["D_algebra_external_token"], "i*p_(a dot_b)*W_plus")
        self.assertEqual(
            typed["covariant_completion"], "Y^(A dot_a)=mathcalD_+^(dot_a)X^A"
        )
        self.assertEqual(
            typed["legacy_verdict"],
            "TYPE_INVALID_DOTTED_OUTPUT_ON_UNDOTTED_SPINOR_DERIVATIVE",
        )

    def test_tildeW_port_must_be_lower_dotted(self) -> None:
        typed = self.payload["dotted_port_type_audit"]
        self.assertEqual(typed["locked_cubic_port"], "TildeW_dot_a*barD^(dot_a)")
        self.assertEqual(typed["required_tildeW_variance"], "DOWN")
        self.assertEqual(typed["required_vector_derivative_variance"], "UP")
        self.assertEqual(
            typed["current_graphir_tildeW_slots"],
            {
                "DIRECT": {"label": "dot_alpha", "variance": "DOWN"},
                "REFLECTED": {"label": "dot_alpha", "variance": "DOWN"},
            },
        )
        self.assertEqual(
            typed["verdict"], "GRAPHIR_TILDEW_VARIANCE_REPAIRED_DOWN"
        )

    def test_findings_are_fail_closed_and_no_coefficient_is_claimed(self) -> None:
        findings = {item["code"]: item for item in self.payload["findings"]}
        self.assertEqual(findings["REFLECTED_FULL_ODD_WORD_SIGN_REPAIRED"]["status"], "CLOSED")
        self.assertEqual(findings["TYPED_CONTACT_REPLAY_AFTER_REPAIR"]["status"], "OPEN")
        self.assertEqual(findings["WW_SOURCE_STATISTICS_REPAIRED_FERMION"]["status"], "CLOSED")
        self.assertEqual(findings["COVARIANT_VECTOR_DERIVATIVE_TOKEN_REPAIRED"]["status"], "CLOSED")
        self.assertEqual(findings["TILDEW_DOTTED_VARIANCE_REPAIRED_DOWN"]["status"], "CLOSED")
        self.assertEqual(
            self.payload["coefficient_status"], "NOT_EVALUATED_BY_THIS_AUDIT"
        )

    def test_exact_checks_and_verification_pass_as_an_audit(self) -> None:
        self.assertEqual(self.payload["totals"], {"exact": 26, "passed": 26, "failed": 0})
        audit = json.loads(AUDIT.read_text())
        self.assertEqual(audit["status"], "PASS_TYPED_REPAIR_WITH_CONTACT_REPLAY_OPEN")
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertIn(
            "PASS\\_REFLECTION\\_SOURCE\\_DERIVATIVE\\_TYPE\\_GATES",
            REPORT.read_text(),
        )

    def test_regeneration_is_byte_reproducible(self) -> None:
        paths = (OUTPUT, AUDIT, REPORT)
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        after = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
