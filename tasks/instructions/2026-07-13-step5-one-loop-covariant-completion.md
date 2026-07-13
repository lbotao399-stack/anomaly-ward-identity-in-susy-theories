# 2026-07-13 Step-5 one-loop covariant completion

## User instruction (verbatim)

还有一个可研究的问题：即1-loop exact prove.
对于O=\nabla_-(\nabla_+ W_+^A \nabla_+ W_+^B)等， 单圈三角图应当是所有的核心结果。但是单纯一个三角图大概没有把整个规范不变性的结果得出，还会有类似四边形、五边形图等，缀饰三角图的结果，使得最终结果就是三角图的结果+规范不变化（例如\bar W展开是V的好几项下去）.这件事有点类似非阿贝尔规范场论里的ABJ anomaly，那里真正产生核心结果的就是三角图，而四边形、五边形图结果也非零，但只是形成对三角图的缀饰，恢复完全F F结构而已。这里我希望研究证明同样的事情----supergraph的1-loop跟高阶图只是缀饰W等结构。这里关于vector representation & chiral representation的问题需要仔细研究，建议和pro商讨几轮后才开始大批量进行

## Scope lock

$$
\boxed{
\text{one-loop exact completion}
:=
\text{one fixed one-loop local coefficient}
+
\text{its all-background-leg covariant completion}.}
$$

$$
\boxed{
\text{This task does not assert}
\quad
\Gamma_{\mathscr O}^{(\ell)}=0
\quad(\ell\ge2).}
$$

No bulk box/pentagon generation is admitted before the theorem gates in
`audits/step5-one-loop-covariant-completion-gap-audit.md` pass.
