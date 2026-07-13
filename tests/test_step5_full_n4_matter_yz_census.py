from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.step5_full_n4_matter_yz_census import (  # noqa: E402
    AUDIT,
    GENERATED,
    SEAGULL_COLORS,
    TRIANGLE_COLORS,
    build_payload,
    seagull_quantum_ports,
    triangle_quantum_ports,
    write_artifacts,
)


SCRIPT = ROOT / "scripts/step5_full_n4_matter_yz_census.py"


class Step5FullN4MatterYZCensusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_payload()

    def test_exact_project_source_and_action_vertices(self) -> None:
        derivation = self.payload["project_derivation"]
        self.assertEqual(
            [row["term_id"] for row in derivation["I2"]],
            ["I2_direct_001", "I2_direct_002"],
        )
        self.assertEqual(
            [row["origin"] for row in derivation["I2"]],
            ["D_- placement LEFT", "D_- placement RIGHT"],
        )
        self.assertTrue(
            all(
                row["coefficient"]["rational"] == {"numerator": 1, "denominator": 64}
                for row in derivation["I2"]
            )
        )
        self.assertEqual(
            derivation["S3m_source"]["ordered_fields"],
            ["TildePhi", "V", "Phi"],
        )
        self.assertEqual(
            derivation["S4m_source"]["ordered_fields"],
            ["TildePhi", "V", "V", "Phi"],
        )

    def test_external_extractions_leave_required_quantum_ports(self) -> None:
        derivation = self.payload["project_derivation"]
        self.assertEqual(
            derivation["S3m_Y_extraction"]["remaining_quantum_fields"],
            ["TildePhi", "V"],
        )
        self.assertEqual(
            derivation["S3m_Z_extraction"]["remaining_quantum_fields"],
            ["V", "Phi"],
        )
        self.assertEqual(
            derivation["S4m_YZ_extraction"]["external_fields"],
            ["Phi", "TildePhi"],
        )
        self.assertEqual(
            derivation["S4m_YZ_extraction"]["remaining_quantum_fields"],
            ["V", "V"],
        )
        self.assertEqual(
            {
                derivation["S3m_Y_extraction"]["functional_derivative_koszul_sign"],
                derivation["S3m_Z_extraction"]["functional_derivative_koszul_sign"],
                derivation["S4m_YZ_extraction"]["functional_derivative_koszul_sign"],
            },
            {1},
        )

    def test_mixed_triangle_has_two_pairings_per_D_minus_placement(self) -> None:
        triangle = self.payload["triangle_I2_S3m_S3m"]
        rows = triangle["connected_labeled_Wick_rows"]
        self.assertEqual(len(rows), 4)
        self.assertEqual(
            {(row["D_minus_placement"], row["orientation"]) for row in rows},
            {
                ("LEFT", "DIRECT"),
                ("LEFT", "CROSSED"),
                ("RIGHT", "DIRECT"),
                ("RIGHT", "CROSSED"),
            },
        )
        self.assertEqual(triangle["disconnected_typed_matching_count"], 1)
        self.assertTrue(all(row["wick_koszul_sign"] == 1 for row in rows))
        self.assertTrue(
            all(row["certificate"]["is_connected_one_loop"] for row in rows)
        )
        self.assertEqual(
            [port.field_type.name for port in triangle_quantum_ports()],
            ["V", "V", "TildePhi", "V", "V", "Phi"],
        )

    def test_triangle_flavor_and_color_tensors_are_exact(self) -> None:
        rows = self.payload["triangle_I2_S3m_S3m"]["connected_labeled_Wick_rows"]
        for row in rows:
            self.assertEqual(row["flavor_tensor"], "delta[u,v]")
            self.assertEqual(row["color_tensor"], TRIANGLE_COLORS[row["orientation"]])
            self.assertEqual(row["typed_automorphism_order"], 1)
            self.assertFalse(row["symmetry_division_applied"])

    def test_mandatory_seagull_has_two_pairings_per_D_minus_placement(self) -> None:
        seagull = self.payload["seagull_I2_S4m"]
        rows = seagull["connected_labeled_Wick_rows"]
        self.assertEqual(len(rows), 4)
        self.assertEqual(
            {(row["D_minus_placement"], row["orientation"]) for row in rows},
            {
                ("LEFT", "DIRECT"),
                ("LEFT", "CROSSED"),
                ("RIGHT", "DIRECT"),
                ("RIGHT", "CROSSED"),
            },
        )
        self.assertEqual(seagull["disconnected_typed_matching_count"], 1)
        self.assertTrue(all(row["wick_koszul_sign"] == 1 for row in rows))
        self.assertEqual(
            [port.field_type.name for port in seagull_quantum_ports()],
            ["V", "V", "V", "V"],
        )
        for row in rows:
            self.assertEqual(row["flavor_tensor"], "delta[u,v]")
            self.assertEqual(row["color_tensor"], SEAGULL_COLORS[row["orientation"]])

    def test_all_incoming_routings_close_exactly(self) -> None:
        for family in ("triangle_I2_S3m_S3m", "seagull_I2_S4m"):
            routing = self.payload[family]["routing"]
            self.assertTrue(
                all(vector == [0, 0, 0] for vector in routing["vertex_sums"].values())
            )
            self.assertTrue(
                all(
                    vector == [0, 0, 0]
                    for vector in routing["edge_endpoint_sums"].values()
                )
            )
        self.assertEqual(
            self.payload["triangle_I2_S3m_S3m"]["routing"]["denominators"],
            ["k^2", "(k+p1)^2", "(k-p2)^2"],
        )
        self.assertEqual(
            self.payload["seagull_I2_S4m"]["routing"]["denominators"],
            ["k^2", "(k+p1+p2)^2"],
        )

    def test_exact_stored_coefficients_do_not_become_an_accepted_amplitude(
        self,
    ) -> None:
        triangle = self.payload["triangle_I2_S3m_S3m"]["coefficient_ledger"]
        seagull = self.payload["seagull_I2_S4m"]["coefficient_ledger"]
        self.assertEqual(
            triangle["stored_monomial_product"],
            {
                "rational": {"numerator": -1, "denominator": 64},
                "sqrt2_power": 0,
                "i_power": 0,
                "symbol_powers": {"h": 2},
            },
        )
        self.assertEqual(
            triangle["known_factor_before_open_matter_propagator"]["rational"],
            {"numerator": -1, "denominator": 16},
        )
        self.assertEqual(
            seagull["per_labeled_Wick_row_before_propagators"],
            {
                "rational": {"numerator": -1, "denominator": 128},
                "sqrt2_power": 0,
                "i_power": 0,
                "symbol_powers": {"h": 1},
            },
        )
        self.assertEqual(
            seagull["factor_after_exact_vector_propagators"],
            {
                "rational": {"numerator": -1, "denominator": 32},
                "sqrt2_power": 0,
                "i_power": 0,
                "symbol_powers": {"g2": 2, "h": 1},
            },
        )
        self.assertEqual(
            self.payload["totals"]["accepted_coefficients"],
            0,
        )

    def test_matter_propagator_Y_projection_and_Euler_sources_fail_closed(self) -> None:
        obligations = {row["id"]: row for row in self.payload["open_obligations"]}
        self.assertEqual(
            set(obligations),
            {
                "MATTER_SUPERPROPAGATOR_NORMALIZATION",
                "EXTERNAL_Y_DALGEBRA_PROJECTION",
                "E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE",
                "E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE",
            },
        )
        self.assertTrue(all(row["status"] == "OPEN" for row in obligations.values()))
        self.assertEqual(
            obligations["E_XI_I3_SOURCE_FUNCTIONAL_DERIVATIVE"][
                "current_mixed_I3_source_term_count"
            ],
            0,
        )
        self.assertEqual(
            obligations["E_XI_I4_SOURCE_FUNCTIONAL_DERIVATIVE"][
                "current_mixed_I4_source_term_count"
            ],
            0,
        )
        boundary = self.payload["acceptance_boundary"]
        self.assertFalse(any(boundary.values()))

    def test_no_external_or_holomorphic_twist_input(self) -> None:
        self.assertFalse(self.payload["external_results_imported"])
        self.assertEqual(self.payload["holomorphic_twist_input_count"], 0)
        self.assertEqual(self.payload["external_target_input_count"], 0)
        self.assertEqual(
            self.payload["status"],
            "PASS_EXACT_PROJECT_GRAPH_CENSUS__AMPLITUDES_FAIL_CLOSED",
        )
        self.assertTrue(all(self.payload["checks"].values()))

    def test_artifacts_are_byte_reproducible(self) -> None:
        first = write_artifacts()
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())
        self.assertEqual(json.loads(generated_first), first)
        audit = json.loads(audit_first)
        self.assertEqual(audit["totals"]["failed"], 0)
        self.assertEqual(audit["holomorphic_twist_input_count"], 0)
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(generated_first).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
