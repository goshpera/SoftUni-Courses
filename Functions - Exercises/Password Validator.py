n = int(input())

while n > 1:
    fact = n * (n-1)
    result += fact
    n -= 1

print(result)
