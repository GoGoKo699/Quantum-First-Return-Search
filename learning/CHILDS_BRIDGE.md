# From Childs to first-return search

Suppose a simulator exposes one reversible update on a set of configurations. Some known configurations are checkpoints. Repeated forward updates take each checkpoint to the next one, with an elapsed time that can depend on the starting configuration. The search task is to identify the checkpoint immediately before a target in this induced cycle.

The educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**, the version dated on the title page of the notes linked from the [author’s University of Maryland course page](https://www.cs.umd.edu/~amchilds/qa/). The [milestone map](MILESTONES.md) pairs those foundations with the [project model](../science/model.md).

## Targeted reading

Page numbers are the printed numbers in the dated notes.

| Sections | Project use | Milestones |
| --- | --- | --- |
| §§1.1–1.2, pp. 1–2 | Basis labels, superposition, registers and known gates | M01–M04 |
| §1.4, pp. 2–3 | Reversible computation and cleaning work registers | M03–M05, M13–M19 |
| §§19.1–19.3, pp. 87–89 | Unstructured search, the marked/unmarked split and coherent amplification | M06–M07, M21–M24 |
| §§23.1–23.3, pp. 109–114 | Comparing pairs of oracles through algorithm-state overlap | M11, M26–M28 |

Childs’s chapter 19 presents unstructured search through a quantum walk. The transferable ideas are the uniform starting state, a distinguished marked component and amplification driven by interference. In the project, the target has an unknown checkpoint predecessor. The [forward-only search step](../science/search.md) uses Holman, Ramachandran and Yirka’s permutation inversion algorithm. Its mark, shift and diffusion operations supply the amplification under the available oracle interface.

Chapter 23 introduces lower bounds by comparing states of the same algorithm under two oracle choices. The project uses the cyclic-rotation relation of Belovs and Yolcu. It rotates a suffix of a single layer’s cycle, changing three successor assignments and the layer’s predecessor of interest. The relative permutation acts as a three-cycle on those three labels. Bounding the largest eigenvalue of the resulting displacement limits how much one forward query can lower the overlap, even when the query is in superposition across layers. [Lower bounds](../science/lower-bounds.md) · [Belovs and Yolcu, *One-Way Ticket to Las Vegas and the Quantum Adversary*](https://arxiv.org/abs/2301.02003)

## Notation

| Object | Notation here | Role |
| --- | --- | --- |
| Ambient labels | $`X`$, with $`M=\lvert X\rvert`$ | Inputs to the original oracle |
| Checkpoint labels | $`S\subseteq X`$, with $`N=\lvert S\rvert`$ | Search domain for the induced permutation |
| Basis permutation | $`P_\pi\lvert x\rangle=\lvert\pi(x)\rangle`$ | One supplied forward call |
| First-return time | $`\tau(x)`$ | Least positive number of forward calls that takes $`x\in S`$ back into $`S`$ |
| Return bound | $`L`$ | Known upper bound on the return time of every checkpoint |
| Induced permutation | $`\rho(x)=\pi^{\tau(x)}(x)`$ | Next checkpoint on the orbit of $`x`$ |
| Uniform state | $`\lvert u_S\rangle=N^{-1/2}\sum_{x\in S}\lvert x\rangle`$ | Known state used in diffusion, called $`\lvert S\rangle`$ in the source’s complete-graph discussion |
| Target and answer | $`y`$ and $`\rho^{-1}(y)`$ | The desired label is the preceding checkpoint on the orbit through $`y`$ |

## A two-checkpoint example

Let $`X=\{0,1,2\}`$, $`S=\{0,2\}`$ and let the ambient orbit be $`0\to1\to2\to0`$. The two return times are $`\tau(0)=2`$ and $`\tau(2)=1`$. The next-checkpoint map swaps $`0`$ and $`2`$. Take $`L=2`$.

Start with a coherent input $`\alpha\lvert0\rangle+\beta\lvert2\rangle`$. Copy its basis label into a zeroed scratch register and traverse forward on the scratch register. The two components record different times.

```math
\alpha\lvert0,2,2\rangle+\beta\lvert2,0,1\rangle .
```

The registers in order are the untouched input label, the scratch return label and the clock. Discarding the clock at this point would remove the off-diagonal coherence between the two components.

Use the clock to schedule departure of the untouched label at slot $`L+1-\tau(x)`$. A label with a two-step return starts in slot 1. A label with a one-step return starts in slot 2. Each branch arrives in slot 2 and the two label registers agree.

```math
\alpha\lvert2,2,2\rangle+\beta\lvert0,0,2\rangle .
```

XOR the first label register into the second and reset the fixed clock. The result is $`\alpha\lvert2\rangle+\beta\lvert0\rangle`$ with clean scratch. The slot schedule uses four forward calls for the two controlled passes. The [compiler proof](../science/compiler.md) gives the reversible gates at each slot.

Now take target $`y=2`$. Its preceding checkpoint is $`0`$. Its immediate ambient predecessor is $`1`$, which is outside $`S`$. Checking the extra forward edge from $`0`$ gives $`\pi(0)=1`$, so the embedded membership answer is negative. The [worked example](../science/example.md) traces the register operations in a separate explicit instance.

## What the project adds

- **Taking one logical step.** The clock first records the travel time and then schedules a complementary launch. The second traversal ends at the same checkpoint as the first, making the clock and the spare label erasable using known gates. [Compiler](../science/compiler.md)
- **Searching with that step.** Each call in the checkpoint search expands into a fixed number of forward oracle slots. The resulting $`O(L\sqrt N)`$ bound is optimal in the worst case when the ambient domain can hold $`L`$ layers of $`N`$ labels. An ambient query checks the immediate-predecessor decision after the checkpoint predecessor has been found. [Search](../science/search.md) · [Lower bounds](../science/lower-bounds.md)
- **Reading the guarantees.** The compiler has an exact promised-subspace action. The search has bounded error, and the known uniform reflection has a separate synthesis cost. The finite checks test instances. The proof covers the full promised subspace. [Model](../science/model.md) · [Verification](../verification/README.md)
