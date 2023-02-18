numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):
    beggars_idx = idx % beggars_count
    num = int(numbers[idx])
    beggars[beggars_idx] += num

print(beggars)
