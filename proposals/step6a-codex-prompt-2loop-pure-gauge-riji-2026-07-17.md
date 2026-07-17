# Step-6A — codex 提示词:纯规范扇区 $\nabla_-(\nabla_+\mathcal W_+^A\nabla_+\mathcal W_+^B\nabla_+\mathcal W_+^C)$ 的两圈"日字图"反常

Status: `NON_AUTHORITY_PROPOSAL` — 这是一份**交给 codex 执行**的提示词/handoff(非备忘录、非授权结果)。
它把一个界限清晰、check point 明确的两圈超图计算完整地交待清楚。下面 `>` 引用块内即
为可直接投喂 codex 的提示词本体;引用块外是给人看的定位说明。

---

## 给人看的定位(不投喂)

- 当前前沿:单圈 component 路线已跑通一次((𝔟,𝔠) 通道,`step5l`,$c_3=-\sqrt2\cdot\hbar g^2/32\pi^2$,机器证书 `scripts/check_step5l_bc_anomaly_assembly.py`)。
- 本任务是**超空间路线的两圈入口**,独立于 component 路线,是复现 HT 两圈结果的第一块砖。
- 关键事实(已从 vendored 源码核实):**HT 是一篇单圈论文**。它从不直接算两圈数,而是用
  Wess–Zumino 相容性 $Q_1^2+\{Q_0,Q_2\}=0$(`main.tex` line 398)**自举**出 $Q_2$;
  两圈拓扑在 Fig. 1 中叫 "two-loop Laman graph"(两三角共边 = 日字图,line 539–561,caption 648)。
  因此"复现 HT 两圈"= 复现相容性所锁定的 $Q_2$,而**直接的日字图费曼计算是 HT 从未做过的独立验证**——这正是创新点。
- 计数逻辑:HT 的 $Q_n$ 作用在 $n+1$ 个 letter 上(line 176–178)。三个 letter $\Rightarrow n=2\Rightarrow$ 两圈。
  所以三个场强 $(\nabla_+\mathcal W_+)^3$ 通道的**首个不可约量子修正就是两圈** $Q_2$。

---

