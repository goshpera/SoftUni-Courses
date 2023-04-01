words = input().split()
final_string = ""

for word in words:
    final_string += word * len(word)

print(final_string)

"""
How to do it with comprehension:
result = [word * len(word) for word in words]
print(*result, sep='')
"""