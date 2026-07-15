# GPT Pro Gate 2S final response — AB1 evanescent cutting audit

Status: `NON_AUTHORITY_PRO_REVIEW__PENDING_LOCAL_ADJUDICATION`.

Conversation: `https://chatgpt.com/c/6a5699d2-4e74-83e8-994f-2a50eeb0c043`.

Captured: `2026-07-14`.

The body below is the unedited visible response text returned by GPT Pro.
Notation / 记号
Ppq:=p+∧q+=p+α˙q+α˙,Wij:=ri,+∧rj,+.P_{pq}:=p_+\wedge q_+
=p_{+\dot\alpha}q_+{}^{\dot\alpha},
\qquad
W_{ij}:=r_{i,+}\wedge r_{j,+}.Ppq​:=p+​∧q+​=p+α˙​q+​α˙,Wij​:=ri,+​∧rj,+​.
Σ2={(y,z):y≥0, z≥0, y+z≤1},x:=1−y−z.\Sigma_2=\{(y,z):y\geq0,\ z\geq0,\ y+z\leq1\},
\qquad
x:=1-y-z.Σ2​={(y,z):y≥0, z≥0, y+z≤1},x:=1−y−z.
χ={+1,+ chirality,−1,− chirality.\chi=
\begin{cases}
+1,&+\text{ chirality},\\
-1,&-\text{ chirality}.
\end{cases}χ={+1,−1,​+ chirality,− chirality.​
FABDE:=κAUκBVκCC′cUCDcVC′E.\mathbb F^{AB}{}_{DE}
:=
\kappa^{AU}\kappa^{BV}\kappa^{CC'}
c_{UCD}c_{VC'E}.FABDE​:=κAUκBVκCC′cUCD​cVC′E​.
所有 adjoint-generator phases 均保留在 color route 中；下文的 scalar prefactor 已投影到实的 FABDE\mathbb F^{AB}{}_{DE}FABDE​ convention。
⟨XD,YE⟩:=FABDE(∂+α˙XD)(∂+α˙YE).\langle X^D,Y^E\rangle
:=
\mathbb F^{AB}{}_{DE}
\bigl(\partial_{+\dot\alpha}X^D\bigr)
\bigl(\partial_+{}^{\dot\alpha}Y^E\bigr).⟨XD,YE⟩:=FABDE​(∂+α˙​XD)(∂+​α˙YE).

1. Universal longitudinal transport
把 matter-propagator 的标量 1/161/161/16 留在 scalar prefactor，定义其 numerator projector
Πn:=Dˉn2Dn2δn.\Pi_n:=\bar D_n^2D_n^2\delta_n.Πn​:=Dˉn2​Dn2​δn​.
被丢弃的 word 是
Le∣n=−12∫d4θ (D+Dˉ2D2δe) Πn X.\mathscr L_{e|n}
=
-\frac12
\int d^4\theta\,
\bigl(D_+\bar D^2D^2\delta_e\bigr)\,
\Pi_n\,\mathscr X.Le∣n​=−21​∫d4θ(D+​Dˉ2D2δe​)Πn​X.
对 D2D^2D2 作 superspace IBP，odd endpoint 给出 −1-1−1：
Le∣n=−12(−1)∫d4θ D+Dˉ2δe (D2Dˉ2D2δn) X=−12(−1)(16)∫d4θ D+Dˉ2δe □nD2δn X=8rˉn 2 Te∣n.\begin{aligned}
\mathscr L_{e|n}
&=
-\frac12(-1)
\int d^4\theta\,
D_+\bar D^2\delta_e\,
\bigl(D^2\bar D^2D^2\delta_n\bigr)\,
\mathscr X
\\
&=
-\frac12(-1)(16)
\int d^4\theta\,
D_+\bar D^2\delta_e\,
\Box_nD^2\delta_n\,
\mathscr X
\\
&=
8\bar r_n^{\,2}\,\mathscr T_{e|n}.
\end{aligned}Le∣n​​=−21​(−1)∫d4θD+​Dˉ2δe​(D2Dˉ2D2δn​)X=−21​(−1)(16)∫d4θD+​Dˉ2δe​□n​D2δn​X=8rˉn2​Te∣n​.​
因此被漏掉的 normalization 是严格的
(−12)(−1)(16)=8.\boxed{
\left(-\frac12\right)(-1)(16)=8.
}(−21​)(−1)(16)=8.​
新 occurrence tag 是 neighboring edge nnn，而不是原 edge eee。只有完成 transport 后才写 full-ddd contact：
Ce∣n(d)=8rn,d 2Te∣n.C_{e|n}^{(d)}
=
8r_{n,d}^{\,2}\mathscr T_{e|n}.Ce∣n(d)​=8rn,d2​Te∣n​.
于是
8rˉn 2Te∣n−8rn,d 2Te∣n=8μℓ2Te∣n.\boxed{
8\bar r_n^{\,2}\mathscr T_{e|n}
-
8r_{n,d}^{\,2}\mathscr T_{e|n}
=
8\mu_\ell^2\mathscr T_{e|n}.
}8rˉn2​Te∣n​−8rn,d2​Te∣n​=8μℓ2​Te∣n​.​
若把 rˉn2\bar r_n^2rˉn2​ 替换为 rn,d2r_{n,d}^2rn,d2​，该 row pointwise 等于零。没有任何额外 4−d4-d4−d multiplier。

2. G1=(I,M1,VVV)G_1=(I,M_1,VVV)G1​=(I,M1​,VVV)
2.1 Scalar prefactor
六个 label permutations 和两个 derivative placements 保留在 D-word sum 中，不再放额外 NVVVN_{VVV}NVVV​。
P1,χ=(−28)⏟source(2gℏ)⏟M1(χi2g256ℏ)⏟VVVχ×[(−ℏ)2(ℏ16)]⏟u,u,ϕϕ~ propagators[(−14)16]⏟chiral Berezin measurei⏟Fourier endpoint×(12! 2)⏟action Wick2⏟DcB1,c↦DB1.\begin{aligned}
\mathcal P_{1,\chi}
={}&
\underbrace{\left(-\frac{\sqrt2}{8}\right)}_{\text{source}}
\underbrace{\left(\frac{\sqrt2g}{\hbar}\right)}_{M_1}
\underbrace{\left(\frac{\chi i\sqrt2g}{256\hbar}\right)}_{VVV_\chi}
\\
&\times
\underbrace{\left[(-\hbar)^2
\left(\frac{\hbar}{16}\right)\right]}_{u,u,\phi\widetilde\phi\ {\rm propagators}}
\underbrace{\left[\left(-\frac14\right)16\right]}_{\text{chiral Berezin measure}}
\underbrace{i}_{\text{Fourier endpoint}}
\\
&\times
\underbrace{\left(\frac1{2!}\,2\right)}_{\text{action Wick}}
\underbrace{\sqrt2}_{D_cB_{1,c}\mapsto DB_1}.
\end{aligned}P1,χ​=​source(−82​​)​​M1​(ℏ2​g​)​​VVVχ​(256ℏχi2​g​)​​×u,u,ϕϕ​ propagators[(−ℏ)2(16ℏ​)]​​chiral Berezin measure[(−41​)16]​​Fourier endpointi​​×action Wick(2!1​2)​​Dc​B1,c​↦DB1​2​​​.​
逐项相乘：
(−28)(2gℏ)(χi2g256ℏ)=−χi2g21024ℏ2,(−ℏ)2ℏ16=ℏ316,(−14)16=−4,(−4)i2=−4i2.\begin{aligned}
\left(-\frac{\sqrt2}{8}\right)
\left(\frac{\sqrt2g}{\hbar}\right)
\left(\frac{\chi i\sqrt2g}{256\hbar}\right)
&=
-\frac{\chi i\sqrt2g^2}{1024\hbar^2},
\\
(-\hbar)^2\frac{\hbar}{16}
&=\frac{\hbar^3}{16},
\\
\left(-\frac14\right)16
&=-4,
\\
(-4)i\sqrt2
&=-4i\sqrt2.
\end{aligned}(−82​​)(ℏ2​g​)(256ℏχi2​g​)(−ℏ)216ℏ​(−41​)16(−4)i2​​=−1024ℏ2χi2​g2​,=16ℏ3​,=−4,=−4i2​.​
故
P1,χ=−χ ℏg22048.\boxed{
\mathcal P_{1,\chi}
=
-\chi\,\frac{\hbar g^2}{2048}.
}P1,χ​=−χ2048ℏg2​.​
这里 canonical external gauge letter 满足
Dc=2D,B1,c=B1,⟨Dc,B1,c⟩=2⟨D,B1⟩.D_c=\sqrt2D,
\qquad
B_{1,c}=B_1,
\qquad
\langle D_c,B_{1,c}\rangle
=
\sqrt2\langle D,B_1\rangle.Dc​=2​D,B1,c​=B1​,⟨Dc​,B1,c​⟩=2​⟨D,B1​⟩.

2.2 Parent replay normalization
χTATBP1,χ+13072−2048−ℏg2/2048−1−30722048+ℏg2/2048\begin{array}{c|cc|c}
\chi&T_A&T_B&\mathcal P_{1,\chi}\\ \hline
+1&3072&-2048&-\hbar g^2/2048\\
-1&-3072&2048&+\hbar g^2/2048
\end{array}χ+1−1​TA​3072−3072​TB​−20482048​P1,χ​−ℏg2/2048+ℏg2/2048​​
由于
ℏg2Iμ2=ℏg232π2=12λ1,\hbar g^2I_{\mu^2}
=
\frac{\hbar g^2}{32\pi^2}
=
\frac12\lambda_1,ℏg2Iμ2​=32π2ℏg2​=21​λ1​,
A-parent 为
Γ1,Aparent=[−30722048−30722048]ℏg2Iμ2=(−3)12λ1=−32λ1⟨DD,B1E⟩.\begin{aligned}
\Gamma_{1,A}^{\rm parent}
&=
\left[
-\frac{3072}{2048}
-\frac{3072}{2048}
\right]
\hbar g^2I_{\mu^2}
\\
&=
(-3)\frac12\lambda_1
\\
&=
\boxed{-\frac32\lambda_1
\langle D^D,B_1^E\rangle}.
\end{aligned}Γ1,Aparent​​=[−20483072​−20483072​]ℏg2Iμ2​=(−3)21​λ1​=−23​λ1​⟨DD,B1E​⟩​.​
B-parent 为
Γ1,Bparent=[20482048+20482048]ℏg2Iμ2=212λ1=+λ1⟨DD,B1E⟩.\begin{aligned}
\Gamma_{1,B}^{\rm parent}
&=
\left[
\frac{2048}{2048}
+\frac{2048}{2048}
\right]
\hbar g^2I_{\mu^2}
\\
&=
2\frac12\lambda_1
\\
&=
\boxed{+\lambda_1
\langle D^D,B_1^E\rangle}.
\end{aligned}Γ1,Bparent​​=[20482048​+20482048​]ℏg2Iμ2​=221​λ1​=+λ1​⟨DD,B1E​⟩​.​

2.3 Twelve occurrence-tagged words
定义
Ω12={123L,123R,132L,132R,213L,213R,231L,231R,312L,312R,321L,321R}.\Omega_{12}
=
\{
123_L,123_R,
132_L,132_R,
213_L,213_R,
231_L,231_R,
312_L,312_R,
321_L,321_R
\}.Ω12​={123L​,123R​,132L​,132R​,213L​,213R​,231L​,231R​,312L​,312R​,321L​,321R​}.
对每个 ω=(π,ρ)∈Ω12\omega=(\pi,\rho)\in\Omega_{12}ω=(π,ρ)∈Ω12​，令


e(ω)e(\omega)e(ω)：原 inverse-kernel occurrence；


n(ω)n(\omega)n(ω)：IBP 后相邻 chiral projector 的 inverse kernel。


每个 word 都有
Lω=−12D+Dˉ2D2∣e(ω) Πn(ω)⟶8rˉn(ω)2Tω.\mathscr L_{\omega}
=
-\frac12
D_+\bar D^2D^2\big|_{e(\omega)}
\,\Pi_{n(\omega)}
\quad\longrightarrow\quad
8\bar r_{n(\omega)}^2\mathscr T_\omega .Lω​=−21​D+​Dˉ2D2​e(ω)​Πn(ω)​⟶8rˉn(ω)2​Tω​.
即每个 occurrence 单独执行
e(ω)⟶n(ω),Tω⟶8Tω.\boxed{
e(\omega)\longrightarrow n(\omega),
\qquad
\mathscr T_\omega\longrightarrow8\mathscr T_\omega .
}e(ω)⟶n(ω),Tω​⟶8Tω​.​
marked branchdiscarded longitudinal wordtransported tagsigned full-ddd cut/contactμℓ2\mu_\ell^2μℓ2​ remainder after the 12-word sumsimplex momentcontact sourceA,+A,+A,+(-\frac12D_+\bar D^2D^2_{e}\Pi_n)e→ne\to ne→n8rn,d2TA,+8r_{n,d}^2\mathscr T_{A,+}8rn,d2​TA,+​, subtracted−4096y μℓ2-4096y\,\mu_\ell^2−4096yμℓ2​13\frac1331​A,−A,-A,−conjugate worde→ne\to ne→n8rn,d2TA,−8r_{n,d}^2\mathscr T_{A,-}8rn,d2​TA,−​, subtracted+4096y μℓ2+4096y\,\mu_\ell^2+4096yμℓ2​13\frac1331​conjugate Euler/current contactB,+B,+B,+transported D−D_-D−​ word through the A-projectore→ne\to ne→n8rn,d2TB,+8r_{n,d}^2\mathscr T_{B,+}8rn,d2​TB,+​, subtracted+4096y μℓ2+4096y\,\mu_\ell^2+4096yμℓ2​13\frac1331​−2AE1~-2A\mathscr E_{\widetilde1}−2AE1​B,−B,-B,−conjugate worde→ne\to ne→n8rn,d2TB,−8r_{n,d}^2\mathscr T_{B,-}8rn,d2​TB,−​, subtracted−4096y μℓ2-4096y\,\mu_\ell^2−4096yμℓ2​13\frac1331​conjugate matter-Euler cut
这里
RA,taggedχ=−512χy,RB,taggedχ=+512χyR_{A,\rm tagged}^{\chi}=-512\chi y,
\qquad
R_{B,\rm tagged}^{\chi}=+512\chi yRA,taggedχ​=−512χy,RB,taggedχ​=+512χy
是 projector saturation 之前的 core。正确 rows 是
RA,fullχ=8RA,taggedχ=−4096χy,\boxed{
R_{A,\rm full}^{\chi}
=
8R_{A,\rm tagged}^{\chi}
=
-4096\chi y,
}RA,fullχ​=8RA,taggedχ​=−4096χy,​
RB,fullχ=8RB,taggedχ=+4096χy.\boxed{
R_{B,\rm full}^{\chi}
=
8R_{B,\rm tagged}^{\chi}
=
+4096\chi y.
}RB,fullχ​=8RB,taggedχ​=+4096χy.​

2.4 Concrete factor-888 normalization row
以 +++-chirality、outer-AAA row 为例。
错误的 tagged-only row：
Γ1,A,+tagged=(−ℏg22048)(−512)(13)(132π2)=ℏg2384π2=124λ1.\begin{aligned}
\Gamma_{1,A,+}^{\rm tagged}
&=
\left(-\frac{\hbar g^2}{2048}\right)
(-512)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
\\
&=
\frac{\hbar g^2}{384\pi^2}
\\
&=
\frac1{24}\lambda_1.
\end{aligned}Γ1,A,+tagged​​=(−2048ℏg2​)(−512)(31​)(32π21​)=384π2ℏg2​=241​λ1​.​
加入
(−12)(−1)(16)=8\left(-\frac12\right)(-1)(16)=8(−21​)(−1)(16)=8
后：
Γ1,A,+full=(−ℏg22048)(−4096)(13)(132π2)=ℏg248π2=13λ1.\begin{aligned}
\Gamma_{1,A,+}^{\rm full}
&=
\left(-\frac{\hbar g^2}{2048}\right)
(-4096)
\left(\frac13\right)
\left(\frac1{32\pi^2}\right)
\\
&=
\frac{\hbar g^2}{48\pi^2}
\\
&=
\frac13\lambda_1.
\end{aligned}Γ1,A,+full​​=(−2048ℏg2​)(−4096)(31​)(32π21​)=48π2ℏg2​=31​λ1​.​
两种 chirality 给出
ΓG1,Aselected=+23λ1⟨DD,B1E⟩.\boxed{
\Gamma_{G_1,A}^{\rm selected}
=
+\frac23\lambda_1
\langle D^D,B_1^E\rangle.
}ΓG1​,Aselected​=+32​λ1​⟨DD,B1E​⟩.​
B-mark 同理：
ΓG1,Bselected=−23λ1⟨DD,B1E⟩.\boxed{
\Gamma_{G_1,B}^{\rm selected}
=
-\frac23\lambda_1
\langle D^D,B_1^E\rangle.
}ΓG1​,Bselected​=−32​λ1​⟨DD,B1E​⟩.​
因此
ΓG1selected=0,\boxed{
\Gamma_{G_1}^{\rm selected}=0,
}ΓG1​selected​=0,​
但这是两个非零 occurrence-tagged amplitudes 的和：
+23λ1−23λ1=0.+\frac23\lambda_1-\frac23\lambda_1=0.+32​λ1​−32​λ1​=0.
没有额外 G1G_1G1​ occurrence survives。理由是：
8rˉe2D+−8re,d2D+8\bar r_e^2D_+
-
8r_{e,d}^2D_+8rˉe2​D+​−8re,d2​D+​
属于原 edge Euler cut；transported longitudinal sector 只产生上述 neighboring tags。没有 occurrence tag 的 algebraic determinant 不进入 cut ledger。

3. Ordered-AAAAAA diagnostic
该 row 只验证 transport rule，不进入 AB1AB_1AB1​ coefficient。
S2=W01(a2+b1−−a1−b2+).\mathcal S_2
=
W_{01}(a_{2+}b_{1-}-a_{1-}b_{2+}).S2​=W01​(a2+​b1−​−a1−​b2+​).
原 tagged-only result：
R2,tagged=(y−z)μℓ2Ppq.\mathcal R_{2,\rm tagged}
=
(y-z)\mu_\ell^2P_{pq}.R2,tagged​=(y−z)μℓ2​Ppq​.
Transported longitudinal correction 是
R2,L=(2z−y−12)μℓ2Ppq.\mathcal R_{2,L}
=
\left(2z-y-\frac12\right)\mu_\ell^2P_{pq}.R2,L​=(2z−y−21​)μℓ2​Ppq​.
其中：


2z−y2z-y2z−y：neighboring inverse-kernel tag；


−12-\frac12−21​：由原 −12D+Dˉ2D2-\frac12D_+\bar D^2D^2−21​D+​Dˉ2D2 endpoint 保留下来的 boundary normalization。


故
R2,full=R2,tagged+R2,L=[(y−z)+(2z−y−12)]μℓ2Ppq=(z−12)μℓ2Ppq.\begin{aligned}
\mathcal R_{2,\rm full}
&=
\mathcal R_{2,\rm tagged}
+
\mathcal R_{2,L}
\\
&=
\left[
(y-z)+(2z-y-\frac12)
\right]\mu_\ell^2P_{pq}
\\
&=
\boxed{
\left(z-\frac12\right)\mu_\ell^2P_{pq}.
}
\end{aligned}R2,full​​=R2,tagged​+R2,L​=[(y−z)+(2z−y−21​)]μℓ2​Ppq​=(z−21​)μℓ2​Ppq​.​​
积分：
∫Σ2z=16,∫Σ21=12.\int_{\Sigma_2}z=\frac16,
\qquad
\int_{\Sigma_2}1=\frac12.∫Σ2​​z=61​,∫Σ2​​1=21​.
2∫Σ2(z−12)=2[16−1212]=2[16−14]=−16.\begin{aligned}
2\int_{\Sigma_2}\left(z-\frac12\right)
&=
2\left[
\frac16-\frac12\frac12
\right]
\\
&=
2\left[
\frac16-\frac14
\right]
\\
&=
-\frac16.
\end{aligned}2∫Σ2​​(z−21​)​=2[61​−21​21​]=2[61​−41​]=−61​.​
4ℏg2(−16)Iμ2=4ℏg2(−16)132π2=−ℏg248π2=−13λ1.\begin{aligned}
4\hbar g^2
\left(-\frac16\right)
I_{\mu^2}
&=
4\hbar g^2
\left(-\frac16\right)
\frac1{32\pi^2}
\\
&=
-\frac{\hbar g^2}{48\pi^2}
\\
&=
\boxed{-\frac13\lambda_1}.
\end{aligned}4ℏg2(−61​)Iμ2​​=4ℏg2(−61​)32π21​=−48π2ℏg2​=−31​λ1​​.​
该 −λ1/3-\lambda_1/3−λ1​/3 不添加到下文 AB1AB_1AB1​ rows。

4. G2=(I,M1,M1)G_2=(I,M_1,M_1)G2​=(I,M1​,M1​)
4.1 Scalar prefactor
P2=(−28)⏟source(2gℏ)2⏟M1M1[(−ℏ)(ℏ16)2]⏟u,ϕϕ~,ϕϕ~×(12! 2)⏟vertex ordering2⏟DcB1,c↦DB1.\begin{aligned}
\mathcal P_2
={}&
\underbrace{\left(-\frac{\sqrt2}{8}\right)}_{\text{source}}
\underbrace{\left(\frac{\sqrt2g}{\hbar}\right)^2}_{M_1M_1}
\underbrace{\left[
(-\hbar)
\left(\frac{\hbar}{16}\right)^2
\right]}_{u,\phi\widetilde\phi,\phi\widetilde\phi}
\\
&\times
\underbrace{\left(\frac1{2!}\,2\right)}_{\text{vertex ordering}}
\underbrace{\sqrt2}_{D_cB_{1,c}\mapsto DB_1}.
\end{aligned}P2​=​source(−82​​)​​M1​M1​(ℏ2​g​)2​​u,ϕϕ​,ϕϕ​[(−ℏ)(16ℏ​)2]​​×vertex ordering(2!1​2)​​Dc​B1,c​↦DB1​2​​​.​
(−28)(2gℏ)2=−2g24ℏ2,(−ℏ)(ℏ16)2=−ℏ3256.\begin{aligned}
\left(-\frac{\sqrt2}{8}\right)
\left(\frac{\sqrt2g}{\hbar}\right)^2
&=
-\frac{\sqrt2g^2}{4\hbar^2},
\\
(-\hbar)
\left(\frac{\hbar}{16}\right)^2
&=
-\frac{\hbar^3}{256}.
\end{aligned}(−82​​)(ℏ2​g​)2(−ℏ)(16ℏ​)2​=−4ℏ22​g2​,=−256ℏ3​.​
所以
P2=+ℏg2512.\boxed{
\mathcal P_2
=
+\frac{\hbar g^2}{512}.
}P2​=+512ℏg2​.​
Color route：
− (TU)CD(TV)C′EκCC′⟶FABDE.-\,
(T_U)^C{}_D
(T_V)^{C'}{}_E
\kappa_{CC'}
\quad\longrightarrow\quad
\mathbb F^{AB}{}_{DE}.−(TU​)CD​(TV​)C′E​κCC′​⟶FABDE​.
前面的 minus 是 reversed matter-arrow/Koszul sign；它与
TUTV=i2cc=−ccT_U T_V=i^2cc=-ccTU​TV​=i2cc=−cc 合并为 +F+\mathbb F+F。

4.2 Transported D-words
局部 endpoint trace 为
T2=128 (r1−r0)+∧(r2−r1)+.\mathscr T_{2}
=
128\,
(r_1-r_0)_+\wedge(r_2-r_1)_+.T2​=128(r1​−r0​)+​∧(r2​−r1​)+​.
采用
r1−r0=q,r2−r1=p,r_1-r_0=q,
\qquad
r_2-r_1=p,r1​−r0​=q,r2​−r1​=p,
得到
T2=128(q+∧p+)=−128Ppq.\mathscr T_2
=
128(q_+\wedge p_+)
=
-128P_{pq}.T2​=128(q+​∧p+​)=−128Ppq​.
Longitudinal transport：
8rˉn2T2=1024rˉn2(q+∧p+)=−1024rˉn2Ppq.8\bar r_n^2\mathscr T_2
=
1024\bar r_n^2(q_+\wedge p_+)
=
-1024\bar r_n^2P_{pq}.8rˉn2​T2​=1024rˉn2​(q+​∧p+​)=−1024rˉn2​Ppq​.
mark / outputdiscarded wordIBP transportnew tagfull-ddd cut/contact, subtractedμℓ2\mu_\ell^2μℓ2​ remaindermomentouter AAA, ⟨DD,B1E⟩\langle D^D,B_1^E\rangle⟨DD,B1E​⟩(-\frac12D_+\bar D^2D^2{r_0}\Pi{r_1}\Pi_{r_2})(−1/2)(−1)(16)=8(-1/2)(-1)(16)=8(−1/2)(−1)(16)=8r0→r1r_0\to r_1r0​→r1​+1024r1,d2(q+∧p+)+1024r_{1,d}^2(q_+\wedge p_+)+1024r1,d2​(q+​∧p+​); gauge-Euler cut plus s=1s=1s=1 nonlinear current contact+1024μℓ2(q+∧p+)=−1024μℓ2Ppq+1024\mu_\ell^2(q_+\wedge p_+)=-1024\mu_\ell^2P_{pq}+1024μℓ2​(q+​∧p+​)=−1024μℓ2​Ppq​outer B1B_1B1​, ⟨B1D,DE⟩\langle B_1^D,D^E\rangle⟨B1D​,DE⟩reflected longitudinal wordsame factor 888reflected edge →r1\to r_1→r1​+1024r1,d2(q+∧p+)+1024r_{1,d}^2(q_+\wedge p_+)+1024r1,d2​(q+​∧p+​); −2AE1~-2A\mathscr E_{\widetilde1}−2AE1​ Euler cut+1024μℓ2(q+∧p+)=−1024μℓ2Ppq+1024\mu_\ell^2(q_+\wedge p_+)=-1024\mu_\ell^2P_{pq}+1024μℓ2​(q+​∧p+​)=−1024μℓ2​Ppq​111
The A(C2×C3)A(C_2\times C_3)A(C2​×C3​) contact is flavor-orthogonal to the G2G_2G2​ ordered DB1DB_1DB1​ route and contributes in G3G_3G3​, not here.
每个 ordered route：
ΓG2,route=(ℏg2512)(−1024)(1)(132π2)=−ℏg216π2=−λ1.\begin{aligned}
\Gamma_{G_2,\rm route}
&=
\left(\frac{\hbar g^2}{512}\right)
(-1024)
(1)
\left(\frac1{32\pi^2}\right)
\\
&=
-\frac{\hbar g^2}{16\pi^2}
\\
&=
-\lambda_1.
\end{aligned}ΓG2​,route​​=(512ℏg2​)(−1024)(1)(32π21​)=−16π2ℏg2​=−λ1​.​
因此
ΓG2=−λ1⟨B1D,DE⟩−λ1⟨DD,B1E⟩.\boxed{
\Gamma_{G_2}
=
-\lambda_1\langle B_1^D,D^E\rangle
-\lambda_1\langle D^D,B_1^E\rangle.
}ΓG2​​=−λ1​⟨B1D​,DE⟩−λ1​⟨DD,B1E​⟩.​

5. G3,2G_{3,2}G3,2​ and G3,3G_{3,3}G3,3​
5.1 Scalar prefactors
Antichiral Berezin measure 给出
(−14D2)(D2θ2=−4)=1.\left(-\frac14D^2\right)
\left(D^2\theta^2=-4\right)=1.(−41​D2)(D2θ2=−4)=1.
最终 spacetime endpoint 的 phase 由
−D+Dˉα˙=+Dˉα˙D++2∂+α˙,∂+α˙↦ip+α˙-D_+\bar D_{\dot\alpha}
=
+\bar D_{\dot\alpha}D_+
+2\partial_{+\dot\alpha},
\qquad
\partial_{+\dot\alpha}\mapsto
ip_{+\dot\alpha}−D+​Dˉα˙​=+Dˉα˙​D+​+2∂+α˙​,∂+α˙​↦ip+α˙​
给出 +i+i+i。数值 222 已包含在 integer D-word 102410241024 中。
G3,2G_{3,2}G3,2​
ε123=+1.\varepsilon_{123}=+1.ε123​=+1.
P3,2=(−28)(2gℏ)(−2gℏ)[(−ℏ)(ℏ16)2]×2⏟two orderedH− flavor slotsi⏟endpoint1⏟C2C3 field map.\begin{aligned}
\mathcal P_{3,2}
={}&
\left(-\frac{\sqrt2}{8}\right)
\left(\frac{\sqrt2g}{\hbar}\right)
\left(-\frac{\sqrt2g}{\hbar}\right)
\left[
(-\hbar)
\left(\frac{\hbar}{16}\right)^2
\right]
\\
&\times
\underbrace{2}_{\substack{\text{two ordered}\\H_-\text{ flavor slots}}}
\underbrace{i}_{\text{endpoint}}
\underbrace{1}_{C_2C_3\text{ field map}}.
\end{aligned}P3,2​=​(−82​​)(ℏ2​g​)(−ℏ2​g​)[(−ℏ)(16ℏ​)2]×two orderedH−​ flavor slots​2​​endpointi​​C2​C3​ field map1​​.​
P3,2=−i2 ℏg2512.\boxed{
\mathcal P_{3,2}
=
-\frac{i\sqrt2\,\hbar g^2}{512}.
}P3,2​=−512i2​ℏg2​.​
Output route：
G3,2:⟨C2D,C3E⟩.\boxed{
G_{3,2}:\quad
\langle C_2^D,C_3^E\rangle.
}G3,2​:⟨C2D​,C3E​⟩.​
G3,3G_{3,3}G3,3​
ε132=−1.\varepsilon_{132}=-1.ε132​=−1.
故
P3,3=+i2 ℏg2512.\boxed{
\mathcal P_{3,3}
=
+\frac{i\sqrt2\,\hbar g^2}{512}.
}P3,3​=+512i2​ℏg2​.​
Output route：
G3,3:⟨C3D,C2E⟩.\boxed{
G_{3,3}:\quad
\langle C_3^D,C_2^E\rangle.
}G3,3​:⟨C3D​,C2E​⟩.​
Color routes：
−i(TU)CD cVC′EκCC′⟶FABDE.-i(T_U)^C{}_D\,c_{VC'E}\kappa_{CC'}
\longrightarrow
\mathbb F^{AB}{}_{DE}.−i(TU​)CD​cVC′E​κCC′​⟶FABDE​.
s=3s=3s=3 route 的唯一额外 sign 是
ε132=−ε123\varepsilon_{132}=-\varepsilon_{123}ε132​=−ε123​。

5.2 Outer-AAA: original edge and transported neighbor
采用 routing
r0=ℓ,r1=ℓ+q,r2=ℓ+p+q.r_0=\ell,
\qquad
r_1=\ell+q,
\qquad
r_2=\ell+p+q.r0​=ℓ,r1​=ℓ+q,r2​=ℓ+p+q.
Exact replay：
RA=−128W12.R_A=-128W_{12}.RA​=−128W12​.
因此原 edge piece 是
8rˉ02RA=−1024rˉ02W12.8\bar r_0^2R_A
=
-1024\bar r_0^2W_{12}.8rˉ02​RA​=−1024rˉ02​W12​.
完整 numerator 为
Nfull=−1024rˉ02W12+1024rˉ12((p+q)+∧r0,+).\boxed{
N_{\rm full}
=
-1024\bar r_0^2W_{12}
+
1024\bar r_1^2
\bigl((p+q)_+\wedge r_{0,+}\bigr).
}Nfull​=−1024rˉ02​W12​+1024rˉ12​((p+q)+​∧r0,+​).​
Ward combination 写为
Nfull−C0,A(d)−C1,A(d).N_{\rm full}
-C_{0,A}^{(d)}
-C_{1,A}^{(d)}.Nfull​−C0,A(d)​−C1,A(d)​.
Pointwise ddd-dimensional contacts 必须是
C0,A(d)=−1024r0,d2W12,\boxed{
C_{0,A}^{(d)}
=
-1024r_{0,d}^2W_{12},
}C0,A(d)​=−1024r0,d2​W12​,​
C1,A(d)=+1024r1,d2((p+q)+∧r0,+).\boxed{
C_{1,A}^{(d)}
=
+1024r_{1,d}^2
\bigl((p+q)_+\wedge r_{0,+}\bigr).
}C1,A(d)​=+1024r1,d2​((p+q)+​∧r0,+​).​
因此：


C0,A(d)C_{0,A}^{(d)}C0,A(d)​：−∇+EV-\nabla_+\mathscr E_V−∇+​EV​ Euler cut；


C1,A(d)C_{1,A}^{(d)}C1,A(d)​：−2i(Bs×Cs)-2i(B_s\times C_s)−2i(Bs​×Cs​) nonlinear contact；


neighboring-contact numerator 的 sign 是 plus，但整个 contact 在 Ward combination 中被 subtract。


剩余：
R3,A=−1024μℓ2W12+1024μℓ2((p+q)+∧r0,+).\boxed{
\mathcal R_{3,A}
=
-1024\mu_\ell^2W_{12}
+
1024\mu_\ell^2
\bigl((p+q)_+\wedge r_{0,+}\bigr).
}R3,A​=−1024μℓ2​W12​+1024μℓ2​((p+q)+​∧r0,+​).​
若 rˉi2=ri,d2\bar r_i^2=r_{i,d}^2rˉi2​=ri,d2​，该式 pointwise 等于零。

5.3 Simplex evaluation of outer-AAA
Feynman shift：
ℓ=k−zp−(y+z)q.\ell
=
k-zp-(y+z)q.ℓ=k−zp−(y+z)q.
因此
r0,+=−zp+−(y+z)q+,r1,+=−zp++xq+,r2,+=(1−z)p++xq+.\begin{aligned}
r_{0,+}
&=
-zp_+-(y+z)q_+,
\\
r_{1,+}
&=
-zp_++xq_+,
\\
r_{2,+}
&=
(1-z)p_++xq_+.
\end{aligned}r0,+​r1,+​r2,+​​=−zp+​−(y+z)q+​,=−zp+​+xq+​,=(1−z)p+​+xq+​.​
第一项：
W12=r1,+∧r2,+=(−zp++xq+)∧((1−z)p++xq+)=−zxPpq−x(1−z)Ppq=−xPpq.\begin{aligned}
W_{12}
&=
r_{1,+}\wedge r_{2,+}
\\
&=
(-zp_++xq_+)
\wedge
((1-z)p_++xq_+)
\\
&=
-zxP_{pq}
-x(1-z)P_{pq}
\\
&=
-xP_{pq}.
\end{aligned}W12​​=r1,+​∧r2,+​=(−zp+​+xq+​)∧((1−z)p+​+xq+​)=−zxPpq​−x(1−z)Ppq​=−xPpq​.​
第二项：
(p+q)+∧r0,+=(p+q)+∧[−zp+−(y+z)q+]=zPpq−(y+z)Ppq=−yPpq.\begin{aligned}
(p+q)_+\wedge r_{0,+}
&=
(p+q)_+
\wedge
[-zp_+-(y+z)q_+]
\\
&=
zP_{pq}-(y+z)P_{pq}
\\
&=
-yP_{pq}.
\end{aligned}(p+q)+​∧r0,+​​=(p+q)+​∧[−zp+​−(y+z)q+​]=zPpq​−(y+z)Ppq​=−yPpq​.​
由于
2∫Σ2x=13,2∫Σ2y=13,2\int_{\Sigma_2}x=\frac13,
\qquad
2\int_{\Sigma_2}y=\frac13,2∫Σ2​​x=31​,2∫Σ2​​y=31​,
有
2∫Σ2W12=−13Ppq,2\int_{\Sigma_2}W_{12}
=
-\frac13P_{pq},2∫Σ2​​W12​=−31​Ppq​,
2∫Σ2(p+q)+∧r0,+=−13Ppq.2\int_{\Sigma_2}(p+q)_+\wedge r_{0,+}
=
-\frac13P_{pq}.2∫Σ2​​(p+q)+​∧r0,+​=−31​Ppq​.
所以 outer-AAA remainder：
2∫Σ2R3,A=−1024μℓ2(−13Ppq)+1024μℓ2(−13Ppq)=0.\begin{aligned}
2\int_{\Sigma_2}\mathcal R_{3,A}
&=
-1024\mu_\ell^2
\left(-\frac13P_{pq}\right)
+
1024\mu_\ell^2
\left(-\frac13P_{pq}\right)
\\
&=
0.
\end{aligned}2∫Σ2​​R3,A​​=−1024μℓ2​(−31​Ppq​)+1024μℓ2​(−31​Ppq​)=0.​
即
ΓG3,2,A=0,ΓG3,3,A=0.\boxed{
\Gamma_{G_{3,2},A}=0,
\qquad
\Gamma_{G_{3,3},A}=0.
}ΓG3,2​,A​=0,ΓG3,3​,A​=0.​
更细分地，
G3,2:−i23λ1+i23λ1=0,G_{3,2}:
\qquad
-\frac{i\sqrt2}{3}\lambda_1
+
\frac{i\sqrt2}{3}\lambda_1
=0,G3,2​:−3i2​​λ1​+3i2​​λ1​=0,
G3,3:+i23λ1−i23λ1=0.G_{3,3}:
\qquad
+\frac{i\sqrt2}{3}\lambda_1
-
\frac{i\sqrt2}{3}\lambda_1
=0.G3,3​:+3i2​​λ1​−3i2​​λ1​=0.

5.4 Outer-B1B_1B1​: Euler plus superpotential contact
这一 branch 没有被遗漏的 D−D+Dˉ2D+D_-D_+\bar D^2D_+D−​D+​Dˉ2D+​ longitudinal occurrence；其 original tag 保留。
完整 local D-word saturation 为
12⋅16⋅16⋅8=1024.\frac12\cdot16\cdot16\cdot8
=
1024.21​⋅16⋅16⋅8=1024.
其中：


1/21/21/2：D−D+=12D2D_-D_+=\frac12D^2D−​D+​=21​D2；


两个 161616：两个 chiral projectors；


888：ordered endpoint trace。


于是
N3,B=1024rˉe2(q+∧p+).N_{3,B}
=
1024\bar r_e^2
(q_+\wedge p_+).N3,B​=1024rˉe2​(q+​∧p+​).
Matching full-ddd Euler/superpotential contact：
C3,B(d)=1024re,d2(q+∧p+).C_{3,B}^{(d)}
=
1024r_{e,d}^2
(q_+\wedge p_+).C3,B(d)​=1024re,d2​(q+​∧p+​).
这里 C3,B(d)C_{3,B}^{(d)}C3,B(d)​ 是
−2AE1~-2A\mathscr E_{\widetilde1}−2AE1​
的 matter-Euler cut 与
−2Aε1st(Cs×Ct)-\sqrt2A\varepsilon_{1st}(C_s\times C_t)−2​Aε1st​(Cs​×Ct​)
的 ordered superpotential contact 之和。两个 ordered H−H_-H−​ slots 正是 scalar prefactor 中的 Wick factor 222。
剩余：
R3,B=1024μℓ2(q+∧p+)=−1024μℓ2Ppq.\begin{aligned}
\mathcal R_{3,B}
&=
1024\mu_\ell^2
(q_+\wedge p_+)
\\
&=
-1024\mu_\ell^2P_{pq}.
\end{aligned}R3,B​​=1024μℓ2​(q+​∧p+​)=−1024μℓ2​Ppq​.​
其 simplex weight 是常数：
2∫Σ21=1.2\int_{\Sigma_2}1=1.2∫Σ2​​1=1.
G3,2G_{3,2}G3,2​
ΓG3,2,B=(−i2ℏg2512)(−1024)(132π2)=+i2ℏg216π2=+i2λ1⟨C2D,C3E⟩.\begin{aligned}
\Gamma_{G_{3,2},B}
&=
\left(
-\frac{i\sqrt2\hbar g^2}{512}
\right)
(-1024)
\left(\frac1{32\pi^2}\right)
\\
&=
+\frac{i\sqrt2\hbar g^2}{16\pi^2}
\\
&=
\boxed{
+i\sqrt2\lambda_1
\langle C_2^D,C_3^E\rangle.
}
\end{aligned}ΓG3,2​,B​​=(−512i2​ℏg2​)(−1024)(32π21​)=+16π2i2​ℏg2​=+i2​λ1​⟨C2D​,C3E​⟩.​​
G3,3G_{3,3}G3,3​
ΓG3,3,B=(+i2ℏg2512)(−1024)(132π2)=−i2ℏg216π2=−i2λ1⟨C3D,C2E⟩.\begin{aligned}
\Gamma_{G_{3,3},B}
&=
\left(
+\frac{i\sqrt2\hbar g^2}{512}
\right)
(-1024)
\left(\frac1{32\pi^2}\right)
\\
&=
-\frac{i\sqrt2\hbar g^2}{16\pi^2}
\\
&=
\boxed{
-i\sqrt2\lambda_1
\langle C_3^D,C_2^E\rangle.
}
\end{aligned}ΓG3,3​,B​​=(+512i2​ℏg2​)(−1024)(32π21​)=−16π2i2​ℏg2​=−i2​λ1​⟨C3D​,C2E​⟩.​​

6. Graph-by-graph result
ΓG1=(23−23)λ1⟨DD,B1E⟩=0.\boxed{
\Gamma_{G_1}
=
\left(
\frac23-\frac23
\right)
\lambda_1
\langle D^D,B_1^E\rangle
=0.
}ΓG1​​=(32​−32​)λ1​⟨DD,B1E​⟩=0.​
ΓG2=−λ1⟨B1D,DE⟩−λ1⟨DD,B1E⟩.\boxed{
\Gamma_{G_2}
=
-\lambda_1\langle B_1^D,D^E\rangle
-\lambda_1\langle D^D,B_1^E\rangle.
}ΓG2​​=−λ1​⟨B1D​,DE⟩−λ1​⟨DD,B1E​⟩.​
ΓG3,2=+i2λ1⟨C2D,C3E⟩.\boxed{
\Gamma_{G_{3,2}}
=
+i\sqrt2\lambda_1
\langle C_2^D,C_3^E\rangle.
}ΓG3,2​​=+i2​λ1​⟨C2D​,C3E​⟩.​
ΓG3,3=−i2λ1⟨C3D,C2E⟩.\boxed{
\Gamma_{G_{3,3}}
=
-i\sqrt2\lambda_1
\langle C_3^D,C_2^E\rangle.
}ΓG3,3​​=−i2​λ1​⟨C3D​,C2E​⟩.​
因此 ordered basis
(⟨B1D,DE⟩,⟨DD,B1E⟩,⟨C3D,C2E⟩,⟨C2D,C3E⟩)\left(
\langle B_1^D,D^E\rangle,
\langle D^D,B_1^E\rangle,
\langle C_3^D,C_2^E\rangle,
\langle C_2^D,C_3^E\rangle
\right)(⟨B1D​,DE⟩,⟨DD,B1E​⟩,⟨C3D​,C2E​⟩,⟨C2D​,C3E​⟩)
中的 coefficient vector 是
(−λ1, −λ1, −i2λ1, +i2λ1).\boxed{
\left(
-\lambda_1,\,
-\lambda_1,\,
-i\sqrt2\lambda_1,\,
+i\sqrt2\lambda_1
\right).
}(−λ1​,−λ1​,−i2​λ1​,+i2​λ1​).​
即完整 Feynman-row sum：
Γ∇−(AB1)(1)=−λ1⟨B1D,DE⟩−λ1⟨DD,B1E⟩−i2λ1⟨C3D,C2E⟩+i2λ1⟨C2D,C3E⟩.\boxed{
\Gamma_{\nabla_-(AB_1)}^{(1)}
=
-\lambda_1\langle B_1^D,D^E\rangle
-\lambda_1\langle D^D,B_1^E\rangle
-i\sqrt2\lambda_1\langle C_3^D,C_2^E\rangle
+i\sqrt2\lambda_1\langle C_2^D,C_3^E\rangle.
}Γ∇−​(AB1​)(1)​=−λ1​⟨B1D​,DE⟩−λ1​⟨DD,B1E​⟩−i2​λ1​⟨C3D​,C2E​⟩+i2​λ1​⟨C2D​,C3E​⟩.​

7. Gate-2R failure ledger
下列 Gate-2R lines 失效：


RA+RB=0⇒μℓ2=0R_A+R_B=0\quad\Rightarrow\quad\mu_\ell^2=0RA​+RB​=0⇒μℓ2​=0
不成立。AAA-mark 与 BBB-mark 是不同 inverse-kernel occurrences，必须分别 transport、cut、形成 μℓ2\mu_\ell^2μℓ2​ remainder 后才能相加。


“G1G_1G1​ 无 surviving occurrence-tagged cut/contact”不成立。实际有
+23λ1,−23λ1+\frac23\lambda_1,
\qquad
-\frac23\lambda_1+32​λ1​,−32​λ1​
两个非零 marked amplitudes；只有它们的最终和为零。


把
−12D+Dˉ2D2-\frac12D_+\bar D^2D^2−21​D+​Dˉ2D2
判为零或直接 IBP 丢弃不成立。正确 transport 给出
(−12)(−1)(16)=8\left(-\frac12\right)(-1)(16)=8(−21​)(−1)(16)=8
并产生 neighboring inverse-kernel tag。


G2G_2G2​ 的
323π2\frac{32}{3\pi^2}3π232​
coefficient 不成立。正确 scalar、D-word、simplex 和 Iμ2I_{\mu^2}Iμ2​ 给出两个独立的 −λ1-\lambda_1−λ1​ ordered rows。


G3,2,G3,3G_{3,2},G_{3,3}G3,2​,G3,3​ 被投影到
⟨D,B1⟩\langle D,B_1\rangle⟨D,B1​⟩ 不成立。正确 outputs 是
G3,2:⟨C2D,C3E⟩,G3,3:⟨C3D,C2E⟩.G_{3,2}:\langle C_2^D,C_3^E\rangle,
\qquad
G_{3,3}:\langle C_3^D,C_2^E\rangle.G3,2​:⟨C2D​,C3E​⟩,G3,3​:⟨C3D​,C2E​⟩.


G3G_3G3​ outer-AAA 只保留 RA=−128W12R_A=-128W_{12}RA​=−128W12​ 不成立。neighboring r1r_1r1​ term
+1024rˉ12((p+q)+∧r0,+)+1024\bar r_1^2((p+q)_+\wedge r_{0,+})+1024rˉ12​((p+q)+​∧r0,+​)
必须同时保留；两项 simplex moments 严格抵消。


Gate-2R 的 standalone “Euler/contact =+512=+512=+512”没有 occurrence tag、没有 matching re,d2r_{e,d}^2re,d2​ square，也没有 pointwise full-ddd check，因而不是 admissible cut/contact row。


最终
803π2\frac{80}{3\pi^2}3π280​
既没有 λ1\lambda_1λ1​ normalization，也混合了四种 ordered output types，故整行失效。
