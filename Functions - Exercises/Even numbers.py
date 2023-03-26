digits_as_str = input().split(" ")
digits = [int(num) for num in digits_as_str]
even_nums = filter(lambda n: n % 2 == 0, digits)
print(list(even_nums))


#def is_even(num):
#    result = num % 2 == 0
#    return result


#nums = [int(x) for x in input().split(" ")]
#print(list(filter(is_even(), nums)))
