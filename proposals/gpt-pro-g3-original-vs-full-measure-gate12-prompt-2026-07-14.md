# GPT Pro Gate 12 — exact $G_3$ original-measure versus full-measure identity

Gate 11 established that the proposed $G_1$ $N_L$ was a duplicate.  Do not
reopen it.  The only remaining raw scalar discrepancy is now sharply
localized to two purported representations of the same $G_3$ supergraph.

## Locked conventions

$$
D^2=2D_-D_+,qquad
\bar D^2=2\bar D_{\dot+}\bar D_{\dot-},
$$

$$
\delta^4(\theta)=\theta^2\bar\theta^2
=4\theta_+\theta_-\bar\theta_{\dot+}\bar\theta_{\dot-},
\qquad
\int d^4\theta\,\delta^4(\theta)=1.
$$

The propagators already carry

$$
G_{\Phi\widetilde\Phi}
=\frac{\hbar}{16p^2}\bar D^2D^2\delta^4(\theta_{12}).
$$

## Representation O: original antichiral measure

At vertices $(S,M,H)$ the direct sparse word is evaluated with

$$
\int d^4\theta_M,d^2\bar\theta_H,
$$

$$
\mathcal A=D_+\bar D^2D_+\delta_{SM},qquad
\mathcal B=D_+\bar D^2D^2\delta_{SH},qquad
\mathcal P_{MH}=\bar D_M^2D_M^2\delta_{MH}.
$$

The two source marks are $D_-\mathcal A$ and $D_-\mathcal B$.  Direct
coefficient extraction gives

$$
T_\perp=2cW,qquad
c_{\rm before\ measure}=32768,
$$

and uses

$$
\int d^4\theta_M:\frac14,qquad
\int d^2\bar\theta_H:\frac12,qquad
c_O=32768\frac14\frac12=4096.
$$

## Representation F: full-superspace conversion

The older replay converts the $H$ antichiral vertex to a full $d^4\theta_H$
integral by moving an explicit $D_H^2$ onto either adjacent chiral projector.
It uses the same two $1/16$ propagator projectors, the same source marks, and

$$
\int d^4\theta_Md^4\theta_H:\frac14\frac14=\frac1{16}.
$$

Its endpoint-weighted word gives the scale-one coefficient corresponding to

$$
c_F=2048.
$$

Representations O and F are claimed to be the same original Feynman graph.
They cannot differ by two.

## Required derivation

1. Derive from the locked Grassmann conventions, without quoting a textbook,
   the exact identity converting

$$
\int d^2\bar\theta_H\,X\big|_{\theta_H=0}
$$

to a full $d^4\theta_H$ integral when $X$ is attached to a chiral projector.
State every sign and coefficient multiplying $D_H^2$.

2. Apply that identity to both adjacent-line choices in the displayed
$\mathcal A\mathcal B\mathcal P_{MH}$ word.  Keep the two propagator $1/16$
factors outside the $D$-word and show the raw top-monomial coefficient before
and after conversion.

3. For two generic affine frames $(y,z)=(0,0)$ and $(1/3,1/3)$, show
explicitly

$$
N_O(y,z;L)-N_F(y,z;L)=0
$$

as a Grassmann polynomial after the correct conversion, not merely after a
transverse trace.

4. Trace the overall $\hbar/2\,\mathrm{STr}$ exactly.  The two nonzero block
cycles are

$$
G M_2 G H_- G I_{\phi_1u},qquad
G H_- G M_2 G I_{u\phi_1}.
$$

Determine whether these are exactly the two action-order terms canceling the
single $1/2$, or whether a second factor two was inadvertently assigned.

5. End with one exact coefficient:

$$
c_{G_3}=2048\quad\text{or}\quad c_{G_3}=4096,
$$

and identify the first false equality in the rejected route.

Do not use the HT coefficient, residual-$q$ closure, or desired matching.
Do not answer `both conventions are possible`: both routes claim the same
locked graph and propagators.
