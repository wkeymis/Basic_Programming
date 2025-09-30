def hit(n, occupied=None):
    if occupied is None:
        occupied = []

    points = 0
    new_occupied = []

    for base in sorted(occupied, reverse=True):
        new_base = base + n
        if new_base >= 4:
            points += 1
        else:
            new_occupied.append(new_base)

    if n > 0:
        if n >= 4:
            points += 1
        else:
            new_occupied.append(n)

    new_occupied.sort()
    return points, new_occupied
def inning(hits):

    points = 0
    occupied = []

    for n in hits:
        hit_points, occupied = hit(n, occupied)
        points += hit_points

    return points, occupied
