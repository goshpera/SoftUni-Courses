def calculate(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.5
        return price * quantity
    if product == "water":
        price = 1.0
        return price * quantity
    if product == "coke":
        price = 1.4
        return price * quantity


item = input()
num = int(input())
print(f"{calculate(item, num):.2f}")
print()
