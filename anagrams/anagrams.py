
def string_reverse(string):
    try:
        words = string.split()
    except AttributeError:
        raise AttributeError("Parameter must be a string!")
    reversed_words = []
    for word in words:
        reversed_word = []
        letters = []
        for char in word:
            if char.isalpha():
                letters.append(char)
        for char in word:
            if char.isalpha():
                reversed_word.append(letters.pop())
            else:
                reversed_word.append(char)
        reversed_words.append(''.join(reversed_word))

    return " ".join(reversed_words)
