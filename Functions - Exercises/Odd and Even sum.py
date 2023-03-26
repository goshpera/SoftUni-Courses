def get_sum(digits_as_str):
    even_sum = 0
    odd_sum = 0

    for digit_as_str in digits_as_str:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

        return even_sum, odd_sum


num_as_str = input()
result = get_sum(num_as_str)
print(f"Odd sum = {result[1]}, Even sum = {result[0]} ")
