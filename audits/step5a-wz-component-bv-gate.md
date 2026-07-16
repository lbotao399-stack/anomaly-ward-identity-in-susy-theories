# Step 5A WZ-component BV gate

Status: BLOCKED_CURRENT_AUTHORITY

Authority: UNTRACKED_PROPOSAL_NOT_PROJECT_AUTHORITY

## 1. Exact tangent test

The WZ surface obeys

$$
\mathcal V_E^{\mathrm{WZ}}\big|=0,
\qquad
D_{Ea}\mathcal V_E^{\mathrm{WZ}}\big|=0,
\qquad
\bar D_{E\dot a}\mathcal V_E^{\mathrm{WZ}}\big|=0.
$$

From Step 5A.39,

$$
\mathbf s_E\mathcal V_E
=\frac{\operatorname{ad}_{\mathcal V_E}}
{1-e^{-\operatorname{ad}_{\mathcal V_E}}}
\left(
ie^{-\operatorname{ad}_{\mathcal V_E}}
\widetilde{\mathfrak c}_E
-i\mathfrak c_E
\right).
$$

Because \(\mathcal V_E^{\mathrm{WZ}}\big|=0\) and its degree-one
spinor projections vanish,

$$
(\mathbf s_E\mathcal V_E^{\mathrm{WZ}})\big|
=i(\widetilde{\mathfrak c}_E\big|-\mathfrak c_E\big|),
$$

$$
D_{Ea}(\mathbf s_E\mathcal V_E^{\mathrm{WZ}})\big|
=-iD_{Ea}\mathfrak c_E\big|,
\qquad
\bar D_{E\dot a}(\mathbf s_E\mathcal V_E^{\mathrm{WZ}})\big|
=+i\bar D_{E\dot a}\widetilde{\mathfrak c}_E\big|.
$$

The Euclidean chiral and antichiral ghosts are independent. These
three expressions do not vanish on the admitted ghost domain. Hence

$$
\boxed{
\mathbf s_E\mathcal V_E^{\mathrm{WZ}}
\notin T_{\mathcal V_E^{\mathrm{WZ}}}
\{\mathscr V_E^{\mathrm{WZ}}\}}.
$$

## 2. Exact blockers

$$
\boxed{\mathrm{BLOCKED\_STEP5A\_WZ\_BV\_REDUCTION\_UNDEFINED}}.
$$

Missing: WZ-preserving ghost constraints; induced residual component
BRST and minimal BV action; a canonical BV pushforward; the algebraic
WZ FP determinant and density carrier; the Euclidean component cycle
and Berezinian.

$$
\boxed{
\mathrm{BLOCKED\_STEP5A\_COMPONENT\_TO\_SUPERFIELD\_WW\_EQUIVALENCE\_UNPROVED}}.
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
| step3d_forbids_implicit_wz_restriction | PASS |
| step5a_uses_unrestricted_prepotential | PASS |
| step5a_forbids_component_propagator_inference | PASS |
| euclidean_ghosts_are_independent | PASS |
| wz_lowest_component_is_zero | PASS |
| full_prepotential_brst_rule_exists | PASS |
