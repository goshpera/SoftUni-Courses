license_plate_username = {}

count = int(input())
for i in range(count):
    command_args = input().split()
    command = command_args[0]
    name = command_args[1]

    if command == "register":
        license_plate = command_args[2]
        if name in license_plate_username:
            print(f"ERROR: already registered with plate number {license_plate_username[name]}")
        else:
            license_plate_username[name] = license_plate
            print(f"{name} registered {license_plate} succesfully")
    else:
        if name in license_plate_username:
            license_plate_username.pop(name)
            print(f"{name} unregistered succesfully")

for key, val in license_plate_username.items():
    print(f"{key} => {val}")
