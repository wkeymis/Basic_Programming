def isISBN(code):
    if not isinstance(code,str):
        return False

    if len(code) != 10:
        return False

    if not code[:9].isdigit():
        return False


    check = int(code[0])
    for i in range(2,10):
        x = int(code[i-1])
        check += i * x
    check %= 11

    x10 = code[9]

    return (check == 10 and x10 == 'X') or x10 == str(check)
