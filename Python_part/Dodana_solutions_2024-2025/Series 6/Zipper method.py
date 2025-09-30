from typing import List, Tuple, Union

Sequence = Union[List, Tuple]

def merge(seq1, seq2):
    result = []

    for pair in zip(seq1, seq2):
        for elem in pair:
            result.append(elem)

    return result

def weave(seq1, seq2):
    max_len = max(len(seq1), len(seq2))
    result = []
    for i in range(max_len):
        if i < len(seq1):
            result.append(seq1[i])
        else:
            result.append(seq1[i % len(seq1)])
        if i < len(seq2):
            result.append(seq2[i])
        else:
            result.append(seq2[i % len(seq2)])
    return result

def zipper(seq1, seq2):
    merged = []
    min_len = min(len(seq1), len(seq2))

    for i in range(min_len):
        merged.append(seq1[i])
        merged.append(seq2[i])

    for i in range(min_len, len(seq1)):
        merged.append(seq1[i])

    for i in range(min_len, len(seq2)):
        merged.append(seq2[i])

    return merged
