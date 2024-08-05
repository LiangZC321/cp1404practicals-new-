# text = input("Text: ")
# texts = text.split()
# WORD_TO_COUNT = {}
#
# for word in texts:
#     word =word.lower()
#     WORD_TO_COUNT[word] = WORD_TO_COUNT.get(word, 0) + 1
#
# max_word_length = max(len(word) for word in WORD_TO_COUNT.keys())
# print("Text: ")
# for word, count in sorted(WORD_TO_COUNT.items()):
#     print(f"{word:<{max_word_length}}: {count}")
word_to_count = {}
text = input("the text: ")
lengths_of_words = []
words = text.split()
for word in words:
    word = word.lower()
    word_to_count[word] = word_to_count.get(word, 0) + 1
    lengths_of_words.append(len(word))
length = max(lengths_of_words)
for word in word_to_count.keys():
    print(f"{word:{length}} : {word_to_count[word]}")
