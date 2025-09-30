def digit_count(s):
    counts = [0] * 10
    for char in s:
        if char.isdigit():
            counts[int(char)] += 1
    return tuple(counts)

def description(counts):
    result = []
    for digit, count in enumerate(counts):
        if count > 0:
            result.append(f"{count}{digit}")
        elif count == 0:
            result.append(f"{digit}")

    return " ".join(result)

def isselfinventorying(sequence):
    cumulative_counts = [0] * 10
    for i, s in enumerate(sequence):
        current_counts = digit_count(s)
        cumulative_counts = [x + y for x, y in zip(cumulative_counts, current_counts)]
        if description(cumulative_counts) != s:
            return False
    return True

def isselfinventorying_2(*args):
    return isselfinventorying(args)




