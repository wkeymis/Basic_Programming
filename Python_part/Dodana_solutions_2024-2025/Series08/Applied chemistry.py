def isvalid(symbol, name, length=None):
    if length is not None and len(symbol) != length:
        return False

    if not symbol[0].isupper() or not all(c.islower() for c in symbol[1:]):
        return False

    name_lower = name.lower()
    pos = -1

    for i, char in enumerate(symbol.lower()):
        new_pos = name_lower.find(char, pos + 1)
        if new_pos == -1:
            return False
        pos = new_pos

    return True

def symbols(name):
    name_lower = name.lower()
    result = set()

    for i, first_char in enumerate(name_lower):
        for j in range(i + 1, len(name_lower)):
            second_char = name_lower[j]
            symbol = first_char.upper() + second_char.lower()
            result.add(symbol)

    return result

def preference(name, last=False):
    all_symbols = sorted(symbols(name))
    return all_symbols[-1] if last else all_symbols[0]
