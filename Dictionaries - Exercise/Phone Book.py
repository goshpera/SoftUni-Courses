phonebook = {}
n = 0

while True:
    line = input()
    data = line.split("-")
    if len(data) == 1:
        n = int(line)
        break
    name = data[0]
    number = data[1]
    phonebook[name] = number

for i in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
