num_orders = int(input())
for i in range(num_orders):
    price = 0
    total = 0
    price_capsule = float(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    days = int(input())
    if days < 1 or days > 31:
        continue
    capsules_per_day = int(input())
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price += price_capsule * capsules_per_day * days
    total += round(price, 2)
    print(f"The price for the coffee is: ${price:.2f}")
    print(f"Total: ${total:.2f}")
