# Step 5 ordered (AA) pure-gauge full source/SD orbit

Status: `TARGET_BLIND_EXACT_DWORD_REPLAY__GAUGE_SOURCE_ORBIT_ZERO__DIRECTED_TRIANGLE_MINUS_LAMBDA1_OVER_8_UNCHANGED`.

## 1. Notation

Define

$$
A_c=A_1+gA_2+g^2A_3,
\qquad
\Gamma_-=g\gamma_1+g^2\gamma_2,
$$

$$
X=D_+u,
\quad
C=Xu-uX,
\quad
E=Xu^2-2uXu+u^2X,
$$

$$
Y=\bar D^2X,
\qquad
Z=\bar D^2C,
\qquad
H=\bar D^2E.
$$

The exact source words are

$$
A_1=-\frac{\sqrt2}{8}D_+Y,
$$

$$
A_2=-\frac18D_+Z-\frac14(XY+YX),
$$

$$
A_3=-\frac{\sqrt2}{24}D_+H
-\frac{\sqrt2}{8}(XZ+ZX+CY+YC),
$$

$$
\gamma_1=\sqrt2D_-u,
\qquad
\gamma_2=(D_-u)u-uD_-u.
$$

For a loop numerator (N(k)), write

$$
N(k)=C_{\mu\nu}k^\mu k^\nu+L_\mu k^\mu+N_0.
$$

The scalar four-dimensional square is present only when

$$
\operatorname{tr}_4C\ne0.
$$

Its DRED cutting remainder is

$$
\mu_k^2:=\bar k^2-k_d^2.
$$

## 2. Order-(g^2) resolvent

The complete gauge source orbit is

$$
\boxed{
\langle I_2\rangle_0
-\frac1\hbar\langle I_1S_{g3}\rangle_0
-\frac1\hbar\langle I_0S_{g4}\rangle_0
+\frac1{2\hbar^2}\langle I_0S_{g3}S_{g3}\rangle_0.}
$$

No contact term is declared to be a cut before its shared-edge (D)-word is evaluated.

## 3. Independent momentum and color frame

Use

$$
p_A=(1,0,0,0),
\qquad
q_D=(0,1,0,0),
\qquad
P=p_A+q_D=(1,1,0,0),
$$

$$
\varepsilon_A=(0,0,0,1),
\qquad
\dot a=0,
\qquad
z:=k_0-ik_1.
$$

For (SU(2)), (T_a=\sigma_a/2), source colors ((A,B)=(0,1)), and output colors ((D,A)=(1,0)),

$$
\mathbb F^{01}{}_{10}=2,
$$

$$
A_{\mathrm{lin}}=\frac{\sqrt2}{2},
\qquad
D_{\mathrm{lin}}=-\frac{\sqrt2}{8}.
$$

Each internal propagator is one shared covariance

$$
-\kappa^{-1}\delta^4(\theta_S-\theta_G).
$$

Placing an independent copy of the same

$$
\delta^4(\theta_S-\theta_G)
$$

at both endpoints would produce the false product ((\delta^4)^2=0); that construction is withdrawn.

## 4. The (\langle I_2\rangle_0) term

The twelve tagged occurrences are

$$
\begin{aligned}
I_2={}&
(D_-A_3)^AA_1^B
[\gamma_1,A_2]^AA_1^B
[\gamma_2,A_1]^AA_1^B\\
&+(D_-A_2)^AA_2^B
[\gamma_1,A_1]^AA_2^B
(D_-A_1)^AA_3^B\\
&+A_3^A(D_-A_1)^B
A_2^A(D_-A_2)^B
A_2^A[\gamma_1,A_1]^B\\
&+A_1^A(D_-A_3)^B
A_1^A[\gamma_1,A_2]^B
A_1^A[\gamma_2,A_1]^B.
\end{aligned}
$$

The exact one-edge component covariance and each internal (SU(2)) color give

$$
\boxed{N_{I_2}(k)=0.}
$$

Independently, its only possible denominator is (k^2), hence every surviving polynomial would be a scaleless tadpole.

## 5. The (-\hbar^{-1}\langle I_1S_{g3}\rangle_0) term

For external (A) at the source and external (D) at the cubic action vertex, the nonzero occurrence words are

$$
\begin{array}{c|c}
\text{source occurrence}&\text{normalized numerator}\\ \hline
A_1^A(D_-A_2)^B&z^2+iz-\dfrac{1+9i}{2}\\[1mm]
A_1^A[\gamma_1,A_1]^B&-3i\\[1mm]
(D_-A_1)^AA_2^B&-\dfrac{1+i}{2}
\end{array}
$$

