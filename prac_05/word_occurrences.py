text = input("Text: ")
texts = text.split()
WORD_TO_COUNT = {}

for word in texts:
    word =word.lower()
    WORD_TO_COUNT[word] = WORD_TO_COUNT.get(word, 0) + 1