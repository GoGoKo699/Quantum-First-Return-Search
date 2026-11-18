# Scientific account

A permutation partitions its labels into directed cycles. Looking only at selected labels gives another permutation: each checkpoint maps to the next checkpoint on its cycle. With forward-only access to the original process, a circuit for this smaller oracle has to clear the record of how long each excursion lasted.

| Reader question | Source |
| --- | --- |
| What input and resources are supplied? | [Model and results](model.md) |
| Where does a variable-duration clock end up? | [Unequal-return example](example.md) |
| How can a reversible circuit clear every record in forward time? | [Exact compiler](compiler.md) |
| How does the induced map enable inversion and the membership decision? | [Search and decision](search.md) |
| Which bounds are tight on the same family? | [Lower bounds](lower-bounds.md) |
| Which ingredients come from earlier work? | [Related work](../references/related-work.md) |

The compiler translates any forward-only circuit for the induced permutation to the original interface with a linear cost per query. Inversion is one application. First-return predecessor search and immediate predecessor membership ask different questions. A detour can leave the first-return answer intact while changing the membership answer.

Start with the [Childs bridge](../learning/CHILDS_BRIDGE.md) to learn the background. The [verification suite](../verification/README.md) checks the finite circuit and search examples.
