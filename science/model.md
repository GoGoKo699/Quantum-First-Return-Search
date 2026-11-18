# Query model

Let $`X=\{0,\ldots,M-1\}`$ be a known set of basis labels and let $`\pi`$ be an unknown permutation of $`X`$. The input is forward in-place quantum access to the same permutation throughout an execution.

```math
P_\pi |x\rangle=|\pi(x)\rangle .
```

Each query applies this unitary to an arbitrary register, which may be entangled with other registers. The supplied unitary is a basis permutation with the indicated phases. The algorithms use forward queries only. A classical algorithm can choose any basis label in $`X`$ and receive its image per query, including labels outside the checkpoint set.

## Checkpoints and first return

The known checkpoint set $`S\subseteq X`$ has size $`N\ge1`$. For each $`x\in S`$, define its first positive return time and return label by

```math
\tau(x)=\min\{j\ge1:\pi^j(x)\in S\},
\qquad
\rho(x)=\pi^{\tau(x)}(x) .
```

Each cycle of $`\pi`$ meeting $`S`$ gives a cyclic ordering of its checkpoints. The map $`\rho`$ sends each checkpoint to the next one in this ordering, so $`\rho`$ is a permutation of $`S`$. A checkpoint alone on its cycle returns to itself. The known integer $`L\ge1`$ bounds all $`\tau(x)`$ for $`x\in S`$. Cycles disjoint from $`S`$ are unrestricted.

The [worked example](example.md) has three checkpoints on one orbit and return lengths three, two and one.

## Outputs

- **Coherent return map.** Apply $`|x\rangle\mapsto|\rho(x)\rangle`$ on the span of the checkpoint basis states. A clean implementation returns each work register to its initial state. The controlled version also preserves the unqueried branch and its relative phase.
- **Checkpoint predecessor.** For a given target $`y\in S`$, return $`\rho^{-1}(y)`$ with success probability at least $`2/3`$.
- **Immediate predecessor membership.** Decide whether $`\pi^{-1}(y)\in S`$ with success probability at least $`2/3`$. More generally, for a candidate set $`C\subseteq S`$, the decision can test membership in $`C`$. To use $`S=C\cup\{y\}`$, the return bound must hold on this union.


## Known operations and cost

Write $`m=\lceil\log_2 M\rceil`$ and $`\ell=\lceil\log_2(L+1)\rceil`$. Let $`C_S`$ be the cost of a coherent membership circuit that flips a clean bit by $`[x\in S]`$ and returns its scratch space. The compiler charges membership, reversible routing and clock arithmetic as known gates.

The search additionally uses known preparation of $`|u_S\rangle=N^{-1/2}\sum_{x\in S}|x\rangle`$ and its reflection. Denote their costs by $`C_{\mathrm{prep}}`$ and $`C_{\mathrm{refl}}`$, with the latter including coherent control. Efficient membership and reflection are separate assumptions. For a set described by an interval, membership uses a comparator, and preparation can use conditional rotations along the binary interval tree. For a general supplied set, the query bounds hold with the costs of its available known circuits.

The results below report both forward calls and their separate known-gate overhead. A gate count for a concrete implementation also includes the cost of realizing each $`P_\pi`$ call.

[Clean return-map compiler](compiler.md) · [Forward-only predecessor search](search.md)

