text = input("Text: ")
texts = text.split()
WORD_TO_COUNT = {}

for word in texts:
    word =word.lower()
    WORD_TO_COUNT[word] = WORD_TO_COUNT.get(word, 0) + 1

max_word_length = max(len(word) for word in WORD_TO_COUNT.keys())
print("Text: ")
for word, count in sorted(WORD_TO_COUNT.items()):
    print(f"{word:<{max_word_length}}: {count}")