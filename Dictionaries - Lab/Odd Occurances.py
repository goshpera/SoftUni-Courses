words = input().split()
dictionary = {}

for word in words:
    lwrc_word = word.lower()
    if lwrc_word not in dictionary:
        dictionary[lwrc_word] = 0
    dictionary[lwrc_word] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
