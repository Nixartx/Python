def rev(string):
    words = string.split()
    reversed_words = []
    for word in words:
        symbol = {}
        letters = []
        for i in range(len(word)):
            if not word[i].isalpha():
                symbol[i] = word[i]
                letters = word[:i] + word[(i + 1):]
        reversed_word = letters[::-1]
        for key, value in symbol.items():
            reversed_word = reversed_word[:key] + value + reversed_word[key:]
        reversed_words.append(reversed_word)
    return ' '.join(reversed_words)


if __name__ == '__main__':

    print(rev("a1bcd efg!h"))
