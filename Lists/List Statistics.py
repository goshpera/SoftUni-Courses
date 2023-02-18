n = int(input())
positives = []
negatives = []

for i in range(n):
    num = int(input())

    if num >= 0:
        positives.append(num)
    if num < 0:
        negatives.append(num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}.")