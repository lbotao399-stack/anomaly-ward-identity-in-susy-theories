# Step 6 symbolic Grassmann oracle

`PROPOSAL_ONLY`; `NO_GRAPH_CONTRACTION`; `NO_TWO_LOOP_NUMERATOR`.

$$
\Lambda=\Lambda(\vartheta^+,\vartheta^-,\bar\vartheta_{\dot+},\bar\vartheta_{\dot-}),
\qquad
p_{(4)}^2=p_{+\dot+}p_{-\dot-}-p_{+\dot-}p_{-\dot+}.
$$

$$
\{D_a,\bar D_{\dot b}\}=-2ip_{a\dot b},\qquad
D^2\bar D^2D^2=-16p_{(4)}^2D^2,\qquad
\bar D^2D^2\bar D^2=-16p_{(4)}^2\bar D^2.
$$

$$
\delta^4(\vartheta)=\vartheta^2\bar\vartheta^2
=-4\vartheta^+\vartheta^-\bar\vartheta_{\dot+}\bar\vartheta_{\dot-},
\qquad
[D^2\bar D^2\delta^4(\vartheta)]_{\vartheta=0}=16.
$$

$$
\mathcal W_{(1)+}=-\frac18\bar D^2D_+V,\qquad
X_{(1)}=-\frac18D_+\bar D^2D_+V=K_+V.
$$

The generic graded-bracket fixture certifies outer-scope distribution only.
The component adjoint grammar is instead

$$
[Y,Z]^C=i\,c_{AB}{}^C Y^A Z^B,\qquad
\text{no reverse component term}.
$$

$$
\left(-\frac{i}{2}\right)i=\frac12,\qquad
\left(\frac{i}{16}\right)i=-\frac1{16}.
$$

Checks: `{'checks': 103, 'failed': 0}`.

## Provenance SHA-256

- `contracts/foundations/step-03b-component-reconstruction.md`: `4b3ae678463747cc78d3c7e594904647620d919eae769c5b5bfd16d5b556a75b`
- `contracts/foundations/step-05-euclidean-n4-awi-supergraphs.md`: `dd06ff2ecf0d78605282cbb505daf16797ce859650fc8d398405031f3acdb002`
- `scripts/verify_step5_propagators.py`: `db7ffb109e6a672e9e23c724ba302a1ec7f47d194a7758d13a026329feb0c718`
- `scripts/verify_step5_seed_dalgebra.py`: `ad5dfa5f3d1198e67fd83381606e519f8a3bcadafb5092c6e682384c18dda970`

## Open typed boundary

`BLOCKED_GRAPH_TENSOR_CONTRACTION_INTERFACE_NOT_IMPLEMENTED`.
