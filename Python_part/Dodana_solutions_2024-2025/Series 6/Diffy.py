from typing import List, Tuple, Union

Sequence = Union[List[int], Tuple[int, ...]]

def next(sequence: Sequence) -> Tuple[int, ...]:
    length = len(sequence)
    new_sequence = []

    for i in range(length):
        current = sequence[i]
        next_value = sequence[(i + 1) % length]
        difference = abs(current - next_value)
        new_sequence.append(difference)

    return tuple(new_sequence)

def ducci(sequence):
    seen = set()
    result = []
    current = tuple(sequence)

    while current not in seen and current != (0,) * len(current):
        seen.add(current)
        result.append(current)
        current = next(current)

    result.append(current)
    return tuple(result)

def period(sequence):
    seen = {}
    current = tuple(sequence)
    steps = 0

    while current not in seen:
        if current == (0,) * len(current):
            return 0
        seen[current] = steps
        steps += 1
        current = next(current)

    return steps - seen[current]
