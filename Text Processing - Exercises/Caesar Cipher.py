text = input()

encrypted_text = ""
for ch in text:
    new_value = ord(ch) + 3
    encrypted_text += chr(new_value)

print(encrypted_text)


"""
Comprehension method for the exercise:

encrypted_text = ''.join([chr(ord(ch) + 3) for ch in text])
print(encrypted_text)
"""