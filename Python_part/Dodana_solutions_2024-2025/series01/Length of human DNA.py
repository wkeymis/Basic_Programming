Basepairs_p_cel = float(input())
length_basepair = float(input())
numeber_cells = float(input())

length_meter = Basepairs_p_cel * length_basepair * numeber_cells * 1e-9

print(length_meter)

length_AU = length_meter / 149597870691

print(length_AU)

length_round_trips = length_AU / 2

print(length_round_trips)