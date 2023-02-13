n = int(input())
best_snowball = float('-inf')
output = ''

for i in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    formula = (weight//time_needed) ** quality
    if formula > best_snowball:
        best_snowball = formula
        output = f'{weight} : {time_needed} = {formula} {quality}'

print(output)