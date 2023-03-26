def is_palindrome(nums):
    for num in range(len(nums)):
        reversed_second_half_str = ""
        if len(nums[num]) % 2 == 0:
            reversed_second_half_str = reversed(nums[num][len(nums[num]) // 2 : len(nums[num])])
        else:
            reversed_second_half_str = reversed(nums[num][(len(nums[num]) // 2 ) + 1 : len(nums[num])])
        for i in reversed_second_half_str:
            reversed_second_half_str += i

        first_half = nums[num][0 : len(nums[num]) // 2]

        if first_half == reversed_second_half_str:
            print(True)
        else:
            print(False)


palindrome = (input().split(", "))
print(is_palindrome(palindrome))

