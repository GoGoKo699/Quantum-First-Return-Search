# Clean forward-only return maps

A traversal that stops at a checkpoint retains its stopping time in the clock. Return times can vary with the input, so a clock left in this state can distinguish branches. A second traversal starts at the complementary time and puts every clock on the same final value.

## The compiler

**Theorem.** Under the [query model](model.md), an exact clean controlled implementation of the permutation $`P_\rho`$ on checkpoint states costs $`2L`$ forward calls to $`P_\pi`$, following one reusable basis calibration if only ordinary forward calls are supplied. It uses $`O(m+\ell)`$ additional qubits apart from the workspace of the known membership circuit, and $`O(L(C_S+m+\ell))`$ known gates. The implementation preserves arbitrary reference entanglement.

Here $`P_\rho|x\rangle=|\rho(x)\rangle`$ for $`x\in S`$, and $`P_\pi`$ is the supplied oracle. The output is specified on the checkpoint subspace and clean work registers.

### Timed traversal

The traversal acts on an ambient label, a clock, and a register with three modes, $`\mathrm{waiting}`$, $`\mathrm{active}`$ and $`\mathrm{done}`$. An active mode has clock value zero. In slot $`j\in\{1,\ldots,L\}`$, apply the following gates.

1. For a scheduled launch, exchange $`(\mathrm{waiting},j)`$ and $`(\mathrm{active},0)`$ if the label lies in $`S`$.
2. Apply $`P_\pi`$ controlled on active mode.
3. Exchange $`(\mathrm{active},0)`$ and $`(\mathrm{done},j)`$ if the label lies in $`S`$.

The first and third gates each swap two specified computational-basis values of the mode and clock. Membership depends only on the label, so the membership bit can be computed and uncomputed across either swap. Each gate is reversible on the full register space.

Just before any scheduled-launch gate, a branch already active from an earlier slot has a label outside $`S`$. An active branch that reached $`S`$ in an earlier slot entered done mode with that earlier timestamp. The launch gate therefore starts precisely the waiting branches scheduled for this slot. At the end of slot $`j`$, any branch reaching $`S`$ enters done mode with clock value $`j`$. The timestamp $`j`$ is fresh at that slot, and all earlier done branches stay fixed.

### Erasing the timestamp

Use a data label $`A`$ and a clean auxiliary label $`B`$. Bitwise XOR from $`A`$ to $`B`$ makes a coherent duplicate of each basis label.

1. Run the timed traversal on $`B`$ from active mode at slot one. After $`L`$ slots, the labels are $`(A,B)=(x,\rho(x))`$, the mode is done, and the clock is $`\tau(x)`$.
2. Change the common mode from done to waiting. Reversibly replace the clock by $`L+1-\tau(x)`$ and run the scheduled traversal on $`A`$. Each branch travels for the same $`\tau(x)`$ as before, so it reaches $`\rho(x)`$ at slot $`(L+1-\tau(x))+\tau(x)-1=L`$.
3. Now $`(A,B)=(\rho(x),\rho(x))`$ on every branch. XOR $`A`$ into $`B`$ and return the fixed mode and clock to their initial values.

The clock update $`c\mapsto L+1-c`$ can be implemented modulo the clock register size. Its value on the supported inputs lies between 1 and $`L`$, inclusive. The steps use reversible gates and unmodified forward permutation calls, so the basis-state action extends by linearity to a checkpoint superposition with any reference system.

```math
\sum_{x\in S}|x\rangle|r_x\rangle|0_{\mathrm{work}}\rangle
\longmapsto
\sum_{x\in S}|\rho(x)\rangle|r_x\rangle|0_{\mathrm{work}}\rangle .
```

The theorem also holds with an external control. Control the known gates on the external bit, and AND it into each internal forward-slot control. This leaves all work registers in the same state on both external branches.

### Paying for controlled forward calls

Choose a known basis label $`z`$ and query its image once to learn $`\pi(z)`$. Supply a reference register initialized to $`|z\rangle`$. For each controlled call, use a controlled register swap to present the reference to the ordinary oracle when the control is off. After the query, undo the register swap. The reference then contains $`\pi(z)`$ on the off branch and $`z`$ on the on branch. A known conditional XOR by $`z\oplus\pi(z)`$ restores $`|z\rangle`$ on both branches. This uses one ordinary query and $`O(m)`$ known gates. The measured calibration result is reused across all slots and attempts. This instantiates the controlled-query idea of [Holman, Ramachandran and Yirka, Lemma 3](https://doi.org/10.4230/LIPIcs.TQC.2025.1).

Each traversal uses $`L`$ forward slots. A coherent membership evaluation and its cleanup cost $`O(C_S)`$ per routing step. A conditional exchange of two specified clock and mode strings is a known basis transposition using $`O(\ell)`$ reversible gates with clean scratch. One implementation conjugates a multi-controlled bit flip by a known affine binary map that sends the difference of the two strings to a single-bit difference. The clock arithmetic and label XORs fit within the same total bound.

## A matching return-time lower bound

Take the ambient labels to be $`(j,b)`$ with $`j\in\mathbb Z_L`$ and $`b\in\{0,1\}`$. For an unknown bit string $`a_0,\ldots,a_{L-1}`$, choose

```math
\pi(j,b)=(j+1\bmod L,\ b\oplus a_j),
\qquad
S=\{(0,0),(0,1)\}.
```

The return time is $`L`$ from each checkpoint. The image of $`(0,0)`$ under $`\rho`$ contains the parity of all $`L`$ bits, and its checkpoint predecessor reveals the same parity. One ordinary forward query is a standard bit query followed by a known increment. An algorithm with controlled forward queries can also simulate those calls with constant overhead in the bit-query model. The bounded-error quantum parity lower bound is $`\Omega(L)`$, so linear dependence on $`L`$ is necessary even on two checkpoints, for exact compilation or for approximation accurate enough to read out the basis label with bounded error. [Farhi, Goldstone, Gutmann and Sipser](https://doi.org/10.1103/PhysRevLett.81.5442)

[Query model](model.md) · [Forward-only predecessor search](search.md)
