#!/usr/bin/env python3
"""Check the return compiler, its coherent action, and the search routine."""

from itertools import combinations, permutations, product
from math import asin, isclose, pi, sin, sqrt
from random import Random


WAITING, ACTIVE, DONE = range(3)


def swap_if(value, left, right, enabled):
    """Apply a transposition when its control is enabled."""
    if enabled:
        if value == left:
            return right
        if value == right:
            return left
    return value


def controlled_forward(value, permutation, enabled, calibration):
    """Model the single forward query routed through a calibrated basis label."""
    anchor, anchor_image = calibration
    reference = anchor
    if not enabled:
        value, reference = reference, value
    value = permutation[value]
    if not enabled:
        value, reference = reference, value
        reference ^= anchor_image ^ anchor
    assert reference == anchor
    return value


def timed_forward(value, rail_clock, permutation, checkpoints, cap, launch, calibration):
    """Apply the slot gates to a basis input."""
    for slot in range(1, cap + 1):
        rail_clock = swap_if(
            rail_clock, (WAITING, slot), (ACTIVE, 0), launch and value in checkpoints
        )
        value = controlled_forward(
            value, permutation, rail_clock[0] == ACTIVE, calibration
        )
        rail_clock = swap_if(
            rail_clock, (ACTIVE, 0), (DONE, slot), value in checkpoints
        )
    return value, rail_clock


def compile_basis(state, permutation, checkpoints, cap, calibration):
    """Execute the controlled compiler as an explicit basis permutation."""
    control, data, scratch, rail, clock = state
    if control == 0:
        return state

    scratch ^= data
    rail ^= WAITING ^ ACTIVE
    scratch, (rail, clock) = timed_forward(
        scratch, (rail, clock), permutation, checkpoints, cap, False, calibration
    )

    clock_modulus = 1 << cap.bit_length()
    clock = (cap + 1 - clock) % clock_modulus
    rail ^= DONE ^ WAITING
    data, (rail, clock) = timed_forward(
        data, (rail, clock), permutation, checkpoints, cap, True, calibration
    )

    scratch ^= data
    rail ^= DONE ^ WAITING
    clock ^= cap
    return control, data, scratch, rail, clock


def first_return(value, permutation, checkpoints):
    """Compute a first return by direct forward iteration of one label."""
    current = value
    for elapsed in range(1, len(permutation) + 1):
        current = permutation[current]
        if current in checkpoints:
            return current, elapsed
    raise AssertionError("A checkpoint must return on its finite permutation cycle")


def verify_unequal_return_example():
    """Check variable return time, controlled superposition, and membership."""
    permutation = (3, 5, 0, 4, 1, 2, 7, 6)
    checkpoints = {0, 1, 2}
    cap = 3
    calibration = (7, permutation[7])
    expected = {0: (1, 3), 1: (2, 2), 2: (0, 1)}
    assert {
        value: first_return(value, permutation, checkpoints) for value in checkpoints
    } == expected

    state = {
        ("reference-0", (1, 0, 0, WAITING, 0)): 0.5,
        ("reference-1", (1, 1, 0, WAITING, 0)): 0.5j,
        ("reference-2", (1, 2, 0, WAITING, 0)): -0.5,
        ("reference-3", (0, 6, 0, WAITING, 0)): -0.5j,
    }
    output = {
        (ref, compile_basis(branch, permutation, checkpoints, cap, calibration)): amplitude
        for (ref, branch), amplitude in state.items()
    }
    assert output == {
        ("reference-0", (1, 1, 0, WAITING, 0)): 0.5,
        ("reference-1", (1, 2, 0, WAITING, 0)): 0.5j,
        ("reference-2", (1, 0, 0, WAITING, 0)): -0.5,
        ("reference-3", (0, 6, 0, WAITING, 0)): -0.5j,
    }

    for target in checkpoints:
        induced_predecessor = next(
            value for value, (arrival, _) in expected.items() if arrival == target
        )
        immediate_predecessor = permutation.index(target)
        assert (permutation[induced_predecessor] == target) == (
            immediate_predecessor in checkpoints
        )
    assert permutation[0] != 1  # The induced predecessor of 1 returns via a detour.
    assert permutation[2] == 0  # This induced predecessor is also immediate.


