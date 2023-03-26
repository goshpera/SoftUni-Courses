elements = input().split()
bakery = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    values = int(elements[i+1])
    bakery[key] = values

print(bakery)
