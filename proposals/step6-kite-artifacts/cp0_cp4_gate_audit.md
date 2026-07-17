# CP0--CP4 fast-engine gate audit

Status: `NON_AUTHORITY_PROPOSAL` at checkout `cca5d343f9bd575c5cfef89fcc4ccc092f9a1e23`.
Admissible authority head: `origin/main=06601a0ed4e6060e2d872980509e1b949e61506c`.
Scope: CP0 and the mandatory CP1 go/no-go gate only.  No web, Notion, GPT formula,
or unallowed repository was used.  Equations are numbered (CP.$n$).

## 1. Fast realization and CP0

Grassmann monomials are integer bitmasks.  Coefficients are sparse polynomials over
$\mathbb Q(i)$ with `Fraction` coefficients.  At point $s$,

$$
D_a^{(s)}=\partial_{\theta_s^a}+\mathsf p_{a\dot b}(r_{\rm in})\bar\theta_s^{\dot b},
\qquad
\bar D_{\dot b}^{(s)}=\partial_{\bar\theta_s^{\dot b}}
+\theta_s^c\mathsf p_{c\dot b}(r_{\rm in}),
\tag{CP.1}
$$

$$
D^2=2D_-D_+,\qquad \bar D^2=2\bar D_{\dot1}\bar D_{\dot2},\qquad
\theta^2=-2\theta^+\theta^-,\qquad
\bar\theta^2=2\bar\theta^{\dot1}\bar\theta^{\dot2}.
\tag{CP.2}
$$

Exact machine output:

| anchor | result |
|---|---:|
| $(D^2\theta^2)|=-4$ | `PASS`, $-4$ |
| $(\bar D^2\bar\theta^2)|=-4$ | `PASS`, $-4$ |
| $[D^2\bar D^2\delta^4]|=16$ | `PASS`, $16$ |
| $\delta_{01}^4D^2\bar D^2\delta_{01}^4=16\delta_{01}^4$ | `PASS`, 16 masks |
| closed loop with $<2D$ and $<2\bar D$ | `PASS`, 13 words |

Thus CP0 passes:

$$
\boxed{\mathrm{CP0}=\mathrm{PASS}}.
\tag{CP.3}
$$

The seed arithmetic factor also passes:

$$
w_D=\left(-\frac18\right)\left(-\frac14\right)(16)(2)(2)
=\frac1{32}(16)(2)(2)=2.
\tag{CP.4}
$$

## 2. CP1 expected endpoint ledger

The locked arithmetic ledger requires

$$
\begin{array}{c|c|c|c}
\mathrm{id}&D_-\text{ placement}&\bar D\text{ endpoint}&D\text{ endpoint}\\ \hline
\mathrm{WW\!\!-DA\!\!-01}&A&r_0&r_1\\
\mathrm{WW\!\!-DA\!\!-02}&A&r_0&r_2\\
\mathrm{WW\!\!-DA\!\!-03}&A&r_1&r_1\\
\mathrm{WW\!\!-DA\!\!-04}&A&r_1&r_2\\
\mathrm{WW\!\!-DA\!\!-05}&B&r_0&r_1\\
\mathrm{WW\!\!-DA\!\!-06}&B&r_0&r_2\\
\mathrm{WW\!\!-DA\!\!-07}&B&r_1&r_1\\
\mathrm{WW\!\!-DA\!\!-08}&B&r_1&r_2
\end{array},
\qquad
r_0=k,\quad r_1=k+q,\quad r_2=k+p+q.
\tag{CP.5}
$$

Every row is asserted to reduce to

$$
(r_i)_{+\dot\beta}\,\mathsf p^{\dot\beta\gamma}(p)\,
(r_j)_{\gamma}{}^{\dot\alpha}\,
\widetilde W_{\dot\alpha}(q)X(p),
\qquad X=D_+W_+,
\tag{CP.6}
$$

and the four rows of either placement are asserted to sum to

$$
L_1=2k+q,\qquad L_2=2k+p+2q.
\tag{CP.7}
$$

## 3. Minimal exact trace: WW-DA-01

For $\dot\alpha=\dot1$, $a=+$, the odd source order
$(0,2,3,5,6)$ becomes $(0,3,6,2,5)$.  The inversions
$(3,2),(6,2),(6,5)$ give $(-1)^\kappa=-1$.  The generated receipt records every
rightmost-first operator stage.  After the two Berezin integrals, vertex factor
$+1/4$, and canonical color sign $-1$, this spin branch contains 3666 exact
coefficient monomials:

$$
\boxed{(-1)^\kappa=-1,\qquad n_{\rm branch}=3666.}
\tag{CP.8}
$$

## 4. First explicit rule divergence

Impose the chiral/antichiral constraints on the external strengths, but no unrecorded
EOM or on-shell quotient.  The same WW-DA-01 word has four independent jet rows:

$$
\begin{aligned}
R_{\dot1,-}={}&
2k_{00}k_{01}k_{11}-2k_{01}^2k_{10}
-2k_{01}k_{10}(p_{01}+q_{01})
+2k_{01}k_{11}(p_{00}+q_{00}),\\
R_{\dot1,+}={}&
2k_{01}\big[k_{01}(p_{00}+q_{00})-k_{00}(p_{01}+q_{01})\big],\\
R_{\dot2,-}={}&
-2k_{00}^2k_{11}+2k_{00}k_{01}k_{10}
+2k_{00}k_{10}(p_{01}+q_{01})
-2k_{00}k_{11}(p_{00}+q_{00}),\\
R_{\dot2,+}={}&
2k_{00}\big[k_{00}(p_{01}+q_{01})-k_{01}(p_{00}+q_{00})\big].
\end{aligned}
\tag{CP.14}
$$

