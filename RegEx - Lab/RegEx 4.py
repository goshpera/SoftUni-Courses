import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

results = re.finditer(pattern, text)

for res in results:
    print(res.group())
