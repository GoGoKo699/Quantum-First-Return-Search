# Three checkpoints with unequal returns

Take the forward cycle

```math
0\to3\to4\to1\to5\to2\to0.
```

The checkpoints are $`S=\{0,1,2\}`$. Starting at $`0,1,2`$ gives first-return times $`3,2,1`$ respectively, so the bound is $`L=3`$. The induced return permutation is $`0\mapsto1\mapsto2\mapsto0`$.

| Input checkpoint | First traversal output | First traversal duration | Second launch slot | Second arrival slot |
| --- | --- | ---: | ---: | ---: |
| $`0`$ | $`1`$ | $`3`$ | $`1`$ | $`3`$ |
| $`1`$ | $`2`$ | $`2`$ | $`2`$ | $`3`$ |
| $`2`$ | $`0`$ | $`1`$ | $`3`$ | $`3`$ |

The branch from $`1`$ waits through slot $`1`$, moves to $`5`$ in slot $`2`$, and reaches checkpoint $`2`$ in slot $`3`$. The branch from $`2`$ waits two slots and takes its one step in slot $`3`$.

Start with the superposition $`\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle`$. A single traversal entangles the arrival labels with clocks $`3,2,1`$. Discarding those orthogonal clocks would remove all cross terms. During the second traversal, each clock value becomes a launch slot. The arrival swap rewrites it to the common value $`3`$. The two data registers agree. XOR clears one and a fixed gate resets the clock. The remaining data state is $`\alpha|1\rangle+\beta|2\rangle+\gamma|0\rangle`$, with the original relative phases.

The previous checkpoint of $`1`$ is $`0`$. The original immediate predecessor of $`1`$ is $`4`$, outside $`S`$. A final forward query on $`0`$ returns $`3`$ and shows that the first-return predecessor reaches $`1`$ by a detour. This extra query distinguishes the two tasks.

[Compiler proof](compiler.md) · [Finite reproduction](../verification/README.md)
