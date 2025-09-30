def isISBN(code):
    if not isinstance(code, str):
        return False

    groups = code.split('-')
    if tuple(len(e) for e in groups) != (1,4,4,1):
        return False
    code = ''.join(groups)

    if not code[:-1].isdigit():
        return False

    return checkdigit(code)  == code[-1]

def checkdigit(code):
    check = int(code[0])
    for i in range(2,10):
        x = int(code[i-1])
        check += i * x
    check %= 11

    return 'X' if check == 10 else str(check)
