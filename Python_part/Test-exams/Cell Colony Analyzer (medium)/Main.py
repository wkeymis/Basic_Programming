class ColonyAnalyser:
    def __init__(self, filename):
        self.grid = []

        with open(filename, "r") as file:
            for line in file:
                line.strip()

                row = []
                cells = line.split()

                for cell in cells:
                    r,g,b = cell.split(",")
                    r = int(r)
                    g = int(g)
                    b = int(b)
                    row.append([r,g,b])
                self.grid.append(row)

    def count_red_colonies(self, threshold = 50):
        count = 0
        for row in self.grid:
            for r,g,b in row:
                if r >= threshold and r > 2 * g and r > b:
                    count += 1
        return count

    def dominantly_color(self, color):
        total_pixels = len(self.grid) * len(self.grid[0])
        color_count = 0

        for row in self.grid:
            for r,g,b in row:
                if color == "red" and r>g and r>b:
                    color_count += 1
                elif color == "green" and g >r and g>b:
                    color_count += 1
                elif color == "blue" and b > r and b > g:
                    color_count += 1
        return color_count >= total_pixels/2

    def largest_red_block(self):
        rows = len(self.grid)
        col = len(self.grid[0])

        for r in range(rows - 1):
            for c in range(col - 1):
                red_count = 0
                for i in range(r, r+2):
                    for j in range(c, c + 2):
                        rr, gg, bb = self.grid[i][j]
                        if rr >= 150 and rr >= 2 * gg and rr > bb:
                            red_count += 1
                if red_count == 4:
                    return (r,c)
        return None

class ColonyReport:
    def __init__(self, analyzer):
        self.analyzer = analyzer
    def generate_report(self):
        total_red = self.analyzer.count_red_colonies()
        for color in ["red", "blue", "green"]:
            if self.analyzer.dominantly_color(color):
                dominant = color
                break
        block = self.analyzer.largest_red_block()



