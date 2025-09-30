code = input()

while code != "stop":
    check = int(code[0])
    for i in range(2,10):
        x = int(code[i-1])
        check += i * x
    check %= 11

    x10 = code[9]

    if (check == 10 and x10 == "X") or x10 == str(check):
        print("OK")
    else:
        print("WRONG")
    code = input()