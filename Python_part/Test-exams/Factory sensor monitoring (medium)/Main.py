class SensorAnalyzer:
    def __init__(self, filename):
        self.data = []

        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                timestamp = parts[0] + " " + parts[1]

                readings = {}
                for part in parts[2:]:
                    key, value = part.split(":")
                    readings[key] = float(value)

                self.data.append({
                    "time": timestamp,
                    "temperature": readings["temperature"],
                    "humidity": readings["humidity"],
                    "vibration": readings["vibration"]
                })
    def average_temperature(self):
        total = 0.0
        count = 0
        for entry in self.data:
            total += entry["temperature"]
            count += 1
        if count == 0:
            return 0.0
        return total/count

    def max_vibration(self):
        max_vibration_value = None
        max_time = None
        for entry in self.data:
            if max_vibration_value is None or entry["vibration"] > max_vibration_value:
                max_vibration_value = entry["vibration"]
                max_time = entry["time"]

            return max_vibration_value, max_time

    def high_humidity_hours(self, threshold):
        high_hours = []
        for entry in self.data:
            if entry["humidity"] > threshold:
                high_hours.append(entry["time"])
        return high_hours

class FactoryAlert:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def Analyze_and_alert(self):
        max_vib, _ = self.analyzer.max_vibration()
        if max_vib > 0.15:
            return "ALERT: high vibration detected"

        if self.analyzer.high_humidity_hours(60):
            return "ALERT: High humidity detected"
        return "All conditions are normal"

analyzer = SensorAnalyzer("sensors.txt")
alert = FactoryAlert(analyzer)

print("Average temperature:", analyzer.average_temperature())
vib, t = analyzer.max_vibration()
print(f"Maximum vibration: {vib} at {t}")
print("High humidity hours (>60%):", analyzer.high_humidity_hours(60))

print("Final status:", alert.Analyze_and_alert())