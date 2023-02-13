n = int(input())

for num in range(1, 1+n):
    is_special = False
    sum_digits = 0
    digit = num

    while digit:
        last_num = digit % 10
        sum_digits += last_num
        digit = int(digit/10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True
    print(f"{num} -> {is_special}")

