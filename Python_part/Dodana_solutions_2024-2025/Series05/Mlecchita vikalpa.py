def iskey(part1: str, part2: str) -> bool:
    combined = part1 + part2

    if len(part1) != 13 or len(part2) != 13:
        return False

    for character in combined:
        if not character.isalpha():
            return False

    unique_letters = set()
    for character in combined.lower():
        unique_letters.add(character)

    if len(unique_letters) != 26:
        return False

    return True


def encode_character(char: str, part1: str, part2: str) -> str:
    if not char.isalpha():
        return char

    part1_lower = part1.lower()
    part2_lower = part2.lower()
    char_lower = char.lower()

    if char_lower in part1_lower:
        index = part1_lower.index(char_lower)
        encoded_char = part2_lower[index]
    else:
        index = part2_lower.index(char_lower)
        encoded_char = part1_lower[index]

    if char.isupper():
        return encoded_char.upper()
    else:
        return encoded_char


def encode(message: str, part1: str, part2: str) -> str:
    encoded_message = ""
    for char in message:
        encoded_message += encode_character(char, part1, part2)
    return encoded_message


def decode(message: str, part1: str, part2: str) -> str:
    decoded_message = ""
    for char in message:
        decoded_message += encode_character(char, part1, part2)
    return decoded_message
