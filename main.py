
def rev(string):
    words = string.split()
    reversed_words = []
    for word in words:
        symbol = {}
        letters = []
        for i in range(len(word)):
            if not word[i].isalpha():
                symbol[i] = word[i]
            else:
                letters.append(word[i])
        reversed_word = letters[::-1]
        for key, value in symbol.items():
            reversed_word = "".join(reversed_word)
            reversed_word = reversed_word[:key] + value + reversed_word[key:]
        reversed_words.append("".join(reversed_word))
    return " ".join(reversed_words)


if __name__ == '__main__':
    cases = [

        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),

    ]
    for text, reversed_text in cases:
        assert rev(text) == reversed_text
