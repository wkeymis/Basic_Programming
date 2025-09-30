def crossoverpoints(chromosome1, chromosome2):
    i, j = 0, 0
    crossover_count = 0

    while i < len(chromosome1) and j < len(chromosome2):
        if chromosome1[i] == chromosome2[j]:
            crossover_count += 1
            i += 1
            j += 1
        elif chromosome1[i] < chromosome2[j]:
            i += 1
        else:
            j += 1

    return crossover_count

def maximalSum(chromosome1, chromosome2):
    i, j = 0, 0
    total_sum = 0
    sum1, sum2 = 0, 0

    while i < len(chromosome1) and j < len(chromosome2):
        if chromosome1[i] == chromosome2[j]:
            total_sum += max(sum1, sum2) + chromosome1[i]
            sum1, sum2 = 0, 0
            i += 1
            j += 1
        elif chromosome1[i] < chromosome2[j]:
            sum1 += chromosome1[i]
            i += 1
        else:
            sum2 += chromosome2[j]
            j += 1

    total_sum += max(sum1 + sum(chromosome1[i:]), sum2 + sum(chromosome2[j:]))

    return total_sum

