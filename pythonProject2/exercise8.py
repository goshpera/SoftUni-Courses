coffeeCounter = 0
extra = False
while True:
    if coffeeCounter > 5:
        print("You need extra sleep")
        extra = True
        break
    event = input()
    if event == "END":
        if extra is False:
            print(coffeeCounter)
        break
    if event == "dog":
        coffeeCounter += 1
        continue
    if event == "DOG":
        coffeeCounter += 2
        continue
    if event == "cat":
        coffeeCounter += 1
        continue
    if event == "CAT":
        coffeeCounter += 2
        continue
    if event == "coding":
        coffeeCounter += 1
        continue
    if event == "CODING":
        coffeeCounter += 2
        continue
    if event == "movie":
        coffeeCounter += 1
        continue
    if event == "MOVIE":
        coffeeCounter += 2
        continue
    