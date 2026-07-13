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

from scripts.step5_full_n4_topology_census import (  # noqa: E402
    AUDIT,
    GENERATED,
    Port,
    build_payload,
    enumerate_perfect_matchings,
    enumerate_two_external_one_loop_topologies,
    matching_graph_certificate,
    topology_witness_ports,
    topology_witnesses,
    write_artifacts,
)


SCRIPT = ROOT / "scripts/step5_full_n4_topology_census.py"


class Step5FullN4TopologyCensusTest(unittest.TestCase):
    def test_diophantine_classification_is_exact(self) -> None:
        rows = enumerate_two_external_one_loop_topologies()
        self.assertEqual(
            [row.topology_id for row in rows],
            ["I2S3S3", "I3S3", "I2S4", "I4"],
        )
        for row in rows:
            self.assertEqual(row.defect_sum, 2)
            self.assertEqual(row.external_leg_count, 2)
            self.assertEqual(row.internal_edge_count, row.action_vertex_count + 1)
            self.assertEqual(row.loop_number, 1)
            self.assertEqual(
                row.insertion_valence + sum(row.action_valences),
                2 * row.internal_edge_count + row.external_leg_count,
            )

    def test_each_topology_has_typed_connected_one_loop_witness(self) -> None:
        witnesses = topology_witnesses()
        self.assertEqual(len(witnesses), 4)
        for witness in witnesses:
            self.assertGreater(witness["connected_one_loop_matching_count"], 0)
            self.assertTrue(witness["certificate"]["is_connected_one_loop"])

    def test_perfect_matching_rejects_type_and_flavor_mismatches(self) -> None:
        self.assertFalse(
            enumerate_perfect_matchings((Port("a", "u", "V"), Port("b", "v", "Phi", 1)))
        )
        self.assertFalse(
            enumerate_perfect_matchings(
                (
                    Port("a", "u", "Phi", 1),
                    Port("b", "v", "TildePhi", 2),
                )
            )
        )
        self.assertTrue(
            enumerate_perfect_matchings(
                (
                    Port("a", "u", "Phi", 3),
                    Port("b", "v", "TildePhi", 3),
                )
            )
        )
        self.assertFalse(
            enumerate_perfect_matchings(
                (
                    Port("a", "u", "V"),
                    Port("b", "v", "V"),
                    Port("c", "w", "V"),
                )
            )
        )

    def test_disconnected_perfect_matching_is_not_a_graph_witness(self) -> None:
        ports = topology_witness_ports("I3S3")
        matchings = enumerate_perfect_matchings(ports)
        certificates = [matching_graph_certificate(ports, row) for row in matchings]
        self.assertTrue(
            any(certificate["is_connected_one_loop"] for certificate in certificates)
        )
        self.assertTrue(
            any(not certificate["connected"] for certificate in certificates)
        )

    def test_channel_census_and_fail_closed_states(self) -> None:
        payload = build_payload()
        channels = payload["channel_ledger"]
        self.assertEqual(len(channels), 16)
        self.assertEqual(sum(row["component_multiplicity"] for row in channels), 81)

        bare_zero = [row for row in channels if row["bare_insertion_zero"]]
        self.assertEqual(
            {row["channel_id"] for row in bare_zero}, {"ZZ", "ZT", "TZ", "TT"}
        )
        self.assertEqual(sum(row["component_multiplicity"] for row in bare_zero), 25)

        nonzero = [row for row in channels if not row["bare_insertion_zero"]]
        self.assertEqual(len(nonzero), 12)
        self.assertEqual(sum(row["component_multiplicity"] for row in nonzero), 56)
        self.assertFalse(any(row["accepted_renormalized_result"] for row in channels))

        xx = next(row for row in channels if row["channel_id"] == "XX")
        self.assertEqual(
            xx["implementation_state"],
            "PARTIAL_PURE_VECTOR_I2S3S3_ONLY__NO_ACCEPTED_COEFFICIENT",
        )
        self.assertEqual(
            xx["required_two_external_one_loop_topologies"],
            ["I2S3S3", "I3S3", "I2S4", "I4"],
        )

    def test_ww_missing_family_boundary_is_explicit(self) -> None:
        payload = build_payload()
        rows = {row["family"]: row for row in payload["ww_missing_families"]}
        self.assertEqual(
            set(rows),
            {"I2S3S3", "I3S3", "I2S4", "I4", "DALGEBRA_COLLAPSED_CHILDREN", "CT2"},
        )
        self.assertTrue(rows["I2S3S3"]["state"].startswith("PARTIAL"))
        self.assertTrue(rows["I3S3"]["state"].startswith("OPEN"))
        self.assertTrue(rows["I2S4"]["state"].startswith("OPEN"))
        self.assertTrue(rows["I4"]["state"].startswith("OPEN"))
        self.assertFalse(
            payload["result_boundary"]["full_n4_one_loop_coefficient_accepted"]
        )

    def test_payload_has_no_external_target_input(self) -> None:
        payload = build_payload()
        self.assertFalse(payload["external_results_imported"])
        self.assertFalse(payload["external_target_data_imported"])
        self.assertEqual(
            payload["status"],
            "PASS_INTERNAL_CENSUS__PHYSICAL_AMPLITUDES_FAIL_CLOSED",
        )
        self.assertTrue(all(row["passed"] for row in payload["checks"]))

    def test_artifacts_are_byte_reproducible(self) -> None:
        first = write_artifacts()
        generated_first = GENERATED.read_bytes()
        audit_first = AUDIT.read_bytes()
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        self.assertEqual(generated_first, GENERATED.read_bytes())
        self.assertEqual(audit_first, AUDIT.read_bytes())

        audit = json.loads(audit_first)
        self.assertEqual(audit["status"], first["status"])
        self.assertEqual(
            audit["generated_sha256"], hashlib.sha256(generated_first).hexdigest()
        )
        self.assertEqual(audit["totals"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
