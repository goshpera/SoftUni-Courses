while True:
    word = ""
    command = input()
    if command == "SoftUni":
        continue
    if command == "End":
        break
    for i in command:
        word += i + i
    print(word)

