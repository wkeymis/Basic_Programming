class Heater:
    def __init__(self, name, temperature=10.0, minimum=0.0, maximum=100.0):
        self.name = name
        self.current_temperature = round(float(temperature), 1)
        self.minimum_temperature = round(float(minimum), 1)
        self.maximum_temperature = round(float(maximum), 1)

    def __str__(self):
        return (f"{self.name}: current temperature: {self.current_temperature:.1f}; "
                f"allowed min: {self.minimum_temperature:.1f}; "
                f"allowed max: {self.maximum_temperature:.1f}")

    def __repr__(self):
        return (f"Heater('{self.name}', {self.current_temperature:.1f}, "
                f"{self.minimum_temperature:.1f}, {self.maximum_temperature:.1f})")

    def change_temperature(self, delta):
        new_temperature = self.current_temperature + delta
        if new_temperature < self.minimum_temperature:
            self.current_temperature = self.minimum_temperature
        elif new_temperature > self.maximum_temperature:
            self.current_temperature = self.maximum_temperature
        else:
            self.current_temperature = round(new_temperature, 1)

    def temperature(self):
        return self.current_temperature

