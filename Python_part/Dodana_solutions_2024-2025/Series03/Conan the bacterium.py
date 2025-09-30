k = int(input())  # growth factor
m = int(input())  # additional cells due to radiation
t = int(input())  # seconds for the first experiment
n = int(input())  # initial cells for the second experiment

# Experiment 1
cells_1 = 1
for _ in range(t):
    cells_1 = cells_1 * k + m

# Experiment 2
cells_2 = n
seconds_2 = 0
while cells_2 < cells_1:
    cells_2 = cells_2 * k + m
    seconds_2 += 1

# Output the results
print(f"experiment #1: {cells_1} cells after {t} seconds")
print(f"experiment #2: {cells_2} cells after {seconds_2} seconds")

