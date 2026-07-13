from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/step5_ww_contact_quotient.py"
OUTPUT = ROOT / "generated/step5/contact-quotient/ww-contact-quotient.json"
REPORT = ROOT / "generated/step5/contact-quotient/ww-contact-quotient.md"
AUDIT = ROOT / "audits/step5-ww-contact-quotient-verification.json"


def load_module():
    specification = importlib.util.spec_from_file_location("step5_ww_contact_quotient", SCRIPT)
    if specification is None or specification.loader is None:
        raise RuntimeError("cannot load WW contact quotient generator")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


class Step5WWContactQuotientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        cls.payload = json.loads(OUTPUT.read_text())

    def test_exact_basis_and_wick_counts(self) -> None:
        self.assertEqual(
            self.payload["counts"],
            {
                "I3_rows": 30,
                "S3_antichiral_rows": 6,
                "I3_x_S3_ordered_vertex_pairs": 180,
                "I3_x_S3_labeled_Wick_pairings": 360,
                "I3_x_S3_decorated_graph_classes": 360,
                "I4_labeled_Wick_pairings": 180,
                "I4_decorated_partial_graph_classes": 180,
                "physical_graph_class_canonicalization": "OPEN",
            },
        )
        bubbles = self.payload["I3_x_S3_graphs"]
        grouped: dict[tuple[str, str], list[dict[str, object]]] = {}
        for row in bubbles:
            metadata = row["graph_ir"]["metadata"]
            key = (metadata["i3_assignment"], metadata["s3_assignment"])
            grouped.setdefault(key, []).append(row)
        self.assertEqual(len(grouped), 180)
        self.assertTrue(all(len(rows) == 2 for rows in grouped.values()))
        self.assertTrue(
            all(
                {row["graph_ir"]["metadata"]["pairing_permutation"] for row in rows}
                == {"0,1", "1,0"}
                for rows in grouped.values()
            )
        )

    def test_projected_rows_are_joined_back_to_lossless_port_and_color_data(self) -> None:
        basis = self.payload["basis"]
        for family in ("joined_I3_rows", "joined_S3_antichiral_rows"):
            for row in basis[family]:
                self.assertTrue(row["ordered_ports"])
                self.assertTrue(row["color_bracket_word"])
                self.assertTrue(
                    all("derivative_word_outer_to_inner" in port for port in row["ordered_ports"])
                )
                self.assertEqual(
                    [port["port_id"] for port in row["ordered_ports"] if port["role"] == "QUANTUM_WICK"],
                    row["quantum_ports"],
                )
        self.assertEqual(len(basis["joined_I4_rows"]), 180)
        for row in basis["joined_I4_rows"]:
            self.assertTrue(row["color_bracket_word"])
            self.assertTrue(
                all("derivative_word_outer_to_inner" in port for port in row["ordered_ports"])
            )
        for row in self.payload["I3_x_S3_graphs"]:
            self.assertTrue(row["color_provenance"]["I3_color_bracket_word"])
            self.assertTrue(row["color_provenance"]["S3_color_bracket_word"])
            for binding in row["source_term_bindings"].values():
                source = self.payload["source_terms"][binding["term_id"]]
                self.assertEqual(source["expression_sha256"], binding["expression_sha256"])
                self.assertTrue(source["expression"])
            for family in row["port_provenance"].values():
                for port in family:
                    self.assertIn("derivative_word_outer_to_inner", port)
                    self.assertIn(
                        port["derivative_scope_classification"],
                        ("ORDERED_DERIVATIVE_WORD", "IDENTITY_NO_DERIVATIVE"),
                    )
                    self.assertTrue(port["color_token"])
        for row in self.payload["I4_tadpole_graphs"]:
            self.assertTrue(row["color_provenance"]["I4_color_bracket_word"])
            self.assertTrue(row["source_term_binding"]["expression_sha256"])
            binding = row["source_term_binding"]
            self.assertEqual(
                self.payload["source_terms"][binding["term_id"]]["expression_sha256"],
                binding["expression_sha256"],
            )
            self.assertTrue(
                all("derivative_word_outer_to_inner" in port for port in row["port_provenance"])
            )

    def test_every_graph_has_exact_routing_and_one_loop(self) -> None:
        for row in self.payload["I3_x_S3_graphs"]:
            graph = row["graph_ir"]
            self.assertTrue(self.module.serialized_graph_routing_passes(graph))
            self.assertEqual(graph["loop_momenta"], ["k"])
            self.assertEqual(len(graph["vertices"]), 2)
            self.assertEqual(len(graph["internal_edges"]), 2)
            self.assertEqual(
                {edge["momentum"] for edge in graph["internal_edges"]},
                {"k", "q-k"},
            )
        for row in self.payload["I4_tadpole_graphs"]:
            graph = row["graph_ir"]
            self.assertTrue(self.module.serialized_graph_routing_passes(graph))
            self.assertEqual(graph["loop_momenta"], ["k"])
            self.assertEqual(len(graph["vertices"]), 1)
            self.assertEqual(len(graph["internal_edges"]), 1)
            self.assertFalse(row["routing_classification"]["external_momentum_in_denominator"])

    def test_source_statistics_X_chirality_and_physical_class_gate_are_honest(self) -> None:
        all_graphs = self.payload["I3_x_S3_graphs"] + self.payload["I4_tadpole_graphs"]
        for row in all_graphs:
            self.assertEqual(
                row["physical_graph_class_status"],
                "OPEN_TYPED_AUTOMORPHISM_COLOR_DWORD_CANONICALIZATION",
            )
            source = next(
                leg for leg in row["graph_ir"]["external_legs"] if leg["leg_id"] == "WW_source"
            )
            self.assertEqual(source["field_type"]["statistics"], "FERMION")
            metadata = row["graph_ir"]["metadata"]
            self.assertEqual(
                metadata["symmetry_factor"],
                "OPEN_TYPED_AUTOMORPHISM_AUDIT",
            )
            self.assertEqual(
                metadata["typed_automorphism_order"],
                "OPEN_TYPED_AUTOMORPHISM_AUDIT",
            )
        for row in self.payload["I3_x_S3_graphs"]:
            external_x = next(
                leg for leg in row["graph_ir"]["external_legs"] if leg["leg_id"] == "X_external"
            )
            self.assertEqual(external_x["field_type"]["statistics"], "BOSON")
            self.assertEqual(external_x["field_type"]["chirality"], "UNCONSTRAINED")

    def test_all_pairing_signs_and_symmetry_provenance_are_explicit(self) -> None:
        all_graphs = self.payload["I3_x_S3_graphs"] + self.payload["I4_tadpole_graphs"]
        for row in all_graphs:
            pairing = row["pairing"]
            coefficient = row["coefficient_provenance"]
            self.assertEqual(pairing["fermion_crossings"], 0)
            self.assertEqual(pairing["wick_sign"], 1)
            self.assertEqual(pairing["koszul_sign"], 1)
            self.assertEqual(pairing["labeled_pairing_multiplicity"], 1)
            self.assertEqual(coefficient["typed_automorphism_order_audit"], "OPEN")
            self.assertFalse(coefficient["automorphism_division_applied"])
        first = self.payload["I3_x_S3_graphs"][0]
        self.assertEqual(
            first["coefficient_provenance"]["known_product_excluding_open_factors"]["rendered"],
            "-1/16384*g^2*g^2*h*kappa^-1*kappa^-1",
        )
        self.assertEqual(
            first["coefficient_provenance"]["open_factors"],
            [
                "EUCLIDEAN_PATH_INTEGRAL_ACTION_VERTEX_EXPANSION",
                "EXTERNAL_PROJECTOR_NORMALIZATION_AND_EXTRACTION_SIGN",
                "TYPED_AUTOMORPHISM_AND_SYMMETRY_AUDIT",
            ],
        )

    def test_structural_quotient_is_total_but_transports_no_coefficient(self) -> None:
        quotient = self.payload["quotient"]
        self.assertEqual(
            quotient["map_type"],
            "SURJECTIVE_STRUCTURAL_QUOTIENT_NOT_AMPLITUDE_IDENTITY",
        )
        self.assertEqual(
            quotient["fiber_counts"],
            {"CR-I3S3-BUBBLE-X-TILDEW": 360, "CR-I4-ONE-V-TADPOLE": 180},
        )
        self.assertEqual(len(quotient["maps"]), 540)
        self.assertEqual(
            len({row["domain_decorated_graph_class_id"] for row in quotient["maps"]}),
            540,
        )
        self.assertTrue(
            all(row["coefficient_transport"] == "NOT_PERFORMED" for row in quotient["maps"])
        )
        self.assertFalse(quotient["aggregate_coefficient_inserted"])
        self.assertFalse(quotient["linear_sum_over_fibers_proved"])

    def test_I4_physical_projection_and_normal_ordering_remain_open(self) -> None:
        for row in self.payload["I4_tadpole_graphs"]:
            self.assertEqual(
                row["external_projection_status"],
                "OPEN_I4_BACKGROUND_PORTS_NOT_MAPPED_TO_X_AND_TILDEW",
            )
            self.assertEqual(
                row["coefficient_provenance"]["open_factors"],
                [
                    "NORMAL_ORDERING_SELF_CONTRACTION_ADMISSION",
                    "TYPED_AUTOMORPHISM_AND_SYMMETRY_AUDIT",
                ],
            )
            self.assertEqual(
                row["routing_classification"]["status"],
                "SCALELESS_DENOMINATOR_ROUTING_PROVED; D_ALGEBRA_NUMERATOR_NOT_REDUCED",
            )

    def test_no_aggregate_pole_or_anomaly_result_is_injected(self) -> None:
        encoded = json.dumps(self.payload, sort_keys=True)
        self.assertFalse(self.payload["aggregate_contact_result_imported"])
        self.assertFalse(self.payload["pole_or_anomaly_coefficient_computed"])
        for fragment in ("1024*pi", "128*pi", "64*pi"):
            self.assertNotIn(fragment, encoded)
        self.assertEqual(
            [row["id"] for row in self.payload["open_proof_obligations"]],
            [f"OPEN_CONTACT_{number:03d}" for number in range(1, 9)],
        )

    def test_artifacts_are_byte_reproducible(self) -> None:
        paths = (OUTPUT, REPORT, AUDIT)
        first = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        self.assertEqual(first, second)
        audit = json.loads(AUDIT.read_text())
        self.assertEqual(audit["status"], "PASS_WITH_OPEN_PROOF_OBLIGATIONS")
        self.assertEqual(audit["totals"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
