n = int(input())
start = 97

for first in range(start, start+2):
    for second in range(start, start+2):
        for third in range(start, start+2):
            print(f"{chr(first)}{chr(second)}{chr(third)}")
        