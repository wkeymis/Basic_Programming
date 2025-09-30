word = input().strip().upper()
start_letter = input().strip().upper()

start_ord = ord(start_letter)
first_ord = ord(word[0])
shift = (start_ord - first_ord) % 26

evolved_word = ""
output = ""

for char in word:
    original_ord = ord(char)
    evolved_ord = (original_ord - ord('A') + shift) % 26 + ord('A')
    evolved_char = chr(evolved_ord)
    evolved_word += evolved_char

    evolution = ""
    current_ord = original_ord
    while current_ord != evolved_ord:
        current_ord = (current_ord - ord('A') + 1) % 26 + ord('A')
        evolution += chr(current_ord).lower()
        if current_ord == original_ord:
            break

    output += f"{char}{evolution[:-1]}{evolved_char}\n"

print(output.strip())
