word = input()
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]
    # print(word[index], end = '')
print(reversed_word)
