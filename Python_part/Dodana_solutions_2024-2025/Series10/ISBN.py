class ISBN13:
    def __init__(self, code, length=1):
        assert isinstance(code, int), 'invalid ISBN code'
        assert 1 <= length <= 5, 'invalid ISBN code'

        self.code = str(code)
        self.length = length
    def __str__(self):
        return '{}-{}-{}-{}'.format(
            self.code[:3],
            self.code[3:3 + self.length],
            self.code[3 + self.length:-1],
            self.code[-1]
        )

    def __repr__(self):
        return 'ISBN13({}, {})'.format(int(self.code), self.length)


    def isvalid(self):
        check = sum((3 if i % 2 else 1) * int(self.code[i]) for i in range(12))
        check = (10 - check % 10) % 10

        return self.code[12] == str(check)

    def asISBN10(self):
        if not self.isvalid() or str(self.code)[:3] != '978':
            return None

        code = self.code[3:-1]

        check = sum((i+1) * int(code[i]) for i in range(9)) % 11
        checkdigit = 'X' if check == 10 else str(check)
        return '{}-{}-{}'.format(
            code[:self.length],
            code[self.length:],
            checkdigit
        )


