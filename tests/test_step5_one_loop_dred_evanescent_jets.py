from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/step5_one_loop_dred_evanescent_jets.py"
SPEC = importlib.util.spec_from_file_location("step5_dred_evanescent_jets", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Step5DredEvanescentJetsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.verification = MODULE.build_verification(cls.payload)

    def test_complete_raw_target_census(self) -> None:
        census = self.payload["raw_jet_census"]
        self.assertEqual(census["skeleton_count"], 18)
        self.assertEqual(
            census["target_spin_copies_by_field_strength_degree"],
            {"0": 40, "1": 20, "2": 6, "3": 0},
        )
        self.assertEqual(census["target_spin_copy_count"], 66)
        self.assertEqual(census["maximum_external_vector_derivative_slots"], 4)

    def test_four_sigma_master_identities_componentwise(self) -> None:
        sigma = self.payload["sigma_component_certificate"]
        self.assertEqual(sigma["component_checks_total"], 256)
        self.assertTrue(sigma["all_passed"])
        self.assertTrue(all(sigma["identity_checks"].values()))
        self.assertEqual(sigma["failures"], [])
        self.assertEqual(
            sigma["tilde_delta_contractions"],
            {
                "SIGMA_BAR_SIGMA_LEFT_IDENTITY": "(+2*epsilon) delta_a^b",
                "BAR_SIGMA_SIGMA_RIGHT_IDENTITY": "(+2*epsilon) delta_dota^dotb",
                "SIGMA_SIGMA_EPSILON_DOWN": "(-2*epsilon) epsilon_ab",
                "BAR_SIGMA_BAR_SIGMA_EPSILON_UP": "(-2*epsilon) epsilon^dotadotb",
            },
        )

    def test_antisymmetric_sigma_channels_are_zero(self) -> None:
        channels = self.payload["sigma_component_certificate"]["antisymmetric_channels"]
        self.assertEqual(channels["tilde_delta_mn_sigma_E^mn"], "0")
        self.assertEqual(channels["tilde_delta_mn_bar_sigma_E^mn"], "0")

    def test_source_sym2_projection_is_exact_and_lorentz_scalar(self) -> None:
        source = self.payload["source_Sym2"]
        self.assertEqual(source["projector"], [["1/2", "1/2"], ["1/2", "1/2"]])
        self.assertTrue(source["projector_squared_equals_projector"])
        self.assertEqual(source["rank"], 1)
        self.assertTrue(source["source_has_no_Lorentz_index"])
        self.assertTrue(source["DRED_reduction_commutes_with_Sym2_source_projection"])

    def test_Project_cross_certificates_sharpen_scope(self) -> None:
        cross = self.payload["Project_cross_certificates"]
        self.assertEqual(
            cross["Project_R_weight"]["status"],
            "PASS_PROJECT_U1R_BINDING",
        )
        self.assertEqual(
            cross["Project_R_weight"]["pure_gauge_letter_weights"],
            {"W": 1, "Wtilde": -1, "nabla": -1, "barnabla": 1, "Dcov": 0},
        )
        self.assertEqual(
            cross["source_color"]["status"],
            "PASS_SCOPED_BACKGROUND_SOURCE_AND_COLOR_GATES",
        )
        self.assertFalse(cross["source_color"]["tau_rank_five_color_map_covered"])

    def test_single_projector_channel_partition_exhibits_tau(self) -> None:
        partition = self.payload["single_tilde_index_channel_partition"]
        self.assertEqual(len(partition), 5)
        results = {row["channel"]: row["outcome"] for row in partition}
        self.assertEqual(
            results["CLOSED_SCALAR_SIGMA_TRACE"],
            "SCALAR_2EPSILON_TIMES_EXISTING_JET",
        )
        self.assertEqual(
            results["AT_LEAST_ONE_EXTERNAL_HAT_MOMENTUM_ENDPOINT"],
            "ZERO_BY_TILDE_DELTA_HAT_DELTA_ORTHOGONALITY",
        )
        self.assertEqual(
            results["OPEN_SYMMETRIC_TRACELESS_SIGMA_PAIR"],
            "TAU_(1,1)_RAW_EVANESCENT_TARGET_CANDIDATE",
        )

    def test_contracted_endpoint_subledger_is_exact_but_excludes_tau(self) -> None:
        skeletons = MODULE.enumerate_skeletons()
        copies = MODULE.build_target_copies(skeletons)
        ledger = MODULE.build_placement_ledger(skeletons, copies)
        self.assertEqual(len(ledger), 908)
        counts: dict[str, int] = {}
        for class_name in {row["class"] for row in ledger}:
            counts[str(class_name)] = sum(row["class"] == class_name for row in ledger)
        self.assertEqual(
            counts,
            {
                "CLOSED_SIGMA_MASTER": 264,
                "CLOSED_ANTISYMMETRIC_SIGMA": 132,
                "EXTERNAL_SIGMA_ENDPOINT": 420,
                "TWO_EXTERNAL_ENDPOINTS": 92,
            },
        )
        self.assertTrue(
            all(
                row["normalized_coefficient"] == "0"
                for row in ledger
                if row["class"] != "CLOSED_SIGMA_MASTER"
            )
        )
        subledger = self.payload["contracted_endpoint_subledger"]
        self.assertTrue(subledger["contracted_trace_external_and_antisymmetric_placements_exhausted"])
        self.assertFalse(subledger["open_traceless_tau_placements_included"])

    def test_traceless_tau_split_is_not_an_epsilon_multiple(self) -> None:
        decomposition = self.payload["tilde_decomposition"]
        self.assertEqual(
            decomposition["exact_split"],
            "tilde_delta^mn=(epsilon/2)delta_(4)^mn+tau^mn",
        )
        self.assertEqual(decomposition["tau_trace"], "delta_(4)_mn tau^mn=0")
        self.assertEqual(
            decomposition["tau_norm_squared"],
            "tau_mn tau^mn=2*epsilon-epsilon^2",
        )
        self.assertEqual(decomposition["tau_trace_polynomial"], {})
        self.assertEqual(decomposition["tau_norm_polynomial"], {"1": "2", "2": "-1"})
        self.assertTrue(decomposition["tau_norm_divisible_by_epsilon"])
        self.assertFalse(decomposition["tau_norm_divisible_by_epsilon_squared"])
        self.assertTrue(decomposition["tau_is_not_in_epsilon_times_regular_tensor_module"])

    def test_tau_extended_target_multiplicity_is_229(self) -> None:
        tau = self.payload["raw_traceless_tau_census"]
        self.assertEqual(
            tau["target_spin_copies_by_field_strength_degree"],
            {"0": 150, "1": 66, "2": 12, "3": 1},
        )
        self.assertEqual(tau["raw_target_spin_copy_count"], 229)
        self.assertTrue(tau["representation_multiplicity_exhausted"])
        self.assertEqual(
            [row["tau_target_multiplicity"] for row in tau["spot_checks"]],
            [30, 3, 1],
        )
        self.assertEqual(
            [
                row["traceless_tilde_spurion_target_multiplicity"]
                for degree in ("0", "1", "2", "3")
                for row in self.payload["raw_jet_census"]["skeletons_by_field_strength_degree"][degree]
            ],
            [30, 30, 30, 30, 30, 9, 9, 9, 9, 10, 10, 10, 3, 3, 3, 3, 0, 1],
        )
        witness = tau["explicit_N3_witness"]
        self.assertEqual(witness["vector_derivative_slots"], 0)
        self.assertEqual(witness["physical_target_multiplicity"], 0)
        self.assertEqual(witness["tau_target_multiplicity"], 1)
        self.assertFalse(witness["external_momentum_annihilation_applicable"])
        self.assertFalse(tau["full_index_placement_projector_matrix_built"])

    def test_exact_nonabelian_color_and_grassmann_witness(self) -> None:
        witness = self.payload["raw_traceless_tau_census"]["explicit_N3_witness"]
        color = witness["color_certificate"]
        self.assertTrue(color["source_AB_symmetric"])
        self.assertTrue(color["DE_antisymmetric"])
        self.assertTrue(color["adjoint_invariant"])
        self.assertEqual(color["adjoint_invariance_component_count"], 729)
        self.assertEqual(color["adjoint_invariance_maximum_absolute_residual"], 0)
        self.assertEqual(color["nonzero_entry_count"], 30)
        self.assertEqual(
            color["SU2_AB00_C0_full_DE_contraction"],
            "K^00_(0[DE]) B^[DE]=4*B^12",
        )
        self.assertEqual(
            color["witness_entries"][0],
            {"A": 0, "B": 0, "C": 0, "D": 1, "E": 2, "value": 2},
        )
        grassmann = witness["Grassmann_and_quadratic_jet_certificate"]["Grassmann_exchange"]
        self.assertEqual(grassmann["B_DE_exchange_sign"], -1)
        self.assertEqual(grassmann["K_DE_exchange_sign"], -1)
        self.assertEqual(grassmann["K_DE_times_B_DE_relabel_sign"], 1)
        self.assertTrue(grassmann["antisymmetric_color_contraction_not_killed"])

    def test_explicit_raw_DRED_quadratic_jet_kernel_and_4d_boundary(self) -> None:
        witness = self.payload["raw_traceless_tau_census"]["explicit_N3_witness"]
        certificate = witness["Grassmann_and_quadratic_jet_certificate"]
        quadratic = certificate["quadratic_jet"]
        self.assertEqual(quadratic["field_strength_degree"], 3)
        self.assertEqual(quadratic["minimum_background_connection_degree"], 3)
        self.assertEqual(quadratic["second_derivative_at_t_zero"], 0)
        self.assertEqual(quadratic["third_derivative_at_t_zero"], 6)
        self.assertTrue(quadratic["raw_DRED_kernel_counterexample"])
        boundary = certificate["quotient_boundary"]
        self.assertEqual(
            boundary["full_DRED_raw_source_module_injectivity"],
            "FAIL_EXPLICIT_KERNEL",
        )
        self.assertEqual(
            boundary["background_CE_covariant_submodule_injectivity"],
            "FAIL_EXPLICIT_KERNEL",
        )
        self.assertTrue(boundary["physical_4d_quotient_sets_tau_to_zero"])
        self.assertFalse(boundary["physical_4d_injectivity_refuted_by_this_witness"])
        self.assertEqual(boundary["full_quantum_BV_cohomology_class_of_witness"], "OPEN")

    def test_separated_internal_sigma_pair_has_exact_sign(self) -> None:
        rows = self.payload["separated_internal_sigma_reduction"]["rows"]
        self.assertEqual(
            [row["exact_reduction"] for row in rows],
            [
                "+2*epsilon times original_hat_sigma_word",
                "-2*epsilon times original_hat_sigma_word",
                "+2*epsilon times original_hat_sigma_word",
                "-2*epsilon times original_hat_sigma_word",
                "+2*epsilon times original_hat_sigma_word",
            ],
        )

    def test_multiple_projector_insertions_reduce_by_idempotence(self) -> None:
        multiple = self.payload["multiple_tilde_insertions"]
        self.assertEqual(len(multiple["finite_exact_power_witnesses"]), 8)
        self.assertTrue(
            all(
                row["open_chain"] == "tilde_delta"
                and row["closed_trace"] == "2*epsilon"
                for row in multiple["finite_exact_power_witnesses"]
            )
        )
        self.assertTrue(multiple["induction_uses_idempotence"])
        self.assertTrue(
            multiple["fully_contracted_nonempty_closed_network_has_coefficient_in_ideal_(epsilon)"]
        )
        self.assertTrue(multiple["does_not_reduce_open_tau_tensor"])

    def test_contracted_sparse_presentation_has_no_new_free_direction(self) -> None:
        presentation = self.payload["module_presentation"]
        scalar_map = presentation["raw_scalar_sigma_map"]
        self.assertEqual(
            (scalar_map["rows"], scalar_map["columns"], scalar_map["nnz"], scalar_map["exact_rank"]),
            (66, 264, 264, 66),
        )
        generators = presentation["presentation_generators"]
        relations = presentation["presentation_relations"]
        self.assertEqual(generators["total"], 776)
        self.assertEqual(relations["total"], 710)
        self.assertEqual(relations["exact_row_rank"], 710)
        self.assertEqual(
            (relations["matrix"]["rows"], relations["matrix"]["columns"], relations["matrix"]["nnz"]),
            (710, 776, 776),
        )
        self.assertEqual(presentation["quotient_free_rank_per_Sym2_color_generator"], 66)
        self.assertEqual(presentation["new_independent_evanescent_free_rank_in_this_submodule"], 0)
        self.assertTrue(presentation["does_not_present_open_traceless_tau_sector"])

    def test_epsilon_torsion_is_only_in_the_quotient(self) -> None:
        torsion = self.payload["module_presentation"]["torsion_statement"]
        self.assertTrue(torsion["M_phys_is_epsilon_torsion_free"])
        self.assertTrue(torsion["quotient_is_epsilon_torsion"])
        self.assertEqual(
            torsion["localized_pole_mixing_identity"],
            "epsilon^(-1) * (2*epsilon*P_i) = 2*P_i",
        )
        self.assertFalse(torsion["loop_or_anomaly_coefficient_computed"])

    def test_gate_scope_is_fail_closed(self) -> None:
        verdict = self.payload["verdict"]
        self.assertEqual(
            verdict["M_DRED_EVANESCENT_JETS"],
            "FAIL_EXPLICIT_FULL_DRED_QUADRATIC_JET_KERNEL",
        )
        self.assertEqual(verdict["full_DRED_raw_source_module_injectivity"], "FAIL_EXPLICIT_KERNEL")
        self.assertEqual(
            verdict["background_CE_covariant_submodule_injectivity"],
            "FAIL_EXPLICIT_KERNEL",
        )
        self.assertEqual(verdict["explicit_raw_kernel_dimension_lower_bound_for_SU2"], 1)
        self.assertFalse(verdict["physical_4d_injectivity_refuted_by_this_witness"])
        self.assertEqual(verdict["full_quantum_BV_cohomology_class_of_witness"], "OPEN")
        self.assertEqual(verdict["raw_traceless_tau_target_directions"], 229)
        self.assertEqual(verdict["post_quotient_independent_evanescent_tensor_directions"], "BLOCKED")
        self.assertEqual(
            verdict["coupled_open_gates"],
            [
                "EXHAUSTIVE_TAU_EOM_IBP_QUOTIENT_MATRIX",
                "FULL_QUANTUM_BV_ST_SOURCE_COMPLEX",
            ],
        )
        self.assertEqual(
            self.payload["scope"]["physical_Project_U1R_binding"],
            "PASS_BY_PROJECT_R_WEIGHT_CERTIFICATE",
        )

    def test_all_verification_checks_pass(self) -> None:
        self.assertTrue(
            self.verification["all_passed"],
            [name for name, passed in self.verification["checks"].items() if not passed],
        )
        self.assertEqual(
            self.verification["status"],
            "PASS_EXACT_EXPLICIT_FULL_DRED_KERNEL_PHYSICAL4D_UNTOUCHED",
        )

    def test_generator_is_byte_deterministic(self) -> None:
        paths = [
            ROOT / "generated/step5/one-loop-dred-evanescent-jets.json",
            ROOT / "audits/step5-one-loop-dred-evanescent-jets-verification.json",
            ROOT / "audits/step5-one-loop-dred-evanescent-jets.md",
        ]
        before = [path.read_bytes() for path in paths]
        subprocess.run([sys.executable, str(MODULE_PATH)], cwd=ROOT, check=True, capture_output=True)
        after = [path.read_bytes() for path in paths]
        self.assertEqual(before, after)
        payload = json.loads(paths[0].read_text())
        verification = json.loads(paths[1].read_text())
        self.assertEqual(verification["payload_sha256"], MODULE.canonical_sha256(payload))


if __name__ == "__main__":
    unittest.main()
