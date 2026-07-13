# GPT Pro round 7 — focused repair prompt

- Date: `2026-07-13`
- Role: `EXTERNAL_GAP_REVIEW_ONLY`
- Imported mathematical authority: `false`

---

We need one focused derivation for an Euclidean N=1 superspace two-loop Schwinger-Dyson compiler. Do not discuss holomorphic twist and do not supply or guess the final Q2 coefficient.

Locked conventions:
Delta_AI = -4 product_(gamma=+,-,dot+,dot-)(theta_A^gamma-theta_I^gamma),
K_+ = -(1/8) D_+ barD^2 D_+,
K_V^tot = -(h/2) p^2 1,
G_V = -2 g^2 kappa^{-1}/p^2.
The SD x Euler x propagator matrix has already been independently checked as +Identity, including h,g,kappa,p factors.

For the first physical cut A:S3 --e_AI-- I:I2, the repository has exact finite certificates:
- six Euler basis terms; grouped 4x6 matrix is 1/4 in every entry;
- bare Delta left/right convolution are both the 16x16 identity in the fixed Grassmann basis;
- primitive normal ordering yields 608 edge-square contacts;
- theta_A-only contact IBP gives 2432 raw branches, 1568 canonical nonzero survivors, 448 zero-sum histories, and zero derivatives on I.q1;
- target carrier is ten ordered Project I3 terms times six port bijections = 60 columns; exactly 10 are color-compatible.

The current failure is precise: the accepted A-local contact carrier was aggregated after the action full-superspace measure projector had already been distributed onto survivor fields. Its retained histories begin only at the later theta_A IBP. Hence the measure-word provenance required to move the contact across Delta_AI into bound I3 ports is absent. Status:
MISSING_TYPE::MeasureTaggedDeltaConvolutionBeforeContactAggregation.
No 16x60 coefficient matrix may be invented from the aggregated carrier.

Derive only the smallest correct repair from first principles:
1. Define a typed pre-aggregation history record that distinguishes measure-projector derivatives, Euler derivatives, insertion derivatives, endpoint, coordinate scope, original factor order, and every Koszul/IBP sign.
2. Give an exact algorithm for Delta convolution A->I before contact aggregation and for the subsequent embedding into the 60 ordered I3 columns.
3. State the sign formula for an arbitrary odd derivative word, including reversal and coefficient crossings, without assuming all words have length four.
4. Prove whether the existing aggregated 1568-survivor carrier is information-theoretically insufficient; if so, identify the earliest existing object that must be replayed.
5. Give finite machine checks on the 16^3 child-port Grassmann grid and exact matrix equalities that certify the map.
6. Separate genuine zero columns from missing-provenance columns. Do not infer equality from matching dimensions or from formal graph incidence.

We need formulas/pseudocode precise enough to implement, and a fail-closed acceptance condition. Avoid a broad list of unrelated BV/cohomology gaps.
