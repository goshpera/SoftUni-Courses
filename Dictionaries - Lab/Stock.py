elements = input().split()
bakery = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    values = int(elements[i+1])
    bakery[key] = values

products = input().split()

for product in products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

