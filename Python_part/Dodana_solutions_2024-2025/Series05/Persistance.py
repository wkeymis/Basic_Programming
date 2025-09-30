def multiplication(n):
    product = 1
    for digit in str(abs(n)):
        product *= int(digit)
    return product

def digital_root(n):
    while n >= 10:
        n = multiplication(n)
    return n

def persistence(n):
    count = 0
    while n >= 10:
        n = multiplication(n)
        count += 1
    return count

def most_persistent(a, b):
    max_persistence = -1
    result = a
    for num in range(a, b + 1):
        current_persistence = persistence(num)
        if (current_persistence > max_persistence or
                (current_persistence == max_persistence and num < result)):
            max_persistence = current_persistence
            result = num
    return result
