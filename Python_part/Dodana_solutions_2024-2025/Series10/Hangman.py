class Hangman:
    def __init__(self, word, chances=6):
        self.word = word
        self.chances = chances
        self.guessed_letters = set()
        self.current_state = ['.' for _ in word]

    def guessLetter(self, letter):
        if self.chances == 0 or '.' not in self.current_state:
            print("Sorry, the game is over.")
            return

        assert isinstance(letter, str) and len(letter) == 1 and letter.isalpha(), "argument is not a letter"
        letter = letter.lower()

        if letter in self.guessed_letters:
            raise AssertionError("letter has already been guessed")

        self.guessed_letters.add(letter)

        if letter in self.word.lower():
            occurrences = 0
            for i, char in enumerate(self.word):
                if char.lower() == letter:
                    self.current_state[i] = char
                    occurrences += 1
            print(f"Correct: letter {letter} occurs {occurrences} times in the word.")
            if '.' not in self.current_state:
                print("Congratulations! You have guessed the word!")
                print(''.join(self.current_state))
            else:
                print(f"You have {self.chances} more chances.")
                print(''.join(self.current_state))

        else:
            self.chances -= 1
            if self.chances == 0:
                print(f"Wrong: letter {letter} does not occur in the word.")
                print("Oops, you have been hung.")
                print(self.word)
            elif self.chances == 1:
                print(f"Wrong: letter {letter} does not occur in the word.")
                print(f"You have {self.chances} more chance.")
                print(''.join(self.current_state))

            else:
                print(f"Wrong: letter {letter} does not occur in the word.")
                print(f"You have {self.chances} more chances.")
                print(''.join(self.current_state))

    def __str__(self):
        if '.' not in self.current_state:
            return f"Congratulations! You have guessed the word!\n{''.join(self.current_state)}"
        if self.chances == 0:
            return f"Oops, you have been hung.\n{self.word}"
        return f"You have {self.chances} more chances.\n{''.join(self.current_state)}"