> # 任务:计算纯规范扇区 $Q_-(\nabla_+\mathcal W_+^A\,\nabla_+\mathcal W_+^B\,\nabla_+\mathcal W_+^C)$ 的两圈日字图反常
>
> ## 0. 你是谁、读什么、遵守什么
>
> 你在仓库 `lbotao399-stack/anomaly-ward-identity-in-susy-theories`,分支
> `claude/n4-sym-brst-bv-quantization-tpfek5`。先读:
> - `AUTHORITY.md` / `AGENTS.md`(仓库法:只有 origin/main + 绿色 verify 才是 authority;
>   `proposals/` 一律 `NON_AUTHORITY_PROPOSAL`;derivation-first,禁止不加推导地引用系数)。
> - 记号锁:$\epsilon^{12}=\epsilon^{\dot1\dot2}=+1,\ \epsilon_{12}=-1$(1.3–1.5);
>   $\sigma_E^m=(-i\sigma^i,\mathbf1),\ \bar\sigma_E^m=(+i\sigma^i,\mathbf1)$(1.51–52);
>   frame $+:=1,\ -:=2$((5D.D4));$\vartheta^2=-2\vartheta^1\vartheta^2$,$D^2\vartheta^2=-4$。
> - 超空间费曼规则:`proposals/step5b-euclidean-feynman-rules-memo-2026-07-16.md`
>   与 `contracts/foundations/step-05a-*.md` 的 (5A.49)–(5A.74)。
> - Letter 与插入:`step5d`(5D.1)(5D.2)(5D.4);Noether 散度 `step5c`(5C.16)。
> - 单圈机器(你要类比推广的模板):`step5g`(5G.5)(5G.6)(5G.8)、`step5k`(5K.P)、
>   `step5l`(5L.1)(5L.2) 及其脚本;独立复核 `step5-independent-physics-review`(R.1)(R.2)(R.3)。
> - 外部对照靶:`references/vendor/arxiv/2512.07771v2/source/main.tex`(仅作**比较对象**,
>   非 authority)。关键行:$Q=\sum_n\hbar^nQ_n$(line 150);$Q_n$ 作用在 $n+1$ letter(line 176–178);
>   $Q_1^2+\{Q_0,Q_2\}=0$(line 398);两圈 Laman 图 Fig. 1(line 539–561);
>   单圈纯规范靶 $Q_1(b^Ab^B)=\kappa^2 f_{ACD}f_{BCE}[\partial_{\dot\alpha}c^D\partial^{\dot\alpha}b^E-\partial_{\dot\alpha}b^D\partial^{\dot\alpha}c^E]$(line 1099–1100);
>   字典 $b\sim F_{++},\ \partial_{\dot\alpha}c\sim\bar\lambda_{\dot\alpha}$(line 704);
>   三角核 $\mathcal D^\triangle$(line 722)。**注意:HT 未显式给出任何两圈数,line 671 明说两圈由相容性自举。**
>
> Euclidean N=4 SYM,权重 $e^{-S_E/\hbar}$,离屏作用量 (4C.42a),全量 incoming 动量,DRED 正规化。
> 只算 Euclidean;Lorentzian 镜像用 (5B.9) workhorse 恒等式,后续机械化,不在本任务内。
>
> ## 1. 我们研究什么,只 focus 什么
>
> 我们研究纯 gauge sector 的
> $$\mathcal O_{ABC}\;=\;\nabla_-\big(\nabla_+\mathcal W_+^A\;\nabla_+\mathcal W_+^B\;\nabla_+\mathcal W_+^C\big),$$
> 即扭转超荷 $Q_-=\nabla_-$ 作用在三个反手征场强 letter $\mathfrak f^X=\nabla_+\mathcal W_+^X|=f_{++}^X$(5D.1)
> $(\nabla_a\mathcal W_b|=-\epsilon_{ab}\mathscr D+\tau(\sigma^{MN})_{ab}F_{MN})$ 之积上。
> 展开为 $Q_-\mathcal O=\underbrace{Q_0(\mathfrak f\mathfrak f\mathfrak f)}_{\text{tree}}
> +\hbar\,Q_1(\ldots)+\hbar^2\,Q_2(\mathfrak f^A\mathfrak f^B\mathfrak f^C)+\dots$。
> **我只要你算 $Q_2$ 的 anomaly sector,而且只 focus 在唯一不可约的两圈日字图这一张图上。**
> (可约部分 = 单圈三角 × tree,属于 $Q_1$/Q_0Q_1,它们是**检验**而非目标,见 §6。)
> 这需要很仔细:分子很复杂,D algebra 很长。分步积分的中间过程可以省略,但每个 check point
> 的化简后结果都要显式写给我看。
>
> ## 2. 交付物(严格按此顺序,逐条给我看)
>
> **CP1 — 画图。** 把你研究的日字图画出来(ASCII 或 tikz 皆可)。它是 HT Fig. 1 的
> two-loop Laman 图:两个三角形共一条内边(K4 去掉一条边,4 顶点 5 内线,$L=E-V+1=2$)。
> 标出:$\nabla_-$ 插入节点、三条外腿 $\nabla_+\mathcal W_+^{A,B,C}$、内部三次规范顶点、
> 5 条 vector 超传播子。**自检写给我**:(i) $L=2$;(ii) 超空间 Grassmann 计数(每圈的
> $d^4\vartheta$ 需要恰好一组 $D^2\bar D^2$ 才能饱和,见 (5B.19));(iii) 由 $\kappa$-transport
> 定出的 color word——把它显式约化,应与 §6 的 $-Q_1^2$ 的 color 结构一致。
>
> **CP2 — 从图到 amplitude。** 用下述规则写出完整超空间被积式(先不做任何 D algebra):
> - vector 超传播子(5B,复述 (5A.69)/(5A.74)):
>   $$\langle V^A(p,\vartheta_1)\,V^B(-p,\vartheta_2)\rangle
>   =\frac{2\hbar g^2\,\kappa^{AB}}{p^2}\,\delta^4(\vartheta_{12}),\qquad
>   \delta^4(\vartheta_{12}):=(\vartheta_1-\vartheta_2)^2(\bar\vartheta_1-\bar\vartheta_2)^2.$$
> - 三次规范顶点:由 (5A.49)–(5A.63) 的 BCH 坐标顶点词取泛函导数,含 (5A.61)–(5A.63) 的
>   排序/Koszul/图权;每条离开手征顶点的内线带一个 $-\tfrac14\bar D^2$(每顶点有一条被吸收),
>   见 5B §"chiral vertices are half-superspace integrals"。
> - 外腿 letter $\nabla_+\mathcal W_+^X$ 与插入 $\nabla_-$ 各自带的 $D$-结构。
> - 两个圈动量积分 $\int d^d\ell_1\,d^d\ell_2/(2\pi)^{2d}$,$d=4-2\epsilon$;
>   两组顶点 $d^4\vartheta$ 积分。
> 把 amplitude 连同全部耦合、$i$-因子、color/flavor、Koszul 符号显式写给我。
>
> **CP3 — D algebra(过程省略,化简后结果给我)。** 做超图 D algebra:把 $D$ 分步积分搬到
> $\vartheta$-delta 与外线上,用 $\{D,\bar D\}_E=-2\sigma_E\partial$(2A.41–42)、投影子
> $\mathcal P_\pm=\bar D^2D^2/16\Box_E$、$D^2\bar D^2D^2=16\Box_E D^2$(5A.65–66),
> 以及圈饱和恒等式
> $$\delta^4(\vartheta_{12})\,D^2\bar D^2\,\delta^4(\vartheta_{12})=16\,\delta^4(\vartheta_{12})$$
> (5B.19)把两组 $d^4\vartheta$ 收成一个单点 $d^4\vartheta$。**只把化简后的结果写给我**:
> 一个动量空间被积式(标量 × 一条 $\sigma$-链),其中残余的 $D$ 已作用到外 letter 上,
> 产出 $\partial_{\dot\alpha}$-型导数结构。**自检写给我**:$D$ 计数守恒(两圈各需一组
> $D^2\bar D^2$ 饱和;总 $D$ 数 = 顶点供给 + 传播子 $\bar D^2$ 之和),leftover $D$ 数应恰好
> 给出输出算符 $\partial_{\dot\alpha}\!X\,\partial^{\dot\alpha}\!Y$ 所需的两个点导数。
>
> **CP4 — 识别 anomaly sector(这是本任务的物理核心)。** 套用 DRED ledger
> (5G §2 / 5B §7 / 5D §5:圈动量严格 $d$ 维;所有 $\sigma$-链、$\gamma_5$、Fierz、frame($\pm$)
> 投影严格四维且形式;两套度规表示**绝不相互缩并**;唯一界面是 $\mu^2$ 公理)。
> 单圈模板是 (5G.5) $(\bar\sigma\!\cdot\!\ell)(\sigma\!\cdot\!\ell)=\ell_d^2+\mu_\ell^2$
> 配 (5G.6) 主积分 $\int\mu^2/(\ell_d^2+\Delta)^3=1/32\pi^2$、$\int\mu^2/D^4=O(\epsilon)$。
> **两圈时仓库尚未陈述以下四点,你必须从头推导并写给我**(honest:这些是 repo gap,
> 见 `step5l`/`step5k` 及本 handoff §给人看部分):
>   1. **两圈主积分骨架**:双 $\mu^2$ 插入 $\iint\mu_{\ell_1}^2\mu_{\ell_2}^2/(D_1^{a}D_2^{b}\dots)$
>      的值(骨架应为 $(1/32\pi^2)^2$),以及单 $\mu^2$ × 子圈 log 的伴项 $\int\mu^2\log(\text{sub})/D^n$。
>   2. **插入计数**:两圈图允许**两个** $\mu^2$(每个坍缩点/每圈一个)**或**一个 $\mu^2$ × 一个
>      子圈 log;把 (T1) 单圈"每标线一个普适 $\mu^2$"推广到两圈,给出独立 $\mu^2$ 因子数与交叉项。
>   3. **R.3 × $\mu^2$ 在两圈**:(R.3) $p^\rho\breve\delta^{mn}(\sigma_m\bar\sigma_\rho\sigma_n)=-2\epsilon\,\sigma\!\cdot\!p$
>      在单圈给 $1/\epsilon\times\epsilon\to$ 有限;两圈的极点可为 $1/\epsilon^2$(整体)或
>      带子发散 $\mu^2$ 的 $1/\epsilon$。给出哪些极点阶遇哪些 evanescent 阶,以及两圈
>      pole-cancellation gate(单圈 W-d 的类比)。
>   4. **两圈配对/坍缩**:把 (5L.1) 配对定理与 (5G.8) 坍缩劈分推广——每个内坍缩点劈成
>      "1"-支 + $\mu^2$-支,坍缩树是各点 $(1+\mu^2/\ell_d^2)$ 之积;判定两圈反常是双-$\mu^2$ 项、
>      单-$\mu^2$×子圈项、还是二者之和,以及"1"-支如何与母 SD 坍缩逐项相消。
> 然后**识别出 anomaly sector**:即在 $\epsilon\to0$ 幸存的、局域(对外动量多项式、$\Delta$-无关)
> 的那部分被积式。**自检写给我**:非反常部分必须像单圈那样成对相消/为 $O(\epsilon)$;
> 反常部分必须局域。
>
> **CP5 — Feynman 参数把积分做掉,给最终结果。** 对带 $\mu^2$ 插入的两圈积分做 Feynman 参数化
> (先做子圈、再做母圈,或 sector decomposition),得到最终
> $$Q_2\big(\mathfrak f^A\mathfrak f^B\mathfrak f^C\big)
> = c_2\cdot(\text{color word})\cdot(\text{输出算符})+O(\epsilon),$$
> 其中 $c_2$ 是显式有理数 × $(1/32\pi^2)^2$(或含单圈子发散时 × $\log$ 的相应结构),
> 输出算符是 $\partial_{\dot\alpha}(\cdot)\partial^{\dot\alpha}(\cdot)$-型(经字典 $\partial c\sim\bar\lambda$
> 即 $\bar\lambda\bar\lambda$ / $\bar\lambda\nabla_+\!\cdots$ 结构)。
>
> ## 3. 黄金检验(必须做,写给我看)
>
> **CP6 — Wess–Zumino 相容性交叉锁。** 这是 HT 从未做过的独立验证,也是本计算的意义所在。
> 由 $Q^2=0$ 逐阶(HT line 394–398):
> $$\{Q_0,Q_2\}=-\,Q_1^2 .$$
> 右边 $-Q_1^2(\mathfrak f^A\mathfrak f^B\mathfrak f^C)$ **完全由已知单圈** $Q_1(\mathfrak f\mathfrak f)$
> (即 HT 的 $Q_1(bb)=\kappa^2 f f[\partial c\partial b-\partial b\partial c]$,line 1099–1100;
> 及本项目 `step5l` 类结果)复合得到——是一个具体可算的表达式。
> 左边把你 CP5 得到的 $Q_2$ 代入,用 tree 括号 $Q_0$(HT line 1153–1170 的 $Q_0\mathfrak f$ 与
> `step5j` 树级锁 $\zeta_Q=\tfrac12$)算 $\{Q_0,Q_2\}$。
> **两边必须相等**(在 $Q_0$-exact 歧义之内)。把两边显式写出并比对,这就是复现 HT 两圈的判据。
> 若不等,回到 CP4 的四点推导找错——通常是 $\mu^2$ 计数或 color word 的问题。
>
> **CP7 — 单圈退化自洽。** 把你的两圈机器"降一圈"(去掉一个 loop / 一个 $\mu^2$ 插入),
> 应重现 `step5l` 的单圈配对定理 (5L.1) 与 $\int\mu^2/D^3=1/32\pi^2$。这是对你两圈推广
> 是否忠实于单圈模板的下界检验。
>
> ## 4. 纪律
>
> - 不许不加推导地引用任何传播子/顶点/系数——每个都从 (4C.42a)+§0 规则导出或引用本仓库已导出的编号式。
> - 每个 CP 都要有一个**人类可读的、可独立复核的中间结论**(图的自检、$D$ 计数、局域性、
>   $\mu^2$ 计数、WZ 相容)。不要把整段计算压成一个黑箱数字。
> - 凡是仓库尚未陈述而你新推的(CP4 的四点、两圈主积分),明确标注 "derived here, gap #k",
>   并尽量配一个小的 sympy 检查(类比 `scripts/check_step5l_bc_anomaly_assembly.py`:
>   显式 $2\times2$ $\sigma$ 矩阵、$\epsilon$ 值、Berezin、su(2) color)。
> - 诚实边界:能算到系数就给系数;只能给到结构就说只到结构;$\varsigma$ 类全局符号/归一
>   若未定,像 5G/5L 那样单独列出、类型化,不要塞进主结果冒充完成。
> - 产出写成 `proposals/step6b-2loop-pure-gauge-riji-<date>.md`(编号式 (6B.$n$)),脚本进 `scripts/`,
>   commit + push 到上述分支;不要开 PR(除非我明说)。
>
> ## 5. 一句话目标
>
> 把纯规范三场强通道的两圈日字图 anomaly sector 老老实实算出来,得到 $Q_2(\mathfrak f\mathfrak f\mathfrak f)$
> 的显式系数与算符,并用 $\{Q_0,Q_2\}=-Q_1^2$ 验证它——这既复现 HT 由相容性自举的两圈结果,
> 又提供 HT 从未做过的直接费曼验证。
