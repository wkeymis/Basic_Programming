class Hexagon:
    OFFSETS = {
        'E': (1, 0),
        'SE': (0, 1),
        'SW': (-1, 1),
        'W': (-1, 0),
        'NW': (0, -1),
        'NE': (1, -1),
    }

    def __init__(self, q, r):
        self.q = q
        self.r = r

    def __str__(self):
        return f"({self.q}, {self.r})"

    def __repr__(self):
        return f"Hexagon({self.q}, {self.r})"

    def __eq__(self, other):
        if isinstance(other, Hexagon):
            return self.q == other.q and self.r == other.r
        return False

    def __hash__(self):
        return hash((self.q, self.r))

    def distance(self, other):
        dq = abs(self.q - other.q)
        dr = abs(self.r - other.r)
        ds = abs((-self.q - self.r) - (-other.q - other.r))
        return max(dq, dr, ds)

    def neighbor(self, direction):
        if direction not in self.OFFSETS:
            raise ValueError(f"Invalid direction: {direction}")
        dq, dr = self.OFFSETS[direction]
        return Hexagon(self.q + dq, self.r + dr)

    def path(self, directions):
        current = self
        i = 0
        while i < len(directions):
            if directions[i:i+2] in self.OFFSETS:
                direction = directions[i:i+2]
                i += 2
            else:
                direction = directions[i]
                i += 1

            current = current.neighbor(direction)
        return current

    def neighbors(self):
        return {self.neighbor(direction) for direction in self.OFFSETS}