Thus

$$
N_{A|D}=z^2+iz-1-8i.
$$

For external (D) at the source and external (A) at the cubic action vertex,

$$
\begin{array}{c|c}
\text{source occurrence}&\text{normalized numerator}\\ \hline
(D_-A_2)^AA_1^B&-z^2+z-1\\[1mm]
A_2^A(D_-A_1)^B&5i
\end{array}
$$

Thus

$$
N_{D|A}=-z^2+z-1+5i.
$$

The quadratic Hessians are

$$
H_{A|D}=
\begin{pmatrix}
2&-2i&0&0\\
-2i&-2&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

$$
H_{D|A}=
\begin{pmatrix}
-2&2i&0&0\\
2i&2&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

Therefore

$$
N_{A|D}+N_{D|A}=(1+i)z-2-3i,
$$

$$
\boxed{H_{A|D}+H_{D|A}=0.}
$$

The two denominators are different:

$$
\frac{N_{A|D}(k)}{k^2(k-q_D)^2},
\qquad
\frac{N_{D|A}(k)}{k^2(k-p_A)^2}.
$$

Thus the Hessian sum is only an occurrence-numerator identity; it is not used to cancel the two fractions.  The anomaly verdict follows separately from

$$
\boxed{
\operatorname{tr}_4H_{A|D}=2-2=0,
\qquad
\operatorname{tr}_4H_{D|A}=-2+2=0.}
$$

Each bubble numerator is a traceless null tensor (z^2), not a scalar (\bar k^2).  Hence neither bubble produces (\mu_k^2).

## 6. The (-\hbar^{-1}\langle I_0S_{g4}\rangle_0) term

The source contains

$$
I_0=(D_-A_1)^AA_1^B+A_1^A(D_-A_1)^B.
$$

Only the second occurrence survives the ordered (DA) projection.  The chiral and antichiral quartic action words are equal:

$$
N_{4,+}=N_{4,-}=-z^2+(1-i)z.
$$

Thus

$$
N_4=-2z^2+(2-2i)z,
$$

$$
H_4=
\begin{pmatrix}
-4&4i&0&0\\
4i&4&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

$$
\boxed{\operatorname{tr}_4H_4=-4+4=0.}
$$

The quartic word is a traceless (z^2) tensor, not a scalar (\bar k^2).  Therefore its anomaly sector is zero.

## 7. The triangle term

For one directed ordered gauge output,

$$
\begin{aligned}
C_{\triangle}
={}&
\left(\frac1{64}\right)(16)(2)(2)
\left[
\left(-\frac{ig}{4\hbar}\right)
\left(+\frac{ig}{4\hbar}\right)
(-\hbar)^3
\right]\\
&\times(-1)\times(-4)\times\frac1{32\pi^2}\\
={}&-\frac{\hbar g^2}{128\pi^2}.
\end{aligned}
$$

With

$$
\lambda_1=\frac{\hbar g^2}{16\pi^2},
$$

one obtains

$$
\boxed{C_{\triangle}=-\frac{\lambda_1}{8}.}
$$

## 8. Route coverage

The target-blind parent census gives

$$
N_{AA}=42,
\qquad
N_{GG}=36,
\qquad
N_{M_rM_r}=2\times3=6.
$$

Both source endpoints are marked:

$$
N_{AA}^{\mathrm{marked}}=2(42)=84.
$$

The functional gauge Hessians above sum the (36) (G-G) routes and their (72) marked source occurrences.  These counts are used only for exhaustiveness, not for coefficient inference.

## 9. Full gauge result

$$
\begin{array}{c|c}
\text{resolvent term}&\text{anomaly coefficient in }\lambda_1\text{ units}\\ \hline
\langle I_2\rangle_0&0\\
-\hbar^{-1}\langle I_1S_{g3}\rangle_0&0\\
-\hbar^{-1}\langle I_0S_{g4}\rangle_0&0\\
(2\hbar^2)^{-1}\langle I_0S_{g3}S_{g3}\rangle_0&-\dfrac18
\end{array}
$$

Therefore

$$
\boxed{
C_{AA,\mathrm{gauge}}^{\mathrm{full}}
=-\frac{\lambda_1}{8}.}
$$

The source/SD orbit does not change the isolated directed triangle coefficient.

Verification:

```text
python scripts/step5_aa_gauge_full_source_sd_orbit_exact_audit.py \
  --output audits/step5-aa-gauge-full-source-sd-orbit-exact.json
```
