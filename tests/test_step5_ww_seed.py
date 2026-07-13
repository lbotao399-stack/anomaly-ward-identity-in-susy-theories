from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ww_seed.py"
OUTPUT = ROOT / "generated/step5/ww-seed-graph-ir.json"
AUDIT = ROOT / "audits/step5-ww-seed-verification.json"


def load_module():
    specification = importlib.util.spec_from_file_location("step5_ww_seed", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load WW seed generator")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5WWSeedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.seed = load_module()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        cls.payload = json.loads(OUTPUT.read_text())

    def test_two_actual_physical_orientations_have_exact_routing(self) -> None:
        self.assertEqual(set(self.payload["graphs"]), {"DIRECT", "REFLECTED"})
        for orientation in ("DIRECT", "REFLECTED"):
            graph = self.seed.physical_triangle(orientation)
            self.assertTrue(graph.validate_linear_momentum_routing()["passed"])
            self.assertEqual(graph.loop_momenta, ("k",))
            self.assertEqual(
                dict(graph.metadata)["denominator"],
                "k^2*(k+q)^2*(k+p+q)^2",
            )
            self.assertEqual(dict(graph.metadata)["bare_numerator_contains_epsilon"], "false")

    def test_eight_exact_rows_per_orientation(self) -> None:
        expected_endpoints = {("e0", "e1"), ("e0", "e2"), ("e1", "e1"), ("e1", "e2")}
        for orientation in ("DIRECT", "REFLECTED"):
            rows = self.payload["traces"][orientation]
            self.assertEqual(len(rows), 8)
            for placement in ("LEFT_LETTER", "RIGHT_LETTER"):
                selected = [row for row in rows if row["D_minus_placement"] == placement]
                self.assertEqual(
                    {(row["barD_endpoint"]["edge"], row["D_endpoint"]["edge"]) for row in selected},
                    expected_endpoints,
                )
            for row in rows:
                self.assertEqual(row["exact_D_chain"]["product"], "-1/2")
                self.assertEqual(
                    row["row_prefactor"],
                    "+g^2/16" if orientation == "DIRECT" else "-g^2/16",
                )
                self.assertTrue(all(row["exact_checks"].values()), row)
                self.assertEqual(row["classification"], "ORDINARY_UV_POLE")
                self.assertTrue(row["external_leg_derivative_tokens"])

    def test_rows_are_bound_to_existing_exact_grassmann_engine(self) -> None:
        binding = self.payload["exact_matrix_binding"]
        self.assertEqual(binding["engine"], "exact 16x16 exterior-algebra matrices over Q(i)")
        self.assertEqual(binding["failed"], 0)
        self.assertEqual(
            set(binding["groups"]),
            {
                "delta_normalization",
                "Project_K_plus_chain",
                "edge_endpoint_transfer",
                "mixed_anticommutators",
                "affine_routing",
            },
        )
        self.assertTrue(
            all(
                value
                for group in binding["groups"].values()
                for value in group.values()
            )
        )

    def test_sd_edge_collapses_are_actual_graph_ir_children(self) -> None:
        for orientation in ("DIRECT", "REFLECTED"):
            children = self.payload["SD_collapsed_children"][orientation]
            self.assertEqual(len(children), 3)
            self.assertEqual(
                {child["metadata"]["collapsed_edge_id"] for child in children},
                {"e0", "e1", "e2"},
            )
            self.assertTrue(all(child["metadata"]["graph_relation"] == "CONTACT_CHILD" for child in children))

    def test_triangle_and_contact_poles_form_exact_metric_mismatch(self) -> None:
        poles = self.payload["poles"]
        self.assertEqual(poles["triangle_status"], "DERIVED_ISOLATED_TRIANGLE_ORDINARY_UV_POLE")
        self.assertIn("+g^2/(128*pi^2*epsilon)", poles["triangle_poles"]["DIRECT"])
        self.assertIn("-g^2/(128*pi^2*epsilon)", poles["triangle_poles"]["REFLECTED"])
        self.assertIn("-g^2/(128*pi^2*epsilon)", poles["contact_poles"]["DIRECT"])
        self.assertIn("+g^2/(128*pi^2*epsilon)", poles["contact_poles"]["REFLECTED"])
        self.assertEqual(
            poles["contact_status"],
            "AGGREGATE_SD_IDENTITY_NOT_BASIS_RESOLVED",
        )
        self.assertTrue(poles["missing_rule_is_not_finite_BV"])
        self.assertTrue(poles["metric_mismatch_proved_at_aggregate_sd_level"])
        self.assertFalse(poles["full_ordinary_triangle_bubble_cancellation_proved"])
        self.assertEqual(poles["anomaly_coefficient_fixed_orientation"], "+g^2/(64*pi^2)")
        self.assertEqual(
            poles["anomaly_coefficients"],
            {"DIRECT": "+g^2/(64*pi^2)", "REFLECTED": "-g^2/(64*pi^2)"},
        )
        self.assertEqual(
            poles["two_orientation_single_color_tensor"],
            "g^2/(64*pi^2)*c_{ACD}c_{BCE}*(i*p_+^dot_alpha)*"
            "[TildeW_dot_alpha^D*X^E-X^D*TildeW_dot_alpha^E]",
        )
        self.assertEqual(
            poles["anomaly_status"],
            "DERIVED_AGGREGATE_SD_CANDIDATE_NOT_ACCEPTED",
        )
        self.assertEqual(poles["post_D_external_operator"], "X^E=nabla_+ W_+^E")

    def test_every_row_has_one_exact_aggregate_metric_contact_child(self) -> None:
        for orientation in ("DIRECT", "REFLECTED"):
            rows = self.payload["traces"][orientation]
            children = self.payload["SD_metric_contact_children"][orientation]
            self.assertEqual(len(children), 8)
            self.assertEqual(
                {child["metadata"]["parent_trace_id"] for child in children},
                {row["trace_id"] for row in rows},
            )
            for child in children:
                metadata = child["metadata"]
                self.assertEqual(metadata["graph_relation"], "SD_AGGREGATE_METRIC_CONTACT")
                self.assertEqual(
                    metadata["unsigned_scalar_pole"],
                    "g^2/(1024*pi^2*epsilon)",
                )
                self.assertEqual(
                    metadata["contact_amplitude_sign"],
                    "-1" if orientation == "DIRECT" else "1",
                )
                self.assertEqual(metadata["contact_metric"], "delta4^(mu nu)")

    def test_reflection_sign_is_external_koszul_not_internal_wick(self) -> None:
        audits = self.payload["external_orientation_sign_audits"]
        direct = audits["DIRECT"]
        reflected = audits["REFLECTED"]
        self.assertEqual(direct["declared_pre_D_word"], ["TildeW", "W"])
        self.assertEqual(reflected["declared_pre_D_word"], ["W", "TildeW"])
        self.assertEqual(direct["external_fermion_permutation_sign"], 1)
        self.assertEqual(reflected["external_fermion_permutation_sign"], -1)
        self.assertEqual(direct["D_transfer"]["IBP_outer_sign"], -1)
        self.assertEqual(direct["D_transfer"]["graded_Leibniz_prefix_sign"], -1)
        self.assertEqual(direct["D_transfer"]["product"], 1)
        self.assertEqual(reflected["D_transfer"]["product"], 1)
        self.assertEqual(direct["total_orientation_sign"], 1)
        self.assertEqual(reflected["total_orientation_sign"], -1)
        self.assertEqual(dict(self.seed.physical_triangle("DIRECT").metadata)["wick_sign"], "+1")
        self.assertEqual(dict(self.seed.physical_triangle("REFLECTED").metadata)["wick_sign"], "+1")
        self.assertEqual(
            dict(self.seed.physical_triangle("REFLECTED").metadata)[
                "external_fermion_permutation_sign"
            ],
            "-1",
        )

    def test_composite_port_basis_is_complete_but_individual_split_is_not_claimed(self) -> None:
        basis = self.payload["contact_basis_catalogue"]
        self.assertEqual(
            basis["counts"],
            {
                "NONLINEAR_I3": 30,
                "ACTION_S3_ANTICHIRAL": 6,
                "QUARTIC_I4_TADPOLE": 180,
            },
        )
        self.assertEqual(len(basis["all_basis_term_ids"]), 216)
        self.assertEqual(
            len(basis["all_basis_term_ids"]),
            len(set(basis["all_basis_term_ids"])),
        )
        self.assertTrue(
            all(
                item["classification"] == "ORDERED_PORT_BASIS_TERM_NOT_GRAPH"
                for family in basis["families"].values()
                for item in family
                if item["family"] != "QUARTIC_I4_TADPOLE"
            )
        )
        self.assertEqual(basis["individual_decomposition"], "BASIS_DEPENDENT")
        self.assertEqual(
            basis["mixed_S4_typed_zero"]["status"],
            "PROVED_ABSENT_BY_INTRINSIC_EUCLIDEAN_CHIRAL_SECTOR",
        )
        self.assertEqual(
            basis["legal_two_vertex_contact_family"]["status"],
            "INSTANTIATED_AS_TWO_DISTINCT_VERTICES",
        )
        self.assertEqual(
            basis["exact_aggregate_rule"],
            "sum_(ordered basis terms in one trace) C_term = +g^2/(1024*pi^2*epsilon)",
        )

    def test_regeneration_is_byte_reproducible(self) -> None:
        first = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (
                OUTPUT,
                AUDIT,
                ROOT / "generated/step5/ww-seed-dalgebra.csv",
                ROOT / "generated/step5/ww-seed-dalgebra.md",
                ROOT / "generated/step5/ww-seed-direct.dot",
                ROOT / "generated/step5/ww-seed-reflected.dot",
                ROOT / "generated/step5/ww-seed-contact-direct.tex",
                ROOT / "generated/step5/ww-seed-contact-reflected.tex",
            )
        }
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in first}
        self.assertEqual(first, second)
        audit = json.loads(AUDIT.read_text())
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["failed"], 0)

    def test_gap_audit_records_the_open_basis_resolved_contact_orbit(self) -> None:
        text = (ROOT / "audits/step5-ww-seed-gap-audit.md").read_text()
        self.assertIn("Unresolved \\(P0/P1\\): \\(1\\)", text)
        self.assertIn("ORDERED_PORT_BASIS_TERM_NOT_GRAPH", text)
        self.assertIn("| G4 | G-ALG |", text)

    def test_publication_contact_figures_bind_to_trace_families(self) -> None:
        direct = (ROOT / "generated/step5/ww-seed-contact-direct.tex").read_text()
        reflected = (ROOT / "generated/step5/ww-seed-contact-reflected.tex").read_text()
        self.assertIn("DA-D-001--008", direct)
        self.assertIn("DA-R-001--008", reflected)
        self.assertIn("I_{(3)}", direct)
        self.assertIn("\\widetilde S_{(3)}", reflected)


if __name__ == "__main__":
    unittest.main()
