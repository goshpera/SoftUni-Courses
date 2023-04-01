products_price = {}
products_quantity = {}

while True:
    line = input()
    data = line.split()
    if line == "buy":
        break

    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product in products_price:
        products_price[product] = price
        products_quantity[product] += quantity
    else:
        products_price[product] = price
        products_quantity[product] = quantity

for product in products_price:
    price = products_price[product]
    quantity = products_quantity[product]
    total = price * quantity
    print(f"{product} -> {total:.2f}")
