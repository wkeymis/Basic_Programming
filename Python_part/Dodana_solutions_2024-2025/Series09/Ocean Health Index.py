def mean(numbers):
    valid_numbers = []
    for n in numbers:
        if n is not None:
            valid_numbers.append(n)

    if len(valid_numbers) == 0:
        return None

    return sum(valid_numbers) / len(valid_numbers)

def database(file_path):
    result = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            state_name = parts[1]

            scores = []
            for x in parts[2:]:
                if x.isdigit():
                    scores.append(int(x))
                else:
                    scores.append(None)

            result[state_name] = scores

    return result

def oceanHealthIndex(state, data):
    if state not in data:
        return None

    scores = data[state]
    if len(scores) < 13:
        return None

    le = mean(scores[:2])
    sp = mean(scores[2:4])
    bd = mean(scores[10:12])

    subgoals = [le, sp, bd] + [scores[i] for i in range(4, 10) if scores[i] is not None] + ([scores[12]] if scores[12] is not None else [])
    ohi = mean(subgoals)

    if ohi is None:
        return None
    return round(ohi)
