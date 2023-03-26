elements = input().split()
ascii_elements = {}

for i in range(0, len(elements)):
    key = elements[i]
    values = ord(key)
    ascii_elements[key] = values

print(ascii_elements)
