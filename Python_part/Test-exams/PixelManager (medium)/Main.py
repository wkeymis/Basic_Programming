class PixelManager:
    def __init__(self, filename):
        self.samples = {}
        current_sample = None

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("Sample:"):
                    current_sample = line.split(":", 1)[1].strip()
                    self.samples[current_sample] = []
                    continue

                if current_sample:
                    row = []
                    cells = line.split()
                    for cell in cells:
                        r, g, b = map(int, cell.split(","))
                        row.append((r, g, b))
                    self.samples[current_sample].append(row)


    def average_brightness(self, sample_name):
        total, count = 0, 0
        for row in self.samples[sample_name]:
            for r, g, b in row:
                total += (r + g + b) / 3
                count += 1
        return total / count if count else 0

    def dominant_color(self, sample_name):
        total_r = total_g = total_b = 0
        for row in self.samples[sample_name]:
            for r, g, b in row:
                total_r += r
                total_g += g
                total_b += b
        if total_r >= total_g and total_r >= total_b:
            return "Red"
        elif total_g >= total_r and total_g >= total_b:
            return "Green"
        else:
            return "Blue"

    def color_histogram(self, sample_name):
        hist = {"Red": 0, "Green": 0, "Blue": 0}
        for row in self.samples[sample_name]:
            for r, g, b in row:
                hist["Red"] += r
                hist["Green"] += g
                hist["Blue"] += b
        return hist


    def invert_colors(self, sample_name):
        inverted = []
        for row in self.samples[sample_name]:
            inverted_row = []
            for r, g, b in row:
                inverted_row.append((255 - r, 255 - g, 255 - b))
            inverted.append(inverted_row)
        return inverted

    def threshold(self, sample_name, cutoff=128):
        binary = []
        for row in self.samples[sample_name]:
            binary_row = []
            for r, g, b in row:
                brightness = (r + g + b) / 3
                binary_row.append(1 if brightness >= cutoff else 0)
            binary.append(binary_row)
        return binary

    def grayscale(self, sample_name):
        gray = []
        for row in self.samples[sample_name]:
            gray_row = []
            for r, g, b in row:
                val = (r + g + b) // 3
                gray_row.append((val, val, val))
            gray.append(gray_row)
        return gray


    def is_uniform(self, sample_name, tolerance=10):
        first = self.samples[sample_name][0][0]
        for row in self.samples[sample_name]:
            for r, g, b in row:
                if abs(r - first[0]) > tolerance or abs(g - first[1]) > tolerance or abs(b - first[2]) > tolerance:
                    return False
        return True

    def brightest_pixel(self, sample_name):
        max_brightness = -1
        coords = (-1, -1)
        for i, row in enumerate(self.samples[sample_name]):
            for j, (r, g, b) in enumerate(row):
                brightness = (r + g + b) / 3
                if brightness > max_brightness:
                    max_brightness = brightness
                    coords = (i, j)
        return coords, max_brightness

    def compare_samples(self, sample1, sample2):
        avg1 = self.average_brightness(sample1)
        avg2 = self.average_brightness(sample2)
        return avg1 - avg2


    def colony_area(self, sample_name, threshold=128):
        """Count pixels above threshold (brighter → colony area)."""
        count = 0
        for row in self.samples[sample_name]:
            for r, g, b in row:
                if (r + g + b) / 3 >= threshold:
                    count += 1
        return count

    def average_fluorescence(self, sample_name):
        return self.average_brightness(sample_name)

    def compare_expression(self, sample1, sample2):
        f1 = self.average_brightness(sample1)
        f2 = self.average_brightness(sample2)
        return f1 / f2 if f2 != 0 else float("inf")
