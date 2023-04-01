my_dict = {}

while True:
    line = input()
    if line == "stop":
        break
    quantity = int(input())

    if line not in my_dict:
        my_dict[line] = quantity
    else:
        my_dict[line] += quantity

for key, value in my_dict.items():
    print(f"{key} -> {value}")
