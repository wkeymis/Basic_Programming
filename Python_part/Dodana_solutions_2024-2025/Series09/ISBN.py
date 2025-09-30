def isISBN13(code):
    if not (
        isinstance(code,str) and
        len(code) == 13 and
        code.isdigit()
    ):
        return False

    if code[:3] not in {'978','979'}:
        return False

    checkdigit = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
    checkdigit = (10 - checkdigit % 10) % 10
    return checkdigit == int(code[-1])

def remove_tags(s):

    s = s.strip()
    while s.find('<') >= 0:
        start = s.find('<')
        stop = s.find('>')
        if stop == -1:
            stop == len(s)
        s = s[:start] + s[stop+1:]
    return s.strip()

def display_book_info(code):
    if not isISBN13(code):
        print('Wrong ISBN-13 code')

    else:
        import urllib.request
        url = 'https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn=97801361106753'
        parameters = '?value1=' + code.strip()
        info = urllib.request.urlopen(url + parameters)

        for line in info:
            line = line.decode('utf-8')
            if line.startswith('<Title>'):
                print('Title: {}'.format(remove_tags(line)))
            elif line.startswith('<AuthorsText>'):
                print('Authors: {}'.format(remove_tags(line).rstrip(', ')))
            elif line.startswith('<PublisherText '):
                print('Publisher: {}'.format(remove_tags(line)))

        info.close()

