temperatures = []
while True:
    line = input().strip()
    if line == "stop":
        break
    temperatures.append(float(line))

n = len(temperatures)

if n < 5:
    print("no heat wave")
else:
    heat_wave = False

    for i in range(n):
        window = []

        for j in range(i, n):
            if temperatures[j] >= 25:
                window.append(temperatures[j])
            else:
                break

        if len(window) >= 5:
            if sum(1 for temp in window if temp >= 30) >= 3:
                heat_wave = True
                break

    if heat_wave:
        print("heat wave")
    else:
        print("no heat wave")
