n = int(input())
numbers = []
filtered_nums = []

for i in range(n):
    current_num = int(input())
    numbers.append(current_num)
    command = input()

    if command == "positive":
        for number in numbers:
            if number >= 0:
                filtered_nums.append(number)
    if command == "negative":
        for number in numbers:
            if number < 0:
                filtered_nums.append(number)
    if command == "even":
        for number in numbers:
            if number % 2 == 0:
                filtered_nums.append(number)
    if command == "odd":
        for number in numbers:
            if number % 2 != 0:
                filtered_nums.append(number)
print(filtered_nums)
