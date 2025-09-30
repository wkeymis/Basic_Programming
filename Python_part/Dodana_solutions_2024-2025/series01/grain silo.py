import math
w = float(input())
l = float(input())
c = float(input())
r = float(input())
h = float(input())

hectares = (w * l) / 10000

total_harvest = hectares * c

surface = r * r * math.pi
volume = surface * h


silos = math.ceil(total_harvest / volume)

print(silos)

last_part = total_harvest % volume

if last_part == 0:
    height = h
else:
    height = last_part / surface


print(height)