data_input = input()
products = {}

while data_input != "statistics":
    key, value = data_input.split(": ")
    value = int(value)
    if key not in products:
        products[key] = value
    else:
        products[key] += value
    data_input = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total products: {len(products)}")
print(f"Total products: {sum(products.values())}")
