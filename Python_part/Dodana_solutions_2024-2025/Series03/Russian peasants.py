a = int(input())
b = int(input())

original_a = a
original_b = b

results = []
sum_of_selected = 0

while b > 0:
    results.append((a, b))
    if b % 2 != 0:
        sum_of_selected += a
    a *= 2
    b //= 2

for row in results:
    print(row[0], row[1])

print(sum_of_selected)
