# Lower bounds for forward-only search

Under the [query model](model.md), the search output is the unique checkpoint whose first return reaches a known target. The ambient domain has $`M`$ labels, the checkpoint set $`S`$ has $`N`$ labels, and $`L`$ bounds the first return time.

For $`N\ge2`$, $`L\ge1`$ and $`M\ge LN`$, the bounded-error quantum query complexity is $`\Theta(L\sqrt N)`$ and the randomized classical query complexity is $`\Theta(LN)`$. The quantum lower bound permits controlled forward access and arbitrary queries throughout the ambient domain. The lower bounds hold even with known layers and with every return time exactly $`L`$. Immediate predecessor membership has its own bounds below.

The quantum upper bound uses the [two-pass compiler](compiler.md) and [forward-only inversion](search.md). To attain the classical upper bound, follow each checkpoint to its first return. The search resource account charges the known operations separately.

## Layered family

Use layers $`j=0,\ldots,L-1`$, each containing $`N`$ labels. Set $`S`$ to layer zero and fix the target $`(0,y)`$. A tuple $`\boldsymbol p=(p_0,\ldots,p_{L-1})`$ of $`N`$-cycles on $`[N]`$ defines

```math
\pi_{\boldsymbol p}(j,z)=\bigl(j+1\bmod L,p_j(z)\bigr).
```

Any extra labels are fixed points. Define $`a_L=y`$ and $`a_j=p_j^{-1}(a_{j+1})`$ for decreasing $`j`$. The answer is $`(0,a_0)`$. For fixed all layers other than $`j`$, the target $`a_{j+1}`$ of local inversion depends only on the fixed suffix, and the output $`a_0`$ is an injective function of the local predecessor $`a_j`$ through the fixed prefix. The backward recurrence defines the relation on hard instances. All algorithm queries use the forward map.

## Adversary for one layer

