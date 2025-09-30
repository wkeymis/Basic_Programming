import math

def euclidean_distance(pos1, pos2):

    return float(math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2))

def manhattan_distance(pos1, pos2):
    return float(abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))

def chessboard_distance(pos1, pos2):

    return float(max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])))

def herd(file_path):

    antelopes = {}
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    rows, cols = len(grid), len(grid[0])
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char.isupper():
                antelopes[(r, c)] = char
    return rows, cols, antelopes

def nearest_antelope(position, antelopes, distance=euclidean_distance):
    min_distance = float('inf')
    closest = set()
    for ant_pos, label in antelopes.items():
        dist = distance(position, ant_pos)
        if dist < min_distance:
            min_distance = dist
            closest = {label}
        elif dist == min_distance:
            closest.add(label)
    return closest

def regions(file_path, distance=euclidean_distance):

    rows, cols, antelopes = herd(file_path)
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if (r, c) in antelopes:
                grid[r][c] = antelopes[(r, c)]
            else:
                nearest = nearest_antelope((r, c), antelopes, distance=distance)
                grid[r][c] = min(nearest).lower()
    return '\n'.join(''.join(row) for row in grid)
