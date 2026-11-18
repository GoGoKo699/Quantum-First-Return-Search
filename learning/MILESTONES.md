# First-return search in 30 milestones

The first 12 milestones build the access model, the idea of clean quantum work registers and the search and lower-bound tools. The next 18 trace the two-pass compiler, show how it gives a searchable permutation, and compare the resulting cost to lower bounds for the same interface. The [Childs bridge](CHILDS_BRIDGE.md) maps the prerequisites to the single educational anchor. The [scientific overview](../science/README.md) leads directly to the definitions and proofs.

| Phase | Milestones | Connection |
| --- | --- | --- |
| Background and preliminaries | [M01](#m01-a-permutation-as-reversible-motion)–[M05](#m05-reversible-control-without-a-measurement) | Reversible basis dynamics, coherent queries and clean workspace |
| Background and preliminaries | [M06](#m06-the-markedunmarked-decomposition)–[M12](#m12-the-complete-access-contract) | Search intuition, return maps, predecessor tasks and access promises |
| Narrative and innovation | [M13](#m13-a-branch-with-two-different-return-lengths)–[M20](#m20-charging-the-two-passes) | From unequal return times to a clean callable permutation |
| Narrative and innovation | [M21](#m21-mark-and-shift)–[M25](#m25-from-search-to-embedded-membership) | From the compiled call to search and embedded decision |
| Narrative and innovation | [M26](#m26-the-classical-splice-comparison)–[M30](#m30-the-complete-first-return-search-argument) | Lower bounds, scope and synthesis |

## Phase I · Background and preliminaries

### M01 A permutation as reversible motion

**Central question.** What does one step do to a configuration?

**Understanding target.** Identify an unknown bijection on a known finite label set. Decompose its action into directed cycles with one successor and one predecessor per label.

**Prerequisites.** None within this map.

**Conceptual connection.** Cycles supply a finite setting where every checkpoint along an orbit has a next occurrence.

**Canonical sources.** [Model](../science/model.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M02 Forward coherent access

**Central question.** What can the query box do to a superposition of labels?

**Understanding target.** Extend basis relabeling linearly to a unitary. Distinguish a forward in-place call from direct inverse access and from a value oracle with a separate output register.

**Prerequisites.** [M01](#m01-a-permutation-as-reversible-motion).

**Conceptual connection.** An available inverse is an interface assumption. The mathematical existence of a reverse map leaves that interface unchanged.

**Canonical sources.** [Model](../science/model.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M03 A label copy in superposition

**Central question.** What happens when a known XOR gate copies a basis label into a zeroed register?

**Understanding target.** Track the resulting correlated pair for a superposed input. Understand how equal labels can later clear one register by a second XOR.

**Prerequisites.** [M01](#m01-a-permutation-as-reversible-motion), [M02](#m02-forward-coherent-access).

**Conceptual connection.** The two traversals use a shared basis label coherently, with correlations between registers.

**Canonical sources.** [Compiler](../science/compiler.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M04 Why a timing record affects interference

**Central question.** What happens to an output when distinguishable timing records are ignored?

**Understanding target.** Read coherence from inner products between the attached work states. Equal work states retain interference between components, whereas orthogonal work states suppress the cross terms when discarded.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M03](#m03-a-label-copy-in-superposition).

**Conceptual connection.** The later diffusion step requires amplitudes to interfere across paths with different original return times.

**Canonical sources.** [Compiler](../science/compiler.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M05 Reversible control without a measurement

**Central question.** How can a circuit act only on branches in a specified mode?

**Understanding target.** Compute a known condition coherently, use it to control a transposition of register values, and uncompute the condition. Explain why both directions of the transposition define a reversible circuit on the full register space.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M03](#m03-a-label-copy-in-superposition).

**Conceptual connection.** Arrival and launch combine a known checkpoint test with reversible mode changes.

**Canonical sources.** [Compiler](../science/compiler.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M06 The marked/unmarked decomposition

**Central question.** How does an unknown answer become a special component of a known initial state?

**Understanding target.** Split the uniform superposition into a marked direction and the uniform direction over unmarked inputs. Relate a single marked label to initial amplitude determined by the size of the search domain.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M04](#m04-why-a-timing-record-affects-interference).

**Conceptual connection.** The predecessor of the target is the unique marked label for the induced permutation.

**Canonical sources.** [Search](../science/search.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M07 Interference as amplification

**Central question.** Why can a small marked amplitude grow over repeated iterations?

**Understanding target.** Explain how interference in the marked/unmarked plane can build marked amplitude. Connect the rotation scale for one marked label with the square-root search scale.

**Prerequisites.** [M04](#m04-why-a-timing-record-affects-interference), [M06](#m06-the-markedunmarked-decomposition).

**Conceptual connection.** The permutation-specific search will require coherent relabeling as well as a mark.

**Canonical sources.** [Search](../science/search.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M08 First returns to a checkpoint set

**Central question.** What makes a return the first one?

**Understanding target.** Define the checkpoint set, the least positive return time and its known cap. Explain why the starting position does not count as a return and why the cap can exceed the actual travel time.

**Prerequisites.** [M01](#m01-a-permutation-as-reversible-motion), [M02](#m02-forward-coherent-access).

**Conceptual connection.** The promise constrains the excursions, permitting a fixed circuit schedule even though individual branches differ.

**Canonical sources.** [Model](../science/model.md) · [Worked example](../science/example.md)

### M09 The induced checkpoint permutation

**Central question.** Why is the next-checkpoint map bijective?

**Understanding target.** Restrict the cyclic order of each ambient orbit to its checkpoint labels. Show that taking the next retained label permutes the checkpoint set, including an orbit with a single checkpoint.

**Prerequisites.** [M01](#m01-a-permutation-as-reversible-motion), [M08](#m08-first-returns-to-a-checkpoint-set).

**Conceptual connection.** This closed permutation is the input interface expected by the inherited inversion routine.

**Canonical sources.** [Model](../science/model.md) · [Search](../science/search.md)

### M10 Two meanings of predecessor

**Central question.** How can a preceding checkpoint differ from the immediate ambient predecessor?

**Understanding target.** Trace both answers along a cycle that leaves the checkpoint set. Identify the extra test needed to tell whether a candidate checkpoint is directly adjacent to the target.

**Prerequisites.** [M08](#m08-first-returns-to-a-checkpoint-set), [M09](#m09-the-induced-checkpoint-permutation).

**Conceptual connection.** The search output and the embedded membership decision have separate resource claims.

**Canonical sources.** [Model](../science/model.md) · [Worked example](../science/example.md)

### M11 Comparing nearby oracles

**Central question.** How can pairs of possible query boxes force an algorithm to spend more queries?

**Understanding target.** Follow the adversary principle from identical initial states to distinguishable final outputs. Identify how overlap progress depends on the query amplitudes where neighboring inputs differ.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M04](#m04-why-a-timing-record-affects-interference).

**Conceptual connection.** The project lower bounds build explicit oracle pairs with different outputs and controlled query-level differences.

**Canonical sources.** [Lower bounds](../science/lower-bounds.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M12 The complete access contract

**Central question.** Which operations and promises make the project question precise?

**Understanding target.** Assemble the ambient oracle, known checkpoint membership, known return cap and preparation or reflection about the uniform checkpoint state. Place controlled calls, scratch and gate synthesis in the resource budget.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M05](#m05-reversible-control-without-a-measurement), [M07](#m07-interference-as-amplification), [M08](#m08-first-returns-to-a-checkpoint-set), [M09](#m09-the-induced-checkpoint-permutation), [M10](#m10-two-meanings-of-predecessor), [M11](#m11-comparing-nearby-oracles).

**Conceptual connection.** This closes the background by keeping the compiler, search, decision and lower-bound contracts explicit.

**Canonical sources.** [Model](../science/model.md) · [Scientific overview](../science/README.md)

## Phase II · Narrative and innovation

### M13 A branch with two different return lengths

**Central question.** What does a short outward excursion do to a superposed checkpoint input?

**Understanding target.** Follow a two-checkpoint cycle whose checkpoint-to-checkpoint travel lengths differ. Predict the return labels and recorded times for each input basis branch.

**Prerequisites.** [M04](#m04-why-a-timing-record-affects-interference), [M08](#m08-first-returns-to-a-checkpoint-set), [M09](#m09-the-induced-checkpoint-permutation), [M12](#m12-the-complete-access-contract).

**Conceptual connection.** The example shows why the first traversal reveals the right labels yet leaves a time record.

**Canonical sources.** [Worked example](../science/example.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M14 Recording the first arrival

**Central question.** How does a clocked forward pass stop the appropriate branches?

**Understanding target.** Follow the forward call on active branches and the checkpoint-controlled transfer into the done mode. Explain why an arrival recorded in an earlier slot cannot be reactivated by a later slot.

**Prerequisites.** [M05](#m05-reversible-control-without-a-measurement), [M08](#m08-first-returns-to-a-checkpoint-set), [M13](#m13-a-branch-with-two-different-return-lengths).

**Conceptual connection.** Fresh clock values allow reversible ejection after the first positive return.

**Canonical sources.** [Compiler](../science/compiler.md) · [Worked example](../science/example.md)

### M15 The state after the first pass

**Central question.** What information remains available after every branch has returned?

**Understanding target.** Identify the untouched input label, the scratch copy of the return label and the branch-dependent clock. Account for the common done mode.

**Prerequisites.** [M03](#m03-a-label-copy-in-superposition), [M04](#m04-why-a-timing-record-affects-interference), [M13](#m13-a-branch-with-two-different-return-lengths), [M14](#m14-recording-the-first-arrival).

**Conceptual connection.** The untouched input can repeat the same excursion, and the clock can set its launch time.

**Canonical sources.** [Compiler](../science/compiler.md) · [Worked example](../science/example.md)

### M16 Scheduling a common finish

**Central question.** How can branches with unequal travel lengths arrive together?

**Understanding target.** Translate each recorded duration into its complementary launch slot. Count slots inclusively to show that this second traversal ends in the fixed final slot.

**Prerequisites.** [M08](#m08-first-returns-to-a-checkpoint-set), [M14](#m14-recording-the-first-arrival), [M15](#m15-the-state-after-the-first-pass).

**Conceptual connection.** The clock determines a forward launch while retaining reversibility. The second arrival replaces its varying value by a constant.

**Canonical sources.** [Compiler](../science/compiler.md) · [Worked example](../science/example.md)

### M17 The final XOR cleanup

**Central question.** Why can the spare label be reset at the end?

**Understanding target.** Track the equal return labels in the two data registers and the common arrival slot in the clock. Clear the scratch label by XOR and reset fixed values with known gates.

**Prerequisites.** [M03](#m03-a-label-copy-in-superposition), [M15](#m15-the-state-after-the-first-pass), [M16](#m16-scheduling-a-common-finish).

**Conceptual connection.** The input register has undergone exactly the induced permutation and the cleanup leaves no branch-dependent output record.

**Canonical sources.** [Compiler](../science/compiler.md) · [Worked example](../science/example.md)

### M18 Correctness on entangled inputs

**Central question.** What makes the construction a coherent oracle rather than a basis-state demonstration?

**Understanding target.** Extend the exact clean basis action to any superposition and tensor it with an untouched reference. Check that the same zero work state accompanies every output.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M04](#m04-why-a-timing-record-affects-interference), [M17](#m17-the-final-xor-cleanup).

**Conceptual connection.** Clean workspace is the condition that lets a search circuit use this subroutine repeatedly and interfere across different starting states.

**Canonical sources.** [Compiler](../science/compiler.md) · [Model](../science/model.md)

### M19 Coherent control of the oracle call

**Central question.** What extra access is needed to choose coherently whether to query?

**Understanding target.** Follow the controlled-query implementation using a known input/output calibration pair and controlled exchanges with a spare register. Explain how the known correction cleans the spare label.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M05](#m05-reversible-control-without-a-measurement), [M18](#m18-correctness-on-entangled-inputs).

**Conceptual connection.** Each controlled forward slot can count as one ordinary forward call after calibration.

**Canonical sources.** [Compiler](../science/compiler.md) · [Related work](../references/related-work.md)

### M20 Charging the two passes

**Central question.** Which costs scale with the return bound and which with register size?

**Understanding target.** Count the scheduled forward slots, checkpoint tests, label registers and clock bits. Identify separately the preparation and reflection costs that later depend on the chosen representation of the checkpoint set.

**Prerequisites.** [M12](#m12-the-complete-access-contract), [M14](#m14-recording-the-first-arrival), [M16](#m16-scheduling-a-common-finish), [M17](#m17-the-final-xor-cleanup), [M19](#m19-coherent-control-of-the-oracle-call).

**Conceptual connection.** The compiler promises a linear-in-cap query cost. Its known gates have their own cost model.

**Canonical sources.** [Compiler](../science/compiler.md) · [Model](../science/model.md)

### M21 Mark and shift

**Central question.** How does forward-only inversion keep the mark while cleaning its work label?

**Understanding target.** Trace copying and evaluating a checkpoint label, recording whether its image equals the target, and shifting the unmarked branch. Identify how each branch removes the spare return label.

**Prerequisites.** [M03](#m03-a-label-copy-in-superposition), [M06](#m06-the-markedunmarked-decomposition), [M09](#m09-the-induced-checkpoint-permutation), [M18](#m18-correctness-on-entangled-inputs), [M20](#m20-charging-the-two-passes).

**Conceptual connection.** The forward-only inversion needs a callable clean permutation, even though the mark concerns its inverse image.

**Canonical sources.** [Search](../science/search.md) · [Related work](../references/related-work.md)

### M22 Diffuse the difference

**Central question.** What turns marked and unmarked tracks into growth of the marked amplitude?

**Understanding target.** Read the flag in its plus/minus basis and relate diffusion in one branch to the marked/unmarked recurrence. Separate the continue branch from the probability paid to obtain it.

**Prerequisites.** [M04](#m04-why-a-timing-record-affects-interference), [M06](#m06-the-markedunmarked-decomposition), [M07](#m07-interference-as-amplification), [M21](#m21-mark-and-shift).

**Conceptual connection.** Interference works because the compiler and the mark/shift step have both cleaned their data work registers.

**Canonical sources.** [Search](../science/search.md)

### M23 The fixed point and the output check

**Central question.** How does the algorithm handle a target that returns to itself?

**Understanding target.** Trace the preflight test, the remaining search case and the check on a proposed checkpoint predecessor. Distinguish the probability of surviving the search steps from the correctness of a verified result.

**Prerequisites.** [M09](#m09-the-induced-checkpoint-permutation), [M10](#m10-two-meanings-of-predecessor), [M21](#m21-mark-and-shift), [M22](#m22-diffuse-the-difference).

**Conceptual connection.** These checks give a bounded-error procedure, including on small checkpoint sets.

**Canonical sources.** [Search](../science/search.md) · [Verification](../verification/README.md)

### M24 Composing the query counts

**Central question.** Where do the return bound and the square root of the checkpoint count enter?

**Understanding target.** Multiply the cost per clean induced call by the number of calls in the inversion routine. Include initial and final checks and the constant number of repetitions for fixed error.

**Prerequisites.** [M07](#m07-interference-as-amplification), [M20](#m20-charging-the-two-passes), [M21](#m21-mark-and-shift), [M22](#m22-diffuse-the-difference), [M23](#m23-the-fixed-point-and-the-output-check).

**Conceptual connection.** The resulting search cost is a function of the checkpoint set and the return promise, with separate known-gate accounting.

**Canonical sources.** [Search](../science/search.md) · [Model](../science/model.md)

### M25 From search to embedded membership

**Central question.** How does the preceding checkpoint answer an immediate-predecessor question?

**Understanding target.** Take the returned checkpoint candidate and check its next ambient label. If the decision instance uses an original candidate set, also check that the candidate belongs to it.

**Prerequisites.** [M10](#m10-two-meanings-of-predecessor), [M23](#m23-the-fixed-point-and-the-output-check), [M24](#m24-composing-the-query-counts).

**Conceptual connection.** A path can pass through an outside label without changing the order of the checkpoints. The extra call detects that difference, and the two-step promise admits a quadratic quantum query advantage.

**Canonical sources.** [Search](../science/search.md) · [Worked example](../science/example.md)

### M26 The classical splice comparison

**Central question.** Why does a two-step return still leave a hard classical decision problem?

**Understanding target.** Compare a random permutation on the checkpoints with a splice inserting a hidden outside label immediately before the target. Explain why a classical transcript first differs only when it queries one of the two altered inputs.

**Prerequisites.** [M10](#m10-two-meanings-of-predecessor), [M11](#m11-comparing-nearby-oracles), [M25](#m25-from-search-to-embedded-membership).

**Conceptual connection.** The matched decision comparison gives linear classical query cost even when no excursion takes more than two steps.

**Canonical sources.** [Lower bounds](../science/lower-bounds.md)

### M27 Parities and layers

**Central question.** How can the number of forward steps carry independent information?

**Understanding target.** Follow a parity bit transported through a sequence of layers. Then describe the wider search construction, where each layer routes labels by a cycle. Explain how rotating a suffix of one cycle changes the predecessor of the label determined by the layers beyond it, and therefore changes the final answer.

**Prerequisites.** [M01](#m01-a-permutation-as-reversible-motion), [M09](#m09-the-induced-checkpoint-permutation), [M11](#m11-comparing-nearby-oracles), [M20](#m20-charging-the-two-passes).

**Conceptual connection.** The parity instance diagnoses the compiler cost. The layered permutation family supports a distinct lower-bound argument for search.

**Canonical sources.** [Lower bounds](../science/lower-bounds.md)

### M28 Overlap progress under one forward query

**Central question.** Which amplitudes govern the progress on a layered oracle pair?

**Understanding target.** Locate the three input labels moved by the relative three-cycle. Explain how bounding the largest eigenvalue of the displacement controls overlap loss. Show why the displacement splits by the queried layer, while the initial overlap weight grows with the number of layers.

**Prerequisites.** [M02](#m02-forward-coherent-access), [M11](#m11-comparing-nearby-oracles), [M26](#m26-the-classical-splice-comparison), [M27](#m27-parities-and-layers).

**Conceptual connection.** The largest-eigenvalue bound uses the sign of the predecessor block. The resulting one-sided query bound matches the compiler-based search order when the ambient space can hold all the layers.

**Canonical sources.** [Lower bounds](../science/lower-bounds.md) · [Childs bridge](CHILDS_BRIDGE.md)

### M29 Reading the evidence and scope

**Central question.** What supports each conclusion and which input promises are essential?

**Understanding target.** Distinguish the proof of a clean call, the inherited inversion analysis, the constructed lower-bound families and the finite verification checks. Identify which cost statements are about queries and which depend on known gate circuits.

**Prerequisites.** [M12](#m12-the-complete-access-contract), [M18](#m18-correctness-on-entangled-inputs), [M24](#m24-composing-the-query-counts), [M25](#m25-from-search-to-embedded-membership), [M26](#m26-the-classical-splice-comparison), [M27](#m27-parities-and-layers), [M28](#m28-overlap-progress-under-one-forward-query).

**Conceptual connection.** The conclusions apply at the stated return cap and oracle interface, with their search and decision claims kept separate.

**Canonical sources.** [Scientific overview](../science/README.md) · [Related work](../references/related-work.md) · [Verification](../verification/README.md)

### M30 The complete first-return search argument

**Central question.** Why does a variable-time traversal still support a coherent search?

**Understanding target.** Explain the whole path from a basis permutation through timestamp recording, complementary launch, clean induced action and amplified predecessor search. Match the optimal search order, the two-step decision separation and the compiler bound with their respective oracle families and assumptions.

**Prerequisites.** [M12](#m12-the-complete-access-contract), [M16](#m16-scheduling-a-common-finish), [M18](#m18-correctness-on-entangled-inputs), [M23](#m23-the-fixed-point-and-the-output-check), [M24](#m24-composing-the-query-counts), [M25](#m25-from-search-to-embedded-membership), [M28](#m28-overlap-progress-under-one-forward-query), [M29](#m29-reading-the-evidence-and-scope).

**Conceptual connection.** The project connects a concrete reversible circuit to an oracle algorithm and the limits of the corresponding model.

**Canonical sources.** [Scientific overview](../science/README.md) · [Model](../science/model.md) · [Lower bounds](../science/lower-bounds.md)
