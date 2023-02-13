n = int(input())
result = 0

for i in range(n):
    symbol = input()
    result += ord(symbol)

print(result)