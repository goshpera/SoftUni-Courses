text = input().split()

for word in text:
    reversed_word = word[::-1]
    print(f"{word} -> {reversed_word}")

