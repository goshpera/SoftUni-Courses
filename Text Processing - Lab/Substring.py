subtext = input()
text = input()

while subtext in text:
    text = text.replace(subtext, "")

print(text)