def verify_all_small_instances():
    """Exhaust all permutations and nonempty checkpoint sets through six labels."""
    instances = 0
    branches = 0
    reversible_instances = 0
    for size in range(1, 7):
        labels = range(size)
        register_size = 1 << (size - 1).bit_length()
        for oracle in permutations(labels):
            padded_oracle = oracle + tuple(range(size, register_size))
            calibration = (size - 1, oracle[size - 1])
            for subset_size in range(1, size + 1):
                for subset in combinations(labels, subset_size):
                    checkpoints = set(subset)
                    expected = {
                        value: first_return(value, oracle, checkpoints)
                        for value in checkpoints
                    }
                    assert {arrival for arrival, _ in expected.values()} == checkpoints
                    cap = max(elapsed for _, elapsed in expected.values())
                    for known_cap in (cap, cap + 2):
                        for value, (arrival, elapsed) in expected.items():
                            scratch, rail_clock = timed_forward(
                                value,
                                (ACTIVE, 0),
                                padded_oracle,
                                checkpoints,
                                known_cap,
                                False,
                                calibration,
                            )
                            assert (scratch, rail_clock) == (arrival, (DONE, elapsed))
                            input_branch = (1, value, 0, WAITING, 0)
                            expected_branch = (1, arrival, 0, WAITING, 0)
                            assert compile_basis(
                                input_branch, padded_oracle, checkpoints, known_cap, calibration
                            ) == expected_branch
                            branches += 1
                    if size <= 4:
                        verify_global_bijection(padded_oracle, checkpoints, calibration)
                        reversible_instances += 1
                    instances += 1
    return instances, branches, reversible_instances


def verify_global_bijection(permutation, checkpoints, calibration):
    """Check the clean-calibration compiler on all data and working basis states."""
    cap = 3
    labels = range(len(permutation))
    states = set(product(range(2), labels, labels, range(4), range(4)))
    outputs = {
        compile_basis(state, permutation, checkpoints, cap, calibration) for state in states
    }
    assert outputs == states


def search_step(amplitudes, returned, target):
    """Apply the HRY iteration and project onto flag zero without rescaling."""
    size = len(returned)
    unmarked = [0.0] * size
    marked = [0.0] * size
    for source, amplitude in enumerate(amplitudes):
        arrival = returned[source]
        if arrival == target:
            marked[source] = amplitude
        else:
            unmarked[arrival] = amplitude

    plus = [(a + b) / sqrt(2) for a, b in zip(unmarked, marked)]
    minus = [(a - b) / sqrt(2) for a, b in zip(unmarked, marked)]
    twice_mean = 2 * sum(minus) / size
    minus = [twice_mean - amplitude for amplitude in minus]
    return [(a + b) / sqrt(2) for a, b in zip(plus, minus)]


def verify_search_probability(returned, target):
    """Compare the flag-resolved amplitudes with the proved rotation."""
    size = len(returned)
    predecessor = returned.index(target)
    if returned[target] == target:
        assert predecessor == target
        return 1.0

    angle = asin(1 / sqrt(size))
    rounds = round(pi / (2 * angle) - 1)
    amplitudes = [1 / sqrt(size)] * size
    for round_number in range(1, rounds + 1):
        amplitudes = search_step(amplitudes, returned, target)
        flag_survival = sum(amplitude**2 for amplitude in amplitudes)
        assert isclose(
            flag_survival, (1 - 1 / size) ** round_number, rel_tol=1e-12
        )

    probability = amplitudes[predecessor] ** 2
    closed_form = (1 - 1 / size) ** rounds * sin((rounds + 1) * angle) ** 2
    assert isclose(probability, closed_form, rel_tol=1e-12)
    assert probability > 1 / 3
    return probability


def verify_search():
    random = Random(20261118)
    cases = 0
    worst_probability = 1.0
    for size in range(2, 129):
        for _ in range(10):
            returned = list(range(size))
            random.shuffle(returned)
            target = random.randrange(size)
            probability = verify_search_probability(returned, target)
            worst_probability = min(worst_probability, probability)
            cases += 1
    return cases, worst_probability


def main():
    verify_unequal_return_example()
    instances, branches, reversible_instances = verify_all_small_instances()
    search_cases, worst_probability = verify_search()
    print("Unequal-return coherent example and predecessor checks passed.")
    print(f"{instances:,} exhaustive permutation and checkpoint-set instances.")
    print(f"{branches:,} promised basis branches checked with two caps.")
    print(f"{reversible_instances:,} full-basis compiler bijectivity checks.")
    print(f"{search_cases:,} search simulations, minimum success {worst_probability:.6f}.")


if __name__ == "__main__":
    main()

