words = input().split()
my_dict = {}

for word in words:
    for char in word:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

for key, val in my_dict.items():
    print(f"{key} -> {val}")
