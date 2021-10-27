
def string_reverse(string):
    words = string.split()
    reversed_words = []
    for word in words:
        reversed_word=[]
        letters=[]
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
