n = int(input())
for i in range(n):
    word = input()
    counter = 0
    for j in word:
        if j == "," or j == "." or j == "_":
            print(f"{word} is not pure!")
            break
        counter += 1
    if len(word) == counter:
        print(f"{word} is pure.")
