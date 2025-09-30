def motifs(sequence, subsequence, begin=0, end=None):
    if end is None:
        end = len(sequence)

    positions = []
    index = sequence.find(subsequence, begin, end)

    while index != -1:
        positions.append(index)
        index = sequence.find(subsequence, index + 1, end)

    return positions
