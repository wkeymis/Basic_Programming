def check(isbn):
    checksum = sum((i + 1) * isbn[i] for i in range(10))
    return checksum % 11 == 0

while True:
    isbn = []
    for l in range(10):
        line = input()
        if line == "stop":
            exit()
        isbn.append(int(line))
    if check(isbn):
        print("OK")
    else:
        print("WRONG")

