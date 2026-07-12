from __future__ import annotations

import json
import hashlib
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.build_step5_graph_catalogue import (
    AUDIT_PATH,
    CATALOGUE_PATH,
    MAPS_PATH,
    build_catalogue,
)
from scripts.step5_graph_ir import emit_ordered_family_channels


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_step5_graph_catalogue.py"


def reconstruct_valence_only_requests(
    catalogue: dict[str, object],
) -> list[dict[str, str]]:
    product = catalogue["valence_only_request_product"]
    channels = {
        tree["channel"]["channel_id"]: tree["channel"]
        for tree in catalogue["tree_channels"]
    }
    templates = {
        template["template_id"]: template
        for template in catalogue["valence_only_templates"]
    }
    requests: list[dict[str, str]] = []
    for channel_id in product["ordered_channel_ids"]:
        channel = channels[channel_id]
        for template_id in product["ordered_template_ids"]:
            template = templates[template_id]
            requests.append(
                {
                    "request_id": f"loop__{channel_id}__{template_id}",
                    "channel_id": channel_id,
                    "template_id": template_id,
                    "reverse_request_id": (
                        f"loop__{channel['reverse_channel_id']}__"
                        f"{template['reflection_template_id']}"
                    ),
                    "reverse_binding_id": f"reverse_binding__{channel_id}",
                }
            )
    return requests


