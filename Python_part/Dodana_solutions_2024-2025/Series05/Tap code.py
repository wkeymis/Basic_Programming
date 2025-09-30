def encode_letter(letter):
    letter = letter.upper()
    if letter == 'K':
        letter = 'C'

    pos = ord(letter) - ord('A')
    if ord(letter) > ord('K'):
        pos -= 1

    row = (pos // 5) + 1
    col = (pos % 5) + 1

    return (row, col)


def decode_letter(row, col):
    pos = (row - 1) * 5 + (col - 1)
    letter = chr(65 + pos)

    if letter >= 'K':
        letter = chr(ord(letter) + 1)
    if letter == 'K':
        letter = 'C'

    return letter


def encode(word):
    result = []
    for letter in word:
        row, col = encode_letter(letter)
        row_dots = '.' * row
        col_dots = '.' * col
        result.append(f"{row_dots} {col_dots}")

    return ' '.join(result)


def decode(message):
    result = []
    parts = [p for p in message.split() if p]

    # Process pairs of dot patterns
    for i in range(0, len(parts), 2):
        row = len(parts[i])
        col = len(parts[i + 1])
        result.append(decode_letter(row, col))

    return ''.join(result)
