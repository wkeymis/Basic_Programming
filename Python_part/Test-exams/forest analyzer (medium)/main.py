class ForestAnalyzer:
    def __init__(self, filename):
        self.image = []

        with open(filename, "r") as file:
            for line in file:
                cells = line.strip().split()
                row = []
                for cell in cells:
                    part = cell.split(",")
                    r = int(part[0])
                    g = int(part[1])
                    b = int(part[2])
                    row.append([r,g,b])
                self.image.append(row)

    def is_dominantly_green(self):
        green_count = 0
        total_pixels = len(self.image) * len(self.image[0])

        for row in self.image:
            for r,g,b in row:
                if g > r and g > b:
                    green_count += 1
        return green_count > (0.6 * total_pixels)

    def is_fire_detected(self):
        rows, cols = len(self.image), len(self.image[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                red_count = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        r, g, b= self.image[x][y]
                        if r >= 200 and r > g and r > b:
                            red_count += 1
                if red_count >= 9:
                    return True
        return False

class Drone:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze_and_act(self):
        if self.analyzer.is_fire_detected():
            return "Alert: fire!!"
        elif self.analyzer.is_dominantly_green():
            return "All clear"
        else:
            return "Investigate further"

if __name__ == "__main__":
    analyzer1 = ForestAnalyzer("forest_fire.csv")
    drone = Drone(analyzer1)
    print(drone.analyze_and_act())
    analyzer2 = ForestAnalyzer("forest_green.csv")
    drone2  = Drone(analyzer2)
    print(drone2.analyze_and_act())
    analyzer3 = ForestAnalyzer("forest_mixed.csv")
    drone3 = Drone(analyzer3)
    print(drone3.analyze_and_act())