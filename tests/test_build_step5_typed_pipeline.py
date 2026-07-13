from __future__ import annotations

import json
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_step5_typed_pipeline import OUT, build_payload, main, render_summary
from scripts.step5_pipeline_ir import project_notation_schema


class BuildStep5TypedPipelineTest(unittest.TestCase):
    def test_schema_graph_and_amplitude_hashes_are_identical(self) -> None:
        payload = build_payload()
        schema_hash = project_notation_schema().canonical_hash
        self.assertEqual(payload["notation_hash"], schema_hash)
        for item in payload["orientations"]:
            graph_amplitude = item["graph_amplitude"]
            self.assertEqual(graph_amplitude["schema_hash"], schema_hash)
            amplitude = graph_amplitude["amplitudes"][0]
            self.assertEqual(amplitude["schema_hash"], schema_hash)
        for relative, digest in payload["source_sha256"].items():
            self.assertEqual(
                digest,
                hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(),
            )
        self.assertEqual(len(payload["compiler_hash"]), 64)

    def test_direct_and_reflected_exact_coefficients_are_separate(self) -> None:
        payload = build_payload()
        values = {
            item["orientation"]: item["graph_amplitude"]["amplitudes"][0][
                "exact_coefficient_reduced"
            ]["rendered"]
            for item in payload["orientations"]
        }
        self.assertEqual(values, {"DIRECT": "-1/8*g2", "REFLECTED": "1/8*g2"})

    def test_canonical_notation_json_is_an_actual_compiler_input(self) -> None:
        schema = project_notation_schema()
        with tempfile.TemporaryDirectory() as directory:
            notation = Path(directory) / "notation.json"
            schema.write_json(notation)
            self.assertEqual(main(("--notation", str(notation))), 0)
            generated = json.loads(
                (OUT / "ww-typed-pipeline.json").read_text(encoding="utf-8")
            )
        self.assertEqual(generated["notation_hash"], schema.canonical_hash)

    def test_graph_bound_projector_passes_and_mixed_external_fails_closed(self) -> None:
        payload = build_payload()
        for item in payload["orientations"]:
            local_result = item["d_algebra"]["local_projector_result"]
            mixed_result = item["d_algebra"]["mixed_external_phase_result"]
            self.assertEqual(local_result["status"], "PASS")
            self.assertEqual(mixed_result["status"], "UNIMPLEMENTED_PHASE_SEQUENCE")
            self.assertEqual(
                local_result["notation_hash"],
                item["graph_amplitude"]["schema_hash"],
            )
            output_words = local_result["normal_form"]["outputs"]
            self.assertTrue(
                any(
                    token["type"] == "Collapse"
                    for output in output_words
                    for token in output["word"]
                )
            )

    def test_stage_status_cannot_be_misread_as_an_accepted_coefficient(self) -> None:
        payload = build_payload()
        status = payload["stage_status"]
        self.assertEqual(status["anomaly_coefficient"], "NOT_ACCEPTED")
        self.assertEqual(status["basis_resolved_sd_contact_orbit"], "OPEN")
        self.assertEqual(
            status["full_scheduled_eight_row_dalgebra_per_orientation"],
            "UNIMPLEMENTED_PHASE_SEQUENCE",
        )
        markdown = render_summary(payload)
        self.assertIn(r"\Gamma_{\rm anomaly}:\ \texttt{NOT\_ACCEPTED}", markdown)
        self.assertIn(
            r"PASS\_SPECIALIZED\_16\_ROW\_DRED\_MASTER\_BINDING",
            markdown,
        )
        self.assertNotIn("accepted anomaly coefficient", markdown.lower())

    def test_all_specialized_rows_bind_exactly_to_the_dred_master(self) -> None:
        payload = build_payload()
        expected = {"DIRECT": "1/128", "REFLECTED": "-1/128"}
        for item in payload["orientations"]:
            binding = item["specialized_row_pole_binding"]
            amplitude = item["graph_amplitude"]["amplitudes"][0]
            self.assertEqual(
                binding["status"],
                "PASS_SPECIALIZED_8_ROW_DRED_MASTER_BINDING",
            )
            self.assertEqual(binding["notation_hash"], payload["notation_hash"])
            self.assertEqual(binding["graph_hash"], amplitude["canonical_key"])
            self.assertEqual(binding["amplitude_id"], amplitude["amplitude_id"])
            self.assertEqual(len(binding["dred_audit_sha256"]), 64)
            self.assertEqual(binding["dred_audit_exact_checks"]["failed_checks"], 0)
            self.assertEqual(len(binding["row_certificates"]), 8)
            self.assertTrue(
                all(row["status"] == "PASS" for row in binding["row_certificates"])
            )
            self.assertEqual(
                binding["orientation_pole_in_pi2_g2"],
                expected[item["orientation"]],
            )
            self.assertFalse(binding["generic_Dword_phase_completion"])
            self.assertFalse(binding["basis_resolved_contact_quotient"])
        self.assertEqual(
            payload["stage_status"]["integral_pole_binding"],
            "PASS_SPECIALIZED_16_ROW_DRED_MASTER_BINDING_"
            "NOT_GENERIC_DWORD_COMPLETION",
        )

    def test_generated_outputs_are_byte_reproducible(self) -> None:
        self.assertEqual(main(), 0)
        first = {
            path.name: path.read_bytes()
            for path in sorted(OUT.iterdir())
            if path.is_file()
        }
        self.assertEqual(main(), 0)
        second = {
            path.name: path.read_bytes()
            for path in sorted(OUT.iterdir())
            if path.is_file()
        }
        self.assertEqual(first, second)
        json.loads((OUT / "ww-typed-pipeline.json").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
