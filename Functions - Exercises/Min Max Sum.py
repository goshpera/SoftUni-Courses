def max_num(num):
    result = max(num)
    return result


def min_num(num):
    result = min(num)
    return result


def sum_nums(num):
    result = sum(num)
    return result


nums = [int(x) for x in input().split(" ")]
print(f"The minimum number is {min_num(nums)}")
print(f"The maximum number is {max_num(nums)}")
print(f"The sum number is: {sum_nums(nums)}")
