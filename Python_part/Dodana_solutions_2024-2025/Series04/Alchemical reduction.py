polymer = input().strip()

stack = []

for unit in polymer:
    if stack and stack[-1].swapcase() == unit:
        stack.pop()
    else:
        stack.append(unit)

result = ''.join(stack)
print(f"{result}({len(result)})")