The one-layer argument uses Belovs and Yolcu’s cyclic-rotation relation, Lemma 10.4 and Claims 10.5–10.6. For the first-return problem, we combine those relations using a target that depends on the later layers. [Primary source](https://arxiv.org/pdf/2301.02003) · [Related work](../references/related-work.md)

Write a cycle from its fixed inversion target $`b`$ as $`(v_1=b,v_2,\ldots,v_N)`$. Choose $`1\le k\lt \ell\lt N`$ and replace its suffix after $`v_k`$ by the rotation

```math
(v_{\ell+1},\ldots,v_N,v_{k+1},\ldots,v_\ell).
```

The resulting cycle has predecessor $`v_\ell`$ of $`b`$, whereas the original one has predecessor $`v_N`$. This is a symmetric relation whose adjacency matrix $`A`$ has row sum $`d=(N-1)(N-2)/2`$. For each fixed $`k`$, allowing the trivial suffix rotation makes the relation an equivalence relation. Its matrix $`E_k`$ consists of all-ones blocks. Each nontrivial edge determines $`k`$ uniquely from the longest common prefix. Thus

```math
A+(N-2)I=\sum_{k=1}^{N-2}E_k\succeq 0.
```

For neighbors $`p,q`$ and their permutation matrices $`P_p,P_q`$, the matrix $`I-P_p^\dagger P_q`$ is supported on $`v_k,v_\ell,v_N`$. The relative permutation maps $`v_k\mapsto v_\ell\mapsto v_N\mapsto v_k`$. In the block matrix $`D_b=[A_{pq}(I-P_p^\dagger P_q)]_{p,q}`$, isolate the entry from row $`(p,v_N)`$ to column $`(q,v_\ell)`$ in each such block. These entries comprise $`-J A J^\dagger`$, where $`J|p\rangle=|p,p^{-1}(b)\rangle`$ is an isometry. Their maximum eigenvalue is at most $`N-2`$.

In the remaining matrix $`B`$, each nonzero has a row or column indexed by a label other than that cycle's predecessor of $`b`$. For any such label, to be in a nonzero row or column it must be one of the two cuts $`v_k,v_\ell`$. It is a cut for at most $`2N`$ rotations, each contributing at most two entries. Consequently a non-predecessor row or column has at most $`4N`$ entries, and any row or column has at most $`2d`$ entries. For a matrix of entries having magnitude at most one, the operator norm is bounded by the maximum of $`\sqrt{r_i c_j}`$ over its nonzero positions, where $`r_i,c_j`$ count nonzeros in their row and column. This follows from the Schur test with row and column weights $`\sqrt{r_i}`$ and $`\sqrt{c_j}`$. Write norm for the operator norm. Then

```math
\lambda_{\max}(D_b)
\le \operatorname{norm}(B)+\lambda_{\max}(-J A J^\dagger)
\le \sqrt{8Nd}+N-2.
```

The one-sided eigenvalue bound is important. An absolute norm bound for the isolated negative matrix would retain its large eigenvalue magnitude and lose the square-root dependence.

## Assembling the layers

For each $`j`$ build a matrix $`\Gamma_j`$ on tuples by connecting tuples that agree outside layer $`j`$ and have local cycles related by $`A`$ for the fixed target $`a_{j+1}`$. Each $`\Gamma_j`$ is symmetric, nonnegative and has row sum $`d`$. Every adjacent pair yields different final answers. Set $`\Gamma=\sum_j\Gamma_j`$, which has row sum $`Ld`$.

If $`O_{\boldsymbol p}`$ is the supplied quantum oracle, including its optional control, its per-query displacement is the Hermitian block matrix

```math
D=\bigl[\Gamma_{\boldsymbol p,\boldsymbol q}\bigl(I-O_{\boldsymbol p}^{\dagger}O_{\boldsymbol q}\bigr)\bigr]_{\boldsymbol p,\boldsymbol q}.
```

The relative permutation preserves the input layer since both forward permutations advance by one. On query layer $`k`$, an edge from $`\Gamma_j`$ with $`j\ne k`$ contributes zero because the forward action on $`k`$ is unchanged. The surviving block splits by the fixed other layer permutations, and within each block it equals $`D_b`$ for the suffix-dependent target $`b=a_{k+1}`$. Inactive control and padded labels contribute zero. A coherent query may superpose all layers, but their displacement is a direct sum, so $`\lambda_{\max}(D)=O(N^{3/2})`$, independently of $`L`$.

Let $`K`$ be the number of hard inputs and $`|\psi_{\boldsymbol p}^t\rangle`$ be the normalized algorithm state for input $`\boldsymbol p`$ after step $`t`$. Deferred measurement and controlled idle query slots cover arbitrary adaptive bounded-query algorithms. For the normalized vector

```math
|\Psi_t\rangle=K^{-1/2}\sum_{\boldsymbol p}|\boldsymbol p\rangle|\psi_{\boldsymbol p}^t\rangle,
```

track $`W_t=\langle\Psi_t|(\Gamma\otimes I)|\Psi_t\rangle`$. Known processing leaves $`W_t`$ invariant. One forward query lowers it by at most $`\lambda_{\max}(D)`$, by substituting the controlled action into the quadratic form. Initially $`W_0=Ld`$. On each edge, measuring the output separates the distinct answers with probability at least $`2/3`$ on each endpoint. The absolute final overlap is at most $`2\sqrt2/3`$ by Cauchy–Schwarz on the two outcomes of the test for the first endpoint's answer. Therefore

```math
T\ge\frac{(1-2\sqrt2/3)Ld}{\sqrt{8Nd}+N-2}.
```

Since $`d=(N-1)(N-2)/2`$, this is $`\Omega(L\sqrt N)`$ for $`N\ge3`$. For $`N=2`$, the [parity construction](compiler.md#a-matching-return-time-lower-bound) yields $`\Omega(L)`$. For $`N=1`$ the answer is the sole checkpoint.

## Matched classical lower bound

Use the same graph of instances and couple two classical executions by giving them the same input-independent randomness. A randomized algorithm with success at least $`2/3`$ on every input is correct on both ends of an edge with probability at least $`1/3`$. As the correct outputs differ, the query transcripts must split on at least this probability. For a fixed random seed, charge each split edge at its first difference to one of the endpoint executions. At this point the queried address $`(j,z)`$ is the same on both ends, and the two instances differ only in layer $`j`$. At least one endpoint has $`z`$ different from its predecessor of $`a_{j+1}`$, since the endpoints have different local predecessors and share $`a_{j+1}`$. Charge to one such endpoint. Its address can be altered in at most $`2N`$ adjacent rotations, because it must be one of the two cuts. A depth-$`T`$ deterministic decision tree therefore receives at most $`2NT`$ charges per input. Averaging over seeds gives

```math
2NTK\ge \frac13\frac{KLd}{2}.
```

This is $`\Omega(LN)`$ for $`N\ge3`$. For $`N=2`$, under uniformly random parity bits every transcript leaving a bit unread has a uniform answer. The parity construction therefore requires $`\Omega(L)`$ classical queries at bounded error. The family uses identical query access for both algorithms and allows queries at any ambient labels.

## The two-step immediate-membership decision

With $`L=2`$ and $`M\ge 2N`$, deciding whether the immediate predecessor of $`y`$ belongs to $`S`$ has quantum query complexity $`\Theta(\sqrt N)`$ and randomized classical query complexity $`\Theta(N)`$. In the cases $`N=1,2`$, both answers are possible, so a constant lower bound suffices.

For the quantum lower bound when $`N\ge3`$, fix a label $`y`$ of a single $`N`$-cycle $`p`$ and a bit function $`b`$ that splits $`[N]\setminus\{y\}`$ into two pieces whose sizes differ by at most one. Consider finding $`b(p^{-1}(y))`$. Use the full one-layer cycle relation above. Under a uniform ordered edge, the two predecessor labels are uniform distinct elements of $`[N]\setminus\{y\}`$, because they are the labels in two distinct positions other than the first in a uniform cycle. At least half the edges have opposite answer bits. These edges contribute at least the constant overlap drop above, and edges with the same answer contribute a nonnegative drop. The same one-sided per-query bound therefore gives $`\Omega(\sqrt N)`$ for this bit task.

Compile an instance of immediate membership on two tagged copies of $`[N]`$. A step first changes $`(z,t)`$ to $`(z,t\oplus b(z))`$, then applies $`p`$ to the first register only if the resulting tag is zero. This uses one controlled forward call and implements a permutation. Take $`S`$ to be tag zero and the target to be $`(y,0)`$. A checkpoint with $`b(z)=0`$ returns in one step. When $`b(z)=1`$ it toggles to tag one, then toggles back and applies $`p`$. The immediate predecessor of $`(y,0)`$ equals $`(p^{-1}(y),b(p^{-1}(y)))`$, so membership in $`S`$ decides the bit. Pad by fixed points for larger $`M`$. The [search algorithm](search.md) and one final forward check supply the matching upper bound.

### Classical comparison at return bound two

Choose a uniformly random permutation of $`S`$ and fix every non-checkpoint label. This is the yes instance. Independently choose a uniform non-checkpoint label $`w`$. Splice $`w`$ between the target’s predecessor $`x`$ and the target. This is the no instance. The two oracles differ only at $`x`$ and $`w`$, and the return bound is at most two on both instances.

Until a classical execution queries one of the two differing addresses, its transcript agrees on the paired instances. Under the yes oracle, as long as the target’s predecessor has not been queried, it is uniform among the unqueried checkpoints by deferred decisions. A $`T`$-query algorithm hits $`x`$ with probability at most $`T/N`$. The label $`w`$ is independent of the yes transcript, so the probability of hitting $`w`$ is at most $`T/(M-N)`$. Transcript total variation is bounded by the sum of these two probabilities. Success $`2/3`$ for both yes and no requires total variation at least $`1/3`$, giving $`\Omega(N)`$ queries when $`M\ge2N`$. Querying the direct image of each checkpoint attains the upper bound.

The factor $`L`$ in the search lower bound comes from the hard layered family, which uses $`LN`$ ambient labels. Smaller ambient domains restrict which return profiles can coexist.

[Query model](model.md) · [Return-map compiler](compiler.md) · [Search algorithm](search.md) · [Related work](../references/related-work.md)
