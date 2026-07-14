#!/usr/bin/env python3
"""Fail-closed audit for a WZ-component BV gauge reduction in current Step 5A."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "audits/step5a-wz-component-bv-gate.json"
MD_PATH = ROOT / "audits/step5a-wz-component-bv-gate.md"


def build() -> dict:
    step3d = (
        ROOT / "contracts/foundations/step-03d-n1-superfield-path-integral-bv-brst.md"
    ).read_text()
    step5a = (
        ROOT
        / "contracts/foundations/step-05a-component-bv-brst-primitive-supergraph-grammar.md"
    ).read_text()
    checks = {
        "step3d_forbids_implicit_wz_restriction": (
            "No Wess--Zumino gauge is imposed." in step3d
        ),
        "step5a_uses_unrestricted_prepotential": (
            "BV--BRST quantization instead uses the unrestricted connected-chart"
            in step5a
        ),
        "step5a_forbids_component_propagator_inference": (
            "No Wess--Zumino-gauge component propagator or ghost rule is inferred"
            in step5a
        ),
        "euclidean_ghosts_are_independent": (
            "Euclidean tilded and untilded fields are independent" in step5a
        ),
        "wz_lowest_component_is_zero": (
            "§mathcal V_E^{§mathrm{WZ}}".replace("§", chr(92)) in step5a
            and "-2i§vartheta§sigma_E^m§bar§vartheta A_m".replace(
                "§", chr(92)
            )
            in step5a
        ),
        "full_prepotential_brst_rule_exists": (
            "§mathbf s_R§mathcal V_R".replace("§", chr(92)) in step5a
            and "ie^{-§operatorname{ad}_{§mathcal V_R}}".replace(
                "§", chr(92)
            )
            in step5a
        ),
    }
    return {
        "schema": 1,
        "task": "CONTRACT-STEP-05-EUCLIDEAN-N4-AWI-SUPERGRAPH-001",
        "artifact": "STEP5A-WZ-COMPONENT-BV-GATE",
        "authority_status": "UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY",
        "checks": checks,
        "tangent_test": {
            "wz_constraints": [
                "V_WZ|=0",
                "D_a V_WZ|=0",
                "barD_dota V_WZ|=0",
            ],
            "brst_images": [
                "(s_E V_WZ)|=i*(tildec|-c|)",
                "D_a(s_E V_WZ)|=-i*D_a c|",
                "barD_dota(s_E V_WZ)|=+i*barD_dota tildec|",
            ],
            "result": "NOT_TANGENT_FOR_THE_INDEPENDENT_STEP5A_GHOST_DOMAIN",
        },
        "blockers": [
            {
                "id": "BLOCKED_STEP5A_WZ_BV_REDUCTION_UNDEFINED",
                "missing": [
                    "WZ-preserving constraints on every chiral and antichiral ghost component",
                    "induced residual component BRST differential and minimal BV action",
                    "canonical BV pushforward or reduction from the unrestricted prepotential",
                    "algebraic WZ-gauge FP determinant and its density carrier",
                    "Euclidean component integration cycle and Berezinian",
                ],
            },
            {
                "id": "BLOCKED_STEP5A_COMPONENT_TO_SUPERFIELD_WW_EQUIVALENCE_UNPROVED",
                "missing": [
                    "a regulator-compatible BV chain map for the WW composite insertion",
                    "equality of component and full-superfield contact/cutting descendants",
                    "equality of DRED evanescent operator mixing and counterterms",
                ],
            },
        ],
        "component_lorenz_gauge_status": (
            "CONSTRUCTIBLE_ONLY_AS_A_NEW_INDEPENDENT_COMPONENT_QUANTIZATION;"
            "NOT_AN_ADMISSIBLE_REDUCTION_OF_CURRENT_STEP3D"
        ),
        "ww_seed_status": "CANNOT_AUTHORIZE_OR_REPRODUCE_WITHOUT_THE_MISSING_EQUIVALENCE",
        "result": "BLOCKED_CURRENT_AUTHORITY",
    }


def render(data: dict) -> str:
    body = """# Step 5A WZ-component BV gate

Status: BLOCKED_CURRENT_AUTHORITY

Authority: UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY

## 1. Exact tangent test

The WZ surface obeys

$$
§mathcal V_E^{§mathrm{WZ}}§big|=0,
§qquad
D_{Ea}§mathcal V_E^{§mathrm{WZ}}§big|=0,
§qquad
§bar D_{E§dot a}§mathcal V_E^{§mathrm{WZ}}§big|=0.
$$

From Step 5A.39,

$$
§mathbf s_E§mathcal V_E
=§frac{§operatorname{ad}_{§mathcal V_E}}
{1-e^{-§operatorname{ad}_{§mathcal V_E}}}
§left(
ie^{-§operatorname{ad}_{§mathcal V_E}}
§widetilde{§mathfrak c}_E
-i§mathfrak c_E
§right).
$$

Because §(§mathcal V_E^{§mathrm{WZ}}§big|=0§) and its degree-one
spinor projections vanish,

$$
(§mathbf s_E§mathcal V_E^{§mathrm{WZ}})§big|
=i(§widetilde{§mathfrak c}_E§big|-§mathfrak c_E§big|),
$$

$$
D_{Ea}(§mathbf s_E§mathcal V_E^{§mathrm{WZ}})§big|
=-iD_{Ea}§mathfrak c_E§big|,
§qquad
§bar D_{E§dot a}(§mathbf s_E§mathcal V_E^{§mathrm{WZ}})§big|
=+i§bar D_{E§dot a}§widetilde{§mathfrak c}_E§big|.
$$

The Euclidean chiral and antichiral ghosts are independent. These
three expressions do not vanish on the admitted ghost domain. Hence

$$
§boxed{
§mathbf s_E§mathcal V_E^{§mathrm{WZ}}
§notin T_{§mathcal V_E^{§mathrm{WZ}}}
§{§mathscr V_E^{§mathrm{WZ}}§}}.
$$

## 2. Exact blockers

$$
§boxed{§mathrm{BLOCKED§_STEP5A§_WZ§_BV§_REDUCTION§_UNDEFINED}}.
$$

Missing: WZ-preserving ghost constraints; induced residual component
BRST and minimal BV action; a canonical BV pushforward; the algebraic
WZ FP determinant and density carrier; the Euclidean component cycle
and Berezinian.

$$
§boxed{
§mathrm{BLOCKED§_STEP5A§_COMPONENT§_TO§_SUPERFIELD§_WW§_EQUIVALENCE§_UNPROVED}}.
$$

Missing: a DRED-compatible BV chain map for the WW insertion; equality
of component and superfield cutting/contact descendants; equality of
evanescent mixing and counterterms.

A separate ordinary component Lorenz gauge can be constructed from
Step 3A.7, but current Steps do not identify it with the Step 3D
unrestricted-prepotential integral. It cannot authorize the WW
superspace seed.

## 3. Checks

| check | result |
|---|---|
"""
    rows = "\n".join(
        "| " + name + " | " + ("PASS" if passed else "FAIL") + " |"
        for name, passed in data["checks"].items()
    )
    return body.replace("§", chr(92)) + rows + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = build()
    if not all(data["checks"].values()):
        print(json.dumps(data, indent=2, sort_keys=True))
        return 1
    if args.write:
        JSON_PATH.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        MD_PATH.write_text(render(data))
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
