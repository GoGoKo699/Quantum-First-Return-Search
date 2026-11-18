# Quantum First Return Search

**Can a quantum algorithm find the previous checkpoint in an unknown reversible process using only forward calls?** Two traversals implement one clean first-return query even when different paths spend different amounts of time outside the checkpoints. The resulting quantum search is quadratically faster in checkpoint count in the query model.

Let $`Q_+`$ apply a fixed unknown permutation of $`M`$ labels in place. A known checkpoint set $`S`$ has size $`N`$, and every first return to $`S`$ occurs within $`L`$ forward steps. Write $`\rho(x)`$ for the next checkpoint from $`x`$.

```math
|x\rangle|0\rangle_{\mathrm{work}}
\longmapsto |\rho(x)\rangle|0\rangle_{\mathrm{work}},
\qquad x\in S.
```

| Task | Quantum forward queries | Classical forward queries |
| --- | --- | --- |
| Apply the first-return permutation coherently | $`2L`$ controlled calls, plus one reusable calibration if control must be built. Worst-case order $`\Theta(L)`$. | |
| Find the previous checkpoint of $`y\in S`$ | $`\Theta(L\sqrt N)`$ | $`\Theta(LN)`$ |
| Decide whether the immediate predecessor of $`y\in S`$ is in $`S`$, with $`L=2`$ | $`\Theta(\sqrt N)`$ | $`\Theta(N)`$ |

The search upper bound holds throughout the promise. Matching search lower bounds are realized when $`M\ge LN`$ and $`N\ge3`$. The decision lower bounds use $`M\ge2N`$. Reversible checkpoint membership, uniform-state preparation and reflection have separate gate costs. [Model and resources](science/model.md)

## How the clock disappears

The first traversal records its duration $`\tau`$. The second launches at slot $`L+1-\tau`$, which puts every return at slot $`L`$. Both data registers now hold the same label, so reversible XOR clears one register. A fixed operation clears the common clock. [Unequal-return example](science/example.md)

The induced permutation lets Holman, Ramachandran and Yirka's forward-only inversion algorithm search over the checkpoints. For the lower bound, the layered construction applies Belovs and Yolcu's cycle adversary to each layer and bounds the progress of a single query even in a superposition of layers. [Related work](references/related-work.md)

## Read and reproduce

- [Science overview](science/README.md) links the exact model, compiler, search and lower bounds.
- [Childs bridge](learning/CHILDS_BRIDGE.md) and the [30 milestones](learning/MILESTONES.md) give a learning route.
- [LLM reading guide](llms.txt) maps specific questions to the scientific sources.
- [Verification](verification/README.md) explains the finite checks. Run `python3 verification/verify_first_return.py` from the root.

## Scope

The compiler uses an exact basis permutation and a supplied return cap. It preserves coherence on any input supported on the checkpoint set, including input entangled with a reference. For direct predecessor membership at growing $`L`$, take the better of first-return search and checking all direct images. The unrestricted Embedded PermInv conjecture remains open.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
