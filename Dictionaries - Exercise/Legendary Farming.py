special_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

crafting_materials = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk_material = {}
crafted = False

while not crafted:
    line = input()
    data = line.split()

    for idx in range(0, len(data) - 1, 2):
        quantity = int(data[idx])
        material = data[idx + 1].lower()

        if material in special_materials:
            special_materials[material] += quantity
            if special_materials[material] >= 250:
                special_materials[material] -= 250
                crafted = True
                print(f"{crafting_materials[material]} obtained!")
                break
        else:
            if material in junk_material:
                junk_material[material] += quantity
            else:
                junk_material[material] = quantity

for key, val in special_materials.items():
    print(f"{key}: {val}")
for key, val in junk_material.items():
    print(f"{key}: {val}")
