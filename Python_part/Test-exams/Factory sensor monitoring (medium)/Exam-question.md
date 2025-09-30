# Question

### Factory Sensor Monitoring

You are given a text file containing sensor readings from a factory.  
Each line has the format:

`<date> <time> temperature:<value> humidity:<value> vibration:<value>`


---

## Your Task

Design two Python classes:

### 1. `SensorAnalyzer`
This class should:
- Read the sensor data from the file and store it in a structured format.  
- Provide the following methods:
  - `average_temperature()`: Returns the average temperature across all readings.  
  - `max_vibration()`: Returns the maximum vibration value and the corresponding timestamp.  
  - `high_humidity_hours(threshold)`: Returns a list of timestamps where humidity exceeds the given threshold.  

### 2. `FactoryAlert`
This class should:
- Be initialized with a `SensorAnalyzer` object.  
- Provide a method `Analyze_and_alert()` that:
  - Returns `"ALERT: high vibration detected"` if the maximum vibration exceeds `0.15`.  
  - Returns `"ALERT: High humidity detected"` if any humidity readings exceed `60`.  
  - Returns `"All conditions are normal"` otherwise.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the provided `sensors.txt` file.  
3. Print:
   - Average temperature  
   - Maximum vibration and corresponding time  
   - Hours with humidity > 60%  
   - Final alert status  

---
