# Step-5 residual-$q$ graph-lift audit

## 1. Notation

$$
q_r:=Q^r_{E,+}/\sqrt2,
\qquad
P_{\dot a}:=(\sigma_E^m)_{+\dot a}\mathcal D_m.
$$

The path `[1,2,3]` means $q_3q_2q_1U$.

## 2. Exact conditional external paths

$$
\begin{aligned}
q_rU&=C_r,\\
q_sq_rU&=\frac1{\sqrt2}\varepsilon_{rst}B_t\quad(r<s),\\
q_3q_2q_1U&=-\frac i{\sqrt2}A,\\
P_{\dot a}U&=iD_{\dot a}.
\end{aligned}
$$

| field | application path | exact relation | check |
|---|---|---|---|
| `A` | `1,2,3` | $q_3 q_2 q_1 U=-1/2*i*sqrt(2)*A$ | `PASS` |
| `B1` | `2,3` | $q_3 q_2 U=1/2*sqrt(2)*B1$ | `PASS` |
| `B2` | `1,3` | $q_3 q_1 U=-1/2*sqrt(2)*B2$ | `PASS` |
| `B3` | `1,2` | $q_2 q_1 U=1/2*sqrt(2)*B3$ | `PASS` |
| `C1` | `1` | $q_1 U=C1$ | `PASS` |
| `C2` | `2` | $q_2 U=C2$ | `PASS` |
| `C3` | `3` | $q_3 U=C3$ | `PASS` |
| `Ddot1` | `-` | $P_dot1 U=i*Ddot1$ | `PASS` |
| `Ddot2` | `-` | $P_dot2 U=i*Ddot2$ | `PASS` |

$$
(-1)^{\kappa(X,Y)}=(-1)^{\epsilon_X|I_Y|}.
$$

The emitted JSON contains all 81 ordered pair rows and all 16 family channels.  Every joint compact coefficient obeys

$$
c_{X,Y}=(-1)^{\epsilon_X|I_Y|}c_Xc_Y.
$$

## 3. Raw WW obstruction

$$
q_r(A^AA^B)
=(q_rA^A)A^B+A^A(q_rA^B)
=0+0
=0.
$$

Hence the forward $q$-orbit of the raw WW external word contains only `A__A`; the other $80$ ordered component pairs are not generated.

The WW seed has exactly eight endpoint $D$-words.  The candidate IR has

$$
N_{\rm orbit}=66,
\qquad
N_{\rm object}=132,
\qquad
N_{\rm non-AA\ orbit}=58,
$$

but only 1 action-vertex/edge template and no common member field among

`edge_transformations, flavour_or_dotted_permutation, koszul_sign, q_path, raw_derivative_words, vertex_transformations`.

Therefore these are compact-kernel/cut representatives, not raw $q$-lifted graphs.

## 4. Missing raw words

| id | state | required word |
|---|---|---|
| `RAW-Q-PARENT-UU` | `BLOCKED_U_SOURCE_VERTEX_UNDEFINED` | the ordered bare U>U insertion and all of its quantum-port functional derivatives |
| `RAW-Q-INVERSE-DESCENT` | `BLOCKED_INVERSE_Q_DESCENT_UNDEFINED` | an explicit h_r on raw graph words with q_r h_r+h_r q_r equal to the required lower-letter projector |
| `RAW-Q-QUANTUM-PORTS` | `BLOCKED_QUANTUM_Q_ACTION_UNDEFINED` | q_r on every background-split quantum port v, Phi_s, tildePhi_s, c, tilde-c, antighost, multiplier, and NK field |
| `RAW-Q-WW-VERTICES` | `BLOCKED_VERTEX_Q_IMAGES_UNDEFINED` | q_r[+(i*g/2)c_UCD tildeW^D_dotgamma(barD_C^dotgamma-barD_U^dotgamma)] and q_r[-(i*g/2)c_VC'E W^{E gamma}(D_C',gamma-D_V,gamma)] resolved into the ordered gauge, tildePhi*V^n*Phi, Phi^3, and tildePhi^3 word basis |
| `RAW-Q-EDGES` | `BLOCKED_EDGE_Q_INTERTWINER_UNDEFINED` | the endpoint identity q_r^(1)G+(-1)^epsilon G q_r^(2) for vector, chiral, antichiral, fermion, ghost, and mixed edges |
| `RAW-Q-SOURCE` | `BLOCKED_SOURCE_Q_IMAGES_UNDEFINED` | q_r[(D_-K_+v^A)(K_+v^B)+(K_+v^A)(D_-K_+v^B)] together with nonlinear-letter, one-link, two-link, and endpoint source vertices |
| `RAW-Q-CUT` | `BLOCKED_CUT_Q_INTERTWINER_UNDEFINED` | q_r on each of the eight WW endpoint D-words and on every contact/link completion row, with [q_r,C_cut] evaluated |
| `RAW-Q-GAUGE-COMPLETION` | `BLOCKED_GAUGE_FIXING_COMPENSATOR_UNDEFINED` | the compensating BRST word, if nonzero, in q_r(S_gf+S_FP+S_NK+measure) |

## 5. Falsification

| mutation | required failure | result |
|---|---|---|
| `FLIP_B2_EPSILON_SIGN` | `Q_PATH::B2` | `PASS` |
| `DROP_DDOT2_LIFT` | `LETTER_LIFT_COVERAGE` | `PASS` |
| `FLIP_B1_C1_KOSZUL` | `PAIR_KOSZUL::B1__C1` | `PASS` |
| `MAKE_qA_NONZERO` | `WW_SEED_Q_CLOSED` | `PASS` |
| `DELETE_WW_ENDPOINT_WORD` | `WW_ENDPOINT_WORD_COUNT` | `PASS` |
| `INVENT_VERTEX_TRANSFORM_WITHOUT_QUANTUM_q` | `UNSUPPORTED_GRAPH_TRANSFORM` | `PASS` |

$$
\boxed{\mathrm{status}=
\mathrm{BLOCKED\_RAW\_GRAPH\_Q\_EQUIVARIANT\_LIFT}}
$$
