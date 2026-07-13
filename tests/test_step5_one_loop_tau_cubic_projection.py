from fractions import Fraction

from scripts.step5_one_loop_tau_cubic_projection import build_payload


def test_complete_n3_rooted_family_census() -> None:
    payload = build_payload()
    census = payload["rooted_family_census"]
    assert census["unpolarized_family_count"] == 8
    assert census["polarized_rooted_row_count"] == 26
    assert [row["polarized_row_count"] for row in census["families"]] == [
        1,
        3,
        3,
        6,
        3,
        6,
        3,
        1,
    ]
    assert sum(row["polarized_row_count"] for row in census["families"]) == 26


def test_neumann_signs_are_exact() -> None:
    payload = build_payload()
    coefficients = [
        Fraction(row["coefficient"]["numerator"], row["coefficient"]["denominator"])
        for row in payload["rooted_family_census"]["families"]
    ]
    assert coefficients == [
        Fraction(-1, 2),
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(-1, 2),
        Fraction(-1, 2),
        Fraction(1, 2),
        Fraction(-1, 2),
        Fraction(1, 2),
    ]


def test_existing_kernel_branches_and_missing_families() -> None:
    payload = build_payload()
    registry = payload["kernel_registry"]
    census = payload["rooted_family_census"]
    assert registry["source_branch_counts"] == {"I0": 4, "I1": 60, "I2": 720}
    assert registry["vector_hessian_branch_counts"] == {"H1": 24, "H2": 144}
    assert [row["family"] for row in census["families"] if row["missing_kernels"]] == [
        "I0_H3",
        "I3",
    ]
    assert census["kernel_branch_available_polarized_rows"] == 24
    assert census["kernel_branch_blocked_polarized_rows"] == 2
    assert census["available_vector_branch_path_count"] == 699_840


def test_H3_and_I3_fail_closed_without_zero_claim() -> None:
    payload = build_payload()
    registry = payload["kernel_registry"]
    assert registry["H3"]["current_valence_five_monomial_count"] == 0
    assert registry["H3"]["status"] == (
        "BLOCKED_MISSING_PROJECT_QUINTIC_GAUGE_ACTION_GRAMMAR"
    )
    assert registry["I3"]["status"] == "BLOCKED_MISSING_PROJECT_I5_COMPOSITE_GRAMMAR"
    assert registry["I3"]["direct_constructor_error"] == (
        "the seed insertion grammar is I2, I3, I4"
    )


def test_raw_DRED_target_and_physical_4d_quotient_are_separated() -> None:
    payload = build_payload()
    target = payload["target"]
    assert target["tau_target_multiplicity_at_N3"] == 1
    assert target["physical_target_multiplicity_at_N3"] == 0
    assert target["SU2_nonzero_component"] == "K^00_(0[DE]) B^[DE]=4*B^12"
    assert target["raw_DRED_background_space"]["status"] == (
        "ADMITTED_AS_REGULATOR_COEFFICIENT_SPURION_NOT_AS_NEW_BACKGROUND_FIELD"
    )
    assert target["physical_4d_quotient"] == {
        "q4d_tau": "0",
        "q4d_E_tau": "0",
        "physical_4d_coefficient_reported": False,
    }


def test_open_tau_projector_and_n3_schedule_are_absent() -> None:
    payload = build_payload()
    projector = payload["target"]["executable_projector"]
    assert projector["full_tau_projector_matrix_built"] is False
    assert projector["open_tau_placements_in_contracted_ledger"] is False
    assert projector["tau_tensor_token_present"] is False
    assert projector["rank_five_color_projection_covered"] is False
    assert projector["scheduled_WW_compiler_is_triangle_only"] is True
    assert payload["pinch_gate"]["n3_pinch_generation_exists"] is False


def test_no_amplitude_pole_or_coefficient_is_claimed() -> None:
    payload = build_payload()
    boundary = payload["coefficient_boundary"]
    assert payload["status"] == "BLOCKED_MISSING_COMPLETE_N3_PROJECT_GRAMMAR"
    assert boundary["preintegration_amplitude"] == "NOT_CONSTRUCTED"
    assert boundary["bare_UV_local_pole"] == "NOT_COMPUTED"
    assert boundary["raw_DRED_E_tau_zero_or_nonzero"] == "NOT_DERIVED"
    assert boundary["physical_4d_projection"] == "q4d(E_tau)=0"
    assert boundary["coefficient_accepted"] is False
    assert payload["counterterm_gate"]["bare_loop_pole_requires_CT3"] is False
    assert (
        payload["counterterm_gate"]["renormalized_local_coefficient_requires_CT3"]
        is True
    )


def test_all_executable_checks_pass() -> None:
    payload = build_payload()
    assert len(payload["checks"]) == 15
    assert all(payload["checks"].values())
