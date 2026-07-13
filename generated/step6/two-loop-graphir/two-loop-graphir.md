# Step 6 pure-gauge two-loop GraphIR: topology and routing only

$$
L=I-V+1=2,\qquad (m-2)+\sum_{r\ge 3}(r-2)n_r=4.
$$

- valence solutions: `12`; every item is `VALENCE_NOT_GRAPH`.
- literal K4-minus-edge direct parents: `3`.
- raw marked K2,3 theta lift: one separate six-edge GraphIR.
- amplitude, D-algebra, subtraction, coefficient: `BLOCKED`.

## Literal direct parents

### G6_DIRECT_K4ME_I3_S3CUBED

$$
D=k^2 l^2 (l-p1)^2 (k+l)^2 (k+l+p2)^2.
$$

$$
V=4,\quad I=5,\quad L=2.
$$

### G6_DIRECT_K4ME_I2_S3SQ_S4

$$
D=k^2 (k-P)^2 l^2 (l-p1)^2 (k+l)^2.
$$

$$
V=4,\quad I=5,\quad L=2.
$$

### G6_DIRECT_K4ME_I2_S3SQ_S4_B2_ON_S4

$$
D=k^2 (k-P)^2 l^2 (l-P)^2 (k-l)^2.
$$

$$
V=4,\quad I=5,\quad L=2.
$$

## Raw marked theta lift

$$
(r_{CI},r_{ID},r_{CA},r_{AD},r_{CB},r_{BD})
=(k,k-P,l,l-p_1,-k-l,-k-l-p_2).
$$

$$
D=k^2 (k-P)^2 l^2 (l-p1)^2 (k+l)^2 (k+l+p2)^2.
$$

$$
\gamma_L=\{CI,ID,CA,AD\},\quad
\gamma_R=\{CI,ID,CB,BD\},\quad
\gamma_O=\{CA,AD,CB,BD\}.
$$

`RAW_MARKED_K2_3_THETA_LIFT_NOT_DIRECT_BITRIANGLE`; no collapse certificate is asserted.
