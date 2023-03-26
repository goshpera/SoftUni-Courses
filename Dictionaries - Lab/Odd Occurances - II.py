words_keys = [el.lower() for el in input().split()]
default = 0

occurances = dict.fromkeys(words_keys, default)
for word in words_keys:
    occurances[word] += 1

for word, count in occurances.items():
    if count % 2 != 0:
        print(word, end=" ")
