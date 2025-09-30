def next_letter(prefix, word):
    word = word.upper()
    prefix = prefix.upper()
    idx = word.find(prefix)
    if idx != -1 and idx + len(prefix) < len(word):
        if word.count(prefix) == 1:
            return word[idx + len(prefix)]
    return ''

def extend(ngram, words):
    profession = ngram.upper()
    for word in words:
        next_char = next_letter(profession[-(len(ngram) - 1):], word)
        if not next_char:
            return ''
        profession += next_char
    return profession

def profession(words, length=2):
    first_word = words[0].upper()
    for i in range(len(first_word) - length + 1):
        ngram = first_word[i:i + length]
        result = extend(ngram, words[1:])
        if result:
            return result
    return ''
