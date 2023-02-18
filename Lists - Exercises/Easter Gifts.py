gifts = input().split(" ")

while True:
    line = input()
    if line == "No Money":
        break

    command_args = line.split()
    command = command_args[0]
    gift = command_args[1]

    if command == "OutOfStock":
        gift_idx = -1
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gift_idx = idx
                break
        if gift_idx != -1:
            gifts[gift_idx] = "None"

    elif command == "Required":
        idx = int(command_args[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=" ")
    