Here $R_{\dot\alpha,-}$ multiplies
$\widetilde W_{\dot\alpha}D_+W^-$ and $R_{\dot\alpha,+}$ multiplies
$\widetilde W_{\dot\alpha}D_+W^+$.  The seed target retains only
$X=D_+W_+=-D_+W^-$ and contains no rule deleting the $W^+$ rows.

The unwanted row is not identically zero.  For

$$
k_{00}=1,\quad k_{01}=2,\quad
p_{00}=7,\quad p_{01}=3,\quad q_{00}=11,\quad q_{01}=5,
\tag{CP.15}
$$

one gets

$$
R_{\dot1,+}=2(2)\big[2(7+11)-1(3+5)\big]=4(36-8)=112.
\tag{CP.16}
$$

Even if the $W^+$ row is deleted by hand, $R_{\dot1,-}$ contains

$$
2k_{00}k_{01}k_{11}-2k_{01}^2k_{10},
\tag{CP.17}
$$

which contains no external $p$.  The asserted seed row
$r_0\,p\,r_1$ contains one external $p$ in every monomial.  Therefore no overall
sign, phase, or isomorphic scalar dictionary can map (CP.14) to (CP.6):

$$
R_{\mathrm{WW-DA-01}}\ne z\,S(r_0,r_1),\qquad
z\in\left\{\frac12,-\frac12,\frac i2,-\frac i2\right\}.
\tag{CP.18}
$$

The independent prepotential-generated fast engine gives `False` for all four values
of $z$; thus the mismatch is still present after constructing $W$ and
$\widetilde W$ directly from canonical prepotentials rather than treating them as
unconstrained superfields.

## 5. Eight-row comparison

| id | exact difference monomials | $\pm1/2,\pm i/2$ dictionary |
|---|---:|---:|
| WW-DA-01 | 18690 | all false |
| WW-DA-02 | 23890 | all false |
| WW-DA-03 | 31110 | all false |
| WW-DA-04 | 34092 | all false |
| WW-DA-05 | 25466 | all false |
| WW-DA-06 | 20993 | all false |
| WW-DA-07 | 34498 | all false |
| WW-DA-08 | 27829 | all false |

The prepotential-generated total differences are 36099 monomials for placement $A$
and 37058 for placement $B$.  The older independent engine gives the same qualitative
result after its 48 chirality substitutions: all eight endpoint rows are outside the
$S(r_i,r_j)$ span.  Its exact internal Leibniz check nevertheless passes:

$$
R_A+R_B=D_-T,\qquad R_A+R_B\ne-D_-T.
\tag{CP.19}
$$

Thus the discrepancy is not ordinary Leibniz failure.

## 6. First missing typed dependency

The allowed seed itself states that its endpoint signs are conditional and that the
two mixed-anticommutator factors are arithmetic inputs, not outputs of an explicit
word trace.  The first missing dependency is

$$
\boxed{\texttt{BLOCKED\_EXPLICIT\_WW\_D\_ALGEBRA\_WORD\_DERIVATION}}.
\tag{CP.20}
$$

To select the eight-row seed from the full off-shell trace, an authoritative input must
define all of the following:

1. the source-ordered representative noncommutative $D$-word;
2. every graded IBP transfer and its sign;
3. the external projection $\Pi_{\widetilde W\otimes X}$;
4. the Bianchi/EOM/contact quotient that removes
   $\widetilde W D_+W^+$, $\widetilde W D_-W^-$, and
   $(\bar D\widetilde W)(D^2W)$;
5. the phase dictionary between $\mathsf p=-i\sigma_E\cdot p$ and the vector
   $\sigma_E\bar\sigma_E\sigma_E$ tensor.

None is fixed by the five CP0 anchors.  Choosing one silently would change the CP3
numerator and CP4 anomaly split.

Therefore

$$
\boxed{\mathrm{CP1}=\mathrm{BLOCKED}},\qquad
\boxed{\mathrm{CP2},\mathrm{CP3},\mathrm{CP4}=\mathrm{NOT\ RUN}}
\tag{CP.21}
$$

by the mandatory ordering of SPEC §6.

## 7. Reproduction commands

```text
/usr/bin/time -p python3 proposals/step6-kite-artifacts/engine_A/calib0.py
/usr/bin/time -p python3 proposals/step6-kite-artifacts/engine_A/calib1.py
python3 l1match.py                                  # cwd engine_A; 9 s
python3 l1final.py                                  # cwd engine_A
python3 l1ledger.py                                 # cwd engine_A
python3 l1leibniz.py                                # cwd engine_A
/usr/bin/time -p python3 proposals/step6-kite-artifacts/fast_cp0_cp1_engine.py
/usr/bin/time -p python3 proposals/step6-kite-artifacts/fast_cp1_minimal_trace.py
```

Artifacts:

- `fast_cp0_cp1_engine.py` — bitmask + `Fraction` CP0/CP1 engine;
- `generated/cp0_cp4_fast_gate_report.json` — five anchors, eight row comparisons, random exact components;
- `fast_cp1_minimal_trace.py` — one-word operator trace;
- `generated/cp0_cp4_cp1_minimal_trace.json` — factor order, Koszul inversions, every operator stage.
