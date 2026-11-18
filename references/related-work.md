# Related work

## Forward in-place inversion

Holman, Ramachandran and Yirka give bounded-error square-root query complexity for inverting a permutation with forward in-place access. Their algorithm marks the unknown predecessor, shifts the unmarked labels by the forward permutation, and diffuses using the uniform state. Their controlled-call construction also shows how to route an ordinary forward call through a known reference label. [Quantum Search with In-Place Queries, Theorem 2 and Lemma 3](https://doi.org/10.4230/LIPIcs.TQC.2025.1)

The [exact compiler](../science/compiler.md) furnishes that algorithm with a coherent query to the permutation induced on a known checkpoint set. In the original interface a single query can leave the set, and different starting labels can require different numbers of steps to return. The new circuit uses a second forward traversal to erase those differing return times. Inversion, once the induced oracle exists, uses the earlier algorithm.

## The two-sided question in Embedded PermInv

Section 6.2 of Holman, Ramachandran and Yirka asks whether an immediate predecessor belongs to a specified set in a larger domain, with unrestricted permutation completions. The [bounded-return decision](../science/search.md) augments the checkpoints with the target when needed. A first-return predecessor becomes an immediate predecessor exactly when its original forward image is the target. A constant cap on returns thus supplies a structural regime with a quadratic advantage over classical queries.

Elbassioni, Gajjala and Ray demonstrate a different decision separation between XOR and forward in-place access by embedding Simon instances with fixed random tags. Their construction takes arbitrary completions of an injective map, and their discussion leaves the unrestricted Embedded PermInv conjecture open. The present bounds use the stated return cap. [Random Garbage Creates Exponential Quantum Query Separations](https://arxiv.org/abs/2609.03628)

## Query lower bounds in the return model

Belovs and Yolcu give a cycle-rotation adversary for forward-only in-place inversion. Their estimate bounds the largest eigenvalue of a displacement operator and uses a negative block that would be expensive if its absolute operator norm were taken. The [layered lower bound](../science/lower-bounds.md) applies their matrix inside each single-layer block. The uniform progress difference accumulates over layers, whereas the oracle displacement reduces to the block for the addressed layer. This is the additional step that controls the joint dependence on checkpoint count and return horizon. [One-Way Ticket to Las Vegas and the Quantum Adversary, §10](https://arxiv.org/abs/2301.02003)

The compiler's linear return-horizon lower bound uses a two-checkpoint permutation whose output stores the parity of independent bit flips. The inherited ingredient is the bounded-error parity bound. [Farhi, Goldstone, Gutmann and Sipser](https://doi.org/10.1103/PhysRevLett.81.5442)

## Nearby access models

Tang and Wright show that general unitary-oracle amplitude amplification and estimation can lose their quadratic query advantage when inverse access is withheld. A basis permutation with a known checkpoint membership test and a guaranteed return horizon supplies additional structure in the present model. [Amplitude amplification and estimation require inverses](https://arxiv.org/abs/2507.23787)

Apers and Piddock sample the first-arrival label of a reversible random walk by electric-flow sampling. That output is a sampled destination under a graph model. The present output is a coherent reusable permutation on checkpoint labels for a fixed directed orbit. [Elfs, Trees and Quantum Walks](https://arxiv.org/abs/2211.16379)

[Structured bibliography](references.bib) · [Scientific overview](../science/README.md)
