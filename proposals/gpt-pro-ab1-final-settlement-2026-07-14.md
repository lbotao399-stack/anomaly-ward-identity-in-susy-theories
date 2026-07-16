# GPT Pro AB1 final-settlement response

Status: `NON_AUTHORITY_PRO_REVIEW`

- Chat: https://chatgpt.com/c/6a56596b-5448-83e8-9284-5a6e4fc5dc65
- Gate: `final`
- Prompt: `/Users/libotao/.codex/procodex/2026-07-14-awi-ab1-pair-standard-feynman/final-settlement-prompt.md`
- Prompt SHA-256: `d179b8b7b80d902b7789cab3d7cfed13a6e96ef2ee152c82028883e57c88853c`
- Rendered-body SHA-256: `fee6749983d7e0ca4a64f43eac2cacf5b0027d91e70f3b3acbd9025e0954746f`
- GPT Pro reported elapsed time: `2m 16s`

The response below is evidence for adjudication only.  It is not Project authority.

---

# `ACCEPTED`

**Review status:** `NON_AUTHORITY_PRO_REVIEW`

1. **Exact reduced Euclidean propagators**
$$
\boxed{
\langle u^A(p,1)u^B(-p,2)\rangle_E
=
-\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12})
}
$$
$$
\boxed{
\langle\phi_r^A(p,1)\widetilde\phi_s^B(-p,2)\rangle_E
=
+\delta_{rs}
\frac{\hbar\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_{12})
}
$$
2. **Stripped chiral-frame words**
With
$$
D:=D_+,\qquad X:=Du,
$$
$$
C:=Xu-uX,\qquad
E:=Xu^2-2uXu+u^2X,
$$
$$
Y:=\bar D^2X,\qquad
Z:=\bar D^2C,\qquad
H_u:=\bar D^2E,
$$
one has
$$
\Gamma_+
=
\sqrt2gX+g^2C+\frac{\sqrt2}{3}g^3E+O(g^4),
$$
$$
A_c=A_1+gA_2+g^2A_3+O(g^3),
$$
$$
A_1=-\frac{\sqrt2}{8}DY,
$$
$$
A_2=-\frac18DZ-\frac14(XY+YX),
$$
$$
A_3
=
-\frac{\sqrt2}{24}DH_u
-\frac{\sqrt2}{8}(XZ+ZX+CY+YC),
$$
$$
B_{1,c}=B_{11}+gB_{12}+g^2B_{13}+O(g^3),
$$
$$
B_{11}=D\phi_1,
$$
$$
B_{12}=\sqrt2(X\phi_1-\phi_1X),
$$
$$
B_{13}=C\phi_1-\phi_1C.
$$
3. **Restricted stripped-source counting**
$$
\#\text{words at }g^0,g^1,g^2=1,3,6,
$$
$$
\#\text{ordered distinct-port pairs}=2,18,72,
$$
$$
2+18+72=92.
$$
This is only a **coarse stripped chiral-frame source port-pair count**. It is neither an occurrence-resolved Hessian census nor the Project vector-frame census.
4. **Primitive antichiral flavor ratio**
$$
\boxed{
G_{3,2}:G_{3,3}=+1:-1
}
$$
This fixes only relative antisymmetry. It does not fix the common sign, magnitude, phase, or renormalized output.
5. **Conditional Q4S trace factor**
$$
A_\epsilon
=
\frac{\mu^{2\epsilon}\Gamma(\epsilon)}
{2(4\pi)^{2-\epsilon}}
\int_{\Sigma_2}dy\,dz\,\Delta^{-\epsilon},
$$
$$
\boxed{
\operatorname{Res}_{\epsilon=0}A_\epsilon
=
\frac1{64\pi^2}
}
$$
and only when a graph-specific numerator produces $4-d$,
$$
\boxed{
\lim_{\epsilon\to0}(4-d)A_\epsilon
=
\frac1{32\pi^2}.
}
$$
No ordered $AB_1$ occurrence has yet produced this numerator.
6. **Physical versus stripped normalization**
$$
\mathcal O_{\rm str}^{AB}
=
A_c^A[\tau_wB_{1,c}]^B,
$$
$$
\boxed{
\mathcal O_{\rm phys}^{AB}
=
g^2\mathcal O_{\rm str}^{AB}.
}
$$
No admitted convention fixes whether $J$ absorbs this $g^2$.
7. **Required vector-frame letters**
$$
\boxed{
A_V=\mathcal B_{\rm ad}A_c\mathcal B_{\rm ad}^{-1},
\qquad
B_{1,V}=\mathcal B_{\rm ad}B_{1,c}.
}
$$
Bridge expansions add gauge-field ports and may change the source census.
8. **Conditional resolvent signs**
Only under
$$
\mathbb K_J=\mathbb K+V-JI,
\qquad
I=\mathcal O_{\rm str}'',
$$
$$
\Gamma_J^{(1)}
=
-\left.
\frac{\overleftarrow\partial\Gamma^{(1)}}{\partial J}
\right|_{J=0},
$$
with $V_{[n]}$ and $I_{[n]}$ defined as $1/n!$ background Taylor coefficients, the formal relative signs are
$$
\boxed{+,-,-,+}.
$$
Reversing the source-derivative convention reverses the entire insertion line.

