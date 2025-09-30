import math

def read_meteo(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    temperature = list(map(float, lines[1].strip().split('\t')))
    humidity = list(map(float, lines[2].strip().split('\t')))

    return {'temperature': temperature, 'humidity': humidity}

def wet_bulb(data):
    T = data['temperature']
    RH = data['humidity']

    if any(t < -20 or t > 50 for t in T) or any(rh < 0 or rh > 100 for rh in RH):
        return -9999

    wet_bulb_temps = []

    for t, rh in zip(T, RH):
        Tnat = (
            t * math.atan(0.151977 * math.sqrt(rh + 8.313659)) +
            math.atan(t + rh) -
            math.atan(rh - 1.676331) +
            0.00391838 * math.pow(rh, 1.5) * math.atan(0.023101 * rh) - 4.686035
        )

        wet_bulb_temps.append(Tnat)

    return wet_bulb_temps

def alert(wet_bulb_temps):
    if wet_bulb_temps == -9999:
        return 'Invalid data'

    max_temp = max(wet_bulb_temps)
    if max_temp < 32:
        return 'green'
    elif 32 <= max_temp < 35:
        return 'yellow'
    else:
        return 'red'

file_name = 'predictions.txt'
data = read_meteo(file_name)
wet_bulb_temps = wet_bulb(data)
alert_level = alert(wet_bulb_temps)

print("Wet Bulb Temperatures:", wet_bulb_temps)
print("Alert Level:", alert_level)
