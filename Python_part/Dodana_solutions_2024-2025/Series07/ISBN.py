def isISBN10(code):
    if not isinstance(code,str):
        return False

    if len(code) != 10:
        return False

    if not code[:9].isdigit():
        return False


    checkdigit = sum((i + 1) * int(code[i]) for i in range(9)) % 11

    x10 = code[9]

    return (checkdigit == 10 and x10 == 'X') or x10 == str(checkdigit)

def isISBN13(code):
    if not isinstance(code,str):
        return False

    if len(code) != 13:
        return False

    if not code.isdigit():
        return False

    checkdigit = 0
    for i in range(12):
        if i%2:
            checkdigit += 3 * int(code[i])
        else:
            checkdigit += int(code[i])
    checkdigit = (10 - checkdigit % 10) % 10
    return checkdigit == int(code[-1])
def isISBN(code, isbn13=True):
    if isbn13:
        return isISBN13(code)
    else:
        return isISBN10(code)

def areISBN(codes, isbn13=None):
    evaluations = []

    for code in codes:
        if isinstance(code,str):
            if isbn13 is None:
                if len(code) == 13:
                    evaluations.append(isISBN(code,True))
                else:
                    evaluations.append(isISBN(code,False))
            else:
                evaluations.append(isISBN(code,isbn13))
        else:
            evaluations.append(False)
    return evaluations
