def serial_number(s):
    if isinstance(s, int):
        s = str(s)

    if not (isinstance(s, str) and s.isdigit() and int(s) > 0):
        raise AssertionError("invalid serial number")

    return s.zfill(8)

def solid(s):
    s = serial_number(s)
    return len(set(s)) == 1

def radar(s):
    s = serial_number(s)
    return s == s[::-1] and not solid(s)

def repeater(s):
    s = serial_number(s)
    half = len(s) // 2
    return len(s) % 2 == 0 and s[:half] == s[half:] and not solid(s)

def radar_repeater(s):
    return radar(s) and repeater(s)

def numismatist(serials, kind=solid):
    result = []
    for s in serials:
        if kind(s):
            result.append(s)
    return result
