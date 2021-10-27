
def string_reverse(string):
    words = string.split()
    reversed_words = []
    for word in words:
        symbol = {}
        letters = []
        for i, char in enumerate(word):
            if not char.isalpha():
                symbol[i] = char
            else:
                letters.append(char)
        reversed_word = letters[::-1]
        for key, value in symbol.items():
            reversed_word.insert(key, value)
        reversed_words.append(''.join(reversed_word))
    return " ".join(reversed_words)
