def reduce(key):
    seen = set()
    reduced_key = ""
    for char in key.upper():
        if char not in seen:
            seen.add(char)
            reduced_key += char
    return reduced_key

def encode(serial, key):
    reduced_key = reduce(key)
    if len(reduced_key) != 10:
        raise ValueError("Invalid key: must have 10 unique letters")

    mapping = {}
    for i in range(1, 10):
        digit_string = str(i)
        letter = reduced_key[i - 1]
        mapping[digit_string] = letter
    mapping['0'] = reduced_key[9]

    encoded_serial = ""
    for digit_char in str(serial):
        encoded_serial += mapping[digit_char]

    return encoded_serial

def decode(encoded, key):
    reduced_key = reduce(key)
    if len(reduced_key) != 10:
        raise ValueError("Invalid key: must have 10 unique letters")

    reverse_mapping = {}
    for i in range(1, 10):
        digit_string = str(i)
        letter = reduced_key[i - 1]
        reverse_mapping[letter] = digit_string
    reverse_mapping[reduced_key[9]] = '0'

    decoded_serial = ""
    for letter_char in encoded:
        decoded_serial += reverse_mapping[letter_char]

    return int(decoded_serial)

def next(encoded, key):
    current_serial = decode(encoded, key)
    next_serial = current_serial + 1
    return encode(next_serial, key)

