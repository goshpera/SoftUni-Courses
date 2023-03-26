num = int(input())
word_dictionary = {}
list_synonyms = []

for i in range(num):
    word = input()
    synonym = input()

    list_synonyms.append(synonym)
    word_dictionary[word] = list_synonyms


for word in word_dictionary:
    print(f"{word} - {', '.join(list_synonyms)}")
