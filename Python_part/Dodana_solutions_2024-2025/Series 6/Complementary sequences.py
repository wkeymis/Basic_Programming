from typing import List, Tuple, Union

Sequence = Union[List[int], Tuple[int, ...]]

def isincreasing(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            return False
    return True

def frequency_sequence(sequence):
    if not isincreasing(sequence):
        raise ValueError("The given sequence is not increasing.")

    max_value = sequence[-1]
    freq_seq = []

    for i in range(1, max_value + 2):
        count = 0
        for x in sequence:
            if x < i:
                count += 1
        freq_seq.append(count)

    return freq_seq

def lift(sequence):
    lifted = []
    for i in range(len(sequence)):
        new_value = sequence[i] + i + 1
        lifted.append(new_value)
    return lifted


def complementary_sequences(sequence):
    if not isincreasing(sequence):
        raise ValueError("The given sequence is not increasing.")

    lifted = lift(sequence)
    freq_lifted = lift(frequency_sequence(sequence))
    return lifted, freq_lifted
