x = float(input())
y = float(input())

if 2.2 < x <= 4 and 0 < y <= 2:
    color = "blue"
elif 6.3 < x and 0 < y < 2.6:
    color = "yellow"
elif 6.3 < x and 4.1 < y <= 6:
    color = "blue"
elif 0 < x < 4.65 and 6 < y:
    color = "red"
else:
    color = "white"

print(color)