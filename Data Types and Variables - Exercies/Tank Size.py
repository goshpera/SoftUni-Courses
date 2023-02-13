n = int(input())
capacity = 255
filled_space = 0

for i in range(n):
    litres_water = int(input())
    if litres_water < capacity:
        capacity -= litres_water
        filled_space += litres_water
    elif litres_water > capacity:
        print("Insufficent capacity!")
print(filled_space)

