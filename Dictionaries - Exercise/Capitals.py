countries = input().split(", ")
capitals = input().split(", ")
my_dict = {countries[idx]: capitals[idx] for idx in range(len(countries))}

for key, val in my_dict.items():
    print(f"{key} -> {val}")
