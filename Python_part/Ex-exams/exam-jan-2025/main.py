class ImageAnalyzer:
    def __init__(self, filename):
        self.image = []

        with open(filename, "r") as file:
            for line in file:
                cells = line.strip().split()
                pixel_row = []

                for cell in cells:
                    parts = cell.split(",")
                    r = int(parts[0])
                    g = int(parts[1])
                    b = int(parts[2])
                    pixel_row.append([r,g,b])
                self.image.append(pixel_row)

    def is_dominantly_blue(self):
        blue_count = 0

        total_pixels = len(self.image) * len(self.image[0])
        for row in self.image:
            for pixel in row:
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if b > r and b > g:
                    blue_count += 1
        return blue_count > (total_pixels/2)

    def is_red_square(self, row, col):
        if row + 1 >= len(self.image) or col + 1 >= len(self.image[0]):
            return False

        red_count = 0
        for i in range(row, row + 2):
            for j in range(col, col + 2):
                pixel = self.image[i][j]
                r_val = pixel[0]
                g_val = pixel[1]
                b_val = pixel[2]

                if r_val >= 150 and r_val > b_val and r_val > 2 * g_val:
                    red_count += 1
        return red_count == 4

    def contains_ripe_apple(self):
        for row in range(len(self.image) - 1):
            for col in range(len(self.image[0]) - 1):
                if self.is_red_square(row, col):
                    return True
        return False

class Drone:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze_and_act(self):
        if self.analyzer.is_dominantly_blue():
            return "Descend"
        elif self.analyzer.contains_ripe_apple():
            return "Pick apple"
        else:
            return "Forward"


analyzer = ImageAnalyzer("sample_image.csv")
drone = Drone(analyzer)
print(drone.analyze_and_act())
print(drone)

