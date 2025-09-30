sep = input()
n = int(input())
encoded_lines = [input() for _ in range(n)]

decoded_lines = []

for line in encoded_lines:
    left, right = line.split(sep)
    decoded_lines.append(right + left)

for decoded_line in decoded_lines:
    print(decoded_line)