class Step5GraphCatalogueTest(unittest.TestCase):
    def test_committed_generated_artifacts_are_byte_reproducible(self) -> None:
        committed = {
            path: path.read_bytes()
            for path in (CATALOGUE_PATH, MAPS_PATH, AUDIT_PATH)
        }
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        first_regeneration = {path: path.read_bytes() for path in committed}
        self.assertEqual(committed, first_regeneration)
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        second_regeneration = {path: path.read_bytes() for path in committed}
        self.assertEqual(first_regeneration, second_regeneration)

    def test_generated_goldens_are_git_tracked(self) -> None:
        for path in (CATALOGUE_PATH, MAPS_PATH):
            relative = str(path.relative_to(ROOT))
            subprocess.run(
                ["git", "ls-files", "--error-unmatch", relative],
                cwd=ROOT,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

    def test_tree_catalogue_is_the_same_indexed_ir_as_channel_emitter(self) -> None:
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        emitted = [channel.canonical_dict() for channel in emit_ordered_family_channels()]
        stored = [item["channel"] for item in catalogue["tree_channels"]]
        self.assertEqual(stored, emitted)
        self.assertEqual(len(stored), 16)
        for item in catalogue["tree_channels"]:
            channel_id = item["channel"]["channel_id"]
            self.assertIn(channel_id, item["ordered_tree_maps"]["mermaid"])
            self.assertIn("reverse_of__", item["reversed_tree_maps"]["mermaid"])
            for descendant_key in ("descendant", "reversed_descendant"):
                for term in item["channel"][descendant_key]["terms"]:
                    for tensor in term["tensor_factors"]:
                        self.assertIsInstance(tensor, dict)
                        self.assertIn(tensor["symbol"], ("c", "epsilon", "kappa"))
                        self.assertEqual(len(tensor["ordered_indices"]), len(tensor["bindings"]))
                        self.assertTrue(
                            all(
                                {"space", "label", "variance"} == set(index)
                                for index in tensor["ordered_indices"]
                            )
                        )
        all_tree_maps = "\n".join(
            item["ordered_tree_maps"]["mermaid"] for item in catalogue["tree_channels"]
        )
        self.assertIn(
            "c[C:COLOR_ADJOINT:DOWN,D:COLOR_ADJOINT:DOWN,A:COLOR_ADJOINT:UP]",
            all_tree_maps,
        )
        self.assertIn(
            "epsilon[r:FLAVOR:DOWN,u:FLAVOR:DOWN,v:FLAVOR:DOWN]",
            all_tree_maps,
        )

    def test_all_valence_only_requests_remain_typed_non_graphs(self) -> None:
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        product = catalogue["valence_only_request_product"]
        requests = reconstruct_valence_only_requests(catalogue)
        self.assertEqual(len(requests), 10432)
        self.assertEqual(product["total_count"], 10432)
        self.assertEqual(catalogue["counts"]["valence_only_templates_per_channel"], 652)
        self.assertEqual(product["kind"], "DECLARATIVE_CARTESIAN_PRODUCT")
        self.assertEqual(
            product["enumeration_order"],
            ["ordered_channel_ids", "ordered_template_ids"],
        )
        self.assertEqual(
            product["ordered_channel_ids"],
            [tree["channel"]["channel_id"] for tree in catalogue["tree_channels"]],
        )
        self.assertEqual(
            product["ordered_template_ids"],
            [template["template_id"] for template in catalogue["valence_only_templates"]],
        )
        self.assertEqual(product["request_id_rule"], "loop__{channel_id}__{template_id}")
        self.assertEqual(
            product["reverse_request_id_rule"],
            "loop__{reverse_channel_id(channel_id)}__"
            "{reflection_template_id(template_id)}",
        )
        self.assertEqual(product["reverse_binding_id_rule"], "reverse_binding__{channel_id}")
        self.assertEqual(product["classification"], "VALENCE_ONLY_NOT_GRAPH")
        self.assertEqual(product["status"], "BLOCKED_VALENCE_ONLY_NOT_GRAPH")
        self.assertEqual(product["blocker_contract_ref"], "blocker_contract.loop_blockers")
        self.assertNotIn("valence_only_requests", catalogue)
        self.assertTrue(
            all(key not in product for key in ("graph_ir", "maps", "amplitude_skeleton"))
        )
        self.assertEqual(len({request["request_id"] for request in requests}), 10432)
        self.assertIn(
            "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
            catalogue["blocker_contract"]["loop_blockers"],
        )
        self.assertEqual(
            catalogue["blocker_contract"]["loop_blockers"],
            [
                "BLOCKED_LOCAL_NONMINIMAL_GAUGE_KERNEL",
                "BLOCKED_GAUGE_FIXED_DENSITY_BEREZINIAN",
                "BLOCKED_VECTOR_TRANSVERSE_FINITE_GAUSSIAN_RECONSTRUCTION",
                "BLOCKED_FP_GHOST_CYCLE_UNDECLARED",
                "BLOCKED_NK_BRANCH_AND_KERNEL_UNFIXED",
                "BLOCKED_UNINSTANTIATED_E_XI_CORE",
                "BLOCKED_COMPOSITE_DESCENDANT_INSERTION_UNINSTANTIATED",
                "BLOCKED_EDGE_TAGGED_PROJECTOR_DALGEBRA_TRACE",
            ],
        )

    def test_reverse_and_reflected_census_is_closed(self) -> None:
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        requests = reconstruct_valence_only_requests(catalogue)
        templates = {
            template["template_id"]: template for template in catalogue["valence_only_templates"]
        }
        by_id = {request["request_id"]: request for request in requests}
        bindings = {
            binding["reverse_binding_id"]: binding for binding in catalogue["reverse_bindings"]
        }
        self.assertEqual(len(bindings), 16)
        self.assertEqual(len(by_id), len(requests))
        for request in requests:
            self.assertIn(request["reverse_binding_id"], bindings)
            reverse = by_id[request["reverse_request_id"]]
            self.assertEqual(reverse["reverse_request_id"], request["request_id"])
            if templates[request["template_id"]]["topology"] == "TRIANGLE":
                self.assertNotEqual(
                    templates[reverse["template_id"]]["orientation"],
                    templates[request["template_id"]]["orientation"],
                )
        for binding in bindings.values():
            channel = catalogue["tree_channels"][binding["tree_channel_ordinal"] - 1]["channel"]
            reversed_descendant = channel["reversed_descendant"]
            digest = hashlib.sha256(
                json.dumps(
                    reversed_descendant,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            self.assertEqual(binding["bound_reversed_descendant_sha256"], digest)
            self.assertEqual(
                binding["bound_reversed_descendant_channel_id"],
                reversed_descendant["channel_id"],
            )
            permutation = binding["fixed_index_permutation"]
            self.assertEqual(
                [(item["source_position"], item["target_position"]) for item in permutation],
                [(0, 1), (1, 0)],
            )
            self.assertEqual(permutation[0]["letter"], channel["left"])
            self.assertEqual(permutation[1]["letter"], channel["right"])

    def test_generic_fixture_ir_and_all_renderers_have_identical_id_inventory(self) -> None:
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        fixtures = catalogue["generic_blocked_graph_fixtures"]
        self.assertEqual(len(fixtures), 8)
        self.assertEqual(sum(item["relation"] == "PARENT_TRIANGLE" for item in fixtures), 2)
        self.assertEqual(
            sum(item["relation"] == "COLLAPSED_CONTACT_CANDIDATE" for item in fixtures),
            6,
        )
        for item in fixtures:
            inventory = item["render_id_inventory"]
            renderings = item["maps"]
            for vertex_id in inventory["vertex_ids"]:
                self.assertTrue(all(vertex_id in rendering for rendering in renderings.values()))
            for edge_id in inventory["internal_edge_ids"]:
                self.assertTrue(all(edge_id in rendering for rendering in renderings.values()))
                self.assertIn(edge_id, item["amplitude_skeleton"]["expression"])
            self.assertFalse(item["admitted_amplitude"])
            self.assertEqual(item["amplitude_skeleton"]["status"], "BLOCKED_NOT_ADMITTED_AMPLITUDE")
            self.assertEqual(
                {entry["op_id"] for entry in item["external_derivative_ledger"]},
                {"D_external_out_D", "D_external_out_E"},
            )
            external_derivatives = {
                derivative["op_id"]
                for leg in item["graph_ir"]["external_legs"]
                for derivative in leg["operator_derivatives"]
            }
            self.assertEqual(external_derivatives, {"D_external_out_D", "D_external_out_E"})
            self.assertEqual(
                item["graph_ir"]["metadata"]["channel_id"],
                "UNASSIGNED_GENERIC_FIXTURE",
            )
            self.assertIn(
                "BLOCKED_COMPOSITE_DESCENDANT_INSERTION_UNINSTANTIATED",
                item["blockers"],
            )
            self.assertTrue(item["momentum_validation"]["passed"])
            self.assertTrue(
                all(
                    checks["endpoint_opposition"] and checks["edge_reference_match"]
                    for checks in item["momentum_validation"]["edge_checks"].values()
                )
            )
            self.assertTrue(
                all(item["momentum_validation"]["vertex_conservation"].values())
            )

        parents = {
            item["graph_ir"]["metadata"]["orientation"]: item
            for item in fixtures
            if item["relation"] == "PARENT_TRIANGLE"
        }
        direct_edges = {
            edge["edge_id"]: edge["momentum"]
            for edge in parents["DIRECT"]["graph_ir"]["internal_edges"]
        }
        reflected_edges = {
            edge["edge_id"]: edge["momentum"]
            for edge in parents["REFLECTED"]["graph_ir"]["internal_edges"]
        }
        self.assertEqual(
            direct_edges,
            {"eI1": "k0", "e12": "k0-p1", "e2I": "k0-p1-p2"},
        )
        self.assertEqual(
            reflected_edges,
            {"eI2": "k0", "e21": "k0-p2", "e1I": "k0-p1-p2"},
        )
        for parent in parents.values():
            insertion_vertex = next(
                vertex for vertex in parent["graph_ir"]["vertices"] if vertex["vertex_id"] == "I"
            )
            self.assertEqual(insertion_vertex["momentum_injection"], "-p1-p2")

    def test_fp_typed_zeros_and_euler_core_blocker_survive_catalogue(self) -> None:
        catalogue = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(catalogue["counts"]["action_monomials"], 27)
        self.assertEqual(catalogue["counts"]["typed_zero_action_monomials"], 2)
        self.assertEqual(
            {item["monomial_id"] for item in catalogue["typed_zero_action_monomials"]},
            {"fp_plus_c_v0", "fp_minus_tilde_c_v0"},
        )
        self.assertTrue(
            all(
                item["core_status"] == "BLOCKED_UNINSTANTIATED_E_XI_CORE"
                for item in catalogue["insertion_chart_monomials"]
            )
        )

    def test_audit_and_human_map_are_exact(self) -> None:
        audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["totals"], {"checks": 22, "failed": 0})
        self.assertEqual(
            audit["topology_distribution"],
            {"TADPOLE": 16, "BUBBLE": 432, "TRIANGLE": 9984},
        )
        markdown = MAPS_PATH.read_text(encoding="utf-8")
        self.assertEqual(markdown.count("## Tree "), 16)
        self.assertEqual(markdown.count("### `generic_blocked_triangle_fixture"), 8)
        self.assertNotIn("WW seed", markdown)
        self.assertIn("BLOCKED_GAUGE_KERNEL_CANDIDATE_CATALOGUE", markdown)
        for relative in (
            "contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md",
            "scripts/step5_graph_ir.py",
            "scripts/step5_vertex_grammar.py",
        ):
            self.assertEqual(
                audit["sha256"][relative],
                hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(),
            )

    def test_builder_matches_committed_generated_json(self) -> None:
        stored = json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, build_catalogue())


if __name__ == "__main__":
    unittest.main()
