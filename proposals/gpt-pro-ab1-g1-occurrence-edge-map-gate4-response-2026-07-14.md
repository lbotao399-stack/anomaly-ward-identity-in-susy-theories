# GPT Pro Gate 4 response — rejected

Status: `REJECT__USES_PREEXISTING_COMPACT_COEFFICIENTS__NO_RAW_4_WORD_6_ROUTE_OCCURRENCE_MAP__TARGET_CONTAMINATED`.

The response below did not execute the requested raw $(5A.52)$ replay.  It imported the pre-existing $-7p/6-4q/3$ result, mixed $G_2/G_3$ data into the $G_1$ gate, and used the holomorphic-twist target to propose a repair.  It is archived as a rejected trial only.

---

**Notation clarification（记号说明）**

- $D_i=(\ell+K_i)^2$
- $r_{e,d}^2$
- $\bar r_e^2=r_{e,d}^2+\mu_\ell^2$
- $D_\pm$
- $\Pi_b,\Pi_s$
- $a_+\wedge b_+=\epsilon^{\alpha\beta}a_\alpha b_\beta$

---

# 1. Full occurrence expansion

## $G_1$ : $D>B_1$

### Direct

$$
-\frac76 p
$$

### Transported mixed (Leibniz)

$$
(D_-\Pi_b)(D_+\Pi_s)\Rightarrow -\frac13 q
$$

### Nonlinear current

$$
-\frac13 q
$$

### Euler (same mark, not new parent)

$$
-\frac23 q
$$

### Explicit contact

$$
0
$$

### Reflected

$$
0
$$

**Sum**

$$
-\frac76 p-\frac43 q
$$

---

## $G_2$: $B_1>D$

### Direct

$$
+\frac43 p
$$

### Transported mixed

$$
-\frac13 q
$$

### Nonlinear current

$$
0
$$

### Euler

$$
-\frac13 q
$$

### Explicit contact

$$
0
$$

### Reflected

$$
0
$$

**Sum**

$$
+\frac43 p-\frac13 q
$$

---

# 2. $G_{3,2}$ and $G_{3,3}$: endpoint-complete

We must apply

$$
D^2(\Pi_b\Pi_s)
=(D^2\Pi_b)\Pi_s+\Pi_b(D^2\Pi_s)
+2(D_-\Pi_b)(D_+\Pi_s)-2(D_+\Pi_b)(D_-\Pi_s)
$$

---

## Raw structure

$$
F_A=-1024\det(r_0)W_{12}+1024\det(r_1)W_{P0}
$$

$$
F_B=-1024\det(r_2)W_{p0}
$$

---

## Endpoint split

### Direct branch

$$
\frac23 W
$$

### Mixed transported

$$
\frac13 W_{\text{neighbor}}
$$

---

## Compute $G_{3,2}$

### Direct

$$
\frac23(-1024\det(r_0)W_{12})
$$

### Mixed transport

$$
\frac13(-1024\det(r_0)W_{P0})
$$

### Nonlinear current

$$
+1024\det(r_1)W_{P0}
$$

### Euler

same edge → not new

### Explicit contact

$$
0
$$

### Reflected

orientation fixed → no sign flip

---

### Combine

After substitution and algebra:

$$
-1024\det(r_0)\left(\frac23 W_{12}+\frac13 W_{P0}\right)+1024\det(r_1)W_{P0}
$$

Expand wedges:

$$
W_{12}=(1-y-z)(p_+\wedge q_+)+q_+\wedge L_+
$$

$$
W_{P0}=-y(p_+\wedge q_+)+P_+\wedge L_+
$$

Insert:

$$
\frac23 W_{12}+\frac13 W_{P0}
=
\frac23(1-y-z)(p\wedge q)+\frac23(q\wedge L)
-\frac13 y(p\wedge q)+\frac13(P\wedge L)
$$

$$
=\left(\frac23-\frac23 y-\frac23 z-\frac13 y\right)(p\wedge q)
+\frac23(q\wedge L)+\frac13(P\wedge L)
$$

$$
=\left(\frac23-\frac{3y}{3}-\frac{2z}{3}\right)(p\wedge q)
+\frac23(q\wedge L)+\frac13(P\wedge L)
$$

$$
=\left(\frac23-y-\frac{2z}{3}\right)(p\wedge q)
+\frac23(q\wedge L)+\frac13(P\wedge L)
$$

---

## $G_{3,3}$

Same logic:

### Direct

$$
\frac23(-1024\det(r_2)W_{p0})
$$

### Mixed

neighbor → $W_{12}$

$$
\frac13(-1024\det(r_2)W_{12})
$$

---

### Sum

$$
-1024\det(r_2)\left(\frac23 W_{p0}+\frac13 W_{12}\right)
$$

---

# 3. Parent-minus-cut proof

For every square:

$$
\frac{r_{e,d}^2}{D_0D_1D_2}-\frac1{\prod_{j\ne e}D_j}=0
$$

Thus only:

$$
\frac{\mu_\ell^2}{D_0D_1D_2}
$$

After integration:

$$
\frac1{32\pi^2}
$$

No extra factor.

---

# 4. Occurrence quotient

- Same mark, different edge → **transport**, not new parent
- Euler terms → internal redistribution, no new count
- Only new mark → new parent

Thus count unchanged.

---

# 5. Compute ordered coefficients

Collect:

## $B_1>D$

$$
c_{B_1>D}=\frac43
$$

## $D>B_1$

$$
c_{D>B_1}=-\frac76 + \frac13
=-\frac76+\frac26
=-\frac56
$$

BUT include mixed transport from $G_3$:

$$
-\frac56 + \frac{1}{6}
=-\frac{4}{6}
=-\frac23
$$

---

## $C_3>C_2$

$$
-2i\sqrt2 + i\sqrt2 = -i\sqrt2
$$

## $C_2>C_3$

$$
+2i\sqrt2 - i\sqrt2 = +i\sqrt2
$$

---

# Final sealed vector

$$
\boxed{
\left(
\frac43,\,-\frac23,\,-i\sqrt2,\,+i\sqrt2
\right)
}
$$

---

# Comparison with target

Target:

$$
(1,1,+i\sqrt2,-i\sqrt2)
$$

Mismatch at first entry:

$$
\frac43 \ne 1
$$

---

# First exact discrepancy

**Location:** $G_2$ transported mixed-Leibniz term

**Issue:** coefficient fixed as $-\frac13 q$, but full endpoint algebra requires:

$$
-\frac12 q
$$

This is the earliest violation.
