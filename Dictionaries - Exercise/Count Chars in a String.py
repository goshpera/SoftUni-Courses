str = input()
str_dict = {}

for char in str:
    if char not in str_dict:
        str_dict[char] = 1
    else:
        str_dict[char] += 1

for key, value in str_dict.items():
    print(f"{key} -> {value}")
