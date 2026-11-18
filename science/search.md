# Forward-only predecessor search

The [compiler](compiler.md) gives a clean forward call to the checkpoint permutation $`\rho`$. Search uses this call in place of the closed-domain oracle in Holman, Ramachandran and Yirka’s algorithm. The proof below makes explicit how diffusion uses a known uniform state on $`S`$, for any checkpoint count. [Holman, Ramachandran and Yirka, Theorem 2](https://doi.org/10.4230/LIPIcs.TQC.2025.1)

## Find the checkpoint predecessor

Fix a target $`y\in S`$ and write $`x_*=\rho^{-1}(y)`$. A basis call checks whether $`\rho(y)=y`$. If it is, output $`y`$. Otherwise $`x_*\ne y`$. For $`N\le3`$, testing the constant number of possible labels is sufficient.

For larger $`N`$, initialize the data register in $`|u_S\rangle`$ and clear an ambient-label register and a flag qubit. One iteration proceeds as follows.

1. **Mark.** Copy the data’s basis label to the label register and apply $`P_\rho`$ to that copy. Set the flag on equality with $`y`$.
2. **Shift.** Apply $`P_\rho`$ to the data register on flag zero. On this branch the two labels are equal, so XOR the data label into the label register to clear it. On flag one the label register contains the known $`y`$, so clear it by conditional XOR with $`y`$.
3. **Diffuse.** Apply $`D=2|u_S\rangle\langle u_S|-I`$ to the data register controlled on the flag state $`|-\rangle`$. Then measure the flag in the computational basis and continue on outcome zero. Outcome one ends the attempt.

Each iteration uses one ordinary and one controlled call to $`P_\rho`$. The known diffusion preserves the checkpoint subspace.

### Why the amplitude grows

After each continuing iteration, the data amplitudes take the value $`\alpha`$ on $`x_*`$ and the same real value $`\beta`$ on all other labels in $`S`$. Initially $`\alpha=\beta=1/\sqrt N`$.

After the shift, the flag-zero vector is $`f=\beta\sum_{z\in S\setminus\{y\}}|z\rangle`$ and the flag-one vector is $`g=\alpha|x_*\rangle`$. Write $`U=|u_S\rangle\langle u_S|`$. The new flag-zero vector is

```math
\frac{f+g + D(f-g)}2
= g+U(f-g)
= \alpha|x_*\rangle+\frac{(N-1)\beta-\alpha}{N}\sum_{z\in S}|z\rangle .
```

Thus its amplitude on $`x_*`$ is $`(1-1/N)(\alpha+\beta)`$. At every other checkpoint it is $`\beta-(\alpha+\beta)/N`$. Its squared norm is $`1-1/N`$, as follows by expanding with $`\alpha^2+(N-1)\beta^2=1`$. This gives the stated two-amplitude form on continuation. Define $`\theta=\arcsin(1/\sqrt N)`$. The normalized pair $`(\alpha,\sqrt{N-1}\,\beta)`$ updates as

```math
\begin{pmatrix}\alpha'\\ \sqrt{N-1}\,\beta'\end{pmatrix}
=
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}
\begin{pmatrix}\alpha\\ \sqrt{N-1}\,\beta\end{pmatrix}.
```

Choose $`k`$ to be the nearest integer to $`\pi/(2\theta)-1`$. An attempt with $`k`$ continuing iterations outputs $`x_*`$ on measuring the data with conditional probability $`\sin^2((k+1)\theta)`$. Its unconditional probability of producing the correct label is

```math
(1-1/N)^k\sin^2((k+1)\theta).
```

For $`N\ge4`$, $`k/(N-1)\le\pi/3`$ and the conditional probability is at least $`3/4`$. Using $`\log(1-1/N)\ge-1/(N-1)`$, an attempt succeeds with probability greater than $`1/4`$. Verify each proposed label by a basis query to $`P_\rho`$ and accept the first verified result. Four attempts give success probability greater than $`2/3`$ in the exact known-gate model.

The hard forward-query budget, including the fixed-point check and verifications, is $`O(L\sqrt N)`$. This bound is tight in the stated worst-case regime of [the layered construction](lower-bounds.md), which applies when $`M\ge LN`$. Apart from the supplied ordinary oracle calls, a gate bound is

```math
O\left(C_{\mathrm{prep}}+\sqrt N\,[L(C_S+m+\ell)+C_{\mathrm{refl}}]\right).
```

Initialization is repeated only a constant number of times. If the known uniform preparation and reflection need synthesis, choose a sufficiently small constant total error budget across the $`O(\sqrt N)`$ calls to known operations. The verified output and repetition margin allow this without changing the asymptotic query count. For example, five attempts give ideal success at least $`1-(3/4)^5`$, leaving room for a total implementation error of $`1/20`$. The displayed gate bound uses the costs of the known circuits at their chosen accuracy.

## Decide immediate predecessor membership

The only checkpoint that could map directly to $`y`$ is $`x_*=\rho^{-1}(y)`$. Indeed, a direct transition from any checkpoint to $`y`$ has return time one, so its induced image is also $`y`$. After verifying the returned $`x_*`$, query $`\pi(x_*)`$. Report that the immediate predecessor belongs to $`S`$ exactly when this query gives $`y`$. For membership in $`C\subseteq S`$, also test $`x_*\in C`$. A failed search attempt can be declared inconclusive during amplification. The final bounded-error decision uses the same order of queries as search.

At return bound two, the [matched lower bounds](lower-bounds.md#the-two-step-immediate-membership-decision) give optimal quantum and randomized classical orders on the same ambient-domain promise. For larger return bounds, scanning the original forward images of the candidate set supplies another upper bound.

[Query model](model.md) · [Clean return-map compiler](compiler.md)
