# Verification

Run the finite checks from the repository root with Python 3.9 or later. The script uses the standard library.

```bash
python3 verification/verify_first_return.py
```

The checks apply the rail and clock transpositions directly to computational-basis labels. A three-checkpoint example covers return times of one, two, and three steps, phases on a reference-entangled input, and the final test for immediate predecessor membership. The calibrated query uses an anchor outside the checkpoint set in this example.

The exhaustive checks cover every permutation and nonempty checkpoint set through six ambient labels. They check both the tight return cap and a cap with two extra steps. With up to four ambient labels they also check bijectivity of the compiler on the full basis of its data, control and working registers, including dirty scratch inputs. The calibrated reference is initialized to its known anchor and restored after each oracle slot. Unused binary labels are padded by fixed points for these checks.

The search checks compare flag-zero amplitudes to the closed form at sizes from 2 through 128, including sets whose sizes are not powers of two. Success probabilities include all aborts. These finite checks accompany the general proofs of the [return compiler](../science/compiler.md) and the [search algorithm](../science/search.md).
