# Step 6 typed DRED numerator reducer

`PROPOSAL_ONLY_BLOCKED_ON_STEP5_ACCEPTANCE`

## 1. Metric types

$$
\delta_{(4)}^{mn}=\widehat\delta^{mn}+\widetilde\delta^{mn},
\qquad
\widehat\delta\widetilde\delta=0.
$$

$$
\operatorname{tr}\delta_{(4)}=4,
\qquad
\operatorname{tr}\widehat\delta=d=4-2\epsilon,
\qquad
\operatorname{tr}\widetilde\delta=2\epsilon.
$$

$$
\text{spin/D algebra}:\ \delta_{(4)},
\qquad
\text{loop tensor averaging}:\ \widehat\delta.
$$

## 2. Rank two

$$
\int q_i^m q_j^nF
=\frac{\widehat\delta^{mn}}{d}
\int(q_i\cdot q_j)F.
$$

## 3. Rank four

$$
T^{mnrs}
=A\widehat\delta^{mn}\widehat\delta^{rs}
+B\widehat\delta^{mr}\widehat\delta^{ns}
+C\widehat\delta^{ms}\widehat\delta^{nr}.
$$

$$
\begin{aligned}
X&=d^2A+dB+dC,\\
Y&=dA+d^2B+dC,\\
Z&=dA+dB+d^2C,
\end{aligned}
$$

$$
\begin{aligned}
A&=\frac{(d+1)X-Y-Z}{d(d-1)(d+2)},\\
B&=\frac{-X+(d+1)Y-Z}{d(d-1)(d+2)},\\
C&=\frac{-X-Y+(d+1)Z}{d(d-1)(d+2)}.
\end{aligned}
$$

For one centered vector,

$$
\int q^mq^nq^rq^sF
=\frac{
\widehat\delta^{mn}\widehat\delta^{rs}
+\widehat\delta^{mr}\widehat\delta^{ns}
+\widehat\delta^{ms}\widehat\delta^{nr}
}{d(d+2)}\int(q^2)^2F.
$$

## 4. Contact subtraction gate

$$
+C\widehat\delta^{mn}-C\delta_{(4)}^{mn}
=-C\widetilde\delta^{mn}.
$$

Proof hash:

`155b166f76b0d55b2df40c14697eb2cc9c52434827600ba68075027e7ebb2b0b`

No master integral, UV pole, or anomaly coefficient is evaluated.
