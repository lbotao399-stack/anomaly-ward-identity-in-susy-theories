from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step6_two_loop_ghost_census.py"
OUTPUT = ROOT / "generated/step6/two-loop-ghost-census/census.json"
AUDIT = ROOT / "audits/step6-two-loop-ghost-census-verification.json"


def load_module():
    specification = importlib.util.spec_from_file_location("step6_two_loop_ghost_census", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load Step-6 two-loop ghost census")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step6TwoLoopGhostCensusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_generator_is_exactly_reproducible(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_output = OUTPUT.read_bytes()
        first_audit = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(first_output, OUTPUT.read_bytes())
        self.assertEqual(first_audit, AUDIT.read_bytes())
        audit = json.loads(first_audit)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"]["failed"], 0)

    def test_FP_candidates_have_exact_species_and_counts(self) -> None:
        payload = self.module.build_payload()
        fp = payload["FP"]
        self.assertEqual(fp["classification"], "ADMITTED_UNCOMPUTED")
        self.assertEqual(fp["candidate_count"], 10)
        self.assertEqual(fp["topology_counts"], {"I2_FP_V1_FP_V1": 6, "I2_FP_V2": 4})
        families = {
            tuple(vertex.source_monomial_id for vertex in candidate.vertices[1:])
            for candidate in self.module.enumerate_fp_candidates()
        }
        self.assertEqual(
            families,
            {
                ("fp_plus_tilde_c_v2",),
                ("fp_minus_c_v2",),
                ("fp_plus_tilde_c_v1", "fp_plus_tilde_c_v1"),
                ("fp_minus_c_v1", "fp_minus_c_v1"),
                ("fp_minus_tilde_c_v1", "fp_plus_c_v1"),
            },
        )

    def test_every_admitted_graph_is_port_complete_connected_L2_and_1PI(self) -> None:
        candidates = self.module.enumerate_fp_candidates() + self.module.enumerate_matter_candidates()
        self.assertTrue(candidates)
        for candidate in candidates:
            with self.subTest(candidate=candidate.candidate_id):
                self.assertEqual(candidate.classification, "ADMITTED_UNCOMPUTED")
                self.assertTrue(candidate.connected)
                self.assertEqual(candidate.loop_number, 2)
                self.assertTrue(candidate.one_particle_irreducible)
                self.assertTrue(all(flag for _, flag in candidate.deletion_connected))
                self.assertTrue(all(count == 1 for _, count in candidate.port_conservation))

    def test_all_FP_species_multisets_receive_a_machine_classification(self) -> None:
        rows = self.module.fp_structural_family_census()
        self.assertEqual(len(rows), 14)
        self.assertEqual(sum(row["classification"] == "ADMITTED_UNCOMPUTED" for row in rows), 5)
        self.assertEqual(sum(row["classification"] == "PROVED_ABSENT_AT_THIS_ORDER" for row in rows), 9)
        absent = [row for row in rows if row["classification"] == "PROVED_ABSENT_AT_THIS_ORDER"]
        self.assertTrue(all(row["negative_witness"] for row in absent))
        self.assertEqual(
            {row["negative_witness"] for row in absent},
            {
                "NO_BIJECTION_BETWEEN_TYPED_ANTIGHOST_AND_GHOST_PORTS",
                "EVERY_TYPED_GHOST_MATCHING_LEAVES_AN_INTERNAL_BRIDGE",
            },
        )

    def test_NK_absence_is_a_typed_cut_not_a_global_determinant_claim(self) -> None:
        payload = self.module.build_payload()
        nk = payload["NK"]
        self.assertEqual(nk["classification"], "PROVED_ABSENT_AT_THIS_ORDER")
        self.assertEqual(nk["scope"], "REFERENCE_FLAT_STEP5A_FIXED_GAUGE_ONLY")
        self.assertEqual(nk["interaction_vertices_with_V"], [])
        self.assertEqual(nk["cut_witness"]["mixed_propagators"], [])
        self.assertEqual(nk["cut_witness"]["mixed_vertices"], [])
        self.assertIn("No equality", nk["nonclaim"])

    def test_matter_is_admitted_but_outside_the_pure_gauge_subsector(self) -> None:
        payload = self.module.build_payload()
        matter = payload["MATTER"]
        self.assertEqual(matter["classification"], "ADMITTED_UNCOMPUTED")
        self.assertEqual(matter["scope_relation"], "OUTSIDE_CURRENT_PURE_GAUGE_SUBSECTOR")
        self.assertEqual(matter["candidate_count"], 12)
        self.assertEqual(
            matter["topology_counts"],
            {"I2_MATTER_V1_MATTER_V1": 6, "I2_MATTER_V2": 6},
        )
        rows = matter["structural_family_census"]
        self.assertEqual(len(rows), 12)
        self.assertEqual(sum(row["classification"] == "ADMITTED_UNCOMPUTED" for row in rows), 6)
        self.assertEqual(sum(row["classification"] == "PROVED_ABSENT_AT_THIS_ORDER" for row in rows), 6)

    def test_two_loop_valence_identity_excludes_physical_gauge_vertices(self) -> None:
        certificate = self.module.build_payload()["topological_valence_certificate"]
        self.assertEqual(certificate["identity"], "L=1+(M+sum_j(q_j-2))/2")
        self.assertEqual(
            certificate["L_equals_2_solution_under_conditions"],
            {"M": 2, "n_gauge": 0, "sum_j(q_j-2)": 0},
        )

    def test_census_has_no_coefficient_or_amplitude(self) -> None:
        payload = self.module.build_payload()
        for sector in ("FP", "MATTER"):
            for candidate in payload[sector]["candidates"]:
                self.assertNotIn("coefficient", candidate)
                self.assertNotIn("amplitude", candidate)
        self.assertIn("coefficient", payload["unevaluated_properties"])
        self.assertIn("finite_BV_density", payload["unevaluated_properties"])


if __name__ == "__main__":
    unittest.main()
