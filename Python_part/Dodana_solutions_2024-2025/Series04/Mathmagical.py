m = int(input())
num_str = str(m)
n = len(num_str)

numbers = []
for i in range(n):
    new_num = num_str[:i] + num_str[i + 1:]
    numbers.append(int(new_num))

total = sum(numbers)

width = n + 1

for i in range(len(numbers) - 1):
    print(f"{numbers[i]:>{width}}")

print(f"+{numbers[-1]:>{width-1}}")

print("=" * width)

print(f"{total:>{width}}")