# `REJECTED`

1. The previously used reversed reduced-propagator signs
$$
\langle u^Au^B\rangle_E
=
+\frac{\hbar\kappa^{AB}}{p^2}\delta^4(\theta_{12}),
$$
$$
\langle\phi_r^A\widetilde\phi_s^B\rangle_E
=
-\delta_{rs}
\frac{\hbar\kappa^{AB}}{16p^2}
\bar D_1^2D_1^2\delta^4(\theta_{12})
$$
are rejected.
2. Every previously stated numerical pre-$D$ parent coefficient depending on those signs is rejected, including
$$
C_{G_2}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{2048},
$$
$$
C_{G_{3,2}}^{\rm preD}
=
+\frac{\hbar\sqrt2\,g^2}{2048},
$$
$$
C_{G_{3,3}}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{2048},
$$
$$
C_{S;AE}^{\rm preD}
=
C_{S;EA}^{\rm preD}
=
-\frac{\hbar\sqrt2\,g^2}{256},
$$
$$
C_{M-I_1}^{\rm loop}
=
+\frac{\hbar\sqrt2\,g^2}{32},
$$
and
$$
C_{G_1}^{\rm preD}
=
+\frac{\hbar g}{128}\mathcal G_{abc}.
$$
3. Any claim that
$$
92
$$
is a complete Project occurrence census, complete Project Hessian census, or Project vector-frame census is rejected.
4. Any multiplication of an $AB_1$ graph by
$$
\frac1{32\pi^2}
$$
before its occurrence-resolved $D$-word produces the graph-specific $4-d$ numerator is rejected.

# `BLOCKED`

```
BLOCKED_NO_ADMITTED_AB1_TREE_GRAPH_DRED_RESULT
BLOCKED_LOCKED_ORDERED_BILOCAL_SOURCE
BLOCKED_AB1_SOURCE_OVERALL_G_NORMALIZATION
BLOCKED_CHIRAL_TO_VECTOR_FRAME_SOURCE_BRIDGE
BLOCKED_SOURCE_COUPLING_INSERTION_SIGN
BLOCKED_LOCKED_BACKGROUND_QUANTUM_PORT_GRAMMAR
BLOCKED_SOURCE_HESSIAN_LEFT_RIGHT_AND_TAYLOR_NORMALIZATION
BLOCKED_LOCAL_PROPOSAL_LINK_CONNECTION_U_LIFT
BLOCKED_VVV_ORDERED_HESSIAN
BLOCKED_COMPLETE_RAW_PORT_WORDS_FOR_NAMED_SECTOR_TABLE
BLOCKED_TYPED_ORIENTED_EDGE_KERNEL_ASSIGNMENT
BLOCKED_AB1_OCCURRENCE_RESOLVED_DWORD_TRACES
BLOCKED_DESCENDANT_CONTACT_HESSIANS_UNSPECIFIED
BLOCKED_STEP5A_UNIQUE_PROPAGATORS_PERTURBATIVE_SLICE_UNFIXED
BLOCKED_STEP5A_NK_BRANCH_UNSELECTED
BLOCKED_STEP5A_MOMENTUM_RULES_FOURIER_DRED_LEDGER_UNFIXED
BLOCKED_LOCKED_Q4S_SPINOR_REALIZATION
BLOCKED_OPEN_COLOR_SOURCE_BV_EXTENSION
BLOCKED_ONE_LOOP_COMPOSITE_Z_MATRIX
BLOCKED_EOM_AND_TOTAL_DERIVATIVE_QUOTIENT
BLOCKED_TOTAL_PROJECT_HT_COMPONENT_INTERTWINER
```

$$
\boxed{
(c_{DB},c_{BD},c_{32},c_{23})_{\rm Project}
=
\texttt{UNDEFINED}.
}
$$

