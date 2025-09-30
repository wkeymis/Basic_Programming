def hydrophobicity(protein, kd):
    return [kd[aa] for aa in protein]


def filter(datapoints, weights):
    if not datapoints or not weights:
        return []

    width = len(weights)
    half_width = width // 2
    result = []

    for i in range(half_width, len(datapoints) - half_width):
        window = datapoints[i - half_width:i + half_width + 1]
        weighted_sum = sum(w * v for w, v in zip(weights, window))
        total_weight = sum(weights)
        result.append(round(weighted_sum / total_weight, 3))

    return result


def filterAverage(datapoints, width=5):
    if width % 2 == 0:
        width += 1

    weights = [1] * width
    return filter(datapoints, weights)


def filterTriangle(datapoints, width=5):
    if width % 2 == 0:
        width += 1

    mid = width // 2
    weights = []

    for i in range(1, mid + 2):
        weights.append(i)

    for i in range(mid, 0, -1):
        weights.append(i)

    return filter(datapoints, weights)

