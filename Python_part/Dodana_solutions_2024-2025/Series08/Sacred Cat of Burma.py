def color(genotype):
    if 'C' in genotype[:2]:
        if 'D' in genotype[2:]:
            return 'seal'
        elif 'd' in genotype[2:]:
            return 'blue'
    elif 'c' in genotype[:2]:
        if 'D' in genotype[2:]:
            return 'chocolate'
        elif 'd' in genotype[2:]:
            return 'lilac'


def combinations(genotype):
    return [c + d for c in genotype[:2] for d in genotype[2:]]

def punnett(male, female, pprint=False):
    male_combinations = combinations(male)
    female_combinations = combinations(female)
    square = [[m[0] + f[0] + m[1] + f[1] for f in female_combinations] for m in male_combinations]

    if pprint:
        return '\n'.join([' '.join(row) for row in square])
    return square

def color_distribution(male, female):
    square = punnett(male, female)
    color_count = {}
    for row in square:
        for genotype in row:
            point_color = color(genotype)
            color_count[point_color] = color_count.get(point_color, 0) + 1
    return color_count
