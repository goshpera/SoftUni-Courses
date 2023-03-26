nums = input().split(" ")
rounded_nums_str = []
rounded_nums = []

for i in nums:
    rounded_nums_str.append(float(i))

round_list = [round(num) for num in rounded_nums_str]
print(round_list)
