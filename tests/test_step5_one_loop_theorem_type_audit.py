from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts import step5_one_loop_theorem_type_audit as module


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_one_loop_theorem_type_audit.py"


class Step5OneLoopTheoremTypeAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.build_payload()

    def test_all_exact_checks_pass(self) -> None:
        self.assertTrue(
            all(self.payload["checks"].values()),
            [name for name, passed in self.payload["checks"].items() if not passed],
        )
        self.assertEqual(
            self.payload["status"], "PASS_EXACT_TYPES_WITH_OPEN_THEOREM_GATES"
        )
        self.assertFalse(self.payload["external_coefficients_imported"])

    def test_connection_degrees_separate_seed_and_candidate(self) -> None:
        certificate = self.payload["connection_degree"]
        self.assertEqual(
            certificate["seed=nabla_minus_X_tensor_X"], [2, 3, 4, 5, 6, 7]
        )
        self.assertEqual(
            certificate["candidate=tildeW_times_DX"], [2, 3, 4, 5, 6]
        )

    def test_source_measure_dual_sign_and_open_representation(self) -> None:
        source = self.payload["source_and_BRST_dual"]
        self.assertEqual(
            source["ordered_graph_carrier"],
            "Adjoint tensor Adjoint with A|B order",
        )
        self.assertEqual(
            source["physical_local_seed_subspace"], "Sym^2(Adjoint)"
        )
        self.assertEqual(
            source["ordered_to_local_quotient"], "OPEN_COLOR_WORD_QUOTIENT"
        )
        self.assertEqual(source["measure"], "E_FULL_SUPERSPACE_d8z")
        self.assertEqual(source["source_dimension"], "-5/2")
        self.assertEqual(source["source_R_weight"], 1)
        self.assertEqual(source["R_weight_status"], "TEMPORARY_FORMAL_GRADING")
        self.assertEqual(source["Project_U1R_binding"], "OPEN")
        self.assertEqual(source["source_parity"], 1)
        self.assertEqual(source["odd_Leibniz_sign"], -1)
        self.assertEqual(source["invariant_pairing_coefficient"], 0)
        self.assertEqual(source["source_extended_BV_closure"], "OPEN")

    def test_literal_dotted_index_positions_and_color_exchange(self) -> None:
        color = self.payload["open_color_and_dotted_index"]
        self.assertEqual(
            color["Y_upper_W_lower_coefficients"], [0, -1, 1, 0]
        )
        self.assertEqual(
            color["W_lower_Y_upper_coefficients"], [0, -1, 1, 0]
        )
        self.assertEqual(
            color["Y_lower_W_upper_coefficients"], [0, 1, -1, 0]
        )
        self.assertTrue(color["lower_upper_is_minus_upper_lower"])
        self.assertEqual(color["seed_exchange_symmetry"], "SYMMETRIC_AB")
        self.assertEqual(
            color["literal_candidate_open_exchange"], "ANTISYMMETRIC_AB"
        )
        self.assertEqual(color["literal_candidate_Sym2_projection"], "ZERO")
        self.assertEqual(
            color["ordered_A_bar_B_to_local_Sym2"],
            "OPEN_COLOR_WORD_QUOTIENT",
        )

    def test_injective_completion_is_not_rank_one_theorem(self) -> None:
        theorem = self.payload["completion_theorem"]
        self.assertFalse(
            theorem["general_injective_completion"]["rank_one_required"]
        )
        self.assertEqual(
            theorem["rank_one_candidate_channel_corollary"]["status"], "OPEN"
        )
        self.assertEqual(
            theorem["pure_gauge_kernel_route"]["filtration_lemma"], "OPEN"
        )

    def test_hessian_spin_ward_and_bridge_gates(self) -> None:
        self.assertEqual(
            self.payload["hessian_census"]["polarized_counts"],
            {"2": 6, "3": 26, "4": 150},
        )
        self.assertEqual(
            self.payload["spin_projector"]["component_identity"],
            "U_-;++++=H_-++++-(4/5)t_+++",
        )
        self.assertEqual(
            self.payload["spin_projector"]["j_five_halves_removal"],
            "CLOSED_EXACT",
        )
        self.assertEqual(
            self.payload["spin_projector"]["tree_EOM_identity"],
            "CLOSED_EXACT_AT_TREE_LEVEL",
        )
        self.assertEqual(self.payload["spin_projector"]["quantum_gates"], "OPEN")
        self.assertEqual(self.payload["Ward_recursion"]["frame"], "GAUGE_CHIRAL")
        self.assertFalse(
            self.payload["Ward_recursion"]["vector_subgroup_level_mixing"]
        )
        self.assertEqual(
            self.payload["frame_bridge"]["Step5A_primary_frame"],
            "GAUGE_VECTOR_NO_CHANGE_OF_VARIABLES_REQUIRED",
        )
        self.assertEqual(self.payload["frame_bridge"]["operator_similarity"], "PASS")
        self.assertEqual(
            self.payload["frame_bridge"]["quadratic_supertrace_similarity_sector"],
            "PASS",
        )
        self.assertEqual(
            self.payload["frame_bridge"]["full_physical_ghost_nonminimal_jacobian"],
            "OPEN_3D109A",
        )
        self.assertEqual(
            self.payload["frame_bridge"]["full_finite_bv_density_and_cycle"],
            "OPEN_STEP5C_3D110",
        )
        self.assertEqual(
            self.payload["frame_bridge"][
                "independent_flat_measure_functional_equality"
            ],
            "NOT_ASSERTED",
        )

    def test_step5a_and_step5c_gates_are_separate(self) -> None:
        self.assertIn(
            "STEP5A_LOCAL_BACKGROUND_WARD_RESTORATION",
            self.payload["open_theorem_gates"],
        )
        self.assertIn(
            "PROJECT_R_WEIGHT_BINDING",
            self.payload["open_theorem_gates"],
        )
        self.assertNotIn(
            "FINITE_BV_DENSITY", self.payload["open_theorem_gates"]
        )
        self.assertEqual(
            self.payload["step5C_only_gates"],
            ["FINITE_BV_DENSITY", "FULL_FUNCTIONAL_FRAME_JACOBIAN"],
        )

    def test_artifacts_are_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        generated_first = module.GENERATED.read_bytes()
        audit_first = module.AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, module.GENERATED.read_bytes())
        self.assertEqual(audit_first, module.AUDIT.read_bytes())
        payload = json.loads(generated_first)
        audit = json.loads(audit_first)
        self.assertEqual(payload, self.payload)
        self.assertEqual(audit["status"], payload["status"])
        self.assertEqual(audit["failed"], [])
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(generated_first).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
